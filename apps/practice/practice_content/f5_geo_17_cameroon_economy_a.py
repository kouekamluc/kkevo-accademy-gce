"""Practice sets for Form 5 Geography: Economic development potentials, part A (one set per lesson)."""

from .dsl import *  # noqa: F403

COURSE = ("geography", "form-5")

MODULE = "The Geography of Cameroon"
TOPIC = "Economic development potentials"

SETS = []

# ------------------------------------------------------------------ 1. Systems and types of agriculture
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Systems and types of agriculture in Cameroon: check your understanding",
    lesson="cmreco-agriculture-systems-and-types",
    questions=[
        MC("Farming done mainly to feed the farmer's own family is called", [
            C("commercial farming", why="Commercial farming is mainly to sell for profit."),
            C("subsistence farming", correct=True),
            C("plantation farming", why="A plantation is a large estate producing for sale."),
            C("mixed farming", why="Mixed farming means crops and animals together; it is not defined by who eats the produce."),
        ], steps=[S("Recall", text="Subsistence farming feeds the family. Only a small surplus is sold.")],
           concept="Subsistence farming", skill="Recall", hint="Think of the word 'subsist', which means to survive."),
        MC("Which of these is mainly a food crop in Cameroon?", [
            C("Rubber", why="Rubber is a plantation cash crop."),
            C("Tea", why="Tea is grown on estates for sale."),
            C("Cassava", correct=True),
            C("Cotton", why="Cotton is a cash crop grown in the north."),
        ], steps=[S("Recall", text="Cassava is eaten by families and sold locally. Rubber, tea and cotton are cash crops.")],
           concept="Food crops", skill="Recall", hint="Which crop do families eat every day?"),
        MC("Which statement describes a plantation?", [
            C("A very large estate growing one crop with many workers", correct=True),
            C("A small family plot of mixed crops", why="That is a subsistence farm."),
            C("A grazing area for herders", why="That is a pasture, not a plantation."),
            C("A fish pond near a village", why="That is fish farming."),
        ], steps=[S("Recall", text="Plantations are large, single-crop and employ many workers, often with a factory.")],
           concept="Plantations", skill="Recall", hint="Think of rows of bananas or oil palms as far as you can see."),
        MC("Large herds of cattle are mainly kept in which part of Cameroon?", [
            C("The coastal plain around Douala", why="The hot, humid coast has tsetse flies and forest, which are poor for cattle."),
            C("The southern forest around Ebolowa", why="The dense forest is not suited to large herds."),
            C("The area around Mount Cameroon", why="This area is known for plantations."),
            C("The Adamawa plateau and the north", correct=True),
        ], steps=[S("Recall", text="Open grassland on the Adamawa plateau, in the north and in the North-West highlands suits cattle.")],
           concept="Livestock rearing", skill="Recall", hint="Think of cool, open grassland."),
        MC("Which crop is grown by many small farmers in the north and sold to a company?", [
            C("Cotton", correct=True),
            C("Cocoa", why="Cocoa belongs to the humid south."),
            C("Oil palm", why="Oil palm needs a hot, wet climate."),
            C("Banana", why="Bananas are grown near the south-west and Littoral."),
        ], steps=[S("Link crop to climate", text="Cotton needs a long dry season for harvesting, so it suits the north.")],
           concept="Cotton in the north", skill="Application", hint="Which cash crop likes a drier climate?"),
        MC("A farmer in the West region grows maize and beans, sells some in Bafoussam market, and eats the rest. This farmer is mainly practising", [
            C("plantation farming", why="A plantation is a large single-crop estate."),
            C("pure commercial farming", why="Most of the harvest is eaten at home."),
            C("subsistence farming with a small surplus", correct=True),
            C("ranching", why="Ranching is large-scale cattle rearing."),
        ], steps=[S("Decide the main purpose", text="The family eats most of the harvest, so it is subsistence. Selling a surplus does not change that.")],
           concept="Subsistence with surplus", skill="Application", hint="Where does most of the harvest go?"),
        MC("Why are bananas, rubber and oil palm more common near Mount Cameroon and the Littoral than in the far north?", [
            C("The north has no farmers", why="Farming is very important in the north too."),
            C("They need a hot, wet climate and fertile volcanic soils, found in the south-west", correct=True),
            C("They are not exported", why="They are mainly export crops."),
            C("The north has too much rain", why="The north has a long dry season."),
        ], steps=[S("Link crops to environment", text="These tree crops need heavy rainfall and warm temperatures all year. The coastal south-west has both and fertile soils.")],
           concept="Climate and farming types", skill="Reasoning", hint="Compare rainfall in Douala and Maroua."),
        MC("Which pair is correctly matched?", [
            C("Tea: northern savanna", why="Tea is grown in the cool, wet highlands such as Tole and Ndu."),
            C("Cattle: dense equatorial forest", why="Dense forest is poor for cattle."),
            C("Cocoa: Lake Chad shore", why="Cocoa needs a humid forest climate."),
            C("Irrigated rice: Logone floodplain in the far north", correct=True),
        ], steps=[S("Check each pair", text="Only irrigated rice on the Logone floodplain is correctly matched. Tea is grown in cool highlands, cocoa in the humid south, and cattle on grasslands.")],
           concept="Matching crops to places", skill="Application", hint="Check the climate each crop needs."),
    ]))

# ------------------------------------------------------------------ 2. Factors, problems and impact of agriculture
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Agriculture in Cameroon: factors, problems, impact and efforts",
    lesson="cmreco-factors-problems-and-impact-of-agriculture",
    questions=[
        MC("Which of these is a human (not physical) factor favouring agriculture in Cameroon?", [
            C("Fertile volcanic soils", why="Soils are a physical factor."),
            C("A varied climate", why="Climate is a physical factor."),
            C("A large rural labour force", correct=True),
            C("Flat land on the Logone floodplain", why="Relief is a physical factor."),
        ], steps=[S("Sort factors", text="Climate, soils and relief come from nature. A labour force is made up of people, so it is a human factor.")],
           concept="Factors favouring agriculture", skill="Concept", hint="Which factor depends on people rather than nature?"),
        MC("Which strategy best solves the problem of produce rotting on muddy rural roads?", [
            C("Build and repair rural roads", correct=True),
            C("Plant more cocoa", why="Planting more crops does not help produce reach the market."),
            C("Clear more forest", why="This does not improve transport and may cause damage."),
            C("Import more food", why="This does not help farmers and costs foreign money."),
        ], steps=[S("Match problem and solution", text="Rotting is caused by slow, difficult transport, so better roads solve it.")],
           concept="Problems and strategies", skill="Application", hint="What delays the produce on its way to the market?"),
        MC("Which organisation carries out agricultural research in Cameroon?", [
            C("SODECOTON only", why="SODECOTON deals mainly with cotton development."),
            C("The Douala port authority", why="A port authority runs the port, not research."),
            C("The Ministry of Defence", why="Defence is not responsible for farm research."),
            C("The Institute of Agricultural Research for Development (IRAD)", correct=True),
        ], steps=[S("Recall", text="IRAD is the national agricultural research institute that develops better seeds and methods.")],
           concept="Government efforts", skill="Recall", hint="The initials start with IR."),
        MC("Climate-smart agriculture aims to", [
            C("clear forest for larger farms", why="Clearing forest can raise emissions and harm the environment."),
            C("raise yields, adapt to climate change and, where possible, cut emissions", correct=True),
            C("grow only export crops", why="The choice of crops does not define climate-smart farming."),
            C("stop all farming in dry areas", why="It helps farmers adapt, not stop farming."),
        ], steps=[S("Recall the definition", text="Climate-smart agriculture links higher output, adaptation to climate change and lower emissions.")],
           concept="Climate-smart agriculture", skill="Concept", hint="It has three goals, not one."),
        MC("Farmers cannot buy fertiliser and improved seeds. Which solution would help most directly?", [
            C("Microfinance loans and farmers' co-operatives", correct=True),
            C("More plantation roads", why="Roads help transport but do not give farmers money for inputs."),
            C("Longer school holidays", why="This is not linked to farm inputs."),
            C("More tourist hotels", why="Hotels do not give farmers credit."),
        ], steps=[S("Identify the problem", text="The problem is lack of money (credit). Loans and co-operatives that buy inputs together address it directly.")],
           concept="Credit and inputs", skill="Application", hint="What does the farmer lack: roads, or money?"),
        MC("Which is an economic impact of agriculture in Cameroon?", [
            C("It increases the height of Mount Cameroon", why="Farming does not change the height of mountains."),
            C("It makes rainfall higher in the north", why="Farming does not control rainfall in this way."),
            C("It supplies raw materials such as cotton and oil palm to industry", correct=True),
            C("It removes the need for any imports", why="Cameroon still imports some food and goods."),
        ], steps=[S("Think about links", text="Farm products such as cotton and oil palm are processed in factories, so agriculture supports industry.")],
           concept="Economic impact", skill="Concept", hint="How do farm products reach factories?"),
        MC("Why can depending on a few export crops be a problem for the economy?", [
            C("The crops cannot be eaten", why="This is not a reason."),
            C("Exports earn no money", why="Exports earn foreign exchange; the issue is price changes."),
            C("Farmers refuse to grow them", why="Many farmers do grow them."),
            C("A fall in world prices can reduce incomes and government earnings", correct=True),
        ], steps=[S("Explain", text="World prices for cocoa, coffee and cotton go up and down. If they fall, farmers and the country earn less.")],
           concept="Dependence on exports", skill="Reasoning", hint="Who decides the world price of cocoa?"),
        MC("Which pair shows efforts by organisations other than the government?", [
            C("MINADER and MINEPIA", why="These are government ministries."),
            C("FAO and farmers' co-operatives", correct=True),
            C("IRAD and MINADER", why="Both are part of government research or administration."),
            C("SODECOTON and the Ministry of Agriculture", why="The ministry is government and SODECOTON is a state-linked company."),
        ], steps=[S("Sort the actors", text="FAO is an international organisation and co-operatives are farmers' own groups, so both are non-government.")],
           concept="Other organisations", skill="Concept", hint="Which pair has no ministry in it?"),
    ]))

# ------------------------------------------------------------------ 3. Food loss and food waste
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Food loss and food waste: definitions, causes and solutions",
    lesson="cmreco-food-loss-and-food-waste",
    questions=[
        MC("Food that is spoiled in storage or transport before it reaches the shop is called", [
            C("food loss", correct=True),
            C("food waste", why="Waste is food thrown away at the shop or home."),
            C("food security", why="Food security means having enough food."),
            C("food processing", why="Processing means changing food into another product."),
        ], steps=[S("Recall", text="Food loss happens between harvest and the shop.")],
           concept="Food loss", skill="Recall", hint="Think of where in the food chain the spoiling happens."),
        MC("A family throws away cooked rice nobody ate. This is", [
            C("food loss", why="Loss is early in the chain, before the shop."),
            C("post-harvest loss", why="Post-harvest loss is on the farm, in stores or in transport."),
            C("food processing", why="Nothing was processed here."),
            C("food waste", correct=True),
        ], steps=[S("Locate it in the chain", text="It happens in the household at the end of the chain, so it is food waste.")],
           concept="Food waste", skill="Application", hint="Where in the food chain is the household?"),
        NUM("In an example, a farmer harvests 200 crates of tomatoes and 50 crates spoil before they reach the market. What percentage of the harvest is lost?", 25,
            steps=[S("Fraction lost", math=r"\frac{50}{200}"), S("Convert to a percentage", math=r"\frac{50}{200} \times 100 = 25")],
            unit="%", concept="Calculating percentage loss", skill="Calculation", hint="Divide the crates lost by the crates harvested, then multiply by 100.",
            feedback="The numbers are invented for practice; real losses vary a lot."),
        MC("Which is a cause of food loss in rural Cameroon?", [
            C("Cooking too much for a party", why="This is a cause of food waste at home."),
            C("Poor roads and no cold storage", correct=True),
            C("Buying too much in the supermarket", why="This is a household waste cause."),
            C("Throwing away food past its date", why="This is a retail or household waste cause."),
        ], steps=[S("Match cause to stage", text="Roads and storage are part of the supply chain, so they cause loss, not waste.")],
           concept="Causes of food loss", skill="Concept", hint="Which cause is on the farm-to-market route?"),
        MC("Which action helps reduce food waste at home?", [
            C("Harvest crops earlier", why="This affects the farm, not household waste."),
            C("Build a bigger road", why="This affects transport loss."),
            C("Plan meals and use left-overs", correct=True),
            C("Export more cocoa", why="Exports do not change household waste."),
        ], steps=[S("Match solution to stage", text="Household waste is reduced by planning, careful buying and reusing left-overs.")],
           concept="Solutions to food waste", skill="Application", hint="The solution should be about habits."),
        MC("Turning cassava into gari helps reduce food loss because", [
            C("processed food keeps longer and can be sold all year", correct=True),
            C("it makes cassava heavier", why="Weight is not the reason."),
            C("it makes people eat more", why="The aim is to keep food, not to make people eat more."),
            C("it removes the need for farms", why="Processing still needs farms."),
        ], steps=[S("Explain the link", text="Drying and processing make food last, so less of it spoils.")],
           concept="Processing and loss", skill="Reasoning", hint="Which lasts longer: fresh cassava or gari?"),
        MC("Which is an environmental consequence of food waste?", [
            C("More rain falls in the north", why="Food waste does not control rainfall."),
            C("Rivers become wider", why="This is not caused by food waste."),
            C("Soil becomes more fertile everywhere", why="Waste on dumps does not do this."),
            C("Rotting food on dumps releases methane, a greenhouse gas", correct=True),
        ], steps=[S("Recall", text="Food rotting in dumps produces methane, which adds to global warming.")],
           concept="Consequences", skill="Concept", hint="What gas comes from rotting rubbish?"),
        MC("A trader in Yaoundé says: 'In my country, most of the food that goes missing is lost before it reaches the market.' Which statement best supports her?", [
            C("Most households cook too much rice", why="This is waste at home, not loss before the market."),
            C("Restaurants throw away unsold food", why="This is waste at the end of the chain."),
            C("Poor storage, rough roads and little processing cause much spoilage after harvest", correct=True),
            C("People ignore sell-by dates", why="This is a household or retail waste cause."),
        ], steps=[S("Find the stage", text="Loss before the market means harvest, storage and transport, so storage, roads and processing are the evidence.")],
           concept="Where loss happens", skill="Reasoning", hint="Look for the stage before the market."),
    ]))

# ------------------------------------------------------------------ 4. Forest and fish resources
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Forest and fish resources of Cameroon: distribution, challenges and impact",
    lesson="cmreco-forest-and-fish-resources",
    questions=[
        MC("Fish and trees are called renewable resources because they", [
            C("are found only in Cameroon", why="Many countries have forests and fish."),
            C("can replace themselves naturally if used carefully", correct=True),
            C("never run out whatever people do", why="Overuse can finish them."),
            C("cannot be sold abroad", why="Timber and fish can be sold."),
        ], steps=[S("Recall", text="A renewable resource can grow back, but only if it is not used faster than it recovers.")],
           concept="Renewable resources", skill="Recall", hint="Think about whether trees can grow again."),
        MC("Dense equatorial forest in Cameroon is found mainly in the", [
            C("far north near Lake Chad", why="The far north is dry Sahel."),
            C("Adamawa grasslands", why="The Adamawa plateau is mainly grassland."),
            C("Mandara mountains", why="The Mandara mountains are in the dry north."),
            C("humid south and east", correct=True),
        ], steps=[S("Link climate to vegetation", text="Heavy rain all year gives dense forest in the south and east.")],
           concept="Distribution of forest", skill="Recall", hint="Where is the rain heaviest and most regular?"),
        MC("Which of these is a non-timber forest product?", [
            C("Honey", correct=True),
            C("Sawn planks", why="Planks are timber."),
            C("Logs of ayous", why="Ayous logs are timber."),
            C("Plywood", why="Plywood is made from timber."),
        ], steps=[S("Sort products", text="Non-timber products are fruits, honey, medicinal plants and similar items. Planks, logs and plywood all come from timber.")],
           concept="Forest products", skill="Concept", hint="Which one does not come from cutting the tree?"),
        MC("Fishing with small canoes, nets and lines by local families is called", [
            C("industrial fishing", why="Industrial fishing uses large boats and modern equipment."),
            C("fish farming", why="Fish farming raises fish in ponds."),
            C("artisanal fishing", correct=True),
            C("trawling", why="Trawling uses large nets pulled by boats."),
        ], steps=[S("Recall", text="Artisanal fishing is small-scale fishing with simple gear.")],
           concept="Fishing types", skill="Recall", hint="Think of the Limbe canoes."),
        MC("Which is a challenge of exploiting forest resources in Cameroon?", [
            C("Too few trees growing", why="The challenge is illegal and excessive cutting, not a lack of growth."),
            C("Illegal logging and poor forest roads", correct=True),
            C("A shortage of rain in the south", why="The south has heavy rainfall."),
            C("Lack of demand for timber", why="There is demand for timber."),
        ], steps=[S("Recall challenges", text="Illegal logging, poor roads and overcutting make forest management difficult.")],
           concept="Forest challenges", skill="Concept", hint="Think about cutting without permission."),
        MC("Why can cutting mangrove trees to smoke fish harm fishing in the long run?", [
            C("Mangroves are breeding grounds for fish", correct=True),
            C("Mangroves make fish bigger", why="They do not do this."),
            C("Mangroves bring more rain", why="Mangroves do not control rainfall."),
            C("Smoked fish never sells", why="Smoked fish sells well."),
        ], steps=[S("Explain the link", text="Young fish grow among mangrove roots. If the mangroves are cut, fewer fish are born and caught later.")],
           concept="Mangroves and fish", skill="Reasoning", hint="Where do young fish shelter?"),
        MC("Which statement describes an environmental impact of deforestation?", [
            C("More jobs in sawmills", why="This is an economic impact."),
            C("Higher government taxes", why="This is an economic impact."),
            C("Bigger timber exports", why="This is an economic impact."),
            C("Soil erosion and loss of animal habitat", correct=True),
        ], steps=[S("Separate economy from environment", text="Jobs, taxes and exports are economic. Erosion and lost habitat concern the natural environment.")],
           concept="Impact of deforestation", skill="Concept", hint="Choose the effect on nature."),
        MC("Which is a government effort to manage forests and fish better?", [
            C("Allowing unlimited cutting", why="This would harm resources."),
            C("Ending all fishing", why="This is not the policy; rules guide use."),
            C("Closing all roads in the forest", why="This is not a management policy."),
            C("Creating protected areas such as Korup and issuing fishing licences", correct=True),
        ], steps=[S("Identify management", text="Protected areas and licences are tools to control use and protect stocks.")],
           concept="Government efforts", skill="Application", hint="Look for an action that controls use."),
    ]))

# ------------------------------------------------------------------ 5. Mineral and energy resources
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Mineral and energy resources of Cameroon: distribution, challenges and impact",
    lesson="cmreco-mineral-and-energy-resources",
    questions=[
        MC("Which resource cannot be replaced once it is used up?", [
            C("Water for hydropower", why="Water is renewable through the water cycle."),
            C("Sunlight", why="Sunlight is renewable."),
            C("Oil", correct=True),
            C("Fuelwood from replanted trees", why="Replanted trees can be renewed."),
        ], steps=[S("Recall", text="Oil is a non-renewable resource because it took millions of years to form.")],
           concept="Non-renewable resources", skill="Recall", hint="Which one forms over millions of years?"),
        MC("The main hydroelectric plants of Edea and Song Loulou are on which river?", [
            C("The Benue", why="Lagdo is on the Benue."),
            C("The Sanaga", correct=True),
            C("The Logone", why="The Logone is in the far north."),
            C("The Cross River", why="The Cross River is in the South-West and is not the site of these plants."),
        ], steps=[S("Recall", text="Edea and Song Loulou are on the Sanaga.")],
           concept="Hydropower sites", skill="Recall", hint="It is the longest river that flows wholly in Cameroon."),
        MC("Bauxite is the ore of which metal?", [
            C("Iron", why="Iron comes from iron ore such as haematite."),
            C("Copper", why="Copper comes from copper ores."),
            C("Gold", why="Gold is found as a metal."),
            C("Aluminium", correct=True),
        ], steps=[S("Recall", text="Bauxite is the main ore of aluminium.")],
           concept="Bauxite", skill="Recall", hint="Think of the Edea smelter."),
        MC("Where is Cameroon's oil produced mainly?", [
            C("Offshore along the south-west coast", correct=True),
            C("Lake Chad", why="Lake Chad is a lake in the far north."),
            C("The Adamawa plateau", why="The Adamawa plateau is known for cattle and bauxite."),
            C("Mount Cameroon summit", why="The summit is a volcano and not an oilfield."),
        ], steps=[S("Recall", text="Oil is produced offshore on the Atlantic coast in the south-west, and refined at Limbe.")],
           concept="Oil distribution", skill="Recall", hint="Think of Limbe and the Atlantic."),
        MC("Why does Cameroon not yet mine iron ore on a large scale in the east?", [
            C("There is no iron ore", why="Iron ore has been found there."),
            C("It is too cold", why="Climate is not the main reason."),
            C("Mining needs a railway and port, which are costly and lacking", correct=True),
            C("Iron has no uses", why="Iron is very useful."),
        ], steps=[S("Explain", text="Heavy ore must be moved to the coast. Without railways and a port, mining is not profitable.")],
           concept="Infrastructure challenge", skill="Reasoning", hint="How does heavy ore reach the sea?"),
        MC("A company wants to build a plant that needs a lot of cheap electricity. Which Cameroonian resource would help most?", [
            C("Hydropower from the Sanaga", correct=True),
            C("Gold from the east", why="Gold is a mineral, not a power source."),
            C("Limestone", why="Limestone is used for cement, not to produce electricity."),
            C("Fish from Lake Chad", why="Fish are not an energy source."),
        ], steps=[S("Match need and resource", text="The Edea aluminium smelter shows how cheap hydropower supports energy-hungry industry.")],
           concept="Hydropower and industry", skill="Application", hint="Which resource produces electricity?"),
        MC("Which is an environmental problem linked to oil and mining?", [
            C("Higher government income", why="This is an economic effect."),
            C("Oil spills and polluted rivers", correct=True),
            C("More jobs for engineers", why="This is an economic effect."),
            C("New electricity lines", why="This is an infrastructure benefit."),
        ], steps=[S("Pick the harm to nature", text="Spills pollute the sea and mangroves, and mining can pollute rivers.")],
           concept="Environmental impact", skill="Concept", hint="Choose the answer that harms nature."),
        MC("Which is a government effort to improve energy supply?", [
            C("Closing all power stations", why="This would reduce power."),
            C("Banning solar panels", why="Solar is being encouraged in places."),
            C("Stopping all mining licences forever", why="This is not the policy described."),
            C("Building new hydropower dams such as Lom Pangar and Nachtigal", correct=True),
        ], steps=[S("Recall", text="New dams, gas power near Kribi and extended networks are efforts to raise supply.")],
           concept="Government efforts", skill="Application", hint="Which action increases electricity production?"),
    ]))

# ------------------------------------------------------------------ 6. Multipurpose river development projects
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Multipurpose river development projects: the Lagdo project",
    lesson="cmreco-multipurpose-river-development-projects",
    questions=[
        MC("A multipurpose river project is one that", [
            C("only produces electricity", why="That is a single-purpose scheme."),
            C("only supplies drinking water", why="That is a single purpose."),
            C("only controls floods", why="That is a single purpose."),
            C("serves several purposes, such as power, irrigation and flood control", correct=True),
        ], steps=[S("Recall", text="Multipurpose means several uses from the same scheme.")],
           concept="Multipurpose project", skill="Recall", hint="Think about the word 'multi'."),
        MC("The Lagdo dam is on which river?", [
            C("The Benue", correct=True),
            C("The Sanaga", why="Edea and Song Loulou are on the Sanaga."),
            C("The Wouri", why="The Wouri is near Douala."),
            C("The Nyong", why="The Nyong flows through the south."),
        ], steps=[S("Recall", text="Lagdo is on the Benue River in the North region.")],
           concept="Lagdo location", skill="Recall", hint="This river flows into Nigeria."),
        MC("Which is an aim of the Lagdo project?", [
            C("To dry up the river completely", why="The aim is to control, not dry up, the river."),
            C("To stop all farming near the river", why="Irrigation encourages farming."),
            C("To supply electricity and water for irrigation", correct=True),
            C("To make Mount Cameroon taller", why="This is not related."),
        ], steps=[S("Recall aims", text="Lagdo was built for electricity, irrigation, flood control and fishing.")],
           concept="Aims of Lagdo", skill="Recall", hint="Think about the uses of the stored water."),
        MC("Which is a benefit of irrigation from the Lagdo reservoir?", [
            C("The Benue never flows", why="The river continues to flow."),
            C("Farmers can grow crops in the dry season", correct=True),
            C("No fertiliser is ever needed", why="Irrigation does not remove the need for inputs."),
            C("Pests disappear", why="Pests are not removed by water."),
        ], steps=[S("Explain", text="Stored water can be sent to fields in the dry season, allowing more crops per year.")],
           concept="Benefits of irrigation", skill="Concept", hint="What does irrigation give in the dry season?"),
        MC("Quick release of water from a full reservoir in the wet season can cause", [
            C("more electricity for the north", why="This is not the problem of sudden releases."),
            C("a longer dry season", why="Releases do not change the season."),
            C("more fish in the reservoir", why="Fish are not affected in this way."),
            C("flooding downstream", correct=True),
        ], steps=[S("Trace the water", text="The extra water goes downstream and can flood farms and villages.")],
           concept="Problems of dams", skill="Reasoning", hint="Where does the released water go?"),
        MC("Which solution best helps families whose villages are flooded by a reservoir?", [
            C("Compensation and resettlement with new land and services", correct=True),
            C("Ignore them", why="This would cause hardship."),
            C("Raise taxes on them", why="This would worsen their situation."),
            C("Close the dam permanently", why="This is not a solution for those displaced."),
        ], steps=[S("Match problem and solution", text="Displaced families need new homes, land and compensation.")],
           concept="Solutions to dam problems", skill="Application", hint="What do displaced families need first?"),
        MC("Which pair of projects is correctly matched with its river?", [
            C("Edea: Benue", why="Edea is on the Sanaga."),
            C("Lagdo: Benue", correct=True),
            C("Song Loulou: Logone", why="Song Loulou is on the Sanaga."),
            C("Lagdo: Sanaga", why="Lagdo is on the Benue."),
        ], steps=[S("Check each pair", text="Lagdo is on the Benue, while Edea and Song Loulou are on the Sanaga.")],
           concept="Identifying projects", skill="Recall", hint="Only one pair has the right river for the right dam."),
        MC("An exam asks you to describe ONE multipurpose project. Which set of headings does the syllabus expect?", [
            C("Soil, climate, relief, drainage, vegetation", why="These describe physical geography, not a project."),
            C("Origin, growth, decline, collapse, future", why="This is not the list of headings."),
            C("Location, aims, benefits, problems and solutions", correct=True),
            C("Population, trade, transport, tourism, industry", why="These are sectors, not project headings."),
        ], steps=[S("Recall the syllabus", text="The five headings are location, aims, benefits, problems and solutions.")],
           concept="Structure of the answer", skill="Recall", hint="Think about what you would ask about any project."),
    ]))
