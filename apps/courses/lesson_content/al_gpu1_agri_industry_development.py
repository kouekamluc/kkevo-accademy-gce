"""A Level Geography (0750), Upper Sixth: Agricultural Geography; Industrial, Transport & Service Geography;
Regional Development & Global Disparities (KKEVO draft, for reviewer checking against the syllabus and textbooks)."""

from .dsl import *  # noqa: F403

COURSE = ("geography", "upper-sixth")

M_AGR = "Agricultural Geography"
M_IND = "Industrial, Transport & Service Geography"
M_DEV = "Regional Development & Global Disparities"

LESSONS = []

# ---------------------------------------------------------------------------
# Agricultural Geography / Factors influencing farming
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_AGR, topic="Factors influencing farming",
    title="Physical, economic and behavioural factors in farming decisions",
    slug="gpu1-factors-influencing-farming",
    minutes=24,
    summary="Why farmers do what they do: physical limits and optimum ranges, economic factors such as markets, capital and land tenure, and behavioural factors such as perception, risk and satisficing, with expected-value and gross-margin reasoning.",
    objectives=[
        "Explain how physical factors set the limits and optimum conditions for crops and animals",
        "Explain the influence of economic and political factors on farm decisions",
        "Use expected value, maximin and gross margin to analyse a farmer's choice under risk",
        "Evaluate how far farming is determined by the environment or by human decisions",
    ],
    key_concepts=["Physical factors", "Economic factors", "Behavioural factors", "Optimum and marginal conditions",
                  "Land tenure", "Risk and uncertainty", "Satisficer", "Gross margin"],
    blocks=[
        H("Introduction"),
        T("Two farmers in the Western Highlands of Cameroon may have the same soil and the same rainfall, yet one grows "
          "Irish potatoes and cabbages for the Douala market while the other grows maize, beans and cocoyams mainly for the family. "
          "The environment is the same; the decisions are different.\n\n"
          "At O Level you listed factors that influence farming. At A Level you must explain **how** each factor works, show that "
          "factors interact, and judge which matter most in a given place. This lesson gives you a framework for every later "
          "lesson in this module."),
        D("A **farming decision** is the choice of what to produce, how much land, labour and capital to use, and how to sell the "
          "output. Geographers group the influences on these choices into three sets: **physical**, **economic** (with political) "
          "and **behavioural** factors.", title="Definition: the three sets of factors"),
        IMG("algpu1-farm-decision.svg",
            alt="Systems diagram: physical, economic and behavioural factors point to the farmer, who perceives and decides; the decision shapes the farm system, which gives outputs; a dashed feedback arrow returns from outputs to the farmer",
            caption="Figure 1. The farm as a decision-making system. Factors act through the farmer's perception, and results feed back into later decisions."),
        H("Physical factors: limits and optimum conditions"),
        T("Physical factors are climate (temperature, rainfall, length of the growing season, sunshine), soil (depth, texture, "
          "fertility, drainage), relief (altitude, slope, aspect) and water supply. They rarely decide exactly what is grown. "
          "Instead they set **limits**: outside a certain range a crop cannot be grown at a profit."),
        D("For each crop there is an **optimum** zone where physical conditions give the highest yield for the lowest cost, "
          "a **marginal** zone where it can be grown but yields are low or risky, and an **absolute limit** beyond which it fails. "
          "Arabica coffee, for example, prefers cooler highland conditions than robusta coffee.", title="Optimum, marginal and absolute limits"),
        T("Altitude changes temperature. Air temperature falls with height, on average by about 6.5 degrees Celsius for every 1 000 m "
          "(the environmental lapse rate you met in Lower Sixth). This is one reason why the highlands of the West and North-West "
          "grow temperate vegetables and arabica coffee, while the coastal lowlands grow bananas, oil palm and rubber."),
        EX("Worked example 1: altitude and temperature", intro="A lowland station at sea level has a mean temperature of 26 degrees Celsius "
           "(an invented teaching figure). Estimate the mean temperature at a farm at 1 500 m, using a lapse rate of 6.5 degrees per 1 000 m. "
           "Then say what this suggests for farming.", steps=[
            S("Height difference in thousands of metres", math=r"1500 \div 1000 = 1.5"),
            S("Temperature fall", math=r"1.5 \times 6.5 = 9.75\ {}^\circ\text{C}"),
            S("Estimated temperature", math=r"26 - 9.75 = 16.25\ {}^\circ\text{C}"),
            S("Interpret", text="About 16 degrees Celsius is too cool for oil palm, which is a lowland crop, but suits arabica coffee, "
              "potatoes and many vegetables. Altitude has moved the farm into a different optimum zone."),
        ]),
        H("Economic and political factors"),
        KEY("Economic and political factors", "Each works by changing costs, prices or security.", cards=[
            ["Market", "Distance to the market, its size and the prices paid. Perishable crops need a near market or good transport."],
            ["Transport", "Good roads lower the cost of moving inputs and outputs and widen the market."],
            ["Capital", "Money for seeds, fertiliser, machines and irrigation. Lack of capital and credit keeps many farms small and low-input."],
            ["Labour", "Its amount, cost and skill. Rural-urban migration of young people can leave farms short of labour."],
            ["Land tenure", "Who owns or controls land, and how securely. A farmer with secure rights is more likely to invest in trees, terraces or wells."],
            ["Government", "Subsidies, prices, credit schemes, extension services, research and trade rules."],
        ]),
        D("**Land tenure** is the system of rights by which land is held: customary (community) ownership, private title, tenancy "
          "or share-cropping, or state ownership. Insecure tenure discourages long-term investment.", title="Definition: land tenure"),
        T("One useful measure is the **gross margin**: the value of the output minus the variable costs (seed, fertiliser, hired "
          "labour, transport). Comparing gross margins per hectare shows which enterprise pays best on a given farm."),
        EX("Worked example 2: gross margin", intro="A farmer harvests 2.5 tonnes of maize from one hectare and sells it at FCFA 180 000 "
           "a tonne. Seed, fertiliser, hired labour and transport cost FCFA 210 000. Find the gross margin per hectare (invented figures).", steps=[
            S("Value of output", math=r"2.5 \times 180\,000 = 450\,000\ \text{FCFA}"),
            S("Subtract variable costs", math=r"450\,000 - 210\,000 = 240\,000\ \text{FCFA}"),
            S("Conclusion", text="The gross margin is FCFA 240 000 per hectare. If the road to market is cut and transport costs rise, the margin "
              "falls even though the physical conditions are unchanged."),
        ]),
        H("Behavioural factors: perception, risk and satisficing"),
        T("Economic models assume an **optimiser**: a farmer with perfect knowledge who always chooses the most profitable option. "
          "Real farmers have limited information, limited capital and good reasons to fear a bad year. The behavioural approach "
          "studies how they actually decide."),
        D("A **satisficer** is a decision-maker who chooses an option that is good enough and safe enough rather than the one that "
          "would give the highest possible profit. The idea of bounded rationality behind it is usually credited to Herbert Simon; "
          "geographers such as Julian Wolpert applied it to farmers.", title="Definition: satisficer"),
        T("Behavioural factors include age, education and experience, attitude to risk, family needs, custom and religion, and "
          "membership of a cooperative. A farmer who feeds a family from the farm will often protect food supply first and seek profit second."),
        EX("Worked example 3: deciding under risk", intro="A farmer in the Far North can plant maize or sorghum. In a wet year (probability 0.6) maize "
           "earns FCFA 1 200 000 and sorghum FCFA 700 000 per hectare. In a dry year (probability 0.4) maize earns FCFA 200 000 and sorghum "
           "FCFA 500 000 (invented figures). Which crop does an optimiser choose, and which does a cautious farmer choose?", steps=[
            S("Expected value of maize", math=r"0.6 \times 1\,200\,000 + 0.4 \times 200\,000 = 800\,000"),
            S("Expected value of sorghum", math=r"0.6 \times 700\,000 + 0.4 \times 500\,000 = 620\,000"),
            S("Optimiser", text="Maize has the higher expected value, so an optimiser plants maize."),
            S("Cautious farmer (maximin)", text="Compare the worst cases: maize 200 000 and sorghum 500 000. A cautious farmer maximises the minimum and plants sorghum. "
              "This is why drought-tolerant sorghum and millet remain important in dry, risky areas even where maize pays more on average."),
        ]),
        H("Evaluation: which factors matter most?"),
        T("No single set of factors explains farming. Physical factors are strongest at the margins: in deserts, high mountains or "
          "flood-prone valleys they decide what is possible. Economic factors dominate in commercial farming near cities and ports. "
          "Behavioural factors matter most where farmers are poor and the risk of a bad year is high. Technology such as irrigation, "
          "greenhouses and new seeds pushes back physical limits, but at a cost that only some farmers can pay."),
        TIP("In Paper 2 essays on farming, use the three sets of factors as your structure, show how they interact (for example, "
            "irrigation is a capital answer to a physical limit), and end with a judgement for a named area. In Paper 1 multiple choice, "
            "expect questions on definitions such as satisficer, land tenure and marginal land. Paper 3 questions on the geography of "
            "Cameroon may ask how the physical environment influences farming patterns.", title="Exam link"),
        MISTAKE("Listing factors without explaining how they work", "The examiners' report criticises bare lists. For each factor, say "
                "what it changes (cost, yield, risk, price) and give a place. Saying 'soil' earns little; saying 'deep volcanic soils on the "
                "slopes of Mount Cameroon hold water and nutrients, which supports bananas and tea' earns credit."),
        MISTAKE("Treating physical factors as deciding everything", "That is environmental determinism. Show that the same environment "
                "supports different systems depending on markets, capital, tenure and the farmer's choices."),
        QUIZ("A farmer chooses a crop that gives a reliable family food supply rather than the crop with the highest average profit. "
             "Which idea best describes this behaviour?",
             ["Optimiser behaviour", "Satisficing behaviour", "Environmental determinism", "Economies of scale"], 1,
             "A satisficer accepts a good-enough, safer option instead of the most profitable one.",
             hint="Is the farmer aiming for the maximum profit?",
             feedback=["An optimiser would choose the highest expected profit.", "",
                       "Determinism says the environment decides; here the farmer is choosing.",
                       "Economies of scale are about lower average costs at larger output."]),
        QUIZ("Why does insecure land tenure discourage farmers from planting tree crops such as cocoa?",
             ["Tree crops need flat land", "Tree crops take years to yield, so the farmer may lose the land before the investment pays",
              "Tree crops cannot be sold", "Land tenure only affects pastoral farmers"], 1,
             "Tree crops are long-term investments, and only secure rights make them worthwhile.",
             hint="Think about how long a cocoa tree takes to yield.",
             feedback=["Cocoa grows on slopes too; tenure, not relief, is the issue here.", "",
                       "Cocoa is a major cash crop.", "Tenure affects every kind of farm."]),
        PQ("Using a lapse rate of 6.5 degrees Celsius per 1 000 m, estimate how much cooler a farm at 2 000 m is than one at 400 m, "
           "and state one effect on farming.",
           "Height difference 1 600 m, so the fall is 1.6 × 6.5 = 10.4 degrees Celsius. The higher farm lies in a cooler zone suited to "
           "temperate vegetables, potatoes or arabica coffee; lowland crops such as oil palm would be marginal or impossible there."),
        PQ("Explain why farmers in dry, risky areas often grow crops with lower average returns.",
           "Model answer points: rainfall is unreliable, so a high-return crop such as maize can fail in a dry year; poor farmers cannot "
           "survive one total failure, so they reduce risk; drought-tolerant crops such as sorghum and millet give a smaller but more "
           "reliable harvest; this is satisficing or maximin behaviour; mixed cropping and staggered planting spread risk further. "
           "Evaluation: insurance, irrigation or credit would let farmers take more risk."),
        PQ("'Physical factors are the most important influence on farming.' Discuss. (Give a model essay plan.)",
           "Plan. Introduction: define the three sets of factors and the idea of limits. Paragraph 1: physical factors set absolute limits "
           "(rainfall in the Sahel, altitude in highlands, flooding in valleys), with examples. Paragraph 2: within those limits, "
           "economic factors decide what is grown (market distance, transport, capital, prices, government policy), e.g. market "
           "gardening near Yaounde. Paragraph 3: behavioural factors (perception, risk, custom, tenure) explain why neighbours with the "
           "same land farm differently. Paragraph 4: technology (irrigation, greenhouses, fertiliser) reduces physical control but costs "
           "money. Conclusion: physical factors matter most at the margins and in poor, low-input systems; economic and behavioural "
           "factors matter most elsewhere, so the statement is only partly true."),
        SUM("Farm decisions are shaped by **physical**, **economic and political**, and **behavioural** factors acting through the farmer's perception.",
            "Physical factors set **optimum, marginal and absolute limits**; altitude lowers temperature by about 6.5 degrees per 1 000 m.",
            "Markets, transport, capital, labour, **land tenure** and government change costs, prices and security; **gross margin** compares enterprises.",
            "Real farmers are often **satisficers** who reduce risk; expected value versus maximin shows why.",
            "Judge the balance of factors for a named place rather than listing them."),
    ],
))

# ---------------------------------------------------------------------------
# Agricultural Geography / Farming systems
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_AGR, topic="Farming systems",
    title="Classifying farming systems: intensity, Ruthenberg's R and the move to permanent cultivation",
    slug="gpu1-farming-systems",
    minutes=24,
    summary="How geographers classify farming systems by intensity, purpose and enterprise, how to measure intensity with yields, labour inputs and Ruthenberg's cultivation index R, and why fallow systems intensify as population grows.",
    objectives=[
        "Classify farming systems by intensity, purpose (subsistence or commercial) and enterprise (arable, pastoral, mixed)",
        "Measure the intensity of a system with input and output ratios and Ruthenberg's R value",
        "Explain the sequence from shifting cultivation through bush fallow to permanent cultivation",
        "Evaluate the advantages and problems of intensive and extensive systems",
    ],
    key_concepts=["Farming system", "Intensive and extensive farming", "Subsistence and commercial farming",
                  "Shifting cultivation", "Bush fallow", "Ruthenberg's R value", "Pastoral nomadism and transhumance", "Plantation agriculture"],
    blocks=[
        H("Introduction"),
        T("In the forest of the East Region a family may clear a plot, crop it for two years and leave it to the bush for ten. Near Bafoussam "
          "the same field may be cropped every year with manure and fertiliser. On the Adamawa plateau herders move cattle between wet-season "
          "and dry-season pastures. These are different **farming systems**.\n\n"
          "This lesson gives you the tools to classify any system precisely and to measure how intensive it is."),
        D("A **farming system** is a farm or group of similar farms seen as a whole: its inputs (land, labour, capital, knowledge), its processes "
          "(ploughing, planting, herding) and its outputs (crops, animals, income), together with the way they are organised.", title="Definition: farming system"),
        H("Three ways to classify"),
        KEY("Classification criteria", "A full description uses all three.", cards=[
            ["Intensity", "Intensive: high inputs of labour or capital per hectare and high output per hectare. Extensive: low inputs and output per hectare, usually over a large area."],
            ["Purpose", "Subsistence: produce mainly for the family. Commercial: produce mainly for sale. Many African farms are semi-commercial."],
            ["Enterprise", "Arable (crops), pastoral (animals) or mixed (both, with links such as manure and fodder)."],
        ]),
        T("So a smallholding near Bamenda growing vegetables for sale with much family labour is **intensive, commercial, arable**; "
          "a cattle ranch is **extensive, commercial, pastoral**; and a forest plot of cassava and plantain for home use is **extensive, "
          "subsistence, arable**. Intensity can be labour-intensive (many workers per hectare, as in wet-rice farming) or capital-intensive "
          "(machines, chemicals and greenhouses with few workers)."),
        H("Measuring intensity"),
        T("Geographers use ratios. **Inputs per hectare**: workers per hectare, fertiliser per hectare, capital per hectare. "
          "**Outputs per hectare**: yield (tonnes per hectare) or value per hectare. **Output per worker** shows labour productivity, "
          "which is often low in labour-intensive systems even when yield per hectare is high."),
        EX("Worked example 1: comparing two farms", intro="Farm P: 2 hectares, 8 workers, 9 tonnes of produce. Farm Q: 400 hectares, 4 workers, "
           "600 tonnes (invented figures). Compare their intensity and labour productivity.", steps=[
            S("Workers per hectare", math=r"P: 8 \div 2 = 4;\quad Q: 4 \div 400 = 0.01"),
            S("Yield per hectare", math=r"P: 9 \div 2 = 4.5\ \text{t/ha};\quad Q: 600 \div 400 = 1.5\ \text{t/ha}"),
            S("Output per worker", math=r"P: 9 \div 8 = 1.125\ \text{t};\quad Q: 600 \div 4 = 150\ \text{t}"),
            S("Interpret", text="P is labour-intensive with a high yield per hectare but low output per worker. Q is extensive and mechanised: "
              "low yield per hectare but very high output per worker."),
        ]),
        H("Ruthenberg's R value: from shifting cultivation to permanent cropping"),
        T("For tropical crop systems with fallow, the agricultural economist Hans Ruthenberg used a simple index of how often land is cultivated."),
        F(r"R = \frac{\text{years of cultivation}}{\text{years of cultivation} + \text{years of fallow}} \times 100", title="Ruthenberg's cultivation index"),
        KEY("Interpreting R", "Thresholds as usually given (check your textbook).", cards=[
            ["R below 33", "Shifting cultivation: short cropping, long fallow; the plot is often abandoned and the farmer moves on."],
            ["R from 33 to 66", "Fallow systems (bush fallow, rotational bush fallow): the farmer stays in one village and rotates plots."],
            ["R above 66", "Permanent cultivation: land is cropped almost every year, so fertility must be kept up with manure, fertiliser or rotation."],
        ]),
        EX("Worked example 2: calculating R", intro="Village A crops a plot for 2 years then leaves it fallow for 10. Village B crops for 3 years and "
           "rests for 3. Village C crops for 4 years and rests for 1. Classify each system.", steps=[
            S("Village A", math=r"R = \frac{2}{2+10} \times 100 = 16.7 \Rightarrow \text{shifting cultivation}"),
            S("Village B", math=r"R = \frac{3}{3+3} \times 100 = 50 \Rightarrow \text{fallow system}"),
            S("Village C", math=r"R = \frac{4}{4+1} \times 100 = 80 \Rightarrow \text{permanent cultivation}"),
        ]),
        T("Why does R rise over time? As population density rises, there is not enough land to leave plots fallow for long. The fallow "
          "shortens, R rises, and farmers must find other ways to keep fertility: composting, manure, legumes, ridging, terracing or fertiliser. "
          "This is the argument of Ester Boserup, whom you met in Lower Sixth population theories: population pressure drives agricultural "
          "intensification. If fallow shortens without these new methods, yields fall and soils degrade."),
        H("Major systems in brief"),
        KEY("Systems you should be able to describe", "Give location, inputs, outputs and problems.", cards=[
            ["Shifting cultivation", "Forest clearing by slash and burn, mixed cropping, long fallow; sustainable at low density, it breaks down when fallow shortens."],
            ["Bush fallow", "Permanent village, rotating plots with shorter fallow; widespread in the forest and savanna zones."],
            ["Pastoral nomadism and transhumance", "Herders move with animals to find grass and water. Transhumance is seasonal movement between fixed pastures, as on the Adamawa plateau and in the North."],
            ["Plantation agriculture", "Large estates growing one cash crop (monoculture) such as banana, oil palm, rubber or tea, with hired labour and processing on site; examples in the South-West and Littoral."],
            ["Intensive market gardening", "Small plots, high inputs, perishable vegetables for nearby urban markets."],
        ]),
        H("Evaluation"),
        T("Intensive systems feed more people from less land, but may cause soil exhaustion, water pollution from chemicals, or heavy debt for "
          "inputs. Extensive systems need few inputs and can suit poor soils or dry land, but they need a lot of land per person and fail when "
          "population grows. No system is 'best'; each fits a combination of environment, population density, capital and markets."),
        TIP("Paper 2 questions on systems often ask you to explain the characteristics of a system or why it is changing. Define the system with "
            "all three criteria, give a located example, and use evidence such as an R value or yields. In Paper 1, expect questions that "
            "ask you to classify a described farm or to interpret a ratio.", title="Exam link"),
        MISTAKE("Equating subsistence with extensive", "Many subsistence farms are labour-intensive (high input of family labour per hectare). "
                "Intensity and purpose are separate criteria."),
        MISTAKE("Using 'intensive' to mean 'large'", "Intensity is about inputs and outputs per hectare, not farm size. A large ranch is extensive; "
                "a tiny vegetable plot can be very intensive."),
        QUIZ("A plot is cropped for 3 years and rested for 9. What is its R value, and which system is it?",
             ["25; shifting cultivation", "33; fallow system", "75; permanent cultivation", "300; permanent cultivation"], 0,
             "R = 3/(3+9) × 100 = 25, which is below 33: shifting cultivation.",
             hint="Divide cultivation years by the whole cycle.",
             feedback=["", "33 would need 3 years cropped in a 9-year cycle; here the cycle is 12 years.",
                       "75 is fallow divided by the whole cycle, not cultivation.", "This divides 9 by 3; R uses cultivation over the whole cycle."]),
        QUIZ("Which farm is capital-intensive?",
             ["A rice paddy worked by ten family members per hectare", "A greenhouse vegetable farm with irrigation, fertiliser and few workers",
              "A cattle ranch of 5 000 hectares with 6 workers", "A forest plot cleared by slash and burn"], 1,
             "High spending on equipment, water and chemicals per hectare with little labour is capital-intensive.",
             hint="Look for high spending per hectare on machines and inputs.",
             feedback=["This is labour-intensive.", "", "This is extensive.", "This is extensive, low-input farming."]),
        PQ("A village crops land for 2 years in every 8-year cycle. Calculate R and explain what will happen to R and to soil fertility if the "
           "population doubles without new farming methods.",
           "R = 2/8 × 100 = 25 (shifting cultivation). If population doubles, more land is needed, so fallow shortens and R rises (for example to 50). "
           "Without manure, legumes or fertiliser, the soil has less time to recover, nutrients are not replaced, yields fall and erosion increases."),
        PQ("Distinguish between pastoral nomadism and transhumance.",
           "Nomadism: herders and their families move with no permanent base, following grass and water. Transhumance: seasonal movement of animals "
           "(often with only some herders) between fixed pastures, for example from highland to lowland or to river valleys in the dry season, "
           "returning to a permanent settlement."),
        PQ("Examine the advantages and problems of plantation agriculture in tropical countries. (Model plan.)",
           "Advantages: export earnings, wage employment, infrastructure (roads, housing, clinics), processing and research, high yields from "
           "scale and management. Problems: monoculture risks pests and price falls, large land areas taken from local users, foreign or state "
           "control of profits, low wages and seasonal work, soil and forest loss. Evaluation: benefits depend on who owns the estate, how "
           "workers are treated and whether smallholders are linked in as outgrowers."),
        SUM("Classify any farming system by **intensity**, **purpose** and **enterprise**.",
            "Intensity is measured per hectare (inputs and yield); labour productivity is output per worker.",
            "**Ruthenberg's R** = cultivation years ÷ whole cycle × 100: below 33 shifting, 33 to 66 fallow, above 66 permanent.",
            "Rising population shortens fallow and drives **intensification** (Boserup), or degradation if methods do not change.",
            "Each system fits its environment, population density, capital and market; evaluate rather than rank."),
    ],
))

# ---------------------------------------------------------------------------
# Agricultural Geography / Von Thünen's model
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_AGR, topic="Von Thünen's model",
    title="Von Thünen's model: locational rent, ring boundaries, modifications and relevance today",
    slug="gpu1-von-thunen-model",
    minutes=25,
    summary="The A Level treatment of Von Thünen: the locational rent equation, why the rent line slopes, how to calculate the margin of cultivation and ring boundaries, the effect of a navigable river or second market, and a balanced evaluation including Sinclair's reversal.",
    objectives=[
        "Use the locational rent equation to calculate rent, the margin of cultivation and ring boundaries",
        "Explain why high-yield, high-freight products occupy the inner rings",
        "Explain how a navigable river, a second market or a change in price modifies the rings",
        "Evaluate the model, including its relevance to urban fringes and African cities",
    ],
    key_concepts=["Locational (economic) rent", "Rent gradient", "Margin of cultivation", "Intensity of land use",
                  "Isolated state", "Modified model", "Sinclair's model"],
    blocks=[
        H("Introduction"),
        T("At O Level you learned the rings: market gardening and dairying near the town, then forestry, crops and ranching. The 2023 examiners' "
          "report notes that many candidates could not recognise a question about why distant farmers farm more extensively as a question on "
          "Von Thünen's model. At A Level you need the **reasoning** behind the rings, and you need to apply it to real patterns, for example "
          "around Yaounde, Douala or Garoua."),
        D("Johann Heinrich von Thünen (1826), in *The Isolated State*, modelled land use around a single market town on a uniform plain with "
          "farmers who maximise profit and pay transport costs that rise in proportion to distance.", title="The model in one sentence"),
        H("Locational rent"),
        D("**Locational rent** (economic rent) is the net return from a hectare of land after the costs of production and transport are paid. "
          "It is the most a farmer could afford to pay for that land and still break even.", title="Definition: locational rent"),
        F(r"R = Y(p - c) - Yfd", title="The locational rent equation"),
        T("Here $R$ is the rent per hectare, $Y$ the yield in tonnes per hectare, $p$ the market price per tonne, $c$ the production cost per tonne, "
          "$f$ the freight (transport) rate per tonne per kilometre and $d$ the distance to the market in kilometres."),
        T("The equation is a straight line. Its **intercept** $Y(p - c)$ is the rent at the market itself. Its **slope** is $-Yf$: rent falls by $Yf$ "
          "for every extra kilometre. A product with a high yield per hectare and a high freight rate (bulky or perishable goods such as vegetables "
          "and milk) has a steep rent gradient. A product with low yield and cheap transport (cattle that walk, or grain that keeps) has a gentle gradient."),
        D("The **margin of cultivation** is the distance at which rent falls to zero; beyond it the product makes a loss. Set $R = 0$:", title="Margin of cultivation",
          formula=r"d_{\max} = \frac{p - c}{f}"),
        IMG("algpu1-thunen-rent.svg",
            alt="Rent against distance: vegetables fall from 800 thousand to zero at 16 km, maize from 400 thousand to zero at 40 km, cattle from 160 thousand to zero at 80 km. Vegetables and maize cross at A (10 km); maize and cattle cross at B (30 km).",
            caption="Figure 1. Rent lines for three products (invented values). At each distance the land goes to the highest line, so ring boundaries are where lines cross (A and B)."),
        EX("Worked example 1: building the rent lines", intro="Use these invented data. Vegetables: Y = 20 t/ha, p − c = FCFA 40 000 per tonne, f = FCFA 2 500 per tonne-km. "
           "Maize: Y = 5, p − c = 80 000, f = 2 000. Cattle (beef): Y = 0.4, p − c = 400 000, f = 5 000. Write each rent line and find each margin of cultivation.", steps=[
            S("Vegetables", math=r"R = 20(40\,000) - 20(2\,500)d = 800\,000 - 50\,000d"),
            S("Maize", math=r"R = 5(80\,000) - 5(2\,000)d = 400\,000 - 10\,000d"),
            S("Cattle", math=r"R = 0.4(400\,000) - 0.4(5\,000)d = 160\,000 - 2\,000d"),
            S("Margins", math=r"d_{veg} = \frac{40\,000}{2\,500} = 16;\ d_{maize} = \frac{80\,000}{2\,000} = 40;\ d_{cattle} = \frac{400\,000}{5\,000} = 80\ \text{km}"),
        ]),
        EX("Worked example 2: ring boundaries", intro="Using the lines from example 1, find where vegetables give way to maize, and maize to cattle.", steps=[
            S("Vegetables = maize", math=r"800\,000 - 50\,000d = 400\,000 - 10\,000d \Rightarrow 40\,000d = 400\,000 \Rightarrow d = 10"),
            S("Maize = cattle", math=r"400\,000 - 10\,000d = 160\,000 - 2\,000d \Rightarrow 8\,000d = 240\,000 \Rightarrow d = 30"),
            S("Rings", text="Vegetables 0 to 10 km, maize 10 to 30 km, cattle 30 to 80 km, then no farming. Note that vegetables could be grown up to "
              "16 km, but beyond 10 km maize outbids them for the land: a ring ends where a competitor pays more, not where the product stops paying."),
        ], check=r"R_{veg}(10) = R_{maize}(10) = 300\,000;\ R_{maize}(30) = R_{cattle}(30) = 100\,000"),
        H("Intensity of land use"),
        T("Von Thünen also showed that the **same** crop is farmed more intensively near the market. Where rent is high, it pays to use more "
          "labour, fertiliser and capital on each hectare to raise yield. Far out, land is cheap and inputs are spread thinly. This is why the "
          "examiners expect you to explain that a distant farmer adopts a more extensive system: transport costs eat into the return, rent is low, "
          "and extra inputs do not pay."),
        H("Modifying the model"),
        KEY("What happens when an assumption is relaxed", "Each change can be reasoned from the rent equation.", cards=[
            ["A navigable river or good road", "Freight rate f is lower along it, so rent lines are gentler there and the rings stretch out along the route into elongated bands."],
            ["A second, smaller market", "A small set of rings forms around it, overlapping and distorting the main rings."],
            ["Higher market price", "p rises, so the intercept and the margin rise: the ring expands outwards."],
            ["Better transport technology", "f falls for all products, the rings widen, and perishables can travel further (refrigerated lorries, air freight)."],
            ["Variable soil or relief", "Yield Y and cost c vary, so rings break up into patches."],
        ]),
        EX("Worked example 3: effect of a better road", intro="A new tarred road halves the freight rate for maize to FCFA 1 000 per tonne-km. Using the data above, "
           "find the new margin of cultivation for maize and say what happens to the maize ring.", steps=[
            S("New margin", math=r"d_{\max} = \frac{80\,000}{1\,000} = 80\ \text{km}"),
            S("New maize line", math=r"R = 400\,000 - 5\,000d"),
            S("New boundary with cattle", math=r"400\,000 - 5\,000d = 160\,000 - 2\,000d \Rightarrow 3\,000d = 240\,000 \Rightarrow d = 80"),
            S("Interpret", text="Maize now outbids cattle all the way to 80 km, where both rents reach zero together, so the cattle ring is squeezed out "
              "along this road: cheaper transport lets more intensive land use spread outwards."),
        ]),
        H("Evaluation"),
        T("**Strengths.** The model isolates one variable, distance, and shows clearly how transport costs and rent shape land use and intensity. "
          "Its logic of bid rent was later used in urban land-use theory. Rough ring patterns can still be seen: intensive vegetable gardens and "
          "poultry on the edges of Yaounde and Douala, and more extensive food-crop farming and grazing further out (check local studies)."),
        T("**Limitations.** The assumptions rarely hold: there are many markets, transport follows roads, relief and soils vary, governments "
          "fix prices or subsidise, and farmers are not all profit-maximisers (the behavioural factors of the first lesson). Modern transport has "
          "reduced the friction of distance, so in many places land use now depends more on physical conditions and policy than on distance."),
        T("**Sinclair's reversal.** Robert Sinclair (1967) argued that at the edge of growing cities in developed countries the pattern is "
          "inverted: farmland nearest the city is used *less* intensively, because farmers expect to sell to urban developers soon and do not "
          "invest. Studies around some African cities also found a ring of firewood or charcoal production close to the city (check your textbook "
          "for the case study it uses). These show that the model is a tool for comparison, not a description."),
        TIP("In Paper 2, a question on why distant farmers farm extensively, or on land use around a market, is a Von Thünen question: name the model, "
            "draw the rent lines or rings, and explain with rent, transport cost and intensity. Paper 1 often tests the effect of a river or price "
            "change, and the margin of cultivation.", title="Exam link"),
        MISTAKE("Not naming the model", "The examiners' report says many candidates did not recognise a Von Thünen question. If the question is about "
                "distance from a market and intensity, say so and use the model's terms."),
        MISTAKE("Treating the margin of cultivation as the ring boundary", "A ring ends where another product pays a higher rent. Find boundaries by "
                "setting two rent equations equal, not by setting one to zero."),
        QUIZ("In the rent equation R = Y(p − c) − Yfd, what decides how steeply rent falls with distance?",
             ["p − c only", "The product Yf", "The distance d", "The intercept Y(p − c)"], 1,
             "The slope of the line is −Yf: high yield per hectare and high freight rate give a steep gradient.",
             hint="Look at the term that is multiplied by d.",
             feedback=["p − c sets the intercept and margin, not the slope.", "", "d is the variable on the axis, not the slope.",
                       "The intercept is the rent at the market, not its rate of fall."]),
        QUIZ("A navigable river runs from the market through the area. How are the rings changed?",
             ["They become smaller circles", "They stretch out into bands along the river", "They disappear", "They reverse order"], 1,
             "Cheaper transport along the river lowers f there, so each use extends further along it.",
             hint="What does the river do to the freight rate?",
             feedback=["Cheaper transport widens, not shrinks, the rings.", "", "The rings still form, but distorted.",
                       "The order is the same; only the shape changes."]),
        PQ("For a crop with p − c = FCFA 60 000 per tonne and f = FCFA 1 500 per tonne-km, find the margin of cultivation. Does the yield affect it?",
           "d max = 60 000 ÷ 1 500 = 40 km. Yield does not affect the margin, because Y cancels when R = 0; yield affects the intercept and slope, "
           "and so which crop wins the competition for land, but not where this crop stops paying."),
        PQ("Product X: R = 600 000 − 40 000d. Product Y: R = 300 000 − 10 000d. Find the ring boundary and which product occupies the inner ring.",
           "Set equal: 600 000 − 40 000d = 300 000 − 10 000d, so 30 000d = 300 000 and d = 10 km. X has the higher rent nearer the market "
           "(at 0 km, 600 000 against 300 000), so X occupies 0 to 10 km and Y from 10 km to its margin at 30 km."),
        PQ("Assess the relevance of Von Thünen's model to agricultural land use in tropical Africa today. (Model plan.)",
           "Introduction: outline the model and its assumptions. Relevance: distance still matters where roads are poor and transport is costly, "
           "so perishable vegetables, milk and poultry concentrate near cities such as Yaounde and Douala, and intensity falls outwards; fuelwood "
           "and charcoal rings around cities. Limits: several markets and road corridors distort rings; relief, soils and rainfall dominate in many "
           "regions; customary tenure and subsistence goals mean many farmers are not profit-maximisers; export crops respond to ports and world "
           "prices. Conclusion: useful as a benchmark for the urban fringe and where transport is poor; weak as a description at regional scale."),
        SUM("**Locational rent** R = Y(p − c) − Yfd: intercept Y(p − c), slope −Yf.",
            "**Margin of cultivation** d = (p − c)/f; **ring boundaries** are where two rent lines are equal.",
            "High-yield, high-freight products have steep gradients and take the inner rings; intensity falls with distance.",
            "Rivers, roads, extra markets and price changes **modify** the rings in predictable ways.",
            "Evaluate: useful benchmark, but many assumptions fail; Sinclair found the pattern inverted at the urban fringe."),
    ],
))

# ---------------------------------------------------------------------------
# Agricultural Geography / The Green Revolution and agrarian reform
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_AGR, topic="The Green Revolution and agrarian reform",
    title="The Green Revolution and agrarian reform: technology, land and who benefits",
    slug="gpu1-green-revolution-agrarian-reform",
    minutes=25,
    summary="What the Green Revolution package was, why it raised yields in Asia and Latin America but less in Africa, how to judge its gains and costs with yield and cost data, and the main types of agrarian reform with their aims and limits.",
    objectives=[
        "Describe the Green Revolution package and where it was most successful",
        "Calculate and interpret yield changes, cost per tonne and gross margins for traditional and high-yielding varieties",
        "Explain the types and aims of agrarian and land reform",
        "Evaluate the social, economic and environmental effects of both approaches",
    ],
    key_concepts=["Green Revolution", "High-yielding varieties (HYVs)", "Package of inputs", "Agrarian reform",
                  "Land redistribution", "Land consolidation", "Land registration", "Social polarisation"],
    blocks=[
        H("Introduction"),
        T("There are two broad ways to raise farm output. One is to change the **technology** of farming: new seeds, fertiliser and water. "
          "The other is to change the **institutions**: who owns land, how it is divided and how farmers get credit and markets. "
          "The Green Revolution is the best-known example of the first; agrarian reform is the name for the second. A strong A Level answer "
          "shows that each works best when combined with the other."),
        D("The **Green Revolution** is the spread, from the 1960s, of **high-yielding varieties (HYVs)** of wheat, rice and maize together "
          "with chemical fertiliser, pesticides and controlled irrigation, which greatly raised yields per hectare in parts of Asia and Latin "
          "America.", title="Definition: Green Revolution"),
        H("The package and where it worked"),
        T("Plant breeders produced short-stemmed (semi-dwarf) varieties that could take heavy doses of fertiliser without falling over, matured "
          "faster and were less sensitive to day length. Norman Borlaug's wheat work in Mexico and the rice variety IR8, released by the "
          "International Rice Research Institute in the Philippines in 1966, are the standard examples. Faster maturing allowed **double "
          "cropping**: two harvests a year on irrigated land."),
        KEY("Why it is called a package", "The seeds alone are not enough.", cards=[
            ["Seed", "HYVs bought each season (hybrids do not breed true)."],
            ["Water", "Reliable irrigation from canals or tube wells."],
            ["Chemicals", "Fertiliser to feed the high yield; pesticides because uniform crops attract pests."],
            ["Support", "Credit, extension advice, roads, storage and guaranteed prices."],
        ]),
        T("The package succeeded most where irrigation, credit and roads already existed, as in Punjab in north-west India. In much of "
          "sub-Saharan Africa the impact was smaller: most farming is rain-fed, the staple crops (cassava, sorghum, millet, yams, plantain) "
          "received less research at first, soils and rainfall vary greatly, and roads and credit were weak. Newer efforts aim to adapt "
          "the approach to African crops and smallholders."),
        H("Measuring gains and costs"),
        EX("Worked example 1: yield change", intro="On an irrigated rice scheme, yields rise from 1.6 t/ha with a traditional variety to 4.0 t/ha with an "
           "HYV (invented figures). Calculate the percentage increase.", steps=[
            S("Change", math=r"4.0 - 1.6 = 2.4\ \text{t/ha}"),
            S("Percentage", math=r"\frac{2.4}{1.6} \times 100 = 150\%"),
            S("Interpret", text="Yield has risen by 150 per cent, so the same land feeds two and a half times as many people, if the extra rice reaches them."),
        ]),
        EX("Worked example 2: cost per tonne and risk", intro="The traditional crop costs FCFA 160 000 per hectare to grow and the HYV package costs FCFA 480 000. "
           "Rice sells at FCFA 200 000 a tonne. Compare cost per tonne and gross margin, then repeat for a bad year when both yields halve.", steps=[
            S("Cost per tonne", math=r"\text{traditional: } \frac{160\,000}{1.6} = 100\,000;\quad \text{HYV: } \frac{480\,000}{4.0} = 120\,000"),
            S("Gross margin, normal year", math=r"\text{traditional: } 1.6(200\,000) - 160\,000 = 160\,000;\quad \text{HYV: } 4.0(200\,000) - 480\,000 = 320\,000"),
            S("Gross margin, bad year", math=r"\text{traditional: } 0.8(200\,000) - 160\,000 = 0;\quad \text{HYV: } 2.0(200\,000) - 480\,000 = -80\,000"),
            S("Interpret", text="In a normal year the HYV doubles the margin. In a bad year the traditional farmer breaks even but the HYV farmer loses "
              "FCFA 80 000 a hectare and may fall into debt. The package raises returns and raises risk; poor farmers without credit or insurance may avoid it."),
        ]),
        H("Effects: an evaluation"),
        KEY("Gains and costs of the Green Revolution", "Use both sides in an essay.", cards=[
            ["Economic gains", "Higher yields and output; India moved from food imports towards self-sufficiency in grain; cheaper food for towns."],
            ["Social costs", "Richer farmers with land, water and credit adopted first and gained most; some small tenants were pushed off land; inequality between regions grew (polarisation)."],
            ["Environmental costs", "Falling water tables from tube wells, salinisation and waterlogging, pesticide poisoning, fewer crop varieties (genetic erosion)."],
            ["Dependence", "Farmers must buy seed and chemicals every season, often from large firms, and are exposed to input price rises."],
        ]),
        H("Agrarian reform"),
        D("**Agrarian reform** is a broad change in the way agriculture is organised, including land ownership, tenancy, credit, marketing and "
          "services. **Land reform** is the narrower part that changes the ownership or distribution of land.", title="Definition: agrarian and land reform"),
        KEY("Main types of reform", "Each tackles a different problem.", cards=[
            ["Redistribution", "Large estates broken up and land given to landless or small farmers. Aim: equity and incentive to invest."],
            ["Consolidation", "Scattered small plots of one farmer combined into one holding. Aim: less time walking between plots, easier mechanisation."],
            ["Tenancy reform", "Rent ceilings and security for tenants and share-croppers. Aim: tenants keep more of the gain from improvements."],
            ["Registration and titling", "Written titles to land. Aim: security, and land can be used as collateral for credit."],
            ["Cooperatives and collectives", "Farmers pool land, machines or marketing. Aim: economies of scale and bargaining power."],
        ]),
        T("Kenya's land consolidation and registration from the 1950s is often used as a case study. In Cameroon, state land, national land and "
          "private land were defined in land tenure laws of 1974, and land registration through a land certificate exists, although much rural land is "
          "still held under customary tenure (check your textbook for the current details). State-supported schemes have also reorganised "
          "farming, for example irrigated rice under SEMRY in the Far North and UNVDA in the Ndop plain."),
        T("**Evaluation of reform.** Reform is political: large owners resist, and compensation is costly. Redistribution without credit, seed, "
          "roads and advice can lower output in the short term because new owners lack capital. Titling can help investment but can also let "
          "wealthier people buy out the poor, and it may ignore women's and customary rights. Reform works best combined with technical support: "
          "this is why a 'Green Revolution' on unreformed land often widened inequality, while reform without technology often failed to raise output."),
        TIP("Paper 2 may ask you to assess the impact of the Green Revolution or the aims and problems of land reform; give a located example and "
            "both sides. Paper 1 tests the parts of the package and the types of reform. In Paper 3 on the geography of Cameroon, irrigated rice "
            "schemes and land tenure are useful examples for questions on agricultural development.", title="Exam link"),
        MISTAKE("Saying the Green Revolution 'solved hunger'", "Output rose, but hunger is also about access and income (see the next lesson). "
                "Use measured language: it raised yields where the package could be supplied, with uneven social effects."),
        MISTAKE("Confusing agrarian reform with land reform", "Land reform changes ownership or distribution of land; agrarian reform is wider and "
                "includes credit, marketing, tenancy and services."),
        QUIZ("Why did the Green Revolution have less effect in much of sub-Saharan Africa than in Asia?",
             ["Africa has no rice or maize farming", "Most farming is rain-fed, staple crops were less researched, and roads and credit were weak",
              "African farmers refused all new seeds", "Fertiliser was banned"], 1,
             "The package needed irrigation, credit and infrastructure, and early research focused on wheat and rice.",
             hint="What did the package need in order to work?",
             feedback=["Rice and maize are grown widely in Africa.", "",
                       "This is an unsupported generalisation; adoption depended on cost, risk and support.", "There was no such ban."]),
        QUIZ("A farmer's six small plots, scattered around a village, are exchanged for one block of the same total area. What type of reform is this?",
             ["Redistribution", "Tenancy reform", "Consolidation", "Collectivisation"], 2,
             "Combining scattered plots of the same owner into one holding is consolidation.",
             hint="The owner and the total area stay the same.",
             feedback=["Redistribution moves land between owners.", "Tenancy reform changes rents and security for tenants.", "",
                       "Collectivisation pools land among many farmers."]),
        PQ("Maize yields rise from 1.4 t/ha to 3.5 t/ha with hybrid seed and fertiliser. Calculate the percentage increase and give two reasons why some farmers may still not adopt the package.",
           "Increase 2.1 t/ha; 2.1 ÷ 1.4 × 100 = 150 per cent. Reasons: high cost of seed and fertiliser each season and lack of credit; greater "
           "loss in a drought year (risk); lack of irrigation, roads or advice; hybrid seed must be bought every year."),
        PQ("Explain two ways in which the Green Revolution increased inequality in rural areas.",
           "First, farmers with more land, water and credit could afford the package first and gained most, buying out or renting land from poorer "
           "neighbours. Second, regions with irrigation (such as Punjab) grew faster than dry regions, widening regional gaps. Mechanisation also "
           "reduced demand for landless labourers in some areas."),
        PQ("'Agrarian reform is more important than new technology for rural development.' Discuss. (Model plan.)",
           "Introduction: define both. For reform: secure tenure and fair distribution give incentives to invest and spread benefits; without it, "
           "technology gains go to the already rich (Green Revolution polarisation). For technology: yields per hectare must rise to feed a growing "
           "population, and redistribution alone does not raise output (new owners need inputs). Examples: Kenya consolidation and titling; Punjab; "
           "irrigated rice schemes in Cameroon. Conclusion: complementary; the best results come where secure, fair access to land is combined with "
           "affordable technology, credit and markets."),
        SUM("The **Green Revolution** combined HYVs with fertiliser, pesticides, irrigation and credit; it raised yields most in irrigated Asia and Latin America.",
            "HYVs can raise yield and gross margin but also **cost per tonne and risk**; a bad year hurts high-input farmers most.",
            "Effects were uneven: output gains, but social polarisation, water and soil problems and dependence on bought inputs.",
            "**Agrarian reform** (redistribution, consolidation, tenancy reform, titling, cooperatives) changes the institutions of farming.",
            "Technology and reform work best together; judge effects for a named place."),
    ],
))

# ---------------------------------------------------------------------------
# Agricultural Geography / Food security
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_AGR, topic="Food security",
    title="Food security: the four pillars, causes of insecurity and strategies",
    slug="gpu1-food-security",
    minutes=24,
    summary="Food security defined through availability, access, utilisation and stability; why hunger is often about access rather than supply (Sen); how to calculate food needs and self-sufficiency ratios; and an evaluation of strategies from storage to food aid.",
    objectives=[
        "Define food security and explain its four pillars",
        "Calculate household energy needs and a national self-sufficiency ratio",
        "Explain the physical, economic and political causes of food insecurity, including the entitlement approach",
        "Evaluate strategies to improve food security at household, national and global scales",
    ],
    key_concepts=["Food security", "Availability", "Access", "Utilisation", "Stability", "Self-sufficiency ratio",
                  "Entitlement approach", "Post-harvest losses", "Food aid"],
    blocks=[
        H("Introduction"),
        T("The world produces enough food to give everyone more energy than they need, yet many people are undernourished. Within Cameroon "
          "markets in Douala and Yaounde are full of food, while some households in the Far North go hungry in the lean season before the harvest. "
          "This shows that food security is not only about how much food is grown. This lesson brings together the farming ideas of the module."),
        D("**Food security** exists when all people, at all times, can obtain enough safe and nutritious food to meet their needs for an active and "
          "healthy life. This is the sense used by the Food and Agriculture Organization (FAO) since the World Food Summit of 1996.", title="Definition: food security"),
        IMG("algpu1-food-pillars.svg",
            alt="Four pillars under a roof labelled food security: availability (production, stocks, imports), access (income, prices, markets and roads), utilisation (diet, clean water, health, food safety) and stability (no shocks such as drought, conflict or price spikes)",
            caption="Figure 1. The four pillars of food security. If any one is weak, people can be food insecure."),
        KEY("The four pillars", "Use them to structure any answer.", cards=[
            ["Availability", "Is there enough food in the area? Production, stocks, imports and food aid."],
            ["Access", "Can people get it? Income, prices, distance to markets, roads, and social rights to food."],
            ["Utilisation", "Can the body use it? Balanced diet, clean water, sanitation, health, cooking and food safety."],
            ["Stability", "Do the other three hold over time? Seasons, droughts, floods, conflict and price spikes cause instability."],
        ]),
        D("**Undernourishment** is too little dietary energy. **Malnutrition** is any imbalance, including lack of protein and micronutrients "
          "(such as iron or vitamin A) and also overweight. **Famine** is a severe, widespread shortage causing large-scale hunger and deaths.", title="Related terms"),
        H("Measuring needs and supply"),
        T("Planners often use about 2 100 kilocalories per person per day as an average energy requirement. A kilogram of maize grain provides "
          "roughly 3 600 kilocalories (check the figure your textbook uses)."),
        EX("Worked example 1: household needs", intro="A household of 6 people relies on maize for its energy. Using 2 100 kcal per person per day and 3 600 kcal per kg, "
           "how much maize does it need for 30 days?", steps=[
            S("Daily energy need", math=r"6 \times 2\,100 = 12\,600\ \text{kcal}"),
            S("Maize per day", math=r"12\,600 \div 3\,600 = 3.5\ \text{kg}"),
            S("Maize for 30 days", math=r"3.5 \times 30 = 105\ \text{kg}"),
            S("Interpret", text="If the family harvests 1 000 kg but loses 20 per cent in storage, it keeps 800 kg: about 7.6 months of food. "
              "The rest of the year must be bought, so access (income and prices) becomes the problem."),
        ]),
        F(r"\text{SSR} = \frac{\text{production}}{\text{production} + \text{imports} - \text{exports}} \times 100", title="Self-sufficiency ratio (SSR)"),
        EX("Worked example 2: self-sufficiency ratio", intro="A country produces 800 000 t of a cereal, imports 300 000 t and exports 100 000 t (invented figures). Calculate the SSR.", steps=[
            S("Domestic supply", math=r"800\,000 + 300\,000 - 100\,000 = 1\,000\,000\ \text{t}"),
            S("Ratio", math=r"\frac{800\,000}{1\,000\,000} \times 100 = 80\%"),
            S("Interpret", text="The country grows 80 per cent of the cereal it uses and depends on imports for the rest, so it is exposed to world price "
              "rises. A ratio above 100 means a surplus for export. Many countries import rice and wheat even when they are self-sufficient in roots and tubers."),
        ]),
        H("Causes of food insecurity"),
        KEY("Causes grouped by pillar", "Show that causes interact.", cards=[
            ["Availability", "Drought, floods, pests (locusts, armyworm), soil degradation, low inputs, post-harvest losses in poor storage."],
            ["Access", "Poverty, unemployment, high prices, poor roads, isolated villages, loss of land or livestock."],
            ["Utilisation", "Unsafe water, diarrhoeal disease, poor knowledge of nutrition, lack of fuel for cooking."],
            ["Stability", "Conflict and displacement, price shocks on world markets, climate variability, seasonal lean periods."],
        ]),
        T("The economist Amartya Sen argued in 1981 that famines often happen without a fall in total food supply. People starve when they lose "
          "their **entitlement** to food: their wages fall, their crops fail, or food prices rise faster than their incomes. This **entitlement "
          "approach** shifts attention from availability to access, and it is a strong evaluation point against a purely Malthusian explanation "
          "of hunger."),
        H("Strategies and their evaluation"),
        KEY("Strategies at different scales", "Always give a limit.", cards=[
            ["Raise production", "Better seed, fertiliser, irrigation, conservation farming. Limit: cost and risk for poor farmers (previous lesson)."],
            ["Cut post-harvest losses", "Hermetic bags, improved granaries, drying, processing. Cheap and effective, but needs training and small loans."],
            ["Improve access", "Rural roads, market information by mobile phone, jobs, cash transfers. Limit: needs funding and good targeting."],
            ["Stabilise supply", "Grain reserves, early warning systems, crop insurance, diversification. Limit: storage costs and price management are hard."],
            ["Food aid", "Saves lives in emergencies. Limit: if prolonged or badly timed it can lower local prices, discourage local farmers and create dependence."],
        ]),
        T("A good evaluation compares **short-term relief** (food aid, cash) with **long-term development** (roads, storage, tenure, irrigation, "
          "education), and shows that the best mix depends on which pillar is weakest in the place studied."),
        TIP("Food security fits Paper 2 questions on agriculture and on development issues. Use the four pillars as a frame, give causes and "
            "solutions linked to specific problems (the examiners' report asks for solutions tied to the problems identified), and refer to a named "
            "area. Paper 1 may test the pillars, the SSR or Sen's idea.", title="Exam link"),
        MISTAKE("Treating food security as food production only", "Production is only the availability pillar. Explain access, utilisation and stability too."),
        MISTAKE("Listing solutions without matching them to causes", "The report criticises answers that give measures without the problems, or problems "
                "without the measures. Pair each measure with the cause it removes."),
        QUIZ("A region harvests a good crop, but many poor households go hungry because food prices doubled while wages stayed the same. Which pillar has failed?",
             ["Availability", "Access", "Utilisation", "None: this is food security"], 1,
             "Food is present, but people cannot afford it: access has failed. This is Sen's entitlement idea.",
             hint="Is the food there? Can people get it?",
             feedback=["The harvest was good, so food is available.", "",
                       "Utilisation is about the body's use of food: diet, water and health.", "Hungry households are food insecure."]),
        QUIZ("A country produces 450 000 t of rice, imports 250 000 t and exports 50 000 t. What is its SSR for rice?",
             ["About 64%", "About 69%", "About 90%", "About 180%"], 1,
             "SSR = 450 000 ÷ (450 000 + 250 000 − 50 000) × 100 = 450 000 ÷ 650 000 × 100 ≈ 69%.",
             hint="Domestic supply = production + imports − exports.",
             feedback=["This divides 450 000 by 700 000, forgetting to subtract exports.", "",
                       "This ignores imports.", "This divides production by imports."]),
        PQ("A household of 5 needs 2 100 kcal per person per day. Using 3 600 kcal per kg of maize, how many kilograms of maize does it need for 90 days?",
           "Daily need 5 × 2 100 = 10 500 kcal; 10 500 ÷ 3 600 ≈ 2.92 kg per day; × 90 ≈ 262.5 kg (about 263 kg)."),
        PQ("Explain why famines can occur when total food supply in a country has not fallen.",
           "Following Sen's entitlement approach: hunger depends on whether people can command food. If incomes fall (crop failure for one group, "
           "loss of livestock, unemployment), or prices rise through hoarding, speculation or market disruption, the poor lose access even when "
           "the national supply is enough. Conflict can also block movement of food to particular areas."),
        PQ("Assess the role of food aid in improving food security. (Model plan.)",
           "Introduction: define food security and food aid (emergency, programme, project). For: saves lives in droughts, floods and conflict; "
           "food-for-work can build roads and terraces; nutrition support for children. Against: if late or prolonged it can depress local prices "
           "and discourage farmers; dependence; distribution problems and diversion; it treats symptoms not causes. Alternatives: cash transfers, "
           "local purchase, storage and early warning. Conclusion: essential for short-term stability and access in emergencies, but long-term "
           "food security needs development of availability and access."),
        SUM("**Food security** means reliable access for all to enough safe, nutritious food; it rests on **availability, access, utilisation and stability**.",
            "Household needs can be calculated from about 2 100 kcal per person per day; the **SSR** compares production with domestic supply.",
            "Causes include drought, pests, poverty, high prices, disease, conflict and post-harvest losses.",
            "**Sen's entitlement approach**: famines often come from loss of access, not lack of food.",
            "Match each strategy to the weak pillar; weigh short-term relief against long-term development."),
    ],
))

# ---------------------------------------------------------------------------
# Industrial, Transport & Service Geography / Industrial location theories
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_IND, topic="Industrial location theories",
    title="Industrial location theories: Weber's least cost, Smith's spatial margins and Lösch's market areas",
    slug="gpu1-industrial-location-theories",
    minutes=25,
    summary="Weber's least-cost theory with tonne-kilometre calculations, the material index and labour deviation by isodapanes; Smith's spatial margins to profitability; Lösch's profit-maximising market areas; and behavioural views, with a balanced evaluation.",
    objectives=[
        "Calculate the least-transport-cost location with tonne-kilometres and the material index",
        "Explain labour and agglomeration deviations using isodapanes and the critical isodapane",
        "Explain Smith's spatial margins to profitability and Lösch's market-area approach",
        "Evaluate the location theories against real industrial patterns",
    ],
    key_concepts=["Least-cost location", "Material index", "Weight-losing and pure materials", "Tonne-kilometre",
                  "Isodapane", "Critical isodapane", "Spatial margins to profitability", "Profit-maximising location"],
    blocks=[
        H("Introduction"),
        T("Why is the Cimencam cement works at Figuil in the North, close to limestone, while breweries and soap factories cluster in "
          "Douala, close to the port and the largest market? Industrial location theories try to explain such choices. At O Level you met "
          "Weber's triangle in outline. At A Level you must calculate with it, explain how factories deviate from the least-transport-cost point, "
          "and compare Weber with later theories."),
        D("**Industrial location theory** explains where firms place factories in order to minimise costs (least-cost theories) or maximise "
          "profit (profit-maximising theories), given the positions of raw materials, labour and markets.", title="Definition"),
        H("Weber's least-cost theory (1909)"),
        T("Alfred Weber assumed one product, fixed sites for raw materials and the market, transport costs proportional to weight and distance, "
          "labour available at fixed places at fixed wages, and firms that seek the lowest total cost. Transport cost is the main force."),
        D("**Localised** materials are found only at certain places. A **pure** material keeps its weight in the product (water in drinks at some "
          "sites); a **weight-losing** (gross) material loses weight in processing (ores, limestone, sugar cane). **Ubiquitous** materials such as "
          "air are found everywhere and do not pull location.", title="Types of material"),
        F(r"\text{Material index (MI)} = \frac{\text{weight of localised materials}}{\text{weight of finished product}}", title="Weber's material index"),
        T("If MI is greater than 1 the industry is weight-losing and is pulled towards its materials; if MI is about 1 (pure materials) it is "
          "footloose with respect to materials and often goes to the market; if the product gains weight (for example with water added) "
          "it locates at the market."),
        IMG("algpu1-weber-triangle.svg",
            alt="Location triangle: M1 (material A, 2 t needed per t of product), M2 (material B, 1.5 t) and market K. Road distances M1 to M2 60 km, M1 to K 60 km, M2 to K 40 km. Point P inside is 30 km from M1, 40 from M2 and 50 from K.",
            caption="Figure 1. A Weber location problem with four candidate sites (invented road distances)."),
        EX("Worked example 1: tonne-kilometres", intro="Each tonne of product needs 2 t of material A from M1 and 1.5 t of material B from M2, and 1 t of product goes "
           "to market K. Use Figure 1 to find the total tonne-kilometres for a factory at M1, M2, K and P.", steps=[
            S("At M1", math=r"2(0) + 1.5(60) + 1(60) = 150\ \text{t-km}"),
            S("At M2", math=r"2(60) + 1.5(0) + 1(40) = 160\ \text{t-km}"),
            S("At K", math=r"2(60) + 1.5(40) + 1(0) = 180\ \text{t-km}"),
            S("At P", math=r"2(30) + 1.5(40) + 1(50) = 170\ \text{t-km}"),
            S("Decide", text="M1 has the lowest total (150 t-km). The heaviest weight-losing material pulls the factory to its source. MI = 3.5 ÷ 1 = 3.5, which confirms a material orientation."),
        ]),
        H("Deviations: labour and agglomeration"),
        D("An **isodapane** is a line joining places of equal **extra** transport cost compared with the least-transport-cost point. The "
          "**critical isodapane** is the isodapane whose extra cost equals the saving offered elsewhere (for example on labour). If a cheap-labour "
          "site lies inside the critical isodapane, the factory moves there.", title="Isodapanes"),
        EX("Worked example 2: labour deviation", intro="Transport costs FCFA 500 per tonne-km. A town L with cheap, skilled labour lies at a site where total movement is 190 t-km. "
           "Labour there is FCFA 25 000 cheaper per tonne of product. Should the factory move from M1 to L?", steps=[
            S("Transport cost at M1", math=r"150 \times 500 = 75\,000\ \text{FCFA per t}"),
            S("Transport cost at L", math=r"190 \times 500 = 95\,000\ \text{FCFA per t}"),
            S("Extra transport cost", math=r"95\,000 - 75\,000 = 20\,000"),
            S("Compare", text="The labour saving (25 000) is greater than the extra transport cost (20 000), so L lies inside the critical isodapane and the factory moves: a net saving of FCFA 5 000 per tonne. The critical isodapane here is the 25 000 FCFA line, 50 t-km beyond the optimum."),
        ]),
        T("Weber's third force is **agglomeration**: savings from clustering with other firms (shared services, suppliers, skilled labour). "
          "If several firms' critical isodapanes overlap, they may all move to the overlap. The next lesson develops agglomeration fully."),
        H("Smith's spatial margins to profitability"),
        T("David M. Smith (1960s and 1970s) combined costs and revenues that vary over space. Total cost per unit is lowest at an optimum point O and "
          "rises with distance from it (the **space-cost curve**). Revenue per unit may be constant over the area (the **space-revenue curve**). "
          "Where revenue exceeds cost the firm makes a profit; the points where the curves cross are the **spatial margins to profitability**."),
        IMG("algpu1-smith-margins.svg",
            alt="V-shaped space-cost curve with its lowest point of 70 thousand FCFA at the least-cost site O, rising 5 thousand per km; a horizontal space-revenue line at 100 thousand. They cross at Ma and Mb, 6 km either side of O; the profit area lies between them.",
            caption="Figure 2. Smith's spatial margins to profitability (invented values)."),
        EX("Worked example 3: finding the margins", intro="In Figure 2 cost per unit is FCFA 70 000 at O and rises by FCFA 5 000 for every kilometre from O. "
           "Revenue is FCFA 100 000 per unit everywhere. How far from O can the factory locate and still make a profit?", steps=[
            S("Cost at distance d", math=r"C = 70\,000 + 5\,000d"),
            S("Set cost = revenue", math=r"70\,000 + 5\,000d = 100\,000 \Rightarrow d = 6\ \text{km}"),
            S("Interpret", text="Any site within 6 km of O is profitable, so the firm can choose among many sites for personal or behavioural reasons. "
              "This explains why real firms are often not at the exact optimum."),
        ]),
        H("Lösch and the behavioural approach"),
        T("August Lösch (1940s) argued that firms seek the location of **maximum profit**, and that demand varies over space as well as cost. "
          "Each firm serves a market area; with competition, market areas become **hexagons** that cover the plain without gaps, linking his "
          "work to central place theory. His approach suits market-oriented industries such as bakeries, drinks and cement distribution.\n\n"
          "**Behavioural** writers such as Allan Pred stressed that managers have imperfect information and different abilities to use it; "
          "location decisions can reflect personal preference, chance, inertia or government incentives. **Industrial inertia** is when a firm "
          "stays at a site after the original advantages have gone, because of sunk investment, skilled labour and linkages."),
        T("**Evaluation.** Weber is useful for heavy, weight-losing industries in the past and today (cement, sugar milling near cane fields, ore smelting). "
          "But transport costs are no longer simply proportional to distance (terminal costs, tapering freight rates, bulk shipping); "
          "many modern industries are footloose; markets, government incentives, export processing zones and global supply chains matter "
          "more; and firms are not perfect optimisers. Smith's margins and behavioural approaches are more realistic but harder to predict with."),
        TIP("Paper 2 may ask you to explain or evaluate a location theory or to apply it to an industry; draw the triangle or the margins diagram, "
            "calculate if data are given, then evaluate. Paper 1 tests the material index, isodapanes and the meaning of footloose industry. "
            "Paper 3 questions on Cameroon industry need concrete examples of raw-material and market-oriented factories.", title="Exam link"),
        MISTAKE("Adding weights without distances", "Tonne-kilometres multiply each weight by its distance. Compare totals for each candidate site; "
                "do not just pick the heaviest material without calculation when data are given."),
        MISTAKE("Calling every modern industry footloose", "Footloose means not tied to materials; such firms are still pulled by labour, markets, "
                "skills and incentives. Explain which factor replaces transport cost."),
        QUIZ("A product is made from 4 t of localised material and weighs 1 t. What is the material index and where does Weber predict the factory?",
             ["0.25; at the market", "4; at the material source", "4; at the market", "1; anywhere"], 1,
             "MI = 4 ÷ 1 = 4, greater than 1: a weight-losing industry is pulled towards its material.",
             hint="Weight of localised materials divided by weight of product.",
             feedback=["The ratio is upside down: divide materials by product.", "",
                       "An MI above 1 pulls towards materials, not the market.", "MI = 1 would mean pure materials; here 4 t become 1 t."]),
        QUIZ("A site offers a labour saving of FCFA 12 000 per tonne but lies on the FCFA 15 000 isodapane. What should the firm do, according to Weber?",
             ["Move, because labour is cheaper", "Stay, because the extra transport cost exceeds the labour saving",
              "Move, because isodapanes show lower costs", "Stay, because labour never matters"], 1,
             "The site is outside the critical isodapane (12 000): extra transport cost of 15 000 is more than the saving.",
             hint="Compare the saving with the extra transport cost.",
             feedback=["The saving does not cover the extra transport cost.", "",
                       "Isodapanes show EXTRA transport cost.", "Labour can cause a deviation if the saving is large enough."]),
        PQ("A product needs 3 t of ore (40 km from a site X) and 1 t of fuel (20 km from X), and the product (1.2 t) travels 30 km to market. "
           "Calculate the tonne-kilometres at X and the material index.",
           "t-km = 3(40) + 1(20) + 1.2(30) = 120 + 20 + 36 = 176 t-km. MI = (3 + 1) ÷ 1.2 = 3.33, so the industry is weight-losing and material-oriented."),
        PQ("Cost per unit at the optimum is FCFA 50 000 and rises by FCFA 4 000 per km; revenue is FCFA 74 000. Find the spatial margins and explain their significance.",
           "50 000 + 4 000d = 74 000 gives d = 6 km on each side. Inside this zone any site is profitable, so the firm has freedom to choose for "
           "personal, behavioural or political reasons; outside it the firm makes a loss."),
        PQ("Evaluate the relevance of Weber's theory to the location of manufacturing industry today. (Model plan.)",
           "Introduction: Weber's aims and assumptions. Relevance: weight-losing industries still locate near materials (cement near limestone, "
           "sugar mills near cane, ore processing); the concept of minimising total cost survives. Limits: transport costs fall and are not linear; "
           "many industries are footloose; market, labour skills, government incentives, export zones and agglomeration dominate; firms are "
           "satisficers (Smith, Pred). Example contrasts: market-oriented breweries and plastics in Douala. Conclusion: a sound starting point and "
           "useful for heavy industry, but a partial explanation in a global, service-based economy."),
        SUM("Weber: firms minimise total transport cost; use **tonne-kilometres** to compare sites.",
            "**Material index** above 1 pulls towards materials; weight-gaining or pure-material industries go to the market.",
            "**Isodapanes** and the **critical isodapane** explain deviations to cheap labour or agglomeration.",
            "Smith: profit is possible anywhere within the **spatial margins**; Lösch: maximise profit over hexagonal market areas.",
            "Behavioural factors and inertia explain why real firms depart from the optimum; evaluate theory against real examples."),
    ],
))

# ---------------------------------------------------------------------------
# Industrial, Transport & Service Geography / Industrial agglomeration and deindustrialization
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_IND, topic="Industrial agglomeration and deindustrialization",
    title="Industrial agglomeration and deindustrialization: why industry clusters and why it declines",
    slug="gpu1-agglomeration-deindustrialization",
    minutes=24,
    summary="Agglomeration economies (localisation and urbanisation) and diseconomies, how agglomeration differs from industrial linkages, the location quotient as a measure of concentration, and the causes, effects and responses to deindustrialization.",
    objectives=[
        "Define industrial agglomeration and distinguish it clearly from industrial linkages",
        "Explain the merits and demerits of agglomeration with examples",
        "Calculate and interpret a location quotient and measures of manufacturing decline",
        "Explain the causes and effects of deindustrialization and evaluate responses",
    ],
    key_concepts=["Industrial agglomeration", "Agglomeration economies", "Localisation and urbanisation economies",
                  "Industrial linkages", "Agglomeration diseconomies", "Location quotient", "Deindustrialization", "Global shift"],
    blocks=[
        H("Introduction"),
        T("Most of Cameroon's manufacturing is concentrated in and around Douala, in industrial zones such as Bassa and Bonabéri, with a smaller "
          "share in Yaounde and other towns. Why do factories cluster rather than spread out? And why, in old industrial regions of Europe and "
          "North America, have so many factories closed? This lesson answers both questions."),
        D("**Industrial agglomeration** is the clustering of many firms and industries in one place, and the cost savings (**agglomeration "
          "economies**) that firms gain from being close together.", title="Definition: industrial agglomeration"),
        D("**Industrial linkages** are the flows of goods, services and information between firms: **backward** linkages to suppliers, "
          "**forward** linkages to customers, and **lateral** (horizontal) links between firms supplying the same customer. Linkages are one "
          "*cause* of agglomeration, but they are not the same thing: agglomeration is the spatial cluster and its savings.", title="Linkages are not agglomeration"),
        H("Agglomeration economies"),
        KEY("Two kinds of external economies", "Savings that come from outside the firm.", cards=[
            ["Localisation economies", "From many firms of the SAME industry in one place: specialised suppliers, pool of skilled workers, shared research and repair services, reputation of the area. Alfred Marshall described such industrial districts."],
            ["Urbanisation economies", "From the size and variety of a CITY: large market, banks and insurance, port and airport, roads, power, water, universities and business services shared by all industries."],
        ]),
        T("Agglomeration can become self-reinforcing. A cluster attracts more firms, more workers and more services, which make it even more "
          "attractive. This **cumulative** growth is the core of Myrdal's model, met later in the module."),
        KEY("Diseconomies of agglomeration", "When clusters grow too large.", cards=[
            ["Congestion", "Traffic jams delay deliveries and workers, raising costs."],
            ["High land and labour costs", "Competition for land and staff pushes up rents and wages."],
            ["Pollution and waste", "Air and water pollution, waste disposal problems, health costs and stricter regulation."],
            ["Infrastructure strain", "Power cuts, water shortages and overcrowded housing."],
        ]),
        T("When diseconomies exceed economies, firms decentralise to suburbs, smaller towns or other regions. A balanced answer on merits and "
          "demerits should therefore give both and say what tips the balance."),
        H("Measuring concentration: the location quotient"),
        F(r"LQ = \frac{e_i / e}{E_i / E}", title="Location quotient"),
        T("Here $e_i$ is employment in industry $i$ in the region, $e$ total employment in the region, $E_i$ employment in industry $i$ in the "
          "nation and $E$ total national employment. LQ above 1 means the region has a higher share of that industry than the nation: it is "
          "concentrated (specialised) there. LQ = 1 means the same share; below 1 means under-represented."),
        EX("Worked example 1: location quotient", intro="A region employs 12 000 of its 60 000 workers in manufacturing. The nation employs 1.5 million of its "
           "15 million workers in manufacturing (invented figures). Calculate and interpret the LQ.", steps=[
            S("Regional share", math=r"12\,000 \div 60\,000 = 0.20"),
            S("National share", math=r"1\,500\,000 \div 15\,000\,000 = 0.10"),
            S("LQ", math=r"0.20 \div 0.10 = 2.0"),
            S("Interpret", text="The region has twice the national share of manufacturing: a strong industrial concentration."),
        ]),
        H("Deindustrialization"),
        D("**Deindustrialization** is the long-term decline of manufacturing industry in a country or region, measured by falling manufacturing "
          "employment, a falling share of employment or output, and factory closures.", title="Definition: deindustrialization"),
        EX("Worked example 2: measuring decline", intro="In an old industrial region, manufacturing employment fell from 800 000 to 260 000, and its share of all jobs "
           "fell from 40 per cent to 13 per cent (invented figures). Express both changes.", steps=[
            S("Absolute fall", math=r"800\,000 - 260\,000 = 540\,000\ \text{jobs}"),
            S("Percentage fall in jobs", math=r"\frac{540\,000}{800\,000} \times 100 = 67.5\%"),
            S("Change in share", text="From 40 to 13 per cent is a fall of 27 percentage points. Say 'percentage points' for a change in a share, not 'per cent'."),
        ]),
        KEY("Causes of deindustrialization", "Usually several act together.", cards=[
            ["Global shift", "Transnational firms move production to lower-cost countries (newly industrialized countries, next lesson)."],
            ["Technology and automation", "Output can rise while jobs fall, because machines replace workers."],
            ["Competition and old plant", "Old factories, high costs and exhausted raw materials (coal, ore) cannot compete."],
            ["Tertiarisation", "Demand and investment shift to services as incomes rise."],
            ["Policy", "Removal of subsidies or trade protection; in some developing countries cheap imports undercut young industries."],
        ]),
        T("**Effects** include unemployment, out-migration, derelict land and buildings, falling tax income and social problems, but also cleaner "
          "air and land that can be reused. **Responses** include regeneration schemes, enterprise zones, retraining, attracting service and "
          "high-technology firms, and reuse of old sites for housing, retail and leisure. Economists such as Dani Rodrik have also described "
          "**premature deindustrialization**: manufacturing peaking at lower income levels in many developing countries than it did in Europe."),
        H("Evaluation"),
        T("Agglomeration explains why industry concentrates in a few cores such as Douala, but it also explains regional inequality, congestion and "
          "pollution there. Deindustrialization is not always a sign of failure: in rich countries it partly reflects rising productivity and growth "
          "of services. But for workers and towns that depended on one industry, the costs are concentrated and long-lasting."),
        TIP("The 2023 examiners' report says candidates gave bald definitions of agglomeration and confused it with industrial linkages. In Paper 2, "
            "define agglomeration precisely, then explain merits (economies) and demerits (diseconomies) with places. Paper 1 can test the LQ and the "
            "types of economies.", title="Exam link"),
        MISTAKE("Writing about linkages when asked about agglomeration", "Linkages are flows between firms; agglomeration is the clustering and the "
                "savings from it. You may mention linkages as one cause, but answer the question set."),
        MISTAKE("Confusing a fall in share with a fall in jobs", "Manufacturing's share can fall while the number of jobs rises (if services grow faster). "
                "State which measure you are using."),
        QUIZ("Which is an URBANISATION economy?",
             ["A pool of workers skilled in one industry", "Specialist suppliers to one industry",
              "A large city market with banks, a port and business services used by all industries", "Internal savings from producing more units in one factory"], 2,
             "Urbanisation economies come from the size and variety of the city, shared across industries.",
             hint="Which saving comes from the city as a whole?",
             feedback=["This is a localisation economy (same industry).", "This is a localisation economy.", "",
                       "This is an internal economy of scale, not an external agglomeration economy."]),
        QUIZ("A region has 6 per cent of its workers in textiles; the nation has 3 per cent. What is the LQ for textiles?",
             ["0.5", "2.0", "3.0", "18"], 1,
             "LQ = 0.06 ÷ 0.03 = 2.0: textiles are concentrated in the region.",
             hint="Divide the regional share by the national share.",
             feedback=["This divides the national share by the regional share.", "", "This subtracts the shares.", "This multiplies the percentages."]),
        PQ("A region employs 3 000 of 50 000 workers in food processing; the nation employs 150 000 of 15 million. Calculate and interpret the LQ.",
           "Regional share 3 000 ÷ 50 000 = 0.06; national share 150 000 ÷ 15 000 000 = 0.01; LQ = 6.0. Food processing is very strongly concentrated in the region."),
        PQ("Explain two merits and two demerits of industrial agglomeration.",
           "Merits: shared infrastructure and services (port, power, banks) lower costs; a pool of skilled labour and specialised suppliers reduces "
           "training and input costs (localisation economies). Demerits: congestion raises transport time and cost; high land rents and wages, and "
           "pollution with its health and clean-up costs (diseconomies). Give a place, for example Douala's industrial zones."),
        PQ("Examine the causes and consequences of deindustrialization in a named region. (Model plan.)",
           "Introduction: define deindustrialization and name the region (for example a former coal and steel region in Europe). Causes: exhaustion "
           "of raw materials, old plant, global shift of production to lower-cost countries, automation, competition, policy change. Consequences: "
           "job losses and unemployment, out-migration, derelict land, social problems, falling local revenue; positive effects such as cleaner "
           "environment and land for redevelopment. Responses and evaluation: regeneration, retraining, new service jobs; success varies. Conclusion: "
           "several interacting causes; effects concentrated in single-industry towns."),
        SUM("**Agglomeration** = clustering of firms and the external economies it brings; **linkages** are flows between firms and only one cause.",
            "**Localisation** economies come from many firms of one industry; **urbanisation** economies from the city's size and variety.",
            "**Diseconomies** (congestion, high costs, pollution) can lead to decentralisation.",
            "The **location quotient** compares regional and national shares; above 1 means concentration.",
            "**Deindustrialization** results from global shift, automation, competition and tertiarisation; effects are uneven."),
    ],
))

# ---------------------------------------------------------------------------
# Industrial, Transport & Service Geography / Newly industrialized countries
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_IND, topic="Newly industrialized countries",
    title="Newly industrialized countries: strategies, stages, growth rates and costs",
    slug="gpu1-newly-industrialized-countries",
    minutes=24,
    summary="What makes a country newly industrialized, the generations of NICs, import-substitution versus export-oriented strategies, the factors behind rapid growth, compound growth and doubling time, the social and environmental costs, and lessons for Africa.",
    objectives=[
        "Define a newly industrialized country and identify the main generations of NICs",
        "Compare import-substitution and export-oriented industrialization",
        "Calculate compound growth and doubling time and interpret them",
        "Evaluate the benefits and costs of rapid industrialization and its relevance to Cameroon",
    ],
    key_concepts=["Newly industrialized country (NIC)", "Import-substitution industrialization (ISI)",
                  "Export-oriented industrialization (EOI)", "Developmental state", "Foreign direct investment (FDI)",
                  "Export processing zone (EPZ)", "Compound growth", "Doubling time"],
    blocks=[
        H("Introduction"),
        T("In the 1960s South Korea had an income per head similar to that of many African countries. Within about a generation it had become "
          "a major producer of ships, steel, cars and electronics. Countries that make this change are called **newly industrialized countries "
          "(NICs)**. Why did some succeed so quickly, what did it cost, and can their experience guide countries such as Cameroon, which aims to "
          "become an emerging economy by 2035?"),
        D("A **newly industrialized country (NIC)** is a country whose economy has moved rapidly from dependence on primary products towards "
          "manufacturing and exports of manufactured goods, with fast growth in income per head, but which has not yet reached the income level "
          "of the long-industrialized countries.", title="Definition: NIC"),
        KEY("Generations of NICs", "Lists differ between textbooks; check yours.", cards=[
            ["First generation (from the 1960s)", "The 'Asian Tigers': South Korea, Taiwan, Hong Kong and Singapore."],
            ["Second generation (from the 1980s)", "Malaysia, Thailand, Indonesia and the Philippines."],
            ["Latin America", "Brazil and Mexico, which industrialized earlier behind trade barriers."],
            ["Later and large", "China, India, Vietnam and Turkey are often added; Mauritius is often cited as an African success with export zones."],
        ]),
        H("Two strategies"),
        D("**Import-substitution industrialization (ISI)** protects home industries with tariffs and quotas so that goods once imported are made "
          "at home for the domestic market. **Export-oriented industrialization (EOI)** encourages firms to make goods for world markets, using "
          "low costs, incentives and export zones.", title="Definitions: ISI and EOI"),
        KEY("Comparing ISI and EOI", "Most NICs used both, in sequence.", cards=[
            ["ISI strengths", "Builds a first industrial base and skills; saves foreign exchange; protects young ('infant') industries."],
            ["ISI weaknesses", "Small home markets limit scale; protected firms may stay inefficient; high-cost inputs; foreign debt for machinery."],
            ["EOI strengths", "Huge world market allows economies of scale; competition forces efficiency; earns foreign exchange; attracts FDI."],
            ["EOI weaknesses", "Dependent on world demand and on TNC decisions; pressure to keep wages low; vulnerable to trade barriers abroad."],
        ]),
        H("Why some countries industrialized rapidly"),
        KEY("Factors behind the first-generation NICs", "Explain how each helped.", cards=[
            ["Developmental state", "Governments planned, directed credit to chosen industries, built infrastructure and set export targets."],
            ["Human capital", "Heavy investment in education and technical skills; a disciplined, low-cost workforce at first."],
            ["Capital", "High domestic savings, foreign aid in the early years, then foreign direct investment by transnational corporations."],
            ["Location and access", "Coastal sites on major shipping routes; preferential access to large markets such as the USA in the Cold War era."],
            ["Export processing zones", "Areas with tax breaks, duty-free imports of inputs and good infrastructure, as in Singapore and later Mauritius."],
        ]),
        T("Many NICs moved through **stages**: first labour-intensive light industry (textiles, clothing, toys), then heavy and capital-intensive "
          "industry (steel, ships, petrochemicals), then high-technology and research-intensive industry (electronics, cars, semiconductors). At each "
          "stage rising wages pushed the simplest work out to cheaper countries, which became the next generation of NICs."),
        H("Measuring rapid growth"),
        F(r"V_n = V_0(1 + r)^n", title="Compound growth"),
        T("Here $V_0$ is the starting value, $r$ the annual growth rate as a decimal and $n$ the number of years. A quick estimate of the time to "
          "double is the **rule of 70**: doubling time is about 70 divided by the growth rate in per cent."),
        EX("Worked example 1: compound growth", intro="A country's income per head is 1 000 units and grows at 7 per cent a year for 10 years. Find the final value and check with the rule of 70.", steps=[
            S("Substitute", math=r"V_{10} = 1000(1.07)^{10}"),
            S("Calculate", math=r"1.07^{10} \approx 1.967 \Rightarrow V_{10} \approx 1967"),
            S("Rule of 70", math=r"70 \div 7 = 10\ \text{years to double}"),
            S("Interpret", text="Income per head almost doubles in a decade. At 3.5 per cent a year it would take about 20 years."),
        ]),
        EX("Worked example 2: change in export structure", intro="Manufactures were 20 per cent of a country's exports in one year and 80 per cent twenty years later (invented figures). "
           "Describe the change and say what it shows.", steps=[
            S("Change in share", text="An increase of 60 percentage points; the share has quadrupled."),
            S("Interpret", text="The economy has shifted from exporting primary products to exporting manufactures: a key sign of NIC status. "
              "Compare Cameroon, where exports remain dominated by primary products such as crude oil, timber, cocoa, coffee, cotton and bananas."),
        ]),
        H("Costs and evaluation"),
        KEY("Costs of rapid industrialization", "Use these for balance.", cards=[
            ["Social", "Long hours and low wages in early stages; weak labour rights in some periods; rapid urbanization and housing shortages."],
            ["Environmental", "Air and water pollution, loss of farmland and coastal habitats, waste."],
            ["Economic", "Foreign debt and exposure to financial shocks, as in the Asian financial crisis of 1997; dependence on export markets."],
            ["Spatial", "Growth concentrated in capital and port regions, widening regional inequality (see the core-periphery lesson)."],
        ]),
        T("Can African countries repeat the NIC path? Supporters point to Mauritius and to rising manufacturing in Ethiopia and Morocco, and to "
          "the African Continental Free Trade Area, which may enlarge markets. Sceptics point to competition from China and Asia, automation, weak "
          "infrastructure and power supply, small domestic markets and today's stricter trade rules that limit the protection the Tigers once used. "
          "For Cameroon, assets include a port, oil, gas, hydroelectric potential, agricultural raw materials and a central position in CEMAC; "
          "constraints include energy supply, transport costs and access to finance (check current figures)."),
        TIP("Paper 2 questions on NICs ask you to explain the factors behind rapid industrialization or to assess its effects; name NICs, explain "
            "strategies and give both benefits and costs. Paper 1 may test the meaning of ISI, EOI, EPZ and FDI, or a growth calculation.", title="Exam link"),
        MISTAKE("Listing NICs without explaining their growth", "Names earn little. Explain the mechanisms: state planning, education, investment, "
                "export orientation, location."),
        MISTAKE("Treating NIC success as automatic", "Global conditions in the 1960s to 1980s (Cold War aid and market access, fewer competitors) "
                "helped the first NICs; these conditions cannot simply be copied."),
        QUIZ("A government raises tariffs on imported soap so that local factories can supply the home market. Which strategy is this?",
             ["Export-oriented industrialization", "Import-substitution industrialization", "Deindustrialization", "Agglomeration"], 1,
             "Protecting home producers to replace imports for the domestic market is ISI.",
             hint="Is the aim to export or to replace imports?",
             feedback=["EOI aims at world markets, not protected home markets.", "", "Deindustrialization is the decline of industry.",
                       "Agglomeration is clustering of firms."]),
        QUIZ("Using the rule of 70, how long does it take an economy growing at 5 per cent a year to double in size?",
             ["5 years", "14 years", "35 years", "70 years"], 1,
             "70 ÷ 5 = 14 years.",
             hint="Divide 70 by the growth rate in per cent.",
             feedback=["This uses the rate itself, not 70 ÷ rate.", "", "This halves 70 instead of dividing by 5.", "This ignores the growth rate."]),
        PQ("Income per head of 2 000 units grows at 8 per cent a year. Estimate the value after 9 years and the doubling time.",
           "2 000 × 1.08 to the power 9 ≈ 2 000 × 1.999 ≈ 3 998 units. Rule of 70: 70 ÷ 8 ≈ 8.75 years, so income roughly doubles in about 9 years, as the calculation confirms."),
        PQ("Explain three factors that helped the first-generation NICs to industrialize rapidly.",
           "Any three, explained: a developmental state that planned investment and directed credit to export industries; heavy investment in "
           "education producing skilled, productive labour; high savings and foreign investment by TNCs; coastal location and access to large "
           "markets such as the USA; export processing zones with tax incentives."),
        PQ("'The benefits of rapid industrialization in NICs have outweighed the costs.' Discuss. (Model plan.)",
           "Introduction: define NIC; name examples. Benefits: rapid rise in income and life expectancy, falling poverty, skills and technology, "
           "infrastructure, export earnings. Costs: low wages and poor conditions in early stages, pollution, regional inequality, debt and financial "
           "crises (1997), urban problems. Evaluation: benefits large and lasting for the Tigers; costs real but partly reduced as incomes rose and "
           "regulation improved; outcomes vary by country and group. Conclusion: overall yes for most first-generation NICs, but with uneven sharing."),
        SUM("A **NIC** has shifted rapidly from primary products to manufacturing and manufactured exports.",
            "Generations: the **Asian Tigers**, then Malaysia, Thailand, Indonesia; plus Brazil, Mexico, China and India.",
            "**ISI** protects home industry; **EOI** targets world markets; most NICs moved from ISI to EOI.",
            "Growth factors: developmental state, education, savings and FDI, location, export zones; growth compounds (rule of 70).",
            "Costs: labour, environmental, financial and regional; judge whether the path can be repeated in Africa today."),
    ],
))

# ---------------------------------------------------------------------------
# Industrial, Transport & Service Geography / Transport network analysis
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_IND, topic="Transport network analysis",
    title="Transport network analysis: connectivity indices, accessibility and the detour index",
    slug="gpu1-transport-network-analysis",
    minutes=25,
    summary="Networks as graphs of vertices and edges; how to calculate and interpret the beta, gamma and alpha indices, the cyclomatic number, the Shimbel accessibility index and the detour index; and the physical and human factors that raise or lower connectivity.",
    objectives=[
        "Define connectivity and accessibility and reduce a road map to a topological graph",
        "Calculate and interpret the beta, gamma and alpha indices and the cyclomatic number",
        "Build a shortest-path matrix to find the Shimbel index and calculate a detour index",
        "Explain, with both positive and negative effects, the factors that influence network connectivity",
    ],
    key_concepts=["Network", "Vertex (node)", "Edge (link)", "Connectivity", "Beta index", "Gamma index", "Alpha index",
                  "Cyclomatic number", "Accessibility", "Shimbel index", "Detour index"],
    blocks=[
        H("Introduction"),
        T("The roads linking Douala, Yaounde, Bafoussam, Bamenda and the towns between them form a **network**. Some regions have many "
          "alternative routes; others depend on a single road, so one landslide or broken bridge cuts them off. Geographers measure these "
          "differences with simple indices taken from graph theory. The 2023 examiners' report found that many candidates could not define "
          "connectivity: this lesson starts there."),
        D("**Connectivity** is the degree to which the places (vertices) in a network are directly joined to one another by links (edges). "
          "A highly connected network has many links and alternative routes between its places.", title="Definition: connectivity"),
        D("**Accessibility** is the ease with which a place can be reached from the other places in the network. It is a property of each "
          "place, whereas connectivity describes the whole network.", title="Definition: accessibility"),
        T("To analyse a network, reduce the map to a **topological graph**: each town or junction becomes a **vertex** (v) and each road between "
          "two vertices becomes an **edge** (e). Distance and shape are ignored; only the pattern of links matters."),
        IMG("algpu1-network.svg",
            alt="Network of six towns A to F joined by eight roads: A-B, A-C, B-C, B-D, C-E, D-E, D-F and E-F.",
            caption="Figure 1. A simple road network with 6 vertices and 8 edges."),
        H("Connectivity indices"),
        KEY("The indices", "v = vertices, e = edges, p = separate sub-graphs (usually 1).", cards=[
            ["Beta index", "β = e ÷ v. Below 1: branching tree; 1: one circuit; above 1: more complex network."],
            ["Gamma index", "γ = e ÷ 3(v − 2), for a planar network. Compares actual edges with the maximum possible; from 0 to 1."],
            ["Alpha index", "α = (e − v + 1) ÷ (2v − 5). Compares actual circuits with the maximum possible; from 0 to 1."],
            ["Cyclomatic number", "μ = e − v + p. The number of circuits (closed loops) in the network."],
        ]),
        EX("Worked example 1: indices for Figure 1", intro="Calculate β, γ, α and μ for the network in Figure 1 (v = 6, e = 8, p = 1).", steps=[
            S("Beta", math=r"\beta = \frac{8}{6} = 1.33"),
            S("Gamma", math=r"\gamma = \frac{8}{3(6-2)} = \frac{8}{12} = 0.67"),
            S("Alpha", math=r"\alpha = \frac{8 - 6 + 1}{2(6) - 5} = \frac{3}{7} = 0.43"),
            S("Cyclomatic number", math=r"\mu = 8 - 6 + 1 = 3"),
            S("Interpret", text="The network has three circuits and two-thirds of the possible links: fairly well connected, with alternative routes, but far from complete."),
        ]),
        H("Accessibility: the shortest-path matrix"),
        T("For each pair of vertices, count the smallest number of edges on a route between them. Write these in a matrix. The row total for a "
          "vertex is its **Shimbel index**: the lower the total, the more accessible the place. The largest single entry in a row is the vertex's "
          "**König number**; the largest in the whole matrix is the network's **diameter**."),
        CODE("""      A  B  C  D  E  F   Shimbel
  A   0  1  1  2  2  3      9
  B   1  0  1  1  2  2      7
  C   1  1  0  2  1  2      7
  D   2  1  2  0  1  1      7
  E   2  2  1  1  0  1      7
  F   3  2  2  1  1  0      9
                     total 46""", "text", title="Shortest-path (topological distance) matrix for Figure 1"),
        EX("Worked example 2: interpreting accessibility", intro="Use the matrix to identify the most and least accessible towns and the network's diameter.", steps=[
            S("Most accessible", text="B, C, D and E each have a Shimbel index of 7: they lie in the centre of the network."),
            S("Least accessible", text="A and F have 9: they are at the edges and need up to 3 edges to reach the opposite end."),
            S("Diameter", text="The largest entry is 3 (A to F), so the diameter is 3."),
            S("Use", text="A planner adding one road to improve accessibility would join A or F more directly, for example A to D."),
        ]),
        H("The detour index"),
        F(r"\text{Detour index} = \frac{\text{actual route distance}}{\text{straight-line distance}} \times 100", title="Detour index"),
        T("A value of 100 means the route is perfectly direct; the higher the value, the more roundabout the route. Some textbooks invert the "
          "fraction (straight-line over actual), so that 100 is perfect and lower values show detours; check which version your textbook uses and "
          "always state your formula."),
        EX("Worked example 3: detour index", intro="Two towns are 30 km apart in a straight line, but the road between them, which winds around a range of hills, is 45 km long. "
           "Calculate the detour index and suggest a reason.", steps=[
            S("Substitute", math=r"\frac{45}{30} \times 100 = 150"),
            S("Interpret", text="The road is 50 per cent longer than the direct line. Steep relief, a river without a bridge, swampy ground or the need "
              "to pass through other settlements could explain the detour."),
        ]),
        H("Factors influencing connectivity"),
        KEY("Factors, explained both ways", "The examiners asked for two-sided explanations: say how each factor can raise or lower connectivity.", cards=[
            ["Relief", "Flat plains allow dense, direct networks; mountains and escarpments reduce links and raise detours, unless tunnels and passes are built."],
            ["Drainage and climate", "Rivers and swamps block links unless bridged; heavy rains wash out unpaved roads, reducing connectivity in the wet season."],
            ["Level of development and capital", "Rich regions can afford dense, paved networks; poor regions have few, often seasonal, roads."],
            ["Population and economic activity", "Dense population, cities, mines and plantations generate traffic that justifies more links; sparse areas get few."],
            ["Government policy and history", "Planned corridors and political decisions add links; colonial networks were often built from ports to export areas, giving tree-like patterns."],
            ["Technology", "Bridges, tunnels and earth-moving machines overcome physical barriers."],
        ]),
        T("**Evaluation.** The indices are quick, objective and good for comparing networks or measuring change over time. But they ignore distance, road quality, "
          "capacity, traffic and cost: a dirt track counts the same as a dual carriageway. They also depend on how vertices are defined. Use them "
          "with maps and fieldwork, not instead of them."),
        TIP("Network questions appear in Paper 2 (factors influencing connectivity, with definitions) and in Paper 3 map work and statistics, where "
            "you may reduce a road map to a graph and calculate indices. Paper 1 tests the formulas and their meaning. Always show the formula, the "
            "substitution and the interpretation.", title="Exam link"),
        MISTAKE("Defining connectivity vaguely", "Write a precise definition (degree to which vertices are directly linked) before discussing factors."),
        MISTAKE("One-sided factor explanations", "Do not only say 'mountains reduce connectivity'. Add how the factor can increase it, or how people overcome it."),
        MISTAKE("Counting edges wrongly", "An edge runs between two adjacent vertices. A road through three towns is two edges, not one."),
        QUIZ("A network has 10 vertices and 9 edges and forms one piece. What does its beta index tell you?",
             ["It has several circuits", "It is a tree-like (branching) network with no circuits", "It is fully connected", "It has exactly one circuit"], 1,
             "β = 9 ÷ 10 = 0.9 < 1, and μ = 9 − 10 + 1 = 0: a branching network.",
             hint="Calculate e ÷ v and compare with 1.",
             feedback=["Circuits need β above 1 (μ above 1).", "", "A fully connected network would have a γ of 1.", "One circuit gives β = 1."]),
        QUIZ("In a shortest-path matrix, which town is the most accessible?",
             ["The town with the highest row total", "The town with the lowest row total", "The town with the most vertices", "The town at the end of the longest road"], 1,
             "The lowest Shimbel index means the fewest edges are needed to reach all other towns.",
             hint="Fewer steps means easier to reach.",
             feedback=["A high total means the town is less accessible.", "", "A town is one vertex.", "Road length is not used in a topological matrix."]),
        PQ("A network has 7 vertices and 8 edges in one piece. Calculate β, γ, α and μ, and interpret.",
           "β = 8 ÷ 7 = 1.14; γ = 8 ÷ 3(5) = 0.53; α = (8 − 7 + 1) ÷ (14 − 5) = 2 ÷ 9 = 0.22; μ = 8 − 7 + 1 = 2. A network with two circuits "
           "and about half the possible links: moderately connected, with limited alternative routes."),
        PQ("The road between two towns is 52 km; the straight-line distance is 40 km. Calculate the detour index and suggest two reasons for the detour.",
           "52 ÷ 40 × 100 = 130. Reasons: steep relief forcing the road along valleys or contours; a river crossed only at one bridge point; "
           "swampy ground; the road serving intermediate villages."),
        PQ("Explain three factors that influence the degree of connectivity of a transport network in a region. (Model plan.)",
           "Define connectivity. Factor 1, relief: plains favour dense direct networks, highlands reduce links, but tunnels and passes can overcome them "
           "(example: winding roads in the Western Highlands). Factor 2, level of economic development: capital allows dense paved networks; poor regions "
           "have sparse, seasonal roads (contrast Littoral with parts of the East). Factor 3, government policy and history: colonial port-to-interior "
           "lines gave branching patterns; national corridor projects add links. Conclude that human factors increasingly override physical ones."),
        SUM("Reduce a map to a graph of **vertices** and **edges**; **connectivity** describes the network, **accessibility** a place.",
            "**β = e/v**, **γ = e/3(v − 2)**, **α = (e − v + 1)/(2v − 5)**, **μ = e − v + p**.",
            "The **shortest-path matrix** gives each place's **Shimbel index**; lowest is most accessible; the largest entry is the **diameter**.",
            "**Detour index** = actual ÷ straight-line distance × 100 (state your version; textbooks differ).",
            "Explain factors both ways: relief, drainage, development, population, policy, technology."),
    ],
))

# ---------------------------------------------------------------------------
# Industrial, Transport & Service Geography / International trade
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_IND, topic="International trade",
    title="International trade: comparative advantage, terms of trade and trade blocs",
    slug="gpu1-international-trade",
    minutes=25,
    summary="Why countries trade (comparative advantage with a worked example), how to calculate the terms of trade and the balance of trade, the problems of primary-product dependence, the role of trade blocs such as CEMAC and the AfCFTA, and fair trade, with evaluation for developing countries.",
    objectives=[
        "Explain comparative advantage and show gains from specialisation with a numerical example",
        "Calculate and interpret the terms of trade index and the balance of trade",
        "Explain why dependence on primary exports disadvantages many developing countries",
        "Evaluate trade blocs, the WTO and fair trade as responses",
    ],
    key_concepts=["International trade", "Absolute and comparative advantage", "Opportunity cost", "Terms of trade",
                  "Balance of trade", "Primary-product dependence", "Trade bloc", "Customs union", "Fair trade"],
    blocks=[
        H("Introduction"),
        T("Cameroon exports crude oil, timber, cocoa, coffee, cotton and bananas, and imports fuels, machinery, vehicles, rice, wheat and fish. "
          "Why trade at all, who gains, and why do many exporters of primary products stay poor? The examiners' report notes that development "
          "issues such as international trade have been neglected by many candidates; they are a real opportunity in Paper 2."),
        D("**International trade** is the exchange of goods and services across national borders. **Visible** trade is in goods; **invisible** "
          "trade is in services such as tourism, shipping, banking and insurance.", title="Definition: international trade"),
        H("Why countries trade: comparative advantage"),
        D("A country has an **absolute advantage** if it can produce more of a good with the same resources. It has a **comparative advantage** "
          "if it can produce the good at a lower **opportunity cost** (the amount of another good given up). The theory of comparative advantage "
          "is credited to David Ricardo (1817).", title="Definitions"),
        CODE("""Output per worker-day     Cocoa (kg)   Cloth (m)
Country X                     10            6
Country Y                      2            4""", "text", title="Invented data for worked example 1"),
        EX("Worked example 1: comparative advantage", intro="Use the table. X has an absolute advantage in both goods. Which good should each country specialise in?", steps=[
            S("Opportunity cost of 1 kg cocoa", math=r"X: \frac{6}{10} = 0.6\ \text{m cloth};\quad Y: \frac{4}{2} = 2\ \text{m cloth}"),
            S("Opportunity cost of 1 m cloth", math=r"X: \frac{10}{6} = 1.67\ \text{kg cocoa};\quad Y: \frac{2}{4} = 0.5\ \text{kg cocoa}"),
            S("Comparative advantage", text="X gives up less cloth to make cocoa, so X has the comparative advantage in cocoa. Y gives up less cocoa to make cloth, so Y has the comparative advantage in cloth."),
            S("Gains", text="Each country has 10 worker-days. With no trade and an even split, total output is 60 kg cocoa and 50 m cloth. If Y makes only cloth (40 m) and X spends 8 days on cocoa and 2 on cloth, output is 80 kg cocoa and 12 + 40 = 52 m cloth: more of both."),
        ], check=r"\text{before: } 60\ \text{kg}, 50\ \text{m};\ \text{after: } 80\ \text{kg}, 52\ \text{m}"),
        T("Trade benefits both only if the exchange rate between the goods lies between the two opportunity costs (here between 0.6 and 2 m of cloth "
          "per kilogram of cocoa). Where it lies decides how the gains are shared: this is the idea of the terms of trade."),
        H("Terms of trade and balance of trade"),
        F(r"\text{Terms of trade} = \frac{\text{index of export prices}}{\text{index of import prices}} \times 100", title="Terms of trade index"),
        T("Above 100 (compared with the base year) the terms of trade have **improved**: each unit of exports buys more imports. Below 100 they have "
          "**worsened**. The **balance of trade** is the value of visible exports minus visible imports; a negative value is a trade deficit."),
        EX("Worked example 2: terms of trade", intro="Since the base year, a cocoa exporter's export price index has fallen to 90 while its import price index has risen to 120 (invented figures). "
           "Calculate and interpret the terms of trade.", steps=[
            S("Substitute", math=r"\frac{90}{120} \times 100 = 75"),
            S("Interpret", text="The terms of trade have worsened by 25 per cent: the country must export about a third more cocoa to buy the same imports "
              "(100 ÷ 75 = 1.33). This is typical when primary prices fall while manufactured import prices rise."),
        ]),
        EX("Worked example 3: balance of trade and export concentration", intro="A country exports goods worth 2 400 billion FCFA, of which crude oil is 960 billion, and imports goods worth "
           "2 900 billion (invented figures). Find the balance of trade and oil's share of exports.", steps=[
            S("Balance of trade", math=r"2\,400 - 2\,900 = -500\ \text{billion FCFA (deficit)}"),
            S("Oil's share", math=r"\frac{960}{2\,400} \times 100 = 40\%"),
            S("Interpret", text="A deficit must be financed by invisible earnings, borrowing or investment; dependence on one product for 40 per cent of exports leaves the country exposed to oil price swings."),
        ]),
        H("Why primary-product dependence is a problem"),
        KEY("Problems for primary exporters", "Explain each with an example.", cards=[
            ["Price volatility", "Prices of cocoa, coffee and oil swing with weather and world demand, so export earnings and government revenue are unstable."],
            ["Declining terms of trade", "Over long periods many primary prices have tended to fall relative to manufactures (the Prebisch-Singer argument; check your textbook)."],
            ["Low value added", "Raw beans or logs earn less than chocolate or furniture; processing jobs and profits go abroad."],
            ["Tariff escalation", "Importing countries may tax processed goods more heavily than raw materials, discouraging local processing."],
        ]),
        H("Trade blocs, the WTO and fair trade"),
        D("A **trade bloc** is a group of countries that reduce trade barriers among themselves. A **free trade area** removes tariffs between members; "
          "a **customs union** also sets a common external tariff; a **common market** adds free movement of labour and capital.", title="Definition: trade bloc"),
        T("Cameroon belongs to **CEMAC** (with the Central African Republic, Chad, Congo, Equatorial Guinea and Gabon), which has a customs union and a "
          "common currency, the CFA franc, and to the wider **ECCAS**. The **African Continental Free Trade Area (AfCFTA)**, which began trading in 2021, "
          "aims to create a single African market. The **World Trade Organization (WTO)** sets global trade rules. Cameroon also has an Economic "
          "Partnership Agreement with the European Union (check your textbook for its current terms)."),
        T("**Evaluation.** Blocs enlarge markets, allow economies of scale and can encourage regional value chains, but intra-African trade is held back by "
          "poor transport links, similar exports, non-tariff barriers and border delays. **Fair trade** schemes guarantee a minimum price and a social "
          "premium to producer cooperatives; they help some farmers but cover a small share of world trade and can cost producers fees to certify."),
        TIP("In Paper 2 Section C (development issues), questions on trade, globalisation or aid need definitions, an explained theory, examples and "
            "evaluation. Paper 1 may test the terms of trade calculation, types of bloc and comparative advantage. Paper 3 Cameroon questions can "
            "ask about exports and imports.", title="Exam link"),
        MISTAKE("Confusing absolute and comparative advantage", "Comparative advantage depends on opportunity cost, not on who produces more. A country "
                "can lack absolute advantage in everything and still gain from trade."),
        MISTAKE("Confusing foreign trade with foreign aid", "The report notes this confusion. Trade is exchange; aid is a transfer of resources on concessional terms."),
        QUIZ("Export prices index 110, import prices index 88 (base 100). What has happened to the terms of trade?",
             ["Worsened to 80", "Improved to 125", "Unchanged at 100", "Improved to 198"], 1,
             "110 ÷ 88 × 100 = 125: each unit of exports buys 25 per cent more imports.",
             hint="Divide the export index by the import index.",
             feedback=["This divides import by export prices.", "", "The indices are different, so the ratio changes.", "This adds the indices."]),
        QUIZ("Which feature distinguishes a customs union from a free trade area?",
             ["Members remove tariffs on trade with each other", "Members share a common external tariff on imports from outside",
              "Members share a single army", "Members trade only with the WTO"], 1,
             "Both remove internal tariffs; a customs union also sets a common external tariff.",
             hint="What happens to imports from non-members?",
             feedback=["Both types remove internal tariffs, so this does not distinguish them.", "",
                       "Trade blocs are economic, not military.", "The WTO is a rules organisation, not a trading partner."]),
        PQ("Country A makes 8 tonnes of maize or 4 tonnes of cloth per worker; country B makes 3 tonnes of maize or 3 tonnes of cloth. Which country has the comparative advantage in cloth?",
           "Opportunity cost of 1 t cloth: A gives up 8 ÷ 4 = 2 t maize; B gives up 3 ÷ 3 = 1 t maize. B has the lower opportunity cost, so B has the "
           "comparative advantage in cloth (and A in maize), even though A has the absolute advantage in both."),
        PQ("Explain two reasons why many developing countries gain less from international trade than developed countries.",
           "First, dependence on primary exports with volatile and often weakening prices, so the terms of trade can worsen. Second, low value added: "
           "raw materials are processed abroad, and tariff escalation discourages local processing, so jobs and profits are captured elsewhere. Also: "
           "weak bargaining power in trade negotiations and high transport costs."),
        PQ("Assess the advantages and disadvantages of regional trade blocs for African countries. (Model plan.)",
           "Define trade bloc and types; examples CEMAC, ECCAS, ECOWAS, AfCFTA. Advantages: bigger markets, economies of scale, attraction of investment, "
           "regional value chains, stronger bargaining power. Disadvantages: similar primary exports limit trade, poor infrastructure and non-tariff "
           "barriers, unequal gains favouring larger, more industrial members, loss of tariff revenue. Conclusion: potential large, but gains depend "
           "on transport links, diversification and implementation."),
        SUM("Trade rests on **comparative advantage**: specialise where opportunity cost is lowest, and both partners can gain.",
            "**Terms of trade** = export price index ÷ import price index × 100; **balance of trade** = visible exports − visible imports.",
            "Primary exporters face volatile prices, weak terms of trade, low value added and tariff escalation.",
            "Blocs (free trade area, customs union, common market) such as **CEMAC** and the **AfCFTA** enlarge markets but face practical barriers.",
            "Fair trade and WTO rules help some producers; evaluate who gains."),
    ],
))

# ---------------------------------------------------------------------------
# Industrial, Transport & Service Geography / Tourism
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_IND, topic="Tourism",
    title="Tourism: growth, Butler's life cycle, impacts and sustainable tourism",
    slug="gpu1-tourism",
    minutes=25,
    summary="Tourism as a service industry: types and growth factors, Butler's tourism area life cycle applied to visitor data, economic leakage and host attitudes (Doxey), carrying capacity, and sustainable and ecotourism with Cameroonian resources and hindrances.",
    objectives=[
        "Explain the factors behind the growth of tourism and classify tourist resources",
        "Apply Butler's tourism area life cycle model to visitor data and evaluate it",
        "Calculate leakage and visitor intensity and explain the economic, social and environmental impacts of tourism",
        "Evaluate sustainable tourism and ecotourism, with reference to Cameroon",
    ],
    key_concepts=["Tourism", "Tourist resources and attractions", "Butler's tourism area life cycle", "Carrying capacity",
                  "Leakage", "Tourism multiplier", "Doxey's irritation index", "Sustainable tourism", "Ecotourism"],
    blocks=[
        H("Introduction"),
        T("Visitors watch elephants and lions in Waza National Park, climb Mount Cameroon, walk in the Korup rainforest, see the Lobé falls "
          "near Kribi where a river drops straight into the sea, and visit the palace of the Sultan in Foumban. Tourism is one of the fastest-growing "
          "service industries in the world. In the 2023 Paper 3, candidates could name tourist resources but often failed to explain their "
          "**attractions** (what tourists actually do there). This lesson gives you the models and the vocabulary."),
        D("**Tourism** is the temporary movement of people to places outside their usual environment, for at least one night and less than a year, "
          "for leisure, business, health, religion or visiting friends and relatives.", title="Definition: tourism"),
        KEY("Tourist resources", "Always say what the attraction is.", cards=[
            ["Natural", "Wildlife (Waza, Dja Faunal Reserve, Korup), mountains (Mount Cameroon, Mandara mountains at Rhumsiki), beaches (Limbe, Kribi), waterfalls (Lobé, Ekom-Nkam)."],
            ["Human (man-made)", "Palaces and museums (Foumban), festivals and cultural events, monuments, conference facilities, hotels and resorts."],
        ]),
        H("Why tourism has grown"),
        T("Rising incomes and paid holidays in rich and emerging countries, cheaper air travel (wide-bodied jets, low-cost airlines), the internet "
          "and online booking, package holidays, government promotion, and the search for new experiences such as ecotourism have all raised "
          "demand. Business and conference tourism has grown with globalisation."),
        H("Butler's tourism area life cycle (1980)"),
        T("Richard Butler suggested that a resort passes through stages, like a product. Visitor numbers follow an S-shaped curve, and what "
          "happens after stagnation depends on management."),
        IMG("algpu1-butler.svg",
            alt="S-shaped curve of tourist numbers against time divided into five stages: 1 exploration, 2 involvement, 3 development, 4 consolidation, 5 stagnation. After stagnation the curve branches into rejuvenation (rising), stabilisation (level) and decline (falling).",
            caption="Figure 1. Butler's tourism area life cycle, with three possible paths after stagnation."),
        KEY("The stages", "Learn the features of each.", cards=[
            ["1 Exploration", "Few, adventurous visitors; no tourist facilities; attractions are natural or cultural."],
            ["2 Involvement", "Local people provide basic accommodation and services; a tourist season begins."],
            ["3 Development", "Rapid growth; outside investors, larger hotels, advertising; local control falls."],
            ["4 Consolidation", "Growth slows; tourism dominates the local economy; some resentment by residents."],
            ["5 Stagnation and after", "Carrying capacity reached; environmental and social problems; then decline, stabilisation or rejuvenation through new attractions or markets."],
        ]),
        D("**Carrying capacity** is the largest number of visitors a place can absorb without unacceptable damage to its environment, its residents' "
          "quality of life or the visitors' experience.", title="Definition: carrying capacity"),
        EX("Worked example 1: applying Butler to data", intro="A beach resort's annual visitors (invented) at five-year intervals were: 2 000, 5 000, 20 000, 60 000, 75 000, 78 000, 77 000. "
           "Calculate the growth between readings and identify the stages.", steps=[
            S("Growth rates", text="+150%, +300%, +200%, +25%, +4%, −1.3% (each change divided by the earlier value)."),
            S("Early readings", text="Small numbers growing from 2 000 to 5 000: exploration and involvement."),
            S("Rapid growth", text="From 5 000 to 60 000 with growth of 200 to 300 per cent: development."),
            S("Slowing", text="+25% then +4%: consolidation."),
            S("Level then slight fall", text="−1.3%: stagnation, possibly the start of decline unless the resort rejuvenates."),
        ]),
        H("Impacts of tourism"),
        D("**Leakage** is the part of tourist spending that leaves the host area or country: profits of foreign-owned hotels and airlines, imported "
          "food and drink, foreign staff wages and marketing abroad. Spending that stays is re-spent locally and creates further income: the "
          "**tourism multiplier**.", title="Leakage and the multiplier"),
        EX("Worked example 2: leakage and visitor intensity", intro="Tourists spend 50 billion FCFA in a region; 55 per cent leaks out. A town of 30 000 residents receives 120 000 visitors a year (invented figures). "
           "Find the money retained and the number of visitors per 100 residents.", steps=[
            S("Retained spending", math=r"50 \times (1 - 0.55) = 22.5\ \text{billion FCFA}"),
            S("Visitor intensity", math=r"\frac{120\,000}{30\,000} \times 100 = 400\ \text{visitors per 100 residents}"),
            S("Interpret", text="Less than half the spending benefits the region, so policies to buy local food and employ local staff raise the gain. "
              "Four visitors for every resident each year suggests pressure on water, housing and culture."),
        ]),
        KEY("Impacts: both sides", "Use all three dimensions.", cards=[
            ["Economic", "Jobs, foreign exchange, tax, infrastructure (roads, airports) and markets for crafts and farm produce; but seasonal, low-paid jobs, leakage and dependence on one sector vulnerable to shocks."],
            ["Social and cultural", "Pride in heritage and income for cultural groups; but commercialisation of culture, crime, and changes in values and dress."],
            ["Environmental", "Money for conservation and park guards; but litter, erosion of paths, disturbance of wildlife, water use and pollution near hotels."],
        ]),
        T("George Doxey's **irritation index** (1975) suggests that residents' attitudes move from **euphoria** to **apathy**, **annoyance** and "
          "finally **antagonism** as tourist numbers grow. It links neatly to the later stages of Butler's model."),
        H("Sustainable tourism and ecotourism"),
        D("**Sustainable tourism** meets the needs of present tourists and host communities while protecting resources for the future. "
          "**Ecotourism** is small-scale, nature-based tourism that conserves the environment, benefits local people and educates visitors.", title="Definitions"),
        T("Measures include limiting visitor numbers to the carrying capacity, zoning parks, using local guides and porters (for example on Mount "
          "Cameroon), sharing park fees with nearby villages, locally owned lodges and community-based tourism. **Hindrances** to tourism development "
          "in Cameroon include poor roads and few direct flights, limited accommodation of international standard, weak marketing, the cost of "
          "travel, and insecurity in some regions that has reduced visits to parks such as Waza (check current advice)."),
        T("**Evaluating Butler's model.** It is simple and useful for planning, and many resorts show the S-curve. But the stages are hard to identify "
          "in advance, their length varies, not every resort passes through all stages, and it describes rather than explains. It fits mass beach resorts "
          "better than cities or wildlife parks, and it underplays the role of management, which can change the path."),
        TIP("Paper 2 may ask you to apply or evaluate Butler's model or discuss the impacts of tourism; Paper 3 (Cameroon) can ask for natural and "
            "human tourist resources, their attractions, hindrances and the importance of tourism. Always pair each resource with its attraction "
            "and a location.", title="Exam link"),
        MISTAKE("Naming resources without attractions", "The examiners' report says candidates listed resources but not what tourists do there. "
                "Write, for example: Waza National Park, Far North: savanna wildlife viewing on game drives."),
        MISTAKE("Treating ecotourism as any tourism in nature", "Ecotourism must also conserve the environment and benefit local people. A large hotel "
                "beside a park is not ecotourism by itself."),
        QUIZ("In Butler's model, at which stage do outside investors build large hotels and visitor numbers grow fastest?",
             ["Exploration", "Involvement", "Development", "Stagnation"], 2,
             "Development is the stage of rapid growth, outside investment and loss of local control.",
             hint="Look for the steepest part of the curve.",
             feedback=["Exploration has few visitors and no facilities.", "Involvement has small, locally provided facilities.", "",
                       "Stagnation is when growth stops at carrying capacity."]),
        QUIZ("Tourists spend 80 billion FCFA and 35 per cent leaks out of the country. How much is retained?",
             ["28 billion FCFA", "35 billion FCFA", "45 billion FCFA", "52 billion FCFA"], 3,
             "80 × (1 − 0.35) = 52 billion FCFA.",
             hint="Retained share = 1 − leakage share.",
             feedback=["28 billion is the amount that leaks out.", "This confuses the percentage with an amount.", "This subtracts 35 from 80.", ""]),
        PQ("Visitors to a park (thousands, invented) at intervals: 1, 3, 12, 40, 52, 54. Identify the stage reached and suggest two management actions.",
           "Rapid growth from 3 to 40 thousand (development), then slowing (+30% then about +4%): consolidation approaching stagnation. Actions: "
           "set limits based on carrying capacity (permits, zoning); diversify attractions or seasons to rejuvenate; share revenue with local communities "
           "to keep their support."),
        PQ("Explain two economic advantages and two disadvantages of tourism for a developing country.",
           "Advantages: foreign exchange earnings; jobs in hotels, transport and crafts, with a multiplier effect on farming and local suppliers. "
           "Disadvantages: leakage of profits to foreign firms and on imported goods; seasonal, low-paid employment and vulnerability to shocks such as "
           "insecurity or pandemics."),
        PQ("Evaluate Butler's tourism area life cycle model. (Model plan.)",
           "Outline the model and stages with a sketch. Strengths: simple, widely observed S-curve, links to carrying capacity, useful planning tool, "
           "shows the need for management after consolidation. Weaknesses: stages hard to identify and predict, variable lengths, not universal "
           "(cities, heritage sites), descriptive, ignores external shocks and policy. Example: a beach resort through development to stagnation. "
           "Conclusion: a useful framework rather than a prediction."),
        SUM("Tourism grows with incomes, cheap travel, the internet and promotion; resources are natural or human and must be linked to **attractions**.",
            "**Butler (1980)**: exploration, involvement, development, consolidation, stagnation, then decline, stabilisation or rejuvenation.",
            "**Carrying capacity** limits sustainable numbers; **Doxey** tracks residents' attitudes from euphoria to antagonism.",
            "Economic gains are reduced by **leakage**; impacts are economic, social and environmental, positive and negative.",
            "**Sustainable tourism and ecotourism** protect resources and share benefits; Cameroon has rich resources but faces hindrances."),
    ],
))

# ---------------------------------------------------------------------------
# Regional Development & Global Disparities / Indicators of development
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_DEV, topic="Indicators of development",
    title="Indicators of development: single measures, the Human Development Index and their limits",
    slug="gpu1-indicators-of-development",
    minutes=25,
    summary="What development means, economic, social and demographic indicators, how the Human Development Index is calculated from dimension indices with a full worked example, other composite indices, and why every indicator hides something.",
    objectives=[
        "Distinguish economic growth from development and classify indicators",
        "Calculate the dimension indices and the Human Development Index from given data",
        "Explain the strengths and limitations of single and composite indicators",
        "Interpret contrasts between indicators for countries and regions",
    ],
    key_concepts=["Development", "Economic growth", "GNI per capita", "Purchasing power parity (PPP)", "Social indicators",
                  "Composite indicator", "Human Development Index (HDI)", "Dimension index", "Multidimensional poverty"],
    blocks=[
        H("Introduction"),
        T("Is a country with a high income per head always more developed than one with a lower income? Not necessarily: an oil exporter may have "
          "a high average income while many people lack schooling or clean water. At A Level you must be able to choose, calculate and criticise "
          "measures of development. Development issues form part of Paper 1 and Section C of Paper 2."),
        D("**Economic growth** is an increase in a country's output of goods and services, usually measured by GDP or GNI. **Development** is a wider "
          "improvement in people's well-being: income, health, education, freedom, security and the environment.", title="Growth and development"),
        H("Single indicators"),
        KEY("Types of indicator", "Each measures one aspect.", cards=[
            ["Economic", "GNI per capita (often at purchasing power parity), share of workers in primary activities, energy use per person."],
            ["Social", "Adult literacy, school enrolment, doctors per 1 000 people, access to safe water, calorie intake."],
            ["Demographic", "Life expectancy, infant mortality rate, birth rate, population growth rate."],
            ["Political and environmental", "Freedom of speech, corruption perception, carbon emissions per head."],
        ]),
        D("**GNI per capita** is gross national income divided by population. **Purchasing power parity (PPP)** adjusts it for differences in the cost "
          "of living, so that one unit buys the same basket of goods in each country. PPP figures make poorer countries' incomes look closer to "
          "richer ones, because prices are lower there.", title="GNI per capita and PPP"),
        T("**Limits of income measures.** An average hides inequality; much production in the informal sector and on family farms is not recorded; "
          "income says nothing about health or freedom; and growth that destroys forests or pollutes rivers still counts as a gain."),
        H("The Human Development Index"),
        T("The United Nations Development Programme (UNDP) has published the Human Development Index since 1990. It combines three dimensions, "
          "each turned into an index from 0 to 1 using fixed minimum and maximum values called **goalposts**."),
        F(r"\text{Dimension index} = \frac{\text{actual value} - \text{minimum}}{\text{maximum} - \text{minimum}}", title="Dimension index"),
        CODE("""Dimension   Indicator                         Minimum   Maximum
Health      Life expectancy at birth (years)       20        85
Education   Expected years of schooling             0        18
            Mean years of schooling                 0        15
Income      GNI per capita (PPP, US dollars)      100    75 000
            (income uses natural logarithms)""", "text", title="HDI goalposts used by the UNDP in recent reports (check your textbook for the current values)"),
        T("The education index is the average of the two schooling indices. The income index uses logarithms because an extra unit of income matters "
          "more to a poor person than to a rich one. Since 2010 the HDI has been the **geometric mean** of the three indices:"),
        F(r"\text{HDI} = \sqrt[3]{I_{\text{health}} \times I_{\text{education}} \times I_{\text{income}}}", title="HDI"),
        EX("Worked example 1: calculating an HDI", intro="An invented country has life expectancy 62 years, expected years of schooling 12.5, mean years of schooling 6.2 "
           "and GNI per capita (PPP) of 3 700. Calculate its HDI.", steps=[
            S("Health index", math=r"\frac{62 - 20}{85 - 20} = \frac{42}{65} = 0.646"),
            S("Schooling indices", math=r"\frac{12.5}{18} = 0.694;\quad \frac{6.2}{15} = 0.413"),
            S("Education index", math=r"\frac{0.694 + 0.413}{2} = 0.554"),
            S("Income index", math=r"\frac{\ln 3700 - \ln 100}{\ln 75000 - \ln 100} = \frac{\ln 37}{\ln 750} = \frac{3.611}{6.620} = 0.545"),
            S("HDI", math=r"\sqrt[3]{0.646 \times 0.554 \times 0.545} = \sqrt[3]{0.195} = 0.580"),
            S("Interpret", text="An HDI of 0.58 is in the 'medium' range used by the UNDP (check your textbook for the exact category boundaries). Education, especially mean years of schooling, pulls the index down."),
        ]),
        EX("Worked example 2: why the geometric mean?", intro="Country X has indices 0.9, 0.9 and 0.3; country Y has 0.7, 0.7 and 0.7. Compare their arithmetic and geometric means.", steps=[
            S("Arithmetic means", math=r"X: \frac{0.9 + 0.9 + 0.3}{3} = 0.70;\quad Y: 0.70"),
            S("Geometric means", math=r"X: \sqrt[3]{0.9 \times 0.9 \times 0.3} = \sqrt[3]{0.243} = 0.624;\quad Y: 0.70"),
            S("Interpret", text="The geometric mean penalises uneven development: a very low score in one dimension cannot be fully offset by high scores in others."),
        ]),
        H("Other composite indicators"),
        T("The **Physical Quality of Life Index** (Morris D. Morris, 1979) averaged literacy, infant mortality and life expectancy. The "
          "**Multidimensional Poverty Index** (UNDP and the Oxford Poverty and Human Development Initiative, from 2010) counts how many people are "
          "deprived in health, education and living standards at the same time. The **inequality-adjusted HDI** lowers the HDI where gains are unequally "
          "shared. Gender indices measure gaps between women and men."),
        H("Evaluation: what indicators hide"),
        KEY("Problems with all indicators", "Use these in evaluation paragraphs.", cards=[
            ["Averages", "National figures hide regional, rural-urban, gender and income gaps (the core-periphery lessons that follow)."],
            ["Data quality", "Censuses and surveys may be old or incomplete; the informal economy is hard to count."],
            ["Choice and weighting", "Which dimensions are included, and with what weight, is a value judgement."],
            ["What is missing", "Freedom, security, culture, happiness and environmental sustainability are hard to measure."],
        ]),
        T("A good answer therefore uses several indicators together, explains contradictions (for example high income but low life expectancy in some "
          "oil states), and uses regional data within a country where possible, such as differences between regions of Cameroon."),
        TIP("Paper 1 can test definitions (PPP, HDI dimensions) and simple calculations. Paper 2 Section C may ask you to examine the usefulness of "
            "indicators; balance strengths and limits, give examples and conclude that composite measures are better but still imperfect.", title="Exam link"),
        MISTAKE("Calling GNI 'development'", "GNI measures economic output, not well-being. Use 'growth' for output and 'development' for the wider idea."),
        MISTAKE("Adding the three HDI indices", "Since 2010 the HDI is the cube root of their product (geometric mean), not the arithmetic average. "
                "Older textbooks may show the earlier method; state the method you use."),
        QUIZ("Which three dimensions make up the Human Development Index?",
             ["Income, employment and housing", "Health, education and income", "Literacy, infant mortality and life expectancy", "Population, urbanization and industry"], 1,
             "The HDI combines a long and healthy life, knowledge, and a decent standard of living (income).",
             hint="Think of a long life, knowledge and living standard.",
             feedback=["Employment and housing are not HDI dimensions.", "", "These are the components of the older PQLI.", "These are not HDI dimensions."]),
        QUIZ("A country's life expectancy is 72 years. With goalposts of 20 and 85, what is its health index?",
             ["0.72", "0.80", "0.85", "0.98"], 1,
             "(72 − 20) ÷ (85 − 20) = 52 ÷ 65 = 0.80.",
             hint="Subtract the minimum, then divide by the range.",
             feedback=["This divides by 100, not by the goalpost range.", "", "This divides 72 by 85, ignoring the minimum.", "This is a guess not based on the formula."]),
        PQ("Calculate the HDI for a country with health index 0.77, education index 0.66 and income index 0.72.",
           "HDI = cube root of (0.77 × 0.66 × 0.72) = cube root of 0.366 = 0.715 (about 0.72)."),
        PQ("Explain why GNI per capita at PPP is a better income measure than GNI per capita at market exchange rates, and give one limit that remains.",
           "PPP adjusts for differences in the cost of living, so it shows what incomes actually buy; at market rates poor countries' incomes look smaller "
           "than their real purchasing power. A remaining limit: it is still an average, hiding inequality, and it ignores non-market production and well-being."),
        PQ("Assess the usefulness of the Human Development Index as a measure of development. (Model plan.)",
           "Define development and HDI. Strengths: combines economic and social dimensions; simple, comparable over time and between countries; geometric "
           "mean penalises uneven development; has drawn attention to health and education. Limits: national averages hide inequality (hence the IHDI); "
           "omits freedom, environment, security; data quality; choice of goalposts and weights; income still a third of the index. Conclusion: more useful "
           "than any single indicator, but best used with other indices and regional data."),
        SUM("**Growth** is more output; **development** is wider improvement in well-being.",
            "Single indicators are economic, social, demographic or political; **GNI per capita at PPP** adjusts for living costs.",
            "**Dimension index** = (actual − min) ÷ (max − min); income uses logarithms.",
            "**HDI** = cube root of health × education × income indices (geometric mean since 2010).",
            "All indicators hide something: averages, data gaps, weighting choices and missing dimensions."),
    ],
))

# ---------------------------------------------------------------------------
# Regional Development & Global Disparities / Models of development
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_DEV, topic="Models of development",
    title="Models of development: Rostow, Myrdal's cumulative causation and Friedmann's core-periphery",
    slug="gpu1-models-of-development",
    minutes=25,
    summary="An A Level comparison of three models: Rostow's stages of growth and their critics, Myrdal's cumulative causation with backwash and spread effects, and Friedmann's four-stage core-periphery model, applied to Cameroon and evaluated.",
    objectives=[
        "Explain Rostow's stages of growth and evaluate the model, including the dependency critique",
        "Explain Myrdal's cumulative causation with backwash and spread effects",
        "Describe Friedmann's four stages and link them to regional inequality",
        "Apply and compare the models in an essay, with Cameroonian examples",
    ],
    key_concepts=["Rostow's stages of growth", "Take-off", "Dependency theory", "Cumulative causation", "Backwash effects",
                  "Spread effects", "Core and periphery", "Polarisation and trickle-down"],
    blocks=[
        H("Introduction"),
        T("Why do some countries, and some regions within countries, grow faster than others, and do the gaps close or widen over time? Three models "
          "offer different answers. Rostow describes how a whole country grows through stages. Myrdal explains why growth, once started in one place, "
          "tends to concentrate there. Friedmann describes how the map of cores and peripheries changes as a country develops. At O Level you met Rostow's "
          "stages; here you compare the models and judge them."),
        D("A **development model** is a simplified explanation of how economic and social change happens over time and space. Models can be "
          "**linear** (all countries follow the same path) or **spatial** (explaining differences between places).", title="Definition"),
        H("Rostow's stages of economic growth (1960)"),
        KEY("The five stages", "Walt Rostow's sequence.", cards=[
            ["1 Traditional society", "Subsistence farming, limited technology, little investment."],
            ["2 Preconditions for take-off", "Investment in transport and education, commercial farming, an entrepreneurial class; often outside influence."],
            ["3 Take-off", "Rapid growth in a few leading industries; investment rises to about 10 per cent of national income; political and social change."],
            ["4 Drive to maturity", "Growth spreads to many sectors; technology diversifies; less reliance on imports."],
            ["5 High mass consumption", "Durable consumer goods, services and welfare spending dominate."],
        ]),
        T("**Evaluation.** Rostow gave a clear, testable sequence and stressed investment, which influenced aid policy. But the model is based on the "
          "history of Western countries and assumes all countries can follow one path. It says little about how to start take-off, ignores the "
          "environment, and treats countries as isolated. **Dependency theorists** (for example Andre Gunder Frank) argued the opposite: that links with "
          "rich countries through colonialism and trade kept poorer countries as suppliers of raw materials, so their 'underdevelopment' was produced by "
          "the world system rather than being an early stage. NICs show that rapid change is possible, but by different routes from Rostow's."),
        H("Myrdal's cumulative causation (1957)"),
        T("Gunnar Myrdal argued that once a region gains an advantage (a port, a mineral, a capital city), growth there becomes **self-reinforcing**. "
          "New firms create jobs and incomes; a larger market and tax base pay for better services; these attract still more firms and workers."),
        IMG("algpu1-myrdal-loop.svg",
            alt="Circular flow of five boxes: new industry locates in core, more jobs and incomes, bigger market and more tax revenue, better services and infrastructure, more firms and workers attracted, then back to new industry: an upward spiral.",
            caption="Figure 1. Cumulative causation in a growing core, with backwash and spread effects on the periphery."),
        D("**Backwash effects** are the harmful effects of core growth on the periphery: young, skilled workers, savings and investment flow to the core, "
          "and core industries out-compete periphery producers. **Spread effects** are the beneficial effects: the core's demand for food and raw materials, "
          "and the spread of technology, ideas and investment outward.", title="Backwash and spread effects"),
        T("Myrdal argued that, left to market forces, backwash usually outweighs spread, so **regional inequality widens**; government action is needed to "
          "narrow it. Albert Hirschman (1958) used similar ideas, calling them **polarisation** and **trickle-down**, but he was more hopeful that trickle-down "
          "would eventually win."),
        H("Friedmann's core-periphery model (1966)"),
        IMG("algpu1-friedmann-stages.svg",
            alt="Four panels: 1 scattered small settlements; 2 one dominant core surrounded by a periphery; 3 the core linked to growing sub-cores; 4 an integrated network of linked cities of similar importance.",
            caption="Figure 2. Friedmann's four stages of spatial development."),
        KEY("The four stages", "Link each to the level of development.", cards=[
            ["1 Pre-industrial", "Independent local centres; little interaction; little inequality between regions."],
            ["2 Single strong core", "Industrialization concentrates in one core (often the capital or port); the periphery loses people and capital; inequality rises sharply."],
            ["3 Sub-cores emerge", "Growth spreads to secondary cores; the national periphery shrinks, though gaps remain."],
            ["4 Functionally integrated system", "A network of linked cities; regional inequality is much reduced."],
        ]),
        H("Applying the models"),
        EX("Worked example 1: applying the models to Cameroon", intro="Use Myrdal and Friedmann to explain regional contrasts within Cameroon.", steps=[
            S("Identify the core", text="Douala (port, industry, commerce) and Yaounde (capital, administration) form the main core, with the Littoral and Centre regions benefiting most."),
            S("Cumulative causation", text="Port, power, banks and markets attract firms, jobs and migrants, which enlarge the market and attract more investment."),
            S("Backwash", text="Young people migrate from rural parts of regions such as the East, Adamawa and the Far North to the cities; investment concentrates in the core."),
            S("Spread", text="Urban demand for food supports farmers in the West and Centre; roads and telecommunications spread services outward."),
            S("Friedmann's stage", text="The pattern resembles stage 2 moving towards stage 3, with secondary centres such as Bafoussam, Garoua, Bamenda and Kribi (check your textbook for the case study it uses)."),
        ]),
        EX("Worked example 2: comparing the models (essay plan)", intro="'Regional inequality inevitably widens as a country develops.' Discuss with reference to development models.", steps=[
            S("Introduction", text="Define regional inequality; introduce Myrdal, Hirschman and Friedmann."),
            S("Widening", text="Myrdal: cumulative causation and backwash widen gaps without intervention; Friedmann stage 2 shows inequality peaking."),
            S("Narrowing", text="Hirschman: trickle-down and policy narrow gaps later; Friedmann stages 3 and 4 show integration; examples of decentralisation and new growth centres."),
            S("Evaluation", text="Outcomes depend on policy, infrastructure and global links; diseconomies in the core can push firms outward."),
            S("Conclusion", text="Inequality tends to widen in early industrialization but need not keep widening: 'inevitably' is too strong."),
        ]),
        T("**Evaluation of the spatial models.** They explain real patterns well and justify regional policy. But they are descriptive, underplay global "
          "forces (transnational firms, commodity prices), assume one dominant core, and the timing of stages is unclear. Friedmann's later stages describe "
          "rich countries better than most low-income countries."),
        TIP("Paper 2 questions on development models often ask you to describe a model and assess its relevance to developing countries. Draw the "
            "diagram, explain the mechanism, apply it to a named country or region, then evaluate. The examiners' report notes candidates confusing the "
            "Demographic Transition Model with Rostow's model; keep each model's variables clear.", title="Exam link"),
        MISTAKE("Describing a model without applying it", "Marks come from application and evaluation. After describing Myrdal or Friedmann, show it working in a named place."),
        MISTAKE("Mixing up backwash and spread", "Backwash harms the periphery (outflows of people and capital); spread helps it (demand and diffusion from the core)."),
        QUIZ("In Myrdal's model, the migration of young, skilled workers from a rural region to the capital is an example of:",
             ["a spread effect", "a backwash effect", "take-off", "high mass consumption"], 1,
             "Losing workers and skills to the core harms the periphery: a backwash effect.",
             hint="Does the flow help or harm the periphery?",
             feedback=["Spread effects benefit the periphery.", "", "Take-off is a Rostow stage.", "High mass consumption is a Rostow stage."]),
        QUIZ("In Friedmann's model, which stage has the greatest inequality between core and periphery?",
             ["Stage 1, pre-industrial", "Stage 2, single strong core", "Stage 3, sub-cores emerge", "Stage 4, integrated system"], 1,
             "Industry and wealth concentrate in one core while the periphery loses people and capital.",
             hint="Which stage has only one centre of growth?",
             feedback=["In stage 1 there is little inequality between regions.", "", "In stage 3 growth spreads to sub-cores.", "Stage 4 has the least inequality."]),
        PQ("Distinguish between backwash and spread effects, with one example of each.",
           "Backwash effects harm the periphery as the core grows: for example, migration of young workers from rural areas to Douala, or local craft "
           "industries closing because of competition from core factories. Spread effects benefit the periphery: for example, growing urban demand for "
           "food from farmers in the West Region, or the spread of mobile phone networks and banking."),
        PQ("Give two criticisms of Rostow's model.",
           "It is based on the history of Western countries and assumes one path for all; it ignores the effects of colonialism and unequal trade "
           "(dependency theory); it neglects the environment and the role of social factors; it does not explain how to reach take-off."),
        PQ("Assess the relevance of Friedmann's core-periphery model to a developing country you have studied. (Model plan.)",
           "Outline the four stages with a sketch. Relevance: a dominant core (for example Douala-Yaounde) with backwash from peripheral regions matches "
           "stage 2; secondary centres suggest movement towards stage 3; policies of decentralisation try to speed this. Limits: two cores rather than one; "
           "global forces (commodity prices, foreign investment) shape the pattern; stage 4 is far off and may not follow automatically. Conclusion: "
           "a good description of present inequality but not a reliable prediction."),
        SUM("**Rostow (1960)**: five linear stages from traditional society to high mass consumption; criticised as Western-based; dependency theory reverses the cause.",
            "**Myrdal (1957)**: growth is self-reinforcing in the core (**cumulative causation**); **backwash** usually outweighs **spread**, so gaps widen.",
            "**Hirschman**: polarisation then trickle-down; more optimistic about convergence.",
            "**Friedmann (1966)**: pre-industrial, single core, sub-cores, integrated system; inequality peaks at stage 2.",
            "Apply each model to a named place and evaluate its limits."),
    ],
))

# ---------------------------------------------------------------------------
# Regional Development & Global Disparities / Regional development strategies
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_DEV, topic="Regional development strategies",
    title="Regional development strategies: growth poles, bottom-up development and decentralisation",
    slug="gpu1-regional-development-strategies",
    minutes=25,
    summary="Why governments try to reduce regional inequality, how to measure it with the ratio and the coefficient of variation, top-down strategies such as growth poles, corridors and new capitals, bottom-up and rural strategies, decentralisation in Cameroon, and how to judge success.",
    objectives=[
        "Explain the aims of regional development policy and measure regional inequality",
        "Explain top-down strategies, especially growth poles, and their strengths and weaknesses",
        "Explain bottom-up, rural and decentralisation strategies, with Cameroonian examples",
        "Evaluate the success of regional development strategies using evidence",
    ],
    key_concepts=["Regional inequality", "Regional development policy", "Top-down development", "Bottom-up development",
                  "Growth pole", "Development corridor", "Decentralisation", "Coefficient of variation"],
    blocks=[
        H("Introduction"),
        T("The previous lesson showed that, left to the market, growth tends to concentrate in cores and widen regional gaps. Governments respond with "
          "**regional development strategies**. Cameroon, for example, has built a deep-sea port and industrial zone at Kribi, hydroelectric dams such as "
          "Lom Pangar and Memve'ele, and has transferred powers to regions and councils. Do such strategies work, and how would we know?"),
        D("A **regional development strategy** is a planned set of policies that aims to raise incomes and living standards in lagging regions and to "
          "reduce inequality between regions, while keeping national growth.", title="Definition"),
        KEY("Why reduce regional inequality?", "Three kinds of reason.", cards=[
            ["Equity", "Fairness: people should have similar opportunities wherever they live."],
            ["Efficiency", "Unused labour and land in the periphery are wasted; congestion and high costs in the core are reduced."],
            ["Unity and stability", "Large gaps can cause resentment, migration pressure and instability; balanced growth supports national cohesion."],
        ]),
        H("Measuring regional inequality"),
        T("Before judging a policy, measure the gap. Two simple measures are the **ratio** of the richest region's value to the poorest region's, and "
          "the **coefficient of variation (CV)**, which you will meet again in statistical techniques: the standard deviation divided by the mean, as a percentage."),
        F(r"CV = \frac{\sigma}{\bar{x}} \times 100", title="Coefficient of variation"),
        EX("Worked example 1: has inequality fallen?", intro="Income per head (thousand FCFA, invented) in five regions was 900, 650, 400, 300 and 250. Ten years after a "
           "regional programme it was 850, 650, 480, 400 and 370. Calculate the ratio and the CV for each year (use the population standard deviation).", steps=[
            S("Before: mean and ratio", math=r"\bar{x} = \frac{2500}{5} = 500;\quad \frac{900}{250} = 3.6"),
            S("Before: standard deviation and CV", math=r"\sigma = 242.9;\quad CV = \frac{242.9}{500} \times 100 = 48.6\%"),
            S("After: mean and ratio", math=r"\bar{x} = \frac{2750}{5} = 550;\quad \frac{850}{370} = 2.3"),
            S("After: standard deviation and CV", math=r"\sigma = 178.8;\quad CV = \frac{178.8}{550} \times 100 = 32.5\%"),
            S("Interpret", text="Both measures fell, so regional inequality narrowed while the average rose: evidence of convergence. Note the richest region fell slightly; the programme would need to explain why."),
        ]),
        H("Top-down strategies"),
        D("**Top-down development** is planned and financed by central government or large agencies, usually through big projects, and is expected to "
          "spread benefits outward to the population.", title="Definition: top-down"),
        D("A **growth pole** is a dynamic, fast-growing industry or group of linked industries, usually placed in a chosen centre, intended to stimulate "
          "growth in the surrounding region through linkages and multiplier effects. The idea comes from François Perroux (1955) and was applied to "
          "places by later planners.", title="Definition: growth pole"),
        T("Growth poles rely on the spread effects of Myrdal and the trickle-down of Hirschman: the pole's firms buy local inputs, pay wages that are "
          "spent locally and attract further investment. Other top-down tools are **development corridors** (roads, railways and power lines that link "
          "regions and attract activity along them), **industrial estates and special economic zones** (in Cameroon, industrial zones are managed by MAGZI), "
          "**large dams and energy projects**, and **new capital cities** such as Brasília (1960) and Abuja, which aimed to move growth inland."),
        KEY("Top-down: strengths and weaknesses", "For evaluation.", cards=[
            ["Strengths", "Large investment quickly; infrastructure that small projects cannot provide; visible results; can attract foreign investment."],
            ["Weaknesses", "Capital-intensive projects create few local jobs; profits leak to the core or abroad; weak local linkages leave 'enclaves' or 'cathedrals in the desert'; displacement of local people; high debt."],
        ]),
        H("Bottom-up and rural strategies"),
        D("**Bottom-up development** starts with local communities, who identify their own needs and take part in small, low-cost projects using "
          "appropriate technology, often with help from non-governmental organisations, cooperatives or councils.", title="Definition: bottom-up"),
        T("Examples include village water schemes, farm-to-market roads, cooperatives, microcredit, health posts and community forestry. **Integrated "
          "rural development** combines farming, roads, health and education in one area. Development authorities linked to particular crops and regions, "
          "such as SODECOTON for cotton in the North and UNVDA for rice in the Ndop plain, combine top-down organisation with smallholder participation."),
        KEY("Bottom-up: strengths and weaknesses", "For evaluation.", cards=[
            ["Strengths", "Meets real local needs; cheap; uses local skills and materials; communities maintain what they own; benefits the poorest directly."],
            ["Weaknesses", "Small scale and slow; cannot provide major infrastructure; depends on outside funding and local leadership; may not change national patterns."],
        ]),
        H("Decentralisation"),
        T("**Decentralisation** transfers powers and resources from central government to regional and local authorities, so that decisions are taken "
          "closer to the people affected. In Cameroon, a general code of regional and local authorities (2019) organised regional councils and councils; "
          "FEICOM, the special council support fund, finances local projects (check your textbook for current details). Supporters argue decentralisation "
          "improves local planning and accountability; its success depends on the actual transfer of money, skilled staff and clear responsibilities."),
        EX("Worked example 2: evaluating a growth pole (essay plan)", intro="'Growth poles are an effective way of reducing regional inequality.' Discuss.", steps=[
            S("Introduction", text="Define growth pole and regional inequality; outline the theory (Perroux, spread effects)."),
            S("For", text="Concentrated investment can create a new centre with linkages and multipliers; corridors and ports (for example Kribi's port and industrial zone) can attract firms to a lagging region."),
            S("Against", text="Many poles became enclaves with weak local linkages, capital-intensive plants and leakage of profits; backwash can drain the surrounding area; costs and debt are high."),
            S("Conditions for success", text="Local linkages, training of local workers, supporting infrastructure, and combination with bottom-up programmes in the hinterland."),
            S("Conclusion", text="Effective only under certain conditions and over long periods; most successful as part of a mixed strategy."),
        ]),
        TIP("Paper 2 questions ask you to examine strategies or assess their success; define each strategy, give a located example, weigh strengths "
            "and weaknesses and decide. The examiners' report recommends distinguishing measures that have been proposed from measures that have actually "
            "been carried out, and using concrete Cameroonian examples in Paper 3.", title="Exam link"),
        MISTAKE("Listing projects without evaluating them", "Each example needs a judgement: who benefited, what problems appeared, and how you know."),
        MISTAKE("Treating top-down and bottom-up as opposites with one 'right' answer", "Most successful programmes combine large infrastructure with local participation."),
        QUIZ("A government builds a steel plant in a lagging region, hoping its suppliers and workers' spending will stimulate the whole region. This is:",
             ["a bottom-up project", "a growth pole strategy", "a backwash effect", "decentralisation"], 1,
             "A dynamic industry placed in a chosen centre to spread growth through linkages is a growth pole.",
             hint="Look for a large industry meant to drive regional growth.",
             feedback=["Bottom-up projects are small and community-led.", "", "Backwash is a harmful effect on the periphery, not a policy.",
                       "Decentralisation transfers powers to local authorities."]),
        QUIZ("Regional incomes (thousand FCFA) are 600, 400 and 200. The population standard deviation is 163.3. What is the coefficient of variation?",
             ["27.2%", "40.8%", "163.3%", "300%"], 1,
             "Mean = 400; CV = 163.3 ÷ 400 × 100 = 40.8%.",
             hint="Divide the standard deviation by the mean and multiply by 100.",
             feedback=["This divides by 600, the highest value, instead of the mean.", "", "This is the standard deviation itself.", "This is the ratio of richest to poorest (×100)."]),
        PQ("Distinguish between top-down and bottom-up development, giving an example of each.",
           "Top-down: planned and funded by central government or large agencies, large-scale, e.g. a hydroelectric dam or a deep-sea port with an industrial zone. "
           "Bottom-up: initiated with local communities, small-scale, low-cost and participatory, e.g. a village water scheme or a farmers' cooperative with microcredit."),
        PQ("The ratio of the richest to the poorest region's income per head fell from 3.6 to 2.3 after a programme. Give two reasons why this alone may not prove the programme worked.",
           "The ratio uses only two regions and ignores the others (the CV is better); the change may be due to other causes such as commodity prices, "
           "migration or a fall in the richest region's income; averages may hide inequality within regions; data quality may differ between years."),
        PQ("Assess the success of regional development strategies in a country you have studied. (Model plan.)",
           "Introduction: the regional problem (core around Douala and Yaounde; lagging regions). Strategies: top-down (ports, dams, industrial zones, roads), "
           "rural development authorities, decentralisation and council funding, bottom-up NGO and community projects. Evidence of success: new "
           "infrastructure, some new employment centres, improved services. Limits: persistent gaps in income and services, enclave effects, insecurity and "
           "funding limits, slow transfer of resources. Conclusion: partial success; combined top-down and bottom-up approaches with real decentralisation "
           "offer the best prospects."),
        SUM("Regional strategies aim at **equity, efficiency and unity**; measure inequality with the **ratio** and the **coefficient of variation**.",
            "**Top-down**: growth poles (Perroux), corridors, industrial zones, dams, new capitals; risk of enclaves and leakage.",
            "**Bottom-up**: small, local, participatory projects; cheap and well targeted but limited in scale.",
            "**Decentralisation** moves decisions and money closer to people; success depends on real transfer of resources.",
            "Evaluate with evidence: who gained, what changed in the measures, and what else could explain it."),
    ],
))
