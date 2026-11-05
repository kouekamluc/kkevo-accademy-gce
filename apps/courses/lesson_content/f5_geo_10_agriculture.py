"""Form 5 Geography: Economic Activities, Agriculture (5 lessons, one practice set each)."""

from .dsl import *  # noqa: F403

COURSE = ("geography", "form-5")

MODULE = "Economic Activities"
TOPIC = "Agriculture"

LESSONS = []

# ------------------------------------------------------------------ 1. Defining and classifying agriculture
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Defining and classifying agriculture",
    slug="agri-defining-and-classifying-agriculture",
    minutes=20,
    summary="What agriculture is, how it is classified into two major systems (intensive and extensive), and how a farm can be shown as a system of inputs, processes and outputs.",
    objectives=[
        "Define agriculture and a farming system",
        "Classify agriculture into the two major systems, intensive and extensive",
        "Illustrate agriculture as a system with inputs, processes and outputs",
        "Identify the main inputs, processes and outputs on a named farm",
    ],
    key_concepts=["Agriculture", "Farming system", "Intensive farming", "Extensive farming", "Inputs", "Processes", "Outputs", "Feedback"],
    blocks=[
        H("Introduction"),
        T("Think of the food on your plate today. The maize, plantain, cocoyam, rice, beans or fish may have come from a family farm "
          "near Bamenda, a market garden outside Douala, or a cocoa farm in the Centre or South-West Region. "
          "Farming is the main activity of a large share of Cameroonian families. It is the first of the **primary industries**."),
        T("This lesson gives you the words and the picture you need for the whole topic. You will define agriculture, "
          "sort farming into **two broad systems**, and draw a farm as a system."),
        D("**Agriculture** is the growing of crops and the rearing of animals on land to produce food and raw materials. "
          "It is a **primary industry** because it takes its products directly from the land.", title="Definition: agriculture"),
        D("A **farming system** is a way of farming in which the inputs, the methods and the products fit together in a pattern. "
          "Two farms with the same pattern belong to the same system.", title="Definition: farming system"),
        T("Farm products include food (maize, rice, milk, meat), drinks (tea, coffee, cocoa) and raw materials for industry "
          "(cotton, rubber, palm oil, timber). Cotton from the Far North and North Regions, for example, is a raw material for textiles."),
        H("Classifying agriculture: two major systems"),
        T("Geographers sort farms into groups so that they can compare them. The revised GCE syllabus uses **two major systems**. "
          "The two systems differ in how much is put into the land compared with the size of the land."),
        D("**Intensive farming** puts a **large amount of labour and/or capital** into a **small area** of land, "
          "to get a **high yield per hectare**.", title="Definition: intensive farming"),
        D("**Extensive farming** puts a **small amount of labour and capital** into a **large area** of land. "
          "The yield per hectare is low, but the farm is big, so the total output can still be large.", title="Definition: extensive farming"),
        T("A **hectare** is an area of 100 m by 100 m, which is 10 000 square metres. A **yield** is the amount harvested "
          "from each hectare, for example kilograms per hectare."),
        IMG("f5g-agri-classification.svg",
            alt="Tree diagram: agriculture divides into intensive farming (rice, market gardening, plantation, dairy) and extensive farming (shifting cultivation, nomadic pastoralism, ranching, prairie wheat)",
            caption="Figure 1. The two major farming systems and some forms under each. The next two lessons study the forms."),
        KEY("Intensive or extensive?", "Ask what is put into each hectare.", cards=[
            ["Intensive", "Small farm, many workers or much money per hectare, high yield per hectare, often near a market or a dense population."],
            ["Extensive", "Large farm, few workers and little money per hectare, low yield per hectare, often far from towns where land is cheap."],
        ], note="Always compare input and yield per hectare, not the total size of the harvest."),
        T("Farming can also be grouped as **subsistence** (food mainly for the farmer's family) or **commercial** (products mainly for sale), "
          "and as **arable** (crops), **pastoral** (animals) or **mixed**. These ideas cut across the two systems. "
          "For example, rice farming in a crowded delta is intensive and subsistence, but a plantation is intensive and commercial."),
        H("Agriculture as a system"),
        D("A **system** is a set of parts that are linked and work together. A farm is a system because what the farmer puts in is "
          "changed by the work on the farm into products that come out.", title="Definition: system"),
        T("A farm system has three parts. **Inputs** are what goes into the farm. **Processes** are the farm activities. "
          "**Outputs** are what comes out. The money from the outputs is often used to buy new inputs. This return flow is called **feedback**."),
        IMG("f5g-agri-system.svg",
            alt="Diagram of a cocoa farm as a system: inputs (land, seedlings, labour, tools), processes (planting, weeding, harvesting, drying), outputs (beans, food crops, income, waste), with a feedback arrow from outputs back to inputs",
            caption="Figure 2. A cocoa farm as a system, with feedback."),
        T("Inputs are of two kinds. **Physical inputs** come from nature: relief, soil, rainfall, temperature. "
          "**Human inputs** come from people: labour, capital (money, machines, fertiliser, seed), knowledge and decisions."),
        EX("Model answer 1: illustrate agriculture as a system", intro="Using a farm you know, illustrate agriculture as a system. (A cocoa farm in the Centre Region is used here.)", steps=[
            S("Draw the system", text="Draw three boxes joined by arrows: inputs, then processes, then outputs. Add a feedback arrow from outputs back to inputs (as in Figure 2)."),
            S("Name the inputs", text="Physical inputs: heavy rainfall, forest soil, warm temperatures. Human inputs: family labour, hired labour, cocoa seedlings, a sprayer, a machete and the farmer's skill."),
            S("Name the processes", text="Clearing the land, planting shade trees and cocoa, weeding, spraying against disease, harvesting the pods, fermenting and drying the beans."),
            S("Name the outputs", text="Dried cocoa beans sold to a buyer, food crops grown between the trees for the family, income in FCFA, and waste such as empty pods."),
            S("Show the feedback", text="Part of the income buys seedlings, spray and tools for the next season, so the system continues."),
        ]),
        EX("Model answer 2: classify two farms", intro="Farm A has 2 hectares of vegetables near Douala and employs 6 workers. Farm B has 1 500 hectares of grassland in the Adamawa plateau with 4 herders. Classify each farm and give reasons.", steps=[
            S("Work out labour per hectare", text="Farm A has 6 workers on 2 hectares, which is 3 workers per hectare. Farm B has 4 herders on 1 500 hectares, which is far less than 1 worker per hectare."),
            S("Classify Farm A", text="Farm A is intensive. Much labour is used on a small area, and vegetables give a high yield per hectare."),
            S("Classify Farm B", text="Farm B is extensive. Few workers and little capital are used on a very large area, and the yield per hectare is low."),
            S("Link to location", text="Farm A is near a town market where land is costly, so every hectare is used fully. Farm B is far from towns where land is cheap and large."),
        ]),
        TIP("In Paper 1, a stem such as 'much labour on a small area' points to intensive farming, and 'large area, few workers' points to extensive farming. "
            "In Paper 2 Section C, you may be asked to define and classify agriculture or to illustrate it as a system: draw the system diagram and label it with a named farm.",
            title="Exam link"),
        MISTAKE("Using farm size alone", "A large farm is not always extensive and a small farm is not always intensive. A big plantation can be intensive if it uses much labour, machines and fertiliser on each hectare. Judge the inputs and yield per hectare."),
        MISTAKE("Leaving out feedback", "Many answers show inputs, processes and outputs but forget the arrow from outputs back to inputs. Feedback, such as profit used to buy fertiliser, is what makes it a system."),
        QUIZ("Which statement best defines intensive farming?", [
            "Farming on a very large area with few workers",
            "Farming with a large input of labour or capital on a small area to get a high yield per hectare",
            "Farming only for the family's own food",
            "Farming that uses no machines",
        ], 1, "Intensive farming means a large input per unit area of land, with a high yield per hectare.",
            hint="Think of input per hectare.",
            feedback=["This describes extensive farming.", "", "This is subsistence farming, which can be intensive or extensive.", "Intensive farms often use machines and fertiliser."]),
        QUIZ("Which of these is a PROCESS in a farm system?", [
            "Rainfall", "Fertiliser bought from a shop", "Weeding the crops", "Milk sold at the market",
        ], 2, "Weeding is an activity carried out on the farm, so it is a process.",
            hint="A process is something the farmer does on the farm.",
            feedback=["Rainfall is a physical input.", "Fertiliser is a human (capital) input.", "", "Milk sold is an output."],
            title="Quick check"),
        PQ("Define agriculture and name the two major farming systems.",
           "Agriculture is the growing of crops and the rearing of animals on land to produce food and raw materials. "
           "The two major systems are intensive farming (large inputs on a small area, high yield per hectare) and extensive farming (small inputs on a large area, low yield per hectare)."),
        PQ("Draw and label a simple system diagram for a named farm in Cameroon. Give two inputs, two processes and two outputs.",
           "Draw three boxes in a row (inputs, processes, outputs) joined by arrows, with a feedback arrow from outputs back to inputs. "
           "Cocoa farm example: inputs are rainfall and family labour; processes are weeding and harvesting; outputs are dried beans and income. "
           "The labels must name the farm and the feedback arrow must be shown."),
        PQ("A farmer in the Far North grows cotton on 10 hectares with 2 workers. A farmer near Yaounde grows vegetables on 1 hectare with 5 workers. Which farm is more intensive? Give two reasons.",
           "The Yaounde vegetable farm is more intensive. First, it uses 5 workers per hectare, while the cotton farm uses only 0.2 workers per hectare. "
           "Second, a small area gives a high yield and high income per hectare, which is typical of intensive farming near a large market."),
        SUM("**Agriculture** is the growing of crops and the rearing of animals; it is a primary industry.",
            "The syllabus groups farming into two major systems: **intensive** (large input on a small area, high yield per hectare) and **extensive** (small input on a large area, low yield per hectare).",
            "Judge a farm by input and yield **per hectare**, not by its size alone.",
            "A farm is a **system**: inputs (physical and human) are changed by processes into outputs.",
            "**Feedback** returns part of the outputs, such as income, to the inputs."),
    ],
))

# ------------------------------------------------------------------ 2. Intensive farming
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Intensive farming: characteristics and forms",
    slug="agri-intensive-farming-systems-and-forms",
    minutes=22,
    summary="The characteristics of intensive farming and four of its forms (intensive subsistence rice, market gardening, plantation agriculture and dairy farming), with examples from LICs, NICs and AICs.",
    objectives=[
        "Outline the characteristics of intensive farming",
        "Identify and define four forms of intensive farming",
        "Illustrate each form with an example from a low-income country (LIC), a newly industrialising country (NIC) or an advanced industrial country (AIC)",
        "Explain why intensive farming is found where it is",
    ],
    key_concepts=["Intensive farming", "Intensive subsistence rice farming", "Market gardening", "Plantation agriculture", "Dairy farming", "LIC, NIC and AIC", "Yield"],
    blocks=[
        H("Introduction"),
        T("Stand at the edge of Douala, Yaounde or Bafoussam and look at the farmland. Close to the town you often see small plots "
          "of vegetables, watered and weeded every day. Near Mount Cameroon you see long rows of banana, rubber or oil palm trees "
          "managed by large companies. Both are examples of **intensive farming**, but they are very different forms of it."),
        T("In this lesson you will list the characteristics of intensive farming, then study four of its forms."),
        D("**LIC** means low-income country (for example Cameroon and Bangladesh). **NIC** means newly industrialising country "
          "(for example Brazil, India, China and Malaysia). **AIC** means advanced industrial country (for example the Netherlands, Denmark and Japan). "
          "Your syllabus asks for examples from all three groups. No full case study is required.", title="LIC, NIC and AIC"),
        H("Characteristics of intensive farming"),
        T("Intensive farming has some features in common wherever it is found."),
        KEY("Main characteristics", "Look for these features.", cards=[
            ["Small farms", "Holdings are small, from a fraction of a hectare to a few hectares, except on plantations."],
            ["High inputs", "Much labour, or much capital (fertiliser, improved seed, irrigation, machines, pesticides)."],
            ["High yields", "Large output per hectare, often two or three harvests a year."],
            ["Land used fully", "Little or no fallow; terraces, greenhouses and irrigation extend the land."],
            ["Where found", "Near large markets, in crowded regions, or where fertile soil and water are available."],
        ]),
        T("Intensive farming is a good answer to a simple problem: where land is scarce or costly, the farmer must get more from each hectare. "
          "The cost is hard work, high spending on inputs and, if the farmer is careless, damage to soil and water."),
        IMG("f5g-agri-spectrum.svg",
            alt="Line from extensive on the left to intensive on the right with six farm forms placed along it: nomadic pastoralism, shifting cultivation, commercial ranching, plantation, rice farming, market gardening",
            caption="Figure 1. Farm forms placed from extensive (left) to intensive (right). The positions are approximate."),
        H("Form 1: intensive subsistence rice farming"),
        D("**Intensive subsistence rice farming** is the growing of rice on very small plots, mainly to feed the farmer's family, "
          "using a great deal of manual labour.", title="Definition"),
        T("It is typical of the crowded monsoon lands of Asia, such as the river deltas of Bangladesh, India, Vietnam and China (LICs and NICs). "
          "Families may farm less than one hectare. Rice grows well in warm, wet conditions on flat, flooded land called **paddies**. "
          "On hillsides, farmers build **terraces**, which are flat steps cut into the slope."),
        T("Main features: many family members work on the plot; fields are flooded, ploughed with animals or small machines, and planted by hand; "
          "improved seed and fertiliser raise yields; two crops a year are possible where there is water. "
          "Most of the harvest is eaten, and any surplus is sold. In Cameroon, irrigated rice is also grown in parts of the Far North Region; check your textbook for the details."),
        H("Form 2: market gardening"),
        D("**Market gardening** is the intensive growing of vegetables, fruit and flowers on small farms, mainly for sale in nearby towns. "
          "Where it is done under glass or plastic and with machines, it is often called **horticulture**.", title="Definition"),
        T("Market gardens are near large markets because fresh vegetables and flowers spoil quickly. "
          "In Cameroon, you find market gardens around Douala, Yaounde, Bafoussam and Bamenda. In the Netherlands (an AIC), "
          "heated glasshouses grow tomatoes, peppers and flowers, many of which are exported. Kenya (a LIC) exports vegetables and cut flowers."),
        T("Features: very small plots, high spending per hectare, irrigation, fertiliser and often hired workers, several crops a year, quick sale at the market."),
        H("Form 3: plantation agriculture"),
        D("**Plantation agriculture** is the large-scale growing of a single cash crop, in a hot, wet region, "
          "on a big estate with hired workers, a processing factory and an export market.", title="Definition"),
        T("Examples: oil palm and rubber in Malaysia (an NIC), tea in Kenya (a LIC), sugar and coffee in Brazil (an NIC), "
          "and banana, rubber, oil palm and tea on large estates near Mount Cameroon and in the western highlands. "
          "For the names of the Cameroonian estates, check your textbook."),
        T("Plantations are intensive because a large amount of labour and capital is used on each hectare. They have a manager, "
          "workers' housing, a processing plant, and a road, railway or port such as Douala or Limbe to export the crop. "
          "They give jobs and foreign exchange. But many depend on one crop, so a fall in the world price hurts the workers and the country."),
        H("Form 4: intensive dairy farming"),
        D("**Dairy farming** is the keeping of cattle mainly for milk. Intensive dairy farming uses improved breeds, "
          "fed grass, silage and concentrates, with milking machines and veterinary care.", title="Definition"),
        T("It is typical of the AICs of north-west Europe, such as Denmark and the Netherlands, close to large cities. "
          "Milk goes bad quickly, so the farms are near towns, dairies and good roads. "
          "Dairy farming also exists in NICs such as India, and on small farms in the Cameroon highlands. For more forms such as mixed farming, check your textbook."),
        EX("Model answer 1: describe an intensive farm", intro="Describe the main features of market gardening near a large town. (Paper 2 style: point, evidence, explanation.)", steps=[
            S("Small area, high inputs", text="The plots are small, often only one or two hectares, but the farmers spend heavily on fertiliser, seed, water and labour."),
            S("High yields and several crops", text="Irrigation lets farmers harvest several times a year, so the yield per hectare and the income per hectare are high."),
            S("Location", text="The gardens are near a big town such as Douala. Vegetables are perishable, so a short journey to the market keeps them fresh and keeps transport costs low."),
            S("Market", text="Most of the produce is sold within hours in town markets, which gives the farmer quick cash to buy the next inputs."),
        ]),
        EX("Model answer 2: compare two forms", intro="Compare intensive subsistence rice farming with plantation agriculture.", steps=[
            S("Similarity", text="Both use much labour and many inputs on each hectare, and both give high yields."),
            S("Difference in aim", text="Rice farmers grow mainly to feed their families. Plantations grow a cash crop for sale and export."),
            S("Difference in size and ownership", text="Rice plots are very small and owned or rented by families. Plantations are large estates with managers and hired workers."),
            S("Difference in crops", text="Rice farms grow rice, often with other food crops. Plantations usually grow one crop such as oil palm, rubber, tea or banana."),
        ]),
        TIP("In Paper 1, a stem about 'small plots, many family workers, rice, monsoon Asia' points to intensive subsistence rice farming. "
            "In Paper 2 Section C, you may be asked to identify and define forms of farming: give the definition first, then a named example from an LIC, NIC or AIC. "
            "Case studies are not required for agriculture, so short examples are enough.", title="Exam link"),
        MISTAKE("Calling all plantations extensive", "Plantations cover large areas, but they use much labour, capital and fertiliser per hectare, so they are intensive. Do not decide from the size of the estate alone."),
        MISTAKE("Giving only one country for every form", "Name examples from different income groups, such as rice in Bangladesh (LIC) and Vietnam, market gardening in the Netherlands (AIC), plantations in Malaysia (NIC)."),
        QUIZ("Which form of farming is found in glasshouses in the Netherlands?", [
            "Intensive subsistence rice farming", "Market gardening or horticulture", "Nomadic pastoralism", "Shifting cultivation",
        ], 1, "Heated glasshouses growing vegetables and flowers for sale are market gardening or horticulture, an intensive form.",
            hint="Think of fresh vegetables and flowers for sale.",
            feedback=["Rice paddies are in warm, wet monsoon Asia.", "", "Nomadic pastoralism is moving herds over large areas.", "Shifting cultivation moves from plot to plot."]),
        QUIZ("Why are market gardens usually found close to large towns?", [
            "Land is cheap near towns",
            "Fresh vegetables are perishable and need a quick, cheap journey to the market",
            "There is no rainfall near towns",
            "Farmers there have no workers",
        ], 1, "Vegetables spoil quickly, so growers stay near the market. Land near towns is usually costly, which encourages intensive use.",
            hint="Think of what happens to tomatoes on a long journey.",
            feedback=["Land near towns is expensive, not cheap.", "", "Rainfall does not decide the location of market gardens; irrigation is used.", "Market gardening uses many workers."],
            title="Quick check"),
        PQ("Define plantation agriculture and give two examples from different countries.",
           "Plantation agriculture is the large-scale growing of a single cash crop on a big estate, with hired workers and a processing factory, mainly for export. "
           "Examples: oil palm and rubber in Malaysia, and tea in Kenya. Banana and rubber estates near Mount Cameroon are examples in Cameroon."),
        PQ("State four characteristics of intensive farming.",
           "Small farm size (except plantations); large input of labour or capital per hectare; high yield per hectare, often with more than one harvest a year; "
           "land used fully with little or no fallow, using irrigation, fertiliser or terraces."),
        PQ("Explain why intensive subsistence rice farming is found in the river deltas of monsoon Asia.",
           "The deltas have flat land and fertile alluvial soil, so fields can be flooded for paddies. Heavy monsoon rain and warm temperatures suit rice, and two crops a year are possible. "
           "The population is very dense and land is scarce, so each family farms a tiny plot very intensively, using many family workers to produce enough food."),
        SUM("Intensive farming uses **large inputs on a small area** and gives **high yields per hectare**.",
            "**Intensive subsistence rice farming**: tiny plots, much family labour, monsoon Asia (LICs, NICs).",
            "**Market gardening**: vegetables, fruit and flowers near big towns; horticulture under glass in the Netherlands (AIC).",
            "**Plantation agriculture**: a large estate with one cash crop, hired labour and processing, for export (Malaysia, Kenya, Cameroon).",
            "**Dairy farming**: milk from improved cattle on farms near cities, typical of AICs like Denmark and the Netherlands."),
    ],
))

# ------------------------------------------------------------------ 3. Extensive farming
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Extensive farming: characteristics and forms",
    slug="agri-extensive-farming-systems-and-forms",
    minutes=22,
    summary="The characteristics of extensive farming and four of its forms (shifting cultivation, nomadic pastoralism, commercial ranching and prairie wheat farming), with examples from LICs, NICs and AICs.",
    objectives=[
        "Outline the characteristics of extensive farming",
        "Identify and define four forms of extensive farming",
        "Illustrate each form with examples from LICs, NICs and AICs",
        "Explain why extensive farming is found where it is",
    ],
    key_concepts=["Extensive farming", "Shifting cultivation", "Fallow", "Nomadic pastoralism", "Commercial ranching", "Prairie wheat farming", "Yield per hectare"],
    blocks=[
        H("Introduction"),
        T("Travel north in Cameroon, from the forests around Yaounde to the Adamawa plateau and then to the savanna and Sahel of the Far North. "
          "The farms change. In the forest zone, many families clear a plot, grow food for a few years and then move on. "
          "On the plateau and in the Sahel, herders walk with their cattle to find grass and water. These are **extensive** ways of using land."),
        T("In extensive farming, a lot of land is used, but little labour and capital is put into each hectare."),
        H("Characteristics of extensive farming"),
        KEY("Main characteristics", "Look for these features.", cards=[
            ["Large area", "Farms or grazing areas cover large areas of land."],
            ["Low inputs", "Few workers and little capital (fertiliser, machines, buildings) for each hectare."],
            ["Low yield per hectare", "But the farm is large, so the total output may still be large."],
            ["Land cheap or plentiful", "Found where land is cheap, population is sparse, or climate and soil limit farming."],
            ["Often far from markets", "Distances to towns are long, so the farmer can use land only lightly."],
        ]),
        T("Some extensive farms are subsistence (for the farmer's family) and others are commercial (for sale). "
          "A highly mechanised wheat farm of a thousand hectares is extensive because the input per hectare is small, "
          "even though the farm has costly machines."),
        IMG("f5g-agri-spectrum.svg",
            alt="Line from extensive on the left to intensive on the right with farm forms placed along it",
            caption="Figure 1. The extensive end of the line (left) holds nomadic pastoralism, shifting cultivation and commercial ranching."),
        H("Form 1: shifting cultivation"),
        D("**Shifting cultivation** is a system in which farmers clear a patch of forest or bush, grow crops on it for a few years until the soil is exhausted, "
          "then leave it **fallow** and move to a new plot.", title="Definition"),
        D("**Fallow** means land left uncultivated so that natural vegetation and soil fertility can recover.", title="Fallow"),
        T("It is found in tropical forest and savanna regions of LICs, such as the Congo basin, the Amazon basin and parts of South-East Asia. "
          "In Cameroon, it is practised in parts of the forest zone of the South and East Regions, where it is sometimes called slash-and-burn or bush fallowing."),
        IMG("f5g-agri-shifting-cycle.svg",
            alt="Circular diagram with four stages: clear and burn, plant, yields fall after two or three years, fallow while the bush regrows, then a move to a new plot",
            caption="Figure 2. The shifting cultivation cycle."),
        T("The steps: (1) the farmer cuts and burns the bush; the ash adds nutrients to the soil. (2) Food crops such as maize, cassava, yam and cocoyam are planted with simple tools like hoes and machetes. "
          "(3) After two or three years, weeds and poor soil lower the yields. (4) The plot is left fallow for many years while the bush regrows, and the farmer moves to a new plot."),
        T("This system works well when population is small, because each plot has a long time to recover. "
          "When population grows, the fallow becomes too short, soils decline and yields fall. Burning also releases smoke and can harm the forest."),
        H("Form 2: nomadic pastoralism"),
        D("**Nomadic pastoralism** is the keeping of herds of animals (cattle, sheep, goats, camels) that are moved from place to place to find "
          "grazing and water. The herders have no fixed home and mainly use the animals for food and for trade.", title="Definition"),
        T("It is found in dry and semi-dry regions that are poor for crops: the Sahel and Sahara in Africa, parts of the Middle East, and central Asia. "
          "The herders (LICs) move with the seasons. In Cameroon, herders raise cattle on the Adamawa plateau and in the Sahelian Far North; check your textbook for the groups and routes. "
          "Herders and farmers also share the land around Lake Chad; check your textbook."),
        T("The system suits the environment because the grass is thin and the rainfall is unreliable. Moving avoids overgrazing one place. "
          "Today, problems include droughts, fewer grazing areas as farmland grows, and conflicts between herders and farmers."),
        H("Form 3: commercial ranching"),
        D("**Commercial ranching** is the rearing of cattle or sheep on very large farms called **ranches**, mainly for meat or wool to sell. "
          "A small number of workers look after thousands of animals.", title="Definition"),
        T("Examples: the pampas of Argentina and the cerrado of Brazil (an NIC), the outback of Australia, and the western plains of the USA (AICs). "
          "Land is cheap and the climate is too dry for crops, so a ranch can be very big. Animals graze freely, and the owner uses fences, water points and sometimes feed. "
          "Meat is chilled or canned and exported by rail and ship."),
        H("Form 4: prairie wheat farming"),
        D("**Prairie wheat farming** is the commercial growing of wheat on very large, flat, mechanised farms in temperate grassland regions.", title="Definition"),
        T("It is found on the prairies of Canada and the USA and the steppes of Ukraine and Russia (AICs and NICs). "
          "Farms are hundreds or thousands of hectares. Machines such as tractors and combine harvesters do most work, so few workers are needed. "
          "Fertile soils, flat land and a dry summer for ripening suit wheat, and the yield per hectare is modest, but the total harvest is huge."),
        EX("Model answer 1: describe shifting cultivation", intro="Describe how shifting cultivation is carried out and why it is called extensive. (Paper 2 style.)", steps=[
            S("Describe the method", text="A farmer cuts and burns a patch of forest or bush. The ash feeds the soil. Crops such as cassava and maize are grown with simple tools such as hoes and machetes."),
            S("Describe the cycle", text="After two or three years, yields fall because of weeds and poorer soil. The plot is abandoned and left fallow while the farmer clears a new one."),
            S("Explain why it is extensive", text="It needs a large area, because each family needs many plots, most of them in fallow. Little capital or labour is used on each hectare, and the yield per hectare is low."),
        ]),
        EX("Model answer 2: compare two extensive forms", intro="Compare commercial ranching with nomadic pastoralism.", steps=[
            S("Similarities", text="Both keep animals on large areas of grazing land, with little input per hectare."),
            S("Aim", text="Ranching is commercial: meat and wool are sold for profit. Nomadic pastoralism is mainly for the herders' own food and trade."),
            S("Movement", text="Ranch animals stay inside fenced land. Nomadic herders move with the seasons in search of grass and water."),
            S("Location and income group", text="Ranching is typical of AICs and NICs such as the USA, Australia and Argentina. Nomadic pastoralism is found in LICs in dry regions such as the Sahel."),
        ]),
        TIP("In Paper 1, 'moves from plot to plot, fallow, forest clearing' is shifting cultivation; 'large fenced farms, meat for export' is commercial ranching; 'combine harvesters on flat grassland' is prairie wheat farming. "
            "In Paper 2 Section C, define the form, give an example from an LIC, NIC or AIC, and explain with the link to climate and land cost. No case study is required for agriculture.", title="Exam link"),
        MISTAKE("Saying extensive farms produce little in total", "The yield per hectare is low, but the farm is huge, so a prairie wheat farm or a large ranch can produce a very large total output. Compare per hectare."),
        MISTAKE("Thinking nomads wander without a plan", "Nomadic herders follow regular routes and seasons, moving to where grass and water will be. The movement is a planned response to a dry climate."),
        QUIZ("Which form of farming leaves land fallow while the farmer moves to a new plot?", [
            "Market gardening", "Plantation agriculture", "Shifting cultivation", "Dairy farming",
        ], 2, "Shifting cultivation clears a plot, uses it for a few years and then moves on, leaving the old plot fallow.",
            hint="Think of the cycle of clearing, planting and moving.",
            feedback=["Market gardens use the same plots all year.", "Plantations stay in the same place for decades.", "", "Dairy farms keep fixed fields."]),
        QUIZ("A farm of 2 000 hectares has 5 workers and grows wheat with large machines. Which statement is correct?", [
            "It is intensive because it uses machines",
            "It is extensive because the input of labour and capital per hectare is small and the area is large",
            "It is subsistence because it grows wheat",
            "It is shifting cultivation because it is flat",
        ], 1, "Large area, few workers per hectare and a modest yield per hectare mean extensive farming, even with machines.",
            hint="Divide the workers by the hectares.",
            feedback=["Machines are costly, but the cost per hectare is still small on such a large area.", "", "Farms like this sell wheat; they are commercial.", "Shifting cultivation moves between plots; flatness is irrelevant."],
            title="Quick check"),
        PQ("Define nomadic pastoralism and name one region where it is found.",
           "Nomadic pastoralism is the keeping of herds of animals that are moved from place to place to find grass and water. "
           "It is found in the Sahel (for example in parts of the Far North of Cameroon and around Lake Chad)."),
        PQ("Explain why commercial ranching is extensive.",
           "Ranches cover very large areas and use few workers and little capital on each hectare. The land is cheap and the climate is too dry for crops, so the animals graze freely. "
           "The yield per hectare is low, although the total output of meat is large."),
        PQ("Describe two problems of shifting cultivation when population grows.",
           "First, the fallow period becomes shorter, so soils do not recover and yields fall. "
           "Second, more forest is cleared and burned, which causes loss of trees and soil erosion. Farmers may then need to move farther or to use fertiliser."),
        SUM("**Extensive farming** uses large areas with small inputs per hectare and gives low yields per hectare.",
            "**Shifting cultivation**: clear, plant for a few years, then leave fallow and move; found in tropical forests in LICs.",
            "**Nomadic pastoralism**: herders move animals to find grass and water; found in the Sahel and other dry lands.",
            "**Commercial ranching**: large fenced farms for meat and wool; Argentina, Brazil, Australia, USA.",
            "**Prairie wheat farming**: huge mechanised grain farms in Canada, USA and Ukraine."),
    ],
))

# ------------------------------------------------------------------ 4. Changes in agriculture
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Changes in agriculture: mechanisation, the green revolution and climate-smart farming",
    slug="agri-changes-in-agriculture-green-revolution-and-climate-smart",
    minutes=24,
    summary="How farming has changed over time: mechanisation, the green revolution with its benefits and problems, and climate-smart agriculture with its practices, benefits and challenges.",
    objectives=[
        "Describe changes in agriculture over time, including mechanisation",
        "Describe the green revolution and outline its benefits and problems",
        "Describe climate-smart agriculture and outline its practices",
        "Outline the benefits and challenges of climate-smart agriculture",
    ],
    key_concepts=["Mechanisation", "Green revolution", "High-yielding varieties", "Climate-smart agriculture", "Drought-resistant crops", "Agroforestry", "Conservation tillage", "Water harvesting"],
    blocks=[
        H("Introduction"),
        T("A farmer in the western highlands of Cameroon today may use improved maize seed, fertiliser, a mobile phone to check the market price "
          "and a sprayer for pests. His grandfather used only a hoe and local seed. Farming has changed a great deal over time, "
          "and it is still changing because of new technology and a changing climate."),
        T("This lesson looks at three big changes: mechanisation, the green revolution, and climate-smart agriculture. "
          "Your syllabus asks you to describe changes in agriculture over time, and climate-smart agriculture is one of the new ideas."),
        H("Mechanisation"),
        D("**Mechanisation** is the use of machines, such as tractors, ploughs, combine harvesters and milking machines, "
          "in place of human or animal labour.", title="Definition"),
        T("Machines do work faster and over larger areas. In the USA and Canada, one farmer with a tractor and a combine harvester can farm hundreds of hectares. "
          "Benefits: faster work, bigger farms, lower labour costs and more output. "
          "Problems: machines are costly, need fuel and repairs, and take away jobs from farm workers. "
          "Small farms in many LICs cannot afford them, so they still use hand tools and animals."),
        H("The green revolution"),
        D("The **green revolution** was a period from the 1960s when new **high-yielding varieties (HYVs)** of crops such as wheat and rice, "
          "together with fertiliser, pesticides and irrigation, greatly raised yields in parts of Asia and Latin America.", title="Definition"),
        T("Scientists, among them Norman Borlaug, bred wheat and rice varieties that gave much more grain on each hectare. "
          "India, Mexico and the Philippines were among the first countries to use them. The new seeds worked best when farmers also used fertiliser, pesticides and reliable water."),
        KEY("Benefits and problems", "Both sides must appear in your answer.", cards=[
            ["Benefits", "Much higher yields; more food and less hunger; two or three crops a year; higher incomes for many farmers; food imports reduced."],
            ["Problems", "Seed, fertiliser and water are costly, so poor farmers fell into debt; richer farmers gained most; heavy chemical use polluted water and soil; fewer crop varieties; machines took away some jobs."],
        ], note="The green revolution was far less successful in much of Africa, partly because of poor irrigation, costly inputs and different crops."),
        T("The green revolution shows that technology can solve one problem (too little food) and create others (cost, pollution and inequality). "
          "Geographers therefore look for farming methods that raise yields while protecting the environment. One of these is climate-smart agriculture."),
        H("Climate-smart agriculture"),
        T("The climate is changing. In Cameroon, farmers face longer dry spells in some areas, irregular rains and floods in others. "
          "Farming also adds greenhouse gases to the air, for example from burning bush and from fertiliser."),
        D("**Climate-smart agriculture** is an approach to farming that aims to (1) raise productivity and income, (2) help farmers adapt to climate change, "
          "and (3) reduce or remove greenhouse gases where possible.", title="Definition: climate-smart agriculture"),
        IMG("f5g-agri-csa.svg",
            alt="Diagram with three boxes under climate-smart agriculture: productivity with drought-resistant seed, adaptation with water harvesting and agroforestry, mitigation with conservation tillage and tree carbon storage",
            caption="Figure 1. The three aims of climate-smart agriculture, with example practices."),
        KEY("Main practices", "Know at least four practices and what each does.", cards=[
            ["Drought-resistant crops", "Varieties that give a crop even when rain is short or irregular, such as improved maize, sorghum and millet."],
            ["Agroforestry", "Growing trees with crops. Trees give shade, firewood, fruit and leaves, protect soil and store carbon."],
            ["Conservation tillage", "Little or no ploughing, with crop residues left on the soil. It saves moisture and cuts erosion and fuel use."],
            ["Water harvesting", "Catching rainwater in ponds, tanks, ridges or small dams, for use in dry spells."],
            ["Others", "Mulching, crop rotation, improved livestock feed, early warning from weather forecasts. Check your textbook."],
        ]),
        T("**Benefits**: more stable yields in bad years, better soil and more water kept in the soil, extra income from trees, less damage from climate hazards, and fewer emissions. "
          "**Challenges**: farmers need training and information; seeds, tanks and tree seedlings cost money; some benefits take years (trees grow slowly); "
          "land rights may be unclear, so people hesitate to plant trees; and extension services (advisers) may be far away."),
        EX("Model answer 1: green revolution", intro="Describe the green revolution and explain two of its problems.", steps=[
            S("Describe it", text="From the 1960s, new high-yielding varieties of wheat and rice were introduced in Asia and Latin America. With fertiliser, pesticides and irrigation they raised yields greatly."),
            S("Problem 1: cost and inequality", text="The seeds, chemicals and water cost a lot. Poor farmers borrowed money and sometimes fell into debt, while richer farmers gained most."),
            S("Problem 2: environment", text="Heavy use of fertiliser and pesticide polluted rivers and soil, and fewer crop varieties were grown, which makes crops more at risk from disease."),
        ]),
        EX("Model answer 2: climate-smart practices", intro="Explain how two climate-smart practices help a farmer in a region with unreliable rain.", steps=[
            S("Water harvesting", text="Rainwater is caught in a pond or tank during the rains and used to water crops in a dry spell. This protects the harvest when the rains fail."),
            S("Agroforestry", text="Trees planted among crops give shade, which reduces water loss from the soil. Their leaves enrich the soil and they provide firewood and fruit for extra income."),
            S("Link to climate change", text="Both practices help farmers adapt, and the trees store carbon, which helps to reduce greenhouse gases."),
        ]),
        TIP("In Paper 1 the likely stems are 'high-yielding varieties' (green revolution) and 'conservation tillage' or 'agroforestry' (climate-smart farming). "
            "In Paper 2 Section C, a question may ask you to describe changes in agriculture over time; always give a benefit and a problem for each change. "
            "Case studies are not required.", title="Exam link"),
        MISTAKE("Saying the green revolution had only good effects", "It raised food output, but it also created debt, inequality and pollution. Examiners reward answers that give both sides."),
        MISTAKE("Confusing mitigation and adaptation", "Adaptation helps farmers cope with a changing climate (water harvesting). Mitigation reduces or absorbs greenhouse gases (trees storing carbon, less burning)."),
        QUIZ("What is the main feature of the green revolution?", [
            "The replacement of farms by forests",
            "The use of high-yielding crop varieties with fertiliser and irrigation",
            "The use of only traditional hand tools",
            "A move from crops to nomadic herding",
        ], 1, "New high-yielding varieties, used with fertiliser, pesticides and water, greatly raised yields.",
            hint="Think of the new wheat and rice seeds.",
            feedback=["The green revolution raised yields on farms; it did not remove them.", "", "It involved new science, not only traditional tools.", "It was about crop farming, not pastoralism."]),
        QUIZ("Which practice is an example of water harvesting?", [
            "Ploughing deeply every year",
            "Burning the bush before planting",
            "Catching rainwater in a pond for use in a dry spell",
            "Growing only one crop",
        ], 2, "Water harvesting means collecting and storing rainwater for later use.",
            hint="Think of storing rain.",
            feedback=["Deep ploughing can dry and erode the soil.", "Burning adds greenhouse gases and exposes soil.", "", "Growing one crop does not store water."],
            title="Quick check"),
        PQ("Define climate-smart agriculture.",
           "Climate-smart agriculture is an approach that raises farm productivity and income, helps farmers adapt to climate change, and reduces or removes greenhouse gases where possible."),
        PQ("Name three practices of climate-smart agriculture and say what each does.",
           "Drought-resistant crops give a harvest when the rain is short. Agroforestry grows trees with crops to give shade, protect the soil and store carbon. "
           "Conservation tillage ploughs little or not at all, which keeps water in the soil and reduces erosion. (Water harvesting is another.)"),
        PQ("Outline two benefits and two challenges of climate-smart agriculture for small farmers in Cameroon.",
           "Benefits: more stable yields in dry years, and better soil and extra income from trees. "
           "Challenges: seeds, water tanks and seedlings cost money and the farmers need training; and benefits such as tree growth take years, while unclear land rights may discourage tree planting."),
        SUM("**Mechanisation** uses machines in place of human or animal labour: faster, but costly and jobs are lost.",
            "The **green revolution** (from the 1960s) used high-yielding wheat and rice varieties with fertiliser and irrigation to raise yields.",
            "Green revolution **problems**: cost, debt, inequality, pollution and loss of crop variety.",
            "**Climate-smart agriculture** aims to raise productivity, adapt to climate change and reduce greenhouse gases.",
            "Practices: drought-resistant crops, agroforestry, conservation tillage and water harvesting; challenges include cost, training and land rights."),
    ],
))

# ------------------------------------------------------------------ 5. Von Thunen
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="The Von Thunen model of agricultural land use",
    slug="agri-the-von-thunen-model",
    minutes=24,
    summary="The aims, assumptions and main conclusions of the Von Thunen model: concentric rings of farming around a market, land rent and transport cost, how to compute and draw the rings, and the limits of the model.",
    objectives=[
        "Outline the aims and main conclusions of the Von Thunen model",
        "State the assumptions of the model",
        "Draw the rings of the model to scale from given distances",
        "Describe the limits of the model in the real world",
    ],
    key_concepts=["Von Thunen model", "Land rent", "Cost of transport", "Perishability", "Concentric rings", "Assumptions", "Limitations"],
    blocks=[
        H("Introduction"),
        T("Look at the land around a town such as Bafoussam or Bamenda. Vegetables and fresh milk come from very near the town. Maize and cassava fields come next, "
          "and grazing cattle are often farther out. Why does farming change with distance? In 1826 a German landowner, Johann Heinrich von Thunen, "
          "tried to explain this pattern with a simple model."),
        D("A **model** is a simplified picture of reality that helps us see a pattern. It leaves out many details on purpose.", title="Definition: model"),
        D("The **Von Thunen model** explains how the use of farmland changes with distance from a market town. "
          "It predicts that farming will form **rings** around the market.", title="Definition: Von Thunen model"),
        H("The aim of the model"),
        T("The aim was to find out **what a farmer should grow, and where**, to make the greatest profit. He asked: if a farm is a certain distance from the market, which crop or animal product is best?"),
        T("The answer depends on two things. First, the **cost of transport**: it rises with distance, and it is higher for heavy, bulky or perishable goods. "
          "Second, **land rent**: this is the price farmers pay for the use of land. Land near the market is in high demand, so rent is highest there. Rent falls as distance increases."),
        D("**Land rent** is the payment for using a piece of land. A farmer will pay the highest rent for the land where the crop gives the greatest profit after paying for transport.", title="Definition: land rent"),
        H("The assumptions"),
        T("To keep the model simple, Von Thunen made several assumptions. In the real world, none is exactly true."),
        KEY("Main assumptions", "Learn these.", cards=[
            ["Isolated state", "One market town in the centre; no other towns or trade."],
            ["Flat and uniform land", "The same soil, climate and relief everywhere, with no rivers, roads or hills."],
            ["Transport", "By horse and cart, with cost rising in proportion to distance."],
            ["Farmers", "All are rational: they aim to make the most profit and know prices and costs."],
            ["Market", "Farmers sell all their produce in the central town at fixed prices."],
        ]),
        H("The main conclusions: the rings"),
        T("From these assumptions, the model predicts four rings of land use around the market, as in Figure 1. Textbooks sometimes show more rings. Check your textbook for the version your teacher uses."),
        IMG("f5g-agri-thunen-rings.svg",
            alt="Four concentric rings around a market at the centre: ring 1 market gardening and dairy out to 2 km, ring 2 forestry to 4 km, ring 3 crops to 8 km, ring 4 ranching to 18 km",
            caption="Figure 1. The Von Thunen rings with example distances (an illustration with invented distances)."),
        KEY("What is grown in each ring, and why", "Rings go outward from the market.", cards=[
            ["Ring 1", "Market gardening and dairying. Fresh vegetables and milk are perishable and costly to carry, so the land near the market is used most intensively."],
            ["Ring 2", "Forestry. Firewood was heavy and bulky in Von Thunen's time, and costly to carry far."],
            ["Ring 3", "Crops (grain). Grain is lighter and keeps well, so it can be grown farther out, with less intensive farming."],
            ["Ring 4", "Ranching and livestock. Animals can walk to market, so transport costs are lower and land use is extensive."],
        ]),
        T("Beyond the last ring, land rent falls to zero. Farming does not pay. Von Thunen called this land the wilderness."),
        T("Two main conclusions follow. First, **land use changes with distance from the market**: perishable and bulky goods near, and others farther out. "
          "Second, **intensity falls with distance**: farming near the market is intensive and farming far away is extensive."),
        H("Why the rings form: rent against distance"),
        T("For each land use, we can draw a line showing the rent the farmer can pay at each distance. The line slopes down because transport costs rise. "
          "At each distance, the land goes to the use that can pay the **highest rent**."),
        IMG("f5g-agri-thunen-rent.svg",
            alt="Graph of rent against distance with four sloping lines that cross at 2, 4 and 8 km and reach zero at 4, 8, 12 and 18 km",
            caption="Figure 2. Land rent against distance for four land uses (invented numbers)."),
        T("In Figure 2, the lines cross at 2 km, 4 km and 8 km. These crossing points are the **ring boundaries**. Nearer than 2 km, ring 1 pays the highest rent. "
          "Between 2 and 4 km, forestry pays more. Between 4 and 8 km, crops pay more. Beyond 8 km, ranching pays more until its rent falls to zero at 18 km."),
        H("Computing and drawing the rings"),
        T("To draw the rings in your exam, work out the radius of each ring using the scale, then draw the circles with compasses. Use these steps."),
        EX("Worked example: draw the rings", intro="A model has ring boundaries at 2 km, 4 km, 8 km and 18 km from the market. Draw it at a scale of 1 cm to 2 km. Give the radius of each ring on your drawing.", steps=[
            S("Convert each distance", text="Divide each real distance by 2 km, because 1 cm stands for 2 km."),
            S("Ring 1 boundary", math=r"2 \div 2 = 1\ \text{cm}"),
            S("Ring 2 boundary", math=r"4 \div 2 = 2\ \text{cm}"),
            S("Ring 3 boundary", math=r"8 \div 2 = 4\ \text{cm}"),
            S("Ring 4 boundary", math=r"18 \div 2 = 9\ \text{cm}"),
            S("Draw", text="Mark the market as a dot at the centre. With compasses, draw circles of radius 1, 2, 4 and 9 cm. Shade or label each ring and add a key and the scale."),
        ]),
        EX("Worked example: which use at a given distance?", intro="Using the rent lines in Figure 2, the rent in units per hectare is: gardening and dairy 120 minus 30 times distance; forestry 80 minus 10 times distance; crops 60 minus 5 times distance; ranching 36 minus 2 times distance. Which land use wins at 6 km?", steps=[
            S("Gardening and dairy", math=r"120 - 30 \times 6 = -60"),
            S("Forestry", math=r"80 - 10 \times 6 = 20"),
            S("Crops", math=r"60 - 5 \times 6 = 30"),
            S("Ranching", math=r"36 - 2 \times 6 = 24"),
            S("Choose the highest", text="Crops pay the highest rent (30), so the 6 km land is used for crops. This agrees with ring 3, which runs from 4 to 8 km."),
        ]),
        H("Limits of the model in the real world"),
        T("The model is useful as a starting point, but the real world is more complicated. Most of the assumptions are not true today."),
        KEY("Why the real pattern differs", "Each limit breaks an assumption.", cards=[
            ["Uneven land", "Soils, relief and climate differ from place to place. Rivers, hills and roads change the pattern."],
            ["Many markets", "There are many towns, not one. Rings overlap and distort."],
            ["Modern transport", "Lorries, roads, railways, refrigeration and the telephone reduce the effect of distance and perishability."],
            ["Government and prices", "Subsidies, taxes, quotas and world prices change what farmers grow."],
            ["Farmers are not always rational", "People follow custom, lack information or farm for the family's food, not profit."],
        ]),
        T("Even so, a rough ring pattern can still be seen, for example around some cities: vegetable gardens close to Douala and Yaounde, and more extensive farming farther out. "
          "Check your textbook for local examples."),
        TIP("In Paper 1 expect questions on which ring grows what, and on the assumptions or limits. "
            "In Paper 2 Section C you may be asked to outline the aims and main conclusions of the model: give the aim, the rings, the role of transport cost and land rent, and draw a ring sketch with a key. "
            "Case studies are not required.", title="Exam link"),
        MISTAKE("Mixing up the rings", "Remember: perishable and heavy goods near the market, extensive ranching farthest. Do not put ranching in the centre."),
        MISTAKE("Using real distances as drawing radii", "Always convert distance with the scale. At 1 cm to 2 km, 18 km is 9 cm, not 18 cm."),
        QUIZ("According to the Von Thunen model, which land use is found closest to the market?", [
            "Ranching", "Crops such as grain", "Market gardening and dairying", "Forestry",
        ], 2, "Perishable and costly-to-carry goods like vegetables and milk are produced near the market, where rent is highest.",
            hint="Which products spoil quickly?",
            feedback=["Ranching is in the outer ring because animals can walk to market.", "Grain keeps well and is grown in the middle.", "", "Forestry is the second ring in the classic model."]),
        QUIZ("Which of these is an assumption of the Von Thunen model?", [
            "Many towns of different sizes",
            "Land that is flat and uniform in soil and climate",
            "Modern refrigerated lorries",
            "Different government subsidies for each crop",
        ], 1, "The model assumes flat land, with the same soil and climate everywhere.",
            hint="The model is a simplified, ideal landscape.",
            feedback=["The model has one market town.", "", "Transport is by horse and cart in the model.", "There is no government in the isolated state."],
            title="Quick check"),
        PQ("State the aim of the Von Thunen model.",
           "To explain how the use of farmland changes with distance from a market town, and so find what a farmer should grow, and where, to make the most profit."),
        PQ("Draw and label a simple sketch of the Von Thunen model with four rings and say what is grown in each.",
           "Draw a dot for the market at the centre and four concentric circles. Label ring 1 market gardening and dairying, ring 2 forestry, ring 3 crops, ring 4 ranching. "
           "Add a key. Beyond ring 4, rent falls to zero and farming does not pay."),
        PQ("A model has ring boundaries at 3 km and 6 km. At a scale of 1 cm to 1.5 km, what are the radii on a drawing? Then give two limits of the model.",
           "3 divided by 1.5 is 2 cm and 6 divided by 1.5 is 4 cm. Limits: the real land is not uniform, with rivers, hills and varying soils; "
           "and modern transport and refrigeration reduce the effect of distance. (There are also many markets and government policies.)"),
        SUM("The Von Thunen model explains **land use as it changes with distance from a market**.",
            "It rests on **assumptions**: one market, flat and uniform land, transport cost proportional to distance, and rational farmers.",
            "**Cost of transport** and **land rent** decide the ring pattern: the land goes to the use that pays the highest rent at each distance.",
            "Rings from the market outward: **market gardening and dairying, forestry, crops, ranching**; intensity falls with distance.",
            "**Limits**: uneven land, many markets, modern transport, government policy and non-rational farmers."),
    ],
))
