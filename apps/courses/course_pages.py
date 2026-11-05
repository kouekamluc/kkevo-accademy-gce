"""Course page text for the GCE outline courses, applied by `python manage.py load_lessons`.

Key: (subject slug, level slug). `summary` (max 300 characters) shows under the course title;
`outcomes` show as "What you will learn". `title`/`slug` are optional renames (used when the
outline course got a fallback name because a demo course already had the plain one).

KKEVO draft text: check against the official GCE syllabus before publishing the course.
"""

PAGES = {
    ("mathematics", "form-5"): dict(
        title="Form 5 General Mathematics", slug="form-5-general-mathematics",
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
                "binomial expansion, coordinate geometry, an introduction to calculus, and mechanics or statistics.",
        outcomes=[
            "Use the remainder and factor theorems and split simple fractions into partial fractions",
            "Work in radians and solve equations with trigonometric identities",
            "Expand (a + b) raised to a whole-number power and find particular terms",
            "Find equations of straight lines and circles",
            "Differentiate and integrate powers of x to find tangents, stationary points and areas",
            "Solve straight-line motion and force problems, or work with discrete probability distributions",
        ]),
    ("computer-science", "form-5"): dict(
        summary="GCE O Level Computer Science topics on building web pages with HTML5 and CSS, and on the legal, "
                "ethical and social side of computing, including Cameroon's cybersecurity laws.",
        outcomes=[
            "Write a correctly structured HTML5 page with text, links, images, tables and forms",
            "Style pages with inline, internal and external CSS, selectors and the box model",
            "Explain copyright, software piracy and open-source licences",
            "Describe Cameroon's legal framework for cybersecurity, cybercrime and data",
            "Discuss the social and economic effects of ICT",
        ]),
    ("ict", "form-5"): dict(
        summary="Hands-on GCE O Level ICT: build and style web pages, use word processors, spreadsheets and "
                "databases, and understand the laws and social effects of technology in Cameroon.",
        outcomes=[
            "Build and style a simple business web page with HTML5 and CSS",
            "Use word processing and spreadsheet formulas and charts to solve everyday problems",
            "Create and query a small relational database",
            "Respect copyright and licences, and stay within Cameroon's cyber laws",
            "Explain how ICT changes work, business and society",
        ]),
    ("history", "form-5"): dict(
        summary="GCE O Level History: nationalism and independence in French Cameroun and the Southern Cameroons, "
                "reunification, Cameroon since 1961, African decolonization and the Cold War world.",
        outcomes=[
            "Explain the rise of nationalism in French Cameroun and the road to independence in 1960",
            "Trace Southern Cameroons politics from 1953 to the plebiscite and reunification in 1961",
            "Describe Cameroon's change from a federation to a unitary state, and the transitions since 1982",
            "Compare peaceful and armed paths to independence in Africa, and the OAU and AU",
            "Explain the main crises of the Cold War and the world after it",
            "Plan and write clear structured and essay answers",
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
