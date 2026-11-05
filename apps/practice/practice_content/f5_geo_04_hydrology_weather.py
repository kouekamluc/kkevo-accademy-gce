"""Practice sets for Form 5 Geography: Hydrology, Meteorology and Climatology (part 1). One set per lesson."""

from .dsl import *  # noqa: F403

COURSE = ("geography", "form-5")

MODULE = "Hydrology, Meteorology and Climatology"
HC = "The hydrological cycle"
ATM = "The earth's atmosphere"
WC = "Weather and climate"
FC = "Forms of condensation"

SETS = []

# ------------------------------------------------------------------ 1. Global water and the water cycle
SETS.append(practice_set(
    module=MODULE, topic=HC,
    title="Global water and the water cycle: stores and pathways",
    lesson="wx-global-water-and-the-water-cycle",
    questions=[
        MC("Which store holds the largest share of all the water on earth?", [
            C("The oceans and seas", correct=True),
            C("Ice caps and glaciers", why="Ice holds most of the fresh water, but the oceans hold far more water overall."),
            C("Groundwater", why="Groundwater is a large store of fresh water, but much smaller than the oceans."),
            C("Lakes and rivers", why="Lakes and rivers hold only a tiny share of the earth's water."),
        ], steps=[S("Recall", text="The oceans and seas hold about 97 percent of all water.")],
           concept="Distribution of global water", skill="Recall", hint="Think of the biggest body of water you know."),
        NUM("The oceans hold about 97 percent of all water. About what percentage of all water is NOT in the oceans?", 3,
            steps=[S("Subtract", math=r"100 - 97 = 3", text="About 3 percent is outside the oceans, and most of it is fresh water.")],
            unit="percent", concept="Distribution of global water", skill="Calculation", hint="The whole is 100 percent."),
        MC("Which is the largest store of FRESH water?", [
            C("Rivers", why="Rivers hold a tiny share of fresh water."),
            C("The atmosphere", why="The air holds only a very small amount of water vapour."),
            C("Ice caps and glaciers", correct=True),
            C("Lakes", why="Lakes hold only a small part of the fresh water."),
        ], steps=[S("Recall", text="About two-thirds of fresh water is locked up as ice in ice caps and glaciers.")],
           concept="Fresh water stores", skill="Recall", hint="This store is far from most people, in cold regions."),
        MC("Which process changes water vapour into tiny water droplets and forms clouds?", [
            C("Evaporation", why="Evaporation is the opposite change: liquid becomes vapour."),
            C("Transpiration", why="Transpiration is the loss of water vapour by plants."),
            C("Infiltration", why="Infiltration is water soaking into the ground."),
            C("Condensation", correct=True),
        ], steps=[S("Recall", text="When air cools, vapour condenses into droplets. This is condensation.")],
           concept="Water cycle pathways", skill="Recall", hint="Cooling air turns vapour into droplets."),
        MC("Why is the global water cycle described as a closed system?", [
            C("Because it never rains over the oceans", why="Rain falls over the oceans as well as over land."),
            C("Because water is moved around inside it, and almost no water enters or leaves", correct=True),
            C("Because the sun is not needed", why="The sun's energy drives the cycle. Only energy, not water, enters the system."),
            C("Because all water is underground", why="Water is stored in many places: oceans, ice, groundwater, lakes and the air."),
        ], steps=[S("Explain", text="At the global scale the same water is recycled. Only the sun's energy enters.")],
           concept="Closed system", skill="Concept", hint="Does water enter or leave the earth in the cycle?"),
        MC("Rain falls on a hillside in Cameroon, runs into a stream, and reaches the sea. Which are the pathways, in order?", [
            C("Infiltration, condensation, transpiration", why="The rain flows over the land. It does not soak in, condense or transpire along the way described."),
            C("Condensation, evaporation, infiltration", why="Evaporation happens before rain, not after it reaches the sea."),
            C("Precipitation, surface runoff, river flow to the sea", correct=True),
            C("Transpiration, precipitation, infiltration", why="Transpiration is by plants, and the water in the question flowed over the surface."),
        ], steps=[S("Follow the water", text="Rain falls (precipitation), flows over the ground (surface runoff) into a stream (river flow) and reaches the sea.")],
           concept="Pathways of the water cycle", skill="Application", hint="Follow the water from the sky to the sea."),
        MC("Why is the fresh water that people can easily use so scarce, though the earth has so much water?", [
            C("Most water is salty, and most fresh water is frozen or deep underground", correct=True),
            C("Because rivers have all dried up", why="Rivers still flow. They simply hold a tiny share of the water."),
            C("Because rain does not fall over land", why="Rain does fall on land. The point is that most water is not in an easy-to-use store."),
            C("Because plants use all the water", why="Plants use some water, but this does not explain the global distribution."),
        ], steps=[S("Reason", text="About 97 percent of water is salty, and of the fresh water most is ice or groundwater.")],
           concept="Availability of fresh water", skill="Reasoning", hint="Think about the oceans and the ice caps."),
        MC("Look at the figure. Which statement about the earth's fresh water is correct?", [
            C("Lakes, soil, rivers and the air together hold more fresh water than groundwater", why="The figure shows that they hold less than 1 percent of fresh water."),
            C("Ice holds less fresh water than groundwater", why="Ice holds about two-thirds, which is more than groundwater."),
            C("The oceans hold most of the fresh water", why="The oceans are salty. They are not part of the fresh water bar."),
            C("Groundwater holds more fresh water than lakes, rivers and the air together", correct=True),
        ], steps=[S("Read the bar", text="The fresh water bar shows ice about two-thirds, groundwater almost one-third, and a tiny share for lakes, soil, rivers and the air.")],
           concept="Reading a bar chart of water stores", skill="Interpretation", hint="Compare the length of the groundwater section with the thin blue section.",
           diagram="f5g-wx-global-water.svg", diagram_alt="Two bars: oceans about 97 percent and fresh water about 3 percent of all water; fresh water split into ice about two-thirds, groundwater almost one-third, and a tiny share for lakes, soil, rivers and the air."),
    ]))

# ------------------------------------------------------------------ 2. The drainage basin
SETS.append(practice_set(
    module=MODULE, topic=HC,
    title="The drainage basin: parts, stores and flows",
    lesson="wx-the-drainage-basin-system",
    questions=[
        MC("What is the high ground that separates one drainage basin from the next called?", [
            C("Confluence", why="The confluence is the point where two rivers meet."),
            C("Watershed", correct=True),
            C("Tributary", why="A tributary is a smaller river that joins a larger one."),
            C("Mouth", why="The mouth is where a river ends."),
        ], steps=[S("Recall", text="The watershed is the boundary of a basin.")],
           concept="Watershed", skill="Recall", hint="It is a boundary, not a river."),
        MC("The point where two rivers meet is called a:", [
            C("Source", why="The source is where a river begins."),
            C("Watershed", why="The watershed is the boundary of the basin."),
            C("Confluence", correct=True),
            C("Channel", why="The channel is the bed and banks along which a river flows."),
        ], steps=[S("Recall", text="A confluence is where two rivers join.")],
           concept="Parts of a river system", skill="Recall", hint="Think of the words 'flow together'."),
        MC("Look at the figure. Which labelled item is an OUTPUT from the drainage basin?", [
            C("Precipitation", why="Precipitation is an input to the basin."),
            C("Surface runoff", why="Surface runoff is a flow inside the basin, not the water leaving it."),
            C("Soil moisture store", why="This is a store inside the basin."),
            C("River flow to the sea", correct=True),
        ], steps=[S("Inputs and outputs", text="Outputs leave the basin: evaporation, transpiration and the river flow to the sea.")],
           concept="Inputs and outputs of a basin", skill="Interpretation", hint="Outputs cross the boundary and leave the basin.",
           diagram="f5g-wx-basin-system.svg", diagram_alt="Cross-section of a drainage basin with precipitation as input, stores, flows, and outputs of transpiration, evaporation and river flow to the sea."),
        MC("Which of these is a STORE of water in a drainage basin?", [
            C("Soil moisture", correct=True),
            C("Stemflow", why="Stemflow is a flow of water down plant stems."),
            C("Surface runoff", why="Surface runoff is a flow over the ground."),
            C("Percolation", why="Percolation is a flow downwards through soil and rock."),
        ], steps=[S("Store or flow?", text="A store holds water. Soil moisture is water held in the soil. The others are movements (flows).")],
           concept="Stores and flows", skill="Concept", hint="A store is a place where water stays for a while."),
        NUM("A drainage basin receives 1200 mm of precipitation in a year. Evaporation and transpiration remove 700 mm. If the stores do not change, how many mm of water leave as river flow?", 500,
            steps=[S("Inputs minus other outputs", math=r"1200 - 700 = 500", text="River flow is 500 mm.")],
            unit="mm", concept="Water balance of a basin", skill="Calculation", hint="Input must equal total output if the stores do not change."),
        MC("Which flow is the SLOWEST way for water to reach a river?", [
            C("Surface runoff", why="Surface runoff is the fastest flow."),
            C("Stemflow", why="Stemflow quickly leads water down a trunk."),
            C("Groundwater flow", correct=True),
            C("Throughfall", why="Throughfall is rain dripping through leaves, which is quick."),
        ], steps=[S("Compare speeds", text="Groundwater moves very slowly through rock. Surface runoff is fastest.")],
           concept="Speed of flows", skill="Concept", hint="Which flow takes place deep underground?"),
        MC("A hillside near Bafoussam is cleared of forest. What is the most likely effect on the nearby river?", [
            C("Less surface runoff and fewer floods", why="Without trees, less rain is intercepted, so runoff increases."),
            C("No change at all", why="Vegetation affects interception, infiltration and transpiration."),
            C("More infiltration and slower flow", why="Roots help infiltration. Without them, less water soaks in."),
            C("More surface runoff and a higher risk of flooding", correct=True),
        ], steps=[S("Reason", text="Less interception and less infiltration mean more water runs quickly over the surface into the river.")],
           concept="Vegetation and runoff", skill="Application", hint="Think about what trees do to rain before it reaches the ground."),
        MC("A river in the highlands still flows in the dry season when it does not rain for weeks. Which part of the basin system explains this?", [
            C("Interception store", why="This store is small and empties quickly."),
            C("Groundwater store feeding the river by groundwater flow", correct=True),
            C("Surface runoff", why="Surface runoff stops when the rain stops."),
            C("Stemflow", why="Stemflow only happens when it rains."),
        ], steps=[S("Reason", text="Groundwater is released slowly into rivers, so they keep flowing between rains.")],
           concept="Groundwater and river flow", skill="Reasoning", hint="Which store releases water slowly?"),
    ]))

# ------------------------------------------------------------------ 3. Structure of the atmosphere
SETS.append(practice_set(
    module=MODULE, topic=ATM,
    title="The atmosphere: layers and characteristics",
    lesson="wx-structure-of-the-atmosphere",
    questions=[
        MC("Which gas makes up most of the dry air in the atmosphere?", [
            C("Oxygen", why="Oxygen is about 21 percent of the air, the second largest part."),
            C("Carbon dioxide", why="Carbon dioxide is a very small part of the air."),
            C("Nitrogen", correct=True),
            C("Water vapour", why="Water vapour varies, but it is much less than nitrogen."),
        ], steps=[S("Recall", text="Nitrogen is about 78 percent and oxygen about 21 percent of dry air.")],
           concept="Composition of the atmosphere", skill="Recall", hint="It is more than three-quarters of the air."),
        NUM("In the troposphere temperature falls by about 6 degrees C for every 1000 m. At sea level the temperature is 28 degrees C. What is the temperature at a height of 2000 m? (in degrees C)", 16,
            steps=[S("Fall in temperature", math=r"2 \times 6 = 12", text="2000 m is two lots of 1000 m."),
                   S("Subtract", math=r"28 - 12 = 16", text="The temperature is about 16 degrees C.")],
            unit="degrees C", concept="Temperature change in the troposphere", skill="Calculation", hint="How many times does 1000 m go into 2000 m?"),
        MC("Which layer of the atmosphere lies directly above the troposphere?", [
            C("Stratosphere", correct=True),
            C("Mesosphere", why="The mesosphere is above the stratosphere."),
            C("Thermosphere", why="The thermosphere is the outer layer, far above."),
            C("The ozone layer", why="Ozone is a zone inside the stratosphere, not a separate layer."),
        ], steps=[S("Order the layers", text="From the ground: troposphere, stratosphere, mesosphere, thermosphere.")],
           concept="Layers of the atmosphere", skill="Recall", hint="The order from the ground is: tropo-, strato-, meso-, thermo-."),
        MC("Why does temperature rise with height in the stratosphere?", [
            C("The air is closer to the sun", why="The sun is far away, and a few kilometres of height make little difference."),
            C("Heat comes up from the ground", why="Heat from the ground warms the lower troposphere."),
            C("There are many clouds", why="The stratosphere has very few clouds."),
            C("The ozone layer absorbs ultraviolet rays and warms the air", correct=True),
        ], steps=[S("Explain", text="Ozone absorbs ultraviolet rays from the sun. The energy warms the air.")],
           concept="The stratosphere and ozone", skill="Concept", hint="What does ozone do with the sun's rays?"),
        MC("Which layer is the coldest, with temperatures of about minus 90 degrees C?", [
            C("Troposphere", why="The top of the troposphere is cold, but the mesosphere is colder."),
            C("Mesosphere", correct=True),
            C("Stratosphere", why="The stratosphere warms with height."),
            C("Thermosphere", why="Temperature rises again in the thermosphere."),
        ], steps=[S("Read the graph", text="Temperature falls through the mesosphere and is lowest at the top, about minus 90 degrees C.")],
           concept="Temperature in the layers", skill="Recall", hint="It is the layer above the stratosphere."),
        MC("Look at the figure. About how high is the top of the troposphere on average?", [
            C("5 km", why="The troposphere is thicker than that on average."),
            C("50 km", why="50 km is the top of the stratosphere."),
            C("12 km", correct=True),
            C("85 km", why="85 km is the top of the mesosphere."),
        ], steps=[S("Read the height scale", text="The first boundary, the tropopause, is at about 12 km.")],
           concept="Heights of the layers", skill="Interpretation", hint="Find the first dashed line above the ground.",
           diagram="f5g-wx-atmosphere-layers.svg", diagram_alt="A column of atmosphere layers with heights 0, 12, 50, 85 and 100 km, and a graph of temperature against height."),
        MC("Why does nearly all weather occur in the troposphere?", [
            C("It holds almost all the water vapour and the air rises and mixes there", correct=True),
            C("It is the highest layer", why="It is the lowest layer."),
            C("It contains the ozone layer", why="The ozone layer is in the stratosphere."),
            C("It is the warmest layer", why="Its temperature falls with height, and the top is very cold."),
        ], steps=[S("Reason", text="Clouds and rain need water vapour and rising air. Both are found in the troposphere.")],
           concept="Weather in the troposphere", skill="Reasoning", hint="Think about what clouds are made of."),
        MC("Which statement about the atmosphere is correct?", [
            C("It has a sharp upper edge", why="The atmosphere thins out gradually into space."),
            C("It has no effect on the earth's temperature", why="It acts like a blanket and keeps the earth warm."),
            C("The air is thinnest at the earth's surface", why="The air is thickest at the surface."),
            C("The ozone layer protects living things from ultraviolet rays", correct=True),
        ], steps=[S("Check each option", text="The ozone layer in the stratosphere absorbs most ultraviolet rays.")],
           concept="Importance of the atmosphere", skill="Concept", hint="Think about how the atmosphere protects living things."),
    ]))

# ------------------------------------------------------------------ 4. Weather versus climate
SETS.append(practice_set(
    module=MODULE, topic=WC,
    title="Weather and climate: meanings and elements",
    lesson="wx-weather-versus-climate-and-weather-elements",
    questions=[
        MC("Climate is best described as:", [
            C("The average weather of a place over a long period", correct=True),
            C("The weather at a place today", why="This describes weather, not climate."),
            C("The weather forecast for next week", why="A forecast describes expected weather for a short time."),
            C("The rainfall of one year", why="One year is too short for climate."),
        ], steps=[S("Recall", text="Climate is the average weather over a long period, usually about 30 years.")],
           concept="Climate defined", skill="Recall", hint="It is about averages over many years."),
        NUM("Climate is usually worked out from weather records over at least how many years?", 30,
            steps=[S("Recall", text="The usual period for describing a climate is 30 years.")],
            unit="years", concept="Climate defined", skill="Recall", hint="It is a period of about three decades."),
        MC("Which statement describes weather, not climate?", [
            C("Maroua has a long dry season.", why="This describes a repeated pattern over many years: climate."),
            C("Kribi is hot and wet for most of the year.", why="This describes a long-term pattern: climate."),
            C("There was a storm over Buea on Tuesday afternoon.", correct=True),
            C("Garoua is usually hotter than Douala.", why="This compares the usual conditions of two places: climate."),
        ], steps=[S("Check the time scale", text="A storm on Tuesday is one event at one time. That is weather.")],
           concept="Weather versus climate", skill="Concept", hint="Look for one place and one particular time."),
        MC("Which instrument measures wind speed?", [
            C("Wind vane", why="A wind vane shows the direction of the wind, not its speed."),
            C("Anemometer", correct=True),
            C("Barometer", why="A barometer measures air pressure."),
            C("Hygrometer", why="A hygrometer measures humidity."),
        ], steps=[S("Recall", text="An anemometer measures wind speed.")],
           concept="Weather instruments", skill="Recall", hint="Its cups spin in the wind."),
        MC("Which weather element is measured in oktas?", [
            C("Humidity", why="Humidity is measured in percent."),
            C("Rainfall", why="Rainfall is measured in millimetres."),
            C("Air pressure", why="Air pressure is measured in hectopascals."),
            C("Cloud cover", correct=True),
        ], steps=[S("Recall", text="Cloud cover is judged by eye, in oktas (eighths of the sky).")],
           concept="Units of weather elements", skill="Recall", hint="Think of eighths of the sky."),
        MC("Which pair is correctly matched?", [
            C("Humidity: hours", why="Sunshine is measured in hours. Humidity is measured in percent."),
            C("Temperature: millimetres", why="Millimetres measure rainfall. Temperature is in degrees Celsius."),
            C("Rainfall: millimetres", correct=True),
            C("Air pressure: degrees Celsius", why="Pressure is measured in hectopascals."),
        ], steps=[S("Check each pair", text="Rainfall is measured in millimetres with a rain gauge.")],
           concept="Units of weather elements", skill="Concept", hint="Think of the rain gauge."),
        MC("Which is a correct difference between weather and climate?", [
            C("Weather changes quickly, climate changes only slowly", correct=True),
            C("Weather is an average, climate is one day's conditions", why="This is reversed."),
            C("Weather is measured over 30 years", why="Climate is found from long records."),
            C("Climate changes every hour", why="Weather changes every hour. Climate changes slowly."),
        ], steps=[S("Contrast", text="Weather is short term and changes rapidly. Climate is long term.")],
           concept="Weather versus climate", skill="Concept", hint="Compare how quickly each one changes."),
        MC("A student records the temperature every day for two weeks and says that she has found the climate of her town. What is wrong with this?", [
            C("Temperature is not a weather element", why="Temperature is one of the main weather elements."),
            C("She should have used a barometer", why="The instrument is not the problem."),
            C("Climate must be measured only in winter", why="Climate uses records over a full range of seasons and years."),
            C("Two weeks is too short. Climate needs records over about 30 years", correct=True),
        ], steps=[S("Reason", text="Two weeks of data show weather. Climate is the average over a long period.")],
           concept="Weather versus climate", skill="Application", hint="How long a record is needed for climate?"),
    ]))


# ------------------------------------------------------------------ 5. Weather instruments
SETS.append(practice_set(
    module=MODULE, topic=WC,
    title="Weather instruments and the Stevenson screen: use and siting",
    lesson="wx-weather-instruments-and-the-stevenson-screen",
    questions=[
        MC("Which instrument records the highest and lowest temperature since it was last set?", [
            C("Barometer", why="A barometer measures air pressure."),
            C("Maximum-minimum thermometer", correct=True),
            C("Hygrometer", why="A hygrometer measures humidity."),
            C("Sunshine recorder", why="A sunshine recorder measures hours of sunshine."),
        ], steps=[S("Recall", text="The maximum-minimum thermometer has two markers that stay at the highest and lowest points.")],
           concept="Maximum-minimum thermometer", skill="Recall", hint="The name tells you what it records."),
        NUM("A wet and dry bulb hygrometer shows 28 degrees C on the dry bulb and 23 degrees C on the wet bulb. What is the difference between the two readings, in degrees C?", 5,
            steps=[S("Subtract", math=r"28 - 23 = 5", text="The difference is 5 degrees C. It is used with tables to find the relative humidity.")],
            unit="degrees C", concept="Hygrometer readings", skill="Calculation", hint="Dry bulb reading minus wet bulb reading."),
        MC("The head of a wind vane points to the south-east. From which direction is the wind blowing?", [
            C("North-west", why="That is the direction the wind is going towards, not where it comes from."),
            C("North-east", why="The head points south-east, not north-east."),
            C("South-east", correct=True),
            C("South-west", why="The head points south-east, not south-west."),
        ], steps=[S("Rule", text="The head of a wind vane points into the wind, so it shows where the wind comes from: the south-east.")],
           concept="Wind vane", skill="Application", hint="A wind vane points into the wind."),
        MC("What does 1 mm of rainfall mean?", [
            C("1 litre of water on every square metre of ground", correct=True),
            C("1 litre of water on every square kilometre", why="The area is a square metre, not a square kilometre."),
            C("1 cm of water on the ground", why="1 mm is one tenth of a centimetre."),
            C("1 millilitre of water on each square metre", why="1 mm is 1 litre per square metre, which is 1000 millilitres."),
        ], steps=[S("Meaning", text="A depth of 1 mm over 1 square metre is a volume of 1 litre.")],
           concept="Rain gauge units", skill="Concept", hint="Think of a layer of water 1 mm deep over a square metre."),
        NUM("A school roof has an area of 20 square metres. A rain gauge records 15 mm of rain in one storm. How many litres of rain fell on the roof? (1 mm of rain is 1 litre on each square metre.)", 300,
            steps=[S("Use the rule", math=r"20 \times 15 = 300", text="20 square metres times 15 litres per square metre is 300 litres.")],
            unit="litres", concept="Rainfall and volume of water", skill="Calculation", hint="Each square metre gets 1 litre for every mm of rain."),
        MC("Why does a Stevenson screen have louvred (slatted) sides?", [
            C("To make it look attractive", why="The slats have a scientific purpose."),
            C("To keep it from falling over", why="The legs support the screen, not the slats."),
            C("To heat the thermometers", why="The screen is built to avoid false heating."),
            C("To let air flow through while keeping out rain and direct sun", correct=True),
        ], steps=[S("Explain", text="The slats let air pass so the thermometers show the true air temperature, and stop rain and direct sunshine.")],
           concept="Stevenson screen", skill="Concept", hint="Think about air and sun."),
        MC("Which is the best site for a school weather station?", [
            C("On a concrete yard beside the classroom wall", why="Concrete and walls heat up and change the air temperature."),
            C("Flat, open ground with short grass, away from buildings and trees", correct=True),
            C("Under a mango tree", why="A tree gives shade and blocks rain and wind."),
            C("On the school roof", why="The roof is hot and windy and does not give true readings."),
        ], steps=[S("Siting rule", text="An open, flat, grassed site gives readings that match the real weather around.")],
           concept="Siting a weather station", skill="Application", hint="Avoid anything that shades or heats the instruments."),
        MC("Look at the figure. Which feature of the Stevenson screen keeps the instruments away from the hot ground?", [
            C("The white paint", why="The paint reflects sunlight, but does not lift the box."),
            C("The door", why="The door lets the observer read the instruments."),
            C("Its legs, which raise it to about 1.25 m", correct=True),
            C("The louvres", why="The louvres let air through."),
        ], steps=[S("Read the figure", text="The legs lift the box about 1.25 m above the grass, away from the hot ground.")],
           concept="Stevenson screen", skill="Interpretation", hint="Look at what stands between the box and the grass.",
           diagram="f5g-wx-stevenson-screen.svg", diagram_alt="A white louvred box with a double roof and a door, on legs about 1.25 metres high standing on short grass."),
    ]))

# ------------------------------------------------------------------ 6. Recording and presenting data
SETS.append(practice_set(
    module=MODULE, topic=WC,
    title="Weather data, climate graphs and simple weather maps",
    lesson="wx-recording-presenting-weather-data-and-simple-weather-maps",
    questions=[
        MC("Look at the climate graph for Kuma (a fictitious station). What is the total rainfall of the three driest months, January, February and December?", [
            C("50 mm", why="This leaves out December: 18 + 32 = 50."),
            C("95 mm", why="95 mm is the rainfall of March, not the total for the dry months."),
            C("120 mm", why="The three bars add up to less than this."),
            C("72 mm", correct=True),
        ], steps=[S("Read the bars", text="January 18, February 32, December 22."),
                  S("Add", math=r"18 + 32 + 22 = 72", text="The total is 72 mm.")],
           concept="Totals from a climate graph", skill="Calculation", hint="Read the three small bars and add them.",
           diagram="f5g-wx-climate-graph.svg", diagram_alt="Climate graph of the fictitious station Kuma. Monthly rainfall in mm: 18, 32, 95, 152, 208, 262, 305, 335, 248, 176, 62, 22. Temperature line between 24 and 28 degrees C."),
        NUM("Use the climate graph for Kuma. What is the mean monthly rainfall from June to September (262, 305, 335 and 248 mm)? Give your answer in mm.", 287.5, tolerance=0.1,
            steps=[S("Add", math=r"262 + 305 + 335 + 248 = 1150"),
                   S("Divide by 4", math=r"1150 \div 4 = 287.5", text="The mean is 287.5 mm per month.")],
            unit="mm", concept="Mean from a climate graph", skill="Calculation", hint="Total divided by the number of months.",
            diagram="f5g-wx-climate-graph.svg", diagram_alt="Climate graph of the fictitious station Kuma with monthly rainfall bars and a temperature line."),
        MC("In which month does Kuma receive the most rain, and how much?", [
            C("July, 305 mm", why="July is wet, but August has more."),
            C("August, 335 mm", correct=True),
            C("September, 248 mm", why="September is lower than August."),
            C("June, 262 mm", why="June is lower than August."),
        ], steps=[S("Find the tallest bar", text="The tallest bar is August, at 335 mm.")],
           concept="Reading a climate graph", skill="Interpretation", hint="Find the tallest bar.",
           diagram="f5g-wx-climate-graph.svg", diagram_alt="Climate graph of Kuma with the tallest bar in August."),
        NUM("The mean monthly temperatures of a town in four months are 24, 26, 28 and 22 degrees C. What is the mean of these four values, in degrees C?", 25,
            steps=[S("Add", math=r"24 + 26 + 28 + 22 = 100"),
                   S("Divide by 4", math=r"100 \div 4 = 25", text="The mean is 25 degrees C.")],
            unit="degrees C", concept="Calculating a mean", skill="Calculation", hint="Add the four values, then divide by 4."),
        MC("Which type of graph is best for showing monthly rainfall totals?", [
            C("A bar graph", correct=True),
            C("A line graph joining the points", why="A line suggests a continuous change, which suits temperature better than monthly totals."),
            C("A weather map", why="A weather map shows conditions at one time, not monthly totals."),
            C("A table with no graph", why="A table is useful but is not a graph."),
        ], steps=[S("Choose", text="Each month's total is a separate amount, so separate bars are used.")],
           concept="Choosing a graph", skill="Concept", hint="Each month is a separate amount."),
        MC("Look at the weather map of Mbanga (a fictitious region). Which station has an overcast sky and rain?", [
            C("Kuma", why="Kuma has a clear sky."),
            C("Mbanga", why="Mbanga has half cloud and no rain symbol."),
            C("Ekoa", correct=True),
            C("Dibo", why="Dibo has half cloud and no rain symbol."),
        ], steps=[S("Read the symbols", text="Ekoa has a filled circle (overcast) and rain dots.")],
           concept="Reading a weather map", skill="Interpretation", hint="Look for a filled circle with rain dots.",
           diagram="f5g-wx-weather-map.svg", diagram_alt="Weather map of fictitious Mbanga with four stations: Kuma clear 33 degrees, Mbanga half cloud 30, Ekoa overcast with rain 24, Dibo half cloud 27, and isobars."),
        MC("On the weather map, from which direction does the wind blow at Mbanga?", [
            C("South-west", why="The staff points up and to the right, not to the south-west."),
            C("North-west", why="The staff points to the north-east, not the north-west."),
            C("South", why="The staff does not point south."),
            C("North-east", correct=True),
        ], steps=[S("Read the staff", text="The staff points from the circle to the north-east. It shows where the wind comes FROM.")],
           concept="Wind on a weather map", skill="Interpretation", hint="The staff points to where the wind comes from.",
           diagram="f5g-wx-weather-map.svg", diagram_alt="Weather map of fictitious Mbanga. The wind staff at Mbanga points to the upper right (north-east)."),
        NUM("On the weather map, the temperatures are Kuma 33, Mbanga 30, Dibo 27 and Ekoa 24 degrees C. What is the difference between the hottest and the coolest station, in degrees C?", 9,
            steps=[S("Subtract", math=r"33 - 24 = 9", text="Kuma is the hottest and Ekoa the coolest, so the difference is 9 degrees C.")],
            unit="degrees C", concept="Range from a weather map", skill="Calculation", hint="Hottest minus coolest.",
            diagram="f5g-wx-weather-map.svg", diagram_alt="Weather map of fictitious Mbanga showing temperatures at four stations."),
    ]))

# ------------------------------------------------------------------ 7. Precipitation and its forms
SETS.append(practice_set(
    module=MODULE, topic=FC,
    title="Precipitation and its forms: definitions and formation",
    lesson="wx-precipitation-and-its-forms",
    questions=[
        MC("Precipitation is best defined as:", [
            C("Water vapour in the air", why="Water vapour is a gas. Precipitation is water that falls."),
            C("Water that evaporates from the sea", why="That is evaporation."),
            C("Water that falls from the atmosphere to the ground as liquid or solid", correct=True),
            C("Water that soaks into the soil", why="That is infiltration."),
        ], steps=[S("Recall", text="Precipitation includes rain, hail, snow and sleet.")],
           concept="Precipitation defined", skill="Recall", hint="It involves water that falls."),
        MC("Which form of precipitation is a hard ball of ice, built up in layers in a storm cloud?", [
            C("Hail", correct=True),
            C("Sleet", why="Sleet is rain mixed with partly melted snow."),
            C("Snow", why="Snow is soft ice crystals."),
            C("Mist", why="Mist is tiny droplets near the ground."),
        ], steps=[S("Recall", text="Hailstones grow layer by layer in strong rising air in storm clouds.")],
           concept="Hail", skill="Recall", hint="Think of ice falling in hot weather."),
        MC("What must happen to air so that its water vapour condenses?", [
            C("It must be heated", why="Heating allows air to hold more vapour."),
            C("It must be blown by wind", why="Wind alone does not cause condensation."),
            C("It must become drier", why="Drier air has less vapour."),
            C("It must be cooled to its dew point", correct=True),
        ], steps=[S("Explain", text="Cooler air holds less vapour. Below the dew point the extra vapour condenses.")],
           concept="Condensation", skill="Concept", hint="Think of drops on a cold bottle."),
        MC("In the middle panel of the figure, the droplets on the grass are called:", [
            C("Fog", why="Fog is a cloud of droplets in the air near the ground."),
            C("Dew", correct=True),
            C("Hail", why="Hail is ice that falls from storm clouds."),
            C("Sleet", why="Sleet is rain and partly melted snow."),
        ], steps=[S("Identify", text="Drops that form on cool surfaces at night are dew.")],
           concept="Dew", skill="Interpretation", hint="They form on the surface, on clear calm nights.",
           diagram="f5g-wx-condensation-forms.svg", diagram_alt="Three scenes: cloud and rain, dew as droplets on grass at night, and fog as a cloud at ground level among trees."),
        MC("Sleet is:", [
            C("A mixture of rain and partly melted snow", correct=True),
            C("A thick layer of cloud at ground level", why="That is fog."),
            C("Ice that forms layers inside a storm cloud", why="That is hail."),
            C("Water drops on grass", why="That is dew."),
        ], steps=[S("Recall", text="Sleet forms when snow melts partly as it falls.")],
           concept="Sleet", skill="Recall", hint="It combines two other forms."),
        MC("How does fog differ from mist?", [
            C("Fog is made of ice, mist is made of water", why="Both are made of tiny water droplets."),
            C("Fog falls from clouds, mist does not", why="Neither falls like rain."),
            C("Fog is thicker: visibility is under 1 km. Mist is thinner", correct=True),
            C("Fog forms only at midday", why="Fog usually forms on calm, clear nights."),
        ], steps=[S("Compare", text="Both are clouds at ground level. Fog is denser and reduces visibility to under 1 km.")],
           concept="Fog and mist", skill="Concept", hint="Think about how far you can see."),
        MC("On a clear, calm night the grass is dry at 8 p.m. and wet at 6 a.m., although it did not rain. What is the best explanation?", [
            C("The grass absorbed water from the sky", why="Dew does not fall from the sky."),
            C("Hail melted on the grass", why="No hail is involved."),
            C("The grass and the air touching it cooled to the dew point, so vapour condensed on the grass", correct=True),
            C("Strong winds blew water onto the grass", why="Dew forms on calm nights, not windy ones."),
        ], steps=[S("Reason", text="On clear nights the ground loses heat and cools. Air touching it reaches the dew point, so dew forms.")],
           concept="Formation of dew", skill="Application", hint="What happens to the ground on a clear night?"),
        NUM("A house roof has an area of 50 square metres. A storm brings 12 mm of rain. How many litres of water fall on the roof? (1 mm of rain is 1 litre on each square metre.)", 600,
            steps=[S("Use the rule", math=r"50 \times 12 = 600", text="50 square metres times 12 litres per square metre is 600 litres.")],
            unit="litres", concept="Rainfall and volume of water", skill="Calculation", hint="Each square metre gets 1 litre for every mm of rain."),
    ]))

# ------------------------------------------------------------------ 8. The three types of rainfall
SETS.append(practice_set(
    module=MODULE, topic=FC,
    title="The three types of rainfall: causes and places",
    lesson="wx-the-three-types-of-rainfall",
    questions=[
        MC("Which type of rainfall is caused by strong heating of the ground, so that warm air rises?", [
            C("Relief rainfall", why="Relief rain is caused by highland forcing air upwards."),
            C("Convectional rainfall", correct=True),
            C("Frontal rainfall", why="Frontal rain happens where warm and cold air masses meet."),
            C("Dew", why="Dew is not a type of rainfall."),
        ], steps=[S("Recall", text="Convection is the rising of heated air. It gives convectional rain.")],
           concept="Convectional rainfall", skill="Recall", hint="The cause is heat from the ground."),
        MC("What is the side of a mountain that faces the wind called?", [
            C("Leeward side", why="The leeward side is the sheltered side."),
            C("Rain shadow", why="The rain shadow is the dry area on the sheltered side."),
            C("Front", why="A front is the boundary between two air masses."),
            C("Windward side", correct=True),
        ], steps=[S("Recall", text="Windward means facing the wind, and this is the wet side.")],
           concept="Windward and leeward", skill="Recall", hint="Wind plus 'ward', which means toward."),
        MC("Look at the figure. Which statement explains the dry area on the leeward side?", [
            C("Air sinks and warms, so little cloud forms", correct=True),
            C("Air rises and cools there", why="Air rises on the windward side, not the leeward side."),
            C("Cold air meets warm air there", why="This describes a front."),
            C("The sea is close to this side", why="In the figure the sea is on the windward side."),
        ], steps=[S("Read the figure", text="After crossing the mountain the air sinks and warms. Warm air can hold more vapour, so cloud and rain are rare.")],
           concept="Rain shadow", skill="Interpretation", hint="What happens to air that goes down a slope?",
           diagram="f5g-wx-relief-rain.svg", diagram_alt="Moist air from the sea rises up a mountain, forms cloud and rain on the windward side, and sinks on the dry leeward side."),
        MC("Which type of rainfall is important on the slopes of Mount Cameroon?", [
            C("Convectional rainfall only", why="Convection may add to it, but the mountain is the main cause of the heavy rain."),
            C("Frontal rainfall", why="Fronts are not the main cause in Cameroon."),
            C("Relief (orographic) rainfall", correct=True),
            C("Dew", why="Dew is not a type of rainfall."),
        ], steps=[S("Reason", text="Moist winds from the Atlantic are forced up the mountain. This is relief rain.")],
           concept="Relief rainfall in Cameroon", skill="Application", hint="Moist sea air meets a high mountain."),
        MC("Frontal rainfall forms when:", [
            C("The ground is heated by the sun", why="That describes convectional rain."),
            C("Warm air is forced to rise over cold air", correct=True),
            C("Air is forced to rise over a mountain", why="That describes relief rain."),
            C("Air touches a cold surface at night", why="That produces dew."),
        ], steps=[S("Recall", text="At a front, warm light air rises over cold dense air, cools and condenses.")],
           concept="Frontal rainfall", skill="Concept", hint="Two air masses with different temperatures meet."),
        MC("Look at the figure. In which order do the steps of convectional rainfall happen?", [
            C("Rain, cooling, rising, heating", why="This is the reverse of the real order."),
            C("Cooling, heating, rain, rising", why="Heating must come first."),
            C("Heating, rising, cooling and condensation, rain", correct=True),
            C("Rising, heating, rain, cooling", why="Air rises because it has been heated."),
        ], steps=[S("Follow the numbers", text="1 Sun heats ground. 2 Warm air rises. 3 Air cools and condenses. 4 Heavy rain.")],
           concept="Convectional rainfall", skill="Interpretation", hint="Follow the numbered steps.",
           diagram="f5g-wx-convectional-rain.svg", diagram_alt="Sun heats the ground, warm air rises, cools and condenses into a tall cloud, and heavy rain falls."),
        MC("Look at the figure. What happens to the warm air at a front?", [
            C("It sinks below the cold air", why="Warm air is lighter, so it cannot sink below cold air."),
            C("It mixes completely with the cold air", why="The two air masses stay separate along the front."),
            C("It stays still", why="The warm air is forced to move upwards."),
            C("It rises over the cold air, cools, and forms cloud and rain", correct=True),
        ], steps=[S("Read the figure", text="The warm air slides up over the sloping boundary of cold air. It cools and clouds and rain form.")],
           concept="Frontal rainfall", skill="Interpretation", hint="Which air is lighter?",
           diagram="f5g-wx-frontal-rain.svg", diagram_alt="Cold dense air forms a wedge near the ground. Warm light air rises over it along a sloping front, with cloud and rain along the front."),
        MC("Two towns are 30 km apart on opposite sides of a highland. The town on the side facing the sea gets heavy rain. The other town gets much less. What is the best explanation?", [
            C("The second town is in the rain shadow, because air sinks and warms on the leeward side", correct=True),
            C("The second town is hotter, so more rain evaporates", why="The difference is caused by the highland, not the heat of the town."),
            C("Convectional rainfall happens only in the first town", why="The pattern is explained by the highland, not by convection."),
            C("Fronts never reach the second town", why="The question describes relief rain, not frontal rain."),
        ], steps=[S("Reason", text="Moist sea air rises on the windward side and gives rain. It sinks, warms and dries on the leeward side.")],
           concept="Relief rainfall and rain shadow", skill="Reasoning", hint="Think about what the highland does to the moving air."),
    ]))
