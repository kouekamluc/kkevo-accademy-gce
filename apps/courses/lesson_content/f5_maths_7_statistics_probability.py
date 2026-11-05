"""Form 5 General Mathematics (GCE O Level 570): Statistics & Probability.

Topic "Grouped data": three lessons. Topic "Probability": three lessons.
"""
from .dsl import *  # noqa: F403

COURSE = ("mathematics", "form-5")

M = "Statistics & Probability"
GD = "Grouped data"
PR = "Probability"

LESSONS = [
    # ------------------------------------------------------------------ Grouped data 1
    lesson(
        module=M,
        topic=GD,
        title="Grouped frequency tables, modal class and estimated mean",
        slug="grouped-frequency-modal-class-estimated-mean",
        minutes=20,
        summary="Read grouped frequency tables, find class boundaries, mid-values and the modal class, and estimate the mean with Σfx ÷ Σf.",
        objectives=[
            "Find the class boundaries, class width and mid-value of a class",
            "State the modal class of a grouped frequency table",
            "Estimate the mean of grouped data using mid-values",
            "Explain why the mean of grouped data is only an estimate",
        ],
        key_concepts=["Grouped frequency table", "Class boundaries", "Class width", "Mid-value",
                      "Modal class", "Estimated mean"],
        blocks=[
            H("Introduction"),
            T("A school in Bamenda asks 40 students how long they take to travel to school. It gets 40 different "
              "numbers. A long list like that is hard to read."),
            T("So we put the data into **classes** (groups) and count how many values fall in each class. "
              "The result is a **grouped frequency table**. In this lesson you will read such a table, find its "
              "modal class and estimate its mean."),
            KEY("Journey times of 40 students", "Each journey time $t$ is in minutes. The number of students in a class is its frequency.",
                cards=[[r"$0 < t \le 10$", "4"], [r"$10 < t \le 20$", "10"], [r"$20 < t \le 30$", "14"],
                       [r"$30 < t \le 40$", "8"], [r"$40 < t \le 50$", "4"]],
                note="Total frequency: 4 + 10 + 14 + 8 + 4 = 40."),
            H("Class boundaries, width and mid-value"),
            D(r"The **class boundaries** are the values where one class ends and the next begins. "
              r"The **class width** is upper boundary minus lower boundary. The **mid-value** (mid-point) is halfway "
              r"between the two boundaries.", title="Describing a class",
              formula=r"\text{mid-value} = \frac{\text{lower boundary} + \text{upper boundary}}{2}"),
            T(r"For $20 < t \le 30$ the boundaries are 20 and 30, the width is 10 and the mid-value is 25."),
            T("When the data are **whole numbers**, classes are often written like 11–20, 21–30. There is a gap of 1 "
              "between 20 and 21, so the boundaries are halfway across the gap: the class 11–20 has boundaries 10.5 and "
              "20.5. Its width is $20.5 - 10.5 = 10$ and its mid-value is $15.5$."),
            QUIZ("Test scores are whole numbers grouped as 21–30, 31–40, and so on. What is the mid-value of the class 21–30?",
                 ["$25.5$", "$25$", "$9$", "$20.5$"], 0,
                 r"The boundaries are 20.5 and 30.5, so the mid-value is $(20.5 + 30.5) \div 2 = 25.5$. "
                 r"You get the same answer from $(21 + 30) \div 2$.",
                 hint="Add the two ends of the class and halve.",
                 feedback=["", "25 is halfway between 20 and 30. The class runs from 21 to 30, so its middle is 25.5.",
                           "9 is $30 - 21$. That is not the mid-value; and the class width is actually 10.",
                           "20.5 is the lower class boundary, not the middle of the class."]),
            H("Modal class and estimated mean"),
            D("The **modal class** is the class with the highest frequency.", title="Modal class",
              note="Give the class itself, not the frequency."),
            D(r"Inside a class we do not know the exact values, so we pretend every value is at the mid-value $x$. "
              r"Multiply each mid-value by its frequency $f$, add, and divide by the total frequency.",
              title="Estimated mean of grouped data",
              formula=r"\bar{x} \approx \frac{\sum fx}{\sum f}"),
            EX("Worked example 1: journey times", intro="Estimate the mean journey time for the 40 students and state the modal class.",
               steps=[
                   S("Mid-values", text="The mid-values are 5, 15, 25, 35 and 45."),
                   S("Multiply each mid-value by its frequency", math=r"5(4) = 20,\ 15(10) = 150,\ 25(14) = 350,\ 35(8) = 280,\ 45(4) = 180"),
                   S("Add the products", math=r"\sum fx = 20 + 150 + 350 + 280 + 180 = 980"),
                   S("Divide by the total frequency", math=r"\bar{x} \approx \frac{980}{40} = 24.5 \text{ minutes}"),
                   S("Modal class", text=r"The highest frequency is 14, so the modal class is $20 < t \le 30$."),
               ]),
            EX("Worked example 2: whole-number classes", intro=(
                "The scores of 50 students in a test were: 1–10: 4 students, 11–20: 9, 21–30: 15, 31–40: 13, 41–50: 9. "
                "Estimate the mean score."),
               steps=[
                   S("Mid-values", text="(1 + 10) ÷ 2 = 5.5, then 15.5, 25.5, 35.5 and 45.5."),
                   S("Products fx", math=r"22,\quad 139.5,\quad 382.5,\quad 461.5,\quad 409.5"),
                   S("Totals", math=r"\sum f = 50, \qquad \sum fx = 1415"),
                   S("Estimated mean", math=r"\bar{x} \approx \frac{1415}{50} = 28.3"),
               ]),
            T("Why only an **estimate**? Four students scored somewhere from 1 to 10, but we used 5.5 for all of them. "
              "Some real scores are above the mid-value and some below, so the answer is close to the true mean but "
              "probably not exactly equal to it."),
            EX("Worked example 3: a missing frequency", intro=(
                r"A farmer in Foumbot weighs bags of tomatoes (kg): $0 < m \le 10$: 3, $10 < m \le 20$: $k$, "
                r"$20 < m \le 30$: 7, $30 < m \le 40$: 5. The estimated mean is 22 kg. Find $k$."),
               steps=[
                   S("Total frequency", math=r"\sum f = 3 + k + 7 + 5 = 15 + k"),
                   S("Sum of fx with mid-values 5, 15, 25, 35", math=r"\sum fx = 15 + 15k + 175 + 175 = 365 + 15k"),
                   S("Set up the equation", math=r"\frac{365 + 15k}{15 + k} = 22"),
                   S("Solve", math=r"365 + 15k = 330 + 22k \;\Rightarrow\; 35 = 7k \;\Rightarrow\; k = 5"),
               ], check=r"\frac{365 + 75}{20} = \frac{440}{20} = 22"),
            MISTAKE("Dividing by the number of classes", r"The mean is $\sum fx \div \sum f$ (the total frequency, 40 above), not $\sum fx$ divided by 5 classes."),
            MISTAKE("Using a class boundary instead of the mid-value", r"Using the upper boundaries (10, 20, 30 …) makes the mean too big. Always use the middle of each class."),
            MISTAKE("Giving the frequency as the modal class", "If the highest frequency is 14, the modal class is the class with 14 students, not the number 14."),
            QUIZ(r"Daily sales of 20 traders (thousands of FCFA): $0 < s \le 4$: 5, $4 < s \le 8$: 10, $8 < s \le 12$: 5. Estimate the mean.",
                 ["$6$", "$40$", "$120$", "$8$"], 0,
                 r"Mid-values 2, 6, 10. $\sum fx = 10 + 60 + 50 = 120$ and $\sum f = 20$, so $\bar{x} \approx 120 \div 20 = 6$ thousand FCFA.",
                 hint=r"Find the mid-values, then $\sum fx$ and $\sum f$.",
                 feedback=["", r"You divided 120 by the 3 classes. Divide by the total frequency, 20.",
                           r"120 is $\sum fx$. You still need to divide by $\sum f = 20$.",
                           r"You used the upper boundaries 4, 8, 12, giving $160 \div 20 = 8$. Use the mid-values."]),
            H("Practice questions"),
            PQ("The marks of 40 students are: 0–20: 3, 20–40: 7, 40–60: 15, 60–80: 10, 80–100: 5. (a) State the modal class. (b) Estimate the mean mark.",
               r"(a) The modal class is 40–60 (frequency 15). (b) Mid-values: 10, 30, 50, 70, 90. "
               r"$\sum fx = 30 + 210 + 750 + 700 + 450 = 2140$. Mean $\approx 2140 \div 40 = 53.5$ marks."),
            PQ("The ages of 40 people at a youth meeting in Limbe are: 10–14: 6, 15–19: 14, 20–24: 12, 25–29: 8. (a) Write down the class boundaries and the width of the class 15–19. (b) Estimate the mean age.",
               r"(a) Boundaries 14.5 and 19.5; width $19.5 - 14.5 = 5$. (b) Mid-values 12, 17, 22, 27. "
               r"$\sum fx = 72 + 238 + 264 + 216 = 790$. Mean $\approx 790 \div 40 = 19.75$ years."),
            PQ(r"The lengths of 20 planks (m) are: $0 < l \le 5$: 6, $5 < l \le 15$: 10, $15 < l \le 30$: 4. The classes have different widths. Estimate the mean length.",
               r"Mid-values 2.5, 10 and 22.5. $\sum fx = 15 + 100 + 90 = 205$. Mean $\approx 205 \div 20 = 10.25$ m. "
               r"Unequal widths do not change the method: always use the middle of each class."),
            PQ("Explain why the mean worked out from a grouped frequency table is called an estimated mean.",
               "The original values are lost when the data are grouped. We assume that every value in a class equals the "
               "class mid-value, which is usually not exactly true, so the result is only approximately the true mean."),
            SUM("Class boundaries mark where classes meet; for whole numbers like 11–20 they are 10.5 and 20.5.",
                "Class width = upper boundary − lower boundary; mid-value = halfway between the boundaries.",
                "The modal class is the class with the highest frequency.",
                r"Estimated mean $= \sum fx \div \sum f$, using mid-values for $x$.",
                "It is only an estimate because each value is replaced by its class mid-value."),
        ],
    ),
    # ------------------------------------------------------------------ Grouped data 2
    lesson(
        module=M,
        topic=GD,
        title="Histograms with equal and unequal class widths",
        slug="histograms-equal-unequal-class-widths",
        minutes=20,
        summary="Draw histograms for grouped data, use frequency density when class widths are unequal, and read frequencies back from the areas of the bars.",
        objectives=[
            "Draw a histogram for classes of equal width",
            "Calculate frequency density and use it for classes of unequal width",
            "Read frequencies back from a histogram using area = frequency",
            "Estimate how many values lie in part of a class",
        ],
        key_concepts=["Histogram", "Class width", "Frequency density", "Area of a bar", "Unequal class widths"],
        blocks=[
            H("Introduction"),
            T("In the previous lesson you summarised grouped data with a modal class and an estimated mean. "
              "A **histogram** shows the same data as a picture, so you can see at a glance where most values lie."),
            T("A histogram looks like a bar chart, but there are two important differences. The bars touch, because the "
              "data are continuous. And the **area** of each bar, not just its height, stands for the frequency."),
            H("Equal class widths"),
            T("When all classes have the same width, every bar is equally wide. Then area is proportional to height, so "
              "you may simply plot **frequency** on the vertical axis."),
            IMG("f5m-histogram-journey-times.svg",
                "Histogram of journey times of 40 students. Five touching bars of width 10 minutes from 0 to 50. Heights: 4, 10, 14, 8 and 4. The tallest bar is 20 to 30 minutes.",
                "Figure 1. Journey times from the previous lesson: equal widths, so the height is the frequency."),
            T("The tallest bar, 20 to 30 minutes, is the modal class. The bars rise and then fall, so most journeys "
              "take between 10 and 40 minutes."),
            H("Unequal class widths and frequency density"),
            T("Sometimes classes have different widths. If we used frequency as the height, a wide class would look far "
              "too important, because its bar would have a large area. So we use **frequency density**."),
            D("For each class, divide the frequency by the class width. Plot frequency density on the vertical axis. "
              "Then the area of each bar equals its frequency.", title="Frequency density",
              formula=r"\text{frequency density} = \frac{\text{frequency}}{\text{class width}}",
              note=r"Turned round: $\text{frequency} = \text{frequency density} \times \text{class width}$ (area of the bar)."),
            EX("Worked example 1: unequal class widths", intro=(
                "The daily earnings of 45 moto-taxi drivers, in thousands of FCFA, are grouped as follows: 0–2: 6 drivers, 2–3: 9 drivers, "
                "3–4: 12 drivers, 4–6: 10 drivers, 6–10: 8 drivers. Find the frequency density of each class and describe the histogram."),
               steps=[
                   S("Class widths", text="The widths are 2, 1, 1, 2 and 4."),
                   S("Divide each frequency by its width", math=r"\tfrac{6}{2} = 3,\quad \tfrac{9}{1} = 9,\quad \tfrac{12}{1} = 12,\quad \tfrac{10}{2} = 5,\quad \tfrac{8}{4} = 2"),
                   S("Draw the bars", text="Earnings on the horizontal axis, frequency density on the vertical axis. The bar for 0–2 is 2 units wide and 3 units tall. The bar for 6–10 is 4 units wide but only 2 units tall."),
               ], check=r"3 \times 2 + 9 \times 1 + 12 \times 1 + 5 \times 2 + 2 \times 4 = 45"),
            IMG("f5-histogram-earnings.svg",
                "Histogram of daily earnings in thousands of FCFA, with no gaps between bars. Bar 0 to 2 has frequency density 3, bar 2 to 3 has 9, bar 3 to 4 has 12, bar 4 to 6 has 5 and bar 6 to 10 has 2. The frequencies 6, 9, 12, 10 and 8 are written inside the bars.",
                "Figure 2. Worked example 1: bar height is frequency density, so the wide 6–10 class is only 2 units tall."),
            QUIZ(r"A class $10 < x \le 25$ has a frequency of 30. What is its frequency density?",
                 ["$2$", "$3$", "$1.2$", "$450$"], 0,
                 r"The class width is $25 - 10 = 15$, so the frequency density is $30 \div 15 = 2$.",
                 hint="Work out the class width first.",
                 feedback=["", "You divided by 10, the lower boundary. Divide by the class width, 15.",
                           "You divided by the upper boundary, 25. Divide by the width.",
                           "You multiplied by the width instead of dividing."]),
            H("Reading frequencies back from a histogram"),
            T("To get a frequency from a histogram, find the **area** of the bar: frequency density times class width."),
            EX("Worked example 2: reading Figure 2", intro=(
                "Use the histogram of earnings. (a) How many drivers earned between 3 and 6 thousand FCFA? "
                "(b) Estimate how many earned between 5 and 8 thousand FCFA."),
               steps=[
                   S("(a) Areas of the bars 3–4 and 4–6", math=r"12 \times 1 + 5 \times 2 = 12 + 10 = 22 \text{ drivers}"),
                   S("(b) Part of the 4–6 bar: from 5 to 6", math=r"5 \times 1 = 5",
                     text="We assume the drivers are spread evenly inside each class."),
                   S("(b) Part of the 6–10 bar: from 6 to 8", math=r"2 \times 2 = 4"),
                   S("(b) Add", math=r"5 + 4 = 9 \text{ drivers (an estimate)}"),
               ]),
            EX("Worked example 3: a histogram with no scale", intro=(
                "In a histogram of the ages of people at a clinic in Bafoussam, the bar for the class 10–20 years is 4 cm tall and "
                "stands for 20 people. The bar for 20–25 years is 6 cm tall. How many people are in the class 20–25?"),
               steps=[
                   S("Area of the first bar", math=r"10 \times 4 = 40 \text{ units for 20 people}"),
                   S("One person is", math=r"40 \div 20 = 2 \text{ units of area}"),
                   S("Area of the second bar", math=r"5 \times 6 = 30 \text{ units}"),
                   S("Number of people", math=r"30 \div 2 = 15"),
               ]),
            MISTAKE("Using frequency as the height with unequal widths", "With unequal class widths the height must be frequency density, or wide classes will look far too important."),
            MISTAKE("Reading the height as the frequency", "On a frequency-density histogram the height is not the frequency. Multiply the height by the class width."),
            MISTAKE("Leaving gaps between the bars", "The classes meet at their boundaries, so the bars must touch."),
            QUIZ("Classes 0–10, 10–15 and 15–30 have frequencies 20, 15 and 30. Which class has the tallest bar in a correct histogram?",
                 ["$15$–$30$", "$10$–$15$", "$0$–$10$", "All three are the same height"], 1,
                 r"Frequency densities: $20 \div 10 = 2$, $15 \div 5 = 3$, $30 \div 15 = 2$. The class 10–15 has the tallest bar.",
                 hint="Work out the frequency density of each class.",
                 feedback=["This class has the highest frequency, but it is 15 wide, so its density is only 2.", "",
                           r"Its density is $20 \div 10 = 2$, less than the 3 for 10–15.",
                           "Two classes have density 2, but 10–15 has density 3."]),
            H("Practice questions"),
            PQ("In a histogram, the bar for the class 20–30 has a frequency density of 1.6. (a) Find its frequency. (b) Another class, 30–35, has a frequency of 12. Find the height of its bar.",
               r"(a) Frequency $=$ frequency density $\times$ width $= 1.6 \times 10 = 16$. (b) Frequency density $= 12 \div 5 = 2.4$."),
            PQ("The ages of 66 patients are: 0–10: 12, 10–15: 9, 15–25: 20, 25–45: 16, 45–75: 9. Calculate the frequency density of each class.",
               r"Widths 10, 5, 10, 20, 30. Densities: $12 \div 10 = 1.2$, $9 \div 5 = 1.8$, $20 \div 10 = 2$, $16 \div 20 = 0.8$, $9 \div 30 = 0.3$."),
            PQ("Use Figure 2 (earnings of moto-taxi drivers). How many drivers earned more than 4 thousand FCFA?",
               r"Bars 4–6 and 6–10: $5 \times 2 + 2 \times 4 = 10 + 8 = 18$ drivers."),
            PQ("In a histogram, the bar for 0–5 kg is 3 cm tall and represents 30 bags. The bar for 5–15 kg is 2 cm tall. How many bags does it represent?",
               r"First bar: area $5 \times 3 = 15$ units for 30 bags, so 1 unit $= 2$ bags. Second bar: area $10 \times 2 = 20$ units, so $20 \times 2 = 40$ bags."),
            SUM("A histogram has touching bars, and the area of each bar shows the frequency.",
                "With equal class widths you may plot frequency as the height.",
                "With unequal class widths, plot frequency density = frequency ÷ class width.",
                "To read a frequency back, find the area: frequency density × class width.",
                "For part of a class, assume the values are spread evenly and take that part of the area."),
        ],
    ),
    # ------------------------------------------------------------------ Grouped data 3
    lesson(
        module=M,
        topic=GD,
        title="Cumulative frequency, median and quartiles",
        slug="cumulative-frequency-median-quartiles",
        minutes=25,
        summary="Build a cumulative frequency table, draw an ogive, and use it to estimate the median, quartiles, interquartile range and how many values lie above or below a given value.",
        objectives=[
            "Build a cumulative frequency table from a grouped frequency table",
            "Draw a cumulative frequency curve (ogive) using upper class boundaries",
            "Estimate the median, quartiles and interquartile range from an ogive",
            "Answer questions such as how many values are more than a given value",
        ],
        key_concepts=["Cumulative frequency", "Upper class boundary", "Ogive", "Median", "Lower quartile",
                      "Upper quartile", "Interquartile range"],
        blocks=[
            H("Introduction"),
            T("The headteacher in Bamenda now asks: what is a typical journey time, and how many students travel for more "
              "than 35 minutes? The mean from the first lesson cannot answer the second question."),
            T("A **cumulative frequency curve**, also called an **ogive**, answers both. In this lesson we use the same 40 "
              "journey times: 4, 10, 14, 8 and 4 students in the classes 0–10, 10–20, 20–30, 30–40 and 40–50 minutes."),
            H("Cumulative frequency"),
            D("The **cumulative frequency** up to a value is the number of data values less than or equal to it. "
              "It is a running total of the frequencies.", title="Cumulative frequency"),
            KEY("Cumulative frequency table", "Keep adding the next frequency: 4, then 4 + 10 = 14, then 14 + 14 = 28, and so on.",
                cards=[[r"$t \le 10$", "4"], [r"$t \le 20$", "14"], [r"$t \le 30$", "28"],
                       [r"$t \le 40$", "36"], [r"$t \le 50$", "40"]],
                note="The last cumulative frequency always equals the total frequency, 40."),
            H("Drawing the ogive"),
            T("Plot each cumulative frequency against the **upper class boundary** of its class: (10, 4), (20, 14), "
              "(30, 28), (40, 36) and (50, 40). Also plot (0, 0), because no student took 0 minutes or less."),
            T("Join the points with a smooth curve. It rises slowly, then steeply through the busiest class, then slowly "
              "again: a stretched S-shape."),
            D("With $n$ values, read across from these cumulative frequencies to the curve, then down to the horizontal axis.",
              title="Median and quartiles from an ogive",
              formula=r"Q_1 \text{ at } \tfrac{1}{4}n, \qquad \text{median at } \tfrac{1}{2}n, \qquad Q_3 \text{ at } \tfrac{3}{4}n",
              note=r"The **interquartile range** is $Q_3 - Q_1$. It measures the spread of the middle half of the data."),
            EX("Worked example 1: median and quartiles", intro="Estimate the median, the quartiles and the interquartile range of the journey times.",
               steps=[
                   S("Find the positions", math=r"\tfrac{1}{4}(40) = 10,\quad \tfrac{1}{2}(40) = 20,\quad \tfrac{3}{4}(40) = 30"),
                   S("Median: the 20th value lies in 20–30 (cumulative 14 to 28)", math=r"20 + \frac{20 - 14}{14} \times 10 \approx 24.3 \text{ min}",
                     text="This is the reading from a straight line between (20, 14) and (30, 28). A smooth curve gives a value close to it."),
                   S("Lower quartile: the 10th value lies in 10–20 (cumulative 4 to 14)", math=r"Q_1 = 10 + \frac{10 - 4}{10} \times 10 = 16 \text{ min}"),
                   S("Upper quartile: the 30th value lies in 30–40 (cumulative 28 to 36)", math=r"Q_3 = 30 + \frac{30 - 28}{8} \times 10 = 32.5 \text{ min}"),
                   S("Interquartile range", math=r"Q_3 - Q_1 = 32.5 - 16 = 16.5 \text{ min}"),
               ]),
            IMG("f5-ogive-journey-times.svg",
                "Cumulative frequency curve of journey times, a stretched S-shape through the points (0, 0), (10, 4), (20, 14), (30, 28), (40, 36) and (50, 40). Dashed lines read across from cumulative frequencies 10, 20 and 30 to the curve and down to the time axis at 16, 24.3 and 32.5 minutes.",
                "Figure 1. Reading the ogive: Q₁ = 16 min, median ≈ 24.3 min and Q₃ = 32.5 min."),
            QUIZ("An ogive is drawn for the scores of 80 students. At which cumulative frequency should you read across to estimate the upper quartile?",
                 ["$40$", "$75$", "$60$", "$20$"], 2,
                 r"The upper quartile is at $\tfrac{3}{4}n = \tfrac{3}{4} \times 80 = 60$.",
                 hint="The upper quartile is three quarters of the way through the data.",
                 feedback=["40 is half of 80, which gives the median.",
                           "75 is the percentage. Use three quarters of the total frequency, not 75 itself.", "",
                           "20 is a quarter of 80, which gives the lower quartile."]),
            H("How many more than a value?"),
            T("To find how many values are **less than** a value, read **up** from that value on the horizontal axis to the "
              "curve, then across to the cumulative frequency. For **more than**, subtract that reading from the total."),
            EX("Worked example 2: reading up from the time axis", intro=(
                "Use the ogive for the 40 journey times. Estimate (a) how many students took 15 minutes or less, "
                "(b) how many took more than 35 minutes."),
               steps=[
                   S("(a) Read up from 15 minutes", math=r"4 + \frac{15 - 10}{10} \times 10 = 9 \text{ students}",
                     text="15 is halfway between 10 and 20, so the reading is about halfway between 4 and 14."),
                   S("(b) Read up from 35 minutes", math=r"28 + \frac{35 - 30}{10} \times 8 = 32",
                     text="About 32 students took 35 minutes or less."),
                   S("(b) Subtract from the total", math=r"40 - 32 = 8 \text{ students took more than 35 minutes}"),
               ]),
            EX("Worked example 3: from a table to answers", intro=(
                "The marks of 40 students are: 0–20: 3, 20–40: 7, 40–60: 15, 60–80: 10, 80–100: 5. "
                "(a) Find the cumulative frequencies. (b) Estimate the median and the interquartile range. "
                "(c) Students need more than 70 marks for a prize. Estimate how many get a prize."),
               steps=[
                   S("(a) Running totals", text="3, 10, 25, 35, 40, plotted at 20, 40, 60, 80 and 100, starting from (0, 0)."),
                   S("(b) Median at the 20th value (in 40–60, cumulative 10 to 25)", math=r"40 + \frac{20 - 10}{15} \times 20 \approx 53.3"),
                   S("(b) Quartiles at the 10th and 30th values", math=r"Q_1 = 40, \qquad Q_3 = 60 + \frac{30 - 25}{10} \times 20 = 70"),
                   S("(b) Interquartile range", math=r"70 - 40 = 30 \text{ marks}"),
                   S("(c) Read up from 70 marks", math=r"25 + \frac{70 - 60}{20} \times 10 = 30, \qquad 40 - 30 = 10 \text{ students}"),
               ]),
            MISTAKE("Plotting at mid-values", "Cumulative frequency is plotted at the **upper** class boundary, because by the end of the class all those values have been counted."),
            MISTAKE("Answering 'more than' with the reading itself", "The ogive gives how many are less than or equal to a value. For 'more than', subtract from the total."),
            MISTAKE("Subtracting cumulative frequencies for the IQR", r"The IQR is a difference of values on the horizontal axis, $Q_3 - Q_1$, not $\tfrac{3}{4}n - \tfrac{1}{4}n$."),
            QUIZ("An ogive for 60 traders shows that 48 of them sold 45 bags of rice or fewer in a month. How many sold more than 45 bags?",
                 ["$48$", "$12$", "$15$", "$105$"], 1,
                 r"The reading 48 counts traders with 45 bags or fewer. More than 45: $60 - 48 = 12$.",
                 hint="The ogive counts values up to 45. How do you get the rest?",
                 feedback=["48 is the number who sold 45 bags or fewer.", "",
                           r"You subtracted 45 (the number of bags) from 60. Subtract the cumulative frequency, 48.",
                           "You added. 'More than' means total minus the reading."]),
            H("Practice questions"),
            PQ("The masses of 50 bags of cocoa (kg) are: 0–10: 5, 10–20: 12, 20–30: 18, 30–40: 10, 40–50: 5. (a) Write down the cumulative frequencies. (b) Estimate the median.",
               r"(a) 5, 17, 35, 45, 50 at 10, 20, 30, 40, 50 kg. (b) Median at $\tfrac{1}{2}(50) = 25$, in 20–30: $20 + \frac{25 - 17}{18} \times 10 \approx 24.4$ kg."),
            PQ("For the cocoa bags, estimate (a) the interquartile range, (b) how many bags weigh more than 35 kg.",
               r"(a) $Q_1$ at 12.5: $10 + \frac{12.5 - 5}{12} \times 10 = 16.25$. $Q_3$ at 37.5: $30 + \frac{37.5 - 35}{10} \times 10 = 32.5$. "
               r"IQR $= 32.5 - 16.25 \approx 16.3$ kg. (b) Cumulative frequency at 35: $35 + \tfrac{1}{2}(10) = 40$, so $50 - 40 = 10$ bags."),
            PQ("From an ogive of the daily sales of 80 market traders (thousands of FCFA), reading across at 20, 40 and 60 gives 34, 41 and 47. State the median and find the interquartile range.",
               r"The median is the reading at $\tfrac{1}{2}(80) = 40$: 41 thousand FCFA. IQR $= Q_3 - Q_1 = 47 - 34 = 13$ thousand FCFA."),
            PQ("Use Figure 1. A quarter of the students took longer than a certain time. Estimate that time.",
               r"The top quarter lies above the upper quartile, so the time is $Q_3 = 32.5$ minutes."),
            SUM("Cumulative frequency is a running total; the last value equals the total frequency.",
                "Plot cumulative frequency at the upper class boundary, start at the lowest boundary with 0, and join with a smooth curve.",
                r"Read $Q_1$, the median and $Q_3$ at $\tfrac{1}{4}n$, $\tfrac{1}{2}n$ and $\tfrac{3}{4}n$.",
                r"Interquartile range $= Q_3 - Q_1$, the spread of the middle half.",
                "For 'more than' a value, read up from the value and subtract the reading from the total."),
        ],
    ),
    # ------------------------------------------------------------------ Probability 1
    lesson(
        module=M,
        topic=PR,
        title="Theoretical probability and sample spaces",
        slug="theoretical-probability-sample-spaces",
        minutes=20,
        summary="Calculate theoretical probabilities from equally likely outcomes, use P(not A) = 1 − P(A), and list outcomes or draw possibility diagrams for two coins, two dice or a coin and a die.",
        objectives=[
            "Calculate the probability of an event when all outcomes are equally likely",
            "Use P(not A) = 1 − P(A)",
            "List the sample space for two coins, or a coin and a die",
            "Use a possibility diagram to find probabilities for two dice",
        ],
        key_concepts=["Probability", "Outcome", "Event", "Equally likely outcomes", "Complementary events",
                      "Sample space", "Possibility diagram"],
        blocks=[
            H("Introduction"),
            T("Before a football match at the Omnisport Stadium, the referee tosses a coin. Each captain has the same chance "
              "of winning the toss. **Probability** puts a number on chances like this."),
            T(r"A probability is a number from 0 (impossible) to 1 (certain). An event with probability $\tfrac{1}{2}$ is "
              "as likely to happen as not. In this lesson you will calculate probabilities by counting outcomes."),
            D("An **outcome** is one possible result, such as getting a 4 on a die. An **event** is a set of outcomes, such "
              "as 'an even number'. Outcomes are **equally likely** when each has the same chance, as with a fair coin or "
              "a fair die.", title="Outcomes and events"),
            D("When all outcomes are equally likely, the **theoretical probability** of an event A is", title="Theoretical probability",
              formula=r"P(A) = \frac{\text{number of outcomes in } A}{\text{total number of possible outcomes}}",
              note=r"Every probability lies between 0 and 1: $0 \le P(A) \le 1$."),
            D("The event 'A does not happen' is the **complement** of A. Either A happens or it does not, so the two "
              "probabilities add up to 1.", title="Complementary events",
              formula=r"P(\text{not } A) = 1 - P(A)"),
            EX("Worked example 1: one bag, one pick", intro=(
                "A bag contains 5 red, 3 blue and 2 green balls. One ball is taken at random. Find (a) P(blue), (b) P(not green)."),
               steps=[
                   S("Count the total", math=r"5 + 3 + 2 = 10 \text{ balls, all equally likely}"),
                   S("(a) 3 of the 10 balls are blue", math=r"P(\text{blue}) = \frac{3}{10}"),
                   S("(b) Use the complement", math=r"P(\text{not green}) = 1 - \frac{2}{10} = \frac{8}{10} = \frac{4}{5}"),
               ], check=r"\text{Not green means red or blue: } \tfrac{5 + 3}{10} = \tfrac{4}{5}"),
            H("Sample spaces"),
            D("The **sample space** is the list of all possible outcomes. When two things happen, such as tossing two "
              "coins, list every pair in order.", title="Sample space"),
            T("For two coins the sample space is HH, HT, TH, TT. HT (head on the first coin, tail on the second) and TH are "
              "**different** outcomes, so there are 4 equally likely outcomes, not 3."),
            QUIZ("Two fair coins are tossed. What is the probability of getting one head and one tail?",
                 [r"$\tfrac{1}{3}$", r"$\tfrac{1}{4}$", r"$\tfrac{3}{4}$", r"$\tfrac{1}{2}$"], 3,
                 r"Two of the four outcomes, HT and TH, have one head and one tail: $\tfrac{2}{4} = \tfrac{1}{2}$.",
                 hint="List all four outcomes for two coins.",
                 feedback=["You treated 'one of each' as one outcome out of three. HT and TH are two different outcomes out of four.",
                           "You counted only HT. TH also has one head and one tail.",
                           "That is P(at least one head), which includes HH.", ""]),
            H("Possibility diagrams for two dice"),
            T(r"Two dice give $6 \times 6 = 36$ equally likely outcomes. A **possibility diagram** is a grid that shows them "
              "all. Here each cell shows the total of the two dice."),
            IMG("f5m-possibility-diagram-two-dice.svg",
                "A 6 by 6 grid. Columns are the first die from 1 to 6, rows are the second die from 1 to 6, and each cell shows the total. The five cells with total 8 are highlighted: (2, 6), (3, 5), (4, 4), (5, 3) and (6, 2).",
                "Figure 1. Possibility diagram for the total of two dice. Total 8 appears in 5 of the 36 cells."),
            EX("Worked example 2: two dice", intro="Two fair dice are thrown. Use Figure 1 to find (a) P(total 8), (b) P(a double), (c) P(total of 10 or more).",
               steps=[
                   S("(a) Count the cells showing 8", math=r"P(\text{total } 8) = \frac{5}{36}"),
                   S("(b) Doubles lie on the diagonal: (1, 1) to (6, 6)", math=r"P(\text{double}) = \frac{6}{36} = \frac{1}{6}"),
                   S("(c) Totals 10, 11, 12 appear in 3, 2 and 1 cells", math=r"P(\text{total} \ge 10) = \frac{3 + 2 + 1}{36} = \frac{6}{36} = \frac{1}{6}"),
               ]),
            EX("Worked example 3: a coin and a die", intro=(
                "A fair coin is tossed and a fair die is thrown. List the sample space and find P(a head and an even number)."),
               steps=[
                   S("List the outcomes", text=r"H1, H2, H3, H4, H5, H6, T1, T2, T3, T4, T5, T6: $2 \times 6 = 12$ outcomes."),
                   S("Outcomes with a head and an even number", text="H2, H4, H6: 3 outcomes."),
                   S("Probability", math=r"P = \frac{3}{12} = \frac{1}{4}"),
               ]),
            MISTAKE("Treating totals as equally likely", r"Two dice give 11 possible totals (2 to 12), but they are not equally likely. Use the 36 outcomes, so P(total 8) is $\tfrac{5}{36}$, not $\tfrac{1}{11}$."),
            MISTAKE("Counting HT and TH as one outcome", "Order matters when you list a sample space. (2, 6) and (6, 2) are different cells in the grid."),
            MISTAKE("A probability bigger than 1", "If your answer is more than 1 or negative, something has gone wrong. Check the total number of outcomes."),
            QUIZ("One letter is chosen at random from the word CAMEROON. What is the probability that it is O?",
                 [r"$\tfrac{1}{8}$", r"$\tfrac{1}{4}$", r"$\tfrac{2}{7}$", r"$\tfrac{1}{7}$"], 1,
                 r"There are 8 letters and 2 of them are O: $\tfrac{2}{8} = \tfrac{1}{4}$.",
                 hint="Count every letter, including repeated ones.",
                 feedback=["There are two O's in CAMEROON, not one.", "",
                           "There are 8 letters, not 7. Each letter, even a repeated one, is one outcome.",
                           "You counted only the 7 different letters and one O. Count all 8 letters and both O's."]),
            H("Practice questions"),
            PQ("A fair six-sided die is thrown once. Find (a) P(a prime number), (b) P(a number greater than 4), (c) P(not a 6).",
               r"(a) The primes are 2, 3 and 5: $\tfrac{3}{6} = \tfrac{1}{2}$. (b) 5 and 6: $\tfrac{2}{6} = \tfrac{1}{3}$. (c) $1 - \tfrac{1}{6} = \tfrac{5}{6}$."),
            PQ("Two fair dice are thrown. What is the probability that the total is 7?",
               r"A total of 7 comes from (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1): 6 of the 36 outcomes. P $= \tfrac{6}{36} = \tfrac{1}{6}$."),
            PQ("Cards numbered 1 to 20 are shuffled and one is drawn. Find the probability that the number is (a) a multiple of 3, (b) not a multiple of 3.",
               r"(a) 3, 6, 9, 12, 15, 18: $\tfrac{6}{20} = \tfrac{3}{10}$. (b) $1 - \tfrac{3}{10} = \tfrac{7}{10}$."),
            PQ(r"A bag contains 24 sweets. The probability of picking a red sweet is $\tfrac{3}{8}$. How many red sweets are in the bag?",
               r"Number of red sweets $= \tfrac{3}{8} \times 24 = 9$."),
            SUM(r"$P(A) = \dfrac{\text{outcomes in } A}{\text{total outcomes}}$ when outcomes are equally likely.",
                r"Probabilities lie from 0 (impossible) to 1 (certain).",
                r"$P(\text{not } A) = 1 - P(A)$.",
                "List a sample space in order: HT and TH are different outcomes.",
                "Two dice give 36 equally likely outcomes; a possibility diagram shows them all."),
        ],
    ),
    # ------------------------------------------------------------------ Probability 2
    lesson(
        module=M,
        topic=PR,
        title="Combined events: the OR and AND rules",
        slug="combined-events-or-and-rules",
        minutes=20,
        summary="Add probabilities of mutually exclusive events (the OR rule) and multiply probabilities of independent events (the AND rule), and decide which rule a question needs.",
        objectives=[
            "Recognise mutually exclusive events and use P(A or B) = P(A) + P(B)",
            "Recognise independent events and use P(A and B) = P(A) × P(B)",
            "Decide whether a question needs the OR rule or the AND rule",
            "Check answers against a list of outcomes or a possibility diagram",
        ],
        key_concepts=["Combined events", "Mutually exclusive events", "OR rule", "Independent events", "AND rule"],
        blocks=[
            H("Introduction"),
            T("In the previous lesson you found probabilities by listing and counting outcomes. Counting is slow when there "
              "are many outcomes, or when the outcomes are not equally likely, such as a bus being late."),
            T("Two rules let you combine probabilities you already know. One rule is for **OR**, the other for **AND**. "
              "The skill is deciding which rule fits."),
            H("The OR rule"),
            D("Two events are **mutually exclusive** if they cannot happen at the same time. On one throw of a die, "
              "'a 1' and 'a 6' are mutually exclusive.", title="Mutually exclusive events",
              formula=r"P(A \text{ or } B) = P(A) + P(B)",
              note="Use this addition only when A and B cannot happen together."),
            EX("Worked example 1: adding probabilities", intro=(
                "A spinner can land on red, blue, green or yellow. P(red) = 0.25 and P(blue) = 0.4. "
                "Find (a) P(red or blue), (b) P(neither red nor blue)."),
               steps=[
                   S("One spin cannot be both colours", text="Red and blue are mutually exclusive, so add."),
                   S("(a) OR rule", math=r"P(\text{red or blue}) = 0.25 + 0.4 = 0.65"),
                   S("(b) Complement", math=r"P(\text{neither}) = 1 - 0.65 = 0.35"),
               ]),
            T(r"Be careful. On a die, 'even' $\{2, 4, 6\}$ and 'greater than 3' $\{4, 5, 6\}$ can happen together (4 or 6). "
              r"Adding gives $\tfrac{3}{6} + \tfrac{3}{6} = 1$, which is wrong, because 4 and 6 are counted twice. List the "
              r"outcomes instead: $\{2, 4, 5, 6\}$, so the probability is $\tfrac{4}{6} = \tfrac{2}{3}$."),
            QUIZ("A die is thrown once. Which pair of events is mutually exclusive?",
                 ["An even number; a number greater than 3", "A 2; an odd number",
                  "A prime number; an even number", "A number less than 3; an odd number"], 1,
                 "2 is even, so a 2 and an odd number can never happen on the same throw.",
                 hint="For each pair, look for one number that belongs to both events.",
                 feedback=["4 and 6 are both even and greater than 3, so both events can happen together.", "",
                           "2 is prime and even, so both events can happen together.",
                           "1 is less than 3 and odd, so both events can happen together."]),
            H("The AND rule"),
            D("Two events are **independent** if one happening does not change the probability of the other. Two coin "
              "tosses are independent: the coin has no memory.", title="Independent events",
              formula=r"P(A \text{ and } B) = P(A) \times P(B)",
              note="Use this multiplication only when A and B are independent."),
            EX("Worked example 2: a coin and a die", intro="A fair coin is tossed and a fair die is thrown. Find P(a head and a 6).",
               steps=[
                   S("The coin does not affect the die", text="The events are independent, so multiply."),
                   S("AND rule", math=r"P(\text{H and } 6) = \frac{1}{2} \times \frac{1}{6} = \frac{1}{12}"),
               ], check=r"\text{Of the 12 outcomes H1 to T6, only H6 works: } \tfrac{1}{12}"),
            EX("Worked example 3: maize seeds", intro=(
                "The probability that a maize seed germinates is 0.7. A farmer near Bafia plants two seeds, which germinate "
                "independently. Find the probability that (a) both germinate, (b) neither germinates, "
                "(c) the first germinates and the second does not."),
               steps=[
                   S("(a) Both", math=r"0.7 \times 0.7 = 0.49"),
                   S("(b) P(a seed does not germinate) = 0.3", math=r"0.3 \times 0.3 = 0.09"),
                   S("(c) First yes, second no", math=r"0.7 \times 0.3 = 0.21"),
               ]),
            T(r"You can check the AND rule with the possibility diagram from the previous lesson. P(both dice even) "
              r"$= \tfrac{1}{2} \times \tfrac{1}{2} = \tfrac{1}{4}$, and the grid has $3 \times 3 = 9$ such cells out of 36: "
              r"$\tfrac{9}{36} = \tfrac{1}{4}$."),
            KEY("Choosing the rule", "Read the question for the key word, then check the condition.",
                cards=[["OR: add", r"Events that **cannot happen together** (mutually exclusive): $P(A) + P(B)$."],
                       ["AND: multiply", r"Events that **do not affect each other** (independent): $P(A) \times P(B)$."]]),
            QUIZ("Two fair coins are tossed. What is the probability of getting two heads?",
                 [r"$\tfrac{1}{2}$", r"$\tfrac{1}{4}$", r"$\tfrac{1}{3}$", r"$1$"], 1,
                 r"The coins are independent: $\tfrac{1}{2} \times \tfrac{1}{2} = \tfrac{1}{4}$. The four outcomes are HH, HT, TH, TT.",
                 hint="You need a head AND a head. Which rule is that?",
                 feedback=["That is the probability for one coin. For two heads you need head AND head, so multiply.", "",
                           "There are four equally likely outcomes, not three: HT and TH are different.",
                           r"You added $\tfrac{1}{2} + \tfrac{1}{2}$. Use 'and': multiply."]),
            MISTAKE("Adding for AND", r"Two sixes on two dice is $\tfrac{1}{6} \times \tfrac{1}{6} = \tfrac{1}{36}$, not $\tfrac{1}{6} + \tfrac{1}{6}$. AND means multiply."),
            MISTAKE("Adding events that overlap", "Only add when the events cannot happen together. If they overlap, list the outcomes."),
            MISTAKE("Multiplying when events affect each other", "Taking two balls from a bag without putting the first back is not independent: the second probability changes. The next lesson shows how to handle this."),
            H("Practice questions"),
            PQ("Events A and B are mutually exclusive, with P(A) = 0.3 and P(B) = 0.45. Find (a) P(A or B), (b) P(neither A nor B).",
               r"(a) $0.3 + 0.45 = 0.75$. (b) $1 - 0.75 = 0.25$."),
            PQ("The probability that Ngum passes Mathematics is 0.8 and the probability that she passes English is 0.6. The events are independent. Find the probability that she (a) passes both, (b) fails both.",
               r"(a) $0.8 \times 0.6 = 0.48$. (b) $0.2 \times 0.4 = 0.08$."),
            PQ("A bag has 3 red and 2 blue counters. A counter is taken, its colour noted, and it is put back. A second counter is then taken. Find P(red then blue).",
               r"The first counter is put back, so the picks are independent: $\tfrac{3}{5} \times \tfrac{2}{5} = \tfrac{6}{25}$."),
            PQ("A fair die is thrown twice. Find the probability that the first throw is a 6 and the second is not a 6.",
               r"$\tfrac{1}{6} \times \tfrac{5}{6} = \tfrac{5}{36}$."),
            SUM("Mutually exclusive events cannot happen together: P(A or B) = P(A) + P(B).",
                "Independent events do not affect each other: P(A and B) = P(A) × P(B).",
                "If events overlap, do not add: list the outcomes instead.",
                "Picking with replacement gives independent events; without replacement does not.",
                "Check answers with a list of outcomes or a possibility diagram when you can."),
        ],
    ),
    # ------------------------------------------------------------------ Probability 3
    lesson(
        module=M,
        topic=PR,
        title="Tree diagrams",
        slug="tree-diagrams-two-events",
        minutes=25,
        summary="Draw and use tree diagrams for two events, with independent events and with picks made without replacement, and find 'at least one' probabilities with the complement.",
        objectives=[
            "Draw a tree diagram for two events and label each branch with its probability",
            "Multiply along a path and add the results of different paths",
            "Use a tree diagram when items are picked without replacement",
            "Find P(at least one) as 1 − P(none)",
        ],
        key_concepts=["Tree diagram", "Branch", "Path", "Independent events", "Without replacement", "At least one"],
        blocks=[
            H("Introduction"),
            T("In the previous lesson you used the AND rule and the OR rule. A **tree diagram** puts both rules into one "
              "picture, so you can answer questions such as 'exactly one' or 'at least one' without missing a case."),
            T("Each set of branches shows the outcomes of one event. The probabilities on the branches leaving one point "
              "always add up to 1."),
            KEY("How to read a tree", "Two rules do all the work.",
                cards=[["Along a path: multiply", "One path is 'this AND then that', so multiply the probabilities on its branches."],
                       ["Several paths: add", "Different paths cannot happen together, so add the results of all the paths you want."]]),
            H("Independent events"),
            EX("Worked example 1: bus and taxi", intro=(
                "Amina travels by bus and Bih travels by taxi, independently. The probability that the bus is late is 0.3. "
                "The probability that the taxi is late is 0.1. Find the probability that (a) both are late, (b) exactly one is late."),
               steps=[
                   S("Draw the tree", text="First pair of branches for the bus: late 0.3, on time 0.7. From the end of each, a pair for the taxi: late 0.1, on time 0.9. This gives four paths."),
                   S("(a) Both late: multiply along one path", math=r"0.3 \times 0.1 = 0.03"),
                   S("(b) Exactly one late: two paths", math=r"0.3 \times 0.9 + 0.7 \times 0.1 = 0.27 + 0.07 = 0.34"),
               ], check=r"0.03 + 0.27 + 0.07 + 0.63 = 1"),
            IMG("f5-tree-bus-taxi.svg",
                "Tree diagram. First branches for the bus: late 0.3, on time 0.7. From each, branches for the taxi: late 0.1, on time 0.9. The four path probabilities are 0.03, 0.27, 0.07 and 0.63.",
                "Figure 1. Worked example 1: multiply along each path; the four results add up to 1."),
            H("At least one"),
            T("'At least one late' means one late or both late: three of the four paths. It is quicker to use the one path "
              "that is **not** wanted, 'neither late', and subtract from 1."),
            F(r"P(\text{at least one}) = 1 - P(\text{none})"),
            T(r"For the bus and taxi: $P(\text{at least one late}) = 1 - 0.7 \times 0.9 = 1 - 0.63 = 0.37$. "
              r"Check: $0.03 + 0.27 + 0.07 = 0.37$."),
            QUIZ("The probability that a maize seed germinates is 0.7. Two seeds are planted and germinate independently. What is the probability that at least one germinates?",
                 ["$0.49$", "$1.4$", "$0.91$", "$0.42$"], 2,
                 r"P(neither) $= 0.3 \times 0.3 = 0.09$, so P(at least one) $= 1 - 0.09 = 0.91$.",
                 hint="Find the probability that neither seed germinates first.",
                 feedback=["That is P(both germinate). At least one also includes exactly one germinating.",
                           "You added 0.7 + 0.7. A probability can never be more than 1.", "",
                           r"That is P(exactly one) $= 2 \times 0.7 \times 0.3$. It leaves out the case where both germinate."]),
            H("Without replacement"),
            T("When you take an item and do **not** put it back, the second pick is from fewer items. The probabilities on "
              "the second set of branches change, and they depend on what happened first."),
            EX("Worked example 2: mangoes in Mokolo market", intro=(
                "A trader has a basket of 10 mangoes: 4 are ripe and 6 are not ripe. A customer picks two mangoes at random, one after the other, "
                "without putting the first back. Find the probability that (a) both are ripe, (b) one is ripe and one is not, (c) at least one is ripe."),
               steps=[
                   S("First pick", text=r"P(ripe) $= \tfrac{4}{10}$ and P(not ripe) $= \tfrac{6}{10}$."),
                   S("Second pick: only 9 mangoes are left", text=r"After a ripe one: P(ripe) $= \tfrac{3}{9}$, P(not ripe) $= \tfrac{6}{9}$. After an unripe one: P(ripe) $= \tfrac{4}{9}$, P(not ripe) $= \tfrac{5}{9}$."),
                   S("(a) Both ripe", math=r"\frac{4}{10} \times \frac{3}{9} = \frac{12}{90} = \frac{2}{15}"),
                   S("(b) Ripe then not, OR not then ripe", math=r"\frac{4}{10} \times \frac{6}{9} + \frac{6}{10} \times \frac{4}{9} = \frac{48}{90} = \frac{8}{15}"),
                   S("(c) Complement of 'neither ripe'", math=r"1 - \frac{6}{10} \times \frac{5}{9} = 1 - \frac{30}{90} = \frac{2}{3}"),
               ], check=r"\tfrac{12}{90} + \tfrac{24}{90} + \tfrac{24}{90} + \tfrac{30}{90} = 1"),
            IMG("f5-tree-mangoes.svg",
                "Tree diagram for two mangoes picked without replacement. First pick: ripe 4/10, not ripe 6/10. After a ripe mango: ripe 3/9, not ripe 6/9. After an unripe mango: ripe 4/9, not ripe 5/9. Path probabilities: 12/90, 24/90, 24/90 and 30/90.",
                "Figure 2. Worked example 2: the second-pick probabilities change because only 9 mangoes are left."),
            EX("Worked example 3: faulty pens", intro=(
                "A box contains 12 pens, of which 3 are faulty. Two pens are chosen at random without replacement. "
                "Find (a) P(both faulty), (b) P(at least one faulty)."),
               steps=[
                   S("(a) Faulty, then faulty from 11 pens with 2 faulty left", math=r"\frac{3}{12} \times \frac{2}{11} = \frac{6}{132} = \frac{1}{22}"),
                   S("(b) Neither faulty: 9 good pens, then 8 out of 11", math=r"\frac{9}{12} \times \frac{8}{11} = \frac{72}{132} = \frac{6}{11}"),
                   S("(b) At least one faulty", math=r"1 - \frac{6}{11} = \frac{5}{11}"),
               ]),
            MISTAKE("Forgetting that the total changes", "Without replacement, the second denominator is one less, and the count of the type already taken goes down by 1."),
            MISTAKE("Adding along a path", "Along one path you **multiply**. You only **add** when you combine different paths."),
            MISTAKE("Counting only one order", "'One ripe and one not ripe' can happen in two orders. Include both paths."),
            QUIZ("A bag has 3 red and 2 blue counters. Two are taken without replacement. What is P(both red)?",
                 [r"$\tfrac{9}{25}$", r"$\tfrac{3}{10}$", r"$\tfrac{6}{25}$", r"$\tfrac{11}{10}$"], 1,
                 r"$\tfrac{3}{5} \times \tfrac{2}{4} = \tfrac{6}{20} = \tfrac{3}{10}$.",
                 hint="After one red counter is taken, how many counters and how many red ones are left?",
                 feedback=[r"$\tfrac{3}{5} \times \tfrac{3}{5}$ is the answer **with** replacement. After one red is taken, 2 red remain out of 4.", "",
                           r"You used $\tfrac{3}{5} \times \tfrac{2}{5}$. The second denominator should be 4, because only 4 counters are left.",
                           r"You added $\tfrac{3}{5} + \tfrac{2}{4}$. Multiply along the path."]),
            H("Practice questions"),
            PQ("The probability that Ngum passes Mathematics is 0.8 and the probability that she passes English is 0.6. The events are independent. Draw a tree diagram and find the probability that she passes exactly one of the two subjects.",
               r"Branches: Maths pass 0.8, fail 0.2; then English pass 0.6, fail 0.4. "
               r"P(exactly one) $= 0.8 \times 0.4 + 0.2 \times 0.6 = 0.32 + 0.12 = 0.44$."),
            PQ("A basket holds 8 oranges: 5 sweet and 3 sour. Two are picked at random without replacement. Find (a) P(both sweet), (b) P(at least one sour).",
               r"(a) $\tfrac{5}{8} \times \tfrac{4}{7} = \tfrac{20}{56} = \tfrac{5}{14}$. (b) At least one sour is the complement of both sweet: $1 - \tfrac{5}{14} = \tfrac{9}{14}$."),
            PQ("A fair coin is tossed three times. Use a tree diagram with three sets of branches to find P(at least one head).",
               r"There are $2 \times 2 \times 2 = 8$ paths. Only TTT has no head: P(TTT) $= \tfrac{1}{2} \times \tfrac{1}{2} \times \tfrac{1}{2} = \tfrac{1}{8}$. "
               r"So P(at least one head) $= 1 - \tfrac{1}{8} = \tfrac{7}{8}$."),
            SUM("Branches leaving one point add up to 1.",
                "Multiply along a path; add the results of different paths.",
                "Without replacement, the second-pick probabilities change: one item fewer in total.",
                r"$P(\text{at least one}) = 1 - P(\text{none})$.",
                "'One of each' usually needs two paths, one for each order."),
        ],
    ),
]
