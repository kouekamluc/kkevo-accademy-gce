"""Upper Sixth Accounting (A Level 0705): practice sets for Partnership Accounting; Company Formation, Share Capital &
Debentures; Modification of Capital, Taxation, Amalgamation & Liquidation. One set of eight questions per lesson.

Draft content. All FCFA figures are invented for practice. Cameroon tax rates used (company tax 30% plus 10% additional
council tax, minimum tax 2.2% of turnover, IRCM 16.5%) are TEACHING VALUES to check against the current Finance Law and
your textbook. Every answer and every distractor figure below is computed by this file with plain integer or Fraction
arithmetic (distractors are the results of the typical wrong methods), and the correct option is placed in a balanced
position A-D by a seeded shuffle bag.
"""

import random
from fractions import Fraction as Fr

from .dsl import *  # noqa: F403

COURSE = ("accounting", "upper-sixth")

M_PART = "Partnership Accounting"
M_COMP = "Company Formation, Share Capital & Debentures"
M_MOD = "Modification of Capital, Taxation, Amalgamation & Liquidation"


def n(x):
    if isinstance(x, Fr):
        assert x.denominator == 1, x
        x = int(x)
    assert x == int(x), x
    x = int(x)
    s = f"{abs(x):,}".replace(",", " ")
    return ("-" if x < 0 else "") + s


def split(amount, ratio):
    """Share `amount` in `ratio` exactly (asserts whole francs)."""
    t = sum(ratio)
    out = [Fr(amount * k, t) for k in ratio]
    assert all(x.denominator == 1 for x in out), (amount, ratio)
    return [int(x) for x in out]


def F_(x):
    return f"FCFA {n(x)}"


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
    assert len(wrongs) == 3 and len(concept) <= 80
    texts = [correct] + [t for t, _ in wrongs]
    assert len(set(texts)) == 4, texts
    pos = BAG.next() if pos is None else pos
    choices = [C(t, why=w) for t, w in wrongs]
    choices.insert(pos, C(correct, correct=True))
    return MC(prompt, choices, steps=[S(a, text=b) for a, b in steps], concept=concept, skill=skill, hint=hint)


def NM(prompt, answer, wrongs, steps, concept, skill, hint):
    """A numeric question set as four-option MC. `wrongs` = [(number, why)] x3 (results of typical wrong methods)."""
    return Q(prompt, F_(answer), [(F_(v), w) for v, w in wrongs], steps, concept, skill, hint)


def N(prompt, answer, steps, concept, skill, hint, tol=0, unit="FCFA"):
    assert len(concept) <= 80
    return NUM(prompt, answer, steps=[S(a, text=b) for a, b in steps], tolerance=tol, unit=unit, concept=concept,
               skill=skill, hint=hint)


SETS = []

# ---------------------------------------------------------------- 1. Appropriation of profits and partners' accounts
use(101)
_p1_ioc = [5_000_000 * 8 // 100, 3_000_000 * 8 // 100]
_p1_res = 6_000_000 - sum(_p1_ioc) - 900_000
_p1_a = Fr(_p1_res * 3, 4)
assert _p1_ioc == [400_000, 240_000] and _p1_res == 4_460_000 and _p1_a == 3_345_000
assert Fr((6_000_000 - 640_000) * 3, 4) == 4_020_000 and 6_000_000 * 3 // 4 == 4_500_000 and _p1_res // 2 == 2_230_000
_p1_iod = Fr(400_000 * 12 * 9, 1200) + Fr(800_000 * 12 * 4, 1200) + Fr(600_000 * 12 * 2, 1200)
assert _p1_iod == 36_000 + 32_000 + 12_000 == 80_000
_p1_cur = 250_000 + 300_000 + 1_400_000 - 1_800_000 - 50_000
assert _p1_cur == 100_000 and 250_000 + 300_000 + 1_400_000 - 1_800_000 + 50_000 == 200_000
assert 300_000 + 1_400_000 - 1_800_000 - 50_000 == -150_000 and -250_000 + 300_000 + 1_400_000 - 1_800_000 - 50_000 == -400_000
_p1_g = [Fr(4_000_000 * k, 5) for k in (2, 2, 1)]
assert _p1_g == [1_600_000, 1_600_000, 800_000]
_p1_short = 1_500_000 - 800_000
assert _p1_short == 700_000 and 1_600_000 - _p1_short // 2 == 1_250_000 and 1_600_000 - Fr(_p1_short * 2, 5) == 1_320_000
assert 1_600_000 - _p1_short == 900_000
assert 1_000_000 - 1_200_000 - 600_000 == -800_000

SETS.append(practice_set(
    module=M_PART, topic="Appropriation of profits and partners' accounts",
    title="Appropriation account and partners' current accounts", lesson="acu1-partnership-appropriation",
    questions=[
        Q("Two partners have no written agreement. Using the default rules most textbooks apply (Partnership Act 1890), how are profits shared?",
          "Equally, with no interest on capital and no salaries",
          [("In the ratio of capitals", "Capital ratio is used only if the partners agree it; the default is equal shares."),
           ("Equally, after 5% interest on capital", "The default gives 5% interest on partners' loans, not on capital."),
           ("In the ratio of hours worked", "No default rule rewards work; salaries need an agreement.")],
          [("Default rules", "Without a deed: equal shares of profit and loss, no interest on capital or drawings, no salaries, 5% a year on partners' loans.")],
          "Default rules without a partnership deed", "Recall", "Think of what the partners would get if nothing was written down."),
        Q("Which item is recorded in the income statement and NOT in the appropriation account?",
          "Interest on a loan made to the firm by a partner",
          [("Interest on a partner's capital", "Interest on capital rewards the partner as owner, so it is an appropriation."),
           ("A salary paid to a working partner", "A partner's salary is a share of profit agreed in the deed, so it is an appropriation."),
           ("Interest charged on a partner's drawings", "Interest on drawings is added in the appropriation account.")],
          [("Owner or lender?", "When a partner lends money the firm owes interest like any other lender, so it is an expense before net profit.")],
          "Partner's loan interest is an expense", "Concept", "Ask whether the partner is acting as an owner or as a lender."),
        NM("A and B have capitals of FCFA 5 000 000 and 3 000 000. The deed gives 8% interest on capital, a salary of 900 000 to B, "
           "and residual profit 3:1. Net profit is FCFA 6 000 000. What is A's share of the residual profit?",
           _p1_a,
           [(4_020_000, "The salary of 900 000 was not deducted before sharing."),
            (4_500_000, "This shares the whole net profit, not the residual profit."),
            (2_230_000, "This shares the residual profit equally instead of 3:1.")],
           [("Interest on capital", "8% × 5 000 000 = 400 000; 8% × 3 000 000 = 240 000."),
            ("Residual profit", "6 000 000 − 640 000 − 900 000 = 4 460 000."),
            ("A's share", "3/4 × 4 460 000 = 3 345 000.")],
           "Residual profit after interest on capital and salary", "Calculation",
           "Deduct interest on capital and the salary before sharing."),
        N("A partner's drawings were FCFA 400 000 on 1 April, 800 000 on 1 September and 600 000 on 1 November. The year ends on "
          "31 December and interest on drawings is 12% a year. Find the interest on drawings.",
          int(_p1_iod),
          [("Months outstanding", "1 April: 9 months; 1 September: 4 months; 1 November: 2 months."),
           ("Interest", "400 000 × 12% × 9/12 = 36 000; 800 000 × 12% × 4/12 = 32 000; 600 000 × 12% × 2/12 = 12 000."),
           ("Total", "36 000 + 32 000 + 12 000 = 80 000.")],
          "Interest on dated drawings", "Calculation", "Count the months from each drawing to the year end."),
        Q("A partner's current account opened with a credit balance of FCFA 250 000. During the year: interest on capital 300 000, share of profit "
          "1 400 000, drawings 1 800 000, interest on drawings 50 000. What is the closing balance?",
          "FCFA 100 000 credit",
          [("FCFA 200 000 credit", "Interest on drawings was added instead of being debited."),
           ("FCFA 150 000 debit", "The opening credit balance of 250 000 was left out."),
           ("FCFA 400 000 debit", "The opening balance was treated as a debit balance.")],
          [("Credits", "250 000 + 300 000 + 1 400 000 = 1 950 000."),
           ("Debits", "1 800 000 + 50 000 = 1 850 000."),
           ("Balance", "1 950 000 − 1 850 000 = 100 000 credit: the firm owes the partner 100 000.")],
          "Closing balance of a partner's current account", "Calculation",
          "Put each item on the side where it belongs, then balance."),
        NM("P, Q and R share residual profit 2:2:1. R is guaranteed a residual share of at least FCFA 1 500 000; any shortfall is borne by P and Q "
           "equally. Residual profit is FCFA 4 000 000. What is P's final share?",
           1_250_000,
           [(1_600_000, "This ignores the guarantee given to R."),
            (900_000, "P has borne the whole shortfall alone instead of sharing it with Q."),
            (1_320_000, "The shortfall was shared 2:2:1 among all three partners, including R.")],
           [("Shares before the guarantee", "4 000 000 × 2/5 = 1 600 000 for P and Q; R gets 800 000."),
            ("Shortfall", "1 500 000 − 800 000 = 700 000."),
            ("P bears half", "1 600 000 − 350 000 = 1 250 000.")],
           "Guaranteed minimum profit share", "Application",
           "Find R's normal share first and compare it with the guarantee."),
        Q("E and F share profits equally after interest on capital of FCFA 1 200 000 in total and a salary of 600 000 to F. "
          "Net profit is only FCFA 1 000 000. What is each partner's share of the residual?",
          "A loss of FCFA 400 000 each",
          [("A profit of FCFA 500 000 each", "This shares the net profit without the agreed appropriations."),
           ("A loss of FCFA 100 000 each", "The salary of 600 000 was not deducted."),
           ("Nil: appropriations cannot exceed profit", "The deed's interest and salary are still credited; the shortfall becomes a residual loss.")],
          [("Residual", "1 000 000 − 1 200 000 − 600 000 = −800 000."),
           ("Share equally", "Each partner bears 400 000 of residual loss.")],
          "Residual loss after appropriations", "Reasoning",
          "Appropriations are made even when they exceed the profit."),
        Q("Which statement describes the fluctuating capital method?",
          "Salaries, interest and profit shares are credited, and drawings debited, directly to the capital accounts",
          [("Capital accounts never change after the deed is signed", "That describes the fixed capital method."),
           ("Each partner has both a capital account and a current account", "Current accounts are used with fixed capitals."),
           ("Drawings are recorded in the appropriation account", "Drawings go to the partners' accounts, never to the appropriation account.")],
          [("Fluctuating capital", "There are no current accounts: every appropriation and drawing changes the capital balance, which fluctuates.")],
          "Fixed and fluctuating capital methods", "Concept", "The name tells you what happens to the capital balance."),
    ]))

# ---------------------------------------------------------------- 2. Revaluation and goodwill
use(102)
_p2_rev = 1_500_000 - 600_000 - 200_000 - 100_000
assert _p2_rev == 600_000 and _p2_rev * 3 // 5 == 360_000 and _p2_rev // 2 == 300_000
assert (1_500_000 - 600_000 - 200_000) * 3 // 5 == 420_000 and (1_500_000 - 600_000 - 200_000 + 100_000) * 3 // 5 == 480_000
_p2_avg = Fr(2_800_000 - 400_000 + 3_600_000, 3)
assert _p2_avg == 2_000_000 and _p2_avg * Fr(5, 2) == 5_000_000
_p2_w = Fr(3_000_000 * 1 + 3_600_000 * 2 + 4_200_000 * 3, 6)
assert _p2_w == 3_800_000 and _p2_w * 2 == 7_600_000
assert Fr(3_000_000 + 3_600_000 + 4_200_000, 3) * 2 == 7_200_000 and Fr(3_000_000 * 3 + 3_600_000 * 2 + 4_200_000, 6) * 2 == 6_800_000
_p2_sp = 5_200_000 - 30_000_000 * 12 // 100
assert _p2_sp == 1_600_000 and _p2_sp * 4 == 6_400_000
assert Fr(900_000 * 100, 15) == 6_000_000 and 900_000 * 15 // 100 == 135_000 and 900_000 * 3 == 2_700_000

SETS.append(practice_set(
    module=M_PART, topic="Revaluation and goodwill",
    title="Revaluation account and goodwill valuation", lesson="acu1-revaluation-goodwill",
    questions=[
        Q("When a partnership changes its profit-sharing ratio, in which ratio is the profit on revaluation shared?",
          "The old profit-sharing ratio",
          [("The new profit-sharing ratio", "The gain arose before the change, while the old ratio applied."),
           ("The ratio of capitals", "Capitals are used only if the deed says so; revaluation follows the old ratio."),
           ("Equally among all partners", "Equal sharing applies only if that was the old ratio.")],
          [("Whose gain?", "Values rose or fell while the old partners shared in the old ratio, so they share the result in that ratio.")],
          "Revaluation result shared in the old ratio", "Recall", "When did the change in value happen?"),
        Q("Premises are revalued from FCFA 8 000 000 to 9 500 000. Which entry records this?",
          "Debit premises 1 500 000; credit revaluation account 1 500 000",
          [("Debit revaluation account 1 500 000; credit premises 1 500 000", "That entry records a fall in value."),
           ("Debit premises 9 500 000; credit revaluation account 9 500 000", "Only the increase is recorded, not the new value."),
           ("Debit premises 1 500 000; credit partners' current accounts 1 500 000", "The increase goes first to the revaluation account; only its net balance goes to the partners, and to capital accounts.")],
          [("Increase", "9 500 000 − 8 000 000 = 1 500 000."),
           ("Entry", "The asset account rises (debit) and the gain is credited to the revaluation account.")],
          "Recording an increase in an asset's value", "Application", "An increase in an asset is a debit to that asset."),
        NM("Partners share 3:2 and change to equal shares. On revaluation: land +1 500 000, vehicles −600 000, inventory −200 000 and the allowance "
           "for doubtful debts rises by 100 000. What is the first partner's share of the revaluation result?",
           360_000,
           [(300_000, "The result was shared in the new ratio (equal) instead of the old 3:2."),
            (420_000, "The increase in the allowance was not treated as a loss."),
            (480_000, "The increase in the allowance was treated as a gain.")],
           [("Net result", "1 500 000 − 600 000 − 200 000 − 100 000 = 600 000 profit."),
            ("Old ratio", "3/5 × 600 000 = 360 000.")],
           "Revaluation result and its sharing", "Calculation", "Add the gains, subtract the losses, then use the old ratio."),
        N("Profits were FCFA 2 800 000, a loss of 400 000, and 3 600 000. Goodwill is valued at two and a half years' purchase of the average profit. "
          "Find goodwill.",
          int(_p2_avg * Fr(5, 2)),
          [("Average", "(2 800 000 − 400 000 + 3 600 000) ÷ 3 = 2 000 000."),
           ("Goodwill", "2.5 × 2 000 000 = 5 000 000.")],
          "Goodwill by average profits with a loss year", "Calculation", "A loss is a negative profit in the total."),
        NM("Profits were 3 000 000 (oldest), 3 600 000 and 4 200 000 (latest). Goodwill = 2 years' purchase of the weighted average profit, "
           "weights 1, 2, 3 (latest year heaviest). Find goodwill.",
           int(_p2_w * 2),
           [(7_200_000, "This uses the simple average, not the weighted average."),
            (6_800_000, "The weights were reversed, giving the oldest year the biggest weight."),
            (3_800_000, "This is the weighted average itself; it was not multiplied by the years' purchase.")],
           [("Weighted total", "3 000 000 × 1 + 3 600 000 × 2 + 4 200 000 × 3 = 22 800 000."),
            ("Weighted average", "22 800 000 ÷ 6 = 3 800 000."),
            ("Goodwill", "2 × 3 800 000 = 7 600 000.")],
           "Goodwill by weighted average profits", "Calculation", "Divide by the sum of the weights, not by 3."),
        N("Average profit is FCFA 5 200 000, capital employed 30 000 000 and the normal rate of return 12%. Value goodwill at four years' purchase "
          "of the super profit.",
          _p2_sp * 4,
          [("Normal return", "12% × 30 000 000 = 3 600 000."),
           ("Super profit", "5 200 000 − 3 600 000 = 1 600 000."),
           ("Goodwill", "4 × 1 600 000 = 6 400 000.")],
          "Goodwill by super profits", "Calculation", "Super profit is the excess over the normal return."),
        NM("A firm's super profit is FCFA 900 000 a year and the normal rate of return is 15%. Value goodwill by capitalizing the super profit.",
           6_000_000,
           [(135_000, "The super profit was multiplied by the rate instead of divided by it."),
            (2_700_000, "This is three years' purchase, a different method from capitalization."),
            (1_035_000, "The normal return on the super profit was added to it; capitalization divides by the rate.")],
           [("Capitalization", "Goodwill = super profit ÷ normal rate = 900 000 ÷ 0.15 = 6 000 000.")],
           "Capitalization of super profit", "Calculation", "What capital would earn 900 000 at 15%?"),
        Q("Which is the strongest criticism of valuing goodwill from past profits?",
          "Past profits may not continue after the change in the partnership",
          [("Goodwill can never be sold", "Goodwill can be sold, but only together with the business."),
           ("Average profits are always lower than super profits", "Super profit is part of average profit, so it is usually smaller."),
           ("Goodwill must be shown at cost in the balance sheet", "This is a presentation rule, not a criticism of the valuation method.")],
          [("Evaluation", "Goodwill is a payment for future profits, but the methods use past profits; the key partner or customers may leave.")],
          "Limits of goodwill valuation", "Reasoning", "What does a buyer of goodwill really pay for?"),
    ]))

# ---------------------------------------------------------------- 3. Admission of a partner
use(103)
assert [Fr(2, 3) * Fr(3, 4), Fr(1, 3) * Fr(3, 4), Fr(1, 4)] == [Fr(1, 2), Fr(1, 4), Fr(1, 4)]
assert [Fr(2, 3) - Fr(1, 8), Fr(1, 3) - Fr(1, 8), Fr(1, 4)] == [Fr(13, 24), Fr(5, 24), Fr(6, 24)]
assert [Fr(2, 3) - Fr(1, 4), Fr(1, 3), Fr(1, 4)] == [Fr(5, 12), Fr(4, 12), Fr(3, 12)]
assert [Fr(3, 5) - Fr(3, 5), Fr(2, 5) - Fr(1, 5)] == [0, Fr(1, 5)]
_p3_net = 7_500_000 // 2 - 7_500_000 * 2 // 5
assert _p3_net == 750_000
assert split(900_000, [2, 1]) == [600_000, 300_000]
_p3_cap = 5_000_000 - 6_000_000 // 4
assert _p3_cap == 3_500_000 and 5_000_000 + 6_000_000 // 4 == 6_500_000 and 5_000_000 - 6_000_000 // 3 == 3_000_000
_p3_tot = 12_000_000 + 400_000 + 3_000_000
assert _p3_tot == 15_400_000 and _p3_tot + 4_000_000 == 19_400_000 and 12_000_000 + 3_000_000 == 15_000_000

SETS.append(practice_set(
    module=M_PART, topic="Admission of a partner",
    title="Admitting a partner: ratios, goodwill and capitals", lesson="acu1-admission-of-partner",
    questions=[
        Q("How is an old partner's sacrifice calculated when a new partner is admitted?",
          "Old share minus new share",
          [("New share minus old share", "That is a gain, which is used for a partner whose share increases."),
           ("New partner's share divided equally among old partners", "That is true only if the question says the share is taken equally."),
           ("Old share multiplied by the new partner's share", "This gives the sacrifice only when the share is taken in the old ratio; the general rule is old − new.")],
          [("Rule", "Sacrifice = old share − new share. A positive answer means the partner gives up part of the profits.")],
          "Sacrificing ratio", "Recall", "Compare what the partner had with what he or she will have."),
        Q("P and Q share 2:1. R is admitted for a 1/4 share, which he takes from P and Q in their old ratio. What is the new ratio P:Q:R?",
          "2:1:1",
          [("13:5:6", "This takes R's 1/4 equally from P and Q instead of in the old ratio."),
           ("1:1:1", "This assumes all partners share equally after admission."),
           ("5:4:3", "This takes the whole 1/4 from P alone.")],
          [("Remaining share", "P and Q keep 3/4 of the profits between them."),
           ("New shares", "P: 2/3 × 3/4 = 1/2; Q: 1/3 × 3/4 = 1/4; R: 1/4."),
           ("Ratio", "1/2 : 1/4 : 1/4 = 2:1:1.")],
          "New ratio when a share is taken in the old ratio", "Calculation",
          "Multiply each old share by the fraction that remains for the old partners."),
        Q("A and B share 3:2. C is admitted and the new ratio A:B:C is 3:1:1. Which statement is correct?",
          "B alone gives up 1/5; A gives up nothing",
          [("A and B each give up 1/10", "That would be the case only if C's share was taken equally."),
           ("A gives up 1/5 and B nothing", "A's share stays 3/5; it is B whose share falls from 2/5 to 1/5."),
           ("A and B give up in the ratio 3:2", "Compute old − new for each partner: A's sacrifice is zero.")],
          [("A", "3/5 − 3/5 = 0."), ("B", "2/5 − 1/5 = 1/5, which equals C's share.")],
          "Sacrificing ratio from old and new ratios", "Application", "Write each share as fifths."),
        N("A and B share equally. C joins and the new ratio is 2:2:1. Goodwill of FCFA 7 500 000 is raised and then written off (not kept). "
          "What is the net increase in A's capital from the goodwill entries?",
          _p3_net,
          [("Raised in old ratio", "A is credited 1/2 × 7 500 000 = 3 750 000."),
           ("Written off in new ratio", "A is debited 2/5 × 7 500 000 = 3 000 000."),
           ("Net", "3 750 000 − 3 000 000 = 750 000 (A's sacrifice 1/2 − 2/5 = 1/10 of 7 500 000).")],
          "Net effect of a goodwill adjustment", "Calculation", "Credit in the old ratio, debit in the new ratio."),
        NM("E and F share 2:1. G pays a premium of FCFA 900 000 into the firm for his share of goodwill, taken from E and F in their old ratio. "
           "How much is credited to E's capital?",
           600_000,
           [(450_000, "The premium was shared equally instead of in the sacrificing ratio."),
            (300_000, "This is F's share of the premium."),
            (900_000, "The whole premium was given to one partner.")],
           [("Sacrificing ratio", "The share was taken in the old ratio, so the sacrifice ratio is 2:1."),
            ("E's credit", "2/3 × 900 000 = 600 000.")],
           "Premium for goodwill credited in the sacrificing ratio", "Calculation", "Who gave up the profits, and in what ratio?"),
        NM("A new partner brings FCFA 5 000 000 in cash for a 1/4 share. Goodwill is FCFA 6 000 000 and is not to remain in the books. "
           "What is the new partner's capital after the goodwill entries?",
           _p3_cap,
           [(5_000_000, "The new partner must be debited with his share when goodwill is written off in the new ratio."),
            (6_500_000, "The newcomer's share of goodwill was credited instead of debited."),
            (3_000_000, "Goodwill was written off equally among three partners instead of by the new partner's 1/4 share.")],
           [("Write-off", "The new partner's share of the write-off is 1/4 × 6 000 000 = 1 500 000 (debit)."),
            ("Capital", "5 000 000 − 1 500 000 = 3 500 000.")],
           "New partner's capital after a goodwill write-off", "Calculation",
           "The new partner appears only in the write-off entry."),
        Q("On admission, inventory is written down by FCFA 300 000. Who bears this loss?",
          "The old partners, in the old profit-sharing ratio",
          [("All partners including the new one, in the new ratio", "The fall in value happened before the new partner joined."),
           ("The new partner alone", "The new partner is not responsible for changes in value before admission."),
           ("Nobody: inventory is valued at cost", "On a change in partnership, assets are revalued to agreed values.")],
          [("Revaluation", "The loss is debited to the revaluation account and its balance is shared by the old partners in the old ratio.")],
          "Revaluation losses on admission", "Concept", "When did the value fall?"),
        NM("Old partners' capitals total FCFA 12 000 000. On admission there is a revaluation profit of 400 000; goodwill of 4 000 000 is raised and "
           "written off; the new partner brings 3 000 000 in cash. What is the total of all capitals after admission?",
           _p3_tot,
           [(19_400_000, "Goodwill was raised but not written off; here it is not kept in the books."),
            (15_000_000, "The revaluation profit was left out."),
            (12_400_000, "The new partner's capital of 3 000 000 was left out.")],
           [("Goodwill", "Raised and written off: no net effect on total capital."),
            ("Total", "12 000 000 + 400 000 + 3 000 000 = 15 400 000.")],
           "Total capital after admission", "Reasoning", "Which entries change the total, and which only move capital between partners?"),
    ]))

# ---------------------------------------------------------------- 4. Retirement and death of a partner
use(104)
assert [Fr(1, 2) - Fr(3, 6), Fr(1, 2) - Fr(1, 6)] == [0, Fr(1, 3)]
_p4_due = 6_000_000 - 200_000 + 300_000 + 1_200_000
assert _p4_due == 7_300_000 and 6_000_000 + 200_000 + 300_000 + 1_200_000 == 7_700_000
assert _p4_due - 1_200_000 == 6_100_000 and _p4_due - 300_000 == 7_000_000
assert (4_500_000 - 1_500_000) * 8 // 100 == 240_000
assert Fr(12_000_000 * 5 * 2, 12 * 5) == 2_000_000
_p4_s = Fr(9_000_000 * 7_200_000, 36_000_000)
assert _p4_s == 1_800_000 and _p4_s / 3 == 600_000 and 7_200_000 // 3 == 2_400_000 and _p4_s * 2 / 3 == 1_200_000
_p4_a = 5_000_000 + 600_000 * 3 // 6 + 3_600_000 * 3 // 6 - 3_600_000 * 3 // 5
assert _p4_a == 4_940_000
assert 5_000_000 + 300_000 + 1_800_000 == 7_100_000 and 5_000_000 + 360_000 + 1_800_000 - 2_160_000 == 5_000_000
assert 5_000_000 + 300_000 + 1_800_000 - 1_800_000 == 5_300_000

SETS.append(practice_set(
    module=M_PART, topic="Retirement and death of a partner",
    title="Retirement and death: amounts due and goodwill", lesson="acu1-retirement-death",
    questions=[
        Q("A partner retires. Goodwill is valued but is not to remain in the books. Who is debited when goodwill is written off?",
          "The continuing partners, in their new profit-sharing ratio",
          [("All partners including the retiring one, in the old ratio", "The old ratio is used to credit goodwill, not to write it off."),
           ("The retiring partner alone", "The retiring partner is paid for goodwill; he or she is not charged for it."),
           ("Nobody: goodwill is shown as an asset", "The question says goodwill is not to remain in the books.")],
          [("Raise", "Credit all old partners (including the retiring one) in the old ratio."),
           ("Write off", "Debit the continuing partners in their new ratio; the net effect charges them for the share they gain.")],
          "Goodwill adjustment on retirement", "Recall", "Who stays in the firm and enjoys the goodwill afterwards?"),
        Q("A, B and C share 3:2:1. B retires; A and C continue sharing equally. Which statement about the gain is correct?",
          "C alone gains 1/3; A gains nothing",
          [("A and C gain equally", "Compute new − old for each: A's share stays 1/2."),
           ("A and C gain in the ratio 3:1", "That is their old ratio, not their gain."),
           ("A gains 1/3 and C gains nothing", "The gains are the other way round.")],
          [("A", "New 1/2 − old 3/6 = 0."), ("C", "New 1/2 − old 1/6 = 1/3, which equals B's old share.")],
          "Gaining ratio on retirement", "Calculation", "Write the old shares as sixths."),
        NM("A retiring partner has capital FCFA 6 000 000 and a current account with a DEBIT balance of 200 000. His share of revaluation profit is "
           "300 000 and his share of goodwill 1 200 000. How much is due to him?",
           _p4_due,
           [(7_700_000, "The debit balance on the current account was added instead of deducted."),
            (6_100_000, "His share of goodwill was left out."),
            (7_000_000, "His share of revaluation profit was left out.")],
           [("Add credits", "6 000 000 + 300 000 + 1 200 000 = 7 500 000."),
            ("Deduct the debit balance", "7 500 000 − 200 000 = 7 300 000.")],
           "Amount due to a retiring partner", "Calculation", "A debit balance on the current account is money the partner owes the firm."),
        N("FCFA 4 500 000 due to a retired partner is kept as a loan at 8% a year on the balance outstanding, repaid by 1 500 000 at the end of each year. "
          "Find the interest charged in the SECOND year.",
          240_000,
          [("Balance in year 2", "4 500 000 − 1 500 000 = 3 000 000."),
           ("Interest", "8% × 3 000 000 = 240 000, an expense of the firm.")],
          "Interest on a retired partner's loan", "Calculation", "Interest is on the balance outstanding during that year."),
        N("A partner with a 2/5 share died on 31 May. The year ends on 31 December and profit to the date of death is time-apportioned from last year's "
          "profit of FCFA 12 000 000. Find the partner's share of profit to the date of death.",
          2_000_000,
          [("Months", "1 January to 31 May is 5 months."),
           ("Profit to date", "12 000 000 × 5/12 = 5 000 000."),
           ("Share", "2/5 × 5 000 000 = 2 000 000.")],
          "Profit to the date of death (time basis)", "Calculation", "Count the months from the start of the year."),
        NM("A partner with a 1/3 share died. Sales to the date of death were FCFA 9 000 000. Last year's sales were 36 000 000 and net profit 7 200 000. "
           "Using the sales basis, find the partner's share of profit to the date of death.",
           600_000,
           [(1_800_000, "This is the whole firm's profit to the date of death, not the partner's share."),
            (2_400_000, "This is a full year's share of last year's profit."),
            (1_200_000, "This is the other partners' 2/3 share, not the dead partner's 1/3.")],
           [("Profit to date", "9 000 000 × 7 200 000 ÷ 36 000 000 = 1 800 000 (a 20% margin on sales)."),
            ("Share", "1/3 × 1 800 000 = 600 000.")],
           "Profit to the date of death (sales basis)", "Calculation", "Use last year's ratio of profit to sales."),
        Q("Part of the amount due to a dead partner remains unpaid at the year end. How is it shown?",
          "As a liability: the balance on the executors' account",
          [("As part of the continuing partners' capital", "The dead partner's capital was closed by transfer to the executors' account."),
           ("As an appropriation of profit", "It is an amount owed, not a share of this year's profit."),
           ("As an asset of the firm", "The firm owes the amount to the executors, so it is a liability.")],
          [("Executors' account", "Debit the dead partner's capital, credit the executors' account; any unpaid balance is a liability, and interest on it is an expense.")],
          "Executors' account", "Concept", "Who owes whom?"),
        NM("A, B and C share 3:2:1. C retires and A and B continue 3:2. Revaluation profit is 600 000; goodwill 3 600 000 is raised and written off. "
           "A's capital was FCFA 5 000 000. What is A's capital after these adjustments?",
           _p4_a,
           [(7_100_000, "Goodwill was raised but not written off."),
            (5_000_000, "The revaluation profit was shared in the new ratio 3:2 instead of the old 3:2:1."),
            (5_300_000, "Goodwill was written off in the old ratio, which cancels the adjustment.")],
           [("Revaluation", "3/6 × 600 000 = 300 000."),
            ("Goodwill raised (old ratio)", "3/6 × 3 600 000 = 1 800 000."),
            ("Goodwill written off (new ratio)", "3/5 × 3 600 000 = 2 160 000."),
            ("Capital", "5 000 000 + 300 000 + 1 800 000 − 2 160 000 = 4 940 000.")],
           "Continuing partner's capital after retirement", "Application", "Old ratio for revaluation and raising goodwill; new ratio for writing it off."),
    ]))

# ---------------------------------------------------------------- 5. Dissolution of a partnership
use(105)
_p5_loss = (10_000_000 + 400_000) - (8_600_000 + 900_000 + 100_000)
assert _p5_loss == 800_000
assert (10_000_000 + 400_000) - (8_600_000 + 100_000) == 1_700_000 and 10_000_000 - (8_600_000 + 900_000 + 100_000) == 400_000
assert (10_000_000 + 400_000 + 100_000) - (8_600_000 + 900_000) == 1_000_000
assert 6_500_000 - 1_200_000 - 800_000 == 4_500_000
assert split(480_000, [5, 3]) == [300_000, 180_000] and 480_000 // 2 == 240_000
_p5_fin = 3_000_000 - 200_000 + 500_000 * 3 // 5 - 1_000_000
assert _p5_fin == 2_100_000 and 3_000_000 - 200_000 + 300_000 == 3_100_000
assert 3_000_000 + 200_000 + 300_000 - 1_000_000 == 2_500_000 and 3_000_000 - 200_000 - 300_000 - 1_000_000 == 1_500_000

SETS.append(practice_set(
    module=M_PART, topic="Dissolution of a partnership",
    title="Dissolution: realisation, settlement and an insolvent partner", lesson="acu1-dissolution",
    questions=[
        Q("On dissolution, which balance is NOT transferred to the realisation account?",
          "Bank (cash at bank)",
          [("Inventory", "Inventory is sold, so it goes to the realisation account."),
           ("Receivables", "Receivables are collected, possibly for less than book value, so they go to realisation."),
           ("Premises", "Premises are sold or taken over, so they go to realisation.")],
          [("Rule", "Cash is already in money form; it stays in the bank account, which receives the proceeds and makes the payments.")],
          "Realisation account contents", "Recall", "Which asset does not need to be turned into money?"),
        Q("A partner takes over office equipment at an agreed value of FCFA 700 000. Which entry is correct?",
          "Debit the partner's capital 700 000; credit realisation 700 000",
          [("Debit realisation 700 000; credit the partner's capital 700 000", "That would increase what the firm owes the partner although he received an asset."),
           ("Debit bank 700 000; credit realisation 700 000", "No cash is received when a partner takes an asset."),
           ("Debit the partner's capital 700 000; credit office equipment 700 000", "The equipment's book value was already moved to the realisation account.")],
          [("Value received", "The partner receives an asset, so his claim on the firm falls: debit capital."),
           ("Realisation", "The agreed value is credited to realisation, like sale proceeds.")],
          "Asset taken over by a partner", "Application", "Is the partner receiving or giving value?"),
        NM("Assets other than bank with a book value of FCFA 10 000 000 are realised: sales bring 8 600 000 and a partner takes an asset at 900 000. "
           "Creditors allow a discount of 100 000 and dissolution costs are 400 000. What is the loss on realisation?",
           _p5_loss,
           [(1_700_000, "The asset taken by the partner was not credited to realisation."),
            (400_000, "The dissolution costs were not debited."),
            (1_000_000, "The discount from creditors was treated as a loss instead of a gain.")],
           [("Debits", "10 000 000 + 400 000 = 10 400 000."),
            ("Credits", "8 600 000 + 900 000 + 100 000 = 9 600 000."),
            ("Loss", "10 400 000 − 9 600 000 = 800 000.")],
           "Loss on realisation", "Calculation", "List what is debited and what is credited to realisation."),
        Q("On dissolution, which is paid LAST?",
          "The partners' capital balances",
          [("Trade payables", "Outside creditors are paid first."),
           ("Dissolution costs", "Costs are paid with the creditors, before partners."),
           ("A loan made to the firm by a partner", "Partners' loans are repaid before capital.")],
          [("Order", "Creditors and costs, then partners' loans, then partners' capitals.")],
          "Order of payment on dissolution", "Recall", "Owners are paid after lenders."),
        N("After all assets are realised the firm has FCFA 6 500 000 at the bank. It owes trade payables 1 200 000 and a partner's loan of 800 000. "
          "How much cash is left to settle the partners' capital accounts?",
          4_500_000,
          [("Creditors", "6 500 000 − 1 200 000 = 5 300 000."),
           ("Partner's loan", "5 300 000 − 800 000 = 4 500 000 for capitals.")],
          "Cash available for partners' capitals", "Calculation", "Pay outside creditors and loans first."),
        NM("X and Y are solvent; Z is insolvent with a capital deficiency of FCFA 480 000. Profits were shared equally. The last agreed capitals of X "
           "and Y were 5 000 000 and 3 000 000. Under Garner v Murray, how much of the deficiency does X bear?",
           300_000,
           [(240_000, "This uses the equal profit-sharing ratio; the rule uses last agreed capitals."),
            (180_000, "This is Y's share of the deficiency."),
            (480_000, "The deficiency is shared between the two solvent partners, not borne by one.")],
           [("Ratio", "Last agreed capitals 5 000 000 : 3 000 000 = 5:3."),
            ("X's share", "5/8 × 480 000 = 300 000.")],
           "Garner v Murray", "Application", "The rule uses the ratio of capitals, not profits."),
        NM("A partner's capital is FCFA 3 000 000 (credit) and his current account has a debit balance of 200 000. His share of the realisation profit "
           "of 500 000 is 3/5, and he took over a vehicle valued at 1 000 000. How much cash does he receive on final settlement?",
           _p5_fin,
           [(3_100_000, "The vehicle he took was not deducted."),
            (2_500_000, "The debit balance on the current account was added instead of deducted."),
            (1_500_000, "His share of the realisation profit was deducted as if it were a loss.")],
           [("Credits", "3 000 000 + 300 000 (3/5 × 500 000) = 3 300 000."),
            ("Debits", "200 000 (current account) + 1 000 000 (vehicle) = 1 200 000."),
            ("Cash", "3 300 000 − 1 200 000 = 2 100 000.")],
           "Final settlement of a partner", "Calculation", "Combine capital and current account, then take off what he received in kind."),
        Q("Creditors of FCFA 2 000 000 are settled for 1 940 000 on dissolution. How is the difference recorded?",
          "Credit realisation account 60 000 (a gain)",
          [("Debit realisation account 60 000 (a loss)", "Paying less than the amount owed is a gain, not a loss."),
           ("Credit the partners' current accounts 60 000", "The gain passes through the realisation account first."),
           ("No entry: only cash paid is recorded", "The creditors' balance of 2 000 000 must be fully closed, so the difference is recorded.")],
          [("Discount received", "Debit creditors 2 000 000, credit bank 1 940 000 and credit realisation 60 000.")],
          "Discount from creditors on dissolution", "Concept", "Is paying less than you owe good or bad for the partners?"),
    ]))

# ---------------------------------------------------------------- 6. Company formation under OHADA
use(106)
assert 600 * 10_000 // 4 == 1_500_000 and 600 * 10_000 == 6_000_000 and 600 * 10_000 // 2 == 3_000_000 and 600 * 10_000 // 10 == 600_000
_p6_unc = 2_000 * 10_000 * 3 // 4
assert _p6_unc == 15_000_000 and 2_000 * 10_000 == 20_000_000 and 30_000_000 - 30_000_000 // 4 == 22_500_000 and 2_000 * 10_000 // 4 == 5_000_000

SETS.append(practice_set(
    module=M_COMP, topic="Company formation under OHADA",
    title="OHADA company forms and the capital accounts", lesson="acu1-company-formation-ohada",
    questions=[
        Q("Under the OHADA Uniform Act on commercial companies, what is the minimum share capital of an SA?",
          "FCFA 10 000 000",
          [("FCFA 1 000 000", "This is the SARL default in the Act, which member states may change."),
           ("FCFA 100 000", "No such minimum is set for an SA."),
           ("No minimum: the statutes decide", "Freedom to fix capital applies to the SAS, not to the SA.")],
          [("Rule", "The SA minimum capital in the Uniform Act is FCFA 10 000 000.")],
          "Minimum capital of an SA", "Recall", "It is ten times the SARL default figure."),
        NM("A shareholder subscribes 600 cash shares of nominal value FCFA 10 000 in a new SA. What is the minimum amount he must pay on subscription?",
           1_500_000,
           [(6_000_000, "This is the full nominal value, which may be paid within three years."),
            (3_000_000, "This is half the nominal value; the minimum is one quarter."),
            (600_000, "This is one tenth; the rule is one quarter.")],
           [("Nominal value", "600 × 10 000 = 6 000 000."),
            ("At least one quarter", "6 000 000 ÷ 4 = 1 500 000.")],
           "Minimum payment on cash shares", "Calculation", "The Act requires at least a quarter of nominal value of cash shares."),
        Q("Within what period must the unpaid part of cash shares in an SA be paid?",
          "Three years from registration",
          [("One year", "The Act allows longer than one year."),
           ("Five years", "The limit is shorter than five years."),
           ("Whenever the shareholder wishes", "The board calls the balance and the Act sets a time limit.")],
          [("Rule", "The balance of cash shares is paid on calls by the board within three years.")],
          "Time limit for calling capital", "Recall", "It is a short number of years."),
        Q("When does a new SA become a legal person?",
          "On registration in the RCCM",
          [("When the statutes are signed", "Signing is an early step; legal personality comes later."),
           ("When the first quarter is paid in", "Payment is required, but personality comes from registration."),
           ("When the first accounts are approved", "The company exists as a legal person long before its first accounts.")],
          [("Registration", "Registration in the Registre du Commerce et du Crédit Mobilier gives the company legal personality.")],
          "Legal personality of a company", "Recall", "Think of the trade and personal property credit register."),
        Q("In which OHADA company form are the members personally liable, jointly and severally, for all its debts?",
          "SNC (société en nom collectif)",
          [("SARL", "SARL partners are liable only up to their contributions."),
           ("SA", "SA shareholders are liable only up to their contributions."),
           ("SAS", "SAS shareholders are liable only up to their contributions.")],
          [("SNC", "The partners of an SNC are traders with unlimited joint and several liability.")],
          "Liability in OHADA company forms", "Concept", "Which form is the general partnership?"),
        Q("Which SYSCOHADA account shows capital that has been called AND paid?",
          "1013",
          [("1011", "1011 is capital subscribed but not yet called."),
           ("1012", "1012 is capital called but not yet paid."),
           ("109", "109 records what contributors owe on capital not yet called.")],
          [("Stages", "1011 uncalled → 1012 called, unpaid → 1013 called and paid.")],
          "Status of capital in SYSCOHADA", "Recall", "The last of the three stages."),
        NM("An SA is formed with capital FCFA 30 000 000: 1 000 shares of 10 000 issued for land, and 2 000 cash shares of 10 000 with one quarter called "
           "on subscription. How much is credited to 1011 (capital uncalled) at subscription?",
           _p6_unc,
           [(20_000_000, "This treats all the cash capital as uncalled, ignoring the quarter called."),
            (22_500_000, "The quarter was applied to the whole capital, including the land shares that are fully paid."),
            (5_000_000, "This is the cash called now, not the uncalled part.")],
           [("Cash capital", "2 000 × 10 000 = 20 000 000."),
            ("Called now", "20 000 000 ÷ 4 = 5 000 000."),
            ("Uncalled", "20 000 000 − 5 000 000 = 15 000 000. The land shares (10 000 000) are fully paid.")],
           "Capital uncalled at formation", "Application", "Shares issued for assets are fully paid at once."),
        Q("Who values a contribution in kind (for example a building) when an SA is formed?",
          "An independent auditor of contributions (commissaire aux apports)",
          [("The contributor himself", "The person contributing the asset could overvalue it, so an independent valuation is required."),
           ("The tax administration", "Tax officials do not value contributions for the company's capital."),
           ("The bank that receives the cash", "The bank receives cash contributions, not assets.")],
          [("Protection", "An independent auditor checks that shares are not issued for assets worth less than their nominal value, protecting other shareholders and creditors.")],
          "Valuation of contributions in kind", "Concept", "Who protects the other shareholders from an overvalued asset?"),
    ]))

# ---------------------------------------------------------------- 7. Issue of shares
use(107)
assert 1_000 * (2_500 + 4_000) == 6_500_000 and 1_000 * 2_500 == 2_500_000 and 1_000 * 4_000 == 4_000_000 and 1_000 * (2_500 + 1_000) == 3_500_000
assert 4_000 * (11_200 - 10_000) == 4_800_000
_p7_bank = 5_000 * 2_000 - 300 * 2_000 + 150_000
assert _p7_bank == 9_550_000 and 10_000_000 - 600_000 == 9_400_000 and 10_000_000 + 150_000 == 10_150_000
_p7_ref = 1_200_000 - 900_000 - 25_000 - 35_000
assert _p7_ref == 240_000 and 1_200_000 - 900_000 == 300_000 and 1_200_000 - 900_000 - 25_000 == 275_000
_p7_res = 200 * 7_000 - 200 * (10_000 - 9_000)
assert _p7_res == 1_200_000

SETS.append(practice_set(
    module=M_COMP, topic="Issue of shares",
    title="Premiums, calls and defaulting shareholders", lesson="acu1-issue-of-shares",
    questions=[
        Q("What is a share premium?",
          "The excess of the issue price over the nominal value of a share",
          [("The excess of the market price over the issue price", "That gain belongs to the buyer on the market, not to the company."),
           ("The part of nominal value not yet called", "That is uncalled capital."),
           ("A bonus paid by the company to new shareholders", "The premium is paid BY the subscriber TO the company.")],
          [("Definition", "Premium = issue price − nominal value, credited to 1051; it is not capital.")],
          "Share premium", "Recall", "Compare what the subscriber pays with the face value."),
        NM("An SA issues 1 000 shares of nominal value FCFA 10 000 at 14 000. What is the minimum cash it receives on subscription?",
           6_500_000,
           [(2_500_000, "The premium was left out; it must be paid in full on subscription."),
            (4_000_000, "This is the premium only; at least a quarter of nominal is also paid."),
            (3_500_000, "Only a quarter of the premium was included; the whole premium is due.")],
           [("Per share", "Quarter of nominal 2 500 + premium 4 000 = 6 500."),
            ("Total", "1 000 × 6 500 = 6 500 000.")],
           "Minimum payment on an issue at a premium", "Calculation", "Quarter of the nominal value plus the whole premium."),
        N("4 000 shares of nominal value FCFA 10 000 are issued at 11 200. Find the total share premium.",
          4_800_000,
          [("Premium per share", "11 200 − 10 000 = 1 200."), ("Total", "4 000 × 1 200 = 4 800 000, credited to 1051.")],
          "Total share premium", "Calculation", "Premium per share times the number of shares."),
        NM("A call of FCFA 2 000 per share is made on 5 000 shares. A holder of 300 shares pays nothing; another shareholder also pays 150 000 for a future "
           "call. How much does the bank receive?",
           _p7_bank,
           [(10_000_000, "Neither the arrears nor the payment in advance was taken into account."),
            (9_400_000, "The payment in advance was left out."),
            (10_150_000, "The arrears of 600 000 were not deducted.")],
           [("Called", "5 000 × 2 000 = 10 000 000."),
            ("Arrears", "300 × 2 000 = 600 000 not received."),
            ("Bank", "10 000 000 − 600 000 + 150 000 = 9 550 000.")],
           "Cash received on a call", "Calculation", "Start with the amount called; adjust for arrears and advances."),
        Q("A shareholder pays an amount before the board has called it. Which account is credited?",
          "4616 Payments in advance (versements anticipés)",
          [("1013 Capital called and paid", "The money cannot be capital paid until the call is made."),
           ("4617 Defaulting shareholders", "That account is for shareholders who have not paid."),
           ("1051 Share premium", "Premium is the excess of issue price over nominal value, not an early payment.")],
          [("Liability", "Until the call, the company owes this money back to the shareholder, so 4616 is a liability.")],
          "Calls in advance", "Concept", "Has the company asked for the money yet?"),
        NM("A defaulting shareholder owes a call of FCFA 900 000, interest for late payment of 25 000, and sale costs of 35 000. His shares are sold for "
           "1 200 000. How much is refunded to him?",
           _p7_ref,
           [(300_000, "The interest and the costs of sale were not deducted."),
            (275_000, "The costs of sale were not deducted."),
            (1_200_000, "The company keeps what the shareholder owes; only the surplus is refunded.")],
           [("Owed", "900 000 + 25 000 + 35 000 = 960 000."),
            ("Refund", "1 200 000 − 960 000 = 240 000.")],
           "Sale of a defaulting shareholder's shares", "Calculation", "Deduct everything he owes from the proceeds."),
        Q("A defaulter's shares are sold for less than he owes the company. What is the result?",
          "The shortfall remains a debt that he still owes the company",
          [("The company writes off the shortfall as a capital loss", "The shareholder remains liable for what he owes."),
           ("The buyer of the shares must pay the shortfall", "The buyer pays only the agreed price."),
           ("The capital is reduced by the shortfall", "Capital is not reduced; the debt remains in 4617.")],
          [("4617", "After the proceeds are credited, a debit balance stays on 4617: the shareholder's continuing debt.")],
          "Shortfall on sale of defaulter's shares", "Reasoning", "Does the sale cancel his debt?"),
        N("English method: 200 shares of nominal value FCFA 10 000, fully called, are forfeited after the holder had paid 7 000 per share. They are reissued "
          "fully paid at 9 000 each. Find the amount transferred to capital reserve.",
          _p7_res,
          [("Forfeited shares account", "Credited with the amount paid: 200 × 7 000 = 1 400 000."),
           ("Discount on reissue", "200 × (10 000 − 9 000) = 200 000 debited."),
           ("Capital reserve", "1 400 000 − 200 000 = 1 200 000.")],
          "Forfeiture and reissue (English method)", "Application", "What the old holder paid, less the discount given on reissue."),
    ]))

# ---------------------------------------------------------------- 8. Appropriation of company profits
use(108)
_p8_lr = min((7_000_000 - 1_000_000) // 10, 25_000_000 // 5 - 4_200_000)
assert _p8_lr == 600_000 and 25_000_000 // 5 - 4_200_000 == 800_000 and 7_000_000 // 10 == 700_000
_p8_cap = min(4_000_000 // 10, 15_000_000 // 5 - 2_800_000)
assert _p8_cap == 200_000
_p8_dist = 10_000_000 - 1_000_000 - 450_000 + 250_000
assert _p8_dist == 8_800_000 and 10_000_000 - 1_000_000 + 250_000 == 9_250_000
assert 10_000_000 - 1_000_000 - 450_000 - 250_000 == 8_300_000 and 10_000_000 + 250_000 == 10_250_000
_p8_fd = 3_000 * 10_000 * 5 // 100 + 1_000 * 5_000 * 5 // 100
assert _p8_fd == 1_750_000 and 4_000 * 500 == 2_000_000 and 3_000 * 500 == 1_500_000 and 1_500_000 + 1_000 * 125 == 1_625_000
_p8_ps = (9_870_000 // 6_000) // 50 * 50
assert 9_870_000 // 6_000 == 1_645 and _p8_ps == 1_600 and 9_870_000 - _p8_ps * 6_000 == 270_000
_p8_net = 3_000 * 2_000 * 835 // 1000
assert _p8_net == 5_010_000 and 6_000_000 * 165 // 1000 == 990_000 and 6_000_000 * 90 // 100 == 5_400_000

SETS.append(practice_set(
    module=M_COMP, topic="Appropriation of company profits",
    title="Legal reserve, distributable profit and dividends", lesson="acu1-company-profit-appropriation",
    questions=[
        Q("Under the OHADA Uniform Act, what is the rule for the legal reserve?",
          "At least 10% of the profit (less losses brought forward) until the reserve reaches 20% of the capital",
          [("5% of the profit until the reserve reaches 10% of the capital", "Both figures are too low: the Act says one tenth and one fifth."),
           ("10% of the profit every year without limit", "The allocation stops being compulsory at one fifth of the capital."),
           ("20% of the profit until the reserve equals the capital", "The rate is one tenth and the ceiling one fifth of capital.")],
          [("Rule", "One tenth of the profit of the year, minus losses brought forward, until the legal reserve reaches one fifth of the share capital.")],
          "Legal reserve rule", "Recall", "One tenth ... one fifth."),
        NM("Capital FCFA 25 000 000; legal reserve 4 200 000; profit for the year 7 000 000; losses brought forward 1 000 000. What is the legal reserve allocation?",
           _p8_lr,
           [(700_000, "The losses brought forward were not deducted before taking 10%."),
            (800_000, "This is the room left below the ceiling, which is larger than 10% of the base."),
            (5_000_000, "This is the ceiling (20% of capital), not the allocation.")],
           [("Base", "7 000 000 − 1 000 000 = 6 000 000; 10% = 600 000."),
            ("Ceiling", "20% × 25 000 000 = 5 000 000; room = 800 000."),
            ("Allocation", "The smaller: 600 000.")],
           "Legal reserve with prior losses", "Calculation", "Deduct losses brought forward, then compare with the room left."),
        N("Capital FCFA 15 000 000; legal reserve 2 800 000; profit for the year 4 000 000 with no prior losses. Find the legal reserve allocation.",
          _p8_cap,
          [("10% of profit", "400 000."), ("Room left", "20% × 15 000 000 = 3 000 000; 3 000 000 − 2 800 000 = 200 000."),
           ("Allocation", "The smaller amount: 200 000.")],
          "Legal reserve ceiling", "Calculation", "How far is the reserve from one fifth of capital?"),
        NM("Profit for the year FCFA 10 000 000; legal reserve allocation 1 000 000; statutory reserve 450 000; profit brought forward 250 000 (credit). "
           "Find the distributable profit.",
           _p8_dist,
           [(9_250_000, "The statutory reserve was not deducted."),
            (8_300_000, "The profit brought forward was deducted instead of added."),
            (10_250_000, "The legal and statutory reserves were not deducted.")],
           [("Formula", "Profit − legal and statutory reserves + profit brought forward."),
            ("Result", "10 000 000 − 1 000 000 − 450 000 + 250 000 = 8 800 000.")],
           "Distributable profit", "Calculation", "Reserves required by law and statutes come off; profit brought forward is added."),
        NM("3 000 shares of 10 000 are fully paid and 1 000 shares are half paid. The first dividend is 5% of the amount paid up. Find the total first dividend.",
           _p8_fd,
           [(2_000_000, "The 5% was applied to the full nominal value of all shares."),
            (1_500_000, "The partly paid shares were left out; they earn 5% on what is paid."),
            (1_625_000, "The partly paid shares were treated as paid by one quarter instead of one half.")],
           [("Fully paid", "3 000 × 5% × 10 000 = 1 500 000."),
            ("Half paid", "1 000 × 5% × 5 000 = 250 000."),
            ("Total", "1 750 000.")],
           "First dividend on paid-up capital", "Calculation", "The first dividend is interest on the amount actually paid."),
        N("After the first dividend and reserves, FCFA 9 870 000 is available for a super dividend on 6 000 shares, rounded down to the nearest 50 francs per share. "
          "How much is carried forward?",
          270_000,
          [("Per share", "9 870 000 ÷ 6 000 = 1 645; rounded down to a multiple of 50 gives 1 600."),
           ("Super dividend", "1 600 × 6 000 = 9 600 000."),
           ("Carried forward", "9 870 000 − 9 600 000 = 270 000 (to 121).")],
          "Super dividend rounding and profit carried forward", "Calculation", "Round the amount per share DOWN, then multiply back."),
        NM("A company declares a gross dividend of FCFA 3 000 per share on 2 000 shares. Using a teaching IRCM rate of 16.5%, how much do shareholders receive in total?",
           _p8_net,
           [(6_000_000, "This is the gross dividend; the tax is withheld before payment."),
            (990_000, "This is the tax withheld, not the net dividend."),
            (5_400_000, "A 10% rate was used instead of the 16.5% teaching rate.")],
           [("Gross", "3 000 × 2 000 = 6 000 000."),
            ("IRCM", "16.5% × 6 000 000 = 990 000 (paid to the State)."),
            ("Net", "6 000 000 − 990 000 = 5 010 000.")],
           "Net dividend after IRCM (teaching rate)", "Application", "The company keeps the tax and pays it to the State."),
        Q("Which reserve is decided freely by the ordinary general meeting, without any legal or statutory requirement?",
          "An optional (free) reserve",
          [("The legal reserve", "The legal reserve is required by the Uniform Act."),
           ("The statutory reserve", "The statutory reserve is required by the company's own statutes."),
           ("The share premium", "The share premium comes from issuing shares above nominal value, not from profit.")],
          [("Optional reserve", "Account 118: the meeting may choose to keep part of the distributable profit in the company.")],
          "Types of reserves", "Concept", "Which reserve has no rule forcing it?"),
    ]))

# ---------------------------------------------------------------- 9. Debentures
use(109)
assert 8_000 * 10_000 * 9 // 100 == 7_200_000 and 8_000 * 9_700 * 9 // 100 == 6_984_000
assert 8_000 * 10_300 * 9 // 100 == 7_416_000 and 8_000 * (10_300 - 9_700) == 4_800_000
assert 6_000 * (10_100 - 9_600) == 3_000_000
assert 4_000 * 9_850 == 39_400_000 and 4_000 * 10_200 == 40_800_000 and 4_000 * (10_200 - 9_850) == 1_400_000
assert 3_000 * 10_000 * 10 // 100 + 1_000 * 10_000 == 13_000_000
_p9_a = round(20_000_000 * 0.1 / (1 - 1.1 ** -4))
assert _p9_a == 6_309_416 and 20_000_000 // 4 + 2_000_000 == 7_000_000
assert 30_000_000 * 10 * 9 // (100 * 12) == 2_250_000

SETS.append(practice_set(
    module=M_COMP, topic="Debentures",
    title="Bond loans: interest, premium and redemption", lesson="acu1-debentures",
    questions=[
        Q("Which statement about bondholders (debenture holders) is correct?",
          "They are creditors entitled to interest whether or not the company makes a profit",
          [("They are owners who vote at general meetings", "Bondholders lend money; only shareholders vote."),
           ("They receive dividends out of distributable profit", "Dividends go to shareholders; bondholders receive interest."),
           ("They are repaid after shareholders on liquidation", "Creditors, including bondholders, are paid before shareholders.")],
          [("Lenders", "A bond is a loan contract: interest is an expense and repayment is a legal debt.")],
          "Bondholders are creditors", "Recall", "Lender or owner?"),
        NM("8 000 bonds of nominal value FCFA 10 000 carry interest at 9%. They were issued at 9 700 and are redeemable at 10 300. What is the yearly interest?",
           7_200_000,
           [(6_984_000, "Interest was calculated on the issue price."),
            (7_416_000, "Interest was calculated on the redemption price."),
            (4_800_000, "This is the total redemption premium, not the interest.")],
           [("Base", "Nominal value: 8 000 × 10 000 = 80 000 000."), ("Interest", "9% × 80 000 000 = 7 200 000.")],
           "Bond interest on nominal value", "Calculation", "Interest always uses the face value."),
        N("6 000 bonds are issued at FCFA 9 600 and are redeemable at 10 100. Find the total redemption premium.",
          3_000_000,
          [("Per bond", "10 100 − 9 600 = 500."), ("Total", "6 000 × 500 = 3 000 000.")],
          "Bond redemption premium", "Calculation", "Redemption price minus issue price."),
        NM("4 000 bonds of nominal value 10 000 are issued at 9 850, redeemable at 10 200. How much cash does the company receive?",
           39_400_000,
           [(40_000_000, "This uses the nominal value; subscribers pay the issue price."),
            (40_800_000, "This is the amount the company will repay, not the cash received."),
            (1_400_000, "This is the redemption premium.")],
           [("Cash", "4 000 × 9 850 = 39 400 000.")],
           "Cash raised by a bond issue", "Calculation", "Subscribers pay the issue price."),
        N("5 000 bonds of nominal value FCFA 10 000 at 10% are redeemed at par, 1 000 bonds at the end of each year. Find the annuity paid in year 3.",
          13_000_000,
          [("Bonds outstanding in year 3", "5 000 − 2 × 1 000 = 3 000."),
           ("Interest", "3 000 × 10 000 × 10% = 3 000 000."),
           ("Repayment", "1 000 × 10 000 = 10 000 000."),
           ("Annuity", "3 000 000 + 10 000 000 = 13 000 000.")],
          "Annuity with equal redemptions", "Calculation", "How many bonds are still outstanding during year 3?"),
        NM("A loan of FCFA 20 000 000 at 10% is repaid by a constant annuity over 4 years, using a = C × i ÷ (1 − (1 + i)^−n). Find the annuity (to the nearest franc).",
           _p9_a,
           [(5_000_000, "This is only the capital divided by 4, without interest."),
            (7_000_000, "This adds a full year's interest on the whole loan to C ÷ 4; the annuity formula spreads interest differently."),
            (2_000_000, "This is the first year's interest only.")],
           [("Factor", "0.1 ÷ (1 − 1.1^−4) = 0.1 ÷ 0.316987 ≈ 0.315471."),
            ("Annuity", "20 000 000 × 0.315471 ≈ 6 309 416.")],
           "Constant annuity formula", "Calculation", "Work out 1.1 to the power −4 first."),
        N("A bond loan of FCFA 30 000 000 at 10% pays interest every 31 March. The year ends on 31 December. Find the interest accrued at the year end.",
          2_250_000,
          [("Months", "1 April to 31 December = 9 months."),
           ("Accrued interest", "30 000 000 × 10% × 9/12 = 2 250 000.")],
          "Accrued bond interest at the year end", "Calculation", "Count months since the last interest date."),
        Q("Why is a bond redemption premium written off over the life of the loan rather than all at once?",
          "It is part of the cost of borrowing, which benefits every year of the loan",
          [("It is an asset that must never be written off", "The premium has no resale value; it is a cost to spread."),
           ("It is a dividend to bondholders", "Bondholders receive interest and the premium, not dividends."),
           ("It reduces the share capital", "The premium has nothing to do with share capital.")],
          [("Matching", "The premium is an extra cost of the loan paid at redemption; spreading it matches the cost with the years that use the money.")],
          "Writing off the redemption premium", "Reasoning", "Think of the premium as extra interest."),
    ]))

# ---------------------------------------------------------------- 10. Increase of capital
use(110)
assert Fr(120_000_000 - 40_000_000, 5_000) == 16_000 and 120_000_000 // 5_000 == 24_000 and 40_000_000 // 5_000 == 8_000
_p10_V0 = Fr(6_000 * 18_000)
_p10_V1 = Fr(6_000 * 18_000 + 2_000 * 14_000, 8_000)
assert _p10_V1 == 17_000 and 18_000 - _p10_V1 == 1_000 and (18_000 - 14_000) * Fr(2_000, 8_000) == 1_000
assert Fr(15_000, 6) == 2_500
assert 50 // 3 == 16 and 50 - 16 * 3 == 2
_p10_v1 = Fr(50_000_000 + 1_000 * 16_000, 3_000)
_p10_v2 = Fr(50_000_000 + 1_000 * 16_000, 4_000)
assert _p10_v1 == 22_000 and _p10_v2 == 16_500 and _p10_v1 - _p10_v2 == 5_500 and 25_000 - _p10_v1 == 3_000
assert 2_000 * 10_000 == 20_000_000 and 2_000 * 3_000 == 6_000_000

SETS.append(practice_set(
    module=M_MOD, topic="Increase of capital",
    title="Capital increases: share value, DS and DA", lesson="acu1-increase-of-capital",
    questions=[
        NM("A company has 5 000 shares. Its assets at real value are FCFA 120 000 000 and its liabilities 40 000 000. What is the mathematical value of a share?",
           16_000,
           [(24_000, "Liabilities were not deducted from the assets."),
            (8_000, "This divides the liabilities, not the net assets, by the number of shares."),
            (10_000, "This is a typical nominal value; the mathematical value uses net assets.")],
           [("Net assets", "120 000 000 − 40 000 000 = 80 000 000."),
            ("Per share", "80 000 000 ÷ 5 000 = 16 000.")],
           "Mathematical value of a share", "Calculation", "Net assets divided by the number of shares."),
        NM("6 000 old shares are worth 18 000 each. The company issues 2 000 new shares for cash at 14 000 (1 for 3). What is the DS?",
           1_000,
           [(4_000, "This is V0 − issue price; it must be multiplied by n ÷ (N + n)."),
            (17_000, "This is the value after the issue, not the right."),
            (14_000, "This is the issue price of a new share.")],
           [("Value after", "(6 000 × 18 000 + 2 000 × 14 000) ÷ 8 000 = 136 000 000 ÷ 8 000 = 17 000."),
            ("DS", "18 000 − 17 000 = 1 000 = (18 000 − 14 000) × 2 000 ÷ 8 000.")],
           "Preferential subscription right (DS)", "Calculation", "Find the value per share after the issue."),
        N("A share is worth FCFA 15 000 before a bonus issue of 1 new share for 5 old. Find the attribution right (DA).",
          2_500,
          [("Value after", "15 000 × 5 ÷ 6 = 12 500."), ("DA", "15 000 − 12 500 = 2 500 = 15 000 × 1 ÷ 6.")],
          "Attribution right (DA)", "Calculation", "Net assets stay the same but are shared by 6 shares instead of 5."),
        Q("A cash issue is made on the basis of 1 new share for 3 old. A shareholder holds 50 old shares and does not want to buy extra rights. What can he do?",
          "Subscribe 16 new shares using 48 rights and sell the other 2 rights",
          [("Subscribe 17 new shares", "17 new shares need 51 rights; he has only 50."),
           ("Subscribe 50 new shares", "Each new share needs 3 rights."),
           ("Nothing, because 50 is not a multiple of 3", "He can use 48 rights and sell or keep the 2 left.")],
          [("Rights", "Each old share gives one DS; 3 DS buy 1 new share."),
           ("Result", "50 ÷ 3 = 16 remainder 2: 16 new shares and 2 rights to sell.")],
          "Using preferential subscription rights", "Application", "How many groups of 3 are in 50?"),
        Q("What is the effect of a bonus issue (incorporation of reserves) on the company?",
          "Capital rises and reserves fall by the same amount; net assets are unchanged",
          [("Net assets rise by the amount incorporated", "No money enters the company in a bonus issue."),
           ("Cash falls because shares are given away", "The shares are free: no cash leaves the company."),
           ("Capital falls and reserves rise", "It is the other way: reserves are turned into capital.")],
          [("Inside equity", "Debit reserves, credit capital: a transfer within equity.")],
          "Effect of a bonus issue", "Concept", "Does any money move?"),
        N("2 000 shares are worth 25 000 each (net assets 50 000 000). The company issues 1 000 shares for cash at 16 000, then makes a bonus issue of 1 share for 3 "
          "(1 000 shares), in which the new cash shares take part. Find the DA in the second stage.",
          5_500,
          [("After the cash issue", "(50 000 000 + 16 000 000) ÷ 3 000 = 22 000 (DS = 3 000)."),
           ("After the bonus issue", "66 000 000 ÷ 4 000 = 16 500."),
           ("DA", "22 000 − 16 500 = 5 500 = 22 000 × 1 ÷ 4.")],
          "Double increase of capital", "Calculation", "Work stage by stage; the second stage starts from the value after the first."),
        Q("2 000 shares of nominal value 10 000 are issued at 13 000, fully paid in cash. Which credits are correct?",
          "Capital 20 000 000 and share premium 6 000 000",
          [("Capital 26 000 000", "Capital is credited only with the nominal value; the excess is premium."),
           ("Capital 20 000 000 and reserves 6 000 000", "The excess over nominal value is a share premium (1051), not a reserve from profit."),
           ("Share premium 26 000 000", "The nominal value goes to capital.")],
          [("Capital", "2 000 × 10 000 = 20 000 000."), ("Premium", "2 000 × 3 000 = 6 000 000.")],
          "Recording a cash issue at a premium", "Application", "Split the issue price into nominal value and premium."),
        Q("A bondholder converts his bonds into shares. What is the main effect on the balance sheet?",
          "Debts fall and equity rises by the same amount, so gearing falls",
          [("Cash rises because new shares are issued", "No cash is received: the debt is exchanged for shares."),
           ("Equity falls because the company gives away shares", "Equity rises; the creditor becomes a shareholder."),
           ("Nothing changes because both are long-term finance", "Debt and equity are different: the mix (gearing) changes.")],
          [("Entry", "Debit the bond loan; credit capital and conversion premium."),
           ("Effect", "Liabilities fall, equity rises: lower gearing and no more interest on that debt.")],
          "Conversion of debt into capital", "Reasoning", "What happens to the debt account?"),
    ]))

# ---------------------------------------------------------------- 11. Reduction and amortization of capital
use(111)
assert (60_000_000 - 21_000_000) // 6_000 == 6_500
assert (25_000_000 - 15_000_000) // 10_000 == 1_000 and Fr(1_000, 2_500) == Fr(2, 5)
assert 5_000 * 10_000 * 20 // 100 == 10_000_000
_p11_fd = 2_000 * 10_000 * 5 // 100
_p11_sd = Fr(4_000_000 - _p11_fd, 2_500)
assert _p11_fd == 1_000_000 and _p11_sd == 1_200 and _p11_sd + 500 == 1_700 and Fr(4_000_000, 2_500) == 1_600 and Fr(3_000_000, 2_000) == 1_500

SETS.append(practice_set(
    module=M_MOD, topic="Reduction and amortization of capital",
    title="Reducing and amortizing capital", lesson="acu1-reduction-amortization-capital",
    questions=[
        Q("A company reduces its capital to absorb losses brought forward of FCFA 8 000 000. Which entry is correct?",
          "Debit capital 8 000 000; credit losses brought forward (129) 8 000 000",
          [("Debit losses brought forward 8 000 000; credit capital 8 000 000", "This would double the losses instead of clearing them."),
           ("Debit capital 8 000 000; credit bank 8 000 000", "No cash is paid when losses are absorbed."),
           ("Debit reserves 8 000 000; credit capital 8 000 000", "That is a bonus issue (incorporation of reserves).")],
          [("Book entry", "The debit balance of 129 is cancelled against capital; no asset leaves the company.")],
          "Reduction of capital to absorb losses", "Application", "Which account has the debit balance to clear?"),
        N("Capital is FCFA 60 000 000 in 6 000 shares. Losses brought forward of 21 000 000 are absorbed by reducing the nominal value. Find the new nominal value per share.",
          6_500,
          [("Capital after reduction", "60 000 000 − 21 000 000 = 39 000 000."),
           ("Per share", "39 000 000 ÷ 6 000 = 6 500.")],
          "New nominal value after a reduction", "Calculation", "Divide the reduced capital by the unchanged number of shares."),
        Q("Capital is 25 000 000 in 2 500 shares of 10 000. Losses of 15 000 000 are absorbed by reducing the NUMBER of shares, keeping the nominal value at 10 000. "
          "What exchange ratio is used?",
          "5 old shares for 2 new shares",
          [("2 old shares for 5 new shares", "This increases the number of shares."),
           ("3 old shares for 2 new shares", "This would leave 1 667 shares, not 1 000."),
           ("5 old shares for 3 new shares", "This would leave 1 500 shares, a capital of 15 000 000.")],
          [("New capital", "25 000 000 − 15 000 000 = 10 000 000, i.e. 1 000 shares of 10 000."),
           ("Ratio", "1 000 : 2 500 = 2 : 5, so 5 old shares are exchanged for 2 new.")],
          "Reduction by reducing the number of shares", "Calculation", "How many shares of 10 000 make the new capital?"),
        Q("Under the OHADA Uniform Act, what must happen when losses make an SA's equity fall below half of its share capital?",
          "The shareholders must decide whether to dissolve the company; if not, capital must be reduced or equity restored within a set period",
          [("The company is dissolved automatically", "Dissolution is not automatic; the shareholders decide."),
           ("Dividends must be doubled to attract investors", "Losses prevent dividends; they do not increase them."),
           ("Nothing: losses only matter on liquidation", "The law requires action to protect creditors.")],
          [("Creditor protection", "Equity below half of capital is a warning sign; the law forces shareholders to act.")],
          "Equity below half of capital", "Recall", "The law protects creditors when equity is too low."),
        Q("Which statement about amortization of capital is correct?",
          "Shareholders are repaid nominal value out of reserves, and total share capital stays the same",
          [("Capital falls by the amount repaid", "That is a reduction of capital by repayment, not amortization."),
           ("It absorbs losses brought forward", "Absorbing losses is a reduction for losses."),
           ("The shares lose their voting rights", "Jouissance shares keep their vote.")],
          [("Amortization", "Debit reserves, credit 4619, pay; and transfer 1013 to 1014. Capital in the statutes is unchanged.")],
          "Amortization of capital", "Concept", "Where does the money come from, and does account 101 change in total?"),
        N("A company amortizes 20% of the nominal value of its 5 000 shares of FCFA 10 000. How much is paid to shareholders?",
          10_000_000,
          [("Per share", "20% × 10 000 = 2 000."), ("Total", "5 000 × 2 000 = 10 000 000, debited to reserves.")],
          "Amount of an amortization", "Calculation", "Find the amount per share first."),
        NM("A company has 2 000 capital shares and 500 jouissance shares, all of nominal value 10 000. The statutes give a first dividend of 5% of non-amortized capital "
           "and the rest equally to every share. Distributable profit is FCFA 4 000 000. What dividend does a jouissance share receive?",
           1_200,
           [(1_700, "This adds the first dividend, which jouissance shares do not receive."),
            (1_600, "This shares the whole profit equally, ignoring the first dividend."),
            (1_500, "The super dividend was shared among capital shares only; jouissance shares also receive it.")],
           [("First dividend", "5% × 10 000 × 2 000 = 1 000 000 (capital shares only)."),
            ("Super dividend", "(4 000 000 − 1 000 000) ÷ 2 500 = 1 200 per share."),
            ("Jouissance share", "1 200; a capital share gets 500 + 1 200 = 1 700.")],
           "Dividends on jouissance shares", "Calculation", "Which shares receive the first dividend?"),
        Q("What is a 'coup d'accordéon'?",
          "A reduction of capital (often to zero or below the minimum) followed at once by an increase",
          [("A capital increase by incorporation of reserves", "That is a bonus issue."),
           ("The repayment of nominal value out of reserves", "That is amortization of capital."),
           ("The conversion of bonds into shares", "That is a conversion of debt.")],
          [("Accordion", "Capital shrinks to absorb losses and then expands with new money, often bringing in new shareholders.")],
          "Reduction followed by increase", "Recall", "An accordion closes and then opens."),
    ]))

# ---------------------------------------------------------------- 12. Company tax
use(112)
_p12_f = 12_000_000 + 900_000 + 300_000 - 400_000
assert _p12_f == 12_800_000 and 12_000_000 + 900_000 + 300_000 + 400_000 == 13_600_000 and 12_000_000 + 900_000 - 400_000 == 12_500_000
assert 12_000_000 + 400_000 - 900_000 - 300_000 == 11_200_000
assert 2_000_000 * 30 // 100 == 600_000 and 2_000_000 * 30 // 100 * 11 // 10 == 660_000
assert 5_000_000 * 22 // 1000 == 110_000
assert 200_000_000 * 22 // 1000 == 4_400_000 and 10_000_000 * 30 // 100 * 11 // 10 == 3_300_000
assert 15_000_000 - 4_000_000 == 11_000_000 and 11_000_000 * 30 // 100 == 3_300_000 and 15_000_000 * 30 // 100 == 4_500_000
assert 20_000_000 - 3_300_000 == 16_700_000 and 20_000_000 - 3_300_000 * 11 // 10 == 16_370_000
assert 6_000_000 * 3 // 10 == 1_800_000 and 1_800_000 * 11 // 10 == 1_980_000 and 120_000_000 * 22 // 1000 == 2_640_000
assert 80_000_000 * 22 // 1000 == 1_760_000

SETS.append(practice_set(
    module=M_MOD, topic="Company tax",
    title="Fiscal analysis, company tax and minimum tax", lesson="acu1-company-tax",
    questions=[
        Q("Why can the accounting profit differ from the fiscal profit?",
          "Tax rules refuse some expenses and exempt some income that the accounts record",
          [("Accountants make errors that inspectors correct", "The difference is built into the rules, not an error."),
           ("Tax is calculated on turnover, not profit", "Company tax is on fiscal profit; the minimum tax uses turnover."),
           ("Fiscal profit includes owners' drawings", "Drawings are not an expense or income of a company.")],
          [("Two rule books", "Accounting follows accounting standards; tax follows the tax code. The fiscal analysis bridges them.")],
          "Accounting profit versus fiscal profit", "Concept", "Which rule book decides what is deductible?"),
        NM("Accounting profit FCFA 12 000 000. Included in expenses: fines 900 000 and personal expenses 300 000 (not deductible). Exempt income of 400 000 is "
           "included in revenue. Find the fiscal profit.",
           _p12_f,
           [(13_600_000, "The exempt income was added instead of deducted."),
            (12_500_000, "The personal expenses were not added back."),
            (11_200_000, "The non-deductible expenses were deducted and the exempt income added.")],
           [("Add back", "900 000 + 300 000 = 1 200 000."),
            ("Deduct", "400 000."),
            ("Fiscal profit", "12 000 000 + 1 200 000 − 400 000 = 12 800 000.")],
           "Fiscal analysis", "Calculation", "Refused expenses are added back; exempt income is deducted."),
        N("Fiscal profit is FCFA 2 000 000 and the teaching company tax rate is 30%. Find the tax on profit (before any additional council tax).",
          600_000,
          [("Tax", "30% × 2 000 000 = 600 000.")],
          "Company tax at the teaching rate", "Calculation", "Apply the rate to the fiscal profit."),
        NM("A company has fiscal profit 10 000 000 and turnover 200 000 000. Teaching values: 30% company tax plus 10% of that tax as additional council tax; minimum "
           "tax 2.2% of turnover. What tax is due?",
           4_400_000,
           [(3_300_000, "The minimum tax was not compared with the tax on profit."),
            (3_000_000, "Neither the additional council tax nor the minimum tax was considered."),
            (4_000_000, "The minimum tax was taken at 2% instead of 2.2%.")],
           [("Tax on profit", "30% × 10 000 000 = 3 000 000; plus 10% = 3 300 000."),
            ("Minimum tax", "2.2% × 200 000 000 = 4 400 000."),
            ("Due", "The higher: 4 400 000.")],
           "Minimum tax comparison", "Application", "Compute both and take the higher."),
        NM("Fiscal profit before losses is FCFA 15 000 000 and a tax loss of 4 000 000 can be carried forward. Using a 30% rate (no other taxes), what is the tax on profit?",
           3_300_000,
           [(4_500_000, "The loss brought forward was not deducted."),
            (1_200_000, "This is 30% of the loss, not of the taxable base."),
            (3_600_000, "This applies 30% to 12 000 000: the loss deducted was too large.")],
           [("Base", "15 000 000 − 4 000 000 = 11 000 000."), ("Tax", "30% × 11 000 000 = 3 300 000.")],
           "Loss carried forward", "Calculation", "Reduce the base before applying the rate."),
        Q("A company has an accounting loss but turnover of 80 000 000. Using a teaching minimum tax of 2.2%, how much minimum tax is due?",
          "FCFA 1 760 000",
          [("Nil, because there is no profit", "The minimum tax is based on turnover and applies even in a loss year."),
           ("FCFA 80 000", "This is 0.1% of turnover; the rate is 2.2%."),
           ("FCFA 17 600 000", "The rate was applied as 22% instead of 2.2%.")],
          [("Minimum tax", "2.2% × 80 000 000 = 1 760 000.")],
          "Minimum tax in a loss year", "Application", "What is the base of the minimum tax?"),
        NM("Accounting profit before tax is FCFA 20 000 000 and the tax due (including additional council tax) is 3 300 000. What is the profit after tax?",
           16_700_000,
           [(16_370_000, "The additional council tax was added again."),
            (20_000_000, "The tax was not deducted."),
            (3_300_000, "This is the tax, not the profit after tax.")],
           [("Profit after tax", "20 000 000 − 3 300 000 = 16 700 000.")],
           "Profit after tax", "Calculation", "Subtract the tax due from the profit before tax."),
        Q("Which entry records the income tax due for the year?",
          "Debit 891 Income tax; credit 441 State, income tax",
          [("Debit 441 State, income tax; credit 891 Income tax", "This reverses the entry."),
           ("Debit 521 Bank; credit 441 State, income tax", "The tax is first recognised as a debt; payment is a later entry."),
           ("Debit 111 Legal reserve; credit 891 Income tax", "Tax is an expense, not an appropriation of reserves.")],
          [("Entry", "Expense (891) and debt to the State (441); on payment debit 441, credit bank.")],
          "Recording income tax", "Application", "Is the tax an expense, and who is owed?"),
    ]))

# ---------------------------------------------------------------- 13. Mergers
use(113)
assert Fr(60_000_000, 4_000) == 15_000 and Fr(21_000_000, 3_000) == 7_000 and Fr(7_000, 15_000) == Fr(7, 15)
assert 6_000 * 7 // 15 == 2_800 and 6_000 * 7 % 15 == 0 and 2_800 * 10_000 == 28_000_000 and 42_000_000 - 28_000_000 == 14_000_000
assert 42_000_000 == 6_000 * 7_000 and 28_000_000 + 14_000_000 == 42_000_000
assert Fr(15_000, 7_000) != Fr(7, 15) and Fr(60_000_000 + 42_000_000, 4_000 + 2_800) == 15_000
assert 42_000_000 - 20_000_000 - 3_000_000 == 19_000_000 and 42_000_000 - 20_000_000 == 22_000_000 and 42_000_000 - 3_000_000 == 39_000_000
assert 45_000_000 - 15_000_000 == 30_000_000 and Fr(30_000_000, 2_000) == 15_000 and 100 * 3 // 5 == 60

SETS.append(practice_set(
    module=M_MOD, topic="Mergers",
    title="Absorption, exchange ratio and merger premium", lesson="acu1-mergers",
    questions=[
        Q("What happens to the absorbed company in a merger by absorption?",
          "It is dissolved, and its assets and liabilities pass to the absorbing company",
          [("It becomes a branch that keeps its own legal personality", "The absorbed company ceases to exist as a legal person."),
           ("It is liquidated and its cash is shared among creditors only", "Its shareholders receive shares of the absorbing company."),
           ("It buys shares in the absorbing company with its own cash", "The shares are issued to its shareholders in exchange for the net assets.")],
          [("Transfer", "All assets and liabilities pass to A, and B's shareholders receive A shares.")],
          "Merger by absorption", "Recall", "Where do B's assets and debts go?"),
        NM("Company B has assets FCFA 70 000 000 and liabilities 28 000 000, with 3 000 shares. What is the value of one B share by net assets?",
           14_000,
           [(23_333, "Liabilities were not deducted (70 000 000 ÷ 3 000)."),
            (9_333, "Only the liabilities were divided by the shares."),
            (42_000, "This is the net assets, not the value per share.")],
           [("Net assets", "70 000 000 − 28 000 000 = 42 000 000."), ("Per share", "42 000 000 ÷ 3 000 = 14 000.")],
           "Value of a share of the absorbed company", "Calculation", "Subtract liabilities, then divide."),
        Q("A share of A is worth 15 000 and a share of B is worth 7 000. Which is the exchange ratio?",
          "7 A shares for 15 B shares",
          [("15 A shares for 7 B shares", "This inverts the ratio."),
           ("1 A share for 1 B share", "Different values give a different ratio."),
           ("22 A shares for 8 B shares", "The values were added or mixed; the ratio is B's value over A's value.")],
          [("Ratio", "7 000 ÷ 15 000 = 7/15: 7 A shares for 15 B shares.")],
          "Exchange ratio", "Calculation", "Divide the value of a B share by the value of an A share."),
        NM("A has net assets FCFA 60 000 000 in 4 000 shares; B has net assets 42 000 000 in 6 000 shares. Shares are of nominal value 10 000. "
           "A absorbs B at the ratio from their values. How many new A shares are issued?",
           2_800,
           [(6_000, "This assumes one A share for each B share."),
            (12_857, "The ratio was inverted (15/7) giving too many shares."),
            (1_867, "The ratio 7/15 was applied to the number of A shares instead of B shares.")],
           [("Values", "A: 15 000. B: 42 000 000 ÷ 6 000 = 7 000."),
            ("Ratio", "7/15."),
            ("New shares", "6 000 × 7/15 = 2 800.")],
           "Shares issued in a merger", "Calculation", "Apply the ratio to the number of B shares."),
        N("Continuing: the new shares have a nominal value of 10 000 each. Find the merger premium in FCFA.",
          14_000_000,
          [("Capital increase", "2 800 × 10 000 = 28 000 000."),
           ("Net assets received", "42 000 000."),
           ("Premium", "42 000 000 − 28 000 000 = 14 000 000.")],
          "Merger premium", "Calculation", "Net assets received minus the nominal value of the new shares."),
        NM("B's net assets are FCFA 42 000 000. A issues shares of nominal value 20 000 000 and pays a cash balance of 3 000 000. What is the merger premium?",
           19_000_000,
           [(22_000_000, "The cash balance was not deducted."),
            (39_000_000, "The nominal value of the new shares was not deducted."),
            (17_000_000, "The cash balance was deducted twice.")],
           [("Formula", "Net assets − nominal value issued − cash balance."),
            ("Result", "42 000 000 − 20 000 000 − 3 000 000 = 19 000 000.")],
           "Merger with a cash balance", "Application", "The cash paid is part of what A gives for the net assets."),
        Q("In a fair exchange, what should be true of the value of an A share after the merger?",
          "It stays the same as before the merger",
          [("It doubles because the company is bigger", "A bigger company does not raise the value per share by itself."),
           ("It falls to the value of a B share", "The value is the weighted result; it equals A's old value when the exchange is fair."),
           ("It cannot be calculated", "It can: total net assets divided by total shares.")],
          [("Check", "(60 000 000 + 42 000 000) ÷ (4 000 + 2 800) = 15 000, equal to the value before.")],
          "Fair exchange test", "Reasoning", "Add the net assets and add the shares."),
        Q("Which statement about the merger premium is correct?",
          "It is part of the equity of the absorbing company, not income",
          [("It is a profit shown in the income statement", "It arises from a share exchange, not from trading."),
           ("It is paid in cash to the absorbed company", "It is an accounting figure, not a cash payment."),
           ("It is a liability to B's shareholders", "It belongs to the equity of the absorbing company.")],
          [("Equity", "Like a share premium, it is credited to a premium account (1054) within equity.")],
          "Nature of the merger premium", "Concept", "Is any trading profit earned?"),
    ]))

# ---------------------------------------------------------------- 14. Liquidation
use(114)
assert 90_000_000 - 4_000_000 - 50_000_000 == 36_000_000 and Fr(36_000_000, 3_000) == 12_000
assert 36_000_000 - 30_000_000 == 6_000_000 and 6_000_000 // 3_000 == 2_000 and 30_000_000 // 3_000 == 10_000
assert 90_000_000 - 50_000_000 == 40_000_000 and 90_000_000 - 4_000_000 * 2 - 50_000_000 == 32_000_000
assert 50_000_000 // 7_000 == 7_142 and 70_000_000 // 7_000 == 10_000 and (70_000_000 - 50_000_000) // 7_000 == 2_857 and 50_000_000 // 1_000 == 50_000
assert 7_000_000 * 100 // 14_000_000 == 50 and 2_000_000 * 50 // 100 == 1_000_000

SETS.append(practice_set(
    module=M_MOD, topic="Liquidation",
    title="Order of payment, surplus and insolvency", lesson="acu1-liquidation",
    questions=[
        Q("In a liquidation, which of the following is paid LAST?",
          "The shareholders (repayment of capital and surplus)",
          [("Ordinary creditors", "Creditors are paid before shareholders."),
           ("Preferential creditors such as staff wages", "Preferential creditors rank near the top."),
           ("The costs of the liquidation", "Costs are paid first from the proceeds.")],
          [("Order", "Costs, preferential and secured creditors, ordinary creditors, then shareholders.")],
          "Order of payment in liquidation", "Recall", "Owners take the residual."),
        Q("What is the difference between dissolution and liquidation?",
          "Dissolution ends the life of the company; liquidation is the process of collecting assets, paying debts and sharing the surplus",
          [("They mean the same thing", "They are two stages: the decision or event, then the process."),
           ("Dissolution is the sale of the assets; liquidation is the vote of the shareholders", "The terms are reversed here."),
           ("Liquidation happens only in an SNC", "All company forms may be liquidated.")],
          [("Stages", "First dissolution (event or decision), then liquidation, then the company is struck off.")],
          "Dissolution and liquidation", "Concept", "One is a decision, the other a procedure."),
        NM("Assets are sold for FCFA 90 000 000. Liquidation costs are 4 000 000 and creditors are 50 000 000. What is left for shareholders?",
           36_000_000,
           [(40_000_000, "The costs were not deducted."),
            (86_000_000, "The creditors were not deducted."),
            (32_000_000, "The costs were deducted twice.")],
           [("Available", "90 000 000 − 4 000 000 = 86 000 000."), ("After creditors", "86 000 000 − 50 000 000 = 36 000 000.")],
           "Cash left for shareholders", "Calculation", "Costs and creditors come before shareholders."),
        NM("FCFA 36 000 000 is left for 3 000 shares of nominal value 10 000 (fully paid). What does each share receive?",
           12_000,
           [(10_000, "This is the nominal value; the boni was left out."),
            (2_000, "This is the boni per share only."),
            (36_000, "The total was not divided by the number of shares.")],
           [("Capital", "3 000 × 10 000 = 30 000 000 repaid first (10 000 per share)."),
            ("Boni", "6 000 000 ÷ 3 000 = 2 000."),
            ("Each share", "10 000 + 2 000 = 12 000 (36 000 000 ÷ 3 000).")],
           "Repayment and boni per share", "Calculation", "Repay capital first, then share the rest."),
        NM("After costs and creditors, FCFA 50 000 000 remains from the liquidation of a company with capital 70 000 000 in 7 000 shares fully paid. "
           "What does each share receive (rounded down to the franc)?",
           7_142,
           [(10_000, "This assumes the capital is repaid in full; there is not enough cash."),
            (2_857, "This is the loss per share, not what is received."),
            (50_000, "The cash was not divided by the number of shares.")],
           [("Per share", "50 000 000 ÷ 7 000 = 7 142.86, about 7 142 (rounded down)."),
            ("No boni", "The cash does not even repay the capital.")],
           "Repayment when cash is short", "Application", "Divide the cash left by the number of shares."),
        N("An insolvent company has FCFA 7 000 000 left for ordinary creditors owed 14 000 000. How much (in FCFA) does a creditor owed 2 000 000 receive?",
          1_000_000,
          [("Proportion", "7 000 000 ÷ 14 000 000 = 50%."), ("Creditor", "50% × 2 000 000 = 1 000 000.")],
          "Dividend to ordinary creditors", "Calculation", "Work out the percentage first."),
        Q("A company's cash is not enough to pay its ordinary creditors in full. What do the shareholders receive?",
          "Nothing",
          [("Their capital, ahead of the creditors", "Creditors rank ahead of shareholders."),
           ("Half of the remaining cash", "There is no cash left after the creditors."),
           ("Their capital in proportion to the creditors' percentage", "Shareholders are paid only after creditors are paid in full.")],
          [("Priority", "Shareholders are residual claimants: if creditors are not paid in full there is nothing left for them.")],
          "Position of shareholders in insolvency", "Reasoning", "Who is paid after creditors?"),
        Q("Which statement about the liquidation surplus (boni) is correct?",
          "It arises only after creditors are paid and capital is repaid in full",
          [("It is paid to creditors in proportion to their claims", "Creditors receive only what they are owed."),
           ("It is shared before the capital is repaid", "Capital is repaid first."),
           ("It is a tax paid to the State", "The boni is shared by the shareholders (taxes are a separate matter: check the current rules).")],
          [("Boni", "Cash left after costs, creditors and the repayment of capital.")],
          "Liquidation surplus", "Concept", "Capital first, then surplus."),
    ]))
