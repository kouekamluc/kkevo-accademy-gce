"""A Level Economics (0725), Lower Sixth, modules 1-3: Economic Methodology & Resource Allocation, Price Theory &
Consumer Behaviour, Theory of Production & Costs. 15 lessons, one practice set each (see the practice file of the same
name).

Scope notes: the outline comes from KKEVO's master curriculum blueprint, not a Board syllabus booklet. Facts are the
standard A Level ones. Where textbooks differ the lesson says "check your textbook". Every number in a worked example is
teaching data, labelled "invented for practice", and was checked by script. Exam facts follow the GCE Board's 2023
Advanced Level subject report.
"""

from .dsl import *  # noqa: F403

COURSE = ("economics", "lower-sixth")

M1 = "Economic Methodology & Resource Allocation"
M2 = "Price Theory & Consumer Behaviour"
M3 = "Theory of Production & Costs"

LESSONS = []

# ------------------------------------------------------------------ 1. Economic methodology
LESSONS.append(lesson(
    module=M1,
    topic="Economic methodology",
    title="Economic methodology: how economists build and test theories",
    slug="ecl1-economic-methodology",
    minutes=22,
    summary="Economics as a social science: positive and normative statements, hypotheses, models and ceteris paribus, and the difference between the inductive and deductive methods of testing a theory.",
    objectives=[
        "Distinguish positive from normative statements and explain why the difference matters",
        "Explain how economists form and test hypotheses using models and the ceteris paribus assumption",
        "Distinguish, using a conjunction, between the inductive and deductive methods",
        "Evaluate the claim that economics is a science",
    ],
    key_concepts=["Positive statement", "Normative statement", "Hypothesis", "Economic model", "Ceteris paribus",
                  "Inductive method", "Deductive method", "Microeconomics and macroeconomics"],
    blocks=[
        H("Introduction"),
        T("At O Level you met positive and normative statements. At A Level you must also explain **how** economists reach their "
          "conclusions. When the price of fuel rises in Douala, an economist wants to predict what happens to taxi fares, to the "
          "number of motorbike taxis and to the cost of food brought from Bafoussam. To do this she builds a simplified picture of "
          "reality (a model), makes a prediction and checks it against the facts. That way of working is economic methodology."),
        D("**Economics** is the social science that studies how individuals, firms and governments make choices about the use of "
          "scarce resources to satisfy unlimited wants. **Methodology** is the set of methods used to build and test economic theories.",
          title="Definitions: economics and methodology"),
        D("**Microeconomics** studies individual units: one consumer, one firm, one market (for example the market for cocoa). "
          "**Macroeconomics** studies the economy as a whole: total output, the general price level, unemployment and the balance of payments. "
          "Lower Sixth is mainly microeconomics.", title="Definitions: micro and macro"),
        H("Positive and normative statements"),
        D("A **positive statement** is a statement about what is, was or will be. It can, in principle, be tested against evidence and "
          "shown to be true or false. A **normative statement** is a value judgement about what ought to be. It cannot be settled by facts alone.",
          title="Definitions: positive and normative"),
        T("A positive statement can be false and still be positive: 'Raising the minimum wage in Cameroon will reduce unemployment' is "
          "positive because evidence could test it, even if the evidence later shows it is wrong. Words such as **should**, **ought**, "
          "**fair**, **too high** or **better** usually signal a normative statement, but read the meaning, not just the words."),
        TIP("Economists disagree for two reasons: different positive analysis (they read the evidence differently) or different values "
            "(they weigh goals such as equity and efficiency differently). Saying which kind of disagreement it is earns analysis marks."),
        H("Hypotheses, models and ceteris paribus"),
        KEY("The scientific method in economics", "Economists follow the same broad steps as natural scientists.", cards=[
            ["1. Observe", "Notice a pattern, for example: when cocoa prices rise, farmers plant more cocoa."],
            ["2. Hypothesis", "State a testable relationship: 'quantity supplied rises when price rises, other things equal'."],
            ["3. Model", "Build a simplified version of reality with stated assumptions, often as a diagram or equation."],
            ["4. Predict", "Derive what should happen if the hypothesis is true."],
            ["5. Test", "Compare the prediction with data. Keep, revise or reject the theory."],
        ]),
        D("**Ceteris paribus** (Latin: 'other things being equal') means that all influences except the one being studied are held constant. "
          "It lets the economist isolate one cause, as a laboratory scientist does with a controlled experiment.",
          title="Definition: ceteris paribus"),
        D("A **model** is a simplified representation of reality built on assumptions. A **hypothesis** is a statement of a relationship "
          "between variables that can be tested. A **theory** is a hypothesis that has survived repeated testing.",
          title="Definitions: model, hypothesis, theory"),
        H("Inductive and deductive methods"),
        KEY("Two routes to a theory", "Learn to state the difference in one sentence with a conjunction such as 'whereas'.", cards=[
            ["Inductive method", "Starts from particular observations and data and generalises to a theory (from the particular to the general). Example: studying many markets and concluding that price and quantity demanded are inversely related."],
            ["Deductive method", "Starts from assumptions or general principles and uses logic to derive predictions, which are then tested (from the general to the particular). Example: assuming consumers maximise utility and deducing that they buy more of a good when its price falls."],
        ], note="The inductive method moves from facts to a general law, whereas the deductive method moves from general assumptions to particular predictions."),
        EX("Worked example 1: sorting statements", intro="Classify each statement: (a) 'The price of a bag of cement in Yaounde rose last year.' (b) 'Government should subsidise fertiliser for small farmers.' (c) 'A subsidy on fertiliser will increase maize output.'", steps=[
            S("Statement (a)", text="Positive: it is about what was, and can be checked with price data."),
            S("Statement (b)", text="Normative: 'should' expresses a judgement about what ought to be done."),
            S("Statement (c)", text="Positive: it is a prediction that evidence could support or reject."),
            S("Lesson", text="(b) and (c) are about the same policy. Economists can agree on (c) and still disagree on (b) because of different values."),
        ]),
        EX("Worked example 2: a distinction answer plan", intro="Plan a short answer to: 'Distinguish between the inductive and the deductive methods of testing hypotheses in economics.'", steps=[
            S("Define inductive", text="Reasoning from particular observed facts to a general theory."),
            S("Define deductive", text="Reasoning from general assumptions by logic to particular predictions that are then tested."),
            S("Contrast with a conjunction", text="The inductive method begins with data, whereas the deductive method begins with assumptions."),
            S("Illustrate each", text="Inductive: collecting price and sales data from Mokolo market and generalising. Deductive: assuming profit maximisation and deducing that firms produce where MC = MR."),
            S("Evaluate", text="In practice economists use both: deduction gives the prediction, induction (data) tests it."),
        ]),
        H("Is economics a science?"),
        KEY("Evaluation", "A balanced A Level answer gives both sides.", cards=[
            ["Yes", "It uses the scientific method: hypotheses, models, prediction and testing with data (econometrics). Many positive statements can be refuted."],
            ["Limits", "Controlled experiments are rarely possible, so ceteris paribus is an assumption, not a laboratory condition. People change behaviour, expectations matter, and data can be poor (large informal sector)."],
            ["Judgement", "Economics is best seen as a social science: scientific in method, but its predictions are less exact than those of physics and its policy advice always involves value judgements."],
        ]),
        MISTAKE("Using 'normative' to mean 'false'", "A normative statement is a value judgement, not a wrong statement. A positive statement can be wrong; it is positive because it can be tested."),
        MISTAKE("Defining the two methods separately without contrasting them", "In a 'distinguish' question, link the two ideas with 'whereas' or 'while'. Examiners report that candidates lose marks by writing two separate definitions and by confusing this question with positive and normative statements."),
        QUIZ("Which statement is positive?",
             ["Petrol in Cameroon is too expensive.", "A rise in the price of petrol will reduce the quantity of petrol bought, ceteris paribus.",
              "The government ought to cut fuel taxes.", "It is unfair that rural areas have fewer schools."], 1,
             "It makes a testable prediction about cause and effect.",
             hint="Which one could be checked with data?",
             feedback=["'Too expensive' is a judgement.", "", "'Ought to' signals a value judgement.", "'Unfair' is a value judgement."]),
        QUIZ("A researcher assumes that consumers maximise satisfaction and, by logic, predicts that a price fall raises quantity demanded. Which method is this?",
             ["Inductive", "Deductive", "Normative", "Ceteris paribus"], 1,
             "It starts from a general assumption and derives a particular prediction.",
             hint="Did the researcher start from data or from an assumption?",
             feedback=["Induction would start from observed data.", "", "Normative is a type of statement, not a method of reasoning.", "Ceteris paribus is an assumption used in both methods, not a method itself."]),
        H("Practice"),
        PQ("Explain why the ceteris paribus assumption is needed in economics.", "Many variables change at once in the real world (price, income, tastes, the prices of other goods). Economists cannot run controlled experiments on a whole market, so they hold other influences constant in their model. This isolates the effect of one variable, for example price on quantity demanded, so a clear testable prediction can be made."),
        PQ("Give one reason why two economists might disagree about whether Cameroon should raise import duties on rice.", "They may disagree on positive analysis (for example how much local rice output would respond) or on values (for example how much weight to give lower prices for poor urban consumers compared with incomes of local farmers). The first can be narrowed by evidence; the second cannot."),
        PQ("Essay plan: 'Economics cannot be a science because it deals with human behaviour.' Discuss.", "Introduction: define science (method of hypothesis, prediction and testing) and economics. For: economists form testable hypotheses, use models and ceteris paribus, test with data; many predictions (law of demand) hold well. Against: no controlled experiments, people react to expectations, data limits, value judgements in policy. Evaluation: economics is a social science; its method is scientific even if predictions are probabilistic. Conclusion: the statement is too strong."),
        PQ("Distinguish between microeconomics and macroeconomics, giving one Cameroonian example of each.", "Microeconomics studies individual consumers, firms and markets, whereas macroeconomics studies the economy as a whole. Micro example: how a fall in the world cocoa price affects the output of cocoa farmers in the South West. Macro example: the rate of inflation or unemployment in Cameroon as a whole."),
        TIP("Exam link: methodology appears in Paper 1 multiple-choice questions (classify a statement, identify a method) and as part of Paper 2 essays, often paired with scarcity and the PPC.", title="Exam link"),
        SUM("Positive statements can be tested by evidence; normative statements are value judgements.",
            "Economists form hypotheses, build models on assumptions and test predictions with data.",
            "Ceteris paribus holds other influences constant to isolate one cause.",
            "Induction goes from particular facts to a general theory, whereas deduction goes from assumptions to particular predictions.",
            "Economics is a social science: scientific in method, less exact in prediction."),
    ],
))

# ------------------------------------------------------------------ 2. Scarcity, choice and the PPC
LESSONS.append(lesson(
    module=M1,
    topic="Scarcity, choice and the production possibility curve",
    title="Scarcity, choice and opportunity cost on the production possibility curve",
    slug="ecl1-scarcity-choice-ppc",
    minutes=24,
    summary="Use the production possibility curve to show scarcity, choice and opportunity cost, explain why it is usually concave, calculate opportunity cost from a schedule, and analyse shifts and pivots.",
    objectives=[
        "Use a PPC to illustrate scarcity, choice and opportunity cost",
        "Calculate the opportunity cost of a move along a PPC from a schedule",
        "Explain why a PPC is usually concave to the origin (increasing opportunity cost)",
        "Analyse the causes of shifts and pivots of the PPC, including the choice between capital and consumer goods",
    ],
    key_concepts=["Scarcity", "Choice", "Opportunity cost", "Production possibility curve", "Increasing opportunity cost",
                  "Economic growth", "Capital goods and consumer goods"],
    blocks=[
        H("Introduction"),
        T("A farming region in the Centre Region has a fixed amount of land, labour, tools and know-how. Every hectare planted with "
          "cocoa is a hectare not planted with maize. This is the basic economic problem: wants are unlimited, resources are scarce, "
          "so choices must be made, and every choice has a cost. The **production possibility curve (PPC)** puts all three ideas on one diagram."),
        D("**Scarcity** means that resources are limited relative to the wants they could satisfy. **Choice** is the decision about which "
          "wants to satisfy and which to leave unsatisfied. **Opportunity cost** is the value of the next best alternative given up when a choice is made.",
          title="Definitions"),
        D("A **production possibility curve** shows the maximum combinations of two goods (or groups of goods) that an economy can produce "
          "when all its resources are fully and efficiently employed, with given technology, in a given period.",
          title="Definition: production possibility curve"),
        KEY("Assumptions behind the PPC", "State them in an essay; examiners reward assumptions.", cards=[
            ["Two goods", "Only two goods (or two groups such as capital and consumer goods) are produced."],
            ["Fixed resources", "The quantity and quality of factors of production are fixed in the period."],
            ["Given technology", "The state of technology does not change."],
            ["Full employment", "Points on the curve use all resources fully and efficiently."],
        ]),
        CODE("""Point   Cocoa (tonnes)   Maize (tonnes)
A              0               100
B             10                96
C             20                88
D             30                76
E             40                60
F             50                40
G             60                 0""", "text", title="Table 1. Production possibility schedule (invented for practice)"),
        IMG("alecl1-ppc.svg", alt="A concave production possibility curve PPC1 for cocoa on the horizontal axis and maize on the vertical axis, with points C and E on the curve, point U inside it, point X between PPC1 and an outward-shifted dashed curve PPC2.",
            caption="Figure 1. The PPC from Table 1 (PPC1) and an outward shift to PPC2."),
        H("Reading the PPC"),
        KEY("Three ideas in one diagram", "Explain each concept with the diagram, not just in words.", cards=[
            ["Scarcity", "Points outside PPC1, such as X, cannot be reached with present resources: the curve is a frontier. X becomes attainable only after growth shifts the curve to PPC2."],
            ["Choice", "The economy must choose one point on (or inside) the curve, such as C or E."],
            ["Opportunity cost", "Moving along the curve from C to E gives more cocoa only by giving up maize."],
        ]),
        T("A point inside the curve, such as U, shows **unemployed or inefficiently used resources**. The economy could produce more of "
          "both goods by moving to the curve, so the opportunity cost of that extra output is zero."),
        EX("Worked example 1: opportunity cost of a move", intro="Using Table 1, find the opportunity cost of moving from C to E, per tonne of cocoa.", steps=[
            S("Gain in cocoa", math=r"40 - 20 = 20 \text{ tonnes}"),
            S("Loss of maize", math=r"88 - 60 = 28 \text{ tonnes}"),
            S("Opportunity cost per tonne of cocoa", math=r"\frac{28}{20} = 1.4 \text{ tonnes of maize}"),
        ], check=r"20 \times 1.4 = 28"),
        EX("Worked example 2: increasing opportunity cost", intro="Find the opportunity cost of each extra 10 tonnes of cocoa along Table 1 and explain the pattern.", steps=[
            S("A to B, B to C, C to D", text="Maize lost: 4, 8 and 12 tonnes, i.e. 0.4, 0.8 and 1.2 tonnes of maize per tonne of cocoa."),
            S("D to E, E to F, F to G", text="Maize lost: 16, 20 and 40 tonnes, i.e. 1.6, 2.0 and 4.0 tonnes per tonne of cocoa."),
            S("Pattern", text="Each extra tonne of cocoa costs more maize: opportunity cost increases."),
            S("Reason", text="Resources are not equally suited to both crops. The land and workers best for cocoa move first; later the economy must use land and workers far better suited to maize, so much more maize is lost. This makes the PPC concave (bowed out) to the origin."),
        ]),
        TIP("If resources were equally suited to both goods, opportunity cost would be constant and the PPC would be a straight line. A question that gives a straight-line PPC is testing exactly this."),
        H("Shifts and pivots"),
        KEY("What moves the curve", "A movement along the curve is a change of choice; a shift is a change in capacity.", cards=[
            ["Outward shift (growth)", "More or better resources: population growth, more capital, better education and health (human capital), discovery of minerals, better technology in both sectors."],
            ["Inward shift", "Loss of capacity: war, natural disaster, emigration of skilled workers, depletion of resources."],
            ["Pivot", "Better technology in one sector only, for example improved cocoa seedlings: the cocoa end moves out, the maize end stays."],
        ]),
        D("**Economic growth** in the PPC sense is an increase in productive capacity, shown by an outward shift of the curve. A move from U to "
          "the curve is a rise in output from using idle resources, not a rise in capacity.", title="Definition: growth on a PPC"),
        T("When the two goods are **capital goods** and **consumer goods**, a country that chooses more capital goods today gives up consumption now "
          "but shifts its future PPC further out. This is the trade-off between present and future living standards."),
        MISTAKE("Explaining scarcity, choice and opportunity cost without the curve", "When a question says 'using a PPC', every concept must be linked to a labelled diagram: axes with goods named, the curve, and the points you discuss. The Board reports that candidates who explained the ideas in words only lost the diagram marks."),
        MISTAKE("Calling a move from inside to the curve 'economic growth'", "That is fuller use of existing resources (actual output rises). Growth in capacity is an outward shift of the whole curve."),
        QUIZ("Using Table 1, what is the opportunity cost of producing the first 10 tonnes of cocoa?",
             ["4 tonnes of maize", "10 tonnes of maize", "96 tonnes of maize", "0.4 tonnes of cocoa"], 0,
             "Maize falls from 100 to 96, so 4 tonnes of maize are given up.",
             hint="Opportunity cost is what you give up, not what you keep.",
             feedback=["", "That is the cocoa gained, not the maize lost.", "96 tonnes is the maize still produced at B.", "Opportunity cost of cocoa is measured in maize."]),
        QUIZ("A new disease-resistant maize variety is introduced. What happens to the PPC in Figure 1?",
             ["It shifts out parallel at both ends", "The maize end moves up while the cocoa end stays fixed", "The economy moves from C to E", "It shifts inward"], 1,
             "Better technology in maize only raises the maximum maize output; maximum cocoa output is unchanged.",
             hint="Which intercept depends on maize technology?",
             feedback=["A parallel shift needs better resources for both goods.", "", "That is a change of choice along the same curve.", "An improvement in technology cannot reduce capacity."]),
        H("Practice"),
        PQ("Using Table 1, calculate the opportunity cost of moving from B to F per tonne of cocoa.", "Cocoa rises from 10 to 50 (40 tonnes). Maize falls from 96 to 40 (56 tonnes). Opportunity cost = 56 / 40 = 1.4 tonnes of maize per tonne of cocoa."),
        PQ("Explain, with a diagram, why point U in Figure 1 shows inefficiency, and state the opportunity cost of moving from U to D.", "U (30 cocoa, 50 maize) lies inside the curve, so some resources are unemployed or badly used. D (30 cocoa, 76 maize) is on the curve. Moving from U to D gives 26 more tonnes of maize with no loss of cocoa, so the opportunity cost is zero."),
        PQ("Essay plan: (a) Using a PPC, explain the concepts of scarcity, choice and opportunity cost. (b) Explain two causes of an outward shift of a country's PPC.", "(a) Define and draw a labelled concave PPC. Scarcity: points outside unattainable. Choice: one point must be selected. Opportunity cost: a move along the curve, with a numerical example; explain the concave shape by increasing opportunity cost. (b) Two causes with mechanism: investment in capital (more machines raise maximum output of both goods); improved education and health (better quality labour). Evaluate: growth is gradual and may favour one good (pivot)."),
        PQ("Why might a government that wants faster long-run growth choose a point with more capital goods on its PPC? What is the cost?", "More capital goods (machines, roads, power plants) raise future productive capacity, shifting the PPC further out in later years. The cost is lower consumption now: the opportunity cost is the consumer goods given up today, which may be hard to accept where living standards are low."),
        TIP("Exam link: the PPC is a regular Paper 2 essay topic (often with methodology) and appears in Paper 1 as diagram and calculation questions. Always label axes with the two goods.", title="Exam link"),
        SUM("The PPC shows the maximum output combinations of two goods with fixed resources and technology.",
            "Scarcity: points outside are unattainable. Choice: one point must be chosen. Opportunity cost: a move along the curve.",
            "Opportunity cost per unit = amount of the other good given up / amount gained.",
            "A concave PPC reflects increasing opportunity cost because resources are not equally suited to both goods.",
            "Outward shifts show growth in capacity; inward shifts show loss of capacity; a pivot shows a change in one sector."),
    ],
))

# ------------------------------------------------------------------ 3. Economic efficiency
LESSONS.append(lesson(
    module=M1,
    topic="Economic efficiency",
    title="Productive, allocative, Pareto and dynamic efficiency",
    slug="ecl1-economic-efficiency",
    minutes=23,
    summary="The kinds of efficiency A Level economists use: productive (minimum average cost, on the PPC), allocative (price equals marginal cost), Pareto optimality, and dynamic and X-efficiency, with their limits.",
    objectives=[
        "Define productive efficiency and identify it from a cost table and on a PPC",
        "Explain allocative efficiency as the output where marginal benefit (price) equals marginal cost",
        "Explain Pareto optimality and link it to points on the PPC",
        "Distinguish static from dynamic efficiency and evaluate the trade-off between efficiency and equity",
    ],
    key_concepts=["Productive efficiency", "Allocative efficiency", "Pareto optimality", "Dynamic efficiency",
                  "X-inefficiency", "Marginal benefit", "Equity"],
    blocks=[
        H("Introduction"),
        T("A bakery in Buea can make bread at a low cost per loaf, but if it bakes bread nobody wants at that time of day the "
          "resources are still wasted. Economists therefore use more than one idea of efficiency. Some are about **how** goods are "
          "made (cost), others about **what** is made (whether it matches what people value)."),
        D("**Economic efficiency** is the use of scarce resources so that they cannot be rearranged to produce more output or more satisfaction. "
          "It has several parts, explained below.", title="Definition: economic efficiency"),
        H("Productive efficiency"),
        D("**Productive efficiency** means producing output at the lowest possible average (unit) cost. For a firm it is output at the "
          "minimum point of its average cost curve. For an economy it means being on the PPC: more of one good cannot be made without less of another.",
          title="Definition: productive efficiency"),
        CODE("""Output (loaves)   Total cost (FCFA thousand)   Average cost (FCFA)
1 000                     600                       600
2 000                   1 000                       500
3 000                   1 320                       440
4 000                   1 800                       450
5 000                   2 500                       500""", "text", title="Table 1. A bakery's costs (invented for practice)"),
        EX("Worked example 1: the productively efficient output", intro="Using Table 1, find the productively efficient output of the bakery.", steps=[
            S("Average cost formula", math=r"AC = \frac{TC}{Q}"),
            S("At 3 000 loaves", math=r"AC = \frac{1\,320\,000}{3\,000} = 440 \text{ FCFA}"),
            S("Compare", text="AC is 600, 500, 440, 450 and 500 FCFA. The lowest is 440 FCFA."),
            S("Answer", text="3 000 loaves is the productively efficient output in this table."),
        ], check=r"4\,000 \times 450 = 1\,800\,000"),
        H("Allocative efficiency"),
        D("**Allocative efficiency** means producing the combination of goods that society values most: resources are allocated so that "
          "the **marginal benefit** of the last unit (shown by the price consumers will pay) equals its **marginal cost** of production. "
          "The condition is P = MC.", title="Definition: allocative efficiency"),
        IMG("alecl1-alloc-eff.svg", alt="Demand curve labelled D = MB slopes down, supply curve labelled S = MC slopes up, meeting at Qe and Pe where MB = MC; at a lower output Q1 a shaded triangle between the curves is labelled loss.",
            caption="Figure 1. Output Qe is allocatively efficient. At Q1 the shaded triangle is the welfare lost."),
        KEY("Why P = MC", "Think about the last unit produced.", cards=[
            ["P > MC", "People value the next unit more than it costs to make: output is too low (Q1 in Figure 1). Producing more adds to welfare."],
            ["P < MC", "The last unit costs more than people value it: output is too high. Producing less adds to welfare."],
            ["P = MC", "No change in output can raise net welfare: allocative efficiency."],
        ]),
        EX("Worked example 2: allocative efficiency from equations", intro="Marginal benefit is MB = 100 - Q and marginal cost is MC = 20 + Q (FCFA, invented for practice). Find the allocatively efficient output and explain why Q = 25 is not efficient.", steps=[
            S("Set MB = MC", math=r"100 - Q = 20 + Q"),
            S("Solve", math=r"80 = 2Q \Rightarrow Q = 40"),
            S("At Q = 25", math=r"MB = 75,\quad MC = 45"),
            S("Conclude", text="At Q = 25 the last unit is worth 75 but costs 45, so more should be produced. Efficiency is at Q = 40, where MB = MC = 60."),
        ], check=r"100 - 40 = 20 + 40 = 60"),
        H("Pareto optimality"),
        D("An allocation is **Pareto optimal** (Pareto efficient) when it is impossible to make one person better off without making at least one other person worse off. The idea is named after the economist Vilfredo Pareto.",
          title="Definition: Pareto optimality"),
        T("Every point on a PPC is Pareto efficient in production: to get more cocoa, some maize must be given up. A point inside the curve is "
          "not, because a move to the curve can give more of both goods with no loser. A **Pareto improvement** is any change that makes at least one "
          "person better off and nobody worse off. Many real policies make some people better off and others worse off, so they are not Pareto improvements."),
        H("Dynamic efficiency and X-inefficiency"),
        KEY("Beyond static efficiency", "Productive and allocative efficiency are static (at a moment in time).", cards=[
            ["Dynamic efficiency", "Improvement in efficiency over time through investment, research and innovation that lower costs and create new products. It shifts cost curves down and the PPC out."],
            ["X-inefficiency", "A firm produces at a cost above the lowest possible for its output, usually because weak competition lets managers be slack (a term from Harvey Leibenstein). The firm is above its cost curve."],
        ]),
        H("Evaluation: efficiency and equity"),
        T("An efficient allocation is not necessarily fair. Many Pareto-optimal points exist, including one where a few people own almost everything. "
          "**Equity** (fairness in the distribution of income and wealth) is a separate, normative goal. Governments often trade a little efficiency for more "
          "equity, for example with progressive taxes. Also, P = MC gives allocative efficiency only if prices reflect all costs and benefits; "
          "externalities (studied later) break this link."),
        MISTAKE("Saying a firm at minimum AC is 'allocatively efficient'", "Minimum AC is productive efficiency. Allocative efficiency needs P = MC. The two can occur at different outputs."),
        MISTAKE("Treating 'Pareto efficient' as 'fair'", "Pareto efficiency says nothing about who gets what. Keep efficiency and equity apart."),
        QUIZ("At a firm's current output, price is 800 FCFA and marginal cost is 650 FCFA. From society's point of view, output should",
             ["fall", "rise", "stay the same", "rise only if average cost is falling"], 1,
             "P > MC: consumers value the next unit more than it costs to produce, so output should rise.",
             hint="Compare what people pay with what the extra unit costs.",
             feedback=["Output should fall only if P < MC.", "", "P = MC is not met.", "Allocative efficiency depends on P and MC, not on the slope of AC."]),
        QUIZ("Which change is a Pareto improvement?",
             ["A tax on the rich used to pay grants to the poor", "Moving from a point inside the PPC to a point on it with more of both goods",
              "Moving along the PPC from more maize to more cocoa", "Raising the price of fuel"], 1,
             "More of both goods can make someone better off with nobody worse off.",
             hint="Who loses in each change?",
             feedback=["The rich lose, so it is not a Pareto improvement.", "", "Maize users lose maize.", "Fuel buyers are made worse off."]),
        H("Practice"),
        PQ("Distinguish between productive efficiency and allocative efficiency.", "Productive efficiency is producing at the lowest average cost (on the PPC, at minimum AC), whereas allocative efficiency is producing the mix of goods consumers value most, where price (marginal benefit) equals marginal cost."),
        PQ("Marginal benefit is MB = 90 - 2Q and marginal cost is MC = 10 + 2Q. Find the allocatively efficient output and price.", "Set 90 - 2Q = 10 + 2Q, so 80 = 4Q and Q = 20. Price = MB = 90 - 40 = 50. Check: MC = 10 + 40 = 50."),
        PQ("Essay plan: 'An economy on its PPC is efficient.' Discuss.", "Define the PPC and efficiency. Agree: on the PPC means productive efficiency and Pareto efficiency in production. But: the chosen point may not be allocatively efficient (wrong mix: P not equal to MC); firms may be X-inefficient in practice; static efficiency may not bring dynamic efficiency; and an efficient point may be very unequal. Conclude: being on the PPC is necessary but not sufficient for full economic efficiency."),
        PQ("Why might a firm with little competition be X-inefficient? Give one Cameroonian-style example.", "Without rivals there is less pressure to control costs, so managers may overstaff, buy inputs carelessly or delay repairs. Example: a sole supplier of a service in a town may keep high costs because customers cannot switch; costs sit above the lowest possible level."),
        TIP("Exam link: efficiency concepts appear in Paper 1 (definitions, P = MC) and support Paper 2 essays on market structures and market failure. Always state the condition for each type.", title="Exam link"),
        SUM("Productive efficiency: lowest average cost; for the economy, on the PPC.",
            "Allocative efficiency: output where price (marginal benefit) equals marginal cost.",
            "Pareto optimal: nobody can be made better off without someone being made worse off.",
            "Dynamic efficiency is improvement over time; X-inefficiency is cost above the lowest possible.",
            "Efficiency is not equity: an efficient outcome can still be very unequal."),
    ],
))

# ------------------------------------------------------------------ 4. Economic systems
LESSONS.append(lesson(
    module=M1,
    topic="Economic systems",
    title="Market, command and mixed economies: how resources are allocated",
    slug="ecl1-economic-systems",
    minutes=23,
    summary="How market, command and mixed economies answer what, how and for whom to produce; the signalling, incentive and rationing functions of the price mechanism; and an evaluation of each system's strengths and weaknesses.",
    objectives=[
        "Explain how each economic system answers the questions what, how and for whom",
        "Explain the signalling, incentive and rationing functions of the price mechanism",
        "Evaluate the strengths and weaknesses of market and command economies",
        "Explain why most economies, including Cameroon's, are mixed",
    ],
    key_concepts=["Economic system", "Price mechanism", "Signalling function", "Incentive function", "Rationing function",
                  "Command economy", "Mixed economy", "Consumer sovereignty"],
    blocks=[
        H("Introduction"),
        T("Every society must answer three questions: **what** to produce, **how** to produce it and **for whom**. At O Level you "
          "described the systems. At A Level you must explain the **mechanism** each system uses and **evaluate** it. When the price "
          "of tomatoes at Mfoundi market doubles after heavy rains, nobody orders farmers to grow more, yet within months more tomatoes arrive. "
          "That is the price mechanism at work."),
        D("An **economic system** is the set of institutions and rules by which a society decides what, how and for whom to produce. "
          "Systems differ in who owns resources (private individuals or the state) and how decisions are coordinated (prices or plans).",
          title="Definition: economic system"),
        KEY("Three systems compared", "Use ownership and coordination to classify.", cards=[
            ["Market (free enterprise)", "Resources mainly privately owned. Decisions coordinated by prices through the interaction of demand and supply. Government limited to law, order and property rights."],
            ["Command (planned)", "Resources mainly state-owned. A central planning authority sets output targets, methods and the distribution of goods."],
            ["Mixed", "A private sector using prices alongside a public sector and government intervention (taxes, subsidies, regulation, state firms)."],
        ]),
        H("The price mechanism"),
        D("The **price mechanism** is the system in which changes in the relative prices of goods and factors, caused by changes in demand and supply, "
          "allocate resources between their different uses.", title="Definition: price mechanism"),
        KEY("Three functions of price", "A strong answer names the function and explains the chain of cause and effect.", cards=[
            ["Signalling", "A price rise tells producers that consumers want more of the good, and tells consumers the good has become scarcer."],
            ["Incentive", "A higher price raises the expected profit from producing the good, so firms expand output and new firms enter; resources move towards it."],
            ["Rationing", "A higher price discourages some buyers, so the limited quantity goes to those most willing and able to pay."],
        ]),
        EX("Worked example 1: the price mechanism after a demand increase", intro="Demand for cement rises as house building expands in Douala. Explain how the price mechanism reallocates resources.", steps=[
            S("Shortage", text="At the old price quantity demanded exceeds quantity supplied."),
            S("Signal", text="The price of cement rises, signalling that cement is wanted more urgently."),
            S("Incentive", text="Higher prices raise profits, so producers raise output and may import or build new capacity; labour and capital move into cement."),
            S("Ration", text="Higher prices ration the available cement to buyers most willing to pay, and some building is delayed."),
            S("Result", text="A new equilibrium with more cement produced: resources have moved without any central order."),
        ]),
        D("**Consumer sovereignty** is the idea that, in a market economy, consumers' spending decisions determine what is produced. "
          "The phrase 'invisible hand', used by Adam Smith, describes how self-interested buyers and sellers are led by prices to an outcome that serves society.",
          title="Definition: consumer sovereignty"),
        H("Evaluating the systems"),
        KEY("Market economy", "Strengths and weaknesses.", cards=[
            ["Strengths", "Efficient use of information: prices carry knowledge no planner holds. Strong incentives to cut costs and innovate. Wide choice. Quick response to changes in demand."],
            ["Weaknesses", "Market failure: public goods are under-provided, externalities ignored, merit goods under-consumed. Income inequality: 'for whom' depends on purchasing power. Monopoly power. Instability (booms and slumps)."],
        ]),
        KEY("Command economy", "Strengths and weaknesses.", cards=[
            ["Strengths", "Can direct resources to national priorities (heavy industry, defence, basic education). Can reduce inequality and open unemployment. Can provide public goods."],
            ["Weaknesses", "Information problem: planners cannot know millions of preferences and costs, so shortages and surpluses persist. Weak incentives to work and innovate. Bureaucracy, queues and black markets. Little consumer choice."],
        ]),
        EX("Worked example 2: an essay plan", intro="Plan an answer to: 'The price mechanism is the best way to allocate resources.' Discuss.", steps=[
            S("Introduction", text="Define the price mechanism and the three economic questions."),
            S("For", text="Explain signalling, incentive and rationing with an example; efficiency (allocative when P = MC in competitive markets); innovation; choice."),
            S("Against", text="Market failures (public goods, externalities, merit and demerit goods), inequality, monopoly, instability."),
            S("Alternative", text="Planning can correct some failures but suffers from the information and incentive problems."),
            S("Conclusion", text="The price mechanism is usually the best coordinator of most goods, but government intervention is needed where markets fail: the case for a mixed economy."),
        ]),
        H("Mixed economies and Cameroon"),
        T("All real economies are mixed; they differ in the balance between market and state. Cameroon has a large private sector, including a very "
          "large informal sector of traders and small producers, alongside public enterprises and government regulation and spending on roads, "
          "health and education. Since the late 1980s and 1990s it, like many African economies, moved towards more market allocation, including the "
          "privatisation of some public enterprises. For the details of particular reforms, check your textbook."),
        MISTAKE("Listing features without the mechanism", "Saying 'in a market economy prices decide' earns little. Explain the chain: change in demand, price change, signal, incentive, reallocation."),
        MISTAKE("Calling the price mechanism 'perfect'", "Always evaluate: markets fail in known ways and can leave large inequality."),
        QUIZ("A fall in the price of plantains leads some farmers to switch land to cassava. Which function of the price mechanism does this show most clearly?",
             ["Rationing", "Incentive", "Consumer sovereignty", "Planning"], 1,
             "Lower prices reduce the reward from plantains, giving farmers an incentive to move resources elsewhere.",
             hint="Which function is about producers' rewards?",
             feedback=["Rationing is about which buyers get the good.", "", "Consumer sovereignty is the broader idea, not the function shown.", "No planner is involved."]),
        QUIZ("The main reason command economies struggle to allocate resources efficiently is that",
             ["planners cannot gather and process information on all preferences and costs", "they have no government", "prices are too high", "all firms are privately owned"], 0,
             "The information problem: millions of changing preferences and costs cannot be known centrally.",
             hint="What do prices carry that a planner lacks?",
             feedback=["", "A command economy is run by the government.", "Planners often set prices low, causing shortages.", "In a command economy most resources are state-owned."]),
        H("Practice"),
        PQ("Explain the rationing function of price, using an example.", "When a good is scarce, its price rises. Some consumers are no longer willing or able to buy, so quantity demanded falls to match the available quantity. Example: when fish catches fall, fish prices rise and the smaller supply goes to buyers willing to pay most."),
        PQ("Give two reasons why a market economy might produce too few health services.", "Health care has positive externalities (treating infectious disease protects others), so private benefit is less than social benefit. It is also a merit good: people may underestimate its benefit or be unable to pay, so the market leaves many without care."),
        PQ("Essay plan: Discuss the advantages and disadvantages of a mixed economy.", "Define a mixed economy. Advantages: price mechanism keeps incentives and choice; government corrects market failure (public goods, merit goods, externalities), reduces inequality and stabilises the economy. Disadvantages: government failure (inefficient state firms, corruption, bureaucracy), high taxes may weaken incentives, unclear boundary between sectors. Evaluation: success depends on the quality of institutions and the balance chosen."),
        PQ("Distinguish between a market economy and a command economy.", "In a market economy resources are mainly privately owned and allocated by prices, whereas in a command economy resources are mainly state-owned and allocated by a central plan."),
        TIP("Exam link: economic systems appear in Paper 1 (functions of price, features of systems) and in Paper 2 essays that ask you to evaluate the price mechanism or a mixed economy.", title="Exam link"),
        SUM("Economic systems answer what, how and for whom; they differ in ownership and coordination.",
            "The price mechanism allocates resources through signalling, incentive and rationing.",
            "Markets are efficient at using information and create incentives, but fail with public goods, externalities and inequality.",
            "Command economies can pursue priorities but suffer information and incentive problems.",
            "All real economies, including Cameroon's, are mixed."),
    ],
))

# ------------------------------------------------------------------ 5. Demand and supply functions
LESSONS.append(lesson(
    module=M2,
    topic="Demand and supply functions",
    title="Demand and supply functions and market equilibrium",
    slug="ecl1-demand-supply-functions",
    minutes=25,
    summary="Write demand and supply as functions, tell movements along a curve from shifts, solve linear functions for equilibrium price and quantity, and analyse shifts, shortages and surpluses with numbers and diagrams.",
    objectives=[
        "Write the general demand and supply functions and list their determinants",
        "Distinguish a change in quantity demanded (or supplied) from a change in demand (or supply)",
        "Solve linear demand and supply functions for equilibrium and for the effect of a shift",
        "Calculate shortages and surpluses when price is not at equilibrium",
    ],
    key_concepts=["Demand function", "Supply function", "Change in quantity demanded", "Change in demand",
                  "Equilibrium", "Excess demand", "Excess supply", "Linear function"],
    blocks=[
        H("Introduction"),
        T("At O Level you drew demand and supply curves. At A Level you also write them as **functions**, which lets you calculate "
          "equilibrium and the size of any change. Cocoa cooperatives, fuel distributors and the government all need numbers, not just "
          "arrows: by how much will the price of rice rise if incomes grow? How large is the shortage if a price is fixed below equilibrium?"),
        D("**Demand** is the quantity of a good that consumers are willing and able to buy at each price in a given period, ceteris paribus. "
          "**Supply** is the quantity producers are willing and able to sell at each price in a given period, ceteris paribus.",
          title="Definitions: demand and supply"),
        H("The general functions"),
        F(r"Q_d = f(P,\ P_r,\ Y,\ T,\ N,\ E,\ \ldots)", title="Demand function"),
        T("Quantity demanded depends on the good's own price P, the prices of related goods $P_r$ (substitutes and complements), income Y, "
          "tastes T, population N, expectations E and other factors such as credit and season."),
        F(r"Q_s = g(P,\ C,\ Tech,\ P_o,\ Tx,\ W,\ \ldots)", title="Supply function"),
        T("Quantity supplied depends on own price P, costs of factors C, technology, the prices of other goods the producer could make $P_o$, "
          "taxes and subsidies Tx, weather W (very important for farm output) and the number of producers."),
        KEY("Movement or shift?", "The single most tested distinction in this topic.", cards=[
            ["Movement along the curve", "Caused only by a change in the good's **own price**. Called a change in **quantity** demanded (or quantity supplied): extension or contraction."],
            ["Shift of the curve", "Caused by a change in **any other** determinant. Called a change in **demand** (or **supply**): an increase shifts the curve right, a decrease shifts it left."],
        ]),
        H("Linear functions and equilibrium"),
        D("A **linear demand function** has the form $Q_d = a - bP$ ($b > 0$) and a **linear supply function** $Q_s = c + dP$ ($d > 0$). "
          "**Equilibrium** is the price at which quantity demanded equals quantity supplied, so there is no tendency for price to change.",
          title="Definitions: linear functions and equilibrium"),
        EX("Worked example 1: solving for equilibrium", intro="The weekly market for tomatoes in a town is $Q_d = 1200 - 4P$ and $Q_s = -300 + 6P$, with P in FCFA per kg and Q in kg (invented for practice). Find the equilibrium.", steps=[
            S("Set quantity demanded equal to quantity supplied", math=r"1200 - 4P = -300 + 6P"),
            S("Collect terms", math=r"1500 = 10P"),
            S("Equilibrium price", math=r"P = 150 \text{ FCFA per kg}"),
            S("Equilibrium quantity", math=r"Q = 1200 - 4(150) = 600 \text{ kg}"),
        ], check=r"-300 + 6(150) = 600"),
        IMG("alecl1-ds-func.svg", alt="Downward demand curve D1 and upward supply curve S meet at E1, price 150 and quantity 600. A dashed demand curve D2 to the right meets S at E2, price 170 and quantity 720.",
            caption="Figure 1. The tomato market: an increase in demand from D1 to D2."),
        EX("Worked example 2: an increase in demand", intro="Incomes rise and demand becomes $Q_d = 1400 - 4P$ (supply unchanged). Find the new equilibrium and describe the change.", steps=[
            S("New equation", math=r"1400 - 4P = -300 + 6P"),
            S("Solve", math=r"1700 = 10P \Rightarrow P = 170"),
            S("Quantity", math=r"Q = 1400 - 4(170) = 720"),
            S("Describe", text="Demand increased (the curve shifted right), price rose by 20 FCFA and the quantity supplied extended along S from 600 to 720 kg."),
        ], check=r"-300 + 6(170) = 720"),
        EX("Worked example 3: a maximum price", intro="With the original functions, the council fixes a maximum price of 120 FCFA per kg. Find the shortage.", steps=[
            S("Quantity demanded at 120", math=r"Q_d = 1200 - 4(120) = 720"),
            S("Quantity supplied at 120", math=r"Q_s = -300 + 6(120) = 420"),
            S("Excess demand (shortage)", math=r"720 - 420 = 300 \text{ kg}"),
            S("Comment", text="A price below equilibrium creates a shortage; queues, rationing or black markets may follow."),
        ]),
        T("A supply shift works in the same way. If fertiliser lowers costs and supply becomes $Q_s = -100 + 6P$, then $1200 - 4P = -100 + 6P$ "
          "gives P = 130 and Q = 680: price falls and quantity rises."),
        MISTAKE("Saying 'demand equals supply' at equilibrium", "Equilibrium is where **quantity demanded** equals **quantity supplied**. Examiners report that candidates lose marks by saying 'demand equals supply'."),
        MISTAKE("Giving determinants of demand when asked about supply (or about elasticity)", "Read the question. Factors that increase supply are not the determinants of demand, and not the determinants of price elasticity of supply. Explain them in the direction asked: 'a fall in the price of fertiliser increases supply because...'."),
        MISTAKE("Ignoring the units in a table", "If a table says price in '000 FCFA, a price of 150 means 150 000 FCFA. State the units in your answer."),
        QUIZ("Which event causes a movement along the demand curve for rice, not a shift?",
             ["A rise in consumers' incomes", "A fall in the price of rice", "A rise in the price of bread, a substitute", "A rise in population"], 1,
             "Only a change in the good's own price causes a movement along its demand curve.",
             hint="Which change is in the price of rice itself?",
             feedback=["Income shifts the curve.", "", "The price of a substitute shifts the demand curve.", "Population shifts the curve."]),
        QUIZ("Demand is $Q_d = 500 - 5P$ and supply is $Q_s = -100 + 10P$. What is the equilibrium price?",
             ["30", "40", "60", "300"], 1,
             "500 - 5P = -100 + 10P gives 600 = 15P, so P = 40.",
             hint="Set the two quantities equal and collect the P terms.",
             feedback=["At 30, Qd = 350 and Qs = 200: there is a shortage.", "", "At 60, Qd = 200 and Qs = 500: a surplus.", "300 is the equilibrium quantity, not the price."]),
        H("Practice"),
        PQ("Using the original tomato functions, find the surplus if a minimum price of 200 FCFA is set.", "Qd = 1200 - 800 = 400 kg. Qs = -300 + 1200 = 900 kg. Excess supply = 900 - 400 = 500 kg."),
        PQ("Demand is $Q_d = 900 - 3P$ and supply is $Q_s = -100 + 2P$. Find equilibrium price and quantity.", "900 - 3P = -100 + 2P, so 1000 = 5P and P = 200. Q = 900 - 600 = 300. Check: -100 + 400 = 300."),
        PQ("Price per tonne ('000 FCFA): 100, 150, 200, 250, 300. Quantity demanded (tonnes): 800, 700, 600, 500, 400. Quantity supplied: 200, 400, 600, 800, 1000. (a) State and justify the equilibrium price. (b) After fertiliser is used, supply rises by 300 tonnes at every price. Find the new equilibrium.", "(a) 200 000 FCFA per tonne, because at this price quantity demanded equals quantity supplied (600 tonnes). (b) New supply: 500, 700, 900, 1100, 1300. At 150 000 FCFA, quantity demanded = quantity supplied = 700 tonnes, so the new equilibrium is 150 000 FCFA per tonne and 700 tonnes."),
        PQ("Explain four factors that could increase the supply of cocoa in Cameroon.", "Each is directional: (1) better weather or rainfall raises yields; (2) a fall in the price of fertiliser or pesticides lowers costs, so more is supplied at each price; (3) improved seedlings or farming methods raise output per hectare; (4) a subsidy to farmers lowers effective costs; also more farmers entering, or a fall in the price of an alternative crop such as coffee, so land switches to cocoa."),
        TIP("Exam link: functions and equilibrium calculations appear in Paper 1 and in Paper 3 data-response questions with schedules; Paper 2 asks you to explain shifts in a directional way.", title="Exam link"),
        SUM("Demand and supply depend on own price and on other determinants (the functions).",
            "Own price moves you along a curve; any other determinant shifts it.",
            "Equilibrium: set quantity demanded equal to quantity supplied and solve for P, then Q.",
            "A shift changes the constant in the function; re-solve to find the new equilibrium.",
            "Below equilibrium price there is a shortage; above it a surplus."),
    ],
))

# ------------------------------------------------------------------ 6. Elasticities
LESSONS.append(lesson(
    module=M2,
    topic="Elasticities of demand and supply",
    title="Price, income and cross elasticity of demand and price elasticity of supply",
    slug="ecl1-elasticities",
    minutes=25,
    summary="Calculate and interpret PED (including point elasticity on a linear demand curve), YED, XED and PES; link PED to total revenue; explain the determinants of each elasticity and their uses for firms and government.",
    objectives=[
        "Calculate PED, YED, XED and PES from data and interpret the sign and size",
        "Calculate point elasticity on a linear demand function and explain why PED varies along a straight line",
        "Explain the relationship between PED and total revenue",
        "Explain the determinants of PED and PES and the uses of elasticity for firms and government",
    ],
    key_concepts=["Price elasticity of demand", "Point elasticity", "Total revenue", "Income elasticity of demand",
                  "Cross elasticity of demand", "Price elasticity of supply", "Normal and inferior goods"],
    blocks=[
        H("Introduction"),
        T("A soft-drink company in Douala wants to raise its price. Will its revenue rise or fall? The government wants to raise a tax on "
          "beer. Will consumption fall much? Elasticity answers these questions by measuring **how strongly** quantity responds to a change in "
          "price, income or the price of another good."),
        D("**Elasticity** is the responsiveness of one variable to a change in another, measured as the percentage change in the first divided "
          "by the percentage change in the second.", title="Definition: elasticity"),
        H("Price elasticity of demand (PED)"),
        F(r"PED = \frac{\%\Delta Q_d}{\%\Delta P}", title="Price elasticity of demand"),
        T("PED is negative for normal demand curves because price and quantity demanded move in opposite directions; economists usually compare "
          "its absolute value. |PED| > 1 is **elastic**, |PED| < 1 is **inelastic**, |PED| = 1 is **unitary**, 0 is **perfectly inelastic** "
          "and infinity is **perfectly elastic**."),
        EX("Worked example 1: PED and total revenue", intro="A drinks seller raises the price of a bottle from 400 to 500 FCFA and daily sales fall from 1 000 to 850 bottles (invented for practice). Find PED and the effect on revenue.", steps=[
            S("Percentage change in quantity", math=r"\frac{850 - 1000}{1000} \times 100 = -15\%"),
            S("Percentage change in price", math=r"\frac{500 - 400}{400} \times 100 = 25\%"),
            S("PED", math=r"\frac{-15}{25} = -0.6 \text{ (inelastic)}"),
            S("Total revenue", math=r"400 \times 1000 = 400\,000 \;\rightarrow\; 500 \times 850 = 425\,000"),
            S("Interpret", text="Demand is inelastic, so the price rise increases total revenue by 25 000 FCFA."),
        ]),
        KEY("PED and total revenue (TR = P x Q)", "Learn the three cases.", cards=[
            ["Elastic (|PED| > 1)", "Price and TR move in opposite directions: a price cut raises TR."],
            ["Inelastic (|PED| < 1)", "Price and TR move in the same direction: a price rise raises TR."],
            ["Unitary (|PED| = 1)", "TR does not change when price changes; TR is at its maximum."],
        ]),
        TIP("Textbooks differ on the base for percentage changes. This lesson uses the original values. Some use the average of the old and new values (the arc or midpoint method), which gives the same answer whichever direction the change goes; for Worked example 1 it gives about -0.73. Check your textbook and use the method your teacher expects."),
        H("Point elasticity on a linear demand curve"),
        F(r"PED = \frac{\Delta Q}{\Delta P} \times \frac{P}{Q}", title="Point elasticity"),
        EX("Worked example 2: PED varies along a straight line", intro="Demand is $Q_d = 1200 - 4P$. Find PED at P = 100, P = 150 and P = 250.", steps=[
            S("Slope term", math=r"\frac{\Delta Q}{\Delta P} = -4"),
            S("At P = 100, Q = 800", math=r"PED = -4 \times \frac{100}{800} = -0.5"),
            S("At P = 150, Q = 600", math=r"PED = -4 \times \frac{150}{600} = -1"),
            S("At P = 250, Q = 200", math=r"PED = -4 \times \frac{250}{200} = -5"),
            S("Conclusion", text="The slope is constant but P/Q rises as we move up the line, so demand is inelastic at low prices, unitary at the midpoint and elastic at high prices."),
        ]),
        MISTAKE("Confusing slope with elasticity", "A straight-line demand curve has a constant slope but its elasticity changes at every point. Only vertical, horizontal and rectangular-hyperbola curves have constant elasticity."),
        KEY("Determinants of PED", "Explain each, do not just list.", cards=[
            ["Substitutes", "More and closer substitutes make demand more elastic (one brand of soap versus soap in general)."],
            ["Share of income", "Goods taking a large share of income (a motorbike) are more elastic than cheap items (matches)."],
            ["Necessity or habit", "Necessities and addictive goods (salt, cigarettes) are inelastic."],
            ["Time", "Demand is more elastic in the long run as buyers find alternatives."],
            ["Definition of the market", "A broadly defined good (food) is less elastic than a narrow one (one brand of rice)."],
        ]),
        H("Income and cross elasticity"),
        F(r"YED = \frac{\%\Delta Q_d}{\%\Delta Y} \qquad XED_{AB} = \frac{\%\Delta Q_{dA}}{\%\Delta P_B}", title="YED and XED"),
        KEY("Reading the sign", "The sign tells you the type of good.", cards=[
            ["YED > 1", "Normal good, income elastic (a luxury): demand rises faster than income."],
            ["0 < YED < 1", "Normal good, income inelastic (a necessity)."],
            ["YED < 0", "Inferior good: demand falls as income rises."],
            ["XED > 0", "Substitutes: a rise in the price of B raises demand for A."],
            ["XED < 0", "Complements: a rise in the price of B lowers demand for A."],
            ["XED = 0", "Unrelated goods."],
        ]),
        EX("Worked example 3: YED, XED and PES", intro="(a) Monthly income rises from 200 000 to 220 000 FCFA and a family's rice purchases rise from 50 to 54 kg. (b) The price of beef rises by 20% and demand for fish rises by 10%. (c) The price of plantain rises by 20% and quantity supplied rises from 500 to 550 bunches. Find each elasticity (invented for practice).", steps=[
            S("(a) YED", math=r"\frac{8\%}{10\%} = 0.8", text="Positive and below 1: rice is a normal necessity for this family."),
            S("(b) XED", math=r"\frac{+10\%}{+20\%} = +0.5", text="Positive: beef and fish are substitutes."),
            S("(c) PES", math=r"\frac{10\%}{20\%} = 0.5", text="Supply is price inelastic."),
        ]),
        H("Price elasticity of supply (PES)"),
        F(r"PES = \frac{\%\Delta Q_s}{\%\Delta P}", title="Price elasticity of supply"),
        T("PES is normally positive. Its determinants are: **time** (supply is more elastic in the long run; farm output is inelastic in the short run "
          "because crops take months to grow), **spare capacity**, **stocks** (goods that can be stored, like dried cocoa, are more elastic), "
          "**mobility of factors** and the **ease of entry** of new firms. Do not mix these up with the determinants of supply."),
        H("Uses of elasticity"),
        T("Firms use PED to set prices and XED to judge rivals' prices. Governments use PED when choosing goods to tax: taxes on goods with "
          "inelastic demand raise much revenue but fall heavily on consumers. YED helps planners forecast which industries will grow as incomes rise. "
          "Low PES of farm goods helps explain why farm prices fluctuate so much."),
        QUIZ("PED for a good is -2. If its price falls by 5%, total revenue will",
             ["fall", "rise", "stay the same", "fall by 10%"], 1,
             "Elastic demand: quantity rises by 10%, more than the 5% price fall, so TR rises.",
             hint="Elastic: price and TR move in opposite directions.",
             feedback=["TR falls after a price cut only when demand is inelastic.", "", "TR is unchanged only at unitary elasticity.", "Quantity rises by 10%; TR rises by about 4.5%."]),
        QUIZ("YED for second-hand clothes is -0.4. This means they are",
             ["a luxury good", "a normal necessity", "an inferior good", "a complement of new clothes"], 2,
             "Negative YED: demand falls as income rises.",
             hint="What does a negative income elasticity mean?",
             feedback=["A luxury has YED greater than 1.", "A normal necessity has YED between 0 and 1.", "", "Complements are identified by XED, not YED."]),
        H("Practice"),
        PQ("Demand is $Q_d = 1200 - 4P$. Calculate PED at P = 200 and say whether a price rise from 200 would raise or lower total revenue.", "At P = 200, Q = 400. PED = -4 x 200/400 = -2 (elastic). A price rise would lower total revenue."),
        PQ("The price of sugar falls from 800 to 600 FCFA per kg and the demand for tea rises by 5%. Calculate XED and state the relationship.", "Price change = -200/800 = -25%. XED = 5 / -25 = -0.2. Negative, so sugar and tea are complements (weak relationship)."),
        PQ("Explain three determinants of the price elasticity of supply of cocoa.", "Time: in the short run trees cannot be planted and grown, so PES is low; in the long run new farms can be planted. Stocks: dried cocoa beans can be stored, so producers can release more when price rises. Spare capacity: if farmers have unused land and labour they can expand output quickly, so PES is higher."),
        PQ("Essay plan: Explain how knowledge of price elasticity of demand is useful to (a) a firm and (b) the government.", "(a) Firm: pricing to raise revenue (raise price if inelastic, cut if elastic); price discrimination between markets with different PED; forecasting sales. (b) Government: choosing goods for indirect taxes (inelastic demand gives stable revenue); predicting the burden of tax on consumers; effect of devaluation on exports and imports. Evaluate: PED estimates are uncertain and change over time."),
        TIP("Exam link: elasticity calculations are common in Paper 1 and Paper 3; Paper 2 essays ask for determinants and uses. Show the formula, the substitution and the interpretation.", title="Exam link"),
        SUM("PED, YED, XED and PES are percentage change in quantity divided by percentage change in the cause.",
            "|PED| > 1 elastic: price and TR move in opposite directions; |PED| < 1 inelastic: same direction.",
            "On a straight-line demand curve PED = (change in Q / change in P) x (P/Q) and varies along the line.",
            "YED sign: positive normal, negative inferior. XED sign: positive substitutes, negative complements.",
            "PES depends on time, spare capacity, stocks and factor mobility."),
    ],
))

# ------------------------------------------------------------------ 7. Consumer and producer surplus
LESSONS.append(lesson(
    module=M2,
    topic="Consumer and producer surplus",
    title="Consumer surplus, producer surplus and economic welfare",
    slug="ecl1-consumer-producer-surplus",
    minutes=23,
    summary="Define and calculate consumer and producer surplus from schedules and linear functions, show them on a demand and supply diagram, and use them to measure welfare changes and the deadweight loss of a maximum price.",
    objectives=[
        "Define consumer surplus and producer surplus and show them on a diagram",
        "Calculate both surpluses from a schedule and from linear demand and supply functions",
        "Analyse how surpluses change when demand or supply shifts",
        "Calculate the deadweight loss caused by a price control and evaluate the measure",
    ],
    key_concepts=["Consumer surplus", "Producer surplus", "Willingness to pay", "Total surplus (economic welfare)",
                  "Deadweight loss", "Price control"],
    blocks=[
        H("Introduction"),
        T("A student in Dschang is ready to pay 1 000 FCFA for a plate of food but the seller charges 600 FCFA. She gains 400 FCFA of "
          "satisfaction she did not pay for. The seller would have accepted 450 FCFA, so he also gains. These gains are **consumer surplus** and "
          "**producer surplus**. Adding them up for a whole market gives economists a money measure of the welfare the market creates."),
        D("**Consumer surplus** is the difference between the total amount consumers are willing to pay for a quantity of a good and the amount they "
          "actually pay. On a diagram it is the area below the demand curve and above the price.", title="Definition: consumer surplus"),
        D("**Producer surplus** is the difference between the total amount producers receive for a quantity and the minimum they would have accepted "
          "to supply it. On a diagram it is the area above the supply curve and below the price.", title="Definition: producer surplus"),
        IMG("alecl1-surplus.svg", alt="Demand curve D from point a on the price axis and supply curve S from point b meet at Pe and Qe. The triangle above Pe and below D is labelled CS; the triangle below Pe and above S is labelled PS.",
            caption="Figure 1. Consumer surplus (CS) and producer surplus (PS) at equilibrium."),
        KEY("Why the demand curve measures willingness to pay", "Read the demand curve vertically.", cards=[
            ["Demand curve", "The height of the demand curve at each quantity is the most the marginal buyer will pay: the marginal benefit."],
            ["Supply curve", "The height of the supply curve at each quantity is the least the marginal seller will accept: the marginal cost."],
            ["Total surplus", "CS + PS is the total welfare from the market. It is largest at the competitive equilibrium, where MB = MC."],
        ]),
        EX("Worked example 1: surplus from a schedule", intro="Five buyers will pay at most 1 000, 800, 700, 600 and 500 FCFA for one plate each. The price is 600 FCFA. Find consumer surplus.", steps=[
            S("Who buys", text="The buyers willing to pay 1 000, 800, 700 and 600 FCFA buy. The 500 FCFA buyer does not."),
            S("Surplus of each", math=r"400 + 200 + 100 + 0"),
            S("Consumer surplus", math=r"= 700 \text{ FCFA}"),
        ]),
        EX("Worked example 2: surplus from linear functions", intro="The tomato market is $Q_d = 1200 - 4P$ and $Q_s = -300 + 6P$ (P in FCFA per kg). Equilibrium is P = 150, Q = 600. Calculate CS and PS.", steps=[
            S("Demand intercept (Q = 0)", math=r"P = \frac{1200}{4} = 300"),
            S("Supply intercept (Q = 0)", math=r"P = \frac{300}{6} = 50"),
            S("Consumer surplus (triangle)", math=r"\tfrac{1}{2} \times 600 \times (300 - 150) = 45\,000 \text{ FCFA}"),
            S("Producer surplus (triangle)", math=r"\tfrac{1}{2} \times 600 \times (150 - 50) = 30\,000 \text{ FCFA}"),
            S("Total surplus", math=r"45\,000 + 30\,000 = 75\,000 \text{ FCFA}"),
        ]),
        H("Changes in surplus"),
        T("When demand rises to $Q_d = 1400 - 4P$, the new equilibrium is P = 170, Q = 720. The new demand intercept is 350, so CS = 0.5 x 720 x 180 = "
          "64 800 FCFA and PS = 0.5 x 720 x 120 = 43 200 FCFA. Both rise. A rise in price alone (with a fixed demand curve) moves surplus from consumers to producers."),
        H("Deadweight loss from a price control"),
        D("**Deadweight loss** is the loss of total surplus (CS + PS) that occurs when output differs from the efficient quantity. It is welfare that nobody receives.",
          title="Definition: deadweight loss"),
        EX("Worked example 3: a maximum price of 120 FCFA", intro="The council fixes a maximum price of 120 FCFA per kg in the tomato market. Calculate the new CS, PS and the deadweight loss.", steps=[
            S("Quantity traded (the short side)", math=r"Q_s = -300 + 6(120) = 420"),
            S("Demand price at Q = 420", math=r"P = 300 - \frac{420}{4} = 195"),
            S("New CS (trapezium)", math=r"\frac{(300 - 120) + (195 - 120)}{2} \times 420 = 53\,550"),
            S("New PS", math=r"\tfrac{1}{2} \times 420 \times (120 - 50) = 14\,700"),
            S("Deadweight loss", math=r"\tfrac{1}{2} \times (600 - 420) \times (195 - 120) = 6\,750"),
        ], check=r"75\,000 - (53\,550 + 14\,700) = 6\,750"),
        T("Consumers who still buy gain (CS rises from 45 000 to 53 550 FCFA, assuming the tomatoes go to the buyers who value them most), producers lose "
          "heavily, and 6 750 FCFA of welfare disappears because 180 kg that buyers valued above their cost are no longer produced."),
        H("Evaluation"),
        T("Surplus analysis is powerful but limited. It assumes the demand curve measures true benefit (not true if consumers are badly informed or for demerit goods), "
          "that 1 FCFA of surplus is worth the same to a poor and a rich person (it ignores equity), and that there are no external costs or benefits. "
          "It also assumes the rationed good goes to the buyers who value it most, which queues and black markets may prevent."),
        MISTAKE("Shading the wrong areas", "CS is between the demand curve and the price line; PS is between the price line and the supply curve. Neither is the rectangle P x Q (that is total revenue)."),
        MISTAKE("Using the equilibrium quantity after a price control", "With a maximum price the quantity traded is the smaller of Qd and Qs (here Qs = 420), not 600."),
        QUIZ("A good's price falls with no shift in demand. Consumer surplus",
             ["falls", "rises", "is unchanged", "becomes equal to producer surplus"], 1,
             "Existing buyers pay less and new buyers enter, so the area under demand and above price grows.",
             hint="What happens to the area between the demand curve and a lower price line?",
             feedback=["CS falls when price rises.", "", "The price line has moved, so the area changes.", "There is no reason for the two areas to be equal."]),
        QUIZ("In Figure 1, total economic welfare is",
             ["the CS triangle only", "the CS and PS triangles together", "the rectangle Pe x Qe", "the PS triangle only"], 1,
             "Total surplus is consumer surplus plus producer surplus.",
             hint="Welfare counts gains to both sides of the market.",
             feedback=["This leaves out producers.", "", "This rectangle is total spending (total revenue).", "This leaves out consumers."]),
        H("Practice"),
        PQ("Demand is $Q_d = 900 - 3P$ and supply is $Q_s = -100 + 2P$ (equilibrium P = 200, Q = 300). Calculate consumer and producer surplus.", "Demand intercept: P = 900/3 = 300. Supply intercept: P = 100/2 = 50. CS = 0.5 x 300 x (300 - 200) = 15 000. PS = 0.5 x 300 x (200 - 50) = 22 500."),
        PQ("Explain why a minimum price set above equilibrium creates a deadweight loss.", "The higher price reduces quantity demanded, and only that smaller quantity is bought. Units between the new quantity and the equilibrium quantity were valued by buyers above their cost of production but are no longer traded, so that surplus is lost to everyone."),
        PQ("Essay plan: Use the concepts of consumer and producer surplus to assess the effects of a maximum price on rice.", "Define CS and PS; draw equilibrium. Show maximum price below equilibrium: shortage, quantity traded falls to Qs. Effects: some consumers gain (lower price), consumers who cannot buy lose, producers lose PS, deadweight loss appears. Evaluate: equity gain for poor buyers if they get the rice; but queues, black markets and falling supply; alternatives such as subsidies or income support."),
        TIP("Exam link: surplus diagrams and triangle calculations appear in Paper 1 and Paper 3; Paper 2 essays on price controls, taxes and market failure use them to show welfare loss.", title="Exam link"),
        SUM("Consumer surplus: willingness to pay minus price paid; area under demand above price.",
            "Producer surplus: price received minus minimum acceptable price; area above supply below price.",
            "With linear curves, each surplus is a triangle: half x quantity x height.",
            "Total surplus is greatest at the competitive equilibrium; output away from it creates a deadweight loss.",
            "Surplus measures ignore equity, externalities and imperfect information."),
    ],
))

# ------------------------------------------------------------------ 8. Marginal utility theory
LESSONS.append(lesson(
    module=M2,
    topic="Marginal utility theory",
    title="Marginal utility, consumer equilibrium and the demand curve",
    slug="ecl1-marginal-utility",
    minutes=24,
    summary="Total and marginal utility, the law of diminishing marginal utility, consumer equilibrium with one good (MU = P) and with several goods (the equi-marginal principle), how this explains the downward-sloping demand curve, and the theory's limits.",
    objectives=[
        "Calculate marginal utility from total utility and state the law of diminishing marginal utility",
        "Find consumer equilibrium using MU = P and the equi-marginal principle",
        "Use marginal utility theory to derive a downward-sloping demand curve and explain the paradox of value",
        "Evaluate the assumptions of the cardinal utility approach",
    ],
    key_concepts=["Utility", "Total utility", "Marginal utility", "Diminishing marginal utility", "Equi-marginal principle",
                  "Consumer equilibrium", "Paradox of value", "Cardinal utility"],
    blocks=[
        H("Introduction"),
        T("On a hot afternoon in Garoua the first cold drink is wonderful, the second is good, the third is barely wanted. This everyday "
          "experience is the basis of **marginal utility theory**, the first of two A Level theories of consumer behaviour. It explains why "
          "people buy more of a good when its price falls, which is the law of demand."),
        D("**Utility** is the satisfaction a consumer gets from consuming a good or service. **Total utility (TU)** is the total satisfaction from "
          "all the units consumed. **Marginal utility (MU)** is the change in total utility from consuming one more unit.",
          title="Definitions: utility"),
        F(r"MU_n = TU_n - TU_{n-1}", title="Marginal utility"),
        D("The **law of diminishing marginal utility** states that, as a consumer consumes more units of a good in a given period, the extra "
          "satisfaction from each additional unit eventually falls, ceteris paribus.", title="The law of diminishing marginal utility"),
        CODE("""Units of bread   Total utility (utils)   Marginal utility (utils)
1                       20                        20
2                       36                        16
3                       48                        12
4                       56                         8
5                       60                         4
6                       62                         2""", "text", title="Table 1. A consumer's utility from bread rolls (invented for practice)"),
        T("Total utility keeps rising while MU is positive, reaches its maximum when MU = 0, and falls if MU becomes negative. MU is the slope of the TU curve."),
        KEY("Assumptions of the theory", "Examiners reward assumptions; state them.", cards=[
            ["Cardinal utility", "Utility can be measured in units (utils) or in money terms."],
            ["Rationality", "The consumer aims to maximise total utility with a given income."],
            ["Constant MU of money", "The utility of each franc stays the same, so money can measure utility."],
            ["Given tastes, income and prices", "These do not change during the analysis."],
        ]),
        H("Consumer equilibrium"),
        D("With one good, and utility measured in money, a consumer buys more units as long as the MU of the next unit is at least its price. "
          "Equilibrium is where **MU = P**.", title="Equilibrium with one good"),
        EX("Worked example 1: deriving demand from MU", intro="A consumer values successive plates of beans at 500, 400, 300, 200 and 100 FCFA (MU in money, invented for practice). How many plates does she buy at a price of 300 FCFA, and at 200 FCFA?", steps=[
            S("At 300 FCFA", text="Plates 1 to 3 have MU of at least 300 FCFA; plate 4 is worth only 200. She buys 3."),
            S("At 200 FCFA", text="Now plate 4 (MU = 200) is also worth buying. She buys 4."),
            S("Demand curve", text="A lower price leads to a larger quantity demanded. Because MU diminishes, the consumer buys more only if price falls: the demand curve slopes downward and is the MU curve measured in money."),
        ]),
        D("With several goods, a consumer maximises total utility when the marginal utility per franc is the same for every good and all income is spent: "
          "$\\frac{MU_A}{P_A} = \\frac{MU_B}{P_B}$ and $P_A Q_A + P_B Q_B = Y$. This is the **equi-marginal principle**.",
          title="The equi-marginal principle",
          formula=r"\frac{MU_A}{P_A} = \frac{MU_B}{P_B} = \cdots"),
        CODE("""Units   MU of bread (A)   MU of drinks (B)
1             20                60
2             16                48
3             12                36
4              8                24
5              4                12""", "text", title="Table 2. Marginal utilities (invented for practice)"),
        EX("Worked example 2: equilibrium with two goods", intro="Bread costs 100 FCFA and drinks cost 300 FCFA. Income is 1 200 FCFA. Using Table 2, find the utility-maximising combination.", steps=[
            S("MU per franc for A", text="20/100 = 0.20, 16/100 = 0.16, 12/100 = 0.12, 8/100 = 0.08 ..."),
            S("MU per franc for B", text="60/300 = 0.20, 48/300 = 0.16, 36/300 = 0.12, 24/300 = 0.08 ..."),
            S("Equal ratios that use all income", math=r"3 \times 100 + 3 \times 300 = 1\,200", text="At 3 bread and 3 drinks both ratios are 0.12."),
            S("Total utility", math=r"(20 + 16 + 12) + (60 + 48 + 36) = 192 \text{ utils}"),
            S("Why it is best", text="Moving 300 FCFA from one drink to 3 more bread would lose 36 utils and gain 8 + 4 + 2 = 14 utils. No other affordable combination gives more than 192."),
        ], check=r"\frac{12}{100} = \frac{36}{300} = 0.12"),
        T("If the price of bread falls, $MU_A/P_A$ rises above $MU_B/P_B$. The consumer buys more bread until the ratios are equal again, so a lower price "
          "raises quantity demanded. This is the second way the theory explains the downward-sloping demand curve."),
        H("The paradox of value"),
        T("Water is essential for life yet cheap; diamonds are not essential yet expensive. Adam Smith described this 'paradox of value'. Marginal utility "
          "resolves it: price reflects **marginal** utility, not total utility. Water is plentiful, so the MU of the last litre is low; diamonds are scarce, "
          "so the MU of the last one is high. The total utility of water is still far greater."),
        H("Evaluation"),
        KEY("Limits of marginal utility theory", "Use these in essays.", cards=[
            ["Measurement", "Utility cannot really be measured in units; satisfaction is personal and subjective (the cardinal assumption is weak)."],
            ["Constant MU of money", "The MU of money falls as income rises, so money is not a fixed measuring rod."],
            ["Indivisible goods", "Goods such as cars or houses cannot be bought in small units, so ratios cannot be equalised."],
            ["Behaviour", "Habit, impulse and limited information mean consumers do not calculate as the theory assumes."],
            ["Response", "Indifference curve analysis (next lessons) needs only ordinal utility: ranking, not measuring."],
        ]),
        MISTAKE("Saying total utility falls as soon as MU falls", "TU rises as long as MU is positive. Diminishing MU means TU rises more slowly."),
        MISTAKE("Equating MU, not MU per franc", "With different prices the condition is MU_A / P_A = MU_B / P_B. Equal MU would be correct only if the prices were equal."),
        QUIZ("Using Table 1, at which number of bread rolls is total utility maximised (assuming MU of the 7th roll is negative)?",
             ["3", "5", "6", "1"], 2,
             "TU rises while MU is positive: it is 62 at 6 rolls, and falls after that.",
             hint="TU is greatest just before MU turns negative.",
             feedback=["TU is still rising at 3 rolls.", "TU is still rising from 5 to 6 rolls (MU = 2).", "", "MU is highest at 1 roll, but TU is not."]),
        QUIZ("A consumer finds MU_A / P_A = 0.3 and MU_B / P_B = 0.1. To raise total utility she should",
             ["buy more A and less B", "buy more B and less A", "keep the same combination", "buy less of both"], 0,
             "A franc spent on A gives more utility than a franc on B, so switch spending to A until the ratios are equal.",
             hint="Which good gives more satisfaction per franc?",
             feedback=["", "This lowers total utility.", "The ratios are not equal, so she is not in equilibrium.", "Spending less in total leaves income unused and lowers utility."]),
        H("Practice"),
        PQ("Total utility from 1, 2, 3 and 4 oranges is 15, 27, 36 and 40 utils. Calculate marginal utility and state the law shown.", "MU = 15, 12, 9 and 4 utils. MU falls as more oranges are eaten: the law of diminishing marginal utility."),
        PQ("Explain the paradox of value using marginal utility.", "Price depends on the marginal utility of the last unit, not total utility. Water is abundant, so the last unit has low MU and a low price, even though total utility is huge. Diamonds are scarce, so their MU and price are high."),
        PQ("Essay plan: Explain how marginal utility theory derives a downward-sloping demand curve, and assess the theory.", "Define TU, MU, diminishing MU; state assumptions. Single good: buy until MU = P; lower price means more units have MU >= P. Several goods: equi-marginal principle; a price fall raises MU/P, consumer buys more. Assess: cardinal measurement unrealistic, MU of money not constant, indivisibility, habits; but gives clear insight and solves the paradox of value; indifference analysis is the ordinal alternative."),
        TIP("Exam link: MU calculations and the equi-marginal condition appear in Paper 1; Paper 2 asks you to explain the demand curve using utility or to compare it with indifference analysis.", title="Exam link"),
        SUM("Marginal utility is the change in total utility from one more unit; it diminishes as consumption rises.",
            "One good: buy until MU = P. Several goods: MU_A / P_A = MU_B / P_B with all income spent.",
            "Because MU diminishes, quantity demanded rises only when price falls: the demand curve slopes down.",
            "Price reflects marginal, not total, utility: this resolves the paradox of value.",
            "The theory relies on measurable (cardinal) utility and a constant MU of money, which are weak assumptions."),
    ],
))

# ------------------------------------------------------------------ 9. Indifference curve analysis
LESSONS.append(lesson(
    module=M2,
    topic="Indifference curve analysis",
    title="Indifference curves, budget lines and consumer equilibrium",
    slug="ecl1-indifference-curves",
    minutes=25,
    summary="The ordinal approach to consumer choice: indifference curves and their properties, the marginal rate of substitution, the budget line and how it shifts or pivots, and consumer equilibrium where an indifference curve is tangent to the budget line.",
    objectives=[
        "Define an indifference curve and explain its four properties",
        "Calculate the marginal rate of substitution and explain why it diminishes",
        "Draw and calculate a budget line and show the effect of changes in income and prices",
        "Explain consumer equilibrium where MRS equals the price ratio",
    ],
    key_concepts=["Ordinal utility", "Indifference curve", "Indifference map", "Marginal rate of substitution",
                  "Budget line", "Consumer equilibrium", "Price ratio"],
    blocks=[
        H("Introduction"),
        T("Marginal utility theory needed satisfaction to be measured in utils. Most economists now prefer an approach that only asks consumers to "
          "**rank** bundles of goods: 'I prefer this to that' or 'I like them equally'. This is the **ordinal** approach, developed by economists "
          "including Francis Edgeworth and, later, John Hicks. It uses two tools: indifference curves (what the consumer wants) and the budget line (what she can afford)."),
        D("**Ordinal utility** means consumers can rank combinations of goods in order of preference without measuring satisfaction in units. "
          "**Cardinal utility** (used in marginal utility theory) assumes satisfaction can be measured.", title="Definitions: ordinal and cardinal utility"),
        D("An **indifference curve** joins all combinations (bundles) of two goods that give a consumer the same level of satisfaction, so she is "
          "indifferent between them. A set of indifference curves for one consumer is an **indifference map**.", title="Definition: indifference curve"),
        KEY("Assumptions", "State them before using the model.", cards=[
            ["Rationality", "The consumer aims to reach the highest possible indifference curve."],
            ["Completeness and consistency", "She can rank any two bundles, and her rankings are transitive (if A > B and B > C, then A > C)."],
            ["Non-satiation", "More of a good is preferred to less."],
            ["Diminishing MRS", "The more of X she has, the less Y she will give up for another unit of X."],
        ]),
        KEY("Properties of indifference curves", "Each property follows from an assumption.", cards=[
            ["Slope downward", "To keep satisfaction constant, more X must be balanced by less Y (non-satiation)."],
            ["Convex to the origin", "The MRS diminishes along the curve."],
            ["Never intersect", "If they crossed, one bundle would give two levels of satisfaction, breaking consistency."],
            ["Higher is better", "A curve further from the origin has more of at least one good, so it gives more satisfaction."],
        ]),
        H("The marginal rate of substitution"),
        D("The **marginal rate of substitution of X for Y** (MRS) is the amount of Y a consumer is willing to give up to gain one more unit of X while "
          "remaining on the same indifference curve. It is the (absolute) slope of the indifference curve and equals $MU_X / MU_Y$.",
          title="Definition: MRS", formula=r"MRS_{XY} = -\frac{\Delta Y}{\Delta X} = \frac{MU_X}{MU_Y}"),
        CODE("""Bundle   Good X   Good Y   Y given up   MRS (per unit of X)
P           2       20         -            -
Q           4       12         8            4
R           6        8         4            2
S           8        6         2            1
T          10        5         1            0.5""", "text", title="Table 1. Bundles on one indifference curve (invented for practice)"),
        EX("Worked example 1: diminishing MRS", intro="Using Table 1, calculate the MRS between P and Q and between S and T, and explain the pattern.", steps=[
            S("P to Q", math=r"MRS = \frac{20 - 12}{4 - 2} = 4"),
            S("S to T", math=r"MRS = \frac{6 - 5}{10 - 8} = 0.5"),
            S("Pattern", text="The MRS falls from 4 to 0.5. When the consumer has little X and much Y, she values X highly and will give up a lot of Y; as X becomes plentiful she gives up less. This makes the curve convex."),
        ]),
        H("The budget line"),
        D("A **budget line** shows all combinations of two goods a consumer can just afford with a given money income and given prices. Its equation is "
          "$P_X X + P_Y Y = M$. The intercepts are $M / P_X$ and $M / P_Y$ and the slope is $-P_X / P_Y$.",
          title="Definition: budget line", formula=r"P_X X + P_Y Y = M"),
        EX("Worked example 2: drawing a budget line", intro="Income is 6 000 FCFA, X costs 300 FCFA and Y costs 500 FCFA (invented for practice). Find the intercepts and slope.", steps=[
            S("All income on X", math=r"\frac{6\,000}{300} = 20 \text{ units}"),
            S("All income on Y", math=r"\frac{6\,000}{500} = 12 \text{ units}"),
            S("Slope", math=r"-\frac{P_X}{P_Y} = -\frac{300}{500} = -0.6"),
            S("Meaning", text="Each extra unit of X costs 0.6 units of Y: the market rate of exchange."),
        ], check=r"300(10) + 500(6) = 6\,000"),
        KEY("Changes in the budget line", "Shifts and pivots.", cards=[
            ["Income rises", "Parallel shift outward (slope unchanged). With income 9 000 FCFA the intercepts become 30 and 18."],
            ["Price of X falls", "The line pivots outward on the Y intercept. If X falls to 200 FCFA, the X intercept becomes 30; the Y intercept stays at 12."],
            ["Both prices double", "Same as halving income: a parallel inward shift."],
        ]),
        H("Consumer equilibrium"),
        IMG("alecl1-ic-budget.svg", alt="Three convex indifference curves IC1, IC2 and IC3 and a straight budget line from 12 on the Y axis to 20 on the X axis. The budget line cuts IC1 at A and B and touches IC2 at E, where X = 10 and Y = 6. IC3 lies beyond the budget line.",
            caption="Figure 1. Consumer equilibrium at E, where the budget line is tangent to IC2."),
        D("The consumer is in equilibrium at the point where the budget line is **tangent** to the highest attainable indifference curve. There the slope of the "
          "indifference curve equals the slope of the budget line: $MRS = P_X / P_Y$, which also gives $MU_X / P_X = MU_Y / P_Y$.",
          title="Equilibrium condition", formula=r"MRS_{XY} = \frac{P_X}{P_Y}"),
        EX("Worked example 3: reading the equilibrium", intro="Use Figure 1 to explain why E is chosen rather than A, B or a point on IC3.", steps=[
            S("A and B", text="Both are affordable (on the budget line) but lie on IC1, a lower level of satisfaction than IC2."),
            S("IC3", text="Every point on IC3 lies outside the budget line, so it cannot be afforded."),
            S("E", text="E is affordable and on the highest attainable curve, IC2. Here MRS = 0.6 = 300/500: the rate at which she is willing to swap equals the rate at which the market lets her swap."),
            S("At A", text="The IC is steeper than the budget line (MRS > 0.6): she values X more than its market cost, so she buys more X and moves towards E."),
        ]),
        MISTAKE("Drawing indifference curves that cross or are concave", "Curves must be convex and must never touch each other. Label the axes with the two goods and each curve IC1, IC2, ..."),
        MISTAKE("Mixing up MRS and the price ratio", "MRS is the slope of the indifference curve (the consumer's willingness); Px/Py is the slope of the budget line (the market). Equilibrium is where they are equal."),
        QUIZ("Income is 4 000 FCFA, X costs 200 FCFA and Y costs 400 FCFA. What is the slope of the budget line (Y on the vertical axis)?",
             ["-2", "-0.5", "-20", "-10"], 1,
             "Slope = -Px/Py = -200/400 = -0.5.",
             hint="Divide the price of the good on the horizontal axis by the price of the other good.",
             feedback=["This is -Py/Px, the wrong way round.", "", "20 is the X intercept, not the slope.", "10 is the Y intercept, not the slope."]),
        QUIZ("Why can two indifference curves of the same consumer never intersect?",
             ["Because prices are fixed", "Because the crossing point would have to give two different levels of satisfaction",
              "Because income is limited", "Because MRS is constant"], 1,
             "Each curve is one level of satisfaction; a shared point would make the rankings inconsistent.",
             hint="What does each curve represent?",
             feedback=["Prices affect the budget line, not indifference curves.", "", "Income affects the budget line.", "MRS diminishes; in any case it is not the reason."]),
        H("Practice"),
        PQ("Income is 9 000 FCFA, X costs 300 FCFA and Y costs 500 FCFA. Find the intercepts of the budget line and compare it with the line for 6 000 FCFA.", "X intercept = 9 000/300 = 30; Y intercept = 9 000/500 = 18. The slope is still -0.6, so the new line is a parallel outward shift of the 6 000 FCFA line (intercepts 20 and 12)."),
        PQ("Explain why an indifference curve is convex to the origin.", "Convexity reflects a diminishing marginal rate of substitution. When a consumer has a lot of Y and little X, she will give up much Y for one more X; as she gets more X and less Y, each extra X is worth less to her relative to Y, so she gives up less Y. The curve becomes flatter as X increases."),
        PQ("Essay plan: Using indifference curves and a budget line, explain how a consumer reaches equilibrium.", "Define indifference curve and budget line; state assumptions. Properties of ICs. Budget line equation and slope. Diagram: highest IC touching budget line at E. Condition MRS = Px/Py, equivalently MU_X/P_X = MU_Y/P_Y. Explain why points on lower ICs (A, B) or higher ICs are not chosen. Evaluate: needs only ranking (ordinal), more realistic than cardinal utility, but assumes rationality, perfect information and divisible goods."),
        TIP("Exam link: indifference curve diagrams appear in Paper 1 (slopes, intercepts, properties) and in Paper 2 essays, usually leading into income and substitution effects.", title="Exam link"),
        SUM("Indifference curves join bundles of equal satisfaction; they slope down, are convex, never cross, and higher is better.",
            "MRS = amount of Y given up for one more X on the same curve = MU_X / MU_Y; it diminishes.",
            "Budget line: Px X + Py Y = M, intercepts M/Px and M/Py, slope -Px/Py.",
            "Income changes shift the budget line parallel; a price change pivots it.",
            "Equilibrium: budget line tangent to the highest attainable indifference curve, MRS = Px/Py."),
    ],
))

# ------------------------------------------------------------------ 10. Income and substitution effects
LESSONS.append(lesson(
    module=M2,
    topic="Income and substitution effects",
    title="Income and substitution effects for normal, inferior and Giffen goods",
    slug="ecl1-income-substitution-effects",
    minutes=25,
    summary="Split the effect of a price change into a substitution effect and an income effect with indifference curves, show why demand curves for normal goods slope downward, and explain inferior and Giffen goods.",
    objectives=[
        "Define the substitution effect and the income effect of a price change",
        "Separate the two effects on an indifference curve diagram using a compensated budget line",
        "Explain the slope of the demand curve for normal, inferior and Giffen goods",
        "Evaluate the importance of Giffen goods in practice",
    ],
    key_concepts=["Substitution effect", "Income effect", "Real income", "Compensated budget line", "Normal good",
                  "Inferior good", "Giffen good", "Price-consumption curve"],
    blocks=[
        H("Introduction"),
        T("When the price of rice falls in Bamenda, households buy more rice for two reasons. Rice is now cheaper **compared with** other foods such as "
          "plantain, so they switch towards it. And with the same money income they can now afford more of everything: their **real income** has risen. "
          "Economists separate these two forces because they explain why most demand curves slope down, and why a few might not."),
        D("The **substitution effect** of a price change is the change in quantity demanded caused only by the change in **relative prices**, with real "
          "income (satisfaction) held constant. The **income effect** is the change in quantity demanded caused only by the change in **real income** "
          "(purchasing power) that the price change brings about.", title="Definitions"),
        D("**Real income** is the quantity of goods and services that a money income can buy. A fall in the price of a good raises real income even "
          "though money income is unchanged.", title="Definition: real income"),
        KEY("Direction of each effect after a price fall", "Learn this table of signs.", cards=[
            ["Substitution effect", "Always raises quantity demanded of the good whose price falls because it is now relatively cheaper. After a price rise it always lowers quantity demanded."],
            ["Income effect, normal good", "Higher real income raises quantity demanded: it reinforces the substitution effect."],
            ["Income effect, inferior good", "Higher real income lowers quantity demanded: it works against the substitution effect."],
        ]),
        H("Separating the effects (Hicks method)"),
        IMG("alecl1-inc-sub.svg", alt="Budget line BL1 touches IC1 at E1. After the price of X falls, budget line BL2 pivots out and touches IC2 at E3. A dashed compensated line CL parallel to BL2 touches IC1 at E2. Quantities X1, X2 and X3 are marked on the X axis.",
            caption="Figure 1. A fall in the price of X for a normal good. X1 to X2 is the substitution effect; X2 to X3 is the income effect."),
        EX("Worked example 1: the steps on the diagram", intro="The price of X falls. Explain how Figure 1 separates the two effects.", steps=[
            S("Start", text="With budget line BL1 the consumer is at E1 on IC1, buying X1."),
            S("Price falls", text="The budget line pivots outward on the Y intercept to BL2. The new equilibrium is E3 on IC2, buying X3. The total effect is X1 to X3."),
            S("Remove the real income gain", text="Draw a compensated budget line CL parallel to BL2 (new relative prices) but tangent to the original IC1 (original real income). It touches IC1 at E2."),
            S("Substitution effect", text="E1 to E2 (X1 to X2): a movement along the same indifference curve caused only by the change in relative prices."),
            S("Income effect", text="E2 to E3 (X2 to X3): a parallel shift from CL to BL2, caused only by the rise in real income."),
        ]),
        EX("Worked example 2: putting numbers on it", intro="In Figure 1 (invented for practice) income is 6 000 FCFA, Y costs 500 FCFA and the price of X falls from 300 to 200 FCFA. The consumer's choices are X1 = 10, X2 = 12.2 (about) and X3 = 15 units. Find the effects.", steps=[
            S("Total effect", math=r"15 - 10 = +5 \text{ units}"),
            S("Substitution effect", math=r"12.2 - 10 \approx +2.2 \text{ units}"),
            S("Income effect", math=r"15 - 12.2 \approx +2.8 \text{ units}"),
            S("Interpret", text="Both effects are positive: X is a normal good. Price fell from 300 to 200 FCFA and quantity rose from 10 to 15, so these are two points on a downward-sloping demand curve."),
        ], check=r"2.2 + 2.8 = 5"),
        H("Normal, inferior and Giffen goods"),
        KEY("Three cases after a price fall", "Compare the size and direction of the two effects.", cards=[
            ["Normal good", "SE raises Qd and IE raises Qd. Total effect: Qd rises. Demand curve slopes downward."],
            ["Inferior good (not Giffen)", "SE raises Qd, IE lowers Qd, but SE is larger. Total effect: Qd still rises. Demand curve slopes downward, but is less elastic."],
            ["Giffen good", "SE raises Qd, IE lowers Qd and IE is larger. Total effect: Qd falls when price falls. Demand curve slopes upward."],
        ]),
        D("A **Giffen good** is a strongly inferior good, taking a large share of a poor household's budget, for which the income effect of a price change "
          "outweighs the substitution effect, so quantity demanded rises when price rises. It is named after Robert Giffen.", title="Definition: Giffen good"),
        EX("Worked example 3: a Giffen-type staple", intro="A very poor household spends most of its income on a cheap staple and buys a little meat. Explain why a rise in the staple's price could lead it to buy more of the staple.", steps=[
            S("Substitution effect", text="The staple is relatively dearer, so the household would like to buy a little less of it."),
            S("Income effect", text="Because the staple is a large share of spending, the price rise cuts real income sharply. The household can no longer afford meat."),
            S("Inferior good", text="With lower real income it replaces meat with more of the cheap staple: the income effect raises demand for the staple."),
            S("Result", text="If this income effect is larger than the substitution effect, quantity demanded rises with price: Giffen behaviour."),
        ]),
        T("Evaluation: Giffen goods are rare. The conditions are strict (strongly inferior, a large share of the budget, few substitutes), and the often-quoted "
          "historical examples are disputed; some recent studies report Giffen behaviour for staple foods among very poor households. Check your textbook for the "
          "examples it uses. Do not confuse Giffen goods with **ostentatious (Veblen) goods**, which are bought more at higher prices because the price itself "
          "signals status; that is not an income effect."),
        TIP("Textbooks use two ways of removing the income effect. The Hicks method (used here) keeps the consumer on the original indifference curve. The "
            "Slutsky method keeps the original bundle just affordable. The direction of the effects is the same. Check which your textbook uses."),
        MISTAKE("Describing the income effect as a change in money income", "Money income does not change. The price change alters real income (purchasing power). The Board reports that candidates lost marks for this."),
        MISTAKE("Explaining the demand curve with shifts of demand", "The question 'explain the shape of a normal demand curve using income and substitution effects' is about a movement along the curve after a price change, not shifts of the curve."),
        QUIZ("The price of a normal good falls. Which is correct?",
             ["The substitution effect raises Qd and the income effect lowers it", "Both effects raise Qd",
              "Both effects lower Qd", "The income effect raises Qd and the substitution effect lowers it"], 1,
             "For a normal good both effects work in the same direction after a price fall.",
             hint="Higher real income and a lower relative price: what does each do for a normal good?",
             feedback=["That is the pattern for an inferior good.", "", "A price fall never makes the substitution effect lower Qd.", "The substitution effect always raises Qd after a price fall."]),
        QUIZ("For a Giffen good, a fall in price leads to",
             ["a rise in quantity demanded because the substitution effect dominates", "a fall in quantity demanded because the income effect is opposite and larger",
              "no change in quantity demanded", "a rise in quantity demanded because the good is normal"], 1,
             "The negative income effect outweighs the positive substitution effect.",
             hint="Which effect is bigger for a Giffen good?",
             feedback=["That describes an ordinary inferior good.", "", "The two effects are unequal, so Qd changes.", "Giffen goods are inferior goods."]),
        H("Practice"),
        PQ("Distinguish between the income effect and the substitution effect of a price change.", "The substitution effect is the change in quantity demanded due to the change in relative prices, holding real income constant, whereas the income effect is the change in quantity demanded due to the change in real income caused by the price change."),
        PQ("Explain why the demand curve for an inferior (non-Giffen) good still slopes downward.", "After a price fall, the substitution effect raises quantity demanded. The income effect lowers it, because the good is inferior, but it is smaller than the substitution effect. The net effect is still a rise in quantity demanded, so the demand curve slopes down."),
        PQ("Essay plan: (a) State how a normal demand curve slopes and illustrate it. (b) Explain its shape using the income and substitution effects.", "(a) Downward from left to right: a lower price gives a larger quantity demanded; draw and label P and Q axes. (b) Define both effects and real income. Indifference diagram: price fall pivots budget line; compensated line separates E1 to E2 (substitution, along IC1) and E2 to E3 (income, to IC2). For a normal good both raise Qd, so the demand curve slopes down. Mention the inferior and Giffen cases as contrasts."),
        PQ("Using Figure 1, explain the role of the compensated budget line CL.", "CL has the new price ratio (parallel to BL2) but is tangent to the original indifference curve IC1, so it removes the gain in real income. The move along IC1 from E1 to E2 then shows the pure substitution effect, and the parallel shift from CL to BL2 shows the income effect."),
        TIP("Exam link: this is a regular Paper 2 essay topic and appears in Paper 1 as diagram questions. The Board has noted that candidates struggle to explain the normal demand curve with these effects: practise the diagram until you can draw it quickly.", title="Exam link"),
        SUM("Substitution effect: response to a change in relative prices at constant real income; after a price fall it always raises Qd.",
            "Income effect: response to the change in real income; positive for normal goods, negative for inferior goods.",
            "A compensated budget line parallel to the new budget line and tangent to the old indifference curve separates the effects.",
            "Normal and ordinary inferior goods have downward-sloping demand curves.",
            "Giffen goods: the negative income effect outweighs the substitution effect, so demand slopes upward; such goods are rare."),
    ],
))

# ------------------------------------------------------------------ 11. Short-run production and diminishing returns
LESSONS.append(lesson(
    module=M3,
    topic="Short-run production and diminishing returns",
    title="Total, average and marginal product and the law of diminishing returns",
    slug="ecl1-short-run-production",
    minutes=23,
    summary="In the short run at least one factor is fixed. Calculate total, average and marginal product, explain the law of diminishing returns, the relationship between AP and MP, and the stages of production.",
    objectives=[
        "Distinguish the short run from the long run and fixed from variable factors",
        "Calculate TP, AP and MP from a table and draw the three curves",
        "State and explain the law of diminishing returns and the MP-AP relationship",
        "Identify the stages of production and explain why a firm operates in stage II",
    ],
    key_concepts=["Short run", "Long run", "Fixed factor", "Total product", "Average product", "Marginal product",
                  "Law of diminishing returns", "Stages of production"],
    blocks=[
        H("Introduction"),
        T("A farmer in the Western Highlands has one hectare of land. Adding the first worker brings a big gain; the tenth worker, "
          "sharing the same land and tools, adds very little. This everyday pattern is the law of diminishing returns, the basis of "
          "the shape of a firm's cost curves."),
        D("The **short run** is the period in which at least one factor of production (such as land or machinery) is fixed, so output can change "
          "only by changing the variable factors (such as labour). The **long run** is the period in which all factors can be varied.",
          title="Definitions: short run and long run"),
        D("**Total product (TP)** is the total output. **Average product (AP)** is output per unit of the variable factor. **Marginal product (MP)** is the "
          "extra output from one more unit of the variable factor.", title="Definitions: TP, AP and MP",
          formula=r"AP = \frac{TP}{L}, \qquad MP = \frac{\Delta TP}{\Delta L}"),
        CODE("""Workers   TP    AP     MP
0          0     -      -
1         10    10     10
2         30    15     20
3         60    20     30
4         80    20     20
5         90    18     10
6         96    16      6
7         98    14      2
8         96    12     -2""", "text", title="Table 1. One hectare of farm land with extra workers (kg of maize, invented for practice)"),
        IMG("alecl1-production.svg", alt="Top panel: total product rises steeply then more slowly and turns down after seven workers. Bottom panel: marginal product rises to a peak at the third worker then falls, cutting average product at its maximum and reaching zero at seven workers. Dashed lines mark three stages.",
            caption="Figure 1. TP, AP and MP from Table 1 (curves smoothed)."),
        H("The law of diminishing returns"),
        D("The **law of diminishing (marginal) returns** states that, in the short run, as more units of a variable factor are added to a fixed factor, "
          "the marginal product of the variable factor eventually falls. It holds if technology is unchanged and the units of the variable factor are equal in quality.",
          title="The law of diminishing returns"),
        T("In Table 1, MP rises up to the third worker (increasing returns: workers specialise and use the land better) and falls from the fourth. "
          "Diminishing returns set in after the third worker. The fixed land and tools become crowded. This is a law about **marginal** product; TP still rises until MP turns negative."),
        KEY("The MP and AP relationship", "A favourite exam point: it is the same as any marginal-average rule.", cards=[
            ["MP above AP", "AP is rising (a new worker above the average pulls it up)."],
            ["MP below AP", "AP is falling."],
            ["MP = AP", "AP is at its maximum: MP cuts AP from above at its peak (workers 3 and 4 in Table 1)."],
            ["MP and TP", "TP rises fastest where MP is highest; TP is maximum where MP = 0 (7 workers); TP falls when MP is negative."],
        ]),
        EX("Worked example 1: completing a table", intro="A bakery's output (loaves) with 1, 2, 3 and 4 bakers and one oven is 20, 60, 90 and 100. Calculate AP and MP and state where diminishing returns begin (invented for practice).", steps=[
            S("MP", math=r"20,\; 40,\; 30,\; 10"),
            S("AP", math=r"\frac{20}{1}=20,\; \frac{60}{2}=30,\; \frac{90}{3}=30,\; \frac{100}{4}=25"),
            S("Diminishing returns", text="MP is highest for the second baker (40) and falls from the third: diminishing returns begin after the second baker."),
            S("Check the rule", text="At 3 bakers MP (30) equals AP (30): AP is at its maximum."),
        ]),
        H("Stages of production"),
        KEY("Three stages (Figure 1)", "The stages are shown by the dashed lines.", cards=[
            ["Stage I", "From zero to where AP is maximum. The fixed factor is under-used. A firm adds workers."],
            ["Stage II", "From maximum AP to MP = 0. AP and MP are falling but TP still rises. The sensible range for a firm."],
            ["Stage III", "MP negative, TP falls. No firm would hire workers whose output reduces the total."],
        ]),
        EX("Worked example 2: why stage II?", intro="Explain why a profit-seeking firm in Table 1 would not use 8 workers, and why it may not stop at 3.", steps=[
            S("8 workers", text="MP is -2: the eighth worker reduces total output while still being paid. The firm loses."),
            S("Stop at 3?", text="At 3 workers AP is highest but MP (30) is still positive: more output could be obtained. If the extra output is worth more than the wage, hire more."),
            S("Decision", text="The exact number depends on wage and price: hire while the value of MP is at least the wage. This idea is developed in the factor-demand lessons."),
        ]),
        T("Diminishing returns is not the same as returns to scale. It is a short-run law about adding one factor to fixed others, whereas returns to scale (next lesson) is a long-run "
          "idea about increasing all factors together. Diminishing returns explains why marginal cost eventually rises."),
        MISTAKE("Saying 'total product falls when diminishing returns start'", "Diminishing returns means marginal product falls. TP keeps rising until MP is zero."),
        MISTAKE("Mixing diminishing returns with diseconomies of scale", "The first is short run with a fixed factor; the second is a long-run rise in average cost when the firm gets too big."),
        QUIZ("From Table 1, between which numbers of workers does diminishing marginal returns begin?",
             ["0 and 1", "2 and 3", "3 and 4", "7 and 8"], 2,
             "MP peaks at the third worker (30) and falls at the fourth (20).",
             hint="Find the largest MP, then the next worker.",
             feedback=["MP is still rising at the first worker.", "MP is still rising at the third worker (30).", "", "MP turns negative there, but diminishing returns began earlier."]),
        QUIZ("When marginal product is above average product,",
             ["average product is falling", "average product is rising", "total product is falling", "average product is at its maximum"], 1,
             "A marginal figure above the average pulls the average up.",
             hint="Think of a new student scoring above the class average.",
             feedback=["AP falls when MP is below it.", "", "TP rises whenever MP is positive.", "AP is maximum when MP equals AP."]),
        H("Practice"),
        PQ("A farm's output with 1, 2, 3 and 4 workers is 15, 40, 60 and 70 kg. Calculate MP and AP for each and identify when diminishing returns set in.", "MP: 15, 25, 20, 10. AP: 15, 20, 20, 17.5. MP peaks at the second worker, so diminishing returns set in at the third worker."),
        PQ("Explain why the law of diminishing returns operates in the short run only.", "It requires at least one fixed factor. In the long run all factors can be increased together, so there is no fixed factor that makes extra workers crowd it."),
        PQ("Essay plan: Explain the law of diminishing returns and its importance to a farmer in Cameroon.", "Define short run and fixed factor; state the law with its conditions (technology unchanged, equal units). Use a table of TP, AP, MP and a diagram with MP cutting AP. Importance: a small farm with fixed land should stop adding labour where MP falls to the wage level; explains rising marginal cost and the upward-sloping short-run supply curve; helps decide to invest in more land, fertiliser or tools in the long run. Evaluation: technology change can shift the curves up."),
        TIP("Exam link: diminishing returns and TP-AP-MP calculations are tested in Paper 1 and Paper 3 data tasks; Paper 2 essays often link the law to cost curves.", title="Exam link"),
        SUM("Short run: at least one fixed factor. Long run: all factors variable.",
            "AP = TP / L and MP = change in TP / change in L.",
            "The law of diminishing returns: MP eventually falls as a variable factor is added to a fixed factor.",
            "MP cuts AP at AP's maximum; TP is maximum when MP = 0.",
            "Firms operate in stage II, where MP is positive and falling."),
    ],
))

# ------------------------------------------------------------------ 12. Returns to scale, isoquants and isocosts
LESSONS.append(lesson(
    module=M3,
    topic="Returns to scale, isoquants and isocosts",
    title="Returns to scale, isoquants and isocosts: the least-cost combination of inputs",
    slug="ecl1-returns-isoquants-isocosts",
    minutes=24,
    summary="Long-run production: increasing, constant and decreasing returns to scale; isoquants and the marginal rate of technical substitution; isocost lines; and the least-cost combination of capital and labour where the isocost is tangent to the isoquant.",
    objectives=[
        "Calculate and classify returns to scale from changes in inputs and output",
        "Define an isoquant and explain its shape and the MRTS",
        "Draw an isocost line and calculate its intercepts and slope",
        "Find the least-cost combination of inputs where MRTS equals the input price ratio",
    ],
    key_concepts=["Returns to scale", "Isoquant", "Marginal rate of technical substitution", "Isocost line",
                  "Least-cost combination", "Expansion path"],
    blocks=[
        H("Introduction"),
        T("A cement factory in Douala can double its machines and workers. Will output exactly double, more than double, or less than double? "
          "That is the question of **returns to scale**. And with machines costing more than labour, how many of each should it use to make a "
          "given output at the lowest cost? The tools are isoquants and isocosts."),
        D("**Returns to scale** describe how output changes when **all** inputs are increased in the same proportion in the long run. There are "
          "**increasing** (output rises by a bigger proportion), **constant** (same proportion) and **decreasing** returns to scale (smaller proportion).",
          title="Definition: returns to scale"),
        CODE("""Firm   Inputs doubled   Output before   Output after   % rise in output   Returns to scale
A      yes                 100            200               100%        constant
B      yes                 100            250               150%        increasing
C      yes                 100            160                60%        decreasing""", "text", title="Table 1. Doubling all inputs (invented for practice)"),
        T("Doubling inputs is a 100% rise. Firm B's output rises by 150%, so returns are increasing. Firm C's rises by 60%, so returns are decreasing. "
          "Do not confuse this with diminishing returns, which concerns adding one input to others held fixed."),
        KEY("Why returns to scale differ", "Link to the next lesson.", cards=[
            ["Increasing", "Specialisation, bigger and more efficient machines, spreading of fixed overheads."],
            ["Constant", "The firm can replicate its production unit exactly."],
            ["Decreasing", "Management and co-ordination problems in very large firms."],
        ]),
        H("Isoquants"),
        D("An **isoquant** is a curve showing all the combinations of two inputs (usually capital K and labour L) that produce the same level of output. A set "
          "of isoquants is an **isoquant map**; a higher isoquant means more output.", title="Definition: isoquant"),
        D("The **marginal rate of technical substitution (MRTS)** is the amount of capital that can be given up when one more unit of labour is used, "
          "keeping output constant. It is the absolute slope of the isoquant and equals $MP_L / MP_K$.",
          title="Definition: MRTS", formula=r"MRTS_{LK} = -\frac{\Delta K}{\Delta L} = \frac{MP_L}{MP_K}"),
        KEY("Properties of isoquants", "They resemble indifference curves, but output is measurable.", cards=[
            ["Downward sloping", "More labour must replace capital to keep output constant."],
            ["Convex to the origin", "MRTS diminishes: inputs are imperfect substitutes."],
            ["Do not intersect", "A crossing point would give two output levels."],
            ["Higher means more output", "A cardinal difference: isoquants are labelled with quantities, e.g. Q = 10."],
        ]),
        CODE("""Capital K   Labour L   K x L (output Q = square root of K x L)
20            5          100   (Q = 10)
10           10          100   (Q = 10)
 5           20          100   (Q = 10)
 4           25          100   (Q = 10)""", "text", title="Table 2. Combinations producing 10 units (invented for practice)"),
        H("Isocost lines"),
        D("An **isocost line** shows all the combinations of capital and labour that cost the same total amount at given input prices. For a total outlay C, "
          "wage w and price of capital r, $wL + rK = C$. Its intercepts are $C/w$ and $C/r$ and its slope is $-w/r$.",
          title="Definition: isocost line", formula=r"wL + rK = C"),
        EX("Worked example 1: an isocost line", intro="Labour costs 50 000 FCFA per worker per month, capital costs 200 000 FCFA per machine per month and the firm spends 2 000 000 FCFA (invented for practice). Find the intercepts and slope.", steps=[
            S("All on labour", math=r"\frac{2\,000\,000}{50\,000} = 40 \text{ workers}"),
            S("All on capital", math=r"\frac{2\,000\,000}{200\,000} = 10 \text{ machines}"),
            S("Slope", math=r"-\frac{w}{r} = -\frac{50\,000}{200\,000} = -0.25"),
        ], check=r"50(20) + 200(5) = 2\,000"),
        H("The least-cost combination"),
        IMG("alecl1-isoquant.svg", alt="Convex isoquant Q = 10 and a higher isoquant Q = 14.1, with a straight isocost line from 10 machines on the vertical axis to 40 workers on the horizontal axis. The isocost touches Q = 10 at E, 20 workers and 5 machines.",
            caption="Figure 1. Producing 10 units at least cost: tangency at E."),
        D("A firm produces a given output at least cost where the isocost line is **tangent** to the isoquant: the slopes are equal, so "
          "$MRTS = w/r$, or $\\frac{MP_L}{w} = \\frac{MP_K}{r}$. The last franc spent on each input adds the same output.",
          title="Least-cost condition", formula=r"\frac{MP_L}{w} = \frac{MP_K}{r}"),
        EX("Worked example 2: comparing combinations", intro="Using Table 2 and the prices in Worked example 1 (w = 50, r = 200 thousand FCFA), find the cheapest way to produce 10 units.", steps=[
            S("Cost of each combination", math=r"(20K, 5L): 4\,250;\; (10, 10): 2\,500;\; (5, 20): 2\,000;\; (4, 25): 2\,050", text="Costs in thousand FCFA, from 50L + 200K."),
            S("Cheapest", text="5 machines and 20 workers cost 2 000 thousand FCFA, the lowest."),
            S("Tangency", text="At (K = 5, L = 20) the isoquant slope is -K/L = -0.25, equal to the isocost slope -w/r = -0.25."),
        ], check=r"50 \times 20 + 200 \times 5 = 2\,000"),
        T("If the price of labour **rises** the isocost line becomes steeper (the labour intercept falls while the capital intercept is unchanged). The firm substitutes capital for labour. "
          "This is why wage rises can push firms towards machines. If output is to rise, the firm moves to higher isoquants and the line joining the tangency points is the **expansion path**."),
        MISTAKE("Saying 'increasing returns to scale' when one input is increased", "Returns to scale require ALL inputs to rise in the same proportion. One input at a time gives diminishing returns."),
        MISTAKE("Reading the isocost as the budget line of a consumer", "It has the same shape, but it is a firm's total cost line: the firm minimises cost for a given output, whereas the consumer maximises utility for a given income."),
        QUIZ("A firm doubles all its inputs and output rises by 80%. Returns to scale are",
             ["increasing", "constant", "decreasing", "diminishing marginal"], 2,
             "Inputs rose by 100% but output by only 80%: decreasing returns to scale.",
             hint="Compare the percentage rise in output with the percentage rise in inputs.",
             feedback=["Increasing would need output up by more than 100%.", "Constant would need exactly 100%.", "", "Diminishing marginal returns is a short-run idea."]),
        QUIZ("At the least-cost combination the slope of the isoquant equals",
             ["the slope of the isocost line", "zero", "the output level", "-1"], 0,
             "Tangency: MRTS = w/r.",
             hint="What does tangent mean?",
             feedback=["", "Isoquants are not flat at tangency.", "Slope and output are different things.", "The slope depends on input prices."]),
        H("Practice"),
        PQ("A firm increases all inputs by 25% and output rises by 25%. State the returns to scale and a possible reason.", "Constant returns to scale: output rises in proportion to inputs. The firm may be able to copy its production line exactly (replication)."),
        PQ("Wages are 40 000 FCFA, capital costs 160 000 FCFA per machine and the budget is 1 600 000 FCFA. Find the intercepts and slope of the isocost line.", "Labour intercept = 1 600 000 / 40 000 = 40; capital intercept = 1 600 000 / 160 000 = 10. Slope = -40 000/160 000 = -0.25."),
        PQ("Essay plan: Explain how a firm chooses the least-cost combination of capital and labour. What happens if wages rise?", "Define isoquant, MRTS, isocost. Draw tangency; condition MRTS = w/r or MP_L/w = MP_K/r. A wage rise makes the isocost steeper in K-L terms (labour intercept falls, capital intercept unchanged). The new tangency uses more capital and less labour (factor substitution), and costs rise. Evaluate: real firms cannot always substitute (technology), capital is fixed in the short run, and the model assumes perfect information."),
        TIP("Exam link: returns to scale and the isoquant-isocost diagram appear in Paper 1 and as Paper 2 essay parts on costs or the demand for factors; always label axes and the tangency point.", title="Exam link"),
        SUM("Returns to scale: all inputs change together; compare the % change in output with the % change in inputs.",
            "An isoquant joins input combinations giving the same output; it is convex because MRTS diminishes.",
            "An isocost line: wL + rK = C, slope -w/r.",
            "Least-cost combination: isocost tangent to the isoquant, MRTS = w/r.",
            "A rise in the price of an input makes the firm substitute away from it."),
    ],
))

# ------------------------------------------------------------------ 13. Economies and diseconomies of scale
LESSONS.append(lesson(
    module=M3,
    topic="Economies and diseconomies of scale",
    title="Internal and external economies and diseconomies of scale",
    slug="ecl1-economies-diseconomies-scale",
    minutes=22,
    summary="Why long-run average cost falls as a firm grows (internal economies), why it may rise (diseconomies), how an industry's growth lowers every firm's costs (external economies), the minimum efficient scale and the shape of the long-run average cost curve.",
    objectives=[
        "Define economies of scale and classify internal and external economies",
        "Explain diseconomies of scale and their causes",
        "Calculate long-run average cost from a table and identify the minimum efficient scale",
        "Evaluate how scale affects market structure and the survival of small firms",
    ],
    key_concepts=["Economies of scale", "Internal economies", "External economies", "Diseconomies of scale",
                  "Long-run average cost", "Minimum efficient scale"],
    blocks=[
        H("Introduction"),
        T("A single baker in Buea makes 100 loaves a day; a large bakery in Douala makes 20 000. The large bakery can usually make each loaf more cheaply. "
          "But a firm that grows too much may become slow and costly to manage. These are economies and diseconomies of scale: the link between the size of a firm "
          "and its **average cost** in the long run."),
        D("**Economies of scale** are the cost advantages that cause long-run average cost (cost per unit) to fall as the scale of production rises. "
          "**Diseconomies of scale** are the disadvantages that cause long-run average cost to rise when the firm grows beyond a certain size.",
          title="Definitions: economies and diseconomies of scale"),
        D("The **long-run average cost (LRAC) curve** shows the lowest cost per unit of producing each level of output when all inputs can be changed. "
          "The **minimum efficient scale (MES)** is the lowest output at which LRAC reaches its minimum.", title="Definitions: LRAC and MES"),
        CODE("""Output (units)   LR total cost (FCFA thousand)   LRAC (FCFA per unit)
1 000                         800                    800
2 000                       1 400                    700
3 000                       1 800                    600
4 000                       2 400                    600
5 000                       3 500                    700""", "text", title="Table 1. A firm's long-run costs (invented for practice)"),
        EX("Worked example 1: LRAC and MES", intro="Using Table 1, calculate LRAC at each output, describe the pattern and state the minimum efficient scale.", steps=[
            S("Formula", math=r"LRAC = \frac{LRTC}{Q}"),
            S("Calculate", math=r"\frac{800\,000}{1\,000} = 800,\; 700,\; 600,\; 600,\; 700"),
            S("Pattern", text="LRAC falls from 800 to 600 (economies of scale), is flat between 3 000 and 4 000 (constant returns) and rises to 700 at 5 000 (diseconomies)."),
            S("MES", text="3 000 units, the lowest output at which LRAC is at its minimum of 600 FCFA."),
        ], check=r"4\,000 \times 600 = 2\,400\,000"),
        H("Internal economies of scale"),
        D("**Internal economies of scale** are cost advantages that arise from the growth of the firm itself, whatever happens in the rest of the industry.",
          title="Definition: internal economies"),
        KEY("Types of internal economies", "Always give the reason with the example.", cards=[
            ["Technical", "Large firms use big, efficient machines and can specialise tasks (a large oil mill versus hand pressing). Indivisible machines are spread over more output."],
            ["Managerial", "Large firms hire specialist managers (finance, marketing, production) who raise efficiency."],
            ["Financial", "Large firms borrow at lower interest rates because banks see less risk, and can raise money by issuing shares."],
            ["Purchasing (bulk buying)", "Large orders win discounts from suppliers."],
            ["Marketing", "Advertising and distribution costs are spread over more units."],
            ["Risk-bearing", "A firm that makes many products or sells in many places is less hurt by a failure of one."],
        ]),
        H("External economies of scale"),
        D("**External economies of scale** are cost advantages that come from the growth of the **industry** or the area, not from the size of an individual firm, "
          "so they lower the costs of every firm in it.", title="Definition: external economies"),
        T("Examples: a cluster of firms near a port attracts specialist suppliers and repair services; a pool of trained workers forms; better roads and electricity are built; "
          "a technical college opens. For instance, many small garment and food-processing firms in a town can share a trained workforce and a wholesaler. "
          "On a diagram, external economies **shift the whole LRAC curve down**, whereas internal economies are a movement **along** it."),
        KEY("Movement or shift?", "A distinction examiners like.", cards=[
            ["Internal economies", "A movement down along a given LRAC curve as the firm's output rises."],
            ["External economies", "A downward shift of the LRAC curve for all firms in the industry."],
            ["External diseconomies", "An upward shift of LRAC, e.g. traffic jams in a crowded industrial zone or higher land rents."],
        ]),
        H("Diseconomies of scale"),
        KEY("Causes of internal diseconomies", "Too much size can raise costs.", cards=[
            ["Communication and control", "Long chains of command slow decisions and instructions get distorted."],
            ["Co-ordination", "More departments and sites are harder to co-ordinate; mistakes cost more."],
            ["Worker motivation", "Workers in very large firms may feel remote, causing lower effort and industrial disputes."],
            ["Bureaucracy", "More rules and paperwork raise administration costs."],
        ]),
        EX("Worked example 2: classify the statement", intro="Classify each as an internal economy, an external economy or a diseconomy: (a) a cement firm buys limestone in bulk at a discount; (b) a new road to the port lowers transport costs for all firms in an area; (c) a very large firm's head office takes weeks to approve small repairs.", steps=[
            S("(a)", text="Internal economy (purchasing): arises from the firm's own large orders."),
            S("(b)", text="External economy: the benefit comes from infrastructure available to the whole area, not from one firm's size."),
            S("(c)", text="Diseconomy of scale (control and bureaucracy)."),
        ]),
        H("Why scale matters"),
        T("The MES decides how many firms an industry can support. If MES is large compared with the market (electricity generation), the industry tends towards one or few "
          "large firms (a natural monopoly). If MES is small (hairdressing), many small firms survive. Small firms also survive by serving niche or local markets, offering personal "
          "service or flexibility. **Evaluation:** economies of scale are only potential; firms must achieve them by good management, and growth can bring diseconomies; "
          "also, some economies depend on the market being big enough to sell the extra output."),
        MISTAKE("Confusing economies of scale with diminishing returns", "Economies of scale are a long-run fall in average cost as all inputs rise. Diminishing returns are a short-run fall in marginal product with a fixed factor."),
        MISTAKE("Listing economies of scale without explaining the cost reduction", "State the type, then explain WHY cost per unit falls. Large firms also need to be linked to a cause: 'bulk buying lowers the cost per unit because suppliers give discounts'."),
        QUIZ("A cluster of cocoa-processing firms in a port town leads to a shared pool of trained workers and cheaper repairs for all of them. This is",
             ["an internal economy of scale", "an external economy of scale", "a diseconomy of scale", "the law of diminishing returns"], 1,
             "The benefit comes from the growth of the industry in the area, so it is external.",
             hint="Does the benefit come from one firm's size, or from the industry?",
             feedback=["Internal economies come from a firm's own size.", "", "Costs fall, so it is an economy.", "That is a short-run law."]),
        QUIZ("In Table 1, the firm's minimum efficient scale is",
             ["1 000 units", "3 000 units", "4 000 units", "5 000 units"], 1,
             "LRAC first reaches its lowest value (600) at 3 000 units.",
             hint="Find the lowest output with minimum LRAC.",
             feedback=["LRAC is still 800 there.", "", "600 is also the LRAC here, but MES is the lowest such output.", "LRAC has risen to 700 at 5 000."]),
        H("Practice"),
        PQ("A firm's long-run total cost is 500 000 FCFA for 1 000 units and 900 000 FCFA for 2 000 units. Calculate LRAC at each level and comment.", "LRAC = 500 FCFA and 450 FCFA. LRAC falls as output doubles: economies of scale."),
        PQ("Explain two internal economies of scale that a large bank might enjoy.", "Financial: it can borrow cheaply and spread risk across many customers. Technical: expensive computer systems are used for more customers, so cost per transaction falls. Managerial: specialist departments (credit analysis, IT) raise efficiency."),
        PQ("Essay plan: Distinguish between internal and external economies of scale and discuss why a very large firm may experience diseconomies.", "Define both; give two examples of each with reasons; diagram: internal = movement down the LRAC, external = downward shift of LRAC. Diseconomies: communication, co-ordination, motivation, bureaucracy; LRAC rises beyond MES. Evaluation: whether diseconomies appear depends on management and technology; the MES versus market size; many large firms avoid them by decentralising."),
        TIP("Exam link: economies and diseconomies of scale appear in Paper 1 (classification, LRAC shape) and are a standard Paper 2 essay (often with the growth of firms). Link every economy to a cost reason.", title="Exam link"),
        SUM("Economies of scale: LRAC falls as output rises; diseconomies: LRAC rises.",
            "Internal economies: technical, managerial, financial, purchasing, marketing, risk-bearing.",
            "External economies come from industry growth and shift the whole LRAC down.",
            "Diseconomies: communication, co-ordination, motivation and bureaucracy problems.",
            "The minimum efficient scale, relative to the market, helps determine how many firms an industry can have."),
    ],
))

# ------------------------------------------------------------------ 14. Short-run and long-run costs
LESSONS.append(lesson(
    module=M3,
    topic="Short-run and long-run costs",
    title="Short-run cost curves (TFC, TVC, TC, AFC, AVC, ATC, MC) and the long-run average cost curve",
    slug="ecl1-short-long-run-costs",
    minutes=25,
    summary="Calculate and draw total, average and marginal costs in the short run, explain the U-shape and the MC relationships with AVC and ATC, link them to diminishing returns, and see how the long-run average cost curve is built from short-run curves.",
    objectives=[
        "Define and calculate TFC, TVC, TC, AFC, AVC, ATC and MC from a table",
        "Explain the shape of the cost curves using diminishing returns",
        "State and explain the relationship between MC and the average cost curves",
        "Explain the LRAC as the envelope of short-run average cost curves",
    ],
    key_concepts=["Fixed cost", "Variable cost", "Total cost", "Average cost", "Marginal cost", "U-shaped cost curve",
                  "Short-run average cost", "Long-run average cost envelope"],
    blocks=[
        H("Introduction"),
        T("A small cocoa-drying business has rent, a drying shed and a loan to repay whether or not it dries any cocoa this month. It also has costs "
          "that rise with output, such as labour and fuel. Separating these costs shows the firm what it must charge, when to produce more, and when to shut."),
        KEY("Cost definitions", "Use the standard abbreviations.", cards=[
            ["TFC", "Total fixed cost: costs that do not change with output in the short run (rent, loan interest). Paid even at zero output."],
            ["TVC", "Total variable cost: costs that change with output (labour, raw materials, fuel)."],
            ["TC", "Total cost = TFC + TVC."],
            ["AFC, AVC, ATC", "Per-unit costs: AFC = TFC/Q, AVC = TVC/Q, ATC (also written AC) = TC/Q = AFC + AVC."],
            ["MC", "Marginal cost: the extra cost of producing one more unit = change in TC / change in Q (= change in TVC / change in Q)."],
        ]),
        CODE("""Q   TFC   TVC    TC    AFC    AVC     ATC     MC
0    60     0    60      -      -       -      -
1    60    40   100   60.00  40.00  100.00     40
2    60    70   130   30.00  35.00   65.00     30
3    60    90   150   20.00  30.00   50.00     20
4    60   120   180   15.00  30.00   45.00     30
5    60   160   220   12.00  32.00   44.00     40
6    60   220   280   10.00  36.67   46.67     60
7    60   300   360    8.57  42.86   51.43     80""", "text", title="Table 1. A firm's short-run costs (FCFA thousand; Q in tonnes; invented for practice)"),
        EX("Worked example 1: completing the table", intro="Check the row Q = 4 in Table 1.", steps=[
            S("TC", math=r"TC = TFC + TVC = 60 + 120 = 180"),
            S("Per unit", math=r"AFC = \frac{60}{4} = 15,\quad AVC = \frac{120}{4} = 30,\quad ATC = \frac{180}{4} = 45"),
            S("Marginal cost", math=r"MC = TC_4 - TC_3 = 180 - 150 = 30"),
            S("Check", math=r"ATC = AFC + AVC = 15 + 30 = 45"),
        ], check=r"180 - 150 = 120 - 90 = 30"),
        IMG("alecl1-costs.svg", alt="Short-run cost curves. AFC falls throughout. AVC and ATC are U-shaped, ATC above AVC. MC falls to a minimum at 3 tonnes, then rises, cutting AVC and ATC at their lowest points.",
            caption="Figure 1. The curves from Table 1 (smoothed)."),
        H("Why the curves are U-shaped"),
        KEY("Four facts to learn", "Explain each in an exam.", cards=[
            ["AFC", "Falls continuously as the same fixed cost is spread over more units (the spreading-overhead effect). It never reaches zero."],
            ["MC and AVC", "Initially they fall because MP rises (increasing returns). Later they rise because of **diminishing returns**: each extra worker adds less output, so the cost of each extra unit rises."],
            ["ATC", "The vertical sum of AFC and AVC. It falls while both fall, and keeps falling after AVC starts to rise until the rising AVC outweighs the falling AFC; so the minimum of ATC is to the right of the minimum of AVC."],
            ["MC cuts AVC and ATC at their minimum", "MC below an average pulls it down; above, it pulls it up. Compare MP and AP."],
        ]),
        EX("Worked example 2: reading the relationships", intro="Use Table 1 to show that MC cuts AVC and ATC at their lowest points.", steps=[
            S("AVC", text="AVC is lowest (30) at 3 to 4 tonnes. MC is 20 at 3 (below AVC) and 30 at 4 (equal to AVC): MC meets AVC at its minimum."),
            S("ATC", text="ATC is lowest (44) at 5 tonnes. MC at 5 is 40 (below ATC, still pulling it down) and 60 at 6 (above ATC, pulling it up). MC cuts ATC from below at the minimum, between 5 and 6 tonnes."),
            S("MC minimum", text="MC is lowest (20) at 3 tonnes, before AVC and ATC reach their minima."),
            S("Link to production", text="The output where MC is lowest (3) is where marginal product was highest (see the earlier lesson): costs and product are two views of the same law."),
        ]),
        H("Long-run costs"),
        T("In the long run all factors are variable: the firm can build a bigger factory. Each size of plant has its own short-run average cost curve (SRAC). "
          "For any output, the firm will choose the plant size with the lowest cost. The long-run average cost curve (LRAC) is therefore the **envelope**: a curve that touches each SRAC curve "
          "and lies below or on all of them. It is also U-shaped, but for a different reason: **economies and diseconomies of scale**, not diminishing returns."),
        KEY("SRAC versus LRAC", "A common essay comparison.", cards=[
            ["Short run", "At least one fixed factor; U-shape caused by diminishing returns."],
            ["Long run", "All factors variable; U-shape caused by economies and then diseconomies of scale."],
            ["Relationship", "LRAC is the lower envelope of the SRAC curves. At the minimum point of LRAC, the SRAC curve touches it at its own minimum."],
        ]),
        T("Do not forget the shutdown rule (developed under profit maximisation): in the short run a firm should continue producing while price covers AVC, because "
          "fixed costs are paid anyway; in the long run it must cover ATC."),
        MISTAKE("Saying MC cuts ATC at its maximum or at any point", "MC cuts both AVC and ATC at their minimum points. It lies below the average when the average falls and above it when the average rises."),
        MISTAKE("Including fixed costs in marginal cost", "MC depends only on variable costs, since fixed costs do not change when one more unit is made."),
        QUIZ("A firm's total cost rises from 150 to 180 FCFA thousand when output rises from 3 to 4 tonnes. Marginal cost is",
             ["30", "45", "60", "180"], 0,
             "MC = change in TC / change in Q = 30 / 1 = 30.",
             hint="Marginal cost is the change in total cost for one more unit.",
             feedback=["", "45 is the average total cost at 4 tonnes.", "Not found in the table for this change.", "180 is total cost, not marginal."]),
        QUIZ("Why does average fixed cost fall continually as output rises?",
             ["Because fixed cost per unit is spread over more units", "Because of diminishing returns", "Because workers become more skilled", "Because marginal cost is falling"], 0,
             "Total fixed cost is the same, so dividing it by more units gives a smaller AFC.",
             hint="What is on the top of the AFC fraction, and does it change?",
             feedback=["", "Diminishing returns affect variable cost.", "That could lower variable cost but not fixed cost.", "AFC does not depend on MC."]),
        H("Practice"),
        PQ("A firm has TFC of 80 FCFA thousand. At 10 tonnes TVC is 120. Calculate TC, AFC, AVC and ATC at 10 tonnes.", "TC = 80 + 120 = 200. AFC = 80/10 = 8. AVC = 120/10 = 12. ATC = 200/10 = 20 (= 8 + 12)."),
        PQ("Explain why marginal cost eventually rises.", "In the short run at least one factor is fixed. As more of the variable factor is added, diminishing returns set in: marginal product falls, so each extra unit of output needs more extra labour and costs more. MC therefore rises."),
        PQ("Essay plan: Explain the shape of the short-run average cost curves and the relationship between MC and AC. How does the long-run average cost curve differ?", "Define fixed and variable costs. AFC falls; AVC U-shaped through increasing then diminishing returns; ATC = AFC + AVC, minimum to the right of AVC's minimum. MC cuts AVC and ATC at their minima (MC below average pulls it down, above pulls it up). Draw diagram. Long run: envelope of SRAC curves, shape from economies and diseconomies of scale, not diminishing returns. Evaluation: real cost curves may be flat or L-shaped over a range; firms may not know their MC."),
        TIP("Exam link: cost curve calculations, diagrams and MC relationships are central to Paper 1, Paper 2 (market structures essays) and Paper 3 cost tables. Draw MC cutting AVC and ATC at their minima.", title="Exam link"),
        SUM("TC = TFC + TVC; ATC = AFC + AVC; MC = change in TC / change in Q.",
            "AFC falls continuously; AVC and MC are U-shaped because of increasing then diminishing returns.",
            "MC cuts AVC and ATC at their minimum points.",
            "LRAC is the envelope of the SRAC curves; its U-shape comes from economies and diseconomies of scale.",
            "In the short run a firm covers AVC at least; in the long run, ATC."),
    ],
))

# ------------------------------------------------------------------ 15. Revenue curves
LESSONS.append(lesson(
    module=M3,
    topic="Revenue curves",
    title="Total, average and marginal revenue under perfect and imperfect competition",
    slug="ecl1-revenue-curves",
    minutes=22,
    summary="Total, average and marginal revenue: why AR equals price and the demand curve, the horizontal AR = MR of a price taker, the downward AR and steeper MR of a firm with market power, and the link between MR, price elasticity and total revenue.",
    objectives=[
        "Define and calculate TR, AR and MR from a table or demand equation",
        "Draw the revenue curves of a price taker and of a firm facing a downward-sloping demand curve",
        "Explain why MR lies below AR for a firm with market power",
        "Link MR and total revenue to price elasticity of demand",
    ],
    key_concepts=["Total revenue", "Average revenue", "Marginal revenue", "Price taker", "Price maker",
                  "Demand curve of the firm", "Elasticity and revenue"],
    blocks=[
        H("Introduction"),
        T("A tomato seller at a crowded market must accept the going price; if she charges more, customers go next door. A mobile-phone network with few rivals can "
          "choose its price, but it must cut the price to sell more. These two situations give two kinds of revenue curve, which in the next module are combined with cost curves to find the profit-maximising output."),
        D("**Total revenue (TR)** is the total income from sales: price times quantity. **Average revenue (AR)** is revenue per unit sold. **Marginal revenue (MR)** is the extra revenue from selling one more unit.",
          title="Definitions: TR, AR and MR", formula=r"TR = P \times Q, \quad AR = \frac{TR}{Q} = P, \quad MR = \frac{\Delta TR}{\Delta Q}"),
        T("Since AR = TR/Q = P, the **average revenue curve is the firm's demand curve**: it shows the price at which each quantity can be sold."),
        H("A price taker"),
        D("A **price taker** is a firm so small relative to the market that it cannot influence the price: it can sell any quantity at the market price. Its demand curve is horizontal (perfectly elastic).",
          title="Definition: price taker"),
        CODE("""Q    Price (AR)   TR    MR
1       50         50    50
2       50        100    50
3       50        150    50""", "text", title="Table 1. A price taker at 50 (FCFA thousand, invented for practice)"),
        T("Every extra unit sells at the same price, so **MR = AR = P**. The AR = MR line is horizontal, and TR is a straight line through the origin."),
        H("A price maker"),
        D("A **price maker** (a firm with market power) faces a downward-sloping demand curve: to sell more it must lower the price **on all units**, so MR is lower than the price.",
          title="Definition: price maker"),
        CODE("""Q     P = AR     TR     MR
0       60         0      -
5       50       250     40
10      40       400     20
15      30       450      0
20      20       400    -20
25      10       250    -40""", "text", title="Table 2. Demand P = 60 - 2Q (FCFA thousand, invented for practice); MR is the slope of TR"),
        EX("Worked example 1: deriving revenue from the demand equation", intro="Demand is P = 60 - 2Q. Derive TR and MR, and find the output where TR is maximum.", steps=[
            S("AR", math=r"AR = P = 60 - 2Q"),
            S("TR", math=r"TR = P \times Q = 60Q - 2Q^2"),
            S("MR", math=r"MR = \frac{dTR}{dQ} = 60 - 4Q", text="For a linear demand curve MR has the same intercept as AR and twice the slope."),
            S("Maximum TR", math=r"MR = 0 \Rightarrow Q = 15,\quad P = 30,\quad TR = 450"),
        ], check=r"60(15) - 2(15)^2 = 900 - 450 = 450"),
        IMG("alecl1-revenue.svg", alt="Upper panel: a straight downward AR curve (also the demand curve) from 60 at zero output to zero at 30 units, and a steeper MR line from the same starting point cutting the horizontal axis at 15. Lower panel: total revenue rises to a maximum at 15 units and falls back to zero at 30.",
            caption="Figure 1. AR, MR and TR for P = 60 - 2Q. TR is maximum where MR = 0."),
        KEY("Why MR is below AR", "Explain the cause.", cards=[
            ["The cost of a price cut", "To sell one more unit the firm cuts the price, and this lower price applies to every unit sold, so the firm loses revenue on the earlier units."],
            ["MR = P minus the loss", "MR is the price of the extra unit minus the revenue lost on the other units; hence MR < AR."],
            ["Negative MR", "When the loss on earlier units exceeds the price of the new one, MR is negative and TR falls."],
        ]),
        H("Revenue and elasticity"),
        F(r"MR = P\left(1 + \frac{1}{PED}\right)", title="MR and elasticity (PED is negative)"),
        EX("Worked example 2: PED and MR on the same demand curve", intro="Using P = 60 - 2Q (so Q = 30 - 0.5P), find PED and MR at Q = 5, Q = 15 and Q = 20.", steps=[
            S("Q = 5, P = 50", math=r"PED = -0.5 \times \frac{50}{5} = -5;\quad MR = 50(1 - 0.2) = 40", text="Elastic: MR positive; a price cut raises TR."),
            S("Q = 15, P = 30", math=r"PED = -0.5 \times \frac{30}{15} = -1;\quad MR = 0", text="Unitary elasticity: TR is at its maximum."),
            S("Q = 20, P = 20", math=r"PED = -0.5 \times \frac{20}{20} = -0.5;\quad MR = 20(1 - 2) = -20", text="Inelastic: MR negative; a price cut lowers TR."),
        ]),
        KEY("Summary of the link", "Learn these three lines.", cards=[
            ["Elastic part of demand", "MR > 0; TR rises as output rises."],
            ["Unitary elasticity", "MR = 0; TR at maximum."],
            ["Inelastic part", "MR < 0; TR falls as output rises."],
        ]),
        T("This is why a profit-maximising firm with market power always operates on the **elastic** part of its demand curve: it equates MC with MR, and MC is positive, so MR must be positive."),
        MISTAKE("Drawing MR above AR or giving it the same slope", "For a straight-line AR curve, MR has the same vertical intercept and twice the slope, so it meets the quantity axis at half the quantity where AR does."),
        MISTAKE("Saying a firm in perfect competition has a downward demand curve", "The market demand curve slopes down, but each price-taking firm's own demand curve is horizontal at the market price."),
        QUIZ("A firm faces P = 100 - 3Q. At Q = 8, total revenue is",
             ["76", "608", "800", "52"], 1,
             "P = 100 - 24 = 76; TR = 76 x 8 = 608.",
             hint="Find the price first, then multiply by Q.",
             feedback=["76 is the price.", "", "100 x 8 ignores the price cut.", "52 is the marginal revenue at Q = 8 (100 - 6 x 8)."]),
        QUIZ("A firm's demand is unit elastic at its current output. Its marginal revenue is",
             ["positive", "zero", "negative", "equal to price"], 1,
             "MR = P(1 + 1/PED) = P(1 - 1) = 0.",
             hint="Substitute PED = -1 into the MR formula.",
             feedback=["MR is positive when demand is elastic.", "", "MR is negative when demand is inelastic.", "MR equals price only for a price taker."]),
        H("Practice"),
        PQ("A firm faces demand P = 80 - 4Q. Derive TR and MR and the output at which TR is maximised.", "TR = 80Q - 4Q^2. MR = 80 - 8Q. MR = 0 gives Q = 10, P = 40, TR = 400."),
        PQ("Explain why the marginal revenue curve of a firm facing a downward-sloping demand curve lies below its average revenue curve.", "To sell an extra unit the firm must lower the price on all units, so the extra revenue is the new price less the revenue lost on the units that could have been sold at the higher price. MR is therefore less than price (AR)."),
        PQ("Essay plan: Distinguish between the revenue curves of a firm in perfect competition and of a monopolist, and explain the relationship between MR and elasticity.", "Perfect competition: price taker, AR = MR = P horizontal, TR straight line. Monopoly (price maker): AR = demand slopes down, MR below it with twice the slope, TR rises then falls. Elasticity: MR positive when |PED| > 1, zero at 1, negative when below 1; so a profit-maximising firm operates on the elastic part. Evaluation: real firms estimate demand imperfectly, and price discrimination can change the revenue curves."),
        TIP("Exam link: revenue curves appear in Paper 1 (calculations, shapes) and are essential for Paper 2 essays on profit maximisation, perfect competition and monopoly; draw AR and MR with the correct relative slope.", title="Exam link"),
        SUM("TR = P x Q, AR = TR/Q = P (the demand curve), MR = change in TR / change in Q.",
            "Price taker: horizontal AR = MR = P. Price maker: downward AR with MR below it.",
            "For linear demand, MR has the same intercept and twice the slope of AR.",
            "MR > 0 when demand is elastic, MR = 0 at unitary elasticity (TR maximum) and MR < 0 when inelastic.",
            "A firm with market power operates on the elastic part of its demand curve."),
    ],
))
