"""Form 5 Citizenship Education (O Level 0562): practice sets for Economic Life, Labour & Public Ethics; Human
Rights, Peace & Environmental Stewardship; Cameroon & International Organizations; and the Examination module.

Draft content: facts are general and well established; items that may have changed are hedged in the lessons. The
mock papers use KKEVO practice settings (time limits), not official Board settings. Paper 2 essays cannot be
marked automatically, so the Paper 2 sets test method, stimulus reading and application by multiple choice.
"""

import random

from .dsl import *  # noqa: F403

COURSE = ("citizenship-education", "form-5")

M_ECON = "Economic Life, Labour & Public Ethics"
M_RIGHTS = "Human Rights, Peace & Environmental Stewardship"
M_WORLD = "Cameroon & International Organizations"
M_EXAM = "Examination"

_BASE = [2, 0, 3, 1, 1, 3, 0, 2]


def Q(prompt, correct, wrongs, steps, concept, skill, hint, diagram="", alt=""):
    """Four-option MC spec. `wrongs` = [(text, why)] x3; position is chosen by build()."""
    if isinstance(steps, str):
        steps = [("Reasoning", steps)]
    return {"_q": True, "prompt": prompt, "correct": correct, "wrongs": wrongs, "steps": steps,
            "concept": concept, "skill": skill, "hint": hint, "diagram": diagram, "alt": alt}


def N(prompt, answer, steps, concept, skill, hint, tol=0, unit=""):
    if isinstance(steps, str):
        steps = [("Working", steps)]
    return NUM(prompt, answer, steps=[S(a, text=b) for a, b in steps], tolerance=tol, unit=unit,
               concept=concept, skill=skill, hint=hint)


def build(items, rot=0, pos=None):
    """Turn specs into MC questions, spreading the correct option over A-D."""
    out = []
    qi = 0
    for i, it in enumerate(items):
        if not it.get("_q"):
            out.append(it)
            continue
        p = (pos[qi] if pos else (_BASE[i % 8] + rot) % 4)
        qi += 1
        choices = [C(t, why=w) for t, w in it["wrongs"]]
        choices.insert(p, C(it["correct"], correct=True))
        out.append(MC(it["prompt"], choices, steps=[S(a, text=b) for a, b in it["steps"]], concept=it["concept"],
                      skill=it["skill"], hint=it["hint"], diagram=it["diagram"], diagram_alt=it["alt"]))
    return out



SETS = []


# ---------------------------------------------------------------------------------------------
# 1. Where the government gets its money
# ---------------------------------------------------------------------------------------------
T1 = "Government revenue and taxation"
SETS.append(practice_set(module=M_ECON, topic=T1, title="Sources of public revenue and spending",
    lesson="cit2-government-revenue-sources", questions=build([
    Q("What is public revenue?", "The money the State receives to pay for its work",
      [("The money the State spends each year", "That is public expenditure, not revenue."),
       ("The yearly plan of income and spending", "That is the budget."),
       ("Money that a citizen saves in a bank", "That is personal savings, not the State's money.")],
      "Revenue is what comes in; expenditure is what goes out.", "Public revenue", "Recall", "Is it money coming in or going out?"),
    Q("A passport fee paid to the State is an example of:", "Non-tax revenue",
      [("Tax revenue", "A fee for a service is not a tax, which is a compulsory payment not linked to a particular service."),
       ("Borrowing", "Borrowing is money received as a loan that must be repaid."),
       ("Capital expenditure", "Expenditure is spending, not revenue.")],
      "A fee for a service is non-tax revenue, with fines and income from State resources.", "Non-tax revenue", "Concept", "Is the payment for a particular service?"),
    Q("Which of these is an example of capital expenditure?", "Building a bridge",
      [("Paying teachers' salaries", "Salaries are paid every year: current expenditure."),
       ("Buying fuel for government vehicles", "Fuel is used up quickly: current expenditure."),
       ("Paying interest on a loan", "Interest is a running cost of debt, part of debt service.")],
      "Capital expenditure buys lasting assets such as bridges and hospitals.", "Capital expenditure", "Concept", "Which item lasts for many years?"),
    N("A government plans revenue of 5 200 and expenditure of 5 650 (billion FCFA, invented for practice). Find the size of the deficit.", 450,
      [("Subtract", "Deficit = expenditure - revenue = 5 650 - 5 200."), ("Answer", "450 billion FCFA.")],
      "Budget deficit", "Calculation", "Which figure is larger, revenue or expenditure?", unit="billion FCFA"),
    Q("Who authorises the annual budget through the finance law in Cameroon?", "Parliament",
      [("The labour inspector", "Labour inspectors deal with employment disputes."),
       ("The local chief", "Chiefs are traditional authorities, not the authority for the State budget."),
       ("The taxpayer who pays most", "Budgets are voted by elected representatives, not by individual taxpayers.")],
      "The finance law is voted by Parliament (National Assembly and Senate).", "The finance law", "Recall", "The body that makes laws."),
    Q("Which statement about government borrowing is correct?", "A loan has to be repaid, usually with interest",
      [("A loan is a gift that never has to be repaid", "A grant may be a gift; a loan is not."),
       ("Borrowing is a kind of tax", "A tax is a compulsory payment; a loan is money lent."),
       ("Borrowing reduces the government's spending", "Borrowing adds to the money available to spend.")],
      "Loans must be repaid with interest, which becomes part of debt service.", "Borrowing", "Concept", "Think about what happens later."),
    Q("A government has a budget deficit. Which action would reduce the deficit?", "Collecting taxes more efficiently",
      [("Paying more salaries without new revenue", "That raises spending and widens the deficit."),
       ("Cancelling all taxes", "That cuts revenue and widens the deficit."),
       ("Ignoring the budget", "Without planning the gap remains.")],
      "To reduce a deficit raise revenue, reduce spending or both.", "Reducing a deficit", "Reasoning", "A deficit means spending is larger than revenue."),
    Q("Revenue is 900 and expenditure is 800 (invented figures). What does this show?", "A surplus of 100",
      [("A deficit of 100", "A deficit is when expenditure is the larger number."),
       ("A balanced budget", "A balance needs the two figures to be equal."),
       ("A deficit of 800", "800 is the expenditure, not the gap.")],
      "Revenue minus expenditure = 900 - 800 = 100, positive, so a surplus.", "Surplus and deficit", "Interpretation", "Subtract expenditure from revenue and look at the sign."),
    ], rot=0)))


# ---------------------------------------------------------------------------------------------
# 2. Taxes
# ---------------------------------------------------------------------------------------------
SETS.append(practice_set(module=M_ECON, topic=T1, title="Direct and indirect taxes, VAT and taxpayer duties",
    lesson="cit2-taxation-types-and-taxpayer-duties", questions=build([
    Q("What is a tax?", "A compulsory payment to the State that is not payment for a particular service",
      [("A voluntary gift to the government", "Taxes are compulsory, not voluntary."),
       ("A fine for breaking the law", "A fine is a penalty, which is non-tax revenue."),
       ("A loan made to the State", "A loan must be repaid; a tax is not repaid.")],
      "A tax is compulsory and not linked to a specific service received.", "Definition of tax", "Recall", "Is paying it a choice?"),
    Q("Which of these is an indirect tax?", "Value added tax (VAT)",
      [("Personal income tax", "It is paid directly by the earner: a direct tax."),
       ("Company profits tax", "It is paid directly by the firm: a direct tax."),
       ("Tax on land owned", "It is paid directly by the owner: a direct tax.")],
      "VAT is added to the price and borne by the final buyer.", "Direct and indirect taxes", "Concept", "Which tax is added to the price in a shop?"),
    Q("A tax takes the same percentage from every income. It is:", "Proportional",
      [("Progressive", "A progressive tax takes a higher percentage from higher incomes."),
       ("Regressive", "A regressive tax takes a larger share of low incomes."),
       ("Indirect", "Direct or indirect refers to how it is collected, not to the rate.")],
      "A fixed percentage for all is proportional.", "Types of tax rate", "Concept", "Does the rate change with income?"),
    N("A generator costs 100 000 FCFA before VAT. VAT is charged at 19.25% (a teaching rate; check the current rate). Find the VAT in FCFA.", 19250,
      [("Calculate", "100 000 x 19.25 / 100 = 19 250.")], "Calculating VAT", "Calculation", "Find 19.25 per cent of the price.", unit="FCFA"),
    Q("Ngum earns 100 000 FCFA and pays 10 000 FCFA tax. Mbarga earns 400 000 FCFA and pays 80 000 FCFA (invented). What kind of tax is this?", "Progressive, because the richer person pays a higher percentage",
      [("Proportional, because both pay some tax", "Proportional means the same percentage; here 10% and 20% differ."),
       ("Regressive, because Mbarga pays more francs", "Regressive means a lower percentage for higher incomes, but Mbarga pays 20% against 10%."),
       ("Indirect, because the tax office collects it", "Indirect refers to taxes added to prices.")],
      [("Rates", "Ngum: 10 000 / 100 000 = 10%. Mbarga: 80 000 / 400 000 = 20%."), ("Compare", "The higher income pays a higher percentage: progressive.")],
      "Progressive taxes", "Application", "Calculate each person's percentage first."),
    Q("Which statement describes tax evasion?", "Illegally hiding income to avoid paying tax due",
      [("Using legal reliefs to reduce tax", "That is tax avoidance, which uses the rules."),
       ("Paying tax on time and keeping receipts", "That is the duty of a taxpayer."),
       ("Asking the tax office to correct a mistake", "That is a taxpayer's right.")],
      "Evasion is illegal hiding of income or refusal to pay what is due.", "Tax evasion", "Concept", "Is it legal or illegal?"),
    Q("A shop owner never gives receipts so that sales cannot be counted for tax. What is the main effect on the community?", "The State loses revenue for schools, health and roads",
      [("Prices always fall", "Evasion does not guarantee lower prices."),
       ("The buyers pay less VAT", "Customers may still be charged VAT that is not passed on."),
       ("The government gets more money", "Less tax is collected, not more.")],
      "Hidden sales reduce public revenue, so there is less for public services.", "Effects of tax evasion", "Reasoning", "Where does public money come from?"),
    Q("Which is a quality of a good tax?", "It is certain: the taxpayer knows how much and when to pay",
      [("It is changed without notice", "A tax should be certain, not unpredictable."),
       ("It costs more to collect than it earns", "A good tax is cheap to collect."),
       ("It is unfair to the poor", "A good tax should be fair.")],
      "A good tax is fair, certain, convenient and cheap to collect.", "Qualities of a good tax", "Analysis", "Think of the four qualities."),
    ], rot=1)))


# ---------------------------------------------------------------------------------------------
# 3. Social security
# ---------------------------------------------------------------------------------------------
T2 = "Social security"
SETS.append(practice_set(module=M_ECON, topic=T2, title="Social security and the CNPS",
    lesson="cit2-social-security-cnps", questions=build([
    Q("What is social security?", "A system that protects people against loss of income from risks such as old age or accidents",
      [("A private shop that sells insurance to anyone", "That describes a private insurer, not a legal social security system."),
       ("A bank account kept only for one's own savings", "Social security pools contributions; it is not personal savings."),
       ("A tax paid on goods in the market", "That is a tax such as VAT.")],
      "Social security is organised by law and protects against risks to income.", "Social security", "Recall", "It protects against risks."),
    Q("Which body manages the main social security schemes for employees in Cameroon?", "The CNPS",
      [("CONAC", "CONAC is the anti-corruption commission."),
       ("ANIF", "ANIF studies suspicious financial transactions."),
       ("ELECAM", "ELECAM organises elections.")],
      "The CNPS (Caisse Nationale de Prévoyance Sociale) manages the main schemes.", "CNPS", "Recall", "The first letter stands for Caisse Nationale."),
    Q("Who pays contributions to the main social security schemes for employees?", "Employers, and in some branches the employees too",
      [("Only the unemployed", "Contributions come from working people and employers."),
       ("Only foreign companies", "All registered employers must contribute."),
       ("Nobody; the State pays everything", "Employers and workers contribute, according to the rules.")],
      "Contributions are a percentage of wages paid by employers and, for some branches, by employees.", "Contributions", "Concept", "Think about who has wages."),
    Q("A builder is injured by a fall on the building site where he is employed. Which branch is most relevant?", "Work accidents and occupational diseases",
      [("Old-age pension", "He has not retired."),
       ("Family benefits", "These concern maternity and children."),
       ("Consumer protection", "That is another topic about buyers.")],
      "Injury caused by the job falls under the work accident branch.", "Work accident benefits", "Application", "The risk is linked to the job."),
    N("A worker earns 150 000 FCFA a month. In an invented example the employee pays 4% and the employer 8%. How much is paid in total each month?", 18000,
      [("Employee share", "150 000 x 4 / 100 = 6 000."), ("Employer share", "150 000 x 8 / 100 = 12 000."), ("Total", "6 000 + 12 000 = 18 000.")],
      "Calculating contributions", "Calculation", "Work out each share, then add.", unit="FCFA"),
    Q("What is the main idea of solidarity in social security?", "Many contribute and those who face a risk are helped from the common fund",
      [("Each worker receives only what he paid in", "Benefits depend on rules and risks, not exact personal savings."),
       ("Only the richest members receive benefits", "Benefits follow the rules for the risk, not wealth."),
       ("Employers decide who is helped", "Rights are set by law.")],
      "Solidarity means pooling contributions to protect those who meet a risk.", "Solidarity", "Concept", "The word means standing together."),
    Q("Which difference between social security and private insurance is correct?", "Social security is organised by law, while private insurance is a contract bought by choice",
      [("Private insurance is compulsory by law, social security is not", "Social security is the legal scheme."),
       ("They are exactly the same thing", "They differ in their legal basis, who runs them and how contributions are set."),
       ("Social security is only for the unemployed", "It protects employees against several risks.")],
      "The legal basis and compulsion distinguish social security from private insurance.", "Social security and private insurance", "Analysis", "Which one is set by law?"),
    Q("An employer fails to register his workers with the CNPS. What is the most likely result?", "The workers are unprotected and the employer breaks the law",
      [("The workers receive double benefits", "Without registration, benefits are put at risk."),
       ("The CNPS pays the employer's share", "The employer remains responsible."),
       ("Nothing, because registration is optional", "Registration is a legal duty. Check the current rules.")],
      "Failure to register means no protection for the workers and penalties for the employer.", "Employer duties", "Reasoning", "Think about the duty of the employer."),
    ], rot=2)))


# ---------------------------------------------------------------------------------------------
# 4. Labour Code
# ---------------------------------------------------------------------------------------------
T3 = "The Labour Code"
SETS.append(practice_set(module=M_ECON, topic=T3, title="Rights and duties of employers and employees",
    lesson="cit2-labour-code-rights-duties", questions=build([
    Q("What is the Labour Code?", "The body of law that sets rights and duties of employers and employees",
      [("A list of public holidays", "Holidays are only a small part of employment rules."),
       ("A tax law for firms", "Tax laws are different from the Labour Code."),
       ("The rules of a trade union", "A union has its own rules; the Code is state law.")],
      "The Labour Code protects workers and sets fair working relations.", "Labour Code", "Recall", "Think of who is covered."),
    Q("An agreement in which a person works under an employer's authority for a wage is a(n):", "Employment contract",
      [("Trade union charter", "A charter belongs to a union."),
       ("Tax declaration", "A tax declaration is made to the tax office."),
       ("Consumer warranty", "A warranty concerns goods bought.")],
      "That is the definition of an employment contract.", "Employment contract", "Recall", "The agreement is between employer and employee."),
    Q("Which of these is a duty of an employer?", "Paying the wage on time and providing safe working conditions",
      [("Arriving on time every morning", "That is a duty of the employee."),
       ("Keeping the firm's trade secrets", "That is a duty of the employee."),
       ("Obeying lawful instructions", "That is a duty of the employee.")],
      "Employer duties include fair pay, safe conditions and registering workers with the CNPS.", "Duties of employers", "Concept", "What does the employer owe?"),
    Q("Which of these is a right of an employee?", "Freedom to join a trade union",
      [("Freedom to choose which orders to obey", "An employee must follow lawful instructions."),
       ("Freedom to take the firm's equipment home", "Employees must care for property."),
       ("Freedom to leave without notice, always", "Notice rules apply, depending on the contract.")],
      "Freedom of association, including joining a union, is protected by the Code.", "Rights of employees", "Concept", "A right protects the worker."),
    N("Suppose paid leave accrues at 1.5 working days for each month worked (a teaching rate; check the current rules). How many days after 8 months?", 12,
      [("Multiply", "8 x 1.5 = 12.")], "Paid leave", "Calculation", "Multiply the months by the rate.", unit="days"),
    Q("Nkeng is dismissed suddenly without notice after three years. What is the best first step?", "Keep her contract and payslips and consult the labour inspector",
      [("Take the employer's goods in return", "That would be wrong, and it is theft."),
       ("Do nothing, because workers have no rights", "The Code gives rights and a way to complain."),
       ("Go straight to the Supreme Court", "The Supreme Court is not the first stage.")],
      "Gather evidence and use conciliation through the labour inspector before the labour court.", "Settling labour disputes", "Application", "Which official reconciles employers and workers?"),
    Q("Which sequence shows the usual order for settling a labour dispute?", "Discussion, labour inspector, labour court",
      [("Labour court, discussion, labour inspector", "Courts come last, not first."),
       ("Labour inspector, strike, discussion", "Discussion comes before outside help."),
       ("Police, court, discussion", "The police are not the first stage.")],
      "Talk first, then conciliation by the labour inspector, then the labour court.", "Settling labour disputes", "Reasoning", "From the least formal to the most formal."),
    Q("A fixed-term contract differs from an indefinite one because it:", "Ends on a set date or when a task is finished",
      [("Has no legal force", "It has full legal force."),
       ("Can never be renewed under any rule", "The law limits how long and how often it can be renewed."),
       ("Is always oral", "A fixed-term contract is better in writing.")],
      "Fixed-term contracts have an end date or task; the law limits their length and renewal. Check the current rules.", "Types of contract", "Analysis", "Look at the words fixed and term."),
    ], rot=3)))


# ---------------------------------------------------------------------------------------------
# 5. Consumer protection
# ---------------------------------------------------------------------------------------------
T4 = "Consumer protection"
SETS.append(practice_set(module=M_ECON, topic=T4, title="Consumer rights, duties and redress",
    lesson="cit2-consumer-protection-rights", questions=build([
    Q("A consumer is a person who:", "Buys or uses goods and services for their own needs",
      [("Buys goods only to resell them", "That is a trader or reseller."),
       ("Produces goods in a factory", "That is a producer."),
       ("Collects taxes from shops", "That is a tax official.")],
      "A consumer uses goods and services for personal needs.", "Consumer", "Recall", "Think of who uses the goods."),
    Q("Which consumer right is broken when a label shows a false expiry date?", "The right to information",
      [("The right to vote", "A political right, not a consumer right."),
       ("The right to a passport", "Not a consumer right."),
       ("The right to a trade licence", "That is a right of traders.")],
      "Labels must give true information.", "Right to information", "Concept", "A label is meant to tell the truth."),
    N("A buyer pays for 5 kg of rice at 600 FCFA per kg, but the rice weighs only 4.5 kg. How much money did the buyer lose?", 300,
      [("Missing weight", "5 - 4.5 = 0.5 kg."), ("Value", "0.5 x 600 = 300 FCFA.")], "False weights and measures", "Calculation", "Find the missing weight first.", unit="FCFA"),
    Q("Which practice is an unfair trade practice?", "Selling goods after their expiry date",
      [("Displaying prices clearly", "That is good practice."),
       ("Giving a receipt", "That is good practice."),
       ("Using a tested scale", "That is correct practice.")],
      "Selling expired goods endangers consumers and is unfair.", "Unfair practices", "Concept", "Which one could harm the buyer?"),
    Q("Why are counterfeit medicines especially dangerous?", "They may contain no active ingredient or harmful substances",
      [("They are always cheaper, so people buy more", "The danger is health, not the price."),
       ("They are taxed twice", "That is not the main danger."),
       ("They make labels harder to print", "That is irrelevant to the danger.")],
      "A sick person may think they are treated when they are not, or be harmed.", "Counterfeit goods", "Reasoning", "What happens to the patient?"),
    Q("A customer buys earphones that stop working after one day. The seller refuses to help. Which step comes first?", "Return to the seller with the receipt and ask for redress",
      [("Break the seller's shop sign", "Violence is wrong and does not give redress."),
       ("Go directly to the Supreme Court", "Other steps come first."),
       ("Say nothing and buy again", "Silence lets cheating continue.")],
      "Redress starts with the seller, then trade officials or an association, then the courts.", "Redress", "Application", "Try the simplest peaceful step first."),
    Q("Which of these is a duty of a consumer?", "To keep receipts and check goods before buying",
      [("To demand refunds without a receipt always", "Receipts are needed to prove purchase."),
       ("To buy smuggled goods if cheaper", "Consumers should avoid unsafe and illegal goods."),
       ("To ignore labels", "Labels give important information.")],
      "Responsible consumers check goods, keep receipts and report cheating.", "Consumer duties", "Concept", "A responsible buyer prepares and records."),
    Q("A seller puts up a sign: 'No refunds, whatever the fault'. What is the best view?", "The sign cannot remove the buyer's legal right to redress for faulty goods",
      [("The sign is always lawful", "A notice cannot cancel legal rights."),
       ("The buyer can no longer complain", "The buyer can still seek redress. Check the current rules."),
       ("Only the seller may decide", "The law protects the buyer.")],
      "A sign cannot remove rights given by the consumer protection law. Check the current rules.", "Consumer rights and the law", "Analysis", "Can a notice override a law?"),
    ], rot=0, pos=[3, 1, 0, 2, 0, 2, 3, 1])))


# ---------------------------------------------------------------------------------------------
# 6. Public service ethics and anti-corruption
# ---------------------------------------------------------------------------------------------
T5 = "Public service ethics and anti-corruption"
SETS.append(practice_set(module=M_ECON, topic=T5, title="Ethics, corruption and the anti-corruption bodies",
    lesson="cit2-public-service-ethics-anti-corruption", questions=build([
    Q("Corruption is best defined as:", "The abuse of public office or power for private gain",
      [("Any payment made by a citizen to the State", "Taxes and fees are lawful payments."),
       ("A disagreement between two civil servants", "That is a conflict, not corruption."),
       ("The slow delivery of documents", "Slowness may be poor service, but corruption involves private gain.")],
      "Corruption means misusing a position for private benefit.", "Corruption", "Recall", "Private gain from public office."),
    Q("A clerk demands money for a form that is free. This is an example of:", "Extortion, a form of bribery",
      [("Nepotism", "Nepotism favours relatives."),
       ("Tax avoidance", "That is using legal rules to pay less tax."),
       ("Good public service", "A free service should be given without payment.")],
      "Demanding payment for a free service is extortion.", "Forms of corruption", "Concept", "He demands payment for something free."),
    Q("A director gives a contract to his brother although a better bidder applied. This is:", "Nepotism",
      [("Embezzlement", "Embezzlement is theft of funds that one manages."),
       ("Impartiality", "Impartiality means treating everyone equally."),
       ("Accountability", "Accountability means being answerable for decisions.")],
      "Favouring a relative is nepotism.", "Forms of corruption", "Application", "Think of the word relative."),
    Q("Which value is shown by a public servant who treats all citizens equally, whatever their tribe or religion?", "Impartiality",
      [("Favouritism", "That is the opposite value."),
       ("Extortion", "That is a form of corruption."),
       ("Secrecy", "Secrecy is not the same as fairness.")],
      "Impartiality means no favouritism.", "Values of public servants", "Concept", "Equal treatment."),
    Q("Which body receives and studies reports of suspicious financial transactions?", "ANIF",
      [("CONAC", "CONAC receives reports of corruption and investigates; it studies the corruption, not financial intelligence."),
       ("The Audit Bench", "It audits public accounts."),
       ("The Special Criminal Court", "It tries cases of embezzlement.")],
      "ANIF is the financial investigation agency.", "ANIF", "Recall", "The F stands for financial."),
    Q("Which statement about CONAC is correct?", "It investigates reports of corruption but is not a court",
      [("It tries and sentences all offenders", "That is the work of the courts."),
       ("It makes the laws of the country", "That is Parliament."),
       ("It collects taxes", "That is the tax administration.")],
      "CONAC is a commission that receives reports, investigates and refers files; it does not judge.", "CONAC", "Concept", "Commission or court?"),
    Q("Which body audits and judges the accounts of public accountants?", "The Audit Bench of the Supreme Court",
      [("ANIF", "ANIF studies suspicious transactions."),
       ("The National Assembly", "The Assembly makes laws and votes the budget."),
       ("A Court of First Instance", "It does not audit public accounts.")],
      "The Audit Bench checks public accounts.", "Audit Bench", "Recall", "Which institution is an auditor of accounts?"),
    Q("A bank sees unusual cash transfers that might hide stolen public money. To whom should it report first?", "ANIF",
      [("The Audit Bench", "It audits accounts of public accountants."),
       ("The local chief", "A chief has no role in financial intelligence."),
       ("The Labour inspector", "That official deals with employment disputes.")],
      [("Spot the clue", "Unusual cash transfers: suspicious transactions."), ("Match", "ANIF receives and studies them.")],
      "Financial intelligence", "Analysis", "Which agency studies suspicious transactions?"),
    ], rot=1)))


# ---------------------------------------------------------------------------------------------
# 7. Human rights
# ---------------------------------------------------------------------------------------------
T6 = "Human rights"
SETS.append(practice_set(module=M_RIGHTS, topic=T6, title="The UDHR, kinds of rights and the NCHRF",
    lesson="cit2-human-rights-udhr-nchrf", questions=build([
    Q("Human rights are:", "Basic rights that every person has because they are human",
      [("Rights only for citizens who pay taxes", "Human rights belong to everyone."),
       ("Privileges given by a government to its supporters", "Rights are not favours."),
       ("Rights that only adults have", "Children have human rights too.")],
      "Human rights are universal and inalienable.", "Human rights", "Recall", "Who has them?"),
    Q("When was the Universal Declaration of Human Rights adopted?", "10 December 1948",
      [("24 October 1945", "That is when the UN Charter came into force."),
       ("9 July 2002", "That is when the African Union was launched."),
       ("1 January 1960", "That is the independence date of Cameroun.")],
      "The UN General Assembly adopted the UDHR in Paris on 10 December 1948.", "UDHR", "Recall", "Human Rights Day is celebrated on this date."),
    Q("Which body adopted the UDHR?", "The United Nations General Assembly",
      [("The African Union Assembly", "The AU was launched in 2002."),
       ("The Security Council", "It was the General Assembly that adopted the UDHR."),
       ("The Commonwealth Secretariat", "The Commonwealth did not adopt it.")],
      "The UDHR was adopted by the UN General Assembly.", "UDHR", "Recall", "It is a body with all UN members."),
    Q("Which of these is an economic, social or cultural right?", "The right to education",
      [("The right to a fair trial", "A civil right."),
       ("The right to vote", "A political right."),
       ("Freedom from torture", "A civil right.")],
      "Education is an economic, social and cultural right.", "Kinds of rights", "Concept", "Which right concerns well-being and development?"),
    Q("Which statement about the UDHR is correct?", "It is a declaration of common standards that has inspired treaties and constitutions",
      [("It is a treaty that punishes states directly", "It is a declaration, not a treaty with its own punishments."),
       ("It has 100 articles", "It has 30 articles."),
       ("It was adopted in 1963", "It was adopted in 1948.")],
      "The UDHR has a preamble and 30 articles; it is not a treaty.", "Nature of the UDHR", "Concept", "Number of articles and type of text."),
    Q("A student says 'I have freedom of speech, so I can say anything about anyone.' What is the best reply?", "Rights have limits and must respect the rights of others",
      [("She is right, because rights are unlimited", "Rights are limited by the rights of others."),
       ("She has no rights at all", "She has the right, but within limits."),
       ("Rights belong only to adults", "Rights belong to everyone.")],
      "Rights come with duties and may be limited by law to protect others and public order.", "Rights and duties", "Application", "Think about the effect of your words on others."),
    Q("What is one function of the National Commission on Human Rights and Freedoms (NCHRF)?", "Receiving complaints and investigating human rights abuses",
      [("Passing the budget", "That is Parliament."),
       ("Collecting taxes", "That is the tax administration."),
       ("Replacing the courts", "It is not a court; it refers and recommends.")],
      "The NCHRF promotes and protects rights; it receives complaints and investigates.", "NCHRF", "Concept", "It is a body for rights and freedoms."),
    Q("Which pair is correctly matched?", "Right to vote - civil and political right",
      [("Right to health - civil and political right", "Health is an economic, social and cultural right."),
       ("Right to a fair trial - cultural right", "A fair trial is a civil right."),
       ("Right to education - political right", "Education is a social right.")],
      "Voting is taking part in government: civil and political.", "Classifying rights", "Analysis", "Which pair puts the right in its correct family?"),
    ], rot=2)))


# ---------------------------------------------------------------------------------------------
# 8. Women, children, minorities
# ---------------------------------------------------------------------------------------------
T7 = "Protection of women, children and minorities"
SETS.append(practice_set(module=M_RIGHTS, topic=T7, title="Protecting women, children and minorities",
    lesson="cit2-protection-women-children-minorities", questions=build([
    Q("Discrimination means:", "Unfair treatment because of sex, origin or similar",
      [("Treating all people equally and fairly", "That is equality."),
       ("Helping a person who is in need", "That is assistance."),
       ("Making a law in Parliament", "That is legislation.")],
      "Discrimination is unfair treatment because of a characteristic.", "Discrimination", "Recall", "It is the opposite of equal treatment."),
    Q("Which international convention aims to end discrimination against women?", "CEDAW",
      [("The Convention on the Rights of the Child", "That concerns children."),
       ("The Geneva Conventions", "They concern victims of war."),
       ("The Vienna Convention", "It deals with diplomatic relations.")],
      "CEDAW was adopted by the UN in 1979.", "CEDAW", "Recall", "The W stands for women."),
    Q("In general, who is a child under the child rights conventions?", "A person under 18",
      [("A person under 10", "The age is higher."),
       ("A person under 14", "14 is the usual minimum working age in the Labour Code, not the age of a child."),
       ("A person under 25", "That is too high.")],
      "A child is generally a person under 18.", "Definition of a child", "Recall", "Think of when a person becomes an adult."),
    Q("Which is a right of the child?", "Protection from harmful work and abuse",
      [("To decide alone on all family matters", "Children are heard, but adults share responsibility."),
       ("To be free from every rule", "Children also need guidance and rules."),
       ("To leave school at any age", "Children have a right to education.")],
      "Rights include survival, education, protection and being heard.", "Rights of the child", "Concept", "A right that protects the child."),
    Q("A girl of 13 is taken out of school to be married. Which right is most clearly at risk?", "The right to education and protection from early marriage",
      [("The right to hold a trade licence", "That concerns traders."),
       ("The right to vote", "A child cannot vote yet; the main risks are different."),
       ("The right to a passport", "That is not the main risk.")],
      "Early marriage endangers education, health and freedom of choice.", "Early marriage", "Application", "What does she lose by leaving school?"),
    Q("What does the principle of the 'best interests of the child' require?", "The child's well-being comes first in decisions",
      [("That the child makes all decisions alone", "Children are heard but not left to decide everything."),
       ("That adults ignore the child's views", "The child's views must be heard."),
       ("That parents have no say", "Parents have responsibilities.")],
      "Adults must give priority to the child's welfare.", "Best interests of the child", "Concept", "Whose well-being comes first?"),
    Q("Which statement about minorities is correct?", "Equal treatment and respect for their culture",
      [("They should be given fewer rights than others", "Minorities have equal rights."),
       ("They must give up their languages", "Their culture should be respected."),
       ("They need no protection at all", "They may face discrimination, so protection is needed.")],
      "The Constitution's preamble commits the State to protect minorities and indigenous populations.", "Minorities", "Concept", "Think of equality and respect."),
    Q("A school refuses to admit a child with a disability. Which principle is broken?", "Equality and non-discrimination",
      [("Compulsory voting", "Not relevant."),
       ("Free trade", "A trade principle, not relevant here."),
       ("Diplomatic immunity", "That concerns diplomats.")],
      "Excluding someone because of disability is discrimination.", "Protecting persons with disabilities", "Analysis", "The child is treated unfairly because of a characteristic."),
    ], rot=3)))


# ---------------------------------------------------------------------------------------------
# 9. International humanitarian law
# ---------------------------------------------------------------------------------------------
T8 = "International humanitarian law"
SETS.append(practice_set(module=M_RIGHTS, topic=T8, title="Rules of war and the Geneva Conventions",
    lesson="cit2-international-humanitarian-law", questions=build([
    Q("International humanitarian law applies:", "During armed conflict",
      [("Only in times of peace", "Human rights law applies at all times; IHL applies in armed conflict."),
       ("Only in elections", "IHL is not about elections."),
       ("Only in schools", "IHL is not about schools.")],
      "IHL limits the effects of armed conflict.", "Definition of IHL", "Recall", "It is also called the law of war."),
    Q("In which year were the four Geneva Conventions adopted?", "1949",
      [("1863", "That is when the ICRC was founded."),
       ("1945", "That is when the UN Charter came into force."),
       ("1977", "The Additional Protocols date from 1977.")],
      "The four Geneva Conventions date from 1949.", "Geneva Conventions", "Recall", "The Protocols came later."),
    Q("Which Geneva Convention protects prisoners of war?", "The third",
      [("The first", "The first protects wounded and sick soldiers on land."),
       ("The second", "The second protects the wounded, sick and shipwrecked at sea."),
       ("The fourth", "The fourth protects civilians.")],
      "The third Geneva Convention is about prisoners of war.", "Geneva Conventions", "Recall", "The conventions are numbered in order of the groups protected."),
    Q("Who founded the movement that led to the Red Cross?", "Henry Dunant",
      [("Kofi Annan", "He was a UN Secretary-General."),
       ("Nelson Mandela", "He was a South African leader."),
       ("Winston Churchill", "He was a British Prime Minister.")],
      "Henry Dunant was moved by the suffering after the Battle of Solferino in 1859.", "The Red Cross", "Recall", "He was Swiss."),
    Q("The principle of distinction requires parties to a conflict to:", "Tell fighters from civilians, and targets from civilian objects",
      [("Attack every building in the area", "Civilian objects are protected."),
       ("Treat all people alike as enemies", "Civilians must be spared."),
       ("Use the biggest weapons available", "Force must be limited.")],
      "Distinction means attacking only military targets.", "Principles of IHL", "Concept", "The word means telling apart."),
    Q("A soldier beats a captured fighter to make him talk. Which rule is broken?", "The ban on torture and cruel treatment",
      [("The rule of distinction", "That concerns civilians and fighters."),
       ("The rule of proportionality", "That concerns excessive harm to civilians."),
       ("The rule of diplomatic immunity", "That concerns diplomats.")],
      "Prisoners must be treated humanely; torture is forbidden.", "Treatment of prisoners", "Application", "A prisoner must be treated humanely."),
    Q("Which of these is protected by IHL?", "A hospital and its medical staff",
      [("A weapons store", "A military target, not protected."),
       ("A battle plan", "Not a protected object."),
       ("A military barracks", "A military target.")],
      "Hospitals, ambulances and medical staff are protected.", "Protected persons and places", "Concept", "Which one helps the wounded?"),
    Q("Which statement is correct?", "War crimes can be punished by national or international courts",
      [("War crimes cannot be punished by any court", "Individuals can be tried."),
       ("Only soldiers can be held responsible", "Commanders and others can be held responsible too."),
       ("IHL forbids all fighting everywhere", "It limits how conflicts are fought; it does not by itself forbid every use of force.")],
      "War crimes can be tried by national courts or by the International Criminal Court.", "War crimes", "Analysis", "Think about responsibility."),
    ], rot=0)))


# ---------------------------------------------------------------------------------------------
# 10. Conflict resolution and peace
# ---------------------------------------------------------------------------------------------
T9 = "Conflict resolution and peace"
SETS.append(practice_set(module=M_RIGHTS, topic=T9, title="Settling conflicts peacefully",
    lesson="cit2-conflict-resolution-peace", questions=build([
    Q("A conflict is best described as:", "A disagreement between people with opposing interests",
      [("A friendly agreement between neighbours", "That is the opposite."),
       ("A law passed by Parliament", "A law is a rule, not a conflict."),
       ("A kind of tax paid to the State", "A tax is a payment to the State.")],
      "A conflict is a disagreement or struggle over needs or interests.", "Conflict", "Recall", "Opposing needs."),
    Q("Which is a common cause of conflict?", "Competition for scarce resources such as land and water",
      [("Plenty of land and water for everyone", "Conflict is more likely when resources are scarce."),
       ("Good communication between neighbours", "Poor communication, not good, causes conflict."),
       ("Equal treatment of everyone", "Unfair treatment causes conflict.")],
      "Scarce resources, unfair treatment, misunderstanding and differences of interest can cause conflict.", "Causes of conflict", "Concept", "Which cause leads to competition?"),
    Q("In negotiation:", "The parties talk directly to reach an agreement",
      [("A judge decides the case", "That is adjudication."),
       ("A neutral person gives a binding decision", "That is arbitration."),
       ("One side forces the other to agree", "That is not negotiation.")],
      "Negotiation is direct talks between the parties.", "Negotiation", "Concept", "Who is in the room?"),
    Q("What is the main difference between mediation and arbitration?", "A mediator helps; an arbitrator gives a decision",
      [("There is no difference between them", "The role of the third person differs."),
       ("A mediator is always a judge of a court", "A mediator is neutral but does not judge."),
       ("Arbitration never involves a third person", "It always involves a neutral third person or panel.")],
      "Mediation helps agreement; arbitration produces a decision.", "Mediation and arbitration", "Concept", "Who makes the decision?"),
    Q("Two traders cannot agree. An elder listens and proposes a solution which they are free to accept or reject. This is:", "Mediation",
      [("Arbitration", "In arbitration the decision is accepted in advance."),
       ("Adjudication", "Adjudication is by a judge."),
       ("Compromise", "A compromise is the result, not the method.")],
      "A neutral helper who proposes but cannot impose is a mediator.", "Mediation", "Application", "Can the elder force them?"),
    Q("Which court at The Hague settles legal disputes between states that agree to bring them?", "The International Court of Justice",
      [("The African Court on Human and Peoples' Rights", "It deals with African human rights cases."),
       ("The Supreme Court of Cameroon", "It is a national court."),
       ("The Special Criminal Court", "It is a Cameroonian court for large embezzlement cases.")],
      "The ICJ is the main judicial organ of the UN.", "International Court of Justice", "Recall", "It is the UN's main court."),
    Q("Which is an example of positive peace?", "A society with justice, rights and chances to develop",
      [("A pause in fighting while both sides prepare", "That is only a temporary absence of violence."),
       ("Silence caused by fear", "Fear is not peace."),
       ("A country with a large army", "An army alone does not give peace.")],
      "Positive peace is more than the absence of war.", "Culture of peace", "Interpretation", "More than just no war."),
    Q("Which behaviour best contributes to a culture of peace in a school?", "Listening to others and settling quarrels through talks",
      [("Spreading rumours about a rival", "Rumours fuel conflict."),
       ("Excluding classmates from other regions", "That is discrimination."),
       ("Settling quarrels by fighting", "Violence harms the school.")],
      "A culture of peace uses dialogue, tolerance and respect.", "Culture of peace", "Application", "Which one is peaceful?"),
    ], rot=1)))


# ---------------------------------------------------------------------------------------------
# 11. Environment and climate change
# ---------------------------------------------------------------------------------------------
T10 = "The environment and climate change"
SETS.append(practice_set(module=M_RIGHTS, topic=T10, title="Degradation, climate change and conservation",
    lesson="cit2-environment-climate-change", questions=build([
    Q("Conservation means:", "Using natural resources carefully so that they last",
      [("Using up resources as fast as possible", "That is wasteful."),
       ("Never using any resource", "Conservation allows wise use."),
       ("Selling all forests", "That destroys the resource.")],
      "Conservation is the careful use and protection of resources.", "Conservation", "Recall", "Think of the word keep."),
    Q("Which activity is a cause of deforestation?", "Cutting trees for farmland, firewood and timber",
      [("Planting new trees", "That restores forests."),
       ("Using improved stoves", "That reduces firewood use."),
       ("Protecting national parks", "That helps conserve forests.")],
      "Deforestation is mainly caused by clearing forests for farming, fuel and timber.", "Deforestation", "Concept", "Which action removes trees?"),
    Q("The greenhouse effect is the:", "Trapping of heat in the atmosphere by certain gases",
      [("Making of a glass building", "It is only a comparison."),
       ("Growing of crops in the dry season", "That is irrigation."),
       ("Destruction of the ozone layer", "That is a different environmental issue.")],
      "Gases such as carbon dioxide trap some of the Earth's heat.", "Greenhouse effect", "Concept", "Think of heat and gases."),
    Q("Which gas, released when fossil fuels are burned, is the main human-made greenhouse gas?", "Carbon dioxide",
      [("Oxygen", "Oxygen is essential for life and is not the main concern."),
       ("Nitrogen", "Nitrogen does not trap heat strongly."),
       ("Helium", "Helium plays no part.")],
      "Burning fossil fuels releases carbon dioxide.", "Greenhouse gases", "Recall", "Plants take it in."),
    Q("Which pairing of cause and effect is correct?", "Blocked drains full of plastic and flooding after heavy rain",
      [("Planting trees and soil erosion", "Trees hold soil; they reduce erosion."),
       ("Recycling and more waste", "Recycling reduces waste."),
       ("Using clean energy and more smoke", "Clean energy reduces smoke.")],
      "Blocked drains cannot carry rainwater away, so floods follow.", "Causes and effects", "Application", "Which cause leads to that effect?"),
    Q("Which long-term effect do scientists link to climate change?", "More droughts and floods and rising sea levels",
      [("A guaranteed rise in rainfall everywhere", "Rainfall patterns vary: some places get less."),
       ("An end of all seasons everywhere", "Seasons change but do not vanish."),
       ("A fall in temperatures worldwide", "Global warming is a rise.")],
      "Climate change brings higher temperatures and more extreme weather.", "Effects of climate change", "Concept", "Think of extreme weather."),
    Q("The Paris Agreement of 2015 aims to:", "Keep global warming well below 2 degrees Celsius",
      [("Ban all air travel between countries", "It does not ban travel."),
       ("Stop the use of all fresh water", "It does not concern that."),
       ("End all trade between rich and poor countries", "It is not a trade ban.")],
      "The Paris Agreement of 2015 commits countries to limit global warming.", "Paris Agreement", "Recall", "It is about temperature."),
    Q("Which action by a school is most in keeping with sustainable development?", "Cutting a few trees and planting new ones to replace them",
      [("Cutting all the trees now to sell the wood", "That leaves nothing for the future."),
       ("Burning plastic waste in the open", "That pollutes the air."),
       ("Draining a stream for no purpose", "That destroys a resource.")],
      "Sustainable development meets present needs without harming future generations.", "Sustainable development", "Analysis", "Can the action continue in the future?"),
    ], rot=2)))


# ---------------------------------------------------------------------------------------------
# 12. Diplomacy
# ---------------------------------------------------------------------------------------------
T11 = "Diplomacy"
SETS.append(practice_set(module=M_WORLD, topic=T11, title="Bilateral and multilateral diplomacy",
    lesson="cit2-diplomacy-bilateral-multilateral", questions=build([
    Q("Diplomacy is:", "The management of relations between states by peaceful means",
      [("The use of armed force to settle disputes", "That is war."),
       ("The collection of taxes from foreigners", "That is not diplomacy."),
       ("The writing of national laws", "That is legislation.")],
      "Diplomacy means peaceful dealings between states.", "Diplomacy", "Recall", "Peaceful relations."),
    Q("A trade agreement between Cameroon and one other country is an example of:", "Bilateral diplomacy",
      [("Multilateral diplomacy", "Multilateral involves three or more states."),
       ("Domestic policy", "It involves another country."),
       ("A civil case", "It is not a court case.")],
      "Two states: bilateral.", "Bilateral diplomacy", "Concept", "Count the states."),
    Q("What is the head of an embassy called?", "An ambassador",
      [("A consul", "A consul heads a consulate."),
       ("A governor", "A governor heads a region."),
       ("A mayor", "A mayor heads a council.")],
      "An ambassador leads an embassy.", "Ambassador", "Recall", "He represents the head of state."),
    Q("A Cameroonian loses a passport in a foreign city where Cameroon has a consulate. Who can help?", "The consul",
      [("The ambassador of another country", "He represents his own country."),
       ("The UN Secretary-General", "He does not issue national passports."),
       ("The local chief at home", "He has no authority abroad.")],
      "Consulates help citizens abroad with documents.", "Consulate", "Application", "Which office helps individual citizens abroad?"),
    Q("Which is an example of multilateral diplomacy?", "A summit of the African Union",
      [("A letter between two presidents", "Two states: bilateral."),
       ("A consul renewing a passport", "That is consular work."),
       ("A visit by one minister to one country", "A bilateral visit.")],
      "Many states in an organisation: multilateral.", "Multilateral diplomacy", "Concept", "Many countries at once."),
    Q("What is the title of the head of a mission between two Commonwealth countries?", "High commissioner",
      [("Chancellor", "A chancellor heads a university or a government in some countries."),
       ("Prefect", "A prefect heads a division."),
       ("Speaker", "A speaker presides over an assembly.")],
      "Commonwealth missions are called high commissions.", "High commissioner", "Recall", "It is not called an embassy."),
    Q("Diplomatic immunity exists so that diplomats can:", "Do their work freely without fear of arrest in the host country",
      [("Break the law without consequences", "They can be expelled and prosecuted at home."),
       ("Avoid learning the local language", "Not the purpose."),
       ("Avoid paying their staff", "Not the purpose.")],
      "Immunity protects free and safe diplomatic work under the Vienna Convention (1961).", "Diplomatic immunity", "Concept", "Think of the reason."),
    Q("Why do countries need diplomatic relations?", "To prevent conflict, promote trade and protect their citizens abroad",
      [("To end all contact with other countries", "Diplomacy is about contact."),
       ("To hide their national interests", "Countries pursue their interests openly through talks."),
       ("To replace their own governments", "Diplomacy does not do that.")],
      "Diplomacy allows talks, trade, cooperation and help for citizens abroad.", "Purpose of diplomacy", "Analysis", "Which choice benefits the country?"),
    ], rot=3)))


# ---------------------------------------------------------------------------------------------
# 13. Regional organizations
# ---------------------------------------------------------------------------------------------
T12 = "Regional organizations"
SETS.append(practice_set(module=M_WORLD, topic=T12, title="CEMAC, ECCAS and the African Union",
    lesson="cit2-regional-organizations-cemac-eccas-au", questions=build([
    Q("What does regional integration mean?", "Neighbouring countries cooperating in trade, security and development",
      [("A country closing its borders to trade", "That is the opposite."),
       ("A country joining the UN", "That is global, not regional."),
       ("A civil war inside one country for years", "That is not integration.")],
      "Regional integration means neighbours working together.", "Regional integration", "Recall", "Think about neighbours."),
    Q("Which of these is a member of CEMAC?", "Gabon",
      [("Nigeria", "Nigeria is in West Africa."),
       ("Kenya", "Kenya is in East Africa."),
       ("Ghana", "Ghana is in West Africa.")],
      "CEMAC members: Cameroon, CAR, Chad, Republic of the Congo, Equatorial Guinea and Gabon.", "CEMAC members", "Recall", "CEMAC is Central African."),
    Q("Where are the headquarters of CEMAC?", "Bangui",
      [("Addis Ababa", "That is the African Union's headquarters."),
       ("Libreville", "That is ECCAS's headquarters."),
       ("New York", "That is the UN's headquarters.")],
      "CEMAC's headquarters are in Bangui.", "CEMAC", "Recall", "It is in the Central African Republic."),
    Q("Which currency is shared by the CEMAC states?", "The CFA franc",
      [("The naira", "That is Nigeria's currency."),
       ("The euro", "The euro is used in part of Europe."),
       ("The pound sterling", "That is the UK's currency.")],
      "The CFA franc is issued by the Bank of Central African States.", "CEMAC", "Recall", "A franc used in Central Africa."),
    Q("The African Union was launched in:", "2002, in Durban",
      [("1963, in Addis Ababa", "That is the founding of the OAU."),
       ("1945, in San Francisco", "That is the UN."),
       ("1983, in Libreville", "That is ECCAS.")],
      "The AU replaced the OAU in 2002.", "African Union", "Recall", "It replaced the OAU."),
    Q("Which statement distinguishes ECCAS from CEMAC?", "ECCAS is wider and was founded in 1983",
      [("ECCAS is smaller than CEMAC", "ECCAS has more members."),
       ("ECCAS was founded in 1994 in Bangui", "That is when CEMAC was created."),
       ("ECCAS has its headquarters in Bangui", "ECCAS has its headquarters in Libreville.")],
      "ECCAS (1983, Libreville) has more members than CEMAC (1994, Bangui).", "ECCAS", "Concept", "Compare the sizes and dates."),
    Q("A trader finds that checkpoints and informal payments slow his goods between two CEMAC states. Which problem of integration is this?", "Weak enforcement of agreed rules on free movement",
      [("Too many shared languages", "That is not the problem described."),
       ("A shortage of members", "Not the problem described."),
       ("Excess of rainfall", "Not relevant.")],
      "CEMAC aims at free movement, but weak enforcement and checkpoints slow trade.", "Problems of integration", "Application", "The aim is free movement of goods."),
    Q("Which organ of the African Union works on preventing and managing conflicts?", "The Peace and Security Council",
      [("The Pan-African Parliament", "It is a consultative parliament."),
       ("The Commonwealth Secretariat", "That belongs to the Commonwealth."),
       ("The Trusteeship Council", "That is a UN organ.")],
      "The Peace and Security Council deals with conflicts.", "Organs of the African Union", "Analysis", "The name includes peace."),
    ], rot=0, pos=[0, 2, 1, 3, 2, 0, 3, 1])))


# ---------------------------------------------------------------------------------------------
# 14. UN, Commonwealth, Francophonie
# ---------------------------------------------------------------------------------------------
T13 = "The United Nations, the Commonwealth and La Francophonie"
SETS.append(practice_set(module=M_WORLD, topic=T13, title="The UN, the Commonwealth and La Francophonie",
    lesson="cit2-un-commonwealth-francophonie", questions=build([
    Q("On which date did the UN Charter come into force?", "24 October 1945",
      [("10 December 1948", "That is the date of the UDHR."),
       ("9 July 2002", "That is the launch of the AU."),
       ("25 May 1963", "That is the foundation of the OAU.")],
      "24 October is celebrated as United Nations Day.", "United Nations", "Recall", "A date in 1945."),
    Q("Where are the headquarters of the United Nations?", "New York",
      [("Geneva", "That is the base of the ICRC and many UN offices."),
       ("Paris", "That is the base of La Francophonie."),
       ("London", "That is the base of the Commonwealth Secretariat.")],
      "The UN headquarters are in New York.", "United Nations", "Recall", "A city in the USA."),
    Q("How many permanent members does the Security Council have?", "Five",
      [("Three", "There are more than three."),
       ("Ten", "That is the number of elected members."),
       ("Fifteen", "That is the total membership.")],
      "Five permanent members with a veto and ten elected members make fifteen.", "Security Council", "Recall", "Fifteen in total."),
    Q("Which UN organ settles legal disputes between states?", "The International Court of Justice",
      [("The General Assembly", "It debates and recommends."),
       ("The Secretariat", "It is the administrative staff."),
       ("The Economic and Social Council", "It coordinates economic and social work.")],
      "The ICJ at The Hague is the main judicial organ.", "UN organs", "Concept", "A court."),
    Q("Which UN agency works for education, science and culture?", "UNESCO",
      [("WHO", "It works for health."),
       ("FAO", "It works for food and agriculture."),
       ("UNICEF", "It works for children.")],
      "UNESCO deals with education, science and culture.", "Specialised agencies", "Recall", "The E stands for educational."),
    Q("The Commonwealth is best described as:", "A voluntary association, mostly of former British territories",
      [("A world government that gives orders to members", "It cannot order members."),
       ("A military alliance of English-speaking states", "It is not a military alliance."),
       ("A trade union of Central African workers", "It is worldwide.")],
      "Members choose to belong and are equal partners.", "The Commonwealth", "Concept", "Think of voluntary."),
    Q("Which pair is correct?", "La Francophonie - headquarters in Paris",
      [("The Commonwealth - headquarters in New York", "The Secretariat is in London."),
       ("The United Nations - headquarters in Addis Ababa", "The UN is in New York."),
       ("The African Union - headquarters in Paris", "The AU is in Addis Ababa.")],
      "La Francophonie has its headquarters in Paris.", "La Francophonie", "Recall", "French-speaking."),
    Q("Why does Cameroon belong to both the Commonwealth and La Francophonie?", "It has English and French as official languages",
      [("It is forced to join every organisation", "Membership is voluntary."),
       ("They are branches of the African Union", "They are separate associations."),
       ("It has no other international links", "It also belongs to the UN, the AU, CEMAC and ECCAS.")],
      "Membership reflects its bilingual heritage.", "Cameroon's memberships", "Analysis", "Think about languages."),
    ], rot=1)))


# ---------------------------------------------------------------------------------------------
# 15. Paper 1 strategy
# ---------------------------------------------------------------------------------------------
P1 = "Paper 1"
SETS.append(practice_set(module=M_EXAM, topic=P1, title="Paper 1 technique: timing, elimination and objectives",
    lesson="citx-paper-1-multiple-choice-strategy", questions=build([
    Q("According to the Board's 2023 report, how many multiple-choice questions are in Paper 1?", "50",
      [("25", "The paper is longer than that."),
       ("40", "That is not the number in the report."),
       ("100", "That would be twice the actual number.")],
      "The report states that candidates answer all 50 multiple-choice questions.", "Structure of Paper 1", "Recall", "It is a round number between 40 and 100."),
    Q("Which share of Paper 1 tests knowledge, according to the report?", "38%",
      [("12%", "That is analysis."),
       ("20%", "That is application."),
       ("30%", "That is comprehension.")],
      "Knowledge 38%, comprehension 30%, application 20%, analysis 12%.", "Objectives of Paper 1", "Recall", "It is the largest share."),
    N("A paper has 50 questions and you have 90 minutes (a KKEVO practice setting). How many minutes can you spend on each question on average?", 1.8,
      [("Divide", "90 / 50 = 1.8 minutes.")], "Timing", "Calculation", "Divide the total time by the number of questions.", tol=0.05, unit="minutes"),
    Q("A question asks 'Which of these is NOT an aim of the United Nations?' What should you do?", "Find the option that does not fit the aims of the UN",
      [("Choose the first true statement", "NOT reverses the task."),
       ("Choose any option", "Guessing blindly wastes the clue in the question."),
       ("Skip the question permanently", "Never leave a gap; mark it and return.")],
      "Rewrite the question: three options are aims, one is not.", "Reading NOT questions", "Reasoning", "Underline the word NOT."),
    Q("'A shopkeeper sells expired biscuits. Which right is broken?' This question mainly tests:", "Application",
      [("Knowledge", "Knowledge recalls a plain fact; this uses a rule in a scenario."),
       ("Memory of a date", "No date is needed."),
       ("Spelling", "The paper does not test spelling.")],
      "Using consumer rights in a short scenario is application.", "Objectives of Paper 1", "Concept", "Does it use an idea in a new situation?"),
    Q("Which approach to a difficult question is best?", "Mark it, move on and return on the second pass",
      [("Spend ten minutes until you are sure", "That takes time from other questions."),
       ("Leave it blank forever", "Answer all questions; a guess is better than a blank."),
       ("Change all your other answers", "That is unhelpful.")],
      "A two-pass method protects your time.", "Time management", "Application", "Think about the whole paper."),
    Q("'Which body investigates reports of corruption but is not a court?' Which pair of clues helps most?", "'Investigates reports' and 'not a court'",
      [("'Which body'", "That clue is too general."),
       ("'Corruption'", "Several bodies are linked to corruption."),
       ("'Reports' only", "Several bodies receive reports.")],
      [("Underline", "'Investigates reports' and 'not a court'."), ("Eliminate", "ANIF, the Audit Bench and the Special Criminal Court do not match; CONAC does.")],
      "Using key clues", "Analysis", "Which words separate CONAC from the others?"),
    Q("The Board's report says weak performance came partly from limited revision of earlier work. What should a candidate do?", "Revise the whole syllabus, including the work of earlier forms",
      [("Revise only the last module", "Paper 1 covers the whole syllabus."),
       ("Learn only your favourite topics", "Questions are set on every topic."),
       ("Skip revision and rely on luck", "That is a poor strategy.")],
      "Paper 1 covers the whole syllabus.", "Revision plan", "Reasoning", "The paper covers the whole syllabus."),
    ], rot=2)))


# ---------------------------------------------------------------------------------------------
# 16. Paper 2 strategy
# ---------------------------------------------------------------------------------------------
P2 = "Paper 2"
SETS.append(practice_set(module=M_EXAM, topic=P2, title="Paper 2 technique: planning, stimulus questions and scenarios",
    lesson="citx-paper-2-essays-and-stimulus-questions", questions=build([
    Q("What does the Board's 2023 report say Paper 2 consists of?", "Essay-type questions",
      [("Fifty multiple-choice questions", "That describes Paper 1."),
       ("Only practical work", "Not in the report."),
       ("An oral test", "Not in the report.")],
      "The report describes essay-type questions, and the blueprint adds a stimulus question.", "Structure of Paper 2", "Recall", "It is a written paper."),
    Q("Which command word asks for reasons or causes?", "Explain",
      [("State", "State asks for a short answer."),
       ("List", "List asks for items, not reasons."),
       ("Name", "Name asks for a name only.")],
      "Explain means give reasons and use because.", "Command words", "Recall", "It starts with 'because'."),
    Q("Which approach does the Board warn against in Paper 2?", "Merely listing points without developing them",
      [("Planning an answer", "Planning helps."),
       ("Reading the instructions", "Candidates should respect the rubric."),
       ("Selecting questions carefully", "The Board recommends this.")],
      "The report advises against merely listing points.", "Essay technique", "Concept", "Think of developed points."),
    Q("A good paragraph in an essay contains:", "A point, an example or evidence, and an explanation",
      [("A list of names only", "That does not develop a point."),
       ("A copy of the question", "That wastes time."),
       ("A story with no link to the question", "It must answer the question.")],
      "Point, evidence and explanation make a developed paragraph.", "Paragraph structure", "Concept", "Develop each point."),
    Q("'Explain two causes of conflict.' Which answer fits best?", "Two causes, each explained with an example",
      [("A list of ten causes in one line", "Only two were asked for and a list does not explain."),
       ("One cause only", "Two were asked for."),
       ("A story about a quarrel", "The story does not answer the question.")],
      "Match the number and the command word.", "Command words", "Application", "Count the number asked."),
    Q("Stimulus text (written for practice): 'Market women told the trade office that a trader's scale gave false weights. An inspector ordered him to use a tested scale.' Which right was broken?", "The right to fair treatment and true information",
      [("The right to vote", "Not a consumer right."),
       ("The right to a passport", "Not a consumer right."),
       ("The right to form a trade union", "Not related to the text.")],
      [("Read", "False weights cheat buyers."), ("Apply", "Consumers have rights to information and fair dealing.")],
      "Using a stimulus text", "Application", "What does a false weight do to the buyer?"),
    Q("A worker is dismissed with no notice and no reason. Which advice follows the Labour Code approach?", "Keep documents and see the labour inspector first",
      [("Take revenge on the employer at once", "That is not lawful or helpful."),
       ("Do nothing, since workers have no rights", "The worker has rights."),
       ("Go to the National Assembly to ask for pay", "The Assembly does not settle individual labour disputes.")],
      "Name the rule, apply it to the case and give steps.", "Applying a rule to a scenario", "Application", "Think about the order of settlement."),
    Q("Why should you refer to the text in a stimulus question?", "The answers are expected to use the information given",
      [("The text has the marks written on it", "That is false."),
       ("The text is always wrong", "That is not true."),
       ("It makes your answer longer", "Length alone earns nothing.")],
      "Answers should use the text as well as your own knowledge.", "Stimulus questions", "Reasoning", "The text is part of the question."),
    ], rot=3)))


# ---------------------------------------------------------------------------------------------
# Paper 1 mock exam A: 50 multiple-choice questions across the six Citizenship modules in proportion to their
# topic counts: 8 + 6 + 11 + 10 + 9 + 6. Objectives: 19 knowledge, 15 comprehension, 10 application, 6 analysis
# (the Board's 2023 mix is 38%, 30%, 20%, 12%).
# ---------------------------------------------------------------------------------------------
_P1 = []


def _m(prompt, correct, wrongs, why, concept, skill, hint):
    _P1.append(Q(prompt, correct, wrongs, why, concept, skill, hint))


# --- The Citizen in Social & Community Life (8) ---
_m("A family made up of two parents and their children living together is called a:", "Nuclear family",
   [("Extended family", "An extended family also includes relatives such as grandparents, uncles and aunts."),
    ("Single-parent family", "That has only one parent with the children."),
    ("Polygamous family", "That has one spouse with several partners and their children.")],
   "A nuclear family is parents and their children.", "The family", "Recall", "Count who lives together.")
_m("Mbi lives in one compound with her parents, her grandmother and her father's brother's family. Which type of family is this?", "Extended family",
   [("Nuclear family", "A nuclear family has only parents and children."),
    ("Single-parent family", "Both of her parents live there."),
    ("Foster family", "She lives with her own relatives, not as a foster child.")],
   "Family members beyond parents and children living together form an extended family.", "The family", "Application", "Who else lives in the compound besides parents and children?")
_m("In Cameroon, a marriage celebrated before a civil status registrar is a:", "Civil marriage",
   [("Customary marriage", "That is celebrated according to local custom, not before the registrar."),
    ("Engagement", "An engagement is a promise to marry, not the marriage itself."),
    ("Bride price payment", "That is a payment between families, not the legal marriage.")],
   "A civil marriage is celebrated before a civil status officer and recorded in a certificate.", "Marriage and succession in Cameroon", "Recall", "Which marriage involves the registrar?")
_m("A will is:", "A statement of wishes about property after death",
   [("A document that records a birth in a family", "That is a birth certificate."),
    ("A promise to marry", "That is an engagement."),
    ("A receipt for a bride price", "A receipt records a payment, not the sharing of property.")],
   "A will states the wishes of a person about their property after death.", "Marriage and succession in Cameroon", "Concept", "Think of the word succession.")
_m("Which body brings parents and teachers together to support a school?", "The Parent-Teacher Association (PTA)",
   [("The school's examination board", "That organises examinations."),
    ("A sports club", "That is for a single activity."),
    ("A student prefects' team", "Prefects are students only.")],
   "The PTA unites parents and teachers.", "The school and the village", "Recall", "The first word is parent.")
_m("Traditional rulers in Cameroon are generally regarded as:", "Auxiliaries of the administration",
   [("Judges of the Supreme Court", "They are not Supreme Court judges."),
    ("Members of the Government", "They are not ministers."),
    ("Elected mayors of city councils", "Mayors are elected heads of councils; chiefs follow custom and the rules on traditional chiefdoms.")],
   "By law, traditional rulers help the administration. Check the current rules.", "The school and the village", "Concept", "Think of helpers of the administration.")
_m("Which of these is NOT a safe road practice?", "Using a phone while riding a motorcycle",
   [("Wearing a helmet", "A helmet protects the head."),
    ("Wearing a seat belt in a car", "A seat belt reduces injury."),
    ("Keeping a safe distance from the vehicle in front", "A safe distance gives time to brake.")],
   "Using a phone while riding takes attention from the road.", "Road safety", "Reasoning", "Three options are safe practices.")
_m("A bus driver is tired after driving for many hours and still has a long way to go. What is the safest decision?", "Stop and rest before continuing",
   [("Drive faster to arrive earlier", "Speed and tiredness increase the risk of accidents."),
    ("Overtake slow vehicles on bends to save time", "Overtaking on bends is dangerous."),
    ("Carry more passengers to share the costs", "Overloading is dangerous.")],
   "A tired driver is a danger; rest first.", "Road safety", "Application", "Which choice puts safety first?")

# --- Administrative Organization of Cameroon (6) ---
_m("Decentralization means:", "Passing powers to elected local authorities",
   [("Appointing officials to represent the central government in each region", "That is deconcentration."),
    ("Moving the capital to another town", "That is a change of location, not of powers."),
    ("Giving all powers to one person", "That is concentration of power.")],
   "Decentralization gives powers and means to elected local authorities.", "Deconcentration and decentralization", "Concept", "The local authorities are elected.")
_m("The Governor of a Region is appointed by the President and represents the State there. This is an example of:", "Deconcentration",
   [("Decentralization", "Decentralization gives powers to elected local authorities."),
    ("Federalism", "Federalism shares sovereignty between states."),
    ("Privatisation", "That concerns ownership of businesses.")],
   "Appointed representatives of the State: deconcentration.", "Deconcentration and decentralization", "Application", "Is the Governor elected locally or appointed?")
_m("How many Regions does Cameroon have?", "Ten",
   [("Eight", "Cameroon has ten."),
    ("Twelve", "There are ten Regions."),
    ("Seven", "That is too few.")],
   "Cameroon has ten Regions, which replaced the former provinces in 2008.", "Administrative units", "Recall", "A round number between seven and twelve.")
_m("Who heads a Division?", "The Senior Divisional Officer",
   [("The Governor", "A Governor heads a Region."),
    ("The Mayor", "A Mayor heads a council."),
    ("The Divisional Officer", "A Divisional Officer heads a sub-division.")],
   "Region: Governor; Division: Senior Divisional Officer; Sub-division: Divisional Officer.", "Administrative units", "Concept", "Region, Division, Sub-division in order.")
_m("Which of these is NOT a decentralized local authority?", "A Division",
   [("A Region", "Regions are decentralized local authorities."),
    ("A council", "Councils are decentralized local authorities."),
    ("A city council", "City councils are also local authorities.")],
   "Divisions are administrative units of the State, not decentralized authorities.", "Decentralized local authorities", "Reasoning", "Local authorities have elected organs.")
_m("A council uses a local market fee to build stalls and answers to its elected councillors. Which idea does this show?", "Decentralization",
   [("Deconcentration", "That is about appointed State representatives."),
    ("Military rule", "Not relevant."),
    ("A federal state", "Cameroon's State is unitary.")],
   "A local authority with its own elected organs and resources shows decentralization.", "Decentralized local authorities", "Reasoning", "Who is in charge of the council?")

# --- Constitutional & Political Organization (11) ---
_m("The referendum of 20 May 1972 created:", "The United Republic of Cameroon",
   [("The Federal Republic of Cameroon", "The federation was created in 1961."),
    ("The independent Republic of Cameroun", "That was in 1960."),
    ("The Senate", "The Senate was provided for by the 1996 constitution.")],
   "In 1972 the federal structure was replaced by a unitary state.", "Constitutional evolution of Cameroon", "Recall", "A year in the 1970s.")
_m("The 1996 constitutional revision provided for which institutions?", "A Senate, Regions and a Constitutional Council",
   [("A federation of two states", "That was in 1961."),
    ("A monarchy with a king", "Cameroon is a republic."),
    ("A single-party state with one chamber", "The 1996 revision concerns multiparty institutions.")],
   "The 1996 constitution provided for these bodies, which were set up later. Check the dates in your textbook.", "Constitutional evolution of Cameroon", "Concept", "Think of the second chamber.")
_m("What is Cameroon's national motto?", "Peace - Work - Fatherland",
   [("Unity and Faith, Peace and Progress", "That is the motto of another country."),
    ("Liberty - Equality - Fraternity", "That is the motto of France."),
    ("Unity - Work - Progress", "That is not Cameroon's motto.")],
   "The motto is Peace, Work, Fatherland.", "National symbols", "Recall", "Three words.")
_m("The flag of Cameroon has:", "Vertical green, red and yellow bands with a star on the red band",
   [("Three horizontal bands of green, red and yellow", "The bands are vertical."),
    ("Two horizontal bands of red and white with a star", "The colours and bands are different."),
    ("Three vertical bands of green, white and red", "The colour sequence is different, and there is a star.")],
   "Green, red and yellow, with a star on the central red band.", "National symbols", "Recall", "Vertical bands and a star.")
_m("Who is the Head of State of Cameroon?", "The President of the Republic",
   [("The Prime Minister", "He is head of government."),
    ("The Speaker of the National Assembly", "He presides over the Assembly."),
    ("The Chief Justice", "He is a judicial authority.")],
   "The President of the Republic is Head of State.", "The executive", "Recall", "The other title is head of government.")
_m("How is the Prime Minister of Cameroon chosen?", "Appointed by the President of the Republic",
   [("Elected by all voters", "The voters do not elect the Prime Minister directly."),
    ("Chosen by the Supreme Court", "The Court does not choose him."),
    ("Chosen by the United Nations", "He is chosen nationally.")],
   "The Prime Minister, head of the Government, is appointed by the President.", "The executive", "Concept", "He is head of government.")
_m("Parliament in Cameroon is made up of:", "The National Assembly and the Senate",
   [("The Supreme Court and the Constitutional Council", "Those are judicial and constitutional bodies."),
    ("The President and the Prime Minister", "They form the executive."),
    ("Regional councils and city councils", "These are local authorities.")],
   "Parliament has two chambers: the National Assembly and the Senate.", "The legislature", "Concept", "Two chambers.")
_m("Which is a function of the legislature?", "Making laws and voting the budget",
   [("Commanding the armed forces", "That belongs to the executive."),
    ("Passing sentences in criminal cases", "That belongs to the judiciary."),
    ("Counting votes at elections", "That is for the electoral body.")],
   "Parliament makes laws, votes the budget and controls the Government.", "The legislature", "Concept", "Think of lawmakers.")
_m("Which court is at the top of the ordinary court system?", "The Supreme Court",
   [("The Court of First Instance", "It is at the base of the system."),
    ("The High Court", "It is higher than the Court of First Instance but below the Supreme Court."),
    ("The Court of Appeal", "It is below the Supreme Court.")],
   "The Supreme Court is at the top of the ordinary courts.", "The judiciary", "Recall", "It is the highest.")
_m("A law is thought to go against the Constitution. Which body rules on whether it is constitutional?", "The Constitutional Council",
   [("The Audit Bench", "It audits public accounts."),
    ("A Court of First Instance", "It does not rule on the constitutionality of laws."),
    ("The Labour inspector", "That official handles employment disputes.")],
   "The Constitutional Council rules on the constitutionality of laws. Check the current rules.", "The judiciary", "Application", "Which body has the Constitution in its name?")
_m("Which body organises and supervises elections in Cameroon?", "ELECAM",
   [("CONAC", "CONAC is the anti-corruption commission."),
    ("CNPS", "That is the social security fund."),
    ("ANIF", "That is the financial investigation agency.")],
   "ELECAM is the body responsible for elections. Check the current rules on the division of tasks.", "The electoral process", "Recall", "The name begins with the word Elections.")

# --- Economic Life, Labour & Public Ethics (10) ---
_m("Which of these is NOT a source of tax revenue?", "A loan from a bank",
   [("Income tax", "A direct tax."),
    ("Value added tax", "An indirect tax."),
    ("Customs duties", "Taxes on goods crossing the border.")],
   "A loan is borrowing, not a tax.", "Government revenue and taxation", "Reasoning", "Three options are taxes.")
_m("Revenue is 3 000 and expenditure is 3 400 (invented figures). The budget shows:", "A deficit of 400",
   [("A surplus of 400", "A surplus needs revenue to exceed expenditure."),
    ("A deficit of 3 400", "3 400 is the expenditure."),
    ("A balanced budget", "A balance needs equal figures.")],
   "3 400 - 3 000 = 400, with expenditure larger: a deficit.", "Government revenue and taxation", "Application", "Compare the two figures.")
_m("The CNPS manages:", "The main social security schemes for employees",
   [("The organisation of elections", "That is ELECAM."),
    ("The audit of public accounts", "That is the Audit Bench."),
    ("The collection of customs duties", "That is the customs administration.")],
   "The CNPS manages the main social security schemes.", "Social security", "Recall", "Social insurance.")
_m("Which benefit is paid to a worker who retires after contributing for enough years?", "An old-age pension",
   [("A work accident benefit", "That is for injury or illness caused by the job."),
    ("A consumer refund", "That concerns faulty goods."),
    ("A fine", "A fine is a penalty.")],
   "An old-age pension is one of the main benefits.", "Social security", "Concept", "He has stopped working.")
_m("Which is a duty of an employee under the Labour Code?", "Following lawful instructions and working with care",
   [("Paying wages on time", "That is an employer's duty."),
    ("Providing safe working conditions", "That is an employer's duty."),
    ("Registering workers with the CNPS", "That is an employer's duty.")],
   "Employees must do the agreed work with care and follow lawful instructions.", "The Labour Code", "Concept", "Which duty belongs to the worker?")
_m("Nkeng is dismissed suddenly without notice. Whom should she consult first?", "The labour inspector",
   [("The Supreme Court", "That is not the first stage."),
    ("The National Assembly", "It does not settle individual labour disputes."),
    ("The Special Criminal Court", "It tries embezzlement cases.")],
   "Conciliation by the labour inspector comes before the labour court.", "The Labour Code", "Application", "An official of the Ministry of Labour.")
_m("The right to be told the true price, contents and date of expiry of a product is the right to:", "Information",
   [("Redress", "Redress is a remedy after a problem."),
    ("Choice", "Choice is the chance to choose between goods."),
    ("Vote", "That is a political right.")],
   "The consumer's right to information.", "Consumer protection", "Recall", "True facts on labels.")
_m("Rice sold as 5 kg weighs only 4.5 kg. What percentage of the weight is missing?", "10%",
   [("5%", "0.5 kg is a tenth of 5 kg, not a twentieth."),
    ("0.5%", "That confuses 0.5 kg with a percentage."),
    ("11%", "That divides by 4.5 kg instead of 5 kg.")],
   "0.5 / 5 x 100 = 10%.", "Consumer protection", "Application", "Divide the missing weight by the stated weight.")
_m("Which body receives and studies reports of suspicious financial transactions?", "ANIF",
   [("CONAC", "CONAC receives reports of corruption and investigates; it is a commission."),
    ("The Audit Bench", "It audits public accounts."),
    ("The Special Criminal Court", "It tries cases of embezzlement.")],
   "ANIF is the financial investigation agency.", "Public service ethics and anti-corruption", "Recall", "The F stands for financial.")
_m("Which best describes nepotism?", "Giving a job to a relative regardless of merit",
   [("Stealing public funds one manages", "That is embezzlement."),
    ("Demanding money for a free service", "That is extortion."),
    ("Refusing a bribe", "That is honest behaviour.")],
   "Nepotism is favouring relatives.", "Public service ethics and anti-corruption", "Concept", "Think of relatives.")

# --- Human Rights, Peace & Environmental Stewardship (9) ---
_m("The UDHR was adopted by the UN General Assembly on:", "10 December 1948",
   [("24 October 1945", "That is when the UN Charter came into force."),
    ("9 July 2002", "That is the launch of the African Union."),
    ("1 January 1960", "That is Cameroun's independence day.")],
   "The UDHR was adopted on 10 December 1948.", "Human rights", "Recall", "Human Rights Day.")
_m("Which is an example of a civil and political right?", "The right to vote",
   [("The right to health", "An economic, social and cultural right."),
    ("The right to education", "An economic, social and cultural right."),
    ("The right to fair pay", "An economic, social and cultural right.")],
   "Voting is taking part in government.", "Human rights", "Concept", "Participation in government.")
_m("Which convention protects the rights of the child?", "The Convention on the Rights of the Child",
   [("CEDAW, adopted in 1979", "That concerns women."),
    ("The Geneva Conventions", "They concern victims of war."),
    ("The Vienna Convention of 1961", "It concerns diplomatic relations.")],
   "The CRC was adopted by the UN in 1989.", "Protection of women, children and minorities", "Recall", "The convention named after children.")
_m("A 12-year-old sells goods at a roadside all day every day and does not go to school. Which right is most directly affected?", "Education and protection from harmful work",
   [("The right to vote in elections", "A child cannot vote."),
    ("The right to a travel passport", "That is not the issue."),
    ("The right to hold a trade licence", "That concerns traders.")],
   "Children have the right to education and protection from exploitative work.", "Protection of women, children and minorities", "Application", "What is the child missing?")
_m("Which principle of IHL requires parties to tell civilians from fighters?", "Distinction",
   [("Proportionality", "That concerns excessive harm compared with the military advantage."),
    ("Humanity", "That concerns humane treatment."),
    ("Neutrality", "That concerns not taking sides.")],
   "Distinction: attack only military targets.", "International humanitarian law", "Concept", "Think of telling apart.")
_m("Which method uses a neutral person who helps the parties but cannot impose a decision?", "Mediation",
   [("Arbitration", "The arbitrator gives a decision."),
    ("Adjudication", "A judge decides."),
    ("Negotiation", "The parties talk directly.")],
   "A mediator helps parties to reach their own agreement.", "Conflict resolution and peace", "Concept", "Neutral helper.")
_m("Two families argue over a boundary and a court gives a binding judgement. Which method is this?", "Adjudication",
   [("Negotiation", "That is direct talks."),
    ("Mediation", "A mediator cannot impose a decision."),
    ("Compromise", "That is an outcome, not a method.")],
   "A judge deciding by law is adjudication.", "Conflict resolution and peace", "Application", "Who decides?")
_m("The spread of desert-like conditions in dry areas is called:", "Desertification",
   [("Deforestation", "That is the clearing of forests."),
    ("Urbanisation", "That is the growth of towns."),
    ("Irrigation", "That is supplying land with water.")],
   "Desertification affects dry areas such as the Sahel.", "The environment and climate change", "Recall", "The word contains desert.")
_m("Which action best reduces flooding in a town and the spread of disease?", "Keeping drains free of waste",
   [("Burning waste in the open", "That pollutes the air."),
    ("Building houses over drainage channels", "That blocks water."),
    ("Cutting trees on river banks", "That worsens erosion.")],
   "Clear drains carry rainwater away and reduce stagnant water.", "The environment and climate change", "Reasoning", "Where does rainwater go?")

# --- Cameroon & International Organizations (6) ---
_m("What is the head of an embassy called?", "An ambassador",
   [("A consul", "A consul heads a consulate."),
    ("A mayor", "A mayor heads a council."),
    ("A governor", "A governor heads a Region.")],
   "An ambassador heads an embassy.", "Diplomacy", "Recall", "He represents the head of state.")
_m("A treaty between Cameroon and one other country on student exchanges is an example of:", "Bilateral diplomacy",
   [("Multilateral diplomacy", "That involves three or more states."),
    ("Domestic policy", "It involves another country."),
    ("A civil case", "It is not a court case.")],
   "Two states: bilateral.", "Diplomacy", "Application", "Count the states.")
_m("Which organisation replaced the OAU in 2002?", "The African Union",
   [("CEMAC", "A Central African community."),
    ("ECCAS", "A Central African community."),
    ("The Commonwealth", "A worldwide association.")],
   "The AU, launched in Durban on 9 July 2002.", "Regional organizations", "Recall", "It is continent-wide.")
_m("Which statement compares CEMAC and ECCAS correctly?", "ECCAS has more members and includes all CEMAC states",
   [("CEMAC has more members than ECCAS", "ECCAS is the wider group."),
    ("ECCAS has its headquarters in Bangui", "ECCAS is based in Libreville."),
    ("CEMAC was founded in 1983", "ECCAS was founded in 1983; CEMAC in 1994.")],
   "ECCAS (1983, Libreville) is wider than CEMAC (1994, Bangui). Check the current membership.", "Regional organizations", "Reasoning", "Compare size, date and headquarters.")
_m("Which UN organ has five permanent members with the power of veto?", "The Security Council",
   [("The General Assembly", "All its members have one vote each."),
    ("The International Court of Justice", "It is a court of judges."),
    ("The Secretariat", "It is the administrative staff.")],
   "The Security Council has five permanent members and ten elected members.", "The United Nations, the Commonwealth and La Francophonie", "Recall", "It has the veto.")
_m("Cameroon belongs to both the Commonwealth and La Francophonie mainly because:", "It has English and French as official languages",
   [("Both are military alliances that it must join", "Neither is a military alliance."),
    ("They are branches of the African Union", "They are separate associations."),
    ("It has no other international links", "It also belongs to the UN, AU, CEMAC and ECCAS.")],
   "Membership reflects its bilingual heritage.", "The United Nations, the Commonwealth and La Francophonie", "Concept", "Think about languages.")

assert len(_P1) == 50
_POS = [0] * 13 + [1] * 13 + [2] * 12 + [3] * 12
random.Random(7).shuffle(_POS)
P1_QUESTIONS = build(_P1, pos=_POS)
SETS.append(practice_set(module=M_EXAM, topic=P1, title="Paper 1 mock exam A",
    lesson="citx-paper-1-multiple-choice-strategy", mock=True, time_limit_minutes=90, questions=P1_QUESTIONS))


# ---------------------------------------------------------------------------------------------
# Paper 2 practice paper A: about 25 auto-markable parts on essay planning, stimulus reading, applying rules to
# short scenarios and exam technique. Essays cannot be marked by the computer; this paper tests the method.
# ---------------------------------------------------------------------------------------------
_P2 = []


def _p(prompt, correct, wrongs, why, concept, skill, hint):
    _P2.append(Q(prompt, correct, wrongs, why, concept, skill, hint))


_STIM_A = ("Stimulus A (written for practice): 'After the rains, the main street of a small town floods every year. "
           "The drains are blocked with plastic bottles and bags. Traders have also built stalls over part of the drainage channel. "
           "The council has asked the community to clean the drains and to move the stalls.'")
_STIM_B = ("Stimulus B (written for practice): 'A clerk at a sub-divisional office tells a young woman that her document will be ready "
           "only if she adds some money to the official fee. She refuses and reports the matter to the proper authority.'")

# --- Question 1: planning an essay (5 parts) ---
_p("Question 1 (a). An essay question begins: 'Explain how decentralization can help the development of a community.' What does the command word 'explain' ask you to do?",
   "Give reasons and show how each point leads to the result",
   [("List the names of the local authorities only", "A list does not explain how decentralization helps."),
    ("Write the history of the Constitution", "That does not answer the question."),
    ("Give a very short definition and stop", "Explain needs reasons, not just a definition.")],
   "Explain means give reasons and link them to results.", "Paper 2", "Recall", "Look at the word 'how'.")
_p("Question 1 (b). Which is the best first step before you write the essay in (a)?", "Underline the command word and key words, and make a short plan",
   [("Write the conclusion first without a plan", "A conclusion without a plan may not follow from the points."),
    ("Copy a paragraph from your notes", "The answer must fit this question."),
    ("Write as much as possible without stopping", "Length without a plan wastes time.")],
   "Reading and planning keep the answer on the question.", "Paper 2", "Application", "What should you do before you write?")
_p("Question 1 (c). Which plan for (a) is best?", "An introduction, developed paragraphs with examples, and a conclusion",
   [("A list of one-word points with no explanation at all", "The Board warns against merely listing points."),
    ("Three paragraphs about the Executive and nothing else", "They do not answer the question."),
    ("A conclusion followed by an unrelated story", "An essay needs an introduction and developed points.")],
   "Introduction, developed paragraphs with examples, and a conclusion.", "Paper 2", "Application", "Which plan has paragraphs with examples?")
_p("Question 1 (d). A candidate writes 'Councils: roads, markets, rubbish.' for a 'discuss' question. What is the main weakness?", "The points are only listed and not developed",
   [("The answer is too long", "It is too short, not too long."),
    ("It uses Cameroonian examples", "Examples are welcome when explained."),
    ("It has no mistakes in spelling", "Spelling is not the issue.")],
   "A list does not explain how each point matters.", "Paper 2", "Analysis", "Does it explain anything?")
_p("Question 1 (e). What should the conclusion of an essay do?", "Sum up the main points and answer the question directly",
   [("Bring in new, unrelated facts", "A conclusion should not start a new topic."),
    ("Repeat the whole essay word for word", "Repeating wastes time."),
    ("Apologise for the length", "That adds nothing.")],
   "A conclusion sums up and answers the question.", "Paper 2", "Recall", "Think of what the examiner reads last.")

# --- Question 2: stimulus A (5 parts) ---
_p(_STIM_A + " (a) Which problem is described?", "Flooding caused by blocked drains",
   [("A shortage of classrooms in the town", "The text is about drains."),
    ("A dispute between two neighbouring countries", "No countries are mentioned."),
    ("A lack of tax revenue for the council", "Taxes are not mentioned.")],
   "The text says the drains are blocked and the channel is built over.", "The environment and climate change", "Interpretation", "Read the first sentence.")
_p(_STIM_A + " (b) Which cause of the flooding is shown in the text?", "Blocked drains and stalls built over the channel",
   [("Too little rain", "The text says floods follow the rains."),
    ("Too many schools", "Not in the text."),
    ("Climate change alone", "The text points to local causes.")],
   "The text gives the causes: plastic waste in drains and stalls over the channel.", "The environment and climate change", "Interpretation", "Use the details in the text.")
_p(_STIM_A + " (c) Which action by the community would best reduce the problem?", "Stop dumping plastic in drains and keep the channel clear",
   [("Burn the waste beside the drains", "That pollutes the air and does not clear the drains."),
    ("Build more stalls over the channel", "That makes the blockage worse."),
    ("Wait for the rains to stop", "That does not solve the cause.")],
   "Cleaning the drains and keeping the channel clear tackles the cause.", "The environment and climate change", "Application", "Tackle the causes named in the text.")
_p(_STIM_A + " (d) The council has asked the community to act. Which idea of administration does this show?", "Decentralization, with an elected local authority",
   [("Deconcentration of the national army", "Not relevant."),
    ("Diplomacy between two foreign states", "No foreign states are involved."),
    ("A referendum on the Constitution", "Not relevant.")],
   "A council is a decentralized local authority.", "Decentralized local authorities", "Application", "Who is acting on the text: the council.")
_p(_STIM_A + " (e) Which statement uses the text correctly in an answer?", "The text shows that both citizens and the council have a part to play",
   [("The text proves that councils have no powers", "The text shows the council acting."),
    ("The text is not needed to answer", "In a stimulus question the answer must use the text."),
    ("The text shows that rainfall never causes floods", "The text does not say that.")],
   "Link your answer to the details in the text.", "Paper 2", "Reasoning", "Does the statement fit the text?")

# --- Question 3: stimulus B (5 parts) ---
_p(_STIM_B + " (a) Which form of corruption does the clerk's request show?", "Extortion, a form of bribery",
   [("Nepotism", "That is favouring relatives."),
    ("Embezzlement", "That is stealing funds that one manages."),
    ("Tax evasion", "That is hiding income from the tax authority.")],
   "Demanding extra money for a service is extortion.", "Public service ethics and anti-corruption", "Application", "He demands money.")
_p(_STIM_B + " (b) Which value should the clerk have shown?", "Integrity",
   [("Favouritism", "That is the opposite of a good value."),
    ("Secrecy", "That is not the value described."),
    ("Delay", "That is poor service.")],
   "Integrity means honesty and refusing bribes.", "Public service ethics and anti-corruption", "Concept", "Think of honesty.")
_p(_STIM_B + " (c) The young woman reports the case. Which commission receives reports of corruption and investigates them?", "CONAC",
   [("ANIF", "ANIF studies suspicious financial transactions."),
    ("The Audit Bench", "It audits public accounts."),
    ("ELECAM", "It organises elections.")],
   "CONAC receives and investigates reports of corruption.", "Public service ethics and anti-corruption", "Recall", "The N stands for National.")
_p(_STIM_B + " (d) Which effect of corruption is shown in the text?", "Citizens must pay more than the official fee for a service",
   [("The State receives more revenue", "The extra money goes to the clerk, not to the State."),
    ("The service is cheaper", "The service becomes dearer."),
    ("Public trust in the administration rises", "Trust falls when officials ask for bribes.")],
   "Corruption makes services costlier and unfair.", "Public service ethics and anti-corruption", "Interpretation", "Who gains and who loses?")
_p(_STIM_B + " (e) What should a model answer say about what the young woman did?", "She acted as a good citizen by refusing the bribe and reporting it",
   [("She should have paid, to avoid trouble", "Paying a bribe supports corruption."),
    ("She should have insulted the clerk", "Insults do not help; report to the proper authority."),
    ("She should have said nothing", "Silence lets corruption continue.")],
   "Refusing and reporting is the right civic response.", "Public service ethics and anti-corruption", "Reasoning", "Think about civic duty.")

# --- Question 4: applying rules to scenarios (5 parts) ---
_P2.append(N("Question 4 (a). A shop sells a mobile phone for 40 000 FCFA before VAT. VAT is charged at 19.25% (a teaching rate; check the current rate). What is the total price in FCFA?", 47700,
             [("VAT", "40 000 x 19.25 / 100 = 7 700."), ("Total", "40 000 + 7 700 = 47 700.")],
             "Government revenue and taxation", "Calculation", "Find the VAT first, then add it to the price.", unit="FCFA"))
_P2.append(N("Question 4 (b). A worker earns 200 000 FCFA a month. In an invented example the employee pays 4% and the employer 8% into the fund. How much in total goes in each month?", 24000,
             [("Employee", "200 000 x 4 / 100 = 8 000."), ("Employer", "200 000 x 8 / 100 = 16 000."), ("Total", "8 000 + 16 000 = 24 000.")],
             "Social security", "Calculation", "Work out each share, then add.", unit="FCFA"))
_p("Question 4 (c). A Cameroonian student loses her passport in a foreign city where Cameroon has a consulate. What should she do?", "Go to the consulate for help with documents",
   [("Wait for the UN Secretary-General", "He does not issue national passports."),
    ("Ask the local police to issue a Cameroonian passport", "Only her own state can issue it."),
    ("Do nothing and return without papers", "That makes matters worse.")],
   "Consulates help citizens abroad with documents.", "Diplomacy", "Application", "Which office serves citizens abroad?")
_p("Question 4 (d). Two traders agree to let a neutral person hear them and give a decision they promise to accept. Which method are they using?", "Arbitration",
   [("Mediation", "A mediator helps but does not decide."),
    ("Negotiation", "That is direct talk."),
    ("Adjudication", "That is a decision by a judge.")],
   "Arbitration produces a decision the parties agreed to accept.", "Conflict resolution and peace", "Application", "Who decides?")
_p("Question 4 (e). A fighter who has been captured is beaten to make him talk. Which rule of international humanitarian law is broken?", "The ban on torture and cruel treatment",
   [("The rule of diplomatic immunity", "That concerns diplomats."),
    ("The rule on tax declaration", "Not relevant."),
    ("The rule of free movement in CEMAC", "Not relevant.")],
   "Prisoners must be treated humanely.", "International humanitarian law", "Application", "Humane treatment of prisoners.")

# --- Question 5: exam technique (5 parts) ---
_P2.append(N("Question 5 (a). In a KKEVO practice setting you have 150 minutes for 5 answers of equal weight. How many minutes can you give to each?", 30,
             [("Divide", "150 / 5 = 30 minutes.")], "Paper 2", "Calculation", "Divide the time by the number of answers.", unit="minutes"))
_p("Question 5 (b). What does the Board's 2023 report advise about choosing questions in Paper 2?", "Select questions carefully, according to what you know",
   [("Choose the most popular questions", "Popular does not mean easy."),
    ("Answer in the order of the paper whatever you know", "The report advises careful selection."),
    ("Never read the questions", "Read them first.")],
   "The report advises candidates to select questions carefully.", "Paper 2", "Recall", "Think of 'selection'.")
_p("Question 5 (c). Which sentence is the best opening of a paragraph?", "Decentralization helps because local people know local needs.",
   [("Councils, roads, markets and rubbish.", "A single word does not make a point."),
    ("In conclusion, I think that it is good.", "That belongs at the end."),
    ("Many things happen in many places.", "It is vague.")],
   "A good paragraph begins with a clear point and a reason.", "Paper 2", "Application", "Point, then reason.")
_p("Question 5 (d). Which of these is a good use of Cameroonian examples in an essay?", "Using a real example to illustrate and explain a point",
   [("Using a long story that does not answer the question", "An example must serve the point."),
    ("Criticising a political party", "Essays should avoid party politics."),
    ("Insulting a region", "Respect for all groups is expected.")],
   "Examples should support the point and be respectful.", "Paper 2", "Reasoning", "Examples must help the answer.")
_p("Question 5 (e). With ten minutes left, what is the best thing to do?", "Finish your answer and read through to correct errors",
   [("Start a new long essay on another question", "There is not enough time."),
    ("Leave the paper at once to rest", "Use the time to improve your answers."),
    ("Rewrite every answer from the beginning", "There is not time.")],
   "Complete and check what you have written.", "Paper 2", "Application", "Time is short.")

assert len(_P2) == 25
_POS2 = [0] * 6 + [1] * 6 + [2] * 5 + [3] * 5
random.Random(11).shuffle(_POS2)
P2_QUESTIONS = build(_P2, pos=_POS2)
SETS.append(practice_set(module=M_EXAM, topic=P2, title="Paper 2 practice paper A",
    lesson="citx-paper-2-essays-and-stimulus-questions", mock=True, time_limit_minutes=150, questions=P2_QUESTIONS))


