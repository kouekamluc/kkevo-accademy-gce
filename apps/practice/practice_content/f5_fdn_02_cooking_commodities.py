"""Practice sets for Form 5 Food and Nutrition: Principles & Methods of Cooking, and Food Commodities,
Flour Mixtures & Raising Agents (one set per lesson)."""

from .dsl import *  # noqa: F403

COURSE = ("food-and-nutrition", "form-5")

M3 = "Principles & Methods of Cooking"
M4 = "Food Commodities, Flour Mixtures & Raising Agents"

SETS = []

# ------------------------------------------------------------------ 1. Why we cook and how heat travels
SETS.append(practice_set(
    module=M3, topic="Why we cook and how heat travels",
    title="Reasons for cooking and heat transfer",
    lesson="fdn2-why-we-cook-and-heat-transfer",
    questions=[
        MC("Which of these is a reason for cooking food?", [
            C("To destroy all the protein in the food", why="Cooking changes protein but does not remove it; proteins remain as nutrients."),
            C("To make the food safe by killing harmful micro-organisms", correct=True),
            C("To make the food heavier", why="Cooking does not aim to add weight; it often loses water."),
            C("To remove all vitamins", why="Cooking may lose some vitamins, but that is a disadvantage, not a reason."),
        ], steps=[S("Recall", text="Cooking makes food safe, digestible, tasty, attractive and varied.")],
           concept="Reasons for cooking", skill="Recall", hint="Think of what heat does to bacteria."),
        MC("Heat passing through the metal base of a pan to the food is called", [
            C("conduction", correct=True),
            C("convection", why="Convection needs currents in a liquid or gas."),
            C("radiation", why="Radiation travels as rays, not through a solid by contact."),
            C("evaporation", why="Evaporation is a liquid changing to a gas, not a way heat travels."),
        ], steps=[S("Identify", text="Movement of heat through a solid by contact between particles is conduction.")],
           concept="Conduction", skill="Recall", hint="Which method needs the particles to touch?"),
        MC("Why does hot water at the bottom of a pot rise?", [
            C("It is heavier than the cold water above", why="It has become lighter, not heavier, when heated."),
            C("It is lighter than the cooler water above", correct=True),
            C("It is pushed by rays from the fire", why="Rays are radiation; the rising water is a convection current."),
            C("It is conducted upwards by the pot", why="The pot conducts heat into the water, but the rising is the water moving."),
        ], steps=[S("Reason", text="Heated water expands and becomes lighter, so it rises while cooler, heavier water sinks. This circulation is convection.")],
           concept="Convection currents", skill="Concept", hint="Compare the weight of hot and cool water."),
        MC("Fish is cooked over glowing charcoal. The main type of heat transfer to the fish is", [
            C("conduction", why="Conduction needs touching; the coals are some distance from the fish."),
            C("convection", why="Hot air also helps, but the main heating is from the rays."),
            C("evaporation", why="This is not a type of heat transfer."),
            C("radiation", correct=True),
        ], steps=[S("Identify", text="Rays from the glowing coals strike the fish with no contact needed. This is radiation.")],
           concept="Radiation in grilling", skill="Application", hint="What reaches the fish without touching it?"),
        MC("Why is a wooden spoon used to stir a hot sauce?", [
            C("Wood is an insulator, so the handle does not become too hot", correct=True),
            C("Wood is a good conductor, so it heats the sauce", why="A good conductor would burn your hand."),
            C("Wood radiates heat to the sauce", why="Wood does not help to heat the sauce."),
            C("Wood does not touch the sauce", why="A spoon does touch the sauce; the reason is insulation."),
        ], steps=[S("Reason", text="Wood conducts heat very slowly, so the part in the hand stays cool.")],
           concept="Conductors and insulators", skill="Concept", hint="Think of what happens to a metal spoon left in a hot pot."),
        MC("A cook says: 'Boiling a yam only uses conduction.' Which statement corrects her?", [
            C("Boiling uses radiation only", why="Radiation plays little part in a pot of boiling water."),
            C("Boiling uses no heat transfer", why="Heat must be transferred to cook the yam."),
            C("Convection carries heat through the water, and conduction moves heat into the yam", correct=True),
            C("Boiling uses convection only", why="Conduction through the pot and into the yam is also involved."),
        ], steps=[S("Analyse", text="The pot conducts heat to the water, convection currents spread it, then conduction takes it inside the yam.")],
           concept="Combined heat transfer", skill="Reasoning", hint="Follow the heat from the flame to the middle of the yam."),
        MC("Which pair of reasons for cooking is correct?", [
            C("To make food unsafe and bland", why="These are the opposite of good reasons."),
            C("To soften fibre so that food is easier to digest, and to develop flavour", correct=True),
            C("To remove all water and increase protein", why="Cooking does not increase protein."),
            C("To prevent all spoilage for years", why="Cooking helps food keep a short time only; preserving needs other methods."),
        ], steps=[S("Match", text="Softening fibre aids digestion, and heat develops flavour and aroma.")],
           concept="Reasons for cooking", skill="Concept", hint="Look for the pair that describes real benefits."),
        MC("A student puts a metal spoon and a plastic spoon into the same hot soup. After one minute, the metal spoon is much hotter. Which conclusion is best supported?", [
            C("Plastic is a better conductor than metal", why="The metal became hotter, so metal conducts better."),
            C("Both materials conduct heat equally", why="They did not heat equally."),
            C("The metal spoon was already hot", why="The test gives no sign of this; both were put in the same soup."),
            C("Metal is a better conductor of heat than plastic", correct=True),
        ], steps=[S("Interpret", text="The spoon that heats faster conducts better. Metal is a good conductor; plastic is an insulator.")],
           concept="Comparing conductors", skill="Interpretation", hint="Which spoon let the heat travel up its handle faster?"),
    ]))

# ------------------------------------------------------------------ 2. Moist methods of cooking
SETS.append(practice_set(
    module=M3, topic="Moist methods of cooking",
    title="Boiling, steaming, stewing and pressure cooking",
    lesson="fdn2-moist-methods-of-cooking",
    questions=[
        MC("Cooking food in a liquid kept just below boiling point, with only a few small bubbles, is called", [
            C("boiling", why="Boiling has large, active bubbles at about 100 degrees Celsius."),
            C("simmering", correct=True),
            C("braising", why="Braising starts with browning the food in fat."),
            C("steaming", why="In steaming the food is not in the liquid."),
        ], steps=[S("Match", text="Gentle bubbling just below boiling point is simmering.")],
           concept="Simmering", skill="Recall", hint="Which method is gentler than boiling but still bubbling?"),
        MC("Which food is cooked by steaming?", [
            C("Chips", why="Chips are deep fried."),
            C("Roast chicken", why="This is a dry method."),
            C("Soya (grilled meat)", why="This is grilling, a dry method."),
            C("Koki wrapped in leaves", correct=True),
        ], steps=[S("Match", text="Koki is a beans pudding wrapped in leaves and cooked by steam.")],
           concept="Steaming", skill="Recall", hint="Think of a food cooked above the water."),
        MC("Why is poaching suitable for a delicate piece of fish?", [
            C("The liquid is very hot and cooks it quickly", why="Poaching uses a gentle, low temperature."),
            C("The gentle heat does not break up the flaky flesh", correct=True),
            C("The fish is browned first", why="Browning is part of braising, not poaching."),
            C("It uses no liquid", why="Poaching needs a liquid."),
        ], steps=[S("Reason", text="Fish flesh breaks easily. A barely moving liquid cooks it without damage.")],
           concept="Poaching", skill="Concept", hint="What would happen to fish in a rolling boil?"),
        MC("Braising differs from stewing because in braising", [
            C("no liquid is used at all", why="A little liquid is used."),
            C("the food is cooked in an open pan", why="Braising is in a covered pot."),
            C("the food is first browned in fat and cooked on a bed of vegetables with a little liquid", correct=True),
            C("the food is cooked in steam only", why="This describes steaming."),
        ], steps=[S("Compare", text="Braising begins with browning in fat, then slow cooking in a covered pot with a little liquid.")],
           concept="Braising", skill="Concept", hint="Which method starts with a frying step?"),
        MC("The main reason a pressure cooker cooks food faster is that", [
            C("the food is cooked by radiation", why="A pressure cooker works with steam, not radiation."),
            C("the higher pressure raises the boiling point of water", correct=True),
            C("the lid keeps the food cold", why="The sealed lid keeps heat in; the food is very hot."),
            C("it uses less water than boiling needs, so it boils sooner", why="Less water is not the reason; the higher pressure is."),
        ], steps=[S("Explain", text="Sealed steam builds pressure; at about 120 degrees Celsius the food cooks faster.")],
           concept="Pressure cooking", skill="Concept", hint="What does the sealed lid do to the steam?"),
        MC("A cook boils spinach in a large pot of water for 30 minutes and pours the water away. Which loss is most likely?", [
            C("Water-soluble vitamins and minerals", correct=True),
            C("All the protein", why="Spinach is not rich in protein and little is lost this way."),
            C("The cellulose, which dissolves completely", why="Cellulose is softened, not dissolved."),
            C("Nothing, since nutrients are never lost in water", why="Vitamin C, B vitamins and minerals dissolve in the water."),
        ], steps=[S("Reason", text="Long boiling in much water dissolves vitamins B and C and minerals, which are then thrown away.")],
           concept="Nutrient loss in boiling", skill="Application", hint="What dissolves in water?"),
        MC("A family uses charcoal and wants to cook dried beans using less fuel. The best advice is to", [
            C("boil them rapidly in a wide open pan", why="This takes the longest and wastes fuel."),
            C("fry them in oil without soaking", why="Dry beans would not cook this way."),
            C("use a pressure cooker, after soaking if possible", correct=True),
            C("steam them for ten minutes", why="Dry beans need much longer to soften."),
        ], steps=[S("Decide", text="A pressure cooker shortens the cooking time of beans, so less fuel is burned.")],
           concept="Choosing a method", skill="Application", hint="Which method cooks hard foods most quickly?"),
        MC("A teacher says, 'Meat boiled hard becomes tough, but meat simmered gently becomes tender.' Which statement best supports this?", [
            C("Hard boiling makes the meat protein shrink and toughen, while gentle heat softens the connective tissue", correct=True),
            C("Hard boiling removes all the water from the meat", why="The meat remains in liquid; the fibres shrink and harden."),
            C("Simmering is hotter than boiling", why="Simmering is below boiling point."),
            C("Gentle heat adds extra protein", why="Cooking does not add protein."),
        ], steps=[S("Analyse", text="Rapid boiling hardens the protein fibres; gentle heat gives time for the connective tissue to become gelatine.")],
           concept="Effect of boiling on meat", skill="Reasoning", hint="Think of what rapid heat does to muscle protein."),
    ]))

# ------------------------------------------------------------------ 3. Dry methods of cooking
SETS.append(practice_set(
    module=M3, topic="Dry methods of cooking",
    title="Baking, roasting and grilling",
    lesson="fdn2-dry-methods-of-cooking",
    questions=[
        MC("Cooking by hot, dry air in a closed oven is called", [
            C("baking", correct=True),
            C("stewing", why="Stewing is a moist method in a little liquid."),
            C("steaming", why="Steaming cooks with steam, a moist method."),
            C("boiling", why="Boiling cooks in water."),
        ], steps=[S("Match", text="Hot dry air in a closed oven is baking.")],
           concept="Baking", skill="Recall", hint="Think of how bread is cooked."),
        MC("Which of these foods is usually grilled?", [
            C("Rice", why="Rice is boiled or steamed."),
            C("Bread dough", why="Dough is baked."),
            C("Fish over charcoal", correct=True),
            C("Soup", why="Soup is simmered."),
        ], steps=[S("Match", text="Fish over glowing charcoal is grilled.")],
           concept="Grilling", skill="Recall", hint="Which food is cooked by rays from glowing coals?"),
        MC("What is basting?", [
            C("Turning the food over", why="Turning is done in grilling, but it is not basting."),
            C("Spooning hot fat over food while it cooks", correct=True),
            C("Letting the food cool before eating", why="This has nothing to do with cooking method."),
            C("Boiling the food", why="Basting is done with fat, not water."),
        ], steps=[S("Define", text="Basting is spooning hot fat or juices over the roast to keep it moist.")],
           concept="Basting", skill="Recall", hint="It keeps the surface of a roast from drying."),
        MC("Why should the oven be pre-heated before cakes are baked?", [
            C("To dry out the flour", why="This is not the purpose."),
            C("To make the oven clean", why="Cleaning is separate."),
            C("To save electricity", why="Pre-heating uses fuel and does not save it."),
            C("So that the cake starts to rise and set at the correct temperature", correct=True),
        ], steps=[S("Explain", text="The mixture must meet the correct heat at once so the raising agent works and the structure sets.")],
           concept="Oven pre-heating", skill="Concept", hint="Think of what happens to a cake put into a cold oven."),
        MC("Which statement about grilling is correct?", [
            C("It cooks thick, tough meat well in a short time", why="Thick tough cuts would burn outside before softening."),
            C("It is best for thin, tender pieces of food", correct=True),
            C("It needs the food to be covered with water", why="Grilling is a dry method."),
            C("It uses no heat", why="It uses radiant heat."),
        ], steps=[S("Reason", text="Grilling is quick, so thin tender food cooks through before the outside burns.")],
           concept="Suitable foods for grilling", skill="Concept", hint="Think of how long the cooking takes."),
        MC("A cook roasts a chicken at a very high temperature. The outside burns but the inside is still raw. The best correction is to", [
            C("cook it at a moderate temperature for longer", correct=True),
            C("cook it at an even higher temperature for a short time", why="This burns the outside more."),
            C("remove the basting", why="Basting helps; removing it dries the outside."),
            C("serve it, since raw chicken is safe", why="Raw poultry can carry harmful bacteria."),
        ], steps=[S("Decide", text="A moderate oven lets heat reach the centre by conduction before the outside overcooks.")],
           concept="Roasting control", skill="Application", hint="How does heat reach the centre of thick food?"),
        MC("Which row correctly matches method and typical food?", [
            C("Grilling: sponge cake", why="Cake is baked."),
            C("Baking: bread", correct=True),
            C("Roasting: boiled egg", why="An egg is boiled or poached."),
            C("Baking: soup", why="Soup is simmered."),
        ], steps=[S("Match", text="Bread is baked in an oven.")],
           concept="Matching method and food", skill="Application", hint="Which food needs hot dry air in an oven?"),
        MC("Which is the best reason why baked and grilled foods keep more water-soluble vitamins than boiled foods?", [
            C("Dry methods use no heat", why="They use heat, often at high temperature."),
            C("There is no cooking water into which the vitamins can dissolve", correct=True),
            C("Dry methods add vitamin C", why="Cooking does not add vitamins."),
            C("High temperatures save vitamins", why="High heat can actually destroy some vitamins."),
        ], steps=[S("Compare", text="Vitamins B and C dissolve in water. With no cooking water, they cannot be poured away.")],
           concept="Nutrient retention in dry methods", skill="Reasoning", hint="What carries vitamins away in boiling?"),
    ]))

# ------------------------------------------------------------------ 4. Frying
SETS.append(practice_set(
    module=M3, topic="Frying",
    title="Shallow, deep and dry frying",
    lesson="fdn2-frying",
    questions=[
        MC("Cooking food completely covered in hot oil is called", [
            C("shallow frying", why="Shallow frying uses only a thin layer of fat."),
            C("deep frying", correct=True),
            C("dry frying", why="Dry frying uses no added fat."),
            C("braising", why="Braising is a moist method."),
        ], steps=[S("Match", text="Complete covering by hot oil is deep frying.")],
           concept="Deep frying", skill="Recall", hint="How much oil covers the food?"),
        MC("Which food is usually shallow fried?", [
            C("Puff-puff", why="Puff-puff is deep fried."),
            C("Chips", why="Chips are usually deep fried."),
            C("A fried egg", correct=True),
            C("Boiled yam", why="Boiling is a moist method."),
        ], steps=[S("Match", text="A fried egg is cooked in a thin layer of fat.")],
           concept="Shallow frying", skill="Recall", hint="Which food needs only a little oil in the pan?"),
        MC("Roasting groundnuts in a pan without adding oil is an example of", [
            C("deep frying", why="No oil covers the nuts."),
            C("dry frying", correct=True),
            C("poaching", why="Poaching is cooking in liquid."),
            C("steaming", why="No steam is used."),
        ], steps=[S("Match", text="No fat is added, so it is dry frying.")],
           concept="Dry frying", skill="Recall", hint="Look for the method with no added fat."),
        MC("What should be done first if the fat in a frying pan catches fire?", [
            C("Pour water on it", why="Water will make the burning fat spray."),
            C("Switch off the heat and cover the pan", correct=True),
            C("Carry the pan outside", why="Burning fat may spill and burn you."),
            C("Add more oil", why="This feeds the fire."),
        ], steps=[S("Respond", text="Cut off the heat and the air supply with a lid or damp cloth.")],
           concept="Fat fires", skill="Application", hint="Remove heat and air."),
        NUM("Chips absorb 20 g of oil in frying (a figure invented for practice). Each gram of fat gives 37 kJ. How much energy does the oil add, in kJ?", 740,
            steps=[S("Multiply", math=r"20 \times 37 = 740 \text{ kJ}")],
            unit="kJ", concept="Energy from absorbed fat", skill="Calculation", hint="Multiply the grams of oil by the energy per gram."),
        MC("Why does food put into oil that is not hot enough become greasy?", [
            C("The food absorbs a lot of oil before a crust forms", correct=True),
            C("The oil evaporates", why="Oil does not evaporate at these temperatures."),
            C("The food loses all its water", why="The food is soaked, not dried out."),
            C("The oil becomes water", why="Oil cannot change into water."),
        ], steps=[S("Explain", text="In hot oil a crust seals the surface quickly. In cool oil there is no seal, so oil soaks in.")],
           concept="Frying temperature", skill="Concept", hint="What seals the food in hot oil?"),
        MC("A cook wants less oil in fried fish and a crisp surface. Which step helps most?", [
            C("Put the fish in cold oil and heat slowly", why="Cold oil is soaked up."),
            C("Coat the fish in flour or batter and fry in hot oil", correct=True),
            C("Cover the pan with wet leaves", why="Water on hot oil is dangerous and does not help."),
            C("Fry a large amount of fish at once", why="Overfilling cools the oil and makes it greasy."),
        ], steps=[S("Decide", text="A coating plus hot oil seals the surface and limits absorbed fat.")],
           concept="Coating in frying", skill="Application", hint="What can form a quick seal around the food?"),
        MC("A nutritionist says, 'Regularly eating deep-fried food can lead to weight gain.' Which fact best explains this?", [
            C("Fried food contains no protein", why="Fried foods may contain protein."),
            C("Fat gives about twice as much energy per gram as carbohydrate or protein, and fried food absorbs fat", correct=True),
            C("Frying adds extra vitamins", why="Frying does not add vitamins."),
            C("Frying removes all the water so food is heavier", why="Frying reduces water."),
        ], steps=[S("Analyse", text="Fat: about 37 kJ per gram. Carbohydrate and protein: about 17 kJ per gram. Fried food absorbs fat, so the energy per portion rises.")],
           concept="Energy density of fried food", skill="Reasoning", hint="Compare the energy in a gram of fat with a gram of starch."),
    ]))

# ------------------------------------------------------------------ 5. Effects of heat on nutrients
SETS.append(practice_set(
    module=M3, topic="Effects of heat on nutrients",
    title="Heat, nutrient losses and nutrient retention",
    lesson="fdn2-effects-of-heat-on-nutrients",
    questions=[
        MC("The change of liquid egg white into a firm solid on heating is called", [
            C("gelatinisation", why="Gelatinisation is the swelling of starch in water."),
            C("coagulation", correct=True),
            C("caramelisation", why="This is the browning of sugar."),
            C("dextrinisation", why="This is the breakdown of starch by dry heat."),
        ], steps=[S("Match", text="Protein setting firm on heating is coagulation.")],
           concept="Coagulation of protein", skill="Recall", hint="It is a protein change."),
        MC("Which vitamin is destroyed most easily by cooking?", [
            C("Vitamin D", why="Vitamin D is fairly stable to ordinary cooking."),
            C("Vitamin A", why="Vitamin A is fairly stable to ordinary cooking."),
            C("Vitamin K", why="Vitamin K is fairly stable."),
            C("Vitamin C", correct=True),
        ], steps=[S("Recall", text="Vitamin C is water-soluble and destroyed by heat and air.")],
           concept="Vitamin C stability", skill="Recall", hint="Which vitamin is found in fresh fruit and spoiled by heat?"),
        MC("What happens to starch when it is heated with water?", [
            C("Gelatinisation: the grains swell and thicken the liquid", correct=True),
            C("It turns into fat", why="Starch is a carbohydrate and does not become fat when cooked."),
            C("It turns into protein", why="Starch cannot become protein."),
            C("It disappears completely", why="It remains, but changed."),
        ], steps=[S("Explain", text="Starch grains absorb water and swell, thickening the mixture.")],
           concept="Gelatinisation", skill="Concept", hint="Think of how pap thickens."),
        MC("Which cooking practice reduces the loss of vitamin C from cabbage?", [
            C("Cutting it into very small pieces and soaking it", why="More cut surface and soaking dissolves more vitamin."),
            C("Boiling it for a long time with bicarbonate of soda", why="Both long cooking and bicarbonate destroy vitamin C."),
            C("Cooking it in a small amount of water, covered, for a short time", correct=True),
            C("Keeping it hot for three hours before serving", why="Prolonged heat destroys more vitamin C."),
        ], steps=[S("Decide", text="Little water, a lid and a short time keep the most vitamin C.")],
           concept="Reducing vitamin loss", skill="Application", hint="Which choice uses the least water, heat and time?"),
        NUM("Fresh pepper has 100 mg of vitamin C in a portion (a figure invented for practice). Cooking destroys 40% of it. How many mg are left?", 60,
            steps=[S("Find the loss", math=r"\frac{40}{100} \times 100 = 40 \text{ mg}"), S("Subtract", math=r"100 - 40 = 60 \text{ mg}")],
            unit="mg", concept="Calculating nutrient retention", skill="Calculation", hint="Work out 40% of the total, then subtract."),
        MC("Why are minerals lost when vegetables are boiled and the water is thrown away?", [
            C("Heat destroys minerals completely", why="Minerals are not destroyed by heat."),
            C("Minerals turn into vitamins", why="Minerals and vitamins are different substances."),
            C("Minerals dissolve in the cooking water", correct=True),
            C("Minerals are burnt by the lid", why="The lid does not burn minerals."),
        ], steps=[S("Explain", text="Minerals dissolve in the water; throwing the water away throws the minerals away.")],
           concept="Mineral loss", skill="Concept", hint="Where do the minerals go in boiling?"),
        MC("Toast turns brown because the starch on the surface undergoes", [
            C("gelatinisation", why="Gelatinisation needs water."),
            C("coagulation", why="Coagulation is a protein change."),
            C("fermentation", why="Fermentation is done by yeast, not by dry heat."),
            C("dextrinisation", correct=True),
        ], steps=[S("Identify", text="Dry heat breaks starch into dextrins that are brown.")],
           concept="Dextrinisation", skill="Application", hint="Which change needs dry heat on starch?"),
        MC("Overcooked meat is dry and tough. Which explanation is best?", [
            C("Too much heat makes the coagulated protein shrink and harden, squeezing out water", correct=True),
            C("Heat adds extra fat to the meat", why="Heat does not add fat; fat melts out."),
            C("Heat turns protein into starch", why="This does not happen."),
            C("Heat makes minerals into water", why="Minerals are not turned into water."),
        ], steps=[S("Analyse", text="Protein first firms, then with more heat the fibres shrink and harden and push out water.")],
           concept="Overcooking protein", skill="Reasoning", hint="Think of what prolonged heat does to coagulated protein."),
    ]))

# ------------------------------------------------------------------ 6. Cereals
SETS.append(practice_set(
    module=M4, topic="Cereals",
    title="Cereal grains: structure, nutrients and storage",
    lesson="fdn2-cereals",
    questions=[
        MC("Which of these foods is a cereal?", [
            C("Cassava", why="Cassava is a root."),
            C("Yam", why="Yam is a tuber."),
            C("Millet", correct=True),
            C("Groundnut", why="Groundnut is a legume (pulse)."),
        ], steps=[S("Recall", text="Millet is the seed of a grass, so it is a cereal.")],
           concept="Cereals", skill="Recall", hint="Cereals are seeds of grasses."),
        MC("Which part of the grain is labelled B in the diagram? (A is the outer coat; C is the small part at the base.)", [
            C("Bran", why="The bran is the outer coat, labelled A."),
            C("Endosperm", correct=True),
            C("Germ", why="The germ is the small part at the base, labelled C."),
            C("Husk", why="The husk is not one of the three parts labelled."),
        ], steps=[S("Read the diagram", text="B is the large middle area: the endosperm, the starch store.")],
           concept="Grain structure", skill="Interpretation", hint="Which part is the largest?",
           diagram="f5fdn2-grain-q.svg", diagram_alt="Section through a grain with three parts labelled A (outer coat), B (large middle) and C (small part at the base)"),
        MC("The main nutrient in the endosperm of a cereal is", [
            C("protein", why="Cereals contain some protein, but the endosperm is mostly starch."),
            C("fat", why="Fat is mainly in the germ and in small amounts."),
            C("vitamin C", why="Cereals contain no vitamin C."),
            C("starch", correct=True),
        ], steps=[S("Recall", text="The endosperm is a store of starch.")],
           concept="Endosperm", skill="Recall", hint="What gives cereals their energy?"),
        MC("Why does brown rice contain more fibre than white rice?", [
            C("It has had the bran removed", why="Removing the bran is what makes white rice."),
            C("It still has its bran", correct=True),
            C("It has been boiled twice", why="Boiling does not add fibre."),
            C("It contains extra water", why="Water is not fibre."),
        ], steps=[S("Explain", text="Fibre is in the bran. Brown rice keeps it; polished white rice does not.")],
           concept="Whole grain and fibre", skill="Concept", hint="Which part of the grain holds the fibre?"),
        MC("Which of these is the best way to store maize flour?", [
            C("In an open basket on the floor", why="This invites damp, rats and insects."),
            C("In a dry, airtight container in a cool place", correct=True),
            C("In a warm, humid kitchen cupboard", why="Warm damp air allows mould and insects."),
            C("Mixed with old flour in a damp bag", why="Old stock may carry insects and mould."),
        ], steps=[S("Decide", text="Dryness and airtightness keep out moisture and pests.")],
           concept="Storing cereals", skill="Application", hint="What do moulds and weevils need?"),
        MC("Why is a meal of rice and beans better than rice alone?", [
            C("Beans contain more starch", why="The advantage is in protein, not in starch."),
            C("Beans give vitamin C which rice lacks in large amounts", why="Dried beans give little vitamin C."),
            C("The two proteins complement each other", correct=True),
            C("Beans make the rice cook faster", why="This is not the nutritional reason."),
        ], steps=[S("Reason", text="Rice is short of lysine; beans supply it. Together they give a better amino acid mix.")],
           concept="Complementary proteins", skill="Reasoning", hint="Think of amino acids."),
        MC("White flour keeps longer than wholemeal flour mainly because", [
            C("it contains more vitamins", why="White flour has fewer vitamins."),
            C("the germ, which holds fat that turns rancid, has been removed", correct=True),
            C("it is made from a different plant", why="Both are made from wheat."),
            C("it has more water", why="Extra water would make it spoil sooner."),
        ], steps=[S("Explain", text="The germ's fat goes rancid. Removing it extends shelf life.")],
           concept="Shelf life of flour", skill="Concept", hint="Which part of the grain contains fat?"),
        MC("A mother is choosing a flour for her family. She wants more fibre and B vitamins. Which should she choose?", [
            C("Highly refined white flour", why="This has lost most fibre and B vitamins."),
            C("Wholemeal flour", correct=True),
            C("Starch powder", why="Starch powder has no fibre or vitamins."),
            C("Sugar", why="Sugar contains none of these."),
        ], steps=[S("Decide", text="Wholemeal keeps the bran and germ, which supply fibre and B vitamins.")],
           concept="Choosing flour", skill="Application", hint="Which product keeps all parts of the grain?"),
    ]))

# ------------------------------------------------------------------ 7. Meat, offal and poultry
SETS.append(practice_set(
    module=M4, topic="Meat, offal and poultry",
    title="Meat structure, offal and poultry",
    lesson="fdn2-meat-offal-poultry",
    questions=[
        MC("Which of these is offal?", [
            C("Chicken breast", why="This is poultry meat, not offal."),
            C("Beef fillet", why="Fillet is muscle meat."),
            C("Liver", correct=True),
            C("Goat leg", why="This is muscle meat."),
        ], steps=[S("Recall", text="Offal means edible internal organs such as liver and kidney.")],
           concept="Offal", skill="Recall", hint="Offal is an organ, not muscle."),
        MC("The protein of meat is described as of high biological value because it", [
            C("contains all the essential amino acids", correct=True),
            C("is cheap", why="Price is not a nutritional reason."),
            C("contains no fat", why="Meat protein foods can contain fat."),
            C("cooks quickly", why="Cooking time is unrelated."),
        ], steps=[S("Recall", text="High biological value means all essential amino acids are supplied in good amounts.")],
           concept="Protein quality", skill="Recall", hint="Think of amino acids."),
        MC("Connective tissue in meat is mainly made of", [
            C("starch", why="Starch is in plants."),
            C("collagen", correct=True),
            C("vitamin C", why="Meat has no vitamin C."),
            C("fibre (cellulose)", why="Cellulose is found only in plants."),
        ], steps=[S("Recall", text="Collagen fibres hold muscle fibres together.")],
           concept="Connective tissue", skill="Recall", hint="It becomes gelatine on slow moist cooking."),
        MC("Which method is best for a tough cut such as shin of beef?", [
            C("Quick grilling", why="It would stay tough."),
            C("Slow stewing or braising", correct=True),
            C("Shallow frying for two minutes", why="This is too short to soften tough meat."),
            C("Eating it raw", why="Raw meat is unsafe and tough."),
        ], steps=[S("Decide", text="Long moist cooking changes collagen to gelatine and tenderises the meat.")],
           concept="Cooking tough cuts", skill="Application", hint="Tough meat needs time and liquid."),
        MC("A cook cuts raw chicken and then slices bread on the same board without washing it. This is a risk of", [
            C("better flavour", why="This is not a flavour matter."),
            C("cross-contamination", correct=True),
            C("faster cooking", why="This has no effect on cooking speed."),
            C("loss of vitamin C", why="The risk is spread of bacteria."),
        ], steps=[S("Identify", text="Bacteria from the raw chicken can pass to bread, which is eaten without cooking.")],
           concept="Cross-contamination", skill="Application", hint="What can pass from raw chicken to ready-to-eat food?"),
        MC("Which statement about liver is correct?", [
            C("It contains no iron", why="Liver is one of the richest sources of iron."),
            C("It is rich in iron and vitamin A", correct=True),
            C("It has no protein", why="Liver is rich in protein."),
            C("It keeps longer than meat without cold storage", why="Offal spoils faster than meat."),
        ], steps=[S("Recall", text="Liver is rich in iron, vitamin A, B vitamins and protein, but spoils quickly.")],
           concept="Nutrients in offal", skill="Concept", hint="Liver stores nutrients for the animal."),
        NUM("Minced meat should be cooked until the centre reaches at least 70 degrees Celsius. A thermometer reads 58 degrees Celsius. By how many degrees must the temperature rise?", 12,
            steps=[S("Subtract", math=r"70 - 58 = 12")], unit="degrees Celsius",
            concept="Safe cooking temperature", skill="Calculation", hint="Subtract the reading from the target."),
        MC("A butcher's stall has meat that is slimy, dull in colour and has a sour smell. The best advice is to", [
            C("buy it and boil it for a long time", why="Spoiled meat can carry toxins that boiling does not remove."),
            C("buy it because it is cheap", why="Price does not make it safe."),
            C("refuse it, since these signs show that the meat is spoiled", correct=True),
            C("wash it with lemon and eat it raw", why="Lemon does not make spoiled meat safe."),
        ], steps=[S("Judge", text="Sliminess, dull colour and a sour smell show bacterial spoilage; the meat is unsafe.")],
           concept="Signs of spoiled meat", skill="Reasoning", hint="What do slime and a bad smell tell you?"),
    ]))

# ------------------------------------------------------------------ 8. Fish
SETS.append(practice_set(
    module=M4, topic="Fish",
    title="Types of fish, freshness and cooking",
    lesson="fdn2-fish",
    questions=[
        MC("Which of these is an oily fish?", [
            C("Mackerel", correct=True),
            C("Cod", why="Cod is a white fish, with fat in the liver only."),
            C("Catfish", why="Catfish is mainly a white, lean freshwater fish."),
            C("Prawn", why="Prawns are shellfish."),
        ], steps=[S("Recall", text="Mackerel has fat through the flesh.")],
           concept="Oily fish", skill="Recall", hint="Which fish has fat all through the flesh?"),
        MC("Which is a sign of fresh fish?", [
            C("Sunken, cloudy eyes", why="These show that the fish is stale."),
            C("Bright red gills", correct=True),
            C("A very strong smell", why="Strong smell shows spoilage."),
            C("Soft flesh that stays dented", why="Fresh flesh springs back."),
        ], steps=[S("Recall", text="Fresh fish has bright red or pink gills.")],
           concept="Freshness of fish", skill="Recall", hint="Think of the colour of fresh gills."),
        MC("Which group of fish includes prawns and crabs?", [
            C("White fish", why="White fish have fins and a backbone."),
            C("Oily fish", why="Oily fish have fins and a backbone."),
            C("Shellfish", correct=True),
            C("Freshwater fish", why="This describes habitat, not the group."),
        ], steps=[S("Recall", text="Prawns and crabs are crustaceans, a kind of shellfish.")],
           concept="Shellfish", skill="Recall", hint="They have a shell."),
        MC("Why is fish easier to digest than meat?", [
            C("It has short muscle fibres and little connective tissue", correct=True),
            C("It contains no protein", why="Fish is rich in protein."),
            C("It is always eaten raw", why="Most fish is cooked."),
            C("It has more collagen than meat", why="It has less collagen."),
        ], steps=[S("Explain", text="Short fibres and weak connective tissue make fish tender and easily digested.")],
           concept="Structure of fish", skill="Concept", hint="Compare the connective tissue in fish and meat."),
        MC("A woman buys fish and keeps it in a hot room for six hours. The likely result is", [
            C("it will become fresher", why="Warmth speeds spoilage."),
            C("bacteria and enzymes will spoil it rapidly", correct=True),
            C("it will become sterile", why="Warmth does not sterilise it."),
            C("it will gain vitamins", why="Spoilage does not add vitamins."),
        ], steps=[S("Reason", text="Fish spoils fast at room temperature in hot climates; it should be kept cold.")],
           concept="Storage of fish", skill="Application", hint="What does warmth do to micro-organisms?"),
        MC("Which cooking method suits a delicate fillet of white fish best?", [
            C("Poaching or steaming gently", correct=True),
            C("Boiling hard for an hour", why="The fish would break up and become dry."),
            C("Braising for three hours", why="This would destroy the fish."),
            C("Leaving it in a hot oven for two hours", why="It would dry out."),
        ], steps=[S("Decide", text="Gentle, short moist heat keeps the flaky flesh whole and moist.")],
           concept="Cooking white fish", skill="Application", hint="The flesh is delicate and cooks quickly."),
        MC("Which nutrient is provided by oily fish but is rare in most other foods?", [
            C("Vitamin C", why="Fish contains little vitamin C."),
            C("Vitamin D", correct=True),
            C("Starch", why="Fish has no starch."),
            C("Fibre", why="Fish contains no fibre."),
        ], steps=[S("Recall", text="Oily fish and egg yolk are among the few good sources of vitamin D.")],
           concept="Vitamins in oily fish", skill="Concept", hint="It helps the body to use calcium."),
        MC("A seller sprays perfume on stale fish to hide its smell. A careful buyer should", [
            C("buy it since it smells pleasant", why="The perfume hides the smell but the fish is still stale."),
            C("check the eyes, gills and flesh before buying", correct=True),
            C("choose the largest fish", why="Size does not show freshness."),
            C("choose the cheapest fish", why="Low price may be a sign of stale fish."),
        ], steps=[S("Judge", text="Eyes, gills and firmness of the flesh show freshness; smell alone can be disguised.")],
           concept="Judging fresh fish", skill="Reasoning", hint="What other signs can you check?"),
    ]))

# ------------------------------------------------------------------ 9. Eggs
SETS.append(practice_set(
    module=M4, topic="Eggs",
    title="Egg structure, freshness and uses",
    lesson="fdn2-eggs",
    questions=[
        MC("In the diagram of an egg, which letter shows the part that holds the yolk in the centre of the egg?", [
            C("E", why="E is the air space at the blunt end."),
            C("F", correct=True),
            C("G", why="G is the thick white, which surrounds the yolk but is not the holding cords."),
            C("H", why="H is the yolk itself."),
        ], steps=[S("Read the diagram", text="F is the pair of twisted cords, the chalazae, which hold the yolk in place.")],
           concept="Chalazae", skill="Interpretation", hint="Look for the cords above and below the yolk.",
           diagram="f5fdn2-egg-q.svg", diagram_alt="Section through an egg with eight parts labelled with the letters A to H"),
        MC("Which part of an egg contains most of the fat?", [
            C("Shell", why="The shell is calcium carbonate."),
            C("White", why="The white is protein and water."),
            C("Yolk", correct=True),
            C("Air space", why="This is only air."),
        ], steps=[S("Recall", text="The yolk contains the fat, vitamins A and D and iron.")],
           concept="Nutrients in the yolk", skill="Recall", hint="It is the yellow part."),
        MC("A fresh egg placed in cold water will", [
            C("float", why="Floating shows an old, stale egg."),
            C("sink and lie flat", correct=True),
            C("break", why="Water does not break the egg."),
            C("turn cloudy", why="A raw egg does not turn cloudy in the water."),
        ], steps=[S("Recall", text="The air space of a fresh egg is small, so it sinks and lies flat.")],
           concept="Freshness test", skill="Recall", hint="Think of the size of the air space."),
        MC("Whisked egg whites are used in meringues because whisking", [
            C("traps air, forming a foam", correct=True),
            C("removes the protein", why="The protein is still there."),
            C("cooks the egg", why="Whisking does not cook the egg."),
            C("turns the egg into fat", why="This does not happen."),
        ], steps=[S("Explain", text="Whisking traps air bubbles in the protein film. This is aeration.")],
           concept="Aeration", skill="Concept", hint="What does whisking add?"),
        NUM("A tray of 30 eggs costs FCFA 2 700 (an invented price for practice). What is the cost of 4 eggs, in FCFA?", 360,
            steps=[S("Cost of one egg", math=r"2700 \div 30 = 90"), S("Cost of four eggs", math=r"4 \times 90 = 360")],
            unit="FCFA", concept="Cost of eggs", skill="Calculation", hint="Find the cost of one egg first."),
        MC("Which use of egg depends on lecithin in the yolk?", [
            C("Glazing a loaf", why="Glazing gives shine and colour, not an emulsion."),
            C("Making mayonnaise (an emulsion of oil and water)", correct=True),
            C("Making a meringue", why="A meringue is a foam of egg white."),
            C("Boiling an egg", why="Boiling shows coagulation."),
        ], steps=[S("Identify", text="Lecithin holds oil and water together in mayonnaise.")],
           concept="Emulsifying", skill="Concept", hint="Which food mixes oil and water?"),
        MC("Why should eggs be stored away from onions and fish?", [
            C("Onions break the shell", why="They do not break it."),
            C("The porous shell lets smells pass into the egg", correct=True),
            C("Eggs make onions rot", why="This is not the reason."),
            C("Eggs freeze with onions", why="This is not the reason."),
        ], steps=[S("Explain", text="The shell has tiny holes through which smells enter the egg.")],
           concept="Storing eggs", skill="Application", hint="Think of the holes in the shell."),
        MC("A student breaks an egg onto a plate. The yolk is flat and the white is thin and watery and spreads out. The egg is", [
            C("very fresh", why="A fresh egg has a high round yolk and thick white."),
            C("stale", correct=True),
            C("hard-boiled", why="This egg is raw."),
            C("unsafe because it has a yolk", why="Every egg has a yolk."),
        ], steps=[S("Interpret", text="A flat yolk and watery white are signs of an old egg.")],
           concept="Break-out test", skill="Interpretation", hint="Think of what happens to the white with age."),
    ]))

# ------------------------------------------------------------------ 10. Milk and cheese
SETS.append(practice_set(
    module=M4, topic="Milk and cheese",
    title="Milk, milk products and cheese",
    lesson="fdn2-milk-and-cheese",
    questions=[
        MC("Which mineral is milk especially rich in?", [
            C("Iron", why="Milk is a poor source of iron."),
            C("Calcium", correct=True),
            C("Iodine", why="This is not a main mineral in milk."),
            C("Fluoride", why="This is not a main mineral in milk."),
        ], steps=[S("Recall", text="Milk is the best everyday source of calcium.")],
           concept="Calcium in milk", skill="Recall", hint="Think of bones and teeth."),
        MC("The sugar in milk is called", [
            C("sucrose", why="Sucrose is table sugar from cane or beet."),
            C("fructose", why="Fructose is fruit sugar."),
            C("maltose", why="Maltose is malt sugar."),
            C("lactose", correct=True),
        ], steps=[S("Recall", text="Milk sugar is lactose.")],
           concept="Lactose", skill="Recall", hint="The name starts with the Latin word for milk."),
        MC("Pasteurisation of milk is", [
            C("heating it to kill disease bacteria and cooling quickly", correct=True),
            C("removing all its water", why="This describes drying."),
            C("adding sugar", why="This describes condensed milk."),
            C("freezing it", why="This is freezing."),
        ], steps=[S("Define", text="Pasteurisation: heating to a moderate temperature for a set time, then cooling, to kill harmful bacteria.")],
           concept="Pasteurisation", skill="Recall", hint="It makes milk safe without changing flavour much."),
        MC("In cheese making, the liquid which separates from the curds is called", [
            C("cream", why="Cream is the fat layer in fresh milk."),
            C("rennet", why="Rennet is the enzyme added to set the milk."),
            C("buttermilk", why="Buttermilk is left after churning butter."),
            C("whey", correct=True),
        ], steps=[S("Recall", text="Curds are the solid; whey is the liquid.")],
           concept="Curds and whey", skill="Recall", hint="It is the opposite of curds."),
        NUM("A glass holds 200 ml of milk with 120 mg of calcium in each 100 ml (a teaching figure). How much calcium does the glass give, in mg?", 240,
            steps=[S("Number of 100 ml portions", math=r"200 \div 100 = 2"), S("Multiply", math=r"2 \times 120 = 240")],
            unit="mg", concept="Calcium in a serving", skill="Calculation", hint="How many 100 ml portions are in 200 ml?"),
        MC("A cook heats milk quickly on strong heat and it burns on the bottom of the pan. This is called", [
            C("curdling", why="Curdling is lumping caused by acid or salt."),
            C("scorching", correct=True),
            C("pasteurising", why="This is a heat treatment to make milk safe."),
            C("fermenting", why="Fermenting is caused by micro-organisms."),
        ], steps=[S("Identify", text="Milk sugar and protein burn on the base when heated too fast.")],
           concept="Scorching", skill="Application", hint="Think of what happens at the bottom of the pan."),
        MC("A baby is fed only on milk for a long time and becomes pale and tired. Which lack of nutrient is the most likely cause?", [
            C("Calcium", why="Milk is rich in calcium."),
            C("Protein", why="Milk is a good protein source."),
            C("Iron", correct=True),
            C("Lactose", why="Milk is full of lactose."),
        ], steps=[S("Reason", text="Milk is a poor source of iron, so long milk-only feeding can cause anaemia, with pallor and tiredness.")],
           concept="Iron deficiency and milk", skill="Reasoning", hint="Which mineral is missing from milk?"),
        MC("A family buys fresh milk straight from a herder. The best advice is to", [
            C("drink it raw, since it is fresh", why="Raw milk can carry harmful bacteria."),
            C("boil it before drinking or using it", correct=True),
            C("add sugar and leave it in the sun", why="Warmth makes bacteria and sourness increase."),
            C("freeze it and eat it frozen", why="Freezing does not kill all bacteria."),
        ], steps=[S("Decide", text="Boiling kills the disease bacteria that may be in raw milk.")],
           concept="Safe use of fresh milk", skill="Application", hint="What does heat do to bacteria?"),
    ]))

# ------------------------------------------------------------------ 11. Pulses and nuts
SETS.append(practice_set(
    module=M4, topic="Pulses and nuts",
    title="Beans, groundnuts and other pulses and nuts",
    lesson="fdn2-pulses-and-nuts",
    questions=[
        MC("Which of these is a pulse?", [
            C("Cowpeas (black-eyed beans)", correct=True),
            C("Maize", why="Maize is a cereal."),
            C("Cocoyam", why="Cocoyam is a tuber."),
            C("Pawpaw", why="Pawpaw is a fruit."),
        ], steps=[S("Recall", text="Pulses are the dry seeds of legumes such as beans.")],
           concept="Pulses", skill="Recall", hint="Look for a dry seed from a pod."),
        MC("The main nutrient in dry beans is", [
            C("vitamin C", why="Dry beans have no vitamin C."),
            C("fat", why="Beans are low in fat."),
            C("protein, together with starch", correct=True),
            C("alcohol", why="This is not a nutrient."),
        ], steps=[S("Recall", text="Dry beans give about 20 to 25% protein and a lot of starch.")],
           concept="Nutrients in pulses", skill="Recall", hint="They are often called the poor man's meat."),
        MC("Which food is richest in fat?", [
            C("Red kidney beans", why="Beans contain very little fat."),
            C("Groundnuts", correct=True),
            C("Cowpeas", why="Cowpeas contain very little fat."),
            C("Lentils", why="Lentils contain very little fat."),
        ], steps=[S("Recall", text="Groundnuts are about half fat by weight.")],
           concept="Fat in nuts", skill="Recall", hint="Which of these is pressed for cooking oil?"),
        MC("Why are dried beans soaked before cooking?", [
            C("To make them harder", why="Soaking softens them."),
            C("To shorten the cooking time and save fuel", correct=True),
            C("To remove all fibre", why="Fibre stays in the beans."),
            C("To add fat", why="Soaking adds water, not fat."),
        ], steps=[S("Explain", text="Soaked beans have absorbed water and soften faster in the pot.")],
           concept="Soaking pulses", skill="Concept", hint="Think about time and fuel."),
        NUM("Dry beans contain 22 g of protein in each 100 g (a teaching figure). How much protein is in 250 g of dry beans, in g?", 55,
            steps=[S("Number of 100 g portions", math=r"250 \div 100 = 2.5"), S("Multiply", math=r"2.5 \times 22 = 55")],
            unit="g", concept="Protein in a serving", skill="Calculation", hint="How many 100 g portions are in 250 g?"),
        MC("Groundnuts stored in a damp room for months become mouldy and taste bitter. The best advice is to", [
            C("roast them and eat them anyway", why="Mould toxins are not destroyed by roasting."),
            C("throw away the mouldy nuts and store clean dry ones in airtight containers", correct=True),
            C("add water to freshen them", why="More water increases mould growth."),
            C("mix them with fresh nuts to hide the taste", why="This spreads the contamination."),
        ], steps=[S("Decide", text="Mouldy nuts can carry toxins. Dry storage prevents mould.")],
           concept="Storing nuts safely", skill="Application", hint="What do moulds need to grow?"),
        MC("A child eats cassava fufu and leaf soup every day with no beans, fish, egg or meat. Which addition would most improve the protein in the meals?", [
            C("More cassava", why="Cassava is mostly starch."),
            C("Beans or groundnut paste in the soup", correct=True),
            C("Salt", why="Salt gives no protein."),
            C("Sugar", why="Sugar gives energy but no protein."),
        ], steps=[S("Reason", text="Beans and groundnuts supply protein, iron and B vitamins missing from a diet of cassava and leaves.")],
           concept="Improving a diet with pulses", skill="Reasoning", hint="Which foods are rich in plant protein?"),
        MC("A cook serves red kidney beans that were soaked but boiled for only five minutes and are still hard. Which statement is correct?", [
            C("They are safe because they were soaked", why="Soaking alone does not make raw beans safe."),
            C("They are unsafe: raw or undercooked beans can make people ill", correct=True),
            C("They are safe if sugar is added", why="Sugar does not remove the toxins."),
            C("They are safe if eaten cold", why="Cold serving does not remove the toxins."),
        ], steps=[S("Judge", text="Beans must be boiled hard and cooked until soft to destroy the harmful substances.")],
           concept="Safe cooking of beans", skill="Application", hint="Why must beans be cooked until soft?"),
    ]))

# ------------------------------------------------------------------ 12. Fruits, vegetables, herbs and spices
SETS.append(practice_set(
    module=M4, topic="Fruits, vegetables, herbs and spices",
    title="Groups, nutrients and uses of fruits, vegetables, herbs and spices",
    lesson="fdn2-fruits-vegetables-herbs-spices",
    questions=[
        MC("Which of these is a leaf vegetable?", [
            C("Carrot", why="Carrot is a root vegetable."),
            C("Ndole (bitterleaf)", correct=True),
            C("Okra", why="Okra is a fruit vegetable."),
            C("Cauliflower", why="Cauliflower is a flower vegetable."),
        ], steps=[S("Classify", text="Ndole is the leaf of the bitterleaf plant.")],
           concept="Vegetable groups", skill="Recall", hint="Which of these is a leaf?"),
        MC("The best local source of vitamin C is", [
            C("an orange", correct=True),
            C("cassava flour", why="Cassava flour has almost no vitamin C."),
            C("rice", why="Rice has no vitamin C."),
            C("palm oil", why="Palm oil is fat; it contains carotene, not vitamin C."),
        ], steps=[S("Recall", text="Citrus fruits are rich in vitamin C.")],
           concept="Vitamin C sources", skill="Recall", hint="Think of a juicy citrus fruit."),
        MC("Carrots and mangoes are valuable because they are rich in", [
            C("carotene, which the body turns into vitamin A", correct=True),
            C("vitamin D", why="Vitamin D is found in oily fish and egg yolk."),
            C("protein", why="These foods have little protein."),
            C("fat", why="These foods have little fat."),
        ], steps=[S("Recall", text="Orange and yellow fruits and vegetables carry carotene.")],
           concept="Carotene", skill="Recall", hint="It gives them their orange colour."),
        MC("Which of these is a spice?", [
            C("Thyme", why="Thyme is a leaf, so it is a herb."),
            C("Basil", why="Basil is a leaf, so it is a herb."),
            C("Ginger", correct=True),
            C("Parsley", why="Parsley is a leaf, so it is a herb."),
        ], steps=[S("Classify", text="Ginger is an underground stem (rhizome), so it is a spice.")],
           concept="Herbs and spices", skill="Concept", hint="Spices are not leaves."),
        MC("Why does cutting vegetables into very small pieces and soaking them cause vitamin loss?", [
            C("A large surface area lets vitamins dissolve into the water", correct=True),
            C("Vitamins are heavy and sink", why="Vitamins do not sink out of food."),
            C("Soaking adds fat to the vegetables", why="Soaking does not add fat."),
            C("Soaking makes vitamins into minerals", why="Vitamins do not change into minerals."),
        ], steps=[S("Explain", text="Smaller pieces expose more surface, and water-soluble vitamins (B, C) dissolve into the soaking water.")],
           concept="Vitamin loss in preparation", skill="Concept", hint="What do B and C vitamins do in water?"),
        MC("Fresh pawpaw and cooked pawpaw are compared. Which statement is most likely true?", [
            C("The cooked fruit has more vitamin C", why="Cooking destroys some vitamin C."),
            C("The fresh fruit has more vitamin C", correct=True),
            C("Both contain exactly the same vitamin C", why="Cooking reduces vitamin C."),
            C("The cooked fruit has more fibre", why="Cooking does not add fibre."),
        ], steps=[S("Reason", text="Heat and water destroy or dissolve vitamin C, so fresh fruit keeps more.")],
           concept="Cooking and vitamin C", skill="Reasoning", hint="Which treatment is gentler on vitamin C?"),
        MC("A cook adds fresh parsley and basil only in the last two minutes of cooking. Why?", [
            C("Their flavour is lost in long cooking", correct=True),
            C("They are poisonous when cooked", why="They are not poisonous."),
            C("They must be raw to be herbs", why="Herbs can be fresh, dried or cooked."),
            C("They make food cold", why="Herbs do not cool food."),
        ], steps=[S("Explain", text="Delicate fresh herbs lose their aroma when heated for a long time.")],
           concept="Using herbs in cooking", skill="Application", hint="What is lost from fresh herbs by long heating?"),
        MC("A mother buys vegetables on Monday for the whole week. Which storage plan will keep them best?", [
            C("Leave leafy vegetables in direct sun on the table", why="Sun wilts leaves and destroys vitamins."),
            C("Keep roots in a cool, dark, dry place and use leafy vegetables first", correct=True),
            C("Wash all vegetables and seal them wet in a bag", why="Wet sealed vegetables rot quickly."),
            C("Store damaged vegetables beside sound ones", why="Rot and mould spread to sound vegetables."),
        ], steps=[S("Decide", text="Leaves wilt first, so use them early; roots and tubers keep longer in a cool, dark, dry place.")],
           concept="Storing vegetables", skill="Application", hint="Which vegetables spoil fastest?"),
    ]))

# ------------------------------------------------------------------ 13. Raising agents and flour mixtures
SETS.append(practice_set(
    module=M4, topic="Raising agents and flour mixtures",
    title="Raising agents, methods and recipe scaling",
    lesson="fdn2-raising-agents-and-flour-mixtures",
    questions=[
        MC("Which raising agent is a living organism?", [
            C("Baking powder", why="Baking powder is a chemical mixture."),
            C("Bicarbonate of soda", why="Bicarbonate of soda is a chemical."),
            C("Yeast", correct=True),
            C("Steam", why="Steam is water vapour."),
        ], steps=[S("Recall", text="Yeast is a living fungus.")],
           concept="Yeast", skill="Recall", hint="It ferments sugar."),
        MC("Baking powder contains bicarbonate of soda and", [
            C("an acid", correct=True),
            C("yeast", why="Yeast is a separate raising agent."),
            C("sugar only", why="The bicarbonate needs an acid to release gas."),
            C("salt only", why="Salt does not react to give gas."),
        ], steps=[S("Recall", text="Bicarbonate plus acid react with moisture and heat to give carbon dioxide.")],
           concept="Composition of baking powder", skill="Recall", hint="The bicarbonate needs a partner to react."),
        MC("Scones are made by which method?", [
            C("Whisking", why="Whisked mixtures are sponges."),
            C("Rubbing-in", correct=True),
            C("Creaming", why="Creaming is used for sandwich cakes."),
            C("Batter making", why="Batters are liquid mixtures."),
        ], steps=[S("Match", text="Scones: fat is rubbed into flour, then liquid is added.")],
           concept="Rubbing-in method", skill="Recall", hint="Think of fat and flour like breadcrumbs."),
        MC("Which gas makes bread dough rise?", [
            C("Oxygen", why="Yeast does not release oxygen as the raising gas."),
            C("Carbon dioxide", correct=True),
            C("Nitrogen", why="Nitrogen plays no part in raising."),
            C("Hydrogen", why="Hydrogen is not produced."),
        ], steps=[S("Explain", text="Yeast ferments sugar and gives off carbon dioxide, which is trapped by the gluten.")],
           concept="Yeast fermentation", skill="Concept", hint="It is the gas in fizzy drinks."),
        NUM("A teaching recipe for 8 scones uses 200 g of flour. How much flour is needed for 20 scones, in g?", 500,
            steps=[S("Scaling factor", math=r"\frac{20}{8} = 2.5"), S("Multiply", math=r"200 \times 2.5 = 500")],
            unit="g", concept="Scaling a recipe", skill="Calculation", hint="Find the factor by dividing 20 by 8."),
        NUM("An equal-weight cake uses 3 eggs that weigh 180 g. How many grams of sugar are used?", 180,
            steps=[S("Equal weights", text="The sugar weighs the same as the eggs."), S("Answer", math=r"180 \text{ g}")],
            unit="g", concept="Equal-weight cakes", skill="Application", hint="Equal-weight means the same weight as the eggs."),
        MC("A student's bread did not rise. Her yeast was mixed with water at 80 degrees Celsius. Which is the best explanation?", [
            C("The water was too cold", why="80 degrees is not cold."),
            C("The heat killed the yeast, so no gas was produced", correct=True),
            C("The yeast was too active", why="Heat of this degree kills yeast; it does not make it more active."),
            C("The flour had too much gluten", why="Gluten does not stop gas being produced."),
        ], steps=[S("Explain", text="Yeast dies above about 55 to 60 degrees Celsius. Dead yeast cannot ferment.")],
           concept="Faults in bread", skill="Reasoning", hint="What happens to a living organism in very hot water?"),
        MC("A cook wants a light sponge cake with very little fat. Which method is the most suitable?", [
            C("Rubbing-in", why="Rubbing-in needs fat to rub in."),
            C("Whisking eggs and sugar until thick, then folding in flour", correct=True),
            C("Boiling the flour in water", why="This makes a paste, not a sponge."),
            C("Kneading with yeast for an hour", why="This makes bread."),
        ], steps=[S("Decide", text="A whisked sponge traps air in eggs and sugar, with little or no fat.")],
           concept="Whisking method", skill="Application", hint="Which method relies on air trapped in eggs?"),
    ]))


def _spread_correct_options():
    """Move the correct option of each multiple-choice question so answers are spread over A-D."""
    for si, s in enumerate(SETS):
        for qi, q in enumerate(s["questions"]):
            if q["kind"] != "choice":
                continue
            ch = q["choices"]
            k = next(i for i, c in enumerate(ch) if c["correct"])
            c = ch.pop(k)
            ch.insert((qi + si) % 4, c)


_spread_correct_options()
