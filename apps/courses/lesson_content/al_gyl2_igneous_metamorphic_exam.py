"""A Level Geology (0755), Lower Sixth: Igneous Petrology, Metamorphic Petrology and the Examination module.

11 topic lessons and 3 examination lessons (slug prefix gyl2-), one practice set each (see the practice file of the same name).
Content follows KKEVO's master curriculum blueprint (module lines L6M4 and L6M5) and the Board's 2023 subject report for exam
structure and common errors; it is not a Board syllabus booklet. Phase diagrams, the facies grid and the P-T-t path are teaching
diagrams (schematic; boundaries and values differ slightly between textbooks). Calculations (pressure and depth, geothermal
gradients, partial melting, Stokes' law, mass balance, lever rule, QAPF normalisation, slab geometry, exhumation rates) were
checked by script.
"""

from .dsl import *  # noqa: F403

COURSE = ("geology", "lower-sixth")

M_IGN = "Igneous Petrology"
M_MET = "Metamorphic Petrology"
M_EXAM = "Examination"

LESSONS = []

# ------------------------------------------------------------------ 1. Magma generation and partial melting
LESSONS.append(lesson(
    module=M_IGN,
    topic="Magma generation and partial melting",
    title="Where magma comes from: the solidus, three ways to melt rock and partial melting",
    slug="gyl2-magma-generation-partial-melting",
    minutes=24,
    summary="The mantle is almost entirely solid; magma forms only where rock crosses its solidus by decompression, by the addition of water or by heating, and it forms by partial melting, which makes melts richer in silica and incompatible elements than their source.",
    objectives=[
        "Explain why the mantle is solid even though it is very hot, using the geotherm and the solidus",
        "Describe decompression melting, flux (water-induced) melting and melting by heat transfer, and name where each happens",
        "Explain partial melting and why the first melt differs in composition from its source rock",
        "Calculate lithostatic pressure and the enrichment of an incompatible element in a partial melt",
    ],
    key_concepts=["Magma", "Geotherm", "Solidus", "Liquidus", "Decompression melting", "Flux melting", "Partial melting", "Incompatible element", "Primary magma"],
    blocks=[
        H("Introduction"),
        T("Mount Cameroon erupted in 1999 and again in 2000, sending basalt lava down its slopes towards villages near Buea and Limbe. "
          "Where did that molten rock come from? A common answer is 'from a layer of liquid under the crust'. That answer is wrong. "
          "Seismology shows that S waves travel through the crust and the mantle all the way to the outer core, and S waves cannot pass through a liquid. "
          "So the mantle is solid. Magma forms only in special places and in small amounts. This lesson explains how."),
        D("**Magma** is molten rock below the surface. It is a mixture of a silicate **melt**, dissolved **volatiles** (mainly water, carbon dioxide and sulphur gases) and, usually, some **crystals**. "
          "**Lava** is magma that has reached the surface and lost most of its gas.", title="Magma"),
        H("Geotherm, solidus and liquidus"),
        D("The **geotherm** is the curve of temperature against depth in the Earth. The **solidus** is the temperature at which a rock begins to melt at a given pressure. "
          "The **liquidus** is the temperature at which it becomes completely molten. Between the two the rock is a mush of crystals and melt.", title="Three curves"),
        T("Pressure raises the melting point of dry rock: atoms are squeezed together and need more energy to break free. So the solidus of dry mantle rock (peridotite) rises with depth. "
          "Under normal conditions the geotherm stays at a lower temperature than the solidus at every depth, so the mantle is hot but solid (Figure 1). "
          "To make magma, a piece of rock must reach the melt field: either the rock moves to a point where it is hotter than its solidus, or the solidus moves to a lower temperature."),
        IMG("algyl2-melting.svg", alt="Graph of depth against temperature showing the geotherm to the left of the dry peridotite solidus, a dashed wet solidus at lower temperature, an arrow of rising mantle crossing the dry solidus and an arrow showing the effect of adding water",
            caption="Figure 1. The geotherm, the dry peridotite solidus and the wet solidus (schematic). Arrow 1: hot mantle rises and crosses the solidus. Arrow 2: adding water lowers the solidus."),
        H("Three ways to melt rock"),
        KEY("How rock reaches its solidus", "Each mechanism has its own plate setting.", cards=[
            ["1. Decompression melting", "Hot mantle rises. It cools only a little (about 0.3 to 0.5 °C per km, because it expands), but the pressure falls fast, so the solidus falls more quickly than the rock cools. The rock crosses the solidus and partly melts. Setting: mid-ocean ridges, continental rifts, mantle plumes (hotspots)."],
            ["2. Flux melting", "Water released from a subducting slab rises into the hot mantle wedge above it. Water breaks silicon-oxygen bonds and lowers the solidus by several hundred degrees, so the mantle melts without any heating. Setting: subduction zones, island arcs, active continental margins."],
            ["3. Heat transfer", "Hot basaltic magma rising from the mantle ponds at the base of the continental crust or intrudes it. The heat it gives up melts the surrounding crust, which has a lower solidus than peridotite. Setting: above subduction zones, in continental rifts and in thickened crust during collision."],
        ]),
        MISTAKE("Saying that magma comes from a molten mantle", "The mantle is solid (S waves pass through it). Magma forms locally, by partial melting, where decompression, water or heat brings rock above its solidus. The low-velocity zone in the upper mantle contains at most a very small fraction of melt."),
        H("Partial melting"),
        D("**Partial melting** is the melting of only part of a rock. Because a rock is a mixture of minerals with different melting temperatures, the first melt to form takes the components that melt most easily, and the solid left behind (the **residue**) is enriched in minerals with high melting points.", title="Partial melting"),
        T("When mantle peridotite (olivine, pyroxenes and a little garnet or spinel) melts by 5 to 25%, the melt has the composition of **basalt**. The residue is richer in olivine and poorer in silica, calcium, aluminium and sodium. "
          "A melt formed directly from the mantle in this way is a **primary magma**. Partial melting of continental crust (which is richer in silica and water) gives more silica-rich melts: granite and rhyolite magmas. "
          "So one general rule holds: **the melt is always richer in silica and in low-melting components than its source**."),
        D("An **incompatible element** does not fit easily into the crystal structures of the minerals in the source (for example potassium, rubidium, lanthanum, uranium and thorium). During melting it goes almost entirely into the melt. "
          "A **compatible element** (such as nickel and chromium in olivine and pyroxene) stays in the residue.", title="Compatible and incompatible elements"),
        F(r"C_L = \frac{C_0}{F} \qquad \text{(perfectly incompatible element, batch melting)}", title="Concentration in the melt"),
        T("Here $C_0$ is the concentration in the source, $C_L$ the concentration in the melt and $F$ the fraction melted (0 to 1). The smaller the degree of melting, the more concentrated the incompatible elements are in the melt. "
          "This is why basalts formed by small degrees of melting (alkali basalts, such as many of those of the Cameroon Volcanic Line) are richer in potassium and sodium than basalts formed by large degrees of melting at mid-ocean ridges (tholeiites)."),
        EX("Worked example 1: lithostatic pressure", intro="Calculate the pressure at a depth of 30 km beneath a crust and upper mantle of average density 3000 kg m⁻³ (g = 9.8 m s⁻²). Give the answer in GPa.", steps=[
            S("Formula", math=r"P = \rho g h"),
            S("Substitute (h in metres)", math=r"P = 3000 \times 9.8 \times 30\,000 = 8.82 \times 10^{8} \text{ Pa}"),
            S("Convert", math=r"8.82 \times 10^{8} \text{ Pa} = 0.88 \text{ GPa}", text="Roughly 1 GPa for every 33 to 35 km of rock: a useful rule for reading phase diagrams."),
        ], check=r"3000 \times 9.8 \times 30000 = 882\,000\,000"),
        EX("Worked example 2: will the mantle melt?", intro="A geotherm has a surface temperature of 25 °C and rises by 25 °C per km. The dry peridotite solidus in Figure 1 follows T = 1120 + 3.3z (°C, z in km). Is mantle rock at 40 km depth molten?", steps=[
            S("Temperature at 40 km", math=r"T = 25 + 25 \times 40 = 1025 {}^\circ\text{C}"),
            S("Solidus at 40 km", math=r"T_s = 1120 + 3.3 \times 40 = 1252 {}^\circ\text{C}"),
            S("Compare", text="1025 °C is below 1252 °C, so dry rock stays solid. It would melt only if it rose quickly (decompression) or if water lowered its solidus below 1025 °C."),
        ], check=r"1025 < 1252"),
        EX("Worked example 3: enrichment of an incompatible element", intro="Mantle peridotite contains 1 ppm of lanthanum, which behaves as a perfectly incompatible element. Find the lanthanum content of the melt for 5% and for 20% melting.", steps=[
            S("5% melting", math=r"C_L = \frac{1}{0.05} = 20 \text{ ppm}"),
            S("20% melting", math=r"C_L = \frac{1}{0.20} = 5 \text{ ppm}"),
            S("Interpret", text="The smaller melt fraction is four times richer in lanthanum. Low-degree melts carry a strong incompatible-element signal."),
        ], check=r"0.05 \times 20 = 1"),
        H("Evaluating the model"),
        T("The geotherm-solidus model explains why magma is found at ridges, rifts, hotspots and subduction zones but not under old, stable continents. Its limits: real solidus curves depend on the exact rock composition and on the amount of water and carbon dioxide, "
          "and the simple $C_L = C_0/F$ rule ignores the small amount of each element that does enter the minerals. "
          "For the Cameroon Volcanic Line, geologists still debate whether a mantle plume or decompression along old zones of weakness in the lithosphere causes the melting (check your textbook)."),
        QUIZ("Why does hot mantle rising beneath a mid-ocean ridge begin to melt?", ["Friction between the plates heats it above its liquidus", "Its pressure falls faster than it cools, so it crosses its solidus", "Sea water reaches it and lowers its solidus", "It is heated by the radioactive decay of the oceanic crust"], 1,
             "Decompression: the solidus falls with decreasing pressure while the rising rock keeps most of its heat.", hint="What changes most as rock rises?",
             feedback=["Friction is very small, and rock begins to melt at the solidus, not the liquidus.", "", "Water is the main cause at subduction zones; the ridge mantle melts by decompression.", "Oceanic crust is poor in radioactive elements and lies above the melting zone."]),
        QUIZ("A peridotite melts by 10%. Which statement about the melt is correct?", ["It has the same composition as the peridotite", "It is richer in silica and incompatible elements than the peridotite", "It is richer in nickel and chromium than the peridotite", "It is richer in olivine than the peridotite"], 1,
             "Partial melts take the low-melting components and the incompatible elements; the residue keeps olivine, nickel and chromium.", hint="Which components melt first?",
             feedback=["Only total melting gives the same composition.", "", "Nickel and chromium are compatible: they stay in olivine and pyroxene in the residue.", "Olivine has a high melting point and stays in the residue."]),
        TIP("Magma generation appears in Paper 1 (mechanisms, compatible and incompatible elements, simple calculations) and in Paper 2 essays on igneous activity and plate tectonics. In an essay, always link each melting mechanism to a named plate setting and give an example.", title="Exam link"),
        PQ("(a) Explain why the upper mantle is solid although its temperature exceeds 1200 °C. (b) Describe two processes that cause it to melt, naming a setting for each.",
           "(a) The melting point (solidus) of peridotite rises with pressure. At each depth the geotherm is at a lower temperature than the solidus, so the rock does not melt; S waves pass through the mantle, which confirms it is solid. "
           "(b) Decompression melting: at mid-ocean ridges and in mantle plumes, hot mantle rises; pressure falls faster than temperature, so it crosses the solidus. Flux melting: at subduction zones, water from the dehydrating slab enters the mantle wedge and lowers its solidus, so it melts at the same temperature."),
        PQ("Calculate the depth at which the pressure is 1.5 GPa if the average density of the overlying rock is 3300 kg m⁻³ (g = 9.8 m s⁻²).",
           "h = P ÷ (ρg) = 1.5 × 10⁹ ÷ (3300 × 9.8) = 46 400 m, about 46 km."),
        PQ("A mantle source contains 0.5 ppm of thorium (perfectly incompatible). A basalt formed from it contains 5 ppm of thorium. Estimate the degree of partial melting and state what kind of basalt is likely.",
           "F = C₀ ÷ C_L = 0.5 ÷ 5 = 0.10, so about 10% melting. A fairly low degree of melting gives a basalt relatively rich in incompatible elements, such as an alkali basalt rather than a mid-ocean ridge tholeiite."),
        PQ("Plan an essay: 'Magma is generated in only a few tectonic settings. Discuss.'",
           "Introduction: mantle and crust are solid; magma requires crossing the solidus. Point 1: decompression at ridges and rifts (example: Mid-Atlantic Ridge, East African Rift). Point 2: plumes and hotspots (Hawaii; the debated case of the Cameroon Volcanic Line). "
           "Point 3: flux melting at subduction zones (Andes, Japan). Point 4: crustal melting by heat transfer and in thickened collision zones (Himalayan granites). Evaluation: the stable interiors of continents (cratons) rarely produce magma because none of the mechanisms operates; the model depends on solidus curves that vary with composition and volatiles. Conclusion."),
        SUM("The mantle is solid: the geotherm normally lies below the solidus of peridotite.",
            "Rock melts when decompression (ridges, rifts, plumes), added water (subduction zones) or added heat (crust above hot magma) brings it above its solidus.",
            "Partial melting gives a melt richer in silica, alkalis and incompatible elements than its source; peridotite gives basalt, crust gives granite.",
            "Lithostatic pressure P = ρgh, about 1 GPa per 33 to 35 km.",
            "For a perfectly incompatible element C_L = C₀ ÷ F: small degrees of melting give strongly enriched melts."),
    ],
))

# ------------------------------------------------------------------ 2. Magmatic differentiation
LESSONS.append(lesson(
    module=M_IGN,
    topic="Magmatic differentiation",
    title="Magmatic differentiation: fractional crystallisation, Bowen's series, assimilation and mixing",
    slug="gyl2-magmatic-differentiation",
    minutes=25,
    summary="One parent magma can give a whole range of igneous rocks: fractional crystallisation (guided by Bowen's reaction series), crystal settling, filter pressing, assimilation of country rock, magma mixing and liquid immiscibility change the composition of the melt.",
    objectives=[
        "Define magmatic differentiation and explain fractional crystallisation using Bowen's reaction series",
        "Describe the continuous and discontinuous series accurately, naming the plagioclase feldspars in order",
        "Describe crystal settling, filter pressing, assimilation, magma mixing and liquid immiscibility, with evidence for each",
        "Use Stokes' law and a simple mass balance to show how the melt composition changes",
    ],
    key_concepts=["Differentiation", "Fractional crystallisation", "Bowen's reaction series", "Continuous series", "Discontinuous series", "Crystal settling", "Cumulate", "Assimilation", "Magma mixing", "Zoning"],
    blocks=[
        H("Introduction"),
        T("Basalt, andesite and rhyolite can all erupt from the same volcanic region, sometimes in the same sequence of lavas. The volcanoes of the Cameroon Volcanic Line, for example, have produced basalts and also more evolved trachytes and phonolites. "
          "Partial melting of the mantle gives basalt, so how do the other rocks form? The answer is that a magma changes as it cools. This process is called **magmatic differentiation**."),
        D("**Magmatic differentiation** is any process by which a single parent magma gives rise to magmas or rocks of different composition.", title="Differentiation"),
        H("Fractional crystallisation and Bowen's series"),
        T("As a magma cools, minerals crystallise in a fairly regular order. N. L. Bowen worked this order out by experiment in the early twentieth century. "
          "Early crystals take more magnesium, iron and calcium and less silica than the melt contains, so if they are **separated** from the melt, the remaining liquid becomes richer in silica, sodium and potassium. "
          "This is **fractional crystallisation**: the crystals are removed (fractionated) and can no longer react with the liquid."),
        IMG("f5gly1-bowen.svg", alt="Bowen's reaction series: the discontinuous series olivine, pyroxene, amphibole and biotite on the left, the continuous plagioclase series from calcium-rich to sodium-rich on the right, joining to potassium feldspar, muscovite and quartz",
            caption="Figure 1. Bowen's reaction series. High temperature at the top, low temperature at the bottom."),
        KEY("Two branches, then one", "Learn the minerals in order and the meaning of each branch.", cards=[
            ["Discontinuous series (left)", "Ferromagnesian minerals: olivine, pyroxene, amphibole, biotite. Each reacts with the melt to give a new mineral with a different silicate structure (isolated tetrahedra, single chains, double chains, sheets). Each step is a distinct phase."],
            ["Continuous series (right)", "Plagioclase feldspar, all with the same framework structure. The composition changes gradually from calcium-rich anorthite through bytownite, labradorite, andesine and oligoclase to sodium-rich albite."],
            ["Low-temperature end", "The branches join. The last minerals to crystallise are orthoclase (potassium feldspar), muscovite and quartz. The two branches run independently and at the same time, not one after the other."],
        ]),
        T("A rock contains the minerals that crystallised together over a temperature range: olivine with calcium-rich plagioclase (gabbro, basalt); hornblende with andesine (diorite, andesite); quartz, orthoclase, sodium-rich plagioclase and micas (granite, rhyolite). "
          "If the early crystals stay in contact with the melt, they react and change (olivine to pyroxene, calcium-rich to sodium-rich plagioclase). If the reaction is incomplete, it leaves evidence: **reaction rims** of pyroxene around olivine, and **zoned plagioclase** with a calcium-rich core and a sodium-rich rim."),
        MISTAKE("Mixing up the two branches or the plagioclase names", "The Board's 2023 report says many candidates mixed up the continuous and discontinuous series, confused Bowen's series with the rock cycle, and misspelled the plagioclase names. Learn the order anorthite, bytownite, labradorite, andesine, oligoclase, albite, and spell them correctly. The ferromagnesian minerals are the discontinuous series."),
        H("How crystals are separated from the melt"),
        KEY("Separation mechanisms", "Fractional crystallisation needs a way to remove crystals.", cards=[
            ["Crystal settling", "Dense early crystals such as olivine and pyroxene sink to the floor of the magma chamber. They pile up as a **cumulate**, often in layers. Light crystals (plagioclase) may float. Example: layered gabbro intrusions such as the Skaergaard (Greenland) and the Bushveld (South Africa)."],
            ["Filter pressing", "When a crystal mush is squeezed (for example by tectonic stress), the liquid is pressed out from between the crystals and moves away, like water from a squeezed sponge."],
            ["Flow differentiation", "In a narrow dyke or sill, crystals move towards the centre of the flow, away from the walls, so the centre becomes richer in early crystals."],
            ["Wall crystallisation", "Crystals grow on the cool walls and roof of the chamber, leaving the more evolved melt in the middle."],
        ]),
        F(r"v = \frac{2 \Delta\rho \, g \, r^2}{9 \eta}", title="Stokes' law: settling velocity of a crystal"),
        T(r"Here $\Delta\rho$ is the density difference between the crystal and the melt (kg m⁻³), $r$ the crystal radius (m) and $\eta$ the viscosity of the melt (Pa s). "
          "Crystal settling works well in hot, runny basaltic magma (viscosity about 10 to 100 Pa s) but very poorly in sticky granitic magma (about 10⁵ Pa s or more)."),
        EX("Worked example 1: crystal settling", intro="An olivine crystal of radius 0.5 mm is 600 kg m⁻³ denser than the surrounding basaltic melt of viscosity 100 Pa s (g = 9.8 m s⁻²). Calculate its settling velocity in metres per day. Repeat for a granitic melt of viscosity 10⁵ Pa s.", steps=[
            S("Basaltic melt", math=r"v = \frac{2 \times 600 \times 9.8 \times (5 \times 10^{-4})^2}{9 \times 100} = 3.27 \times 10^{-6} \text{ m s}^{-1}"),
            S("Per day", math=r"3.27 \times 10^{-6} \times 86\,400 = 0.28 \text{ m per day}"),
            S("Granitic melt", math=r"v = 3.27 \times 10^{-9} \text{ m s}^{-1} \approx 0.0003 \text{ m per day}", text="A thousand times slower: settling cannot separate crystals effectively in viscous silica-rich magma."),
        ], check=r"2 \times 600 \times 9.8 \times 2.5\times10^{-7} \div 900 = 3.27\times 10^{-6}"),
        EX("Worked example 2: mass balance", intro="A basaltic magma contains 50% SiO₂. Olivine containing 40% SiO₂ crystallises and is removed until it makes up 30% of the original mass. What is the SiO₂ content of the remaining melt?", steps=[
            S("Silica in 100 g of magma", math=r"50 \text{ g}"),
            S("Silica removed in 30 g of olivine", math=r"0.30 \times 40 = 12 \text{ g}"),
            S("Silica left in 70 g of melt", math=r"\frac{50 - 12}{70} \times 100 = 54.3\%", text="Removing a mineral poorer in silica than the melt makes the melt richer in silica."),
        ], check=r"0.3 \times 40 + 0.7 \times 54.29 = 50"),
        H("Other ways a magma changes"),
        KEY("Open-system processes", "Each leaves its own evidence.", cards=[
            ["Assimilation (contamination)", "Hot magma melts or dissolves the country rock it passes through and absorbs it. Evidence: partly digested **xenoliths** (fragments of country rock) and unusual compositions. Heat for melting comes from crystallisation, so assimilation and fractional crystallisation often happen together."],
            ["Magma mixing", "Two magmas of different composition meet and mix, for example basalt injected into a granite chamber. Evidence: blobs of one rock in the other, crystals that are out of equilibrium (resorbed quartz in a basalt) and reversed zoning in plagioclase."],
            ["Liquid immiscibility", "Some melts separate into two liquids that do not mix, like oil and water. A sulphide liquid can separate from a basaltic melt and collect nickel-copper ore. It is a minor process for silicate rocks."],
        ]),
        T("**Evaluation.** Fractional crystallisation explains the common series basalt, andesite, dacite, rhyolite and the layered cumulates of large intrusions. But it has limits: to make a small amount of granite from basalt, about 90% of the magma must crystallise first, which would leave huge volumes of gabbro and cumulates. "
          "Large granite batholiths are therefore better explained by partial melting of continental crust. In most real magma systems, partial melting, fractional crystallisation, assimilation and mixing all play a part."),
        QUIZ("Which list gives the plagioclase feldspars in the order in which they crystallise from a cooling basaltic magma?", ["Albite, oligoclase, andesine, labradorite, bytownite, anorthite", "Anorthite, bytownite, labradorite, andesine, oligoclase, albite", "Anorthite, labradorite, bytownite, oligoclase, andesine, albite", "Olivine, pyroxene, amphibole, biotite, orthoclase, quartz"], 1,
             "The continuous series runs from calcium-rich anorthite at high temperature to sodium-rich albite at low temperature.", hint="Which end member forms at the highest temperature?",
             feedback=["This is the reverse order: albite is the low-temperature end member.", "", "Labradorite and bytownite, and andesine and oligoclase, are swapped.", "That is the discontinuous series and the final minerals, not the plagioclase series."]),
        QUIZ("A dolerite sill shows a layer rich in olivine crystals just above its lower contact. Which process best explains this?", ["Assimilation of the floor rock", "Crystal settling of dense olivine", "Liquid immiscibility", "Magma mixing with a granitic melt"], 1,
             "Olivine is denser than basaltic melt and sinks towards the floor, forming a cumulate layer.", hint="Where would dense crystals collect?",
             feedback=["Assimilation would add country rock material, not concentrate olivine.", "", "Immiscibility separates two liquids, not olivine crystals.", "Mixing with granite would make the magma more silica-rich, not richer in olivine."]),
        TIP("Bowen's reaction series is a favourite in Paper 2: draw it (two labelled branches joining at the low-temperature end), explain the difference between the continuous and discontinuous series, and link it to fractional crystallisation. In Paper 1, expect questions on the order of crystallisation and evidence for differentiation.", title="Exam link"),
        PQ("Draw and describe Bowen's reaction series and explain how it accounts for the formation of different igneous rocks from one basaltic magma.",
           "Diagram: left branch olivine, pyroxene, amphibole, biotite (discontinuous); right branch anorthite, bytownite, labradorite, andesine, oligoclase, albite (continuous); joined at the bottom by orthoclase, muscovite, quartz; temperature arrow from high (top) to low. "
           "Description: the discontinuous series is a sequence of ferromagnesian minerals, each a different structure formed by reaction with the melt; the continuous series is a solid solution whose composition changes gradually from calcium-rich to sodium-rich. "
           "Explanation: if early crystals are removed (fractional crystallisation), the melt becomes richer in silica, sodium and potassium; basalt and gabbro form from early stages, andesite and diorite from middle stages, and granite and rhyolite from the residual melt."),
        PQ("A melt contains 55% SiO₂. Plagioclase with 52% SiO₂ crystallises and is removed until it is 25% of the original mass. Calculate the SiO₂ content of the remaining melt and comment.",
           "Silica in 100 g = 55 g; removed = 0.25 × 52 = 13 g; remaining melt = (55 − 13) ÷ 75 × 100 = 56%. The melt becomes only slightly richer in silica, because plagioclase has a silica content close to that of the melt. Removing olivine or magnetite would change the melt more."),
        PQ("Give two pieces of evidence, visible in hand specimen or thin section, that a magma has assimilated country rock or mixed with another magma.",
           "Assimilation: partly melted or reacted xenoliths of country rock; minerals unusual for the rock type (for example garnet or cordierite in a basic rock). Mixing: rounded blobs (enclaves) of a darker rock in a lighter one; quartz or feldspar crystals with corroded (resorbed) outlines; plagioclase with reversed zoning."),
        SUM("Differentiation turns one parent magma into rocks of different compositions.",
            "Fractional crystallisation removes early, silica-poor, Mg-Fe-Ca-rich minerals, so the melt becomes richer in silica, Na and K.",
            "Bowen's series: discontinuous olivine, pyroxene, amphibole, biotite; continuous anorthite, bytownite, labradorite, andesine, oligoclase, albite; then orthoclase, muscovite, quartz.",
            "Crystals are separated by settling (Stokes' law, effective in runny basalt), filter pressing, flow differentiation and wall crystallisation; cumulates form layers.",
            "Assimilation, mixing and immiscibility also change magmas; large granites owe more to crustal melting than to fractional crystallisation."),
    ],
))

# ------------------------------------------------------------------ 3. Binary phase diagrams
LESSONS.append(lesson(
    module=M_IGN,
    topic="Binary phase diagrams",
    title="Binary phase diagrams: the eutectic, the plagioclase loop and incongruent melting",
    slug="gyl2-binary-phase-diagrams",
    minutes=25,
    summary="How to read the diopside-anorthite eutectic system, the albite-anorthite solid-solution loop and the forsterite-silica system with incongruent melting of enstatite, and how to use the lever rule to find the proportions of crystals and melt.",
    objectives=[
        "Read a binary phase diagram: liquidus, solidus, eutectic, fields and tie lines",
        "Describe equilibrium crystallisation of a melt in the diopside-anorthite system and apply the lever rule",
        "Explain crystallisation in the albite-anorthite system, and why fractional crystallisation produces zoned plagioclase",
        "Explain incongruent melting of enstatite and the reaction relationship between olivine and pyroxene",
    ],
    key_concepts=["Phase", "Binary system", "Liquidus", "Solidus", "Eutectic", "Lever rule", "Solid solution", "Incongruent melting", "Peritectic"],
    blocks=[
        H("Introduction"),
        T("Bowen's reaction series came from experiments. Geologists melted simple mixtures of two minerals in furnaces, cooled them to different temperatures, quenched them to glass and looked at the crystals with a microscope. "
          "The results are drawn as **phase diagrams**. A phase diagram is a map that tells you which minerals and how much melt are stable at each temperature and composition. "
          "Three two-component (binary) systems explain most of what happens in basaltic magma."),
        D("A **phase** is a physically distinct, uniform part of a system, such as a melt or one kind of crystal. A **binary system** has two components. On the diagram, composition is plotted horizontally and temperature vertically, at a fixed pressure (usually 1 atmosphere).", title="Phase and binary system"),
        H("1. Diopside-anorthite: a eutectic system"),
        T("Diopside (a calcium-magnesium pyroxene) melts at 1392 °C and anorthite (calcium plagioclase) at 1553 °C. Mixtures of the two begin to melt at a lower temperature than either pure mineral. "
          "The lowest point on the liquidus is the **eutectic** E, at about 1274 °C and 42% anorthite (values from the classic experiments; textbooks round them slightly differently)."),
        IMG("algyl2-di-an.svg", alt="Phase diagram of temperature against percentage anorthite, with liquidus lines falling from diopside at 1392 degrees and from anorthite at 1553 degrees to a eutectic E at 1274 degrees and 42 percent anorthite, and a dashed vertical line for melt X at 30 percent anorthite",
            caption="Figure 1. The diopside-anorthite system (simplified with straight liquidus lines). Melt X contains 30% anorthite."),
        D("The **liquidus** is the line above which everything is melt. The **solidus** (here the horizontal eutectic line) is the line below which everything is solid. A **eutectic** is the point where the melt is in equilibrium with both solids at the lowest possible melting temperature.", title="Key lines"),
        EX("Worked example 1: cooling melt X", intro="Melt X (30% anorthite) cools slowly from 1500 °C. Using Figure 1, describe its crystallisation and find the proportions of crystals and melt just above 1274 °C.", steps=[
            S("Above the liquidus", text="At 1500 °C X is entirely liquid."),
            S("First crystals", math=r"T = 1392 - \tfrac{118}{42} \times 30 \approx 1308 {}^\circ\text{C}", text="X reaches the liquidus at about 1308 °C. X lies on the diopside side of E, so diopside crystallises first."),
            S("Cooling to the eutectic", text="As diopside forms, the melt loses diopside and moves down the liquidus towards E, becoming richer in anorthite."),
            S("Lever rule just above 1274 °C", math=r"\text{diopside} = \frac{42 - 30}{42 - 0} = 0.29, \quad \text{melt} = \frac{30 - 0}{42 - 0} = 0.71"),
            S("At the eutectic", text="The remaining 71% of the material (all melt) crystallises diopside and anorthite together at 1274 °C until no melt is left. The final rock is 70% diopside and 30% anorthite: early large diopside crystals in a finer intergrowth of both minerals."),
        ], check=r"0.29 + 0.71 = 1"),
        KEY("The lever rule", "Use it on any tie line (a horizontal line across a two-phase field).", cards=[
            ["Step 1", "Draw the tie line at the temperature asked, from the composition of one phase to the composition of the other."],
            ["Step 2", "Mark the bulk composition on the line."],
            ["Step 3", "The fraction of a phase = length of the line on the OPPOSITE side of the bulk composition ÷ total length. Like a see-saw: the phase nearer the bulk composition is the more abundant."],
        ]),
        T("Notice two rules that apply to all eutectic systems. Whichever side of E the melt starts on, the **last** melt always has the eutectic composition. And the first mineral to crystallise depends on the starting composition: diopside for melts with less than 42% anorthite, anorthite for those with more. "
          "In basalts, this explains why either pyroxene or plagioclase may appear first as large crystals (phenocrysts), and why **ophitic texture** (plagioclase laths enclosed in pyroxene) forms."),
        H("2. Albite-anorthite: a solid solution"),
        T("Albite (NaAlSi₃O₈) melts at 1118 °C and anorthite (CaAl₂Si₂O₈) at 1553 °C. Sodium plus silicon can replace calcium plus aluminium in the feldspar structure in any proportion, so there is a complete **solid solution**: every composition between Ab and An is one mineral, plagioclase. "
          "The diagram has no eutectic. Instead, a lens-shaped loop lies between the liquidus (above) and the solidus (below)."),
        IMG("algyl2-ab-an.svg", alt="Phase diagram of temperature against percentage anorthite showing a lens between a curved liquidus above and a curved solidus below, joining albite at the left and anorthite at the right, with a dashed line for a melt of An50 and a horizontal tie line from L to S at 1330 degrees",
            caption="Figure 2. The albite-anorthite (plagioclase) system, schematic teaching diagram. At 1330 °C the tie line joins melt L (about An35) and crystals S (about An63)."),
        EX("Worked example 2: a melt of An50", intro="Using Figure 2, describe the equilibrium crystallisation of a melt containing 50% anorthite.", steps=[
            S("First crystals", text="The melt reaches the liquidus at about 1400 °C. The first crystals have the composition on the solidus at that temperature: about An76, much richer in calcium than the melt."),
            S("At 1330 °C", math=r"\text{crystals} = \frac{50 - 35}{63 - 35} = 0.54, \quad \text{melt} = 0.46", text="The melt has moved down the liquidus to about An35 and the crystals down the solidus to about An63."),
            S("End of crystallisation", text="Under equilibrium the crystals react continuously with the melt. The last melt (about An24) disappears at about 1270 °C, when the crystals have the bulk composition, An50."),
        ], check=r"0.54 \times 63 + 0.46 \times 35 \approx 50"),
        T("**Fractional crystallisation** is different. If cooling is too fast for the crystals to react with the melt, each crystal keeps a calcium-rich core and grows sodium-richer layers around it. This gives **zoned plagioclase**, seen in thin section as concentric bands that go into extinction at different positions. "
          "The melt can then become far more sodium-rich than An24, which is how the continuous series of Bowen reaches albite. Zoning is strong evidence of fractional crystallisation."),
        MISTAKE("Reading the crystal composition from the liquidus", "At any temperature in the loop, the melt composition is on the liquidus and the crystal composition is on the solidus. Draw the tie line and read both ends; the bulk composition lies between them."),
        H("3. Forsterite-silica: incongruent melting"),
        T("Forsterite (Mg₂SiO₄, magnesium olivine) melts at about 1890 °C and silica (cristobalite) at about 1713 °C. Between them lies enstatite (MgSiO₃, a pyroxene). Enstatite does not melt to a liquid of its own composition. "
          "At about 1557 °C it breaks down to forsterite crystals plus a melt richer in silica. This is **incongruent melting**, and the point P where it happens is a **peritectic**."),
        IMG("algyl2-fo-silica.svg", alt="Schematic phase diagram from forsterite on the left to silica on the right with enstatite marked about a third of the way across, a peritectic point P at 1557 degrees just to the silica side of enstatite, and a eutectic E at 1543 degrees between enstatite and silica",
            caption="Figure 3. The forsterite-silica system (schematic, compositions not to scale). P is the peritectic and E the eutectic between enstatite and silica."),
        KEY("What the system shows", "This is the origin of the reaction relationship in Bowen's series.", cards=[
            ["Equilibrium cooling", "A melt between Fo and En first crystallises forsterite. At P the forsterite reacts with the melt to form enstatite. Olivine is used up until the melt is gone, leaving olivine + enstatite."],
            ["Fractional cooling", "If the forsterite crystals are removed (by settling) before they can react, the melt moves past P to the eutectic E and crystallises enstatite + silica. A silica-poor starting melt has produced free silica (quartz)."],
            ["Evidence in rocks", "Olivine crystals with rims of pyroxene (reaction rims); olivine and quartz are almost never in equilibrium in the same rock."],
        ]),
        T("**Evaluation.** Binary diagrams are simplifications: real magmas contain at least eight major oxides and water, crystallise under pressure, and solid-solution minerals such as olivine and pyroxene contain iron as well as magnesium. "
          "Yet the diagrams correctly predict the order of crystallisation, the eutectic intergrowths of basic rocks, zoned plagioclase and the reaction relationship of olivine and pyroxene, which is why Bowen's series is still taught."),
        QUIZ("In Figure 1, a melt with 70% anorthite cools. Which mineral crystallises first, and at roughly what temperature?", ["Diopside at about 1392 °C", "Anorthite at about 1409 °C", "Diopside and anorthite together at 1274 °C", "Anorthite at 1553 °C"], 1,
             "The melt lies on the anorthite side of E, so anorthite forms first, at the liquidus: 1274 + (279 ÷ 58) × 28 ≈ 1409 °C.", hint="Which side of the eutectic is the melt on?",
             feedback=["Diopside forms first only from melts with less than 42% anorthite.", "", "Both minerals form together only when the melt reaches the eutectic.", "1553 °C is the melting point of pure anorthite, not of a mixture."]),
        QUIZ("Which observation in a thin section is the best evidence that plagioclase crystallised by fractional (not equilibrium) crystallisation?", ["Plagioclase shows lamellar twinning", "Plagioclase crystals are compositionally zoned, calcic in the core and sodic at the rim", "Plagioclase is enclosed by pyroxene (ophitic texture)", "Plagioclase forms large phenocrysts"], 1,
             "Normal zoning shows that the early calcic cores did not react with the melt.", hint="What does incomplete reaction leave behind?",
             feedback=["Twinning is a normal feature of plagioclase, not evidence of fractionation.", "", "Ophitic texture shows the order of crystallisation of two minerals, not fractionation of plagioclase.", "Phenocrysts show two stages of cooling."]),
        TIP("Phase diagrams appear in Paper 1 (reading temperatures, first mineral, lever rule) and in Paper 2 (describe the crystallisation of a melt; link to Bowen's series). Always state the temperature at each stage, the phases present and how the melt composition changes.", title="Exam link"),
        PQ("Using Figure 1, describe the crystallisation of a melt of 20% anorthite and give the proportion of early diopside crystals just above the eutectic.",
           "Liquidus at 1392 − (118 ÷ 42) × 20 ≈ 1336 °C: diopside crystallises first. The melt moves down the liquidus towards E as diopside forms. Just above 1274 °C, by the lever rule: diopside = (42 − 20) ÷ 42 = 0.52 (52%), melt = 0.48. At 1274 °C the melt crystallises diopside and anorthite together until it is used up."),
        PQ("Distinguish between a eutectic system and a solid-solution system, giving one example of each.",
           "Eutectic: the two minerals do not mix in the solid state; mixtures melt at a lower temperature than either mineral and the last melt has the eutectic composition; example diopside-anorthite. Solid solution: the two end members mix in any proportion to form one mineral whose composition changes continuously; the diagram is a loop between liquidus and solidus; example albite-anorthite (plagioclase)."),
        PQ("Explain the term incongruent melting, and how the forsterite-silica system explains the reaction relationship in Bowen's discontinuous series.",
           "Incongruent melting: a mineral melts to a liquid of a different composition plus a different solid; enstatite melts at about 1557 °C to forsterite plus a silica-richer melt. On cooling, forsterite crystallises first and then reacts with the melt at the peritectic to form enstatite; this is the olivine-to-pyroxene step of the discontinuous series. If olivine is removed, the melt can reach the eutectic and crystallise silica."),
        SUM("A phase diagram shows the phases stable at each composition and temperature; read the liquidus, solidus, fields and tie lines.",
            "Diopside-anorthite is a eutectic system (E about 1274 °C, An42): the first mineral depends on which side of E the melt lies; the last melt is always at E.",
            "Lever rule: fraction of a phase = opposite segment ÷ total tie-line length.",
            "Albite-anorthite is a complete solid solution; fractional crystallisation leaves zoned plagioclase with calcic cores and sodic rims.",
            "Enstatite melts incongruently to forsterite + melt at a peritectic: the origin of the olivine-pyroxene reaction relationship."),
    ],
))

# ------------------------------------------------------------------ 4. Igneous textures and structures
LESSONS.append(lesson(
    module=M_IGN,
    topic="Igneous textures and structures",
    title="Reading the cooling history: igneous textures, lava structures and intrusions",
    slug="gyl2-igneous-textures-structures",
    minutes=25,
    summary="Igneous textures (crystallinity, grain size, crystal shape, porphyritic, ophitic, graphic, vesicular and flow textures) record how a magma cooled, and structures such as pillow lavas, columnar joints, sills and lava flows record where it cooled.",
    objectives=[
        "Describe igneous textures using the terms for crystallinity, grain size, crystal shape and crystal relationships",
        "Explain each texture in terms of nucleation, growth rate and cooling history",
        "Describe and explain lava structures such as pillows, columnar joints, vesicles and flow banding",
        "Distinguish a lava flow from a sill, and a concordant from a discordant intrusion, using field evidence",
    ],
    key_concepts=["Texture", "Holocrystalline", "Euhedral", "Porphyritic", "Ophitic", "Graphic texture", "Vesicular", "Amygdaloidal", "Columnar joints", "Chilled margin", "Sill"],
    blocks=[
        H("Introduction"),
        T("Two black rocks from the Mount Cameroon area can be made of the same minerals, yet one is full of gas holes and has a glassy crust, while the other has crystals large enough to see. "
          "The difference is texture, and texture is a record of how the magma cooled. Geologists use texture and structure together to say whether a rock cooled at the surface, at shallow depth or deep in the crust."),
        D("**Texture** is the size, shape and arrangement of the grains (crystals and glass) in a rock. **Structure** is a larger feature of a rock body, seen in an outcrop or in the field, such as jointing, banding or the shape of an intrusion.", title="Texture and structure"),
        H("Why cooling rate controls grain size"),
        T("Crystals form in two steps: **nucleation** (tiny seed crystals appear) and **growth** (atoms add to the seeds). When magma cools slowly, few nuclei form and each has time to grow, so crystals are large. "
          "When it cools fast, many nuclei form and none grows far, so crystals are tiny. If cooling is extremely fast, atoms cannot arrange themselves at all and the melt freezes as **glass** (for example obsidian, or the skin of a pillow lava)."),
        KEY("Terms for describing texture", "Use them in Paper 3 descriptions of hand specimens and thin sections.", cards=[
            ["Crystallinity", "Holocrystalline: all crystals. Hypocrystalline: crystals and glass. Holohyaline (glassy): all glass."],
            ["Grain size", "Coarse, medium and fine grained. A common scheme is coarse above 5 mm, medium 1 to 5 mm and fine below 1 mm; textbooks use slightly different limits, so check yours. Write 'coarse grained', not 'coarse grain'."],
            ["Crystal shape", "Euhedral: bounded by its own crystal faces. Subhedral: some faces. Anhedral: no faces, filling spaces between earlier crystals. Early crystals are often euhedral; late ones (quartz in granite) are anhedral."],
            ["Relative size", "Equigranular: crystals of similar size. Porphyritic: large crystals (phenocrysts) in a finer groundmass. Pegmatitic: very coarse (crystals of several centimetres). Aplitic: fine, sugary, even-grained."],
        ]),
        H("Textures and what they mean"),
        KEY("Textures that tell a story", "Each texture has a cooling explanation.", cards=[
            ["Porphyritic", "Two stages of cooling: phenocrysts grew slowly at depth, then the magma rose and the rest cooled quickly as fine groundmass. Example: porphyritic andesite or basalt."],
            ["Ophitic and subophitic", "Large pyroxene crystals enclose small laths of plagioclase. Plagioclase began crystallising first and pyroxene grew around it. Typical of dolerite in dykes and sills."],
            ["Graphic (granophyric)", "Quartz and alkali feldspar intergrown in angular patterns like old writing. They crystallised together at a eutectic-like point, typical of the last melt of a granite."],
            ["Poikilitic", "Many small crystals of one mineral enclosed in a large crystal of another; ophitic texture is a special case."],
            ["Vesicular and amygdaloidal", "Vesicles are holes left by gas bubbles near the top of a lava. Amygdales are vesicles later filled with minerals such as calcite, quartz or zeolites from circulating water."],
            ["Flow textures", "Flow banding (layers of different colour or crystal content, common in rhyolite) and trachytic texture (feldspar laths lined up parallel to the flow)."],
        ]),
        EX("Worked example 1: interpreting a texture", intro="A hand specimen is dark grey. It has euhedral olivine and plagioclase crystals 3 to 4 mm long set in a groundmass too fine to see, and a few rounded holes filled with white calcite. Name the texture and interpret the cooling history.", steps=[
            S("Describe", text="Large euhedral crystals in a fine groundmass: porphyritic texture. Filled gas holes: amygdaloidal."),
            S("Interpret the crystals", text="The olivine and plagioclase phenocrysts grew slowly in a magma chamber at depth; the groundmass cooled quickly after eruption."),
            S("Interpret the holes", text="Gas came out of solution as pressure fell near the surface, making vesicles; later, warm water deposited calcite in them."),
            S("Name", text="A porphyritic, amygdaloidal basalt: a lava that cooled at the surface after a period of slow cooling at depth."),
        ]),
        H("Lava structures"),
        KEY("Structures formed at the surface", "Each forms in a particular way.", cards=[
            ["Pahoehoe and aa", "Pahoehoe: smooth, ropy surface of hot, runny basalt. Aa: rough, broken, clinkery surface of cooler, more viscous lava."],
            ["Pillow lavas", "Basalt erupted under water forms rounded pillows with glassy rims, because the outer skin is chilled instantly while the inside keeps flowing. They show eruption under water, for example at mid-ocean ridges."],
            ["Columnar joints", "Closely packed, mostly five- or six-sided vertical columns. As a thick lava or sill cools it contracts; tensional forces pull towards many centres and open joints at right angles to the cooling surface, splitting the rock into polygonal columns."],
            ["Lava tubes and flow tops", "The surface of a flow crusts over while lava flows on inside. Flow tops are rubbly, vesicular and often weathered before the next flow covers them."],
        ]),
        MISTAKE("Naming columnar joints as pillow lavas or mud cracks", "The Board's 2023 report says many candidates could not name columnar joints in a photograph, or confused them with pillow lavas, tors or mud cracks. Columnar joints are regular polygonal columns; pillows are rounded masses with glassy rims; mud cracks are shallow cracks in drying mud."),
        H("Lava flow or sill?"),
        T("A sill and a buried lava flow both look like a sheet of igneous rock lying parallel to the beds. Distinguishing them is a classic examination question, and the Board's 2023 report says many candidates could not do it. The key is that a lava cooled at the surface and was buried later, whereas a sill was intruded between beds that already existed."),
        CODE("Feature                 Buried lava flow                  Sill\n"
             "Upper surface           irregular, rubbly, may be         regular, even\n"
             "                        weathered\n"
             "Grain size              fine grained to glassy            medium to fine grained (dolerite)\n"
             "Vesicles, amygdales     common near the top               rare\n"
             "Baked (heated) rock     only below the flow               above AND below the sill\n"
             "Chilled margin          at the base (and top)             at both upper and lower contacts\n"
             "Fragments               pieces of lava in the bed above   no fragments in the bed above\n"
             "Veins of igneous rock   only in the rock below            in rocks above and below\n"
             "Xenoliths               only from the rock below          from rocks above and below\n"
             "Cross-cutting           never cuts up into younger beds   may step across beds", "text", title="Table 1. Distinguishing a buried lava flow from a sill"),
        T("Remember also that a sill is intrusive (hypabyssal) and cooled below the surface, so it is younger than the beds on both sides of it, while a lava flow is younger than the bed below it but older than the bed above it. This matters when you work out a geological history from a map or section."),
        EX("Worked example 2: lava flow or sill from a borehole", intro="A borehole passes down through sandstone, then 12 m of fine-grained basalt, then shale. The top metre of the basalt is reddened and full of amygdales. The sandstone just above the basalt contains rounded basalt pebbles. The shale is hardened for 2 m below the basalt, but the sandstone above is not altered. Is the basalt a lava flow or a sill?", steps=[
            S("Upper contact", text="A weathered (reddened), amygdaloidal top and basalt pebbles in the overlying sandstone show that the top of the basalt was exposed and eroded before the sand was deposited."),
            S("Baking", text="Only the rock below is baked; the sandstone above was laid down on cold basalt."),
            S("Conclusion", text="The basalt is a buried lava flow. Order of events: shale deposited, lava erupted onto it, top weathered and eroded, sandstone deposited."),
        ]),
        H("Intrusive structures"),
        T("**Concordant** intrusions lie parallel to the layering: **sills**, **laccoliths** (domed roof, flat floor) and **lopoliths** (saucer-shaped, often layered gabbro). **Discordant** intrusions cut across it: **dykes** (often in swarms), **ring dykes** and **cone sheets** around volcanic centres, **volcanic necks** (the solidified feeder pipes of volcanoes), **stocks** and **batholiths** (huge granite masses). "
          "Along every contact look for a **chilled margin** (finer grain in the intrusion next to the contact, because it cooled fast against cold rock) and a **baked margin** (country rock hardened and recrystallised by heat), as well as **xenoliths**."),
        QUIZ("A thick dolerite sheet has chilled margins and baked rock at both its upper and lower contacts, and xenoliths of the overlying shale. What is it?", ["A buried lava flow", "A sill", "A volcanic neck", "A pillow lava"], 1,
             "Baking and chilling on both sides and xenoliths from the rock above show that magma was intruded between existing beds.", hint="Which body was in contact with hot magma on both sides?",
             feedback=["A lava flow bakes only the rock beneath it and cannot contain xenoliths of a bed laid down later.", "", "A neck is a vertical pipe, not a sheet parallel to bedding.", "Pillows form in water and are rounded, not a sheet with baked contacts above."]),
        QUIZ("Which texture shows that a rock had two stages of cooling?", ["Equigranular", "Porphyritic", "Glassy", "Graphic"], 1,
             "Phenocrysts grew slowly first; the groundmass cooled quickly later.", hint="Two crystal sizes mean two different cooling rates.",
             feedback=["Similar-sized crystals show one steady rate of cooling.", "", "A glass shows very rapid cooling only.", "Graphic texture shows simultaneous crystallisation of quartz and feldspar, not two stages."]),
        TIP("Textures appear in all three papers: in Paper 1 as definitions, in Paper 2 as 'describe and explain' and 'distinguish' questions (lava flow and sill, chilled and baked margins), and in Paper 3 when you describe a hand specimen, a thin section or a photograph of columnar joints. Describe first, then explain the cooling.", title="Exam link"),
        PQ("State five differences between a buried lava flow and a sill.",
           "Any five, each stated for both bodies: lava has an irregular, rubbly or weathered top, a sill a regular top; lava is fine grained or glassy, a sill medium to fine grained; lava is often vesicular or amygdaloidal near the top, a sill rarely; lava bakes only the rock below, a sill bakes the rocks above and below; lava fragments may occur in the bed above a flow, but not above a sill; veins and xenoliths occur only below a lava, but above and below a sill; a sill may cut across beds, a lava does not."),
        PQ("Describe and explain the formation of columnar joints.",
           "Description: closely packed, regular columns, usually five- or six-sided, perpendicular to the top and base of a thick lava flow or sill. Explanation: as the rock cools it contracts; tensional stresses develop towards many evenly spaced centres; joints open between these centres at right angles to the cooling surfaces and grow inwards as cooling proceeds, dividing the rock into polygonal prisms."),
        PQ("Explain why a granite pegmatite has very large crystals although it often forms as a thin vein.",
           "Pegmatite forms from the last, water-rich melt of a granite. Water lowers the viscosity of the melt and allows atoms to move quickly to growing crystals, and few nuclei form, so a few crystals grow very large even though the vein is thin. Its texture reflects the melt's water content more than its cooling rate."),
        SUM("Texture records cooling rate: slow cooling gives few nuclei and large crystals, fast cooling many small crystals or glass.",
            "Describe crystallinity, grain size ('coarse grained'), crystal shape and relationships before interpreting.",
            "Porphyritic = two stages of cooling; ophitic = plagioclase enclosed in pyroxene (dolerite); graphic = quartz-feldspar intergrowth; vesicles and amygdales = gas near the surface.",
            "Pillows show eruption under water; columnar joints form by contraction on cooling.",
            "A sill bakes and chills on both sides and has xenoliths from above and below; a buried lava flow bakes only below and has a rubbly, vesicular top."),
    ],
))

# ------------------------------------------------------------------ 5. Classification of igneous rocks
LESSONS.append(lesson(
    module=M_IGN,
    topic="Classification of igneous rocks",
    title="Classifying igneous rocks: silica, saturation, colour index and the IUGS QAPF diagram",
    slug="gyl2-classification-igneous-rocks",
    minutes=25,
    summary="Igneous rocks are classified by grain size, silica content, silica saturation and colour index, and precisely by the IUGS QAPF diagram, which uses the modal proportions of quartz, alkali feldspar and plagioclase recalculated to 100%.",
    objectives=[
        "Classify igneous rocks by grain size and by silica content (acid, intermediate, basic, ultrabasic)",
        "Explain silica saturation and use colour index to describe a rock",
        "Recalculate a modal analysis to Q + A + P = 100 and name a plutonic rock on the QAPF diagram",
        "Evaluate chemical and modal classification schemes, including TAS for volcanic rocks",
    ],
    key_concepts=["Modal analysis", "Silica content", "Silica saturation", "Feldspathoid", "Colour index", "QAPF diagram", "IUGS", "TAS diagram"],
    blocks=[
        H("Introduction"),
        T("Different geologists once used different names for the same rock, which made reports hard to compare. In the 1970s the International Union of Geological Sciences (IUGS) agreed a common scheme. "
          "At A Level you need both the simple chemical scheme you met at O Level and the IUGS modal scheme, and you need to know why each is used. A **modal analysis** gives the volume percentage of each mineral in a rock, measured in thin section by point counting."),
        H("Four simple bases of classification"),
        KEY("Grain size, silica, saturation and colour", "Combine them to name a rock.", cards=[
            ["Grain size", "Coarse (plutonic), medium (hypabyssal), fine or glassy (volcanic). Each composition has a coarse and a fine equivalent: granite and rhyolite, diorite and andesite, gabbro and basalt."],
            ["Silica content (by mass of SiO2)", "Acid above 63%, intermediate 52 to 63%, basic 45 to 52%, ultrabasic below 45%. Some older textbooks use 66% for the acid boundary, so check yours. Silica content is a chemical measure; it is not the same as the amount of quartz."],
            ["Silica saturation", "Oversaturated: enough silica to make free quartz. Saturated: no quartz and no silica-poor minerals. Undersaturated: too little silica, so feldspathoids (nepheline, leucite) or magnesium-rich olivine form instead; these never occur with primary quartz."],
            ["Colour index", "The percentage of dark (mafic) minerals by volume. Leucocratic below 35, mesocratic 35 to 65, melanocratic 65 to 90, ultramafic above 90."],
        ]),
        CODE("Silica class    Coarse        Medium          Fine           Typical minerals\n"
             "Acid            granite       microgranite    rhyolite       quartz, K-feldspar, Na-plagioclase, micas\n"
             "Intermediate    diorite       microdiorite    andesite       andesine, hornblende, biotite\n"
             "                syenite       microsyenite    trachyte       K-feldspar, little quartz\n"
             "Basic           gabbro        dolerite        basalt         labradorite, augite, olivine\n"
             "Ultrabasic      peridotite    -               komatiite      olivine, pyroxene\n"
             "Undersaturated  nepheline     -               phonolite      K-feldspar, nepheline\n"
             "                syenite", "text", title="Table 1. Common igneous rocks"),
        MISTAKE("Equating 'acid' with 'contains acid'", "Acid, intermediate and basic describe the SiO₂ content, a historical term. A basalt contains about 48% SiO₂ although it has no free quartz: the silica is locked up in feldspar, pyroxene and olivine."),
        H("The QAPF diagram"),
        T("For rocks with less than 90% mafic minerals, the IUGS scheme uses only three groups of light minerals: **Q** quartz, **A** alkali feldspar (orthoclase, microcline, sanidine and albite with less than 5% anorthite), and **P** plagioclase (An5 to An100). "
          "(A fourth group, F, the feldspathoids, has its own lower triangle, used for undersaturated rocks.) The three values are recalculated so that Q + A + P = 100, and the rock is plotted on a triangle. Mafic minerals are ignored for the name, but described with the colour index."),
        IMG("algyl2-qapf.svg", alt="Upper QAPF triangle, Q at the top and A and P at the base, divided by lines at 5, 20, 60 and 90 percent quartz and at 10, 35, 65 and 90 percent of P over A plus P, with 16 numbered fields named in a key",
            caption="Figure 1. The upper (Q-A-P) triangle of the IUGS classification of plutonic rocks, simplified. Fields 3 and 4 together are granite."),
        KEY("How to use the diagram", "Two numbers locate any rock.", cards=[
            ["Step 1", "Recalculate: Q' = Q × 100 ÷ (Q + A + P), and the same for A and P."],
            ["Step 2", "Find the band from Q': below 5, 5 to 20, 20 to 60, 60 to 90, above 90."],
            ["Step 3", "Find the column from the ratio P ÷ (A + P) × 100: below 10, 10 to 35, 35 to 65, 65 to 90, above 90."],
            ["Step 4", "Read the field name. In the bottom-right field, diorite has plagioclase with less than 50% anorthite and gabbro more than 50%."],
        ]),
        EX("Worked example 1: naming a granite", intro="A coarse-grained rock has a mode of quartz 25%, orthoclase 30%, plagioclase (oligoclase) 25%, biotite 12% and hornblende 8%. Name it and give its colour index.", steps=[
            S("Sum of Q + A + P", math=r"25 + 30 + 25 = 80"),
            S("Recalculate", math=r"Q' = \frac{25}{80} \times 100 = 31, \quad A' = 37.5, \quad P' = 31"),
            S("Plagioclase ratio", math=r"\frac{P}{A + P} = \frac{25}{55} \times 100 = 45\%"),
            S("Read the diagram", text="Q' is in the band 20 to 60 and the ratio is in the column 35 to 65: field 4, monzogranite, which is a granite."),
            S("Colour index", math=r"12 + 8 = 20 \Rightarrow \text{leucocratic}"),
        ], check=r"31.25 + 37.5 + 31.25 = 100"),
        EX("Worked example 2: diorite or gabbro?", intro="A coarse rock contains quartz 5%, orthoclase 5%, plagioclase (andesine, An40) 50%, hornblende 30% and biotite 10%. Name it.", steps=[
            S("Recalculate", math=r"Q' = \frac{5}{60} \times 100 = 8.3, \quad \frac{P}{A+P} = \frac{50}{55} \times 100 = 91\%"),
            S("Field", text="Q' between 5 and 20 and ratio above 90: field 11, quartz diorite or quartz gabbro."),
            S("Decide", text="The plagioclase is andesine (An40, below An50) and the mafic mineral is hornblende, so the rock is a **quartz diorite**. Colour index 40: mesocratic."),
        ], check=r"\frac{50}{55} = 0.909"),
        H("Volcanic rocks and the TAS diagram"),
        T("Fine-grained and glassy rocks cannot be point-counted reliably, so the IUGS names volcanic rocks from their chemical analysis with the **TAS diagram**: total alkalis (Na₂O + K₂O) plotted against SiO₂. "
          "It separates subalkaline rocks (basalt, andesite, dacite, rhyolite) from alkaline rocks rich in sodium and potassium (basanite, trachybasalt, trachyte, phonolite). Many lavas of the Cameroon Volcanic Line plot in the alkaline fields. You are not expected to memorise the TAS boundaries; know what the axes are and why the diagram is used."),
        T("**Evaluation.** Modal schemes such as QAPF use what can be seen and are ideal for coarse rocks, but need a thin section and careful point counting, and cannot be used for glassy rocks. Chemical schemes such as TAS work for any rock but need a laboratory analysis, and rocks altered by weathering give misleading results. "
          "The simple silica scheme is quick, but the boundaries are arbitrary and a rock's silica content cannot be seen in hand specimen. A good description uses several schemes: for example 'a coarse-grained, leucocratic, oversaturated acid rock: granite'."),
        QUIZ("A rock has Q' = 43 and P ÷ (A + P) = 88%. Which field of Figure 1 is it in?", ["Monzogranite", "Granodiorite", "Tonalite", "Quartz monzonite"], 1,
             "Q' between 20 and 60 and a ratio between 65 and 90 places it in field 5, granodiorite.", hint="First the quartz band, then the plagioclase column.",
             feedback=["Monzogranite needs a ratio of 35 to 65.", "", "Tonalite needs a ratio above 90.", "Quartz monzonite has Q' between 5 and 20."]),
        QUIZ("Which mineral shows that an igneous rock is silica-undersaturated?", ["Quartz", "Nepheline", "Orthoclase", "Hornblende"], 1,
             "Feldspathoids such as nepheline form only when there is too little silica to make feldspar.", hint="Which mineral contains less silica than the feldspar of the same alkali?",
             feedback=["Quartz shows oversaturation.", "", "Orthoclase forms in saturated and oversaturated rocks.", "Hornblende can occur in many rocks and does not show saturation."]),
        TIP("In Paper 1 expect questions on silica classes, saturation, colour index and QAPF fields; in Paper 2, classification schemes and their merits; in Paper 3, naming a hand specimen from its texture, colour and minerals. Always calculate Q + A + P = 100 before plotting.", title="Exam link"),
        PQ("A plutonic rock contains alkali feldspar 60%, plagioclase 8%, quartz 2% and hornblende 30%. Name it using Figure 1 and give its colour index class.",
           "Q + A + P = 70. Q' = 2 ÷ 70 × 100 = 2.9 (below 5). P ÷ (A + P) = 8 ÷ 68 × 100 = 11.8% (10 to 35). Field 13: syenite. Colour index 30: leucocratic."),
        PQ("Explain the difference between the silica content of a rock and its quartz content, using basalt and granite as examples.",
           "Silica content is the total SiO₂ by mass from a chemical analysis; quartz content is the volume of the mineral quartz. Basalt has about 48% SiO₂ but no free quartz, because all its silica is combined in plagioclase, pyroxene and olivine. Granite has about 70% SiO₂, and the silica left over after making feldspars and micas crystallises as quartz (oversaturated)."),
        PQ("Discuss the advantages and disadvantages of classifying igneous rocks by their mineral content (mode) and by their chemical composition.",
           "Mode: based on what is visible; quick in coarse rocks; names reflect the minerals (QAPF). But it needs thin sections and point counting, and fails for fine-grained and glassy rocks. Chemistry: works for all rocks including glass; precise; allows the TAS diagram and silica classes. But it needs costly laboratory analysis, weathering and alteration change the results, and it does not show texture or how the rock formed. Best practice combines texture, mode and chemistry."),
        SUM("Basic bases: grain size (plutonic, hypabyssal, volcanic), silica content (acid > 63%, intermediate, basic, ultrabasic < 45%; some books use 66%), silica saturation and colour index.",
            "Undersaturated rocks contain feldspathoids or Mg-olivine and never primary quartz.",
            "QAPF: recalculate Q + A + P to 100, find the quartz band and the column P ÷ (A + P); granite = syenogranite + monzogranite.",
            "Volcanic rocks are named chemically on the TAS diagram (total alkalis against silica).",
            "Each scheme has limits: modal needs coarse rocks, chemical needs fresh rocks and a laboratory."),
    ],
))

# ------------------------------------------------------------------ 6. Igneous rocks and tectonic settings
LESSONS.append(lesson(
    module=M_IGN,
    topic="Igneous rocks and tectonic settings",
    title="Igneous rocks and plate tectonic settings: ridges, arcs, collision zones, rifts and hotspots",
    slug="gyl2-igneous-tectonic-settings",
    minutes=25,
    summary="Each plate setting has its own igneous rocks: tholeiitic basalt and ophiolites at ridges, calc-alkaline andesite and granodiorite at subduction zones, crustal granites in collision zones, alkaline and bimodal rocks in rifts and at hotspots; the Cameroon Volcanic Line as a case.",
    objectives=[
        "Link each plate tectonic setting to its melting mechanism, magma type and typical rocks",
        "Describe an ophiolite sequence and explain what it tells us about oceanic crust",
        "Distinguish I-type and S-type granites and explain where each forms",
        "Use simple geometry to locate arc volcanoes above a subducting slab, and discuss the Cameroon Volcanic Line",
    ],
    key_concepts=["MORB", "Ophiolite", "Calc-alkaline", "Island arc", "Batholith", "I-type and S-type granite", "Bimodal volcanism", "Hotspot", "Cameroon Volcanic Line"],
    blocks=[
        H("Introduction"),
        T("If you know where on a plate a rock formed, you can often predict what kind of igneous rock it is, and the reverse is also true: old igneous rocks can tell us which plate settings existed in the past. "
          "Cameroon is a good place to think about this. The Cameroon Volcanic Line is an active chain of volcanoes, while old granites and gneisses of the Pan-African belt record ancient mountain building. This lesson builds on the three melting mechanisms of the first lesson."),
        IMG("algyl2-settings.svg", alt="Cross-section showing a mid-ocean ridge with magma rising beneath it, oceanic lithosphere moving to a subduction zone under a continent with a volcanic arc above, a mantle plume rising to a hotspot volcano, and a key listing the magma type of each setting",
            caption="Figure 1. Igneous activity and plate settings (schematic, not to scale)."),
        H("Constructive margins: mid-ocean ridges"),
        T("Decompression melting of the upper mantle beneath ridges produces large volumes of **tholeiitic basalt**, called MORB (mid-ocean ridge basalt). It is low in potassium and incompatible elements because the mantle under ridges has already lost them in earlier melting and melts by a large degree. "
          "The oceanic crust it builds has a regular layered structure, seen where slices of it have been pushed onto land as **ophiolites** (for example Troodos in Cyprus and Oman)."),
        CODE("Ophiolite sequence (top to bottom)\n"
             "deep-sea sediments: chert, shale\n"
             "pillow lavas (basalt erupted on the sea floor)\n"
             "sheeted dyke complex (dolerite dykes intruded side by side at the ridge)\n"
             "gabbro, layered at the base (cumulates of the magma chamber)\n"
             "peridotite (mantle residue left after melting)", "text", title="Table 1. A complete ophiolite"),
        H("Destructive margins: subduction zones"),
        T("At about 100 km depth, the descending slab releases water into the mantle wedge (flux melting). The basaltic melts rise, pond at the base of the crust, differentiate and assimilate crust, giving a **calc-alkaline** association: basaltic andesite, **andesite** (the commonest arc lava), dacite and rhyolite, often erupted explosively because the magmas are viscous and rich in water. "
          "Deeper in the crust they crystallise as composite **batholiths** of diorite, tonalite and granodiorite. Island arcs (Japan, the Lesser Antilles) form where ocean subducts under ocean; active continental margins (the Andes) where ocean subducts under a continent."),
        EX("Worked example 1: where is the volcanic arc?", intro="Arc volcanoes form roughly where the top of the slab is 100 km deep. A slab dips at 30° from the trench. How far from the trench is the arc? How far if the slab dips at 60°?", steps=[
            S("Geometry", math=r"\tan\theta = \frac{\text{depth}}{\text{horizontal distance}} \Rightarrow d = \frac{100}{\tan\theta}"),
            S("Dip 30°", math=r"d = \frac{100}{\tan 30^\circ} = \frac{100}{0.577} = 173 \text{ km}"),
            S("Dip 60°", math=r"d = \frac{100}{\tan 60^\circ} = 58 \text{ km}", text="A gently dipping slab places the arc far from the trench; a steep slab places it close."),
        ], check=r"173 \times \tan 30^\circ = 100"),
        H("Collision zones and granite types"),
        T("When two continents collide (the Himalaya), the crust is thickened to about twice its normal thickness. Deeply buried sedimentary and metamorphic rocks heat up and partly melt (heat transfer and dehydration of micas), giving granites that are rich in aluminium and contain muscovite, and sometimes garnet or cordierite."),
        KEY("I-type and S-type granites", "A classification by source rock (Chappell and White, 1970s).", cards=[
            ["I-type (igneous source)", "Formed by melting of older igneous rocks or by differentiation of mantle magmas; typical of subduction zones. Hornblende and biotite, magnetite; tonalite to granite."],
            ["S-type (sedimentary source)", "Formed by melting of sedimentary or metasedimentary rocks; typical of collision zones. Muscovite, biotite, garnet or cordierite; peraluminous (excess aluminium)."],
            ["A-type (anorogenic)", "Some textbooks also use A-type granites, formed in rifts and within plates, rich in alkalis. Check whether your textbook includes them."],
        ]),
        H("Within plates: rifts and hotspots"),
        T("**Continental rifts** (the East African Rift) are fed by decompression melting of the mantle as the lithosphere is stretched. Small degrees of melting give **alkaline** magmas: alkali basalt, basanite, trachyte, phonolite, even carbonatite. "
          "Basaltic magma also melts the continental crust, giving rhyolite. The result is **bimodal** volcanism: basalt and rhyolite with few intermediate rocks. "
          "**Hotspots** lie above mantle plumes. Oceanic hotspots (Hawaii, Iceland) build huge shield volcanoes of ocean-island basalt; the volcanoes get older away from the active one as the plate moves over the plume. Very large plumes may produce **large igneous provinces** (flood basalts such as the Deccan Traps of India)."),
        H("The Cameroon Volcanic Line"),
        T("The Cameroon Volcanic Line is a chain of volcanoes about 1600 km long that runs from the islands of the Gulf of Guinea (Annobón, São Tomé, Príncipe and Bioko) onto the continent through Mount Cameroon, Manengouba, the Bamboutos Mountains and Mount Oku towards the Adamawa Plateau. It is unusual because it crosses the boundary between ocean and continent. "
          "Its rocks are mostly alkaline: alkali basalts and basanites, with trachytes and phonolites formed by differentiation. Mount Cameroon is its active volcano, and Lake Nyos, where a release of carbon dioxide killed many people in 1986, lies in a volcanic crater on the line. "
          "Unlike Hawaii, the volcanoes do not show a simple age progression along the line, so geologists debate its origin: a mantle plume, decompression melting along old zones of weakness (shear zones) in the lithosphere, or mantle flow at the edge of the thick Congo Craton. Present it as a debate in essays (check your textbook for the current views)."),
        EX("Worked example 2: identify the setting", intro="A sequence of rocks contains abundant andesite lavas and pyroclastic rocks, intruded by a batholith of granodiorite containing hornblende. Name the setting and explain each rock.", steps=[
            S("Andesite and explosive deposits", text="Viscous, water-rich, intermediate magma: calc-alkaline volcanism above a subduction zone."),
            S("Hornblende granodiorite batholith", text="An I-type granitoid crystallised from arc magma deep in the crust; hornblende shows the magma was rich in water."),
            S("Setting", text="An active continental margin (or a mature island arc), like the Andes."),
        ]),
        MISTAKE("Saying that subduction melts the slab to make andesite", "At most subduction zones the slab itself rarely melts. Water released from it causes melting of the overlying mantle wedge, giving basalt; andesite forms mainly by differentiation and crustal assimilation of that basalt."),
        QUIZ("Which association is typical of a continental rift?", ["Andesite lavas and granodiorite batholiths", "Basalt and rhyolite with few intermediate rocks, and alkaline lavas", "Pillow lavas above sheeted dykes and gabbro", "Muscovite-garnet granites in thickened crust"], 1,
             "Rifts give bimodal and alkaline volcanism from decompression melting and crustal melting.", hint="Rifts are stretched continents.",
             feedback=["That is the calc-alkaline association of subduction zones.", "", "That is the ophiolite sequence of oceanic crust formed at a ridge.", "Those are S-type granites of collision zones."]),
        QUIZ("Why is mid-ocean ridge basalt low in potassium compared with hotspot basalts?", ["It forms by a large degree of melting of mantle already depleted in incompatible elements", "It is contaminated by sea water", "It forms by melting of continental crust", "It cools too fast for potassium to enter it"], 0,
             "Large degrees of melting of a depleted source dilute incompatible elements such as potassium.", hint="Think of C_L = C₀ ÷ F.",
             feedback=["", "Sea water would add potassium if anything.", "MORB comes from the mantle, not from continental crust.", "Cooling rate controls grain size, not the potassium content of the melt."]),
        TIP("Paper 2 essays often ask you to relate igneous rocks to plate settings. Organise your answer by setting; for each, give the melting mechanism, the magma type, named rocks and a named example. Use the Cameroon Volcanic Line with care: describe it accurately and say that its origin is debated.", title="Exam link"),
        PQ("Describe the sequence of rocks in an ophiolite and explain how each layer formed.",
           "From top: deep-sea sediments deposited on the new sea floor; pillow lavas erupted under water at the ridge; a sheeted dyke complex formed as dyke after dyke was intruded into the spreading axis; gabbro crystallised in the magma chamber, with layered cumulates at its base; peridotite, the mantle residue left after partial melting. Ophiolites are oceanic lithosphere thrust onto land at destructive margins."),
        PQ("A slab dips at 45°. Volcanoes form where the slab is about 100 km deep. How far from the trench should the volcanic arc be?",
           "d = 100 ÷ tan 45° = 100 ÷ 1 = 100 km from the trench."),
        PQ("Compare the igneous rocks formed at a destructive plate margin with those formed at a constructive plate margin.",
           "Constructive: decompression melting of dry mantle; tholeiitic basalt (MORB), low in potassium and water; quiet eruptions, pillow lavas; dolerite dykes and gabbro; forms new oceanic crust. Destructive: flux melting of the mantle wedge plus differentiation and assimilation; calc-alkaline basaltic andesite, andesite, dacite and rhyolite, rich in water; explosive eruptions and pyroclastic rocks; batholiths of diorite, tonalite, granodiorite (I-type). Both involve basaltic primary magma from the mantle."),
        PQ("Outline the evidence that the origin of the Cameroon Volcanic Line is not a simple hotspot like Hawaii.",
           "At a simple hotspot, the volcanoes get older in the direction of plate motion, with one active centre. Along the Cameroon Volcanic Line, volcanoes of different ages are scattered along its length with no simple age progression, and the line continues from oceanic to continental lithosphere. This has led to alternative models: melting along reactivated shear zones, or mantle flow at the edge of the Congo Craton."),
        SUM("Ridges: decompression gives tholeiitic MORB; ophiolites show the oceanic crust: sediments, pillow lavas, sheeted dykes, gabbro, peridotite.",
            "Subduction zones: flux melting of the wedge, then differentiation and assimilation: calc-alkaline andesite, explosive volcanism, I-type granodiorite and tonalite batholiths.",
            "Collision zones: crustal melting of thickened crust gives S-type, aluminium-rich granites with muscovite and garnet.",
            "Rifts: bimodal basalt-rhyolite and alkaline rocks; hotspots: ocean-island basalts and age-progressive chains; plumes may make flood basalts.",
            "The Cameroon Volcanic Line is alkaline and crosses the ocean-continent boundary; its origin is debated."),
    ],
))

# ------------------------------------------------------------------ 7. Agents and types of metamorphism
LESSONS.append(lesson(
    module=M_MET,
    topic="Agents and types of metamorphism",
    title="Agents and types of metamorphism: heat, pressure, fluids and the settings where rocks change",
    slug="gyl2-agents-types-metamorphism",
    minutes=25,
    summary="Metamorphism changes rocks in the solid state through heat, confining pressure, directed stress and chemically active fluids; prograde reactions release water and CO2, and contact, regional, dynamic, burial, hydrothermal and impact metamorphism each have their own setting and products.",
    objectives=[
        "Define metamorphism and state its limits (diagenesis below, melting above)",
        "Explain the role of temperature, confining pressure, directed stress, fluids and time",
        "Distinguish prograde and retrograde metamorphism and write a simple metamorphic reaction",
        "Describe contact, regional, dynamic, burial, hydrothermal and impact metamorphism, including pneumatolytic processes",
    ],
    key_concepts=["Metamorphism", "Protolith", "Confining pressure", "Directed stress", "Prograde", "Retrograde", "Contact metamorphism", "Regional metamorphism", "Metasomatism", "Pneumatolysis"],
    blocks=[
        H("Introduction"),
        T("Much of southern and central Cameroon is built of gneisses, schists and migmatites: rocks that were once sediments or igneous rocks, then buried, heated and squeezed during ancient mountain building, such as the Pan-African orogeny. "
          "Near granite intrusions elsewhere, hard, splintery hornfels has formed from shale baked by the hot magma. Both are **metamorphic rocks**. The Board's 2023 report comments that metamorphism seems to be poorly taught in many schools, and candidates scored badly on it, so take this module carefully."),
        D("**Metamorphism** is the change in the mineralogy and texture of a rock in the **solid state**, in response to changes in temperature, pressure and chemically active fluids. The original rock is the **protolith** (parent rock).", title="Metamorphism"),
        T("Metamorphism begins where **diagenesis** (the low-temperature changes that turn sediment into sedimentary rock) ends, at roughly 150 to 200 °C, and stops where the rock begins to melt, at about 650 to 750 °C for wet granite compositions (higher for dry or basic rocks). "
          "Above that, partial melting gives **migmatite** and then magma. Most metamorphism is close to **isochemical**: the bulk chemistry stays nearly the same except for water and carbon dioxide."),
        H("The agents of metamorphism"),
        KEY("Agents", "Each agent does a different job.", cards=[
            ["Temperature", "The most important agent. Heat speeds up reactions and makes some minerals unstable, so new ones grow. Sources: the geothermal gradient (burial), nearby magma and radioactive heat in thickened crust."],
            ["Confining (lithostatic) pressure", "Equal in all directions, from the weight of overlying rock. It favours dense minerals (kyanite, garnet, jadeite) but produces no foliation."],
            ["Directed (differential) stress", "Unequal in different directions, from plate movements. It rotates, flattens and aligns platy and elongate minerals, producing foliation and lineation."],
            ["Chemically active fluids", "Hot water with CO₂ and dissolved ions. Fluids speed up reactions and carry material in or out. When the bulk chemistry changes, the process is **metasomatism**."],
            ["Time", "Reactions in solids are slow. Large crystals (porphyroblasts) need long periods at high temperature."],
        ]),
        EX("Worked example 1: pressure and depth", intro="A schist contains minerals that formed at 0.6 GPa and 600 °C. Estimate the depth of metamorphism (average rock density 2800 kg m⁻³, g = 9.8 m s⁻²) and the geothermal gradient at that time.", steps=[
            S("Depth", math=r"h = \frac{P}{\rho g} = \frac{0.6 \times 10^{9}}{2800 \times 9.8} = 21\,900 \text{ m} \approx 22 \text{ km}"),
            S("Gradient", math=r"\frac{600}{22} \approx 27 {}^\circ\text{C per km}", text="A normal to slightly warm gradient, typical of regional metamorphism in a mountain belt."),
        ], check=r"2800 \times 9.8 \times 21\,900 \approx 6.0 \times 10^{8}"),
        H("Prograde and retrograde reactions"),
        T("**Prograde** metamorphism happens as temperature (and usually pressure) rises. Most prograde reactions release water or carbon dioxide (they are **devolatilisation** reactions), because hydrous minerals such as clays, chlorite and micas become unstable on heating. "
          "**Retrograde** metamorphism happens as the rock cools. It needs water to be added back, and the water has mostly gone, so retrograde reactions are usually slow and incomplete. That is why high-grade rocks survive at the surface instead of turning back into clay and chlorite."),
        F(r"\text{CaCO}_3 + \text{SiO}_2 \rightarrow \text{CaSiO}_3 + \text{CO}_2", title="A prograde reaction in a siliceous limestone (calcite + quartz gives wollastonite)"),
        F(r"\text{muscovite} + \text{quartz} \rightarrow \text{K-feldspar} + \text{sillimanite} + \text{H}_2\text{O}", title="A high-grade dehydration reaction in pelites"),
        EX("Worked example 2: carbon dioxide released", intro="How much carbon dioxide is released when 1 tonne of calcite reacts completely with quartz to form wollastonite? (Ca = 40.08, C = 12.01, O = 16.00.)", steps=[
            S("Molar masses", math=r"M(\text{CaCO}_3) = 100.09, \quad M(\text{CO}_2) = 44.01 \text{ g mol}^{-1}"),
            S("Mass ratio", math=r"\frac{44.01}{100.09} \times 1000 \text{ kg} = 440 \text{ kg of CO}_2"),
            S("Comment", text="Contact metamorphism of limestone releases large amounts of CO₂; the fluid must escape, otherwise it slows the reaction."),
        ], check=r"0.4397 \times 1000 = 440"),
        H("Types of metamorphism"),
        KEY("Types and settings", "Name the setting, the main agent and typical rocks.", cards=[
            ["Contact (thermal)", "Around igneous intrusions; high temperature, low pressure, little stress. Forms an **aureole** of hornfels, spotted slate and marble that grades outwards into unaltered rock. Aureole width depends on the size, temperature and fluid content of the intrusion."],
            ["Regional (dynamothermal)", "Over thousands of square kilometres in orogenic belts; high temperature, pressure and directed stress. Forms foliated slate, phyllite, schist and gneiss. Example: the Pan-African belt of Cameroon; the Scottish Highlands."],
            ["Dynamic (cataclastic)", "Along fault and shear zones; intense directed stress, moderate heat. Near the surface: fault breccia and gouge; deeper: finely ground, streaky mylonite."],
            ["Burial", "In deep sedimentary basins; low temperature, moderate pressure, no stress. Zeolite minerals form; the rocks look little changed."],
            ["Hydrothermal and ocean-floor", "Hot sea water circulates through new oceanic crust at ridges; basalt changes to greenstone with chlorite, epidote and albite."],
            ["Impact (shock)", "Meteorite impacts give extreme pressure for an instant: shocked quartz and high-pressure silica (coesite, stishovite)."],
        ]),
        H("Pneumatolytic processes in contact aureoles"),
        T("The last stage of a granite releases hot gases and fluids rich in boron, fluorine, tin and tungsten. Their action on the granite and on the country rock is **pneumatolysis** (a kind of metasomatism). The Board's 2023 report says candidates who were asked to name and describe processes of contact metamorphism usually wrote about contact metamorphism in general instead. These are the processes to learn:"),
        KEY("Pneumatolytic processes", "Name, agent and product.", cards=[
            ["Tourmalinisation", "Boron-rich vapours (with some fluorine) react with the country rock or granite to form tourmaline. In a limestone or other calcium-rich rock, a calcium-boron silicate, axinite, forms."],
            ["Greisening", "Fluorine-rich vapours alter granite to greisen, a rock of quartz and white mica, sometimes with topaz and tourmaline. Extreme alteration can give a quartz-topaz rock."],
            ["Ore mineralisation", "Tin and tungsten are carried as fluorides and deposited as oxides: cassiterite (tin), and wolframite (with iron and manganese) or scheelite (with calcium)."],
            ["Skarn formation", "Fluids from the granite react with limestone to give calcium-silicate rocks (garnet, pyroxene) that may contain iron, copper or tungsten ores."],
        ]),
        MISTAKE("Answering a different question about contact metamorphism", "If asked for the processes associated with contact metamorphism, name and describe tourmalinisation, greisening and ore mineralisation (and skarn formation), each with its agent and product. Do not just define contact metamorphism or list the factors controlling metamorphism."),
        QUIZ("Which agent of metamorphism is mainly responsible for the alignment of mica flakes in a slate?", ["Confining pressure", "Directed stress", "Temperature alone", "Chemically active fluids"], 1,
             "Directed (differential) stress rotates and grows platy minerals perpendicular to the greatest stress, giving foliation.", hint="Which pressure is unequal in different directions?",
             feedback=["Confining pressure is equal in all directions, so it cannot align minerals.", "", "Heat alone, as in contact metamorphism, gives non-foliated hornfels.", "Fluids speed reactions and move ions, but do not align grains."]),
        QUIZ("Why are retrograde reactions often incomplete?", ["Retrograde metamorphism happens at higher temperature", "Water released during prograde metamorphism has escaped, and reactions are slow at lower temperatures", "Retrograde minerals are denser", "Retrograde metamorphism only affects igneous rocks"], 1,
             "Retrograde reactions need water to rehydrate the minerals and run slowly as the rock cools.", hint="What do most prograde reactions release?",
             feedback=["Retrograde means cooling, at lower temperature.", "", "Density does not stop a reaction from happening.", "Any metamorphic rock can be affected."]),
        TIP("Paper 1 tests definitions, agents and types; Paper 2 can ask you to compare contact and regional metamorphism or to describe the processes of contact metamorphism; Paper 3 may ask for the mode of formation of a specimen such as marble (contact metamorphism of a pure limestone). Always state the protolith, the agent and the setting.", title="Exam link"),
        PQ("Compare contact and regional metamorphism under the headings: setting, main agents, extent, and typical rocks.",
           "Contact: around igneous intrusions; mainly heat at low pressure, little stress; local (an aureole from metres to a few kilometres wide); non-foliated hornfels, spotted slate, marble, quartzite. Regional: in orogenic belts at convergent margins; heat, high confining pressure and directed stress; extends over thousands of square kilometres; foliated slate, phyllite, schist, gneiss, migmatite."),
        PQ("Name and describe three processes associated with contact (pneumatolytic) metamorphism around a granite.",
           "Tourmalinisation: boron-rich vapours with some fluorine react with the rock to form tourmaline (axinite in calcium-rich rocks). Greisening: fluorine-rich vapours change granite into greisen (quartz and white mica, with topaz or tourmaline). Ore mineralisation: tin and tungsten carried as fluorides react with water to form oxides: cassiterite, wolframite (with Fe and Mn) and scheelite (with Ca)."),
        PQ("A gneiss formed at 0.8 GPa and 750 °C. Estimate the depth (density 2900 kg m⁻³, g = 9.8 m s⁻²) and the geothermal gradient.",
           "Depth = 0.8 × 10⁹ ÷ (2900 × 9.8) = 28 100 m ≈ 28 km. Gradient ≈ 750 ÷ 28 ≈ 27 °C per km."),
        SUM("Metamorphism changes mineralogy and texture in the solid state, between diagenesis (about 150 to 200 °C) and melting.",
            "Agents: temperature, confining pressure, directed stress (foliation), chemically active fluids (metasomatism) and time.",
            "Prograde reactions release H₂O and CO₂; retrograde reactions need water and are usually incomplete.",
            "Types: contact (aureoles, hornfels), regional (orogenic belts, foliated rocks), dynamic (mylonite), burial, hydrothermal, impact.",
            "Pneumatolytic processes: tourmalinisation, greisening, tin-tungsten ore mineralisation and skarns."),
    ],
))

# ------------------------------------------------------------------ 8. Metamorphic textures and rocks
LESSONS.append(lesson(
    module=M_MET,
    topic="Metamorphic textures and rocks",
    title="Metamorphic textures and rocks: from slate to migmatite, marble, quartzite and hornfels",
    slug="gyl2-metamorphic-textures-rocks",
    minutes=25,
    summary="Foliated textures (slaty cleavage, phyllitic sheen, schistosity, gneissose banding) and non-foliated ones (granoblastic, hornfelsic) record stress and grade; each metamorphic rock is described by its minerals, texture, protolith and grade.",
    objectives=[
        "Describe foliated and non-foliated metamorphic textures, including porphyroblastic and augen textures",
        "Describe slate, phyllite, schist, gneiss and migmatite by mineralogy, texture and mode of formation",
        "Describe marble, quartzite, hornfels, metabasic rocks and mylonite and name their protoliths",
        "Distinguish similar specimens such as marble and quartzite, and slate and shale",
    ],
    key_concepts=["Foliation", "Slaty cleavage", "Schistosity", "Gneissose banding", "Porphyroblast", "Granoblastic", "Hornfels", "Anatexis", "Protolith", "Grade"],
    blocks=[
        H("Introduction"),
        T("A slate roof tile, a polished marble floor and a block of banded gneiss from a Cameroonian quarry are all metamorphic rocks, but they formed from different protoliths under different conditions. "
          "In examinations you must be able to describe a metamorphic rock (minerals and texture) and explain its formation (protolith, type of metamorphism and **grade**). The Board's 2023 report says many candidates described the minerals and texture well but could not explain the mode of formation, forgot to name the parent rock, or did not say whether the grade was low or high."),
        D("**Metamorphic grade** describes the intensity of metamorphism, mainly the temperature reached: low grade (about 200 to 400 °C), medium grade (about 400 to 600 °C) and high grade (above about 600 °C). The figures are approximate.", title="Grade"),
        H("Foliated textures"),
        D("**Foliation** is a planar fabric produced by the parallel alignment of platy minerals (micas, chlorite) or by layers of different minerals. A **lineation** is a linear fabric, such as aligned needles of hornblende.", title="Foliation"),
        KEY("A sequence with increasing grade (pelitic rocks)", "Grain size and the type of foliation change together.", cards=[
            ["Slaty cleavage", "Very fine-grained micas aligned perfectly, so the rock splits into thin, flat sheets. Cleavage is often at an angle to the original bedding."],
            ["Phyllitic texture", "Slightly coarser micas give a silky sheen on the foliation surfaces, which are often crinkled."],
            ["Schistosity", "Medium- to coarse-grained micas visible to the eye; the rock splits along wavy, shiny surfaces; often with porphyroblasts."],
            ["Gneissose banding", "Coarse grained; light bands of quartz and feldspar alternate with dark bands of biotite and hornblende. Fewer micas, so the rock does not split easily."],
        ]),
        KEY("Other textures", "Learn the meaning of each term.", cards=[
            ["Porphyroblastic", "Large crystals (porphyroblasts) such as garnet, staurolite or andalusite that grew in the solid state, in a finer matrix. Compare porphyritic, which is igneous."],
            ["Poikiloblastic", "Porphyroblasts full of small inclusions of the matrix minerals; trails of inclusions can record earlier fabrics."],
            ["Augen", "Eye-shaped feldspar porphyroclasts with foliation wrapped around them, in augen gneiss and mylonite."],
            ["Granoblastic (granular)", "Roughly equal-sized grains with straight boundaries meeting at about 120°, with no foliation; typical of marble, quartzite and hornfels. In marble the texture is often called saccharoidal (sugary)."],
        ]),
        H("The pelitic sequence: slate to migmatite"),
        CODE("Rock       Minerals                                   Texture                       Grade and formation\n"
             "Slate      micas (sericite, biotite), chlorite,      very fine; slaty cleavage     low-grade regional\n"
             "           quartz                                                                  metamorphism of shale\n"
             "Phyllite   muscovite, chlorite, biotite, quartz,     fine; silky phyllitic sheen   low-grade regional\n"
             "           some feldspar, epidote                                                  metamorphism of shale\n"
             "Schist     micas, quartz, feldspar, often garnet,    medium-coarse; schistosity;   medium-grade regional\n"
             "           staurolite or kyanite                     porphyroblastic               metamorphism of shale\n"
             "Gneiss     quartz, feldspar, biotite, hornblende,    coarse; gneissose banding;    high-grade regional\n"
             "           garnet, sillimanite or pyroxene           porphyroblastic               metamorphism\n"
             "Migmatite  quartz, feldspar, biotite, hornblende,    coarse; light veins of        very high grade, partial\n"
             "           garnet                                    granite in dark host          melting (anatexis)", "text", title="Table 1. Foliated rocks from a shale (pelitic) protolith"),
        T("Gneiss can form from shale (paragneiss) or from granite and other igneous rocks (orthogneiss). **Migmatite** ('mixed rock') forms when high-grade rocks begin to melt (**anatexis**): the light, granitic veins are the frozen melt and the dark parts are the unmelted residue. It marks the boundary between metamorphism and magma formation."),
        MISTAKE("Treating mica and biotite as two different minerals", "The Board's 2023 report noted that some candidates listed 'mica' and 'biotite' as two minerals. Biotite is a mica (dark mica); muscovite is the light mica. Write 'micas (biotite and muscovite)'. Also, granite is not a foliated metamorphic rock: it is igneous."),
        H("Non-foliated rocks and their protoliths"),
        KEY("Rocks that are not foliated", "These form mainly by heat, or from protoliths without platy minerals.", cards=[
            ["Marble", "Protolith: limestone or dolomite. Interlocking calcite (or dolomite) crystals, sugary (saccharoidal) texture; fizzes with dilute hydrochloric acid. Formed by contact or regional metamorphism; impurities give coloured bands."],
            ["Quartzite (metaquartzite)", "Protolith: quartz sandstone. Interlocking quartz grains; breaks across the grains, not around them; does not fizz; hardness 7 (scratches glass)."],
            ["Hornfels", "Protolith: usually shale or mudstone. Very fine-grained, hard, splintery, granoblastic; may contain andalusite or cordierite. Contact metamorphism close to an intrusion. Further out, spotted slate shows the first growth of new minerals."],
            ["Metabasic rocks", "Protolith: basalt, dolerite or gabbro. Greenschist (chlorite, epidote, actinolite, albite), amphibolite (hornblende and plagioclase), granulite and eclogite (garnet and green pyroxene) with increasing grade or pressure."],
            ["Serpentinite and mylonite", "Serpentinite: hydrated peridotite, green and soapy. Mylonite: fine-grained, streaky rock from intense shearing in a ductile shear zone."],
        ]),
        EX("Worked example 1: describing and explaining a specimen", intro="A hand specimen is coarse grained, with light bands of quartz and pink feldspar alternating with dark bands of biotite and hornblende, and a few red garnet crystals 5 mm across. Identify it and explain its formation.", steps=[
            S("Describe the minerals", text="Quartz, feldspar, biotite, hornblende and garnet."),
            S("Describe the texture", text="Coarse grained, foliated by gneissose banding, porphyroblastic (garnet)."),
            S("Identify", text="Gneiss."),
            S("Mode of formation", text="High-grade regional metamorphism (high temperature and pressure, with directed stress) of a shale (pelitic) protolith, or of an igneous rock such as granite. The banding formed by segregation of light and dark minerals during deformation."),
        ]),
        EX("Worked example 2: marble or quartzite?", intro="Two white, sugary, granoblastic specimens look alike. Describe two simple tests to tell them apart.", steps=[
            S("Acid test", text="Add a drop of dilute hydrochloric acid. Marble (calcite) fizzes, giving carbon dioxide. Quartzite does not react."),
            S("Hardness test", text="Try to scratch with a steel knife. Marble (calcite, hardness 3) is scratched. Quartzite (quartz, hardness 7) is not, and scratches glass."),
            S("Protoliths", text="Marble formed from limestone; quartzite from quartz sandstone."),
        ]),
        QUIZ("A fine-grained rock splits into thin, flat sheets along planes that cut across the original bedding. What is it?", ["Shale", "Slate", "Schist", "Hornfels"], 1,
             "Slaty cleavage is a metamorphic foliation, often oblique to bedding.", hint="Which rock splits along a fabric that is not bedding?",
             feedback=["Shale splits along its bedding (fissility), not across it.", "", "Schist is coarser, with visible micas and wavy foliation.", "Hornfels is not foliated and breaks into splintery pieces."]),
        QUIZ("A rock contains light granitic veins wrapping around dark, biotite-rich patches. What process formed it?", ["Low-grade regional metamorphism", "Partial melting (anatexis) at very high grade", "Contact metamorphism of limestone", "Shearing along a fault near the surface"], 1,
             "Migmatite records the start of melting: granitic veins are the melt, the dark parts the residue.", hint="Light veins of granite inside a metamorphic rock suggest melt.",
             feedback=["Low grade gives slate or phyllite, with no melting.", "", "Contact metamorphism of limestone gives marble.", "Near-surface shearing gives breccia or gouge."]),
        TIP("In Paper 3 you will be asked to describe and identify metamorphic specimens and to give their mode of formation; in Paper 2, to describe the composition, texture and formation of foliated rocks. Use a fixed order: minerals, texture, name, protolith, type and grade of metamorphism.", title="Exam link"),
        PQ("Describe the mineral composition, texture and mode of formation of slate and schist.",
           "Slate: very fine-grained micas (sericite, biotite) and chlorite with quartz; slaty cleavage (foliated); low-grade regional metamorphism (low temperature and pressure, with directed stress) of shale. Schist: micas (biotite and muscovite), quartz, feldspar, often garnet, staurolite or kyanite porphyroblasts; medium to coarse grained, schistose (foliated), porphyroblastic; medium-grade regional metamorphism of shale."),
        PQ("Explain why marble and quartzite are not usually foliated, even when formed by regional metamorphism.",
           "Their protoliths (limestone and quartz sandstone) are made almost entirely of one mineral, calcite or quartz, which forms roughly equal-sized (equant) grains rather than platy minerals. With no micas to align, the rock recrystallises to a granoblastic mosaic. Strong deformation can still flatten the grains a little."),
        PQ("State the protolith of each rock: amphibolite, marble, quartzite, slate, serpentinite.",
           "Amphibolite: basalt, dolerite or gabbro (basic igneous rock). Marble: limestone or dolomite. Quartzite: quartz sandstone (orthoquartzite). Slate: shale or mudstone. Serpentinite: peridotite (ultrabasic rock)."),
        SUM("Grade measures the intensity (mainly temperature) of metamorphism: low, medium, high.",
            "Foliated textures with increasing grade: slaty cleavage, phyllitic sheen, schistosity, gneissose banding; porphyroblasts grow in the solid state.",
            "Pelitic sequence: shale, slate, phyllite, schist, gneiss, migmatite (anatexis).",
            "Non-foliated: marble (limestone, fizzes), quartzite (sandstone, hard), hornfels (contact), metabasites (greenschist, amphibolite, eclogite), serpentinite.",
            "Describe minerals and texture, then name the rock, its protolith and the type and grade of metamorphism."),
    ],
))

# ------------------------------------------------------------------ 9. Index minerals and Barrow's zones
LESSONS.append(lesson(
    module=M_MET,
    topic="Index minerals and Barrow's zones",
    title="Index minerals, isograds and Barrow's zones: mapping metamorphic grade",
    slug="gyl2-index-minerals-barrow-zones",
    minutes=24,
    summary="Barrow mapped zones of increasing grade in pelitic rocks by the first appearance of index minerals (chlorite, biotite, garnet, staurolite, kyanite, sillimanite); isograds separate the zones, and the aluminosilicates and Buchan zones show how pressure also matters.",
    objectives=[
        "Define index mineral, isograd and metamorphic zone",
        "List Barrow's zones in order and link each to the pelitic rock type",
        "Use the aluminosilicate polymorphs and the Buchan sequence to compare pressure conditions",
        "Interpret a map of isograds, including the field gradient and the position of the heat source",
    ],
    key_concepts=["Index mineral", "Isograd", "Metamorphic zone", "Barrovian zones", "Buchan zones", "Aluminosilicate polymorphs", "Field gradient"],
    blocks=[
        H("Introduction"),
        T("In the 1890s the Scottish geologist George Barrow mapped the rocks of the south-eastern Scottish Highlands. He noticed that shales had changed step by step across the region, and that the change could be followed by the appearance of particular minerals. "
          "His method, mapping zones of metamorphism by their minerals, is still used in metamorphic belts all over the world, including the Pan-African belt of central Africa."),
        D("An **index mineral** is a mineral whose first appearance, as rocks of the same composition are followed across an area, marks a particular grade of metamorphism. "
          "An **isograd** is a line on a map joining points where the index mineral first appears; it joins places that reached about the same grade. A **metamorphic zone** is the belt between two isograds, named after the index mineral of its lower-grade isograd.", title="Index mineral, isograd, zone"),
        H("Barrow's zones"),
        IMG("algyl2-barrow.svg", alt="Strip divided into six coloured zones from left to right: chlorite, biotite, garnet, staurolite, kyanite and sillimanite, separated by dashed isograds, with rock names slate, phyllite, schist, schist, schist, gneiss below, and an arrow showing grade increasing to the right",
            caption="Figure 1. Barrow's zones in pelitic rocks (schematic). Each dashed isograd marks the first appearance of the next index mineral."),
        KEY("Zones in order of increasing grade", "Approximate temperatures are rough guides only; textbooks differ.", cards=[
            ["Chlorite zone", "Slates and phyllites with chlorite, muscovite and quartz (low grade, below about 400 °C)."],
            ["Biotite zone", "Biotite appears; phyllites and fine schists (about 400 to 450 °C)."],
            ["Garnet zone", "Red almandine garnet porphyroblasts appear in schists (about 500 °C)."],
            ["Staurolite zone", "Brown staurolite, often in cross-shaped twins, appears in schists (about 550 °C)."],
            ["Kyanite zone", "Blue blade-like kyanite appears in coarse schists (about 600 °C)."],
            ["Sillimanite zone", "Fibrous sillimanite appears in gneisses; partial melting may begin (above about 650 °C)."],
        ]),
        T("Each new index mineral forms by a reaction among the minerals already present. For example (simplified), chlorite reacts with muscovite to form biotite; chlorite and other minerals react to form garnet; and kyanite changes into sillimanite at higher temperature. "
          "An index mineral usually stays stable into higher zones (garnet is still present in the kyanite and sillimanite zones), which is why a zone is defined by the **first** appearance of its mineral."),
        MISTAKE("Using index minerals in the wrong rock type", "Barrow's sequence applies to pelitic rocks (metamorphosed shales and mudstones), rich in aluminium. A metamorphosed limestone or sandstone of the same grade will not contain staurolite or kyanite, because it lacks the chemical ingredients. Compare only rocks of the same composition."),
        H("Pressure matters too: the aluminosilicates and Buchan zones"),
        T("Kyanite, andalusite and sillimanite are three **polymorphs** of Al₂SiO₅: the same chemical formula with different crystal structures. Kyanite is stable at high pressure, andalusite at low pressure and sillimanite at high temperature. The three fields meet at a **triple point**, at roughly 500 °C and 0.4 GPa (published values differ; check your textbook). "
          "In Barrow's area, kyanite appears before sillimanite, so the rocks passed through the kyanite field: moderate to high pressure. In the Buchan area of north-east Scotland, the sequence is biotite, cordierite, andalusite, sillimanite: andalusite and cordierite show **lower pressure** at the same temperatures."),
        KEY("Barrovian and Buchan sequences", "Two kinds of regional metamorphism.", cards=[
            ["Barrovian (medium pressure)", "chlorite, biotite, garnet, staurolite, kyanite, sillimanite. Typical of thickened crust in collision belts."],
            ["Buchan (low pressure)", "biotite, cordierite, andalusite, sillimanite. Typical of areas with a high geothermal gradient, for example where many granites were intruded."],
        ]),
        EX("Worked example 1: reading a map of isograds", intro="On a map, a garnet isograd and a sillimanite isograd run roughly north-south, parallel to each other, 12 km apart, and the grade rises towards the east. Using teaching values of 500 °C for the garnet isograd and 650 °C for the sillimanite isograd, estimate the temperature change per kilometre across the map, and say where the heat source probably lay.", steps=[
            S("Temperature difference", math=r"650 - 500 = 150 {}^\circ\text{C}"),
            S("Gradient across the map", math=r"\frac{150}{12} = 12.5 {}^\circ\text{C per km of map distance}"),
            S("Interpret", text="This is a field gradient across the land surface, not a geothermal gradient with depth. Grade rises to the east, so the hottest rocks, perhaps the core of the mountain belt or a large intrusion at depth, lay to the east."),
        ], check=r"12.5 \times 12 = 150"),
        EX("Worked example 2: placing a specimen in a zone", intro="A pelitic schist contains muscovite, biotite, garnet and staurolite, but no kyanite or sillimanite. Which zone is it from, and what was the approximate grade?", steps=[
            S("Highest index mineral", text="Staurolite is the highest-grade index mineral present."),
            S("Zone", text="Staurolite zone: above the staurolite isograd but below the kyanite isograd."),
            S("Grade", text="Medium grade, roughly 550 to 600 °C (teaching values)."),
        ]),
        T("**Evaluation.** Barrow's method is simple and visual and works with a hand lens. But the appearance of a mineral depends on rock composition, on pressure and on the amount of water, so an isograd is not exactly a line of equal temperature. Modern geologists use mineral assemblages (facies) and chemical thermometers and barometers alongside index minerals."),
        QUIZ("What does an isograd join on a geological map?", ["Places of equal height", "Points where an index mineral first appears, showing about the same metamorphic grade", "Points where beds of the same age outcrop", "Places where a granite meets the country rock"], 1,
             "An isograd marks the first appearance of an index mineral in rocks of a given composition.", hint="Iso = equal, grad = grade.",
             feedback=["Those are contours.", "", "That describes an outcrop pattern of a bed.", "That is an igneous contact."]),
        QUIZ("A sequence of pelitic rocks contains andalusite and cordierite in the middle-grade zones instead of staurolite and kyanite. What does this suggest?", ["Higher pressure than in Barrow's area", "Lower pressure (a higher geothermal gradient) than in Barrow's area", "No metamorphism has taken place", "The rocks are limestones"], 1,
             "Andalusite and cordierite are low-pressure minerals: this is a Buchan-type sequence.", hint="Which Al₂SiO₅ polymorph is stable at low pressure?",
             feedback=["Higher pressure would favour kyanite.", "", "Andalusite and cordierite are metamorphic minerals.", "Limestones lack the aluminium to form these minerals."]),
        TIP("Barrow's zones appear in Paper 1 as order and definition questions, and in Paper 2 as 'describe and explain' questions with a labelled sketch map of zones. Always state that the zones are defined in pelitic rocks by the first appearance of the index mineral, and give the order correctly.", title="Exam link"),
        PQ("Define the terms index mineral and isograd, and list Barrow's zones in order of increasing grade.",
           "Index mineral: a mineral whose first appearance in rocks of a given (pelitic) composition marks a particular grade. Isograd: a line on a map joining points where the index mineral first appears. Zones: chlorite, biotite, garnet, staurolite, kyanite, sillimanite."),
        PQ("Explain why a metamorphosed limestone next to a kyanite-zone schist contains no kyanite.",
           "Kyanite is Al₂SiO₅. Limestone is mainly calcium carbonate and lacks the aluminium and silica needed, so at the same grade it recrystallises to marble with calcite (and calc-silicate minerals if impure). Index minerals can only be compared in rocks of the same composition."),
        PQ("Compare Barrovian and Buchan metamorphism.",
           "Both are regional metamorphism of pelitic rocks recorded by zones of index minerals. Barrovian: chlorite, biotite, garnet, staurolite, kyanite, sillimanite; kyanite shows moderate to high pressure; typical of thickened collision belts. Buchan: biotite, cordierite, andalusite, sillimanite; andalusite and cordierite show low pressure and a high geothermal gradient, often linked to many granite intrusions."),
        SUM("An index mineral's first appearance marks a grade; isograds join those points; zones lie between isograds.",
            "Barrow's zones in pelites: chlorite, biotite, garnet, staurolite, kyanite, sillimanite (slate to gneiss).",
            "Kyanite (high pressure), andalusite (low pressure) and sillimanite (high temperature) are Al₂SiO₅ polymorphs.",
            "Buchan zones (biotite, cordierite, andalusite, sillimanite) show lower pressure than Barrovian zones.",
            "Isograd maps show the direction of increasing grade and the field gradient; compare only rocks of the same composition."),
    ],
))

# ------------------------------------------------------------------ 10. Metamorphic facies
LESSONS.append(lesson(
    module=M_MET,
    topic="Metamorphic facies",
    title="Metamorphic facies: mineral assemblages as pressure-temperature gauges",
    slug="gyl2-metamorphic-facies",
    minutes=25,
    summary="A metamorphic facies is a set of mineral assemblages formed under a particular range of pressure and temperature, named after metamorphosed basalt; zeolite, greenschist, amphibolite, granulite, blueschist, eclogite and hornfels facies link rocks to geothermal gradients and plate settings.",
    objectives=[
        "Define a metamorphic facies and explain why facies are named from metabasic rocks",
        "Describe the characteristic mineral assemblages of the main facies and place them on a P-T diagram",
        "Calculate depth and geothermal gradient from a facies' pressure and temperature",
        "Relate facies series and paired metamorphic belts to plate tectonic settings",
    ],
    key_concepts=["Metamorphic facies", "Mineral assemblage", "Greenschist", "Amphibolite", "Granulite", "Blueschist", "Eclogite", "Hornfels facies", "Facies series", "Paired metamorphic belts"],
    blocks=[
        H("Introduction"),
        T("Barrow's zones work in shales. But what about a metamorphosed basalt, or a region where the rocks are of many kinds? In the early twentieth century the Finnish geologist Pentti Eskola proposed a more general idea: rocks of the same composition, metamorphosed under the same conditions, always end up with the same set of minerals. "
          "So the mineral assemblage of a rock is a gauge of the pressure and temperature it reached."),
        D("A **metamorphic facies** is a set of mineral assemblages that formed under a particular range of pressure and temperature. Each facies is named after the assemblage that forms in a metamorphosed basalt (a **metabasite**), but it applies to all rock compositions at those conditions. "
          "A **mineral assemblage** is the group of minerals that grew together in equilibrium.", title="Facies"),
        T("Basalt is used because it is common, it occurs in almost every setting, and its minerals change clearly with pressure and temperature. A shale and a basalt in the amphibolite facies will contain different minerals, but both formed at medium to high temperature and medium pressure."),
        IMG("algyl2-facies.svg", alt="P-T diagram, pressure increasing downward: zeolite at low T, hornfels at very low P, greenschist, amphibolite and granulite with rising T, blueschist at low T and high P, eclogite at high P, and a dashed line for conditions not reached on Earth",
            caption="Figure 1. Metamorphic facies (schematic). Some textbooks also show a prehnite-pumpellyite facies between zeolite and greenschist, and divide hornfels into several facies."),
        KEY("Facies and their assemblages in metabasites", "Learn the key minerals.", cards=[
            ["Zeolite", "Zeolites with clays; very low grade, burial metamorphism."],
            ["Greenschist", "Chlorite + actinolite + epidote + albite: green, often schistose. Low-grade regional and ocean-floor metamorphism."],
            ["Amphibolite", "Hornblende + plagioclase (± garnet). Medium to high-grade regional metamorphism."],
            ["Granulite", "Pyroxenes (orthopyroxene and clinopyroxene) + plagioclase (± garnet); hydrous minerals gone. Very high temperature in the deep crust."],
            ["Blueschist", "Glaucophane (a blue amphibole) + lawsonite: high pressure at low temperature, found only in subduction zones."],
            ["Eclogite", "Omphacite (green sodium pyroxene) + red garnet; no plagioclase. Very high pressure, deep subduction or the roots of collision belts. Dense (about 3.4 g cm⁻³)."],
            ["Hornfels facies", "Fine granoblastic rocks of contact aureoles; high temperature at very low pressure (albite-epidote, hornblende and pyroxene hornfels with rising temperature)."],
        ]),
        H("Facies, depth and geothermal gradient"),
        T("Because pressure gives depth and temperature gives heat, each facies indicates a **geothermal gradient**. Blueschists and eclogites need low gradients (cold rock carried deep quickly). Greenschist and amphibolite form at normal gradients of about 20 to 35 °C per km. Hornfels and granulites in some settings need high gradients (heat added by magma)."),
        EX("Worked example 1: a blueschist", intro="A blueschist formed at about 1.0 GPa and 300 °C. Taking an average density of 3000 kg m⁻³ and g = 9.8 m s⁻², find the depth and the geothermal gradient.", steps=[
            S("Depth", math=r"h = \frac{1.0 \times 10^{9}}{3000 \times 9.8} = 34\,000 \text{ m} = 34 \text{ km}"),
            S("Gradient", math=r"\frac{300}{34} \approx 9 {}^\circ\text{C per km}"),
            S("Interpret", text="This is far colder than a normal gradient. Only a subducting slab, carried down faster than it can heat up, reaches such conditions."),
        ], check=r"3000 \times 9.8 \times 34\,000 \approx 1.0 \times 10^{9}"),
        EX("Worked example 2: an amphibolite and a hornfels", intro="Compare an amphibolite formed at 0.6 GPa and 600 °C with a hornfels formed at 0.1 GPa and 600 °C (density 2800 kg m⁻³).", steps=[
            S("Amphibolite depth and gradient", math=r"h = \frac{0.6 \times 10^{9}}{2800 \times 9.8} = 21.9 \text{ km}, \quad \frac{600}{21.9} = 27 {}^\circ\text{C km}^{-1}"),
            S("Hornfels depth and gradient", math=r"h = \frac{0.1 \times 10^{9}}{2800 \times 9.8} = 3.6 \text{ km}, \quad \frac{600}{3.6} \approx 165 {}^\circ\text{C km}^{-1}"),
            S("Interpret", text="The amphibolite fits a normal regional gradient. The 'gradient' of the hornfels is impossible on a regional scale: the heat came from a nearby intrusion. Contact metamorphism."),
        ], check=r"600 \div 3.64 = 165"),
        H("Facies series and plate settings"),
        T("Rocks heated and buried along one geothermal gradient pass through a **facies series**: for example zeolite, greenschist, amphibolite, granulite in a collision belt (medium pressure), or zeolite, blueschist, eclogite in a subduction zone (high pressure, low temperature). "
          "In Japan, the geologist Akiho Miyashiro described **paired metamorphic belts**: a high-pressure, low-temperature belt (blueschist) on the ocean side, formed in the subduction zone, and a parallel low-pressure, high-temperature belt (hornfels, andalusite-bearing rocks) on the continent side, formed beneath the volcanic arc. Paired belts are evidence of former subduction zones."),
        MISTAKE("Thinking a facies is a rock name", "A facies is a range of pressure and temperature conditions, identified by mineral assemblages. 'Amphibolite' is both a rock name and a facies name, which causes confusion: a schist with garnet and kyanite can belong to the amphibolite facies without being an amphibolite."),
        T("**Evaluation.** The facies concept is powerful because a single thin section can tell you the approximate conditions and the setting. Its limits: facies boundaries are gradational reactions, not sharp lines; assemblages depend on water and on rock composition; and the assemblage records mainly the peak conditions, not the whole history (the next lesson deals with that)."),
        QUIZ("A metabasite contains glaucophane and lawsonite. In which facies and setting did it form?", ["Granulite facies in the deep continental crust", "Blueschist facies in a subduction zone", "Greenschist facies at a mid-ocean ridge", "Hornfels facies around a granite"], 1,
             "Glaucophane and lawsonite form at high pressure and low temperature: blueschist facies, found in subduction zones.", hint="Glaucophane is a blue amphibole.",
             feedback=["Granulites form at very high temperature with pyroxenes.", "", "Greenschist facies has chlorite, actinolite, epidote and albite.", "Hornfels forms at low pressure."]),
        QUIZ("Why are facies named after the minerals in metamorphosed basalt?", ["Basalt is the only rock that changes during metamorphism", "Basalt is widespread in many settings and its minerals change clearly with pressure and temperature", "Basalt contains index minerals such as kyanite", "Basalt melts at the lowest temperature"], 1,
             "Metabasites are common and sensitive gauges of P and T.", hint="Think about where basalt is found.",
             feedback=["All rock types change.", "", "Kyanite is an index mineral of pelites.", "Granite, not basalt, melts at the lowest temperature."]),
        TIP("Facies appear in Paper 1 (characteristic minerals, positions on a P-T diagram) and in Paper 2 (link facies to plate settings; paired belts). Learn the key assemblage of each facies and draw a simple labelled P-T sketch with temperature on one axis and pressure (depth) on the other.", title="Exam link"),
        PQ("Name the facies in which each assemblage formed: (a) chlorite + actinolite + epidote + albite; (b) omphacite + garnet; (c) hornblende + plagioclase + garnet; (d) orthopyroxene + clinopyroxene + plagioclase.",
           "(a) Greenschist facies. (b) Eclogite facies. (c) Amphibolite facies. (d) Granulite facies."),
        PQ("An eclogite formed at 1.2 GPa and 650 °C. Estimate the depth (density 3000 kg m⁻³, g = 9.8 m s⁻²) and the geothermal gradient, and comment on the setting.",
           "Depth = 1.2 × 10⁹ ÷ (3000 × 9.8) = 40 800 m ≈ 41 km. Gradient ≈ 650 ÷ 41 ≈ 16 °C per km. A fairly low gradient at great depth: a subducted slab or the root of a thickened collision belt."),
        PQ("Explain how paired metamorphic belts provide evidence of a former subduction zone.",
           "In a subduction zone, the cold slab carries rocks deep quickly, giving high-pressure, low-temperature blueschist (and eclogite) on the ocean side. Beneath the volcanic arc, rising magma heats the crust at shallow depth, giving low-pressure, high-temperature rocks on the continent side. Two parallel belts of contrasting facies, with the high-pressure belt nearer the old trench, show where and in which direction subduction occurred."),
        SUM("A facies is a range of P and T recognised by a mineral assemblage; facies are named from metabasites.",
            "Greenschist (chlorite, actinolite, epidote, albite), amphibolite (hornblende, plagioclase), granulite (pyroxenes, plagioclase).",
            "Blueschist (glaucophane, lawsonite) and eclogite (omphacite, garnet) need high pressure at low to moderate temperature.",
            "Hornfels facies: high temperature at low pressure, contact aureoles.",
            "Depth = P ÷ (ρg); gradient = T ÷ depth; facies series and paired belts reveal plate settings."),
    ],
))

# ------------------------------------------------------------------ 11. Pressure-temperature-time paths
LESSONS.append(lesson(
    module=M_MET,
    topic="Pressure-temperature-time paths",
    title="Pressure-temperature-time (P-T-t) paths: reading the journey of a metamorphic rock",
    slug="gyl2-pt-t-paths",
    minutes=24,
    summary="A P-T-t path traces the changing pressure and temperature of a rock through time; clockwise paths record burial then heating then uplift in collision belts, anticlockwise paths heating before burial, and the evidence comes from inclusions, zoning, reaction textures and dating.",
    objectives=[
        "Define a P-T-t path and distinguish peak pressure from peak temperature",
        "Describe clockwise and anticlockwise paths and the tectonic settings that produce them",
        "Explain the evidence used to reconstruct a path: inclusions, zoned garnet, reaction textures, polymorphs and dating",
        "Calculate burial depth, exhumation and cooling rates from P-T-t data",
    ],
    key_concepts=["P-T-t path", "Peak metamorphism", "Clockwise path", "Anticlockwise path", "Exhumation", "Geothermobarometry", "Zoned garnet", "Reaction texture"],
    blocks=[
        H("Introduction"),
        T("A metamorphic rock collected at the surface has made a long journey: down to depth, heated, then back up again. Facies and index minerals tell us roughly the highest conditions it reached. But geologists want the whole story: how deep it went, when it was hottest, and how fast it came back. "
          "That story, drawn on a pressure-temperature diagram with times added, is a **P-T-t path** (pressure-temperature-time path)."),
        D("A **P-T-t path** is the sequence of pressure and temperature conditions that a rock passed through, with the time at which each was reached. **Peak pressure** is the deepest point of the path and **peak temperature** its hottest point; they are often reached at different times.", title="P-T-t path"),
        IMG("algyl2-ptt.svg", alt="P-T diagram, pressure increasing upwards, with kyanite, andalusite and sillimanite fields meeting near 500 degrees and 0.4 GPa, and a clockwise path: 1 low pressure, 2 peak pressure in kyanite, 3 peak temperature in sillimanite, 4 near the surface",
            caption="Figure 1. A clockwise P-T-t path in a collision belt (schematic), drawn with pressure increasing upwards, as in most textbooks. The grey lines are the Al₂SiO₅ boundaries."),
        H("The clockwise path"),
        KEY("Four stages (Figure 1)", "Typical of continental collision and crustal thickening.", cards=[
            ["1 to 2: burial", "Thrusting stacks rocks quickly. Pressure rises fast, but rock heats slowly because it conducts heat poorly, so the path climbs steeply. Kyanite grows."],
            ["2: peak pressure", "Thickening stops. The rock is at its deepest but has not yet caught up thermally."],
            ["2 to 3: heating", "Heat from radioactive decay in the thickened crust, and from below, warms the rock, while erosion begins to lift it. Peak temperature is reached after peak pressure. Kyanite changes to sillimanite."],
            ["3 to 4: exhumation", "Erosion and extension bring the rock up and it cools. Retrograde reactions are slow and incomplete because water is scarce, so the peak assemblage survives."],
        ]),
        T("Plotted with pressure increasing upwards (Figure 1), this path turns in the same direction as the hands of a clock, so it is called **clockwise**. An **anticlockwise** path heats first and is buried later: for example in a magmatic arc or a rift, where intruded magma heats the crust at shallow depth, and later loading by lavas and intrusions increases the pressure. Some paths show almost **isothermal decompression** (rapid uplift without cooling) or **isobaric cooling** (cooling at constant depth)."),
        MISTAKE("Mixing up the direction of a path when the axis is flipped", "Some diagrams draw pressure (depth) increasing downwards. Then a clockwise path looks anticlockwise on the page. Always check the axes, and describe the path in words: 'burial before heating' or 'heating before burial'."),
        H("How the path is reconstructed"),
        KEY("Evidence", "Each type of evidence records a different part of the path.", cards=[
            ["Inclusions in porphyroblasts", "A garnet that grew early may trap minerals of the earlier assemblage, such as chloritoid or kyanite, preserving the prograde stage."],
            ["Zoned garnet", "Garnet grows outward. The composition of each zone records the conditions when it grew; chemical thermometers and barometers (geothermobarometry, such as the garnet-biotite thermometer) are applied to core and rim."],
            ["Reaction textures", "Coronas (rims of new minerals around old ones) and pseudomorphs (a new mineral in the shape of an old one) show reactions during heating or decompression."],
            ["Aluminosilicate polymorphs", "Kyanite replaced by sillimanite shows heating or decompression across that boundary; andalusite replacing kyanite shows decompression."],
            ["Radiometric dating", "Different minerals record different stages: for example the age of growth of garnet or zircon rims, and later cooling ages from micas. This adds the 't' to the path."],
        ]),
        EX("Worked example 1: depth at peak pressure", intro="Garnet cores in a schist record a peak pressure of 0.9 GPa. Estimate the depth reached (density 2900 kg m⁻³, g = 9.8 m s⁻²).", steps=[
            S("Formula", math=r"h = \frac{P}{\rho g}"),
            S("Calculate", math=r"h = \frac{0.9 \times 10^{9}}{2900 \times 9.8} = 31\,700 \text{ m} \approx 32 \text{ km}"),
        ], check=r"2900 \times 9.8 \times 31\,700 \approx 9.0 \times 10^{8}"),
        EX("Worked example 2: rates from dating", intro="Dating shows that a rock was at 35 km depth and 650 °C at 40 million years ago (Ma), had cooled to 300 °C by 25 Ma, and reached the surface by 10 Ma. Calculate the average exhumation rate and the cooling rate between 40 and 25 Ma.", steps=[
            S("Exhumation", math=r"\frac{35 \text{ km}}{40 - 10 = 30 \text{ Myr}} = 1.17 \text{ km per Myr} = 1.17 \text{ mm per year}", text="1 km per million years equals 1 mm per year."),
            S("Cooling", math=r"\frac{650 - 300}{40 - 25} = \frac{350}{15} = 23 {}^\circ\text{C per Myr}"),
            S("Interpret", text="Rapid exhumation of about a millimetre a year is typical of active mountain belts, where erosion and faulting remove the overlying rock."),
        ], check=r"1.17 \times 30 \approx 35"),
        T("**Evaluation.** P-T-t paths turn metamorphic rocks into records of tectonic processes and allow tectonic models (thickening, subduction, extension) to be tested. But each point carries uncertainties of perhaps ±50 °C and ±0.1 GPa, the early part of the path is often erased by later growth, and the assumption that minerals were in equilibrium may not hold. Paths are best treated as models built from several kinds of evidence."),
        QUIZ("In a clockwise P-T-t path for a collision belt, why is peak temperature reached after peak pressure?", ["Rock heats instantly when buried", "Rock conducts heat slowly, so it keeps warming after burial stops and while uplift begins", "Peak temperature is reached at the surface", "Pressure increases during uplift"], 1,
             "Thermal relaxation lags behind rapid burial; the rock continues heating as it begins to rise.", hint="Is burial or heating faster?",
             feedback=["Rock is a poor conductor; heating is slow.", "", "Rocks cool as they approach the surface.", "Pressure falls during uplift."]),
        QUIZ("Kyanite crystals in a gneiss are partly replaced by sillimanite. What does this show?", ["The rock was cooled at high pressure", "The rock crossed from the kyanite field into the sillimanite field, by heating or decompression", "The rock was weathered at the surface", "The rock never left the kyanite field"], 1,
             "Sillimanite replacing kyanite records a change of conditions across the kyanite-sillimanite boundary.", hint="Where is sillimanite stable?",
             feedback=["Cooling at high pressure would keep kyanite stable.", "", "Weathering produces clays, not sillimanite.", "The new sillimanite shows it did leave that field."]),
        TIP("P-T-t paths are an advanced topic. In Paper 1 expect questions on the shape of a path, peak pressure and peak temperature and the meaning of polymorph textures; in Paper 2 you may be asked to sketch and explain a clockwise path for a collision belt. Label the axes, the stages and the aluminosilicate fields.", title="Exam link"),
        PQ("Sketch a clockwise P-T-t path for a rock in a continental collision zone and explain each stage.",
           "Axes: temperature (horizontal), pressure or depth (vertical, increasing upwards); Al₂SiO₅ fields as reference. Stage 1 to 2: rapid burial by thrusting, pressure rises faster than temperature (steep path, kyanite grows). Stage 2: peak pressure. Stage 2 to 3: heating from radioactive and basal heat while erosion starts lifting the rock; peak temperature after peak pressure (sillimanite grows). Stage 3 to 4: exhumation and cooling; retrograde reactions limited by lack of water, so peak minerals survive."),
        PQ("A rock reached 0.6 GPa (density 2800 kg m⁻³) at 30 Ma and reached the surface at 12 Ma. Calculate the depth and the average exhumation rate in mm per year.",
           "Depth = 0.6 × 10⁹ ÷ (2800 × 9.8) = 21 900 m ≈ 21.9 km. Time = 30 − 12 = 18 Myr. Rate = 21.9 ÷ 18 = 1.2 km per Myr = 1.2 mm per year."),
        PQ("Describe two kinds of evidence in a metamorphic rock that can be used to reconstruct its P-T-t path.",
           "Any two: zoned garnet, whose core and rim compositions record different conditions (geothermobarometry); inclusions of early minerals trapped in porphyroblasts; reaction textures such as coronas and pseudomorphs; replacement of one Al₂SiO₅ polymorph by another (kyanite by sillimanite); radiometric ages of different minerals giving the time of each stage."),
        SUM("A P-T-t path records how the pressure and temperature of a rock changed through time; peak P and peak T are often at different times.",
            "Clockwise (pressure up the page): burial, then heating, then exhumation: collision belts.",
            "Anticlockwise: heating before burial: magmatic arcs and rifts.",
            "Evidence: inclusions, zoned garnet and geothermobarometry, coronas and pseudomorphs, polymorph replacement, and radiometric dates.",
            "Depth = P ÷ (ρg); exhumation rate in km per Myr equals mm per year."),
    ],
))

# ------------------------------------------------------------------ Examination 1. Paper 1
LESSONS.append(lesson(
    module=M_EXAM,
    topic="Paper 1",
    title="Paper 1: working through 50 multiple-choice questions in geology",
    slug="gyl2-paper1-multiple-choice",
    minutes=23,
    summary="How to approach the 50 multiple-choice questions of Geology Paper 1: what the Board's 2023 report says about the paper, a routine for each question, quick calculations, the traps built into wrong options, and a revision map of the five Lower Sixth modules.",
    objectives=[
        "Describe the structure of Paper 1 and the balance of skills it tests",
        "Use a routine for every question: read, predict, eliminate, check",
        "Do the common Lower Sixth calculations quickly and check them against the options",
        "Recognise the misconceptions that wrong options are built on and plan revision across all five modules",
    ],
    key_concepts=["Stem", "Distractor", "Elimination", "Table of specifications", "Command word", "Time per question", "Revision map"],
    blocks=[
        H("Introduction"),
        T("According to the Board's 2023 subject report, Geology Paper 1 consisted of 50 multiple-choice questions covering the whole Advanced Level syllabus, weighted 30% of the examination. It was marked electronically and every question carried one mark. "
          "The report's table of specifications shows that about 40% of the paper tested knowledge, about a quarter comprehension, and the rest application, analysis, synthesis and evaluation. So recall matters, but more than a third of the marks need you to use what you know. "
          "In the KKEVO mock that goes with this lesson we allow 90 minutes for 50 questions (a KKEVO practice setting, not a Board timing): a little under two minutes per question."),
        H("A routine for every question"),
        KEY("Four steps", "Do them in order, quickly.", cards=[
            ["1. Read the stem", "Find the key words: which, NOT, most likely, best explains. Note units and numbers. Decide whether it asks about a mineral, a rock, a process or a structure."],
            ["2. Predict", "Answer in your head before reading the options. This protects you from attractive wrong options."],
            ["3. Eliminate", "Cross out options you know are wrong and say why: each is built on a real misconception."],
            ["4. Check", "Re-read the stem with your chosen option. For calculations, check units and size (is 17 km a sensible root depth?)."],
        ]),
        T("If you cannot decide within about two minutes, choose your best answer, mark the question and move on. Come back at the end. Do not leave any question blank: a blank cannot score. (In the KKEVO mock a wrong answer simply scores nothing; follow your teacher's guidance for the real paper.)"),
        H("Quick calculations"),
        T("Several Lower Sixth topics give short calculations. Learn the formula, write it in the margin, substitute with units, then compare with the options. The commonest are: P = ρgh and depth from pressure; Airy isostasy; heat flow q = k dT/dz; palaeolatitude from tan I = 2 tan λ; Miller indices; the lever rule; QAPF recalculation; magnification of the microscope."),
        EX("Worked example 1: Miller indices", intro="A face cuts the a axis at 2 units, the b axis at 3 units and is parallel to the c axis. What are its Miller indices? A (230), B (320), C (23∞), D (110).", steps=[
            S("Predict: intercepts", math=r"2, \; 3, \; \infty"),
            S("Reciprocals", math=r"\tfrac{1}{2}, \; \tfrac{1}{3}, \; 0"),
            S("Clear fractions (multiply by 6)", math=r"(3\,2\,0)", text="The answer is B. A forgets to take reciprocals; C writes the intercepts; D has no basis."),
        ], check=r"6 \times \tfrac{1}{2} = 3, \; 6 \times \tfrac{1}{3} = 2"),
        EX("Worked example 2: Airy isostasy", intro="A mountain range stands 3 km above sea level. With crust density 2.8 g cm⁻³ and mantle density 3.3 g cm⁻³, how deep is its root below normal crust (Airy model)? A 3.5 km, B 9.9 km, C 16.8 km, D 19.8 km.", steps=[
            S("Formula", math=r"r = \frac{h\rho_c}{\rho_m - \rho_c}"),
            S("Substitute", math=r"r = \frac{3 \times 2.8}{3.3 - 2.8} = \frac{8.4}{0.5} = 16.8 \text{ km}"),
            S("Eliminate", text="C is correct. D uses the mantle density on top (3 × 3.3 ÷ 0.5). B is 3 × 3.3 with no division. A is 3 × 3.3 ÷ 2.8, a wrong formula."),
        ], check=r"16.8 \times 0.5 = 3 \times 2.8"),
        EX("Worked example 3: a phase-diagram question", intro="In the diopside-anorthite system (eutectic at 1274 °C, 42% anorthite), a melt with 70% anorthite cools slowly. Which mineral forms first? A diopside, B anorthite, C both together, D neither, the melt forms glass.", steps=[
            S("Predict", text="70% lies on the anorthite side of the eutectic, so anorthite crystallises first."),
            S("Eliminate", text="A is true only for melts with less than 42% anorthite; C happens only at the eutectic; D needs very fast cooling, but the stem says slowly. Answer B."),
        ]),
        H("Traps built into wrong options"),
        KEY("Common distractors in geology", "Recognise them before they catch you.", cards=[
            ["Mineral for rock", "Offering a mineral (muscovite, calcite) where a rock (schist, limestone) is asked, or the reverse. The Board's 2023 report notes candidates confusing them."],
            ["Neighbouring item in a sequence", "The next zone in Barrow's sequence, the next mineral in Bowen's series, the next discontinuity: check the order carefully."],
            ["Reversed relationship", "Higher for lower, older for younger, plutonic for volcanic, dense for light. Re-read the direction in the stem."],
            ["Unfinished calculation", "The result of the first step only: intercepts instead of Miller indices, depth instead of gradient."],
            ["Similar terms", "Porphyritic and porphyroblastic; antiform and anticline; isograd and isogram; tetrad (iv) and triad (iii) axes."],
        ]),
        H("Revision map: the five Lower Sixth modules"),
        T("The KKEVO mock samples every module roughly in proportion to its number of topics. Use this map for revision."),
        CODE("Module                               Be ready for\n"
             "Geophysics & Global Plate Tectonics  seismic waves and discontinuities, refraction,\n"
             "                                     gravity anomalies, isostasy, palaeomagnetism,\n"
             "                                     heat flow, plate boundaries, Wilson cycle\n"
             "Crystallography                      symmetry elements, seven systems and axes,\n"
             "                                     Miller indices, stereograms, 32 classes\n"
             "Optical & Systematic Mineralogy      PPL and XPL, relief, birefringence, extinction,\n"
             "                                     silicate structures, rock-forming and ore minerals\n"
             "Igneous Petrology                    melting, Bowen's series, phase diagrams, textures,\n"
             "                                     QAPF, plate settings\n"
             "Metamorphic Petrology                agents and types, textures and rocks, Barrow's\n"
             "                                     zones, facies, P-T-t paths", "text", title="Table 1. Lower Sixth revision map"),
        MISTAKE("Changing a correct answer without a reason", "Change an answer only if you find a definite error in your reasoning, such as a misread word or a wrong step in a calculation, not because of a feeling."),
        MISTAKE("Spending too long on one item", "Every question carries the same single mark. If a calculation or diagram needs more than about two minutes, mark it and return later."),
        QUIZ("A question asks: 'Which of these is NOT a member of the discontinuous series of Bowen's reaction series?' Options: A olivine, B pyroxene, C labradorite, D biotite. What is the answer?", ["A", "B", "C", "D"], 2,
             "Labradorite is a plagioclase feldspar of the continuous series; the others are ferromagnesian minerals of the discontinuous series.", hint="In a NOT question, find the odd one out.",
             feedback=["Olivine is the first mineral of the discontinuous series.", "Pyroxene is in the discontinuous series.", "", "Biotite is the last ferromagnesian mineral of the discontinuous series."]),
        QUIZ("Heat flow q = k dT/dz. A rock has k = 2.5 W m⁻¹ K⁻¹ and the gradient is 25 °C per km. What is q?", ["62.5 W m⁻²", "62.5 mW m⁻²", "0.1 mW m⁻²", "10 mW m⁻²"], 1,
             "dT/dz = 0.025 K m⁻¹, so q = 2.5 × 0.025 = 0.0625 W m⁻² = 62.5 mW m⁻².", hint="Convert the gradient to kelvin per metre first.",
             feedback=["The number is right but the unit is a thousand times too big: the gradient was not converted from per km to per m.", "", "That divides the gradient by k.", "That divides 25 by 2.5 with no unit conversion."]),
        TIP("Work through the paper once, answering everything you are sure of; then return to the marked questions. Keep 5 to 10 minutes at the end to make sure every question has an answer.", title="Exam link"),
        PQ("A rock at 0.9 GPa lies beneath crust of average density 3000 kg m⁻³ (g = 9.8 m s⁻²). Its depth is about: A 3 km, B 31 km, C 300 km, D 310 km.",
           "h = 0.9 × 10⁹ ÷ (3000 × 9.8) = 30 600 m ≈ 31 km: B. C forgets to divide by g (0.9 × 10⁹ ÷ 3000 = 300 000 m); A and D are slips of a power of ten."),
        PQ("A lava erupted at 30° latitude acquires a magnetic inclination I given by tan I = 2 tan λ. I is about: A 30°, B 49°, C 60°, D 15°.",
           "tan I = 2 × tan 30° = 2 × 0.577 = 1.155, so I = 49°: B. A copies the latitude, C doubles it, D halves it."),
        PQ("List four kinds of distractor (wrong option) common in geology multiple-choice questions, with an example of each.",
           "Mineral for rock (calcite offered for limestone); neighbouring item in a sequence (kyanite zone for staurolite zone); reversed relationship (volcanic for plutonic); unfinished calculation (intercepts instead of Miller indices); similar terms (porphyritic for porphyroblastic)."),
        SUM("Paper 1: 50 multiple-choice questions, one mark each, about 30% of the examination (Board's 2023 report); about 40% of the paper tests knowledge and the rest understanding and application.",
            "Routine: read, predict, eliminate, check. Never leave a blank.",
            "Practise the short calculations: P = ρgh, Airy roots, heat flow, tan I = 2 tan λ, Miller indices, lever rule, QAPF.",
            "Watch for mineral-for-rock, neighbouring-item, reversed and unfinished-calculation distractors.",
            "Revise all five modules; budget a little under two minutes per question in the KKEVO mock."),
    ],
))

# ------------------------------------------------------------------ Examination 2. Paper 2
LESSONS.append(lesson(
    module=M_EXAM,
    topic="Paper 2",
    title="Paper 2: choosing, planning and writing geology essays",
    slug="gyl2-paper2-essay-questions",
    minutes=25,
    summary="How to choose four questions from six, read command words, plan and write essay answers with labelled diagrams and comparison tables, and avoid the errors the Board's 2023 report describes for Geology Paper 2.",
    objectives=[
        "Describe the structure of Paper 2 and use a strategy to choose questions",
        "Interpret command words such as describe, explain, distinguish, account for and discuss",
        "Plan an essay answer with headings, paired comparisons and labelled diagrams",
        "Avoid the errors reported by the Board in 2023, such as answering a related but different question",
    ],
    key_concepts=["Command word", "Question choice", "Essay plan", "Comparison table", "Labelled diagram", "Relevance", "Technical terms"],
    blocks=[
        H("Introduction"),
        T("According to the Board's 2023 subject report, Geology Paper 2 was an essay paper of six questions, weighted 35% of the examination. Candidates answered any four, and the questions carried equal marks. "
          "The report says that performance fell compared with the year before and that many candidates scored very low marks. Its comments show the same pattern again and again: candidates wrote about a related topic instead of answering the question set. This lesson trains you to answer what is asked."),
        T("Paper 2 cannot be marked automatically, so the KKEVO 'Paper 2 practice paper A' that goes with this lesson uses multiple-choice and numeric parts that test planning, key points, diagrams and calculations. Practise full written answers on paper too, and ask your teacher to mark them."),
        H("Choosing four questions"),
        T("Read all six questions and every part of each before choosing. A question can be popular yet badly answered: in the 2023 report the most popular question had a low pass rate because its definitions were not known precisely. "
          "Choose questions where you can answer every part, not only the first. In our practice setting (150 minutes) that gives about 35 minutes per question, plus a few minutes to choose and check."),
        H("Command words"),
        KEY("What each word asks for", "Answer the word, not the topic.", cards=[
            ["State, name, list", "Short facts, no explanation."],
            ["Define", "A precise meaning in one sentence with the correct technical words (for example 'revolves', not 'rotates', for a planet's orbit)."],
            ["Describe", "What it is or what happens: composition, texture, shape, sequence."],
            ["Explain, account for", "Reasons and processes: how and why it formed. 'Account for the formation' needs the process, not a description."],
            ["Distinguish, compare", "Paired points: each difference stated for both items, best in a two-column table."],
            ["Discuss, evaluate", "Arguments for and against, evidence and limitations, and a conclusion."],
        ]),
        H("Errors from the Board's 2023 report"),
        KEY("Answering the wrong question", "Paraphrased from the report; each lost marks that were within reach.", cards=[
            ["Major structures associated with folds", "Candidates described anticlines and synclines, or minor structures, instead of major ones such as salt domes, nappes and thrust sheets, periclines (domes and basins), and valley bulges and cambering."],
            ["Processes of contact metamorphism", "Candidates described contact metamorphism in general instead of naming and describing tourmalinisation, greisening and ore mineralisation."],
            ["Formation of foliated rocks", "Candidates described minerals and textures but did not account for formation: parent rock (shale), grade (low, medium, high) and type (regional)."],
            ["Evidence for sea-floor spreading", "Candidates explained the theory instead of the evidence: topography (high, hot ridge; older, colder, deeper floor towards trenches) and symmetrical magnetic stripes."],
            ["Bowen's reaction series", "Candidates confused it with the rock cycle, mixed up the two branches and misspelled the plagioclase names."],
            ["Lava flow and sill", "Candidates could not give the differences in upper surface, grain size, vesicles, baking, chilling, xenoliths and veins."],
        ]),
        H("Planning and writing"),
        T("Spend two to three minutes on a plan for each part. Write headings in the margin, one for each point you will make. Then write one short paragraph per heading, using the technical terms of the topic. "
          "Use a labelled diagram where it saves words: Bowen's series, a cross-section of an intrusion, Barrow's zones, a P-T sketch of facies. Draw it large, in pencil, with a title and labels. Where the question says 'compare' or 'distinguish', use a table with the two items as columns."),
        EX("Worked example 1: a plan for an 'account for' question", intro="Describe the composition and texture of, and account for the formation of, slate, schist and gneiss. (Model plan.)", steps=[
            S("Slate", text="Composition: fine micas (sericite, biotite), chlorite, quartz. Texture: very fine grained, slaty cleavage. Formation: low-grade regional metamorphism (low temperature and pressure, with directed stress) of shale."),
            S("Schist", text="Composition: micas (biotite and muscovite), quartz, feldspar, often garnet or kyanite. Texture: medium to coarse grained, schistose, porphyroblastic. Formation: medium-grade regional metamorphism of shale."),
            S("Gneiss", text="Composition: quartz, feldspar, biotite, hornblende, garnet. Texture: coarse grained, gneissose banding. Formation: high-grade regional metamorphism of shale (paragneiss) or of granite (orthogneiss)."),
            S("Link", text="A sentence that grain size and foliation develop as grade increases; a simple diagram of Barrow's zones can support it."),
        ]),
        EX("Worked example 2: a plan for a 'distinguish' question", intro="Distinguish between oceanic and continental lithosphere. (Model plan as paired points.)", steps=[
            S("Thickness and density", text="Oceanic: thinner, denser (about 3.0 g cm⁻³ crust). Continental: thicker, less dense (about 2.7 g cm⁻³ crust)."),
            S("Composition", text="Oceanic: basalt and gabbro (sima), fairly uniform. Continental: granite, sedimentary and metamorphic rocks (sial over sima), varied."),
            S("Age", text="Oceanic: no older than about 200 million years. Continental: up to about 4 billion years old."),
            S("Features", text="Oceanic: magnetic stripes, ridges, transform faults; no Conrad discontinuity. Continental: no magnetic stripes of that kind; a Conrad discontinuity in places; mountain belts and cratons."),
        ]),
        MISTAKE("Writing everything you know about the topic", "Marks go only to points that answer the question. A long answer about the theory of plate tectonics earns nothing if the question asked for the evidence of sea-floor spreading. Underline the key words of the question and check each paragraph against them."),
        MISTAKE("Careless terms and spellings", "The report notes spelling errors (for example in plagioclase names), abbreviations and shorthand. Write terms in full and spell them correctly: bytownite, labradorite, andesine, oligoclase; 'dip', not 'deep'; 'coarse grained', not 'coarse grain'."),
        QUIZ("A question asks: 'Account for the formation of a migmatite.' Which answer is best?", ["Migmatite is a banded rock of light and dark layers", "Migmatite forms when high-grade regional metamorphism of shale reaches temperatures at which partial melting (anatexis) begins; the light granitic veins are melt and the dark parts are residue", "Migmatite contains quartz, feldspar and biotite", "Migmatite is found in the Pan-African belt"], 1,
             "'Account for the formation' asks for the process and conditions, not a description.", hint="Which answer explains how it formed?",
             feedback=["That is a description, not an account of formation.", "", "That lists the minerals only.", "That gives a location, not a process."]),
        QUIZ("Which is the best way to answer 'Distinguish between a lava flow and a sill'?", ["Write a paragraph about lava flows and then a paragraph about sills", "Use a table of paired differences, each point stated for both", "Draw a cross-section of a volcano", "Define the word sill"], 1,
             "Paired points make each difference clear and easy to mark.", hint="Each difference needs both sides.",
             feedback=["Separate paragraphs often fail to compare the same feature.", "", "A volcano diagram does not show the differences asked for.", "A definition alone does not distinguish them."]),
        TIP("Paper 2 questions can come from any part of the syllabus, and a single question often combines topics (for example rock description with plate tectonics). Revise by linking topics, and practise at least one timed essay a week.", title="Exam link"),
        PQ("Plan an answer to: 'Explain how sea-floor topography and palaeomagnetic stripes support the theory of sea-floor spreading.'",
           "Topography: the ridge crest stands high because new, hot rock is less dense; the sea floor deepens towards the trenches as the lithosphere cools, becomes denser and subsides; seamounts and guyots are lower and older away from the ridge. Stripes: new basalt at the ridge records the field polarity as it cools; reversals produce bands of normal and reversed magnetism; the pattern is parallel and symmetrical about the ridge, with the youngest at the crest and older stripes towards the flanks, showing that crust forms at the ridge and moves away."),
        PQ("Name and briefly describe four major structures associated with folds.",
           "Nappes and thrust sheets: large recumbent folds whose limbs are thrust far over younger rocks. Periclines: domes and basins with dips outwards or inwards in all directions. Salt domes: upward movement of salt that folds the overlying beds. Valley bulges and cambering: beds bulge up in valley floors and sag towards valleys on the sides, where soft clays are squeezed out beneath hard caprocks. Gravity collapse structures may also be given."),
        PQ("Explain why the command word matters by rewriting this answer to 'State three causes of earthquakes': 'Earthquakes are vibrations of the ground that cause damage.'",
           "The answer gives a definition and an effect, not causes. Better: sudden slip along faults (elastic rebound); volcanic activity; human activities such as filling reservoirs, mining or fluid injection. Other acceptable causes include undersea landslides and explosions."),
        SUM("Paper 2: six essay questions, answer any four, equal marks, about 35% of the examination (Board's 2023 report).",
            "Read every part before choosing; choose questions you can finish.",
            "Answer the command word: describe, explain or account for, distinguish, discuss.",
            "Plan with headings; use tables for comparisons and large labelled diagrams.",
            "Avoid the report's errors: answering a related topic, missing the formation part, careless terms and spellings."),
    ],
))

# ------------------------------------------------------------------ Examination 3. Paper 3
LESSONS.append(lesson(
    module=M_EXAM,
    topic="Paper 3",
    title="Paper 3: practical skills with specimens, thin sections, crystal models and maps",
    slug="gyl2-paper3-practical-skills",
    minutes=25,
    summary="The practical skills for Paper 3: describing and identifying hand specimens of minerals and rocks, using thin sections, crystal models, photographs and geological maps, and getting practical experience even in a school with little equipment.",
    objectives=[
        "Describe and identify mineral and rock specimens with a systematic routine, and give their mode of formation",
        "Use simple tests (streak, hardness, acid, specific gravity) and calculate specific gravity",
        "Describe a thin section and a crystal model correctly, including axes and symmetry",
        "Give six-figure grid references, describe folds, faults and outliers, and plan a cross-section",
    ],
    key_concepts=["Hand specimen", "Streak", "Hardness", "Specific gravity", "Thin section", "Crystal model", "Grid reference", "Outlier", "Cross-section", "School-based assessment"],
    blocks=[
        H("Introduction"),
        T("According to the Board's 2023 report, Geology Paper 3 was a practical paper of five compulsory questions, weighted 25%, and candidates were also assessed on school-based assessment over the two years and on fieldwork (5% each). "
          "The report describes questions on a geological map, a crystal model, fossils, a photograph of a structure and a set of hand specimens. It also says that the specimen section was answered best and the map and crystal sections worst. "
          "Practical skill comes from practice, so use this lesson with real specimens whenever you can."),
        H("Hand specimens: a routine"),
        KEY("Describe, then identify, then explain", "Use the same order every time.", cards=[
            ["Minerals", "Colour, streak (on an unglazed tile), lustre (metallic, vitreous, pearly, earthy), hardness (Mohs), cleavage or fracture, crystal form, specific gravity, reaction with dilute acid, magnetism."],
            ["Igneous rocks", "Grain size ('coarse grained'), colour (leucocratic or melanocratic), minerals, texture (equigranular, porphyritic, vesicular, flow banded). Then name, silica class and mode of formation."],
            ["Sedimentary rocks", "Composition (grains, matrix, cement), grain size, shape, sorting, maturity, structures, fossils, reaction with acid."],
            ["Metamorphic rocks", "Minerals, grain size, foliation or granoblastic texture, porphyroblasts. Then name, protolith, type and grade of metamorphism."],
        ]),
        CODE("Specimen          Key observations                                 Identification\n"
             "coarse, pink      quartz, pink feldspar, mica; equigranular       granite\n"
             "fine, light       phenocrysts of quartz, flow banding             rhyolite\n"
             "red-brown, heavy  cherry-red streak, metallic or earthy lustre    haematite\n"
             "pink, H = 6       two cleavages at about 90 degrees, vitreous     orthoclase\n"
             "sugary, white     fizzes with dilute HCl, interlocking calcite    marble\n"
             "banded, coarse    quartz-feldspar and biotite-hornblende bands,   gneiss\n"
             "                  porphyroblasts of garnet\n"
             "red, well sorted  rounded quartz grains, haematite cement         red (ferruginous)\n"
             "                                                                   sandstone", "text", title="Table 1. Examples of descriptions and identifications"),
        T("Questions also ask how specimens are **related**. Granite and rhyolite are both acid igneous rocks with the same minerals: granite is the plutonic equivalent of rhyolite. Limestone and marble both contain calcite and react with acid: limestone is the protolith of marble. "
          "And they ask for **modes of formation**: granite, by slow cooling of acid magma at depth; marble, by contact (or regional) metamorphism of a pure limestone; red sandstone, typically in an arid, desert or piedmont environment."),
        EX("Worked example 1: specific gravity", intro="A mineral weighs 52 g in air and 32 g when suspended in water. A second mineral weighs 50 g in air and 40 g in water. Find the specific gravity of each and suggest what they might be.", steps=[
            S("Formula", math=r"SG = \frac{W_{air}}{W_{air} - W_{water}}"),
            S("First mineral", math=r"SG = \frac{52}{52 - 32} = \frac{52}{20} = 2.6", text="Light: quartz or feldspar (about 2.6 to 2.65)."),
            S("Second mineral", math=r"SG = \frac{50}{50 - 40} = 5.0", text="Heavy: haematite (about 5) would fit if it has a red streak."),
        ], check=r"20 \times 2.6 = 52"),
        H("Simple tests in a school laboratory"),
        T("Many schools have few specimens and no microscope. You can still practise. Make a hardness kit: fingernail (about 2.5), copper coin (about 3.5), steel knife or glass (about 5.5), and a piece of quartz (7). Use the back of an unglazed tile as a streak plate. "
          "Dilute hydrochloric acid tests for calcite; where the laboratory has none, strong vinegar reacts slowly with powdered calcite (a teacher should supervise any acid). A small magnet identifies magnetite. A kitchen balance and a cup of water give specific gravity. "
          "Build a class collection from road cuttings, quarries and riverbeds near your school, label each specimen with where it was found, and describe it in a notebook. The Board's report advises fieldwork within the school's own region and keeping its cost low."),
        H("Thin sections and crystal models"),
        T("For a thin section, describe in plane-polarised light (colour, pleochroism, relief, shape, cleavage) and then in crossed polars (interference colours, extinction, twinning). For example: lamellar (polysynthetic) twinning shows plagioclase; simple Carlsbad twinning suggests orthoclase; high relief and bright second-order colours with irregular cracks suggest olivine. Where no microscope is available, practise from good photographs of thin sections."),
        KEY("Crystal models: what the report says", "Small details lose marks.", cards=[
            ["Axes", "Insert the axes in the model and label them in lower case with the sign first: +a, +b, +c (not a+ or capitals). In monoclinic and triclinic models the a axis is inclined, not horizontal."],
            ["Symmetry", "List the elements present: planes, axes (ii, iii, iv, vi) and centre. For a triclinic pinacoidal model the answer is no plane, no axis, but a centre of symmetry, never 'none'."],
            ["System and reason", "Name the system and give the diagnostic symmetry as the reason: for example triclinic because there is only a centre of symmetry."],
            ["Example mineral", "Give a mineral that crystallises in that system and habit; albite (triclinic) is a standard example."],
        ]),
        H("Geological maps"),
        KEY("Map skills", "From the report's comments on candidates' answers.", cards=[
            ["Six-figure grid references", "Eastings first, then northings: for example 432176 means 43.2 east, 17.6 north. Four figures are not precise enough."],
            ["Folds", "Use dip arrows: beds dipping away from the core make an anticline (older rocks in the core); dipping towards it, a syncline. Use anticline and syncline when the order of beds is known. State the core bed. Spell 'dip' correctly."],
            ["Faults", "Locate with grid references or cardinal points and give the trend in full, for example north-south (N-S)."],
            ["Outliers and inliers", "An outlier is an area of younger rock completely surrounded by older rock, isolated by erosion; an inlier is older rock surrounded by younger."],
            ["Cross-sections", "Draw the topographic profile along the line, mark where each boundary crosses it, use the dips, insert the fold axes and label the beds, faults and core beds."],
        ]),
        EX("Worked example 2: vertical exaggeration", intro="A map has a scale of 1 : 25 000. You draw a cross-section with a vertical scale of 1 cm to 100 m. What is the vertical exaggeration, and what effect does it have on dips?", steps=[
            S("Vertical scale as a ratio", math=r"1 \text{ cm} : 100 \text{ m} = 1 : 10\,000"),
            S("Exaggeration", math=r"VE = \frac{25\,000}{10\,000} = 2.5"),
            S("Effect", text="Slopes and dips appear steeper than they really are. State the vertical exaggeration on the section; use VE = 1 (equal scales) when true dips must be drawn."),
        ], check=r"2.5 \times 10\,000 = 25\,000"),
        MISTAKE("Calling a structure in a photograph by the wrong name", "The report says many candidates did not recognise columnar joints in a photograph, naming them pillow lavas, tors or mud cracks. Practise naming structures from photographs: columnar joints, pillow lavas, folds, faults, unconformities, cross-bedding."),
        QUIZ("Which six-figure grid reference is written correctly for a point 41.7 km east and 26.3 km north on the grid?", ["263417", "417263", "4126", "26.3 41.7"], 1,
             "Eastings first (417), then northings (263).", hint="Along the corridor, then up the stairs.",
             feedback=["That gives northings first.", "", "Four figures are not precise enough when six are asked for.", "Grid references are written as one number without decimal points, eastings first."]),
        QUIZ("A crystal model has no plane of symmetry and no axis of symmetry but has a centre of symmetry. Which system is it, and which mineral is a good example?", ["Monoclinic; orthoclase", "Triclinic; albite", "Orthorhombic; olivine", "Cubic; halite"], 1,
             "A centre of symmetry only is diagnostic of the triclinic system; albite is triclinic.", hint="Which system has the least symmetry?",
             feedback=["Monoclinic has one diad axis and one plane.", "", "Orthorhombic has three diad axes and three planes.", "Cubic has four triad axes."]),
        TIP("Paper 3 rewards precise description: the right term, the right unit, the right spelling. Practise each skill with a timer, and keep a practical notebook through Lower and Upper Sixth, which also helps your school-based assessment and fieldwork marks.", title="Exam link"),
        PQ("Describe and identify a specimen that is pink, has a hardness of 6, vitreous lustre and two cleavages at about 90°. State one rock in which it is common.",
           "Description: pink colour, vitreous lustre, hardness 6 (scratches glass with difficulty, scratched by quartz), two good cleavages at about 90° (prismatic). Identification: orthoclase (potassium feldspar). Common in granite."),
        PQ("Give two relationships between granite and rhyolite, and two between limestone and marble.",
           "Granite and rhyolite: both acid igneous rocks; same mineralogy (quartz, feldspars, micas); granite is the plutonic (coarse-grained) equivalent of rhyolite, which is volcanic. Limestone and marble: both made of calcite and react with dilute hydrochloric acid; limestone is the parent rock (protolith) of marble, formed by metamorphism of limestone."),
        PQ("A mineral weighs 36 g in air and 27 g in water. Calculate its specific gravity and comment.",
           "SG = 36 ÷ (36 − 27) = 36 ÷ 9 = 4.0. A fairly heavy mineral, heavier than quartz and feldspar (about 2.6); other tests (streak, hardness, lustre) are needed to identify it."),
        SUM("Paper 3: five compulsory practical questions (25%), plus school-based assessment and fieldwork (5% each), per the Board's 2023 report.",
            "Specimens: describe, identify, then give mode of formation and relationships (plutonic and volcanic equivalents; protolith and metamorphic product).",
            "Tests: streak, hardness kit, acid, magnet, SG = W_air ÷ (W_air − W_water).",
            "Crystal models: label +a, +b, +c; triclinic = centre of symmetry only (albite).",
            "Maps: six-figure grid references eastings first; dip arrows for folds; fault trends in full; outliers are younger rock surrounded by older; state vertical exaggeration."),
    ],
))

# ==== END LESSONS ====
