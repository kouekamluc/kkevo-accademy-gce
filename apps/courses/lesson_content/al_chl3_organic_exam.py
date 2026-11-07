"""Lower Sixth Chemistry (A Level 0715): Foundations of Organic Chemistry (6 topics) and the Examination module.

Draft content built from KKEVO's master curriculum blueprint, not from a Board syllabus booklet; a reviewer must check
it against the Board's syllabus and textbooks. Exam facts are only those of the Board's 2023 subject report: three
papers (Paper 1 multiple choice with 50 questions, Paper 2 structured theory in three sections, Paper 3 practical with
quantitative and qualitative analysis plus school-based assessment). Study plans and checklists are KKEVO advice.

Notation (converted by fx() at the bottom): [[CH3CH2OH]] is a formula or equation in running text,
<<2H2 + O2 -> 2H2O>> is the same as bare LaTeX for a math= or check= field; ^ gives a charge (Cu^2+).
Relative atomic masses: H 1, C 12, N 14, O 16, F 19, Na 23, Mg 24, S 32, Cl 35.5, K 39, Ca 40, Mn 55, Fe 56, Br 80, I 127.
Every structure, name, formula and isomer count was checked by script (RDKit, OPSIN name-to-structure, brute-force enumeration).
"""

import re

from .dsl import *  # noqa: F403

COURSE = ("chemistry", "lower-sixth")

M_ORG = "Foundations of Organic Chemistry"
M_EXAM = "Examination"

_ARROWS = {"->": r"\rightarrow ", "<=>": r"\rightleftharpoons ", "+": "+", "=": "="}


def _tok(t):
    """One token of a chemical formula or equation -> LaTeX (see the notation note above)."""
    if t in _ARROWS:
        return _ARROWS[t]
    if re.fullmatch(r"[\d.]+|n", t):
        return t
    coef = ""
    m = re.match(r"^(\d+)(?=[A-Z(\[e])", t)
    if m:
        coef, t = m.group(1) + r"\,", t[m.end():]
    ch = ""
    if "^" in t:
        t, ch = t.split("^", 1)
        ch = "^{" + ch + "}"
    t = re.sub(r"(?<=[A-Za-z)\]])(\d+)", r"_{\1}", t).replace(".", r"\cdot ").replace("#", r"\equiv ")
    return coef + r"\mathrm{" + t + ch + "}"


def _eq(s):
    return " ".join(_tok(t) for t in s.split())


def fx(s):
    """[[CH4]] -> inline maths; <<2H2 + O2 -> 2H2O>> -> bare LaTeX for a math= field."""
    s = re.sub(r"\[\[!(.+?)\]\]", lambda m: r"$\mathrm{" + m.group(1) + "}$", s)
    s = re.sub(r"\[\[(.+?)\]\]", lambda m: "$" + _eq(m.group(1)) + "$", s)
    return re.sub(r"<<(.+?)>>", lambda m: _eq(m.group(1)), s)


def _walk(x):
    if isinstance(x, str):
        return fx(x)
    if isinstance(x, list):
        return [_walk(i) for i in x]
    if isinstance(x, dict):
        return {k: _walk(v) for k, v in x.items()}
    return x


LESSONS = []

# ============================================================================================
# Topic 1. Classification and IUPAC nomenclature (lesson 1 of 2)
# ============================================================================================
LESSONS += [lesson(
    module=M_ORG, topic="Classification and IUPAC nomenclature",
    title="Classifying organic compounds: homologous series and functional groups",
    slug="chl3-classification-functional-groups", minutes=22,
    summary="Organic compounds are grouped into homologous series by functional group and general formula, and further classified as aliphatic or aromatic, saturated or unsaturated, primary, secondary or tertiary.",
    objectives=[
        "Define a functional group and a homologous series and give the features of a series",
        "Recognise the main functional groups and write the general formula of each series",
        "Classify compounds as aliphatic, alicyclic or aromatic, saturated or unsaturated, and as primary, secondary or tertiary",
        "Use the general formula and the degree of unsaturation to work out a molecular formula",
    ],
    key_concepts=["Functional group", "Homologous series", "General formula", "Primary, secondary and tertiary", "Degree of unsaturation", "Skeletal formula"],
    blocks=[
        H("Introduction"),
        T("The gas in a kitchen cylinder in Douala is mostly butane and propane. Palm wine contains ethanol, vinegar contains ethanoic acid, and the shopping bag you carry is made of poly(ethene). Different substances, but all are compounds of **carbon**, and that is the field of **organic chemistry**."),
        T("There are millions of organic compounds, so chemists sort them into families. Members of a family react in the same way because they share one small group of atoms. Learning the families, and how to recognise them from a formula, is the first skill of organic chemistry."),
        H("Why carbon, and what is a hydrocarbon?"),
        T("A carbon atom forms four covalent bonds. It can bond to other carbon atoms to make long chains, branched chains and rings (this is called **catenation**), and it forms strong bonds to hydrogen, oxygen, nitrogen and the halogens. This is why carbon has so many compounds."),
        D("A **hydrocarbon** is a compound containing carbon and hydrogen only. A **saturated** compound has only single bonds between carbon atoms. An **unsaturated** compound has at least one carbon-carbon double or triple bond.", title="Hydrocarbons"),
        H("Functional groups and homologous series"),
        D("A **functional group** is an atom or group of atoms in a molecule that is responsible for its characteristic chemical reactions.", title="Functional group"),
        D("A **homologous series** is a family of compounds with the same functional group and the same general formula. Each member differs from the next by one [[CH2]] group.", title="Homologous series"),
        T("Members of a homologous series have similar chemical properties, because they have the same functional group. Their physical properties change steadily along the series. For example, boiling points rise as the chain gets longer, because the instantaneous dipole-induced dipole forces between molecules get stronger."),
        CODE("""Series            Functional group     General formula   Example
alkane            C-C (single only)    CnH2n+2           ethane  CH3CH3
alkene            C=C                  CnH2n             propene CH3CH=CH2
alkyne            C≡C                  CnH2n-2           propyne CH3C≡CH
haloalkane        -X (F, Cl, Br, I)    CnH2n+1X          bromoethane CH3CH2Br
alcohol           -OH                  CnH2n+1OH         ethanol CH3CH2OH
ether             C-O-C                CnH2n+2O          methoxymethane CH3OCH3
aldehyde          -CHO                 CnH2nO            ethanal CH3CHO
ketone            C=O inside chain     CnH2nO            propanone CH3COCH3
carboxylic acid   -COOH                CnH2nO2           ethanoic acid CH3COOH
ester             -COO-                CnH2nO2           methyl ethanoate CH3COOCH3
amine             -NH2                 CnH2n+3N          ethylamine CH3CH2NH2
nitrile           -C≡N                 CnH2n-1N          ethanenitrile CH3CN
amide             -CONH2               CnH2n+1NO         ethanamide CH3CONH2""", "text", title="The main series (n is the number of carbon atoms)"),
        TIP("Learn this table by writing it out from memory twice. Note the pairs with the same general formula: aldehydes and ketones, carboxylic acids and esters, alcohols and ethers. These pairs are **functional-group isomers** (next lessons)."),
        H("Writing the formula in different ways"),
        T("The same compound can be shown in several ways. For ethanoic acid:"),
        CODE("""empirical formula   CH2O      simplest whole-number ratio of atoms
molecular formula   C2H4O2    actual number of atoms of each element
structural formula  CH3COOH   shows the groups (condensed)
displayed formula   every atom and every bond drawn
skeletal formula    zig-zag line, each corner or end is a C atom,
                    H atoms on carbon are not shown""", "text", title="Types of formula"),
        T("In a **skeletal formula** the corners and line ends are carbon atoms, and you add the hydrogen atoms mentally so that each carbon has four bonds. Atoms other than carbon and hydrogen, such as O, N, Br, and the hydrogen in an -OH group, **are** written."),
        H("Classifying compounds"),
        KEY("Three ways to classify", "Organic compounds can be sorted by their carbon skeleton, by their bonds and by where the functional group sits.", cards=[
            ["Skeleton", "**Aliphatic**: straight or branched chains and non-aromatic rings. **Alicyclic** means aliphatic with a ring, such as cyclohexane. **Aromatic**: contains a benzene ring."],
            ["Bonding", "**Saturated**: only C-C single bonds. **Unsaturated**: at least one C=C or C≡C bond."],
            ["Position of the group", "**Primary**, **secondary** or **tertiary** (1°, 2°, 3°), explained below."],
        ]),
        D("For a haloalkane or an alcohol, count the carbon atoms joined directly to the carbon that carries the -X or -OH group. If it is attached to **one** other carbon the compound is **primary**; to **two**, **secondary**; to **three**, **tertiary**. For an amine, the degree is the number of carbon groups joined to the nitrogen atom.", title="Primary, secondary and tertiary"),
        EX("Worked example 1: primary, secondary or tertiary?", intro="Classify (a) [[CH3CH2CH2OH]], (b) [[CH3CH(OH)CH3]], (c) [[(CH3)3CBr]], (d) [[(CH3)2CHCH2Br]].", steps=[
            S("(a) Find the carbon carrying -OH", text="It is the end carbon, joined to one other carbon. So propan-1-ol is a **primary** alcohol."),
            S("(b) The carbon carrying -OH", text="It is joined to two carbon atoms (two CH3 groups). So propan-2-ol is a **secondary** alcohol."),
            S("(c) The carbon carrying -Br", text="It is joined to three CH3 groups. So 2-bromo-2-methylpropane is a **tertiary** haloalkane."),
            S("(d) The carbon carrying -Br", text="It is a CH2 group joined to one carbon only (the CH). The branch is **next** to it, not on it. So 1-bromo-2-methylpropane is a **primary** haloalkane."),
        ]),
        H("Degree of unsaturation"),
        T("The formula of a compound tells you how many rings or double bonds it contains. A saturated, non-cyclic hydrocarbon has the formula [[!C_nH_{2n+2}]]. Each C=C bond or each ring removes two hydrogen atoms; each C≡C bond removes four. The number of rings plus double bonds (counting a triple bond as two) is the **degree of unsaturation**."),
        F(r"\text{degree of unsaturation} = \dfrac{2C + 2 + N - H - X}{2}", title="Degree of unsaturation (C, H, N and halogen atoms X; oxygen is ignored)"),
        EX("Worked example 2: degree of unsaturation", intro="Find the degree of unsaturation of (a) [[C4H8]], (b) [[C5H8]], (c) [[C7H8]] (methylbenzene).", steps=[
            S("(a) [[C4H8]]", math=r"\dfrac{2(4) + 2 - 8}{2} = 1", text="One C=C double bond or one ring (for example but-1-ene or cyclobutane)."),
            S("(b) [[C5H8]]", math=r"\dfrac{2(5) + 2 - 8}{2} = 2", text="Two double bonds, or one triple bond, or one ring plus one double bond."),
            S("(c) [[C7H8]]", math=r"\dfrac{2(7) + 2 - 8}{2} = 4", text="A benzene ring accounts for 4: the ring is 1 and the three C=C bonds are 3."),
        ]),
        EX("Worked example 3: using general formulae", intro="(a) An alkane has 22 hydrogen atoms. How many carbon atoms? (b) An alcohol [[!C_nH_{2n+1}OH]] has relative molecular mass 74. Find its formula. (Ar: C 12, H 1, O 16.)", steps=[
            S("(a) Alkane: [[!C_nH_{2n+2}]]", math=r"2n + 2 = 22 \;\Rightarrow\; n = 10", text="The alkane is [[C10H22]] (decane)."),
            S("(b) Write Mr in terms of n", math=r"M_r = 12n + (2n + 1) + 16 + 1 = 14n + 18"),
            S("Solve", math=r"14n + 18 = 74 \;\Rightarrow\; n = 4", text="The alcohol is [[C4H9OH]], that is butanol ([[C4H10O]])."),
        ], check=r"4 \times 12 + 10 \times 1 + 16 = 74"),
        H("Common mistakes"),
        MISTAKE("Counting branches instead of the carbon holding the group", "The class of a haloalkane or alcohol depends on the carbon that carries the -X or -OH, not on how branched the rest of the molecule is. 1-bromo-2-methylpropane is primary even though it has a branch."),
        MISTAKE("Mixing up aldehydes and ketones", "Both contain C=O. In an aldehyde the C=O carbon is at the **end** of the chain and carries a hydrogen (-CHO). In a ketone it is **inside** the chain, joined to two carbon atoms."),
        MISTAKE("Forgetting that -OH in an acid is not an alcohol", "In [[CH3COOH]] the -OH is part of the -COOH group. The compound is a carboxylic acid, not an alcohol."),
        MISTAKE("Using the alkane formula for every hydrocarbon", "[[!C_nH_{2n+2}]] is for alkanes only. Alkenes are [[!C_nH_{2n}]] and alkynes [[!C_nH_{2n-2}]]."),
        QUIZ("Which general formula belongs to the alkenes?", [r"$\mathrm{C_nH_{2n+2}}$", r"$\mathrm{C_nH_{2n}}$", r"$\mathrm{C_nH_{2n-2}}$", r"$\mathrm{C_nH_{2n+1}OH}$"], 1,
             "Each C=C double bond removes two hydrogen atoms from the alkane formula, so alkenes are [[!C_nH_{2n}]].",
             feedback=["That is the alkane formula (fully saturated).", "", "That is the formula for alkynes (one C≡C bond), or alkadienes.", "That is the formula for alcohols."]),
        QUIZ("The compound [[(CH3)2CHCH2Br]] is best described as", ["a tertiary haloalkane, because it has a branched chain", "a secondary haloalkane, because it has two methyl groups", "a primary haloalkane", "an unsaturated haloalkane"], 2,
             "The carbon bonded to Br (the CH2) is attached to one carbon only, so the compound is primary. Branching elsewhere does not change this.",
             feedback=["Tertiary needs the carbon holding Br to be joined to three carbons.", "The two methyl groups are on the next carbon, not on the carbon holding Br.", "", "There are no double bonds in the molecule, so it is saturated."]),
        H("Practice questions"),
        PQ("(a) Define a homologous series. (b) State **two** features shared by members of a homologous series.",
           "(a) A family of organic compounds with the same functional group and the same general formula, each member differing from the next by a [[CH2]] group. (b) Any two of: same functional group; same general formula; similar chemical properties; steady gradation of physical properties such as boiling point; successive members differ by [[CH2]]."),
        PQ("Name the functional groups in [[CH3CH(OH)CH2COOH]] and state the class of the alcohol group.",
           "A hydroxyl group (-OH, alcohol) and a carboxyl group (-COOH, carboxylic acid). The carbon carrying -OH is joined to two other carbons (the CH3 and the CH2), so it is a secondary alcohol group."),
        PQ("A hydrocarbon has molecular formula [[C6H12]]. (a) Find its degree of unsaturation. (b) Give the structural formula of one alkene and one alicyclic compound with this formula.",
           "(a) (2 × 6 + 2 − 12) / 2 = 1. (b) Alkene: [[CH3CH2CH2CH2CH=CH2]] (hex-1-ene). Alicyclic: cyclohexane, a ring of six [[CH2]] groups."),
        PQ("A compound [[!C_nH_{2n+2}O]] has relative molecular mass 46. Find n and give the structural formulae of two possible compounds. (Ar: C 12, H 1, O 16.)",
           "14n + 18 = 46, so n = 2 and the formula is [[C2H6O]]. Possible compounds: ethanol [[CH3CH2OH]] (alcohol) and methoxymethane [[CH3OCH3]] (ether). They are functional-group isomers."),
        TIP("In the exam: classification and nomenclature appear in Paper 1 multiple choice and in the organic section of Paper 2 (naming compounds, identifying functional groups and writing formulae of isomers). Show every bond clearly in displayed formulae."),
        H("Summary"),
        SUM("A functional group is the atom or group responsible for the characteristic reactions of a compound.",
            "A homologous series has one functional group, one general formula, steady gradation of physical properties and members that differ by [[CH2]].",
            "Aliphatic means chains and non-aromatic rings; aromatic means a benzene ring. Saturated means only single bonds between carbons.",
            "Primary, secondary and tertiary depend on the number of carbons attached to the carbon bearing the group (for amines, to the nitrogen).",
            "Degree of unsaturation = (2C + 2 + N − H − X)/2, the number of rings plus double bonds (a triple bond counts as two)."),
    ])]
# ============================================================================================
# Topic 1. Classification and IUPAC nomenclature (lesson 2 of 2)
# ============================================================================================
LESSONS += [lesson(
    module=M_ORG, topic="Classification and IUPAC nomenclature",
    title="IUPAC nomenclature: naming alkanes, alkenes, alkynes, haloalkanes, alcohols and carbonyl compounds",
    slug="chl3-iupac-naming", minutes=24,
    summary="Name organic compounds by the IUPAC rules: find the parent chain, give the principal group the lowest number, list prefixes alphabetically; and draw a structure from its name.",
    objectives=[
        "Name branched alkanes, alkenes, alkynes, haloalkanes and alcohols by the IUPAC rules",
        "Name aldehydes, ketones, carboxylic acids and esters, and use hydroxy as a prefix when a higher-priority group is present",
        "Draw structural and skeletal formulae from IUPAC names",
        "Avoid the common errors: wrong chain, wrong numbering, wrong alphabetical order",
    ],
    key_concepts=["Parent chain", "Locant", "Principal group", "Alphabetical order of prefixes", "Priority of functional groups"],
    blocks=[
        H("Introduction"),
        T("In a pharmacy in Yaoundé, a bottle may say \"ethanol\", \"methylated spirit\" or \"alcohol\", and a student may call the same substance \"ethyl alcohol\". Common names are fine for shop labels, but chemists everywhere need **one name for one structure**. The International Union of Pure and Applied Chemistry (IUPAC) set the rules, and an exam question that asks you to \"name\" a compound expects them."),
        H("The parts of an IUPAC name"),
        T("Every name is built from three parts: a **prefix** (branches and halogens), a **stem** (how many carbon atoms in the longest chain) and a **suffix** (the principal functional group)."),
        CODE("""Stem   C atoms      Stem   C atoms
meth     1          hex      6
eth      2          hept     7
prop     3          oct      8
but      4          non      9
pent     5          dec     10""", "text", title="Stems for the carbon chain"),
        CODE("""Series            Ending                  Example
alkane            -ane                    propane
alkene            -ene                    propene
alkyne            -yne                    propyne
alcohol           -ol                     propan-1-ol
aldehyde          -al                     propanal
ketone            -one                    propanone
carboxylic acid   -oic acid               propanoic acid
haloalkane        prefix fluoro-, chloro-, bromo-, iodo-    2-bromopropane
ester             alkyl -oate             methyl propanoate""", "text", title="Suffixes and prefixes"),
        D("1. Find the **longest continuous chain** that contains the principal functional group (and any double or triple bond). This is the parent chain.\n\n2. **Number** the chain from the end that gives the **lowest number to the principal group**. If there is a tie, give the lowest numbers to double or triple bonds, then to all substituents together.\n\n3. Name each **branch or halogen** as a prefix with its number. Put the prefixes in **alphabetical order**. Ignore di-, tri-, tetra- when alphabetising.\n\n4. If a branch occurs more than once, use **di-, tri-, tetra-** and give every position: 2,2-dimethyl. Use commas between numbers and hyphens between numbers and letters.", title="The rules"),
        T("Branch (alkyl group) names come from the alkane stem: [[CH3]] is **methyl**, [[CH3CH2]] is **ethyl**, [[CH3CH2CH2]] is **propyl**. The group [[(CH3)2CH]] is **1-methylethyl** (often called isopropyl) and the benzene ring as a branch is **phenyl**."),
        H("Alkanes"),
        EX("Worked example 1: naming a branched alkane", intro="Name [[CH3CH2CH(CH3)CH2CH2CH3]].", steps=[
            S("Find the longest chain", text="Count the carbons in the main chain: 6. The parent is **hexane**. The [[CH3]] hanging off is a branch."),
            S("Number from the end that gives the branch the lower number", text="From the left the branch is on carbon 3; from the right it would be on carbon 4. Choose 3."),
            S("Assemble", text="One methyl on carbon 3, parent hexane: **3-methylhexane**."),
        ]),
        EX("Worked example 2: two branches", intro="Name [[CH3CH(CH3)CH(CH3)CH2CH3]].", steps=[
            S("Longest chain", text="The longest chain has 5 carbons: pentane. There are two methyl branches."),
            S("Number to give the lowest locants", text="Numbering from the left puts the branches on carbons 2 and 3 (set {2,3}). Numbering from the right gives {3,4}. {2,3} is lower."),
            S("Use di- and a comma", text="**2,3-dimethylpentane**."),
        ]),
        TIP("Rotate the molecule in your mind. The longest chain does not have to be a straight line on paper. Count the carbons along every route and take the longest."),
        H("Alkenes, alkynes and haloalkanes"),
        T("For alkenes and alkynes, the chain must **contain the double or triple bond**, and the number given is that of the **first** carbon of the bond. The bond gets the lowest number, even if a branch then gets a higher one."),
        EX("Worked example 3: alkene with a halogen", intro="Name [[CH2=CHCH(CH3)CH(CH3)Cl]].", steps=[
            S("Longest chain containing the C=C", text="Five carbons: pent-ene."),
            S("Number so that C=C gets the lowest number", text="Start at the [[CH2=]] end. The double bond is between carbons 1 and 2: **pent-1-ene**."),
            S("Find the branches", text="Methyl on carbon 3 and chlorine on carbon 4."),
            S("Alphabetical order", text="chloro comes before methyl: **4-chloro-3-methylpent-1-ene**."),
        ]),
        T("Examples for haloalkanes: [[CH3CHBrCH2CH3]] is **2-bromobutane**; [[(CH3)2CHCH2Br]] is **1-bromo-2-methylpropane**; [[BrCH2CHClCH3]] is **1-bromo-2-chloropropane** (b before c). Alkynes: [[CH3C#CCH2CH3]] is **pent-2-yne**; [[HC#CCH2CH3]] is **but-1-yne**."),
        H("Alcohols, carbonyl compounds and acids"),
        T("For an alcohol the -OH is the principal group: drop the final -e of the alkane and add **-ol** with a number: [[CH3CH2CH(OH)CH3]] is **butan-2-ol**. Two -OH groups: add **-diol** and keep the -e: [[HOCH2CH(OH)CH3]] is **propane-1,2-diol**. A branch on the carbon holding -OH: [[(CH3)3COH]] is **2-methylpropan-2-ol**."),
        T("Aldehydes end in **-al**. The C=O carbon is always carbon 1, so no number is needed: [[(CH3)2CHCH2CHO]] is **3-methylbutanal**. Ketones end in **-one** with a number once the chain is long enough to need it: [[CH3COCH2CH2CH3]] is **pentan-2-one**; [[CH3COCH3]] is **propanone** (the only place for C=O is carbon 2). Carboxylic acids end in **-oic acid** and the -COOH carbon is carbon 1: [[(CH3)2CHCOOH]] is **2-methylpropanoic acid**. Esters are named as an alkyl group first, then the acid part: [[CH3COOCH3]] is **methyl ethanoate**."),
        KEY("Which group wins the suffix?", "A molecule with two different groups is named from the **higher-priority** one. The other group becomes a prefix.", cards=[
            ["Order of priority", "carboxylic acid  >  aldehyde  >  ketone  >  alcohol  >  amine  >  alkene  >  halogen or alkyl (always prefix)"],
            ["Prefix names", "-OH as a prefix is **hydroxy-**, C=O inside the chain as a prefix is **oxo-**, -NH2 is **amino-**."],
        ]),
        EX("Worked example 4: two functional groups", intro="Name [[HOCH2CH(CH3)CH(Br)CH3]] and [[CH3CH(OH)CH2COOH]].", steps=[
            S("First compound: principal group is -OH", text="The chain has four carbons: butan-ol. Number from the -OH end: -OH on carbon 1."),
            S("Branches", text="Methyl on carbon 2, bromo on carbon 3. Alphabetical: bromo before methyl."),
            S("Result", text="**3-bromo-2-methylbutan-1-ol**."),
            S("Second compound: -COOH has higher priority than -OH", text="The acid is the parent: butanoic acid, with -COOH as carbon 1. The -OH is on carbon 3, so it becomes the prefix hydroxy."),
            S("Result", text="**3-hydroxybutanoic acid**."),
        ]),
        H("From a name back to a structure"),
        EX("Worked example 5: draw 2,2-dimethylbutane and but-3-en-2-ol", intro="Write the structural formula of each.", steps=[
            S("2,2-dimethylbutane", text="Draw a four-carbon chain (butane), put two methyl groups on carbon 2: [[CH3C(CH3)2CH2CH3]]. Check: six carbons altogether, formula [[C6H14]]."),
            S("but-3-en-2-ol", text="Four carbons, C=C starting at carbon 3 (between carbons 3 and 4), -OH on carbon 2: [[CH2=CHCH(OH)CH3]]. Formula [[C4H8O]]."),
        ]),
        H("Common mistakes"),
        MISTAKE("Taking the wrong chain", "Do not stop at the first straight line you see. The parent chain is the **longest** chain containing the principal group. Writing 2-ethylbutane is wrong; the compound is 3-methylpentane."),
        MISTAKE("Numbering from the wrong end", "The principal group (then double bond, then branches) decides the direction. In [[CH3CH2CH(CH3)CH2OH]] number from the -OH end: 2-methylbutan-1-ol, not 3-methylbutan-4-ol."),
        MISTAKE("Wrong alphabetical order or missing numbers", "Write 2-bromo-3-methylpentane, not 3-methyl-2-bromopentane. Write propan-2-ol, not propanol, when the position matters. Ignore di and tri when sorting: 3-ethyl-2,4-dimethylhexane puts ethyl before methyl."),
        QUIZ("What is the IUPAC name of [[CH3CH2CH(CH3)CH2Br]]?", ["2-methyl-1-bromobutane", "1-bromo-2-methylbutane", "2-bromo-3-methylbutane", "1-bromo-3-methylbutane"], 1,
             "The longest chain has four carbons (butane). Number from the end with Br: Br on carbon 1, methyl on carbon 2. Alphabetical order puts bromo before methyl: 1-bromo-2-methylbutane.",
             feedback=["The numbers are right but the prefixes are not alphabetical: bromo comes before methyl.", "", "The chain has been numbered from the wrong end and the structure does not fit; Br is on an end carbon.", "The methyl group is on carbon 2 of the chain, not carbon 3."]),
        QUIZ("Which compound is correctly named?", ["pent-3-ene (for [[CH3CH2CH=CHCH3]])", "2-hydroxypropanoic acid (for [[CH3CH(OH)COOH]])", "3-propanone (for [[CH3CH2COCH3]])", "1-methylpropane (for [[CH3CH2CH2CH3]])"], 1,
             "The acid group has higher priority than -OH, so -OH is the prefix hydroxy. -COOH is carbon 1, so -OH is on carbon 2. The other three names break the numbering or chain rules.",
             feedback=["The double bond must have the lowest number: pent-2-ene.", "", "The compound is butanone; the C=O is carbon 2 and the chain has four carbons.", "A straight four-carbon chain is just butane; there is no branch."]),
        H("Practice questions"),
        PQ("Name (a) [[CH3CH(CH3)CH2CH3]], (b) [[CH3CH2C(CH3)2CH3]] (c) [[(CH3)2C=CH2]].",
           "(a) 2-methylbutane (chain of four, methyl on carbon 2). (b) 2,2-dimethylbutane (longest chain four carbons, two methyl groups on carbon 2). (c) 2-methylpropene (chain of three, C=C starting at carbon 1, methyl on carbon 2; no number is needed for the double bond in propene)."),
        PQ("Give the IUPAC name of (a) [[CH3CH(OH)CH(CH3)2]] and (b) [[CH3CH2CH(CH3)CHO]].",
           "(a) The longest chain containing -OH has four carbons. Numbering from the -OH end gives butan-2-ol with a methyl on carbon 3: 3-methylbutan-2-ol. (b) The aldehyde carbon is carbon 1 in a four-carbon chain with a methyl on carbon 2: 2-methylbutanal."),
        PQ("Draw the structural formula of (a) 4-chloro-3-methylpent-1-ene and (b) 2-bromo-3-methylpentane and give the molecular formula of each.",
           "(a) [[CH2=CHCH(CH3)CH(Cl)CH3]], molecular formula [[C6H11Cl]]. (b) [[CH3CHBrCH(CH3)CH2CH3]], molecular formula [[C6H13Br]]."),
        PQ("Explain why [[CH3CH(OH)CH2COOH]] is named 3-hydroxybutanoic acid and not butan-3-ol-1-oic acid.",
           "The carboxylic acid group has higher priority than the alcohol group, so it provides the suffix (-oic acid) and its carbon is carbon 1. The lower-priority -OH group is shown as the prefix hydroxy- on carbon 3. Only one suffix is allowed in a name."),
        TIP("In the exam: naming is tested in Paper 1 multiple choice (pick the correct name or structure) and within Paper 2 organic questions, where a wrong name often loses a mark that a correct structure would have earned. Always give a number where the position could be in doubt."),
        H("Summary"),
        SUM("Name = prefixes (branches and halogens, alphabetical) + stem (longest chain) + suffix (principal functional group).",
            "Number the chain to give the lowest locant to the principal group, then the double or triple bond, then the substituents.",
            "Use di-, tri-, tetra- for repeated groups and list every position; ignore them when sorting alphabetically.",
            "Priority of groups: acid, aldehyde, ketone, alcohol, amine, alkene; halogens and alkyl groups are always prefixes.",
            "Check a name by drawing the structure back and counting carbons."),
    ])]
# ============================================================================================
# Topic 2. Structural isomerism and stereoisomerism (lesson 1 of 2)
# ============================================================================================
LESSONS += [lesson(
    module=M_ORG, topic="Structural isomerism and stereoisomerism",
    title="Structural isomerism: chain, position and functional-group isomers",
    slug="chl3-structural-isomerism", minutes=22,
    summary="Isomers share a molecular formula but differ in structure. Learn to find every chain, position and functional-group isomer systematically and explain how their properties differ.",
    objectives=[
        "Define isomerism and distinguish chain, position and functional-group isomers",
        "Find all structural isomers of a given formula by a systematic method without repeats",
        "Name each isomer by the IUPAC rules",
        "Explain why isomers differ in boiling point and reactivity",
    ],
    key_concepts=["Isomers", "Chain isomerism", "Position isomerism", "Functional-group isomerism", "Systematic enumeration"],
    blocks=[
        H("Introduction"),
        T("Two bottles on a pharmacy shelf can contain substances with the **same formula**, [[C2H6O]], and yet one is ethanol (a liquid used in drinks and sanitiser) and the other is methoxymethane (a gas). The atoms are the same; they are joined differently. This is **isomerism**, and it is one reason why the number of organic compounds is so large."),
        D("**Isomers** are compounds with the same molecular formula but different arrangements of atoms. **Structural isomers** have different structural formulae (the atoms are joined in a different order). **Stereoisomers** have the same structural formula but different arrangement of atoms in space (the next lesson).", title="Isomers"),
        H("Three kinds of structural isomerism"),
        KEY("Chain, position, functional group", "Structural isomers fall into three types, which often occur together in one set of isomers.", cards=[
            ["Chain isomers", "Different carbon skeleton: straight or branched. Butane and 2-methylpropane, both [[C4H10]]."],
            ["Position isomers", "Same skeleton and same functional group, but the group is in a different position. Propan-1-ol and propan-2-ol, both [[C3H8O]]."],
            ["Functional-group isomers", "Different functional groups. Ethanol [[CH3CH2OH]] (alcohol) and methoxymethane [[CH3OCH3]] (ether)."],
        ]),
        T("Pairs of functional-group isomers to remember: alcohols and ethers ([[!C_nH_{2n+2}O]]), aldehydes and ketones ([[!C_nH_{2n}O]]), carboxylic acids and esters ([[!C_nH_{2n}O_2]]), and alkenes and cycloalkanes ([[!C_nH_{2n}]])."),
        H("Finding isomers systematically"),
        T("The danger when drawing isomers is **missing some** or **counting one structure twice**. A fixed method prevents both."),
        D("1. Find the degree of unsaturation to see if rings or double bonds are needed.\n\n2. Draw the **longest straight chain** first.\n\n3. Shorten the main chain by one carbon and place that carbon as a branch on **every different position** (not on the end carbons, which just lengthens the chain).\n\n4. Shorten again and repeat. Check that no two drawings are the same by finding the longest chain of each and naming it.\n\n5. Add the functional group in every different position on each skeleton.", title="Method"),
        EX("Worked example 1: all isomers of [[C5H12]]", intro="Draw and name every structural isomer of [[C5H12]].", steps=[
            S("Saturated, no rings", text="The degree of unsaturation is 0, so the carbons form chains only."),
            S("Longest chain of five", text="[[CH3CH2CH2CH2CH3]] is **pentane**."),
            S("Longest chain of four, one methyl branch", text="A methyl on carbon 2 gives [[(CH3)2CHCH2CH3]], **2-methylbutane**. A methyl on carbon 3 gives the same molecule when numbered from the other end, so there is no new isomer."),
            S("Longest chain of three, two methyl branches", text="Both on carbon 2: [[(CH3)4C]], **2,2-dimethylpropane**."),
            S("Count", text="There are **3** isomers, shown in the figure below."),
        ]),
        IMG("al-chl3-c5h12-isomers.svg", alt="Skeletal formulae of pentane, 2-methylbutane and 2,2-dimethylpropane in three boxes.", caption="Figure 1. The three chain isomers of C5H12."),
        EX("Worked example 2: [[C4H10O]], alcohols and ethers", intro="Draw and name all structural isomers of [[C4H10O]] (no rings).", steps=[
            S("Alcohols from the straight chain, butane", text="-OH on carbon 1: **butan-1-ol**. -OH on carbon 2: **butan-2-ol**. (Carbon 3 repeats carbon 2 and carbon 4 repeats carbon 1.)"),
            S("Alcohols from the branched chain, methylpropane", text="-OH on an end carbon: **2-methylpropan-1-ol**. -OH on the middle carbon: **2-methylpropan-2-ol**."),
            S("Ethers: C-O-C with the two sides sharing four carbons", text="Methyl and propyl: **methoxypropane**. Ethyl and ethyl: **ethoxyethane**. Methyl and 1-methylethyl: **2-methoxypropane**."),
            S("Count", text="4 alcohols (position and chain isomers) plus 3 ethers (functional-group isomers) give **7** structural isomers."),
        ]),
        EX("Worked example 3: [[C4H8]]", intro="Find all structural isomers of [[C4H8]], and name them.", steps=[
            S("Degree of unsaturation", math=r"\dfrac{2(4) + 2 - 8}{2} = 1", text="One double bond **or** one ring."),
            S("Alkenes", text="Straight chain: **but-1-ene** and **but-2-ene**. Branched chain: **2-methylpropene**."),
            S("Cycloalkanes", text="A four-membered ring: **cyclobutane**. A three-membered ring with a methyl branch: **methylcyclopropane**."),
            S("Count", text="**5** structural isomers (cis and trans forms of but-2-ene are stereoisomers, counted in the next lesson)."),
        ]),
        H("How isomers differ in properties"),
        T("Isomers have the same relative molecular mass but different properties, because their shapes and functional groups differ."),
        T("**Chain isomers** have different boiling points. A branched molecule is more compact, so it has less surface area to make contact with its neighbours, and its instantaneous dipole-induced dipole forces are weaker. Approximate boiling points: pentane 36 °C, 2-methylbutane 28 °C, 2,2-dimethylpropane 10 °C (the more branched, the lower)."),
        T("**Functional-group isomers** differ in both physical and chemical properties. Ethanol (boiling point about 78 °C) forms hydrogen bonds between molecules; methoxymethane (about -24 °C) has no O-H group so it cannot. Ethanol reacts with sodium to give hydrogen; the ether does not."),
        H("Common mistakes"),
        MISTAKE("Counting a bent drawing as a new isomer", "A chain can be drawn as a zig-zag, bent or folded; the structure is the same. Two drawings are the same compound if they have the same longest chain and the same branches in the same positions. Always name each drawing to check."),
        MISTAKE("Forgetting the functional-group isomers", "For [[C4H10O]] students often give only the four alcohols. The three ethers must be included. Ask yourself: can the oxygen sit between two carbons?"),
        MISTAKE("Calling rotation about a single bond a new isomer", "A carbon-carbon single bond can rotate freely. The two ways of drawing a butane chain (zig-zag or bent) are the same molecule, not isomers."),
        QUIZ("How many structural isomers has [[C4H9Br]]?", ["2", "3", "4", "5"], 2,
             "Butane gives 1-bromobutane and 2-bromobutane. Methylpropane gives 1-bromo-2-methylpropane and 2-bromo-2-methylpropane. Total 4. (2-bromobutane also has optical isomers, but these are stereoisomers.)",
             feedback=["There are two skeletons, and each gives two position isomers.", "You may have missed one of the two methylpropane isomers.", "", "The fifth count would include the mirror-image form of 2-bromobutane, which is a stereoisomer, not a structural isomer."]),
        QUIZ("Which pair are **functional-group** isomers?", ["Butan-1-ol and butan-2-ol", "Butane and methylpropane", "Propanal and propanone", "Propan-1-ol and propanal"], 2,
             "Propanal [[CH3CH2CHO]] (aldehyde) and propanone [[CH3COCH3]] (ketone) both have the formula [[C3H6O]] but different functional groups.",
             feedback=["These are position isomers: the same functional group in different positions.", "These are chain isomers.", "", "These do not have the same molecular formula ([[C3H8O]] and [[C3H6O]])."]),
        H("Practice questions"),
        PQ("Draw and name all the structural isomers of [[C6H14]].",
           "There are 5: hexane [[CH3(CH2)4CH3]]; 2-methylpentane [[(CH3)2CHCH2CH2CH3]]; 3-methylpentane [[CH3CH2CH(CH3)CH2CH3]]; 2,2-dimethylbutane [[(CH3)3CCH2CH3]]; 2,3-dimethylbutane [[(CH3)2CHCH(CH3)2]]. (A methyl group on carbon 1 or 5 of pentane only lengthens the chain, so it gives hexane.)"),
        PQ("(a) Give the structural formulae and names of the three isomers of [[C3H8O]]. (b) State which type of isomerism relates propan-1-ol and propan-2-ol, and which relates propan-1-ol and methoxyethane.",
           "(a) Propan-1-ol [[CH3CH2CH2OH]]; propan-2-ol [[CH3CH(OH)CH3]]; methoxyethane [[CH3OCH2CH3]]. (b) Propan-1-ol and propan-2-ol are position isomers (the same group in different positions). Propan-1-ol and methoxyethane are functional-group isomers (alcohol and ether)."),
        PQ("Explain why 2,2-dimethylpropane has a lower boiling point than pentane although both have the formula [[C5H12]].",
           "Both are non-polar molecules held together only by instantaneous dipole-induced dipole forces. Pentane is a long, thin molecule that can make contact with neighbours along its whole length. 2,2-Dimethylpropane is compact and almost spherical, so it has a smaller surface area in contact with other molecules, the forces between molecules are weaker and less energy is needed to separate them. So its boiling point (about 10 °C) is lower than that of pentane (about 36 °C)."),
        PQ("An organic compound has the molecular formula [[C3H6O]] and contains a C=O group. Draw both possible structures, name them and say what type of isomers they are.",
           "Propanal [[CH3CH2CHO]] (the C=O is at the end of the chain with an H) and propanone [[CH3COCH3]] (the C=O is inside the chain). They are functional-group isomers: an aldehyde and a ketone."),
        TIP("In the exam: structural isomers appear in Paper 1 (count the isomers, identify an isomer) and in Paper 2 organic questions (for example, naming and drawing the isomers of a formula such as [[C3H8O]] and then using test results to decide which isomer is present)."),
        H("Summary"),
        SUM("Isomers have the same molecular formula but different structures.",
            "Chain isomers differ in the carbon skeleton, position isomers in the position of the group, functional-group isomers in the group itself.",
            "Enumerate systematically: longest chain first, then shorter chains with branches, then place groups on each different carbon; name each to avoid repeats.",
            "Counts: [[C5H12]] 3, [[C6H14]] 5, [[C4H9Br]] 4, [[C4H10O]] 7, [[C4H8]] 5 (all structural).",
            "Branching lowers boiling point; functional-group isomers have different physical and chemical properties."),
    ])]
# ============================================================================================
# Topic 2. Structural isomerism and stereoisomerism (lesson 2 of 2)
# ============================================================================================
LESSONS += [lesson(
    module=M_ORG, topic="Structural isomerism and stereoisomerism",
    title="Stereoisomerism: geometric (E/Z) and optical isomerism",
    slug="chl3-stereoisomerism", minutes=25,
    summary="Stereoisomers have the same structural formula but a different arrangement in space: cis-trans (E/Z) isomers about a C=C bond, and optical isomers (enantiomers) with a chiral centre.",
    objectives=[
        "Explain why geometric isomerism occurs and decide whether a compound shows it",
        "Assign E or Z using the Cahn-Ingold-Prelog priority rules",
        "Identify a chiral centre and draw the two enantiomers using wedge and dash bonds",
        "Describe optical activity, a racemic mixture and how a racemate can be resolved",
    ],
    key_concepts=["Geometric isomerism", "E/Z notation", "Chiral centre", "Enantiomers", "Optical activity", "Racemic mixture", "Resolution"],
    blocks=[
        H("Introduction"),
        T("When milk turns sour in a warm kitchen, bacteria make lactic acid. The same acid builds up in tired muscles after a football match. The lactic acid in muscle is one of **two mirror-image forms** of the molecule. The two forms have the same formula and the same bonds, yet they are different compounds, and living cells can tell them apart."),
        T("This is **stereoisomerism**. Here you learn the two types you need at A Level: geometric isomerism and optical isomerism."),
        D("**Stereoisomers** have the same molecular formula and the same structural formula (the atoms are joined in the same order) but a different arrangement of the atoms in space.", title="Stereoisomers"),
        H("Geometric isomerism (cis-trans, E/Z)"),
        T("A carbon-carbon **single** bond can rotate freely. A carbon-carbon **double** bond cannot, because the sideways overlap of the p orbitals (the pi bond) would have to be broken to rotate it. The groups on each carbon are therefore **locked** on one side or the other of the double bond."),
        D("A compound shows geometric isomerism if (1) it has a C=C bond (or a ring) that prevents rotation, and (2) **each carbon** of the double bond carries **two different groups**.", title="Condition for geometric isomerism"),
        T("But-2-ene [[CH3CH=CHCH3]] qualifies: each double-bond carbon has a [[CH3]] and an H. But-1-ene [[CH2=CHCH2CH3]] does not: one carbon has two H atoms. 2-Methylbut-2-ene does not: one carbon has two [[CH3]] groups."),
        D("In the **cis** isomer the two similar groups are on the **same side** of the double bond; in the **trans** isomer they are on **opposite sides**. For more complex alkenes, cis and trans are unclear, so chemists use **E/Z**. On each carbon, rank the two groups by **priority**: the group whose first atom has the **higher atomic number** is higher (if the first atoms are the same, compare the next atoms). **Z** (German *zusammen*, together) means the two higher-priority groups are on the same side; **E** (*entgegen*, opposite) means they are on opposite sides.", title="Cis, trans, E and Z"),
        IMG("al-chl3-ez-but2ene.svg", alt="Two drawings of but-2-ene. In the Z isomer both CH3 groups are above the double bond; in the E isomer one CH3 is above and one below.", caption="Figure 1. (Z)- and (E)-but-2-ene. In but-2-ene, cis is the same as Z and trans is the same as E."),
        EX("Worked example 1: does it show geometric isomerism?", intro="State which of these show geometric isomerism and give E/Z labels where they do: (a) pent-2-ene, (b) 2-methylbut-2-ene, (c) 1-bromo-2-chloroethene, (d) 3-methylpent-2-ene.", steps=[
            S("(a) Pent-2-ene [[CH3CH=CHCH2CH3]]", text="Each carbon of C=C has two different groups (CH3 and H; C2H5 and H). **Yes**: the isomers are (Z)-pent-2-ene (cis) and (E)-pent-2-ene (trans)."),
            S("(b) 2-Methylbut-2-ene [[(CH3)2C=CHCH3]]", text="One carbon has two identical methyl groups. **No**."),
            S("(c) 1-Bromo-2-chloroethene [[BrCH=CHCl]]", text="Each carbon has H and a halogen. Br outranks H and Cl outranks H. If Br and Cl are on the same side the isomer is **(Z)**; if on opposite sides, **(E)**."),
            S("(d) 3-Methylpent-2-ene [[CH3CH=C(CH3)CH2CH3]]", text="One carbon has CH3 and H (CH3 is higher). The other has CH3 and [[CH2CH3]]: ethyl is higher (the first atom is carbon in both groups, so compare the atoms attached to it: CH3 carries H, H, H but CH2CH3 carries C, H, H). If the ethyl group and the CH3 on the other carbon are on the same side the isomer is **(Z)**; if opposite, **(E)**. Cis/trans would be ambiguous here, which is why E/Z is used."),
        ]),
        T("Geometric isomers differ in physical properties (boiling point, melting point, polarity) and sometimes in chemical reactivity. For example, cis-but-2-ene has a small overall dipole moment because its two C-CH3 bond dipoles partly add, while trans-but-2-ene has almost none, since the dipoles cancel."),
        H("Optical isomerism"),
        D("A **chiral centre** (asymmetric carbon) is a carbon atom bonded to **four different** atoms or groups. A molecule with one chiral centre exists as two forms that are **non-superimposable mirror images** of each other. These two forms are called **enantiomers** or **optical isomers**.", title="Chiral centre and enantiomers"),
        T("Think of your left and right hands: they are mirror images, but you cannot place one exactly on top of the other. Molecules with a chiral centre behave in the same way."),
        T("Examples: butan-2-ol [[CH3CH(OH)CH2CH3]] (the second carbon holds H, OH, [[CH3]] and [[CH2CH3]]), 2-hydroxypropanoic acid (lactic acid) [[CH3CH(OH)COOH]] and the amino acid alanine [[CH3CH(NH2)COOH]]. Butan-1-ol and propan-2-ol have **no** chiral centre: in propan-2-ol the central carbon holds two [[CH3]] groups."),
        H("Drawing enantiomers"),
        T("Draw the chiral carbon with two bonds in the plane of the paper, one **wedge** bond (a thick triangle) coming towards you and one **dashed** bond going away. The second enantiomer is the **mirror image** of the first: swap the wedge and dash positions, or reflect the drawing left to right."),
        IMG("al-chl3-enantiomers-alanine.svg", alt="Two drawings of alanine that are mirror images: the left has NH2 on the left, CH3 on a wedge and H on a dash; the right is the reflection.", caption="Figure 2. The enantiomers of alanine, (R) and (S), as mirror images."),
        EX("Worked example 2: identify the chiral centre and draw the enantiomers", intro="Show that 2-bromobutane [[CH3CHBrCH2CH3]] is chiral and draw both enantiomers.", steps=[
            S("Look for a carbon with four different groups", text="Carbon 2 holds H, Br, [[CH3]] and [[CH2CH3]]. All four are different, so it is a chiral centre."),
            S("Draw the first enantiomer", text="Put C2 in the centre. Draw [[CH3]] and [[CH2CH3]] in the plane, Br on a wedge and H on a dash."),
            S("Draw the second enantiomer", text="Keep the same two in-plane groups but swap Br and H (Br on the dash, H on the wedge). The result is the mirror image and cannot be superimposed on the first."),
            S("State the consequence", text="2-Bromobutane exists as a pair of enantiomers. Together with its three structural isomers, [[C4H9Br]] has **5** stereoisomers in total."),
        ]),
        H("Optical activity and racemic mixtures"),
        T("Enantiomers have identical melting points, boiling points, solubilities and chemical reactions with ordinary reagents. They differ in two ways. First, they **rotate the plane of plane-polarised light** in opposite directions by equal amounts. A **polarimeter** measures this. The enantiomer that rotates it clockwise is labelled (+) (dextrorotatory), the other (−) (laevorotatory). Second, they react differently with other chiral molecules, such as the enzymes in your body."),
        D("A **racemic mixture** (racemate) contains **equal amounts** of two enantiomers. The rotations cancel, so a racemic mixture shows **no net optical activity**.", title="Racemic mixture"),
        T("A reaction that makes a chiral centre from non-chiral reactants, such as the addition of HCN to propanal, produces a racemic mixture because the attacking group can approach from either side of the flat molecule with equal probability. In the laboratory, enantiomers made in the usual way are mixed 50:50; living cells make only one."),
        D("**Resolution** is the separation of a racemic mixture into its enantiomers. One method: react the racemate with a single pure enantiomer of another chiral compound. This gives two products (diastereoisomers) that are **not** mirror images and so have **different** physical properties, for example solubility. They can be separated by crystallisation, and each is then converted back to the pure enantiomer.", title="Resolution of a racemic mixture"),
        KEY("R and S labels (check your textbook)", "Many textbooks also label each chiral centre R or S using the same priority rules as E/Z.", cards=[
            ["Rank the four groups", "Highest priority = highest atomic number of the atom attached to the chiral centre. In alanine: NH2 (1), COOH (2), CH3 (3), H (4)."],
            ["Look from the side opposite the lowest priority", "H points away from you. If 1 to 2 to 3 runs **clockwise** the centre is **R**; **anticlockwise** is **S**. The alanine in proteins is (S)."],
        ]),
        H("How many stereoisomers?"),
        T("A molecule with **n** chiral centres can have up to $2^n$ stereoisomers. 2,3-Dibromopentane [[CH3CHBrCHBrCH2CH3]] has two chiral centres and four stereoisomers. If a molecule has two similar chiral centres, as in 2,3-dibromobutane, a form with an internal mirror plane (a *meso* compound) can occur and the total is lower (3 here). A molecule can have both kinds: [[CH3CHBrCH2CH=CHCH3]] has one chiral centre and one C=C that can be E or Z, so it has 4 stereoisomers."),
        H("Common mistakes"),
        MISTAKE("Forgetting that hydrogen counts as a group", "In but-1-ene the carbon with two H atoms has two identical groups. Always write in the H atoms, so you see that each carbon needs two **different** groups."),
        MISTAKE("Assuming cis means Z for every compound", "Cis/trans refers to the same group on both carbons. E/Z uses priority. They match for but-2-ene but not always. Use CIP priority for E/Z."),
        MISTAKE("Saying a molecule is chiral because it has four groups", "The four groups on the carbon must all be **different**. If two are the same (two CH3 groups, two H atoms) the carbon is not a chiral centre."),
        MISTAKE("Saying a racemic mixture is a pure compound with no optical activity", "It is a 50:50 mixture of two optically active enantiomers whose effects cancel."),
        QUIZ("Which compound shows geometric isomerism?", ["But-1-ene", "2-Methylbut-2-ene", "Pent-2-ene", "Propene"], 2,
             "Pent-2-ene has two different groups on each carbon of the C=C (CH3 and H on one; [[CH2CH3]] and H on the other).",
             feedback=["One carbon of the C=C carries two H atoms.", "One carbon of the C=C carries two identical [[CH3]] groups.", "", "One carbon of the C=C carries two H atoms."]),
        QUIZ("Which compound has a chiral centre?", ["Propan-2-ol", "Butan-1-ol", "Butan-2-ol", "2-Methylpropan-2-ol"], 2,
             "In butan-2-ol the second carbon holds H, OH, [[CH3]] and [[CH2CH3]]: four different groups.",
             feedback=["The central carbon holds two [[CH3]] groups.", "Carbon 1 has two H atoms and no carbon has four different groups.", "", "The carbon with OH holds three identical [[CH3]] groups."]),
        H("Practice questions"),
        PQ("Draw the structures of (Z)- and (E)-1-bromo-2-chloroethene and say which has the larger dipole moment. Give a reason.",
           "(Z): Br and Cl on the same side of C=C; (E): on opposite sides. The (Z) isomer has the larger dipole moment because the C-Br and C-Cl bond dipoles point to the same side and partly add; in the (E) isomer they point in roughly opposite directions and partly cancel."),
        PQ("(a) Explain why geometric isomerism is possible in but-2-ene but not in but-1-ene. (b) Name the two isomers of but-2-ene.",
           "(a) Rotation about C=C is not possible because the pi bond would have to break. In but-2-ene each double-bond carbon has two different groups (CH3 and H), so the two arrangements differ. In but-1-ene the carbon C1 has two H atoms, so swapping them gives the same molecule. (b) (Z)-but-2-ene (cis) and (E)-but-2-ene (trans)."),
        PQ("2-Hydroxypropanoic acid [[CH3CH(OH)COOH]] is chiral. (a) Mark the chiral centre. (b) Explain why the two enantiomers have the same melting point but a mixture of equal amounts does not rotate plane-polarised light.",
           "(a) The central carbon (C2) is bonded to H, OH, [[CH3]] and [[COOH]]. (b) Enantiomers have the same bonds and the same intermolecular forces, so the same melting point. Each rotates plane-polarised light by the same angle but in opposite directions; in an equal mixture the rotations cancel, so there is no net rotation."),
        PQ("The addition of HCN to propanal [[CH3CH2CHO]] gives [[CH3CH2CH(OH)CN]]. Explain why the product shows no optical activity although it has a chiral centre.",
           "The C=O carbon in propanal is flat (trigonal planar). The cyanide ion can attack from either face with equal probability, giving the two enantiomers in equal numbers. The product is a racemic mixture: the optical activity of one enantiomer is cancelled by the other."),
        TIP("In the exam: geometric and optical isomerism are common in Paper 1 (identify isomers, count stereoisomers, choose a chiral compound) and in Paper 2 organic questions, which can ask you to draw the optical isomers of an amino acid with wedge and dash bonds. Show all four groups on the chiral centre clearly."),
        H("Summary"),
        SUM("Stereoisomers share a structural formula but differ in arrangement in space.",
            "Geometric isomerism needs a C=C (restricted rotation) and two different groups on each carbon; Z means the higher-priority groups are on the same side, E on opposite sides.",
            "A chiral centre is a carbon with four different groups; its two non-superimposable mirror images are enantiomers.",
            "Enantiomers rotate plane-polarised light in opposite directions; a racemic mixture (1:1) is optically inactive.",
            "A racemate can be resolved by reacting it with a pure enantiomer to make separable diastereoisomers; a molecule with n chiral centres has at most $2^n$ stereoisomers."),
    ])]
# ============================================================================================
# Topic 3. Reaction mechanisms (1 lesson)
# ============================================================================================
LESSONS += [lesson(
    module=M_ORG, topic="Reaction mechanisms",
    title="Electron effects, bond fission and curly arrows: nucleophiles, electrophiles and radicals",
    slug="chl3-electron-effects-bond-fission-curly-arrows", minutes=25,
    summary="A mechanism shows how bonds break and form. Learn homolytic and heterolytic fission, nucleophiles, electrophiles and radicals, inductive and mesomeric effects, and how to draw curly arrows correctly.",
    objectives=[
        "Distinguish homolytic from heterolytic fission and name the species formed",
        "Define nucleophile, electrophile and free radical and classify common examples",
        "Explain the inductive and mesomeric effects and use them to compare stabilities",
        "Draw curly arrows that start from a lone pair or bond and end at an atom or new bond",
    ],
    key_concepts=["Homolytic fission", "Heterolytic fission", "Free radical", "Nucleophile", "Electrophile", "Inductive effect", "Mesomeric effect", "Curly arrow"],
    blocks=[
        H("Introduction"),
        T("A roadside mechanic in Bafoussam can tell you that petrol burns and the engine runs, but a chemist asks a different question: **how**? Which bonds break first, which form next, and in what order? The step-by-step account of a reaction is its **mechanism**. Mechanisms let you predict products, explain why reaction conditions matter, and answer exam questions on reactions you have never seen."),
        H("Types of organic reaction"),
        CODE("""Type            What happens                          Example
substitution    one atom or group replaced by another CH3CH2Br + OH-  ->  CH3CH2OH + Br-
addition        two molecules join to one product     CH2=CH2 + HBr  ->  CH3CH2Br
elimination     a small molecule is removed,          CH3CH2Br  ->  CH2=CH2 + HBr
                a double bond forms
oxidation       O added or H removed (or electrons    CH3CH2OH  ->  CH3CHO (with [O])
                lost)
hydrolysis      reaction with water (or aqueous       CH3CH2Br + H2O -> CH3CH2OH + HBr
                alkali) that splits a molecule""", "text", title="Main types of reaction"),
        H("How a covalent bond can break"),
        D("In **homolytic fission** a covalent bond breaks so that **each** atom takes **one** of the two shared electrons. The products are **free radicals**: atoms or groups with an unpaired electron. It needs energy such as ultraviolet light or high temperature and is typical of non-polar bonds, such as Cl-Cl.", title="Homolytic fission"),
        D("In **heterolytic fission** the bond breaks so that **both** shared electrons go to **one** atom, the more electronegative one. The products are **ions**: a positive ion (such as a **carbocation**, a carbon with a positive charge and only six electrons) and a negative ion. It is typical of polar bonds such as C-Br, usually in a solvent.", title="Heterolytic fission"),
        IMG("al-chl3-bond-fission.svg", alt="Two panels: homolytic fission of Cl-Cl into two chlorine radicals with half-headed arrows, and heterolytic fission of CH3-Br into CH3+ and Br- with a full-headed arrow.", caption="Figure 1. Homolytic fission (fish-hook arrows) and heterolytic fission (full-headed curly arrow)."),
        H("Radicals, nucleophiles and electrophiles"),
        KEY("Three kinds of attacking species", "The type of species decides which reactions can occur.", cards=[
            ["Free radical", "Has an unpaired electron: Cl•, •CH3. Very reactive. Attacks non-polar bonds such as C-H in alkanes."],
            ["Nucleophile", "A species that **donates a pair of electrons** to form a bond. It is attracted to positive centres (a carbon with δ+). Examples: OH⁻, CN⁻, NH3, H2O, Br⁻."],
            ["Electrophile", "A species that **accepts a pair of electrons** to form a bond. It is attracted to electron-rich centres (a C=C bond). Examples: H⁺, NO2⁺, Br2 (polarised), carbocations."],
        ]),
        T("Nucleophiles have a **lone pair** of electrons (or a negative charge). Electrophiles have a **positive or partial positive charge**, or an empty orbital. A useful memory: a nucleophile is *nucleus-loving*, an electrophile is *electron-loving*."),
        H("Showing movement of electrons: curly arrows"),
        D("A **curly arrow** shows the movement of an electron pair. It starts at a lone pair or at the middle of a bond (where the electrons are) and finishes at an atom (forming a lone pair) or between two atoms (forming a new bond). A **half-headed** (fish-hook) arrow shows the movement of a **single** electron and is used for radical reactions.", title="Rules for curly arrows"),
        T("Check three things after you draw the arrows. First, the arrow begins at electrons, never at an atom with no electrons shown. Second, the charges balance: the total charge before the arrow equals the total after. Third, no atom ends with too many bonds (carbon never has five)."),
        EX("Worked example 1: classify the species", intro="Classify each as a nucleophile, an electrophile or a free radical: [[OH^-]], [[NH3]], [[H^+]], [[NO2^+]], [[Cl.]], [[CN^-]], [[(CH3)3C^+]].", steps=[
            S("Species with a lone pair or negative charge", text="[[OH^-]], [[NH3]], [[CN^-]] are **nucleophiles** (each can donate an electron pair)."),
            S("Species with a positive charge or empty orbital", text="[[H^+]], [[NO2^+]], [[(CH3)3C^+]] are **electrophiles** (each can accept an electron pair)."),
            S("Species with an unpaired electron", text="[[Cl.]] is a **free radical**."),
        ]),
        EX("Worked example 2: describe a heterolytic fission with curly arrows", intro="The C-Br bond in 2-bromo-2-methylpropane breaks heterolytically. Show it with a curly arrow and name the products.", steps=[
            S("Polarity", text="Br is more electronegative than C, so the bond is polar: carbon δ+, bromine δ−."),
            S("Draw the arrow", text="Start the curly arrow at the middle of the C-Br bond and finish it on the bromine atom, because the bond pair goes to Br."),
            S("Write the products", text="The carbon is left with only three bonds and a positive charge, the carbocation [[(CH3)3C^+]]. Bromine becomes the bromide ion [[Br^-]] with four lone pairs."),
            S("Check the charges", math=r"0 \;\rightarrow\; (+1) + (-1) = 0", text="Charge is conserved."),
        ]),
        H("The inductive effect"),
        D("The **inductive effect** is the permanent shift of electron density along a **sigma** bond caused by a difference in electronegativity. A group that pulls electron density towards itself (more electronegative than hydrogen, such as -Cl, -F, -OH, -NO2) has a **−I** (electron-withdrawing) effect. Alkyl groups push electron density away from themselves and have a **+I** (electron-releasing) effect.", title="Inductive effect"),
        T("The effect passes along the chain but **weakens quickly** with distance, becoming small after about two or three bonds."),
        T("**Consequence 1: stability of carbocations.** Alkyl groups release electrons towards the positive carbon and spread its charge. The more alkyl groups, the more stable the ion: tertiary > secondary > primary > methyl. A simple order to remember is [[(CH3)3C^+]] > [[(CH3)2CH^+]] > [[CH3CH2^+]] > [[CH3^+]]. This explains why electrophilic addition follows Markovnikov's rule and why tertiary haloalkanes react by the SN1 route (next lessons)."),
        T("**Consequence 2: acid strength.** Chlorine withdraws electrons, spreads the negative charge on the carboxylate ion and stabilises it. So the acids get stronger as chlorine atoms are added. Approximate pKa values: ethanoic acid 4.8, chloroethanoic acid 2.9, dichloroethanoic acid 1.3, trichloroethanoic acid 0.7 (a lower pKa is a stronger acid)."),
        H("The mesomeric effect (delocalisation)"),
        D("The **mesomeric effect** (resonance) is the delocalisation of **pi electrons or lone pairs** over several atoms. It is shown by drawing two or more structures (resonance forms) joined by a double-headed arrow. The real molecule is a **hybrid** of these forms, **not** a rapid flip between them; it is more stable than any single drawing suggests. Groups that donate a lone pair into a pi system (-OH, -NH2) show **+M**; groups that withdraw electrons from it (C=O, -NO2, -CN) show **−M**.", title="Mesomeric effect"),
        CODE("""Resonance form 1:   CH3-C(=O)-O(-)     the charge is on the single-bonded O
        <---->     (double-headed arrow)
Resonance form 2:   CH3-C(-O(-))=O     the charge is on the other O

Real ion: one hybrid. Both C-O bonds have the same length (between a C=O
and a C-O bond) and the negative charge is shared equally by the two O atoms.""", "text", title="Delocalisation in the ethanoate ion"),
        T("In the ethanoate ion the charge is spread over two oxygen atoms, so the ion is stable. In the ethoxide ion [[CH3CH2O^-]] the charge sits on **one** oxygen atom. This is why ethanoic acid (a carboxylic acid) is a much stronger acid than ethanol. Benzene is another example: its six carbon-carbon bonds are all the same length (about 140 pm, between a C-C bond at 154 pm and a C=C bond at 134 pm) because the pi electrons are delocalised over the whole ring."),
        EX("Worked example 3: use electron effects to compare", intro="(a) Which carbocation is more stable, [[(CH3)2CH^+]] or [[CH3CH2CH2^+]]? (b) Which is the stronger acid, [[CH3COOH]] or [[CH2FCOOH]]?", steps=[
            S("(a) Count alkyl groups on the positive carbon", text="[[(CH3)2CH^+]] is secondary (two alkyl groups); [[CH3CH2CH2^+]] is primary (one). More +I donation stabilises the ion, so the **secondary** carbocation is more stable."),
            S("(b) Look for electron-withdrawing groups", text="Fluorine is highly electronegative and has a −I effect, which stabilises the anion [[CH2FCOO^-]] by spreading its charge. So **fluoroethanoic acid** is the stronger acid."),
        ]),
        H("Common mistakes"),
        MISTAKE("Curly arrows that start in the wrong place", "The tail of the arrow must start at a lone pair or at a bond, because that is where the electron pair is. An arrow starting at a positive charge or at an atom with no electrons is wrong. The head goes where the pair ends up."),
        MISTAKE("Mixing up nucleophile and electrophile", "Nucleophiles **donate** an electron pair (they are electron-rich, often negative); electrophiles **accept** one (electron-poor, often positive). A negative ion attacks a δ+ carbon."),
        MISTAKE("Using a full-headed arrow for one electron", "A full-headed arrow means a **pair** of electrons. Radical steps use half-headed arrows. Do not mix them."),
        MISTAKE("Thinking resonance forms are different molecules", "Resonance forms are not isomers and the molecule does not flip between them. There is one species: the hybrid. Draw a double-headed arrow between the forms, never an equilibrium arrow."),
        QUIZ("Heterolytic fission of the C-Cl bond in [[CH3Cl]] gives", ["two free radicals", "[[CH3^+]] and [[Cl^-]]", "[[CH3^-]] and [[Cl^+]]", "[[CH2]] and HCl"], 1,
             "Chlorine is more electronegative than carbon, so it takes both electrons of the bond. The products are [[CH3^+]] (carbocation) and [[Cl^-]].",
             feedback=["Two radicals come from homolytic fission, where each atom keeps one electron.", "", "That would give chlorine a positive charge. The more electronegative atom takes the electron pair, becoming negative.", "That is a different (elimination) reaction."]),
        QUIZ("Which of these is a nucleophile?", ["[[BF3]]", "[[H^+]]", "[[NH3]]", "[[Cl.]]"], 2,
             "Ammonia has a lone pair on nitrogen which it can donate to a positive centre.",
             feedback=["[[BF3]] has an empty orbital on boron and accepts an electron pair: an electrophile.", "[[H^+]] has no electrons and accepts a pair: an electrophile.", "", "[[Cl.]] has one unpaired electron: it is a free radical."]),
        H("Practice questions"),
        PQ("Define (a) a nucleophile, (b) an electrophile and give one example of each.",
           "(a) A nucleophile is a species that donates a lone pair of electrons to form a covalent bond, for example [[OH^-]] or [[CN^-]]. (b) An electrophile is a species that accepts a pair of electrons to form a covalent bond, for example [[H^+]] or [[NO2^+]]."),
        PQ("Explain, with reference to the inductive effect, why the tertiary carbocation [[(CH3)3C^+]] is more stable than the primary carbocation [[CH3CH2^+]].",
           "Alkyl groups have a +I effect: they push electron density towards the carbon carrying the positive charge. The tertiary carbocation has three alkyl groups, so more electron density flows onto the positive carbon and its charge is spread over more atoms. The primary carbocation has only one alkyl group, so it is less stabilised. Stability: tertiary > secondary > primary."),
        PQ("Explain why trichloroethanoic acid ([[CCl3COOH]], pKa about 0.7) is a much stronger acid than ethanoic acid (pKa about 4.8).",
           "Each chlorine atom is more electronegative than hydrogen and withdraws electron density (a −I effect). The three Cl atoms pull electrons away from the carboxylate group, which spreads the negative charge of [[CCl3COO^-]] and stabilises it. A more stable anion means the acid dissociates more and is stronger. In ethanoate, the methyl group has a small +I effect, which slightly destabilises the anion."),
        PQ("Draw the two resonance forms of the ethanoate ion and explain why both C-O bond lengths in the ion are equal.",
           "Form 1: CH3-C(=O)-O⁻ with the negative charge on the single-bonded oxygen. Form 2: CH3-C(-O⁻)=O with the charge on the other oxygen. The two forms are linked by a double-headed arrow. The real ion is a hybrid: the pi electrons and the negative charge are delocalised over both oxygen atoms and the carbon, so both C-O bonds have the same intermediate length and the same bond strength."),
        TIP("In the exam: curly arrows and definitions of nucleophile and electrophile are marked in Paper 2 organic questions, including the mechanism for alkaline hydrolysis of a haloalkane. In Paper 1, expect multiple-choice questions on stability of intermediates and on the type of bond fission."),
        H("Summary"),
        SUM("Homolytic fission gives two radicals (one electron each); heterolytic fission gives ions (both electrons to the more electronegative atom).",
            "A nucleophile donates an electron pair; an electrophile accepts one; a free radical has an unpaired electron.",
            "A full curly arrow starts at a lone pair or bond and shows an electron pair moving; a half-headed arrow shows one electron.",
            "The inductive effect is a permanent polarisation along sigma bonds: alkyl groups are +I, electronegative groups are −I. It stabilises carbocations (tertiary > secondary > primary) and affects acid strength.",
            "The mesomeric effect is delocalisation of pi electrons or lone pairs; the hybrid is more stable than any one resonance form."),
    ])]
# ============================================================================================
# Topic 4. Alkanes and alkenes (1 lesson)
# ============================================================================================
LESSONS += [lesson(
    module=M_ORG, topic="Alkanes and alkenes",
    title="Alkanes and alkenes: free-radical substitution, cracking and electrophilic addition",
    slug="chl3-alkanes-and-alkenes", minutes=26,
    summary="Alkanes burn, are cracked and react with halogens by a free-radical chain; alkenes are more reactive because of the C=C bond and undergo electrophilic addition that follows Markovnikov's rule.",
    objectives=[
        "Describe the combustion, free-radical substitution and cracking of alkanes",
        "Write the initiation, propagation and termination steps of the chlorination of methane",
        "Describe the electrophilic addition of H2, Br2, HBr and H2O to alkenes, with mechanism and Markovnikov's rule",
        "Describe tests for unsaturation and oxidative cleavage of alkenes by ozone",
    ],
    key_concepts=["Free-radical substitution", "Chain reaction", "Cracking", "Electrophilic addition", "Markovnikov's rule", "Bromine water test", "Ozonolysis"],
    blocks=[
        H("Introduction"),
        T("Bottled gas in a kitchen, petrol in a taxi and diesel in a bus are mixtures of **alkanes** from crude oil. When refineries heat the heavy fractions with a catalyst, large molecules split into smaller, more useful ones, and **alkenes** such as ethene are among the products. Ethene is the raw material for poly(ethene), used in the plastic bags and water pipes you see everywhere."),
        T("Alkanes are often unreactive, while alkenes react easily. The reason is in the bonds, and the same idea explains their mechanisms."),
        H("Alkanes: structure and reactivity"),
        T("Alkanes have the general formula [[!C_nH_{2n+2}]]. All their bonds are sigma bonds: C-C (about 347 kJ/mol) and C-H (about 413 kJ/mol). These bonds are **strong** and almost **non-polar**, because carbon and hydrogen have similar electronegativity. So alkanes are not attacked by nucleophiles or electrophiles, and they do not react with acids, alkalis or oxidising agents at room temperature. They react in two ways: they **burn**, and they react with halogens when radicals are produced."),
        T("**Combustion.** In a plentiful supply of air alkanes burn completely: [[C3H8 + 5O2 -> 3CO2 + 4H2O]]. In a limited supply (a gas stove in a closed room, charcoal burning without ventilation), carbon monoxide forms: [[2CH4 + 3O2 -> 2CO + 4H2O]]. Carbon monoxide is poisonous because it binds to haemoglobin, so never use a stove in a closed room."),
        H("Free-radical substitution of alkanes"),
        T("Methane and chlorine do not react in the dark. In sunlight or ultraviolet (UV) light they react: [[CH4 + Cl2 -> CH3Cl + HCl]]. The reaction goes by a **chain reaction** with three stages."),
        CODE("""Initiation      Cl2  ->  2Cl.                  (UV light, homolytic fission)

Propagation     CH4 + Cl.  ->  .CH3 + HCl      (a radical is used and
                .CH3 + Cl2 ->  CH3Cl + Cl.      another is made: the chain continues)

Termination     Cl. + Cl.   ->  Cl2            (two radicals join:
                .CH3 + Cl.  ->  CH3Cl           the chain stops)
                .CH3 + .CH3 ->  C2H6""", "text", title="Free-radical chain: chlorination of methane"),
        T("In the propagation steps, a chlorine radical removes a hydrogen atom from methane, giving a methyl radical; the methyl radical then reacts with a chlorine molecule, giving chloromethane and **regenerating** a chlorine radical. One chlorine radical can therefore cause thousands of reactions. Termination steps remove radicals. Because the product still has C-H bonds, further substitution gives a **mixture**: [[CH3Cl]], [[CH2Cl2]], [[CHCl3]] and [[CCl4]]. Using a large excess of methane favours [[CH3Cl]]. Bromine reacts in the same way, but more slowly."),
        H("Cracking"),
        D("**Cracking** is the breaking of long-chain alkanes into shorter alkanes and alkenes (and sometimes hydrogen) by heating, with or without a catalyst. Thermal cracking uses high temperature and pressure; catalytic cracking uses a zeolite catalyst at about 500 °C and gives branched alkanes and aromatic compounds useful in petrol.", title="Cracking"),
        T("Example: [[C10H22 -> C8H18 + C2H4]]. The alkene products are important raw materials for the plastics industry. Cracking matches the supply of heavy fractions to the demand for petrol and alkenes."),
        H("Alkenes: why they are reactive"),
        T("Alkenes have the formula [[!C_nH_{2n}]] and contain a C=C bond. The double bond is one **sigma** bond plus one **pi** bond. The pi bond is formed by sideways overlap of p orbitals, above and below the plane of the molecule. The C=C bond energy is about 612 kJ/mol, less than twice the C-C value, so the pi bond is only about 265 kJ/mol and is easier to break. It is also a region of **high electron density** that attracts **electrophiles**."),
        D("In an **electrophilic addition** reaction an electrophile is attracted to the electron-rich C=C bond. The pi bond breaks and two new sigma bonds form, so the alkene becomes a saturated product.", title="Electrophilic addition"),
        KEY("Reactions of ethene and propene", "All are addition reactions across the C=C bond.", cards=[
            ["Hydrogen", "[[C2H4 + H2 -> C2H6]]. Nickel catalyst, about 150 °C. Used to harden vegetable oils."],
            ["Bromine", "[[C2H4 + Br2 -> CH2BrCH2Br]]. Room temperature, no catalyst. Orange bromine water becomes colourless: the test for C=C."],
            ["Hydrogen bromide", "[[CH3CH=CH2 + HBr -> CH3CHBrCH3]]. Gas, room temperature. Major product 2-bromopropane."],
            ["Steam", "[[C2H4 + H2O -> C2H5OH]]. Steam over a phosphoric acid catalyst at about 300 °C and high pressure; the industrial route to ethanol (conditions: check your textbook)."],
        ]),
        H("The mechanism and Markovnikov's rule"),
        T("Hydrogen bromide is polar: H is δ+. The pi electrons of propene attack the δ+ hydrogen (step 1); the H-Br bond breaks heterolytically and Br goes away as [[Br^-]]. A **carbocation** is left. In step 2 the bromide ion, a nucleophile, attacks the carbocation."),
        IMG("al-chl3-electrophilic-addition.svg", alt="Two-step mechanism: propene pi electrons attack the hydrogen of HBr giving a secondary carbocation and bromide; bromide then attacks the carbocation to give 2-bromopropane.", caption="Figure 1. Electrophilic addition of HBr to propene. Curly arrows show electron pairs moving."),
        D("When HX adds to an **unsymmetrical** alkene, the **hydrogen adds to the carbon that already has more hydrogen atoms**. In other words, the halogen ends up on the carbon with fewer hydrogens. The reason: the H⁺ can add to either carbon of C=C. Adding to C1 of propene gives a **secondary** carbocation; adding to C2 gives a **primary** carbocation, which is less stable. The more stable carbocation forms faster, so the major product comes from it.", title="Markovnikov's rule"),
        T("For propene: the secondary carbocation [[!CH_3CH^{+}CH_3]] gives **2-bromopropane** (major product). The primary carbocation [[CH3CH2CH2^+]] would give 1-bromopropane (minor product)."),
        T("For the reaction with bromine, many textbooks give a similar mechanism: the Br-Br molecule is polarised (induced dipole) by the pi electrons, the pi electrons attack the near bromine and Br⁻ leaves, then Br⁻ attacks the carbocation. More advanced texts describe a three-membered bromonium ion instead (check your textbook)."),
        H("Testing for and breaking the C=C bond"),
        T("**Bromine water test:** shake with the sample; orange to colourless means unsaturation. **Potassium manganate(VII):** cold, dilute, alkaline [[KMnO4]] is decolourised (purple to green or brown) and the alkene becomes a **diol**: [[C2H4 + H2O + O -> HOCH2CH2OH]], where [O] is oxygen from the oxidising agent. Hot acidified [[KMnO4]] breaks the C=C bond completely and gives carboxylic acids, ketones or carbon dioxide."),
        T("**Ozonolysis:** ozone [[O3]] adds to the C=C bond to form an ozonide. Water (often with zinc to prevent further oxidation) then splits it into **two carbonyl compounds**. Each carbon of the old C=C becomes a C=O group. A carbon with an H gives an aldehyde; a carbon with two alkyl groups gives a ketone. This is used to find the position of a double bond."),
        EX("Worked example 1: free-radical chain", intro="Write the equations for the propagation and termination steps in the reaction of ethane with bromine under UV light.", steps=[
            S("Initiation", text="[[Br2 -> 2Br.]] (homolytic fission by UV light)."),
            S("Propagation step 1", text="[[C2H6 + Br. -> C2H5. + HBr]]."),
            S("Propagation step 2", text="[[C2H5. + Br2 -> C2H5Br + Br.]], which regenerates a bromine radical."),
            S("Termination", text="Any two radicals combine, for example [[C2H5. + Br. -> C2H5Br]] or [[Br. + Br. -> Br2]]."),
        ]),
        EX("Worked example 2: Markovnikov addition", intro="Predict the major product when [[(CH3)2C=CH2]] reacts with HBr and explain.", steps=[
            S("Where can H add?", text="H can add to the CH2 carbon or to the C(CH3)2 carbon."),
            S("Which carbocation is formed?", text="H adds to CH2 (the carbon with more hydrogens), leaving [[(CH3)3C^+]], a **tertiary** carbocation. The other route gives a primary carbocation."),
            S("Add bromide", text="[[Br^-]] attacks the tertiary carbocation: **2-bromo-2-methylpropane** [[(CH3)3CBr]] is the major product."),
        ]),
        EX("Worked example 3: combustion volumes", intro="10 cm³ of a gaseous hydrocarbon are burnt in 70 cm³ of oxygen (an excess). After cooling to room temperature, the gas volume is 50 cm³; shaking with potassium hydroxide solution leaves 10 cm³. Find the formula of the hydrocarbon.", steps=[
            S("Gas removed by KOH", text="This is CO2: 50 − 10 = 40 cm³. The 10 cm³ left is unused oxygen."),
            S("Carbon atoms per molecule", math=r"x = \dfrac{40}{10} = 4"),
            S("Oxygen used", math=r"70 - 10 = 60\ \text{cm}^3 \;\Rightarrow\; 6\ \text{volumes per volume of hydrocarbon}"),
            S("Use the equation", math=r"x + \dfrac{y}{4} = 6 \;\Rightarrow\; y = 8", text="The hydrocarbon is [[C4H8]] (a butene or cyclobutane). Water is liquid at room temperature, so it takes up no volume."),
        ], check=r"\mathrm{C_4H_8} + 6\mathrm{O_2} \rightarrow 4\mathrm{CO_2} + 4\mathrm{H_2O}"),
        EX("Worked example 4: use ozonolysis to find the alkene", intro="An alkene [[C5H10]] reacts with ozone and then water. The products are propanone and ethanal. Identify the alkene.", steps=[
            S("Join the two carbonyl carbons by a double bond", text="Propanone [[(CH3)2C=O]] gives [[(CH3)2C=]]. Ethanal [[CH3CH=O]] gives [[=CHCH3]]."),
            S("Write the alkene", text="[[(CH3)2C=CHCH3]], **2-methylbut-2-ene**. Check: C5H10, two carbonyl products."),
        ]),
        H("Common mistakes"),
        MISTAKE("Reversing Markovnikov's rule", "The halogen goes on the carbon with **fewer** hydrogens (the one that gives the more stable carbocation). Do not memorise the rule without the reason: the reason is carbocation stability."),
        MISTAKE("Saying bromine water becomes 'clear'", "It becomes **colourless** (orange to colourless). 'Clear' only describes transparency, and a solution can be clear and coloured."),
        MISTAKE("Calling the chlorination of methane an addition reaction", "A hydrogen is **replaced** by chlorine. It is a free-radical **substitution**; the mechanism needs UV light and goes through radicals, not ions."),
        MISTAKE("Forgetting that radical substitution gives a mixture", "The product still contains C-H bonds, so more substitution is possible. Write [[CH3Cl]] as the first product, and say that [[CH2Cl2]], [[CHCl3]] and [[CCl4]] can also form."),
        QUIZ("Which step is a **propagation** step in the chlorination of methane?", ["[[Cl2 -> 2Cl.]]", "[[CH4 + Cl. -> .CH3 + HCl]]", "[[.CH3 + Cl. -> CH3Cl]]", "[[.CH3 + .CH3 -> C2H6]]"], 1,
             "In a propagation step a radical reacts and another radical is formed, so the chain continues.",
             feedback=["This is initiation: radicals are made from a molecule.", "", "Two radicals combine and no radical is left: termination.", "Two radicals combine and no radical is left: termination."]),
        QUIZ("The major product of [[CH3CH2CH=CH2 + HBr]] is", ["1-bromobutane", "2-bromobutane", "1,2-dibromobutane", "bromoethane"], 1,
             "H adds to C1 (more hydrogens) to give the secondary carbocation [[!CH_3CH_2CH^{+}CH_3]], which is attacked by Br⁻ to give 2-bromobutane.",
             feedback=["This comes from the less stable primary carbocation.", "", "Two bromines would require [[Br2]] rather than HBr.", "The carbon chain has not been broken; the product has four carbons."]),
        H("Practice questions"),
        PQ("Explain why alkanes are unreactive towards polar reagents such as aqueous acids and alkalis.",
           "The C-C and C-H bonds are strong and non-polar (carbon and hydrogen have almost equal electronegativity). There is no electron-rich or electron-deficient site for nucleophiles or electrophiles to attack, so reaction needs radicals or high temperatures."),
        PQ("Describe, with equations, the mechanism of the reaction of methane with chlorine in UV light. Name each stage.",
           "Initiation: [[Cl2 -> 2Cl.]] (homolytic fission in UV light). Propagation: [[CH4 + Cl. -> .CH3 + HCl]]; then [[.CH3 + Cl2 -> CH3Cl + Cl.]]. Termination: [[Cl. + Cl. -> Cl2]], [[.CH3 + Cl. -> CH3Cl]] or [[.CH3 + .CH3 -> C2H6]]. Overall: [[CH4 + Cl2 -> CH3Cl + HCl]]."),
        PQ("Draw the mechanism for the reaction of propene with hydrogen bromide, and explain why 2-bromopropane is the major product.",
           "Step 1: the pi electrons of C=C attack the δ+ hydrogen of H-Br (curved arrow from the C=C to H); the H-Br bond breaks heterolytically (curved arrow from the bond to Br). A carbocation and [[Br^-]] form. H adds to C1, so the carbocation is [[!CH_3CH^{+}CH_3]] (secondary). Step 2: a lone pair of [[Br^-]] attacks the carbocation (curved arrow to C+), giving [[CH3CHBrCH3]]. The secondary carbocation is more stable than the primary one ([[CH3CH2CH2^+]]) because of the +I effect of two alkyl groups, so it forms faster and 2-bromopropane is the major product."),
        PQ("An alkene X reacts with ozone and then water to give only one product, ethanal. Identify X and explain your answer. Describe what you would see when X is shaken with bromine water.",
           "Ozonolysis splits the C=C and puts a C=O on each carbon. If only ethanal [[CH3CHO]] forms, both carbons of the C=C each carry one [[CH3]] and one H, so X is but-2-ene [[CH3CH=CHCH3]]. With bromine water, the orange colour disappears: the solution becomes colourless."),
        TIP("In the exam: alkanes and alkenes are asked in Paper 1 (mechanism steps, products of ozonolysis, Markovnikov addition, tests) and in Paper 2 organic questions (give conditions, mechanism with curly arrows, distinguish ethane from ethene). Always state the **reagent**, the **conditions** and the **observation**."),
        H("Summary"),
        SUM("Alkanes are unreactive (strong non-polar sigma bonds); they burn and react with halogens by a free-radical chain (initiation, propagation, termination) in UV light, giving a mixture.",
            "Cracking breaks long alkanes into shorter alkanes and alkenes using heat or a zeolite catalyst.",
            "Alkenes have a pi bond: electron-rich, weaker, attacked by electrophiles in electrophilic addition (H2, Br2, HBr, H2O).",
            "Markovnikov's rule: with HX the H adds to the carbon with more hydrogens, because this gives the more stable (more substituted) carbocation.",
            "Bromine water is decolourised by alkenes; ozone then water splits C=C into two carbonyl compounds."),
    ])]
# ============================================================================================
# Topic 5. Alkynes and haloalkanes (lesson 1 of 2): alkynes
# ============================================================================================
LESSONS += [lesson(
    module=M_ORG, topic="Alkynes and haloalkanes",
    title="Alkynes: structure, preparation and reactions of ethyne",
    slug="chl3-alkynes", minutes=22,
    summary="Alkynes contain a C≡C bond (one sigma, two pi). They undergo addition reactions in two stages, hydration to carbonyl compounds, and terminal alkynes give precipitates with ammoniacal silver or copper(I) because of their acidic C-H.",
    objectives=[
        "Describe the sp hybridisation, linear shape and bonding of the C≡C bond",
        "Prepare ethyne from calcium carbide and from a dihaloalkane, and give its uses",
        "Describe the addition reactions of alkynes with H2, Br2, HBr and H2O, using Markovnikov's rule",
        "Use the acidity of the terminal C-H to distinguish terminal from internal alkynes",
    ],
    key_concepts=["C≡C bond", "sp hybridisation", "Terminal alkyne", "Addition in two stages", "Hydration of ethyne", "Silver ethynide"],
    blocks=[
        H("Introduction"),
        T("In many garages and metal workshops across Cameroon, welders cut and join steel with an **oxy-acetylene** torch. The gas, **ethyne** (acetylene), is made when calcium carbide, a grey stone-like solid, meets water. Ethyne burns with the hottest flame of any common fuel gas, over 3000 °C in pure oxygen. Ethyne is the simplest **alkyne**, a hydrocarbon with a carbon-carbon **triple bond**."),
        H("Structure and bonding"),
        T("Alkynes have the general formula [[!C_nH_{2n-2}]] and the functional group -C≡C-. The triple bond is made of one **sigma** bond and **two pi** bonds at right angles. Each carbon of the triple bond forms two sigma bonds (one to the other carbon, one to H or to another carbon) using **sp hybrid orbitals**: one s and one p orbital mix to give two sp orbitals 180° apart. The two remaining p orbitals on each carbon overlap sideways to make the two pi bonds."),
        D("Because each carbon has two sigma bonds arranged at 180°, the C-C≡C-H unit is **linear**. Ethyne [[HC#CH]] is a linear molecule with a H-C≡C bond angle of 180°. The C≡C bond is short (about 120 pm) and strong (about 837 kJ/mol).", title="Shape of alkynes"),
        T("Alkynes are named with the ending **-yne**: ethyne, propyne [[CH3C#CH]], but-1-yne [[HC#CCH2CH3]], but-2-yne [[CH3C#CCH3]]. An alkyne with the triple bond at the end of the chain (a **terminal** alkyne, with a [[C#C-H]] group) behaves differently from one with the triple bond inside the chain (an **internal** alkyne)."),
        EX("Worked example 1: isomers of [[C5H8]] that are alkynes", intro="Draw and name all the alkynes with the formula [[C5H8]].", steps=[
            S("Degree of unsaturation", math=r"\dfrac{2(5) + 2 - 8}{2} = 2", text="One triple bond accounts for 2."),
            S("Straight chain, five carbons", text="Triple bond at carbon 1: **pent-1-yne** [[HC#CCH2CH2CH3]]. At carbon 2: **pent-2-yne** [[CH3C#CCH2CH3]]. (Position 3 repeats position 2, by numbering from the other end.)"),
            S("Branched chain, four carbons plus a methyl", text="The triple bond cannot be at the carbon carrying the methyl branch (that carbon would need five bonds), so only **3-methylbut-1-yne** [[HC#CCH(CH3)2]] is possible."),
            S("Count", text="There are **3** alkyne isomers of [[C5H8]]."),
        ]),
        H("Making ethyne"),
        T("**From calcium carbide.** Calcium carbide reacts with cold water: [[CaC2 + 2H2O -> C2H2 + Ca(OH)2]]. This is used in welding and in the laboratory. The gas is collected over water."),
        T("**By elimination.** Heating 1,2-dibromoethane with a **concentrated solution of potassium hydroxide in ethanol** removes two molecules of HBr: [[BrCH2CH2Br + 2KOH -> HC#CH + 2KBr + 2H2O]]. The same type of reaction works for other dihaloalkanes."),
        H("Reactions of alkynes"),
        T("Like alkenes, alkynes are electron-rich and undergo **electrophilic addition**. Because there are two pi bonds, addition can happen **twice**."),
        KEY("Addition reactions of ethyne", "Each reagent can add once or twice, depending on how much is used.", cards=[
            ["Hydrogen", "[[C2H2 + 2H2 -> C2H6]] with a nickel catalyst. With a poisoned palladium catalyst (Lindlar catalyst, check your textbook) the reaction stops at the alkene [[C2H4]]."],
            ["Bromine", "First 1,2-dibromoethene [[CHBr=CHBr]], then 1,1,2,2-tetrabromoethane [[CHBr2CHBr2]]. Bromine water is decolourised."],
            ["Hydrogen bromide", "[[C2H2 + HBr -> CH2=CHBr]] (bromoethene); excess HBr gives [[CH3CHBr2]] (1,1-dibromoethane) by Markovnikov's rule."],
            ["Water (hydration)", "[[C2H2 + H2O -> CH3CHO]]. Catalyst: mercury(II) sulfate in dilute sulfuric acid, about 60 °C."],
        ]),
        T("**Hydration** first gives an **enol** (a compound with -OH on a C=C carbon, [[CH2=CHOH]]), which is unstable and rearranges at once to the carbonyl compound. Ethyne gives **ethanal**. Any other terminal alkyne and any internal alkyne gives a **ketone**, because Markovnikov's rule puts the -OH on the more substituted carbon: propyne [[CH3C#CH]] gives propanone [[CH3COCH3]]."),
        T("**Combustion.** [[2C2H2 + 5O2 -> 4CO2 + 2H2O]]. In air, ethyne burns with a **smoky, yellow flame** because its percentage of carbon is high and combustion is incomplete. In an oxy-acetylene torch the flame is very hot."),
        T("**Trimerisation.** Ethyne passed through a red-hot tube forms benzene: [[3C2H2 -> C6H6]]."),
        H("The acidity of the terminal alkyne"),
        T("The carbon of a [[C#C-H]] group uses an sp orbital, which has 50% s character and holds electrons close to the nucleus. This makes the carbon more electronegative than an alkene or alkane carbon, so the C-H bond is **weakly acidic** (ethyne, pKa about 25). Terminal alkynes react with sodium to give hydrogen, and they give **precipitates with ammoniacal silver nitrate** (white) and with ammoniacal copper(I) chloride (red):"),
        F(r"\mathrm{C_2H_2} + 2[\mathrm{Ag(NH_3)_2}]^{+} \rightarrow \mathrm{Ag_2C_2}\downarrow + 2\mathrm{NH_4^{+}} + 2\mathrm{NH_3}", title="Silver ethynide precipitate"),
        MISTAKE("Dry metal acetylides are explosive", "Silver and copper acetylides are shock-sensitive when dry. In a laboratory, keep the precipitate wet and destroy it with dilute nitric acid after the test. Never keep it. This is a real safety rule in practical work."),
        T("Internal alkynes such as but-2-yne have **no** acidic hydrogen and give **no** precipitate. So the test distinguishes but-1-yne from but-2-yne."),
        EX("Worked example 2: identify the compound from tests", intro="A hydrocarbon [[C4H6]] decolourises bromine water and gives a white precipitate with ammoniacal silver nitrate. Identify it, and give the product of its reaction with excess hydrogen and nickel.", steps=[
            S("Degree of unsaturation", math=r"\dfrac{2(4) + 2 - 6}{2} = 2", text="A triple bond (or two double bonds) is present."),
            S("The precipitate shows a terminal alkyne", text="Only a compound with a [[C#C-H]] group gives silver ethynide. The terminal alkyne with four carbons is **but-1-yne** [[HC#CCH2CH3]]."),
            S("Hydrogenation", text="[[C4H6 + 2H2 -> C4H10]]: butane [[CH3CH2CH2CH3]]."),
        ]),
        EX("Worked example 3: Markovnikov addition to propyne", intro="Give the product of propyne [[CH3C#CH]] with excess hydrogen bromide.", steps=[
            S("First addition", text="H adds to the terminal carbon (which has more hydrogens), Br to the middle carbon: [[CH3CBr=CH2]] (2-bromopropene)."),
            S("Second addition", text="Again H adds to the carbon with more hydrogens (CH2) and Br to the carbon that already carries Br: [[CH3CBr2CH3]]."),
            S("Name", text="**2,2-dibromopropane**. Both bromine atoms are on the same carbon."),
        ]),
        EX("Worked example 4: volume of ethyne from calcium carbide", intro="6.4 g of calcium carbide are added to excess water. What volume of ethyne forms at rtp? (Ar: Ca 40, C 12; molar volume 24 dm³ at rtp.)", steps=[
            S("Mr of calcium carbide", math=r"M_r(\mathrm{CaC_2}) = 40 + 2 \times 12 = 64"),
            S("Moles", math=r"n = \dfrac{6.4}{64} = 0.10\ \text{mol}"),
            S("Ratio 1 : 1 with ethyne", text="From the equation, 1 mol of [[CaC2]] gives 1 mol of [[C2H2]]."),
            S("Volume", math=r"V = 0.10 \times 24 = 2.4\ \text{dm}^3"),
        ]),
        H("Common mistakes"),
        MISTAKE("Stopping addition at one stage", "With excess reagent, an alkyne takes up **two** molecules of H2, Br2 or HX. Read the question: 'excess' or 'one mole' decides the product."),
        MISTAKE("Giving an aldehyde from every alkyne hydration", "Only ethyne gives an aldehyde (ethanal). Every other alkyne gives a ketone, because -OH adds to the more substituted carbon."),
        MISTAKE("Saying but-2-yne gives a precipitate with silver nitrate", "The test needs a terminal C-H. But-2-yne has none."),
        QUIZ("The shape of the ethyne molecule and the hybridisation of its carbon atoms are", ["bent, sp2", "trigonal planar, sp2", "linear, sp", "tetrahedral, sp3"], 2,
             "Each carbon has two sigma bonds arranged at 180°, which needs two sp hybrid orbitals. The molecule is linear.",
             feedback=["The H-C≡C bond angle is 180°, not bent.", "Trigonal planar shape and sp2 belong to alkenes (angle 120°).", "", "Tetrahedral and sp3 belong to alkanes."]),
        QUIZ("Which compound gives a white precipitate with ammoniacal silver nitrate?", ["but-2-yne", "but-1-yne", "but-1-ene", "butane"], 1,
             "But-1-yne is a terminal alkyne. Its acidic C-H is replaced by Ag to give a white solid.",
             feedback=["But-2-yne is internal, with no terminal C-H.", "", "Alkenes have no acidic hydrogen of this type.", "Alkanes are unreactive."]),
        H("Practice questions"),
        PQ("Describe the bonding in ethyne in terms of sigma bonds, pi bonds and hybrid orbitals, and state the H-C-C bond angle.",
           "Each carbon is sp hybridised: two sp orbitals at 180°. One sp orbital forms a sigma bond to hydrogen, the other forms the C-C sigma bond. The two unhybridised p orbitals on each carbon overlap sideways in two perpendicular directions to make two pi bonds. So the triple bond is one sigma and two pi bonds. The H-C-C angle is 180° and the molecule is linear."),
        PQ("Write equations for the preparation of ethyne from calcium carbide, and for its complete reaction with bromine.",
           "[[CaC2 + 2H2O -> C2H2 + Ca(OH)2]]. With excess bromine: [[C2H2 + 2Br2 -> CHBr2CHBr2]] (1,1,2,2-tetrabromoethane), via [[CHBr=CHBr]] (1,2-dibromoethene)."),
        PQ("Compound P is [[C5H8]] and gives no precipitate with ammoniacal silver nitrate. It reacts with water in the presence of mercury(II) sulfate and dilute acid to form a ketone. Suggest a structure for P and name it.",
           "P has no terminal C-H, so it is an internal alkyne: pent-2-yne [[CH3C#CCH2CH3]]. (3-Methylbut-1-yne and pent-1-yne are terminal alkynes and would give the precipitate.) Hydration gives a ketone: pentan-2-one or pentan-3-one, by -OH adding to either carbon of the triple bond (a mixture)."),
        PQ("Describe how you could distinguish between ethane, ethene and ethyne using simple tests.",
           "Add bromine water: ethane does not change it; ethene and ethyne decolourise it (ethyne more slowly). Add ammoniacal silver nitrate to the gas that decolourised bromine: ethyne gives a white precipitate; ethene gives none. Alternatively, note that ethyne burns with a very smoky flame."),
        TIP("In the exam: alkynes are tested in Paper 1 (shape, tests, products of hydration) and Paper 2 (distinguishing ethane, ethene and ethyne; the Board's 2023 report mentions hybridisation of an sp compound and chemical tests to distinguish compounds). Give the reagent and the observation."),
        H("Summary"),
        SUM("An alkyne has a C≡C bond: one sigma and two pi. Each triple-bond carbon is sp hybridised and the group is linear (180°).",
            "Ethyne is made from [[CaC2]] and water, or by double elimination of HBr from 1,2-dibromoethane with ethanolic KOH.",
            "Alkynes add H2, Br2 and HX twice with excess reagent; HX follows Markovnikov's rule.",
            "Hydration (HgSO4, dilute H2SO4) gives a carbonyl compound by an enol: ethanal from ethyne, ketones from other alkynes.",
            "Terminal alkynes have an acidic C-H and give precipitates with ammoniacal silver nitrate (white) or copper(I) chloride (red); the dry solids are explosive."),
    ])]
# ============================================================================================
# Topic 5. Alkynes and haloalkanes (lesson 2 of 2): haloalkanes
# ============================================================================================
LESSONS += [lesson(
    module=M_ORG, topic="Alkynes and haloalkanes",
    title="Haloalkanes: nucleophilic substitution (SN1, SN2) and elimination (E1, E2)",
    slug="chl3-haloalkanes-substitution-elimination", minutes=28,
    summary="Haloalkanes react with nucleophiles by SN1 or SN2, and with ethanolic base by elimination to alkenes (E1, E2). Learn their preparation, mechanisms with curly arrows, rates, stereochemistry and how to choose the conditions.",
    objectives=[
        "Describe the preparation and physical properties of haloalkanes and explain the trend in C-X reactivity",
        "Write the SN2 and SN1 mechanisms with curly arrows and link them to rate equations and stereochemistry",
        "Explain how aqueous and ethanolic hydroxide give substitution and elimination, and predict the products using Zaitsev's rule",
        "Use silver nitrate to identify the halogen in a haloalkane",
    ],
    key_concepts=["Nucleophilic substitution", "SN1 and SN2", "Rate equation", "Inversion and racemisation", "Elimination E1 and E2", "Zaitsev's rule", "C-X bond strength"],
    blocks=[
        H("Introduction"),
        T("PVC pipes carry water in many Cameroonian homes. The monomer of PVC is chloroethene, a haloalkene. Other haloalkanes were used as refrigerants, solvents and insecticides, and the chlorofluorocarbons (CFCs) once used in fridges and aerosol sprays have damaged the ozone layer. In the stratosphere, ultraviolet light breaks a C-Cl bond homolytically; the chlorine radical then destroys ozone in a chain: [[Cl. + O3 -> ClO. + O2]] followed by [[ClO. + O -> Cl. + O2]]. For chemists, haloalkanes are most important as **starting materials**: the C-X bond is easily replaced, so a haloalkane can be turned into alcohols, nitriles, amines and alkenes."),
        H("Structure, classification and properties"),
        T("A haloalkane has the formula [[!C_nH_{2n+1}X]] with X = F, Cl, Br or I. Classify them as primary, secondary or tertiary, as in the first lesson. Halogens are more electronegative than carbon, so the **C-X bond is polar**: carbon is δ+, halogen δ−. The δ+ carbon is attacked by **nucleophiles**."),
        T("**Boiling points** rise with chain length and, for a given alkyl group, from chloro to bromo to iodo (chloroethane 12 °C, bromoethane 38 °C, iodoethane 72 °C) because larger atoms have more electrons and stronger dispersion forces. Haloalkanes are **insoluble in water**: they cannot hydrogen-bond with water, and the attraction between their molecules and water is weaker than water's own hydrogen bonding. The bromo- and iodoalkanes are denser than water."),
        H("Making haloalkanes"),
        KEY("Preparation methods", "Alcohols are the usual starting point in the laboratory.", cards=[
            ["From an alcohol and PCl5 or SOCl2", "[[C2H5OH + PCl5 -> C2H5Cl + POCl3 + HCl]] and [[C2H5OH + SOCl2 -> C2H5Cl + SO2 + HCl]]. With SOCl2 the by-products are gases, so the product is easy to purify."],
            ["From an alcohol and HBr", "[[C2H5OH + HBr -> C2H5Br + H2O]]. The HBr is made in the flask from sodium bromide and concentrated sulfuric acid: [[NaBr + H2SO4 -> NaHSO4 + HBr]]. For iodoalkanes use red phosphorus and iodine, which make PI3 in the flask."],
            ["From an alkene", "Addition of HX or [[X2]] (previous lesson). Gives the Markovnikov product."],
            ["From an alkane", "Free-radical substitution in UV light. Gives mixtures, so it is not a good method."],
        ]),
        H("Nucleophilic substitution"),
        D("In **nucleophilic substitution** a nucleophile uses a lone pair to bond to the δ+ carbon, and the halide ion leaves (the **leaving group**).", title="Nucleophilic substitution"),
        CODE("""Reagent (nucleophile)      Conditions                  Product
aqueous NaOH or KOH, OH-   warm / reflux               alcohol      CH3CH2OH
ethanolic KCN, CN-         heat under reflux           nitrile      CH3CH2CN
excess ethanolic NH3       heated in a sealed tube     amine        CH3CH2NH2
water                      slow, warm                  alcohol

Chain extension: CH3CH2Br -> CH3CH2CN -> (hydrolysis) -> CH3CH2COOH""", "text", title="Nucleophilic substitution of bromoethane"),
        T("The nitrile route is useful because it **adds one carbon atom**: [[CH3CH2Br + CN^- -> CH3CH2CN + Br^-]]. Acid hydrolysis then gives propanoic acid: [[CH3CH2CN + 2H2O + H^+ -> CH3CH2COOH + NH4^+]]."),
        H("How fast? The C-X bond strength"),
        T("The rate of hydrolysis follows the **strength of the C-X bond**, not its polarity. Approximate bond enthalpies are C-F 485, C-Cl 340, C-Br 280, C-I 240 kJ/mol (values vary slightly between data books). The weaker the bond, the faster it breaks: **RI > RBr > RCl >> RF**. Fluoroalkanes are almost inert."),
        T("This can be shown by warming the haloalkane with aqueous silver nitrate in ethanol. The released halide ion makes a precipitate: [[Ag^+ + Cl^- -> AgCl]] (white), [[Ag^+ + Br^- -> AgBr]] (cream) and AgI (yellow). The yellow precipitate of AgI appears first, the white AgCl last."),
        EX("Worked example 1: identify the halogen in an unknown haloalkane", intro="Describe how you would show that a liquid contains bromine in a haloalkane.", steps=[
            S("Release the halide ion", text="Warm the liquid with aqueous sodium hydroxide. The haloalkane is hydrolysed: [[RBr + OH^- -> ROH + Br^-]]."),
            S("Acidify", text="Add dilute nitric acid to destroy any excess hydroxide (otherwise [[Ag2O]] would precipitate)."),
            S("Add silver nitrate", text="A **cream precipitate** of AgBr shows that bromide is present. Confirm with ammonia: AgBr is insoluble in dilute ammonia but dissolves in concentrated ammonia."),
        ]),
        H("The SN2 mechanism"),
        D("**SN2** stands for substitution, nucleophilic, **bimolecular**. The nucleophile attacks the carbon from the side **opposite** the leaving group, and as the new bond forms the old one breaks, in **one step** through a **transition state** in which carbon is partly bonded to both. The rate depends on **both** reactants: rate = k[haloalkane][nucleophile].", title="SN2"),
        IMG("al-chl3-sn2-mechanism.svg", alt="SN2 mechanism: hydroxide attacks the carbon from the side opposite bromine, through a bracketed transition state with partial bonds, to give an alcohol and bromide.", caption="Figure 1. The SN2 mechanism. Curly arrows: lone pair of OH⁻ to carbon, and C-Br bond pair to bromine."),
        T("Because the nucleophile attacks from the back, a chiral carbon is **inverted** (like an umbrella blown inside out). SN2 is fastest for **primary** haloalkanes: three small hydrogens leave room for the nucleophile. A tertiary carbon is too crowded."),
        EX("Worked example 2: stereochemistry of SN2", intro="(R)-2-Bromobutane reacts with aqueous sodium hydroxide by the SN2 mechanism. What is the product, and what is its configuration?", steps=[
            S("Product", text="Butan-2-ol [[CH3CH(OH)CH2CH3]]."),
            S("Inversion", text="The nucleophile attacks from the side opposite bromine, so the three other groups flip. The priority order (OH > C2H5 > CH3 > H) matches the order for bromine, so the label changes."),
            S("Answer", text="The product is **(S)-butan-2-ol**, the mirror image of what retention would give."),
        ]),
        H("The SN1 mechanism"),
        D("**SN1** stands for substitution, nucleophilic, **unimolecular**. It has **two steps**. Step 1 (slow, rate-determining): the C-X bond breaks heterolytically, giving a carbocation and a halide ion. Step 2 (fast): the nucleophile attacks the carbocation. The slow step involves only the haloalkane, so rate = k[haloalkane]; the concentration of the nucleophile does not appear.", title="SN1"),
        IMG("al-chl3-sn1-mechanism.svg", alt="SN1 mechanism: step 1 shows the C-Br bond of 2-bromo-2-methylpropane breaking to give a planar carbocation and bromide; step 2 shows hydroxide attacking the carbocation to give 2-methylpropan-2-ol.", caption="Figure 2. The SN1 mechanism of a tertiary haloalkane."),
        T("SN1 is favoured for **tertiary** haloalkanes because they form stable carbocations (three alkyl groups give +I stabilisation) and are too crowded for SN2. The carbocation is **planar**, so the nucleophile can attack from either face. If the carbon was chiral, the product is a mixture of both enantiomers (a racemate, or partly racemised). Polar solvents such as water and ethanol stabilise the ions and speed up SN1."),
        CODE("""                  SN2                     SN1
Steps             1                       2
Rate equation     k[RX][Nu]               k[RX]
Molecularity      bimolecular             unimolecular
Intermediate      none (transition state) carbocation
Favoured by       primary RX              tertiary RX
Chiral centre     inversion               racemisation
Secondary RX      can use both, depending on conditions""", "text", title="SN2 compared with SN1"),
        EX("Worked example 3: deduce the mechanism from rate data", intro="For the hydrolysis of a bromoalkane RBr, initial rates were: [RBr] = 0.10 mol/dm³, [OH⁻] = 0.10 mol/dm³, rate = 2.0 × 10⁻⁴ mol dm⁻³ s⁻¹; [RBr] = 0.20, [OH⁻] = 0.10, rate = 4.0 × 10⁻⁴; [RBr] = 0.10, [OH⁻] = 0.20, rate = 2.0 × 10⁻⁴. Find the rate equation and suggest the type of haloalkane.", steps=[
            S("Effect of [RBr]", text="Doubling [RBr] doubles the rate: first order in RBr."),
            S("Effect of [OH⁻]", text="Doubling [OH⁻] does not change the rate: zero order in OH⁻."),
            S("Rate equation", math=r"\text{rate} = k[\mathrm{RBr}]", text="First order overall."),
            S("Value of k", math=r"k = \dfrac{2.0\times10^{-4}}{0.10} = 2.0\times10^{-3}\ \text{s}^{-1}"),
            S("Mechanism", text="A rate equation with no nucleophile term fits **SN1**: the slow step involves RBr alone. RBr is most likely a **tertiary** bromoalkane."),
        ]),
        H("Elimination"),
        T("A haloalkane with a hydrogen on the carbon next to the C-X carbon can lose HX and form an alkene. The reagent is a **strong base**, **hot ethanolic** potassium hydroxide. The hydroxide ion now acts as a **base** (it removes H⁺) rather than as a nucleophile."),
        F(r"\mathrm{CH_3CHBrCH_3} + \mathrm{KOH} \rightarrow \mathrm{CH_3CH{=}CH_2} + \mathrm{KBr} + \mathrm{H_2O}", title="Elimination (ethanolic KOH, heat)"),
        D("**E2** (elimination, bimolecular): one step. The base removes a hydrogen from the carbon next to the C-X carbon at the same moment the halide leaves and the C=C forms. Rate = k[RX][base]. **E1** (elimination, unimolecular): two steps with the same slow first step as SN1 (carbocation formation), then loss of H⁺ from a neighbouring carbon. Rate = k[RX].", title="E2 and E1"),
        D("When more than one alkene can form, the **major product is the more substituted alkene** (the one with more alkyl groups on the C=C), because it is more stable. Example: 2-bromobutane with ethanolic KOH gives mainly but-2-ene (cis and trans) with a little but-1-ene.", title="Zaitsev's rule"),
        KEY("Substitution or elimination? Choose the conditions", "The same two reagents, but a different solvent, give different products.", cards=[
            ["Aqueous KOH, warm", "More water: OH⁻ acts as a **nucleophile**. Substitution: alcohol."],
            ["Ethanolic KOH, hot", "Little water, high temperature: OH⁻ acts as a **base**. Elimination: alkene."],
            ["Structure of RX", "Primary: mainly SN2. Tertiary: SN1 and E1 (E2 with a strong base). Secondary: mixtures; high temperature favours elimination."],
        ]),
        EX("Worked example 4: predict the products", intro="Give the organic product of 2-bromopropane with (a) aqueous NaOH, warm, and (b) ethanolic KOH, hot. Name the type of reaction in each case.", steps=[
            S("(a) Aqueous alkali", text="[[CH3CHBrCH3 + OH^- -> CH3CH(OH)CH3 + Br^-]]: **propan-2-ol**; nucleophilic substitution (hydrolysis)."),
            S("(b) Ethanolic alkali", text="[[CH3CHBrCH3 + KOH -> CH3CH=CH2 + KBr + H2O]]: **propene**; elimination (dehydrobromination)."),
        ]),
        H("Common mistakes"),
        MISTAKE("Mixing up the conditions", "Aqueous hydroxide gives an alcohol (substitution). Ethanolic hydroxide gives an alkene (elimination). Always write the solvent in your answer."),
        MISTAKE("Starting curly arrows at the wrong place in SN2", "The arrow starts at the **lone pair** of the nucleophile (not at the negative charge sign) and ends at the carbon; a second arrow starts at the **middle of the C-X bond** and ends at the halogen."),
        MISTAKE("Saying the C-F bond is the most reactive because it is most polar", "Rate depends on **bond strength**. C-I is the weakest and so the most reactive; C-F is the strongest and nearly inert."),
        MISTAKE("Forgetting to acidify before silver nitrate", "Hydroxide ions would precipitate brown silver oxide and hide the halide result. Add dilute nitric acid first."),
        QUIZ("A haloalkane hydrolyses with a rate equation: rate = k[RX]. The mechanism is", ["SN2", "SN1", "E2", "free-radical substitution"], 1,
             "A first-order rate equation, independent of the nucleophile, fits SN1: the slow step involves only RX. (E1 also has this rate equation, but the reaction here is hydrolysis, a substitution.)",
             feedback=["SN2 would be first order in the nucleophile as well.", "", "E2 would be first order in the base as well, and gives an alkene.", "Radical substitution needs UV light and is not a hydrolysis."]),
        QUIZ("Which of these gives the **fastest** reaction with warm aqueous silver nitrate?", ["1-chlorobutane", "1-bromobutane", "1-iodobutane", "1-fluorobutane"], 2,
             "The C-I bond is the weakest of the four, so iodide leaves most easily and the yellow AgI precipitate forms first.",
             feedback=["C-Cl is stronger than C-Br and C-I.", "C-Br is stronger than C-I.", "", "C-F is the strongest bond and is almost unreactive."]),
        H("Practice questions"),
        PQ("Write the mechanism, using curly arrows, for the alkaline hydrolysis of bromoethane [[CH3CH2Br]], and state its name and order.",
           "The lone pair on the oxygen of [[OH^-]] attacks the δ+ carbon (curly arrow from the lone pair to carbon) while the C-Br bond breaks heterolytically (curly arrow from the middle of the C-Br bond to Br). One step through a transition state [HO···CH2(CH3)···Br]. Products: [[CH3CH2OH]] and [[Br^-]]. It is a nucleophilic substitution by the SN2 mechanism: rate = k[CH3CH2Br][OH⁻], second order overall."),
        PQ("Explain why 2-bromo-2-methylpropane reacts by SN1 while 1-bromobutane reacts by SN2.",
           "2-Bromo-2-methylpropane is tertiary: the carbon is crowded by three methyl groups, so back-side attack by a nucleophile is hindered, and the three alkyl groups stabilise the carbocation [[(CH3)3C^+]] by the +I effect. So it ionises in a slow first step (SN1). 1-Bromobutane is primary: the carbon has only one alkyl group and two H atoms, leaving room for back-side attack, and the primary carbocation would be unstable. So it reacts by SN2."),
        PQ("Compound Y, [[C4H9Br]], reacts with ethanolic potassium hydroxide to give a mixture of but-1-ene and but-2-ene. (a) Identify Y. (b) Which alkene is the major product and why? (c) Y reacts with aqueous sodium hydroxide to give a chiral alcohol. Name it.",
           "(a) Y is 2-bromobutane [[CH3CHBrCH2CH3]]: it can lose HBr towards C1 or C3. (b) But-2-ene is the major product: it has two alkyl groups on each side of the C=C (more substituted, more stable); Zaitsev's rule. (c) Butan-2-ol [[CH3CH(OH)CH2CH3]] has a chiral centre at C2."),
        PQ("Describe how you could show experimentally that 1-iodobutane is hydrolysed faster than 1-chlorobutane, and state the observations.",
           "Warm equal volumes of each haloalkane with the same volume of ethanolic silver nitrate in a water bath at the same temperature. 1-iodobutane gives a yellow precipitate of AgI quickly; 1-chlorobutane gives a white precipitate of AgCl slowly. The C-I bond is weaker (about 240 kJ/mol) than C-Cl (about 340 kJ/mol), so it breaks more easily."),
        TIP("In the exam: the Board's 2023 report lists the alkaline hydrolysis mechanism of a haloalkane and the products of reactions of organic compounds among the questions candidates found hardest. Practise the arrows: lone pair to carbon, bond to halogen. State the **conditions** (aqueous or ethanolic, heat), and the **name** of the mechanism."),
        H("Summary"),
        SUM("Haloalkanes are made from alcohols with PCl5, SOCl2 or HBr, or from alkenes by addition. The C-X bond is polar; reactivity follows bond strength: RI > RBr > RCl >> RF.",
            "Nucleophiles (OH⁻, CN⁻, NH3) replace the halogen. SN2 is one step, rate = k[RX][Nu], inversion, primary haloalkanes.",
            "SN1 is two steps through a planar carbocation, rate = k[RX], racemisation, tertiary haloalkanes.",
            "Hot ethanolic KOH eliminates HX to give an alkene (E2 or E1); the more substituted alkene is the major product (Zaitsev's rule). Aqueous KOH gives substitution.",
            "To test for the halogen: warm with NaOH(aq), acidify with HNO3, add AgNO3(aq): white AgCl, cream AgBr, yellow AgI."),
    ])]
# ============================================================================================
# Topic 6. Alcohols (1 lesson)
# ============================================================================================
LESSONS += [lesson(
    module=M_ORG, topic="Alcohols",
    title="Alcohols: preparation, properties, oxidation and tests",
    slug="chl3-alcohols", minutes=26,
    summary="Alcohols contain the -OH group. Learn how they are made (hydration, fermentation), how hydrogen bonding explains their properties, and their reactions: sodium, halogenation, esterification, dehydration and oxidation, which distinguishes primary, secondary and tertiary alcohols.",
    objectives=[
        "Explain the physical properties of alcohols using hydrogen bonding",
        "Describe the preparation of ethanol by fermentation and by hydration of ethene",
        "Write equations and give conditions for the reactions of alcohols with sodium, halogenating agents, carboxylic acids and dehydrating agents",
        "Distinguish primary, secondary and tertiary alcohols by their oxidation products and by tests",
    ],
    key_concepts=["Hydroxyl group", "Hydrogen bonding", "Fermentation", "Esterification", "Dehydration", "Oxidation of primary, secondary and tertiary alcohols", "Iodoform test"],
    blocks=[
        H("Introduction"),
        T("Palm wine, tapped from the oil palm or raffia palm and sold at roadside bars from Bamenda to Kumba, ferments within hours because yeast in the air turns the sugar of the sap into **ethanol**. Hand sanitiser, the fuel in a spirit lamp and the active ingredient of many drinks are all ethanol. Alcohols are a large family, and they are the central compounds that connect alkenes, haloalkanes, aldehydes, ketones and acids."),
        T("A word of caution: methanol, the simplest alcohol, is **highly poisonous**; badly made spirits can contain it and cause blindness or death. Never drink an unknown spirit or use laboratory alcohol in drinks."),
        H("Structure, classification and physical properties"),
        T("Alcohols have the functional group **-OH** (hydroxyl) attached to a saturated carbon, with the general formula [[!C_nH_{2n+1}OH]]. They are classified as primary, secondary or tertiary by the number of carbon atoms attached to the carbon that carries the -OH group (see the first lesson). Diols and triols have two or three -OH groups: ethane-1,2-diol (used in antifreeze) and propane-1,2,3-triol, **glycerol** (obtained when fats are hydrolysed)."),
        T("The O-H bond is polar and the oxygen has two lone pairs, so alcohol molecules form **hydrogen bonds** with each other. This explains why alcohols have much **higher boiling points** than alkanes or haloalkanes of similar relative molecular mass (ethanol 78 °C; propane, Mr 44, boils at −42 °C), and why the smallest alcohols are **soluble in water**: they hydrogen-bond with water molecules. Solubility falls as the non-polar carbon chain gets longer; methanol, ethanol and propanols mix with water in all proportions, but butan-1-ol is only slightly soluble."),
        H("Making alcohols"),
        KEY("Two routes to ethanol", "One uses a renewable sugar, the other uses ethene from crude oil.", cards=[
            ["Fermentation", "[[C6H12O6 -> 2C2H5OH + 2CO2]]. Yeast enzymes, warm (25 to 35 °C), no oxygen. The yeast is killed when the alcohol reaches about 15%, so distillation is needed to make stronger spirits. A slow, batch process giving impure ethanol from a renewable source."],
            ["Hydration of ethene", "[[C2H4 + H2O -> C2H5OH]]. Steam and ethene over a phosphoric acid catalyst at about 300 °C and 60 to 70 atm. A fast, continuous process giving pure ethanol, but it uses a non-renewable raw material (check your textbook for exact industrial conditions)."],
        ]),
        T("Other methods: hydrolysis of a haloalkane with aqueous hydroxide ([[CH3CH2Br + OH^- -> CH3CH2OH + Br^-]]) and reduction of aldehydes, ketones and carboxylic acids with reducing agents such as lithium aluminium hydride."),
        EX("Worked example 1: yield of ethanol", intro="90.0 g of glucose [[C6H12O6]] are fermented completely. Calculate the maximum mass of ethanol, and the mass obtained if the yield is 60%. (Ar: C 12, H 1, O 16.)", steps=[
            S("Moles of glucose", math=r"M_r = 6(12) + 12(1) + 6(16) = 180, \qquad n = \dfrac{90.0}{180} = 0.500\ \text{mol}"),
            S("Ratio 1 : 2", math=r"n(\mathrm{C_2H_5OH}) = 2 \times 0.500 = 1.00\ \text{mol}"),
            S("Maximum mass", math=r"M_r(\mathrm{C_2H_5OH}) = 46, \qquad m = 1.00 \times 46 = 46.0\ \text{g}"),
            S("At 60% yield", math=r"46.0 \times 0.60 = 27.6\ \text{g}"),
        ]),
        H("Reactions of alcohols"),
        T("The -OH group can react in three ways: the **O-H bond breaks** (acidic behaviour, esterification), the **C-O bond breaks** (replacement by halogen, dehydration), or the carbon is **oxidised**."),
        KEY("Four key reactions of ethanol", "Learn the reagent, the conditions and the observation.", cards=[
            ["With sodium", "[[2CH3CH2OH + 2Na -> 2CH3CH2ONa + H2]]. Effervescence; hydrogen released. Sodium ethoxide forms. Alcohols are much weaker acids than water, so the reaction is gentler than with water."],
            ["Replacement of -OH by halogen", "[[CH3CH2OH + PCl5 -> CH3CH2Cl + POCl3 + HCl]]: steamy fumes of HCl at room temperature (a test for -OH). Also SOCl2, or NaBr and concentrated [[H2SO4]], or red phosphorus and iodine."],
            ["Esterification", "[[CH3CH2OH + CH3COOH -> CH3COOCH2CH3 + H2O]]. Concentrated [[H2SO4]] catalyst, heat under reflux. Reversible. Product: ethyl ethanoate, a sweet-smelling ester."],
            ["Dehydration", "[[CH3CH2OH -> CH2=CH2 + H2O]]. Concentrated [[H2SO4]] at about 170 °C, or hot aluminium oxide. At about 140 °C with excess ethanol, an ether forms: [[2C2H5OH -> C2H5OC2H5 + H2O]]."],
        ]),
        T("**Dehydration mechanism (secondary and tertiary alcohols).** The acid protonates the oxygen of -OH (a lone pair on O accepts H⁺). Water leaves, giving a carbocation, and a base removes H⁺ from a neighbouring carbon to form the C=C. This is an E1 elimination. If two alkenes are possible the more substituted one is the major product."),
        H("Oxidation: primary, secondary and tertiary"),
        T("The oxidising agent is **acidified potassium dichromate(VI)**, [[K2Cr2O7]] with dilute sulfuric acid. The orange [[Cr2O7^2-]] ion is reduced to the green [[Cr^3+]] ion, so a colour change from orange to green shows that oxidation has taken place. (Acidified potassium manganate(VII) can also be used: purple to colourless.) What forms depends on the type of alcohol:"),
        IMG("al-chl3-alcohol-oxidation.svg", alt="Scheme: ethanol is oxidised to ethanal then ethanoic acid; propan-2-ol is oxidised to propanone; 2-methylpropan-2-ol is not oxidised.", caption="Figure 1. Oxidation of primary, secondary and tertiary alcohols."),
        T("A **primary** alcohol is oxidised first to an **aldehyde** and then to a **carboxylic acid**. To collect the aldehyde, **distil** it off as it forms (aldehydes have lower boiling points than alcohols because they cannot hydrogen-bond); to make the acid, **heat under reflux** with excess oxidant. A **secondary** alcohol gives a **ketone**, which resists further oxidation. A **tertiary** alcohol has no hydrogen on the carbon bearing -OH and is **not oxidised** (the orange colour stays)."),
        F(r"3\mathrm{CH_3CH_2OH} + \mathrm{Cr_2O_7^{2-}} + 8\mathrm{H^+} \rightarrow 3\mathrm{CH_3CHO} + 2\mathrm{Cr^{3+}} + 7\mathrm{H_2O}", title="Ethanol to ethanal (distillation)"),
        F(r"3\mathrm{CH_3CH_2OH} + 2\mathrm{Cr_2O_7^{2-}} + 16\mathrm{H^+} \rightarrow 3\mathrm{CH_3COOH} + 4\mathrm{Cr^{3+}} + 11\mathrm{H_2O}", title="Ethanol to ethanoic acid (reflux, excess oxidant)"),
        H("Tests to distinguish alcohols"),
        KEY("Useful tests", "Always give the reagent, the conditions and the observation.", cards=[
            ["Primary, secondary or tertiary?", "Warm with acidified [[K2Cr2O7]]. Orange to green: primary or secondary. No change: tertiary. To separate primary from secondary, distil off the product and test it: an aldehyde gives a silver mirror with Tollens' reagent (or a brick-red precipitate with Fehling's solution); a ketone does not."],
            ["Iodoform test", "Warm with iodine and aqueous sodium hydroxide. A **yellow precipitate of iodoform** [[CHI3]] forms with ethanol and with alcohols containing [[CH3CH(OH)-]], such as propan-2-ol. It is not given by propan-1-ol."],
            ["Alcohol or phenol?", "A phenol gives a violet colour with neutral iron(III) chloride; an alcohol does not (phenols come in a later lesson)."],
        ]),
        EX("Worked example 2: identify an isomer of [[C3H8O]]", intro="Three isomers have the formula [[C3H8O]]. Compound X does not react with sodium. Compound Y reacts with sodium, is oxidised by acidified dichromate to a product that gives a silver mirror with Tollens' reagent. Compound Z reacts with sodium and is oxidised to a product that does not give a silver mirror but forms a yellow precipitate with iodine and sodium hydroxide. Identify X, Y and Z.", steps=[
            S("List the isomers", text="Propan-1-ol, propan-2-ol and methoxyethane."),
            S("X: no reaction with sodium", text="No -OH group, so X is the ether **methoxyethane** [[CH3OCH2CH3]]."),
            S("Y: alcohol oxidised to an aldehyde", text="A silver mirror means an aldehyde, formed from a primary alcohol: Y is **propan-1-ol** [[CH3CH2CH2OH]], giving propanal."),
            S("Z: oxidised to a ketone", text="No silver mirror but a positive iodoform test: a methyl ketone, propanone, from a secondary alcohol. Z is **propan-2-ol** [[CH3CH(OH)CH3]]."),
        ]),
        EX("Worked example 3: products of oxidation of the isomers of [[C4H10O]]", intro="Name the product of heating each alcohol under reflux with excess acidified potassium dichromate(VI): (a) butan-1-ol, (b) butan-2-ol, (c) 2-methylpropan-2-ol.", steps=[
            S("(a) Primary", text="Butan-1-ol is oxidised to butanal and then to **butanoic acid** [[CH3CH2CH2COOH]]."),
            S("(b) Secondary", text="Butan-2-ol is oxidised to **butanone** [[CH3COCH2CH3]]. It cannot be oxidised further."),
            S("(c) Tertiary", text="2-Methylpropan-2-ol is **not oxidised**: the carbon with the -OH group has no hydrogen. The solution stays orange."),
        ]),
        H("Common mistakes"),
        MISTAKE("Using reflux when the aldehyde is wanted", "If you heat a primary alcohol under reflux with excess oxidant, the aldehyde is oxidised on to the acid. To get the aldehyde, distil it off as it forms."),
        MISTAKE("Saying a tertiary alcohol is oxidised to a ketone", "A tertiary alcohol has no H on the C-OH carbon, so it cannot lose H and form C=O without breaking a C-C bond. There is no reaction under mild conditions."),
        MISTAKE("Writing 'the solution turns clear' or 'colourless' for dichromate", "The orange dichromate ion turns **green** as it forms [[Cr^3+]]. Say 'orange to green'."),
        MISTAKE("Forgetting that esterification is reversible", "Use the reversible arrow, a concentrated sulfuric acid catalyst and reflux. Removing water or using excess of one reactant increases the yield."),
        QUIZ("Which alcohol is **not** oxidised by hot acidified potassium dichromate(VI)?", ["Butan-1-ol", "Butan-2-ol", "2-Methylpropan-1-ol", "2-Methylpropan-2-ol"], 3,
             "2-Methylpropan-2-ol is tertiary: the carbon bonded to -OH carries no hydrogen atom, so it cannot be oxidised.",
             feedback=["Primary alcohols are oxidised to aldehydes and acids.", "Secondary alcohols are oxidised to ketones.", "This is a primary alcohol (the C-OH carbon is attached to one carbon), so it is oxidised.", ""]),
        QUIZ("When ethanol is warmed with an excess of acidified potassium dichromate(VI) under reflux, the organic product is", ["ethanal", "ethanoic acid", "ethene", "ethyl ethanoate"], 1,
             "Reflux with excess oxidant oxidises the ethanol first to ethanal and then on to ethanoic acid.",
             feedback=["Ethanal forms first, but under reflux it is oxidised further.", "", "Ethene would need dehydration with concentrated sulfuric acid.", "An ester needs a carboxylic acid and an alcohol with an acid catalyst."]),
        H("Practice questions"),
        PQ("Explain why ethanol (boiling point 78 °C) has a much higher boiling point than ethane (-89 °C) and why it dissolves in water.",
           "Ethanol molecules have a polar O-H bond and lone pairs on oxygen, so they form hydrogen bonds with each other, which need a lot of energy to break. Ethane has only weak instantaneous dipole-induced dipole forces. Ethanol dissolves in water because its -OH group forms hydrogen bonds with water molecules; the energy released balances the energy needed to separate the molecules."),
        PQ("Compare the preparation of ethanol by fermentation and by hydration of ethene. Give two differences.",
           "Fermentation uses glucose (a renewable raw material), enzymes of yeast, about 25 to 35 °C, no oxygen, and is a slow batch process giving dilute impure ethanol that needs distillation. Hydration uses ethene (from crude oil, non-renewable) and steam with a phosphoric acid catalyst at about 300 °C and 60 to 70 atm; it is a fast continuous process giving pure ethanol."),
        PQ("Compound W is a liquid with formula [[C4H10O]]. It reacts with sodium. On warming with acidified dichromate it gives a product that does not give a silver mirror but gives a yellow precipitate with iodine and alkali. Identify W, and write the equation for the oxidation using [O] for the oxidising agent.",
           "W reacts with sodium, so it contains -OH. A product with no silver mirror but a positive iodoform test is a methyl ketone, so W is a secondary alcohol with the [[CH3CH(OH)-]] group: butan-2-ol [[CH3CH(OH)CH2CH3]]. Oxidation: [[CH3CH(OH)CH2CH3 + O -> CH3COCH2CH3 + H2O]]; the product is butanone."),
        PQ("Describe a test that distinguishes propan-1-ol from propan-2-ol, and give the observations.",
           "Method 1: warm each with iodine and sodium hydroxide solution; propan-2-ol gives a yellow precipitate of iodoform, propan-1-ol does not. Method 2: warm each with acidified dichromate and distil off the product; the propanal from propan-1-ol gives a silver mirror with Tollens' reagent, the propanone from propan-2-ol does not. Both alcohols turn dichromate from orange to green, so that test alone does not distinguish them."),
        TIP("In the exam: alcohols are a favourite in Paper 1 (class of alcohol, oxidation products, tests, the 2023 report lists questions on distinguishing primary from secondary alcohols and on alcohols and phenols) and in Paper 2, which can ask you to identify an isomer of [[C3H8O]] from reagents and give the products. Always state the reagent, the conditions (reflux or distil) and the observation."),
        H("Summary"),
        SUM("Alcohols have -OH. Hydrogen bonding gives them high boiling points and, for small alcohols, solubility in water.",
            "Ethanol is made by fermentation of glucose (yeast, 25 to 35 °C) and by hydration of ethene (steam, [[H3PO4]], about 300 °C, high pressure).",
            "Reactions: sodium gives hydrogen; [[PCl5]], [[SOCl2]] or HBr give haloalkanes; carboxylic acids give esters (reversible, acid catalyst); concentrated [[H2SO4]] at 170 °C gives alkenes.",
            "Acidified dichromate: primary gives aldehyde (distil) then acid (reflux); secondary gives ketone; tertiary is not oxidised. Orange turns green.",
            "Iodoform (yellow precipitate) is positive for ethanol and for [[CH3CH(OH)-]] alcohols, not for propan-1-ol."),
    ])]
# ============================================================================================
# Examination module: Paper 1
# ============================================================================================
LESSONS += [lesson(
    module=M_EXAM, topic="Paper 1",
    title="Paper 1 technique: multiple-choice strategy for Lower Sixth Chemistry",
    slug="chxl-paper-1-multiple-choice-strategy", minutes=22,
    summary="Paper 1 is 50 multiple-choice questions across the whole syllabus. Learn the three question formats, a first-pass and second-pass method, quick calculation checks, and how to revise the seven Lower Sixth modules.",
    objectives=[
        "Recognise single-response, multiple-selection and assertion-reason questions and answer each correctly",
        "Use elimination, estimation and unit checks to avoid calculation traps",
        "Plan time across 50 questions and revise by module",
        "Apply the key formulae of the seven Lower Sixth Chemistry modules quickly",
    ],
    key_concepts=["Single response", "Multiple selection", "Assertion-reason", "Elimination", "Unit check", "Time plan"],
    blocks=[
        H("Introduction"),
        T("Paper 1 of A Level Chemistry (0715) is made up of **50 multiple-choice questions**, and the Board's 2023 subject report says it covers the whole syllabus and is machine scored. That has one consequence you can use straight away: only the **letter you choose** counts, not your working, so your method must be fast and safe."),
        T("The same report describes the 2023 paper as mostly **single-response** questions, with some **multiple-selection** questions and some **assertion-reason** questions, and says about 40% of the questions were on physical and general chemistry, about 28% on inorganic chemistry and about 32% on organic chemistry. It also says nine of the fifty needed a calculation. Treat these figures as a guide to emphasis, not as a promise for your paper. In the Lower Sixth the seven modules feed the physical and general chemistry and the organic parts."),
        KEY("Three question formats", "Read the instructions printed on your own paper; the key below is the usual pattern.", cards=[
            ["Single response", "Four options, one correct. Choose the best answer."],
            ["Multiple selection", "Several numbered statements (1, 2, 3). You decide which are correct and choose the option that lists the right combination, for example: 1 and 2 only; 2 and 3 only."],
            ["Assertion-reason", "An assertion and a reason. You decide whether each is true, and if both are true, whether the reason **explains** the assertion."],
        ]),
        H("A method that works"),
        D("1. **Read the stem twice** and underline words such as NOT, ONLY, MOST, LEAST, at rtp, at stp.\n\n2. **Predict** the answer before you look at the options.\n\n3. **Eliminate** options you know are wrong; wrong options are built from typical mistakes.\n\n4. For calculations, **estimate first** (is the answer larger or smaller than the numbers given?) and **check the unit** (cm³ or dm³, g or kg, kJ or J).\n\n5. **Mark** your first-pass answer, flag any question that takes more than about two minutes, and **return** to it later.", title="Five steps for each question"),
        T("In the KKEVO practice mock, 90 minutes are given for 50 questions, which is a KKEVO practice setting (about 1.8 minutes a question). A good plan is a first pass at about one minute per question, answering every question you can do at once, then a second pass on the flagged ones. Keep five minutes at the end to check that every question has an answer. Check the instructions on your paper about wrong answers; if no penalty is stated, answer every question."),
        EX("Worked example 1: a calculation question (single response)", intro="0.40 g of a volatile liquid is vaporised and occupies 120 cm³ at 373 K and 100 kPa. Which value is closest to its relative molecular mass? (R = 8.314 J mol⁻¹ K⁻¹) A 52   B 103   C 207   D 1.03 × 10⁵", steps=[
            S("Convert the units to SI", math=r"P = 100\,000\ \text{Pa}, \quad V = 120\ \text{cm}^3 = 1.20\times10^{-4}\ \text{m}^3"),
            S("Rearrange $PV = nRT$ with $n = m/M$", math=r"M = \dfrac{mRT}{PV} = \dfrac{0.40 \times 8.314 \times 373}{100\,000 \times 1.20\times10^{-4}}"),
            S("Calculate", math=r"M = \dfrac{1240}{12.0} = 103\ \text{g/mol}", text="Answer **B**. Option D comes from using the pressure in kPa without converting to Pa; A and C come from halving or doubling."),
        ]),
        EX("Worked example 2: multiple selection", intro="Which of these species have a bond angle of about 109.5°? 1 [[CH4]]   2 [[NH4^+]]   3 [[H2O]]. Options: A 1, 2 and 3   B 1 and 2 only   C 2 and 3 only   D 1 only.", steps=[
            S("Test statement 1", text="[[CH4]] has four bonding pairs and no lone pairs: tetrahedral, 109.5°. **True**."),
            S("Test statement 2", text="[[NH4^+]] has four bonding pairs and no lone pairs: tetrahedral, 109.5°. **True**."),
            S("Test statement 3", text="[[H2O]] has two bonding pairs and two lone pairs. Lone pairs repel more strongly, so the angle is about 104.5°. **False**."),
            S("Choose the combination", text="Only 1 and 2 are correct: answer **B**."),
        ]),
        EX("Worked example 3: assertion-reason", intro="Assertion: But-1-ene shows geometric (cis-trans) isomerism. Reason: rotation about a C=C double bond is restricted. Decide whether each statement is true, and whether the reason explains the assertion.", steps=[
            S("Assertion", text="But-1-ene [[CH2=CHCH2CH3]] has two H atoms on one carbon of the C=C, so it does **not** show geometric isomerism. The assertion is **false**."),
            S("Reason", text="Rotation about C=C is restricted because the pi bond would have to break. The reason is **true**."),
            S("Conclusion", text="Assertion false, reason true. Choose the option that says exactly this. The reason is a correct statement, but it does not rescue a false assertion."),
        ]),
        EX("Worked example 4: an energetics calculation", intro="Using standard enthalpies of formation (kJ/mol): [[CO2(g)]] −394, [[H2O(l)]] −286, [[C2H5OH(l)]] −277, calculate the standard enthalpy of combustion of ethanol. A −1369   B −1011   C +1369   D −803", steps=[
            S("Write the equation", math=r"\mathrm{C_2H_5OH(l)} + 3\mathrm{O_2(g)} \rightarrow 2\mathrm{CO_2(g)} + 3\mathrm{H_2O(l)}"),
            S("Products minus reactants", math=r"\Delta H = [2(-394) + 3(-286)] - [(-277) + 0] = -1646 + 277 = -1369\ \text{kJ/mol}"),
            S("Answer", text="**A**. Option B comes from forgetting the factor 3 for water; C from reversing the subtraction sign; O₂ contributes 0 because it is an element."),
        ]),
        H("Formulae and facts to know quickly"),
        CODE("""Module                  Quick-recall items
Mole and titrations     n = m/M, n = cV, PV = nRT, ratios from the equation,
                        MnO4- : Fe2+ = 1 : 5, S2O3 2- : I2 = 2 : 1
Atomic structure        electron configuration order, ionisation energy trends,
                        isotopes and relative atomic mass from mass spectra
Bonding                 VSEPR shapes and angles, sigma and pi, sp / sp2 / sp3,
                        hydrogen bonding, dipole moments
States of matter        real gases deviate at high pressure / low temperature,
                        unit-cell counts and coordination numbers
Energetics              Hess's law, bond energies, lattice energy cycle,
                        delta G = delta H - T delta S
Equilibria              Kc, Kp expressions, Le Chatelier, Raoult's law, KD
Organic                 naming, isomers, mechanisms, tests and conditions""", "text", title="Lower Sixth quick-recall sheet"),
        H("Common mistakes"),
        MISTAKE("Missing NOT and ONLY", "A stem that says 'Which statement is NOT correct?' reverses the task. Underline the word before you read the options, and re-read it before you choose."),
        MISTAKE("Leaving a unit conversion until the end", "Convert cm³ to dm³ and grams to moles at the start. Many wrong options are built from forgetting that 1 dm³ = 1000 cm³."),
        MISTAKE("Choosing the first option that looks right", "Wrong options are deliberately attractive. Read all four before you choose, especially when two look similar."),
        MISTAKE("Rounding too early", "Carry at least one extra figure in the working and round at the end; options are often close in value."),
        QUIZ("In an assertion-reason question you decide that the assertion is true and the reason is true. What must you check next?", ["Whether the reason is written in the same units", "Whether the reason correctly explains the assertion", "Whether the assertion is a definition", "Nothing: choose the first option"], 1,
             "If both statements are true you must check whether the reason is the correct explanation of the assertion. Two true statements can be unrelated.",
             feedback=["Units are not part of this step.", "", "Whether it is a definition is irrelevant.", "The options differ exactly in whether the reason explains the assertion."]),
        QUIZ("The question asks for the volume of gas in cm³, but your working gives 0.0240 dm³. What should you choose?", ["0.0240", "2.40", "24.0", "240"], 2,
             "1 dm³ = 1000 cm³, so 0.0240 dm³ = 24.0 cm³.",
             feedback=["This is the volume in dm³. The question asks for cm³.", "This multiplies by 100, not 1000.", "", "This multiplies by 10 000."]),
        H("Practice questions"),
        PQ("20.0 cm³ of 0.100 mol/dm³ hydrochloric acid are neutralised by barium hydroxide solution of concentration 0.0500 mol/dm³. What volume of barium hydroxide is needed? A 10.0 cm³   B 20.0 cm³   C 40.0 cm³   D 5.00 cm³",
           "[[Ba(OH)2 + 2HCl -> BaCl2 + 2H2O]]. n(HCl) = 0.100 × 0.0200 = 2.00 × 10⁻³ mol. n(Ba(OH)2) = half = 1.00 × 10⁻³ mol. V = 1.00 × 10⁻³ / 0.0500 = 0.0200 dm³ = 20.0 cm³. Answer B. (A comes from using the 1 : 1 ratio; C from doubling.)"),
        PQ("Which of these molecules contains at least one pi bond? 1 [[CH2=CH2]]   2 [[CH3C#CH]]   3 [[CH3CH3]]. A 1, 2 and 3   B 1 and 2 only   C 2 and 3 only   D 1 only",
           "Ethene has a C=C (one sigma, one pi). Propyne has a C≡C (one sigma, two pi). Ethane has only sigma bonds. Statements 1 and 2 are correct: B."),
        PQ("Assertion: Ethanol has a higher boiling point than methoxymethane. Reason: Ethanol molecules form hydrogen bonds with each other. Is each statement true, and does the reason explain the assertion?",
           "Both statements are true (ethanol about 78 °C, methoxymethane about −24 °C). Ethanol has an O-H group and its molecules hydrogen-bond; methoxymethane has no O-H, so it has only weaker forces. The reason explains the assertion: choose 'both true and the reason is a correct explanation'."),
        PQ("A hydrocarbon is 85.7% carbon by mass and its relative molecular mass is 56. Find its molecular formula. (Ar: C 12, H 1) A [[CH2]]   B [[C2H4]]   C [[C4H8]]   D [[C4H10]]",
           "Percentage of H = 14.3%. Moles in 100 g: C = 85.7/12 = 7.14, H = 14.3/1 = 14.3. Ratio C : H = 1 : 2, empirical formula [[CH2]] (mass 14). 56/14 = 4, so the molecular formula is [[C4H8]]: C."),
        TIP("In the exam: Paper 1 is machine scored, so shade or mark your answers clearly and check that the number you answer matches the question number. Quick revision tool: after each module, do ten multiple-choice questions on it, mark them, and write down why each wrong option was wrong."),
        H("Summary"),
        SUM("Paper 1 has 50 multiple-choice questions on the whole syllabus; the Board's 2023 report describes single-response, multiple-selection and assertion-reason questions.",
            "For every question: read twice, predict, eliminate, then estimate and check units.",
            "In multiple selection, test each statement separately, then choose the matching combination. In assertion-reason, check each statement, then whether the reason explains the assertion.",
            "Plan time: a quick first pass, flagged questions in a second pass, and a final check that every question has an answer.",
            "Revise by module with short timed sets and learn from every wrong option."),
    ])]
# ============================================================================================
# Examination module: Paper 2
# ============================================================================================
LESSONS += [lesson(
    module=M_EXAM, topic="Paper 2",
    title="Paper 2 technique: answering structured theory questions in Chemistry",
    slug="chxl-paper-2-structured-questions", minutes=25,
    summary="Paper 2 is a structured theory paper of six questions in three sections. Learn what the command words ask, how to set out calculations, structures, equations, mechanisms and tests, and how to avoid the errors the Board's report records.",
    objectives=[
        "Explain what each command word demands and match the length of your answer to the marks",
        "Set out calculations with working, units and correct significant figures",
        "Write structures, balanced equations, curly-arrow mechanisms and test descriptions to examination standard",
        "Use the Board's report on common errors to plan revision for physical and organic chemistry",
    ],
    key_concepts=["Command words", "Showing working", "Balanced equations", "Curly arrows", "Test, observation, inference", "Common errors"],
    blocks=[
        H("Introduction"),
        T("Paper 2 of A Level Chemistry (0715) is the **structured theory paper**. The Board's 2023 subject report describes it as six questions in three sections: **A, physical and general chemistry; B, inorganic chemistry; C, organic chemistry**, with two compulsory questions in each section. It carries about 35% of the whole examination. In the Lower Sixth you meet the physical and general chemistry and the organic chemistry; the inorganic section depends mainly on the Upper Sixth course."),
        T("A structured question is a chain of parts, (a), (b), (c) and so on, with the later parts often depending on the earlier ones. Marks are given for method, for correct statements and for clear working, so a half-correct answer still earns marks if you show your reasoning."),
        H("Command words: what the question is asking"),
        CODE("""State, Name     Give the answer only; no explanation needed.
Define          Give the exact meaning; every key word of the definition counts.
Explain         Give a reason: cause, then effect, using chemical ideas.
Suggest         Apply what you know to an unfamiliar case; reasoning is marked.
Deduce          Work out an answer from the information given; show the steps.
Calculate       Show working, give the answer with correct unit and sig. figs.
Describe        Give the observations or the steps in order.
Draw            Make a clear diagram or structure with every bond that matters.
Distinguish     Give a test, with reagent, conditions and BOTH results.
Outline         A short, ordered account of the main steps.""", "text", title="Common command words"),
        TIP("The number of marks tells you how many separate points to make. A 2-mark 'explain' needs two linked statements, not one. A 1-mark 'state' needs one precise statement."),
        H("Setting out a calculation"),
        D("1. Write the **balanced equation** (it gives the mole ratio).\n\n2. Convert to **moles** with n = m/M, n = cV or n = V/Vm.\n\n3. Use the **mole ratio** from the equation.\n\n4. Convert back to the quantity asked for.\n\n5. Give the **unit** and round the final answer to the **significant figures** of the least precise data.", title="The calculation chain"),
        H("What the Board's 2023 report says candidates lost marks on"),
        T("Without quoting from the report, its comments on Paper 2 point to these weak areas for Lower Sixth topics. Use them as a revision checklist."),
        KEY("Common weak points", "Each one is a skill you can practise.", cards=[
            ["Physical and general", "Calculating the molar mass of a volatile liquid; finding the molar volume of a gas from an equation; partial pressure from mole fraction; energetics calculations; naming crystal structures."],
            ["Organic: formulae", "Working out empirical and molecular formulae from data and then deducing the structure of an unknown compound."],
            ["Organic: isomers and mechanisms", "Writing optical isomers of an amino acid with wedge and dash bonds; the mechanism of alkaline hydrolysis of a haloalkane; naming and drawing the isomers of [[C3H8O]] and using reagents to decide which one is present."],
            ["Organic: tests", "Distinguishing ethane from ethene, propanal from propanone; defining hybridisation and giving an sp example."],
        ]),
        EX("Worked example 1: deduce a compound from data", intro="A liquid X contains 60.0% carbon, 13.3% hydrogen and 26.7% oxygen by mass. Its relative molecular mass is 60. X reacts with sodium to give hydrogen. When X is warmed with acidified potassium dichromate(VI) and the product distilled out, the product forms a silver mirror with Tollens' reagent. (a) Find the empirical and molecular formula. (b) Identify X. (c) Write an equation for the oxidation using [O].", steps=[
            S("(a) Divide each percentage by Ar", math=r"\text{C}: \dfrac{60.0}{12} = 5.00;\quad \text{H}: \dfrac{13.3}{1} = 13.3;\quad \text{O}: \dfrac{26.7}{16} = 1.67"),
            S("Divide by the smallest", math=r"\text{C} : \text{H} : \text{O} = 3 : 8 : 1", text="Empirical formula [[C3H8O]], mass 60, equal to the relative molecular mass, so the molecular formula is also [[C3H8O]]."),
            S("(b) Use the tests", text="Reaction with sodium: it has an -OH group, so it is an alcohol, not an ether. The oxidation product gives a silver mirror: it is an aldehyde, so X is a **primary alcohol**: propan-1-ol [[CH3CH2CH2OH]]."),
            S("(c) Equation", text="[[CH3CH2CH2OH + O -> CH3CH2CHO + H2O]]. The product is propanal."),
        ]),
        EX("Worked example 2: equilibrium and partial pressure", intro="At a certain temperature, an equilibrium mixture of [[N2O4]] and [[NO2]] contains 0.40 mol of [[N2O4]] and 0.60 mol of [[NO2]] at a total pressure of 200 kPa. [[N2O4(g)]] ⇌ [[2NO2(g)]]. (a) Calculate the partial pressure of each gas. (b) Write the expression for Kp and calculate its value.", steps=[
            S("(a) Mole fractions", math=r"x(\mathrm{N_2O_4}) = \dfrac{0.40}{1.00} = 0.40; \quad x(\mathrm{NO_2}) = 0.60"),
            S("Partial pressures", math=r"p(\mathrm{N_2O_4}) = 0.40 \times 200 = 80\ \text{kPa}; \quad p(\mathrm{NO_2}) = 0.60 \times 200 = 120\ \text{kPa}"),
            S("(b) Expression", math=r"K_p = \dfrac{p(\mathrm{NO_2})^2}{p(\mathrm{N_2O_4})}"),
            S("Calculation", math=r"K_p = \dfrac{(120)^2}{80} = 180\ \text{kPa}", text="The unit comes from kPa² / kPa = kPa."),
        ]),
        EX("Worked example 3: a mechanism answer", intro="Describe the mechanism of the hydrolysis of 2-bromo-2-methylpropane with aqueous sodium hydroxide. Name the mechanism.", steps=[
            S("Name and reasoning", text="2-Bromo-2-methylpropane is a tertiary haloalkane, so the mechanism is **SN1** (nucleophilic substitution, unimolecular), rate = k[RBr]."),
            S("Step 1 (slow)", text="The C-Br bond breaks heterolytically. A curly arrow starts at the middle of the C-Br bond and ends on Br. Products: the carbocation [[(CH3)3C^+]] and [[Br^-]]."),
            S("Step 2 (fast)", text="A lone pair on the oxygen of [[OH^-]] attacks the carbocation: a curly arrow from the lone pair to the carbon. Product: [[(CH3)3COH]], 2-methylpropan-2-ol."),
            S("Mark points", text="Correct name, a curly arrow from bond to Br, the carbocation, a curly arrow from the lone pair to C+, the final product."),
        ]),
        H("Equations, structures and tests"),
        KEY("Examiners' favourite details", "Small habits that earn marks.", cards=[
            ["Equations", "Balance atoms and charge. Add state symbols if asked. Use the correct formula for every species; do not write [[CO]] when you mean [[CO2]]."],
            ["Structures", "When asked for a displayed formula, show **every** atom and bond. In a skeletal or structural formula, put each atom in the right place (-OH on a carbon, not -HO). Draw wedges and dashes for optical isomers."],
            ["Mechanisms", "Curly arrows start at a lone pair or a bond; show charges and partial charges; draw the intermediate; name the mechanism."],
            ["Tests", "Give reagent, conditions, observation and inference, in that order. Say 'orange to green', not 'changes colour'."],
        ]),
        H("Common mistakes"),
        MISTAKE("Answering a different question", "Underline the command word and the quantity asked for. 'Calculate the mass' is not 'calculate the moles'."),
        MISTAKE("Lost units and wrong significant figures", "An answer without a unit usually loses a mark. Do not write 14.285714 mol; write 14.3 mol if the data have three significant figures."),
        MISTAKE("Writing 'it reacts' without evidence", "In a test, say what you see (effervescence, a colour change, a precipitate of a stated colour) and then what you infer (the compound is a carboxylic acid)."),
        MISTAKE("Leaving gaps in a mechanism", "The intermediate, the lone pair on the nucleophile and both arrows must be shown. An unsupported 'substitution happens' earns nothing."),
        QUIZ("Which is the correct way to present the final answer to a calculation with data to three significant figures?", ["0.0970", "0.097", "0.0970 mol/dm³", "0.09700000 mol/dm³"], 2,
             "A complete answer has the correct number of significant figures and a unit: 0.0970 mol/dm³.",
             feedback=["The unit is missing.", "The unit is missing and the figures are fewer than the data.", "", "Too many significant figures for data with three."]),
        QUIZ("A question says 'Distinguish between propanal and propanone.' Which answer earns full marks?", ["Propanal is an aldehyde and propanone is a ketone.", "Warm each with Tollens' reagent: propanal gives a silver mirror; propanone gives no change.", "Add water to each and see which dissolves.", "Heat both: propanal burns."], 1,
             "A distinguishing test needs a named reagent, conditions and both results.",
             feedback=["This restates the classes but gives no test.", "", "Both are soluble in water, so there is no difference.", "Both burn."]),
        H("Practice questions"),
        PQ("(a) Explain why the mole ratio from the equation is needed when calculating the volume of gas formed in a reaction. (b) 0.65 g of zinc reacts with excess dilute hydrochloric acid: [[Zn + 2HCl -> ZnCl2 + H2]]. Calculate the volume of hydrogen at rtp. (Ar: Zn 65; molar volume 24 dm³.)",
           "(a) The balanced equation shows the proportion in which substances react, so the moles of the unknown must be found from the moles of the known using that ratio. (b) n(Zn) = 0.65/65 = 0.010 mol. Ratio Zn : [[H2]] = 1 : 1, so n([[H2]]) = 0.010 mol. V = 0.010 × 24 = 0.24 dm³ (240 cm³)."),
        PQ("Compound Z has the formula [[C3H6O]]. It forms an orange precipitate with 2,4-dinitrophenylhydrazine and gives no silver mirror with Tollens' reagent. Name Z, draw its structure, and name another isomer of [[C3H6O]] which would give a silver mirror.",
           "The orange precipitate with 2,4-DNPH shows a carbonyl group (aldehyde or ketone). No silver mirror: not an aldehyde, so Z is a ketone: propanone [[CH3COCH3]]. The aldehyde isomer is propanal [[CH3CH2CHO]], which gives a silver mirror."),
        PQ("Draw the two enantiomers of alanine, [[CH3CH(NH2)COOH]], using wedge and dash bonds, and state what is meant by a chiral centre.",
           "Draw the central carbon with two bonds in the plane (for example [[COOH]] up and [[NH2]] to the left), one wedge bond to [[CH3]] and one dashed bond to H. The second enantiomer is the mirror image: swap the wedge and dashed groups (or put [[NH2]] on the right). A chiral centre is a carbon atom bonded to four different atoms or groups, which gives two non-superimposable mirror images."),
        PQ("An equilibrium mixture at 500 K contains 0.50 mol of [[N2]], 1.50 mol of [[H2]] and 0.20 mol of [[NH3]] at a total pressure of 100 atm. Calculate the partial pressure of each gas. [[N2 + 3H2 <=> 2NH3]]",
           "Total moles = 0.50 + 1.50 + 0.20 = 2.20 mol. Mole fractions: [[N2]] 0.227, [[H2]] 0.682, [[NH3]] 0.0909. Partial pressures: [[N2]] 22.7 atm, [[H2]] 68.2 atm, [[NH3]] 9.09 atm. (Check: they add up to 100 atm.)"),
        TIP("In the exam: before you write, scan the whole paper and answer the questions you are strongest in first, but keep your numbering clear. Use the marks beside each part to decide how much to write; leave a few minutes at the end to check units and structures."),
        H("Summary"),
        SUM("Paper 2 is a structured theory paper of six questions in three sections: physical and general, inorganic and organic. Lower Sixth supports A and C.",
            "The command word and the marks tell you what to write and how much; 'explain' needs a reason, 'distinguish' needs a test with both results.",
            "For calculations: balanced equation, moles, ratio, answer with unit and the right significant figures.",
            "Show every bond in displayed formulae, start curly arrows at lone pairs or bonds, and write tests as reagent, conditions, observation, inference.",
            "Revise the weak points the Board's report lists: gas calculations, energetics, empirical formula to structure, isomers, hydrolysis mechanism and distinguishing tests."),
    ])]
# ============================================================================================
# Examination module: Paper 3 (practical skills)
# ============================================================================================
LESSONS += [lesson(
    module=M_EXAM, topic="Paper 3",
    title="Paper 3 practical skills: titrations, thermometric titrations, qualitative tests and recording",
    slug="chxl-paper-3-practical-skills", minutes=28,
    summary="Paper 3 tests practical skills: volumetric and thermometric titrations with accurate recording and calculation, qualitative analysis of inorganic and organic unknowns with observations and inferences, and evaluation of errors.",
    objectives=[
        "Carry out and record a titration correctly, choose concordant results and calculate a concentration",
        "Analyse thermometric titration data by plotting two lines and extrapolating",
        "Perform and report qualitative tests for common cations, anions and organic functional groups as observation then inference",
        "Estimate percentage errors and suggest sensible improvements",
    ],
    key_concepts=["Concordant titres", "Recording tables", "Redox and acid-base titration", "Thermometric titration", "Observation and inference", "Percentage error"],
    blocks=[
        H("Introduction"),
        T("The Board's 2023 report says Paper 3 assesses practical skills rather than theory. It describes a **quantitative analysis** question, where candidates use titration data (weighing, measuring volumes with a burette and pipette, observing the end-point colour, recording readings and calculating concentrations), and a **qualitative analysis** question, where candidates identify unknown inorganic and organic substances from observations and inferences. The paper also includes school-based assessment of laboratory books and a project or field-trip report. The report also notes that students do better when practical work begins early in the Lower Sixth, so use every laboratory session."),
        T("In many schools the laboratory has limited equipment and a few shared burettes. Skills such as careful reading and clear tables cost nothing and earn marks, so practise them with whatever you have, and keep your laboratory book tidy because it is part of the assessment."),
        H("Volumetric analysis: technique"),
        IMG("al-chl3-titration-setup.svg", alt="Burette clamped on a stand above a conical flask standing on a white tile.", caption="Figure 1. A burette, conical flask and white tile."),
        D("1. **Rinse** the burette with a little of the titrant, the pipette with the solution it will measure, and the conical flask with distilled water only.\n\n2. Fill the burette, open the tap briefly to fill the jet, **remove the funnel**, and read the **bottom of the meniscus** at eye level.\n\n3. **Pipette** the fixed volume into the flask, add the indicator if needed.\n\n4. Do a **rough** titration, then accurate ones, adding the titrant **dropwise** near the end-point and swirling.\n\n5. Repeat until two or more results are **concordant** (within 0.10 cm³).", title="Titration method"),
        T("**Recording.** A burette is read to the nearest 0.05 cm³, so record every reading to **two decimal places**, ending in 0 or 5 (for example 24.30, not 24.3). Put units in the column headings and show initial reading, final reading and titre. Calculate the mean from the **concordant** results only and say which you used."),
        CODE("""Titration number          Rough    1       2       3
Final reading / cm3       25.10    24.40   48.55   24.35
Initial reading / cm3      0.00     0.10   24.30    0.10
Titre / cm3               25.10    24.30   24.25   24.25

Concordant: 24.30, 24.25, 24.25 (within 0.10 cm3)
Mean titre = (24.30 + 24.25 + 24.25) / 3 = 24.27 cm3""", "text", title="A model results table (teaching data)"),
        T("**End-points.** Potassium manganate(VII) is its own indicator: the end-point is the first **permanent pale pink**. The solution must be acidified with **dilute sulfuric acid**, not hydrochloric acid, because chloride ions would be oxidised by permanganate. In iodine-thiosulfate titrations, the iodine is titrated with sodium thiosulfate until the brown solution turns pale yellow; then starch is added, which turns it blue-black, and the titration continues until the blue colour **disappears**."),
        EX("Worked example 1: redox titration with manganate(VII)", intro="25.0 cm³ of an iron(II) solution are titrated with 0.0200 mol/dm³ potassium manganate(VII). The mean concordant titre is 24.25 cm³. [[MnO4^- + 8H^+ + 5Fe^2+ -> Mn^2+ + 5Fe^3+ + 4H2O]]. (a) Calculate the concentration of iron(II). (b) The solution came from dissolving a sample in water and making the volume up to 250 cm³. Calculate the mass of [[FeSO4.7H2O]] (Mr = 278) in the sample.", steps=[
            S("(a) Moles of manganate(VII)", math=r"n = 0.0200 \times \dfrac{24.25}{1000} = 4.85\times10^{-4}\ \text{mol}"),
            S("Ratio 1 : 5", math=r"n(\mathrm{Fe^{2+}}) = 5 \times 4.85\times10^{-4} = 2.425\times10^{-3}\ \text{mol}"),
            S("Concentration", math=r"c = \dfrac{2.425\times10^{-3}}{0.0250} = 0.0970\ \text{mol/dm}^3"),
            S("(b) Moles in 250 cm³", math=r"0.0970 \times 0.250 = 0.02425\ \text{mol}"),
            S("Mass", math=r"0.02425 \times 278 = 6.74\ \text{g}"),
        ]),
        EX("Worked example 2: iodometric titration", intro="Copper(II) ions react with excess iodide: [[2Cu^2+ + 4I^- -> 2CuI + I2]]; the iodine is titrated with thiosulfate: [[I2 + 2S2O3^2- -> 2I^- + S4O6^2-]]. 25.0 cm³ of a copper(II) solution need 20.40 cm³ of 0.100 mol/dm³ sodium thiosulfate. Find the concentration of copper(II).", steps=[
            S("Link the two equations", text="2 mol of [[Cu^2+]] give 1 mol of [[I2]], which needs 2 mol of thiosulfate. So [[Cu^2+]] : [[S2O3^2-]] = 1 : 1."),
            S("Moles of thiosulfate", math=r"0.100 \times \dfrac{20.40}{1000} = 2.040\times10^{-3}\ \text{mol}"),
            S("Concentration of copper(II)", math=r"c = \dfrac{2.040\times10^{-3}}{0.0250} = 0.0816\ \text{mol/dm}^3"),
        ]),
        H("Thermometric titration"),
        T("In a thermometric titration, one solution is added in portions to another and the **temperature** is recorded after each addition. For a neutralisation, the temperature rises until the acid and base are in the exact reacting ratio and then falls slowly as extra, cooler solution is added. Plot temperature (y) against volume added (x), draw **two best-fit straight lines** (the rising and the falling parts), and read the volume where they **intersect**: this is the volume at the **end-point**, and the temperature there is the corrected maximum."),
        CODE("""Volume of 2.00 mol/dm3 NaOH added / cm3 :   0     5     10    15    20    25    30    35    40
Temperature / deg C (teaching data)     :  25.0  28.0  31.0  34.0  37.0  37.9  37.4  36.9  36.4

Rising line   : T = 25.0 + 0.60 V
Falling line  : T = 40.4 - 0.10 V
Intersection  : 25.0 + 0.60 V = 40.4 - 0.10 V   ->   V = 22.0 cm3,  T = 38.2 deg C""", "text", title="Thermometric titration of 25.0 cm3 of hydrochloric acid"),
        EX("Worked example 3: use the two lines", intro="Using the data above: (a) find the concentration of the hydrochloric acid (25.0 cm³); (b) calculate the enthalpy of neutralisation. Assume density 1.00 g/cm³ and specific heat capacity 4.18 J g⁻¹ K⁻¹.", steps=[
            S("(a) Moles of NaOH at the end-point", math=r"n = 2.00 \times \dfrac{22.0}{1000} = 0.0440\ \text{mol}"),
            S("1 : 1 reaction, so moles of HCl", math=r"c(\mathrm{HCl}) = \dfrac{0.0440}{0.0250} = 1.76\ \text{mol/dm}^3"),
            S("(b) Temperature rise from the lines", math=r"\Delta T = 38.2 - 25.0 = 13.2\ \text{K}"),
            S("Heat released", math=r"q = mc\Delta T = 47.0 \times 4.18 \times 13.2 = 2593\ \text{J}"),
            S("Enthalpy per mole", math=r"\Delta H = -\dfrac{2593}{0.0440} = -58\,900\ \text{J/mol} \approx -58.9\ \text{kJ/mol}", text="The accepted value is about −57 kJ/mol; heat losses and rounding explain small differences."),
        ]),
        H("Qualitative analysis: observations and inferences"),
        T("Qualitative analysis is detective work. For each test write: the **test** (reagent and conditions), the **observation** (what you see, smell or hear) and the **inference** (what you conclude). Never write only the conclusion. Use exact colours and say whether a precipitate dissolves in excess."),
        CODE("""Cation   NaOH(aq)                           NH3(aq)
Cu2+     pale blue ppt, insoluble in excess   pale blue ppt; deep blue solution in excess
Fe2+     green ppt, turns brown on standing   green ppt, insoluble in excess
Fe3+     red-brown ppt, insoluble in excess   red-brown ppt, insoluble in excess
Zn2+     white ppt, soluble in excess         white ppt, soluble in excess
Pb2+     white ppt, soluble in excess         white ppt, insoluble in excess
Al3+     white ppt, soluble in excess         white ppt, insoluble in excess
Ca2+     white ppt, insoluble in excess       no ppt or only a trace
Mg2+     white ppt, insoluble in excess       white ppt, insoluble in excess
NH4+     no ppt; warm: NH3 gas (turns damp red litmus blue)

Flame tests: Na yellow, K lilac, Ca brick-red, Sr crimson, Ba apple-green, Cu blue-green""", "text", title="Tests for cations (summary)"),
        CODE("""Anion    Test and observation
CO3 2-   dilute acid: effervescence; gas turns limewater milky (CO2)
SO4 2-   acidify with dilute HCl, add BaCl2(aq): white ppt
Cl-      dilute HNO3, then AgNO3(aq): white ppt, soluble in dilute NH3
Br-      same test: cream ppt, soluble only in concentrated NH3
I-       same test: yellow ppt, insoluble in NH3
S2O3 2-  dilute HCl: pale yellow ppt of sulfur and a choking smell of SO2
CrO4 2-  yellow solution; add dilute acid: turns orange (Cr2O7 2-)
NO3-     warm with NaOH(aq) and aluminium foil: NH3 gas given off""", "text", title="Tests for anions (summary)"),
        CODE("""Test                                      Positive result and meaning
Bromine water                             orange to colourless: C=C (alkene)
Acidified KMnO4, cold                     purple to colourless: C=C or an easily oxidised group
NaHCO3(aq) or Na2CO3(aq)                  effervescence of CO2: carboxylic acid
Na metal (dry sample)                     bubbles of H2: -OH (alcohol or acid)
Acidified K2Cr2O7, warm                   orange to green: primary or secondary alcohol, aldehyde
Tollens' reagent, warm                    silver mirror: aldehyde (and methanoic acid)
2,4-DNPH                                  orange precipitate: aldehyde or ketone
I2 + NaOH(aq), warm                       yellow precipitate: CH3CO- or CH3CH(OH)- group
Neutral FeCl3(aq)                         violet colour: phenol""", "text", title="Tests for organic compounds (summary)"),
        T("Two cases that need care. **Methanoic acid** [[HCOOH]] is an acid (effervescence with carbonate), but it also behaves like an aldehyde: it decolourises acidified permanganate and gives a silver mirror. **Maleic acid** [[HOOCCH=CHCOOH]] is a dicarboxylic acid with a C=C: it gives effervescence with carbonate **and** decolourises bromine water. Benzoic acid is a white solid, effervesces with carbonate and does not decolourise bromine water."),
        EX("Worked example 4: write observation and inference", intro="A white solid S dissolves in water. (i) Dilute hydrochloric acid gives an effervescence of a colourless gas that turns limewater milky. (ii) NaOH(aq) gives a white precipitate that dissolves in excess NaOH. (iii) NH3(aq) gives a white precipitate that dissolves in excess. Suggest the ions present.", steps=[
            S("(i) Observation to inference", text="Effervescence and milky limewater: the gas is [[CO2]], so a **carbonate** anion is present."),
            S("(ii) and (iii) Precipitate soluble in both reagents", text="White precipitate soluble in excess NaOH and in excess NH3: [[Zn^2+]] (Al³⁺ and Pb²⁺ dissolve only in NaOH)."),
            S("Conclusion", text="S is probably zinc carbonate, though a careful report would add a flame test or another test to confirm."),
        ]),
        H("Errors and evaluation"),
        T("Every measuring instrument has an uncertainty. A burette reading has an uncertainty of about ±0.05 cm³; a titre is the difference of two readings, so the uncertainty is ±0.10 cm³. The **percentage error** is the uncertainty divided by the measured value. For a titre of 24.25 cm³: 0.10 / 24.25 × 100 = 0.41%. For a balance reading to ±0.01 g, weighing by difference (two readings) gives ±0.02 g: on 1.50 g, that is 1.3%. To reduce the percentage error, use a **larger** mass or volume. Other improvements: repeat and average, use a more precise instrument (burette instead of measuring cylinder), swirl, use a white tile, and insulate a thermometric titration (polystyrene cup with a lid)."),
        H("Common mistakes"),
        MISTAKE("Poor recording", "Readings to one decimal place, missing units, a table without headings, or a final answer with different precision from the data all lose marks. Record every burette reading to 0.05 cm³ (two decimal places)."),
        MISTAKE("Averaging all the titres", "Rough titres and results that are not concordant are not used in the mean. Say which values you averaged."),
        MISTAKE("Writing only the conclusion", "'Contains copper' is not an observation. Write 'pale blue precipitate, insoluble in excess' and then 'Cu²⁺ is present'."),
        MISTAKE("Using hydrochloric acid with permanganate", "Chloride ions react with permanganate and give a titre that is too large. Use dilute sulfuric acid."),
        QUIZ("A student records burette readings as 24.3 cm³ and 0.1 cm³. What is wrong?", ["Nothing: one decimal place is enough", "The readings should be recorded to two decimal places, ending in 0 or 5 (for example 24.30 and 0.10)", "The initial reading should always be 0.00", "The readings must be in dm³"], 1,
             "A burette is read to ±0.05 cm³, so readings are recorded to two decimal places.",
             feedback=["One decimal place hides the half-division reading.", "", "The initial reading need not be zero; record whatever it is.", "Titres are recorded in cm³."]),
        QUIZ("A white precipitate forms with NaOH(aq) and dissolves in excess NaOH, but does not dissolve in excess NH3. The cation is most likely", ["Zn²⁺", "Mg²⁺", "Al³⁺", "Cu²⁺"], 2,
             "Al³⁺ dissolves in excess NaOH but not in NH3. Zn²⁺ dissolves in both; Mg²⁺ dissolves in neither; Cu²⁺ gives a blue precipitate.",
             feedback=["Zinc hydroxide also dissolves in excess ammonia.", "Magnesium hydroxide does not dissolve in excess NaOH.", "", "Copper(II) gives a blue, not a white, precipitate."]),
        H("Practice questions"),
        PQ("In a titration, 25.0 cm³ of sulfuric acid need 22.50 cm³ of 0.100 mol/dm³ sodium hydroxide: [[H2SO4 + 2NaOH -> Na2SO4 + 2H2O]]. Calculate the concentration of the acid.",
           "n(NaOH) = 0.100 × 0.02250 = 2.250 × 10⁻³ mol. Ratio [[H2SO4]] : NaOH = 1 : 2, so n([[H2SO4]]) = 1.125 × 10⁻³ mol. c = 1.125 × 10⁻³ / 0.0250 = 0.0450 mol/dm³."),
        PQ("Four titres are 26.10 (rough), 24.85, 24.80 and 25.30 cm³. Which are used for the mean? Calculate it.",
           "The rough titre and 25.30 are not concordant with 24.85 and 24.80 (within 0.10 cm³). The mean of 24.85 and 24.80 is 24.825, recorded as 24.83 cm³. Good practice is to repeat once more to confirm."),
        PQ("A solution Q gives a pale blue precipitate with aqueous ammonia that dissolves in excess to give a deep blue solution. Acidified barium chloride gives a white precipitate. Identify the ions and write the observation-inference table.",
           "Test: NH3(aq) added dropwise then in excess; observation: pale blue precipitate dissolving to a deep blue solution; inference: [[Cu^2+]] is present. Test: dilute HCl then [[BaCl2(aq)]]; observation: white precipitate; inference: sulfate [[SO4^2-]] is present. Q is probably copper(II) sulfate."),
        PQ("A burette is read to ±0.05 cm³ and the titre is 20.00 cm³. Calculate the percentage error and suggest one way to reduce it.",
           "The titre uses two readings, so the uncertainty is ±0.10 cm³. Percentage error = 0.10/20.00 × 100 = 0.50%. To reduce it, use a larger titre (for example a more dilute titrant, so that more is needed) so that the same ±0.10 cm³ is a smaller fraction."),
        TIP("In the exam: for quantitative analysis, set out every reading in a clean table with units, show your mean, equation, moles and concentration. For qualitative analysis, work through each test on a fresh sample, write what you see, and only then what you infer. Keep your laboratory book up to date; it counts in the school-based assessment."),
        H("Summary"),
        SUM("Paper 3 tests practical skills: a quantitative analysis question, a qualitative analysis question and school-based assessment of laboratory books and projects.",
            "Rinse correctly, read the meniscus at eye level, record burette readings to two decimal places, use concordant titres (within 0.10 cm³) for the mean.",
            "Permanganate is acidified with dilute sulfuric acid and self-indicates (permanent pale pink); starch is added late in iodine-thiosulfate titrations.",
            "Thermometric titration: plot two lines and take the intersection for the end-point volume and the corrected temperature rise.",
            "In qualitative analysis write test, observation, inference. Percentage error = uncertainty / measurement × 100; reduce it with larger quantities and more precise apparatus."),
    ])]

LESSONS = _walk(LESSONS)
