"""A Level Geography (0750), Upper Sixth: Agricultural Geography; Industrial, Transport & Service Geography;
Regional Development & Global Disparities practice sets, one per lesson (KKEVO draft, for reviewer checking against the syllabus and textbooks)."""

from .dsl import *  # noqa: F403

COURSE = ("geography", "upper-sixth")

M_AGR = "Agricultural Geography"
M_IND = "Industrial, Transport & Service Geography"
M_DEV = "Regional Development & Global Disparities"

SETS = []

# ---------------------------------------------------------------------------
# Agricultural Geography / Factors influencing farming
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_AGR, topic="Factors influencing farming",
    title="Physical, economic and behavioural factors: practice",
    lesson="gpu1-factors-influencing-farming",
    questions=[
        MC("Which term describes land where a crop can be grown, but only with low or unreliable yields?", [
            C("Optimum land", why="Optimum land gives the highest yield for the lowest cost."),
            C("Marginal land", correct=True),
            C("Beyond the absolute limit", why="Beyond the absolute limit the crop fails completely."),
            C("Fallow land", why="Fallow land is resting land, not a measure of suitability."),
        ], steps=[S("Recall the three zones", text="Optimum, marginal and absolute limit. Marginal land can be farmed but with low or risky returns.")],
           concept="Optimum and marginal conditions", skill="Recall",
           hint="Think of the zone between the best conditions and failure."),
        MC("Which of these is a BEHAVIOURAL factor in farming?", [
            C("The length of the growing season", why="This is a physical (climatic) factor."),
            C("The price of fertiliser", why="This is an economic factor."),
            C("A government subsidy on seed", why="This is a political or economic factor."),
            C("A farmer's attitude to risk", correct=True),
        ], steps=[S("Classify", text="Behavioural factors are about how people perceive and decide: knowledge, attitude to risk, custom and family needs.")],
           concept="Behavioural factors", skill="Concept",
           hint="Which option is about the person, not the land or the market?"),
        NUM("A lowland station at 200 m has a mean temperature of 25 degrees Celsius. Using a lapse rate of 6.5 degrees per 1 000 m, "
            "estimate the mean temperature at a farm at 1 800 m (invented figures).", 14.6,
            steps=[S("Height difference", math=r"1800 - 200 = 1600\ \text{m}"),
                   S("Temperature fall", math=r"1.6 \times 6.5 = 10.4"),
                   S("Estimate", math=r"25 - 10.4 = 14.6\ {}^\circ\text{C}")],
            tolerance=0.1, unit="degrees Celsius", concept="Altitude and temperature", skill="Calculation",
            hint="Work out the height difference first, in thousands of metres."),
        MC("A farmer sells 3 tonnes of beans at FCFA 400 000 a tonne. Variable costs are FCFA 750 000. What is the gross margin?", [
            C("FCFA 450 000", correct=True),
            C("FCFA 1 200 000", why="This is the value of output before costs are subtracted."),
            C("FCFA 1 950 000", why="Costs were added instead of subtracted."),
            C("FCFA 150 000", why="This divides or misreads the output value; output is 3 × 400 000 = 1 200 000."),
        ], steps=[S("Output value", math=r"3 \times 400\,000 = 1\,200\,000"),
                  S("Gross margin", math=r"1\,200\,000 - 750\,000 = 450\,000")],
           concept="Gross margin", skill="Calculation",
           hint="Gross margin = value of output minus variable costs."),
        MC("Crop X earns FCFA 900 000 in a good year and FCFA 100 000 in a bad year. Crop Y earns FCFA 500 000 and FCFA 400 000. "
           "Good and bad years are equally likely. Which statement is correct?", [
            C("An optimiser and a cautious farmer both choose X", why="A cautious farmer compares worst cases: X gives only 100 000."),
            C("An optimiser chooses Y because its expected value is higher", why="Y's expected value is 450 000, below X's 500 000."),
            C("An optimiser chooses X; a cautious (maximin) farmer chooses Y", correct=True),
            C("Both choose Y because it never makes a loss", why="An optimiser goes by expected value, which favours X."),
        ], steps=[S("Expected values", math=r"X: 0.5(900\,000) + 0.5(100\,000) = 500\,000;\ Y: 0.5(500\,000) + 0.5(400\,000) = 450\,000"),
                  S("Worst cases", text="X: 100 000; Y: 400 000. Maximin picks Y; the optimiser picks X.")],
           concept="Decisions under risk", skill="Reasoning",
           hint="Work out the expected value of each crop, then compare the worst cases."),
        MC("Why are farmers with insecure land tenure less likely to build terraces or plant fruit trees?", [
            C("Terraces and trees are not allowed on customary land", why="Customary land can carry terraces and trees; the issue is security of rights."),
            C("These are long-term investments, and the farmer may lose the land before they pay back", correct=True),
            C("Terraces and trees lower yields in the short and long run", why="They usually raise or protect yields in the long run."),
            C("Land tenure only affects the size of the farm", why="Tenure also affects security and willingness to invest."),
        ], steps=[S("Reason", text="Long-term improvements pay back over many years. Without secure rights the farmer may not benefit, so he or she does not invest.")],
           concept="Land tenure", skill="Reasoning",
           hint="How long does it take for a terrace or a fruit tree to pay back?"),
        MC("Neighbouring farms in the Western Highlands have the same soils and climate, but one grows vegetables for Douala and the other "
           "grows food crops for the family. Which conclusion is best supported?", [
            C("Physical factors alone explain farming patterns", why="The physical factors are the same, so they cannot explain the difference."),
            C("Soil fertility must differ between the farms", why="The question states the soils are the same."),
            C("Vegetables cannot be grown in the highlands", why="One farm does grow them."),
            C("Economic and behavioural factors explain the difference", correct=True),
        ], steps=[S("Eliminate", text="Physical factors are equal, so they cannot cause the difference."),
                  S("Conclude", text="Capital, market access, information and attitude to risk differ between the farmers.")],
           concept="Interaction of factors", skill="Application",
           hint="If the land is the same, what else can differ?"),
        MC("Which statement gives the best evaluation of the role of physical factors in farming?", [
            C("Physical factors are strongest at the margins, while economic and behavioural factors decide what is grown within the possible range", correct=True),
            C("Physical factors no longer matter because technology has removed all limits", why="Technology reduces limits at a cost, but drought and altitude still matter."),
            C("Physical factors decide exactly which crop every farmer grows", why="This is determinism; the same land supports different choices."),
            C("Physical factors matter only in rich countries", why="Poor, low-input farmers are usually more exposed to physical limits."),
        ], steps=[S("Balance", text="Physical factors set limits, strongest in extreme or risky areas; inside those limits, markets, capital and choices decide.")],
           concept="Evaluating farming factors", skill="Reasoning",
           hint="Think of limits versus choices inside the limits."),
    ]))

# ---------------------------------------------------------------------------
# Agricultural Geography / Farming systems
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_AGR, topic="Farming systems",
    title="Classifying and measuring farming systems: practice",
    lesson="gpu1-farming-systems",
    questions=[
        MC("Which pair of terms classifies farming by PURPOSE?", [
            C("Intensive and extensive", why="These classify by intensity of inputs per hectare."),
            C("Arable and pastoral", why="These classify by enterprise (crops or animals)."),
            C("Subsistence and commercial", correct=True),
            C("Shifting and permanent", why="These describe how often land is cultivated."),
        ], steps=[S("Recall", text="Purpose asks who the produce is for: the family (subsistence) or the market (commercial).")],
           concept="Classifying farming systems", skill="Recall",
           hint="Purpose means: who is the produce for?"),
        NUM("A plot is cropped for 2 years and then left fallow for 6 years. Calculate Ruthenberg's R value.", 25,
            steps=[S("Whole cycle", math=r"2 + 6 = 8\ \text{years}"),
                   S("R", math=r"R = \frac{2}{8} \times 100 = 25")],
            tolerance=0.1, concept="Ruthenberg's R value", skill="Calculation",
            hint="Divide the years of cultivation by the whole cycle, then multiply by 100."),
        MC("A system has an R value of 50. How is it classified?", [
            C("A fallow system", correct=True),
            C("Shifting cultivation", why="Shifting cultivation has R below 33."),
            C("Permanent cultivation", why="Permanent cultivation has R above 66."),
            C("Pastoral nomadism", why="R measures crop cultivation frequency, not herding."),
        ], steps=[S("Compare with thresholds", text="Below 33 shifting; 33 to 66 fallow; above 66 permanent. 50 lies in the fallow range.")],
           concept="Interpreting R", skill="Interpretation",
           hint="Recall the two threshold values, 33 and 66."),
        MC("Farm X: 3 ha, 12 workers, 15 t. Farm Y: 600 ha, 5 workers, 900 t. Which statement is correct?", [
            C("X has the higher output per worker", why="X: 15 ÷ 12 = 1.25 t; Y: 900 ÷ 5 = 180 t per worker."),
            C("Y has the higher yield per hectare", why="Y: 1.5 t/ha; X: 5 t/ha."),
            C("Both farms are extensive", why="X has 4 workers per hectare, which is labour-intensive."),
            C("X has the higher yield per hectare but the lower output per worker", correct=True),
        ], steps=[S("Yield", math=r"X: 15 \div 3 = 5;\ Y: 900 \div 600 = 1.5\ \text{t/ha}"),
                  S("Output per worker", math=r"X: 15 \div 12 = 1.25;\ Y: 900 \div 5 = 180\ \text{t}")],
           concept="Measuring intensity", skill="Calculation",
           hint="Work out yield per hectare and output per worker for both farms."),
        MC("Which description fits transhumance?", [
            C("Herders move with their families with no permanent home", why="This is nomadism."),
            C("Seasonal movement of livestock between fixed pastures, returning to a permanent base", correct=True),
            C("Animals kept all year in sheds and fed on concentrates", why="This is intensive (zero-grazing) livestock farming."),
            C("Crops grown on cleared forest plots for two years", why="This is shifting cultivation."),
        ], steps=[S("Recall", text="Transhumance is seasonal, between fixed pastures (for example highland and lowland), from a permanent settlement.")],
           concept="Pastoral systems", skill="Concept",
           hint="The key word is seasonal, between fixed places."),
        MC("According to Boserup's argument, what happens to farming as population density rises in a fallow system?", [
            C("Fallows lengthen because farmers move to towns", why="Rising density on the land shortens fallows."),
            C("Farming stays unchanged until famine occurs", why="That is closer to a Malthusian view; Boserup argued for change."),
            C("The system becomes more extensive", why="More people on the same land push the system towards intensity."),
            C("Fallows shorten and farmers adopt new methods to keep fertility, so the system intensifies", correct=True),
        ], steps=[S("Reason", text="Less land per person shortens fallow (R rises). Boserup argued this pressure pushes farmers to manure, terraces, legumes and other innovations.")],
           concept="Intensification", skill="Reasoning",
           hint="What happens to the length of fallow when there are more people per hectare?"),
        MC("A smallholder near Bamenda grows cabbages and carrots on 0.5 ha with family labour and manure and sells them in town. Classify the farm.", [
            C("Intensive, commercial, arable", correct=True),
            C("Extensive, subsistence, arable", why="High inputs on a tiny plot and sale in town make it intensive and commercial."),
            C("Intensive, subsistence, pastoral", why="Vegetables are crops and they are sold."),
            C("Extensive, commercial, mixed", why="There are no animals, and inputs per hectare are high."),
        ], steps=[S("Intensity", text="High labour and manure on 0.5 ha: intensive."),
                  S("Purpose and enterprise", text="Sold in town: commercial. Vegetables only: arable.")],
           concept="Classifying a farm", skill="Application",
           hint="Use all three criteria: intensity, purpose, enterprise."),
        MC("Which is the strongest criticism of shifting cultivation where population is rising?", [
            C("It uses too much fertiliser", why="Shifting cultivation uses little or no fertiliser."),
            C("Its yields per hectare are always higher than permanent systems", why="This is not a criticism and is not true."),
            C("Shortened fallows stop the soil recovering, so yields fall and erosion and deforestation increase", correct=True),
            C("It needs expensive machines", why="It relies on hand tools and fire."),
        ], steps=[S("Link", text="The system is sustainable only with long fallow. Higher density shortens fallow, breaking the fertility cycle.")],
           concept="Evaluating shifting cultivation", skill="Reasoning",
           hint="What does the system need in order to restore fertility?"),
    ]))

# ---------------------------------------------------------------------------
# Agricultural Geography / Von Thünen's model
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_AGR, topic="Von Thünen's model",
    title="Locational rent and the Von Thünen rings: practice",
    lesson="gpu1-von-thunen-model",
    questions=[
        MC("In Von Thünen's model, what is locational rent?", [
            C("The rent a landlord charges a tenant under a written lease", why="Locational rent is an economic return, not a contract rent."),
            C("The cost of transporting one tonne one kilometre", why="That is the freight rate f."),
            C("The net return per hectare after production and transport costs", correct=True),
            C("The market price of the crop", why="Price p is only one part of the calculation."),
        ], steps=[S("Recall", text="R = Y(p − c) − Yfd: what is left from a hectare after production and transport costs.")],
           concept="Locational rent", skill="Recall",
           hint="Think of what is left after all costs are paid."),
        NUM("A crop has Y = 4 t/ha, p − c = FCFA 50 000 per tonne and f = FCFA 1 000 per tonne-km. Calculate its locational rent per hectare at 20 km.", 120000,
            steps=[S("Intercept", math=r"Y(p - c) = 4 \times 50\,000 = 200\,000"),
                   S("Transport cost at 20 km", math=r"Yfd = 4 \times 1\,000 \times 20 = 80\,000"),
                   S("Rent", math=r"R = 200\,000 - 80\,000 = 120\,000")],
            unit="FCFA per hectare", concept="Locational rent equation", skill="Calculation",
            hint="Use R = Y(p − c) − Yfd."),
        NUM("For the same crop (p − c = FCFA 50 000 per tonne, f = FCFA 1 000 per tonne-km), at what distance does rent fall to zero?", 50,
            steps=[S("Set R = 0", math=r"d_{\max} = \frac{p - c}{f} = \frac{50\,000}{1\,000} = 50")],
            unit="km", concept="Margin of cultivation", skill="Calculation",
            hint="Set R = 0 and solve for d; the yield cancels."),
        MC("Use the graph. At what distance does maize replace vegetables as the land use that pays the highest rent?", [
            C("About 16 km", why="16 km is where vegetable rent reaches zero, but maize already pays more before that."),
            C("About 10 km", correct=True),
            C("About 30 km", why="30 km is the boundary between maize and cattle."),
            C("About 40 km", why="40 km is maize's margin of cultivation."),
        ], steps=[S("Read the graph", text="Find where the vegetable line crosses the maize line: at 10 km, both pay 300 thousand FCFA."),
                  S("Rule", text="A ring boundary is where two rent lines cross, not where one reaches zero.")],
           concept="Ring boundaries", skill="Interpretation",
           hint="Look for the crossing point of two lines.",
           diagram="algpu1-thunen-rent-q.svg",
           diagram_alt="Graph of locational rent against distance with three falling lines: vegetables from 800 thousand to zero at 16 km, maize from 400 thousand to zero at 40 km, cattle from 160 thousand to zero at 80 km. No crossing points are marked."),
        MC("Product P: R = 500 000 − 25 000d. Product Q: R = 200 000 − 5 000d. Where is the boundary between their rings?", [
            C("At 20 km", why="20 km is P's margin of cultivation (500 000 ÷ 25 000)."),
            C("At 40 km", why="40 km is Q's margin of cultivation."),
            C("At 12 km", why="This comes from dividing 300 000 by 25 000; the slopes must be subtracted first."),
            C("At 15 km", correct=True),
        ], steps=[S("Set equal", math=r"500\,000 - 25\,000d = 200\,000 - 5\,000d"),
                  S("Solve", math=r"20\,000d = 300\,000 \Rightarrow d = 15")],
           concept="Ring boundaries", skill="Calculation",
           hint="Set the two rent equations equal."),
        MC("Why are fresh vegetables and milk found in the inner ring?", [
            C("They have high yields per hectare and high freight costs, so their rent falls steeply with distance", correct=True),
            C("They need the most fertile soil, which is found near towns", why="The model assumes uniform soil everywhere."),
            C("Their margin of cultivation is the furthest from the market", why="Steep gradients give a short margin, not a long one."),
            C("Government rules keep them near towns", why="The isolated state has no government intervention."),
        ], steps=[S("Slope", text="The slope of the rent line is −Yf. Perishable, bulky products have a high Y and high f, so a steep line that wins near the market and loses further out.")],
           concept="Rent gradient", skill="Reasoning",
           hint="Think about the slope term Yf."),
        MC("A new refrigerated lorry service halves the freight rate for milk. According to the model, what happens to the dairy zone?", [
            C("It shrinks towards the market", why="Lower transport cost makes rent fall less steeply, so the zone expands."),
            C("It disappears", why="Dairying becomes more profitable, not less."),
            C("It expands outwards because the rent line becomes less steep", correct=True),
            C("It is unchanged because transport is not in the model", why="Transport cost is the core of the model."),
        ], steps=[S("Effect on f", text="f falls, so slope −Yf is gentler and the margin (p − c)/f doubles."),
                  S("Effect on land use", text="Dairy outbids other uses further from the market, so its ring widens.")],
           concept="Modifying the model", skill="Application",
           hint="Which part of the equation does the lorry change?"),
        MC("Which statement best summarises Sinclair's criticism of Von Thünen?", [
            C("Farmers near rivers earn more rent", why="This describes a modification of Von Thünen's own model."),
            C("Land use depends only on soil quality", why="Sinclair's argument is about urban growth, not soil."),
            C("Transport costs have risen since 1826", why="Transport costs have generally fallen."),
            C("At the edge of growing cities, land nearest the city is farmed less intensively because farmers expect to sell it for building", correct=True),
        ], steps=[S("Recall", text="Sinclair (1967) found intensity can rise with distance at the urban fringe: speculation on urban land discourages investment in farming.")],
           concept="Evaluating Von Thünen", skill="Concept",
           hint="Think about what farmers expect to happen to land next to a growing city."),
    ]))

# ---------------------------------------------------------------------------
# Agricultural Geography / The Green Revolution and agrarian reform
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_AGR, topic="The Green Revolution and agrarian reform",
    title="Green Revolution gains and costs, and types of reform: practice",
    lesson="gpu1-green-revolution-agrarian-reform",
    questions=[
        MC("Which combination best describes the Green Revolution package?", [
            C("High-yielding seed, fertiliser, pesticides and irrigation, with credit and advice", correct=True),
            C("Land redistribution and cooperatives", why="These are agrarian reform measures."),
            C("Shifting cultivation with longer fallows", why="This is a traditional extensive system."),
            C("Organic manure and traditional seed only", why="The package relied on new seed and chemical inputs."),
        ], steps=[S("Recall", text="HYVs only perform with water, fertiliser and pest control, supported by credit and extension.")],
           concept="Green Revolution package", skill="Recall",
           hint="Think of everything a high-yielding variety needs to give its high yield."),
        NUM("Wheat yields rise from 1.2 t/ha to 3.0 t/ha. Calculate the percentage increase.", 150,
            steps=[S("Change", math=r"3.0 - 1.2 = 1.8"), S("Percentage", math=r"\frac{1.8}{1.2} \times 100 = 150")],
            tolerance=0.5, unit="%", concept="Yield change", skill="Calculation",
            hint="Divide the change by the original yield."),
        MC("An HYV package costs FCFA 400 000 per hectare and yields 4 t/ha. What is the cost per tonne?", [
            C("FCFA 1 600 000", why="This multiplies instead of dividing."),
            C("FCFA 400 000", why="This is the cost per hectare, not per tonne."),
            C("FCFA 100 000", correct=True),
            C("FCFA 40 000", why="This divides by 10 instead of by the yield of 4 t."),
        ], steps=[S("Divide cost by output", math=r"400\,000 \div 4 = 100\,000")],
           concept="Cost per tonne", skill="Calculation",
           hint="Cost per tonne = cost per hectare ÷ tonnes per hectare."),
        MC("Why do poor farmers often face a greater risk with the HYV package than with traditional varieties?", [
            C("HYVs always yield less than traditional seed", why="In good conditions HYVs yield much more."),
            C("HYVs cannot be sold", why="HYV output is sold like any other grain."),
            C("Traditional seed needs more irrigation", why="It is the HYVs that depend on reliable water."),
            C("High input costs are paid before harvest, so a bad season can leave them with a loss and debt", correct=True),
        ], steps=[S("Reason", text="The package costs more per hectare. If yields fall, revenue may not cover the inputs, and the loss is larger than with low-cost traditional seed.")],
           concept="Risk of the package", skill="Reasoning",
           hint="Compare what is spent before harvest under each method."),
        MC("Which is an ENVIRONMENTAL cost often linked to the Green Revolution in irrigated areas?", [
            C("Higher yields per hectare", why="This is a gain, not a cost."),
            C("Falling water tables and salinisation from heavy irrigation", correct=True),
            C("Landless labourers losing work to machines", why="This is a social cost."),
            C("Dependence on buying seed every season", why="This is an economic cost."),
        ], steps=[S("Classify", text="Over-pumping groundwater and poor drainage cause falling water tables, waterlogging and salt build-up: environmental costs.")],
           concept="Effects of the Green Revolution", skill="Concept",
           hint="Look for the effect on water and soil."),
        MC("Which type of reform gives a farmer a written title so the land can be used as security for a loan?", [
            C("Consolidation", why="Consolidation merges scattered plots; it need not give a title."),
            C("Collectivisation", why="Collectivisation pools land under group control."),
            C("Registration and titling", correct=True),
            C("Tenancy reform", why="Tenancy reform protects tenants but does not make them owners with a title."),
        ], steps=[S("Recall", text="Titling records ownership in writing; a title can be pledged as collateral to a bank.")],
           concept="Types of agrarian reform", skill="Recall",
           hint="Which reform produces a legal document?"),
        MC("A government breaks up large estates and gives the land to landless families, but gives no credit, seed or advice. What is the most likely short-term result?", [
            C("Output may fall because the new owners lack capital and inputs", correct=True),
            C("Output will certainly double", why="Land alone does not provide the inputs needed to farm well."),
            C("Inequality will rise sharply", why="Redistribution reduces inequality in land ownership."),
            C("Mechanisation will spread quickly", why="Small new owners without credit cannot buy machines."),
        ], steps=[S("Reason", text="Redistribution improves equity, but production needs seed, tools, credit and markets; without them yields often fall at first.")],
           concept="Evaluating land reform", skill="Application",
           hint="What else besides land does a farmer need?"),
        MC("Which conclusion about the Green Revolution and agrarian reform is best supported?", [
            C("Technology alone always reduces rural inequality", why="Green Revolution gains went first to those with land, water and credit."),
            C("Land reform alone always raises output", why="New owners without inputs may produce less."),
            C("Neither has had any effect on yields", why="The Green Revolution raised yields greatly in irrigated areas."),
            C("They work best together: secure, fair access to land plus affordable inputs, credit and markets", correct=True),
        ], steps=[S("Synthesise", text="Technology on unreformed land widened inequality; reform without technology often failed to raise output. Combined, they reinforce each other.")],
           concept="Technology and reform", skill="Reasoning",
           hint="Think about the weakness of each when used alone."),
    ]))

# ---------------------------------------------------------------------------
# Agricultural Geography / Food security
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_AGR, topic="Food security",
    title="The four pillars, food needs and self-sufficiency: practice",
    lesson="gpu1-food-security",
    questions=[
        MC("Which pillar of food security is about whether the body can make good use of the food eaten?", [
            C("Availability", why="Availability is about whether food is present."),
            C("Access", why="Access is about whether people can obtain food."),
            C("Stability", why="Stability is about the other pillars holding over time."),
            C("Utilisation", correct=True),
        ], steps=[S("Recall", text="Utilisation covers diet quality, clean water, sanitation, health and food safety.")],
           concept="Four pillars of food security", skill="Recall",
           hint="Think of water, health and diet."),
        NUM("A household of 4 needs 2 100 kcal per person per day. Using 3 600 kcal per kg of maize, how many kilograms of maize does it need for 30 days?", 70,
            steps=[S("Daily energy", math=r"4 \times 2\,100 = 8\,400\ \text{kcal}"),
                   S("Daily maize", math=r"8\,400 \div 3\,600 = 2.33\ \text{kg}"),
                   S("30 days", math=r"\frac{8\,400 \times 30}{3\,600} = 70\ \text{kg}")],
            tolerance=0.5, unit="kg", concept="Household food needs", skill="Calculation",
            hint="Find total kilocalories needed, then divide by kilocalories per kilogram."),
        MC("A country produces 600 000 t of a cereal, imports 200 000 t and exports 50 000 t. What is its self-sufficiency ratio?", [
            C("75%", why="This divides by 800 000 and forgets to subtract exports."),
            C("80%", correct=True),
            C("300%", why="This divides production by imports."),
            C("109%", why="This leaves out imports: 600 000 ÷ 550 000. Domestic supply includes imports."),
        ], steps=[S("Domestic supply", math=r"600\,000 + 200\,000 - 50\,000 = 750\,000"),
                  S("SSR", math=r"\frac{600\,000}{750\,000} \times 100 = 80\%")],
           concept="Self-sufficiency ratio", skill="Calculation",
           hint="SSR = production ÷ (production + imports − exports) × 100."),
        MC("Which statement best summarises Sen's entitlement approach?", [
            C("Famines are caused only by population growing faster than food supply", why="This is a Malthusian view, which Sen challenged."),
            C("Famines happen only in countries without farms", why="Sen studied famines in farming societies."),
            C("Famines can occur without a fall in food supply when groups lose the means to obtain food", correct=True),
            C("Food aid always prevents famine", why="Sen's argument is about access and entitlements, not aid."),
        ], steps=[S("Recall", text="Sen (1981): people starve when their entitlements (wages, crops, assets, prices) collapse, even if total supply is adequate.")],
           concept="Entitlement approach", skill="Concept",
           hint="Sen moved attention from supply to access."),
        MC("A farmer loses a quarter of her stored maize to weevils and damp each year. Which measure tackles this cause most directly?", [
            C("Hermetic storage bags and improved granaries", correct=True),
            C("A new tarred road to the market", why="Roads help access and prices, not losses in storage."),
            C("Emergency food aid", why="Aid treats the shortage, not the cause of the loss."),
            C("A larger farm", why="A larger farm still loses a quarter in poor storage."),
        ], steps=[S("Match cause and measure", text="The cause is post-harvest loss; the direct remedy is better storage and drying.")],
           concept="Post-harvest losses", skill="Application",
           hint="Match the measure to the cause of the loss."),
        MC("Families in a dry area eat well after harvest but go hungry for three months before the next harvest every year. Which pillar is weakest?", [
            C("Availability, because the area grows no food", why="The area does grow food; the problem is how supply varies through the year."),
            C("Stability", correct=True),
            C("Utilisation", why="The problem is the timing of supply, not the body's use of food."),
            C("None, because they eat well after harvest", why="Seasonal hunger is food insecurity."),
        ], steps=[S("Identify", text="A seasonal lean period means supply and access do not hold over time: stability fails.")],
           concept="Stability pillar", skill="Interpretation",
           hint="The key word is 'every year before the harvest'."),
        MC("Which is the strongest argument AGAINST relying on long-term food aid?", [
            C("Food aid cannot reach any emergency", why="Food aid often saves lives in emergencies."),
            C("Food aid always contains unsafe food", why="This is an unsupported generalisation."),
            C("Food aid raises local prices so farmers produce too much", why="Large free supplies tend to LOWER local prices."),
            C("Prolonged free food can depress local prices, discourage local farmers and create dependence", correct=True),
        ], steps=[S("Evaluate", text="Aid is vital in crises but, if prolonged, it can undercut local producers and weaken long-term availability.")],
           concept="Evaluating food aid", skill="Reasoning",
           hint="Think about the effect of free food on local farmers' prices."),
        MC("A region has good harvests, but many children are malnourished because of unsafe water and diarrhoea. Which strategy best fits?", [
            C("Higher-yielding seed", why="Availability is already good."),
            C("A national grain reserve", why="Reserves address stability, not the body's use of food."),
            C("Clean water, sanitation and nutrition education", correct=True),
            C("Export bans on cereals", why="Export bans affect supply and prices, not disease."),
        ], steps=[S("Diagnose", text="Food is available; disease stops the body using it, so utilisation is weak."),
                  S("Match", text="Water, sanitation, health care and nutrition education improve utilisation.")],
           concept="Matching strategies to pillars", skill="Application",
           hint="Which pillar is affected by disease and water?"),
    ]))

# ---------------------------------------------------------------------------
# Industrial, Transport & Service Geography / Industrial location theories
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_IND, topic="Industrial location theories",
    title="Weber, Smith and Lösch: practice",
    lesson="gpu1-industrial-location-theories",
    questions=[
        MC("In Weber's theory, which kind of material pulls a factory towards its source?", [
            C("A ubiquitous material", why="Ubiquitous materials are everywhere, so they pull nowhere."),
            C("A pure material", why="A pure material keeps its weight, so it does not especially pull towards its source."),
            C("A weight-losing (gross) localised material", correct=True),
            C("Any material carried by road", why="The mode of transport is not the key; weight loss is."),
        ], steps=[S("Recall", text="Carrying the waste part of a weight-losing material is costly, so processing near the source saves transport.")],
           concept="Types of material", skill="Recall",
           hint="Which material loses weight in processing?"),
        NUM("A product weighing 2 t is made from 5 t of ore and 1 t of fuel, both localised. Calculate the material index.", 3,
            steps=[S("Localised materials", math=r"5 + 1 = 6\ \text{t}"), S("MI", math=r"6 \div 2 = 3")],
            tolerance=0.01, concept="Material index", skill="Calculation",
            hint="Divide the weight of localised materials by the weight of the product."),
        MC("Use the figure. Each tonne of product needs 2 t of A from M1 and 1.5 t of B from M2; 1 t of product goes to K. What is the total movement for a factory at M2?", [
            C("150 t-km", why="This is the total for a factory at M1."),
            C("180 t-km", why="This is the total for a factory at K."),
            C("100 t-km", why="This adds the distances 60 + 40 without multiplying by the weights."),
            C("160 t-km", correct=True),
        ], steps=[S("Multiply weights by distances", math=r"2(60) + 1.5(0) + 1(40) = 160")],
           concept="Tonne-kilometres", skill="Calculation",
           hint="Multiply each weight by its distance from M2, then add.",
           diagram="algpu1-weber-triangle.svg",
           diagram_alt="Location triangle: M1 (material A), M2 (material B), market K. Road distances M1 to M2 60 km, M1 to K 60 km, M2 to K 40 km, with a point P inside."),
        MC("What is an isodapane?", [
            C("A line joining places of equal extra transport cost compared with the least-cost point", correct=True),
            C("A line joining places of equal labour cost", why="Labour costs are compared with isodapanes, but isodapanes show transport cost."),
            C("The boundary of a firm's market area", why="Market areas belong to Lösch's approach."),
            C("A line of equal land rent", why="This is a bid-rent idea from Von Thünen and urban models."),
        ], steps=[S("Recall", text="Isodapanes are contours of equal additional transport cost around the least-transport-cost point.")],
           concept="Isodapanes", skill="Concept",
           hint="'Iso' means equal; what cost is being mapped?"),
        MC("A cheap-labour town saves FCFA 30 000 per tonne in wages. It lies on the FCFA 22 000 isodapane. According to Weber, the firm should:", [
            C("stay at the least-transport-cost point", why="The labour saving is larger than the extra transport cost."),
            C("move to the town, saving FCFA 8 000 per tonne overall", correct=True),
            C("move to the town, saving FCFA 52 000 per tonne", why="The extra transport cost must be subtracted, not added."),
            C("move to the market", why="The comparison is between the optimum and the labour site."),
        ], steps=[S("Compare", math=r"30\,000 - 22\,000 = 8\,000"),
                  S("Decide", text="The town lies inside the critical isodapane, so the factory deviates to cheap labour.")],
           concept="Labour deviation", skill="Application",
           hint="Subtract the extra transport cost from the labour saving."),
        NUM("Cost per unit is FCFA 80 000 at the optimum and rises by FCFA 2 500 per km. Revenue is FCFA 95 000 per unit everywhere. How far from the optimum is the spatial margin to profitability?", 6,
            steps=[S("Set cost equal to revenue", math=r"80\,000 + 2\,500d = 95\,000"), S("Solve", math=r"d = \frac{15\,000}{2\,500} = 6")],
            tolerance=0.01, unit="km", concept="Spatial margins to profitability", skill="Calculation",
            hint="Find where the space-cost curve meets the space-revenue line."),
        MC("Which statement best describes Lösch's approach?", [
            C("Firms minimise transport costs between fixed material sites", why="That is Weber's least-cost approach."),
            C("Firms seek any site that gives a profit", why="That is Smith's idea of spatial margins."),
            C("Firms stay where they are because of sunk costs", why="That is industrial inertia."),
            C("Firms seek the site of maximum profit, considering how demand varies, giving hexagonal market areas", correct=True),
        ], steps=[S("Recall", text="Lösch focused on demand and revenue over space, not only cost, and derived hexagonal market areas under competition.")],
           concept="Lösch's profit-maximising theory", skill="Concept",
           hint="Lösch added demand to the analysis."),
        MC("Which is the strongest criticism of Weber's theory for modern industry?", [
            C("It cannot explain any industry at all", why="It still explains many heavy, weight-losing industries."),
            C("Many industries are footloose and transport costs are no longer proportional to distance", correct=True),
            C("It ignores transport costs", why="Transport cost is the centre of the theory."),
            C("It assumes firms seek maximum profit", why="Weber assumed least cost; maximum profit is Lösch."),
        ], steps=[S("Evaluate", text="Cheaper, non-linear transport, light high-value products, and incentives and markets reduce the pull of materials.")],
           concept="Evaluating location theory", skill="Reasoning",
           hint="What has changed about transport and products since 1909?"),
    ]))

# ---------------------------------------------------------------------------
# Industrial, Transport & Service Geography / Industrial agglomeration and deindustrialization
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_IND, topic="Industrial agglomeration and deindustrialization",
    title="Agglomeration, location quotients and industrial decline: practice",
    lesson="gpu1-agglomeration-deindustrialization",
    questions=[
        MC("Which statement best defines industrial agglomeration?", [
            C("The flow of components from a supplier to an assembly plant", why="This is a backward linkage, not agglomeration."),
            C("The clustering of firms in one place and the cost savings they gain from being close together", correct=True),
            C("The closure of factories in an old industrial region", why="This is deindustrialization."),
            C("A firm producing more units to lower its average cost", why="This is an internal economy of scale."),
        ], steps=[S("Recall", text="Agglomeration is the spatial cluster plus the external economies it brings.")],
           concept="Definition of agglomeration", skill="Recall",
           hint="Think of clustering in space and the savings from it."),
        MC("A car-parts maker sells its parts to a nearby car assembly plant. For the parts maker, this is:", [
            C("a backward linkage", why="A backward linkage is to a supplier of inputs."),
            C("a lateral linkage", why="Lateral links join firms supplying the same customer."),
            C("an urbanisation economy", why="This is a specific flow between two firms, not a city-wide saving."),
            C("a forward linkage", correct=True),
        ], steps=[S("Direction", text="Selling output to a customer firm is a forward linkage for the seller.")],
           concept="Industrial linkages", skill="Concept",
           hint="Is the flow going to a customer or coming from a supplier?"),
        NUM("A region employs 9 000 of its 45 000 workers in manufacturing. The nation employs 2 million of its 20 million workers in manufacturing. Calculate the location quotient.", 2,
            steps=[S("Regional share", math=r"9\,000 \div 45\,000 = 0.2"),
                   S("National share", math=r"2\,000\,000 \div 20\,000\,000 = 0.1"),
                   S("LQ", math=r"0.2 \div 0.1 = 2")],
            tolerance=0.01, concept="Location quotient", skill="Calculation",
            hint="Divide the regional share by the national share."),
        MC("A region's LQ for textiles is 0.4. What does this mean?", [
            C("Textiles are under-represented in the region compared with the nation", correct=True),
            C("Textiles employ 40 per cent of the region's workers", why="The LQ is a ratio of shares, not a share."),
            C("The region is highly specialised in textiles", why="Specialisation needs an LQ above 1."),
            C("Textile employment fell by 40 per cent", why="The LQ compares places at one time, not change over time."),
        ], steps=[S("Interpret", text="LQ below 1 means the region's share is smaller than the national share.")],
           concept="Interpreting the LQ", skill="Interpretation",
           hint="Compare the value with 1."),
        MC("Which is a DISECONOMY of agglomeration?", [
            C("Shared port and power supply", why="This is an urbanisation economy."),
            C("Specialist repair services nearby", why="This is a localisation economy."),
            C("Rising land rents and traffic congestion", correct=True),
            C("A large local market", why="This is an urbanisation economy."),
        ], steps=[S("Classify", text="Diseconomies are rising costs of being in a large cluster: congestion, high rents and wages, pollution.")],
           concept="Diseconomies of agglomeration", skill="Concept",
           hint="Look for a cost that grows as the cluster grows."),
        NUM("Manufacturing employment in a region fell from 500 000 to 175 000. Calculate the percentage fall.", 65,
            steps=[S("Fall", math=r"500\,000 - 175\,000 = 325\,000"),
                   S("Percentage", math=r"\frac{325\,000}{500\,000} \times 100 = 65")],
            tolerance=0.1, unit="%", concept="Measuring deindustrialization", skill="Calculation",
            hint="Divide the fall by the original number."),
        MC("Manufacturing output in a rich country rises, but manufacturing jobs fall. Which cause of deindustrialization best explains this?", [
            C("Exhaustion of coal and ore", why="This would reduce output, not raise it."),
            C("Automation and rising productivity", correct=True),
            C("Agglomeration economies", why="These attract industry rather than cutting jobs."),
            C("Import substitution", why="This is a strategy to build industry behind trade barriers."),
        ], steps=[S("Reason", text="Machines let fewer workers produce more, so output can grow while employment falls.")],
           concept="Causes of deindustrialization", skill="Reasoning",
           hint="How can more be made with fewer workers?"),
        MC("Which conclusion about deindustrialization is most balanced?", [
            C("It is always a sign of national economic failure", why="In rich countries it partly reflects productivity growth and the rise of services."),
            C("It has no effect on local communities", why="Job losses are often concentrated in single-industry towns."),
            C("It only happens in developing countries", why="It is best known in old industrial regions of Europe and North America."),
            C("It can reflect growth of services nationally, while imposing heavy concentrated costs on particular regions", correct=True),
        ], steps=[S("Evaluate", text="National structural change may be healthy, yet local unemployment, derelict land and out-migration are real costs.")],
           concept="Evaluating deindustrialization", skill="Reasoning",
           hint="Consider both national and local scales."),
    ]))

# ---------------------------------------------------------------------------
# Industrial, Transport & Service Geography / Newly industrialized countries
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_IND, topic="Newly industrialized countries",
    title="NIC strategies, growth and costs: practice",
    lesson="gpu1-newly-industrialized-countries",
    questions=[
        MC("Which group is usually called the first-generation NICs or 'Asian Tigers'?", [
            C("China, India, Brazil and Russia", why="These are large emerging economies, often grouped as BRICS, not the first Tigers."),
            C("Malaysia, Thailand, Indonesia and the Philippines", why="These are usually the second generation."),
            C("South Korea, Taiwan, Hong Kong and Singapore", correct=True),
            C("Japan, Germany, the USA and the UK", why="These are long-industrialized countries."),
        ], steps=[S("Recall", text="The four Tigers industrialized rapidly from the 1960s.")],
           concept="Generations of NICs", skill="Recall",
           hint="Think of the four economies that grew fastest from the 1960s."),
        MC("What is the main aim of export-oriented industrialization?", [
            C("To make goods that replace imports in the home market", why="This is import substitution."),
            C("To make manufactured goods for sale on world markets", correct=True),
            C("To protect farmers from imported food", why="This is agricultural protection, not EOI."),
            C("To reduce the number of factories", why="EOI aims to expand industry."),
        ], steps=[S("Recall", text="EOI uses low costs, incentives and export zones to sell manufactures abroad.")],
           concept="ISI and EOI", skill="Concept",
           hint="'Export-oriented' tells you where the goods go."),
        NUM("Income per head is 1 500 units and grows at 6 per cent a year for 5 years. Calculate the final value (to the nearest unit).", 2007,
            steps=[S("Formula", math=r"V_5 = 1500(1.06)^5"), S("Calculate", math=r"1.06^5 \approx 1.3382 \Rightarrow V_5 \approx 2007")],
            tolerance=2, unit="units", concept="Compound growth", skill="Calculation",
            hint="Use V = V0 × (1 + r) to the power n, with r as a decimal."),
        NUM("Using the rule of 70, estimate the doubling time of an economy growing at 2 per cent a year.", 35,
            steps=[S("Rule of 70", math=r"70 \div 2 = 35")],
            tolerance=0.1, unit="years", concept="Doubling time", skill="Calculation",
            hint="Divide 70 by the growth rate in per cent."),
        MC("What is an export processing zone?", [
            C("A port used only for crude oil exports", why="An EPZ is for manufacturing, with incentives, not a single-product port."),
            C("A protected home market behind tariffs", why="This describes import substitution."),
            C("A farming area producing export crops", why="EPZs host factories, not farms."),
            C("An area with tax breaks, duty-free imports of inputs and good infrastructure to attract export manufacturing", correct=True),
        ], steps=[S("Recall", text="EPZs offer incentives so firms, often foreign, manufacture there for export.")],
           concept="Export processing zones", skill="Recall",
           hint="Think of incentives offered to factories that export."),
        MC("Why did many NICs move from ISI to EOI?", [
            C("Small home markets limited economies of scale and protected firms stayed inefficient", correct=True),
            C("ISI caused deindustrialization immediately", why="ISI built industry at first; its limits appeared later."),
            C("EOI needed no investment", why="EOI needed large investment, often from TNCs."),
            C("World markets were closed to manufactures", why="EOI depends on open world markets."),
        ], steps=[S("Reason", text="Once the home market was supplied, growth needed the larger world market and the efficiency that competition brings.")],
           concept="Shift from ISI to EOI", skill="Reasoning",
           hint="What limits a factory that sells only at home?"),
        MC("Which is an ECONOMIC cost of rapid export-led industrialization?", [
            C("Air and water pollution", why="This is an environmental cost."),
            C("Rapid growth of urban slums", why="This is a social and urban cost."),
            C("Exposure to falls in world demand and to financial crises, as in 1997", correct=True),
            C("Loss of coastal habitats", why="This is an environmental cost."),
        ], steps=[S("Classify", text="Dependence on export markets and foreign capital makes the economy vulnerable to external shocks.")],
           concept="Costs of industrialization", skill="Concept",
           hint="Which option affects incomes and finance directly?"),
        MC("Which argument best explains why the first NICs' path is hard for African countries to repeat today?", [
            C("African countries have no raw materials", why="Many African countries are rich in raw materials."),
            C("Industrialization is impossible in the tropics", why="Singapore and Malaysia are tropical NICs."),
            C("There are no world markets for manufactures", why="World trade in manufactures is very large."),
            C("Strong competition from established Asian producers, automation, weak infrastructure and stricter trade rules", correct=True),
        ], steps=[S("Evaluate", text="Global conditions differ from the 1960s to 1980s: more competitors, automation and limits on protection; infrastructure gaps raise costs.")],
           concept="Relevance of the NIC model to Africa", skill="Reasoning",
           hint="Think about how world conditions have changed since the 1960s."),
    ]))

# ---------------------------------------------------------------------------
# Industrial, Transport & Service Geography / Transport network analysis
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_IND, topic="Transport network analysis",
    title="Network indices, accessibility and detour: practice",
    lesson="gpu1-transport-network-analysis",
    questions=[
        MC("Which is the best definition of connectivity?", [
            C("The ease with which one place can be reached from all others", why="This defines accessibility, a property of a single place."),
            C("The total length of roads in a region", why="Length is not used in topological connectivity."),
            C("The number of vehicles using a road", why="This is traffic flow."),
            C("The degree to which the vertices of a network are directly linked to one another", correct=True),
        ], steps=[S("Recall", text="Connectivity describes the whole network: how directly its places are joined.")],
           concept="Connectivity", skill="Recall",
           hint="Connectivity is about the whole network, not one place."),
        NUM("Use the figure. Count the vertices and edges and calculate the beta index (to 2 decimal places).", 1.14,
            steps=[S("Count", text="Vertices P, Q, R, S, T, U, V: v = 7. Edges PQ, QR, RS, ST, TP, QS, RU, UV: e = 8."),
                   S("Beta", math=r"\beta = \frac{8}{7} = 1.14")],
            tolerance=0.01, concept="Beta index", skill="Calculation",
            hint="Count every road between two adjacent towns as one edge.",
            diagram="algpu1-network-b.svg",
            diagram_alt="Road network of seven towns P to V: P-Q, Q-R, R-S, S-T, T-P, Q-S, R-U and U-V."),
        NUM("For the same network (v = 7, e = 8), calculate the gamma index (to 2 decimal places).", 0.53,
            steps=[S("Formula", math=r"\gamma = \frac{e}{3(v-2)}"), S("Substitute", math=r"\gamma = \frac{8}{3 \times 5} = 0.53")],
            tolerance=0.01, concept="Gamma index", skill="Calculation",
            hint="The maximum number of edges in a planar network is 3(v − 2).",
            diagram="algpu1-network-b.svg",
            diagram_alt="Road network of seven towns P to V: P-Q, Q-R, R-S, S-T, T-P, Q-S, R-U and U-V."),
        MC("For the same network, what is the cyclomatic number, and what does it mean?", [
            C("1: there is one circuit", why="μ = e − v + p = 8 − 7 + 1 = 2, not 1."),
            C("2: there are two circuits", correct=True),
            C("15: the network is complete", why="This adds e and v instead of using e − v + p."),
            C("0: the network is a tree", why="A tree would have e = v − 1 = 6 edges."),
        ], steps=[S("Calculate", math=r"\mu = e - v + p = 8 - 7 + 1 = 2"),
                  S("Check on the map", text="The loops are P-Q-S-T and Q-R-S.")],
           concept="Cyclomatic number", skill="Calculation",
           hint="Use μ = e − v + p with p = 1.",
           diagram="algpu1-network-b.svg",
           diagram_alt="Road network of seven towns P to V: P-Q, Q-R, R-S, S-T, T-P, Q-S, R-U and U-V."),
        MC("In the same network, which town has the lowest Shimbel index (is most accessible)?", [
            C("R", correct=True),
            C("Q", why="Q's total is 10: it is 3 edges from V."),
            C("P", why="P's total is 13: it is on the edge of the network."),
            C("V", why="V is at the end of a branch, with the highest total, 17."),
        ], steps=[S("Row for R", text="R to Q 1, S 1, U 1, P 2, T 2, V 2: total 9."),
                  S("Compare", text="Q 10, S 10, U 12, P 13, T 13, V 17. R has the lowest total.")],
           concept="Shimbel accessibility index", skill="Interpretation",
           hint="Add the fewest edges from each town to all others.",
           diagram="algpu1-network-b.svg",
           diagram_alt="Road network of seven towns P to V: P-Q, Q-R, R-S, S-T, T-P, Q-S, R-U and U-V."),
        NUM("A road between two towns is 63 km long; the straight-line distance is 42 km. Calculate the detour index (actual ÷ straight-line × 100).", 150,
            steps=[S("Substitute", math=r"\frac{63}{42} \times 100 = 150")],
            tolerance=0.1, concept="Detour index", skill="Calculation",
            hint="Divide the road distance by the straight-line distance."),
        MC("Which is a two-sided explanation of the influence of relief on connectivity?", [
            C("Mountains always stop roads being built", why="This is one-sided and not true: passes and tunnels exist."),
            C("Relief does not affect transport", why="Relief strongly affects the cost and direction of routes."),
            C("Highlands raise building costs and reduce links, but passes, tunnels and engineering can overcome them; lowlands allow dense direct networks", correct=True),
            C("Flat land always has more roads than highland", why="Swampy or empty lowland can have few roads; human factors also matter."),
        ], steps=[S("Balance", text="Explain how the factor lowers connectivity and how it can be overcome or can raise connectivity elsewhere.")],
           concept="Factors influencing connectivity", skill="Reasoning",
           hint="Look for the answer that shows both a negative and a positive side."),
        MC("Which is the main limitation of the beta and gamma indices?", [
            C("They cannot be calculated for road networks", why="They are designed for networks such as roads."),
            C("They ignore distance, road quality, capacity and traffic", correct=True),
            C("They need computers to calculate", why="They are simple ratios."),
            C("They only work for networks with more than 100 vertices", why="They work for small networks too."),
        ], steps=[S("Evaluate", text="Topological indices count links only; a dirt track and a highway count the same.")],
           concept="Evaluating network indices", skill="Reasoning",
           hint="What information is lost when a map becomes a graph?"),
    ]))

# ---------------------------------------------------------------------------
# Industrial, Transport & Service Geography / International trade
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_IND, topic="International trade",
    title="Comparative advantage, terms of trade and blocs: practice",
    lesson="gpu1-international-trade",
    questions=[
        MC("A country has a comparative advantage in a good when it can produce it:", [
            C("in larger quantities than any other country", why="This is closer to absolute advantage."),
            C("using more workers", why="Using more workers does not show advantage."),
            C("at a lower opportunity cost than its trading partner", correct=True),
            C("with government subsidies", why="Subsidies distort costs but do not define comparative advantage."),
        ], steps=[S("Recall", text="Comparative advantage is about what must be given up (opportunity cost), not absolute output.")],
           concept="Comparative advantage", skill="Recall",
           hint="Think of what is given up to produce the good."),
        MC("Per worker, country P makes 12 t of rice or 4 t of cloth; country Q makes 6 t of rice or 3 t of cloth. Which statement is correct?", [
            C("Q has the comparative advantage in rice", why="Q's opportunity cost of rice is 0.5 t cloth, higher than P's 0.33 t."),
            C("P has the comparative advantage in rice and Q in cloth", correct=True),
            C("P has the comparative advantage in both goods", why="A country cannot have the lower opportunity cost in both goods."),
            C("Neither can gain from trade because P is better at both", why="Gains depend on comparative, not absolute, advantage."),
        ], steps=[S("OC of 1 t rice", math=r"P: \frac{4}{12} = 0.33;\quad Q: \frac{3}{6} = 0.5\ \text{t cloth}"),
                  S("OC of 1 t cloth", math=r"P: \frac{12}{4} = 3;\quad Q: \frac{6}{3} = 2\ \text{t rice}"),
                  S("Conclude", text="P has the lower OC for rice; Q for cloth.")],
           concept="Comparative advantage calculation", skill="Calculation",
           hint="Work out the opportunity cost of each good in each country."),
        NUM("A country's export price index is 95 and its import price index is 125. Calculate the terms of trade index.", 76,
            steps=[S("Substitute", math=r"\frac{95}{125} \times 100 = 76")],
            tolerance=0.1, concept="Terms of trade", skill="Calculation",
            hint="Export price index ÷ import price index × 100."),
        MC("A terms of trade index of 76 (base year 100) means that:", [
            C("export volumes have fallen by 24 per cent", why="The index measures relative prices, not volumes."),
            C("the country has a trade surplus", why="The index says nothing directly about the balance of trade."),
            C("import prices have fallen", why="Import prices rose relative to export prices."),
            C("each unit of exports now buys fewer imports than in the base year", correct=True),
        ], steps=[S("Interpret", text="Below 100 the terms of trade have worsened: more exports are needed to pay for the same imports.")],
           concept="Interpreting terms of trade", skill="Interpretation",
           hint="Compare the index with 100."),
        NUM("A country exports goods worth 1 800 billion FCFA and imports goods worth 2 250 billion FCFA. What is its balance of trade, in billion FCFA? (Use a minus sign for a deficit.)", -450,
            steps=[S("Exports minus imports", math=r"1\,800 - 2\,250 = -450")],
            tolerance=0.5, unit="billion FCFA", concept="Balance of trade", skill="Calculation",
            hint="Balance of trade = value of visible exports − value of visible imports."),
        MC("Which of these is a customs union with a common currency that includes Cameroon?", [
            C("CEMAC", correct=True),
            C("ECOWAS", why="ECOWAS is the West African community; Cameroon is not a member."),
            C("The WTO", why="The WTO is a global rules body, not a customs union."),
            C("The European Union", why="Cameroon trades with the EU under an agreement but is not a member."),
        ], steps=[S("Recall", text="CEMAC members share a common external tariff and the CFA franc.")],
           concept="Trade blocs", skill="Recall",
           hint="Think of the Central African economic and monetary community."),
        MC("Why does tariff escalation discourage processing in cocoa-producing countries?", [
            C("It bans the export of cocoa beans", why="Escalation is about tariff levels, not bans."),
            C("Importing countries charge higher tariffs on processed products such as chocolate than on raw beans", correct=True),
            C("It lowers the world price of chocolate", why="It raises the cost of exporting processed goods, not their world price."),
            C("It removes tariffs on all products", why="That would be free trade, not escalation."),
        ], steps=[S("Reason", text="Higher tariffs on processed goods make exporting them less competitive, so producers export raw beans and value is added abroad.")],
           concept="Primary-product dependence", skill="Reasoning",
           hint="Compare the tariff on raw beans with the tariff on chocolate."),
        MC("Which is the most important obstacle to increasing trade among African countries within the AfCFTA?", [
            C("African countries have nothing to trade", why="They trade food, manufactures, fuels and services."),
            C("Tariffs cannot be reduced", why="Tariff reduction is the core of the agreement."),
            C("All African countries use the same currency", why="Africa has many currencies; this is not the obstacle described."),
            C("Weak transport links, similar primary exports and non-tariff barriers such as border delays", correct=True),
        ], steps=[S("Evaluate", text="Removing tariffs is not enough if roads, rail and border procedures make trade slow and costly, and if countries export similar goods.")],
           concept="Evaluating trade blocs", skill="Reasoning",
           hint="Think about barriers other than tariffs."),
    ]))

# ---------------------------------------------------------------------------
# Industrial, Transport & Service Geography / Tourism
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_IND, topic="Tourism",
    title="Butler's model, impacts and sustainable tourism: practice",
    lesson="gpu1-tourism",
    questions=[
        MC("Which pair correctly matches a Cameroonian tourist resource with its attraction?", [
            C("Waza National Park: viewing savanna wildlife such as elephants and giraffes", correct=True),
            C("Foumban: surfing on ocean beaches", why="Foumban is inland; its attractions are the Sultan's palace, museums and crafts."),
            C("Lobé falls: skiing", why="The Lobé falls near Kribi drop into the sea; there is no skiing in Cameroon."),
            C("Korup: desert dune trekking", why="Korup is a rainforest park in the South-West."),
        ], steps=[S("Match", text="Waza in the Far North is a savanna park visited for game viewing.")],
           concept="Tourist resources and attractions", skill="Recall",
           hint="Link each place with what tourists actually do there."),
        MC("Use the figure. Which lettered stage shows the fastest growth in tourist numbers?", [
            C("A", why="A is exploration: few visitors and slow growth."),
            C("D", why="D is consolidation: growth is slowing."),
            C("C", correct=True),
            C("E", why="E is stagnation: numbers have levelled off."),
        ], steps=[S("Read the curve", text="The steepest part of the S-curve is stage C."),
                  S("Name it", text="C is the development stage of Butler's model.")],
           concept="Butler's tourism area life cycle", skill="Interpretation",
           hint="Find the steepest part of the curve.",
           diagram="algpu1-butler-q.svg",
           diagram_alt="S-shaped curve of tourist numbers against time divided into five lettered stages A to E, with three branches after E: rejuvenation, stabilisation and decline."),
        MC("In which stage of Butler's model do local people first provide simple accommodation and services for a growing number of visitors?", [
            C("Exploration", why="In exploration there are almost no services for tourists."),
            C("Involvement", correct=True),
            C("Consolidation", why="By consolidation large, often outside-owned facilities dominate."),
            C("Decline", why="Decline is the fall in visitors after stagnation."),
        ], steps=[S("Recall", text="Involvement: local initiative, basic facilities, a tourist season begins.")],
           concept="Butler's stages", skill="Recall",
           hint="Local people become involved."),
        NUM("Visitors to a resort rose from 48 000 to 60 000 in five years. Calculate the percentage growth.", 25,
            steps=[S("Change", math=r"60\,000 - 48\,000 = 12\,000"), S("Percentage", math=r"\frac{12\,000}{48\,000} \times 100 = 25")],
            tolerance=0.1, unit="%", concept="Applying Butler to data", skill="Calculation",
            hint="Divide the change by the earlier value."),
        NUM("Tourists spend 40 billion FCFA in a country and 60 per cent leaks out. How many billion FCFA are retained?", 16,
            steps=[S("Retained share", math=r"1 - 0.60 = 0.40"), S("Amount", math=r"40 \times 0.40 = 16")],
            tolerance=0.01, unit="billion FCFA", concept="Leakage", skill="Calculation",
            hint="Retained = total × (1 − leakage share)."),
        MC("According to Doxey's irritation index, what is the final stage of residents' attitudes if tourism keeps growing?", [
            C("Euphoria", why="Euphoria is the first stage, when visitors are welcomed."),
            C("Apathy", why="Apathy is the second stage."),
            C("Annoyance", why="Annoyance comes before the final stage."),
            C("Antagonism", correct=True),
        ], steps=[S("Recall", text="Euphoria, apathy, annoyance (irritation), antagonism.")],
           concept="Doxey's irritation index", skill="Recall",
           hint="The last stage is open hostility."),
        MC("Which project best fits the definition of ecotourism?", [
            C("A 400-room beach hotel owned by a foreign chain", why="Large scale and high leakage; no conservation or community aim is stated."),
            C("A small village-run lodge near a rainforest park, with local guides and fees that fund conservation", correct=True),
            C("A new airport terminal", why="Infrastructure supports tourism but is not ecotourism."),
            C("A city conference centre", why="This is business tourism."),
        ], steps=[S("Check the criteria", text="Ecotourism is small-scale, nature-based, conserves the environment, benefits local people and educates visitors.")],
           concept="Ecotourism", skill="Application",
           hint="Check for conservation AND local benefit."),
        MC("Which is the strongest criticism of Butler's model?", [
            C("It cannot be drawn as a graph", why="It is usually drawn as an S-curve."),
            C("It ignores visitor numbers", why="Visitor numbers are its main variable."),
            C("Stages are hard to identify in advance and not all places follow the same path", correct=True),
            C("It only applies to Cameroon", why="It was developed from resorts in North America and Europe and applied widely."),
        ], steps=[S("Evaluate", text="The model describes a common pattern but cannot predict timing; management, shocks and resort type change the path.")],
           concept="Evaluating Butler's model", skill="Reasoning",
           hint="Think about prediction and variety of tourist places."),
    ]))

# ---------------------------------------------------------------------------
# Regional Development & Global Disparities / Indicators of development
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_DEV, topic="Indicators of development",
    title="Development indicators and the HDI: practice",
    lesson="gpu1-indicators-of-development",
    questions=[
        MC("Which statement best distinguishes development from economic growth?", [
            C("Growth is an increase in output; development is a wider improvement in well-being including health, education and freedom", correct=True),
            C("They mean exactly the same thing", why="Growth can occur without improvements in health, education or equality."),
            C("Development is measured only by GNI per capita", why="GNI measures output and income, not the whole of well-being."),
            C("Growth refers only to population increase", why="Economic growth is about output, not population."),
        ], steps=[S("Recall", text="Growth = more goods and services; development = better lives in a wider sense.")],
           concept="Growth and development", skill="Concept",
           hint="One is about output, the other about people's lives."),
        MC("What does purchasing power parity (PPP) adjust GNI per capita for?", [
            C("Population growth", why="Dividing by population gives per capita; PPP is about prices."),
            C("Inflation over time only", why="PPP compares price levels between countries at the same time."),
            C("Differences in the cost of living between countries", correct=True),
            C("Income inequality within a country", why="Inequality is measured by the Gini coefficient or the IHDI."),
        ], steps=[S("Recall", text="PPP converts incomes so that each unit buys the same basket of goods in every country.")],
           concept="PPP", skill="Recall",
           hint="Think about what money can buy in different countries."),
        NUM("Life expectancy is 68 years. Using goalposts of 20 and 85, calculate the health index (to 3 decimal places).", 0.738,
            steps=[S("Formula", math=r"\frac{68 - 20}{85 - 20}"), S("Calculate", math=r"\frac{48}{65} = 0.738")],
            tolerance=0.001, concept="Dimension index", skill="Calculation",
            hint="(actual − minimum) ÷ (maximum − minimum)."),
        NUM("Expected years of schooling are 14 (maximum 18) and mean years of schooling are 9 (maximum 15). Calculate the education index (to 3 decimal places).", 0.689,
            steps=[S("Schooling indices", math=r"\frac{14}{18} = 0.778;\quad \frac{9}{15} = 0.600"),
                   S("Average", math=r"\frac{0.778 + 0.600}{2} = 0.689")],
            tolerance=0.002, concept="Education index", skill="Calculation",
            hint="Find each schooling index, then take their average."),
        MC("A country has a health index of 0.8, an education index of 0.6 and an income index of 0.5. What is its HDI?", [
            C("0.633", why="This is the arithmetic mean; the HDI uses the geometric mean."),
            C("0.240", why="This is the product before taking the cube root."),
            C("1.900", why="This adds the indices."),
            C("0.621", correct=True),
        ], steps=[S("Product", math=r"0.8 \times 0.6 \times 0.5 = 0.24"), S("Cube root", math=r"\sqrt[3]{0.24} = 0.621")],
           concept="Calculating the HDI", skill="Calculation",
           hint="Multiply the three indices and take the cube root."),
        MC("Why does the HDI use the logarithm of income?", [
            C("Because income data are always too large to handle", why="The reason is economic, not about the size of numbers."),
            C("Because an extra unit of income adds more to well-being for a poor person than for a rich one", correct=True),
            C("To make rich countries score higher", why="The log actually reduces the advantage of very high incomes."),
            C("Because income cannot be measured in PPP", why="The HDI uses GNI per capita at PPP."),
        ], steps=[S("Reason", text="Diminishing returns: each extra unit of income matters less as income rises, which a log scale captures.")],
           concept="Income index", skill="Reasoning",
           hint="Think of diminishing returns to income."),
        MC("Two countries have the same HDI, but country A's figure hides large gaps between its capital region and rural regions. Which measure would best reveal this?", [
            C("GNI per capita at PPP", why="This is another national average."),
            C("The birth rate", why="This measures one demographic aspect, not inequality."),
            C("Life expectancy at birth", why="A national average hides regional gaps."),
            C("Regional HDI values or the inequality-adjusted HDI", correct=True),
        ], steps=[S("Reason", text="Inequality is hidden by national averages; regional data or the IHDI expose it.")],
           concept="Limits of indicators", skill="Application",
           hint="What do national averages hide?"),
        MC("An oil-exporting country has a high GNI per capita but low life expectancy and literacy. What is the best conclusion?", [
            C("Its development is fully shown by its GNI", why="The social indicators contradict the income figure."),
            C("Income is unevenly shared or not converted into health and education, so a composite measure gives a truer picture", correct=True),
            C("Its life expectancy data must be wrong", why="There is no reason to reject the data; contradictions are common."),
            C("Oil exports always reduce life expectancy", why="This is an unsupported generalisation."),
        ], steps=[S("Interpret", text="High average income with weak social indicators suggests inequality or weak public services: use several indicators together.")],
           concept="Interpreting contradictory indicators", skill="Reasoning",
           hint="What could stop high income from improving health?"),
    ]))

# ---------------------------------------------------------------------------
# Regional Development & Global Disparities / Models of development
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_DEV, topic="Models of development",
    title="Rostow, Myrdal and Friedmann: practice",
    lesson="gpu1-models-of-development",
    questions=[
        MC("In Rostow's model, which stage follows the preconditions for take-off?", [
            C("Drive to maturity", why="Drive to maturity follows take-off."),
            C("Traditional society", why="Traditional society is the first stage."),
            C("High mass consumption", why="This is the final stage."),
            C("Take-off", correct=True),
        ], steps=[S("Recall the order", text="Traditional society, preconditions, take-off, drive to maturity, high mass consumption.")],
           concept="Rostow's stages", skill="Recall",
           hint="The stage is named in the question itself."),
        MC("Which is the main argument of dependency theorists against Rostow?", [
            C("Poorer countries are not at an early stage; their links with rich countries have kept them as raw-material suppliers", correct=True),
            C("Rostow's model has too many stages", why="The criticism is about cause, not the number of stages."),
            C("Rich countries never passed through stages", why="Dependency theory does not deny the history of rich countries."),
            C("Development depends only on population size", why="This is not the dependency argument."),
        ], steps=[S("Recall", text="Dependency theory sees underdevelopment as produced by unequal relations in the world economy, not as an original state.")],
           concept="Dependency critique", skill="Concept",
           hint="Think about colonial and trade relationships."),
        MC("Which sequence shows cumulative causation in a growing core?", [
            C("Industry closes, jobs fall, people leave, services decline", why="This is a downward spiral, as in a declining periphery."),
            C("Population rises, food runs short, famine reduces population", why="This is a Malthusian sequence."),
            C("New industry, more jobs and income, bigger market and taxes, better services, more firms attracted", correct=True),
            C("Farmers adopt HYVs, yields rise, prices fall", why="This is about the Green Revolution, not regional growth."),
        ], steps=[S("Recall", text="Myrdal's upward spiral: each gain attracts further growth in the same place.")],
           concept="Cumulative causation", skill="Concept",
           hint="Look for a self-reinforcing upward chain."),
        MC("Which is a SPREAD effect of growth in a core city?", [
            C("Young people migrate from villages to the city", why="Outflow of labour is a backwash effect."),
            C("City demand raises prices for farmers' vegetables in surrounding regions", correct=True),
            C("Rural savings are deposited in city banks and lent to city firms", why="Outflow of capital is a backwash effect."),
            C("City factories out-compete rural craft workshops", why="Competition that harms the periphery is a backwash effect."),
        ], steps=[S("Classify", text="Spread effects benefit the periphery: demand for its products and diffusion of technology and ideas.")],
           concept="Backwash and spread effects", skill="Application",
           hint="Which option helps the periphery?"),
        MC("According to Myrdal, what usually happens to regional inequality if market forces are left alone?", [
            C("It disappears quickly", why="Myrdal argued the opposite."),
            C("It stays exactly the same", why="He argued that cumulative causation changes it."),
            C("It narrows because spread effects are always stronger", why="Myrdal thought backwash usually outweighs spread."),
            C("It widens because backwash effects usually outweigh spread effects", correct=True),
        ], steps=[S("Recall", text="Myrdal: without government intervention, backwash dominates, so the gap between core and periphery grows.")],
           concept="Myrdal on regional inequality", skill="Recall",
           hint="Which effect did Myrdal think was usually stronger?"),
        MC("A country has secondary cities growing alongside the capital, linked by improving roads, but large poor rural areas remain. Which Friedmann stage does this best match?", [
            C("Stage 1, pre-industrial", why="Stage 1 has no dominant cores at all."),
            C("Stage 3, sub-cores emerge", correct=True),
            C("Stage 4, integrated system", why="Large poor peripheries remain, so integration is incomplete."),
            C("Stage 2, single strong core", why="Secondary cores are already growing."),
        ], steps=[S("Match", text="Growing secondary cores with a remaining periphery describe stage 3.")],
           concept="Friedmann's stages", skill="Interpretation",
           hint="Count the growth centres and check the periphery."),
        MC("How does Hirschman's view differ from Myrdal's?", [
            C("Hirschman denied that growth concentrates in cores", why="Hirschman accepted polarisation in early stages."),
            C("Hirschman studied only farming", why="He wrote about economic development generally."),
            C("Hirschman was more optimistic that trickle-down would eventually reduce regional gaps", correct=True),
            C("Hirschman argued for five linear stages", why="That is Rostow."),
        ], steps=[S("Compare", text="Both describe polarisation; Hirschman expected trickle-down (spread) to win over time, Myrdal expected backwash to dominate.")],
           concept="Comparing development models", skill="Reasoning",
           hint="Who expected the gap to close in the end?"),
        MC("Which is the strongest general criticism of Friedmann's core-periphery model for low-income countries today?", [
            C("It is descriptive, underplays global forces and the move to later stages is not automatic", correct=True),
            C("It does not include any cores", why="Cores are central to the model."),
            C("It only applies to agriculture", why="It concerns the whole space economy."),
            C("It was written after 2000", why="It dates from 1966."),
        ], steps=[S("Evaluate", text="The model describes patterns well but does not explain how to reach integration; commodity prices and foreign investment also shape the map.")],
           concept="Evaluating Friedmann", skill="Reasoning",
           hint="Think about prediction and outside influences."),
    ]))

# ---------------------------------------------------------------------------
# Regional Development & Global Disparities / Regional development strategies
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_DEV, topic="Regional development strategies",
    title="Growth poles, bottom-up development and measuring inequality: practice",
    lesson="gpu1-regional-development-strategies",
    questions=[
        MC("Which is the best definition of a growth pole?", [
            C("A small community project chosen by villagers", why="This describes bottom-up development."),
            C("A dynamic industry or group of linked industries in a chosen centre, intended to stimulate growth in the surrounding region", correct=True),
            C("A city that loses population to the capital", why="This describes backwash in a periphery."),
            C("A boundary between two regions", why="A growth pole is a centre of growth, not a boundary."),
        ], steps=[S("Recall", text="Perroux's growth pole: a propulsive industry whose linkages and multipliers spread growth.")],
           concept="Growth poles", skill="Recall",
           hint="Think of a driving industry placed in a chosen centre."),
        MC("Which project is the clearest example of bottom-up development?", [
            C("A national hydroelectric dam", why="This is a large, centrally planned top-down project."),
            C("A new capital city", why="This is top-down."),
            C("A deep-sea port with an industrial zone", why="This is top-down."),
            C("A village water committee that builds and maintains a gravity-fed water supply with help from an NGO", correct=True),
        ], steps=[S("Classify", text="Bottom-up projects are small, local, low-cost and community-led.")],
           concept="Bottom-up development", skill="Application",
           hint="Who plans and runs the project?"),
        NUM("Regional incomes per head (thousand FCFA) are 800, 500, 350, 250 and 100. Calculate the ratio of the richest to the poorest region.", 8,
            steps=[S("Divide", math=r"800 \div 100 = 8")],
            tolerance=0.01, concept="Measuring regional inequality", skill="Calculation",
            hint="Divide the highest value by the lowest."),
        NUM("A set of regional incomes has a mean of 450 and a population standard deviation of 180. Calculate the coefficient of variation.", 40,
            steps=[S("Formula", math=r"CV = \frac{\sigma}{\bar{x}} \times 100"), S("Substitute", math=r"\frac{180}{450} \times 100 = 40")],
            tolerance=0.1, unit="%", concept="Coefficient of variation", skill="Calculation",
            hint="Divide the standard deviation by the mean and multiply by 100."),
        MC("A regional CV falls from 48.6% to 32.5% over ten years. What does this show?", [
            C("Regional inequality has narrowed relative to the average", correct=True),
            C("Every region has become richer", why="The CV measures spread, not whether each region gained."),
            C("The average income has fallen", why="The CV says nothing directly about the level of the mean."),
            C("Inequality has widened", why="A lower CV means less relative spread."),
        ], steps=[S("Interpret", text="The CV measures relative spread; a fall means regions have moved closer together.")],
           concept="Interpreting the CV", skill="Interpretation",
           hint="Does a smaller CV mean more or less spread?"),
        MC("Why have some growth poles become 'enclaves' with little effect on their regions?", [
            C("They employed too many local workers", why="Enclaves typically employ few local workers."),
            C("They were too small to matter", why="Enclaves are often large projects."),
            C("Capital-intensive plants bought inputs from outside and sent profits away, creating few local linkages", correct=True),
            C("They were planned by local communities", why="Growth poles are top-down; community planning is bottom-up."),
        ], steps=[S("Reason", text="Spread effects need local linkages; without them jobs, purchases and profits leak away.")],
           concept="Evaluating growth poles", skill="Reasoning",
           hint="What does a growth pole need to spread growth?"),
        MC("What does decentralisation mean in regional development?", [
            C("Moving all industry to the capital", why="That is centralisation of industry."),
            C("Transferring powers and resources from central government to regional and local authorities", correct=True),
            C("Removing all government from development", why="Decentralisation moves government closer to people; it does not remove it."),
            C("Building a new capital city", why="A new capital is a top-down project, not a transfer of powers."),
        ], steps=[S("Recall", text="Decision-making and money are moved closer to the people affected, as with Cameroon's regional councils.")],
           concept="Decentralisation", skill="Concept",
           hint="Think about where decisions are made."),
        MC("Which conclusion about regional development strategies is best supported by evidence?", [
            C("Top-down projects always fail", why="Infrastructure such as ports, dams and roads can bring real benefits."),
            C("Bottom-up projects can change national patterns quickly on their own", why="They are small and slow; national patterns need large investment too."),
            C("Regional inequality disappears without government action", why="Myrdal's model and evidence suggest gaps often widen without action."),
            C("Combining large infrastructure with local participation and real decentralisation usually works best", correct=True),
        ], steps=[S("Synthesise", text="Top-down gives scale; bottom-up gives local fit and ownership; each covers the other's weakness.")],
           concept="Evaluating regional strategies", skill="Reasoning",
           hint="Think about the weaknesses of each approach on its own."),
    ]))
