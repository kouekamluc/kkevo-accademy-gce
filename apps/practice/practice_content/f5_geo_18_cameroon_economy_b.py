"""Practice sets for Form 5 Geography: Economic development potentials of Cameroon, part B (one set per lesson)."""

from .dsl import *  # noqa: F403

COURSE = ("geography", "form-5")

MODULE = "The Geography of Cameroon"
TOPIC = "Economic development potentials"

SETS = []

PMAP = "f5g-cmrdev-practice-map.svg"
PMAP_ALT = ("Simplified sketch map of Cameroon with letters A to H marking towns and sites; a dashed line shows the railway "
            "from the coast to Ngaoundere. A is Douala, B is Yaounde, C is Kribi, D is Ngaoundere, E is Limbe, F is Waza, G is Garoua and H is Edea.")

# ------------------------------------------------------------------ 1. Manufacturing types and distribution
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Types and distribution of manufacturing in Cameroon",
    lesson="cmrdev-manufacturing-types-and-distribution",
    questions=[
        MC("Which of these is an example of manufacturing?", [
            C("Growing cocoa on a farm", why="Growing a crop is a primary activity, not manufacturing."),
            C("Turning cocoa beans into chocolate in a factory", correct=True),
            C("Catching fish in the sea", why="Fishing is a primary activity."),
            C("Selling cocoa in a market", why="Selling goods is a trade (tertiary) activity."),
        ], steps=[S("Define manufacturing", text="Manufacturing changes raw materials into finished goods, usually in a factory. Cocoa to chocolate fits this.")],
           concept="Meaning of manufacturing", skill="Recall", hint="Look for the option where a raw material is changed into a new product."),
        MC("The aluminium smelter at Edea is an example of which type of industry?", [
            C("Agro-processing", why="Agro-processing uses farm products such as cocoa or cotton."),
            C("Wood-based industry", why="Wood-based industries use timber."),
            C("Beverage industry", why="Beverages are drinks."),
            C("Metal and mineral-based industry", correct=True),
        ], steps=[S("Identify the raw material", text="Aluminium is a metal made from ore. Smelting it is a metal-based industry.")],
           concept="Types of industry", skill="Recall", hint="What kind of raw material does aluminium come from?"),
        MC("On the map, which letter marks Edea, where aluminium is smelted using hydroelectric power from the Sanaga?", [
            C("H", correct=True),
            C("A", why="A is Douala, the main port city, not Edea."),
            C("E", why="E is Limbe on the coast, where the oil refinery is."),
            C("C", why="C is Kribi on the coast, further south."),
        ], steps=[S("Locate on the map", text="Edea lies on the Sanaga close to Douala. On the map, that is letter H.")],
           concept="Location of Edea", skill="Interpretation", hint="Edea is close to Douala, slightly to the south-east.",
           diagram=PMAP, diagram_alt=PMAP_ALT),
        MC("Which group of reasons best explains why Douala has so many factories?", [
            C("It is the capital and has the highest mountain", why="Yaounde is the capital, and mountains do not attract factories."),
            C("It has no taxes and no competition", why="Firms in Douala do pay taxes and face competition."),
            C("It has a port, a large market, workers and road and rail links", correct=True),
            C("It is far from the sea so goods cannot be imported", why="Douala is on the coast, which is the opposite."),
        ], steps=[S("Match to location factors", text="A port, market, labour and transport are the main reasons for clustering in Douala.")],
           concept="Clustering at Douala", skill="Concept", hint="Think of what a factory needs in order to get raw materials in and goods out."),
        MC("Why are sawmills usually built close to the forest?", [
            C("Customers live in the forest", why="Few customers live in forests. Markets are in towns."),
            C("Logs are heavy and lose weight when sawn, so it is cheaper to process them near the source", correct=True),
            C("Planks cannot be moved by road", why="Planks are moved by road all the time."),
            C("Forests have the most electricity", why="Power is not the main reason for sawmill sites."),
        ], steps=[S("Apply the weight-loss idea", text="A log weighs more than the planks cut from it. Carrying planks costs less than carrying logs.")],
           concept="Raw-material oriented industry", skill="Reasoning", hint="Think about what is cheaper to carry: logs or planks."),
        MC("Why are drink bottling plants found in many towns across Cameroon?", [
            C("Drinks are bulky and sell to the local market, so they are made near customers", correct=True),
            C("Bottles can only be made in forests", why="Bottling has nothing to do with forests."),
            C("Drinks cannot be sold in the town where they are made", why="Drinks are mostly sold close to where they are made."),
            C("Only the capital has electricity", why="Many towns have electricity."),
        ], steps=[S("Market-oriented industry", text="Heavy, bulky products cost a lot to carry, so they are made near the market.")],
           concept="Market-oriented industry", skill="Concept", hint="Who buys the product, and where do they live?"),
        MC("The map shows letter E at a coastal town where the oil refinery stands. Which town is it?", [
            C("Douala", why="Douala has many industries, but the refinery is at the town marked E."),
            C("Kribi", why="Kribi is a port and tourist town, marked C."),
            C("Yaounde", why="Yaounde is inland, marked B."),
            C("Limbe", correct=True),
        ], steps=[S("Locate on the map", text="E is Limbe, close to Mount Cameroon. The refinery is on the coast so that tankers can deliver oil.")],
           concept="Oil refining at Limbe", skill="Interpretation", hint="The refinery needs a coast for tankers; look at the western coast near Mount Cameroon.",
           diagram=PMAP, diagram_alt=PMAP_ALT),
        MC("After a few factories open in a town, more factories often follow. Which is the best explanation?", [
            C("The government stops factories being built elsewhere", why="Location is decided by costs and markets, not by a ban."),
            C("People dislike farming", why="Preferences for farming do not explain clustering."),
            C("Banks, workers, repair shops and suppliers are already there, which lowers costs", correct=True),
            C("Factories need to be close together to avoid customers", why="Factories actually want customers, not to avoid them."),
        ], steps=[S("Explain clustering", text="Existing services and workers make later factories cheaper to run. This is clustering.")],
           concept="Industrial clustering", skill="Reasoning", hint="Think of what a second factory can share with the first."),
    ]))

# ------------------------------------------------------------------ 2. Problems of manufacturing
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Problems of manufacturing in Cameroon and responses",
    lesson="cmrdev-problems-of-manufacturing",
    questions=[
        MC("Which of these is a problem of manufacturing in Cameroon?", [
            C("Regular, cheap electricity", why="Steady cheap power would help, not harm."),
            C("Frequent power cuts", correct=True),
            C("Very short transport distances", why="Transport costs are a problem, not short distances."),
            C("Too many skilled technicians", why="Shortage of skills, not too many, is the problem."),
        ], steps=[S("Recall", text="Power cuts stop machines and raise costs. They are a main problem.")],
           concept="Problems of manufacturing", skill="Recall", hint="Think of what happens to a machine without electricity."),
        MC("Why does a shortage of capital limit manufacturing?", [
            C("Firms cannot buy machines or expand", correct=True),
            C("Workers cannot go to school", why="This is unrelated to capital in a firm."),
            C("Roads become longer", why="Capital shortage does not change road length."),
            C("Imports become cheaper", why="Prices of imports depend on other factors."),
        ], steps=[S("Link the cause to its effect", text="Capital pays for machines and growth. Without it, firms stay small.")],
           concept="Shortage of capital", skill="Concept", hint="What does a firm need money for?"),
        MC("Which response best matches the problem of poor roads and port delays?", [
            C("Opening more primary schools", why="Schools help skills, not transport."),
            C("Printing more money", why="This does not improve transport."),
            C("Repairing roads and improving port handling", correct=True),
            C("Closing factories in the interior", why="Closing factories removes jobs and does not fix transport."),
        ], steps=[S("Match problem and solution", text="Transport problems need better roads, railways and port handling.")],
           concept="Solutions to transport problems", skill="Application", hint="Choose the answer that directly improves transport."),
        MC("Why do cheap imports harm local manufacturers?", [
            C("They are always of better quality", why="Price, not quality, is the main point here."),
            C("They give workers more skills", why="Imports do not train workers."),
            C("They remove all taxes", why="Imports do not remove taxes on local firms."),
            C("They sell at lower prices, so local firms lose customers", correct=True),
        ], steps=[S("Competition", text="A customer who sees a cheaper imported good may buy it instead of the local product.")],
           concept="Competition from imports", skill="Reasoning", hint="Imagine two similar goods with different prices."),
        MC("A factory owner in Bafoussam says that he can only hire untrained workers and must call technicians from abroad. Which problem does he describe?", [
            C("Small market", why="This concerns buyers, not workers."),
            C("Shortage of skilled labour", correct=True),
            C("High taxation", why="The owner mentions workers, not taxes."),
            C("Power shortage", why="The owner mentions workers, not electricity."),
        ], steps=[S("Identify", text="Untrained workers and outside technicians show a shortage of skills.")],
           concept="Shortage of skills", skill="Application", hint="Look at the type of worker that he cannot find."),
        MC("Which action would most directly increase the market for Cameroonian manufactured goods?", [
            C("Trading freely with neighbouring countries in a regional group", correct=True),
            C("Closing the border to all goods", why="This reduces trade and market size."),
            C("Increasing power cuts", why="Power cuts raise costs and reduce output."),
            C("Reducing the number of schools", why="This does not enlarge markets and harms skills."),
        ], steps=[S("Market size", text="Regional trade groups give firms access to more customers.")],
           concept="Market size and regional trade", skill="Application", hint="A bigger market means more buyers beyond one country."),
        MC("Which statement best explains why problems of manufacturing are said to be linked?", [
            C("Each problem has nothing to do with the others", why="They interact: poor power raises costs, which weakens competition."),
            C("Better roads and power lower costs, which helps firms compete with imports", correct=True),
            C("Only taxes matter", why="Taxes are one of several problems."),
            C("Solving one problem always solves all the others", why="One solution rarely solves everything."),
        ], steps=[S("Linked problems", text="Power, transport, skills and capital together decide costs. Solving several together works best.")],
           concept="Linked problems", skill="Reasoning", hint="Think of how power cuts and competition affect each other."),
        MC("A firm has frequent power cuts, buys a generator and finds its prices are higher than those of imports. Which sequence is correct?", [
            C("Power cuts, generator cost, higher production cost, lower competitiveness", correct=True),
            C("Generator cost, power cuts, lower costs, higher competitiveness", why="Generators add cost; they do not reduce it."),
            C("Higher prices, then fewer cuts, then more skills", why="Prices do not reduce power cuts."),
            C("Power cuts, lower costs, more profits", why="Power cuts raise costs and lower profits."),
        ], steps=[S("Chain of effects", text="Cuts lead to generator costs, so production costs rise, so the price is higher than imports.")],
           concept="Cause and effect chain", skill="Reasoning", hint="Follow the cost step by step from cuts to final price."),
    ]))

# ------------------------------------------------------------------ 3. The informal sector
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="The informal sector in Cameroon",
    lesson="cmrdev-the-informal-sector",
    questions=[
        MC("Which best defines the informal sector?", [
            C("Large registered firms that pay all taxes", why="That describes the formal sector."),
            C("Government departments", why="Government offices are part of the formal sector."),
            C("Small activities that are mostly unregistered and lightly taxed, using little capital", correct=True),
            C("All farming in the country", why="Not all farming is informal, and informality is not defined by farming."),
        ], steps=[S("Recall the definition", text="The informal sector is made up of small, mostly unregistered, lightly taxed activities with little capital.")],
           concept="Definition of the informal sector", skill="Recall", hint="Think of a small seller who is not registered."),
        MC("Which of these is an informal activity?", [
            C("A bank clerk with a contract", why="A bank job is formal, with a contract and registered employer."),
            C("A roadside tailor who works alone", correct=True),
            C("A civil servant", why="Civil servants work in the formal sector."),
            C("A factory manager in a registered firm", why="A registered factory is formal."),
        ], steps=[S("Spot the informal job", text="Self-employed, unregistered and small: the roadside tailor.")],
           concept="Examples of informal work", skill="Recall", hint="Choose the one who works alone, with little capital."),
        MC("Which is a reason for the rapid growth of the informal sector?", [
            C("There are more formal jobs than workers", why="The opposite is true: formal jobs are too few."),
            C("Starting a small business needs little money", correct=True),
            C("Everyone has a high income", why="Low incomes push people into informal work."),
            C("Towns are becoming smaller", why="Towns are growing, not shrinking."),
        ], steps=[S("Reasons", text="Easy, cheap entry is a main reason. People can start with small savings.")],
           concept="Reasons for growth", skill="Concept", hint="Think of what stops people from starting formal firms."),
        MC("How does rural-urban migration help to explain the growth of the informal sector?", [
            C("Migrants always find formal jobs at once", why="Most formal jobs are scarce."),
            C("Migrants leave towns and return to villages", why="This reverses the movement described."),
            C("Migrants cannot do any work", why="Migrants work; they just work informally."),
            C("Many migrants reach towns without formal jobs and create their own work", correct=True),
        ], steps=[S("Link migration and work", text="Towns receive more people than formal jobs. Migrants trade, drive and repair to earn.")],
           concept="Rural-urban migration and informal work", skill="Reasoning", hint="What happens to people who arrive in a town with no job?"),
        MC("Which is an advantage of the informal sector to the economy?", [
            C("It gives work and income to many people", correct=True),
            C("It pays high taxes to the government", why="Informal firms pay little tax."),
            C("It gives all workers pensions", why="Few informal workers have pensions."),
            C("It removes congestion from towns", why="Informal trade and transport often add to congestion."),
        ], steps=[S("Benefit", text="Jobs and income are its main benefit, especially for young people and women.")],
           concept="Importance of the informal sector", skill="Recall", hint="Which choice is a benefit of work that is easy to enter?"),
        MC("Which is a challenge faced by informal workers?", [
            C("Large, steady wages", why="Wages are usually small and unsteady."),
            C("Social insurance and pensions", why="These are mostly missing, which is the problem."),
            C("Low, unstable income and little protection", correct=True),
            C("Free bank loans", why="Informal workers often cannot get loans."),
        ], steps=[S("Challenge", text="No contract or insurance means income is low and risky.")],
           concept="Challenges of the informal sector", skill="Concept", hint="Choose the problem, not the benefit."),
        NUM("In an imaginary town (exercise data), 600 of the 1000 working people work in the informal sector. What percentage of the workers is this?", 60,
            steps=[S("Compute the percentage", math=r"\frac{600}{1000} \times 100 = 60")],
            tolerance=0.5, unit="%", concept="Share of informal workers", skill="Calculation",
            hint="Divide the informal workers by all workers, then multiply by 100."),
        MC("A town council builds a covered market, offers cheap registration and runs training for traders. What is its likely aim?", [
            C("To remove all traders from the town", why="The aim is to help traders improve, not to remove them."),
            C("To help informal traders work safely and improve, while keeping the town clean and safe", correct=True),
            C("To stop all trade", why="This would harm the economy and workers."),
            C("To raise food prices", why="The measures do not aim to raise prices."),
        ], steps=[S("Purpose of the measures", text="Better markets, easy registration and training help informal firms improve and reduce rubbish and congestion.")],
           concept="Responses to informal sector problems", skill="Application", hint="Think about helping, not punishing, informal traders."),
    ]))


# ------------------------------------------------------------------ 4. Transport systems and distribution
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Transport systems and networks in Cameroon",
    lesson="cmrdev-transport-systems-and-their-distribution",
    questions=[
        MC("Which type of transport carries most people and goods in Cameroon?", [
            C("Air transport", why="Air transport is fast but costly and used by few."),
            C("Road transport", correct=True),
            C("Pipeline", why="Pipelines carry oil, not people."),
            C("River transport", why="Rivers are used only in some places."),
        ], steps=[S("Recall", text="Roads reach most towns and villages. Most goods and passengers travel by road.")],
           concept="Types of transport", skill="Recall", hint="Think of what a market trader uses most days."),
        MC("The railway in Cameroon runs from Douala to Yaounde and continues to which northern town?", [
            C("Ngaoundere", correct=True),
            C("Maroua", why="The line ends before Maroua; Maroua is further north."),
            C("Bamenda", why="Bamenda is in the western highlands and is not on this line."),
            C("Limbe", why="Limbe is a coastal town west of Douala."),
        ], steps=[S("Follow the line", text="The main line goes Douala, Yaounde, then Ngaoundere. On the map the dashed line ends at D.")],
           concept="Main railway", skill="Interpretation", hint="Look at where the dashed line ends.",
           diagram=PMAP, diagram_alt=PMAP_ALT),
        MC("On the map, which letter marks Kribi, the deep-sea port on the south coast?", [
            C("A", why="A is Douala, the larger and older port."),
            C("B", why="B is Yaounde, which is inland."),
            C("C", correct=True),
            C("E", why="E is Limbe, west of Douala."),
        ], steps=[S("Locate the port", text="Kribi is on the coast south of Douala. That is letter C.")],
           concept="Location of Kribi port", skill="Interpretation", hint="Look south of Douala along the coast.",
           diagram=PMAP, diagram_alt=PMAP_ALT),
        MC("Chad and the Central African Republic have no sea coast. Which port in Cameroon helps them trade with the world?", [
            C("Maroua", why="Maroua is an inland town and not a sea port."),
            C("Bamenda", why="Bamenda is inland."),
            C("Bertoua", why="Bertoua is an inland town."),
            C("Douala", correct=True),
        ], steps=[S("Landlocked trade", text="Landlocked countries use Douala port and the road and rail links.")],
           concept="Role of Douala port", skill="Application", hint="Which sea port is the main one?"),
        MC("Which statement best describes the distribution of transport networks in Cameroon?", [
            C("Equally dense everywhere", why="Networks are much denser in some areas."),
            C("Dense in the east and sparse near the coast", why="This is the opposite of the real pattern."),
            C("Dense in the south-west and centre and sparse in the east and the far north", correct=True),
            C("Found only along the coast", why="Roads and railways extend inland."),
        ], steps=[S("Pattern", text="The south-west and centre have more people, ports and industries.")],
           concept="Distribution of networks", skill="Concept", hint="Where are the biggest towns and ports?"),
        MC("Which factor best explains why roads are few in the thick forests of the south-east?", [
            C("Few people and high building cost", correct=True),
            C("Too many industries", why="The area has few industries."),
            C("Too many airports", why="Airports are few."),
            C("A very dense population", why="Population is sparse."),
        ], steps=[S("Explain", text="Low population gives low demand, and dense forest raises cost. Fewer roads result.")],
           concept="Reasons for sparse networks", skill="Reasoning", hint="Think of demand and cost."),
        MC("Which is a negative environmental effect of transport?", [
            C("More jobs for drivers", why="That is an economic benefit."),
            C("Easier access to schools", why="That is a social benefit."),
            C("Smoke from vehicles and clearing of forest for roads", correct=True),
            C("Faster delivery of goods", why="That is an economic benefit."),
        ], steps=[S("Environment", text="Vehicles pollute the air and roads clear land.")],
           concept="Environmental impact", skill="Concept", hint="Choose the harm, not the benefit."),
        MC("A new road is built into a forest area. Which is the most likely environmental effect?", [
            C("Less hunting", why="Easier access usually increases hunting."),
            C("More forest cleared and more illegal logging", correct=True),
            C("More forest regrows", why="Roads usually remove trees."),
            C("Less air pollution", why="More vehicles bring more pollution."),
        ], steps=[S("Predict", text="A road gives access, so forest is cleared and hunting and logging increase.")],
           concept="Road building and forests", skill="Application", hint="What does a road let people do?"),
    ]))


# ------------------------------------------------------------------ 5. Problems of transport and measures
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Transport problems and government measures",
    lesson="cmrdev-problems-of-transport-and-government-measures",
    questions=[
        MC("Which of these is a problem of road transport in Cameroon?", [
            C("Muddy and flooded roads in the rainy season", correct=True),
            C("Too many tarred roads", why="Many roads are untarred; tarred roads are not a problem."),
            C("Too few vehicles on every road", why="Congestion in cities is more of a problem than too few vehicles."),
            C("Roads that are always dry", why="Heavy rain damages roads in much of the country."),
        ], steps=[S("Recall", text="Rain turns untarred roads to mud and floods weak roads. This is a main problem.")],
           concept="Problems of roads", skill="Recall", hint="Think of what rain does to a road made of earth."),
        MC("Why is overloading of trucks a problem?", [
            C("It makes roads last longer", why="It does the opposite."),
            C("It lowers the price of fuel", why="Overloading does not change fuel prices."),
            C("It damages road surfaces and causes accidents", correct=True),
            C("It reduces traffic", why="It does not reduce traffic."),
        ], steps=[S("Effect", text="Heavy loads break road surfaces and make trucks hard to control.")],
           concept="Overloading", skill="Concept", hint="Think of heavy weight on a thin road."),
        NUM("In an exercise, the legal limit for a lorry is 10 tonnes. A lorry carries 14 tonnes. By how many tonnes is it overloaded?", 4,
            steps=[S("Subtract", math=r"14 - 10 = 4")], unit="tonnes",
            concept="Overloading calculation", skill="Calculation", hint="Subtract the limit from the actual load."),
        MC("Which measure best reduces traffic congestion in a large city such as Douala?", [
            C("Closing all bus routes", why="Fewer buses push more people into cars and taxis."),
            C("Building bypasses and flyovers and organising public transport", correct=True),
            C("Allowing more overloading", why="This does not reduce congestion."),
            C("Closing roads to markets", why="This disrupts trade and does not solve congestion."),
        ], steps=[S("Match measure to problem", text="Bypasses and better bus services move vehicles and people more smoothly.")],
           concept="Solving congestion", skill="Application", hint="Choose a measure that moves traffic around or carries more people per vehicle."),
        MC("How does improving the railway help the economy?", [
            C("It removes the need for ports", why="Rail links ports with the interior; it does not replace them."),
            C("It stops all road transport", why="Roads remain important."),
            C("It makes goods more expensive", why="Better rail should lower costs."),
            C("It moves heavy goods and passengers faster and more cheaply over long distances", correct=True),
        ], steps=[S("Benefit of rail", text="Trains carry large loads over long distances at lower cost per tonne.")],
           concept="Railway improvement", skill="Reasoning", hint="Think of what trains do well."),
        MC("How does the deep-sea port at Kribi help transport and trade?", [
            C("It handles larger ships and shares the work of Douala", correct=True),
            C("It is an airport", why="Kribi is a sea port."),
            C("It replaces all roads", why="Roads and rail are still needed."),
            C("It is used only for fishing", why="It is a commercial port too."),
        ], steps=[S("Port development", text="A deep-sea port can take larger ships and eases pressure on Douala.")],
           concept="Kribi deep-sea port", skill="Concept", hint="What does 'deep-sea' allow?"),
        MC("Which statement about transport problems is the most balanced?", [
            C("They are caused only by the government", why="Weather, relief, overloading and money also play a part."),
            C("They have several causes, including rain, relief, overloading and limited funds", correct=True),
            C("They have no effect on the economy", why="They raise costs and cause food loss."),
            C("They cannot be reduced", why="Many measures exist, though some take time."),
        ], steps=[S("Balanced view", text="Several causes act together, so several measures are needed.")],
           concept="Balanced view of transport problems", skill="Reasoning", hint="Choose the answer that gives more than one cause."),
        MC("Farmers in a village cannot sell tomatoes in the rainy season because the road to market is impassable and the tomatoes rot. Which measure would help most?", [
            C("Building a new airport", why="This does not help a village with a market road problem."),
            C("Raising taxes on tomatoes", why="This would not fix the road."),
            C("Building and maintaining a feeder road to the market", correct=True),
            C("Closing the market", why="This would remove the buyers."),
        ], steps=[S("Match", text="A feeder road links the village to the market and reduces food loss.")],
           concept="Feeder roads", skill="Application", hint="Fix the link between the farm and the market."),
    ]))

# ------------------------------------------------------------------ 6. Tourism potentials and factors
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Tourist potentials of Cameroon and favourable factors",
    lesson="cmrdev-tourism-potentials-and-factors",
    questions=[
        MC("What is tourism?", [
            C("Moving house to another country", why="Tourism is temporary travel for leisure or similar purposes."),
            C("Travelling for leisure, adventure or culture and the services that support it", correct=True),
            C("Growing food for sale", why="This is farming."),
            C("Making goods in a factory", why="This is manufacturing."),
        ], steps=[S("Definition", text="Tourism is travelling away from home for leisure and the services that serve visitors.")],
           concept="Meaning of tourism", skill="Recall", hint="Think of a visitor spending a short time away from home."),
        MC("The map shows letter F at a savanna wildlife park in the Far North. Which park is it?", [
            C("Lobe falls", why="The Lobe falls are on the south coast, near Kribi."),
            C("Waza National Park", correct=True),
            C("Mount Cameroon", why="Mount Cameroon is a mountain near Buea and Limbe."),
            C("Limbe", why="Limbe is a town on the coast."),
        ], steps=[S("Locate", text="F is in the Far North, where Waza National Park lies.")],
           concept="Waza National Park", skill="Interpretation", hint="Look at the far north of the map.",
           diagram=PMAP, diagram_alt=PMAP_ALT),
        MC("Which feature is the highest mountain in Cameroon and an active volcano?", [
            C("Mandara mountains", why="The Mandara mountains are in the Far North and are not volcanic peaks like this."),
            C("Lobe falls", why="These are falls, not a mountain."),
            C("Waza", why="Waza is a park."),
            C("Mount Cameroon", correct=True),
        ], steps=[S("Recall", text="Mount Cameroon is the highest peak and an active volcano near the coast.")],
           concept="Mount Cameroon", skill="Recall", hint="It stands near Buea and Limbe."),
        MC("Where are the Lobe falls found?", [
            C("Near Kribi on the south coast", correct=True),
            C("In the Far North", why="The Far North has Waza and Lake Chad."),
            C("Near Bamenda", why="Bamenda has highland scenery, not these falls."),
            C("Near Garoua", why="Garoua is on the Benue in the north."),
        ], steps=[S("Locate", text="The Lobe falls tumble near the ocean close to Kribi.")],
           concept="Lobe falls", skill="Recall", hint="They are a coastal attraction."),
        MC("Which is a cultural attraction?", [
            C("Waterfall", why="A waterfall is a natural attraction."),
            C("The palaces and festivals of the western highlands", correct=True),
            C("Volcano", why="A volcano is a natural attraction."),
            C("Beach", why="A beach is a natural attraction."),
        ], steps=[S("Classify", text="Palaces, festivals and crafts are human or cultural features.")],
           concept="Cultural attractions", skill="Concept", hint="Choose a human-made or traditional feature."),
        NUM("In an imaginary hotel (exercise data), 30 of its 40 rooms are occupied. What is the occupancy rate as a percentage?", 75,
            steps=[S("Compute", math=r"\frac{30}{40} \times 100 = 75")], unit="%", tolerance=0.5,
            concept="Hotel occupancy", skill="Calculation", hint="Divide the occupied rooms by all rooms and multiply by 100."),
        MC("On the map, which letter marks Limbe, a coastal town near Mount Cameroon?", [
            C("A", why="A is Douala."),
            C("C", why="C is Kribi, to the south."),
            C("H", why="H is Edea, inland of the coast."),
            C("E", correct=True),
        ], steps=[S("Locate", text="Limbe is on the coast west of Douala. That is letter E.")],
           concept="Location of Limbe", skill="Interpretation", hint="It is west of Douala, near the mountain.",
           diagram=PMAP, diagram_alt=PMAP_ALT),
        MC("Which factor most directly makes it easier for foreign tourists to reach Cameroon?", [
            C("International airports at Douala and Yaounde", correct=True),
            C("A very high price of hotel rooms", why="High prices discourage tourists."),
            C("Muddy roads in the rainy season", why="Poor roads discourage tourists."),
            C("A lack of guides", why="This is a constraint, not a favourable factor."),
        ], steps=[S("Accessibility", text="International airports bring visitors from other countries.")],
           concept="Factors encouraging tourism", skill="Application", hint="Think of how a visitor from overseas arrives."),
    ]))


# ------------------------------------------------------------------ 7. Constraints and impact of tourism
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Constraints, impact and development efforts in tourism",
    lesson="cmrdev-constraints-and-impact-of-tourism",
    questions=[
        MC("Which of these is a constraint to tourism development?", [
            C("Beautiful scenery", why="Scenery attracts tourists; it is a strength."),
            C("Good hotels in every town", why="Good hotels would help tourism."),
            C("Poor roads to tourist sites", correct=True),
            C("Friendly people", why="Welcoming people encourage tourism."),
        ], steps=[S("Identify", text="A constraint holds tourism back. Poor roads make sites hard to reach.")],
           concept="Constraints to tourism", skill="Recall", hint="Choose what makes a visit harder."),
        MC("Which is a positive economic effect of tourism?", [
            C("It brings foreign exchange and creates jobs", correct=True),
            C("It always lowers prices", why="Prices of land and food may rise."),
            C("It removes the need for taxes", why="Tourism adds taxes; it does not remove them."),
            C("It stops other sectors", why="It can help other sectors."),
        ], steps=[S("Benefit", text="Tourists spend money, which creates jobs and brings foreign currency.")],
           concept="Economic impact of tourism", skill="Recall", hint="Think of what visitors spend."),
        MC("Which is a negative environmental effect of tourism?", [
            C("Money for park rangers", why="This is a positive effect."),
            C("Litter and damaged mountain trails", correct=True),
            C("More jobs for guides", why="This is an economic benefit."),
            C("More foreign exchange", why="This is an economic benefit."),
        ], steps=[S("Harm", text="Many walkers produce litter and wear away trails.")],
           concept="Environmental impact of tourism", skill="Concept", hint="Choose the harm to nature."),
        MC("Hotels in a coastal town are owned by outside companies and most profits leave the area. Which negative effect is described?", [
            C("Leakage of profits", correct=True),
            C("Higher foreign exchange", why="This is a benefit."),
            C("Better conservation", why="This is an environmental benefit."),
            C("More jobs", why="This is a benefit."),
        ], steps=[S("Name the effect", text="When profits go to outside owners, local people gain less. This is leakage.")],
           concept="Leakage of tourist income", skill="Application", hint="Where does the money end up?"),
        MC("A mountain trail is eroded because too many visitors walk off the path. Which measure is the best response?", [
            C("Ban all visitors forever", why="This removes the income that protects the site."),
            C("Ignore the problem", why="Damage would grow."),
            C("Manage visitor numbers and keep walkers on marked paths", correct=True),
            C("Cut down the trees", why="This causes more damage."),
        ], steps=[S("Sustainable tourism", text="Limiting numbers and marking paths protect the site while still allowing visits.")],
           concept="Sustainable tourism", skill="Application", hint="Choose a measure that protects and still allows tourism."),
        MC("Which is a stakeholder in tourism other than the government?", [
            C("A hotel owner", correct=True),
            C("Nobody else has an interest", why="Many groups have an interest in tourism."),
            C("Only foreign visitors", why="Local owners, communities and groups are stakeholders too."),
            C("Only farmers", why="Farmers can benefit but are not the only stakeholders."),
        ], steps=[S("Define stakeholder", text="A stakeholder is anyone with an interest: hotel owners, tour firms, airlines, communities and conservation groups.")],
           concept="Stakeholders", skill="Concept", hint="Think of who earns from visitors."),
        NUM("In an exercise (imaginary data), a park earns 5 000 000 FCFA from entrance fees in a year and spends 2 000 000 FCFA on ranger pay and path repair. How many FCFA is left to spend on conservation?", 3000000,
            steps=[S("Subtract", math=r"5\,000\,000 - 2\,000\,000 = 3\,000\,000")], unit="FCFA",
            concept="Tourism income and conservation", skill="Calculation", hint="Subtract the costs from the income."),
        MC("Which statement gives the most balanced view of tourism?", [
            C("Tourism is entirely good", why="It also causes harm if poorly managed."),
            C("Tourism is entirely bad", why="It also gives jobs and funds conservation."),
            C("Tourism has no effect", why="It has clear economic and environmental effects."),
            C("Tourism brings benefits and harm, so careful management is needed", correct=True),
        ], steps=[S("Balance", text="Good planning keeps the gains and reduces the damage.")],
           concept="Balanced view of tourism", skill="Reasoning", hint="Choose the answer that mentions both sides."),
    ]))

# ------------------------------------------------------------------ 8. Reasons for slow economic growth
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Reasons for slow economic growth in Cameroon",
    lesson="cmrdev-reasons-for-slow-economic-growth",
    questions=[
        MC("What is economic growth?", [
            C("A fall in the population", why="Population change is not economic growth."),
            C("An increase in the goods and services produced by a country over time", correct=True),
            C("A rise in the number of rivers", why="This has nothing to do with the economy."),
            C("A fall in all prices", why="Falling prices are not the definition of growth."),
        ], steps=[S("Define", text="Economic growth is a rise in total output, usually measured by GDP.")],
           concept="Economic growth", skill="Recall", hint="Think of output over time."),
        MC("Which of these is an economic reason for slow growth?", [
            C("Reliance on exports of raw materials whose prices change", correct=True),
            C("Too many hydroelectric rivers", why="Rivers are a potential resource, not a cause of slow growth."),
            C("Too many ports", why="Ports are an advantage."),
            C("Too many skilled workers", why="A shortage of skills, not too many, slows growth."),
        ], steps=[S("Identify", text="Unstable raw-material prices make earnings uncertain and add little value.")],
           concept="Dependence on raw materials", skill="Concept", hint="Think of the type of goods exported."),
        MC("Why do power cuts slow economic growth?", [
            C("They lower the price of imports", why="Power cuts do not lower import prices."),
            C("They stop machines and raise costs", correct=True),
            C("They create more skilled workers", why="They do not train workers."),
            C("They increase exports", why="They usually reduce output."),
        ], steps=[S("Effect", text="Power cuts stop production and force firms to buy costly generators.")],
           concept="Power and growth", skill="Concept", hint="Think of a factory without electricity."),
        NUM("In an exercise (imaginary data), a country's output rises from 200 units to 210 units in a year. What is the percentage growth?", 5,
            steps=[S("Compute", math=r"\frac{210 - 200}{200} \times 100 = 5")], unit="%", tolerance=0.05,
            concept="Growth rate calculation", skill="Calculation", hint="Divide the increase by the starting value, then multiply by 100."),
        MC("In the exercise above, the population also rises by 6 percent. What can you say about output per person?", [
            C("It rises faster than output", why="Population grew faster than output."),
            C("It falls, because population grew faster than output", correct=True),
            C("It stays exactly the same", why="5 percent and 6 percent are not equal."),
            C("It cannot be judged", why="Comparing the two rates gives the answer."),
        ], steps=[S("Compare rates", text="Output grew 5 percent, population 6 percent, so output per person fell slightly.")],
           concept="Output and population growth", skill="Reasoning", hint="Compare 5 percent with 6 percent."),
        MC("Which is an example of weak infrastructure that slows growth?", [
            C("Reliable roads", why="Reliable roads help growth."),
            C("Poor roads and an old railway", correct=True),
            C("Cheap electricity", why="Cheap power helps growth."),
            C("Modern ports", why="Modern ports help growth."),
        ], steps=[S("Identify", text="Poor roads and an old railway raise costs and isolate farms.")],
           concept="Infrastructure and growth", skill="Recall", hint="Choose the weakness."),
        MC("Which answer shows the most balanced approach to the question 'why is growth slow?'", [
            C("Blame one cause only", why="Growth depends on several linked causes."),
            C("Say there are no problems", why="There are real constraints."),
            C("Give several linked causes without blaming a single group", correct=True),
            C("Quote exact figures from memory", why="Do not use figures you cannot check."),
        ], steps=[S("Balanced answer", text="Give several causes, link them and avoid invented figures.")],
           concept="Balanced geography answers", skill="Reasoning", hint="Choose the answer that is fair and uses several causes."),
        MC("Which chain shows how constraints are linked?", [
            C("Power cuts raise costs, local goods lose to imports, industry stays small, raw materials continue to be exported", correct=True),
            C("Tourism closes roads, roads cause rain, rain stops factories", why="This chain is not realistic."),
            C("Dams cause debt, debt causes rivers, rivers cause cocoa", why="These links do not make sense."),
            C("More schools cause less food, which causes more ports", why="These links do not make sense."),
        ], steps=[S("Linked causes", text="Power, costs, competition, small industry and raw-material exports form a chain.")],
           concept="Linked constraints", skill="Reasoning", hint="Pick the chain where each step causes the next."),
    ]))

# ------------------------------------------------------------------ 9. Measures to uplift the economy
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Measures to uplift the economy towards emergence",
    lesson="cmrdev-measures-to-uplift-the-economy",
    questions=[
        MC("Which best describes an emerging economy?", [
            C("One that depends on a single raw material", why="Emergence means a varied economy."),
            C("One with more industry and services and higher incomes shared among more people", correct=True),
            C("One with no trade", why="Trade is important for emergence."),
            C("One with no cities", why="Cities are not excluded."),
        ], steps=[S("Define", text="Emergence means a stronger, more varied economy and better living standards.")],
           concept="Meaning of emergence", skill="Recall", hint="Think of a varied economy with higher incomes."),
        MC("Which measure adds value to Cameroon's cocoa?", [
            C("Exporting beans unprocessed", why="This earns less per tonne."),
            C("Burning the cocoa trees", why="This destroys the resource."),
            C("Processing it into products in local factories", correct=True),
            C("Stopping all trade", why="This would lose income."),
        ], steps=[S("Value added", text="Processing makes more valuable products and creates local jobs.")],
           concept="Adding value", skill="Application", hint="Think of chocolate rather than beans."),
        MC("Which measure would most help factories reduce their costs?", [
            C("Steadier power supply", correct=True),
            C("More power cuts", why="More cuts raise costs."),
            C("Higher fuel taxes only", why="This raises costs."),
            C("Closing roads", why="This raises transport costs."),
        ], steps=[S("Cost reduction", text="Steady power means no generator costs and fewer stoppages.")],
           concept="Energy for industry", skill="Application", hint="Think of the problems factories face."),
        MC("Why does diversification help an economy?", [
            C("It makes a country depend on one product", why="That is the opposite of diversification."),
            C("It stops all risk", why="Risk is reduced, not removed."),
            C("It makes imports free", why="Diversification is not about imports."),
            C("A fall in the price of one product does not harm the whole economy", correct=True),
        ], steps=[S("Spread the risk", text="With many products and services, one price fall does less damage.")],
           concept="Diversification", skill="Concept", hint="Do not put all eggs in one basket."),
        MC("Which measure links most closely to the problem of a small market?", [
            C("Trading with neighbours in regional groups", correct=True),
            C("Closing the borders", why="This shrinks the market."),
            C("Banning all imports of tools", why="This does not enlarge the market."),
            C("Reducing school places", why="This does not enlarge the market."),
        ], steps=[S("Market size", text="Regional trade gives firms more customers.")],
           concept="Regional trade", skill="Application", hint="A bigger market has more buyers."),
        MC("Which statement is the most realistic about emergence?", [
            C("It will happen immediately", why="Emergence needs time and money."),
            C("It needs time, money, good management and several measures working together", correct=True),
            C("It needs only one dam", why="One project cannot do everything."),
            C("It needs no education", why="Skills are central to emergence."),
        ], steps=[S("Realism", text="Measures must be combined, planned and sustained over time.")],
           concept="Realism about development", skill="Reasoning", hint="Choose the answer that mentions several conditions."),
        MC("A village wants to earn more from its cassava. Which sequence of measures is most logical?", [
            C("Poor road, poor storage, sell raw cassava cheaply", why="This describes the problem, not a solution."),
            C("Build a road, add a small processing unit and sell packaged flour in town", correct=True),
            C("Burn the crop, stop planting, close the road", why="This destroys income."),
            C("Ban sales, stop trade, close the market", why="This removes income."),
        ], steps=[S("Chain of measures", text="Transport links, processing and market access raise income.")],
           concept="Linking measures", skill="Application", hint="Look for the sequence that adds value and links to the market."),
        MC("Which measure helps both tourism and farmers at the same time?", [
            C("Repairing roads to rural areas", correct=True),
            C("Closing all roads", why="This harms both."),
            C("Raising fares", why="This harms both."),
            C("Cutting all forests", why="This harms tourism and farmers' water supply."),
        ], steps=[S("Shared benefit", text="Better roads bring tourists to sites and let farmers reach markets.")],
           concept="Linking sectors", skill="Reasoning", hint="Which measure serves both visitors and farmers?"),
    ]))
