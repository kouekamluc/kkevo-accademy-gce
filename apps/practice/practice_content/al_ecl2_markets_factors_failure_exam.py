"""A Level Economics (0725), Lower Sixth: practice sets for Market Structures, Theory of Distribution & Factor
Pricing, Market Failure & Government Micro-Intervention and the Examination module.

One 8-question set per lesson (15 topic lessons, 3 examination lessons), plus 'Paper 1 mock exam A' (50 multiple-choice
questions across all six Lower Sixth modules in proportion to their topic counts), 'Paper 2 practice paper A' (25
auto-markable parts, microeconomics side only) and 'Paper 3 practice paper A' (20 auto-markable parts). Exam facts are
only those of the Board's 2023 subject report. Mock timings (90 and 150 minutes) are KKEVO practice settings. Every
numerical answer was checked by script.
"""

import random

from .dsl import *  # noqa: F403

COURSE = ("economics", "lower-sixth")

M_MET = "Economic Methodology & Resource Allocation"
M_PRI = "Price Theory & Consumer Behaviour"
M_PRO = "Theory of Production & Costs"
M_MKT = "Market Structures"
M_DIS = "Theory of Distribution & Factor Pricing"
M_MF = "Market Failure & Government Micro-Intervention"
M_EXAM = "Examination"

# Exact topic titles (apps/academics/gce_curriculum.py, ("economics", "lower-sixth")).
T_METH = "Economic methodology"
T_PPC = "Scarcity, choice and the production possibility curve"
T_EFF = "Economic efficiency"
T_SYS = "Economic systems"
T_DSF = "Demand and supply functions"
T_ELA = "Elasticities of demand and supply"
T_SUR = "Consumer and producer surplus"
T_MU = "Marginal utility theory"
T_IC = "Indifference curve analysis"
T_IS = "Income and substitution effects"
T_SRP = "Short-run production and diminishing returns"
T_RTS = "Returns to scale, isoquants and isocosts"
T_EOS = "Economies and diseconomies of scale"
T_COST = "Short-run and long-run costs"
T_REV = "Revenue curves"
T_PMAX = "Profit maximization"
T_PC = "Perfect competition"
T_MON = "Monopoly and price discrimination"
T_MC = "Monopolistic competition"
T_OLI = "Oligopoly"
T_CON = "Contestable markets"
T_MRP = "Marginal revenue product and the demand for factors"
T_WAGE = "Wage determination and trade unions"
T_RENT = "Economic rent and transfer earnings"
T_INT = "Interest"
T_PROF = "Profit"
T_PUB = "Public, merit and demerit goods"
T_EXT = "Externalities"
T_TAX = "Taxes, subsidies and pollution permits"
T_REG = "Regulation, privatization and nationalization"


def Q(prompt, correct, wrongs, steps, concept, skill, hint, diagram="", alt=""):
    """Four-option MC spec. `wrongs` = [(text, why)] x3. The position of the correct option is balanced by build()."""
    assert len(wrongs) == 3, prompt
    return {"k": "mc", "prompt": prompt, "correct": correct, "wrongs": wrongs, "steps": steps, "concept": concept,
            "skill": skill, "hint": hint, "diagram": diagram, "alt": alt}


def N(prompt, answer, steps, concept, skill, hint, tol=0, unit="", diagram="", alt=""):
    return {"k": "num", "prompt": prompt, "answer": answer, "steps": steps, "concept": concept, "skill": skill,
            "hint": hint, "tol": tol, "unit": unit, "diagram": diagram, "alt": alt}


def build(specs, seed):
    """Turn specs into MC/NUM questions with the correct option spread evenly over A-D."""
    rng = random.Random(seed)
    counts = [0, 0, 0, 0]
    out = []
    for s in specs:
        st = [S(a, text=b) for a, b in s["steps"]]
        assert s["concept"] and len(s["concept"]) <= 80, s["concept"]
        assert s["hint"] and s["skill"], s["prompt"]
        if s["k"] == "num":
            out.append(NUM(s["prompt"], s["answer"], steps=st, tolerance=s["tol"], unit=s["unit"], concept=s["concept"],
                           skill=s["skill"], hint=s["hint"], diagram=s["diagram"], diagram_alt=s["alt"]))
            continue
        m = min(counts)
        pos = rng.choice([i for i in range(4) if counts[i] == m])
        counts[pos] += 1
        ch = [C(t, why=w) for t, w in s["wrongs"]]
        ch.insert(pos, C(s["correct"], correct=True))
        out.append(MC(s["prompt"], ch, steps=st, concept=s["concept"], skill=s["skill"], hint=s["hint"],
                      diagram=s["diagram"], diagram_alt=s["alt"]))
    return out


SETS = []

# ------------------------------------------------------------------ Profit maximization
V1 = [
    Q("Normal profit is best described as:", "The minimum return needed to keep the entrepreneur in the industry, included in total cost",
      [("Any profit above total cost", "That is supernormal (abnormal) profit."), ("The profit shown in the firm's accounts", "Accounting profit ignores opportunity costs such as the owner's time."), ("The profit at the output where TR is greatest", "Revenue maximization is a different objective.")],
      [("Definition", "Normal profit is the opportunity cost of the entrepreneur's time and capital; economists count it as a cost.")], "Normal and supernormal profit", "Recall", "Is normal profit inside or outside total cost?"),
    Q("A firm's marginal revenue is 800 FCFA and its marginal cost is 950 FCFA at its current output. To raise profit it should:", "Reduce output",
      [("Increase output", "The next unit would add 950 to cost but only 800 to revenue."), ("Leave output unchanged", "Profit is not maximized while MC is not equal to MR."), ("Shut down at once", "Nothing suggests total revenue fails to cover variable cost.")],
      [("Compare", "MC > MR: the last unit reduced profit by 150 FCFA, so cut output until MC = MR.")], "MC = MR rule", "Application", "Which is larger, MR or MC?"),
    Q("In the diagram, MC cuts MR at Qa and at Qb. At which output is profit maximized, and why?", "At Qb, because MC cuts MR from below there",
      [("At Qa, because it is reached first", "At Qa MC is falling: producing a little more would add to profit, so profit is at a minimum there."), ("At both, since MC = MR at each", "MC = MR is necessary but not sufficient; the slope of MC matters."), ("Where MR = 0", "That output maximizes revenue, not profit.")],
      [("Second-order condition", "Profit is greatest where MC = MR and MC is rising (cutting MR from below), which is Qb.")], "Second-order condition", "Interpretation", "Look at whether MC is rising or falling at each crossing.",
      diagram="alecl2-profit-max-q.svg", alt="A downward-sloping MR line cut twice by a U-shaped MC curve, first at Qa and then at Qb."),
    N("A firm's total revenue is 500 000 FCFA at 100 units and 540 000 FCFA at 101 units. What is the marginal revenue of the 101st unit, in FCFA?", 40000,
      [("Marginal revenue", "MR = 540 000 − 500 000 = 40 000 FCFA.")], "Marginal revenue", "Calculation", "MR is the change in total revenue.", tol=0, unit="FCFA"),
    N("A firm faces P = 100 − 2Q and has MC = 10 + 2Q. Find the profit-maximizing output Q.", 15,
      [("MR", "MR = 100 − 4Q (twice the slope of demand)."), ("Solve", "10 + 2Q = 100 − 4Q, so 6Q = 90 and Q = 15.")], "Profit maximization by equation", "Calculation", "Write MR first, then set MC = MR.", tol=0),
    N("For the firm in the previous question (P = 100 − 2Q, TC = 50 + 10Q + Q²), what output maximizes sales revenue?", 25,
      [("Rule", "Sales revenue is maximized where MR = 0."), ("Solve", "100 − 4Q = 0, so Q = 25.")], "Sales revenue maximization", "Calculation", "Where is total revenue at its peak?", tol=0),
    Q("Which objective is linked with Herbert Simon and the idea that firms aim for a satisfactory rather than a maximum profit?", "Satisficing",
      [("Sales revenue maximization", "That is associated with Baumol and the rule MR = 0."), ("Growth maximization", "That is associated with Marris."), ("Profit maximization", "That is the traditional assumption Simon questioned.")],
      [("Recall", "Satisficing: with limited information and several groups to please, the firm aims for 'good enough' results.")], "Alternative objectives", "Recall", "Which word combines 'satisfy' and 'suffice'?"),
    Q("Why might the managers of a large company produce more than the profit-maximizing output?", "Their pay and status rise with sales, and shareholders cannot fully monitor them",
      [("Because MC is always zero for large firms", "MC is not zero; and with MC = 0 the profit and revenue maxima coincide."), ("Because more output always gives more profit", "Beyond MC = MR extra output reduces profit."), ("Because shareholders want lower profit", "Shareholders (principals) want profit; that is the point of the conflict.")],
      [("Principal-agent problem", "Separation of ownership and control lets managers (agents) pursue sales or growth rather than the owners' profit.")], "Principal-agent problem", "Reasoning", "Who controls the firm day to day, and what do they want?"),
]
SETS.append(practice_set(module=M_MKT, topic=T_PMAX, title="The MC = MR rule and other objectives", lesson="ecl2-profit-maximization", questions=build(V1, 201)))

# ------------------------------------------------------------------ Perfect competition
V2 = [
    Q("Which assumption explains why a perfectly competitive firm earns only normal profit in the long run?", "Freedom of entry and exit",
      [("Many buyers", "Many buyers make the firm a price taker but do not remove profit."), ("Perfect information alone", "Information helps, but it is entry that competes profit away."), ("Perfect factor mobility alone", "Mobility of factors does not, by itself, bring new firms in.")],
      [("Entry", "Supernormal profit attracts new firms; industry supply rises and price falls to minimum AC.")], "Long-run equilibrium", "Concept", "What happens when outsiders see supernormal profit?"),
    Q("For a firm in perfect competition, which is true?", "AR = MR = P at every output",
      [("MR is below AR", "That is true of a firm with a downward-sloping demand curve."), ("The firm chooses its price", "It is a price taker."), ("Demand for its output is perfectly inelastic", "It is perfectly elastic: horizontal at the market price.")],
      [("Price taker", "Each extra unit sells at the market price, so it adds P to revenue: AR = MR = P.")], "Price taker", "Recall", "Can the firm affect the market price?"),
    Q("In the diagram, below which price will the firm shut down in the short run?", "P1, the minimum of AVC",
      [("P2, the minimum of AC", "Below P2 the firm makes a loss, but it still covers variable cost down to P1."), ("Any price at which it makes a loss", "A short-run loss is acceptable if price covers AVC."), ("The price where MC is at its minimum", "The minimum of MC is not the shut-down point.")],
      [("Rule", "Shut down if P < minimum AVC: then producing loses more than the fixed cost.")], "Shut-down point", "Interpretation", "Which cost must revenue cover in the short run?",
      diagram="alecl2-pc-shutdown-q.svg", alt="A firm's MC, AC and AVC curves, with dashed horizontal price lines P1 at the minimum of AVC and P2 at the minimum of AC."),
    N("A perfectly competitive firm sells 400 units at 1 500 FCFA. Its average cost is 1 650 FCFA and its average variable cost is 1 200 FCFA. What is its loss, in FCFA?", 60000,
      [("Loss per unit", "1 650 − 1 500 = 150 FCFA."), ("Total", "150 × 400 = 60 000 FCFA. It keeps producing because 1 500 > AVC of 1 200.")], "Short-run loss", "Calculation", "Loss = (AC − P) × Q.", tol=0, unit="FCFA"),
    N("A firm has fixed cost 40 and total variable cost 22, 38, 50, 64, 82, 106 for outputs 1 to 6. The price is 20. Using P = MC, how many units should it produce?", 5,
      [("MC", "MC = 22, 16, 12, 14, 18, 24."), ("Rule", "Produce while MC ≤ 20: the 5th unit costs 18, the 6th 24, so Q = 5. P = 20 is above AVC (82 ÷ 5 = 16.4), so it produces.")], "Short-run output", "Calculation", "Work out MC for each unit.", tol=0, unit="units"),
    Q("The short-run supply curve of a perfectly competitive firm is:", "Its MC curve above the minimum of AVC",
      [("Its AC curve", "The firm chooses output where P = MC, not where P = AC."), ("Its whole MC curve", "Below minimum AVC it supplies nothing."), ("A horizontal line at the market price", "That is its demand (AR) curve.")],
      [("Supply", "At each price above minimum AVC the firm supplies the output where P = MC.")], "Short-run supply curve", "Concept", "At each price, where does the firm produce?"),
    Q("When the industry is in long-run equilibrium, a perfectly competitive firm is allocatively efficient because:", "Price equals marginal cost",
      [("Price equals minimum AC", "That is productive efficiency."), ("It earns supernormal profit", "In long-run equilibrium it earns only normal profit."), ("It spends on advertising", "A perfect competitor has no reason to advertise.")],
      [("Allocative efficiency", "P = MC: the value buyers place on the last unit equals its cost.")], "Efficiency", "Concept", "Allocative efficiency compares price with which cost?"),
    Q("Which is the strongest criticism of perfect competition as an ideal?", "With only normal profit in the long run, firms may lack funds and incentive to innovate",
      [("Prices are too high", "Prices equal minimum AC, the lowest possible."), ("It is allocatively inefficient", "Long-run equilibrium has P = MC."), ("Firms earn excessive profit", "Only normal profit is earned in the long run.")],
      [("Dynamic efficiency", "Static efficiency is excellent, but the lack of supernormal profit may slow research and new products.")], "Evaluation of perfect competition", "Reasoning", "Think about the long run and new technology."),
]
SETS.append(practice_set(module=M_MKT, topic=T_PC, title="Short-run and long-run equilibrium of the price taker", lesson="ecl2-perfect-competition", questions=build(V2, 202)))

# ------------------------------------------------------------------ Monopoly and price discrimination
V3 = [
    Q("Which is a barrier to entry that gives rise to a natural monopoly?", "Economies of scale so large that one firm can supply the whole market at the lowest average cost",
      [("A patent on a new medicine", "That is a legal barrier, not the cause of natural monopoly."), ("Brand loyalty built by advertising", "That is a strategic barrier."), ("A government ban on imports", "That is a legal barrier.")],
      [("Natural monopoly", "When average cost keeps falling over the whole range of market demand, one firm is cheaper than two.")], "Barriers to entry", "Recall", "Natural monopoly comes from cost conditions."),
    Q("A profit-maximizing monopolist always produces where demand is price elastic because:", "MR is positive only where PED is greater than 1, and MR must equal a positive MC",
      [("Monopolists prefer low prices", "It sets the highest price consistent with MC = MR."), ("Demand for monopoly goods is always elastic", "Market demand can have inelastic sections; the monopolist avoids them."), ("Its MC is zero", "MC is positive; that is why MR must be positive too.")],
      [("Link", "Where demand is inelastic MR is negative, so cutting output would raise revenue and lower cost.")], "Monopoly and elasticity", "Reasoning", "What is the sign of MR when demand is inelastic?"),
    N("A monopolist faces P = 120 − 2Q and has MC = AC = 20. Find its profit-maximizing price.", 70,
      [("MR", "MR = 120 − 4Q."), ("MC = MR", "120 − 4Q = 20, so Q = 25."), ("Price", "P = 120 − 50 = 70.")], "Monopoly equilibrium", "Calculation", "Find Q from MC = MR, then read P from demand.", tol=0, unit="FCFA"),
    N("For the same monopolist (P = 120 − 2Q, MC = AC = 20), what is the deadweight loss compared with perfect competition?", 625,
      [("Outputs", "Monopoly Q = 25 at P = 70; competition Q = 50 at P = 20."), ("Triangle", "½ × (70 − 20) × (50 − 25) = 625.")], "Deadweight loss", "Calculation", "The triangle lies between demand and MC, from the monopoly output to the competitive output.", tol=0),
    Q("X-inefficiency in a monopoly means:", "Costs are higher than the lowest possible for the output, because there is no competitive pressure",
      [("Output is below the competitive output", "That is allocative inefficiency."), ("The firm makes a loss", "X-inefficiency raises cost; the monopolist may still make profit."), ("Price differs between markets", "That is price discrimination.")],
      [("Definition", "Without competition, managers may allow slack: overstaffing, waste, little effort to cut costs.")], "X-inefficiency", "Concept", "X-inefficiency is about the level of costs."),
    Q("A telephone company charges a high rate for calls in the day and a low rate at night. This is:", "Third-degree price discrimination",
      [("First-degree price discrimination", "First degree charges each buyer his or her own maximum price."), ("Second-degree price discrimination", "Second degree varies the price with the quantity bought."), ("Not discrimination, because costs differ", "If the cost of a call is the same, the price difference reflects demand, not cost.")],
      [("Classify", "Groups (daytime business callers, night-time callers) are separated by time and charged different prices.")], "Degrees of price discrimination", "Application", "Are buyers grouped, or is each charged separately?"),
    Q("In third-degree price discrimination the firm maximizes profit when:", "MR in each market equals MC",
      [("Price is the same in both markets", "Then it would not be discriminating."), ("AR in each market equals MC", "That would be allocatively efficient pricing, not profit maximization."), ("Total revenue in each market is equal", "Revenue need not be equal.")],
      [("Rule", "If MR were higher in one market, moving a unit there would raise revenue: so MRA = MRB = MC.")], "Third-degree discrimination rule", "Concept", "Where would the firm move its next unit?"),
    N("A firm sells in two markets with MC = 20. Market A: P = 100 − Q; market B: P = 60 − 0.5Q. What price does it charge in market A (FCFA)?", 60,
      [("MR in A", "MR = 100 − 2Q = 20, so Q = 40."), ("Price", "P = 100 − 40 = 60 FCFA. (In B, Q = 40 and P = 40: the less elastic market A pays more.)")], "Third-degree discrimination calculation", "Calculation", "Set MR in market A equal to MC.", tol=0, unit="FCFA"),
]
SETS.append(practice_set(module=M_MKT, topic=T_MON, title="Monopoly equilibrium, welfare and price discrimination", lesson="ecl2-monopoly-price-discrimination", questions=build(V3, 203)))

# ------------------------------------------------------------------ Monopolistic competition
V4 = [
    Q("Which combination describes monopolistic competition?", "Many firms, differentiated products, free entry and exit",
      [("Many firms, homogeneous products, free entry", "That is perfect competition."), ("A few firms, interdependence, high barriers", "That is oligopoly."), ("One firm, no close substitutes, barriers to entry", "That is monopoly.")],
      [("Features", "Many sellers, each with its own brand, and no barriers to entry.")], "Features", "Recall", "Which structure has brands but easy entry?"),
    Q("Customers keep buying one brand of soap even when a similar brand is cheaper. The economic term for this is:", "Brand loyalty",
      [("Excess capacity", "That is the gap between output and the output at minimum AC."), ("Price rigidity", "That is a feature of the kinked demand model."), ("Consumer surplus", "That is the gap between willingness to pay and price.")],
      [("Term", "Brand loyalty makes a firm's demand less elastic.")], "Brand loyalty", "Recall", "It is about loyalty to a name."),
    Q("Which is a form of product differentiation?", "Offering home delivery and an attractive package",
      [("Cutting the price below rivals'", "That is price competition, not differentiation."), ("Buying raw materials in bulk", "That lowers cost; it is an economy of scale."), ("Paying workers by the piece", "That is a method of wage payment.")],
      [("Differentiation", "Packaging, service, location, quality and branding make a product seem different.")], "Product differentiation", "Application", "Which option changes how buyers see the product?"),
    Q("In long-run equilibrium, a monopolistically competitive firm's demand curve:", "Is tangent to its AC curve at the output where MC = MR",
      [("Lies above AC, giving supernormal profit", "Entry removes supernormal profit in the long run."), ("Is tangent to AC at the minimum of AC", "Only a horizontal demand curve could touch AC at its minimum."), ("Is horizontal", "Differentiation gives a downward-sloping demand curve.")],
      [("Tangency", "AR = AC (normal profit) and MC = MR at the same output.")], "Long-run tangency", "Concept", "What does free entry do to profit?"),
    N("A salon has AC = 1 000 + 20 000/Q (FCFA) and faces demand P = 3 000 − 50Q, with MC = 1 000. Find its profit-maximizing output Q.", 20,
      [("MR", "MR = 3 000 − 100Q."), ("MC = MR", "3 000 − 100Q = 1 000, so Q = 20. Then P = 2 000 = AC: normal profit.")], "Long-run equilibrium calculation", "Calculation", "Set MR = MC.", tol=0, unit="braids"),
    N("A monopolistically competitive firm produces 300 units in long-run equilibrium. The minimum point of its AC curve is at 380 units. What is its excess capacity, in units?", 80,
      [("Excess capacity", "380 − 300 = 80 units.")], "Excess capacity", "Calculation", "Subtract actual output from the output at minimum AC.", tol=0, unit="units"),
    Q("Which statement correctly distinguishes the two structures?", "A perfect competitor produces at minimum AC in the long run, whereas a monopolistic competitor produces to the left of minimum AC",
      [("A perfect competitor earns supernormal profit in the long run, whereas a monopolistic competitor earns normal profit", "Both earn normal profit in the long run."), ("Both sell differentiated products", "A perfect competitor's product is homogeneous."), ("A perfect competitor advertises heavily, whereas a monopolistic competitor does not", "It is the other way round.")],
      [("Distinction", "Use 'whereas' and state both sides: the tangency of a downward AR forces output below the minimum-cost level.")], "Comparison with perfect competition", "Reasoning", "Which option states two correct, contrasting facts?"),
    Q("Which is the best argument in defence of monopolistic competition?", "Consumers gain variety and choice, which they value",
      [("Firms produce at minimum AC", "They produce with excess capacity."), ("Price equals marginal cost", "P > MC in long-run equilibrium."), ("Firms earn high long-run profits to fund research", "Long-run profit is only normal.")],
      [("Evaluation", "Excess capacity can be seen as the cost of variety; buyers may prefer a nearby salon or a favourite style.")], "Evaluation", "Reasoning", "What do consumers get that perfect competition does not offer?"),
]
SETS.append(practice_set(module=M_MKT, topic=T_MC, title="Differentiation, tangency and excess capacity", lesson="ecl2-monopolistic-competition", questions=build(V4, 204)))

# ------------------------------------------------------------------ Oligopoly
V5 = [
    Q("The key feature that distinguishes oligopoly from other market structures is:", "Interdependence: each firm must consider rivals' reactions",
      [("Homogeneous products", "Oligopoly products may be homogeneous or differentiated."), ("Freedom of entry", "Oligopoly usually has significant barriers."), ("Price-taking behaviour", "Oligopolists are price makers.")],
      [("Interdependence", "With few large firms, one firm's decision changes its rivals' sales.")], "Interdependence", "Recall", "What must an oligopolist think about before changing price?"),
    N("Market shares are 30%, 22%, 18%, 12% and 18% for all other firms together. What is the four-firm concentration ratio (%)?", 82,
      [("Add", "30 + 22 + 18 + 12 = 82%.")], "Concentration ratio", "Calculation", "Add the four largest shares.", tol=0, unit="%"),
    Q("In the kinked demand curve model, demand above the current price is elastic because:", "Rivals do not follow a price rise, so the firm loses many customers",
      [("Rivals follow a price rise", "If they followed, the firm would lose few customers."), ("The government sets a maximum price", "The model has no price control."), ("Consumers have brand loyalty", "Loyalty would make demand less elastic.")],
      [("Assumption", "Rises are not matched (elastic), cuts are matched (inelastic).")], "Kinked demand curve", "Concept", "How do rivals react to a price rise?"),
    Q("Why can MC rise without changing the price in the kinked demand model?", "MC can move within the vertical gap in MR at the kink",
      [("Because MR is horizontal", "MR is discontinuous, not horizontal."), ("Because oligopolists ignore costs", "They still set MC = MR."), ("Because demand is perfectly inelastic", "Demand is kinked, not perfectly inelastic.")],
      [("Gap", "Any MC passing through the gap gives the same MC = MR output and price.")], "Price rigidity", "Reasoning", "Look at MR at the kink.", diagram="alecl2-kinked-demand.svg", alt="Kinked demand curve with a vertical gap in MR at output Q∗; two MC curves pass through the gap."),
    Q("Payoffs (A, B): both high price (50, 50); A high, B low (20, 70); A low, B high (70, 20); both low (30, 30). What is the Nash equilibrium?", "Both set a low price",
      [("Both set a high price", "Each could gain by switching to a low price (70 > 50)."), ("A high, B low", "A would switch to low (30 > 20)."), ("There is none", "Both low is a Nash equilibrium: neither gains by changing alone.")],
      [("Dominant strategy", "Low price is best for each firm whatever the other does."), ("Nash", "At (low, low) a move by either alone gives 20 < 30.")], "Game theory", "Application", "Find each firm's best reply to each choice of the other."),
    Q("Why do cartels tend to be unstable?", "Each member can raise its own profit by secretly producing more than its quota",
      [("Members always have identical costs", "Identical costs would make agreement easier, not harder."), ("Cartels earn less than competitive firms", "Cartels aim to earn more, as a joint monopoly."), ("Demand for cartel products is perfectly elastic", "A cartel faces the downward-sloping market demand.")],
      [("Incentive to cheat", "At the high cartel price, extra sales are very profitable for one member: a prisoners' dilemma.")], "Collusion and cartels", "Reasoning", "What does each member gain by breaking the agreement?"),
    Q("A large brewer raises its price and the smaller brewers soon raise theirs by the same amount, without any agreement. This is:", "Tacit collusion through price leadership",
      [("A formal cartel", "A cartel is an explicit agreement."), ("Perfect competition", "Brewers here have price-setting power."), ("Limit pricing", "Limit pricing keeps price low to deter entry.")],
      [("Price leadership", "A dominant firm sets the price and the others follow without a formal agreement.")], "Tacit collusion", "Application", "Is there an agreement?"),
    Q("Which is a weakness of the kinked demand curve model?", "It does not explain how the price at the kink was set in the first place",
      [("It cannot explain price rigidity", "Explaining rigidity is its main strength."), ("It assumes many firms", "It is a model of oligopoly."), ("It ignores MR", "The MR gap is central to it.")],
      [("Evaluation", "The model starts from an existing price; it also assumes fixed reactions, and rivals often follow rises in common costs.")], "Evaluation of oligopoly models", "Reasoning", "What does the model take as given?"),
]
SETS.append(practice_set(module=M_MKT, topic=T_OLI, title="Interdependence, kinked demand, collusion and games", lesson="ecl2-oligopoly", questions=build(V5, 205)))

# ------------------------------------------------------------------ Contestable markets
V6 = [
    Q("A market is perfectly contestable when:", "There are no barriers to entry or exit and no sunk costs",
      [("There are many firms selling a homogeneous product", "That describes perfect competition."), ("There is a single firm with a patent", "A patent is a barrier to entry."), ("Firms collude to fix prices", "Collusion is about conduct, not contestability.")],
      [("Definition", "Free and costless entry and exit make the threat of entry real.")], "Definition", "Recall", "Contestability is about entry and exit."),
    Q("Which of these costs is a sunk cost for a new bus operator?", "A radio advertising campaign to launch the service",
      [("The purchase of buses that can be resold", "Resaleable assets are recoverable."), ("The daily fuel bill", "Fuel is a variable cost that stops when the firm stops."), ("Drivers' wages", "Wages stop when the firm leaves.")],
      [("Sunk", "Advertising spending cannot be recovered on exit.")], "Sunk costs", "Application", "Which cost cannot be recovered on exit?"),
    Q("In a perfectly contestable market with only one firm, the firm will:", "Earn only normal profit, because supernormal profit would attract hit-and-run entry",
      [("Charge the monopoly price", "That would invite entry."), ("Make a loss to deter entry", "It need only set price equal to average cost."), ("Charge a price below marginal cost", "That is not needed and would cause losses.")],
      [("Threat of entry", "The incumbent keeps P = AC to give entrants nothing to take.")], "Outcome of contestability", "Concept", "What does the threat of entry do?"),
    N("An entrant expects supernormal profit of 2 million FCFA a month for 3 months. Sunk costs of entry are 1.5 million FCFA. What is its expected net gain, in millions of FCFA?", 4.5,
      [("Gain", "2 × 3 = 6 million."), ("Net", "6 − 1.5 = 4.5 million: entry pays.")], "Hit-and-run entry", "Calculation", "Multiply monthly profit by months, then subtract sunk costs.", tol=0.01, unit="million FCFA"),
    N("An entrant expects 800 000 FCFA a month of supernormal profit, but incumbents can respond within 2 months. Sunk costs are 2 500 000 FCFA. What is the expected net gain (FCFA)? Give a negative number for a loss.", -900000,
      [("Gain", "800 000 × 2 = 1 600 000."), ("Net", "1 600 000 − 2 500 000 = −900 000 FCFA: entry does not pay.")], "Hit-and-run entry", "Calculation", "Profit while the window is open, minus sunk costs.", tol=0, unit="FCFA"),
    Q("An incumbent with AC of 4 000 FCFA faces a possible entrant with AC of 4 400 FCFA. Which price deters entry while keeping some profit?", "About 4 400 FCFA",
      [("About 3 800 FCFA", "That is below the incumbent's own AC: a loss."), ("About 5 200 FCFA", "That would let the entrant make profit."), ("Exactly 4 000 FCFA", "That deters entry but gives up all supernormal profit unnecessarily.")],
      [("Limit price", "At the entrant's AC the entrant earns nothing, while the incumbent earns 400 FCFA a unit.")], "Limit pricing", "Application", "What price leaves the entrant with no profit?"),
    Q("According to contestable markets theory, competition policy should mainly:", "Reduce barriers to entry and exit",
      [("Break up every large firm", "Size alone is not the problem if the market is contestable."), ("Fix the prices of all oligopolists", "Price control is unnecessary where entry disciplines firms."), ("Nationalize large firms", "The theory points to entry conditions, not ownership.")],
      [("Policy", "Remove licences, open access to networks, end exclusive contracts.")], "Policy implications", "Reasoning", "What creates the discipline in a contestable market?"),
    Q("Which is the strongest criticism of the theory of contestable markets?", "Few markets have zero sunk costs, and incumbents can cut prices quickly when entry occurs",
      [("It assumes too many firms", "It can apply to one firm."), ("It ignores entry", "Entry is at its centre."), ("It predicts supernormal profit for incumbents", "It predicts normal profit.")],
      [("Evaluation", "Sunk costs and fast reactions make hit-and-run entry risky, so real markets are less contestable.")], "Evaluation", "Reasoning", "Are the conditions realistic?"),
]
SETS.append(practice_set(module=M_MKT, topic=T_CON, title="Sunk costs, hit-and-run entry and limit pricing", lesson="ecl2-contestable-markets", questions=build(V6, 206)))

# ------------------------------------------------------------------ MRP and the demand for factors
V7 = [
    Q("The demand for labour is described as a derived demand because:", "It depends on the demand for the goods that labour helps to produce",
      [("It is derived from the wage rate", "The wage is the price of labour, not the source of its demand."), ("It comes from workers' demand for leisure", "That is related to labour supply."), ("It is set by the government", "Firms demand labour; the state does not set it.")],
      [("Definition", "Firms hire workers because the output they produce can be sold.")], "Derived demand", "Recall", "Why does a farmer hire pickers?"),
    N("A worker's marginal physical product is 10 loaves a day and the price of a loaf is 500 FCFA in a competitive market. What is the marginal revenue product in FCFA?", 5000,
      [("Formula", "MRP = MPP × P = 10 × 500 = 5 000 FCFA.")], "MRP calculation", "Calculation", "Multiply output by price.", tol=0, unit="FCFA"),
    Q("A firm's MRP of the next worker is 5 400 FCFA and the daily wage is 5 000 FCFA. The firm should:", "Hire the worker",
      [("Not hire, because MRP is above the wage", "That reverses the rule: MRP above the wage adds to profit."), ("Hire only if ARP equals the wage", "The rule compares MRP with the wage, not ARP."), ("Cut the wage to 4 000 first", "Wage cuts are not part of the hiring rule.")],
      [("Rule", "Hire while MRP ≥ MRC (the wage). The worker adds 400 FCFA to profit.")], "Hiring rule", "Application", "Compare MRP with the wage."),
    N("Output with 1 to 5 workers is 8, 18, 26, 32, 36 units. The price is 700 FCFA a unit in a competitive market and the daily wage is 4 500 FCFA. How many workers should be hired?", 3,
      [("MRP", "MPP = 8, 10, 8, 6, 4, so MRP = 5 600, 7 000, 5 600, 4 200, 2 800."), ("Rule", "The 3rd worker's MRP (5 600) is above 4 500; the 4th (4 200) is below. Hire 3.")], "Number of workers hired", "Calculation", "Find MRP for each extra worker.", tol=0, unit="workers"),
    N("A firm must cut its price to sell more. With 3 workers it sells 32 units at 560 FCFA; with 4 workers it sells 40 units at 540 FCFA. Calculate the MRP of the 4th worker in FCFA.", 3680,
      [("Revenues", "32 × 560 = 17 920; 40 × 540 = 21 600."), ("MRP", "21 600 − 17 920 = 3 680 FCFA.")], "MRP with falling price", "Calculation", "MRP is the change in total revenue.", tol=0, unit="FCFA"),
    Q("Which would shift the demand curve for labour in a factory to the right?", "A rise in the price of the factory's product",
      [("A rise in the wage rate", "That causes a movement along the demand curve, not a shift."), ("A fall in labour productivity", "That lowers MRP and shifts demand left."), ("A fall in demand for the product", "That lowers MRP and shifts demand left.")],
      [("Shift", "A higher product price raises MRP at every level of employment.")], "Shifts in labour demand", "Concept", "What changes MRP?"),
    Q("The demand for labour is likely to be more elastic when:", "Machines can easily be substituted for workers",
      [("Labour is a very small part of total cost", "A small share makes demand less elastic."), ("Demand for the product is highly inelastic", "That makes labour demand less elastic."), ("The time period is very short", "A longer time period makes demand more elastic.")],
      [("Marshall's rules", "Easy substitution lets firms switch away from labour when wages rise.")], "Elasticity of demand for labour", "Concept", "Think about alternatives to workers."),
    Q("Which is a limitation of MRP theory?", "The output of one worker is hard to measure in teams and in the public sector",
      [("It assumes workers are paid more than they produce", "It says the wage equals MRP at the margin."), ("It ignores the demand for the product", "Product demand is central to MRP."), ("It cannot be applied to any firm", "It works best for firms selling output in markets.")],
      [("Evaluation", "Where output is not sold or is made by teams, MRP cannot be measured in money.")], "Evaluation of MRP theory", "Reasoning", "Think about nurses or civil servants."),
]
SETS.append(practice_set(module=M_DIS, topic=T_MRP, title="MPP, MRP and the hiring rule", lesson="ecl2-marginal-revenue-product", questions=build(V7, 207)))

# ------------------------------------------------------------------ Wage determination and trade unions
V8 = [
    Q("A monopsony is a market with:", "A single buyer, such as one employer of labour",
      [("A single seller", "That is monopoly."), ("Two sellers", "That is duopoly."), ("Many buyers and many sellers", "That is competition.")],
      [("Definition", "Monopsony: one buyer.")], "Monopsony", "Recall", "Mono means one; which side?"),
    N("A plantation is the only employer. The labour supply curve is W = 1 000 + 100L. Its marginal cost of labour is MCL = 1 000 + 200L. What is MCL (FCFA) at L = 20 workers?", 5000,
      [("Substitute", "1 000 + 200 × 20 = 5 000 FCFA. This is above the wage of 3 000, because raising pay for one worker means raising it for all.")], "Marginal cost of labour", "Calculation", "Substitute L = 20 into MCL.", tol=0, unit="FCFA"),
    N("With MRP = 7 000 − 100L and MCL = 1 000 + 200L, how many workers does the monopsonist employ?", 20,
      [("Rule", "Hire where MCL = MRP."), ("Solve", "1 000 + 200L = 7 000 − 100L, so 300L = 6 000 and L = 20.")], "Monopsony employment", "Calculation", "Set MCL equal to MRP.", tol=0, unit="workers"),
    N("For the same market, what wage (FCFA a day) does the monopsonist pay, read from the supply curve at L = 20?", 3000,
      [("Wage", "W = 1 000 + 100 × 20 = 3 000 FCFA, less than MRP of 5 000.")], "Monopsony wage", "Calculation", "Read the wage from supply, not from MCL.", tol=0, unit="FCFA"),
    Q("Compared with a competitive labour market, a monopsonist employs:", "Fewer workers at a lower wage",
      [("More workers at a higher wage", "That describes the effect of a union in some cases, not monopsony."), ("The same number at a lower wage", "Employment is also reduced."), ("Fewer workers at a higher wage", "The wage is lower too.")],
      [("Result", "MCL = MRP at a smaller employment than where supply meets MRP.")], "Monopsony outcome", "Concept", "Where is MCL relative to supply?"),
    Q("A union raises the wage above equilibrium in a competitive labour market. The likely result is:", "Higher pay for those employed but fewer jobs",
      [("Higher pay and more jobs", "More jobs happen only in a monopsony."), ("Lower pay and fewer jobs", "The wage rises."), ("No change in employment", "Quantity demanded of labour falls when the wage rises.")],
      [("Trade-off", "Employers demand less labour at the higher wage while more people want jobs.")], "Union effect in competition", "Reasoning", "What happens to quantity demanded when the wage rises?"),
    N("In the monopsony example, a union negotiates a fixed wage of 4 500 FCFA. Using MRP = 7 000 − 100L, how many workers does the employer demand?", 25,
      [("Demand", "MRP = 4 500 gives 7 000 − 100L = 4 500, so L = 25. Supply at 4 500 is 35, so employment is the smaller, 25: above the monopsony level of 20.")], "Union in a monopsony", "Calculation", "Where does MRP equal the union wage?", tol=0, unit="workers"),
    Q("Which is an INTRA-industry wage differential?", "A mining engineer earning more than a labourer in the same mine",
      [("Bank staff earning more than farm workers", "That is between industries."), ("Workers in the capital earning more than workers in a village", "That is a regional differential."), ("Oil workers earning more than teachers", "That is between industries.")],
      [("Definition", "Intra means within: the same industry or firm.")], "Wage differentials", "Application", "Which option compares workers in one industry?"),
]
SETS.append(practice_set(module=M_DIS, topic=T_WAGE, title="Competitive and monopsony labour markets and unions", lesson="ecl2-wage-determination-trade-unions", questions=build(V8, 208)))

# ------------------------------------------------------------------ Economic rent and transfer earnings
V9 = [
    Q("Transfer earnings are:", "The minimum payment needed to keep a factor in its present use",
      [("Any payment above what is needed to keep the factor", "That is economic rent."), ("The rent paid for a house", "That is commercial rent."), ("The money a factor sends abroad", "That is an unrelated meaning of 'transfer'.")],
      [("Definition", "What the factor could earn in its next best use.")], "Transfer earnings", "Recall", "What would make the factor move?"),
    N("A mechanic earns 150 000 FCFA a month. His next best alternative is driving a taxi for 110 000 FCFA. What is his economic rent per month, in FCFA?", 40000,
      [("Subtract", "150 000 − 110 000 = 40 000 FCFA.")], "Economic rent calculation", "Calculation", "Earnings minus transfer earnings.", tol=0, unit="FCFA"),
    Q("If the supply of a factor is perfectly inelastic, its earnings are:", "All economic rent",
      [("All transfer earnings", "That describes perfectly elastic supply."), ("Equal parts rent and transfer earnings", "The split depends on elasticity."), ("Zero", "The factor still earns what demand allows.")],
      [("Vertical supply", "The factor has no alternative use, so everything it is paid is surplus.")], "Elasticity and rent", "Concept", "What is the minimum needed to keep a factor that cannot move?"),
    N("The supply of labour is W = 2 000 + 50L (W in FCFA a day) and the market wage is 5 000 FCFA. How many workers are employed?", 60,
      [("Solve", "5 000 = 2 000 + 50L, so L = 60.")], "Market employment", "Calculation", "Set W = 5 000 in the supply equation.", tol=0, unit="workers"),
    N("For this market (supply W = 2 000 + 50L, wage 5 000, 60 workers), calculate total economic rent in FCFA a day.", 90000,
      [("Triangle", "Rent is the triangle above the supply curve: ½ × (5 000 − 2 000) × 60 = 90 000 FCFA.")], "Economic rent in a market", "Calculation", "The area between the wage line and the supply curve.", tol=0, unit="FCFA"),
    Q("A tax that takes only economic rent from a factor will:", "Not change the supply of the factor, because transfer earnings are untouched",
      [("Reduce the supply by the amount of the tax", "The factor still earns enough to stay."), ("Raise the supply, because pay rises", "A tax does not raise pay."), ("Make supply perfectly elastic", "It leaves the shape of supply unchanged.")],
      [("Policy", "The factor still receives its transfer earnings, so it stays.")], "Taxing economic rent", "Reasoning", "What is the factor paid after the tax?"),
    Q("Quasi-rent is:", "Economic rent earned in the short run while the supply of a factor is fixed",
      [("Rent paid on land by a tenant", "That is commercial rent."), ("The same as transfer earnings", "Transfer earnings are the minimum payment."), ("A tax on rent", "It is a type of earnings, not a tax.")],
      [("Definition", "Associated with Marshall: short-run surplus that more supply competes away.")], "Quasi-rent", "Recall", "Short run or long run?"),
    Q("Which statement best distinguishes economic rent from commercial rent?", "Economic rent is a surplus over transfer earnings that any factor can earn, whereas commercial rent is the price paid for the use of property",
      [("Economic rent is paid only to landowners, whereas commercial rent is paid to workers", "Economic rent can be earned by any factor."), ("They are the same thing", "They have different meanings."), ("Commercial rent is a surplus, whereas economic rent is a cost", "Economic rent is the surplus.")],
      [("Distinction", "Use 'whereas' and state both sides.")], "Economic against commercial rent", "Concept", "One is a surplus, the other a payment for use."),
]
SETS.append(practice_set(module=M_DIS, topic=T_RENT, title="Rent, transfer earnings and supply elasticity", lesson="ecl2-economic-rent-transfer-earnings", questions=build(V9, 209)))

# ------------------------------------------------------------------ Interest
V10 = [
    Q("The real rate of interest is approximately:", "The nominal rate minus the rate of inflation",
      [("The nominal rate plus inflation", "Inflation reduces the real return, not raises it."), ("The rate of inflation minus the nominal rate", "The order is reversed."), ("The central bank's rate", "That is one nominal rate.")],
      [("Formula", "r ≈ i − π.")], "Real interest rate", "Recall", "What does inflation do to the value of repayments?"),
    N("A bank pays 7% a year on a deposit and inflation is 3%. What is the approximate real rate of interest (%)?", 4,
      [("Subtract", "7 − 3 = 4%.")], "Real interest rate", "Calculation", "Nominal minus inflation.", tol=0.05, unit="%"),
    N("Loanable funds: supply S = 100 + 20r and demand I = 400 − 10r (r in %). What is the equilibrium rate of interest (%)?", 10,
      [("Solve", "100 + 20r = 400 − 10r, so 30r = 300 and r = 10%.")], "Loanable funds equilibrium", "Calculation", "Set supply equal to demand.", tol=0, unit="%"),
    N("Households save more so that S = 160 + 20r (demand unchanged, I = 400 − 10r). What is the new equilibrium rate (%)?", 8,
      [("Solve", "160 + 20r = 400 − 10r, so 30r = 240 and r = 8%: more saving lowers the rate.")], "Effect of saving on the rate", "Calculation", "Solve the new equation.", tol=0, unit="%"),
    Q("According to Keynes, which balances are IDLE balances?", "Money held for the speculative motive",
      [("Money held for transactions", "That is an active balance."), ("Money held for precautions", "That is an active balance."), ("All money held in banks", "Idle balances are defined by the motive, not the place.")],
      [("Definition", "Idle balances are held as a store of wealth awaiting a better use, depending on the interest rate.")], "Active and idle balances", "Concept", "Which motive responds to the interest rate?"),
    N("A bond pays a fixed 4 000 FCFA a year for ever. The market rate of interest is 8%. What is its price in FCFA?", 50000,
      [("Formula", "Price = 4 000 ÷ 0.08 = 50 000 FCFA.")], "Bond price", "Calculation", "Divide the yearly payment by the rate.", tol=0, unit="FCFA"),
    Q("When the rate of interest rises, the price of existing bonds:", "Falls",
      [("Rises", "A fixed payment is worth less when new loans pay more."), ("Is unchanged", "The price adjusts to give the market rate."), ("Doubles", "There is no such rule.")],
      [("Inverse link", "Price = payment ÷ rate, so a higher rate means a lower price.")], "Bond prices and interest", "Concept", "Price = payment ÷ rate."),
    Q("In the liquidity trap:", "Extra money supply is held as idle money and cannot lower the interest rate further",
      [("Extra money supply always lowers the rate", "At very low rates it does not."), ("People spend all extra money on goods", "They hold it idle."), ("The central bank cannot print money", "It can, but it does not lower the rate.")],
      [("Trap", "At low rates people expect bond prices to fall and prefer to hold money: the L curve is flat.")], "Liquidity trap", "Reasoning", "What do people expect about bond prices at very low rates?"),
]
SETS.append(practice_set(module=M_DIS, topic=T_INT, title="Loanable funds and liquidity preference", lesson="ecl2-interest", questions=build(V10, 210)))

# ------------------------------------------------------------------ Profit
V11 = [
    Q("Which statement about profit is correct?", "It is a residual reward to the entrepreneur and can be negative",
      [("It is agreed in advance like a wage", "Profit is what remains after other payments."), ("It can never be negative", "Losses are negative profit."), ("It is the same as interest", "Interest is the reward to capital.")],
      [("Definition", "Profit is paid after other factors; it can fall below zero.")], "Nature of profit", "Recall", "Is profit contracted in advance?"),
    N("A shop has revenue of 12 million FCFA and explicit costs of 9 million FCFA. What is its accounting profit in millions of FCFA?", 3,
      [("Subtract", "12 − 9 = 3 million FCFA.")], "Accounting profit", "Calculation", "Revenue minus explicit costs.", tol=0, unit="million FCFA"),
    N("The owner of the same shop gave up a salary of 1.8 million FCFA and has 5 million FCFA of her own savings in the shop, which could earn 10% a year elsewhere. What is the economic profit in millions of FCFA?", 0.7,
      [("Implicit costs", "1.8 + 0.10 × 5 = 2.3 million FCFA."), ("Economic profit", "3 − 2.3 = 0.7 million FCFA.")], "Economic profit", "Calculation", "Subtract implicit costs from accounting profit.", tol=0.01, unit="million FCFA"),
    Q("Normal profit is:", "The opportunity cost of the entrepreneur's time and capital, included in economic cost",
      [("Profit above total cost", "That is supernormal profit."), ("The profit shown in published accounts", "That is accounting profit."), ("A tax on profit", "It is not a tax.")],
      [("Definition", "It is the minimum reward to keep the entrepreneur in the industry.")], "Normal profit", "Concept", "Is it inside or outside economic cost?"),
    Q("Which theory links profit with introducing new products and methods?", "Schumpeter's innovation theory",
      [("Knight's uncertainty theory", "That links profit with bearing uncertainty."), ("The monopoly theory", "That links profit with market power."), ("The loanable funds theory", "That is a theory of interest.")],
      [("Attribution", "Schumpeter's innovating entrepreneur earns temporary profit until imitators arrive.")], "Theories of profit", "Recall", "Which entrepreneur creates something new?"),
    Q("In Knight's theory, profit is the reward for bearing:", "Uncertainty that cannot be insured",
      [("Any risk, including insurable risk", "Insurable risks become a cost through premiums."), ("Taxes", "Taxes are a cost."), ("The costs of labour", "Wages are the reward to labour.")],
      [("Risk and uncertainty", "Risks that can be calculated and insured are costs; uncertainty is not.")], "Uncertainty theory", "Concept", "What cannot be insured?"),
    Q("A rise in profits in the poultry industry encourages more resources to move into it. This shows the role of profit as:", "A signal",
      [("A tax", "It is not a tax."), ("A cost", "Here it is information."), ("A subsidy", "It is not a payment from the government.")],
      [("Function", "High profit tells resources where consumers want more output.")], "Functions of profit", "Application", "What information does profit carry?"),
    Q("A critic says high profits are harmful. Which is the strongest evidence for the critic?", "Profits that come from market power and high prices that cause a deadweight loss",
      [("Profits that come from successful innovation", "Innovation is usually seen as a benefit."), ("Profits that fund new investment", "That is a benefit."), ("Profits as a reward for risk", "That is a justification, not a criticism.")],
      [("Evaluation", "Monopoly profit raises prices above cost and cuts output.")], "Evaluation of profit", "Reasoning", "Which profit comes at consumers' expense?"),
]
SETS.append(practice_set(module=M_DIS, topic=T_PROF, title="Accounting and economic profit, and the theories of profit", lesson="ecl2-profit-theories", questions=build(V11, 211)))

# ------------------------------------------------------------------ Public, merit and demerit goods
V12 = [
    Q("A good that is non-rival and non-excludable is a:", "Pure public good",
      [("Private good", "Private goods are rival and excludable."), ("Merit good", "Merit goods are under-consumed but usually rival and excludable."), ("Demerit good", "Demerit goods are over-consumed.")],
      [("Definition", "Both features together define a pure public good.")], "Public goods", "Recall", "Check both tests."),
    Q("The free-rider problem arises with public goods because:", "People cannot be excluded, so each hopes others will pay",
      [("Public goods are too expensive for anyone", "Cost alone is not the problem."), ("Public goods are rival", "They are non-rival."), ("Consumers pay too much", "The problem is that they pay too little or nothing.")],
      [("Free riding", "If you benefit whether or not you pay, you have no reason to pay.")], "Free-rider problem", "Concept", "What happens when nobody can be excluded?"),
    N("Three households value a street light at 3 000, 2 500 and 1 500 FCFA a month. It costs 6 000 FCFA a month to run. What is the net social benefit of providing it, in FCFA a month?", 1000,
      [("Total value", "3 000 + 2 500 + 1 500 = 7 000, because a non-rival good is enjoyed by all."), ("Net", "7 000 − 6 000 = 1 000 FCFA.")], "Public good valuation", "Calculation", "Add the values: all three enjoy the same light.", tol=0, unit="FCFA"),
    Q("A toll motorway is best described as:", "A quasi-public good: non-rival until congested but excludable by tolls",
      [("A pure public good", "Tolls make it excludable."), ("A demerit good", "Roads are not harmful goods."), ("A common resource", "It is excludable, unlike a common resource.")],
      [("Classification", "It has some, but not all, public-good features.")], "Quasi-public goods", "Application", "Can people be excluded?"),
    Q("Public schools and hospitals are:", "Merit goods provided by the state",
      [("Pure public goods", "They are rival and excludable."), ("Demerit goods", "They are beneficial."), ("Private goods that cannot be provided publicly", "Many governments do provide them.")],
      [("Classification", "Government provision does not make a good public.")], "Merit goods", "Concept", "Is a hospital bed rival?"),
    Q("Merit goods are under-consumed in a free market mainly because of:", "Information failure and positive externalities",
      [("Free riding on a non-excludable good", "That explains public goods."), ("Perfect information", "Perfect information would reduce the problem."), ("Excessive advertising", "That is not the core reason.")],
      [("Cause", "People underestimate private benefits and ignore benefits to others.")], "Merit goods", "Reasoning", "What do consumers not fully know?"),
    Q("A high tax on cigarettes reduces smoking only slightly. The most likely reason is:", "Demand is price inelastic because of addiction",
      [("Demand is perfectly elastic", "Then consumption would fall sharply."), ("Cigarettes are public goods", "They are private goods."), ("The tax shifts demand to the right", "A tax shifts supply, and demand is unchanged.")],
      [("Elasticity", "With inelastic demand, a price rise reduces quantity only a little.")], "Taxing demerit goods", "Application", "How much do addicted buyers cut back?"),
    Q("Fish in an open lake that anyone may catch are:", "A common resource: non-excludable but rival",
      [("A pure public good", "One person's catch reduces what others can take."), ("A private good", "Nobody can be excluded."), ("A merit good", "They are not defined by under-consumption.")],
      [("Classification", "Over-use is a risk because users ignore the effect on others.")], "Common resources", "Application", "Is one person's catch available to others?"),
]
SETS.append(practice_set(module=M_MF, topic=T_PUB, title="Public goods, free riders, merit and demerit goods", lesson="ecl2-public-merit-demerit-goods", questions=build(V12, 212)))

# ------------------------------------------------------------------ Externalities
V13 = [
    Q("An externality is:", "A cost or benefit that falls on a third party and is not reflected in the market price",
      [("Any cost paid by a producer", "That is a private cost."), ("A tax paid to the government", "A tax is a policy instrument."), ("Profit earned by a monopolist", "Profit is the owner's reward.")],
      [("Definition", "Externalities affect people outside the transaction.")], "Externalities", "Recall", "Who is the third party?"),
    Q("Marginal social cost equals:", "Marginal private cost plus marginal external cost",
      [("Marginal private cost minus marginal external cost", "External costs add to private cost."), ("Marginal private benefit", "That is on the demand side."), ("Marginal external benefit", "That is on the benefit side.")],
      [("Identity", "MSC = MPC + MEC.")], "Marginal social cost", "Concept", "Social includes private and external."),
    N("Demand is P = 100 − Q and the firms' MPC is P = 20 + Q. What is the free-market output Qm?", 40,
      [("Solve", "100 − Q = 20 + Q, so Q = 40.")], "Market equilibrium", "Calculation", "The market uses MPC.", tol=0),
    N("Each unit also causes an external cost of 20, so MSC = 40 + Q. What is the socially optimal output Q∗?", 30,
      [("Solve", "100 − Q = 40 + Q, so Q = 30.")], "Social optimum", "Calculation", "Social optimum: MSB = MSC.", tol=0),
    N("Using the two outputs above (40 and 30) and an external cost of 20 a unit, calculate the welfare loss.", 100,
      [("Triangle", "½ × 20 × (40 − 30) = 100.")], "Welfare loss", "Calculation", "A triangle with base 10 and height 20.", tol=0),
    Q("In the diagram, which output is the social optimum?", "Qa, where demand meets MSC",
      [("Qb, where demand meets MPC", "That is the market output."), ("Neither: social optimum is at the origin", "Zero output is not optimal."), ("Both are optimal", "Only one point has MSB = MSC.")],
      [("Reading", "The higher cost curve is MSC; it meets demand at the smaller output, Qa.")], "Reading an externality diagram", "Interpretation", "Which curve includes the external cost?",
      diagram="alecl2-neg-ext-q.svg", alt="Demand, a lower supply curve and a higher parallel curve. The higher curve meets demand at Qa; the lower curve meets demand at Qb, to the right."),
    N("Private demand for a vaccine is P = 80 − Q, MSB = 100 − Q and MC = 20 + Q. What is the socially optimal output?", 40,
      [("Solve", "100 − Q = 20 + Q, so Q = 40 (the market gives 30).")], "Positive externality", "Calculation", "Use the social benefit curve.", tol=0),
    Q("Which makes externalities hard to correct in practice?", "It is difficult to value them in money and the affected people are often many and scattered",
      [("They are always zero", "That is false."), ("Producers always pay for them", "Then they would not be externalities."), ("The market price already includes them", "By definition it does not.")],
      [("Evaluation", "Measurement and the number of third parties complicate policy.")], "Measuring externalities", "Reasoning", "How would you price a damaged river?"),
]
SETS.append(practice_set(module=M_MF, topic=T_EXT, title="Private and social costs and benefits, and the welfare loss", lesson="ecl2-externalities", questions=build(V13, 213)))

# ------------------------------------------------------------------ Taxes, subsidies and pollution permits
V14 = [
    Q("A specific indirect tax on a good shifts:", "The supply curve upwards by the amount of the tax",
      [("The demand curve to the left by the tax", "The tax is collected from sellers, so supply shifts."), ("Both curves to the right", "Neither shifts right."), ("The supply curve downwards", "That describes a subsidy.")],
      [("Shift", "Each unit costs the seller an extra tax, so supply moves up.")], "Effect of a tax", "Concept", "Who pays the tax to the government?"),
    N("Demand is P = 100 − Q and supply is P = 20 + Q. A tax of 20 FCFA a unit is imposed. What is the new equilibrium quantity?", 30,
      [("New supply", "P = 40 + Q."), ("Solve", "100 − Q = 40 + Q, so Q = 30.")], "Tax and quantity", "Calculation", "Add the tax to the supply equation.", tol=0),
    N("Using the same figures, what is the tax revenue in FCFA (Q in thousands, so give the answer in thousands of FCFA)?", 600,
      [("Revenue", "20 × 30 = 600 thousand FCFA.")], "Tax revenue", "Calculation", "Tax per unit times quantity sold.", tol=0, unit="thousand FCFA"),
    N("Demand P = 100 − Q, supply P = 20 + Q, tax 20. By how much does the price paid by buyers rise (FCFA)?", 10,
      [("Prices", "Before: 60. After: 70. Rise: 10 (half the tax).")], "Tax incidence", "Calculation", "Compare the old and new equilibrium prices.", tol=0, unit="FCFA"),
    Q("A tax is most likely to be paid mainly by buyers when:", "Demand is price inelastic",
      [("Demand is price elastic", "Then sellers must absorb more of the tax."), ("Supply is perfectly inelastic", "That would put the burden on sellers."), ("The tax is very small", "The size does not decide the split.")],
      [("Incidence", "The less elastic side bears more.")], "Tax incidence", "Concept", "Who cannot easily switch away?"),
    N("A per-unit subsidy of 20 shifts supply to P = Q with demand P = 100 − Q. What is the cost of the subsidy to the government, in thousands of FCFA (Q in thousands)?", 1000,
      [("New equilibrium", "100 − Q = Q, so Q = 50."), ("Cost", "20 × 50 = 1 000.")], "Subsidy cost", "Calculation", "Subsidy per unit times quantity.", tol=0, unit="thousand FCFA"),
    Q("A Pigovian tax is correctly set when it equals:", "The marginal external cost at the social optimum",
      [("The producer's profit", "Profit is unrelated."), ("The price of the good", "That would be far too high."), ("The marginal private cost", "That is already paid by the producer.")],
      [("Rule", "The tax makes MPC plus tax equal MSC.")], "Pigovian tax", "Concept", "What cost is being left out?"),
    Q("In a cap-and-trade scheme, a lower cap with unchanged demand for permits will:", "Raise the price of permits",
      [("Lower the price of permits", "Scarcer permits cost more."), ("Raise total emissions", "Emissions are limited to the cap."), ("Abolish the market in permits", "The market continues, with fewer permits.")],
      [("Supply and demand", "Vertical supply moves left, so price rises.")], "Pollution permits", "Application", "Where does the supply curve of permits lie?"),
]
SETS.append(practice_set(module=M_MF, topic=T_TAX, title="Taxes, subsidies, incidence and permits", lesson="ecl2-taxes-subsidies-permits", questions=build(V14, 214)))

# ------------------------------------------------------------------ Regulation, privatization and nationalization
V15 = [
    Q("A natural monopoly exists when:", "Average cost keeps falling over the whole range of market demand",
      [("The government grants a patent", "That is a legal monopoly."), ("Many firms sell a differentiated product", "That is monopolistic competition."), ("Marginal cost is rising", "Rising MC at small output does not give natural monopoly.")],
      [("Definition", "One firm can supply the market at lower cost than two.")], "Natural monopoly", "Recall", "Think about cost conditions."),
    N("A natural monopoly faces P = 100 − Q with MC = 20. At what output does it maximize profit (MR = 100 − 2Q)?", 40,
      [("Solve", "100 − 2Q = 20, so Q = 40 and P = 60.")], "Unregulated monopoly", "Calculation", "Set MR = MC.", tol=0),
    N("If the regulator sets a price equal to average cost (AC = 20 + 1 200/Q), the output is 60 (the other root, 20, is not used). What is the price (FCFA)?", 40,
      [("Price", "P = 100 − 60 = 40 = 20 + 1 200/60. Normal profit only.")], "P = AC regulation", "Calculation", "Read the price from demand at Q = 60.", tol=0, unit="FCFA"),
    Q("If a regulator forces a natural monopoly to price at marginal cost, the firm:", "Makes a loss and may need a subsidy",
      [("Earns supernormal profit", "Price is below average cost, so there is a loss."), ("Earns normal profit", "That is the P = AC case."), ("Shuts down in the long run without any problem", "It needs a subsidy to continue.")],
      [("Result", "AC is above MC for a natural monopoly.")], "P = MC pricing", "Concept", "Compare AC with MC."),
    N("A water company charges 500 FCFA. Inflation is 5% and the regulator sets X = 2. What is the maximum price after the cap is applied (FCFA)?", 515,
      [("RPI − X", "5% − 2% = 3%."), ("New price", "500 × 1.03 = 515.")], "Price cap", "Calculation", "The allowed rise is inflation minus X.", tol=0.5, unit="FCFA"),
    Q("Which is a common argument for privatization?", "Competition and the profit motive may reduce costs",
      [("It guarantees lower prices with no regulation", "Private monopolies may raise prices."), ("It raises taxpayers' losses", "Privatization usually aims to reduce them."), ("It removes the need for competition policy", "Regulation is still needed.")],
      [("Argument", "Private owners have a stronger reason to cut costs.")], "Privatization", "Concept", "What drives private firms?"),
    Q("Which is an argument for nationalizing a natural monopoly?", "It can be run in the public interest, with universal service",
      [("It always raises efficiency", "State firms may be X-inefficient."), ("It removes political influence", "The state may use it for political aims."), ("It raises competition", "A state monopoly has no rivals.")],
      [("Argument", "The state can serve social goals and avoid private monopoly profit.")], "Nationalization", "Concept", "What does the state aim at?"),
    Q("Government failure means:", "Intervention that makes the allocation of resources worse than the market outcome",
      [("The market has failed to provide a public good", "That is market failure."), ("A government has no budget", "That is a fiscal problem."), ("A firm has made a loss", "That is a business outcome.")],
      [("Definition", "Examples: regulatory capture, lack of information, unintended effects of price controls.")], "Government failure", "Recall", "Is it the market or the state that fails?"),
]
SETS.append(practice_set(module=M_MF, topic=T_REG, title="Regulating monopolies, privatization and nationalization", lesson="ecl2-regulation-privatization-nationalization", questions=build(V15, 215)))

# ------------------------------------------------------------------ Examination: Paper 1 technique
X1 = [
    Q("Before looking at the four options of a multiple-choice question, a good candidate should:", "Read the stem and predict the answer",
      [("Choose the longest option", "Length does not show that an option is correct."), ("Look for options with the word 'always'", "Absolute words are often wrong but you must still check the facts."), ("Skip the stem and read the options", "The stem tells you what is being asked.")],
      [("Routine", "Read, predict, eliminate, check.")], "MCQ routine", "Recall", "What do you do first?"),
    Q("A stem says: 'Which of the following is NOT an assumption of perfect competition?' The correct option is the one that is:", "False as an assumption of perfect competition, such as differentiated products",
      [("The first true statement", "In a NOT question the answer is the false statement."), ("The longest statement", "Length is no clue."), ("The one with a number", "Numbers are no clue.")],
      [("Command", "Test each option and choose the one that is not an assumption.")], "NOT questions", "Concept", "What are you hunting for?"),
    N("TR for outputs 1 to 4 is 60, 110, 150, 180 and TC is 50, 70, 100, 140 (FCFA thousand). What is the profit at the profit-maximizing output, in FCFA thousand?", 50,
      [("Profit", "TR − TC = 10, 40, 50, 40."), ("Maximum", "50 at 3 units.")], "Calculation questions", "Calculation", "Compute profit for each output.", tol=0, unit="FCFA thousand"),
    N("A firm's AR is 80 FCFA and its AC is 70 FCFA at an output of 100 units. What is its profit in FCFA?", 1000,
      [("Per unit", "80 − 70 = 10."), ("Total", "10 × 100 = 1 000 FCFA.")], "Calculation questions", "Calculation", "Profit = (AR − AC) × Q.", tol=0, unit="FCFA"),
    Q("A calculation gives the total revenue (500) when the question asks for the marginal revenue of the 11th unit (40). Which type of wrong option is this?", "An unfinished or wrong-quantity calculation",
      [("A reversed answer", "A reversed answer has the opposite direction."), ("An absolute word", "That is the words 'always' and 'never'."), ("A correct answer", "The question needs MR, not TR.")],
      [("Distractor", "Many wrong options are the answer to a different question.")], "Distractors", "Concept", "Is it the quantity asked for?"),
    Q("A price rise for a good moves us along its demand curve. A rise in consumers' incomes (for a normal good) will:", "Shift the demand curve to the right",
      [("Move along the demand curve upwards", "Only a change in the good's own price moves along the curve."), ("Shift the supply curve to the left", "Income affects demand."), ("Have no effect", "For a normal good, demand rises.")],
      [("Movement or shift", "Own price changes move along; other factors shift.")], "Movement or shift", "Concept", "Is the cause the good's own price?"),
    N("The KKEVO Paper 1 mock has 50 questions in 90 minutes. How many minutes are available for each question, on average?", 1.8,
      [("Divide", "90 ÷ 50 = 1.8 minutes.")], "Time per question", "Calculation", "Divide the total time by the number of questions.", tol=0.01, unit="minutes"),
    Q("Which module covers MRP, economic rent, interest and profit?", "Theory of Distribution & Factor Pricing",
      [("Market Structures", "That module covers perfect competition, monopoly and oligopoly."), ("Theory of Production & Costs", "That module covers returns and cost curves."), ("Market Failure & Government Micro-Intervention", "That module covers public goods, externalities and policy.")],
      [("Revision map", "These are the factor rewards: wages, rent, interest and profit.")], "Revision map", "Recall", "Which module is about incomes of factors?"),
]
SETS.append(practice_set(module=M_EXAM, topic="Paper 1", title="Multiple-choice technique and calculations", lesson="ecl2-paper1-multiple-choice", questions=build(X1, 221)))

# ------------------------------------------------------------------ Examination: Paper 2 technique
X2 = [
    Q("Which word in an essay question tells you that a diagram is required?", "Illustrate (with the help of a diagram)",
      [("State", "State asks for a short fact."), ("Define", "Define asks for a precise meaning."), ("Name", "Name asks for a term.")],
      [("Command words", "The Board's report notes candidates lost marks for not drawing the diagram asked for.")], "Command words", "Recall", "Which word asks you to show?"),
    Q("A question says: 'Distinguish between a perfect competitor and a monopolistic competitor.' Which answer is best?", "A perfect competitor sells a homogeneous product, whereas a monopolistic competitor sells a differentiated product",
      [("A perfect competitor sells a homogeneous product", "This describes only one side."), ("Both are market structures with many firms", "This states a similarity, not a difference."), ("A monopolistic competitor has brands. A perfect competitor has not", "Without a conjunction the difference is weakly stated; use whereas or while.")],
      [("Conjunctions", "Use 'whereas' or 'while' to state both sides.")], "Distinguishing questions", "Application", "Which option states both sides in one sentence?"),
    Q("A question asks for factors that would INCREASE the supply of a good. Which answer is directional?", "A fall in the cost of raw materials raises profit per unit, so more is supplied at each price",
      [("The determinants of supply are costs, technology and taxes", "This lists determinants without direction."), ("Supply is the quantity firms offer at each price", "This only defines supply."), ("Demand depends on income and tastes", "This is about demand.")],
      [("Directional", "State the change, the direction and the effect on supply.")], "Directional questions", "Application", "Which answer says what changes and which way?"),
    Q("On a long-run diagram for a perfect competitor, which feature is correct?", "The horizontal AR = MR line touches the minimum of AC",
      [("AR slopes downward and is tangent to AC", "That is a monopolistic competitor."), ("The firm makes supernormal profit", "Free entry removes it in the long run."), ("The firm makes a loss", "A loss-making diagram is an error reported by the Board.")],
      [("Diagram", "The Board's report noted loss-making and wrongly labelled long-run diagrams.")], "Diagrams", "Application", "What does free entry do to profit?"),
    Q("Which axes should be labelled on an MC and MR profit-maximization diagram?", "Costs and revenue (vertical) and output (horizontal)",
      [("Quantity (vertical) and price (horizontal)", "The axes are reversed."), ("Profit (vertical) and time (horizontal)", "Time is not the variable."), ("Income (vertical) and employment (horizontal)", "That is a macroeconomic diagram.")],
      [("Labelling", "The report noted wrongly labelled axes.")], "Diagram labelling", "Recall", "What do MC and MR measure?"),
    Q("The Board's 2023 report notes some candidates avoided questions on whole topics. The best advice is to:", "Revise the whole syllabus rather than selecting topics",
      [("Revise only your favourite topics", "The report warns against selecting topics."), ("Revise only diagrams", "Explanations are needed as well."), ("Skip evaluation", "Evaluation earns marks in discuss questions.")],
      [("Coverage", "Questions can come from any topic.")], "Topic coverage", "Reasoning", "What did the report say about selecting topics?"),
    N("Paper 2 asks you to answer five of eight questions, with no more than three from either section. What is the smallest number of questions you must answer from the microeconomics section, if you answer three from macroeconomics?", 2,
      [("Total", "Five questions in all."), ("Subtract", "5 − 3 = 2 from microeconomics.")], "Choosing questions", "Calculation", "Total minus the macro questions.", tol=0),
    Q("A 'discuss' question on monopoly earns the highest marks if the answer:", "Gives arguments for and against with a diagram and a reasoned conclusion",
      [("Lists the features of monopoly", "A list does not discuss."), ("Gives only the disadvantages", "A one-sided answer loses evaluation marks."), ("Repeats the definition several times", "Repetition earns nothing.")],
      [("Evaluation", "State both sides and judge.")], "Evaluation", "Reasoning", "What do examiners want in 'discuss'?"),
]
SETS.append(practice_set(module=M_EXAM, topic="Paper 2", title="Command words, diagrams and essay planning", lesson="ecl2-paper2-essays", questions=build(X2, 222)))

# ------------------------------------------------------------------ Examination: Paper 3 technique
X3 = [
    N("A table gives prices in '000 FCFA. At a price of 50 quantity demanded and quantity supplied are both 70 tonnes. What is the market price in FCFA?", 50000,
      [("Units", "50 in '000 FCFA is 50 000 FCFA.")], "Reading units", "Calculation", "Read the units in the table heading.", tol=0, unit="FCFA"),
    Q("How should you justify the market price from a schedule?", "Quantity demanded equals quantity supplied at that price",
      [("Demand equals supply", "The Board's report notes the difference between demand and quantity demanded."), ("The price is the highest in the table", "The market price is the clearing price."), ("The price is the lowest in the table", "That is not the rule.")],
      [("Justify", "Use the precise terms: quantity demanded and quantity supplied.")], "Justifying from data", "Concept", "Which words does the report stress?"),
    N("At the old price the new quantity supplied is 95 tonnes and quantity demanded is 70 tonnes. How many tonnes must the producers' association buy to hold the price?", 25,
      [("Surplus", "95 − 70 = 25 tonnes.")], "Buffer scheme", "Calculation", "Buy the surplus at the supported price.", tol=0, unit="tonnes"),
    Q("A question asks for four other factors that increase the supply of plantains. Which approach is best?", "Four short, separate points about plantains, each stated in the direction of increase",
      [("One long paragraph on supply in general", "The report notes candidates giving general determinants."), ("Repeating the factors in the passage", "Paper 3 is not a reading comprehension paper."), ("Two long explained points", "Four points are asked for.")],
      [("Tags", "Respect the number of points and the context.")], "Directional questions", "Application", "How many points are asked for?"),
    Q("A diagram shows a firm facing a horizontal demand line. Which structure is it?", "Perfect competition",
      [("Monopoly", "A monopoly faces a downward-sloping demand curve."), ("Oligopoly", "An oligopolist has a kinked or downward-sloping curve."), ("Monopolistic competition", "That structure has a downward-sloping curve.")],
      [("Reading", "Horizontal AR = MR means a price taker.")], "Reading diagrams", "Interpretation", "What does a horizontal curve mean for price?"),
    N("A perfect competitor sells 120 units at 500 FCFA. AC at that output is 560 FCFA. What is its profit in FCFA (negative for a loss)?", -7200,
      [("Per unit", "500 − 560 = −60."), ("Total", "−60 × 120 = −7 200 FCFA.")], "Profit from a diagram", "Calculation", "Profit = (P − AC) × Q.", tol=0, unit="FCFA"),
    Q("Why is a short-run loss acceptable for a perfect competitor?", "Price covers average variable cost, so each unit contributes to fixed costs",
      [("Price is below AVC", "Then it should shut down."), ("Fixed costs are zero", "Fixed costs exist in the short run."), ("It earns supernormal profit", "It makes a loss.")],
      [("Condition", "P ≥ AVC.")], "Short-run production decision", "Reasoning", "Which cost must revenue cover?"),
    Q("An answer to a Paper 3 part should be:", "Brief and precise, with units, and about the situation named",
      [("A long essay with a general discussion", "The report stresses brief answers."), ("Copied from the passage", "Repeating the passage earns no marks."), ("Left blank if the data are in thousands", "Units must be read, not avoided.")],
      [("Technique", "Short, directional, in context.")], "Answer style", "Recall", "What did the report say about length?"),
]
SETS.append(practice_set(module=M_EXAM, topic="Paper 3", title="Application questions: schedules, units and diagrams", lesson="ecl2-paper3-application", questions=build(X3, 223)))

# ------------------------------------------------------------------ Paper 1 mock exam A (50 MC across the six Lower Sixth modules)
# Allocation by topic count: Methodology 4 topics -> 7, Price theory 6 -> 10, Production 5 -> 8, Market structures 6 -> 10,
# Distribution 5 -> 8, Market failure 4 -> 7 (total 50).
P1 = [
    # ---- Economic Methodology & Resource Allocation (7)
    Q("Which of the following is a normative statement?", "The government ought to spend more on rural roads",
      [("A rise in the price of fuel reduces the quantity of fuel demanded", "This can be tested against evidence: it is positive."), ("Cocoa production in a region rose last year", "This is a statement of fact, which can be checked."), ("If incomes rise, demand for cars will rise", "This is a testable cause-and-effect claim: positive.")],
      [("Value judgement", "'Ought' signals an opinion that facts alone cannot prove.")], T_METH, "Recall", "Which statement is an opinion about what should be done?"),
    Q("The deductive method of testing a hypothesis in economics:", "Starts from assumptions and theory, deduces predictions and tests them against data",
      [("Starts from observed data and generalizes to a theory", "That is the inductive method."), ("Distinguishes positive from normative statements", "That is a different distinction."), ("Uses only opinions", "Both methods use evidence.")],
      [("Methods", "Deductive: general to particular; inductive: particular to general.")], T_METH, "Concept", "Which way does the reasoning run?"),
    Q("A production possibility curve passes through (cocoa, cassava) = (20, 36) and (30, 16) in thousand tonnes. The opportunity cost of one extra tonne of cocoa between these points is:", "2 tonnes of cassava",
      [("20 tonnes of cassava", "That is the total cassava lost for 10 extra tonnes of cocoa."), ("0.5 tonne of cassava", "That inverts the ratio."), ("10 tonnes of cassava", "That is the extra cocoa, not the cassava lost.")],
      [("Loss", "36 − 16 = 20 tonnes of cassava given up."), ("Per tonne", "20 ÷ 10 = 2.")], T_PPC, "Calculation", "Divide the cassava lost by the cocoa gained."),
    Q("An economy is producing at a point inside its production possibility curve. This most likely indicates:", "Unemployed or inefficiently used resources",
      [("Economic growth", "Growth is an outward shift of the curve."), ("Full employment of all resources", "Full employment is on the curve."), ("An unattainable output", "Points outside the curve are unattainable.")],
      [("Interpretation", "Inside the curve, more of both goods could be produced.")], T_PPC, "Interpretation", "Where are points on the curve?"),
    Q("Allocative efficiency is achieved when:", "Price equals marginal cost",
      [("Output is produced at minimum average cost", "That is productive efficiency."), ("Nobody can be made better off without making someone worse off", "That is the definition of Pareto efficiency."), ("The firm earns supernormal profit", "Profit does not define efficiency.")],
      [("Definition", "The value consumers place on the last unit equals its cost.")], T_EFF, "Recall", "Which condition compares price with cost?"),
    Q("A change is a Pareto improvement if it:", "Makes at least one person better off without making anyone worse off",
      [("Makes everybody equally well off", "Equality is not required."), ("Raises GDP", "A rise in output may leave some worse off."), ("Makes most people better off at the cost of a few", "Someone is worse off, so it is not a Pareto improvement.")],
      [("Definition", "Named after Vilfredo Pareto.")], T_EFF, "Concept", "Does anyone lose?"),
    Q("In a command economy, the questions of what, how and for whom to produce are decided mainly by:", "A central planning authority",
      [("The price mechanism", "That is a market economy."), ("Custom and tradition", "That is a traditional economy."), ("Consumers' spending", "That is a feature of a market economy.")],
      [("Systems", "State ownership and planning characterize a command economy.")], T_SYS, "Recall", "Who owns resources in a command economy?"),
    # ---- Price Theory & Consumer Behaviour (10)
    Q("Demand is Qd = 120 − 2P and supply is Qs = −30 + 3P. The equilibrium price (FCFA) is:", "30",
      [("40", "At P = 40, Qd = 40 but Qs = 90: excess supply."), ("24", "At P = 24, Qd = 72 but Qs = 42: excess demand."), ("60", "60 is the equilibrium quantity, not the price.")],
      [("Solve", "120 − 2P = −30 + 3P, so 150 = 5P and P = 30. Q = 60 on both sides.")], T_DSF, "Calculation", "Set Qd = Qs."),
    Q("A rise in consumers' incomes for a normal good will:", "Shift the demand curve to the right, raising the equilibrium price and quantity",
      [("Shift the supply curve to the right", "Income affects demand."), ("Move along the demand curve to a lower price", "Income is not the good's own price."), ("Leave equilibrium unchanged", "Demand rises.")],
      [("Shift", "Normal good: more is demanded at every price.")], T_DSF, "Concept", "Which curve is income a determinant of?"),
    Q("The price of a good rises by 10% and the quantity demanded falls by 25%. Price elasticity of demand (ignoring the sign) is:", "2.5, so demand is elastic",
      [("0.4, so demand is inelastic", "That inverts the ratio."), ("15, so demand is very elastic", "That subtracts the percentages."), ("35", "That adds the percentages.")],
      [("Formula", "PED = %ΔQd ÷ %ΔP = 25 ÷ 10 = 2.5, which is greater than 1.")], T_ELA, "Calculation", "Divide the percentage change in quantity by that in price.", ),
    Q("A firm raises the price of a good with inelastic demand. Its total revenue will:", "Rise",
      [("Fall", "That is the result for elastic demand."), ("Stay the same", "That is unit elastic demand."), ("Fall to zero", "Demand does not collapse.")],
      [("Revenue", "Quantity falls proportionally less than price rises.")], T_ELA, "Application", "Is the fall in quantity bigger or smaller than the price rise?"),
    Q("The cross elasticity of demand between tea and coffee is likely to be:", "Positive, because they are substitutes",
      [("Negative", "That would indicate complements."), ("Zero", "They are related goods."), ("Infinite", "Substitutes are close but not perfect.")],
      [("XED", "A rise in the price of tea raises the demand for coffee.")], T_ELA, "Concept", "What happens to coffee demand when tea becomes dearer?"),
    Q("Demand is P = 100 − Q and supply is P = 20 + Q. The consumer surplus at equilibrium is:", "800",
      [("1 600", "That is the area of the whole triangle formed by price intercept and equilibrium output."), ("2 400", "That is the area of the rectangle at 60 × 40."), ("400", "That is half the correct answer.")],
      [("Equilibrium", "Q = 40, P = 60."), ("Triangle", "½ × (100 − 60) × 40 = 800.")], T_SUR, "Calculation", "The triangle between demand and the price line."),
    Q("A fall in the price of a good received by farmers (all else equal) will:", "Reduce producer surplus",
      [("Increase producer surplus", "Lower prices reduce it."), ("Leave producer surplus unchanged", "Producer surplus depends on price above the supply curve."), ("Increase consumer surplus only", "Producers lose surplus too.")],
      [("Definition", "Producer surplus = price received minus the minimum acceptable price.")], T_SUR, "Concept", "What is the area above the supply curve and below the price?"),
    Q("A consumer's marginal utility of good X is 24 at a price of 6 and of good Y is 20 at a price of 4. To maximize utility she should:", "Buy more Y and less X",
      [("Buy more X and less Y", "MU per franc is higher for Y (5) than for X (4)."), ("Change nothing", "The equimarginal condition is not met."), ("Buy only X", "That ignores diminishing marginal utility.")],
      [("Equimarginal principle", "MUx/Px = 4; MUy/Py = 5, so shift spending to Y.")], T_MU, "Application", "Compare utility per franc."),
    Q("A consumer has an income of 12 000 FCFA. Good Y costs 600 FCFA a unit. The intercept of her budget line on the Y axis is:", "20 units",
      [("200 units", "That divides 12 000 by 60."), ("600 units", "That is the price, not the quantity."), ("12 units", "That divides 12 000 by 1 000.")],
      [("Divide", "12 000 ÷ 600 = 20 units.")], T_IC, "Calculation", "Income divided by the price of Y."),
    Q("A Giffen good is one for which:", "The income effect of a price rise outweighs the substitution effect, so quantity demanded rises",
      [("The substitution effect is stronger than the income effect", "That gives a normal downward-sloping demand curve."), ("Demand rises when income rises", "That is a normal good."), ("Price has no effect on quantity", "That is perfectly inelastic demand.")],
      [("Giffen", "It is a very inferior good with a strong negative income effect.")], T_IS, "Concept", "Which effect dominates?"),
    # ---- Theory of Production & Costs (8)
    Q("Total product with 1 to 5 workers is 10, 24, 36, 44, 48. Diminishing returns set in with the:", "3rd worker",
      [("2nd worker", "MPP rises from 10 to 14 at the 2nd worker."), ("4th worker", "MPP already fell at the 3rd."), ("5th worker", "MPP already fell earlier.")],
      [("MPP", "10, 14, 12, 8, 4: MPP first falls at the 3rd worker.")], T_SRP, "Interpretation", "Find the first fall in marginal product."),
    Q("Using the same total products (10, 24, 36, 44, 48), the marginal product of the 4th worker is:", "8",
      [("11", "That is the average product (44 ÷ 4)."), ("44", "That is the total product."), ("12", "That is the marginal product of the 3rd worker.")],
      [("Difference", "44 − 36 = 8.")], T_SRP, "Calculation", "Marginal product is the change in total product."),
    Q("If all inputs are doubled and output rises by 150% (to 2.5 times), the firm experiences:", "Increasing returns to scale",
      [("Constant returns to scale", "Constant would be output doubling."), ("Decreasing returns to scale", "Output rises by more than the inputs."), ("Diminishing marginal returns", "That is a short-run idea with a fixed input.")],
      [("Long run", "Output rises more than proportionately.")], T_RTS, "Concept", "Compare 2.5 with 2."),
    Q("A firm minimizes the cost of a given output where the isoquant is tangent to the isocost line, so that:", "The marginal product per franc is equal for all inputs",
      [("Total cost is zero", "Tangency gives the lowest cost, not zero."), ("The inputs have the same price", "The ratio of prices equals the MRTS."), ("All inputs have the same marginal product", "The ratio MP/price is equalized.")],
      [("Condition", "MPL/w = MPK/r.")], T_RTS, "Concept", "Think of the equimarginal rule for inputs."),
    Q("Which is an external economy of scale?", "A growing industry attracts a skilled labour pool and suppliers nearby, lowering all firms' costs",
      [("A firm buys raw materials in bulk at a discount", "That is an internal economy."), ("A firm spreads its fixed administration costs", "That is an internal economy."), ("A firm divides tasks among its workers", "That is an internal technical economy.")],
      [("External", "Benefits come from the growth of the industry, not the single firm.")], T_EOS, "Application", "Does the benefit arise inside the firm?"),
    Q("A firm's total cost is 700 FCFA at 10 units. Its average cost is:", "70 FCFA",
      [("7 000 FCFA", "That multiplies instead of dividing."), ("690 FCFA", "That subtracts the units."), ("710 FCFA", "That adds the units.")],
      [("Divide", "700 ÷ 10 = 70.")], T_COST, "Calculation", "Total cost divided by output."),
    Q("Total cost is 700 at 10 units and 735 at 11 units. The marginal cost of the 11th unit is:", "35",
      [("735", "That is the total cost."), ("66.8", "That is the average cost at 11 units."), ("70", "That is the average cost at 10 units.")],
      [("Marginal", "735 − 700 = 35.")], T_COST, "Calculation", "The change in total cost."),
    Q("For a firm in perfect competition, which is true of revenue?", "Average revenue equals marginal revenue and equals price",
      [("Marginal revenue is below average revenue", "That is for a downward-sloping demand curve."), ("Total revenue falls as output rises", "Total revenue rises at a constant rate."), ("Marginal revenue is zero", "MR equals the price.")],
      [("Price taker", "Each unit sells at the market price.")], T_REV, "Concept", "What is the shape of the demand curve it faces?"),
    # ---- Market Structures (10)
    Q("A firm maximizes profit by producing where:", "MC = MR, with MC cutting MR from below",
      [("TR is greatest", "That maximizes revenue."), ("MC = AC", "That is the minimum of AC."), ("MR = 0", "That also maximizes revenue.")],
      [("Rule", "The second condition rules out the output where profit is lowest.")], T_PMAX, "Recall", "Which two curves cross?"),
    Q("Demand is P = 60 − Q and MC = 2Q. The profit-maximizing output is:", "15 units",
      [("20 units", "That sets MC = P (2Q = 60 − Q), as if the firm were a price taker."), ("30 units", "That sets MR = 0, which maximizes revenue."), ("12 units", "That does not satisfy MC = MR.")],
      [("MR", "MR = 60 − 2Q."), ("Solve", "2Q = 60 − 2Q, so Q = 15.")], T_PMAX, "Calculation", "Find MR first, then set MC = MR."),
    Q("A perfectly competitive firm should shut down in the short run when:", "Price falls below the minimum of average variable cost",
      [("Price falls below the minimum of average cost", "It can still cover variable costs above AVC."), ("It makes a loss", "A loss is acceptable if P ≥ AVC."), ("Price equals marginal cost", "That is its profit-maximizing rule.")],
      [("Shut-down", "Below AVC it loses more than the fixed cost.")], T_PC, "Concept", "Which cost must revenue cover in the short run?"),
    Q("In long-run equilibrium, a perfectly competitive firm:", "Earns normal profit and produces at the minimum of AC",
      [("Earns supernormal profit", "Entry removes it."), ("Produces to the left of minimum AC", "That is monopolistic competition."), ("Has downward-sloping demand", "Its demand is horizontal.")],
      [("Equilibrium", "P = MC = minimum AC.")], T_PC, "Concept", "What does free entry do?"),
    Q("A monopolist faces P = 120 − 2Q with constant MC = AC = 20 (MR = 120 − 4Q). Its supernormal profit is:", "1 250",
      [("2 500", "That is the consumer surplus under competition, not the profit."), ("1 750", "That is 70 × 25, the total revenue."), ("625", "That is the deadweight loss, not the profit.")],
      [("Output", "120 − 4Q = 20, so Q = 25 and P = 70."), ("Profit", "(70 − 20) × 25 = 1 250.")], T_MON, "Calculation", "Find Q and P, then (P − AC) × Q."),
    Q("Which is a condition for successful price discrimination?", "Buyers in the cheaper market cannot resell to buyers in the dearer market",
      [("The product is sold by many identical firms", "The firm needs market power."), ("The markets have identical elasticities", "Different elasticities are needed."), ("Costs differ greatly between the markets", "Discrimination means price differences not based on cost.")],
      [("Conditions", "Market power, separable markets with different PED, no arbitrage.")], T_MON, "Concept", "What stops buyers undermining the scheme?"),
    Q("In the long run, a monopolistically competitive firm earns:", "Normal profit, with AR tangent to AC and excess capacity",
      [("Supernormal profit, because of brand loyalty", "Entry removes it."), ("Losses", "Firms would leave."), ("Normal profit, with output at minimum AC", "Because AR slopes down, the tangency is to the left of minimum AC.")],
      [("Tangency", "Entry shifts demand left until AR = AC.")], T_MC, "Concept", "What does free entry do to profit?"),
    Q("The kinked demand curve model of oligopoly predicts price rigidity because:", "MR has a vertical gap at the current price, so MC can change without changing price",
      [("Firms have no costs", "The model uses costs."), ("Demand is perfectly inelastic", "Demand is kinked."), ("Competition authorities fix prices", "No price control is involved.")],
      [("Gap in MR", "Any MC through the gap gives the same price and output.")], T_OLI, "Concept", "What does the kink do to MR?"),
    Q("Payoffs (A, B) in a pricing game: both high (50, 50); A high, B low (20, 70); A low, B high (70, 20); both low (30, 30). The Nash equilibrium is:", "Both low, with 30 each",
      [("Both high, with 50 each", "Each firm gains by deviating to low."), ("A high, B low", "A would switch to low."), ("A low, B high", "B would switch to low.")],
      [("Dominant strategy", "Low is best whatever the other does.")], T_OLI, "Application", "Find each firm's best reply."),
    Q("A market is contestable when:", "Entry and exit are easy and sunk costs are low, so incumbents fear hit-and-run entry",
      [("There is a very large number of firms", "A contestable market may have only one firm."), ("The government owns the firms", "Ownership is not the key."), ("Firms sell identical products", "Product type does not define contestability.")],
      [("Definition", "The threat of entry disciplines incumbents.")], T_CON, "Concept", "What is the key condition for entrants?"),
    # ---- Theory of Distribution & Factor Pricing (8)
    Q("A worker's marginal physical product is 12 units and the price is 450 FCFA a unit in a competitive market. The MRP is:", "5 400 FCFA",
      [("462 FCFA", "That adds the two numbers."), ("37.5 FCFA", "That divides 450 by 12."), ("12 FCFA", "That is the physical product, not the revenue product.")],
      [("Formula", "12 × 450 = 5 400.")], T_MRP, "Calculation", "MRP = MPP × P."),
    Q("The firm's demand curve for labour is its:", "MRP curve (below the maximum of ARP)",
      [("MPP curve", "That is in physical units."), ("AC curve", "That is for output."), ("Supply curve of labour", "That is the workers' side.")],
      [("Hiring rule", "The firm hires where MRP = wage.")], T_MRP, "Recall", "Which curve is in money terms?"),
    Q("A monopsonist employer, compared with a competitive employer:", "Hires fewer workers and pays a lower wage",
      [("Hires more workers at a higher wage", "That is the opposite."), ("Hires the same number at the same wage", "That is competition."), ("Pays each worker his or her MRP", "Under monopsony the wage is below MRP.")],
      [("Rule", "MCL = MRP, then the wage is read from supply.")], T_WAGE, "Concept", "Where is MCL relative to the supply curve?"),
    Q("A trade union that raises the wage above the competitive equilibrium is likely to:", "Raise pay for those employed but reduce employment",
      [("Raise both pay and employment", "That can happen in monopsony."), ("Lower pay and employment", "The wage rises."), ("Have no effect", "Quantity demanded of labour falls.")],
      [("Trade-off", "The size depends on the elasticity of labour demand.")], T_WAGE, "Reasoning", "What happens to quantity demanded when the wage rises?"),
    Q("An economist says that a footballer's high pay is mostly economic rent. This means:", "Much of his earnings is above what he could earn in his next best job",
      [("He pays a high rent for his house", "That is commercial rent."), ("His wage is below his MRP", "That is monopsony."), ("His pay is a transfer from the government", "Transfer earnings are the minimum payment.")],
      [("Rent", "Economic rent = earnings − transfer earnings.")], T_RENT, "Concept", "What is the next best alternative?"),
    Q("According to Keynes, money held for the speculative motive is:", "Idle balances, which fall as the interest rate rises",
      [("Active balances, which depend on income", "Those are transactions and precautionary balances."), ("Always spent immediately", "Idle balances are held."), ("Independent of the interest rate", "They depend inversely on it.")],
      [("Motives", "Speculative demand is linked to bond prices.")], T_INT, "Concept", "Which motive depends on the rate of interest?"),
    Q("A firm has revenue 12 million FCFA, explicit costs 9 million and implicit costs 2.3 million. Its economic profit is:", "0.7 million FCFA",
      [("3 million FCFA", "That is accounting profit and ignores implicit costs."), ("1.7 million FCFA", "That subtracts only part of the implicit costs."), ("5.3 million FCFA", "That adds the implicit costs instead of subtracting.")],
      [("Subtract", "12 − 9 − 2.3 = 0.7.")], T_PROF, "Calculation", "Subtract explicit and implicit costs."),
    Q("Which theory says that profit is the reward for introducing new products and methods?", "Schumpeter's innovation theory",
      [("Knight's uncertainty theory", "That links profit with uncertainty-bearing."), ("The monopoly theory", "That links profit with market power."), ("The loanable funds theory", "That explains interest.")],
      [("Attribution", "The innovator earns profit until imitators arrive.")], T_PROF, "Recall", "Which entrepreneur creates something new?"),
    # ---- Market Failure & Government Micro-Intervention (7)
    Q("Which pair of features defines a pure public good?", "Non-rival and non-excludable",
      [("Rival and excludable", "That is a private good."), ("Rival and non-excludable", "That is a common resource."), ("Non-rival and excludable", "That is a club or quasi-public good.")],
      [("Definition", "Both features together.")], T_PUB, "Recall", "Check both tests."),
    Q("Public schools are best classified as:", "Merit goods",
      [("Pure public goods", "They are rival and excludable."), ("Demerit goods", "They are beneficial."), ("Common resources", "They are not open-access.")],
      [("Merit", "Education is under-consumed in a free market.")], T_PUB, "Application", "Is a school place rival?"),
    Q("A factory's smoke harms the health of nearby residents. At the free-market output:", "Marginal social cost exceeds marginal private cost, and output is too high",
      [("MSC is below MPC", "External cost adds to MPC."), ("Output is too low", "A negative externality causes over-production."), ("There is no market failure", "External costs are ignored in prices.")],
      [("Externality", "MSC = MPC + MEC; the market produces where MPB = MPC.")], T_EXT, "Concept", "Who bears the smoke costs?"),
    Q("Demand is P = 100 − Q, MPC = 20 + Q and the external cost is 20 per unit. The welfare loss at the market output is:", "100",
      [("200", "That uses the full rectangle 20 × 10."), ("400", "That is 20 × 20, the wrong base."), ("10", "That is the over-production, not the loss in value.")],
      [("Outputs", "Market Q = 40; social optimum Q = 30 (100 − Q = 40 + Q)."), ("Triangle", "½ × 20 × 10 = 100.")], T_EXT, "Calculation", "Triangle between the two outputs."),
    Q("Demand is P = 100 − Q and supply is P = 20 + Q. A tax of 20 FCFA a unit is imposed. The new equilibrium quantity is:", "30",
      [("40", "That is the quantity before the tax."), ("20", "That subtracts the whole tax from the old quantity."), ("35", "That would be the answer for a tax of 10 with different curves.")],
      [("New supply", "P = 40 + Q."), ("Solve", "100 − Q = 40 + Q, so Q = 30.")], T_TAX, "Calculation", "Add the tax to supply."),
    Q("A government prefers tradable pollution permits to a tax because permits:", "Fix the total quantity of pollution at the cap",
      [("Fix the price of pollution", "The price is set by the market."), ("Need no monitoring", "Monitoring is needed."), ("Always raise revenue", "Free permits raise none.")],
      [("Cap and trade", "The cap sets quantity; trading finds the lowest-cost reductions.")], T_TAX, "Concept", "What is fixed in the scheme?"),
    Q("A regulator sets a price cap of RPI − X on a water company. This gives the firm an incentive to:", "Cut costs, because it keeps savings beyond X",
      [("Raise prices freely", "Prices are capped."), ("Ignore costs", "Savings raise its profit."), ("Reduce quality in all cases", "Quality may suffer but it is not the main incentive; standards are also set.")],
      [("Incentive", "Prices are set independently of actual costs.")], T_REG, "Concept", "What happens to profit when costs fall faster than the cap?"),
]
SETS.append(practice_set(module=M_EXAM, topic="Paper 1", title="Paper 1 mock exam A", lesson="ecl2-paper1-multiple-choice", questions=build(P1, 231), mock=True, time_limit_minutes=90))

# ------------------------------------------------------------------ Paper 2 practice paper A (microeconomics side only; essays cannot be auto-marked)
P2 = [
    # Question 1: PPC and methodology
    Q("Lower Sixth practice: this paper uses the microeconomics side only. Question 1 (a). Using a production possibility curve for cocoa and cassava, which statement correctly explains opportunity cost?", "It is the amount of cassava given up to produce more cocoa, the next best alternative forgone",
      [("It is the money price of cocoa", "Opportunity cost is measured in forgone alternatives, not necessarily money."), ("It is the total of all goods an economy does not produce", "It is only the next best alternative."), ("It is zero when resources are unemployed", "Opportunity cost exists on the curve; unemployment is a point inside it.")],
      [("Definition", "Opportunity cost is the value of the next best alternative given up.")], T_PPC, "Concept", "What is given up when resources move?"),
    N("Question 1 (b). The curve passes through (cocoa, cassava) = (20, 36) and (30, 16) in thousand tonnes. Calculate the opportunity cost of one extra tonne of cocoa between these points, in tonnes of cassava.", 2,
      [("Cassava lost", "36 − 16 = 20."), ("Per tonne", "20 ÷ (30 − 20) = 2.")], T_PPC, "Calculation", "Divide the cassava lost by the cocoa gained.", tol=0.01, unit="tonnes"),
    Q("Question 1 (c). Distinguish between the inductive and deductive methods of testing hypotheses. Which answer uses a conjunction correctly?", "The deductive method starts from assumptions and theory to predict outcomes, whereas the inductive method starts from observed data to build general conclusions",
      [("The deductive method uses data and the inductive method uses opinions", "Both use evidence; the difference is the direction of reasoning."), ("Both methods start from assumptions", "The inductive method starts from observation."), ("The deductive method is about normative statements", "The Board's report notes candidates confusing the methods with positive and normative statements.")],
      [("Distinction", "Deductive: general to particular; inductive: particular to general.")], T_METH, "Application", "Which direction does each method run?"),
    # Question 2: demand, supply and elasticity
    Q("Question 2 (a). Why does the demand curve for a normal good slope downward? Which answer is complete?", "A fall in price makes the good cheaper relative to others (substitution effect) and raises real income (income effect), so more is demanded",
      [("A fall in price shifts the demand curve to the right", "That confuses a movement along the curve with a shift."), ("A fall in price raises money income", "The Board's report notes candidates explaining the income effect in terms of money income instead of real income."), ("Consumers have more income at lower prices, so supply rises", "This is about supply.")],
      [("Effects", "Substitution effect plus income effect (real income).")], T_IS, "Reasoning", "Which two effects does a price fall have?"),
    N("Question 2 (b). The price of cassava rises by 10% and the quantity supplied rises by 20%. Calculate the price elasticity of supply.", 2,
      [("Formula", "PES = %ΔQs ÷ %ΔP = 20 ÷ 10 = 2.")], T_ELA, "Calculation", "Divide the percentage change in quantity supplied by that in price.", tol=0.01),
    Q("Question 2 (c). Which is a directional factor that would INCREASE the supply of cassava?", "A fall in the price of fertilizer, which lowers the cost of production",
      [("A rise in consumers' incomes", "That changes demand."), ("A rise in the price of cassava", "That is a movement along the supply curve."), ("The determinants of supply", "That names the topic without direction.")],
      [("Directional", "A change in a determinant of supply, in the direction that increases supply.")], T_DSF, "Application", "Which option changes a cost and says which way?"),
    # Question 3: profit maximization
    N("Question 3 (a). A firm faces P = 100 − 2Q and has MC = 10 + 2Q (MR = 100 − 4Q). Find the profit-maximizing output.", 15,
      [("MC = MR", "10 + 2Q = 100 − 4Q, so Q = 15.")], T_PMAX, "Calculation", "Set MC equal to MR.", tol=0),
    N("Question 3 (b). Total cost is TC = 50 + 10Q + Q². Using Q = 15 and P = 70, find the profit.", 625,
      [("TR", "70 × 15 = 1 050."), ("TC", "50 + 150 + 225 = 425."), ("Profit", "1 050 − 425 = 625.")], T_PMAX, "Calculation", "Profit = TR − TC.", tol=0),
    Q("Question 3 (c). A firm's managers, paid according to sales, maximize sales revenue instead of profit. Which output rule do they follow?", "They produce where MR = 0",
      [("MC = MR", "That maximizes profit."), ("AR = AC", "That maximizes sales volume subject to normal profit."), ("MC = AC", "That is the minimum of AC.")],
      [("Rule", "Sales revenue is greatest where MR = 0.")], T_PMAX, "Concept", "Where is total revenue at its peak?"),
    # Question 4: wages and discrimination
    Q("Question 4 (a). Which is an intra-industry wage differential in the cement industry?", "A kiln engineer is paid more than a loader in the same company",
      [("Cement workers are paid more than farm workers", "That is inter-industry."), ("Workers in the capital are paid more than rural workers", "That is regional."), ("Teachers are paid less than bankers", "That is inter-industry.")],
      [("Distinction", "The Board's report notes candidates mixing the two. Intra means within the same industry.")], T_WAGE, "Application", "Is the comparison within one industry?"),
    Q("Question 4 (b). Which is a reason why some employers discriminate against women?", "They expect career breaks for childbirth and judge individuals by the average of the group (statistical discrimination)",
      [("Women have lower productivity in every job", "That is false and not a justification."), ("Men are paid less than women", "That reverses the wage gap."), ("Wage differentials are caused only by inter-industry factors", "That does not explain discrimination.")],
      [("Discrimination", "Statistical discrimination treats a person by beliefs about the group.")], T_WAGE, "Reasoning", "The question asks why employers discriminate, not why men earn more."),
    N("Question 4 (c). A plantation is the only employer. Labour supply is W = 1 000 + 100L and MRP = 7 000 − 100L (MCL = 1 000 + 200L). Find the monopsony wage in FCFA.", 3000,
      [("Employment", "MCL = MRP: 1 000 + 200L = 7 000 − 100L, so L = 20."), ("Wage", "From supply: 1 000 + 100 × 20 = 3 000 FCFA.")], T_WAGE, "Calculation", "Find L first, then read the wage from the supply curve.", tol=0, unit="FCFA"),
    # Question 5: perfect and monopolistic competition
    Q("Question 5 (a). Which diagram shows a perfect competitor in long-run equilibrium?", "A horizontal AR = MR line touching AC at its minimum",
      [("A downward-sloping AR tangent to AC to the left of its minimum", "That is monopolistic competition."), ("An AR line above AC giving a profit rectangle", "That is not long-run equilibrium; entry removes profit."), ("An AR line below AC giving a loss", "Loss-making firms leave; the Board's report notes this common error.")],
      [("Diagram", "P = MC = minimum AC.")], T_PC, "Interpretation", "What does free entry do to profit?"),
    Q("Question 5 (b). Which statement best distinguishes a monopolistic competitor from a perfect competitor in the long run?", "A monopolistic competitor produces with excess capacity, whereas a perfect competitor produces at minimum average cost",
      [("A monopolistic competitor earns supernormal profit, whereas a perfect competitor earns normal profit", "Both earn normal profit in the long run."), ("A monopolistic competitor is a price taker", "It faces a downward-sloping demand curve."), ("A perfect competitor differentiates its product", "Its product is homogeneous.")],
      [("Distinction", "Use whereas: tangency to the left of minimum AC against the minimum.")], T_MC, "Application", "Which one has excess capacity?"),
    Q("Question 5 (c). Customers prefer a particular brand of bread even when another brand is slightly cheaper. The economic term for this is:", "Brand loyalty",
      [("Price discrimination", "That is charging different prices for the same good."), ("Economies of scale", "That is a cost advantage of size."), ("Limit pricing", "That is a pricing strategy to deter entry.")],
      [("Term", "The Board's report notes few candidates identified this term.")], T_MC, "Recall", "Which term describes loyalty to a name?"),
    # Question 6: monopoly and oligopoly
    N("Question 6 (a). A monopolist faces P = 120 − 2Q with MC = AC = 20. Under perfect competition output would be 50. Calculate the deadweight loss caused by the monopoly (output 25, price 70).", 625,
      [("Triangle", "½ × (70 − 20) × (50 − 25) = 625.")], T_MON, "Calculation", "The triangle between demand and MC.", tol=0),
    Q("Question 6 (b). A firm sells in two markets with the same MC. Which statement about third-degree price discrimination is correct?", "The higher price is charged in the market with the less elastic demand",
      [("The higher price is charged where demand is more elastic", "Elastic buyers react strongly to price."), ("The same price is charged in both markets", "That is not discrimination."), ("MR is highest in the market with the highest price", "Profit is maximized where MR in each market equals MC.")],
      [("Rule", "MRA = MRB = MC; the less elastic market pays more.")], T_MON, "Concept", "Which buyers react least to price?"),
    N("Question 6 (c). In an oligopolistic market the shares of the largest firms are 35%, 25%, 15% and 10%. Calculate the three-firm concentration ratio (%).", 75,
      [("Add", "35 + 25 + 15 = 75%.")], T_OLI, "Calculation", "Add the three largest shares.", tol=0, unit="%"),
    # Question 7: externalities and taxes
    Q("Question 7 (a). Marginal social cost is equal to:", "Marginal private cost plus marginal external cost",
      [("Marginal private cost minus marginal external cost", "External costs add to private cost."), ("Marginal social benefit", "Costs and benefits are different curves."), ("Marginal private benefit", "That is on the demand side.")],
      [("Identity", "MSC = MPC + MEC.")], T_EXT, "Recall", "Social costs include private and external."),
    N("Question 7 (b). Demand is P = 100 − Q and MPC = 20 + Q. The external cost is 20 per unit. Calculate the welfare loss at the free-market output.", 100,
      [("Outputs", "Market 40; social optimum 30."), ("Triangle", "½ × 20 × 10 = 100.")], T_EXT, "Calculation", "The triangle between the two outputs.", tol=0),
    N("Question 7 (c). A tax of 20 FCFA is imposed on this good (supply becomes P = 40 + Q). Calculate the tax revenue in thousands of FCFA (Q in thousands).", 600,
      [("Quantity", "100 − Q = 40 + Q, so Q = 30."), ("Revenue", "20 × 30 = 600.")], T_TAX, "Calculation", "Tax per unit times the new quantity.", tol=0, unit="thousand FCFA"),
    Q("Question 7 (d). Which is a limitation of a Pigovian tax?", "It is difficult to measure the marginal external cost, so the tax may be set too high or too low",
      [("It always raises the price by more than the tax", "The rise depends on elasticity."), ("It cannot reduce output", "It shifts supply and reduces output."), ("It has no cost to anyone", "Buyers and sellers bear it.")],
      [("Evaluation", "Measuring external cost is hard.")], T_TAX, "Reasoning", "What must the tax equal?"),
    # Question 8: rent, interest, profit
    N("Question 8 (a). A mechanic earns 150 000 FCFA a month. His next best alternative is 110 000 FCFA. Calculate his economic rent.", 40000,
      [("Subtract", "150 000 − 110 000 = 40 000 FCFA.")], T_RENT, "Calculation", "Earnings minus transfer earnings.", tol=0, unit="FCFA"),
    Q("Question 8 (b). Which statement distinguishes active from idle balances?", "Active balances are held for transactions and precautionary motives and depend on income, whereas idle balances are held for the speculative motive and depend on the interest rate",
      [("Active balances are held in banks, whereas idle balances are held at home", "The distinction is by motive, not place."), ("Idle balances depend on income, whereas active balances depend on the interest rate", "The dependence is reversed."), ("Both are held only for speculation", "Active balances are not speculative.")],
      [("Distinction", "The Board's report notes that candidates did not link the three motives to the two kinds of balances.")], T_INT, "Concept", "Which motive responds to interest?"),
    N("Question 8 (c). A shop has revenue 12 million FCFA, explicit costs 9 million FCFA and implicit costs 2.3 million FCFA. Calculate its economic profit in millions of FCFA.", 0.7,
      [("Subtract", "12 − 9 − 2.3 = 0.7.")], T_PROF, "Calculation", "Subtract both kinds of cost.", tol=0.01, unit="million FCFA"),
]
SETS.append(practice_set(module=M_EXAM, topic="Paper 2", title="Paper 2 practice paper A", lesson="ecl2-paper2-essays", questions=build(P2, 232), mock=True, time_limit_minutes=150))

# ------------------------------------------------------------------ Paper 3 practice paper A (20 auto-markable parts)
# Data are invented for practice. Plantain market: price in '000 FCFA per tonne; quantities in tonnes.
P3 = [
    # Question 1: plantain market (price in thousand FCFA per tonne)
    # Price 20,30,40,50,60 ; quantity demanded 100,85,70,55,40 ; quantity supplied 30,50,70,90,110 (tonnes)
    N("Lower Sixth practice: this paper uses the microeconomics side only; the data are invented for practice. Question 1 (a). A table gives, for plantains, price (thousand FCFA per tonne) 20, 30, 40, 50, 60; quantity demanded (tonnes) 100, 85, 70, 55, 40; quantity supplied (tonnes) 30, 50, 70, 90, 110. Determine the market price in FCFA per tonne.", 40000,
      [("Clearing price", "Quantity demanded equals quantity supplied (70 tonnes) at 40 thousand FCFA, that is 40 000 FCFA per tonne.")], T_DSF, "Interpretation", "Find where the two quantity columns are equal, then read the units.", tol=0, unit="FCFA per tonne"),
    N("Question 1 (b). After farmers adopt better planting suckers, quantity supplied at each price rises by 35 tonnes. Determine the new market price in FCFA per tonne.", 30000,
      [("New supply", "65, 85, 105, 125, 145."), ("Clearing price", "At 30 thousand FCFA, quantity demanded (85) equals the new quantity supplied (85): 30 000 FCFA per tonne.")], T_DSF, "Interpretation", "Add 35 to every supply figure.", tol=0, unit="FCFA per tonne"),
    N("Question 1 (c). A farmers' union wants to hold the price at 40 000 FCFA per tonne after the shift in supply. How many tonnes must it buy?", 35,
      [("Quantities", "New quantity supplied at 40 thousand FCFA = 105; quantity demanded = 70."), ("Surplus", "105 − 70 = 35 tonnes.")], T_DSF, "Application", "Buy the surplus at the supported price.", tol=0, unit="tonnes"),
    N("Question 1 (d). When the price rises from 30 000 to 40 000 FCFA per tonne, quantity demanded falls from 85 to 70 tonnes. By how much does total revenue (in thousand FCFA) change?", 250,
      [("Revenues", "30 × 85 = 2 550; 40 × 70 = 2 800 thousand FCFA."), ("Change", "2 800 − 2 550 = +250: demand is inelastic over this range.")], T_ELA, "Calculation", "Compare price times quantity before and after.", tol=0, unit="thousand FCFA"),
    # Question 2: a firm's revenue and cost schedule (FCFA)
    N("Question 2 (a). A firm's total revenue at outputs 1 to 5 is 800, 1 500, 2 100, 2 600, 3 000 FCFA. Calculate the marginal revenue of the 3rd unit in FCFA.", 600,
      [("MR", "2 100 − 1 500 = 600.")], T_REV, "Calculation", "MR is the change in total revenue.", tol=0, unit="FCFA"),
    N("Question 2 (b). Total cost at outputs 1 to 5 is 900, 1 300, 1 600, 2 000, 2 600 FCFA. Calculate the marginal cost of the 4th unit in FCFA.", 400,
      [("MC", "2 000 − 1 600 = 400.")], T_COST, "Calculation", "MC is the change in total cost.", tol=0, unit="FCFA"),
    N("Question 2 (c). Using these schedules, at what output is profit maximized?", 4,
      [("Profit", "TR − TC = −100, 200, 500, 600, 400."), ("Maximum", "600 at 4 units. Check: MR of unit 4 is 500 and MC is 400; unit 5 has MR 400 < MC 600.")], T_PMAX, "Calculation", "Compute profit at each output.", tol=0, unit="units"),
    N("Question 2 (d). What is the maximum profit in FCFA?", 600,
      [("Profit", "2 600 − 2 000 = 600.")], T_PMAX, "Calculation", "Profit at the best output.", tol=0, unit="FCFA"),
    # Question 3: perfect competitor in the short run
    Q("Question 3 (a). A firm sells at a constant price of 500 FCFA however much it sells, and produces 120 units. The economic term for this kind of firm is:", "A price taker, in perfect competition",
      [("A price maker in monopoly", "A monopolist faces a downward-sloping demand curve."), ("A kinked-demand oligopolist", "Its demand curve is horizontal, not kinked."), ("A discriminating monopolist", "It charges one price.")],
      [("Structure", "Horizontal demand: AR = MR = P.")], T_PC, "Concept", "What does a constant price whatever the output show?"),
    N("Question 3 (b). At 120 units the firm's average cost is 560 FCFA and its average variable cost is 470 FCFA. Calculate its profit in FCFA (negative for a loss).", -7200,
      [("Per unit", "500 − 560 = −60."), ("Total", "−60 × 120 = −7 200 FCFA.")], T_PC, "Calculation", "Profit = (P − AC) × Q.", tol=0, unit="FCFA"),
    Q("Question 3 (c). Should the firm continue to produce in the short run? Which justification is correct?", "Yes, because price (500) is above AVC (470) so revenue covers variable cost and contributes 30 FCFA a unit to fixed cost",
      [("No, because it makes a loss", "A short-run loss is acceptable if P ≥ AVC."), ("Yes, because price is above AC", "Price (500) is below AC (560)."), ("No, because fixed costs must be zero first", "Fixed costs exist in the short run.")],
      [("Rule", "Continue while P ≥ AVC.")], T_PC, "Reasoning", "Which cost must revenue cover in the short run?"),
    Q("Question 3 (d). If losses continue in the long run, what happens in this industry?", "Some firms leave, supply falls, and the price rises until firms earn normal profit",
      [("More firms enter and price falls further", "Entry follows supernormal profit."), ("Nothing changes", "Long-run losses cause exit."), ("Price falls to the shut-down price", "Exit pushes the price up.")],
      [("Long run", "Exit raises price to minimum AC.")], T_PC, "Reasoning", "What do firms do when they cannot cover all costs for long?"),
    # Question 4: a labour market (W in FCFA a day, L = workers)
    N("Question 4 (a). In a competitive labour market, labour supply is W = 1 000 + 100L and MRP = 7 000 − 100L. Find the equilibrium employment.", 30,
      [("Solve", "1 000 + 100L = 7 000 − 100L, so 200L = 6 000 and L = 30 (wage 4 000).")], T_WAGE, "Calculation", "Set supply equal to MRP.", tol=0, unit="workers"),
    N("Question 4 (b). The only employer in the area is a monopsonist with MCL = 1 000 + 200L. Find its employment.", 20,
      [("Rule", "MCL = MRP: 1 000 + 200L = 7 000 − 100L, so L = 20.")], T_WAGE, "Calculation", "Set MCL equal to MRP.", tol=0, unit="workers"),
    N("Question 4 (c). What wage (FCFA a day) does the monopsonist pay?", 3000,
      [("Supply curve", "W = 1 000 + 100 × 20 = 3 000.")], T_WAGE, "Calculation", "Read the wage from supply at L = 20.", tol=0, unit="FCFA"),
    N("Question 4 (d). A union negotiates a fixed wage of 4 500 FCFA a day. How many workers are employed?", 25,
      [("Demand", "MRP = 4 500 gives 7 000 − 100L = 4 500, so L = 25."), ("Supply at 4 500", "35 workers, so employment is the smaller number, 25.")], T_WAGE, "Calculation", "Employment is the lesser of demand and supply at the wage.", tol=0, unit="workers"),
    # Question 5: a polluting industry (Q in thousand tonnes)
    N("Question 5 (a). Demand (MPB) is P = 100 − Q and private marginal cost (supply) is P = 20 + Q. A factory also imposes an external cost of 20 FCFA on each unit. Find the free-market output (thousand tonnes).", 40,
      [("Market", "100 − Q = 20 + Q, so Q = 40.")], T_EXT, "Calculation", "The market ignores the external cost.", tol=0, unit="thousand tonnes"),
    N("Question 5 (b). Find the socially optimal output (MSC = 40 + Q), in thousand tonnes.", 30,
      [("Optimum", "100 − Q = 40 + Q, so Q = 30.")], T_EXT, "Calculation", "Use MSC.", tol=0, unit="thousand tonnes"),
    N("Question 5 (c). What per-unit tax would move the market to the social optimum, in FCFA?", 20,
      [("Pigovian tax", "The tax should equal the marginal external cost: 20 FCFA.")], T_TAX, "Application", "The tax equals the external cost.", tol=0, unit="FCFA"),
    N("Question 5 (d). With that tax, what is the tax revenue in thousands of FCFA?", 600,
      [("Revenue", "20 × 30 = 600 thousand FCFA.")], T_TAX, "Calculation", "Tax per unit times the new quantity.", tol=0, unit="thousand FCFA"),
]
SETS.append(practice_set(module=M_EXAM, topic="Paper 3", title="Paper 3 practice paper A", lesson="ecl2-paper3-application", questions=build(P3, 233), mock=True, time_limit_minutes=150))

# END-OF-SETS
