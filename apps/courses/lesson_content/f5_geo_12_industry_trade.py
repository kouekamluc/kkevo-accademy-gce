"""Form 5 Geography: Economic Activities, secondary industries and globalisation and trade (lessons)."""

from .dsl import *  # noqa: F403

COURSE = ("geography", "form-5")

MODULE = "Economic Activities"
SEC = "Secondary industries"
TER = "Tertiary industries"

LESSONS = [
    # ------------------------------------------------------------------ 1
    lesson(
        module=MODULE, topic=SEC,
        title="Meaning and classification of manufacturing, and where industry is found",
        slug="ind-meaning-and-classification-of-manufacturing",
        minutes=22,
        summary="Industries are primary, secondary or tertiary; manufacturing is heavy or light. Factories gather where raw materials, power, labour, markets, transport, capital and government policy favour them.",
        objectives=[
            "Define industry and manufacturing, and classify industries as primary, secondary or tertiary.",
            "Classify manufacturing into heavy and light industries, with examples.",
            "Illustrate the global distribution of manufacturing industries on a sketch map.",
            "State and explain the factors that influence where industries are located.",
        ],
        key_concepts=["Industry", "Primary, secondary and tertiary", "Manufacturing", "Heavy industry", "Light industry",
                      "Industrial location factors", "Global distribution of industry"],
        blocks=[
            H("Introduction"),
            T("Think of a bottle of soft drink bought in Bamenda. The sugar was grown on a farm. The drink was made and bottled "
              "in a factory, probably in Douala. A trader then sold it from a shop. Three different kinds of work stand behind one bottle. "
              "Geographers group all these jobs into **industries**. In this lesson you learn how industries are classified, "
              "where in the world factories are found, and why."),
            H("Meaning and classification of industries"),
            D("An **industry** is a group of activities by which people earn a living by producing goods or providing services.",
              title="Definition: industry"),
            D("**Manufacturing** is the making of goods by processing raw materials or assembling parts, usually in factories "
              "and with the help of machines and power.", title="Definition: manufacturing"),
            T("Industries fall into three groups. **Primary industries** take raw materials from the land or sea: farming, "
              "mining, fishing and forestry. **Secondary industries** make or process goods: manufacturing and construction. "
              "**Tertiary industries** provide services: trade, transport, banking, teaching and health care."),
            IMG("f5g-ind-classification.svg",
                alt="Three boxes for primary, secondary and tertiary industry; secondary industry splits into heavy and light manufacturing.",
                caption="Figure 1. Primary, secondary and tertiary industry, and the two kinds of manufacturing."),
            T("The groups depend on each other. Cocoa grown in the South-West is a primary product. Processed in a factory "
              "into cocoa butter, it becomes a secondary product. Sold in a shop or shipped from Douala port, it supports "
              "tertiary industry."),
            KEY("Heavy and light manufacturing",
                "Manufacturing is divided by the weight and bulk of the materials and products, and by the power and machinery needed.",
                cards=[
                    ["Heavy industry", "Uses large, heavy raw materials, big machines and a lot of power. Products are bulky. "
                     "Examples: iron and steel, cement, shipbuilding, oil refining, aluminium smelting, heavy chemicals."],
                    ["Light industry", "Uses small, light parts or materials and less power. Products are easy to carry. "
                     "Examples: clothing, soap, bottled drinks, baked bread, electronics, furniture, printing."],
                ]),
            EX("Worked example 1: classifying industries", intro="Classify each activity as primary, secondary or tertiary. For "
               "each secondary activity, say whether it is heavy or light: (a) growing cocoa in Kumba; (b) smelting aluminium; "
               "(c) making soap in Douala; (d) running a bus service from Maroua; (e) mining iron ore.", steps=[
                S("Ask: does it take from nature, make goods or provide a service?",
                  text="Taking from the land is primary. Making goods is secondary. Giving a service is tertiary."),
                S("(a) and (e) are primary", text="Growing cocoa is farming. Mining iron ore takes a raw material from the ground."),
                S("(b) is secondary and heavy", text="Aluminium smelting processes a raw material, uses very large amounts of power and makes a heavy product."),
                S("(c) is secondary and light", text="Soap is a small, light product made with little power and simple machines."),
                S("(d) is tertiary", text="Running buses sells a transport service, not a product."),
            ]),
            H("Where is industry found in the world?"),
            T("Manufacturing is not spread evenly. It is **concentrated** in a few large regions. The oldest and biggest are "
              "north-eastern USA and the Great Lakes, north-western Europe, and Japan. In recent decades the eastern coast of "
              "China, South Korea, Taiwan and parts of India and Brazil have grown very quickly."),
            IMG("f5g-ind-world-map.svg",
                alt="Sketch world map with nine numbered industrial regions: USA, Europe, Japan, China, Korea and Taiwan, Brazil, India, South Africa and Douala.",
                caption="Figure 2. Sketch map of major industrial regions (schematic, simplified outlines)."),
            T("Most of the large industrial regions lie in the northern hemisphere, in the middle latitudes, and near the coast "
              "or a large river. Africa has only small industrial areas, such as Gauteng in South Africa and some port cities, "
              "among them Douala. Much of the tropics and the world's hot deserts have very little manufacturing."),
            H("Factors that influence the location of industry"),
            T("A factory owner wants to make goods at the lowest cost and sell them easily. The following factors decide "
              "which places are best."),
            KEY("Location factors", "Each factor can attract a factory to a place.", cards=[
                ["Raw materials", "Factories that process heavy or perishable raw materials locate near them. Sugar mills and "
                 "sawmills stand close to the farms and forests."],
                ["Power", "Heavy industry needs coal, oil, gas or electricity. Aluminium smelting is placed where cheap electricity is available."],
                ["Labour", "Factories need workers. Cheap labour attracts clothing and assembly work. Skilled labour attracts high-tech industry."],
                ["Market", "People who buy the goods. A large, rich market, such as a big city, attracts factories making bread, drinks or furniture."],
                ["Transport", "Roads, railways, ports and airports move materials in and goods out. Ports attract industry that imports or exports."],
                ["Capital", "Money for land, buildings and machines. Banks and investors are found where there is already wealth."],
                ["Government policy", "Tax relief, cheap land, industrial zones and trade rules can draw factories to a chosen area."],
            ]),
            T("The factors work together. Douala is Cameroon's main industrial city because it has a seaport, the biggest "
              "local market, many workers, electricity and banks. Check your textbook for the main industries of Douala and "
              "of other Cameroonian towns."),
            EX("Worked example 2: model answer", intro="Explain why many factories in Cameroon are found in Douala.", steps=[
                S("Point 1: transport", text="Douala has the country's main seaport. Factories can import machines and raw "
                  "materials easily and export finished goods. Roads and a railway link it to the interior."),
                S("Point 2: market", text="Douala is a very large city. Many people live there and buy bread, drinks, soap "
                  "and clothes, so goods are sold at a short distance and at low transport cost."),
                S("Point 3: labour", text="People from all regions move to Douala to find work, so factories find workers easily."),
                S("Point 4: services", text="Banks, electricity, water and port services are already in place, so a new factory spends less on setting up."),
                S("Link the points", text="Each reason cuts costs or raises sales, which is why one city attracts so many factories."),
            ]),
            TIP("In the exam, label your sketch map with names, a title and a short key. Mark regions with a number or shading, "
                "not only with a dot. Never say that a continent has no industry at all."),
            MISTAKE("Mixing up heavy and light industry",
                    "Heavy and light do not mean important and unimportant, nor many and few workers. They refer to the weight and bulk of "
                    "materials and products and the power and machinery needed. Steel is heavy. Soap is light."),
            MISTAKE("Listing factors without explaining them",
                    "Writing only 'power, labour, market' earns little. Say how each factor affects cost or sales and give an "
                    "example, as in Worked example 2."),
            QUIZ("Which of these is a SECONDARY industry?",
                 ["Fishing at Limbe", "Making cement at a factory", "Teaching at a school", "Mining sand from a river"], 1,
                 "Making cement turns raw materials into a new product, so it is manufacturing, which is secondary industry.",
                 hint="Secondary industry changes materials into goods.",
                 feedback=["Fishing takes a resource from nature: primary industry.", "",
                           "Teaching is a service: tertiary industry.", "Mining sand takes a material from the ground: primary industry."]),
            QUIZ("A factory making bottled water and soft drinks is usually built close to a large city mainly because",
                 ["the raw materials are very heavy", "it needs a large market nearby", "it needs a great deal of coal",
                  "it needs a deep mine"], 1,
                 "Bottled drinks are bulky to carry and sold to many people, so a nearby market lowers transport cost.",
                 hint="Think about who buys the goods.",
                 feedback=["Water is heavy, but it is found nearly everywhere, so it is not the deciding factor.", "",
                           "Light industries do not need large amounts of coal.", "A mine is needed by primary industry, not by a drinks factory."]),
            TIP("Exam link: this topic appears in Paper 1 as multiple-choice questions on classification and on the factors of "
                "location, and in Paper 2 Section C (human geography) as a description of distribution with a sketch map and "
                "an explanation of factors. Cameroon examples (Douala) may also appear in Section D.", title="Exam link"),
            PQ("Define manufacturing and give two examples each of heavy and light industries.",
               "Manufacturing is the making of goods by processing raw materials or assembling parts, usually in factories. "
               "Heavy industries: iron and steel, cement, shipbuilding. Light industries: clothing, soap, electronics, bread."),
            PQ("State four factors that influence the location of industry.",
               "Any four of: raw materials, power, labour, market, transport, capital, government policy."),
            PQ("Describe the global distribution of manufacturing industry.",
               "Manufacturing is concentrated in a few regions, mostly in the northern hemisphere in the middle latitudes: "
               "north-eastern USA, north-western Europe and Japan. Newer centres include eastern China, South Korea, Taiwan, "
               "India and south-east Brazil. Africa and much of the tropics have little, apart from small areas such as Gauteng and port cities such as Douala."),
            PQ("Explain why aluminium smelting needs a different location from bread baking.",
               "Aluminium smelting is a heavy industry that uses a very large amount of electricity, so it is placed where "
               "power is cheap, for example near a hydroelectric station or a port that imports its raw material. Baking is a light industry whose "
               "bread is perishable and bulky, and is sold to many people, so bakeries are placed in towns near their market."),
            SUM("Industries are primary (raw materials), secondary (manufacturing) or tertiary (services).",
                "Manufacturing is heavy (bulky, power-hungry, such as steel and cement) or light (small, such as clothes and soap).",
                "Industry is concentrated in north-eastern USA, north-western Europe, Japan and fast-growing regions of Asia and Brazil.",
                "Location depends on raw materials, power, labour, market, transport, capital and government policy.",
                "Explain each factor as a cost or a sales advantage, with an example, and label your sketch maps."),
        ],
    ),
    # ------------------------------------------------------------------ 2
    lesson(
        module=MODULE, topic=SEC,
        title="Why industrialisation is low in low-income countries",
        slug="ind-industrialisation-in-lics",
        minutes=20,
        summary="Many LICs have few factories because of a shortage of capital, technology, markets, power, skills and infrastructure. These problems feed each other in a cycle of poverty.",
        objectives=[
            "Define industrialisation and low-income country (LIC).",
            "Outline the reasons for the low level of industrialisation in LICs.",
            "Explain how these reasons are linked in a cycle that is hard to break.",
            "Use examples from Africa, including Cameroon, to support an answer.",
        ],
        key_concepts=["Industrialisation", "Low-income country (LIC)", "Capital", "Technology", "Market", "Power supply",
                      "Skills", "Infrastructure", "Value added", "Cycle of poverty"],
        blocks=[
            H("Introduction"),
            T("A tailor in a small town in the Far North region has a good idea: make school uniforms for the whole division. "
              "But the bank will not lend her money for a better machine. Electricity goes off for hours each day. The roads to "
              "the next town are poor, and few families can afford many uniforms."),
            T("One small business shows, in miniature, why many poorer countries have few factories. In this lesson "
              "you study the main reasons, and you see how they link together."),
            H("Key terms"),
            D("**Industrialisation** is the growth of manufacturing in a country, so that factories provide more of its jobs and income.",
              title="Definition: industrialisation"),
            D("A **low-income country (LIC)** is a country where average income per person is very low and most people depend "
              "on farming or other primary activities. Many countries of the Sahel and of tropical Africa are LICs. "
              "Check your textbook for the current World Bank list.", title="Definition: LIC"),
            T("Most LICs export raw materials such as cocoa, cotton, timber or minerals. Factories in richer countries turn them "
              "into goods, and the factories earn the extra money. The extra value created by processing is called **value added**. "
              "A country that processes its own raw materials keeps more of that value."),
            H("Reasons for low industrialisation"),
            KEY("Six main reasons", "Each reason raises costs, lowers sales, or both.", cards=[
                ["Shortage of capital", "Capital is money for land, buildings and machines. Incomes are low, so people save little. "
                 "Banks lend cautiously, interest rates are high, and the government has little to invest."],
                ["Weak technology", "Modern machines are expensive and are often imported. Few local firms can research or repair them, "
                 "so productivity stays low."],
                ["Small markets", "Most people are poor and cannot buy many manufactured goods. Poor roads and borders make "
                 "it hard to sell far away. Cheaper imports compete with local goods."],
                ["Poor power supply", "Factories need steady electricity. Shortages and cuts stop machines, spoil goods and force "
                 "firms to buy expensive generators."],
                ["Lack of skills", "Many people have little schooling or technical training. Skilled engineers, managers and "
                 "technicians may leave to work abroad."],
                ["Poor infrastructure", "Weak roads, railways, ports, water and telephone networks raise the cost of moving "
                 "materials and goods and delay deliveries."],
            ]),
            IMG("f5g-ind-poverty-cycle.svg",
                alt="Cycle: low incomes, little saving and capital, few factories and old technology, few skills and weak markets, low output and few jobs, back to low incomes.",
                caption="Figure 1. The cycle that holds back industry in many LICs."),
            T("Figure 1 shows why the problem is hard to solve. Low incomes mean little saving. Little saving means little capital. "
              "Without capital, factories are few and use old methods. Output and jobs stay low, so incomes stay low."),
            T("Other reasons also matter. Some LICs depend on selling a few raw materials whose prices rise and fall. Some have "
              "heavy debts. War or unstable government frightens investors. Colonial trade often linked the economy to exporting "
              "raw materials, not to making goods."),
            EX("Worked example 1: model answer", intro="Outline four reasons for the low level of industrialisation in low-income countries.", steps=[
                S("Reason 1: capital", text="People earn little, so they save little. Banks lend little, so firms cannot buy land or machines."),
                S("Reason 2: markets", text="Most people are poor and buy few manufactured goods. Poor transport also makes it hard to sell far away."),
                S("Reason 3: power", text="Electricity is expensive or often cut. Factories stop work or must buy costly generators."),
                S("Reason 4: skills", text="Few workers have technical training, and trained people may move abroad, so firms struggle to run modern machines."),
                S("Link", text="These problems feed each other in a cycle of poverty, which is why industry grows slowly."),
            ]),
            EX("Worked example 2: applying the reasons to Cameroon", intro="Cameroon exports much cocoa, cotton and timber. Suggest why "
               "these are often sold with little processing, and what this means for industry.", steps=[
                S("Capital and technology", text="Processing plants cost a great deal. Firms need loans and imported machines, which many "
                  "local businesses cannot get."),
                S("Power and infrastructure", text="Plants need steady power and good roads and ports. Where they are weak, it is cheaper to export the raw material."),
                S("Markets", text="Richer countries often have bigger, better markets for finished goods, so processing happens there."),
                S("Result", text="The country earns less value added and creates fewer jobs. Check your textbook for the cases of "
                  "cocoa, cotton and timber processing in Cameroon."),
            ]),
            EX("Worked example 3: ways to break the cycle", intro="Suggest two things that could help an LIC to industrialise.", steps=[
                S("Improve power and transport", text="Build dams, power lines, roads and ports so that factories can work and deliver goods."),
                S("Train workers", text="Technical schools and apprenticeships create the skills that factories need."),
                S("Attract investment", text="Stable government, fair taxes and loans for small firms encourage local and foreign investors."),
                S("Take care", text="Each measure costs money, so help may be needed from aid, trade partners or regional markets."),
            ]),
            TIP("A good answer gives the reason, then says how it affects industry. Write 'poor roads raise transport costs and "
                "limit the market' instead of just 'poor roads'."),
            MISTAKE("Saying LICs have no raw materials",
                    "Many LICs are rich in raw materials. The problem is lack of capital, power, skills and markets to process them. "
                    "Raw materials alone do not create industry."),
            MISTAKE("Treating one reason on its own",
                    "Reasons are linked. A weak answer lists them. A strong answer shows that low income causes low savings, which causes "
                    "low capital, which causes few factories, as in the cycle."),
            QUIZ("Which is a reason for a LOW level of industrialisation in an LIC?",
                 ["A large, rich home market", "Frequent power cuts", "Many trained engineers", "Excellent roads and ports"], 1,
                 "Power cuts stop machines and raise costs, which discourages factories.",
                 hint="Pick the problem, not the advantage.",
                 feedback=["A large, rich market would encourage industry.", "", "Trained engineers help industry grow.",
                           "Good transport would encourage industry."]),
            QUIZ("Why do most people in an LIC save little money?",
                 ["Banks give large loans to everyone", "Their incomes are low and mostly spent on basic needs", "They prefer to import machines",
                  "Taxes are always zero"], 1,
                 "With low incomes, most money goes on food, housing and other basic needs, so little remains for saving or investing.",
                 hint="Think about what low-income families must buy first.",
                 feedback=["If banks gave large loans to everyone, capital would be easy to find.", "",
                           "Importing machines needs capital, which they lack.", "Taxes are not zero and are not the main reason."]),
            TIP("Exam link: Paper 1 asks multiple-choice questions on the reasons for low industrialisation. Paper 2 Section C asks "
                "'Outline the reasons for the low level of industrialisation in LICs', often using Africa or Cameroon examples. "
                "Section D can ask about the constraints on manufacturing in Cameroon.", title="Exam link"),
            PQ("Define industrialisation.",
               "Industrialisation is the growth of manufacturing in a country, so that factories provide a larger share of its jobs and income."),
            PQ("State four reasons for the low level of industrialisation in LICs.",
               "Any four of: shortage of capital, weak technology, small markets, poor power supply, lack of skills, poor infrastructure."),
            PQ("Explain how a shortage of capital slows industrial growth in an LIC.",
               "Incomes are low, so people save little and banks have little to lend. Firms cannot buy land, buildings or machines, "
               "so few factories are built and those that exist use old methods. Output, jobs and incomes stay low, so saving stays "
               "low, which is a cycle of poverty."),
            PQ("Explain why poor infrastructure discourages factories in an LIC.",
               "Poor roads, ports, water and telephone networks raise the cost of bringing in materials and taking goods to market and delay "
               "deliveries. Power cuts stop machines. Firms prefer places with better infrastructure, so investment goes elsewhere."),
            SUM("Industrialisation is the growth of manufacturing; many LICs have little of it.",
                "Main reasons: shortage of capital, weak technology, small markets, poor power, lack of skills and poor infrastructure.",
                "The reasons link in a cycle of poverty, so low income keeps industry small.",
                "Many LICs export raw materials and lose the value added by processing.",
                "In answers, state each reason, explain its effect on costs or sales, and use an example."),
        ],
    ),
    # ------------------------------------------------------------------ 3
    lesson(
        module=MODULE, topic=SEC,
        title="Rapid industrial growth in newly industrialising countries",
        slug="ind-industrial-growth-in-nics",
        minutes=20,
        summary="NICs grew fast by making goods for export, helped by cheap trainable labour, government support, foreign investment, good ports and reinvested earnings. Growth also brings costs.",
        objectives=[
            "Define a newly industrialising country (NIC) and name examples.",
            "Outline the reasons for the rapid industrial growth of NICs.",
            "Explain how export earnings help industry to keep growing.",
            "Describe some problems that rapid industrial growth can cause.",
        ],
        key_concepts=["Newly industrialising country (NIC)", "Export-led growth", "Foreign investment", "Transnational company",
                      "Cheap labour", "Government policy", "Reinvestment"],
        blocks=[
            H("Introduction"),
            T("Walk into a shop in Douala or Yaounde and look at the labels: televisions, phones, motorbikes, clothes. "
              "Many were made in East Asia, in countries that were poor farming economies only two or three generations ago."),
            T("Some countries moved from farming to making goods very quickly. They are called **newly industrialising countries**. "
              "In this lesson you find out why their industry grew so fast."),
            H("What is a NIC?"),
            D("A **newly industrialising country (NIC)** is a country that has recently moved from an economy based on farming "
              "and raw materials to one based on manufacturing, with rapid growth and rising incomes.", title="Definition: NIC"),
            T("The first group, sometimes called the Asian Tigers, were South Korea, Taiwan, Singapore and Hong Kong. A later "
              "group includes Malaysia, Thailand and Mexico. Brazil, India and China are also described as fast-growing "
              "industrial economies. South Africa is often described as an emerging economy. Textbooks differ on which "
              "countries to list, so check your textbook."),
            H("Reasons for rapid industrial growth"),
            IMG("f5g-ind-nic-growth.svg",
                alt="Flow diagram: cheap trainable labour, government support and foreign investment lead to factories making goods for export, then export earnings, which are reinvested in schools, ports, roads and technology.",
                caption="Figure 1. How a NIC grows by making goods for export."),
            KEY("Main reasons", "Several advantages worked together.", cards=[
                ["Cheap, trainable labour", "Wages were low compared with richer countries, and workers learned new skills quickly, "
                 "so firms could make goods cheaply."],
                ["Government policy", "Governments gave tax relief, built industrial zones and spent on schools, roads and ports. "
                 "Many chose to make goods for export."],
                ["Foreign investment", "Transnational companies (TNCs) built factories to use cheap labour and brought capital, "
                 "machines and know-how."],
                ["Good location and transport", "Coastal sites and fine ports made it cheap to import materials and export goods to world markets."],
                ["Export markets", "Selling to rich countries brought in large earnings, much larger than a small home market could give."],
                ["Reinvestment", "Export earnings paid for better education, new technology and better infrastructure, so industry could move from simple to advanced goods."],
            ]),
            T("Look again at Figure 1. Growth is a loop. Factories make goods for export. Exports earn money. The money is "
              "reinvested, and industry grows further. Compare this with the cycle of poverty in an LIC: here the cycle runs "
              "upward, not downward."),
            T("In many NICs the first goods were simple: clothing, toys and shoes. Later came ships, steel and electronics. "
              "Finally some countries moved into computers, cars and advanced services as wages and skills rose."),
            H("Costs of rapid growth"),
            T("Rapid growth is not free of problems. Air and water pollution can rise. Cities become crowded. Workers may face long "
              "hours and low pay. Richer and poorer groups can grow apart. A country that depends on exports can suffer if world demand falls."),
            EX("Worked example 1: model answer", intro="Outline four reasons for the rapid industrial growth of NICs.", steps=[
                S("Reason 1: labour", text="Wages were low and workers learned quickly, so goods were cheap to make and could undercut richer countries."),
                S("Reason 2: government", text="Governments gave tax breaks, built industrial zones and spent on schools and ports, which attracted firms."),
                S("Reason 3: foreign investment", text="TNCs built factories and brought capital and technology that the country lacked."),
                S("Reason 4: exports and reinvestment", text="Selling goods abroad earned large sums, which were reinvested in training, machines and transport."),
            ]),
            EX("Worked example 2: comparing a NIC and an LIC", intro="Explain why the industries of a NIC grow faster than those of an LIC.", steps=[
                S("Capital", text="NICs attract foreign investment and keep export earnings, while LICs often lack capital."),
                S("Skills and technology", text="NIC governments invest in schooling and technical training, while LIC workers often have little training."),
                S("Infrastructure", text="NICs have good ports, roads and power for exporters, while LICs often have weak networks."),
                S("Markets", text="NICs sell to large foreign markets, while LICs often have small home markets and few exports of goods."),
            ]),
            EX("Worked example 3: balanced answer", intro="Discuss whether rapid industrial growth is good for a country.", steps=[
                S("Benefits", text="Jobs, higher incomes, new skills and tax money for schools and hospitals."),
                S("Costs", text="Pollution, crowded cities, long working hours and unequal sharing of wealth."),
                S("Conclusion", text="Growth brings real gains, but governments need rules and planning so that people and the environment are protected."),
            ]),
            TIP("Keep examples general. Name one or two NICs, such as South Korea and Brazil, and give the reasons. Do not "
                "quote exact figures unless your teacher gave them to you."),
            MISTAKE("Saying NICs are the same as AICs",
                    "AICs are long-established rich industrial countries. NICs are newer industrial countries whose industry and incomes "
                    "have risen quickly but whose incomes are still, on average, lower than in AICs."),
            MISTAKE("Giving only 'cheap labour'",
                    "Cheap labour alone does not explain growth, because many LICs also have cheap labour. Add government policy, "
                    "investment, transport and exports to earn full marks."),
            QUIZ("Which of these is a NIC?",
                 ["Chad", "South Korea", "The United Kingdom", "Niger"], 1,
                 "South Korea moved quickly from farming to manufacturing and is a well-known NIC.",
                 hint="Think of the Asian Tigers.",
                 feedback=["Chad is a low-income country with little industry.", "",
                           "The United Kingdom is an old AIC.", "Niger is a low-income country with little industry."]),
            QUIZ("Why do TNCs build factories in NICs?",
                 ["To use cheap trainable labour and reach export markets", "Because NICs have no ports", "Because wages are higher than at home",
                  "Because governments forbid factories"], 0,
                 "TNCs save on labour costs and use the NIC as a base for export, and the government usually welcomes them.",
                 hint="Think about cost and markets.",
                 feedback=["", "NICs usually have good ports.", "Wages are lower, not higher.", "Governments in NICs usually encourage factories."]),
            TIP("Exam link: Paper 1 has multiple-choice questions on NICs and their reasons for growth. Paper 2 Section C asks "
                "'Outline the reasons for the rapid industrial growth of NICs'. Remember the loop: labour, policy, investment, exports, reinvestment.",
                title="Exam link"),
            PQ("Define a newly industrialising country.",
               "A NIC is a country that has recently changed from an economy based on farming and raw materials to one based on "
               "manufacturing, with fast growth and rising incomes. South Korea and Taiwan are examples."),
            PQ("State four reasons for the rapid industrial growth of NICs.",
               "Any four of: cheap trainable labour, government support, foreign investment by TNCs, good ports and location, "
               "export markets, reinvestment of earnings."),
            PQ("Explain how foreign investment helps a country to industrialise.",
               "TNCs bring capital, machines, technology and management skills that the country lacks. They build factories "
               "that create jobs and pay wages, and workers learn new skills. The goods made are exported, so the country earns money."),
            PQ("Describe two problems that rapid industrial growth may cause.",
               "Pollution of air and water as factories and traffic increase; crowded cities with pressure on housing and water; "
               "long hours and low pay for some workers; a wider gap between rich and poor."),
            SUM("A NIC has recently moved from farming and raw materials to fast manufacturing growth.",
                "Reasons: cheap trainable labour, government support, foreign investment, good ports, export markets and reinvestment.",
                "Export earnings paid for schools, ports and technology, so growth became a loop.",
                "Growth brings jobs and income but also pollution, crowding and inequality.",
                "Keep examples general: South Korea, Taiwan, Brazil, India, and so on."),
        ],
    ),
    # ------------------------------------------------------------------ 4
    lesson(
        module=MODULE, topic=SEC,
        title="Industry in advanced industrial countries: recent changes",
        slug="ind-industry-in-aics-recent-changes",
        minutes=20,
        summary="In AICs heavy industry has declined while high-tech industry and services have grown. Many factories have relocated abroad and many jobs have been automated, mainly because of costs, competition and new technology.",
        objectives=[
            "Define an advanced industrial country (AIC).",
            "Describe recent changes in industry in AICs: decline of heavy industry, growth of high-tech and services, relocation and automation.",
            "Outline reasons for these changes.",
            "Describe the effects of the changes on people and places.",
        ],
        key_concepts=["Advanced industrial country (AIC)", "Decline of heavy industry", "High-tech industry", "Service industries",
                      "Relocation", "Automation", "Deindustrialisation"],
        blocks=[
            H("Introduction"),
            T("When you buy a phone in Bamenda, the brand may come from the United States or Europe, but the parts were "
              "probably made in several Asian countries. The old pattern, in which rich countries made everything at home, "
              "has changed."),
            T("In this lesson you study how industry in the older rich countries has changed in recent decades, and why."),
            D("An **advanced industrial country (AIC)** is a long-established, wealthy country with a high level of industry, "
              "technology and income per person. Examples are the United States, Germany, the United Kingdom and Japan.",
              title="Definition: AIC"),
            H("Current trends"),
            IMG("f5g-ind-aic-trends.svg",
                alt="Three rows: decline of heavy industry replaced by high-tech and services; factories in the home country replaced by relocation abroad; assembly-line workers replaced by robots and computers.",
                caption="Figure 1. Three recent changes in industry in AICs."),
            KEY("Four trends", "These changes have gone on for several decades.", cards=[
                ["Decline of heavy industry", "Coal mining, steel making and shipbuilding have shrunk in many AICs, for example in older "
                 "industrial regions of the United Kingdom, Germany and the United States. Factories have closed and jobs have been lost."],
                ["Growth of high-tech industry and services", "Firms making computers, medicines, aircraft parts and software have grown, as have "
                 "banking, tourism and retail. They are located near universities and in science parks."],
                ["Relocation", "Many firms moved factories, especially for low-skilled work, to countries with lower wages, "
                 "such as NICs. Head offices and design stay at home."],
                ["Automation", "Robots and computer-controlled machines do work once done by people. Fewer workers produce more goods."],
            ]),
            T("Together these trends are sometimes called **deindustrialisation**: manufacturing provides fewer jobs than before. "
              "The value of what is made often stays high, but it is made by fewer workers and in cleaner, smaller factories."),
            H("Reasons for the changes"),
            KEY("Why have these changes happened?", "Several causes work together.", cards=[
                ["Competition from NICs", "NICs make steel, ships and electronics more cheaply because wages are lower, so AIC factories lose sales."],
                ["High costs at home", "High wages, land prices and taxes push firms to move or close."],
                ["Running out of resources", "Some coal and iron ore deposits near old industrial areas are exhausted or too costly to mine."],
                ["Changing demand", "People now spend more on services, technology and leisure than on heavy goods."],
                ["New technology", "Automation and computers cut labour needs. High-tech industry needs few raw materials, so it can locate near skilled people."],
                ["Government and TNC decisions", "Governments encourage new industries. TNCs choose the cheapest places for each stage of production."],
                ["Environmental rules", "Strict pollution laws raise the cost of old heavy industry and favour cleaner, newer industry."],
            ]),
            T("High-tech industry follows different rules from old heavy industry. It needs skilled workers, research, "
              "good communications and an attractive place to live, not coal or iron ore. Clusters such as Silicon Valley in "
              "California grew around universities. Many such clusters now exist."),
            H("Effects of the changes"),
            T("Where heavy industry closed, unemployment rose and some towns lost people and shops. Governments helped with "
              "retraining and new industrial parks. Other regions with universities and new firms grew quickly. Cheaper "
              "imports lowered the prices of goods, but some AIC workers lost their jobs."),
            EX("Worked example 1: describing the changes", intro="Describe recent changes in industry in AICs.", steps=[
                S("Change 1", text="Heavy industries such as coal, steel and shipbuilding have declined, and factories have closed."),
                S("Change 2", text="High-tech industries and services have grown, usually near universities and in science parks."),
                S("Change 3", text="Many factories have moved to countries with cheaper labour, a trend called relocation."),
                S("Change 4", text="Machines and robots have replaced many workers, so manufacturing needs fewer workers than before."),
            ]),
            EX("Worked example 2: explaining the decline of heavy industry", intro="Explain why heavy industry has declined in many AICs.", steps=[
                S("Competition", text="NICs produce steel and ships at lower cost because wages are lower, so AIC firms lose customers."),
                S("Costs and resources", text="Wages and land are expensive in AICs and some local coal and ore have run out."),
                S("Demand and technology", text="Demand for heavy goods has fallen as people spend on services, and automation needs fewer workers."),
                S("Conclusion", text="Together these changes make old heavy industry unprofitable, so it closes."),
            ]),
            EX("Worked example 3: why high-tech clusters form", intro="Explain why high-tech industries often locate near universities.", steps=[
                S("Skilled workers", text="Universities train the scientists and engineers that firms need."),
                S("Research links", text="Firms can work with university researchers on new products."),
                S("Light inputs", text="Chips and software are light and valuable, so raw materials and transport hardly matter."),
                S("Quality of place", text="Pleasant surroundings and good communications attract the staff firms want."),
            ]),
            TIP("When you explain a change, give two or three linked reasons and one example. For instance: 'Steel in the "
                "United Kingdom declined because of competition from cheaper steel made abroad and because costs at home were high.'"),
            MISTAKE("Thinking AICs stopped making things",
                    "AICs still manufacture a great deal, but in fewer factories with fewer workers and with more advanced goods. "
                    "Do not write that industry has disappeared."),
            MISTAKE("Mixing relocation and automation",
                    "Relocation means the factory moves to another place or country. Automation means machines replace workers, "
                    "whether the factory moves or not."),
            QUIZ("Which is an example of heavy industry that has declined in many AICs?",
                 ["Software writing", "Steel making", "Banking", "Tourism"], 1,
                 "Steel making is a heavy industry that has declined in many AICs.",
                 hint="Pick the one that uses bulky raw materials and large machines.",
                 feedback=["Software is high-tech and has grown.", "", "Banking is a growing service.", "Tourism is a growing service."]),
            QUIZ("Why do many firms in AICs move factories to countries with lower wages?",
                 ["To raise their labour costs", "To cut the cost of making goods", "Because AICs have no workers", "Because robots are banned"], 1,
                 "Lower wages cut production costs, so firms can sell goods more cheaply.",
                 hint="Think about profit.",
                 feedback=["Moving would not raise labour costs.", "", "AICs have workers, but they cost more.", "Robots are widely used in AICs."]),
            TIP("Exam link: Paper 1 asks multiple-choice questions on trends in AIC industry. Paper 2 Section C asks you to "
                "'Describe recent changes in industry in AICs and outline the reasons for them'. Use the headings: decline of heavy industry, "
                "growth of high-tech, relocation, automation.", title="Exam link"),
            PQ("Define an advanced industrial country (AIC) and give two examples.",
               "An AIC is a long-established wealthy country with a high level of industry, technology and income. Examples: the United States and Germany."),
            PQ("Describe two recent changes in industry in AICs.",
               "Heavy industries such as coal, steel and shipbuilding have declined and many factories have closed. High-tech industries "
               "and services have grown, often near universities. Other correct changes: relocation of factories to cheaper countries, and automation."),
            PQ("Outline three reasons for the decline of heavy industry in AICs.",
               "Competition from cheaper goods made in NICs; high wages and costs at home and exhausted local resources; falling demand for "
               "heavy goods; automation that needs fewer workers."),
            PQ("Explain why high-tech industries are growing in AICs.",
               "AICs have universities and skilled workers, money for research, and good communications. High-tech goods are light and "
               "valuable, so raw materials and transport matter little, and governments encourage science parks. Demand for new technology is also strong."),
            SUM("AICs are long-established wealthy industrial countries.",
                "Heavy industry has declined; high-tech industry and services have grown.",
                "Many factories have relocated to cheaper countries, and automation has cut the number of workers needed.",
                "Reasons: competition from NICs, high costs, resource exhaustion, changing demand, new technology and government policy.",
                "Effects: job losses and unemployment in old industrial regions, growth where universities and new firms are found."),
        ],
    ),
    # ------------------------------------------------------------------ 5
    lesson(
        module=MODULE, topic=SEC,
        title="Weber's theory of industrial location",
        slug="ind-webers-theory-of-industrial-location",
        minutes=25,
        summary="Alfred Weber explained where a factory will be sited to keep costs lowest. Transport cost is the key; the material index shows whether the site is near the raw materials, near the market or flexible. Labour and agglomeration can alter the site.",
        objectives=[
            "Outline the aims of Weber's industrial location model.",
            "Outline its main conclusions, using the location triangle.",
            "Calculate and use the material index to classify industries as weight-losing, weight-gaining or footloose.",
            "Outline the limitations of the model, with examples.",
        ],
        key_concepts=["Weber's model", "Least-cost location", "Location triangle", "Transport cost", "Material index",
                      "Localised and ubiquitous materials", "Weight-losing", "Weight-gaining", "Footloose", "Agglomeration"],
        blocks=[
            H("Introduction"),
            T("Why is a sugar mill built beside the cane fields, while a soft-drink bottling plant stands in the middle of a city? "
              "Why do cement works sit near limestone, while bakeries are in every town? "
              "In the early 1900s a German economist, Alfred Weber, tried to answer such questions with a simple model. "
              "In this lesson you learn its aims and main conclusions, and how to use it."),
            H("The aim and the assumptions"),
            D("**Weber's model** aims to explain where a factory will locate if its owner wants to keep production costs as low as "
              "possible. It looks for the **least-cost location**, mainly by working out where transport costs are lowest.",
              title="Weber's aim"),
            T("To make the problem simple, Weber assumed: one product; one market at a fixed place; raw materials found at fixed "
              "places; workers living in fixed places and paid fixed wages; flat land with equal transport in all directions; "
              "and owners who think only of cost. Transport cost is weight times distance times the rate per tonne for each kilometre, "
              "so a heavy load over a long distance costs the most."),
            H("The location triangle"),
            IMG("f5g-ind-weber-triangle.svg",
                alt="Triangle with raw material sources R1 and R2 at the base, a market M at the top and the least-cost factory site L inside, joined to each corner by dashed lines.",
                caption="Figure 1. Weber's location triangle."),
            T("In Figure 1, R1 and R2 are the two sources of raw materials and M is the market. Joining them makes a triangle. "
              "The factory carries material from R1 and R2 to the site, then carries the product to M. The best site, L, is the point "
              "inside the triangle where the total of these transport costs is lowest. The weights decide where L lies: a heavy "
              "raw material pulls the site towards it, and if one corner is much heavier than the other two put together, the site moves right to that corner."),
            H("The material index"),
            D("The **material index (MI)** compares the weight of the localised raw materials with the weight of the finished product.",
              title="Material index", formula=r"\text{MI} = \dfrac{\text{weight of localised raw materials}}{\text{weight of finished product}}"),
            T("**Localised materials** are found only in certain places, such as iron ore, bauxite or sugar cane. "
              "**Ubiquitous materials** are found almost everywhere, such as water, air and sand. Ubiquitous materials cost "
              "almost nothing to move, so they are left out of the top line of the formula."),
            IMG("f5g-ind-material-index.svg",
                alt="Three cases: four units of raw material giving one unit of product with MI 4; one unit plus water giving two units with MI 0.5; one unit giving one unit with MI 1.",
                caption="Figure 2. The three classes of industry by material index."),
            KEY("Three classes of industry", "The index tells you where the factory is pulled.", cards=[
                ["MI more than 1: weight-losing", "The raw material loses weight in processing, so it is cheaper to process it "
                 "near the source. Sites: near raw materials. Examples: sugar milling, cotton ginning, copper smelting, cement, sawmilling."],
                ["MI less than 1: weight-gaining", "Ubiquitous materials, such as water, are added or the product is bulky, "
                 "so the product weighs more than the localised material. Sites: near the market. Examples: bottling soft drinks, brewing, baking bread."],
                ["MI about 1: footloose", "The product weighs about the same as the materials, or materials and products are light and "
                 "valuable. Transport cost hardly matters, so the factory can be sited almost anywhere. Examples: electronics assembly, watches, software, jewellery."],
            ]),
            H("Labour and agglomeration"),
            T("Weber added two more ideas to the pull of transport cost. First, **labour**. If a place with cheap labour saves more "
              "money than the extra transport costs, the factory moves there, away from the least-transport-cost site. "
              "Second, **agglomeration**: when firms cluster together, they share skilled workers, suppliers, repair services, "
              "banks and roads. These savings can draw a factory to the cluster, as in industrial towns and science parks. Too much clustering "
              "can lead to congestion and high land prices, which push some firms out."),
            EX("Worked example 1: calculating the best site", intro="A factory uses 3 tonnes of raw material to make 1 tonne of product. "
               "The raw material is at A and the market is at B, 140 km away. Transport costs 10 FCFA per tonne per km. "
               "Compare the transport cost at three sites: at A, 70 km from A, and at B.", steps=[
                S("Site at A", text="The material travels 0 km. The product travels 140 km.", math=r"1 \times 140 \times 10 = 1400 \text{ FCFA}"),
                S("Site 70 km from A", text="Material 70 km, product 70 km.", math=r"3 \times 70 \times 10 + 1 \times 70 \times 10 = 2100 + 700 = 2800 \text{ FCFA}"),
                S("Site at B", text="The material travels 140 km. The product travels 0 km.", math=r"3 \times 140 \times 10 = 4200 \text{ FCFA}"),
                S("Conclude", text="The lowest cost is at A, near the raw material. This agrees with the material index: MI = 3 / 1 = 3, which is more than 1, so the industry is weight-losing."),
            ]),
            EX("Worked example 2: classify the industry", intro="Suppose 1 tonne of fruit concentrate, mixed with 3 tonnes of "
               "water, makes 4 tonnes of drink. Calculate the material index and say where the factory should be.", steps=[
                S("Find the localised material", text="Only the concentrate is localised. Water is ubiquitous and is left out."),
                S("Calculate", math=r"\text{MI} = \dfrac{1}{4} = 0.25"),
                S("Classify", text="MI is less than 1, so the industry is weight-gaining."),
                S("Locate", text="The product is much heavier than the localised material, so it is cheaper to make the drink near the market."),
            ]),
            EX("Worked example 3: model answer", intro="Outline the main ideas of Weber's industrial location model.", steps=[
                S("Aim", text="Weber tried to explain where a factory will locate to keep costs as low as possible."),
                S("Transport cost", text="Transport cost is the main factor. The factory sits at the least-cost point in the triangle formed by the raw materials and the market."),
                S("Material index", text="If the index is more than 1 (weight-losing) the factory goes near the raw materials. If less than 1 (weight-gaining) it goes near the market. If about 1 it is footloose."),
                S("Labour and agglomeration", text="Cheap labour or the savings from clustering can pull the factory away from the least-transport-cost site."),
            ]),
            H("Limits of the model"),
            KEY("Why Weber's model is only a guide", "The real world is more complicated.", cards=[
                ["Simple assumptions", "Real firms have many raw materials, many products and many markets, and land is not flat."],
                ["Transport costs", "Containers, pipelines and motorways make transport cheaper and less tied to weight and distance. Costs do not always rise evenly with distance."],
                ["Other factors", "Government policy, capital, power, climate, personal choice and the wish to live in a certain town also matter."],
                ["Modern industry", "Many modern industries are footloose. TNCs, fast communications and new technology allow production almost anywhere."],
            ]),
            T("The model still helps. In Cameroon, cotton ginning mills are found near cotton-growing areas of the north and sawmills near forests. "
              "Both are weight-losing. Bottling plants and bakeries stand in towns such as Douala and Yaounde. Both are close to their markets. "
              "Check your textbook for other Cameroonian examples."),
            MISTAKE("Putting water in the top line",
                    "Only localised materials count in the numerator of the formula. Ubiquitous materials such as water, air and sand are left out."),
            QUIZ("A factory uses 8 tonnes of raw material to make 2 tonnes of product. What is the material index and where should it be sited?",
                 ["4, near the raw material", "0.25, near the market", "4, near the market", "0.25, near the raw material"], 0,
                 "MI = 8 / 2 = 4, which is more than 1, so the industry is weight-losing and is sited near the raw material.",
                 hint="Divide the weight of raw material by the weight of product.",
                 feedback=["", "This turns the fraction upside down.", "The value is correct but the location is wrong: weight-losing industries go near raw material.",
                           "The fraction is upside down."]),
            QUIZ("Which of these industries is the best example of a weight-gaining industry?",
                 ["Copper smelting", "Sugar milling", "Bottling soft drinks", "Sawmilling"], 2,
                 "Bottling adds water, which is found everywhere, and the product is heavier than the localised material, so it is sited near the market.",
                 hint="Which one adds heavy water to a small amount of concentrate?",
                 feedback=["Smelting removes waste rock: weight-losing.", "Sugar milling removes most of the cane weight: weight-losing.", "",
                           "Sawmilling removes bark and waste: weight-losing."]),
            TIP("Exam link: Paper 1 has multiple-choice questions on Weber's model and on classifying industries by material index. "
                "Paper 2 Section C asks you to outline the aims and conclusions and to classify industries. A neat sketch of the triangle earns marks.",
                title="Exam link"),
            PQ("State the aim of Weber's industrial location model.",
               "Weber's aim was to explain where a factory will locate if its owner wants production costs to be as low as possible, mainly by finding the point of lowest transport cost."),
            PQ("Draw and label Weber's location triangle, and say what the points represent.",
               "Draw a triangle. Mark the two raw material sources R1 and R2 at the base and the market M at the top. Mark L inside the "
               "triangle, joined to each corner by lines. L is the least-cost site, where total transport cost is lowest."),
            PQ("Define material index and calculate it for an industry that uses 6 tonnes of localised raw material to make 2 tonnes of product. Say where it should be sited.",
               "The material index is the weight of localised raw materials divided by the weight of the finished product. MI = 6 / 2 = 3. "
               "This is more than 1, so the industry is weight-losing and is sited near the raw material."),
            PQ("Give two limits of Weber's model.",
               "It assumes one product, one market and equal transport costs in all directions, which is unrealistic. It ignores government policy, "
               "capital and personal choice, and modern transport and communications make many industries footloose."),
            SUM("Weber's model explains where a factory will locate to keep costs lowest, mainly by minimising transport cost.",
                "The location triangle joins two raw materials and the market; the best site is the least-cost point inside it.",
                "Material index = weight of localised raw materials divided by weight of product.",
                "More than 1 is weight-losing (near raw materials), less than 1 weight-gaining (near market), about 1 footloose.",
                "Cheap labour and agglomeration can move the site, and the model has limits, as many modern industries are footloose."),
        ],
    ),
    # ------------------------------------------------------------------ 6
    lesson(
        module=MODULE, topic=TER,
        title="Globalisation: meaning, characteristics, advantages and disadvantages",
        slug="ind-globalisation",
        minutes=22,
        summary="Globalisation is the growing connection of the world's economies, cultures and people through trade, transnational companies, communications, migration and culture. It brings gains and costs for both LICs and AICs.",
        objectives=[
            "Define globalisation.",
            "Outline the main characteristics of globalisation: trade, transnational companies, communications, migration and culture.",
            "State the advantages and disadvantages of globalisation for LICs.",
            "State the advantages and disadvantages of globalisation for AICs.",
        ],
        key_concepts=["Globalisation", "Transnational company (TNC)", "Free flow of trade", "Communications", "Migration",
                      "Remittances", "Brain drain", "Cultural exchange"],
        blocks=[
            H("Introduction"),
            T("A farmer near Kumba sells cocoa that ends up in chocolate in Europe. Her son sends money to her by mobile phone from "
              "a city abroad. The shirt she wears was made in Asia. The football match on the radio is played in Europe."),
            T("These links across the world are examples of **globalisation**. In this lesson you define it, outline its "
              "main features, and weigh its advantages and disadvantages."),
            H("What is globalisation?"),
            D("**Globalisation** is the process by which countries, businesses and people around the world become more closely "
              "connected through the movement of goods, money, information, ideas and people.", title="Definition: globalisation"),
            D("A **transnational company (TNC)** is a firm that has offices or factories in several countries. Many "
              "mobile phone, fuel, drink and car firms are TNCs.", title="Definition: TNC"),
            H("Main characteristics"),
            IMG("f5g-ind-globalisation.svg",
                alt="Globalisation in the centre linked to trade, transnational companies, communications, migration and culture.",
                caption="Figure 1. Five links that make the world more connected."),
            KEY("Five characteristics", "Each one speeds up the others.", cards=[
                ["Trade", "More goods and services are bought and sold across borders, helped by lower trade barriers, containers and trade agreements."],
                ["Transnational companies", "TNCs spread production across countries, placing each stage where it is cheapest, and sell the same brands everywhere."],
                ["Communications", "Mobile phones, the internet, satellites and air transport let people, money and information move almost instantly."],
                ["Migration", "People move between countries for work, study or safety, and send home money, known as remittances."],
                ["Culture", "Music, films, food, fashion, sport and languages spread around the world, so places grow more alike."],
            ]),
            T("Cameroon shows these links. Cocoa, timber and oil are traded abroad. Mobile phone and fuel companies from other countries "
              "operate in towns across the country. Mobile money moves cash in seconds. Cameroonians study and work abroad and send money home. "
              "Football and music from many countries are followed in Douala and Yaounde."),
            H("Advantages and disadvantages"),
            T("Globalisation does not affect every place in the same way. Look at LICs and AICs separately."),
            CODE(
                "                ADVANTAGES                       DISADVANTAGES\n"
                "LICs     Investment and jobs from TNCs      Profits of TNCs often leave the country\n"
                "         New technology and skills          Local firms cannot compete with imports\n"
                "         Bigger markets for exports         Dependence on a few raw materials\n"
                "         Money sent home by migrants        Brain drain; low pay and poor conditions\n"
                "         Faster access to information       Local culture and languages weakened\n"
                "\n"
                "AICs     Cheaper goods for shoppers         Factory jobs lost to cheaper countries\n"
                "         Larger markets, high TNC profits   Pressure on wages in some jobs\n"
                "         Skilled workers from abroad        Social strain between groups\n"
                "         Wider choice of goods and ideas    Dependence on imports; diseases spread quickly",
                "text", title="Table 1. Advantages and disadvantages of globalisation"),
            T("Notice that a point can be both. A TNC factory creates jobs in an LIC, which is an advantage, but wages may be low and "
              "profits may leave the country, which is a disadvantage. Always say who gains and who loses."),
            EX("Worked example 1: defining and outlining", intro="Define globalisation and outline three of its characteristics.", steps=[
                S("Definition", text="Globalisation is the process by which countries and people become more closely connected through trade, money, information and people."),
                S("Characteristic 1: trade", text="More goods and services are sold across borders, for example cocoa from Cameroon to Europe."),
                S("Characteristic 2: TNCs", text="Firms with offices or factories in many countries place production where it is cheapest."),
                S("Characteristic 3: communications", text="Mobile phones and the internet move money and information instantly, for example mobile money."),
            ]),
            EX("Worked example 2: advantages and disadvantages for an LIC", intro="State two advantages and two disadvantages of globalisation for an LIC.", steps=[
                S("Advantage 1", text="TNCs invest and provide jobs, technology and skills."),
                S("Advantage 2", text="Migrants send money home, and exporters reach bigger markets."),
                S("Disadvantage 1", text="Local firms struggle against cheap imports and TNC profits often leave the country."),
                S("Disadvantage 2", text="Skilled people leave (brain drain) and workers may be paid little and work in poor conditions."),
            ]),
            EX("Worked example 3: effects on an AIC", intro="Explain one advantage and one disadvantage of globalisation for an AIC.", steps=[
                S("Advantage", text="Goods made abroad are cheaper, so shoppers have lower prices and a wider choice."),
                S("Disadvantage", text="Factories that move to cheaper countries cause job losses in old industrial towns."),
                S("Balance", text="Some workers gain and some lose, so governments help through retraining and new industries."),
            ]),
            TIP("A balanced answer names both sides and says who is affected. For example: 'LIC governments gain tax and jobs from TNCs, "
                "but small local firms may lose customers to cheaper imports.'"),
            MISTAKE("Saying globalisation is only about trade",
                    "Trade is only one characteristic. Add TNCs, communications, migration and culture to earn full marks."),
            MISTAKE("Thinking only LICs have problems",
                    "AICs also lose jobs when factories relocate, and face social strain and dependence on imports. Give points for both."),
            QUIZ("Which of the following is the best definition of globalisation?",
                 ["Growth of cities", "Closer links between countries through trade, communications, people and ideas",
                  "Moving from farms to towns", "A single government for the whole world"], 1,
                 "Globalisation means the world is becoming more connected through trade, TNCs, communications, migration and culture.",
                 hint="Look for the word 'links' or 'connected'.",
                 feedback=["Growth of cities is urbanisation.", "", "That is rural-urban migration.", "Globalisation does not mean a world government."]),
            QUIZ("Money sent home by people working abroad is called",
                 ["tariffs", "remittances", "exports", "subsidies"], 1,
                 "Remittances are the money that migrants send to families at home.",
                 hint="Think of money transfers to relatives.",
                 feedback=["Tariffs are taxes on imports.", "", "Exports are goods sold abroad.", "Subsidies are payments by governments to producers."]),
            TIP("Exam link: Paper 1 asks multiple-choice questions on the meaning, features, advantages and disadvantages of globalisation. "
                "Paper 2 Section C asks you to 'Define globalisation, outline its characteristics and state its advantages and disadvantages'. "
                "Use Cameroon examples such as cocoa exports, mobile money and migrants' remittances.", title="Exam link"),
            PQ("Define globalisation.",
               "Globalisation is the process by which countries, businesses and people around the world become more closely connected through trade, money, information, ideas and the movement of people."),
            PQ("Outline three characteristics of globalisation.",
               "Any three of: increased trade across borders; growth of transnational companies; faster communications such as the internet and mobile phones; "
               "increased migration; spread of culture such as music, films and food."),
            PQ("State two advantages and two disadvantages of globalisation for LICs.",
               "Advantages: TNCs bring investment, jobs and technology; migrants send money home; exporters reach larger markets. "
               "Disadvantages: profits of TNCs often leave the country; local firms cannot compete with cheap imports; skilled people leave; local cultures weaken."),
            PQ("Explain why globalisation may cause job losses in an AIC.",
               "Transnational companies move factories to countries where wages and costs are lower. Goods are then imported cheaply into the AIC, "
               "so factories at home close and workers lose their jobs, especially in older industrial towns."),
            SUM("Globalisation is the growing connection of countries and people through trade, money, information, ideas and movement.",
                "Main characteristics: trade, TNCs, communications, migration and culture.",
                "LICs gain investment, jobs, technology and markets, but may lose profits, local firms, skilled people and local culture.",
                "AICs gain cheaper goods and larger markets but may lose factory jobs and face social strain.",
                "Balanced answers name both sides and say who gains and who loses."),
        ],
    ),
    # ------------------------------------------------------------------ 7
    lesson(
        module=MODULE, topic=TER,
        title="Trade: types, world patterns and the balance of trade",
        slug="ind-trade-types-and-patterns",
        minutes=24,
        summary="Trade is the exchange of goods and services. It may be internal or external, bilateral or multilateral, free or protected, visible or invisible. Most world trade is between rich countries; LICs mainly export raw materials.",
        objectives=[
            "Define trade and state its main types.",
            "Define imports, exports and the balance of trade, and calculate it.",
            "Describe the main patterns of world trade.",
            "Explain the patterns, and the position of LICs such as Cameroon in world trade.",
        ],
        key_concepts=["Trade", "Internal and external trade", "Bilateral and multilateral trade", "Free trade", "Protectionism",
                      "Tariff and quota", "Visible and invisible trade", "Imports and exports", "Balance of trade", "Trade bloc"],
        blocks=[
            H("Introduction"),
            T("On market day in Bafoussam, traders from the West region sell plantains and maize to buyers from other regions. "
              "At the port of Douala, trucks load cocoa and timber for ships, and unload rice, cars and machines. "
              "Both are trade, but they work on very different scales. In this lesson you learn the main types of trade, how to calculate a country's balance of trade, and how "
              "world trade is patterned."),
            H("What is trade?"),
            D("**Trade** is the buying and selling of goods and services between people, regions or countries.", title="Definition: trade"),
            D("**Imports** are goods and services bought from other countries. **Exports** are goods and services sold to other countries.",
              title="Imports and exports"),
            IMG("f5g-ind-trade-types.svg",
                alt="Four groups of trade types: internal or external, bilateral or multilateral, free trade or protection, visible or invisible.",
                caption="Figure 1. Types of trade."),
            H("Types of trade"),
            KEY("Four ways to group trade", "A trade can belong to several groups at once.", cards=[
                ["Internal and external", "**Internal (home) trade** takes place inside one country, such as maize from Bafoussam sold in Yaounde. "
                 "**External (foreign) trade** crosses borders and includes imports and exports."],
                ["Bilateral and multilateral", "**Bilateral trade** is between two countries under an agreement. **Multilateral trade** involves many countries, "
                 "for example under the World Trade Organization or a regional group such as CEMAC (check your textbook)."],
                ["Free trade and protectionism", "**Free trade** has no or few barriers. **Protectionism** protects local industry with tariffs "
                 "(taxes on imports), quotas (limits on the amount imported) or subsidies (payments to local producers)."],
                ["Visible and invisible", "**Visible trade** is in physical goods, such as cocoa and cars. **Invisible trade** is in services, "
                 "such as banking, insurance, shipping and tourism."],
            ]),
            H("Balance of trade"),
            D("The **balance of trade** is the difference between the value of a country's visible exports and the value of its visible imports.",
              title="Balance of trade", formula=r"\text{Balance of trade} = \text{value of exports} - \text{value of imports}"),
            T("If exports are worth more than imports, there is a **trade surplus**. If imports are worth more, there is a "
              "**trade deficit**. Many LICs have deficits because they import expensive machines and fuel but export raw materials that sell cheaply."),
            EX("Worked example 1: calculating the balance of trade", intro="A country (the figures are invented for practice) exports goods worth 850 "
               "million FCFA and imports goods worth 1 000 million FCFA in one year. Find its balance of trade.", steps=[
                S("Write the formula", math=r"\text{Balance} = \text{exports} - \text{imports}"),
                S("Substitute", math=r"850 - 1000 = -150 \text{ million FCFA}"),
                S("Say what it means", text="The answer is negative, so there is a trade deficit of 150 million FCFA."),
            ]),
            H("World trade patterns"),
            IMG("f5g-ind-trade-pattern.svg",
                alt="Arrows between AICs, LICs and NICs: manufactured goods flow to LICs, raw materials flow to AICs, and the largest flows are between AICs.",
                caption="Figure 2. Main trade flows, drawn qualitatively and not to scale."),
            T("Describe the patterns first. Most world trade takes place between AICs: North America, western Europe and Japan. "
              "Trade has grown quickly for East Asia, especially China, which exports many manufactured goods. "
              "LICs, including most African countries, take a small share of world trade. Most of what they export is raw material, such as oil, cocoa, cotton, timber and minerals. "
              "They import manufactured goods, machines, vehicles, medicines and fuel."),
            T("Cameroon follows this pattern. Its main exports include crude oil, cocoa, timber, bananas and cotton, and its imports "
              "include machinery, vehicles, fuel products and some foods such as rice. Check your textbook for exact lists and for Cameroon's main trading partners."),
            KEY("Explaining the patterns", "Several causes combine.", cards=[
                ["Unequal resources", "Resources such as oil, minerals and good farmland are unevenly spread, so countries trade to obtain what they lack."],
                ["Level of development", "AICs have the capital, technology and skills to make goods that rich consumers want, so they trade a lot with each other."],
                ["Specialisation", "Countries make what they produce best and cheapest, then exchange. LICs often specialise in raw materials."],
                ["Transport and communications", "Ports, containers and the internet make trade easier, so places with good links trade more."],
                ["Trade blocs and agreements", "Groups such as the European Union remove barriers between members, which boosts trade within the bloc."],
                ["TNCs and history", "TNCs decide where goods are made and sold. Old colonial links still shape routes and partners."],
            ]),
            T("Trade is not always fair. Raw material prices rise and fall and are usually lower than the prices of manufactured goods. "
              "So LICs may have to sell more and more to buy the same imports. Some LICs try to process their raw materials to earn more."),
            EX("Worked example 2: describing and explaining", intro="Describe and explain the pattern of world trade.", steps=[
                S("Describe", text="Most trade is between AICs. East Asia has become a major exporter of manufactured goods. LICs have a small share and sell mainly raw materials."),
                S("Explain: resources and development", text="AICs have capital and technology for high-value goods, while LICs rely on raw materials."),
                S("Explain: links", text="Ports, trade blocs, TNCs and good communications make trade easier between rich countries."),
                S("Conclude", text="So the largest flows are between rich countries, and poorer countries take part mainly as suppliers of raw materials."),
            ]),
            EX("Worked example 3: classifying trade", intro="Classify each: (a) a bank in Douala selling insurance to a firm in Europe; "
               "(b) a market woman in Maroua selling millet in Garoua; (c) a country taxing imported cars heavily.", steps=[
                S("(a)", text="External and invisible: a service sold across borders."),
                S("(b)", text="Internal and visible: goods sold inside one country."),
                S("(c)", text="Protectionism: a tariff on imports protects local industry."),
            ]),
            TIP("Write balance of trade answers as 'surplus' or 'deficit' with the amount and the unit. Never leave a negative "
                "answer without saying what it means."),
            MISTAKE("Confusing balance of trade with balance of payments",
                    "The balance of trade is only visible goods, exports minus imports. The balance of payments is wider and includes "
                    "services and money flows. At this level, use the simple formula."),
            QUIZ("Which of the following is an example of invisible trade?",
                 ["Selling cocoa abroad", "Importing cars", "A foreign tourist paying for a hotel in Limbe", "Exporting timber"], 2,
                 "Tourism is a service, so it is invisible trade. The others are physical goods, which are visible trade.",
                 hint="Invisible trade is in services.",
                 feedback=["Cocoa is a physical good: visible.", "Cars are physical goods: visible.", "",
                           "Timber is a physical good: visible."]),
            QUIZ("A government puts a tax on imported rice to protect local rice farmers. This tax is called",
                 ["a subsidy", "a tariff", "a quota", "a loan"], 1,
                 "A tax on imports is a tariff.",
                 hint="A tax on imports has a special name.",
                 feedback=["A subsidy is a payment to producers, not a tax.", "", "A quota limits the amount imported, not the price.", "A loan is borrowed money."]),
            TIP("Exam link: Paper 1 asks multiple-choice questions on the types of trade and the balance of trade. Paper 2 Section C asks you to "
                "'Define trade, state its types, and describe and explain trade patterns'. Section D can ask about Cameroon's main exports and imports.",
                title="Exam link"),
            PQ("Define trade and state two types of trade.",
               "Trade is the buying and selling of goods and services between people, regions or countries. Types: internal and external trade; bilateral and multilateral trade; "
               "free trade and protectionism; visible and invisible trade."),
            PQ("Explain the difference between visible and invisible trade, with an example of each.",
               "Visible trade is in physical goods, such as cocoa exported from Douala. Invisible trade is in services, such as banking, insurance, shipping or tourism."),
            PQ("A country exports goods worth 1 200 million FCFA and imports goods worth 900 million FCFA. Calculate the balance of trade and say what it shows.",
               "Balance of trade = exports minus imports = 1 200 - 900 = 300 million FCFA. This is a trade surplus, because exports are worth more than imports."),
            PQ("Describe and explain the pattern of trade between AICs and LICs.",
               "LICs mainly export raw materials such as oil, cocoa, cotton and timber, and import manufactured goods, machines and fuel from AICs. "
               "AICs trade most with each other. LICs rely on raw materials because they lack capital, technology and skills for manufacturing, and raw material prices are low and unstable."),
            SUM("Trade is the buying and selling of goods and services; imports are bought from abroad, exports sold abroad.",
                "Types: internal and external, bilateral and multilateral, free trade and protectionism, visible and invisible.",
                "Balance of trade = value of exports minus value of imports: a surplus if positive, a deficit if negative.",
                "Most world trade is between AICs. East Asia is a growing exporter of manufactures. LICs take a small share and mostly export raw materials.",
                "Patterns are explained by unequal resources, level of development, specialisation, transport, trade blocs, TNCs and history."),
        ],
    ),
]
