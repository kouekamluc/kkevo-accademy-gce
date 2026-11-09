"""Form 5 Food and Nutrition: Principles & Methods of Cooking, and Food Commodities, Flour Mixtures & Raising Agents
(13 lessons, one practice set each)."""

from .dsl import *  # noqa: F403

COURSE = ("food-and-nutrition", "form-5")

M3 = "Principles & Methods of Cooking"
M4 = "Food Commodities, Flour Mixtures & Raising Agents"

LESSONS = []

# ------------------------------------------------------------------ 1. Why we cook and how heat travels
LESSONS.append(lesson(
    module=M3,
    topic="Why we cook and how heat travels",
    title="Why we cook food and the three ways heat travels",
    slug="fdn2-why-we-cook-and-heat-transfer",
    minutes=20,
    summary="The reasons for cooking food, and how heat reaches food by conduction, convection and radiation, with everyday Cameroonian examples.",
    objectives=[
        "Give five reasons for cooking food",
        "Define conduction, convection and radiation",
        "Identify which kind of heat transfer is at work in a cooking situation",
        "Explain why a pan is metal and its handle is wood or plastic",
    ],
    key_concepts=["Reasons for cooking", "Conduction", "Convection", "Radiation", "Conductor", "Insulator"],
    blocks=[
        H("Introduction"),
        T("A tomato can be eaten raw, but most of us boil, fry or grill our food. In a Cameroonian kitchen, a pot of ndole simmers on a gas ring, "
          "fish is grilled over charcoal at a roadside, and bread is baked in an oven. Each of these uses heat. "
          "To cook well, you need to know why we cook and how the heat gets from the fire into the food."),
        H("Why we cook food"),
        D("**Cooking** is the preparation of food by the use of heat, so that it is safe, easier to digest and pleasant to eat.", title="Definition: cooking"),
        KEY("Reasons for cooking", "Learn these reasons in groups.", cards=[
            ["Safety", "Heat kills harmful micro-organisms (bacteria) and some poisons in raw foods. Properly cooked food is safer to eat."],
            ["Digestion", "Heat softens fibre and changes starch and protein, so the body digests the food more easily."],
            ["Taste and appearance", "Cooking develops flavour, aroma, colour and texture, for example the brown crust on bread."],
            ["Variety", "One food can be boiled, fried, roasted or baked, so meals are more interesting."],
            ["Keeping quality", "Cooked food, properly stored, keeps longer than some raw foods, and cooking stops enzymes that spoil food."],
        ]),
        T("Some cooked foods also become easier to chew: a hard cocoyam or a dry bean is almost impossible to eat raw, but becomes soft after cooking."),
        H("Heat travels in three ways"),
        T("Heat is a form of energy that moves from a hotter place to a cooler place. In the kitchen it reaches food in three ways. "
          "In many dishes, two or three of them work at the same time."),
        D("**Conduction** is the movement of heat through a solid, or between solids that touch, from particle to particle. "
          "Metals are good **conductors**; wood, plastic, and air are poor conductors, called **insulators**.", title="Definition: conduction"),
        D("**Convection** is the movement of heat through a liquid or a gas by currents. The heated part becomes lighter and rises, "
          "and the cooler, heavier part sinks to take its place, so a circular current forms.", title="Definition: convection"),
        D("**Radiation** is heat travelling in rays (infrared waves) straight from a hot object. It needs no solid, liquid or gas to carry it, "
          "and the rays heat the surface of the food they strike.", title="Definition: radiation"),
        IMG("f5fdn2-heat-transfer.svg",
            alt="Three panels: a metal pan over a fire (conduction through the metal), a pot of water with circular arrows (convection currents), and a fish above hot charcoal with rays rising (radiation)",
            caption="Figure 1. Conduction, convection and radiation in the kitchen."),
        KEY("Match the method to the example", "Look for what carries the heat.", cards=[
            ["Conduction", "Heat passes from the flame through the metal base of the pan, and from the pan into the food touching it."],
            ["Convection", "Hot water at the bottom of the pot rises and cooler water sinks, so the whole pot heats. Hot air in an oven moves in the same way."],
            ["Radiation", "Fish grilled over glowing charcoal is cooked by rays from the coals. A fire's heat on your face is also radiation."],
        ]),
        H("Why pans are metal and handles are not"),
        T("A saucepan is made of metal such as aluminium because metals are good conductors: the heat passes quickly to the food. "
          "The handle is made of wood or plastic, which are insulators, so that it stays cool enough to hold. "
          "A wooden spoon is used to stir a hot pot for the same reason."),
        EX("Worked example 1: heat transfer in boiling water", intro="Explain how the water in a pot on a charcoal stove becomes hot all the way through.", steps=[
            S("Conduction first", text="Heat passes from the burning charcoal through the metal base of the pot to the water touching it."),
            S("Convection next", text="The water at the bottom becomes hot, lighter and rises. Cooler, heavier water from the top sinks to the bottom."),
            S("The current continues", text="This circular movement spreads the heat through all the water until it boils."),
            S("Answer", text="Conduction heats the water at the base; convection currents carry the heat through the rest of the water."),
        ]),
        EX("Worked example 2: grilled fish", intro="A woman grills fish over a charcoal fire (poisson braise). Name the type of heat transfer and say why the fish is turned over.", steps=[
            S("Name the type", text="The fish is cooked mainly by radiation: rays travel from the glowing coals to the surface of the fish."),
            S("Other types", text="The metal grid touching the fish also conducts a little heat, and hot air rising around it carries heat by convection."),
            S("Why turn it", text="Radiation heats only the side facing the coals. Turning the fish cooks both sides evenly and stops one side from burning."),
        ]),
        TIP("The Board's 2023 report says that the question on reasons for cooking food was the least attempted in Paper 2, and that teachers were asked to give these topics more emphasis. "
            "Learn the reasons for cooking well. Heat transfer is tested in Paper 1 multiple-choice items and as part of Paper 2 answers on cooking methods.", title="Exam link"),
        MISTAKE("Saying that heat rises", "Hot air and hot water rise (convection), but heat itself travels in every direction. In a pan, the heat moves sideways and up by conduction, so never say 'heat always rises'."),
        MISTAKE("Giving one reason only", "A question on reasons for cooking usually expects several separate points: safety, digestion, flavour, texture, appearance, variety. Do not repeat the same point in different words."),
        QUIZ("A wooden spoon is left standing in a hot pot of stew. The handle stays cool. Why?", [
            "Wood is a good conductor of heat",
            "Wood is a poor conductor (an insulator) of heat",
            "Wood reflects all the heat back into the pot",
            "Convection currents cannot reach wood",
        ], 1, "Wood is an insulator: heat passes through it very slowly by conduction, so the end in your hand stays cool.",
            hint="Which kind of material lets heat move through it slowly?",
            feedback=["A good conductor, like metal, would make the handle hot quickly.", "", "Wood absorbs some heat; the point is that it conducts it slowly.", "Convection happens in liquids and gases, not in solid wood; the handle is cool because wood conducts poorly."]),
        QUIZ("Which cooking situation is MAINLY heating by radiation?", [
            "Water boiling in a pot",
            "Soup heated by a metal ladle left in the pot",
            "Meat held over glowing charcoal",
            "Oil heating at the bottom of a frying pan",
        ], 2, "Heat from the glowing charcoal reaches the meat as rays, without needing contact: this is radiation.",
            hint="Which one has no contact between the food and the heat source?",
            feedback=["Boiling water is mainly conduction through the pot and convection in the water.", "A metal ladle gets hot by conduction.", "", "Oil in a pan is heated by conduction through the base, then convection currents."]),
        PQ("State five reasons for cooking food.", "Any five of: to kill harmful micro-organisms and make food safe; to make food easier to digest; to improve flavour and aroma; to improve colour and appearance; to soften food and improve texture; to give variety to meals; to help food keep longer."),
        PQ("Name the three methods of heat transfer and give one kitchen example of each.", "Conduction: heat passing through the base of a metal pan to the food. Convection: currents of hot water rising and cool water sinking in a pot. Radiation: grilling fish over glowing charcoal."),
        PQ("Why is the base of a cooking pot made of metal while the handle is made of plastic or wood?", "Metal is a good conductor, so heat passes quickly into the food. Plastic or wood are insulators, so the handle stays cool and can be held safely."),
        PQ("Explain why an oven heats food even though the food does not touch the heating element.", "Hot air near the element rises and moves round the oven by convection, and the element also gives off rays (radiation) that strike the food. Heat then moves into the food by conduction from the outside."),
        SUM("Food is cooked to make it safe, easy to digest, tasty, attractive and varied.",
            "Conduction: heat passes through solids by contact; metals conduct well, wood and plastic are insulators.",
            "Convection: heat is carried by currents in liquids and gases; the hot part rises, the cool part sinks.",
            "Radiation: heat travels as rays from a hot object and needs no contact.",
            "Most real cooking uses two or three of these methods together."),
    ],
))

# ------------------------------------------------------------------ 2. Moist methods of cooking
LESSONS.append(lesson(
    module=M3,
    topic="Moist methods of cooking",
    title="Moist methods: boiling, simmering, poaching, steaming, stewing, braising and pressure cooking",
    slug="fdn2-moist-methods-of-cooking",
    minutes=22,
    summary="How seven moist cooking methods work, what temperature each uses, which foods suit each, and their advantages and disadvantages.",
    objectives=[
        "Define the seven moist methods of cooking",
        "Choose a suitable method and food for a given situation",
        "State the advantages and disadvantages of moist methods",
        "Explain how a pressure cooker saves time and fuel",
    ],
    key_concepts=["Boiling", "Simmering", "Poaching", "Steaming", "Stewing", "Braising", "Pressure cooking"],
    blocks=[
        H("Introduction"),
        T("In a moist method of cooking, the heat is carried to the food by **water, other liquid or steam**. "
          "Think of boiled plantains, koki steamed in leaves, fish pepper soup, or beans cooked in a pressure cooker. "
          "Moist methods do not brown food, and they suit tough foods that need long, gentle cooking."),
        D("A **moist method** of cooking is one in which food is cooked in a hot liquid (such as water, stock or milk) or in steam.", title="Definition: moist method"),
        H("The seven methods"),
        D("**Boiling**: food is cooked in a liquid kept at its boiling point, about 100 degrees Celsius at sea level, with large bubbles breaking on the surface. "
          "It is quick but rough, so delicate foods can break up.", title="Definition: boiling"),
        D("**Simmering**: food is cooked in a liquid kept just below boiling point, with only a few small bubbles. "
          "It is gentler than boiling and suits tougher foods, soups and sauces.", title="Definition: simmering"),
        D("**Poaching**: food is cooked in a liquid that barely moves, below simmering point. "
          "It suits delicate foods such as eggs and fish, which would break up if boiled.", title="Definition: poaching"),
        D("**Steaming**: food is cooked by the steam from boiling water and does not touch the water. "
          "Examples are koki and other puddings wrapped in leaves, steamed fish and steamed vegetables.", title="Definition: steaming"),
        D("**Stewing**: food cut into small pieces is cooked slowly in a small amount of liquid in a covered pan, and the liquid is served with the food. "
          "It suits tough meat and cheaper cuts; fish and chicken stews are popular.", title="Definition: stewing"),
        D("**Braising**: food (usually meat) is first browned in fat, then cooked slowly in a covered pot with a little liquid, on a bed of vegetables. "
          "It is used for large, tough pieces.", title="Definition: braising"),
        D("**Pressure cooking**: food is cooked in a sealed pot in which steam pressure builds up. The pressure raises the boiling point of water to about 120 degrees Celsius, "
          "so the food cooks much faster.", title="Definition: pressure cooking"),
        CODE("""Method      Liquid temperature        Typical food
Boiling     about 100 C, bubbling      rice, yam, eggs, pasta
Simmering   just below 100 C           soups, tough meat, beans
Poaching    well below boiling, still  eggs, fish
Steaming    steam above the water      koki, vegetables, fish
Stewing     small amount of liquid     tough meat, chicken, fish
Braising    browned, then covered      large pieces of tough meat
Pressure    sealed pot, about 120 C    beans, tough meat, cocoyam""", "text", title="Table 1. Moist methods compared"),
        T("The boiling point of water falls a little at high altitude, because the air pressure is lower. "
          "In a town like Bamenda, water boils a few degrees below 100 degrees Celsius, so food takes longer. A pressure cooker removes this problem."),
        H("Advantages and disadvantages"),
        KEY("Moist methods: strengths and weaknesses", "Compare them in an answer.", cards=[
            ["Advantages", "Easy and cheap; little attention; no fat needed so the food is lower in fat; tenderises tough foods; steaming keeps the shape, colour and many nutrients; one pot can cook a whole meal."],
            ["Disadvantages", "No brown crust or crisp texture; water-soluble vitamins (B and C) and minerals dissolve into the water and may be thrown away; overcooking makes food soft and tasteless."],
        ]),
        EX("Worked example 1: choosing a method", intro="Choose the most suitable moist method for (a) a whole egg that must not crack, (b) tough goat meat, and (c) a delicate piece of fish. Give a reason for each.", steps=[
            S("Egg", text="Simmer or poach (or boil gently from cold water). Rapid boiling makes the egg knock against the pan and crack."),
            S("Tough goat meat", text="Stew or braise, or use a pressure cooker. Long, slow cooking in liquid changes the tough connective tissue into soft gelatine."),
            S("Delicate fish", text="Poach or steam. Rough boiling would break the flaky flesh into pieces."),
        ]),
        EX("Worked example 2: the pressure cooker", intro="Explain why dried beans cook faster in a pressure cooker than in an open pot, and why this saves fuel.", steps=[
            S("The pot is sealed", text="Steam cannot escape, so the pressure inside rises."),
            S("The boiling point rises", text="At higher pressure, water boils at about 120 degrees Celsius, not 100."),
            S("The food is hotter", text="The beans are surrounded by water and steam hotter than in an open pot, so they soften in a much shorter time."),
            S("Fuel saving", text="A shorter cooking time means less gas, charcoal or firewood is used. This helps a family that buys fuel."),
        ]),
        TIP("Paper 2 questions often ask you to define two or three methods and give a suitable food for each. Always give a **named food** and a **reason**. "
            "In Paper 3, a practical question may also expect you to keep the liquid at the right level: a gentle simmer, not a hard boil.", title="Exam link"),
        MISTAKE("Confusing simmering and boiling", "Simmering has only small bubbles and a gentle movement; boiling has large bubbles and heavy movement. Most recipes that say 'boil' for meat and soup really want a simmer, because a hard boil toughens meat and breaks up delicate food."),
        MISTAKE("Saying steaming and boiling are the same", "In steaming the food does NOT touch the water; it is cooked by the steam above the water, so fewer nutrients dissolve away."),
        QUIZ("In which method does the food NOT touch the boiling water?", [
            "Simmering", "Steaming", "Poaching", "Stewing",
        ], 1, "In steaming, the food is held above the water and is cooked by the steam only.",
            hint="Which method uses the vapour from boiling water, not the water?",
            feedback=["In simmering the food sits in the liquid.", "", "In poaching the food sits in a gently moving liquid.", "Stewing keeps the food in a small amount of liquid."]),
        QUIZ("Tough, cheap cuts of meat are best cooked by", [
            "Rapid boiling for 5 minutes", "Slow stewing or braising", "Steaming for 5 minutes", "Poaching in cold water",
        ], 1, "Long, slow cooking in liquid turns the tough connective tissue into gelatine, so the meat becomes tender.",
            hint="Tough meat needs time and moisture.",
            feedback=["A short time leaves it tough.", "", "A short time leaves it tough.", "Poaching is for delicate foods and is gentle but not long enough for tough meat."]),
        PQ("Define simmering and name two foods suitable for this method.", "Simmering is cooking in liquid kept just below boiling point, with small bubbles. Suitable foods are soups and tough meats (also beans or stock)."),
        PQ("State three advantages of cooking by moist methods.", "No added fat is needed; tough foods are made tender; little attention is needed; steaming keeps colour and many nutrients; one pot can cook the whole meal. (Any three.)"),
        PQ("State two disadvantages of boiling vegetables in a lot of water.", "Water-soluble vitamins (B and C) and minerals dissolve into the water and are lost if it is thrown away; the vegetables become soft, lose colour and flavour if overcooked."),
        PQ("Explain how a pressure cooker cooks food more quickly than an ordinary pot.", "The lid seals the pot so steam pressure builds up. The higher pressure raises the boiling point of water to about 120 degrees Celsius, so the food is cooked at a higher temperature in less time."),
        SUM("Moist methods cook with water, other liquid or steam: boiling, simmering, poaching, steaming, stewing, braising and pressure cooking.",
            "Boiling is at about 100 degrees Celsius with large bubbles; simmering is just below; poaching is gentler still.",
            "Stewing and braising use slow cooking in a little liquid to make tough meat tender; braising begins with browning.",
            "Steaming cooks with steam only and keeps more nutrients; pressure cooking is faster and saves fuel.",
            "Disadvantages: no browning, and water-soluble nutrients may be lost in the cooking water."),
    ],
))

# ------------------------------------------------------------------ 3. Dry methods of cooking
LESSONS.append(lesson(
    module=M3,
    topic="Dry methods of cooking",
    title="Dry methods: baking, roasting and grilling",
    slug="fdn2-dry-methods-of-cooking",
    minutes=20,
    summary="How baking, roasting and grilling cook food with dry heat, which foods suit each, how to use an oven, and their advantages and disadvantages.",
    objectives=[
        "Define baking, roasting and grilling",
        "Explain how heat reaches food in each method",
        "Choose a suitable food and method for a situation",
        "State advantages and disadvantages of dry methods",
    ],
    key_concepts=["Baking", "Roasting", "Grilling", "Basting", "Pre-heating", "Browning"],
    blocks=[
        H("Introduction"),
        T("The smell of bread from a bakery, roasted plantain and fish at a street corner, and soya (spiced grilled meat) in the evening all come from **dry methods of cooking**. "
          "Here the food is cooked by hot air, radiant heat or hot fat, not in water. The surface browns, becomes crisp and develops a rich flavour."),
        D("A **dry method** of cooking uses dry heat, such as hot air in an oven, or rays from a fire or heater, without cooking the food in water or steam.", title="Definition: dry method"),
        H("Baking"),
        D("**Baking** is cooking food by hot, dry air in a closed oven. The heat reaches the food by convection and radiation, then passes inside by conduction.", title="Definition: baking"),
        T("Bread, cakes, pastries, buns, biscuits and baked fish or potatoes are baked. Always **pre-heat** the oven, which means switching it on in time to reach the right temperature before the food goes in. "
          "Putting cake into a cold oven spoils its rise."),
        CODE("""Oven setting (teaching guide, check your cooker)
Cool/slow      about 150 C       meringues, rich fruit cakes
Moderate       about 180 C       sponge cakes, scones, biscuits
Hot            about 200-220 C   bread, pastry, roasting""", "text", title="Table 1. Typical oven temperatures"),
        H("Roasting"),
        D("**Roasting** is cooking meat, poultry or vegetables by dry heat, with a little fat, in an oven or over an open fire. "
          "The food is **basted**, which means spooned over with its hot fat, to keep it moist and help it brown.", title="Definition: roasting"),
        T("Chicken, goat meat and potatoes can be roasted in an oven. Roasted corn and plantain over charcoal are also called roasting in everyday speech. "
          "Roasting needs a good cut of meat; tough cuts would stay tough in dry heat unless cooked slowly."),
        H("Grilling"),
        D("**Grilling** is cooking food quickly by radiant heat from a glowing source, such as charcoal or a hot electric element or gas grill, above or below the food. "
          "The food is turned so both sides cook.", title="Definition: grilling"),
        T("Fish (poisson braise), soya, sausages, chops and toast are grilled. Use tender, thin pieces, because grilling is fast and does not soften tough meat. "
          "Brush the food with a little oil to stop it drying out."),
        IMG("f5fdn2-heat-transfer.svg",
            alt="Three panels showing conduction, convection and radiation; the third shows fish above hot charcoal",
            caption="Figure 1. Grilling uses radiation from the coals (panel on the right)."),
        KEY("Dry methods: strengths and weaknesses", "Compare them in an answer.", cards=[
            ["Advantages", "Brown, crisp surface and a rich flavour; little or no water, so fewer water-soluble nutrients are lost; baking suits large amounts; grilling is quick and lets fat drip away."],
            ["Disadvantages", "Food can dry out or burn; tough cuts stay tough; ovens and fuel can be costly; roasting and baking take a long time; some vitamins are lost to high heat."],
        ]),
        EX("Worked example 1: choosing a dry method", intro="Name the best dry method for (a) bread, (b) a whole chicken for a family meal, (c) thin slices of fish at a roadside, and give a reason.", steps=[
            S("Bread", text="Baking: the dough needs hot, even air in an oven so it rises, sets and forms a crust."),
            S("Whole chicken", text="Roasting: a tender bird cooks slowly in the oven and is basted to keep it moist."),
            S("Thin fish", text="Grilling: radiation from hot charcoal cooks thin pieces quickly, and the surface browns."),
        ]),
        EX("Worked example 2: a better roast", intro="A student's roast chicken came out dry on the outside and pink near the bone. Give three causes and a remedy for each.", steps=[
            S("Oven too hot", text="Remedy: cook at a moderate temperature for longer, so the heat reaches the centre before the outside dries."),
            S("No basting or fat", text="Remedy: baste with the hot fat or cover loosely with foil to keep the meat moist."),
            S("Cooking time too short for the weight", text="Remedy: calculate the time from the weight, and check that the juices run clear. Poultry must be cooked right through to be safe."),
        ]),
        TIP("Cake, bread and pastry questions in Paper 2 and Paper 3 often depend on oven use: pre-heat, place the food on the right shelf, avoid opening the door too early, and cool on a wire rack. "
            "Give the method AND the reason (for example, 'bake: hot dry air sets the crust').", title="Exam link"),
        MISTAKE("Grilling thick, tough meat", "Grilling is quick. A thick, tough cut will burn outside before it softens. Use thin tender pieces, or tenderise first, or choose a moist method."),
        MISTAKE("Forgetting to pre-heat", "A cold oven means the food heats slowly and does not rise or brown correctly. Switch on the oven in good time."),
        QUIZ("Which method is BEST described as 'cooking by radiant heat from a glowing source above or below the food'?", [
            "Baking", "Roasting", "Grilling", "Stewing",
        ], 2, "Grilling uses rays from hot charcoal, gas or an electric element.",
            hint="Think of fish over charcoal.",
            feedback=["Baking uses hot air in a closed oven.", "Roasting is slower, with fat, and usually in an oven.", "", "Stewing is a moist method."]),
        QUIZ("Basting a roast chicken means", [
            "Covering it with flour", "Spooning hot fat over it during cooking", "Boiling it first", "Turning off the oven",
        ], 1, "Basting keeps the meat moist and helps it brown.",
            hint="Think of what keeps the surface from drying.",
            feedback=["Flour would form a coat, not baste it.", "", "This is not basting.", "The oven stays on."]),
        PQ("Define baking and name three foods that are baked.", "Baking is cooking by hot, dry air in a closed oven. Examples: bread, cakes, pastries, biscuits, scones."),
        PQ("State three advantages of grilling food.", "It is quick; little fat is needed and fat drips away; it gives a brown crisp surface and good flavour; fewer nutrients are lost than in boiling. (Any three.)"),
        PQ("Why should an oven be pre-heated before baking a cake?", "The cake needs the correct temperature from the start so the raising agent works, the mixture sets and rises evenly, and the cake does not sink."),
        PQ("Give two differences between roasting and grilling.", "Roasting is slow, in an oven or on a spit, with fat and basting, for larger pieces; grilling is fast, by radiant heat from above or below, for thin tender pieces that are turned."),
        SUM("Dry methods use hot air, radiant heat or hot fat, with no cooking in water.",
            "Baking: hot dry air in an oven (bread, cakes); pre-heat the oven first.",
            "Roasting: dry heat with a little fat and basting (chicken, potatoes).",
            "Grilling: fast cooking by radiation from a glowing source; use thin tender pieces and turn them.",
            "Dry methods give brown, crisp, tasty food but can dry out or burn it."),
    ],
))

# ------------------------------------------------------------------ 4. Frying
LESSONS.append(lesson(
    module=M3,
    topic="Frying",
    title="Frying: shallow, deep and dry frying",
    slug="fdn2-frying",
    minutes=20,
    summary="The three kinds of frying, how to fry safely and well, why fried food is high in energy, and how to deal with a pan fire.",
    objectives=[
        "Define shallow frying, deep frying and dry frying",
        "Give local examples of foods cooked by each kind of frying",
        "State rules for frying safely and well",
        "State advantages and disadvantages of frying and compare the energy in fat with other nutrients",
    ],
    key_concepts=["Shallow frying", "Deep frying", "Dry frying", "Coating", "Smoking point", "Energy value of fat"],
    blocks=[
        H("Introduction"),
        T("Fried plantain, puff-puff, beignets, fried fish, chips and fried eggs are loved in Cameroon. "
          "**Frying** cooks food in hot fat or oil. Fat can be heated far above the boiling point of water, so frying is fast and gives a golden, crisp surface. "
          "The same speed makes frying risky, so it needs care."),
        D("**Frying** is cooking food in hot fat or oil. The heat passes from the pan to the fat by conduction, through the fat by convection and into the food by conduction.", title="Definition: frying"),
        H("The three kinds of frying"),
        D("**Shallow frying**: food is cooked in a thin layer of hot fat, not enough to cover the food, and turned once. "
          "Examples: fried eggs, fish fillets, fried plantain slices, pancakes, sausages.", title="Definition: shallow frying"),
        D("**Deep frying**: food is completely covered with hot oil in a deep pan, at about 180 degrees Celsius. "
          "Examples: chips, puff-puff, beignets, doughnuts, chin-chin, fish in batter. The food is often coated first.", title="Definition: deep frying"),
        D("**Dry frying**: food is cooked in a pan with no added fat, using its own fat or none. "
          "Examples: bacon and sausages (which release fat), and roasting groundnuts or spices in a dry pan.", title="Definition: dry frying"),
        T("In **stir frying**, small pieces are tossed quickly in a little hot oil. It is a form of shallow frying."),
        H("Frying well"),
        KEY("Rules for good frying", "Heat, dryness and coating are the key.", cards=[
            ["Heat the fat first", "Food added to fat that is not hot enough soaks up fat and is greasy. Teaching test: a small cube of bread should turn golden in about a minute in oil for deep frying."],
            ["Dry the food", "Wet food makes hot fat spit and splash. Pat food dry. Never add water to hot oil."],
            ["Coat some foods", "A coat of flour, batter or egg and crumbs forms a crisp seal that cuts the fat absorbed and holds soft food together."],
            ["Do not overfill", "Too much food cools the oil, so the food becomes oily. Fry in small batches."],
            ["Drain", "Lift out and drain on kitchen paper to remove surplus fat."],
        ]),
        H("Safety"),
        T("Hot fat causes serious burns and fires. Never leave a frying pan unattended. Keep the handle turned inward. Never fill a deep pan more than half full. "
          "If fat catches fire, **switch off the heat and cover the pan with a lid or damp cloth. Never pour water on it.** Water turns to steam suddenly and throws burning fat out. "
          "Oil that has been used again and again, or heated until it smokes, breaks down and is harmful, so do not reuse it endlessly."),
        H("Energy in fried food"),
        T("Fat gives more energy than other nutrients. Each gram of fat gives about 37 kJ, but each gram of carbohydrate or protein gives about 17 kJ. "
          "Fried foods hold extra fat, so they are high in energy. People who eat a lot of fried food may gain weight."),
        EX("Worked example 1: fat absorbed in frying", intro="A serving of boiled potato and a serving of chips each have the same weight of potato. The chips absorb 15 g of oil in frying (a figure invented for practice). "
           "How much extra energy do the chips contain, using 37 kJ per gram of fat?", steps=[
            S("Find the extra fat", text="The chips hold 15 g of added oil; the boiled potato holds none."),
            S("Multiply", math=r"15 \times 37 = 555 \text{ kJ}"),
            S("Conclusion", text="The chips contain about 555 kJ more energy than the boiled potato from the oil alone."),
        ], check=r"15 \times 37 = 555"),
        EX("Worked example 2: choosing the kind of frying", intro="Choose the kind of frying for (a) a fried egg, (b) puff-puff dough, (c) roasting groundnuts, and say why.", steps=[
            S("Fried egg", text="Shallow frying: a thin layer of oil is enough for a flat food that is turned or basted."),
            S("Puff-puff", text="Deep frying: the dough balls must be covered in hot oil so they puff up and brown all round."),
            S("Groundnuts", text="Dry frying: the nuts have their own oil, so no extra fat is added; stir to avoid burning."),
        ]),
        KEY("Advantages and disadvantages of frying", "Both sides in an answer.", cards=[
            ["Advantages", "Quick; crisp, brown surface; good flavour; gives variety; a small amount of food can be cooked in a few minutes."],
            ["Disadvantages", "High in fat and energy; fat can burn or catch fire; fatty food is harder to digest; over-heated oil is unhealthy; fried food often loses some vitamins."],
        ]),
        TIP("The Board's 2023 report notes that candidates did well on questions about avoiding kitchen accidents, so expect safety in frying to appear. "
            "A Paper 3 practical question may ask you to fry a food: heat the fat first, drain, and serve hot and neat.", title="Exam link"),
        MISTAKE("Putting out a fat fire with water", "Water sinks below the oil, turns to steam instantly and sprays burning fat. Cover the pan, turn off the heat, and let it cool."),
        MISTAKE("Frying in cold oil", "Food put into oil that is not hot enough absorbs too much fat and becomes greasy and soggy. Test the heat before adding food."),
        QUIZ("Which food is cooked by deep frying?", [
            "A fried egg", "Puff-puff", "Roasted groundnuts in a dry pan", "Boiled plantain",
        ], 1, "Puff-puff dough is completely covered in hot oil, which is deep frying.",
            hint="Which food is covered completely by oil?",
            feedback=["A fried egg is shallow fried.", "", "Dry-pan groundnuts are dry fried.", "Boiling uses water."]),
        QUIZ("A pan of oil catches fire. The first correct action is to", [
            "Pour water on it", "Move it outside while burning", "Switch off the heat and cover the pan with a lid", "Fan it with a cloth",
        ], 2, "Switching off the heat and covering the pan cuts off the air, so the fire goes out.",
            hint="What does a fire need besides fuel and heat?",
            feedback=["Water makes burning fat spray out.", "Carrying burning oil may spill it and burn you.", "", "Fanning supplies more air and makes the fire worse."]),
        PQ("Define deep frying and give two local examples.", "Deep frying is cooking food completely covered in hot oil, at about 180 degrees Celsius. Examples: puff-puff, chips, beignets, chin-chin."),
        PQ("State four rules for safe frying.", "Never leave the pan; do not fill it more than half full; keep the handle inward; dry the food; do not add water to hot oil; cover the pan if fat catches fire and switch off the heat. (Any four.)"),
        PQ("Why is fried food high in energy?", "Food absorbs fat during frying, and fat gives about 37 kJ per gram, more than double the energy per gram of carbohydrate or protein."),
        PQ("Why are some foods coated with batter or flour before deep frying?", "The coating forms a crisp seal that reduces the amount of fat absorbed, protects soft foods such as fish from breaking up, and gives a golden, crunchy surface."),
        SUM("Frying cooks food in hot fat or oil: shallow, deep or dry.",
            "Heat the fat before adding the food, dry the food, coat soft foods, do not overfill, and drain.",
            "Never leave hot fat unattended; for a fat fire, switch off the heat and cover the pan, never use water.",
            "Fat gives about 37 kJ per gram, so fried foods are rich in energy.",
            "Frying is quick and gives crisp, tasty food, but it is fatty and can be dangerous."),
    ],
))

# ------------------------------------------------------------------ 5. Effects of heat on nutrients
LESSONS.append(lesson(
    module=M3,
    topic="Effects of heat on nutrients",
    title="What heat does to nutrients, and how to keep them",
    slug="fdn2-effects-of-heat-on-nutrients",
    minutes=22,
    summary="How cooking changes proteins, carbohydrates, fats, vitamins and minerals, and the rules that keep nutrient losses small.",
    objectives=[
        "Describe the effect of heat on proteins, starch, sugar and fats",
        "Explain how vitamins and minerals are lost in cooking",
        "State ways of reducing nutrient losses when preparing and cooking vegetables",
        "Calculate the amount of a nutrient left after a given percentage loss",
    ],
    key_concepts=["Coagulation", "Gelatinisation", "Dextrinisation", "Caramelisation", "Water-soluble vitamins", "Nutrient retention"],
    blocks=[
        H("Introduction"),
        T("Cooking makes food safe and tasty, but heat also changes the nutrients inside. Some changes are useful, such as softening starch. "
          "Others are harmful, such as the loss of vitamin C. A good cook keeps the useful changes and avoids the losses. "
          "This lesson looks at each nutrient in turn. Only well-established changes are described."),
        H("Proteins"),
        D("**Coagulation** is the change in protein, when heated, from a liquid or soft form into a firm, solid form. The protein is **denatured**: its shape changes permanently.", title="Definition: coagulation"),
        T("The white of an egg turns from clear liquid to white solid. Meat and fish become firm. This makes the food easier to eat, but too much heat makes protein **shrink and toughen**: overcooked egg is rubbery and overcooked meat is dry and hard. Also, some browning reactions between protein and sugar reduce the usable amount of a few amino acids."),
        H("Carbohydrates"),
        D("**Gelatinisation**: starch grains heated with water absorb the water, swell and burst, and the mixture thickens. This is how a pap, a sauce or a pot of rice thickens and becomes digestible.", title="Definition: gelatinisation"),
        D("**Dextrinisation**: dry heat breaks starch into shorter pieces called dextrins. It browns the surface of toast, bread crust and roasted plantain.", title="Definition: dextrinisation"),
        D("**Caramelisation**: sugar heated alone melts and turns brown, forming caramel with a sweet, slightly bitter flavour.", title="Definition: caramelisation"),
        T("Cellulose (the fibre in vegetables) is softened by heat, but it is not digested by humans. Softening makes vegetables easier to chew."),
        H("Fats"),
        T("Solid fats **melt** when heated and become liquid oil. Fats do not mix with water. At high temperatures fat begins to give off blue smoke (its **smoking point**) and breaks down, with an unpleasant taste and harmful substances. "
          "Fat that is used again and again breaks down faster. The fat-soluble vitamins (A, D, E and K) dissolve in the fat, so when fat is thrown away or drips out, those vitamins go with it."),
        H("Vitamins and minerals"),
        KEY("How vitamins are lost", "Remember three causes: water, heat and air.", cards=[
            ["Vitamin C", "The least stable vitamin. It dissolves in water, is destroyed by heat and by air (oxidation), and by bicarbonate of soda."],
            ["B vitamins", "Water-soluble, so they dissolve in cooking water. Thiamin (B1) is also destroyed by heat and by bicarbonate of soda."],
            ["Vitamins A, D, E, K", "Fat-soluble and fairly stable to ordinary cooking, but lost with the fat that drips away or is thrown out, and in over-heating."],
            ["Minerals", "Not destroyed by heat, but they dissolve in cooking water. They are lost only if the water is thrown away."],
        ]),
        H("Keeping the nutrients"),
        KEY("Rules for vegetables and other foods", "Short, small, covered, quick.", cards=[
            ["Preparing", "Use fresh vegetables. Wash before cutting, not after. Cut into large pieces, not tiny ones, to reduce the surface area. Peel thinly, since nutrients lie just under the skin. Do not soak cut vegetables."],
            ["Cooking", "Use a small amount of water or steam. Add the vegetables when the water is boiling. Use a lid. Cook for as short a time as possible. Do not add bicarbonate of soda."],
            ["After cooking", "Serve at once. Use the cooking water for soup or sauce. Do not keep food hot for hours."],
        ]),
        EX("Worked example 1: vitamin C left after cooking", intro="Fresh cabbage has 60 mg of vitamin C in a portion (a figure invented for practice). Boiling for a long time in much water destroys or washes out 70% of it. "
           "How much vitamin C is left?", steps=[
            S("Find the amount lost", math=r"\frac{70}{100} \times 60 = 42 \text{ mg}"),
            S("Subtract from the original", math=r"60 - 42 = 18 \text{ mg}"),
            S("State the answer", text="18 mg of vitamin C is left, which is 30% of the original."),
        ], check=r"0.30 \times 60 = 18"),
        EX("Worked example 2: improving a method", intro="Ndole leaves are boiled in a large pot for an hour and the water is poured away. Suggest three changes to keep more nutrients.", steps=[
            S("Less water and shorter time", text="Cook with only a little water for a shorter time so less vitamin C and B vitamins dissolve or are destroyed."),
            S("Keep the water", text="Use the cooking water in the sauce, because it holds dissolved minerals and vitamins."),
            S("Cover the pot", text="Use a lid so that cooking is quicker and less vitamin C is destroyed by air."),
        ]),
        TIP("A frequent Paper 2 question asks how to reduce nutrient losses when cooking vegetables. Give at least four separate rules, and say WHY for two of them "
            "(for example: use little water, because vitamins B and C dissolve in it). The Board's 2023 report asked teachers to stress the principles of food preparation.", title="Exam link"),
        MISTAKE("Saying that heat destroys minerals", "Minerals are elements and are not destroyed by heat. They are lost only because they dissolve in cooking water that is then thrown away."),
        MISTAKE("Adding bicarbonate of soda to keep greens green", "It keeps the colour but destroys vitamin C and thiamin. Do not add it."),
        QUIZ("Which vitamin is most easily lost in cooking?", [
            "Vitamin A", "Vitamin D", "Vitamin C", "Vitamin K",
        ], 2, "Vitamin C is water-soluble and is destroyed by heat and air, so it is the least stable.",
            hint="Which vitamin dissolves in water and is spoiled by heat?",
            feedback=["Vitamin A is fat-soluble and fairly stable.", "Vitamin D is fat-soluble and fairly stable.", "", "Vitamin K is fat-soluble and fairly stable."]),
        QUIZ("What happens to starch grains heated with water?", [
            "They turn to protein", "They absorb water, swell and thicken the liquid", "They become vitamin C", "They stay unchanged",
        ], 1, "This is gelatinisation: it makes the mixture thick and the starch easier to digest.",
            hint="Think of what happens to a pap as it cooks.",
            feedback=["Starch cannot turn into protein.", "", "Starch cannot become a vitamin.", "Heat and water change starch clearly."]),
        PQ("State four ways of reducing the loss of vitamin C when cooking green vegetables.", "Use fresh vegetables; cut into large pieces; cook in a small amount of water or steam; use a lid; cook for a short time; do not add bicarbonate of soda; serve immediately; use the cooking water. (Any four.)"),
        PQ("Explain what happens to the white of an egg when it is boiled, and what happens if it is overcooked.", "The protein coagulates: it changes from clear liquid to firm white solid. If overcooked, the protein shrinks and toughens, so the egg is rubbery."),
        PQ("A portion of spinach has 80 mg of vitamin C (invented for practice). After cooking, 25% is lost. How much is left?", "25% of 80 = 20 mg lost; 80 - 20 = 60 mg left."),
        PQ("Why are minerals lost when vegetables are boiled even though heat does not destroy them?", "Minerals dissolve in the cooking water. If the water is thrown away, the minerals go with it."),
        SUM("Protein coagulates with heat; overcooking toughens it.",
            "Starch gelatinises in water (thickens) and dextrinises in dry heat (browns); sugar caramelises.",
            "Vitamin C and the B vitamins are lost by dissolving in water and by heat and air; fat-soluble vitamins are lost with fat that is discarded.",
            "Minerals are not destroyed by heat but dissolve in cooking water.",
            "To keep nutrients: fresh food, large pieces, little water, a lid, a short time, no bicarbonate of soda, and use the cooking water."),
    ],
))

# ------------------------------------------------------------------ 6. Cereals
LESSONS.append(lesson(
    module=M4,
    topic="Cereals",
    title="Cereals: grain structure, nutritive value, storage and uses",
    slug="fdn2-cereals",
    minutes=20,
    summary="The structure of a cereal grain, what cereals give the body, how to store them, and how maize, rice, wheat, millet and sorghum are used in cooking.",
    objectives=[
        "Name the main cereals eaten in Cameroon",
        "Describe the three parts of a grain and the nutrients in each",
        "Explain how whole grain differs from refined grain",
        "State how cereals are stored and used in cooking",
    ],
    key_concepts=["Cereal", "Bran", "Endosperm", "Germ", "Wholegrain", "Refined", "Weevils"],
    blocks=[
        H("Introduction"),
        T("Fufu corn, rice and stew, bread, pap and millet couscous: cereals are the main staple food of most Cameroonian families. "
          "A **staple food** is the food eaten in the largest amount at most meals. This lesson looks at what a cereal is made of, what it gives the body, and how to store and cook it."),
        D("A **cereal** is the edible seed (grain) of a cultivated grass. The main cereals are **maize, rice, wheat, millet, sorghum, oats and barley**.", title="Definition: cereal"),
        T("Cassava, plantain, yam and cocoyam are **not** cereals: they are roots, tubers or fruit. In the northern regions, sorghum and millet are the main cereals; maize is grown widely; rice and wheat are grown and also imported."),
        H("Structure of a grain"),
        IMG("f5fdn2-grain.svg", alt="Section through a cereal grain showing the outer bran, the large endosperm and the small germ at the base",
            caption="Figure 1. A cereal grain has three parts: bran, endosperm and germ."),
        KEY("The three parts of a grain", "Know what each part contains.", cards=[
            ["Bran", "The tough outer coat. It is rich in **dietary fibre (NSP)**, B vitamins and minerals such as iron."],
            ["Endosperm", "The largest part, the food store of the seed. It is mostly **starch**, with some protein. White flour and white rice are mainly endosperm."],
            ["Germ", "The small embryo that can grow into a new plant. It contains **fat, protein, B vitamins and vitamin E**. It can turn rancid, so it is often removed."],
        ]),
        T("When grain is **refined** (milled to white flour or polished white rice), the bran and germ are removed. The product keeps well and is soft, but contains less fibre, B vitamins and minerals. "
          "**Wholegrain** products (wholemeal flour, brown rice, whole maize meal) keep all three parts."),
        H("Nutritive value"),
        T("About 70% of the dry weight of most cereals is **starch**, so cereals are the main source of **energy** in the diet. They contain a fair amount of protein (about 7 to 12%), but it is of **lower biological value** because it is short of an amino acid called lysine. "
          "A cereal eaten with **pulses** (beans, groundnuts) gives a good mixture of amino acids: this is why rice and beans, or corn and beans (corn chaff and beans is a well-known dish) are such good combinations. "
          "Cereals have little fat and no vitamin C. Wholegrain cereals supply B vitamins, iron and fibre."),
        H("Storage"),
        T("Store dry cereals and flour in clean, **dry, airtight containers** in a cool, dry, well-ventilated place, off the floor. Moisture allows moulds to grow, and warm damp stores invite **weevils** and other insects and rats. "
          "Keep old and new stock apart and use the older first. Do not store near strong-smelling substances."),
        H("Culinary uses"),
        CODE("""Cereal       Local and common uses
Maize        corn fufu, pap (corn pap), corn chaff and beans, roasted or boiled cobs
Rice         boiled rice with stew, fried rice, jollof rice, rice pudding
Wheat        bread, buns, pastry, pasta, doughnuts, cakes
Millet       porridge, couscous and drinks in the northern regions
Sorghum      porridge and couscous in the northern regions""", "text", title="Table 1. Cereals and their uses"),
        T("In cooking, starch **gelatinises**: it absorbs water, swells and thickens, so a cereal cooked in water becomes soft and digestible. Pap thickens for this reason. "
          "Wheat flour is special because it forms **gluten** with water, which gives bread its stretch. Rice is washed lightly and cooked with about the right amount of water, so that no water is thrown away and no vitamins are lost."),
        EX("Worked example 1: whole grain or refined?", intro="A family compares brown rice and white rice. Which is richer in fibre and B vitamins, and why?", steps=[
            S("Think of the parts", text="Brown rice keeps its bran and germ. White rice has them removed in polishing."),
            S("Bran and germ", text="The bran has fibre, B vitamins and minerals. The germ has fat, B vitamins and vitamin E."),
            S("Conclusion", text="Brown rice is richer in fibre and B vitamins. White rice is mostly starch and keeps longer."),
        ]),
        EX("Worked example 2: a balanced cereal meal", intro="Why is a meal of corn fufu and beans better for a growing child than corn fufu alone?", steps=[
            S("Cereal protein", text="Corn protein is short of lysine, so it has a lower biological value."),
            S("Pulse protein", text="Beans are rich in lysine but short of another amino acid (methionine)."),
            S("Complementary", text="Eaten together, each makes up for what the other lacks, so the mixture gives a better protein. Beans also add iron and fibre."),
        ]),
        TIP("The cereal topic appears in Paper 1 (grain structure, nutrient in the bran or germ, storage, correct examples) and in Paper 2 questions on food choices and food preparation, which the Board reported as the best-answered question in 2023. "
            "Always give a named local food as an example.", title="Exam link"),
        MISTAKE("Calling cassava or plantain a cereal", "Cereals are the seeds of grasses. Cassava is a root, plantain is a fruit, and yam and cocoyam are tubers."),
        MISTAKE("Saying that the germ is mostly starch", "The endosperm is mostly starch. The germ is small and contains fat, protein and vitamins."),
        QUIZ("Which part of the grain contains most of the starch?", [
            "Bran", "Germ", "Endosperm", "The husk"
        ], 2, "The endosperm is the food store of the grain and is mostly starch.",
            hint="White flour is made mainly from which part?",
            feedback=["The bran is mostly fibre, with vitamins and minerals.", "The germ has fat, protein and vitamins.", "", "The husk is the outer covering that is removed."]),
        QUIZ("Which is a cereal?", [
            "Cassava", "Maize", "Yam", "Plantain"
        ], 1, "Maize is the seed of a grass, so it is a cereal.",
            hint="Which of these is the seed of a grass?",
            feedback=["Cassava is a root.", "", "Yam is a tuber.", "Plantain is a fruit."]),
        PQ("Name the three parts of a cereal grain and state one nutrient found in each.", "Bran: dietary fibre (also B vitamins, iron). Endosperm: starch. Germ: fat and B vitamins (also vitamin E)."),
        PQ("Why is white flour keeping longer than wholemeal flour?", "White flour has had the germ removed. The germ contains fat, which goes rancid, so removing it lets the flour keep longer."),
        PQ("State three ways of storing rice or maize flour safely.", "Keep it in clean, dry, airtight containers; store in a cool, dry, well-ventilated place off the floor; protect from weevils and rats; use older stock first. (Any three.)"),
        PQ("Name two cereals and give a local dish made from each.", "Maize: corn fufu or pap. Rice: boiled rice with stew or jollof rice. (Also wheat: bread; millet: millet couscous or porridge.)"),
        SUM("Cereals are seeds of grasses: maize, rice, wheat, millet, sorghum, oats and barley.",
            "A grain has bran (fibre, B vitamins, minerals), endosperm (starch) and germ (fat, protein, vitamins B and E).",
            "Refined cereals lose the bran and germ; wholegrain keeps them.",
            "Cereals give mainly energy and some protein, short of lysine, which pulses supply.",
            "Store dry, airtight and cool to avoid mould and weevils; starch gelatinises on cooking."),
    ],
))

# ------------------------------------------------------------------ 7. Meat, offal and poultry
LESSONS.append(lesson(
    module=M4,
    topic="Meat, offal and poultry",
    title="Meat, offal and poultry: structure, nutrients, storage and cooking",
    slug="fdn2-meat-offal-poultry",
    minutes=21,
    summary="The structure of meat, why some cuts are tough, what meat, offal and poultry give the body, and how to store, choose and cook them safely.",
    objectives=[
        "Describe the structure of meat: muscle fibres, connective tissue and fat",
        "Explain why some cuts are tender and some tough, and match cooking methods to them",
        "State the nutritive value of meat, offal and poultry",
        "State rules for buying, storing and cooking meat safely",
    ],
    key_concepts=["Muscle fibre", "Connective tissue", "Collagen", "Offal", "Poultry", "High biological value protein", "Cross-contamination"],
    blocks=[
        H("Introduction"),
        T("Beef, goat, pork and chicken are among the most valued foods at festive meals in Cameroon. Chicken with plantain (the dish known as chicken DG), grilled soya, "
          "stewed goat and kanda are only a few examples. Meat is costly, so it pays to know how to choose it, keep it safe and cook it well."),
        D("**Meat** is the flesh of animals such as cattle, goats, sheep and pigs, eaten as food. **Offal** is the edible internal organs and other parts, such as liver, kidney, heart, tripe, tongue. "
          "**Poultry** is domestic birds kept for food, such as chicken, duck and turkey.", title="Definition: meat, offal, poultry"),
        H("Structure of meat"),
        KEY("What meat is made of", "Three tissues decide how tender it is.", cards=[
            ["Muscle fibres", "Long thin cells bundled together. They are mainly **protein** and water. Short fibres are tender; long thick fibres are tough."],
            ["Connective tissue", "White fibres of **collagen** that hold fibres together. Collagen is tough, but slow moist cooking turns it into soft **gelatine**. Another type, elastin, stays tough."],
            ["Fat", "Stored under the skin and between and inside the muscles. It gives flavour and juiciness. Fat running through the muscle is called marbling."],
        ]),
        T("**Tender cuts** come from young animals and from muscles that do little work, such as the back (fillet, loin). They can be grilled, fried or roasted. "
          "**Tough cuts** come from old animals and from muscles that work hard, such as the neck, shin and legs. They have more connective tissue, and need long, slow, moist cooking: stewing, braising or pressure cooking. "
          "A cut can also be tenderised by beating or cutting small, or by marinating in lemon juice or other acid."),
        T("After slaughter, muscles stiffen (rigor mortis) and then soften again when the meat is kept cool for a short time. This **conditioning** makes the meat more tender and flavoursome. Meat sold very fresh and cooked at once can be tough."),
        H("Nutritive value"),
        KEY("What meat gives", "Meat is valued above all for protein and iron.", cards=[
            ["Protein", "About 20% of lean meat. It is of **high biological value**: it supplies all the essential amino acids for growth and repair."],
            ["Iron and zinc", "Meat iron is easily absorbed by the body, which helps to prevent anaemia."],
            ["B vitamins", "Especially B3 and B12 (vitamin B12 is found only in animal foods)."],
            ["Fat", "Gives energy and fat-soluble vitamins, but a lot of animal fat is not healthy."],
            ["Missing", "Meat has no carbohydrate or fibre and no vitamin C, so serve it with vegetables and a staple."],
        ]),
        T("**Offal** is often cheap and rich in nutrients. **Liver** is very rich in iron, vitamin A and B vitamins (including folic acid and B12) and is often recommended for children and pregnant women (but pregnant women should ask a health worker about the amount of liver). "
          "Kidney and heart are rich in protein, iron and B vitamins. Offal spoils faster than meat and must be bought fresh, kept cold and cooked soon. "
          "**Poultry** has high-quality protein and less fat than most meat, especially if the skin is removed. Its flesh is fine-fibred and cooks faster, so it is easy to digest."),
        H("Buying, storing and cooking safely"),
        T("Fresh meat is firm and elastic, with a bright natural colour, and has no bad smell or slimy surface. Fresh chicken has clean, moist skin without bruises. "
          "Buy meat from a clean stall, protected from flies, and use it quickly. Do not eat the meat of animals that died of disease."),
        T("Keep raw meat in a refrigerator at about 0 to 5 degrees Celsius, covered, **below** cooked foods so that its juices cannot drip on them. For longer storage, freeze. "
          "Thaw frozen meat in the refrigerator, never leave it for hours in the sun. Use separate knives and boards for raw meat and cooked or ready-to-eat food; this prevents **cross-contamination**, the spreading of bacteria from one food to another. "
          "Cook poultry and minced meat right through, until the thickest part reaches at least 70 degrees Celsius and no pink remains. Reheat leftovers until very hot, and only once."),
        CODE("""Cut / meat            Cooking method
Fillet, loin, chops   grill, fry, roast
Chicken (young)       roast, grill, fry, stew (chicken DG)
Neck, shin, brisket   stew, braise, pressure cook
Liver, kidney         fry or grill quickly, or stew
Minced meat           fry, stew, grill (cook right through)""", "text", title="Table 1. Matching cut and method"),
        EX("Worked example 1: tough or tender?", intro="Why is shin of beef tough, and how should it be cooked to be tender?", steps=[
            S("The muscle works hard", text="The shin is a leg muscle that works all the time, so it has thick fibres and much connective tissue."),
            S("Collagen needs time", text="Slow moist cooking, such as stewing for two hours or more, changes the collagen into gelatine."),
            S("Choose the method", text="Stew, braise or pressure cook it. Frying or grilling quickly would leave it tough."),
        ]),
        EX("Worked example 2: safe handling", intro="Raw chicken was cut on a board, and then the same board and knife were used to slice tomatoes for a salad. What is the risk and how can it be avoided?", steps=[
            S("The risk", text="Raw chicken may carry bacteria. Used on the salad, they will not be killed because the tomatoes are not cooked. This is cross-contamination."),
            S("Avoid it", text="Use separate boards and knives for raw meat. Or wash and sterilise them in hot soapy water before using them for other foods."),
            S("Other steps", text="Wash hands after touching raw meat, and cook the chicken until no pink remains."),
        ]),
        TIP("Meat, offal and poultry link to Paper 2 questions on food choices, food preparation and food safety. For a 'structure of meat' question, draw or describe muscle fibres, connective tissue and fat. "
            "Linking the cut to the cooking method gains marks.", title="Exam link"),
        MISTAKE("Saying that all meat needs the same cooking time", "Tender cuts cook quickly with dry heat, and tough cuts need long, slow, moist cooking. Match the method to the cut."),
        MISTAKE("Storing raw meat above cooked food", "Raw meat juices may drip on food below. Store raw meat on the lowest shelf, covered."),
        QUIZ("Which tissue in meat changes into gelatine during slow moist cooking?", [
            "Muscle fibre", "Fat", "Collagen in the connective tissue", "Bone",
        ], 2, "Collagen is changed to soft gelatine by long, moist, gentle cooking, so tough cuts become tender.",
            hint="It is the tissue that holds the fibres together.",
            feedback=["Muscle fibres shrink and harden with heat.", "Fat melts, it does not form gelatine.", "", "Bone does not change into gelatine in ordinary cooking time."]),
        QUIZ("Which food is the richest source of vitamin A among these?", [
            "Lean beef", "Liver", "Chicken breast", "Egg white",
        ], 1, "Liver stores vitamin A and iron and is much richer in vitamin A than the other choices.",
            hint="Which one is an organ that stores vitamins?",
            feedback=["Lean beef has little vitamin A.", "", "Chicken breast has little vitamin A.", "Egg white has protein but no vitamin A."]),
        PQ("Name the three tissues found in meat and state the part each plays.", "Muscle fibres: the protein that makes up the lean meat. Connective tissue: holds fibres together, and makes meat tough. Fat: gives flavour and juiciness."),
        PQ("Why must tough cuts of meat be cooked slowly in moist heat?", "They contain much collagen. Slow moist heat changes collagen to gelatine, so the meat becomes tender. Dry fast heat would harden the fibres."),
        PQ("State four rules for storing and handling raw meat safely.", "Keep it cold (refrigerate or freeze); store it covered on the lowest shelf; use separate boards and knives; wash hands after handling; cook right through; do not leave it in warm places. (Any four.)"),
        PQ("State three nutrients that meat gives and one thing that it lacks.", "Protein of high biological value, iron, B vitamins (also zinc). It lacks vitamin C, carbohydrate and fibre."),
        SUM("Meat is made of muscle fibres (protein), connective tissue (collagen) and fat.",
            "Tender cuts are cooked quickly with dry heat; tough cuts need long, slow moist cooking, which turns collagen to gelatine.",
            "Meat and poultry give high biological value protein, iron and B vitamins; liver is also very rich in vitamin A.",
            "Buy fresh, keep cold, store raw meat below cooked food, avoid cross-contamination.",
            "Cook poultry and minced meat right through, to at least 70 degrees Celsius in the thickest part."),
    ],
))

# ------------------------------------------------------------------ 8. Fish
LESSONS.append(lesson(
    module=M4,
    topic="Fish",
    title="Fish: types, nutrients, freshness, storage and cooking",
    slug="fdn2-fish",
    minutes=20,
    summary="Types of fish, why fish cooks quickly and is easy to digest, what fish gives the body, how to recognise fresh fish and how to store and cook it.",
    objectives=[
        "Classify fish into white fish, oily fish and shellfish, with local examples",
        "Explain why fish is more tender and cooks faster than meat",
        "State the nutritive value of fish",
        "List signs of fresh fish and rules for storing and cooking it",
    ],
    key_concepts=["White fish", "Oily fish", "Shellfish", "Fresh fish", "Spoilage", "Omega-3 fatty acids"],
    blocks=[
        H("Introduction"),
        T("Mackerel (called Titus in many markets), catfish, tilapia, bonga, stockfish, dried crayfish and prawns are widely eaten in Cameroon, from the coast to the lakes and rivers. "
          "Fish is a cheap, tasty source of protein. It is also easily spoiled, so freshness and storage matter."),
        D("**Fish** are animals that live in water, with gills and fins, eaten as food. Fish are grouped as **white fish**, **oily fish** and **shellfish**.", title="Definition: fish"),
        H("Types of fish"),
        KEY("Three groups", "The group depends on where the fat is stored.", cards=[
            ["White fish", "Fat stored only in the liver, so the flesh is low in fat. Examples: cod and hake (and stockfish, which is dried cod), tilapia and most freshwater fish such as catfish."],
            ["Oily fish", "Fat spread through the flesh, 10 to 20% or more. Examples: mackerel, herring, sardines, tuna and bonga. Rich in vitamins A and D and omega-3 fatty acids."],
            ["Shellfish", "Have a shell. Crustaceans (prawns, crab, crayfish) and molluscs (oysters, snails). Often sold dried or frozen."],
        ]),
        H("Structure: why fish is tender"),
        T("Fish flesh is made of short muscle fibres arranged in flakes, separated by very thin sheets of connective tissue. "
          "The connective tissue is much weaker than in meat and changes to gelatine at a low temperature. Fish therefore **cooks quickly** (usually 10 to 20 minutes) and is **tender and easy to digest**. "
          "It also breaks up easily, so it needs gentle handling and short cooking."),
        H("Nutritive value"),
        KEY("What fish gives", "Fish is more than protein.", cards=[
            ["Protein", "About 15 to 20% in flesh: high biological value, with all the essential amino acids."],
            ["Fat", "Low in white fish, high in oily fish. Oily fish fat is rich in omega-3 fatty acids, which are good for the heart and brain."],
            ["Vitamins", "Oily fish gives vitamins A and D (white fish keeps them in the liver oil). Also B vitamins."],
            ["Minerals", "Sea fish gives iodine. Small fish with soft bones (sardines, dried small fish) give calcium and phosphorus if the bones are eaten. Fish also gives iron and zinc."],
        ]),
        H("Freshness and storage"),
        T("Fish spoils faster than meat. Enzymes in the fish and bacteria on it quickly break the flesh down, and a strong smell develops. "
          "Signs of **fresh fish**: bright, clear, bulging eyes; bright red or pink gills; shiny, firmly attached scales; firm flesh that springs back when pressed; a fresh, clean smell. "
          "Signs of **stale fish**: sunken, cloudy eyes; grey, slimy gills; dull skin; soft flesh that keeps the mark of a finger; a strong, unpleasant smell."),
        T("Gut and clean fish soon after catching, and keep it cold (on ice or in a refrigerator at about 0 to 4 degrees Celsius). Wrap it so that its smell does not reach other foods. "
          "Use it the same day or freeze it. Fish can also be **preserved** by smoking, drying or salting, which are traditional ways of keeping it where there is no electricity."),
        H("Cooking fish"),
        T("Fish can be steamed, poached, grilled (poisson braise), baked, fried, or stewed in soups and sauces such as fish pepper soup. "
          "Because it is delicate, cook it only until the flesh is opaque and comes away from the bone in flakes. "
          "Overcooking makes it dry and breaks it up. Add lemon juice, herbs and spices to give flavour, and wash hands and boards well after handling raw fish."),
        EX("Worked example 1: is this fish fresh?", intro="At the market, a fish has sunken cloudy eyes, grey slimy gills and soft flesh that stays dented when pressed. Is it fresh? Give reasons.", steps=[
            S("Check the eyes", text="Fresh fish has bright, clear, bulging eyes. These eyes are sunken and cloudy: stale."),
            S("Check the gills", text="Fresh gills are bright red or pink. Grey and slimy gills show spoilage."),
            S("Check the flesh", text="Fresh flesh is firm and springs back. This flesh stays dented, so the fish is old."),
            S("Answer", text="The fish is not fresh and should not be bought."),
        ]),
        EX("Worked example 2: which cooking method?", intro="Suggest a suitable method and a reason for (a) a delicate white fish fillet and (b) a whole mackerel.", steps=[
            S("White fish fillet", text="Poach or steam it gently. White fish is low in fat and delicate; gentle moist heat keeps it moist and unbroken."),
            S("Whole mackerel", text="Grill or bake it. Oily fish has fat in the flesh, which keeps it moist during dry heat and gives rich flavour."),
        ]),
        TIP("Paper 2 may ask about the structure of fish or the signs of freshness, and Paper 1 often tests oily and white fish, or the vitamins in fish. "
            "In your answer, give a local fish as an example.", title="Exam link"),
        MISTAKE("Saying fish is tough like meat", "Fish has very little connective tissue and therefore cooks fast. Long cooking spoils it."),
        MISTAKE("Judging freshness by smell only", "Use all the signs: eyes, gills, flesh and smell. Stale fish may be washed or sprayed to hide the smell."),
        QUIZ("Which group of fish stores fat throughout the flesh?", [
            "White fish", "Oily fish", "Shellfish", "Dried fish only",
        ], 1, "Oily fish such as mackerel and sardines have fat spread through the flesh.",
            hint="Think of mackerel.",
            feedback=["White fish store fat in the liver only.", "", "Shellfish have shells; they are not defined by where fat is stored.", "Drying is a preserving method."]),
        QUIZ("Which is a sign of FRESH fish?", [
            "Sunken eyes", "Grey slimy gills", "Firm flesh that springs back", "Strong smell",
        ], 2, "Fresh flesh is firm and elastic and springs back after being pressed.",
            hint="Think of the texture.",
            feedback=["Sunken eyes mean stale.", "Fresh gills are red or pink.", "", "A strong smell means spoilage."]),
        PQ("Why does fish cook faster than meat?", "Fish has short muscle fibres and very little, weak connective tissue, which softens at a lower temperature. So it cooks in a short time and is tender."),
        PQ("Distinguish between white fish and oily fish, giving a local example of each.", "White fish store fat only in the liver, so the flesh is low in fat (catfish, tilapia, cod). Oily fish have fat through the flesh (mackerel, sardines, bonga)."),
        PQ("State four signs of fresh fish.", "Bright clear bulging eyes; red or pink gills; shiny scales fixed firmly; firm elastic flesh; fresh smell. (Any four.)"),
        PQ("State two nutrients that oily fish supplies that meat supplies in smaller amounts.", "Vitamin D (and vitamin A) and omega-3 fatty acids. (Sea fish also gives iodine.)"),
        SUM("Fish are white fish, oily fish or shellfish.",
            "Fish has short muscle fibres and little connective tissue, so it is tender and cooks quickly.",
            "Fish gives high biological value protein; oily fish also gives vitamins A and D and omega-3 fats; sea fish gives iodine.",
            "Fresh fish has bright clear eyes, red gills, firm flesh and a clean smell.",
            "Keep fish cold, use it quickly, cook it gently, or preserve it by smoking, drying or salting."),
    ],
))

# ------------------------------------------------------------------ 9. Eggs
LESSONS.append(lesson(
    module=M4,
    topic="Eggs",
    title="Eggs: structure, nutrients, freshness and the uses of eggs in cooking",
    slug="fdn2-eggs",
    minutes=22,
    summary="The structure of a hen's egg, its nutritive value, tests for freshness, storage, and the cooking properties of eggs: coagulation, foaming, emulsifying, binding, coating and glazing.",
    objectives=[
        "Name the parts of a hen's egg and state their functions",
        "State the nutritive value of an egg",
        "Describe tests for the freshness of an egg and how to store eggs",
        "Explain the uses of eggs in cooking: coagulation, aeration, emulsification, binding, coating and glazing",
    ],
    key_concepts=["Shell", "Air space", "Albumen", "Yolk", "Chalaza", "Coagulation", "Aeration", "Emulsion", "Lecithin"],
    blocks=[
        H("Introduction"),
        T("Boiled eggs for breakfast, egg sauce with plantain, an omelette, the egg in a cake or in beignet dough: the egg is one of the most useful foods in the kitchen. "
          "It is cheap, nutritious and can do many jobs in cooking. A tray of 30 eggs is easy to buy at a market. This lesson looks at its structure and its uses."),
        H("Structure of a hen's egg"),
        IMG("f5fdn2-egg.svg", alt="Section through an egg showing shell, shell membranes, air space at the blunt end, thin white, thick white, chalaza cords, yolk membrane and yolk",
            caption="Figure 1. The structure of a hen's egg."),
        KEY("The parts of an egg", "Learn the function of each part.", cards=[
            ["Shell", "Hard outer layer of calcium carbonate. It protects the egg but is **porous**: tiny holes let air in and out, and let smells and bacteria in. A thin outer coating (cuticle) helps to block the holes."],
            ["Shell membranes", "Two thin skins just inside the shell, which protect against bacteria."],
            ["Air space", "A pocket of air between the membranes at the blunt end. It grows larger as the egg gets older."],
            ["White (albumen)", "The clear part, about 90% water and the rest protein. It has a thick part and a thinner outer part."],
            ["Chalazae", "Two twisted cords that hold the yolk in the centre."],
            ["Yolk", "The yellow part inside a thin yolk membrane. It contains fat, protein, vitamins A and D, iron and lecithin."],
        ]),
        H("Nutritive value"),
        T("An egg is a very nutritious food. Its protein is of **high biological value**: it contains all the essential amino acids in the best proportions, and it is used as the standard for comparing other proteins. "
          "The **yolk** contains the fat, vitamins A, D, B12 and riboflavin, and iron. The **white** has protein and water, with almost no fat. "
          "An egg has no vitamin C and very little carbohydrate. Eggs are good for growing children, pregnant women and the sick, since they are easy to digest when lightly cooked."),
        H("Freshness and storage"),
        KEY("Testing an egg for freshness", "Three simple tests.", cards=[
            ["Water test", "Put the egg in a bowl of cold water. A fresh egg sinks and lies flat. An older egg tilts or stands on end because its air space is bigger. A stale egg floats."],
            ["Candling", "Hold the egg to a bright light in a dark room. A fresh egg is clear, with a small air space."],
            ["Break-out test", "A fresh egg has a high round yolk and a thick white that stays together. A stale egg has a flat yolk and watery white that spreads out."],
        ]),
        T("Store eggs in a cool place, preferably a refrigerator, with the **pointed end down** (this keeps the yolk centred and the air space at the top). "
          "Keep them away from strong-smelling foods because the shell is porous. Do not wash eggs before storing, because washing removes the protective cuticle. "
          "Always cook eggs thoroughly for babies, the sick and the elderly: raw eggs can carry salmonella bacteria."),
        H("What eggs do in cooking"),
        KEY("Jobs of the egg", "Each job comes from the egg protein.", cards=[
            ["Coagulation (setting)", "Egg protein sets firm on heating: the white begins to set at about 60 degrees Celsius and the yolk a little higher (check your textbook for exact figures). This is why boiled, poached, fried eggs and custards set."],
            ["Aeration (foaming)", "Whisking egg white traps air bubbles and makes a stable foam that expands in the oven. It is used in sponge cakes and meringues. For best foam, use a clean bowl with no grease or yolk."],
            ["Emulsifying", "Egg yolk contains lecithin, which holds oil and water together as an emulsion. It makes mayonnaise and keeps cake mixtures from curdling."],
            ["Binding and thickening", "Egg holds ingredients together, as in fish cakes and burgers, and thickens custard and sauces."],
            ["Coating", "Beaten egg and breadcrumbs make a crisp coat on foods to be fried."],
            ["Glazing", "Brushing beaten egg on pastry or bread gives a shiny golden crust."],
            ["Enriching and colouring", "Egg adds nutrients and a yellow colour to dough, cakes and sauces."],
        ]),
        T("When an egg is boiled too long, a grey-green ring forms around the yolk. The egg becomes hard and rubbery. A usual teaching guide: about 3 to 4 minutes for a soft-boiled egg and about 10 minutes for a hard-boiled egg, then cool in cold water."),
        EX("Worked example 1: is the egg fresh?", intro="A student places three eggs in cold water. Egg A sinks and lies flat. Egg B sinks but stands on its end. Egg C floats. Comment on each.", steps=[
            S("Egg A", text="It lies flat on the bottom, so the air space is small: fresh."),
            S("Egg B", text="It stands on its end, so the air space has grown: it is older and should be used soon and cooked thoroughly."),
            S("Egg C", text="It floats because the air space is large: stale. Do not use it."),
        ]),
        EX("Worked example 2: the cost of an egg", intro="A tray of 30 eggs costs FCFA 2 400 (an invented price for practice). What is the cost of one egg, and of the 3 eggs in a cake?", steps=[
            S("Cost of one egg", math=r"2400 \div 30 = 80 \text{ FCFA}"),
            S("Cost of three eggs", math=r"3 \times 80 = 240 \text{ FCFA}"),
            S("Answer", text="One egg costs FCFA 80 and three cost FCFA 240."),
        ], check=r"30 \times 80 = 2400"),
        TIP("Eggs appear often in Paper 2 and Paper 3 (cakes, custards, omelettes) as well as in Paper 1. Learn the structure drawing, the freshness tests and the uses of egg, and give a food example for each use "
            "(for example, 'aeration: whisked whites in a meringue').", title="Exam link"),
        MISTAKE("Saying that a fresh egg floats", "A fresh egg sinks and lies flat. Old eggs float because the air space becomes larger as water evaporates through the shell and air enters."),
        MISTAKE("Listing coagulation and aeration as the same thing", "Coagulation is setting by heat; aeration is trapping air by whisking. They are separate uses of egg."),
        QUIZ("Which part of the egg contains the lecithin that makes an emulsion?", [
            "The shell", "The white", "The yolk", "The air space",
        ], 2, "Lecithin is in the egg yolk and holds oil and water together.",
            hint="It is the yellow part.",
            feedback=["The shell is calcium carbonate.", "The white is mostly water and protein.", "", "The air space is just air."]),
        QUIZ("In a bowl of water, an egg floats. This shows that the egg is", [
            "very fresh", "stale", "hard-boiled", "double yolked",
        ], 1, "A large air space makes it float: the egg is stale.",
            hint="The air space grows with age.",
            feedback=["A very fresh egg sinks.", "", "The test is for raw eggs, and boiling is a separate matter.", "A double yolk does not make an egg float."]),
        PQ("Name four parts of an egg and state one function of each.", "Shell: protection. Membranes: stop bacteria. Air space: supplies air to a chick. Yolk: food store, with fat and vitamins. White: protein and water. Chalaza: holds the yolk in place. (Any four.)"),
        PQ("Describe a test for the freshness of an egg.", "Place the egg in cold water. A fresh egg sinks and lies flat; an older egg tilts or stands up; a stale egg floats."),
        PQ("State three uses of eggs in cooking, with an example of each.", "Binding: fish cakes. Aeration (foam): meringues or sponge cakes. Coating: egg and breadcrumbs on fried fish. Glazing: brushing pastry. Emulsifying: mayonnaise. Thickening: custard. (Any three.)"),
        PQ("Why should eggs be stored away from strongly smelling foods?", "The shell is porous, so smells pass in through it and spoil the egg flavour."),
        SUM("An egg has a porous shell, two membranes, an air space, a white (albumen), chalazae and a yolk.",
            "Egg protein is of high biological value; the yolk supplies fat, vitamins A and D, and iron.",
            "A fresh egg sinks and lies flat in water; a stale egg floats.",
            "Store eggs cool, pointed end down, away from strong smells; cook thoroughly.",
            "Uses: setting, foaming, emulsifying, binding, thickening, coating, glazing and enriching."),
    ],
))

# ------------------------------------------------------------------ 10. Milk and cheese
LESSONS.append(lesson(
    module=M4,
    topic="Milk and cheese",
    title="Milk and cheese: composition, kinds, safety and cooking",
    slug="fdn2-milk-and-cheese",
    minutes=21,
    summary="What milk contains, the kinds of milk and milk products, how milk is made safe, how it behaves in cooking, and how cheese is made and used.",
    objectives=[
        "State the composition and nutritive value of milk",
        "Name the kinds of milk and milk products",
        "Explain pasteurisation and why fresh milk should be boiled or pasteurised",
        "Describe how milk behaves in cooking and how cheese is made, stored and used",
    ],
    key_concepts=["Casein", "Lactose", "Pasteurisation", "UHT", "Evaporated milk", "Curds and whey", "Rennet", "Scorching"],
    blocks=[
        H("Introduction"),
        T("Fresh milk from the herds of the Adamawa and North West highlands, powdered milk in tins and sachets, yoghurt, and cheese: dairy foods are used in tea, pap, sauces and desserts. "
          "Milk is called a **complete food for the young**, since a baby mammal can grow on it alone. For older children and adults it is a very useful part of the diet."),
        D("**Milk** is the white liquid made by female mammals to feed their young. In cooking, milk usually means cow's milk, but goat's and sheep's milk are also used.", title="Definition: milk"),
        H("Composition and nutritive value"),
        CODE("""Approximate composition of whole cow's milk (teaching figures)
Water          about 87 %
Carbohydrate   about 4.7 %  (lactose, the milk sugar)
Fat            about 3.5-4 %
Protein        about 3.4 %  (mainly casein)
Minerals       about 0.7 %  (calcium, phosphorus)
Vitamins       A, D (some), B2 (riboflavin)""", "text", title="Table 1. Whole milk"),
        T("Milk protein is of **high biological value**. Milk is the best everyday source of **calcium**, needed for bones and teeth, and it supplies riboflavin and some vitamin A. "
          "It is **low in iron** and has no vitamin C, which is why babies fed only milk for a long time can become anaemic. Skimmed milk has the fat (and fat-soluble vitamins) removed."),
        H("Kinds of milk and milk products"),
        KEY("Milk on the market", "Know how each is made.", cards=[
            ["Pasteurised milk", "Heated to about 72 degrees Celsius for 15 seconds (or about 63 degrees for 30 minutes) and cooled quickly. It kills disease bacteria but keeps most of the flavour. It must be kept cold and used in a few days."],
            ["UHT (long-life) milk", "Heated to a much higher temperature, about 135 degrees Celsius, for a very short time, and packed in sterile cartons. It keeps for months unopened without refrigeration."],
            ["Evaporated milk", "Whole milk with about half of the water removed, in a tin. It is sterilised in the tin."],
            ["Condensed milk", "Evaporated milk with much sugar added. Very sweet; not for babies."],
            ["Dried (powdered) milk", "Water removed completely. It keeps well when dry and airtight, and is mixed with clean water."],
            ["Yoghurt, cream, butter, cheese", "Made from milk. Yoghurt is milk fermented by harmless bacteria. Butter is churned from cream."],
        ]),
        T("**Fresh milk from local herds must be boiled or pasteurised** before it is drunk. Raw milk can carry bacteria that cause diseases such as brucellosis and tuberculosis. "
          "Keep fresh milk covered and cold and use it the same day: it sours quickly in warm weather."),
        H("Milk in cooking"),
        KEY("How milk behaves when heated", "Three common problems.", cards=[
            ["Skin", "On heating, protein and fat form a skin on top. Stir, or cover, to avoid it."],
            ["Scorching", "The milk sugar and protein stick and burn at the bottom of the pan. Use a heavy pan, a low heat and stirring, or heat in a pan over hot water."],
            ["Curdling", "Acid (lemon, tomatoes), salt or too much heat make casein clot into lumps. Add the acid slowly and keep the heat gentle."],
        ]),
        H("Cheese"),
        T("Cheese is made by **curdling milk** with **rennet** (an enzyme) or acid, so that the casein sets into solid **curds**. The liquid left is the **whey**. "
          "The curds are drained, salted, pressed and, for hard cheese, ripened for months. Cheese is a concentrated food: it contains the protein, fat and most of the calcium of the milk, in a small bulk. "
          "It is also high in salt and fat, so it should be eaten in moderation. It has no vitamin C or fibre."),
        T("Types: **hard** (such as cheddar), **soft** (such as cream and cottage cheese), and **processed**. Cheese keeps best covered in a cool place or a refrigerator. "
          "Use it in sauces, on toast, in sandwiches, with pasta, and in baking. Cook it gently, since high heat makes it tough and stringy."),
        EX("Worked example 1: calcium from milk", intro="A glass of milk (250 ml) holds about 120 mg of calcium per 100 ml (a teaching figure). How much calcium is in a glass?", steps=[
            S("Number of 100 ml portions", math=r"250 \div 100 = 2.5"),
            S("Multiply", math=r"2.5 \times 120 = 300 \text{ mg}"),
            S("Answer", text="A glass of milk gives about 300 mg of calcium."),
        ], check=r"120 \times 2.5 = 300"),
        EX("Worked example 2: why did the sauce curdle?", intro="A cook adds lemon juice to hot milk in a sauce, and the milk forms lumps. Explain, and say how to avoid it.", steps=[
            S("Cause", text="Acid makes the casein protein clot into curds, especially when the milk is hot."),
            S("Avoid it", text="Cool the milk, add the acid slowly and stir, or thicken the milk with flour first (as in a white sauce), which helps keep it smooth."),
        ]),
        TIP("Milk and cheese questions in the examination usually ask for composition, uses, and how to care for milk. Mention both calcium and protein, give an example of a milk product, and state the need to boil raw milk.", title="Exam link"),
        MISTAKE("Saying that milk is rich in iron", "Milk is a good source of calcium and protein but is a poor source of iron and has no vitamin C."),
        MISTAKE("Boiling milk fast on high heat", "It boils over and scorches. Heat slowly and stir."),
        QUIZ("What is the main mineral in milk?", [
            "Iron", "Calcium", "Iodine", "Sodium chloride"
        ], 1, "Milk is rich in calcium, needed for bones and teeth.",
            hint="Think of bones and teeth.",
            feedback=["Milk is a poor source of iron.", "", "Milk is not an important source of iodine.", "Salt is not the main mineral in milk."]),
        QUIZ("In cheese making, the solid part that forms when milk is curdled is called", [
            "whey", "curds", "cream", "lactose",
        ], 1, "Curds are the solid casein and fat; the liquid left is whey.",
            hint="The liquid is whey.",
            feedback=["Whey is the liquid left after curds form.", "", "Cream is the fat that rises to the top of milk.", "Lactose is the milk sugar."]),
        PQ("State four nutrients found in milk.", "Protein (casein), fat, lactose (carbohydrate), calcium and phosphorus, vitamins A and B2 (riboflavin). (Any four.)"),
        PQ("Why should fresh milk from a farm be boiled or pasteurised before drinking?", "Raw milk may contain harmful bacteria, such as those causing brucellosis or tuberculosis. Heating kills them."),
        PQ("Give two differences between evaporated milk and UHT milk.", "Evaporated milk has about half its water removed and is sold in tins; UHT milk has all of its water and is heat-treated at a very high temperature and packed in sterile cartons."),
        PQ("Explain how cheese is made.", "Milk is warmed and curdled with rennet or acid. The curds are separated from the whey, drained, salted and pressed, and left to ripen for hard cheeses."),
        SUM("Milk contains water, lactose, fat, protein (casein), calcium, phosphorus and some vitamins; it is low in iron and has no vitamin C.",
            "Kinds: fresh, pasteurised, UHT, evaporated, condensed, dried milk, with yoghurt, cream, butter and cheese.",
            "Boil or pasteurise raw milk; store it covered and cold.",
            "When heated, milk forms a skin, scorches, or curdles with acid or high heat.",
            "Cheese is curds from milk set with rennet or acid; it is rich in protein, fat and calcium, and also in salt."),
    ],
))

# ------------------------------------------------------------------ 11. Pulses and nuts
LESSONS.append(lesson(
    module=M4,
    topic="Pulses and nuts",
    title="Pulses and nuts: structure, nutritive value, preparation and uses",
    slug="fdn2-pulses-and-nuts",
    minutes=20,
    summary="What pulses and nuts are, their nutritive value, why pulses are soaked and well cooked, how to store them, and how they are used in Cameroonian cooking.",
    objectives=[
        "Define pulses and nuts and give local examples",
        "State the nutritive value of pulses and of nuts",
        "Explain why pulses are soaked and thoroughly cooked",
        "State how pulses and nuts are stored and used",
    ],
    key_concepts=["Pulses", "Legume", "Nuts and oil seeds", "Protein", "Soaking", "Rancidity", "Complementary protein"],
    blocks=[
        H("Introduction"),
        T("Koki, bean porridge, akara or bean fritters, groundnut soup, njansang sauce, pistache (egusi) soup: dishes from the bean and nut families are everywhere in Cameroon. "
          "They are filling, cheaper than meat, and rich in protein. For many families, they are the main protein food."),
        D("**Pulses** are the dry seeds of plants of the legume family that grow in pods. Examples: beans (cowpeas or black-eyed beans, red kidney beans), peas, lentils, soya beans and Bambara groundnuts.", title="Definition: pulses"),
        D("**Nuts and oil seeds** are seeds or fruits with a hard shell or skin and a kernel rich in fat. Examples: groundnuts (which are botanically legumes), cashew nuts, coconut, palm kernels, and oil seeds such as njansang and egusi melon seeds.", title="Definition: nuts and oil seeds"),
        H("Nutritive value of pulses"),
        KEY("What pulses give", "Pulses are cheap plant proteins.", cards=[
            ["Protein", "About 20 to 25% in dry beans, and still more in soya beans (about 35 to 40%). It is of lower biological value than meat, because it lacks some amino acids, but a mixture with a cereal fills the gap."],
            ["Carbohydrate", "Mostly starch, so pulses give energy."],
            ["Vitamins and minerals", "B vitamins, iron, calcium and zinc in useful amounts. Dry pulses have no vitamin C (germinated seeds do)."],
            ["Fibre", "A very good source of dietary fibre (NSP), which helps digestion."],
            ["Fat", "Very little, except in soya beans and groundnuts."],
        ]),
        H("Preparing pulses"),
        T("Dry pulses are hard. Before cooking, **sort and wash** them to remove stones and bad seeds, and **soak** them in water for several hours or overnight. "
          "Soaking allows the seed to take up water, which reduces the cooking time and fuel. Cook in fresh water until quite soft. "
          "Raw or undercooked beans (particularly red kidney beans) contain substances that upset the stomach and can make people ill, so they must be boiled hard for at least ten minutes and then cooked thoroughly until soft. Do not add bicarbonate of soda, which spoils the B vitamins. "
          "A pressure cooker saves a lot of fuel. Add salt late if the beans are slow to soften."),
        H("Nutritive value of nuts"),
        T("Nuts and oil seeds are rich in **fat** (groundnuts have around half of their weight as fat), and therefore give much energy. They contain protein (about 25% in groundnuts), vitamin E, B vitamins, iron and fibre. "
          "Their protein is of lower biological value, so they are best eaten with other foods. They contain no vitamin C. "
          "Because they are rich in fat, they **go rancid** if kept too long or in warm damp places. Nuts and groundnuts stored damp can grow moulds that produce harmful toxins (aflatoxins). "
          "Some people are **allergic** to nuts, and the reaction can be serious, so care is needed in preparing food for others."),
        H("Storage and uses"),
        T("Store dry pulses and nuts in clean, **airtight, dry containers** in a cool place away from damp, insects and rats. Dry them well in the sun before storing. Discard any that are mouldy or have holes made by weevils. "
          "Shelled groundnuts and ground nut paste keep best in a cool place or refrigerator."),
        CODE("""Food                 Use
Beans                koki, bean porridge, akara (bean fritters), stews, boiled beans with plantain
Soya                 soya milk, soya flour for pap and bread
Bambara groundnut    boiled, or ground into flour
Groundnut            soups and sauces, paste, roasted snack, oil
Egusi (pistache)     thick soups with leaves or fish
Njansang             ground for sauces
Coconut              rice, sweets, milk and oil
Cashew               snack and in sweet dishes""", "text", title="Table 1. Pulses and nuts in cooking"),
        EX("Worked example 1: improving a family meal", intro="A family eats only cassava fufu with leaf soup. Suggest how adding beans or groundnuts improves the meal.", steps=[
            S("The problem", text="Cassava is mostly starch and has little protein, so the meal is low in protein."),
            S("Add a pulse or nut", text="Beans or groundnut paste in the soup supply protein, iron, B vitamins and fibre."),
            S("Result", text="The meal now gives energy, body-building protein and more protective nutrients, and costs less than meat or fish."),
        ]),
        EX("Worked example 2: protein in a serving", intro="A cooked serving uses 150 g of dry beans, which have about 22 g of protein in each 100 g (a teaching figure). How much protein does the serving give?", steps=[
            S("Number of 100 g portions", math=r"150 \div 100 = 1.5"),
            S("Multiply", math=r"1.5 \times 22 = 33 \text{ g}"),
            S("Answer", text="The beans supply about 33 g of protein (before any losses in cooking water)."),
        ], check=r"22 \times 1.5 = 33"),
        TIP("Pulses and nuts often appear as 'name two foods rich in protein other than meat', or as 'why soak dried beans'. Give a local example, and say that pulses should be eaten with cereals to give complementary proteins.", title="Exam link"),
        MISTAKE("Saying that groundnuts are low in fat", "Groundnuts and other nuts are rich in fat. Pulses such as beans are low in fat (soya is an exception)."),
        MISTAKE("Eating undercooked beans", "Undercooked beans can cause illness and are difficult to digest. Soak, boil hard, and cook until soft."),
        QUIZ("Why are dry beans soaked before cooking?", [
            "To make them rich in vitamin C", "To soften them so that they cook in less time and fuel", "To remove all the protein", "To make them go rancid",
        ], 1, "Soaking lets the seeds take up water, so they soften and cook faster, saving fuel.",
            hint="Think of the cooking time of hard dry beans.",
            feedback=["Soaking does not add vitamin C.", "", "Soaking does not remove all the protein.", "Rancidity is spoilage of fat and is not the purpose."]),
        QUIZ("Which of these is a nut (oil seed) rich in fat?", [
            "Red kidney beans", "Lentils", "Groundnuts", "Cassava",
        ], 2, "Groundnuts have a large share of their weight as fat.",
            hint="One of these is used to make cooking oil.",
            feedback=["Kidney beans are low-fat pulses.", "Lentils are low-fat pulses.", "", "Cassava is a root and is mostly starch."]),
        PQ("Define pulses and give three examples.", "Pulses are the dry seeds of legumes, growing in pods. Examples: cowpeas (black-eyed beans), red kidney beans, soya beans, lentils, peas, Bambara groundnuts."),
        PQ("State four nutrients found in pulses.", "Protein, carbohydrate (starch), B vitamins, iron, calcium, fibre. (Any four.)"),
        PQ("Why does a meal of maize and beans give better protein than maize alone?", "Maize is short of lysine and beans supply it, while beans are short of methionine, which maize provides. Together they supply a better range of amino acids."),
        PQ("State three rules for storing groundnuts.", "Dry them well; keep them in airtight containers in a cool, dry place; protect from insects and rats; throw away mouldy nuts. (Any three.)"),
        SUM("Pulses are dry legume seeds (beans, peas, lentils, soya); nuts and oil seeds include groundnuts, njansang, egusi, coconut and cashew.",
            "Pulses give protein, starch, B vitamins, iron and fibre; nuts give fat, protein and vitamin E.",
            "Soak pulses, boil them hard at first and cook them until soft; avoid bicarbonate of soda.",
            "Eat pulses with cereals so that the proteins complement each other.",
            "Store dry and airtight; fatty nuts go rancid, and damp nuts grow moulds."),
    ],
))

# ------------------------------------------------------------------ 12. Fruits, vegetables, herbs and spices
LESSONS.append(lesson(
    module=M4,
    topic="Fruits, vegetables, herbs and spices",
    title="Fruits, vegetables, herbs and spices: groups, nutrients, storage and uses",
    slug="fdn2-fruits-vegetables-herbs-spices",
    minutes=21,
    summary="The groups of vegetables and fruits, their nutritive value, how to choose, store and prepare them, and the difference between herbs and spices and how they flavour food.",
    objectives=[
        "Classify vegetables into groups with local examples",
        "State the nutritive value of fruits and vegetables",
        "Describe how fruits and vegetables are chosen, stored and prepared",
        "Distinguish between herbs and spices and state their uses",
    ],
    key_concepts=["Leafy vegetables", "Root vegetables", "Carotene", "Vitamin C", "Dietary fibre", "Herbs", "Spices"],
    blocks=[
        H("Introduction"),
        T("A Cameroonian market is full of green leaves, tomatoes, peppers, okra, carrots, oranges, mangoes, pineapples and bananas. "
          "Fruits and vegetables add colour, flavour and **protective nutrients** to every meal. Herbs and spices make a plain dish taste special. "
          "This lesson covers all four groups."),
        H("Groups of vegetables"),
        KEY("Six groups", "Classify by the part of the plant that is eaten.", cards=[
            ["Leaves", "Cabbage, lettuce, spinach, ndole (bitterleaf), huckleberry leaves (njama njama), pumpkin leaves, cassava leaves."],
            ["Roots and tubers", "Carrot, beetroot, onion bulb, yam, cocoyam, sweet potato, Irish potato."],
            ["Stems", "Celery, asparagus."],
            ["Flowers", "Cauliflower, broccoli."],
            ["Seeds and pods", "Green peas, green beans, sweetcorn."],
            ["Fruit vegetables", "Tomato, okra, garden egg, pepper, cucumber, pumpkin."],
        ]),
        T("**Fruits** are the sweet, fleshy parts of plants that carry seeds. They include **citrus fruits** (orange, lemon, grapefruit, tangerine), **tropical fruits** (mango, pawpaw, pineapple, banana, avocado, guava) and berries. Some foods, such as tomatoes, are botanically fruits but are eaten as vegetables."),
        H("Nutritive value"),
        KEY("What fruits and vegetables give", "Rich in protective nutrients, low in energy.", cards=[
            ["Vitamin C", "Citrus fruits, guava, pawpaw, pineapple, tomatoes, green peppers, fresh leaves. It prevents scurvy and helps wounds to heal."],
            ["Carotene (made into vitamin A)", "Dark green leaves, carrots, mangoes, pawpaw, orange sweet potato."],
            ["Minerals", "Iron and calcium in dark green leaves; potassium in bananas. Iron from plants is less well absorbed than iron from meat."],
            ["Dietary fibre (NSP)", "Cellulose, in skins, leaves and stems, helps to prevent constipation."],
            ["Water", "High: 80 to 95%. They are low in energy, so they help weight control."],
            ["Missing or low", "Little protein and fat (avocado and some seeds are exceptions). Ripe fruit and some vegetables have sugar."],
        ]),
        H("Choosing, storing and preparing"),
        T("Choose produce that is fresh, firm and brightly coloured, with no bruises, mould or wilting. Fresh leaves should be crisp. Use produce **in season** because it is cheaper and tastier. "
          "Store leafy vegetables in a cool, airy place or a refrigerator, and use them soon. Roots and tubers keep in a cool, dark, dry, airy place. Store ripe fruit cool, and keep unripe fruit at room temperature until it ripens. "
          "Do not store damaged items with sound ones, because rot spreads."),
        T("To keep nutrients: wash vegetables before cutting; do not soak them; cut with a sharp knife into large pieces; peel thinly; cook for a short time in a little water or steam; serve at once. Eat fruit raw when possible, since cooking destroys vitamin C. "
          "Cooking softens cellulose, makes starch digestible, and changes colour: green leaves keep their colour best when cooked quickly in a little water without a lid for a moment, but bicarbonate of soda to keep them green destroys vitamin C and thiamin, so do not use it."),
        H("Herbs and spices"),
        D("**Herbs** are the fresh or dried **leaves** of plants used in small amounts to flavour food. Examples: thyme, parsley, basil, mint, bay leaf, celery leaf and the aromatic leaves widely used in Cameroon, such as scent leaf.", title="Definition: herbs"),
        D("**Spices** are the **seeds, bark, roots, buds or fruits** of plants, usually dried, used to flavour food. Examples: black pepper, chilli, ginger, garlic, cloves, nutmeg, cinnamon, pebe (calabash nutmeg) and country onion (olom).", title="Definition: spices"),
        T("Herbs and spices add **flavour, aroma and colour**. They make plain food more appetising, which starts the flow of digestive juices, and reduce the need for salt. Some also help preserve food. "
          "They are used in small amounts and add almost no nutrients. Add delicate fresh herbs near the end of cooking so that their flavour is not lost. Whole spices and dried herbs can go in early. Store dried herbs and spices in airtight containers away from heat and light."),
        EX("Worked example 1: choosing sources of vitamin C", intro="A child needs vitamin C each day. Suggest three local foods and say how to serve them to keep the vitamin.", steps=[
            S("Choose foods", text="Oranges, guava, pawpaw, tomatoes or fresh green pepper are good local sources."),
            S("Serve raw", text="Fruit is best eaten fresh. Tomatoes and green pepper can be added to a sauce at the end of cooking."),
            S("Prepare quickly", text="Cut just before eating, and avoid keeping them cut or cooking them for a long time, because vitamin C is lost to air, water and heat."),
        ]),
        EX("Worked example 2: classify the vegetables", intro="Classify these vegetables into groups: ndole, carrot, cauliflower, okra, green peas.", steps=[
            S("Ndole", text="Leaf vegetable."),
            S("Carrot", text="Root vegetable."),
            S("Cauliflower", text="Flower vegetable."),
            S("Okra", text="Fruit vegetable (botanically a fruit)."),
            S("Green peas", text="Seed or pod vegetable."),
        ]),
        TIP("The topic is tested in Paper 1 (vitamins in fruit and vegetables, groups, storage) and in Paper 2, where the question on food choices and preparation was best answered in 2023. "
            "Name the vitamin or mineral with its food source, for example 'carotene in carrots and mangoes'.", title="Exam link"),
        MISTAKE("Saying that herbs and spices are the same thing", "Herbs are leaves; spices are seeds, bark, roots, buds or fruit. Give the part of the plant to show you know the difference."),
        MISTAKE("Calling fruits and vegetables a good source of protein", "Most fruits and vegetables supply vitamins, minerals and fibre but very little protein or fat."),
        QUIZ("Which is a SPICE and not a herb?", [
            "Thyme", "Parsley", "Cloves", "Mint",
        ], 2, "Cloves are the dried flower buds of a tree, and so they are spices. Thyme, parsley and mint are leaves, so they are herbs.",
            hint="Which one is not a leaf?",
            feedback=["Thyme is a leaf, a herb.", "Parsley is a leaf, a herb.", "", "Mint is a leaf, a herb."]),
        QUIZ("Which nutrient is found in large amounts in oranges and guavas?", [
            "Vitamin C", "Vitamin D", "Protein", "Starch",
        ], 0, "Citrus fruits and guavas are rich in vitamin C.",
            hint="It prevents scurvy.",
            feedback=["", "Vitamin D is found in oily fish and egg yolk.", "Fruits have little protein.", "Fresh fruit contains little starch."]),
        PQ("Classify vegetables into four groups and give a local example of each.", "Leaves: ndole or spinach. Roots: carrot. Flowers: cauliflower. Fruits: tomato or okra. (Also seeds: peas; stems: celery.)"),
        PQ("State four nutrients supplied by fruits and vegetables and one food source of each.", "Vitamin C: orange. Carotene: carrot or mango. Iron: dark green leaves. Fibre: cabbage or skins of fruit. Water: cucumber. (Any four.)"),
        PQ("Give four ways to keep vitamins when preparing vegetables.", "Wash before cutting; do not soak; cut into large pieces; use little water; cook for a short time; use a lid; serve quickly; use the cooking water. (Any four.)"),
        PQ("Distinguish between herbs and spices, with two examples of each.", "Herbs are leaves, used fresh or dried: thyme, parsley, basil, mint. Spices are seeds, bark, roots, buds or fruit: pepper, ginger, cloves, nutmeg, cinnamon. (Two of each.)"),
        SUM("Vegetables are grouped as leaves, roots and tubers, stems, flowers, seeds and pods, and fruit vegetables.",
            "Fruits and vegetables give vitamin C, carotene, minerals, fibre and water, but little protein or fat.",
            "Choose fresh, firm, undamaged produce; store it in a cool, airy place; prepare it quickly and cook it briefly.",
            "Herbs are leaves; spices are seeds, bark, roots, buds or fruit.",
            "Herbs and spices give flavour, aroma and colour, in small amounts."),
    ],
))

# ------------------------------------------------------------------ 13. Raising agents and flour mixtures
LESSONS.append(lesson(
    module=M4,
    topic="Raising agents and flour mixtures",
    title="Raising agents and flour mixtures: cakes, pastry, batters and bread",
    slug="fdn2-raising-agents-and-flour-mixtures",
    minutes=25,
    summary="How air, steam, baking powder, bicarbonate of soda and yeast raise flour mixtures, and the main methods for scones, cakes, pastry, batters and bread, with teaching recipes and scaling.",
    objectives=[
        "Name the raising agents and explain how each makes a mixture rise",
        "Describe the rubbing-in, creaming and whisking methods and the flour mixtures made by each",
        "Describe how batters, shortcrust pastry and bread are made",
        "Scale a teaching recipe up or down correctly",
    ],
    key_concepts=["Raising agent", "Gluten", "Baking powder", "Bicarbonate of soda", "Yeast", "Fermentation", "Proving", "Rubbing-in", "Creaming", "Whisking"],
    blocks=[
        H("Introduction"),
        T("Bread, buns, cakes, puff-puff, beignets and scones all begin with flour, yet one is light and airy and another is flat and heavy. "
          "The difference is the **raising agent**. Making flour mixtures well is one of the main skills tested in the practical paper (Paper 3), so this lesson links the science to the method."),
        D("A **raising agent** is a substance or process that makes a flour mixture lighter, more open in texture and larger in volume, by putting gas (air, steam or carbon dioxide) into it. "
          "The heat of the oven then sets the mixture around the gas bubbles.", title="Definition: raising agent"),
        H("The raising agents"),
        KEY("Five ways to raise a mixture", "Gas is the key.", cards=[
            ["Air", "Trapped by sieving flour, rubbing fat into flour, creaming fat and sugar, whisking eggs, folding, and rolling and folding pastry. In the heat, the trapped air expands."],
            ["Steam", "Water in the mixture turns into steam in a hot oven and pushes the mixture up. It works in Yorkshire pudding, batters, choux pastry and puff pastry."],
            ["Baking powder", "A dry mixture of **bicarbonate of soda**, an acid (such as cream of tartar) and a little starch as a filler. When it gets wet and warm, the bicarbonate and acid react to release **carbon dioxide** gas."],
            ["Bicarbonate of soda alone", "Needs an acid in the mixture (sour milk, lemon juice, vinegar, honey) to react. Heat alone also releases some gas. Too much leaves a soapy taste and a yellow colour."],
            ["Yeast", "A living, single-celled fungus. It feeds on sugar in the dough and, by **fermentation**, releases carbon dioxide and a little alcohol. It needs sugar, moisture and warmth."],
        ]),
        T("Yeast works best in gentle warmth (about body temperature). It works slowly when cold and is **killed above about 55 to 60 degrees Celsius**, so water that is too hot ruins the dough. Too much salt also slows yeast. "
          "Yeast gives bread its flavour, and its dough must be left to rise, which is called **proving**."),
        H("Gluten and types of flour"),
        T("**Plain flour** has no raising agent. **Self-raising flour** has baking powder already mixed in. **Strong flour** (bread flour) is made from hard wheat with a lot of protein. "
          "When wheat flour is mixed with water and worked, its proteins form **gluten**, an elastic network that stretches and holds the gas. Kneading builds gluten, which is needed for bread. "
          "For cakes and pastry, handle gently so that gluten does not make them tough."),
        H("Methods of making flour mixtures"),
        CODE("""Method        How it is done                                   Examples
Rubbing-in    Rub fat into flour with fingertips until like     scones, rock cakes,
              breadcrumbs, then add liquid                      shortcrust pastry
Creaming      Beat fat and sugar until pale and fluffy, add     Victoria sandwich,
              egg gradually, fold in flour                      queen cakes
Whisking      Whisk eggs and sugar until thick and pale,        sponge, Swiss roll
              fold in flour gently (little or no fat)
Batter        Beat flour with liquid and egg to a pouring        pancakes, Yorkshire pudding,
              or dropping mixture                               coating batter, fritters
Dough         Mix to a firm dough, knead, and (for bread)       bread, buns, doughnuts
              prove with yeast""", "text", title="Table 1. Main methods"),
        KEY("Rules for success", "Common to most mixtures.", cards=[
            ["Before mixing", "Pre-heat the oven, prepare the tins, weigh the ingredients exactly and sieve the flour."],
            ["Fat for rubbing in", "Keep the fat and your hands cool; use fat at about half the weight of flour or less."],
            ["Creaming", "Use soft fat. Add the egg slowly. If the mixture curdles, add a spoonful of flour."],
            ["Folding", "Use a metal spoon and cut through the mixture gently to keep the air in."],
            ["Baking", "Do not open the oven door early, or the cake may sink. A cake is done when it springs back and a skewer comes out clean."],
        ]),
        H("Teaching recipes and scaling"),
        T("The amounts below are **teaching recipes**. Adjust them to your teacher's recipe, since recipes differ. The point is to learn the method, and the idea that all amounts must be changed by the same factor when you scale a recipe."),
        CODE("""Teaching recipe: scones (rubbing-in), makes 8
Self-raising flour    200 g
Margarine              50 g
Sugar                  25 g
Milk                  about 100 ml
Oven: about 200 C (hot), 10-15 minutes

Teaching recipe: shortcrust pastry
Plain flour           200 g
Fat                   100 g   (half the weight of the flour)
Cold water            about 3-4 tablespoons
Pinch of salt

Teaching recipe: Victoria sandwich (creaming)
Weigh the eggs; use the SAME weight of margarine, sugar
and self-raising flour. Oven: about 180 C.""", "text", title="Table 2. Teaching recipes (adjust to your teacher's)"),
        EX("Worked example 1: scaling a recipe", intro="Scale the scone recipe from 8 scones to 12 scones.", steps=[
            S("Find the scaling factor", math=r"\frac{12}{8} = 1.5"),
            S("Multiply each ingredient by 1.5", math=r"200 \times 1.5 = 300 \text{ g flour}"),
            S("Margarine", math=r"50 \times 1.5 = 75 \text{ g}"),
            S("Sugar and milk", math=r"25 \times 1.5 = 37.5 \text{ g sugar}, \quad 100 \times 1.5 = 150 \text{ ml milk}"),
        ], check=r"300 : 75 : 37.5 : 150 = 200 : 50 : 25 : 100"),
        EX("Worked example 2: equal-weight cake", intro="Four eggs weigh 240 g altogether. How much margarine, sugar and self-raising flour does the cake need by the creaming method (equal weights)?", steps=[
            S("Use the egg weight", text="Equal-weight cakes use the same weight of fat, sugar and flour as the eggs."),
            S("Each ingredient", math=r"240 \text{ g margarine}, \; 240 \text{ g sugar}, \; 240 \text{ g flour}"),
            S("Total weight of mixture", math=r"240 \times 4 = 960 \text{ g}"),
        ], check=r"240 + 240 + 240 + 240 = 960"),
        EX("Worked example 3: why did the bread not rise?", intro="A student's bread dough stayed small and dense. Give three possible causes.", steps=[
            S("Dead yeast", text="The water was too hot (above about 55 to 60 degrees Celsius), or the yeast was old."),
            S("No time or warmth", text="The dough was not left long enough in a warm place to prove."),
            S("Too much salt or too little kneading", text="Salt slows yeast, and under-kneaded dough does not build enough gluten to trap the gas."),
        ]),
        H("Bread making in brief"),
        T("Bread uses strong flour, yeast, a little sugar to feed the yeast, salt and warm water. Mix to a dough, **knead** for about ten minutes until smooth and elastic, cover and **prove** in a warm place until it has doubled in size. "
          "**Knock back** (knead again briefly to remove large gas bubbles), shape, prove again, and bake in a hot oven (about 220 degrees Celsius). The bread is cooked when it sounds hollow when tapped on the base. "
          "In the oven, the yeast is killed, the gas expands, the gluten sets and the crust browns."),
        TIP("Paper 2 and Paper 3 test raising agents, methods and faults. Learn one example for each method, a reason for each step, and the science behind each raising agent. "
            "The Board reported that Paper 3 candidates performed well, and advised teachers to give more practical work, so practise these methods at home or in the laboratory.", title="Exam link"),
        MISTAKE("Saying that yeast is a chemical", "Yeast is a living fungus. Baking powder is the chemical raising agent. Hot water kills yeast."),
        MISTAKE("Scaling only one ingredient", "When a recipe is scaled, every ingredient must be multiplied by the same factor, or the mixture will not work."),
        QUIZ("Which raising agent is a living organism?", [
            "Baking powder", "Bicarbonate of soda", "Yeast", "Steam",
        ], 2, "Yeast is a living single-celled fungus that ferments sugar and releases carbon dioxide.",
            hint="Which one needs food and warmth?",
            feedback=["Baking powder is a chemical mixture.", "Bicarbonate of soda is a chemical.", "", "Steam is water vapour."]),
        QUIZ("In the creaming method, which two ingredients are beaten together first?", [
            "Flour and eggs", "Fat and sugar", "Eggs and milk", "Flour and baking powder",
        ], 1, "Fat and sugar are creamed until pale and fluffy, trapping air.",
            hint="The name 'creaming' refers to the soft mixture.",
            feedback=["Flour is added last in creaming.", "", "Eggs are added a little at a time after creaming.", "Flour and baking powder are sieved together and folded in."]),
        PQ("Name four raising agents and state how each works.", "Air: trapped by whisking, sieving and creaming, expands in the heat. Steam: water turns to steam in a hot oven. Baking powder: gives carbon dioxide when wet and warm. Yeast: ferments sugar to give carbon dioxide."),
        PQ("Describe the rubbing-in method and name two foods made by it.", "Rub the fat into the flour with fingertips until it looks like breadcrumbs, then add liquid to bind. Examples: scones, rock cakes, shortcrust pastry."),
        PQ("A teaching recipe for 6 buns uses 150 g flour and 30 g sugar. Find the amounts for 15 buns.", "Factor: 15 / 6 = 2.5. Flour: 150 x 2.5 = 375 g. Sugar: 30 x 2.5 = 75 g."),
        PQ("Why is water that is too hot harmful in bread making?", "Yeast is killed above about 55 to 60 degrees Celsius, so no gas is produced and the dough will not rise."),
        SUM("Raising agents put gas into mixtures: air, steam, carbon dioxide from baking powder or bicarbonate of soda, and carbon dioxide from yeast fermentation.",
            "Baking powder is bicarbonate of soda plus an acid; yeast is a living fungus killed by great heat.",
            "Methods: rubbing-in (scones, pastry), creaming (cakes), whisking (sponges), batters, and dough (bread).",
            "Gluten from wheat flour proteins holds the gas; kneading builds it and bread needs strong flour.",
            "When scaling a recipe, multiply every ingredient by the same factor."),
    ],
))
