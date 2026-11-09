"""Form 5 Commerce: Foreign / International Trade and Business Units & Commercial Finance (12 lessons, one practice set each).

All money figures in worked examples and exercises are invented for practice.
"""

from .dsl import *  # noqa: F403

COURSE = ("commerce", "form-5")

M3 = "Foreign / International Trade"
M4 = "Business Units & Commercial Finance"

LESSONS = []

# ------------------------------------------------------------------ 1. Reasons for international trade
LESSONS.append(lesson(
    module=M3,
    topic="Reasons for international trade",
    title="Why countries trade with one another",
    slug="com2-reasons-for-international-trade",
    minutes=18,
    summary="Why countries import and export: unequal natural resources, different skills and technology, specialisation, variety and larger markets, and the factors that made foreign trade grow.",
    objectives=[
        "Define international (foreign) trade, imports and exports",
        "Explain why countries trade, using differences in natural endowment, skills and technology",
        "Explain how specialisation and better transport and communication increase foreign trade",
        "Plan a short answer on the factors that led to the growth of foreign trade",
    ],
    key_concepts=["International trade", "Import", "Export", "Natural endowment", "Specialisation"],
    blocks=[
        H("Introduction"),
        T("Look at what is on your table at home. The rice may come from Asia, the cooking oil from a local palm, the phone from China and the cocoa in your chocolate from Cameroon. "
          "No country makes everything it needs. So countries sell what they have in plenty and buy what they lack. This is **international trade**."),
        D("**International trade** (also called foreign trade) is the buying and selling of goods and services between people or firms in different countries.", title="Definition: international trade"),
        KEY("Imports and exports", "Always say which direction the goods travel, from the point of view of one country.", cards=[
            ["Export", "A good or service sold to another country. Cameroon exports cocoa, timber and crude oil, for example."],
            ["Import", "A good or service bought from another country. Cameroon imports vehicles, machinery and some foodstuffs, for example."],
        ]),
        T("Trade inside one country, such as a trader in Bafoussam selling to a shop in Yaounde, is **home trade**. Foreign trade is more complicated: different currencies, laws, languages, customs checks and long journeys by sea or air."),
        H("Reason 1: Differences in natural endowment"),
        D("**Natural endowment** means the natural resources a country has: climate, soil, minerals, forests, rivers and sea.", title="Definition: natural endowment"),
        T("Climate and soil decide what crops grow. Cameroon's warm, wet climate suits cocoa, coffee, bananas and rubber, but wheat grows badly here, so wheat is imported. "
          "A cold country cannot grow cocoa at all, so it must import it. The same is true of minerals: a country without oil must buy oil from one that has it."),
        H("Reason 2: Differences in skills and technology"),
        T("Some countries have many skilled engineers and advanced factories. They make computers, aircraft and medicines cheaply and well. "
          "Other countries have more land or labour than machines. Each buys what it cannot make easily and sells what it makes well."),
        H("Reason 3: Specialisation and cost"),
        D("**Specialisation** means a country (or firm or person) concentrating on the goods it can produce best and at the lowest cost, then trading for the rest.", title="Definition: specialisation"),
        T("If Country A makes cocoa cheaply and Country B makes machinery cheaply, both gain when A sells cocoa to B and B sells machines to A. Each uses its resources where they are most productive, and total output rises. "
          "Specialisation also lets a factory produce on a large scale, which lowers the cost of each unit."),
        EX("Worked example 1: A simple gain from trade (invented figures)", intro="In one month Country A can make either 60 tonnes of cocoa or 30 machines. Country B can make either 20 tonnes of cocoa or 40 machines. Which country should specialise in what?", steps=[
            S("Compare what each country gives up", text="For A: 60 tonnes of cocoa = 30 machines, so 1 machine costs 2 tonnes of cocoa. For B: 40 machines = 20 tonnes of cocoa, so 1 machine costs half a tonne of cocoa."),
            S("Find the cheaper producer of each good", math=r"\text{Machine cost: A} = 2 \text{ t cocoa};\quad \text{B} = 0.5 \text{ t cocoa}", text="B gives up less cocoa to make a machine, so B is the cheaper machine maker. A gives up less machinery to make cocoa, so A is the cheaper cocoa grower."),
            S("Conclude", text="A should specialise in cocoa and B in machines, then they should trade. Both can end with more of both goods than if each made some of everything."),
        ]),
        H("Other reasons"),
        KEY("More reasons countries trade", "Examiners accept any well explained reason. Learn at least five.", cards=[
            ["Variety and choice", "Consumers enjoy goods that are not made at home, such as foreign cars, fabrics and foods."],
            ["Larger markets", "Selling abroad lets firms produce more, lower their unit costs and earn foreign currency."],
            ["Shortage and surplus", "A country sells the surplus it cannot use and buys goods that are in short supply."],
            ["Political and cultural links", "Friendly relations, trade agreements and shared languages make trade easier."],
            ["Raw materials and capital goods", "Factories need imported machines and raw materials to run."],
        ]),
        H("Why foreign trade has grown"),
        T("Foreign trade today is far larger than a hundred years ago. The main reasons are improved transport (large ships, containers, aircraft), better communication (telephone, internet, mobile money, e-mail), "
          "advances in technology and banking, trade agreements that lower taxes, and growing populations with more money to spend."),
        TIP("The Board's 2023 report says a question on the factors that led to the growth of foreign trade was very well answered, with most scripts scoring above average. Good answers named differences in natural endowment, "
            "better transport and communication, and better technology, and explained each in a sentence or two.", title="Exam link"),
        MISTAKE("Listing without explaining", "Writing only 'climate, transport, technology' earns little. Add one sentence to each reason, for example: 'Cameroon has a climate suited to cocoa, so it exports cocoa and imports wheat it cannot grow.'"),
        MISTAKE("Mixing up import and export", "Imports come INTO your country; exports go OUT. When Cameroon sells timber to Italy, it is an export for Cameroon and an import for Italy."),
        QUIZ("Which is the best example of a difference in natural endowment leading to trade?", [
            "A country with no oil buys oil from a country that has oil fields",
            "A shop offers a discount to customers who buy in bulk",
            "A government prints more banknotes",
            "A company opens a second branch in the same town",
        ], 0, "Natural endowment means natural resources. A country lacking oil must import it from one that has it.",
            hint="Which choice is about a natural resource that one country has and another lacks?",
            feedback=["", "A discount is a pricing method inside one market, not a reason for countries to trade.", "Printing money is a government monetary action and has nothing to do with natural resources.", "Opening a second branch is home trade expansion, not trade between countries."]),
        QUIZ("Country A can make cloth more cheaply than Country B, and B can make bicycles more cheaply than A. What should they do to gain most?", [
            "Each make both goods for itself",
            "A makes cloth, B makes bicycles, and they trade",
            "A makes bicycles and B makes cloth",
            "Neither should trade",
        ], 1, "Each country should specialise in the good it makes at lower cost and then trade. Both gain more total output.",
            hint="Think of specialisation: each country does what it does best.",
            feedback=["Making everything alone wastes the advantage each country has.", "", "This is the reverse of what lowers cost: each would produce its more expensive good.", "Without trade each country goes without the good it makes poorly and loses the gain from specialisation."]),
        PQ("Define international trade and give two examples of goods that Cameroon exports and two that it imports.", "International trade is the buying and selling of goods and services between people or firms in different countries. Cameroon exports, for example, cocoa and timber. It imports, for example, machinery and vehicles."),
        PQ("Explain two reasons why countries trade with one another.", "1. Differences in natural endowment: no country has every resource, so a country with oil sells it to one without, and buys goods such as wheat that its own climate cannot grow. 2. Specialisation: each country produces what it makes best and cheapest and trades for the rest, so total output and choice rise."),
        PQ("State three factors that have led to the growth of foreign trade and say how each helps.", "Improved transport (ships, containers, aircraft) moves goods faster, more safely and more cheaply. Improved communication (telephone, internet, mobile money) lets buyers and sellers contact each other and pay quickly. Improved technology produces more goods and better packing and storage, so more can be sold abroad."),
        SUM("International trade is the buying and selling of goods and services between countries; exports go out and imports come in.",
            "Countries trade because of differences in natural endowment, skills and technology.",
            "Specialisation lets each country produce what it makes at the lowest cost, and trade then gives both more.",
            "Variety, larger markets, surplus disposal and political links are further reasons.",
            "Foreign trade has grown because of better transport, communication, technology and trade agreements."),
    ],
))

# ------------------------------------------------------------------ 2. Visible and invisible trade
LESSONS.append(lesson(
    module=M3,
    topic="Visible and invisible trade",
    title="Visible and invisible trade",
    slug="com2-visible-and-invisible-trade",
    minutes=18,
    summary="The difference between visible trade (goods you can touch) and invisible trade (services), with examples of each, plus entrepot and transit trade.",
    objectives=[
        "Define visible trade and invisible trade",
        "Classify items as visible or invisible exports and imports",
        "Explain why invisible trade matters to a country's earnings",
        "Define entrepot trade and transit trade",
    ],
    key_concepts=["Visible trade", "Invisible trade", "Invisible exports and imports", "Entrepot trade", "Transit trade"],
    blocks=[
        H("Introduction"),
        T("A cocoa farmer in Mbalmayo sells beans to an exporter. The beans are loaded on a ship at Douala and seen by customs officers. That is trade you can see. "
          "Now think of a tourist from Europe who stays in a hotel in Kribi, or a Cameroonian who pays a foreign firm for insurance. Nothing physical crosses a border, but money still moves between countries. "
          "Commerce calls the first kind **visible** and the second kind **invisible** trade."),
        D("**Visible trade** is the buying and selling of tangible goods between countries. The goods can be seen, touched and counted at the port or border.", title="Definition: visible trade"),
        D("**Invisible trade** is the buying and selling of services between countries. Nothing physical is passed over a border, so customs officers do not count it as goods.", title="Definition: invisible trade"),
        KEY("Examples", "A country has both visible and invisible exports and imports.", cards=[
            ["Visible exports", "Cocoa, coffee, timber, bananas and crude oil sold abroad."],
            ["Visible imports", "Vehicles, machinery, rice, fuel and mobile phones bought from abroad."],
            ["Invisible exports", "Foreign tourists spending in Cameroon hotels; a Cameroonian bank or airline serving a foreign customer; foreigners using Cameroon's port services."],
            ["Invisible imports", "Cameroon firms paying foreign shipping lines, insurers, banks, consultants and software providers."],
        ]),
        T("The key test: **does money come in or go out for the service?** If a foreigner pays a service provider in your country, that is an invisible export, because your country earns foreign money. If your country pays a foreign provider, it is an invisible import."),
        H("Main kinds of invisible trade"),
        T("Shipping and air transport carry goods and passengers. Banking and insurance help traders pay and protect goods. Tourism brings visitors who spend money. "
          "Communication, education and professional services (such as engineering advice) are also sold across borders. "
          "Many textbooks also list money sent home by workers abroad (remittances) and interest and profits sent abroad as invisible items. Check how your textbook groups them."),
        EX("Worked example 1: Classify each item", intro="Say whether each is a visible export, visible import, invisible export or invisible import for Cameroon: (a) timber sold to Spain, (b) a Cameroonian trader buying a lorry from abroad, (c) a French tourist paying a Limbe hotel, (d) a Douala firm paying a foreign shipping company.", steps=[
            S("(a) Timber is a good that leaves", text="Visible export."),
            S("(b) The lorry is a good that comes in", text="Visible import."),
            S("(c) A foreigner pays for a service in Cameroon", text="Invisible export. Cameroon earns foreign money from a service."),
            S("(d) Cameroon pays a foreigner for a service", text="Invisible import. Money goes out for transport service."),
        ]),
        H("Why invisible trade matters"),
        T("Services earn foreign currency without needing a ship to carry anything. A country with a strong port, good hotels, an airline or a strong banking sector can earn a lot from invisible exports. "
          "Cameroon's beaches, mountains, wildlife parks and cities attract tourists; a well-run Douala port also earns money by serving ships and transit cargo."),
        H("Entrepot and transit trade"),
        D("**Entrepot trade** (re-export trade) is when a country imports goods and then exports them again, often after storing, sorting, packing or finishing them, without using them at home.", title="Definition: entrepot trade"),
        D("**Transit trade** is trade in goods that pass through a country on the way from one country to another. The goods are not sold in the country they pass through.", title="Definition: transit trade"),
        T("Transit trade matters to Cameroon: the port of Douala handles goods for landlocked neighbours such as Chad and the Central African Republic. The goods are not for sale in Cameroon, but Cameroon earns money from port, transport and storage services."),
        TIP("In a table of figures, goods are visible and services are invisible. When a service pays Cameroon, it adds to exports; when Cameroon pays, it adds to imports.", title="Quick rule"),
        MISTAKE("Calling money 'invisible trade'", "Invisible trade means services, not money itself. Say 'a hotel service sold to a tourist', not 'the money'."),
        MISTAKE("Thinking invisible means illegal or hidden", "Invisible trade is perfectly legal. It is called invisible only because no goods are carried across the border."),
        QUIZ("Which of these is an invisible export for Cameroon?", [
            "Cocoa beans sold to a foreign chocolate factory",
            "A foreign visitor paying a Kribi hotel",
            "A Cameroon importer buying cars from Japan",
            "Rice bought from abroad",
        ], 1, "A hotel stay is a service sold to a foreigner who pays Cameroon, so it is an invisible export.",
            hint="Services, not goods, and foreign money coming in.",
            feedback=["Cocoa beans are goods, so this is a visible export.", "", "Cars are goods and they come in, so a visible import.", "Rice is a good and it comes in, so a visible import."]),
        QUIZ("Goods arrive at Douala from Europe and are sent on by truck to N'Djamena without being sold in Cameroon. What is this trade called?", [
            "Home trade",
            "Entrepot trade",
            "Transit trade",
            "Barter",
        ], 2, "Goods passing through a country on their way to another are transit trade. In entrepot trade the goods are re-exported by the importing country.",
            hint="Are the goods only passing through, or bought and re-sold by Cameroon?",
            feedback=["Home trade is between buyers and sellers inside one country.", "Entrepot trade means the country imports the goods and then re-exports them, often after some work. Here the goods only pass through.", "", "Barter is exchange of goods without money, not a name for goods in transit."]),
        PQ("Define visible trade and invisible trade, with one example of each.", "Visible trade is trade in tangible goods between countries, for example cocoa exported to another country. Invisible trade is trade in services between countries, for example a foreign tourist paying a hotel in Cameroon."),
        PQ("State three examples of invisible trade.", "Any three of: shipping and air transport, banking, insurance, tourism, communication services, professional or consulting services, education sold to foreign students."),
        PQ("Distinguish between entrepot trade and transit trade.", "In entrepot trade a country imports goods and then re-exports them, often after storing, packing or finishing them. In transit trade the goods only pass through the country on their way to another country and are never sold there. Douala handling cargo for Chad is an example of transit."),
        SUM("Visible trade is trade in goods; invisible trade is trade in services.",
            "Money coming into a country for a service is an invisible export; money going out is an invisible import.",
            "Tourism, shipping, banking, insurance and communication are common invisible items.",
            "Entrepot trade is import then re-export; transit trade is passing through a country to another.",
            "Invisible trade earns foreign money without carrying goods across a border."),
    ],
))

# ------------------------------------------------------------------ 3. Balance of trade and balance of payments
LESSONS.append(lesson(
    module=M3,
    topic="Balance of trade and balance of payments",
    title="Balance of trade and balance of payments",
    slug="com2-balance-of-trade-and-balance-of-payments",
    minutes=22,
    summary="How to calculate the balance of trade and the current account balance, the meaning of surplus and deficit, what the balance of payments includes, and ways to correct a deficit.",
    objectives=[
        "Calculate the balance of trade from the value of visible exports and imports",
        "Distinguish a favourable (surplus) from an unfavourable (deficit) balance",
        "Explain how the balance of payments differs from the balance of trade",
        "Suggest ways to correct a deficit",
    ],
    key_concepts=["Balance of trade", "Favourable and unfavourable balance", "Balance of payments", "Current account", "Capital account"],
    blocks=[
        H("Introduction"),
        T("Think of your family money for one month. You count what came in and what you spent. A country does the same with the rest of the world. "
          "If a country earns more from selling abroad than it pays for buying abroad, it is better off; if not, it must borrow or use savings. Two records tell the story: the **balance of trade** and the **balance of payments**."),
        D("The **balance of trade** is the difference between the value of a country's visible exports and the value of its visible imports over a period, usually a year.", title="Definition: balance of trade",
          formula=r"\text{Balance of trade} = \text{value of visible exports} - \text{value of visible imports}"),
        KEY("Surplus and deficit", "Compare exports with imports.", cards=[
            ["Favourable (surplus)", "Visible exports are greater than visible imports. The answer is positive."],
            ["Unfavourable (deficit)", "Visible imports are greater than visible exports. The answer is negative."],
            ["Balanced", "Exports equal imports. The balance is zero."],
        ]),
        T("Note: the words 'favourable' and 'unfavourable' are the traditional exam terms. A deficit is not always bad, for example when a country buys machines that help it produce more later. But a large deficit over many years can be a problem."),
        H("Balance of payments"),
        D("The **balance of payments** is a record of all the money coming into a country and all the money going out of it, for goods, services and capital movements, over a period.", title="Definition: balance of payments"),
        IMG("f5com2-balance-of-payments.svg",
            alt="Tree showing the balance of payments split into the current account, with visible trade and invisible trade, and the capital account",
            caption="Figure 1. The balance of payments. The balance of trade is only the visible part of the current account. Figures are invented for practice."),
        T("The **current account** records payments for visible trade (goods) and invisible trade (services and transfers). The **capital account** records loans, investments and aid moving in and out. "
          "The balance of trade covers only the visible part; the balance of payments covers everything."),
        F(r"\text{Current account balance} = \text{balance of trade} + \text{invisible balance}", title="Current account"),
        EX("Worked example 1: Balance of trade (invented figures, millions of FCFA)", intro="A country had visible exports of 480 and visible imports of 520. Find the balance of trade and say whether it is favourable.", steps=[
            S("Write the formula", math=r"\text{Balance of trade} = \text{exports} - \text{imports}"),
            S("Substitute", math=r"480 - 520 = -40"),
            S("State the result", text="The balance of trade is -40 million FCFA, a deficit. It is unfavourable because imports exceeded exports."),
        ]),
        EX("Worked example 2: Current account (same country, invented figures)", intro="Invisible exports were 150 and invisible imports were 90. Find the invisible balance and the current account balance.", steps=[
            S("Invisible balance", math=r"150 - 90 = +60"),
            S("Add the balance of trade", math=r"\text{Current account} = -40 + 60 = +20"),
            S("Interpret", text="Strong services earnings (tourism, transport) turn a trade deficit of 40 into a current account surplus of 20 million FCFA."),
        ], check=r"(480 + 150) - (520 + 90) = 630 - 610 = 20"),
        H("Correcting a deficit"),
        T("A government worried about a lasting deficit can try to increase exports (help exporters, improve quality and transport), reduce imports (taxes called tariffs, limits called quotas), "
          "and encourage people to buy local goods. It can also promote tourism and invisible earnings. "
          "Restricting imports can raise prices and cause other countries to answer in the same way, so it has costs."),
        TIP("Exam questions often give a list of exports and imports and ask for the balance of trade or the current account. Add the correct columns, show the formula and state 'surplus' or 'deficit' in words.", title="Exam link"),
        MISTAKE("Including services in the balance of trade", "The balance of trade counts visible goods only. Services belong in the invisible balance, which is added to give the current account."),
        MISTAKE("Subtracting the wrong way round", "Always exports minus imports. If you reverse it, a deficit looks like a surplus."),
        QUIZ("Visible exports are 350 and visible imports are 410 (millions of FCFA, invented). What is the balance of trade?", [
            "+60", "-60", "+760", "-760",
        ], 1, "Balance of trade = exports minus imports = 350 - 410 = -60, a deficit.",
            hint="Subtract imports from exports and keep the sign.",
            feedback=["The numbers are right but the sign is wrong: imports are larger, so the balance is negative.", "", "You added the two values. A balance is a difference, not a total.", "You added them and then gave a negative sign. A balance is a difference."]),
        QUIZ("Which statement correctly describes the balance of payments?", [
            "It records only visible exports and imports",
            "It records all money flowing into and out of a country, including services and capital",
            "It records government spending at home",
            "It is the same as the national budget",
        ], 1, "The balance of payments covers goods, services and capital movements between a country and the rest of the world.",
            hint="Which choice includes more than just goods?",
            feedback=["That describes the balance of trade, which is only one part.", "", "Spending at home is not trade with other countries.", "The national budget is about government income and spending, not dealings with the rest of the world."]),
        PQ("A country exported goods worth 900 and imported goods worth 750 (millions of FCFA, invented). Calculate the balance of trade and state whether it is favourable.", "Balance of trade = 900 - 750 = +150 million FCFA. It is a surplus, so it is favourable."),
        PQ("Distinguish between the balance of trade and the balance of payments.", "The balance of trade is the difference between the value of visible exports and visible imports only. The balance of payments is the full record of money coming in and going out for goods, services and capital movements, so it also includes invisible trade and loans and investments."),
        PQ("Give three ways a government can reduce a balance of trade deficit.", "Any three of: encourage and support exports; reduce imports with tariffs or quotas; encourage people to buy locally made goods; promote tourism and other invisible earnings; improve the quality and price of local goods."),
        SUM("Balance of trade = visible exports minus visible imports; surplus is favourable and deficit is unfavourable.",
            "The balance of payments records all money flows with other countries: goods, services and capital.",
            "Current account balance = balance of trade + invisible balance.",
            "A deficit can be reduced by raising exports, cutting imports and promoting tourism and services.",
            "Show the formula, the working and a word conclusion in calculation questions."),
    ],
))

# ------------------------------------------------------------------ 4. Import and export documents
LESSONS.append(lesson(
    module=M3,
    topic="Import and export documents",
    title="Import and export documents",
    slug="com2-import-and-export-documents",
    minutes=22,
    summary="The documents used when goods cross a border: bill of lading, airway bill, certificate of origin, consular invoice, commercial invoice and packing list, what each does and who uses it.",
    objectives=[
        "Name the main documents used in export and import trade",
        "State the purpose of the bill of lading, airway bill, certificate of origin and consular invoice",
        "Distinguish a bill of lading from an airway bill",
        "Follow the order of documents in a simple export transaction",
    ],
    key_concepts=["Bill of lading", "Airway bill", "Certificate of origin", "Consular invoice", "Commercial invoice"],
    blocks=[
        H("Introduction"),
        T("A trader in Douala wants to send 200 bags of cocoa to a buyer abroad. The buyer cannot see the goods, the shipping company must know what it is carrying, customs must know what leaves and what enters, "
          "and the bank wants proof before it pays. Each party relies on a **document**. Trade across borders is a paper (or electronic) trail."),
        D("**Export and import documents** are written or electronic records that describe the goods, the sale, the transport and the countries involved, so that buyers, sellers, carriers, banks and customs can do their work.", title="Definition: trade documents"),
        H("Documents that describe the sale"),
        KEY("Commercial invoice and packing list", "These come from the seller.", cards=[
            ["Commercial invoice", "The seller's bill to the buyer. It shows the goods, quantity, price, terms of sale (such as FOB or CIF) and total amount. Customs also use it to value the goods."],
            ["Packing list", "Shows what is in each package, with weights and sizes, so that the contents can be checked on arrival."],
        ]),
        H("Documents for transport"),
        D("A **bill of lading (B/L)** is a document issued by a shipping company (the carrier) to the exporter. It is a receipt for goods loaded, evidence of the contract to carry them, and a document of title, so whoever holds the proper original can claim the goods at the destination port.", title="Definition: bill of lading"),
        D("An **airway bill** is the transport document used when goods travel by air. It is a receipt for the goods and evidence of the contract of carriage, but it is not a document of title: the goods go to the named receiver (consignee).", title="Definition: airway bill"),
        CODE(
            "BILL OF LADING  (invented, simplified, for practice)\n"
            "--------------------------------------------------\n"
            "Shipper    : Ngono Cocoa Export, Douala\n"
            "Consignee  : To order of the buyer's bank\n"
            "Vessel     : MV Example                  Voyage 12\n"
            "Port of loading   : Douala\n"
            "Port of discharge : Rotterdam\n"
            "Goods      : 200 bags raw cocoa beans, 64 kg each\n"
            "Gross weight      : 12 800 kg\n"
            "Freight    : prepaid\n"
            "Remarks    : Shipped on board, goods in good order\n"
            "Date of issue     : 14 March\n"
            "Signed for the Carrier : ______________",
            "text", title="A simplified bill of lading",
            caption="Check: 200 bags x 64 kg = 12 800 kg. Real forms have more boxes, and the details are invented for practice."),
        T("A bill of lading marked **clean** says the goods were received in good order. A **claused** (or 'foul') bill of lading records damage or a shortage. Banks usually refuse to pay against a claused bill, so exporters try to get a clean one."),
        H("Documents about origin"),
        D("A **certificate of origin** is a document saying in which country the goods were produced or made. It is issued by an authorised body, often a chamber of commerce, and is used by customs to decide whether special tariff treatment or a ban applies.", title="Definition: certificate of origin"),
        D("A **consular invoice** is an invoice for the imported goods that has been certified by the consul (a government official) of the importing country, working in the exporting country. Some importing countries require it to check the value and origin. Not every country uses it, so check your textbook.", title="Definition: consular invoice"),
        H("Other documents"),
        T("An **insurance certificate or policy** shows that the goods are insured in transit (especially when the sale is on CIF terms). A **customs declaration** is the form completed for customs to show what is entering or leaving. "
          "A **bill of exchange** may be used to arrange payment. Your syllabus focuses on the bill of lading, airway bill, certificate of origin and consular invoice."),
        CODE(
            "Simple export of cocoa by sea\n"
            "1. Buyer and seller agree the sale (order, proforma or invoice)\n"
            "2. Seller packs the goods; packing list prepared\n"
            "3. Goods are taken to the port; customs declaration made\n"
            "4. Goods loaded; carrier issues the BILL OF LADING\n"
            "5. Seller sends invoice, B/L, certificate of origin,\n"
            "   insurance certificate to buyer (or buyer's bank)\n"
            "6. Buyer pays, collects the B/L, clears customs at destination\n"
            "   and takes delivery of the goods",
            "text", title="Steps in a sea export"),
        EX("Worked example 1: Choose the document", intro="Which document would you use in each case? (a) An importer must prove that goods were made in a particular country. (b) A shipping company needs to give the exporter a receipt for goods loaded on a ship. (c) A courier company carries samples by air to a buyer.", steps=[
            S("(a) Proof of country of production", text="Certificate of origin."),
            S("(b) Receipt for goods loaded on a ship", text="Bill of lading, which is also the document of title."),
            S("(c) Goods carried by air", text="Airway bill. It names the receiver and is not a document of title."),
        ]),
        TIP("Examiners like short, exact statements: 'A bill of lading is a receipt for goods shipped, evidence of the contract of carriage and a document of title.' Learn that sentence.", title="Exam link"),
        MISTAKE("Using a bill of lading for air freight", "Bill of lading is for sea transport. For air transport the document is the airway bill."),
        MISTAKE("Confusing an invoice with a certificate of origin", "An invoice is a bill for payment. A certificate of origin only says where the goods were produced."),
        QUIZ("Which document is a receipt for goods loaded on a ship and a document of title?", [
            "Airway bill", "Certificate of origin", "Bill of lading", "Packing list",
        ], 2, "The bill of lading is issued by the carrier, is a receipt for goods shipped and acts as a document of title.",
            hint="Which one is used for sea transport and gives the holder the right to claim the goods?",
            feedback=["The airway bill is used for air transport and is not a document of title.", "It only shows the country of production.", "", "It lists package contents but is not issued by the carrier as title to the goods."]),
        QUIZ("What does a clean bill of lading mean?", [
            "The goods were washed before loading",
            "The goods were received in good order and condition",
            "The carrier is not responsible for the goods",
            "The goods have been paid for",
        ], 1, "A clean bill of lading carries no remark about damage or shortage; the goods were received in good order.",
            hint="Think of what the carrier writes about the goods.",
            feedback=["'Clean' describes the carrier's remarks, not washing.", "", "A bill of lading does not remove the carrier's responsibility.", "A bill of lading says nothing about payment."]),
        PQ("State three functions of a bill of lading.", "It is a receipt for goods received on board; it is evidence of the contract of carriage between shipper and carrier; and it is a document of title, so the holder of the proper original can claim the goods at the destination."),
        PQ("Distinguish between a bill of lading and an airway bill.", "A bill of lading is used for goods carried by sea and is a document of title. An airway bill is used for goods carried by air; it is a receipt and evidence of the contract but is not a document of title, and the goods are delivered to the named consignee."),
        PQ("What is a certificate of origin and why might an importing country ask for one?", "It is a document stating the country in which the goods were produced, usually issued by an authorised body such as a chamber of commerce. The importing country's customs may use it to apply the correct duty, to give special tariff treatment to goods from certain countries, or to refuse goods from a banned source."),
        SUM("Trade documents let buyers, sellers, carriers, banks and customs do their work.",
            "The commercial invoice is the seller's bill; the packing list shows what is in each package.",
            "The bill of lading is for sea freight: receipt, evidence of contract and document of title.",
            "The airway bill is for air freight and is not a document of title.",
            "The certificate of origin states where goods were produced; the consular invoice is an invoice certified by the importing country's consul."),
    ],
))

# ------------------------------------------------------------------ 5. Incoterms, customs and excise duties
LESSONS.append(lesson(
    module=M3,
    topic="Incoterms, customs and excise duties",
    title="Incoterms, customs duty and excise duty",
    slug="com2-incoterms-customs-and-excise-duties",
    minutes=22,
    summary="The trade terms FOB, CIF, FAS and franco and who pays for what, the difference between customs duty and excise duty, why governments charge them, and a simple duty calculation.",
    objectives=[
        "Explain the terms FOB, FAS, CIF and franco",
        "Calculate the CIF value from the FOB price, freight and insurance",
        "Distinguish customs duty from excise duty",
        "State reasons why governments charge customs duties",
    ],
    key_concepts=["Incoterms", "FOB", "CIF", "FAS", "Franco", "Customs duty", "Excise duty"],
    blocks=[
        H("Introduction"),
        T("A seller in Douala quotes a price of FCFA 800 000 for a consignment of timber. Does that price include the cost of loading it on the ship? The sea freight? Insurance? Unless the quote says so, buyer and seller may disagree. "
          "To avoid arguments, traders use short **trade terms** that say who pays for what and where the risk passes."),
        D("**Incoterms** (International Commercial Terms) are standard trade terms published by the International Chamber of Commerce. They state the duties of buyer and seller: who arranges transport, who pays costs and where the risk of loss passes.", title="Definition: Incoterms"),
        T("Versions of the rules change over time and school textbooks often simplify them. What follows is the usual O Level meaning. Check your textbook for its wording."),
        IMG("f5com2-incoterms-cost.svg",
            alt="Route from seller's premises to buyer's premises with bars showing how far the seller pays the cost under FAS, FOB and CIF",
            caption="Figure 1. How far the seller pays under three sea-freight terms."),
        KEY("The four terms", "All three Incoterms below are for sea (and inland waterway) transport. Franco is a general trade term.", cards=[
            ["FAS (Free Alongside Ship)", "The seller pays until the goods are placed alongside the ship at the port of shipment. The buyer pays for loading and everything after."],
            ["FOB (Free On Board)", "The seller pays until the goods are loaded on board the ship at the port of shipment. The buyer pays the sea freight, insurance and later costs. Risk passes to the buyer once the goods are on board."],
            ["CIF (Cost, Insurance and Freight)", "The seller pays the cost of the goods, insurance and sea freight to the destination port. Note that risk of loss still passes to the buyer when the goods are on board at the port of shipment."],
            ["Franco", "'Free' or carriage-paid delivery: the price includes delivery to the buyer's place, so the seller pays transport costs to that place."],
        ]),
        T("Franco is not one of the formal sea-freight Incoterms. Textbooks use it for a price that includes delivery to the buyer's door or named place. Check your textbook's definition."),
        EX("Worked example 1: Find the CIF value (invented figures)", intro="A Douala exporter sells timber at an FOB price of FCFA 800 000. Sea freight to the buyer's port is FCFA 120 000 and insurance is FCFA 20 000. Find the CIF price.", steps=[
            S("Write the relationship", math=r"\text{CIF} = \text{FOB} + \text{freight} + \text{insurance}"),
            S("Substitute", math=r"800\,000 + 120\,000 + 20\,000 = 940\,000"),
            S("State the result", text="The CIF price is FCFA 940 000. The buyer pays the same total either way, but under CIF the seller arranges the freight and insurance."),
        ]),
        H("Customs duty and excise duty"),
        D("**Customs duty** is a tax charged on goods when they are imported into a country (and sometimes when exported). It is collected by the Customs service at ports, airports and borders.", title="Definition: customs duty"),
        D("**Excise duty** is a tax charged on certain goods made and sold inside a country, such as alcoholic drinks, tobacco and fuel. It is collected from the producer, who includes it in the price.", title="Definition: excise duty"),
        KEY("Why governments charge customs duties", "Know three or more reasons.", cards=[
            ["Revenue", "Duties give the government income to pay for services."],
            ["Protection", "Taxing imports makes them dearer, so local products are more competitive."],
            ["Restrict harmful goods", "High duty discourages goods such as tobacco."],
            ["Balance of payments", "Duties can reduce imports and so help a deficit."],
        ]),
        T("Duty may be **ad valorem** (a percentage of the goods' value) or **specific** (a fixed sum per unit, kilogram or litre). Rates differ by product and change, so this lesson uses invented rates only. Check the current rates with Cameroon Customs."),
        EX("Worked example 2: Ad valorem duty (invented rate)", intro="For this exercise, customs duty is charged at 10% of the CIF value (an invented rate for practice). Find the duty on the timber in Example 1.", steps=[
            S("Take the value for duty", math=r"\text{CIF} = 940\,000"),
            S("Calculate 10%", math=r"\frac{10}{100} \times 940\,000 = 94\,000"),
            S("State the answer", text="The duty is FCFA 94 000, so the importer's cost before other charges is 940 000 + 94 000 = FCFA 1 034 000."),
        ], check=r"940\,000 + 94\,000 = 1\,034\,000"),
        TIP("In many countries customs value is based on the CIF value of imported goods. Use the value given in the question and say so in your working.", title="Exam link"),
        MISTAKE("Adding duty to FOB instead of CIF", "In questions, work out the value for duty as the question states. If it says duty on CIF, you must add freight and insurance first."),
        MISTAKE("Confusing customs duty with excise duty", "Customs duty is on goods entering the country. Excise duty is on selected goods made inside the country."),
        QUIZ("Under FOB terms, who pays the sea freight?", [
            "The seller", "The buyer", "The customs officer", "The port authority",
        ], 1, "Under FOB the seller pays only up to loading on the ship. The buyer pays the sea freight and insurance.",
            hint="FOB ends at the ship: who pays after that?",
            feedback=["Under CIF the seller pays freight, not FOB.", "", "Customs collects duty. It does not pay freight.", "The port authority charges for port services; it does not pay freight."]),
        QUIZ("Which tax is charged on locally manufactured drinks and tobacco?", [
            "Customs duty", "Excise duty", "Freight", "Insurance premium",
        ], 1, "Excise duty is a tax on certain goods produced and sold inside the country.",
            hint="Think of goods made inside the country.",
            feedback=["Customs duty is charged on imports.", "", "Freight is the cost of carrying goods, not a tax.", "A premium is paid to an insurer, not to the government."]),
        PQ("Explain the terms FOB and CIF.", "FOB (free on board): the seller pays all costs until the goods are loaded on board the ship at the port of shipment; the buyer pays sea freight and insurance. CIF (cost, insurance and freight): the price includes the cost of the goods, insurance and freight to the destination port."),
        PQ("An exporter's FOB price is FCFA 500 000. Freight is FCFA 60 000 and insurance FCFA 10 000. Calculate the CIF price.", "CIF = FOB + freight + insurance = 500 000 + 60 000 + 10 000 = FCFA 570 000."),
        PQ("State three reasons why a government charges customs duties on imports.", "To earn revenue for the government; to protect local industries from cheaper foreign goods; to discourage imports of harmful or luxury goods; or to help reduce a balance of payments deficit. (Any three.)"),
        SUM("Incoterms are standard trade terms that say who pays for what and where risk passes.",
            "FAS: seller pays to alongside the ship. FOB: to loaded on board. CIF: cost, insurance and freight to destination; the buyer's risk begins on board.",
            "Franco means a delivered price to the buyer's named place; check your textbook's wording.",
            "CIF = FOB + freight + insurance.",
            "Customs duty is a tax on imports; excise duty is a tax on certain goods made inside the country."),
    ],
))

# ------------------------------------------------------------------ 6. Ports and port authorities
LESSONS.append(lesson(
    module=M3,
    topic="Ports and port authorities",
    title="Ports and port authorities: Douala and Kribi",
    slug="com2-ports-and-port-authorities",
    minutes=18,
    summary="What a seaport is, what port authorities do, the roles of the ports of Douala and Kribi, transit trade to neighbouring countries and the main causes of delays and costs at ports.",
    objectives=[
        "Define a port and state the services a port provides",
        "Describe the role of a port authority",
        "State the importance of the ports of Douala and Kribi to Cameroon",
        "Explain port transit trade and common causes of congestion",
    ],
    key_concepts=["Port", "Port authority", "Douala", "Kribi", "Transit trade", "Congestion"],
    blocks=[
        H("Introduction"),
        T("Most of Cameroon's foreign trade in goods travels by sea. A ship from Europe or Asia must have a safe place to stop, cranes to unload, stores to keep goods and roads or rail to carry them inland. That place is a **port**."),
        D("A **port** is a place on the coast (or a river) where ships load and unload goods and passengers. It has berths, cranes, storage and links to road and rail.", title="Definition: port"),
        D("A **port authority** is the public body that owns, runs or regulates a port. It provides and maintains the facilities and sets and collects port charges.", title="Definition: port authority"),
        IMG("f5com2-port-flow.svg",
            alt="Five-step flow showing a ship berthing, goods unloaded, customs checks, storage and onward transport by road or rail",
            caption="Figure 1. A simplified path for imported goods through a port (schematic, not a map)."),
        H("What a port provides"),
        KEY("Port services", "A port offers more than a place to tie up.", cards=[
            ["For ships", "Channels, pilots, tugs, berths and lighting; fuel and repair."],
            ["For cargo", "Cranes and equipment for loading and unloading; container yards; warehouses and cold stores."],
            ["For trade", "Customs and inspection offices, banks, shipping agents and clearing agents (who prepare documents and clear goods)."],
            ["Links", "Roads and rail that connect the port with towns and neighbouring countries."],
        ]),
        T("A port authority runs these services, keeps channels dredged (cleared of mud and sand), keeps the port secure and works with customs and other agencies. Port users pay charges such as port dues and handling fees. Customs duty, however, is collected by Customs, not by the port authority."),
        H("The ports of Douala and Kribi"),
        D("**Douala** is Cameroon's largest seaport and main commercial city. It lies on the Wouri estuary. The port is run by the Port Authority of Douala. It handles most of the country's sea trade and also goods in transit for neighbouring Chad and the Central African Republic.", title="The port of Douala"),
        T("Because Douala lies up an estuary, big ships can be limited by the depth of the channel, and the channel must be dredged regularly. The city is crowded and the port can become congested."),
        D("**Kribi** is a deep-sea port on the Atlantic coast in the South Region. It was built to take larger ships than Douala can. The Port Authority of Kribi runs it. It began operating in the late 2010s and serves industrial and export projects. Check the current facilities and traffic.", title="The port of Kribi"),
        T("Together the two ports give Cameroon a second route to the sea. Kribi can ease pressure on Douala and take large vessels, while Douala remains the main general-cargo port for now. Other smaller ports and river terminals exist; check your textbook for those it names."),
        H("Transit trade and delays"),
        T("Chad and the Central African Republic have no coast. Goods bound for them arrive at Douala and travel on by road or rail. This **transit trade** earns Cameroon income from port, transport and storage services. "
          "Delays at ports, caused by slow clearance, too many trucks, missing documents, poor roads or too few cranes, raise costs for traders and ultimately for consumers."),
        TIP("Link the port to what you have learnt: a ship carries a bill of lading, goods are cleared by customs, duty is paid, and the port authority charges for its services. Questions may ask you to explain any one link.", title="Exam link"),
        MISTAKE("Saying the port authority collects customs duty", "Customs duty is collected by the Customs service. The port authority earns port dues and handling charges."),
        MISTAKE("Saying Douala and Kribi are the same place", "They are two separate ports run by two port authorities. Douala is the long-established main port; Kribi is the newer deep-sea port."),
        QUIZ("Which body runs and maintains the facilities of a seaport?", [
            "The port authority", "The chamber of commerce", "The consular office", "The insurance company",
        ], 0, "The port authority provides and maintains the port's facilities and sets port charges.",
            hint="Which body has the word 'port' in its name?",
            feedback=["", "A chamber of commerce supports businesses but does not run ports.", "A consular office deals with documents and citizens abroad.", "An insurer covers risks but does not run the port."]),
        QUIZ("Why is Douala important to Chad and the Central African Republic?", [
            "They have no sea coast, so some of their imports pass through Douala",
            "Douala makes all the goods they need",
            "Douala is the capital of both countries",
            "They pay no charges at Douala",
        ], 0, "As landlocked countries, they depend on a neighbour's port. Goods in transit through Douala earn Cameroon income.",
            hint="What do the two countries lack that Douala provides?",
            feedback=["", "A port handles goods; it does not make them all.", "Yaounde is Cameroon's capital; Douala is not the capital of any of them.", "Transit goods still pay for port services and transport."]),
        PQ("Define a port and a port authority.", "A port is a place where ships load and unload goods and passengers, with berths, cranes, storage and transport links. A port authority is the public body that owns, runs or regulates the port, provides the facilities and collects port charges."),
        PQ("State four services provided by a seaport.", "Any four of: berths and cranes for loading and unloading; storage in warehouses and container yards; pilot and tug services; customs and inspection offices; shipping and clearing agents; links to road and rail."),
        PQ("Explain why Cameroon developed the deep-sea port at Kribi.", "Douala lies up an estuary and cannot easily take the largest ships, and its channel needs dredging and the port is congested. Kribi is a deep-sea port on the coast that can take bigger vessels, give Cameroon a second route to the sea, ease pressure on Douala and support industrial and export projects."),
        SUM("A port is where ships load and unload; a port authority runs its facilities and charges port dues.",
            "Ports offer berths, cranes, storage, customs offices and road or rail links.",
            "Douala is the main, long-established port; Kribi is the newer deep-sea port.",
            "Douala handles transit goods for Chad and the Central African Republic.",
            "Slow clearance, congestion and poor links raise costs; Customs, not the port authority, collects customs duty."),
    ],
))

# ------------------------------------------------------------------ 7. Sole traders and partnerships
LESSONS.append(lesson(
    module=M4,
    topic="Sole traders and partnerships",
    title="Sole traders and partnerships",
    slug="com2-sole-traders-and-partnerships",
    minutes=20,
    summary="The features, advantages and disadvantages of sole traders and partnerships, the partnership deed, unlimited liability, and how partners share profit.",
    objectives=[
        "Describe a sole trader and a partnership",
        "State advantages and disadvantages of each",
        "Explain unlimited liability and the purpose of a partnership deed",
        "Share a partnership's profit using interest on capital and a profit-sharing ratio",
    ],
    key_concepts=["Sole trader", "Partnership", "Unlimited liability", "Partnership deed", "Sleeping partner", "Unincorporated business"],
    blocks=[
        H("Introduction"),
        T("In every market in Cameroon you see a tailor, a provision-shop owner or a mobile-money agent working for themselves. Others start a business with a friend or a sister. "
          "These are the oldest and most common forms of business ownership. They are called **unincorporated** because the business has no separate legal existence from its owners."),
        D("A **sole trader** (one-man business) is a business owned, financed and usually run by one person, who keeps all the profit and bears all the risk.", title="Definition: sole trader"),
        KEY("Sole trader: advantages and disadvantages", "These are the points the Board's 2023 report lists for a sole trader.", cards=[
            ["Advantages", "Easy and cheap to start; the owner makes decisions quickly; keeps all profit; close contact with customers; flexible to change; few legal formalities; business affairs kept private."],
            ["Disadvantages", "Unlimited liability; limited capital and borrowing; the business may end if the owner falls ill or dies (no continuity); all the work and decisions rest on one person; hard to expand."],
        ]),
        D("**Unlimited liability** means the owner is personally responsible for all the debts of the business. If the business cannot pay, creditors can claim the owner's personal property, such as a house or car.", title="Definition: unlimited liability"),
        H("Partnerships"),
        D("A **partnership** is a business owned by two or more people who agree to share the capital, the work, the profits and the losses. Textbooks give the usual number as between two and twenty partners; check the current legal limits in your textbook.", title="Definition: partnership"),
        T("Partners usually sign a **partnership deed** (agreement). It says how much capital each puts in, how profits and losses are shared, whether partners get salaries or interest on capital, who does what and what happens if a partner leaves. "
          "Without a deed, disputes are harder to settle. Under OHADA's company law, the general partnership and limited partnership have their own rules; this level only needs the main ideas."),
        KEY("Types of partner", "", cards=[
            ["Active partner", "Puts in money and also takes part in running the business."],
            ["Sleeping (dormant) partner", "Puts in money but does not take part in management. Shares profit."],
            ["Limited partner", "Where the law allows it, liability is limited to the money put in; at least one partner must still have unlimited liability."],
        ]),
        KEY("Partnership: advantages and disadvantages", "", cards=[
            ["Advantages", "More capital than a sole trader; shared skills and workload; shared risk; easier to borrow; decisions discussed."],
            ["Disadvantages", "Unlimited liability (usually for all general partners); disagreements; slow decisions; one partner's mistake can bind all; profit is shared; the partnership may end if a partner leaves or dies."],
        ]),
        EX("Worked example 1: Sharing partnership profit (invented figures)", intro="Abena and Biyik are partners. Their capitals are FCFA 4 000 000 and FCFA 2 000 000. The deed gives 5% yearly interest on capital and shares the remaining profit in the ratio 3 : 2. Net profit for the year is FCFA 1 500 000. How much does each partner receive?", steps=[
            S("Interest on capital", math=r"\text{Abena: } 5\% \times 4\,000\,000 = 200\,000;\quad \text{Biyik: } 5\% \times 2\,000\,000 = 100\,000", text="Total interest = 300 000."),
            S("Profit left to share", math=r"1\,500\,000 - 300\,000 = 1\,200\,000"),
            S("Share in the ratio 3 : 2", math=r"\text{Abena: } \tfrac{3}{5} \times 1\,200\,000 = 720\,000;\quad \text{Biyik: } \tfrac{2}{5} \times 1\,200\,000 = 480\,000"),
            S("Add interest and share", math=r"\text{Abena: } 200\,000 + 720\,000 = 920\,000;\quad \text{Biyik: } 100\,000 + 480\,000 = 580\,000"),
        ], check=r"920\,000 + 580\,000 = 1\,500\,000"),
        TIP("The Board's 2023 report says many candidates compared incorporated and unincorporated businesses by describing private and public companies, which are both incorporated. Remember: sole trader and partnership are the unincorporated ones.", title="Exam link"),
        MISTAKE("Sharing profit before interest", "If the deed gives interest on capital, give it first, then share what remains in the ratio. Sharing first gives the wrong totals."),
        MISTAKE("Saying a partnership has limited liability", "Ordinary partners have unlimited liability. Only a limited partner (where allowed) or a company has limited liability."),
        QUIZ("What is the main disadvantage of being a sole trader?", [
            "The owner shares all profit with others",
            "The owner has unlimited liability",
            "A deed is needed to start",
            "Two directors are required",
        ], 1, "A sole trader has unlimited liability, so personal property can be used to pay business debts.",
            hint="What happens to the owner's own property if the business fails?",
            feedback=["A sole trader keeps all profit; sharing is a partnership matter.", "", "A deed belongs to partnerships, not sole traders.", "Directors belong to companies."]),
        QUIZ("A person invests money in a partnership but takes no part in management. What is the person called?", [
            "Active partner", "Sleeping partner", "Director", "Debenture holder",
        ], 1, "A sleeping partner provides capital and shares profit but does not take part in running the business.",
            hint="The partner is 'quiet' in the business.",
            feedback=["An active partner works in the business.", "", "Directors manage a company, not a partnership.", "A debenture holder lends money to a company."]),
        PQ("State four advantages of being a sole trader.", "Easy to start; owner takes all decisions quickly; owner keeps all profit; close contact with customers; flexible; few legal formalities. (Any four.)"),
        PQ("List four items that might be included in a partnership deed.", "Capital each partner invests; the profit-sharing ratio; interest on capital and any partner salaries; duties of each partner; how a partner may join or leave; how disputes are settled. (Any four.)"),
        PQ("Tamba and Nkeng share profit equally after 10% interest on capital. Tamba put in FCFA 3 000 000 and Nkeng FCFA 1 000 000. Net profit is FCFA 900 000. Find each partner's total share.", "Interest: Tamba 300 000, Nkeng 100 000, total 400 000. Remainder = 900 000 - 400 000 = 500 000, shared equally = 250 000 each. Tamba: 300 000 + 250 000 = FCFA 550 000. Nkeng: 100 000 + 250 000 = FCFA 350 000. Total 900 000."),
        SUM("A sole trader is owned and run by one person who keeps all profit and has unlimited liability.",
            "A partnership has two or more owners who share capital, work, profit and loss, usually by a partnership deed.",
            "Sole traders and partnerships are unincorporated: no separate legal existence.",
            "Partners can be active, sleeping or limited (where allowed).",
            "Pay interest on capital first, then share the rest in the agreed ratio."),
    ],
))

# ------------------------------------------------------------------ 8. Companies under OHADA
LESSONS.append(lesson(
    module=M4,
    topic="Companies under OHADA",
    title="Companies under OHADA: SARL and SA",
    slug="com2-companies-under-ohada",
    minutes=20,
    summary="What a joint-stock company is, limited liability and separate legal personality, how the SARL (private) and the SA (public) differ, and how dividends are calculated.",
    objectives=[
        "Define a company, a share, a shareholder and limited liability",
        "Explain the meaning of OHADA and why it matters for companies in Cameroon",
        "Distinguish a SARL (private limited) from an SA (public limited)",
        "Calculate a dividend per share and a shareholder's dividend",
    ],
    key_concepts=["Company", "Limited liability", "Share and shareholder", "SARL", "SA", "Dividend", "OHADA"],
    blocks=[
        H("Introduction"),
        T("A business that wants to grow needs more money than one person or a few partners can provide. It may become a **company**, which can bring in many shareholders. "
          "In Cameroon, as in other member states of OHADA, the law for companies is shared across countries."),
        D("**OHADA** (Organisation pour l'Harmonisation en Afrique du Droit des Affaires) is a group of mainly African countries, including Cameroon, that share common business laws. Its Uniform Act on commercial companies sets the rules for companies in member states. The rules are revised from time to time, so check current details with your teacher.", title="Definition: OHADA"),
        D("A **company** (joint-stock company) is a business that is registered as a separate legal person. Its capital is divided into **shares**; the owners are **shareholders**, who share its profit.", title="Definition: company"),
        KEY("Two key features", "", cards=[
            ["Separate legal personality", "The company is a legal person in its own right. It can own property, sign contracts, sue and be sued in its own name. It continues even if shareholders change."],
            ["Limited liability", "A shareholder can lose only the amount invested or still unpaid on the shares. Personal property cannot be taken to pay the company's debts."],
        ]),
        H("SARL and SA"),
        D("A **SARL** (Societe a Responsabilite Limitee) is the private limited company. It is usually owned by a small group, often family or friends. Its shares cannot be offered to the general public, and are not freely sold.", title="SARL: private limited company"),
        D("An **SA** (Societe Anonyme) is the public limited company. It can raise money by offering shares to the public, and its shares can be bought and sold on a stock exchange when listed. It has more rules, such as stricter reporting.", title="SA: public limited company"),
        CODE(
            "Feature            SARL (private)             SA (public)\n"
            "-----------------  -------------------------  --------------------------\n"
            "Ownership          Few shareholders           Many shareholders\n"
            "Raising capital    From members/lenders       Can offer shares to public\n"
            "Share transfer     Restricted                 Freer, may be listed\n"
            "Rules and reports  Fewer                      More\n"
            "Liability          Limited                    Limited",
            "text", title="SARL and SA compared", caption="Exact capital minimums and member numbers are set by the OHADA Uniform Act and change: check the current rules."),
        T("Both kinds are **incorporated**: they have their own legal personality and limited liability. Do not mistake private and public companies for 'unincorporated' businesses. They are not."),
        H("Directors, meetings and dividends"),
        T("Shareholders own the company but a **board of directors** manages it. Shareholders meet at least once a year at the **annual general meeting (AGM)** to approve accounts, elect directors and decide on dividends."),
        D("A **dividend** is the part of a company's profit paid to shareholders, usually shown as a sum per share.", title="Definition: dividend",
          formula=r"\text{Dividend per share} = \frac{\text{profit paid out}}{\text{number of shares}}"),
        EX("Worked example 1: Dividend per share (invented figures)", intro="A company has 100 000 shares. It decides to pay out FCFA 3 000 000 as dividend. Ms Fotso owns 2 000 shares. Find the dividend per share and her total dividend.", steps=[
            S("Dividend per share", math=r"\frac{3\,000\,000}{100\,000} = 30", text="FCFA 30 per share."),
            S("Her dividend", math=r"2\,000 \times 30 = 60\,000", text="Ms Fotso receives FCFA 60 000."),
        ], check=r"\frac{2\,000}{100\,000} \times 3\,000\,000 = 60\,000"),
        KEY("Advantages and disadvantages of companies", "", cards=[
            ["Advantages", "Limited liability; large capital from many shareholders; continuity; can employ experts; easier to borrow."],
            ["Disadvantages", "More legal rules and costs to set up; accounts must be published (more for SA); profit shared widely; directors' decisions may differ from small shareholders' wishes."],
        ]),
        TIP("When asked to compare incorporated and unincorporated businesses, use: legal entity, liability, capital, continuity and rules. Do not write only about private versus public companies.", title="Exam link"),
        MISTAKE("Saying shareholders run the company day to day", "Directors manage the company. Shareholders elect directors and vote at meetings."),
        MISTAKE("Mixing up SA and SARL", "SARL = private; SA = public. Think 'A' for anyone, as an SA may offer shares to anyone."),
        QUIZ("Which feature protects the personal property of shareholders in a company?", [
            "Unlimited liability", "Limited liability", "Partnership deed", "Franchise",
        ], 1, "Limited liability means a shareholder can lose only the money invested in the shares.",
            hint="What word describes liability that has a limit?",
            feedback=["Unlimited liability is the opposite: the owner's personal property is at risk.", "", "A deed is used by partnerships.", "A franchise is permission to use a brand, not a protection of liability."]),
        QUIZ("Which type of company may offer its shares to the general public?", [
            "SARL (private limited)", "SA (public limited)", "A sole trader", "A partnership",
        ], 1, "The SA is the public limited company, which can offer shares to the public and be listed on a stock exchange.",
            hint="Which of the two company types is the 'public' one?",
            feedback=["The SARL is private and cannot offer shares to the public.", "", "A sole trader has no shares.", "A partnership has partners, not shares."]),
        PQ("Define a company and state two advantages of forming one.", "A company is a business registered as a separate legal person whose capital is divided into shares owned by shareholders. Advantages: limited liability for shareholders, and the ability to raise large capital from many people; also continuity if owners change."),
        PQ("State three differences between a SARL and an SA.", "A SARL is private, with few shareholders, restricted share transfer and fewer rules; it cannot offer shares to the public. An SA is public, with many shareholders, can offer shares to the public and be listed on a stock exchange, and has stricter rules and reporting."),
        PQ("A company with 50 000 shares pays FCFA 1 500 000 in dividends. Find the dividend per share and the dividend of a person holding 800 shares.", "Per share = 1 500 000 / 50 000 = FCFA 30. For 800 shares: 800 x 30 = FCFA 24 000."),
        SUM("A company is a separate legal person with shares owned by shareholders; it has limited liability.",
            "OHADA gives Cameroon and other member states common company law.",
            "SARL = private limited; SA = public limited and may offer shares to the public.",
            "Directors run the company; shareholders vote at the AGM and receive dividends.",
            "Dividend per share = profit paid out divided by number of shares."),
    ],
))

# ------------------------------------------------------------------ 9. Cooperatives and public corporations
LESSONS.append(lesson(
    module=M4,
    topic="Cooperatives and public corporations",
    title="Cooperative societies and public corporations",
    slug="com2-cooperatives-and-public-corporations",
    minutes=20,
    summary="The features and types of cooperative societies, how a cooperative surplus can be shared, the nature, aims and problems of public corporations, and the idea of privatisation.",
    objectives=[
        "Describe the main features of a cooperative society",
        "Name types of cooperative and distinguish them from a tontine",
        "Describe a public corporation and give reasons for its existence",
        "State disadvantages of public corporations and explain privatisation",
    ],
    key_concepts=["Cooperative society", "Open membership", "Democratic control", "Public corporation", "Privatisation"],
    blocks=[
        H("Introduction"),
        T("Cocoa farmers in a village may find it hard to bargain with big buyers alone. Together they can pool their cocoa, sell in bulk and share the gain. Their group is a **cooperative**. "
          "Other businesses are owned not by people but by the **state**: an electricity or water supplier, a national oil company or the national broadcaster. These are **public corporations**."),
        D("A **cooperative society** is a business owned and run by its members, who join voluntarily to help themselves and each other by working together, rather than only to earn a profit.", title="Definition: cooperative society"),
        KEY("Features of a cooperative", "Learn these; the Board's 2023 report names open membership, democratic control and limited liability.", cards=[
            ["Open membership", "Anyone who shares the aim may join, and may leave when they wish."],
            ["Democratic control", "One member, one vote, whatever the number of shares held."],
            ["Limited liability", "Members risk only the money they paid in."],
            ["Mutual help", "Members help each other; services are for members' benefit."],
            ["Surplus shared", "Interest on share capital is limited. Surplus is shared by members according to their use of the society."],
        ]),
        KEY("Types of cooperative", "", cards=[
            ["Consumer", "Members buy goods in bulk and sell to members at lower prices."],
            ["Producer or marketing (farmers')", "Farmers pool crops like cocoa or coffee, process and sell together for better prices."],
            ["Credit and savings", "Members save and borrow from a shared fund at fair interest; often called credit unions."],
            ["Housing", "Members combine savings to build or buy homes."],
        ]),
        T("A cooperative is not the same as a **tontine**. A tontine is an informal rotating savings group with a fixed contribution and a member taking the pot in turn. Cooperatives are formal societies with rules and records. OHADA has a Uniform Act for cooperative societies; check the current rules with your teacher."),
        EX("Worked example 1: Sharing a surplus (invented figures)", intro="A consumer cooperative has a surplus of FCFA 480 000. Members' total purchases were FCFA 8 000 000. The surplus is shared in proportion to purchases. Find the rate and the share of a member who bought FCFA 150 000.", steps=[
            S("Find the rate", math=r"\frac{480\,000}{8\,000\,000} = 0.06 = 6\%"),
            S("Apply to the member", math=r"0.06 \times 150\,000 = 9\,000", text="The member receives FCFA 9 000."),
        ], check=r"\frac{150\,000}{8\,000\,000} \times 480\,000 = 9\,000"),
        H("Public corporations"),
        D("A **public corporation** is a business owned by the government but run by a board and managers appointed by the government. It provides a service or product to the public and is set up by law.", title="Definition: public corporation"),
        T("In Cameroon, bodies often cited as public enterprises include the national hydrocarbons company, the state telecommunications company, the national radio and television and the Port Authorities of Douala and Kribi. "
          "Ownership changes over the years, so check the current status in your textbook before using a particular example."),
        KEY("Why governments run public corporations", "", cards=[
            ["Essential services", "Water, power, post and transport serve everyone, including areas where profit is low."],
            ["Avoid private monopoly", "The state can prevent one private firm from abusing its power over prices."],
            ["Strategic industries", "The state controls industries important for security or the economy."],
            ["Jobs and development", "Corporations can create jobs and develop poor regions."],
        ]),
        KEY("Problems of public corporations", "", cards=[
            ["Inefficiency", "Without competition or profit motive, costs may be high and service slow."],
            ["Political interference", "Appointments and decisions may follow political rather than business reasons."],
            ["Losses", "Losses may be covered by taxpayers' money."],
        ]),
        D("**Privatisation** is the transfer of a publicly owned business, in whole or in part, to private owners. Governments may do this to improve efficiency or raise money.", title="Definition: privatisation"),
        TIP("The Board's 2023 report says that questions on the differences between incorporated and unincorporated bodies, and on the features of cooperatives, got only average scores. Learn the exact features and add a short explanation to each.", title="Exam link"),
        MISTAKE("Saying cooperative members vote by number of shares", "In a cooperative the rule is one member, one vote. Voting by shares is a company rule."),
        MISTAKE("Confusing public corporations with public companies", "A public corporation is owned by the state. A public limited company (SA) is owned by shareholders from the public."),
        QUIZ("Which feature of a cooperative describes 'one member, one vote'?", [
            "Open membership", "Democratic control", "Limited liability", "Unlimited capital",
        ], 1, "Democratic control means every member has one vote regardless of how many shares they hold.",
            hint="Which feature is about who controls decisions?",
            feedback=["Open membership means anyone who shares the aim may join.", "", "Limited liability concerns what members can lose.", "A cooperative's capital is limited to what members provide."]),
        QUIZ("Which statement about a public corporation is correct?", [
            "It is owned by shareholders who buy shares on the stock exchange",
            "It is owned by the government and run by a board",
            "It is owned by its customers on a one-person-one-vote basis",
            "It is owned by two or more partners",
        ], 1, "A public corporation is owned by the state and managed by a board.",
            hint="Who owns it?",
            feedback=["That describes a public limited company (SA).", "", "That describes a cooperative society.", "That describes a partnership."]),
        PQ("State four features of a cooperative society.", "Open and voluntary membership; democratic control, one member one vote; limited liability; mutual help among members; limited interest on shares, surplus shared among members. (Any four.)"),
        PQ("Distinguish between a cooperative society and a tontine.", "A cooperative society is a formal, registered business owned and controlled by its members, with rules, records and limited liability. A tontine is an informal rotating savings group in which members contribute regularly and take the whole pot in turn."),
        PQ("Give three reasons why governments set up public corporations and two problems they face.", "Reasons: to provide essential services such as water or power; to prevent private monopoly; to control strategic industries; to create jobs. Problems: inefficiency without competition; political interference; losses covered by taxpayers."),
        SUM("A cooperative is owned and run by members who help each other; it has open membership, one member one vote and limited liability.",
            "Types include consumer, producer, credit and housing cooperatives.",
            "A cooperative surplus can be shared in proportion to members' use of the society.",
            "A public corporation is owned by the state and run by a board to provide a public service.",
            "Privatisation transfers a state business to private owners."),
    ],
))

# ------------------------------------------------------------------ 10. Sources of finance and the stock exchange
LESSONS.append(lesson(
    module=M4,
    topic="Sources of business finance and the stock exchange",
    title="Sources of business finance and the stock exchange",
    slug="com2-sources-of-finance-and-stock-exchange",
    minutes=20,
    summary="Short, medium and long-term sources of finance, internal and external finance, shares and debentures, and how a stock exchange helps companies raise money.",
    objectives=[
        "Classify sources of finance as short, medium or long term, internal or external",
        "Distinguish shares from debentures",
        "Explain what a stock exchange is and what it does",
        "Choose a suitable source of finance for a stated need",
    ],
    key_concepts=["Short, medium and long-term finance", "Retained profit", "Overdraft", "Shares", "Debentures", "Stock exchange"],
    blocks=[
        H("Introduction"),
        T("Madame Ngu wants to open a small shop. She needs money for shelves, stock and a first month's rent. Where will it come from? Her own savings? A loan from a bank or microfinance? A supplier who allows her to pay later? "
          "Every business, from a stall to a large company, needs **finance**, and the right source depends on how much is needed and for how long."),
        D("**Business finance** is the money a business uses to start, run and grow. Sources are grouped by how long the money is needed and by whether it comes from inside or outside the business.", title="Definition: business finance"),
        H("By time"),
        KEY("Short, medium and long term", "Match the source to the length of the need.", cards=[
            ["Short term (up to about a year)", "Bank overdraft, trade credit from suppliers, short loans. Used for day-to-day needs like buying stock."],
            ["Medium term (about 1 to 5 years)", "Bank term loans, hire purchase and leasing. Used for vehicles and equipment."],
            ["Long term (over about 5 years)", "Issuing shares, debentures, long bank loans, mortgages, retained profit. Used for land, buildings and expansion."],
        ]),
        T("A **bank overdraft** lets a business spend more than it has in its account, up to an agreed limit, and pay interest on the amount overdrawn. **Trade credit** means the supplier delivers goods now and is paid later. "
          "**Hire purchase** lets a business use an asset while paying for it by instalments; it becomes the buyer's after the last payment. **Leasing** is renting an asset for a fee."),
        H("Internal and external sources"),
        KEY("Where the money comes from", "", cards=[
            ["Internal", "From inside the business: owner's savings, retained (ploughed-back) profit, selling unwanted assets."],
            ["External", "From outside: bank loans, overdrafts, suppliers' credit, microfinance, family loans, shares sold to new owners, debentures."],
        ]),
        T("A sole trader in Cameroon often relies on personal savings, family, a **tontine** (a rotating savings group), a microfinance institution or supplier credit. Mobile money can help make payments and small short-term loans, but check terms and charges before borrowing."),
        H("Shares and debentures"),
        D("A **share** is a unit of ownership in a company. Shareholders receive a dividend that varies with profit and may vote at meetings. **Ordinary shares** carry the most risk and reward; **preference shares** get a fixed dividend paid first.", title="Definition: share"),
        D("A **debenture** is a loan to a company, usually for a fixed period. The holder is a **creditor**, not an owner, and receives fixed interest whether or not the company makes a profit.", title="Definition: debenture"),
        CODE(
            "Feature         Shares                     Debentures\n"
            "--------------  -------------------------  ---------------------------\n"
            "Holder is       Owner (shareholder)        Lender (creditor)\n"
            "Return          Dividend, varies           Fixed interest\n"
            "Votes           Usually yes (ordinary)     No\n"
            "Repayment       Not repaid by company      Repaid on a fixed date\n"
            "If company      Paid after creditors       Paid before shareholders\n"
            "closes down",
            "text", title="Shares and debentures compared"),
        H("The stock exchange"),
        D("A **stock exchange** is an organised market where shares and bonds of listed companies are bought and sold through licensed brokers.", title="Definition: stock exchange"),
        T("It has two jobs. In the **primary market** a company sells new shares or bonds and receives the money. In the **secondary market** existing shares are sold between investors, so a shareholder can turn shares into cash. "
          "A **stockbroker** carries out the buying and selling for investors. Cameroon has the Douala Stock Exchange (DSX), and Central Africa also has a regional exchange (BVMAC); check the current set-up in your textbook."),
        KEY("Benefits and risks", "", cards=[
            ["Benefits", "Helps companies raise large long-term funds; shares can be sold quickly; prices show the market's view of a company; encourages saving and investment."],
            ["Risks", "Share prices can fall; dividends are not guaranteed; small markets may have few buyers."],
        ]),
        EX("Worked example 1: Returns on two investments (invented figures)", intro="Mr Essomba buys a share for FCFA 2 000 and receives a dividend of FCFA 150 in the year. He also holds a debenture of FCFA 10 000 paying 8% interest. Find the share's dividend as a percentage of its price and the debenture interest.", steps=[
            S("Dividend as a percentage", math=r"\frac{150}{2\,000} \times 100 = 7.5\%"),
            S("Debenture interest", math=r"\frac{8}{100} \times 10\,000 = 800", text="The interest is FCFA 800 a year and is fixed. The dividend may change from year to year."),
        ]),
        EX("Worked example 2: Choosing finance", intro="A bakery needs (a) FCFA 300 000 to buy flour for the next month and (b) a new oven it will use for ten years. Suggest suitable sources.", steps=[
            S("(a) Flour is a short-term need", text="Use trade credit from the flour supplier or a short-term overdraft; repay from sales within weeks."),
            S("(b) The oven is a long-term asset", text="Use a long-term loan or retained profit, or hire purchase or leasing for the medium-term. Do not use a short-term overdraft for a long-life asset."),
        ]),
        TIP("When a question asks you to advise on finance, state the purpose, how long the money is needed and then name a matching source.", title="Exam link"),
        MISTAKE("Calling a debenture holder an owner", "A debenture holder lent money and is a creditor. Only shareholders are owners."),
        MISTAKE("Using short-term finance for a long-term asset", "Buying a building with an overdraft is risky because the overdraft may be called in. Match the source to how long the money is needed."),
        QUIZ("Which of these is an internal source of finance?", [
            "Bank overdraft", "Retained profit", "Debentures", "Supplier credit",
        ], 1, "Retained profit is money the business already earned and keeps inside the business.",
            hint="Which source needs no outside lender or investor?",
            feedback=["A bank is outside the business.", "", "Debentures are loans from outsiders.", "Supplier credit comes from outside suppliers."]),
        QUIZ("What is the main difference between a share and a debenture?", [
            "A shareholder is an owner; a debenture holder is a lender",
            "A debenture holder votes; a shareholder does not",
            "Shares pay fixed interest; debentures pay a variable dividend",
            "There is no difference",
        ], 0, "A share is part ownership with a variable dividend; a debenture is a loan with fixed interest.",
            hint="Think owner versus lender.",
            feedback=["", "Usually the reverse: ordinary shareholders vote; debenture holders do not.", "This is the wrong way round: debentures pay fixed interest and shares pay variable dividends.", "They are different in ownership, return and risk."]),
        PQ("Explain the term stock exchange and state two functions.", "A stock exchange is an organised market where shares and bonds of listed companies are bought and sold through brokers. Functions: it helps companies raise long-term finance by selling shares; and it lets investors sell their shares for cash quickly. It also shows the market value of companies."),
        PQ("Distinguish between short-term and long-term sources of finance, giving one example of each.", "Short-term finance is needed for up to about a year, for example a bank overdraft or trade credit, to buy stock. Long-term finance is needed for several years, for example issuing shares or a long-term bank loan, to buy land or buildings."),
        PQ("A debenture of FCFA 5 000 000 pays 6% interest a year. Calculate the annual interest.", "Interest = 6/100 x 5 000 000 = FCFA 300 000."),
        SUM("Finance is grouped by time (short, medium, long term) and by origin (internal or external).",
            "Match the source to the purpose: overdraft or trade credit for stock; loans, shares or retained profit for fixed assets.",
            "Shares make you an owner with a variable dividend; debentures make you a lender with fixed interest.",
            "A stock exchange is a market for shares and bonds, with a primary and a secondary market.",
            "Sole traders rely on savings, family, tontines, microfinance and supplier credit."),
    ],
))

# ------------------------------------------------------------------ 11. Capital and working capital calculations
LESSONS.append(lesson(
    module=M4,
    topic="Capital and working capital calculations",
    title="Capital owned, working capital and capital employed",
    slug="com2-capital-and-working-capital",
    minutes=22,
    summary="How to calculate capital owned, working capital and capital employed from a list of assets and liabilities, with formulas, a worked example and a quick check that the figures agree.",
    objectives=[
        "Distinguish fixed assets, current assets, current liabilities and long-term liabilities",
        "Calculate working capital",
        "Calculate capital employed and capital owned",
        "Check that capital owned equals total assets minus total liabilities",
    ],
    key_concepts=["Fixed assets", "Current assets", "Current liabilities", "Working capital", "Capital employed", "Capital owned"],
    blocks=[
        H("Introduction"),
        T("Ask yourself: if Madame Ngo closed her shop today, sold everything and paid every debt, how much would be left for her? And does she have enough cash and stock to pay this month's bills? "
          "The first question is about **capital owned**; the second is about **working capital**. Both come from the same list of things the business has and owes."),
        KEY("Assets and liabilities", "Sort every item before you calculate.", cards=[
            ["Fixed assets", "Things the business keeps for a long time to use, not to sell: land, buildings, equipment, vehicles."],
            ["Current assets", "Things that are, or will soon become, cash: stock, debtors (people who owe the business), bank balance, cash in hand."],
            ["Current liabilities", "Debts to be paid within about a year: creditors (suppliers owed), bank overdraft."],
            ["Long-term liabilities", "Debts payable after more than a year: a long-term bank loan, a mortgage."],
        ]),
        D("**Working capital** (net current assets) is the money available for the day-to-day running of the business. It is current assets minus current liabilities.", title="Definition: working capital",
          formula=r"\text{Working capital} = \text{current assets} - \text{current liabilities}"),
        D("**Capital employed** is the total long-term money used in the business. It is fixed assets plus working capital.", title="Definition: capital employed",
          formula=r"\text{Capital employed} = \text{fixed assets} + \text{working capital}"),
        D("**Capital owned** (owner's capital or net worth) is what the owner has put into the business plus profit kept, less drawings. It equals the money left when all liabilities are subtracted from all assets.", title="Definition: capital owned",
          formula=r"\text{Capital owned} = \text{total assets} - \text{total liabilities}"),
        KEY("Two ways to see capital employed", "The same figure from either side.", cards=[
            ["From the uses side", "Fixed assets + working capital"],
            ["From the sources side", "Capital owned + long-term liabilities"],
        ]),
        IMG("f5com2-capital-employed.svg",
            alt="Two columns showing fixed assets plus working capital on the left, and long-term loan plus capital owned on the right, both totalling 16 500 000 francs",
            caption="Figure 1. Both sides of capital employed give the same total (invented figures, FCFA)."),
        EX("Worked example 1: Working capital, capital employed and capital owned (invented figures)", intro="Madame Ngo's business has these items, in FCFA: land and building 8 000 000; equipment 2 500 000; vehicle 3 500 000; stock 1 800 000; debtors 900 000; bank 1 100 000; cash 200 000; creditors 1 300 000; bank overdraft 200 000; long-term loan 5 000 000. Find (a) working capital, (b) capital employed, (c) capital owned.", steps=[
            S("Add the fixed assets", math=r"8\,000\,000 + 2\,500\,000 + 3\,500\,000 = 14\,000\,000"),
            S("Add the current assets", math=r"1\,800\,000 + 900\,000 + 1\,100\,000 + 200\,000 = 4\,000\,000"),
            S("Add the current liabilities", math=r"1\,300\,000 + 200\,000 = 1\,500\,000"),
            S("(a) Working capital", math=r"4\,000\,000 - 1\,500\,000 = 2\,500\,000"),
            S("(b) Capital employed", math=r"14\,000\,000 + 2\,500\,000 = 16\,500\,000"),
            S("(c) Capital owned", math=r"16\,500\,000 - 5\,000\,000 = 11\,500\,000", text="Capital employed less the long-term loan leaves the owner's part."),
        ], check=r"(14\,000\,000 + 4\,000\,000) - (1\,500\,000 + 5\,000\,000) = 11\,500\,000"),
        EX("Worked example 2: How capital owned changes (same business)", intro="At the start of the year the owner's capital was FCFA 10 000 000. The year's net profit was FCFA 3 000 000 and she took drawings (money for private use) of FCFA 1 500 000. Find the closing capital.", steps=[
            S("Use the formula", math=r"\text{Closing capital} = \text{opening capital} + \text{net profit} - \text{drawings}"),
            S("Substitute", math=r"10\,000\,000 + 3\,000\,000 - 1\,500\,000 = 11\,500\,000", text="This matches the capital owned found in Example 1, so the figures agree."),
        ]),
        T("A rough guide: current assets should usually be larger than current liabilities. If working capital is negative, the business may struggle to pay its bills on time. The ratio of current assets to current liabilities is called the current ratio. Here it is 4 000 000 : 1 500 000, about 2.7 : 1."),
        TIP("Write the formula, then the working, then the answer with the unit (FCFA). Always list the groups first: fixed assets, current assets, current liabilities, long-term liabilities. The Board's 2023 report notes that business performance questions were poorly answered, so practise calculations regularly.", title="Exam link"),
        MISTAKE("Counting stock as a fixed asset", "Stock is bought to be sold, so it is a current asset. A shop's shelves are fixed assets; the goods on them are current assets."),
        MISTAKE("Treating a long-term loan as a current liability", "Only debts due within about a year are current liabilities. A five-year loan is long term, so it is not subtracted when finding working capital."),
        QUIZ("Current assets are FCFA 2 750 000 and current liabilities are FCFA 1 900 000. What is the working capital?", [
            "FCFA 4 650 000", "FCFA 850 000", "FCFA 1 900 000", "FCFA 2 750 000",
        ], 1, "Working capital = current assets - current liabilities = 2 750 000 - 1 900 000 = 850 000.",
            hint="Subtract the debts due soon from the cash-like items.",
            feedback=["You added them. Working capital is a difference.", "", "That is the current liabilities figure only.", "That is the current assets figure only."]),
        QUIZ("Which item is a current asset?", [
            "Delivery van", "Debtors", "Mortgage on the building", "Long-term loan",
        ], 1, "Debtors owe the business money and will pay soon, so they are current assets.",
            hint="Which item will soon become cash?",
            feedback=["A van is kept for long use, so it is a fixed asset.", "", "A mortgage is a long-term liability.", "A long-term loan is a liability, not an asset."]),
        PQ("Define working capital and write its formula.", "Working capital is the money available for day-to-day running of the business. Working capital = current assets - current liabilities."),
        PQ("A trader has fixed assets FCFA 6 000 000, current assets FCFA 2 000 000 and current liabilities FCFA 800 000. Calculate working capital and capital employed.", "Working capital = 2 000 000 - 800 000 = FCFA 1 200 000. Capital employed = 6 000 000 + 1 200 000 = FCFA 7 200 000."),
        PQ("A business has capital employed FCFA 7 200 000 and a long-term loan of FCFA 2 000 000. Find the capital owned.", "Capital owned = capital employed - long-term liabilities = 7 200 000 - 2 000 000 = FCFA 5 200 000."),
        SUM("Sort items into fixed assets, current assets, current liabilities and long-term liabilities first.",
            "Working capital = current assets - current liabilities.",
            "Capital employed = fixed assets + working capital = capital owned + long-term liabilities.",
            "Capital owned = total assets - total liabilities = opening capital + net profit - drawings.",
            "Show formula, working and answer with the unit."),
    ],
))

# ------------------------------------------------------------------ 12. Profit, stockturn, mark-up and margin
LESSONS.append(lesson(
    module=M4,
    topic="Profit, stockturn, mark-up and margin",
    title="Turnover, profit, stockturn, mark-up and margin",
    slug="com2-profit-stockturn-markup-margin",
    minutes=25,
    summary="How to find turnover, cost of goods sold, gross and net profit, the rate of stockturn, mark-up and margin from trading figures, with formulas, worked examples and a trial-balance style exercise.",
    objectives=[
        "Calculate turnover, cost of goods sold, gross profit and net profit",
        "Calculate the rate of stockturn from cost of goods sold and average stock",
        "Calculate mark-up and margin and convert between selling price, cost and profit",
        "Express gross and net profit as a percentage of sales",
    ],
    key_concepts=["Turnover", "Cost of goods sold", "Gross profit", "Net profit", "Rate of stockturn", "Mark-up", "Margin"],
    blocks=[
        H("Introduction"),
        T("At the end of the year a trader asks three questions. Did I make a profit? How fast did my stock sell? What percentage did I add to the cost price? "
          "In the Board's 2023 report, a question asking candidates to calculate gross profit, net profit, rate of turnover and net profit as a percentage of sales from trial-balance figures was left unattempted by more than 70% of candidates. Learn the steps and you will gain easy marks."),
        D("**Turnover** (sales) is the total value of goods sold in a period. **Net turnover** is sales less returns inwards (goods customers sent back).", title="Definition: turnover"),
        D("**Cost of goods sold** is the cost of the goods that were actually sold in the period.", title="Definition: cost of goods sold",
          formula=r"\text{Cost of goods sold} = \text{opening stock} + \text{purchases} + \text{carriage inwards} - \text{returns outwards} - \text{closing stock}"),
        D("**Gross profit** is net sales less cost of goods sold. **Net profit** is gross profit less the running expenses (wages, rent, electricity, transport and so on), plus any other income.", title="Definition: gross and net profit",
          formula=r"\text{Gross profit} = \text{net sales} - \text{cost of goods sold} \qquad \text{Net profit} = \text{gross profit} - \text{expenses}"),
        T("Carriage inwards is the cost of bringing purchases to the business, so it is added to cost. Returns outwards are goods sent back to suppliers, so they are subtracted. Carriage outwards (delivering to customers) is an expense, not a cost of goods."),
        EX("Worked example 1: Gross and net profit (invented figures, FCFA)", intro="A trader's figures: sales 6 200 000; returns inwards 200 000; opening stock 500 000; purchases 3 900 000; carriage inwards 50 000; returns outwards 150 000; closing stock 700 000; wages 700 000; rent 240 000; electricity 80 000; transport 120 000. Find net sales, cost of goods sold, gross profit, net profit and each as a percentage where asked.", steps=[
            S("Net sales", math=r"6\,200\,000 - 200\,000 = 6\,000\,000"),
            S("Cost of goods sold", math=r"500\,000 + 3\,900\,000 + 50\,000 - 150\,000 - 700\,000 = 3\,600\,000"),
            S("Gross profit", math=r"6\,000\,000 - 3\,600\,000 = 2\,400\,000"),
            S("Total expenses", math=r"700\,000 + 240\,000 + 80\,000 + 120\,000 = 1\,140\,000"),
            S("Net profit", math=r"2\,400\,000 - 1\,140\,000 = 1\,260\,000"),
            S("Net profit as a percentage of sales", math=r"\frac{1\,260\,000}{6\,000\,000} \times 100 = 21\%"),
        ], check=r"\text{Gross profit} \% = \frac{2\,400\,000}{6\,000\,000} \times 100 = 40\%"),
        H("Rate of stockturn"),
        D("The **rate of stockturn** (stock turnover) tells how many times the average stock is sold and replaced in a year. A higher rate usually means goods sell fast.", title="Definition: rate of stockturn",
          formula=r"\text{Rate of stockturn} = \frac{\text{cost of goods sold}}{\text{average stock}}, \qquad \text{Average stock} = \frac{\text{opening stock} + \text{closing stock}}{2}"),
        EX("Worked example 2: Stockturn (same trader)", intro="Find the average stock and the rate of stockturn.", steps=[
            S("Average stock", math=r"\frac{500\,000 + 700\,000}{2} = 600\,000"),
            S("Rate of stockturn", math=r"\frac{3\,600\,000}{600\,000} = 6", text="Stock was sold and replaced 6 times in the year, about once every two months (12 months / 6)."),
        ]),
        T("Some textbooks call this rate 'rate of turnover'. The Board's wording is 'rate of turnover' in its report. Use the formula given by your teacher, and note which stock figure is used."),
        H("Mark-up and margin"),
        D("**Mark-up** is gross profit as a percentage of the cost price. **Margin** is gross profit as a percentage of the selling price (sales).", title="Definition: mark-up and margin",
          formula=r"\text{Mark-up} = \frac{\text{gross profit}}{\text{cost}} \times 100 \qquad \text{Margin} = \frac{\text{gross profit}}{\text{selling price}} \times 100"),
        EX("Worked example 3: Mark-up and margin (invented figures)", intro="A shop buys a sack of rice for FCFA 8 000 and sells it for FCFA 10 000. Find the profit, mark-up and margin.", steps=[
            S("Profit", math=r"10\,000 - 8\,000 = 2\,000"),
            S("Mark-up", math=r"\frac{2\,000}{8\,000} \times 100 = 25\%"),
            S("Margin", math=r"\frac{2\,000}{10\,000} \times 100 = 20\%"),
        ]),
        EX("Worked example 4: Selling price from mark-up", intro="A trader buys goods at FCFA 12 000 and adds a mark-up of 50%. Find the selling price and the margin.", steps=[
            S("Profit", math=r"50\% \times 12\,000 = 6\,000"),
            S("Selling price", math=r"12\,000 + 6\,000 = 18\,000"),
            S("Margin", math=r"\frac{6\,000}{18\,000} \times 100 = 33.3\%", text="Same profit, but a smaller percentage, because it is taken on the bigger selling price."),
        ]),
        KEY("Remember", "", cards=[
            ["Mark-up", "Profit divided by COST. Always bigger than margin for the same profit."],
            ["Margin", "Profit divided by SELLING PRICE."],
            ["Stockturn", "COST OF GOODS SOLD divided by average stock, not sales."],
        ]),
        TIP("Lay out the trading account step by step and label each total. If you make an arithmetic slip, examiners can still give marks for correct method.", title="Exam link"),
        MISTAKE("Dividing mark-up by the selling price", "Mark-up uses cost as the base. Using the selling price gives the margin. Check the wording: 'mark-up' means cost price."),
        MISTAKE("Forgetting returns and carriage", "Subtract returns inwards from sales and returns outwards from purchases. Add carriage inwards to purchases. Leaving these out changes gross profit."),
        QUIZ("Opening stock is FCFA 200 000, purchases FCFA 1 000 000 and closing stock FCFA 300 000. What is the cost of goods sold?", [
            "FCFA 900 000", "FCFA 1 500 000", "FCFA 700 000", "FCFA 1 200 000",
        ], 0, "Cost of goods sold = 200 000 + 1 000 000 - 300 000 = 900 000.",
            hint="Add opening stock and purchases, then subtract the stock left over.",
            feedback=["", "You added closing stock instead of subtracting it: 200 000 + 1 000 000 + 300 000 = 1 500 000.", "You left out the opening stock: 1 000 000 - 300 000 = 700 000.", "You ignored the closing stock: 200 000 + 1 000 000 = 1 200 000 is the goods available for sale."]),
        QUIZ("Which is correct for an item bought at FCFA 15 000 and sold at FCFA 20 000?", [
            "Mark-up 25%, margin 33.3%", "Mark-up 33.3%, margin 25%", "Mark-up 25%, margin 25%", "Mark-up 5%, margin 5%",
        ], 1, "Profit is 5 000. Mark-up = 5 000 / 15 000 = 33.3%. Margin = 5 000 / 20 000 = 25%.",
            hint="Mark-up is on cost; margin is on selling price.",
            feedback=["You swapped mark-up and margin.", "", "The two bases differ, so the percentages cannot be equal when there is a profit.", "5 000 is the profit in francs, not a percentage."]),
        PQ("Write the formulae for gross profit and net profit.", "Gross profit = net sales - cost of goods sold. Net profit = gross profit - expenses (plus other income, if any)."),
        PQ("Opening stock FCFA 300 000, purchases FCFA 2 000 000, closing stock FCFA 500 000, sales FCFA 3 000 000. Find cost of goods sold, gross profit and the rate of stockturn.", "Cost of goods sold = 300 000 + 2 000 000 - 500 000 = 1 800 000. Gross profit = 3 000 000 - 1 800 000 = 1 200 000. Average stock = (300 000 + 500 000) / 2 = 400 000. Rate of stockturn = 1 800 000 / 400 000 = 4.5 times."),
        PQ("A product costs FCFA 6 000 and sells for FCFA 7 500. Calculate the mark-up and the margin.", "Profit = 1 500. Mark-up = 1 500 / 6 000 x 100 = 25%. Margin = 1 500 / 7 500 x 100 = 20%."),
        PQ("Gross profit is FCFA 800 000, expenses FCFA 500 000 and net sales FCFA 4 000 000. Find net profit and net profit as a percentage of sales.", "Net profit = 800 000 - 500 000 = 300 000. Percentage = 300 000 / 4 000 000 x 100 = 7.5%."),
        SUM("Net sales = sales - returns inwards. Cost of goods sold = opening stock + purchases + carriage inwards - returns outwards - closing stock.",
            "Gross profit = net sales - cost of goods sold. Net profit = gross profit - expenses.",
            "Rate of stockturn = cost of goods sold / average stock.",
            "Mark-up = profit / cost x 100. Margin = profit / selling price x 100.",
            "Show formula, working and unit; label each total."),
    ],
))
