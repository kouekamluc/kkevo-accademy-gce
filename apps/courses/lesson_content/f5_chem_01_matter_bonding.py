"""Form 5 Chemistry: Matter, Atomic Structure & Bonding (14 lessons, one practice set each)."""

from .dsl import *  # noqa: F403

COURSE = ("chemistry", "form-5")

MODULE = "Matter, Atomic Structure & Bonding"
STATES = "States of matter and kinetic theory"
PURE = "Pure substances, mixtures and separation"
ATOM = "Atomic structure, isotopes and relative atomic mass"
CONFIG = "Electronic configuration and the periodic table"
TRENDS = "Periodic trends and groups"
BOND = "Chemical bonding"
SOLIDS = "Structure and properties of solids"

LESSONS = []

# ------------------------------------------------------------------ 1. States of matter and kinetic theory
LESSONS.append(lesson(
    module=MODULE,
    topic=STATES,
    title="The three states of matter and the kinetic theory",
    slug="cha-states-kinetic-theory",
    minutes=18,
    summary="Matter is made of tiny particles that are always moving. The kinetic theory explains why solids, liquids and gases differ, and why gases spread out and can be squeezed.",
    objectives=[
        "Name the three states of matter and describe the arrangement and movement of the particles in each",
        "State the main ideas of the kinetic theory of matter",
        "Use the theory to explain compression, shape, volume and gas pressure",
        "Explain diffusion and Brownian motion",
    ],
    key_concepts=["Matter", "Particle", "Kinetic theory", "Solid, liquid, gas", "Diffusion", "Brownian motion"],
    blocks=[
        H("Introduction"),
        T("When a woman roasts fish at a roadside in Douala, you smell it from far away. A block of ice is hard, but when it melts "
          "it flows. Air is all around you, yet you cannot hold it in your hand. Why do solids, liquids and gases behave so differently?"),
        T("Chemists answer with one idea: everything is made of tiny **particles** that are always moving. In this lesson you will "
          "use that idea, called the kinetic theory, to explain what you see every day."),
        D("**Matter** is anything that has mass and takes up space. All matter exists in one of three **states**: solid, liquid or gas.", title="Definition: matter"),
        D("The **kinetic theory of matter** says that all matter is made of tiny particles (atoms, molecules or ions) that are "
          "always moving. The higher the temperature, the faster the particles move.", title="Definition: kinetic theory"),
        H("Particles in solids, liquids and gases"),
        IMG("f5ch-a-states.svg",
            alt="Three boxes. Solid: particles in a regular pattern, touching. Liquid: particles close together but irregular, filling the bottom of the box. Gas: a few particles far apart with arrows showing random movement.",
            caption="Figure 1. The arrangement of particles in a solid, a liquid and a gas."),
        KEY("How the three states differ", "The differences come from how close the particles are and how strongly they attract one another.", cards=[
            ["Solid", "Particles are very close, in a regular pattern. Strong forces hold them in place. They only vibrate."],
            ["Liquid", "Particles are close but not in a pattern. They can slide past each other, so a liquid flows."],
            ["Gas", "Particles are far apart and move quickly in all directions. The forces between them are very weak."],
        ]),
        CODE("""Property            Solid       Liquid       Gas
Shape               fixed       takes the    fills the
                                container    container
Volume              fixed       fixed        not fixed
Can be compressed?  no          hardly       yes, easily
Flows?              no          yes          yes
Density             high        fairly high  very low""", "text", title="Summary of properties"),
        T("Use the theory to explain each property. A **solid** has a fixed shape because its particles cannot leave their places. "
          "A **liquid** takes the shape of its container because its particles can move around, but its volume is fixed because they "
          "stay close together. A **gas** fills any container because its particles move freely and the forces between them are weak."),
        T("A gas can be **compressed** (squeezed into a smaller volume) because most of a gas is empty space between the particles. "
          "The particles of a solid or a liquid are already touching, so there is almost no space to squeeze them into. "
          "This is why a bicycle pump can push air into a tyre."),
        T("A gas also exerts **pressure**. The particles hit the walls of the container again and again, and the many tiny hits "
          "add up to a steady push on the wall. This is what you feel when you press the end of a closed bicycle pump."),
        H("Diffusion and Brownian motion"),
        D("**Diffusion** is the spreading of particles of one substance through another substance, from where there are many "
          "particles to where there are fewer, until they are evenly mixed.", title="Definition: diffusion"),
        T("Diffusion is fastest in gases, slower in liquids and almost zero in solids. It is also faster at a higher temperature, "
          "because the particles move faster. Among gases, **lighter particles diffuse faster** than heavier ones."),
        D("**Brownian motion** is the random zig-zag movement of tiny solid specks (such as smoke or pollen grains) in a gas or a "
          "liquid. It happens because fast-moving particles of the gas or liquid keep hitting the speck from all sides.", title="Definition: Brownian motion"),
        T("Brownian motion is seen under a microscope. It is evidence that the particles of a gas or liquid really exist and really move, "
          "even though we cannot see them."),
        H("Worked examples"),
        EX("Worked example 1: compression", intro="Explain why air in a sealed syringe can be squeezed, but water in the same syringe cannot.", steps=[
            S("Look at the spacing", text="In a gas the particles are far apart, so there is a lot of empty space between them."),
            S("Explain the gas", text="Pushing the plunger moves the air particles closer together, so the gas is compressed."),
            S("Explain the liquid", text="The particles of water are already close together and touching, so there is no empty space to push them into."),
            S("Conclusion", text="Gases can be compressed easily. Liquids cannot be compressed in practice."),
        ]),
        EX("Worked example 2: diffusion", intro="A drop of ink is placed in a glass of water and left without stirring. After some time the whole glass is coloured. Explain this.", steps=[
            S("Name the process", text="This is diffusion."),
            S("Use particles", text="Ink particles and water particles are both always moving. They move randomly and slowly mix."),
            S("Direction", text="Ink particles spread from the region of high concentration (the drop) to regions of low concentration."),
            S("Prediction", text="In hot water the colour spreads faster, because the particles move faster."),
        ]),
        EX("Worked example 3: which gas diffuses faster?", intro="A cotton-wool pad with ammonia solution (NH₃) is placed at one end of a long glass tube and a pad with hydrogen chloride solution (HCl) at the other end. A white ring of ammonium chloride forms. Does it form nearer the NH₃ end or the HCl end?", steps=[
            S("Compare the particles", text="An NH₃ molecule has a mass of 17 units. An HCl molecule has a mass of 36.5 units, so it is heavier."),
            S("Apply the rule", text="Lighter particles diffuse faster, so ammonia travels further in the same time."),
            S("Locate the ring", text="The two gases meet where they have spread to the same place. This is nearer the HCl end, because HCl has travelled a shorter distance."),
        ]),
        MISTAKE("Saying the particles expand or melt", "When a substance is heated its particles move faster and, in a gas, move further apart. The particles themselves do not get bigger. Write: 'the particles move faster and spread out', not 'the particles expand'."),
        MISTAKE("Thinking particles in a solid do not move", "The particles of a solid are not still. They vibrate about fixed positions. Say 'vibrate in fixed positions', never 'do not move'."),
        MISTAKE("Mixing up diffusion with dissolving", "Diffusion is the spreading of particles by their own movement. It happens in any gas or liquid, with no need for a solvent."),
        QUIZ("Which statement about the particles in a liquid is correct?", [
            "They are far apart and move randomly",
            "They are close together and can slide past each other",
            "They are in a regular pattern and only vibrate",
            "They are far apart and in a regular pattern"], 1,
            "In a liquid the particles are close together but not in a fixed pattern, so they can move past one another and the liquid flows.",
            hint="Think of how water flows but is hard to compress.",
            feedback=["This describes a gas.", "", "This describes a solid.", "No state has particles that are far apart in a regular pattern."]),
        QUIZ("Smoke particles in the air under a microscope move in a random zig-zag. What causes this?", [
            "The smoke particles are alive",
            "Air currents from the microscope lamp",
            "Fast-moving air particles hitting the smoke particles from different sides",
            "The smoke particles are attracted to each other"], 2,
            "Brownian motion is caused by the unequal hits of the fast-moving particles of the air on each tiny speck.",
            hint="What is invisible but constantly colliding with the smoke?",
            feedback=["Smoke is not alive. The motion is caused by collisions.", "The motion happens even in still air.", "", "Attraction would pull them together, not make them zig-zag."]),
        TIP("This topic appears in Paper 1 (multiple choice) as particle diagrams, and in Paper 2 as short explanations. Always answer in terms of "
            "particles: say how they are arranged, how close they are, and how they move.", title="Exam link"),
        H("Practice questions"),
        PQ("Describe the arrangement and movement of the particles in a gas.", "The particles are far apart, with no pattern. They move quickly and randomly in all directions, and the forces between them are very weak."),
        PQ("Use the kinetic theory to explain why a gas can be compressed but a solid cannot.", "The particles of a gas are far apart with a lot of empty space between them, so they can be pushed closer together. The particles of a solid are already touching in a fixed arrangement, so there is no space to move them into."),
        PQ("Explain how a gas exerts pressure on the walls of its container.", "The gas particles move randomly at high speed and keep colliding with the walls. Millions of collisions each second give a steady force on the walls, which is the pressure."),
        PQ("Why does perfume sprayed in one corner of a room soon reach the other side?", "Perfume particles spread by diffusion. The air particles and perfume particles are always moving, so the perfume particles spread from the high concentration near the spray to low concentration across the room."),
        SUM("All matter is made of tiny particles that are always moving. Their speed rises with temperature.",
            "In a solid the particles vibrate in fixed places. In a liquid they slide past each other. In a gas they move freely and far apart.",
            "Gases are easily compressed because there is a lot of empty space. They exert pressure by hitting the container walls.",
            "Diffusion is the spreading of particles from high to low concentration. Lighter particles diffuse faster.",
            "Brownian motion is the random movement of tiny specks caused by collisions with fast-moving particles."),
    ],
))

# ------------------------------------------------------------------ 2. Changes of state and heating/cooling curves
LESSONS.append(lesson(
    module=MODULE,
    topic=STATES,
    title="Changes of state and heating and cooling curves",
    slug="cha-heating-cooling-curves",
    minutes=20,
    summary="Substances change state when they gain or lose energy. A heating or cooling curve shows temperature against time, and the flat parts show melting, boiling or freezing of a pure substance.",
    objectives=[
        "Name the six changes of state and explain them with the kinetic theory",
        "Distinguish evaporation from boiling",
        "Read melting and boiling points from a heating or cooling curve",
        "Explain why the temperature stays constant during a change of state and how impurities change melting and boiling points",
    ],
    key_concepts=["Melting point", "Boiling point", "Evaporation", "Sublimation", "Heating curve", "Cooling curve"],
    blocks=[
        H("Introduction"),
        T("Water in a pot on a charcoal fire first gets hot, then bubbles, then turns to steam. Ice from a cold-box melts on a market "
          "table in the sun. These are **changes of state**. In each one the substance stays the same: ice, water and steam are all H₂O."),
        D("A **change of state** happens when a substance changes from solid, liquid or gas to another of these states. It is a physical change: "
          "no new substance is made.", title="Definition: change of state"),
        H("The six changes of state"),
        CODE("""melting        solid  -> liquid       (heat taken in)
freezing       liquid -> solid        (heat given out)
evaporation    liquid -> gas          (heat taken in)
boiling        liquid -> gas          (heat taken in)
condensation   gas    -> liquid       (heat given out)
sublimation    solid  <-> gas         (direct, no liquid stage)""", "text", title="Changes of state"),
        T("When a solid is heated its particles vibrate more and more. At the **melting point** they vibrate so strongly that they break "
          "out of their fixed positions and the solid becomes a liquid. At the **boiling point** the particles have enough energy to "
          "escape from each other completely and become a gas."),
        D("The **melting point** is the fixed temperature at which a pure solid changes into a liquid. The **freezing point** of the "
          "same liquid is the same temperature. The **boiling point** is the fixed temperature at which a pure liquid boils.", title="Definitions: melting point and boiling point"),
        T("Water melts and freezes at 0 °C and boils at 100 °C when the air pressure is normal (at sea level). The boiling point changes "
          "with pressure. On the top of Mount Cameroon the air pressure is lower, so water boils below 100 °C."),
        D("**Sublimation** is the change of a solid straight into a gas (and the reverse) without passing through the liquid state. "
          "Examples are iodine, ammonium chloride and dry ice (solid carbon dioxide).", title="Definition: sublimation"),
        H("Evaporation and boiling are not the same"),
        KEY("Two ways a liquid becomes a gas", "Both need energy, but they happen differently.", cards=[
            ["Evaporation", "Happens at the surface only, at any temperature below the boiling point. Only the fastest particles escape. It is slow and the liquid cools."],
            ["Boiling", "Happens throughout the liquid, at the boiling point only. Bubbles of gas form inside the liquid. It is fast."],
        ], note="Wet clothes dry on a line by evaporation, not by boiling. Wind and sunshine make evaporation faster."),
        H("Heating and cooling curves"),
        T("A **heating curve** is a graph of temperature against time while a substance is heated steadily. Figure 1 shows water."),
        IMG("f5ch-a-heating-curve.svg",
            alt="Heating curve of water. A rises from below 0 degrees to 0; B is flat at 0 degrees while ice melts; C rises from 0 to 100 degrees; D is flat at 100 degrees while water boils; E rises as steam is heated.",
            caption="Figure 1. The heating curve of water. The flat sections B and D are changes of state."),
        T("In the **sloping parts** (A, C, E) the heat makes the particles move faster, so the temperature rises. In the **flat parts** (B, D) "
          "the heat does not raise the temperature. All the energy is used to pull the particles apart against the forces between them. "
          "The solid and liquid, or the liquid and gas, exist together at this one temperature."),
        T("A **cooling curve** is the opposite. When a hot liquid is cooled it loses heat, and the temperature falls until it reaches the freezing point. "
          "It then stays constant while the liquid freezes, because the particles give out energy as they settle into place. "
          "After that the solid cools further."),
        KEY("Pure substance or mixture?", "A pure substance changes state at one sharp, fixed temperature. This is why the curve has a perfectly flat part.", cards=[
            ["Pure substance", "Sharp melting point and boiling point. Flat parts on the curve."],
            ["Impure substance", "Melts over a range of temperatures, and at a lower temperature than the pure substance. Boils at a higher temperature."],
        ], note="Chemists use melting point and boiling point to test purity."),
        H("Worked examples"),
        EX("Worked example 1: reading a table of results", intro="A pure solid is heated steadily. The temperature is read every 2 minutes.", steps=[
            S("The results", text="Time (min): 0, 2, 4, 6, 8, 10, 12, 14. Temperature (°C): 40, 60, 80, 80, 80, 80, 100, 120."),
            S("Find the melting point", text="The temperature stays at 80 °C for a while, so the melting point is 80 °C."),
            S("Find how long melting lasted", text="The temperature is 80 °C from 4 min to 10 min, so melting took 10 − 4 = 6 minutes."),
            S("State at 8 minutes", text="The substance is melting, so it is a mixture of solid and liquid."),
            S("State at 14 minutes", text="The temperature is above the melting point and rising, so it is a liquid (if the boiling point has not been reached)."),
        ]),
        EX("Worked example 2: explain a flat part", intro="Explain why the temperature of boiling water stays at 100 °C although the heater is still on.", steps=[
            S("Where does the heat go?", text="The particles at 100 °C already have enough energy to move around freely."),
            S("Use the kinetic theory", text="The extra energy is used to pull the liquid particles completely apart from each other and turn them into a gas."),
            S("Conclusion", text="None of the energy increases the speed of the particles, so the temperature does not rise until all the liquid has turned to gas."),
        ]),
        EX("Worked example 3: evaporation", intro="Explain why wet washing dries faster on a hot, windy day.", steps=[
            S("Name the process", text="The water leaves by evaporation, from the surface of the cloth."),
            S("Heat", text="At a higher temperature more water particles have enough energy to escape."),
            S("Wind", text="Wind carries away the escaped water particles, so more can leave."),
        ]),
        MISTAKE("Saying the temperature rises during melting", "During melting or boiling of a pure substance the temperature stays constant. The heat is used to change the state, not to raise the temperature."),
        MISTAKE("Confusing boiling with evaporation", "Evaporation happens at the surface at any temperature. Boiling happens throughout the liquid at the boiling point only."),
        QUIZ("A cooling curve of a pure liquid has a flat section at 54 °C. What is happening in that section?", [
            "The liquid is boiling",
            "The liquid is freezing",
            "The solid is melting",
            "The particles have stopped moving"], 1,
            "On cooling, the flat section is the freezing point. The liquid is changing into a solid at 54 °C and the particles are giving out energy.",
            hint="Is the substance getting hotter or colder?",
            feedback=["Boiling happens on heating and gives a flat part at the boiling point.", "", "Melting happens on heating, not cooling.", "Particles never stop moving, even in a solid."]),
        QUIZ("A student heats a sample and sees it melt gradually between 78 °C and 84 °C. What does this suggest?", [
            "The sample is a pure substance",
            "The sample is impure",
            "The sample is a gas",
            "The thermometer is broken"], 1,
            "A pure solid melts at one sharp temperature. Melting over a range of temperatures, below the true melting point, shows the sample is impure.",
            hint="Think of the sharp melting point of a pure substance.",
            feedback=["A pure substance would give a sharp melting point.", "", "The sample is a solid that melts, not a gas.", "Nothing suggests a fault; this is a typical result for an impure solid."]),
        TIP("Heating curves and the explanation of the flat parts appear in Paper 1 as graph-reading questions and in Paper 2 as short "
            "explanations. Always say that the energy is used to overcome the forces between particles.", title="Exam link"),
        H("Practice questions"),
        PQ("Name the change of state when (a) ice becomes water and (b) steam becomes water.", "(a) melting. (b) condensation."),
        PQ("State two differences between evaporation and boiling.", "Evaporation happens only at the surface and at any temperature below the boiling point; it is slow. Boiling happens throughout the liquid at the boiling point only, with bubbles; it is fast."),
        PQ("A pure substance is cooled from 90 °C. The temperature falls to 62 °C and stays at 62 °C for 5 minutes before it falls again. What is the freezing point, and why does the temperature stay constant?", "The freezing point is 62 °C. The temperature stays constant because the particles give out energy as they join the solid. This energy balances the heat lost to the surroundings until all the liquid has frozen."),
        PQ("How do impurities change the melting point and the boiling point of a pure substance?", "Impurities lower the melting point and raise the boiling point, and the change of state takes place over a range of temperatures instead of one sharp temperature."),
        SUM("The six changes of state are melting, freezing, evaporation, boiling, condensation and sublimation.",
            "Evaporation is at the surface at any temperature; boiling is throughout the liquid at the boiling point.",
            "A heating or cooling curve of a pure substance has flat parts at the melting or boiling point.",
            "During a change of state the energy goes into overcoming forces between particles, so the temperature stays constant.",
            "Impurities lower the melting point and raise the boiling point; a pure substance has sharp fixed values."),
    ],
))

# ------------------------------------------------------------------ 3. Pure substances, elements, compounds, mixtures
LESSONS.append(lesson(
    module=MODULE,
    topic=PURE,
    title="Pure substances, elements, compounds and mixtures",
    slug="cha-pure-substances-mixtures",
    minutes=18,
    summary="A pure substance contains only one substance. Elements and compounds are pure; mixtures are not. Learn how to tell a mixture from a compound and name the types of mixture.",
    objectives=[
        "Define element, compound, mixture and pure substance",
        "Compare a mixture with a compound using iron and sulfur",
        "Name types of mixture: solution, suspension, emulsion and alloy",
        "Use the terms solute, solvent, solution, soluble and insoluble correctly",
    ],
    key_concepts=["Element", "Compound", "Mixture", "Pure substance", "Solution", "Alloy"],
    blocks=[
        H("Introduction"),
        T("A bottle of 'pure' mineral water in a shop in Yaoundé is clear and tasty, but a chemist would not call it pure. It contains small "
          "amounts of dissolved minerals. In chemistry, **pure** has a strict meaning. This lesson shows you how chemists sort everything "
          "around us into elements, compounds and mixtures."),
        H("Elements, compounds and pure substances"),
        D("An **element** is a pure substance made of only one kind of atom. It cannot be broken down into simpler substances by chemical reactions. "
          "Examples: iron (Fe), oxygen (O₂), carbon (C), sulfur (S), gold (Au).", title="Definition: element"),
        D("A **compound** is a pure substance made of two or more different elements that are chemically joined together in a fixed ratio. "
          "It can be broken down into its elements only by chemical reactions. Examples: water (H₂O), sodium chloride (NaCl), carbon dioxide (CO₂).", title="Definition: compound"),
        D("A **mixture** is made of two or more substances that are only physically mixed. They are not chemically joined, so each keeps its own properties, "
          "and they can be present in any proportion. Examples: air, sea water, soil, palm oil mixed with water.", title="Definition: mixture"),
        D("A **pure substance** is one that contains only a single substance: one element or one compound. It has a fixed composition and sharp melting and boiling points.", title="Definition: pure substance"),
        KEY("A quick way to sort substances", "Ask two questions.", cards=[
            ["Is it made of one substance only?", "If yes, it is pure: an element (one kind of atom) or a compound (different atoms joined)."],
            ["Is it two or more substances just mixed?", "If yes, it is a mixture. It can be separated by physical methods."],
        ]),
        H("Mixture or compound? Iron and sulfur"),
        T("Iron filings (a grey powder) and sulfur (a yellow powder) can be mixed in any proportion. This is a mixture. The two powders "
          "can still be seen, and a magnet picks out the iron. If the mixture is heated strongly, the two elements react and a new black "
          "substance, iron(II) sulfide, forms. This is a compound."),
        T("Word equation: iron + sulfur → iron(II) sulfide. Chemical equation: Fe + S → FeS."),
        CODE("""                    Mixture of Fe and S          Compound FeS
Made by             mixing only                  chemical reaction
Proportions         any amounts                  fixed (1 Fe : 1 S)
Properties          each part keeps its own      new properties
Magnet              iron is attracted            not attracted
Separation          physical methods             chemical reactions only
Energy change       little or none               heat given out or taken in""", "text", title="Mixture compared with compound"),
        H("Types of mixture"),
        KEY("Common types of mixture", "Chemists use special names for different kinds of mixture.", cards=[
            ["Solution", "A solid, liquid or gas dissolved in a liquid. Salt in water. It is clear and the particles are too small to see."],
            ["Suspension", "Insoluble solid particles spread through a liquid. Muddy water. It looks cloudy and the solid settles on standing."],
            ["Emulsion", "Tiny drops of one liquid spread through another liquid that does not mix with it. Oil in water."],
            ["Alloy", "A mixture of a metal with other elements, usually other metals. Brass is copper and zinc; bronze is copper and tin."],
        ]),
        T("Air is a mixture of gases: about four-fifths nitrogen and one-fifth oxygen, with small amounts of argon, carbon dioxide and water vapour."),
        H("Words to know about solutions"),
        D("A **solute** is the substance that dissolves. A **solvent** is the liquid in which it dissolves. The two together form a **solution**. "
          "Water is the commonest solvent. In a cup of sweet tea, sugar is the solute and the tea is the solvent.", title="Definition: solute, solvent and solution"),
        T("A substance is **soluble** if it dissolves in a solvent and **insoluble** if it does not. Sugar is soluble in water. Sand is insoluble in water. "
          "Two liquids that mix completely are **miscible** (ethanol and water). Two that do not mix, and form layers, are **immiscible** (oil and water)."),
        H("Worked examples"),
        EX("Worked example 1: classify the substances", intro="Classify each of these as an element, a compound or a mixture: (a) sulfur, (b) sea water, (c) carbon dioxide, (d) brass.", steps=[
            S("(a) sulfur", text="One kind of atom only, so an element."),
            S("(b) sea water", text="Water with salts and other substances dissolved in it. It is a mixture (a solution)."),
            S("(c) carbon dioxide", text="Carbon and oxygen atoms chemically joined in a fixed ratio, so a compound."),
            S("(d) brass", text="Copper and zinc mixed. It is a mixture, and since it is a mixture of metals, an alloy."),
        ]),
        EX("Worked example 2: why is it a compound?", intro="Hydrogen and oxygen are both gases. They react to give water, which is a liquid. Explain why water is a compound and not a mixture of hydrogen and oxygen.", steps=[
            S("Check the properties", text="Water has very different properties from hydrogen or oxygen. In a mixture each part would keep its own properties."),
            S("Check the ratio", text="Water always has 2 hydrogen atoms for each oxygen atom. A mixture could have any proportions."),
            S("Check the separation", text="The elements can only be separated again by a chemical reaction (electrolysis), not by simple physical methods."),
        ]),
        EX("Worked example 3: use the words correctly", intro="Sugar is stirred into water until it disappears. Name the solute, the solvent and the solution.", steps=[
            S("Solute", text="Sugar, because it dissolves."),
            S("Solvent", text="Water, the liquid in which the sugar dissolves."),
            S("Solution", text="The clear sugar solution that forms."),
        ]),
        MISTAKE("Thinking that 'pure' means 'natural' or 'clean'", "In chemistry, pure means only one substance. Pure water has only H₂O. Clean drinking water, mineral water and natural juice are mixtures."),
        MISTAKE("Calling a mixture a compound because it looks even", "A solution looks the same all through, but it is still a mixture. Only a chemical reaction makes a compound."),
        QUIZ("Which of these is a compound?", ["Air", "Sea water", "Sodium chloride", "Brass"], 2,
             "Sodium chloride (NaCl) has sodium and chlorine chemically joined in a fixed ratio. The other three are mixtures.",
             hint="A compound has a fixed formula.",
             feedback=["Air is a mixture of gases.", "Sea water is salt and other things dissolved in water.", "", "Brass is an alloy, a mixture of copper and zinc."]),
        QUIZ("When iron filings and sulfur are heated strongly, a black solid forms that is not attracted by a magnet. This shows that", [
            "a mixture has formed",
            "a new compound has formed",
            "the iron has dissolved",
            "the sulfur has evaporated"], 1,
            "A new substance with new properties (not magnetic) has formed. This is a chemical reaction making the compound iron(II) sulfide.",
            hint="Think about what a mixture would do to a magnet.",
            feedback=["In a mixture the iron would still be attracted by the magnet.", "", "The iron has reacted, not dissolved.", "Sulfur has joined with iron. It has not just evaporated."]),
        TIP("Paper 1 often asks you to classify a substance or to choose a property that shows a mixture from a compound. In Paper 2 you may be asked to define "
            "the terms and give examples. Always give an example in your definition.", title="Exam link"),
        H("Practice questions"),
        PQ("Define the term 'compound' and give two examples.", "A compound is a pure substance made of two or more elements chemically joined in a fixed ratio. Examples: water (H₂O) and carbon dioxide (CO₂)."),
        PQ("State three differences between a mixture and a compound.", "In a mixture the parts keep their own properties; in a compound there are new properties. A mixture can have any proportions; a compound has a fixed ratio. A mixture can be separated by physical methods; a compound needs a chemical reaction."),
        PQ("Muddy water from a river is left in a bucket. The mud settles. What type of mixture is muddy water?", "It is a suspension, because insoluble solid particles are spread through water and settle on standing."),
        PQ("Name the solute and the solvent when salt dissolves in water.", "The salt is the solute and the water is the solvent."),
        SUM("An element has one kind of atom; a compound has different elements chemically joined in a fixed ratio.",
            "A mixture is only physically mixed, with any proportions, and each part keeps its properties.",
            "A pure substance is one element or one compound with sharp melting and boiling points.",
            "Types of mixture include solution, suspension, emulsion and alloy.",
            "In a solution the solute dissolves in the solvent; soluble substances dissolve, insoluble ones do not."),
    ],
))

# ------------------------------------------------------------------ 4. Separation techniques
LESSONS.append(lesson(
    module=MODULE,
    topic=PURE,
    title="Separation techniques",
    slug="cha-separation-techniques",
    minutes=22,
    summary="Mixtures are separated by physical methods that use differences in properties: filtration, evaporation, crystallization, distillation, separating funnel, magnet and sublimation.",
    objectives=[
        "Choose a separation method from the properties of the substances in a mixture",
        "Describe filtration, evaporation, crystallization, simple and fractional distillation, the separating funnel, magnetic separation and sublimation",
        "Describe the apparatus for filtration and simple distillation",
        "Plan the separation of a mixture of several substances in the right order",
    ],
    key_concepts=["Filtration", "Residue and filtrate", "Crystallization", "Simple distillation", "Fractional distillation", "Separating funnel"],
    blocks=[
        H("Introduction"),
        T("On the coast near Limbe, salt is made by letting sea water evaporate in the sun. A farmer sieves sand out of garri flour. Palm oil is "
          "left in a bottle until the water sinks below it. Each of these is a way of **separating a mixture**."),
        T("A mixture can be separated by **physical methods** because its parts are not chemically joined. The best method depends on how the "
          "substances differ: whether one dissolves, whether they have different boiling points, whether one is magnetic."),
        D("**Separation techniques** are physical methods used to separate the substances in a mixture, using differences in their physical properties.", title="Definition: separation techniques"),
        H("Separating a solid from a liquid"),
        KEY("Filtration", "Use it to separate an insoluble solid from a liquid.", cards=[
            ["How it works", "The mixture is poured through filter paper in a funnel. The tiny holes let liquid through but not solid particles."],
            ["Names", "The solid left on the paper is the residue. The liquid that passes through is the filtrate."],
        ], note="Example: sand from salt solution. Sand is the residue; the salt solution is the filtrate."),
        IMG("f5ch-a-filtration.svg",
            alt="A funnel with filter paper above a beaker. The mixture of sand and salt solution is poured in; sand remains on the paper and salt solution drips into the beaker.",
            caption="Figure 1. Filtration. The residue stays on the filter paper; the filtrate goes into the beaker."),
        KEY("Evaporation and crystallization", "Use them to get a dissolved solid out of a solution.", cards=[
            ["Evaporation to dryness", "Heat the solution until all the water has gone. The solid is left in the dish. It is quick, but it can spoil solids that decompose on strong heating."],
            ["Crystallization", "Heat the solution gently to evaporate some of the water until it is almost saturated. Leave it to cool slowly. Crystals form. Filter them off, wash with a little cold distilled water and dry between filter papers."],
        ], note="Crystallization gives larger, purer crystals. Salt makers on the coast use evaporation in the sun."),
        KEY("Decanting", "Use it when a solid settles to the bottom.", cards=[
            ["How it works", "Let the solid settle, then carefully pour off the liquid above it. It is simple but leaves some liquid with the solid."],
        ]),
        H("Distillation"),
        T("Distillation separates a liquid from a solution or from another liquid by using differences in **boiling point**. "
          "The liquid is boiled, the vapour is cooled in a condenser, and the liquid that collects is called the **distillate**."),
        IMG("f5ch-a-distillation.svg",
            alt="Simple distillation apparatus: a flask of mixture heated from below with a thermometer at the neck, a slanting condenser with cold water entering at the bottom and leaving at the top, and a beaker collecting the distillate.",
            caption="Figure 2. Simple distillation. Cold water enters at the bottom of the condenser and leaves at the top, so the jacket stays full."),
        D("**Simple distillation** separates a pure liquid (the solvent) from a solution. Example: pure water from salty water. The water boils and "
          "condenses in the condenser. The salt does not boil, so it stays behind in the flask.", title="Definition: simple distillation"),
        D("**Fractional distillation** separates a mixture of liquids that mix with each other (miscible) and have different boiling points. A "
          "fractionating column is fitted above the flask. The liquid with the **lower boiling point** reaches the top first and is collected first.", title="Definition: fractional distillation"),
        T("Example: ethanol (boiling point 78 °C) and water (100 °C). When the mixture is heated, the vapour that rises up the column is rich in ethanol. The "
          "thermometer reads about 78 °C while ethanol distils. When it starts to rise towards 100 °C, water is beginning to distil and the receiver "
          "should be changed. Crude oil and liquid air are also separated by fractional distillation."),
        H("Other methods"),
        KEY("Separating funnel", "Use it to separate two liquids that do not mix (immiscible), such as palm oil and water.", cards=[
            ["How it works", "The mixture is left to form two layers in the funnel. The denser liquid is at the bottom. Open the tap and run the bottom layer out into one beaker, then close the tap and pour the top layer out of the neck."],
        ]),
        KEY("Magnet", "Use it to separate a magnetic substance from a non-magnetic one.", cards=[
            ["How it works", "Iron, cobalt and nickel are attracted by a magnet. Iron filings can be pulled out of sulfur or sand with a magnet."],
        ]),
        KEY("Sublimation", "Use it when one solid sublimes on heating and the other does not.", cards=[
            ["How it works", "Heat the mixture. The solid that sublimes becomes a gas, leaves the other solid behind, and condenses back to solid on a cool surface above the dish. Ammonium chloride can be separated from sand this way."],
        ]),
        CODE("""Mixture                          Method               Property used
sand and water                   filtration           sand is insoluble
salt from salt solution          crystallization      salt is soluble, water evaporates
pure water from salt water       simple distillation  water boils, salt does not
ethanol and water                fractional dist.     different boiling points
oil and water                    separating funnel    immiscible, different density
iron filings and sulfur          magnet               iron is magnetic
ammonium chloride and sand       sublimation          ammonium chloride sublimes""", "text", title="Choosing a method"),
        H("Worked examples"),
        EX("Worked example 1: a mixture of three solids", intro="A mixture contains iron filings, sand and salt. Describe how to obtain each substance separately.", steps=[
            S("Use a magnet", text="Pass a magnet over the dry mixture. Iron is magnetic and is pulled out."),
            S("Add water and stir", text="The salt dissolves; the sand is insoluble."),
            S("Filter", text="The sand is the residue; dry it. The salt solution is the filtrate."),
            S("Crystallize the filtrate", text="Heat it gently to evaporate some water, cool it, filter off the salt crystals and dry them."),
        ]),
        EX("Worked example 2: simple distillation", intro="Salty water is heated in a distillation apparatus. (a) Why is cold water fed into the bottom of the condenser? (b) What is left in the flask? (c) What does the thermometer read?", steps=[
            S("(a) Cold water at the bottom", text="The water enters at the bottom and leaves at the top, so the jacket is always full of cold water. This gives better cooling."),
            S("(b) In the flask", text="The salt stays in the flask because it does not boil at this temperature."),
            S("(c) The thermometer", text="It reads about 100 °C, the boiling point of pure water, while the water distils."),
        ]),
        EX("Worked example 3: choose a method", intro="Palm oil and water have been mixed. Which method separates them and which layer is run off first?", steps=[
            S("Identify the type of mixture", text="The liquids do not mix, so they are immiscible."),
            S("Choose the method", text="Use a separating funnel."),
            S("Which layer first?", text="Palm oil is less dense than water, so it floats on top and water is the lower layer. Run the water out first."),
        ]),
        MISTAKE("Using filtration to separate a solution", "The solute in a solution is dissolved and passes through the filter paper with the solvent. Filtration only separates an insoluble solid. To recover the solute use evaporation or crystallization."),
        MISTAKE("Mixing up residue and filtrate", "The residue stays on the paper. The filtrate passes through. Say which is which and name the substance."),
        MISTAKE("Using simple distillation for two liquids with close boiling points", "Simple distillation works when only one substance boils. For two miscible liquids with different boiling points use fractional distillation."),
        QUIZ("Which method is best for separating ethanol from a mixture of ethanol and water?", [
            "Filtration", "Fractional distillation", "A separating funnel", "A magnet"], 1,
            "Ethanol and water mix completely but boil at different temperatures (78 °C and 100 °C), so fractional distillation is used.",
            hint="Do the liquids mix or form layers?",
            feedback=["Filtration separates insoluble solids from liquids.", "", "A separating funnel works only for liquids that do not mix.", "Neither liquid is magnetic."]),
        QUIZ("After filtering a mixture of sand and salt solution, the sand is called the", [
            "filtrate", "residue", "distillate", "solute"], 1,
            "The solid that stays on the filter paper is the residue.",
            hint="Which part stays on the paper?",
            feedback=["The filtrate is the liquid that passes through.", "", "The distillate is the liquid collected in distillation.", "The solute is the dissolved substance."]),
        TIP("Separation techniques are tested in Paper 1 (choose the method) and in Paper 2 Section A and in the practical-skills Section B, where you may "
            "draw or label apparatus, describe a method in steps, or say why a step is done. Always say which property of the substances the method uses.", title="Exam link"),
        H("Practice questions"),
        PQ("Name the method used to obtain pure water from sea water.", "Simple distillation."),
        PQ("Describe how to obtain dry crystals of salt from salt solution.", "Heat the solution gently to evaporate some of the water until it is saturated. Leave it to cool so that crystals form. Filter off the crystals, wash them with a little cold distilled water and dry them between filter papers."),
        PQ("Why must a mixture of two miscible liquids be separated by fractional distillation rather than by a separating funnel?", "Miscible liquids mix completely, so they do not form layers. They can be separated only by their different boiling points."),
        PQ("A mixture of ammonium chloride and sand is heated in a dish with a cold funnel above it. Describe what is seen and why.", "The ammonium chloride sublimes, changing to a gas that rises, and then it condenses as a white solid on the cool funnel. The sand does not sublime, so it stays in the dish."),
        SUM("Mixtures are separated by physical methods that use differences in properties.",
            "Filtration separates an insoluble solid (residue) from a liquid (filtrate). Crystallization recovers a soluble solid from its solution.",
            "Simple distillation separates a solvent from a solution. Fractional distillation separates miscible liquids with different boiling points; the lowest boiling point comes off first.",
            "A separating funnel separates immiscible liquids; the denser liquid is the lower layer.",
            "A magnet separates magnetic substances, and sublimation separates a solid that sublimes from one that does not."),
    ],
))

# ------------------------------------------------------------------ 5. Chromatography and purity
LESSONS.append(lesson(
    module=MODULE,
    topic=PURE,
    title="Paper chromatography, Rf values and tests for purity",
    slug="cha-chromatography-purity",
    minutes=18,
    summary="Paper chromatography separates coloured substances because they travel at different speeds. The Rf value identifies a substance, and a pure substance gives one spot and sharp melting and boiling points.",
    objectives=[
        "Describe how to run a paper chromatogram and why the baseline is drawn in pencil",
        "Interpret a chromatogram to say whether a substance is pure and which substances a mixture contains",
        "Calculate an Rf value",
        "Describe the tests used to check the purity of a substance",
    ],
    key_concepts=["Chromatography", "Solvent front", "Baseline", "Rf value", "Purity"],
    blocks=[
        H("Introduction"),
        T("The bright green on a packet of sweets sold at a market in Bafoussam may be one dye or a blend of several. How can a chemist find out without "
          "tasting it? A very simple method, **paper chromatography**, can show how many substances are in a coloured mixture and what they are."),
        D("**Chromatography** is a method of separating the substances in a mixture by letting a solvent carry them at different speeds through a stationary material, such as filter paper.", title="Definition: chromatography"),
        H("How paper chromatography works"),
        T("A solvent (often water or ethanol) rises up the paper by capillary action. As it moves, it carries the coloured substances with it. "
          "A substance that dissolves well in the solvent and clings only weakly to the paper is carried far. One that dissolves poorly or clings strongly to the paper moves only a short way. "
          "So the substances in a mixture end up at different heights."),
        KEY("Steps in running a chromatogram", "Follow the steps in order.", cards=[
            ["1. Baseline", "Draw a line across the paper with a pencil, about 2 cm from the bottom. Use pencil, because pencil lead does not dissolve in the solvent. Ink would run up the paper too."],
            ["2. Spots", "Put a small spot of each sample on the line, well apart. Let each spot dry. Add more drops on the same spot to make it darker."],
            ["3. Solvent", "Stand the paper in a container with a little solvent. The solvent must be below the baseline, otherwise the spots dissolve in the container."],
            ["4. Develop", "Cover the container and wait. Before the solvent reaches the top, remove the paper and mark the solvent front at once with a pencil. Then dry the paper."],
        ]),
        IMG("f5ch-a-chromatography.svg",
            alt="A paper chromatogram with columns P, Q and M. P has one yellow spot at 6 cm, Q has one blue spot at 3 cm, M has both spots. The solvent front is at 10 cm.",
            caption="Figure 1. A developed chromatogram. P and Q are pure dyes; M is a mixture. Distances are measured from the baseline."),
        H("Reading a chromatogram"),
        T("Look at Figure 1. Dye P gives one spot, so it is pure. Dye Q gives one spot, so it is pure. Mixture M gives two spots, at the same heights as P and Q. "
          "So M contains dyes P and Q. Spots at the **same height** (using the same solvent and paper) are the same substance."),
        KEY("What the spots tell you", "Count and compare the spots.", cards=[
            ["One spot", "The sample is probably a pure substance."],
            ["Two or more spots", "The sample is a mixture. The number of spots is the minimum number of substances."],
            ["Spots match a known sample", "The substance in the mixture is the same as the known substance."],
        ], note="Colourless substances can be made visible with a locating agent, a chemical that reacts with them to give a colour."),
        H("The Rf value"),
        D("The **Rf value** (retention factor) of a substance is the distance moved by the substance divided by the distance moved by the solvent front. Both are measured from the baseline, and the substance distance is measured to the **centre of the spot**.", title="Definition: Rf value", formula=r"R_f = \frac{\text{distance moved by the substance}}{\text{distance moved by the solvent front}}"),
        T("An Rf value has no unit, because it is a ratio of two lengths. It is always between 0 and 1. For a given substance, solvent and paper, the Rf value is the same every time, so it can be used to identify the substance."),
        H("Tests for purity"),
        T("A **pure substance** contains only one substance. Three simple tests are used to check purity."),
        KEY("How to test for purity", "A pure substance passes each test.", cards=[
            ["Melting point", "A pure solid melts at a sharp, fixed temperature. An impure solid melts over a range, at a lower temperature."],
            ["Boiling point", "A pure liquid boils at a fixed temperature. An impure liquid boils over a range, at a higher temperature."],
            ["Chromatography", "A pure substance gives only one spot, whatever solvent is used."],
        ]),
        H("Worked examples"),
        EX("Worked example 1: calculate Rf from Figure 1", intro="In Figure 1 the solvent front moved 10 cm. The yellow spot moved 6 cm and the blue spot 3 cm. Find the Rf value of each dye.", steps=[
            S("Write the formula", math=r"R_f = \frac{\text{distance moved by the substance}}{\text{distance moved by the solvent front}}"),
            S("Yellow dye", math=r"R_f = \frac{6}{10} = 0.6"),
            S("Blue dye", math=r"R_f = \frac{3}{10} = 0.3"),
        ]),
        EX("Worked example 2: identify a dye", intro="A solvent front moves 8.0 cm. An unknown spot has moved 5.2 cm. A reference dye has an Rf of 0.65 in the same solvent. Is the unknown the same dye?", steps=[
            S("Calculate Rf for the unknown", math=r"R_f = \frac{5.2}{8.0} = 0.65"),
            S("Compare", text="The Rf values are the same, 0.65, so the unknown is probably the same dye as the reference."),
        ]),
        EX("Worked example 3: why pencil?", intro="A student draws the baseline in ink and sees extra coloured streaks above it. Explain.", steps=[
            S("What is ink?", text="Ink is made of dyes that dissolve in the solvent."),
            S("What happens?", text="The ink from the baseline dissolves and runs up the paper, forming extra coloured streaks that are not from the sample."),
            S("Fix", text="Use a pencil. Graphite does not dissolve in the solvent."),
        ]),
        MISTAKE("Letting the solvent cover the baseline", "The solvent level must start below the baseline. If it covers the spots they dissolve into the container and the experiment fails."),
        MISTAKE("Measuring to the edge of the spot, or forgetting the solvent front", "Measure to the centre of each spot, and mark the solvent front as soon as you take the paper out. After drying you cannot see where it reached."),
        MISTAKE("Writing a unit for Rf", "Rf has no unit. Do not write cm after it. It is a ratio, and it cannot be bigger than 1."),
        QUIZ("A chromatogram of a sample shows three spots. What does this tell you?", [
            "The sample is a pure substance",
            "The sample is a mixture of at least three substances",
            "The solvent was not pure",
            "The baseline was drawn in ink"], 1,
            "Each spot is a different substance, so the sample contains at least three substances.",
            hint="One spot shows one substance.",
            feedback=["A pure substance gives only one spot.", "", "Nothing in the result points to the solvent.", "Ink would give extra streaks above the baseline, not three clear spots of the sample."]),
        QUIZ("A spot moves 2.4 cm while the solvent front moves 12.0 cm. What is its Rf value?", ["0.20", "0.50", "5.0", "0.24"], 0,
            "Rf = 2.4 divided by 12.0 = 0.20.",
            hint="Divide the distance moved by the substance by the distance moved by the solvent.",
            feedback=["", "This would need the spot to move half way.", "This is the wrong way round: 12.0 divided by 2.4. Rf can never be more than 1.", "This uses 10.0 instead of 12.0 as the distance moved by the solvent front."]),
        TIP("Chromatography appears in Paper 1 as chromatogram-reading questions and in Section B of Paper 2 (the practical-skills section), where you may be asked "
            "to describe the method, draw a chromatogram, calculate Rf, or say why pencil is used.", title="Exam link"),
        H("Practice questions"),
        PQ("Why is the starting line drawn in pencil and not ink?", "Pencil (graphite) does not dissolve in the solvent. Ink dissolves and runs up the paper, so it would give extra spots and spoil the result."),
        PQ("A chromatogram shows that a spot has moved 4.5 cm and the solvent front 9.0 cm. Calculate the Rf value.", "Rf = 4.5 divided by 9.0 = 0.50."),
        PQ("A food dye gives one spot with water as solvent and two spots with ethanol. What can be said about the dye?", "The dye is a mixture. It gave only one spot in water because both substances travelled at the same rate, but with ethanol they separate into two spots."),
        PQ("State two ways of showing that a sample of a solid is pure.", "It has a sharp, fixed melting point, and it gives only one spot in chromatography."),
        SUM("In paper chromatography the solvent carries different substances different distances up the paper.",
            "Use a pencil baseline and keep the solvent below it. Mark the solvent front as soon as the paper is removed.",
            "One spot shows a pure substance; several spots show a mixture; matching spots show the same substance.",
            "Rf = distance moved by the substance divided by the distance moved by the solvent front. It has no unit and is less than 1.",
            "A pure substance has a sharp melting and boiling point and gives one spot."),
    ],
))

# ------------------------------------------------------------------ 6. Subatomic particles, atomic number, mass number, ions
LESSONS.append(lesson(
    module=MODULE,
    topic=ATOM,
    title="Subatomic particles, atomic number and mass number",
    slug="cha-subatomic-particles",
    minutes=18,
    summary="Atoms are made of protons, neutrons and electrons. The atomic number is the number of protons and the mass number is protons plus neutrons. Use them to work out the particles in atoms and ions.",
    objectives=[
        "Describe the structure of an atom and name the three subatomic particles with their relative mass and charge",
        "Define atomic number and mass number",
        "Calculate the numbers of protons, neutrons and electrons in an atom",
        "Work out the particles in an ion and explain how ions form",
    ],
    key_concepts=["Proton, neutron, electron", "Nucleus", "Atomic number", "Mass number", "Ion"],
    blocks=[
        H("Introduction"),
        T("Everything around you, from the iron roof of a house in Kumba to the oxygen in your breath, is built from atoms. An atom is so small that "
          "millions of them in a row would be thinner than a hair. Yet atoms have an inside, and what is inside decides what the element is and how it behaves."),
        D("An **atom** is the smallest particle of an element that can take part in a chemical reaction. It has a tiny central **nucleus** containing **protons** and "
          "**neutrons**, with **electrons** moving around the nucleus in regions called **shells**.", title="Definition: atom"),
        H("The three subatomic particles"),
        CODE("""Particle   Relative mass    Relative charge    Where found
proton     1                +1                 in the nucleus
neutron    1                0 (neutral)        in the nucleus
electron   about 1/1840     -1                 in shells around the nucleus""", "text", title="Subatomic particles"),
        T("The nucleus is very small compared with the whole atom, but almost all the mass of the atom is in it, because protons and neutrons are "
          "about 1840 times heavier than an electron. Most of the atom is empty space where the electrons move."),
        T("An atom has **no overall charge**, because it has the same number of protons (positive) and electrons (negative). The charges cancel."),
        H("Atomic number and mass number"),
        D("The **atomic number** (symbol Z) is the number of protons in the nucleus of an atom. It identifies the element: every atom with 6 protons is carbon.", title="Definition: atomic number"),
        D("The **mass number** (symbol A) is the total number of protons and neutrons in the nucleus of an atom.", title="Definition: mass number"),
        KEY("Three rules to remember", "Use these every time.", cards=[
            ["Protons", "number of protons = atomic number (Z)"],
            ["Electrons (in a neutral atom)", "number of electrons = number of protons = Z"],
            ["Neutrons", "number of neutrons = mass number − atomic number = A − Z"],
        ]),
        CODE("""Notation:   mass number  ->   23
                             Na
            atomic number -> 11

Written in a line: sodium-23 or Na-23""", "text", title="How an atom is written"),
        H("Ions"),
        D("An **ion** is an atom (or group of atoms) that has gained or lost electrons, so it carries an electric charge. The nucleus does not change: the number of protons stays the same.", title="Definition: ion"),
        T("A metal atom usually **loses** electrons and becomes a positive ion (a **cation**). A non-metal atom usually **gains** electrons and becomes a negative ion (an **anion**). "
          "If an atom loses 2 electrons, it has 2 more protons than electrons, so the ion has a charge of 2+. If it gains 1 electron, it has 1 more electron than protons, so the charge is 1−."),
        CODE("""Particle     Z    A    protons   neutrons   electrons
Na           11   23   11        12         11
Na+          11   23   11        12         10
Cl-          17   35   17        18         18
Mg2+         12   24   12        12         10
O2-          8    16   8         8          10
Al3+         13   27   13        14         10""", "text", title="Worked table of atoms and ions"),
        H("Worked examples"),
        EX("Worked example 1: an atom", intro="An atom of potassium has atomic number 19 and mass number 39. Find the number of protons, neutrons and electrons.", steps=[
            S("Protons", text="Number of protons = atomic number = 19."),
            S("Electrons", text="In a neutral atom the electrons equal the protons, so 19 electrons."),
            S("Neutrons", math=r"A - Z = 39 - 19 = 20"),
        ]),
        EX("Worked example 2: an ion", intro="How many protons, neutrons and electrons are in the magnesium ion ²⁴Mg²⁺ (atomic number 12)?", steps=[
            S("Protons", text="12, the atomic number. This does not change when the ion forms."),
            S("Neutrons", math=r"24 - 12 = 12"),
            S("Electrons", text="A neutral Mg atom has 12 electrons. The ion has lost 2 electrons, so 12 − 2 = 10 electrons."),
            S("Check the charge", text="12 positive charges and 10 negative charges give a net 2+. ✓"),
        ]),
        EX("Worked example 3: a negative ion", intro="A particle has 17 protons, 18 neutrons and 18 electrons. Write its symbol and charge.", steps=[
            S("Identify the element", text="17 protons means atomic number 17, which is chlorine."),
            S("Mass number", math=r"17 + 18 = 35"),
            S("Charge", text="Protons 17 and electrons 18. There is one extra electron, so the charge is 1−."),
            S("Symbol", text="The particle is the chloride ion, Cl⁻, of chlorine-35."),
        ]),
        MISTAKE("Using the mass number as the number of protons", "The number of protons is the atomic number, the smaller number. The mass number is protons plus neutrons."),
        MISTAKE("Changing the number of protons to make an ion", "Ions form by gaining or losing electrons only. The number of protons never changes in a chemical reaction."),
        MISTAKE("Forgetting that the charge sign comes from the extra particles", "More protons than electrons means a positive ion. More electrons than protons means a negative ion."),
        QUIZ("An atom has atomic number 13 and mass number 27. How many neutrons does it have?", ["13", "14", "27", "40"], 1,
             "Neutrons = mass number − atomic number = 27 − 13 = 14.",
             hint="Subtract the atomic number from the mass number.",
             feedback=["13 is the number of protons.", "", "27 is the total of protons and neutrons.", "40 adds the two numbers instead of subtracting."]),
        QUIZ("How many electrons are there in the ion O²⁻ (atomic number 8)?", ["6", "8", "10", "16"], 2,
             "A neutral oxygen atom has 8 electrons. The ion has gained 2 electrons, so 8 + 2 = 10.",
             hint="A 2− charge means two extra electrons.",
             feedback=["This takes the 2 electrons away instead of adding them.", "This is the number in the neutral atom.", "", "16 is the mass number."]),
        TIP("These calculations are tested in Paper 1 (multiple choice) and are the base of many Paper 2 Section A questions on atomic structure and bonding. "
            "Draw a small table of protons, neutrons and electrons every time.", title="Exam link"),
        H("Practice questions"),
        PQ("State the relative mass and relative charge of (a) a proton and (b) an electron.", "(a) A proton has relative mass 1 and relative charge +1. (b) An electron has relative mass about 1/1840 (negligible) and relative charge −1."),
        PQ("An atom of fluorine has atomic number 9 and mass number 19. State the number of protons, neutrons and electrons.", "Protons 9, electrons 9, neutrons 19 − 9 = 10."),
        PQ("Calculate the number of protons, neutrons and electrons in the calcium ion ⁴⁰Ca²⁺ (atomic number 20).", "Protons 20. Neutrons 40 − 20 = 20. Electrons 20 − 2 = 18."),
        PQ("Why is an atom electrically neutral?", "It has equal numbers of protons (positive) and electrons (negative), so the charges cancel out."),
        SUM("An atom has a nucleus of protons and neutrons, and electrons in shells. Most of the mass is in the nucleus.",
            "Proton: mass 1, charge +1. Neutron: mass 1, charge 0. Electron: mass about 1/1840, charge −1.",
            "Atomic number = number of protons. Mass number = protons + neutrons. Neutrons = A − Z.",
            "In a neutral atom the number of electrons equals the number of protons.",
            "An ion forms when an atom gains or loses electrons. The protons stay the same."),
    ],
))

# ------------------------------------------------------------------ 7. Isotopes and relative atomic mass
LESSONS.append(lesson(
    module=MODULE,
    topic=ATOM,
    title="Isotopes and relative atomic mass",
    slug="cha-isotopes-relative-atomic-mass",
    minutes=20,
    summary="Isotopes are atoms of the same element with different numbers of neutrons. The relative atomic mass is the average mass of the isotopes, taking their abundance into account.",
    objectives=[
        "Define isotopes and give examples",
        "Explain why isotopes have the same chemical properties but different physical properties",
        "Define relative atomic mass",
        "Calculate relative atomic mass from isotope abundances, and abundances from a relative atomic mass",
    ],
    key_concepts=["Isotope", "Relative atomic mass (Ar)", "Percentage abundance", "Radioactive isotope"],
    blocks=[
        H("Introduction"),
        T("If you look at the periodic table, the mass of chlorine is given as 35.5. But you cannot have half a proton or half a neutron, so no single chlorine atom "
          "has a mass of 35.5. How can the table say that? The answer is isotopes."),
        D("**Isotopes** are atoms of the same element that have the same number of protons (the same atomic number) but different numbers of neutrons (different mass numbers).", title="Definition: isotopes"),
        T("For example, chlorine has two common isotopes. Both have 17 protons. Chlorine-35 has 18 neutrons and chlorine-37 has 20 neutrons."),
        CODE("""Isotope      Protons   Neutrons   Electrons   Mass number
chlorine-35    17        18         17          35
chlorine-37    17        20         17          37

carbon-12       6         6          6          12
carbon-13       6         7          6          13
carbon-14       6         8          6          14""", "text", title="Examples of isotopes"),
        H("Properties of isotopes"),
        KEY("Same or different?", "The properties depend on which part of the atom is involved.", cards=[
            ["Same chemical properties", "Chemical reactions depend on the electrons, and isotopes of an element have the same number of electrons and the same electron arrangement."],
            ["Different physical properties", "Isotopes have different masses. So they have slightly different densities, and lighter isotopes diffuse faster."],
        ]),
        T("Some isotopes are **radioactive**, which means their nuclei are unstable and give out radiation. Carbon-14 is used to estimate the age of "
          "ancient wood and bones. Cobalt-60 is used in hospitals in cancer treatment, and iodine-131 is used for thyroid conditions. Radioactive isotopes must be handled with great care."),
        H("Relative atomic mass"),
        T("A sample of chlorine contains atoms of both Cl-35 and Cl-37. Chemists use an **average** mass of all the atoms in the sample. This average takes into account how much of each isotope there is."),
        D("The **relative atomic mass** (Ar) of an element is the weighted average mass of the atoms of its isotopes, compared with one-twelfth of the mass of an atom of carbon-12.", title="Definition: relative atomic mass"),
        F(r"A_r = \frac{\sum (\text{mass number} \times \text{percentage abundance})}{100}", title="Formula"),
        T("Because it is an average and a comparison, Ar has no unit. It is not usually a whole number when an element has more than one common isotope. "
          "The percentage of each isotope is called its **abundance**, and it is measured with an instrument called a mass spectrometer."),
        T("In this course you will use these values: H = 1, C = 12, N = 14, O = 16, Na = 23, Mg = 24, Cl = 35.5."),
        H("Worked examples"),
        EX("Worked example 1: chlorine", intro="Chlorine has two isotopes: chlorine-35 (75%) and chlorine-37 (25%). Calculate the relative atomic mass.", steps=[
            S("Multiply each mass by its percentage", math=r"35 \times 75 = 2625 \qquad 37 \times 25 = 925"),
            S("Add and divide by 100", math=r"A_r = \frac{2625 + 925}{100} = \frac{3550}{100} = 35.5"),
        ], check=r"\text{The answer lies between 35 and 37, and is nearer 35 because there is more } ^{35}\text{Cl}."),
        EX("Worked example 2: magnesium", intro="Magnesium has three isotopes: Mg-24 (79%), Mg-25 (10%) and Mg-26 (11%). Calculate the relative atomic mass to 1 decimal place.", steps=[
            S("Multiply", math=r"24 \times 79 = 1896 \qquad 25 \times 10 = 250 \qquad 26 \times 11 = 286"),
            S("Add and divide", math=r"A_r = \frac{1896 + 250 + 286}{100} = \frac{2432}{100} = 24.32"),
            S("Round", math=r"A_r = 24.3"),
        ]),
        EX("Worked example 3: finding an abundance", intro="Boron has two isotopes, boron-10 and boron-11. Its relative atomic mass is 10.8. Find the percentage of boron-11.", steps=[
            S("Let x be the percentage of boron-11", text="Then the percentage of boron-10 is 100 − x."),
            S("Set up the equation", math=r"\frac{10(100 - x) + 11x}{100} = 10.8"),
            S("Simplify", math=r"1000 + x = 1080"),
            S("Solve", math=r"x = 80"),
            S("Answer", text="Boron-11 is 80% and boron-10 is 20%."),
        ], check=r"\frac{10 \times 20 + 11 \times 80}{100} = \frac{200 + 880}{100} = 10.8"),
        MISTAKE("Saying isotopes have different numbers of protons or electrons", "Isotopes have the same number of protons and electrons. Only the number of neutrons is different."),
        MISTAKE("Saying isotopes have different chemical properties", "Chemical properties depend on electrons, which are the same. Only physical properties that depend on mass, such as density, are different."),
        MISTAKE("Forgetting to divide by 100", "If the abundances are percentages, divide the total by 100. If they are given as fractions (such as 0.75 and 0.25) do not divide."),
        QUIZ("Which pair of particles are isotopes of the same element?", [
            "6 protons, 6 neutrons and 6 protons, 7 neutrons",
            "6 protons, 6 neutrons and 7 protons, 6 neutrons",
            "6 protons, 6 neutrons and 6 protons, 6 neutrons",
            "6 protons, 6 neutrons and 7 protons, 7 neutrons"], 0,
            "Isotopes have the same number of protons and different numbers of neutrons. Only the first pair does.",
            hint="Compare the numbers of protons first.",
            feedback=["", "Different numbers of protons mean different elements.", "These two are identical, with the same neutron number.", "Different numbers of protons mean different elements."]),
        QUIZ("Neon has two main isotopes, neon-20 (90%) and neon-22 (10%). Which is the relative atomic mass of neon?", ["20", "20.2", "21", "21.8"], 1,
             "Ar = (20 × 90 + 22 × 10) ÷ 100 = (1800 + 220) ÷ 100 = 20.2.",
             hint="Multiply each mass number by its percentage, add and divide by 100.",
             feedback=["This ignores the neon-22 isotope.", "", "This is the simple average of 20 and 22, which ignores abundance.", "This puts too much weight on neon-22."]),
        TIP("Isotope definitions and Ar calculations appear in Paper 1 and in Paper 2 Section A (atomic structure). State that isotopes have the same number of protons "
            "but different numbers of neutrons. Always show the working for an Ar calculation.", title="Exam link"),
        H("Practice questions"),
        PQ("Define the term 'isotopes'.", "Isotopes are atoms of the same element, with the same number of protons but different numbers of neutrons."),
        PQ("Copper has two isotopes: copper-63 (69%) and copper-65 (31%). Calculate the relative atomic mass of copper to 1 decimal place.", "Ar = (63 × 69 + 65 × 31) ÷ 100 = (4347 + 2015) ÷ 100 = 63.62, which is 63.6 to 1 decimal place."),
        PQ("Explain why isotopes of an element have the same chemical properties.", "They have the same number of electrons and so the same electron arrangement. Chemical reactions depend on the electrons."),
        PQ("Bromine consists of two isotopes, bromine-79 and bromine-81, in equal amounts. Calculate its relative atomic mass.", "Ar = (79 × 50 + 81 × 50) ÷ 100 = 80."),
        SUM("Isotopes are atoms of the same element with the same number of protons but different numbers of neutrons.",
            "They have the same chemical properties but different physical properties that depend on mass.",
            "Relative atomic mass is the weighted average mass of an element's isotopes compared with one-twelfth of carbon-12. It has no unit.",
            "Ar = (sum of mass number × percentage abundance) ÷ 100.",
            "Radioactive isotopes have uses in medicine and dating, but must be handled with care."),
    ],
))

# ------------------------------------------------------------------ 8. Electronic configuration and the periodic table
LESSONS.append(lesson(
    module=MODULE,
    topic=CONFIG,
    title="Electronic configuration and the organization of the periodic table",
    slug="cha-electron-configuration-table",
    minutes=22,
    summary="Electrons fill shells in order: 2, 8, 8, then the next shell. The configuration of an atom decides its period, its group and its valency, and so how the periodic table is organized.",
    objectives=[
        "Write the electronic configuration of the first 20 elements",
        "Explain how the periods and groups of the periodic table are linked to electronic configuration",
        "State the period, the group and the valency of an element from its configuration",
        "Describe where metals, non-metals and noble gases are found in the table",
    ],
    key_concepts=["Electron shell", "Electronic configuration", "Outer-shell (valence) electrons", "Period", "Group", "Valency", "Noble gases"],
    blocks=[
        H("Introduction"),
        T("In a library, books are put on shelves by subject so you can find them quickly. The **periodic table** does the same for the elements. "
          "Elements in one column behave in a similar way, just as books on one shelf are about one subject. The reason is the way the electrons are arranged in the atoms."),
        H("Electron shells"),
        D("An **electron shell** (or energy level) is a region around the nucleus where electrons move. Shells are numbered 1, 2, 3 ... outwards from the nucleus. "
          "Shell 1 is closest to the nucleus and has the lowest energy.", title="Definition: electron shell"),
        D("The **electronic configuration** of an atom is the way its electrons are arranged in the shells. It is written as numbers separated by commas, for example 2,8,1 for sodium.", title="Definition: electronic configuration"),
        KEY("The filling rules (up to calcium, Z = 20)", "Electrons go into the lowest shell that has room.", cards=[
            ["Shell 1", "Holds a maximum of 2 electrons."],
            ["Shell 2", "Holds a maximum of 8 electrons. It starts to fill only when shell 1 is full."],
            ["Shell 3", "Fills up to 8 electrons for the first 20 elements. (It can hold more, but the fourth shell begins to fill after 8.)"],
            ["Shell 4", "Receives the 19th and 20th electrons (K and Ca)."],
        ], note="The third shell can hold up to 18 electrons in total. Your syllabus only needs the first 20 elements, so use 2, 8, 8, 2. Check your textbook."),
        IMG("f5ch-a-shells.svg",
            alt="Electron shell diagrams of lithium 2,1; carbon 2,4; oxygen 2,6; neon 2,8; sodium 2,8,1 and chlorine 2,8,7, with the outer shell electrons coloured differently.",
            caption="Figure 1. Electron arrangements of six atoms. The outer-shell electrons are shown in a different colour."),
        CODE("""Z   Element  Configuration   Period  Group
1   H        1               1       I
2   He       2               1       0
3   Li       2,1             2       I
4   Be       2,2             2       II
5   B        2,3             2       III
6   C        2,4             2       IV
7   N        2,5             2       V
8   O        2,6             2       VI
9   F        2,7             2       VII
10  Ne       2,8             2       0
11  Na       2,8,1           3       I
12  Mg       2,8,2           3       II
13  Al       2,8,3           3       III
14  Si       2,8,4           3       IV
15  P        2,8,5           3       V
16  S        2,8,6           3       VI
17  Cl       2,8,7           3       VII
18  Ar       2,8,8           3       0
19  K        2,8,8,1         4       I
20  Ca       2,8,8,2         4       II""", "text", title="The first 20 elements"),
        H("Linking configuration to the periodic table"),
        IMG("f5ch-a-periodic-excerpt.svg",
            alt="The first 20 elements in periods 1 to 4 and groups I to VII and 0, coloured as metals, non-metals and metalloids.",
            caption="Figure 2. The first 20 elements. Rows are periods; columns are groups."),
        D("The **periodic table** arranges the elements in order of increasing atomic number. A horizontal row is a **period** and a vertical column is a **group**.", title="Definition: periodic table"),
        KEY("Two rules that connect configuration to position", "These rules let you place any of the first 20 elements.", cards=[
            ["Period number", "Period number = number of occupied shells. Sodium (2,8,1) has 3 shells, so it is in period 3."],
            ["Group number", "Group number (I to VII) = number of electrons in the outer shell. Sodium has 1 outer electron, so it is in group I. Group 0 has a full outer shell (8, or 2 for helium)."],
        ]),
        T("The electrons in the outer shell are the **outer-shell electrons**, or **valence electrons**. They take part in chemical reactions. "
          "Because elements in the same group have the same number of outer electrons, they have similar chemical properties. "
          "Lithium, sodium and potassium all have one outer electron, and all react in a similar way with water."),
        T("A full outer shell is very stable. The **noble gases** (group 0: helium, neon, argon ...) have full outer shells and hardly react at all."),
        H("Valency and ions"),
        D("**Valency** is the number of electrons an atom gains, loses or shares when it forms compounds. It tells you the combining power of an element.", title="Definition: valency"),
        CODE("""Group            I   II   III   IV   V   VI   VII   0
Outer electrons  1   2    3     4    5   6    7     8 (2 for He)
Valency          1   2    3     4    3   2    1     0""", "text", title="Group and valency"),
        T("Atoms with 1, 2 or 3 outer electrons (metals) lose them and become positive ions: Na → Na⁺, Mg → Mg²⁺, Al → Al³⁺. "
          "Atoms with 5, 6 or 7 outer electrons gain electrons to fill the shell and become negative ions: O → O²⁻, Cl → Cl⁻. "
          "In both cases the ion has the stable configuration of a noble gas."),
        T("In the periodic table, **metals** are on the left and in the middle. **Non-metals** are on the right. A few elements between them, "
          "such as boron and silicon, are metalloids with properties between the two."),
        H("Worked examples"),
        EX("Worked example 1: write a configuration", intro="Write the electronic configuration of phosphorus (atomic number 15) and state its period and group.", steps=[
            S("Fill the shells in order", text="Shell 1: 2. Shell 2: 8. That uses 10 electrons. Shell 3 gets the remaining 15 − 10 = 5."),
            S("Write it", text="Phosphorus is 2,8,5."),
            S("Period", text="Three shells, so period 3."),
            S("Group", text="5 outer electrons, so group V."),
        ]),
        EX("Worked example 2: identify an element", intro="An element has the configuration 2,8,2. Identify it and state its group, period, and the ion it forms.", steps=[
            S("Add the electrons", math=r"2 + 8 + 2 = 12"),
            S("Atomic number 12", text="This is magnesium (Mg)."),
            S("Position", text="Three shells: period 3. Two outer electrons: group II."),
            S("Ion", text="Mg loses its 2 outer electrons to form Mg²⁺ with configuration 2,8 (like neon)."),
        ]),
        EX("Worked example 3: valency", intro="Find the valency of (a) fluorine (atomic number 9) and (b) oxygen (atomic number 8).", steps=[
            S("(a) Fluorine", text="Configuration 2,7. It needs 1 more electron to fill the shell, so the valency is 1 (F⁻)."),
            S("(b) Oxygen", text="Configuration 2,6. It needs 2 more electrons, so the valency is 2 (O²⁻)."),
        ]),
        MISTAKE("Putting more than 8 electrons in shell 2, or filling shell 3 before shell 2", "Fill from the inside out. Shell 2 holds only 8. After 8 electrons in shell 3, the next one goes into shell 4."),
        MISTAKE("Mixing up period and group", "The period is the row and equals the number of shells. The group is the column and equals the number of outer electrons. Sodium 2,8,1 is in period 3, group I."),
        MISTAKE("Giving the valency of chlorine as 7", "Chlorine has 7 outer electrons but needs only 1 more to fill its shell. Its valency is 1. For groups V to VII, valency = 8 minus the number of outer electrons."),
        QUIZ("An atom has the electronic configuration 2,8,4. In which group and period is it?", [
            "Group IV, period 3", "Group III, period 4", "Group IV, period 4", "Group VIII, period 3"], 0,
            "Three shells means period 3. Four outer electrons means group IV. The element is silicon.",
            hint="Count the numbers for the period; the last number gives the group.",
            feedback=["", "This swaps the period and group numbers.", "Three numbers means three shells, so period 3, not 4.", "The group is the number of outer electrons, which is 4."]),
        QUIZ("Why do lithium, sodium and potassium react in a similar way?", [
            "They are all in period 2",
            "They all have one electron in the outer shell",
            "They all have three shells",
            "They all have the same mass"], 1,
            "They are all in group I and have one outer electron. Chemical properties depend on the outer electrons.",
            hint="Think of group and outer electrons.",
            feedback=["They are in periods 2, 3 and 4 respectively.", "", "Lithium has 2 shells, sodium 3 and potassium 4.", "They have different masses."]),
        TIP("Writing configurations and linking them to period, group and valency is tested in Paper 1 and in Paper 2 Section A, where "
            "you may be asked to use a configuration to predict valency, formula or the type of bonding. Always write the full configuration, such as 2,8,1.", title="Exam link"),
        H("Practice questions"),
        PQ("Write the electronic configuration of (a) oxygen (Z = 8) and (b) calcium (Z = 20).", "(a) 2,6. (b) 2,8,8,2."),
        PQ("An element has atomic number 17. Give its configuration, group, period and valency.", "Configuration 2,8,7. Group VII. Period 3. Valency 1."),
        PQ("Explain why neon is very unreactive.", "Neon has the configuration 2,8. Its outer shell is full, which is a very stable arrangement, so its atoms do not need to gain, lose or share electrons."),
        PQ("Sodium and potassium are in the same group. Explain why they have similar chemical properties.", "Both atoms have one electron in the outer shell (2,8,1 and 2,8,8,1). Chemical properties depend on the outer electrons, so they behave similarly."),
        SUM("Electrons fill shells from the inside out: 2, 8, 8, then the fourth shell, up to calcium.",
            "The period number equals the number of occupied shells. The group number equals the number of outer-shell electrons.",
            "Elements in the same group have the same number of outer electrons, so similar chemical properties.",
            "Valency is the number of electrons gained, lost or shared: it is the group number for groups I to IV and 8 minus the group number for groups V to VII.",
            "Metals lose electrons to form positive ions, non-metals gain electrons to form negative ions, and noble gases have full outer shells."),
    ],
))

# ------------------------------------------------------------------ 9. Groups I and II
LESSONS.append(lesson(
    module=MODULE,
    topic=TRENDS,
    title="Group I and Group II metals: properties and trends",
    slug="cha-groups-one-two",
    minutes=20,
    summary="The alkali metals (group I) and the alkaline earth metals (group II) become more reactive as you go down the group. Learn their properties, their reactions with water and oxygen, and the reason for the trend.",
    objectives=[
        "State the physical properties of the group I metals and how they change down the group",
        "Describe and write equations for the reactions of group I metals with water",
        "Describe the reactions of magnesium and calcium with oxygen, water and dilute acid",
        "Explain why reactivity increases down both groups",
    ],
    key_concepts=["Alkali metals", "Alkaline earth metals", "Reactivity trend", "Flame test", "Metal hydroxide"],
    blocks=[
        H("Introduction"),
        T("In a school laboratory, sodium is kept in a bottle of oil. A piece the size of a rice grain is cut with a knife and dropped on water. "
          "It skates across the surface, fizzes and disappears. The same test with potassium is much more violent. Why is one group of metals so reactive, "
          "and why does it get more reactive going down?"),
        H("Group I: the alkali metals"),
        D("The **alkali metals** are the elements of group I: lithium (Li), sodium (Na), potassium (K), and others below them. Each has **one electron in its outer shell** and forms a **+1 ion**, for example Na⁺.", title="Definition: alkali metals"),
        KEY("Physical properties of group I", "They are unlike most other metals.", cards=[
            ["Soft", "They can be cut with a knife. They are shiny when cut but quickly tarnish in air."],
            ["Low density", "Lithium, sodium and potassium are less dense than water and float on it."],
            ["Low melting points", "Much lower than most metals. The melting point falls as you go down the group."],
            ["Good conductors", "They conduct electricity and heat, like all metals."],
        ]),
        CODE("""Metal        Melting point (approx.)   Flame colour
Lithium      181 C                     red
Sodium        98 C                     golden yellow
Potassium     63 C                     lilac""", "text", title="Group I data"),
        T("Because they react so easily with air and water, lithium, sodium and potassium are stored under oil."),
        H("Reactions of group I metals with water"),
        T("Group I metals react with cold water. They make hydrogen gas and a solution of the metal hydroxide, which is an alkali. This is why they are called alkali metals. "
          "The general equation is: metal + water → metal hydroxide + hydrogen."),
        CODE("""2Li + 2H2O -> 2LiOH + H2
2Na + 2H2O -> 2NaOH + H2
2K  + 2H2O -> 2KOH  + H2""", "text", title="Equations (all balanced)"),
        KEY("What you see", "The reaction gets more vigorous down the group.", cards=[
            ["Lithium", "Floats, fizzes steadily and moves slowly. It does not melt."],
            ["Sodium", "Floats, melts into a ball, fizzes and moves quickly over the surface."],
            ["Potassium", "Melts, moves very fast and the hydrogen burns with a lilac flame. Sometimes it explodes."],
        ], note="After the reaction, universal indicator in the solution turns purple, showing a strong alkali. Hydrogen gives a squeaky pop with a lighted splint."),
        T("Group I metals also react with chlorine to form white solid chlorides: 2Na + Cl₂ → 2NaCl. All group I compounds are white solids that dissolve in water to give colourless solutions."),
        H("Group II: the alkaline earth metals"),
        D("The **alkaline earth metals** are the elements of group II: beryllium, magnesium (Mg), calcium (Ca) and others below them. Each has **two electrons in its outer shell** and forms a **2+ ion**, for example Mg²⁺.", title="Definition: alkaline earth metals"),
        T("Group II metals are harder and denser than group I metals, and they have higher melting points. They are less reactive than the group I metal in the same period, "
          "but their reactivity also increases down the group."),
        KEY("Reactions of magnesium and calcium", "Compare the two metals.", cards=[
            ["With oxygen", "Magnesium burns in air with a bright white flame and leaves white magnesium oxide: 2Mg + O₂ → 2MgO."],
            ["With cold water", "Magnesium reacts very slowly. Calcium reacts steadily with bubbles of hydrogen, forming cloudy calcium hydroxide solution: Ca + 2H₂O → Ca(OH)₂ + H₂."],
            ["With steam", "Hot magnesium reacts with steam to give magnesium oxide and hydrogen: Mg + H₂O → MgO + H₂."],
            ["With dilute acid", "Both fizz and release hydrogen: Mg + 2HCl → MgCl₂ + H₂. Calcium reacts much faster than magnesium."],
        ]),
        H("Why does reactivity increase down the group?"),
        T("In a reaction the metal atom **loses** its outer electrons. The easier it is to lose them, the more reactive the metal. Going down a group:"),
        KEY("Reason for the trend", "Say this in three short steps.", cards=[
            ["1. More shells", "The atoms have more electron shells, so the outer electrons are farther from the nucleus."],
            ["2. Weaker attraction", "The attraction of the nucleus for the outer electrons is weaker, partly because the inner shells shield them."],
            ["3. Easier loss", "The outer electrons are lost more easily, so the metal is more reactive."],
        ]),
        H("Worked examples"),
        EX("Worked example 1: predict a reaction", intro="Predict what happens when potassium is added to water and write the balanced equation.", steps=[
            S("Products", text="Potassium hydroxide (an alkali) and hydrogen gas."),
            S("Word equation", text="potassium + water → potassium hydroxide + hydrogen"),
            S("Symbol equation", math=r"2\text{K} + 2\text{H}_2\text{O} \rightarrow 2\text{KOH} + \text{H}_2"),
            S("Observations", text="It floats, melts, moves very fast over the water and the hydrogen burns with a lilac flame. Universal indicator turns purple."),
        ], check=r"\text{K: } 2 = 2;\ \text{H: } 4 = 2 + 2;\ \text{O: } 2 = 2"),
        EX("Worked example 2: explain the trend", intro="Explain why potassium is more reactive than sodium.", steps=[
            S("Compare the atoms", text="Sodium is 2,8,1 (three shells). Potassium is 2,8,8,1 (four shells)."),
            S("Outer electron", text="Potassium's outer electron is farther from the nucleus and more shielded, so it is held less strongly."),
            S("Conclusion", text="It is lost more easily, so potassium is more reactive."),
        ]),
        EX("Worked example 3: calcium and acid", intro="Write the equation for calcium and dilute hydrochloric acid and say how the reaction compares with magnesium.", steps=[
            S("Products", text="Calcium chloride and hydrogen."),
            S("Equation", math=r"\text{Ca} + 2\text{HCl} \rightarrow \text{CaCl}_2 + \text{H}_2"),
            S("Compare", text="Calcium is below magnesium in group II, so the reaction is faster and more vigorous."),
        ]),
        MISTAKE("Giving the wrong reason why sodium melts on water", "Sodium melts because the reaction gives out heat and its melting point is low (98 °C). The water itself does not need to be hot."),
        MISTAKE("Explaining the trend with 'bigger atoms are more reactive' only", "State that the outer electron is farther from the nucleus and shielded, so it is held less strongly and lost more easily."),
        MISTAKE("Unbalanced equations for group I metals and water", "The metal and water always react 1 : 1 in the form 2M + 2H₂O. Remember that two metal atoms are needed to make one H₂ molecule."),
        QUIZ("Which gas is produced when sodium reacts with water?", ["Oxygen", "Hydrogen", "Carbon dioxide", "Chlorine"], 1,
             "Sodium and water give sodium hydroxide and hydrogen gas. Hydrogen burns with a squeaky pop.",
             hint="Think of the equation 2Na + 2H₂O → 2NaOH + ?",
             feedback=["No oxygen is released. The oxygen stays in the hydroxide.", "", "There is no carbon in either reactant.", "There is no chlorine in either reactant."]),
        QUIZ("Which statement correctly describes the trend in group I as you go down from lithium to potassium?", [
            "Reactivity decreases", "Melting point increases", "Reactivity increases", "The number of outer electrons increases"], 2,
            "Reactivity increases down group I, because the outer electron is lost more easily. The melting point decreases, and all group I atoms have one outer electron.",
            hint="Compare how violently lithium and potassium react with water.",
            feedback=["Potassium is more reactive than lithium.", "The melting point falls down the group.", "", "Every group I atom has exactly one outer electron."]),
        TIP("Group I and group II properties and trends appear in Paper 1 and in Paper 2 Section A (periodic classification and families of elements). "
            "Be ready to write balanced equations and to explain a trend using the outer electrons and the number of shells.", title="Exam link"),
        H("Practice questions"),
        PQ("State two physical properties of sodium that are different from those of iron.", "Sodium is soft (cut with a knife), has a low density (floats on water) and a low melting point (98 °C). Iron is hard, dense and has a high melting point."),
        PQ("Write a balanced equation for the reaction of lithium with water.", "2Li + 2H₂O → 2LiOH + H₂."),
        PQ("Describe what is seen when magnesium ribbon burns in air, and name the product.", "It burns with a bright white flame. A white powder, magnesium oxide, is formed."),
        PQ("Explain why calcium is more reactive than magnesium.", "Calcium has more electron shells. Its two outer electrons are farther from the nucleus and more shielded, so they are lost more easily."),
        SUM("Group I metals have one outer electron. They are soft, low in density and melting point, and stored under oil.",
            "They react with water to give a metal hydroxide (alkali) and hydrogen: 2Na + 2H₂O → 2NaOH + H₂. Lithium red, sodium yellow, potassium lilac in a flame.",
            "Group II metals have two outer electrons and form 2+ ions. Magnesium burns with a white flame; calcium reacts with cold water.",
            "Reactivity increases down both groups.",
            "The reason is that the outer electrons are farther from the nucleus and more shielded, so they are lost more easily."),
    ],
))

# ------------------------------------------------------------------ 10. Halogens, noble gases, transition metals
LESSONS.append(lesson(
    module=MODULE,
    topic=TRENDS,
    title="The halogens, the noble gases and the transition metals",
    slug="cha-halogens-noble-transition",
    minutes=22,
    summary="The halogens (group VII) get less reactive down the group and displace one another from solutions. The noble gases (group 0) are unreactive. The transition metals are hard, dense, coloured and good catalysts.",
    objectives=[
        "State the colour, state and trends in properties of the halogens",
        "Use displacement reactions to compare the reactivity of halogens and write the equations",
        "Explain why the noble gases are unreactive and state their uses",
        "State the general properties of the transition metals and compare them with group I metals",
    ],
    key_concepts=["Halogens", "Displacement reaction", "Noble gases", "Transition metals", "Catalyst"],
    blocks=[
        H("Introduction"),
        T("Chlorine is added to the water supply to kill germs. Iron, a transition metal, is used for roofing sheets and cooking pots. Argon, a noble gas, fills "
          "some electric bulbs. These three kinds of element sit in different parts of the periodic table, and their properties follow from their electron arrangements."),
        H("Group VII: the halogens"),
        D("The **halogens** are the elements of group VII: fluorine (F), chlorine (Cl), bromine (Br) and iodine (I), and others below. Each atom has **seven electrons in its outer shell** and "
          "forms a **1− ion** (for example Cl⁻) by gaining one electron. Their molecules are **diatomic**: F₂, Cl₂, Br₂, I₂.", title="Definition: halogens"),
        CODE("""Halogen    State at room temp    Colour
Fluorine   gas                   pale yellow
Chlorine   gas                   pale yellow-green
Bromine    liquid                red-brown (orange-brown vapour)
Iodine     solid                 grey-black (purple vapour)""", "text", title="Halogens at room temperature"),
        KEY("Trends down group VII", "Fluorine is at the top; iodine is near the bottom.", cards=[
            ["Colour", "Gets darker: pale yellow, yellow-green, red-brown, grey-black."],
            ["Melting and boiling points", "Increase down the group, so the state changes from gas to liquid to solid."],
            ["Reactivity", "Decreases down the group. Fluorine is the most reactive halogen; iodine is the least reactive."],
        ]),
        T("Halogens react with metals to form ionic salts called halides: 2Na + Cl₂ → 2NaCl, and with iron wool, 2Fe + 3Cl₂ → 2FeCl₃. They react with hydrogen to give hydrogen halides: H₂ + Cl₂ → 2HCl. "
          "Chlorine is toxic. It must be used in a fume cupboard or a well-ventilated place."),
        H("Displacement reactions"),
        D("In a **displacement reaction**, a more reactive halogen takes the place of a less reactive halogen in a solution of its halide salt.", title="Definition: displacement reaction"),
        T("Chlorine water is added to potassium bromide solution. The colourless solution turns orange-brown as bromine forms. Chlorine is more reactive than bromine, so it displaces it."),
        CODE("""Cl2 + 2KBr -> 2KCl + Br2      (orange-brown solution)
Cl2 + 2KI  -> 2KCl + I2       (brown solution, black solid may form)
Br2 + 2KI  -> 2KBr + I2       (brown solution)
Br2 + KCl  -> no reaction     (bromine is less reactive than chlorine)
I2 + KBr   -> no reaction""", "text", title="Displacement reactions"),
        T("In ionic form, the reaction of chlorine with bromide ions is Cl₂ + 2Br⁻ → 2Cl⁻ + Br₂. Chlorine gains electrons (it is reduced) and bromide ions lose electrons (they are oxidized)."),
        T("**Why does reactivity fall down the group?** A halogen atom reacts by **gaining** one electron. Going down the group the outer shell is farther from the nucleus and more shielded, "
          "so the nucleus attracts the incoming electron less strongly. It is harder to gain an electron, so the halogen is less reactive."),
        H("Group 0: the noble gases"),
        D("The **noble gases** are the elements of group 0: helium (He), neon (Ne), argon (Ar), krypton (Kr), xenon (Xe) and radon (Rn). They have a **full outer shell** (2 electrons for helium, 8 for the others), "
          "so they are very unreactive. They exist as single atoms (monatomic gases).", title="Definition: noble gases"),
        KEY("Uses of noble gases", "Their uses depend on being unreactive or very light.", cards=[
            ["Helium", "Fills balloons and airships. It is much less dense than air and does not burn."],
            ["Neon", "Gives a bright red-orange glow in advertising signs."],
            ["Argon", "Fills filament lamps. It stops the hot metal filament from reacting with oxygen. Also used as a shield gas in welding."],
        ]),
        H("The transition metals"),
        D("The **transition metals** are the block of metals between group II and group III of the periodic table, for example iron (Fe), copper (Cu), nickel (Ni), manganese (Mn) and chromium (Cr).", title="Definition: transition metals"),
        CODE("""Property              Group I metals          Transition metals
Hardness              soft                    hard and strong
Density               low (float on water)    high (sink in water)
Melting point         low                     high (Fe 1538 C, Cu 1085 C)
Reaction with water   very vigorous           none, or very slow
Compounds             white, colourless soln  often coloured
Catalyst              not used                often good catalysts
Ions                  one charge (Na+)        often more than one (Fe2+, Fe3+)""", "text", title="Group I metals compared with transition metals"),
        KEY("Special features of transition metals", "These set them apart from the other metals.", cards=[
            ["Coloured compounds", "Copper(II) compounds are blue, iron(II) compounds are pale green and iron(III) compounds are yellow-brown."],
            ["More than one ion", "Iron forms Fe²⁺ and Fe³⁺. Copper forms Cu²⁺ (and Cu⁺). The Roman numeral in the name gives the charge: iron(III) means Fe³⁺."],
            ["Catalysts", "Iron is the catalyst in the Haber process for ammonia, vanadium(V) oxide in the Contact process for sulfuric acid and nickel in the hydrogenation of alkenes."],
        ], note="Some books treat zinc differently from the other transition metals. Check your textbook."),
        H("Worked examples"),
        EX("Worked example 1: will a reaction occur?", intro="Chlorine water is added to sodium iodide solution. Will a reaction occur? Write the equation and say what is seen.", steps=[
            S("Compare reactivity", text="Chlorine is above iodine in group VII, so it is more reactive."),
            S("Prediction", text="Chlorine displaces iodine. A reaction occurs."),
            S("Equation", math=r"\text{Cl}_2 + 2\text{NaI} \rightarrow 2\text{NaCl} + \text{I}_2"),
            S("Observation", text="The colourless solution turns brown as iodine forms."),
        ]),
        EX("Worked example 2: no reaction", intro="Iodine solution is added to potassium chloride solution. What happens?", steps=[
            S("Compare reactivity", text="Iodine is below chlorine in group VII, so it is less reactive."),
            S("Conclusion", text="A less reactive halogen cannot displace a more reactive one. There is no reaction, and the brown colour of the iodine solution remains."),
        ]),
        EX("Worked example 3: noble gas use", intro="Explain why argon is used to fill a filament lamp.", steps=[
            S("Why is argon unreactive?", text="Its outer shell is full (2,8,8), so it does not react."),
            S("What does the filament need?", text="The tungsten filament gets very hot. In air, it would react with oxygen and burn away."),
            S("Conclusion", text="Argon surrounds the filament and does not react with it, so the filament lasts longer."),
        ]),
        MISTAKE("Saying reactivity increases down group VII", "Group VII is the opposite of group I. Fluorine is the most reactive halogen and the reactivity decreases down the group."),
        MISTAKE("Forgetting that the halogens are diatomic", "Chlorine is Cl₂, not Cl, in equations. Write F₂, Cl₂, Br₂ and I₂."),
        MISTAKE("Saying the noble gases do not react because they have eight outer electrons", "Helium has only two. Say the noble gases have a full outer shell (two for helium, eight for the others)."),
        QUIZ("Bromine water is added to potassium iodide solution. Which statement is correct?", [
            "No reaction occurs",
            "Iodine is displaced and the solution turns brown",
            "Chlorine is displaced",
            "Potassium is displaced"], 1,
            "Bromine is more reactive than iodine, so it displaces iodine from potassium iodide: Br₂ + 2KI → 2KBr + I₂. Iodine makes the solution brown.",
            hint="Compare the positions of bromine and iodine in group VII.",
            feedback=["Bromine is above iodine, so there is a displacement.", "", "There is no chlorine in the reaction.", "The halogens displace halogens, not metals."]),
        QUIZ("Which property is typical of transition metals but not of group I metals?", [
            "Soft and low density", "They form coloured compounds", "They react violently with water", "They form only 1+ ions"], 1,
            "Transition metals often form coloured compounds. Group I metals are soft, light, react violently with water and form only 1+ ions.",
            hint="Think of the blue colour of copper(II) sulfate.",
            feedback=["These are group I properties.", "", "Transition metals react very slowly, if at all.", "Transition metals often have more than one ion."]),
        TIP("This topic is asked in Paper 1 (colours, trends, uses) and Paper 2 Section A (periodic classification and families of elements). Give the trend and the "
            "reason, and write balanced equations with diatomic halogen molecules.", title="Exam link"),
        H("Practice questions"),
        PQ("State the colour and physical state of (a) chlorine and (b) iodine at room temperature.", "(a) Chlorine is a pale yellow-green gas. (b) Iodine is a grey-black solid."),
        PQ("Chlorine water is added to potassium bromide solution. State what is seen and write the equation.", "The colourless solution turns orange-brown because bromine is displaced. Cl₂ + 2KBr → 2KCl + Br₂."),
        PQ("Explain why the noble gases are unreactive.", "They have full outer shells (2 electrons for helium, 8 for the others). They have no tendency to gain, lose or share electrons."),
        PQ("State three ways in which iron differs from sodium.", "Iron is harder and stronger, has a much higher density and melting point, and reacts much less (or not at all) with water. Iron forms coloured compounds and ions with more than one charge, and can act as a catalyst."),
        SUM("Halogens have seven outer electrons, exist as diatomic molecules, and get darker with higher melting points down the group.",
            "Halogen reactivity decreases down the group. A more reactive halogen displaces a less reactive one from its halide solution.",
            "Noble gases have full outer shells, so they are unreactive and monatomic. Helium, neon and argon have everyday uses.",
            "Transition metals are hard, dense, with high melting points; they form coloured compounds, ions with more than one charge, and many are catalysts.",
            "Transition metals are much less reactive with water than group I metals."),
    ],
))

# ------------------------------------------------------------------ 11. Ionic and metallic bonding
LESSONS.append(lesson(
    module=MODULE,
    topic=BOND,
    title="Ionic bonding and metallic bonding",
    slug="cha-ionic-metallic-bonding",
    minutes=22,
    summary="Ionic bonds hold ions together after a metal gives electrons to a non-metal. Metallic bonds hold metal ions together in a sea of free electrons. Learn the dot-and-cross diagrams and how to write ionic formulae.",
    objectives=[
        "Explain why atoms form bonds in terms of full outer shells",
        "Describe ionic bonding and draw dot-and-cross diagrams for NaCl, MgO and MgCl₂",
        "Write the formula of an ionic compound from the charges of its ions",
        "Describe metallic bonding and use it to explain conduction and malleability",
    ],
    key_concepts=["Chemical bond", "Ionic bond", "Dot-and-cross diagram", "Ionic formula", "Metallic bond", "Delocalized electrons"],
    blocks=[
        H("Introduction"),
        T("Table salt is made of sodium and chlorine. Sodium is a soft, reactive metal that burns in water. Chlorine is a poisonous gas. But when they join, "
          "they make the safe salt you cook with. What joins them is a **chemical bond**."),
        D("A **chemical bond** is the force of attraction that holds atoms or ions together in a substance. Atoms form bonds to reach a **full outer shell** of electrons, like a noble gas.", title="Definition: chemical bond"),
        T("There are three main kinds of strong bond: ionic, covalent and metallic. In this lesson you will study ionic and metallic bonding."),
        H("Ionic bonding"),
        D("An **ionic bond** is the strong electrostatic attraction between positive and negative ions. It forms when a **metal atom transfers** one or more electrons to a **non-metal atom**.", title="Definition: ionic bond"),
        T("Look at sodium (2,8,1) and chlorine (2,8,7). Sodium has just one outer electron. Chlorine is one electron short of a full outer shell. "
          "Sodium gives its outer electron to chlorine. Sodium becomes Na⁺ (2,8) and chlorine becomes Cl⁻ (2,8,8). The two oppositely charged ions attract each other."),
        IMG("f5ch-a-dot-cross-ionic.svg",
            alt="Dot-and-cross diagrams. Top: a sodium atom gives one electron to a chlorine atom, giving Na+ and Cl- ions in square brackets. Bottom: a magnesium atom gives two electrons to an oxygen atom, giving Mg2+ and O2- ions.",
            caption="Figure 1. Ionic bonding in sodium chloride and magnesium oxide. Only outer-shell electrons are drawn."),
        KEY("How to draw a dot-and-cross diagram for an ionic compound", "Follow the steps in this order.", cards=[
            ["1", "Draw the outer shell of each atom. Use crosses for the electrons of the metal and dots for the non-metal."],
            ["2", "Show the electron(s) moving from the metal atom to the non-metal atom."],
            ["3", "Draw each ion in square brackets with its charge at the top right. The metal ion has lost its outer shell, and the non-metal ion has a full outer shell of 8."],
        ]),
        T("Ionic bonds usually form between **metals** (groups I, II, III) and **non-metals** (groups V, VI, VII). Metals lose electrons to form positive ions. Non-metals gain electrons to form negative ions."),
        H("Writing ionic formulae"),
        T("An ionic compound has no overall charge. The total positive charge equals the total negative charge. Use the charges of the ions to write the formula."),
        CODE("""Common ions
Positive:  Na+   K+   Ag+   Mg2+   Ca2+   Zn2+   Cu2+   Fe2+   Al3+   Fe3+
Negative:  Cl-   Br-  F-    O2-    S2-    OH-    NO3-   CO3(2-)   SO4(2-)""", "text", title="Common ions"),
        EX("Worked example: writing a formula from charges", intro="Write the formula of aluminium oxide.", steps=[
            S("Write the ions", text="Aluminium forms Al³⁺ and oxygen forms O²⁻."),
            S("Find the lowest common charge", math=r"2 \times (3+) = 6+ \qquad 3 \times (2-) = 6-"),
            S("Use 2 Al and 3 O", text="The formula is Al₂O₃."),
            S("Check", text="Total charge = 6+ and 6−, which cancel to zero. ✓"),
        ]),
        H("Metallic bonding"),
        D("A **metallic bond** is the strong attraction between the positive metal ions and the sea of **delocalized electrons** that move freely through the whole metal.", title="Definition: metallic bond"),
        T("A metal atom loses its outer electrons easily. In a piece of metal the atoms become positive ions arranged in a regular lattice. The outer electrons are no longer held by one atom. "
          "They form a **sea of electrons** that move freely between the ions and hold them together."),
        IMG("f5ch-a-metallic.svg",
            alt="Rows of positive metal ions in a regular lattice surrounded by small free electrons.",
            caption="Figure 2. Metallic bonding: positive ions in a sea of delocalized electrons."),
        KEY("Properties of metals explained by metallic bonding", "Each property follows from the free electrons.", cards=[
            ["Conduct electricity and heat", "The delocalized electrons are free to move and carry charge and energy."],
            ["Malleable and ductile", "The layers of ions can slide over each other without breaking the bond, because the electrons still hold the ions together."],
            ["High melting point and strong", "The attraction between the positive ions and the electron sea is strong and needs much energy to overcome."],
        ]),
        H("Worked examples"),
        EX("Worked example 1: magnesium chloride", intro="Show by a dot-and-cross description how magnesium (2,8,2) and chlorine (2,8,7) form magnesium chloride.", steps=[
            S("Count the electrons to transfer", text="Mg has 2 outer electrons to lose. Each Cl needs 1 electron."),
            S("Number of atoms", text="Two chlorine atoms are needed to take the two electrons, one each."),
            S("Ions formed", text="Mg²⁺ (2,8) and two Cl⁻ (2,8,8 each)."),
            S("Formula", text="MgCl₂. Charge check: 2+ and 2 × 1− = 2−. ✓"),
        ]),
        EX("Worked example 2: write a formula", intro="Write the formula of calcium nitrate, using Ca²⁺ and NO₃⁻.", steps=[
            S("Balance the charges", text="One Ca²⁺ has 2+. Two NO₃⁻ ions have 2−."),
            S("Write the formula", text="Put brackets round the group when you need more than one: Ca(NO₃)₂."),
        ]),
        EX("Worked example 3: why copper wire conducts", intro="Explain why copper conducts electricity but copper(II) oxide does not when solid.", steps=[
            S("Copper", text="Copper has delocalized electrons that are free to move through the metal. They carry the charge."),
            S("Copper(II) oxide", text="In the solid, the ions are held in fixed positions in a lattice. There are no free electrons or free ions, so no charge can move."),
        ]),
        MISTAKE("Showing electrons shared in an ionic compound", "In ionic bonding the electrons are transferred from one atom to the other, not shared. Draw arrows, and show ions in brackets with charges."),
        MISTAKE("Forgetting the brackets and charges on ions", "A dot-and-cross diagram of an ionic compound must show each ion in square brackets with its charge at the top right."),
        MISTAKE("Writing the formula of aluminium oxide as AlO", "The charges Al³⁺ and O²⁻ do not cancel in a 1 : 1 ratio. You need Al₂O₃ so that 6+ balances 6−."),
        QUIZ("What happens to the electrons when sodium reacts with chlorine to form sodium chloride?", [
            "They are shared equally between the atoms",
            "Sodium transfers one electron to chlorine",
            "Chlorine transfers one electron to sodium",
            "They are lost from the compound"], 1,
            "Sodium (a metal) gives its one outer electron to chlorine (a non-metal). This forms Na⁺ and Cl⁻ ions, which attract each other.",
            hint="Which atom is a metal?",
            feedback=["Sharing is covalent bonding.", "", "Chlorine needs electrons. It does not give them away.", "The electrons are not lost. They are transferred."]),
        QUIZ("Which is the correct formula for magnesium oxide, formed from Mg²⁺ and O²⁻?", ["Mg₂O", "MgO₂", "MgO", "Mg₂O₂"], 2,
             "The charges 2+ and 2− cancel in a 1 : 1 ratio, so the formula is MgO.",
             hint="Compare the sizes of the two charges.",
             feedback=["That would be 4+ and 2−.", "That would be 2+ and 4−.", "", "This is a multiple of the formula and is not written in its simplest form."]),
        TIP("The ionic bonding, dot-and-cross diagrams and formulae are in both Paper 1 and Paper 2 Section A. The Board's report says candidates need to apply the electronic configuration to find "
            "valency, write formulae, and predict the type of bond. Practice using configurations to explain.", title="Exam link"),
        H("Practice questions"),
        PQ("Describe, in terms of electrons, how the ionic bond in lithium fluoride forms.", "A lithium atom (2,1) loses its one outer electron to a fluorine atom (2,7). The lithium forms Li⁺ (2) and the fluorine forms F⁻ (2,8). The oppositely charged ions attract each other strongly."),
        PQ("Write the formulae of (a) sodium oxide (b) calcium chloride (c) aluminium chloride.", "(a) Na₂O (b) CaCl₂ (c) AlCl₃."),
        PQ("Explain why metals can be hammered into shape without breaking.", "The layers of positive ions can slide over each other. The delocalized electrons still hold the ions together in the new positions, so the metallic bond is not broken."),
        PQ("State the type of bonding in (a) potassium bromide and (b) zinc.", "(a) Ionic bonding. (b) Metallic bonding."),
        SUM("Atoms bond to reach a full outer shell. An ionic bond is the attraction between oppositely charged ions after electrons transfer from a metal to a non-metal.",
            "In a dot-and-cross diagram of an ionic compound, draw ions in brackets with charges.",
            "The formula of an ionic compound makes the total positive and negative charges equal: Al³⁺ and O²⁻ give Al₂O₃.",
            "A metallic bond is the attraction between positive metal ions and a sea of delocalized electrons.",
            "Free electrons explain conduction, and sliding layers explain malleability."),
    ],
))

# ------------------------------------------------------------------ 12. Covalent and dative bonding
LESSONS.append(lesson(
    module=MODULE,
    topic=BOND,
    title="Covalent bonding and dative covalent bonding",
    slug="cha-covalent-dative-bonding",
    minutes=22,
    summary="A covalent bond is a shared pair of electrons between non-metal atoms. A dative bond is a shared pair where both electrons come from one atom. Draw dot-and-cross diagrams for common molecules and for the ammonium ion.",
    objectives=[
        "Define a covalent bond and explain how it gives each atom a full outer shell",
        "Draw dot-and-cross diagrams for H₂, Cl₂, H₂O, NH₃, CH₄, CO₂ and N₂",
        "Distinguish single, double and triple bonds and lone pairs",
        "Describe dative covalent bonding using the ammonium ion",
    ],
    key_concepts=["Covalent bond", "Shared pair", "Lone pair", "Double and triple bond", "Dative (coordinate) bond", "Molecule"],
    blocks=[
        H("Introduction"),
        T("The water you drink, the oxygen you breathe and the cooking gas in a bottle are all made of **molecules**. In a molecule, atoms are not holding on "
          "by giving and taking electrons as in salt. They **share** electrons. This sharing is called covalent bonding."),
        D("A **covalent bond** is a shared pair of electrons between two atoms. It forms between **non-metal atoms**. Each atom provides one electron to the pair, and the shared pair is attracted by both nuclei.", title="Definition: covalent bond"),
        D("A **molecule** is a group of atoms joined by covalent bonds. Examples: hydrogen H₂, water H₂O, methane CH₄.", title="Definition: molecule"),
        T("Atoms share electrons so that each atom in the molecule has a **full outer shell**: 8 electrons, or 2 for hydrogen."),
        H("Drawing covalent molecules"),
        IMG("f5ch-a-dot-cross-covalent.svg",
            alt="Dot-and-cross diagrams of water, methane, carbon dioxide and nitrogen with overlapping outer shells, showing shared pairs in the overlap and lone pairs on the outer sides.",
            caption="Figure 1. Dot-and-cross diagrams of H₂O, CH₄, CO₂ and N₂. Shared pairs are in the overlap; lone pairs are on the outside."),
        KEY("Words for dot-and-cross diagrams", "Learn these terms.", cards=[
            ["Bonding (shared) pair", "A pair of electrons shared between two atoms. Written as a line in a structural formula."],
            ["Lone pair", "A pair of outer electrons on one atom that is not shared."],
            ["Single bond", "One shared pair: H–H, H–Cl."],
            ["Double bond", "Two shared pairs: O=O, O=C=O."],
            ["Triple bond", "Three shared pairs: N≡N."],
        ]),
        CODE("""Molecule   Outer electrons used          Structural formula
H2         each H shares 1 pair          H-H
Cl2        1 shared pair, 3 lone pairs   Cl-Cl   (lone pairs on each Cl)
HCl        1 shared pair                 H-Cl
H2O        2 shared pairs, 2 lone pairs  H-O-H   (lone pairs on O)
NH3        3 shared pairs, 1 lone pair   N bonded to 3 H (lone pair on N)
CH4        4 shared pairs                C with 4 H
CO2        2 double bonds                O=C=O
N2         1 triple bond                 N≡N
O2         1 double bond                 O=O""", "text", title="Common molecules"),
        T("To draw a molecule, start with the central atom. Work out how many electrons each atom needs. Place shared pairs in the overlap of the circles, using dots for one atom's electrons and crosses for the other's. "
          "Then draw any lone pairs. Finally check that each atom has a full outer shell."),
        H("Count the electrons"),
        T("Check your drawing by counting. Water: oxygen has 6 outer electrons and each hydrogen has 1, so the total is 6 + 1 + 1 = 8, which is four pairs. "
          "Two pairs are shared (the two O–H bonds) and two are lone pairs on oxygen. Oxygen then has 4 + 2 + 2 = 8 electrons around it, and each hydrogen has 2."),
        H("Dative (coordinate) covalent bonding"),
        D("A **dative covalent bond** (also called a **coordinate bond**) is a covalent bond in which **both electrons of the shared pair come from one atom**. The other atom provides an empty space for them.", title="Definition: dative covalent bond"),
        T("The ammonium ion NH₄⁺ forms when an ammonia molecule uses the **lone pair** on its nitrogen atom to bond to a hydrogen ion H⁺. The hydrogen ion has no electrons at all. It receives both electrons from nitrogen."),
        IMG("f5ch-a-dative.svg",
            alt="An ammonia molecule with a lone pair on nitrogen joins a hydrogen ion with no electrons to form the ammonium ion with four bonds, one of them labelled dative.",
            caption="Figure 2. The dative bond in the ammonium ion, NH₄⁺. Both electrons of one N–H bond come from nitrogen."),
        T("Once formed, a dative bond is no different from other covalent bonds. In NH₄⁺, all four N–H bonds are identical. The oxonium ion H₃O⁺, formed when a water molecule uses a lone pair to bond to H⁺, is another example. "
          "The dative bond is often drawn as an arrow from the atom that gives the pair."),
        H("Ionic and covalent bonding compared"),
        CODE("""                  Ionic bonding            Covalent bonding
Between           metal and non-metal      non-metal and non-metal
Electrons         transferred              shared
Particles         ions                     molecules (usually)
Force             attraction of ions       shared pair held by nuclei""", "text", title="Ionic and covalent bonding"),
        H("Worked examples"),
        EX("Worked example 1: ammonia", intro="Describe the bonding in ammonia, NH₃, using the electron configurations.", steps=[
            S("Count the outer electrons", text="N (2,5) has 5 outer electrons. Each H has 1."),
            S("What N needs", text="N needs 3 more electrons for a full shell of 8. It shares one pair with each of 3 hydrogen atoms."),
            S("Lone pair", text="N used 3 of its 5 electrons for sharing, leaving 2, which form one lone pair."),
            S("Check", text="N has 3 shared pairs and 1 lone pair = 8 electrons. Each H has 2. ✓"),
        ]),
        EX("Worked example 2: carbon dioxide", intro="Explain why carbon dioxide, CO₂, has two double bonds.", steps=[
            S("Carbon", text="C (2,4) has 4 outer electrons and needs 4 more."),
            S("Oxygen", text="Each O (2,6) needs 2 more electrons."),
            S("Share", text="Carbon shares 2 electrons with each oxygen atom. This is 2 shared pairs, a double bond, on each side."),
            S("Check", text="Carbon has 4 shared pairs = 8 electrons. Each oxygen has 2 shared pairs and 2 lone pairs = 8 electrons. ✓"),
        ]),
        EX("Worked example 3: dative bond", intro="Explain how a dative bond is formed in the ammonium ion.", steps=[
            S("The donor", text="Ammonia has a lone pair on the nitrogen atom."),
            S("The acceptor", text="The hydrogen ion H⁺ has no electrons and an empty first shell."),
            S("Bond", text="Nitrogen donates both electrons of its lone pair to form a shared pair with H⁺. This is a dative covalent bond."),
            S("Result", text="NH₄⁺ has 4 N–H bonds, one of which was formed by the dative bond. They are all the same."),
        ]),
        MISTAKE("Forgetting that a shared pair counts for both atoms", "In a dot-and-cross diagram each atom should end with 8 outer electrons (2 for H). Count the shared pairs for both atoms, together with the lone pairs."),
        MISTAKE("Calling a dative bond a weaker bond", "A dative bond differs only in where the electrons came from. Once formed it is as strong as any other covalent bond. In NH₄⁺ all four bonds are identical."),
        MISTAKE("Drawing a transfer of electrons in a covalent molecule", "Covalent bonding is sharing. Electrons are not transferred and the atoms do not become ions."),
        QUIZ("How many lone pairs are there on the oxygen atom in a water molecule?", ["0", "1", "2", "4"], 2,
             "Oxygen has 6 outer electrons. Two are used in the two O–H bonds, leaving 4 electrons, which form 2 lone pairs.",
             hint="Count the outer electrons of oxygen and subtract those used in bonds.",
             feedback=["Oxygen has 6 outer electrons and uses only 2 in bonds.", "This would leave only 2 non-bonding electrons.", "", "Four electrons form two pairs, not four."]),
        QUIZ("In the ammonium ion NH₄⁺, which statement about the dative bond is correct?", [
            "Both electrons in the bond come from hydrogen",
            "Both electrons in the bond come from nitrogen",
            "The bond is ionic",
            "The bond is weaker than the other N–H bonds"], 1,
            "The lone pair on nitrogen provides both electrons. Once the bond forms, it is identical to the other N–H bonds.",
            hint="Which atom has the lone pair?",
            feedback=["The hydrogen ion H⁺ has no electrons.", "", "A shared pair of electrons is covalent.", "All four bonds are identical in strength."]),
        TIP("Dot-and-cross diagrams of H₂O, NH₃, CH₄, CO₂ and N₂ are tested in Paper 1 and Paper 2 Section A. The Board's report points to using the "
            "electronic configuration to predict bond type. Always draw the outer shells only and make sure each atom has a full shell.", title="Exam link"),
        H("Practice questions"),
        PQ("Define a covalent bond.", "A covalent bond is a shared pair of electrons between two atoms (usually non-metals)."),
        PQ("Draw (describe) the dot-and-cross diagram of a molecule of hydrogen chloride, HCl.", "H and Cl share one pair of electrons: one electron from H and one from Cl. Cl has three further lone pairs (6 non-bonding electrons) and so 8 electrons in its outer shell. H has 2 electrons."),
        PQ("State the number of shared pairs of electrons in (a) N₂ (b) CH₄ (c) O₂.", "(a) 3 (a triple bond). (b) 4 (four single bonds). (c) 2 (a double bond)."),
        PQ("Explain what is meant by a dative covalent bond, using NH₄⁺ as an example.", "In a dative covalent bond both electrons of the shared pair come from the same atom. In NH₄⁺ the nitrogen atom donates its lone pair to a hydrogen ion H⁺, which has no electrons."),
        SUM("A covalent bond is a shared pair of electrons between non-metal atoms, so that each atom has a full outer shell.",
            "Bonding pairs are shared; lone pairs belong to one atom. Single, double and triple bonds have 1, 2 and 3 shared pairs.",
            "Dot-and-cross diagrams use dots and crosses to show which atom each electron came from. Check that each atom has 8 outer electrons (2 for H).",
            "A dative bond is a shared pair where both electrons come from one atom, as in NH₄⁺ and H₃O⁺.",
            "Ionic bonding transfers electrons; covalent bonding shares them."),
    ],
))

# ------------------------------------------------------------------ 13. Intermolecular forces
LESSONS.append(lesson(
    module=MODULE,
    topic=BOND,
    title="Intermolecular forces: van der Waals forces and hydrogen bonding",
    slug="cha-intermolecular-forces",
    minutes=18,
    summary="Covalent bonds hold atoms together inside a molecule. Weak forces between molecules, van der Waals forces and hydrogen bonds, decide the melting and boiling points of simple molecular substances.",
    objectives=[
        "Distinguish a covalent bond (within a molecule) from an intermolecular force (between molecules)",
        "Describe van der Waals forces and hydrogen bonding",
        "State the conditions for hydrogen bonding",
        "Use intermolecular forces to explain trends in boiling points",
    ],
    key_concepts=["Intermolecular force", "van der Waals force", "Hydrogen bond", "Polar molecule", "Boiling point"],
    blocks=[
        H("Introduction"),
        T("Water boils at 100 °C. Oxygen, which is also made of small molecules, boils at −183 °C. Why does water need so much more heat? "
          "When water boils, its covalent bonds are not broken. Something else holds the molecules together. That something is the subject of this lesson."),
        D("**Intermolecular forces** are the forces of attraction **between** molecules. They are much weaker than the covalent bonds **within** a molecule.", title="Definition: intermolecular forces"),
        KEY("Two different kinds of force", "Do not mix them up.", cards=[
            ["Inside the molecule", "Strong covalent bonds between the atoms. They are not broken when a substance melts or boils."],
            ["Between molecules", "Weak intermolecular forces. These are overcome when a simple molecular substance melts or boils."],
        ]),
        H("van der Waals forces"),
        D("**van der Waals forces** are weak attractions between all molecules. They arise because the electrons in a molecule are always moving, so one side of the molecule can become slightly more negative than the other for a very short time. "
          "This temporary charge causes a similar charge in the neighbouring molecule, and the two attract.", title="Definition: van der Waals forces"),
        T("Every molecule has van der Waals forces, including non-polar ones such as the halogens, oxygen and nitrogen. The larger the molecule, the more electrons it has and the stronger the forces. "
          "So larger molecules have higher boiling points."),
        CODE("""Halogen   Molecule   Relative size   Boiling point (approx.)   State at 25 C
Chlorine  Cl2        smallest        -34 C                     gas
Bromine   Br2        medium           59 C                     liquid
Iodine    I2         largest         184 C                     solid""", "text", title="Van der Waals forces in the halogens"),
        T("This explains the trend you met in group VII. The molecules get bigger down the group, the van der Waals forces get stronger, and the boiling point rises."),
        H("Hydrogen bonding"),
        T("Some molecules have an extra, stronger attraction. In a molecule such as water, oxygen attracts the shared electrons more strongly than hydrogen does. "
          "The oxygen end of the molecule becomes slightly negative (written δ−) and the hydrogen end slightly positive (δ+). Such a molecule is **polar**."),
        D("A **hydrogen bond** is a strong intermolecular attraction between a hydrogen atom bonded to nitrogen, oxygen or fluorine (carrying a δ+ charge) and a lone pair on a nitrogen, oxygen or fluorine atom of a neighbouring molecule.", title="Definition: hydrogen bond"),
        IMG("f5ch-a-hydrogen-bonds.svg",
            alt="Three water molecules. Each hydrogen atom in one molecule is joined by a dashed hydrogen bond to the oxygen atom of the next molecule. The solid lines are the covalent O-H bonds.",
            caption="Figure 1. Hydrogen bonds between water molecules (dashed). Covalent bonds are drawn as solid lines."),
        T("Hydrogen bonds are stronger than ordinary van der Waals forces, but much weaker than covalent bonds. They form in water (H₂O), ammonia (NH₃), hydrogen fluoride (HF) and alcohols such as ethanol."),
        KEY("Effects of hydrogen bonding", "Hydrogen bonds explain several special properties of water.", cards=[
            ["High boiling point", "Extra energy is needed to separate hydrogen-bonded molecules, so water boils at 100 °C. Compare hydrogen sulfide, H₂S, which boils at about −60 °C."],
            ["Ice floats", "In ice, hydrogen bonds hold the molecules in an open arrangement, so ice is less dense than liquid water."],
            ["Good solvent", "Water molecules form hydrogen bonds and other attractions with many dissolved substances."],
        ]),
        CODE("""Substance   Hydrogen bonds?   Boiling point (approx.)
H2O         yes               100 C
H2S         no                -60 C
NH3         yes               -33 C
PH3         no                -88 C""", "text", title="Boiling points: hydrogen bonding effect"),
        H("Worked examples"),
        EX("Worked example 1: why does iodine have a higher boiling point than chlorine?", intro="Chlorine is a gas at room temperature and iodine is a solid. Explain.", steps=[
            S("Size", text="Iodine molecules are larger than chlorine molecules and have more electrons."),
            S("Forces", text="The van der Waals forces between I₂ molecules are stronger."),
            S("Energy", text="More energy is needed to overcome them, so iodine has the higher boiling point. Covalent bonds are not broken."),
        ]),
        EX("Worked example 2: water and hydrogen sulfide", intro="Water boils at 100 °C and hydrogen sulfide at −60 °C. Explain the difference.", steps=[
            S("Water", text="Oxygen is bonded to hydrogen, so water molecules form hydrogen bonds."),
            S("Hydrogen sulfide", text="Sulfur does not form hydrogen bonds, so there are only weak van der Waals forces."),
            S("Conclusion", text="More energy is needed to separate hydrogen-bonded water molecules, so water has the much higher boiling point."),
        ]),
        EX("Worked example 3: which bonds break?", intro="What is broken when (a) water boils (b) water is split into hydrogen and oxygen by electricity?", steps=[
            S("(a) Boiling", text="Hydrogen bonds between the molecules are broken. The molecules stay as H₂O."),
            S("(b) Electrolysis", text="Covalent O–H bonds are broken inside the molecules, and new bonds make H₂ and O₂."),
        ]),
        MISTAKE("Saying covalent bonds break when a simple molecular substance melts or boils", "Only the weak intermolecular forces are overcome. The covalent bonds inside each molecule stay unchanged. Write 'the forces between the molecules'."),
        MISTAKE("Saying that hydrogen bonds are present in any molecule that contains hydrogen", "Hydrogen bonds need H bonded to N, O or F. Methane (CH₄) has hydrogen atoms but has no hydrogen bonds."),
        MISTAKE("Calling a hydrogen bond a covalent bond", "A hydrogen bond is an attraction between molecules and is much weaker than the covalent bond within a molecule. Draw it as a dashed line."),
        QUIZ("Which kind of particle-to-particle force is overcome when ice melts?", [
            "Covalent bonds within each molecule",
            "Hydrogen bonds between molecules",
            "Ionic bonds",
            "Metallic bonds"], 1,
            "In ice, the water molecules are held by hydrogen bonds. Melting loosens these bonds. The molecules stay as H₂O.",
            hint="Water is a simple molecular substance.",
            feedback=["The H–O covalent bonds are not broken. The molecules stay as H₂O.", "", "Water has no ions.", "Water has no metal."]),
        QUIZ("Which of these molecules can form hydrogen bonds with other molecules of the same kind?", ["CH₄", "H₂S", "NH₃", "HCl"], 2,
             "Ammonia has hydrogen bonded to nitrogen, and nitrogen has a lone pair. So hydrogen bonds form between NH₃ molecules.",
             hint="The hydrogen must be bonded to nitrogen, oxygen or fluorine.",
             feedback=["Carbon is not N, O or F.", "Sulfur is not N, O or F.", "", "Chlorine is not N, O or F."]),
        TIP("Intermolecular forces appear in Paper 1 and in Paper 2 when you explain melting and boiling points, solubility, and why ice floats. "
            "Always say 'intermolecular forces between the molecules', and name the type: van der Waals or hydrogen bonds.", title="Exam link"),
        H("Practice questions"),
        PQ("Define a hydrogen bond.", "A hydrogen bond is an attraction between a hydrogen atom bonded to N, O or F in one molecule and a lone pair on an N, O or F atom of a neighbouring molecule."),
        PQ("Why does bromine have a higher boiling point than chlorine?", "Bromine molecules are larger with more electrons, so the van der Waals forces between them are stronger and more energy is needed to overcome them."),
        PQ("Ammonia boils at −33 °C but phosphine, PH₃, boils at −88 °C. Explain.", "Ammonia molecules form hydrogen bonds with each other because H is bonded to N. Phosphine has only weak van der Waals forces, so it needs less energy to boil."),
        PQ("State why a gas such as methane condenses to a liquid at very low temperatures.", "At very low temperatures the molecules have little energy. The weak intermolecular forces between the molecules can hold them together as a liquid."),
        SUM("Covalent bonds hold atoms inside a molecule. Intermolecular forces act between molecules and are much weaker.",
            "van der Waals forces act between all molecules; they get stronger as the molecules get bigger, raising the boiling point.",
            "A hydrogen bond forms between H bonded to N, O or F and a lone pair on N, O or F in another molecule.",
            "Hydrogen bonding gives water a high boiling point and makes ice less dense than water.",
            "When a simple molecular substance melts or boils, only intermolecular forces are overcome, not covalent bonds."),
    ],
))

# ------------------------------------------------------------------ 14. Structure and properties of solids
LESSONS.append(lesson(
    module=MODULE,
    topic=SOLIDS,
    title="Giant ionic, giant covalent and simple molecular structures",
    slug="cha-structure-properties-solids",
    minutes=22,
    summary="The structure of a solid decides its properties. Compare giant ionic lattices, giant covalent structures such as diamond and graphite, simple molecular solids and metals, and identify a structure from its properties.",
    objectives=[
        "Describe the structure of giant ionic, giant covalent and simple molecular solids",
        "Explain the melting point, hardness, conductivity and solubility of each type",
        "Compare diamond and graphite and link their uses to their structures",
        "Identify the type of structure of a substance from its properties",
    ],
    key_concepts=["Giant ionic lattice", "Giant covalent structure", "Simple molecular structure", "Diamond", "Graphite", "Conductivity of ions"],
    blocks=[
        H("Introduction"),
        T("Why can a diamond cut glass, while the graphite in a pencil leaves a mark on paper? Both are made only of carbon atoms. Why does salt dissolve in "
          "your soup, but sand does not, and why does candle wax melt over a small flame? The answer to each lies in the **structure**: how the particles are arranged and what holds them."),
        T("In this lesson you will use bonding (ionic, covalent, metallic and intermolecular forces) to explain the properties of the main types of solid."),
        H("Giant ionic structures"),
        D("A **giant ionic lattice** is a regular three-dimensional arrangement of a very large number of positive and negative ions held by strong electrostatic attraction in all directions. Example: sodium chloride, NaCl.", title="Definition: giant ionic lattice"),
        IMG("f5ch-a-nacl-lattice.svg",
            alt="A three-dimensional sketch of the sodium chloride lattice with small sodium ions and large chloride ions alternating in rows and columns.",
            caption="Figure 1. The sodium chloride lattice. Each ion is surrounded by six ions of opposite charge."),
        KEY("Properties of giant ionic compounds", "Each property follows from the strong lattice of ions.", cards=[
            ["High melting and boiling points", "Strong ionic bonds in all directions need a great deal of energy to break. NaCl melts at about 801 °C."],
            ["Hard but brittle", "A hard blow moves a layer of ions so that like charges are side by side. They repel, and the crystal splits."],
            ["Do not conduct when solid", "The ions are fixed in position and cannot move."],
            ["Conduct when molten or dissolved", "The ions are free to move and carry charge."],
            ["Often soluble in water", "Water molecules attract and separate the ions. (Not all ionic compounds dissolve.)"],
        ]),
        H("Giant covalent structures"),
        D("A **giant covalent structure** is a very large network of atoms joined together by strong covalent bonds throughout the whole structure. There are no separate molecules. Examples: diamond, graphite and silicon(IV) oxide (silica, found in sand).", title="Definition: giant covalent structure"),
        IMG("f5ch-a-giant-covalent.svg",
            alt="Left: diamond, a carbon atom bonded to four other carbon atoms. Right: graphite, flat layers of carbon hexagons with weak forces between the layers.",
            caption="Figure 2. Diamond and graphite are both pure carbon, with different structures."),
        CODE("""                  Diamond                  Graphite
Bonding           each C bonded to 4 C     each C bonded to 3 C in layers
Structure         rigid 3-D network        flat layers of hexagons
Hardness          very hard                soft, layers slide
Melting point     very high (over 3500 C)  very high
Conducts?         no (no free electrons)   yes (free electrons between layers)
Uses              cutting tools, drills,   pencils, lubricant,
                  jewellery                electrodes""", "text", title="Diamond compared with graphite"),
        T("In diamond all four outer electrons of every carbon atom are used in bonds, so no electrons are free to move and diamond does not conduct. "
          "In graphite, each carbon uses only three electrons for bonding in its layer. The fourth electron is **delocalized** between the layers and free to move, so graphite conducts electricity. "
          "The layers are held by weak forces, so they slide easily, which makes graphite soft and slippery."),
        T("Silicon(IV) oxide (SiO₂) has a giant structure like diamond, but with silicon and oxygen atoms. It is hard, has a very high melting point (about 1700 °C) and does not conduct."),
        KEY("Properties of giant covalent substances", "All have strong bonds throughout.", cards=[
            ["Very high melting points", "Many strong covalent bonds must be broken."],
            ["Hard (except graphite)", "Atoms are held rigidly in place."],
            ["Do not conduct (except graphite)", "No free electrons or ions."],
            ["Insoluble in water", "The strong bonds are not overcome by water."],
        ]),
        H("Simple molecular structures"),
        D("A **simple molecular structure** is made of small separate molecules, each held together by strong covalent bonds inside, but attracted to other molecules only by weak intermolecular forces. Examples: iodine, carbon dioxide (dry ice), water (ice) and wax.", title="Definition: simple molecular structure"),
        KEY("Properties of simple molecular substances", "The weak forces between the molecules explain them.", cards=[
            ["Low melting and boiling points", "Only weak intermolecular forces are overcome. The covalent bonds in the molecules are not broken."],
            ["Soft or brittle, easily crushed", "The molecules separate easily."],
            ["Do not conduct electricity", "The molecules have no charge and no free electrons."],
            ["Usually insoluble in water", "But many dissolve in organic solvents."],
        ]),
        H("Putting it together"),
        CODE("""Type             Particles          Bonding                   Melting pt   Conducts?
Giant ionic      ions               ionic (strong)            high         molten or dissolved
Giant covalent   atoms              covalent (strong)         very high    no (graphite: yes)
Simple molecular molecules          covalent inside,          low          no
                                    weak forces between
Metallic         ions + electrons   metallic (strong)         high         yes, solid and liquid""", "text", title="Summary of structures"),
        H("Worked examples"),
        EX("Worked example 1: identify the structure", intro="Substance X melts at 802 °C. It does not conduct when solid but conducts when molten. It dissolves in water. What type of structure does it have?", steps=[
            S("Melting point", text="802 °C is high, so there are strong forces in all directions."),
            S("Conductivity", text="It does not conduct when solid but does when molten. Ions are fixed in the solid, but free to move when molten."),
            S("Conclusion", text="It is a giant ionic compound."),
        ]),
        EX("Worked example 2: explain a property", intro="Explain why diamond has a very high melting point but iodine melts easily.", steps=[
            S("Diamond", text="Diamond is a giant covalent structure. Every atom is joined to four others by strong covalent bonds, and all of them must be broken to melt it."),
            S("Iodine", text="Iodine is a simple molecular substance. Only the weak forces between I₂ molecules are overcome. The I–I bonds do not break."),
        ]),
        EX("Worked example 3: graphite", intro="Explain why graphite conducts electricity and is used as a lubricant.", steps=[
            S("Conduction", text="Each carbon atom uses 3 outer electrons in bonds. The fourth is delocalized and free to move along the layers, carrying charge."),
            S("Lubricant", text="The layers are held by weak forces, so they slide over one another easily."),
        ]),
        MISTAKE("Saying ionic compounds conduct because they contain electrons", "Ionic compounds conduct when molten or dissolved because their **ions** are free to move. In the solid the ions are fixed and cannot carry charge."),
        MISTAKE("Saying covalent bonds break when iodine or ice melts", "Only intermolecular forces are overcome when a simple molecular substance melts. The covalent bonds stay unchanged."),
        MISTAKE("Saying all covalent substances have low melting points", "Only simple molecular substances do. Diamond and silicon(IV) oxide are covalent but have very high melting points because they are giant structures."),
        QUIZ("Why does solid sodium chloride not conduct electricity, while molten sodium chloride does?", [
            "Solid sodium chloride has no ions",
            "In the solid the ions are fixed in position; when molten they are free to move",
            "Molten sodium chloride contains free electrons",
            "The solid has covalent bonds"], 1,
            "A solid has ions fixed in the lattice. When molten, the ions are free to move and carry the charge.",
            hint="Which particles carry charge in an ionic compound?",
            feedback=["The solid contains ions, but they cannot move.", "", "The charge is carried by ions, not by free electrons.", "Sodium chloride is ionic."]),
        QUIZ("Which substance has a giant covalent structure?", ["Iodine", "Sodium chloride", "Diamond", "Carbon dioxide"], 2,
             "Diamond is a giant network of carbon atoms joined by covalent bonds. Iodine and carbon dioxide are simple molecular. Sodium chloride is a giant ionic lattice.",
             hint="Which one is made only of atoms joined in a huge network?",
             feedback=["Iodine is a simple molecular substance.", "Sodium chloride is a giant ionic lattice.", "", "Carbon dioxide is a simple molecular substance."]),
        TIP("Structure and properties of solids is tested in Paper 1 and in Paper 2 Section A. The Board's 2023 report notes that many candidates could not tell the crystalline forms of carbon from the non-crystalline forms, so learn diamond and graphite well. "
            "Always link the property to the type of particle and the type of bond, and name the particles that move when a substance conducts.", title="Exam link"),
        H("Practice questions"),
        PQ("Explain why sodium chloride has a high melting point.", "Sodium chloride is a giant ionic lattice. Each ion is held to the oppositely charged ions around it by strong electrostatic forces in all directions, and a large amount of energy is needed to overcome them."),
        PQ("Explain why graphite can be used as an electrode, but diamond cannot.", "In graphite, each carbon has one delocalized electron, which is free to move and carry charge. In diamond all outer electrons are used in bonds, so there are no free electrons."),
        PQ("Substance Y melts at 55 °C, does not conduct in any state, and is insoluble in water. What type of structure does it probably have? Explain.", "It has a simple molecular structure. The low melting point shows that the forces between the particles are weak. It does not conduct because it has no ions or free electrons."),
        PQ("Why is silicon(IV) oxide hard and why does it have a very high melting point?", "It has a giant covalent structure in which each atom is bonded to others by strong covalent bonds throughout the whole structure. A large amount of energy is needed to break them."),
        SUM("A giant ionic lattice has strong forces in all directions: high melting point, brittle, conducts only when molten or dissolved.",
            "A giant covalent structure is a huge network of atoms: very high melting point, hard, and non-conducting, except graphite.",
            "Graphite conducts because each carbon has a delocalized electron, and is soft because its layers slide. Diamond is hard because each carbon is bonded to four others.",
            "A simple molecular substance has weak forces between the molecules: low melting point, does not conduct, easy to crush.",
            "Link every property to the particles and the forces, and say which particles carry charge in conduction."),
    ],
))
