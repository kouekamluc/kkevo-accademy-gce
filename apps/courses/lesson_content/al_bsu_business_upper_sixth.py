"""A Level Business Studies, Upper Sixth: Operations & Production Management, Business Finance & Managerial Accounting,
Financial Statement Analysis & Investment Appraisal, Strategic Management & Change, and the Examination module.

KKEVO draft for reviewer checking. The outline follows KKEVO's master curriculum blueprint (module lines U6M1-U6M4), not
a Board syllabus booklet, and Business Studies is not in the Board's 2023 Advanced Level report, so paper details are
given in general terms ("check the exact format with your teacher").
All firms, prices and figures in examples are invented for practice. Every EOQ, reorder level, critical path and float,
break-even, cash flow, budget variance, ratio, payback, ARR, NPV and IRR was checked by script.
Where textbooks differ (gearing formula, ROCE definition, ARR denominator, free float wording) the lesson says
"check your textbook".
"""

from .dsl import *  # noqa: F403

COURSE = ("business-studies", "upper-sixth")

M_OPS = "Operations & Production Management"
M_FIN = "Business Finance & Managerial Accounting"
M_FSA = "Financial Statement Analysis & Investment Appraisal"
M_STR = "Strategic Management & Change"
M_EX = "Examination"

LESSONS = []


# ------------------------------------------------------------------ 1. Location of industry
LESSONS.append(lesson(
    module=M_OPS,
    topic="Location of industry",
    title="Choosing where to locate: factors, factor rating and location break-even",
    slug="bsu-location-of-industry",
    minutes=21,
    summary="How firms choose a location: quantitative and qualitative factors, the weighted factor-rating method, location break-even (cost-volume) comparison, industrial inertia and international location, with evaluation.",
    objectives=[
        "Explain the quantitative and qualitative factors that influence a location decision",
        "Use weighted factor rating and location break-even analysis to compare sites",
        "Explain industrial inertia, footloose industry and the reasons for locating abroad",
        "Evaluate the limits of numerical location methods",
    ],
    key_concepts=["Quantitative factor", "Qualitative factor", "Weighted factor rating", "Location break-even",
                  "Industrial inertia", "Footloose industry", "Offshoring"],
    blocks=[
        H("Introduction"),
        T("A brewery, a cement works, a cocoa-processing plant and a call centre have very different needs. A cement works wants to be near limestone and a port; a call centre wants reliable electricity, internet and staff who speak the customers' language. "
          "The **location decision** is a long-term, high-cost decision that is hard to reverse, so A Level questions expect you to weigh several factors and use numerical methods with care."),
        D("A **quantitative factor** can be measured in money or numbers (land price, wage rates, transport cost per tonne, grants, tax). A **qualitative factor** cannot easily be measured (quality of life for managers, political stability, the attitude of the local community, room to expand).", title="Two kinds of factor"),
        KEY("Main location factors", "Most exam answers group the factors like this.", cards=[
            ["Costs", "Land and rent, labour (wages and skills), transport of raw materials and finished goods, utilities such as power and water."],
            ["Market", "Nearness to customers matters most for bulky, perishable or service products: bread, soft drinks, banking."],
            ["Infrastructure", "Roads, rail, ports (Douala, Kribi), airports, reliable electricity and telecommunications."],
            ["Government", "Grants, tax reliefs, special economic zones, planning rules, regulations. Check the current incentives in the investment law."],
            ["Other", "Safety, political stability, community attitudes, environmental rules, access to suppliers (clusters)."],
        ]),
        T("A firm is **bulk-reducing** when the product weighs less than its raw materials (cocoa beans into cocoa butter, timber into planks): it tends to locate near the raw material. A firm is **bulk-increasing** when the product is heavier or more fragile than its inputs (bottled drinks): it tends to locate near the market."),
        H("Method 1: weighted factor rating"),
        D("Choose the factors, give each a **weight** that shows its importance (weights add to 1 or to 100%), score each site on each factor (for example out of 10), multiply score by weight and add. The highest total is preferred.", title="Weighted factor rating"),
        F(r"\text{Weighted score} = \sum (\text{weight} \times \text{score})"),
        CODE("Factor (weight)        Douala   Kribi   Yaounde\n"
             "Market access (0.30)      9        5        8\n"
             "Port/transport (0.25)     9        8        5\n"
             "Labour cost (0.20)        5        7        6\n"
             "Land cost (0.15)          4        8        6\n"
             "Utilities (0.10)          7        5        7", "text", title="Table 1. Scores out of 10 (invented for practice)"),
        EX("Worked example 1: rating three sites", intro="A drinks firm compares Douala, Kribi and Yaounde using Table 1. Which site does the method recommend?", steps=[
            S("Douala", math=r"0.3(9) + 0.25(9) + 0.2(5) + 0.15(4) + 0.1(7) = 2.7 + 2.25 + 1.0 + 0.6 + 0.7 = 7.25"),
            S("Kribi", math=r"1.5 + 2.0 + 1.4 + 1.2 + 0.5 = 6.60"),
            S("Yaounde", math=r"2.4 + 1.25 + 1.2 + 0.9 + 0.7 = 6.45"),
            S("Decision", text="Douala scores highest (7.25). But the weights and scores are judgements: if land cost were given a weight of 0.30, the ranking could change. Always say this in an evaluation."),
        ], check=r"0.3 + 0.25 + 0.2 + 0.15 + 0.1 = 1"),
        H("Method 2: location break-even"),
        D(r"Compare the **total cost** at each site, $TC = FC + VC \times Q$. The output at which two sites cost the same is the **indifference point**; above it the site with the lower variable cost is cheaper.", title="Location break-even (cost-volume analysis)"),
        F(r"Q^{*} = \frac{FC_A - FC_B}{VC_B - VC_A}"),
        EX("Worked example 2: two sites", intro="Site A: fixed costs FCFA 40 000 000 a year, variable cost FCFA 2 000 a unit. Site B: fixed costs FCFA 25 000 000, variable cost FCFA 3 500 a unit. Expected output is 12 000 units a year. Which site is cheaper?", steps=[
            S("Indifference output", math=r"Q^{*} = \frac{40\,000\,000 - 25\,000\,000}{3\,500 - 2\,000} = \frac{15\,000\,000}{1\,500} = 10\,000 \text{ units}"),
            S("Cost at 12 000 units, site A", math=r"40\,000\,000 + 2\,000 \times 12\,000 = 64\,000\,000"),
            S("Cost at 12 000 units, site B", math=r"25\,000\,000 + 3\,500 \times 12\,000 = 67\,000\,000"),
            S("Decision", text="Above 10 000 units, site A (lower variable cost) is cheaper: FCFA 3 000 000 a year less at 12 000 units. If demand is uncertain and may stay below 10 000 units, site B carries less risk."),
        ], check=r"40\,000\,000 + 2\,000(10\,000) = 25\,000\,000 + 3\,500(10\,000) = 60\,000\,000"),
        H("Inertia, footloose firms and going abroad"),
        T("**Industrial inertia** is when a firm stays in its location after the original advantages have gone, because moving is costly, the workforce and suppliers are there, and the name is linked to the place. "
          "A **footloose industry** is not tied to raw materials or a market (software, call centres, many services), so it can choose on cost and quality of life. "
          "**Offshoring** means moving production or services abroad; **reshoring** means bringing them back. Firms locate abroad to reach new markets, avoid tariffs, use cheaper inputs or follow customers, but they face exchange-rate risk, cultural and legal differences, longer supply chains and reputational risk."),
        KEY("Evaluation: limits of the methods", "Numbers help, but judgement decides.", cards=[
            ["Subjective inputs", "Weights and scores in factor rating are opinions; a small change can reverse the ranking."],
            ["Forecasts", "Location break-even depends on forecast costs and output, which may be wrong."],
            ["Qualitative factors", "Security, quality of life and community attitudes are hard to score but can decide the outcome."],
            ["Long term", "Costs change: a new road, port or power line can change the best site within a few years."],
        ]),
        MISTAKE("Listing factors without applying them", "Explain WHY a factor matters for THIS business: a bulky, low-value product such as cement is driven by transport cost; a bank branch is driven by the market."),
        MISTAKE("Treating the top weighted score as the final answer", "The method is only as good as its weights. Comment on sensitivity and on factors left out."),
        QUIZ("Site P has fixed costs of FCFA 30 m and variable cost FCFA 1 000 a unit; site Q has fixed costs FCFA 18 m and variable cost FCFA 1 600 a unit. At what output do they cost the same?",
             ["7 500 units", "20 000 units", "12 000 units", "30 000 units"], 1,
             "(30 m − 18 m) ÷ (1 600 − 1 000) = 12 m ÷ 600 = 20 000 units.", hint="Divide the difference in fixed costs by the difference in variable costs.",
             feedback=["That is 12 m ÷ 1 600: divide by the difference in variable costs, not one of them.", "", "That is the difference in fixed costs in millions, not an output.", "That is 30 m ÷ 1 000, which ignores site Q."]),
        QUIZ("A firm turns 10 tonnes of timber into 4 tonnes of planks. Where is it most likely to locate?",
             ["Near the forest", "Near the market", "Near the capital city", "Anywhere: it is footloose"], 0,
             "It is bulk-reducing: carrying the lighter finished product saves transport cost, so it locates near the raw material.", hint="Which is heavier to carry: the input or the output?",
             feedback=["", "Near the market suits bulk-increasing or perishable products.", "Being near the government is not the main cost factor here.", "A firm tied to a heavy raw material is not footloose."]),
        TIP("Location appears in Paper 1 (factors, calculations such as indifference output) and in Paper 2 essays and Paper 3 case studies, where you must recommend a site and justify it. Check the exact format with your teacher.", title="Exam link"),
        PQ("Using Table 1, the firm decides labour cost should have weight 0.30 and market access 0.20 (other weights unchanged). Recalculate the scores. Does the decision change?",
           "Douala = 0.2(9) + 0.25(9) + 0.3(5) + 0.15(4) + 0.1(7) = 1.8 + 2.25 + 1.5 + 0.6 + 0.7 = 6.85. Kribi = 1.0 + 2.0 + 2.1 + 1.2 + 0.5 = 6.80. Yaounde = 1.6 + 1.25 + 1.8 + 0.9 + 0.7 = 6.25. Douala still wins, but only just (6.85 against 6.80): the decision is sensitive to the weights, so qualitative factors should decide."),
        PQ("Site X: fixed costs FCFA 50 m, variable cost FCFA 4 000 a unit. Site Y: fixed costs FCFA 32 m, variable cost FCFA 5 500 a unit. Find the indifference output and the cheaper site at 15 000 units.",
           "Q* = (50 m − 32 m) ÷ (5 500 − 4 000) = 18 m ÷ 1 500 = 12 000 units. At 15 000 units: X = 50 m + 60 m = 110 m; Y = 32 m + 82.5 m = 114.5 m. X is cheaper by FCFA 4.5 m."),
        PQ("Evaluate whether a Cameroonian food-processing firm should locate its new factory in a special economic zone near a deep-water port. (Essay plan)",
           "Introduction: define location decision; long-term and costly. For: lower export transport costs, possible tax reliefs and simpler procedures (check the current rules), reliable infrastructure, nearness to other firms (suppliers, services). Against: distance from raw materials (farms) raises inbound costs for a bulk-reducing product; skilled staff may need to move; land and services may be dearer; incentives may be time-limited. Evaluation: depends on whether the firm mainly exports (port matters) or serves the home market; use factor rating and location break-even but test the weights; qualitative factors (security, community, expansion space) may decide. Conclusion: a justified judgement for this firm."),
        SUM("Location is a long-term, costly, hard-to-reverse decision based on quantitative and qualitative factors.",
            "Bulk-reducing firms locate near raw materials; bulk-increasing and perishable products locate near the market.",
            "Weighted factor rating: total = sum of weight × score; the result depends on subjective weights.",
            "Location break-even: indifference output = difference in fixed costs ÷ difference in variable costs; above it the lower-variable-cost site is cheaper.",
            "Inertia, footloose firms and offshoring explain why real locations do not always match the cheapest site."),
    ],
))


# ------------------------------------------------------------------ 2. Methods of production
LESSONS.append(lesson(
    module=M_OPS,
    topic="Methods of production",
    title="Job, batch, flow and mass customization: choosing a production method",
    slug="bsu-methods-of-production",
    minutes=20,
    summary="The main methods of production (job, batch, flow, mass customization and cell production), the cost of set-ups in batch work, and how a firm chooses a method from the product, the market, technology and finance.",
    objectives=[
        "Describe job, batch, flow, mass customization and cell production with examples",
        "Calculate how batch size affects the cost per unit when there is a set-up cost",
        "Analyse the advantages and disadvantages of each method for a given business",
        "Evaluate which method suits a business and why firms change method as they grow",
    ],
    key_concepts=["Job production", "Batch production", "Flow production", "Mass customization", "Cell production",
                  "Set-up cost", "Capital intensity"],
    blocks=[
        H("Introduction"),
        T("A tailor in Bamenda sews one suit to a customer's measurements. A bakery in Buea makes 300 loaves of white bread, then 200 of sweet bread. A brewery fills bottles on a line that runs day and night. "
          "These are three **methods of production**. The method affects unit cost, quality, flexibility, the skills needed and the money that must be invested, so it is a key operations decision."),
        D("**Job production**: one unique item is made at a time to a customer's specification (a wedding dress, a bridge, a custom website). **Batch production**: a group of identical items passes through each stage together before the next batch starts (bread, shoes, medicines). **Flow production**: items move continuously from one stage to the next on a production line (bottled drinks, cement, refined oil).", title="Three classic methods"),
        D("**Mass customization** combines the low unit cost of flow production with some choice for each customer, usually through flexible machines and computer systems (choosing the options of a car or the design of a printed T-shirt online). **Cell production** splits a flow line into self-contained teams (cells), each making a complete part or product, which links to lean production.", title="Modern methods"),
        KEY("Comparing the methods", "The trade-off is between flexibility and unit cost.", cards=[
            ["Job", "Very flexible, high quality, motivated skilled staff, high price possible. But high unit cost, slow, labour-intensive."],
            ["Batch", "Some variety, machines shared between products, some economies of scale. But idle time and set-up costs between batches, stocks of work in progress."],
            ["Flow", "Lowest unit cost, consistent quality, high capacity, often capital-intensive. But inflexible, huge investment, repetitive work, a breakdown stops the whole line."],
            ["Mass customization", "Choice and low cost together; customers may pay more. But needs flexible technology, IT and a responsive supply chain."],
        ]),
        H("The cost of a set-up in batch production"),
        T("Before each batch, machines must be cleaned, adjusted or re-tooled. This **set-up cost** is the same whatever the batch size, so larger batches spread it over more units. But larger batches mean more stock held and less flexibility."),
        F(r"\text{Cost per unit} = \text{variable cost per unit} + \frac{\text{set-up cost}}{\text{batch size}}"),
        EX("Worked example 1: batch size and unit cost", intro="A juice firm has a set-up cost of FCFA 60 000 for each batch and a variable cost of FCFA 500 a bottle. Find the cost per bottle for batches of 200 and 1 000 bottles.", steps=[
            S("Batch of 200", math=r"500 + \frac{60\,000}{200} = 500 + 300 = 800 \text{ FCFA}"),
            S("Batch of 1 000", math=r"500 + \frac{60\,000}{1\,000} = 500 + 60 = 560 \text{ FCFA}"),
            S("Interpret", text="Larger batches cut the cost per bottle by FCFA 240, but the firm then holds more stock of each flavour and responds more slowly to changes in demand. The best batch size balances set-up cost against holding cost (the same idea as the economic order quantity in the next lessons)."),
        ], check=r"60\,000 \div 200 = 300"),
        H("Choosing a method"),
        T("The choice depends on: the **nature of the product** (unique or standard); the **size of the market** (flow needs high, stable demand); **finance** available (flow and mass customization need large capital); **technology** and skills; and the firm's **marketing strategy** (a premium, personalised product or a low-cost one). Firms often move from job to batch to flow as the market grows, and many factories mix methods: flow for the main product, batch for packaging variants."),
        EX("Worked example 2: recommending a method", intro="A furniture maker in Yaounde makes beds to order for wealthy customers. A supermarket chain now wants 2 000 identical beds a year. Should it change its method?", steps=[
            S("Present method", text="Job production suits unique, high-price beds made by skilled carpenters."),
            S("The new order", text="2 000 identical beds is a large, standard volume: batch production would cut unit cost by sharing machines and set-ups."),
            S("Constraints", text="It needs new machines (finance), space, staff training and quality control; the supermarket will press for a low price."),
            S("Judgement", text="A sensible answer: use batch production for the supermarket order in a separate area, and keep job production for the premium customers so the brand is not damaged. Flow production is not justified at 2 000 units a year."),
        ]),
        MISTAKE("Saying flow production is always best because it is cheapest", "Flow is cheapest per unit only at high, stable volumes. With small or changing demand, its fixed costs and inflexibility make it the wrong choice."),
        MISTAKE("Confusing batch size with method", "Batch production can have small or large batches; what defines it is that items move between stages in groups, with set-ups between batches."),
        QUIZ("Which product is most suited to flow production?", ["Bottled mineral water", "A wedding dress", "A new hospital building", "A batch of 50 school uniforms in one size"], 0,
             "Bottled water is standard, in high and steady demand: ideal for a continuous line.", hint="Which product is identical and needed in very large numbers?",
             feedback=["", "A wedding dress is unique: job production.", "A building is a one-off project: job production.", "50 identical uniforms is a batch."]),
        QUIZ("Set-up cost FCFA 45 000 a batch, variable cost FCFA 300 a unit. What is the cost per unit for a batch of 150?", ["FCFA 300", "FCFA 600", "FCFA 450", "FCFA 345"], 1,
             "300 + 45 000 ÷ 150 = 300 + 300 = FCFA 600.", hint="Spread the set-up cost over the batch, then add the variable cost.",
             feedback=["That ignores the set-up cost.", "", "That is 300 × 1.5: divide 45 000 by 150 instead.", "That adds 45, not 45 000 ÷ 150."]),
        TIP("Methods of production appear in Paper 1 (definitions, matching products to methods, simple unit-cost calculations) and in Paper 2 and Paper 3 when you must recommend a method for a business. Always link the method to the product, market and finance in the case.", title="Exam link"),
        PQ("Set-up cost FCFA 90 000, variable cost FCFA 1 200 a unit. Calculate the cost per unit for batches of 100 and 450. What is the saving per unit?",
           "Batch 100: 1 200 + 90 000 ÷ 100 = 1 200 + 900 = 2 100. Batch 450: 1 200 + 200 = 1 400. Saving: FCFA 700 a unit. The firm must weigh this against holding more stock."),
        PQ("Explain two disadvantages of flow production for workers and two for the business.",
           "Workers: repetitive, boring tasks lead to low motivation and absence; little use of skills (link to Herzberg and job design). Business: very high capital cost and long payback; inflexible, so a change in demand leaves expensive capacity idle; one breakdown stops the whole line; poor motivation may raise labour turnover and defects."),
        PQ("Discuss whether mass customization is a suitable strategy for a growing Cameroonian clothing brand. (Essay plan)",
           "Define mass customization. For: customers want personal designs; can charge a premium; online ordering reaches more buyers; digital printing and cutting allow small runs at low cost. Against: needs investment in IT, flexible machines and fast delivery; reliable power and internet are needed; returns and errors cost money; competition from imported cheap clothes. Evaluation: suitable if the brand targets a segment willing to pay for personal designs and can start small (e.g. printed designs on standard blanks) before investing heavily. Conclusion with a justified judgement."),
        SUM("Job production makes one unique item at a time: flexible and high quality, but high unit cost.",
            "Batch production moves groups of items through each stage; set-up costs are spread over the batch.",
            "Flow production gives the lowest unit cost at high, stable volume but is inflexible and capital-intensive.",
            "Mass customization and cell production try to combine low cost with flexibility.",
            "The choice depends on the product, the market size, finance, technology and marketing strategy."),
    ],
))


# ------------------------------------------------------------------ 3. Productivity and capacity utilization
LESSONS.append(lesson(
    module=M_OPS,
    topic="Productivity and capacity utilization",
    title="Productivity and capacity utilization: measuring and improving efficiency",
    slug="bsu-productivity-capacity-utilization",
    minutes=21,
    summary="Labour and capital productivity, unit labour cost, capacity utilization and its effect on unit fixed cost, and how firms deal with under- and over-utilization (rationalization, subcontracting, extra shifts).",
    objectives=[
        "Calculate labour productivity, unit labour cost and capacity utilization",
        "Explain why higher capacity utilization lowers the fixed cost per unit",
        "Analyse ways to raise productivity and to deal with excess or insufficient capacity",
        "Evaluate whether a firm should aim for 100% capacity utilization",
    ],
    key_concepts=["Productivity", "Labour productivity", "Unit labour cost", "Capacity", "Capacity utilization",
                  "Rationalization", "Subcontracting"],
    blocks=[
        H("Introduction"),
        T("Two bakeries in Douala each employ 15 workers. One makes 9 000 loaves a week, the other 12 000. The second is more **productive**: it turns the same input into more output, so its cost per loaf is lower and it can cut prices or earn more profit. "
          "This lesson measures efficiency in two ways: how much each input produces (productivity) and how much of the possible output is actually made (capacity utilization)."),
        D("**Productivity** is output per unit of input in a period. **Labour productivity** = output ÷ number of workers (or ÷ hours worked). **Capital productivity** = output ÷ capital employed or ÷ machine hours.", title="Productivity", formula=r"\text{Labour productivity} = \frac{\text{output per period}}{\text{number of workers}}"),
        D("**Unit labour cost** is the labour cost of making one unit. It falls if productivity rises faster than wages.", title="Unit labour cost", formula=r"\text{Unit labour cost} = \frac{\text{total labour cost}}{\text{output}}"),
        D("**Capacity** is the maximum output a firm can produce with its present resources in a period. **Capacity utilization** is actual output as a percentage of that maximum.", title="Capacity utilization", formula=r"\text{Capacity utilization} = \frac{\text{actual output}}{\text{maximum possible output}} \times 100"),
        EX("Worked example 1: a bakery", intro="A bakery employs 15 workers, each paid FCFA 30 000 a week. It makes 9 000 loaves a week; its maximum is 12 000. Fixed costs are FCFA 1 800 000 a week. Find labour productivity, unit labour cost, capacity utilization and fixed cost per loaf.", steps=[
            S("Labour productivity", math=r"9\,000 \div 15 = 600 \text{ loaves per worker per week}"),
            S("Unit labour cost", math=r"\frac{15 \times 30\,000}{9\,000} = \frac{450\,000}{9\,000} = 50 \text{ FCFA a loaf}"),
            S("Capacity utilization", math=r"\frac{9\,000}{12\,000} \times 100 = 75\%"),
            S("Fixed cost per loaf", math=r"1\,800\,000 \div 9\,000 = 200 \text{ FCFA}"),
        ], check=r"600 \times 15 = 9\,000"),
        H("Why utilization matters for cost"),
        T("Fixed costs (rent, loan interest, salaried managers, depreciation) do not change with output in the short run. When output rises towards capacity, the same fixed cost is spread over more units, so **average fixed cost** and therefore **average (unit) cost** fall."),
        EX("Worked example 2: raising utilization to 90%", intro="The bakery wins a hotel contract and raises output to 90% of capacity. Variable cost is FCFA 150 a loaf. What happens to the cost per loaf?", steps=[
            S("New output", math=r"0.9 \times 12\,000 = 10\,800 \text{ loaves}"),
            S("Fixed cost per loaf", math=r"1\,800\,000 \div 10\,800 \approx 166.67 \text{ FCFA}"),
            S("Average cost before and after", math=r"150 + 200 = 350 \;\to\; 150 + 166.67 = 316.67 \text{ FCFA}"),
            S("Interpret", text="The unit cost falls by about FCFA 33 a loaf, which strengthens the bakery's competitiveness."),
        ], check=r"1\,800\,000 \div 10\,800 = 166.\overline{6}"),
        H("Dealing with too little or too much use"),
        KEY("Under-utilization (spare capacity)", "Causes: falling demand, new competitors, seasonal sales.", cards=[
            ["Raise demand", "Marketing, new markets, using spare capacity to make for other firms (be a subcontractor)."],
            ["Rationalization", "Cut capacity: close a plant or line, sell machines, reduce staff. Lowers fixed cost but may hurt morale and cost redundancy pay."],
        ]),
        KEY("Over-utilization (close to or above 100%)", "Running flat out has costs too.", cards=[
            ["Problems", "No time for maintenance, more breakdowns and mistakes, overtime costs, stressed staff, orders turned away."],
            ["Responses", "Subcontract (outsource) some work, add shifts, invest in new capacity if the demand is expected to last."],
        ]),
        T("Ways to raise **productivity**: training, better motivation and job design, new technology and automation, lean methods (less waste), better maintenance, and improved layout. Each costs money and takes time, and higher productivity can lead to job cuts, which may cause resistance."),
        MISTAKE("Mixing up productivity and production", "Production is total output. Productivity is output per unit of input. A firm can raise production by hiring more staff while its productivity falls."),
        MISTAKE("Saying 100% utilization is the ideal", "Most firms aim for a high rate (often 85% to 95% in textbooks; check yours) that leaves time for maintenance and room for unexpected orders."),
        QUIZ("A factory can make 25 000 units a month and makes 20 000. What is its capacity utilization?", ["80%", "125%", "20%", "5 000 units"], 0,
             "20 000 ÷ 25 000 × 100 = 80%.", hint="Actual output ÷ maximum output × 100.",
             feedback=["", "That is maximum ÷ actual: the fraction is upside down.", "That is the spare capacity as a percentage.", "That is the spare capacity in units, not a utilization rate."]),
        QUIZ("Wages rise by 5% and labour productivity rises by 10%. What happens to unit labour cost?", ["It rises", "It falls", "It stays the same", "It cannot change because wages rose"], 1,
             "Each unit uses less labour time, and the productivity gain is larger than the wage rise, so labour cost per unit falls (1.05 ÷ 1.10 ≈ 0.955, about 4.5% lower).", hint="Unit labour cost = labour cost ÷ output. Which grows faster?",
             feedback=["It would rise only if wages grew faster than productivity.", "", "It stays the same only if both grow at the same rate.", "Unit labour cost depends on output too, not only on wages."]),
        TIP("Paper 1 often tests the formulas (capacity utilization, productivity, unit costs). In Paper 2 and Paper 3, link utilization to unit costs, prices and profit, and weigh rationalization against its human cost.", title="Exam link"),
        PQ("A garage with 6 mechanics services 288 cars in a 4-week month. A new diagnostic machine lets 6 mechanics service 360 cars. Calculate labour productivity per mechanic per week before and after, and the percentage increase.",
           "Before: 288 ÷ 6 ÷ 4 = 12 cars per mechanic per week. After: 360 ÷ 6 ÷ 4 = 15. Increase: (15 − 12) ÷ 12 × 100 = 25%."),
        PQ("A hotel has 80 rooms, so 2 400 room-nights in a 30-day month. It sells 1 680 room-nights. Fixed costs are FCFA 21 000 000 a month. Find capacity utilization and fixed cost per room-night. What happens to fixed cost per room-night if it sells 2 100?",
           "Utilization = 1 680 ÷ 2 400 × 100 = 70%. Fixed cost per room-night = 21 000 000 ÷ 1 680 = FCFA 12 500. At 2 100 room-nights (87.5%): 21 000 000 ÷ 2 100 = FCFA 10 000, a fall of FCFA 2 500."),
        PQ("A manufacturer is working at 98% capacity and demand is still growing. Discuss whether it should subcontract or build new capacity. (Essay plan)",
           "Define capacity and utilization; problems of running near 100%. Subcontracting: quick, no capital, flexible if the rise is temporary; but less control of quality and delivery, lower margin, risk of the subcontractor becoming a competitor. New capacity: lower unit cost long term, control, economies of scale; but high capital cost, risk if demand falls, time lag to build. Evaluation: depends on how certain and lasting the growth is (forecasts), finance available (gearing), quality importance and competitors. Judgement: subcontract now while gathering evidence, invest if growth is confirmed."),
        SUM("Productivity is output per unit of input; labour productivity = output ÷ workers (or hours).",
            "Unit labour cost = labour cost ÷ output; it falls when productivity rises faster than wages.",
            "Capacity utilization = actual output ÷ maximum output × 100.",
            "Higher utilization spreads fixed costs, lowering fixed and average cost per unit.",
            "Spare capacity: raise demand or rationalize. Near-full capacity: subcontract, add shifts or invest, but not without evidence that demand will last."),
    ],
))


# ------------------------------------------------------------------ 4. Inventory control
LESSONS.append(lesson(
    module=M_OPS,
    topic="Inventory control",
    title="Inventory control: stock control charts, reorder levels and the economic order quantity",
    slug="bsu-inventory-control",
    minutes=22,
    summary="Why firms hold inventory, the costs of holding too much or too little, reading a stock control chart (buffer, reorder level, lead time, maximum) and calculating the reorder level and the economic order quantity (EOQ), with its limits.",
    objectives=[
        "Explain the costs of holding too much and too little inventory",
        "Read and draw a stock control chart and calculate the reorder level and maximum stock",
        "Calculate the economic order quantity and the ordering and holding costs",
        "Evaluate the assumptions of the EOQ model and of buffer-stock systems",
    ],
    key_concepts=["Inventory (stock)", "Buffer stock", "Lead time", "Reorder level", "Reorder quantity",
                  "Holding cost", "Ordering cost", "Economic order quantity (EOQ)"],
    blocks=[
        H("Introduction"),
        T("A cement distributor in Garoua must never run out in the building season, but every bag in the warehouse ties up cash, takes space and may harden in the damp. "
          "**Inventory** (stock) is held as raw materials, work in progress and finished goods. Inventory control asks two questions: **when** to order and **how much** to order."),
        KEY("Too much or too little?", "Both cost money.", cards=[
            ["Costs of holding too much", "Cash tied up (opportunity cost), storage and insurance, security, damage, theft and going out of date (obsolescence)."],
            ["Costs of holding too little (stock-out)", "Lost sales and customer goodwill, idle production and workers, emergency orders at high prices, lost bulk discounts."],
        ]),
        H("The stock control chart"),
        D("**Buffer stock**: the minimum level held to cover delays or unexpected demand. **Lead time**: the time between placing an order and receiving it. **Reorder level**: the stock level at which a new order is placed. **Reorder quantity**: the amount ordered each time. **Maximum stock** = buffer stock + reorder quantity.", title="Key terms"),
        F(r"\text{Reorder level} = \text{usage per period} \times \text{lead time} + \text{buffer stock}"),
        IMG("albsu-stock-control.svg", alt="Stock control chart: stock falls in straight lines from 1 300 to 300 bags every 2.5 weeks, an order is placed when stock reaches the reorder level of 1 100 and arrives 2 weeks later, bringing stock back to the maximum.",
            caption="Figure 1. A stock control chart (invented figures): usage 400 bags a week, lead time 2 weeks, buffer stock 300, order quantity 1 000."),
        EX("Worked example 1: reading Figure 1", intro="A distributor uses 400 bags a week. Lead time is 2 weeks, buffer stock 300 bags and each order is for 1 000 bags. Find the reorder level and maximum stock, and how often orders arrive.", steps=[
            S("Usage during the lead time", math=r"400 \times 2 = 800 \text{ bags}"),
            S("Reorder level", math=r"800 + 300 = 1\,100 \text{ bags}"),
            S("Maximum stock", math=r"300 + 1\,000 = 1\,300 \text{ bags}"),
            S("Time between deliveries", math=r"1\,000 \div 400 = 2.5 \text{ weeks}"),
        ], check=r"1\,100 - 400 \times 2 = 300 = \text{buffer}"),
        H("How much to order: the economic order quantity"),
        T("Ordering in large amounts means few orders (low **ordering costs**: administration, delivery charges) but a high average stock (high **holding costs**). Small orders do the opposite. The **economic order quantity** (EOQ) is the order size that minimises the total of the two. With steady usage, average stock is half the order quantity."),
        F(r"EOQ = \sqrt{\frac{2DS}{H}}", title="D = yearly demand (units), S = cost of placing one order, H = holding cost of one unit for a year"),
        EX("Worked example 2: calculating the EOQ", intro="Yearly demand is 20 000 bags (400 a week for 50 weeks). Each order costs FCFA 10 000 to place and deliver. Holding one bag for a year costs FCFA 400. Find the EOQ and the yearly ordering and holding costs at the EOQ.", steps=[
            S("Substitute", math=r"EOQ = \sqrt{\frac{2 \times 20\,000 \times 10\,000}{400}} = \sqrt{1\,000\,000} = 1\,000 \text{ bags}"),
            S("Ordering cost", math=r"\frac{20\,000}{1\,000} \times 10\,000 = 20 \times 10\,000 = 200\,000 \text{ FCFA}"),
            S("Holding cost", math=r"\frac{1\,000}{2} \times 400 = 200\,000 \text{ FCFA}"),
            S("Interpret", text="At the EOQ the two costs are equal and their total (FCFA 400 000 a year) is the lowest possible. This is why Figure 1 uses an order of 1 000 bags."),
        ], check=r"\frac{D}{Q}S = \frac{Q}{2}H \text{ at } Q = 1\,000"),
        EX("Worked example 3: holding cost as a percentage", intro="A shop sells 7 200 cartons a year. Each order costs FCFA 5 000. A carton costs FCFA 800 and holding costs are 25% of its value a year. Find the EOQ.", steps=[
            S("Holding cost per unit", math=r"H = 0.25 \times 800 = 200 \text{ FCFA}"),
            S("EOQ", math=r"\sqrt{\frac{2 \times 7\,200 \times 5\,000}{200}} = \sqrt{360\,000} = 600 \text{ cartons}"),
            S("Orders a year", math=r"7\,200 \div 600 = 12 \text{ orders (one a month)}"),
        ]),
        KEY("Evaluating the EOQ and buffer systems", "Useful, but built on assumptions.", cards=[
            ["Assumptions", "Demand, lead time and costs are known and constant; no bulk discounts; stock arrives all at once."],
            ["Reality", "Demand is seasonal (school uniforms, cement in the dry season); suppliers are late; discounts reward big orders."],
            ["Judgement", "Use the EOQ as a guide, then adjust for discounts, storage space, cash available and supplier reliability. Computerised systems and JIT (next lesson) change the approach."],
        ]),
        MISTAKE("Forgetting the buffer in the reorder level", "Reorder level is usage during the lead time PLUS buffer stock. Without the buffer, the firm would reach zero just as the delivery arrives, with no margin for delay."),
        MISTAKE("Using the price instead of the holding cost in the EOQ", "H is the cost of holding ONE unit for a YEAR. If it is given as a percentage, multiply the percentage by the unit value first."),
        QUIZ("Usage is 250 units a day, lead time 4 days and buffer stock 600 units. What is the reorder level?", ["1 000 units", "1 600 units", "850 units", "600 units"], 1,
             "250 × 4 + 600 = 1 600 units.", hint="Usage during the lead time, plus the buffer.",
             feedback=["That is the usage during the lead time without the buffer.", "", "That adds one day's usage to the buffer, not four.", "That is only the buffer stock."]),
        QUIZ("If the cost of placing an order rises, what happens to the EOQ?", ["It falls", "It rises", "It stays the same", "It becomes zero"], 1,
             "S is in the numerator of the formula, so a higher ordering cost raises the EOQ: the firm orders more each time, and less often.", hint="Where is S in the formula?",
             feedback=["That would happen if HOLDING cost rose.", "", "The EOQ depends on S.", "The EOQ is never zero while demand is positive."]),
        TIP("Paper 1 tests reorder level, maximum stock and EOQ calculations and chart reading. In Paper 2 and Paper 3, use them to judge whether a firm holds too much stock, and link to working capital and cash flow.", title="Exam link"),
        PQ("Daily usage 150 kg, lead time 6 days, buffer stock 400 kg, reorder quantity 2 400 kg. Find the reorder level, the maximum stock and the number of days between deliveries.",
           "Reorder level = 150 × 6 + 400 = 1 300 kg. Maximum = 400 + 2 400 = 2 800 kg. Days between deliveries = 2 400 ÷ 150 = 16 days."),
        PQ("Yearly demand 48 000 units, ordering cost FCFA 15 000 an order, holding cost FCFA 900 a unit a year. Calculate the EOQ and the total yearly ordering and holding cost at the EOQ.",
           "EOQ = √(2 × 48 000 × 15 000 ÷ 900) = √1 600 000 ≈ 1 265 units. Ordering cost = 48 000 ÷ 1 264.9 × 15 000 ≈ FCFA 569 210; holding cost = 1 264.9 ÷ 2 × 900 ≈ FCFA 569 210; total ≈ FCFA 1 138 420 a year."),
        PQ("A supplier offers a 3% discount on orders of at least 5 000 units, far above the EOQ. Explain how the firm should decide. (Short answer)",
           "Compare total yearly cost (purchase cost + ordering cost + holding cost) at the EOQ with the total at 5 000 units. The discount cuts the purchase cost and ordering cost (fewer orders) but raises holding cost (average stock 2 500). Also consider storage space, cash flow, risk of damage or obsolescence and supplier reliability. Take the discount only if the total cost is lower and cash and space allow."),
        SUM("Inventory is held as raw materials, work in progress and finished goods; too much and too little both cost money.",
            "Reorder level = usage per period × lead time + buffer stock; maximum stock = buffer + reorder quantity.",
            "EOQ = √(2DS ÷ H) minimises ordering plus holding costs; at the EOQ the two are equal.",
            "Holding cost per unit may be given as a percentage of unit value: convert it first.",
            "The EOQ assumes steady demand and costs and no discounts, so use it as a guide, not a rule."),
    ],
))


# ------------------------------------------------------------------ 5. Lean production and quality management
LESSONS.append(lesson(
    module=M_OPS,
    topic="Lean production and quality management",
    title="Lean production, JIT, kaizen and total quality management",
    slug="bsu-lean-production-quality",
    minutes=22,
    summary="Lean production and the wastes it removes, just-in-time and kanban, kaizen, quality control versus quality assurance, total quality management, benchmarking and quality standards, with the conditions each needs to work.",
    objectives=[
        "Explain lean production and the main forms of waste it removes",
        "Analyse just-in-time inventory and kaizen, including the conditions they need",
        "Distinguish quality control, quality assurance and total quality management",
        "Evaluate lean and quality methods for a business in a given context",
    ],
    key_concepts=["Lean production", "Waste", "Just-in-time (JIT)", "Kanban", "Kaizen", "Quality control",
                  "Quality assurance", "Total quality management (TQM)", "Benchmarking"],
    blocks=[
        H("Introduction"),
        T("Lean production grew out of the Toyota Production System in Japan. Its idea is simple: use fewer resources (materials, time, space, labour, stock) to make the same or better output, by removing everything that does not add value for the customer. "
          "Quality management asks a related question: how do we make sure every product is right first time? Both matter to Cameroonian firms competing with imports on price and quality."),
        D("**Lean production** is an approach that aims to cut waste of all kinds in every part of production while keeping or raising quality.", title="Lean production"),
        KEY("Seven wastes (a common textbook list)", "Look for these in any process.", cards=[
            ["Over-production", "Making more than is ordered."],
            ["Waiting", "Workers or machines idle."],
            ["Transport and motion", "Moving goods or people more than needed."],
            ["Over-processing", "Doing more work than the customer values."],
            ["Inventory", "Stock that ties up cash and hides problems."],
            ["Defects", "Faulty items that need rework or are scrapped."],
        ], note="Some textbooks add an eighth waste, the unused skills of workers. Check your textbook."),
        H("Just-in-time and kanban"),
        D("**Just-in-time (JIT)** means materials arrive just when they are needed and goods are made only when ordered, so little or no buffer stock is held. A **kanban** is a signal (a card, bin or electronic message) that tells the previous stage or the supplier to send more.", title="JIT and kanban"),
        EX("Worked example 1: the stock saving from JIT", intro="A furniture maker holds average stock worth FCFA 4 000 000. Holding costs (storage, insurance, capital tied up) are 20% of stock value a year. With JIT, average stock falls to FCFA 1 000 000. What is the yearly saving, and how much cash is released?", steps=[
            S("Holding cost before", math=r"0.20 \times 4\,000\,000 = 800\,000 \text{ FCFA}"),
            S("Holding cost after", math=r"0.20 \times 1\,000\,000 = 200\,000 \text{ FCFA}"),
            S("Yearly saving", math=r"800\,000 - 200\,000 = 600\,000 \text{ FCFA}"),
            S("Cash released", text="FCFA 3 000 000 of working capital is freed once, which improves liquidity (link to the working capital lesson). Against this, the firm may lose bulk discounts and pay more for frequent small deliveries."),
        ]),
        KEY("When does JIT work?", "JIT is not right for every firm.", cards=[
            ["Needs", "Reliable, nearby suppliers; good roads and transport; reliable power; flexible, multi-skilled staff; good IT and communication; steady demand."],
            ["Benefits", "Lower holding costs and cash tied up, less waste and space, problems become visible, faster response to customers."],
            ["Risks", "One late delivery stops production; no stock to meet a sudden rise in demand; more ordering and delivery costs; dependence on suppliers."],
        ]),
        H("Kaizen and cell production"),
        T("**Kaizen** (continuous improvement) means many small, regular improvements suggested by the workers who do the job, rather than rare large changes. It needs worker involvement, empowerment and trust, and it links to Herzberg's motivators and to team working. "
          "**Cell production** organises workers into teams that each make a complete part or product, which gives ownership and makes kaizen easier."),
        H("Approaches to quality"),
        D("**Quality control** inspects products, usually at the end of production, to find and remove faulty ones. **Quality assurance** builds quality into every stage, setting standards and checking the process, so faults are prevented. **Total quality management (TQM)** makes quality the responsibility of every employee, focuses on the internal and external customer, and aims for zero defects through continuous improvement.", title="Three approaches"),
        T("TQM is usually linked with W. Edwards Deming and with Japanese manufacturing. Other tools: **quality circles** (small groups of workers who meet to solve quality problems), **benchmarking** (comparing processes with the best firms and adopting their methods) and **quality standards** such as ISO 9001 certification, which shows customers that a firm follows a documented quality system."),
        EX("Worked example 2: the cost of defects", intro="A shoe factory makes 1 200 pairs a week at a cost of FCFA 6 000 a pair. 24 pairs are faulty and scrapped. After a quality-assurance programme, defects fall to 6 pairs. Find the defect rate before and after, and the cost of each good pair before and after.", steps=[
            S("Defect rate before", math=r"24 \div 1\,200 \times 100 = 2\%"),
            S("Defect rate after", math=r"6 \div 1\,200 \times 100 = 0.5\%"),
            S("Cost per good pair before", math=r"\frac{1\,200 \times 6\,000}{1\,176} = \frac{7\,200\,000}{1\,176} \approx 6\,122 \text{ FCFA}"),
            S("Cost per good pair after", math=r"\frac{7\,200\,000}{1\,194} \approx 6\,030 \text{ FCFA}"),
        ], check=r"1\,200 - 24 = 1\,176"),
        T("**Evaluation.** Lean and TQM need a change of culture, training and time; gains are often slow at first. They may fail if managers do not trust workers or if supply conditions are poor. But they can give a lasting competitive advantage through lower costs and better reputation."),
        MISTAKE("Saying JIT means holding no stock at all", "JIT means holding as little as possible, timed to need. Most firms using JIT still hold a small amount of stock for safety."),
        MISTAKE("Treating quality control and quality assurance as the same", "Control finds faults after they happen; assurance prevents them during the process. TQM goes further by involving everyone."),
        QUIZ("A firm relies on imported parts that take several weeks to clear a port and often arrive late. Is JIT suitable?", ["Yes, because JIT always cuts costs", "No, because JIT needs reliable and quick deliveries", "Yes, because JIT removes the need for suppliers", "No, because JIT only works for services"], 1,
             "JIT depends on reliable, short lead times. Long, uncertain deliveries would cause stock-outs and stop production.", hint="What happens under JIT if a delivery is late?",
             feedback=["JIT cuts costs only when its conditions are met.", "", "JIT depends heavily on suppliers.", "JIT is used mostly in manufacturing."]),
        QUIZ("Which approach makes every employee responsible for quality and aims for zero defects?", ["Quality control", "Total quality management", "Benchmarking", "Batch production"], 1,
             "TQM spreads responsibility for quality to everyone and seeks continuous improvement.", hint="Which approach is 'total'?",
             feedback=["Quality control relies on inspectors checking output.", "", "Benchmarking compares with the best firms; it is one tool, not the whole approach.", "Batch production is a method of production, not a quality approach."]),
        TIP("In Paper 1 expect definitions (JIT, kaizen, TQM, benchmarking) and simple calculations (holding cost saving, defect rate). In Paper 2 and Paper 3, judge whether lean methods suit the business in its setting: supplier reliability, infrastructure, culture and finance.", title="Exam link"),
        PQ("Average stock falls from FCFA 9 000 000 to FCFA 2 500 000 after JIT. Holding costs are 18% of stock value a year. Calculate the yearly holding-cost saving.",
           "Before: 0.18 × 9 000 000 = 1 620 000. After: 0.18 × 2 500 000 = 450 000. Saving = FCFA 1 170 000 a year (and FCFA 6 500 000 of cash is released once)."),
        PQ("Explain two differences between quality control and total quality management.",
           "1. Who: in quality control, inspectors check quality; in TQM every worker is responsible. 2. When: quality control finds faults at the end of a process (detection); TQM prevents them at every stage (prevention) and aims for zero defects. Also: TQM includes the internal customer and continuous improvement; quality control does not."),
        PQ("Evaluate whether a large Cameroonian brewery should introduce lean production. (Essay plan)",
           "Define lean and its tools (JIT, kaizen, TQM, cells). Benefits: lower stock and holding costs, less waste of bottles and ingredients, higher quality, motivated staff through kaizen, cash freed. Problems: imported inputs (malt, packaging) with long and uncertain lead times make full JIT risky; power cuts; training costs; resistance to change; seasonal demand peaks. Evaluation: adopt lean selectively: kaizen and TQM in the plant, JIT for local inputs only, buffer stock for imported inputs. Conclusion: a justified judgement on the extent of lean adoption."),
        SUM("Lean production cuts all forms of waste: over-production, waiting, transport, motion, over-processing, inventory and defects.",
            "JIT keeps stock low by matching deliveries to need; it needs reliable suppliers, transport and steady demand.",
            "Kaizen is continuous improvement through many small, worker-led changes.",
            "Quality control detects faults; quality assurance prevents them; TQM makes quality everyone's job.",
            "Benchmarking and quality standards help, but lean and TQM need culture change, training and time."),
    ],
))


# ------------------------------------------------------------------ 6. Critical path analysis
LESSONS.append(lesson(
    module=M_OPS,
    topic="Critical path analysis",
    title="Critical path analysis: network diagrams, earliest and latest times, total and free float",
    slug="bsu-critical-path-analysis",
    minutes=22,
    summary="How to draw an activity-on-arrow network, calculate earliest start times and latest finish times, find the critical path and the project duration, calculate total and free float, use a PERT estimate, and evaluate CPA as a planning tool.",
    objectives=[
        "Draw a network from a table of activities, durations and dependencies",
        "Calculate earliest start times (EST) and latest finish times (LFT) and identify the critical path",
        "Calculate total float and free float and explain what each means for managers",
        "Evaluate the usefulness and limits of critical path analysis, including PERT estimates",
    ],
    key_concepts=["Network diagram", "Node", "Activity", "Earliest start time (EST)", "Latest finish time (LFT)",
                  "Critical path", "Total float", "Free float", "PERT"],
    blocks=[
        H("Introduction"),
        T("A firm opening a new bakery outlet in Limbe must find premises, fit them out, install ovens, recruit and train staff and advertise. Some tasks must wait for others; some can run at the same time. "
          "**Critical path analysis** (CPA, also called network analysis) shows the order of tasks, the shortest time in which the whole project can be finished, and which tasks cannot be delayed without delaying the project."),
        D("An **activity** is a task that takes time (an arrow). A **node** (circle) is the start or end of activities: an event. In this course's style each node shows its number (left), the **earliest start time** of the activities leaving it (EST, top right) and the **latest finish time** of the activities entering it (LFT, bottom right). Check your textbook: some books use activity-on-node diagrams instead.", title="Network terms"),
        CODE("Activity   Description              Depends on   Duration (days)\n"
             "A          Find and lease premises   -            3\n"
             "B          Order ovens               -            2\n"
             "C          Fit out the shop          A            4\n"
             "D          Recruit staff             A            5\n"
             "E          Deliver ovens             B            3\n"
             "F          Install ovens             C, E         2\n"
             "G          Train staff and open      D, F         3", "text", title="Table 1. The bakery project (invented)"),
        IMG("albsu-cpa-network.svg", alt="Network, six nodes. Arrows (days): A 3 node 1 to 2, B 2 node 1 to 3, C 4 node 2 to 4, D 5 node 2 to 5, E 3 node 3 to 4, F 2 node 4 to 5, G 3 node 5 to 6. ESTs 0, 3, 2, 7, 9, 12; LFTs 0, 3, 4, 7, 9, 12. Critical path A, C, F, G in blue.",
            caption="Figure 1. The network for Table 1 with EST (top) and LFT (bottom) in each node."),
        H("Step 1: the forward pass (EST)"),
        T("Start with EST = 0 at node 1. Move left to right: EST of a node = EST of the previous node + duration of the activity. Where several arrows enter a node, take the **largest** value, because the next activities cannot start until all of them are finished."),
        EX("Worked example 1: forward pass", intro="Find the EST at each node of Figure 1.", steps=[
            S("Nodes 2 and 3", math=r"EST_2 = 0 + 3 = 3, \quad EST_3 = 0 + 2 = 2"),
            S("Node 4 (C and E enter)", math=r"EST_4 = \max(3 + 4,\; 2 + 3) = \max(7, 5) = 7"),
            S("Node 5 (D and F enter)", math=r"EST_5 = \max(3 + 5,\; 7 + 2) = \max(8, 9) = 9"),
            S("Node 6", math=r"EST_6 = 9 + 3 = 12 \text{ days: the project duration}"),
        ]),
        H("Step 2: the backward pass (LFT)"),
        T("At the last node, LFT = EST (12). Move right to left: LFT of a node = LFT of the next node − duration of the activity. Where several arrows leave a node, take the **smallest** value."),
        EX("Worked example 2: backward pass and critical path", intro="Find the LFT at each node and the critical path.", steps=[
            S("Nodes 6 and 5", math=r"LFT_6 = 12, \quad LFT_5 = 12 - 3 = 9"),
            S("Node 4", math=r"LFT_4 = 9 - 2 = 7"),
            S("Node 3", math=r"LFT_3 = 7 - 3 = 4"),
            S("Node 2 (C and D leave)", math=r"LFT_2 = \min(7 - 4,\; 9 - 5) = \min(3, 4) = 3"),
            S("Critical path", text="Activities whose start and end nodes have EST = LFT and whose duration fills the gap: A, C, F, G (3 + 4 + 2 + 3 = 12 days). A delay to any of them delays the opening."),
        ], check=r"3 + 4 + 2 + 3 = 12"),
        H("Step 3: float"),
        D("**Total float** is the time an activity can be delayed without delaying the whole project. **Free float** is the time it can be delayed without delaying the earliest start of the NEXT activity. Critical activities have zero float.", title="Float",
          formula=r"\text{Total float} = LFT_{end} - \text{duration} - EST_{start}, \qquad \text{Free float} = EST_{end} - \text{duration} - EST_{start}"),
        EX("Worked example 3: float on non-critical activities", intro="Calculate the total and free float of B, D and E.", steps=[
            S("B (node 1 to 3)", math=r"TF = 4 - 2 - 0 = 2, \quad FF = 2 - 2 - 0 = 0"),
            S("D (node 2 to 5)", math=r"TF = 9 - 5 - 3 = 1, \quad FF = 9 - 5 - 3 = 1"),
            S("E (node 3 to 4)", math=r"TF = 7 - 3 - 2 = 2, \quad FF = 7 - 3 - 2 = 2"),
            S("Interpret", text="B has 2 days of total float but no free float: if B slips, E starts late and uses up E's float. The float of B and E is shared along the path B-E."),
        ]),
        T("**PERT.** When durations are uncertain, PERT uses three estimates: optimistic (o), most likely (m) and pessimistic (p). The expected time is (o + 4m + p) ÷ 6. If recruiting staff could take 4, 6 or 14 days, the expected time is (4 + 24 + 14) ÷ 6 = 7 days. Using 7 instead of 5 for D would give D a negative total float (9 − 7 − 3 = −1), so D would become critical and the project would take 13 days."),
        KEY("Evaluating CPA", "A planning tool, not a guarantee.", cards=[
            ["Benefits", "Shows the shortest project time, the order of tasks and where to focus control; helps plan resources and cash (JIT deliveries of materials); float shows where staff can be moved."],
            ["Limits", "Durations are estimates; complex projects need software; it does not show costs or quality; the plan must be updated as delays happen; it may encourage pressure on staff."],
        ]),
        MISTAKE("Taking the smaller value in the forward pass", "In the forward pass, a node waits for ALL incoming activities: take the LARGEST total. In the backward pass take the SMALLEST."),
        MISTAKE("Confusing total and free float", "Total float uses the LFT of the end node; free float uses the EST of the end node. Free float can never be bigger than total float."),
        QUIZ("In Figure 1, by how many days can activity D be delayed without delaying the project?", ["0 days", "1 day", "2 days", "4 days"], 1,
             "TF of D = LFT of node 5 (9) − 5 − EST of node 2 (3) = 1 day.", hint="Total float = LFT(end node) − duration − EST(start node).",
             feedback=["D is not on the critical path, so it has some float.", "", "That is the float of B or E.", "That is 9 − 5, which forgets to subtract the EST of 3."]),
        QUIZ("Activity E is delayed by 3 days. What happens to the project?", ["Nothing: E has 3 days of float", "It is delayed by 1 day", "It is delayed by 3 days", "It is finished 1 day early"], 1,
             "E has a total float of 2 days, so a 3-day delay uses all of it and delays the project by 3 − 2 = 1 day.", hint="Compare the delay with E's total float.",
             feedback=["E's total float is 2 days, not 3.", "", "Only the part of the delay beyond the float delays the project.", "A delay cannot shorten the project."]),
        TIP("CPA is a favourite calculation: Paper 1 may ask for an EST, an LFT, a float or the critical path from a small network; Paper 2 and Paper 3 may ask you to complete a network and then evaluate the plan. Show the node values clearly and state the critical path and duration.", title="Exam link"),
        PQ("Using Figure 1, the time to fit out the shop (C) rises from 4 to 6 days. Find the new project duration and critical path.",
           "Forward pass: EST2 = 3, EST3 = 2, EST4 = max(3 + 6, 2 + 3) = 9, EST5 = max(3 + 5, 9 + 2) = 11, EST6 = 14. The project now takes 14 days; the critical path is still A, C, F, G (3 + 6 + 2 + 3 = 14)."),
        PQ("Activities: P 4 days (start), Q 6 days (start), R 3 days (after P), S 5 days (after P), T 2 days (after Q and R), U 4 days (after S and T). Find the project duration, the critical path and the total float of Q.",
           "Forward pass: P ends 4, Q ends 6, R ends 7, S ends 9, T starts max(6, 7) = 7 and ends 9, U starts max(9, 9) = 9 and ends 13. Duration 13 days. Backward pass: LFT of U's start = 9, so S and T must finish by 9; T's start event LFT = 7; R must finish by 7 and so P by min(7 − 3, 9 − 5) = 4. Critical paths: P-S-U (4 + 5 + 4 = 13) and P-R-T-U (4 + 3 + 2 + 4 = 13). Q: TF = 7 − 6 − 0 = 1 day."),
        PQ("Evaluate the use of critical path analysis by a construction firm building a new market hall. (Essay plan)",
           "Explain CPA: network, EST, LFT, critical path, float. Benefits: shortest completion time, focus on critical tasks, plan when to order materials and hire labour (cash flow, JIT), float lets managers move workers, basis for monitoring. Limits: durations are estimates (rainy season, late deliveries, permits), needs updating, no cost or quality information, complexity on large projects. Evaluation: very useful if updated regularly and combined with PERT estimates, cost budgets and quality control. Conclusion."),
        SUM("CPA shows the order of activities, the shortest project time and the critical activities.",
            "Forward pass: EST of a node = largest of (previous EST + duration). Backward pass: LFT = smallest of (next LFT − duration).",
            "The critical path has zero float; its length is the project duration.",
            "Total float = LFT(end) − duration − EST(start); free float = EST(end) − duration − EST(start).",
            "PERT expected time = (o + 4m + p) ÷ 6; CPA is only as good as its estimates and must be updated."),
    ],
))


# ------------------------------------------------------------------ 7. Sources of finance
LESSONS.append(lesson(
    module=M_FIN,
    topic="Sources of finance",
    title="Sources of finance: internal and external, short and long term, and gearing",
    slug="bsu-sources-of-finance",
    minutes=21,
    summary="Internal and external sources of short-term and long-term finance (retained profit, overdrafts, trade credit, factoring, leasing, loans, bonds, shares, venture capital, microfinance), the gearing ratio and how a business chooses the right source.",
    objectives=[
        "Classify sources of finance as internal or external and short or long term",
        "Explain the advantages and disadvantages of the main sources, including factoring and leasing",
        "Calculate gearing and explain how a new loan or share issue changes it",
        "Evaluate the most suitable source of finance for a business in a given situation",
    ],
    key_concepts=["Internal finance", "External finance", "Retained profit", "Overdraft", "Trade credit", "Factoring",
                  "Leasing", "Debenture (bond)", "Share capital", "Venture capital", "Gearing"],
    blocks=[
        H("Introduction"),
        T("Every business needs money: to start, to pay suppliers while waiting for customers to pay, and to grow. A market trader may borrow from a tontine (njangi); a growing manufacturer may take a bank loan; a large company may sell shares. "
          "Choosing the wrong source is costly: a long-term project paid for with an overdraft, or a small firm giving away control it did not need to, can ruin a sound business."),
        D("**Internal finance** comes from within the business: retained profit, sale of assets, cutting inventory or collecting debts faster. **External finance** comes from outside: banks, suppliers, investors, owners putting in new capital, government or donors.", title="Internal and external"),
        D("**Short-term finance** is repaid within a year and usually pays for working capital (stock, wages, bills). **Long-term finance** (often more than five years; check your textbook for the exact split between medium and long term) pays for non-current assets such as buildings and machines. The basic rule is to **match** the source to the use.", title="Short and long term"),
        KEY("Short-term sources", "Mainly for working capital.", cards=[
            ["Overdraft", "Flexible borrowing up to a limit on a current account; interest only on what is used. But the rate is high and the bank can ask for repayment at short notice."],
            ["Trade credit", "Buying now and paying the supplier later (often 30 to 90 days). Free if paid on time, but discounts for quick payment are lost."],
            ["Factoring", "Selling receivables (money owed by customers) to a factor for immediate cash, less a fee. Improves cash flow but cuts profit and the factor deals with customers."],
        ]),
        KEY("Long-term sources", "For non-current assets and growth.", cards=[
            ["Retained profit", "No interest and no loss of control, but limited in size and shareholders may want dividends instead."],
            ["Bank loans and bonds (debentures)", "Large sums for a fixed period; interest must be paid even in bad years; security (collateral) is often needed. Raises gearing."],
            ["Leasing and hire purchase", "Use of an asset (vehicles, machines) for regular payments without a large outlay. Costlier in total; with leasing the firm does not own the asset."],
            ["Share capital", "Permanent, no interest; but dividends are expected and new shareholders dilute control. A public share issue is costly and needs a listed company (check the current listing rules)."],
            ["Venture capital and microfinance", "Venture capitalists take a stake in risky, high-growth firms and give advice; microfinance institutions lend small sums to small firms, often at high interest rates."],
        ]),
        H("Gearing"),
        D("**Gearing** measures how far a business relies on long-term borrowing rather than on its owners' capital. A highly geared firm (often taken as above 50%) has high fixed interest payments and is riskier in a downturn, but owners keep more control and may gain more when profits are high. Check your textbook: some books define gearing as debt ÷ equity instead.", title="Gearing",
          formula=r"\text{Gearing} = \frac{\text{non-current liabilities}}{\text{non-current liabilities} + \text{equity}} \times 100"),
        EX("Worked example 1: loan or share issue?", intro="A company has non-current liabilities (loans) of FCFA 30 m and equity of FCFA 70 m. It needs FCFA 50 m for a new production line. A bank offers a loan at 12% a year. Compare gearing after a loan and after a share issue, and find the yearly interest on the loan.", steps=[
            S("Gearing now", math=r"\frac{30}{30 + 70} \times 100 = 30\%"),
            S("After a FCFA 50 m loan", math=r"\frac{80}{80 + 70} \times 100 = \frac{80}{150} \times 100 \approx 53.3\%"),
            S("After a FCFA 50 m share issue", math=r"\frac{30}{30 + 120} \times 100 = 20\%"),
            S("Yearly interest on the loan", math=r"0.12 \times 50 = 6 \text{ m FCFA}"),
            S("Interpret", text="The loan makes the company highly geared with FCFA 6 m of fixed interest a year; the share issue keeps gearing low but dilutes the owners' control and creates an expectation of dividends."),
        ], check=r"80 \div 150 = 0.5\overline{3}"),
        EX("Worked example 2: the cost of factoring", intro="A firm is owed FCFA 10 000 000 by customers who will pay in 60 days. A factor pays FCFA 9 500 000 now. What does factoring cost, as a percentage of the debts?", steps=[
            S("Fee", math=r"10\,000\,000 - 9\,500\,000 = 500\,000 \text{ FCFA}"),
            S("As a percentage", math=r"500\,000 \div 10\,000\,000 \times 100 = 5\%"),
            S("Judgement", text="5% for 60 days is expensive (roughly 30% a year), so factoring is worth it only if the cash prevents a costly problem, such as missing a payroll or losing a supplier discount."),
        ]),
        KEY("Choosing a source: the factors", "Use these in every evaluation.", cards=[
            ["Purpose and time", "Match long-term uses with long-term finance."],
            ["Cost", "Interest rates, fees, dividends expected, issue costs."],
            ["Amount and legal form", "Only companies can sell shares; a sole trader is limited to personal savings, loans, njangi, microfinance."],
            ["Gearing and risk", "A highly geared firm may be refused loans or charged more."],
            ["Control", "Owners may refuse to share control with new shareholders or venture capitalists."],
        ]),
        MISTAKE("Using an overdraft to buy a building", "An overdraft is short term and can be withdrawn. Long-term assets need long-term finance (loan, mortgage, shares, leasing)."),
        MISTAKE("Calling retained profit 'free'", "Retained profit has no interest, but it has an opportunity cost: it could have been paid as dividends or used elsewhere."),
        QUIZ("A company has loans of FCFA 45 m and equity of FCFA 105 m. What is its gearing (non-current liabilities ÷ capital employed)?", ["30%", "42.9%", "70%", "45%"], 0,
             "45 ÷ (45 + 105) × 100 = 45 ÷ 150 × 100 = 30%.", hint="Capital employed = non-current liabilities + equity.",
             feedback=["", "That is 45 ÷ 105, the debt-to-equity version.", "That is equity as a share of capital employed.", "That is the loan in millions, not a percentage."]),
        QUIZ("A sole trader needs FCFA 2 m for three months to buy stock before the festive season. Which source is most suitable?", ["Issuing shares", "A 10-year bank loan", "An overdraft or trade credit", "A bond issue"], 2,
             "The need is short term and for working capital, so short-term finance fits.", hint="Match the time period of the source to the need.",
             feedback=["A sole trader cannot issue shares.", "A 10-year loan for a 3-month need costs interest long after the stock is sold.", "", "Bonds are for large companies and long-term needs."]),
        TIP("Paper 1 tests classification (internal/external, short/long) and gearing. In Paper 2 and Paper 3 you must recommend a source for a business in its context: say why it fits and why the alternatives do not.", title="Exam link"),
        PQ("A company with loans of FCFA 60 m and equity of FCFA 140 m takes a new loan of FCFA 40 m. Calculate gearing before and after, and comment.",
           "Before: 60 ÷ 200 × 100 = 30%. After: 100 ÷ 240 × 100 ≈ 41.7%. Gearing rises but stays below the 50% level often used as a guide; risk rises because interest must be paid even if profits fall."),
        PQ("Explain two advantages and two disadvantages of leasing delivery vehicles rather than buying them with a loan.",
           "Advantages: no large initial outlay, so cash is kept for working capital; maintenance and replacement may be included, keeping the fleet modern. Disadvantages: more expensive in total over the life of the asset; the firm never owns the vehicles, so they cannot be sold or used as security."),
        PQ("A family-owned food processor in Bafoussam wants FCFA 300 m to build a second factory. Evaluate the options. (Essay plan)",
           "Options: retained profit (cheap, control kept, but probably not enough), bank loan (control kept, but gearing and interest rise; collateral needed), new shares to outside investors or a venture capitalist (no interest, expertise, but loss of family control), leasing of machines (spreads cost), government or development-bank schemes (check current programmes). Evaluate using purpose, cost, gearing, control and risk; consider a mix (retained profit + loan + leasing). Conclusion: recommend a justified combination."),
        SUM("Sources are internal (retained profit, asset sales, working capital) or external (banks, suppliers, investors).",
            "Match the source to the use: short-term finance for working capital, long-term finance for non-current assets.",
            "Overdrafts, trade credit and factoring are short term; loans, bonds, leasing, shares and venture capital are long term.",
            "Gearing = non-current liabilities ÷ (non-current liabilities + equity) × 100; high gearing means more financial risk.",
            "Choose using purpose, cost, amount, legal form, gearing and control."),
    ],
))


# ------------------------------------------------------------------ 8. Working capital and cash flow forecasting
LESSONS.append(lesson(
    module=M_FIN,
    topic="Working capital and cash flow forecasting",
    title="Working capital, the cash cycle and cash flow forecasts",
    slug="bsu-working-capital-cash-flow",
    minutes=22,
    summary="Working capital and the working capital (cash) cycle, the difference between cash and profit, how to build and read a cash flow forecast, and ways to improve cash flow, with their costs.",
    objectives=[
        "Calculate working capital and the length of the working capital cycle",
        "Explain why a profitable business can run out of cash",
        "Complete and interpret a cash flow forecast",
        "Evaluate methods of improving cash flow and of managing working capital",
    ],
    key_concepts=["Working capital", "Working capital cycle", "Liquidity", "Cash flow", "Cash flow forecast",
                  "Net cash flow", "Opening and closing balance", "Insolvency"],
    blocks=[
        H("Introduction"),
        T("Many businesses that fail are profitable on paper. A wholesaler in Douala sells on 60 days' credit but must pay suppliers in 30 days and wages every month: if cash runs out before customers pay, it cannot pay its bills. "
          "**Working capital** is the money available for day-to-day running; the **cash flow forecast** shows whether there will be enough in the months ahead."),
        D("**Working capital** = current assets − current liabilities. Current assets are inventory, trade receivables and cash; current liabilities are trade payables, overdraft and other debts due within a year. Too little working capital means the firm may not pay its debts on time (a **liquidity** problem); too much means cash lies idle instead of earning a return.", title="Working capital",
          formula=r"\text{Working capital} = \text{current assets} - \text{current liabilities}"),
        H("The working capital cycle"),
        T("Cash is paid for materials, which become inventory, then finished goods, then sales on credit, then cash again. The **working capital (cash) cycle** is the time between paying suppliers and receiving cash from customers."),
        F(r"\text{Cycle (days)} = \text{inventory days} + \text{receivable days} - \text{payable days}"),
        EX("Worked example 1: the cycle", intro="A furniture wholesaler holds inventory for 45 days, gives customers 60 days' credit and takes 30 days' credit from suppliers. Current assets are FCFA 18 m and current liabilities FCFA 10 m. Find working capital and the length of the cycle.", steps=[
            S("Working capital", math=r"18 - 10 = 8 \text{ m FCFA}"),
            S("Cycle", math=r"45 + 60 - 30 = 75 \text{ days}"),
            S("Interpret", text="For 75 days the firm's own cash is tied up. Shorter credit to customers or longer credit from suppliers would shorten the cycle and reduce the working capital needed."),
        ]),
        D("**Profit** = revenue − costs for a period, recorded when sales are made. **Cash flow** is the actual money in and out, recorded when it is paid or received. They differ because of credit sales and purchases, buying non-current assets (cash out at once, cost spread by depreciation), loans and owners' capital.", title="Cash is not profit"),
        H("The cash flow forecast"),
        T("A **cash flow forecast** predicts monthly cash inflows and outflows. Net cash flow = inflows − outflows. Closing balance = opening balance + net cash flow, and each month's closing balance becomes the next month's opening balance."),
        CODE("FCFA thousands           Jan     Feb     Mar\n"
             "Cash sales              1 200   1 000   1 500\n"
             "Credit sales received     800     900     700\n"
             "Total inflows           2 000   1 900   2 200\n"
             "Purchases                 900   1 100     800\n"
             "Wages                     600     600     600\n"
             "Rent                      300     300     300\n"
             "New oven                    0     800       0\n"
             "Total outflows          1 800   2 800   1 700\n"
             "Net cash flow             200    -900     500\n"
             "Opening balance           500     700    -200\n"
             "Closing balance           700    -200     300", "text", title="Table 1. Cash flow forecast for a bakery (invented)"),
        EX("Worked example 2: checking and reading Table 1", intro="Check the forecast and say what the bakery should do.", steps=[
            S("January", math=r"2\,000 - 1\,800 = 200; \quad 500 + 200 = 700"),
            S("February", math=r"1\,900 - 2\,800 = -900; \quad 700 - 900 = -200"),
            S("March", math=r"2\,200 - 1\,700 = 500; \quad -200 + 500 = 300"),
            S("Interpret", text="The bakery is short of FCFA 200 000 at the end of February because it pays for the oven in one month. Options: arrange an overdraft of at least FCFA 200 000 now (with a margin), lease or buy the oven on hire purchase, delay the purchase to March, or ask the supplier for credit."),
        ], check=r"500 + 200 - 900 + 500 = 300"),
        KEY("Improving cash flow", "Every method has a cost.", cards=[
            ["Speed up inflows", "Cut credit terms, offer discounts for early payment, factor receivables, sell unused assets, run a sale to clear stock. Cost: lost customers, lower margins."],
            ["Slow down outflows", "Ask suppliers for longer credit, lease instead of buy, delay non-urgent spending. Cost: lost discounts, supplier goodwill."],
            ["Bridge the gap", "Overdraft or short-term loan. Cost: interest and fees."],
            ["Hold less inventory", "JIT and better stock control release cash. Cost: risk of stock-outs."],
        ]),
        T("**Limits of forecasts.** They depend on predicted sales, prices and payment dates; a new competitor, a price rise of inputs or late-paying customers can make them wrong. They are most useful when updated monthly and compared with actual results (variance, see the Budgeting lesson)."),
        MISTAKE("Adding the opening balance to inflows twice", "Opening balance is not an inflow. Net cash flow = inflows − outflows; then closing = opening + net."),
        MISTAKE("Putting depreciation in a cash flow forecast", "Depreciation is not a cash payment. The cash leaves when the asset is paid for."),
        QUIZ("A firm's inventory days are 30, receivable days 50 and payable days 40. How long is its working capital cycle?", ["120 days", "40 days", "60 days", "20 days"], 1,
             "30 + 50 − 40 = 40 days.", hint="Inventory days + receivable days − payable days.",
             feedback=["That adds the payable days instead of subtracting them.", "", "That is 30 + 50 − 20.", "That is 50 − 30."]),
        QUIZ("Which of these causes profit and cash flow to differ?", ["Selling goods on credit", "Paying wages in cash on time", "Cash sales", "Paying rent in the month it is due"], 0,
             "A credit sale counts in revenue (and profit) now but the cash arrives later.", hint="Which item is recorded at one time and paid at another?",
             feedback=["", "Cash wages are recorded and paid at the same time.", "Cash sales bring cash at the same time as the revenue.", "Rent paid when due affects cash and costs together."]),
        TIP("Expect to complete or correct a cash flow forecast and calculate a cycle in Paper 1 and Paper 2; Paper 3 case studies often hide a cash problem behind good profits. Always say what the business should do about a negative balance.", title="Exam link"),
        PQ("Opening balance −150 (FCFA thousands). Inflows: 3 200, 2 800, 3 600. Outflows: 2 900, 3 400, 3 000. Find the closing balance of each month.",
           "Month 1: net +300, closing 150. Month 2: net −600, closing −450. Month 3: net +600, closing 150. The firm needs an overdraft of at least FCFA 450 000 in month 2."),
        PQ("Explain why a fast-growing business may run short of cash even though it is profitable (overtrading).",
           "Growth means buying more stock and paying more wages before the extra sales are paid for, especially if customers get credit. Cash outflows rise before inflows, so the working capital cycle needs more finance. If the firm cannot raise it, it may be unable to pay suppliers and could become insolvent even with a full order book."),
        PQ("Evaluate two ways in which a wholesaler with a 90-day working capital cycle could shorten it. (Short essay plan)",
           "1. Cut receivable days (shorter credit, early-payment discounts, factoring): faster cash, but customers may go to rivals that give credit, and discounts or factor fees cut margins. 2. Cut inventory days (JIT, better forecasting, selling slow stock): releases cash, but risk of stock-outs if suppliers are unreliable. (Also: longer payable days, which may damage supplier relations.) Judgement: depends on market power: a firm with loyal customers can tighten credit; otherwise improve stock control first."),
        SUM("Working capital = current assets − current liabilities; it must be enough, but not excessive.",
            "Cycle = inventory days + receivable days − payable days; a longer cycle needs more working capital.",
            "Profit and cash differ because of credit, asset purchases, depreciation, loans and capital.",
            "Closing balance = opening balance + (inflows − outflows); it becomes the next opening balance.",
            "Improve cash flow by speeding inflows, slowing outflows, holding less stock or arranging finance, each with a cost."),
    ],
))


# ------------------------------------------------------------------ 9. Costs, contribution and break-even analysis
LESSONS.append(lesson(
    module=M_FIN,
    topic="Costs, contribution and break-even analysis",
    title="Cost and profit centres, contribution and break-even analysis",
    slug="bsu-costs-contribution-break-even",
    minutes=22,
    summary="Fixed, variable and semi-variable costs, cost and profit centres, contribution per unit, break-even output and revenue, margin of safety, target profit, the break-even chart, special-order decisions using contribution, and the limits of break-even analysis.",
    objectives=[
        "Classify costs and explain the purpose of cost centres and profit centres",
        "Calculate contribution, break-even output and revenue, margin of safety and the output for a target profit",
        "Draw and read a break-even chart and show the effect of changes in price or costs",
        "Use contribution to decide on a special order and evaluate break-even analysis",
    ],
    key_concepts=["Fixed cost", "Variable cost", "Cost centre", "Profit centre", "Contribution", "Break-even point",
                  "Margin of safety", "Contribution-to-sales ratio", "Special order"],
    blocks=[
        H("Introduction"),
        T("A juice producer in Ebolowa wants to know how many cartons it must sell each month before it makes any profit, and whether to accept a supermarket's request for a large order at a lower price. "
          "Break-even analysis and the idea of **contribution** answer both questions. You met costs and break-even at O Level; here we use them for decisions and evaluate them."),
        D("**Fixed costs** do not change with output in the short run (rent, salaries, loan interest). **Variable costs** change directly with output (materials, piece-rate wages, packaging). **Semi-variable costs** have a fixed and a variable part (a phone or electricity bill with a standing charge).", title="Classifying costs"),
        D("A **cost centre** is a part of a business to which costs can be charged (a department, a machine, a branch). A **profit centre** is a part for which both costs and revenues can be measured, so its profit can be found (a branch, a product line). They help control costs, make managers accountable and motivate through delegation; but sharing out overheads between centres can be arbitrary and centres may compete instead of co-operating.", title="Cost and profit centres"),
        H("Contribution and break-even"),
        D("**Contribution per unit** = selling price − variable cost per unit. Each unit sold 'contributes' this amount first to paying fixed costs, then to profit. Total contribution − fixed costs = profit.", title="Contribution",
          formula=r"\text{Break-even output} = \frac{\text{fixed costs}}{\text{contribution per unit}}"),
        F(r"\text{Margin of safety} = \text{actual (or planned) output} - \text{break-even output}"),
        EX("Worked example 1: the juice producer", intro="Price FCFA 2 500 a carton, variable cost FCFA 1 500 a carton, fixed costs FCFA 4 000 000 a month. Planned sales are 5 500 cartons. Find the break-even output, margin of safety and profit.", steps=[
            S("Contribution per unit", math=r"2\,500 - 1\,500 = 1\,000 \text{ FCFA}"),
            S("Break-even output", math=r"4\,000\,000 \div 1\,000 = 4\,000 \text{ cartons}"),
            S("Margin of safety", math=r"5\,500 - 4\,000 = 1\,500 \text{ cartons} \;(\approx 27\% \text{ of sales})"),
            S("Profit", math=r"1\,500 \times 1\,000 = 1\,500\,000 \text{ FCFA}"),
        ], check=r"5\,500 \times 1\,000 - 4\,000\,000 = 1\,500\,000"),
        IMG("albsu-break-even.svg", alt="Break-even chart: fixed cost horizontal at 4 million; total cost rises from 4 million to 16 million at 8 000 units; revenue rises from 0 to 20 million. They cross at 4 000 units and 10 million. Sales of 5 500 units give a margin of safety of 1 500 units.",
            caption="Figure 1. Break-even chart for the juice producer (invented figures)."),
        T("On the chart, the vertical gap between revenue and total cost is the profit (to the right of break-even) or the loss (to the left). A higher price makes the revenue line steeper and lowers break-even; higher fixed costs shift the total cost line up and raise break-even."),
        EX("Worked example 2: target profit and break-even revenue", intro="The producer wants a profit of FCFA 2 000 000 a month. How many cartons must it sell? What is break-even revenue?", steps=[
            S("Output for a target profit", math=r"\frac{4\,000\,000 + 2\,000\,000}{1\,000} = 6\,000 \text{ cartons}"),
            S("Contribution-to-sales ratio", math=r"1\,000 \div 2\,500 = 0.4"),
            S("Break-even revenue", math=r"4\,000\,000 \div 0.4 = 10\,000\,000 \text{ FCFA} \;(= 4\,000 \times 2\,500)"),
        ]),
        EX("Worked example 3: a special order", intro="A supermarket offers to buy 800 extra cartons at FCFA 2 000 each. The firm has spare capacity and fixed costs will not change. Should it accept?", steps=[
            S("Contribution per carton on the order", math=r"2\,000 - 1\,500 = 500 \text{ FCFA}"),
            S("Extra profit", math=r"800 \times 500 = 400\,000 \text{ FCFA}"),
            S("Qualitative points", text="Accept on financial grounds, since fixed costs are already covered. But check: will regular customers learn of the lower price and ask for it? Is capacity really spare? Could the order lead to more business? Is the price above variable cost after any extra delivery costs?"),
        ]),
        KEY("Evaluating break-even analysis", "Simple and useful, but based on assumptions.", cards=[
            ["Uses", "Quick test of a new product or price change, supports loan applications, shows the margin of safety and the effect of 'what if' changes."],
            ["Limits", "Assumes all output is sold at one price; costs and revenues are straight lines (no bulk discounts or price cuts); fixed costs stay fixed; only one product; data are forecasts."],
        ]),
        MISTAKE("Dividing fixed costs by the price", "Break-even output = fixed costs ÷ CONTRIBUTION per unit, not ÷ price. Using price ignores variable costs and gives a break-even that is far too low."),
        MISTAKE("Rejecting a special order because the price is below full (average) cost", "If capacity is spare and fixed costs do not change, any price above variable cost adds contribution and so adds profit. Then weigh the qualitative effects."),
        QUIZ("Price FCFA 1 200, variable cost FCFA 700, fixed costs FCFA 3 000 000. What is the break-even output?", ["2 500 units", "6 000 units", "4 286 units", "1 579 units"], 1,
             "Contribution = 1 200 − 700 = 500; 3 000 000 ÷ 500 = 6 000 units.", hint="Find the contribution per unit first.",
             feedback=["That divides by the price (3 000 000 ÷ 1 200).", "", "That divides by the variable cost.", "That divides by price PLUS variable cost (1 900) instead of the difference."]),
        QUIZ("Fixed costs rise while price and variable cost stay the same. What happens?", ["Break-even output falls", "Break-even output rises and the margin of safety falls", "Contribution per unit rises", "Nothing changes"], 1,
             "More fixed costs must be covered by the same contribution per unit, so more units are needed to break even.", hint="Which part of the formula changes?",
             feedback=["It rises, not falls.", "", "Contribution per unit depends only on price and variable cost.", "Break-even depends on fixed costs."]),
        TIP("Break-even and contribution calculations are very common in Paper 1 and in data questions of Paper 2 and Paper 3. Show the formula, the substitution and units, and always add a comment on the assumptions or the qualitative factors.", title="Exam link"),
        PQ("Price FCFA 3 000, variable cost FCFA 1 800, fixed costs FCFA 9 600 000 a month, sales 10 000 units. Find break-even output, margin of safety, profit and the output needed for a profit of FCFA 3 600 000.",
           "Contribution = 1 200. Break-even = 9 600 000 ÷ 1 200 = 8 000 units. Margin of safety = 2 000 units. Profit = 2 000 × 1 200 = FCFA 2 400 000. Target: (9 600 000 + 3 600 000) ÷ 1 200 = 11 000 units."),
        PQ("In the previous question, the firm cuts its price to FCFA 2 700 and sales stay at 10 000 units. What happens to break-even and profit?",
           "Contribution falls to 900. Break-even = 9 600 000 ÷ 900 ≈ 10 667 units, above sales. Profit = 10 000 × 900 − 9 600 000 = −FCFA 600 000, a loss. The price cut works only if sales rise above 10 667 units (link to price elasticity of demand)."),
        PQ("Evaluate the usefulness of break-even analysis for a new restaurant in Kribi. (Essay plan)",
           "Explain contribution, break-even, margin of safety. Useful: shows how many meals a day are needed, supports a bank loan, tests prices and costs; simple. Limits: many menu items (an average contribution must be used), demand is seasonal (tourists), costs are not linear (food waste, staff overtime), forecasts may be optimistic. Evaluation: a good starting point if updated with real data and combined with cash flow forecasts and market research. Conclusion."),
        SUM("Fixed costs do not change with output; variable costs do; cost and profit centres help control and accountability.",
            "Contribution per unit = price − variable cost; total contribution − fixed costs = profit.",
            "Break-even output = fixed costs ÷ contribution per unit; margin of safety = sales − break-even output.",
            "Output for a target profit = (fixed costs + target profit) ÷ contribution per unit; break-even revenue = fixed costs ÷ contribution-to-sales ratio.",
            "Accept a special order if it adds contribution and capacity is spare, after weighing qualitative effects; break-even rests on simplifying assumptions."),
    ],
))


# ------------------------------------------------------------------ 10. Budgeting
LESSONS.append(lesson(
    module=M_FIN,
    topic="Budgeting",
    title="Budgeting: setting budgets, flexible budgets and variance analysis",
    slug="bsu-budgeting",
    minutes=21,
    summary="The purposes of budgets, how they are set (incremental and zero-based budgeting), fixed and flexible budgets, calculating and interpreting favourable and adverse variances, and the behavioural benefits and problems of budgeting.",
    objectives=[
        "Explain the purposes of budgeting and the stages of setting a budget",
        "Compare incremental and zero-based budgeting",
        "Flex a budget and calculate favourable and adverse variances",
        "Evaluate budgets as tools for planning, control and motivation",
    ],
    key_concepts=["Budget", "Budget holder", "Incremental budgeting", "Zero-based budgeting", "Fixed budget",
                  "Flexible budget", "Variance", "Favourable variance", "Adverse variance"],
    blocks=[
        H("Introduction"),
        T("A school canteen manager in Bamenda is told she may spend FCFA 2 000 000 on food this term and must sell meals worth FCFA 3 000 000. That is a **budget**: a financial plan for a future period, agreed in advance. "
          "Budgets turn objectives into numbers, give managers targets and let the business compare what happened with what was planned."),
        D("A **budget** is an agreed financial plan of revenue and/or costs for a future period (usually a year, split into months). The **budget holder** is the manager responsible for it, usually the manager of a cost or profit centre.", title="Budget"),
        KEY("Why budget?", "Four purposes.", cards=[
            ["Planning", "Forces managers to think ahead and link spending to objectives."],
            ["Co-ordination", "Sales, production, HR and finance budgets must fit together."],
            ["Control", "Comparing actual with budget (variance analysis) shows where action is needed."],
            ["Motivation", "Agreed targets and delegated authority can motivate budget holders."],
        ]),
        H("Setting budgets"),
        T("The sales budget usually comes first, because sales limit everything else; production, materials, labour, overhead and cash budgets follow, then the master budget. Budgets should be **agreed** with budget holders rather than imposed: imposed budgets often demotivate."),
        D("**Incremental budgeting** takes last year's budget and adds or subtracts a percentage. It is quick but repeats past waste. **Zero-based budgeting** starts each budget from zero: every item must be justified. It removes waste and fits changing priorities but takes much more time and management skill.", title="Incremental or zero-based"),
        H("Fixed and flexible budgets"),
        D("A **fixed budget** is set for one level of output and does not change. A **flexible (flexed) budget** recalculates the budget for the ACTUAL level of output, so that like is compared with like. A **variance** is actual − budget. It is **favourable (F)** if it raises profit (revenue above budget or cost below budget) and **adverse (A)** if it lowers profit.", title="Variances"),
        CODE("FCFA m          Fixed budget   Flexed budget   Actual    Variance\n"
             "                (10 000 units) (11 000 units)  (11 000)  (actual v flexed)\n"
             "Revenue             25.00          27.50        26.95     0.55 A\n"
             "Materials            8.00           8.80         9.20     0.40 A\n"
             "Labour               5.00           5.50         5.39     0.11 F\n"
             "Overheads (fixed)    6.00           6.00         6.30     0.30 A\n"
             "Profit               6.00           7.20         6.06     1.14 A", "text", title="Table 1. A manufacturer's budget and results for one month (invented)"),
        EX("Worked example 1: flexing the budget", intro="Budget: price FCFA 2 500, materials FCFA 800 a unit, labour FCFA 500 a unit, fixed overheads FCFA 6 m, for 10 000 units. Actual output and sales were 11 000 units. Build the flexed budget.", steps=[
            S("Revenue", math=r"11\,000 \times 2\,500 = 27\,500\,000"),
            S("Variable costs", math=r"11\,000 \times 800 = 8\,800\,000; \quad 11\,000 \times 500 = 5\,500\,000"),
            S("Fixed overheads", text="Fixed costs do not change with output: FCFA 6 000 000."),
            S("Flexed profit", math=r"27.5 - 8.8 - 5.5 - 6.0 = 7.2 \text{ m FCFA}"),
        ]),
        EX("Worked example 2: interpreting the variances", intro="Use Table 1. Compare the actual results with the fixed budget and with the flexed budget.", steps=[
            S("Against the fixed budget", math=r"6.06 - 6.00 = 0.06 \text{ m F}", text="It looks as if the month went well."),
            S("Against the flexed budget", math=r"6.06 - 7.20 = -1.14 \text{ m: } 1.14 \text{ m A}"),
            S("Find the causes", text="Revenue 0.55 m A: the price was cut to FCFA 2 450 (26.95 m ÷ 11 000). Materials 0.40 m A: dearer inputs or waste. Labour 0.11 m F: higher productivity. Overheads 0.30 m A: perhaps higher electricity charges."),
            S("Conclusion", text="The fixed budget hid a poor performance: at 11 000 units the firm should have made FCFA 7.2 m. Managers should investigate the price cut and the material cost."),
        ], check=r"-0.55 - 0.40 + 0.11 - 0.30 = -1.14"),
        T("**Evaluation.** A favourable variance is not always good news (lower material cost may mean poorer quality; higher sales may come from an unplanned price cut) and an adverse variance is not always bad (higher spending on training may raise future productivity). Variances show WHERE to look, not WHY. Budgets can also be gamed: managers may pad costs to make targets easy or spend all that is left at year-end so that next year's budget is not cut."),
        MISTAKE("Marking a cost variance as favourable because the number went up", "For costs, actual ABOVE budget is ADVERSE. For revenue and profit, actual above budget is favourable. Always ask: does this raise or lower profit?"),
        MISTAKE("Flexing fixed costs", "Only variable items change in a flexed budget. Fixed overheads stay at the budgeted figure."),
        QUIZ("Budgeted labour cost is FCFA 4 200 000; actual is FCFA 4 500 000. What is the variance?", ["FCFA 300 000 favourable", "FCFA 300 000 adverse", "FCFA 8 700 000 adverse", "No variance, because labour is a variable cost"], 1,
             "Actual cost is above budget by FCFA 300 000, which lowers profit: adverse.", hint="Does spending more than planned raise or lower profit?",
             feedback=["A cost above budget reduces profit, so it is adverse.", "", "That adds the two figures instead of subtracting.", "Variable costs still have variances; the budget may need flexing first."]),
        QUIZ("Which is the main advantage of zero-based budgeting?", ["It is quicker to prepare than incremental budgeting", "Every item of spending must be justified, so waste is cut", "It needs no input from managers", "It never changes from year to year"], 1,
             "Starting from zero forces managers to justify each item, which removes spending that only continues out of habit.", hint="What does 'starting from zero' force managers to do?",
             feedback=["It is slower: every item must be justified.", "", "It needs a lot of manager time and skill.", "It is rebuilt from zero each period."]),
        TIP("Variance tables appear in Paper 1 and in data questions in Paper 2 and Paper 3. Label each variance F or A, flex the budget where output changed, and explain possible causes before recommending action.", title="Exam link"),
        PQ("Budgeted sales revenue FCFA 18 m, actual FCFA 16.5 m; budgeted materials FCFA 6 m, actual FCFA 5.4 m; budgeted wages FCFA 4 m, actual FCFA 4.3 m. Calculate each variance and the net effect on profit.",
           "Revenue: 1.5 m A. Materials: 0.6 m F. Wages: 0.3 m A. Net effect on profit: −1.5 + 0.6 − 0.3 = −1.2 m, so profit is FCFA 1.2 m below budget (adverse). If output fell, the budget should be flexed before judging the cost variances."),
        PQ("Explain why a flexible budget gives a fairer basis than a fixed budget for judging a production manager.",
           "If output differs from plan, variable costs must differ too. A fixed budget would show adverse cost variances when output rises (and favourable ones when it falls) that have nothing to do with efficiency. Flexing the budget to actual output compares actual costs with what they should have been at that output, so the variances measure the manager's control of prices and usage."),
        PQ("Evaluate the view that budgets do more harm than good to employee motivation. (Essay plan)",
           "For harm: imposed or unrealistic budgets demotivate; focus on short-term targets; padding and year-end spending; blame culture over adverse variances. Against: agreed budgets give clear targets (link to goal-setting and Drucker's management by objectives), delegate authority (Herzberg's responsibility), and recognise success; variances guide help, not punishment. Evaluation: depends on how budgets are set (participation), whether they are flexible and how variances are used (support or blame). Conclusion."),
        SUM("A budget is an agreed financial plan; it serves planning, co-ordination, control and motivation.",
            "Incremental budgeting adjusts last year's figures; zero-based budgeting justifies every item from zero.",
            "A flexible budget recalculates variable items for actual output; fixed costs stay unchanged.",
            "Variance = actual − budget; favourable if it raises profit, adverse if it lowers profit.",
            "Variances show where to look, not why; participation and fair use decide whether budgets motivate."),
    ],
))


# ------------------------------------------------------------------ 11. Financial statements
LESSONS.append(lesson(
    module=M_FSA,
    topic="Financial statements",
    title="Reading the income statement and the statement of financial position",
    slug="bsu-financial-statements",
    minutes=21,
    summary="The purpose and users of financial statements, the structure of the income statement and the statement of financial position (balance sheet), how they link, the effect of depreciation, and the limits of published accounts.",
    objectives=[
        "Identify the users of financial statements and what each wants to know",
        "Build and read an income statement from revenue to retained profit",
        "Build and read a statement of financial position and calculate capital employed",
        "Explain the effect of depreciation and evaluate the limits of published accounts",
    ],
    key_concepts=["Income statement", "Gross profit", "Operating profit", "Profit for the year", "Statement of financial position",
                  "Non-current assets", "Current assets", "Current liabilities", "Equity", "Capital employed", "Depreciation"],
    blocks=[
        H("Introduction"),
        T("Ndole Foods SA (an invented company) makes packaged foods. Its shareholders, bank, suppliers, workers and the tax office all read its yearly accounts, but they look for different things. "
          "Before you can calculate ratios (next lesson) you must know where each figure comes from. In Cameroon, companies prepare accounts under the OHADA accounting system (SYSCOHADA), whose layouts and headings differ from the international format used in many textbooks; the ideas are the same. This lesson uses the simpler textbook layout: check your textbook for the SYSCOHADA version."),
        KEY("Users and their interests", "Link each user to a question.", cards=[
            ["Shareholders", "Is the company profitable, and will dividends and the share price grow?"],
            ["Banks and lenders", "Can it pay interest and repay loans (liquidity, gearing)?"],
            ["Suppliers", "Will it pay its bills on time?"],
            ["Employees and unions", "Is it secure, and can it afford pay rises?"],
            ["Government", "How much tax is due? Is it complying with the law?"],
        ]),
        H("The income statement"),
        D("The **income statement** shows revenue and costs over a period (usually a year) and the resulting profit. **Gross profit** = revenue − cost of sales. **Operating profit** = gross profit − operating expenses (distribution and administration). **Profit before tax** = operating profit − finance costs (interest). **Profit for the year** = profit before tax − tax. Profit for the year is paid out as dividends or kept as **retained profit**.", title="Income statement"),
        CODE("Ndole Foods SA: income statement for the year (FCFA m)\n"
             "Revenue                          800\n"
             "Cost of sales                   (480)\n"
             "Gross profit                     320\n"
             "Operating expenses              (200)\n"
             "Operating profit                 120\n"
             "Finance costs                    (20)\n"
             "Profit before tax                100\n"
             "Tax (teaching value 30%)          (30)\n"
             "Profit for the year               70\n"
             "Dividends paid                   (28)\n"
             "Retained profit for the year      42", "text", title="Table 1. Income statement (invented figures)"),
        EX("Worked example 1: building the income statement", intro="Using the figures in Table 1, show how each profit line is found.", steps=[
            S("Gross profit", math=r"800 - 480 = 320"),
            S("Operating profit", math=r"320 - 200 = 120"),
            S("Profit before tax", math=r"120 - 20 = 100"),
            S("Profit for the year", math=r"100 - 0.30 \times 100 = 70", text="30% is a teaching value: check the current company tax rate in the Finance Law."),
            S("Retained profit", math=r"70 - 28 = 42"),
        ]),
        H("The statement of financial position"),
        D("The **statement of financial position** (balance sheet) shows what a business owns (assets) and owes (liabilities) at one date, and the owners' stake (**equity**). **Non-current assets** are kept for more than a year (land, buildings, machines, vehicles). **Current assets** are expected to turn into cash within a year (inventory, receivables, cash). **Current liabilities** are due within a year (payables, overdraft). **Non-current liabilities** are due after a year (long-term loans, bonds).", title="Statement of financial position",
          formula=r"\text{Total assets} - \text{total liabilities} = \text{equity}"),
        CODE("Ndole Foods SA: statement of financial position at year end (FCFA m)\n"
             "Non-current assets                         600\n"
             "Inventory                   90\n"
             "Trade receivables          100\n"
             "Cash                        30\n"
             "Current assets                             220\n"
             "Total assets                               820\n"
             "Trade payables              80\n"
             "Bank overdraft              40\n"
             "Current liabilities                       (120)\n"
             "Non-current liabilities (loans)           (200)\n"
             "Net assets                                 500\n"
             "Share capital (20 m shares)                200\n"
             "Retained earnings                          300\n"
             "Equity                                     500", "text", title="Table 2. Statement of financial position (invented figures)"),
        EX("Worked example 2: equity and capital employed", intro="Use Table 2 to find equity, working capital and capital employed.", steps=[
            S("Equity", math=r"820 - 120 - 200 = 500 \text{ m FCFA}"),
            S("Working capital", math=r"220 - 120 = 100 \text{ m FCFA}"),
            S("Capital employed", math=r"\text{equity} + \text{non-current liabilities} = 500 + 200 = 700 \text{ m FCFA}"),
            S("Link", text="The FCFA 42 m retained this year is part of the retained earnings of 300 in equity: the two statements are linked."),
        ], check=r"600 + 100 = 700 = 500 + 200"),
        H("Depreciation"),
        T("**Depreciation** spreads the cost of a non-current asset over its useful life. With the straight-line method, yearly depreciation = (cost − residual value) ÷ useful life. It is an expense in the income statement (lowering profit) and reduces the asset's value in the statement of financial position, but it is not a cash payment."),
        EX("Worked example 3: straight-line depreciation", intro="A packing machine costs FCFA 50 m, will last 5 years and can then be sold for FCFA 10 m. Find the yearly depreciation and the book value after 2 years.", steps=[
            S("Yearly depreciation", math=r"\frac{50 - 10}{5} = 8 \text{ m FCFA}"),
            S("Book value after 2 years", math=r"50 - 2 \times 8 = 34 \text{ m FCFA}"),
        ]),
        KEY("Limits of published accounts", "Use them with care.", cards=[
            ["Historical", "They show the past, not the future."],
            ["Judgements", "Depreciation, inventory values and provisions involve estimates; window dressing can make a year look better (for example selling an asset just before the year end to raise cash)."],
            ["What is missing", "Staff skills, brand, customer loyalty, environmental impact and the market position are not shown in full."],
            ["Inflation and one date", "A balance sheet is a snapshot of one day, which may not be typical."],
        ]),
        MISTAKE("Mixing up profit for the year and retained profit", "Profit for the year is after tax; retained profit is what is left after dividends. Shareholders' dividends come out of profit for the year."),
        MISTAKE("Treating depreciation as cash", "Depreciation lowers profit but no cash leaves the business when it is charged; the cash left when the asset was bought."),
        QUIZ("Revenue FCFA 500 m, cost of sales FCFA 300 m, operating expenses FCFA 120 m. What is operating profit?", ["FCFA 200 m", "FCFA 80 m", "FCFA 380 m", "FCFA 420 m"], 1,
             "Gross profit = 500 − 300 = 200; operating profit = 200 − 120 = 80.", hint="Find gross profit first.",
             feedback=["That is gross profit.", "", "That is revenue − operating expenses only.", "That is cost of sales + operating expenses."]),
        QUIZ("Which item is a current liability?", ["A five-year bank loan", "Trade payables", "Inventory", "Share capital"], 1,
             "Trade payables are owed to suppliers and due within a year.", hint="What does the business owe and must pay within a year?",
             feedback=["A five-year loan is a non-current liability (except the part due within a year).", "", "Inventory is a current asset.", "Share capital is part of equity."]),
        TIP("You will rarely be asked to prepare full accounts in Business Studies, but Paper 1 tests the structure (which line is which), and Paper 2 and Paper 3 give extracts to analyse. Know where each figure for the ratios comes from.", title="Exam link"),
        PQ("Revenue FCFA 1 200 m, cost of sales FCFA 700 m, operating expenses FCFA 330 m, finance costs FCFA 30 m, tax FCFA 42 m, dividends FCFA 50 m. Calculate gross profit, operating profit, profit for the year and retained profit.",
           "Gross profit = 500. Operating profit = 500 − 330 = 170. Profit before tax = 170 − 30 = 140. Profit for the year = 140 − 42 = 98. Retained profit = 98 − 50 = FCFA 48 m."),
        PQ("Non-current assets FCFA 450 m, current assets FCFA 180 m, current liabilities FCFA 110 m, non-current liabilities FCFA 150 m. Calculate equity and capital employed.",
           "Equity = 450 + 180 − 110 − 150 = FCFA 370 m. Capital employed = 370 + 150 = FCFA 520 m (also = non-current assets + working capital = 450 + 70)."),
        PQ("A bank is deciding whether to lend to a company. Explain which parts of the financial statements it will study and why, and one limitation of relying on them.",
           "It will study liquidity (current assets against current liabilities, cash), gearing (non-current liabilities against capital employed), the ability to pay interest (operating profit against finance costs) and the trend in profit. Limitation: the statements are historical and may be window-dressed; the bank should also ask for cash flow forecasts and look at security."),
        SUM("Financial statements serve shareholders, lenders, suppliers, employees and government, each with different questions.",
            "Income statement: revenue − cost of sales = gross profit; − expenses = operating profit; − interest − tax = profit for the year; − dividends = retained profit.",
            "Statement of financial position: assets − liabilities = equity; capital employed = equity + non-current liabilities.",
            "Depreciation spreads an asset's cost over its life; it lowers profit but is not a cash flow.",
            "Accounts are historical, involve judgement and leave out important non-financial information."),
    ],
))


# ------------------------------------------------------------------ 12. Ratio analysis
LESSONS.append(lesson(
    module=M_FSA,
    topic="Ratio analysis",
    title="Ratio analysis: profitability, liquidity, efficiency, gearing and shareholder ratios",
    slug="bsu-ratio-analysis",
    minutes=22,
    summary="Calculating and interpreting profitability (margins, ROCE), liquidity (current and acid test), efficiency (inventory turnover, receivable and payable days), gearing and shareholder ratios (EPS, dividend yield, cover, P/E), and the limits of ratio analysis.",
    objectives=[
        "Calculate the main profitability, liquidity, efficiency, gearing and shareholder ratios",
        "Interpret ratios by comparing them over time and with other firms",
        "Suggest ways to improve weak ratios and the possible drawbacks",
        "Evaluate the usefulness and limits of ratio analysis",
    ],
    key_concepts=["Gross profit margin", "Operating profit margin", "Return on capital employed (ROCE)", "Current ratio",
                  "Acid test ratio", "Inventory turnover", "Receivable days", "Payable days", "Gearing",
                  "Earnings per share", "Dividend yield", "Price/earnings ratio"],
    blocks=[
        H("Introduction"),
        T("A single figure, such as a profit of FCFA 120 m, tells you little: is that good for a firm of this size? Ratios compare one figure with another so that performance can be judged over time and against other firms. "
          "We use the accounts of Ndole Foods SA from the previous lesson (revenue 800, cost of sales 480, gross profit 320, operating profit 120, profit for the year 70, dividends 28; inventory 90, receivables 100, cash 30, current assets 220, payables 80, current liabilities 120, non-current liabilities 200, equity 500, capital employed 700, all FCFA m; 20 m shares; share price FCFA 42 000)."),
        H("Profitability"),
        D("**Gross profit margin** = gross profit ÷ revenue × 100. **Operating profit margin** = operating profit ÷ revenue × 100. **Return on capital employed (ROCE)** = operating profit ÷ capital employed × 100: the return the business makes on all its long-term finance. Check your textbook: some books use profit before interest and tax, which is the same as operating profit here.", title="Profitability ratios"),
        EX("Worked example 1: profitability", intro="Calculate the gross profit margin, operating profit margin and ROCE of Ndole Foods.", steps=[
            S("Gross profit margin", math=r"\frac{320}{800} \times 100 = 40\%"),
            S("Operating profit margin", math=r"\frac{120}{800} \times 100 = 15\%"),
            S("ROCE", math=r"\frac{120}{700} \times 100 \approx 17.1\%"),
            S("Interpret", text="Last year (invented) the gross margin was 42% and ROCE 19%: margins have narrowed, perhaps because input costs rose faster than prices. ROCE is well above a bank deposit rate, but compare it with competitors and the cost of borrowing."),
        ]),
        H("Liquidity"),
        D("**Current ratio** = current assets ÷ current liabilities. **Acid test (quick) ratio** = (current assets − inventory) ÷ current liabilities: it leaves out inventory because stock may be hard to sell quickly. Textbooks often suggest about 1.5 to 2 for the current ratio and about 1 for the acid test, but the right level depends on the industry (supermarkets sell for cash and run lower ratios).", title="Liquidity ratios"),
        EX("Worked example 2: liquidity", intro="Calculate the current and acid test ratios.", steps=[
            S("Current ratio", math=r"\frac{220}{120} \approx 1.83"),
            S("Acid test ratio", math=r"\frac{220 - 90}{120} = \frac{130}{120} \approx 1.08"),
            S("Interpret", text="Both are in the usual safe range, and better than last year (invented: 1.5 and 0.9). Too high a ratio would suggest idle cash or excess stock."),
        ]),
        H("Efficiency"),
        D("**Inventory turnover** = cost of sales ÷ average (or closing) inventory (times a year); inventory days = inventory ÷ cost of sales × 365. **Receivable days** = trade receivables ÷ revenue × 365. **Payable days** = trade payables ÷ cost of sales (or purchases) × 365. **Asset turnover** = revenue ÷ capital employed (some books use total assets). Check your textbook for the exact versions it uses.", title="Efficiency ratios"),
        EX("Worked example 3: efficiency", intro="Calculate inventory turnover, receivable days, payable days and asset turnover.", steps=[
            S("Inventory turnover", math=r"\frac{480}{90} \approx 5.3 \text{ times a year (about 68 days)}"),
            S("Receivable days", math=r"\frac{100}{800} \times 365 \approx 45.6 \text{ days}"),
            S("Payable days", math=r"\frac{80}{480} \times 365 \approx 60.8 \text{ days}"),
            S("Asset turnover", math=r"\frac{800}{700} \approx 1.14 \text{ times}"),
            S("Interpret", text="Customers pay in about 46 days while Ndole pays suppliers in about 61: good for cash flow, as long as suppliers accept it. Holding 68 days of stock is long for food; JIT or better forecasting could release cash."),
        ]),
        H("Gearing and shareholder ratios"),
        D("**Gearing** = non-current liabilities ÷ capital employed × 100. **Earnings per share (EPS)** = profit for the year ÷ number of shares. **Dividend per share (DPS)** = total dividends ÷ number of shares. **Dividend yield** = DPS ÷ share price × 100. **Dividend cover** = profit for the year ÷ dividends. **Price/earnings (P/E) ratio** = share price ÷ EPS.", title="Gearing and investor ratios"),
        EX("Worked example 4: gearing and shareholder ratios", intro="Calculate gearing, EPS, DPS, dividend yield, dividend cover and the P/E ratio.", steps=[
            S("Gearing", math=r"\frac{200}{700} \times 100 \approx 28.6\%"),
            S("EPS and DPS", math=r"\frac{70\,000\,000}{20\,000\,000} = 3\,500 \text{ FCFA}; \quad \frac{28\,000\,000}{20\,000\,000} = 1\,400 \text{ FCFA}"),
            S("Dividend yield and cover", math=r"\frac{1\,400}{42\,000} \times 100 \approx 3.3\%; \quad \frac{70}{28} = 2.5 \text{ times}"),
            S("P/E ratio", math=r"\frac{42\,000}{3\,500} = 12"),
            S("Interpret", text="Low gearing gives room to borrow. Investors pay 12 times current earnings, which suggests they expect growth; the dividend is covered 2.5 times, so it looks safe."),
        ]),
        KEY("Evaluating ratio analysis", "Ratios raise questions; they rarely answer them.", cards=[
            ["Need comparisons", "A ratio means little alone: compare with past years, competitors and industry averages."],
            ["Data limits", "Accounts are historical, may be window-dressed, and firms may use different accounting policies."],
            ["Missing factors", "Ratios ignore quality, staff morale, brand, the economy and the competitive situation."],
            ["Interpretation", "A lower margin may be a deliberate strategy (price cuts to win market share)."],
        ]),
        MISTAKE("Calculating ROCE with profit for the year", "ROCE uses OPERATING profit (before interest and tax), because capital employed includes loans as well as equity."),
        MISTAKE("Giving ratios without units or interpretation", "Margins and ROCE are percentages, liquidity ratios are 'x : 1' or a number, turnover is 'times', receivable days are days. Then say what the figure means and compare it."),
        QUIZ("Current assets FCFA 150 m, of which inventory FCFA 60 m; current liabilities FCFA 100 m. What is the acid test ratio?", ["1.5", "0.9", "0.6", "2.5"], 1,
             "(150 − 60) ÷ 100 = 0.9.", hint="Take inventory out of current assets first.",
             feedback=["That is the current ratio.", "", "That is inventory ÷ current liabilities.", "That is 150 ÷ 60."]),
        QUIZ("Receivable days rise from 30 to 55. What is the most likely effect?", ["Cash flow improves", "Cash flow worsens, because customers take longer to pay", "Gross profit margin falls", "Gearing rises"], 1,
             "More days means cash is collected later, so less cash is available.", hint="What do receivable days measure?",
             feedback=["Slower collection worsens cash flow.", "", "Gross margin depends on price and cost of sales, not on collection.", "Gearing depends on long-term borrowing."]),
        TIP("Ratio questions are common in all three papers: Paper 1 asks for one ratio from data; Paper 2 and Paper 3 ask you to calculate several and judge performance. Show formula, working and unit, compare, explain causes and suggest improvements with their drawbacks.", title="Exam link"),
        PQ("A company has operating profit FCFA 90 m, revenue FCFA 600 m, equity FCFA 400 m and non-current liabilities FCFA 200 m. Calculate the operating margin, ROCE and gearing.",
           "Operating margin = 90 ÷ 600 × 100 = 15%. Capital employed = 600, so ROCE = 90 ÷ 600 × 100 = 15%. Gearing = 200 ÷ 600 × 100 ≈ 33.3%."),
        PQ("Profit for the year FCFA 54 m, 18 m shares, dividends FCFA 27 m, share price FCFA 30 000. Calculate EPS, dividend per share, dividend yield, dividend cover and P/E ratio.",
           "EPS = 54 m ÷ 18 m = FCFA 3 000. DPS = 27 m ÷ 18 m = FCFA 1 500. Dividend yield = 1 500 ÷ 30 000 × 100 = 5%. Dividend cover = 54 ÷ 27 = 2 times. P/E = 30 000 ÷ 3 000 = 10."),
        PQ("Ndole Foods' ROCE has fallen from 19% to 17.1% while its current ratio rose from 1.5 to 1.83. Discuss what the directors might do and how far ratios alone can guide them. (Essay plan)",
           "Analyse: lower margins (gross 42% to 40%) pulled ROCE down; liquidity improved, possibly because more cash or stock is held. Actions: raise prices or cut cost of sales (supplier negotiation, waste reduction), use idle current assets more productively (cut 68 days of stock), sell under-used assets. Limits: ratios do not show the cause (input prices, competition, deliberate price strategy), need industry comparisons, are historical. Judgement: use ratios to identify questions, then investigate with market and operational data."),
        SUM("Profitability: gross margin, operating margin and ROCE (operating profit ÷ capital employed).",
            "Liquidity: current ratio and acid test (current assets less inventory, over current liabilities).",
            "Efficiency: inventory turnover, receivable days, payable days and asset turnover.",
            "Gearing and investor ratios: gearing, EPS, DPS, dividend yield, dividend cover and P/E.",
            "Ratios need comparison and interpretation, and they leave out non-financial factors."),
    ],
))


# ------------------------------------------------------------------ 13. Investment appraisal
LESSONS.append(lesson(
    module=M_FSA,
    topic="Investment appraisal",
    title="Investment appraisal: payback, ARR, NPV and IRR",
    slug="bsu-investment-appraisal",
    minutes=22,
    summary="Appraising a capital investment with payback, the average rate of return, net present value (discounted cash flow) and the internal rate of return, comparing projects whose methods disagree, and weighing the qualitative factors and risks behind the forecasts.",
    objectives=[
        "Calculate the payback period and the average rate of return (ARR)",
        "Explain discounting and calculate net present value (NPV) from discount factors",
        "Estimate the internal rate of return (IRR) by interpolation and interpret it",
        "Evaluate the methods and the qualitative factors in an investment decision",
    ],
    key_concepts=["Investment appraisal", "Payback period", "Average rate of return (ARR)", "Time value of money",
                  "Discount factor", "Net present value (NPV)", "Internal rate of return (IRR)", "Qualitative factors"],
    blocks=[
        H("Introduction"),
        T("A rice mill in the North West must choose between two new machines, each costing FCFA 50 m. The money is spent now, but the returns arrive over several years and are only forecasts. "
          "**Investment appraisal** uses quantitative methods to judge whether a capital project is worth it and which of several is best. A Level questions expect you to calculate, compare and then judge."),
        CODE("FCFA m          Year 0   Year 1   Year 2   Year 3   Year 4   Total inflows\n"
             "Machine A        (50)      15       20       20       15          70\n"
             "Machine B        (50)       5       10       25       40          80", "text", title="Table 1. Forecast net cash flows (invented)"),
        H("Payback"),
        D("The **payback period** is the time a project takes to repay its initial cost from its net cash inflows. Shorter is better. It is simple and stresses liquidity and lower risk, but it ignores cash flows after payback and the timing of money within the period.", title="Payback"),
        EX("Worked example 1: payback of A and B", intro="Use cumulative cash flows.", steps=[
            S("A: cumulative", math=r"-50,\; -35,\; -15,\; +5", text="Payback falls in year 3."),
            S("A: part of year 3", math=r"2 + \frac{15}{20} = 2.75 \text{ years (2 years 9 months)}"),
            S("B: cumulative", math=r"-50,\; -45,\; -35,\; -10,\; +30"),
            S("B: part of year 4", math=r"3 + \frac{10}{40} = 3.25 \text{ years (3 years 3 months)}"),
        ]),
        H("Average rate of return"),
        D("The **average (accounting) rate of return** = average yearly profit ÷ initial investment × 100, where average yearly profit = (total inflows − cost) ÷ number of years. It uses all the cash flows but ignores timing. Check your textbook: some use the average investment ((cost + residual value) ÷ 2) as the denominator, which gives a higher figure.", title="ARR",
          formula=r"ARR = \frac{(\text{total net inflows} - \text{cost}) \div \text{years}}{\text{initial cost}} \times 100"),
        EX("Worked example 2: ARR", intro="Calculate the ARR of A and B on initial cost.", steps=[
            S("A", math=r"\frac{(70 - 50) \div 4}{50} \times 100 = \frac{5}{50} \times 100 = 10\%"),
            S("B", math=r"\frac{(80 - 50) \div 4}{50} \times 100 = \frac{7.5}{50} \times 100 = 15\%"),
        ]),
        H("Discounted cash flow: NPV"),
        D(r"Money received in the future is worth less than the same sum today, because today's money could earn interest (the **time value of money**) and future sums are less certain. **Discounting** turns future cash into its **present value**: multiply by a discount factor $1 \div (1 + r)^n$, where r is the discount rate (often the cost of borrowing) and n the year. **Net present value** = sum of present values of inflows − initial cost. A positive NPV means the project earns more than the discount rate.", title="Net present value"),
        CODE("Year                    1       2       3       4\n"
             "Discount factor 10%   0.909   0.826   0.751   0.683\n"
             "Discount factor 15%   0.870   0.756   0.658   0.572", "text", title="Table 2. Discount factors (rounded to 3 decimal places)"),
        EX("Worked example 3: NPV at 10%", intro="Calculate the NPV of A and B at a discount rate of 10%.", steps=[
            S("A: present values", math=r"15(0.909) + 20(0.826) + 20(0.751) + 15(0.683) = 13.635 + 16.52 + 15.02 + 10.245 = 55.42"),
            S("A: NPV", math=r"55.42 - 50 = +5.42 \text{ m FCFA}"),
            S("B: present values", math=r"5(0.909) + 10(0.826) + 25(0.751) + 40(0.683) = 4.545 + 8.26 + 18.775 + 27.32 = 58.90"),
            S("B: NPV", math=r"58.90 - 50 = +8.90 \text{ m FCFA}"),
        ]),
        H("Internal rate of return"),
        D("The **internal rate of return** is the discount rate at which NPV = 0. If the IRR is above the cost of finance, the project is worth doing. It can be estimated by **linear interpolation** between a rate with a positive NPV and a rate with a negative NPV.", title="IRR",
          formula=r"IRR \approx r_1 + \frac{NPV_1}{NPV_1 - NPV_2}(r_2 - r_1)"),
        EX("Worked example 4: IRR of machine A", intro="At 15% the NPV of A is 15(0.870) + 20(0.756) + 20(0.658) + 15(0.572) − 50 = −0.09. Estimate the IRR.", steps=[
            S("Interpolate", math=r"IRR \approx 10 + \frac{5.42}{5.42 - (-0.09)} \times 5 = 10 + \frac{5.42}{5.51} \times 5 \approx 14.9\%"),
            S("Interpret", text="If the mill can borrow at, say, 12%, machine A clears that hurdle. (By the same method, B's IRR is about 15.9%.)"),
        ], check=r"NPV_A(14.9\%) \approx 0"),
        KEY("When the methods disagree", "A pays back sooner; B has the higher ARR, NPV and IRR.", cards=[
            ["Choose A if", "Cash is short, the future is very uncertain (later forecasts are riskier), or the technology may soon be out of date."],
            ["Choose B if", "The firm can wait for returns and trusts the later forecasts: NPV is usually seen as the best guide to value."],
            ["Qualitative factors", "Fit with objectives and strategy, effect on staff and community, reliability of the supplier, environmental impact, the economy, and how reliable the forecasts are."],
        ]),
        MISTAKE("Discounting the year 0 cost", "The initial cost is paid now: its discount factor is 1. Only future cash flows are discounted."),
        MISTAKE("Saying a positive NPV means the project will make a profit", "It means that, IF the forecasts are right, the project earns more than the discount rate. Forecasts can be wrong: always comment on risk."),
        QUIZ("A project costs FCFA 24 m and earns FCFA 8 m a year. What is its payback period?", ["2 years", "3 years", "4 years", "0.33 years"], 1,
             "24 ÷ 8 = 3 years.", hint="How many years of FCFA 8 m are needed to reach FCFA 24 m?",
             feedback=["After 2 years only FCFA 16 m has been repaid.", "", "That is one year too many.", "That is 8 ÷ 24, the fraction upside down."]),
        QUIZ("At a 12% discount rate a project's NPV is FCFA −2 m. What does this suggest?", ["The project returns more than 12%", "The project returns less than 12%, so its IRR is below 12%", "The project will certainly make a loss", "The payback period is negative"], 1,
             "A negative NPV at 12% means the present value of inflows is below the cost, so the return is below 12%.", hint="What does NPV compare the project's return with?",
             feedback=["That would give a positive NPV.", "", "It may still make an accounting profit, just less than 12% a year.", "Payback cannot be negative; it is a different measure."]),
        TIP("Investment appraisal calculations are very likely in Paper 1 (one method), Paper 2 data questions and Paper 3 case studies (several methods and a recommendation). Discount factors are usually given. Finish with a judgement that uses the qualitative factors and the risk of the forecasts.", title="Exam link"),
        PQ("A van costs FCFA 30 m and is forecast to add FCFA 12 m a year to net cash flow for 4 years. Discount factors at 8%: 0.926, 0.857, 0.794, 0.735. Calculate the payback period, ARR (on initial cost) and NPV.",
           "Payback = 30 ÷ 12 = 2.5 years. ARR: average profit = (48 − 30) ÷ 4 = 4.5; 4.5 ÷ 30 × 100 = 15%. NPV = 12 × (0.926 + 0.857 + 0.794 + 0.735) − 30 = 12 × 3.312 − 30 = 39.744 − 30 = +FCFA 9.744 m."),
        PQ("A project has an NPV of +FCFA 6 m at 10% and −FCFA 2 m at 18%. Estimate its IRR.",
           "IRR ≈ 10 + 6 ÷ (6 + 2) × 8 = 10 + 6 = 16%."),
        PQ("Evaluate whether a company should rely on NPV alone when deciding to build a new factory. (Essay plan)",
           "NPV strengths: uses all cash flows, allows for the time value of money, gives a money value of the gain. Limits: the forecasts of sales, costs and the right discount rate are uncertain, especially 5 to 10 years ahead; NPV ignores how quickly cash returns (liquidity), which payback shows; qualitative factors (strategy, staff, community, environment, government policy) are left out. Use sensitivity analysis (what if sales are 10% lower?) and several methods. Conclusion: NPV is the best single method but should not be used alone."),
        SUM("Payback = time to recover the cost; simple, stresses liquidity and risk, ignores later cash and timing.",
            "ARR = average yearly profit ÷ initial cost × 100; uses all flows, ignores timing (check the denominator your textbook uses).",
            "NPV = present value of inflows − cost; positive NPV means the project beats the discount rate.",
            "IRR is the rate at which NPV = 0; estimate it by interpolation and compare it with the cost of finance.",
            "Methods can disagree; forecasts are uncertain, so add sensitivity analysis and qualitative factors."),
    ],
))


# ------------------------------------------------------------------ 14. Strategic analysis
LESSONS.append(lesson(
    module=M_STR,
    topic="Strategic analysis",
    title="Strategic analysis: SWOT, Porter's five forces and core competencies",
    slug="bsu-strategic-analysis",
    minutes=22,
    summary="How strategy is formed (mission, objectives, levels of strategy) and the tools of strategic analysis: SWOT, PESTLE as the external input, Porter's five forces of industry competition and core competencies, with their uses and limits.",
    objectives=[
        "Explain the difference between strategy and tactics and the levels of strategy",
        "Carry out a SWOT analysis that separates internal and external factors and draws conclusions",
        "Use Porter's five forces to judge how attractive an industry is",
        "Explain core competencies and evaluate the limits of strategic analysis tools",
    ],
    key_concepts=["Strategy", "Tactics", "Mission statement", "SWOT analysis", "PESTLE", "Porter's five forces",
                  "Barriers to entry", "Core competence", "Competitive advantage"],
    blocks=[
        H("Introduction"),
        T("A Cameroonian bottled-water company is thinking about expanding into soft drinks. Before it decides, it must understand its own position and its environment. "
          "**Strategic management** has three stages: **analysis** (where are we now?), **choice** (where do we want to be and how will we get there?) and **implementation** (making it happen and managing change). This lesson covers analysis; the next lessons cover choice and change."),
        D("A **strategy** is a long-term plan to achieve the objectives of the whole organisation, involving major resources and hard to reverse. **Tactics** are short-term, smaller-scale actions that carry out the strategy (a price promotion, a new advert). Strategy is set at three levels: **corporate** (which markets and industries to be in), **business** (how to compete in each market) and **functional** (marketing, operations, finance and HR plans).", title="Strategy and tactics"),
        T("Strategy starts from the **mission** (the purpose of the organisation, often published as a mission statement) and the **corporate objectives** (measurable targets such as market share, growth or return on capital), which in turn guide the strategy."),
        H("SWOT analysis"),
        D("**SWOT** lists the internal **Strengths** and **Weaknesses** of the business (within its control: brand, staff, finance, technology, costs) and the external **Opportunities** and **Threats** (outside its control: markets, competitors, the economy, laws). External factors are usually found with a **PESTLE** analysis (political, economic, social, technological, legal, environmental), which you met in Lower Sixth.", title="SWOT"),
        EX("Worked example 1: SWOT for the water company", intro="Sort these points into SWOT and draw a conclusion: well-known local brand; one ageing bottling line; growing urban population; new imported brands entering; strong distribution to small shops; possible rise in import duties on plastic preforms (check the current rules).", steps=[
            S("Strengths (internal)", text="Well-known local brand; strong distribution network to small shops."),
            S("Weaknesses (internal)", text="One ageing bottling line: risk of breakdowns, limited capacity."),
            S("Opportunities (external)", text="Growing urban population raises demand for packaged drinks."),
            S("Threats (external)", text="New imported brands; higher cost of plastic inputs if duties rise."),
            S("Conclusion", text="Use the brand and distribution (strengths) to capture urban growth (opportunity), but first invest in capacity (weakness) and secure input supply (threat). A SWOT is useful only when it leads to such conclusions."),
        ]),
        H("Porter's five forces"),
        T("Michael Porter's **five forces** model analyses the competitive environment of an industry. The stronger the forces, the more intense the competition and the lower the profit potential of the industry."),
        IMG("albsu-five-forces.svg", alt="Porter's five forces: rivalry among existing firms in the centre, with arrows from the threat of new entrants (top), the threat of substitutes (bottom), the bargaining power of suppliers (left) and the bargaining power of buyers (right).",
            caption="Figure 1. Porter's five forces."),
        KEY("What makes each force strong?", "Use these in an analysis.", cards=[
            ["New entrants", "Strong when barriers to entry are low: little capital needed, no brand loyalty, easy access to distribution, no licences."],
            ["Substitutes", "Strong when other products meet the same need cheaply (sachet water, tap water, juices for bottled water)."],
            ["Suppliers", "Strong when there are few suppliers, inputs are unique, or switching supplier is costly."],
            ["Buyers", "Strong when buyers are few and large (supermarkets, government), products are standard and switching is easy."],
            ["Rivalry", "Strong when there are many similar firms, slow market growth, high fixed costs and little product differentiation."],
        ]),
        EX("Worked example 2: rating the soft-drinks industry", intro="The firm scores each force from 1 (weak) to 5 (strong) for the soft-drinks market: new entrants 2 (big brands, costly bottling plants), substitutes 4 (juices, water, local drinks), suppliers 3 (sugar and packaging from few sources), buyers 3 (many small shops, but large distributors), rivalry 5 (powerful established brands). What does this suggest?", steps=[
            S("Total", math=r"2 + 4 + 3 + 3 + 5 = 17 \text{ out of } 25"),
            S("Interpret", text="High overall pressure, especially rivalry and substitutes: the industry is not very attractive for a new, small entrant. Entry would need a clear point of difference (a niche such as local fruit flavours) rather than head-on competition."),
            S("Caution", text="The scores are judgements (invented for practice); the value of the model is in the reasoning behind each score, not in the total."),
        ]),
        H("Core competencies"),
        D("A **core competence** (an idea associated with Prahalad and Hamel) is a combination of skills and technologies that gives real value to customers, is hard for competitors to copy, and can be used in several markets. Examples: a firm's skill in managing a nationwide distribution network to small shops; an expertise in food safety and hygiene. Core competencies are a source of lasting **competitive advantage** and should guide which markets a firm enters.", title="Core competencies"),
        KEY("Evaluating the analysis tools", "Tools support judgement; they do not replace it.", cards=[
            ["SWOT", "Simple and flexible; but often a list without priorities, subjective, and quickly out of date."],
            ["Five forces", "Gives a structured view of an industry's profitability; but static, says little about co-operation between firms or about government, and boundaries of the industry can be unclear."],
            ["Core competencies", "Focuses on what is unique; but competencies are hard to identify honestly and can become 'core rigidities' when markets change."],
        ]),
        MISTAKE("Putting external factors in strengths or weaknesses", "Strengths and weaknesses are internal (within the firm's control). A growing market is an opportunity, not a strength."),
        MISTAKE("Listing forces without judging them", "In a five forces answer, say whether each force is strong or weak FOR THIS INDUSTRY and why, then conclude on the industry's attractiveness."),
        QUIZ("In a SWOT analysis, 'a new government programme to build rural roads' is most likely to be:", ["A strength", "A weakness", "An opportunity", "A core competence"], 2,
             "It is external to the firm and could help it reach new customers: an opportunity.", hint="Is the factor inside or outside the firm's control?",
             feedback=["Strengths are internal.", "Weaknesses are internal.", "", "A core competence is an internal capability."]),
        QUIZ("Which situation gives buyers strong bargaining power?", ["Many small buyers each purchasing small amounts", "A few large supermarket chains buying most of the output of standard products", "Buyers who face high costs if they switch supplier", "A product protected by a patent"], 1,
             "Few, large buyers of standard products can switch easily and negotiate low prices.", hint="When can a customer force the price down?",
             feedback=["Many small buyers have little power individually.", "", "High switching costs weaken buyers.", "A patent gives the SELLER power."]),
        TIP("Strategic analysis is central to Paper 2 essays and Paper 3 case studies: apply SWOT or the five forces to the business in the question, prioritise the most important points, and conclude. Paper 1 tests the definitions and which force a situation belongs to.", title="Exam link"),
        PQ("Distinguish between strategy and tactics with an example of each for a mobile phone retailer.",
           "Strategy: long-term, whole-business, major resources, hard to reverse; for example opening branches in every regional capital over five years. Tactics: short-term actions within the strategy; for example a two-week discount on accessories to attract customers to a new branch."),
        PQ("Use Porter's five forces to explain why profits in the market for basic sachet water tend to be low.",
           "Barriers to entry are low (cheap machines, simple product), so new entrants are a strong force. Substitutes (tap water, bottled water) are many. Buyers can switch easily because the product is standard, so buyer power is high. Rivalry among many small producers is intense, often on price. Supplier power is moderate. Together, strong forces push prices close to costs, so profits are low."),
        PQ("Evaluate the usefulness of SWOT analysis for a business planning to enter a new market. (Essay plan)",
           "Explain SWOT and its link to PESTLE. Useful: simple, cheap, brings internal and external factors together, prompts strategies (use strengths to exploit opportunities, fix weaknesses, prepare for threats). Limits: subjective, lists without weighting, snapshot that dates quickly, can be done to justify a decision already made. Improve with evidence (market research, financial data), priorities and regular review; combine with five forces and core competence analysis. Conclusion."),
        SUM("Strategy is long-term and whole-business; tactics are short-term actions. Strategy exists at corporate, business and functional levels.",
            "SWOT: internal strengths and weaknesses, external opportunities and threats (found through PESTLE); it must lead to conclusions.",
            "Porter's five forces: new entrants, substitutes, supplier power, buyer power and rivalry; strong forces mean lower industry profitability.",
            "Core competencies are hard-to-copy capabilities that create value and open several markets.",
            "All the tools are subjective and static: use evidence, prioritise and review them."),
    ],
))


# ------------------------------------------------------------------ 15. Strategic choice
LESSONS.append(lesson(
    module=M_STR,
    topic="Strategic choice",
    title="Strategic choice: Ansoff's matrix and Porter's generic strategies",
    slug="bsu-strategic-choice",
    minutes=21,
    summary="Choosing a direction for growth with Ansoff's matrix (market penetration, product development, market development, diversification) and a way to compete with Porter's generic strategies (cost leadership, differentiation, focus), with the risks and the conditions each needs.",
    objectives=[
        "Explain the four growth strategies of Ansoff's matrix and the risk of each",
        "Explain Porter's generic strategies and the danger of being 'stuck in the middle'",
        "Apply both models to recommend a strategy for a business",
        "Evaluate the usefulness and limits of the models",
    ],
    key_concepts=["Ansoff's matrix", "Market penetration", "Product development", "Market development",
                  "Diversification", "Cost leadership", "Differentiation", "Focus strategy", "Stuck in the middle"],
    blocks=[
        H("Introduction"),
        T("After analysing its position, the water company from the previous lesson must decide WHERE to grow (which products, which markets) and HOW to compete (on price or on something special). "
          "Two models help: **Igor Ansoff's product-market matrix** for direction, and **Michael Porter's generic strategies** for the basis of competition."),
        H("Ansoff's matrix"),
        IMG("albsu-ansoff.svg", alt="Ansoff's matrix: products (existing, new) across, markets (existing, new) down. Existing product and market: market penetration. New product, existing market: product development. Existing product, new market: market development. Both new: diversification, the riskiest.",
            caption="Figure 1. Ansoff's product-market matrix."),
        KEY("The four directions", "Risk rises as the firm moves away from what it knows.", cards=[
            ["Market penetration", "Sell more of existing products in existing markets: promotion, price offers, loyalty schemes, more outlets. Lowest risk, but limited by market size and rivals' reactions."],
            ["Product development", "New products for existing customers: a flavoured water, a larger bottle. Uses brand and customer knowledge; needs research and development and carries the risk of failure."],
            ["Market development", "Existing products in new markets: new regions, export to CEMAC neighbours, new segments such as offices. Needs market research; local tastes, laws and distribution may differ."],
            ["Diversification", "New products in new markets: highest risk because the firm has neither product nor market knowledge. Related diversification (linked to existing skills) is less risky than unrelated (conglomerate)."],
        ]),
        EX("Worked example 1: classifying options", intro="Classify each option for the water company: (a) a radio campaign to win customers from rivals in Douala; (b) selling the existing water in Chad; (c) launching a fruit juice for its current shop customers; (d) buying a hotel.", steps=[
            S("(a)", text="Existing product, existing market: market penetration."),
            S("(b)", text="Existing product, new market: market development."),
            S("(c)", text="New product, existing market: product development."),
            S("(d)", text="New product (a service), new market: unrelated diversification, the riskiest option."),
        ]),
        H("Porter's generic strategies"),
        D("Porter argued that a firm gains competitive advantage in one of three ways. **Cost leadership**: be the lowest-cost producer in the industry, so you can charge average prices with higher margins or cut prices. **Differentiation**: offer something customers value and will pay more for (quality, brand, design, service). **Focus**: serve a narrow segment (a niche), either with low cost (cost focus) or a special product (differentiation focus). A firm that tries to do everything may end up **stuck in the middle**: not cheap enough to win on price, not special enough to win on value.", title="Generic strategies"),
        EX("Worked example 2: choosing a generic strategy", intro="A small firm makes fruit juice from local mangoes and pineapples. Large brands sell imported juice concentrate cheaply. Which generic strategy should it choose?", steps=[
            S("Cost leadership?", text="Unlikely: the large brands have economies of scale in bottling, buying and advertising."),
            S("Broad differentiation?", text="Expensive: national advertising and a full range would stretch a small firm's finance."),
            S("Differentiation focus", text="A niche of health-conscious urban buyers who value fresh, local, no-added-sugar juice and will pay more. It plays to the firm's strengths (local sourcing, freshness)."),
            S("Risks", text="The niche may be small; a large rival could copy the idea; the premium must cover higher costs. The firm needs to protect quality and build the brand."),
        ]),
        KEY("Evaluating the models", "Helpful frameworks, not answers.", cards=[
            ["Ansoff", "Clear link between direction and risk; but four boxes simplify reality, it ignores competitors' reactions and the firm's resources, and 'new' is a matter of degree."],
            ["Porter", "Focuses attention on a clear basis for advantage; but some firms succeed with both low cost and differentiation (for example through lean production and good design), and advantage can be copied."],
            ["Choice in practice", "Depends on objectives, resources, the results of analysis (SWOT, five forces, core competencies), risk attitude and the stakeholders' views; investment appraisal tests the numbers."],
        ]),
        MISTAKE("Treating a new region as 'diversification'", "Selling the same product in a new market is market development. Diversification needs BOTH a new product and a new market."),
        MISTAKE("Assuming differentiation just means high price", "Differentiation is about value that customers recognise. The higher price is a result, and costs must still be controlled."),
        QUIZ("A bakery begins selling its existing bread to hotels, which it never supplied before. In Ansoff's terms this is:", ["Market penetration", "Market development", "Product development", "Diversification"], 1,
             "The product is the same; the customers (hotels) are a new market segment.", hint="Is the product new? Is the market new?",
             feedback=["Penetration means more sales to EXISTING markets.", "", "The bread is not new.", "Diversification needs a new product too."]),
        QUIZ("A firm offers products that are neither the cheapest nor clearly better than rivals'. Porter would say it is:", ["A cost leader", "Following a focus strategy", "Stuck in the middle", "Differentiated"], 2,
             "Without a clear cost or value advantage it is stuck in the middle and risks low profits.", hint="Does the firm have any clear basis for advantage?",
             feedback=["A cost leader has the lowest costs.", "Focus means serving a clear niche.", "", "Differentiation requires features customers value more."]),
        TIP("Ansoff and Porter appear in Paper 1 (classify the strategy) and often in Paper 2 and Paper 3 (recommend and justify a strategy). Always link your choice to evidence in the case: the firm's resources, its market and the risk.", title="Exam link"),
        PQ("For a mobile money provider, give one example of each of Ansoff's four strategies.",
           "Market penetration: lower fees to win more transfers from existing users. Product development: offer savings or micro-loans to existing users. Market development: launch the existing transfer service in a neighbouring country or among small farmers not yet served. Diversification: open a chain of internet cafes or enter insurance for new customers (new product and market)."),
        PQ("Explain why a cost leadership strategy usually needs large-scale production.",
           "Lowest unit cost in the industry comes mainly from economies of scale (bulk buying, specialised machines, spreading fixed costs over high output) and from efficient processes. A small firm rarely matches these, so cost leadership suits firms with high market share and capacity."),
        PQ("A successful Cameroonian soap maker is considering diversifying into cosmetics for export. Evaluate this strategy. (Essay plan)",
           "Classify: new products and new markets = diversification (related, since soap and cosmetics share skills and materials). For: spreads risk, uses chemistry skills and supplier links, growth beyond a mature home market. Against: highest Ansoff risk, little knowledge of export customers and regulations, large investment, management stretch, strong international rivals. Alternatives: product development at home or market development of soap first. Use SWOT, five forces and investment appraisal. Conclusion: perhaps phased entry, starting with related cosmetics in the home market."),
        SUM("Ansoff's matrix: market penetration, product development, market development and diversification, in rising order of risk.",
            "Diversification needs both a new product and a new market; related diversification is less risky than unrelated.",
            "Porter's generic strategies: cost leadership, differentiation, and focus (cost or differentiation in a niche).",
            "A firm with no clear basis for advantage is 'stuck in the middle'.",
            "Both models simplify: choose using evidence from analysis, resources, objectives, risk and investment appraisal."),
    ],
))


# ------------------------------------------------------------------ 16. Growth, mergers and multinational business
LESSONS.append(lesson(
    module=M_STR,
    topic="Growth, mergers and multinational business",
    title="Growth strategies: organic growth, mergers and takeovers, and multinational business",
    slug="bsu-growth-mergers-multinationals",
    minutes=22,
    summary="Organic and external growth, types of integration (horizontal, vertical, conglomerate), reasons mergers succeed or fail, joint ventures, franchising and alliances, economies and diseconomies of scale, and why firms become multinationals and how they affect host countries.",
    objectives=[
        "Compare organic growth with mergers and takeovers",
        "Classify integration as horizontal, vertical (backward or forward) or conglomerate and explain its aims",
        "Explain why many mergers fail to deliver the expected synergies",
        "Analyse the strategies of multinational businesses and evaluate their effects on a host country",
    ],
    key_concepts=["Organic growth", "Merger", "Takeover", "Horizontal integration", "Vertical integration",
                  "Conglomerate", "Synergy", "Joint venture", "Diseconomies of scale", "Multinational company"],
    blocks=[
        H("Introduction"),
        T("Businesses grow to reach economies of scale, gain market power, spread risk and satisfy owners. Growth can come from inside (opening new branches) or by joining with other firms. "
          "Many large firms operating in Cameroon, such as international banks, breweries and telecom operators, are part of **multinational** groups. This lesson asks how firms grow and whether growth helps everyone."),
        D("**Organic (internal) growth** means expanding from within: new products, new branches, more capacity, financed mainly from profits or loans. **External growth** means joining with other firms: a **merger** (two firms agree to combine into one) or a **takeover** (acquisition: one firm buys a controlling share of another, which may be hostile).", title="Organic and external growth"),
        KEY("Organic or external?", "Compare speed, risk and control.", cards=[
            ["Organic", "Slower, lower risk, culture kept, financed step by step; but may miss opportunities and be too slow against rivals."],
            ["External", "Fast, buys market share, brands, skills and capacity at once; but costly (often a premium over the share price), risky and culture clashes are common."],
        ]),
        H("Types of integration"),
        D("**Horizontal**: firms at the same stage of the same industry (two breweries). **Vertical backward**: a firm joins a supplier (a brewery buys a maize or sorghum farm). **Vertical forward**: a firm joins a customer or outlet (a brewery buys a chain of bars or a distributor). **Conglomerate**: firms in unrelated industries (a brewery buys an insurance company).", title="Integration"),
        KEY("Why integrate?", "Each type has a different main aim.", cards=[
            ["Horizontal", "Economies of scale, higher market share, fewer competitors. Risk: competition authorities may object."],
            ["Backward vertical", "Secure and control supplies and their quality; capture the supplier's profit margin."],
            ["Forward vertical", "Control distribution and the customer experience; capture the retailer's margin."],
            ["Conglomerate", "Spread risk across industries. Risk: managers lack knowledge of the new industry."],
        ]),
        EX("Worked example 1: market share and cost savings", intro="In a market for soft drinks, firm P has a 22% market share and firm Q 15%. They merge. The combined firm closes one head office, saving FCFA 600 m a year, and its unit cost falls from FCFA 210 to FCFA 195 on 80 m bottles a year. Find the new market share and the yearly saving from the lower unit cost.", steps=[
            S("Market share", math=r"22\% + 15\% = 37\% \text{ (if no customers leave)}"),
            S("Unit cost saving", math=r"(210 - 195) \times 80\,000\,000 = 15 \times 80\,000\,000 = 1\,200\,000\,000 \text{ FCFA}"),
            S("Total planned synergy", math=r"1\,200 \text{ m} + 600 \text{ m} = 1\,800 \text{ m FCFA a year}"),
            S("Caution", text="These are planned savings (invented). In practice some customers switch to rivals, integration costs money, and the competition authorities (in the CEMAC area, the regional competition rules: check the current rules) may impose conditions."),
        ]),
        H("Why do many mergers disappoint?"),
        T("**Synergy** is the idea that the combined firm is worth more than the two parts (2 + 2 = 5), through cost savings and shared strengths. Studies often find that many mergers fail to create the value expected. Reasons: paying too much; **culture clash** between the two organisations; poor communication and staff uncertainty; loss of key staff and customers; and **diseconomies of scale** (slower decisions, weaker co-ordination and motivation in a larger organisation)."),
        T("**Other routes to growth.** A **joint venture** is a new business set up and owned by two or more firms that share risks and skills (common when a foreign firm enters a new country with a local partner). A **strategic alliance** is co-operation without a new firm (shared distribution or research). **Franchising** lets others use the brand and system in return for fees, giving fast growth with little capital."),
        H("Multinational business"),
        D("A **multinational company (MNC)** has its headquarters in one country and production or service operations in at least one other country (not only exports).", title="Multinational company"),
        KEY("Why become multinational?", "Reasons and strategies.", cards=[
            ["Reasons", "New markets as home markets mature; lower costs (labour, raw materials); avoid tariffs by producing inside a trade bloc such as CEMAC; spread risk; follow customers."],
            ["Strategies", "Global standardisation (the same product everywhere, low cost) or local adaptation to tastes, laws and culture; many use a mix, sometimes called 'glocalisation'."],
        ]),
        KEY("Effects on a host country", "Balanced judgements are needed.", cards=[
            ["Possible benefits", "Jobs and training, investment, new technology and management skills, tax revenue, exports, better products for consumers, local suppliers gain contracts."],
            ["Possible costs", "Profits sent abroad, local firms squeezed out, pressure for tax concessions, transfer pricing to lower local tax, environmental damage, decisions taken far away, jobs may be low-skilled."],
        ]),
        EX("Worked example 2: an essay plan on MNCs", intro="'Multinational companies always benefit the host country.' Discuss, with reference to a developing economy such as Cameroon.", steps=[
            S("Introduction", text="Define an MNC; note the question's absolute word 'always'."),
            S("Benefits", text="Jobs, skills, investment, technology transfer, tax, exports, links to local suppliers."),
            S("Costs", text="Profit repatriation, competition with local firms, possible tax avoidance, environmental and social impacts."),
            S("Depends on", text="The sector, the share of local inputs and staff, the strength of regulation and tax collection, and the MNC's own policies (corporate social responsibility)."),
            S("Conclusion", text="Not always: the balance depends on the conditions and the host government's policies."),
        ]),
        MISTAKE("Calling every merger 'horizontal'", "Identify the stage of production of each firm. A brewery buying a bottle maker is backward vertical; buying a hotel chain is conglomerate."),
        MISTAKE("Assuming growth always lowers unit costs", "Beyond a point, diseconomies of scale (communication, co-ordination, motivation problems) raise unit costs."),
        QUIZ("A cocoa grinder buys a chain of chocolate shops. This is:", ["Horizontal integration", "Backward vertical integration", "Forward vertical integration", "Conglomerate integration"], 2,
             "The shops are nearer the final customer than the grinder: forward vertical integration.", hint="Is the firm moving towards its suppliers or its customers?",
             feedback=["Horizontal means the same stage of production.", "Backward means joining a supplier, such as cocoa farms.", "", "The industries are related, so it is not conglomerate."]),
        QUIZ("Which is the most common reason why mergers fail to deliver the expected synergy?", ["The firms become too small", "Culture clash and poor integration of the two organisations", "Economies of scale are always too large", "Market share always falls to zero"], 1,
             "Different cultures, systems and management styles make combining the firms hard, so savings are lower than planned.", hint="Think about the people inside the two firms.",
             feedback=["Mergers make firms larger, not smaller.", "", "Economies of scale are a benefit, not a cause of failure.", "Market share may fall a little, not to zero."]),
        TIP("Paper 1 asks you to classify integration and identify reasons for growth; Paper 2 and Paper 3 essays ask you to evaluate a merger, a takeover or an MNC's entry. Use the case evidence and judge which effects are most important.", title="Exam link"),
        PQ("Firm A has a market share of 18% and firm B 12%. After a merger, 2 percentage points of customers switch to rivals. What is the market share of the merged firm?",
           "18% + 12% − 2% = 28%."),
        PQ("Explain two advantages and two disadvantages of growth by franchising for a fast-food brand.",
           "Advantages: rapid growth using franchisees' capital; motivated owner-managers who know the local market. Disadvantages: less control over quality, which can damage the brand; profits are shared (the franchisor receives fees and royalties, not the full profit)."),
        PQ("Evaluate whether a Cameroonian bank should grow organically or by acquiring a smaller rival. (Essay plan)",
           "Organic: lower risk, culture kept, step-by-step finance, but slow. Acquisition: fast increase in customers, branches and skilled staff; possible cost savings (synergy); but price premium, integration costs, culture clash, IT systems to merge, regulatory approval (check the banking regulator's current rules). Depends on: the bank's finance and gearing, the quality of the target, competition, and the urgency of growth. Conclusion: a justified judgement."),
        SUM("Organic growth is slower and safer; external growth (mergers and takeovers) is fast but risky.",
            "Integration can be horizontal, vertical backward, vertical forward or conglomerate, each with a different aim.",
            "Synergy is often smaller than expected because of high prices, culture clash and diseconomies of scale.",
            "Joint ventures, alliances and franchising are other ways to grow.",
            "Multinationals bring investment, jobs and skills but may repatriate profits and squeeze local firms; their net effect depends on conditions and policy."),
    ],
))


# ------------------------------------------------------------------ 17. Organizational culture
LESSONS.append(lesson(
    module=M_STR,
    topic="Organizational culture",
    title="Organizational culture: Handy's four cultures, strong cultures and changing culture",
    slug="bsu-organizational-culture",
    minutes=20,
    summary="What organisational culture is and how it shows, Charles Handy's power, role, task and person cultures, what shapes culture, strong and weak cultures, and why culture matters for strategy, mergers and change.",
    objectives=[
        "Define organisational culture and identify how it shows in a business",
        "Describe Handy's power, role, task and person cultures and the businesses that suit each",
        "Explain what shapes a culture and the effects of strong and weak cultures",
        "Evaluate why changing culture is difficult and how it can be done",
    ],
    key_concepts=["Organisational culture", "Power culture", "Role culture", "Task culture", "Person culture",
                  "Strong culture", "Cultural change"],
    blocks=[
        H("Introduction"),
        T("Two shops sell the same phones. In one, staff wait for the owner to decide everything; in the other, staff greet customers by name, solve problems themselves and share ideas at weekly meetings. The difference is **culture**. "
          "Culture is often summed up as 'the way we do things around here'. It affects motivation, customer service, the success of a strategy and the success of mergers."),
        D("**Organisational culture** is the set of shared values, beliefs, attitudes and habits that shape how people in an organisation behave. It shows in dress, language, stories told about the firm, how decisions are made, how mistakes are treated, office layout, rituals and who is rewarded.", title="Organisational culture"),
        H("Handy's four cultures"),
        T("Charles Handy described four types of culture, each linked to a structure and a style of management. Most real organisations mix them, and different departments can have different cultures."),
        KEY("Handy's typology", "Name, picture and fit.", cards=[
            ["Power culture", "Power is held by one person or a small group at the centre (like a spider's web). Fast decisions, few rules, loyalty to the leader. Suits small, owner-run firms. Risk: depends on one person; others may not take initiative."],
            ["Role culture", "Power comes from a person's position; clear rules, procedures and job descriptions (like a Greek temple with pillars). Stable and predictable; suits large bureaucracies, banks, government. Risk: slow and rigid when change is needed."],
            ["Task culture", "Power comes from expertise; teams form to complete projects (a net or matrix). Flexible and creative; suits consultancies, research, advertising. Risk: costly, can be hard to control, teams may compete for resources."],
            ["Person culture", "The organisation exists to serve the individuals in it, who are experts (a cluster). Found in partnerships of lawyers, doctors or architects. Risk: hard to manage or to set shared goals."],
        ]),
        EX("Worked example 1: identifying a culture", intro="Identify the dominant culture in each case: (a) a family bakery where the founder decides everything and staff check with her before acting; (b) a ministry with strict procedures, grades and forms for every decision; (c) a software firm that forms a new team of experts for each client project; (d) a chambers of independent lawyers sharing an office and a secretary.", steps=[
            S("(a)", text="Power culture: authority at the centre, decisions by the founder."),
            S("(b)", text="Role culture: rules, procedures and positions."),
            S("(c)", text="Task culture: expertise and project teams (linked to matrix structure)."),
            S("(d)", text="Person culture: the organisation serves the professionals."),
        ]),
        H("What shapes culture, and why it matters"),
        T("Culture is shaped by the **founder** and the firm's history, the **leadership style** of managers, the **size** and structure of the business, the **industry** (safety rules in mining, creativity in design), the **national culture** of the country (Geert Hofstede's research compared national cultures; check your textbook), and the people recruited and promoted."),
        D("A **strong culture** is one where values are widely shared and deeply held. It can give commitment, clear direction and good service; but if the values are wrong for the market (for example resistance to new technology), a strong culture becomes a barrier to change and can lead to 'groupthink'.", title="Strong and weak cultures"),
        EX("Worked example 2: culture and a merger", intro="A fast-moving mobile-money start-up with a task culture is bought by a large bank with a role culture. Predict two problems and suggest how to reduce them.", steps=[
            S("Problem 1", text="Start-up staff, used to freedom and quick decisions, face forms and approval layers: motivation falls and key staff leave."),
            S("Problem 2", text="Bank managers see the start-up as risky and undisciplined; conflict slows the projects the bank bought it for."),
            S("Reduce them", text="Keep the start-up as a separate unit with its own culture for a period, agree clear shared goals, communicate openly, and keep key people with retention incentives."),
        ]),
        H("Changing culture"),
        T("Culture is hard to change because values are deep, habits are comfortable, and people fear losing status or jobs. Methods include: new leaders who model the new values; changing recruitment, training and reward systems; changing structure (for example delayering); communicating a clear vision; and celebrating early successes. It usually takes years, not months, and links to the next lesson on managing change."),
        MISTAKE("Describing culture only as 'the atmosphere'", "Define it as shared values, beliefs and behaviour, and give evidence of how it shows (decisions, rules, rewards, stories)."),
        MISTAKE("Saying one Handy culture is always best", "Each culture suits some situations. Judge the fit with the firm's size, market and strategy."),
        QUIZ("A consultancy forms a new team of specialists for each client project, and authority comes from expertise. This is Handy's:", ["Power culture", "Role culture", "Task culture", "Person culture"], 2,
             "Teams formed around tasks, with power from expertise, describe a task culture.", hint="Where does power come from in this firm?",
             feedback=["Power culture centres on one leader.", "Role culture is based on positions and procedures.", "", "Person culture serves individual professionals rather than projects."]),
        QUIZ("Which is a risk of a very strong culture?", ["Staff do not share any values", "It can resist necessary change and encourage groupthink", "It always lowers motivation", "It makes the firm illegal"], 1,
             "Deeply shared values can make people defend old ways when the market changes.", hint="What happens when strongly held values no longer fit the market?",
             feedback=["That describes a weak culture.", "", "Strong cultures often raise commitment.", "Culture has nothing to do with legality here."]),
        TIP("Culture appears in Paper 1 (match a description to Handy's types) and in Paper 2 and Paper 3, especially in questions on mergers, change and leadership. Use evidence from the case to identify the culture and judge its fit with the strategy.", title="Exam link"),
        PQ("Explain why a role culture may suit a bank but not an advertising agency.",
           "A bank must follow strict rules, procedures and controls for security and regulation; clear roles and predictable behaviour reduce risk. An advertising agency needs creativity, flexibility and fast teamwork on different campaigns; rigid rules and hierarchy would slow ideas, so a task culture suits it better."),
        PQ("A founder's power culture worked well when her firm had 10 staff. It now has 150 staff in three towns. Explain two problems this may cause.",
           "Decisions wait for one person, so they are slow and the founder is overloaded; managers in the other towns cannot respond to local customers. Staff do not develop initiative or management skills, which hurts motivation and succession planning. The firm may need more delegation and a role or task culture."),
        PQ("Evaluate the view that changing an organisation's culture is the hardest part of any strategic change. (Essay plan)",
           "Define culture; explain why change is hard (deep values, fear, habits, power). For the view: many strategies and mergers fail for cultural reasons; structures and systems can be changed quickly but beliefs cannot. Against: some changes are mainly technical or financial; a crisis or new leader can change culture faster; with communication, training and rewards culture does shift. Evaluation: depends on the size of the change, the strength of the existing culture and leadership. Conclusion."),
        SUM("Culture is the shared values, beliefs and behaviour of an organisation: 'the way we do things around here'.",
            "Handy: power (central leader), role (rules and positions), task (expert teams) and person (serving professionals).",
            "Culture is shaped by founders, leaders, size, industry, national culture and recruitment.",
            "A strong culture gives commitment but can block change; culture clashes often wreck mergers.",
            "Changing culture needs leadership, new systems, communication and time."),
    ],
))


# ------------------------------------------------------------------ 18. Managing change
LESSONS.append(lesson(
    module=M_STR,
    topic="Managing change",
    title="Managing change: force field analysis, Lewin, Kotter and contingency planning",
    slug="bsu-managing-change",
    minutes=22,
    summary="Causes of change, why people resist it and how to reduce resistance, Lewin's force field analysis and three-stage model, Kotter's eight steps, and contingency planning and crisis management.",
    objectives=[
        "Identify internal and external causes of change and the reasons people resist it",
        "Use Lewin's force field analysis to weigh driving and restraining forces",
        "Apply Lewin's three stages and Kotter's eight steps to a change programme",
        "Explain contingency planning and crisis management and evaluate approaches to change",
    ],
    key_concepts=["Driving force", "Restraining force", "Force field analysis", "Unfreeze, change, refreeze",
                  "Kotter's eight steps", "Resistance to change", "Contingency planning", "Crisis management"],
    blocks=[
        H("Introduction"),
        T("A distribution company in Douala wants to replace paper order books with a computer system. Customers want faster service and rivals have already changed, but many staff fear for their jobs and some lack IT skills. "
          "Change is constant: new technology, competitors, laws, the economy, mergers and new strategies all force businesses to change. The question is how to manage it so that it succeeds."),
        KEY("Causes of change", "Internal and external.", cards=[
            ["External", "New technology, competitors, changes in consumer tastes, the economy (inflation, exchange rates), new laws and taxes, the environment (PESTLE)."],
            ["Internal", "New leaders or owners, new strategy, growth, mergers, poor performance, reorganisation of structure."],
        ]),
        KEY("Why people resist change", "Understand resistance before trying to reduce it.", cards=[
            ["Self-interest", "Fear of losing jobs, pay, status or power."],
            ["Uncertainty", "Fear of the unknown and of not coping with new skills."],
            ["Misunderstanding and distrust", "Poor communication; past changes that went badly."],
            ["Different judgement", "Staff may honestly think the change is a mistake, and sometimes they are right."],
        ], note="Approaches to reducing resistance (an idea associated with Kotter and Schlesinger) range from education and participation, through support and negotiation, to manipulation and coercion; the softer approaches take longer but give more lasting commitment."),
        H("Lewin's force field analysis"),
        D("Kurt Lewin's **force field analysis** lists the **driving forces** pushing for a change and the **restraining forces** resisting it, and gives each a score for its strength. If the driving forces outweigh the restraining forces, change is likely to succeed; managers can then plan to strengthen drivers or, often more effectively, to weaken restraints.", title="Force field analysis"),
        IMG("albsu-force-field.svg", alt="Force field diagram for a new computer system. Driving forces on the left pointing right: customers want faster service 5, lower running costs 4, rivals already changed 3, total 12. Restraining forces on the right pointing left: fear of job losses 4, cost of training 3, lack of IT skills 2, total 9.",
            caption="Figure 1. Force field analysis for the distribution company (scores invented for practice)."),
        EX("Worked example 1: using the force field", intro="Use Figure 1. Should the company go ahead, and how could it make success more likely?", steps=[
            S("Totals", math=r"\text{Driving} = 5 + 4 + 3 = 12; \quad \text{Restraining} = 4 + 3 + 2 = 9"),
            S("Judgement", text="Driving forces are stronger (12 against 9), so the change is likely to succeed if managed well."),
            S("Weaken restraints", text="Guarantee no compulsory redundancies or offer retraining (fear of job losses 4 to 2); train staff before launch (lack of IT skills 2 to 0)."),
            S("New balance", math=r"\text{Restraining} = 2 + 3 + 0 = 5 \text{ against driving } 12"),
        ], check=r"12 - 9 = 3; \quad 12 - 5 = 7"),
        H("Lewin's three stages"),
        T("Lewin also described change as three stages. **Unfreeze**: show why the present way must change (share data on lost customers, involve staff in diagnosis). **Change (move)**: introduce the new system with training, support and communication. **Refreeze**: make the new way normal through new procedures, rewards and culture, so people do not slip back. Critics say that in fast-changing markets organisations never 'refreeze' for long."),
        H("Kotter's eight steps"),
        CODE("1  Create a sense of urgency\n"
             "2  Build a guiding coalition (a team with power to lead the change)\n"
             "3  Form a strategic vision\n"
             "4  Communicate the vision widely\n"
             "5  Remove obstacles and empower people to act\n"
             "6  Generate short-term wins\n"
             "7  Build on the change (do not declare victory too early)\n"
             "8  Anchor the change in the culture", "text", title="Table 1. Kotter's eight steps for leading change (summarised)"),
        EX("Worked example 2: applying Kotter", intro="Apply three of Kotter's steps to the computer system.", steps=[
            S("Urgency (step 1)", text="Show staff the figures on orders lost to faster rivals."),
            S("Short-term wins (step 6)", text="Launch the system first in one depot; publicise faster deliveries and the staff who made it work."),
            S("Anchor in culture (step 8)", text="Include system use in appraisal and training of new staff; recognise teams that improve service."),
        ]),
        H("Contingency planning and crisis management"),
        D("**Contingency planning** means preparing in advance for possible but unlikely events (a fire, a cyber-attack, loss of a major supplier, a power failure, an epidemic) so that the business can keep running. **Crisis management** is the response when such an event happens: a clear leader, fast decisions, honest communication with staff, customers and the media.", title="Contingency planning"),
        T("**Evaluation.** Contingency plans cost time and money and cannot cover every risk, but they cut the damage and recovery time when a crisis strikes. Plans must be tested and updated, and staff trained, or they are useless when needed."),
        MISTAKE("Ignoring the scores in force field analysis", "Give each force a score, total both sides, compare, and then suggest specific actions to weaken the strongest restraining forces."),
        MISTAKE("Treating all resistance as bad", "Resistance can reveal real problems with the plan. Listening to it can improve the change."),
        QUIZ("Driving forces score 4, 3 and 2; restraining forces score 5 and 3. What does force field analysis suggest?", ["The change will certainly succeed", "Forces are balanced (9 against 8), so managers should weaken restraints before going ahead", "Restraining forces are stronger, so the change is impossible", "The change should be forced through at once"], 1,
             "Driving 9 against restraining 8 is close: success is uncertain, so reduce the strongest restraint (score 5) first.", hint="Add each side and compare.",
             feedback=["A narrow margin does not guarantee success.", "", "Restraining forces total 8, less than 9.", "Forcing change against strong resistance often fails."]),
        QUIZ("In Lewin's three-stage model, what happens in the 'refreeze' stage?", ["People are made aware that change is needed", "The new system is introduced", "The new ways are made permanent through procedures, rewards and culture", "The old system is restored"], 2,
             "Refreezing locks in the change so people do not return to old habits.", hint="What stops people slipping back to old ways?",
             feedback=["That is unfreezing.", "That is the change (move) stage.", "", "Restoring the old system would undo the change."]),
        TIP("Change management is a frequent Paper 2 essay and Paper 3 case-study theme. Apply a model (force field, Lewin, Kotter) to the case, explain resistance, and recommend specific actions. Paper 1 tests the stages and terms.", title="Exam link"),
        PQ("A hospital plans to introduce shift work. Driving forces: patient waiting times (5), government targets (3). Restraining: staff family commitments (4), cost of extra pay (3), union opposition (3). Analyse and recommend.",
           "Driving total 8, restraining total 10: change is likely to fail as planned. Weaken restraints: consult staff and unions on shift patterns (union opposition 3 to 1), offer flexible or voluntary shifts and childcare support (family commitments 4 to 2). New restraining total 2 + 3 + 1 = 6 < 8. Recommend consultation before implementation."),
        PQ("Explain two reasons why employees resist change and one method to overcome each.",
           "Fear of job loss: overcome by honest communication and guarantees or retraining. Fear of not coping with new skills: overcome by training and support before the change. (Also: loss of status or power, handled by participation and negotiation.)"),
        PQ("Evaluate the usefulness of Kotter's eight steps for a family company merging with a larger rival. (Essay plan)",
           "Explain the steps. Useful: structured, stresses urgency, leadership coalition, vision and communication, short-term wins and culture, which address common merger problems (culture clash, fear). Limits: linear model for a messy process; takes time a merger may not allow; depends on strong leadership; steps may need adapting to the national and company culture. Compare with Lewin. Conclusion: a helpful guide if adapted, combined with force field analysis and attention to resistance."),
        SUM("Change has external causes (PESTLE, competitors) and internal causes (new leaders, strategy, growth).",
            "People resist through self-interest, uncertainty, distrust and different judgement; communication and participation reduce resistance.",
            "Force field analysis: score and total driving and restraining forces, then weaken the strongest restraints.",
            "Lewin: unfreeze, change, refreeze. Kotter: eight steps from urgency to anchoring change in the culture.",
            "Contingency planning prepares for unlikely events; crisis management handles them when they happen."),
    ],
))


# ------------------------------------------------------------------ Examination 1. Paper 1
LESSONS.append(lesson(
    module=M_EX,
    topic="Paper 1",
    title="Paper 1: working through 50 multiple-choice questions in Business Studies",
    slug="bsu-exam-paper1-multiple-choice",
    minutes=20,
    summary="A routine for the 50 multiple-choice questions of Paper 1: reading the stem, predicting, eliminating distractors, fast business calculations, applying models to short scenarios, and a revision map of the four Upper Sixth modules.",
    objectives=[
        "Use a four-step routine for every multiple-choice question",
        "Do the common Upper Sixth calculations quickly and accurately",
        "Recognise the traps that wrong options are built on",
        "Plan revision with a map of the four Upper Sixth modules",
    ],
    key_concepts=["Stem", "Distractor", "Elimination", "Scenario question", "Calculation question", "Revision map"],
    blocks=[
        H("Introduction"),
        T("Paper 1 of A Level Business Studies is made up of 50 multiple-choice questions. Business Studies is not covered by the Board's 2023 subject report, so check the exact format, timing and weighting with your teacher. "
          "In the KKEVO mock paper for this lesson we set 90 minutes (a KKEVO practice setting), a little under two minutes a question. Each question has one correct option; a wrong answer earns nothing, so the aim is to choose the best option every time."),
        KEY("Four steps for every question", "Quick and in order.", cards=[
            ["1. Read the stem", "Find the command (which, calculate, NOT, most likely, best). Note figures and units (FCFA, %, days, times)."],
            ["2. Predict", "Answer in your head before reading the options, so attractive distractors do not lead you."],
            ["3. Eliminate", "Cross out options you can prove wrong. Each wrong option is built on a real mistake."],
            ["4. Check", "Re-read the stem with your choice. For calculations, check units and size."],
        ]),
        H("Three kinds of question"),
        T("**Knowledge** questions test a term or model (what is free float? which Handy culture?). **Calculation** questions need a formula: capacity utilization, reorder level, EOQ, break-even, margin of safety, variance, ratios, payback, ARR, NPV, IRR, float. **Scenario** questions describe a short business case and ask you to classify or judge (which Ansoff strategy? which source of finance is most suitable? what is the most likely effect?)."),
        EX("Worked example 1: a calculation", intro="A firm sells at FCFA 1 500, variable cost FCFA 900, fixed costs FCFA 3 600 000 a month, sales 7 500 units. What is the margin of safety? Options: 6 000 units; 1 500 units; 2 400 units; 3 900 units.", steps=[
            S("Predict", math=r"BEP = 3\,600\,000 \div (1\,500 - 900) = 6\,000; \quad MOS = 7\,500 - 6\,000 = 1\,500"),
            S("Eliminate", text="6 000 is the break-even output, not the margin. 2 400 divides by the price (3 600 000 ÷ 1 500) and 3 900 is 7 500 minus 3 600 (wrong units). The answer is 1 500 units."),
        ]),
        EX("Worked example 2: a scenario", intro="A bakery that sells bread in Buea starts selling the same bread in Kumba. In Ansoff's matrix this is: product development; market development; diversification; market penetration.", steps=[
            S("Predict", text="Same product, new market: market development."),
            S("Eliminate", text="Product development needs a new product; diversification needs both new; penetration means the existing market."),
        ]),
        KEY("Common distractors", "Recognise the trap.", cards=[
            ["The unfinished calculation", "Break-even instead of margin of safety; gross instead of operating profit; NPV before subtracting the cost."],
            ["The wrong formula", "Dividing by price instead of contribution; debt ÷ equity instead of debt ÷ capital employed."],
            ["The reversed idea", "Adverse for favourable; backward for forward integration; maximum for reorder level."],
            ["The true but irrelevant statement", "Correct in general but not an answer to this stem."],
        ]),
        CODE("Module                                   Ideas to be ready for\n"
             "Operations & Production Management       location factors and break-even, job/batch/flow,\n"
             "                                         productivity, capacity utilization, reorder level,\n"
             "                                         EOQ, JIT, kaizen, TQM, CPA (EST, LFT, float)\n"
             "Business Finance & Managerial Accounting sources of finance, gearing, working capital cycle,\n"
             "                                         cash flow forecasts, contribution, break-even,\n"
             "                                         budgets and variances\n"
             "Financial Statement Analysis &           income statement, balance sheet, ratios,\n"
             "Investment Appraisal                     payback, ARR, NPV, IRR\n"
             "Strategic Management & Change            SWOT, five forces, core competencies, Ansoff,\n"
             "                                         Porter, integration, MNCs, Handy, Lewin, Kotter", "text", title="Table 1. Revision map for the Upper Sixth modules"),
        T("Your teacher will tell you whether the paper also covers the Lower Sixth modules (enterprise, management, people and marketing); revise them as well if it does."),
        MISTAKE("Spending five minutes on one calculation", "Mark it, guess sensibly, move on and come back. Every question carries the same credit."),
        MISTAKE("Choosing an option because it contains a familiar term", "Distractors often use the right vocabulary in the wrong way. Test each option against the stem."),
        QUIZ("A question asks which statement about JIT is NOT correct. What should you do?", ["Choose the first true statement", "Test each statement and choose the false one", "Choose the longest statement", "Leave it blank"], 1,
             "A NOT question asks for the false statement: test each one.", hint="What are you looking for in a NOT question?",
             feedback=["A true statement is the wrong choice here.", "", "Length does not show truth.", "A blank cannot score; a reasoned answer can."]),
        QUIZ("Current assets FCFA 90 m, inventory FCFA 30 m, current liabilities FCFA 50 m. Acid test ratio?", ["1.8", "1.2", "0.6", "3.0"], 1,
             "(90 − 30) ÷ 50 = 1.2.", hint="Remove inventory first.",
             feedback=["That is the current ratio.", "", "That is inventory ÷ current liabilities.", "That is 90 ÷ 30."]),
        TIP("Do a first pass answering everything you know, mark doubtful questions, then return. Leave the last 5 to 10 minutes to check that every question has an answer and that answers are in the right places on the sheet.", title="Exam link"),
        PQ("Usage 300 units a day, lead time 5 days, buffer 500 units. Reorder level? Options: 1 500; 2 000; 800; 500.",
           "300 × 5 + 500 = 2 000 units. 1 500 forgets the buffer; 800 adds one day's usage; 500 is the buffer only."),
        PQ("A project costs FCFA 20 m and earns FCFA 6 m a year for 5 years. ARR on initial cost? Options: 30%; 10%; 50%; 6%.",
           "Average profit = (30 − 20) ÷ 5 = 2; 2 ÷ 20 × 100 = 10%. 30% is 6 ÷ 20 (no deduction of cost); 50% is 10 ÷ 20; 6% has no basis."),
        PQ("List four steps for answering a multiple-choice question.",
           "Read the stem and note the command and figures; predict the answer; eliminate options you can prove wrong; check your choice against the stem and units."),
        SUM("Paper 1 is 50 multiple-choice questions; check the exact format with your teacher. The KKEVO mock uses 90 minutes.",
            "Use read, predict, eliminate, check for every question.",
            "Know the formulas: utilization, reorder level, EOQ, break-even, variances, ratios, payback, ARR, NPV, IRR, float.",
            "Distractors are unfinished calculations, wrong formulas, reversed ideas and irrelevant truths.",
            "Revise every module; never leave a question blank."),
    ],
))

# ------------------------------------------------------------------ Examination 2. Paper 2
LESSONS.append(lesson(
    module=M_EX,
    topic="Paper 2",
    title="Paper 2: planning and writing business essays that analyse and evaluate",
    slug="bsu-exam-paper2-essays",
    minutes=21,
    summary="How to answer Business Studies essay questions: reading command words, planning, building chains of analysis, using numbers and models, writing evaluation that reaches a supported judgement, and managing time.",
    objectives=[
        "Interpret command words such as explain, analyse, evaluate, discuss and assess",
        "Plan an essay with definitions, developed points, evaluation and a conclusion",
        "Build chains of analysis that link a cause to a business outcome",
        "Write evaluation that weighs arguments and reaches a justified judgement",
    ],
    key_concepts=["Command word", "Essay plan", "Chain of analysis", "Application", "Evaluation", "Judgement"],
    blocks=[
        H("Introduction"),
        T("Paper 2 is a paper of management and business essays. Business Studies is not in the Board's 2023 report, so check the exact format (number of questions, choice and timing) with your teacher. In the KKEVO practice paper we set 150 minutes (a KKEVO practice setting). "
          "Examiners in all A Level business-type subjects look for the same skills: **knowledge** (correct terms and models), **application** (to the business or situation in the question), **analysis** (developed cause-and-effect reasoning) and **evaluation** (weighing and judging)."),
        KEY("Command words", "They tell you what to do.", cards=[
            ["Explain", "Give reasons and show how or why, with an example."],
            ["Analyse", "Break the issue into parts and follow each through its causes and effects."],
            ["Evaluate / assess", "Weigh the arguments, decide which matter most and reach a supported judgement."],
            ["Discuss / to what extent", "Present both sides and give your view with reasons; 'to what extent' needs a degree, not just yes or no."],
        ]),
        H("A plan before you write"),
        T("Spend a few minutes planning. A good plan has: definitions of the key terms; three or four main points, each with a chain of analysis; the evaluation (what it depends on, which point matters most, short and long term, different stakeholders); and the conclusion that answers the question directly."),
        D("A **chain of analysis** links a point to its effect on the business in several logical steps, often with connectives such as 'this means that', 'as a result', 'therefore', 'which leads to'. Example: JIT cuts average stock → holding costs and cash tied up fall → working capital improves → the firm can pay suppliers on time or invest, BUT a late delivery would stop production.", title="Chain of analysis"),
        EX("Worked example 1: a model plan", intro="'Evaluate whether a manufacturer should finance a new factory with a bank loan rather than a share issue.'", steps=[
            S("Introduction", text="Define loan and share capital and gearing. State that the choice depends on the firm's situation."),
            S("Point 1: control", text="A loan keeps control with existing owners → no dilution → managers can follow their long-term plans; shares bring new owners and dividend expectations."),
            S("Point 2: cost and risk", text="Interest must be paid in good and bad years → gearing rises (show a calculation, e.g. from 30% to 53%) → higher financial risk and possible refusal of future loans; shares carry no compulsory payments."),
            S("Point 3: cost of finance and profitability", text="If ROCE is above the interest rate, borrowing raises returns to shareholders; if not, it lowers them."),
            S("Evaluation", text="Depends on current gearing, stability of profits, interest rates, the owners' attitude to control, and the legal form (only companies can issue shares). The most important factor is the risk the firm can carry."),
            S("Conclusion", text="A judgement for the firm in the question, for example a mix of retained profit and a loan if gearing is low and profits stable."),
        ]),
        H("Writing evaluation"),
        T("Evaluation is not a list of advantages and disadvantages followed by 'it depends'. Say WHAT it depends on and HOW. Useful methods: rank the factors and say which matters most and why; distinguish short-term and long-term effects; consider different stakeholders; question the data or the model's assumptions (for example the forecasts behind an NPV); and finish with a clear judgement that follows from your arguments."),
        EX("Worked example 2: improving an evaluation", intro="Weak: 'JIT has advantages and disadvantages, so it depends.' Improve it for a brewery that imports its malt.", steps=[
            S("Identify the key factor", text="Whether JIT works depends mainly on the reliability of supply."),
            S("Apply", text="Imported malt can be delayed at the port for weeks, so full JIT would risk stopping production, which would cost far more than the holding costs saved."),
            S("Judge", text="The brewery should use JIT for local, reliable inputs (labels, crates) but keep buffer stock of imported malt. The benefit of JIT is therefore limited, not absent."),
        ]),
        T("**Using numbers and diagrams.** Short calculations (a ratio, a break-even output, an NPV) and simple diagrams (a break-even chart, Ansoff's matrix, a force field) make arguments precise. Use them when they support a point; label them and explain what they show."),
        MISTAKE("Writing everything you know about a topic", "Answer the question set. Material that does not support your argument earns nothing and wastes time."),
        MISTAKE("A conclusion that repeats the essay", "The conclusion should give a judgement and the main reason for it, not a summary of every point."),
        QUIZ("Which is the best example of analysis?", ["Gearing is a ratio", "A loan raises gearing, so interest payments rise and profit becomes more sensitive to falls in sales, raising the risk for shareholders", "Loans have advantages and disadvantages", "Many firms take loans"], 1,
             "It follows the effect through several linked steps to an outcome for the business.", hint="Which answer links cause and effect in several steps?",
             feedback=["That is a definition (knowledge) only.", "", "That is a vague statement with no development.", "That is a general fact, not analysis."]),
        QUIZ("A question asks 'To what extent...?'. What must the answer contain?", ["Only arguments for", "Only a definition", "Arguments on both sides and a judgement on how far the statement is true", "A list of facts"], 2,
             "'To what extent' asks you to weigh and decide the degree to which the statement holds.", hint="What does 'extent' ask you to measure?",
             feedback=["One-sided answers cannot judge extent.", "A definition is only the start.", "", "Facts alone do not give a judgement."]),
        TIP("Plan before writing, keep to time for each essay (share the time in proportion to the questions), and leave a few minutes to check. Check the number of essays and the choice of questions with your teacher.", title="Exam link"),
        PQ("Write a chain of analysis for: 'A rise in capacity utilization can improve a firm's competitiveness.'",
           "Higher utilization spreads the same fixed costs over more units → fixed and average cost per unit fall → the firm can cut its price or earn a higher margin at the same price → it can win market share or invest more, improving competitiveness (as long as running near 100% does not cause breakdowns and lost quality)."),
        PQ("Give three different ways of evaluating in a Business Studies essay.",
           "Rank the factors and say which matters most and why; distinguish short-term and long-term effects; consider different stakeholders; question the reliability of the data or the model's assumptions; say what the outcome depends on and how. Any three with explanation."),
        PQ("Plan an answer to: 'Discuss whether Porter's five forces model is useful to a small firm entering a new market.'",
           "Introduction: define the model and its purpose. For: shows industry attractiveness, highlights barriers to entry and buyer/supplier power, helps choose a niche (focus strategy). Against: static, subjective scores, ignores co-operation and government, needs data a small firm may lack. Evaluation: useful as a structured starting point if combined with market research and SWOT; most useful in judging barriers to entry. Conclusion: useful but not sufficient alone."),
        SUM("Paper 2 is management and business essays; check the exact format with your teacher.",
            "Command words decide the task: explain, analyse, evaluate, discuss, to what extent.",
            "Plan: definitions, three or four developed points, evaluation, conclusion.",
            "Analysis is a chain of linked effects; evaluation weighs, ranks and reaches a judgement.",
            "Use short calculations and labelled diagrams where they support the argument."),
    ],
))

# ------------------------------------------------------------------ Examination 3. Paper 3
LESSONS.append(lesson(
    module=M_EX,
    topic="Paper 3",
    title="Paper 3: the strategic business case study method",
    slug="bsu-exam-paper3-case-study",
    minutes=22,
    summary="How to tackle a business case study: reading and annotating the case, extracting and calculating from the appendices, choosing the right tools (ratios, break-even, NPV, CPA, SWOT, Ansoff), answering in context and making a justified recommendation.",
    objectives=[
        "Read and annotate a case study for objectives, stakeholders, problems and data",
        "Select and carry out the calculations the data allow",
        "Apply analytical tools to the business in the case rather than in general",
        "Write a recommendation that weighs options and is supported by evidence",
    ],
    key_concepts=["Case study", "Annotation", "Appendix data", "Context", "Recommendation", "Justification"],
    blocks=[
        H("Introduction"),
        T("Paper 3 is a strategic business case study: a description of a real-style business with data in appendices, followed by questions. Business Studies is not in the Board's 2023 report, so check the exact format with your teacher. "
          "The key skill is **context**: every answer must be about THIS business, its objectives, its market, its people and its numbers. A general answer that could be about any firm scores poorly."),
        KEY("A five-step method", "Use it for every case.", cards=[
            ["1. Skim, then read closely", "First get the story: who, what, where, the problem. Then read again, slowly."],
            ["2. Annotate", "Mark objectives, stakeholders, strengths and problems, figures, dates and any hint of change, conflict or risk."],
            ["3. Work the numbers", "List what each appendix allows you to calculate (ratios, break-even, cash flow, NPV, float, utilization)."],
            ["4. Choose tools", "SWOT, five forces, Ansoff, Porter, force field, decision criteria. Use a tool only if it helps answer the question."],
            ["5. Recommend", "Compare options against the firm's objectives and constraints; choose one; justify; say what it depends on."],
        ]),
        H("A mini case"),
        CODE("Mbe Juices Ltd (invented) makes fruit juice near Bafoussam.\n"
             "Objective: grow sales by 20% in three years without losing control\n"
             "of the family company.\n"
             "Appendix 1 (FCFA m): revenue 400, gross profit 140, operating\n"
             "profit 36, capital employed 300, loans 60.\n"
             "Appendix 2: option A, new bottling line, cost 80, NPV at 10% = +12,\n"
             "payback 3.5 years. Option B, export to Gabon with an agent, cost 20,\n"
             "NPV at 10% = +5, payback 1.8 years.\n"
             "Notes: the founder dislikes debt; two local rivals cut prices last\n"
             "year; the current line runs at 95% capacity.", "text", title="Case 1. Mbe Juices (invented for practice)"),
        EX("Worked example 1: working the numbers", intro="What can be calculated from Appendix 1, and what do the results suggest?", steps=[
            S("Gross margin", math=r"140 \div 400 \times 100 = 35\%"),
            S("Operating margin", math=r"36 \div 400 \times 100 = 9\%"),
            S("ROCE", math=r"36 \div 300 \times 100 = 12\%"),
            S("Gearing", math=r"60 \div 300 \times 100 = 20\%"),
            S("Interpret", text="Low gearing leaves room to borrow, but the founder dislikes debt. ROCE of 12% is above the 10% discount rate. Running at 95% capacity means growth needs new capacity or outsourcing."),
        ]),
        EX("Worked example 2: a recommendation", intro="Should Mbe Juices choose option A or option B? Justify your answer.", steps=[
            S("Compare numbers", text="A has the higher NPV (+12 against +5), but costs four times as much and pays back more slowly (3.5 against 1.8 years)."),
            S("Link to objectives and constraints", text="The 20% growth target needs capacity: at 95% utilization, export sales (B) could not be supplied without new capacity. A loan for A would raise gearing from 20% to 140 ÷ 380 ≈ 36.8% (if borrowed in full), still moderate, but the founder dislikes debt."),
            S("Other factors", text="Price-cutting rivals at home make growth abroad attractive; B carries risks of the agent, exchange and border delays; A is a long-term commitment."),
            S("Judgement", text="Recommend A first, financed partly from retained profit and partly by a modest loan (or leasing) to respect the founder's view, followed by B once capacity exists. This depends on the reliability of the demand forecasts behind the NPV."),
        ], check=r"(60 + 80) \div (300 + 80) \approx 36.8\%"),
        MISTAKE("Ignoring the appendices", "Data are there to be used. A recommendation with no figures is weaker than one that uses ratios, NPV or break-even from the case."),
        MISTAKE("Recommending without rejecting the alternative", "Explain why the chosen option is better than the others for this firm, and what the decision depends on."),
        QUIZ("In a case study, which answer best shows 'context'?", ["JIT reduces stock holding costs for any firm", "Because Mbe Juices runs at 95% capacity, it cannot take on export orders without the new line", "Ratios are useful for all businesses", "Exporting can be risky"], 1,
             "It uses a specific fact from the case to make the point about this business.", hint="Which answer could ONLY be written about this firm?",
             feedback=["This is general and could apply to any firm.", "", "General statement with no link to the case.", "True in general but not tied to the case evidence."]),
        QUIZ("From the case, Mbe Juices' operating profit is FCFA 36 m and capital employed FCFA 300 m. What is its ROCE?", ["9%", "12%", "35%", "20%"], 1,
             "36 ÷ 300 × 100 = 12%.", hint="Operating profit ÷ capital employed × 100.",
             feedback=["That is the operating margin (36 ÷ 400).", "", "That is the gross margin.", "That is the gearing."]),
        TIP("In Paper 3 time goes fast: read and annotate first, then answer. Quote figures from the case, show calculations with units, and finish each long answer with a recommendation tied to the firm's objectives. Check the exact format with your teacher.", title="Exam link"),
        PQ("From Case 1, what is the margin of operating expenses (gross profit − operating profit) as a percentage of revenue, and what might it suggest?",
           "Operating expenses = 140 − 36 = FCFA 104 m; 104 ÷ 400 × 100 = 26% of revenue. It suggests overheads (distribution, administration) take a large share of gross profit; controlling them could raise ROCE without new investment."),
        PQ("Using Case 1, explain one way the founder's attitude to debt affects the choice between options A and B.",
           "Option A costs FCFA 80 m, more than the firm may be able to fund internally, so it probably needs a loan, raising gearing and interest costs; the founder's dislike of debt makes A harder to accept. Option B costs only FCFA 20 m and could be paid from retained profit, which fits the founder's preference, even though its NPV is lower."),
        PQ("Draw up a short SWOT for Mbe Juices from the case.",
           "Strengths: family control and stable management; 35% gross margin; low gearing (20%). Weaknesses: full capacity (95%); dependence on one line; possible high overheads. Opportunities: export market (Gabon); growth target supported by positive-NPV projects. Threats: price-cutting local rivals; export risks (agent, borders, exchange)."),
        SUM("Paper 3 is a business case study; check the exact format with your teacher.",
            "Skim, read closely, annotate objectives, stakeholders, problems and data.",
            "Use the appendices: calculate ratios, NPV, break-even, utilization, gearing and use them in arguments.",
            "Apply tools to this business only; general answers score poorly.",
            "Recommend: compare options against objectives and constraints, justify, and say what the decision depends on."),
    ],
))
