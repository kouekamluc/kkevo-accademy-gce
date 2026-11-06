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
    ("logic", "form-5"): ("Logic (O Level, 0590)",
                          "Outline taken from the GCE Board's revised 0590 Logic syllabus (first examined June 2025, "
                          "dated March 2024), published at camgceb.org. The Board gives a list of nine modules and "
                          "their topics. Paper 1 is 50 multiple-choice questions in 1 hour 30 minutes; Paper 2 has six "
                          "questions in 2 hours 30 minutes, five to be answered.", [
        ("The Foundation of Logic", [
            ("Definition and origin of Logic", "What logic is and where it comes from."),
            ("Purpose (value) and division (types) of Logic", "Why logic is studied and its main types."),
            ("Logic and related fields", "How logic relates to other subjects."),
            ("Laws of thought", "The laws of thought."),
            ("Operations of the mind", "The three operations of the mind: simple apprehension, judging and reasoning."),
        ]),
        ("First Operation of the Mind: Simple Apprehension (Ideas, Words and Terms)", [
            ("Properties of ideas and terms", "Properties of ideas and of terms."),
            ("Classification of terms according to quantity and quality", "Classifying terms by quantity and quality."),
            ("Classification of terms according to definiteness of meaning and relation", "Classifying terms by definiteness of meaning and by relation."),
        ]),
        ("Definitions and Logical Division", [
            ("The basic functions of language", "What language is used for."),
            ("Basic notions of definition", "What a definition is and what it is for."),
            ("Kinds of definition", "The kinds of definition."),
            ("Rules and fallacies of definition", "The rules of good definition and the fallacies that break them."),
            ("Structure and rules of logical division", "The structure of logical division and its rules."),
        ]),
        ("The Second Operation of the Mind: Judging (Propositions)", [
            ("Definition and components of a proposition", "What a proposition is and its parts."),
            ("Properties of categorical propositions", "Properties of categorical propositions."),
            ("Distribution of terms in categorical propositions", "Which terms are distributed in each categorical proposition."),
            ("Symbolization and Venn diagramming of categorical propositions", "Symbols and Venn diagrams for categorical propositions."),
            ("Hypothetical proposition and types", "Hypothetical propositions and their types."),
            ("Disjunctive proposition and types", "Disjunctive propositions and their types."),
            ("Modal proposition and types", "Modal propositions and their types."),
            ("Translating ordinary propositions into standard forms", "Translating ordinary sentences into standard forms, and propositions from one form to another."),
        ]),
        ("Introduction to Symbolic Logic", [
            ("Basic notions and the importance of symbolic logic", "What symbolic logic is and why it matters."),
            ("Connectives and symbols in symbolic logic", "Connectives and the selected symbols: negation, conjunction, disjunction, material implication and biconditional."),
            ("Logical constants (truth-functional statements)", "Logical constants and truth-functional statements."),
            ("Punctuation in symbolic logic", "Punctuation in symbolic formulas."),
            ("Structure of truth tables and their uses", "How a truth table is built and what it is used for."),
            ("Truth tables and logical constants", "Truth tables for truth-functional statements."),
        ]),
        ("The Third Operation of the Mind: Reasoning (Inference)", [
            ("Methods of reasoning", "Methods of reasoning."),
            ("Definition and types of inference", "What inference is and its types."),
            ("Forms of opposition", "The forms of opposition between propositions."),
            ("Squares and truth table for opposition", "The square of opposition and the truth table for opposition."),
            ("Forms of eduction", "The forms of eduction."),
        ]),
        ("Mediate Inference (Arguments)", [
            ("Structure of an argument", "Premises and conclusion."),
            ("Validity and soundness", "Validity and soundness of arguments."),
            ("Value of the syllogism and structure of the categorical syllogism", "Why the syllogism matters and the structure of the categorical syllogism."),
            ("The figures of the categorical syllogism", "The figures of the categorical syllogism."),
            ("The moods of the categorical syllogism", "The moods of the categorical syllogism."),
            ("Representing categorical syllogisms on the Venn diagram", "Testing categorical syllogisms with Venn diagrams."),
            ("Translating categorical arguments into standard forms", "Putting categorical arguments into standard form."),
            ("The general rules of the syllogism and fallacies", "The general rules of the syllogism and the fallacies from breaking them."),
        ]),
        ("Other Types of Arguments", [
            ("The enthymeme", "The enthymeme."),
            ("The hypothetical syllogism", "The hypothetical syllogism."),
            ("The disjunctive syllogism", "The disjunctive syllogism."),
            ("Definition, nature and importance of the dilemma", "What a dilemma is and why it matters."),
            ("Constructive dilemma", "The constructive dilemma."),
            ("Destructive dilemma", "The destructive dilemma."),
        ]),
        ("Informal Fallacies", [
            ("Definition, classification and significance of fallacies", "What fallacies are, how they are classified and why they matter."),
            ("Fallacies of relevance: fallacies of no evidence", "Fallacies of relevance that offer no evidence."),
            ("Fallacies of relevance: fallacies of little evidence", "Fallacies of relevance that offer little evidence."),
            ("Fallacies of ambiguity", "Fallacies of ambiguity."),
        ]),
        ("Examination", [
            ("Paper 1", "50 multiple-choice questions, all to be answered, in 1 hour 30 minutes; one mark each (40% of the marks)."),
            ("Paper 2", "Six questions in 2 hours 30 minutes: Section A structural (three questions, all answered) and Section B problem-solving (three questions, any two answered); 20 marks each (60%)."),
        ]),
    ]),
    ("english-language", "form-5"): ("English Language (O Level, 0530)",
        "Outline taken from KKEVO's master curriculum blueprint (module and topic list). It is not a Board syllabus booklet, so a teacher should check it against the Board's own syllabus. Paper details follow the GCE Board's 2023 Ordinary Level subject report.", [
        ("Phonology & Listening Comprehension", [
            ("Pure vowel sounds (monophthongs)", "The pure vowel sounds of English."),
            ("Diphthongs and triphthongs", "Gliding vowel sounds."),
            ("Consonant sounds and clusters", "Consonants and consonant clusters."),
            ("Silent letters and homophones", "Silent letters and words that sound alike."),
            ("Word stress and sentence stress", "Stress in words and in sentences."),
            ("Intonation patterns", "Rising and falling intonation."),
            ("Listening comprehension strategies and note-taking", "How to listen for information and take notes."),
        ]),
        ("Grammar & Structural Accuracy", [
            ("Nouns, pronouns and determiners", "Nouns, pronouns and determiners."),
            ("Verb tenses, aspect and mood", "Verb tenses, aspect and mood."),
            ("Subject-verb concord", "Agreement between subject and verb."),
            ("Adjectives, adverbs and comparatives", "Adjectives, adverbs and degrees of comparison."),
            ("Prepositions and conjunctions", "Prepositions and conjunctions."),
            ("Active and passive voice", "Changing between active and passive voice."),
            ("Direct and reported speech", "Changing direct speech to reported speech."),
            ("Clauses", "Main, subordinate, relative and conditional clauses."),
            ("Question tags and phrasal verbs", "Question tags and phrasal verbs."),
            ("Punctuation and capitalization", "Punctuation marks and capital letters."),
        ]),
        ("Vocabulary, Semantics & Register", [
            ("Word formation", "Prefixes, suffixes and compounding."),
            ("Synonyms, antonyms and homonyms", "Words with related, opposite and same-form meanings."),
            ("Idiomatic expressions and proverbs", "Idioms and proverbs."),
            ("Figurative language in context", "Figures of speech in use."),
            ("Register: health, medicine and environment", "Vocabulary for health and the environment."),
            ("Register: science, technology and ICT", "Vocabulary for science and technology."),
            ("Register: commerce, finance and administration", "Vocabulary for business and administration."),
            ("Register: law, governance and human rights", "Vocabulary for law and governance."),
        ]),
        ("Reading Comprehension & Summary", [
            ("Skimming, scanning and main ideas", "Reading quickly for the main ideas and for details."),
            ("Contextual vocabulary deduction", "Working out word meanings from context."),
            ("Tone, attitude and purpose", "Identifying the author's tone, attitude and purpose."),
            ("Factual and inferential questions", "Answering factual and inferential questions."),
            ("Summary writing", "Filtering out repetition and paraphrasing."),
        ]),
        ("Composition & Directed Writing", [
            ("Narrative and descriptive essays", "Narrative and descriptive essays."),
            ("Expository and argumentative essays", "Expository and argumentative or debate essays."),
            ("Formal letters", "Applications, complaints and letters to an editor."),
            ("Informal and semi-formal letters", "Informal and semi-formal letters."),
            ("Speeches, articles, reports and minutes", "Speech writing, articles, reports and minutes."),
        ]),
        ("Examination", [
            ("Paper 1", "50 multiple-choice questions (listening, reading, grammar and vocabulary), 1 hour 30 minutes, marked electronically."),
            ("Paper 2", "Written paper with Section A Directed Writing and Section B Composition (check the exact format with your teacher)."),
        ]),
    ]),
    ("physics", "form-5"): ("Physics (O Level, 0580)",
        "Outline taken from KKEVO's master curriculum blueprint (module and topic list). It is not a Board syllabus booklet, so a teacher should check it against the Board's own syllabus. Paper details follow the GCE Board's 2023 Ordinary Level subject report.", [
        ("Measurement & Physical Quantities", [
            ("SI units", "Fundamental and derived SI units."),
            ("Measuring length, mass, time and volume", "Instruments and methods of measurement."),
            ("Density and relative density", "Density and relative density."),
            ("Scalars and vectors", "Adding and resolving vectors."),
        ]),
        ("Mechanics & Properties of Matter", [
            ("Kinematics and motion graphs", "Speed, velocity, acceleration and motion graphs."),
            ("Equations of uniformly accelerated motion", "The equations of motion and free fall."),
            ("Newton's laws of motion and weight", "Newton's laws and weight."),
            ("Momentum and impulse", "Linear momentum, impulse and conservation of momentum."),
            ("Moments and centre of gravity", "Turning effect of forces and the centre of gravity."),
            ("Work, energy and power", "Work, energy, power and conservation of energy."),
            ("Simple machines", "Levers, pulleys and inclined planes; mechanical advantage, velocity ratio and efficiency."),
            ("Hooke's law and elasticity", "Hooke's law and elasticity."),
            ("Pressure in solids and liquids", "Pressure, pressure in liquids and barometers."),
            ("Upthrust and flotation", "Upthrust, Archimedes' principle and the law of flotation."),
        ]),
        ("Thermal Physics (Heat)", [
            ("Temperature scales and thermometers", "Temperature scales and liquid-in-glass thermometers."),
            ("Thermal expansion", "Expansion of solids, liquids and gases."),
            ("Heat transfer", "Conduction, convection and radiation."),
            ("Specific heat capacity", "Specific heat capacity and calorimetry."),
            ("Change of state and latent heat", "Change of state and specific latent heat."),
            ("Gas laws and kinetic theory", "Boyle's law, Charles' law, the pressure law and kinetic theory."),
        ]),
        ("Waves, Optics & Sound", [
            ("Wave motion and the wave equation", "Transverse and longitudinal waves and the wave equation."),
            ("Wave properties", "Reflection, refraction, diffraction and interference."),
            ("Reflection of light and mirrors", "Rectilinear propagation and reflection at plane and curved mirrors."),
            ("Refraction and total internal reflection", "Refraction, Snell's law and total internal reflection."),
            ("Lenses and optical instruments", "Thin lenses, the eye, the camera and the projector."),
            ("Dispersion and the electromagnetic spectrum", "Dispersion of white light and the electromagnetic spectrum."),
            ("Sound waves", "Production and speed of sound, echoes, pitch, loudness and timbre."),
        ]),
        ("Electricity & Magnetism", [
            ("Electrostatics", "Charging, electric fields and lightning conductors."),
            ("Current, potential difference and Ohm's law", "Current, potential difference, EMF and Ohm's law."),
            ("Resistance and circuits", "Resistance, series and parallel circuits and internal resistance."),
            ("Electrical energy and power", "Electrical energy, power and kilowatt-hour tariff calculations."),
            ("Domestic wiring and safety", "Domestic wiring, fuses, circuit breakers and earthing."),
            ("Magnetism and magnetic fields", "Magnets, magnetic fields and magnetization."),
            ("Electromagnetism and motors", "Force on a current-carrying conductor and the DC motor."),
            ("Electromagnetic induction and transformers", "Faraday's and Lenz's laws, AC generators and transformers."),
        ]),
        ("Atomic, Nuclear & Basic Electronics", [
            ("Atomic structure, nuclides and isotopes", "Atomic structure, nuclide notation and isotopes."),
            ("Radioactivity", "Alpha, beta and gamma radiation."),
            ("Radioactive decay and half-life", "Decay equations, half-life and carbon dating."),
            ("Nuclear fission and fusion", "Fission, fusion and mass-energy equivalence."),
            ("Thermionic emission and the cathode ray oscilloscope", "Thermionic emission and the CRO."),
            ("Semiconductors, diodes and logic gates", "Semiconductors, p-n junction diodes, rectification and basic logic gates."),
        ]),
        ("Examination", [
            ("Paper 1", "50 multiple-choice questions, 1 hour 30 minutes."),
            ("Paper 2", "Written paper, 2 hours 30 minutes: Section I compulsory questions, Section II either/or questions (check the exact format with your teacher)."),
        ]),
    ]),
    ("chemistry", "form-5"): ("Chemistry (O Level, 0515)",
        "Outline taken from KKEVO's master curriculum blueprint (module and topic list). It is not a Board syllabus booklet, so a teacher should check it against the Board's own syllabus. Paper details follow the GCE Board's 2023 Ordinary Level subject report.", [
        ("Matter, Atomic Structure & Bonding", [
            ("States of matter and kinetic theory", "States of matter, kinetic theory and heating and cooling curves."),
            ("Pure substances, mixtures and separation", "Pure substances, mixtures and separation techniques."),
            ("Atomic structure, isotopes and relative atomic mass", "Subatomic particles, isotopes and relative atomic mass."),
            ("Electronic configuration and the periodic table", "Electronic configuration and the organization of the periodic table."),
            ("Periodic trends and groups", "Groups I, II, VII and 0 and the transition metals."),
            ("Chemical bonding", "Ionic, covalent, dative and metallic bonding and intermolecular forces."),
            ("Structure and properties of solids", "Giant ionic, giant covalent and simple molecular solids."),
        ]),
        ("Formulae, Stoichiometry & Mole Concept", [
            ("Symbols, valency and balanced equations", "Chemical symbols, valency, radicals and balanced equations."),
            ("Relative formula mass and percentage composition", "Relative molecular or formula mass and percentage composition."),
            ("The mole and Avogadro's constant", "The mole, Avogadro's constant and molar mass."),
            ("Empirical and molecular formulae", "Empirical and molecular formula calculations."),
            ("Molar gas volume and gas laws", "Molar gas volume, Gay-Lussac's law and Avogadro's law."),
            ("Solution concentration", "Molarity and mass concentration."),
            ("Reacting masses and titration calculations", "Reacting masses, limiting reagents, percentage yield and volumetric titration calculations."),
        ]),
        ("Acids, Bases, Salts & Redox", [
            ("Acids, bases and electrolytes", "Arrhenius and Bronsted-Lowry acids and bases; strong and weak electrolytes."),
            ("The pH scale, indicators and neutralization", "The pH scale, indicators and neutralization reactions."),
            ("Preparation of salts and solubility", "Preparing soluble and insoluble salts; solubility rules and curves."),
            ("Water of crystallization and related terms", "Efflorescence, deliquescence and hygroscopy."),
            ("Oxidation and reduction", "Oxidation and reduction, oxidation numbers and tests for oxidizing and reducing agents."),
        ]),
        ("Energetics, Kinetics & Equilibria", [
            ("Exothermic and endothermic reactions", "Energy profile diagrams."),
            ("Enthalpy changes", "Enthalpy of combustion, neutralization, formation and solution."),
            ("Rate of reaction and collision theory", "Factors affecting rate and collision theory."),
            ("Reversible reactions and equilibrium", "Dynamic equilibrium and Le Chatelier's principle."),
        ]),
        ("Electrochemistry", [
            ("Electrolytes and ionic theory", "Electrolytes, non-electrolytes and ionic theory."),
            ("Mechanism of electrolysis", "Electrolysis and preferential discharge of ions."),
            ("Electrolysis of common electrolytes", "Molten salts, acidified water, brine and copper(II) sulfate with inert and active electrodes."),
            ("Faraday's laws of electrolysis", "Faraday's first and second laws."),
            ("Electrochemical series, cells and electroplating", "The electrochemical series, simple cells and electroplating."),
        ]),
        ("Inorganic Chemistry (Non-Metals & Metals)", [
            ("Hydrogen, oxygen, air and water", "Hydrogen, oxygen, air, water, hardness and water treatment."),
            ("Carbon and its compounds", "Allotropes of carbon, carbon monoxide, carbon dioxide and carbonates."),
            ("Nitrogen and its compounds", "Nitrogen, ammonia, the Haber process, nitric acid and the nitrogen cycle."),
            ("Sulfur and its compounds", "Sulfur, sulfur dioxide and sulfuric acid by the Contact process."),
            ("Chlorine and hydrogen chloride", "Chlorine and hydrogen chloride."),
            ("Reactivity series and extraction of metals", "The reactivity series, and the extraction and properties of sodium, aluminium, iron and copper."),
        ]),
        ("Organic Chemistry & Qualitative Analysis", [
            ("Homologous series and nomenclature", "Homologous series, functional groups, IUPAC names and isomerism."),
            ("Crude oil and cracking", "Fractional distillation of crude oil and cracking."),
            ("Alkanes", "Methane and ethane: combustion and substitution."),
            ("Alkenes and alkynes", "Ethene and ethyne: addition and polymerization."),
            ("Alcohols", "Ethanol: fermentation, oxidation, esterification and dehydration."),
            ("Carboxylic acids, soaps and detergents", "Ethanoic acid, saponification, soaps and detergents."),
            ("Natural and synthetic polymers", "Addition and condensation polymers."),
            ("Qualitative analysis", "Identifying common cations, anions and gases."),
        ]),
        ("Examination", [
            ("Paper 1", "50 multiple-choice questions, 1 hour 30 minutes."),
            ("Paper 2", "Written paper with ten questions in Sections A, B (alternative to practical) and C (check the exact format with your teacher)."),
        ]),
    ]),
    ("biology", "form-5"): ("Biology (O Level, 0510)",
        "Outline taken from KKEVO's master curriculum blueprint (module and topic list). It is not a Board syllabus booklet, so a teacher should check it against the Board's own syllabus. Paper details follow the GCE Board's 2023 Ordinary Level subject report.", [
        ("Taxonomy & Variety of Living Organisms", [
            ("Characteristics of living things and classification", "Characteristics of living things and binomial classification."),
            ("Viruses", "Structure and replication of viruses."),
            ("Bacteria, protoctists and fungi", "Kingdoms Prokaryotae, Protoctista and Fungi."),
            ("Kingdom Plantae", "Bryophytes, filicinophytes, coniferophytes, monocots and dicots."),
            ("Invertebrate animals", "Invertebrate groups and insect life cycles."),
            ("Vertebrate animals", "Fish, amphibians, reptiles, birds and mammals."),
        ]),
        ("Cell Biology & Cellular Transport", [
            ("Microscopy and magnification", "Light and electron microscopes and magnification calculations."),
            ("Plant and animal cell structure", "Ultrastructure and functions of organelles."),
            ("Cell specialization and organization", "Specialized cells, tissues, organs and systems."),
            ("Diffusion, osmosis and active transport", "Movement of substances into and out of cells."),
        ]),
        ("Nutrition in Plants & Animals", [
            ("Food nutrients", "Carbohydrates, proteins, lipids, vitamins, minerals, water and roughage."),
            ("Food tests", "Qualitative food tests."),
            ("Enzymes", "Properties, mechanism and factors affecting enzyme activity."),
            ("Photosynthesis and plant nutrition", "Photosynthesis, limiting factors, leaf adaptations and mineral requirements."),
            ("Nutrition in mammals", "Dentition, the alimentary canal, digestion, absorption and assimilation."),
        ]),
        ("Respiration & Gaseous Exchange", [
            ("Aerobic and anaerobic respiration", "Respiration, fermentation, oxygen debt and ATP."),
            ("Gaseous exchange in plants", "Gaseous exchange surfaces and the stomatal mechanism."),
            ("Gaseous exchange in animals", "Amoeba, earthworm, insects and fish."),
            ("The human respiratory system", "Ventilation mechanism and lung capacities."),
        ]),
        ("Transport, Excretion & Homeostasis", [
            ("Transport in plants", "Root hair uptake, transpiration, translocation and the potometer."),
            ("Mammalian blood", "Blood composition, functions, blood groups and clotting."),
            ("The heart, blood vessels and lymphatic system", "Structure of the heart, the cardiac cycle and blood vessels."),
            ("Excretion and the kidney", "Excretion in plants and animals; the kidney and nephron."),
            ("Osmoregulation, the liver and the skin", "Osmoregulation, liver functions and thermoregulation."),
        ]),
        ("Coordination, Response & Locomotion", [
            ("Plant responses", "Tropisms, taxic and nastic responses and auxins."),
            ("The human nervous system", "Neurones, synapse, brain, spinal cord and reflex actions."),
            ("The eye and the ear", "Structure and function of the eye and ear."),
            ("The endocrine system", "Hormones and the glands that secrete them."),
            ("The skeleton, joints and muscles", "The skeleton, joints and antagonistic muscles."),
        ]),
        ("Reproduction, Growth & Genetics", [
            ("Cell division", "Mitosis and meiosis."),
            ("Asexual reproduction and vegetative propagation", "Asexual reproduction and vegetative propagation."),
            ("Sexual reproduction in flowering plants", "Flower structure, pollination, fertilization, dispersal and germination."),
            ("Human reproduction", "Reproductive systems, the menstrual cycle, fertilization, pregnancy, birth and contraception."),
            ("DNA and inheritance", "DNA, Mendelian inheritance, sex determination and sex linkage."),
            ("Variation, mutation and evolution", "Variation, mutation, natural selection and theories of evolution."),
        ]),
        ("Ecology & Community Health", [
            ("Ecological concepts and food webs", "Habitats, trophic levels, food chains, webs and pyramids."),
            ("Energy flow, populations and cycles", "Energy flow, population estimation and biogeochemical cycles."),
            ("Biological associations", "Parasitism, mutualism, commensalism and predation."),
            ("Human impact on the environment", "Pollution, deforestation, eutrophication and conservation."),
            ("Pathogens, immunity and disease control", "Pathogens, immunity and the control of common diseases."),
        ]),
        ("Examination", [
            ("Paper 1", "50 multiple-choice questions in six sections, marked electronically."),
            ("Paper 2", "Seven essay-type questions: Section A three compulsory, Section B any two of four (check the exact format with your teacher)."),
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
    ("Examination", [
        ("Paper 1", "Multiple-choice paper covering the whole core (KKEVO practice setting; check the paper format with your teacher)."),
        ("Paper 2", "Structured pure mathematics paper (KKEVO practice setting; check the paper format with your teacher)."),
    ]),
]
_PURE_NOTE = "Core pure syllabus; the guide does not split it between Lower and Upper Sixth."
SYLLABI[("pure-mathematics-with-mechanics", "lower-sixth")] = (
    "Pure Mathematics with Mechanics (A Level, 765) — Core Pure", _PURE_NOTE, _PURE_CORE)
SYLLABI[("pure-mathematics-with-statistics", "lower-sixth")] = (
    "Pure Mathematics with Statistics (A Level, 770) — Core Pure", _PURE_NOTE, _PURE_CORE)


# A Level courses that have a practice paper: KKEVO's own exam practice, not a Board paper.
for _key in [("computer-science", "lower-sixth"), ("computer-science", "upper-sixth"),
             ("ict", "lower-sixth"), ("ict", "upper-sixth"),
             ("history", "lower-sixth"), ("history", "upper-sixth")]:
    SYLLABI[_key][2].append(("Examination", [
        ("Practice paper", "KKEVO practice paper for this year (check the real paper format with your teacher)."),
    ]))
