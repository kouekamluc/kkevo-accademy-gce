"""Form 5 Geography: Economic development potentials of Cameroon, part B
(manufacturing, informal sector, transport, tourism, economic growth). 9 lessons, one practice set each."""

from .dsl import *  # noqa: F403

COURSE = ("geography", "form-5")

MODULE = "The Geography of Cameroon"
TOPIC = "Economic development potentials"

LESSONS = []

# ------------------------------------------------------------------ 1. Manufacturing: types and distribution
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Manufacturing in Cameroon: types and distribution",
    slug="cmrdev-manufacturing-types-and-distribution",
    minutes=22,
    summary="The main types of manufacturing industry in Cameroon, where they are found (Douala, Yaounde, Bafoussam, Limbe, Edea and the north) and the reasons for that distribution.",
    objectives=[
        "Identify the types of manufacturing industries found in Cameroon",
        "Illustrate the distribution of manufacturing industries on a sketch map",
        "Explain why industries cluster in Douala and in other towns",
        "Describe the factors that influence where a factory is sited",
    ],
    key_concepts=["Manufacturing", "Agro-processing", "Industrial location factors", "Industrial cluster", "Raw materials", "Market", "Hydroelectric power"],
    blocks=[
        H("Introduction"),
        T("The bottle of soft drink you buy at a roadside stall in Bamenda, the planks used for a new house in Kumba and the "
          "bag of cement in a Yaounde hardware shop were all made in factories. They are products of **manufacturing**.\n\n"
          "Manufacturing is the **secondary sector** of the economy. It adds value to raw materials. Cocoa beans become chocolate "
          "and logs become furniture. A country that processes its own raw materials earns more than one that only sells them raw."),
        D("**Manufacturing** is the making of goods by changing raw materials into finished or semi-finished products, usually "
          "with machines, in a factory.", title="Manufacturing"),
        D("**Agro-processing** is the processing of farm products (such as cocoa, coffee, cotton, palm oil, rubber, sugar and tea) "
          "into forms that can be stored, sold or exported.", title="Agro-processing"),
        H("Types of manufacturing industry"),
        KEY("Main types of industry", "Geographers group industries by the raw material they use. Always give a type and an example in an answer.", cards=[
            ["Agro-processing", "Cocoa processing, coffee hulling, cotton ginning, palm oil and rubber processing, sugar and tea factories, flour and food processing."],
            ["Wood-based", "Sawmills, plywood and veneer, furniture and carpentry. Raw material: timber from the forests of the south and east."],
            ["Beverages", "Breweries, soft drinks and bottled water. These are made in many towns because the market is large."],
            ["Textiles", "Cotton cloth and clothing. Raw material: cotton grown in the north. Check your textbook for the factory towns."],
            ["Metal and mineral based", "Aluminium smelting at Edea, cement (limestone), and metal products."],
            ["Oil refining", "The refinery at Limbe turns imported or local crude oil into petrol, diesel and other fuels."],
            ["Other light industries", "Soap, plastics, paints, printing, assembly of goods. Many of these replace imports."],
        ]),
        T("Industries can also be grouped by size. **Large-scale** factories use machines and many workers. **Small-scale** workshops, "
          "such as carpenters, bakers and tailors, employ a few people and often work in the informal sector (see the lesson on that topic)."),
        IMG("f5g-cmrdev-industry-map.svg", alt="Simplified sketch map of Cameroon showing industries at Douala, Edea, Limbe, Bafoussam and Garoua",
            caption="Figure 1. Where some industries are found. Simplified sketch map, not to scale."),
        H("Distribution of industries and why"),
        T("Industries are not spread evenly. Most large factories are in the south-west and centre. A few are in the west and the north."),
        KEY("Where industries cluster", "Towns and the main reasons for their industries.", cards=[
            ["Douala", "The main industrial city. It has the biggest port, the largest market, a large labour force, banks, electricity, and road and rail links to the interior. Many types of industry are found here."],
            ["Yaounde", "The capital. Big market and government demand, many skilled workers, road and rail links. Food, drinks, printing and light industries."],
            ["Edea", "Aluminium smelting. The factory needs huge amounts of electricity, and Edea has hydroelectric power from the Sanaga river."],
            ["Limbe area", "Oil refinery on the coast, beside the sea so that tankers can deliver oil. Plantation products (rubber, palm) are also processed in the South-West."],
            ["Bafoussam", "In a farming region with a dense population. Agro-processing and drinks for a large local market. Check your textbook for the factories."],
            ["The north (for example Garoua)", "Cotton is grown here, so ginning and textile factories are placed near the raw material."],
        ]),
        TIP("The idea behind the pattern: industry goes where costs are lowest and sales are highest. Ports, power, roads, workers and a big market "
            "pull factories into the same towns. Once a few factories exist, banks, repair shops and suppliers follow. This is called **clustering**."),
        H("Factors that decide where a factory is sited"),
        T("Think of a factory owner choosing a site. The main factors are raw materials, power, market, labour, transport, capital and "
          "government policy.\n\n"
          "**Raw materials.** If the raw material loses weight in processing, the factory is built near the source. A sawmill is near the forest and a "
          "cotton ginnery is near the cotton fields. It is cheaper to carry the lighter product.\n\n"
          "**Market.** If the product is bulky or breaks easily (drinks, bread, cement), the factory is built near its customers.\n\n"
          "**Power and transport.** Heavy industries need cheap, reliable power and a port or road. Aluminium at Edea and refining at Limbe show this.\n\n"
          "**Labour, capital and policy.** Big towns have more skilled workers, banks and services. Government decisions such as tax "
          "breaks or industrial zones can also attract factories."),
        EX("Model answer 1: sketch map and explanation", intro="Illustrate and explain the distribution of manufacturing industries in Cameroon.", steps=[
            S("Draw the sketch", text="Draw the outline of Cameroon with the coast in the south-west. Mark Douala, Yaounde, Edea, Limbe, Bafoussam and Garoua. Add symbols and a key (as in Figure 1). Write 'Simplified sketch map, not to scale'."),
            S("State the pattern", text="Most industries are in the south-west and the centre, especially around Douala. Fewer are found in the west and the north."),
            S("Explain Douala", text="Douala has the main port, a big market, plenty of workers, electricity and road and rail links. Raw materials arrive and goods leave easily, so many industries cluster there."),
            S("Explain other towns", text="Edea has hydroelectric power from the Sanaga, used for aluminium. Limbe has a coastal refinery. Bafoussam and the north are near farm raw materials."),
            S("Conclude", text="Industry follows ports, power, raw materials and markets, so it is concentrated in a few towns."),
        ]),
        EX("Model answer 2: types of industry", intro="Name four types of manufacturing industry in Cameroon and give an example of each.", steps=[
            S("Agro-processing", text="Processing of farm products, for example cocoa, sugar or cotton ginning."),
            S("Wood-based", text="Sawmills and furniture workshops using timber."),
            S("Beverages", text="Breweries and soft-drink bottling plants."),
            S("Metal-based", text="Aluminium smelting at Edea. Cement is a mineral-based example."),
        ]),
        H("Common mistakes"),
        MISTAKE("Listing towns without reasons", "A list such as 'Douala, Yaounde, Edea' scores little. For each town give the factor: port, market, power or raw material."),
        MISTAKE("Mixing primary and secondary activities", "Growing cocoa or cutting logs is primary. Making chocolate or planks is manufacturing. Say which one you mean."),
        MISTAKE("Inventing details", "If you do not know where a factory stands, do not guess. Use the towns you are sure of and give the right reason."),
        QUIZ("Why is an aluminium smelter found at Edea?",
             ["Edea is the capital city", "Edea has cheap hydroelectric power from the Sanaga", "Edea is the biggest market", "Aluminium ore is mined at Edea"], 1,
             "Smelting aluminium needs very large amounts of electricity. Edea has hydroelectric power from the Sanaga river.",
             hint="Think of what the smelter uses most of.",
             feedback=["The capital is Yaounde, and factories are not sited because of capitals alone.", "",
                       "Douala, not Edea, is the biggest industrial market.", "The ore is not the reason for Edea's site. Power is."]),
        QUIZ("Why is a sawmill usually built near the forest rather than in a big town?",
             ["Timber loses weight when it is sawn, so it is cheaper to process it near the source", "Sawdust is needed in town", "Forests have big markets", "Towns have no workers"], 0,
             "A log is heavier than the planks cut from it. Carrying the lighter product saves transport cost.",
             hint="Think of what is carried, and how heavy it is.",
             feedback=["", "Sawdust is a waste product, not the reason.", "Forests have few customers. The market is elsewhere.", "Towns have plenty of workers."]),
        H("Practice questions"),
        PQ("Name four types of manufacturing industry found in Cameroon.",
           "Any four of: agro-processing (cocoa, sugar, cotton ginning), wood-based (sawmills, furniture), beverages (breweries, soft drinks), textiles, aluminium smelting, cement, oil refining."),
        PQ("Give two reasons why Douala has more factories than other towns.",
           "It has the main port for raw materials and exports. It has a large market and labour force. It has electricity, banks and road and rail links to the interior. (Any two, explained.)"),
        PQ("Explain why aluminium smelting is carried out at Edea.",
           "Smelting needs very large amounts of electricity. Edea has hydroelectric power from the Sanaga river and is linked to Douala port by road and rail, so it is a good site."),
        PQ("Explain why cotton ginning factories are built in the north.",
           "Cotton is grown in the north. Raw cotton is bulky and loses weight when the seeds are removed, so it is cheaper to gin it near the fields."),
        SUM("Manufacturing changes raw materials into finished goods and adds value. Main types in Cameroon: agro-processing, wood, beverages, textiles, aluminium, cement and refining.",
            "Industry is concentrated in the south-west and centre, above all around Douala, with others at Yaounde, Edea, Limbe, Bafoussam and in the north.",
            "Location factors: raw materials, power, market, labour, transport, capital and government policy.",
            "Weight-losing raw materials pull factories to the source. Bulky or fragile products pull them to the market.",
            "In an exam, draw a sketch map, give the pattern, and explain each town with a reason."),
    ],
))

# ------------------------------------------------------------------ 2. Problems of manufacturing
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Problems facing manufacturing and how they are tackled",
    slug="cmrdev-problems-of-manufacturing",
    minutes=20,
    summary="The main problems of the manufacturing sector in Cameroon (power, transport, capital, skills, small market, competition, taxation) and the responses that can reduce them.",
    objectives=[
        "Outline the problems faced by the manufacturing sector in Cameroon",
        "Explain how each problem reduces output or raises costs",
        "Describe responses that can reduce these problems",
        "Write a balanced answer using problem, effect and solution",
    ],
    key_concepts=["Power supply", "Capital", "Skilled labour", "Market size", "Competition from imports", "Taxation", "Import substitution"],
    blocks=[
        H("Introduction"),
        T("A baker in Douala can bake all night, but if electricity fails the dough is wasted. A furniture maker in Bafoussam may "
          "have orders but no money to buy a better machine. These small stories show the problems of **manufacturing** in Cameroon."),
        T("Cameroon has farm products, timber, minerals and water power. Yet manufacturing contributes less to the economy than it could. "
          "In this lesson we outline why, and what can be done."),
        IMG("f5g-cmrdev-problems-cycle.svg", alt="Diagram with six problems (power cuts, transport cost, little capital, few skills, small market and competition, taxes) pointing to weak industry",
            caption="Figure 1. The main problems of manufacturing."),
        H("The problems, one by one"),
        KEY("Problems", "For each problem, learn the effect.", cards=[
            ["Power problems", "Cuts and low voltage stop machines and spoil goods. Many firms buy generators, which are costly to run. Hydropower can fall in the dry season."],
            ["Transport problems", "Poor roads and delays at ports and checkpoints make raw materials and goods cost more. Factories in the interior suffer most."],
            ["Shortage of capital", "Banks lend little to small firms and interest is high. Firms cannot buy machines or expand."],
            ["Shortage of skills", "Too few trained technicians and managers. Many machines are repaired by outside experts, which costs money."],
            ["Small market", "Many people have low incomes, so they buy little. Local firms cannot make goods cheaply in large numbers."],
            ["Competition", "Cheap imports and goods that enter without paying duty undercut local products. The informal sector also competes."],
            ["Taxation and red tape", "Several taxes and long procedures raise costs. Check your textbook for the details of the taxes."],
        ]),
        T("Other problems include a weak supply of raw materials of good quality, and the high cost of spare parts which must be imported."),
        TIP("Every problem should be followed by its effect: 'Power cuts stop machines, so output falls and costs rise.' Examiners award marks for the effect, not for the name alone."),
        H("Responses"),
        T("Problems can be reduced. Some of the main responses are shown below. Each response is linked to a problem."),
        KEY("Responses linked to problems", "Match each problem to a response.", cards=[
            ["Power", "Build more dams and power lines, use solar and other sources, and improve maintenance so that supply is steady."],
            ["Transport", "Repair and build roads and railways, and improve port handling so that goods move faster."],
            ["Capital", "Offer credit to small firms, encourage microfinance, and invite local and foreign investors."],
            ["Skills", "Expand technical and vocational schools and apprenticeships so that firms find trained workers."],
            ["Market", "Trade within regional groups such as CEMAC, improve product quality so that goods can be exported, and promote buying local products."],
            ["Competition and taxation", "Control smuggling, protect young industries and simplify taxes and procedures."],
        ]),
        T("These responses are linked. Better roads and power lower costs, which lets firms compete with imports. More skilled workers help "
          "firms use machines well. This is why manufacturing grows only when several problems are solved together."),
        EX("Model answer 1", intro="Outline four problems faced by the manufacturing sector in Cameroon.", steps=[
            S("Power", text="Power cuts stop machines and spoil goods. Firms buy generators, which raises costs."),
            S("Transport", text="Poor roads and delays at ports raise the cost of raw materials and goods."),
            S("Capital", text="Small firms cannot borrow easily and interest is high, so they cannot buy machines."),
            S("Market and competition", text="Low incomes limit sales, and cheap imports undercut local goods."),
        ]),
        EX("Model answer 2", intro="Describe the measures that can be taken to solve the problems of manufacturing in Cameroon.", steps=[
            S("Introduction", text="Say that problems are linked, so solutions must work together."),
            S("Power and transport", text="More dams and power lines, better maintenance, and repair of roads, railways and port handling."),
            S("Capital and skills", text="Credit and microfinance for small firms, and technical schools to train workers."),
            S("Markets and rules", text="Regional trade (CEMAC), control of smuggling, and simpler taxes and procedures."),
            S("Conclusion", text="When costs fall and skills rise, firms can compete and manufacturing can add more value."),
        ]),
        H("Common mistakes"),
        MISTAKE("Naming the problem without an effect", "'Lack of capital' is a problem name. Add what happens: 'so firms cannot buy machines and output stays low'."),
        MISTAKE("Only blaming one cause", "Do not say that all problems come from the government or from imports. Show that several causes combine."),
        MISTAKE("Solutions that do not match", "Do not answer a power problem with a skills solution. Link each response to its own problem."),
        QUIZ("Which response best matches the problem of power cuts?",
             ["Teaching more apprentices", "Building more power stations and improving maintenance", "Lowering school fees", "Opening more banks"], 1,
             "Power cuts need a steadier supply of electricity: more generation, better lines and maintenance.",
             hint="Match the cause to its direct solution.",
             feedback=["Apprentices solve a skills problem.", "", "School fees are unrelated to power cuts.", "Banks help capital, not electricity."]),
        QUIZ("Why do cheap imports harm local manufacturers?",
             ["They raise local taxes", "They sell at lower prices, so local firms lose customers", "They give local firms free machines", "They lengthen roads"], 1,
             "Cheap imported goods undercut local prices. Local firms lose sales and may close.",
             hint="Think of a customer comparing two prices.",
             feedback=["Imports do not raise local taxes on firms.", "", "Imports do not supply machines to local firms.", "Imports have no effect on road length."]),
        H("Practice questions"),
        PQ("State three problems faced by manufacturing industries in Cameroon.",
           "Any three of: power cuts, poor transport, shortage of capital, shortage of skilled workers, small market, competition from imports, heavy taxation and red tape."),
        PQ("Explain how power cuts affect a factory.",
           "Machines stop, so output falls and goods may spoil. The firm may buy a generator, which is costly to run. Costs rise and the firm cannot compete."),
        PQ("Describe two measures that can improve the supply of skilled workers.",
           "Expand technical and vocational schools, and promote apprenticeships in firms, so that students learn skills that industry needs."),
        PQ("Suggest two ways of increasing the market for Cameroon's manufactured goods.",
           "Trade freely with neighbouring countries (for example in CEMAC), improve quality so that goods can be exported, and encourage people to buy local products."),
        SUM("The main problems are power, transport, capital, skills, a small market, competition and taxation.",
            "Each problem raises costs or lowers sales; always state the effect.",
            "Responses include more power stations, better roads and ports, credit, technical training, regional trade and simpler taxes.",
            "The problems are linked, so solutions work best together.",
            "In exams, give problem, effect and a matching solution."),
    ],
))

# ------------------------------------------------------------------ 3. The informal sector
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="The informal sector in Cameroon",
    slug="cmrdev-the-informal-sector",
    minutes=20,
    summary="What the informal sector is, why it has grown quickly in Cameroon, why it matters to the economy and what challenges it faces.",
    objectives=[
        "Define the informal sector and give Cameroonian examples",
        "Outline the reasons for its rapid increase in recent times",
        "Outline its importance to the economy",
        "Outline the challenges faced by informal workers and by the country",
    ],
    key_concepts=["Informal sector", "Formal sector", "Petty trade", "Self-employment", "Urbanisation", "Unemployment", "Tontine"],
    blocks=[
        H("Introduction"),
        T("Walk through Mokolo market in Yaounde or any busy market in Douala, Bamenda or Maroua and you see people selling vegetables, "
          "mending shoes, driving motorbike taxis and cooking snacks at the roadside. Few of them have a contract or pay a business tax."),
        T("These people work in the **informal sector**. It is one of the largest sources of work and income in Cameroon and in many other African countries."),
        D("The **informal sector** is made up of small economic activities that are not officially registered, not fully taxed or regulated, "
          "use little capital, and often depend on the owner's own work or family labour.", title="Informal sector"),
        D("The **formal sector** is made up of registered businesses that pay taxes, follow labour laws and usually give wages, contracts and social protection.", title="Formal sector"),
        IMG("f5g-cmrdev-informal-sector.svg", alt="Diagram of the informal sector: reasons for growth on the left, importance and challenges on the right",
            caption="Figure 1. The informal sector: why it grows, why it matters and what its problems are."),
        H("Examples"),
        KEY("Common informal activities", "Informal activities are found in towns and in villages. Learn at least four examples, from different kinds of work.", cards=[
            ["Trade", "Petty traders and street sellers (called bayam sellam in Cameroon), market sellers and roadside kiosks."],
            ["Transport", "Motorbike taxis (often called bendskin in Douala and okada in some Anglophone towns), hand-cart and head-load porters."],
            ["Crafts and repair", "Tailors, carpenters, welders, shoe menders, mechanics under trees."],
            ["Food and services", "Roadside cooking, hairdressers, phone-charging and small repair stalls."],
            ["Farming and fishing", "Small farms and fishing on a family basis, selling at local markets."],
        ]),
        H("Reasons for the rapid increase"),
        T("The informal sector has grown quickly for several reasons.\n\n"
          "**Too few formal jobs.** Industry and government cannot offer enough work for the many young people leaving school, so they create their own jobs.\n\n"
          "**Rapid urban growth.** Many people move from villages to towns such as Douala and Yaounde looking for work. The towns have more people than formal jobs.\n\n"
          "**Low incomes and rising prices.** A family with one low wage needs an extra income. Selling goods or services is a way to get it.\n\n"
          "**Easy to start.** Selling fruit or driving a motorbike taxi needs little money, no office and no special certificate.\n\n"
          "**Periods of economic difficulty and strict rules.** When formal firms close or lay off workers, people turn to informal work. "
          "Registration costs and taxes can also push small traders to stay unregistered. Check your textbook for the economic crisis years."),
        H("Importance to the economy"),
        T("The informal sector matters because it **gives jobs and income** to a large share of workers (check your textbook for current figures), "
          "especially women and young people. It supplies **cheap goods and services** to people with low incomes. It acts as a **training ground**, because "
          "apprentices learn skills from masters. It also **links farmers and consumers**: food crops from villages reach towns through petty traders. "
          "Informal incomes are spent in local shops and markets, which keeps money moving in the economy."),
        H("Challenges"),
        T("Informal work also has serious problems.\n\n"
          "**For workers:** low and unstable incomes, long hours, no insurance, no pension, and no protection if they are sick or injured. "
          "Many cannot borrow from banks because they have no papers or collateral.\n\n"
          "**For towns and the country:** traders blocking roads and pavements, rubbish in markets, congestion and accidents from motorbike taxis, and "
          "lost tax income for the government. Poor sanitation in crowded markets also affects health.\n\n"
          "**Responses:** simpler and cheaper business registration, microfinance and savings groups (tontines or njangi), training, "
          "better market buildings, and rules to keep roads safe. The aim is to help informal firms improve, not to punish them."),
        EX("Model answer 1", intro="Define the informal sector and give three examples from Cameroon.", steps=[
            S("Definition", text="The informal sector is the part of the economy made up of small activities that are not officially registered or fully taxed, use little capital and depend mainly on the owner's labour."),
            S("Examples", text="Petty trade (bayam sellam) in markets, motorbike taxis, and roadside tailoring or repair work."),
        ]),
        EX("Model answer 2", intro="Outline the reasons for the rapid growth of the informal sector in Cameroon.", steps=[
            S("Few formal jobs", text="School-leavers outnumber formal jobs, so many create their own work."),
            S("Rural-urban migration", text="Migrants to towns have no formal job and start trading or driving."),
            S("Low incomes", text="Families need extra income, so they sell goods or services."),
            S("Easy entry", text="Little money or training is needed and there are few rules."),
            S("Conclusion", text="The informal sector grows because it is a way to survive when formal jobs are scarce."),
        ]),
        H("Common mistakes"),
        MISTAKE("Calling the informal sector illegal", "Most informal work is legal work that is simply not registered or fully taxed. It is not crime."),
        MISTAKE("Saying it is only a problem", "Give both importance and challenges. The sector gives work to millions of people while also creating problems."),
        MISTAKE("Using unsupported numbers", "Do not quote exact percentages unless you have them from your textbook. Say 'a large share of workers'."),
        QUIZ("Which of these is an example of the informal sector?",
             ["A bank branch with contracts for its staff", "A roadside motorbike taxi rider who owns his motorbike", "A big brewery's factory", "A government ministry"], 1,
             "A self-employed motorbike taxi rider is usually unregistered, uses little capital and is not fully taxed.",
             hint="Look for a small, self-employed activity.",
             feedback=["A bank is formal, with contracts and registered business.", "", "A brewery is a registered, large formal firm.", "A ministry is part of the government, which is formal."]),
        QUIZ("Which is a challenge of the informal sector for the country?",
             ["It creates jobs", "It trains apprentices", "The government loses tax income and workers have little protection", "It supplies cheap goods"], 2,
             "Unregistered firms pay little tax and workers have no insurance. Jobs, training and cheap goods are advantages.",
             hint="Choose the problem, not the benefit.",
             feedback=["Jobs are an advantage.", "Training is an advantage.", "", "Cheap goods are an advantage."]),
        H("Practice questions"),
        PQ("Define the informal sector.",
           "The informal sector is made up of small economic activities that are not officially registered, not fully taxed or regulated, use little capital and depend mainly on the owner's or family's labour."),
        PQ("Give three reasons why the informal sector has grown rapidly in Cameroon.",
           "Too few formal jobs for school-leavers; rural-urban migration into towns; low incomes and the need for extra income; easy entry with little capital. (Any three.)"),
        PQ("State two ways in which the informal sector is important to the economy.",
           "It provides jobs and income to many people; it supplies cheap goods and services; it trains apprentices; it links farmers to town consumers. (Any two.)"),
        PQ("Outline two problems of the informal sector.",
           "Workers have low and unstable income and no insurance or pension; the government loses tax; markets and motorbike taxis can cause congestion, rubbish and accidents. (Any two.)"),
        SUM("The informal sector is made up of small, mostly unregistered and lightly taxed activities such as petty trade, motorbike taxis and crafts.",
            "It has grown because of few formal jobs, urban growth, low incomes, easy entry and costly formal rules.",
            "It gives jobs and income, cheap goods, training and links between farms and towns.",
            "Its challenges include low and unsafe work, no protection, lost tax and congestion and rubbish in towns.",
            "Good answers give both importance and challenges and avoid made-up statistics."),
    ],
))


# ------------------------------------------------------------------ 4. Transport systems and distribution
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Transport systems in Cameroon: types, distribution and impact",
    slug="cmrdev-transport-systems-and-their-distribution",
    minutes=22,
    summary="The types of transport in Cameroon (road, rail, water, air, pipeline), how the networks are distributed on a sketch map, and their impact on the economy and the environment.",
    objectives=[
        "Identify the types of transport systems in Cameroon",
        "Illustrate the distribution of transport networks on a sketch map",
        "Explain why networks are dense in some areas and sparse in others",
        "Outline the impact of transport on the economy and the environment",
    ],
    key_concepts=["Road transport", "Railway", "Sea port", "Air transport", "Pipeline", "Transport network", "Landlocked country"],
    blocks=[
        H("Introduction"),
        T("A truck loaded with food crops leaves Bafoussam at dawn and reaches Douala the same day. A train carries goods from Yaounde "
          "towards Ngaoundere. A ship unloads at Douala port. A passenger flies from Douala to Yaounde in less than an hour. All of these are **transport**."),
        D("**Transport** is the movement of people and goods from one place to another. A **transport network** is the system of routes (roads, railways, "
          "waterways, air routes and pipelines) and the places they join.", title="Transport and transport network"),
        T("Transport is the blood system of an economy. Without it, farmers cannot reach markets and factories cannot receive raw materials."),
        IMG("f5g-cmrdev-transport-modes.svg", alt="Four boxes: road, rail, water and air transport and what each is used for", caption="Figure 1. Types of transport system."),
        H("Types of transport"),
        KEY("Transport systems in Cameroon", "Learn each type and one example.", cards=[
            ["Road", "The most used. National roads join towns such as Douala, Yaounde, Bafoussam, Bamenda, Bertoua, Ngaoundere, Garoua and Maroua. Many rural roads are not tarred. Motorbikes, taxis, buses and trucks use them."],
            ["Rail", "The main line runs from Douala to Yaounde and continues to Ngaoundere in the north. It carries heavy goods and passengers. Check your textbook for other lines."],
            ["Water", "Sea ports at Douala (the largest) and Kribi (a deep-sea port), and smaller ports. Rivers such as the Benue are used in some places, the Benue only in part of the year."],
            ["Air", "International airports at Douala and Yaounde, and airports in some regional towns such as Garoua. Check your textbook for the full list."],
            ["Pipeline", "The Chad to Cameroon oil pipeline carries oil from Chad to the coast near Kribi."],
        ]),
        T("Douala port also serves neighbouring countries without a sea coast, such as Chad and the Central African Republic. "
          "These countries are called **landlocked**. Trucks and the railway carry their goods through Cameroon."),
        H("Distribution of transport networks"),
        IMG("f5g-cmrdev-transport-map.svg", alt="Simplified sketch map of Cameroon with main roads, the railway from Douala to Ngaoundere, ports at Douala and Kribi and Yaounde marked as a capital with an airport",
            caption="Figure 2. Main transport routes (simplified). Roads and railways are not spread evenly. Simplified sketch map, not to scale."),
        T("**Dense networks:** the south-west and the centre, around Douala, Yaounde, Bafoussam and Bamenda. Here there are many towns, "
          "a large population, ports, farms and industries.\n\n"
          "**Sparse networks:** the East, the far north and the forest areas of the south-east. Here the population is smaller, "
          "the forest is thick or the land is dry, and there are few industries.\n\n"
          "**Main axes:** Douala to Yaounde, Douala to the western highlands (Bafoussam and Bamenda), Yaounde to Bertoua and the east, "
          "and Yaounde to Ngaoundere and the north by rail and road. Routes radiate from Douala and Yaounde."),
        KEY("Why networks are dense or sparse", "Use these factors in an explanation.", cards=[
            ["Population and economic activity", "Where people and industries are many, demand for transport is high and routes are built."],
            ["Relief and rivers", "Mountains, swamps and big rivers make roads costly to build."],
            ["Climate and vegetation", "Heavy rain damages roads, and dense forest is hard to clear."],
            ["Government policy and money", "Roads are built first to link the main towns, ports and resources."],
        ]),
        H("Impact on the economy and the environment"),
        T("**Economic impact (positive).** Transport lets farmers sell food in towns, factories receive raw materials, and exports leave through Douala "
          "and Kribi. It creates jobs for drivers, mechanics, porters and traders. It lowers prices by reducing delays and food loss. "
          "It brings people to schools, hospitals and tourist sites.\n\n"
          "**Environmental impact (negative).** Roads clear forest and farmland. Vehicles produce smoke and noise, especially in cities. Oil spills and ship waste "
          "can pollute water. Construction can cause erosion and flooding. New roads can open forests to illegal logging and hunting.\n\n"
          "**Reducing harm:** plan routes with care, plant trees along roads, keep vehicles in good order, and control spills."),
        EX("Model answer 1: describe a distribution", intro="Describe the distribution of transport networks in Cameroon.", steps=[
            S("Draw", text="Sketch the outline of Cameroon with the coast in the south-west. Mark Douala, Yaounde and Ngaoundere. Draw the main roads and the railway, with a key. Write 'Simplified sketch map, not to scale'."),
            S("Pattern", text="Networks are dense in the south-west and centre and sparse in the east and the far north."),
            S("Main routes", text="Douala to Yaounde, Douala to Bafoussam and Bamenda, and Yaounde to Ngaoundere by road and rail. Douala and Kribi are the sea ports."),
            S("Explain", text="Dense networks match dense population and industry. Forest and low population in the east keep roads few."),
        ]),
        EX("Model answer 2: impact", intro="Outline the impact of transport on the economy and the environment of Cameroon.", steps=[
            S("Economy", text="It carries food to markets, raw materials to factories and exports to ports. It creates jobs and lowers prices."),
            S("Environment", text="Road building clears forest and causes erosion. Vehicles cause air pollution and noise. Spills can pollute water."),
            S("Balance", text="Good planning keeps the benefits and reduces the harm."),
        ]),
        H("Common mistakes"),
        MISTAKE("Drawing a map with too much detail", "Use the outline, a few towns, and only the routes you are sure of. Add a key and the words 'sketch map, not to scale'."),
        MISTAKE("Listing types without examples", "After each type, give a Cameroonian example, such as the Douala to Yaounde railway or the port of Kribi."),
        MISTAKE("Only positive effects", "Transport also harms the environment. Give both."),
        QUIZ("Which is a deep-sea port on the south coast of Cameroon?",
             ["Maroua", "Kribi", "Bamenda", "Garoua"], 1,
             "Kribi is a deep-sea port on the coast. Maroua, Bamenda and Garoua are inland towns.",
             hint="Pick the coastal town.",
             feedback=["Maroua is in the Far North, inland.", "", "Bamenda is a highland town, inland.", "Garoua is on the Benue, inland."]),
        QUIZ("Why are road and rail networks sparse in the East and the far north?",
             ["They are the main industrial areas", "They have smaller populations, thick forest or dry land and few industries", "They have no towns at all", "They are next to the sea"], 1,
             "Few people and industries, and difficult forest or dry land, mean less demand and higher cost.",
             hint="Think of demand for transport and the cost of building.",
             feedback=["The main industrial areas are Douala and Yaounde.", "", "There are towns, such as Bertoua and Maroua.", "They are inland."]),
        H("Practice questions"),
        PQ("Name four types of transport in Cameroon.",
           "Road, rail, water (sea ports and rivers), air and pipeline."),
        PQ("Describe the distribution of the main roads and railways of Cameroon.",
           "Dense in the south-west and centre around Douala, Yaounde, Bafoussam and Bamenda. The railway runs from Douala to Yaounde and on to Ngaoundere. Networks are sparse in the east and far north."),
        PQ("Give two reasons why transport networks are dense in the south-west and centre.",
           "More people and industries; main ports and cities; easier relief for roads; more government investment. (Any two.)"),
        PQ("Outline two negative effects of transport on the environment.",
           "Forest and land are cleared for roads; air pollution and noise from vehicles; oil spills and erosion. (Any two.)"),
        SUM("Cameroon has road, rail, water, air and pipeline transport. Roads carry most traffic.",
            "Douala and Kribi are the main sea ports. The main railway links Douala, Yaounde and Ngaoundere.",
            "Networks are dense in the south-west and centre and sparse in the east and the far north.",
            "Density depends on population, industry, relief, climate, vegetation and money.",
            "Transport boosts trade and jobs but can pollute and clear land."),
    ],
))

# ------------------------------------------------------------------ 5. Problems of transport and measures
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Transport problems in Cameroon and government measures",
    slug="cmrdev-problems-of-transport-and-government-measures",
    minutes=20,
    summary="The main problems of the transport sector in Cameroon and the measures taken to improve roads, railways, ports, air transport and traffic safety.",
    objectives=[
        "Identify the problems of the transport sector in Cameroon",
        "Explain how these problems affect the economy and people",
        "Describe government measures to improve transport",
        "Link each problem to a suitable measure",
    ],
    key_concepts=["Road maintenance", "Congestion", "Overloading", "Road safety", "Rehabilitation", "Feeder road", "Port efficiency"],
    blocks=[
        H("Introduction"),
        T("In the rainy season a farmer far from the main road may find the way to market closed by mud. Fruit rots in the truck, and "
          "prices at the market rise. In Douala at rush hour, traffic is slow and passengers are late."),
        T("These pictures show the problems of the **transport sector**. In this lesson we identify them and describe the measures to improve transport."),
        IMG("f5g-cmrdev-transport-problems.svg", alt="Five problems of transport matched with five measures", caption="Figure 1. Problems of transport and matching measures."),
        H("Problems of the transport sector"),
        KEY("Main problems", "Always give the effect after the problem.", cards=[
            ["Poor roads", "Many roads are not tarred and become muddy or flooded in the rainy season. Potholes damage vehicles. Maintenance is often late."],
            ["Overloading", "Heavy trucks damage road surfaces and cause accidents."],
            ["Old, slow railway", "Trains can be slow and the network is small. Freight and passengers lose time."],
            ["Traffic congestion", "In Douala and Yaounde, many vehicles and motorbike taxis crowd narrow roads. Journeys are slow and the air is polluted."],
            ["Accidents", "Bad roads, speeding and old vehicles cause crashes and deaths."],
            ["Port and checkpoint delays", "Waiting for goods to clear port and many stops on the road raise costs."],
            ["High costs", "Fuel, spare parts and fares are costly, which raises the price of goods."],
        ]),
        T("The effects are serious. Food crops from isolated villages rot before they reach markets. Factories pay more for raw materials. "
          "Tourists find sites hard to reach. Landlocked neighbours that use Douala also pay more."),
        H("Government measures"),
        T("The government, with partners, uses several measures. For names and dates of projects, check your textbook."),
        KEY("Measures", "Match each to a problem.", cards=[
            ["Build and repair roads", "Tar main roads, build bridges and repair feeder roads that link villages to markets."],
            ["Road maintenance funds", "Money from road users and the budget is used to maintain roads regularly."],
            ["Control overloading", "Weighbridges check trucks so that heavy loads do not destroy roads."],
            ["Improve rail", "Rehabilitate tracks, buy engines and wagons and speed up journeys."],
            ["Develop ports", "Build the deep-sea port at Kribi and improve handling at Douala."],
            ["Urban transport", "Widen roads, build bypasses and flyovers, and organise buses and taxis to ease congestion."],
            ["Safety rules and training", "Driving tests, vehicle checks, speed limits and awareness campaigns."],
            ["Air transport", "Maintain airports and encourage airlines to link towns and other countries."],
        ]),
        TIP("In answers, name a measure and then say which problem it reduces and how. Example: 'Weighbridges stop overloading, so roads last longer.'"),
        T("Not all problems are solved. Money is limited, and projects can be slow. Local communities can help by clearing drains and "
          "reporting damage. Private firms can build and run roads or ports under agreements with the state."),
        EX("Model answer 1", intro="Identify four problems of the transport sector in Cameroon.", steps=[
            S("Poor roads", text="Many roads are untarred and become muddy and flooded in the rainy season."),
            S("Overloading", text="Heavy trucks break road surfaces and cause accidents."),
            S("Congestion", text="Many vehicles crowd Douala and Yaounde, causing delays and pollution."),
            S("Accidents", text="Bad roads, speeding and old vehicles cause crashes."),
        ]),
        EX("Model answer 2", intro="Describe the measures taken by the government to improve transport in Cameroon.", steps=[
            S("Introduction", text="Say that transport is vital and that several measures exist."),
            S("Roads", text="Building and tarring roads, repairing feeder roads and keeping up maintenance funds."),
            S("Control of overloading and safety", text="Weighbridges, vehicle checks and traffic rules reduce damage and accidents."),
            S("Rail and ports", text="Rehabilitating the railway and developing the deep-sea port of Kribi and handling at Douala."),
            S("Cities", text="Bypasses, flyovers and better bus services reduce congestion."),
            S("Conclusion", text="These measures lower costs and move goods and people faster, but money and upkeep remain challenges."),
        ]),
        H("Common mistakes"),
        MISTAKE("Naming projects you are not sure of", "If you are unsure of the name or date of a project, describe the type of measure instead. Do not invent names."),
        MISTAKE("Blaming only one cause", "Problems also come from weather, relief, overloading and a lack of funds. Give a balanced view."),
        MISTAKE("Measures without the problem they solve", "Link each measure to its problem so the answer shows reasoning."),
        QUIZ("Which measure directly reduces damage caused by overloaded trucks?",
             ["Building hotels", "Using weighbridges", "Planting trees", "Opening more banks"], 1,
             "Weighbridges check the weight of trucks and stop overloaded vehicles.",
             hint="Which measure checks the weight of trucks?",
             feedback=["Hotels are unrelated.", "", "Trees do not stop overloading.", "Banks are unrelated."]),
        QUIZ("Why is the deep-sea port at Kribi important for the transport sector?",
             ["It reduces pressure on Douala and can take larger ships", "It replaces all roads", "It is an inland river port", "It is used only by tourists"], 0,
             "A deep-sea port can handle larger ships and shares the work of Douala, speeding up trade.",
             hint="Think of what deep-sea allows.",
             feedback=["", "A port does not replace roads.", "Kribi is on the coast.", "It is a commercial port as well."]),
        H("Practice questions"),
        PQ("State three problems of the transport sector in Cameroon.",
           "Poor and flooded roads, overloading, traffic congestion, accidents, an old and slow railway, port delays. (Any three.)"),
        PQ("Explain how poor feeder roads affect farmers.",
           "Farm products cannot reach markets quickly or at all in the rainy season, so food rots, farmers earn less and prices rise in towns."),
        PQ("Describe two measures that reduce traffic congestion in a city such as Douala.",
           "Build bypasses and flyovers; widen roads; organise bus services and taxis; regulate motorbike taxis. (Any two.)"),
        PQ("Give two ways in which the development of the Kribi deep-sea port helps the economy.",
           "It handles larger ships and reduces pressure on Douala; it speeds up imports and exports; it creates jobs and encourages industry nearby. (Any two.)"),
        SUM("Main problems: poor roads, overloading, an old railway, congestion, accidents, port delays and high costs.",
            "Effects: rotting food, high prices, delays, lost lives and pollution.",
            "Measures: road building and maintenance, control of overloading, rail and port development, urban schemes and safety rules.",
            "Link each measure to the problem it solves.",
            "Do not invent project names; describe measures and check your textbook for specifics."),
    ],
))

# ------------------------------------------------------------------ 6. Tourism potentials and factors
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Tourism in Cameroon: potentials and favourable factors",
    slug="cmrdev-tourism-potentials-and-factors",
    minutes=20,
    summary="The tourist potentials of Cameroon (mountains, coast, waterfalls, wildlife, culture), where they are found, and the factors that encourage tourism.",
    objectives=[
        "Outline and locate the tourist potentials of Cameroon",
        "Identify the factors encouraging the development of tourism",
        "Sketch a map showing selected tourist sites",
        "Give examples of natural and cultural attractions",
    ],
    key_concepts=["Tourism", "Tourist potential", "Natural attractions", "Cultural attractions", "National park", "Accessibility"],
    blocks=[
        H("Introduction"),
        T("Cameroon is often called 'Africa in miniature' because it has beaches, mountains, forests, savanna and dry Sahel, "
          "and many cultures in one country. This variety is a great asset for tourism."),
        D("**Tourism** is travelling to places away from home for leisure, adventure, culture or rest, and the services that support it "
          "(hotels, transport, guides and food).", title="Tourism"),
        D("A **tourist potential** is a natural or human feature that can attract visitors, whether or not it is yet well developed.", title="Tourist potential"),
        H("Tourist potentials and where they are found"),
        IMG("f5g-cmrdev-tourism-map.svg", alt="Simplified sketch map of Cameroon with Mount Cameroon, Limbe, Kribi beaches and Lobe falls, and Waza National Park marked",
            caption="Figure 1. Some tourist sites. Simplified sketch map, not to scale."),
        KEY("Natural attractions", "Learn at least one example from each group.", cards=[
            ["Mountains and volcano", "Mount Cameroon, the highest peak and an active volcano near Buea and Limbe. Hikers climb it, and an annual mountain race is held on it. The Mandara mountains in the Far North and the western highlands are also scenic."],
            ["Coast and beaches", "Limbe has beaches on the coast near Mount Cameroon, and Kribi has sandy beaches. The Lobe falls near Kribi tumble close to the ocean, which is a rare sight."],
            ["Wildlife and parks", "Waza National Park in the Far North is known for savanna animals such as elephants. Forest reserves in the south and east protect rainforest species; Korup and Dja are examples (check your textbook for their exact locations)."],
            ["Lakes and rivers", "Lake Chad in the far north and crater lakes in the highlands. Check your textbook for names."],
        ]),
        KEY("Cultural attractions", "Human features that also attract visitors.", cards=[
            ["Palaces and chiefdoms", "The palaces and museums of the western highlands, for example in Foumban, with their art and history."],
            ["Festivals and traditions", "Dances, masquerades, crafts and local food in the grassfields and elsewhere."],
            ["Towns and markets", "Markets, craft villages and city life in Douala, Yaounde and Bamenda."],
        ]),
        T("Different regions offer different attractions: the coast for beach and water sport, the highlands for scenery and culture, "
          "and the north for wildlife and landscapes. Check your textbook for further regional examples."),
        H("Factors encouraging the development of tourism"),
        KEY("Favourable factors", "Use a factor, then a Cameroon example.", cards=[
            ["Varied physical features", "Mountains, beaches, falls and parks offer different types of tourism."],
            ["Wildlife and forests", "National parks and reserves attract nature lovers."],
            ["Culture and welcome", "Many cultures, crafts, festivals and friendly people."],
            ["Peace in most areas", "Visitors travel where they feel safe."],
            ["Transport and accommodation", "International airports at Douala and Yaounde, roads to main sites, and hotels in main towns."],
            ["Government policy", "A ministry in charge of tourism, protected parks and promotion of the country."],
            ["Two official languages", "English and French help visitors from many countries."],
        ]),
        TIP("Tourism is a service (tertiary) industry. It brings foreign exchange, which helps the country pay for goods bought abroad."),
        EX("Model answer 1", intro="Outline four tourist potentials of Cameroon and locate each.", steps=[
            S("Mount Cameroon", text="A high volcano near Buea and Limbe in the South-West, popular with hikers."),
            S("Kribi beaches and Lobe falls", text="Sandy beaches and falls near the ocean on the south coast."),
            S("Limbe", text="A coastal town with beaches, west of Douala, close to Mount Cameroon."),
            S("Waza National Park", text="A savanna park in the Far North with elephants and other animals."),
        ]),
        EX("Model answer 2", intro="Identify the factors that encourage the development of tourism in Cameroon.", steps=[
            S("Natural attractions", text="Varied relief, coast, falls and wildlife give many types of tourism."),
            S("Cultural wealth", text="Palaces, festivals and crafts attract cultural visitors."),
            S("Facilities", text="International airports, roads and hotels make travel easier."),
            S("Policy and peace", text="Government promotion, protected parks and general peace attract visitors."),
        ]),
        H("Common mistakes"),
        MISTAKE("Listing attractions without a location", "Say where each site is: Mount Cameroon in the South-West, Waza in the Far North, Kribi on the south coast."),
        MISTAKE("Forgetting cultural attractions", "Tourism is not only nature. Include palaces, festivals, crafts and markets."),
        MISTAKE("Inventing sites", "If you are unsure of a site's name or place, use the ones you are sure of and add a general description."),
        QUIZ("Where is Waza National Park found?",
             ["In the Far North of Cameroon", "On the south coast", "In the western highlands", "In Douala city"], 0,
             "Waza National Park is in the Far North, a savanna region with large wildlife.",
             hint="It is a savanna park in the north.",
             feedback=["", "The south coast has beaches and the Lobe falls.", "The western highlands have crater lakes and palaces.", "Douala is a port city."]),
        QUIZ("Which features are found near Kribi?",
             ["Mount Cameroon", "Lobe falls and sandy beaches", "Waza National Park", "Mandara mountains"], 1,
             "The Lobe falls and the beaches are near Kribi on the coast.",
             hint="Choose a coastal attraction.",
             feedback=["Mount Cameroon is near Buea and Limbe.", "", "Waza is in the Far North.", "The Mandara mountains are in the Far North."]),
        H("Practice questions"),
        PQ("Name four tourist sites in Cameroon and say where each is found.",
           "Mount Cameroon (South-West, near Buea); Limbe (coast, South-West); Kribi beaches and Lobe falls (south coast); Waza National Park (Far North)."),
        PQ("State two cultural attractions of Cameroon.",
           "Palaces and museums (for example in Foumban), festivals and dances, crafts and traditional food. (Any two.)"),
        PQ("Give three factors that encourage tourism in Cameroon.",
           "Varied natural attractions; cultural diversity; international airports and hotels; government policy; general peace and two official languages. (Any three.)"),
        PQ("Explain why Mount Cameroon is a tourist potential.",
           "It is the highest mountain and an active volcano, offering climbs and views, and it is near Buea and Limbe, which have accommodation and links to Douala."),
        SUM("Cameroon has varied natural and cultural attractions in one country.",
            "Examples: Mount Cameroon, Limbe, Kribi beaches, Lobe falls, Waza National Park, palaces and festivals.",
            "Factors: varied relief and wildlife, culture, airports and hotels, government policy and peace.",
            "Locate each site and give its type.",
            "Draw a simple sketch map with a key for full marks."),
    ],
))


# ------------------------------------------------------------------ 7. Constraints and impact of tourism
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Tourism in Cameroon: constraints, impact and efforts to develop it",
    slug="cmrdev-constraints-and-impact-of-tourism",
    minutes=22,
    summary="The constraints to tourism development in Cameroon, its impact on the economy and the environment, and the efforts of the government and other stakeholders to develop it.",
    objectives=[
        "Describe the constraints to tourism development in Cameroon",
        "Describe the impact of tourism on the economy and the environment",
        "Describe the efforts of the government and other stakeholders",
        "Give a balanced answer using positive and negative effects",
    ],
    key_concepts=["Constraint", "Foreign exchange", "Multiplier effect", "Seasonal employment", "Sustainable tourism", "Stakeholder", "Conservation"],
    blocks=[
        H("Introduction"),
        T("A visitor who wants to see the Lobe falls or climb Mount Cameroon needs a way to get there, a place to sleep, a guide and "
          "a feeling of safety. Where any of these is missing, the visitor may choose another country."),
        T("This lesson looks at what holds tourism back in Cameroon, what tourism does to the economy and the environment, "
          "and what is being done. Remember the lesson on potentials: Cameroon has the attractions, but it has not fully used them."),
        H("Constraints to tourism development"),
        KEY("Main constraints", "Each constraint should be followed by its effect.", cards=[
            ["Poor access", "Many tourist sites are reached by roads that are bad in the rainy season, and air tickets are costly. Visitors lose time and money."],
            ["Too few facilities", "Hotels, restaurants and clean toilets are few outside the big towns, and quality varies. Visitors may not stay long."],
            ["Limited promotion", "Cameroon is less known abroad than some other African destinations, so fewer tourists come."],
            ["Skills shortage", "Not enough trained guides, hotel staff and managers."],
            ["Security worries", "Visitors avoid areas that are reported as unsafe, and reports of insecurity in some regions also affect the whole country's image."],
            ["Health and procedures", "Visitors need vaccinations and visas, which are costly and slow."],
            ["Poor site management", "Litter, poaching and lack of money harm parks and trails."],
            ["Weak power and water supply", "Hotels must run generators and may lack water."],
        ]),
        T("Seasonal factors also matter. Rain can close roads and hide the views on Mount Cameroon, so visitors cluster in the dry season."),
        H("Impact of tourism"),
        IMG("f5g-cmrdev-tourism-impact.svg", alt="Four boxes showing positive and negative effects of tourism on the economy and the environment",
            caption="Figure 1. Impact of tourism on the economy and the environment."),
        T("**Positive economic effects.** Tourists spend money on hotels, food, transport, guides and crafts. This creates jobs and incomes. "
          "Visitors from abroad bring **foreign exchange**. The government earns taxes. Local farmers and craft makers find new customers. "
          "This is called the **multiplier effect**, because each franc spent passes through many hands.\n\n"
          "**Negative economic effects.** Many tourism jobs are seasonal and low-paid. Prices of land, food and rooms may rise for local people. "
          "Some profits leave the area if hotels or tour firms belong to outside owners. A country that depends on tourism suffers when visitors stay away.\n\n"
          "**Positive environmental effects.** Income from tourism pays for parks, rangers and conservation. It gives communities a reason to protect forests, wildlife and "
          "scenery.\n\n"
          "**Negative environmental effects.** Litter and waste, trampled trails on mountains, damaged beaches, noise and disturbed wildlife. Building hotels and roads can clear forest. "
          "Poaching and the trade in animal products can be linked to demand from visitors."),
        KEY("Sustainable tourism", "Tourism that brings benefits now without harming sites for future visitors.", cards=[
            ["Manage numbers", "Limit visitors to fragile sites and keep them on marked paths."],
            ["Involve communities", "Local people guide, sell crafts and share income, so they protect the site."],
            ["Control waste", "Collect rubbish, treat sewage and ban hunting and taking of wildlife."],
        ]),
        H("Efforts by the government and other stakeholders"),
        T("A **stakeholder** is a person or group with an interest in tourism. In Cameroon these include the government, private hotel owners, tour "
          "operators, airlines, local communities and conservation groups."),
        KEY("What is being done", "Give at least one effort of the government and one of another stakeholder.", cards=[
            ["Government", "The ministry in charge of tourism plans and promotes tourism, classifies hotels and supports training. The state protects national parks and reserves, builds roads and airports, and promotes the country at fairs and in other countries."],
            ["Private sector", "Hotel owners, restaurants, travel agencies and airlines invest in rooms and tours and create jobs."],
            ["Communities", "Local people run guide services, craft markets, festivals and community-managed reserves."],
            ["Conservation groups and partners", "Non-governmental organisations such as WWF and international partners support the protection of parks and train rangers. Check your textbook for the details."],
        ]),
        EX("Model answer 1", intro="Describe three constraints to the development of tourism in Cameroon.", steps=[
            S("Poor access", text="Bad roads and costly flights make some sites hard and expensive to reach."),
            S("Few facilities", text="There are few good hotels and services outside the big towns, so visitors stay for a short time."),
            S("Skills and promotion", text="Few trained guides and limited advertising abroad mean fewer visitors."),
        ]),
        EX("Model answer 2", intro="Describe the impact of tourism on the economy and the environment of Cameroon.", steps=[
            S("Economy (positive)", text="Jobs, income, taxes and foreign exchange; markets for farmers and craft makers."),
            S("Economy (negative)", text="Seasonal jobs, rising prices and profits that may leave the area."),
            S("Environment (positive)", text="Money for parks and a reason to protect nature."),
            S("Environment (negative)", text="Litter, damaged trails, disturbed wildlife and forest cleared for buildings."),
            S("Conclusion", text="Good planning and sustainable tourism keep the gains and reduce the harm."),
        ]),
        H("Common mistakes"),
        MISTAKE("Giving only one side", "The question says 'impact': give both positive and negative effects, for the economy and for the environment."),
        MISTAKE("Mixing impact and constraints", "A constraint holds tourism back (poor roads). An impact is what tourism causes (jobs, litter)."),
        MISTAKE("Vague efforts", "Do not write 'the government helps'. Say how: protects parks, trains guides, builds airports, promotes the country."),
        QUIZ("Which is a constraint to tourism development?",
             ["Beautiful scenery", "Poor roads to tourist sites", "Friendly people", "Many attractions"], 1,
             "Poor access makes visits difficult. The other options are advantages.",
             hint="Choose the one that holds tourism back.",
             feedback=["Scenery is a strength.", "", "Friendly people help tourism.", "Many attractions help tourism."]),
        QUIZ("Which is a positive environmental effect of tourism?",
             ["Litter on beaches", "Money that pays for park rangers and conservation", "Damaged mountain trails", "Disturbed wildlife"], 1,
             "Income from tourism can fund parks and protection. The others are negative effects.",
             hint="Choose the benefit to nature.",
             feedback=["Litter is harmful.", "", "Damaged trails are harmful.", "Disturbed wildlife is harmful."]),
        H("Practice questions"),
        PQ("State three constraints to tourism development in Cameroon.",
           "Poor roads and access; few hotels and services; limited promotion; shortage of skilled guides and staff; security worries; poor site management. (Any three.)"),
        PQ("Explain how tourism can benefit the economy of Cameroon.",
           "It creates jobs, brings foreign exchange and tax income, and gives markets to farmers and craft makers. The money passes through many hands (the multiplier effect)."),
        PQ("Describe two harmful effects of tourism on the environment.",
           "Litter and waste on beaches and mountains; trampled trails and erosion; disturbed wildlife; forest cleared for hotels and roads. (Any two.)"),
        PQ("Outline two efforts made by stakeholders to develop tourism.",
           "The government protects parks, builds airports and roads and promotes the country. Private firms build hotels and run tours. Communities run guides and craft markets. Conservation groups support parks. (Any two.)"),
        SUM("Constraints: poor access, few facilities, limited promotion, skills gaps, security worries, health and visa procedures and weak site management.",
            "Impact on the economy: jobs, income, foreign exchange and taxes, but also seasonal work, rising prices and leakage of profits.",
            "Impact on the environment: funds for conservation, but also litter, damaged sites and disturbed wildlife.",
            "Stakeholders include the government, hotel owners, tour firms, airlines, communities and conservation groups.",
            "A balanced answer gives positive and negative effects and says what is being done."),
    ],
))

# ------------------------------------------------------------------ 8. Reasons for slow economic growth
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Why economic growth is slow despite great potential",
    slug="cmrdev-reasons-for-slow-economic-growth",
    minutes=22,
    summary="The reasons why Cameroon's economic growth has been slower than its potential suggests: dependence on raw materials, weak infrastructure and energy, limited capital and skills, management problems and other constraints.",
    objectives=[
        "Describe Cameroon's economic potentials",
        "Describe the reasons for slow economic growth despite these potentials",
        "Explain how the constraints are linked",
        "Write a balanced answer without taking sides",
    ],
    key_concepts=["Economic growth", "Potential", "Primary exports", "Infrastructure", "Debt", "Value added", "Constraint"],
    blocks=[
        H("Introduction"),
        T("Cameroon has fertile soils, forests, fish, oil and minerals, hydroelectric rivers, ports and many tourist sites. "
          "It is called a country of great potential. Yet many families still live on low incomes, and growth has been slow compared with the country's resources."),
        D("**Economic growth** is an increase in the total goods and services that a country produces over time. It is usually measured by the rise in the "
          "**GDP** (gross domestic product), and for people's living standards by the rise in GDP per person.", title="Economic growth"),
        D("**Potential** is what a country could produce and earn if it used its resources fully.", title="Potential"),
        IMG("f5g-cmrdev-growth-constraints.svg", alt="Two columns: potentials of Cameroon on the left and constraints on the right, with slower growth between them",
            caption="Figure 1. Great potential and the constraints that slow growth."),
        H("Potentials in brief"),
        T("From the course: farming in several climate zones (cocoa, coffee, cotton, bananas, food crops); forests and fish; oil and some minerals; "
          "rivers for hydroelectric power such as the Sanaga; the ports of Douala and Kribi; tourist sites; and a young population. Lesson by lesson, you have seen how each can be developed."),
        H("Reasons for slow growth"),
        T("There is no single reason. Several causes combine. Learn them as groups."),
        KEY("Economic reasons", "Linked to what the country produces and sells.", cards=[
            ["Dependence on raw materials", "Cameroon exports mainly raw products such as crude oil, cocoa, timber and cotton. Their prices on world markets rise and fall, so earnings are unstable. Little value is added at home."],
            ["Weak industry", "Manufacturing is small, so the country imports many finished goods and loses jobs and income."],
            ["Limited capital and debt", "Savings and investment are low. Money used for debt repayment cannot be used for roads or schools."],
            ["Small and low-income market", "Many people have little to spend, so firms cannot grow easily."],
        ]),
        KEY("Infrastructure and skills", "Linked to services that firms and people need.", cards=[
            ["Weak transport", "Poor roads, an old railway and port delays raise costs and isolate farms."],
            ["Power shortages", "Cuts and weak supply in many areas stop factories and raise costs."],
            ["Skills gaps", "Too few trained technicians and managers, and many graduates without jobs."],
            ["Health and education problems", "Illness such as malaria reduces working time and school attendance."],
        ]),
        KEY("Management and other reasons", "State these calmly and factually, not as accusations.", cards=[
            ["Management and rules", "Where funds are badly managed, rules are weakly enforced or projects are delayed, the benefits of investment are reduced. Check your textbook for the details."],
            ["Large informal sector", "Many activities are small and unregistered, so productivity and tax income are low."],
            ["Population growth", "Fast population growth puts pressure on jobs, schools and health services."],
            ["Climate and environmental risks", "Droughts and floods hurt farmers, and deforestation and pollution harm resources."],
            ["Regional and world events", "Falling world prices, global crises, and insecurity in some areas and in neighbouring countries can reduce trade and investment."],
        ]),
        TIP("Group the reasons into economic, infrastructure and skills, and management and other reasons. Then give a short example for each group."),
        T("These reasons are linked. Power cuts weaken industry. Weak industry keeps the country exporting raw materials. Raw materials have unstable prices. "
          "Unstable prices make saving and investing difficult. This is a cycle that is hard to break, but it can be broken, as you will see in the next lesson."),
        EX("Model answer 1", intro="Describe the reasons for the slow economic growth of Cameroon despite her potentials.", steps=[
            S("Introduction", text="Cameroon has fertile soils, forests, oil, hydropower and ports. Growth is nevertheless slower than the potential suggests."),
            S("Dependence on raw materials", text="Mainly crude oil, cocoa, timber and cotton are exported unprocessed. World prices change, so earnings are unstable and little value is added."),
            S("Weak infrastructure", text="Poor roads, an old railway and power shortages raise costs and cut output."),
            S("Skills and capital", text="Few trained workers and limited investment hold back industry."),
            S("Other reasons", text="Management weaknesses, a large informal sector, fast population growth and climate risks add to the problem."),
            S("Conclusion", text="The reasons are linked, so growth needs several actions together."),
        ]),
        EX("Model answer 2: a simple calculation", intro="In an exercise with imaginary numbers, a country's output rises from 200 units to 210 units in a year while its population rises by 3 percent. Is output per person rising or falling, and what is the growth rate of output?", steps=[
            S("Growth of output", math=r"\frac{210 - 200}{200} \times 100 = 5\%"),
            S("Compare with population", text="Output grew 5 percent and the population 3 percent."),
            S("Conclusion", text="Output per person is rising, but only by a little (about 2 percent). Slow growth can be cancelled out by fast population growth."),
        ]),
        H("Common mistakes"),
        MISTAKE("Blaming one cause", "Do not write that the whole problem is due to the government, or to colonial history, or to the weather. Give a balanced mix of causes."),
        MISTAKE("Quoting precise statistics", "Do not quote exact figures for GDP or debt unless your textbook gives them. Say 'slow' or 'unstable'."),
        MISTAKE("Listing without explaining", "'Poor roads' is a label. Add what it does: 'raises costs and isolates farmers'."),
        QUIZ("Which reason explains why export earnings are unstable?",
             ["Cameroon exports mainly raw materials whose world prices rise and fall", "Cameroon has too many hydroelectric dams", "Cameroon has too many manufactured exports", "Cameroon has no ports"], 0,
             "Raw materials such as oil, cocoa and timber change in price on world markets, so earnings change too.",
             hint="Think of prices of raw materials on the world market.",
             feedback=["", "Dams supply electricity and do not make export earnings unstable.", "Manufactured exports are limited, not too many.", "Douala and Kribi are sea ports."]),
        QUIZ("Which is an example of a link between constraints?",
             ["Power cuts raise costs, which makes local factories lose to imports", "Roads make rain heavier", "Education lowers population", "Tourism closes ports"], 0,
             "Power cuts raise costs, weakening industry and keeping the country exporting raw materials.",
             hint="Look for a cause and its effect on firms.",
             feedback=["", "Roads do not affect rainfall.", "This is not the link described.", "Tourism does not close ports."]),
        H("Practice questions"),
        PQ("Define economic growth.",
           "Economic growth is an increase in the total goods and services produced by a country over time, usually measured by the rise in GDP."),
        PQ("State four reasons for the slow economic growth of Cameroon.",
           "Dependence on raw material exports with unstable prices; weak infrastructure (roads, rail, power); shortage of skills and capital; weak manufacturing; management weaknesses; a large informal sector; fast population growth. (Any four.)"),
        PQ("Explain how dependence on raw materials slows growth.",
           "Raw materials sell at low prices that change on world markets, so earnings are unstable. Little value is added at home, so fewer jobs and less income are created than from processing."),
        PQ("Explain why poor transport and power cuts together make it hard for factories to compete.",
           "Poor transport raises the cost of raw materials and delivery. Power cuts stop machines and force firms to buy generators. Together they raise costs, so local goods cost more than imports."),
        SUM("Cameroon has great potential in farming, forests, minerals, energy, ports and tourism.",
            "Growth is slow because of many linked causes.",
            "Economic causes: dependence on raw materials, weak industry, limited capital and debt, and a small market.",
            "Infrastructure and skills causes: poor transport, power shortages, skills gaps, health and education problems.",
            "Other causes: management weaknesses, a large informal sector, fast population growth, climate risks and outside events. Be balanced and avoid invented figures."),
    ],
))

# ------------------------------------------------------------------ 9. Measures to uplift the economy
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Measures to uplift the economy towards emergence",
    slug="cmrdev-measures-to-uplift-the-economy",
    minutes=22,
    summary="Possible measures to lift Cameroon's economy towards emergence: processing raw materials, energy, transport, skills, diversification, investment, tourism, good management and regional trade, linked to the sectors in the course.",
    objectives=[
        "Explain the idea of emergence",
        "Identify measures that can uplift the economy towards emergence",
        "Link each measure to a resource or sector studied in the course",
        "Write a structured, balanced essay answer",
    ],
    key_concepts=["Emergence", "Diversification", "Value added", "Industrialisation", "Investment", "Regional integration", "Sustainable development"],
    blocks=[
        H("Introduction"),
        T("In the last lesson we saw why growth is slow. This lesson looks forward. What can Cameroon do to move towards **emergence**?"),
        D("**Emergence** is the stage at which a country has moved from low income and heavy dependence on raw materials towards a stronger, more varied "
          "economy with more industry and services, higher incomes shared among more people, and better living standards.", title="Emergence"),
        T("Cameroon's long-term plan aims at emergence in the coming years (check your textbook for the name of the plan and the target date). "
          "Whatever the plan, geography shows which measures are logical."),
        IMG("f5g-cmrdev-emergence.svg", alt="Six boxes (farming and forests, energy and minerals, manufacturing, transport and ports, tourism, skills and good rules) all pointing to emergence",
            caption="Figure 1. Measures that link sectors towards emergence."),
        H("Measures, linked to the sectors in the course"),
        KEY("Measures", "Each one is linked to a resource, sector or problem from this course.", cards=[
            ["Add value to farm, forest and fish products", "Process cocoa, coffee, cotton, timber and fish at home instead of exporting them raw. This creates jobs and earns more per tonne. Improve farming with better seeds, storage, credit and climate-smart methods."],
            ["Develop energy", "Build more hydroelectric and solar plants and power lines so that homes and factories have steady electricity. Use the rivers for multi-purpose projects."],
            ["Use minerals and oil wisely", "Process minerals where possible, use income from oil and minerals to build roads, schools and industry, and protect the environment."],
            ["Build industry", "Support agro-processing, wood, textile and building-material industries. Industrial zones near ports and power make factories cheaper to run."],
            ["Improve transport", "Repair and extend roads and rail, link farms to markets, and develop the ports of Douala and Kribi, so that goods move cheaply."],
            ["Promote tourism", "Improve roads, hotels, guides and promotion, and manage sites sustainably so that tourism earns foreign exchange and protects nature."],
        ]),
        KEY("Measures for people, rules and trade", "These help all sectors.", cards=[
            ["Education and skills", "Expand technical and vocational training, link schools to industry, and improve health so that people can work well."],
            ["Good management and a good business climate", "Use public money well, apply rules fairly, simplify taxes and procedures and protect property. This attracts investment."],
            ["Help small firms and the informal sector", "Offer credit, training and simple registration so that small firms grow and join the formal economy."],
            ["Diversify the economy", "Depend on many products and services, not on a few raw materials, so that falls in the price of one do not harm the whole economy."],
            ["Regional and international trade", "Trade with neighbours in regional groups such as CEMAC and in African trade agreements, to enlarge the market for Cameroonian goods."],
            ["Protect the environment", "Manage forests, soils and water so that growth can continue for future generations. This is sustainable development."],
        ]),
        T("These measures work together. Power and roads make factories cheaper to run. Factories need skilled workers. Skilled workers earn more and "
          "buy more, which enlarges the market. A bigger market encourages investment."),
        TIP("In an essay, link each measure to the problem it solves from the previous lesson, and name a resource from the course. Use 'because' and 'so' to show cause and effect."),
        EX("Model answer 1", intro="Identify the measures that can uplift the economy of Cameroon towards emergence.", steps=[
            S("Introduction", text="Emergence means a stronger, more varied economy with higher shared incomes. Several measures are needed."),
            S("Processing and industry", text="Process cocoa, cotton, timber and fish at home. This adds value and creates jobs."),
            S("Energy and transport", text="Expand hydroelectric and solar power and improve roads, rail and ports so that costs fall."),
            S("People and rules", text="Train workers and improve the management of funds and the business climate to attract investors."),
            S("Diversify and trade", text="Develop tourism and services, support small firms, and trade within regional groups."),
            S("Conclusion", text="Measures must work together and protect the environment so that growth is lasting."),
        ]),
        EX("Model answer 2", intro="Explain how developing hydroelectric power can help Cameroon move towards emergence.", steps=[
            S("Cause", text="Cameroon has large rivers such as the Sanaga, and hydropower is renewable and cheaper than imported fuel."),
            S("Industry", text="Steady power lets factories run without generators and attracts industries such as aluminium smelting, as at Edea."),
            S("People", text="Electricity in villages helps schools, clinics and small businesses."),
            S("Risks", text="Dams need money and can affect people and rivers, and low water in the dry season can reduce supply, so planning and other sources such as solar are needed."),
            S("Conclusion", text="Well-planned hydropower lowers costs and supports growth."),
        ]),
        H("Common mistakes"),
        MISTAKE("Listing without links", "Do not list 'build roads, build schools' only. Show how each measure helps growth."),
        MISTAKE("Ignoring the course", "Use examples from the course: cocoa, timber, the Sanaga, Douala, Kribi, Mount Cameroon and the informal sector."),
        MISTAKE("Promising quick results", "Emergence is long-term. Say that it needs time, money and good management."),
        QUIZ("Which measure adds value to Cameroon's cocoa and timber?",
             ["Exporting them unprocessed", "Processing them in local factories before export", "Burning the trees", "Stopping production"], 1,
             "Processing makes more valuable products and creates jobs at home.",
             hint="Think of chocolate and planks.",
             feedback=["Unprocessed exports earn less per tonne.", "", "Burning trees destroys a resource.", "Stopping production loses income."]),
        QUIZ("Why does diversification help an economy?",
             ["It makes the country depend on one product", "It reduces the effect of a price fall in any single product", "It removes all risk", "It stops trade"], 1,
             "With many products and services, a fall in one price does not harm the whole economy.",
             hint="Think of not putting all eggs in one basket.",
             feedback=["That is the opposite of diversification.", "", "Risk is reduced, not removed.", "Diversification does not stop trade."]),
        H("Practice questions"),
        PQ("What is meant by emergence?",
           "Emergence is the stage when a country has a stronger, more varied economy with more industry and services, higher incomes shared among more people and better living standards."),
        PQ("Give four measures that can uplift the economy of Cameroon.",
           "Process raw materials at home; develop energy; improve roads, rail and ports; train skilled workers; promote tourism; support small firms; improve management; trade within regional groups. (Any four.)"),
        PQ("Explain how improving transport can help the economy to grow.",
           "Good roads, rail and ports lower the cost and time of moving goods, link farms to markets, bring raw materials to factories and bring tourists to sites, so output and income rise."),
        PQ("Explain why processing raw materials in Cameroon is better than exporting them raw.",
           "Processed goods sell at higher prices, create jobs and give factories business. Exports become less dependent on the unstable prices of raw materials."),
        SUM("Emergence means a stronger, more varied economy with higher, shared incomes.",
            "Measures: processing raw materials, energy, industry, transport, tourism, skills, good management, support for small firms, diversification, regional trade and environmental care.",
            "Each measure answers a problem from the previous lesson and uses a resource from the course.",
            "Measures work best together and take time.",
            "In an essay, name the measure, explain how it helps, and give a Cameroonian example."),
    ],
))
