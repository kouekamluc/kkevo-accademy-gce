"""Lower Sixth Chemistry (A Level 0715): practice sets for Foundations of Organic Chemistry and the Examination module (mocks).

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


SETS = []

# ------------------------------------------------------------------ Topic 1, lesson 1: classification
SETS += [practice_set(
    module=M_ORG, topic="Classification and IUPAC nomenclature",
    title="Homologous series, functional groups and classification", lesson="chl3-classification-functional-groups",
    questions=[
        MC("Which group is the functional group of a carboxylic acid?", [
            C("-CHO", why="This is the aldehyde group: a C=O carbon with one hydrogen, no -OH."),
            C("-COOH", correct=True),
            C("-COO- (inside the chain)", why="This is the ester group: the oxygen is joined to a second carbon group, not to hydrogen."),
            C("-OH on a carbon chain", why="A hydroxyl group alone is an alcohol. An acid has the -OH attached to a C=O carbon."),
        ], steps=[S("Recall the group", text="A carboxylic acid contains a carbonyl group C=O and a hydroxyl group -OH on the **same** carbon: -COOH.")],
           concept="Functional groups", skill="Recall", hint="The name carboxylic acid joins 'carbonyl' and 'hydroxyl'.",
           feedback="Correct: -COOH combines C=O and -OH on one carbon."),
        MC("Which pair of compounds belongs to the same homologous series?", [
            C("[[CH3CH2OH]] and [[CH3OCH3]]", why="These have the same molecular formula but different functional groups (alcohol and ether). They are isomers, not members of one series."),
            C("[[CH3CH2CH3]] and [[CH3CH=CH2]]", why="Propane is an alkane and propene is an alkene: different functional groups and general formulae."),
            C("[[CH3OH]] and [[CH3CH2CH2OH]]", correct=True),
            C("[[CH3CHO]] and [[CH3COCH3]]", why="An aldehyde and a ketone have different functional groups, although both contain C=O."),
        ], steps=[S("Test the rule", text="Same functional group and same general formula, differing by [[CH2]] groups."),
                  S("Check each pair", text="Methanol [[CH3OH]] and propan-1-ol [[CH3CH2CH2OH]] are both alcohols ([[!C_nH_{2n+1}OH]]) and differ by two [[CH2]]. The other pairs have different groups.")],
           concept="Homologous series", skill="Concept", hint="Look for the pair with the same functional group, differing only by CH2 units.",
           feedback="Both are primary alcohols from the same series."),
        MC("Which is a **secondary** alcohol?", [
            C("[[CH3CH(OH)CH3]]", correct=True),
            C("[[CH3CH2CH2OH]]", why="The carbon holding -OH is joined to only one other carbon: a primary alcohol."),
            C("[[(CH3)3COH]]", why="The carbon holding -OH is joined to three other carbons: a tertiary alcohol."),
            C("[[CH3OH]]", why="The carbon holding -OH is joined to no other carbon (it is a methanol): classed as primary."),
        ], steps=[S("Count carbons attached to the C-OH carbon", text="In propan-2-ol the carbon holding -OH is joined to two [[CH3]] groups, so it is secondary.")],
           concept="Primary, secondary, tertiary", skill="Concept", hint="Count only the carbon atoms attached to the carbon that carries the -OH group.",
           feedback="Two carbon neighbours means secondary."),
        NUM("A hydrocarbon has molecular formula [[C8H10]]. What is its degree of unsaturation (number of rings plus double bonds, a triple bond counting as two)?", 4,
            steps=[S("Use the formula", math=r"\dfrac{2(8) + 2 - 10}{2} = 4", text="Ethylbenzene is an example: the benzene ring counts as four.")],
            concept="Degree of unsaturation", skill="Calculation", hint="Compare with the saturated alkane C8H18: how many H atoms are missing?",
            feedback="C8H18 minus C8H10 is 8 hydrogen atoms, which is 4 pairs."),
        MC("A saturated, non-cyclic ester has five carbon atoms. What is its molecular formula?", [
            C("[[C5H12O2]]", why="This would fit a diol, not an ester. The C=O in an ester removes two more hydrogens."),
            C("[[C5H8O2]]", why="This has one extra unsaturation (a ring or another double bond)."),
            C("[[C5H10O]]", why="An ester has two oxygen atoms (C=O and C-O-C)."),
            C("[[C5H10O2]]", correct=True),
        ], steps=[S("Use the general formula", text="Esters are [[!C_nH_{2n}O_2]]. With n = 5 the formula is [[C5H10O2]]. An example is propyl ethanoate.")],
           concept="General formulae", skill="Application", hint="Esters share a general formula with carboxylic acids.",
           feedback="Esters and carboxylic acids are both CnH2nO2."),
        MC("Which compound is a ketone?", [
            C("[[CH3CH2CHO]]", why="The C=O carbon is at the end of the chain and carries H: an aldehyde (propanal)."),
            C("[[CH3COCH2CH3]]", correct=True),
            C("[[CH3CH2COOH]]", why="This contains the -COOH group: a carboxylic acid."),
            C("[[CH3COOCH3]]", why="The C=O carbon is also bonded to an O-C group: an ester."),
        ], steps=[S("Look for C=O inside the chain", text="Butanone, [[CH3COCH2CH3]], has C=O between two carbon groups: a ketone.")],
           concept="Functional groups", skill="Recall", hint="A ketone's C=O is joined to two carbon atoms and nothing else.",
           feedback="The C=O is joined to two carbon groups."),
        NUM("A haloalkane [[!C_nH_{2n+1}Br]] has relative molecular mass 123. Find n. (Ar: C 12, H 1, Br 80.)", 3,
            steps=[S("Write Mr in terms of n", math=r"12n + (2n + 1) + 80 = 14n + 81"),
                   S("Solve", math=r"14n + 81 = 123 \;\Rightarrow\; n = 3", text="The compound is [[C3H7Br]], a bromopropane.")],
            concept="General formulae", skill="Calculation", hint="Add up the masses of the carbon, hydrogen and bromine atoms in terms of n.",
            feedback="14n + 81 = 123 gives n = 3."),
        MC("Which structural formula represents a **tertiary** haloalkane with formula [[C4H9Br]]?", [
            C("[[CH3CH2CH2CH2Br]]", why="Br is on an end carbon, joined to one carbon: primary."),
            C("[[(CH3)2CHCH2Br]]", why="This is branched, but the carbon holding Br is joined to only one carbon: primary."),
            C("[[CH3CH2CHBrCH3]]", why="The carbon holding Br is joined to two carbons: secondary."),
            C("[[(CH3)3CBr]]", correct=True),
        ], steps=[S("Find the structure where the C-Br carbon has three carbon neighbours", text="In 2-bromo-2-methylpropane the carbon with Br is bonded to three [[CH3]] groups.")],
           concept="Primary, secondary, tertiary", skill="Application", hint="You need a carbon bearing Br with no hydrogen atoms and three carbon neighbours.",
           feedback="Three carbon neighbours: tertiary."),
    ])]
# ------------------------------------------------------------------ Topic 1, lesson 2: IUPAC naming
SETS += [practice_set(
    module=M_ORG, topic="Classification and IUPAC nomenclature",
    title="Naming organic compounds by the IUPAC rules", lesson="chl3-iupac-naming",
    questions=[
        MC("What is the IUPAC name of [[CH3CH(CH3)CH2CH3]]?", [
            C("3-methylbutane", why="The branch must have the lowest number. Numbering from the other end puts it on carbon 2."),
            C("2-ethylpropane", why="This takes a three-carbon chain. The longest chain has four carbons, so the parent is butane."),
            C("2-methylbutane", correct=True),
            C("isopentane", why="This is a common name, not an IUPAC name."),
        ], steps=[S("Longest chain", text="Four carbons: butane."), S("Number for the lowest locant", text="The methyl group is on carbon 2 when numbered from the left. Name: 2-methylbutane.")],
           concept="Naming alkanes", skill="Recall", hint="Count the longest chain first, then decide which end to number from.",
           feedback="Longest chain four carbons, methyl on carbon 2."),
        MC("What is the IUPAC name of [[CH3CH=CHCH(CH3)2]]?", [
            C("4-methylpent-2-ene", correct=True),
            C("2-methylpent-3-ene", why="The double bond must be given the lowest number, so number from the end nearest the C=C."),
            C("4-methylpent-3-ene", why="The double bond is on carbons 2 and 3 when numbered from the left, so it is pent-2-ene."),
            C("1,1-dimethylbut-2-ene", why="The longest chain is five carbons, with one methyl branch, not four carbons with two branches."),
        ], steps=[S("Longest chain containing C=C", text="Five carbons: pentene."),
                  S("Number from the end nearest the double bond", text="C=C is between carbons 2 and 3 from the left: pent-2-ene. The methyl branch is then on carbon 4."),
                  S("Name", text="4-methylpent-2-ene.")],
           concept="Naming alkenes", skill="Application", hint="The double bond gets the lowest number, even if the branch then gets a higher one.",
           feedback="The C=C position decides the numbering direction."),
        MC("The skeletal formula of compound X is shown. What is its IUPAC name?", [
            C("4-bromo-3-methylpentane", why="Numbering is from the wrong end. The bromine must have the lowest possible number: 2."),
            C("2-bromo-3-ethylbutane", why="The longest chain is five carbons. The ethyl 'branch' is really part of the main chain."),
            C("3-methyl-2-bromopentane", why="The numbers are right but the prefixes must be in alphabetical order: bromo before methyl."),
            C("2-bromo-3-methylpentane", correct=True),
        ], steps=[S("Find the longest chain", text="Five carbons (pentane), with Br on one carbon and a methyl on another."),
                  S("Number from the end that gives the lower locants", text="Br on carbon 2, methyl on carbon 3 (set {2,3} beats {3,4})."),
                  S("Alphabetical order", text="bromo, then methyl: 2-bromo-3-methylpentane.")],
           concept="Naming haloalkanes", skill="Application", hint="Count the zig-zag chain from the bromine end, then put the prefixes in alphabetical order.",
           diagram="al-chl3-skeletal-name.svg", diagram_alt="Skeletal formula of a five-carbon chain with a bromine on the second carbon and a methyl branch on the third carbon.",
           feedback="Lowest locants, then alphabetical order."),
        MC("What is the IUPAC name of [[CH3CH(OH)CH2CH3]]?", [
            C("butan-3-ol", why="Number from the end that gives -OH the lowest number: carbon 2, not 3."),
            C("butan-2-ol", correct=True),
            C("1-methylpropan-1-ol", why="The longest chain containing -OH has four carbons; do not use a shorter chain with a branch."),
            C("2-hydroxybutane", why="An alcohol is named with the suffix -ol, not the prefix hydroxy, unless a higher priority group is present."),
        ], steps=[S("Chain and numbering", text="Four carbons; -OH on carbon 2 from the left (3 from the right). Choose 2: butan-2-ol.")],
           concept="Naming alcohols", skill="Recall", hint="Which end of the chain gives the -OH group the smaller number?",
           feedback="-OH on carbon 2 of a four-carbon chain."),
        NUM("How many carbon atoms are there in one molecule of 2,2,4-trimethylpentane?", 8,
            steps=[S("Parent chain", text="Pentane has 5 carbon atoms."),
                   S("Three methyl branches", math=r"5 + 3 \times 1 = 8", text="The formula is [[C8H18]].")],
            concept="Naming alkanes", skill="Application", hint="Count the carbons in the parent name, then add the carbons in each branch.",
            feedback="5 in the chain plus 3 methyl groups gives 8."),
        MC("What is the IUPAC name of [[CH3CH(OH)CH2COOH]]?", [
            C("butan-3-ol-1-oic acid", why="A name has only one suffix. The acid group takes the suffix and -OH becomes a prefix."),
            C("2-hydroxybutanoic acid", why="The -OH is on the third carbon (the -COOH carbon is carbon 1), not the second."),
            C("3-hydroxybutanoic acid", correct=True),
            C("1-carboxypropan-2-ol", why="The carboxylic acid has higher priority than the alcohol, so the compound is named as an acid."),
        ], steps=[S("Choose the principal group", text="Carboxylic acid outranks alcohol: parent is butanoic acid, -COOH is carbon 1."),
                  S("Locate -OH", text="It is on carbon 3: hydroxy prefix. Name: 3-hydroxybutanoic acid.")],
           concept="Priority of functional groups", skill="Application", hint="Decide which group has higher priority, then number from it.",
           feedback="Acid parent, hydroxy prefix on carbon 3."),
        MC("Which structural formula represents 3-methylbutan-1-ol?", [
            C("[[(CH3)2CHCH2CH2OH]]", correct=True),
            C("[[CH3CH2CH(CH3)CH2OH]]", why="This is 2-methylbutan-1-ol: the methyl group is on carbon 2."),
            C("[[CH3CH2C(CH3)2OH]]", why="This is 2-methylbutan-2-ol: -OH is on carbon 2, on the carbon with the methyl group."),
            C("[[CH3CH(OH)CH(CH3)2]]", why="This is 3-methylbutan-2-ol: -OH is on carbon 2."),
        ], steps=[S("Draw the chain", text="Butane chain C1 to C4, -OH on C1, methyl on C3: [[HOCH2CH2CH(CH3)CH3]], which is [[(CH3)2CHCH2CH2OH]].")],
           concept="Drawing from names", skill="Application", hint="Draw four carbons, then attach -OH to carbon 1 and a methyl group to carbon 3.",
           feedback="-OH on C1, methyl on C3."),
        MC("What is the IUPAC name of [[CH3CH(Br)CH2CH=C(CH3)2]]?", [
            C("2-bromo-5-methylhex-4-ene", why="The double bond must have the lowest number, so number from the end nearest the C=C, not from the bromine end."),
            C("2-methyl-5-bromohex-2-ene", why="Prefixes must be in alphabetical order: bromo before methyl."),
            C("5-bromo-2-methylhex-3-ene", why="The C=C is between carbons 2 and 3, so it is hex-2-ene."),
            C("5-bromo-2-methylhex-2-ene", correct=True),
        ], steps=[S("Longest chain with C=C", text="Six carbons. Number from the [[(CH3)2C=]] end so that C=C is hex-2-ene."),
                  S("Substituents", text="Methyl on carbon 2 and bromine on carbon 5. Alphabetical: 5-bromo-2-methylhex-2-ene.")],
           concept="Naming alkenes", skill="Reasoning", hint="Which end of the chain gives the double bond the lower number? That decides the direction.",
           feedback="C=C first, then alphabetical order of prefixes."),
    ])]
# ------------------------------------------------------------------ Topic 2, lesson 1: structural isomerism
SETS += [practice_set(
    module=M_ORG, topic="Structural isomerism and stereoisomerism",
    title="Chain, position and functional-group isomers", lesson="chl3-structural-isomerism",
    questions=[
        MC("Butan-1-ol and butan-2-ol are", [
            C("chain isomers", why="Both have the same four-carbon chain. Only the position of -OH changes."),
            C("position isomers", correct=True),
            C("functional-group isomers", why="Both are alcohols, so the functional group is the same."),
            C("the same compound", why="-OH is on a different carbon in each, so these are different compounds with different properties."),
        ], steps=[S("Compare", text="Same skeleton and same -OH group, but -OH is on carbon 1 in one and carbon 2 in the other: position isomers.")],
           concept="Position isomerism", skill="Recall", hint="What changes between the two: the skeleton, the group, or only where the group is?",
           feedback="Same group, different position."),
        MC("Which compound is **not** an isomer of [[C4H10O]]?", [
            C("[[CH3CH2OCH2CH3]]", why="Ethoxyethane is [[C4H10O]]: it is an ether isomer."),
            C("[[(CH3)3COH]]", why="2-Methylpropan-2-ol is [[C4H10O]]: a branched alcohol isomer."),
            C("[[CH3CH2CH(OH)CH3]]", why="Butan-2-ol is [[C4H10O]]: a position isomer."),
            C("[[CH3CH2CH2CHO]]", correct=True),
        ], steps=[S("Find the formulae", text="The first three are [[C4H10O]]. Butanal [[CH3CH2CH2CHO]] is [[C4H8O]]: it has two fewer hydrogens because of the C=O group.")],
           concept="Isomer formulae", skill="Application", hint="Work out the molecular formula of each option. Which one differs?",
           feedback="Butanal is C4H8O, so it is not an isomer of C4H10O."),
        MC("Which pair are functional-group isomers?", [
            C("[[CH3COOH]] and [[HCOOCH3]]", correct=True),
            C("[[CH3CH2OH]] and [[CH3CHO]]", why="Their formulae are [[C2H6O]] and [[C2H4O]]. They are not isomers."),
            C("[[CH3CH2CH2Cl]] and [[CH3CHClCH3]]", why="The same group in different positions: position isomers."),
            C("[[CH3CH2CH2CH2CH3]] and [[(CH3)2CHCH2CH3]]", why="Different carbon skeletons: chain isomers."),
        ], steps=[S("Test formula then group", text="Ethanoic acid and methyl methanoate are both [[C2H4O2]]: a carboxylic acid and an ester.")],
           concept="Functional-group isomerism", skill="Concept", hint="First check the molecular formulae are equal, then compare the groups.",
           feedback="An acid and an ester with the same formula."),
        NUM("How many structural isomers has [[C6H14]]?", 5,
            steps=[S("Systematic search", text="Hexane; 2-methylpentane; 3-methylpentane; 2,2-dimethylbutane; 2,3-dimethylbutane."),
                   S("Count", math=r"1 + 2 + 2 = 5")],
            concept="Systematic enumeration", skill="Application", hint="Start with the six-carbon chain, then five-carbon chains with one methyl, then four-carbon chains with two methyls.",
            feedback="Five isomers; a methyl on carbon 4 or 5 of pentane just repeats earlier ones."),
        MC("Which of these [[C5H12]] isomers has the highest boiling point?", [
            C("2,2-dimethylpropane", why="It is the most compact, with the smallest surface area, so it has the lowest boiling point."),
            C("2-methylbutane", why="It is branched, so less surface contact than pentane."),
            C("pentane", correct=True),
            C("All three are equal because they have the same formula", why="The strength of instantaneous dipole-induced dipole forces depends on the shape and surface area, not only the formula."),
        ], steps=[S("Link shape to forces", text="The straight chain has the largest surface of contact between molecules, so the strongest dispersion forces and the highest boiling point (about 36 °C).")],
           concept="Isomers and boiling point", skill="Reasoning", hint="Which shape lets molecules touch each other over the longest contact?",
           feedback="Less branching, more contact, higher boiling point."),
        MC("How many **alcohols** (not ethers) have the molecular formula [[C4H10O]]?", [
            C("3", why="You may have left out one of the two alcohols from methylpropane."),
            C("4", correct=True),
            C("5", why="Butan-3-ol and butan-4-ol are not new: they repeat butan-2-ol and butan-1-ol."),
            C("7", why="7 is the number of isomers including the three ethers."),
        ], steps=[S("Butane skeleton", text="butan-1-ol, butan-2-ol."), S("Methylpropane skeleton", text="2-methylpropan-1-ol, 2-methylpropan-2-ol."), S("Total", math=r"2 + 2 = 4")],
           concept="Systematic enumeration", skill="Application", hint="Two skeletons are possible; put -OH on each different carbon of each.",
           feedback="Four alcohols; with three ethers, seven isomers."),
        MC("Which compound is a structural isomer of but-1-ene?", [
            C("butane", why="Butane is [[C4H10]], which is not the same formula as [[C4H8]]."),
            C("but-1-yne", why="But-1-yne is [[C4H6]]."),
            C("2-methylpropane", why="2-Methylpropane is [[C4H10]]."),
            C("cyclobutane", correct=True),
        ], steps=[S("Match the formula", text="But-1-ene is [[C4H8]]. Cyclobutane is also [[C4H8]], with a ring instead of a double bond.")],
           concept="Alkene and cycloalkane isomers", skill="Concept", hint="Find the molecular formula of but-1-ene, then compare with each option.",
           feedback="A ring and a double bond each use up two hydrogens."),
        MC("Ethanol boils at about 78 °C but its isomer methoxymethane boils at about -24 °C. The best explanation is that", [
            C("ethanol molecules form hydrogen bonds with each other", correct=True),
            C("ethanol has a larger relative molecular mass", why="Both isomers have the same relative molecular mass, 46."),
            C("ethanol contains ionic bonds", why="Both are covalent molecular compounds."),
            C("the covalent bonds in ethanol are stronger", why="Boiling separates molecules without breaking the covalent bonds inside them."),
        ], steps=[S("Compare intermolecular forces", text="Ethanol has an O-H group, so its molecules hydrogen-bond. Methoxymethane has no O-H group and only weaker dipole-dipole and dispersion forces.")],
           concept="Isomers and properties", skill="Reasoning", hint="Which isomer has an O-H group?",
           feedback="Hydrogen bonding raises the boiling point."),
    ])]
# ------------------------------------------------------------------ Topic 2, lesson 2: stereoisomerism
SETS += [practice_set(
    module=M_ORG, topic="Structural isomerism and stereoisomerism",
    title="Geometric (E/Z) and optical isomerism", lesson="chl3-stereoisomerism",
    questions=[
        MC("Which alkene shows geometric (cis-trans) isomerism?", [
            C("But-1-ene", why="One carbon of the C=C has two hydrogen atoms, so swapping groups gives the same molecule."),
            C("2-Methylbut-2-ene", why="One carbon of the C=C carries two identical methyl groups."),
            C("Hex-3-ene", correct=True),
            C("2-Methylpropene", why="One carbon of the C=C carries two H atoms and the other two CH3 groups."),
        ], steps=[S("Test each carbon of C=C", text="Each double-bond carbon must carry two different groups. In hex-3-ene each carbon has an ethyl group and an H.")],
           concept="Geometric isomerism", skill="Concept", hint="Write in the H atoms. Does each carbon of the double bond have two different groups?",
           feedback="Two different groups on each C=C carbon are required."),
        MC("Which compound contains a chiral centre?", [
            C("[[CH3CHClCH2CH3]]", correct=True),
            C("[[CH3CH2CH2Cl]]", why="The carbon holding Cl has two H atoms, so it is not chiral."),
            C("[[(CH3)2CHCl]]", why="The carbon holding Cl carries two identical CH3 groups."),
            C("[[CH3CCl2CH3]]", why="The central carbon carries two Cl atoms and two CH3 groups."),
        ], steps=[S("Search for a carbon with four different groups", text="In 2-chlorobutane carbon 2 carries H, Cl, [[CH3]] and [[CH2CH3]].")],
           concept="Chiral centre", skill="Concept", hint="Look for a carbon bonded to four different atoms or groups.",
           feedback="Four different groups make a chiral centre."),
        MC("The compound [[CH3CH=C(CH3)CH2CH3]] is drawn with the [[CH3]] on carbon 2 and the ethyl group on carbon 3 on the same side of the C=C. Which statement is correct?", [
            C("It is E, because the two methyl groups are on opposite sides.", why="E/Z uses the higher-priority group on each carbon. On carbon 3 the ethyl group, not the methyl, has higher priority."),
            C("It is neither E nor Z because the groups are different.", why="E/Z notation is designed exactly for alkenes with different groups and always applies when each carbon has two different groups."),
            C("It is E, because ethyl is larger than methyl.", why="Size does not decide; priority is by atomic number, and E means the higher-priority groups are on opposite sides."),
            C("It is Z, because the higher-priority groups (CH3 on carbon 2, ethyl on carbon 3) are on the same side.", correct=True),
        ], steps=[S("Priorities on carbon 2", text="[[CH3]] has higher priority than H."),
                  S("Priorities on carbon 3", text="[[CH2CH3]] (C, H, H) beats [[CH3]] (H, H, H)."),
                  S("Compare sides", text="CH3 on C2 and ethyl on C3 are on the same side: **Z**.")],
           concept="E/Z notation", skill="Application", hint="Find the higher-priority group on each carbon, then check whether they are on the same side.",
           feedback="Z means the higher-priority groups are together."),
        NUM("How many stereoisomers does 2,3-dibromopentane [[CH3CHBrCHBrCH2CH3]] have?", 4,
            steps=[S("Chiral centres", text="Carbons 2 and 3 are each bonded to four different groups, so there are two chiral centres."),
                   S("Count", math=r"2^2 = 4", text="The two centres are not identical in groups (CH3 end and C2H5 end), so there is no meso form and all four forms are different.")],
            concept="Counting stereoisomers", skill="Calculation", hint="Count the chiral centres, n, then use 2 to the power n.",
            feedback="Two chiral centres give 2 x 2 = 4 stereoisomers."),
        MC("A racemic mixture is", [
            C("a single enantiomer dissolved in water", why="A racemic mixture contains both enantiomers."),
            C("a mixture of two geometric isomers", why="Racemic mixtures involve enantiomers (optical isomers), not cis-trans isomers."),
            C("an equal mixture of two enantiomers, which does not rotate plane-polarised light", correct=True),
            C("a compound with no chiral centre", why="The molecules in a racemate each have a chiral centre."),
        ], steps=[S("Definition", text="Equal amounts of two enantiomers: their rotations are equal and opposite, so there is no net rotation.")],
           concept="Racemic mixture", skill="Recall", hint="Recall what 'rac' means: equal amounts of mirror images.",
           feedback="Equal amounts of mirror-image molecules cancel their optical activity."),
        MC("How many chiral centres are there in 3-chlorobutan-2-ol, [[CH3CH(OH)CH(Cl)CH3]]?", [
            C("1", why="Carbon 2 is chiral, but so is carbon 3: it has H, Cl, CH3 and CH(OH)CH3."),
            C("2", correct=True),
            C("3", why="Carbons 1 and 4 are CH3 groups with three identical H atoms, so they are not chiral."),
            C("4", why="Only carbons with four different groups count."),
        ], steps=[S("Carbon 2", text="Groups: H, OH, [[CH3]], [[CH(Cl)CH3]]: all different, so chiral."),
                  S("Carbon 3", text="Groups: H, Cl, [[CH3]], [[CH(OH)CH3]]: all different, so chiral.")],
           concept="Chiral centre", skill="Application", hint="Test carbons 2 and 3 separately; carbons 1 and 4 are CH3 groups.",
           feedback="Two chiral centres."),
        MC("Two enantiomers of the same compound differ in", [
            C("their boiling points", why="Their intermolecular forces are identical, so boiling points are the same."),
            C("their solubility in water", why="Enantiomers dissolve equally in an ordinary (non-chiral) solvent."),
            C("their reaction with sodium", why="Enantiomers react the same way with achiral reagents."),
            C("the direction in which they rotate plane-polarised light", correct=True),
        ], steps=[S("Recall", text="Enantiomers have identical physical properties and reactions with achiral reagents. They rotate plane-polarised light by equal amounts in opposite directions, and react differently with chiral molecules such as enzymes.")],
           concept="Optical activity", skill="Recall", hint="What do enantiomers do to polarised light?",
           feedback="Opposite rotation of plane-polarised light is the key difference."),
        MC("Hydrogen cyanide adds to propanal to give [[CH3CH2CH(OH)CN]] as a racemic mixture. The reason is that", [
            C("the C=O group is flat, so the cyanide ion can attack either face equally", correct=True),
            C("the cyanide ion is a chiral nucleophile", why="The cyanide ion is a simple linear ion with no chirality."),
            C("the product has no chiral centre", why="The product carbon holds H, OH, CN and [[CH2CH3]]: four different groups, so it is chiral."),
            C("the reaction is too slow to be selective", why="Speed does not matter; the equal probability of attack from the two faces gives equal amounts of the two enantiomers."),
        ], steps=[S("Shape of the reactant", text="The carbonyl carbon is trigonal planar, so a nucleophile can approach from above or below with equal probability."),
                  S("Result", text="Equal amounts of the two enantiomers form: a racemate, with no net optical activity.")],
           concept="Racemic mixture from planar attack", skill="Reasoning", hint="Think about the shape around the carbon of C=O. Where can the attacking ion approach from?",
           feedback="Attack from either face of a planar carbon gives both enantiomers."),
    ])]
# ------------------------------------------------------------------ Topic 3: reaction mechanisms
SETS += [practice_set(
    module=M_ORG, topic="Reaction mechanisms",
    title="Bond fission, nucleophiles, electrophiles and electron effects", lesson="chl3-electron-effects-bond-fission-curly-arrows",
    questions=[
        MC("Which kind of bond fission produces free radicals?", [
            C("Heterolytic fission", why="Heterolytic fission gives a pair of ions because both electrons go to one atom."),
            C("Homolytic fission", correct=True),
            C("Electrophilic addition", why="This is a type of reaction, not a type of bond fission."),
            C("Hydrolysis", why="This is a reaction with water, not a type of bond fission."),
        ], steps=[S("Definition", text="In homolytic fission each atom takes one electron from the bond, so each product has an unpaired electron: a free radical.")],
           concept="Bond fission", skill="Recall", hint="Which fission shares the bonding pair equally, one electron to each atom?",
           feedback="One electron each gives two radicals."),
        MC("Which of these species is an electrophile?", [
            C("[[CN^-]]", why="It has a lone pair and a negative charge: it donates electrons, so it is a nucleophile."),
            C("[[H2O]]", why="Water has lone pairs on oxygen and acts as a nucleophile."),
            C("[[Br^-]]", why="A bromide ion has lone pairs and acts as a nucleophile."),
            C("[[NO2^+]]", correct=True),
        ], steps=[S("Look for electron-poor species", text="[[NO2^+]] has a positive charge and accepts an electron pair: an electrophile.")],
           concept="Nucleophile and electrophile", skill="Concept", hint="An electrophile is electron-loving. Which species is positive?",
           feedback="Positively charged species accept electron pairs."),
        MC("The C-Cl bond in [[CH3Cl]] breaks heterolytically. Which description of the curly arrow is correct?", [
            C("Starts at the middle of the C-Cl bond and ends on the Cl atom", correct=True),
            C("Starts on the Cl atom and ends on the C atom", why="The arrow must start where the electrons are (the bond) and point to where they go. It cannot start on an atom with no pair shown."),
            C("Starts on the C atom and ends on the Cl atom", why="Arrows start at electrons: the bond, not the carbon atom."),
            C("Is half-headed, from the bond to each atom", why="Half-headed arrows show homolytic fission. Heterolytic fission has one full-headed arrow."),
        ], steps=[S("Where do the electrons go?", text="Chlorine is more electronegative, so the bonding pair moves to Cl. The arrow runs from the bond to the chlorine atom.")],
           concept="Curly arrows", skill="Application", hint="A curly arrow starts at the electrons and finishes where they end up.",
           feedback="The arrow shows the pair moving from the bond to chlorine."),
        MC("Which carbocation is the most stable?", [
            C("[[CH3^+]]", why="It has no alkyl groups to donate electrons by the +I effect."),
            C("[[CH3CH2^+]]", why="It has only one alkyl group (primary)."),
            C("[[(CH3)3C^+]]", correct=True),
            C("[[(CH3)2CH^+]]", why="It has two alkyl groups (secondary). A tertiary ion has three."),
        ], steps=[S("Count alkyl groups", text="Each alkyl group releases electron density (+I) to the positive carbon. The tertiary ion has three, so it is the most stable.")],
           concept="Inductive effect", skill="Concept", hint="Count the alkyl groups attached to the positively charged carbon.",
           feedback="More alkyl groups, more stabilisation."),
        MC("Which is the strongest acid?", [
            C("[[CH3COOH]]", why="It has no electron-withdrawing atoms to stabilise the anion."),
            C("[[CCl3COOH]]", correct=True),
            C("[[CH3CH2COOH]]", why="The extra alkyl group releases electrons (+I), which destabilises the anion and makes the acid weaker."),
            C("[[ClCH2CH2COOH]]", why="One chlorine, two carbons away from the acid group, has only a weak effect that fades quickly with distance."),
        ], steps=[S("Compare the anions", text="Three Cl atoms next to the carboxylate group give a strong −I effect, stabilising [[CCl3COO^-]]. A more stable anion means a stronger acid.")],
           concept="Inductive effect and acidity", skill="Reasoning", hint="Which acid has the most electron-withdrawing atoms close to the -COOH group?",
           feedback="Three chlorines withdraw the most electron density."),
        MC("In the ethanoate ion the two C-O bonds are the same length because", [
            C("the ion flips rapidly between two different structures", why="Resonance forms are not different molecules and there is no flipping. One hybrid structure exists."),
            C("both oxygen atoms are bonded to hydrogen", why="The ethanoate ion has no hydrogen on either oxygen."),
            C("each C-O bond is a full double bond", why="A double bond is shorter than a single bond; the observed length is in between."),
            C("the negative charge and pi electrons are delocalised over the O-C-O group", correct=True),
        ], steps=[S("Explain", text="Delocalisation spreads the charge equally over both oxygen atoms, giving two equivalent bonds of intermediate length.")],
           concept="Mesomeric effect", skill="Reasoning", hint="Think about resonance forms. Is the negative charge on one oxygen or shared?",
           feedback="Delocalisation makes the two bonds identical."),
        MC("Why is ultraviolet light needed to start the reaction of methane with chlorine?", [
            C("It supplies energy to break the Cl-Cl bond homolytically into chlorine radicals", correct=True),
            C("It makes methane polar so that it can be attacked by ions", why="Methane is non-polar and remains so; the reaction goes through radicals, not ions."),
            C("It acts as a catalyst by lowering the activation energy", why="Light is not a catalyst; it provides energy to break bonds and is used up as photons."),
            C("It breaks the C-H bond directly into ions", why="The C-H bond is not broken by the light in this reaction; the Cl-Cl bond is."),
        ], steps=[S("Initiation", text="[[Cl2 -> 2Cl.]] occurs by homolytic fission when each Cl-Cl bond absorbs enough energy from UV light.")],
           concept="Free radicals", skill="Application", hint="Which bond in the mixture is the weakest and non-polar?",
           feedback="UV light provides the energy to split the Cl-Cl bond into radicals."),
        MC("2-Bromo-2-methylpropane forms a carbocation more readily than bromomethane. The best reason is that", [
            C("the C-Br bond in bromomethane is stronger", why="Bond strengths are similar; the difference is in the stability of the ion formed."),
            C("a tertiary carbon is more electronegative than a methyl carbon", why="Carbon atoms have the same electronegativity; the difference is the number of alkyl groups."),
            C("the three alkyl groups stabilise the positive charge by the +I effect", correct=True),
            C("the carbocation from bromomethane has six electrons but the tertiary one has eight", why="Both carbocations have six electrons around the positive carbon."),
        ], steps=[S("Compare the ions", text="[[(CH3)3C^+]] has three electron-releasing alkyl groups; [[CH3^+]] has none. So the tertiary ion is more stable and forms more readily.")],
           concept="Carbocation stability", skill="Reasoning", hint="What does each alkyl group do to the electron density on the positive carbon?",
           feedback="+I effect stabilises tertiary carbocations."),
    ])]
# ------------------------------------------------------------------ Topic 4: alkanes and alkenes
SETS += [practice_set(
    module=M_ORG, topic="Alkanes and alkenes",
    title="Reactions of alkanes and alkenes", lesson="chl3-alkanes-and-alkenes",
    questions=[
        MC("Which condition is needed for methane to react with chlorine to form chloromethane?", [
            C("Darkness at room temperature", why="Without UV light no radicals form, so methane and chlorine do not react in the dark."),
            C("Reflux with aqueous sodium hydroxide", why="This is the condition for hydrolysis of a haloalkane, not for substituting an alkane."),
            C("Ultraviolet light", correct=True),
            C("Nickel catalyst at 150 °C", why="This is the condition for hydrogenation of an alkene."),
        ], steps=[S("Initiation", text="UV light supplies the energy to break the Cl-Cl bond homolytically into chlorine radicals that start the chain.")],
           concept="Free-radical substitution", skill="Recall", hint="Which energy source breaks the Cl-Cl bond into radicals?",
           feedback="UV light starts the radical chain."),
        MC("Which equation is a **termination** step in the chlorination of methane?", [
            C("[[.CH3 + Cl. -> CH3Cl]]", correct=True),
            C("[[Cl2 -> 2Cl.]]", why="This is initiation: radicals form from a molecule."),
            C("[[CH4 + Cl. -> .CH3 + HCl]]", why="This is propagation: a radical is used and another is made."),
            C("[[.CH3 + Cl2 -> CH3Cl + Cl.]]", why="This is propagation: it makes a new chlorine radical."),
        ], steps=[S("Termination", text="Two radicals combine and no new radical forms, so the chain ends.")],
           concept="Free-radical chain", skill="Concept", hint="In which step do two radicals combine and none remain?",
           feedback="Two radicals joining ends the chain."),
        MC("What is the major organic product of the reaction of propene with hydrogen bromide?", [
            C("1-Bromopropane", why="This comes from the primary carbocation, which is less stable. It is the minor product."),
            C("1,2-Dibromopropane", why="This needs two bromine atoms, from [[Br2]], not from HBr."),
            C("Propan-2-ol", why="The reagent is HBr, not water, so no -OH group is formed."),
            C("2-Bromopropane", correct=True),
        ], steps=[S("Where does H add?", text="H adds to the carbon with more hydrogens (CH2), giving the secondary carbocation [[!CH_3CH^{+}CH_3]]."),
                  S("Add bromide", text="[[Br^-]] attacks it: [[CH3CHBrCH3]], 2-bromopropane.")],
           concept="Markovnikov's rule", skill="Application", hint="Which carbocation is more stable: primary or secondary?",
           feedback="The more stable secondary carbocation leads to the major product."),
        MC("What is observed when ethene is bubbled through bromine water?", [
            C("The orange colour is unchanged", why="Ethene reacts rapidly with bromine, so the colour changes."),
            C("The orange solution becomes colourless", correct=True),
            C("The solution turns purple", why="Purple is the colour of potassium manganate(VII), not of bromine water."),
            C("A white precipitate forms", why="A precipitate is not the characteristic result; the key change is the loss of the orange colour."),
        ], steps=[S("Reaction", text="[[C2H4 + Br2 -> CH2BrCH2Br]]: bromine is used up in the addition, so the orange colour disappears.")],
           concept="Test for unsaturation", skill="Recall", hint="What happens to bromine's colour when it is used up?",
           feedback="Bromine water is decolourised by alkenes."),
        NUM("20 cm³ of propane [[C3H8]] are burnt completely in excess oxygen. What volume of oxygen (in cm³, measured at the same temperature and pressure) is used?", 100,
            steps=[S("Equation", math=r"\mathrm{C_3H_8} + 5\mathrm{O_2} \rightarrow 3\mathrm{CO_2} + 4\mathrm{H_2O}"),
                   S("Volume ratio 1 : 5", math=r"20 \times 5 = 100\ \text{cm}^3", text="Gas volumes at the same temperature and pressure are in the same ratio as moles.")],
            unit="cm³", concept="Combustion of alkanes", skill="Calculation", hint="Write the balanced equation and use the mole (volume) ratio of propane to oxygen.",
            feedback="1 volume of propane needs 5 volumes of oxygen."),
        MC("Which products form when [[(CH3)2C=CH2]] reacts with ozone and then water?", [
            C("Propanal and methanal", why="Propanal [[CH3CH2CHO]] has a different carbon chain. The carbon with two methyl groups gives a ketone, not an aldehyde."),
            C("Propanone only", why="Both carbons of the C=C become carbonyl groups, so two products form."),
            C("Propanone and methanal", correct=True),
            C("2-Methylpropan-2-ol", why="Ozone and water cleave the C=C; they do not add water across the bond."),
        ], steps=[S("Split the C=C", text="The carbon with two methyl groups becomes [[(CH3)2C=O]] (propanone). The CH2 carbon becomes [[CH2=O]] (methanal).")],
           concept="Ozonolysis", skill="Application", hint="Each carbon of the C=C becomes a C=O group.",
           feedback="Propanone and methanal form."),
        MC("Alkenes are much more reactive than alkanes mainly because", [
            C("the pi bond is a region of high electron density and is weaker than a sigma bond", correct=True),
            C("the C=C bond is stronger than a C-C bond", why="Strength is not the reason; the extra pi bond is weaker than the sigma bond, which makes it easier to break."),
            C("alkenes are polar molecules", why="Alkenes are essentially non-polar. Reactivity comes from the electron-rich pi bond."),
            C("alkenes have more hydrogen atoms", why="Alkenes have fewer hydrogen atoms than the alkanes with the same number of carbons."),
        ], steps=[S("Compare the bonds", text="The pi bond lies above and below the molecule, is exposed to electrophiles and has a lower bond energy, so it breaks readily in addition reactions.")],
           concept="Reactivity of alkenes", skill="Reasoning", hint="Think about the pi electrons: where are they and how strongly are they held?",
           feedback="The exposed, weaker pi bond makes alkenes reactive."),
        MC("2-Bromopropane is the major product of propene with HBr because", [
            C("bromine always attaches to the carbon with more hydrogens", why="The opposite is true: hydrogen adds to the carbon with more hydrogens and bromine ends up on the other carbon."),
            C("a primary carbocation is more stable than a secondary one", why="Secondary carbocations are more stable than primary ones because they have two electron-releasing alkyl groups."),
            C("the reaction is a free-radical substitution", why="The reaction is electrophilic addition, which proceeds by ions (carbocations), not radicals."),
            C("the intermediate secondary carbocation is more stable than the primary one", correct=True),
        ], steps=[S("Stability decides the route", text="The more stable secondary carbocation forms faster. The +I effect of two alkyl groups stabilises it. The bromide ion then attacks it, giving 2-bromopropane.")],
           concept="Carbocation stability", skill="Reasoning", hint="Compare the two possible carbocations formed when H adds to propene.",
           feedback="Secondary carbocation is the more stable intermediate."),
    ])]
# ------------------------------------------------------------------ Topic 5, lesson 1: alkynes
SETS += [practice_set(
    module=M_ORG, topic="Alkynes and haloalkanes",
    title="Alkynes: bonding, tests and addition reactions", lesson="chl3-alkynes",
    questions=[
        MC("In propyne [[CH3C#CH]] the hybridisations of the three carbon atoms, from left to right, are", [
            C("sp³, sp, sp", correct=True),
            C("sp³, sp², sp²", why="sp² carbons have a double bond. Propyne has a triple bond, whose carbons are sp."),
            C("sp, sp, sp³", why="The methyl carbon has four single bonds (sp³) and is on the left; the order is reversed."),
            C("sp², sp, sp", why="The methyl carbon forms four sigma bonds, so it is sp³, not sp²."),
        ], steps=[S("Count sigma bonds around each carbon", text="[[CH3]]: four sigma bonds, so sp³. Each carbon of C≡C has two sigma bonds, so sp.")],
           concept="sp hybridisation", skill="Concept", hint="Count the number of sigma bonds around each carbon atom.",
           feedback="Four sigma bonds is sp³; two sigma bonds is sp."),
        MC("Which pair of compounds can be distinguished by ammoniacal silver nitrate?", [
            C("Ethene and ethane", why="Neither has a terminal C-H of the alkyne type, so neither gives a precipitate."),
            C("But-2-yne and pent-2-yne", why="Both are internal alkynes and give no precipitate."),
            C("But-1-yne and but-2-yne", correct=True),
            C("Propane and propene", why="Neither is a terminal alkyne."),
        ], steps=[S("Which has a terminal C-H?", text="But-1-yne [[HC#CCH2CH3]] has an acidic [[C#C-H]] and forms a white precipitate; but-2-yne [[CH3C#CCH3]] does not.")],
           concept="Test for terminal alkynes", skill="Application", hint="Only one of the two compounds has a hydrogen on a triple-bond carbon.",
           feedback="The terminal alkyne gives the precipitate."),
        MC("What is the product of the reaction of ethyne with water in the presence of mercury(II) sulfate and dilute sulfuric acid?", [
            C("Ethanol", why="This would need addition of H2O to an alkene [[C2H4]], not to ethyne."),
            C("Ethanoic acid", why="Further oxidation would be needed; hydration alone does not produce an acid."),
            C("Ethane-1,2-diol", why="This forms from ethene with cold alkaline [[KMnO4]], not from hydration of ethyne."),
            C("Ethanal", correct=True),
        ], steps=[S("Hydration", text="[[HC#CH + H2O -> CH2=CHOH]] (enol), which rearranges at once to [[CH3CHO]].")],
           concept="Hydration of alkynes", skill="Recall", hint="The first product is an enol, which changes to a carbonyl compound.",
           feedback="Ethyne gives ethanal via an unstable enol."),
        MC("Propyne reacts with an excess of hydrogen bromide. What is the final product?", [
            C("1,2-Dibromopropane", why="This would form from propene with bromine, not from propyne with HBr."),
            C("2,2-Dibromopropane", correct=True),
            C("1,1-Dibromopropane", why="Markovnikov's rule places the bromine on the carbon that already carries one, but that carbon is C2, not C1."),
            C("1,3-Dibromopropane", why="The two bromine atoms add across the same triple bond, so they end up on adjacent or the same carbon, not on carbons 1 and 3."),
        ], steps=[S("First HBr", text="Br adds to C2 (the carbon with fewer hydrogens): [[CH3CBr=CH2]]."),
                  S("Second HBr", text="Br again adds to C2: [[CH3CBr2CH3]], 2,2-dibromopropane.")],
           concept="Addition to alkynes", skill="Application", hint="Apply Markovnikov's rule twice. Which carbon ends up with both bromines?",
           feedback="Both Br atoms on carbon 2."),
        NUM("12.8 g of calcium carbide [[CaC2]] react completely with excess water. What volume of ethyne (in dm³) is formed at rtp? (Ar: Ca 40, C 12; molar volume 24 dm³ at rtp.)", 4.8, tolerance=0.05,
            steps=[S("Moles of [[CaC2]]", math=r"n = \dfrac{12.8}{64} = 0.20\ \text{mol}"),
                   S("1 : 1 ratio", text="[[CaC2 + 2H2O -> C2H2 + Ca(OH)2]] gives 0.20 mol of ethyne."),
                   S("Volume", math=r"V = 0.20 \times 24 = 4.8\ \text{dm}^3")],
            unit="dm³", concept="Preparation of ethyne", skill="Calculation", hint="Find the molar mass of calcium carbide, then the moles, then use the 1 : 1 ratio.",
            feedback="0.20 mol of ethyne occupies 4.8 dm³ at rtp."),
        MC("How many structural isomers of [[C5H8]] are alkynes?", [
            C("3", correct=True),
            C("2", why="You may have missed 3-methylbut-1-yne, the branched alkyne."),
            C("4", why="Pent-3-yne is the same as pent-2-yne when numbered from the other end."),
            C("5", why="Only three arrangements of a triple bond in a five-carbon skeleton are possible."),
        ], steps=[S("List them", text="Pent-1-yne, pent-2-yne and 3-methylbut-1-yne: three.")],
           concept="Isomers of alkynes", skill="Application", hint="Triple bond on carbon 1 or 2 of the straight chain, then try the branched skeleton.",
           feedback="Three alkyne isomers."),
        MC("Ethyne burns in air with a smokier flame than ethane mainly because", [
            C("it contains more oxygen", why="Ethyne contains no oxygen; the oxygen comes from the air."),
            C("it has a higher proportion of carbon, so combustion is less complete and soot forms", correct=True),
            C("it has a lower boiling point", why="The boiling point does not control the smoke."),
            C("it contains a pi bond that does not burn", why="Pi bonds break easily in combustion; the smoke comes from unburnt carbon."),
        ], steps=[S("Compare carbon content", text="Ethyne [[C2H2]] is 92% carbon by mass; ethane is 80%. The air supply is not enough to oxidise all the carbon, so soot forms.")],
           concept="Combustion of alkynes", skill="Reasoning", hint="Compare the C : H ratio of ethyne and ethane.",
           feedback="High carbon content gives a smoky flame in air."),
        MC("The C-H bond in ethyne is more acidic than the C-H bond in ethene mainly because", [
            C("the molecule is linear", why="Shape alone does not decide acidity."),
            C("ethyne has a higher relative molecular mass", why="Acidity does not depend on molar mass in this way."),
            C("the pi bonds donate electrons to hydrogen", why="Pi electrons are not donated to H; they make the carbon appear electronegative."),
            C("the sp carbon has 50% s character and is more electronegative, stabilising the anion", correct=True),
        ], steps=[S("Why?", text="s orbitals hold electrons closer to the nucleus. An sp carbon (50% s) holds the electron pair of the conjugate base more tightly than an sp² carbon (33% s), so the anion is more stable.")],
           concept="Acidity of terminal alkynes", skill="Reasoning", hint="Compare the hybridisation, and so the s character, of the carbon in each C-H bond.",
           feedback="Greater s character means greater electronegativity of the carbon."),
    ])]
# ------------------------------------------------------------------ Topic 5, lesson 2: haloalkanes
SETS += [practice_set(
    module=M_ORG, topic="Alkynes and haloalkanes",
    title="Substitution and elimination in haloalkanes", lesson="chl3-haloalkanes-substitution-elimination",
    questions=[
        MC("Which reagent converts ethanol into chloroethane?", [
            C("Aqueous sodium chloride", why="Chloride ions in water are poor nucleophiles and cannot replace the -OH group."),
            C("Chlorine gas in ultraviolet light", why="This substitutes hydrogen atoms in an alkane and does not convert an alcohol."),
            C("Dilute sodium hydroxide", why="Hydroxide would not introduce chlorine; it is the reagent for hydrolysis."),
            C("Thionyl chloride, [[SOCl2]]", correct=True),
        ], steps=[S("Equation", text="[[C2H5OH + SOCl2 -> C2H5Cl + SO2 + HCl]]. Phosphorus(V) chloride [[PCl5]] also works.")],
           concept="Preparation of haloalkanes", skill="Recall", hint="Which reagent replaces -OH by -Cl and forms gaseous by-products?",
           feedback="SOCl2 and PCl5 convert alcohols into chloroalkanes."),
        MC("The rate of hydrolysis of haloalkanes increases in the order chloro < bromo < iodo mainly because", [
            C("the C-X bond becomes more polar", why="The C-X bond becomes less polar down the group, yet the rate increases, so polarity is not the deciding factor."),
            C("the C-X bond enthalpy decreases", correct=True),
            C("the halogen becomes more electronegative", why="Electronegativity decreases from Cl to I."),
            C("the haloalkane becomes more soluble in water", why="Haloalkanes are insoluble in water for all halogens."),
        ], steps=[S("Compare bond strengths", text="Approximate C-X bond enthalpies: C-Cl 340, C-Br 280, C-I 240 kJ/mol. The weaker the bond, the faster it breaks.")],
           concept="Reactivity and bond enthalpy", skill="Concept", hint="Think about which factor decides how easily the C-X bond breaks.",
           feedback="Weaker C-X bond, faster hydrolysis."),
        MC("Bromoethane is heated under reflux with ethanolic potassium cyanide. What is the organic product?", [
            C("Propanenitrile", correct=True),
            C("Ethanenitrile", why="This has only two carbon atoms. Substitution of Br by CN adds a carbon, giving three."),
            C("Propanoic acid", why="This forms only after the nitrile is hydrolysed with acid, in a second step."),
            C("Ethylamine", why="Ethylamine forms with ammonia, not cyanide."),
        ], steps=[S("Substitution", text="[[CH3CH2Br + CN^- -> CH3CH2CN + Br^-]]: propanenitrile has three carbons.")],
           concept="Nucleophilic substitution", skill="Application", hint="Cyanide replaces bromine and adds one carbon to the chain.",
           feedback="The chain grows by one carbon."),
        NUM("An SN2 reaction has rate = k[RBr][OH⁻] with k = 1.5 × 10⁻³ dm³ mol⁻¹ s⁻¹. When [RBr] = 0.20 mol/dm³ and [OH⁻] = 0.10 mol/dm³, what is the rate in units of 10⁻⁵ mol dm⁻³ s⁻¹?", 3.0, tolerance=0.05,
            steps=[S("Substitute", math=r"\text{rate} = 1.5\times10^{-3} \times 0.20 \times 0.10 = 3.0\times10^{-5}"),
                   S("State in the requested units", text="3.0 × 10⁻⁵ mol dm⁻³ s⁻¹ is 3.0 in units of 10⁻⁵.")],
            unit="x 10^-5 mol dm^-3 s^-1", concept="Rate equation for SN2", skill="Calculation", hint="Multiply k by both concentrations.",
            feedback="Rate = 1.5e-3 x 0.20 x 0.10 = 3.0e-5."),
        MC("What is the main organic product when 2-bromopropane is heated with ethanolic potassium hydroxide?", [
            C("Propan-2-ol", why="This is the product with aqueous hydroxide (substitution), not ethanolic (elimination)."),
            C("Propan-1-ol", why="The OH would not move to the end carbon, and ethanolic KOH gives elimination."),
            C("Propene", correct=True),
            C("Propane", why="Elimination removes HBr; it does not add hydrogen."),
        ], steps=[S("Elimination", text="[[CH3CHBrCH3 + KOH -> CH3CH=CH2 + KBr + H2O]] with ethanolic KOH and heat.")],
           concept="Elimination", skill="Application", hint="Ethanolic hydroxide acts as a base, not a nucleophile.",
           feedback="Ethanolic KOH removes HBr to form the alkene."),
        MC("The rate of hydrolysis of a bromoalkane doubles when [RBr] doubles and does not change when [OH⁻] doubles. This shows that", [
            C("the reaction is SN2, second order overall", why="An SN2 rate would also double when [OH⁻] doubles."),
            C("the reaction is a free-radical substitution", why="Radical reactions need UV light and do not match this hydrolysis."),
            C("the nucleophile is in the slow step", why="If it were, the rate would depend on [OH⁻]."),
            C("the reaction is SN1: rate = k[RBr], zero order in hydroxide", correct=True),
        ], steps=[S("Orders", text="First order in RBr, zero order in OH⁻: rate = k[RBr]. The slow step involves only RBr: SN1.")],
           concept="SN1 rate equation", skill="Interpretation", hint="Which reactant concentrations appear in the rate equation?",
           feedback="No [OH⁻] term means SN1."),
        MC("(R)-2-Bromobutane reacts with aqueous sodium hydroxide entirely by the SN2 mechanism. The product is", [
            C("(R)-butan-2-ol", why="Retention would need the nucleophile to attack from the same side as the leaving group. SN2 inverts the configuration."),
            C("(S)-butan-2-ol", correct=True),
            C("a racemic mixture of butan-2-ol", why="A racemic mixture comes from SN1 (planar carbocation), not from SN2."),
            C("but-2-ene", why="Elimination needs ethanolic KOH and heat; with aqueous alkali and SN2 the product is the alcohol."),
        ], steps=[S("Back-side attack", text="The nucleophile attacks opposite to the leaving group, inverting the configuration. The priority order is unchanged, so (R) becomes (S).")],
           concept="Stereochemistry of SN2", skill="Application", hint="SN2 attacks from the side opposite the leaving group. What does that do to the configuration?",
           feedback="SN2 gives inversion of configuration."),
        MC("Which is the major alkene formed when 2-bromobutane is heated with ethanolic potassium hydroxide?", [
            C("But-2-ene", correct=True),
            C("But-1-ene", why="This is the minor product; it is less substituted and less stable."),
            C("2-Methylpropene", why="This has a different carbon skeleton and cannot form from 2-bromobutane."),
            C("Butane", why="Elimination makes an alkene, not an alkane."),
        ], steps=[S("Zaitsev's rule", text="Loss of H from C3 gives but-2-ene (more substituted, more stable); loss of H from C1 gives but-1-ene. But-2-ene is the major product.")],
           concept="Zaitsev's rule", skill="Reasoning", hint="Which alkene has more alkyl groups on its double bond?",
           feedback="The more substituted alkene is the major product."),
    ])]
# ------------------------------------------------------------------ Topic 6: alcohols
SETS += [practice_set(
    module=M_ORG, topic="Alcohols",
    title="Properties and reactions of alcohols", lesson="chl3-alcohols",
    questions=[
        MC("Ethanol dissolves readily in water mainly because", [
            C("both are ionic compounds", why="Ethanol is a covalent molecular compound, not ionic."),
            C("ethanol molecules form hydrogen bonds with water molecules", correct=True),
            C("ethanol has a high relative molecular mass", why="Its relative molecular mass (46) is low, and mass alone does not explain solubility."),
            C("ethanol reacts with water to form ethoxide ions", why="Ethanol is a very weak acid and does not react with water to any significant extent."),
        ], steps=[S("Hydrogen bonding", text="The -OH group of ethanol forms hydrogen bonds with water, releasing energy that offsets the energy needed to separate the molecules.")],
           concept="Physical properties of alcohols", skill="Concept", hint="What can the O-H group of ethanol form with water molecules?",
           feedback="Hydrogen bonding makes small alcohols soluble."),
        MC("What are the products of the reaction between ethanol and sodium?", [
            C("Ethane and sodium hydroxide", why="Sodium replaces the hydrogen of -OH; the carbon skeleton is unchanged, so no ethane forms."),
            C("Ethene and sodium hydroxide", why="Elimination needs a dehydrating agent, not sodium."),
            C("Sodium carbonate and hydrogen", why="There is no carbon dioxide or carbonate source in this reaction."),
            C("Sodium ethoxide and hydrogen", correct=True),
        ], steps=[S("Equation", math=r"2\mathrm{CH_3CH_2OH} + 2\mathrm{Na} \rightarrow 2\mathrm{CH_3CH_2ONa} + \mathrm{H_2}")],
           concept="Reactions of alcohols with sodium", skill="Recall", hint="Sodium replaces the hydrogen atom of the -OH group.",
           feedback="Sodium ethoxide forms and hydrogen is released."),
        MC("Which alcohol gives a yellow precipitate when warmed with iodine and aqueous sodium hydroxide?", [
            C("Propan-1-ol", why="It does not contain the [[CH3CH(OH)-]] group needed for the iodoform test."),
            C("Butan-1-ol", why="A primary alcohol other than ethanol does not give the test."),
            C("Butan-2-ol", correct=True),
            C("2-Methylpropan-2-ol", why="It is a tertiary alcohol with no [[CH3CH(OH)-]] group."),
        ], steps=[S("The group needed", text="The iodoform test needs the group [[CH3CH(OH)-]] (or ethanol). Butan-2-ol [[CH3CH(OH)CH2CH3]] has it.")],
           concept="Iodoform test", skill="Application", hint="Look for a methyl group on the carbon that carries the -OH.",
           feedback="Butan-2-ol contains CH3CH(OH)-."),
        MC("How can ethanal be collected when ethanol is oxidised with acidified dichromate?", [
            C("Distil it off as soon as it forms", correct=True),
            C("Heat under reflux with excess dichromate", why="Under reflux the ethanal stays in the flask and is oxidised on to ethanoic acid."),
            C("Add a catalyst of concentrated sulfuric acid", why="Sulfuric acid is the catalyst for esterification and dehydration, not a way to stop oxidation."),
            C("Use a tertiary alcohol instead", why="A tertiary alcohol cannot be oxidised, so no ethanal would form."),
        ], steps=[S("Boiling points", text="Ethanal (boiling point 21 °C) boils far below ethanol (78 °C), so it can be distilled off before it is oxidised further.")],
           concept="Oxidation of primary alcohols", skill="Application", hint="Aldehydes boil lower than alcohols. How can you use that?",
           feedback="Distil the aldehyde as it forms."),
        NUM("36.0 g of glucose [[C6H12O6]] are fermented completely: [[C6H12O6 -> 2C2H5OH + 2CO2]]. What is the maximum mass of ethanol, in g? (Ar: C 12, H 1, O 16.)", 18.4, tolerance=0.1,
            steps=[S("Moles of glucose", math=r"n = \dfrac{36.0}{180} = 0.200\ \text{mol}"),
                   S("Moles of ethanol (ratio 1 : 2)", math=r"0.200 \times 2 = 0.400\ \text{mol}"),
                   S("Mass", math=r"0.400 \times 46 = 18.4\ \text{g}")],
            unit="g", concept="Fermentation", skill="Calculation", hint="Find the moles of glucose, then use the 1 : 2 ratio to ethanol.",
            feedback="0.400 mol of ethanol of Mr 46 is 18.4 g."),
        MC("Ethene is made from ethanol in the laboratory by heating the ethanol with", [
            C("aqueous sodium hydroxide", why="This is the reagent for hydrolysis of haloalkanes, not dehydration of an alcohol."),
            C("concentrated sulfuric acid at about 170 °C", correct=True),
            C("acidified potassium dichromate(VI)", why="This oxidises ethanol to ethanal or ethanoic acid."),
            C("sodium metal", why="Sodium makes sodium ethoxide and hydrogen."),
        ], steps=[S("Dehydration", text="[[CH3CH2OH -> CH2=CH2 + H2O]] with concentrated [[H2SO4]] at about 170 °C (or hot [[Al2O3]]).")],
           concept="Dehydration of alcohols", skill="Recall", hint="Which reagent removes the elements of water from ethanol?",
           feedback="A dehydrating agent such as concentrated sulfuric acid is needed."),
        MC("A compound [[C3H8O]] does not react with sodium. It is", [
            C("propan-1-ol", why="Propan-1-ol has an -OH group and reacts with sodium."),
            C("propan-2-ol", why="Propan-2-ol also has an -OH group and reacts with sodium."),
            C("propanal", why="Propanal has the formula [[C3H6O]], not [[C3H8O]]."),
            C("methoxyethane", correct=True),
        ], steps=[S("Which isomer has no -OH?", text="The isomers of [[C3H8O]] are propan-1-ol, propan-2-ol and methoxyethane. Only the ether has no O-H bond, so it does not react with sodium.")],
           concept="Functional-group isomers", skill="Reasoning", hint="Sodium reacts with the O-H group. Which isomer has none?",
           feedback="The ether has no O-H group."),
        MC("Propan-2-ol is heated under reflux with excess acidified potassium dichromate(VI). The organic product is", [
            C("propanal", why="Propanal comes from propan-1-ol, a primary alcohol."),
            C("propanoic acid", why="Propanoic acid comes from propan-1-ol with excess oxidant."),
            C("propanone", correct=True),
            C("propene", why="Propene is a dehydration product, not an oxidation product."),
        ], steps=[S("Secondary alcohol", text="[[CH3CH(OH)CH3 + O -> CH3COCH3 + H2O]]: propanone, which resists further oxidation.")],
           concept="Oxidation of secondary alcohols", skill="Application", hint="Is propan-2-ol primary, secondary or tertiary?",
           feedback="Secondary alcohols give ketones."),
    ])]
# ------------------------------------------------------------------ Examination: Paper 1 technique
SETS += [practice_set(
    module=M_EXAM, topic="Paper 1",
    title="Paper 1 technique: question types and calculation traps", lesson="chxl-paper-1-multiple-choice-strategy",
    questions=[
        MC("What mass of sodium hydroxide (Mr = 40.0) is needed to make 250 cm³ of a 0.200 mol/dm³ solution?", [
            C("0.500 g", why="The moles are 0.0500 mol and 0.0500 × 40.0 = 2.00 g; this value is a decimal-place slip."),
            C("8.00 g", why="This is the mass for 1 dm³ of the solution; the volume is only 250 cm³."),
            C("2.00 g", correct=True),
            C("10.0 g", why="You forgot to multiply by the concentration 0.200: 0.250 × 40 = 10.0."),
        ], steps=[S("Moles", math=r"n = cV = 0.200 \times 0.250 = 0.0500\ \text{mol}"),
                  S("Mass", math=r"m = nM = 0.0500 \times 40.0 = 2.00\ \text{g}")],
           concept="Question types and calculation traps", skill="Calculation", hint="Convert the volume to dm³ first, then find the moles.",
           feedback="n = cV then m = nM."),
        MC("Which of these are structural isomers of [[C4H10O]]? 1  butan-2-ol   2  ethoxyethane   3  butanal", [
            C("1, 2 and 3", why="Butanal is [[C4H8O]]: it has two fewer hydrogen atoms, so it is not an isomer."),
            C("1 and 2 only", correct=True),
            C("2 and 3 only", why="Statement 3 is incorrect (butanal is [[C4H8O]])."),
            C("1 only", why="Ethoxyethane [[CH3CH2OCH2CH3]] is also [[C4H10O]]: a functional-group isomer."),
        ], steps=[S("Test each statement", text="Butan-2-ol [[C4H10O]]: yes. Ethoxyethane [[C4H10O]]: yes. Butanal [[C4H8O]]: no."),
                  S("Choose the combination", text="Only 1 and 2.")],
           concept="Question types and calculation traps", skill="Application", hint="Work out the molecular formula of each statement separately.",
           feedback="Check each statement against the formula [[C4H10O]]."),
        MC("Assertion: Propan-2-ol can be oxidised by acidified potassium dichromate(VI) to propanal. Reason: Propan-2-ol is a secondary alcohol. Choose: A both true and the reason explains the assertion; B both true but the reason does not explain the assertion; C assertion true, reason false; D assertion false, reason true.", [
            C("A", why="The assertion is false: propan-2-ol gives propanone, not propanal."),
            C("B", why="The assertion is false, so this option cannot apply."),
            C("C", why="The reason is true: propan-2-ol is secondary."),
            C("D", correct=True),
        ], steps=[S("Assertion", text="Propan-2-ol (secondary) is oxidised to propanone, not propanal. **False**."),
                  S("Reason", text="Propan-2-ol is a secondary alcohol. **True**."),
                  S("Choose", text="Assertion false, reason true: D.")],
           concept="Question types and calculation traps", skill="Reasoning", hint="Check each statement on its own first. What does a secondary alcohol give on oxidation?",
           feedback="False assertion, true reason."),
        NUM("0.50 g of calcium carbonate (Mr = 100) is heated until it decomposes completely: [[CaCO3 -> CaO + CO2]]. What volume of carbon dioxide forms at rtp, in cm³? (Molar volume 24 dm³ at rtp.)", 120, tolerance=1,
            steps=[S("Moles", math=r"n = \dfrac{0.50}{100} = 5.0\times10^{-3}\ \text{mol}"),
                   S("Volume in dm³", math=r"V = 5.0\times10^{-3} \times 24 = 0.120\ \text{dm}^3"),
                   S("Convert to cm³", math=r"0.120 \times 1000 = 120\ \text{cm}^3")],
            unit="cm³", concept="Question types and calculation traps", skill="Calculation", hint="The question asks for cm³. Remember 1 dm³ = 1000 cm³.",
            feedback="0.120 dm³ is 120 cm³."),
        MC("Which statement about hydrogen bonding is **NOT** correct?", [
            C("It occurs between molecules of hydrogen sulfide, [[H2S]], giving it a high boiling point.", correct=True),
            C("It explains why water has a higher boiling point than hydrogen sulfide.", why="This is correct: water molecules hydrogen-bond; [[H2S]] molecules do not significantly."),
            C("It occurs between molecules of ammonia.", why="This is correct: N-H bonds with a lone pair on N allow hydrogen bonding."),
            C("It is a force between molecules that is weaker than a covalent bond.", why="This is correct: hydrogen bonds are weaker than covalent bonds."),
        ], steps=[S("The stem says NOT", text="Find the false statement. Sulfur is not electronegative enough for significant hydrogen bonding, and [[H2S]] has a low boiling point (about −60 °C).")],
           concept="Question types and calculation traps", skill="Concept", hint="Underline NOT. Which statement is false?",
           feedback="H2S does not form significant hydrogen bonds."),
        MC("25.0 cm³ of acidified iron(II) sulfate solution need 20.0 cm³ of 0.0200 mol/dm³ potassium manganate(VII) for complete reaction. What is the concentration of iron(II) ions? ([[MnO4^- + 8H^+ + 5Fe^2+ -> Mn^2+ + 5Fe^3+ + 4H2O]])", [
            C("0.0160 mol/dm³", why="You used a 1 : 1 ratio instead of 1 : 5."),
            C("0.0320 mol/dm³", why="You multiplied the moles of manganate(VII) by 2 instead of 5."),
            C("0.0800 mol/dm³", correct=True),
            C("0.400 mol/dm³", why="You multiplied by 5 twice or forgot to divide by the volume of the iron(II) solution."),
        ], steps=[S("Moles of manganate(VII)", math=r"0.0200 \times 0.0200 = 4.00\times10^{-4}\ \text{mol}"),
                  S("Ratio 1 : 5", math=r"n(\mathrm{Fe^{2+}}) = 5 \times 4.00\times10^{-4} = 2.00\times10^{-3}\ \text{mol}"),
                  S("Concentration", math=r"c = \dfrac{2.00\times10^{-3}}{0.0250} = 0.0800\ \text{mol/dm}^3")],
           concept="Question types and calculation traps", skill="Calculation", hint="Use the mole ratio in the equation, then divide by the volume of the iron(II) solution in dm³.",
           feedback="5 Fe²⁺ react with 1 MnO₄⁻."),
        MC("Standard enthalpies of formation (kJ/mol): [[C3H8(g)]] −104, [[CO2(g)]] −394, [[H2O(l)]] −286. What is the standard enthalpy of combustion of propane?", [
            C("−1364 kJ/mol", why="You counted only one water molecule. The equation gives four."),
            C("−2430 kJ/mol", why="You added the enthalpy of formation of propane instead of subtracting it (reactants are subtracted)."),
            C("+2222 kJ/mol", why="Combustion is exothermic, so the sign is negative."),
            C("−2222 kJ/mol", correct=True),
        ], steps=[S("Equation", math=r"\mathrm{C_3H_8} + 5\mathrm{O_2} \rightarrow 3\mathrm{CO_2} + 4\mathrm{H_2O(l)}"),
                  S("Products minus reactants", math=r"3(-394) + 4(-286) - (-104) = -1182 - 1144 + 104 = -2222\ \text{kJ/mol}")],
           concept="Question types and calculation traps", skill="Calculation", hint="Write the balanced equation, then subtract the reactants' enthalpies from the products'.",
           feedback="Products minus reactants, with the right multipliers."),
        MC("You have spent three minutes on a difficult Paper 1 question and are not sure of the answer. What is the best action?", [
            C("Keep working until you are certain", why="This costs time that could earn marks on easier questions."),
            C("Mark a provisional answer, flag the question and return to it later", correct=True),
            C("Leave it blank and never come back", why="If no penalty is stated for wrong answers, a considered guess scores; a blank cannot."),
            C("Choose at random without reading the options", why="Reading the options and eliminating wrong ones improves your chance of a correct guess."),
        ], steps=[S("Time plan", text="Use a quick first pass, flag hard questions, and use the second pass. Keep a few minutes at the end to check that every question has an answer.")],
           concept="Question types and calculation traps", skill="Application", hint="Think about the value of time across all 50 questions.",
           feedback="Flag and return."),
    ])]
# ------------------------------------------------------------------ Examination: Paper 2 technique
SETS += [practice_set(
    module=M_EXAM, topic="Paper 2",
    title="Paper 2 technique: command words, calculations and organic answers", lesson="chxl-paper-2-structured-questions",
    questions=[
        MC("A question begins 'Deduce the structure of compound Q.' What must your answer show?", [
            C("The structure, worked out from the information given, with the reasoning steps", correct=True),
            C("The name of the compound with no explanation", why="'Deduce' asks you to work something out from information; the reasoning is marked."),
            C("A definition of the compound's functional group", why="That would answer 'define', not 'deduce'."),
            C("A list of all possible isomers of the formula", why="You are asked for the one structure that fits the evidence."),
        ], steps=[S("Command word", text="Deduce means work out an answer from given information. Show how each piece of evidence leads to the structure.")],
           concept="Command words", skill="Concept", hint="Think about what the command word asks you to do with the data.",
           feedback="Deduce: work out from the evidence and show the steps."),
        MC("A calculation uses data given as 25.0 cm³, 0.0200 mol/dm³ and 24.25 cm³. How many significant figures should the final answer have?", [
            C("2", why="The least precise datum, 0.0200 or 25.0, has three significant figures."),
            C("3", correct=True),
            C("4", why="Only the titre has four significant figures; the final answer is limited by the least precise value."),
            C("As many as the calculator shows", why="Calculator digits do not reflect the precision of the measurements."),
        ], steps=[S("Least precise datum", text="25.0 (3 s.f.), 0.0200 (3 s.f.) and 24.25 (4 s.f.): the answer is limited to 3 significant figures.")],
           concept="Setting out calculations", skill="Application", hint="The answer cannot be more precise than the least precise measurement.",
           feedback="Three significant figures."),
        NUM("A gas mixture contains 0.20 mol of [[CO2]] and 0.30 mol of [[N2]] at a total pressure of 150 kPa. What is the partial pressure of [[CO2]] in kPa?", 60, tolerance=0.5,
            steps=[S("Mole fraction", math=r"x(\mathrm{CO_2}) = \dfrac{0.20}{0.50} = 0.40"),
                   S("Partial pressure", math=r"p = 0.40 \times 150 = 60\ \text{kPa}")],
            unit="kPa", concept="Partial pressure", skill="Calculation", hint="Find the mole fraction of CO2 first, then multiply by the total pressure.",
            feedback="p = mole fraction x total pressure."),
        MC("Which description of the curly arrows in the first (slow) step of the SN1 hydrolysis of 2-bromo-2-methylpropane is correct?", [
            C("An arrow from the lone pair of [[OH^-]] to the carbon atom", why="This is the second, fast step in SN1 (attack on the carbocation)."),
            C("An arrow from the carbon atom to the bromine atom", why="Arrows start at electrons (the bond), not at an atom."),
            C("A half-headed arrow from the C-Br bond to each atom", why="Half-headed arrows show radical (homolytic) reactions, not this heterolytic step."),
            C("An arrow from the middle of the C-Br bond to the bromine atom", correct=True),
        ], steps=[S("First step", text="The C-Br bond breaks heterolytically: the bond pair moves to Br, giving [[(CH3)3C^+]] and [[Br^-]].")],
           concept="Mechanism answers", skill="Application", hint="In the slow step of SN1 only the haloalkane is involved.",
           feedback="The arrow runs from the bond to bromine."),
        MC("A compound contains 40.0% carbon, 6.7% hydrogen and 53.3% oxygen by mass and has a relative molecular mass of 60. What is its molecular formula? (Ar: C 12, H 1, O 16)", [
            C("[[CH2O]]", why="This is the empirical formula, with mass 30. The molecular mass is 60, which is twice that."),
            C("[[C2H4O2]]", correct=True),
            C("[[C3H6O3]]", why="This would have a relative molecular mass of 90."),
            C("[[C2H6O2]]", why="This has the wrong hydrogen content (about 9.7% H) and mass 62."),
        ], steps=[S("Ratio", math=r"\dfrac{40.0}{12} : \dfrac{6.7}{1} : \dfrac{53.3}{16} = 3.33 : 6.7 : 3.33 = 1 : 2 : 1"),
                  S("Scale up", text="Empirical formula [[CH2O]] (30). 60/30 = 2, so the molecular formula is [[C2H4O2]].")],
           concept="Formulae from data", skill="Calculation", hint="Find the empirical formula, then compare its mass with the relative molecular mass.",
           feedback="Molecular formula = n x empirical formula."),
        MC("Which answer earns full marks for 'Distinguish between ethane and ethene'?", [
            C("Ethene is an alkene and ethane is an alkane", why="This states what they are but gives no test."),
            C("Heat both strongly; ethene burns", why="Both burn, so this does not distinguish them."),
            C("Shake each with bromine water: ethene turns it from orange to colourless; ethane gives no change", correct=True),
            C("Add aqueous sodium hydroxide to each", why="Neither reacts with aqueous alkali."),
        ], steps=[S("Test, observation, inference", text="Bromine water adds across the C=C of ethene, so it is decolourised. Ethane has no C=C, so the colour stays orange.")],
           concept="Distinguishing tests", skill="Application", hint="A good answer names the reagent and gives the result for each compound.",
           feedback="Name the reagent and give both results."),
        MC("1.30 g of zinc react with excess dilute hydrochloric acid: [[Zn + 2HCl -> ZnCl2 + H2]]. What volume of hydrogen forms at rtp? (Ar: Zn 65; molar volume 24 dm³)", [
            C("0.48 dm³", correct=True),
            C("0.24 dm³", why="This is the volume for 0.65 g. The mass here is 1.30 g, so double it."),
            C("0.96 dm³", why="You doubled for the 2 in 2HCl, but the ratio Zn : [[H2]] is 1 : 1."),
            C("0.020 dm³", why="0.020 is the number of moles, not the volume."),
        ], steps=[S("Moles", math=r"n(\mathrm{Zn}) = \dfrac{1.30}{65} = 0.0200\ \text{mol}"),
                  S("Ratio 1 : 1", text="n([[H2]]) = 0.0200 mol."),
                  S("Volume", math=r"V = 0.0200 \times 24 = 0.48\ \text{dm}^3")],
           concept="Setting out calculations", skill="Calculation", hint="Use the mole ratio of zinc to hydrogen in the equation.",
           feedback="n = 0.0200 mol; V = 0.48 dm³."),
        MC("How do you draw the enantiomer of a molecule with one chiral centre, such as alanine?", [
            C("Rotate the drawing by 180° in the plane of the paper", why="Rotating in the plane gives the same molecule, not its mirror image."),
            C("Replace [[NH2]] by [[OH]]", why="That makes a different compound (lactic acid), not the enantiomer."),
            C("Put both [[CH3]] and H on wedge bonds", why="This does not represent a tetrahedral centre properly and does not generate the mirror image."),
            C("Swap the wedge and dashed groups, giving the mirror image", correct=True),
        ], steps=[S("Mirror image", text="Keep two groups in the plane and swap the groups on the wedge and dash bonds. The mirror image cannot be superimposed on the original.")],
           concept="Optical isomers", skill="Application", hint="Think of the mirror: a wedge bond becomes a dash bond in the reflection.",
           feedback="Swapping a wedge and a dash gives the enantiomer."),
    ])]
# ------------------------------------------------------------------ Examination: Paper 3 practical skills
SETS += [practice_set(
    module=M_EXAM, topic="Paper 3",
    title="Paper 3 skills: titrations, recording and qualitative tests", lesson="chxl-paper-3-practical-skills",
    questions=[
        MC("Which burette reading is recorded correctly?", [
            C("24.3 cm³", why="A burette is read to 0.05 cm³, so the reading needs two decimal places."),
            C("24.30 cm³", correct=True),
            C("24.300 cm³", why="Three decimal places claim more precision than a burette gives."),
            C("24 cm³", why="This throws away the precision of the instrument."),
        ], steps=[S("Convention", text="Burette readings are recorded to two decimal places, ending in 0 or 5.")],
           concept="Recording results", skill="Recall", hint="Think about the smallest division on a burette.",
           feedback="Two decimal places."),
        MC("Which acid is used to acidify a titration of iron(II) with potassium manganate(VII)?", [
            C("Dilute hydrochloric acid", why="Chloride ions are oxidised by permanganate, so the titre would be too large."),
            C("Dilute nitric acid", why="Nitric acid is itself an oxidising agent and interferes with the result."),
            C("Ethanoic acid", why="It is too weak to provide enough hydrogen ions."),
            C("Dilute sulfuric acid", correct=True),
        ], steps=[S("Choose an acid that does not react", text="Sulfate ions do not react with permanganate or iron(II), so dilute sulfuric acid is used.")],
           concept="End-points and reagents", skill="Recall", hint="Which acid does not take part in a redox reaction with permanganate?",
           feedback="Dilute sulfuric acid is the standard choice."),
        NUM("25.0 cm³ of iron(II) solution need 15.00 cm³ of 0.0200 mol/dm³ potassium manganate(VII). What is the concentration of iron(II) in mol/dm³? ([[MnO4^- + 8H^+ + 5Fe^2+ -> Mn^2+ + 5Fe^3+ + 4H2O]])", 0.0600, tolerance=0.0005,
            steps=[S("Moles of manganate(VII)", math=r"0.0200 \times 0.01500 = 3.00\times10^{-4}\ \text{mol}"),
                   S("Ratio 1 : 5", math=r"n(\mathrm{Fe^{2+}}) = 1.50\times10^{-3}\ \text{mol}"),
                   S("Concentration", math=r"c = \dfrac{1.50\times10^{-3}}{0.0250} = 0.0600\ \text{mol/dm}^3")],
            unit="mol/dm³", concept="Redox titration calculation", skill="Calculation", hint="Use the 1 : 5 ratio, then divide by the volume of the iron(II) solution in dm³.",
            feedback="0.0600 mol/dm³."),
        MC("A solution gives a pale blue precipitate with aqueous ammonia that dissolves in excess to give a deep blue solution. Which ion is present?", [
            C("[[Cu^2+]]", correct=True),
            C("[[Fe^2+]]", why="Iron(II) gives a green precipitate that does not dissolve in excess ammonia."),
            C("[[Zn^2+]]", why="Zinc gives a white precipitate that dissolves in excess ammonia."),
            C("[[Fe^3+]]", why="Iron(III) gives a red-brown precipitate that does not dissolve in excess."),
        ], steps=[S("Match to the table", text="A pale blue precipitate dissolving to a deep blue solution in excess ammonia is characteristic of copper(II).")],
           concept="Qualitative tests for cations", skill="Recall", hint="Think of the colours: pale blue, then deep blue.",
           feedback="Copper(II) forms the deep blue tetraammine complex."),
        MC("The titres of a titration are 23.40 (rough), 22.85, 22.80 and 22.90 cm³. What mean titre should be reported?", [
            C("22.99 cm³", why="This averages all four, including the rough titre, which is not concordant."),
            C("22.83 cm³", why="22.90 is concordant with the other two accurate titres (within 0.10 cm³) and should be included."),
            C("22.85 cm³", correct=True),
            C("22.80 cm³", why="The mean uses all concordant titres; do not choose the smallest."),
        ], steps=[S("Select concordant values", text="Leave out the rough titre. 22.85, 22.80 and 22.90 lie within 0.10 cm³."),
                  S("Mean", math=r"\dfrac{22.85 + 22.80 + 22.90}{3} = 22.85\ \text{cm}^3")],
           concept="Concordant titres", skill="Calculation", hint="Which results lie within 0.10 cm³ of each other?",
           feedback="Mean of the three concordant titres."),
        MC("A titre of 25.00 cm³ is obtained from two burette readings, each with an uncertainty of ±0.05 cm³. What is the percentage error in the titre?", [
            C("0.20%", why="This uses only one reading's uncertainty (0.05). A titre uses two readings, so the uncertainty is 0.10 cm³."),
            C("0.40%", correct=True),
            C("0.040%", why="A slip of a factor of ten: 0.10 / 25.00 = 0.0040, which is 0.40%."),
            C("4.0%", why="The uncertainty is 0.10 cm³, which is 0.40% of 25.00 cm³, not 4%."),
        ], steps=[S("Total uncertainty", text="Two readings: ±0.05 ± 0.05 = ±0.10 cm³."),
                  S("Percentage", math=r"\dfrac{0.10}{25.00} \times 100 = 0.40\%")],
           concept="Percentage error", skill="Calculation", hint="A titre is the difference between two readings, each with its own uncertainty.",
           feedback="0.10 / 25.00 x 100 = 0.40%."),
        MC("In a thermometric titration the rising line is T = 20.0 + 0.50V and the falling line is T = 36.0 − 0.10V (T in °C, V in cm³). At what volume do the lines intersect?", [
            C("16.0 cm³", why="At 16.0 cm³ the lines give 28.0 and 34.4 °C, which are not equal."),
            C("32.0 cm³", why="At 32.0 cm³ the lines give 36.0 and 32.8 °C, which are not equal."),
            C("24.0 cm³", why="At 24.0 cm³ the lines give 32.0 and 33.6 °C, which are not equal."),
            C("26.7 cm³", correct=True),
        ], steps=[S("Equate the lines", math=r"20.0 + 0.50V = 36.0 - 0.10V"),
                  S("Solve", math=r"0.60V = 16.0 \;\Rightarrow\; V = 26.7\ \text{cm}^3")],
           concept="Thermometric titration", skill="Calculation", hint="Set the two equations equal and solve for V.",
           feedback="0.60V = 16.0 gives V = 26.7."),
        MC("Which test distinguishes methanoic acid from ethanoic acid?", [
            C("Add sodium hydrogencarbonate: only methanoic acid fizzes", why="Both are carboxylic acids and both give carbon dioxide."),
            C("Add litmus: only methanoic acid turns it red", why="Both acids turn litmus red."),
            C("Warm with Tollens' reagent: methanoic acid gives a silver mirror; ethanoic acid does not", correct=True),
            C("Add water: only methanoic acid dissolves", why="Both are fully miscible with water."),
        ], steps=[S("The aldehyde-like group", text="Methanoic acid [[HCOOH]] contains an H-C(=O)- unit and is oxidised easily, so it reduces Tollens' reagent. Ethanoic acid does not.")],
           concept="Qualitative tests for organic compounds", skill="Application", hint="Which acid also behaves a little like an aldehyde?",
           feedback="Only methanoic acid gives a silver mirror."),
    ])]
# ------------------------------------------------------------------ Paper 1 mock exam A (50 questions)
# Allocation: Mole 6, Atomic structure 8, Bonding 8, States of matter 5, Energetics 9, Equilibria 6, Organic 8.
_POS = [2, 0, 3, 1, 1, 3, 0, 2]
_P1 = []


def Q(topic, prompt, right, wrongs, step, hint, skill, math=""):
    """One mock question: `wrongs` is a list of three (text, why) pairs; the correct option position cycles A-D."""
    pos = _POS[len(_P1) % 8] if len(_P1) < 48 else (0 if len(_P1) == 48 else 3)
    opts = [C(t, why=w) for t, w in wrongs]
    opts.insert(pos, C(right, correct=True))
    _P1.append(MC(prompt, opts, steps=[S("Working", math=math, text=step)], concept=topic, skill=skill, hint=hint,
                  feedback="Check the working in the solution."))


T1, T2, T3, T4 = ("Avogadro constant and the ideal gas equation", "Formulae from combustion data",
                  "Acid-base and back titrations", "Redox titrations")
Q(T1, "How many atoms are present in 0.50 mol of ammonia, [[NH3]]? (Avogadro constant 6.02 × 10²³ mol⁻¹)", "1.20 × 10²⁴",
  [("3.01 × 10²³", "This counts molecules only. Each molecule has four atoms."), ("2.41 × 10²⁴", "This doubles the correct number; 0.50 × 4 = 2.0 mol of atoms, not 4.0."),
   ("6.02 × 10²³", "This is the number of particles in 1.0 mol, not 2.0 mol of atoms.")],
  "Each molecule has 1 N + 3 H = 4 atoms. Atoms = 0.50 × 4 × 6.02 × 10²³ = 1.20 × 10²⁴.", "Count atoms per molecule first.", "Calculation")
Q(T1, "What volume is occupied by 0.0500 mol of an ideal gas at 300 K and 100 kPa? (R = 8.314 J mol⁻¹ K⁻¹)", "1.25 dm³",
  [("1.25 cm³", "The value in dm³ was read as cm³; 1 dm³ = 1000 cm³."), ("12.5 dm³", "Slip of a factor of ten in the arithmetic."), ("0.0125 dm³", "Slip of a factor of one hundred; check the pressure conversion.")],
  "V = nRT/P = 0.0500 × 8.314 × 300 / 100 000 = 1.25 × 10⁻³ m³ = 1.25 dm³.", "Convert the pressure to pascals.", "Calculation")
Q(T2, "0.74 g of a compound of carbon, hydrogen and oxygen burns to give 1.76 g of carbon dioxide and 0.90 g of water. What is its empirical formula? (Ar: C 12, H 1, O 16; Mr: [[CO2]] 44, [[H2O]] 18)", "[[C4H10O]]",
  [("[[C2H5O]]", "This is the correct ratio of C to H but the oxygen is wrong: 0.16 g of O is 0.010 mol, giving C : H : O = 4 : 10 : 1."), ("[[C4H8O]]", "The hydrogen is 0.10 mol, not 0.08 mol."), ("[[C3H8O]]", "The carbon is 0.040 mol, not 0.030 mol.")],
  "C: 1.76/44 = 0.040 mol (0.48 g). H: 2 × 0.90/18 = 0.10 mol (0.10 g). O: 0.74 − 0.58 = 0.16 g = 0.010 mol. Ratio C : H : O = 4 : 10 : 1.", "Find the mass of oxygen by difference.", "Calculation")
Q(T2, "20 cm³ of a gaseous hydrocarbon are burnt in 100 cm³ of oxygen (excess). After cooling to room temperature, the volume is 70 cm³; potassium hydroxide solution then removes 40 cm³. What is the formula of the hydrocarbon?", "[[C2H6]]",
  [("[[C2H4]]", "With C2H4 the oxygen used would be 60 cm³, leaving 40 cm³ of oxygen and a total of 80 cm³."), ("[[C3H6]]", "CO2 would be 60 cm³, but only 40 cm³ was absorbed."), ("[[C2H2]]", "With C2H2 the oxygen used would be 50 cm³ and the total after combustion would be 90 cm³.")],
  "CO2 = 40 cm³, so x = 2. Oxygen left = 70 − 40 = 30 cm³, so 70 cm³ used = 20(x + y/4), giving y = 6.", "The gas removed by KOH is carbon dioxide.", "Reasoning")
Q(T3, "1.00 g of impure calcium carbonate is added to 50.0 cm³ of 0.500 mol/dm³ hydrochloric acid (excess). The excess acid needs 30.00 cm³ of 0.200 mol/dm³ sodium hydroxide. What is the percentage of [[CaCO3]] in the sample? (Mr = 100)", "95.0%",
  [("47.5%", "You halved twice; one mole of CaCO₃ reacts with 2 mol of HCl, applied once."), ("190%", "You forgot the 1 : 2 ratio; a purity above 100% is impossible."), ("5.00%", "This is the percentage of impurity, not of calcium carbonate.")],
  "HCl added = 0.0250 mol; excess = 0.200 × 0.0300 = 0.00600 mol; used = 0.0190 mol; CaCO₃ = 0.00950 mol = 0.950 g, so 95.0%.", "A back titration: find the acid that was NOT used up.", "Calculation")
Q(T4, "In acid solution: [[2MnO4^- + 5C2O4^2- + 16H^+ -> 2Mn^2+ + 10CO2 + 8H2O]]. 20.0 cm³ of 0.0100 mol/dm³ potassium manganate(VII) react completely with ethanedioate ions. How many moles of ethanedioate react?", "5.00 × 10⁻⁴",
  [("8.00 × 10⁻⁵", "You used the ratio 2/5 instead of 5/2."), ("2.00 × 10⁻⁴", "This is the number of moles of manganate(VII); the ratio to ethanedioate is 2 : 5."), ("1.00 × 10⁻³", "You multiplied by 5 instead of 5/2.")],
  "n(MnO₄⁻) = 0.0100 × 0.0200 = 2.00 × 10⁻⁴ mol. n(C₂O₄²⁻) = 2.00 × 10⁻⁴ × 5/2 = 5.00 × 10⁻⁴ mol.", "Use the mole ratio 2 : 5 from the equation.", "Calculation")

A1, A2, A3, A4, A5 = ("Subatomic particles", "Mass spectrometry", "Ionization energy trends", "Atomic orbitals and quantum numbers",
                      "Aufbau principle, Hund's rule and the Pauli exclusion principle")
Q(A1, "How many protons, neutrons and electrons are in the ion 56Fe³⁺? (Atomic number of iron is 26)", "26 protons, 30 neutrons, 23 electrons",
  [("26 protons, 30 neutrons, 26 electrons", "Fe³⁺ has lost three electrons, so it has 23."), ("23 protons, 33 neutrons, 26 electrons", "The number of protons is the atomic number, 26, which does not change on ionisation."),
   ("29 protons, 30 neutrons, 26 electrons", "Protons are not gained when a positive ion forms.")],
  "Protons = 26. Neutrons = 56 − 26 = 30. Electrons = 26 − 3 = 23.", "The charge changes only the electrons.", "Application")
Q(A1, "In Rutherford's experiment most alpha particles passed straight through gold foil and a few were deflected through large angles. Which conclusion does this support?", "The atom is mostly empty space with a small, dense, positive nucleus",
  [("Electrons are embedded in a positive sphere", "That is the plum-pudding model, which the experiment disproved."), ("Alpha particles are heavier than gold atoms", "Alpha particles are lighter than gold atoms; the deflections come from the positive nucleus."),
   ("The nucleus contains only neutrons", "The large-angle deflection shows a positive charge, from protons.")],
  "Most particles pass through empty space; the few large deflections come from repulsion by a concentrated positive nucleus.", "Think about what a rare large deflection means.", "Concept")
Q(A2, "Chlorine has two isotopes: 35Cl (75.8%) and 37Cl (24.2%). What is the relative atomic mass of chlorine?", "35.5",
  [("36.0", "This is the simple mean of 35 and 37; it ignores the abundances."), ("35.0", "This is the mass of the most abundant isotope only."), ("37.0", "This is the mass of the less abundant isotope only.")],
  "Ar = (35 × 75.8 + 37 × 24.2)/100 = 35.48, which rounds to 35.5.", "Weight each isotope by its abundance.", "Calculation")
Q(A2, "How many molecular-ion peaks does the mass spectrum of [[Cl2]] show, and what are their approximate relative heights? (Isotopes 35Cl : 37Cl about 3 : 1)", "3 peaks at m/z 70, 72, 74 in the ratio about 9 : 6 : 1",
  [("2 peaks at m/z 35 and 37 in the ratio 3 : 1", "Those are the atomic ion peaks; the molecular ion is the whole molecule."), ("3 peaks at m/z 70, 72, 74 in the ratio 1 : 1 : 1", "The ratio is set by the probabilities of the isotope combinations."),
   ("1 peak at m/z 71", "The molecule has several isotope combinations, 35+35, 35+37 and 37+37.")],
  "Combinations: 35/35 (0.75²), 35/37 (2 × 0.75 × 0.25), 37/37 (0.25²) give 9 : 6 : 1 at m/z 70, 72, 74.", "List the ways the two atoms can be chosen.", "Reasoning")
Q(A3, "The first ionisation energy of aluminium is lower than that of magnesium because", "the outer electron in aluminium is in a 3p orbital, which is higher in energy and better shielded",
  [("aluminium has fewer protons than magnesium", "Aluminium has more protons (13 against 12)."), ("aluminium atoms are larger than magnesium atoms", "Aluminium atoms are slightly smaller across the period."),
   ("the 3s electrons repel the 3p electron less strongly", "The 3s electrons shield the 3p electron, which makes it easier to remove.")],
  "Mg: [Ne]3s²; Al: [Ne]3s²3p¹. The 3p electron is further from the nucleus and shielded by the 3s electrons.", "Compare the sub-shell of the outer electron.", "Reasoning")
Q(A3, "The first four ionisation energies (kJ/mol) of an element are 738, 1450, 7730 and 10 500. To which group of the Periodic Table does it belong?", "Group 2",
  [("Group 1", "A Group 1 element would show a big jump after the first ionisation energy."), ("Group 13", "A Group 13 element would show its big jump after the third."), ("Group 14", "A Group 14 element would show its big jump after the fourth.")],
  "The large jump from the second (1450) to the third (7730) means a third electron comes from an inner shell: two outer electrons, Group 2.", "Look for the biggest jump between successive values.", "Interpretation")
Q(A4, "Which set of quantum numbers (n, l, ml, ms) is **not** allowed for an electron in an atom?", "2, 2, 0, +½",
  [("2, 1, −1, +½", "This describes a 2p electron: allowed."), ("3, 2, 0, −½", "This describes a 3d electron: allowed."), ("1, 0, 0, −½", "This describes a 1s electron: allowed.")],
  "The value of l runs from 0 to n − 1. For n = 2, l can only be 0 or 1, so l = 2 is not allowed.", "Check the rule for l in terms of n.", "Concept")
Q(A5, "What is the electronic configuration of the [[Fe^3+]] ion? (Fe: [Ar]3d⁶4s²)", "[Ar]3d⁵",
  [("[Ar]3d³4s²", "The 4s electrons are lost first when a transition metal ionises."), ("[Ar]3d⁶", "That would be Fe²⁺ (two 4s electrons lost); Fe³⁺ loses one 3d electron as well."), ("[Ar]3d⁴4s¹", "The 4s electrons are removed before the 3d electrons.")],
  "Remove the two 4s electrons, then one 3d electron: [Ar]3d⁵ (a half-filled d sub-shell).", "Which electrons are removed first, 4s or 3d?", "Application")

B1, B2, B3, B4, B5 = ("Ionic bonding and polarization", "Covalent bonding and VSEPR shapes", "Sigma and pi bonds and hybridization",
                      "Metallic bonding", "Dipole moments and hydrogen bonding")
Q(B1, "Which compound is likely to have the greatest covalent character?", "[[AlI3]]",
  [("[[NaF]]", "A small, singly charged cation and a small anion give a mainly ionic compound."), ("[[KCl]]", "A large, singly charged cation polarises little."), ("[[MgCl2]]", "Mg²⁺ polarises Cl⁻, but less than Al³⁺ polarises the larger, more polarisable I⁻.")],
  "Fajans' rules: a small, highly charged cation (Al³⁺) and a large, easily polarised anion (I⁻) give the most covalent character.", "Combine charge, size of cation and size of anion.", "Concept")
Q(B1, "Which cation has the greatest polarising power?", "[[Al^3+]]",
  [("[[Na^+]]", "Larger and singly charged, so lower charge density."), ("[[K^+]]", "Larger and singly charged."), ("[[Mg^2+]]", "Smaller charge than Al³⁺ and a slightly larger radius.")],
  "Polarising power rises with charge and falls with radius: Al³⁺ has the highest charge density.", "Charge divided by size.", "Concept")
Q(B2, "Which species has a square planar shape?", "[[XeF4]]",
  [("[[CH4]]", "Tetrahedral."), ("[[SF4]]", "See-saw shaped, with one lone pair on the central atom."), ("[[NH4^+]]", "Tetrahedral.")],
  "Xe has 4 bonding pairs and 2 lone pairs (6 electron pairs, octahedral arrangement); the lone pairs are opposite each other, leaving a square planar shape.", "Count bonding pairs and lone pairs.", "Application")
Q(B2, "The H-O-H bond angle in water (104.5°) is smaller than the H-N-H bond angle in ammonia (107°) because", "water has two lone pairs on the central atom, which repel the bonding pairs more strongly",
  [("oxygen is less electronegative than nitrogen", "Oxygen is more electronegative than nitrogen."), ("water has three bonding pairs", "Water has two bonding pairs."), ("the O-H bond is longer than the N-H bond", "Bond length does not explain the angle; electron-pair repulsion does.")],
  "Lone pair-bonding pair repulsion is greater than bonding pair-bonding pair repulsion. Water has two lone pairs and ammonia one.", "Count the lone pairs on the central atom.", "Reasoning")
Q(B3, "How many sigma (σ) and pi (π) bonds are there in one molecule of propyne, [[CH3C#CH]]?", "6 sigma and 2 pi",
  [("7 sigma and 1 pi", "The triple bond has one sigma and two pi bonds."), ("5 sigma and 3 pi", "Only the triple bond contains pi bonds, and it has two."), ("8 sigma and 2 pi", "There are only six sigma bonds: three C-H in CH₃, one C-C, one C≡C sigma, and one C-H.")],
  "Sigma: 3 (C-H in CH₃) + 1 (C-C) + 1 (C≡C) + 1 (≡C-H) = 6. Pi: 2 in the triple bond.", "A triple bond is one sigma and two pi bonds.", "Application")
Q(B4, "Magnesium has a higher melting point than sodium because", "each magnesium atom donates two delocalised electrons and the ion is smaller, so the metallic bonding is stronger",
  [("magnesium has a larger atomic radius", "Magnesium ions are smaller than sodium ions."), ("magnesium atoms form covalent bonds", "Both are metals with metallic bonding."), ("sodium has more delocalised electrons", "Sodium donates only one electron per atom, magnesium two.")],
  "Stronger attraction between Mg²⁺ ions and the sea of two delocalised electrons per atom, with a smaller ionic radius.", "Compare charge and size of the ions.", "Reasoning")
Q(B4, "Metals are malleable because", "layers of positive ions can slide over each other while the delocalised electrons keep holding the structure together",
  [("their ions are held in fixed positions by directional covalent bonds", "Metallic bonding is non-directional."), ("the metal ions repel each other and move apart", "The delocalised electrons attract the positive ions."), ("the delocalised electrons are fixed on particular atoms", "The electrons are free to move through the lattice.")],
  "The metallic bond is non-directional, so layers can move without breaking the structure.", "Think about the nature of the bond when layers slide.", "Concept")
Q(B5, "Which molecule has polar bonds but no overall dipole moment?", "[[CO2]]",
  [("[[H2O]]", "Water is bent, so the bond dipoles do not cancel."), ("[[NH3]]", "Ammonia is pyramidal with a lone pair, so it is polar."), ("[[CHCl3]]", "The three C-Cl bonds and one C-H bond give a net dipole.")],
  "CO₂ is linear and symmetrical, so the two C=O dipoles cancel.", "Draw the shape and look for symmetry.", "Concept")

S1, S2, S3 = "Kinetic theory and real gases", "Unit cells and coordination numbers", "Crystal lattices"
Q(S1, "Real gases deviate most from ideal behaviour at", "high pressure and low temperature",
  [("low pressure and high temperature", "At these conditions molecules are far apart and fast-moving, and the gas behaves ideally."), ("low pressure and low temperature", "Low pressure favours ideal behaviour even if temperature is low."),
   ("high pressure and high temperature", "High temperature favours ideal behaviour even if the pressure is high.")],
  "At high pressure the molecules' own volume matters; at low temperature the attractions between molecules matter.", "Which conditions bring molecules close together and slow?", "Concept")
Q(S1, "In the van der Waals equation (P + an²/V²)(V − nb) = nRT, the term nb corrects for", "the volume occupied by the gas molecules themselves",
  [("the attractions between molecules", "That is the 'a' term added to the pressure."), ("the mass of the molecules", "Mass is not corrected in this equation."), ("the temperature of the gas", "Temperature appears separately as T.")],
  "The molecules take up volume, so the free volume is V − nb.", "Which of the two corrections acts on the volume?", "Concept")
Q(S2, "How many atoms belong to one face-centred cubic unit cell, and what is the coordination number of each atom?", "4 atoms; coordination number 12",
  [("2 atoms; coordination number 8", "These are the values for body-centred cubic."), ("1 atom; coordination number 6", "These are the values for simple cubic."), ("4 atoms; coordination number 8", "The atoms per cell are right, but each atom touches 12 neighbours.")],
  "8 corners × 1/8 + 6 faces × 1/2 = 4 atoms. Each atom has 12 nearest neighbours.", "Count corner and face contributions.", "Calculation")
Q(S2, "Which pair is correct for a body-centred cubic metal?", "2 atoms per unit cell; coordination number 8",
  [("4 atoms per unit cell; coordination number 12", "That is face-centred cubic."), ("1 atom per unit cell; coordination number 6", "That is simple cubic."), ("2 atoms per unit cell; coordination number 12", "The atoms per cell are right, but the coordination number is 8.")],
  "8 corners × 1/8 + 1 centre = 2 atoms. The central atom touches the 8 corner atoms.", "Count corner and body atoms.", "Recall")
Q(S3, "In the caesium chloride lattice, the coordination numbers of [[Cs^+]] and [[Cl^-]] are", "8 and 8",
  [("6 and 6", "These are the numbers for the sodium chloride structure."), ("4 and 4", "These are the numbers for the zinc blende structure."), ("12 and 6", "No simple 1 : 1 ionic lattice has these coordination numbers.")],
  "Each Cs⁺ is surrounded by 8 Cl⁻ and vice versa (body-centred arrangement).", "Recall the three common AB structures.", "Recall")

E1, E2, E3, E4, E5, E6 = ("Standard enthalpy changes", "Hess's law", "Bond dissociation energies", "Lattice energy and Born-Haber cycles", "Entropy", "Gibbs free energy")
Q(E1, "Which equation represents the standard enthalpy of formation of ethanol, [[C2H5OH(l)]]?", "[[2C(s) + 3H2(g) + 1/2O2(g) -> C2H5OH(l)]]",
  [("[[C2H4(g) + H2O(l) -> C2H5OH(l)]]", "This is a reaction between compounds, not the formation from elements."), ("[[C2H5OH(l) + 3O2(g) -> 2CO2(g) + 3H2O(l)]]", "This is combustion."),
   ("[[2C(g) + 6H(g) + O(g) -> C2H5OH(l)]]", "This starts from gaseous atoms, not from elements in their standard states.")],
  "Formation: one mole of the compound from its elements in their standard states (carbon as graphite).", "Elements in their standard states only.", "Recall")
Q(E1, "50.0 cm³ of 1.00 mol/dm³ HCl are mixed with 50.0 cm³ of 1.00 mol/dm³ NaOH and the temperature rises by 6.8 K. Calculate the enthalpy of neutralisation. (Assume 1.00 g/cm³ and 4.18 J g⁻¹ K⁻¹)", "−56.8 kJ/mol",
  [("−28.4 kJ/mol", "You divided by 0.100 mol; the reaction is between 0.0500 mol of each."), ("+56.8 kJ/mol", "The reaction is exothermic: the temperature rose, so ΔH is negative."), ("−5.68 kJ/mol", "Slip of a factor of ten when dividing by the moles.")],
  "q = 100 × 4.18 × 6.8 = 2842 J. n = 0.0500 mol. ΔH = −2842/0.0500 = −56.8 kJ/mol.", "Use total mass 100 g and moles of water formed.", "Calculation")
Q(E2, "Standard enthalpies of combustion (kJ/mol): C(graphite) −394; [[H2]] −286; [[C2H5OH(l)]] −1367. What is the standard enthalpy of formation of ethanol?", "−279 kJ/mol",
  [("+279 kJ/mol", "The sign is reversed: reactants and products were subtracted the wrong way round."), ("−3013 kJ/mol", "You added the enthalpy of combustion of ethanol instead of subtracting it."), ("−1367 kJ/mol", "This is the enthalpy of combustion, not of formation.")],
  "ΔHf = 2(−394) + 3(−286) − (−1367) = −788 − 858 + 1367 = −279 kJ/mol.", "Sum of the combustion enthalpies of the elements minus that of the compound.", "Calculation")
Q(E2, "ΔHc of graphite is −393.5 kJ/mol and ΔHc of diamond is −395.4 kJ/mol. What is ΔH for C(graphite) → C(diamond)?", "+1.9 kJ/mol",
  [("−1.9 kJ/mol", "The sign is wrong: you subtracted in the wrong order."), ("−788.9 kJ/mol", "You added the two enthalpies of combustion."), ("+788.9 kJ/mol", "You added the values and reversed the sign.")],
  "ΔH = ΔHc(graphite) − ΔHc(diamond) = −393.5 − (−395.4) = +1.9 kJ/mol.", "Both burn to carbon dioxide: build a Hess cycle.", "Calculation")
Q(E3, "Use the bond energies (kJ/mol): C=C 612, H-H 436, C-C 347, C-H 413. Calculate ΔH for [[C2H4 + H2 -> C2H6]].", "−125 kJ/mol",
  [("+125 kJ/mol", "Energy is released overall; the sign is reversed."), ("−1173 kJ/mol", "This is the energy released in forming bonds only; breaking bonds must be subtracted too."), ("+1048 kJ/mol", "This is only the energy absorbed in breaking bonds.")],
  "Bonds broken: C=C + H-H = 612 + 436 = 1048. Bonds formed: C-C + 2 C-H = 347 + 826 = 1173.", "ΔH = bonds broken − bonds formed.", "Calculation", math=r"\Delta H = 1048 - 1173 = -125\ \text{kJ/mol}")
Q(E4, "Which step in the Born-Haber cycle for sodium chloride is **exothermic**?", "the formation of the solid lattice from gaseous ions",
  [("the sublimation of sodium", "Sublimation is endothermic: energy is needed to separate atoms."), ("the first ionisation energy of sodium", "Removing an electron needs energy."), ("the atomisation of chlorine", "Breaking the Cl-Cl bond needs energy.")],
  "Lattice formation releases energy as the oppositely charged ions come together.", "Which step involves forming bonds only?", "Concept")
Q(E5, "Which change shows the greatest increase in entropy?", "[[CaCO3(s) -> CaO(s) + CO2(g)]]",
  [("[[H2O(g) -> H2O(l)]]", "A gas turning to a liquid reduces entropy."), ("[[N2(g) + 3H2(g) -> 2NH3(g)]]", "Four moles of gas become two moles: entropy decreases."), ("[[2Mg(s) + O2(g) -> 2MgO(s)]]", "A gas is lost, so entropy decreases.")],
  "A gas is produced from a solid: the number of gas molecules and disorder increase greatly.", "Look at the change in the number of moles of gas.", "Reasoning")
Q(E5, "The entropy change of the system for [[N2(g) + 3H2(g) -> 2NH3(g)]] is negative because", "the number of moles of gas decreases from 4 to 2",
  [("the reaction is exothermic", "The sign of ΔH does not decide the entropy change of the system."), ("ammonia is a liquid", "Ammonia is a gas under these conditions."), ("the reaction needs a catalyst", "A catalyst changes the rate, not the entropy change.")],
  "Fewer gas molecules mean fewer ways to arrange energy and particles.", "Count the moles of gas on each side.", "Reasoning")
Q(E6, "For [[CaCO3(s) -> CaO(s) + CO2(g)]], ΔH = +178 kJ/mol and ΔS = +161 J mol⁻¹ K⁻¹. Above approximately what temperature is the decomposition spontaneous?", "1106 K",
  [("1.11 K", "You did not convert ΔH from kJ to J."), ("0.904 K", "You divided ΔS by ΔH, the wrong way round, and mixed units."), ("178 K", "This is the value of ΔH in kJ, not a temperature.")],
  "Spontaneous when ΔG < 0: T > ΔH/ΔS = 178 000 / 161 = 1106 K.", "Set ΔG = 0 and keep units consistent (J).", "Calculation")

K1, K2, K3, K4 = ("Equilibrium constants Kc and Kp", "Le Chatelier's principle in industry", "Raoult's law and fractional distillation", "Steam distillation and the partition coefficient")
Q(K1, "What is the expression for Kc, with units, for [[N2(g) + 3H2(g) <=> 2NH3(g)]]?", "Kc = [NH3]²/([N2][H2]³), units dm⁶ mol⁻²",
  [("Kc = [N2][H2]³/[NH3]², units mol² dm⁻⁶", "The products belong in the numerator."), ("Kc = [NH3]²/([N2][H2]), units dm³ mol⁻¹", "The concentration of hydrogen is raised to its coefficient, 3."),
   ("Kc = 2[NH3]/([N2] + 3[H2]), no units", "Coefficients are powers, not multipliers, and reactants are multiplied.")],
  "Kc = [NH₃]²/([N₂][H₂]³); units = (mol dm⁻³)² / (mol dm⁻³)⁴ = dm⁶ mol⁻².", "Products over reactants, each raised to its coefficient.", "Application")
Q(K1, "At equilibrium [[H2(g) + I2(g) <=> 2HI(g)]] has [H₂] = [I₂] = 0.20 mol/dm³ and [HI] = 1.40 mol/dm³. What is Kc?", "49",
  [("0.020", "You inverted the expression."), ("7.0", "You forgot to square [HI] and divided by only one of the two denominator concentrations (1.40/0.20)."), ("35", "You forgot to square [HI]: 1.40/0.040 = 35.")],
  "Kc = [HI]²/([H₂][I₂]) = 1.40²/(0.20 × 0.20) = 1.96/0.040 = 49.", "Square [HI] because its coefficient is 2.", "Calculation")
Q(K2, "In the Haber process a temperature of about 400-450 °C is used rather than a lower one because", "a lower temperature would give a higher yield but the rate would be too slow",
  [("the reaction is endothermic, so it needs heat", "The synthesis of ammonia is exothermic."), ("a higher temperature increases the equilibrium yield", "For an exothermic reaction, higher temperature decreases the yield."), ("the catalyst only works above 1000 °C", "The iron catalyst works at these moderate temperatures.")],
  "Lower temperature favours the exothermic forward reaction but slows it; a compromise gives an acceptable rate and yield.", "Think of rate and yield together.", "Reasoning")
Q(K2, "For an exothermic gas-phase reaction at equilibrium, which change alters the value of Kc?", "an increase in temperature",
  [("an increase in pressure", "Pressure changes the position of equilibrium but not Kc."), ("adding a catalyst", "A catalyst speeds both reactions equally and does not change Kc."), ("adding more reactant", "This shifts the position of equilibrium; Kc is unchanged.")],
  "Kc depends only on temperature. Raising the temperature of an exothermic reaction decreases Kc.", "Which variable appears in the definition of Kc?", "Concept")
Q(K3, "A and B form an ideal solution with mole fraction of A = 0.40. At the same temperature, pure A has vapour pressure 80 kPa and pure B 40 kPa. What is the total vapour pressure?", "56 kPa",
  [("60 kPa", "This is the simple mean of the two values; mole fractions must be used."), ("48 kPa", "You used 0.40 for both components."), ("120 kPa", "You added the pure vapour pressures without multiplying by mole fractions.")],
  "p = 0.40 × 80 + 0.60 × 40 = 32 + 24 = 56 kPa.", "Raoult's law: partial pressure = mole fraction × vapour pressure of the pure liquid.", "Calculation")
Q(K4, "A solute has a partition coefficient K = [solute in ether] / [solute in water] = 10. In one extraction, 100 cm³ of aqueous solution are shaken with 100 cm³ of ether. What fraction of the solute passes into the ether?", "10/11",
  [("1/11", "This is the fraction left in the water."), ("1/2", "This assumes equal distribution; K = 10 favours ether."), ("10/1", "A fraction cannot exceed 1.")],
  "Let x be the fraction in water: ether : water = 10 : 1, so the fraction in ether is 10/11 (91%).", "With equal volumes the amounts are in the ratio of K.", "Calculation")

O1, O2, O3, O4, O5, O6 = ("Classification and IUPAC nomenclature", "Structural isomerism and stereoisomerism", "Reaction mechanisms", "Alkanes and alkenes", "Alkynes and haloalkanes", "Alcohols")
Q(O1, "What is the IUPAC name of [[(CH3)2CHCH2CH(OH)CH3]]?", "4-methylpentan-2-ol",
  [("2-methylpentan-4-ol", "The -OH must have the lowest possible number."), ("4-methylpentan-1-ol", "The -OH is on carbon 2, not carbon 1."), ("2-methylpentan-2-ol", "Both the position of -OH and of the methyl group are wrong.")],
  "Longest chain with -OH: five carbons. Number from the -OH end: -OH on C2, methyl on C4.", "Give the -OH group the lowest number.", "Application")
Q(O2, "How many structural isomers of [[C5H10]] are acyclic alkenes (ignoring cis-trans isomers)?", "5",
  [("3", "You may have missed the branched isomers."), ("4", "One of the isomers is missing: list the pentenes and the methylbutenes."), ("6", "This count includes cis-trans isomers, which are stereoisomers.")],
  "Pent-1-ene, pent-2-ene, 2-methylbut-1-ene, 3-methylbut-1-ene, 2-methylbut-2-ene.", "Straight chain first, then branched.", "Application")
Q(O2, "How many stereoisomers does pent-3-en-2-ol, [[CH3CH(OH)CH=CHCH3]], have?", "4",
  [("2", "There is a chiral centre and also a C=C that can be E or Z; both count."), ("3", "The stereoisomers come in pairs of enantiomers, so the total cannot be odd here."), ("8", "There is only one chiral centre and one C=C: 2 × 2.")],
  "One chiral centre (C2) gives 2 forms and the C=C gives E and Z: 2 × 2 = 4.", "Find each source of stereoisomerism and multiply.", "Reasoning")
Q(O3, "In the SN1 hydrolysis of 2-bromo-2-methylpropane, which species forms in the slow (rate-determining) step?", "the carbocation [[(CH3)3C^+]]",
  [("the alcohol [[(CH3)3COH]]", "The alcohol forms in the fast second step."), ("a pentavalent transition state with OH and Br both bonded", "That is the SN2 mechanism, not SN1."), ("a free radical [[(CH3)3C.]]", "The bond breaks heterolytically, not homolytically.")],
  "The C-Br bond breaks heterolytically to give the carbocation and bromide ion; this is the slow step.", "Which step involves only the haloalkane?", "Concept")
Q(O4, "Ozone followed by water (with zinc) cleaves [[(CH3)2C=CHCH3]]. What are the products?", "propanone and ethanal",
  [("propanal and ethanal", "The carbon with two methyl groups gives a ketone, propanone, not an aldehyde."), ("propanone only", "The C=C has two ends, each gives a carbonyl compound."), ("2-methylbutane-2,3-diol", "That is the product of cold alkaline permanganate, not ozonolysis.")],
  "C(CH₃)₂= gives (CH₃)₂C=O (propanone); =CHCH₃ gives CH₃CHO (ethanal).", "Each carbon of the C=C becomes C=O.", "Application")
Q(O4, "Which statement about the reaction of methane with chlorine in ultraviolet light is correct?", "It is initiated by homolytic fission of the Cl-Cl bond",
  [("It is an electrophilic addition", "Methane has no double bond, so substitution occurs."), ("It proceeds by heterolytic fission of the C-H bond", "The C-H bond is not polar enough; chlorine radicals are involved."), ("It gives only chloromethane", "Further substitution gives a mixture including [[CH2Cl2]], [[CHCl3]] and [[CCl4]].")],
  "UV light splits Cl₂ into two chlorine radicals (initiation), starting a chain reaction.", "Think about the type of reaction and bond fission.", "Concept")
Q(O5, "Which haloalkane is hydrolysed fastest by warm aqueous sodium hydroxide?", "1-iodopropane",
  [("1-fluoropropane", "The C-F bond is the strongest, so it reacts most slowly."), ("1-chloropropane", "C-Cl is stronger than C-Br and C-I."), ("1-bromopropane", "C-Br is stronger than C-I.")],
  "The C-I bond is the weakest of the carbon-halogen bonds, so it breaks most easily.", "Compare bond enthalpies, not polarity.", "Reasoning")
Q(O6, "Which alcohol is oxidised by acidified potassium dichromate(VI) to a ketone?", "butan-2-ol",
  [("butan-1-ol", "A primary alcohol gives an aldehyde, then a carboxylic acid."), ("2-methylpropan-2-ol", "A tertiary alcohol is not oxidised."), ("2-methylpropan-1-ol", "A primary alcohol gives an aldehyde, then an acid.")],
  "A secondary alcohol, [[CH3CH(OH)CH2CH3]], is oxidised to the ketone butanone.", "Which alcohol is secondary?", "Application")

assert len(_P1) == 50, len(_P1)
SETS += [practice_set(module=M_EXAM, topic="Paper 1", title="Paper 1 mock exam A", lesson="chxl-paper-1-multiple-choice-strategy",
                      mock=True, time_limit_minutes=90, questions=_P1)]

# ------------------------------------------------------------------ Paper 2 practice paper A (27 auto-markable parts)
# KKEVO practice setting: six numbered questions; essay and drawing parts cannot be auto-marked, so only MC and NUM parts appear.
_P2 = []
_MPOS = [1, 3, 0, 2, 2, 0, 3, 1, 1, 3, 0, 2, 0, 2, 3, 1, 0, 2, 1, 3]


def P(topic, label, context, prompt, right, wrongs, step, hint, skill, math=""):
    pos = _MPOS[sum(1 for q in _P2 if q["kind"] == "choice") % len(_MPOS)]
    opts = [C(t, why=w) for t, w in wrongs]
    opts.insert(pos, C(right, correct=True))
    _P2.append(MC(f"**{label}** {context} {prompt}", opts, steps=[S("Working", math=math, text=step)], concept=topic, skill=skill,
                  hint=hint, feedback="Check the working in the solution."))


def N(topic, label, context, prompt, answer, tol, unit, step, hint, skill, math=""):
    _P2.append(NUM(f"**{label}** {context} {prompt}", answer, tolerance=tol, unit=unit, steps=[S("Working", math=math, text=step)],
                   concept=topic, skill=skill, hint=hint, feedback="Check the working in the solution."))


X1 = "A volatile liquid X is analysed. (Ar: C 12, H 1, O 16; R = 8.314 J mol⁻¹ K⁻¹.)"
N("Avogadro constant and the ideal gas equation", "Question 1(a)", X1, "0.600 g of X vaporises to give 200 cm³ of vapour at 373 K and 100 kPa. Calculate the relative molecular mass of X.", 93, 1, "",
  "M = mRT/(PV) with P = 100 000 Pa and V = 2.00 × 10⁻⁴ m³.", "Convert the pressure and volume to SI units first.", "Calculation",
  math=r"M = \dfrac{0.600 \times 8.314 \times 373}{100\,000 \times 2.00\times10^{-4}} = 93.0")
P("Formulae from combustion data", "Question 1(b)", X1, "0.450 g of a different compound Y (C, H and O only) gives 0.660 g of carbon dioxide and 0.270 g of water on complete combustion. What is the empirical formula of Y?",
  "[[CH2O]]", [("[[CHO]]", "The hydrogen is 0.030 mol, twice the 0.015 mol of carbon, not equal to it."), ("[[C2H4O]]", "The oxygen is 0.24 g = 0.015 mol, equal to the carbon; there is not half as much."), ("[[CH4O]]", "The hydrogen is 0.030 mol, giving 2 H per C, not 4.")],
  "C: 0.660/44 = 0.0150 mol. H: 2 × 0.270/18 = 0.0300 mol. O: 0.450 − 0.180 − 0.030 = 0.240 g = 0.0150 mol. C : H : O = 1 : 2 : 1.", "Find the mass of oxygen by difference.", "Calculation")
N("Formulae from combustion data", "Question 1(c)", "Compound Y of part (b) has relative molecular mass 90.", "How many carbon atoms are in one molecule of Y?", 3, 0, "",
  "The empirical formula mass is 30, and 90/30 = 3, so the molecular formula is [[C3H6O3]].", "Divide the relative molecular mass by the empirical formula mass.", "Calculation")
N("Acid-base and back titrations", "Question 1(d)", "25.0 cm³ of sodium hydroxide solution need 20.00 cm³ of 0.100 mol/dm³ hydrochloric acid for neutralisation.", "Calculate the concentration of the sodium hydroxide in mol/dm³.", 0.0800, 0.0005, "mol/dm³",
  "n(HCl) = 0.100 × 0.02000 = 2.00 × 10⁻³ mol = n(NaOH) (1 : 1). c = 2.00 × 10⁻³/0.0250 = 0.0800 mol/dm³.", "Find the moles of acid, then use the 1 : 1 ratio.", "Calculation")

X2 = "Atomic structure and bonding."
N("Mass spectrometry", "Question 2(a)", X2, "An element has two isotopes of mass numbers 10 (20.0% abundance) and 11 (80.0% abundance). Calculate its relative atomic mass to 3 significant figures.", 10.8, 0.05, "",
  "Ar = (10 × 20.0 + 11 × 80.0)/100 = 10.8.", "Weight each mass by its abundance.", "Calculation")
P("Ionization energy trends", "Question 2(b)", X2, "The first ionisation energy of oxygen is lower than that of nitrogen. The best explanation is that", "in oxygen two electrons share one 2p orbital and repel each other, so one is easier to remove",
  [("oxygen has fewer protons than nitrogen", "Oxygen has 8 protons and nitrogen 7."), ("oxygen has a larger atomic radius than nitrogen", "Oxygen is slightly smaller, not larger."), ("oxygen has a half-filled 2p sub-shell", "It is nitrogen, [He]2s²2p³, that has the half-filled sub-shell.")],
  "Nitrogen 2p³ has three unpaired electrons. Oxygen 2p⁴ has a pair in one p orbital; the pairing repulsion lowers the energy needed to remove it.", "Compare the 2p occupancy of N and O.", "Reasoning")
P("Aufbau principle, Hund's rule and the Pauli exclusion principle", "Question 2(c)", X2, "What is the ground-state electronic configuration of chromium (Z = 24)?", "[Ar]3d⁵4s¹",
  [("[Ar]3d⁴4s²", "This follows the simple filling order, but a half-filled 3d sub-shell is more stable in chromium."), ("[Ar]3d⁶", "The 4s orbital keeps one electron."), ("[Ar]4s²4p⁴", "The electrons go into the 3d sub-shell, not 4p.")],
  "Chromium promotes one 4s electron into 3d to give a half-filled d sub-shell, which is more stable.", "Think about half-filled sub-shells.", "Recall")
P("Covalent bonding and VSEPR shapes", "Question 2(d)", X2, "What is the shape of the [[XeF2]] molecule?", "linear, with three lone pairs on xenon",
  [("bent, with two lone pairs on xenon", "Xenon has 2 bonding pairs and 3 lone pairs, not 2."), ("trigonal planar", "There are only two bonded atoms; the lone pairs occupy the equatorial positions."), ("T-shaped", "T-shaped is the shape of [[ClF3]], with two lone pairs.")],
  "Xe has 8 outer electrons; 2 bonds + 3 lone pairs = 5 pairs (trigonal bipyramid). The three lone pairs occupy the equatorial plane, leaving the two F atoms at 180°.", "Count the lone pairs on the central atom.", "Application")
P("Sigma and pi bonds and hybridization", "Question 2(e)", X2, "What is the hybridisation of the carbon atom in carbon dioxide?", "sp",
  [("sp²", "sp² carbon has three sigma bonds; carbon in CO₂ has two."), ("sp³", "sp³ carbon has four sigma bonds."), ("none; carbon uses pure p orbitals", "Hybrid orbitals are needed to explain the 180° angle.")],
  "Carbon in O=C=O has two sigma bonds and two pi bonds: two sp hybrid orbitals, linear.", "Count the sigma bonds around carbon.", "Application")

X3 = "States of matter and solids."
N("Unit cells and coordination numbers", "Question 3(a)", X3, "How many sodium ions belong to one unit cell of sodium chloride (face-centred cubic arrangement of ions)?", 4, 0, "",
  "Sodium ions occupy the edge centres (12 × 1/4 = 3) and the body centre (1): 4 per unit cell, and also 4 chloride ions.", "Count edge and centre positions, with their fractions.", "Calculation")
P("Crystal lattices", "Question 3(b)", X3, "Graphite conducts electricity but diamond does not. The reason is that", "graphite has delocalised electrons that move between its layers, while all four outer electrons of carbon in diamond are in localised bonds",
  [("graphite contains ions", "Graphite is a giant covalent structure with no ions."), ("graphite has a lower melting point than diamond", "Both have very high melting points; melting point does not explain conductivity."), ("diamond has weaker covalent bonds", "The covalent bonds in diamond are very strong.")],
  "Each carbon in graphite bonds to three others, leaving one electron delocalised across the layer.", "Compare the number of bonds per carbon atom.", "Concept")
P("Dipole moments and hydrogen bonding", "Question 3(c)", X3, "Hydrogen fluoride boils at a much higher temperature than hydrogen chloride because", "hydrogen bonds form between HF molecules",
  [("the H-F bond is weaker than the H-Cl bond", "The H-F bond is stronger, and bond strength does not control boiling."), ("HF has a larger relative molecular mass", "HF has the smaller relative molecular mass (20 against 36.5)."), ("HF is an ionic compound", "HF is covalent and molecular.")],
  "Fluorine is small and highly electronegative, so H-F···H-F hydrogen bonds form; HCl has only weaker dipole-dipole forces.", "Which molecule contains H bonded to a very electronegative small atom?", "Reasoning")

X4 = "Energetics. (Specific heat capacity of water 4.18 J g⁻¹ K⁻¹; density 1.00 g/cm³.)"
N("Standard enthalpy changes", "Question 4(a)", X4, "Burning 0.23 g of ethanol (Mr = 46) raises the temperature of 100 g of water by 7.5 K. Calculate the enthalpy change of combustion of ethanol in kJ/mol (include the sign).", -627, 2, "kJ/mol",
  "q = 100 × 4.18 × 7.5 = 3135 J. n = 0.23/46 = 0.0050 mol. ΔH = −3135/0.0050 = −627 000 J/mol = −627 kJ/mol. (The accepted value is about −1367 kJ/mol; heat loss makes this experiment low.)", "q = mcΔT, then divide by the moles burnt.", "Calculation")
N("Hess's law", "Question 4(b)", "Standard enthalpies of formation (kJ/mol): [[C4H10(g)]] −126, [[CO2(g)]] −394, [[H2O(l)]] −286.", "Calculate the standard enthalpy of combustion of butane in kJ/mol.", -2880, 2, "kJ/mol",
  "C₄H₁₀ + 6½O₂ → 4CO₂ + 5H₂O. ΔH = 4(−394) + 5(−286) − (−126) = −1576 − 1430 + 126 = −2880 kJ/mol.", "Products minus reactants, with the right multipliers.", "Calculation")
P("Lattice energy and Born-Haber cycles", "Question 4(c)", X4, "The lattice energy of magnesium oxide is much more exothermic than that of sodium chloride mainly because", "the ions in MgO have higher charges (2+ and 2−) and are smaller",
  [("MgO is more covalent", "Both are mainly ionic; the stronger attraction between 2+ and 2− ions is the cause."), ("the ions in MgO are larger", "The ions in MgO are smaller (Mg²⁺ against Na⁺, O²⁻ against Cl⁻), which strengthens the attraction."), ("MgO has more ions per formula unit", "Lattice energy is per mole of formula units; charges and radii are the key factors.")],
  "Lattice energy rises with the product of the ionic charges and falls with the distance between ions.", "Compare charges and radii.", "Reasoning")
N("Gibbs free energy", "Question 4(d)", "For [[N2(g) + 3H2(g) -> 2NH3(g)]], ΔH = −92 kJ/mol and ΔS = −199 J mol⁻¹ K⁻¹ at 298 K.", "Calculate ΔG at 298 K in kJ/mol.", -32.7, 0.3, "kJ/mol",
  "ΔG = ΔH − TΔS = −92 − 298 × (−0.199) = −92 + 59.3 = −32.7 kJ/mol.", "Convert ΔS to kJ before using it.", "Calculation", math=r"\Delta G = -92 - (298)(-0.199) = -32.7\ \text{kJ/mol}")

X5 = "Equilibria."
P("Equilibrium constants Kc and Kp", "Question 5(a)", X5, "For [[2SO2(g) + O2(g) <=> 2SO3(g)]], what are the expression for Kc and its unit?", "Kc = [SO3]²/([SO2]²[O2]), unit dm³ mol⁻¹",
  [("Kc = [SO3]/([SO2][O2]), unit dm³ mol⁻¹", "Each concentration must be raised to its coefficient."), ("Kc = [SO2]²[O2]/[SO3]², unit mol dm⁻³", "The expression is inverted."), ("Kc = [SO3]²/([SO2]²[O2]), no unit", "The numbers of terms differ (2 against 3), so there is a unit.")],
  "Units: (mol dm⁻³)² / (mol dm⁻³)³ = dm³ mol⁻¹.", "Products over reactants with powers.", "Application")
N("Equilibrium constants Kc and Kp", "Question 5(b)", X5, "At a certain temperature the equilibrium [[PCl5 <=> PCl3 + Cl2]] has [PCl5] = 0.020, [PCl3] = [Cl2] = 0.040 mol/dm³. Calculate Kc in mol/dm³.", 0.080, 0.002, "mol/dm³",
  "Kc = [PCl₃][Cl₂]/[PCl₅] = 0.040 × 0.040/0.020 = 0.080 mol/dm³.", "Products over reactants.", "Calculation")
N("Equilibrium constants Kc and Kp", "Question 5(c)", X5, "An equilibrium mixture [[N2O4(g) <=> 2NO2(g)]] at total pressure 100 kPa contains 30 mol% [[N2O4]] and 70 mol% [[NO2]]. Calculate Kp in kPa.", 163, 2, "kPa",
  "p(N₂O₄) = 30 kPa, p(NO₂) = 70 kPa. Kp = 70²/30 = 163 kPa.", "Partial pressure = mole fraction × total pressure.", "Calculation")
P("Le Chatelier's principle in industry", "Question 5(d)", X5, "In the Contact process, a pressure of only 1-2 atm is used in spite of the fact that high pressure favours [[SO3]], because", "the yield is already high at this pressure and high-pressure plant is very expensive",
  [("high pressure would reduce the rate", "Higher pressure increases the rate."), ("pressure has no effect on this equilibrium", "There are 3 mol of gas on the left and 2 on the right, so pressure does affect it."), ("the catalyst is poisoned by high pressure", "The vanadium(V) oxide catalyst is not poisoned by pressure.")],
  "The conversion is about 99% at 450 °C and 1-2 atm, so the extra cost of high pressure is not justified.", "Think about cost against gain in yield.", "Application")
N("Raoult's law and fractional distillation", "Question 5(e)", X5, "A and B form an ideal solution with x(A) = 0.25. Pure A has vapour pressure 60 kPa and pure B 20 kPa at the same temperature. What is the total vapour pressure in kPa?", 30, 0.5, "kPa",
  "p = 0.25 × 60 + 0.75 × 20 = 15 + 15 = 30 kPa.", "Raoult's law for each component, then add.", "Calculation")

X6 = "Organic chemistry."
P("Classification and IUPAC nomenclature", "Question 6(a)", X6, "What is the IUPAC name of [[(CH3)2CHCHBrCH3]]?", "2-bromo-3-methylbutane",
  [("3-bromo-2-methylbutane", "The bromine should receive the lower number: C2."), ("2-methyl-3-bromobutane", "The prefixes must be in alphabetical order: bromo before methyl."), ("2-bromo-3-ethylpropane", "The longest chain has four carbons and there is no ethyl group.")],
  "Four-carbon chain; numbering from the Br end gives {2,3}; alphabetical order: 2-bromo-3-methylbutane.", "Give the lowest number to the first-cited substituent in a tie.", "Application")
N("Structural isomerism and stereoisomerism", "Question 6(b)", X6, "How many structural isomers (not counting optical isomers) have the formula [[C4H9Br]]?", 4, 0, "",
  "1-Bromobutane, 2-bromobutane, 1-bromo-2-methylpropane and 2-bromo-2-methylpropane.", "Two carbon skeletons, each with the bromine in different positions.", "Application")
P("Reaction mechanisms", "Question 6(c)", X6, "Bromoethane reacts with aqueous sodium hydroxide by the SN2 mechanism. Which statement is correct?", "The rate depends on the concentrations of both bromoethane and hydroxide ions",
  [("The rate depends only on the concentration of bromoethane", "This describes SN1."), ("A carbocation intermediate is formed", "SN2 has no intermediate, only a transition state."), ("The reaction proceeds with retention of configuration at carbon", "SN2 gives inversion.")],
  "SN2 is one-step and bimolecular: rate = k[RBr][OH⁻].", "SN2 is bimolecular. What does that imply for the rate equation?", "Concept")
P("Alkanes and alkenes", "Question 6(d)", X6, "What is the major product when but-1-ene reacts with hydrogen bromide?", "2-bromobutane",
  [("1-bromobutane", "This comes from the less stable primary carbocation: the minor product."), ("1,2-dibromobutane", "This would need [[Br2]]."), ("butan-2-ol", "Water is not a reagent here.")],
  "H adds to C1 (more hydrogens) giving the secondary carbocation, then Br⁻ adds to C2.", "Apply Markovnikov's rule.", "Application")
P("Alkynes and haloalkanes", "Question 6(e)", X6, "Which observation shows that a hydrocarbon of formula [[C3H4]] is propyne rather than a different isomer?", "A white precipitate with ammoniacal silver nitrate",
  [("It decolourises bromine water", "All the unsaturated isomers do this."), ("It burns with a smoky flame", "This is true of all unsaturated hydrocarbons."), ("It is a gas at room temperature", "Other isomers are gases too.")],
  "Only the terminal alkyne, with its acidic C-H, gives the white silver ethynide precipitate.", "Which feature is unique to a terminal alkyne?", "Application")
P("Alcohols", "Question 6(f)", X6, "An alcohol of formula [[C4H10O]] is oxidised by acidified dichromate to a product that gives no silver mirror but forms a yellow precipitate with iodine and sodium hydroxide. The alcohol is", "butan-2-ol",
  [("butan-1-ol", "It would give an aldehyde, which gives a silver mirror."), ("2-methylpropan-1-ol", "It would give an aldehyde, which gives a silver mirror."), ("2-methylpropan-2-ol", "A tertiary alcohol is not oxidised.")],
  "No silver mirror: the product is a ketone. The iodoform test needs [[CH3CO-]]: butanone from butan-2-ol.", "No silver mirror rules out an aldehyde.", "Reasoning")

assert len(_P2) == 27, len(_P2)
SETS += [practice_set(module=M_EXAM, topic="Paper 2", title="Paper 2 practice paper A", lesson="chxl-paper-2-structured-questions",
                      mock=True, time_limit_minutes=150, questions=_P2)]

SETS = _walk(SETS)
