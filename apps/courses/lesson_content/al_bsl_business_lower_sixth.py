"""A Level Business Studies, Lower Sixth: lessons (KKEVO draft from the master curriculum blueprint; a reviewer should check them against the Board syllabus and textbooks)."""

from .dsl import *  # noqa: F403

COURSE = ("business-studies", "lower-sixth")

M1 = "Enterprise & the Business Environment"
M2 = "Management Theory & Organizational Design"
M3 = "Leadership, Motivation & Human Resource Management"
M4 = "Marketing Management & Strategy"
MX = "Examination"

LESSONS = []

# ---------------------------------------------------------------------------
# M1 / The nature of business activity and enterprise
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M1, topic="The nature of business activity and enterprise",
    title="Business activity, added value and the entrepreneur",
    slug="bsl-business-activity-added-value-enterprise",
    minutes=21,
    summary="What a business does, how it creates added value, how activity moves through the sectors of the economy, and what an entrepreneur contributes, risks and gains.",
    objectives=[
        "Explain the purpose of business activity and the role of the factors of production",
        "Calculate added value and explain how a business can increase it",
        "Classify activity into primary, secondary, tertiary and quaternary sectors and explain structural change",
        "Evaluate the qualities, risks and rewards of entrepreneurs, including in the informal sector",
    ],
    key_concepts=["Business activity", "Factors of production", "Added value", "Opportunity cost",
                  "Sectors of production", "Enterprise", "Entrepreneur", "Informal sector"],
    blocks=[
        H("Introduction"),
        T("A woman in Bafoussam buys raw cassava, peels, grates, presses and roasts it, and sells bags of garri in the market. "
          "She has run a business: she combined resources to make something people want and will pay more for than it cost her.\n\n"
          "At O Level you met the main types of business. At A Level the questions go further: why do businesses exist, how do "
          "they create value, and why do some people take the risk of starting one while others do not?"),
        D("The process of combining resources (inputs) to produce goods or services (outputs) that satisfy the needs and wants "
          "of customers, usually in return for payment.", title="Business activity"),
        D("The resources used to produce goods and services: **land** (natural resources), **labour** (human effort), "
          "**capital** (man-made aids to production such as machines and buildings) and **enterprise** (the risk-taking "
          "and organising of the other three).", title="Factors of production"),
        H("Added value"),
        D("The difference between the selling price of a product and the cost of the bought-in materials and services used "
          "to make it. Added value is not the same as profit, because wages, rent and other overheads must still be paid "
          "out of it.", title="Added value", formula=r"\text{Added value} = \text{Sales revenue} - \text{Cost of bought-in inputs}"),
        EX("Worked example 1: the garri processor", intro="In one month the processor (invented figures) sells garri for "
           "FCFA 750 000. She bought cassava for FCFA 400 000 and bags for FCFA 50 000. Find her added value and express it as a "
           "percentage of sales.", steps=[
            S("Add the bought-in inputs", math=r"400\,000 + 50\,000 = 450\,000 \text{ FCFA}"),
            S("Subtract from sales revenue", math=r"750\,000 - 450\,000 = 300\,000 \text{ FCFA}"),
            S("Percentage of sales", math=r"\frac{300\,000}{750\,000} \times 100 = 40\%"),
            S("Interpret", text="FCFA 300 000 is the value she created. Her own wage, any helper's pay, transport and rent must "
              "come out of it before there is any profit."),
        ]),
        EX("Worked example 2: a tailor in Bamenda", intro="A tailor (invented figures) sells 40 shirts at FCFA 6 000 each. "
           "Fabric cost FCFA 90 000 and thread and buttons FCFA 10 000. Find the added value.", steps=[
            S("Sales revenue", math=r"40 \times 6\,000 = 240\,000 \text{ FCFA}"),
            S("Bought-in inputs", math=r"90\,000 + 10\,000 = 100\,000 \text{ FCFA}"),
            S("Added value", math=r"240\,000 - 100\,000 = 140\,000 \text{ FCFA}"),
        ]),
        KEY("Ways to increase added value", "A business can raise the price customers will pay, or lower the cost of inputs, "
            "without losing what customers value.", cards=[
            ["Raise what customers pay", "Branding, better design, packaging, convenience, after-sales service, a quality label."],
            ["Lower input cost", "Cheaper suppliers, less waste, buying in bulk, better stock control."],
            ["Process further", "Selling roasted garri instead of raw cassava, or chocolate instead of cocoa beans."],
        ]),
        H("Sectors of production and structural change"),
        T("**Primary** activity extracts natural resources (farming, fishing, forestry, mining). **Secondary** activity "
          "manufactures or builds (food processing, cement, construction). **Tertiary** activity provides services (banking, "
          "transport, retail, health). Many textbooks add a **quaternary** sector of knowledge-based services such as research "
          "and software; check which classification your textbook uses.\n\n"
          "**Structural change** is the shift in the share of output and employment between sectors over time. As economies "
          "develop, the share of the primary sector usually falls and the tertiary share rises. Products also form a "
          "**chain of production**: cocoa grown (primary), processed (secondary), sold and shipped (tertiary)."),
        H("Opportunity cost and the entrepreneur"),
        D("The value of the next best alternative given up when a choice is made.", title="Opportunity cost"),
        D("A person who identifies a business opportunity, organises resources to exploit it and bears the risk of failure "
          "in return for the chance of profit. **Enterprise** is this willingness to take risks and to innovate.",
          title="Entrepreneur"),
        T("Common qualities of entrepreneurs are initiative, willingness to take calculated risks, resilience after failure, "
          "creativity, and the ability to organise people and money. Their rewards are profit, independence and satisfaction; "
          "their risks include losing their savings, debt, stress and the opportunity cost of a paid job they gave up.\n\n"
          "In Cameroon a large share of activity is in the **informal sector**: small unregistered businesses such as "
          "street trading, small workshops and many farms. Informal businesses are easy to start, but find it harder to borrow, "
          "to win large contracts and to grow."),
        KEY("Why enterprise matters to an economy", "Use these points in evaluation answers.", cards=[
            ["Benefits", "Jobs and incomes, competition and lower prices, innovation, tax revenue once firms register, local supply of goods."],
            ["Limits", "Many new firms fail early; informal firms pay little tax and may avoid labour and safety rules; finance and infrastructure limit growth."],
        ]),
        TIP("Exam link: added value, sectors and entrepreneurship appear in Paper 1 multiple choice and in short Paper 2 "
            "explanations; in a Paper 3 case study you may be asked to assess an entrepreneur's chances of success. Always "
            "use the business in the question."),
        MISTAKE("Treating added value as profit", "Added value only subtracts bought-in inputs. Wages, rent and interest still "
                "have to be paid, so profit is smaller than added value."),
        MISTAKE("Listing qualities without applying them", "Saying 'an entrepreneur must be a risk-taker' earns little. Show "
                "which risk this entrepreneur takes (her savings, a loan) and how it affects the decision."),
        QUIZ("A carpenter sells a table for FCFA 85 000. Wood and varnish cost FCFA 35 000 and he pays an apprentice FCFA "
             "20 000. What is the added value?",
             ["FCFA 30 000", "FCFA 50 000", "FCFA 65 000", "FCFA 85 000"], 1,
             "Added value = 85 000 - 35 000 = FCFA 50 000. The apprentice's wage is paid out of added value; it is not a bought-in input.",
             hint="Subtract only the materials and services bought from other firms.",
             feedback=["This subtracts the wage as well, which gives a profit-type figure, not added value.", "",
                       "This subtracts only the wage, not the bought-in materials.", "This is the selling price, not the value added."]),
        QUIZ("A cocoa farmer in the South West region starts drying and grinding her beans into cocoa powder before selling. "
             "In which way has her business changed?",
             ["She has moved from the tertiary to the primary sector", "She has added secondary activity and can increase added value",
              "She has reduced her added value", "She has become a quaternary business"], 1,
             "Processing is secondary activity; selling a processed product usually raises added value.",
             feedback=["Farming is primary; she has not moved into services.", "", "Processing usually increases added value because customers pay more.",
                       "Quaternary refers to knowledge-based services such as research."]),
        PQ("A business buys inputs worth FCFA 1.2 million and sells its output for FCFA 2 million. Calculate its added value "
           "and explain one reason why its profit will be lower than this figure.",
           "Added value = 2 000 000 - 1 200 000 = FCFA 800 000. Profit is lower because wages, rent, interest and other "
           "overheads are paid out of added value."),
        PQ("Explain two ways in which a palm oil producer could increase added value.",
           "(1) Refine and bottle the oil under a brand and sell to supermarkets at a higher price per litre. (2) Cut waste "
           "in pressing so less fruit is bought per litre. Each raises the gap between price and the cost of bought-in inputs."),
        PQ("Discuss whether entrepreneurs are the most important factor of production in a developing economy.",
           "Plan: define enterprise and the other factors. For: entrepreneurs combine the other factors, spot opportunities, "
           "create jobs and innovate. Against: without capital (finance, roads, electricity) and skilled labour, enterprise "
           "cannot grow; many informal firms stay small. Judgement: enterprise is necessary but not sufficient; its importance "
           "depends on access to finance and infrastructure."),
        SUM("Business activity combines land, labour, capital and enterprise to satisfy wants.",
            "Added value = sales revenue - cost of bought-in inputs; it is not profit.",
            "Added value rises with branding, quality, processing and lower input costs.",
            "Activity is primary, secondary, tertiary (and in some books quaternary); structures shift as economies develop.",
            "Entrepreneurs take risks for profit and independence; their opportunity cost is the next best alternative given up."),
    ],
))


# ---------------------------------------------------------------------------
# M1 / Legal forms of business
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M1, topic="Legal forms of business",
    title="Legal forms of business under OHADA: liability, ownership and choice",
    slug="bsl-legal-forms-under-ohada",
    minutes=22,
    summary="The OHADA legal forms used in Cameroon (individual trader, SNC, SCS, SARL, SA, SAS, GIE, cooperative), what limited liability and legal personality mean, and how an owner chooses a form.",
    objectives=[
        "Explain unincorporated and incorporated businesses, legal personality and limited liability",
        "Compare the main OHADA legal forms: individual trader, SNC, SCS, SARL, SA, SAS and GIE",
        "Work out who bears losses when a business fails under different legal forms",
        "Recommend and justify a legal form for a given business",
    ],
    key_concepts=["OHADA", "Unlimited liability", "Limited liability", "Legal personality", "RCCM",
                  "SARL", "SA", "SAS", "GIE", "Divorce of ownership and control"],
    blocks=[
        H("Introduction"),
        T("Two friends in Buea want to open a printing shop. One will put in FCFA 3 million, the other FCFA 2 million and her "
          "skills. Should they trade as partners, or form a company? If the shop fails, could they lose their houses? The legal "
          "form they choose answers these questions.\n\n"
          "In Cameroon, company law comes mainly from **OHADA**, the Organisation for the Harmonisation of Business Law in "
          "Africa. Its Uniform Acts apply directly in the member states, including Cameroon. The Uniform Act on commercial "
          "companies and economic interest groups was revised in 2014."),
        D("A business with **legal personality** (it is a separate legal person) can own property, sign contracts, sue and be "
          "sued in its own name. A company gains legal personality when it is registered in the Trade and Personal Property "
          "Credit Register (**RCCM**). An unincorporated business (an individual trader) has no separate personality: the "
          "owner and the business are the same person in law.", title="Legal personality"),
        D("**Unlimited liability**: the owner is personally responsible for all the business's debts, so personal assets can be "
          "taken to pay creditors. **Limited liability**: an owner can lose only the money they invested (their contribution "
          "to the capital).", title="Liability"),
        H("The main forms"),
        KEY("Unincorporated and partnership forms", "Simple to set up, but owners carry heavy personal risk.", cards=[
            ["Individual trader", "One owner, full control, keeps all profit; unlimited liability; limited capital. OHADA's general commercial law also has a simplified 'entreprenant' status for very small activities."],
            ["SNC (general partnership)", "All partners are traders and are jointly and severally liable without limit for the firm's debts; shares cannot be transferred freely."],
            ["SCS (limited partnership)", "Active (general) partners have unlimited liability and manage; sleeping (limited) partners risk only their contribution and do not manage."],
        ]),
        KEY("Company forms", "Separate legal persons; associates or shareholders have limited liability.", cards=[
            ["SARL", "Private limited liability company; can have a single associate; run by one or more managers (gérants); shares (parts sociales) are not freely sold to outsiders."],
            ["SA", "Joint-stock (public limited) company; can raise large capital; run by a board of directors or a general administrator; only an SA can offer shares to the public."],
            ["SAS", "Simplified joint-stock company, introduced by the 2014 revision; the articles set the rules for management, giving great flexibility."],
        ]),
        D("A **GIE** (economic interest group) lets existing businesses pool activities, such as joint buying or export, to "
          "help their own activity; it is not mainly for making profit for itself and can be formed without capital. Its members "
          "remain liable for its debts. **Cooperatives** (governed by a separate OHADA Uniform Act) are owned and run by their "
          "members, often farmers, on the principle of one member, one vote.", title="GIE and cooperatives"),
        TIP("The Uniform Act sets minimum capital rules (for the SA, and for the SARL with room for national rules). The "
            "amounts can change, so check the current figures with your teacher before quoting a number."),
        H("Who bears the loss?"),
        EX("Worked example 1: an SARL fails", intro="An SARL in Douala (invented figures) has capital of FCFA 5 million: "
           "associate A put in FCFA 3 million and B FCFA 2 million. It closes owing creditors FCFA 12 million. Its assets are "
           "sold for FCFA 7 million. Who bears the loss?", steps=[
            S("Creditors are paid from the company's assets", math=r"7\,000\,000 \text{ paid out of } 12\,000\,000"),
            S("Unpaid debts", math=r"12\,000\,000 - 7\,000\,000 = 5\,000\,000 \text{ FCFA}"),
            S("Apply limited liability", text="A and B lose their contributions (3 million and 2 million) but their houses and "
              "savings are safe, because the company is a separate person."),
            S("Conclusion", text="The creditors bear the unpaid FCFA 5 million. This is why lenders often ask the owners of a "
              "small SARL for a personal guarantee, which removes some of the protection."),
        ]),
        EX("Worked example 2: an individual trader fails", intro="A trader owes FCFA 4 million. The business assets sell for "
           "FCFA 1.5 million. How much can creditors claim from her personal assets?", steps=[
            S("Shortfall", math=r"4\,000\,000 - 1\,500\,000 = 2\,500\,000 \text{ FCFA}"),
            S("Apply unlimited liability", text="She and her business are one person in law, so creditors can claim the "
                                                "FCFA 2.5 million from her personal property."),
        ]),
        H("Ownership and control"),
        T("In a small SARL the associates usually manage the business themselves. In a large SA, thousands of shareholders own "
          "the company but directors and managers run it: this is the **divorce (separation) of ownership and control**. It "
          "can cause a **principal-agent problem**: managers (agents) may pursue their own goals, such as higher pay or size, "
          "rather than the owners' (principals') goals."),
        EX("Worked example 3: choosing a legal form", intro="Recommend a legal form for the two friends opening the Buea "
           "printing shop.", steps=[
            S("Identify their needs", text="Two owners, FCFA 5 million capital, a risk of debts from buying machines, a wish to keep control."),
            S("Reject the SNC", text="Unlimited joint and several liability would put both friends' personal assets at risk."),
            S("Reject the SA", text="Built for raising large capital from many shareholders; more formalities than they need."),
            S("Recommend", text="An SARL with two associates: limited liability, both can be managers, shares stay within the "
              "business. An SAS is an alternative if they want flexible rules for management or future investors."),
        ]),
        MISTAKE("Thinking limited liability means the company's debts disappear", "The company itself must still pay all its debts "
                "out of its assets; limited liability only protects the owners' personal property beyond their contribution."),
        MISTAKE("Calling every company a 'public company'", "Only the SA can offer its shares to the public. An SARL is a private "
                "company whose parts sociales are not freely sold to outsiders."),
        QUIZ("Which OHADA form gives some partners limited liability and others unlimited liability?",
             ["SNC", "SCS", "SARL", "GIE"], 1,
             "In an SCS, active partners have unlimited liability and sleeping partners limited liability.",
             feedback=["In an SNC every partner has unlimited, joint and several liability.", "",
                       "In an SARL every associate has limited liability.", "GIE members remain liable for its debts; the group is for pooling activity."]),
        QUIZ("Why do banks often ask the owners of a small SARL for a personal guarantee?",
             ["Because an SARL has unlimited liability", "To reduce the risk created by the owners' limited liability",
              "Because an SARL cannot own property", "Because SARL shares are sold on a stock exchange"], 1,
             "Limited liability shifts risk to creditors, so a lender asks for a personal guarantee to recover that protection.",
             feedback=["An SARL gives its associates limited liability.", "", "A registered SARL is a legal person and can own property.",
                       "SARL shares are not offered to the public."]),
        PQ("Distinguish between an SNC and an SARL.",
           "SNC: a partnership whose partners are traders with unlimited, joint and several liability; shares not freely "
           "transferable. SARL: a company with legal personality whose associates have limited liability; can have one associate; "
           "managed by gérants. Key difference: personal risk of the owners."),
        PQ("An individual trader's business owes FCFA 6 million and its assets are worth FCFA 2.2 million. Calculate how much "
           "creditors can claim from her personal assets and explain why.",
           "6 000 000 - 2 200 000 = FCFA 3 800 000. She has unlimited liability: she and the business are one legal person, so "
           "creditors can claim against her personal property."),
        PQ("A successful family SARL making furniture wants to build a large factory. Discuss whether it should convert into an SA.",
           "Plan: For: an SA can raise large capital from many shareholders and, if it meets the conditions, offer shares to the "
           "public; greater status with banks and suppliers. Against: more formalities and disclosure, cost of conversion, risk "
           "that the family loses control and the divorce of ownership and control. Alternatives: loans, retained profit, an SAS "
           "with selected investors. Judgement: convert only if the capital needed cannot be raised while keeping control."),
        SUM("OHADA Uniform Acts govern company law in Cameroon; companies gain legal personality on registration in the RCCM.",
            "Individual traders and SNC partners have unlimited liability; in an SCS only sleeping partners are limited.",
            "SARL, SA and SAS associates or shareholders have limited liability; only an SA can offer shares to the public.",
            "A GIE pools members' activities; cooperatives are member-owned on one member, one vote.",
            "The choice depends on risk, capital needed, control and formalities; large companies face a divorce of ownership and control."),
    ],
))


# ---------------------------------------------------------------------------
# M1 / Business objectives and social responsibility
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M1, topic="Business objectives and social responsibility",
    title="Mission, SMART objectives and corporate social responsibility",
    slug="bsl-objectives-and-csr",
    minutes=21,
    summary="How mission statements, aims and SMART objectives fit together, why firms pursue profit, survival, growth or market share, and how to evaluate corporate social responsibility.",
    objectives=[
        "Explain the hierarchy of mission, aims, objectives, strategy and tactics",
        "Write and judge SMART objectives and calculate simple objective targets",
        "Compare profit maximisation, satisficing, survival, growth and market share objectives",
        "Evaluate corporate social responsibility using Carroll's pyramid and the triple bottom line",
    ],
    key_concepts=["Mission statement", "SMART objectives", "Profit maximisation", "Satisficing",
                  "Corporate social responsibility", "Carroll's pyramid", "Triple bottom line", "Social enterprise"],
    blocks=[
        H("Introduction"),
        T("A water-bottling firm near Buea says its mission is 'safe, affordable water for every home'. Its managers also need a "
          "target for next year: how many litres, at what profit, by when? And what should it do about the plastic bottles that "
          "end up in rivers? This lesson links what a business says it wants with what it actually measures."),
        D("A short statement of the business's purpose and values, meant to guide staff and inform stakeholders. It is general "
          "and usually not measurable.", title="Mission statement"),
        KEY("The hierarchy of objectives", "Each level turns the one above into something more specific.", cards=[
            ["Mission and aims", "Long-term purpose and broad intentions."],
            ["Corporate objectives", "Measurable targets for the whole business."],
            ["Functional objectives", "Targets for marketing, operations, finance and people that support the corporate ones."],
            ["Strategy and tactics", "The long-term plan and the short-term actions used to reach the objectives."],
        ]),
        D("Objectives that are **S**pecific, **M**easurable, **A**chievable (agreed), **R**ealistic (relevant) and **T**ime-bound. "
          "Textbooks differ slightly on the A and R words; check your textbook.", title="SMART objectives"),
        EX("Worked example 1: making an objective SMART", intro="'We want to grow' is the bottling firm's objective. Rewrite it "
           "and set a numerical target.", steps=[
            S("Choose a measure", text="Market share of bottled water sales in the South West region."),
            S("Current position (invented)", math=r"\frac{120}{800} \times 100 = 15\% \text{ (sales and market in FCFA million)}"),
            S("Target", text="Raise market share from 15% to 20% by the end of next year."),
            S("Sales needed if the market stays at FCFA 800 million", math=r"0.20 \times 800 = 160 \text{ million FCFA}"),
        ]),
        H("Types of corporate objective"),
        T("**Profit maximisation**: producing where marginal revenue equals marginal cost, so the profit from one more unit is "
          "zero. In practice managers rarely know MR and MC exactly. **Satisficing**: aiming for a satisfactory profit that keeps "
          "owners content while managers pursue other goals, a common result of the divorce of ownership and control. "
          "**Survival**: the main aim of new firms and of firms in a crisis. **Growth** and **market share**: bring economies of "
          "scale and market power. **Social and ethical objectives**: important for cooperatives and social enterprises."),
        EX("Worked example 2: a profit margin objective", intro="A firm (invented figures) earns profit of FCFA 18 million on "
           "sales of FCFA 150 million. Its objective was a 10% profit margin. Has it met the objective?", steps=[
            S("Profit margin", math=r"\frac{18}{150} \times 100 = 12\%"),
            S("Compare", text="12% is above the 10% target, so the objective is met."),
        ]),
        H("Corporate social responsibility (CSR)"),
        D("The idea that a business should take account of the effects of its decisions on society and the environment, not only "
          "on its owners, and go beyond what the law requires.", title="Corporate social responsibility"),
        KEY("Carroll's pyramid of CSR (Archie Carroll)", "Four layers, from the base upwards.", cards=[
            ["Economic", "Be profitable: the foundation that allows everything else."],
            ["Legal", "Obey the law (labour, tax, environmental rules)."],
            ["Ethical", "Do what is right and fair even where the law does not require it."],
            ["Philanthropic", "Contribute to the community: schools, health, sport."],
        ]),
        T("The **triple bottom line** (associated with John Elkington) asks a business to report on people, planet and profit, "
          "not profit alone. A **social enterprise** is a business whose main objective is social or environmental, using any "
          "surplus mainly for that purpose."),
        KEY("Evaluating CSR", "A balanced answer weighs both sides for the business in the case.", cards=[
            ["Benefits", "Better reputation and brand loyalty; easier recruitment and motivation; good relations with government and communities; lower risk of fines and protests."],
            ["Costs and doubts", "Higher costs reduce short-term profit; may be only public relations ('greenwashing'); some argue managers should simply maximise profit within the law."],
        ]),
        TIP("Exam link: Paper 2 often asks you to 'discuss' or 'evaluate' CSR. Use the business's objectives, its stakeholders "
            "and its finances to decide whether CSR is worth its cost in that case."),
        MISTAKE("Writing a vague 'SMART' objective", "'Increase sales soon' is neither measurable nor time-bound. Give a number, a "
                "measure and a date."),
        MISTAKE("Assuming every firm maximises profit", "New firms aim to survive; managers in large firms may satisfice; "
                "cooperatives serve members. Name the objective that fits the case."),
        QUIZ("Which objective is SMART?",
             ["Become the best bakery in Bamenda", "Increase sales revenue by 8% by 31 December next year",
              "Improve customer service", "Cut costs as much as possible"], 1,
             "It is specific, measurable (8%), achievable and time-bound (31 December).",
             feedback=["'Best' is not measurable and has no deadline.", "", "No measure and no time limit.",
                       "No target figure and no date."]),
        QUIZ("Managers of a large SA aim for a profit that keeps shareholders content while expanding the firm's size. This is",
             ["profit maximisation", "satisficing", "survival", "philanthropy"], 1,
             "Satisficing means aiming for a satisfactory level rather than the maximum.",
             feedback=["They are not aiming for maximum profit.", "", "The firm is not in danger.", "Philanthropy is giving to the community."]),
        PQ("A firm's market is worth FCFA 2 billion and its sales are FCFA 300 million. Calculate its market share and the "
           "sales needed for a 20% share if the market does not change.",
           "Share = 300 / 2 000 x 100 = 15%. Target sales = 0.20 x 2 000 million = FCFA 400 million."),
        PQ("Explain why a new business is more likely to have survival rather than profit maximisation as its main objective.",
           "A new firm has few customers, uncertain cash flow and high start-up costs; running out of cash would end it, so it "
           "first aims to cover costs and build a customer base. Profit becomes the focus once it is established."),
        PQ("Evaluate whether a mining company operating in Cameroon should spend money on CSR.",
           "Plan: define CSR. For: licence to operate with local communities; reputation with government and buyers; fewer "
           "conflicts and protests; easier recruitment. Against: cost reduces profit and dividends; benefits are hard to measure; "
           "risk of being seen as greenwashing. Judgement: for a firm whose operations visibly affect land and water, CSR is "
           "close to essential for long-run profit, provided it is genuine and linked to its impact."),
        SUM("Mission and aims are broad; objectives turn them into measurable targets; strategy and tactics deliver them.",
            "Good objectives are SMART: specific, measurable, achievable, realistic and time-bound.",
            "Firms may aim for profit maximisation (MR = MC), satisficing, survival, growth, market share or social goals.",
            "CSR means considering society and the environment beyond the law; Carroll's pyramid has economic, legal, ethical and philanthropic layers.",
            "Evaluate CSR by weighing reputation and long-run gains against short-run cost and the risk of greenwashing."),
    ],
))


# ---------------------------------------------------------------------------
# M1 / Stakeholders
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M1, topic="Stakeholders",
    title="Stakeholders: interests, conflict and Mendelow's matrix",
    slug="bsl-stakeholders-conflict-mendelow",
    minutes=20,
    summary="Who the stakeholders of a business are, what each wants, why their objectives conflict, and how managers use Mendelow's power-interest matrix to prioritise them.",
    objectives=[
        "Distinguish shareholders from stakeholders and internal from external stakeholders",
        "Explain the objectives of each stakeholder group and where they conflict",
        "Use Mendelow's matrix to map and prioritise stakeholders",
        "Evaluate the shareholder and stakeholder views of the business",
    ],
    key_concepts=["Stakeholder", "Shareholder", "Internal stakeholder", "External stakeholder",
                  "Stakeholder conflict", "Mendelow's matrix", "Shareholder concept", "Stakeholder concept"],
    blocks=[
        H("Introduction"),
        T("A brewery plans to close its depot in a small town and serve customers from Douala. Shareholders expect lower costs. "
          "Depot workers fear losing their jobs. Local traders who sell to the workers worry about lost trade. The local council "
          "loses a taxpayer. One decision touches many groups: these are the business's stakeholders."),
        D("Any individual or group with an interest in, or affected by, the activities of a business. **Shareholders** (or "
          "associates in an SARL) are one stakeholder group: the owners.", title="Stakeholder"),
        KEY("Stakeholder groups and their main interests", "Internal groups are inside the business; external groups are outside it.", cards=[
            ["Internal", "Owners (profit, dividends, share value); managers (pay, status, career); employees (pay, security, conditions)."],
            ["External", "Customers (price, quality); suppliers (orders, prompt payment); lenders (repayment, interest); government (taxes, jobs, law); local community (jobs, environment)."],
        ]),
        H("Conflict between stakeholders"),
        T("Stakeholder objectives often conflict. Higher wages raise costs and may cut dividends. Lower prices please customers "
          "but squeeze suppliers and profit. Expansion brings jobs but may damage the local environment. Objectives can also "
          "coincide: a profitable firm can pay better wages and more tax."),
        EX("Worked example 1: analysing a conflict", intro="A cocoa processor (invented case) plans to automate its packing line, "
           "cutting 40 jobs but lowering unit costs by 15%. Analyse the stakeholder conflict.", steps=[
            S("Who gains", text="Shareholders (higher profit), customers (possibly lower prices), and the machine supplier."),
            S("Who loses", text="The 40 workers and their families; local traders who depend on their spending; perhaps trade unions' influence."),
            S("Mixed", text="Government gains tax from profit but loses income tax and social security contributions from the jobs, and may face unemployment."),
            S("Possible compromise", text="Retrain and redeploy some workers, phase the change in, or offer voluntary redundancy."),
        ]),
        H("Mendelow's power-interest matrix"),
        T("Aubrey Mendelow's matrix maps stakeholders by their **power** to affect the business and their **interest** in a "
          "particular decision. The position tells managers how to handle each group."),
        IMG("albsl-mendelow-matrix.svg", alt="Two by two grid with power on the vertical axis and level of interest on the horizontal axis. "
            "Low power, low interest: monitor. High power, low interest: keep satisfied. Low power, high interest: keep informed. "
            "High power, high interest: manage closely.", caption="Figure 1. Mendelow's power-interest matrix."),
        EX("Worked example 2: mapping stakeholders for the depot closure", intro="Place each group in Mendelow's matrix for the brewery's depot closure.", steps=[
            S("Major shareholders", text="High power, high interest: manage closely (key players)."),
            S("Depot workers and their union", text="High interest; power depends on union strength. A strong union may move them to 'manage closely'."),
            S("Local council", text="Some power (permits, local taxes), moderate interest: keep satisfied."),
            S("Customers in the town", text="High interest in supply, low power individually: keep informed."),
            S("General public elsewhere", text="Low power, low interest: monitor."),
        ]),
        TIP("Positions are not fixed. A group's power can rise quickly, for example when workers unite in a union or a community "
            "gains media attention. Say this in evaluation."),
        H("The shareholder and stakeholder views"),
        T("The **shareholder concept** says a business exists to maximise returns to its owners within the law. The "
          "**stakeholder concept** says it should balance the interests of all groups affected. Supporters argue the stakeholder "
          "approach builds loyalty and long-run profit; critics say it blurs accountability, since managers cannot serve every "
          "group at once."),
        MISTAKE("Using 'stakeholder' and 'shareholder' as the same word", "Shareholders own the company; stakeholders are every "
                "group affected. All shareholders are stakeholders, but not the other way round."),
        MISTAKE("Listing stakeholders without analysing conflict", "Examiners reward explaining why two groups want different "
                "things in the case and how the business might resolve it."),
        QUIZ("Which stakeholder is external to the business?", ["A manager", "An employee", "A supplier", "An owner"], 2,
             "Suppliers are outside the organisation.",
             feedback=["Managers work inside the business.", "Employees are internal.", "", "Owners are internal stakeholders."]),
        QUIZ("In Mendelow's matrix, a group with high power but low interest in a decision should be",
             ["managed closely", "kept satisfied", "kept informed", "ignored"], 1,
             "High power, low interest: keep them satisfied so they do not use their power against the decision.",
             feedback=["This is for high power and high interest.", "", "This is for low power and high interest.",
                       "No group is simply ignored; low-low groups are monitored."]),
        PQ("Explain one conflict between employees and shareholders when a firm decides to increase dividends.",
           "Higher dividends leave less retained profit for wage rises, training or job security, so employees may lose out while shareholders gain."),
        PQ("Explain why a supplier's interest in a business may increase when the business is short of cash.",
           "The supplier is owed money (trade credit); if the business delays payment or fails, the supplier may not be paid, "
           "so it watches the business closely and may shorten credit terms."),
        PQ("'A business should always put shareholders first.' Discuss.",
           "Plan: define shareholder and stakeholder concepts. For: owners carry the risk and appoint directors; clear objective; "
           "profit funds everything else. Against: ignoring workers, customers and communities can harm reputation and long-run "
           "profit; the law and CSR demand wider responsibility. Judgement: in the long run serving key stakeholders usually "
           "serves shareholders too; conflicts must be handled case by case using a tool such as Mendelow's matrix."),
        SUM("Stakeholders are all groups affected by a business; shareholders are the owners.",
            "Internal: owners, managers, employees; external: customers, suppliers, lenders, government, community.",
            "Objectives often conflict (wages v dividends, prices v profit, growth v environment) but can coincide.",
            "Mendelow's matrix: manage closely, keep satisfied, keep informed, monitor; positions can change.",
            "The shareholder view puts owners first; the stakeholder view balances all groups."),
    ],
))


# ---------------------------------------------------------------------------
# M1 / The external environment
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M1, topic="The external environment",
    title="PESTLE and the macroeconomic environment of business",
    slug="bsl-external-environment-pestle-macro",
    minutes=22,
    summary="How PESTLE factors and macroeconomic changes (interest rates, inflation, exchange rates, growth and unemployment) affect businesses in Cameroon, with calculations on loans, imports and real wages.",
    objectives=[
        "Use PESTLE to analyse the external environment of a business",
        "Explain how interest rates, inflation, exchange rates, economic growth and unemployment affect businesses",
        "Calculate the effect of interest-rate and exchange-rate changes on costs",
        "Evaluate which external factor matters most for a given business",
    ],
    key_concepts=["PESTLE", "Interest rate", "Inflation", "Exchange rate", "CFA franc peg",
                  "Business cycle", "Unemployment", "Real income"],
    blocks=[
        H("Introduction"),
        T("A Garoua firm that imports spare parts from China, borrows from a bank and sells to farmers cannot control the "
          "exchange rate, the interest rate, the rainfall or new tax rules. These are part of its **external environment**. "
          "Good managers cannot change them, but they can anticipate them and plan."),
        D("A framework for analysing the external environment under six headings: **P**olitical, **E**conomic, **S**ocial, "
          "**T**echnological, **L**egal and **E**nvironmental factors.", title="PESTLE"),
        KEY("PESTLE examples for a Cameroonian business", "Use factors that fit the business in the question.", cards=[
            ["Political and legal", "Tax changes in the annual Finance Law, trade agreements, labour law, product standards, business registration rules."],
            ["Economic", "Interest rates, inflation, exchange rates, growth, unemployment, consumer incomes."],
            ["Social", "Population growth, urbanisation, tastes, attitudes to health, the use of both English and French."],
            ["Technological and environmental", "Mobile money, internet access, automation; climate, flooding, pollution rules, waste."],
        ]),
        H("Interest rates"),
        T("In the CEMAC zone, the central bank is the **BEAC** (Bank of Central African States). Its policy rate influences the "
          "rates commercial banks charge. Higher interest rates raise the cost of loans and overdrafts, reduce investment, and "
          "reduce consumer spending on goods bought on credit. They may also encourage saving."),
        EX("Worked example 1: the cost of a loan", intro="A firm has a loan of FCFA 20 million. Its bank raises the annual "
           "interest rate from 7% to 9% (invented teaching rates). Find the change in annual interest.", steps=[
            S("Interest at 7%", math=r"0.07 \times 20\,000\,000 = 1\,400\,000 \text{ FCFA}"),
            S("Interest at 9%", math=r"0.09 \times 20\,000\,000 = 1\,800\,000 \text{ FCFA}"),
            S("Change", math=r"1\,800\,000 - 1\,400\,000 = 400\,000 \text{ FCFA a year}", text="This comes straight out of profit unless the firm raises prices."),
        ]),
        H("Exchange rates"),
        D("The price of one currency in terms of another. The CFA franc used in Cameroon is pegged to the euro at a fixed rate of "
          "**1 euro = 655.957 FCFA**. Against the euro the rate does not move; against other currencies such as the US dollar or "
          "the Chinese yuan it moves whenever the euro moves.", title="Exchange rate"),
        EX("Worked example 2: importing from Europe and from the USA", intro="(a) A firm buys a machine priced at 20 000 euros. "
           "(b) It also buys parts priced at 5 000 US dollars; the rate moves from 600 FCFA to 560 FCFA per dollar (invented "
           "rates). Find the FCFA costs.", steps=[
            S("(a) Euro import at the fixed rate", math=r"20\,000 \times 655.957 = 13\,119\,140 \text{ FCFA}"),
            S("(b) Dollar import before", math=r"5\,000 \times 600 = 3\,000\,000 \text{ FCFA}"),
            S("(b) Dollar import after", math=r"5\,000 \times 560 = 2\,800\,000 \text{ FCFA}"),
            S("Interpret", text="The FCFA has strengthened against the dollar, so imports priced in dollars are FCFA 200 000 "
              "cheaper. Exporters selling in dollars receive fewer FCFA per dollar earned."),
        ]),
        TIP("Remember the rule: a stronger currency makes imports cheaper and exports dearer (or less profitable) and a weaker "
            "currency does the opposite. Trade with the euro area carries no exchange-rate risk because of the peg."),
        H("Inflation, growth and unemployment"),
        T("**Inflation** is a sustained rise in the general price level. It raises input costs, reduces the real value of wages "
          "and makes planning harder. **Real income** changes by roughly the money change minus inflation. **Economic growth** "
          "raises incomes and demand, especially for income-elastic goods; a **recession** does the opposite. The **business "
          "cycle** moves through boom, downturn, recession and recovery. **Unemployment** lowers demand but makes recruitment "
          "easier and wage pressure lower."),
        EX("Worked example 3: real wages", intro="Workers get a 4% pay rise while inflation is 6%. What happens to their real wage?", steps=[
            S("Approximate change", math=r"4\% - 6\% \approx -2\%"),
            S("Exact change", math=r"\frac{1.04}{1.06} - 1 \approx -0.0189 = -1.89\%"),
            S("Effect on business", text="Customers can buy less, so demand for non-essential goods falls; workers may press for higher pay."),
        ]),
        MISTAKE("Saying the FCFA 'falls against the euro'", "The CFA franc is pegged to the euro at 655.957. It moves against the "
                "dollar, yuan or naira, not against the euro, unless the peg itself is changed."),
        MISTAKE("Listing PESTLE factors without impact", "Each factor must be linked to costs, revenue, demand or risk for the "
                "business in the case, and you should say which matters most."),
        QUIZ("A Cameroonian firm imports goods priced in US dollars. The CFA franc weakens against the dollar. What happens?",
             ["Its imports become cheaper in FCFA", "Its imports become dearer in FCFA",
              "Nothing, because the FCFA is pegged to the dollar", "Its exports to France become dearer"], 1,
             "A weaker FCFA buys fewer dollars, so each dollar of imports costs more FCFA.",
             feedback=["That happens when the FCFA strengthens.", "", "The FCFA is pegged to the euro, not the dollar.",
                       "Trade with France is in euros at the fixed rate."]),
        QUIZ("Which business is likely to be hurt most by a rise in interest rates?",
             ["A cash-rich retailer with no debt", "A highly indebted builder selling houses bought with mortgages",
              "A barber who rents a chair", "A firm that holds large bank deposits"], 1,
             "It pays more interest on its own debt and its customers' borrowing costs rise, so demand falls.",
             feedback=["With no debt it pays no extra interest.", "", "Small, cash-based service with little borrowing.",
                       "It earns more interest on deposits."]),
        PQ("A firm imports a machine costing 35 000 euros. Calculate the cost in FCFA.",
           "35 000 x 655.957 = FCFA 22 958 495."),
        PQ("Explain how a recession in Cameroon might affect a business selling motorbikes.",
           "Incomes fall and unemployment rises, so demand for motorbikes (often bought on credit and income-elastic) falls; "
           "the business may cut prices, hold more unsold stock and face cash-flow problems."),
        PQ("Discuss which external factor is most important for a small exporter of dried fruit to Europe and Nigeria.",
           "Plan: Exchange rates: euro sales safe because of the peg, but naira sales are exposed to swings. Political and legal: "
           "border rules, standards in Europe. Environmental: weather affects harvests. Economic: demand in the export markets. "
           "Judgement: for Nigerian sales the exchange rate and border rules are likely to matter most; for European sales, "
           "quality standards and weather matter more than the exchange rate."),
        SUM("PESTLE: political, economic, social, technological, legal and environmental factors.",
            "Higher interest rates raise borrowing costs and reduce investment and credit-based demand.",
            "The FCFA is pegged at 1 euro = 655.957 FCFA; it floats against other currencies with the euro.",
            "A stronger currency makes imports cheaper and exports less competitive; a weaker one does the opposite.",
            "Inflation reduces real incomes; growth raises demand; recession and unemployment reduce it."),
    ],
))


# ---------------------------------------------------------------------------
# M2 / Classical management theories
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M2, topic="Classical management theories",
    title="Taylor, Fayol and Weber: the classical school of management",
    slug="bsl-classical-management-taylor-fayol-weber",
    minutes=22,
    summary="The classical theories of management: Taylor's scientific management and differential piece rate, Fayol's functions and principles of management, and Weber's bureaucracy, with their strengths and limits today.",
    objectives=[
        "Explain the main ideas of Taylor's scientific management and calculate pay under a differential piece rate",
        "Describe Fayol's five functions of management and key principles such as unity of command",
        "Describe the features of Weber's bureaucracy",
        "Evaluate the usefulness of classical theories for modern Cameroonian organisations",
    ],
    key_concepts=["Scientific management", "Time and motion study", "Differential piece rate",
                  "Functions of management", "Unity of command", "Scalar chain", "Bureaucracy"],
    blocks=[
        H("Introduction"),
        T("Walk into a bottling plant and you see each worker doing one short task at a set speed, with a supervisor checking "
          "output against a target. Walk into a ministry and you see forms, rules, files and a clear chain of officials. Both "
          "owe much to three thinkers of the late nineteenth and early twentieth centuries: Frederick Taylor, Henri Fayol and "
          "Max Weber. Together they are called the **classical school** of management."),
        H("Frederick Taylor: scientific management"),
        D("An approach that uses careful observation and measurement to find the 'one best way' to do each task, then selects "
          "and trains workers to follow it and pays them according to output. Taylor set out the ideas in *The Principles of "
          "Scientific Management* (1911).", title="Scientific management"),
        T("Taylor's main steps: break each job into small tasks; time and study each movement (**time and motion study**); "
          "design the best method and tools; select workers suited to the task and train them; separate planning (by managers) "
          "from doing (by workers); and pay by results. He assumed workers are motivated mainly by money."),
        D("Taylor's pay system in which workers who reach the standard output are paid a higher rate for **every** unit, while "
          "those below the standard are paid a lower rate for every unit.", title="Differential piece rate"),
        EX("Worked example 1: differential piece rate", intro="A packing plant (invented figures) sets a standard of 80 units a "
           "day. Below 80 the rate is FCFA 250 a unit; at 80 or more it is FCFA 300 a unit for all units. Worker A packs 75 "
           "units and worker B packs 90.", steps=[
            S("Worker A is below standard", math=r"75 \times 250 = 18\,750 \text{ FCFA}"),
            S("Worker B reaches the standard", math=r"90 \times 300 = 27\,000 \text{ FCFA}"),
            S("Effect of the higher rate", math=r"90 \times 250 = 22\,500, \text{ so B gains } 4\,500 \text{ FCFA from the higher rate}"),
            S("Interpret", text="The jump at the standard gives a strong money incentive to reach the target, which is exactly "
              "what Taylor intended."),
        ]),
        H("Henri Fayol: the functions of management"),
        KEY("Fayol's five functions of management", "Fayol, a French mining engineer, described what all managers do.", cards=[
            ["Planning (forecasting)", "Looking ahead and setting objectives and plans."],
            ["Organising", "Arranging people and resources into a structure."],
            ["Commanding", "Directing and instructing staff."],
            ["Coordinating", "Making the parts work together."],
            ["Controlling", "Checking results against plans and correcting."],
        ]),
        T("Fayol also listed fourteen principles of management. The ones most used in exams are **division of work**, "
          "**authority and responsibility** (they go together), **unity of command** (each worker takes orders from one "
          "superior only), **unity of direction**, the **scalar chain** (a clear line of authority from top to bottom), "
          "**centralisation**, **equity**, **stability of tenure** and **esprit de corps** (team spirit)."),
        H("Max Weber: bureaucracy"),
        D("An organisation run on formal written rules, a clear hierarchy of offices, specialised roles, impersonal treatment of "
          "cases, records kept in files, and appointment and promotion on qualifications and merit. Weber, a German sociologist, "
          "saw it as the most rational and efficient form of large organisation.", title="Bureaucracy"),
        EX("Worked example 2: applying the classical ideas", intro="A state-owned water utility has long delays in connecting new "
           "customers. Show how each classical thinker would approach the problem.", steps=[
            S("Taylor", text="Time each step of a connection, design the fastest method, train fitters and pay a bonus per connection completed to standard."),
            S("Fayol", text="Plan targets for connections, organise teams by district, give each fitter one supervisor (unity of command) and control by comparing results with the plan."),
            S("Weber", text="Write clear rules for handling applications in order, keep records of each file, and promote staff on merit."),
        ]),
        KEY("Evaluating the classical school", "A Paper 2 answer needs both sides.", cards=[
            ["Strengths", "Large productivity gains in repetitive work; clear roles and accountability; fairness and consistency through rules; ideas still used in fast-food, factories and call centres."],
            ["Limits", "Treats workers as motivated by money alone; boring, repetitive jobs and alienation; ignores social needs (shown by the human relations school); rigid rules slow decisions and frustrate customers ('red tape')."],
        ]),
        TIP("Exam link: Paper 1 often tests which thinker is linked to which idea; Paper 2 essays ask you to assess the relevance "
            "of classical theory today. Use a real type of organisation, such as a bottling plant or a public office."),
        MISTAKE("Mixing up Taylor and Fayol", "Taylor studied the work on the shop floor (tasks, timing, pay). Fayol studied the "
                "job of the manager (functions and principles). Weber studied the design of the whole organisation."),
        MISTAKE("Using 'bureaucracy' only as an insult", "In Weber's sense it is a model of rational organisation. Discuss its "
                "advantages (consistency, fairness) as well as its problems (rigidity, delay)."),
        QUIZ("Which principle says that each employee should receive orders from only one superior?",
             ["Scalar chain", "Unity of command", "Division of work", "Esprit de corps"], 1,
             "Unity of command is Fayol's principle that each worker has one boss.",
             feedback=["The scalar chain is the line of authority from top to bottom.", "",
                       "Division of work is specialisation.", "Esprit de corps is team spirit."]),
        QUIZ("Using the differential piece rate in Worked example 1, how much does a worker who packs exactly 80 units earn?",
             ["FCFA 20 000", "FCFA 24 000", "FCFA 22 500", "FCFA 27 000"], 1,
             "80 reaches the standard, so all 80 units earn FCFA 300: 80 x 300 = FCFA 24 000.",
             feedback=["This uses the lower rate, but 80 units meets the standard.", "",
                       "This is 90 units at the lower rate.", "This is worker B's pay for 90 units."]),
        PQ("Outline three features of Weber's bureaucracy.",
           "(1) A hierarchy of offices with clear authority. (2) Formal written rules applied impersonally to every case. "
           "(3) Appointment and promotion on qualifications and merit, with records kept in files."),
        PQ("Under a differential piece rate, the standard is 120 units, the low rate is FCFA 150 and the high rate FCFA 180. "
           "Calculate the pay of a worker making 110 units and one making 125 units.",
           "110 x 150 = FCFA 16 500. 125 x 180 = FCFA 22 500."),
        PQ("Evaluate the relevance of Taylor's scientific management to a modern call centre in Douala.",
           "Plan: Relevant: calls timed, scripts (one best way), targets and bonuses per call, close supervision. Limits: staff "
           "are not motivated by money alone; repetitive work raises absence and labour turnover; customers want flexible, "
           "human answers. Judgement: Taylor's methods raise measured productivity, but the centre also needs human relations "
           "ideas (teamwork, recognition) to keep staff and serve customers well."),
        SUM("Taylor: one best way, time and motion study, select and train, separate planning from doing, pay by results.",
            "Under a differential piece rate, reaching the standard earns the higher rate on every unit.",
            "Fayol: plan, organise, command, coordinate, control; principles include unity of command and the scalar chain.",
            "Weber: hierarchy, written rules, specialisation, impersonality, merit and records.",
            "Classical ideas boost efficiency in routine work but ignore social needs and can cause rigidity."),
    ],
))


# ---------------------------------------------------------------------------
# M2 / Human relations and modern management thinkers
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M2, topic="Human relations and modern management thinkers",
    title="Mayo, Drucker and Mintzberg: people, objectives and managerial roles",
    slug="bsl-human-relations-mayo-drucker-mintzberg",
    minutes=21,
    summary="Mayo's Hawthorne studies and the human relations school, Drucker's management by objectives, and Mintzberg's ten managerial roles, compared with the classical school and evaluated.",
    objectives=[
        "Explain the Hawthorne studies and the main conclusions of the human relations school",
        "Explain Drucker's management by objectives and its strengths and limits",
        "Classify Mintzberg's ten managerial roles into interpersonal, informational and decisional groups",
        "Compare classical and human relations approaches in a given case",
    ],
    key_concepts=["Human relations school", "Hawthorne studies", "Hawthorne effect", "Informal group",
                  "Management by objectives", "Knowledge worker", "Mintzberg's managerial roles"],
    blocks=[
        H("Introduction"),
        T("The classical thinkers saw workers as parts of a machine who respond to pay. Later researchers noticed that people at "
          "work also care about their colleagues, being noticed and having a say. This lesson follows that change of view and "
          "two thinkers who described what modern managers actually do."),
        H("Elton Mayo and the Hawthorne studies"),
        T("Between the 1920s and early 1930s, researchers led by Elton Mayo studied workers at the Hawthorne plant of the Western "
          "Electric Company near Chicago. Early experiments changed lighting levels; output rose in both the test group and the "
          "control group, and even when lighting was reduced. Later studies of a small group of women assembling relays found "
          "output rose as rest breaks and conditions changed, and often stayed high when conditions were returned to the "
          "original. A study of a group of men wiring equipment found the group itself set an informal output norm."),
        KEY("Conclusions of the human relations school", "What the studies suggested about motivation.", cards=[
            ["Attention matters", "Workers who feel noticed and consulted work harder: the Hawthorne effect."],
            ["Groups matter", "Informal groups set their own norms of output and behaviour, which can support or resist managers."],
            ["Social needs", "Belonging, recognition and good relations with supervisors motivate, not money alone."],
        ]),
        D("The change in behaviour that occurs because people know they are being studied or given attention, rather than "
          "because of the change being tested.", title="Hawthorne effect"),
        T("Researchers still debate how to interpret the Hawthorne results, since the studies had small groups and many "
          "changing conditions; check your textbook for the detail it expects."),
        H("Peter Drucker: management by objectives"),
        D("A system in which managers and employees agree specific objectives together, the employee works towards them with "
          "some freedom over method, and performance is reviewed against them. Drucker described it in *The Practice of "
          "Management* (1954).", title="Management by objectives (MBO)"),
        T("Drucker also stressed that the purpose of a business is to create a customer, that managers must balance several "
          "objectives rather than profit alone, and that modern economies depend on **knowledge workers** who must be managed "
          "by goals and trust rather than close supervision."),
        H("Henry Mintzberg: what managers really do"),
        T("Mintzberg observed managers at work and found their days fragmented: many short activities, frequent interruptions and "
          "much talking. He grouped what they do into ten roles."),
        KEY("Mintzberg's ten managerial roles", "Three groups.", cards=[
            ["Interpersonal", "Figurehead, leader, liaison."],
            ["Informational", "Monitor, disseminator, spokesperson."],
            ["Decisional", "Entrepreneur, disturbance handler, resource allocator, negotiator."],
        ]),
        EX("Worked example 1: classifying roles", intro="Classify each activity of the manager of a Limbe hotel using Mintzberg's roles.", steps=[
            S("She opens a tourism fair on behalf of the hotel", text="Figurehead (interpersonal)."),
            S("She reads reports on rival hotels' prices", text="Monitor (informational)."),
            S("She deals with a power cut during a wedding", text="Disturbance handler (decisional)."),
            S("She agrees a contract with a tour operator", text="Negotiator (decisional)."),
            S("She tells staff about a new booking policy", text="Disseminator (informational)."),
        ]),
        EX("Worked example 2: model essay plan", intro="'The human relations school has replaced scientific management.' Discuss.", steps=[
            S("Introduction", text="Define both schools; judgement: the human relations approach complements rather than replaces Taylor."),
            S("For", text="Team working, consultation, recognition schemes and MBO are widespread; social needs matter as Mayo showed; knowledge work suits trust and objectives."),
            S("Against", text="Factories, bottling lines and call centres still use timing, targets and piece rates; much work is still measured in Taylor's way."),
            S("Judgement", text="Most organisations blend the two: measured methods for routine tasks, human relations for commitment and service."),
        ]),
        MISTAKE("Saying the Hawthorne studies proved 'lighting does not matter'", "The point was that social factors and attention "
                "affected output, so changes in physical conditions alone could not explain the results."),
        MISTAKE("Confusing MBO with Taylor's targets", "Taylor imposed standards from above. In MBO the objectives are agreed with "
                "the employee, who has freedom over method."),
        QUIZ("A manager meets a delegation of farmers' representatives to agree supply prices. Which Mintzberg role is this?",
             ["Figurehead", "Monitor", "Negotiator", "Disseminator"], 2,
             "Agreeing terms with outside parties is the negotiator role, a decisional role.",
             feedback=["A figurehead performs ceremonial duties.", "A monitor gathers information.", "",
                       "A disseminator passes information to staff."]),
        QUIZ("What is the main lesson of the Hawthorne studies for managers?",
             ["Pay is the only motivator", "Attention, group norms and social needs affect productivity",
              "Lighting should always be reduced", "Workers should be closely supervised at all times"], 1,
             "Mayo's work showed the importance of social factors and of workers feeling valued.",
             feedback=["That is Taylor's view, which the studies challenged.", "",
                       "Output rose even with less light, which pointed to social factors, not lighting itself.",
                       "Close supervision is a classical idea."]),
        PQ("Explain two advantages of management by objectives for a firm employing engineers.",
           "(1) Engineers agree their own goals, which raises commitment and motivation. (2) Objectives link each engineer's work "
           "to the firm's corporate objectives, making performance easy to review and reward."),
        PQ("Explain the role of informal groups in the Hawthorne studies.",
           "In the wiring room, the workers set their own norm of a 'fair day's output' and pressured members not to produce much "
           "more or less. This showed that group norms can matter more than pay incentives."),
        PQ("Discuss whether Mintzberg's view of management is more realistic than Fayol's.",
           "Plan: Fayol describes what managers should do in a logical sequence (plan, organise...). Mintzberg describes what they "
           "actually do: fragmented, verbal, many roles at once. For Mintzberg: based on observation, fits modern busy managers. "
           "For Fayol: still useful as a checklist; Mintzberg's roles can be mapped onto Fayol's functions. Judgement: Mintzberg "
           "is more realistic as a description; Fayol remains useful as a prescription."),
        SUM("Mayo's Hawthorne studies showed attention, groups and social needs affect output (the Hawthorne effect).",
            "The human relations school stresses communication, teamwork and recognition, not pay alone.",
            "Drucker: management by objectives agrees goals with staff; business exists to create customers; knowledge workers.",
            "Mintzberg: ten roles in three groups: interpersonal, informational, decisional.",
            "Modern organisations usually combine classical methods with human relations ideas."),
    ],
))


# ---------------------------------------------------------------------------
# M2 / Organizational structures
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M2, topic="Organizational structures",
    title="Organisational structures: hierarchy, tall and flat, functional and matrix",
    slug="bsl-organisational-structures",
    minutes=22,
    summary="How businesses organise people: hierarchy, chain of command and levels; tall and flat structures and delayering; functional, product, geographical and matrix structures; and the informal organisation.",
    objectives=[
        "Explain hierarchy, chain of command, levels of hierarchy and span of control",
        "Compare tall and flat structures and calculate the managers and levels a structure needs",
        "Compare functional, product, geographical and matrix structures",
        "Recommend a structure for a given business and justify it",
    ],
    key_concepts=["Organisation chart", "Hierarchy", "Chain of command", "Span of control", "Tall structure",
                  "Flat structure", "Delayering", "Matrix structure", "Informal organisation"],
    blocks=[
        H("Introduction"),
        T("When a family bakery in Kumba grows into a company with three branches, a delivery fleet and a finance office, the "
          "owner can no longer decide everything herself. Who reports to whom? Who decides what? The answer is the business's "
          "**organisational structure**, usually drawn as an **organisation chart**."),
        D("**Hierarchy**: the levels of management and authority from the top to the bottom of an organisation. **Chain of "
          "command**: the route by which instructions pass down and information passes up. **Span of control**: the number of "
          "subordinates who report directly to one manager.", title="Key terms"),
        H("Tall and flat structures"),
        IMG("albsl-tall-flat-structures.svg", alt="Two organisation charts. Left, a tall structure where each manager has two "
            "subordinates, giving four levels and a long chain of command. Right, a flat structure where one manager has seven "
            "subordinates, giving two levels and a short chain of command.", caption="Figure 1. A tall structure (narrow spans) and a flat structure (wide spans)."),
        KEY("Tall v flat", "The same number of workers can be organised either way.", cards=[
            ["Tall", "Many levels, narrow spans: close supervision and clear promotion steps, but slow communication, more managers to pay and staff far from decision-makers."],
            ["Flat", "Few levels, wide spans: faster communication, lower management cost and more delegation, but managers may be overloaded and promotion chances fewer."],
        ]),
        EX("Worked example 1: levels and managers", intro="A factory has 64 operatives. Compare a structure with a span of control "
           "of 4 at every level with one using a span of 8.", steps=[
            S("Span 4: supervisors", math=r"64 \div 4 = 16"),
            S("Span 4: managers above them", math=r"16 \div 4 = 4, \quad 4 \div 4 = 1 \text{ director}"),
            S("Span 4 total", text="16 + 4 + 1 = 21 managers; with the operatives there are 4 levels."),
            S("Span 8", math=r"64 \div 8 = 8 \text{ supervisors}, \quad 8 \div 8 = 1 \text{ director}"),
            S("Span 8 total", text="8 + 1 = 9 managers and 3 levels: 12 fewer managers to pay and a shorter chain of command."),
        ]),
        D("Removing one or more levels of management to create a flatter structure, usually to cut costs and speed up "
          "decisions.", title="Delayering"),
        H("Ways of grouping work"),
        KEY("Four common structures", "Choose by asking what the business most needs to coordinate.", cards=[
            ["Functional", "Departments by function: marketing, operations, finance, human resources. Specialist expertise, but departments may pursue their own goals."],
            ["Product", "Divisions by product line, each with its own functions. Focus on each product, but functions are duplicated."],
            ["Geographical", "Divisions by region (for example North, Centre, Littoral). Close to local customers, but duplication and weaker central control."],
            ["Matrix", "Project teams draw specialists from functional departments; each member reports to a project manager and a functional manager."],
        ]),
        T("A **matrix structure** suits projects that need several skills at once, such as building a new plant or launching a "
          "product. It encourages cooperation and flexible use of experts, but breaks unity of command: two bosses can give "
          "conflicting orders, and it can be costly to coordinate."),
        D("The network of relationships, friendships and communication channels (the 'grapevine') that exists alongside the "
          "formal structure. It can spread information quickly and support morale, but also spreads rumours and can resist "
          "change.", title="Informal organisation"),
        EX("Worked example 2: recommending a structure", intro="A Cameroonian engineering firm handles several large building "
           "projects at once, each needing architects, engineers and accountants. Recommend a structure.", steps=[
            S("Need", text="Each project needs a mix of specialists for a fixed period."),
            S("Option", text="A matrix structure: project managers lead teams drawn from the functional departments."),
            S("Benefit", text="Experts are shared across projects and each project has one person responsible."),
            S("Risk and remedy", text="Dual reporting can cause conflict; agree clearly which manager decides what."),
        ]),
        TIP("Exam link: Paper 1 often gives an organisation chart and asks about levels, spans or chains of command; Paper 2 "
            "and the case study ask you to recommend or evaluate a change of structure such as delayering."),
        MISTAKE("Confusing span of control with chain of command", "Span is width (how many report to one manager); chain is "
                "length (how many levels an instruction passes through)."),
        MISTAKE("Saying flat structures are always better", "Wide spans need capable, trusted staff and managers with time. In "
                "high-risk or routine work, closer supervision may be wiser."),
        QUIZ("A structure in which an engineer reports both to a project manager and to the head of engineering is",
             ["functional", "geographical", "matrix", "tall"], 2,
             "Dual reporting to a project and a function is the defining feature of a matrix structure.",
             feedback=["A functional structure has one line of reporting through the department.",
                       "A geographical structure groups by region.", "", "Tall describes the number of levels, not dual reporting."]),
        QUIZ("A firm removes a whole level of middle managers. Which result is most likely?",
             ["Longer chain of command", "Narrower spans of control", "Wider spans of control and faster communication",
              "More promotion opportunities"], 2,
             "Delayering shortens the hierarchy, so remaining managers supervise more people and messages pass through fewer levels.",
             feedback=["Removing a level shortens the chain.", "Spans widen when a level is removed.", "",
                       "Fewer management posts mean fewer promotion steps."]),
        PQ("A business has 120 operatives. Work out how many supervisors are needed with a span of control of 6, and how many with a span of 10.",
           "120 / 6 = 20 supervisors; 120 / 10 = 12 supervisors. The wider span needs 8 fewer supervisors."),
        PQ("Explain one advantage and one disadvantage of a geographical structure for a drinks company selling across Cameroon.",
           "Advantage: regional managers understand local tastes, distribution and languages, so they respond faster. "
           "Disadvantage: functions such as marketing and finance are duplicated in each region, raising costs."),
        PQ("Evaluate whether a growing bank should delayer.",
           "Plan: For: lower salary costs, faster decisions, more empowerment of branch staff, closer contact between senior "
           "managers and customers. Against: wider spans overload managers; banking needs control of risk and fraud; fewer "
           "promotion steps may raise labour turnover; the loss of experienced managers. Judgement: delayer only where staff are "
           "trained and systems provide control; keep closer supervision where risk is high."),
        SUM("Hierarchy, chain of command and span of control describe a structure; the organisation chart shows it.",
            "Tall: narrow spans, many levels, close control; flat: wide spans, few levels, faster communication.",
            "Managers needed = workers divided by the span at each level; wider spans need fewer managers.",
            "Structures group work by function, product, region or as a matrix of projects and functions.",
            "The informal organisation runs alongside the formal one and can help or hinder management."),
    ],
))


# ---------------------------------------------------------------------------
# M2 / Delegation, span of control and centralization
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M2, topic="Delegation, span of control and centralization",
    title="Delegation, the right span of control and centralisation",
    slug="bsl-delegation-span-centralisation",
    minutes=21,
    summary="What delegation, authority, responsibility and accountability mean, what decides the right span of control, and when a business should centralise or decentralise decisions.",
    objectives=[
        "Distinguish delegation, empowerment, authority, responsibility and accountability",
        "Explain the factors that determine an appropriate span of control",
        "Calculate the effect of a change in span or a removed layer on managers and costs",
        "Evaluate centralisation and decentralisation for a given business",
    ],
    key_concepts=["Delegation", "Empowerment", "Authority", "Responsibility", "Accountability",
                  "Centralisation", "Decentralisation"],
    blocks=[
        H("Introduction"),
        T("The owner of a supermarket chain in Yaounde used to approve every price change, every new supplier and every hire. "
          "With six branches, decisions now wait for days. Should she pass some decisions to branch managers? This lesson "
          "looks at delegation, spans of control and where decisions should be made."),
        D("Passing authority to make decisions or carry out tasks down the hierarchy to a subordinate.", title="Delegation"),
        KEY("Authority, responsibility and accountability", "These are often confused in answers.", cards=[
            ["Authority", "The right to make decisions and give instructions. It can be delegated."],
            ["Responsibility", "The duty to carry out a task. The manager remains ultimately responsible even after delegating."],
            ["Accountability", "Having to explain and justify results to a superior."],
        ]),
        D("Going further than delegation: giving employees the power and resources to decide **how** to do their work and to "
          "solve problems without asking permission.", title="Empowerment"),
        H("Benefits and risks of delegation"),
        KEY("Delegation", "A balanced view.", cards=[
            ["Benefits", "Frees senior managers for strategy; faster decisions by people close to the problem; motivates and develops staff (Herzberg's motivators, Maslow's esteem)."],
            ["Risks", "Poor decisions if staff lack skill or information; loss of control and consistency; managers may delegate only dull tasks; needs trust and training."],
        ]),
        H("What decides the right span of control?"),
        T("A wider span is possible when subordinates are skilled and trained, tasks are similar and routine, the manager is "
          "capable and has time, communication is good (for example, a shared information system), and staff are close "
          "together. A narrower span is needed when work is complex, varied or risky, staff are new, or they are spread across "
          "many sites."),
        EX("Worked example 1: managers needed and the saving from delayering", intro="A firm has 120 workers. Supervisors have a "
           "span of 8 and managers a span of 5 over the supervisors; one director heads the firm. Each manager costs FCFA "
           "450 000 a month (invented). The firm removes the manager layer and the supervisors report to the director.", steps=[
            S("Supervisors", math=r"120 \div 8 = 15"),
            S("Managers", math=r"15 \div 5 = 3"),
            S("Management posts before", math=r"15 + 3 + 1 = 19"),
            S("Annual saving from removing 3 managers", math=r"3 \times 450\,000 \times 12 = 16\,200\,000 \text{ FCFA}"),
            S("New span of the director", text="The director now has 15 direct reports, a very wide span. The firm saves "
              "money but must check that the director can cope."),
        ]),
        H("Centralisation and decentralisation"),
        D("**Centralisation**: most important decisions are taken by senior managers at the head office. **Decentralisation**: "
          "decision-making authority is passed to managers in branches, divisions or regions.", title="Centralisation and decentralisation"),
        KEY("Comparing the two", "The best choice depends on the business and its environment.", cards=[
            ["Centralisation", "Consistent policies and brand; tight control of costs and risk; economies of scale in buying; strong leadership in a crisis. But slow, distant from local needs, demotivating for branch managers."],
            ["Decentralisation", "Fast local decisions; uses local knowledge; motivates and trains future leaders; frees head office. But inconsistency, duplication, and risk of decisions that suit a branch but not the whole firm."],
        ]),
        EX("Worked example 2: model essay plan", intro="'A supermarket chain should decentralise decision-making to its branch managers.' Discuss.", steps=[
            S("Define", text="Centralisation and decentralisation; link to delegation."),
            S("For", text="Branches in Bamenda, Douala and Garoua serve customers with different tastes and incomes; branch managers know local suppliers; faster decisions on stock and prices; motivation."),
            S("Against", text="Central buying gives lower prices from suppliers; brand and price consistency; control of cash and fraud risk."),
            S("Judgement", text="Decentralise local decisions (staffing rotas, local products, promotions) and keep central control of buying, pricing policy and finance."),
        ]),
        TIP("Exam link: centralisation questions rarely have a pure answer. Examiners reward a judgement that decides which "
            "decisions to centralise and which to delegate, for the business in the question."),
        MISTAKE("Saying a manager 'delegates responsibility'", "Authority is delegated, but the manager stays ultimately responsible "
                "for the result. Write 'delegates authority'."),
        MISTAKE("Treating delegation and decentralisation as identical", "Delegation is passing a task or decision to one "
                "subordinate. Decentralisation is a structure in which authority is spread across the organisation."),
        QUIZ("A manager delegates the task of ordering stock to her assistant, who orders the wrong goods. Who is ultimately responsible to the owner?",
             ["Only the assistant", "The manager", "The supplier", "Nobody, since the task was delegated"], 1,
             "Authority was delegated, but the manager remains ultimately responsible and accountable to her superior.",
             feedback=["The assistant is accountable to the manager, but the manager still answers to the owner.", "",
                       "The supplier delivered what was ordered.", "Responsibility cannot be passed away completely."]),
        QUIZ("Which situation best suits a wide span of control?",
             ["New staff doing complex, varied work on many sites", "Skilled staff doing similar routine tasks in one place",
              "Dangerous work needing constant checking", "A manager with little time and poor communication systems"], 1,
             "Similar routine work by trained staff in one place needs little supervision.",
             feedback=["New staff, complexity and scattered sites need a narrow span.", "",
                       "Risky work needs close supervision.", "A busy manager with weak systems can supervise few people well."]),
        PQ("A firm has 180 workers and a span of control of 9 for supervisors, who report to managers with a span of 4. "
           "Calculate the number of supervisors and managers (round up where needed).",
           "Supervisors = 180 / 9 = 20. Managers = 20 / 4 = 5. Total management below the director = 25."),
        PQ("Explain the difference between delegation and empowerment.",
           "Delegation passes authority for a particular task or decision to a subordinate. Empowerment goes further: staff are "
           "given the power and resources to decide how to do their own work and solve problems without permission."),
        PQ("Evaluate the case for centralising decisions in a microfinance institution with branches in rural towns.",
           "Plan: For centralisation: control of lending risk and fraud, consistent loan rules, regulators' requirements. "
           "For decentralisation: branch staff know borrowers and local conditions, faster loan decisions, better service. "
           "Judgement: centralise lending rules and limits, but delegate small loan decisions within those limits to trained "
           "branch staff, with regular checks."),
        SUM("Delegation passes authority down; the manager remains responsible; staff are accountable for results.",
            "Empowerment gives staff power to decide how to work and solve problems.",
            "Spans can be wider with skilled staff, routine tasks, good communication and capable managers.",
            "Removing a layer cuts costs but widens spans, so check that managers can cope.",
            "Centralisation gives control and consistency; decentralisation gives speed, local knowledge and motivation."),
    ],
))


# ---------------------------------------------------------------------------
# M3 / Leadership
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M3, topic="Leadership",
    title="Leadership styles, McGregor's Theory X and Y and the Blake-Mouton grid",
    slug="bsl-leadership-styles-mcgregor-blake-mouton",
    minutes=22,
    summary="Autocratic, democratic, laissez-faire and paternalistic leadership, McGregor's Theory X and Theory Y, the Blake and Mouton managerial grid, and how to judge which style fits a situation.",
    objectives=[
        "Distinguish leadership from management and describe four leadership styles",
        "Explain McGregor's Theory X and Theory Y and link them to leadership styles",
        "Place leaders on the Blake and Mouton grid and interpret their positions",
        "Evaluate which leadership style suits a given situation",
    ],
    key_concepts=["Leadership", "Autocratic", "Democratic", "Laissez-faire", "Paternalistic",
                  "Theory X", "Theory Y", "Blake and Mouton grid", "Contingency approach"],
    blocks=[
        H("Introduction"),
        T("Two head teachers run similar schools. One decides everything and checks every teacher's register. The other holds "
          "meetings, asks teachers for ideas and lets them run their own clubs. Both may be effective, in different situations. "
          "This lesson gives you the language and models to analyse such differences in businesses."),
        D("The ability to influence and inspire people to work towards goals. **Management** is more about planning, organising "
          "and controlling resources. A good manager needs leadership, but the two are not the same.", title="Leadership"),
        KEY("Four leadership styles", "Each describes how much the leader shares decision-making.", cards=[
            ["Autocratic", "The leader decides alone and gives instructions; close supervision; one-way communication."],
            ["Democratic", "The leader consults or lets the group share decisions; two-way communication; delegation."],
            ["Laissez-faire", "The leader sets broad goals and leaves staff to decide almost everything."],
            ["Paternalistic", "The leader decides, but in what she believes is the workers' best interest, explaining decisions and caring for their welfare, like a parent."],
        ]),
        T("Tannenbaum and Schmidt described these styles as points on a **continuum**, from 'boss-centred' leadership (the leader "
          "tells) to 'subordinate-centred' leadership (the team decides within limits)."),
        H("McGregor's Theory X and Theory Y"),
        T("Douglas McGregor (*The Human Side of Enterprise*, 1960) argued that managers' assumptions about workers shape how they lead."),
        KEY("Two sets of assumptions", "Theories about managers' beliefs, not two types of worker.", cards=[
            ["Theory X", "Workers dislike work, avoid responsibility, need to be controlled and are motivated mainly by money and fear. Leads to autocratic, close supervision."],
            ["Theory Y", "Workers can enjoy work, seek responsibility, use creativity and are motivated by achievement. Leads to democratic leadership and delegation."],
        ]),
        T("McGregor suggested assumptions can become self-fulfilling: workers treated as Theory X may behave that way."),
        H("The Blake and Mouton managerial grid"),
        T("Robert Blake and Jane Mouton placed leaders on a 9 by 9 grid according to their **concern for production** (tasks, "
          "results) and **concern for people** (relationships, welfare)."),
        IMG("albsl-blake-mouton-grid.svg", alt="Grid with concern for production from 1 to 9 on the horizontal axis and concern "
            "for people from 1 to 9 on the vertical axis. Points: 1,1 impoverished; 9,1 produce or perish; 1,9 country club; "
            "5,5 middle of the road; 9,9 team.", caption="Figure 1. The Blake and Mouton managerial grid."),
        EX("Worked example 1: placing leaders on the grid", intro="Place each supervisor on the grid.", steps=[
            S("A sets high targets, ignores complaints, punishes mistakes", text="High task, low people: (9,1) produce or perish (authority-compliance)."),
            S("B keeps everyone happy but output keeps falling", text="Low task, high people: (1,9) country club."),
            S("C does the minimum to keep her job", text="(1,1) impoverished."),
            S("D sets clear goals with the team and supports them to meet them", text="(9,9) team management, the style Blake and Mouton recommended."),
        ]),
        H("Which style is best?"),
        T("The **contingency** (situational) view says no single style is always best. It depends on the leader (skills, "
          "personality), the followers (skill, experience, motivation), the task (routine or creative, urgent or not) and the "
          "situation (crisis, culture, time available)."),
        EX("Worked example 2: model essay plan", intro="'Democratic leadership is always the most effective style.' Discuss.", steps=[
            S("Define", text="Democratic leadership; contrast with autocratic and laissez-faire."),
            S("For", text="Uses staff ideas; motivates (Theory Y, Maslow's esteem needs); better decisions on complex problems; lower labour turnover."),
            S("Against", text="Slow in a crisis (fire, cash crisis); unsuitable for new, untrained staff; some decisions need confidentiality."),
            S("Judgement", text="Effective with skilled staff and when time allows; autocratic leadership may be better in emergencies; the best leaders adapt their style."),
        ]),
        MISTAKE("Treating Theory X and Y as types of worker", "They are assumptions held by managers about workers. Write 'a Theory "
                "X manager assumes...'."),
        MISTAKE("Calling laissez-faire 'no leadership'", "The leader still sets goals and provides resources; it can work well "
                "with expert, self-motivated teams such as researchers."),
        QUIZ("A manager who believes staff are lazy and must be watched closely holds",
             ["Theory Y assumptions", "Theory X assumptions", "a democratic style", "a laissez-faire style"], 1,
             "Belief that workers avoid work and need control is Theory X.",
             feedback=["Theory Y assumes workers seek responsibility.", "", "A democratic leader trusts and consults staff.",
                       "A laissez-faire leader gives staff freedom."]),
        QUIZ("On the Blake and Mouton grid, position (1,9) is",
             ["produce or perish", "country club", "team management", "impoverished"], 1,
             "1 for production, 9 for people: country club management.",
             feedback=["Produce or perish is (9,1).", "", "Team management is (9,9).", "Impoverished is (1,1)."]),
        PQ("Distinguish between autocratic and paternalistic leadership.",
           "Both leaders take decisions themselves. The autocrat simply instructs and controls; the paternalistic leader explains "
           "decisions and acts in what she sees as the workers' best interest, caring for their welfare."),
        PQ("Explain why an autocratic style might be appropriate on a construction site.",
           "Safety-critical tasks need clear, quick instructions that are followed exactly; many workers may be casual or new; "
           "delays are costly. Close control reduces accidents and errors."),
        PQ("Evaluate the usefulness of the Blake and Mouton grid to a manager of a hotel.",
           "Plan: Useful: shows the balance between guest service tasks and staff welfare; helps the manager see if she is "
           "'country club' or 'produce or perish'; training tool. Limits: based on attitudes, not results; 9,9 may not suit "
           "every situation (a crisis); placing a person on the grid is subjective. Judgement: a useful self-assessment tool, "
           "best combined with the contingency view."),
        SUM("Leadership styles: autocratic, democratic, laissez-faire and paternalistic, on a continuum of shared decision-making.",
            "McGregor: Theory X managers assume staff avoid work; Theory Y managers assume staff seek responsibility.",
            "Blake and Mouton: concern for production v concern for people; (9,9) team management is recommended.",
            "The contingency view: the best style depends on leader, followers, task and situation.",
            "Evaluate style by asking what this team, task and situation need."),
    ],
))


# ---------------------------------------------------------------------------
# M3 / Motivation theories
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M3, topic="Motivation theories",
    title="Motivation: Maslow, Herzberg, Vroom and Adams",
    slug="bsl-motivation-maslow-herzberg-vroom-adams",
    minutes=23,
    summary="Content theories (Maslow's hierarchy, Herzberg's two factors) and process theories (Vroom's expectancy, Adams' equity) of motivation, with calculations and their use in choosing financial and non-financial rewards.",
    objectives=[
        "Explain Maslow's hierarchy of needs and Herzberg's hygiene factors and motivators",
        "Calculate and interpret motivational force with Vroom's expectancy theory",
        "Use Adams' equity theory to compare output-input ratios",
        "Evaluate financial and non-financial methods of motivation using the theories",
    ],
    key_concepts=["Motivation", "Hierarchy of needs", "Hygiene factors", "Motivators", "Job enrichment",
                  "Expectancy", "Instrumentality", "Valence", "Equity theory"],
    blocks=[
        H("Introduction"),
        T("Two nurses in a Bamenda clinic earn the same salary. One stays late to help patients; the other watches the clock. "
          "Motivation explains the difference. Motivated staff work harder, make fewer mistakes and stay longer, which lowers "
          "recruitment costs. Business Studies uses four main theories, two about **what** motivates (content theories) and two "
          "about **how** people decide how much effort to give (process theories)."),
        D("The internal and external factors that stimulate people to work towards goals and to keep up their effort.", title="Motivation"),
        H("Maslow's hierarchy of needs"),
        IMG("albsl-maslow-hierarchy.svg", alt="Pyramid with five levels, from the base: physiological, safety, social, esteem, "
            "self-actualisation at the top. The lower levels are lower-order needs and the top two are higher-order needs.",
            caption="Figure 1. Maslow's hierarchy of needs."),
        T("Abraham Maslow argued that people satisfy needs in order, from **physiological** (food, shelter: met at work by a "
          "basic wage) to **safety** (job security, safe conditions), **social** (friendship, teamwork), **esteem** (recognition, "
          "status, promotion) and **self-actualisation** (reaching one's potential: challenging work). A satisfied need no longer "
          "motivates, so managers must find the next level for each worker."),
        H("Herzberg's two-factor theory"),
        KEY("Herzberg: hygiene factors and motivators", "From interviews with accountants and engineers in the late 1950s.", cards=[
            ["Hygiene (maintenance) factors", "Pay, working conditions, company policy, supervision, security. If poor they cause dissatisfaction; if good they only remove dissatisfaction."],
            ["Motivators", "Achievement, recognition, responsibility, the work itself, advancement. These create positive motivation."],
        ]),
        T("Herzberg's practical answer is **job enrichment**: giving a job more responsibility, a complete unit of work and "
          "chances to use skills. Compare **job enlargement** (more tasks at the same level) and **job rotation** (moving between tasks)."),
        H("Vroom's expectancy theory"),
        F(r"\text{Motivational force} = E \times I \times V", title="Vroom's expectancy theory"),
        T("**Expectancy** (E, 0 to 1): the belief that effort will lead to the required performance. **Instrumentality** "
          "(I, 0 to 1): the belief that performance will be rewarded. **Valence** (V): how much the person values the reward "
          "(here scored 0 to 1). If any one is zero, motivation is zero."),
        EX("Worked example 1: comparing two bonus schemes", intro="A salesperson scores scheme A: E = 0.8, I = 0.5, V = 0.9 and "
           "scheme B: E = 0.6, I = 0.9, V = 0.8. Which motivates her more?", steps=[
            S("Scheme A", math=r"0.8 \times 0.5 \times 0.9 = 0.36"),
            S("Scheme B", math=r"0.6 \times 0.9 \times 0.8 = 0.432"),
            S("Interpret", text="B gives the higher force. Although its target is harder, she is far more confident the bonus "
              "will actually be paid (I = 0.9), which outweighs the lower expectancy."),
        ]),
        H("Adams' equity theory"),
        T("J. Stacy Adams argued that workers compare the ratio of their **outputs** (pay, recognition, benefits) to their "
          "**inputs** (effort, time, skill) with the ratio of others. If they feel under-rewarded they may reduce effort, ask for "
          "more pay or leave."),
        EX("Worked example 2: an equity comparison", intro="Awa earns FCFA 180 000 a week for 40 hours. Ben earns FCFA 200 000 "
           "a week for 50 hours of the same work (invented figures). Compare their ratios.", steps=[
            S("Awa", math=r"\frac{180\,000}{40} = 4\,500 \text{ FCFA per hour}"),
            S("Ben", math=r"\frac{200\,000}{50} = 4\,000 \text{ FCFA per hour}"),
            S("Interpret", text="Ben's ratio is lower. He may feel under-rewarded even though his weekly pay is higher, and may "
              "cut his hours or effort to restore equity."),
        ]),
        KEY("Evaluating the theories", "Use these points in Paper 2 essays.", cards=[
            ["Maslow", "Simple and intuitive; but needs are not always met in order, and are hard to measure."],
            ["Herzberg", "Shows pay alone will not motivate; but based on professional staff, and pay can be a motivator where wages are low."],
            ["Vroom and Adams", "Explain individual differences and perceptions; but scores are subjective and hard for managers to use."],
        ]),
        MISTAKE("Saying 'Herzberg says money does not matter'", "Pay is a hygiene factor: poor pay causes dissatisfaction. Herzberg's "
                "point is that good pay alone does not create lasting motivation."),
        MISTAKE("Adding instead of multiplying in Vroom", "The terms are multiplied. A zero in any one gives zero motivation, which "
                "is why a bonus nobody believes will be paid motivates nobody."),
        QUIZ("Which is a motivator in Herzberg's theory?", ["Salary", "Working conditions", "Recognition for achievement", "Company policy"], 2,
             "Recognition is a motivator; the others are hygiene factors.",
             feedback=["Pay is a hygiene factor.", "Conditions are a hygiene factor.", "", "Policy is a hygiene factor."]),
        QUIZ("Using Vroom, E = 0.9, I = 0.0, V = 1.0. What is the motivational force?", ["1.9", "0.9", "0", "0.45"], 2,
             "0.9 x 0 x 1.0 = 0. If the worker does not believe the reward will follow, there is no motivation.",
             feedback=["The terms are multiplied, not added.", "This ignores the zero instrumentality.", "",
                       "This is not a product of the three values."]),
        PQ("A worker rates a promotion scheme: expectancy 0.7, instrumentality 0.6, valence 0.9. Calculate the motivational force.",
           "0.7 x 0.6 x 0.9 = 0.378."),
        PQ("Explain how a supermarket could use job enrichment to motivate checkout staff.",
           "Give experienced staff responsibility for a whole section: ordering stock, arranging displays and training new "
           "staff. This adds responsibility, achievement and recognition (Herzberg's motivators)."),
        PQ("'Money is the best motivator.' Discuss with reference to motivation theories.",
           "Plan: For: Taylor; Maslow's lower needs met by pay, important where wages are low; Vroom shows a valued, credible "
           "bonus motivates. Against: Herzberg treats pay as a hygiene factor; Maslow's higher needs need recognition and "
           "challenge; Adams shows fairness matters as much as the amount. Judgement: money is essential and motivates most "
           "when basic needs are not met, but lasting motivation needs non-financial rewards too."),
        SUM("Maslow: physiological, safety, social, esteem, self-actualisation; a satisfied need no longer motivates.",
            "Herzberg: hygiene factors prevent dissatisfaction; motivators (achievement, recognition, responsibility) motivate.",
            "Vroom: motivational force = expectancy x instrumentality x valence; any zero gives zero.",
            "Adams: workers compare output-input ratios with others; perceived unfairness reduces effort.",
            "Use the theories to judge rewards: pay matters, but recognition, responsibility and fairness also do."),
    ],
))


# ---------------------------------------------------------------------------
# M3 / Workforce planning, recruitment and selection
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M3, topic="Workforce planning, recruitment and selection",
    title="Workforce planning, labour turnover, recruitment and selection",
    slug="bsl-workforce-planning-recruitment-selection",
    minutes=22,
    summary="How a business plans the staff it needs, measures labour turnover, retention and absenteeism, and recruits and selects employees using job analysis, internal and external recruitment and selection methods.",
    objectives=[
        "Explain workforce planning and the factors that affect future staffing needs",
        "Calculate and interpret labour turnover, retention and absenteeism rates",
        "Describe the recruitment process from job analysis to job description and person specification",
        "Evaluate internal and external recruitment and different selection methods",
    ],
    key_concepts=["Workforce planning", "Labour turnover", "Retention rate", "Absenteeism", "Job analysis",
                  "Job description", "Person specification", "Internal recruitment", "External recruitment", "Selection"],
    blocks=[
        H("Introduction"),
        T("A hospital opening a new wing in Ngaoundere needs nurses, technicians and cleaners on the first day. If it hires too "
          "late, the wing stands empty; if it hires too many, it pays wages it cannot afford. **Human resource management** (HRM) "
          "plans, recruits, trains and keeps the right people. This lesson covers the first steps."),
        D("Assessing the number and skills of staff the business will need in future, comparing this with the current "
          "workforce, and planning how to close the gap (recruitment, training, redeployment or redundancy).", title="Workforce planning"),
        T("Future needs depend on forecast sales, new technology, planned expansion or closure, labour turnover and retirements, "
          "and changes in the law. Internal data (age profile, skills audit) and external data (labour market, wage rates, "
          "competitors) both feed the plan."),
        H("Measuring the workforce"),
        F(r"\text{Labour turnover} = \frac{\text{Number of staff leaving in the year}}{\text{Average number of staff}} \times 100", title="Labour turnover rate"),
        F(r"\text{Absenteeism} = \frac{\text{Working days lost through absence}}{\text{Total possible working days}} \times 100", title="Absenteeism rate"),
        F(r"\text{Retention rate} = \frac{\text{Staff employed for the whole year}}{\text{Staff at the start of the year}} \times 100", title="Retention rate"),
        T("Textbooks define retention in slightly different ways (for example, staff with more than one year's service); check "
          "your textbook and always show your formula."),
        EX("Worked example 1: workforce measures", intro="A firm (invented figures) had 140 staff on 1 January and 160 on 31 "
           "December; 18 left during the year. Of the 140 at the start, 126 stayed all year. In a separate department of 60 staff, "
           "360 days were lost through absence out of 240 working days each.", steps=[
            S("Average staff", math=r"\frac{140 + 160}{2} = 150"),
            S("Labour turnover", math=r"\frac{18}{150} \times 100 = 12\%"),
            S("Retention", math=r"\frac{126}{140} \times 100 = 90\%"),
            S("Absenteeism", math=r"\frac{360}{60 \times 240} \times 100 = \frac{360}{14\,400} \times 100 = 2.5\%"),
            S("Cost of turnover", text="If replacing each leaver costs FCFA 350 000 in advertising, interviews and training, the "
              "18 leavers cost 18 x 350 000 = FCFA 6 300 000."),
        ]),
        KEY("Interpreting labour turnover", "Neither a high nor a very low rate is automatically good or bad.", cards=[
            ["High turnover", "Recruitment and training costs, lost skills, low morale; may signal poor pay, management or conditions."],
            ["Some turnover", "Brings new ideas and lets a firm cut staff without redundancy; very low turnover can mean an ageing, static workforce."],
        ]),
        H("Recruitment"),
        T("**Job analysis** studies what a job involves. It produces a **job description** (title, duties, responsibilities, who "
          "the job holder reports to) and a **person specification** (qualifications, skills, experience and qualities of the "
          "ideal candidate, often split into essential and desirable)."),
        KEY("Internal v external recruitment", "Choose by asking what the vacancy needs.", cards=[
            ["Internal", "Cheaper and faster; candidate known; motivates staff through promotion. But no new ideas, creates another vacancy, may cause jealousy."],
            ["External", "Wider choice and new ideas and skills. But costly (adverts, agencies), slower, and the candidate is less well known. Sources include newspapers, websites, recruitment agencies, universities and the National Employment Fund (FNE) in Cameroon."],
        ]),
        H("Selection"),
        T("Selection methods include application forms and CVs, interviews, aptitude and skills tests (typing, driving, "
          "accounting), psychometric (personality) tests, assessment centres with group tasks, and references. Each method should "
          "test what the person specification requires. Selection must be fair: no discrimination on grounds unrelated to the job."),
        EX("Worked example 2: choosing a method", intro="A Douala logistics firm needs a warehouse supervisor. Recommend a recruitment and selection approach.", steps=[
            S("Recruitment", text="Advertise internally first: experienced warehouse staff know the systems and promotion motivates them."),
            S("If no strong internal candidate", text="Use an online job site to reach a wider pool."),
            S("Selection", text="Interview plus a practical test (planning a shift rota, checking a stock record) and references from previous employers."),
            S("Why", text="The tests measure the skills in the person specification better than an interview alone."),
        ]),
        MISTAKE("Using closing staff numbers for labour turnover", "Divide by the average number of staff over the period, not by the "
                "number at the start or the end."),
        MISTAKE("Mixing up job description and person specification", "The job description describes the job; the person "
                "specification describes the person wanted for it."),
        QUIZ("A firm starts the year with 80 staff and ends with 100; 9 leave during the year. What is labour turnover?",
             ["9%", "10%", "11.25%", "12%"], 1,
             "Average staff = (80 + 100) / 2 = 90; turnover = 9 / 90 x 100 = 10%.",
             feedback=["This divides by 100, the closing figure.", "", "This divides by 80, the opening figure.",
                       "This is not a result of the correct formula."]),
        QUIZ("Which document lists the qualifications and qualities required of the ideal candidate?",
             ["Job description", "Person specification", "Contract of employment", "Organisation chart"], 1,
             "The person specification describes the person; the job description describes the job.",
             feedback=["The job description lists duties and responsibilities.", "",
                       "The contract sets out terms after selection.", "The chart shows the structure."]),
        PQ("A factory loses 1 080 working days to absence in a year. It employs 90 staff, each with 240 working days. Calculate the absenteeism rate.",
           "Possible days = 90 x 240 = 21 600. Absenteeism = 1 080 / 21 600 x 100 = 5%."),
        PQ("Explain two possible causes of high labour turnover in a hotel.",
           "(1) Low pay compared with other hotels, so staff leave for better wages. (2) Poor management or long, irregular hours, "
           "lowering morale. Many hotel jobs are also seasonal or temporary."),
        PQ("Evaluate whether a bank should fill a branch manager vacancy internally or externally.",
           "Plan: Internal: knows systems and customers, cheaper, motivates staff, lower risk. External: new ideas, wider skills, "
           "useful if the branch is failing. Judgement: internal if a trained candidate exists and the branch performs well; "
           "external if new skills or change are needed. Use fair selection either way."),
        SUM("Workforce planning compares future staff needs with the current workforce and plans how to close the gap.",
            "Labour turnover = leavers / average staff x 100; absenteeism = days lost / possible days x 100.",
            "Job analysis gives a job description (the job) and a person specification (the person).",
            "Internal recruitment is cheap and motivating; external brings new skills and ideas.",
            "Selection methods (interviews, tests, assessment centres, references) should test the person specification fairly."),
    ],
))


# ---------------------------------------------------------------------------
# M3 / Training and appraisal
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M3, topic="Training and appraisal",
    title="Training, labour productivity and performance appraisal",
    slug="bsl-training-productivity-appraisal",
    minutes=21,
    summary="Induction, on-the-job and off-the-job training, how to judge whether training pays using labour productivity and payback, and the purposes and methods of performance appraisal.",
    objectives=[
        "Distinguish induction, on-the-job and off-the-job training",
        "Calculate labour productivity and the payback period of a training programme",
        "Explain the purposes and methods of performance appraisal, including 360-degree appraisal",
        "Evaluate training and appraisal for a given business",
    ],
    key_concepts=["Induction", "On-the-job training", "Off-the-job training", "Labour productivity",
                  "Performance appraisal", "360-degree appraisal", "Self-appraisal"],
    blocks=[
        H("Introduction"),
        T("A mobile money agent network in the North West trains new agents to spot fake notes and follow identity rules. "
          "Untrained agents lose money and break regulations. Training costs money now, but it can raise output, cut mistakes "
          "and keep staff. Appraisal then checks how well people perform and what they still need."),
        D("Planned activity that increases the knowledge and skills of employees to do their jobs better. **Development** is "
          "broader: preparing staff for future roles.", title="Training"),
        KEY("Types of training", "Most businesses use a mix.", cards=[
            ["Induction", "Introduces new staff to the business: people, rules, safety, culture. Helps them become productive quickly and reduces early leaving."],
            ["On-the-job", "Learning while working: shadowing, coaching, job rotation. Cheap and relevant, but may pass on bad habits and slows the trainer's own work."],
            ["Off-the-job", "Courses at a college or training centre or online. Experts and new ideas, no workplace pressure, but costly, time away from work, and trained staff may leave for better jobs."],
        ]),
        H("Does training pay?"),
        F(r"\text{Labour productivity} = \frac{\text{Output in a period}}{\text{Number of workers}}", title="Labour productivity"),
        EX("Worked example 1: productivity and payback", intro="A clothing workshop with 12 machinists (invented figures) produces "
           "4 800 garments a month. After a training course costing FCFA 3 000 000, output rises to 5 400 a month with the same "
           "staff. Each garment earns a contribution of FCFA 500.", steps=[
            S("Productivity before", math=r"\frac{4\,800}{12} = 400 \text{ garments per worker}"),
            S("Productivity after", math=r"\frac{5\,400}{12} = 450 \text{ garments per worker}"),
            S("Percentage rise", math=r"\frac{450 - 400}{400} \times 100 = 12.5\%"),
            S("Extra contribution per month", math=r"600 \times 500 = 300\,000 \text{ FCFA}"),
            S("Payback", math=r"\frac{3\,000\,000}{300\,000} = 10 \text{ months}", text="The course pays for itself in 10 months, if the gain lasts and trained staff stay."),
        ]),
        T("Contribution means selling price minus variable cost per unit; you will study it fully in the Upper Sixth."),
        H("Performance appraisal"),
        D("A regular, formal review of an employee's performance against agreed objectives, usually leading to new objectives "
          "and a training plan.", title="Performance appraisal"),
        KEY("Purposes of appraisal", "Link each purpose to the theory it uses.", cards=[
            ["Develop", "Identify training needs and career plans."],
            ["Motivate", "Recognition and feedback (Herzberg's motivators, Maslow's esteem); agreed objectives (Drucker's MBO)."],
            ["Reward and decide", "Evidence for pay rises, bonuses and promotion; records for workforce planning."],
        ]),
        KEY("Methods of appraisal", "Who gives the feedback?", cards=[
            ["Manager appraisal", "The line manager reviews the employee. Simple, but may reflect bias."],
            ["Self-appraisal", "The employee rates herself first. Encourages reflection, but may be too kind or too harsh."],
            ["Peer appraisal", "Colleagues give feedback. Useful in teams, but friendships and rivalries can distort it."],
            ["360-degree appraisal", "Feedback from managers, peers, subordinates and sometimes customers. Rounded, but time-consuming and can feel threatening."],
        ]),
        EX("Worked example 2: model essay plan", intro="'Performance appraisal is a waste of managers' time.' Discuss.", steps=[
            S("Define", text="Appraisal and its purposes."),
            S("Against the statement", text="Identifies training needs; links staff to corporate objectives (MBO); motivates through recognition; gives fair evidence for pay and promotion."),
            S("For the statement", text="Done badly, it is a box-ticking exercise; linking it to pay can make staff hide weaknesses; bias; time-consuming."),
            S("Judgement", text="Valuable when done regularly, fairly and followed by action (training, objectives); wasteful if it is a once-a-year formality."),
        ]),
        TIP("Exam link: calculations of productivity or the payback of training appear in Paper 1 and in case-study data; essays "
            "ask whether training or appraisal is worth its cost. Use the figures given in the case."),
        MISTAKE("Confusing productivity with production", "Production is total output; productivity is output per worker (or per "
                "hour). Output can rise while productivity falls if more workers are added."),
        MISTAKE("Assuming training always pays", "Benefits are uncertain and may be lost if trained staff leave. Say what must hold "
                "for the training to pay back."),
        QUIZ("A firm employs 25 workers producing 7 500 units a week. What is labour productivity?",
             ["250 units per worker", "300 units per worker", "7 500 units per worker", "187 500 units per worker"], 1,
             "7 500 / 25 = 300 units per worker per week.",
             feedback=["This divides by 30, not 25.", "", "This is total output.", "This multiplies instead of dividing."]),
        QUIZ("Feedback collected from a manager's boss, colleagues and the staff who report to her is",
             ["self-appraisal", "360-degree appraisal", "induction", "on-the-job training"], 1,
             "Feedback from all around the employee is 360-degree appraisal.",
             feedback=["Self-appraisal is the employee's own view.", "", "Induction introduces new staff.", "This is a training method."]),
        PQ("Training costing FCFA 4 800 000 raises output by 400 units a month, each with a contribution of FCFA 1 500. Calculate the payback period.",
           "Extra contribution = 400 x 1 500 = FCFA 600 000 a month. Payback = 4 800 000 / 600 000 = 8 months."),
        PQ("Explain one advantage and one disadvantage of off-the-job training for a bank.",
           "Advantage: experts teach new regulations and systems without the pressure of customers. Disadvantage: staff are away "
           "from branches, which costs output, and newly qualified staff may be recruited by rival banks."),
        PQ("Evaluate the use of 360-degree appraisal in a small family business.",
           "Plan: For: rounded view, managers learn how staff see them, builds openness. Against: time and cost for a small firm; "
           "family relationships make honest feedback hard; staff may fear consequences. Judgement: a simpler manager-plus-self "
           "appraisal may suit a small family firm better, with 360-degree feedback introduced as it grows."),
        SUM("Induction settles new staff; on-the-job is cheap and relevant; off-the-job brings expert knowledge at higher cost.",
            "Labour productivity = output / number of workers; it is not the same as total production.",
            "Training payback = cost / extra contribution per period.",
            "Appraisal reviews performance against objectives to develop, motivate and reward staff.",
            "Methods: manager, self, peer and 360-degree appraisal, each with costs and risks of bias."),
    ],
))


# ---------------------------------------------------------------------------
# M3 / Industrial relations
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M3, topic="Industrial relations",
    title="Industrial relations: trade unions, collective bargaining and disputes",
    slug="bsl-industrial-relations-unions-disputes",
    minutes=21,
    summary="The role of trade unions and employers' organisations, collective bargaining, the forms and costs of industrial action, and how conciliation and arbitration settle disputes, with costing of wage claims.",
    objectives=[
        "Explain the functions of trade unions and employers' organisations",
        "Describe collective bargaining and the forms of industrial action",
        "Calculate the cost of a wage claim and of a strike to a business",
        "Evaluate ways of resolving industrial disputes, including conciliation and arbitration",
    ],
    key_concepts=["Industrial relations", "Trade union", "Collective bargaining", "Industrial action",
                  "Conciliation", "Arbitration", "Employers' organisation", "Worker participation"],
    blocks=[
        H("Introduction"),
        T("Workers at a plantation ask for a pay rise after prices of food and transport go up. Managers say the company cannot "
          "afford it. If talks fail, the workers might refuse overtime or stop work, and the harvest could rot. **Industrial "
          "relations** is the relationship between employers and employees, and the ways they settle disagreements."),
        D("An organisation of workers formed to protect and improve the pay, conditions and job security of its members by "
          "acting together.", title="Trade union"),
        KEY("Functions of trade unions", "What unions do for members.", cards=[
            ["Negotiate", "Bargain over pay, hours, conditions and redundancy terms."],
            ["Protect", "Represent members in disciplinary and grievance cases; press for health and safety."],
            ["Inform and influence", "Advise members; lobby government on labour laws and the minimum wage."],
        ]),
        T("Employers also organise. In Cameroon the best-known employers' organisation is GICAM (Groupement Inter-patronal du "
          "Cameroun), which represents businesses in discussions with government and unions. In Cameroon, workers' rights and "
          "the procedure for collective disputes are set out mainly in the Labour Code of 1992; check the current procedure "
          "with your teacher."),
        H("Collective bargaining"),
        D("Negotiation between employers (or their organisation) and trade unions representing many workers, to agree pay and "
          "conditions for the whole group. The result is often written into a **collective agreement**.", title="Collective bargaining"),
        T("Bargaining strength depends on the union's membership and unity, how easily workers can be replaced, the state of "
          "the labour market, the firm's profits and order book, and public opinion. Each side has a target and a resistance "
          "point; a deal is possible where these overlap."),
        EX("Worked example 1: costing a wage claim", intro="A union representing 200 workers with an average monthly wage of "
           "FCFA 150 000 (invented figures) claims a 5% rise. The employer offers 3%. Find the annual cost of each.", steps=[
            S("Monthly cost of 5%", math=r"200 \times 150\,000 \times 0.05 = 1\,500\,000 \text{ FCFA}"),
            S("Annual cost of 5%", math=r"1\,500\,000 \times 12 = 18\,000\,000 \text{ FCFA}"),
            S("Annual cost of 3%", math=r"200 \times 150\,000 \times 0.03 \times 12 = 10\,800\,000 \text{ FCFA}"),
            S("Gap", math=r"18\,000\,000 - 10\,800\,000 = 7\,200\,000 \text{ FCFA a year}"),
        ]),
        H("Industrial action"),
        KEY("Forms of industrial action", "Action short of a strike puts pressure on the employer while workers keep most of their pay.", cards=[
            ["Overtime ban", "Workers refuse to work beyond normal hours."],
            ["Work-to-rule", "Workers follow every rule exactly, slowing work."],
            ["Go-slow", "Workers deliberately work slowly."],
            ["Strike", "Workers stop work completely; they usually lose pay and the employer loses output."],
        ]),
        EX("Worked example 2: the cost of a strike", intro="A strike stops a factory for 4 days. It normally earns a contribution "
           "of FCFA 2 500 000 a day (invented). Compare the cost with the wage gap in Worked example 1.", steps=[
            S("Lost contribution", math=r"4 \times 2\,500\,000 = 10\,000\,000 \text{ FCFA}"),
            S("Compare", text="The strike costs more than the FCFA 7.2 million a year gap between claim and offer, before counting "
              "lost customers and reputation. This strengthens the case for a compromise."),
        ]),
        H("Resolving disputes"),
        KEY("Third-party help", "Used when direct talks fail.", cards=[
            ["Conciliation", "A neutral third party (in Cameroon often a labour inspector) helps the two sides talk and find their own agreement."],
            ["Mediation", "The third party also proposes a solution, which the sides may accept or reject."],
            ["Arbitration", "An arbitrator hears both sides and makes a decision, which may be binding. Pendulum arbitration chooses one side's final offer, which pushes both towards reasonable positions."],
        ]),
        T("Good industrial relations also depend on **worker participation**: works councils, staff representatives, consultation "
          "before change and clear grievance procedures. These prevent many disputes from starting."),
        MISTAKE("Thinking a strike only harms the employer", "Workers lose pay, customers lose supply and both sides may lose future "
                "business. Show the costs to each side."),
        MISTAKE("Confusing conciliation with arbitration", "In conciliation the parties reach their own agreement; in arbitration a "
                "third party decides."),
        QUIZ("Workers do exactly what their contracts and rules require and nothing more, slowing production. This is",
             ["a strike", "an overtime ban", "a work-to-rule", "arbitration"], 2,
             "Following rules to the letter is a work-to-rule.",
             feedback=["In a strike workers stop work completely.", "An overtime ban refuses extra hours only.", "",
                       "Arbitration is a way of settling a dispute."]),
        QUIZ("In pendulum arbitration the arbitrator",
             ["splits the difference between the two offers", "chooses either the union's or the employer's final offer",
              "only helps the two sides to talk", "always sides with the employer"], 1,
             "The arbitrator must pick one side's final position, so each side makes a reasonable offer.",
             feedback=["Splitting the difference is what pendulum arbitration avoids.", "", "That is conciliation.",
                       "The arbitrator is neutral."]),
        PQ("150 workers earn an average of FCFA 120 000 a month. Calculate the annual cost of a 4% pay rise.",
           "150 x 120 000 x 0.04 = FCFA 720 000 a month; x 12 = FCFA 8 640 000 a year."),
        PQ("Explain two factors that strengthen a trade union's bargaining position.",
           "(1) High membership and unity, so action would stop most of the work. (2) Workers' skills are scarce and hard to "
           "replace, and the firm has full order books, so a strike would be very costly."),
        PQ("Evaluate whether a business should accept a union's wage claim to avoid a strike.",
           "Plan: Accept: avoids lost output and customers, protects morale and reputation; compare the strike cost with the wage "
           "cost. Reject: the cost is permanent and may weaken competitiveness; it may encourage further claims. Alternatives: "
           "partial offer linked to productivity, conciliation or arbitration. Judgement: depends on the size of each cost, the "
           "firm's profits and the long-term relationship; a negotiated compromise is usually best."),
        SUM("Trade unions negotiate, protect and inform members; employers' organisations such as GICAM represent firms.",
            "Collective bargaining sets pay and conditions for groups of workers; strength depends on unity, skills and the market.",
            "Industrial action: overtime ban, work-to-rule, go-slow, strike; each has costs for both sides.",
            "Cost a wage claim as workers x wage x % rise x 12; compare with the cost of lost output.",
            "Disputes are resolved by conciliation, mediation or arbitration; participation prevents many disputes."),
    ],
))


# ---------------------------------------------------------------------------
# M4 / Marketing and market orientation
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M4, topic="Marketing and market orientation",
    title="Marketing, market orientation and market measures",
    slug="bsl-marketing-market-orientation",
    minutes=21,
    summary="What marketing is, the difference between market orientation, product orientation and asset-led marketing, societal marketing, and how to calculate market size, market growth and market share.",
    objectives=[
        "Define marketing and explain its role in achieving business objectives",
        "Compare market orientation, product orientation and asset-led marketing",
        "Calculate market size, market growth and market share and interpret changes",
        "Evaluate market orientation for a given business",
    ],
    key_concepts=["Marketing", "Market orientation", "Product orientation", "Asset-led marketing",
                  "Societal marketing", "Market size", "Market growth", "Market share"],
    blocks=[
        H("Introduction"),
        T("A juice company in Bafoussam made a mango drink it was proud of, but sales were weak. When it asked customers, it "
          "learned they wanted smaller, cheaper bottles they could buy every day. It changed the pack and sales rose. The "
          "lesson: successful marketing starts with the customer."),
        D("The management process of identifying, anticipating and satisfying customer requirements profitably.", title="Marketing"),
        KEY("Three orientations", "Where does the business start its thinking?", cards=[
            ["Market orientation", "Starts with customers: research their needs, then design the product and mix. Lower risk of failure, but research is costly and customers cannot always imagine new technologies."],
            ["Product orientation", "Starts with the product or technology: make the best product and then sell it. Suits new technologies and products where quality is the main selling point, but risks making goods nobody wants."],
            ["Asset-led marketing", "Combines both: meets customer needs using the firm's existing strengths (brand, skills, distribution)."],
        ]),
        D("Marketing that balances customers' wants, the firm's profit and the long-term welfare of society, for example "
          "avoiding harmful products or wasteful packaging.", title="Societal marketing"),
        H("Measuring the market"),
        F(r"\text{Market share} = \frac{\text{Firm's sales}}{\text{Total market sales}} \times 100", title="Market share"),
        F(r"\text{Market growth} = \frac{\text{Change in market size}}{\text{Original market size}} \times 100", title="Market growth"),
        T("**Market size** can be measured by volume (units sold) or value (sales revenue). Always say which you use."),
        EX("Worked example 1: growth and share", intro="A firm sold FCFA 120 million in a market worth FCFA 800 million last year. "
           "This year the market is FCFA 880 million and the firm's sales are FCFA 126 million (invented figures).", steps=[
            S("Market growth", math=r"\frac{880 - 800}{800} \times 100 = 10\%"),
            S("Firm's sales growth", math=r"\frac{126 - 120}{120} \times 100 = 5\%"),
            S("Share last year", math=r"\frac{120}{800} \times 100 = 15\%"),
            S("Share this year", math=r"\frac{126}{880} \times 100 \approx 14.32\%"),
            S("Interpret", text="The firm's sales rose, but more slowly than the market, so it lost market share to rivals."),
        ]),
        EX("Worked example 2: model essay plan", intro="'All businesses should be market orientated.' Discuss.", steps=[
            S("Define", text="Market and product orientation."),
            S("For", text="Products match needs, so fewer failures; competitive markets such as mobile phones and drinks need it; customer loyalty."),
            S("Against", text="Research is costly for small firms; customers may not imagine radical innovations; firms with strong technical skills or quality (a pharmaceutical maker) may lead with the product; asset-led marketing combines both."),
            S("Judgement", text="Most firms in competitive consumer markets need a strong market orientation, but the best approach uses the firm's assets too."),
        ]),
        TIP("Exam link: market share and growth calculations are common in Paper 1 and in case studies. Always interpret: a rising "
            "share means the firm is growing faster than the market."),
        MISTAKE("Thinking rising sales mean rising market share", "If the market grows faster than the firm's sales, its share falls. "
                "Always compare the two growth rates."),
        MISTAKE("Defining marketing as advertising", "Advertising is one part of promotion, which is one part of the marketing mix. "
                "Marketing begins with identifying customer needs."),
        QUIZ("A firm's sales rise by 8% while the market grows by 12%. What happens to its market share?",
             ["It rises", "It falls", "It stays the same", "It cannot change if sales rise"], 1,
             "The firm grows more slowly than the market, so its share falls.",
             feedback=["Share rises only if the firm grows faster than the market.", "",
                       "Share is constant only if both grow at the same rate.", "Share depends on relative growth."]),
        QUIZ("A firm uses its well-known brand and nationwide distribution to launch a product that research shows customers want. This is",
             ["product orientation", "asset-led marketing", "societal marketing", "mass production"], 1,
             "It combines customer needs with the firm's existing assets.",
             feedback=["Product orientation ignores customer research.", "", "Societal marketing focuses on society's welfare.",
                       "Mass production is an operations method."]),
        PQ("A market grows from FCFA 500 million to FCFA 575 million. A firm's sales rise from FCFA 100 million to FCFA 120 million. "
           "Calculate the market growth and the firm's market share in each year.",
           "Market growth = 75 / 500 x 100 = 15%. Share before = 100 / 500 x 100 = 20%; after = 120 / 575 x 100 = 20.87% (2 d.p.). "
           "The firm grew faster (20%) than the market, so its share rose."),
        PQ("Explain why a pharmaceutical company may be more product orientated than a fashion retailer.",
           "Its success depends on research and the effectiveness of the product, which customers cannot design; regulations "
           "require quality. A fashion retailer must follow changing customer tastes closely, so it needs market orientation."),
        PQ("Evaluate whether a small bakery should spend money on becoming more market orientated.",
           "Plan: For: knowing which breads and times customers want raises sales and cuts waste; simple research is cheap "
           "(talking to customers, tracking sales). Against: limited money; costly formal research may not pay. Judgement: yes, "
           "through low-cost methods suited to its size."),
        SUM("Marketing identifies, anticipates and satisfies customer needs profitably.",
            "Market orientation starts with customers; product orientation with the product; asset-led marketing combines both.",
            "Societal marketing also considers society's long-term welfare.",
            "Market share = firm's sales / market sales x 100; market growth = change / original x 100.",
            "A firm gains share only if its sales grow faster than the market."),
    ],
))


# ---------------------------------------------------------------------------
# M4 / Market research and sampling
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M4, topic="Market research and sampling",
    title="Primary and secondary research and sampling methods",
    slug="bsl-market-research-sampling",
    minutes=22,
    summary="Primary and secondary research, qualitative and quantitative data, the main sampling methods (random, systematic, stratified, quota, cluster, convenience), how to calculate sample shares, and sources of bias.",
    objectives=[
        "Compare primary and secondary research and qualitative and quantitative data",
        "Describe the main sampling methods and calculate stratified and systematic samples",
        "Explain sources of bias and the effect of sample size on reliability",
        "Evaluate a research plan for a given business",
    ],
    key_concepts=["Primary research", "Secondary research", "Qualitative data", "Quantitative data",
                  "Random sampling", "Systematic sampling", "Stratified sampling", "Quota sampling", "Sampling bias"],
    blocks=[
        H("Introduction"),
        T("Before opening a cyber cafe and printing shop near a university in Buea, an entrepreneur wants to know how many "
          "students print documents each week and how much they pay. She cannot ask all of them, so she must choose some. How "
          "she chooses them decides whether her results can be trusted."),
        D("The collection and analysis of information about customers, competitors and markets to reduce the risk of marketing decisions.", title="Market research"),
        KEY("Primary v secondary research", "Most businesses use secondary research first because it is cheaper.", cards=[
            ["Primary (field)", "New data collected for the firm's own purpose: questionnaires, interviews, focus groups, observation, test marketing. Specific and up to date, but costly and slow."],
            ["Secondary (desk)", "Data already collected by others: government statistics, trade reports, newspapers, the internet, the firm's own sales records. Cheap and quick, but may be out of date or not fit the exact question."],
        ]),
        T("**Quantitative** data is numerical (how many, how often, what price) and can be analysed statistically. **Qualitative** "
          "data is about opinions, feelings and reasons (why customers buy), often from focus groups or in-depth interviews. "
          "Good research usually uses both."),
        H("Sampling methods"),
        D("The group of people selected from the whole **population** (all the people of interest) to take part in research.", title="Sample"),
        KEY("Probability sampling", "Every member has a known chance of selection.", cards=[
            ["Random", "Every member of the population has an equal chance of selection (for example, numbers drawn from a full list). Needs a complete list."],
            ["Systematic", "Every nth item from a list, after a random start. Simple, but a pattern in the list can bias it."],
            ["Stratified", "The population is divided into groups (strata) and each is sampled in proportion to its size. Representative, but needs data on the strata."],
        ]),
        KEY("Non-probability sampling", "Quicker and cheaper, but less representative.", cards=[
            ["Quota", "Interviewers must find set numbers of people with given characteristics (for example 30 women aged 18 to 25), choosing whom they ask."],
            ["Cluster", "One or a few areas (clusters) are chosen and people within them are surveyed. Cheap where the population is spread out, but the area may be untypical."],
            ["Convenience", "Whoever is easiest to reach. Cheap but often biased."],
        ]),
        EX("Worked example 1: a stratified sample", intro="A supermarket has 2 000 loyalty-card customers: 1 200 women and 800 men. "
           "It wants a stratified sample of 150.", steps=[
            S("Women", math=r"\frac{1\,200}{2\,000} \times 150 = 90"),
            S("Men", math=r"\frac{800}{2\,000} \times 150 = 60"),
            S("Check", math=r"90 + 60 = 150"),
        ]),
        EX("Worked example 2: a systematic sample", intro="The same list of 2 000 customers is used for a systematic sample of 100.", steps=[
            S("Sampling interval", math=r"\frac{2\,000}{100} = 20"),
            S("Method", text="Pick a random start from 1 to 20 (say 7), then take customers 7, 27, 47, ... to the end of the list."),
        ]),
        H("Bias and reliability"),
        T("**Sampling bias** occurs when the sample does not represent the population: interviewing only in one market, asking "
          "leading questions, or relying on people who choose to reply. Larger samples usually give more reliable results but "
          "cost more. The trade-off between cost and confidence must be judged against the risk of the decision."),
        EX("Worked example 3: judging a research plan", intro="The Buea entrepreneur plans to ask 20 friends whether they would use her printing shop. Evaluate the plan.", steps=[
            S("Problem 1", text="Convenience sample of friends: likely to be biased and too polite."),
            S("Problem 2", text="20 is too small to be reliable for an investment decision."),
            S("Improvement", text="A quota sample of about 150 students across faculties and years, with a short questionnaire on printing frequency and prices paid, plus observation of queues at existing shops."),
        ]),
        MISTAKE("Calling any 'random-looking' sample random", "Standing at a market and stopping whoever passes is convenience "
                "sampling. Random sampling needs a full list in which each member has an equal chance."),
        MISTAKE("Mixing up quota and stratified sampling", "Both use groups, but in stratified sampling people are selected randomly "
                "within each group; in quota sampling the interviewer chooses whom to ask."),
        QUIZ("A firm has 3 000 customers: 1 800 in Douala and 1 200 in Yaounde. In a stratified sample of 250, how many should be from Yaounde?",
             ["100", "125", "150", "120"], 0,
             "1 200 / 3 000 x 250 = 100.",
             feedback=["", "This splits the sample equally, ignoring the strata sizes.", "This is the Douala figure.",
                       "This is 1 200 divided by 10, not Yaounde's share of the sample of 250."]),
        QUIZ("Interviewers must each find 20 men and 20 women aged over 30 and choose whom to stop. This is",
             ["random sampling", "quota sampling", "systematic sampling", "stratified random sampling"], 1,
             "Set numbers per group, with the interviewer choosing whom to ask: quota sampling.",
             feedback=["Random sampling gives every member an equal chance from a list.", "",
                       "Systematic sampling takes every nth name.", "In stratified random sampling people are drawn randomly within groups."]),
        PQ("A list of 4 500 households is to be sampled systematically for 150 interviews. Calculate the sampling interval and describe the method.",
           "Interval = 4 500 / 150 = 30. Choose a random start from 1 to 30 and then every 30th household on the list."),
        PQ("Explain one advantage and one disadvantage of secondary research for a firm planning to export cocoa products.",
           "Advantage: trade statistics and reports on export markets are cheap and quick to obtain. Disadvantage: they may be out "
           "of date or not cover the firm's exact product or target customers."),
        PQ("Evaluate whether a small firm should spend a large amount on primary research before launching a new product.",
           "Plan: For: reduces the risk of failure; gives specific, up-to-date data on its target customers. Against: cost and "
           "time; small firms may use cheaper secondary data, observation or a small test launch. Judgement: spend in proportion "
           "to the risk of the decision; for a small launch, low-cost primary research plus secondary data is usually enough."),
        SUM("Primary research is new, specific and costly; secondary research is existing, cheap and may be out of date.",
            "Quantitative data is numerical; qualitative data explains opinions and reasons.",
            "Random, systematic and stratified samples are probability methods; quota, cluster and convenience are not.",
            "Stratified share = stratum size / population x sample size; systematic interval = population / sample size.",
            "Bias and small samples reduce reliability; balance research cost against the risk of the decision."),
    ],
))


# ---------------------------------------------------------------------------
# M4 / Demand forecasting
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M4, topic="Demand forecasting",
    title="Forecasting sales with moving averages, trends and seasonal variation",
    slug="bsl-demand-forecasting-moving-averages",
    minutes=24,
    summary="Why businesses forecast demand, how to calculate three-point and four-quarter centred moving averages, find the trend and seasonal variations, extrapolate a forecast, and judge its reliability alongside qualitative methods.",
    objectives=[
        "Explain why businesses forecast sales and the factors that make forecasting difficult",
        "Calculate three-point and four-quarter centred moving averages",
        "Calculate seasonal variations and use the trend to forecast future sales",
        "Evaluate quantitative and qualitative forecasting methods",
    ],
    key_concepts=["Sales forecast", "Time series", "Moving average", "Centred moving average", "Trend",
                  "Seasonal variation", "Extrapolation", "Delphi method"],
    blocks=[
        H("Introduction"),
        T("A school-uniform tailor in Bamenda sells far more in August and September, when the school year starts, than in "
          "March. A soft-drinks seller sells more in the hot dry season. To buy fabric, hire staff and plan cash, these businesses "
          "need forecasts. A **time series** of past sales can reveal the long-term trend and the regular seasonal pattern."),
        D("A list of values recorded at regular intervals (monthly, quarterly). It can be split into the **trend** (long-term "
          "direction), **seasonal variation** (regular pattern within each year), **cyclical variation** (the business cycle) "
          "and **random variation** (one-off events).", title="Time series"),
        H("Three-point moving averages"),
        D("The average of a fixed number of consecutive values, recalculated as the period moves forward one step. It smooths "
          "out short-term fluctuations to show the trend.", title="Moving average"),
        EX("Worked example 1: three-point moving average", intro="Monthly sales (units, invented): 30, 36, 33, 39, 42, 45. "
           "Calculate the three-point moving averages.", steps=[
            S("First average (months 1 to 3), placed at month 2", math=r"\frac{30 + 36 + 33}{3} = 33"),
            S("Months 2 to 4, at month 3", math=r"\frac{36 + 33 + 39}{3} = 36"),
            S("Months 3 to 5, at month 4", math=r"\frac{33 + 39 + 42}{3} = 38"),
            S("Months 4 to 6, at month 5", math=r"\frac{39 + 42 + 45}{3} = 42"),
            S("Interpret", text="The averages 33, 36, 38, 42 show a rising trend once the ups and downs are smoothed."),
        ]),
        H("Four-quarter centred moving averages"),
        T("With quarterly data, a four-quarter average falls between two quarters (for example between Q2 and Q3). To place it "
          "against an actual quarter we **centre** it: add two neighbouring four-quarter totals and divide by 8."),
        CODE("""
Year  Quarter  Sales  4-quarter total  8-quarter total  Trend (/8)  Seasonal variation
2024  Q1        40
2024  Q2        60
                          232
2024  Q3        52                     472              59          52 - 59 = -7
                          240
2024  Q4        80                     488              61          80 - 61 = +19
                          248
2025  Q1        48                     504              63          48 - 63 = -15
                          256
2025  Q2        68                     520              65          68 - 65 = +3
                          264
2025  Q3        60
2025  Q4        88
""", "text", title="Table 1. Quarterly sales of a uniform tailor (thousand FCFA, invented figures)"),
        EX("Worked example 2: building Table 1", intro="Show how the first trend value and seasonal variation are found.", steps=[
            S("First 4-quarter total (Q1 to Q4 2024)", math=r"40 + 60 + 52 + 80 = 232"),
            S("Next total (Q2 2024 to Q1 2025)", math=r"60 + 52 + 80 + 48 = 240"),
            S("Centred total", math=r"232 + 240 = 472"),
            S("Trend for Q3 2024", math=r"\frac{472}{8} = 59"),
            S("Seasonal variation", math=r"\text{Actual} - \text{Trend} = 52 - 59 = -7"),
        ]),
        EX("Worked example 3: forecasting", intro="Use Table 1 to forecast sales for Q1 2026.", steps=[
            S("Trend increase per quarter", math=r"\frac{65 - 59}{3} = 2"),
            S("Quarters from Q2 2025 to Q1 2026", text="Q3 2025, Q4 2025, Q1 2026: 3 quarters ahead."),
            S("Forecast trend", math=r"65 + 3 \times 2 = 71"),
            S("Add the Q1 seasonal variation", math=r"71 + (-15) = 56", text="Forecast: about 56 thousand FCFA. With more years of data you would average the variations for each quarter."),
        ]),
        D("Extending the trend line into the future on the assumption that past patterns will continue.", title="Extrapolation"),
        H("How reliable is a forecast?"),
        T("Quantitative forecasts assume the past is a guide to the future. They become unreliable when tastes change, a new rival "
          "enters, prices or incomes change, or events such as floods or border closures occur. The further ahead the forecast, "
          "the less reliable it is. **Qualitative methods** help: the **Delphi method** (a panel of experts answers in rounds, "
          "anonymously, until views converge), sales-force opinion and executive judgement."),
        TIP("Exam link: moving-average calculations appear in Paper 1 and case studies; a Paper 2 question may ask how far a "
            "firm can rely on forecasts. Always show the 4-quarter totals, centring and seasonal variations."),
        MISTAKE("Dividing a four-quarter total by 8 without centring", "Divide one 4-quarter total by 4 for a simple average, or the "
                "sum of two neighbouring totals by 8 for a centred value. Do not mix the two."),
        MISTAKE("Getting the sign of the seasonal variation wrong", "Seasonal variation = actual - trend. A quarter below the trend "
                "has a negative variation."),
        QUIZ("Sales for four months are 20, 26, 23, 29. What is the second three-point moving average?",
             ["23", "26", "24.5", "78"], 1,
             "(26 + 23 + 29) / 3 = 78 / 3 = 26.",
             feedback=["This is the first average (20 + 26 + 23) / 3.", "", "This is an average of four values.",
                       "This is the total, not divided by 3."]),
        QUIZ("Actual sales in a quarter are 120 and the trend value is 132. The seasonal variation is",
             ["+12", "-12", "252", "0.91"], 1,
             "Actual - trend = 120 - 132 = -12.",
             feedback=["The quarter is below the trend, so the variation is negative.", "", "This adds the two values.",
                       "This is a ratio, not the additive seasonal variation."]),
        PQ("Quarterly sales are Q1 30, Q2 50, Q3 40, Q4 60 and next Q1 34. Calculate the centred moving average for Q3 and its seasonal variation.",
           "Totals: 30 + 50 + 40 + 60 = 180; 50 + 40 + 60 + 34 = 184. Centred = (180 + 184) / 8 = 45.5. Seasonal variation = 40 - 45.5 = -5.5."),
        PQ("The trend is 70 in Q4 of one year and rises by 1.5 a quarter. The average seasonal variation for Q2 is +6. Forecast sales for Q2 of the next year.",
           "Q2 next year is 2 quarters after Q4. Trend = 70 + 2 x 1.5 = 73. Forecast = 73 + 6 = 79."),
        PQ("Evaluate the usefulness of moving averages for a firm launching a completely new product.",
           "Plan: Useful: once some sales data exist, they show the trend and seasonality. Limits: a new product has no past data; "
           "early sales follow the product life cycle, not a steady trend; competitors and marketing change demand. Alternatives: "
           "market research, test marketing, Delphi or comparisons with similar products. Judgement: of limited use at launch; "
           "more useful once a few years of data exist."),
        SUM("A time series contains a trend, seasonal, cyclical and random variations.",
            "Three-point moving average: average of three consecutive values, placed at the middle one.",
            "Centred four-quarter average = (two neighbouring 4-quarter totals) / 8.",
            "Seasonal variation = actual - trend; forecast = extrapolated trend + seasonal variation.",
            "Forecasts are less reliable further ahead and when conditions change; qualitative methods such as Delphi help."),
    ],
))


# ---------------------------------------------------------------------------
# M4 / Segmentation, targeting and positioning
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M4, topic="Segmentation, targeting and positioning",
    title="Segmentation, targeting, positioning and the positioning map",
    slug="bsl-segmentation-targeting-positioning",
    minutes=21,
    summary="How businesses divide a market into segments, choose target segments (mass, niche, differentiated), value a segment, and position a brand using a positioning map to find gaps.",
    objectives=[
        "Explain the bases of market segmentation: demographic, geographic, psychographic and behavioural",
        "Compare mass, niche and differentiated targeting and calculate the value of a segment",
        "Use a positioning map to analyse competitors and identify gaps",
        "Evaluate a segmentation and positioning strategy",
    ],
    key_concepts=["Market segmentation", "Demographic segmentation", "Psychographic segmentation",
                  "Behavioural segmentation", "Targeting", "Niche marketing", "Mass marketing", "Positioning", "Positioning map"],
    blocks=[
        H("Introduction"),
        T("Mobile phone networks sell cheap daily data bundles to students, monthly business plans to companies and roaming "
          "packs to travellers. They do not treat 'the market' as one group. They **segment** it, choose which segments to "
          "**target**, and **position** each offer in customers' minds. This sequence is called STP."),
        D("Dividing a market into groups of customers with similar needs or characteristics who will respond similarly to a "
          "marketing mix.", title="Market segmentation"),
        KEY("Bases of segmentation", "Firms often combine several bases.", cards=[
            ["Demographic", "Age, gender, income, family size, occupation, education."],
            ["Geographic", "Region, town or village, climate, urban or rural."],
            ["Psychographic", "Lifestyle, values, personality, social class, attitudes (for example health-conscious buyers)."],
            ["Behavioural", "How customers use the product: frequency, loyalty, benefits sought, occasion (weddings, school start)."],
        ]),
        T("A useful segment is **measurable** (its size can be estimated), **substantial** (large enough to be profitable), "
          "**accessible** (the firm can reach it) and **distinct** (it responds differently from other segments)."),
        EX("Worked example 1: valuing a segment", intro="A firm making baby food estimates that 12% of the 500 000 households in its "
           "region have a child under two, and that each such household spends FCFA 2 500 a month on baby food (invented figures). "
           "Estimate the annual value of the segment.", steps=[
            S("Households in the segment", math=r"0.12 \times 500\,000 = 60\,000"),
            S("Annual spending per household", math=r"2\,500 \times 12 = 30\,000 \text{ FCFA}"),
            S("Segment value", math=r"60\,000 \times 30\,000 = 1\,800\,000\,000 \text{ FCFA}", text="About FCFA 1.8 billion a year: substantial enough to target."),
        ]),
        H("Targeting"),
        KEY("Targeting strategies", "Which segments will the firm serve?", cards=[
            ["Mass (undifferentiated)", "One mix for the whole market. Economies of scale, but ignores different needs; suits basic goods such as salt or sugar."],
            ["Differentiated", "A different mix for each of several segments. Wider reach, but higher costs."],
            ["Niche (concentrated)", "One small, specialised segment. Less competition and higher prices, but dependence on a small market and risk of larger rivals entering."],
        ]),
        H("Positioning"),
        D("The place a brand occupies in customers' minds relative to competitors, built through its product, price, image and promotion.", title="Positioning"),
        IMG("albsl-positioning-map.svg", alt="Positioning map: price on the vertical axis, quality on the horizontal axis. "
            "W is high price, premium quality; X and Y are low price, basic quality; planned brand Z sits in the empty "
            "good quality, low price area.",
            caption="Figure 1. A positioning map for cooking oil brands (invented)."),
        EX("Worked example 2: reading the positioning map", intro="Use Figure 1 to advise a firm planning brand Z.", steps=[
            S("Describe", text="W is premium and expensive; X and Y compete closely at low price and basic quality."),
            S("Identify the gap", text="No brand offers good quality at a low price."),
            S("Question the gap", text="A gap is only worth filling if customers want that combination and the firm can make a profit at that price."),
            S("Advice", text="Research demand and costs; if both are favourable, position Z as 'quality you can afford' and avoid head-on competition with X and Y."),
        ]),
        MISTAKE("Assuming every gap on a map is an opportunity", "Some gaps exist because there is no demand or no way to make a "
                "profit there. Always ask why the gap is empty."),
        MISTAKE("Confusing segmentation with targeting", "Segmentation divides the market; targeting chooses which segments to serve."),
        QUIZ("Segmenting customers by whether they are health-conscious or not is",
             ["geographic", "demographic", "psychographic", "behavioural by occasion"], 2,
             "Attitudes and lifestyle are psychographic bases.",
             feedback=["Geographic is about location.", "Demographic is about age, income, gender and similar.", "",
                       "Occasion refers to when a product is bought, not attitudes."]),
        QUIZ("A small firm makes handmade leather shoes for wealthy professionals only. Its targeting strategy is",
             ["mass marketing", "niche marketing", "differentiated marketing", "undifferentiated marketing"], 1,
             "Serving one small, specialised segment is niche marketing.",
             feedback=["Mass marketing targets the whole market.", "", "Differentiated marketing serves several segments with different mixes.",
                       "Undifferentiated is another name for mass marketing."]),
        PQ("A market has 800 000 consumers; 15% are in a target segment, each spending FCFA 1 000 a month. Estimate the annual value of the segment.",
           "Segment size = 0.15 x 800 000 = 120 000. Annual spend each = 12 000. Value = 120 000 x 12 000 = FCFA 1 440 000 000 (1.44 billion)."),
        PQ("Explain two benefits of segmentation for a bank.",
           "(1) It can design products for each group, such as student accounts and business loans, raising sales. (2) It can "
           "aim promotion at the right customers through the right media, so marketing money is not wasted."),
        PQ("Evaluate niche marketing as a strategy for a new Cameroonian cosmetics firm.",
           "Plan: For: avoids head-on competition with large international brands; can charge higher prices for products for "
           "specific skin or hair types; builds loyalty. Against: small market limits growth; larger firms may copy; dependence on "
           "one segment. Judgement: a sensible entry strategy if the niche is substantial and the firm builds a strong brand, "
           "with plans to widen later."),
        SUM("Segmentation divides a market by demographic, geographic, psychographic or behavioural characteristics.",
            "Good segments are measurable, substantial, accessible and distinct; value = number of buyers x annual spending.",
            "Targeting may be mass, differentiated or niche, each with costs and risks.",
            "Positioning is the place a brand holds in customers' minds compared with rivals.",
            "Positioning maps reveal gaps, but a gap is worth filling only if there is profitable demand."),
    ],
))


# ---------------------------------------------------------------------------
# M4 / The product life cycle and the Boston matrix
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M4, topic="The product life cycle and the Boston matrix",
    title="The product life cycle, extension strategies and the Boston matrix",
    slug="bsl-product-life-cycle-boston-matrix",
    minutes=23,
    summary="The stages of the product life cycle and their cash-flow effects, extension strategies, and the Boston matrix (stars, cash cows, question marks, dogs) with relative market share, used to manage a product portfolio.",
    objectives=[
        "Describe the stages of the product life cycle and the cash flow and marketing at each stage",
        "Explain extension strategies and when to use them",
        "Calculate relative market share and place products in the Boston matrix",
        "Use and evaluate the Boston matrix to manage a product portfolio",
    ],
    key_concepts=["Product life cycle", "Extension strategy", "Product portfolio", "Boston matrix",
                  "Relative market share", "Star", "Cash cow", "Question mark", "Dog"],
    blocks=[
        H("Introduction"),
        T("Products are born, grow, mature and decline. A soft drink launched with heavy advertising may take years to become "
          "popular, sell steadily for a decade and then lose customers to new flavours. A firm with several products must decide "
          "which to support, which to milk for cash and which to drop. Two tools help: the **product life cycle** and the "
          "**Boston matrix**."),
        H("The product life cycle"),
        IMG("albsl-plc-curve.svg", alt="Sales curve over time: low and slowly rising in introduction, rising steeply in growth, "
            "levelling off and peaking in maturity, then falling in decline.", caption="Figure 1. The product life cycle."),
        KEY("Stages, cash flow and marketing", "Cash flow is usually negative early and strongest in maturity.", cards=[
            ["Introduction", "Low sales, high promotion costs, often losses and negative cash flow. Prices may be skimming or penetration."],
            ["Growth", "Sales rise fast; rivals enter; profits begin; cash flow improves but investment in capacity continues."],
            ["Maturity", "Sales peak and level off; competition is intense; cash flow is strongest; extension strategies used."],
            ["Decline", "Sales fall as tastes change or better products appear; the firm may cut support, harvest cash or withdraw."],
        ]),
        D("Actions that lengthen the maturity stage: new uses, new markets (for example export), new packaging or sizes, "
          "new flavours or features, price changes, or new promotion.", title="Extension strategies"),
        H("The Boston matrix"),
        T("The Boston Consulting Group's matrix places each product by **market growth** (the growth rate of its market) and "
          "**relative market share** (its share compared with the largest rival)."),
        F(r"\text{Relative market share} = \frac{\text{Product's market share}}{\text{Market share of the largest rival}}", title="Relative market share"),
        IMG("albsl-boston-matrix.svg", alt="Two by two matrix. Vertical axis market growth, high at top. Horizontal axis relative "
            "market share, high on the left. Top left star, top right question mark, bottom left cash cow, bottom right dog.",
            caption="Figure 2. The Boston matrix. Note that high relative share is on the left."),
        KEY("The four categories", "What to do with each.", cards=[
            ["Star (high growth, high share)", "Strong sales, but needs investment to keep up with growth. Support it."],
            ["Cash cow (low growth, high share)", "Generates more cash than it needs. 'Milk' it to fund other products."],
            ["Question mark (high growth, low share)", "Uncertain; needs heavy investment to win share. Build it or drop it."],
            ["Dog (low growth, low share)", "Weak. Withdraw, or keep if it supports other products."],
        ]),
        EX("Worked example 1: relative market share", intro="Product A has a 30% market share and its largest rival 15%. Product B "
           "has a 10% share and the market leader 25%. A's market grows 2% a year; B's grows 12% (invented).", steps=[
            S("Product A", math=r"\frac{30}{15} = 2.0", text="Twice the leading rival's share, in a slow-growing market: a cash cow."),
            S("Product B", math=r"\frac{10}{25} = 0.4", text="Well below the leader, in a fast-growing market: a question mark."),
            S("Portfolio advice", text="Use the cash from A to fund marketing for B, if research suggests B can win share."),
        ]),
        EX("Worked example 2: linking the two models", intro="Explain how the PLC and the Boston matrix connect.", steps=[
            S("Introduction and growth", text="New products in growing markets are usually question marks; successful ones become stars."),
            S("Maturity", text="As market growth slows, stars with high share become cash cows."),
            S("Decline", text="Products losing share in a slow market become dogs."),
            S("Use", text="A balanced portfolio has cash cows funding stars and selected question marks, with new products launched before cash cows decline."),
        ]),
        KEY("Evaluating the Boston matrix", "Use in essays.", cards=[
            ["Strengths", "Simple picture of the whole portfolio; links products to cash flow; helps decide where to invest."],
            ["Limits", "Only two variables; ignores profit and links between products (a dog may support a cash cow); categories depend on where lines are drawn; a snapshot that quickly dates."],
        ]),
        MISTAKE("Reading the share axis the wrong way", "In the standard matrix, high relative market share is on the **left**. "
                "Check the axis labels before placing a product."),
        MISTAKE("Assuming every product follows the PLC on a fixed timetable", "Stage lengths vary widely and some products stay in "
                "maturity for decades with good extension strategies. The PLC describes, it does not predict."),
        QUIZ("A product has a large share of a market that is growing slowly. In the Boston matrix it is a",
             ["star", "cash cow", "question mark", "dog"], 1,
             "High share and low growth: cash cow.",
             feedback=["A star is in a high-growth market.", "", "A question mark has low share in a high-growth market.",
                       "A dog has low share."]),
        QUIZ("At which stage of the product life cycle is cash flow usually most negative?",
             ["Introduction", "Growth", "Maturity", "Decline"], 0,
             "Development and launch promotion costs are high while sales are low.",
             feedback=["", "Sales are rising quickly and cash flow is improving.", "Maturity usually gives the strongest cash flow.",
                       "Spending is usually cut in decline."]),
        PQ("Product C has an 18% share; its largest rival has 24%. Calculate C's relative market share and explain what it means.",
           "18 / 24 = 0.75. C's share is three-quarters of the leader's, so it is not the market leader (relative share below 1)."),
        PQ("Explain two extension strategies a bottled-water firm could use in maturity.",
           "(1) New sizes such as small sachet-style bottles for street sale or large containers for offices. (2) New markets, for "
           "example selling to schools or exporting to neighbouring countries. Both raise sales without a completely new product."),
        PQ("Evaluate the usefulness of the Boston matrix to a firm with five products.",
           "Plan: Useful: shows which products produce cash and which need it; supports a balanced portfolio and investment "
           "decisions. Limits: ignores profitability and product links; categories are crude; market definitions can change the "
           "result; needs market data. Judgement: a useful starting point that must be combined with profit data, the PLC and "
           "managers' judgement."),
        SUM("PLC stages: introduction, growth, maturity, decline; cash flow is weakest at launch and strongest in maturity.",
            "Extension strategies (new uses, markets, packaging, features, promotion) prolong maturity.",
            "Relative market share = product's share / largest rival's share; above 1 means market leader.",
            "Boston matrix: stars, cash cows, question marks, dogs; cash cows fund stars and question marks.",
            "Both models simplify; use them with profit data and judgement."),
    ],
))


# ---------------------------------------------------------------------------
# M4 / The marketing mix
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M4, topic="The marketing mix",
    title="The integrated 7Ps marketing mix, pricing and price elasticity",
    slug="bsl-marketing-mix-7ps-pricing",
    minutes=24,
    summary="The seven elements of the marketing mix (product, price, place, promotion, people, process, physical evidence), pricing methods with cost-plus and price elasticity calculations, promotion and channels, and why the mix must be integrated.",
    objectives=[
        "Explain the 7Ps and why services need people, process and physical evidence",
        "Calculate cost-plus prices and price elasticity of demand and use them in pricing decisions",
        "Compare pricing strategies, forms of promotion and distribution channels",
        "Evaluate whether a marketing mix is integrated and suits the target market",
    ],
    key_concepts=["Marketing mix", "7Ps", "Cost-plus pricing", "Penetration pricing", "Price skimming",
                  "Price elasticity of demand", "Above-the-line promotion", "Below-the-line promotion", "Channel of distribution"],
    blocks=[
        H("Introduction"),
        T("A new brand of plantain chips in Douala needs more than a good recipe. It needs the right pack, a price students can "
          "afford, shelves in kiosks and supermarkets, promotion on social media and radio, friendly sales staff and a clean "
          "stand. These decisions together form the **marketing mix**, and they must fit each other and the target market."),
        D("The combination of decisions a business makes to market a product to its target market. For goods the 4Ps are "
          "**product, price, place, promotion**. For services (and increasingly for goods) three more are added: **people, "
          "process and physical evidence**.", title="Marketing mix"),
        KEY("The extra 3Ps", "Important wherever customers experience a service.", cards=[
            ["People", "Staff who deal with customers: their skills, attitude and appearance."],
            ["Process", "How the service is delivered: speed, ease of payment (for example mobile money), booking, after-sales."],
            ["Physical evidence", "What customers can see: premises, uniforms, packaging, receipts, website, reviews."],
        ]),
        H("Price"),
        F(r"\text{Price} = \text{Unit cost} \times (1 + \text{mark-up})", title="Cost-plus pricing"),
        KEY("Pricing strategies", "Choose by objective, product stage and competition.", cards=[
            ["Penetration", "Low launch price to win market share quickly; raise later. Suits mass markets with many rivals."],
            ["Skimming", "High launch price for an innovative product, lowered over time. Suits new technology and early adopters."],
            ["Competitive and psychological", "Price close to rivals (price taker); prices such as 990 instead of 1 000."],
            ["Price discrimination", "Different prices for different groups or times, such as student or off-peak prices."],
        ]),
        D("The responsiveness of quantity demanded to a change in price.", title="Price elasticity of demand (PED)",
          formula=r"\text{PED} = \frac{\%\ \text{change in quantity demanded}}{\%\ \text{change in price}}"),
        T("If PED is greater than 1 (ignoring the minus sign), demand is **price elastic**: a price rise reduces revenue. If PED "
          "is less than 1, demand is **inelastic**: a price rise increases revenue. Brands, few substitutes and necessities "
          "make demand more inelastic."),
        EX("Worked example 1: cost-plus price and PED", intro="The chips cost FCFA 800 a pack to make and the firm adds a 25% "
           "mark-up. Later it raises the price to FCFA 1 100 and weekly sales fall from 5 000 to 4 400 packs.", steps=[
            S("Cost-plus price", math=r"800 \times 1.25 = 1\,000 \text{ FCFA}"),
            S("Percentage change in price", math=r"\frac{1\,100 - 1\,000}{1\,000} \times 100 = +10\%"),
            S("Percentage change in quantity", math=r"\frac{4\,400 - 5\,000}{5\,000} \times 100 = -12\%"),
            S("PED", math=r"\frac{-12}{+10} = -1.2", text="Elastic: quantity changes proportionally more than price."),
            S("Revenue check", math=r"1\,000 \times 5\,000 = 5\,000\,000 \to 1\,100 \times 4\,400 = 4\,840\,000", text="Revenue falls by FCFA 160 000, as expected with elastic demand."),
        ]),
        H("Promotion and place"),
        T("**Above-the-line** promotion uses paid mass media: television, radio, newspapers, billboards, online adverts. "
          "**Below-the-line** promotion is more targeted: sales promotions (free samples, buy-one-get-one), personal selling, "
          "sponsorship, public relations, direct marketing, social media influencers and events.\n\n"
          "**Place** covers how the product reaches customers. Channels can be direct (producer to consumer, including online "
          "sales), one-level (producer to retailer to consumer) or two-level (producer to wholesaler to retailer to consumer). "
          "Many Cameroonian consumer goods reach buyers through wholesalers and small retailers in markets and neighbourhoods."),
        H("An integrated mix"),
        EX("Worked example 2: is the mix integrated?", intro="A firm sells a premium skin cream at a high price, but distributes it "
           "through roadside kiosks with no staff training and promotes it with 'cheapest in town' radio adverts. Evaluate the mix.", steps=[
            S("Product and price", text="Premium product and high price fit each other."),
            S("Place", text="Roadside kiosks do not match a premium image; pharmacies or beauty shops fit better."),
            S("Promotion", text="'Cheapest in town' contradicts the high price and premium position."),
            S("People and physical evidence", text="Untrained sellers and plain stands weaken trust in a premium product."),
            S("Judgement", text="The mix is not integrated; customers receive mixed messages. Align place, promotion and people with the premium positioning."),
        ]),
        TIP("Exam link: PED and cost-plus calculations appear in Paper 1 and case studies; Paper 2 and the case study often ask "
            "you to recommend or evaluate a marketing mix. Link every P to the target market and to the other Ps."),
        MISTAKE("Saying a price rise always increases revenue", "It does so only when demand is price inelastic. Use PED to decide."),
        MISTAKE("Treating the Ps separately", "Examiners reward showing how the Ps support each other and suit the target segment, "
                "not a list of seven separate points."),
        QUIZ("A product's price falls by 5% and quantity demanded rises by 2%. What is the PED and what happens to revenue?",
             ["-2.5, revenue rises", "-0.4, revenue falls", "-0.4, revenue rises", "-2.5, revenue falls"], 1,
             "PED = +2 / -5 = -0.4, inelastic. A price cut with inelastic demand reduces revenue.",
             feedback=["This divides the price change by the quantity change, so the PED is upside down.", "",
                       "With inelastic demand a price cut reduces revenue.",
                       "The division is upside down; and if demand really were elastic, a price cut would raise revenue."]),
        QUIZ("A firm launches a new smartphone at a high price, aiming at early adopters, and lowers it later. This is",
             ["penetration pricing", "price skimming", "cost-plus pricing", "psychological pricing"], 1,
             "A high launch price lowered over time is skimming.",
             feedback=["Penetration starts low.", "", "Cost-plus adds a mark-up to cost.", "Psychological pricing uses prices like 990."]),
        PQ("A product costs FCFA 1 600 to make. Calculate its price with a 40% mark-up.",
           "1 600 x 1.40 = FCFA 2 240."),
        PQ("Price rises from FCFA 500 to FCFA 550 and sales fall from 2 000 to 1 900 units. Calculate PED and the change in revenue.",
           "Price +10%; quantity -5%; PED = -5 / 10 = -0.5 (inelastic). Revenue: 500 x 2 000 = 1 000 000; 550 x 1 900 = 1 045 000; "
           "revenue rises by FCFA 45 000."),
        PQ("Evaluate the importance of 'people' in the marketing mix of a private hospital.",
           "Plan: Important: patients judge quality largely through doctors' and nurses' skill and care; trust and reputation "
           "spread by word of mouth; process and physical evidence (cleanliness, waiting times) also matter. Other Ps: price "
           "must match patients' incomes and insurance; place (location, opening hours). Judgement: people are probably the most "
           "important P for a hospital, but only if supported by process and physical evidence."),
        SUM("The 7Ps: product, price, place, promotion, people, process and physical evidence.",
            "Cost-plus price = unit cost x (1 + mark-up); pricing strategies include penetration, skimming and discrimination.",
            "PED = % change in quantity / % change in price; elastic demand means a price rise cuts revenue.",
            "Promotion is above or below the line; channels may be direct, one-level or two-level.",
            "A good mix is integrated: every P fits the others and the target market."),
    ],
))


# ---------------------------------------------------------------------------
# Examination / Paper 1
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=MX, topic="Paper 1",
    title="Paper 1: multiple-choice strategy for Business Studies",
    slug="bsl-paper1-multiple-choice",
    minutes=19,
    summary="How to approach the 50 multiple-choice questions of Business Studies Paper 1: reading the stem, handling 'best' and 'most likely' questions, quick calculations, eliminating distractors, and the traps set in each Lower Sixth module.",
    objectives=[
        "Describe what Paper 1 tests and plan how to work through it",
        "Use a step-by-step method to answer knowledge, calculation and judgement questions",
        "Recognise the common distractors in each Lower Sixth module",
        "Practise with timed questions and review errors by topic",
    ],
    key_concepts=["Stem", "Distractor", "Key word", "Elimination", "Calculation question", "Best-answer question"],
    blocks=[
        H("What Paper 1 is"),
        T("According to KKEVO's curriculum blueprint, Business Studies Paper 1 is made of **50 multiple-choice questions** covering "
          "the whole syllabus. This subject is not covered in the Board's 2023 Advanced Level report, so check the exact format, "
          "timing and instructions with your teacher. The method below works for any multiple-choice business paper."),
        D("The **stem** is the question or statement. The **key** is the correct option. **Distractors** are wrong options "
          "designed to attract candidates who make a common mistake.", title="Parts of a multiple-choice question"),
        KEY("Three kinds of question", "Recognise the kind first; each needs a different approach.", cards=[
            ["Knowledge", "Define or identify: 'Unity of command means...'. Know your definitions and which thinker said what."],
            ["Calculation", "Added value, market share, labour turnover, PED, moving averages, relative market share. Work it out before looking at the options."],
            ["Judgement", "'Which is the most likely...', 'Which is the best...'. Several options may be partly true; choose the one that best fits the situation in the stem."],
        ]),
        H("A method for every question"),
        EX("Worked example 1: a judgement question", intro="'A firm's sales rise by 6% while its market grows by 9%. Which is the "
           "most likely conclusion? A: its market share has risen. B: its market share has fallen. C: its profit has fallen. D: "
           "the market is in decline.'", steps=[
            S("Read the stem and underline the key words", text="Sales +6%, market +9%, 'most likely conclusion'."),
            S("Recall the rule", text="Share rises only if the firm grows faster than the market."),
            S("Eliminate", text="A contradicts the rule; C cannot be known (no cost data); D contradicts market growth of 9%."),
            S("Choose", text="B: market share has fallen."),
        ]),
        EX("Worked example 2: a calculation question", intro="'A firm had 180 staff at the start of the year and 220 at the end; "
           "30 left. What is labour turnover? A 13.6% B 15% C 16.7% D 30%'", steps=[
            S("Work it out first", math=r"\text{Average} = \frac{180 + 220}{2} = 200, \quad \frac{30}{200} \times 100 = 15\%"),
            S("Spot the distractors", text="13.6% divides by 220 (closing staff); 16.7% divides by 180 (opening staff); 30% treats the number of leavers as a percentage."),
            S("Choose", text="B, 15%."),
        ]),
        KEY("Traps by module", "Distractors are built from these mistakes.", cards=[
            ["Enterprise and environment", "Added value v profit; limited v unlimited liability; the FCFA's fixed rate with the euro; stakeholder v shareholder."],
            ["Management theory", "Taylor v Fayol v Weber v Mayo; span (width) v chain of command (length); delegating authority, not responsibility."],
            ["People", "Theory X/Y as managers' assumptions; Herzberg's hygiene v motivators; Vroom multiplies; average staff in turnover."],
            ["Marketing", "Share v sales growth; quota v stratified; seasonal variation = actual - trend; high relative share on the left of the Boston matrix; PED sign and revenue effect."],
        ]),
        TIP("Do the questions you are sure of first, mark the others and return to them. Never leave a question blank unless your "
            "teacher tells you that wrong answers lose marks; check the instructions on the paper."),
        TIP("For 'NOT' or 'EXCEPT' questions, circle the word. Three options will be true; you are looking for the false one."),
        MISTAKE("Looking at the options before working out a calculation", "The distractors are the answers to common mistakes, so "
                "an option that 'looks right' may be the result of an error. Calculate first, then match."),
        MISTAKE("Choosing an option that is true but does not answer the stem", "In judgement questions, several statements can be "
                "true. Choose the one that answers the exact question, for the situation described."),
        QUIZ("Which of the following is NOT a feature of Weber's bureaucracy?",
             ["A hierarchy of offices", "Written rules applied impersonally", "Decisions made through informal friendships", "Promotion on merit"], 2,
             "Weber stressed formal, impersonal rules; informal friendship-based decisions are the opposite.",
             feedback=["This is a feature of bureaucracy.", "This is a feature of bureaucracy.", "", "This is a feature of bureaucracy."]),
        QUIZ("Before choosing an answer to 'Calculate the PED when price rises 10% and quantity falls 15%', you should first",
             ["look for the option closest to 1", "work out -15 / 10 = -1.5 yourself", "choose the largest number", "skip all calculation questions"], 1,
             "Calculate first; then match your answer to the options.",
             feedback=["PED can be far from 1.", "", "Size alone does not make an option correct.", "Calculation questions are often quick marks."]),
        PQ("Explain how you would tackle a Paper 1 question beginning 'Which is the most likely reason...'.",
           "Underline the key facts in the stem; recall the relevant theory; cross out options that contradict the facts or are "
           "irrelevant; of the remaining options, choose the one that best explains the situation described, not one that is merely true."),
        PQ("A friend scores 31 out of 50 on a practice paper. Suggest how she should use the results to improve.",
           "Sort the wrong answers by topic and by type (knowledge, calculation, judgement); revise the weakest topics with their "
           "lessons; redo the practice sets; note which distractors caught her and the mistake behind each."),
        PQ("Why is it useful to know the common mistakes in each topic before Paper 1?",
           "Distractors are built from those mistakes. Knowing them, for example dividing labour turnover by closing staff, lets "
           "you recognise and avoid the trap option."),
        SUM("Paper 1 (blueprint): 50 multiple-choice questions across the syllabus; check the exact format with your teacher.",
            "Identify the question type: knowledge, calculation or judgement.",
            "Calculate before looking at the options; distractors are the answers to common mistakes.",
            "In 'most likely' and 'best' questions, choose the option that fits the situation in the stem.",
            "Review practice papers by topic and by mistake type, then revise those lessons."),
    ],
))


# ---------------------------------------------------------------------------
# Examination / Paper 2
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=MX, topic="Paper 2",
    title="Paper 2: writing management and business essays",
    slug="bsl-paper2-essay-technique",
    minutes=21,
    summary="How to answer Business Studies Paper 2 essays: command words, planning, building analysis with chains of reasoning, using theory and calculations, applying to the business, and reaching a supported judgement.",
    objectives=[
        "Interpret the command words used in business essays",
        "Plan an essay with an introduction, developed points and a judgement",
        "Build analysis using chains of reasoning, theory, data and diagrams",
        "Write evaluation that reaches a supported, conditional judgement",
    ],
    key_concepts=["Command word", "Knowledge", "Application", "Analysis", "Evaluation", "Chain of reasoning", "Judgement"],
    blocks=[
        H("What Paper 2 is"),
        T("KKEVO's curriculum blueprint describes Paper 2 as management and business **essays**. The number of questions, the "
          "choice and the timing are not given in any Board report we can quote, so check the exact format with your teacher. "
          "Whatever the format, examiners reward the same four skills: **knowledge**, **application**, **analysis** and "
          "**evaluation**."),
        KEY("The four skills", "Every good essay shows all four.", cards=[
            ["Knowledge", "Accurate definitions, theories and formulae: Herzberg's motivators, Mendelow's matrix, PED."],
            ["Application", "Using the business, industry or country in the question: a Cameroonian bank, a cooperative, a brewery."],
            ["Analysis", "Explaining cause and effect in steps: this leads to that, which means..."],
            ["Evaluation", "Weighing arguments, deciding which matters most and on what it depends, then reaching a judgement."],
        ]),
        H("Command words"),
        KEY("What the question asks you to do", "Underline the command word first.", cards=[
            ["Explain / Analyse", "Give reasons and develop the chain of cause and effect; no judgement is needed, but analysis must be deep."],
            ["Discuss / Evaluate / Assess / To what extent", "Give both sides, weigh them and reach a judgement."],
            ["Compare / Distinguish", "Show similarities and differences point by point, not two separate descriptions."],
        ]),
        H("Planning"),
        T("Spend a few minutes planning before writing. A plan lists: a definition of the key terms; three or four developed "
          "points, each with a theory or example; points on the other side; and the judgement you will reach and the condition it "
          "depends on. Planning stops you repeating yourself and keeps the essay focused on the question."),
        EX("Worked example 1: a chain of reasoning", intro="Show the difference between a simple point and analysis for 'Why might delayering improve a firm's performance?'", steps=[
            S("Simple point (knowledge only)", text="'Delayering removes a level of management.'"),
            S("Add the first link", text="'...which shortens the chain of command,'"),
            S("Add the second link", text="'so decisions and information pass between senior managers and customers faster,'"),
            S("Add the consequence", text="'allowing the firm to respond to changes in demand before rivals, which can raise sales and market share.'"),
            S("Add application", text="'For a mobile phone network facing fast-moving competition, this speed is especially valuable.'"),
        ]),
        EX("Worked example 2: model essay plan", intro="'Financial rewards are the most effective way to motivate employees in a "
           "Cameroonian manufacturing firm.' Discuss.", steps=[
            S("Introduction", text="Define motivation and financial rewards (piece rate, bonus, profit sharing). State the line of argument."),
            S("Point for", text="Taylor and Maslow's lower needs: where wages are low, more pay meets basic and safety needs; piece rates raise output on repetitive lines."),
            S("Point for", text="Vroom: a credible, valued bonus raises motivational force; calculation example."),
            S("Point against", text="Herzberg: pay is a hygiene factor; lasting motivation needs recognition, responsibility and job enrichment."),
            S("Point against", text="Adams: unfair pay differences demotivate; piece rates may reduce quality and teamwork."),
            S("Judgement", text="Financial rewards are necessary and effective for routine output where pay is low, but most effective when combined with non-financial methods; it depends on the job, the workers' needs and the fairness of the scheme."),
        ]),
        H("Writing evaluation"),
        T("Evaluation is more than 'on the other hand'. Strong evaluation: weighs which factor matters most; says **it depends on** "
          "specific conditions (the size of the firm, the market, the time scale, the stakeholders); considers short run against "
          "long run; and gives a clear final judgement that follows from the argument. Use diagrams (Boston matrix, Mendelow's "
          "matrix, Blake-Mouton grid) or small calculations where they support a point, and refer to them in your text."),
        TIP("Use one paragraph per point, starting with the point in one sentence, then the chain of reasoning, then application. "
            "Examiners read many scripts; a clear structure helps them find your marks."),
        MISTAKE("Writing everything you know about a topic", "Knowledge not linked to the question gains little. Every paragraph "
                "should answer the question set."),
        MISTAKE("Ending with a vague conclusion", "'There are advantages and disadvantages' is not a judgement. Say which side is "
                "stronger and on what it depends."),
        QUIZ("Which command word requires a judgement?", ["Explain", "Describe", "Evaluate", "State"], 2,
             "Evaluate (like discuss and assess) asks you to weigh arguments and decide.",
             feedback=["Explain asks for reasons, not a judgement.", "Describe asks what something is like.", "",
                       "State asks for a brief fact."]),
        QUIZ("Which sentence shows the best evaluation?",
             ["There are many advantages and disadvantages of CSR.",
              "CSR is good for business.",
              "For a mining firm whose activity visibly affects local water, CSR is likely to be worth its cost because it protects its licence to operate, but less so for a small trader with little impact.",
              "Carroll described a pyramid of CSR."], 2,
             "It weighs the case, gives conditions and reaches a judgement for a specific business.",
             feedback=["This states both sides exist but decides nothing.", "This is an unsupported assertion.", "",
                       "This is knowledge, not evaluation."]),
        PQ("Turn this point into a chain of reasoning: 'Training raises productivity.'",
           "Training improves workers' skills, so they make fewer errors and work faster; output per worker rises, so unit labour "
           "costs fall; the firm can cut prices or raise margins, improving competitiveness. For example, a garment workshop whose "
           "machinists learn faster techniques can meet larger orders without extra staff."),
        PQ("Write a plan for: 'To what extent should a family business convert from an SARL to an SA in order to grow?'",
           "Define SARL and SA. For: access to large capital, status, possible public offer. Against: loss of family control, "
           "formalities and disclosure, divorce of ownership and control, alternative finance. Judgement: depends on how much "
           "capital is needed and how much the family values control."),
        PQ("Explain the difference between 'explain' and 'discuss' questions and how your answer should change.",
           "Explain: give reasons and develop them; no judgement needed. Discuss: present both sides, weigh them and reach a "
           "supported judgement, so leave time for evaluation and a conclusion."),
        SUM("Paper 2 (blueprint): management and business essays; check the exact format with your teacher.",
            "Show knowledge, application, analysis and evaluation in every essay.",
            "Read the command word: explain and analyse need reasons; discuss, evaluate and assess need a judgement.",
            "Plan first: definitions, developed points, the other side, and the judgement.",
            "Analysis is a chain of reasoning; evaluation weighs factors and says what the judgement depends on."),
    ],
))


# ---------------------------------------------------------------------------
# Examination / Paper 3
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=MX, topic="Paper 3",
    title="Paper 3: the business case study method",
    slug="bsl-paper3-case-study-method",
    minutes=22,
    summary="A step-by-step method for the Business Studies case study: reading the case actively, finding the business's objectives and problems, using the data with quick calculations, applying theory to the case, and writing supported recommendations.",
    objectives=[
        "Read a case study actively and identify the business's situation, objectives and stakeholders",
        "Extract and calculate key figures from case data and interpret them",
        "Apply Lower Sixth theory directly to the case rather than in general",
        "Write a justified recommendation that weighs options and risks",
    ],
    key_concepts=["Case study", "Context", "Application", "Data interpretation", "Recommendation", "Justification"],
    blocks=[
        H("What Paper 3 is"),
        T("KKEVO's curriculum blueprint describes Paper 3 as a **business case study**: an account of a business, often with "
          "tables of data, followed by questions. The length, the number of questions and the timing are not given in any Board "
          "report we can quote, so check the exact format with your teacher. What is certain is that case-study marks go to "
          "answers that use the **case**: its people, its numbers, its market and its problems."),
        H("Step 1: read actively"),
        T("Read the questions first, so you know what to look for. Then read the case twice. On the second reading, mark: the "
          "legal form and size of the business; its objectives; its stakeholders and their conflicts; its problems and "
          "opportunities; and every number. Write a short note in the margin beside each paragraph ('labour turnover rising', "
          "'new rival')."),
        H("Step 2: work with the data"),
        CODE("""
Sunrise Juice SARL, Bafoussam (invented)    Last year   This year
Sales revenue (FCFA million)                      240         276
Regional juice market (FCFA million)            1 600       1 760
Staff at start of year                             70          80
Staff leaving during the year                       -          12
Staff at end of year                               80          80
""", "text", title="Table 1. Extract from a case study"),
        EX("Worked example 1: turning data into evidence", intro="Use Table 1 to judge Sunrise Juice's performance.", steps=[
            S("Sales growth", math=r"\frac{276 - 240}{240} \times 100 = 15\%"),
            S("Market growth", math=r"\frac{1\,760 - 1\,600}{1\,600} \times 100 = 10\%"),
            S("Market share", math=r"\frac{240}{1\,600} = 15\% \;\to\; \frac{276}{1\,760} \approx 15.68\%"),
            S("Labour turnover this year", math=r"\frac{12}{(80 + 80)/2} \times 100 = \frac{12}{80} \times 100 = 15\%"),
            S("Interpret", text="Sunrise is growing faster than its market and gaining share, but losing staff at 15% a year; "
              "rising turnover could threaten quality and growth. This is the kind of balanced reading examiners reward."),
        ]),
        H("Step 3: apply theory to the case"),
        T("Choose the theory that fits the problem and use it with the case's details. If staff are leaving, use Herzberg or "
          "Maslow with the facts given (low pay? no promotion? an autocratic manager?). If a product is losing share, use the PLC "
          "or the Boston matrix with the product's actual figures. A theory written out in general, with no link to the case, "
          "earns little."),
        EX("Worked example 2: applied versus generic answers", intro="Question: 'Analyse one reason for Sunrise's labour turnover.' Compare two answers.", steps=[
            S("Generic", text="'Herzberg said hygiene factors cause dissatisfaction, so staff leave.' This could be about any firm."),
            S("Applied", text="'The case says machine operators earn less than at the new brewery nearby and work under close supervision. "
              "Pay below local rates is a hygiene factor causing dissatisfaction, and close supervision removes responsibility, a "
              "motivator, so operators leave for the brewery: 12 of 80 staff left this year.'"),
        ]),
        H("Step 4: recommend and justify"),
        T("Recommendation questions ask you to choose. Set out the options, weigh each against the business's objectives and "
          "resources (use the numbers), consider risks and stakeholders, then decide clearly. Say what the decision depends on and "
          "what the business should do first."),
        EX("Worked example 3: a recommendation plan", intro="'Should Sunrise Juice spend its FCFA 20 million budget on a new bottling "
           "machine or on raising operators' pay and training? Recommend.'", steps=[
            S("Option A: machine", text="Raises capacity for a growing market (sales +15%); but needs skilled operators, who are leaving."),
            S("Option B: pay and training", text="Addresses 15% turnover, protects quality and keeps skills; less immediate capacity."),
            S("Weigh", text="A machine is of little use if trained operators keep leaving; turnover is the binding constraint."),
            S("Recommend", text="Option B first, then the machine once turnover falls; review turnover after six months. Depends on whether demand growth continues."),
        ]),
        TIP("Use the business's name and figures in nearly every paragraph. A useful check: could your paragraph be moved into an "
            "answer about a different business without changes? If so, it is not applied enough."),
        MISTAKE("Copying out the case instead of using it", "Quoting a fact earns credit only if you then explain what it shows and "
                "why it matters for the question."),
        MISTAKE("Recommending without weighing", "Choosing an option with no comparison or conditions is an assertion. Compare the "
                "options and justify the choice with evidence from the case."),
        QUIZ("Which answer shows the best application to a case about a cooperative of coffee farmers?",
             ["Cooperatives are owned by their members.",
              "Motivation theories are important in all businesses.",
              "Because the cooperative's 300 members each have one vote, the plan to cut prices paid to farmers is likely to be voted down.",
              "Businesses have many stakeholders."], 2,
             "It uses specific features of the case (members, voting, the price plan) to reach a conclusion.",
             feedback=["True, but general knowledge.", "Generic; could be about any business.", "", "Generic; no link to the case."]),
        QUIZ("In a case, a firm's sales rose from FCFA 50 million to FCFA 60 million while its market grew from FCFA 400 million to FCFA 500 million. What happened to its market share?",
             ["It rose from 12.5% to 12%", "It fell from 12.5% to 12%", "It rose by 20%", "It stayed the same"], 1,
             "50/400 = 12.5%; 60/500 = 12%. Share fell even though sales rose 20%.",
             feedback=["12% is lower than 12.5%, so the share fell.", "", "20% is the growth of sales, not of share.",
                       "Sales grew 20% but the market grew 25%, so the share changed."]),
        PQ("A case states that a firm's 4 managers each supervise 15 staff and that complaints about slow decisions are rising. "
           "Explain how you would use this in an answer about organisational structure.",
           "Spans of 15 are wide: managers may be overloaded, delaying decisions, which links to the complaints. Possible remedies "
           "applied to the case: appoint supervisors, delegate routine decisions or train staff. Judge against the cost."),
        PQ("Why should you read the questions before reading the case study?",
           "So you know which information to look for and can mark the relevant facts and figures on the first full reading, "
           "saving time and making answers more focused."),
        PQ("Outline a four-step method for answering a case-study recommendation question.",
           "(1) Identify the options and the business's objectives. (2) Use the case data to assess each option (costs, benefits, "
           "risks, stakeholders). (3) Weigh the options against each other. (4) Make a clear recommendation, say what it depends "
           "on and what should be done first."),
        SUM("Paper 3 (blueprint): a business case study; check the exact format with your teacher.",
            "Read the questions first, then the case twice, marking objectives, problems, stakeholders and numbers.",
            "Calculate and interpret key figures: growth, share, turnover, productivity.",
            "Apply theory to the case's own details; generic theory earns little.",
            "Recommend clearly, weighing options with evidence and stating what the decision depends on."),
    ],
))
