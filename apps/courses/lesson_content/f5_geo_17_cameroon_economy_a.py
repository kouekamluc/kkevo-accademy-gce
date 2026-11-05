"""Form 5 Geography: Geography of Cameroon, Economic development potentials, part A
(agriculture; forest, fish, mineral and energy resources; multipurpose river development).
Six lessons, one practice set each."""

from .dsl import *  # noqa: F403

COURSE = ("geography", "form-5")

MODULE = "The Geography of Cameroon"
TOPIC = "Economic development potentials"

LESSONS = []

# ------------------------------------------------------------------ 1. Systems and types of agriculture
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Systems and types of agriculture in Cameroon",
    slug="cmreco-agriculture-systems-and-types",
    minutes=22,
    summary="The systems (subsistence and commercial) and types (food crops, cash crops, plantations, smallholdings, livestock and fishing) of agriculture in Cameroon, where each is found and what characterises it.",
    objectives=[
        "Identify the systems and types of agriculture found in Cameroon",
        "Outline the characteristics of subsistence and commercial farming",
        "Describe where plantations, smallholdings, livestock rearing and fishing are found",
        "Distinguish food crops from cash crops using Cameroonian examples",
    ],
    key_concepts=["Agriculture", "Subsistence farming", "Commercial farming", "Food crop", "Cash crop", "Plantation", "Smallholding", "Livestock rearing", "Fishing"],
    blocks=[
        H("Introduction"),
        T("Walk through a market in Mbouda, Bafoussam or Mokolo and you will see the result of farming: plantain, cassava, "
          "maize, beans, onions, vegetables and fish. Drive through Tiko or Njombe and you will see long rows of bananas "
          "and oil palms. Go north and you will see herds of cattle and fields of cotton and millet."),
        T("Farming is the main activity of a very large share of Cameroonians. It gives food, jobs and money. But farming is "
          "not the same everywhere. This lesson shows the **systems** and **types** of agriculture in Cameroon."),
        D("**Agriculture** is the growing of crops and the rearing of animals for human use. In this course it also includes "
          "fishing, which is the catching or breeding of fish.", title="Agriculture"),
        H("Two systems of agriculture"),
        T("A **system** of farming is the way the whole farm is organised: why the farmer produces, how much land and money "
          "is used, and where the produce goes. There are two main systems."),
        D("**Subsistence farming** is farming in which the farmer grows food mainly to feed their own family. Only a small "
          "surplus is sold.", title="Subsistence farming"),
        D("**Commercial farming** is farming in which crops or animals are produced mainly to be sold, for profit, in "
          "local, national or foreign markets.", title="Commercial farming"),
        KEY("Subsistence or commercial?", "Compare the two systems.", cards=[
            ["Subsistence", "Small farms. Family labour. Simple tools such as the hoe and cutlass. Mixed crops. Little money or machinery. Low yields."],
            ["Commercial", "Larger farms. Hired workers. More capital, fertiliser and machines. One main crop. Produce sold for money. Higher yields."],
        ], note="Many Cameroonian farmers do both: they eat part of the harvest and sell the rest."),
        H("Types of agriculture"),
        T("A **type** of agriculture is what is produced and how. The main types in Cameroon are food crop farming, cash crop "
          "farming, plantation farming, smallholder farming, livestock rearing and fishing."),
        D("**Food crops** are grown mainly to be eaten. Examples: cassava, plantain, maize, yams, cocoyams, groundnuts, beans, "
          "millet and sorghum. Rice and Irish potatoes are also grown in several regions.", title="Food crops"),
        D("**Cash crops** are grown mainly to be sold, often for export. Examples: cocoa, coffee, cotton, bananas, rubber, "
          "oil palm and tea.", title="Cash crops"),
        IMG("f5g-cmreco-farming-zones-map.svg",
            alt="Simplified sketch map of Cameroon showing five farming zones: north, Adamawa plateau, southern forest zone, western highlands and coastal plantations, with Lake Chad, Mount Cameroon, main towns and two dams",
            caption="Figure 1. Main farming zones of Cameroon. Simplified sketch map, not to scale."),
        T("Look at Figure 1. Farming follows climate and relief. The hot, wet south has forest and tree crops. The cooler "
          "western highlands have coffee and many food crops. The drier north has cotton, millet, sorghum and cattle."),
        KEY("Plantations and smallholdings", "Both grow cash crops, but they are very different.", cards=[
            ["Plantation", "A very large estate that grows one crop and employs many workers, often with a factory on site. Examples: bananas, rubber, oil palm and tea. The Cameroon Development Corporation (CDC) in the South-West is a well-known example."],
            ["Smallholding", "A small family farm, often under a few hectares. Cocoa and coffee are mainly grown by smallholders in the Centre, South, South-West, Littoral, West and North-West regions."],
        ]),
        T("Cotton is grown mainly in the north by many small farmers. A company buys it and processes it. Sugar cane is grown "
          "on large estates in the Centre region. Rice is grown with irrigation in the far north, for example on the "
          "Logone floodplain near Yagoua."),
        T("**Livestock rearing** is the keeping of animals such as cattle, goats, sheep, pigs and poultry. Large herds of "
          "cattle are kept on the grasslands of the Adamawa plateau, the North-West highlands and the north, mostly by "
          "herders who move their animals in search of pasture. Poultry and pigs are common near towns."),
        T("**Fishing** is done in the Atlantic Ocean near Limbe, Douala and Kribi, in Lake Chad and in rivers and lakes "
          "across the country. Most fishing is done by small canoes (artisanal fishing). Fish ponds (fish farming) are a "
          "growing activity. Fish are an important cheap source of protein."),
        H("Worked examples"),
        EX("Model answer 1: contrasting two systems", intro="Distinguish between subsistence farming and commercial farming, with an example of each in Cameroon.", steps=[
            S("Define subsistence farming", text="Subsistence farming is farming mainly to feed the farmer's family, with only a small surplus sold."),
            S("Give its features and an example", text="It uses family labour, small plots and simple tools. Example: a family in the West region growing maize, beans and cocoyams on a small plot for its own food."),
            S("Define commercial farming", text="Commercial farming is farming mainly to sell the produce for profit."),
            S("Give its features and an example", text="It uses large areas, hired workers, machines and fertiliser. Example: the banana plantations of the Moungo area, or the CDC rubber and oil palm estates."),
            S("Conclude with the main difference", text="The main difference is the purpose of production: eating (subsistence) or selling (commercial)."),
        ]),
        EX("Model answer 2: describing the types in one area", intro="Describe the types of farming found in the northern part of Cameroon.", steps=[
            S("Point: crops", text="The north is drier, so farmers grow millet, sorghum, maize and groundnuts for food, and cotton as a cash crop."),
            S("Evidence", text="Cotton is grown by many small farmers and bought by a company that processes it. Irrigated rice is grown on the Logone floodplain."),
            S("Point: livestock", text="Cattle, goats and sheep are reared on open grassland and herded to find pasture, especially in the dry season."),
            S("Point: fishing", text="Fishing takes place in Lake Chad and in the rivers, mainly with canoes and nets."),
            S("Link to climate", text="Short rainy seasons and long dry seasons suit grain crops, cotton and grazing better than tree crops such as cocoa."),
        ]),
        MISTAKE("Saying food crops are never sold", "Food crops are grown mainly for the family, but any surplus is sold in the market. Maize and plantain are sold in towns. The difference is the main purpose, not the only use."),
        MISTAKE("Saying cash crops cannot be eaten", "Bananas and sugar can be eaten. A crop is a cash crop because it is mainly grown to be sold. Always say 'mainly'."),
        MISTAKE("Mixing up plantation and smallholding", "A plantation is one very large estate with many workers. A smallholding is a small family farm. Cocoa can be grown on both, but in Cameroon it is mainly a smallholder crop."),
        TIP("Exam link: this topic appears in Paper 1 (multiple choice on Cameroon) and in Paper 2 Section D (Geography of Cameroon). "
            "A good answer gives the type, the place, the crop and a characteristic. Use a sketch map of Cameroon with a few labels.", title="Exam link"),
        QUIZ("Which of these is a cash crop grown mainly on plantations in Cameroon?",
             ["Cassava", "Rubber", "Plantain", "Beans"], 1,
             "Rubber is grown on large plantations and sold. Cassava, plantain and beans are mainly food crops.",
             hint="Which crop is processed in a factory and exported?",
             feedback=["Cassava is mainly a food crop eaten by families.", "", "Plantain is mainly a food crop.", "Beans are mainly a food crop."]),
        QUIZ("Which statement best describes subsistence farming?",
             ["Large estates with machines selling to foreign markets", "Farming mainly to feed the farmer's family", "Keeping only cattle", "Catching fish only in the sea"], 1,
             "Subsistence farming is mainly to feed the farmer's family.",
             hint="Think of the word 'subsist', which means to survive.",
             feedback=["That describes commercial or plantation farming.", "", "Cattle rearing is one type of farming, not the definition of subsistence.", "That describes sea fishing."]),
        PQ("Define a plantation and name two plantation crops grown in Cameroon.",
           "A plantation is a very large farm that grows one crop, uses many workers and often has a factory on the estate. Two plantation crops in Cameroon are bananas, rubber, oil palm and tea (any two)."),
        PQ("Name two food crops and two cash crops grown in Cameroon.",
           "Food crops: cassava, plantain, maize, yams, beans, millet or sorghum (any two). Cash crops: cocoa, coffee, cotton, bananas, rubber, oil palm or tea (any two)."),
        PQ("Describe livestock rearing in the north and Adamawa areas of Cameroon.",
           "Cattle, sheep and goats are kept on open grassland. Herders move the animals in search of pasture and water, especially in the dry season. The animals give meat, milk and hides and are sold in livestock markets. The Adamawa plateau is a cool grassland area suited to cattle."),
        PQ("Give two characteristics of commercial farming.",
           "It is done on a large scale with hired labour. It uses capital, machines, fertiliser and improved seeds. The produce is mainly sold for profit (any two)."),
        SUM("Agriculture means growing crops, rearing animals and fishing.",
            "Subsistence farming feeds the family; commercial farming produces to sell.",
            "Food crops are mainly eaten; cash crops are mainly sold.",
            "Plantations are huge single-crop estates; smallholdings are small family farms.",
            "Climate and relief decide where each type is found: tree crops in the south, coffee in the highlands, cotton, grain and cattle in the north.",
            "Fishing and livestock rearing are also important types of agriculture."),
    ],
))

# ------------------------------------------------------------------ 2. Factors, problems and impact of agriculture
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Agriculture in Cameroon: factors, problems, impact and efforts",
    slug="cmreco-factors-problems-and-impact-of-agriculture",
    minutes=24,
    summary="Why Cameroon's farming can succeed (climate, soils, labour, markets, ports), the main problems and strategies to solve them, farming's impact on the economy, and the efforts of government and other organisations to raise production.",
    objectives=[
        "Describe the factors favouring agriculture in Cameroon",
        "Outline the main problems of agriculture and strategies to solve them",
        "Describe the impact of agriculture on the economy of Cameroon",
        "Describe efforts by the government and other organisations to boost agricultural production",
    ],
    key_concepts=["Physical factors", "Human and economic factors", "Agricultural problems", "Climate-smart agriculture", "Extension services", "Food security", "Export earnings"],
    blocks=[
        H("Introduction"),
        T("Cameroon is sometimes called 'Africa in miniature' because it has forest, highland, savanna and Sahel zones in one country. "
          "That variety lets farmers grow almost every tropical crop. Yet many farmers still earn little, and the country still "
          "imports some food. Why?"),
        T("This lesson looks at four questions: what helps farming, what holds it back, how farming helps the economy, and what is "
          "being done to improve it."),
        H("Factors favouring agriculture"),
        KEY("Physical factors", "These come from nature.", cards=[
            ["Climate", "The hot, wet south suits cocoa, oil palm and plantain. The cooler highlands suit coffee, tea and Irish potatoes. The drier north suits cotton, millet and cattle."],
            ["Soils", "Fertile volcanic soils on the slopes of Mount Cameroon and in the western highlands give good yields. Alluvial soils along rivers are also fertile."],
            ["Relief and water", "Flat land on the Logone floodplain suits irrigated rice. Many rivers give water for irrigation and fish."],
        ]),
        KEY("Human and economic factors", "These come from people and organisations.", cards=[
            ["Labour", "A large and young rural population provides workers."],
            ["Markets", "Growing towns such as Douala and Yaoundé need food. Foreign buyers want cocoa, coffee, bananas and cotton."],
            ["Transport and ports", "Roads, the railway and the ports of Douala and Kribi help produce reach markets and export."],
            ["Support", "Government policy, research and farmer training help production."],
        ]),
        H("Main problems and strategies"),
        T("Farming faces many problems. Each problem has a possible strategy to solve it. Figure 2 shows some of the most important pairs."),
        IMG("f5g-cmreco-problems-strategies.svg",
            alt="Six problems of agriculture on the left, each with an arrow to a strategy on the right: roads, pests, credit, small farms, climate and storage",
            caption="Figure 2. Problems of agriculture and strategies to solve them."),
        T("**Poor roads.** In the rainy season many farm roads are muddy or cut. Produce rots before it reaches the market. "
          "Strategy: build and maintain rural roads."),
        T("**Pests, diseases and low yields.** Old cocoa and coffee trees, pests and plant diseases reduce harvests. Strategy: "
          "research on better seeds, spraying, and advice from agricultural officers (extension services)."),
        T("**Lack of money (credit) and inputs.** Many farmers cannot buy fertiliser, seeds or tools. Strategy: loans from "
          "microfinance institutions and banks, farmers' co-operatives, and cheaper inputs."),
        T("**Small farms and old tools.** Hoes and cutlasses give low output. Land is often divided into small pieces. "
          "Strategy: training, simple machines such as ploughs and mills, and better organisation in groups."),
        T("**Climate problems and soil loss.** Droughts in the north, floods, and bush burning damage crops and soils. "
          "Strategy: **climate-smart agriculture**."),
        D("**Climate-smart agriculture** is farming that raises yields in a lasting way, helps farmers adapt to climate change "
          "and, where possible, reduces greenhouse gases. Examples: drought-resistant seeds, planting trees among crops "
          "(agroforestry), mulching, rainwater harvesting and crop rotation.", title="Climate-smart agriculture"),
        T("**Poor storage, processing and markets.** Much food is lost after harvest, and farmers often sell at low prices. "
          "Strategy: stores, drying and processing, and better access to markets (see the lesson on food loss and waste). "
          "Other problems include falling world prices for export crops, young people leaving farming for towns, "
          "competition for land between crop farmers and herders, and insecurity in some areas."),
        H("Impact on the economy"),
        T("Agriculture is one of the most important sectors of Cameroon's economy. Its impacts include these."),
        KEY("Economic impact of agriculture", "Main points for an exam answer.", cards=[
            ["Employment", "It employs a large share of the population, especially in rural areas."],
            ["Food supply", "It feeds the population and reduces the need for imports."],
            ["Export earnings", "Cocoa, coffee, cotton, bananas, rubber and timber earn foreign money."],
            ["Raw materials", "Cotton, oil palm, sugar cane and rubber supply factories."],
            ["Income and tax", "Farm incomes and taxes support rural families and government spending."],
        ], note="Do not quote statistics unless your textbook gives them. Say 'a large share' or 'one of the largest'."),
        T("There are also costs. Clearing forest for farms causes deforestation. Depending on a few export crops makes the "
          "economy sensitive to world price changes."),
        H("Efforts to boost production"),
        T("The government works through ministries such as the Ministry of Agriculture and Rural Development (MINADER) and the "
          "Ministry of Livestock, Fisheries and Animal Industries (MINEPIA). Research is carried out by institutions such as "
          "the Institute of Agricultural Research for Development (IRAD)."),
        T("Government efforts include training and advice for farmers, improved seeds and planting material, building rural "
          "roads, help to form co-operatives and farmer groups, support for processing, and state or semi-state bodies for "
          "particular crops such as cotton (SODECOTON) and the CDC plantations. For the names of recent national programmes, "
          "check your textbook."),
        T("Other organisations also help. The Food and Agriculture Organization of the United Nations (FAO) and international "
          "research centres such as IITA, which has a station near Yaoundé, give technical help. Development partners, banks, "
          "microfinance institutions and non-governmental organisations (NGOs) give training, loans and equipment."),
        H("Worked examples"),
        EX("Model answer 1: problems and solutions", intro="Outline three problems faced by farmers in Cameroon and suggest a solution to each.", steps=[
            S("Problem 1 and solution", text="Poor roads make it hard to carry produce to market and cause rotting. The government and councils can build and repair rural roads."),
            S("Problem 2 and solution", text="Lack of credit stops farmers buying fertiliser and seeds. Microfinance, banks and co-operatives can give loans and share buying costs."),
            S("Problem 3 and solution", text="Pests and old trees reduce yields. Research bodies such as IRAD and extension workers can supply better seeds and teach pest control."),
            S("Conclusion", text="Solving these problems would raise yields, incomes and food supply."),
        ]),
        EX("Model answer 2: impact on the economy", intro="Describe the importance of agriculture to the economy of Cameroon.", steps=[
            S("Employment", text="Agriculture gives work to a large share of Cameroonians, especially in villages, so it reduces unemployment."),
            S("Food and import saving", text="It supplies food to towns and markets, which reduces the amount of food that must be bought from abroad."),
            S("Exports", text="Cocoa, coffee, bananas, cotton and rubber earn foreign exchange and taxes for government."),
            S("Industry", text="Cotton, oil palm, sugar cane and rubber are raw materials for factories, so farming links to manufacturing."),
            S("Balance", text="But depending on a few crops makes incomes unstable when world prices fall."),
        ]),
        MISTAKE("Listing without explaining", "Writing 'roads, pests, credit' earns few marks. Say what the problem does (produce rots) and give a matching solution."),
        MISTAKE("Giving only government efforts", "The syllabus asks for efforts by the government AND other organisations such as FAO, NGOs, banks and farmer co-operatives."),
        MISTAKE("Using invented figures", "Do not quote percentages or tonnes unless you are sure. 'A large share' is safer than a wrong number."),
        TIP("Exam link: expect this topic in Paper 2 Section D as an essay ('Describe the problems of agriculture in Cameroon and suggest solutions') and in Paper 1 as multiple choice. "
            "Use the pattern: problem, effect, solution.", title="Exam link"),
        QUIZ("Which is a physical factor favouring agriculture in Cameroon?",
             ["A large rural labour force", "Fertile volcanic soils near Mount Cameroon", "The port of Douala", "Government training programmes"], 1,
             "Soils come from nature, so they are a physical factor. The others are human or economic factors.",
             hint="Physical factors come from nature, not from people.",
             feedback=["Labour is a human factor.", "", "A port is built by people, so it is a human or economic factor.", "Training is a human or government factor."]),
        QUIZ("Climate-smart agriculture means",
             ["farming only in the dry season", "farming that raises yields, adapts to climate change and, where possible, cuts emissions", "growing only export crops", "using more land by clearing forest"], 1,
             "Climate-smart agriculture links higher output, adaptation and lower emissions.",
             hint="It has three goals: output, adaptation, emissions.",
             feedback=["The season is not what makes farming climate-smart.", "", "The crops grown do not define it.", "Clearing forest can increase emissions and damage the environment."]),
        PQ("State three factors that favour agriculture in Cameroon.",
           "Varied climates that suit many crops; fertile volcanic and alluvial soils; a large labour force; growing markets in towns; ports such as Douala and Kribi for export; government and research support (any three)."),
        PQ("Outline three problems of agriculture in Cameroon and one way of solving each.",
           "Poor roads - build rural roads. Pests and disease - research and better seeds. Lack of credit - microfinance and co-operatives. Small farms and old tools - training and simple machines. Drought and soil loss - climate-smart farming (any three with solutions)."),
        PQ("Describe three ways in which agriculture contributes to the economy of Cameroon.",
           "It gives jobs to many people, feeds the population, earns foreign exchange from export crops such as cocoa, coffee and cotton, supplies raw materials to factories, and gives incomes and taxes (any three, explained)."),
        PQ("Name two organisations other than the government that help to improve agriculture and say what they do.",
           "FAO gives technical help and advice. IITA does research. Microfinance institutions give loans. NGOs train farmers and give equipment. Co-operatives help farmers sell and buy together (any two with their role)."),
        SUM("Physical factors: varied climates, fertile soils, flat land and water. Human factors: labour, markets, transport and support.",
            "Main problems: poor roads, pests, lack of credit, small farms and old tools, climate hazards, storage and market problems.",
            "Each problem has a strategy: roads, research, loans, training, climate-smart methods, stores and processing.",
            "Agriculture gives jobs, food, exports, raw materials and income, but has environmental costs.",
            "Efforts come from government (ministries, IRAD, extension) and others (FAO, IITA, banks, NGOs, co-operatives)."),
    ],
))

# ------------------------------------------------------------------ 3. Food loss and food waste
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Food loss and food waste in Cameroon",
    slug="cmreco-food-loss-and-food-waste",
    minutes=20,
    summary="The difference between food loss and food waste, their causes and consequences, and practical solutions in Cameroon: storage, roads, markets, processing and household habits.",
    objectives=[
        "Differentiate between food loss and food waste",
        "Outline the causes of food loss and food waste in Cameroon",
        "Outline the consequences of food loss and food waste",
        "Outline possible solutions to food loss and food waste",
    ],
    key_concepts=["Food loss", "Food waste", "Food chain", "Post-harvest loss", "Food security", "Processing", "Storage"],
    blocks=[
        H("Introduction"),
        T("A farmer near Bafoussam harvests a big crop of tomatoes. The road to the city market is bad, there is no cold store, "
          "and the sun is hot. By the time the tomatoes arrive, many are soft and cannot be sold. Another family in a town "
          "cooks too much rice and throws the left-overs away."),
        T("Both stories are about food that was grown but never eaten. Geographers give them two different names."),
        D("The **food chain** is the series of steps through which food passes: farm, storage, transport, processing, market "
          "and household.", title="Food chain"),
        IMG("f5g-cmreco-food-loss-vs-waste.svg",
            alt="A chain of six boxes: farm, storage, transport, processing, market, household. The first four are marked food loss and the last two food waste.",
            caption="Figure 3. Food loss happens early in the food chain; food waste happens at the end."),
        H("Food loss and food waste"),
        D("**Food loss** is food that is lost or spoiled between harvest and the shop, during harvesting, storage, transport and "
          "processing. It is mainly caused by weak systems.", title="Food loss"),
        D("**Food waste** is good food that is thrown away by retailers (shops and markets), restaurants and households. It is "
          "mainly caused by choices and habits.", title="Food waste"),
        T("In many poorer countries, including Cameroon, much of the problem is food loss early in the chain. In richer "
          "countries, more is wasted at the end of the chain. Do not mix the two terms in the exam."),
        H("Causes in Cameroon"),
        KEY("Causes of food loss", "Early in the chain.", cards=[
            ["Poor storage", "Damp, pests (weevils, rats) and moulds destroy maize, beans and groundnuts. Fruit and fish spoil quickly without cooling."],
            ["Bad roads and transport", "Slow, rough journeys damage soft produce such as tomatoes, plantain and fruit."],
            ["Little processing", "Without drying, smoking or canning, fresh produce cannot be kept."],
            ["Market problems", "At harvest time there is too much supply and not enough buyers, so produce is left to rot."],
        ]),
        KEY("Causes of food waste", "Late in the chain.", cards=[
            ["Retail and market", "Unsold food is thrown away when it goes bad, or because it does not look perfect."],
            ["Households and events", "Cooking too much, buying too much, forgetting food at the back of the store cupboard, and left-overs from parties."],
        ]),
        H("Consequences"),
        T("Food loss and waste cause several problems."),
        KEY("Consequences", "What happens when food is lost or wasted.", cards=[
            ["Less food", "Less food is available for people, which reduces food security and can raise prices."],
            ["Lost income", "Farmers and traders lose money. Poor families lose the most."],
            ["Wasted resources", "The land, water, labour, fertiliser and fuel used to grow and move the food are wasted too."],
            ["Environment", "Rotting food on dumps gives off methane, a greenhouse gas. More land may be cleared to replace the lost food."],
        ]),
        H("Possible solutions"),
        T("**For food loss:** build or improve stores (dry, clean, protected from pests), use sealed bags or crates, dry grain and "
          "fish well, repair rural roads, organise co-operatives and market information, and add value by processing: for example, "
          "cassava into gari, tomatoes into paste, fish smoked in improved kilns. Solar dryers and small cold rooms also help."),
        T("**For food waste:** plan meals and shopping lists, store food correctly, use left-overs, share extra food, turn peels "
          "and scraps into animal feed or compost, and teach people about the problem in schools and markets."),
        T("**Everyone can help.** Government, NGOs, farmers, traders and families all have a role."),
        H("Worked examples"),
        EX("Model answer 1: differentiate", intro="Differentiate between food loss and food waste.", steps=[
            S("Define food loss", text="Food loss is food that is lost or spoiled between harvest and the shop: at the farm, in storage, in transport or in processing."),
            S("Define food waste", text="Food waste is edible food thrown away at the shop, restaurant or home."),
            S("Give an example of each", text="Loss: maize that rots in a damp store after harvest. Waste: a family throwing away cooked rice that nobody ate."),
            S("State the main difference", text="Loss happens early in the chain and is mostly caused by poor systems. Waste happens late and is caused by habits and choices."),
        ]),
        EX("Model answer 2: causes and solutions", intro="Tomato farmers in a rural area of Cameroon lose a large part of each harvest. Explain the causes and suggest solutions.", steps=[
            S("Cause: poor transport", text="Rough roads and slow vehicles crush the soft tomatoes before they reach the market."),
            S("Cause: no storage", text="Without cold stores or shade, tomatoes spoil quickly in the heat."),
            S("Cause: too much supply", text="Everyone harvests at the same time, prices fall and unsold tomatoes rot."),
            S("Solutions", text="Repair roads, use strong crates, build shaded or cooled stores, and form a co-operative to find buyers."),
            S("Add value", text="Make tomatoes into paste or dried slices, which keep for months and sell all year."),
        ]),
        MISTAKE("Using food loss and food waste as the same thing", "Loss is early in the chain (farm to shop). Waste is at the shop or in the home. Define both clearly."),
        MISTAKE("Blaming only households", "In Cameroon, much food is lost before it reaches the household, because of storage, roads and processing. Do not forget the supply chain."),
        TIP("Exam link: this is NEW in the revised syllabus. Expect a Paper 1 multiple-choice question on the definitions or causes, "
            "and a Paper 2 Section D part-question on causes, consequences and solutions.", title="Exam link"),
        QUIZ("Maize rots in a damp store a month after harvest. This is",
             ["food waste", "food loss", "food processing", "food export"], 1,
             "It happens in storage before the food reaches the shop, so it is food loss.",
             hint="Where in the food chain does it happen?",
             feedback=["Waste is at the shop or in the home.", "", "Processing is making food into other products.", "Export is selling abroad."]),
        QUIZ("Which is a good solution to food waste at home?",
             ["Cook as much as possible every day", "Plan meals and use left-overs", "Build a new road", "Sell cassava at harvest"], 1,
             "Planning meals and using left-overs reduces food thrown away at household level.",
             hint="Waste at home is about habits.",
             feedback=["Cooking too much is a cause of waste.", "", "Roads help to reduce loss in transport, not household waste.", "Selling at harvest does not reduce waste at home."]),
        PQ("Differentiate between food loss and food waste.",
           "Food loss is food lost or spoiled between harvest and the shop, for example in storage or transport. Food waste is good food thrown away by shops, restaurants and households."),
        PQ("Give three causes of food loss in Cameroon.",
           "Poor storage (damp, pests, moulds); bad roads and slow transport; lack of processing; no cooling for fruit and fish; too much supply at harvest time (any three)."),
        PQ("Outline three consequences of food loss and food waste.",
           "Less food is available and food security falls; farmers and traders lose income; the resources used to grow the food are wasted; rotting food releases methane and may lead to more land clearing (any three)."),
        PQ("Suggest three ways of reducing food loss and food waste in Cameroon.",
           "Build better stores and use sealed bags; repair rural roads and use crates; process crops by drying, smoking or making paste; form co-operatives for markets; plan meals and use left-overs at home (any three)."),
        SUM("Food loss is food lost between harvest and the shop; food waste is food thrown away at the shop or home.",
            "In Cameroon, loss is mainly caused by poor storage, rough roads, little processing and market problems.",
            "Waste is caused by over-buying, over-cooking, unsold food and appearance standards.",
            "The consequences are less food, lost income, wasted resources and environmental harm.",
            "Solutions: better stores, roads and processing, co-operatives, and good habits at home."),
    ],
))

# ------------------------------------------------------------------ 4. Forest and fish resources
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Forest and fish resources of Cameroon",
    slug="cmreco-forest-and-fish-resources",
    minutes=22,
    summary="Where Cameroon's forest and fish resources are found, the challenges of using them, their impact on the economy and environment, and government efforts to manage them.",
    objectives=[
        "Illustrate the distribution of forest and fish resources in Cameroon",
        "Outline the challenges of exploiting forest and fish resources",
        "Describe the impact of their exploitation on the economy and the environment",
        "Describe government efforts to improve the management of forest and fish resources",
    ],
    key_concepts=["Dense equatorial forest", "Timber", "Non-timber forest products", "Artisanal fishing", "Fish farming", "Deforestation", "Overfishing", "Sustainable management"],
    blocks=[
        H("Introduction"),
        T("At the port of Douala, huge logs and sawn planks wait to be shipped abroad. At the beach in Limbe, fishermen pull "
          "their canoes ashore and women smoke fish over wood fires. Forests and waters are among the natural resources "
          "that Cameroon can use to develop."),
        T("A **natural resource** is something found in nature that people can use. Forest and fish are **renewable** "
          "resources: they can grow back, but only if they are used carefully."),
        D("A **renewable resource** is a resource that can replace itself naturally, such as trees and fish, if it is not used "
          "faster than it recovers.", title="Renewable resource"),
        H("Distribution of forest resources"),
        T("Dense equatorial forest covers much of the humid south of Cameroon: the South, East, Centre, Littoral and "
          "South-West regions. It is part of the great Congo Basin forest. Further north the forest thins into savanna."),
        IMG("f5g-cmreco-farming-zones-map.svg",
            alt="Simplified sketch map of Cameroon showing the southern forest zone in the south, the western highlands, the north and the Adamawa plateau, with Lake Chad, Mount Cameroon and the coast",
            caption="Figure 4. The forest zone lies in the south and east (zone 3 and the coast). Simplified sketch map, not to scale."),
        T("The forest gives **timber**: trees such as ayous (obeche), sapele and iroko are cut and sawn for furniture and "
          "building, and many logs and planks are exported through Douala. It also gives **non-timber forest products** such "
          "as fruits, honey, medicinal plants, rattan and bush foods. Forest areas include protected zones such as Korup "
          "National Park in the South-West and the Dja Faunal Reserve in the south-east."),
        H("Distribution of fish resources"),
        T("Fish are found in the Atlantic Ocean off the coast of Cameroon (near Limbe, Douala and Kribi), in the Wouri "
          "estuary and mangroves, in Lake Chad in the far north, and in rivers and reservoirs across the country, "
          "such as the Sanaga, the Benue and the lake behind the Lagdo dam."),
        T("Most fishing is **artisanal**: small canoes, nets and lines, with the catch sold fresh or smoked. A few "
          "companies use bigger boats called trawlers. **Fish farming** (aquaculture) in ponds is growing in several regions."),
        D("**Artisanal fishing** is small-scale fishing with simple canoes and gear, mainly by families and local "
          "communities. **Industrial fishing** uses big boats and modern equipment to catch large quantities.", title="Fishing types"),
        T("Fish is a cheap and important source of protein. Cameroon still imports a lot of frozen fish, which shows that "
          "local production does not meet demand."),
        H("Challenges of exploitation"),
        KEY("Challenges", "Problems faced in using forest and fish resources.", cards=[
            ["Forest", "Illegal logging. Poor roads inside the forest, which raise costs. Overcutting of valuable trees. Fires and clearing for farms. Conflicts with local communities who depend on the forest. Few sawmills, so many logs are exported unprocessed."],
            ["Fish", "Overfishing. Small-mesh nets that catch young fish. Poor storage and smoking, which waste fish. Few cold stores or landing sites. Pollution of waters. Cutting mangrove wood for smoking fish. Lake Chad has shrunk, reducing fish and fishing areas."],
        ]),
        H("Impact on the economy and environment"),
        IMG("f5g-cmreco-forest-gains-costs.svg",
            alt="Two columns: economic gains of forest exploitation (timber sales, jobs, taxes, food and medicine, farmland, village income) and costs (deforestation, soil erosion, habitat loss, illegal logging, less carbon storage, land conflicts)",
            caption="Figure 5. Gains and costs of exploiting the forest."),
        T("**Economic impact.** Timber is among Cameroon's important export products. Forestry and fishing provide jobs, "
          "incomes, food and taxes. Fish reduces hunger. Local fish production can reduce imports."),
        T("**Environmental impact.** Deforestation removes habitat for animals, leaves soil open to erosion and floods, and "
          "releases carbon dioxide. Overfishing reduces fish stocks. Cutting mangroves destroys breeding grounds for fish. "
          "Pollution damages rivers and the sea."),
        H("Government efforts to improve management"),
        T("The Ministry of Forestry and Wildlife (MINFOF) manages forests, and the Ministry of Livestock, Fisheries and "
          "Animal Industries (MINEPIA) looks after fishing. Efforts include these."),
        KEY("What the government does", "Main points for an exam answer.", cards=[
            ["Forest law and planning", "A forestry law sets rules on cutting, forest classification, management plans and taxes (check your textbook for the name and date)."],
            ["Protected areas", "National parks and reserves such as Korup and Dja protect forest and wildlife."],
            ["Community forests", "Villages can manage a forest for their own benefit."],
            ["Anti-illegal-logging", "Checking logging permits and transport, with help from partners."],
            ["Replanting and processing", "Tree planting and encouraging local sawmills to add value."],
            ["Fisheries rules", "Fishing licences, rules on net size, support for fish farming, training and fishing groups."],
        ]),
        H("Worked examples"),
        EX("Model answer 1: distribution and challenges of the forest", intro="Describe where the dense forest is found in Cameroon and outline two challenges of exploiting it.", steps=[
            S("Distribution", text="Dense equatorial forest covers the humid south and east: the South, East, Centre, Littoral and South-West regions, as part of the Congo Basin forest."),
            S("Resources", text="It provides timber such as ayous and sapele, which is exported through Douala, and products such as fruits, honey and medicine."),
            S("Challenge 1", text="Illegal logging: trees are cut without permits, so the government loses taxes and the forest is overcut."),
            S("Challenge 2", text="Poor roads inside the forest make it costly to bring logs out, and many logs are exported unprocessed, so Cameroon gains less money."),
        ]),
        EX("Model answer 2: effects of overfishing", intro="Explain the effects of overfishing in the coastal waters of Cameroon.", steps=[
            S("Define", text="Overfishing is catching fish faster than they can reproduce."),
            S("Effect on stocks", text="Fish become fewer and smaller. Fishermen need to travel further for lower catches."),
            S("Economic effect", text="Fishermen earn less and fish becomes more expensive, so the country imports more frozen fish."),
            S("Environmental effect", text="Small-mesh nets catch young fish, so the next generation is lost. Cutting mangroves for smoking fish destroys breeding grounds."),
            S("Solution", text="Licences, net-size rules and fish farming allow fishing to continue in a sustainable way."),
        ]),
        MISTAKE("Saying the forest is unlimited", "Forest and fish are renewable only if used carefully. Overuse turns them into depleted resources."),
        MISTAKE("Mentioning only benefits", "Questions on impact ask for the economy AND the environment, and usually expect both gains and costs."),
        MISTAKE("Confusing artisanal and industrial fishing", "Artisanal means small canoes and families. Industrial means big boats and companies."),
        TIP("Exam link: this topic comes in Paper 2 Section D (for example, 'Describe the distribution of forest resources in Cameroon and outline the challenges of exploiting them') "
            "and in Paper 1 multiple choice. Sketch a simple map of Cameroon and shade the forest zone.", title="Exam link"),
        QUIZ("In which part of Cameroon is dense equatorial forest mainly found?",
             ["The far north around Lake Chad", "The humid south and east", "The Mandara mountains", "The Logone floodplain"], 1,
             "Dense equatorial forest covers the humid south and east, part of the Congo Basin forest.",
             hint="Think of the hot, wet part of the country.",
             feedback=["The far north has a dry Sahel climate.", "", "The Mandara mountains are in the dry north.", "The Logone floodplain lies in the far north."]),
        QUIZ("Which is an environmental effect of deforestation?",
             ["Higher timber exports", "Soil erosion and loss of animal habitat", "More jobs in sawmills", "More taxes for government"], 1,
             "Removing trees exposes soil to erosion and destroys the habitat of animals.",
             hint="Choose the answer about nature, not money.",
             feedback=["This is an economic effect.", "", "This is an economic effect.", "This is an economic effect."]),
        PQ("Name two forest products and two fishing areas of Cameroon.",
           "Forest products: timber (ayous, sapele, iroko), fruits, honey, medicinal plants, rattan (any two). Fishing areas: the Atlantic coast near Limbe, Douala and Kribi; Lake Chad; rivers such as the Sanaga and Benue; reservoirs such as Lagdo (any two)."),
        PQ("Outline three challenges of exploiting forest resources in Cameroon.",
           "Illegal logging; poor roads in the forest that raise costs; overcutting of valuable trees; clearing for farms and fires; conflicts with local communities; logs exported without processing (any three)."),
        PQ("Describe two effects of exploiting forest resources on the environment.",
           "Deforestation destroys the habitat of animals and reduces biodiversity. Bare soil is eroded and floods are more likely. Less carbon dioxide is stored and more is released. Streams may dry up (any two explained)."),
        PQ("Describe three efforts made by the government to manage forest and fish resources.",
           "Forest laws and management plans; protected areas such as Korup and Dja; community forests; checking logging permits; tree planting; fishing licences and net-size rules; support for fish farming and training (any three)."),
        SUM("Dense forest covers the humid south and east; fish are found along the coast, in Lake Chad, rivers and reservoirs.",
            "Forest gives timber and other products; fishing is mostly artisanal and gives cheap protein.",
            "Challenges: illegal logging, poor roads, overfishing, poor storage, pollution and shrinking Lake Chad.",
            "Economic gains: jobs, exports, income and food. Environmental costs: deforestation, erosion and falling fish stocks.",
            "The government manages resources through ministries, laws, protected areas, community forests and fishing rules."),
    ],
))

# ------------------------------------------------------------------ 5. Mineral and energy resources
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Mineral and energy resources of Cameroon",
    slug="cmreco-mineral-and-energy-resources",
    minutes=24,
    summary="Where Cameroon's main mineral and energy resources are found (oil, gas, hydroelectric power, bauxite, iron ore and others), the challenges of exploiting them, their impact and the efforts to manage them.",
    objectives=[
        "Illustrate the distribution of mineral and energy resources in Cameroon",
        "Outline the challenges of exploiting these resources",
        "Describe the impact of their exploitation on the economy and the environment",
        "Describe government efforts to improve the management of these resources",
    ],
    key_concepts=["Mineral", "Non-renewable resource", "Petroleum", "Natural gas", "Hydroelectric power", "Bauxite", "Iron ore", "Biomass energy"],
    blocks=[
        H("Introduction"),
        T("When you switch on a light in Douala, the power often comes from water turning turbines on the Sanaga River. "
          "When a car fills up at a petrol station, the fuel may be made at the refinery in Limbe. Cameroon has many mineral and "
          "energy resources, but some are still waiting to be developed."),
        D("A **mineral** is a natural substance found in rocks that people can mine and use, such as bauxite and iron ore. An "
          "**energy resource** is a source of power, such as oil, gas, falling water and wood.", title="Minerals and energy"),
        D("A **non-renewable resource** (such as oil and iron ore) cannot be replaced once used up. A **renewable** resource "
          "(such as water for hydropower, sun and wood if replanted) can be used again.", title="Renewable and non-renewable"),
        H("Energy resources and where they are found"),
        T("**Oil (petroleum).** Oil is produced mainly offshore along the Atlantic coast, near the south-west coast. It is "
          "managed for the state by the National Hydrocarbons Corporation (SNH). A refinery at Limbe (SONARA) refines some of it. Oil from "
          "the Doba field in Chad also reaches the sea through a pipeline to a terminal near Kribi, and Cameroon earns fees. "
          "Oil production has fallen from its peak, so it must be managed carefully (check your textbook for current details)."),
        T("**Natural gas.** Gas is found in the Douala area (Logbaba) and offshore near the Kribi coast. It is used to make "
          "electricity and by industry."),
        T("**Hydroelectric power (HEP).** Cameroon has many rivers that fall from the highlands to the coast, so it has a large "
          "hydropower potential. The most important plants are at Edea and Song Loulou on the Sanaga, and at Lagdo on the Benue. "
          "Others, such as Lom Pangar, Memve'ele and Nachtigal, are newer (check your textbook for the details and dates)."),
        T("**Other energy.** In villages, most families still cook with fuelwood. Solar energy is growing, especially in the "
          "sunny north."),
        H("Mineral resources and where they are found"),
        IMG("f5g-cmreco-resources-table.svg",
            alt="A table of selected resources with area and use: oil offshore on the south-west coast, gas near Douala and Kribi, hydropower on the Sanaga and Benue, bauxite in Adamawa, iron ore in the east and south, limestone in the north, and gold in the east",
            caption="Figure 6. Selected resources and where they are found. Check exact sites in your textbook."),
        T("**Bauxite**, the ore of aluminium, is found in the Adamawa highlands, with other deposits in the west. "
          "An aluminium smelter at Edea uses cheap hydroelectric power."),
        T("**Iron ore** is found in the east and south. It is not yet mined on a large scale because it needs a railway and a "
          "port to carry it out."),
        T("**Limestone** is found in the north, for example near Figuil, and is used to make cement. **Gold** is mined in "
          "the east, mostly in small workings. Cobalt, nickel and rutile are also found, mostly in the east and centre. "
          "For the exact sites and the present state of each project, check your textbook."),
        IMG("f5g-cmreco-farming-zones-map.svg",
            alt="Simplified sketch map of Cameroon with offshore oil area in the south-west, the Edea and Lagdo dams, Douala, Yaounde, Garoua, and Lake Chad",
            caption="Figure 7. Offshore oil in the south-west, and the dams at Edea (Sanaga) and Lagdo (Benue). Simplified sketch map, not to scale."),
        H("Challenges of exploitation"),
        KEY("Challenges", "Why resources are not fully used.", cards=[
            ["Money and technology", "Mining and drilling are very costly, and Cameroon needs foreign partners and skills."],
            ["Poor infrastructure", "Heavy ores need railways and ports. Many mining areas have poor roads."],
            ["World prices", "Oil and mineral prices rise and fall, so income is not stable."],
            ["Limited reserves", "Oil is non-renewable and production has fallen."],
            ["Power supply", "Hydropower depends on rain. In the dry season output can fall, and many people are not connected to the grid."],
            ["Environment and people", "Spills, pollution of rivers, loss of forest and land, and the moving of villages."],
        ]),
        H("Impact on the economy and environment"),
        T("**Economy.** Oil has been a major source of government income and export earnings. Electricity powers factories, "
          "homes and businesses and attracts industry such as aluminium. Mining and energy projects create jobs and "
          "training. Cement from limestone supports construction."),
        T("**Environment.** Oil drilling and spills can pollute the sea and mangroves. Gas flaring adds to air pollution. "
          "Gold mining can pollute rivers and clear land. Dams flood land and change river flow. Cutting wood for fuel "
          "contributes to deforestation."),
        H("Government efforts"),
        T("The government encourages foreign and local investment through a mining code and agreements with companies. It "
          "builds new hydropower dams such as Lom Pangar, Memve'ele and Nachtigal, develops gas power near Kribi, and builds the "
          "deep-sea port at Kribi. It also extends the electricity network, supports solar power in rural areas, and tries to "
          "control illegal and artisanal mining. For names of laws and dates, check your textbook."),
        H("Worked examples"),
        EX("Model answer 1: distribution", intro="Describe the distribution of energy resources in Cameroon.", steps=[
            S("Oil", text="Oil is produced offshore on the Atlantic coast in the south-west, and a refinery stands at Limbe."),
            S("Gas", text="Gas is found near Douala and off the coast near Kribi, and is used for power and industry."),
            S("Hydropower", text="Hydroelectric stations are on the Sanaga at Edea and Song Loulou and on the Benue at Lagdo, because the rivers have a strong flow and a drop in height."),
            S("Other energy", text="Fuelwood is the main household fuel in villages, and solar energy is used in the sunny north."),
        ]),
        EX("Model answer 2: challenges and impact", intro="Outline the challenges of exploiting mineral resources in Cameroon and describe one effect on the environment.", steps=[
            S("Challenge: capital", text="Mining is expensive and needs foreign investment and skills."),
            S("Challenge: transport", text="Heavy ores such as iron ore need railways and ports, which are not yet in place in many areas."),
            S("Challenge: prices", text="World prices change, so projects can become unprofitable."),
            S("Environmental effect", text="Gold mining in rivers pollutes water and strips vegetation, harming fish and farms."),
        ]),
        MISTAKE("Calling all energy 'oil'", "Cameroon uses oil, gas, hydropower, fuelwood and solar. Name at least three and say where each is found."),
        MISTAKE("Giving exact figures from memory", "Do not quote tonnes, megawatts or dates unless you are sure. Describe in words or say 'check your textbook'."),
        MISTAKE("Forgetting that minerals are non-renewable", "Oil and ores cannot be replaced once used, so they need careful management and saving."),
        TIP("Exam link: this topic appears in Paper 2 Section D (for example, 'Describe the distribution of energy resources in Cameroon') and in Paper 1 multiple choice. "
            "Always name the resource, the place and one use.", title="Exam link"),
        QUIZ("Where is the aluminium smelter in Cameroon located?",
             ["Garoua", "Edea", "Maroua", "Bamenda"], 1,
             "The aluminium smelter is at Edea on the Sanaga, where it uses hydroelectric power.",
             hint="It is next to a big dam on the Sanaga.",
             feedback=["Garoua is on the Benue and is a cotton and river town.", "", "Maroua is in the far north.", "Bamenda is a highland city."]),
        QUIZ("Why is oil called a non-renewable resource?",
             ["It is found only at sea", "It cannot be replaced once used", "It is very costly", "It is used for electricity"], 1,
             "Oil formed over millions of years and cannot be replaced in a human lifetime.",
             hint="Think about what happens when the last barrel is used.",
             feedback=["Oil is also found on land elsewhere; this does not define it.", "", "Cost does not define a non-renewable resource.", "Use does not define it."]),
        PQ("Name three energy resources and one place where each is found in Cameroon.",
           "Oil: offshore on the south-west coast. Gas: near Douala (Logbaba) or Kribi. Hydroelectric power: Edea and Song Loulou on the Sanaga, or Lagdo on the Benue. Fuelwood: most villages. Solar: the north (any three with places)."),
        PQ("Outline three challenges of exploiting mineral and energy resources in Cameroon.",
           "Lack of money and technology; poor roads, railways and ports; changing world prices; oil running down; hydropower depending on rain; environmental damage (any three)."),
        PQ("Describe two effects of exploiting oil and mineral resources on the environment.",
           "Oil spills pollute the sea and mangroves, harming fish. Gas flaring pollutes the air. Mining clears land and pollutes rivers. Dams flood land (any two explained)."),
        PQ("Describe three ways in which the government is trying to improve the management of Cameroon's energy and mineral resources.",
           "Building new hydropower dams; developing gas power near Kribi; attracting investors through a mining code; extending the electricity network and solar power; trying to control illegal mining; building the Kribi deep-sea port (any three)."),
        SUM("Energy resources: oil offshore in the south-west, gas near Douala and Kribi, hydropower on the Sanaga and Benue, plus fuelwood and solar.",
            "Mineral resources include bauxite, iron ore, limestone, gold, cobalt, nickel and rutile; many are still undeveloped.",
            "Challenges: money, transport, prices, limited oil, dry-season power and environmental harm.",
            "Impact: income, jobs, power and industry, but pollution, land loss and deforestation.",
            "The government invests in dams, gas, ports and electricity networks, and encourages investors."),
    ],
))

# ------------------------------------------------------------------ 6. Multipurpose river development projects
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Multipurpose river development projects: the Lagdo project",
    slug="cmreco-multipurpose-river-development-projects",
    minutes=22,
    summary="What a multipurpose river development project is, the major projects in Cameroon, and a full description of the Lagdo project on the Benue under the headings location, aims, benefits, problems and solutions.",
    objectives=[
        "Identify the major river development projects in Cameroon",
        "Define a multipurpose river development project",
        "Describe the Lagdo project under the headings location, aims, benefits, problems and solutions",
        "Explain why dams cause both benefits and problems",
    ],
    key_concepts=["Multipurpose project", "Dam", "Reservoir", "Hydroelectric power", "Irrigation", "Flood control", "Resettlement", "Lagdo dam"],
    blocks=[
        H("Introduction"),
        T("In the dry season, the Benue River near Garoua can almost shrink. In the rainy season it can flood farms. A dam "
          "can store water in the wet season and release it in a controlled way. The same dam can also make electricity, "
          "water fields and feed a fishing industry."),
        D("A **multipurpose river development project** is a scheme in which a river is controlled, usually by a dam, to serve "
          "several purposes at once: for example electricity, irrigation, flood control, fishing and water supply.", title="Multipurpose project"),
        IMG("f5g-cmreco-multipurpose-dam.svg",
            alt="Cross-section of a dam: reservoir behind the dam wall, a turbine in a power house, an electricity pylon, controlled river flow downstream, irrigation canals to fields, and fish in the reservoir",
            caption="Figure 8. How a multipurpose dam works."),
        H("Major river projects in Cameroon"),
        T("Several rivers have been developed. The main projects are these. For dates, sizes and exact uses, check your textbook."),
        KEY("Major projects", "Name the river and one purpose.", cards=[
            ["Lagdo dam, Benue River", "A multipurpose dam in the north: electricity, irrigation, fishing and flood control."],
            ["Edea and Song Loulou, Sanaga River", "Hydroelectric plants that supply the south and the industries of Douala and Edea."],
            ["Lom Pangar, Bamendjin and others", "Reservoirs that store water to keep the Sanaga flowing in the dry season, plus electricity."],
            ["Maga dam, Logone", "A project for irrigated rice farming in the far north."],
            ["Memve'ele and Nachtigal", "Newer hydropower projects on the Ntem and the Sanaga."],
        ], note="Many projects are mainly for electricity. Lagdo is a good one to choose for 'multipurpose'."),
        H("Case study: the Lagdo project on the Benue"),
        T("The syllabus asks you to describe ONE project under five headings: **location, aims, benefits, problems and "
          "solutions**. We use Lagdo."),
        KEY("1. Location", "Where is it?", cards=[
            ["Place", "On the Benue River in the North region of Cameroon, a short distance upstream (south) of the city of Garoua near the town of Lagdo."],
            ["The river", "The Benue rises in the Adamawa highlands, flows north and west into Nigeria, and joins the Niger. The reservoir behind the dam is called Lake Lagdo."],
        ], note="Check your textbook for the distance from Garoua and the opening date (it was built in the early 1980s)."),
        KEY("2. Aims", "Why was it built?", cards=[
            ["Electricity", "To supply power to Garoua and the towns of the north."],
            ["Irrigation", "To water fields in the dry season so farmers can grow rice, cotton, sorghum and vegetables."],
            ["Flood control", "To store flood water and reduce flooding downstream."],
            ["Fishing and water supply", "To create a lake for fishing and supply water to towns and animals."],
        ]),
        KEY("3. Benefits", "What has it brought?", cards=[
            ["Power", "Electricity for homes, businesses and small industry in the north."],
            ["Farming", "Irrigation allows farming in the dry season and can raise food and cotton output."],
            ["Fishing and jobs", "Fish from the lake give food and income, and the project gave construction and operating jobs."],
            ["Safety and water", "Flood control and a steadier water supply."],
        ]),
        KEY("4. Problems", "What went wrong?", cards=[
            ["People", "Villages and farmland were flooded by the lake, so people had to move."],
            ["Floods downstream", "If the lake is too full in the wet season, water must be released quickly. This has caused serious flooding in Cameroon and in Nigeria in some years."],
            ["Health", "Standing water can increase diseases such as bilharzia and malaria."],
            ["Siltation and upkeep", "Soil washed in by rivers fills the lake over time. Canals and machines need costly repairs."],
            ["Limited output", "Power and water may not meet all demand, especially in the dry season."],
        ]),
        KEY("5. Solutions", "How can the problems be reduced?", cards=[
            ["Resettlement", "Fair compensation, new land, houses and services for displaced families."],
            ["Flood warning", "Plan water releases, warn villages early and work with Nigeria."],
            ["Health", "Clean water, bed nets, health centres and control of water snails."],
            ["Care of the catchment", "Plant trees and protect soil upstream to reduce silt; keep canals and turbines in good order."],
            ["More energy sources", "Link to the national grid and add solar and other sources."],
        ]),
        H("Worked examples"),
        EX("Model answer 1: the Lagdo project", intro="Describe the Lagdo multipurpose project under the headings location, aims, benefits, problems and solutions.", steps=[
            S("Location", text="Lagdo is on the Benue River in the North region, a short distance upstream of Garoua. The Benue flows west into Nigeria and joins the Niger."),
            S("Aims", text="It was built to produce electricity for the north, irrigate farmland, control floods, create a fishing lake and supply water."),
            S("Benefits", text="It gives electricity to Garoua and nearby towns, dry-season irrigation for crops such as rice, cotton and vegetables, fish and jobs, and reduces normal flooding."),
            S("Problems", text="Villages and farmland were flooded by the lake. Emergency water releases in the wet season have flooded land downstream. Standing water increases disease, and silt and repairs are costly."),
            S("Solutions", text="Pay fair compensation and resettle families. Warn villages and neighbouring Nigeria before releases. Improve health care, protect the catchment and maintain canals and turbines."),
        ]),
        EX("Model answer 2: why dams cause both benefits and problems", intro="Explain why a large dam can bring both advantages and disadvantages to local people.", steps=[
            S("Advantages for some", text="Farmers near irrigation canals, fishermen and towns that receive electricity gain income and services."),
            S("Disadvantages for others", text="People whose land is flooded lose homes and fields, and those downstream can be affected by sudden releases."),
            S("Link to management", text="The balance depends on planning: resettlement, warnings and sharing of benefits can turn problems into smaller costs."),
            S("Conclusion", text="A multipurpose dam can raise development, but its costs must be managed fairly."),
        ]),
        MISTAKE("Writing only about electricity", "Multipurpose means several uses. Give at least electricity, irrigation, flood control and fishing."),
        MISTAKE("Mixing up the rivers", "Lagdo is on the Benue in the north. Edea and Song Loulou are on the Sanaga in the centre and south."),
        MISTAKE("Missing one of the five headings", "The syllabus names five headings: location, aims, benefits, problems and solutions. Use them as sub-headings."),
        TIP("Exam link: expect Paper 2 Section D to ask you to describe one project 'under the headings location, aims, benefits, problems and solutions', "
            "and Paper 1 to ask to identify a project. Learn one project (Lagdo) fully. Draw a simple sketch of a dam with labels.", title="Exam link"),
        QUIZ("Lagdo dam is built on which river?",
             ["The Sanaga", "The Benue", "The Wouri", "The Logone"], 1,
             "Lagdo is on the Benue River in the North region.",
             hint="The river flows west into Nigeria.",
             feedback=["The Sanaga has the Edea and Song Loulou plants.", "", "The Wouri flows to the estuary at Douala.", "The Logone is in the far north and flows toward Lake Chad."]),
        QUIZ("Which is a problem caused by releasing a lot of water quickly from a dam in the wet season?",
             ["More electricity for the north", "Flooding of farms and villages downstream", "More fish in the reservoir", "A lower reservoir level for tourism"], 1,
             "Sudden releases can flood land downstream. The other choices are not problems of releasing water.",
             hint="Where does the released water go?",
             feedback=["That is a benefit of the dam.", "", "That is not caused by releases.", "That is not the main problem."]),
        PQ("What is a multipurpose river development project?",
           "A scheme in which a river is controlled, usually by a dam, so that it serves several purposes at once, such as electricity, irrigation, flood control, fishing and water supply."),
        PQ("Name three major river development projects in Cameroon.",
           "Lagdo (Benue), Edea and Song Loulou (Sanaga), Lom Pangar, Bamendjin, Maga (Logone), Memve'ele, Nachtigal (any three)."),
        PQ("State three aims of the Lagdo project.",
           "To produce electricity for the north; to irrigate farmland in the dry season; to control floods; to provide fish and water supply (any three)."),
        PQ("Describe two problems of the Lagdo project and suggest one solution to each.",
           "Villages and land were flooded, so people moved: give compensation and resettlement. Releases of water cause floods downstream: plan releases, give early warnings and cooperate with neighbouring Nigeria. Standing water increases disease: improve health care and clean water. Silt fills the lake: protect the catchment (any two with solutions)."),
        SUM("A multipurpose project controls a river to serve several purposes, such as electricity, irrigation, flood control, fishing and water supply.",
            "Major projects: Lagdo (Benue), Edea and Song Loulou (Sanaga), Lom Pangar, Bamendjin, Maga, Memve'ele and Nachtigal.",
            "Lagdo: location on the Benue near Garoua; aims of power, irrigation, flood control and fishing.",
            "Benefits: electricity, dry-season farming, fish, jobs and safety. Problems: displacement, downstream floods, disease, silt.",
            "Solutions: resettlement, warnings, health care, protecting the catchment and maintenance."),
    ],
))
