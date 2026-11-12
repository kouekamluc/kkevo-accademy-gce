"""A Level Economics (0725), Upper Sixth: Macroeconomic Problems, International Economics, Economic Growth, Development &
the Cameroonian Economy, and the Examination module.

14 topic lessons and 3 examination lessons (slugs ecu2-), one practice set each (see the practice file of the same name).
Content follows KKEVO's master curriculum blueprint (module lines U6M4 to U6M6) and the Board's 2023 subject report for exam
structure and common errors; it is not a Board syllabus booklet. All figures for countries and firms are invented for practice
unless stated otherwise. Facts about Cameroon are limited to well-established ones (CEMAC, BEAC, the CFA franc peg of 655.957
francs to the euro, the 1994 devaluation, the structural adjustment years, HIPC, Vision 2035, NDS30, AfCFTA); students are told
to check current data. Every calculation (rates, indices, multiplier-accelerator sequence, opportunity costs, balances,
exchange rates, HDI, Gini, Harrod-Domar) was checked by script.
"""

from .dsl import *  # noqa: F403

COURSE = ("economics", "upper-sixth")

M_PROB = "Macroeconomic Problems: Unemployment, Inflation & Trade Cycles"
M_INT = "International Economics"
M_DEV = "Economic Growth, Development & the Cameroonian Economy"
M_EXAM = "Examination"

LESSONS = []

# ------------------------------------------------------------------ 1. Unemployment
LESSONS.append(lesson(
    module=M_PROB,
    topic="Unemployment",
    title="Unemployment: measurement, types, costs and remedies",
    slug="ecu2-unemployment",
    minutes=24,
    summary="How unemployment is defined and measured, the main types (frictional, structural, seasonal, cyclical and real-wage), underemployment in an economy like Cameroon's, the costs of unemployment and the policies that match each type.",
    objectives=[
        "Define unemployment, the labour force and the unemployment rate, and calculate the rate and the participation rate",
        "Distinguish frictional, structural, seasonal, demand-deficient and real-wage unemployment, using diagrams",
        "Explain underemployment and disguised unemployment in a developing economy",
        "Match each type of unemployment to a suitable policy and evaluate the policy",
    ],
    key_concepts=["Labour force", "Unemployment rate", "Frictional unemployment", "Structural unemployment",
                  "Demand-deficient unemployment", "Real-wage unemployment", "Underemployment", "Natural rate of unemployment"],
    blocks=[
        H("Introduction"),
        T("Each year thousands of young Cameroonians leave secondary school and university and look for work. Some find a salaried job quickly, "
          "some wait months, and many take up small activities in the informal sector: selling phone credit, riding a motorbike taxi, helping in a family shop. "
          "Are they all employed? Economists need clear definitions before they can measure the problem, find its causes and choose a remedy. "
          "This lesson builds the A Level treatment of **unemployment**."),
        H("Definitions and measurement"),
        D("A person is **unemployed** if he or she is of working age, without work, available for work and actively looking for work. "
          "This is the standard definition used by the International Labour Organization (ILO) in labour force surveys.", title="Unemployment"),
        D("The **labour force** (economically active population) is everyone of working age who is either employed or unemployed. "
          "People who are not looking for work (full-time students, homemakers, the retired, discouraged workers) are **outside** the labour force.",
          title="Labour force"),
        F(r"\text{Unemployment rate} = \frac{\text{number unemployed}}{\text{labour force}} \times 100 \qquad \text{Participation rate} = \frac{\text{labour force}}{\text{working-age population}} \times 100",
          title="Two key rates"),
        T("Two methods are used. A **labour force survey** asks a sample of households about their activity (in Cameroon such surveys are run by the "
          "National Institute of Statistics, INS). A **claimant count** counts people receiving unemployment benefit; it only works where such benefits exist, "
          "which is not the case for most Cameroonian workers. Surveys can miss **discouraged workers** (who have stopped searching) and hide **underemployment**."),
        EX("Worked example 1: rates", intro="In a country (figures invented for practice) the working-age population is 16 million, 9.2 million people are employed and 0.8 million are unemployed. Calculate the unemployment rate and the participation rate.", steps=[
            S("Labour force", math=r"9.2 + 0.8 = 10 \text{ million}"),
            S("Unemployment rate", math=r"\frac{0.8}{10} \times 100 = 8\%"),
            S("Participation rate", math=r"\frac{10}{16} \times 100 = 62.5\%", text="Divide by the labour force, not by the working-age population, for the unemployment rate."),
        ], check=r"9.2 + 0.8 = 10"),
        H("Types of unemployment"),
        KEY("Types and causes", "Each type has a different cause, so it needs a different cure.", cards=[
            ["Frictional", "Workers between jobs or new entrants searching. Caused by imperfect information. Always present; short-term."],
            ["Structural", "A mismatch between workers' skills or location and the jobs available, often after a change in demand or technology (for example a decline in one crop or industry). Long-term."],
            ["Seasonal", "Work that rises and falls with the seasons: farm labour between harvests, tourism, construction in the rains."],
            ["Demand-deficient (cyclical, Keynesian)", "Aggregate demand is too low to employ the whole labour force, as in a recession. Linked to the deflationary gap."],
            ["Real-wage (classical)", "The real wage is held above the market-clearing level (by a minimum wage or union bargaining), so labour supplied exceeds labour demanded."],
        ]),
        IMG("alecu2-real-wage-unemployment.svg", alt="Labour market with downward-sloping labour demand DL and upward-sloping labour supply SL meeting at E with wage We and employment Le. A wage W1 above We gives demand L1 and supply L2; the gap L1 to L2 is labelled real-wage unemployment",
            caption="Figure 1. Real-wage (classical) unemployment: at W1, firms demand L1 workers but L2 offer themselves, so L2 minus L1 are unemployed."),
        T("Frictional and structural unemployment exist even when the labour market is in equilibrium. Together they make up the **natural rate of unemployment**: "
          "the rate that remains when aggregate demand is at its long-run level. Policies that raise demand cannot remove it; only supply-side measures can. "
          "You will meet this idea again as the NAIRU in the lesson on the Phillips curve."),
        D("**Underemployment**: people work fewer hours than they want, or in jobs below their qualifications, or earn very little. "
          "**Disguised unemployment**: more workers share a task than are needed, so the marginal product of the extra workers is close to zero (common in family farms). "
          "In developing economies these are often a larger problem than open unemployment.", title="Underemployment and disguised unemployment"),
        H("Costs and remedies"),
        T("Unemployment wastes output: the economy produces inside its production possibility curve. Government loses tax revenue and may spend more on support. "
          "The unemployed lose income and skills (the longer they wait, the less employable they become, called **hysteresis**). There are social costs too: poverty, "
          "migration pressures and crime. Some frictional unemployment can be useful, as it lets workers find jobs that match their skills."),
        KEY("Matching policy to type", "Diagnose the type first.", cards=[
            ["Demand-deficient", "Expansionary fiscal or monetary policy to raise aggregate demand (limits: inflation, the budget deficit, and for Cameroon monetary policy is set by BEAC for all of CEMAC)."],
            ["Structural", "Retraining, technical and vocational education, help to move, regional policy (supply-side; slow and costly)."],
            ["Frictional", "Better job information: employment agencies and job centres (in Cameroon the National Employment Fund, FNE, is one such body; check its current role)."],
            ["Real-wage", "Allow real wages to adjust or raise labour productivity; controversial because it affects low-paid workers."],
        ]),
        EX("Worked example 2: diagnosing the type (essay plan)", intro="Explain, with examples, why unemployment among university graduates in a developing country may be structural rather than demand-deficient.", steps=[
            S("Define both", text="Structural: a mismatch of skills or location with jobs. Demand-deficient: too little aggregate demand for the labour force."),
            S("Evidence for structural", text="Vacancies exist for technicians, engineers or nurses while graduates in other fields cannot find work; the gap persists in good years and bad years."),
            S("Cause", text="Courses do not match the needs of employers; the formal sector is small; workers cannot move easily to where jobs are."),
            S("Evaluate", text="Both types can co-exist: a fall in export prices may add cyclical unemployment on top. The remedy differs: training and reform of education, not just more spending."),
        ]),
        MISTAKE("Dividing by the population", "The unemployment rate divides the number unemployed by the labour force, not by the whole population or the working-age population."),
        MISTAKE("Listing types without causes", "Examiners reward the cause and the policy linked to each type. The Board's report notes that many candidates explain points in general terms when the question asks for a specific direction or context: say which type, why it arises, and what would reduce it."),
        QUIZ("A cocoa farm worker in the South Region has no paid work between harvests. Which type of unemployment is this?", ["Structural", "Seasonal", "Frictional", "Demand-deficient"], 1,
             "The work rises and falls with the farming calendar, so it is seasonal.", hint="Does the job come back at a fixed time of year?",
             feedback=["Structural unemployment is a lasting mismatch of skills or location, not a regular yearly pattern.", "", "Frictional unemployment is the time spent searching between jobs.", "Demand-deficient unemployment comes from low aggregate demand in a recession."]),
        QUIZ("A minimum wage is set above the equilibrium wage. In Figure 1, unemployment is measured by:", ["Le minus L1", "L2 minus Le", "L2 minus L1", "Le"], 2,
             "At W1 the quantity of labour supplied is L2 and demanded is L1, so the excess supply is L2 minus L1.", hint="Compare labour supplied and labour demanded at W1.",
             feedback=["That is the fall in employment only; it ignores the extra people attracted into the labour force.", "That is only the extra labour supplied.", "", "Le is equilibrium employment, not unemployment."]),
        TIP("Unemployment appears in Paper 1 (definitions and rate calculations), in Paper 2 macroeconomics essays (types, causes, costs and policies) and in Paper 3 data questions. When the question names Cameroon, apply each point to it.", title="Exam link"),
        PQ("A country's working-age population is 20 million. 11.4 million people are employed and 0.6 million are unemployed. Calculate (a) the labour force, (b) the unemployment rate, (c) the participation rate.",
           "(a) 11.4 + 0.6 = 12 million. (b) 0.6 ÷ 12 × 100 = 5%. (c) 12 ÷ 20 × 100 = 60%."),
        PQ("Distinguish between structural and frictional unemployment.",
           "Frictional unemployment is short-term unemployment while workers search between jobs or enter the labour market, caused by imperfect information, whereas structural unemployment is long-term unemployment caused by a mismatch between the skills or location of workers and the jobs available, often after a change in the structure of demand or technology."),
        PQ("Essay plan: 'Expansionary fiscal policy is the best way to reduce unemployment.' Discuss.",
           "Introduction: define unemployment and fiscal policy. For: when unemployment is demand-deficient, higher government spending or lower taxes raise aggregate demand, and the multiplier increases output and jobs (show the deflationary gap). Against: it does not cure frictional, structural or seasonal unemployment; it may cause inflation once the economy nears full employment; it raises the budget deficit and debt; there are time lags; in an open economy much of the extra demand leaks into imports. Evaluation: diagnose the type first; combine demand management with supply-side measures such as training. Conclusion: best only for cyclical unemployment."),
        SUM("Unemployed: of working age, without work, available and actively seeking work. Rate = unemployed ÷ labour force × 100.",
            "Types: frictional, structural, seasonal, demand-deficient (cyclical) and real-wage (classical).",
            "Frictional plus structural unemployment form the natural rate, which demand policies cannot remove.",
            "Underemployment and disguised unemployment are major problems in developing economies.",
            "Choose the remedy by type: demand management for cyclical, training and mobility for structural, information for frictional."),
    ],
))

# ------------------------------------------------------------------ 2. Inflation
LESSONS.append(lesson(
    module=M_PROB,
    topic="Inflation",
    title="Inflation: measurement, causes, effects and control",
    slug="ecu2-inflation",
    minutes=25,
    summary="How inflation is measured with a weighted consumer price index, the demand-pull, cost-push, monetarist and imported explanations shown on AD-AS diagrams, the effects of inflation and deflation, and the policies available inside the CEMAC monetary union.",
    objectives=[
        "Construct a weighted price index and calculate the rate of inflation and the change in real income",
        "Explain demand-pull and cost-push inflation using AD-AS diagrams, and state the monetarist and imported-inflation views",
        "Analyse the effects of inflation and deflation on different groups and on competitiveness",
        "Evaluate policies to control inflation, including the limits for a CEMAC member",
    ],
    key_concepts=["Inflation", "Consumer price index", "Weights", "Demand-pull inflation", "Cost-push inflation",
                  "Imported inflation", "Real income", "Deflation", "Wage-price spiral"],
    blocks=[
        H("Introduction"),
        T("When the price of a bag of rice, a litre of fuel and a taxi fare all rise in the same year, households in Douala and Garoua feel poorer even if their pay "
          "has not changed. **Inflation** is a sustained rise in the general price level, which is the same as a fall in the purchasing power of money. "
          "A single price rising is not inflation; the **average** of prices must keep rising. At A Level you must measure it, explain its causes with diagrams "
          "and judge the policies used to control it."),
        H("Measuring inflation: the consumer price index"),
        D("A **consumer price index (CPI)** measures the average price of a representative basket of goods and services bought by households, compared with a base year (index = 100). "
          "Each item has a **weight** that shows its share of household spending, found from household budget surveys.", title="Consumer price index"),
        F(r"\text{CPI} = \frac{\sum (\text{weight} \times \text{price index of item})}{\sum \text{weights}} \qquad \text{inflation rate} = \frac{\text{CPI}_{t} - \text{CPI}_{t-1}}{\text{CPI}_{t-1}} \times 100",
          title="Weighted index and inflation rate"),
        EX("Worked example 1: a weighted CPI", intro="A basket (invented for practice) has weights Food 50, Transport 20, Housing 20, Other 10. A year after the base year the price indices are Food 110, Transport 120, Housing 105, Other 100. Find the CPI and the inflation rate.", steps=[
            S("Multiply each index by its weight", math=r"50(110) + 20(120) + 20(105) + 10(100) = 5500 + 2400 + 2100 + 1000 = 11\,000"),
            S("Divide by the total weight", math=r"\text{CPI} = \frac{11\,000}{100} = 110"),
            S("Inflation rate", math=r"\frac{110 - 100}{100} \times 100 = 10\%", text="If next year the CPI is 115.5, inflation that year is (115.5 − 110) ÷ 110 × 100 = 5%: always divide by the previous year's index."),
        ], check=r"50 + 20 + 20 + 10 = 100"),
        T("Limits of the CPI: the basket and weights may be out of date; it misses changes in quality and new products; it measures an average household, "
          "not a farmer in the Far North or a civil servant in Yaounde; and informal-market prices are hard to collect."),
        F(r"\%\Delta \text{ real income} \approx \%\Delta \text{ money income} - \text{inflation rate}", title="Real income (approximation)"),
        EX("Worked example 2: real wages", intro="A worker's money wage rises by 6% while the CPI rises by 10%. What happens to her real wage?", steps=[
            S("Exact method", math=r"\frac{1.06}{1.10} = 0.9636"),
            S("Interpret", text="Her real wage falls by about 3.6% (the quick approximation 6 − 10 gives −4%). She can buy less than before."),
        ]),
        H("Causes of inflation"),
        IMG("alecu2-ad-as-inflation.svg", alt="Two AD-AS diagrams. Left, demand-pull: AD shifts right from AD1 to AD2 along SRAS, price level rises from P1 to P2 and real GDP from Y1 to Y2. Right, cost-push: SRAS shifts left from SRAS1 to SRAS2 along AD, price level rises from P1 to P2 and real GDP falls from Y1 to Y2",
            caption="Figure 1. Demand-pull inflation (left) and cost-push inflation (right)."),
        KEY("Four explanations", "Link each to a shift on the AD-AS diagram where you can.", cards=[
            ["Demand-pull", "Aggregate demand grows faster than the economy's capacity: high government spending, a credit boom, an export boom. AD shifts right; output rises at first, then mostly prices (the inflationary gap)."],
            ["Cost-push", "Higher costs of production: wages, fuel, imported inputs, indirect taxes. SRAS shifts left; prices rise while output falls (stagflation)."],
            ["Monetarist", "From the quantity theory MV = PT: if the money supply grows faster than output, the price level rises. 'Too much money chasing too few goods.' Associated with Milton Friedman."],
            ["Imported", "Higher world prices of imported goods (fuel, wheat, rice, fertiliser) or a fall in the exchange rate raise domestic prices. Important for an open economy like Cameroon's."],
        ]),
        T("Causes can feed each other. Higher prices lead workers to demand higher wages; higher wages raise costs and prices again. This is the **wage-price spiral**, "
          "and **expectations** keep it going: if everyone expects 10% inflation, they set wages and prices to match."),
        H("Effects of inflation"),
        KEY("Who gains and who loses", "Distinguish anticipated from unanticipated inflation.", cards=[
            ["Losers", "People on fixed incomes (some pensioners), savers when the interest rate is below inflation, lenders, and exporters whose prices become less competitive."],
            ["Gainers", "Borrowers (the real value of debt falls), and governments with large debts. Firms may gain if prices rise faster than costs."],
            ["Costs to the economy", "Shoe-leather costs (holding less cash), menu costs (changing prices), uncertainty that discourages investment, arbitrary redistribution, and loss of international competitiveness under a fixed exchange rate."],
        ]),
        T("**Deflation** is a sustained fall in the general price level. It can be harmful: consumers delay purchases expecting lower prices, the real burden of debt rises, "
          "and firms cut output and jobs. A fall in prices caused by higher productivity (benign deflation) is less harmful than one caused by falling demand."),
        H("Controlling inflation"),
        T("**Monetary policy**: higher interest rates and tighter credit reduce demand and money growth. In Cameroon this is decided by the Bank of Central African States (BEAC) "
          "for all six CEMAC countries, and the fixed peg of the CFA franc to the euro anchors prices; BEAC's main objective is price stability (check your textbook for its current inflation target). "
          "**Fiscal policy**: lower government spending or higher taxes reduce demand. **Supply-side policies** raise capacity and productivity, the long-run cure for cost-push pressures. "
          "**Prices and incomes policies**: price controls or wage limits act quickly but cause shortages and black markets if kept for long."),
        MISTAKE("Calling one price rise inflation", "A rise in the price of fuel alone is a relative price change. It becomes inflation only if the general price level keeps rising."),
        MISTAKE("Dividing by the wrong year", "The rate of inflation divides the change in the index by the earlier year's index, not by 100 (unless the earlier year is the base year)."),
        QUIZ("A sharp rise in world oil prices raises transport and production costs in Cameroon. On an AD-AS diagram, this is shown by:", ["AD shifting right", "SRAS shifting left", "LRAS shifting right", "AD shifting left"], 1,
             "Higher costs at every level of output shift short-run aggregate supply to the left: cost-push inflation, with lower output.", hint="Is this a change in spending or in costs?",
             feedback=["An AD shift shows a change in spending (demand-pull).", "", "LRAS shifts right when capacity grows, which lowers prices.", "A fall in AD would lower prices."]),
        QUIZ("A CPI rises from 120 to 126. The inflation rate is:", ["6%", "5%", "26%", "4.8%"], 1,
             "(126 − 120) ÷ 120 × 100 = 5%.", hint="Divide the change by the earlier index.",
             feedback=["6 is the change in index points, not a percentage of 120.", "", "That compares 126 with the base of 100.", "That divides the change by 126, the later index."]),
        TIP("Inflation is a regular Paper 2 macroeconomics essay topic (causes with diagrams, effects, control) and appears in Paper 1 and Paper 3 as index calculations. Draw the AD-AS diagram for each cause, label axes and both equilibria, and explain in the direction the question asks.", title="Exam link"),
        PQ("Weights: food 40, clothing 10, transport 30, other 20. Price indices: food 115, clothing 102, transport 110, other 105. Calculate the CPI.",
           "40 × 115 = 4600; 10 × 102 = 1020; 30 × 110 = 3300; 20 × 105 = 2100. Total = 11 020. CPI = 11 020 ÷ 100 = 110.2. Prices have risen 10.2% since the base year."),
        PQ("Distinguish between demand-pull and cost-push inflation, with a diagram for each.",
           "Demand-pull inflation is caused by aggregate demand rising faster than capacity, shown by AD shifting right along SRAS so that both the price level and output rise, whereas cost-push inflation is caused by rising costs of production, shown by SRAS shifting left along AD so that the price level rises while output falls. Each diagram needs axes (price level, real GDP), the curves before and after, and P1, P2, Y1, Y2 marked."),
        PQ("Essay plan: Discuss the view that inflation always harms an economy.",
           "Define inflation. Harms: lower purchasing power of fixed incomes; savers and lenders lose; menu and shoe-leather costs; uncertainty reduces investment; under the CFA franc's fixed peg, higher inflation than in trading partners makes exports less competitive and worsens the current account. But: mild, stable and anticipated inflation does little harm and may ease adjustment of relative wages; borrowers gain; deflation can be worse. Evaluation: the harm depends on the rate, whether it is anticipated and whether it is above that of trading partners. Conclusion: high or unstable inflation harms; low stable inflation need not."),
        SUM("Inflation is a sustained rise in the general price level, measured with a weighted CPI.",
            "Inflation rate = change in CPI ÷ previous CPI × 100; real income falls if prices rise faster than money income.",
            "Causes: demand-pull (AD right), cost-push (SRAS left), monetary growth (MV = PT) and imported inflation.",
            "Effects fall unevenly: fixed-income earners, savers and exporters lose; borrowers may gain.",
            "Control: monetary policy (set by BEAC for CEMAC), fiscal restraint, supply-side measures and, briefly, price controls."),
    ],
))

# ------------------------------------------------------------------ 3. The Phillips curve
LESSONS.append(lesson(
    module=M_PROB,
    topic="The Phillips curve",
    title="The Phillips curve: short-run trade-off, expectations and the NAIRU",
    slug="ecu2-phillips-curve",
    minutes=23,
    summary="The original Phillips curve trade-off between unemployment and inflation, why it broke down in the stagflation of the 1970s, the expectations-augmented short-run curves, the vertical long-run Phillips curve at the NAIRU, and what this means for policy.",
    objectives=[
        "Describe the original Phillips curve and explain the trade-off it suggests",
        "Explain, with a diagram, how expectations shift the short-run Phillips curve and why the long-run curve is vertical",
        "Define the NAIRU and calculate inflation from a simple expectations-augmented equation",
        "Evaluate the policy implications of the Phillips curve debate",
    ],
    key_concepts=["Phillips curve", "Trade-off", "Stagflation", "Adaptive expectations", "Short-run Phillips curve",
                  "Long-run Phillips curve", "NAIRU", "Natural rate of unemployment"],
    blocks=[
        H("Introduction"),
        T("Can a government buy lower unemployment by accepting a little more inflation? In the 1960s many economists said yes. In the 1970s, many countries had "
          "**both** high inflation and high unemployment, and the answer changed. The Phillips curve is the tool that tells this story, and it links your lessons "
          "on unemployment and inflation."),
        H("The original Phillips curve"),
        D("The **Phillips curve** shows an inverse relationship between the rate of unemployment and the rate of inflation. "
          "It is named after A. W. Phillips, who in 1958 published a study of UK data showing that money-wage inflation was high when unemployment was low. "
          "Later economists restated it with price inflation.", title="Phillips curve"),
        T("The reasoning: when unemployment is low, the labour market is tight; firms compete for workers, wages rise faster, and firms pass higher costs on as higher prices. "
          "When unemployment is high, wage growth slows. This suggested a **menu of choices**: a government could choose a point on the curve, trading lower unemployment "
          "for higher inflation."),
        H("Breakdown and the expectations-augmented curve"),
        T("In the 1970s, oil price shocks and rising inflation expectations produced **stagflation**: rising inflation together with rising unemployment. "
          "This does not fit a single stable curve. Milton Friedman and Edmund Phelps had argued that workers bargain over **real** wages, so the curve depends on the "
          "inflation they **expect**. With **adaptive expectations**, people expect inflation to be what it was recently."),
        IMG("alecu2-phillips.svg", alt="Inflation against unemployment: vertical LRPC at 5% unemployment; downward-sloping SRPC1 and a higher SRPC2. A (5%, 2%) and B (3%, 6%) lie on SRPC1; C (5%, 6%) lies on SRPC2",
            caption="Figure 1. Short-run Phillips curves (one for each expected inflation rate) and the vertical long-run Phillips curve at the NAIRU (teaching values)."),
        KEY("The A-B-C story", "Follow Figure 1.", cards=[
            ["A", "The economy is at the natural rate (5%) with 2% inflation, which everyone expects."],
            ["A to B", "The government expands demand. Firms raise prices and hire more; workers, still expecting 2%, accept jobs at money wages that are really lower. Unemployment falls to 3%, inflation rises to 6%."],
            ["B to C", "Workers learn that inflation is 6% and demand higher money wages. Real wages return to normal, firms cut back hiring, and unemployment returns to 5%. Expected inflation is now 6%: the economy is on SRPC2."],
            ["Result", "In the long run unemployment is back at the natural rate but inflation is higher. The long-run Phillips curve (LRPC) is vertical."],
        ]),
        D("The **NAIRU** (non-accelerating inflation rate of unemployment) is the rate of unemployment at which inflation is stable, because actual and expected inflation are equal. "
          "Pushing unemployment below it makes inflation accelerate. It is closely linked to the natural rate of unemployment (frictional plus structural); some textbooks treat the two terms as the same (check your textbook).", title="NAIRU"),
        F(r"\pi = \pi^{e} - \beta(U - U^{*})", title="Expectations-augmented Phillips curve (simple linear form)"),
        T(r"Here $\pi$ is actual inflation, $\pi^{e}$ expected inflation, $U$ the unemployment rate, $U^{*}$ the NAIRU and $\beta$ a positive number showing how strongly inflation responds. "
          r"When $U = U^{*}$, $\pi = \pi^{e}$: inflation is stable."),
        EX("Worked example 1: using the equation", intro=r"Take $\pi = \pi^{e} - 2(U - 5)$. Expected inflation is 2%. (a) Find inflation if unemployment is pushed to 3%. (b) Next year expected inflation adapts to last year's actual rate. What inflation is needed to keep unemployment at 3%?", steps=[
            S("(a) Substitute", math=r"\pi = 2 - 2(3 - 5) = 2 + 4 = 6\%"),
            S("(b) New expectation", text="Expected inflation is now 6%."),
            S("Substitute again", math=r"\pi = 6 - 2(3 - 5) = 6 + 4 = 10\%", text="Holding unemployment below the NAIRU requires ever-rising inflation: inflation accelerates."),
        ], check=r"U = 5 \Rightarrow \pi = \pi^{e}"),
        EX("Worked example 2: reducing inflation (disinflation)", intro=r"With the same equation, expected inflation is 6% and the government wants inflation of 2% next year. What unemployment rate does this need in the short run?", steps=[
            S("Set up", math=r"2 = 6 - 2(U - 5)"),
            S("Solve", math=r"2(U - 5) = 4 \Rightarrow U = 7\%"),
            S("Interpret", text="Unemployment must rise above the NAIRU for a time: this is the short-run cost of reducing inflation, until expectations fall."),
        ], check=r"6 - 2(7 - 5) = 2"),
        H("Policy implications and evaluation"),
        T("If the LRPC is vertical, demand management can only reduce unemployment temporarily; the lasting way to lower unemployment is to reduce the NAIRU with "
          "**supply-side policies** (training, better job information, flexible labour markets). With **rational expectations** (the new classical view), people "
          "anticipate policy, so even the short-run trade-off may vanish if policy is credible. Keynesians reply that wages are sticky and that long spells of "
          "unemployment can raise the NAIRU itself (hysteresis), so the trade-off may last longer."),
        T("Applying it to Cameroon needs care: a large informal sector and underemployment make the unemployment rate a weak measure of labour-market pressure, and much inflation "
          "is imported or caused by supply shocks to food. The fixed peg to the euro also anchors expectations."),
        MISTAKE("Drawing the LRPC at zero unemployment", "The long-run curve is vertical at the NAIRU (natural rate), which is positive, not at zero unemployment."),
        MISTAKE("Calling stagflation a movement along one curve", "Stagflation (higher inflation and higher unemployment together) is shown by the short-run curve shifting upwards or by a supply shock, not by a movement along a single curve."),
        QUIZ("In Figure 1, which move shows the long-run result of an attempt to hold unemployment below the NAIRU?", ["A to B", "B to C", "C to A", "B to A"], 1,
             "As expectations adjust, the economy moves from B to C: unemployment returns to the NAIRU at higher inflation.", hint="What happens once workers expect the higher inflation?",
             feedback=["A to B is the short-run effect of the demand expansion.", "", "C to A would need expected inflation to fall, for example after a period of higher unemployment.", "B to A would mean inflation falls while unemployment rises along the same short-run curve; that is not what expectations do."]),
        QUIZ(r"With $\pi = 4 - 0.5(U - 6)$, at what unemployment rate is inflation stable at the expected rate?", ["4%", "6%", "0.5%", "10%"], 1,
             "Inflation equals expected inflation when U = U* = 6%.", hint="When does the bracket equal zero?",
             feedback=["4 is the expected inflation rate, not the unemployment rate.", "", "0.5 is the slope coefficient.", "10 is 4 + 6, which has no meaning here."]),
        TIP("The Phillips curve is a favourite for Paper 1 (reading points on the diagram) and for Paper 2 essays that ask whether governments face a trade-off. Draw SRPCs and the vertical LRPC, label the NAIRU, and evaluate with expectations and supply-side policy.", title="Exam link"),
        PQ(r"Using $\pi = 3 - 1.5(U - 6)$: (a) calculate inflation when U = 4%; (b) state the NAIRU.",
           r"(a) $\pi = 3 - 1.5(4 - 6) = 3 + 3 = 6\%$. (b) The NAIRU is 6%, where actual inflation equals the expected 3%."),
        PQ("Explain why the long-run Phillips curve is vertical according to the expectations-augmented view.",
           "Any fall in unemployment below the natural rate happens only because workers underestimate inflation and accept lower real wages. Once expectations adjust, workers demand higher money wages, real wages return to their equilibrium level, and unemployment returns to the natural rate at a higher rate of inflation. Since this happens at every expected inflation rate, the long-run relationship is a vertical line at the NAIRU: there is no long-run trade-off."),
        PQ("Essay plan: 'There is a trade-off between unemployment and inflation.' Discuss.",
           "Define both and draw the original Phillips curve; explain the wage-bargaining logic. For: short-run evidence of an inverse relationship; demand expansion lowers unemployment at the cost of inflation. Against: stagflation in the 1970s; the expectations-augmented model gives a vertical LRPC at the NAIRU; rational expectations may remove even the short-run trade-off; supply shocks move inflation and unemployment in the same direction. Evaluation: a short-run trade-off may exist while wages are sticky; in the long run lower unemployment needs supply-side policy. Conclusion: a short-run, not a long-run, trade-off."),
        SUM("The original Phillips curve showed lower unemployment with higher inflation, suggesting a policy trade-off.",
            "Stagflation in the 1970s broke the simple curve; expectations shift the short-run curve.",
            "With adaptive expectations, unemployment returns to the NAIRU and the long-run Phillips curve is vertical.",
            "π = πᵉ − β(U − U*): holding U below U* makes inflation accelerate.",
            "Lasting falls in unemployment need lower NAIRU through supply-side policies."),
    ],
))

# ------------------------------------------------------------------ 4. The trade cycle
LESSONS.append(lesson(
    module=M_PROB,
    topic="The trade cycle",
    title="The trade cycle: phases, output gaps and the multiplier-accelerator",
    slug="ecu2-trade-cycle",
    minutes=24,
    summary="The phases of the trade (business) cycle around trend growth, how to measure growth rates and output gaps, the causes of cycles including the multiplier-accelerator interaction, external shocks to commodity exporters, and the role of stabilisation policy.",
    objectives=[
        "Describe the four phases of the trade cycle and the behaviour of key indicators in each",
        "Calculate growth rates and output gaps and interpret them",
        "Explain the multiplier-accelerator theory of the cycle with a numerical sequence",
        "Evaluate other causes of cycles and the use of stabilisation policy, with reference to a commodity exporter",
    ],
    key_concepts=["Trade cycle", "Boom", "Recession", "Trough", "Recovery", "Trend growth", "Output gap",
                  "Multiplier-accelerator", "Automatic stabilisers"],
    blocks=[
        H("Introduction"),
        T("Economies do not grow smoothly. Output and employment rise fast for some years, then slow or fall, then recover. For Cameroon, swings in the world prices of "
          "oil, cocoa, coffee and timber have often set this rhythm. The **trade cycle** (business cycle) describes these fluctuations of real GDP around its long-run trend."),
        H("Phases of the cycle"),
        IMG("alecu2-trade-cycle.svg", alt="Actual real GDP drawn as a wave around a rising dashed trend line. The wave is labelled peak (boom), recession, trough (slump) and recovery; a positive output gap is marked above the trend at the second peak and a negative output gap below the trend at the trough",
            caption="Figure 1. The trade cycle: actual GDP fluctuates around trend (potential) GDP."),
        KEY("The four phases", "Learn what happens to output, jobs, prices and the budget in each.", cards=[
            ["Boom (peak)", "Output above trend (positive output gap), low unemployment, rising inflation, rising imports, high profits and tax revenue. Bottlenecks appear."],
            ["Recession", "Output growth turns negative; a common convention is two consecutive quarters of falling real GDP (check your textbook). Unemployment rises, investment falls sharply."],
            ["Trough (slump or depression)", "The lowest point: large negative output gap, high unemployment, low inflation or falling prices, low business confidence."],
            ["Recovery", "Output grows again, unemployment begins to fall, confidence and investment return."],
        ]),
        D("**Trend (potential) growth** is the long-run rate at which the productive capacity of the economy grows. The **output gap** is the difference between actual and potential output. "
          "A **positive** gap (actual above potential) brings inflationary pressure; a **negative** gap (actual below potential) means unemployed resources.", title="Trend growth and the output gap"),
        F(r"\text{growth rate} = \frac{Y_t - Y_{t-1}}{Y_{t-1}} \times 100 \qquad \text{output gap (\% of potential)} = \frac{Y_{\text{actual}} - Y_{\text{potential}}}{Y_{\text{potential}}} \times 100", title="Measuring the cycle"),
        EX("Worked example 1: growth and the output gap", intro="Real GDP (invented, in billions of FCFA) was 10 000 last year and 10 350 this year. Potential GDP this year is estimated at 10 800. Find the growth rate and the output gap.", steps=[
            S("Growth rate", math=r"\frac{10\,350 - 10\,000}{10\,000} \times 100 = 3.5\%"),
            S("Output gap", math=r"\frac{10\,350 - 10\,800}{10\,800} \times 100 = -4.2\%", text="A negative gap: the economy is producing below capacity even though it is growing."),
        ]),
        H("Why do cycles happen? The multiplier-accelerator"),
        T("The **multiplier** says a change in investment causes a larger change in income. The **accelerator** says investment depends on the **change** in output (or consumption): "
          "firms add capacity only while demand is growing. Paul Samuelson showed that when the two interact, a single rise in spending can make income rise, overshoot, "
          "and fall back in waves."),
        F(r"Y_t = C_t + I_t + G \qquad C_t = c\,Y_{t-1} \qquad I_t = v\,(C_t - C_{t-1})", title="A simple Samuelson model"),
        EX("Worked example 2: a multiplier-accelerator sequence", intro=r"Take $c = 0.5$ and $v = 1$. The economy is in equilibrium with $G = 100$, $Y = 200$, $C = 100$, $I = 0$. In period 2, $G$ rises permanently to 110. Trace income.", steps=[
            S("Period 2", math=r"C_2 = 0.5(200) = 100,\; I_2 = 1(100 - 100) = 0,\; Y_2 = 100 + 0 + 110 = 210"),
            S("Period 3", math=r"C_3 = 0.5(210) = 105,\; I_3 = 105 - 100 = 5,\; Y_3 = 105 + 5 + 110 = 220"),
            S("Period 4", math=r"C_4 = 110,\; I_4 = 5,\; Y_4 = 225"),
            S("Periods 5 to 7", text="Y = 225, then 222.5, then 220: consumption stops rising, induced investment falls to zero and then turns negative, so income falls back."),
            S("Long run", math=r"Y^{*} = \frac{G}{1 - c} = \frac{110}{0.5} = 220", text="Income overshoots to 225 and oscillates towards 220: a damped cycle. With larger values of v the waves can be bigger or even grow."),
        ], check=r"220 = 110 + 0.5(220) + 0"),
        CODE("Period   G     C       I      Y\n"
             "  1     100   100     0      200\n"
             "  2     110   100     0      210\n"
             "  3     110   105     5      220\n"
             "  4     110   110     5      225\n"
             "  5     110   112.5   2.5    225\n"
             "  6     110   112.5   0      222.5\n"
             "  7     110   111.25 -1.25   220\n"
             "  8     110   110    -1.25   218.75", "text", title="Table 1. The sequence in Worked example 2"),
        KEY("Other causes of cycles", "Use several in an essay and evaluate them.", cards=[
            ["Stock (inventory) cycle", "Firms build up stocks when sales rise and run them down when sales fall, magnifying swings."],
            ["Monetary and credit causes", "Easy credit fuels booms; tight credit or banking crises deepen recessions."],
            ["External shocks", "For commodity exporters such as Cameroon, falls in the world prices of oil or cocoa reduce export income, government revenue and demand (the crisis of the mid-1980s is the classic Cameroonian example)."],
            ["Expectations and confidence", "Keynes's 'animal spirits': waves of optimism and pessimism change investment."],
            ["Political cycle", "Governments may expand spending before elections and tighten afterwards (a theory, not a proven rule)."],
            ["Real business cycle", "New classical economists stress supply shocks such as technology or harvests."],
        ]),
        H("Stabilisation policy"),
        T("**Automatic stabilisers** (tax revenue that rises in booms and falls in slumps, and spending on support that does the reverse) smooth the cycle without any decision. "
          "**Discretionary** fiscal and monetary policy can lean against the wind, but time lags, poor forecasts and, for CEMAC members, a common monetary policy limit their power. "
          "Commodity exporters can also save revenue in good years to spend in bad years."),
        MISTAKE("Saying a recession means negative GDP", "A recession is a period of falling real GDP. GDP itself stays positive; it is the growth rate that becomes negative."),
        MISTAKE("Forgetting that the accelerator uses changes", "Induced investment depends on the change in output or consumption, not its level. Investment can fall even while output is still rising, if output rises more slowly."),
        QUIZ("Which feature is typical of the boom phase?", ["Large negative output gap", "Falling inflation and rising unemployment", "Positive output gap and rising inflation", "Low business confidence"], 2,
             "In a boom actual output exceeds potential, labour is scarce and inflation rises.", hint="Is output above or below trend at the peak?",
             feedback=["A negative gap belongs to the trough.", "This describes a recession.", "", "Confidence is high in a boom."]),
        QUIZ("Under the accelerator principle, investment falls when:", ["Output falls", "The rate of growth of output slows down", "Output stays at a high level", "All of these"], 3,
             "Induced investment depends on the change in output: it falls whenever the change becomes smaller, including when output stops rising or falls.", hint="Investment depends on the change in output.",
             feedback=["This is one case, but not the only one.", "This is one case, but not the only one.", "This is one case (a constant level gives zero induced investment), but not the only one.", ""]),
        TIP("The trade cycle appears in Paper 1 (phases, output gap, accelerator) and in Paper 2 essays on causes and stabilisation. In an essay, draw the cycle around a trend line and explain at least two causes before evaluating policy.", title="Exam link"),
        PQ("Real GDP rose from 8 000 to 8 160 billion FCFA (invented). Potential GDP is 8 000. Calculate the growth rate and the output gap, and state what the gap suggests.",
           "Growth = (8 160 − 8 000) ÷ 8 000 × 100 = 2%. Output gap = (8 160 − 8 000) ÷ 8 000 × 100 = +2%. A positive gap suggests demand is above capacity, so inflationary pressure is likely."),
        PQ("Explain how the multiplier and the accelerator interact to produce a trade cycle.",
           "A rise in spending raises income by a multiple through the multiplier. Higher income raises consumption; because consumption is growing, firms invest to add capacity (accelerator), which raises income further. When the growth of consumption slows, induced investment falls, and through the multiplier income falls. Falling income reduces consumption and investment further until replacement needs and autonomous spending start a recovery. The interaction creates turning points and waves."),
        PQ("Essay plan: Discuss the causes of trade cycles in an economy that depends on primary exports.",
           "Define the cycle and phases (diagram). Causes: external shocks to commodity prices and volumes (main for a primary exporter; effects through export income, government revenue and the multiplier); multiplier-accelerator; credit conditions; weather and harvests (supply shocks); confidence. Evaluation: external shocks are likely to dominate; domestic policy can soften them through saving in booms, diversification and automatic stabilisers; within CEMAC the exchange rate cannot adjust, so fiscal policy carries more weight. Conclusion."),
        SUM("The trade cycle is the fluctuation of real GDP around its trend: boom, recession, trough, recovery.",
            "Growth rate = change ÷ previous value × 100; the output gap compares actual with potential output.",
            "The multiplier-accelerator interaction can turn one shock into waves of income.",
            "Other causes: stocks, credit, confidence, politics, supply and external commodity-price shocks.",
            "Automatic stabilisers and discretionary policy can smooth the cycle, with lags and limits."),
    ],
))

# ------------------------------------------------------------------ 5. Supply-side policies
LESSONS.append(lesson(
    module=M_PROB,
    topic="Supply-side policies",
    title="Supply-side policies: raising productive capacity",
    slug="ecu2-supply-side-policies",
    minutes=22,
    summary="What supply-side policies are, the difference between market-based and interventionist measures, how they shift long-run aggregate supply and lower the natural rate of unemployment, examples relevant to Cameroon, and their strengths and limits.",
    objectives=[
        "Define supply-side policies and show their effect with an LRAS diagram",
        "Distinguish market-based from interventionist supply-side policies with examples",
        "Calculate changes in labour productivity and link them to growth and costs",
        "Evaluate supply-side policies: time lags, cost, equity and effectiveness",
    ],
    key_concepts=["Supply-side policy", "Long-run aggregate supply", "Productivity", "Market-based policy",
                  "Interventionist policy", "Deregulation", "Human capital", "Infrastructure"],
    blocks=[
        H("Introduction"),
        T("Demand-side policies change how much people spend. **Supply-side policies** change how much the economy **can** produce. "
          "When a new port, a hydroelectric dam or a technical college raises the productive capacity of Cameroon, the country can grow faster without inflation. "
          "This lesson brings together ideas from the lessons on unemployment, inflation and the Phillips curve: supply-side policies are the long-run cure for all three."),
        D("**Supply-side policies** are government measures that aim to increase the productive capacity of the economy (aggregate supply) by improving the quantity, quality "
          "and efficiency of the factors of production and the working of markets.", title="Supply-side policies"),
        IMG("alecu2-lras-shift.svg", alt="AD-AS diagram with a downward-sloping AD curve and two vertical long-run aggregate supply curves; LRAS shifts right from LRAS1 to LRAS2, so the price level falls from P1 to P2 and real GDP rises from Y1 to Y2",
            caption="Figure 1. A successful supply-side policy shifts LRAS to the right: more output at a lower price level."),
        T("Figure 1 shows why supply-side policies are attractive: unlike a rise in AD, a rise in LRAS increases real GDP and **reduces** inflationary pressure. "
          "In the labour market they reduce frictional and structural unemployment, lowering the natural rate (NAIRU), and they improve international competitiveness."),
        H("Two families of policy"),
        KEY("Market-based (free-market) policies", "Make markets work better by reducing government interference.", cards=[
            ["Tax reform", "Lower income and profit taxes to raise incentives to work, save and invest (see the Laffer curve in the taxation lesson)."],
            ["Privatisation and deregulation", "Sell state firms or open markets to competition to raise efficiency."],
            ["Labour-market reform", "Make hiring easier and wages more flexible; reform benefits so that work pays."],
            ["Trade liberalisation", "Lower tariffs to expose firms to competition and cheaper inputs."],
        ]),
        KEY("Interventionist policies", "The state invests where markets under-provide.", cards=[
            ["Education and training", "Raise human capital: technical and vocational education, apprenticeships, university courses matched to employers' needs."],
            ["Infrastructure", "Roads, ports, power and telecommunications cut costs for all firms (examples in Cameroon include the Kribi deep-sea port and hydroelectric projects such as Lom Pangar)."],
            ["Research and industrial policy", "Support for research, new industries and small firms; credit for agriculture."],
            ["Health", "A healthier workforce is more productive and works longer."],
        ]),
        T("Improving the **business environment** is a supply-side policy too: faster business registration, reliable courts, less corruption and simpler taxes lower the cost "
          "of producing. Cameroon has set up one-stop shops for creating businesses (check the current procedures). Many of these aims appear in the National Development "
          "Strategy 2020-2030 (NDS30), covered in the lesson on the Cameroonian economy."),
        F(r"\text{labour productivity} = \frac{\text{output}}{\text{number of workers (or hours worked)}}", title="Labour productivity"),
        EX("Worked example 1: productivity", intro="A cassava-processing cooperative (figures invented) produced output worth 20 million FCFA with 10 workers. After a training programme and new grating machines it produces 26.4 million FCFA with 12 workers. Calculate the change in labour productivity.", steps=[
            S("Before", math=r"\frac{20}{10} = 2.0 \text{ million FCFA per worker}"),
            S("After", math=r"\frac{26.4}{12} = 2.2 \text{ million FCFA per worker}"),
            S("Percentage change", math=r"\frac{2.2 - 2.0}{2.0} \times 100 = 10\%", text="Higher productivity lowers unit labour costs if wages do not rise as fast, so prices can be more competitive."),
        ], check=r"2.2 \times 12 = 26.4"),
        EX("Worked example 2: evaluating a policy (plan)", intro="Evaluate a large public programme of technical and vocational training as a way to reduce unemployment in Cameroon.", steps=[
            S("Mechanism", text="Training gives skills that employers want, reducing structural unemployment and raising productivity, so LRAS shifts right."),
            S("Strengths", text="Attacks the cause of skill mismatch; lasting effect; also raises incomes and can attract investment."),
            S("Limits", text="Long time lag; costly for the budget; courses may still not match jobs; trained workers may emigrate; if demand is weak, there may be no jobs to fill."),
            S("Judgement", text="Most effective combined with infrastructure and a better business climate, and with enough aggregate demand for the extra capacity to be used."),
        ]),
        H("Evaluation"),
        T("Supply-side policies take years to work and are hard to measure. Interventionist measures cost public money and depend on good management. Market-based measures "
          "can increase inequality (tax cuts for high earners, weaker job security) and their incentive effects may be small. Supply-side policies do little in a recession "
          "caused by low demand: capacity is not the problem then. Most economists see demand-side and supply-side policies as complements."),
        MISTAKE("Calling any spending a supply-side policy", "Government spending is supply-side only if it raises productive capacity (for example roads, training, health). Spending on current consumption raises AD, not LRAS."),
        MISTAKE("Drawing the shift on AD", "Show supply-side policy as a rightward shift of LRAS (or of the vertical part of a Keynesian AS curve), not as a shift of AD."),
        QUIZ("Which is an interventionist supply-side policy?", ["Cutting the top rate of income tax", "Selling a state telecommunications firm", "Building technical colleges", "Reducing employment protection laws"], 2,
             "The state invests directly in human capital, which is interventionist.", hint="Which option has the state doing more, not less?",
             feedback=["A tax cut is a market-based (incentive) policy.", "Privatisation is market-based.", "", "Labour-market deregulation is market-based."]),
        QUIZ("A successful supply-side policy is shown by:", ["AD shifting right, raising the price level", "LRAS shifting right, raising output and easing inflation", "SRAS shifting left", "AD shifting left"], 1,
             "Higher capacity shifts LRAS right: more output and downward pressure on prices.", hint="Supply-side means the supply curve.",
             feedback=["That is a demand-side expansion.", "", "A leftward SRAS shift is a cost shock.", "That is a contraction of demand."]),
        TIP("Supply-side policies appear in Paper 2 essays (often as the evaluation of demand policies, or as 'policies to reduce unemployment or promote growth') and in Paper 3 questions on Cameroon's development. Always give the mechanism, a diagram and an evaluation.", title="Exam link"),
        PQ("A factory's output rises from 400 to 450 units a day while its workforce stays at 50. Calculate the percentage change in labour productivity.",
           "Before: 400 ÷ 50 = 8 units per worker. After: 450 ÷ 50 = 9 units per worker. Change: (9 − 8) ÷ 8 × 100 = 12.5%."),
        PQ("Give two market-based and two interventionist supply-side policies, and explain how one of them increases aggregate supply.",
           "Market-based: lower income or profit taxes; privatisation; deregulation; labour-market flexibility. Interventionist: education and training; infrastructure; health spending; research subsidies. Example: better roads lower transport costs and journey times for every firm, so firms can produce and deliver more with the same resources; productive capacity rises and LRAS shifts right."),
        PQ("Essay plan: 'Supply-side policies are better than demand-side policies for reducing inflation and unemployment together.' Discuss.",
           "Define both. For: LRAS shift raises output and lowers price pressure together; lowers the NAIRU; improves competitiveness under a fixed exchange rate. Against: long lags; costs; may raise inequality; ineffective when unemployment is demand-deficient; uncertain results. Demand-side policies act faster on cyclical unemployment but trade off with inflation. Conclusion: supply-side policies are better for long-run problems; both are needed in practice."),
        SUM("Supply-side policies raise productive capacity: LRAS shifts right, raising output and easing inflation.",
            "Market-based: tax incentives, privatisation, deregulation, flexible labour markets, trade liberalisation.",
            "Interventionist: education, training, infrastructure, health and research.",
            "Labour productivity = output ÷ workers; higher productivity lowers unit costs.",
            "Limits: time lags, cost, equity concerns and little effect when demand is the problem."),
    ],
))

# ------------------------------------------------------------------ 6. The theory of international trade
LESSONS.append(lesson(
    module=M_INT,
    topic="The theory of international trade",
    title="Absolute and comparative advantage and the gains from trade",
    slug="ecu2-comparative-advantage",
    minutes=25,
    summary="Why countries trade: absolute and comparative advantage measured by opportunity cost, the gains from specialisation, the limits for the terms of trade, the Heckscher-Ohlin explanation, the assumptions and limits of the theory, and the arguments for protection.",
    objectives=[
        "Distinguish absolute from comparative advantage and identify each from production data",
        "Calculate opportunity cost ratios, the gains from specialisation and the range of mutually beneficial terms of trade",
        "Explain the Heckscher-Ohlin factor-endowment theory and apply it to Cameroon",
        "Evaluate the theory's assumptions and the arguments for and against protection",
    ],
    key_concepts=["Absolute advantage", "Comparative advantage", "Opportunity cost", "Specialisation", "Gains from trade",
                  "Terms of trade limits", "Factor endowments", "Protectionism"],
    blocks=[
        H("Introduction"),
        T("Cameroon exports cocoa, coffee, timber, bananas, cotton and crude oil, and imports machinery, vehicles, rice, wheat and medicines. Why not produce everything at home? "
          "The theory of international trade explains why countries gain by **specialising** and exchanging, even when one country is better at producing everything."),
        H("Absolute and comparative advantage"),
        D("A country has an **absolute advantage** in a good if it can produce more of it than another country with the same resources (Adam Smith). "
          "A country has a **comparative advantage** in a good if it can produce it at a **lower opportunity cost** than another country (David Ricardo).", title="Two kinds of advantage"),
        T("The key insight of Ricardo's **law of comparative advantage**: trade benefits both countries as long as their opportunity costs differ, even if one has an absolute advantage in both goods."),
        IMG("alecu2-comparative-ppf.svg", alt="Two straight-line production possibility frontiers with cocoa in tonnes on the horizontal axis and cloth in thousand metres on the vertical axis. Cameroon's runs from 45 cloth to 60 cocoa; Northland's runs from 30 cloth to 20 cocoa",
            caption="Figure 1. Production possibility frontiers (constant opportunity cost; figures invented for practice)."),
        CODE("               Cocoa (tonnes)   Cloth (thousand m)\n"
             "Cameroon             60                 45\n"
             "Northland            20                 30", "text", title="Table 1. Maximum output if all resources go into one good"),
        EX("Worked example 1: who has which advantage?", intro="Use Table 1. Identify absolute and comparative advantage.", steps=[
            S("Absolute advantage", text="Cameroon can produce more of both goods (60 > 20, 45 > 30): it has an absolute advantage in both."),
            S("Opportunity cost of 1 tonne of cocoa", math=r"\text{Cameroon: } \tfrac{45}{60} = 0.75 \text{ cloth} \qquad \text{Northland: } \tfrac{30}{20} = 1.5 \text{ cloth}"),
            S("Opportunity cost of 1 unit of cloth", math=r"\text{Cameroon: } \tfrac{60}{45} = 1.33 \text{ cocoa} \qquad \text{Northland: } \tfrac{20}{30} = 0.67 \text{ cocoa}"),
            S("Conclusion", text="Cameroon has the comparative advantage in cocoa (0.75 < 1.5); Northland has the comparative advantage in cloth (0.67 < 1.33)."),
        ], check=r"0.75 \times 1.33 = 1"),
        EX("Worked example 2: the gains from specialisation", intro="Before trade, each country splits its resources equally between the goods. Show that specialisation according to comparative advantage raises world output.", steps=[
            S("Before trade", text="Cameroon: 30 cocoa + 22.5 cloth. Northland: 10 cocoa + 15 cloth. World: 40 cocoa and 37.5 cloth."),
            S("Specialise", text="Northland produces only cloth: 30. Cameroon keeps world cloth at 37.5 by making 7.5 cloth, which costs it 7.5 ÷ 0.75 = 10 tonnes of cocoa, so it makes 50 cocoa."),
            S("After specialisation", text="World: 50 cocoa and 37.5 cloth. There are 10 extra tonnes of cocoa, with no loss of cloth."),
            S("Share the gain", text="Trade at any rate between 0.75 and 1.5 cloth per tonne of cocoa (for example 1 for 1) lets both countries consume beyond their own frontiers."),
        ], check=r"50 + 7.5 \div 0.75 = 60"),
        D("Trade benefits both countries only if the **terms of trade** (the rate at which goods exchange) lie **between** the two countries' opportunity cost ratios. "
          "Here: 0.75 < cloth per tonne of cocoa < 1.5.", title="Limits of the terms of trade"),
        H("Why do opportunity costs differ? Heckscher-Ohlin"),
        T("The **Heckscher-Ohlin theory** says a country has a comparative advantage in goods that use intensively the factor it has in abundance. A country with abundant "
          "fertile land and a tropical climate (like Cameroon) tends to export land-intensive goods such as cocoa, coffee and timber; a country with abundant capital exports "
          "capital-intensive manufactures. Comparative advantage can change over time as countries build up capital and skills (**dynamic comparative advantage**)."),
        H("Assumptions, limits and protection"),
        KEY("Assumptions of the simple model", "Each one is a point of evaluation.", cards=[
            ["Constant costs", "In reality, opportunity costs rise as a country specialises (curved PPF), so gains are smaller."],
            ["No transport costs or barriers", "Transport costs and tariffs reduce or remove the gains."],
            ["Perfect factor mobility inside a country", "Workers cannot easily move from cloth to cocoa: there is structural unemployment during adjustment."],
            ["Full employment and two goods", "A simplification of a complex world."],
        ]),
        T("Specialising in a few primary products leaves a country exposed to price swings and to a possible long-run fall in its terms of trade (see the next lesson). "
          "Arguments for **protection** (tariffs, quotas, subsidies, import bans) include: protecting **infant industries** until they can compete, protecting jobs, "
          "raising government revenue, preventing **dumping**, strategic or food security, and correcting a balance of payments deficit. Arguments against: higher prices for consumers, "
          "less competition and efficiency, retaliation, and loss of the gains from comparative advantage. The infant-industry argument is usually judged the strongest for a developing country, "
          "provided protection is temporary."),
        MISTAKE("Using absolute advantage to decide specialisation", "Specialisation follows comparative advantage. Compare opportunity costs, not the size of output."),
        MISTAKE("Inverting the opportunity cost", "The opportunity cost of one unit of cocoa is cloth given up divided by cocoa gained (45 ÷ 60), not cocoa divided by cloth."),
        QUIZ("Country A can produce 40 units of maize or 20 units of cotton; Country B can produce 30 maize or 30 cotton. Which is correct?", ["A has a comparative advantage in cotton", "B has a comparative advantage in maize", "A has a comparative advantage in maize", "Neither country gains from trade"], 2,
             "Opportunity cost of maize: A 20 ÷ 40 = 0.5 cotton; B 30 ÷ 30 = 1 cotton. A's is lower, so A has the comparative advantage in maize.", hint="Compare the cotton given up for one unit of maize.",
             feedback=["A gives up 2 maize for each cotton, B only 1, so B has the advantage in cotton.", "B's opportunity cost of maize (1 cotton) is higher than A's (0.5).", "", "Opportunity costs differ, so both can gain."]),
        QUIZ("With the opportunity costs of cocoa at 0.75 cloth (Cameroon) and 1.5 cloth (Northland), which terms of trade benefit both countries?", ["1 tonne of cocoa for 0.5 cloth", "1 tonne of cocoa for 1.2 cloth", "1 tonne of cocoa for 2 cloth", "1 tonne of cocoa for 0.75 cloth"], 1,
             "1.2 lies between 0.75 and 1.5, so both countries gain.", hint="The rate must lie strictly between the two opportunity costs.",
             feedback=["Below 0.75: Cameroon would do better producing cloth itself.", "", "Above 1.5: Northland would do better producing cocoa itself.", "At exactly 0.75, Cameroon gains nothing."]),
        TIP("Comparative advantage is often tested with a table in Paper 1 and Paper 3: compute opportunity costs as fractions, state who specialises in what, and show the gain. In Paper 2 essays, explain the theory and then evaluate its assumptions and the case for protection.", title="Exam link"),
        PQ("Country X: 10 workers produce 50 bags of coffee or 25 radios. Country Y: 10 workers produce 20 bags of coffee or 20 radios. Identify comparative advantage and the range of terms of trade.",
           "Opportunity cost of 1 bag of coffee: X 25 ÷ 50 = 0.5 radio; Y 20 ÷ 20 = 1 radio. X has the comparative advantage in coffee; Y in radios (Y's cost of a radio is 1 coffee, X's is 2). Mutually beneficial terms: between 0.5 and 1 radio per bag of coffee."),
        PQ("Distinguish between absolute advantage and comparative advantage.",
           "Absolute advantage is the ability to produce more of a good than another country with the same resources, whereas comparative advantage is the ability to produce a good at a lower opportunity cost than another country. A country can have an absolute advantage in both goods but a comparative advantage in only one."),
        PQ("Essay plan: 'Free trade according to comparative advantage benefits all countries.' Discuss with reference to a primary-exporting country.",
           "Explain comparative advantage with a numerical example; gains: higher world output, lower prices, wider choice, economies of scale, competition. Limits: assumptions (constant costs, no transport costs, mobility); concentration on primary exports brings unstable prices and a possible fall in the terms of trade; infant industries never develop; adjustment costs and job losses. Evaluation: gains are real but unevenly shared; case for temporary protection and diversification (dynamic comparative advantage). Conclusion."),
        SUM("Absolute advantage: more output from the same resources. Comparative advantage: lower opportunity cost.",
            "Specialising according to comparative advantage raises world output, even if one country is better at everything.",
            "Trade benefits both only if the terms of trade lie between the two opportunity cost ratios.",
            "Heckscher-Ohlin: countries export goods that use their abundant factor intensively.",
            "Evaluate with the model's assumptions, primary-product dependence and the arguments for protection."),
    ],
))

# ------------------------------------------------------------------ 7. Terms of trade
LESSONS.append(lesson(
    module=M_INT,
    topic="Terms of trade",
    title="The terms of trade: measurement, causes and consequences",
    slug="ecu2-terms-of-trade",
    minutes=21,
    summary="How the terms of trade index is calculated, what makes it improve or deteriorate, why an 'improvement' is not always good news, the income terms of trade, and the Prebisch-Singer view of primary-commodity exporters such as Cameroon.",
    objectives=[
        "Calculate the terms of trade index and the percentage change in it",
        "Explain the causes of a favourable or unfavourable movement in the terms of trade",
        "Analyse the effects of a change in the terms of trade using price elasticity of demand and the income terms of trade",
        "Evaluate the Prebisch-Singer hypothesis for primary-commodity exporters",
    ],
    key_concepts=["Terms of trade", "Export price index", "Import price index", "Favourable movement", "Unfavourable movement",
                  "Income terms of trade", "Prebisch-Singer hypothesis"],
    blocks=[
        H("Introduction"),
        T("If the world price of cocoa falls while the price of imported tractors rises, Cameroon must export more cocoa to buy the same tractor. "
          "The **terms of trade** measure this rate of exchange between a country's exports and its imports. For a country that depends on a few primary exports, "
          "the terms of trade can matter as much as the volume of production."),
        D("The **terms of trade (ToT)** compare the average price of a country's exports with the average price of its imports, as an index number.", title="Terms of trade",
          formula=r"\text{ToT} = \frac{\text{index of export prices}}{\text{index of import prices}} \times 100"),
        T("In the base year the index is 100. A **rise** in the index is a **favourable** (improving) movement: each unit of exports buys more imports. "
          "A **fall** is an **unfavourable** (deteriorating) movement. These words describe the price ratio only; they do not tell you whether the economy is better off overall."),
        EX("Worked example 1: calculating the index", intro="From the base year to year 2 (invented data) the export price index rises to 120 and the import price index to 150. Find the terms of trade and the change.", steps=[
            S("Index", math=r"\text{ToT} = \frac{120}{150} \times 100 = 80"),
            S("Change", math=r"\frac{80 - 100}{100} \times 100 = -20\%", text="An unfavourable movement: although export prices rose, import prices rose faster."),
        ], check=r"120 \div 150 = 0.8"),
        H("Causes of changes"),
        KEY("What moves the terms of trade?", "Anything that changes export prices relative to import prices.", cards=[
            ["World demand and supply", "A rise in world demand for oil or cocoa raises export prices; a bumper world harvest lowers them."],
            ["Exchange rate", "An appreciation raises export prices in foreign currency and lowers import prices in home currency: the ToT improve. A devaluation does the opposite."],
            ["Relative inflation", "Faster domestic inflation than abroad raises export prices relative to import prices."],
            ["Productivity", "Falling costs in exporting industries may be passed on as lower export prices."],
        ]),
        H("Is an improvement good news?"),
        T("It depends on **why** the index changed and on the **price elasticity of demand** for exports. If the ToT improve because export prices rise due to strong world demand, "
          "export revenue rises: good news. If they improve because domestic inflation or an appreciation makes exports dearer, and demand for exports is price elastic, "
          "export volumes and revenue fall, jobs are lost and the current account may worsen."),
        D("The **income terms of trade** take export volume into account: they measure the capacity of export earnings to buy imports.", title="Income terms of trade",
          formula=r"\text{income ToT} = \frac{\text{index of export prices}}{\text{index of import prices}} \times \text{index of export volume}"),
        EX("Worked example 2: price and income terms of trade", intro="An export price index of 90, an import price index of 108, and an export volume index of 130 (invented). Find the terms of trade and the income terms of trade.", steps=[
            S("Terms of trade", math=r"\frac{90}{108} \times 100 = 83.3", text="Unfavourable: down 16.7%."),
            S("Income terms of trade", math=r"\frac{90}{108} \times 130 = 108.3", text="Because the volume of exports rose strongly, export earnings can buy 8.3% more imports than in the base year."),
        ], check=r"0.8333 \times 130 = 108.3"),
        H("The Prebisch-Singer hypothesis"),
        T("Raúl Prebisch and Hans Singer argued (around 1950) that the terms of trade of countries exporting primary commodities tend to **deteriorate in the long run** against manufactures. "
          "Reasons given: primary goods have a low income elasticity of demand, so world demand grows slowly as incomes rise; synthetic substitutes replace some raw materials; "
          "productivity gains in commodities are passed on as lower prices, while in manufacturing they are kept as higher wages and profits by firms with market power. "
          "Evidence is debated: commodity prices also show long booms (for example the 2000s) and sharp falls, so **volatility** may be the bigger problem. "
          "The policy conclusion often drawn is **diversification** into processing and manufacturing, an aim of Cameroon's development strategy."),
        MISTAKE("Calling a favourable movement always beneficial", "A 'favourable' movement means export prices have risen relative to import prices. If demand for exports is elastic, revenue and jobs may fall. Always explain the cause and the elasticity."),
        MISTAKE("Turning the ratio upside down", "The terms of trade are export prices over import prices, multiplied by 100. Import over export gives the wrong direction."),
        QUIZ("Export prices fall by 10% and import prices are unchanged. The terms of trade index (base 100) becomes:", ["110", "90", "111.1", "100"], 1,
             "90 ÷ 100 × 100 = 90: an unfavourable movement.", hint="Divide the new export price index by the import price index.",
             feedback=["That would follow a 10% rise in export prices.", "", "That is 100 ÷ 90 × 100, the ratio inverted.", "The index changes because export prices changed."]),
        QUIZ("Which is most likely to IMPROVE a country's terms of trade?", ["A devaluation of its currency", "A rise in world demand for its main export", "A fall in world prices of its exports", "Faster inflation among its trading partners' exports than among its own"], 1,
             "Higher world demand raises export prices relative to import prices.", hint="Which option raises export prices relative to import prices?",
             feedback=["A devaluation lowers export prices in foreign currency and raises import prices: the ToT worsen.", "", "That worsens the terms of trade.", "That raises the prices of its imports relative to its exports: the ToT worsen."]),
        TIP("Terms of trade calculations are common in Paper 1 and Paper 3. In Paper 2, explain whether a change is good or bad by linking it to its cause, price elasticity and the balance of payments.", title="Exam link"),
        PQ("Between two years the export price index rises from 100 to 110 and the import price index falls from 100 to 95. Calculate the terms of trade and state the direction of change.",
           "ToT = 110 ÷ 95 × 100 = 115.8. This is a favourable movement of 15.8%: each unit of exports buys more imports."),
        PQ("Explain two reasons why the terms of trade of a primary-exporting country may deteriorate in the long run.",
           "1. Low income elasticity of demand for primary products: as world incomes rise, demand for food and raw materials grows more slowly than demand for manufactures, so their relative prices tend to fall. 2. Productivity gains and new supplies in primary production lower prices in competitive world markets, while manufacturers with market power keep gains as profits and wages; synthetic substitutes also reduce demand for raw materials."),
        PQ("Essay plan: 'An improvement in the terms of trade is always beneficial.' Discuss.",
           "Define ToT and favourable movement; formula. Beneficial when caused by rising world demand for exports: more imports per unit of exports, higher export revenue and income, better current account. Not beneficial when caused by domestic inflation or appreciation with price-elastic export demand: export volumes fall, unemployment rises, current account worsens (use PED and the income terms of trade). Evaluation: depends on cause, elasticities, time period and the country's structure. Conclusion."),
        SUM("ToT = export price index ÷ import price index × 100; a rise is favourable, a fall unfavourable.",
            "Causes: world demand and supply, exchange rates, relative inflation and productivity.",
            "A favourable movement is good only if it does not cut export volumes too much: check the cause and PED.",
            "Income terms of trade = price ToT × export volume index ÷ 100.",
            "Prebisch-Singer: primary exporters' terms of trade tend to deteriorate; diversification is the usual response."),
    ],
))

# ------------------------------------------------------------------ 8. The balance of payments
LESSONS.append(lesson(
    module=M_INT,
    topic="The balance of payments",
    title="The balance of payments: accounts, disequilibrium and its correction",
    slug="ecu2-balance-of-payments",
    minutes=25,
    summary="The current, capital and financial accounts, the components of the current account, why the accounts balance yet a deficit or surplus can be a problem, and how to correct it, including the Marshall-Lerner condition and the J-curve.",
    objectives=[
        "Describe the components of the current, capital and financial accounts and calculate the current account balance",
        "Explain why the balance of payments always balances in accounting terms but can be in disequilibrium",
        "Explain short-term and long-term measures to correct a current account deficit or surplus",
        "Explain the Marshall-Lerner condition and the J-curve and use them to evaluate devaluation",
    ],
    key_concepts=["Balance of payments", "Current account", "Visible trade", "Invisible trade", "Primary income", "Secondary income",
                  "Financial account", "Expenditure-switching", "Expenditure-reducing", "Marshall-Lerner condition", "J-curve"],
    blocks=[
        H("Introduction"),
        T("Every time a Cameroonian firm exports bananas, a family in Bamenda receives money from a relative abroad, or a foreign company builds a factory in Douala, "
          "a record is made. The **balance of payments (BoP)** is the record of all economic transactions between the residents of a country and the rest of the world over a period, usually a year. "
          "The Board's 2023 report noted that many candidates could not explain the components of the current account, so learn them carefully."),
        H("The structure of the accounts"),
        KEY("The current account", "Flows of income and spending. Older textbooks use 'visible' and 'invisible' terms; newer ones use the four headings below (check your textbook).", cards=[
            ["Trade in goods (visible trade)", "Exports and imports of physical goods: cocoa, crude oil, timber, machinery, rice. The balance is the visible balance or balance of trade."],
            ["Trade in services (invisibles)", "Transport, insurance, banking, tourism, telecommunications, education and health services bought from or sold to non-residents."],
            ["Primary income (invisibles)", "Income from factors: wages of cross-border workers, interest, profits and dividends on foreign investment (for example profits sent home by foreign firms)."],
            ["Secondary income (current transfers)", "Transfers with nothing given in return: remittances from migrants, aid grants for current spending, payments to international bodies."],
        ]),
        T("The **capital account** records capital transfers (for example debt forgiveness and the purchase or sale of non-produced assets such as patents) and is usually small. "
          "The **financial account** records flows of investment: **direct investment** (FDI, buying a lasting controlling interest), **portfolio investment** (shares and bonds), "
          "**other investment** (loans and bank deposits) and changes in **reserve assets** (foreign currency held by the central bank; for CEMAC states these are pooled at BEAC). "
          "**Net errors and omissions** is a balancing item for transactions that were missed or wrongly measured."),
        D("Because every transaction is recorded twice (a credit and a debit), the balance of payments as a whole always balances: a current account deficit must be matched "
          "by a net inflow on the capital and financial accounts (borrowing, selling assets or using reserves). **Disequilibrium** means a persistent deficit or surplus on the "
          "current account that cannot be financed or sustained.", title="Why the BoP balances but can still be a problem"),
        EX("Worked example 1: the current account", intro="Data (billion FCFA, invented): exports of goods 2 500, imports of goods 2 900; exports of services 600, imports of services 900; primary income received 100, paid 350; net secondary income +350. Calculate each balance and the current account.", steps=[
            S("Trade in goods", math=r"2500 - 2900 = -400"),
            S("Trade in services", math=r"600 - 900 = -300"),
            S("Primary income", math=r"100 - 350 = -250"),
            S("Current account", math=r"-400 - 300 - 250 + 350 = -600", text="A current account deficit of 600 billion FCFA, which must be financed by net inflows on the financial account (or by reserves)."),
        ], check=r"-400 - 300 - 250 + 350 = -600"),
        H("Causes and correction of a deficit"),
        T("Causes of a current account deficit: high domestic demand pulling in imports, a fall in export prices or volumes, low competitiveness (high costs or an overvalued exchange rate), "
          "large outflows of profits and interest, and dependence on imported capital goods and food. A deficit can be sustainable if it finances productive investment and is matched by long-term inflows."),
        KEY("Policies to correct a deficit", "Learn both the type and the time scale.", cards=[
            ["Expenditure-switching (short term)", "Switch spending from imports to home goods: devaluation or depreciation, tariffs, quotas, export subsidies."],
            ["Expenditure-reducing (short term)", "Reduce total spending, and so imports: higher taxes, lower government spending, higher interest rates, credit limits. Cost: lower growth and jobs."],
            ["Supply-side (long term)", "Raise productivity and competitiveness, diversify exports, develop import substitutes."],
            ["Financing", "Borrowing, attracting FDI or using reserves cover a deficit for a while but do not cure it."],
        ]),
        T("The Board's report also noted that candidates forgot the short-term measures to remedy a **surplus**. A persistent surplus can cause inflationary pressure, means "
          "a country is consuming less than it could, and causes friction with trading partners. Short-term measures: revalue or allow the currency to appreciate, reduce tariffs and "
          "quotas to let in more imports, expand domestic demand (lower taxes, more spending, lower interest rates), and encourage capital outflows or lending abroad. "
          "Long-term: encourage investment abroad and raise domestic consumption."),
        H("Devaluation: Marshall-Lerner and the J-curve"),
        D("A devaluation (or depreciation) improves the current account only if the sum of the price elasticities of demand for exports and imports is greater than one.",
          title="Marshall-Lerner condition", formula=r"|PED_{X}| + |PED_{M}| > 1"),
        IMG("alecu2-j-curve.svg", alt="Graph of the current account balance against time. Before a devaluation the balance is a steady deficit; after the devaluation it falls further into deficit, then rises, crosses zero and moves into surplus, tracing a J shape",
            caption="Figure 1. The J-curve: after a devaluation the current account first worsens, then improves."),
        T("In the short run, demand is inelastic: contracts are fixed and buyers take time to switch, so the same quantity of imports costs more in home currency and exports "
          "earn less foreign currency. The deficit worsens. As buyers adjust, elasticities rise, the Marshall-Lerner condition is met, and the balance improves: the **J-curve**. "
          "For Cameroon, devaluation is not a national choice: the CFA franc is shared by the CEMAC states and pegged to the euro. The 1994 devaluation of the CFA franc was a joint decision of the franc zone countries."),
        EX("Worked example 2: testing Marshall-Lerner", intro="Estimates for two economies: Economy P, PED of exports −0.4 and PED of imports −0.5; Economy Q, −0.7 and −0.6. Will devaluation improve the current account?", steps=[
            S("Economy P", math=r"0.4 + 0.5 = 0.9 < 1", text="The condition fails: devaluation would worsen the current account."),
            S("Economy Q", math=r"0.7 + 0.6 = 1.3 > 1", text="The condition holds (in the long run): devaluation would improve the current account, after any J-curve dip."),
        ]),
        MISTAKE("Mixing up the BoP and a balance sheet", "The balance of payments records flows between residents and non-residents over a period. It is not the balance sheet of a bank or a firm, an error the Board's report mentioned."),
        MISTAKE("Saying the BoP is in deficit overall", "The whole BoP always balances. Say which account is in deficit, usually the current account."),
        QUIZ("Money sent home by Cameroonians working abroad is recorded under:", ["Trade in services", "Primary income", "Secondary income (current transfers)", "The financial account"], 2,
             "Remittances are transfers with nothing given in return: secondary income in the current account.", hint="Is anything given in return?",
             feedback=["No service is sold.", "Primary income is income earned by factors (wages of short-term cross-border workers, interest, profits); money sent to families by migrants living abroad is a transfer.", "", "The financial account records investment, not gifts."]),
        QUIZ("Which is an expenditure-switching policy?", ["Raising income tax", "Imposing a tariff on imported rice", "Cutting government spending", "Raising interest rates"], 1,
             "A tariff makes imports dearer, switching spending towards home-produced goods.", hint="Which policy changes relative prices rather than total spending?",
             feedback=["A tax rise reduces total spending: expenditure-reducing.", "", "Lower spending reduces total demand: expenditure-reducing.", "Higher interest rates reduce total demand: expenditure-reducing."]),
        TIP("The balance of payments appears in Paper 1 (classifying items, calculating balances), Paper 2 essays (components, causes and correction of deficits and surpluses) and Paper 3 data questions. Define the account first, link items to visible and invisible trade, and give both short-term and long-term measures when the question asks for them.", title="Exam link"),
        PQ("Classify each item for Cameroon: (a) export of cocoa; (b) profits sent home by a foreign-owned brewery; (c) a French tourist's spending in Kribi; (d) a foreign firm building a new factory in Douala.",
           "(a) Trade in goods (visible), current account credit. (b) Primary income, current account debit. (c) Trade in services (invisible), current account credit. (d) Direct investment, financial account inflow."),
        PQ("Distinguish between expenditure-switching and expenditure-reducing policies, giving one example of each.",
           "Expenditure-switching policies change relative prices so that residents and foreigners switch spending from foreign to domestic goods, for example a devaluation or a tariff, whereas expenditure-reducing policies cut total spending in the economy, which reduces spending on imports too, for example higher taxes or higher interest rates."),
        PQ("Essay plan: (a) Explain how a current account deficit is financed through the other accounts of the balance of payments. (b) Discuss the measures a government can use to reduce a persistent current account surplus.",
           "(a) Define the current account deficit; explain that it is matched by net inflows on the capital and financial accounts: FDI, portfolio inflows, loans, or a fall in reserve assets; net errors and omissions. (b) Define a surplus and why it may be a problem (inflation, unused purchasing power, retaliation). Measures: revaluation or appreciation; lower tariffs and quotas; reflationary fiscal policy; lower interest rates; encouraging investment and lending abroad. Evaluate each: effect on inflation, competitiveness, jobs; limits for a member of a monetary union with a fixed peg. Conclusion."),
        SUM("The BoP records all transactions with the rest of the world: current, capital and financial accounts plus net errors and omissions.",
            "Current account: trade in goods (visible), trade in services, primary income and secondary income (invisibles).",
            "The BoP always balances overall; disequilibrium means a persistent current account deficit or surplus.",
            "Deficits are corrected by expenditure-switching, expenditure-reducing and supply-side policies; surpluses by the reverse.",
            "Devaluation works only if |PEDx| + |PEDm| > 1, and often after a J-curve dip."),
    ],
))

# ------------------------------------------------------------------ 9. Exchange rates
LESSONS.append(lesson(
    module=M_INT,
    topic="Exchange rates",
    title="Exchange rate systems, purchasing power parity and the CFA franc",
    slug="ecu2-exchange-rates",
    minutes=25,
    summary="How floating exchange rates are set by demand and supply, the language of appreciation, depreciation, revaluation and devaluation, fixed and managed systems including the CFA franc peg to the euro, purchasing power parity, and the case for fixed against floating rates.",
    objectives=[
        "Explain, with a diagram, how a floating exchange rate is determined and why it changes",
        "Distinguish appreciation and depreciation from revaluation and devaluation, and calculate their effects on prices",
        "Explain purchasing power parity and calculate a PPP exchange rate",
        "Evaluate fixed and floating systems, with reference to the CFA franc",
    ],
    key_concepts=["Exchange rate", "Floating exchange rate", "Fixed exchange rate", "Managed float", "Appreciation", "Depreciation",
                  "Devaluation", "Revaluation", "Purchasing power parity", "Currency peg"],
    blocks=[
        H("Introduction"),
        T("An exchange rate is the price of one currency in terms of another. The CFA franc used in Cameroon is fixed to the euro at 655.957 FCFA for 1 euro, "
          "while its value against the US dollar or the Nigerian naira changes every day as the euro moves. To understand prices of imports, exports and debts, "
          "you need both kinds of system: fixed and floating."),
        H("Floating exchange rates"),
        D("Under a **floating** (flexible) exchange rate, the rate is set by the demand for and supply of the currency on the foreign exchange market, with no government target.", title="Floating rate"),
        IMG("alecu2-forex-market.svg", alt="Foreign exchange market for currency X: price of X in dollars on the vertical axis, quantity of X on the horizontal axis. Demand shifts right from D1 to D2 along an upward-sloping supply S, raising the exchange rate from e1 to e2 and quantity from Q1 to Q2",
            caption="Figure 1. A rise in demand for currency X causes it to appreciate from e1 to e2."),
        KEY("Demand and supply of a currency", "Ask: who needs this currency, and who is selling it?", cards=[
            ["Demand for X comes from", "Foreigners buying the country's exports, tourists visiting it, foreign investors buying its assets, speculators expecting X to rise."],
            ["Supply of X comes from", "Residents buying imports, travelling abroad, investing abroad, and speculators selling X."],
            ["Shifts", "Higher export demand, higher interest rates (attracting hot money), lower relative inflation and optimistic expectations raise demand for X and cause appreciation."],
        ]),
        D("Under a floating system a rise in the value of a currency is an **appreciation** and a fall is a **depreciation**. Under a fixed system, an official rise is a **revaluation** and an official fall is a **devaluation**.",
          title="Four words, two systems"),
        EX("Worked example 1: effect of a depreciation on prices", intro="Currency X falls from 2 dollars to 1.6 dollars. (a) Find the percentage depreciation. (b) A US machine costs 100 dollars. What does it cost in X before and after?", steps=[
            S("(a) Depreciation", math=r"\frac{1.6 - 2}{2} \times 100 = -20\%"),
            S("(b) Before", math=r"100 \div 2 = 50 \text{ X}"),
            S("After", math=r"100 \div 1.6 = 62.5 \text{ X}", text="Imports become dearer (by 25% in X) and exports become cheaper for foreigners."),
        ], check=r"62.5 \times 1.6 = 100"),
        H("Fixed and managed systems, and the CFA franc"),
        T("Under a **fixed** exchange rate the central bank keeps the rate at an announced level (a **peg**) by buying or selling its currency with its reserves and by setting interest rates. "
          "A **managed float** lets the rate float but the central bank intervenes to limit large movements."),
        T("The CFA franc of Central Africa (code XAF) is issued by BEAC for the six CEMAC countries (Cameroon, the Central African Republic, Chad, the Republic of Congo, Equatorial Guinea and Gabon). "
          "It is pegged to the euro at 655.957 FCFA per euro, with a convertibility guarantee from the French Treasury linked to the deposit of part of the reserves (the arrangements have been reformed over time: check current data). "
          "Its rate against the dollar therefore moves with the euro. In January 1994 the CFA franc was devalued by 50% against the French franc: the rate went from 50 to 100 CFA francs per French franc."),
        EX("Worked example 2: working through the peg", intro="1 euro = 655.957 FCFA. Suppose (a teaching value) 1 euro = 1.10 US dollars. (a) How many FCFA buy 1 dollar? (b) In 1994, how did the FCFA price of an import costing 1 000 French francs change?", steps=[
            S("(a) Cross rate", math=r"\frac{655.957}{1.10} = 596.3 \text{ FCFA per dollar}"),
            S("(b) Before devaluation", math=r"1000 \times 50 = 50\,000 \text{ FCFA}"),
            S("After devaluation", math=r"1000 \times 100 = 100\,000 \text{ FCFA}", text="Import prices in FCFA doubled, while CFA-zone exports became much cheaper abroad."),
        ]),
        H("Purchasing power parity"),
        D("The **purchasing power parity (PPP)** theory says that, in the long run, exchange rates move so that the same basket of goods costs the same in different countries when converted into one currency.",
          title="Purchasing power parity", formula=r"\text{PPP rate (home per foreign)} = \frac{\text{price of basket at home}}{\text{price of basket abroad}}"),
        T("Example: if a basket costs 3 000 FCFA in Cameroon and 5 euros in the euro area, the PPP rate is 3 000 ÷ 5 = 600 FCFA per euro. At the actual rate of 655.957, "
          "a euro buys more than PPP suggests, so the CFA franc is **undervalued** relative to PPP on this basket (figures invented). **Relative PPP** says a country with higher inflation should see its currency depreciate by roughly the inflation difference. "
          "Limits: many goods and services are not traded, transport costs and tariffs exist, and capital flows and speculation move rates in the short run. PPP is also used to compare GDP per head across countries."),
        H("Fixed or floating?"),
        KEY("Evaluate both systems", "No system is best for every country.", cards=[
            ["Fixed: for", "Certainty for traders and investors; discipline against inflation (the CFA peg has helped keep inflation relatively low); less speculation."],
            ["Fixed: against", "Needs large reserves; loses an independent monetary policy; cannot use the exchange rate to correct a deficit; a misaligned peg can make exports uncompetitive."],
            ["Floating: for", "Automatic correction of current account imbalances; independent monetary policy; no need for big reserves."],
            ["Floating: against", "Volatility and uncertainty; risk of imported inflation after depreciation; speculation can push rates far from fundamentals."],
        ]),
        MISTAKE("Using 'devaluation' for a floating currency", "A floating currency depreciates; a fixed currency is devalued by an official decision. Use the right word for the system."),
        MISTAKE("Getting the direction of import prices wrong", "When the home currency falls, imports become dearer in home currency and exports cheaper in foreign currency, not the other way round."),
        QUIZ("Which would cause a floating currency to appreciate?", ["Higher inflation at home than abroad", "A rise in the country's interest rates relative to others", "A rise in imports", "Expectations that the currency will fall"], 1,
             "Higher interest rates attract financial inflows, raising demand for the currency.", hint="Which change raises demand for the currency?",
             feedback=["Higher inflation makes exports less competitive and lowers demand for the currency.", "", "More imports increase the supply of the currency.", "Speculators would sell, increasing supply."]),
        QUIZ("A basket costs 4 500 FCFA in Cameroon and 9 dollars in the USA. The PPP exchange rate is:", ["500 FCFA per dollar", "0.002 FCFA per dollar", "40 500 FCFA per dollar", "2 dollars per FCFA"], 0,
             "4 500 ÷ 9 = 500 FCFA per dollar.", hint="Home price divided by foreign price.",
             feedback=["", "That is 9 ÷ 4 500, the inverse.", "That multiplies instead of dividing.", "That is not a sensible ratio of the two prices."]),
        TIP("Exchange rates appear in Paper 1 (definitions, diagram shifts, PPP and price calculations) and in Paper 2 essays comparing fixed and floating systems or discussing the CFA franc. Draw the currency market diagram with correct axes, and use the correct word for each system.", title="Exam link"),
        PQ("The rate of currency Y rises from 4 to 5 units of Z per Y. (a) Has Y appreciated or depreciated, and by what percentage? (b) What happens to the Z price of a good costing 20 Y?",
           "(a) Appreciated by (5 − 4) ÷ 4 × 100 = 25%. (b) Before: 20 × 4 = 80 Z. After: 20 × 5 = 100 Z. Y's exports become dearer for buyers who pay in Z."),
        PQ("Explain three factors that increase the demand for a country's currency on the foreign exchange market.",
           "1. Higher demand for its exports (foreigners must buy the currency to pay). 2. Higher interest rates than abroad, attracting financial inflows. 3. Inward foreign direct investment, as firms buy currency to build factories. Others: tourism into the country; speculation that the currency will rise; lower relative inflation."),
        PQ("Essay plan: Discuss the advantages and disadvantages for Cameroon of a fixed exchange rate between the CFA franc and the euro.",
           "Explain the peg (655.957 FCFA per euro, BEAC, CEMAC). Advantages: price stability and lower inflation; certainty for trade with the euro area and for investors; credibility; a common currency eases trade within CEMAC. Disadvantages: no independent monetary or exchange rate policy; rate moves with the euro against the dollar, in which oil and many commodities are priced; risk of overvaluation and lost competitiveness (as before 1994); need for reserves. Evaluation: depends on inflation differences, shocks and fiscal discipline; reform debates. Conclusion."),
        SUM("A floating rate is set by demand and supply of the currency; a fixed rate is held by the central bank.",
            "Floating: appreciation and depreciation. Fixed: revaluation and devaluation.",
            "A fall in the home currency makes imports dearer and exports cheaper.",
            "The CFA franc is pegged to the euro at 655.957 FCFA; it was devalued by 50% against the French franc in 1994.",
            "PPP: in the long run rates move so that a basket costs the same everywhere; it fails for many short-run reasons."),
    ],
))

# ------------------------------------------------------------------ 10. Economic integration
LESSONS.append(lesson(
    module=M_INT,
    topic="Economic integration",
    title="Economic integration: stages, trade creation and diversion, CEMAC and AfCFTA",
    slug="ecu2-economic-integration",
    minutes=24,
    summary="The stages of economic integration from a preferential trade area to complete union, the static effects of trade creation and trade diversion, the dynamic gains, and an evaluation of CEMAC and the African Continental Free Trade Area for Cameroon.",
    objectives=[
        "Describe the stages of economic integration and place CEMAC and AfCFTA on them",
        "Explain and calculate trade creation and trade diversion",
        "Explain the dynamic benefits and the costs of integration",
        "Evaluate the problems facing regional integration in Africa",
    ],
    key_concepts=["Economic integration", "Free trade area", "Customs union", "Common external tariff", "Common market",
                  "Monetary union", "Trade creation", "Trade diversion", "CEMAC", "AfCFTA"],
    blocks=[
        H("Introduction"),
        T("A trader carrying goods from Douala to Libreville or N'Djamena should, in principle, face no customs duty, because Cameroon, Gabon and Chad belong to the same customs union. "
          "Countries group together to trade more freely and to grow faster, but the gains are not automatic. This lesson explains the forms of **economic integration** and how to judge them."),
        D("**Economic integration** is the removal of barriers to trade and to the movement of factors between member countries, and the coordination of their economic policies.", title="Economic integration"),
        IMG("alecu2-integration-stages.svg", alt="Six stacked boxes showing the stages of integration: preferential trade area, free trade area, customs union, common market, economic union, complete integration, each with a note of what is added",
            caption="Figure 1. Stages of economic integration: each stage adds to the one before."),
        T("A **free trade area** removes tariffs between members, but each keeps its own tariffs on outsiders, so **rules of origin** are needed to stop goods entering through the member with the lowest tariff. "
          "A **customs union** adds a **common external tariff (CET)**. A **common market** adds free movement of labour and capital. An **economic union** harmonises economic policies; a **monetary union** shares one currency and one central bank."),
        H("Cameroon's regional groupings"),
        KEY("Where Cameroon belongs", "Well-established facts; check the current details of tariffs and timetables.", cards=[
            ["CEMAC", "The Economic and Monetary Community of Central Africa: Cameroon, the Central African Republic, Chad, the Republic of Congo, Equatorial Guinea and Gabon. Its treaty dates from 1994. It is a customs union with a common external tariff and a monetary union using the CFA franc issued by BEAC, with free movement of people agreed among its members (implementation has been uneven)."],
            ["ECCAS", "The Economic Community of Central African States, a wider regional community that includes the CEMAC states and others in Central Africa."],
            ["AfCFTA", "The African Continental Free Trade Area, an agreement among African Union members adopted in 2018; trading under it formally began on 1 January 2021 and its secretariat is in Accra, Ghana. It aims to remove tariffs on most goods traded between members and to liberalise services. Cameroon is a party (check its current schedules)."],
        ]),
        H("Static effects: trade creation and trade diversion"),
        D("**Trade creation**: joining a union shifts consumption from a higher-cost domestic producer to a lower-cost partner producer; resources are used more efficiently and welfare rises. "
          "**Trade diversion**: joining a union shifts imports from a lower-cost non-member to a higher-cost member, because only the outsider still pays the tariff; resources are used less efficiently. "
          "The terms were introduced by Jacob Viner (1950).", title="Trade creation and trade diversion"),
        EX("Worked example 1: trade diversion", intro="Cameroon imports a good. The cost of production (invented, FCFA per unit) is 800 in Country A (outside the union) and 900 in partner B. Before the union, Cameroon charges a 25% tariff on all imports. After joining a union with B, imports from B are tariff-free but the 25% CET still applies to A.", steps=[
            S("Before the union", math=r"A: 800 \times 1.25 = 1000 \qquad B: 900 \times 1.25 = 1125", text="Cameroon buys from A at 1 000; the government collects 200 per unit in tariff revenue."),
            S("After the union", math=r"A: 1000 \qquad B: 900", text="Consumers switch to B, which is now cheaper to them."),
            S("Effect", text="Imports are diverted from the lowest-cost producer (800) to a higher-cost one (900). Consumers save 100 per unit but the government loses 200 in revenue: the economy loses 100 per unit of real resources. This is trade diversion."),
        ], check=r"200 - 100 = 100"),
        EX("Worked example 2: trade creation", intro="Now a domestic producer makes the good at 950 per unit, partner B at 900, and the pre-union tariff is 25% on B. What happens when the tariff on B is removed?", steps=[
            S("Before", math=r"B: 900 \times 1.25 = 1125 > 950", text="The domestic producer supplies the market at 950."),
            S("After", math=r"B: 900 < 950", text="Imports from B replace dearer domestic output."),
            S("Effect", text="A saving of 50 per unit in real resources: production moves to a lower-cost source. This is trade creation; consumers also gain from the lower price, but domestic producers lose sales."),
        ]),
        T("A union is more likely to raise welfare when the pre-union tariffs were high, the CET is low, members' costs are close to world costs, and members produce competing goods "
          "so that low-cost producers can replace high-cost ones."),
        H("Dynamic effects and problems"),
        KEY("Dynamic gains", "These may outweigh the static effects.", cards=[
            ["Larger market", "Economies of scale for firms that sell to the whole union."],
            ["Competition", "Firms must become more efficient."],
            ["Investment", "A bigger market attracts foreign direct investment."],
            ["Bargaining power", "A group can negotiate better in world trade talks."],
        ]),
        T("Problems facing African integration: members produce similar primary goods, so there is little to trade with each other; poor transport links and many checkpoints raise costs; "
          "non-tariff barriers persist; overlapping memberships of regional groups; loss of tariff revenue for governments that depend on it; fear that benefits go to the most industrial member; "
          "and political will. Within CEMAC, Cameroon is the largest economy and often the main supplier of manufactured goods to its neighbours, so it may gain more from trade creation than smaller members."),
        MISTAKE("Confusing a free trade area with a customs union", "Both remove tariffs between members. Only a customs union has a common external tariff. A free trade area needs rules of origin."),
        MISTAKE("Assuming all integration raises welfare", "Integration can divert trade towards higher-cost members. Weigh trade creation against trade diversion and add the dynamic effects."),
        QUIZ("Which stage of integration first adds free movement of labour and capital?", ["Free trade area", "Customs union", "Common market", "Preferential trade area"], 2,
             "A common market is a customs union plus free movement of factors.", hint="Which stage goes beyond goods?",
             feedback=["A free trade area covers goods only.", "A customs union adds a common external tariff, not factor mobility.", "", "A preferential trade area only lowers some tariffs."]),
        QUIZ("A union causes a country to buy from a higher-cost member instead of a lower-cost non-member. This is:", ["Trade creation", "Trade diversion", "Dumping", "Comparative advantage"], 1,
             "Shifting purchases to a higher-cost source because of the union's tariff structure is trade diversion.", hint="Has trade moved to a cheaper or a dearer producer?",
             feedback=["Trade creation moves production to a lower-cost source.", "", "Dumping is selling abroad below cost.", "This moves trade away from the lowest-cost producer, against comparative advantage."]),
        TIP("Integration appears in Paper 1 (stages, creation and diversion) and in Paper 2 essays on CEMAC, AfCFTA or the benefits and costs of regional groupings. Name the stage, use creation and diversion, then evaluate with dynamic gains and real African problems.", title="Exam link"),
        PQ("Country A produces a good at 600, partner B at 650 and the home country at 700 (FCFA per unit, invented). The home tariff is 20%. Which source supplies the home market (a) before and (b) after a customs union with B that keeps a 20% CET on A? Name the effect.",
           "(a) Before: A costs 600 × 1.2 = 720, B 650 × 1.2 = 780, home 700. Home producer supplies at 700. (b) After: A 720, B 650, home 700. B supplies at 650. Compared with home production at 700, this saves 50 per unit: trade creation. (Compared with the lowest-cost world source A at 600, the union price is higher, but A was not supplying before, so there is no diversion.)"),
        PQ("Distinguish between a customs union and a common market.",
           "A customs union removes barriers to trade in goods between members and sets a common external tariff on non-members, whereas a common market goes further by also allowing free movement of factors of production, labour and capital, between members."),
        PQ("Essay plan: Discuss the likely benefits and costs for Cameroon of the African Continental Free Trade Area.",
           "Explain AfCFTA as a free trade area (stage, rules of origin). Benefits: access to a continental market; economies of scale for Cameroonian manufacturers and agro-industries; trade creation; FDI; diversification away from primary exports. Costs: competition for infant industries; loss of tariff revenue; possible trade diversion; adjustment and unemployment. Problems: infrastructure, non-tariff barriers, similar exports, overlapping CEMAC commitments. Evaluation: benefits depend on transport links and supply-side improvements. Conclusion."),
        SUM("Stages: preferential trade area, free trade area, customs union (CET), common market, economic or monetary union, complete integration.",
            "CEMAC is a customs union and monetary union (CFA franc, BEAC); AfCFTA is a continental free trade area.",
            "Trade creation moves supply to lower-cost producers; trade diversion moves it to higher-cost members.",
            "Dynamic gains: scale, competition, investment, bargaining power.",
            "African integration faces similar exports, poor infrastructure, non-tariff barriers and revenue losses."),
    ],
))

# ------------------------------------------------------------------ 11. Economic growth models
LESSONS.append(lesson(
    module=M_DEV,
    topic="Economic growth models",
    title="Economic growth: sources, the Harrod-Domar model and Rostow's stages",
    slug="ecu2-growth-models",
    minutes=25,
    summary="Actual and potential growth, the sources of growth (capital deepening, human capital, technology), the Harrod-Domar model and the savings gap, Rostow's five stages of growth, and the criticisms of both models.",
    objectives=[
        "Distinguish actual from potential growth and explain the main sources of growth, including capital deepening and human capital",
        "State and use the Harrod-Domar equation to find growth rates and the savings required for a target",
        "Describe Rostow's five stages of economic growth",
        "Evaluate both models as guides for a developing economy such as Cameroon",
    ],
    key_concepts=["Actual growth", "Potential growth", "Capital deepening", "Human capital", "Harrod-Domar model",
                  "Capital-output ratio", "Savings gap", "Rostow's stages", "Take-off"],
    blocks=[
        H("Introduction"),
        T("Cameroon's Vision 2035 aims for the country to become an emerging economy, which requires sustained high growth. But what makes an economy grow, and how much saving and investment "
          "does growth need? This lesson looks at the sources of growth and two classic models used to think about growth in developing countries."),
        D("**Actual growth** is the annual percentage increase in real GDP. **Potential growth** is the increase in the economy's productive capacity (an outward shift of the production possibility curve or of LRAS). "
          "Actual growth can exceed potential growth for a while if there are unused resources, but in the long run it is limited by potential growth.", title="Actual and potential growth"),
        KEY("Sources of growth", "What raises productive capacity?", cards=[
            ["Physical capital", "More machines, roads and buildings. **Capital deepening** means more capital per worker, which raises labour productivity; capital widening only keeps capital per worker constant as the labour force grows."],
            ["Human capital", "The skills, knowledge and health of workers, raised by education, training and health care."],
            ["Technology", "Better methods and new products raise output from the same inputs."],
            ["Natural resources and labour", "New discoveries (such as oil and gas) and a growing, more employed labour force."],
            ["Institutions", "Secure property rights, stable policy and low corruption encourage investment."],
        ]),
        H("The Harrod-Domar model"),
        D("The **Harrod-Domar model** (Roy Harrod and Evsey Domar, 1930s-1940s) says the rate of growth of national income depends on the savings ratio and the productivity of capital.",
          title="Harrod-Domar", formula=r"g = \frac{s}{v}"),
        T(r"Here $g$ is the growth rate of GDP, $s$ the proportion of income saved (and invested), and $v$ the **capital-output ratio** (the amount of capital needed to produce one extra unit of output). "
          r"The logic: saving finances investment; investment adds to the capital stock; the extra capital produces extra output at the rate $1/v$. "
          r"The policy message: to grow faster, raise saving or make capital more productive (lower $v$)."),
        EX("Worked example 1: growth and the savings gap", intro="A country saves 20% of its income and has a capital-output ratio of 4. Its population grows at 2.5% a year. (a) What is the growth rate? (b) What is the growth of income per head? (c) What savings ratio is needed to grow at 7%?", steps=[
            S("(a) Growth", math=r"g = \frac{0.20}{4} = 0.05 = 5\%"),
            S("(b) Per head", math=r"5\% - 2.5\% \approx 2.5\%"),
            S("(c) Required saving", math=r"s = g \times v = 0.07 \times 4 = 0.28 = 28\%"),
            S("Savings gap", math=r"28\% - 20\% = 8\% \text{ of GDP}", text="The gap could be filled by foreign aid, borrowing or foreign direct investment: the model's argument for external finance."),
        ], check=r"0.28 \div 4 = 0.07"),
        T("**Criticisms**: saving does not automatically become productive investment (weak banks, capital flight); the capital-output ratio is not fixed; the model ignores human capital, technology and institutions; "
          "it was built for industrial economies; and aid filling the savings gap has often not produced the predicted growth."),
        H("Rostow's stages of growth"),
        IMG("alecu2-rostow.svg", alt="Five bars rising like a staircase, labelled 1 traditional society, 2 preconditions for take-off, 3 take-off, 4 drive to maturity, 5 high mass consumption, with an arrow for rising income per head",
            caption="Figure 1. W. W. Rostow's five stages of economic growth (1960)."),
        KEY("The five stages", "Rostow described them from the history of industrial countries.", cards=[
            ["1. Traditional society", "Mostly subsistence farming, limited technology, little saving."],
            ["2. Preconditions for take-off", "Rising saving and investment, infrastructure, an entrepreneurial class, more trade."],
            ["3. Take-off", "Rapid growth led by a few leading sectors; investment rises to over 10% of national income (Rostow's figure)."],
            ["4. Drive to maturity", "Growth spreads to many sectors; technology improves; the economy diversifies."],
            ["5. Age of high mass consumption", "High incomes, consumer durables and services dominate."],
        ]),
        T("**Criticisms**: the stages are descriptive, not a theory of how to move between them; not every country follows the same path; the stages overlap; the model ignores colonial history, "
          "world trade and external constraints faced by today's developing countries; and it is hard to test. Its strength is to stress investment, leading sectors and the preconditions for growth."),
        EX("Worked example 2: applying the models (plan)", intro="Use the two models to discuss what Cameroon needs for faster growth.", steps=[
            S("Harrod-Domar", text="Raise domestic saving (financial inclusion, banking access), attract FDI, and make investment efficient (lower v) through good project choice and maintenance."),
            S("Rostow", text="Strengthen the preconditions: infrastructure, an entrepreneurial class, agricultural productivity; identify leading sectors such as agro-processing."),
            S("Beyond the models", text="Human capital, technology and institutions matter as much as capital, as the Board's 2023 report suggested in a question on capital deepening and human capital."),
            S("Judge", text="The models give useful but partial guidance; growth also needs diversification and stable policy."),
        ]),
        MISTAKE("Confusing capital deepening with more investment in general", "Capital deepening means a rise in capital **per worker**. If capital grows only as fast as the labour force, that is capital widening, and productivity does not rise."),
        MISTAKE("Repeating points from the passage", "In data questions the Board's report warns against copying factors already given in the passage. Give new points and state them in the direction the question asks."),
        QUIZ("Using Harrod-Domar, a country saves 15% of GDP with a capital-output ratio of 5. Its growth rate is:", ["3%", "75%", "20%", "33%"], 0,
             "g = s ÷ v = 0.15 ÷ 5 = 0.03 = 3%.", hint="Divide the savings ratio by the capital-output ratio.",
             feedback=["", "That multiplies 15 by 5.", "That adds 15 and 5.", "That divides 5 by 15."]),
        QUIZ("In Rostow's model, the stage in which a few leading sectors grow rapidly and investment rises sharply is:", ["Traditional society", "Preconditions for take-off", "Take-off", "High mass consumption"], 2,
             "Take-off is the stage of rapid, self-sustaining growth led by leading sectors.", hint="Which stage is named after an aeroplane leaving the ground?",
             feedback=["Traditional society has little growth.", "This stage prepares for growth.", "", "This is the final stage of mature, consumption-led economies."]),
        TIP("Growth models appear in Paper 1 (Harrod-Domar calculations, stages) and in Paper 2 and Paper 3 questions on growth in Cameroon. Give the formula, define each term, calculate, and then criticise the model.", title="Exam link"),
        PQ("A country has a savings ratio of 24% and a capital-output ratio of 3. Its population grows at 3% a year. Calculate the growth rate of GDP and of GDP per head.",
           "g = 0.24 ÷ 3 = 0.08 = 8%. Growth of GDP per head ≈ 8% − 3% = 5%."),
        PQ("Distinguish between capital deepening and human capital, and give one way to increase each.",
           "Capital deepening is an increase in the amount of physical capital per worker, for example giving farmers machinery or building more workshops per worker, whereas human capital is the stock of skills, knowledge and health embodied in workers, increased for example through education, training and better health care."),
        PQ("Essay plan: Evaluate the usefulness of the Harrod-Domar model for a developing country.",
           "Explain the model (g = s/v, terms, logic). Uses: shows the importance of saving and investment; identifies the savings gap; justifies aid, FDI and borrowing; simple to apply. Limits: saving may not be invested productively; v not constant; ignores human capital, technology, institutions; aid did not deliver predicted growth; debt problems from borrowing. Evaluation: a starting point, not a full theory; combine with human capital and structural change. Conclusion."),
        SUM("Actual growth is the rise in real GDP; potential growth is the rise in productive capacity.",
            "Sources: physical capital (capital deepening), human capital, technology, resources and institutions.",
            "Harrod-Domar: g = s ÷ v; the savings gap is the extra saving needed for a target growth rate.",
            "Rostow: traditional society, preconditions, take-off, drive to maturity, high mass consumption.",
            "Both models are useful but partial; they ignore much of what limits growth today."),
    ],
))

# ------------------------------------------------------------------ 12. Development and its measurement
LESSONS.append(lesson(
    module=M_DEV,
    topic="Development and its measurement",
    title="Development: meaning, characteristics, the HDI and the vicious circle of poverty",
    slug="ecu2-development-measurement",
    minutes=25,
    summary="The difference between growth and development, the characteristics of developing countries, how development is measured (GNI per head at PPP, the Human Development Index, the Lorenz curve and Gini coefficient, other indicators), and the vicious circle of poverty.",
    objectives=[
        "Distinguish economic growth from economic development and list the characteristics of developing countries",
        "Calculate the Human Development Index from its three dimension indices and evaluate it",
        "Interpret a Lorenz curve and calculate a Gini coefficient from income shares",
        "Explain the vicious circle of poverty and how it might be broken",
    ],
    key_concepts=["Economic development", "GNI per head at PPP", "Human Development Index", "Lorenz curve", "Gini coefficient",
                  "Multidimensional poverty", "Vicious circle of poverty"],
    blocks=[
        H("Introduction"),
        T("Two countries can have the same income per head, yet in one most children finish school and live to old age, while in the other many do not. "
          "**Economic development** is about more than income: it is about the quality of people's lives. This lesson shows how economists define and measure it."),
        D("**Economic growth** is an increase in real GDP (a quantitative change). **Economic development** is an improvement in the economic welfare and living standards of the population: "
          "higher real incomes, but also better health, education, less poverty and inequality, and more freedom of choice (a qualitative change). Growth can happen without much development "
          "if its benefits are narrowly shared.", title="Growth and development"),
        KEY("Common characteristics of developing countries", "Not every country has all of them.", cards=[
            ["Income and poverty", "Low income per head, high absolute poverty and often high inequality."],
            ["Structure", "A large share of employment in agriculture and the informal sector; dependence on a few primary exports."],
            ["People", "Rapid population growth, a young population, lower life expectancy and literacy, and rural-urban migration."],
            ["Capital and markets", "Low saving and investment, weak infrastructure, small financial sectors, and external debt."],
        ]),
        H("Measuring development"),
        T("**GNI per head at purchasing power parity (PPP)** adjusts income for the cost of living, so it compares living standards better than income at market exchange rates. "
          "But it ignores distribution, non-market output, health and education, and the environment. Composite indicators try to fix this."),
        D("The **Human Development Index (HDI)**, published by the United Nations Development Programme since 1990, combines three dimensions: a long and healthy life (life expectancy at birth), "
          "knowledge (mean years of schooling of adults and expected years of schooling of children) and a decent standard of living (GNI per head at PPP). "
          "Each dimension index runs from 0 to 1; the HDI is their geometric mean.", title="Human Development Index",
          formula=r"\text{dimension index} = \frac{\text{actual} - \text{minimum}}{\text{maximum} - \text{minimum}} \qquad \text{HDI} = (I_{\text{health}} \times I_{\text{education}} \times I_{\text{income}})^{1/3}"),
        T("The UNDP's goalposts used here (check your textbook or the latest technical notes, as they are revised): life expectancy 20 to 85 years; expected schooling 0 to 18 years; mean schooling 0 to 15 years; "
          "GNI per head 100 to 75 000 PPP dollars, using natural logarithms. The education index is the average of the two schooling indices."),
        EX("Worked example 1: an HDI calculation", intro="A country (invented data) has life expectancy 60 years, expected schooling 12 years, mean schooling 6 years and GNI per head 3 500 PPP dollars. Calculate its HDI.", steps=[
            S("Health index", math=r"\frac{60 - 20}{85 - 20} = \frac{40}{65} = 0.615"),
            S("Education index", math=r"\tfrac{1}{2}\left(\frac{12}{18} + \frac{6}{15}\right) = \tfrac{1}{2}(0.667 + 0.400) = 0.533"),
            S("Income index", math=r"\frac{\ln 3500 - \ln 100}{\ln 75\,000 - \ln 100} = \frac{\ln 35}{\ln 750} = \frac{3.555}{6.620} = 0.537"),
            S("HDI", math=r"(0.615 \times 0.533 \times 0.537)^{1/3} = 0.561", text="A value in the UNDP's 'medium' band on its usual thresholds (check the current bands)."),
        ], check=r"0.561^3 \approx 0.176"),
        T("**Evaluating the HDI**: it is broader than income alone and easy to compare. But it ignores inequality (the inequality-adjusted HDI tries to correct this), "
          "political freedom, the environment and the informal economy; the weights and goalposts are chosen by judgement; and the data in poor countries can be weak. "
          "Other indicators include the **Multidimensional Poverty Index** (deprivations in health, education and living standards), absolute poverty lines, literacy, infant mortality, and access to water and electricity."),
        H("Measuring inequality: Lorenz curve and Gini coefficient"),
        IMG("alecu2-lorenz.svg", alt="Cumulative % of income against cumulative % of households: a diagonal line of equality and a Lorenz curve bowed below it through (20, 5), (40, 15), (60, 30), (80, 55); area A between the lines, area B under the curve",
            caption="Figure 1. A Lorenz curve. Gini coefficient = A ÷ (A + B)."),
        F(r"\text{Gini} = \frac{A}{A + B} = \frac{0.5 - B}{0.5} \quad (\text{axes as fractions, so } A + B = 0.5)", title="Gini coefficient"),
        EX("Worked example 2: Gini from quintile shares", intro="The poorest to richest 20% of households receive 5%, 10%, 15%, 25% and 45% of income (invented). Find the Gini coefficient using trapezia under the Lorenz curve.", steps=[
            S("Cumulative shares", text="0, 0.05, 0.15, 0.30, 0.55, 1.00 at 0, 0.2, 0.4, 0.6, 0.8, 1.0 of households."),
            S("Area B (five trapezia, width 0.2)", math=r"B = 0.2 \times \tfrac{1}{2}[(0 + 0.05) + (0.05 + 0.15) + (0.15 + 0.30) + (0.30 + 0.55) + (0.55 + 1)] = 0.2 \times 1.55 = 0.31"),
            S("Gini", math=r"\frac{0.5 - 0.31}{0.5} = 0.38", text="0 means perfect equality, 1 means one household has everything. The further the Lorenz curve bows from the diagonal, the higher the Gini."),
        ], check=r"0.5 - 0.31 = 0.19"),
        H("The vicious circle of poverty"),
        IMG("alecu2-vicious-circle.svg", alt="Circle of five linked boxes with arrows: low income per head leads to low saving, which leads to low investment, then little capital per worker, then low productivity, and back to low income per head",
            caption="Figure 2. The vicious circle of poverty."),
        T("The idea, associated with Ragnar Nurkse, is that poverty perpetuates itself: low incomes allow little saving, so investment is low, workers have little capital, productivity stays low, and incomes stay low. "
          "A demand-side version adds that low incomes mean small markets, which give little incentive to invest. Ways to break the circle: foreign aid and FDI to supplement saving, "
          "investment in human capital, better access to finance (microfinance, mobile money), land and agricultural reform, and trade to reach larger markets. Critics note that some poor countries have escaped poverty, "
          "so the circle is not unbreakable."),
        MISTAKE("Treating growth and development as the same", "Growth is a rise in real output; development is a broader improvement in welfare. Show you know they can diverge."),
        MISTAKE("Averaging the HDI dimensions arithmetically", "Since 2010 the HDI uses the geometric mean of the three indices, and the income index uses logarithms (check your textbook's version)."),
        QUIZ("Which is NOT one of the three dimensions of the HDI?", ["A long and healthy life", "Knowledge", "A decent standard of living", "Income equality"], 3,
             "The HDI uses health, education and income; inequality is captured by the separate inequality-adjusted HDI or by the Gini coefficient.", hint="Recall the three components.",
             feedback=["Measured by life expectancy at birth.", "Measured by mean and expected years of schooling.", "Measured by GNI per head at PPP.", ""]),
        QUIZ("If a country's Lorenz curve moves closer to the line of equality, its Gini coefficient:", ["Rises", "Falls", "Stays the same", "Becomes negative"], 1,
             "Area A shrinks, so A ÷ (A + B) falls: income is more equally shared.", hint="What happens to area A?",
             feedback=["A rise means more inequality, with the curve bowing further away.", "", "The area between the curves changes, so the Gini changes.", "The Gini lies between 0 and 1."]),
        TIP("The Board's report noted that characteristics of developing countries were well answered but obstacles to growth in Cameroon were sometimes given in a dual (two-way) manner when one direction was asked. In Paper 1 expect HDI and Gini calculations; in Paper 2 essays, compare indicators and evaluate.", title="Exam link"),
        PQ("Life expectancy 72 years, expected schooling 13.5 years, mean schooling 9 years, GNI per head 7 500 PPP dollars (invented). Calculate the health and education indices.",
           "Health index = (72 − 20) ÷ (85 − 20) = 52 ÷ 65 = 0.800. Expected schooling index = 13.5 ÷ 18 = 0.750; mean schooling index = 9 ÷ 15 = 0.600; education index = (0.750 + 0.600) ÷ 2 = 0.675."),
        PQ("Distinguish between economic growth and economic development.",
           "Economic growth is an increase in a country's real output (real GDP) over time, a quantitative change, whereas economic development is a broader improvement in living standards and welfare, including health, education, poverty, inequality and freedom, a qualitative change."),
        PQ("Essay plan: 'GNI per head is the best measure of development.' Discuss.",
           "Explain GNI per head at PPP: data available, comparable, linked to material welfare. Limits: ignores distribution (show Lorenz/Gini), non-market and informal output, health and education, environment, freedom. Alternatives: HDI (calculation, strengths and weaknesses), MPI, inequality-adjusted HDI, social indicators. Evaluation: no single measure is best; use several. Conclusion."),
        SUM("Growth is a rise in real output; development is a broader rise in welfare and living standards.",
            "Developing countries often share low income, primary dependence, a large informal sector and weak infrastructure.",
            "HDI = geometric mean of health, education and income indices, each (actual − min) ÷ (max − min).",
            "Lorenz curve and Gini coefficient measure inequality: Gini = A ÷ (A + B).",
            "The vicious circle of poverty links low income, saving, investment and productivity; aid, FDI and human capital can break it."),
    ],
))

# ------------------------------------------------------------------ 13. Aid, FDI and MNCs
LESSONS.append(lesson(
    module=M_DEV,
    topic="Aid, foreign investment and multinational corporations",
    title="Foreign aid, foreign direct investment, multinationals and structural adjustment",
    slug="ecu2-aid-fdi-mncs",
    minutes=25,
    summary="Types of foreign aid and the arguments for and against it, the two-gap model, foreign direct investment and multinational corporations with their benefits and costs, external debt ratios, and the role of the IMF and World Bank, including structural adjustment in Cameroon.",
    objectives=[
        "Classify foreign aid and explain the savings gap and foreign exchange gap it may fill",
        "Analyse the benefits and costs of FDI and multinational corporations for a host country",
        "Calculate and interpret the debt service ratio and the effect of profit repatriation",
        "Explain and evaluate IMF and World Bank structural adjustment programmes, with reference to Cameroon",
    ],
    key_concepts=["Bilateral aid", "Multilateral aid", "Tied aid", "Two-gap model", "Foreign direct investment",
                  "Multinational corporation", "Transfer pricing", "Debt service ratio", "Structural adjustment programme", "HIPC"],
    blocks=[
        H("Introduction"),
        T("A new bridge financed by a foreign government, a mobile network owned by a foreign company, and an IMF programme with conditions attached: all three bring foreign resources into an economy. "
          "In the growth models lesson you met the savings gap. This lesson asks how well aid, foreign investment and borrowing fill it, and at what cost."),
        H("Foreign aid"),
        D("**Foreign aid** (official development assistance) is the transfer of resources to developing countries on concessional terms: grants, or loans at below-market interest rates and long repayment periods.", title="Foreign aid"),
        KEY("Types of aid", "Classify by who gives it, on what terms and in what form.", cards=[
            ["Bilateral or multilateral", "From one government to another, or through international bodies such as the World Bank, the African Development Bank or UN agencies."],
            ["Tied or untied", "Tied aid must be spent on goods and services from the donor country, often at higher cost; untied aid can be spent anywhere."],
            ["Grants or soft loans", "Grants need no repayment; soft loans must be repaid, adding to debt."],
            ["Project, programme, technical, humanitarian", "Aid for a specific project (a road), for the budget or a sector, for expertise and training, or for emergencies."],
        ]),
        T("The **two-gap model** extends Harrod-Domar: growth may be held back by a **savings gap** (domestic saving below the investment needed) and a **foreign exchange gap** (export earnings below the imports needed, "
          "such as machinery and fuel). Aid and foreign capital can fill whichever gap is binding."),
        KEY("Evaluating aid", "Use both sides in an essay.", cards=[
            ["For", "Fills savings and foreign exchange gaps; funds infrastructure, health and education; emergency relief; technical knowledge."],
            ["Against", "Tied aid raises costs; loans add to debt; aid may be lost to corruption or fund prestige projects; dependency; it may weaken incentives to collect taxes; donors' political aims."],
        ]),
        H("Foreign direct investment and multinational corporations"),
        D("**Foreign direct investment (FDI)** is investment by a firm in one country that gives it a lasting controlling interest in a business in another, either by building new facilities (**greenfield**) "
          "or by buying an existing firm. A **multinational corporation (MNC)** produces in more than one country.", title="FDI and MNCs"),
        KEY("FDI and MNCs in a host country", "Weigh the two sides with examples (brewing, telecommunications, agro-industry, oil).", cards=[
            ["Benefits", "Capital without debt; jobs and training; technology and management skills; exports and foreign exchange; tax revenue; links to local suppliers; better infrastructure."],
            ["Costs", "Profits repatriated abroad (a primary income outflow); **transfer pricing** to shift profits to low-tax countries; capital-intensive methods with few jobs; competition that pushes out local firms; environmental damage; political influence; footloose firms that leave."],
        ]),
        EX("Worked example 1: debt and profit outflows", intro="A country's annual debt service (interest plus repayments) is 300 billion FCFA and its export earnings are 2 000 billion FCFA. Separately, an MNC earns annual profits of 10 billion FCFA and sends 60% home. (Figures invented.)", steps=[
            S("Debt service ratio", math=r"\frac{300}{2000} \times 100 = 15\%", text="15% of export earnings go to servicing debt and cannot buy imports."),
            S("Profit repatriated", math=r"0.6 \times 10 = 6 \text{ billion FCFA}", text="Recorded as a debit in primary income: it worsens the current account each year."),
            S("Retained", math=r"10 - 6 = 4 \text{ billion FCFA}", text="Reinvested earnings stay in the host economy."),
        ], check=r"6 + 4 = 10"),
        H("The IMF, the World Bank and structural adjustment"),
        T("The **International Monetary Fund (IMF)** lends to countries with balance of payments problems and monitors economic policy. The **World Bank** lends for development projects and reforms. "
          "In the 1980s and 1990s many indebted countries received loans under **structural adjustment programmes (SAPs)**, with conditions such as: cutting budget deficits, "
          "removing subsidies and price controls, privatising state enterprises, liberalising trade and finance, and devaluing overvalued currencies."),
        T("Cameroon's experience is a standard case. Falling oil and commodity prices from the mid-1980s led to a deep economic crisis. Cameroon adopted adjustment programmes with the IMF and World Bank from 1988, "
          "including public enterprise reform, privatisation and cuts in public spending; the CFA franc was devalued in 1994. Under the Heavily Indebted Poor Countries (HIPC) initiative, "
          "Cameroon reached its completion point in 2006 and received large debt relief. Growth recovered after the mid-1990s, but the social costs of adjustment were high (check your textbook for details)."),
        EX("Worked example 2: evaluating SAPs (plan)", intro="Evaluate the effects of structural adjustment programmes on developing countries.", steps=[
            S("Aims", text="Restore balance of payments and fiscal balance; improve efficiency by letting markets work; regain access to finance."),
            S("Positive effects", text="Lower inflation and deficits; more efficient firms after privatisation; better export competitiveness after devaluation; debt relief later linked to reforms."),
            S("Negative effects", text="Spending cuts on health and education; job losses in the public sector; higher prices after subsidy removal; growth slow to return; reduced policy freedom."),
            S("Judgement", text="Outcomes depended on how reforms were sequenced and on world prices; later programmes added poverty reduction strategies to protect social spending."),
        ]),
        MISTAKE("Treating all foreign money as aid", "Aid is concessional. FDI is private investment for profit, and commercial loans are borrowing at market rates. Classify the flow first."),
        MISTAKE("Listing MNC benefits with no costs", "Evaluation needs both sides, linked to the host country: repatriated profits, transfer pricing and few local linkages can cancel many benefits."),
        QUIZ("Aid that must be spent on goods and services from the donor country is:", ["Multilateral aid", "Untied aid", "Tied aid", "Humanitarian aid"], 2,
             "Tied aid restricts spending to the donor's suppliers, often raising costs.", hint="Look for the word that means restricted.",
             feedback=["Multilateral aid comes through international bodies.", "Untied aid can be spent anywhere.", "", "Humanitarian aid is defined by its purpose (emergencies), not by where it is spent."]),
        QUIZ("Transfer pricing by an MNC means:", ["Charging different prices to different consumers", "Setting prices on trade between its own subsidiaries to move profits to low-tax countries", "Paying higher wages than local firms", "Transferring technology to the host country"], 1,
             "Internal prices between branches can shift recorded profits to where taxes are lowest, reducing the host's tax revenue.", hint="The trade is inside the same company.",
             feedback=["That is price discrimination.", "", "Wages are not transfer pricing.", "Technology transfer is a benefit, not transfer pricing."]),
        TIP("Aid, FDI and MNCs are common Paper 2 essay topics and appear in Paper 3 data questions. Define each flow, use the two-gap model, and give a two-sided evaluation applied to Cameroon.", title="Exam link"),
        PQ("Debt service is 450 billion FCFA and export earnings are 3 000 billion FCFA. Calculate the debt service ratio and explain why a high ratio is a problem.",
           "450 ÷ 3 000 × 100 = 15%. A high ratio means a large share of foreign exchange goes to creditors, leaving less to import capital goods, food and fuel; it signals vulnerability if export prices fall."),
        PQ("Distinguish between bilateral and multilateral aid.",
           "Bilateral aid is given directly by one government to another, whereas multilateral aid is given through international organisations such as the World Bank, the African Development Bank or UN agencies, which pool funds from many donors."),
        PQ("Essay plan: Discuss whether multinational corporations do more good than harm to developing countries.",
           "Define MNC and FDI. Benefits: capital, jobs, skills, technology, exports, tax, infrastructure, linkages. Harms: profit repatriation, transfer pricing, enclave production, crowding out of local firms, environmental damage, political influence. Evaluation: depends on the host's regulation and bargaining power, the sector, local content rules and governance. Conclusion with a judgement."),
        SUM("Aid: concessional transfers; bilateral or multilateral, tied or untied, grants or loans.",
            "The two-gap model: aid and foreign capital fill savings and foreign exchange gaps.",
            "FDI gives capital, jobs and technology, but profits may be repatriated and taxes avoided by transfer pricing.",
            "Debt service ratio = debt service ÷ export earnings × 100.",
            "IMF and World Bank SAPs (Cameroon from 1988; CFA devaluation 1994; HIPC completion 2006) restored balances at social cost."),
    ],
))

# ------------------------------------------------------------------ 14. The Cameroonian economy
LESSONS.append(lesson(
    module=M_DEV,
    topic="The Cameroonian economy",
    title="The Cameroonian economy: structure, history and the NDS30 strategy",
    slug="ecu2-cameroonian-economy",
    minutes=25,
    summary="A structural analysis of Cameroon's economy: its sectors and main products, the path from the oil boom through crisis, adjustment and debt relief, the National Development Strategy 2020-2030 (NDS30) and Vision 2035, and the main obstacles to faster growth and development.",
    objectives=[
        "Describe the structure of the Cameroonian economy by sector, main products and trade partners' groupings",
        "Outline the main phases of Cameroon's economic history since independence using well-established facts",
        "Explain the pillars and aims of the NDS30 and link them to the theory in this course",
        "Analyse obstacles to rapid growth in Cameroon and evaluate policies to overcome them",
    ],
    key_concepts=["Primary, secondary and tertiary sectors", "Informal sector", "Export concentration", "Structural transformation",
                  "Import substitution", "Vision 2035", "NDS30", "Diversification"],
    blocks=[
        H("Introduction"),
        T("This final content lesson applies the whole Upper Sixth course to one economy: Cameroon. It uses only well-established facts; any figures are invented for practice, "
          "so always check the latest data from the National Institute of Statistics (INS), the Ministry of the Economy (MINEPAT), BEAC or the World Bank before quoting numbers in an exam."),
        H("Structure of the economy"),
        KEY("Three sectors", "Cameroon is often called 'Africa in miniature' for its variety of climates and resources.", cards=[
            ["Primary", "Food crops (cassava, plantains, maize, sorghum, groundnuts), cash crops (cocoa, coffee, cotton, bananas, rubber, palm oil), timber, livestock and fishing, crude oil and natural gas, and some mining."],
            ["Secondary", "Agro-processing, brewing and soft drinks, cement, aluminium smelting at Edea, oil refining, wood processing, construction and energy (hydroelectric dams)."],
            ["Tertiary", "Trade, transport (the ports of Douala and Kribi serve Cameroon and landlocked neighbours such as Chad and the Central African Republic), telecommunications, banking and public administration."],
        ]),
        T("Two features stand out. First, a very large **informal sector**: most workers are self-employed or in small unregistered activities, especially in agriculture and petty trade, which links to the underemployment you met in the unemployment lesson. "
          "Second, **export concentration**: a few primary products (crude oil, cocoa, timber, and a handful of others) earn most of the foreign exchange, exposing the economy to world price shocks (see the lessons on the terms of trade and the trade cycle)."),
        EX("Worked example 1: sector shares (invented data)", intro="GDP is 20 000 billion FCFA: primary sector 3 400, secondary 5 600, tertiary 11 000. Find each share and comment.", steps=[
            S("Primary", math=r"\frac{3400}{20\,000} \times 100 = 17\%"),
            S("Secondary", math=r"\frac{5600}{20\,000} \times 100 = 28\%"),
            S("Tertiary", math=r"\frac{11\,000}{20\,000} \times 100 = 55\%"),
            S("Comment", text="A large tertiary share does not always mean a 'modern' economy: much of it may be informal trade. A sector's share of employment can be very different from its share of output; agriculture usually employs a much larger share of workers than its share of GDP."),
        ], check=r"17 + 28 + 55 = 100"),
        H("A short economic history"),
        KEY("Main phases", "Well-established outline; check your textbook for detail.", cards=[
            ["1960s to mid-1980s", "Growth based on agricultural exports under five-year development plans; oil production began in the late 1970s and boosted growth and government revenue."],
            ["Mid-1980s to mid-1990s", "Falling oil and commodity prices, an overvalued currency and public enterprise losses caused a deep crisis. Adjustment programmes with the IMF and World Bank began in 1988; public sector pay was cut; the CFA franc was devalued by 50% in January 1994."],
            ["Mid-1990s to 2010", "Growth recovered; privatisation of several state enterprises; HIPC debt relief with the completion point reached in 2006. Vision 2035 (adopted in 2009) set the long-term aim of becoming an emerging economy."],
            ["2010 to 2019", "The Growth and Employment Strategy Paper (GESP) guided large infrastructure projects such as the Kribi deep-sea port and hydroelectric dams (for example Lom Pangar and Memve'ele)."],
            ["2020 to 2030", "The National Development Strategy 2020-2030 (NDS30) is the second phase of Vision 2035."],
        ]),
        H("The National Development Strategy 2020-2030 (NDS30)"),
        T("The NDS30 aims at **structural transformation**: moving workers and resources from low-productivity activities into processing, manufacturing and modern services, so that growth is faster, more diversified and creates more decent jobs. "
          "It places weight on **import substitution** (producing locally goods that are now imported, such as rice, fish, milk and building materials) and on processing local raw materials such as cocoa, cotton and timber before export. "
          "It is organised around four pillars (check the official document for details):"),
        KEY("Four pillars of NDS30", "Link each pillar to economic theory.", cards=[
            ["1. Structural transformation of the economy", "Industrialisation, agro-industry, energy and infrastructure: a supply-side and diversification strategy (Rostow's leading sectors; Prebisch-Singer's case for diversification)."],
            ["2. Human capital development and well-being", "Education, training, health and social protection: raising human capital and HDI."],
            ["3. Promotion of employment and economic integration", "Jobs and regional and continental integration (CEMAC, AfCFTA): trade creation and larger markets."],
            ["4. Governance, decentralisation and strategic management of the State", "Institutions, public finance management and decentralised local government: the institutional source of growth."],
        ]),
        EX("Worked example 2: an obstacles-and-policies plan", intro="Identify four obstacles to rapid economic growth in Cameroon and suggest a policy for each.", steps=[
            S("Infrastructure gaps", text="Power cuts and poor roads raise costs. Policy: invest in energy and transport, with public-private partnerships."),
            S("Dependence on primary exports", text="Price shocks cause boom and bust. Policy: diversification and local processing; saving revenue in good years."),
            S("Skills mismatch and informality", text="Low productivity and underemployment. Policy: technical and vocational training; simpler registration and taxes to bring firms into the formal sector."),
            S("Governance and the business climate", text="Corruption and slow procedures discourage investment. Policy: stronger institutions, transparent public finance and faster courts. (Insecurity in some regions also disrupts activity; discuss it in neutral, economic terms.)"),
        ]),
        T("**Evaluation**: Cameroon's strengths include a diverse resource base, a relatively diversified economy for the region, a strategic coastline and ports serving neighbours, and price stability helped by the CFA peg. "
          "Constraints include limited monetary independence within CEMAC, debt servicing, the size of the informal sector and the time needed for structural change. The success of NDS30 depends on financing, execution and maintenance of projects, and on the world economy."),
        MISTAKE("Inventing statistics", "Examiners reward accurate reasoning more than numbers. If you are not sure of a figure, describe the trend in words (for example 'agriculture employs a large share of the labour force') rather than inventing a percentage."),
        MISTAKE("Stating obstacles in a dual manner", "The Board's report noted that candidates stated obstacles to growth in Cameroon in a two-way manner when the question asked for one direction. If asked for obstacles, state each as a cause of slow growth, for example 'inadequate electricity supply raises production costs'."),
        QUIZ("Which is the best example of import substitution in Cameroon?", ["Exporting more raw cocoa beans", "Expanding local rice production to replace imported rice", "Lowering tariffs on imported rice", "Borrowing abroad to import more food"], 1,
             "Import substitution means producing at home goods that were imported.", hint="Which option replaces imports with home production?",
             feedback=["This raises exports of a raw product; it does not replace imports.", "", "Lower tariffs encourage imports.", "This increases imports."]),
        QUIZ("The NDS30 covers which period?", ["2010 to 2019", "2020 to 2030", "1988 to 1994", "2035 to 2045"], 1,
             "NDS30 is the National Development Strategy for 2020 to 2030, the second phase of Vision 2035.", hint="The number in the name is a year.",
             feedback=["That was the period of the GESP.", "", "Those years mark the start of adjustment and the CFA devaluation.", "2035 is the target year of Vision 2035."]),
        TIP("Questions on Cameroon appear across all three papers, especially Paper 3 (data on growth and obstacles) and Paper 2 (applying theory to Cameroon). Use well-established facts, apply the theory from each module, and avoid copying points from a passage.", title="Exam link"),
        PQ("Output (invented) is: agriculture 4 000, industry 5 000, services 11 000 billion FCFA. Calculate the share of each sector in GDP.",
           "Total = 20 000. Agriculture 4 000 ÷ 20 000 = 20%; industry 5 000 ÷ 20 000 = 25%; services 11 000 ÷ 20 000 = 55%."),
        PQ("State four obstacles to rapid economic growth in Cameroon.",
           "Any four, each stated as a cause of slow growth: inadequate and unreliable electricity supply; poor road and rail networks raising transport costs; dependence on a few primary exports with unstable prices; a large informal sector with low productivity; skills mismatch in the labour force; corruption and a weak business climate; high debt service; insecurity in some regions disrupting production and trade."),
        PQ("Essay plan: Evaluate the strategies of the NDS30 for achieving structural transformation in Cameroon.",
           "Explain structural transformation and the four pillars. Analyse with theory: industrialisation and import substitution (infant industries, diversification, Prebisch-Singer); human capital (growth sources, HDI); integration (AfCFTA, CEMAC, trade creation); governance (institutions). Evaluate: financing needs and debt; risk of inefficient protected firms; execution and maintenance of projects; world price shocks; the CEMAC framework limits monetary tools. Conclusion: sound direction, success depends on implementation."),
        SUM("Cameroon has diverse primary, secondary and tertiary activities, a large informal sector and concentrated primary exports.",
            "History: export-led growth and oil, crisis from the mid-1980s, adjustment from 1988, devaluation in 1994, HIPC completion in 2006.",
            "Vision 2035 aims for an emerging economy; GESP (2010-2019) and NDS30 (2020-2030) are its phases.",
            "NDS30 pillars: structural transformation, human capital, employment and integration, governance.",
            "Obstacles include infrastructure, skills, informality, export dependence and governance; use only well-established facts."),
    ],
))

# ------------------------------------------------------------------ Examination 1. Paper 1
LESSONS.append(lesson(
    module=M_EXAM,
    topic="Paper 1",
    title="Paper 1: 50 multiple-choice questions in Economics",
    slug="ecu2-paper1-multiple-choice",
    minutes=23,
    summary="How to approach the 50 multiple-choice questions of Economics Paper 1: what the Board's 2023 report says about the paper, a routine for each question, fast methods for the common Upper Sixth calculations, the traps in wrong options and a revision map of the six modules.",
    objectives=[
        "Describe the structure of Paper 1 using the Board's 2023 report",
        "Use a four-step routine to answer recall, application and evaluation questions",
        "Carry out the standard Upper Sixth calculations quickly and check them against the options",
        "Recognise the common distractors and plan revision across all six modules",
    ],
    key_concepts=["Multiple-choice question", "Stem", "Distractor", "Elimination", "Calculation check", "Revision map"],
    blocks=[
        H("Introduction"),
        T("Paper 1 of the A Level Economics examination (0725) has **50 multiple-choice questions** and is worth **30%** of the examination. The Board's 2023 report says the paper covered the whole syllabus, "
          "with most questions testing knowledge and comprehension, a smaller group testing application and analysis, and a few testing synthesis and evaluation. "
          "So most marks reward secure knowledge of definitions and relationships, but you also need quick calculation and reasoning. "
          "In the KKEVO mock that goes with this lesson we allow 90 minutes (a KKEVO practice setting): a little under two minutes a question."),
        H("A routine for every question"),
        KEY("Read, predict, eliminate, check", "Use the same four steps each time.", cards=[
            ["1. Read the stem", "Underline key words: NOT, MOST likely, in the short run, real or nominal, increase or decrease. Note the units."],
            ["2. Predict", "Answer in your head before you read the options, so a tempting wrong option does not lead you."],
            ["3. Eliminate", "Cross out options you know are wrong and say why: wrong direction, wrong curve, wrong formula."],
            ["4. Check", "Re-read the stem with your choice. For calculations, substitute back or estimate the size."],
        ]),
        H("Calculations you must do fast"),
        CODE("Topic                    Formula\n"
             "Multiplier               k = 1 / (1 - MPC) = 1 / MPW (open economy)\n"
             "Credit multiplier        1 / reserve ratio\n"
             "Quantity theory          MV = PT\n"
             "Real GDP                 nominal GDP / deflator x 100\n"
             "Unemployment rate        unemployed / labour force x 100\n"
             "Inflation rate           change in CPI / previous CPI x 100\n"
             "Terms of trade           export price index / import price index x 100\n"
             "Marshall-Lerner          |PEDx| + |PEDm| > 1\n"
             "Harrod-Domar             g = s / v\n"
             "Debt service ratio       debt service / export earnings x 100", "text", title="Table 1. Upper Sixth formulae for Paper 1"),
        EX("Worked example 1: a multiplier question", intro="In an open economy the MPS is 0.1, the marginal tax rate 0.15 and the MPM 0.25. Investment rises by 60 billion FCFA. By how much does national income rise? A 60, B 120, C 171, D 600.", steps=[
            S("Predict", math=r"k = \frac{1}{0.1 + 0.15 + 0.25} = \frac{1}{0.5} = 2"),
            S("Calculate", math=r"\Delta Y = 2 \times 60 = 120"),
            S("Eliminate", text="A ignores the multiplier; C forgets the tax leakage (60 ÷ 0.35 ≈ 171); D uses the closed-economy multiplier 1 ÷ 0.1 = 10. The answer is B."),
        ], check=r"0.1 + 0.15 + 0.25 = 0.5"),
        EX("Worked example 2: a diagram-reading question", intro="On a Phillips curve diagram the economy moves from a point on the vertical line at 5% unemployment and 2% inflation to a point at 3% unemployment and 6% inflation on the same short-run curve. What has happened?", steps=[
            S("Predict", text="A movement along a short-run curve to lower unemployment and higher inflation follows a rise in aggregate demand while expectations are unchanged."),
            S("Eliminate", text="An option saying 'expected inflation has risen' is wrong: that would shift the curve. An option saying 'supply-side policy' is wrong: that would move the vertical line."),
            S("Check", text="Choose the option that describes an unanticipated demand expansion in the short run."),
        ]),
        H("Traps in the wrong options"),
        KEY("Common distractors", "Each is built on a real mistake.", cards=[
            ["Wrong direction", "Appreciation for depreciation, surplus for deficit, rise for fall."],
            ["Wrong system", "'Devaluation' for a floating currency; 'BEAC raises Cameroon's own rate' when BEAC sets one rate for CEMAC."],
            ["Half a calculation", "The first step only: the change in index points instead of the percentage, or income before the multiplier."],
            ["True but irrelevant", "A correct statement that does not answer this stem."],
            ["Reversed ratio", "Imports over exports for the terms of trade; labour force over unemployed."],
        ]),
        H("Revision map: six Upper Sixth modules"),
        CODE("Module                                 Be ready for\n"
             "National Income & Keynesian Equil.     GDP/GNP/NNP, deflator, C/S functions,\n"
             "                                       multiplier, accelerator, gaps\n"
             "Money, Banking & Monetary Policy       money supply, credit creation, liquidity\n"
             "                                       preference, MV = PT, BEAC instruments\n"
             "Public Finance & Fiscal Policy         fiscal policy, tax principles and\n"
             "                                       incidence, budget, national debt\n"
             "Unemployment, Inflation & Cycles       types, CPI, Phillips curve, cycle,\n"
             "                                       supply-side policy\n"
             "International Economics                comparative advantage, ToT, BoP,\n"
             "                                       exchange rates, integration\n"
             "Growth, Development & Cameroon         Harrod-Domar, Rostow, HDI, aid/FDI,\n"
             "                                       NDS30", "text", title="Table 2. Revision map"),
        T("Remember that the GCE examines the whole A Level course: Lower Sixth microeconomics will also appear in the examination. Revise it with the Lower Sixth course."),
        MISTAKE("Leaving questions blank", "A blank cannot score. If unsure after elimination, choose the best remaining option, mark the question and return to it if time allows."),
        MISTAKE("Missing NOT or EXCEPT", "Many wrong answers come from not noticing a negative stem. Circle NOT, EXCEPT and LEAST before reading the options."),
        QUIZ("A question asks: 'Which of the following would NOT shift a country's LRAS to the right?' What are you looking for?", ["The option that increases productive capacity", "The option that does not increase productive capacity", "The longest option", "Any option about aggregate demand being wrong"], 1,
             "In a NOT question, three options are true (they do shift LRAS right) and you choose the one that does not.", hint="Read the negative carefully.",
             feedback=["That would be true for three of the options.", "", "Length tells you nothing.", "An aggregate demand option may well be the answer, but you must check it rather than assume."]),
        QUIZ("The CPI rises from 150 to 159. The rate of inflation is:", ["9%", "6%", "5.7%", "59%"], 1,
             "9 ÷ 150 × 100 = 6%.", hint="Change divided by the earlier index.",
             feedback=["9 is the change in index points.", "", "That divides by 159, the later index.", "That compares 159 with a base of 100."]),
        TIP("Work through the paper once, answering what you know; mark difficult items and return to them. Keep a few minutes at the end to check that every answer is entered.", title="Exam link"),
        PQ("Reserve ratio 20%. A customer deposits 50 billion FCFA of new cash. What is the maximum total increase in deposits? A 10, B 50, C 250, D 1 000.",
           "Credit multiplier = 1 ÷ 0.2 = 5; total deposits = 5 × 50 = 250, so C. A is 20% of 50; B ignores the multiplier; D multiplies 50 by 20."),
        PQ("Export price index 105, import price index 140. The terms of trade index is: A 75, B 133.3, C 35, D 245.",
           "105 ÷ 140 × 100 = 75, so A. B inverts the ratio; C and D subtract and add the indices."),
        PQ("Name four kinds of distractor used in multiple-choice questions and give an example of each from this course.",
           "Wrong direction (appreciation instead of depreciation after a fall in demand for a currency); half a calculation (index point change instead of the percentage inflation rate); true but irrelevant (a correct fact about BEAC in a question on fiscal policy); reversed ratio (import over export prices for the terms of trade); wrong system (devaluation for a floating currency)."),
        SUM("Paper 1: 50 multiple-choice questions, 30% of the examination, covering the whole syllabus (Board's 2023 report).",
            "Use read, predict, eliminate, check for every question.",
            "Know the formulae in Table 1 and check each calculation against the options.",
            "Watch for wrong direction, wrong system, half calculations, irrelevant truths and reversed ratios.",
            "Revise all six Upper Sixth modules and the Lower Sixth course; never leave a blank."),
    ],
))

# ------------------------------------------------------------------ Examination 2. Paper 2
LESSONS.append(lesson(
    module=M_EXAM,
    topic="Paper 2",
    title="Paper 2: planning and writing Economics essays",
    slug="ecu2-paper2-essays",
    minutes=25,
    summary="How to choose, plan and write the five essays of Economics Paper 2, using the Board's 2023 report: the micro and macro sections, command words, distinctions with conjunctions, directional answers, labelled diagrams, application to Cameroon and evaluation.",
    objectives=[
        "Describe the structure and rules of Paper 2 from the Board's 2023 report",
        "Interpret command words, and tell directional questions from those that need a two-way answer",
        "Plan an essay with definitions, developed points, diagrams, application and evaluation",
        "Avoid the errors the Board's report identified",
    ],
    key_concepts=["Essay plan", "Command word", "Directional question", "Conjunction for distinction", "Labelled diagram", "Evaluation", "Application"],
    blocks=[
        H("Introduction"),
        T("Paper 2 is worth **40%** of the A Level Economics examination. The Board's 2023 report describes **8 essay questions** in two sections, **microeconomics** and **macroeconomics**. "
          "Candidates answer **five** questions, choosing **not more than three from a section**. Most questions have two parts. The report also shows that the macroeconomics questions on active and idle balances "
          "and on the balance of payments were among the worst answered, and that some candidates avoided national income questions. Do not select topics narrowly: revise the whole syllabus."),
        H("Choosing your questions"),
        T("Read all eight questions first. Count: five answers, with at most three from either section, so you need at least two from each section. Choose questions where you can answer **both parts**, "
          "draw any diagram needed, and evaluate. A popular question is not always an easy one. In the KKEVO practice paper we set 150 minutes (a KKEVO practice setting; check the real timing on your timetable), which suggests sharing your time about equally among the five essays."),
        H("What the question wants"),
        KEY("Command words and their demands", "Read the command before you plan.", cards=[
            ["Define, state, identify", "A precise definition or a short list. Accuracy matters more than length."],
            ["Explain", "Give the reason or mechanism: cause, effect, link. Use a diagram where it helps."],
            ["Distinguish (or explain the difference)", "Compare the two ideas in the same sentence using a conjunction such as 'whereas', 'while' or 'but'."],
            ["Analyse", "Break down the chain of cause and effect, step by step, often with a diagram."],
            ["Discuss, evaluate, assess, to what extent", "Two sides, weighed, with a reasoned conclusion."],
        ]),
        D("A **directional** question asks for effects or factors in one direction, for example 'factors that will **reduce** the demand for active balances' or 'factors likely to **increase** the supply of a good'. "
          "Each point must be stated in that direction: 'a **fall** in income reduces transactions demand', not 'income affects demand'. The Board's 2023 report criticised answers that explained factors in both directions, "
          "or that answered a different question (for example the determinants of demand instead of supply).", title="Directional questions"),
        T("The report also asked for answers **applied to the context**: if the question names Cameroon or a Cameroonian industry, every point must refer to it. And it repeatedly asked for **diagrams that are correctly drawn and labelled**: "
          "axes named, curves labelled, equilibria and shifts marked, and the diagram explained in the text."),
        H("A plan for every essay"),
        KEY("Structure", "Plan for two or three minutes before writing.", cards=[
            ["Introduction", "Define the key terms of the question in one or two sentences."],
            ["Developed points", "Each paragraph: one point, explained with the economic mechanism, a diagram if relevant, and an example (Cameroonian where possible)."],
            ["Evaluation", "For discuss or evaluate questions: limits, conditions ('it depends on'), short run and long run, size of effects, who gains and who loses."],
            ["Conclusion", "Answer the question directly, with a judgement based on what you have argued."],
        ]),
        EX("Worked example 1: a distinction question", intro="Distinguish between a budget deficit and the national debt.", steps=[
            S("Define with a conjunction", text="A budget deficit is the amount by which government spending exceeds government revenue in one year (a flow), whereas the national debt is the total amount the government owes from all past borrowing (a stock)."),
            S("Link the two", text="Each year's deficit, financed by borrowing, adds to the national debt; a surplus can be used to reduce it. A simple bath diagram (water flowing in and the level in the bath) can illustrate flow and stock."),
            S("Why marks are gained", text="Both ideas are defined in one comparison with a conjunction, the key difference (flow against stock) is stated, and the link is explained."),
        ]),
        EX("Worked example 2: a two-part macroeconomics plan", intro="(a) Explain the causes of a persistent current account deficit. (b) Discuss the short-term and long-term measures a government could use to reduce it.", steps=[
            S("(a) Define", text="A current account deficit: debits (imports of goods and services, income paid abroad) exceed credits."),
            S("(a) Causes", text="High domestic demand pulling in imports; falling export prices or volumes (cocoa, oil); low competitiveness from high costs or an overvalued rate; large profit and interest outflows."),
            S("(b) Short-term measures", text="Expenditure-reducing (higher taxes, lower spending, higher interest rates) and expenditure-switching (tariffs, quotas, devaluation where the country controls its exchange rate)."),
            S("(b) Long-term measures", text="Supply-side policies to raise productivity; export diversification and processing; import substitution; attracting FDI into export industries."),
            S("(b) Evaluate", text="Expenditure-reducing measures cost growth and jobs; protection invites retaliation; a CEMAC member cannot devalue alone; supply-side measures are slow. Conclude with the best combination."),
        ]),
        MISTAKE("Answering a different question", "The report saw candidates explain the uses of government revenue when asked for its sources, and the balance sheet of banks when asked about the balance of payments. Underline the key words of the question and check your plan against them."),
        MISTAKE("Stating points without explaining them", "Lists earn few marks. Each point needs a 'because' and an effect, and the report asked for short-term and long-term measures where the syllabus has both."),
        MISTAKE("Diagrams with wrong or missing labels", "Label both axes, every curve, the equilibrium and any shift. Refer to the diagram in your writing."),
        QUIZ("A question says: 'Explain the factors that will reduce the demand for imports in an economy.' Which answer is best?", ["Income affects imports", "A fall in national income reduces spending on imports", "Imports are goods bought from abroad", "A rise in income increases imports"], 1,
             "It names the factor, states it in the required direction (a fall) and gives the effect.", hint="Is the answer directional, in the direction asked?",
             feedback=["Not directional: it does not say which way.", "", "This is a definition, not a factor.", "This is the wrong direction for the question."]),
        QUIZ("How many Paper 2 essays must you answer, and what is the limit per section?", ["Eight; four per section", "Five; not more than three from a section", "Five; all from one section if you wish", "Three; one from each section"], 1,
             "The Board's 2023 report: answer five of eight, not more than three from either section.", hint="Recall the report's description of Paper 2.",
             feedback=["There are eight questions, but you answer five.", "", "Not more than three can come from one section.", "That describes Paper 3 (answer three)."]),
        TIP("Write the definitions first, then use one paragraph per point. For any 'distinguish' question use a conjunction in one sentence; for any directional question state each factor in that direction; for any named country apply each point to it.", title="Exam link"),
        PQ("Rewrite this weak answer to 'Distinguish between demand-pull and cost-push inflation': 'Demand-pull is caused by demand. Cost-push is caused by costs.'",
           "Demand-pull inflation is a sustained rise in the price level caused by aggregate demand growing faster than productive capacity (AD shifts right), whereas cost-push inflation is a sustained rise in the price level caused by rising costs of production such as wages, fuel or imported inputs (SRAS shifts left), so that output tends to rise in the first case but fall in the second."),
        PQ("Write a plan for: 'Discuss the effects of a cut in government spending on employment, the budget deficit and the current account.'",
           "Define the spending cut and the three variables. Employment: lower spending reduces AD and, through the multiplier, output and jobs (deflationary gap diagram); public sector jobs may be lost directly. Budget deficit: falls at first, but lower income reduces tax revenue (automatic stabilisers), so the deficit falls by less than the cut. Current account: lower income reduces imports, so the current account improves. Evaluation: size of the multiplier, which spending is cut (investment or current), the state of the economy, crowding in of private spending. Conclusion. (The question asks only about these three variables: keep to them.)"),
        PQ("List the parts of a good Paper 2 essay plan.",
           "Definitions of key terms; developed points each with mechanism, diagram if relevant and example; application to the named context; evaluation (conditions, short and long run, size, winners and losers); a conclusion that answers the question."),
        SUM("Paper 2: 8 essays in microeconomics and macroeconomics sections; answer five, not more than three from a section; 40% (Board's 2023 report).",
            "Read the command word; for 'distinguish' use a conjunction; for directional questions give one direction.",
            "Plan: definitions, developed points, diagrams, application, evaluation, conclusion.",
            "Draw and label diagrams correctly and refer to them.",
            "Answer the question asked and revise the whole syllabus, including national income, money and the balance of payments."),
    ],
))

# ------------------------------------------------------------------ Examination 3. Paper 3
LESSONS.append(lesson(
    module=M_EXAM,
    topic="Paper 3",
    title="Paper 3: applying economics to data, diagrams and passages",
    slug="ecu2-paper3-application",
    minutes=24,
    summary="How to answer the application questions of Economics Paper 3: reading tables with their units, calculating from schedules, interpreting diagrams, writing brief directional answers, using question tags and not copying the passage, with worked examples from typical data.",
    objectives=[
        "Describe the structure of Paper 3 from the Board's 2023 report",
        "Read tables and diagrams accurately, including units, and carry out calculations from them",
        "Write brief, directional answers that respect question tags and do not repeat the passage",
        "Plan time across three questions",
    ],
    key_concepts=["Data response", "Units", "Schedule", "Buffer stock", "Question tags", "Brief answers", "Interpretation"],
    blocks=[
        H("Introduction"),
        T("Paper 3 is worth **30%** of the A Level Economics examination. In 2023, according to the Board's report, it had **five questions** and candidates answered **any three**. The paper tests the ability to **apply principles and concepts**: "
          "questions give a table, a diagram or a short passage, followed by parts that ask you to calculate, identify, state, explain or list. The 2023 questions covered both microeconomics (price theory, integration of firms, the theory of the firm) "
          "and macroeconomics (the paradox of thrift, economic growth). In the KKEVO practice paper we set 150 minutes (a KKEVO practice setting)."),
        H("What the Board's report asks for"),
        KEY("Six habits that earn marks", "Each comes from the examiners' comments.", cards=[
            ["Read the units", "If a table is in '000 FCFA or thousands of tonnes, use those units in your answer."],
            ["Use the right words", "The market clears where quantity demanded equals quantity supplied, not where 'demand equals supply'."],
            ["Respect the tags", "'Two', 'four', 'state', 'list', 'from the diagram', 'in Cameroon', 'other than': each limits what you may write."],
            ["Be brief", "Paper 3 parts need short, precise answers, not essays."],
            ["Do not copy the passage", "When asked for 'other' factors, points already in the passage earn nothing: Paper 3 is not a reading comprehension."],
            ["Be directional", "'Factors that can increase saving' need factors stated in the increasing direction."],
        ]),
        H("Calculations from schedules"),
        EX("Worked example 1: a market schedule and a buffer stock", intro="Price of cocoa ('000 FCFA per tonne) and quantities (tonnes), invented: at price 700, demand 260 and supply 260. After fertiliser use, supply at 700 rises to 410 while demand is unchanged. A producers' union wants to keep the price at 700 ('000 FCFA). (a) State the market price before fertiliser use. (b) How many tonnes must the union buy?", steps=[
            S("(a) Equilibrium", text="At 700 000 FCFA per tonne, quantity demanded equals quantity supplied (260 tonnes). Answer with the unit: 700 ('000 FCFA), that is 700 000 FCFA per tonne."),
            S("(b) Excess supply at the target price", math=r"410 - 260 = 150 \text{ tonnes}"),
            S("Why", text="To hold the price at 700, the union must buy the surplus that the market would not take at that price. Using 410 or 260 alone (the total supply or demand) is a common error."),
        ], check=r"260 + 150 = 410"),
        EX("Worked example 2: national income data", intro="A table gives (billion FCFA): consumption 12 000, investment 3 000, government spending 2 500, exports 4 000, imports 4 500. Calculate (a) GDP at market prices by the expenditure method and (b) total final expenditure (TFE).", steps=[
            S("(a) GDP", math=r"C + I + G + (X - M) = 12\,000 + 3000 + 2500 + 4000 - 4500 = 17\,000"),
            S("(b) TFE", math=r"C + I + G + X = 12\,000 + 3000 + 2500 + 4000 = 21\,500", text="TFE includes exports and does not subtract imports; the report noted that candidates confused TFE with GDP."),
        ], check=r"21\,500 - 4500 = 17\,000"),
        H("Reading diagrams"),
        T("Paper 3 diagrams (a Keynesian cross for the paradox of thrift, a chart of integration of firms, long-run cost and revenue curves) need you to **identify** what is shown and **justify** it from the diagram. "
          "For example, a consumption line with a positive intercept that rises with income has an **autonomous** part (the intercept, spending that does not depend on income) and an **induced** part (the slope, spending that rises with income). "
          "Say what in the diagram proves your answer."),
        H("Using your time"),
        T("Read all five questions and choose three where you can do every part. Note the tags in each part. Do the calculations carefully, showing a line of working with units. Keep answers short and move on; return to unfinished parts at the end."),
        MISTAKE("Ignoring the units of a table", "Writing '600 FCFA' when the table is in '000 FCFA loses accuracy marks. Copy the unit from the table heading."),
        MISTAKE("Giving general points when the question is specific", "If asked for factors that can increase the supply of cocoa, link each factor to cocoa (for example 'better weather in the cocoa-growing regions'), not to goods in general."),
        QUIZ("At a support price, quantity supplied is 520 tonnes and quantity demanded is 380 tonnes. How much must a buffer stock agency buy to hold the price?", ["520 tonnes", "380 tonnes", "140 tonnes", "900 tonnes"], 2,
             "The agency buys the excess supply: 520 − 380 = 140 tonnes.", hint="What does the market leave unsold at that price?",
             feedback=["That is total supply; consumers still buy 340.", "That is what consumers buy.", "", "That adds the two quantities."]),
        QUIZ("A question asks: 'State two OTHER factors, apart from those in the passage, that are sources of economic growth.' The passage mentions new machinery and better schooling. Which answer is acceptable?", ["New machinery and better schooling", "Technological progress and discovery of new natural resources", "Better schooling and technology", "Growth is caused by many factors"], 1,
             "Both are new sources not mentioned in the passage, stated clearly.", hint="Read the tag 'other'.",
             feedback=["These are in the passage, so they score nothing.", "", "Schooling is in the passage, so only one of the two points can count.", "Too vague: no factor is named."]),
        TIP("Paper 3 rewards accuracy and economy. Show working with units for calculations, identify from the diagram when asked, keep each answer to the point, and never repeat what the passage already gives.", title="Exam link"),
        PQ("A table (in '000 FCFA) shows: price 400, quantity demanded 50, quantity supplied 30; price 500, quantity demanded 40, quantity supplied 40; price 600, quantity demanded 30, quantity supplied 50. State and justify the equilibrium price.",
           "500 ('000 FCFA), that is 500 000 FCFA, because at this price quantity demanded equals quantity supplied (40 units)."),
        PQ("A diagram shows the consumption function C = 200 + 0.75Y. Use it to identify autonomous and induced consumption.",
           "Autonomous consumption is 200: spending that takes place even when income is zero (the intercept on the vertical axis). Induced consumption is 0.75Y: consumption rises by 0.75 for each extra unit of income (the slope, the MPC)."),
        PQ("State four factors that can increase the volume of exports from Cameroon.",
           "Any four, each in the increasing direction: a rise in world demand and prices for Cameroon's products; higher productivity and lower costs of export producers; better roads, ports and power lowering transport and production costs; processing raw materials locally to sell higher-value goods; access to new markets through AfCFTA; export promotion and finance for exporters; faster customs procedures."),
        SUM("Paper 3: five application questions, answer any three, 30% of the examination (Board's 2023 report).",
            "Read units and use them; the market clears where quantity demanded equals quantity supplied.",
            "Respect tags: number of points, 'other', 'from the diagram', 'in Cameroon', direction.",
            "Keep answers brief; show calculations with units; justify from the diagram.",
            "Never repeat points given in the passage."),
    ],
))

# --- END OF LESSONS ---
