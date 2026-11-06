"""Practice sets for Form 5 Chemistry: Matter, Atomic Structure & Bonding (one set per lesson)."""

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

SETS = []

# ------------------------------------------------------------------ 1. States and kinetic theory
SETS.append(practice_set(
    module=MODULE, topic=STATES,
    title="The three states of matter and the kinetic theory",
    lesson="cha-states-kinetic-theory",
    questions=[
        MC("Which statement describes the particles in a solid?", [
            C("They are far apart and move quickly in all directions", why="This describes a gas."),
            C("They are close together in a regular pattern and vibrate about fixed positions", correct=True),
            C("They are close together but irregular, and slide past each other", why="This describes a liquid."),
            C("They are far apart in a regular pattern", why="No state of matter has particles far apart in a regular pattern."),
        ], steps=[S("Recall", text="In a solid the particles are packed closely in a regular pattern. Strong forces hold them in place, so they only vibrate.")],
           concept="Particles in a solid", skill="Recall", hint="Think of what keeps a solid in a fixed shape."),
        MC("Why can a gas be compressed easily?", [
            C("Gas particles are very soft and can be crushed", why="Particles are not crushed. Only the spaces between them get smaller."),
            C("The forces between gas particles are very strong", why="The forces between gas particles are very weak."),
            C("Gas particles are arranged in a regular pattern", why="Gas particles move randomly and have no pattern."),
            C("There is a lot of empty space between the particles", correct=True),
        ], steps=[S("Use the theory", text="The particles of a gas are far apart. Pressure pushes them closer, so the volume gets smaller.")],
           concept="Compression of gases", skill="Concept", hint="Compare how far apart the particles are in a gas and in a solid."),
        MC("Why does a liquid take the shape of its container?", [
            C("Its particles can slide past one another", correct=True),
            C("Its particles are far apart and move freely", why="Liquid particles are close together. Far apart particles describe a gas."),
            C("Its particles vibrate in fixed positions", why="That describes a solid, which keeps its own shape."),
            C("There are no forces between its particles", why="There are forces between liquid particles. They keep the volume fixed."),
        ], steps=[S("Use the theory", text="Liquid particles are close together but not fixed in place. They move past one another and so flow into the shape of the container.")],
           concept="Shape of liquids", skill="Concept", hint="What can the particles of a liquid do that the particles of a solid cannot?"),
        MC("In which state of matter does diffusion happen fastest?", [
            C("Solid", why="Particles in a solid only vibrate, so diffusion is almost zero."),
            C("Liquid", why="Diffusion in a liquid is slower than in a gas, because the particles are close and collide often."),
            C("Gas", correct=True),
            C("It is the same in all three states", why="The speed depends on how freely the particles move."),
        ], steps=[S("Compare", text="Gas particles move fastest and are free to move through the space between other particles.")],
           concept="Rate of diffusion in the states", skill="Concept", hint="Which state has particles that move most freely?"),
        MC("Under a microscope, smoke particles in air move in random zig-zags. This provides evidence that", [
            C("the smoke particles are alive", why="The motion is caused by collisions, not life."),
            C("air is made of particles that move randomly", correct=True),
            C("gases can be compressed", why="Compression is a different property and is not shown by the zig-zag."),
            C("solids are made of particles in a regular pattern", why="Brownian motion is about the particles of a gas or liquid."),
        ], steps=[S("Explain", text="The smoke specks are knocked from different sides by fast-moving air particles that we cannot see. So air must be made of moving particles.")],
           concept="Brownian motion as evidence", skill="Reasoning", hint="What invisible things are hitting the smoke specks?"),
        NUM("In the ammonia and hydrogen chloride experiment, a 100 cm glass tube has ammonia at one end and hydrogen chloride at the other. The white ring forms 60 cm from the ammonia end. How far is the ring from the hydrogen chloride end?", 40,
            steps=[S("Use the tube length", math=r"100 - 60 = 40", text="The two distances add up to the length of the tube."),
                   S("Check the idea", text="The ring is nearer the HCl end, because the lighter NH₃ travelled further.")],
            tolerance=0, unit="cm", concept="Diffusion of ammonia and hydrogen chloride", skill="Application",
            hint="The two distances must add up to the length of the tube."),
        MC("A sealed rigid container of gas is heated. The pressure rises. Which is the best explanation?", [
            C("The particles get bigger", why="The particles do not change size when heated."),
            C("There are more particles in the container", why="The container is sealed, so the number of particles has not changed."),
            C("The particles move closer together", why="The container is rigid, so the particles are no closer. They are moving faster."),
            C("The particles move faster and hit the walls harder and more often", correct=True),
        ], steps=[S("Link temperature and speed", text="A higher temperature means faster particles."),
                  S("Link speed and pressure", text="Faster particles hit the walls harder and more often, so the pressure is greater.")],
           concept="Gas pressure and temperature", skill="Reasoning", hint="What happens to the speed of the particles when the gas is heated?"),
        MC("A crystal of potassium manganate(VII) is placed at the bottom of a beaker of still water. Which observation shows diffusion?", [
            C("The crystal gets smaller when stirred", why="Stirring makes the crystal dissolve faster, but this is not diffusion by itself."),
            C("The water level rises a little", why="This is not related to particles spreading."),
            C("The purple colour slowly spreads through the whole beaker", correct=True),
            C("Bubbles rise from the crystal", why="Bubbles would be a gas. They are not evidence of diffusion."),
        ], steps=[S("Recognise diffusion", text="The coloured particles spread from the crystal (high concentration) into the water (low concentration) by their own movement, even with no stirring.")],
           concept="Diffusion in liquids", skill="Application", hint="Look for particles spreading without anything moving them."),
    ]))

# ------------------------------------------------------------------ 2. Changes of state and curves
SETS.append(practice_set(
    module=MODULE, topic=STATES,
    title="Changes of state and heating and cooling curves",
    lesson="cha-heating-cooling-curves",
    questions=[
        MC("What is the name of the change of a solid straight into a gas?", [
            C("Sublimation", correct=True),
            C("Evaporation", why="Evaporation is a liquid changing into a gas."),
            C("Melting", why="Melting is a solid becoming a liquid."),
            C("Condensation", why="Condensation is a gas becoming a liquid."),
        ], steps=[S("Recall", text="Sublimation is a direct change between solid and gas, with no liquid stage. Iodine does this when heated gently.")],
           concept="Sublimation", skill="Recall", hint="No liquid appears in this change."),
        MC("At normal pressure, pure water freezes at", [
            C("100 °C", why="100 °C is the boiling point of water."),
            C("0 °C", correct=True),
            C("10 °C", why="Water does not freeze until it reaches a lower temperature."),
            C("−10 °C", why="Pure water freezes at 0 °C. It only goes lower with a dissolved substance."),
        ], steps=[S("Recall", text="Pure water freezes and melts at 0 °C at normal pressure.")],
           concept="Freezing point of water", skill="Recall", hint="It is the same temperature at which ice melts."),
        MC("The figure shows the heating curve of a pure substance. Which section shows the substance boiling?", [
            C("Section B", why="Section B is the flat part at the lower temperature. It is melting."),
            C("Section C", why="In section C the temperature is rising, so the liquid is just getting hotter."),
            C("Section E", why="In section E the temperature rises again because the gas is being heated."),
            C("Section D", correct=True),
        ], steps=[S("Find flat sections", text="B and D are flat. The lower flat section is melting; the higher one is boiling."),
                  S("Choose", text="Boiling is the flat section at the higher temperature, section D.")],
           concept="Reading a heating curve", skill="Interpretation", hint="There are two flat sections. Which is at the higher temperature?",
           diagram="f5ch-a-heating-curve-q.svg", diagram_alt="Heating curve with sections A to E. B is flat at 0 degrees Celsius, D is flat at 100 degrees Celsius."),
        MC("Why does the temperature stay constant while a pure solid melts?", [
            C("The heater has switched off", why="The substance is still taking in heat."),
            C("The heat is used to overcome the forces between particles", correct=True),
            C("The particles stop moving", why="Particles never stop moving."),
            C("The solid is losing heat to the air", why="Heat is still being supplied. Heat lost to the air does not explain the flat part."),
        ], steps=[S("Use the theory", text="The energy supplied breaks the forces that hold the particles in the solid. It does not make them move faster, so the temperature stays the same.")],
           concept="Constant temperature in melting", skill="Concept", hint="Where does the energy go if not into a higher temperature?"),
        NUM("A pure liquid is cooled and its temperature is recorded every minute: 0 min 90 °C, 1 min 78 °C, 2 min 66 °C, 3 min 54 °C, 4 min 54 °C, 5 min 54 °C, 6 min 54 °C, 7 min 44 °C. What is the freezing point of the liquid?", 54,
            steps=[S("Find the flat part", text="The temperature stays at 54 °C from 3 min to 6 min."),
                   S("Conclusion", text="The flat part of a cooling curve is the freezing point, so it is 54 °C.")],
            tolerance=0, unit="°C", concept="Freezing point from a cooling curve", skill="Interpretation", hint="Look for the temperature that does not change."),
        MC("Which statement about evaporation is correct?", [
            C("It happens only at the surface of a liquid", correct=True),
            C("It happens only at the boiling point", why="That is boiling. Evaporation happens at any temperature."),
            C("It makes bubbles throughout the liquid", why="Bubbles through the liquid are a sign of boiling."),
            C("It happens only when the liquid is heated", why="Evaporation happens in cold liquids too, such as puddles drying."),
        ], steps=[S("Recall", text="Evaporation is the escape of the fastest particles from the surface of a liquid, at any temperature below the boiling point.")],
           concept="Evaporation", skill="Concept", hint="Think of a puddle that dries without being heated."),
        MC("A sample of a solid melts slowly between 70 °C and 76 °C. The pure solid melts at 80 °C. Which is the best conclusion?", [
            C("The sample is a pure substance", why="A pure substance melts sharply at a single temperature."),
            C("The sample is a gas", why="A gas is not a solid that melts."),
            C("The thermometer was heated too fast", why="A fast rate cannot explain melting at a lower temperature and over a range."),
            C("The sample is impure", correct=True),
        ], steps=[S("Compare with a pure sample", text="A pure solid has a sharp melting point at 80 °C."),
                  S("Conclusion", text="Melting over a range and below 80 °C shows the sample contains impurities.")],
           concept="Purity and melting point", skill="Reasoning", hint="How does an impurity change the melting point?"),
        MC("Why does a person feel cooler when sweat evaporates from the skin?", [
            C("Sweat is always colder than the skin", why="The sweat is at body temperature. The cooling comes from evaporation."),
            C("The slowest particles leave the sweat and take energy with them", why="It is the fastest, highest-energy particles that escape."),
            C("The fastest particles leave the sweat, so the remaining liquid and the skin cool", correct=True),
            C("The sweat boils and takes heat from the air", why="Sweat does not boil at body temperature. It evaporates."),
        ], steps=[S("Who escapes?", text="Only the fastest particles at the surface have enough energy to leave."),
                  S("Effect", text="They take their energy with them, so the average energy of the rest falls and the skin cools.")],
           concept="Cooling effect of evaporation", skill="Application", hint="Which particles are able to escape from the surface?"),
    ]))

# ------------------------------------------------------------------ 3. Pure substances and mixtures
SETS.append(practice_set(
    module=MODULE, topic=PURE,
    title="Pure substances, elements, compounds and mixtures",
    lesson="cha-pure-substances-mixtures",
    questions=[
        MC("Which of these is an element?", [
            C("Sea water", why="Sea water is a mixture of water and dissolved salts."),
            C("Brass", why="Brass is an alloy, a mixture of copper and zinc."),
            C("Sulfur", correct=True),
            C("Air", why="Air is a mixture of gases."),
        ], steps=[S("Check the atoms", text="Sulfur contains only sulfur atoms, so it is an element. The others contain more than one substance.")],
           concept="Identifying an element", skill="Recall", hint="An element contains only one kind of atom."),
        MC("Which statement about a mixture is correct?", [
            C("Its parts are chemically joined", why="In a mixture the parts are not chemically joined."),
            C("It has a fixed formula", why="A fixed formula is a property of a compound."),
            C("It can only be separated by a chemical reaction", why="A mixture is separated by physical methods."),
            C("Its parts can be present in any proportion", correct=True),
        ], steps=[S("Recall", text="A mixture has no fixed composition. Its parts keep their own properties and are separated by physical methods.")],
           concept="Properties of a mixture", skill="Recall", hint="Think of how much sugar you can put in a cup of tea."),
        MC("A pure substance is one that", [
            C("contains only one substance and has sharp melting and boiling points", correct=True),
            C("looks the same all through", why="A solution looks the same all through but is still a mixture."),
            C("is natural and has nothing added to it", why="In chemistry pure does not mean natural. Natural juice is a mixture."),
            C("contains only one element", why="A pure substance can also be a compound, such as water."),
        ], steps=[S("Recall", text="A pure substance is a single element or a single compound, with fixed composition and sharp melting and boiling points.")],
           concept="Definition of a pure substance", skill="Recall", hint="Remember that a compound can be pure too."),
        MC("Which of these is a solution?", [
            C("Muddy river water", why="Muddy water is a suspension. The mud settles."),
            C("Salt dissolved in water", correct=True),
            C("Palm oil shaken with water", why="This forms an emulsion, not a solution, because the oil does not dissolve."),
            C("Sand stirred into water", why="Sand is insoluble and forms a suspension."),
        ], steps=[S("Look for dissolving", text="A solution is a solute dissolved in a solvent. Only salt in water is dissolved. The others are insoluble.")],
           concept="Recognising a solution", skill="Concept", hint="In a solution the solute cannot be seen and does not settle."),
        MC("Iron filings and sulfur are heated and a black solid forms. Which observation shows that a compound has formed?", [
            C("The powder is hot", why="Heat alone does not show a new substance; it could be heated for any reason."),
            C("The sulfur is still yellow", why="If sulfur were still present as it was, no compound would have formed."),
            C("The black solid is not attracted by a magnet", correct=True),
            C("The black solid is a powder", why="Both the mixture and the compound can be powders."),
        ], steps=[S("Compare properties", text="Iron is magnetic. A compound has new properties, so a black solid not attracted by a magnet shows that iron(II) sulfide, a new substance, has formed.")],
           concept="Mixture versus compound", skill="Reasoning", hint="Which property of iron would be kept in a mixture?"),
        MC("In a cup of sweet tea, which substance is the solute?", [
            C("Sugar", correct=True),
            C("Tea", why="The tea (mostly water) is the solvent, not the solute."),
            C("The cup", why="The cup is not part of the solution."),
            C("Water", why="Water is the solvent."),
        ], steps=[S("Identify", text="The solute is the substance that dissolves. Sugar dissolves in the tea, so sugar is the solute.")],
           concept="Solute and solvent", skill="Application", hint="Which substance disappears into the liquid?"),
        NUM("Air is about 21% oxygen by volume. How many cm³ of oxygen are there in 500 cm³ of air?", 105,
            steps=[S("Find 21%", math=r"\frac{21}{100} \times 500 = 105")],
            tolerance=1, unit="cm³", concept="Composition of air", skill="Calculation", hint="Find 21% of 500."),
        MC("Which observation proves that a substance is a mixture rather than a compound?", [
            C("It is a solid", why="Both mixtures and compounds can be solids."),
            C("Its parts can be separated by a physical method such as a magnet or filtering", correct=True),
            C("It has a high melting point", why="Some compounds have very high melting points."),
            C("It is made of more than one element", why="A compound is also made of more than one element."),
        ], steps=[S("Think", text="A compound's elements are chemically joined, so only a chemical reaction separates them. Separation by physical methods shows the parts were only mixed.")],
           concept="Evidence for a mixture", skill="Reasoning", hint="Think about which kind of method separates a compound."),
    ]))

# ------------------------------------------------------------------ 4. Separation techniques
SETS.append(practice_set(
    module=MODULE, topic=PURE,
    title="Separation techniques",
    lesson="cha-separation-techniques",
    questions=[
        MC("Which method separates sand from a mixture of sand and water?", [
            C("Filtration", correct=True),
            C("Simple distillation", why="Distillation would boil off the water, which is not needed to remove an insoluble solid."),
            C("Using a magnet", why="Sand is not magnetic."),
            C("Sublimation", why="Neither substance sublimes."),
        ], steps=[S("Match the property", text="Sand is an insoluble solid, so filtration removes it. The sand stays on the filter paper.")],
           concept="Filtration", skill="Recall", hint="One substance is an insoluble solid in a liquid."),
        MC("After filtering a muddy mixture, the solid left on the filter paper is called the", [
            C("filtrate", why="The filtrate is the liquid that passes through the paper."),
            C("distillate", why="The distillate is what is collected after distillation."),
            C("residue", correct=True),
            C("solvent", why="The solvent is the liquid that dissolves a solute."),
        ], steps=[S("Recall", text="The residue is what stays on the paper. The filtrate goes through.")],
           concept="Residue and filtrate", skill="Recall", hint="It is the part that is left behind."),
        MC("In simple distillation, cold water enters the condenser at the bottom and leaves at the top. Why?", [
            C("So that the water can be heated up", why="The water is there to cool the vapour, not to be heated."),
            C("To stop the thermometer from breaking", why="The thermometer is in the flask and is not cooled by this water."),
            C("To make the vapour boil faster", why="Cold water makes vapour condense, not boil."),
            C("So that the jacket stays full of cold water and cools the vapour well", correct=True),
        ], steps=[S("Think about the flow", text="Water entering at the bottom rises and fills the jacket completely. A full jacket cools the vapour all along its length.")],
           concept="Condenser water flow", skill="Concept", hint="Think about what would happen if water entered at the top."),
        MC("Which pair of liquids can be separated using a separating funnel?", [
            C("Ethanol and water", why="They mix completely, so they do not form layers."),
            C("Kerosene and water", correct=True),
            C("Vinegar and water", why="Vinegar mixes with water, so there are no layers."),
            C("Methanol and ethanol", why="These two liquids mix completely."),
        ], steps=[S("Look for immiscible liquids", text="A separating funnel works for liquids that do not mix and form layers. Kerosene does not mix with water.")],
           concept="Separating funnel", skill="Application", hint="Which pair forms two layers?"),
        MC("A mixture of liquid X (boiling point 65 °C) and liquid Y (boiling point 98 °C) that mix completely is separated by fractional distillation. Which is collected first?", [
            C("Y, because it has the higher boiling point", why="The substance with the higher boiling point is collected last."),
            C("Neither, they come off together", why="The column separates them by boiling point."),
            C("X, because it has the lower boiling point", correct=True),
            C("Y, because it is heavier", why="Mass does not decide the order. The boiling point does."),
        ], steps=[S("Compare boiling points", text="X boils at the lower temperature, so its vapour reaches the top of the column first and is collected first.")],
           concept="Fractional distillation order", skill="Concept", hint="Which liquid boils at the lower temperature?"),
        NUM("A student separates ethanol from 40 cm³ of an ethanol–water mixture by fractional distillation. The mixture contains 40% ethanol by volume. The student collects 14.4 cm³ of ethanol. What percentage of the ethanol was recovered?", 90,
            steps=[S("Find the ethanol present", math=r"0.40 \times 40 = 16\ \text{cm}^3"),
                   S("Percentage recovered", math=r"\frac{14.4}{16} \times 100 = 90\%")],
            tolerance=0.5, unit="%", concept="Percentage recovered in a separation", skill="Calculation",
            hint="First work out how much ethanol was in the mixture."),
        MC("A dry mixture contains iron filings, sand and salt. Which is the correct order of steps to separate all three?", [
            C("Add water and filter, then use a magnet, then evaporate", why="The magnet is best used on the dry mixture first. Iron wet with water is harder to remove and may rust."),
            C("Use a magnet, add water and filter, then evaporate the filtrate", correct=True),
            C("Evaporate, then use a magnet, then filter", why="Evaporating a dry mixture does nothing, and filtering needs a liquid."),
            C("Filter, then use a magnet, then add water", why="Filtering a dry mixture does not work. Water must be added first."),
        ], steps=[S("Magnet first", text="The magnet removes iron from the dry mixture."),
                  S("Dissolve and filter", text="Adding water dissolves the salt. Filtering leaves the sand as residue."),
                  S("Evaporate", text="Evaporating the filtrate gives back the salt.")],
           concept="Planning a separation", skill="Reasoning", hint="Which substance can be removed from a dry mixture?"),
        MC("Why is a salt solution evaporated only until it is almost saturated and then cooled, instead of being heated to dryness?", [
            C("To give larger, purer crystals", correct=True),
            C("Because salt is destroyed by gentle heat", why="Sodium chloride is stable. The reason is the quality of the crystals."),
            C("Because cooling makes the salt dissolve", why="Cooling makes less solid dissolve, so crystals form."),
            C("To stop the water from evaporating", why="Water has already been evaporated. Cooling is used to make crystals."),
        ], steps=[S("Compare", text="Evaporating to dryness leaves a crust of small crystals that can hold impurities. Slow cooling of a saturated solution gives larger, purer crystals.")],
           concept="Crystallization", skill="Application", hint="Think of the size and purity of the crystals."),
    ]))

# ------------------------------------------------------------------ 5. Chromatography and purity
SETS.append(practice_set(
    module=MODULE, topic=PURE,
    title="Paper chromatography, Rf values and tests for purity",
    lesson="cha-chromatography-purity",
    questions=[
        MC("Why is the baseline on a chromatography paper drawn in pencil?", [
            C("Pencil is easier to see", why="Seeing the line is not the reason. The reason is chemical."),
            C("Pencil lead does not dissolve in the solvent", correct=True),
            C("Pencil makes the solvent rise faster", why="The line does not change how fast the solvent rises."),
            C("Pencil lead reacts with the spots", why="Graphite does not react with the dyes. It simply does not dissolve."),
        ], steps=[S("Think about the solvent", text="Ink contains dyes that dissolve in the solvent and would run up the paper. Graphite does not dissolve, so it stays on the line.")],
           concept="Pencil baseline", skill="Recall", hint="What would happen to an ink line in the solvent?"),
        MC("A sample gives three separate spots on a chromatogram. This shows that the sample", [
            C("is a pure substance", why="A pure substance gives a single spot."),
            C("is a compound", why="The number of spots shows how many substances are mixed. It does not show a compound."),
            C("contains at least three substances", correct=True),
            C("has a high boiling point", why="Chromatography does not measure boiling point."),
        ], steps=[S("Count the spots", text="Each spot is a different substance, so there are at least three substances in the sample.")],
           concept="Interpreting the number of spots", skill="Concept", hint="One spot means one substance."),
        MC("In the chromatogram, which sample or samples are mixtures?", [
            C("P only", why="P gives one spot, so it is a pure dye."),
            C("Q only", why="Q gives one spot, so it is a pure dye."),
            C("P and Q", why="Both give a single spot."),
            C("M only", correct=True),
        ], steps=[S("Count the spots in each column", text="P has one spot, Q has one spot and M has two spots."),
                  S("Decide", text="Only M has more than one spot, so only M is a mixture.")],
           concept="Identifying mixtures on a chromatogram", skill="Interpretation", hint="Count the spots above each letter.",
           diagram="f5ch-a-chromatography.svg", diagram_alt="Chromatogram: columns P and Q each have one spot, M has two spots at the same heights as P and Q."),
        NUM("Use the chromatogram. The solvent front moved 10 cm and the blue spot moved 3 cm. Calculate the Rf value of the blue dye.", 0.3,
            steps=[S("Formula", math=r"R_f = \frac{3}{10}"), S("Answer", math=r"R_f = 0.3")],
            tolerance=0.01, unit="", concept="Rf from a chromatogram", skill="Calculation", hint="Divide the distance moved by the spot by the distance moved by the solvent front.",
            diagram="f5ch-a-chromatography.svg", diagram_alt="Chromatogram with solvent front at 10 cm, yellow spot at 6 cm and blue spot at 3 cm above the baseline."),
        NUM("In another experiment the solvent front moves 7.5 cm and a spot moves 3.0 cm. Calculate its Rf value.", 0.4,
            steps=[S("Divide", math=r"R_f = \frac{3.0}{7.5} = 0.4")],
            tolerance=0.01, unit="", concept="Calculating Rf", skill="Calculation", hint="Substance distance divided by solvent distance."),
        MC("Which of these could be a correct Rf value?", [
            C("0.45", correct=True),
            C("1.4", why="The substance can never travel further than the solvent front, so Rf cannot be above 1."),
            C("2.5 cm", why="Rf has no unit, and it cannot be above 1."),
            C("−0.3", why="A distance cannot be negative."),
        ], steps=[S("Use the definition", text="Rf is the distance moved by the substance divided by the distance moved by the solvent. The substance cannot go further than the solvent, so Rf is between 0 and 1, with no unit.")],
           concept="Range of Rf values", skill="Concept", hint="Can a spot travel further than the solvent front?"),
        MC("A student starts a chromatogram with the solvent level above the baseline. What is the likely result?", [
            C("The spots rise faster", why="The solvent cannot carry spots that have already dissolved into the container."),
            C("The spots separate better", why="Separation needs the spots to stay on the paper."),
            C("The spots dissolve into the solvent in the container and no chromatogram forms", correct=True),
            C("The paper turns the colour of the solvent", why="The paper only changes colour if a dye moves up it."),
        ], steps=[S("Think", text="The spots must be above the solvent level at the start. If the solvent covers them, the dyes dissolve into the container.")],
           concept="Setting up chromatography", skill="Application", hint="Where must the starting spots be, compared with the solvent level?"),
        MC("A liquid boils over the range 98 °C to 104 °C. What does this suggest?", [
            C("The liquid is pure", why="A pure liquid has a sharp, fixed boiling point."),
            C("The liquid is impure", correct=True),
            C("The liquid is a solid", why="A solid does not boil."),
            C("The thermometer reads too slowly", why="Nothing suggests a fault. Impure liquids typically boil over a range."),
        ], steps=[S("Compare with a pure liquid", text="A pure liquid boils at one fixed temperature. Boiling over a range means other substances are present.")],
           concept="Boiling range and purity", skill="Reasoning", hint="Does a pure liquid boil at a single temperature?"),
    ]))

# ------------------------------------------------------------------ 6. Subatomic particles
SETS.append(practice_set(
    module=MODULE, topic=ATOM,
    title="Subatomic particles, atomic number and mass number",
    lesson="cha-subatomic-particles",
    questions=[
        MC("What is the relative charge of a neutron?", [
            C("+1", why="+1 is the charge of a proton."),
            C("0", correct=True),
            C("−1", why="−1 is the charge of an electron."),
            C("+1/1840", why="This mixes up the charge with the mass of an electron."),
        ], steps=[S("Recall", text="A neutron is neutral, with relative charge 0.")],
           concept="Charge of a neutron", skill="Recall", hint="The name hints at the answer."),
        MC("Which two particles are found in the nucleus of an atom?", [
            C("Protons and neutrons", correct=True),
            C("Protons and electrons", why="Electrons move in shells outside the nucleus."),
            C("Neutrons and electrons", why="Electrons are not in the nucleus."),
            C("Electrons only", why="The electrons are outside the nucleus."),
        ], steps=[S("Recall", text="The nucleus contains protons and neutrons. The electrons are in shells around it.")],
           concept="Particles in the nucleus", skill="Recall", hint="Which particles are outside the nucleus?"),
        MC("The atomic number of an atom is the number of", [
            C("neutrons in the nucleus", why="The number of neutrons is the mass number minus the atomic number."),
            C("protons and neutrons in the nucleus", why="This is the mass number."),
            C("electrons in the outer shell", why="This decides the group, not the atomic number."),
            C("protons in the nucleus", correct=True),
        ], steps=[S("Recall", text="The atomic number is the number of protons. It identifies the element.")],
           concept="Definition of atomic number", skill="Recall", hint="It identifies the element."),
        NUM("An atom of iron has atomic number 26 and mass number 56. How many neutrons does it have?", 30,
            steps=[S("Neutrons = A − Z", math=r"56 - 26 = 30")],
            tolerance=0, unit="", concept="Calculating neutrons", skill="Calculation", hint="Subtract the atomic number from the mass number."),
        MC("How many electrons are in an aluminium ion Al³⁺? (Atomic number of Al is 13.)", [
            C("13", why="This is the number of electrons in the neutral atom."),
            C("16", why="The electrons were added instead of removed. Al³⁺ has lost electrons."),
            C("10", correct=True),
            C("3", why="The charge 3+ shows how many electrons were lost, not how many remain."),
        ], steps=[S("Start with the atom", text="A neutral Al atom has 13 electrons."),
                  S("Remove 3", math=r"13 - 3 = 10")],
           concept="Electrons in a positive ion", skill="Calculation", hint="A 3+ ion has lost three electrons."),
        MC("The diagram shows an atom of element X. What is the atomic number of X?", [
            C("13", correct=True),
            C("3", why="This is the number of electrons in the outer shell."),
            C("8", why="This is the number in the second shell only."),
            C("10", why="This is the number in the first two shells only."),
        ], steps=[S("Count all electrons", math=r"2 + 8 + 3 = 13"),
                  S("Link to protons", text="A neutral atom has equal protons and electrons, so the atomic number is 13.")],
           concept="Atomic number from an electron diagram", skill="Interpretation", hint="Add up all the dots in all the shells.",
           diagram="f5ch-a-shell-x.svg", diagram_alt="Electron shell diagram of a neutral atom X with 2 electrons in the first shell, 8 in the second shell and 3 in the third shell."),
        MC("A particle has 9 protons, 10 neutrons and 10 electrons. Which is it?", [
            C("A neutral atom of mass number 19", why="A neutral atom would have equal protons and electrons."),
            C("A negative ion with mass number 19 and charge 1−", correct=True),
            C("A positive ion with mass number 19 and charge 1+", why="There are more electrons than protons, so the ion is negative, not positive."),
            C("A negative ion with mass number 10 and charge 1−", why="The mass number is protons plus neutrons, which is 19, not 10."),
        ], steps=[S("Mass number", math=r"9 + 10 = 19"),
                  S("Charge", text="10 electrons and 9 protons: one extra electron, so the charge is 1−. This is a fluoride ion, F⁻.")],
           concept="Identifying an ion from its particles", skill="Reasoning", hint="Compare the number of protons with the number of electrons."),
        MC("Which species contains 18 electrons? (Atomic numbers: Ca 20, Na 11, O 8, F 9.)", [
            C("Na⁺", why="Na⁺ has 11 − 1 = 10 electrons."),
            C("O²⁻", why="O²⁻ has 8 + 2 = 10 electrons."),
            C("F⁻", why="F⁻ has 9 + 1 = 10 electrons."),
            C("Ca²⁺", correct=True),
        ], steps=[S("Count for each", text="Na⁺ 11 − 1 = 10. O²⁻ 8 + 2 = 10. F⁻ 9 + 1 = 10. Ca²⁺ 20 − 2 = 18.")],
           concept="Counting electrons in ions", skill="Calculation", hint="Start with the atomic number, then add or remove electrons for the charge."),
    ]))

# ------------------------------------------------------------------ 7. Isotopes and relative atomic mass
SETS.append(practice_set(
    module=MODULE, topic=ATOM,
    title="Isotopes and relative atomic mass",
    lesson="cha-isotopes-relative-atomic-mass",
    questions=[
        MC("Isotopes of an element have", [
            C("different numbers of protons", why="Different numbers of protons would make them different elements."),
            C("the same number of protons and different numbers of neutrons", correct=True),
            C("the same number of neutrons and different numbers of electrons", why="Isotopes have the same number of electrons as protons."),
            C("different numbers of protons and electrons", why="Neither the protons nor the electrons differ in isotopes."),
        ], steps=[S("Recall the definition", text="Isotopes are atoms of the same element, so they have the same number of protons. They differ in the number of neutrons.")],
           concept="Definition of isotopes", skill="Recall", hint="They are atoms of the same element."),
        MC("Why do isotopes of the same element have the same chemical properties?", [
            C("They have the same mass", why="Isotopes have different masses."),
            C("They have the same number of neutrons", why="Isotopes differ in the number of neutrons."),
            C("They are radioactive", why="Many isotopes are not radioactive. Radioactivity does not decide chemical properties."),
            C("They have the same number of electrons", correct=True),
        ], steps=[S("Link properties to electrons", text="Chemical properties depend on the electron arrangement. Isotopes have the same number of electrons, so they react in the same way.")],
           concept="Chemical properties of isotopes", skill="Concept", hint="Which particles take part in chemical reactions?"),
        NUM("How many neutrons are in an atom of carbon-14? (Atomic number of carbon is 6.)", 8,
            steps=[S("Neutrons = mass number − atomic number", math=r"14 - 6 = 8")],
            tolerance=0, unit="", concept="Neutrons in an isotope", skill="Calculation", hint="Subtract the atomic number from the mass number."),
        NUM("Lithium has two isotopes: lithium-6 (7.5%) and lithium-7 (92.5%). Calculate the relative atomic mass of lithium to 1 decimal place.", 6.9,
            steps=[S("Multiply", math=r"6 \times 7.5 = 45 \qquad 7 \times 92.5 = 647.5"),
                   S("Add and divide by 100", math=r"\frac{45 + 647.5}{100} = 6.925"),
                   S("Round", math=r"A_r = 6.9")],
            tolerance=0.05, unit="", concept="Calculating relative atomic mass", skill="Calculation", hint="Multiply each mass number by its percentage, add, then divide by 100."),
        MC("Which statement about chlorine-35 and chlorine-37 is correct?", [
            C("Chlorine-37 has two more neutrons than chlorine-35", correct=True),
            C("Chlorine-37 has two more protons than chlorine-35", why="Both have 17 protons, because both are chlorine."),
            C("Chlorine-37 has two more electrons than chlorine-35", why="Both atoms have 17 electrons."),
            C("They have different chemical properties", why="They have the same electrons, so the same chemical properties."),
        ], steps=[S("Compare", text="Both have 17 protons and 17 electrons. Neutrons: 35 − 17 = 18 and 37 − 17 = 20, so chlorine-37 has 2 more neutrons.")],
           concept="Comparing isotopes of chlorine", skill="Concept", hint="Work out the neutrons in each isotope."),
        MC("The relative atomic mass of chlorine is 35.5, not a whole number. This is because", [
            C("a chlorine atom contains half a neutron", why="Atoms contain whole numbers of particles only."),
            C("chlorine atoms are compared with oxygen", why="Relative atomic mass is compared with carbon-12."),
            C("it is an average of the masses of the isotopes, taking their abundance into account", correct=True),
            C("some chlorine atoms have lost electrons", why="Electrons have almost no mass, so they do not change the relative atomic mass."),
        ], steps=[S("Explain", text="Chlorine is a mixture of isotopes with mass numbers 35 and 37. 35.5 is the weighted average, closer to 35 because chlorine-35 is more common.")],
           concept="Why Ar is not a whole number", skill="Concept", hint="Chlorine has more than one kind of atom."),
        NUM("Element Y has two isotopes, Y-69 and Y-71. Its relative atomic mass is 69.8. What is the percentage of Y-71?", 40,
            steps=[S("Let x be the % of Y-71", math=r"\frac{69(100 - x) + 71x}{100} = 69.8"),
                   S("Simplify", math=r"6900 + 2x = 6980"),
                   S("Solve", math=r"x = 40")],
            tolerance=0.5, unit="%", concept="Finding abundance from Ar", skill="Calculation", hint="Let x be the percentage of the heavier isotope and the other is 100 − x."),
        MC("Which property is different for chlorine-35 and chlorine-37?", [
            C("The way they react with sodium", why="Both react in the same way, because they have the same electrons."),
            C("The mass of the atom", correct=True),
            C("The charge of the nucleus", why="Both nuclei have 17 protons and so the same charge."),
            C("The number of electrons in the outer shell", why="Both have 7 outer electrons."),
        ], steps=[S("Think", text="Only the number of neutrons differs, so only mass and mass-dependent physical properties differ.")],
           concept="Physical differences of isotopes", skill="Application", hint="Only one type of particle differs between isotopes."),
    ]))

# ------------------------------------------------------------------ 8. Electronic configuration and the periodic table
SETS.append(practice_set(
    module=MODULE, topic=CONFIG,
    title="Electronic configuration and the organization of the periodic table",
    lesson="cha-electron-configuration-table",
    questions=[
        MC("What is the maximum number of electrons in the second shell?", [
            C("2", why="2 is the maximum in the first shell."),
            C("6", why="6 is not the capacity of a shell. The second shell holds up to 8."),
            C("8", correct=True),
            C("18", why="18 is the maximum for the third shell in full, but not for the second."),
        ], steps=[S("Recall", text="Shell 1 holds 2. Shell 2 holds 8.")],
           concept="Capacity of shells", skill="Recall", hint="The first shell holds 2; the second holds more."),
        MC("What is the electronic configuration of sodium (atomic number 11)?", [
            C("2,9", why="The second shell holds only 8 electrons."),
            C("2,8,2", why="This adds one electron too many. That is magnesium."),
            C("2,1,8", why="The shells are filled from the inside out, so the outer shell is last."),
            C("2,8,1", correct=True),
        ], steps=[S("Fill the shells", text="2 + 8 = 10 electrons fill shells 1 and 2. The 11th electron goes in shell 3.")],
           concept="Configuration of sodium", skill="Recall", hint="Fill 2, then 8, then see how many are left."),
        MC("The diagram shows an atom of element X. In which group of the periodic table is X?", [
            C("Group I", why="Group I elements have 1 outer electron. X has 3."),
            C("Group III", correct=True),
            C("Group V", why="Group V elements have 5 outer electrons."),
            C("Group VIII", why="X does not have a full outer shell. Noble gases are group 0."),
        ], steps=[S("Find the outer shell", text="The outer (third) shell has 3 electrons."),
                  S("Link to group", text="Group number = number of outer electrons, so X is in group III.")],
           concept="Group from an electron diagram", skill="Interpretation", hint="Count the electrons in the outermost shell only.",
           diagram="f5ch-a-shell-x.svg", diagram_alt="Electron shell diagram of an atom X with 2 electrons in the first shell, 8 in the second and 3 in the third."),
        MC("An element has atoms with three occupied electron shells. In which period is it?", [
            C("Period 3", correct=True),
            C("Period 2", why="Period 2 elements have two occupied shells."),
            C("Group 3", why="The question asks for the period (row), not the group."),
            C("Period 8", why="8 is the maximum number of electrons in the outer shell, not the period."),
        ], steps=[S("Link shells to period", text="Period number = number of occupied shells = 3.")],
           concept="Period from shells", skill="Concept", hint="The row number equals the number of occupied shells."),
        NUM("How many electrons are in the outer shell of sulfur, atomic number 16?", 6,
            steps=[S("Write the configuration", text="Shell 1: 2. Shell 2: 8. Shell 3: 16 − 10 = 6."),
                   S("Answer", text="The configuration is 2,8,6, so there are 6 outer-shell electrons.")],
            tolerance=0, unit="", concept="Outer-shell electrons", skill="Calculation", hint="Fill the first shells before counting what is left."),
        MC("Which two elements are in the same group of the periodic table?", [
            C("Lithium 2,1 and sodium 2,8,1", correct=True),
            C("Carbon 2,4 and nitrogen 2,5", why="They are in the same period but have different outer electrons: group IV and group V."),
            C("Magnesium 2,8,2 and chlorine 2,8,7", why="They are in the same period but different groups."),
            C("Neon 2,8 and sodium 2,8,1", why="These have different numbers of outer electrons."),
        ], steps=[S("Compare outer electrons", text="Lithium and sodium each have 1 outer electron, so both are in group I. They are in different periods because they have different numbers of shells.")],
           concept="Elements in the same group", skill="Reasoning", hint="The group depends on the number of outer electrons."),
        MC("An element has the configuration 2,8,5. What is its valency?", [
            C("5", why="5 is the number of outer electrons. It would need to gain 3 more, so the valency is 3."),
            C("8", why="8 is the full shell. It is not a valency."),
            C("3", correct=True),
            C("2", why="2 is the number of electrons in the first shell."),
        ], steps=[S("Compare with a full shell", text="It has 5 outer electrons and needs 3 more to reach 8."),
                  S("Valency", math=r"8 - 5 = 3")],
           concept="Valency from configuration", skill="Application", hint="How many electrons does it need to make 8?"),
        MC("What is the electronic configuration of the magnesium ion Mg²⁺? (Mg atom: 2,8,2.)", [
            C("2,8,2", why="This is the atom. The ion has lost its two outer electrons."),
            C("2,8,4", why="Losing electrons cannot add to the outer shell."),
            C("2,8,8", why="This would be gaining 6 electrons. Mg forms a positive ion by losing electrons."),
            C("2,8", correct=True),
        ], steps=[S("Lose the outer electrons", text="Mg loses the 2 outer electrons. The ion has the configuration 2,8, the same as neon.")],
           concept="Configuration of a positive ion", skill="Application", hint="A 2+ charge means two electrons are lost from the outer shell."),
    ]))

# ------------------------------------------------------------------ 9. Groups I and II
SETS.append(practice_set(
    module=MODULE, topic=TRENDS,
    title="Group I and Group II metals: properties and trends",
    lesson="cha-groups-one-two",
    questions=[
        MC("Which statement about the group I metals is correct?", [
            C("They have two electrons in the outer shell", why="Two outer electrons describes group II."),
            C("They are hard and have high melting points", why="Group I metals are soft with low melting points."),
            C("They form 2+ ions", why="Group I metals form 1+ ions."),
            C("Each atom has one electron in the outer shell", correct=True),
        ], steps=[S("Recall", text="Group I atoms have one outer electron, which they lose to form 1+ ions.")],
           concept="Outer electrons of group I", skill="Recall", hint="The group number gives the number of outer electrons."),
        MC("Why are lithium, sodium and potassium stored under oil?", [
            C("To make them melt", why="Oil does not melt them. They would melt only at low temperatures."),
            C("To stop them reacting with air and water", correct=True),
            C("To make them harder", why="They are soft. Oil does not change that."),
            C("To stop them floating", why="Floating is not the reason; oil keeps out air and moisture."),
        ], steps=[S("Explain", text="They react quickly with oxygen and water in the air. Oil keeps them away from both.")],
           concept="Storing alkali metals", skill="Recall", hint="Think of what they react with so easily."),
        MC("What colour does a sodium compound give to a flame?", [
            C("Red", why="Red is the flame colour of lithium."),
            C("Lilac", why="Lilac is the flame colour of potassium."),
            C("Golden yellow", correct=True),
            C("Green", why="This is not a flame colour of the group I metals."),
        ], steps=[S("Recall", text="Lithium gives red, sodium golden yellow and potassium lilac.")],
           concept="Flame tests of group I", skill="Recall", hint="Think of the yellow glow when salt falls on a cooking fire."),
        MC("Which products are formed when potassium reacts with water?", [
            C("Potassium hydroxide and hydrogen", correct=True),
            C("Potassium oxide and hydrogen", why="With cold water the metal makes a hydroxide, not an oxide."),
            C("Potassium hydroxide and oxygen", why="The gas is hydrogen, not oxygen."),
            C("Potassium chloride and hydrogen", why="There is no chlorine in water."),
        ], steps=[S("Equation", math=r"2\text{K} + 2\text{H}_2\text{O} \rightarrow 2\text{KOH} + \text{H}_2")],
           concept="Group I with water", skill="Concept", hint="Metal + water gives a metal hydroxide and a gas."),
        MC("Which is the correct balanced equation for calcium and water?", [
            C("Ca + H₂O → CaO + H₂", why="The product with cold water is calcium hydroxide, not the oxide."),
            C("Ca + 2H₂O → CaOH + H₂", why="Calcium forms Ca²⁺, so the formula of the hydroxide is Ca(OH)₂, not CaOH."),
            C("2Ca + H₂O → 2CaOH + H₂", why="Wrong formula and not balanced."),
            C("Ca + 2H₂O → Ca(OH)₂ + H₂", correct=True),
        ], steps=[S("Count the atoms", text="Left: 1 Ca, 4 H, 2 O. Right: 1 Ca, 2 O, 2 H in the hydroxide plus 2 H in H₂, which makes 4 H.")],
           concept="Equation for calcium and water", skill="Calculation", hint="Calcium forms a 2+ ion, so its hydroxide has two OH groups."),
        MC("Why is potassium more reactive than sodium?", [
            C("Potassium has more outer electrons", why="Both have one outer electron."),
            C("Its outer electron is farther from the nucleus and is lost more easily", correct=True),
            C("Potassium atoms are lighter", why="Potassium atoms are heavier. Mass does not decide reactivity."),
            C("Potassium has a higher melting point", why="Potassium has a lower melting point than sodium, and melting point is not the reason."),
        ], steps=[S("Compare", text="Potassium (2,8,8,1) has one more shell than sodium (2,8,1). The outer electron is farther away and held less strongly, so it is lost more easily.")],
           concept="Reactivity trend in group I", skill="Reasoning", hint="Compare the number of shells in the two atoms."),
        NUM("The melting points of lithium, sodium and potassium are about 181 °C, 98 °C and 63 °C. By how many degrees does the melting point fall from lithium to potassium?", 118,
            steps=[S("Subtract", math=r"181 - 63 = 118")],
            tolerance=0, unit="°C", concept="Trend in melting point", skill="Calculation", hint="Subtract the melting point of potassium from that of lithium."),
        MC("Pieces of magnesium and calcium of the same size are placed in separate tubes of dilute hydrochloric acid. Which result is expected?", [
            C("Magnesium fizzes more vigorously", why="Calcium is below magnesium in group II, so it is more reactive."),
            C("Neither reacts", why="Both are reactive metals and release hydrogen from dilute acid."),
            C("Calcium fizzes more vigorously than magnesium", correct=True),
            C("Both react at the same speed", why="Reactivity increases down the group, so the speeds are different."),
        ], steps=[S("Use the trend", text="Calcium is below magnesium, so it loses its outer electrons more easily and reacts faster. Both release hydrogen.")],
           concept="Comparing Mg and Ca", skill="Application", hint="Which metal is lower in group II?"),
    ]))

# ------------------------------------------------------------------ 10. Halogens, noble gases, transition metals
SETS.append(practice_set(
    module=MODULE, topic=TRENDS,
    title="The halogens, the noble gases and the transition metals",
    lesson="cha-halogens-noble-transition",
    questions=[
        MC("What is the appearance of bromine at room temperature?", [
            C("A pale yellow gas", why="This describes fluorine."),
            C("A grey-black solid", why="This describes iodine."),
            C("A red-brown liquid", correct=True),
            C("A colourless gas", why="No halogen is a colourless gas. This describes a noble gas."),
        ], steps=[S("Recall", text="Bromine is a red-brown liquid giving orange-brown vapour.")],
           concept="State and colour of bromine", skill="Recall", hint="Recall the halogen colours, from pale yellow to grey-black."),
        MC("How many electrons are in the outer shell of a halogen atom?", [
            C("1", why="One outer electron is group I."),
            C("7", correct=True),
            C("8", why="Eight is a full shell, found in noble gases."),
            C("2", why="Two outer electrons is group II."),
        ], steps=[S("Link group to electrons", text="Group VII means 7 outer electrons.")],
           concept="Outer electrons of halogens", skill="Recall", hint="The group number gives the outer electrons."),
        MC("Why are the noble gases very unreactive?", [
            C("They have full outer shells", correct=True),
            C("They have only one outer electron", why="One outer electron would make a very reactive group I metal."),
            C("They are all very heavy", why="Helium is very light, yet unreactive. Mass is not the reason."),
            C("They are liquids at room temperature", why="They are gases at room temperature."),
        ], steps=[S("Use electron arrangement", text="A full outer shell is stable. The atoms do not need to gain, lose or share electrons.")],
           concept="Unreactivity of noble gases", skill="Concept", hint="Think about the outer shell."),
        MC("Chlorine water is added to potassium bromide solution. What is seen?", [
            C("Nothing, no reaction occurs", why="Chlorine is more reactive than bromine, so it displaces bromine."),
            C("A black solid forms", why="A black solid is iodine, not bromine."),
            C("The solution turns purple", why="Purple is the colour of iodine vapour. Bromine is orange-brown."),
            C("The colourless solution turns orange-brown", correct=True),
        ], steps=[S("Equation", math=r"\text{Cl}_2 + 2\text{KBr} \rightarrow 2\text{KCl} + \text{Br}_2"),
                  S("Observation", text="Bromine is formed, so the solution turns orange-brown.")],
           concept="Displacement by chlorine", skill="Application", hint="Which halogen is more reactive, chlorine or bromine?"),
        MC("Which mixture will NOT react?", [
            C("Iodine solution and potassium chloride solution", correct=True),
            C("Chlorine water and potassium iodide solution", why="Chlorine is more reactive than iodine, so it displaces it."),
            C("Bromine water and potassium iodide solution", why="Bromine is more reactive than iodine, so it displaces it."),
            C("Chlorine water and potassium bromide solution", why="Chlorine is more reactive than bromine, so it displaces it."),
        ], steps=[S("Check each pair", text="A halogen displaces another only if it is above it in the group. Iodine is below chlorine, so it cannot displace chlorine.")],
           concept="Predicting displacement", skill="Reasoning", hint="A halogen can only displace one that is below it in the group."),
        MC("Which of these is a typical property of a transition metal?", [
            C("It is soft and floats on water", why="This describes group I metals."),
            C("It forms only white compounds", why="Transition metal compounds are often coloured."),
            C("It forms coloured compounds", correct=True),
            C("It has a very low melting point", why="Transition metals have high melting points."),
        ], steps=[S("Recall", text="Transition metals are hard and dense, have high melting points, form coloured compounds and are often catalysts.")],
           concept="Properties of transition metals", skill="Recall", hint="Think of blue copper(II) sulfate."),
        MC("Halogen A displaces halogen B from a solution of its salt. Halogen B displaces halogen C from a solution of its salt. Which is the order of reactivity, from most reactive to least reactive?", [
            C("C, B, A", why="This is the reverse order. A displaces B, so A is more reactive than B."),
            C("B, A, C", why="A displaces B, so A must be more reactive than B."),
            C("A, C, B", why="B displaces C, so B is more reactive than C."),
            C("A, B, C", correct=True),
        ], steps=[S("Use the rule", text="A more reactive halogen displaces a less reactive one. A displaces B, so A > B. B displaces C, so B > C."),
                  S("Order", text="A, B, C.")],
           concept="Order of reactivity from displacement", skill="Reasoning", hint="Write the two comparisons separately, then join them."),
        MC("Why does the reactivity of the halogens decrease down group VII?", [
            C("Atoms lose electrons more easily", why="Halogens react by gaining electrons, not by losing them."),
            C("Atoms get larger, so the nucleus attracts the incoming electron less strongly", correct=True),
            C("Atoms have more outer electrons", why="All halogens have 7 outer electrons."),
            C("Atoms have fewer protons", why="The number of protons increases down the group."),
        ], steps=[S("Explain", text="Halogens react by gaining one electron. Lower in the group, the outer shell is farther from the nucleus and more shielded, so the attraction for an extra electron is weaker.")],
           concept="Halogen reactivity trend", skill="Concept", hint="Halogens react by gaining an electron. How hard is that for a larger atom?"),
    ]))

# ------------------------------------------------------------------ 11. Ionic and metallic bonding
SETS.append(practice_set(
    module=MODULE, topic=BOND,
    title="Ionic bonding and metallic bonding",
    lesson="cha-ionic-metallic-bonding",
    questions=[
        MC("Ionic bonds usually form between", [
            C("two non-metals", why="Two non-metals share electrons and form covalent bonds."),
            C("two metals", why="Two metals form a mixture (alloy) held by metallic bonding."),
            C("a metal and a non-metal", correct=True),
            C("two noble gases", why="Noble gases have full outer shells and do not form bonds."),
        ], steps=[S("Recall", text="A metal atom loses electrons and a non-metal atom gains them, so ions form and attract each other.")],
           concept="Where ionic bonds form", skill="Recall", hint="One atom must lose electrons and the other must gain them."),
        MC("What is the electronic configuration of the chloride ion, Cl⁻? (Cl atom: 2,8,7.)", [
            C("2,8,8", correct=True),
            C("2,8,7", why="This is the neutral chlorine atom."),
            C("2,8,6", why="This would mean the atom lost an electron, not gained one."),
            C("2,8", why="This would be the loss of all seven outer electrons."),
        ], steps=[S("Add an electron", text="Chlorine gains 1 electron: 2,8,7 + 1 gives 2,8,8, a full outer shell.")],
           concept="Configuration of an anion", skill="Application", hint="A 1− ion has gained one electron."),
        MC("What is the formula of calcium chloride, formed from Ca²⁺ and Cl⁻?", [
            C("CaCl", why="The charges 2+ and 1− do not cancel."),
            C("Ca₂Cl", why="This has 4+ and 1−, which do not cancel."),
            C("Ca₂Cl₂", why="This is not in the simplest ratio, and the 1 : 1 ratio is wrong."),
            C("CaCl₂", correct=True),
        ], steps=[S("Balance the charges", text="One Ca²⁺ is 2+. Two Cl⁻ ions are 2−. The charges cancel.")],
           concept="Writing an ionic formula", skill="Calculation", hint="How many Cl⁻ ions balance one Ca²⁺ ion?"),
        MC("What is the formula of aluminium oxide, formed from Al³⁺ and O²⁻?", [
            C("AlO", why="3+ and 2− do not cancel in a 1 : 1 ratio."),
            C("Al₂O₃", correct=True),
            C("Al₃O₂", why="The numbers of the charges have been placed on the wrong ions."),
            C("AlO₃", why="This would give 3+ and 6−."),
        ], steps=[S("Find the lowest common charge", math=r"2 \times 3 = 6 \qquad 3 \times 2 = 6"),
                  S("Formula", text="Two Al³⁺ (6+) and three O²⁻ (6−) give Al₂O₃.")],
           concept="Formula of aluminium oxide", skill="Calculation", hint="Find the smallest number that both 3 and 2 divide into."),
        MC("Which statement describes metallic bonding?", [
            C("Attraction between positive metal ions and a sea of delocalized electrons", correct=True),
            C("Attraction between positive and negative ions", why="This describes ionic bonding."),
            C("A shared pair of electrons between two atoms", why="This describes covalent bonding."),
            C("Attraction between molecules", why="This describes intermolecular forces."),
        ], steps=[S("Recall", text="A metallic bond is the attraction between the positive ions in the lattice and the free electrons around them.")],
           concept="Definition of metallic bonding", skill="Recall", hint="Think of positive ions in a sea of electrons."),
        MC("Why can metals be hammered into different shapes?", [
            C("The ions are held by rigid covalent bonds", why="Metals have no covalent bonds, and rigid bonds would make them brittle."),
            C("The electrons are all fixed in one place", why="The electrons are free to move, which keeps the metal together while the layers slide."),
            C("The metal ions have no charge", why="The metal ions are positive."),
            C("The layers of ions can slide, and the electron sea still holds them together", correct=True),
        ], steps=[S("Explain", text="When hammered, layers of ions slide over each other. The delocalized electrons move with them, so the bonding is not broken.")],
           concept="Malleability of metals", skill="Concept", hint="What happens to the layers of ions when force is applied?"),
        MC("Element X has electronic configuration 2,8,2 and element Y has 2,6. Which is the formula and the bonding of the compound they form?", [
            C("X₂Y, covalent", why="X is a metal, so it forms an ionic compound, and 2+ and 2− balance in a 1 : 1 ratio."),
            C("XY₂, ionic", why="X loses 2 electrons and Y gains 2, so the ratio is 1 : 1, not 1 : 2."),
            C("XY, ionic", correct=True),
            C("XY, covalent", why="X is a metal (group II) and Y is a non-metal (group VI), so the bond is ionic."),
        ], steps=[S("Identify the elements", text="2,8,2 is magnesium (group II, a metal). 2,6 is oxygen (group VI, a non-metal)."),
                  S("Ions", text="Mg²⁺ and O²⁻ balance in a 1 : 1 ratio, so the formula is XY (MgO) and the bond is ionic.")],
           concept="Predicting formula and bonding from configurations", skill="Application", hint="Work out the group of each element and what ion it forms."),
        NUM("How many chloride ions, Cl⁻, are needed to balance the charge of one aluminium ion, Al³⁺?", 3,
            steps=[S("Balance", math=r"3+ \; \text{needs} \; 3 \times (1-)"), S("Answer", text="Three chloride ions, giving AlCl₃.")],
            tolerance=0, unit="", concept="Balancing ionic charges", skill="Calculation", hint="The total positive charge must equal the total negative charge."),
    ]))

# ------------------------------------------------------------------ 12. Covalent and dative bonding
SETS.append(practice_set(
    module=MODULE, topic=BOND,
    title="Covalent bonding and dative covalent bonding",
    lesson="cha-covalent-dative-bonding",
    questions=[
        MC("A covalent bond is", [
            C("the attraction between a positive ion and a negative ion", why="This describes an ionic bond."),
            C("a shared pair of electrons between two atoms", correct=True),
            C("the attraction between metal ions and free electrons", why="This describes a metallic bond."),
            C("a transfer of electrons from one atom to another", why="Transfer of electrons is ionic bonding."),
        ], steps=[S("Recall", text="In a covalent bond, two atoms share a pair of electrons so each gets a full outer shell.")],
           concept="Definition of covalent bond", skill="Recall", hint="Think of the word 'shared'."),
        MC("Which of these compounds contains only covalent bonds?", [
            C("Sodium chloride", why="Sodium chloride is ionic, a metal bonded to a non-metal."),
            C("Magnesium oxide", why="Magnesium oxide is ionic."),
            C("Methane", correct=True),
            C("Potassium bromide", why="Potassium bromide is ionic."),
        ], steps=[S("Check the elements", text="Methane (CH₄) contains only the non-metals carbon and hydrogen, which share electrons.")],
           concept="Recognising covalent compounds", skill="Concept", hint="Look for a compound made of non-metals only."),
        NUM("How many pairs of electrons are shared between the two atoms in a nitrogen molecule, N₂?", 3,
            steps=[S("Count", text="Each N (2,5) needs 3 more electrons to make 8. Each shares 3 electrons, so 3 pairs are shared (a triple bond).")],
            tolerance=0, unit="", concept="Triple bond in nitrogen", skill="Application", hint="How many electrons does each nitrogen atom need to fill its outer shell?"),
        MC("How many lone pairs are on the nitrogen atom in an ammonia molecule, NH₃?", [
            C("1", correct=True),
            C("0", why="N has 5 outer electrons and uses only 3 in bonds, so 2 electrons are left over."),
            C("2", why="This would need four non-bonding electrons. N has only two left after bonding."),
            C("3", why="Three is the number of bonding pairs, not lone pairs."),
        ], steps=[S("Count", text="N has 5 outer electrons. 3 are shared with hydrogen atoms. The remaining 2 form one lone pair.")],
           concept="Lone pairs in ammonia", skill="Application", hint="Subtract the electrons used in bonding from the 5 outer electrons."),
        MC("Which statement about the structure of carbon dioxide is correct?", [
            C("It has two single bonds", why="Carbon needs 4 more electrons, so two single bonds would leave it with only 6."),
            C("It has two triple bonds", why="Triple bonds would give carbon 12 electrons."),
            C("It has one double bond and one single bond", why="The molecule is symmetrical. Both C–O bonds are double."),
            C("It has two double bonds, O=C=O", correct=True),
        ], steps=[S("Count", text="Carbon has 4 outer electrons and each oxygen has 6. Carbon shares 2 pairs with each oxygen, so every atom has 8 outer electrons.")],
           concept="Structure of carbon dioxide", skill="Concept", hint="Carbon needs four more electrons. Two oxygen atoms share them."),
        MC("Which particle contains a dative covalent bond?", [
            C("The ammonia molecule, NH₃", why="All three N–H bonds in NH₃ are ordinary covalent bonds, each from one electron of each atom."),
            C("The ammonium ion, NH₄⁺", correct=True),
            C("The methane molecule, CH₄", why="Each C–H bond uses one electron from each atom."),
            C("The sodium ion, Na⁺", why="Na⁺ is a single ion with no covalent bonds."),
        ], steps=[S("Look for a lone pair donor", text="In NH₄⁺, nitrogen donates its lone pair to H⁺, which has no electrons. This forms a dative bond.")],
           concept="Identifying dative bonds", skill="Concept", hint="Which particle forms when a lone pair attaches to H⁺?"),
        MC("In a molecule of hydrogen chloride, HCl, how many electrons does the chlorine atom have in its outer shell, counting the shared pair?", [
            C("1", why="This is the number of electrons chlorine shares, not its total."),
            C("7", why="This is its number before bonding. The shared pair adds one more."),
            C("8", correct=True),
            C("2", why="This is the number around hydrogen."),
        ], steps=[S("Count", text="Chlorine has 7 outer electrons. The shared pair adds 1, so it has 8, a full outer shell. Hydrogen has 2.")],
           concept="Electrons in HCl", skill="Calculation", hint="Chlorine has 7 outer electrons. How many does the shared pair add to its count?"),
        MC("An element X has the electronic configuration 2,7. It reacts with hydrogen. Which is the formula and the type of bonding?", [
            C("HX, covalent", correct=True),
            C("HX, ionic", why="Both X and H are non-metals, so they share electrons."),
            C("H₂X, covalent", why="X needs only one more electron, so one hydrogen is enough."),
            C("HX₂, ionic", why="Wrong ratio and the bonding is covalent between non-metals."),
        ], steps=[S("Find the electron need", text="X has 7 outer electrons and needs 1 more. Hydrogen needs 1. They share one pair.")],
           concept="Predicting formula and bonding", skill="Application", hint="How many electrons does X need to fill its outer shell?"),
    ]))

# ------------------------------------------------------------------ 13. Intermolecular forces
SETS.append(practice_set(
    module=MODULE, topic=BOND,
    title="Intermolecular forces: van der Waals forces and hydrogen bonding",
    lesson="cha-intermolecular-forces",
    questions=[
        MC("Compared with covalent bonds, intermolecular forces are", [
            C("stronger", why="Covalent bonds are much stronger than the forces between molecules."),
            C("much weaker", correct=True),
            C("the same strength", why="The two kinds of force are very different in strength."),
            C("found only in metals", why="Intermolecular forces act between molecules, not in metals."),
        ], steps=[S("Recall", text="Covalent bonds inside molecules are strong. Intermolecular forces between molecules are weak, which is why simple molecular substances melt at low temperatures.")],
           concept="Strength of intermolecular forces", skill="Recall", hint="Think of why wax melts at a low temperature."),
        MC("When liquid bromine boils, which of these is overcome?", [
            C("The forces between the Br₂ molecules", correct=True),
            C("The covalent bonds in each Br₂ molecule", why="The bond in each Br₂ molecule stays. Bromine vapour still has Br₂ molecules."),
            C("The ionic bonds between bromine atoms", why="There are no ions in bromine."),
            C("The metallic bonds in bromine", why="Bromine is a non-metal and has no metallic bonds."),
        ], steps=[S("Think about boiling", text="When a molecular liquid boils, the molecules separate. The weak forces between them are overcome, but the atoms inside each molecule stay bonded.")],
           concept="What is overcome on boiling", skill="Concept", hint="Does boiling bromine turn Br₂ into Br atoms?"),
        MC("Which substance has hydrogen bonds between its molecules?", [
            C("Methane, CH₄", why="Hydrogen in methane is bonded to carbon, not N, O or F."),
            C("Carbon dioxide, CO₂", why="CO₂ has no hydrogen atoms."),
            C("Water, H₂O", correct=True),
            C("Hydrogen chloride, HCl", why="Hydrogen in HCl is bonded to chlorine, which is not N, O or F."),
        ], steps=[S("Check the rule", text="Hydrogen bonds need H bonded to N, O or F. In water, H is bonded to O.")],
           concept="Recognising hydrogen bonding", skill="Concept", hint="Look for hydrogen bonded to N, O or F."),
        MC("The boiling points of chlorine, bromine and iodine increase in that order. This is because", [
            C("the covalent bond gets stronger", why="The covalent bond inside the molecule is not what is overcome."),
            C("they form hydrogen bonds", why="Halogen molecules contain no H bonded to N, O or F."),
            C("their atoms become more reactive", why="Reactivity decreases down the group, and it has nothing to do with boiling points."),
            C("the molecules get larger, so the van der Waals forces get stronger", correct=True),
        ], steps=[S("Link size and force", text="Larger molecules have more electrons, which gives stronger van der Waals forces.")],
           concept="Trend in halogen boiling points", skill="Concept", hint="What changes in the molecules as you go down the group?"),
        NUM("Water boils at 100 °C and hydrogen sulfide, H₂S, boils at −60 °C. By how many degrees is the boiling point of water higher?", 160,
            steps=[S("Subtract", math=r"100 - (-60) = 160")],
            tolerance=0, unit="°C", concept="Effect of hydrogen bonding on boiling point", skill="Calculation", hint="Subtract a negative number: it increases the difference."),
        MC("Why is ice less dense than liquid water?", [
            C("Ice has more water molecules than water", why="Equal masses have the same number of molecules. The difference is in the spacing."),
            C("Hydrogen bonds hold the molecules in an open arrangement in ice", correct=True),
            C("The covalent bonds are longer in ice", why="The covalent bonds inside the molecules do not change."),
            C("Ice particles move faster", why="Ice particles only vibrate. They move less than in liquid water."),
        ], steps=[S("Explain", text="In ice, each molecule forms hydrogen bonds in a fixed open pattern with empty space. In liquid water the molecules are slightly closer, so ice is less dense.")],
           concept="Why ice floats", skill="Reasoning", hint="Think of the pattern of hydrogen bonds in the solid."),
        MC("Methane boils at about −162 °C and water boils at 100 °C. Which statement explains this?", [
            C("Water molecules form hydrogen bonds, which need much more energy to overcome", correct=True),
            C("Methane has stronger covalent bonds", why="Covalent bonds are not broken on boiling."),
            C("Water has stronger van der Waals forces only", why="The main reason is hydrogen bonding, which is stronger than van der Waals forces."),
            C("Methane molecules are larger than water molecules", why="The difference is the hydrogen bonding. Methane has a similar size to water."),
        ], steps=[S("Compare the forces", text="Water has hydrogen bonds between molecules. Methane has only weak van der Waals forces. More energy is needed to separate water molecules.")],
           concept="Comparing boiling points of methane and water", skill="Reasoning", hint="What special force acts between water molecules?"),
        MC("Which statement about van der Waals forces is correct?", [
            C("They are found only in water", why="They are found between all molecules."),
            C("They are stronger than covalent bonds", why="They are much weaker."),
            C("They act between all molecules and get stronger as the molecules get larger", correct=True),
            C("They only act between ions", why="Ions attract by ionic bonds. Van der Waals forces act between molecules."),
        ], steps=[S("Recall", text="All molecules have van der Waals forces. They are weak, and stronger for larger molecules.")],
           concept="Van der Waals forces", skill="Recall", hint="Do all molecules have them, or only some?"),
    ]))

# ------------------------------------------------------------------ 14. Structure and properties of solids
SETS.append(practice_set(
    module=MODULE, topic=SOLIDS,
    title="Giant ionic, giant covalent and simple molecular structures",
    lesson="cha-structure-properties-solids",
    questions=[
        MC("Which substance has a giant ionic lattice?", [
            C("Iodine", why="Iodine is a simple molecular solid."),
            C("Diamond", why="Diamond is a giant covalent structure."),
            C("Sodium chloride", correct=True),
            C("Carbon dioxide", why="Solid carbon dioxide is a simple molecular solid."),
        ], steps=[S("Match the structure", text="Sodium chloride is a metal bonded to a non-metal, in a lattice of Na⁺ and Cl⁻ ions.")],
           concept="Identifying a giant ionic lattice", skill="Recall", hint="Look for a metal combined with a non-metal."),
        MC("Why does solid sodium chloride not conduct electricity?", [
            C("It contains no charged particles", why="It contains ions. They are charged but fixed."),
            C("Its ions are fixed in the lattice and cannot move", correct=True),
            C("Its electrons are all held tightly", why="The charge in an ionic compound is carried by ions, not electrons."),
            C("It is made of molecules", why="Sodium chloride is a lattice of ions, not molecules."),
        ], steps=[S("Explain", text="To conduct, charged particles must be free to move. In the solid the ions are held in fixed positions.")],
           concept="Conductivity of solid ionic compounds", skill="Concept", hint="What must be free to move for a substance to conduct?"),
        MC("Why can graphite conduct electricity?", [
            C("It contains ions that are free to move", why="Graphite has no ions. It is made of carbon atoms."),
            C("Its layers can slide over each other", why="This explains why graphite is soft, not why it conducts."),
            C("It has a very high melting point", why="Diamond also has a very high melting point but does not conduct."),
            C("Each carbon atom has one delocalized electron free to move", correct=True),
        ], steps=[S("Count electrons", text="Each carbon forms 3 bonds in its layer, using 3 of its 4 outer electrons. The fourth is delocalized and carries charge.")],
           concept="Why graphite conducts", skill="Concept", hint="Count how many of carbon's four outer electrons are used in bonds."),
        MC("Why is diamond very hard?", [
            C("Each carbon atom is bonded to four others by strong covalent bonds in a rigid network", correct=True),
            C("It is made of layers of carbon atoms that slide over each other", why="This describes graphite."),
            C("Its carbon atoms are held by weak forces", why="The bonds in diamond are strong."),
            C("It contains free electrons", why="Diamond has no free electrons."),
        ], steps=[S("Explain", text="Every atom is held rigidly by 4 strong covalent bonds, and the bonds extend through the whole crystal.")],
           concept="Hardness of diamond", skill="Concept", hint="Think of the number of bonds on each carbon atom."),
        MC("Substance X is a hard solid that melts above 3000 °C. It does not dissolve in water and does not conduct electricity in any state. What type of structure does it have?", [
            C("Simple molecular", why="A simple molecular substance would melt at a low temperature."),
            C("Giant covalent", correct=True),
            C("Giant ionic", why="A giant ionic compound would conduct when molten."),
            C("Metallic", why="A metal would conduct electricity."),
        ], steps=[S("Use the clues", text="A very high melting point needs strong bonds throughout the structure. No conduction in any state rules out ions and free electrons. So it is a giant covalent structure.")],
           concept="Identifying a structure from properties", skill="Reasoning", hint="Which structures have a very high melting point and do not conduct?"),
        NUM("How many other carbon atoms is each carbon atom bonded to in diamond?", 4,
            steps=[S("Recall", text="Carbon has 4 outer electrons. In diamond each atom shares all four, forming four single covalent bonds with four other carbon atoms.")],
            tolerance=0, unit="", concept="Bonding in diamond", skill="Recall", hint="Carbon has four outer electrons."),
        MC("Substance Z melts at 114 °C, does not conduct electricity as a solid or liquid, and dissolves poorly in water. Which type of structure is likely?", [
            C("Simple molecular", correct=True),
            C("Giant ionic", why="A giant ionic compound would have a high melting point and conduct when molten."),
            C("Giant covalent", why="A giant covalent substance would have a very high melting point."),
            C("Metallic", why="A metal would conduct electricity in the solid and liquid."),
        ], steps=[S("Use the clues", text="Low melting point means weak forces between particles. No conduction means no ions or free electrons. So Z is a simple molecular substance (like iodine).")],
           concept="Identifying simple molecular substances", skill="Reasoning", hint="A low melting point means weak forces between the particles."),
        MC("Four substances have these properties. P: melts at 1085 °C; conducts as a solid and as a liquid. Q: melts at 801 °C; conducts only when molten or dissolved. R: melts at 3550 °C; does not conduct. S: melts at 44 °C; does not conduct. Which is a giant covalent substance?", [
            C("P", why="P conducts as a solid, so it is a metal."),
            C("Q", why="Q conducts when molten or dissolved, so it is ionic."),
            C("S", why="S has a low melting point, so it is simple molecular."),
            C("R", correct=True),
        ], steps=[S("Classify each", text="P is a metal. Q is giant ionic. S is simple molecular. R has a very high melting point and does not conduct, which fits a giant covalent structure.")],
           concept="Classifying structures from data", skill="Interpretation", hint="Which one has a very high melting point and cannot conduct in any state?"),
    ]))
