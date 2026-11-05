"""Form 5 General Mathematics: Commercial Mathematics & Variation (7 focused lessons)."""

from .dsl import *  # noqa: F403

COURSE = ("mathematics", "form-5")

M = "Commercial Mathematics & Variation"
COM = "Commercial arithmetic"
VAR = "Variation"

LESSONS = [
    # ------------------------------------------------------------------ Commercial arithmetic
    lesson(
        module=M,
        topic=COM,
        title="Simple and compound interest",
        slug="simple-and-compound-interest",
        minutes=22,
        summary="Calculate simple interest and compound interest with the multiplier method, compare the two, and find a rate or a time by working backwards or by trial.",
        objectives=[
            r"Calculate simple interest with $I = \frac{PRT}{100}$",
            r"Calculate the amount and the interest with $A = P\left(1 + \frac{r}{100}\right)^n$",
            "Compare simple and compound interest on the same principal",
            "Find an unknown rate or number of years by working backwards or by trial",
        ],
        key_concepts=["Principal", "Simple interest", "Compound interest", "Amount", "Multiplier"],
        blocks=[
            H("Introduction"),
            T("A teacher in Buea puts her savings in a bank. A trader in Bafoussam borrows money to buy stock. "
              "In both cases money is paid for the use of money. This payment is called **interest**."),
            T("There are two ways to work out interest. With **simple interest**, the interest is the same every year. "
              "With **compound interest**, the interest is added to the money each year, so the interest itself earns interest. "
              "All amounts in this lesson are in FCFA."),
            H("Simple interest"),
            D("The **principal** $P$ is the money first saved or borrowed. With **simple interest**, interest is paid only on the principal. "
              "$R$ is the rate per cent per year and $T$ is the time in years.",
              title="Definition: simple interest", formula=r"I = \frac{P \times R \times T}{100}",
              note="The **amount** is the principal plus the interest: $A = P + I$."),
            EX("Worked example 1: simple interest", intro=(
                "A teacher saves 500 000 FCFA at 8% per year simple interest. Find the interest after 3 years and the amount."), steps=[
                S("Write the formula", math=r"I = \frac{PRT}{100}"),
                S("Substitute", math=r"I = \frac{500\,000 \times 8 \times 3}{100}"),
                S("Calculate the interest", math=r"I = 120\,000 \text{ FCFA}"),
                S("Find the amount", math=r"A = 500\,000 + 120\,000 = 620\,000 \text{ FCFA}"),
            ], check=r"\text{Each year: } 8\% \times 500\,000 = 40\,000, \quad 3 \times 40\,000 = 120\,000"),
            H("Compound interest"),
            D("With **compound interest**, each year's interest is added to the money. Next year, interest is paid on this larger amount. "
              "To increase by $r\\%$, multiply by $1 + \\frac{r}{100}$ once for each year.",
              title="Definition: compound interest",
              formula=r"A = P\left(1 + \frac{r}{100}\right)^n",
              note="$A$ is the amount after $n$ years. The compound interest is $A - P$."),
            EX("Worked example 2: compound interest", intro=(
                "The same teacher saves 500 000 FCFA at 8% per year compound interest instead. "
                "Find the amount after 3 years, the interest, and how much more she earns than with simple interest."), steps=[
                S("Write the multiplier", math=r"1 + \frac{8}{100} = 1.08"),
                S("Multiply once for each year", math=r"A = 500\,000 \times 1.08^3"),
                S("Calculate", math=r"1.08^3 = 1.259712, \quad A = 629\,856 \text{ FCFA}"),
                S("Find the interest", math=r"629\,856 - 500\,000 = 129\,856 \text{ FCFA}"),
                S("Compare with simple interest", math=r"129\,856 - 120\,000 = 9\,856 \text{ FCFA more}"),
            ], check=r"\text{Year by year: } 540\,000 \to 583\,200 \to 629\,856"),
            KEY("Simple or compound?", "Over one year they give the same interest. After that, compound interest is always larger.", cards=[
                ["Simple", "Same interest every year, worked out on the principal only."],
                ["Compound", "Interest grows every year, because it is worked out on the new amount."],
            ]),
            QUIZ("Find the simple interest on 400 000 FCFA at 5% per year for 3 years.",
                 ["20 000 FCFA", "60 000 FCFA", "460 000 FCFA", "63 050 FCFA"], 1,
                 r"$I = \frac{400\,000 \times 5 \times 3}{100} = 60\,000$ FCFA.",
                 hint=r"Use $I = \frac{PRT}{100}$.",
                 feedback=["That is the interest for 1 year only. Multiply by the 3 years.", "",
                           "That is the amount (principal + interest). The question asks for the interest.",
                           "That is the compound interest. The question asks for simple interest."]),
            H("Finding the rate or the time"),
            T("Sometimes the interest or the amount is given and the rate or the time is unknown. "
              r"For simple interest, rearrange the formula: $R = \frac{100I}{PT}$ and $T = \frac{100I}{PR}$."),
            T("For compound interest, find the multiplier first by dividing the amount by the principal. "
              "To find a number of years, try $n = 1, 2, 3, \\ldots$ until the amount passes the target. This is called **trial**."),
            EX("Worked example 3: finding the rate", intro=(
                "500 000 FCFA grows to 583 200 FCFA after 2 years at compound interest. Find the rate."), steps=[
                S("Find the total multiplier", math=r"\frac{583\,200}{500\,000} = 1.1664"),
                S("This is the yearly multiplier squared", math=r"\left(1 + \frac{r}{100}\right)^2 = 1.1664"),
                S("Take the square root", math=r"1 + \frac{r}{100} = \sqrt{1.1664} = 1.08"),
                S("Read off the rate", math=r"r = 8\%"),
            ], check=r"500\,000 \times 1.08^2 = 583\,200"),
            EX("Worked example 4: finding the time by trial", intro=(
                "A cooperative in Bamenda invests 300 000 FCFA at 10% per year compound interest. "
                "After how many whole years will the amount first be more than 400 000 FCFA?"), steps=[
                S("Multiplier", math=r"1 + \frac{10}{100} = 1.1"),
                S("Try year by year", math=r"330\,000,\; 363\,000,\; 399\,300,\; 439\,230"),
                S("Compare with 400 000", text="After 3 years it is 399 300 FCFA, still just below. After 4 years it is 439 230 FCFA."),
                S("Answer", math=r"n = 4 \text{ years}"),
            ]),
            H("Common mistakes"),
            MISTAKE("Using simple interest when the question says compound",
                    r"$500\,000 \times 8\% \times 3 = 120\,000$ is simple interest. Compound interest needs $1.08^3$."),
            MISTAKE("Giving the amount when the question asks for the interest",
                    "Read carefully. Interest is the amount **minus** the principal."),
            MISTAKE("Dividing the total rate by the number of years for compound interest",
                    r"If the money grows by 16.64% in 2 years, the yearly rate is not 8.32%. Take the square root of the multiplier: $\sqrt{1.1664} = 1.08$."),
            QUIZ("Which saving gives the larger interest after 2 years on 200 000 FCFA?",
                 ["6% simple interest", "6% compound interest", "Both give the same interest", "It depends on the bank"], 1,
                 r"Simple: $200\,000 \times 6 \times 2 \div 100 = 24\,000$. Compound: $200\,000 \times 1.06^2 - 200\,000 = 24\,720$.",
                 hint="Work out both interests and compare them.",
                 feedback=["Simple interest gives 24 000 FCFA, which is 720 FCFA less than compound interest.", "",
                           "They are equal only after 1 year. In the second year compound interest also earns interest on the first year's interest.",
                           "With the same rate and time, the formulas always give the same answers."]),
            H("Practice questions"),
            PQ("Find the compound interest on 200 000 FCFA at 5% per year for 2 years.",
               r"$A = 200\,000 \times 1.05^2 = 200\,000 \times 1.1025 = 220\,500$ FCFA. Interest $= 220\,500 - 200\,000 = 20\,500$ FCFA."),
            PQ("A loan of 150 000 FCFA earns 27 000 FCFA simple interest in 3 years. Find the rate per year.",
               r"$R = \frac{100I}{PT} = \frac{100 \times 27\,000}{150\,000 \times 3} = \frac{2\,700\,000}{450\,000} = 6\%$ per year."),
            PQ("Mr Tabi saves 250 000 FCFA at 4% per year compound interest. Find (a) the amount after 3 years (b) the interest earned.",
               r"(a) $A = 250\,000 \times 1.04^3 = 250\,000 \times 1.124864 = 281\,216$ FCFA. (b) Interest $= 281\,216 - 250\,000 = 31\,216$ FCFA."),
            PQ("100 000 FCFA is invested at 20% per year compound interest. By trial, find the smallest whole number of years after which the money has more than doubled.",
               r"Multiplier 1.2. Amounts: 120 000, 144 000, 172 800, 207 360 FCFA. After 3 years it is below 200 000; after 4 years it is above. Answer: 4 years."),
            H("Summary"),
            SUM(r"Simple interest: $I = \frac{PRT}{100}$, the same every year.",
                r"Compound interest: $A = P\left(1 + \frac{r}{100}\right)^n$, and interest $= A - P$.",
                "After the first year, compound interest is larger than simple interest at the same rate.",
                "To find a compound rate, divide amount by principal, then take the root that matches the number of years.",
                "To find a number of years, try n = 1, 2, 3, ... until the amount passes the target."),
        ],
    ),
    lesson(
        module=M,
        topic=COM,
        title="Depreciation and appreciation",
        slug="depreciation-and-appreciation",
        minutes=20,
        summary="Use reducing-balance multipliers to find the value of an item after it loses or gains value each year, and work backwards to find its original value.",
        objectives=[
            r"Find a value after $n$ years of depreciation with $V = P\left(1 - \frac{r}{100}\right)^n$",
            "Find a value after appreciation with an increase multiplier",
            "Find the total loss in value and express it as a percentage",
            "Work backwards to find the original value",
        ],
        key_concepts=["Depreciation", "Reducing balance", "Appreciation", "Multiplier", "Original value"],
        blocks=[
            H("Introduction"),
            T("A new moto-taxi in Douala loses value every year: the engine wears out and newer models appear. "
              "A plot of land in Bafoussam usually gains value as the town grows."),
            T("In the previous lesson, money grew by a fixed percentage each year. Here the same multiplier idea is used for the value of things. "
              "All values are in FCFA."),
            H("Depreciation by reducing balance"),
            D("**Depreciation** is the loss in value of an item over time. In the **reducing balance** method, the item loses $r\\%$ of its value "
              "**at the start of that year** every year. So we multiply by $1 - \\frac{r}{100}$ once for each year.",
              title="Definition: depreciation", formula=r"V = P\left(1 - \frac{r}{100}\right)^n",
              note="$P$ is the original value and $V$ the value after $n$ years."),
            EX("Worked example 1: value after depreciation", intro=(
                "A motorbike costs 1 200 000 FCFA. It depreciates by 15% each year. Find its value after 2 years and the total loss in value."), steps=[
                S("Write the multiplier", math=r"1 - \frac{15}{100} = 0.85"),
                S("Multiply once for each year", math=r"V = 1\,200\,000 \times 0.85^2"),
                S("Calculate", math=r"V = 1\,200\,000 \times 0.7225 = 867\,000 \text{ FCFA}"),
                S("Total loss", math=r"1\,200\,000 - 867\,000 = 333\,000 \text{ FCFA}"),
            ], check=r"1\,200\,000 \to 1\,020\,000 \to 867\,000"),
            TIP("The loss is not the same every year. In year 1 the motorbike lost 180 000 FCFA, but in year 2 it lost 15% of 1 020 000, which is only 153 000 FCFA."),
            QUIZ("A phone worth 100 000 FCFA depreciates by 10% each year. What is it worth after 2 years?",
                 ["80 000 FCFA", "81 000 FCFA", "90 000 FCFA", "121 000 FCFA"], 1,
                 r"$100\,000 \times 0.9^2 = 100\,000 \times 0.81 = 81\,000$ FCFA.",
                 hint="Multiply by 0.9 once for each year.",
                 feedback=["You took 10% of the original price twice. Each year's 10% is taken from the new, lower value.", "",
                           "This is the value after only 1 year.", "You increased the value. Depreciation makes it smaller."]),
            H("Appreciation"),
            D("**Appreciation** is a gain in value over time, for example land or a house. "
              "When the value rises by $r\\%$ each year, multiply by $1 + \\frac{r}{100}$ once for each year.",
              title="Definition: appreciation", formula=r"V = P\left(1 + \frac{r}{100}\right)^n"),
            EX("Worked example 2: appreciation", intro=(
                "A plot of land in Bafoussam is worth 2 000 000 FCFA. Its value rises by 10% each year. Find its value after 3 years."), steps=[
                S("Write the multiplier", math=r"1 + \frac{10}{100} = 1.1"),
                S("Multiply once for each year", math=r"V = 2\,000\,000 \times 1.1^3"),
                S("Calculate", math=r"V = 2\,000\,000 \times 1.331 = 2\,662\,000 \text{ FCFA}"),
            ], check=r"2\,000\,000 \to 2\,200\,000 \to 2\,420\,000 \to 2\,662\,000"),
            H("Finding the original value"),
            T("If you know the value **after** $n$ years, call the original value $P$ and write the equation. "
              "Then **divide** by the multiplier to the power $n$. Adding the percentage back does not work."),
            EX("Worked example 3: working backwards", intro=(
                "A motorbike depreciates by 10% each year. After 2 years it is worth 405 000 FCFA. What was its value when new?"), steps=[
                S("Write the equation", math=r"P \times 0.9^2 = 405\,000"),
                S("Work out the multiplier", math=r"0.9^2 = 0.81"),
                S("Divide", math=r"P = \frac{405\,000}{0.81} = 500\,000 \text{ FCFA}"),
            ], check=r"500\,000 \times 0.81 = 405\,000"),
            EX("Worked example 4: total percentage loss", intro=(
                "A laptop depreciates by 20% each year. What percentage of its original value has it lost after 2 years?"), steps=[
                S("Multiplier for 2 years", math=r"0.8^2 = 0.64"),
                S("Fraction of the value left", text="64% of the original value is left."),
                S("Percentage lost", math=r"100\% - 64\% = 36\%"),
            ]),
            H("Common mistakes"),
            MISTAKE("Taking the percentage of the original value every year",
                    r"10% for 2 years is not a 20% loss. Use $0.9^2 = 0.81$, which is a 19% loss."),
            MISTAKE("Adding the percentage back to find the original value",
                    r"$405\,000 \times 1.1^2 = 490\,050$ is wrong. A 10% fall is undone by dividing by 0.9, not by adding 10%."),
            MISTAKE("Using the wrong multiplier", "Depreciation (losing value) uses a multiplier less than 1. Appreciation (gaining value) uses a multiplier more than 1."),
            QUIZ("A house worth 5 000 000 FCFA appreciates by 4% per year. Which calculation gives its value after 3 years?",
                 [r"$5\,000\,000 \times 0.96^3$", r"$5\,000\,000 \times 1.04 \times 3$", r"$5\,000\,000 \times 1.04^3$", r"$5\,000\,000 \times 1.12$"], 2,
                 r"Appreciation multiplies by $1.04$ once for each year: $5\,000\,000 \times 1.04^3$.",
                 hint="Is the value going up or down? Then how many times do you multiply?",
                 feedback=["0.96 is a depreciation multiplier. The house gains value.",
                           "Multiplying by 3 triples the value. You must multiply by 1.04 three times, which is a power.", "",
                           r"1.12 adds 4% three times on the original value (simple growth). Compound growth uses $1.04^3$."]),
            H("Practice questions"),
            PQ("A car bought for 6 000 000 FCFA depreciates by 20% each year. Find its value after 3 years.",
               r"$V = 6\,000\,000 \times 0.8^3 = 6\,000\,000 \times 0.512 = 3\,072\,000$ FCFA."),
            PQ("A house in Limbe is worth 8 000 000 FCFA. Its value increases by 5% each year. Find its value after 2 years.",
               r"$V = 8\,000\,000 \times 1.05^2 = 8\,000\,000 \times 1.1025 = 8\,820\,000$ FCFA."),
            PQ("A grinding machine depreciates by 10% each year. After 3 years it is worth 1 458 000 FCFA. Find its original value.",
               r"$P \times 0.9^3 = 1\,458\,000$. $0.9^3 = 0.729$, so $P = \frac{1\,458\,000}{0.729} = 2\,000\,000$ FCFA."),
            PQ("A truck depreciates by 25% each year. After how many whole years is its value first less than half of the original value?",
               r"Multiplier 0.75. $0.75^1 = 0.75$, $0.75^2 = 0.5625$, $0.75^3 = 0.421875$. The value first falls below half after 3 years."),
            H("Summary"),
            SUM(r"Depreciation by reducing balance: $V = P\left(1 - \frac{r}{100}\right)^n$.",
                r"Appreciation: $V = P\left(1 + \frac{r}{100}\right)^n$.",
                "Each year's percentage is taken from the value at the start of that year, so the yearly loss gets smaller.",
                "To find the original value, divide by the multiplier to the power n. Never just add the percentage back.",
                "Total percentage loss = 100% minus the percentage left."),
        ],
    ),
    lesson(
        module=M,
        topic=COM,
        title="Hire purchase",
        slug="hire-purchase-deposits-and-instalments",
        minutes=18,
        summary="Find the hire purchase price from the deposit and instalments, compare it with the cash price, express the extra cost as a percentage, and find a missing deposit or instalment.",
        objectives=[
            "Calculate the total hire purchase price",
            "Find the extra cost of hire purchase compared with the cash price",
            "Express the extra cost as a percentage of the cash price",
            "Find an unknown deposit, instalment or number of instalments",
        ],
        key_concepts=["Hire purchase", "Cash price", "Deposit", "Instalment", "Extra cost"],
        blocks=[
            H("Introduction"),
            T("Many families in Yaoundé buy a fridge, a television or a motorbike without paying the full price at once. "
              "The shop lets them pay a part now and the rest in monthly payments. This is **hire purchase**."),
            T("Hire purchase helps people who do not have all the money today, but it usually costs more than paying cash. "
              "In this lesson you will find out exactly how much more. All prices are in FCFA."),
            H("Key words"),
            D("The **cash price** is what you pay if you pay everything at once. With **hire purchase** (HP), you pay a **deposit** first, "
              "then a number of equal **instalments** (usually monthly).", title="Definition: hire purchase",
              formula=r"\text{HP price} = \text{deposit} + (\text{number of instalments} \times \text{instalment})"),
            KEY("Comparing HP with cash", "Two numbers answer the question \"how much more does HP cost?\"", cards=[
                ["Extra cost", r"$\text{HP price} - \text{cash price}$"],
                ["Percentage extra", r"$\frac{\text{extra cost}}{\text{cash price}} \times 100\%$"],
            ]),
            EX("Worked example 1: HP price and extra cost", intro=(
                "A television has a cash price of 250 000 FCFA. On hire purchase, the buyer pays a deposit of 20% of the cash price "
                "and 12 monthly instalments of 18 500 FCFA. Find (a) the HP price (b) the extra cost (c) the extra cost as a percentage of the cash price."), steps=[
                S("Deposit", math=r"20\% \times 250\,000 = 50\,000"),
                S("Total of the instalments", math=r"12 \times 18\,500 = 222\,000"),
                S("(a) HP price", math=r"50\,000 + 222\,000 = 272\,000 \text{ FCFA}"),
                S("(b) Extra cost", math=r"272\,000 - 250\,000 = 22\,000 \text{ FCFA}"),
                S("(c) Percentage extra", math=r"\frac{22\,000}{250\,000} \times 100\% = 8.8\%"),
            ]),
            QUIZ("A gas cooker has a cash price of 150 000 FCFA. On HP the deposit is 25% of the cash price, then 8 monthly instalments of 15 000 FCFA. How much more does HP cost?",
                 ["157 500 FCFA", "37 500 FCFA", "7 500 FCFA", "120 000 FCFA"], 2,
                 r"Deposit $= 37\,500$, instalments $= 8 \times 15\,000 = 120\,000$, HP price $= 157\,500$. Extra $= 157\,500 - 150\,000 = 7\,500$ FCFA.",
                 hint="Find the deposit and the total of the instalments first.",
                 feedback=["That is the HP price. Subtract the cash price to find how much more it costs.",
                           "That is the deposit only.", "",
                           "That is the total of the instalments only. Add the deposit, then compare with the cash price."]),
            EX("Worked example 2: percentage extra", intro=(
                "A fridge has a cash price of 180 000 FCFA. On HP it costs a deposit of 30 000 FCFA and 10 monthly payments of 17 000 FCFA. "
                "Express the extra cost as a percentage of the cash price, correct to 1 decimal place."), steps=[
                S("HP price", math=r"30\,000 + 10 \times 17\,000 = 200\,000"),
                S("Extra cost", math=r"200\,000 - 180\,000 = 20\,000"),
                S("Divide by the cash price", math=r"\frac{20\,000}{180\,000} \times 100\% = 11.1\%"),
            ]),
            H("Finding a missing part"),
            T("If you know the HP price, you can work backwards. Subtract the deposit to find the total of the instalments, then divide by the number of instalments."),
            EX("Worked example 3: finding the instalment", intro=(
                "A motorbike has a cash price of 900 000 FCFA. The HP price is 20% more than the cash price. "
                "The deposit is 180 000 FCFA and the rest is paid in 18 equal monthly instalments. Find each instalment."), steps=[
                S("HP price", math=r"900\,000 \times 1.2 = 1\,080\,000"),
                S("Amount left after the deposit", math=r"1\,080\,000 - 180\,000 = 900\,000"),
                S("Each instalment", math=r"\frac{900\,000}{18} = 50\,000 \text{ FCFA}"),
            ], check=r"180\,000 + 18 \times 50\,000 = 1\,080\,000"),
            H("Common mistakes"),
            MISTAKE("Forgetting the deposit", "The HP price is the deposit **plus** all the instalments. Do not add only the instalments."),
            MISTAKE("Dividing by the HP price for the percentage",
                    "The percentage extra is worked out on the **cash price**, unless the question says otherwise."),
            MISTAKE("Working out the deposit from the wrong price", "A deposit of 20% \"of the cash price\" means 20% of the cash price, not of the HP price."),
            H("Practice questions"),
            PQ("A sewing machine has a cash price of 120 000 FCFA. On HP the buyer pays 24 000 FCFA deposit and 12 monthly instalments of 9 000 FCFA. "
               "Find (a) the HP price (b) the extra cost as a percentage of the cash price.",
               r"(a) $24\,000 + 12 \times 9\,000 = 24\,000 + 108\,000 = 132\,000$ FCFA. "
               r"(b) Extra $= 12\,000$ FCFA. Percentage $= \frac{12\,000}{120\,000} \times 100 = 10\%$."),
            PQ("The HP price of a generator is 345 000 FCFA. The buyer pays 10 instalments of 27 000 FCFA. How much was the deposit?",
               r"Instalments $= 10 \times 27\,000 = 270\,000$ FCFA. Deposit $= 345\,000 - 270\,000 = 75\,000$ FCFA."),
            PQ("A laptop costs 400 000 FCFA cash. On HP a student pays a deposit of 10% of the cash price and 24 monthly instalments of 17 500 FCFA. "
               "Find the extra cost and express it as a percentage of the cash price.",
               r"Deposit $= 40\,000$. Instalments $= 24 \times 17\,500 = 420\,000$. HP price $= 460\,000$ FCFA. "
               r"Extra $= 60\,000$ FCFA, which is $\frac{60\,000}{400\,000} \times 100 = 15\%$ of the cash price."),
            H("Summary"),
            SUM("HP price = deposit + (number of instalments × instalment).",
                "Extra cost = HP price − cash price.",
                "Percentage extra = extra cost ÷ cash price × 100%.",
                "To find a missing instalment: subtract the deposit from the HP price, then divide by the number of instalments.",
                "HP lets you buy now, but you usually pay more than the cash price."),
        ],
    ),
    lesson(
        module=M,
        topic=COM,
        title="Taxes, discounts, profit and loss",
        slug="taxes-discounts-profit-and-loss",
        minutes=24,
        summary="Calculate income tax on taxable income, add or remove a sales tax, apply discounts, and find percentage profit or loss and cost or selling prices.",
        objectives=[
            "Calculate income tax on taxable income after allowances, including two tax bands",
            "Add a sales tax to a price and find the price before tax",
            "Calculate a discount and the price after discount",
            "Find percentage profit or loss and a cost or selling price",
        ],
        key_concepts=["Taxable income", "Allowance", "Income tax", "Sales tax", "Discount", "Cost price", "Selling price", "Percentage profit"],
        blocks=[
            H("Introduction"),
            T("A trader at Mokolo market in Yaoundé buys rice by the bag and sells it by the cup. A civil servant in Garoua pays tax on his salary. "
              "A shop in Douala gives a discount during the festive season. All of these use percentages of money."),
            T("In this lesson every tax rate is an **example chosen for practice**. Real tax rules are set by the government and change over time, "
              "so always use the rates given in the question. All amounts are in FCFA."),
            H("Income tax"),
            D("Part of a person's income is free of tax. These tax-free amounts are called **allowances**. "
              "What is left is the **taxable income**, and income tax is a percentage of it.",
              title="Definition: taxable income", formula=r"\text{taxable income} = \text{income} - \text{allowances}"),
            EX("Worked example 1: income tax with one rate", intro=(
                "A worker earns 2 400 000 FCFA per year. Allowances of 600 000 FCFA are tax-free. "
                "The rest is taxed at 10% (an example rate). Find the tax paid."), steps=[
                S("Taxable income", math=r"2\,400\,000 - 600\,000 = 1\,800\,000"),
                S("Tax", math=r"10\% \times 1\,800\,000 = 180\,000 \text{ FCFA}"),
            ]),
            EX("Worked example 2: income tax with two bands", intro=(
                "In an example tax system, the first 1 000 000 FCFA of taxable income is taxed at 10% and the rest at 15%. "
                "Find the tax on a taxable income of 1 800 000 FCFA."), steps=[
                S("Tax on the first band", math=r"10\% \times 1\,000\,000 = 100\,000"),
                S("Amount in the second band", math=r"1\,800\,000 - 1\,000\,000 = 800\,000"),
                S("Tax on the second band", math=r"15\% \times 800\,000 = 120\,000"),
                S("Total tax", math=r"100\,000 + 120\,000 = 220\,000 \text{ FCFA}"),
            ]),
            H("Sales tax and discounts"),
            T("A **sales tax** (VAT is one kind) is a percentage **added** to the price of goods. "
              r"To add $r\%$ tax, multiply by $1 + \frac{r}{100}$. To find the price **before** tax, divide by the same multiplier."),
            EX("Worked example 3: adding and removing a sales tax", intro=(
                "An example sales tax is 15%. (a) A bag costs 40 000 FCFA before tax. Find the price with tax. "
                "(b) With a 20% tax, a phone costs 60 000 FCFA including tax. Find its price before tax."), steps=[
                S("(a) Add 15%", math=r"40\,000 \times 1.15 = 46\,000 \text{ FCFA}"),
                S("(b) Price before tax times 1.2 gives 60 000", math=r"P \times 1.2 = 60\,000"),
                S("Divide", math=r"P = \frac{60\,000}{1.2} = 50\,000 \text{ FCFA}"),
            ], check=r"50\,000 + 20\% \times 50\,000 = 60\,000"),
            D("A **discount** is an amount taken off the marked price. A discount of $r\\%$ means multiply by $1 - \\frac{r}{100}$.",
              title="Definition: discount", formula=r"\text{price after discount} = \text{marked price} \times \left(1 - \frac{r}{100}\right)",
              note=r"Example: shoes marked 25 000 FCFA with a 12% discount cost $25\,000 \times 0.88 = 22\,000$ FCFA."),
            H("Profit and loss"),
            D("The **cost price** (CP) is what the trader paid. The **selling price** (SP) is what the customer pays. "
              "Profit or loss is given as a percentage of the **cost price**.",
              title="Definition: percentage profit and loss",
              formula=r"\text{percentage profit} = \frac{\text{SP} - \text{CP}}{\text{CP}} \times 100\%",
              note=r"Percentage loss $= \frac{\text{CP} - \text{SP}}{\text{CP}} \times 100\%$."),
            EX("Worked example 4: profit and loss", intro=(
                "(a) A trader buys a basin of tomatoes for 8 000 FCFA and sells it for 10 000 FCFA. Find the percentage profit. "
                "(b) She wants a 20% profit on a sack costing 15 000 FCFA. What should she sell it for? "
                "(c) A radio sold for 23 000 FCFA gave a 15% profit. Find its cost price."), steps=[
                S("(a) Profit", math=r"10\,000 - 8\,000 = 2\,000"),
                S("(a) Percentage of the cost price", math=r"\frac{2\,000}{8\,000} \times 100\% = 25\%"),
                S("(b) Selling price", math=r"15\,000 \times 1.2 = 18\,000 \text{ FCFA}"),
                S("(c) Cost price", math=r"\text{CP} \times 1.15 = 23\,000 \;\Rightarrow\; \text{CP} = \frac{23\,000}{1.15} = 20\,000 \text{ FCFA}"),
            ]),
            QUIZ("A trader buys a radio for 12 000 FCFA and sells it for 15 000 FCFA. What is the percentage profit?",
                 ["20%", "25%", "3 000%", "125%"], 1,
                 r"Profit $= 3\,000$. Percentage profit $= \frac{3\,000}{12\,000} \times 100 = 25\%$.",
                 hint="Profit percentage is worked out on the cost price.",
                 feedback=["You divided by the selling price. Use the cost price, 12 000 FCFA.", "",
                           "3 000 is the profit in FCFA. Divide it by the cost price and multiply by 100.",
                           "125% is the selling price as a percentage of the cost price. The profit part is 125% − 100%."]),
            H("Common mistakes"),
            MISTAKE("Taxing the whole income", "Subtract the allowances first, then apply the tax rate."),
            MISTAKE("Removing a tax by subtracting the percentage",
                    r"$60\,000 - 20\% \times 60\,000 = 48\,000$ is wrong, because the 20% was added to the price **before** tax. Divide by 1.2 instead."),
            MISTAKE("Dividing by the selling price", "Percentage profit and loss use the **cost price** at the bottom of the fraction."),
            QUIZ("A dress costs 40 000 FCFA and is sold for 34 000 FCFA. What is the percentage loss?",
                 ["6%", "17.6%", "85%", "15%"], 3,
                 r"Loss $= 6\,000$. Percentage loss $= \frac{6\,000}{40\,000} \times 100 = 15\%$.",
                 hint="Find the loss in FCFA, then divide by the cost price.",
                 feedback=["6 000 FCFA is the loss in money. Divide by the cost price to make it a percentage.",
                           "You divided by the selling price, 34 000. Use the cost price, 40 000.",
                           "85% is the part of the cost that was recovered, not the loss.", ""]),
            H("Practice questions"),
            PQ("A teacher earns 3 000 000 FCFA a year. Her allowances total 800 000 FCFA. Using an example tax rate of 10%, find her income tax.",
               r"Taxable income $= 3\,000\,000 - 800\,000 = 2\,200\,000$ FCFA. Tax $= 10\% \times 2\,200\,000 = 220\,000$ FCFA."),
            PQ("A trader buys a bag of groundnuts for 30 000 FCFA and sells it for 36 000 FCFA. Find the percentage profit.",
               r"Profit $= 6\,000$ FCFA. Percentage profit $= \frac{6\,000}{30\,000} \times 100 = 20\%$."),
            PQ("A shirt costs 54 000 FCFA including a 20% sales tax (an example rate). Find the price before tax and the amount of tax.",
               r"$P \times 1.2 = 54\,000$, so $P = \frac{54\,000}{1.2} = 45\,000$ FCFA. Tax $= 54\,000 - 45\,000 = 9\,000$ FCFA."),
            PQ("A shop gives a 10% discount on a 20 000 FCFA cooking pot, then a further 5% off the new price. Find the final price and the total percentage discount.",
               r"$20\,000 \times 0.9 \times 0.95 = 17\,100$ FCFA. Total discount $= 2\,900$ FCFA, which is $\frac{2\,900}{20\,000} \times 100 = 14.5\%$ (not 15%)."),
            H("Summary"),
            SUM("Taxable income = income − allowances. Income tax is a percentage of taxable income, sometimes in bands.",
                "Tax rates in questions are examples: always use the rate given.",
                r"Add a sales tax: multiply by $1 + \frac{r}{100}$. Remove it: divide by the same number.",
                r"A discount of $r\%$: multiply by $1 - \frac{r}{100}$.",
                "Percentage profit or loss is always worked out on the cost price."),
        ],
    ),
    # ------------------------------------------------------------------ Variation
    lesson(
        module=M,
        topic=VAR,
        title="Direct and inverse variation",
        slug="direct-and-inverse-variation",
        minutes=22,
        summary="Turn direct and inverse variation statements (including squares and square roots) into equations, find the constant k, and recognise variation from tables and graphs.",
        objectives=[
            r"Write statements such as $y \propto x^2$ and $y \propto \frac{1}{x}$ as equations with a constant $k$",
            "Find $k$ from one pair of values and use it to find unknown values",
            "Decide from a table whether two quantities vary directly or inversely",
            "Recognise the graphs of direct and inverse variation",
        ],
        key_concepts=["Direct variation", "Inverse variation", "Constant of variation", "Proportional"],
        blocks=[
            H("Introduction"),
            T("At the market in Bamenda, if one kilogram of tomatoes costs 600 FCFA, then two kilograms cost 1 200 FCFA. "
              "The cost **varies directly** with the mass: double one, and the other doubles."),
            T("When more workers build a wall, it takes fewer days. The time **varies inversely** with the number of workers: "
              "double the workers, and the time is halved. Variation turns sentences like these into equations."),
            H("Direct variation"),
            D(r"$y$ **varies directly as** $x$ (or $y$ is **proportional** to $x$) when $y = kx$ for a fixed number $k$. "
              r"We write $y \propto x$. The number $k$ is the **constant of variation**.",
              title="Definition: direct variation", formula=r"y \propto x \iff y = kx",
              note=r"The same idea works with powers and roots: $y \propto x^2$ means $y = kx^2$, and $y \propto \sqrt{x}$ means $y = k\sqrt{x}$."),
            EX("Worked example 1: direct variation with a square", intro="$y$ varies directly as $x^2$. When $x = 2$, $y = 12$. Find $y$ when $x = 5$.", steps=[
                S("Write the equation", math=r"y = kx^2"),
                S("Substitute the given values", math=r"12 = k \times 2^2 = 4k"),
                S("Find $k$", math=r"k = 3, \text{ so } y = 3x^2"),
                S("Use the equation", math=r"y = 3 \times 5^2 = 75"),
            ]),
            H("Inverse variation"),
            D(r"$y$ **varies inversely as** $x$ when $y = \frac{k}{x}$. Then the product $xy = k$ stays the same.",
              title="Definition: inverse variation", formula=r"y \propto \frac{1}{x} \iff y = \frac{k}{x}",
              note=r"$y$ varies inversely as the square of $x$ means $y = \frac{k}{x^2}$."),
            EX("Worked example 2: inverse variation", intro=(
                "The time to build a wall in Ebolowa varies inversely as the number of workers. 6 workers take 10 days. How long would 4 workers take?"), steps=[
                S("Write the equation", math=r"t = \frac{k}{w}"),
                S("Substitute the given values", math=r"10 = \frac{k}{6}, \text{ so } k = 60"),
                S("Use the equation", math=r"t = \frac{60}{4} = 15 \text{ days}"),
            ], check=r"\text{Fewer workers, more days: } 15 > 10"),
            QUIZ(r"$y$ is inversely proportional to $x$. When $x = 3$, $y = 8$. What is $y$ when $x = 6$?",
                 ["16", "4", "24", "2"], 1,
                 r"$k = xy = 3 \times 8 = 24$, so $y = \frac{24}{6} = 4$.",
                 hint="For inverse variation, $x \\times y$ stays the same.",
                 feedback=["That is direct variation: doubling $x$ doubled $y$. In inverse variation, doubling $x$ halves $y$.", "",
                           "24 is the constant $k$, not the value of $y$.", r"You divided by $x^2$ ($\frac{72}{36}$). The question says inversely as $x$, not $x^2$."]),
            EX("Worked example 3: inverse square", intro=r"$y \propto \frac{1}{x^2}$. When $x = 2$, $y = 5$. Find (a) $y$ when $x = 4$ (b) $x$ when $y = 0.8$, given $x > 0$.", steps=[
                S("Write the equation", math=r"y = \frac{k}{x^2}"),
                S("Find $k$", math=r"5 = \frac{k}{4} \;\Rightarrow\; k = 20"),
                S("(a) Substitute $x = 4$", math=r"y = \frac{20}{16} = 1.25"),
                S("(b) Substitute $y = 0.8$", math=r"0.8 = \frac{20}{x^2} \;\Rightarrow\; x^2 = 25 \;\Rightarrow\; x = 5"),
            ]),
            H("Tables and graphs"),
            T(r"In a table, test the pairs. If $\frac{y}{x}$ is the same for every pair, $y \propto x$. If $xy$ is the same for every pair, $y \propto \frac{1}{x}$."),
            EX("Worked example 4: reading a table", intro=(
                r"The table gives $x = 2, 4, 6, 8$ with $y = 30, 15, 10, 7.5$. Decide the type of variation and find $y$ when $x = 5$."), steps=[
                S("Test the ratios", math=r"\frac{30}{2} = 15, \quad \frac{15}{4} = 3.75", text="The ratio changes, so this is not direct variation."),
                S("Test the products", math=r"2 \times 30 = 4 \times 15 = 6 \times 10 = 8 \times 7.5 = 60"),
                S("Write the equation", math=r"y = \frac{60}{x}"),
                S("Substitute $x = 5$", math=r"y = \frac{60}{5} = 12"),
            ]),
            IMG("f5m-variation-graphs.svg", alt="Three small graphs: a straight line through the origin for y = kx, a curve through the origin for y = kx squared, and a curve that gets close to both axes without touching them for y = k over x.",
                caption=r"Figure 1. Graphs of $y = kx$, $y = kx^2$ and $y = \frac{k}{x}$ for $x > 0$."),
            T(r"Only $y = kx$ gives a straight line through the origin when $y$ is plotted against $x$. If $y = kx^2$, plotting $y$ against $x^2$ gives a straight line through the origin, with gradient $k$."),
            H("Common mistakes"),
            MISTAKE("Using the wrong form of equation",
                    r"Read the words carefully. 'Inversely as the square of $x$' means $y = \frac{k}{x^2}$, not $y = \frac{k}{x}$ or $y = kx^2$."),
            MISTAKE("Not finding $k$ first", "Always find the constant from the given pair of values before you calculate anything new."),
            H("Practice questions"),
            PQ(r"$p$ varies directly as the square root of $q$. When $q = 9$, $p = 6$. Find (a) $p$ when $q = 25$ (b) $q$ when $p = 14$.",
               r"$p = k\sqrt{q}$. $6 = k \times 3$, so $k = 2$ and $p = 2\sqrt{q}$. "
               r"(a) $p = 2 \times 5 = 10$. (b) $14 = 2\sqrt{q}$, so $\sqrt{q} = 7$ and $q = 49$."),
            PQ("The cost of rice varies directly as its mass. 3 kg cost 1 800 FCFA. Find (a) the cost of 5 kg (b) the mass that costs 4 200 FCFA.",
               r"$C = km$. $1\,800 = 3k$, so $k = 600$. (a) $C = 600 \times 5 = 3\,000$ FCFA. (b) $4\,200 = 600m$, so $m = 7$ kg."),
            PQ(r"The table shows $x = 1, 2, 3$ and $y = 4, 16, 36$. Show that $y \propto x^2$ and find $y$ when $x = 5$.",
               r"$\frac{y}{x^2} = \frac{4}{1} = \frac{16}{4} = \frac{36}{9} = 4$, the same each time. So $y = 4x^2$ and $y = 4 \times 25 = 100$."),
            PQ(r"$y \propto x^2$. What happens to $y$ when $x$ is doubled?",
               r"$y = kx^2$. Replacing $x$ by $2x$ gives $k(2x)^2 = 4kx^2 = 4y$. So $y$ is multiplied by 4."),
            H("Summary"),
            SUM(r"Direct: $y \propto x$ means $y = kx$. Inverse: $y \propto \frac{1}{x}$ means $y = \frac{k}{x}$.",
                r"Powers and roots go inside the equation, for example $y = kx^2$ or $y = \frac{k}{x^2}$.",
                "Find k first from the given pair of values, then substitute the new values.",
                r"In a table: constant $\frac{y}{x}$ means direct variation; constant $xy$ means inverse variation.",
                "The graph of y = kx is a straight line through the origin; y = k/x is a curve that never meets the axes."),
        ],
    ),
    lesson(
        module=M,
        topic=VAR,
        title="Joint variation",
        slug="joint-variation",
        minutes=20,
        summary="Write joint variation statements such as y ∝ xz and y ∝ x/z² as equations, find k, and work out the effect on one quantity when the others change by a factor or a percentage.",
        objectives=[
            r"Write joint variation statements such as $y \propto xz$ and $y \propto \frac{x}{z^2}$ as equations",
            "Find the constant from one set of values and use it to find an unknown",
            "Find the factor by which a quantity changes when the others are multiplied",
            "Find the percentage change in a quantity when the others change by percentages",
        ],
        key_concepts=["Joint variation", "Combined variation", "Constant of variation", "Percentage change"],
        blocks=[
            H("Introduction"),
            T("A transporter in Garoua charges more to carry heavier loads, and more to carry them further. "
              "The cost depends on **two** quantities at once: the mass and the distance."),
            T("In the previous lesson one quantity depended on one other. Now one quantity depends on two or more. "
              "This is **joint variation**. The method is the same: write the equation, find $k$, then use it."),
            H("Writing the equation"),
            D(r"$y$ **varies jointly as** $x$ and $z$ when $y = kxz$. "
              r"When $y$ varies directly as one quantity and inversely as another, the direct part goes on top and the inverse part goes underneath.",
              title="Definition: joint variation", formula=r"y \propto xz \iff y = kxz"),
            KEY("From words to equations", "One constant $k$ covers all the variables.", cards=[
                ["Jointly as x and z", r"$y = kxz$"],
                ["Jointly as x and the square of z", r"$y = kxz^2$"],
                ["Directly as x, inversely as z²", r"$y = \frac{kx}{z^2}$"],
            ]),
            EX("Worked example 1: joint variation", intro="$z$ varies jointly as $x$ and $y$. When $x = 2$ and $y = 3$, $z = 24$. Find $z$ when $x = 5$ and $y = 1.5$.", steps=[
                S("Write the equation", math=r"z = kxy"),
                S("Find $k$", math=r"24 = k \times 2 \times 3 = 6k \;\Rightarrow\; k = 4"),
                S("Use the equation", math=r"z = 4 \times 5 \times 1.5 = 30"),
            ]),
            EX("Worked example 2: direct and inverse together", intro=(
                r"$y$ varies directly as $x$ and inversely as the square of $z$. When $x = 4$ and $z = 2$, $y = 9$. Find $y$ when $x = 6$ and $z = 3$."), steps=[
                S("Write the equation", math=r"y = \frac{kx}{z^2}"),
                S("Find $k$", math=r"9 = \frac{k \times 4}{2^2} = k \;\Rightarrow\; k = 9"),
                S("Use the equation", math=r"y = \frac{9 \times 6}{3^2} = \frac{54}{9} = 6"),
            ]),
            EX("Worked example 3: a transport problem", intro=(
                "The cost $C$ FCFA of transporting goods varies jointly as the mass $m$ kg and the distance $d$ km. "
                "Carrying 200 kg over 50 km costs 20 000 FCFA. Find the cost of carrying 350 kg over 80 km."), steps=[
                S("Write the equation", math=r"C = kmd"),
                S("Find $k$", math=r"20\,000 = k \times 200 \times 50 = 10\,000k \;\Rightarrow\; k = 2"),
                S("Use the equation", math=r"C = 2 \times 350 \times 80 = 56\,000 \text{ FCFA}"),
            ]),
            QUIZ(r"$z$ varies jointly as $x$ and $y$. When $x = 3$ and $y = 4$, $z = 36$. Find $z$ when $x = 2$ and $y = 5$.",
                 ["10", "3", "30", "36"], 2,
                 r"$36 = 12k$, so $k = 3$. Then $z = 3 \times 2 \times 5 = 30$.",
                 hint="Write $z = kxy$ and find $k$ first.",
                 feedback=[r"You forgot the constant: $z = kxy$ with $k = 3$, not $z = xy$.",
                           "3 is the constant $k$, not the new value of $z$.", "",
                           r"You used $z = k(x + y)$: both $3 + 4$ and $2 + 5$ equal 7, so $z$ stayed 36. Joint variation multiplies the variables: $z = kxy$."]),
            H("Changing the variables"),
            T(r"To see the effect of a change, replace each variable by its new value written as a multiple. "
              r"A 20% increase multiplies by 1.2. A 10% decrease multiplies by 0.9. The constant $k$ does not change."),
            EX("Worked example 4: percentage change", intro=(
                r"$y \propto xz$. $x$ is increased by 20% and $z$ is decreased by 10%. Find the percentage change in $y$."), steps=[
                S("Write the equation", math=r"y = kxz"),
                S("New values", math=r"x \to 1.2x, \quad z \to 0.9z"),
                S("New $y$", math=r"k(1.2x)(0.9z) = 1.08\,kxz = 1.08y"),
                S("Percentage change", text="y is multiplied by 1.08, so y increases by 8%."),
            ]),
            EX("Worked example 5: an inverse square", intro=(
                r"$y \propto \frac{x}{z^2}$. $x$ and $z$ are both increased by 10%. Find the percentage change in $y$, to 1 decimal place."), steps=[
                S("Write the equation", math=r"y = \frac{kx}{z^2}"),
                S("New $y$", math=r"\frac{k(1.1x)}{(1.1z)^2} = \frac{1.1}{1.21} \times \frac{kx}{z^2} = 0.909y"),
                S("Percentage change", math=r"0.909 - 1 = -0.091", text="y decreases by about 9.1%."),
            ]),
            H("Common mistakes"),
            MISTAKE("Adding or subtracting the percentages",
                    "A 20% increase and a 10% decrease do not give a 10% increase. Multiply the factors: 1.2 × 0.9 = 1.08."),
            MISTAKE("Forgetting to square the factor",
                    r"If $y \propto \frac{1}{z^2}$ and $z$ is doubled, $y$ is divided by $2^2 = 4$, not by 2."),
            MISTAKE("Using a different constant for each variable", "Joint variation has one constant $k$ for the whole equation."),
            QUIZ(r"$y \propto xz$. If $x$ is doubled and $z$ is halved, what happens to $y$?",
                 ["It doubles", "It is halved", "It is multiplied by 4", "It does not change"], 3,
                 r"$k(2x)\left(\frac{z}{2}\right) = kxz = y$, so $y$ stays the same.",
                 hint="Replace $x$ by $2x$ and $z$ by $\\frac{z}{2}$, then simplify.",
                 feedback=["That ignores the change in $z$. Halving $z$ cancels doubling $x$.",
                           "That ignores the change in $x$. Doubling $x$ cancels halving $z$.",
                           r"You multiplied by 2 twice. Halving $z$ multiplies by $\frac{1}{2}$, not 2.", ""]),
            H("Practice questions"),
            PQ(r"The volume $V$ of a cylinder varies jointly as the square of its radius $r$ and its height $h$. When $r = 3$ and $h = 10$, $V = 270$. Find $V$ when $r = 2$ and $h = 15$.",
               r"$V = kr^2h$. $270 = k \times 9 \times 10 = 90k$, so $k = 3$. Then $V = 3 \times 4 \times 15 = 180$."),
            PQ(r"$P$ varies directly as $Q$ and inversely as $R$. When $Q = 8$ and $R = 2$, $P = 12$. Find $R$ when $P = 6$ and $Q = 10$.",
               r"$P = \frac{kQ}{R}$. $12 = \frac{8k}{2} = 4k$, so $k = 3$. Then $6 = \frac{3 \times 10}{R}$, so $R = \frac{30}{6} = 5$."),
            PQ(r"$y \propto x^2 z$. $x$ is increased by 20% and $z$ is decreased by 25%. Find the percentage change in $y$.",
               r"New $y = k(1.2x)^2(0.75z) = 1.44 \times 0.75 \times kx^2z = 1.08y$. So $y$ increases by 8%."),
            PQ("The number of days $d$ needed to dig ditches varies directly as the number of ditches $n$ and inversely as the number of workers $w$. "
               "6 workers dig 4 ditches in 10 days. How many days do 10 workers need for 5 ditches?",
               r"$d = \frac{kn}{w}$. $10 = \frac{4k}{6}$, so $k = 15$. Then $d = \frac{15 \times 5}{10} = 7.5$ days."),
            H("Summary"),
            SUM(r"Joint variation: $y \propto xz$ means $y = kxz$, with one constant $k$.",
                r"Direct parts go on top, inverse parts go underneath: $y \propto \frac{x}{z^2}$ means $y = \frac{kx}{z^2}$.",
                "Find k from one full set of values, then substitute the new values.",
                "For changes, multiply by the factors (for example 1.2 for +20%, 0.9 for −10%), remembering powers.",
                "Never add or subtract percentage changes: multiply the factors."),
        ],
    ),
    lesson(
        module=M,
        topic=VAR,
        title="Partial variation",
        slug="partial-variation",
        minutes=22,
        summary="Write partial variation as y = a + bx or y = ax + bx², find the two constants from two conditions with simultaneous equations, and use the law to find unknown values.",
        objectives=[
            "Recognise partial variation and write it as $y = a + bx$ or $y = ax + bx^2$",
            "Form two simultaneous equations from two given conditions",
            "Solve for the two constants and write the law",
            "Use the law to find an unknown value",
        ],
        key_concepts=["Partial variation", "Fixed part", "Variable part", "Simultaneous equations"],
        blocks=[
            H("Introduction"),
            T("A hall in Buea charges a fixed fee for the room, plus an amount for each guest. "
              "A moto-taxi fare can work the same way: a fixed starting charge, plus so much per kilometre."),
            T("The total is **partly constant** and **partly varies** with the number of guests or kilometres. "
              "In the previous lessons there was one constant $k$. Now there are **two** constants, so we need **two** facts to find them."),
            H("Partly constant, partly varying"),
            D(r"$y$ is **partly constant and partly varies as** $x$ when $y = a + bx$, where $a$ and $b$ are constants. "
              r"$a$ is the fixed part and $bx$ is the varying part.",
              title="Definition: partial variation", formula=r"y = a + bx",
              note="Two pairs of values give two simultaneous equations in a and b."),
            EX("Worked example 1: hiring a hall", intro=(
                "The cost $C$ FCFA of hiring a hall in Buea is partly constant and partly varies as the number of guests $n$. "
                "It costs 150 000 FCFA for 50 guests and 250 000 FCFA for 100 guests. Find the law and the cost for 80 guests."), steps=[
                S("Write the equation", math=r"C = a + bn"),
                S("Form two equations", math=r"a + 50b = 150\,000 \qquad a + 100b = 250\,000"),
                S("Subtract the first from the second", math=r"50b = 100\,000 \;\Rightarrow\; b = 2\,000"),
                S("Find $a$", math=r"a = 150\,000 - 50 \times 2\,000 = 50\,000"),
                S("Write the law", math=r"C = 50\,000 + 2\,000n"),
                S("Cost for 80 guests", math=r"C = 50\,000 + 2\,000 \times 80 = 210\,000 \text{ FCFA}"),
            ], check=r"50\,000 + 2\,000 \times 100 = 250\,000"),
            GRAPH([2000, 50000], alt="A straight line starting at 50 000 on the vertical axis and rising steadily, showing C = 50 000 + 2 000n.",
                  caption="Figure 1. The law C = 50 000 + 2 000n is a straight line that cuts the C-axis at the fixed part, 50 000 FCFA, not at the origin.",
                  xmin=0, xmax=120, ymin=0, ymax=300000, label="C = 50 000 + 2 000n"),
            QUIZ(r"For the hall, $C = 50\,000 + 2\,000n$. 80 guests cost 210 000 FCFA. What do 160 guests cost?",
                 ["420 000 FCFA", "370 000 FCFA", "320 000 FCFA", "260 000 FCFA"], 1,
                 r"$C = 50\,000 + 2\,000 \times 160 = 370\,000$ FCFA. Doubling $n$ does not double $C$, because the fixed part stays the same.",
                 hint="Substitute $n = 160$ into the law. Do not just double the cost.",
                 feedback=["You doubled 210 000. That doubles the fixed fee as well, but the fixed fee is paid only once.", "",
                           "That is only the varying part, 2 000 × 160. Add the fixed part, 50 000 FCFA.",
                           "You added 50 000 to 210 000. Use the law with n = 160."]),
            H("Partly as x, partly as x²"),
            D(r"$y$ **varies partly as** $x$ **and partly as** $x^2$ when $y = ax + bx^2$. There is no constant term, so $y = 0$ when $x = 0$.",
              title="Definition: partial variation with a square", formula=r"y = ax + bx^2"),
            EX("Worked example 2: finding a and b", intro=(
                r"$y$ varies partly as $x$ and partly as $x^2$. When $x = 2$, $y = 16$, and when $x = 3$, $y = 33$. Find $y$ when $x = 4$."), steps=[
                S("Write the equation", math=r"y = ax + bx^2"),
                S("Substitute both pairs", math=r"2a + 4b = 16 \qquad 3a + 9b = 33"),
                S("Simplify each equation", math=r"a + 2b = 8 \qquad a + 3b = 11"),
                S("Subtract", math=r"b = 3, \quad a = 8 - 2 \times 3 = 2"),
                S("Write the law and substitute", math=r"y = 2x + 3x^2 \;\Rightarrow\; y = 8 + 48 = 56"),
            ], check=r"x = 3: \; 2(3) + 3(9) = 6 + 27 = 33"),
            EX("Worked example 3: stopping distance", intro=(
                "The stopping distance $d$ m of a car is partly proportional to its speed $v$ km/h and partly proportional to $v^2$. "
                "At 20 km/h, $d = 8$ m. At 40 km/h, $d = 24$ m. Find the stopping distance at 60 km/h."), steps=[
                S("Write the equation", math=r"d = av + bv^2"),
                S("Substitute both pairs", math=r"20a + 400b = 8 \qquad 40a + 1600b = 24"),
                S("Divide the first by 20 and the second by 40", math=r"a + 20b = 0.4 \qquad a + 40b = 0.6"),
                S("Subtract", math=r"20b = 0.2 \;\Rightarrow\; b = 0.01, \quad a = 0.2"),
                S("At 60 km/h", math=r"d = 0.2 \times 60 + 0.01 \times 3600 = 12 + 36 = 48 \text{ m}"),
            ]),
            H("Common mistakes"),
            MISTAKE("Treating partial variation as direct variation",
                    r"If $C = a + bn$, doubling $n$ does **not** double $C$, because of the fixed part $a$. Always find $a$ and $b$ first."),
            MISTAKE("Using only one pair of values", "Two unknown constants need two equations. Use both conditions given in the question."),
            MISTAKE("Forgetting to square in the second term", r"In $y = ax + bx^2$ with $x = 3$, the second term is $9b$, not $3b$ or $6b$."),
            H("Practice questions"),
            PQ("A taxi fare $F$ FCFA is partly constant and partly varies as the distance $d$ km. A 5 km trip costs 1 500 FCFA and a 10 km trip costs 2 500 FCFA. "
               "Find the fare for an 8 km trip.",
               r"$F = a + bd$. $a + 5b = 1\,500$ and $a + 10b = 2\,500$. Subtracting: $5b = 1\,000$, so $b = 200$ and $a = 500$. "
               r"For 8 km: $F = 500 + 200 \times 8 = 2\,100$ FCFA."),
            PQ(r"$y = a + bx$. When $x = 2$, $y = 11$, and when $x = 5$, $y = 20$. Find $a$ and $b$, then find $x$ when $y = 35$.",
               r"$a + 2b = 11$ and $a + 5b = 20$. Subtracting: $3b = 9$, so $b = 3$ and $a = 5$. Then $35 = 5 + 3x$, so $x = 10$."),
            PQ(r"$y$ varies partly as $x$ and partly as $x^2$. When $x = 1$, $y = 5$, and when $x = 2$, $y = 14$. Find $y$ when $x = 3$.",
               r"$y = ax + bx^2$. $a + b = 5$ and $2a + 4b = 14$, so $a + 2b = 7$. Subtracting: $b = 2$, $a = 3$. Then $y = 3(3) + 2(9) = 27$."),
            PQ("The cost of making $n$ school bags in a workshop in Bafoussam is partly constant and partly varies as $n$. "
               "20 bags cost 70 000 FCFA and 50 bags cost 130 000 FCFA. Find the cost of 100 bags.",
               r"$C = a + bn$. $a + 20b = 70\,000$ and $a + 50b = 130\,000$. Subtracting: $30b = 60\,000$, so $b = 2\,000$ and $a = 30\,000$. "
               r"Cost of 100 bags $= 30\,000 + 2\,000 \times 100 = 230\,000$ FCFA."),
            H("Summary"),
            SUM(r"Partly constant, partly varying as $x$: $y = a + bx$.",
                r"Partly as $x$, partly as $x^2$: $y = ax + bx^2$.",
                "Two constants need two conditions: substitute each pair to get two simultaneous equations.",
                "Solve for a and b (usually by subtracting), write the law, then substitute the new value.",
                "Doubling x does not double y in partial variation."),
        ],
    ),
]
