"""A Level Geography (0750), Upper Sixth: Practical Geography II: Statistical Techniques & Fieldwork, and the Examination module.

6 topic lessons (gpu3-) and 3 examination lessons, one practice set each (see the practice file of the same name), plus the
mock papers in the practice file. Content follows KKEVO's master curriculum blueprint (module line U6M6) and the Board's 2023
Advanced Level subject report for exam structure and common errors; it is not a Board syllabus booklet. All data sets are
invented for practice. Every statistic (standard deviation, coefficient of variation, quartiles, Lorenz cumulative
percentages, nearest neighbour index, Spearman, Pearson, chi-squared, proportional symbols, channel area, hydraulic radius,
discharge) was checked by script. Critical values were checked by script against the t, chi-squared and exact Spearman
distributions; they are given as approximate, and students are told to check their own tables.
"""

from .dsl import *  # noqa: F403

COURSE = ("geography", "upper-sixth")

M_STAT = "Practical Geography II: Statistical Techniques & Fieldwork"
M_EXAM = "Examination"

LESSONS = []

# ------------------------------------------------------------------ 1. Central tendency and dispersion
LESSONS.append(lesson(
    module=M_STAT,
    topic="Central tendency and dispersion",
    title="Central tendency and dispersion: from the mean to the coefficient of variation",
    slug="gpu3-central-tendency-dispersion",
    minutes=25,
    summary="How to summarise a geographical data set with the mean, median and mode, and how to measure its spread with the range, interquartile range, standard deviation and coefficient of variation.",
    objectives=[
        "Calculate and choose between the mean, median and mode for a geographical data set",
        "Find the range and the interquartile range and explain what each shows",
        "Calculate the standard deviation step by step and interpret it",
        "Use the coefficient of variation to compare the reliability of two data sets with different means",
    ],
    key_concepts=["Mean", "Median", "Mode", "Range", "Interquartile range", "Standard deviation", "Coefficient of variation", "Normal distribution"],
    blocks=[
        H("Introduction"),
        T("A farmer near Garoua and a farmer near Douala both ask the same question: how much rain can I count on next year? "
          "A single average does not answer it. The farmer also needs to know how much the rainfall changes from one year to another. "
          "Geographers summarise a data set with two kinds of number: a **measure of central tendency** (a typical value) and a **measure of dispersion** (how spread out the values are). "
          "This lesson goes beyond the averages you met at O Level: you will calculate the standard deviation and the coefficient of variation, the tools used in Paper 3 and in fieldwork reports."),
        H("Measures of central tendency"),
        KEY("Three averages", "Each has a use and a weakness.", cards=[
            ["Mean", "Add all the values and divide by the number of values. It uses every value, but one extreme value (an outlier) pulls it up or down."],
            ["Median", "The middle value when the data are in order; for n values it is the value in position (n + 1) ÷ 2. Extreme values do not affect it, so it suits skewed data such as incomes or farm sizes."],
            ["Mode", "The value (or class) that occurs most often. Useful for categories (the most common crop, the most common building use) but a set may have no mode or several."],
        ]),
        F(r"\bar{x} = \frac{\sum x}{n}", title="The mean"),
        H("Measures of dispersion"),
        D("The **range** is the highest value minus the lowest. The **interquartile range (IQR)** is the upper quartile minus the lower quartile: it gives the spread of the middle 50% of the values and is not affected by extreme values.", title="Range and interquartile range"),
        T("To find the quartiles, put the data in order. The lower quartile (LQ) is the value in position (n + 1) ÷ 4 and the upper quartile (UQ) is in position 3(n + 1) ÷ 4. "
          "Textbooks use slightly different methods for the quartiles when these positions are not whole numbers, so check the method in your textbook and show which one you used."),
        EX("Worked example 1: median and interquartile range", intro="The number of market stalls selling food crops was counted in 11 villages: 18, 25, 7, 31, 12, 22, 40, 15, 9, 27, 20. Find the median and the interquartile range.", steps=[
            S("Put the values in order", text="7, 9, 12, 15, 18, 20, 22, 25, 27, 31, 40 (n = 11)."),
            S("Median", math=r"\text{position} = \frac{11+1}{2} = 6 \Rightarrow \text{median} = 20"),
            S("Quartiles", math=r"\text{LQ: position } \frac{12}{4} = 3 \Rightarrow 12 \qquad \text{UQ: position } \frac{3 \times 12}{4} = 9 \Rightarrow 27"),
            S("Interquartile range", math=r"\text{IQR} = 27 - 12 = 15", text="The range is 40 − 7 = 33, but the IQR (15) is not affected by the extreme value 40."),
        ], check=r"\text{IQR} = 27 - 12 = 15"),
        H("The standard deviation"),
        D("The **standard deviation (SD, written σ)** measures the average distance of the values from the mean. A small SD means the values are close to the mean; a large SD means they are widely spread.", title="Definition: standard deviation",
          formula=r"\sigma = \sqrt{\frac{\sum (x - \bar{x})^2}{n}}"),
        T("Method: (1) find the mean; (2) subtract the mean from each value to get the deviation; (3) square each deviation, so negatives do not cancel positives; (4) add the squares; (5) divide by n; (6) take the square root. "
          "Some textbooks divide by n − 1 when the data are a sample; the answer is then a little larger. Use the formula your textbook and teacher use, and write it down before you substitute."),
        IMG("algpu3-normal-sd.svg", alt="A bell-shaped normal curve. The central band from one standard deviation below the mean to one above holds about 68% of values; the band from two below to two above holds about 95%.",
            caption="Figure 1. In a normal distribution about 68% of values lie within 1 SD of the mean and about 95% within 2 SD."),
        T("When the data are roughly normal (bell-shaped), the SD tells you more: about 68% of the values lie within one SD of the mean and about 95% within two. "
          "So if the mean annual rainfall at a station is 1 000 mm and the SD is 155 mm, about two years in three have between 845 mm and 1 155 mm."),
        CODE("Station A (coastal)          Station B (northern)\n"
             "x      x - mean  (x - mean)^2  x      x - mean  (x - mean)^2\n"
             "3700   -300      90000         900    -100      10000\n"
             "4100    100      10000         1150    150      22500\n"
             "3900   -100      10000         800    -200      40000\n"
             "4300    300      90000         1250    250      62500\n"
             "3800   -200      40000         1000      0          0\n"
             "4200    200      40000         900    -100      10000\n"
             "Sum 24000        280000        6000              145000", "text",
             title="Table 1. Annual rainfall (mm) for six years at two stations (invented for practice)"),
        EX("Worked example 2: standard deviation of station B", intro="Use Table 1. Calculate the standard deviation of the annual rainfall at station B.", steps=[
            S("Mean", math=r"\bar{x} = \frac{6000}{6} = 1000 \text{ mm}"),
            S("Deviations squared and added", math=r"\sum (x - \bar{x})^2 = 10000 + 22500 + 40000 + 62500 + 0 + 10000 = 145000"),
            S("Divide by n", math=r"\frac{145000}{6} = 24166.7"),
            S("Square root", math=r"\sigma = \sqrt{24166.7} = 155.5 \text{ mm}", text="Station A, by the same method, has σ = √(280 000 ÷ 6) = 216.0 mm."),
        ], check=r"\sqrt{145000/6} = 155.5"),
        H("The coefficient of variation"),
        D("The **coefficient of variation (CV)** is the standard deviation expressed as a percentage of the mean. It lets you compare the variability of data sets with very different means.", title="Coefficient of variation",
          formula=r"CV = \frac{\sigma}{\bar{x}} \times 100"),
        EX("Worked example 3: which station has the less reliable rainfall?", intro="Station A: mean 4 000 mm, SD 216.0 mm. Station B: mean 1 000 mm, SD 155.5 mm. Compare their reliability.", steps=[
            S("CV of station A", math=r"CV = \frac{216.0}{4000} \times 100 = 5.4\%"),
            S("CV of station B", math=r"CV = \frac{155.5}{1000} \times 100 = 15.5\%"),
            S("Interpret", text="Station A has the larger SD in millimetres, but relative to its mean its rainfall varies much less. Station B's rainfall is about three times as variable, so it is less reliable: a real risk for farmers in a drier region."),
        ], check=r"216.0/4000 = 0.054"),
        KEY("Evaluating the measures", "Choose the measure that suits the data.", cards=[
            ["Range", "Quick, but uses only two values, so one extreme value distorts it."],
            ["Interquartile range", "Ignores extreme values; pairs with the median for skewed data. It does not use every value."],
            ["Standard deviation", "Uses every value and links to the normal distribution, but takes longer and is affected by extreme values. Cannot compare sets with different means."],
            ["Coefficient of variation", "Removes the effect of the size of the mean, so it compares variability fairly, for example rainfall reliability between stations."],
        ]),
        MISTAKE("Comparing standard deviations of data with different means", "A larger SD does not always mean a more variable data set. If the means differ greatly, calculate the CV before you compare."),
        MISTAKE("Forgetting to square, or to take the square root", "Write the six steps as columns: x, x − mean, (x − mean)². The final answer must have the same unit as the data (mm, not mm²)."),
        MISTAKE("Figures and tables without titles", "The Board's 2023 report noted many statistics answers with untitled tables and unlabelled axes. Give every table a title and every value a unit."),
        QUIZ("A data set has a mean of 50 and a standard deviation of 10. A second set has a mean of 200 and a standard deviation of 30. Which statement is correct?",
             ["The second set is relatively less variable, because its CV is 15% compared with 20%", "The second set is more variable because its SD is larger", "Both sets are equally variable", "The variability cannot be compared"], 0,
             "CV = 10 ÷ 50 × 100 = 20% and 30 ÷ 200 × 100 = 15%. Relative to its mean, the second set varies less.", hint="Express each SD as a percentage of its mean.",
             feedback=["", "The SD alone ignores the size of the mean.", "The CVs are 20% and 15%, not equal.", "The CV makes the comparison possible."]),
        QUIZ("Which measure of dispersion is least affected by one very high value?", ["The range", "The standard deviation", "The interquartile range", "The mean"], 2,
             "The IQR uses only the middle half of the ordered data, so one extreme value does not change it.", hint="Which measure ignores the top and bottom quarters?",
             feedback=["The range uses the highest value directly.", "The SD uses every value, so an extreme value raises it.", "", "The mean is a measure of central tendency, not dispersion."]),
        TIP("Dispersion appears in Paper 1 (a quick calculation or a definition) and in Paper 3, where the 2023 statistics question used the interquartile range. In fieldwork answers, name the technique, show the formula and working in a table, and say what the result means.", title="Exam link"),
        PQ("The daily number of vehicles crossing a ferry was recorded on 5 days: 12, 15, 9, 14, 10. Calculate the mean and the standard deviation.",
           "Mean = 60 ÷ 5 = 12. Deviations: 0, 3, −3, 2, −2. Squares: 0, 9, 9, 4, 4; sum = 26. σ = √(26 ÷ 5) = √5.2 = 2.28 vehicles (to 2 d.p.). (Using n − 1: √(26 ÷ 4) = 2.55.)"),
        PQ("Explain why the median and interquartile range may be better than the mean and standard deviation for describing farm sizes in a district where a few plantations are very large.",
           "Farm sizes are strongly skewed: most farms are small but a few plantations are huge. The plantations pull the mean far above the size of a typical farm and inflate the standard deviation. The median is the middle farm size, so it describes a typical farm; the interquartile range measures the spread of the middle half and ignores the extreme plantation values."),
        PQ("Two rain gauges record a mean annual rainfall of 1 600 mm (SD 240 mm) and 2 800 mm (SD 280 mm). Which has the more reliable rainfall? Show your working.",
           "CV of the first = 240 ÷ 1 600 × 100 = 15%. CV of the second = 280 ÷ 2 800 × 100 = 10%. The second station has the lower coefficient of variation, so its rainfall is more reliable, although its standard deviation is larger."),
        SUM("Central tendency: mean (uses all values), median (resists extremes), mode (most frequent; for categories).",
            "Range = highest − lowest; IQR = UQ − LQ, the spread of the middle 50%.",
            "Standard deviation σ = √(Σ(x − mean)² ÷ n): about 68% of normal data lie within 1 SD of the mean.",
            "Coefficient of variation = SD ÷ mean × 100: use it to compare variability when the means differ.",
            "Show the formula, a working table, units and an interpretation of every result."),
    ],
))

# ------------------------------------------------------------------ 2. Lorenz curves and the nearest neighbour index
LESSONS.append(lesson(
    module=M_STAT,
    topic="Lorenz curves and the nearest neighbour index",
    title="Measuring unevenness and pattern: Lorenz curves and the nearest neighbour index",
    slug="gpu3-lorenz-nearest-neighbour",
    minutes=25,
    summary="How to draw and read a Lorenz curve to show how evenly something is shared out, and how to calculate and interpret the nearest neighbour index of a point pattern such as settlements.",
    objectives=[
        "Prepare cumulative percentages and draw a Lorenz curve with a line of equality",
        "Interpret the shape of a Lorenz curve and use it to compare distributions",
        "Calculate the nearest neighbour index Rn and classify a pattern as clustered, random or regular",
        "Explain the limitations of both techniques",
    ],
    key_concepts=["Lorenz curve", "Line of equality", "Cumulative percentage", "Concentration", "Nearest neighbour index", "Clustered pattern", "Random pattern", "Regular pattern"],
    blocks=[
        H("Introduction"),
        T("Two questions come up again and again in human geography. **How evenly is something shared out?** For example, is a region's population spread across all its divisions, or crowded into a few? "
          "And **what is the pattern of points on a map?** Are the villages on a topographic map bunched together, scattered at random, or evenly spaced? "
          "The Lorenz curve answers the first question; the nearest neighbour index answers the second."),
        H("The Lorenz curve"),
        D("A **Lorenz curve** is a graph of cumulative percentages that shows how evenly a quantity (population, income, land, employment) is shared among areas or groups. "
          "The straight diagonal is the **line of equality**: every 10% of the area would hold 10% of the quantity. The further the curve bends away from the diagonal, the more uneven (concentrated) the distribution.", title="Definition: Lorenz curve"),
        T("Method: (1) for each unit, work out its percentage share of the area and of the quantity; (2) rank the units, usually from the one with the highest ratio of quantity to area (the densest) to the lowest; "
          "(3) add up the percentages in that order to get cumulative percentages; (4) plot cumulative % of area (x) against cumulative % of quantity (y), starting at (0, 0) and ending at (100, 100); (5) draw the line of equality. "
          "Some textbooks rank from the lowest ratio instead, so the curve bends below the line; the distance from the line still shows the unevenness. Check the convention in your textbook."),
        CODE("District  % of area  % of pop.  pop. ÷ area  Rank  Cum. % area  Cum. % pop.\n"
             "P            10         35         3.50       1       10          35\n"
             "Q            20         30         1.50       2       30          65\n"
             "R            15         15         1.00       3       45          80\n"
             "S            25         12         0.48       4       70          92\n"
             "T            30          8         0.27       5      100         100", "text",
             title="Table 1. Population of five districts of a region (invented for practice)"),
        EX("Worked example 1: preparing a Lorenz curve", intro="Use Table 1. Rank the districts and find the cumulative percentages to plot.", steps=[
            S("Ratio of population share to area share", text="P: 35 ÷ 10 = 3.50; Q: 30 ÷ 20 = 1.50; R: 15 ÷ 15 = 1.00; S: 12 ÷ 25 = 0.48; T: 8 ÷ 30 = 0.27."),
            S("Rank from the highest ratio", text="P, Q, R, S, T."),
            S("Cumulate in that order", text="Area: 10, 30, 45, 70, 100. Population: 35, 65, 80, 92, 100."),
            S("Plot and read", text="The points (10, 35), (30, 65), (45, 80), (70, 92) and (100, 100) lie well above the diagonal: 45% of the area holds 80% of the people, so the population is concentrated."),
        ]),
        IMG("algpu3-lorenz.svg", alt="Lorenz curve rising steeply from the origin through points P (10, 35), Q (30, 65), R (45, 80), S (70, 92) to T (100, 100), well above the dashed diagonal line of equality; the gap between them is shaded.",
            caption="Figure 1. The Lorenz curve for Table 1. The shaded gap between the curve and the line of equality shows the degree of unevenness."),
        T("To compare two regions (or one region in two years), draw both curves on the same axes: the curve further from the diagonal shows the more uneven distribution. "
          "Some courses also measure the gap with a single number, the **Gini coefficient** (0 = perfect equality, 1 = everything in one unit); check whether your syllabus asks for it."),
        KEY("Uses and limitations of the Lorenz curve", "A good descriptive tool.", cards=[
            ["Uses", "Population and settlement concentration, land ownership, income inequality between regions, industrial employment, the concentration of rainfall in a few months of the year."],
            ["Limitations", "It shows how uneven a distribution is but not WHERE the concentration is; the result depends on the size and number of units chosen; it does not explain the causes."],
        ]),
        H("The nearest neighbour index"),
        D("The **nearest neighbour index (Rn)** compares the average distance between each point and its nearest neighbour with the average distance expected if the same number of points were scattered at random over the same area.", title="Definition: nearest neighbour index",
          formula=r"R_n = 2\bar{d}\sqrt{\frac{n}{A}}"),
        T("Here d̄ is the mean observed distance between each point and its nearest neighbour, n is the number of points and A is the area of the study region, in the same units (for example km and km²). "
          "Rn runs from 0 to 2.15: a value near **0** is a **clustered** pattern (all points close together), about **1.0** is **random**, and the maximum **2.15** is a perfectly **regular** (evenly spaced, triangular) pattern."),
        IMG("algpu3-nni-patterns.svg", alt="Three square panels: a clustered pattern with two tight groups of points (Rn near 0), a random scatter (Rn about 1.0) and an evenly spaced grid (Rn up to 2.15), above a scale from 0 to 2.15.",
            caption="Figure 2. The three kinds of point pattern and their position on the Rn scale."),
        EX("Worked example 2: villages on a topographic map", intro="A study area of 40 km² contains 12 villages. The mean distance from each village to its nearest neighbour is 1.1 km. Calculate and interpret Rn.", steps=[
            S("Density term", math=r"\sqrt{\frac{n}{A}} = \sqrt{\frac{12}{40}} = \sqrt{0.3} = 0.548"),
            S("Substitute", math=r"R_n = 2 \times 1.1 \times 0.548 = 1.20"),
            S("Interpret", text="1.20 is a little above 1.0: the pattern is close to random, with a slight tendency towards regular spacing. This may reflect an even spread of farmland and water, with villages keeping some distance from one another."),
        ], check=r"2 \times 1.1 \times \sqrt{0.3} = 1.205"),
        EX("Worked example 3: from measured distances", intro="In an area of 20 km², ten settlements have nearest-neighbour distances of 0.8, 1.2, 0.6, 1.0, 1.4, 0.9, 1.1, 0.7, 1.3 and 1.0 km. Calculate Rn.", steps=[
            S("Mean distance", math=r"\bar{d} = \frac{10.0}{10} = 1.0 \text{ km}"),
            S("Substitute", math=r"R_n = 2 \times 1.0 \times \sqrt{\frac{10}{20}} = 2 \times 0.707 = 1.41"),
            S("Interpret", text="1.41 lies between random (1.0) and regular (2.15), so the settlements tend towards a regular pattern, as central place theory would predict where market centres compete for customers."),
        ], check=r"2 \times \sqrt{0.5} = 1.414"),
        KEY("Explaining the pattern", "Always link the value to geography.", cards=[
            ["Clustered (Rn below about 0.5)", "Points share a resource: springs or a river, fertile valley soils, a road junction, mining sites, or a defensive hill site."],
            ["Random (about 1.0)", "No single factor dominates; the land is fairly uniform in soil, relief and water."],
            ["Regular (above about 1.5)", "Competition for space or customers (market centres), or planned layouts such as resettlement schemes."],
        ]),
        T("Limitations: the result depends on the boundary of the study area (adding empty land increases A and lowers Rn); points near the edge may have their true nearest neighbour outside the area; a village must be reduced to a single point; straight-line distances ignore relief and rivers. "
          "A value close to 1 may also arise by chance: textbooks give tables of significance for Rn according to n, so check your tables before claiming a pattern is truly clustered or regular."),
        MISTAKE("Mixing units", "If d̄ is in km, A must be in km². Using metres for distance and km² for area gives a nonsense value (for example Rn = 1 200)."),
        MISTAKE("Giving the value without the meaning", "In the Board's 2023 report, candidates who calculated a map value correctly (sinuosity) often lost credit by not interpreting it. After every Rn, say clustered, random or regular, and suggest why."),
        QUIZ("Twenty water points lie in an area of 50 km². The mean nearest-neighbour distance is 0.3 km. What is Rn and what pattern does it show?",
             ["0.38, clustered", "0.38, regular", "0.95, random", "0.19, random"], 0,
             "Rn = 2 × 0.3 × √(20 ÷ 50) = 0.6 × 0.632 = 0.38, close to 0, so the points are clustered.", hint="Work out √(n ÷ A) first.",
             feedback=["", "Values near 0 show clustering, not regularity.", "This uses √(A ÷ n) instead of √(n ÷ A); the fraction is upside down.", "This forgets the factor 2, and 0.19 would still be clustered, not random."]),
        QUIZ("On a Lorenz curve, the curve for region X lies much closer to the line of equality than the curve for region Y. What does this show?",
             ["The population of X is spread more evenly than that of Y", "X has a larger population than Y", "X has a more concentrated population than Y", "X is smaller in area than Y"], 0,
             "The closer the curve is to the diagonal, the more even the distribution.", hint="What does the diagonal line represent?",
             feedback=["", "Lorenz curves use percentages, so they do not show total size.", "This is the reverse: concentration bends the curve away from the line.", "Area is converted to percentages, so size is not shown."]),
        TIP("The nearest neighbour index links Paper 3 statistics with map work: you may be asked to measure distances between settlements on a map and calculate Rn. The Lorenz curve suits data-response questions on population and development. Show the table of cumulative values and label both axes.", title="Exam link"),
        PQ("Explain how you would use a topographic map to test whether the settlements in a grid square area are clustered.",
           "Define the study area and calculate its area in km². Mark each settlement as one point (its centre). For each point, measure the straight-line distance to its nearest neighbour and convert to km using the scale. Find the mean distance d̄ and count n. Calculate Rn = 2d̄√(n ÷ A). A value close to 0 shows clustering, about 1 random and up to 2.15 regular. Check the significance in a table and explain the pattern with map evidence, such as springs or a valley floor."),
        PQ("Nine market centres lie in an area of 16 km², with a mean nearest-neighbour distance of 1.2 km. Calculate Rn and interpret it.",
           "√(9 ÷ 16) = 0.75. Rn = 2 × 1.2 × 0.75 = 1.80. This is well above 1.0 and approaches the maximum of 2.15, so the market centres are fairly regularly spaced, as central place theory predicts where centres compete for customers and each serves its own surrounding area."),
        PQ("Describe two limitations of the Lorenz curve as a tool for studying population distribution.",
           "First, it shows the degree of unevenness but not where the people are concentrated: two very different maps can give the same curve. Second, the result depends on the number and size of the units: using fewer, larger divisions hides concentration inside them. It also only describes the distribution and does not explain its causes."),
        SUM("A Lorenz curve plots cumulative % of area against cumulative % of a quantity, ranked by density; the line of equality is the diagonal.",
            "The further the curve bends from the diagonal, the more concentrated the distribution.",
            "Rn = 2d̄√(n ÷ A): about 0 clustered, about 1.0 random, up to 2.15 regular.",
            "Use consistent units, interpret every value and check significance in your tables.",
            "Both techniques describe a pattern but do not explain it: link the result to physical and human factors."),
    ],
))

# ------------------------------------------------------------------ 3. Correlation: Spearman and Pearson
LESSONS.append(lesson(
    module=M_STAT,
    topic="Correlation: Spearman and Pearson",
    title="Correlation: Spearman's rank and Pearson's product-moment coefficients",
    slug="gpu3-spearman-pearson-correlation",
    minutes=25,
    summary="How to test whether two geographical variables are related: scatter graphs, Spearman's rank correlation with tied ranks, Pearson's product-moment correlation, hypotheses and significance testing.",
    objectives=[
        "Describe the strength and direction of a relationship from a scatter graph",
        "Calculate Spearman's rank correlation coefficient, including tied ranks",
        "Calculate Pearson's product-moment correlation coefficient from summary values",
        "Test the significance of a coefficient against critical values and draw a valid conclusion",
    ],
    key_concepts=["Correlation", "Scatter graph", "Spearman's rank correlation", "Tied ranks", "Pearson's product-moment correlation", "Null hypothesis", "Significance level", "Critical value"],
    blocks=[
        H("Introduction"),
        T("Do larger settlements offer more services? Does maize yield rise with rainfall? Does temperature fall as we climb Mount Cameroon? "
          "Each question links two variables. **Correlation** measures how closely two variables are related. "
          "A correlation coefficient runs from **+1** (perfect positive: both rise together) through **0** (no relationship) to **−1** (perfect negative: one rises as the other falls)."),
        H("Start with a scatter graph"),
        T("Plot the independent variable (the one you think is the cause) on the x-axis and the dependent variable on the y-axis. Look at the direction (positive or negative), the strength (how close the points lie to a line) and any **anomalies** (points far from the trend), which need explaining."),
        IMG("algpu3-scatter-services.svg", alt="Scatter graph of ten settlements, population in thousands on the x-axis from 0 to 60 and number of services on the y-axis from 0 to 50; the points rise from lower left to upper right close to a dashed trend line.",
            caption="Figure 1. A strong positive relationship between population and the number of services (Table 1)."),
        H("Spearman's rank correlation coefficient"),
        D("**Spearman's rank correlation coefficient (rs)** measures the strength of a relationship between two sets of ranks. It suits ordinal data and relationships that are not straight lines.", title="Spearman's rank correlation",
          formula=r"r_s = 1 - \frac{6\sum d^2}{n^3 - n}"),
        T("Method: (1) rank each variable separately (largest = 1, or smallest = 1, but the same way for both); (2) find d, the difference between the two ranks of each place; (3) square and add to get Σd²; (4) substitute. "
          "**Tied ranks**: if two values are equal, give each the average of the ranks they would occupy. Two values sharing 5th and 6th place both get 5.5, and the next value is 7th."),
        CODE("Settlement  Pop. (000)  Rank  Services  Rank   d    d^2\n"
             "A               42        2       38       2     0     0\n"
             "B               18        6       20       6     0     0\n"
             "C               25        4       22       5    -1     1\n"
             "D                9        9       10      10    -1     1\n"
             "E               31        3       26       3     0     0\n"
             "F               12        8       14       7     1     1\n"
             "G               55        1       45       1     0     0\n"
             "H                7       10       11       9     1     1\n"
             "I               20        5       24       4     1     1\n"
             "J               15        7       12       8    -1     1\n"
             "                                                Sum d^2 = 6", "text",
             title="Table 1. Population and number of services in ten settlements (invented for practice)"),
        EX("Worked example 1: Spearman for Table 1", intro="Calculate rs for the data in Table 1.", steps=[
            S("Substitute n = 10 and Σd² = 6", math=r"r_s = 1 - \frac{6 \times 6}{10^3 - 10} = 1 - \frac{36}{990}"),
            S("Calculate", math=r"r_s = 1 - 0.036 = +0.96"),
            S("Describe", text="A very strong positive correlation: larger settlements have more services, as central place theory predicts (higher thresholds are reached in larger places)."),
        ], check=r"1 - 36/990 = 0.9636"),
        H("Is the result significant?"),
        T("A strong-looking coefficient from a small sample could arise by chance. We therefore test it: "
          "(1) state the **null hypothesis H0**: there is no significant correlation between the two variables; and the **alternative hypothesis H1**: there is a significant correlation; "
          "(2) choose a **significance level**, usually 0.05 (95% confidence) or the stricter 0.01 (99%); "
          "(3) look up the **critical value** for your sample size in the table; (4) if the size of your coefficient (ignoring the sign) is greater than the critical value, reject H0."),
        CODE("Approximate two-tailed critical values (check your own tables)\n"
             "                     0.05 level   0.01 level\n"
             "Spearman, n = 8         0.74         0.88\n"
             "Spearman, n = 10        0.65         0.79\n"
             "Pearson,  n = 5         0.88         0.96\n"
             "Pearson,  n = 8         0.71         0.83\n"
             "Pearson,  n = 10        0.63         0.77", "text",
             title="Table 2. Critical values used in this lesson"),
        T("Tables differ: some are one-tailed (lower values, used when H1 states the direction), some list Spearman values by n and others by degrees of freedom (n − 2). Use the table your teacher gives you and state which level you used. "
          "For Table 1, rs = 0.96 with n = 10 is above 0.79, so we reject H0 at the 0.01 level: the correlation is very unlikely to be due to chance."),
        EX("Worked example 2: tied ranks", intro="Eight farms record growing-season rainfall (cm): 120, 95, 150, 80, 110, 95, 60, 130, and maize yields (bags per hectare): 30, 22, 34, 18, 25, 26, 15, 28. Calculate rs and test it.", steps=[
            S("Rank rainfall (largest = 1)", text="150 → 1, 130 → 2, 120 → 3, 110 → 4, the two 95s share 5th and 6th so each gets 5.5, 80 → 7, 60 → 8."),
            S("Rank yield and find d²", text="Yield ranks in farm order: 2, 6, 1, 7, 5, 4, 8, 3. Rainfall ranks: 3, 5.5, 1, 7, 4, 5.5, 8, 2. d² = 1, 0.25, 0, 0, 1, 2.25, 0, 1; Σd² = 5.5."),
            S("Substitute", math=r"r_s = 1 - \frac{6 \times 5.5}{8^3 - 8} = 1 - \frac{33}{504} = +0.93"),
            S("Test", text="For n = 8 the critical values are about 0.74 (0.05) and 0.88 (0.01). 0.93 > 0.88, so reject H0 at the 0.01 level: yield is significantly related to rainfall on these farms."),
        ], check=r"1 - 33/504 = 0.9345"),
        H("Pearson's product-moment correlation coefficient"),
        D("**Pearson's product-moment correlation coefficient (r)** uses the actual values, not ranks. It measures how close the points lie to a straight line, and is used for interval or ratio data with a linear relationship.", title="Pearson's r",
          formula=r"r = \frac{\sum (x - \bar{x})(y - \bar{y})}{\sqrt{\sum (x - \bar{x})^2 \sum (y - \bar{y})^2}}"),
        EX("Worked example 3: Pearson's r", intro="Five farms have sizes x (ha) of 2, 4, 6, 8, 10 and employ y workers: 3, 5, 4, 8, 10. Calculate r and test it.", steps=[
            S("Means", math=r"\bar{x} = 6, \quad \bar{y} = 6"),
            S("Deviations", text="x − mean: −4, −2, 0, 2, 4. y − mean: −3, −1, −2, 2, 4."),
            S("Sums", math=r"\sum (x-\bar{x})(y-\bar{y}) = 12 + 2 + 0 + 4 + 16 = 34, \quad \sum (x-\bar{x})^2 = 40, \quad \sum (y-\bar{y})^2 = 34"),
            S("Substitute", math=r"r = \frac{34}{\sqrt{40 \times 34}} = \frac{34}{36.88} = +0.92"),
            S("Test", text="With n = 5 (3 degrees of freedom) the critical values are about 0.88 (0.05) and 0.96 (0.01). 0.92 is significant at 0.05 but not at 0.01. With only five farms the evidence is weak: collect more data."),
        ], check=r"34/\sqrt{1360} = 0.922"),
        KEY("Spearman or Pearson?", "Choose by the data and the shape of the relationship.", cards=[
            ["Spearman (rs)", "Ranked or ordinal data; relationships that rise or fall steadily but not in a straight line; resists the effect of one extreme value. Easier by hand. Loses some information by using ranks."],
            ["Pearson (r)", "Interval or ratio data (measurements); a straight-line relationship; uses the full values so it is more powerful. Affected by outliers and needs data that are roughly normal."],
        ]),
        MISTAKE("Saying that correlation proves cause", "A significant correlation shows that two variables vary together, not that one causes the other. A third factor may cause both. Explain the link with geographical reasoning, not with the coefficient alone."),
        MISTAKE("Ranking the two variables in opposite directions", "If you rank one variable from largest = 1 and the other from smallest = 1, the sign of rs is reversed. Use the same rule for both columns."),
        MISTAKE("Ignoring the sample size", "With fewer than about 8 to 10 pairs, even a high coefficient may not be significant. Always test against the critical value for your n."),
        QUIZ("For ten pairs, Σd² = 322. What is Spearman's rs?", ["+0.95", "−0.95", "−0.93", "+0.68"], 1,
             "rs = 1 − (6 × 322) ÷ 990 = 1 − 1.95 = −0.95, a very strong negative correlation.", hint="Calculate 6Σd² ÷ (n³ − n) and subtract it from 1.",
             feedback=["The fraction is larger than 1, so the result is negative.", "", "This divides by n³ = 1 000 instead of n³ − n = 990.", "This forgets to multiply Σd² by 6: 1 − 322 ÷ 990 = 0.68."]),
        QUIZ("A student finds rs = 0.60 for 10 pairs and the critical value at the 0.05 level is about 0.65. What should she conclude?",
             ["Accept H1: the correlation is significant", "The correlation is perfect", "Reject H0 at the 0.01 level", "Do not reject H0: the correlation could be due to chance"], 3,
             "0.60 is less than the critical value 0.65, so the correlation is not significant at the 0.05 level.", hint="Compare the coefficient with the critical value.",
             feedback=["The coefficient is below the critical value, so H1 cannot be accepted.", "A perfect correlation is 1.0.", "It is not even significant at the 0.05 level.", ""]),
        TIP("Correlation is a classic Paper 3 statistics and fieldwork technique: state H0, show the ranking table, calculate, compare with the critical value and explain the relationship in geographical terms. Paper 1 may test the meaning of a coefficient or of significance.", title="Exam link"),
        PQ("Ten points along a street have distance from the city centre (km) 0.5 to 5.0 in steps of 0.5, and land values (index) 95, 70, 82, 60, 48, 52, 30, 45, 20, 25. With distance ranked largest = 1 and land value ranked largest = 1, Σd² = 322. Calculate rs, test it and explain the result.",
           "rs = 1 − (6 × 322) ÷ (1 000 − 10) = 1 − 1 932 ÷ 990 = −0.95. For n = 10 the critical value at the 0.01 level is about 0.79; 0.95 > 0.79 so reject H0: there is a significant negative correlation. Land values fall with distance from the centre because accessibility is greatest at the centre, where competition for land (bid rent) is highest."),
        PQ("Eight weather stations on a mountain give Σ(x − x̄)(y − ȳ) = −27 290, Σ(x − x̄)² = 4 822 150 (altitude, m) and Σ(y − ȳ)² = 155 (temperature, °C). Calculate Pearson's r and interpret it.",
           "r = −27 290 ÷ √(4 822 150 × 155) = −27 290 ÷ 27 339 = −0.998. With n = 8 the critical value at 0.01 is about 0.83, so the correlation is significant: temperature falls almost perfectly in a straight line as altitude rises, as expected from the environmental lapse rate."),
        PQ("Give two reasons why a geographer might choose Spearman's rank rather than Pearson's coefficient.",
           "Spearman works with ranks, so it can be used when the data are ordinal (for example environmental quality scores) or when the relationship is not a straight line but rises or falls steadily. It is also less affected by one extreme value and is quicker to calculate by hand in the field."),
        SUM("Correlation runs from −1 (perfect negative) through 0 to +1 (perfect positive); start with a scatter graph.",
            "Spearman: rs = 1 − 6Σd² ÷ (n³ − n); rank both variables the same way and average tied ranks.",
            "Pearson: r = Σ(x − x̄)(y − ȳ) ÷ √(Σ(x − x̄)² Σ(y − ȳ)²) for measured data with a linear trend.",
            "Test: state H0 and H1, choose 0.05 or 0.01, compare with the critical value for your n (check your tables).",
            "Correlation does not prove cause: explain the link geographically and comment on anomalies."),
    ],
))

# ------------------------------------------------------------------ 4. The chi-squared test
LESSONS.append(lesson(
    module=M_STAT,
    topic="The chi-squared test",
    title="The chi-squared test: comparing observed and expected frequencies",
    slug="gpu3-chi-squared-test",
    minutes=24,
    summary="How to use the chi-squared test to decide whether an observed distribution of counts differs significantly from what is expected, in one-row (goodness-of-fit) and two-way (contingency) tables.",
    objectives=[
        "State null and alternative hypotheses for a chi-squared test",
        "Calculate expected frequencies for a one-row test and for a contingency table",
        "Calculate χ², find the degrees of freedom and compare with critical values",
        "State the conditions and limitations of the test",
    ],
    key_concepts=["Chi-squared test", "Observed frequency", "Expected frequency", "Goodness of fit", "Contingency table", "Degrees of freedom", "Critical value", "Null hypothesis"],
    blocks=[
        H("Introduction"),
        T("In a district of the Western Highlands, a student notices that many villages seem to lie on volcanic rocks rather than on granite. Is this a real preference, or could the pattern arise by chance? "
          "The **chi-squared (χ²) test** answers questions like this. It compares the numbers we **observe** in each category with the numbers we would **expect** if there were no real difference."),
        D("The **chi-squared test** measures the difference between observed (O) and expected (E) frequencies in categories. The larger χ², the less likely the difference is to be due to chance.", title="Definition: chi-squared",
          formula=r"\chi^2 = \sum \frac{(O - E)^2}{E}"),
        KEY("Two forms of the test", "The method is the same; the expected values differ.", cards=[
            ["Goodness of fit (one row)", "Compares a set of counts with an expected distribution: an even spread, or a spread in proportion to area. Degrees of freedom = number of categories − 1."],
            ["Contingency table (two-way)", "Tests whether two classifications are linked, such as distance from a road and whether households sell crops. E = row total × column total ÷ grand total. Degrees of freedom = (rows − 1)(columns − 1)."],
        ]),
        H("The steps"),
        T("(1) State **H0**: there is no significant difference between the observed and expected frequencies (or: no association between the two variables). State **H1**: there is a significant difference. "
          "(2) Calculate the expected frequencies. (3) For each category calculate (O − E)² ÷ E, then add them up. (4) Find the degrees of freedom. "
          "(5) Compare χ² with the critical value at the 0.05 and 0.01 levels: if χ² is **greater** than the critical value, reject H0."),
        CODE("Degrees of     Critical value   Critical value\n"
             "freedom        0.05 level       0.01 level\n"
             "1              3.84             6.63\n"
             "2              5.99             9.21\n"
             "3              7.81             11.34\n"
             "4              9.49             13.28\n"
             "5              11.07            15.09", "text",
             title="Table 1. Critical values of chi-squared (standard values; check your own tables)"),
        CODE("Rock type       % of area   Observed (O)   Expected (E)   (O - E)^2 / E\n"
             "Volcanic           40           30             24            1.50\n"
             "Granite            30           12             18            2.00\n"
             "Sandstone          20           10             12            0.33\n"
             "Alluvium           10            8              6            0.67\n"
             "Total             100           60             60            4.50", "text",
             title="Table 2. Villages on four rock types (invented for practice)"),
        EX("Worked example 1: goodness of fit in proportion to area", intro="Sixty villages lie on four rock types as shown in Table 2. Test whether the villages are distributed in proportion to the area of each rock type.", steps=[
            S("Hypotheses", text="H0: there is no significant difference between the observed distribution and one in proportion to area. H1: there is a significant difference."),
            S("Expected values", math=r"E = 60 \times 0.40 = 24, \quad 60 \times 0.30 = 18, \quad 60 \times 0.20 = 12, \quad 60 \times 0.10 = 6"),
            S("Calculate", math=r"\chi^2 = \frac{6^2}{24} + \frac{(-6)^2}{18} + \frac{(-2)^2}{12} + \frac{2^2}{6} = 1.50 + 2.00 + 0.33 + 0.67 = 4.50"),
            S("Degrees of freedom and decision", text="df = 4 − 1 = 3; critical value at 0.05 is 7.81. 4.50 < 7.81, so H0 is not rejected: the apparent preference for volcanic rock could be due to chance. The student would need a larger sample, or other evidence, before claiming a real preference."),
        ], check=r"1.5 + 2 + 0.333 + 0.667 = 4.5"),
        CODE("                    Sell surplus   Do not sell   Row total\n"
             "Near a tarred road      30 (22.5)     10 (17.5)        40\n"
             "Far from a road         15 (22.5)     25 (17.5)        40\n"
             "Column total            45            35               80", "text",
             title="Table 3. Farm households and crop sales; expected values in brackets (invented for practice)"),
        EX("Worked example 2: a contingency table", intro="A survey of 80 farm households records whether each lives near a tarred road and whether it sells surplus crops (Table 3). Is selling associated with road access?", steps=[
            S("Hypotheses", text="H0: there is no association between road access and selling surplus crops. H1: there is an association."),
            S("Expected values", math=r"E = \frac{\text{row total} \times \text{column total}}{\text{grand total}} = \frac{40 \times 45}{80} = 22.5 \text{ and } \frac{40 \times 35}{80} = 17.5"),
            S("Calculate", math=r"\chi^2 = \frac{7.5^2}{22.5} + \frac{7.5^2}{17.5} + \frac{7.5^2}{22.5} + \frac{7.5^2}{17.5} = 2.50 + 3.21 + 2.50 + 3.21 = 11.43"),
            S("Decision", text="df = (2 − 1)(2 − 1) = 1. 11.43 is greater than 6.63, so reject H0 at the 0.01 level: households near tarred roads are significantly more likely to sell their surplus, as lower transport costs make the market accessible."),
        ], check=r"2 \times 56.25/22.5 + 2 \times 56.25/17.5 = 11.43"),
        T("For a 2 × 2 table with one degree of freedom, some textbooks apply **Yates' correction** (subtract 0.5 from each |O − E| before squaring). Here it gives 9.96, which is still significant. Check whether your textbook uses it."),
        KEY("Conditions and limitations", "The test is only valid if these hold.", cards=[
            ["Counts only", "Use actual frequencies (numbers of villages, shops, people), never percentages, means or measurements."],
            ["Expected values", "Each expected value should be at least 5. If not, combine neighbouring categories (this reduces the degrees of freedom)."],
            ["Independent data", "Each item is counted once, in one category only."],
            ["What it shows", "It shows whether a difference is significant, not why it exists or how strong a link is. Explain the result with geographical reasoning."],
        ]),
        MISTAKE("Using percentages instead of counts", "Converting the observed values to percentages changes χ² and makes the result invalid. Work with the raw numbers."),
        MISTAKE("Getting the decision the wrong way round", "A LARGE χ² (above the critical value) means a significant difference: reject H0. A small χ² means the difference could be due to chance."),
        QUIZ("Shops on 5 streets are counted to test whether they are spread evenly. What are the degrees of freedom?", ["5", "4", "1", "10"], 1,
             "For a one-row test, df = number of categories − 1 = 5 − 1 = 4.", hint="One row of categories: subtract one.",
             feedback=["df is one less than the number of categories.", "", "df = 1 belongs to a 2 × 2 table or a 2-category row.", "This doubles the number of streets, which has no meaning here."]),
        QUIZ("In a contingency table, the row total is 60, the column total is 50 and the grand total is 200. What is the expected frequency for that cell?", ["3 000", "110", "15", "30"], 2,
             "E = 60 × 50 ÷ 200 = 3 000 ÷ 200 = 15.", hint="Row total × column total ÷ grand total.",
             feedback=["This multiplies the totals but forgets to divide by the grand total.", "This adds the two totals.", "", "This is 60 ÷ 2, not the formula."]),
        TIP("Chi-squared is a Paper 3 statistics technique and suits fieldwork with categories (land use types, shop functions, rock types). Lay out O, E and (O − E)² ÷ E in a table, state the degrees of freedom and the critical value, and finish with a geographical explanation.", title="Exam link"),
        PQ("Eighty shops are counted on five streets of a town centre: 18, 12, 25, 15 and 10. Test whether the shops are evenly spread.",
           "H0: there is no significant difference from an even spread. E = 80 ÷ 5 = 16 for each street. (O − E)² ÷ E: 4 ÷ 16 = 0.25, 16 ÷ 16 = 1.00, 81 ÷ 16 = 5.06, 1 ÷ 16 = 0.06, 36 ÷ 16 = 2.25; χ² = 8.63 (8.625). df = 4; critical value at 0.05 = 9.49. 8.63 < 9.49, so H0 is not rejected: the uneven spread could be due to chance, although the street with 25 shops (perhaps the most accessible) deserves further study."),
        PQ("Explain why the chi-squared test cannot be used directly on the mean rainfall of five stations.",
           "Chi-squared works only with frequencies (counts of items in categories). Mean rainfall is a measurement, not a count, so (O − E)² ÷ E would have no meaning and its size would change with the units used. A test for measured data, such as correlation or a comparison of means, should be used instead."),
        PQ("In a 3 × 4 contingency table, how many degrees of freedom are there, and what is the critical value at the 0.05 level from standard tables?",
           "df = (3 − 1)(4 − 1) = 2 × 3 = 6. The 0.05 critical value for 6 degrees of freedom is 12.59 in standard tables (check your own table)."),
        SUM("χ² = Σ(O − E)² ÷ E compares observed and expected counts.",
            "One-row test: E from an even spread or from proportions (such as area); df = categories − 1.",
            "Contingency table: E = row total × column total ÷ grand total; df = (rows − 1)(columns − 1).",
            "If χ² exceeds the critical value (for example 3.84 at df 1, 0.05), reject H0.",
            "Use counts only, keep each E at least 5, and explain the result geographically."),
    ],
))

# ------------------------------------------------------------------ 5. Statistical maps and diagrams
LESSONS.append(lesson(
    module=M_STAT,
    topic="Statistical maps and diagrams",
    title="Statistical maps and diagrams: choropleths, isolines, flow lines and climographs",
    slug="gpu3-statistical-maps-diagrams",
    minutes=25,
    summary="How to choose, construct and evaluate the main statistical maps (choropleth, isoline, flow-line, proportional symbol, dot) and diagrams (climograph, pie and divided bar, triangular graph).",
    objectives=[
        "Choose class intervals and shading for a choropleth map, including classes based on quartiles",
        "Construct isoline, flow-line and proportional-symbol maps with correct scales",
        "Draw and interpret a climograph, including the rainfall regime of an equatorial station",
        "Evaluate the strengths and limitations of each technique",
    ],
    key_concepts=["Choropleth map", "Class interval", "Isoline", "Interpolation", "Flow-line map", "Proportional symbol", "Climograph", "Triangular graph"],
    blocks=[
        H("Introduction"),
        T("Numbers become geography when they are mapped. A table of population densities for the divisions of a region is hard to read; a shaded map shows the pattern at a glance. "
          "The Board's 2023 report recorded that the statistics question (on a choropleth, the interquartile range and a climograph) was the least popular in Paper 3, and that many graphs had no titles or labelled axes. "
          "Learning the conventions below gives you marks that many candidates leave behind."),
        H("Choropleth maps"),
        D("A **choropleth map** shades each area unit (division, region, district) according to the class into which its value falls, with darker or denser shading for higher values.", title="Definition: choropleth map"),
        T("Rules: map **ratios** such as density or percentages, not raw totals (a big division would look important just because it is big); use **4 to 6 classes**; use one colour graded from light (low) to dark (high); give a key with the class limits, a title, a scale and a north arrow. "
          "Class intervals can be **equal** (range ÷ number of classes), based on **quartiles** (so each class holds about a quarter of the units), or set at **natural breaks** in the data."),
        IMG("algpu3-choropleth.svg", alt="A schematic region of six divisions A to F shaded in four blue tones by population density: A 18 and D 32 lightest, B 64 light, E 96 and F 120 medium, C 145 darkest; a key gives classes 0 to 49, 50 to 99, 100 to 149 and 150 and over.",
            caption="Figure 1. A choropleth map with equal class intervals of 50 persons per km² (invented data)."),
        EX("Worked example 1: classes from quartiles", intro="Eleven divisions have densities (persons per km²) of 12, 18, 25, 32, 45, 64, 88, 96, 120, 145 and 210. Use the quartiles to create four classes.", steps=[
            S("Data already in order; n = 11", text="Median = 6th value = 64. LQ = 3rd value = 25. UQ = 9th value = 120."),
            S("Interquartile range", math=r"\text{IQR} = 120 - 25 = 95"),
            S("Classes", text="Class 1: up to 25 (3 divisions); class 2: 26 to 64 (3); class 3: 65 to 120 (3); class 4: above 120 (2). Each class holds about a quarter of the divisions."),
            S("Why use quartiles", text="Equal intervals of 50 would put five divisions in the lowest class and leave a nearly empty top class because of the extreme value 210. Quartile classes spread the units more evenly across the shades."),
        ]),
        KEY("Strengths and limitations of choropleths", "Use them for ratios over areas.", cards=[
            ["Strengths", "Clear visual pattern; easy to compare regions; good for densities, percentages and rates."],
            ["Limitations", "Implies an even value across each unit and sudden changes at boundaries; large units dominate the eye; the pattern changes with the choice of class intervals and units."],
        ]),
        H("Isoline maps"),
        D("An **isoline** joins points of equal value: contours (height), isotherms (temperature), isohyets (rainfall), isobars (pressure) and isochrones (travel time). Lines are placed by **interpolation** between the values at known points.", title="Definition: isoline"),
        EX("Worked example 2: interpolation", intro="Two rain gauges 3 cm apart on a map record 640 mm and 700 mm. Where should the 660 mm isohyet cross the line between them?", steps=[
            S("Fraction of the difference", math=r"\frac{660 - 640}{700 - 640} = \frac{20}{60} = \frac{1}{3}"),
            S("Distance", math=r"\frac{1}{3} \times 3 \text{ cm} = 1 \text{ cm from the 640 mm gauge}"),
        ], check=r"640 + \frac{1}{3} \times 60 = 660"),
        T("Isolines suit values that change gradually across space (temperature, rainfall, relief). They need many, well-spread data points, and they assume a steady change between points, which may hide local variations."),
        H("Flow lines, proportional symbols and dot maps"),
        T("A **flow-line map** shows movement (traffic, migrants, goods) along routes; the **width** of each line is proportional to the volume, and arrows show the direction. "
          "With a scale of 1 mm = 500 vehicles a day, a road carrying 3 750 vehicles a day is drawn 3 750 ÷ 500 = 7.5 mm wide. Flow lines show both route and volume, but wide lines overlap at junctions and in towns."),
        T("**Proportional symbols** (usually circles) are drawn at a place with an **area** proportional to its value, so the **radius** is proportional to the **square root** of the value. A **dot map** uses one dot for a fixed number (for example 1 dot = 500 cattle), placed where the items actually are."),
        EX("Worked example 3: proportional circles", intro="A city of 2 500 000 people is shown by a circle of radius 2.5 cm. What radius should be used for towns of 900 000 and 400 000?", steps=[
            S("Radius is proportional to the square root", math=r"r = 2.5 \times \sqrt{\frac{900\,000}{2\,500\,000}} = 2.5 \times 0.6 = 1.5 \text{ cm}"),
            S("Second town", math=r"r = 2.5 \times \sqrt{\frac{400\,000}{2\,500\,000}} = 2.5 \times 0.4 = 1.0 \text{ cm}", text="If the radius were made proportional to the value itself, the large city's circle would look far too big compared with the towns."),
        ], check=r"\sqrt{0.36} = 0.6, \quad \sqrt{0.16} = 0.4"),
        H("Climographs and other diagrams"),
        D("A **climograph** (climate graph) shows monthly rainfall as **bars** (left axis, mm) and monthly mean temperature as a **line** (right axis, °C), month by month, on one diagram.", title="Definition: climograph"),
        IMG("algpu3-climograph.svg", alt="Climograph of station K: rainfall bars with two peaks, 220 mm in May and 290 mm in October, and dry months in December to February and in July; the temperature line stays between about 23 and 25.6 degrees Celsius all year.",
            caption="Figure 2. Climograph of station K (invented data, similar to a station near the equator in southern Cameroon)."),
        T("Reading Figure 2: annual rainfall = 1 605 mm; there are **two rainfall maxima** (May and October) separated by a drier spell in July and August and a dry season from December to February; the annual temperature range is only 25.6 − 23.1 = 2.5 °C. "
          "**Why two maxima?** Near the equator the overhead midday sun, and with it the belt of rising air and convectional rain associated with the ITCZ, passes over the station twice a year, on its way north and on its way back south. "
          "**Why is the temperature nearly constant?** The midday sun is high in the sky in every month and day length hardly changes, so heating is similar all year; the slightly cooler months coincide with the cloudier rainy period."),
        KEY("Other diagrams to know", "Match the diagram to the data.", cards=[
            ["Pie chart and divided bar", "Show parts of a whole; angle = value ÷ total × 360°. A crop taking 45 of 120 hectares gets 135°."],
            ["Triangular graph", "Three components that add up to 100%: employment in primary, secondary and tertiary sectors, or sand, silt and clay in soil."],
            ["Dispersion diagram and box plot", "Show the spread of values along one axis; mark the median and quartiles."],
            ["Scatter graph", "Two variables, to look for correlation (see the correlation lesson)."],
        ]),
        MISTAKE("Mapping totals on a choropleth", "Shading total population makes large divisions look crowded. Convert to densities or percentages first."),
        MISTAKE("Graphs without titles, axes labels or units", "The Board's 2023 report noted climographs with unlabelled axes and no titles. Every graph needs a title, both axes labelled with units, a key and a sensible scale."),
        QUIZ("Which technique is most suitable for showing the number of vehicles using each road into a town?", ["Choropleth map", "Isoline map", "Flow-line map", "Triangular graph"], 2,
             "Flow lines show route and volume of movement, with width proportional to traffic.", hint="Which map shows movement along routes?",
             feedback=["Choropleths shade areas, not routes.", "Isolines join points of equal value over a surface.", "", "A triangular graph shows three percentage components."]),
        QUIZ("On a climograph of an equatorial station, why are there two rainy seasons?", ["The sea is warmer twice a year", "Trade winds blow from the sea all year", "The overhead sun and the rain belt pass over the station twice a year", "Mountains block the rain in the middle of the year"], 2,
             "The overhead sun (and the ITCZ rain belt) crosses the station twice a year, each time bringing a rainy season.", hint="Think about the apparent movement of the overhead sun between the tropics.",
             feedback=["Sea temperature does not explain a double maximum in this way.", "Constant winds would not give two separate peaks.", "", "Relief does not explain a double maximum."]),
        TIP("In Paper 3 the statistics question may ask you to draw a diagram (climograph, choropleth, proportional symbols), state the advantages of the technique, and explain the pattern it shows. Bring a ruler, pencil and calculator, and practise drawing to scale under time.", title="Exam link"),
        PQ("State three advantages of showing climate data as a climograph rather than in a table.",
           "It shows rainfall and temperature together, so their relationship (for example, the wettest months being slightly cooler) is clear. The seasonal pattern, such as the two rainfall maxima, is visible at a glance. Different stations can be compared quickly by their shapes, and extremes (the wettest and driest months, the annual range) are easy to pick out."),
        PQ("Pie chart: a farm of 120 ha has 45 ha of cocoa, 30 ha of plantain, 25 ha of cassava and 20 ha of fallow. Calculate the angle for each sector.",
           "Angle = area ÷ 120 × 360. Cocoa 45 → 135°; plantain 30 → 90°; cassava 25 → 75°; fallow 20 → 60°. Check: 135 + 90 + 75 + 60 = 360°."),
        PQ("Explain two limitations of a choropleth map of population density.",
           "It shows each division as if the density were the same everywhere inside it, hiding concentrations such as a town within a mostly empty division. It suggests abrupt changes at administrative boundaries, while real densities change gradually. Its appearance also depends on the choice of class intervals, so the same data can give different-looking maps."),
        SUM("Choropleths shade areas by ratios (density, percentage) in 4 to 6 graded classes; classes may be equal, quartile-based or natural breaks.",
            "Isolines join equal values by interpolation; they suit gradually changing data.",
            "Flow-line width is proportional to volume; proportional circles have radius proportional to the square root of the value.",
            "A climograph shows rainfall bars and a temperature line; equatorial stations show two rainfall maxima and a small temperature range.",
            "Every map or graph needs a title, key, scale or labelled axes with units."),
    ],
))

# ------------------------------------------------------------------ 6. Fieldwork research design
LESSONS.append(lesson(
    module=M_STAT,
    topic="Fieldwork research design",
    title="Designing and reporting a geographical field investigation",
    slug="gpu3-fieldwork-research-design",
    minutes=25,
    summary="How to plan, carry out and report a field investigation: aim, hypotheses and objectives, sampling, data-collection tools, processing and testing, conclusions and evaluation, with a stream channel study worked through.",
    objectives=[
        "Distinguish an aim, an objective and a hypothesis, and write null and alternative hypotheses",
        "Choose a sampling method and data-collection tools suited to the question",
        "Process field data, such as channel area, hydraulic radius and discharge, and choose a statistical test",
        "Write a conclusion that answers the hypothesis and evaluate the investigation and its value to the community",
    ],
    key_concepts=["Aim", "Hypothesis", "Objective", "Sampling", "Primary data", "Risk assessment", "Hydraulic radius", "Discharge", "Evaluation"],
    blocks=[
        H("Introduction"),
        T("The Board's 2023 report showed that the fieldwork question in Paper 3 is now the most popular question after the compulsory map work, and that its choice has risen steadily since 2019. "
          "It also showed why marks were lost: unclear objectives and hypotheses, data-collection tools confused with classroom materials, invented figures, graphs without titles or labelled axes, and conclusions not linked to the hypothesis. "
          "The report also advised candidates not to choose the fieldwork question unless they really carried out the fieldwork. This lesson gives you a framework that avoids every one of those problems."),
        IMG("algpu3-enquiry.svg", alt="Six boxes linked by arrows in a loop: 1 aim and hypotheses, 2 site and sampling, 3 data collection, 4 processing and presentation, 5 analysis and tests, 6 conclusion and evaluation, with a dashed arrow from 6 back to 1 labelled results tested against the hypothesis.",
            caption="Figure 1. The route of a geographical enquiry."),
        H("Aim, objectives and hypotheses"),
        KEY("Three different things", "Examiners expect you to keep them apart.", cards=[
            ["Aim", "The broad purpose: To investigate how the characteristics of River X change downstream."],
            ["Objective", "A specific task that helps achieve the aim: To measure the width, depth and velocity at five sites 200 m apart."],
            ["Hypothesis", "A testable statement of the expected relationship: The cross-sectional area of River X increases downstream."],
        ]),
        D("The **null hypothesis (H0)** states that there is no significant relationship or difference (There is no significant relationship between distance downstream and cross-sectional area). The **alternative hypothesis (H1)** states that there is one. A statistical test decides between them.", title="Null and alternative hypotheses"),
        T("Keep to **one** clear topic and objective set for each investigation; the Board's report advised against handling several related topics on one outing. Choose a site close to school that you can visit safely, and state its location with a sketch map."),
        H("Sampling and data collection"),
        KEY("Sampling methods", "You can rarely measure everything.", cards=[
            ["Random", "Every point has an equal chance (random number tables or a calculator). Avoids bias but may miss parts of the area."],
            ["Systematic", "At regular intervals (every 200 m along a river, every fifth house). Covers the area evenly and is easy, but may miss or repeat a pattern."],
            ["Stratified", "Samples in proportion to sub-groups (land-use zones, age groups, rock types). Represents every group, but needs prior knowledge of the groups."],
        ]),
        T("Samples may be taken at **points**, along **lines** (transects) or in **areas** (quadrats). **Primary data** are collected by you in the field; **secondary data** come from others (maps, census reports, rainfall records). "
          "**Data-collection tools** are the instruments that produce the data: tape measure, metre rule or ranging pole, float and stopwatch or flow meter, clinometer, quadrat, thermometer, questionnaire, land-use recording sheet, GPS or a phone compass. Pens and notebooks are not data-collection tools. "
          "Before collecting data, carry out a **pilot survey**, a **risk assessment** (deep water, traffic, weather, animals) and obtain **permission** from the people and authorities concerned. Respect the people you question: explain the purpose, keep answers anonymous and do not pressure anyone."),
        H("Worked example: a stream channel study"),
        IMG("algpu3-channel.svg", alt="Cross-section of a stream 4.0 m wide with depth readings every 0.5 m: 0.20, 0.35, 0.50, 0.55, 0.45, 0.30 and 0.15 m, zero at both banks.",
            caption="Figure 2. Field measurements at site 1 (invented for practice)."),
        EX("Worked example 1: processing the channel data", intro="At site 1 the stream is 4.0 m wide, with depths every 0.5 m as in Figure 2. A float travels 10 m in an average of 25 s (three timings: 24, 26 and 25 s). Calculate the cross-sectional area, hydraulic radius and discharge.", steps=[
            S("Cross-sectional area", math=r"A = 0.5 \times (0.20 + 0.35 + 0.50 + 0.55 + 0.45 + 0.30 + 0.15) = 0.5 \times 2.50 = 1.25 \text{ m}^2", text="Each reading represents a strip 0.5 m wide (with zero depth at both banks this equals the trapezium method)."),
            S("Wetted perimeter", text="Measured along the bed with a tape (or calculated from the readings): 4.16 m."),
            S("Hydraulic radius", math=r"R = \frac{A}{\text{wetted perimeter}} = \frac{1.25}{4.16} = 0.30 \text{ m}", text="The higher R, the less friction per unit of water and the more efficient the channel."),
            S("Velocity", math=r"v_{\text{surface}} = \frac{10}{25} = 0.40 \text{ m s}^{-1}; \quad v \approx 0.8 \times 0.40 = 0.32 \text{ m s}^{-1}", text="The surface float moves faster than the water near the bed, so a correction factor is used (often 0.8; some textbooks use 0.85, so check yours)."),
            S("Discharge", math=r"Q = A \times v = 1.25 \times 0.32 = 0.40 \text{ m}^3 \text{ s}^{-1} \text{ (cumecs)}"),
        ], check=r"1.25 \times 0.32 = 0.40"),
        T("Repeat at every site, present the results (cross-sections drawn to scale, a line graph of discharge against distance, a table with titles and units) and test the hypothesis: for example, Spearman's rank correlation between distance downstream and cross-sectional area, with H0 accepted or rejected at the 0.05 level. "
          "Then explain the results (more tributaries and a larger drainage area downstream increase discharge) and note anomalies (a bridge, a weir or a rock bar at one site)."),
        EX("Worked example 2: planning a functional segregation study", intro="Plan an investigation into functional segregation (the separation of land uses) in a town.", steps=[
            S("Aim and hypothesis", text="Aim: to investigate how land use changes with distance from the town centre. H1: the proportion of commercial land use decreases with distance from the centre. H0: there is no significant relationship between distance and the proportion of commercial land use."),
            S("Sampling and tools", text="Systematic sampling along two transects from the centre, recording the ground-floor use of every building in 100 m sections on a land-use recording sheet; a base map and a tape or GPS for distance."),
            S("Processing and test", text="Percentage of commercial use in each section; divided bars or a land-use map; Spearman's rank between distance and % commercial (or chi-squared on counts of uses in inner and outer zones)."),
            S("Conclusion and evaluation", text="State whether H0 is rejected, link to bid-rent and accessibility, evaluate (sample size, one day only, classification problems for mixed-use buildings) and explain the value of the results to the town council."),
        ]),
        H("Writing the conclusion and evaluation"),
        T("A good conclusion **refers back to the hypothesis** using the evidence: The Spearman value of 0.90 is above the critical value, so H0 is rejected; the cross-sectional area increases downstream. "
          "The **evaluation** discusses problems encountered (rain the day before raised the water level, a float caught on a branch), the reliability of the data (number of sites, repeats) and how the study could be improved. "
          "Finally, show the **significance to the community**: for example, the flow data help plan a footbridge or a water supply point, and a land-use study helps the council plan parking and markets. This is the importance to the community, not to you as a student."),
        MISTAKE("Mixing up objectives and hypotheses", "An objective is a task (to measure); a hypothesis is a testable prediction (X increases with Y). The 2023 report noted candidates who gave only one of the two or confused them."),
        MISTAKE("Listing classroom materials as tools", "Pens, rulers for writing and exercise books are not data-collection tools. Name the instrument and what it measured, for example a stopwatch and float to measure surface velocity."),
        MISTAKE("Memorised or invented figures", "Examiners recognise impossible or copied numbers (for example a stream velocity of 25 m/s). Use realistic values from your own fieldwork and show how they were processed."),
        QUIZ("Which statement is a hypothesis?", ["To measure the velocity of the stream at five sites", "To investigate the characteristics of River X", "Stream velocity increases with distance downstream", "A tape measure was used to measure the width"], 2,
             "A hypothesis is a testable statement predicting a relationship.", hint="Which statement can be proved right or wrong with data?",
             feedback=["This is an objective (a task).", "This is the aim.", "", "This describes a method and a tool."]),
        QUIZ("A student samples every fifth shop along a street. What kind of sampling is this?", ["Random", "Stratified", "Opportunistic", "Systematic"], 3,
             "Choosing at a regular interval is systematic sampling.", hint="Is the interval regular or chosen by chance?",
             feedback=["Random sampling uses random numbers, not a fixed interval.", "Stratified sampling divides the population into groups first.", "Opportunistic sampling takes whatever is convenient.", ""]),
        TIP("The fieldwork question in Paper 3 typically asks you to locate the study area (sketch map), state objectives and hypotheses, the tools and how data were collected, how data were processed and presented, the findings related to the hypothesis, and the importance of the study. Practise writing each part in a few clear sentences.", title="Exam link"),
        PQ("A second site downstream has a cross-sectional area of 2.1 m² and a wetted perimeter of 4.79 m. The float covers 10 m in 20 s (correction factor 0.8). Calculate the hydraulic radius and the discharge, and compare with site 1 (R = 0.30 m, Q = 0.40 m³/s).",
           "R = 2.1 ÷ 4.79 = 0.44 m. Surface velocity = 10 ÷ 20 = 0.50 m/s; mean velocity = 0.8 × 0.50 = 0.40 m/s. Q = 2.1 × 0.40 = 0.84 m³/s. Downstream the channel is larger and more efficient (higher hydraulic radius), and discharge has roughly doubled, supporting the hypothesis that discharge increases downstream."),
        PQ("State three precautions to take before and during a field visit to a river.",
           "Carry out a risk assessment and check the weather and water level, avoiding the river after heavy rain. Work in groups with a teacher, wear suitable footwear and do not enter water deeper than knee height or fast-flowing water. Obtain permission from landowners or local authorities and do not damage crops or property."),
        PQ("Explain how the results of a study of traffic congestion in a town centre could be useful to the local community.",
           "Counts of vehicles at different times identify the busiest roads and peak hours. The council could use them to plan one-way systems, parking areas, lorry loading times or a bypass. Traders and transport operators could adjust their hours, and residents benefit from shorter journeys and less pollution."),
        SUM("Aim = purpose; objective = task; hypothesis = testable prediction; H0 states no significant relationship.",
            "Choose random, systematic or stratified sampling at points, along transects or in areas; collect primary data with proper instruments.",
            "Do a pilot survey, a risk assessment and ask permission; respect the people you survey.",
            "Process and test: e.g. A = Σ(depth × interval), R = A ÷ wetted perimeter, Q = A × v; then Spearman or chi-squared.",
            "Conclude against the hypothesis, evaluate the method, and explain the value of the study to the community."),
    ],
))

# ------------------------------------------------------------------ Examination 1. Paper 1
LESSONS.append(lesson(
    module=M_EXAM,
    topic="Paper 1",
    title="Paper 1: fifty multiple-choice questions across physical and human geography",
    slug="gpu3-paper1-multiple-choice",
    minutes=22,
    summary="How Paper 1 of A Level Geography is built (50 multiple-choice questions in a physical and a human section), a routine for every question, how to handle calculations and data, and a revision map of the whole syllabus.",
    objectives=[
        "Describe the structure of Paper 1 as reported by the Board in 2023",
        "Use a read, predict, eliminate, check routine on every question",
        "Answer calculation and data questions quickly and accurately",
        "Plan revision across all Lower and Upper Sixth modules",
    ],
    key_concepts=["Stem", "Distractor", "Elimination", "Section A physical", "Section B human", "Calculation question", "Revision map"],
    blocks=[
        H("Introduction"),
        T("Paper 1 is the multiple-choice paper of the 0750 Geography examination. The Board's 2023 subject report states that it had **fifty questions**, as the syllabus stipulates, divided into **Section A (physical geography)** and **Section B (human geography)** of **25 questions each**, and that it is marked by machine. "
          "The report rated the 2023 paper as more demanding than the 2022 one. Because every question is worth the same and is simply right or wrong, careful technique turns knowledge into marks."),
        CODE("Section A: physical                    Section B: human\n"
             "Meteorology, climatology,               Population             7\n"
             "  hydrology                   8         Economic activity      8\n"
             "Geomorphology                 7         Settlement             7\n"
             "Biogeography                  7         Development issues     3\n"
             "Environmental issues          3\n"
             "Total                        25         Total                 25", "text",
             title="Table 1. Questions per syllabus area in the 2023 Paper 1 (Board's 2023 report)"),
        T("Use Table 1 as a guide to the balance, not as a promise: the spread may change from year to year. Notice that economic activity (farming, industry, transport, trade, tourism) carried the largest share of the human section, and that statistics, map work and Cameroon examples can appear inside any syllabus area."),
        H("A routine for every question"),
        KEY("Read, predict, eliminate, check", "Do it every time, quickly.", cards=[
            ["1. Read the stem", "Underline the key words: NOT, MOST, LEAST, BEST, EXCEPT, the units and any figures."],
            ["2. Predict", "Answer in your head before you look at the options, so an attractive wrong option does not lead you."],
            ["3. Eliminate", "Cross out options you know are wrong and say why: reversed, half-right, about another topic, or an unfinished calculation."],
            ["4. Check", "Re-read the stem with your chosen option. For a calculation, check units and size."],
        ]),
        T("In the KKEVO mock that goes with this lesson we set 90 minutes for 50 questions (a KKEVO practice setting, not a Board timing): just under two minutes a question. Do a first pass answering what you know, mark the hard ones and come back. Never leave a blank."),
        H("Calculation and data questions"),
        EX("Worked example 1: a calculation question", intro="In von Thünen's model a crop has p − c = FCFA 60 000 per tonne and a freight rate f = FCFA 1 500 per tonne per km. Where is its margin of cultivation? A 0.025 km, B 40 km, C 400 km, D 4 km.", steps=[
            S("Predict", text="The margin is where rent falls to zero: d = (p − c) ÷ f."),
            S("Calculate", math=r"d = \frac{60\,000}{1\,500} = 40 \text{ km}"),
            S("Eliminate", text="A divides the wrong way round (1 500 ÷ 60 000); C and D come from misplaced zeros (dividing by 150 or by 15 000). The answer is B."),
        ], check=r"60000/1500 = 40"),
        EX("Worked example 2: a statistics data question", intro="A Spearman test on 10 pairs gives rs = 0.70. The critical values are about 0.65 (0.05) and 0.79 (0.01). Which statement is correct? A The result is significant at the 0.01 level. B There is no relationship. C The result is significant at the 0.05 level only. D The variables are negatively related.", steps=[
            S("Compare", text="0.70 is above 0.65 but below 0.79."),
            S("Decide", text="Significant at 0.05 but not at 0.01: option C. A over-claims, B ignores the coefficient and D has the wrong sign."),
        ]),
        H("Traps built into wrong options"),
        KEY("Common distractors in geography", "Recognise the pattern.", cards=[
            ["Reversed", "Increase for decrease, windward for leeward, core for periphery, regular for clustered."],
            ["Related but different idea", "Linkages offered for agglomeration, urbanization for suburbanization, foreign trade for foreign aid, drought for desertification. The 2023 report found these confusions in essays too."],
            ["Wrong model", "A feature of Weber's model attached to Lösch, or of Burgess to Hoyt."],
            ["Unfinished or inverted calculation", "√(A ÷ n) instead of √(n ÷ A); the first step only; a percentage not multiplied by 100."],
            ["Absolute words", "Always, never, only: rarely true in geography, where places differ."],
        ]),
        H("A revision map of the whole syllabus"),
        CODE("Lower Sixth                            Upper Sixth\n"
             "Hydrology & fluvial geomorphology      Agricultural geography\n"
             "Meteorology & climatology              Industry, transport & services\n"
             "Biogeography & pedology                Regional development & disparities\n"
             "Tectonic, slope, coastal, arid         Geography of Cameroon\n"
             "Population & migration                 Map work\n"
             "Settlement & urban geography           Statistics & fieldwork", "text",
             title="Table 2. Modules to revise for Paper 1"),
        T("The KKEVO 'Paper 1 mock exam A' for this course samples only the six Upper Sixth modules, in proportion to their topics. The real Paper 1 samples the whole syllabus, so use the Lower Sixth mocks as well."),
        MISTAKE("Changing answers without a reason", "Change an answer only when you find a definite error in your reasoning, not because of a feeling."),
        MISTAKE("Reading only half of the stem", "Questions with NOT or EXCEPT reverse what you look for. Circle these words before you answer."),
        QUIZ("Which question word in a stem most often causes careless errors?", ["Describe", "NOT", "Calculate", "Which"], 1,
             "A NOT question asks for the false statement; candidates who miss the word choose a true statement.", hint="Which word reverses what you are looking for?",
             feedback=["'Describe' is a Paper 2 command word, not a multiple-choice trap.", "", "Calculate tells you what to do; it does not reverse the task.", "'Which' simply introduces the question."]),
        QUIZ("Twelve villages lie in 48 km² with a mean nearest-neighbour distance of 2.0 km. Rn = ?", ["4.0", "1.0", "2.0", "0.5"], 2,
             "√(12 ÷ 48) = 0.5; Rn = 2 × 2.0 × 0.5 = 2.0, close to regular.", hint="Find √(n ÷ A) first.",
             feedback=["This uses √(A ÷ n) = 2 instead of √(n ÷ A).", "This forgets the factor 2.", "", "This is √(n ÷ A) alone."]),
        TIP("Paper 1 rewards breadth: a little on every topic is worth more than a lot on a few. Revise with short daily sets of questions, and learn the formulas (Rn, rs, χ², CV, gradient, VE, sinuosity, beta index, von Thünen rent) with what each value means.", title="Exam link"),
        PQ("A question asks: 'Which of the following is NOT a cause of industrial agglomeration?' Explain how you would approach it.",
           "Circle NOT. Recall the causes of agglomeration (shared infrastructure, a pool of skilled labour, nearby suppliers and markets, specialised services). Test each option: those that are causes are wrong answers here. The correct answer is the one option that is not a cause, for example a feature of deindustrialization."),
        PQ("A crop gives R = Y(p − c) − Yfd with Y = 4 t/ha, p − c = FCFA 50 000 per tonne and f = FCFA 1 000 per tonne-km. What is the rent at 20 km? A FCFA 120 000, B FCFA 200 000, C FCFA 80 000, D FCFA 30 000.",
           "R = 4 × 50 000 − 4 × 1 000 × 20 = 200 000 − 80 000 = FCFA 120 000: A. B is the rent at the market (d = 0); C is only the transport cost; D forgets to multiply by the yield (50 000 − 20 000)."),
        PQ("Why should you never leave a multiple-choice question blank?",
           "A blank cannot score. Eliminating even one or two options raises the chance of choosing the right one. Mark the question, make your best choice and return to it if time allows."),
        SUM("Paper 1: 50 multiple-choice questions, Section A physical and Section B human, 25 each (2023 report); machine-marked.",
            "Routine: read the stem, predict, eliminate with reasons, check.",
            "Wrong options are reversed, related-but-different, from the wrong model, or unfinished calculations.",
            "Learn the formulas with the meaning of their values.",
            "Revise all twelve modules; the KKEVO mock A covers the Upper Sixth six."),
    ],
))

# ------------------------------------------------------------------ Examination 2. Paper 2
LESSONS.append(lesson(
    module=M_EXAM,
    topic="Paper 2",
    title="Paper 2: planning and writing A Level geography essays",
    slug="gpu3-paper2-essay-technique",
    minutes=24,
    summary="The structure of Paper 2 (physical, human and contemporary environmental and development issues), command words, how to plan and write a high-level answer with Cameroon examples, and the errors the Board reported in 2023.",
    objectives=[
        "Describe the structure of Paper 2 as reported by the Board in 2023",
        "Interpret command words and the exact scope of a question",
        "Plan an answer with defined terms, developed points, examples and evaluation",
        "Avoid the digressions and confusions reported by examiners",
    ],
    key_concepts=["Command word", "Section C (CEDI)", "Essay plan", "Developed point", "Case study", "Evaluation", "Digression"],
    blocks=[
        H("Introduction"),
        T("The Board's 2023 report describes Paper 2 as the paper on concepts and theories in physical and human geography. It had **7 questions** in **three sections**: "
          "**Section A, Physical Geography** (meteorology, climatology and hydrology; geomorphology; biogeography), **Section B, Human Geography** (population; economic activity; settlement), and "
          "**Section C, Contemporary Environmental and Development Issues (CEDI)**, set as one question with an EITHER (environmental issues) and an OR (development issues) option. "
          "Questions were structured in parts (a), (b), (c). The report does not state how many questions a candidate must answer, so read the rubric on the paper and check the current format with your teacher."),
        T("The report also tells teachers to follow the **new examination structure**, in which Cameroon geography is integrated into the branches tested in Paper 2 (for example the relief of Cameroon within geomorphology and its soils and vegetation within biogeography). So Cameroon examples now strengthen every essay."),
        H("Command words"),
        KEY("What the examiner wants", "Answer the command, not the topic.", cards=[
            ["Describe", "Say what is there or what happens: features, pattern, trend, with figures."],
            ["Explain / account for", "Give reasons: why or how something happens."],
            ["Examine / discuss", "Explain several sides or factors and weigh them; examples needed."],
            ["Assess / evaluate / to what extent", "Judge importance or success, with evidence for and against, and reach a conclusion."],
            ["Illustrate", "Use a diagram, graph or map as part of the answer, not just words. The 2023 report noted candidates who did not illustrate when asked."],
            ["Compare / contrast / differentiate", "Point-by-point similarities and/or differences, not two separate accounts."],
        ]),
        H("Planning a high-level answer"),
        T("Spend a few minutes planning each answer. A good plan has: (1) a short introduction that **defines the key terms properly** (the report warns that bald, one-line definitions are not acceptable at A Level); "
          "(2) one paragraph per point, each with **Point, Explanation and Example** (PEE), using named places in Cameroon and elsewhere; (3) **evaluation**: which factor matters most, limits of a model, success and failure of a measure; (4) a conclusion that answers the question."),
        EX("Worked example 1: a model plan on von Thünen", intro="Question: 'Using von Thünen's model, explain why land use becomes more extensive with distance from the market. To what extent does the model help to explain farming patterns around a Cameroonian city?'", steps=[
            S("Introduction", text="Name the model (von Thünen, 1826), its assumptions (isolated state, uniform plain, one market, transport cost proportional to distance) and define locational rent R = Y(p − c) − Yfd and extensive farming (low inputs per hectare)."),
            S("Explanation", text="Transport cost rises with distance, so locational rent falls; near the market high rent makes intensive use (vegetables, dairy) worthwhile; far away rent is low and extra inputs do not pay, so extensive use (grazing, grain) dominates. Use a rent-line diagram with ring boundaries."),
            S("Application", text="Around Yaoundé or Douala: market gardening and poultry on the edge of the city; food crops further out; extensive grazing or forest far away. Mention improved roads and refrigeration that stretch the rings."),
            S("Evaluation", text="Limitations: relief, soils and rivers break the rings; several markets; government policy; cash crops for export; behavioural decisions. The model remains useful as a principle (distance-decay of intensity) even where the rings are distorted."),
            S("Conclusion", text="Answer the 'to what extent': the principle helps, the exact pattern does not fit."),
        ]),
        EX("Worked example 2: a model plan for a Section C question", intro="Question: 'Differentiate between drought and desertification, and examine the effects of deforestation on local communities in Cameroon.'", steps=[
            S("Differentiate", text="Drought: a temporary period of well-below-normal rainfall (a meteorological event). Desertification: long-term land degradation in drylands, caused by climate variability and human activity. Contrast point by point: duration, cause, reversibility. The 2023 report found candidates writing two separate accounts or calling desertification deforestation."),
            S("Effects on local communities", text="Loss of fuelwood and non-timber products (bush mango, medicinal plants); soil erosion and lower yields; changing water supply; loss of cultural sites; some gain jobs in logging or farming. Name places (the forest of the East and South Regions, the Far North for fuelwood pressure)."),
            S("Evaluate", text="Balance short-term income against long-term loss; distinguish measures proposed from measures actually carried out, as the report recommends."),
        ]),
        KEY("Errors reported by the Board in 2023 (paraphrased)", "Turn them into checks.", cards=[
            ["Wrong model or concept", "Not recognising von Thünen's model; using another model instead; agglomeration confused with industrial linkages; suburbanization confused with urbanization or rural-urban migration."],
            ["Describing instead of answering", "Giving the features of the Demographic Transition Model when its significance was asked; listing problems when solutions were asked."],
            ["One-sided explanations", "Factors of transport connectivity explained only negatively; give both how a factor helps and how it hinders."],
            ["Generalised examples", "Effects of deforestation described in general instead of on local communities; measures not linked to the problems identified."],
        ]),
        MISTAKE("Bald definitions", "A one-line definition earns little. Define, then expand: Suburbanization is the outward growth of urban areas as people and activities move from the inner city to the edges, which in developed countries is driven by..."),
        MISTAKE("Answering the topic, not the question", "If the question asks for two measures to reduce traffic congestion, do not write about its causes. Underline the command word and the scope (two, Cameroon, developed countries) before planning."),
        QUIZ("A question asks you to 'examine two merits and two demerits of industrial agglomeration'. Which plan fits best?",
             ["Define agglomeration; explain two merits and two demerits with examples; brief judgement", "Describe the types of industrial linkage", "List ten advantages of industry", "Explain Weber's theory in full"], 0,
             "The plan matches the command (examine), the number (two and two) and the concept (agglomeration).", hint="Check the concept and the number asked for.",
             feedback=["", "Linkages are a cause of agglomeration, not the same thing; the report noted this confusion.", "A list ignores 'two' and 'examine'.", "Weber's theory is not what is asked."]),
        QUIZ("Which command word requires a judgement supported by evidence on both sides?", ["Describe", "State", "Identify", "To what extent"], 3,
             "To what extent asks you to weigh evidence and conclude.", hint="Which command asks 'how far'?",
             feedback=["Describe asks what is there, not a judgement.", "State asks for a brief answer without discussion.", "Identify asks you to name or pick out.", ""]),
        TIP("Paper 2 rewards depth: defined terms, developed explanations, named examples (with Cameroon now part of every branch), diagrams where they help and a judgement. In the KKEVO 'Paper 2 practice paper A' the parts test planning, key arguments, diagrams and calculations, because essays cannot be marked automatically.", title="Exam link"),
        PQ("Write a plan for: 'Explain three factors that influence the degree of connectivity of a transport network in a region.'",
           "Introduction: define connectivity (the degree to which nodes in a network are directly linked; measured by the beta index e ÷ v). Factor 1, relief: flat land allows many links (higher connectivity), steep or swampy land limits them. Factor 2, level of economic development and capital: richer regions build more links. Factor 3, population density and economic activity: dense, productive areas generate traffic that justifies links; sparse areas have few. For each, give both the positive and negative effect and an example (dense road network in the Littoral; sparse links in parts of the East). Conclude on which factor is most important."),
        PQ("What is wrong with this answer: 'Suburbanization is when people move from rural areas to towns because of jobs.'?",
           "It describes rural-urban migration (part of urbanization), not suburbanization. Suburbanization is the outward movement of people, housing and services from the inner city to the suburbs on the edge of the urban area, driven in developed countries by car ownership, better transport, cheaper land and a desire for space and a cleaner environment."),
        PQ("State four features of a good Paper 2 introduction.",
           "It defines the key terms fully (not bald definitions); it shows that the candidate understands the exact question; it states the scope (place, scale, model); and it outlines the line of argument or the structure of the answer."),
        SUM("Paper 2 (2023): 7 structured questions in Section A physical, Section B human and Section C CEDI (Either environmental, Or development); check the rubric for how many to answer.",
            "Cameroon geography is now integrated into the Paper 2 branches: use Cameroon examples.",
            "Read the command word and the scope; plan before writing.",
            "Define terms fully, use Point, Explanation, Example, add diagrams where useful, and evaluate.",
            "Avoid the reported confusions: agglomeration and linkages, suburbanization and urbanization, drought and desertification, aid and trade."),
    ],
))

# ------------------------------------------------------------------ Examination 3. Paper 3
LESSONS.append(lesson(
    module=M_EXAM,
    topic="Paper 3",
    title="Paper 3: map work, fieldwork and techniques, and the geography of Cameroon",
    slug="gpu3-paper3-practical-paper",
    minutes=24,
    summary="The structure of Paper 3 (compulsory map work, fieldwork and statistical techniques, and Cameroon), how to use map evidence, how to write a fieldwork answer, how to tackle the statistics question, and the Board's 2023 comments.",
    objectives=[
        "Describe the structure of Paper 3 as reported by the Board in 2023",
        "Answer map work questions with map evidence, calculations and interpretations",
        "Write a structured fieldwork answer and a statistics answer",
        "Answer Cameroon questions with concrete, located examples",
    ],
    key_concepts=["Map evidence", "Sinuosity", "Relief description", "Fieldwork report", "Statistical technique", "Concrete example", "Problem-solving"],
    blocks=[
        H("Introduction"),
        T("The Board's 2023 report describes Paper 3 as the paper on the **application** of knowledge. It had **7 questions** in three sections: **Section A, map work** (one compulsory question); "
          "**Section B, fieldwork and techniques** (two questions: one on fieldwork and one on statistical techniques); and **Section C, Cameroon geography** (four questions). "
          "The map work question was the most attempted (it is compulsory), fieldwork was second, and the statistics question was the least popular. Check the rubric and the current format with your teacher, because the report also asks teachers to apply the new structure that integrates Cameroon geography into Paper 2."),
        H("Section A: map work"),
        KEY("What the 2023 report asked for", "Turn the comments into habits.", cards=[
            ["Divide the map", "Use eastings, northings, cardinal directions and relief regions to divide the map into parts, and describe each (for example east and west of a stated easting)."],
            ["Describe relief properly", "Height (in metres, from contours and spot heights), nature of slopes (steep, gentle, concave, convex), main landforms (ridges, valleys, plateaus, spurs) and orientation."],
            ["Use map evidence only", "When told to use map evidence, quote what is on the map (swamps, river names, contour patterns, grid references), not general knowledge."],
            ["Interpret every value", "After a calculation (gradient, sinuosity, distance), say what it means: a sinuosity of 1.8 shows a strongly meandering river on gentle, low-lying land."],
            ["Solve problems", "Link physical features to development challenges (roads, farming, HEP) and propose realistic solutions."],
        ]),
        EX("Worked example 1: sinuosity and its meaning", intro="On a 1:50 000 map, a river measures 9.0 cm along its channel between two points that are 5.0 cm apart in a straight line. Calculate and interpret the sinuosity.", steps=[
            S("Formula", math=r"\text{sinuosity} = \frac{\text{channel length}}{\text{straight-line length}} = \frac{9.0}{5.0} = 1.8"),
            S("Interpret", text="Values near 1 show a straight channel; values above about 1.5 are usually called meandering (check the thresholds in your textbook). 1.8 shows a meandering river, typical of a gentle gradient on a floodplain, which may also flood and create swamps suitable for rice."),
        ], check=r"9.0/5.0 = 1.8"),
        H("Section B: fieldwork and statistical techniques"),
        T("The fieldwork question asks about a study you actually carried out: location with a sketch map that follows cartographic norms (title, frame, scale, north arrow, key), objectives and hypotheses, data-collection tools and their use, the procedure, processing and presentation, findings related to the hypothesis, and the importance of the study to the community. "
          "The report noted that statistics should be taught before fieldwork, because they are the tools of analysis."),
        T("The statistics question in 2023 asked candidates to represent climate data as a climograph, to give the advantages of the technique, and to explain the climate it showed (two rainfall maxima, nearly constant temperature); the report also listed the interquartile range and choropleth among the techniques tested. "
          "Very few candidates explained the two rainfall maxima. A well-prepared statistics candidate can score reliably because the methods are fixed and the answers can be checked."),
        EX("Worked example 2: a statistics answer in steps", intro="Ten settlements give rs = +0.96 for population against number of services. Write the analysis paragraph.", steps=[
            S("Hypotheses", text="H0: there is no significant relationship between population and the number of services. H1: there is a significant positive relationship."),
            S("Test", text="For n = 10 the critical value at the 0.01 level is about 0.79 (check your tables). 0.96 > 0.79, so reject H0 at the 0.01 level."),
            S("Explain", text="Larger settlements reach the thresholds of more services (central place theory), so they offer more and higher-order services."),
            S("Evaluate", text="Ten settlements is a small sample; anomalies (a small town with a large market) should be explained."),
        ]),
        H("Section C: Cameroon"),
        T("The 2023 report praised answers with concrete Cameroonian examples and criticised generalised ones. It asked for: sub-climates, not only the major climatic zones (for example contrasting the South Cameroon Plateau with the Adamawa Plateau); crops linked to farming systems; raw materials linked to particular industries; "
          "energy with concrete examples (HEP stations named, not just HEP in general); and a clear distinction between measures **proposed** and measures **actually carried out**."),
        MISTAKE("Speculative map answers", "Writing about modern machines or tarred roads when the question asks for strategies based on the map. Use features shown on the map and say where they are."),
        MISTAKE("Sketch maps without cartographic norms", "A fieldwork sketch map needs a title, frame, scale, north arrow and key. The report noted poorly made sketch maps and untitled graphs."),
        MISTAKE("Choosing fieldwork without having done it", "The report advised candidates not to attempt the fieldwork question if they did not carry out fieldwork; invented or memorised figures are easy to spot."),
        QUIZ("A map question says 'Using map evidence only, suggest why the valley floor is suitable for rice cultivation.' Which answer fits?",
             ["Rice needs capital and government support", "The flat land below the 1 100 m contour, the swamp symbols and the permanent river in the grid square provide level, waterlogged land", "Rice is common in northern Cameroon", "Rice is an important crop in Asia"], 1,
             "Only this answer uses features shown on the map, located by grid reference.", hint="Which answer could be proved by pointing at the map?",
             feedback=["This is general knowledge, not map evidence.", "", "This is general knowledge about another region.", "This is irrelevant to the map."]),
        QUIZ("In the 2023 Paper 3, which section contained the compulsory question?", ["Section A, map work", "Section B, fieldwork", "Section C, Cameroon", "None; all were optional"], 0,
             "The report states that the map work question in Section A is compulsory.", hint="Which question did almost every candidate answer?",
             feedback=["", "Fieldwork was the second most popular, but not compulsory.", "Section C offered four questions to choose from.", "The map work question was compulsory."]),
        TIP("Paper 3 is about using skills: measure accurately, show the formula and working, interpret every value, quote map evidence, follow the norms of graphs and sketch maps, and give Cameroonian examples by name. The KKEVO 'Paper 3 practice paper A' gives auto-marked parts in each section.", title="Exam link"),
        PQ("On a 1:50 000 map, two spot heights are 640 m and 440 m and are 4 cm apart. Calculate the average gradient and interpret it.",
           "Horizontal distance = 4 × 50 000 = 200 000 cm = 2 000 m. Vertical interval = 640 − 440 = 200 m. Gradient = 200 ÷ 2 000 = 1 in 10 (about 5.7°). A fairly steep slope: road builders would need bends (hairpins) or cuttings, and farming would need terraces to reduce erosion."),
        PQ("List the parts of a complete fieldwork answer in the order you would write them.",
           "Location of the study area with a sketch map (title, scale, north, key); aim, objectives and hypotheses; data-collection tools and their uses; procedure of data collection and sampling; data processing and presentation (tables, graphs, statistical tests); findings related to the hypothesis and conclusion; problems encountered and evaluation; importance of the study to the community."),
        PQ("Why did the Board's report recommend distinguishing 'proposed measures' from 'actual measures' in Cameroon answers?",
           "Because a question about what the government has done needs real policies and projects (named and located), while a question asking what could be done needs suggestions. Mixing them shows weak knowledge of Cameroon and does not answer the question set."),
        SUM("Paper 3 (2023): 7 questions; Section A map work (compulsory), Section B fieldwork and statistical techniques, Section C Cameroon (four questions); check the current format.",
            "Map work: divide the map, describe relief fully, use map evidence only, interpret every calculated value, solve problems.",
            "Fieldwork: location sketch map, objectives and hypotheses, tools, procedure, processing, findings against the hypothesis, value to the community.",
            "Statistics: name the technique, show working, test significance, explain and evaluate.",
            "Cameroon: concrete, named examples; sub-regional detail; proposed versus actual measures."),
    ],
))
