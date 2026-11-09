"""Form 5 Commerce (O Level 0520): Production & Scope of Commerce, Home Trade: Retail & Wholesale (lessons).
Draft content: teaching figures are invented for practice; check against the Board's syllabus and your textbook."""

from .dsl import *  # noqa: F403

COURSE = ("commerce", "form-5")

M1 = "Production & Scope of Commerce"
M2 = "Home Trade: Retail & Wholesale"

LESSONS = []

# ------------------------------------------------------------------ 1. Stages of production
LESSONS.append(lesson(
    module=M1, topic="Stages of production",
    title="Stages of production: primary, secondary and tertiary",
    slug="com-stages-of-production",
    minutes=20,
    summary="Production is the creation of goods and services that satisfy wants. Primary production extracts or grows, secondary production manufactures or builds, and tertiary production provides the services that move goods to consumers.",
    objectives=[
        "Define production, goods and services",
        "Name and describe the primary, secondary and tertiary stages of production",
        "Classify an activity or a business into the correct stage",
        "Explain how the stages depend on one another and each adds value",
    ],
    key_concepts=["Production", "Primary production", "Secondary production", "Tertiary production", "Chain of production", "Value added"],
    blocks=[
        H("Introduction"),
        T("Think of a bar of chocolate sold in a shop in Douala. Before you buy it, a farmer grew cocoa, a factory turned the beans into chocolate, "
          "a lorry carried the bars to town, and a shop sold them to you. Each of those steps is a **stage of production**. "
          "Commerce is about understanding how goods and services travel along this chain until they reach the people who want them."),
        D("**Production** is the making of goods and services that satisfy human wants. **Goods** are physical things we can touch (rice, a phone, a chair). "
          "**Services** are activities done for us that we cannot touch (transport, banking, teaching, a haircut).", title="Definition: production"),
        H("The three stages"),
        D("**Primary production** is the growing, rearing or extraction of natural resources. Examples: farming cocoa or plantain, fishing at Limbe, "
          "felling timber, mining sand or oil.", title="Definition: primary production"),
        D("**Secondary production** is the changing of raw materials into finished or semi-finished goods, and the building of houses, roads and bridges. "
          "Examples: a sawmill making planks, a gari factory, a bakery, a cement works, a builder.", title="Definition: secondary production"),
        D("**Tertiary production** is the provision of services. It includes the **commercial services** that help goods reach consumers (trade, transport, banking, insurance, "
          "warehousing, advertising, communication) and **direct services** given to people (teachers, doctors, hairdressers, police).", title="Definition: tertiary production"),
        IMG("f5com-stages.svg", alt="Three boxes from left to right: primary (farmer grows cocoa beans), secondary (factory makes chocolate bars), tertiary (transport and shop bring bars to buyers).",
            caption="Figure 1. The three stages of production, using chocolate as an example."),
        KEY("How to classify an activity", "Ask one question about what the worker is doing.", cards=[
            ["Takes from nature?", "Growing, fishing, mining, forestry: primary."],
            ["Changes or builds something?", "Manufacturing, processing, construction: secondary."],
            ["Serves people or business?", "Trade, transport, banking, teaching: tertiary."],
        ]),
        H("Stages depend on each other"),
        T("The stages form a **chain of production**. Secondary industry needs raw materials from primary industry. Both need tertiary services: "
          "transport to move goods, banks to lend money, insurers to cover risks, and traders to sell. If one link breaks, such as a bad road in the rainy season, the whole chain suffers."),
        T("Every stage adds **value**. Value added is the difference between what a business sells its product for and what it paid for the materials it bought from others."),
        EX("Worked example 1: value added along the chain", intro="Teaching figures (invented for practice). A farmer sells cocoa beans for FCFA 600 000. A factory makes the beans into chocolate and sells it to shops for FCFA 1 500 000. The shops sell it to the public for FCFA 1 800 000. How much value does each stage add?", steps=[
            S("Primary stage", text="The farmer bought no materials from others, so value added is FCFA 600 000."),
            S("Secondary stage", text="The factory sells for 1 500 000 and paid 600 000 for the beans: 1 500 000 − 600 000 = FCFA 900 000."),
            S("Tertiary stage", text="The shops sell for 1 800 000 and paid 1 500 000: 1 800 000 − 1 500 000 = FCFA 300 000."),
            S("Check", text="600 000 + 900 000 + 300 000 = FCFA 1 800 000, the final price paid by the consumer."),
        ], check=r"600\,000 + 900\,000 + 300\,000 = 1\,800\,000"),
        EX("Worked example 2: classify the activities", intro="Place each activity in its stage: (a) a fisherman at Limbe, (b) a company that builds a bridge, (c) a bank lending to a trader, (d) a bakery in Bamenda.", steps=[
            S("(a) Fisherman", text="Takes fish from nature: primary."),
            S("(b) Bridge builder", text="Builds a structure: secondary (construction)."),
            S("(c) Bank", text="Provides a financial service that aids trade: tertiary."),
            S("(d) Bakery", text="Changes flour into bread: secondary."),
        ]),
        T("Some firms work in more than one stage. A palm oil company that owns plantations (primary) and a refinery (secondary) is an example. When asked to classify a business, look at the main activity."),
        MISTAKE("Calling every shop or factory 'secondary'", "A shop sells goods but does not change them, so it is tertiary. Only businesses that change materials into other goods, or build, are secondary. Remember that the commercial services of trade, transport and banking belong to the tertiary stage."),
        MISTAKE("Forgetting that services are production", "Teaching, banking and transport do not produce a physical item, but they are still production because they satisfy wants. They are the tertiary stage."),
        QUIZ("A timber company at a forest site fells trees and sells the logs. Its stage of production is:",
             ["Secondary", "Primary", "Tertiary", "Commercial"], 1,
             "Felling trees takes a resource from nature, so it is primary production.",
             hint="Is the company changing the material or taking it from nature?",
             feedback=["Secondary would be turning the logs into planks.", "", "Tertiary is a service such as transporting the logs.", "Commercial services are part of the tertiary stage."]),
        QUIZ("Which of these is a tertiary activity?",
             ["Making soap in a factory", "Growing maize", "Driving goods from Douala to Yaounde", "Mining sand"], 2,
             "Transport is a service that helps goods reach buyers: tertiary.",
             hint="Which one is a service rather than a thing made or taken from the ground?",
             feedback=["Making soap changes materials: secondary.", "Growing crops is primary.", "", "Mining is primary."]),
        TIP("Exam link: stages of production often appear in Paper 1 as a classification question (which activity is secondary?) and can be the opening part of a Paper 2 essay on the scope of commerce. "
            "Define each stage and give one local example for each."),
        PQ("Define primary, secondary and tertiary production and give one Cameroonian example of each.", "Primary production is growing or extracting natural resources, for example cocoa farming. Secondary production is changing raw materials into goods or building, for example a sawmill making planks. Tertiary production is providing services, for example a bank or a transport company."),
        PQ("Explain why a farmer needs tertiary production to sell his harvest.", "He needs transport to carry the produce to the market, traders to buy it, banks to keep or lend money, and possibly insurance and storage. These services are tertiary, and without them the produce could not reach consumers."),
        PQ("A baker buys flour for FCFA 40 000 and sells bread worth FCFA 95 000 (invented for practice). What is the value added by the baker?", "95 000 − 40 000 = FCFA 55 000."),
        SUM("Production is making goods and services that satisfy wants.",
            "Primary production grows or extracts; secondary production changes materials or builds; tertiary production provides services.",
            "The stages form a chain and each depends on the others.",
            "Each stage adds value; the shops and transport belong to the tertiary stage, not the secondary."),
    ],
))

# ------------------------------------------------------------------ 2. Specialization and division of labour
LESSONS.append(lesson(
    module=M1, topic="Specialization and division of labour",
    title="Specialization and division of labour",
    slug="com-specialization-division-of-labour",
    minutes=20,
    summary="Specialization means concentrating on what one does best; division of labour splits a job into tasks done by different workers. Both raise output but make people depend on exchange and trade.",
    objectives=[
        "Define specialization and division of labour",
        "Identify types of specialization (by person, firm, region and country)",
        "Explain the advantages and disadvantages of division of labour",
        "Explain why specialization leads to trade and why the size of the market limits it",
    ],
    key_concepts=["Specialization", "Division of labour", "Interdependence", "Exchange and trade", "Size of the market"],
    blocks=[
        H("Introduction"),
        T("In a small village, one family may grow food, build its own house and make its own clothes. In a town like Douala, a person usually does one job, such as driving a taxi, and buys everything else. "
          "Doing one thing well and exchanging for the rest is the idea of **specialization**."),
        D("**Specialization** is when a person, firm, region or country concentrates on producing the goods or services it can produce best.", title="Definition: specialization"),
        D("**Division of labour** is the splitting of the production of a good into separate tasks, each done by a different worker or group.", title="Definition: division of labour"),
        T("They are linked but different. Specialization is about what a worker or area does. Division of labour is about breaking one product into stages of work. "
          "In a bakery, one person mixes dough, another bakes, another packs and another sells. That is division of labour."),
        KEY("Types of specialization", "Specialization can happen at several levels.", cards=[
            ["By person", "A tailor, an electrician, a nurse."],
            ["By firm", "A firm that only makes furniture or only sells phones."],
            ["By region", "Some areas become known for a crop or industry, for example coastal areas for fishing and palm products."],
            ["By country", "A country concentrates on what it exports, for example crude oil, cocoa or timber."],
        ]),
        H("Why it raises output"),
        EX("Worked example 1: a small workshop", intro="Teaching figures (invented for practice). One shoemaker working alone makes 4 pairs of shoes a day. A workshop employs 5 workers who divide the work (cutting, stitching, sole fitting, finishing and packing) and together produce 30 pairs a day. By how much does output per worker rise?", steps=[
            S("Output per worker, divided labour", text="30 pairs ÷ 5 workers = 6 pairs per worker per day."),
            S("Output per worker, alone", text="4 pairs per day."),
            S("Increase", text="6 − 4 = 2 pairs per worker per day, which is 50% more."),
        ], check=r"\frac{6-4}{4} = 0.5"),
        T("The gain comes from skill through practice, no time lost moving from one task to another, easier use of machines, and a chance to put each worker in the task that suits him or her best."),
        H("Advantages and disadvantages"),
        KEY("Advantages of division of labour", "These help the producer and often the consumer.", cards=[
            ["Higher output", "More goods are made in the same time."],
            ["Better quality", "Workers become skilled at one task."],
            ["Lower unit cost", "Mass production can bring lower prices."],
            ["Time saved", "No moving between tasks; training is short."],
        ]),
        KEY("Disadvantages of division of labour", "These help explain why it has limits.", cards=[
            ["Boredom", "Repeating one task lowers interest and care."],
            ["Dependence", "If one section stops (strike, breakdown), the whole line stops."],
            ["Unemployment", "Machines may replace workers if skills become out of date."],
            ["Less variety", "Products can become alike and workers lose wider skills."],
        ]),
        H("Specialization leads to trade"),
        T("A specialist produces more of one thing than he needs. He must **exchange** the surplus for other goods and services. "
          "This is why specialization produces **interdependence**: producers depend on one another and on traders, transport, banks and money to carry out the exchanges. "
          "This link between production and trade is the heart of commerce."),
        T("Specialization is limited by the **size of the market**. A tailor in a small village cannot specialize in only wedding dresses if too few customers buy them. Better roads, mobile money and the internet widen the market and allow more specialization."),
        EX("Worked example 2: exchange after specialization", intro="A coastal village specializes in fish and an inland village in plantain. Each has a surplus. Explain what is needed for both to gain.", steps=[
            S("Surplus", text="Each village produces more of its own product than it can use."),
            S("Exchange", text="They exchange (barter) or, more usually, sell for money and buy what they lack."),
            S("Aids needed", text="A road and a vehicle (transport), a market or traders, and money or mobile money for payment."),
            S("Result", text="Both villages have both foods, so they are better off than if each tried to produce everything."),
        ]),
        MISTAKE("Using the two terms as if they were the same", "Division of labour is a way of organising work inside a production process. Specialization is the wider idea that people, firms, regions and countries concentrate on what they do best. Define each separately in an examination."),
        MISTAKE("Listing only advantages", "Questions often ask for both sides. Give at least two advantages and two disadvantages and relate them to a real example such as a factory or bakery."),
        QUIZ("Which of these is a disadvantage of division of labour?",
             ["Higher output", "Workers become more skilled", "Boredom from repeating one task", "Lower cost per unit"], 2,
             "Doing the same small task all day is boring and can lower care and interest.",
             hint="Three of the options are benefits.",
             feedback=["Higher output is an advantage.", "Skill is an advantage.", "", "Lower unit cost is an advantage."]),
        QUIZ("A region that grows mainly cocoa and buys its food from other regions is an example of:",
             ["Division of labour", "Regional specialization", "Barter only", "Primary consumption"], 1,
             "Concentrating on one product that suits the area is regional specialization.",
             hint="The question is about an area, not about a worker.",
             feedback=["Division of labour splits work inside a production process.", "", "Barter is a method of exchange; the region may use money.", "This is not a standard commerce term."]),
        TIP("Exam link: this topic is examined in Paper 1 (definitions, advantages, disadvantages) and may open a Paper 2 essay on production and trade. A good answer always ends by linking specialization to exchange and trade."),
        PQ("Distinguish between specialization and division of labour.", "Specialization is concentrating on producing what a person, firm, region or country does best. Division of labour is splitting the making of one product into separate tasks done by different workers."),
        PQ("State three advantages and two disadvantages of division of labour.", "Advantages: higher output, better quality through skill, lower cost per unit. Disadvantages: boredom, and dependence (if one section stops the whole line stops)."),
        PQ("Explain why specialization leads to trade.", "A specialist produces more of one thing than he needs and lacks other goods. He must exchange the surplus for what he needs, so trade and the services that help it (transport, money, banks) grow."),
        SUM("Specialization is concentrating on what one does best; division of labour splits a product into tasks.",
            "It raises output, quality and often lowers unit cost, but causes boredom, dependence and possible unemployment.",
            "Specialization creates surpluses and interdependence, so trade is needed.",
            "The size of the market limits how far specialization can go."),
    ],
))

# ------------------------------------------------------------------ 3. Trade and the aids to trade
LESSONS.append(lesson(
    module=M1, topic="Trade and the aids to trade",
    title="Trade and the aids to trade",
    slug="com-trade-and-aids-to-trade",
    minutes=20,
    summary="Commerce consists of trade (buying and selling, at home or abroad) and the aids to trade (banking, insurance, transport, warehousing, advertising and communication) that remove the obstacles between producer and consumer.",
    objectives=[
        "Define commerce, trade and aids to trade",
        "Distinguish home trade (retail, wholesale) from foreign trade (import, export, entrepot)",
        "Match each aid to trade with the obstacle it removes",
        "Describe the relationship between production, trade and aids to trade",
    ],
    key_concepts=["Commerce", "Trade", "Home trade", "Foreign trade", "Aids to trade", "Entrepot trade"],
    blocks=[
        H("Introduction"),
        T("A tomato farmer in Dschang cannot eat all his tomatoes, and a customer in Douala wants some. Between them lie distance, time, money and risk. "
          "Commerce is the name for everything that removes these obstacles so that goods reach the people who need them."),
        D("**Commerce** is all the activities that bring goods from producers to consumers. It has two parts: **trade** and the **aids to trade**.", title="Definition: commerce"),
        D("**Trade** is the buying and selling of goods and services.", title="Definition: trade"),
        D("**Aids to trade** are the services that help trade to take place by removing obstacles. They are banking, insurance, transport, warehousing, advertising and communication.", title="Definition: aids to trade"),
        H("Kinds of trade"),
        KEY("Home trade and foreign trade", "Trade inside the country is home trade; trade across borders is foreign trade.", cards=[
            ["Home trade: retail", "Selling in small quantities to final consumers, for example a market stall or a supermarket."],
            ["Home trade: wholesale", "Selling in large quantities to retailers and other businesses."],
            ["Foreign trade: import and export", "Buying from other countries (import) and selling to other countries (export)."],
            ["Foreign trade: entrepot", "Importing goods in order to export them again, as a port city may do for neighbouring countries."],
        ]),
        T("Cameroon's ports and roads link it to neighbouring countries, so entrepot trade is possible. Foreign trade is studied in detail later in the course."),
        H("Obstacles and the aids that remove them"),
        T("Each aid to trade removes one obstacle. Learn the pairs, because examiners ask for them in both multiple choice and essays."),
        CODE("Obstacle                     Aid to trade that removes it\n"
             "--------------------------   ------------------------------\n"
             "Distance (place)             Transport\n"
             "Time (goods wait for buyers) Warehousing\n"
             "Payment and credit           Banking\n"
             "Risk (loss, theft, fire)     Insurance\n"
             "Lack of knowledge of goods   Advertising\n"
             "Lack of information          Communication (phone, post, internet)", "text", title="Obstacles and aids"),
        T("Mobile money is a good local example of banking-type help: it lets a buyer in Bamenda pay a seller in Douala in seconds without travelling."),
        H("The relationship: production, trade and aids"),
        T("Production creates goods. Trade carries goods through the chain of buyers and sellers to the consumer. The aids to trade support both production and trade. "
          "Without aids, trade is slow and risky; without trade, producers have no market; without production, there is nothing to trade."),
        EX("Worked example 1: aids used by a cocoa exporter", intro="A trader in Kumba buys cocoa beans and ships them from Douala. Name the aids he needs and the obstacle each removes.", steps=[
            S("Transport", text="Lorries and ships remove the obstacle of distance."),
            S("Warehousing", text="A store keeps the beans safe until the ship sails: it removes the time obstacle."),
            S("Insurance", text="Covers loss or damage at sea and in storage: it removes risk."),
            S("Banking", text="A bank pays the farmers and handles payment from the foreign buyer: it solves the payment obstacle."),
            S("Communication", text="Phone and email agree the price and the shipping date."),
        ]),
        EX("Worked example 2: classify the activity", intro="Say whether each is trade or an aid to trade: (a) a shopkeeper sells rice, (b) a radio advertisement for a soap, (c) a wholesaler sells cartons of tomato paste to a retailer, (d) a firm insures its shop against fire.", steps=[
            S("(a)", text="Selling goods to consumers: retail trade."),
            S("(b)", text="Advertising: an aid to trade."),
            S("(c)", text="Selling in bulk to a retailer: wholesale (home) trade."),
            S("(d)", text="Insurance: an aid to trade."),
        ]),
        MISTAKE("Listing producers as part of commerce", "Producing is not commerce. Commerce starts when the goods are finished and need to be traded and delivered. Farming and manufacturing are production; the services that help sell and deliver are commerce."),
        MISTAKE("Mixing the obstacle with the aid", "Write 'transport removes distance' not 'distance is the aid'. Keep the pair clear: obstacle, then the aid that removes it."),
        QUIZ("Which aid to trade removes the obstacle of risk of loss by fire or theft?",
             ["Transport", "Insurance", "Advertising", "Warehousing"], 1,
             "Insurance pays compensation for loss, so it removes the risk obstacle.",
             hint="Which service pays you when something goes wrong?",
             feedback=["Transport moves goods; it removes distance.", "", "Advertising informs buyers.", "Warehousing stores goods; it removes time."]),
        QUIZ("Buying goods in a foreign country in order to sell them again to another foreign country is called:",
             ["Retail trade", "Wholesale trade", "Entrepot trade", "Home trade"], 2,
             "Re-exporting imported goods is entrepot trade.",
             hint="The goods come in and then go out again.",
             feedback=["Retail is selling small quantities to consumers.", "Wholesale is home bulk selling.", "", "Home trade stays inside the country."]),
        TIP("Exam link: the scope of commerce appears in Paper 1 (matching obstacles with aids; home vs foreign trade) and underlies many Paper 2 essays. When you list aids, name the obstacle each one removes."),
        PQ("Define commerce and list the aids to trade.", "Commerce is all the activities that bring goods from producers to consumers; it includes trade and the aids to trade. The aids are banking, insurance, transport, warehousing, advertising and communication."),
        PQ("Explain how warehousing and insurance help a retailer.", "Warehousing keeps goods safe until they are needed, so supply is continuous; insurance pays compensation if the goods are lost or damaged, so the retailer can continue in business after a fire or theft."),
        PQ("Distinguish between home trade and foreign trade, with one example of each.", "Home trade is buying and selling within the country, for example a Douala retailer buying from a wholesaler. Foreign trade is buying and selling between countries, for example Cameroon exporting cocoa."),
        SUM("Commerce is trade plus the aids to trade.",
            "Home trade is retail and wholesale; foreign trade is import, export and entrepot.",
            "Each aid removes an obstacle: transport (distance), warehousing (time), banking (payment), insurance (risk), advertising (knowledge), communication (information).",
            "Production, trade and aids depend on one another."),
    ],
))

# ------------------------------------------------------------------ 4. Channels of distribution
LESSONS.append(lesson(
    module=M1, topic="Channels of distribution",
    title="Channels of distribution",
    slug="com-channels-of-distribution",
    minutes=20,
    summary="A channel of distribution is the route goods take from producer to consumer. It may be direct or pass through agents, wholesalers and retailers, and the producer chooses the channel that suits the product and the market.",
    objectives=[
        "Define channel of distribution and middleman",
        "Describe the four main channels",
        "Explain the factors that influence the choice of channel",
        "Discuss the advantages and disadvantages of cutting out middlemen",
    ],
    key_concepts=["Channel of distribution", "Middleman", "Agent", "Wholesaler", "Retailer", "Direct selling"],
    blocks=[
        H("Introduction"),
        T("A woman in Bafoussam grows tomatoes. She may sell them herself at her roadside stall. Or she may sell to a trader who carries them to a wholesaler in Douala, who then sells to market retailers. "
          "These are two different routes from farm to buyer. Each route is a **channel of distribution**."),
        D("A **channel of distribution** is the route by which goods pass from the producer to the final consumer.", title="Definition: channel of distribution"),
        D("A **middleman** (or intermediary) is a person or firm between the producer and the consumer, such as an agent, wholesaler or retailer.", title="Definition: middleman"),
        H("The four main channels"),
        IMG("f5com-channels.svg", alt="Four rows of boxes joined by arrows. A: producer to consumer. B: producer, retailer, consumer. C: producer, wholesaler, retailer, consumer. D: producer, agent, wholesaler, retailer, consumer.",
            caption="Figure 1. Four channels of distribution. The consumer is the end of every chain."),
        KEY("What each channel means", "From shortest to longest.", cards=[
            ["A: Producer to consumer", "Direct selling: a farmer at his stall, a tailor, a factory shop, or a firm selling online to the public."],
            ["B: Producer, retailer, consumer", "Large retailers such as supermarkets buy directly from the producer."],
            ["C: Producer, wholesaler, retailer, consumer", "The traditional channel for many consumer goods such as rice, soap and cooking oil."],
            ["D: Producer, agent, wholesaler, retailer, consumer", "An agent finds buyers, often for goods from distant or foreign producers."],
        ]),
        T("An **agent** arranges sales for a producer in return for a commission and does not usually own the goods. A **wholesaler** buys in bulk and sells to retailers. A **retailer** sells small quantities to consumers."),
        H("Choosing a channel"),
        T("A producer does not pick a channel by chance. These factors matter."),
        KEY("Factors that influence the choice of channel", "Think about the product, the market and the producer.", cards=[
            ["Nature of the product", "Perishable goods (fish, tomatoes) need short channels. Durable, standard goods can use long ones."],
            ["Value and technical nature", "Expensive or technical goods (machines) are often sold directly or through specialist agents."],
            ["Size and spread of the market", "Many scattered customers call for wholesalers and retailers; a few large customers allow direct sale."],
            ["Resources of the producer", "A small producer lacks vehicles and shops, so uses middlemen; a large firm may sell directly."],
            ["Need for service", "Goods needing demonstration or repair work better with specialist sellers."],
        ]),
        H("Should we cut out the middleman?"),
        T("People say that middlemen make goods dearer, so a shorter channel is cheaper. This is only partly true, because middlemen also do useful work: they store goods, break bulk, give credit and take risks."),
        EX("Worked example 1: price build-up", intro="Teaching figures (invented for practice) for a carton of soap. The factory sells to a wholesaler at FCFA 4 000. The wholesaler sells to a retailer at FCFA 5 000. The retailer sells to the consumer at FCFA 6 500. How much does each middleman add, and what is the total?", steps=[
            S("Wholesaler's addition", text="5 000 − 4 000 = FCFA 1 000."),
            S("Retailer's addition", text="6 500 − 5 000 = FCFA 1 500."),
            S("Total added by middlemen", text="1 000 + 1 500 = FCFA 2 500, which is 62.5% of the factory price."),
            S("Meaning", text="These additions pay for storage, transport, shop rent, wages and the middlemen's profit. They are not all pure profit."),
        ], check=r"1\,000 + 1\,500 = 2\,500"),
        EX("Worked example 2: direct selling compared", intro="The same factory opens a shop and sells the carton directly at FCFA 5 200 (invented for practice). Compare with the consumer price of FCFA 6 500 through the chain.", steps=[
            S("Saving for the consumer", text="6 500 − 5 200 = FCFA 1 300 cheaper."),
            S("Cost to the factory", text="It must now pay for shop rent, staff, delivery and the risk of unsold stock, which the middlemen used to bear."),
            S("Conclusion", text="Direct selling can lower the price but the work and risk do not disappear; they move to the producer."),
        ]),
        KEY("Cutting out middlemen: for and against", "A balanced answer gives both sides.", cards=[
            ["In favour", "Lower prices for consumers; producer keeps more profit; direct contact with customers; fresher goods."],
            ["Against", "Producer needs more capital, stores and transport; no bulk-breaking or credit; wider market is harder to reach; more risk."],
        ]),
        MISTAKE("Saying the longest channel is always the most expensive", "A long channel may be the only practical way to reach thousands of small shops across the country. Judge the channel by the product and the market, not only by the number of links."),
        MISTAKE("Forgetting that agents do not buy the goods", "An agent earns commission for arranging a sale. A wholesaler buys the goods and owns them. Do not mix these two in an answer."),
        QUIZ("A producer of fresh fish in Limbe wants the goods to reach buyers quickly. Which channel is most suitable?",
             ["Producer, agent, wholesaler, retailer, consumer", "A short channel such as producer to retailer or consumer", "A very long chain with storage at each stage", "Any channel; perishability does not matter"], 1,
             "Perishable goods spoil quickly, so they need the shortest practical route.",
             hint="What happens to fish that waits at every stage?",
             feedback=["That is the longest chain, which takes time.", "", "Storage at every stage is slow and costly for perishable goods.", "Perishability is a main factor in choosing a channel."]),
        QUIZ("Which person arranges sales for a producer for a commission and normally does not own the goods?",
             ["Wholesaler", "Retailer", "Agent", "Consumer"], 2,
             "An agent works for commission and does not usually buy the goods.",
             hint="Who is paid commission?",
             feedback=["A wholesaler buys the goods and owns them.", "A retailer buys and sells to consumers.", "", "The consumer is the final buyer."]),
        TIP("Exam link: channels of distribution are tested in Paper 1 (identify the channel, the middleman, the factors) and in Paper 2 essays on intermediaries of trade. Draw a small chain diagram in your answer if the question asks you to describe a channel."),
        PQ("Define a channel of distribution and describe the traditional channel for consumer goods.", "A channel of distribution is the route goods follow from producer to consumer. The traditional channel is producer to wholesaler to retailer to consumer."),
        PQ("State three factors that influence the choice of a channel of distribution.", "The nature of the product (perishable goods need short channels), the size and spread of the market, and the resources of the producer. Value and the need for after-sales service are also accepted."),
        PQ("Give two advantages and two disadvantages of cutting out middlemen.", "Advantages: possibly lower prices, and the producer keeps more profit. Disadvantages: the producer needs more capital, storage and transport, and he loses the wholesaler's bulk-breaking and credit."),
        SUM("A channel of distribution is the route from producer to consumer; middlemen include agents, wholesalers and retailers.",
            "There are four main channels, from direct selling to producer, agent, wholesaler, retailer, consumer.",
            "The choice depends on the product, the market and the producer's resources.",
            "Cutting out middlemen can lower prices but moves their work and risk to the producer."),
    ],
))

# ------------------------------------------------------------------ 5. Small-scale retailers
LESSONS.append(lesson(
    module=M2, topic="Small-scale retailers",
    title="Small-scale retailers: hawkers, stalls, shops and tied shops",
    slug="com-small-scale-retailers",
    minutes=20,
    summary="Small-scale retailers such as hawkers, market traders, kiosks and tied shops sell in small quantities close to consumers. They offer convenience and credit but have limited stock, high costs and weak buying power.",
    objectives=[
        "Define retailer and retail trade",
        "Describe hawkers, market stalls, general shops and tied shops",
        "State the services retailers give to consumers and to wholesalers",
        "Calculate a small retailer's gross profit and explain its advantages and disadvantages",
    ],
    key_concepts=["Retailer", "Hawker", "Market stall", "General shop", "Tied shop", "Gross profit"],
    blocks=[
        H("Introduction"),
        T("In most Cameroonian towns you can buy bread, matches and a phone top-up within two minutes' walk of your house. The person who sells to you in small quantities is a **retailer**. "
          "Millions of consumers depend on small-scale retailers, so this is an important part of home trade."),
        D("A **retailer** is a trader who buys goods from producers or wholesalers and sells them in small quantities to final consumers. **Retail trade** is the last link in the chain of distribution.", title="Definition: retailer"),
        H("Types of small-scale retailer"),
        KEY("Common small-scale retailers", "Know the main features of each.", cards=[
            ["Hawkers (itinerant traders)", "Carry or push goods, or sell from a bicycle, motorbike or van, going to customers on streets, in traffic or from house to house. No fixed place; low capital."],
            ["Market stalls and street traders", "Sell at a fixed spot in a market or at the roadside, often on market days. Many Cameroonian markets are famous for fresh food and clothing."],
            ["General shops, kiosks and boutiques", "Fixed, small shops that sell a wide range of everyday goods, such as sugar, rice, soap, drinks and phone credit, often open long hours and near homes."],
            ["Specialist shops", "Sell one type of goods, such as a pharmacy, a shoe shop or a bookshop, with knowledge of the goods."],
            ["Tied shops", "Shops that sell mainly or only the goods of one manufacturer, for example a filling station selling one company's fuel or a bar selling one brewer's drinks. The producer may give loans, equipment or better prices in return."],
        ]),
        T("Buyam-sellam is the popular Cameroonian word for trading in which a person buys goods cheaply, often in bulk, and sells them in small quantities at a profit. It fits the definition of retailing."),
        H("Services of retailers"),
        KEY("What retailers do", "Their services help both consumers and wholesalers.", cards=[
            ["To consumers", "Convenience and nearness; small quantities; credit; advice; home delivery; after-sales help."],
            ["To wholesalers and producers", "Sell goods to the public; hold stock; give market information about what customers want; promote goods."],
        ]),
        EX("Worked example 1: a market trader's gross profit", intro="Teaching figures (invented for practice). A trader buys 40 bunches of plantain at FCFA 1 500 each. She sells 36 bunches at FCFA 2 200 each; the other 4 rot and are thrown away. Find her gross profit.", steps=[
            S("Cost of the goods", text="40 × 1 500 = FCFA 60 000."),
            S("Sales revenue", text="36 × 2 200 = FCFA 79 200."),
            S("Gross profit", text="79 200 − 60 000 = FCFA 19 200. (The 4 rotten bunches are a loss that is already inside the cost of 60 000.)"),
        ], check=r"36 \times 2200 - 40 \times 1500 = 19\,200"),
        EX("Worked example 2: advantages and disadvantages for a boutique", intro="A boutique owner opens near a student hostel. Explain why this site suits a small-scale retailer and what weaknesses she faces.", steps=[
            S("Advantages", text="Nearness to customers; long opening hours; personal service; she knows each buyer and may give small credit; low running costs."),
            S("Disadvantages", text="Small stock and limited choice; she buys in small quantities so pays higher prices; little capital; weak bargaining power; no advertising budget; supermarkets may sell cheaper."),
            S("Conclusion", text="Convenience and credit keep customers loyal; weak buying power and limited capital make growth hard."),
        ]),
        KEY("Advantages and disadvantages of small-scale retailing", "Be ready with two of each.", cards=[
            ["Advantages", "Convenient location and hours; personal attention; credit to known customers; sell in small quantities; easy to start with little capital."],
            ["Disadvantages", "Limited choice; higher prices because bulk discounts are not available; small stocks run out; little capital; high risk of failure."],
        ]),
        MISTAKE("Calling a hawker a wholesaler because he buys in bulk", "What defines a retailer is who he sells to: final consumers in small quantities. A hawker may buy a whole carton, but he sells single items to the public."),
        MISTAKE("Saying a tied shop is owned by the producer", "A tied shop is usually owned by an independent trader who agrees to sell mainly one producer's goods in return for help. A shop owned by the producer would be a company shop or branch."),
        QUIZ("A trader who carries his goods from house to house and has no fixed place of business is called a:",
             ["Hawker", "Wholesaler", "Department store", "Tied shop"], 0,
             "A hawker is an itinerant retailer: no fixed premises, goes to the customers.",
             hint="He moves; the customers do not.",
             feedback=["", "A wholesaler sells in bulk to retailers.", "A department store is a large shop with many sections.", "A tied shop is a fixed shop selling one producer's goods."]),
        QUIZ("Which of the following is a disadvantage of small-scale retailing?",
             ["Personal service", "Convenient location", "Higher prices because of small purchases", "Long opening hours"], 2,
             "Buying in small amounts means no bulk discount, so costs and prices are higher.",
             hint="Three options are advantages.",
             feedback=["Personal service is an advantage.", "Location is an advantage.", "", "Long hours are an advantage."]),
        TIP("Exam link: small-scale retailers are examined in Paper 1 (identify the type) and in Paper 2 essays on intermediaries of trade. Always give the definition and one or two features for each type you name."),
        PQ("Define a retailer and name three types of small-scale retailer.", "A retailer buys goods from wholesalers or producers and sells them in small quantities to final consumers. Types: hawkers, market stalls, general shops (also kiosks and tied shops)."),
        PQ("Explain what is meant by a tied shop and give one benefit to the shopkeeper.", "A tied shop sells mainly the goods of one producer. The shopkeeper may receive loans, equipment such as a fridge, or lower prices from the producer."),
        PQ("A trader buys 50 packets of biscuits at FCFA 400 and sells all at FCFA 550 (invented for practice). Calculate her gross profit.", "Cost: 50 × 400 = FCFA 20 000. Sales: 50 × 550 = FCFA 27 500. Gross profit: 27 500 − 20 000 = FCFA 7 500."),
        SUM("A retailer sells small quantities to final consumers and is the last link in the chain.",
            "Main small-scale types: hawkers, market stalls, general shops and kiosks, specialist shops and tied shops.",
            "They give convenience, credit and personal service but have small stocks, high prices and little capital.",
            "Gross profit equals sales less the cost of the goods sold."),
    ],
))

# ------------------------------------------------------------------ 6. Large-scale retailers and e-commerce
LESSONS.append(lesson(
    module=M2, topic="Large-scale retailers and e-commerce",
    title="Large-scale retailers and e-commerce",
    slug="com-large-scale-retailers-ecommerce",
    minutes=22,
    summary="Large-scale retailers (department stores, supermarkets, chain stores, mail order) use bulk buying and wide choice to lower prices. E-commerce sells over the internet and phones, with mobile money payment and delivery.",
    objectives=[
        "Describe department stores, supermarkets, chain (multiple) stores, mail order and e-commerce",
        "State the advantages and disadvantages of each type",
        "Explain why large retailers can charge lower prices than small ones",
        "Compare large-scale and small-scale retailing",
    ],
    key_concepts=["Department store", "Supermarket", "Chain store", "Mail order", "E-commerce", "Loss leader"],
    blocks=[
        H("Introduction"),
        T("In Douala and Yaounde you find shops with trolleys, many shelves, cashiers and a car park. You may also order shoes on a phone app and pay with mobile money. "
          "These are **large-scale retailers**. They buy in great quantities, employ many workers and serve a large number of customers."),
        D("A **large-scale retailer** is a retail business with a big turnover, many customers and a wide range of goods, usually owned by a company.", title="Definition: large-scale retailer"),
        H("Main types"),
        KEY("Types of large-scale retailer", "Learn the main feature of each.", cards=[
            ["Department store", "A very large shop divided into departments (clothes, furniture, electronics, food), under one roof. Customers find many goods in one place."],
            ["Supermarket", "A large self-service shop selling mainly food and household goods. Customers take goods from shelves and pay at a checkout."],
            ["Chain (multiple) store", "A company that owns many shops in different towns that look alike and sell similar goods, with central buying and a common brand."],
            ["Mail-order business", "Customers choose from a catalogue or advertisement and the goods are sent by post or courier; payment may be by bank, card or mobile money."],
            ["E-commerce", "Buying and selling over the internet or by phone, using websites, apps and social media, with online payment and delivery."],
        ]),
        T("Some shops sell certain goods at a very low price, even at a loss, to attract customers who will then buy other goods. Such a product is a **loss leader**."),
        H("Why large retailers can sell cheaply"),
        T("They buy in huge quantities and receive big trade discounts. They spread fixed costs (rent, lighting, manager) over very large sales. Self-service saves wages. They may deal directly with producers, which cuts out the wholesaler. As a result they can reduce prices and still make profit."),
        KEY("Advantages to the customer", "These are the points examiners usually ask for.", cards=[
            ["Wide choice under one roof", "Department stores and supermarkets save time."],
            ["Lower prices", "Bulk buying, discounts and loss leaders."],
            ["Extra services", "Parking, restaurants, delivery, credit cards, sales and quality control."],
            ["Convenience", "Open long hours; mail order and e-commerce come to your home."],
        ]),
        KEY("Disadvantages", "Not all customers benefit equally.", cards=[
            ["Impersonal service", "Less personal attention and advice than a small shop."],
            ["Distance", "May be far from home, and not available in villages."],
            ["High running costs", "Staff, security, rent and advertising need heavy spending."],
            ["Risks of mail order and e-commerce", "Goods cannot be touched before buying; slow delivery; fraud; need for internet and a payment method; returns can be difficult."],
        ]),
        EX("Worked example 1: an online order", intro="Teaching figures (invented for practice). A student orders three items from an online shop: a school bag at FCFA 18 500, a calculator at FCFA 42 000 and a pair of socks at FCFA 9 500. Delivery costs FCFA 2 500. She pays by mobile money. What is the total payment?", steps=[
            S("Add the goods", text="18 500 + 42 000 + 9 500 = FCFA 70 000."),
            S("Add delivery", text="70 000 + 2 500 = FCFA 72 500."),
            S("Payment", text="She pays FCFA 72 500 (mobile money may add a small fee; check the current charges)."),
            S("Risks", text="She cannot test the calculator before paying, so she should check the seller's reputation and return policy."),
        ], check=r"18\,500 + 42\,000 + 9\,500 + 2\,500 = 72\,500"),
        EX("Worked example 2: shopping at a department store", intro="Mrs Ndeh needs a school uniform, a mattress and groceries for her family. Explain why a department store may suit her.", steps=[
            S("One place", text="All three kinds of goods can be bought on one visit, saving time and transport."),
            S("Prices and offers", text="The store may sell some goods cheaply as loss leaders and offer seasonal sales."),
            S("Services", text="Parking, trolleys, a restaurant, credit or card payment and delivery of the heavy mattress."),
            S("But", text="Prices of some goods may be higher than at a market stall, and service is less personal."),
        ]),
        KEY("Large-scale versus small-scale retailers", "A short comparison to remember.", cards=[
            ["Large-scale", "Wide choice, lower prices on many items, services, but impersonal, further away and needs big capital."],
            ["Small-scale", "Near homes, personal, credit, long hours, but narrow choice, higher prices, limited capital."],
        ]),
        MISTAKE("Mixing department stores with supermarkets", "A department store has many separate departments selling different kinds of goods (clothes, furniture, electrical goods). A supermarket is self-service, selling mainly food and household items. The Board's 2023 report shows only average marks on the advantages of a department store, so learn them clearly: shopping under one roof, free parking, loss leaders, extra services."),
        MISTAKE("Giving only one-word advantages", "'Cheap' alone earns little. Write 'Prices can be lower because the store buys in bulk and gets discounts, and it may sell loss leaders to attract customers'."),
        QUIZ("A very large shop with separate sections for clothes, furniture and electrical goods is a:",
             ["Supermarket", "Chain store", "Department store", "Tied shop"], 2,
             "A department store is divided into departments selling different kinds of goods.",
             hint="Look at the word 'sections' in the question.",
             feedback=["A supermarket sells mainly food on a self-service basis.", "A chain store is one of many identical shops owned by a company.", "", "A tied shop sells mainly one producer's goods."]),
        QUIZ("Which is a disadvantage of buying through e-commerce?",
             ["Goods are delivered to your home", "You can compare many sellers quickly", "You cannot touch or test the goods before buying", "You can shop at any hour"], 2,
             "A buyer cannot check the quality of the goods physically before paying.",
             hint="Three options are advantages.",
             feedback=["Home delivery is an advantage.", "Comparing sellers is an advantage.", "", "Shopping at any hour is an advantage."]),
        TIP("Exam link: large-scale retailing appears in Paper 1 (identify the type) and may be set as a Paper 2 essay on the advantages of shopping in a department store. Give several developed advantages."),
        PQ("List four advantages of shopping in a department store.", "Many goods under one roof; parking; prices that may be lower through loss leaders; extra services such as restaurants, delivery and credit."),
        PQ("Explain how a supermarket can charge lower prices than a small shop.", "It buys goods in large quantities and gets bulk discounts, spreads its fixed costs over high sales, and saves wages through self-service."),
        PQ("State two disadvantages of mail-order or online shopping.", "The buyer cannot see or test the goods before paying; delivery can be slow or goods may be lost; there is a risk of fraud and returns can be difficult."),
        SUM("Large-scale retailers buy in bulk, sell widely and usually belong to companies.",
            "Types: department store, supermarket, chain store, mail order and e-commerce.",
            "Customers gain choice, lower prices and services but lose personal service; online buyers cannot inspect goods.",
            "Loss leaders attract customers who buy other goods."),
    ],
))

# ------------------------------------------------------------------ 7. Functions of the wholesaler
LESSONS.append(lesson(
    module=M2, topic="Functions of the wholesaler",
    title="Functions of the wholesaler",
    slug="com-functions-of-the-wholesaler",
    minutes=20,
    summary="The wholesaler buys in bulk from producers and sells in smaller lots to retailers. He breaks bulk, stores goods, gives credit, delivers, advises and carries risk, serving both producers and retailers.",
    objectives=[
        "Define wholesaler and wholesale trade",
        "Explain the functions of a wholesaler to the retailer",
        "Explain the functions of a wholesaler to the producer",
        "Calculate a wholesaler's gross profit and explain why wholesalers can be bypassed",
    ],
    key_concepts=["Wholesaler", "Breaking bulk", "Storage", "Credit", "Risk-bearing", "Market information"],
    blocks=[
        H("Introduction"),
        T("A shopkeeper in Mokolo market does not drive to the factory each time she runs out of cooking oil. She buys a few cartons from a wholesaler in town, who has bought thousands of cartons from the producer. "
          "The wholesaler stands between producer and retailer and does work for both."),
        D("A **wholesaler** is a trader who buys goods in large quantities from producers and sells them in smaller quantities to retailers and other businesses, not normally to final consumers. **Wholesale trade** is this buying and selling in bulk.", title="Definition: wholesaler"),
        H("Functions to the retailer"),
        KEY("What the wholesaler does for the retailer", "This part was well answered by candidates in the Board's 2023 report; make sure you can give all of these.", cards=[
            ["Breaks bulk", "Sells in smaller quantities (a carton, a bag) so the retailer need not buy a whole lorry-load."],
            ["Provides a variety", "Offers goods from many producers in one place, saving the retailer time."],
            ["Gives credit", "Lets the retailer pay later, which helps one with little capital."],
            ["Stores goods", "The retailer needs little storage space and can order often."],
            ["Delivers", "Brings goods to the shop, saving transport costs."],
            ["Advice and information", "Tells the retailer about new goods, prices and demand."],
            ["Packs and grades goods", "May pack or sort goods into suitable sizes."],
        ]),
        H("Functions to the producer"),
        KEY("What the wholesaler does for the producer", "The producer benefits too.", cards=[
            ["Buys in bulk", "Producer sells large quantities and gets money quickly."],
            ["Stores goods", "Producer does not need large warehouses for finished goods."],
            ["Takes risks", "Bears the risk of price falls, damage, theft and unsold stock."],
            ["Finance", "Pays early, giving the producer working capital."],
            ["Market information", "Passes on what retailers and customers want."],
            ["Reaches many retailers", "Saves the producer from dealing with hundreds of small shops."],
        ]),
        EX("Worked example 1: wholesaler's gross profit", intro="Teaching figures (invented for practice). A wholesaler in Douala buys 100 cartons of tomato paste at FCFA 7 500 a carton and sells them all to retailers at FCFA 9 000 a carton. Find the gross profit, the mark-up on cost and the margin on sales.", steps=[
            S("Cost", text="100 × 7 500 = FCFA 750 000."),
            S("Sales", text="100 × 9 000 = FCFA 900 000."),
            S("Gross profit", text="900 000 − 750 000 = FCFA 150 000."),
            S("Mark-up on cost", text="150 000 ÷ 750 000 × 100 = 20%."),
            S("Margin on sales", text="150 000 ÷ 900 000 × 100 = 16.7% (to 1 decimal place)."),
        ], check=r"\frac{150\,000}{750\,000} \times 100 = 20"),
        EX("Worked example 2: breaking bulk for the retailer", intro="A retailer buys one carton of 24 tins from the wholesaler for FCFA 9 000 and sells the tins singly at FCFA 500 each (invented for practice). What is her gross profit per carton?", steps=[
            S("Sales per carton", text="24 × 500 = FCFA 12 000."),
            S("Cost", text="FCFA 9 000."),
            S("Gross profit", text="12 000 − 9 000 = FCFA 3 000 per carton."),
            S("Meaning", text="The wholesaler allowed her to buy one carton, not a whole lorry-load, and gave her a price she could resell at a profit."),
        ], check=r"24 \times 500 - 9\,000 = 3\,000"),
        H("Can the wholesaler be cut out?"),
        T("Large retailers such as supermarkets and chain stores often buy directly from producers. Producers with their own shops or websites also sell directly. Wholesalers still survive where there are many small retailers, "
          "poor roads and a need for credit, because they do jobs that individual producers and retailers cannot do cheaply."),
        MISTAKE("Listing the functions without explaining the benefit", "Do not write only 'storage'. Write 'storage: the retailer needs less space and can order little and often'. Marks go for the explanation."),
        MISTAKE("Mixing the wholesaler's services to the retailer with those to the producer", "Read the question: 'to the retailer' means credit, breaking bulk, delivery and variety. 'To the producer' means bulk purchase, storage, risk and finance. Examiners saw good marks on the retailer part, so do not lose them by drifting into the other."),
        QUIZ("When a wholesaler sells one carton from a lorry-load, he is:",
             ["Giving credit", "Breaking bulk", "Bearing risk", "Advertising"], 1,
             "Dividing large lots into smaller quantities for retailers is breaking bulk.",
             hint="The word 'bulk' means large quantity.",
             feedback=["Credit is allowing payment later.", "", "Risk-bearing is accepting possible losses from price falls or damage.", "Advertising is promoting goods."]),
        QUIZ("A function of the wholesaler to the producer is:",
             ["Selling to final consumers", "Giving credit to consumers", "Buying in bulk and storing the goods", "Producing the goods"], 2,
             "The wholesaler buys large quantities and stores them, helping the producer's cash flow and space.",
             hint="Which option helps the producer, not the retailer or consumer?",
             feedback=["Wholesalers sell to retailers, not mainly to final consumers.", "Credit is given to retailers, not consumers.", "", "Production is the producer's job."]),
        TIP("Exam link: the wholesaler's functions are a favourite essay part (the Board's report notes the part on functions to the retailer was well answered) and appear in Paper 1. Give five functions with a brief benefit for each."),
        PQ("Define a wholesaler and explain four of his functions to the retailer.", "A wholesaler buys in bulk and sells in smaller quantities to retailers. He breaks bulk, offers a variety of goods, gives credit so the retailer needs less capital, stores goods and delivers them."),
        PQ("Explain two services the wholesaler provides to the manufacturer.", "He buys in large quantities, giving quick payment, and stores the goods, saving the producer storage cost; he also takes the risk of unsold goods and passes on market information."),
        PQ("A wholesaler buys 200 sacks of rice at FCFA 20 000 and sells them at FCFA 24 000 each (invented for practice). Calculate his gross profit.", "Cost: 200 × 20 000 = 4 000 000. Sales: 200 × 24 000 = 4 800 000. Gross profit = FCFA 800 000."),
        SUM("A wholesaler buys in bulk and sells in smaller lots to retailers and other businesses.",
            "To retailers he breaks bulk, gives credit, stores, delivers, offers variety and advises.",
            "To producers he buys in bulk, stores, bears risk, finances and passes on information.",
            "Large retailers may cut him out, but small retailers still need him."),
    ],
))

# ------------------------------------------------------------------ 8. Commercial documents
LESSONS.append(lesson(
    module=M2, topic="Commercial documents",
    title="Commercial documents in home trade",
    slug="com-commercial-documents",
    minutes=25,
    summary="Buyer and seller exchange documents: letter of inquiry, quotation, order, delivery note, invoice, debit and credit notes, and statement of account. Each has a sender, a purpose and a place in the order of events.",
    objectives=[
        "Name the commercial documents in order and say who sends each",
        "State the purpose of the letter of inquiry, quotation, order, delivery note and invoice",
        "Explain when a debit note and a credit note are issued",
        "Read an invoice, a credit note and a statement of account and check the figures",
    ],
    key_concepts=["Letter of inquiry", "Quotation", "Order", "Delivery note", "Invoice", "Debit note", "Credit note", "Statement of account", "Catalogue"],
    blocks=[
        H("Introduction"),
        T("When Ngum Stores in Bamenda wants cartons of soap from a wholesaler in Douala, the two firms cannot rely on talk alone. They need written proof of what was asked, offered, ordered, delivered and owed. "
          "These written papers are **commercial documents**. They avoid disputes and are the base of the accounting records."),
        D("**Commercial documents** are written records that pass between buyer and seller during a sale. They show the details of the deal: goods, quantity, price, delivery and payment.", title="Definition: commercial documents"),
        H("The order of events"),
        IMG("f5com-documents.svg", alt="Eight boxes in order: 1 letter of inquiry from the buyer, 2 quotation from the seller, 3 order from the buyer, 4 delivery note from the seller, 5 invoice from the seller, 6 credit note if needed, 7 statement of account, 8 payment by the buyer.",
            caption="Figure 1. Documents in a home-trade sale. Blue boxes come from the buyer, green boxes from the seller."),
        KEY("The documents and who sends them", "Learn the sender and the purpose of each.", cards=[
            ["Catalogue / price list", "From the seller: lists goods, descriptions and prices so buyers can choose. It is sent before any inquiry, often to many buyers."],
            ["Letter of inquiry", "From the buyer: asks the seller for prices, terms and delivery for stated goods."],
            ["Quotation (estimate)", "From the seller: replies with prices, discounts, delivery and payment terms. It states the offer but is not yet a sale."],
            ["Order", "From the buyer: a firm request for stated goods at the quoted price. It forms a contract once the seller accepts."],
            ["Delivery note", "From the seller, with the goods: lists what is delivered. The buyer checks it and signs a copy."],
            ["Invoice", "From the seller: the bill. Shows goods, quantity, prices, discounts and the amount to pay."],
            ["Debit note", "From the seller: charges the buyer extra when the invoice was too low (undercharge)."],
            ["Credit note", "From the seller: reduces the buyer's debt for returned, damaged or overcharged goods."],
            ["Statement of account", "From the seller, usually monthly: summary of invoices, notes and payments, showing the balance due."],
            ["Receipt", "From the seller: proof that payment was received."],
        ]),
        H("An invoice"),
        T("The invoice is the document most often tested. Read the following invoice (all names and figures are invented for practice). Work out where the net amount comes from."),
        CODE("INVOICE No. 0417            Date: 12 March (invented)\n"
             "From: Mbeki Wholesale, Douala\n"
             "To:   Ngum Stores, Bamenda        Order No. 88\n"
             "\n"
             "Qty Description              Unit price     Amount\n"
             "--------------------------------------------------\n"
             "20  Bags of rice                 24 000    480 000\n"
             "10  Cartons tomato paste          9 500     95 000\n"
             "15  Cartons of soap               6 000     90 000\n"
             "--------------------------------------------------\n"
             "Total at list price                        665 000\n"
             "Less trade discount 10%                     66 500\n"
             "Net amount payable                         598 500\n"
             "Terms: net 30 days.  Errors and omissions excepted.", "text", title="Invoice (FCFA)"),
        EX("Worked example 1: check the invoice", intro="Verify the figures on invoice 0417.", steps=[
            S("Each line", text="20 × 24 000 = 480 000; 10 × 9 500 = 95 000; 15 × 6 000 = 90 000."),
            S("Total at list price", text="480 000 + 95 000 + 90 000 = FCFA 665 000."),
            S("Trade discount", text="10% of 665 000 = FCFA 66 500."),
            S("Net amount", text="665 000 − 66 500 = FCFA 598 500."),
        ], check=r"665\,000 - 66\,500 = 598\,500"),
        H("Credit note, debit note and statement"),
        T("Two cartons of soap were damaged on delivery. The wholesaler issues a **credit note**, a document that reduces what the buyer owes. The credit includes the trade discount, because the buyer was only charged the discounted price."),
        CODE("CREDIT NOTE No. 0051         Date: 15 March (invented)\n"
             "To: Ngum Stores, Bamenda\n"
             "Reason: 2 cartons of soap damaged on delivery\n"
             "\n"
             "Qty Description              Unit price     Amount\n"
             "--------------------------------------------------\n"
             "2   Cartons of soap               6 000     12 000\n"
             "Less trade discount 10%                      1 200\n"
             "Credit allowed                              10 800", "text", title="Credit note (FCFA)"),
        T("A day later the wholesaler finds that one carton of soap was delivered but left off the invoice. It sends a **debit note** charging the buyer the extra amount: 1 carton at 6 000 less 10% = FCFA 5 400. "
          "At the month end it sends a **statement of account**, a summary of all the transactions, so that the buyer knows how much to pay."),
        CODE("STATEMENT OF ACCOUNT: Ngum Stores, Bamenda\n"
             "From: Mbeki Wholesale, Douala   Month: March (invented)\n"
             "\n"
             "Date    Details                  Debit    Credit    Balance\n"
             "-----------------------------------------------------------\n"
             "1 Mar   Balance b/f            150 000              150 000\n"
             "12 Mar  Invoice 0417           598 500              748 500\n"
             "15 Mar  Credit note 0051                  10 800    737 700\n"
             "16 Mar  Debit note 0009          5 400              743 100\n"
             "20 Mar  Payment received                 150 000    593 100\n"
             "-----------------------------------------------------------\n"
             "Amount now due                                      593 100", "text", title="Statement of account (FCFA)"),
        EX("Worked example 2: check the statement", intro="Follow the balance down the statement.", steps=[
            S("Start", text="Balance brought forward: FCFA 150 000 owed by the buyer."),
            S("Debits increase the debt", text="150 000 + 598 500 = 748 500."),
            S("Credit note decreases it", text="748 500 − 10 800 = 737 700."),
            S("Debit note increases it", text="737 700 + 5 400 = 743 100."),
            S("Payment decreases it", text="743 100 − 150 000 = FCFA 593 100 now due."),
        ], check=r"150\,000 + 598\,500 - 10\,800 + 5\,400 - 150\,000 = 593\,100"),
        MISTAKE("Mixing up debit and credit notes", "A credit note reduces the buyer's debt (returns, damage, overcharge). A debit note increases it (undercharge). In the Board's 2023 report, explanations of the catalogue, the invoice and the credit note were below the expected standard, so learn the purpose and the sender of each."),
        MISTAKE("Confusing the quotation with the order, or the invoice with the receipt", "A quotation is the seller's offer. An order is the buyer's request. An invoice asks for payment; a receipt is proof that payment was made."),
        QUIZ("Which document does a seller send to tell a buyer how much to pay for goods sold?",
             ["Delivery note", "Quotation", "Invoice", "Order"], 2,
             "The invoice is the bill, giving quantities, prices, discount and the amount payable.",
             hint="Which one is the bill?",
             feedback=["A delivery note lists the goods delivered, not the price to pay.", "A quotation is an offer made before the sale.", "", "An order is sent by the buyer."]),
        QUIZ("A buyer returns damaged goods. The seller sends a:",
             ["Debit note", "Credit note", "Quotation", "Catalogue"], 1,
             "A credit note reduces the amount owed by the buyer.",
             hint="Does the buyer owe more or less after the return?",
             feedback=["A debit note increases the amount owed.", "", "A quotation is a price offer.", "A catalogue is a list of goods and prices."]),
        TIP("Exam link: commercial documents appear in Paper 1 (match the document with its purpose or sender) and in Paper 2 essays on buying and selling operations, which may ask you to explain three documents such as the catalogue, invoice and credit note. For each give: who sends it, to whom, and why."),
        PQ("State two documents the buyer sends and two the seller sends in a home-trade transaction.", "Buyer: letter of inquiry and order. Seller: quotation, delivery note, invoice, credit note or statement (any two)."),
        PQ("Explain what an invoice is and list five items of information it shows.", "An invoice is the seller's bill. It shows the seller's and buyer's names, date and invoice number, description, quantity and price of goods, discounts, and the net amount to pay with the terms of payment."),
        PQ("Explain when a credit note is issued, with an example.", "A credit note is issued when the seller reduces the buyer's debt, for example when the buyer returns damaged goods, receives the wrong goods or was overcharged on the invoice."),
        PQ("A buyer owes FCFA 300 000 at the start of the month, is invoiced FCFA 450 000, is given a credit note for FCFA 20 000 and pays FCFA 300 000. What does the statement show as owing? (invented for practice)", "300 000 + 450 000 − 20 000 − 300 000 = FCFA 430 000."),
        SUM("Commercial documents are the written record of a sale; they follow an order from inquiry to payment.",
            "Buyer sends the letter of inquiry and the order. Seller sends the quotation, delivery note, invoice, notes and statement.",
            "A credit note reduces what the buyer owes; a debit note increases it.",
            "The statement of account summarises the transactions and shows the balance due."),
    ],
))

# ------------------------------------------------------------------ 9. Trade discount and cash discount
LESSONS.append(lesson(
    module=M2, topic="Trade discount and cash discount",
    title="Trade discount and cash discount: calculations",
    slug="com-trade-and-cash-discount",
    minutes=22,
    summary="Trade discount is a reduction from the list price given to a business buyer and is taken off first. Cash discount is a reduction on the net amount for prompt payment and is lost if payment is late.",
    objectives=[
        "Define trade discount and cash discount and explain the difference",
        "Calculate net invoice amounts after trade discount",
        "Calculate the amount payable after cash discount, in the correct order",
        "Explain who gains from each kind of discount and decide whether a buyer has qualified",
    ],
    key_concepts=["List price", "Trade discount", "Net amount", "Cash discount", "Settlement period"],
    blocks=[
        H("Introduction"),
        T("A wholesaler's price list says a carton of cooking oil costs FCFA 15 000. A shop owner who buys many cartons does not pay that much. The wholesaler gives a discount. "
          "If she also pays within ten days, she may get a second, smaller discount. In Commerce these two reductions have different names and are worked out in a fixed order."),
        D("**List price** (catalogue price) is the price shown in the seller's catalogue or price list before any discount.", title="Definition: list price"),
        D("**Trade discount** is a reduction from the list price given by a wholesaler or manufacturer to a business buyer (a retailer). It is allowed whether or not the buyer pays quickly, and it is shown on the invoice.", title="Definition: trade discount"),
        D("**Cash discount** is a reduction allowed to a buyer for paying within a stated time, or in cash. It is taken off the net amount after trade discount, and the buyer loses it if he pays late.", title="Definition: cash discount"),
        KEY("Trade discount and cash discount compared", "A frequent examination contrast.", cards=[
            ["Why given", "Trade: to reward the business buyer's status or large orders, so the retailer can make a profit. Cash: to encourage quick payment."],
            ["When", "Trade: on the invoice, always. Cash: only if payment is made in time."],
            ["Taken from", "Trade: the list price. Cash: the net amount after trade discount."],
            ["Appears", "Trade: shown on the invoice. Cash: stated in the terms; recorded when payment is made."],
            ["Who gains", "Trade: the retailer gets lower cost. Cash: the seller gets money sooner and the buyer saves money."],
        ]),
        H("The calculation order"),
        CODE("List price\n"
             "- trade discount (% of list price)\n"
             "= Net amount (invoice total)\n"
             "- cash discount (% of net amount, only if paid in time)\n"
             "= Amount paid", "text", title="Order of working"),
        EX("Worked example 1: both discounts", intro="Teaching figures (invented for practice). A retailer orders 10 sacks of rice at FCFA 28 000 and 5 cartons of cooking oil at FCFA 15 000. The wholesaler allows a 20% trade discount and a 4% cash discount for payment within 10 days. She pays on day 8. How much does she pay?", steps=[
            S("Goods at list price", text="10 × 28 000 = 280 000; 5 × 15 000 = 75 000; total FCFA 355 000."),
            S("Trade discount", text="20% of 355 000 = FCFA 71 000."),
            S("Net amount", text="355 000 − 71 000 = FCFA 284 000."),
            S("Cash discount", text="4% of 284 000 = FCFA 11 360 (she paid within 10 days, so she qualifies)."),
            S("Amount paid", text="284 000 − 11 360 = FCFA 272 640."),
        ], check=r"355\,000 \times 0.80 \times 0.96 = 272\,640"),
        EX("Worked example 2: payment too late", intro="Another buyer owes a net amount of FCFA 135 000 after trade discount. The terms are 2.5% cash discount for payment within 14 days. He pays on day 20. How much does he pay, and how much did he lose by being late? (invented for practice)", steps=[
            S("Is he in time?", text="Day 20 is after day 14, so he does not qualify for the cash discount."),
            S("Amount paid", text="FCFA 135 000."),
            S("What he lost", text="2.5% of 135 000 = FCFA 3 375 would have been saved had he paid by day 14."),
        ], check=r"135\,000 \times 0.025 = 3\,375"),
        EX("Worked example 3: when only trade discount applies", intro="A list price of FCFA 150 000 carries a trade discount of 10% and a cash discount of 2.5% for prompt payment. Find the net amount and the amount paid if payment is on time. (invented for practice)", steps=[
            S("Trade discount", text="10% of 150 000 = 15 000."),
            S("Net amount", text="150 000 − 15 000 = FCFA 135 000."),
            S("Cash discount", text="2.5% of 135 000 = FCFA 3 375."),
            S("Paid", text="135 000 − 3 375 = FCFA 131 625."),
        ], check=r"150\,000 \times 0.90 \times 0.975 = 131\,625"),
        T("Notice the cash discount is smaller than 2.5% of the list price. It is 2.5% of the net amount only. Buyers who pay early still gain, but not as much as a careless calculation suggests."),
        MISTAKE("Calculating cash discount on the list price", "Cash discount is worked on the net amount after trade discount, not on the list price. In the example above, 2.5% of 150 000 would give 3 750, which is wrong; the correct figure is 3 375."),
        MISTAKE("Adding the two percentages together", "Trade discount 20% plus cash discount 4% does not equal 24% of the list price. The two are applied one after the other, each on a different base."),
        QUIZ("A list price is FCFA 80 000 and the trade discount is 15%. What is the net amount?",
             ["FCFA 12 000", "FCFA 68 000", "FCFA 92 000", "FCFA 65 000"], 1,
             "15% of 80 000 = 12 000. Net amount = 80 000 − 12 000 = FCFA 68 000.",
             hint="First find the discount, then subtract.",
             feedback=["That is the discount, not the net amount.", "", "You added the discount instead of subtracting it.", "This subtracts 15 000, which is not 15% of 80 000."]),
        QUIZ("Which statement about cash discount is correct?",
             ["It is always given with the trade discount", "It is lost if the buyer pays after the stated time", "It is calculated on the list price", "It is given only to wholesalers"], 1,
             "Cash discount rewards prompt payment, so late payment loses it.",
             hint="What does the buyer have to do to earn it?",
             feedback=["Only buyers who pay in time get it.", "", "It is worked on the net amount after trade discount.", "Any buyer paying in time can be allowed it."]),
        TIP("Exam link: discount calculations appear in Paper 1 and in Paper 2 data-response parts. Show the order clearly: list price, trade discount, net amount, cash discount, amount paid. Marks are given for method."),
        PQ("Distinguish between trade discount and cash discount.", "Trade discount is a deduction from the list price given to a business buyer regardless of when he pays. Cash discount is a deduction from the net amount given for prompt payment."),
        PQ("Goods have a list price of FCFA 200 000. Trade discount is 25%. Calculate the net amount. (invented for practice)", "25% of 200 000 = 50 000. Net amount = 200 000 − 50 000 = FCFA 150 000."),
        PQ("A net invoice total is FCFA 150 000 with 4% cash discount for payment within 7 days. What is paid if the buyer pays on day 5? (invented for practice)", "4% of 150 000 = 6 000. Paid = 150 000 − 6 000 = FCFA 144 000."),
        PQ("Explain why a seller offers a cash discount.", "It encourages buyers to pay quickly. The seller receives cash sooner, which improves cash flow, reduces bad debts and can be used to buy more stock."),
        SUM("List price less trade discount gives the net amount; cash discount is then taken off the net amount.",
            "Trade discount is always allowed to the business buyer; cash discount is lost if payment is late.",
            "Always apply the discounts one after another, never add the percentages.",
            "Show each step in an examination; the method earns marks."),
    ],
))
