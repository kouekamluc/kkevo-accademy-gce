"""Course page text for the GCE outline courses, applied by `python manage.py load_lessons`.

Key: (subject slug, level slug). `summary` (max 300 characters) shows under the course title;
`outcomes` show as "What you will learn". `title`/`slug` are optional renames (used when the
outline course got a fallback name because a demo course already had the plain one).

KKEVO draft text: check against the official GCE syllabus before publishing the course.
"""

PAGES = {
    ("mathematics", "form-5"): dict(
        title="Form 5 General Mathematics", slug="form-5-general-mathematics", primary=True,
        summary="Everything for GCE O Level General Mathematics: sets and logic, commercial maths, quadratics, "
                "sequences, matrices and vectors, trigonometry and bearings, circle theorems, statistics and "
                "probability. Each lesson explains, works examples, then lets you practise.",
        outcomes=[
            "Solve problems with Venn diagrams, logic, compound interest, hire purchase and variation",
            "Solve quadratic equations by factorization, completing the square and the formula, and read their graphs",
            "Use the nth term and sum of arithmetic and geometric progressions",
            "Work with 2×2 matrices and column vectors, including solving simultaneous equations",
            "Apply the sine and cosine rules, bearings and circle theorems",
            "Draw and interpret histograms and ogives, and calculate probabilities with tree diagrams",
        ]),
    ("additional-mathematics", "form-5"): dict(
        summary="GCE O Level Additional Mathematics: polynomials, partial fractions, radians and identities, the "
                "binomial expansion, lines and circles, differentiation and integration, then your applied "
                "option (Mechanics or Statistics), with timed mock papers.",
        outcomes=[
            "Use the remainder and factor theorems and split simple fractions into partial fractions",
            "Work in radians and solve equations with trigonometric identities",
            "Expand (a + b) raised to a whole-number power and find particular terms",
            "Find equations of straight lines and circles",
            "Differentiate and integrate powers of x to find tangents, stationary points and areas",
            "Solve straight-line motion and force problems, or work with discrete probability distributions",
        ]),
    ("computer-science", "form-5"): dict(
        summary="GCE O Level Computer Science: build and style web pages with HTML5 and CSS, learn the legal, "
                "ethical and social side of computing, and practise the exam skills (logic circuits, pseudo-code, "
                "trace tables, database design, the practical lab) with timed mock papers.",
        outcomes=[
            "Write a correctly structured HTML5 page with text, links, images, tables and forms",
            "Style pages with inline, internal and external CSS, selectors and the box model",
            "Explain copyright, software piracy and open-source licences",
            "Describe Cameroon's legal framework for cybersecurity and cybercrime, in general terms",
            "Discuss the social and economic effects of ICT",
            "Draw logic circuits and truth tables, write pseudo-code and complete trace tables",
            "Design a simple database and prepare for the timed practical paper",
        ]),
    ("ict", "form-5"): dict(
        summary="Hands-on GCE O Level ICT: build and style web pages, use word processors, spreadsheets and "
                "databases, understand the laws and social effects of technology in Cameroon, and prepare for "
                "the theory and practical papers with timed mock papers.",
        outcomes=[
            "Build and style a simple business web page with HTML5 and CSS",
            "Use word processing and spreadsheet formulas and charts to solve everyday problems",
            "Create, query and report from a small relational database",
            "Respect copyright and licences, and follow Cameroon's cyber rules in general terms",
            "Explain how ICT changes work, business and society",
            "Plan your time and work through typical tasks in the practical lab",
        ]),
    ("history", "form-5"): dict(
        summary="GCE O Level History: nationalism and independence in French Cameroun and the Southern Cameroons, "
                "reunification, Cameroon since 1961, African decolonization and the Cold War world, with "
                "exam-technique lessons and a timed multiple-choice mock paper.",
        outcomes=[
            "Explain the rise of nationalism in French Cameroun and the road to independence in 1960",
            "Trace Southern Cameroons politics from 1953 to the plebiscite and reunification in 1961",
            "Describe Cameroon's change from a federation to a unitary state, and the transitions since 1982",
            "Compare peaceful and armed paths to independence in Africa, and the OAU and AU",
            "Explain the main crises of the Cold War and the world after it",
            "Plan and write clear structured and essay answers",
        ]),
    ("geography", "form-5"): dict(
        title="Form 5 Geography (GCE 0550)", slug="form-5-geography-gce-0550", primary=True,
        summary="GCE O Level Geography, built on the Board's revised 0550 syllabus: map reading and interpretation, "
                "physical and human geography, and the Geography of Cameroon, with Paper 1 and Paper 2 practice and "
                "timed mock papers.",
        outcomes=[
            "Read maps: grid references, bearings, scales, distances, areas and contours",
            "Describe relief, drainage, settlement and land use from a map and draw sketch maps",
            "Explain weather, climate, the water cycle, soils, vegetation and ecosystems",
            "Explain how rocks, volcanoes, earthquakes, rivers, waves and wind shape the land",
            "Explain development, agriculture, industry, trade, population and settlement",
            "Describe the physical, human and economic geography of Cameroon",
            "Answer Paper 1 multiple choice and plan Paper 2 map-reading and essay questions",
        ]),
    ("logic", "form-5"): dict(
        summary="GCE O Level Logic, built on the Board's revised 0590 syllabus: ideas and terms, definitions, "
                "propositions, symbolic logic and truth tables, inference and syllogisms, other arguments and "
                "fallacies, with Paper 1 and Paper 2 practice and timed mock papers.",
        outcomes=[
            "Explain what logic is, its laws of thought and the three operations of the mind",
            "Classify terms and write and test definitions and logical divisions",
            "Write categorical, hypothetical, disjunctive and modal propositions in standard form",
            "Use symbols and truth tables to test statements",
            "Test syllogisms and other arguments for validity and soundness",
            "Spot formal and informal fallacies in everyday reasoning",
            "Answer Paper 1 multiple choice and plan Paper 2 structured and problem-solving questions",
        ]),
    ("english-language", "form-5"): dict(
        title="Form 5 English Language (GCE 0530)", slug="form-5-english-language-gce-0530", primary=True,
        summary="GCE O Level English Language: sounds and listening, grammar, vocabulary and register, reading and summary, composition and directed writing, with Paper 1 and Paper 2 practice and a timed mock paper.",
        outcomes=[
            "Use English sounds, stress and intonation and listen for information",
            "Write accurate sentences with correct tenses, concord, voice and reported speech",
            "Build vocabulary and use the right register for health, science, commerce and law",
            "Read passages for main ideas, tone and inference and write a summary",
            "Write essays, letters, speeches, articles and reports, and handle directed writing",
            "Answer Paper 1 multiple choice and plan Paper 2 Directed Writing and Composition",
        ]),
    ("physics", "form-5"): dict(
        title="Form 5 Physics (GCE 0580)", slug="form-5-physics-gce-0580", primary=True,
        summary="GCE O Level Physics: measurement, mechanics, heat, waves, light and sound, electricity and magnetism, and atomic and nuclear physics, with Paper 1 and Paper 2 practice and timed mock papers.",
        outcomes=[
            "Measure quantities and use vectors, units and density",
            "Solve problems on motion, forces, momentum, moments, work, energy and pressure",
            "Explain heat transfer, thermal properties and the gas laws",
            "Describe waves, reflection, refraction, lenses, sound and the electromagnetic spectrum",
            "Analyse electric circuits, domestic electricity, magnetism and induction",
            "Explain radioactivity, nuclear energy and basic electronics",
            "Answer Paper 1 multiple choice and plan Paper 2 Section I and Section II questions",
        ]),
    ("chemistry", "form-5"): dict(
        title="Form 5 Chemistry (GCE 0515)", slug="form-5-chemistry-gce-0515", primary=True,
        summary="GCE O Level Chemistry: atoms and bonding, the mole concept, acids and salts, energy changes, rates, electrolysis, inorganic and organic chemistry and qualitative analysis, with Paper 1 and Paper 2 practice and timed mock papers.",
        outcomes=[
            "Explain atomic structure, the periodic table and bonding",
            "Do mole, concentration and titration calculations",
            "Prepare salts and use acids, bases and redox ideas",
            "Explain energy changes, rates of reaction and equilibrium",
            "Describe electrolysis and the chemistry of common non-metals and metals",
            "Name and describe organic compounds and identify ions and gases",
            "Answer Paper 1 multiple choice and plan Paper 2 including Alternative to Practical questions",
        ]),
    ("biology", "form-5"): dict(
        title="Form 5 Biology (GCE 0510)", slug="form-5-biology-gce-0510", primary=True,
        summary="GCE O Level Biology: living organisms, cells, nutrition, respiration, transport, coordination, reproduction and genetics, and ecology and health, with Paper 1 and Paper 2 practice and timed mock papers.",
        outcomes=[
            "Classify living organisms and describe cell structure and transport",
            "Explain nutrition, enzymes, respiration and gaseous exchange",
            "Describe transport, excretion, homeostasis, coordination and movement",
            "Explain reproduction, inheritance, variation and evolution",
            "Describe ecosystems, human impact and the control of disease",
            "Answer Paper 1 questions of six types and plan Paper 2 essay questions",
        ]),
    ("pure-mathematics-with-mechanics", "lower-sixth"): dict(
        summary="The core pure mathematics of GCE A Level Pure Mathematics with Mechanics: proof, algebra and "
                "functions, trigonometry, conic sections, calculus, series, differential equations and 3D vectors.",
        outcomes=[
            "Prove results by induction and by contradiction",
            "Use partial fractions, the binomial theorem and the roots of polynomials",
            "Work with composite and inverse functions and sketch curves with asymptotes",
            "Use compound, double and half-angle identities and the harmonic form R cos(θ ± α)",
            "Differentiate and integrate with the standard rules and techniques, including series",
            "Solve first-order differential equations and problems with lines and planes in 3D",
        ]),
    ("pure-mathematics-with-statistics", "lower-sixth"): dict(
        summary="The core pure mathematics of GCE A Level Pure Mathematics with Statistics: proof, algebra and "
                "functions, trigonometry, conic sections, calculus, series, differential equations and 3D vectors.",
        outcomes=[
            "Prove results by induction and by contradiction",
            "Use partial fractions, the binomial theorem and the roots of polynomials",
            "Work with composite and inverse functions and sketch curves with asymptotes",
            "Use compound, double and half-angle identities and the harmonic form R cos(θ ± α)",
            "Differentiate and integrate with the standard rules and techniques, including series",
            "Solve first-order differential equations and problems with lines and planes in 3D",
        ]),
    ("computer-science", "lower-sixth"): dict(
        summary="GCE A Level Computer Science, year 1: how computers work inside, digital logic, operating "
                "systems and translators, networks, software engineering and procedural programming.",
        outcomes=[
            "Explain the Von Neumann and Harvard models and trace the fetch–decode–execute cycle",
            "Design and simplify logic circuits with Boolean algebra and Karnaugh maps",
            "Compare scheduling algorithms and memory management methods",
            "Describe the stages of a compiler and the roles of interpreters and assemblers",
            "Use the OSI and TCP/IP models, subnet IPv4 addresses and check data with CRC",
            "Write structured, recursive programs with files and pointers",
        ]),
    ("computer-science", "upper-sixth"): dict(
        summary="GCE A Level Computer Science, year 2: data structures and algorithms, complexity, relational "
                "databases and SQL, object-oriented programming, and a guide to the individual project.",
        outcomes=[
            "Implement and trace stacks, queues, linked lists and binary search trees",
            "Compare searching and sorting algorithms using Big-O notation",
            "Use relational algebra, normalize tables to 3NF and BCNF, and write SQL queries with joins",
            "Design classes with encapsulation, inheritance and polymorphism",
            "Plan, build, test and report on an individual software project",
        ]),
    ("ict", "lower-sixth"): dict(
        summary="GCE A Level ICT, year 1: PC hardware and operating system deployment, business technologies, "
                "green computing, database automation, and modern web layout with HTML5, CSS3 and JavaScript.",
        outcomes=[
            "Identify PC components, configure BIOS/UEFI and diagnose start-up problems",
            "Install operating systems and choose partition schemes, file systems and virtual machines",
            "Explain e-commerce, VPNs and VoIP for businesses",
            "Reduce energy use and manage e-waste responsibly",
            "Automate database tasks",
            "Build responsive layouts with Flexbox and Grid and add interactivity with JavaScript",
        ]),
    ("ict", "upper-sixth"): dict(
        summary="GCE A Level ICT, year 2: network cabling and switching, cybersecurity and cryptography, defence "
                "and disaster recovery, advanced Excel, and IT project management.",
        outcomes=[
            "Terminate network cables and plan VLANs and DHCP scopes",
            "Apply the CIA triad and explain symmetric and asymmetric encryption, hashing and signatures",
            "Plan firewalls, intrusion detection and disaster recovery",
            "Use lookups, pivot tables, Solver and macros in Excel",
            "Plan IT projects with work breakdown structures, critical path analysis and Gantt charts",
        ]),
    ("history", "lower-sixth"): dict(
        summary="GCE A Level History, year 1: Cameroon under German, British and French rule (1884–1945), the 1848 "
                "revolutions, Italian and German unification, imperialism, the First World War and the interwar crises.",
        outcomes=[
            "Evaluate the Germano-Douala Treaty and the making of Cameroon's borders",
            "Compare German, British and French colonial rule in Cameroon",
            "Explain the causes and failure of the 1848 revolutions and the unification of Italy and Germany",
            "Assess interpretations of the Scramble for Africa and the causes of the First World War",
            "Explain the rise of Fascism and Nazism and judge the policy of appeasement",
            "Write analytical essays that weigh evidence and historians' views",
        ]),
    ("history", "upper-sixth"): dict(
        summary="GCE A Level History, year 2: Cameroon from trusteeship to today, decolonization across Africa, "
                "the struggle against apartheid, the Cold War, the United Nations and regional integration.",
        outcomes=[
            "Analyse trusteeship, nationalism and decolonization in both Cameroons",
            "Evaluate the plebiscite, Foumban and the evolution of the post-colonial state",
            "Compare constitutional and armed paths to independence in Africa",
            "Explain the anti-apartheid struggle in South Africa",
            "Assess Cold War rivalry, the work of the UN and regional bodies such as the AU, CEMAC and ECOWAS",
            "Write analytical essays that weigh evidence and historians' views",
        ]),
}
