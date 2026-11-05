"""GCE subjects and syllabus outlines, taken from docs/curriculum/GCE_CURRICULUM_GUIDE.md.

This is KKEVO's own summary of the curriculum, not the official GCE Board text, so the
syllabi it creates are stored with `is_official=False` and status "draft". Check each one
against the official GCE Board syllabus before publishing.

Loaded by `python manage.py load_gce_curriculum`.
"""

SOURCE = "docs/curriculum/GCE_CURRICULUM_GUIDE.md"
VERSION = "KKEVO guide 2026"  # Syllabus.version for every syllabus this file creates

O, A = ["form-5"], ["lower-sixth", "upper-sixth"]
SCI, ARTS = "science", "arts"
# The guide has a Commerce & Business stream, but the platform (and the onboarding
# "Arts or Science?" step) only has two pathways, so commerce subjects go under Arts.
COM = ARTS

# slug, name, icon_text, icon, accent, category, summary, levels, pathways
SUBJECTS = [
    # Science & Mathematics
    ("mathematics", "General Mathematics", "x²", "", "blue", "sciences",
     "Sets, commercial maths, quadratics, matrices, trigonometry and statistics.", O, [SCI, ARTS, COM]),
    ("additional-mathematics", "Additional Mathematics", "Σ", "", "blue", "sciences",
     "Pure maths, introductory calculus, and mechanics or statistics.", O, [SCI]),
    ("pure-mathematics-with-mechanics", "Pure Mathematics with Mechanics", "∫", "", "blue", "sciences",
     "Rigorous algebra, calculus, 3D vectors and classical mechanics.", A, [SCI]),
    ("pure-mathematics-with-statistics", "Pure Mathematics with Statistics", "σ", "", "blue", "sciences",
     "Calculus, proof, probability and statistical inference.", A, [SCI, COM]),
    ("further-mathematics", "Further Mathematics", "∞", "", "blue", "sciences",
     "Advanced pure maths, advanced mechanics and numerical methods.", A, [SCI]),
    ("physics", "Physics", "F", "", "blue", "sciences",
     "Motion, forces, energy, waves, electricity and modern physics.", O + A, [SCI]),
    ("chemistry", "Chemistry", "H₂O", "", "blue", "sciences",
     "Atomic structure, bonding, the mole, acids and organic chemistry.", O + A, [SCI]),
    ("biology", "Biology", "", "dna", "emerald", "sciences",
     "Cells, nutrition, genetics, ecology and human health.", O + A, [SCI]),
    ("human-biology", "Human Biology", "", "dna", "emerald", "sciences",
     "The human body, health and disease.", O, [SCI]),
    ("computer-science", "Computer Science", "</>", "", "blue", "sciences",
     "Architecture, logic, algorithms, programming, databases and software engineering.", O + A, [SCI]),
    ("ict", "Information and Communication Technology", "ICT", "", "blue", "sciences",
     "Office tools, web design, networks, cybersecurity and IT projects.", O + A, [SCI, ARTS, COM]),
    ("geology", "Geology", "⛰", "", "amber", "sciences",
     "Rocks, minerals, earth structure and geological processes.", O + A, [SCI]),
    ("food-and-nutrition", "Food and Nutrition", "Nu", "", "emerald", "sciences",
     "Nutrients, diet, food preparation and food science.", O + A, [SCI]),
    # Arts, Languages & Humanities
    ("english-language", "English Language", "Aa", "", "slate", "languages",
     "Comprehension, summary, grammar and composition writing.", O + A, [SCI, ARTS, COM]),
    ("literature-in-english", "Literature in English", "¶", "", "slate", "languages",
     "Prose, poetry and drama: themes, character and style.", O + A, [ARTS]),
    ("french", "French", "Fr", "", "slate", "languages",
     "Grammar, vocabulary, reading and writing in French.", O + A, [SCI, ARTS, COM]),
    ("history", "History", "1884", "", "amber", "humanities",
     "Cameroon, African and world history, from 1848 to today.", O + A, [ARTS]),
    ("geography", "Geography", "", "map", "amber", "humanities",
     "Physical and human geography, map reading and fieldwork.", O + A, [SCI, ARTS]),
    ("religious-studies", "Religious Studies", "✦", "", "amber", "humanities",
     "Religious texts, beliefs and their place in society.", O + A, [ARTS]),
    ("logic", "Logic", "∴", "", "slate", "humanities",
     "Reasoning, arguments and fallacies.", O, [ARTS]),
    ("philosophy", "Philosophy", "φ", "", "slate", "humanities",
     "Major thinkers and questions of knowledge, ethics and politics.", A, [ARTS]),
    ("citizenship-education", "Citizenship Education", "⚖", "", "amber", "humanities",
     "Rights, duties, institutions and civic life in Cameroon.", O, [SCI, ARTS, COM]),
    ("economics", "Economics", "", "chart", "amber", "business",
     "Demand and supply, money, markets and national income.", O + A, [ARTS, COM]),
    # Commerce & Business
    ("commerce", "Commerce", "₣", "", "emerald", "business",
     "Trade, banking, insurance, transport and communication.", O, [COM]),
    ("principles-of-accounts", "Principles of Accounts", "Dr", "", "emerald", "business",
     "Double entry, books of original entry and final accounts.", O, [COM]),
    ("office-practice", "Office Practice", "✉", "", "emerald", "business",
     "Office organisation, records, mail and communication.", O, [COM]),
    ("accounting", "Accounting", "Cr", "", "emerald", "business",
     "Financial and cost accounting, analysis and interpretation.", A, [COM]),
    ("business-studies", "Business Studies", "B", "", "emerald", "business",
     "Business organisation, management, marketing and finance.", A, [COM]),
]

# Syllabus outlines. Key: (subject slug, level slug).
# Value: title, notes, sections = [(section title, [(item title, description), ...]), ...]
SYLLABI = {
    ("computer-science", "form-5"): ("Computer Science (O Level, 0595)", "", [
        ("Web Design & Publishing", [
            ("HTML5 structure", "<!DOCTYPE html>, tag hierarchy, text formatting, hyperlinks, images, tables and forms."),
            ("CSS styling", "Inline, internal and external CSS; selectors, typography and the box model."),
        ]),
        ("Legal, Ethical & Social Aspects", [
            ("Intellectual property", "Copyright, software piracy and open-source licences (GPL, MIT, Creative Commons)."),
            ("Cameroon legal framework", "Cybersecurity, cybercrime and data privacy rules (ANTIC, MINPOSTEL)."),
            ("Social and economic impact", "Digital divide, automation and job displacement, e-waste, remote collaboration."),
        ]),
        ("Examination", [
            ("Paper 1", "1.5-hour multiple choice covering the whole syllabus."),
            ("Paper 2", "Structured theory: logic circuits, pseudo-code, database design and trace tables."),
            ("Paper 3 (practical)", "Timed lab: word processing, spreadsheets, databases and basic web design."),
        ]),
    ]),
    ("ict", "form-5"): ("ICT (O Level, 0596)", "The guide gives ICT and Computer Science one shared O Level outline.", [
        ("Web Design & Publishing", [
            ("HTML5 structure", "Tag hierarchy, text formatting, hyperlinks, images, tables and forms."),
            ("CSS styling", "Inline, internal and external CSS; selectors, typography and the box model."),
        ]),
        ("Legal, Ethical & Social Aspects", [
            ("Intellectual property", "Copyright, software piracy and open-source licences."),
            ("Cameroon legal framework", "Cybersecurity, cybercrime and data privacy rules (ANTIC, MINPOSTEL)."),
            ("Social and economic impact", "Digital divide, automation, e-waste, remote collaboration."),
        ]),
        ("Practical skills", [
            ("Office productivity", "Word processing and spreadsheet modelling."),
            ("Databases", "Creating and querying a relational database."),
        ]),
        ("Examination", [
            ("Paper 1", "Multiple choice."),
            ("Paper 2", "Structured theory."),
            ("Paper 3 (practical)", "Practical lab: word processing, spreadsheets, databases and basic web design."),
        ]),
    ]),
    ("mathematics", "form-5"): ("General Mathematics (O Level, 570)", "", [
        ("Set Theory & Logic", [
            ("Venn diagrams", "Two- and three-set Venn diagrams and set algebra laws."),
            ("Logic", "Logical deductions and truth values."),
        ]),
        ("Commercial Mathematics & Variation", [
            ("Commercial arithmetic", "Compound interest, depreciation, hire purchase and taxes."),
            ("Variation", "Direct, inverse, joint and partial variation."),
        ]),
        ("Quadratic Functions & Equations", [
            ("Solving quadratics", "Factorization, completing the square and the quadratic formula."),
            ("Quadratic graphs", "Turning points and roots from graphs."),
        ]),
        ("Sequences & Series", [
            ("Arithmetic progressions", "nth term and sum of an AP."),
            ("Geometric progressions", "nth term and sum of a GP."),
        ]),
        ("Matrices & Vectors", [
            ("2×2 matrices", "Operations, determinant, inverse, solving linear systems."),
            ("2D vectors", "Column vectors: magnitude, direction and collinearity."),
        ]),
        ("Trigonometry & Bearings", [
            ("Sine and cosine rules", "Sine rule, cosine rule and the area ½ab sin C."),
            ("Bearings", "Three-figure bearings and navigation problems."),
        ]),
        ("Circle Theorems", [
            ("Circle theorems", "Cyclic quadrilaterals and the alternate segment theorem."),
        ]),
        ("Statistics & Probability", [
            ("Grouped data", "Grouped frequency, histograms, cumulative frequency ogives, median and quartiles."),
            ("Probability", "Theoretical probability and tree diagrams."),
        ]),
        ("Examination", [
            ("Paper 1", "30%: 50 multiple choice questions, 1.5 hours."),
            ("Paper 2", "70%: structured core and optional multi-part problems, 2.5 hours."),
        ]),
    ]),
    ("additional-mathematics", "form-5"): ("Additional Mathematics (O Level, 575)", "", [
        ("Pure Mathematics", [
            ("Polynomials", "Remainder and factor theorems; partial fractions."),
            ("Trigonometry", "Radian measure and trigonometric identities."),
            ("Binomial expansion", "Binomial expansions."),
            ("Coordinate geometry", "Straight lines and circles."),
        ]),
        ("Calculus", [
            ("Differentiation", "First principles, derivative of xⁿ, tangents, normals and stationary points."),
            ("Integration", "Definite integrals and area under a curve."),
        ]),
        ("Applied option", [
            ("Mechanics", "Rectilinear kinematics and resolving forces."),
            ("Statistics", "Probability distributions."),
        ]),
        ("Examination", [
            ("Paper 1", "33.3%: multiple choice."),
            ("Paper 2", "66.7%: extended response."),
        ]),
    ]),
    ("history", "form-5"): ("History (O Level, 0560)", "", [
        ("Trusteeship & Nationalism in Cameroon (1945–1961)", [
            ("French Cameroun", "Trade unions, UPC, BDC, ESOCAM; Um Nyobè, Moumié, Ouandié; the 1955 UPC ban and the maquis; "
             "Loi-Cadre (1956); independence on 1 January 1960 under Ahidjo."),
            ("British Southern Cameroons", "1953 Eastern House of Assembly crisis; KNC, KNDP, OK (Endeley, Foncha, Muna, Jua); "
             "UN plebiscite of 11 February 1961; Foumban Conference; reunification on 1 October 1961."),
        ]),
        ("Post-Independence Cameroon", [
            ("Federal to unitary state", "Federal Republic (1961–1972), CNU single party (1966), 20 May 1972 referendum."),
            ("Modern transitions", "1982 Ahidjo–Biya transition, 1984 name change, 1990 liberty laws, ghost towns, "
             "Tripartite Conference and the 1996 constitution."),
        ]),
        ("World History since 1870", [
            ("African decolonization", "Peaceful transfers vs armed struggles; OAU (1963) and AU (2002)."),
            ("Cold War", "Containment, Cuban Missile Crisis, proxy wars, collapse of the USSR."),
            ("Post-Cold War world", "Arab–Israeli conflict and the post-Cold War order."),
        ]),
        ("Examination", [
            ("Paper 1", "Multiple choice."),
            ("Paper 2", "Structured essays."),
        ]),
    ]),
    ("geography", "form-5"): ("Geography (O Level, 0550)",
                              "Outline summarised from the GCE Board's revised 0550 Geography syllabus (first examined "
                              "June 2025), published at camgceb.org. Paper 1 is 50 multiple-choice questions in 1 hour "
                              "30 minutes; Paper 2 has seven questions, four to be answered, in 2 hours 30 minutes, and "
                              "the map reading question is compulsory.", [
        ("Map Reading and Interpretation", [
            ("Map reading", "Definition and importance of maps; marginal information; conventional signs and colours; grid references; directions and bearings; scales; measuring distance and area; copying, reducing and enlarging."),
            ("Map interpretation", "Relief and contours, drainage, vegetation, settlement, communication, location of economic activity and land use; sketch maps; links between the physical environment and human activities."),
        ]),
        ("The Earth as a Planet", [
            ("The earth in the solar system", "The solar system and the planets; the shape of the earth and the evidence for it."),
            ("Location and time", "Latitude, longitude, great circles and the International Date Line; distances; local time, standard time and time zones."),
            ("Rotation and revolution", "The difference between rotation and revolution, and the effects of each."),
        ]),
        ("Hydrology, Meteorology and Climatology", [
            ("The hydrological cycle", "Global water resources; the water cycle as a system at global and drainage-basin scale; inputs, outputs, flows and stores."),
            ("The earth's atmosphere", "Definition and structure of the atmosphere; the main characteristics of the troposphere and stratosphere."),
            ("Weather and climate", "Weather versus climate; weather elements and instruments; observing, recording and presenting weather data; simple weather maps."),
            ("Forms of condensation", "Precipitation and its forms (rain, hail, snow, fog, mist, dew, sleet); the three main types of rainfall."),
            ("Pressure and winds", "Atmospheric pressure and the planetary pressure belts and winds; local winds (land and sea breezes, mountain and valley winds, monsoons)."),
            ("Basic concepts of climate", "Tropical humid, tropical wet and dry and tropical dry climates; the factors that influence weather and climate."),
            ("Environmental hazards", "Global warming; floods, droughts and desertification; water scarcity; waste management: causes, effects, adaptation and mitigation."),
        ]),
        ("Biogeography", [
            ("Soil", "Meaning and components of soil; main soil types and climatic zones; the soil profile; soil erosion and conservation."),
            ("Vegetation", "Classification of world vegetation; tropical rainforest, tropical grassland and tropical desert; factors, problems and solutions."),
            ("Ecosystems", "Meaning, structure (biotic and abiotic parts) and functioning of ecosystems; food chains and food webs."),
        ]),
        ("Geomorphology", [
            ("The structure of the Earth", "Structure of the earth; rocks by origin; volcanic eruptions, earthquakes and geo-hazards; landscape formation at plate margins."),
            ("Denudational processes and landforms", "Weathering; erosion, transport and deposition by running water, wind and waves; dendritic, trellised and radial drainage; denudational hazards."),
        ]),
        ("Development", [
            ("Concept of development and economic growth", "Development, economic growth, underdevelopment and poverty; indicators of development; LICs, AICs, NICs and oil-rich countries; sustainable development."),
            ("The process of development", "Causes of and solutions to underdevelopment and poverty (MDGs and SDGs); the economic miracle of NICs (one case study); Rostow's model of economic growth."),
        ]),
        ("Economic Activities", [
            ("Agriculture", "Classifying agriculture; intensive and extensive farming systems and their forms; agriculture as a system; changes over time (green revolution, climate-smart agriculture); the Von Thunen model."),
            ("Management of primary resources", "Meaning, classification and conservation of resources; forest, fish and mineral resources: distribution, importance, problems and solutions."),
            ("Major sources of power", "Traditional and modern sources of power; renewable and non-renewable energy; global distribution; energy sources of the future."),
            ("Secondary industries", "Classifying manufacturing; global distribution of industry; industrialisation in LICs, NICs and AICs; Weber's model of industrial location."),
            ("Tertiary industries", "Globalisation; trade; transport and telecommunication; the internet; tourism."),
        ]),
        ("Population Geography", [
            ("Population distribution", "Population data and sources; population density and distribution; the global pattern."),
            ("Population composition and structure", "Age groups and their characteristics; the basic age-sex pyramids."),
            ("Population change", "World population growth; fertility and mortality; the demographic transition model; migration."),
            ("Population and resources", "Optimum, over- and under-population; Malthus's model of population and resources."),
        ]),
        ("Settlement Geography", [
            ("General concepts of settlement", "Settlement and its types; site and situation; factors in siting; rural and urban settlement."),
            ("Settlement types and their morphology", "Types and patterns of rural settlement; urbanisation; types of urban settlement; urban problems and solutions; urban fields."),
        ]),
        ("Human Activities and the Environment", [
            ("Development and environmental management", "Land reclamation; multi-purpose river development projects; pollution: types, causes and solutions."),
        ]),
        ("The Geography of Cameroon", [
            ("Background of Cameroon", "Location of Cameroon in Africa; the administrative map and regional headquarters."),
            ("Physical characteristics", "Relief units, drainage systems and watersheds, climatic types, vegetation and soils of Cameroon."),
            ("Human characteristics", "Population growth, structure, distribution and migration; settlement and urbanisation; town and countryside relationships."),
            ("Economic development potentials", "Agriculture; forest, fish, mineral and energy resources; multi-purpose river development; manufacturing; the informal sector; transport; tourism; economic growth and constraints."),
        ]),
        ("Examination", [
            ("Paper 1", "50 multiple-choice questions, all to be answered, in 1 hour 30 minutes (35% of the marks)."),
            ("Paper 2", "Seven essay and problem-solving questions, four to be answered, in 2 hours 30 minutes (65%); the map reading question is compulsory."),
        ]),
    ]),
    ("computer-science", "lower-sixth"): ("Computer Science (A Level, 795) — Year 1", "", [
        ("Computer Organization & Architecture", [
            ("Machine models", "Von Neumann vs Harvard; data, address and control buses."),
            ("The CPU", "Fetch–decode–execute cycle; PC, MAR, MDR, CIR, ACC; pipelining."),
        ]),
        ("Digital Logic", [
            ("Combinational circuits", "Half and full adders, multiplexers, decoders."),
            ("Sequential circuits", "SR, D, JK and T flip-flops."),
            ("Simplification", "Boolean algebra, De Morgan's laws, Karnaugh maps up to 4 variables."),
        ]),
        ("Operating Systems & Translators", [
            ("Process management", "FCFS, SJF, Round Robin; semaphores and deadlock."),
            ("Memory management", "Paging, segmentation, virtual memory and page faults."),
            ("Translators", "Compiler stages (lexical, syntax, semantic), interpreters, assemblers."),
        ]),
        ("Networks & Software Engineering", [
            ("Network models", "OSI 7-layer and TCP/IP models."),
            ("Addressing and errors", "IPv4/IPv6, CIDR subnetting, CRC error detection."),
            ("Software development", "Waterfall, Agile/Scrum, Spiral; DFDs, ERDs and UML."),
        ]),
        ("Procedural Programming", [
            ("Structured programming", "C or Python: subroutines, scope, recursion and stack frames."),
            ("Files and pointers", "File handling and pointer management."),
        ]),
    ]),
    ("computer-science", "upper-sixth"): ("Computer Science (A Level, 795) — Year 2", "", [
        ("Data Structures & Algorithms", [
            ("Abstract data types", "Stacks, queues, singly/doubly linked lists, binary search trees."),
            ("Searching and sorting", "Linear and binary search; bubble, insertion, selection, merge and quick sort."),
            ("Complexity", "Time and space complexity with Big-O, O(1) to O(n²)."),
        ]),
        ("Relational Databases", [
            ("Relational algebra", "Select, project, product, join, union, intersection, difference."),
            ("Normalization", "Functional dependencies; 1NF, 2NF, 3NF, BCNF."),
            ("SQL", "DDL, DML, joins and nested subqueries."),
        ]),
        ("Object-Oriented Programming", [
            ("OOP principles", "Abstraction, encapsulation, inheritance, polymorphism."),
            ("Classes in practice", "UML class diagrams, access modifiers, constructors/destructors, exceptions."),
        ]),
        ("Software Project", [
            ("Individual project", "Design, coding, unit and integration testing, and a technical report."),
        ]),
    ]),
    ("ict", "lower-sixth"): ("ICT (A Level, 796) — Year 1", "", [
        ("Hardware Maintenance & Deployment", [
            ("PC hardware", "Socket types, dual-channel RAM, BIOS/UEFI setup, POST diagnostics."),
            ("OS deployment", "Installing Windows/Linux by USB or network; MBR vs GPT; NTFS, ext4; virtual machines."),
        ]),
        ("Enterprise Infrastructure", [
            ("Business technologies", "E-commerce (B2B, B2C), VPNs, VoIP, learning platforms."),
            ("Green computing", "Energy use and e-waste management."),
            ("Database automation", "Automating relational databases."),
        ]),
        ("Web Development", [
            ("Layout", "Semantic HTML5, CSS3 Flexbox and Grid."),
            ("JavaScript", "Client-side JavaScript and DOM manipulation."),
        ]),
    ]),
    ("ict", "upper-sixth"): ("ICT (A Level, 796) — Year 2", "", [
        ("Network Engineering", [
            ("Cabling and switching", "RJ-45 termination (T568A/B), VLANs, DHCP scopes."),
        ]),
        ("Cybersecurity", [
            ("Security principles", "The CIA triad."),
            ("Cryptography", "AES vs RSA, PKI, digital signatures, SHA-256 hashing."),
            ("Defence and recovery", "Firewalls, IDS/IPS and disaster recovery planning."),
        ]),
        ("Productivity & Project Management", [
            ("Advanced Excel", "XLOOKUP, INDEX/MATCH, pivot tables, Solver, VBA macros."),
            ("IT project management", "Work breakdown structures, critical path method, Gantt charts."),
        ]),
    ]),
    ("history", "lower-sixth"): ("History (A Level, 0760) — Year 1", "", [
        ("Cameroon 1884–1945", [
            ("Treaties and borders", "Germano-Douala Treaty (12 July 1884), the Kings' Memorandum; Franco-German and Anglo-German conventions."),
            ("Comparative colonial rule", "British indirect rule, French assimilation and association, German imperial policy."),
            ("Social and economic change", "Urbanization, forced labour, mission education, the early press, Jeucafra, Unikamerun."),
        ]),
        ("European Revolutions & Unifications", [
            ("1848 revolutions", "Causes, liberalism, socialism and nationalism; France, Germany, Austria; why they failed."),
            ("Italian and German unification", "Cavour, Bismarck and Realpolitik; effects on the balance of power."),
        ]),
        ("Imperialism & the First World War", [
            ("The Scramble for Africa", "Eurocentric, Afrocentric, peripheral and Marxist interpretations."),
            ("The First World War", "Causes, diplomacy, the Paris peace settlement and the mandate system."),
        ]),
        ("The Interwar Crises", [
            ("Fascism and Nazism", "Rise of Italian Fascism, fall of the Weimar Republic, rise of Nazism."),
            ("Appeasement", "Anglo-French appeasement."),
        ]),
    ]),
    ("history", "upper-sixth"): ("History (A Level, 0760) — Year 2", "", [
        ("Cameroon 1945 to Today", [
            ("Trusteeship and decolonization", "UN visiting missions and petitions; UPC insurrection and pacification; Ahidjo's rise."),
            ("Southern Cameroons politics", "KNC, KNDP, OK; Mamfe, Lancaster House and London conferences; the plebiscite; Foumban."),
            ("The post-colonial state", "Federalism vs unitarism; CNU/CPDM; 1982 transition; 1990s liberalization; 1996 constitution."),
        ]),
        ("Decolonization in Africa", [
            ("Constitutional transfers", "British transfers in Ghana and Nigeria; French Loi-Cadre and the 1958 referendum (Guinea)."),
            ("Armed liberation", "Algeria, Kenya (Mau Mau), Portuguese colonies, Zimbabwe (Chimurenga)."),
            ("South Africa", "The anti-apartheid struggle, 1948–1994."),
        ]),
        ("Cold War & International Governance", [
            ("Cold War geopolitics", "Truman Doctrine, Marshall Plan, containment, nuclear deterrence, rivalry in the Global South."),
            ("The United Nations", "UN Charter, Security Council, peacekeeping (Congo, Balkans, Rwanda)."),
            ("Regional integration", "OAU to AU, CEMAC, ECOWAS, SADC; the post-1991 world."),
        ]),
    ]),
}

_PURE_CORE = [
    ("Algebra & Functions", [
        ("Proof", "Mathematical induction and proof by contradiction."),
        ("Algebra", "Partial fractions; binomial theorem for rational indices; symmetric functions of roots."),
        ("Functions and graphs", "Composite and inverse functions; curve sketching with oblique asymptotes."),
    ]),
    ("Trigonometry & Coordinate Geometry", [
        ("Identities", "Compound, double and half-angle identities; R cos(θ ± α)."),
        ("Conic sections", "Circles, parabolas, ellipses and hyperbolas in cartesian and parametric form."),
    ]),
    ("Calculus", [
        ("Differentiation", "Product, quotient and chain rules; implicit, logarithmic and parametric differentiation."),
        ("Series", "Maclaurin and Taylor series."),
        ("Integration", "By parts, substitution and partial fractions; volumes of revolution."),
        ("Differential equations", "First-order differential equations."),
    ]),
    ("3D Vectors", [
        ("Vectors in space", "Scalar product; vector equations of lines and planes; intersections and distances."),
    ]),
]
_PURE_NOTE = "Core pure syllabus; the guide does not split it between Lower and Upper Sixth."
SYLLABI[("pure-mathematics-with-mechanics", "lower-sixth")] = (
    "Pure Mathematics with Mechanics (A Level, 765) — Core Pure", _PURE_NOTE, _PURE_CORE)
SYLLABI[("pure-mathematics-with-statistics", "lower-sixth")] = (
    "Pure Mathematics with Statistics (A Level, 770) — Core Pure", _PURE_NOTE, _PURE_CORE)
