"""Form 5 Geography: Economic Activities, resources and power (7 lessons, one practice set each)."""

from .dsl import *  # noqa: F403

COURSE = ("geography", "form-5")

MODULE = "Economic Activities"
RES = "Management of primary resources"
POW = "Major sources of power"

LESSONS = []

# ------------------------------------------------------------------ 1. What are resources
LESSONS.append(lesson(
    module=MODULE,
    topic=RES,
    title="What are resources? Meaning, classification and uses",
    slug="res-what-are-resources-and-how-they-are-classified",
    minutes=18,
    summary="What a resource is, how resources are classified as natural or non-natural and as renewable or non-renewable, and the main uses of resources to people and the economy.",
    objectives=[
        "Define resources",
        "Classify resources into renewable and non-renewable, natural and non-natural",
        "Identify the uses of resources",
        "Illustrate each class with examples from different parts of the world",
    ],
    key_concepts=["Resource", "Natural resource", "Non-natural resource", "Renewable resource", "Non-renewable resource", "Primary industry"],
    blocks=[
        H("Introduction"),
        T("Walk through Mokolo market in Yaounde or Mboppi market in Douala. You will see fish from Limbe, timber from the forest of the "
          "East Region, tomatoes from the Western highlands and charcoal for cooking. Every one of these goods began as something "
          "found in nature or made by people."),
        T("In geography, we call such things **resources**. This lesson explains what resources are and how geographers sort them "
          "into groups. The next lessons study forests, fish, minerals and energy in more detail."),
        H("What is a resource?"),
        D("A **resource** is anything found in the environment, or made by people, that is useful and that people have the "
          "knowledge and tools to use.", title="Resource"),
        T("Two points are important. First, a resource must be **useful**. Second, people must be **able** to use it. Crude oil under the "
          "sea was not a resource for people who had no way to drill for it. It became a resource when technology arrived."),
        D("**Primary industries** are activities that take resources directly from nature, such as farming, forestry, fishing "
          "and mining. This is why this topic is called the management of primary resources.", title="Primary industry"),
        H("Classifying resources"),
        T("Geographers classify resources in two ways. The first way asks: who made the resource? The second asks: can it be replaced?"),
        D("**Natural resources** are gifts of nature that people did not make, such as soil, water, forests, fish, minerals, "
          "sunshine and wind.", title="Natural resources"),
        D("**Non-natural resources** are made or developed by people, such as skilled workers, money (capital), machines, roads, "
          "ports, factories and knowledge. They are also called human or human-made resources.", title="Non-natural resources"),
        IMG("f5g-res-classification.svg", alt="Tree diagram: resources divide into natural resources (renewable and non-renewable) and non-natural resources (skills, capital, roads, factories, knowledge)",
            caption="Figure 1. The classification of resources."),
        KEY("Renewable and non-renewable", "Natural resources are split again according to how fast they can be replaced.", cards=[
            ["Renewable", "Can be replaced naturally within a human lifetime if they are used with care. Examples: forests, fish, water, soil, sunshine, wind."],
            ["Non-renewable", "Take millions of years to form, so once used they are gone for practical purposes. Examples: oil, coal, natural gas, iron ore, copper, gold."],
        ]),
        T("Examples come from every kind of country. Brazil (a newly industrialised country, NIC) has huge forests. Norway (an advanced "
          "industrial country, AIC) has fish and oil under the North Sea. Chad (a low-income country, LIC) shares Lake Chad with "
          "Cameroon, Nigeria and Niger. Each of these resources can be placed in the tree above."),
        TIP("Renewable does not mean unlimited. A forest is renewable, but if trees are cut faster than they grow, the forest "
            "disappears. Fish are renewable, but overfishing can wipe out a fish stock. Always add this point in an exam answer.",
            title="Renewable resources can still run out"),
        H("Uses of resources"),
        T("Resources are the base of every economy. Their main uses are shown below."),
        KEY("Main uses of resources", "", cards=[
            ["Food", "Farm crops, fish and animals feed people."],
            ["Shelter and construction", "Timber, sand, stone and cement (from limestone) build houses, roads and bridges."],
            ["Energy", "Oil, gas, coal, firewood and water give heat, light and power."],
            ["Raw materials", "Factories turn cotton into cloth, iron ore into steel and logs into furniture."],
            ["Income and trade", "Cocoa, timber, oil and bananas are exported and earn foreign money."],
            ["Jobs", "Farming, fishing, mining and transport employ millions of people."],
        ]),
        T("In Cameroon, cocoa, coffee, timber and oil are examples of resources that earn money from abroad. Water from the Sanaga "
          "and other rivers also supports farming and electricity."),
        EX("Model answer 1: define and classify", intro="Define the term resources and classify resources into renewable and non-renewable, "
           "giving two examples of each.", steps=[
            S("Define", text="A resource is anything in the environment, or made by people, that is useful and that people can use."),
            S("Renewable resources", text="These can be replaced naturally if used carefully. Examples are forests and fish."),
            S("Non-renewable resources", text="These cannot be replaced within a human lifetime. Examples are oil and iron ore."),
            S("Add the warning", text="Renewable resources can still be destroyed by overuse, for example overfished waters."),
        ]),
        EX("Model answer 2: natural and non-natural", intro="Distinguish natural resources from non-natural resources.", steps=[
            S("Natural", text="Natural resources are provided by nature, such as soil, water, minerals and sunshine."),
            S("Non-natural", text="Non-natural resources are created or developed by people, such as skilled labour, capital, roads and machines."),
            S("Link", text="The two work together: a fish stock (natural) is only useful when fishermen have boats and cold stores (non-natural)."),
        ]),
        TIP("Paper 1 asks multiple-choice questions on definitions and classification. Paper 2 Section C (human geography) may ask "
            "you to define resources, classify them and give uses. Use the tree diagram as a quick sketch in your answer.",
            title="Exam link"),
        MISTAKE("Confusing non-natural with non-renewable", "These are different pairs. Natural and non-natural ask who made the "
                "resource. Renewable and non-renewable ask whether it can be replaced. A road is non-natural; oil is natural AND non-renewable."),
        MISTAKE("Calling every fuel non-renewable", "Firewood, charcoal and biofuels come from plants and can be regrown, so they can be "
                "renewable. Coal, oil and gas are non-renewable."),
        QUIZ("Which of these is a natural, non-renewable resource?", ["Fish", "Copper ore", "A road", "Sunshine"], 1,
             "Copper ore is a mineral formed over millions of years, so it is natural and non-renewable.", hint="Look for something nature made that cannot be replaced.",
             feedback=["Fish are natural but renewable, because they breed.", "", "A road is made by people, so it is non-natural.", "Sunshine is natural but renewable."]),
        QUIZ("A government builds a new port at Kribi. In which group of resources does the port belong?", ["Natural, renewable", "Natural, non-renewable", "Non-natural", "Primary"], 2,
             "A port is built by people, so it is a non-natural (human-made) resource.", hint="Ask who made it.",
             feedback=["Nothing about a port is made by nature.", "Nothing about a port is made by nature.", "", "Primary describes industries such as farming and mining, not a kind of resource."]),
        PQ("Define the term resource and give two examples of natural resources found in Cameroon.",
           "A resource is anything in the environment, or made by people, that is useful and that people can use. Two natural resources in "
           "Cameroon are forests (timber) and water from rivers such as the Sanaga. Oil and fish from the Atlantic coast are also correct."),
        PQ("Classify the following into renewable and non-renewable: coal, wind, bauxite, soil.",
           "Renewable: wind and soil. Non-renewable: coal and bauxite (a mineral that is the ore of aluminium). Soil is renewable only "
           "when it is protected, because erosion can remove it quickly."),
        PQ("State four uses of resources to people and to a country's economy.",
           "Any four of: food; shelter and construction materials; energy for homes, industry and transport; raw materials for factories; "
           "exports that earn foreign money; jobs and income; taxes for the government."),
        SUM("A resource is anything useful in the environment, or made by people, that people can use.",
            "Natural resources come from nature; non-natural resources are made or developed by people.",
            "Natural resources are renewable (can be replaced) or non-renewable (cannot be replaced quickly).",
            "Renewable resources can still be destroyed by overuse.",
            "Resources give food, shelter, energy, raw materials, trade income and jobs."),
    ],
))

# ------------------------------------------------------------------ 2. Conservation
LESSONS.append(lesson(
    module=MODULE,
    topic=RES,
    title="Conserving natural resources: why, how and the challenges",
    slug="res-conserving-natural-resources",
    minutes=20,
    summary="The meaning of conservation and preservation, why natural resources must be protected, the main methods of protecting them and the challenges that make this difficult.",
    objectives=[
        "Define conservation and preservation and state the difference",
        "Explain why natural resources should be conserved",
        "Outline methods of conserving resources",
        "Outline the challenges of conservation and preservation",
    ],
    key_concepts=["Conservation", "Preservation", "Sustainable use", "Protected area", "Future generations", "Challenges of conservation"],
    blocks=[
        H("Introduction"),
        T("Ask an elder in a village near Bamenda about the hills of their childhood. Many will describe thick forest and streams that "
          "never dried up. Today some of those hills are bare and some streams run only in the rainy season."),
        T("Resources do not disappear on their own. People use them, and sometimes use them too fast. Conservation is how societies try "
          "to make sure a resource is still there for children and grandchildren."),
        H("Conservation and preservation"),
        D("**Conservation** means using natural resources wisely, so that they last and are available to future generations. "
          "Conserved resources are still used.", title="Conservation"),
        D("**Preservation** means protecting a part of nature and keeping it untouched, with no cutting, fishing, farming or mining. "
          "Human use is kept out or strictly limited.", title="Preservation"),
        IMG("f5g-res-conservation.svg", alt="Scale from no use to heavy use: preservation at the no-use end, conservation at wise use",
            caption="Figure 1. Preservation allows no use. Conservation allows wise use."),
        T("The word **sustainable** is often used with conservation. Sustainable use means using a resource at a speed that lets it "
          "replace itself, or using it in a way that does not damage the future."),
        H("Why conserve natural resources?"),
        KEY("Four main reasons", "", cards=[
            ["For future generations", "Resources such as oil and minerals cannot be replaced. If we use them all now, nothing is left for later."],
            ["To protect the environment", "Trees, wetlands and wildlife keep soil, water and air healthy and hold back floods."],
            ["To protect jobs and income", "Fishermen, loggers, farmers and miners depend on resources lasting."],
            ["To keep nature in balance", "Every plant and animal has a place. Losing one species can harm others (biodiversity)."],
        ]),
        H("How resources are conserved"),
        T("Governments, communities and companies use many methods. Examples come from rich and poor countries alike."),
        KEY("Main methods", "", cards=[
            ["Laws and protected areas", "National parks, forest reserves and marine reserves limit use. Kenya's national parks protect wildlife; Cameroon has parks and reserves too."],
            ["Replanting", "Trees are planted to replace those cut (reforestation) or on bare land (afforestation)."],
            ["Quotas and seasons", "Fishing quotas, closed seasons and net-size rules protect fish stocks. Norway and Iceland use quotas."],
            ["Recycling and saving", "Recycling metals and plastic and saving energy reduce the need for new resources."],
            ["Education", "Teaching farmers, fishermen and children why protection matters changes habits."],
            ["Alternatives", "Improved cooking stoves, gas and solar power reduce the cutting of trees for firewood."],
        ]),
        H("Challenges of conservation and preservation"),
        T("If conservation is so useful, why is it difficult? The Board asks you to outline the challenges, so learn them as a group."),
        KEY("Challenges", "", cards=[
            ["Poverty", "A family with no other income may cut trees or fish small fish to survive today."],
            ["Population growth", "More people need more food, fuel and land, which puts pressure on resources."],
            ["Weak law enforcement", "Few guards, long borders and corruption make illegal cutting, hunting and fishing hard to stop."],
            ["Conflicting interests", "Governments want income from logging and mining, while others want the land protected."],
            ["Cost and lack of technology", "Patrol boats, guards, replanting and recycling plants are expensive for poor countries."],
            ["Shared resources", "Fish, rivers and forests cross borders, so one country cannot protect them alone."],
        ]),
        EX("Model answer 1: why conserve?", intro="Explain why natural resources should be conserved.", steps=[
            S("Point 1: future generations", text="Non-renewable resources such as oil cannot be replaced, so careful use leaves some for later."),
            S("Point 2: environment", text="Forests protect soil from erosion and reduce floods, so cutting them without replanting harms farmland and homes."),
            S("Point 3: economy", text="Fishermen and farmers need healthy stocks and soil to earn a living year after year."),
            S("Conclusion", text="Conservation therefore protects people, nature and the economy together."),
        ]),
        EX("Model answer 2: challenges", intro="Outline three challenges faced in conserving natural resources.", steps=[
            S("Poverty", text="Poor families may cut trees for firewood or sell timber because they have no other income, even if they know the harm."),
            S("Weak enforcement", text="Parks and reserves are large, and there are too few guards, so illegal logging and poaching continue."),
            S("Conflict of interest", text="A government may want money from mining or logging, which can clash with protecting the same land."),
        ]),
        TIP("Do not just list. For each point give a short reason or example, as in the model answers. One short sentence of explanation "
            "turns a list point into a mark-winning point.", title="Exam technique"),
        TIP("Conservation and preservation can appear in Paper 1 (definitions) and in Paper 2 Section C. For the conservation of a particular "
            "resource, see the forest, fish and mineral lessons.", title="Exam link"),
        MISTAKE("Saying conservation means not touching nature", "That is preservation. Conservation means wise use, such as cutting only "
                "some trees and replanting."),
        MISTAKE("Giving only 'make laws' as a method", "A law means little without enforcement, replanting or alternatives. Always name a "
                "specific method such as quotas, protected areas or replanting."),
        QUIZ("A fisheries officer limits each boat to a set weight of fish and closes the sea for three months a year. This is an example of", ["Preservation", "Conservation", "Pollution", "Deforestation"], 1,
             "Fishing is still allowed, but in a controlled way so the stock recovers. That is conservation.", hint="Is fishing completely banned?",
             feedback=["Preservation would stop all fishing in the area.", "", "Pollution is damage, not protection.", "Deforestation is forest clearing, not fishing."]),
        QUIZ("Which is a challenge of conservation in a poor country?", ["Too many national parks", "Families who need firewood and farmland now", "Too much rain", "Cheap technology"], 1,
             "Poverty pushes people to use resources for short-term survival.", hint="Think about a family's daily needs.",
             feedback=["Few countries have too many parks; the challenge is protecting the ones that exist.", "", "Rainfall is not a conservation challenge.", "Technology is usually expensive, which is the challenge."]),
        PQ("Distinguish between conservation and preservation of resources.",
           "Conservation means the wise use of resources so that they last for future generations; the resources are still used, for example "
           "selective logging with replanting. Preservation means keeping an area untouched, with no use at all, for example a strict nature reserve."),
        PQ("Give three reasons why natural resources should be conserved.",
           "(1) So that future generations can use them, especially non-renewable resources. (2) To protect the environment, for example "
           "forests prevent soil erosion and floods. (3) To protect jobs and income for farmers, fishermen and loggers. Biodiversity can also be given."),
        PQ("Outline three challenges to the conservation of natural resources.",
           "Poverty makes people use resources for survival. Weak law enforcement allows illegal logging and fishing. Population growth increases "
           "the demand for land, food and fuel. Other answers: cost of protection, conflicts between development and protection, shared resources across borders."),
        SUM("Conservation is the wise use of resources so that they last; preservation is keeping nature untouched.",
            "We conserve resources for future generations, for the environment, for jobs and for the balance of nature.",
            "Main methods: protected areas, replanting, quotas and seasons, recycling and saving, education, alternatives.",
            "Main challenges: poverty, population growth, weak enforcement, conflicting interests, cost and shared resources.",
            "In an exam answer, give a reason or an example for every point."),
    ],
))

# ------------------------------------------------------------------ 3. Forest resources
LESSONS.append(lesson(
    module=MODULE,
    topic=RES,
    title="Forest resources: types, distribution, importance and problems",
    slug="res-forest-resources",
    minutes=24,
    summary="The main types of forest and where they grow, why forests matter to the economy, the problems of deforestation and illegal logging, their environmental impacts, and the solutions.",
    objectives=[
        "Outline the types of forest and illustrate their world distribution on a sketch map",
        "Outline the importance of forest exploitation to the economy",
        "Describe the problems of forest exploitation, their environmental impacts and attempted solutions",
        "Give examples from low-income, newly industrialised and advanced countries",
    ],
    key_concepts=["Tropical rainforest", "Temperate forest", "Coniferous (boreal) forest", "Hardwood and softwood", "Deforestation", "Illegal logging", "Sustainable logging", "Reforestation"],
    blocks=[
        H("Introduction"),
        T("Trucks loaded with huge logs leave the forests of the East and South Regions of Cameroon for the port of Douala. "
          "Timber from the forest is one of the country's important exports. It also supports sawmills, drivers and traders along the way."),
        T("Forests are a **renewable** resource, but only if they are managed well. This lesson shows where the world's forests are, "
          "why they matter, and what goes wrong when they are overused."),
        H("Types of forest"),
        D("A **forest** is a large area covered mainly by trees growing close together.", title="Forest"),
        KEY("Three main types", "They differ in climate, tree species and use.", cards=[
            ["Tropical rainforest", "Hot, wet climate near the Equator. Tall evergreen trees in layers. Mostly hardwoods such as mahogany, iroko and sapele. Hardwood is hard, slow growing and valuable."],
            ["Temperate forest", "Mild climates in mid-latitudes. Broadleaf trees such as oak and beech (many lose their leaves in autumn) and mixed forest. Much has been cleared for farms and towns."],
            ["Coniferous (boreal) forest", "Cold northern lands. Needle-leaved evergreens such as pine, spruce and fir. Softwoods grow fast and in large stands, ideal for paper and construction."],
        ]),
        T("Savanna regions also have trees, such as the woodland of the Adamawa plateau, but the large forest regions are the three types above. "
          "Cameroon has dense tropical rainforest in the south and east and thinner woodland towards the north."),
        H("World distribution"),
        IMG("f5g-res-forest-map.svg", alt="Sketch map of the world: tropical rainforest in the Amazon basin, Congo basin and South-East Asia; coniferous forest across northern Canada and Eurasia; temperate forest in eastern USA, Europe and eastern China; Cameroon marked",
            caption="Figure 1. Simplified sketch map of the main forest regions (approximate)."),
        T("Describe the map from the Equator outwards."),
        KEY("Where the forests are", "", cards=[
            ["Tropical rainforest", "The Amazon basin in Brazil and its neighbours; the Congo basin of Central Africa, including southern Cameroon; South-East Asia, such as Indonesia and Malaysia."],
            ["Temperate forest", "Eastern United States, western and central Europe and eastern China."],
            ["Coniferous forest", "A broad belt across northern Canada, Scandinavia and northern Russia (Siberia)."],
        ]),
        TIP("When you draw a sketch map in an exam, draw simple continents, shade the forests lightly, label them and add a key. A neat sketch "
            "with three or four correct areas earns more than a perfect outline. Mark the Equator and the Tropics to place the forests.", title="Sketch map technique"),
        H("Importance of forests to the economy"),
        KEY("Why forests matter", "", cards=[
            ["Timber and wood products", "Logs, sawn wood, plywood and furniture are exported or used at home. Softwood is made into paper and pulp."],
            ["Fuelwood", "Firewood and charcoal are the main cooking fuels for many households in Africa."],
            ["Jobs and income", "Loggers, sawmill workers, drivers, carpenters and traders earn a living from forests."],
            ["Foreign exchange", "Timber exports earn money from abroad and pay taxes to government."],
            ["Other products", "Honey, fruits, medicinal plants, bush meat and rubber come from forests."],
            ["Environmental services", "Forests store carbon, protect soil, keep rivers flowing and shelter wildlife and tourists."],
        ]),
        H("Problems, impacts and solutions"),
        D("**Deforestation** is the permanent clearing of forest, so that trees are removed faster than they can regrow.", title="Deforestation"),
        D("**Illegal logging** is cutting timber without permission or outside the rules, for example in protected areas or beyond the "
          "allowed quantity. It loses tax money and is difficult to control.", title="Illegal logging"),
        IMG("f5g-res-deforestation.svg", alt="Diagram: causes of deforestation (farming, logging, firewood, roads) lead to impacts (soil erosion and floods, loss of wildlife, less rain, more carbon dioxide); solutions at the bottom",
            caption="Figure 2. Causes, impacts and solutions of deforestation."),
        KEY("Problems of forest exploitation", "", cards=[
            ["Forest clearance for farming", "Farmers burn and clear forest for crops, and large companies clear land for plantations such as palm oil."],
            ["Over-logging and illegal logging", "More trees are cut than grow back. Careless logging damages young trees around the one that is felled."],
            ["Fuelwood demand", "Growing towns need firewood and charcoal; this strips nearby forest."],
            ["Mining, dams and roads", "These open up the forest to settlers and loggers."],
            ["Fires", "Dry-season fires, set for farming or by accident, spread into forest."],
        ]),
        KEY("Environmental impacts", "", cards=[
            ["Soil erosion", "Bare soil is washed away by heavy rain and farmland loses fertility."],
            ["Floods and landslides", "Without trees, rainwater runs quickly into rivers. Steep hills may slip."],
            ["Loss of biodiversity", "Animals and plants lose their homes; some species can disappear."],
            ["Climate effects", "Fewer trees mean less carbon stored and less moisture returned to the air, so the local climate may become drier and hotter."],
        ]),
        KEY("Attempted solutions", "", cards=[
            ["Replanting", "Reforestation (replanting cleared forest) and afforestation (planting on bare land)."],
            ["Protected areas", "National parks and forest reserves where logging is banned or limited."],
            ["Sustainable logging", "Felling only selected mature trees, issuing licences and quotas, and allowing the forest to regrow."],
            ["Law enforcement", "Patrols, tracking of timber and punishment of illegal logging."],
            ["Reducing the need to clear", "Agro-forestry, better farming methods and improved cooking stoves."],
        ]),
        T("Examples (not case studies): Brazil, a newly industrialised country, has lost large areas of Amazon forest to cattle ranches and "
          "farms, and has created protected areas to slow this. Canada, an advanced industrial country, replants cut areas of its coniferous "
          "forest. In many low-income countries in Central Africa, illegal logging and firewood demand are major problems."),
        EX("Model answer 1: describe a distribution", intro="Describe the world distribution of tropical rainforest.", steps=[
            S("Where", text="Tropical rainforest lies in a belt close to the Equator, mostly between the Tropics of Cancer and Capricorn."),
            S("Examples", text="There are three main areas: the Amazon basin of South America, the Congo basin of Central Africa (including southern Cameroon) and South-East Asia."),
            S("Pattern", text="It grows where the climate is hot and wet all year, so it is absent from dry deserts and cooler regions."),
            S("Sketch", text="Draw a simple world map, shade these three areas and label them, then add the Equator."),
        ]),
        EX("Model answer 2: problems and solutions", intro="Describe the problems of forest exploitation and the solutions that have been tried.", steps=[
            S("Problem: clearing and over-logging", text="Forests are cleared for farms and logged faster than they regrow. Illegal logging adds to the loss."),
            S("Impact", text="Soil erosion, floods, and the loss of animals and plants follow, and less carbon is stored."),
            S("Solution: replanting and protected areas", text="Governments plant trees, set up reserves and parks, and ban logging in them."),
            S("Solution: sustainable logging", text="Only selected trees are cut under licence, so the forest can regrow and jobs continue."),
            S("Challenge", text="Poverty and weak law enforcement still allow clearing, so the solutions only partly work."),
        ]),
        MISTAKE("Naming only the continent", "Say 'the Amazon basin in South America', not just 'South America'. Name the actual forest region and, where possible, a country."),
        MISTAKE("Treating deforestation as only logging", "Clearing land for farms and firewood causes much of the loss, not only timber companies. Mention several causes."),
        MISTAKE("Saying forests are renewable so there is no problem", "Trees take decades to grow. If they are cut faster than they regrow, the forest disappears."),
        TIP("Forests appear in Paper 1 (types, distribution, definitions) and in Paper 2 Section C (importance, problems and solutions, often with a sketch map).", title="Exam link"),
        QUIZ("Which type of forest produces mainly softwood used for paper?", ["Tropical rainforest", "Coniferous forest", "Mediterranean scrub", "Mangrove"], 1,
             "Coniferous forests grow in cold northern lands. Their softwood grows fast and is used for paper and building.", hint="Think of pine and spruce.",
             feedback=["Rainforests mostly give hardwoods such as mahogany.", "", "Scrub does not give large quantities of timber.", "Mangroves are coastal swamp trees, not a main source of paper."]),
        QUIZ("A river floods more often after the forest on the hills above it is cleared. The best reason is that", ["trees make more rain fall", "without trees rainwater runs quickly into the river", "forests are always flooded", "farmers dig channels"], 1,
             "Tree roots and leaves slow rainwater and soak it up. After clearing, water runs off quickly.", hint="What do trees do to rainwater?",
             feedback=["Trees do not make more rain fall in this simple way.", "", "Forests are not always flooded.", "Farmers digging channels is not the main cause."]),
        PQ("Name three areas of tropical rainforest in the world.",
           "The Amazon basin (Brazil and neighbouring countries), the Congo basin in Central Africa (including southern Cameroon) and South-East Asia (Indonesia and Malaysia)."),
        PQ("Outline three ways in which forest exploitation is important to a country's economy.",
           "Timber and products such as plywood and furniture are exported and earn foreign exchange. Forests give jobs to loggers, sawmill workers, "
           "drivers and traders. Fuelwood and charcoal supply cooking energy. Other answers: paper, medicines and tourism."),
        PQ("Describe two environmental impacts of deforestation and two attempted solutions.",
           "Impacts: soil erosion and floods because there are no roots and leaves to protect the soil; loss of habitats and species. "
           "Solutions: replanting trees (reforestation) and creating protected areas such as national parks, or sustainable logging with quotas."),
        SUM("The main forest types are tropical rainforest (hardwoods), temperate forest and coniferous forest (softwoods).",
            "Rainforests lie near the Equator in the Amazon, Congo basin and South-East Asia; coniferous forest forms a northern belt.",
            "Forests give timber, fuel, jobs, foreign exchange and environmental services.",
            "Deforestation and illegal logging cause erosion, floods, loss of wildlife and climate effects.",
            "Solutions include replanting, protected areas, sustainable logging and law enforcement."),
    ],
))

# ------------------------------------------------------------------ 4. Fish resources
LESSONS.append(lesson(
    module=MODULE,
    topic=RES,
    title="Fish resources: types of fishing, fishing grounds, problems and solutions",
    slug="res-fish-resources",
    minutes=24,
    summary="The main types of fishing, the world's chief fishing grounds and why fish gather there, the importance of fishing, and the problems of overfishing and pollution with their impacts and solutions.",
    objectives=[
        "Outline the types of fishing and illustrate the main fishing grounds on a sketch map",
        "Outline the importance of fishing to the economy",
        "Describe the problems of overfishing and pollution, their impacts and attempted solutions",
        "Explain why fish stocks are renewable but can be depleted",
    ],
    key_concepts=["Inland fishing", "Inshore (coastal) fishing", "Deep-sea fishing", "Fish farming", "Fishing ground", "Overfishing", "Fishing quota"],
    blocks=[
        H("Introduction"),
        T("Early in the morning at Limbe or Douala beach, canoes arrive with fish. Women buy and smoke the fish, and traders carry it to "
          "markets inland. In the Far North, people fish in the Logone and in Lake Chad. Fish gives protein, jobs and income to millions "
          "of families in West and Central Africa."),
        T("Fish are a renewable resource. The stock replaces itself by breeding, but only if enough adult fish are left."),
        H("Types of fishing"),
        KEY("Four main types", "", cards=[
            ["Inland fishing", "In rivers, lakes and ponds, such as the Benue and Lake Chad. Usually small scale, with nets, traps and canoes."],
            ["Inshore (coastal) fishing", "Close to the shore in small boats, often by local people. Also called artisanal fishing."],
            ["Deep-sea (commercial) fishing", "Large trawlers and factory ships travel far out to sea. They carry freezers and huge nets."],
            ["Fish farming (aquaculture)", "Fish are raised in ponds, cages or tanks and harvested like crops."],
        ]),
        D("A **fishing ground** is an area of sea or inland water where fish are caught in large numbers.", title="Fishing ground"),
        D("**Subsistence fishing** catches fish mainly for the fisher's own family. **Commercial fishing** catches fish to sell for profit.", title="Subsistence and commercial"),
        H("World distribution of fishing grounds"),
        IMG("f5g-res-fishing-map.svg", alt="Sketch map of the world with seven fishing grounds numbered: North-East Atlantic, North-West Atlantic, North-West Pacific, North-East Pacific, South-East Pacific, West Africa coast, South-West Africa; Cameroon coast marked",
            caption="Figure 1. Simplified sketch map of the main fishing grounds (approximate)."),
        T("Most of the world's fish are caught in a few areas. Learn the list and the pattern."),
        KEY("Main fishing grounds", "", cards=[
            ["North-East Atlantic", "The North Sea and the seas off Norway and Iceland."],
            ["North-West Atlantic", "The Grand Banks off Newfoundland, Canada."],
            ["North-West Pacific", "Seas around Japan, China and eastern Russia."],
            ["South-East Pacific", "Off Peru and Chile."],
            ["Africa", "The coast of West Africa, including the Gulf of Guinea, and the coast of south-west Africa."],
            ["North-East Pacific", "The seas off Alaska."],
        ]),
        T("Why do fish gather there? Four reasons explain most fishing grounds."),
        KEY("Why fishing grounds are rich", "", cards=[
            ["Shallow continental shelf", "Sunlight reaches the sea floor, so plants and tiny animals (plankton) grow in large amounts."],
            ["Plankton", "Plankton is the food of small fish, which are eaten by bigger fish."],
            ["Meeting of ocean currents", "Where a warm and a cold current meet, plankton and fish are concentrated."],
            ["Upwelling", "Off Peru and south-west Africa, winds push surface water away and cold water rich in food rises."],
        ]),
        T("Other factors help: indented coasts give shelter for ports, nearby markets, and cold storage and good roads to reach buyers."),
        H("Importance of fishing"),
        T("Fish gives cheap **protein**. Fishing and the jobs around it (boat-building, net-making, smoking, canning, transport and selling) "
          "employ many people. Fish products such as fish meal (animal feed) and oil are exported. Many coastal communities of Cameroon "
          "depend on fish for food and income."),
        H("Problems, impacts and solutions"),
        D("**Overfishing** is catching fish faster than the stock can breed, so the number of fish falls.", title="Overfishing"),
        IMG("f5g-res-overfishing.svg", alt="Graph over time: fish stock falls as heavy fishing begins; catch rises, peaks, then falls when the stock collapses",
            caption="Figure 2. How overfishing leads to a collapse (an illustration, not real data)."),
        KEY("Problems", "", cards=[
            ["Overfishing", "Too many boats and modern nets (trawlers) take young and breeding fish, so the stock cannot recover."],
            ["Illegal and unreported fishing", "Boats fish without licences or inside another country's waters, for example off West Africa."],
            ["Harmful methods", "Very small net holes, poison or explosives destroy young fish and coral."],
            ["Pollution", "Oil spills, sewage, plastic and chemicals kill fish or make them unsafe to eat."],
            ["Poor storage and transport", "Without ice or cold stores, much of a small fisher's catch spoils."],
        ]),
        KEY("Impacts", "", cards=[
            ["Falling catches", "Fishermen have to go further for fewer fish. Some stocks collapse. The cod stocks off Newfoundland collapsed in the early 1990s."],
            ["Loss of marine life", "Food chains are damaged, and corals and sea turtles can be harmed."],
            ["Food and job losses", "Coastal families lose protein and income."],
        ]),
        KEY("Attempted solutions", "", cards=[
            ["Quotas and licences", "A quota limits how many tonnes a boat or country may catch."],
            ["Closed seasons and net rules", "Fishing is banned in the breeding season, and net holes must be large enough to let young fish escape."],
            ["Marine protected areas", "Parts of the sea where fishing is limited so stocks can recover."],
            ["Patrols and agreements", "Countries control a 200-nautical-mile zone (the exclusive economic zone) and sign agreements to share stocks."],
            ["Fish farming", "Raising fish in ponds eases pressure on wild fish."],
            ["Pollution control", "Treating sewage, controlling oil spills and clearing plastic."],
        ]),
        T("Examples: Norway and Iceland, advanced industrial countries, use strict quotas. Peru, a middle-income country, controls its anchovy "
          "catch with seasons. Many low-income countries find patrolling their coasts expensive."),
        EX("Model answer 1: fishing grounds", intro="Describe the distribution of the world's main fishing grounds and give two reasons for it.", steps=[
            S("Distribution", text="Most grounds are in the North Atlantic (North Sea, Grand Banks), the North-West Pacific off Japan and China, the South-East Pacific off Peru and Chile, and off the west coast of Africa."),
            S("Reason 1", text="They lie on shallow continental shelves where sunlight reaches the bottom and plankton grows."),
            S("Reason 2", text="In some places warm and cold currents meet, or cold water rises (upwelling) and brings food for fish."),
            S("Sketch", text="Draw a simple world map and mark each ground with a numbered circle and a key."),
        ]),
        EX("Model answer 2: overfishing", intro="Explain the problem of overfishing and suggest two solutions.", steps=[
            S("Meaning", text="Overfishing is catching fish faster than they can breed."),
            S("Cause", text="Large trawlers with modern nets catch young and breeding fish. Too many boats fish the same area."),
            S("Result", text="The stock falls, catches fall, and fishing families lose food and income."),
            S("Solution 1", text="Quotas and closed seasons let the stock recover."),
            S("Solution 2", text="Larger net holes and marine protected areas protect young fish."),
        ]),
        TIP("Fishing questions appear in Paper 1 (grounds, types, definitions) and in Paper 2 Section C (problems and solutions). Use the "
            "problem, impact, solution pattern in your answers.", title="Exam link"),
        MISTAKE("Saying fish cannot run out because they are renewable", "Fish breed, but if too many are caught, there are not enough adults left to breed and the stock collapses."),
        MISTAKE("Giving reasons without saying how they attract fish", "Do not just write 'shallow sea'. Say that sunlight reaches the bottom, plankton grows and fish feed on it."),
        QUIZ("Which is the main reason why many fishing grounds lie over continental shelves?", ["The water is warm", "Sunlight reaches the sea floor so plankton grows", "There are no waves", "Ships can anchor"], 1,
             "Shallow water lets sunlight reach the bottom, so plankton grows. This feeds the whole food chain.", hint="What do small fish eat?",
             feedback=["Warm water alone does not make a rich fishing ground; cold water often holds more food.", "", "Waves are not the reason.", "Anchoring is not the reason fish gather."]),
        QUIZ("A fishing quota is", ["a type of net", "a limit on the amount of fish that may be caught", "a fish farm", "a tax on boats"], 1,
             "A quota sets the maximum weight of fish a boat or country may catch in a season.", hint="Think of a fixed share.",
             feedback=["A net is equipment, not a quota.", "", "A fish farm is aquaculture.", "A tax is money, not a limit on catch."]),
        PQ("Name and describe two types of fishing.",
           "Inland fishing takes place in rivers and lakes, such as Lake Chad, usually on a small scale. Deep-sea fishing uses large trawlers "
           "that travel far from land with freezers. Inshore fishing (close to the coast with small boats) and fish farming are also correct."),
        PQ("Give three reasons for the formation of rich fishing grounds.",
           "Shallow continental shelves let sunlight reach the bottom, so plankton grows. Warm and cold currents meeting concentrate plankton and fish. "
           "Upwelling brings nutrient-rich cold water to the surface. Indented coasts and nearby markets also help."),
        PQ("Describe two problems of fishing and two solutions that have been tried.",
           "Problems: overfishing, which reduces the stock, and pollution from oil and sewage, which kills fish. Solutions: quotas, closed seasons "
           "and net-size rules to protect breeding fish, and treating waste or controlling spills to reduce pollution."),
        SUM("Fishing is inland, inshore, deep-sea or fish farming.",
            "Main grounds are the North Atlantic, North-West Pacific, South-East Pacific and off the west and south-west coast of Africa.",
            "Grounds are rich where shallow shelves, plankton, meeting currents or upwelling occur.",
            "Fishing gives protein, jobs, exports and income.",
            "Overfishing and pollution reduce stocks; quotas, closed seasons, protected areas and fish farming help."),
    ],
))

# ------------------------------------------------------------------ 5. Mineral resources
LESSONS.append(lesson(
    module=MODULE,
    topic=RES,
    title="Mineral resources: types, distribution, importance and problems",
    slug="res-mineral-resources",
    minutes=24,
    summary="The metallic, non-metallic and fuel minerals, where major deposits lie, why mining matters to an economy, and the problems and environmental impacts of exploiting minerals and the solutions.",
    objectives=[
        "Outline the types of minerals and illustrate their world distribution",
        "Outline the importance of mineral exploitation to the economy",
        "Describe the problems of mineral exploitation, their environmental impacts and attempted solutions",
        "Explain why mineral resources are non-renewable",
    ],
    key_concepts=["Mineral", "Ore", "Metallic minerals", "Non-metallic minerals", "Mineral fuels", "Mining", "Land reclamation"],
    blocks=[
        H("Introduction"),
        T("Look around your classroom. The metal in the roof, the cement in the floor, the glass in the window and the fuel in the "
          "generator all began as minerals taken from the ground. Even the mobile phone in your pocket contains many minerals."),
        T("Minerals formed over millions of years. We take them out faster than nature can replace them, so they are **non-renewable**."),
        H("What is a mineral?"),
        D("A **mineral** is a natural substance found in the ground, formed by natural processes. Mining is the process of taking "
          "minerals out of the earth.", title="Mineral"),
        D("An **ore** is a rock that contains enough of a metal to be worth mining, for example iron ore or bauxite (aluminium ore).", title="Ore"),
        H("Types of minerals"),
        KEY("Three groups", "", cards=[
            ["Metallic minerals", "Give metals. Iron ore (steel), copper (wires), bauxite (aluminium), gold, tin, manganese."],
            ["Non-metallic minerals", "Not metals. Limestone (cement), sand and gravel (building), salt, phosphates (fertiliser), diamonds, clay."],
            ["Mineral fuels", "Give energy. Coal, crude oil and natural gas (fossil fuels formed from ancient plants and animals)."],
        ]),
        H("World distribution"),
        IMG("f5g-res-mineral-map.svg", alt="Sketch map of the world with markers for iron ore, copper, bauxite, gold, tin, diamonds, phosphate, oil and gas, and coal; Cameroon marked",
            caption="Figure 1. Simplified sketch map showing well-known mining areas (approximate)."),
        T("Minerals are found where the rocks that contain them are found, so their distribution is very uneven. Some countries have "
          "much, others have little. Examples are given below, and you should be able to name two or three for each group."),
        KEY("Examples from different regions", "", cards=[
            ["Iron ore", "Australia, Brazil, China, India, Russia."],
            ["Copper", "Chile and Peru in South America; the Copperbelt of Zambia and the Democratic Republic of Congo."],
            ["Bauxite", "Australia, Guinea, Brazil, Jamaica."],
            ["Gold and diamonds", "Gold in South Africa and Australia; diamonds in Botswana, Russia and the DR Congo."],
            ["Oil and natural gas", "The Middle East (Saudi Arabia, Iran, Iraq and neighbours), Russia, the United States, Venezuela, and in Africa Nigeria, Angola and North African states."],
            ["Coal", "China, India, the United States, Australia, South Africa and Europe."],
        ]),
        T("Cameroon is not a major mining country. It has oil in the Gulf of Guinea and bauxite and other minerals in smaller amounts "
          "(check your textbook for details of Cameroon's own minerals)."),
        H("Importance of mineral exploitation to the economy"),
        KEY("Why minerals matter", "", cards=[
            ["Raw materials for industry", "Steel, aluminium, cement and chemicals are made from minerals."],
            ["Energy", "Coal, oil and gas power factories, vehicles and homes."],
            ["Export earnings", "Minerals such as oil, copper and gold earn foreign money for many countries."],
            ["Jobs and development", "Mines create jobs and lead to new roads, towns and railways."],
            ["Government revenue", "Taxes and royalties from mining pay for schools and hospitals."],
        ]),
        H("Problems of mineral exploitation"),
        KEY("Problems", "", cards=[
            ["High cost", "Mining needs machines, skilled workers and money, which poor countries may not have."],
            ["Remote locations", "Many deposits are far from ports and towns, so roads and railways must be built."],
            ["Price changes", "World prices of minerals rise and fall, so income is not stable."],
            ["Running out", "Non-renewable minerals will eventually be exhausted, leaving mining towns without jobs."],
            ["Danger to workers", "Mine collapses, gas and dust cause accidents and illness."],
            ["Illegal and small-scale mining", "Often poorly regulated, unsafe and harmful to land and rivers."],
        ]),
        H("Environmental impacts"),
        KEY("Impacts", "", cards=[
            ["Land damage", "Open pits, spoil heaps and holes scar the land and take farmland and forest."],
            ["Water pollution", "Chemicals, mud and waste from mines enter rivers. Oil spills pollute seas and land."],
            ["Air pollution", "Dust and gases from mines, smelters and burning fuels."],
            ["Habitat loss and noise", "Wildlife loses homes, and blasting and trucks disturb people."],
            ["Climate", "Burning coal, oil and gas releases carbon dioxide, which adds to global warming."],
        ]),
        H("Attempted solutions"),
        KEY("Solutions", "", cards=[
            ["Land reclamation", "Refill pits, level spoil heaps, replant trees and grass after mining."],
            ["Laws and checks", "Environmental impact assessments before mining and fines for pollution."],
            ["Waste treatment", "Treat dirty water before it is released."],
            ["Recycling", "Reuse metals such as aluminium and copper so fewer new mines are needed."],
            ["Local processing and fair deals", "Refining at home creates more jobs and a larger share of profit stays in the country."],
            ["Diversifying the economy", "Using mining money to develop other activities, so the country does not depend on one mineral."],
        ]),
        T("Examples (not case studies): oil producers in the Gulf of Guinea earn large export income but suffer oil spills. Chile, a "
          "newly industrialised country, earns heavily from copper. Australia, an advanced industrial country, exports iron ore and "
          "requires mining companies to restore mined land."),
        EX("Model answer 1: importance", intro="Outline the importance of mineral exploitation to a country's economy.", steps=[
            S("Raw materials", text="Minerals such as iron ore and bauxite supply factories that make steel and aluminium."),
            S("Energy", text="Oil, gas and coal provide fuel for transport, industry and electricity."),
            S("Exports and revenue", text="Selling minerals abroad earns foreign money and taxes for schools and roads."),
            S("Jobs", text="Mines and the industries around them employ many people and attract new towns and transport links."),
        ]),
        EX("Model answer 2: problems and solutions", intro="Describe the problems of mineral exploitation and suggest solutions.", steps=[
            S("Environmental problem", text="Mining leaves pits and waste heaps, and chemicals pollute rivers."),
            S("Economic problem", text="Mineral prices change and the mineral will eventually run out."),
            S("Solution 1", text="Land reclamation: refill and replant after mining, and treat polluted water."),
            S("Solution 2", text="Recycle metals and use the income to build other industries so the economy is not tied to one mineral."),
        ]),
        TIP("Minerals appear in Paper 1 as questions on types, examples and importance, and in Paper 2 Section C as problems and solutions. "
            "Link the mineral to its use when you give examples.", title="Exam link"),
        MISTAKE("Thinking all minerals are metals", "Limestone, salt and diamonds are non-metallic. Oil, coal and gas are mineral fuels."),
        MISTAKE("Giving only damage without any solution", "A full answer states the problem, the environmental impact and at least one attempted solution."),
        QUIZ("Which group of minerals does limestone, used to make cement, belong to?", ["Metallic", "Non-metallic", "Mineral fuel", "Renewable"], 1,
             "Limestone is not a metal and is not burned for energy, so it is non-metallic.", hint="Is limestone a metal?",
             feedback=["Limestone does not give a metal.", "", "It is not burnt to give energy.", "Minerals are non-renewable."]),
        QUIZ("Which is a good example of land reclamation?", ["Digging a second pit", "Refilling a mine pit and planting trees", "Burning coal", "Exporting ore"], 1,
             "Reclamation repairs the land after mining by refilling, levelling and replanting.", hint="Reclaim means to bring back.",
             feedback=["That adds damage.", "", "Burning coal is energy use, not repair.", "Exporting is trade, not repair."]),
        PQ("Name one example of each of the three groups of minerals.",
           "Metallic: iron ore or copper. Non-metallic: limestone or phosphate. Mineral fuel: coal, oil or natural gas."),
        PQ("Outline three ways in which minerals are important to the economy of a country.",
           "They are raw materials for industries (steel, cement); they give energy (coal, oil, gas); they earn export income and government taxes; "
           "and they create jobs and new roads or railways."),
        PQ("Describe two environmental impacts of mining and two attempted solutions.",
           "Impacts: pits and waste heaps damage land and vegetation; waste and chemicals pollute rivers. Solutions: land reclamation by refilling "
           "pits and replanting; treating waste water, and making companies carry out environmental impact checks."),
        SUM("Minerals are metallic, non-metallic or mineral fuels.",
            "They are unevenly distributed: for example oil in the Middle East, copper in Chile and the Copperbelt, iron ore in Australia and Brazil.",
            "Minerals supply industry and energy and earn income and jobs.",
            "Problems: cost, remote places, price changes, danger and the fact that minerals run out.",
            "Impacts such as land damage and pollution are reduced by reclamation, laws, waste treatment and recycling."),
    ],
))

# ------------------------------------------------------------------ 6. Traditional and modern sources of power
LESSONS.append(lesson(
    module=MODULE,
    topic=POW,
    title="Traditional and modern sources of power, renewable and non-renewable",
    slug="res-traditional-and-modern-sources-of-power",
    minutes=24,
    summary="The traditional and modern sources of power, which are renewable and which are not, how each is used, and their importance and problems.",
    objectives=[
        "Differentiate between non-renewable and renewable energy sources",
        "Outline the traditional and modern sources of power",
        "Outline the importance and uses of energy resources",
        "Describe the problems associated with each group of energy sources",
    ],
    key_concepts=["Energy", "Traditional sources", "Modern sources", "Fossil fuels", "Hydroelectricity", "Nuclear power", "Solar and wind power", "Geothermal power", "Biomass"],
    blocks=[
        H("Introduction"),
        T("In a village in the Far North, a woman walks two hours to collect firewood for cooking. In Douala, a restaurant owner "
          "cooks with gas, and a factory runs on electricity. Both are using energy, but from very different sources."),
        T("Energy is needed for cooking, light, transport, farming, factories and phones. This lesson sorts the sources of power into "
          "groups and shows the advantages and problems of each."),
        D("**Energy** is the power to do work, such as heating, lighting or moving machines. A **source of power** is a resource that supplies "
          "energy.", title="Energy and power"),
        H("Traditional and modern sources"),
        KEY("Two groups", "", cards=[
            ["Traditional sources", "Old, simple sources used for centuries: firewood, charcoal, animal power (oxen, donkeys, horses) and human muscle power."],
            ["Modern sources", "Developed with science and technology: coal, oil (petroleum), natural gas, hydroelectricity, nuclear power, solar power, wind power, geothermal power and biomass (plant and animal waste, biofuels)."],
        ]),
        H("Renewable and non-renewable sources"),
        D("**Renewable energy** comes from sources that are naturally replaced and do not run out, such as sunshine, wind, flowing water, "
          "heat from the earth and plants that can be regrown.", title="Renewable energy"),
        D("**Non-renewable energy** comes from sources that cannot be replaced within a human lifetime, such as coal, oil, natural gas and "
          "uranium (the fuel of nuclear power).", title="Non-renewable energy"),
        IMG("f5g-res-power-grid.svg", alt="Table with four boxes: traditional renewable sources (firewood, charcoal, animal and human power), traditional non-renewable (few), modern renewable (hydro, solar, wind, geothermal, biomass) and modern non-renewable (coal, oil, gas, nuclear)",
            caption="Figure 1. Sources of power sorted by age (traditional or modern) and by type (renewable or not)."),
        T("Firewood and charcoal are renewable only when trees are replanted. If trees are cut faster than they grow, they are not sustainable."),
        H("How the main sources work"),
        T("Most electricity is made by a **generator**: something turns a turbine (a wheel with blades), and the turbine turns the "
          "generator. Different sources turn the turbine in different ways."),
        KEY("Fuels burnt for heat", "", cards=[
            ["Coal", "Burnt in power stations to make steam, which turns turbines. Also used in industry (steel)."],
            ["Oil", "Refined into petrol, diesel and kerosene for transport and generators. Some oil is burnt for electricity."],
            ["Natural gas", "Burnt for cooking, heating and electricity. It burns more cleanly than coal or oil."],
        ]),
        KEY("Other modern sources", "", cards=[
            ["Hydroelectricity", "Falling water from a dam turns turbines. Examples: dams on the Sanaga in Cameroon, and the Lagdo dam on the Benue."],
            ["Nuclear power", "Heat from splitting uranium atoms makes steam. France and the United States use it widely."],
            ["Solar power", "Panels turn sunlight into electricity, or sunshine heats water. Good in sunny regions such as the Sahel."],
            ["Wind power", "Wind turns the blades of a wind turbine. Common in northern Europe, the United States and China."],
            ["Geothermal power", "Heat from inside the earth makes steam. Iceland, Kenya and Indonesia use it."],
            ["Biomass and biofuels", "Burning or converting crops, waste and wood into heat, gas or fuel such as ethanol."],
        ]),
        IMG("f5g-res-hydro.svg", alt="Cross-section of a hydroelectric station: reservoir, dam, intake, penstock pipe, turbine, generator and power lines",
            caption="Figure 2. A hydroelectric power station."),
        H("Importance and uses of energy"),
        KEY("Uses", "", cards=[
            ["Homes", "Cooking, lighting, heating, cooling, television and phones."],
            ["Industry", "Running machines, smelting metals, processing food and making goods."],
            ["Transport", "Petrol, diesel and electricity power cars, trucks, trains, ships and planes."],
            ["Agriculture", "Tractors, pumps for irrigation, and food stores."],
            ["Services", "Hospitals, schools, banks, internet and mobile networks need reliable electricity."],
        ]),
        T("Energy is also important to development. Countries with reliable energy can run factories, attract investment and improve health "
          "and education. Power cuts, known in Cameroon as load shedding, disturb businesses and schools."),
        H("Problems of the different sources"),
        KEY("Traditional sources", "", cards=[
            ["Deforestation", "Cutting trees for firewood and charcoal clears forests and causes erosion."],
            ["Smoke and health", "Indoor smoke harms lungs, especially of women and children."],
            ["Time and effort", "Collecting wood takes hours that could be used for school or work."],
            ["Low power", "Human and animal power cannot run big machines or move heavy loads far."],
        ]),
        KEY("Modern sources", "", cards=[
            ["Fossil fuels", "Burning coal, oil and gas releases carbon dioxide and other gases, which add to air pollution and global warming. They will also run out, and prices change."],
            ["Hydroelectricity", "Dams are expensive, flood land and move people, and output falls in a dry season."],
            ["Nuclear power", "Very expensive to build, produces dangerous radioactive waste that must be stored safely, and accidents, though rare, are serious."],
            ["Solar and wind", "Output varies with sun and wind, and panels and turbines cost a lot at the start."],
            ["Geothermal", "Only possible in a few places with hot rocks near the surface."],
            ["Biofuels", "Growing fuel crops may take land from food crops."],
        ]),
        EX("Model answer 1: renewable and non-renewable", intro="Differentiate between renewable and non-renewable energy sources, giving two examples of each.", steps=[
            S("Renewable", text="These are replaced naturally and do not run out. Examples are solar power and hydroelectricity."),
            S("Non-renewable", text="These cannot be replaced within a human lifetime. Examples are coal and crude oil."),
            S("Contrast", text="Renewable sources usually pollute less, while non-renewable fossil fuels give much of the world's energy but add to global warming."),
        ]),
        EX("Model answer 2: importance and problems of fossil fuels", intro="Outline the importance and the problems of oil and coal as energy sources.", steps=[
            S("Importance", text="Oil powers transport and generators; coal feeds power stations and steel making; they are used in homes and industry everywhere."),
            S("Problem 1: pollution", text="Burning them releases carbon dioxide, which adds to global warming, and smoke, which harms health."),
            S("Problem 2: supply", text="They will eventually run out, and world prices rise and fall, which harms countries that import them."),
            S("Conclusion", text="Fossil fuels remain very useful, but many countries are adding renewable sources."),
        ]),
        TIP("This lesson matches Paper 1 questions on classifying energy sources and Paper 2 Section C questions on the importance and problems "
            "of energy. When you list problems, name the source they belong to.", title="Exam link"),
        MISTAKE("Calling nuclear power renewable", "Uranium is mined and cannot be replaced, so nuclear power is non-renewable, even though it produces little carbon dioxide."),
        MISTAKE("Saying all renewable energy is problem-free", "Dams flood land, solar and wind vary with weather and cost a lot to install. Give the problem as well as the advantage."),
        QUIZ("Which of these is a traditional, renewable source of energy?", ["Natural gas", "Firewood from replanted trees", "Nuclear power", "Coal"], 1,
             "Firewood is an old source that can be renewed if trees are replanted.", hint="Look for something old and plant-based.",
             feedback=["Natural gas is modern and non-renewable.", "", "Nuclear power is modern and non-renewable.", "Coal is non-renewable."]),
        QUIZ("A dam on a river produces electricity. This is called", ["geothermal power", "solar power", "hydroelectricity", "biomass"], 2,
             "Falling water turns turbines that drive generators, so it is hydroelectricity.", hint="Hydro means water.",
             feedback=["Geothermal power uses heat from inside the earth.", "Solar power uses sunlight.", "", "Biomass uses plants and waste."]),
        PQ("List four traditional and four modern sources of power.",
           "Traditional: firewood, charcoal, animal power and human power. Modern: coal, oil, natural gas, hydroelectricity (also nuclear, solar, wind, "
           "geothermal and biomass are acceptable)."),
        PQ("Name two renewable and two non-renewable sources of energy.",
           "Renewable: solar power and wind power (also hydroelectricity, geothermal, biomass). Non-renewable: coal and oil (also natural gas and nuclear power)."),
        PQ("Outline the importance of energy resources and two problems of using firewood as the main source of energy.",
           "Energy is needed for cooking, light, transport, industry and services such as hospitals and schools. Problems of firewood: it causes "
           "deforestation and soil erosion, and the smoke harms health. Collecting firewood also takes time."),
        SUM("Traditional sources are firewood, charcoal, animal and human power; modern sources include coal, oil, gas, hydro, nuclear, solar, wind, geothermal and biomass.",
            "Renewable sources are naturally replaced; non-renewable sources are not.",
            "Energy is used in homes, industry, transport, agriculture and services, and it supports development.",
            "Fossil fuels pollute and run out; hydro, nuclear, solar, wind and geothermal each have their own problems.",
            "Over-use of firewood causes deforestation."),
    ],
))

# ------------------------------------------------------------------ 7. Global energy distribution and the future
LESSONS.append(lesson(
    module=MODULE,
    topic=POW,
    title="Global distribution of energy resources and the energy of the future",
    slug="res-global-energy-distribution-and-the-future",
    minutes=24,
    summary="Where the world's main energy resources are produced, the advantages of renewable over non-renewable energy, and the energy sources expected to matter in the future.",
    objectives=[
        "Illustrate the global distribution of energy resources and their production",
        "Outline the advantages of renewable energy sources over non-renewable energy resources",
        "State the energy sources of the future",
        "Outline the importance and uses of energy resources",
    ],
    key_concepts=["Energy production", "Oil and gas fields", "Coalfields", "Renewable advantages", "Solar power", "Wind power", "Biofuels", "Hydrogen"],
    blocks=[
        H("Introduction"),
        T("Cameroon is not far from the oil-producing coast of the Gulf of Guinea, and the petrol in a taxi in Yaounde may have been refined from "
          "crude oil that came from across the sea. Energy resources are not spread evenly. Some countries have plenty and export it; others "
          "must buy all they use."),
        T("This lesson maps the main areas of energy production and then looks at the future, when more energy will come from renewable sources."),
        H("Global distribution of energy resources"),
        IMG("f5g-res-energy-map.svg", alt="Sketch map of the world with markers for oil and gas, coal, hydroelectricity, nuclear, geothermal, solar and wind producing areas; Cameroon marked",
            caption="Figure 1. Simplified sketch map of well-known energy producing areas (approximate)."),
        T("The map shows well-known producing areas, not every producer. Use it to make a short, accurate description."),
        KEY("Fossil fuels", "", cards=[
            ["Oil and natural gas", "The Middle East has the largest known reserves. Other major producers are Russia, the United States, Venezuela and, in Africa, Nigeria and Angola."],
            ["Coal", "China and India produce and use very large amounts. The United States, Australia, South Africa and parts of Europe are also important."],
        ]),
        KEY("Other sources", "", cards=[
            ["Hydroelectricity", "Large producers include Canada, Brazil, China and Norway, countries with big rivers, mountains and rainfall. In Africa, the Congo basin and rivers such as the Sanaga have great potential."],
            ["Nuclear power", "The United States, France, China, Russia and Japan have many nuclear stations. Few low-income countries have any."],
            ["Geothermal", "Where the earth is hot near the surface, such as Iceland, Kenya, Indonesia, the Philippines and New Zealand."],
            ["Solar", "Sunny regions: the Sahara, the Sahel, the Middle East, Australia and the Atacama desert."],
            ["Wind", "Windy lands, such as northern Europe, the Great Plains of the United States and parts of China and India."],
        ]),
        T("The pattern: oil, gas and coal are found only where ancient plants and animals were buried and turned to fuel. Hydro needs "
          "large rivers and steep land. Solar needs sunshine, wind needs strong, steady winds and geothermal needs hot rocks. So production "
          "follows nature, but **use** follows wealth and industry. Rich and newly industrialised countries use the most energy per person."),
        TIP("In an exam, name a region and a country, say what is produced and give one reason. For example: oil is produced in the Middle East, "
            "for instance Saudi Arabia, because the right rocks and ancient marine life were found there.", title="Describing a distribution"),
        H("Advantages of renewable over non-renewable energy"),
        KEY("Why renewables are valued", "", cards=[
            ["They do not run out", "Sun, wind and water are replaced naturally; coal and oil are not."],
            ["Cleaner", "Little or no carbon dioxide is released when they work, so they cause less global warming and air pollution."],
            ["Low running costs", "Sunshine and wind are free. After building, costs are low."],
            ["Energy security", "A country that uses its own sun, water and wind need not buy fuel from abroad."],
            ["Suitable for remote places", "Solar panels and small hydro plants can power villages far from the national grid."],
            ["Jobs", "Making, installing and repairing panels and turbines creates work."],
        ]),
        T("There are limits. Renewables can cost much to build, and solar and wind output varies with weather. This is why most countries "
          "use a mix of sources."),
        H("Energy sources of the future"),
        KEY("Five likely sources", "", cards=[
            ["Solar power", "Costs are falling, and sunny countries such as those of the Sahel have great potential."],
            ["Wind power", "Wind farms on land and at sea are growing in many countries."],
            ["Hydroelectricity", "Large and small dams on the world's rivers; Africa has much unused potential."],
            ["Biofuels", "Ethanol from sugar cane (used in Brazil) and biodiesel from oil crops can replace some petrol and diesel. But fuel crops can take land from food."],
            ["Hydrogen", "Hydrogen used in a fuel cell produces only water. It is clean if made using renewable electricity, because making hydrogen needs energy."],
        ]),
        EX("Model answer 1: distribution", intro="Describe the global distribution of oil and natural gas production.", steps=[
            S("Main region", text="The Middle East is the leading region, with countries such as Saudi Arabia, Iran and Iraq."),
            S("Other regions", text="Russia, the United States and Venezuela are also major producers. In Africa, Nigeria and Angola produce oil, and North African countries produce oil and gas."),
            S("Reason", text="Oil and gas are found only where particular rocks trapped fuel formed from ancient sea life, so production is uneven."),
            S("Sketch", text="Draw a simple world map and mark these areas with a key."),
        ]),
        EX("Model answer 2: advantages of renewables", intro="Outline three advantages of renewable energy over non-renewable energy.", steps=[
            S("Sustainable", text="Sunshine, wind and water are replaced naturally, but oil and coal will run out."),
            S("Cleaner", text="Renewables release little carbon dioxide, so they cause less pollution and global warming."),
            S("Local and cheap to run", text="A country can use its own resources without imports, and sunshine and wind are free, so running costs are low."),
            S("Balance", text="The main drawbacks are high set-up costs and varying output."),
        ]),
        TIP("Energy appears in Paper 1 (classification, distribution, definitions) and in Paper 2 Section C (distribution, advantages of renewables, "
            "future sources).", title="Exam link"),
        MISTAKE("Saying where energy is used instead of where it is produced", "A country may use a lot of coal and produce none. Describe the producing areas on the map."),
        MISTAKE("Calling hydrogen a free source of energy", "Hydrogen must be made using energy, so it is clean only when produced with clean power."),
        QUIZ("Which region has the largest known reserves of oil?", ["Western Europe", "The Middle East", "Southern Africa", "Australia"], 1,
             "The Middle East holds the largest known oil reserves in the world.", hint="Think of Saudi Arabia.",
             feedback=["Western Europe has little oil, apart from the North Sea.", "", "Southern Africa is better known for coal and minerals.", "Australia is known for coal and iron ore."]),
        QUIZ("Which is an advantage of solar power over coal?", ["It works at night", "It releases almost no carbon dioxide when working", "It costs nothing to install", "It is found everywhere equally"], 1,
             "Solar panels make electricity without burning fuel, so they release almost no carbon dioxide.", hint="Think about pollution.",
             feedback=["Panels need storage to work at night.", "", "Installing panels costs a lot at first.", "Sunshine is stronger near the Equator and in deserts than at high latitudes."]),
        PQ("Name two countries that are major producers of each of: oil, coal and hydroelectricity.",
           "Oil: Saudi Arabia and Russia (also the United States, Nigeria). Coal: China and India (also the United States, Australia). "
           "Hydroelectricity: Canada and Brazil (also China and Norway)."),
        PQ("Outline three advantages of renewable over non-renewable energy.",
           "They do not run out. They release little carbon dioxide, so they are cleaner. They are cheap to run because sun, wind and water are free. "
           "They can supply remote villages and reduce the need for imported fuel."),
        PQ("State the five energy sources of the future and explain one of them.",
           "Solar power, wind power, hydroelectricity, biofuels and hydrogen. Example: biofuels such as ethanol from sugar cane replace some petrol, "
           "but fuel crops can compete with food crops for land."),
        SUM("Oil and gas come mainly from the Middle East, Russia, the Americas and West Africa; coal from China, India, the United States and Australia.",
            "Hydro, solar, wind and geothermal production follows rivers, sunshine, wind and hot rocks.",
            "Renewable energy does not run out, is cleaner, is cheap to run, helps energy security and can serve remote places.",
            "Renewables can be costly to build and vary with weather.",
            "Energy sources of the future are solar, wind, hydro, biofuels and hydrogen."),
    ],
))
