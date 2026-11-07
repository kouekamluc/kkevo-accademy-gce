"""Practice sets for A Level English Language (0730), Upper Sixth: Paper 3 skills (one set per lesson, 8 questions each) and the Paper 3 skills check A.

All texts, letters, articles, reports, speeches, debates, minutes and stories are original and invented; names, places and figures are invented.
Word counts in the lessons are computed by the file itself (wc), so they always match the text shown.
Where textbooks or examiners differ (for example on how words are counted), the lesson says 'check your textbook' or 'ask your teacher'.
"""

from .dsl import *  # noqa: F403

COURSE = ("english-language", "upper-sixth")

M_SUM = "Summary Writing"
M_REC = "Text Reconstruction"
M_EDIT = "Editing"
M_EXAM = "Examination"
T_SELECT = "Selecting and paraphrasing information"
T_TYPES = "Summarising different text types"
T_LIMITS = "Word and paragraph limits"
T_SEQ = "Sequencing and cohesion"
T_RTYPES = "Reconstructing different text types"
T_CORRECT = "Correcting errors in a text"
T_CONDENSE = "Condensing and reorganising a text"
T_STRUCT = "Text structures and language features"
T_P3 = "Paper 3"

SETS = []


# ------------------------------------------------------------------ shared texts (all invented for practice)
def wc(s):
    """Word count used in these lessons: every group of characters between spaces is one word (a hyphenated word is one word, a figure such as 1,200,000 is one word)."""
    return len(s.split())


def scramble(sentences, perm):
    """Return (jumbled text with letters, answer letters). perm[i] = index in `sentences` of the sentence shown in position i."""
    letters = "ABCDEFGHIJKLMNOP"
    shown = "\n".join(f"{letters[i]}. {sentences[k]}" for i, k in enumerate(perm))
    ans = "".join(letters[perm.index(k)] for k in range(len(sentences)))
    return shown, ans


# ---- Summary: the Mbeng water article (invented)
P_WATER = (
    "For twenty years the women of Mbeng, a village of about 900 people in the Western Highlands, walked three kilometres to a muddy stream "
    "each morning. Children often missed school because they were carrying water, and diarrhoea was common, especially in the rainy season.\n\n"
    "In March last year the village development committee decided to act. It collected 1,200,000 FCFA from families, and a farmers' union in "
    "the nearby town agreed to add 3,000,000 FCFA. The money paid for pipes, a concrete tank and two public taps. Young men from the village "
    "dug the trench for the pipes without pay, which saved about 800,000 FCFA in labour costs.\n\n"
    "The water now flows from a protected spring on the hill. A caretaker, chosen by the committee, keeps the taps clean and collects a small "
    "monthly fee of 500 FCFA from each household for repairs. School attendance has improved and the clinic reports fewer cases of stomach "
    "illness. For example, the nurse recorded only four cases last month, compared with about twenty a month before the project. Other villages "
    "have already sent visitors to learn how Mbeng did it."
)
M_WATER = (
    "Because Mbeng's villagers had to fetch dirty water from a distant stream, children missed lessons and illness was frequent. The village "
    "committee therefore raised 1,200,000 FCFA from families, and a farmers' union gave 3,000,000 FCFA more. Unpaid local labour helped to lay "
    "pipes from a protected spring to a tank and two taps. A caretaker looks after them, funded by a small household fee. Consequently, pupils "
    "attend school more regularly, fewer people fall ill, and neighbouring villages want to copy the scheme."
)

# ---- Summary: the Foumban buses (invented), used in practice questions
P_BUS = (
    "Every morning, hundreds of pupils in Foumban wait by the roadside for a lift. Many arrive late because the taxis are already full. In "
    "January the council bought two buses and hired drivers. Pupils pay 100 FCFA a ride, less than half of a taxi fare. Within a term, late "
    "arrivals fell sharply, and parents say their children are safer. However, the council admits that two buses are too few, and it hopes to "
    "buy three more next year."
)
M_BUS = (
    "Pupils in Foumban were often late because taxis were full, so the council bought two cheap buses. Lateness has fallen and parents feel "
    "their children are safer, but more buses are needed."
)

# ---- Summary: text types (one short extract of each)
X_SPEECH = (
    "Fellow citizens, I stand before you today because our market has become a danger to us all. Every Saturday the drains overflow, and "
    "children play beside the dirty water. Some traders say that the council should clean the drains; others say that traders should do it "
    "themselves. I say that both are right. If the council provides the bins and the traders pay a small weekly fee for collection, our market "
    "can be clean within a month. Let us work together, and let us start this Saturday."
)
M_SPEECH = (
    "The speaker argues that the overflowing drains endanger children and proposes that the council supply bins while traders pay a small "
    "collection fee, so that the market is clean within a month."
)
X_MINUTES = (
    "Minutes of the meeting of the Ndop Youth Football Club held on 14 June at 4 p.m. in the club house. Present: Mr Fon (Chairman), Miss "
    "Ayuk (Secretary), Mr Neba (Treasurer) and nine members.\n"
    "1. The Secretary read the minutes of the last meeting, and they were accepted.\n"
    "2. The Treasurer reported that the club held 85,000 FCFA. It was agreed to spend 60,000 FCFA on new balls and nets.\n"
    "3. The Chairman proposed a friendly match against Bali on 5 July. This was approved. Miss Ayuk will write to Bali.\n"
    "4. The meeting ended at 5.15 p.m."
)
M_MINUTES = (
    "The club agreed to spend 60,000 FCFA of its 85,000 FCFA on balls and nets and approved a friendly match against Bali on 5 July; the "
    "Secretary will write to Bali."
)
X_DEBATE = (
    "Proposer: Mr Speaker, school uniforms should stay. They make all students look equal, they save parents the cost of many outfits, and "
    "they help teachers to spot strangers on the compound.\n"
    "Opposer: Mr Speaker, uniforms are costly because schools sell them at high prices, and they take away the freedom of students to express "
    "themselves. Students learn as well in ordinary clothes as in uniform."
)
M_DEBATE = (
    "The proposer defends uniforms as a sign of equality, a saving for parents and a protection against strangers, whereas the opposer replies "
    "that they are expensive, limit self-expression and do not improve learning."
)
X_LETTER = (
    "Dear Sir, I bought a mobile phone from your shop on 3 May for 45,000 FCFA. After five days the screen stopped working. When I returned "
    "the phone, your assistant refused to replace it, saying that I had dropped it. This is untrue, because the phone was never dropped. I "
    "therefore request a replacement or a full refund within seven days. I attach a copy of the receipt. Yours faithfully,"
)
M_LETTER = (
    "A customer whose 45,000 FCFA phone failed after five days denies dropping it and asks the shop for a replacement or a refund within a week."
)
X_STORY = (
    "Tabe had walked for two hours when he reached the river. It was swollen by the night's rain, and the log that served as a bridge had been "
    "washed away. He sat down and thought. Then he remembered the old fishermen's canoe tied below the bend. With some effort he pulled it "
    "into the water and paddled across, trembling. On the far bank his uncle was waiting with a lamp, smiling."
)
M_STORY = (
    "After a two-hour walk Tabe found the river swollen and its log bridge washed away, so he crossed in a fishermen's canoe and was welcomed "
    "by his uncle."
)

# ---- Summary: word limits lesson. A draft that is too long, and the trimmed version
D_LONG = (
    "The village of Mbeng, which has about 900 people, had no clean water for twenty years, and the women walked three kilometres every "
    "morning to a muddy stream. Because of this, many children missed school, and diarrhoea was very common in the rainy season. The village "
    "development committee collected 1,200,000 FCFA from the families, and a farmers' union in the nearby town added 3,000,000 FCFA. With this "
    "money, they bought pipes, built a concrete tank and put up two public taps, and young men dug the trench for free. Now the water comes "
    "from a protected spring, and a caretaker keeps the taps clean."
)
D_TRIM = (
    "Mbeng's women walked three kilometres to a muddy stream for twenty years, so children missed school and illness spread. The committee "
    "raised 1,200,000 FCFA and a farmers' union added 3,000,000 FCFA. Pipes, a tank and two taps now bring spring water to the village, "
    "and a caretaker keeps them clean."
)


# ---- Reconstruction: jumbled news report about a bridge (correct order given; shown order by perm)
BR = [
    "A new footbridge over the River Menchum was opened on Monday in Wum.",
    "The bridge, which is 40 metres long, replaces a wooden one that collapsed two years ago.",
    "Since then, villagers have crossed by canoe, which was slow and sometimes unsafe.",
    "The new structure was paid for by the council with help from a charity.",
    "At the opening ceremony, the Senior Divisional Officer thanked the workers and cut the ribbon.",
    "Afterwards, the crowd celebrated with music and food.",
    "Market women said that they would now reach Wum in half the time.",
    "The council says that it will inspect the bridge every year to keep it safe.",
]
BR_PERM = [4, 0, 6, 2, 7, 1, 3, 5]
BR_SHOWN, BR_ANS = scramble(BR, BR_PERM)

# ---- Reconstruction: gap-filling (cohesion)
GAP_TEXT = (
    "The market was crowded on Saturday. (1) ______ traders had arrived early to set up their stalls, (2) ______ the buyers came later. "
    "(3) ______ the rain began, everybody ran for shelter, and (4) ______ of the stalls were destroyed. (5) ______, the traders agreed to "
    "ask the council for a roof."
)
GAP_ANS = ["Most", "while", "When", "some", "Consequently"]

# ---- Reconstruction: formal letter body, five paragraphs
LT = [
    "I am writing to ask permission to hold a clean-up campaign in the school compound on Saturday 22 November.",
    "At present, plastic bags and bottles lie in the drains behind the classrooms. After rain, the water cannot flow and the area smells badly.",
    "Firstly, forty members of the Environment Club will collect the waste between 8 a.m. and noon. Secondly, the Parents' Association has promised to lend ten wheelbarrows. Finally, the local council will remove the waste afterwards.",
    "We should be grateful if the school could provide gloves and drinking water for the volunteers.",
    "I hope that you will approve this request, and I thank you in advance for your support.",
]
LT_PERM = [3, 0, 4, 2, 1]
LT_SHOWN, LT_ANS = scramble(LT, LT_PERM)

# ---- Reconstruction: newspaper article
AR = [
    "Forty students of Mbeng Secondary School cleaned the school compound on Saturday and removed more than sixty sacks of waste.",
    "The campaign, organised by the Environment Club, began at 8 a.m.",
    "Club president Miss Lum Fonyuy said that the drains behind the classrooms had been blocked for months.",
    "Her team cleared them first and then collected plastic bottles from the playground.",
    "By noon the compound was clean, and a council lorry took away the sacks.",
    "The principal, Mr Tanyi Ekema, thanked the volunteers and promised new bins.",
    "The club plans to repeat the exercise every term.",
]
AR_PERM = [5, 2, 0, 6, 3, 1, 4]
AR_SHOWN, AR_ANS = scramble(AR, AR_PERM)

# ---- Reconstruction: report in five parts
RP = [
    "This report examines how often students of Mbeng Secondary School use the library.",
    "A survey of 100 students was carried out in October. Only 18 students said that they visit the library every week, while 52 said that they never go.",
    "Students gave three main reasons: the opening hours clash with lessons, there are too few seats, and many books are old.",
    "It is clear that the library is under-used because it is hard to reach, not because students dislike reading.",
    "It is recommended that the library should open after school and that the old reference books should be replaced.",
]
RP_PERM = [3, 1, 4, 0, 2]
RP_SHOWN, RP_ANS = scramble(RP, RP_PERM)

# ---- Reconstruction: notes into continuous text
NOTES = (
    "Notes: palace of the Fon repaired 2022; cost 7,000,000 FCFA; villagers paid 2,000,000; government paid 5,000,000; 14 workers; finished in "
    "8 months; opened by the Divisional Officer."
)
NOTES_TEXT = (
    "The palace of the Fon was repaired in 2022 at a cost of 7,000,000 FCFA. The villagers paid 2,000,000 FCFA and the government paid the "
    "remaining 5,000,000 FCFA. Fourteen workers finished the job in eight months, and the Divisional Officer opened the building."
)

# ---- Reconstruction: dialogue into reported speech
DIALOGUE = (
    'Bih: "I want to start a poultry farm."\n'
    'Tanyi: "Do you have enough money?"\n'
    'Bih: "I have 200,000 FCFA, but I need 100,000 more."\n'
    'Tanyi: "I lend money to friends at no interest. I can give you the rest next month."\n'
    'Bih: "Thank you. I promise to repay you after the first sale."'
)
REPORT_PAST = (
    "Bih said that she wanted to start a poultry farm. Tanyi asked whether she had enough money. Bih replied that she had 200,000 FCFA but "
    "needed 100,000 more. Tanyi said that he lent money to friends at no interest and could give her the rest the following month. Bih "
    "thanked him and promised to repay him after the first sale."
)
REPORT_PRES = (
    "Bih says that she wants to start a poultry farm. Tanyi asks whether she has enough money. Bih replies that she has 200,000 FCFA but "
    "needs 100,000 more. Tanyi says that he lends money to friends at no interest and can give her the rest next month. Bih thanks him and "
    "promises to repay him after the first sale."
)

# ---- Reconstruction: notes into minutes
MIN_NOTES = (
    "Notes: Parents' Association, 8 March, 3 p.m., school hall. Present: Mrs Njong (chair) and 42 parents. Fees: chair proposed +2,000 FCFA "
    "a term; parents refused; agreed +1,000 FCFA. Roof of Block B: cost 1,500,000 FCFA; fundraising match 22 March. Ended 4.30 p.m."
)
MIN_TEXT = (
    "Minutes of the meeting of the Parents' Association held on 8 March at 3 p.m. in the school hall.\n"
    "Present: Mrs Njong (Chairperson) and 42 parents.\n"
    "1. Fees. The Chairperson proposed an increase of 2,000 FCFA a term. The parents rejected this, and it was agreed to raise the fees by "
    "1,000 FCFA.\n"
    "2. Roof. It was reported that the roof of Block B would cost 1,500,000 FCFA. It was agreed to hold a fundraising match on 22 March.\n"
    "3. The meeting ended at 4.30 p.m."
)

# ---- Reconstruction: a story
ST = [
    "It was market day in Bafut, and Nkeng had been selling plantains since dawn.",
    "By midday she had sold almost everything, and she began to count her money.",
    "Suddenly she noticed that her purse, which had held 8,000 FCFA, was missing.",
    "She searched under the table, in her basket and along the path, but found nothing.",
    "Then a small boy ran up and held out the purse, saying that it had fallen near the gate.",
    "Nkeng thanked him warmly and gave him two ripe plantains.",
    "That evening she told her family that honesty is still alive in the market.",
]
ST_PERM = [4, 0, 6, 2, 5, 1, 3]
ST_SHOWN, ST_ANS = scramble(ST, ST_PERM)

# ---- Reconstruction: a speech
SP = [
    "Good morning, ladies and gentlemen, and thank you for coming.",
    "Today I wish to speak to you about the danger of speeding on our road.",
    "Last year, three people died within two kilometres of this school.",
    "I therefore urge every driver to slow down near the gate and every parent to hold a child's hand.",
    "Thank you for listening; let us make our road safe.",
]
SP_PERM = [3, 1, 4, 0, 2]
SP_SHOWN, SP_ANS = scramble(SP, SP_PERM)


# ---- Editing: text with grammar errors (8 errors) and its corrected version
E1_ERR = (
    "Last Saturday, our class go on a visit to the water factory in Bafoussam. We left school at seven o'clock and arrive at nine. The manager "
    "welcomed us and explain how the water was cleaned. He gave us many informations about the machines. Each of the students were given a "
    "bottle of water. After the visit, we thanked him for his kindness and returned at home tired but happy. The teacher said that it was a "
    "visit we will never forget it."
)
E1_FIX = (
    "Last Saturday, our class went on a visit to the water factory in Bafoussam. We left school at seven o'clock and arrived at nine. The "
    "manager welcomed us and explained how the water was cleaned. He gave us a lot of information about the machines. Each of the students was "
    "given a bottle of water. After the visit, we thanked him for his kindness and returned home tired but happy. The teacher said that it was "
    "a visit we would never forget."
)

# ---- Editing: punctuation, spelling and word-choice errors (8 errors; 'affect' is correct)
E2_ERR = (
    "Our school principle announced that there will be a sports day on Friday, all students must wear white shirts. Students who dont want to "
    "run can join the choir. The weather forcast says that rain may affect the match, so the organisers have discussed about moving it "
    "indoors. Because the hall is more cheaper to prepare than the field. Parents are welcome, the entrance is free."
)
E2_FIX = (
    "Our school principal announced that there will be a sports day on Friday; all students must wear white shirts. Students who don't want to "
    "run can join the choir. The weather forecast says that rain may affect the match, so the organisers have discussed moving it indoors, "
    "because the hall is cheaper to prepare than the field. Parents are welcome; the entrance is free."
)

# ---- Editing: condensing
E3_LONG = (
    "It is a fact that, in the present day and age, a very large number of young people who are students in our schools spend a great deal of "
    "their time every single day looking at the screens of their mobile telephones. This is a habit that has become very common. Many of these "
    "students stay awake until very late at night, and as a result of this they are tired and sleepy in class the next morning. Teachers have "
    "complained that the students do not pay attention. In addition to this, the students' marks have fallen. It is therefore my opinion that "
    "school authorities should introduce a rule that phones must be handed in to the teacher at the start of each school day."
)
E3_SHORT = (
    "Many students spend too much time on their phones and stay awake late, so they are tired and inattentive in class and their marks have "
    "fallen. School authorities should therefore require phones to be handed in at the start of each day."
)

# ---- Editing: reorganising (mixed advantages and disadvantages)
E4_MIX = (
    "Motorbike taxis (called bendskin in Cameroon) are cheap, so many people use them. They are dangerous because riders seldom wear helmets. "
    "They can enter narrow streets that cars cannot. Accidents injure many passengers every year. They also create jobs for thousands of "
    "young men. Some riders ignore traffic lights."
)
E4_ORG = (
    "Motorbike taxis (called bendskin in Cameroon) have clear advantages. They are cheap, they can enter narrow streets that cars cannot, and "
    "they create jobs for thousands of young men.\n\n"
    "However, they are also dangerous. Riders seldom wear helmets, some ignore traffic lights, and accidents injure many passengers every year."
)

# ---- Editing: three extracts for text structures and language features (invented)
F_INF = (
    "The Moko Highlands lie in the north of the region. Their height, between 1,000 and 2,000 metres, makes the climate cooler than on the "
    "coast. For this reason, farmers grow maize, beans and coffee there. Rainfall is heaviest between April and October."
)
F_PER = (
    "Do you want your children to sleep safely tonight? Of course you do. Then join us. Our neighbourhood watch needs you: a few hours a "
    "week, a torch, a whistle and a brave heart. Together we can make every street safe."
)
F_IMG = (
    "The harmattan wind came down from the north like a dry hand, wiping the colour from the hills. Dust hung in the air, and the sun, a pale "
    "coin, rolled slowly over the roofs."
)



_POS = [1, 3, 0, 2, 2, 0, 3, 1]   # position of the correct option: each set of 8 has A, B, C and D twice
_count = [0]


def Q(prompt, right, wrongs, step, concept, skill, hint, feedback=""):
    """4-option MC. `wrongs` is 3 (text, why) pairs; the correct option is placed by a fixed cycle."""
    pos = _POS[_count[0] % 8]
    _count[0] += 1
    assert len(wrongs) == 3
    choices = []
    w = iter(wrongs)
    for i in range(4):
        if i == pos:
            choices.append(C(right, correct=True))
        else:
            t, why = next(w)
            choices.append(C(t, why=why))
    steps = [S("Reasoning", text=s) for s in ([step] if isinstance(step, str) else step)]
    return MC(prompt, choices, steps, concept=concept, skill=skill, hint=hint, feedback=feedback)


def N(prompt, answer, step, concept, skill, hint, unit="words"):
    _count[0] += 1
    steps = [S("Reasoning", text=s) for s in ([step] if isinstance(step, str) else step)]
    return NUM(prompt, answer, steps, tolerance=0, unit=unit, concept=concept, skill=skill, hint=hint)


SETS = []



# ================================================================== 1. Selecting points
SETS.append(practice_set(
    module=M_SUM, topic=T_SELECT, title="Finding the points that matter", lesson="enu1-summary-select-points",
    questions=[
        Q("Which sentence best defines a summary?",
          "A shorter text that gives the main points of a longer text in your own words, without your opinions",
          [("A copy of the first paragraph of the passage", "Copying is lifting, and the first paragraph may not hold all the main points."),
           ("A list of every fact in the passage in a smaller handwriting", "A summary selects; it does not include every fact."),
           ("The passage with some adjectives removed", "That is still the writer's words and not a selection of main points.")],
          "A summary selects the main points, uses your own words and adds no opinion.", T_SELECT, "Recall", "Think of what you tell your mother about your school day."),
        Q("Task on the Mbeng passage: 'Summarise the problems the village had before the project.' Which fact is needed?\n\n" + P_WATER,
          "Women walked three kilometres to a muddy stream",
          [("The farmers' union added 3,000,000 FCFA", "That is part of the solution, not a problem."),
           ("A caretaker collects 500 FCFA a month", "That is how the system is run now."),
           ("Other villages have sent visitors", "That is a later result.")],
          "The task decides the points. Problems come from paragraph 1.", T_SELECT, "Application", "Read the task words before you choose points."),
        Q("Task: summarise the Foumban bus passage in about 30 words. Which detail is LEAST necessary?\n\n" + P_BUS,
          "The buses were bought in January",
          [("Late arrivals fell sharply", "This is the main result."),
           ("Many pupils were late because taxis were full", "This is the problem that the project solves."),
           ("The council says two buses are too few", "This is a main point: the problem is not fully solved.")],
          "The month is a small detail; the problem, action, result and limitation are main points.", T_SELECT, "Analysis", "Which fact would the reader not miss?"),
        Q("Why should you read the task before you read the passage?",
          "The task tells you which points are needed",
          [("The task contains the answer", "It does not; it tells you what to look for."),
           ("It saves you from reading the passage", "You must still read the passage carefully."),
           ("It tells you which words to copy", "You should use your own words.")],
          "The task decides what counts as a main point.", T_SELECT, "Concept", "Think of how the task changes the points you need."),
        Q("A candidate copies the Mbeng passage from the top until the words run out. What is the main fault?",
          "The points were not chosen according to the task, and the ending, which holds the results, was lost",
          [("The candidate used too many figures", "The fault is not about figures but about selection."),
           ("The candidate wrote in the past tense", "Tense is not the issue here."),
           ("The candidate included a title", "Nothing in the question says a title was added.")],
          "Choose points first; the end of a passage often holds the results.", T_SELECT, "Analysis", "What did the candidate not do before writing?"),
        Q("Which of these should NOT appear in a summary?",
          "I believe the village was foolish to wait twenty years",
          [("The committee collected 1,200,000 FCFA", "It is a main fact from the passage."),
           ("A caretaker collects a small fee for repairs", "It is a main fact from the passage."),
           ("Pupils now attend school more regularly", "It is a main result.")],
          "A summary has no opinion of the summariser.", T_SELECT, "Reasoning", "Is the sentence in the passage?"),
        Q("What is the main idea of paragraph 2 of the Mbeng passage (the committee, the money, the pipes)?\n\n" + P_WATER,
          "The village raised money and built a water system",
          [("The village is in the Western Highlands", "That is a detail from paragraph 1."),
           ("Children missed school", "That is a problem in paragraph 1."),
           ("Illness has fallen", "That is a result in paragraph 3.")],
          "Paragraph 2 describes the action taken.", T_SELECT, "Interpretation", "Say the paragraph in six words."),
        Q("A question asks for a summary in one paragraph of not more than 60 words. Which answer follows the Board's advice?",
          "One paragraph of 58 words with no title and no introduction paragraph",
          [("A title and one paragraph of 58 words", "A title was not asked for."),
           ("Two paragraphs of 30 words each", "Two paragraphs break the instruction."),
           ("Six numbered points of 10 words each", "A list is not continuous prose and is not one paragraph.")],
          "Follow the instruction to the letter: one paragraph, within the limit, no extras.", T_SELECT, "Application", "Check number of paragraphs, number of words and extras."),
    ]))



# ================================================================== 2. Paraphrasing
SETS.append(practice_set(
    module=M_SUM, topic=T_SELECT, title="Paraphrasing in your own words", lesson="enu1-paraphrase-own-words",
    questions=[
        Q("Which is the best paraphrase of: 'Some children missed school.'?",
          "A number of pupils were absent from lessons.",
          [("All children missed school.", "*Some* has become *all*, so the meaning changed."),
           ("Some children missed school.", "It is lifted without any change."),
           ("Children never go to school.", "This is untrue and extreme.")],
          "Keep the strength (some means a number, not all) and change the words.", T_SELECT, "Application", "Keep some; change the other words."),
        Q("Which word should be kept unchanged when you paraphrase 'The committee collected 1,200,000 FCFA'?",
          "1,200,000 FCFA",
          [("collected", "It can be replaced by *raised*."),
           ("families", "It can be replaced by *households*."),
           ("from", "It can be replaced by *among* or the structure can change.")],
          "Figures and amounts of money are exact.", T_SELECT, "Concept", "Which item has no synonym?"),
        Q("Which paraphrase changes the meaning of 'The nurse says there may be fewer cases next year'?",
          "The nurse says there will be no cases next year.",
          [("The nurse thinks illness could fall next year.", "The meaning is kept: may is *could*."),
           ("According to the nurse, fewer people might fall ill next year.", "The meaning is kept."),
           ("The nurse expects a smaller number of cases next year, possibly.", "The meaning is kept.")],
          "*May be fewer* is possible; *will be no* is certain and total.", T_SELECT, "Analysis", "Compare strength words: may, will, no."),
        Q("Which is a paraphrase by change of voice of 'The council bought two buses'?",
          "Two buses were bought by the council.",
          [("The council buys two buses.", "That changes the tense and is not a change of voice."),
           ("Two buses buy the council.", "The subject and object are reversed."),
           ("The council had two buses.", "That changes the meaning.")],
          "Active to passive moves the object to the front.", T_SELECT, "Concept", "Who did what to whom?"),
        Q("A candidate paraphrases 'a few cases' as 'many cases'. What is wrong?",
          "The strength of the statement has changed",
          [("A paraphrase must be longer", "Length is not the rule."),
           ("Numbers must never be changed into words", "The problem is the meaning of few and many."),
           ("Paraphrasing is not allowed in summaries", "It is expected where necessary.")],
          "A paraphrase must keep few as few.", T_SELECT, "Reasoning", "Compare few and many."),
        Q("Which is the best paraphrase of 'Within a term, late arrivals fell sharply'?",
          "Within one school term, lateness dropped greatly.",
          [("Within a term, late arrivals fell sharply.", "It is lifted."),
           ("Lateness rose slowly over the year.", "It means the opposite."),
           ("Late arrivals disappeared in one day.", "It exaggerates and changes the time.")],
          "Change the words and keep the idea and the time frame: lateness fell a great deal within a term.", T_SELECT, "Application", "Which one says the same in new words?"),
        Q("Which is the best reason for looking away from the passage while you write a paraphrase?",
          "It stops you copying phrases",
          [("It makes the summary longer", "That is not the aim."),
           ("It lets you add your own ideas", "You must not add ideas."),
           ("It lets you change the names of people", "Names must not be changed.")],
          "Writing from memory of the idea gives your own wording.", T_SELECT, "Concept", "What does copying come from?"),
        Q("Which pair shows a change of word class that keeps the meaning?\n'The rise in prices was rapid.'",
          "'Prices rose rapidly.'",
          [("'Prices fell rapidly.'", "The opposite direction."),
           ("'The price was raised by the rapid.'", "It is ungrammatical."),
           ("'Rapid prices rose.'", "It is ungrammatical.")],
          "Noun *rise* becomes verb *rose*, adjective *rapid* becomes adverb *rapidly*.", T_SELECT, "Application", "Turn the noun into a verb."),
    ]))



# ================================================================== 3. Text types
SETS.append(practice_set(
    module=M_SUM, topic=T_TYPES, title="Summarising different text types", lesson="enu1-summary-text-types",
    questions=[
        Q("Which is the best opening for a summary of this speech?\n\n" + X_SPEECH,
          "The speaker argues that the market is dangerous and proposes a way to clean it.",
          [("Fellow citizens, the market is dangerous.", "It copies the speaker's address to the audience."),
           ("I think the speaker is right about the market.", "It gives the summariser's opinion."),
           ("The speech was very good.", "It comments on the speech instead of reporting its message.")],
          "Use a reporting verb, the third person and a neutral voice.", T_TYPES, "Application", "Report the message neutrally."),
        Q("Which details should a summary of minutes keep?",
          "Decisions, amounts, dates and who will act",
          [("The time each item was discussed and the seating plan", "These are routine details."),
           ("The feelings of the Secretary", "Minutes do not record feelings."),
           ("The names of the people who clapped", "This is not a decision or action.")],
          "Minutes record what was decided and who will act.", T_TYPES, "Concept", "Think of the reader who missed the meeting."),
        Q("Which summary of the debate is the most balanced?\n\n" + X_DEBATE,
          M_DEBATE,
          [("The proposer says uniforms should stay because they are good.", "It gives only one side."),
           ("The opposer is right that uniforms are costly, so they should go.", "It gives only one side and an opinion."),
           ("Both speakers talk about uniforms.", "It says nothing about what each argued.")],
          "A debate summary gives both sides, linked by whereas or while.", T_TYPES, "Application", "Which one includes both speakers?"),
        Q("Which tense suits a summary of the minutes of a meeting that has ended?",
          "The past tense",
          [("The present tense", "That suits the message of a speech or a general article."),
           ("The future tense throughout", "Only future actions use *will*."),
           ("The present perfect only", "It is not the normal tense for a record of finished events.")],
          "Minutes record finished decisions: *agreed*, *approved*; future actions use *will*.", T_TYPES, "Concept", "Is the meeting over?"),
        Q("What must a summary of a formal letter of complaint keep?\n\n" + X_LETTER,
          "The purpose (complaint and request), the key facts and the deadline",
          [("The greeting and the closing formula", "These are routine parts of the letter."),
           ("Only the date of purchase", "That is only one detail."),
           ("The writer's address", "It is not in the text and not a main point.")],
          "Keep purpose, facts and the request.", T_TYPES, "Application", "Why was the letter written?"),
        Q("In a summary of the story about Tabe, which detail can be dropped?\n\n" + X_STORY,
          "He was trembling and his uncle was smiling",
          [("The river was swollen and the bridge was gone", "It is the problem."),
           ("He crossed in the fishermen's canoe", "It is the solution."),
           ("He had walked for two hours", "It is part of the setting that explains the situation.")],
          "A story summary keeps the problem, the solution and the outcome.", T_TYPES, "Analysis", "Which detail is only decoration?"),
        Q("Which reporting verb best fits a speaker who says 'If we do nothing, more children will fall ill'?",
          "warns",
          [("agrees", "Nobody is agreeing with an earlier speaker here."),
           ("asks", "The speaker is not asking a question."),
           ("thanks", "No thanks are given.")],
          "A warning tells what may happen if something is not done.", T_TYPES, "Application", "What is the speaker doing?"),
        Q("A candidate ends a summary of a debate with 'So uniforms are good.' What is wrong?",
          "It adds the summariser's own opinion and favours one side",
          [("It is too short", "Length is not the problem."),
           ("It uses the present tense", "Tense is not the problem."),
           ("It repeats a word from the passage", "The fault is opinion, not repetition.")],
          "A summary must be neutral and keep the meaning of the original.", T_TYPES, "Reasoning", "Whose opinion is it?"),
    ]))



# ================================================================== 4. Limits
SETS.append(practice_set(
    module=M_SUM, topic=T_LIMITS, title="Writing to a word and paragraph limit", lesson="enu1-summary-word-paragraph-limits",
    questions=[
        N("Count the words (each group of letters or figures between spaces is one word):\n\n" + M_BUS, wc(M_BUS),
          "Count word by word, with 1,200,000-type figures as one word. The total is %d." % wc(M_BUS), T_LIMITS, "Calculation", "Count in tens."),
        Q("A question says: 'Summarise in one paragraph of not more than 70 words.' Which answer follows it?",
          "One paragraph of 66 words, no title",
          [("One paragraph of 82 words", "It is over the limit."),
           ("Two paragraphs of 33 words each", "It breaks the paragraph limit."),
           ("A title and one paragraph of 66 words", "A title was not asked for.")],
          "One paragraph, within the limit, nothing extra.", T_LIMITS, "Application", "Check three things: paragraphs, words, extras."),
        N("How many words is the trimmed summary of the Mbeng article below?\n\n" + D_TRIM, wc(D_TRIM),
          "Count the words: the total is %d, which is inside a limit of 55." % wc(D_TRIM), T_LIMITS, "Calculation", "Count carefully; figures count as one word."),
        Q("You have six points and a limit of 90 words. About how many words can each point have?",
          "About 15",
          [("About 6", "That divides 90 by 15, not by 6."),
           ("About 30", "That would use 180 words."),
           ("About 90", "That is the whole limit.")],
          "90 divided by 6 is 15.", T_LIMITS, "Calculation", "Divide the limit by the number of points."),
        Q("Your draft is 120 words and the limit is 90. What is the best first step?",
          "Delete small details and repetition, and merge sentences",
          [("Delete the last two sentences", "The ending may hold a main point."),
           ("Write smaller", "The word count does not change."),
           ("Add a title", "A title adds words and was not asked for.")],
          "Cut detail throughout; keep the main points.", T_LIMITS, "Application", "Which cut keeps the main points?"),
        Q("Which phrase can replace 'in spite of the fact that' to save words?",
          "although",
          [("because", "It gives a cause, not a contrast."),
           ("therefore", "It gives a result."),
           ("for example", "It gives an example.")],
          "*In spite of the fact that* shows contrast, like *although*.", T_LIMITS, "Concept", "Which word shows contrast?"),
        Q("Which is a transition marker of ADDITION?",
          "furthermore",
          [("however", "It marks contrast."),
           ("consequently", "It marks result."),
           ("although", "It marks contrast.")],
          "Furthermore, in addition, also, besides add a point.", T_LIMITS, "Recall", "Which one adds another point?"),
        Q("The Board's report says that some candidates lost marks in the summary because they",
          "wrote more than one paragraph and added titles and introductory paragraphs when the instruction did not ask for them",
          [("wrote in one paragraph as instructed", "That is correct practice."),
           ("crossed out their plan", "The report recommends crossing out the plan."),
           ("used transition markers", "The report praises them.")],
          "Follow the instructions to the letter.", T_LIMITS, "Recall", "Recall the Board's advice."),
    ]))



# ================================================================== 5. Sequencing and cohesion
_JUMBLE = ("a. As a result, the shop now closes at six.\nb. Last year, thieves broke into the shop twice.\n"
           "c. The owner then installed two lights and a strong door.\nd. Mr Ngu runs a small shop near the junction.\n\n")
SETS.append(practice_set(
    module=M_REC, topic=T_SEQ, title="Ordering sentences and filling gaps", lesson="enu1-reconstruction-sequencing-cohesion",
    questions=[
        Q("Which sentence is most likely to OPEN a text?",
          "A new clinic opened in Wum last week.",
          [("However, the clinic was not ready.", "However marks contrast with an earlier statement."),
           ("This surprised everyone in the town.", "*This* refers back to something already said."),
           ("Therefore, patients came early.", "Therefore gives the result of an earlier sentence.")],
          "An opening introduces something new with *a/an* and no link back.", T_SEQ, "Concept", "Which sentence needs no sentence before it?"),
        Q(_JUMBLE + "Put the sentences in order.",
          "d, b, c, a",
          [("b, d, c, a", "The shop must be introduced before the thieves are mentioned."),
           ("d, c, b, a", "The owner's reaction (c) cannot come before the problem (b)."),
           ("a, b, c, d", "*As a result* cannot open the text.")],
          "d introduces the shop, b gives the problem, c the action (then), a the result.", T_SEQ, "Application", "Find the sentence that introduces Mr Ngu."),
        Q("In 'A new bridge opened on Monday. The bridge replaces a wooden one.', why does the second sentence use *the*?",
          "The bridge has already been mentioned",
          [("Because *the* is more formal than *a*", "The choice depends on mention, not formality."),
           ("Because bridges are always definite", "A noun is introduced with *a* the first time."),
           ("Because the first sentence was short", "Length does not decide the article.")],
          "First mention: a. Later mention: the.", T_SEQ, "Concept", "Has the bridge been named before?"),
        Q("Which word best fills the gap? 'The road was narrow. (______), many drivers avoided it.'",
          "Consequently",
          [("Nevertheless", "It shows an unexpected contrast."),
           ("Meanwhile", "It shows events at the same time."),
           ("For instance", "The second sentence is not an example of the first.")],
          "The second sentence is a result.", T_SEQ, "Application", "Result, contrast, time or example?"),
        Q("Which gap-word fits? '(______) the rain began, everybody ran for shelter.'",
          "When",
          [("Although", "It shows contrast, which does not fit."),
           ("Because of", "It needs a noun, not a clause."),
           ("Unless", "It sets a condition, which does not fit.")],
          "A time clause with a clause after it needs *when*.", T_SEQ, "Application", "Which word opens a time clause?"),
        Q("In a reconstruction task, a student lists only the missing words instead of writing out the whole passage. According to the Board's report on a task of this type,",
          "the student loses half of the marks scored in that section",
          [("the student gets bonus marks for speed", "No such credit exists."),
           ("the student is credited in full", "The Board's report says the opposite."),
           ("the student's answer is not marked", "It is marked, but with a penalty.")],
          "Follow the instruction and write out the full text.", T_SEQ, "Recall", "Recall the Board's remark on listing words."),
        Q("A sentence begins 'Since then, villagers have crossed by canoe.' Which sentence must come BEFORE it?",
          "A sentence stating when the bridge collapsed",
          [("A sentence about the opening party", "It does not give the time that *then* refers to."),
           ("A sentence about the council's inspections in future", "A future plan comes later."),
           ("A sentence thanking the workers", "It does not give the time that *then* refers to.")],
          "*Then* refers back to a time already given.", T_SEQ, "Reasoning", "Which sentence gives the time?"),
        Q("Which pair shows a word chain (lexical cohesion)?",
          "footbridge ... the bridge ... the new structure",
          [("at ... in ... on", "These are prepositions, not a chain of the same idea."),
           ("first ... ten ... Monday", "They are unrelated words."),
           ("quickly ... slowly ... never", "They are adverbs but not a chain of the same thing.")],
          "A word chain repeats or renames the same thing.", T_SEQ, "Concept", "Which words name one thing in different ways?"),
    ]))



# ================================================================== 6. Letters, articles, reports
SETS.append(practice_set(
    module=M_REC, topic=T_RTYPES, title="Letters, news articles and reports in order", lesson="enu1-reconstruct-letters-articles-reports",
    questions=[
        Q("Which paragraph usually comes first in the body of a formal letter?",
          "The purpose of the letter",
          [("The polite close", "The close comes last."),
           ("The request for help", "The request comes after the reasons and plan."),
           ("The details of the plan", "The plan follows the purpose and reasons.")],
          "Tell the reader at once why you are writing.", T_RTYPES, "Recall", "What must the reader know first?"),
        Q("A letter begins 'Dear Madam,'. Which closing is correct?",
          "Yours faithfully,",
          [("Yours sincerely,", "It is used when the person is named."),
           ("Your friend,", "It is informal."),
           ("Best wishes,", "It is informal.")],
          "No name used: Yours faithfully.", T_RTYPES, "Recall", "Is the receiver named?"),
        Q("Which sentence is the best LEAD of a news article?",
          "Forty students cleaned the school compound on Saturday and removed sixty sacks of waste.",
          [("The principal thanked the volunteers.", "A reaction comes later."),
           ("The club plans to repeat the exercise.", "A future plan comes at the end."),
           ("She said that the drains had been blocked.", "*She* has no earlier mention.")],
          "The lead gives who, what, where, when and the result.", T_RTYPES, "Application", "Which sentence tells the whole story at once?"),
        Q("Report sentences:\na. It is recommended that the council repair the road.\nb. This report examines the road to Nkwen.\nc. The road has 14 holes in 3 kilometres.\nd. It is clear that the road is unsafe.\n\nWhat is the correct order?",
          "b, c, d, a",
          [("a, b, c, d", "The recommendation comes last."),
           ("b, a, c, d", "The recommendation cannot come before the findings."),
           ("c, b, d, a", "The introduction must come first.")],
          "Introduction, finding, conclusion, recommendation.", T_RTYPES, "Application", "Which sentence states the purpose?"),
        Q("Notes: 'Market, Saturday, 200 traders, rain, 3 stalls destroyed.' Which sentence builds them into text WITHOUT adding facts?",
          "On Saturday, 200 traders were at the market when rain destroyed three stalls.",
          [("On Saturday, about 500 traders ran from the rain and lost three stalls.", "It changes the number of traders."),
           ("On Saturday, rain destroyed three stalls, and the council promised new ones.", "It adds a fact."),
           ("Market Saturday 200 traders rain 3 stalls.", "It is not a sentence.")],
          "Use full sentences; keep facts exactly; add none.", T_RTYPES, "Application", "Which one keeps every figure unchanged?"),
        Q("A question gives you the name 'Ayuk Bih' and an address. How should you sign a formal letter?",
          "With the name given in the question",
          [("With your real name", "Candidates must conceal their identity."),
           ("With your school's name", "That also reveals identity."),
           ("Leave it unsigned", "A formal letter ends with a signature and name.")],
          "Use the name and address provided.", T_RTYPES, "Application", "Recall the rule on identity."),
        Q("Which sentence signals the END of a news article?",
          "The club plans to repeat the exercise every term.",
          [("Forty students cleaned the compound on Saturday.", "That is the lead."),
           ("The campaign began at 8 a.m.", "That is early detail."),
           ("Club president Miss Lum said the drains were blocked.", "That is middle detail.")],
          "Articles often end with a future plan or a reaction.", T_RTYPES, "Reasoning", "Which sentence looks ahead?"),
        Q("Which is true of the inverted pyramid in a news article?",
          "The most important facts come first and the details follow",
          [("The details come first and the main fact last", "That is the opposite."),
           ("Every paragraph has the same importance", "Importance decreases."),
           ("The writer's opinion must come first", "News articles report facts first.")],
          "Lead first, details after.", T_RTYPES, "Concept", "Which comes first, the key facts or the details?"),
    ]))



# ================================================================== 7. Dialogue, minutes, stories, speeches
SETS.append(practice_set(
    module=M_REC, topic=T_RTYPES, title="Dialogue, minutes, stories and speeches", lesson="enu1-reconstruct-dialogue-minutes-stories-speeches",
    questions=[
        Q("Report in the past: Neba said, 'I am tired.'",
          "Neba said that he was tired.",
          [("Neba said that he is tired.", "After a past reporting verb the present tense is usually backshifted."),
           ("Neba said that I was tired.", "The pronoun has not changed."),
           ("Neba said, that he was tired?", "A report has no question mark and no comma here.")],
          "am becomes was; I becomes he.", T_RTYPES, "Application", "Change the tense and the pronoun."),
        Q("Report: Tanyi asked Bih, 'Do you have enough money?'",
          "Tanyi asked Bih whether she had enough money.",
          [("Tanyi asked Bih do you have enough money?", "A report has normal word order and no question mark."),
           ("Tanyi asked Bih that she had enough money.", "A question is reported with whether or if."),
           ("Tanyi asked Bih whether she has enough money?", "A report has no question mark.")],
          "Questions become whether/if clauses with statement order.", T_RTYPES, "Application", "Which word introduces a yes-no question?"),
        Q("Report: Bih said, 'I will repay you next month.' (to Tanyi, past reporting verb)",
          "Bih told Tanyi that she would repay him the following month.",
          [("Bih told Tanyi that she will repay him next month.", "Will should become would."),
           ("Bih told Tanyi that I would repay you the following month.", "The pronouns have not changed."),
           ("Bih told Tanyi that he would repay her the following month.", "The pronouns are reversed.")],
          "will to would; I to she; you to him; next month to the following month.", T_RTYPES, "Application", "Change tense, pronouns and time words."),
        Q("Which sentence is in the correct style for minutes?",
          "It was agreed that the fence would be repaired.",
          [("We agree that we shall repair the fence.", "First person and present tense do not suit minutes."),
           ("The fence is broken says the Chairperson.", "It is present tense and not reported."),
           ("I think we must repair the fence.", "Minutes do not record the writer's opinion.")],
          "Minutes use the past tense, the third person and the passive for decisions.", T_RTYPES, "Concept", "Past tense, third person."),
        Q("A story has these sentences:\na. Suddenly she noticed that her purse was missing.\nb. It was market day, and Nkeng was selling plantains.\nc. A boy returned the purse.\nWhat is the best order?",
          "b, a, c",
          [("a, b, c", "The setting must come first."),
           ("c, b, a", "The solution cannot come first."),
           ("b, c, a", "The purse cannot be returned before it is lost.")],
          "Setting, complication, resolution.", T_RTYPES, "Application", "Which sentence sets the scene?"),
        Q("In a speech, which part comes right after the greeting?",
          "The theme of the speech",
          [("The thanks to the audience", "Thanks come at the end."),
           ("The call to action", "The call to action comes near the end."),
           ("The closing greeting", "It is not a part of the usual structure.")],
          "Greeting, theme, body, call to action, thanks.", T_RTYPES, "Recall", "What does the speaker announce first?"),
        Q("The Board's report on a dialogue task found that candidates lost marks when they",
          "wrote in point form instead of continuous prose",
          [("wrote continuous prose", "That was what the task required."),
           ("followed the instructions", "That earned marks."),
           ("used the correct tense", "That earned marks.")],
          "Write a full prose passage.", T_RTYPES, "Recall", "Recall the Board's remark."),
        Q("Report in the present tense: Bih: 'I need 100,000 FCFA more.'",
          "Bih says that she needs 100,000 FCFA more.",
          [("Bih says that she needed 100,000 FCFA more.", "A present reporting verb does not require backshift."),
           ("Bih says that I need 100,000 FCFA more.", "The pronoun has not changed."),
           ("Bih said that she needs 100,000 FCFA more.", "The reporting verb is not in the present as the instruction requires.")],
          "Present reporting verb: no backshift; the pronoun still changes.", T_RTYPES, "Application", "Is the reporting verb present or past?"),
    ]))



# ================================================================== 8. Editing grammar
SETS.append(practice_set(
    module=M_EDIT, topic=T_CORRECT, title="Editing grammar errors", lesson="enu1-editing-grammar-errors",
    questions=[
        Q("Which sentence has NO error?",
          "Each of the boys was given a prize.",
          [("The children has finished their lunch.", "*Children* is plural: *have*."),
           ("She gave me many advices.", "*Advice* has no plural."),
           ("We discussed about the problem.", "*Discuss* takes no *about*.")],
          "*Each* is singular: *was*.", T_CORRECT, "Application", "Check agreement, plural nouns and prepositions."),
        Q("Correct: 'Yesterday, the driver stop the bus and ask us to get out.'",
          "Yesterday, the driver stopped the bus and asked us to get out.",
          [("Yesterday, the driver stops the bus and asks us to get out.", "Present tense does not match *yesterday*."),
           ("Yesterday, the driver stopped the bus and asks us to get out.", "The second verb is still wrong."),
           ("Yesterday, the driver has stopped the bus and asked us to get out.", "The present perfect does not match *yesterday*.")],
          "A past time word needs the past tense for both verbs.", T_CORRECT, "Application", "Look at the time word."),
        Q("Which is the correct form? 'The teacher gave us (______) about the exam.'",
          "a lot of information",
          [("many informations", "*Information* has no plural."),
           ("a lot of informations", "*Information* has no plural."),
           ("an information", "*Information* is uncountable and takes no *a*.")],
          "Information is uncountable.", T_CORRECT, "Concept", "Can you say *two informations*?"),
        Q("Which sentence is correct?",
          "We returned home late.",
          [("We returned at home late.", "*Home* needs no preposition here."),
           ("We returned back at home late.", "Both *back* and *at* are unnecessary."),
           ("We returned to the home late.", "It changes the meaning and sounds unnatural.")],
          "Home is an adverb here.", T_CORRECT, "Application", "Is a preposition needed before *home*?"),
        Q("Correct the repeated pronoun: 'It was a visit we would never forget it.'",
          "It was a visit we would never forget.",
          [("It was a visit that we would never forget it.", "The final *it* is still repeated."),
           ("It was a visit we would never to forget.", "*Would* is followed by the base verb without *to*."),
           ("It was a visit what we would never forget.", "*What* cannot be used as a relative pronoun here.")],
          "The relative object is already understood, so the final *it* is not needed.", T_CORRECT, "Application", "Is the object stated twice?"),
        Q("Which verb completes: 'The cost of the new desks (______) high.'?",
          "is",
          [("are", "The subject is *cost*, not *desks*."),
           ("were", "The subject is singular, and the tense is present."),
           ("have been", "The subject is singular.")],
          "Find the true subject: *cost*.", T_CORRECT, "Reasoning", "Ignore the phrase between subject and verb."),
        Q("In 'He said that he will come tomorrow' (said in the past), the best correction is",
          "He said that he would come the next day.",
          [("He said that he would come tomorrow.", "*Tomorrow* should change to *the next day* in a past report."),
           ("He said that he will come the next day.", "*Will* should be *would*."),
           ("He said that he comes the next day.", "The tense is wrong.")],
          "Backshift will to would and change the time word.", T_CORRECT, "Application", "Past reporting verb: change tense and time word."),
        Q("A candidate changes a correct sentence, 'The water was cleaned', into 'The water were cleaned' while editing. What is the fault?",
          "A correct sentence was changed and a new error was introduced",
          [("The candidate did not change the tense", "The tense was already right."),
           ("The candidate used the passive", "The passive was already in the text and is correct."),
           ("The candidate corrected too few sentences", "The fault is over-correction.")],
          "Change only what is wrong.", T_CORRECT, "Reasoning", "Was the original sentence correct?"),
    ]))



# ================================================================== 9. Editing punctuation, spelling, words
SETS.append(practice_set(
    module=M_EDIT, topic=T_CORRECT, title="Editing punctuation, spelling and word choice", lesson="enu1-editing-punctuation-spelling-words",
    questions=[
        Q("Which sentence is a comma splice?",
          "The road was flooded, we stayed at home.",
          [("The road was flooded, so we stayed at home.", "A conjunction follows the comma, so it is correct."),
           ("The road was flooded; we stayed at home.", "A semicolon is correct."),
           ("The road was flooded. We stayed at home.", "Two sentences with a full stop are correct.")],
          "Two full sentences joined by a comma alone.", T_CORRECT, "Concept", "Which one joins two sentences with only a comma?"),
        Q("Choose the correct word: 'The new rule will (______) all students.'",
          "affect",
          [("effect", "*Effect* is usually a noun."),
           ("affects", "After *will* the verb has no -s."),
           ("effects", "It is a plural noun.")],
          "Affect is the verb; effect is the noun.", T_CORRECT, "Application", "You need a verb after *will*."),
        Q("Which sentence is correctly punctuated?",
          "The students' books are on the table.",
          [("The student's books are on the table (many students).", "The apostrophe before s shows one student."),
           ("The students book's are on the table.", "The apostrophe is in the wrong word."),
           ("The students books are on the table.", "The possessive apostrophe is missing.")],
          "A plural noun ending in s takes the apostrophe after the s.", T_CORRECT, "Application", "Whose books? Many students."),
        Q("Which word is spelt correctly?",
          "forecast",
          [("forcast", "A letter is missing."),
           ("foracast", "An extra letter has been added."),
           ("forecaste", "An extra e has been added.")],
          "forecast = fore + cast.", T_CORRECT, "Recall", "Break the word into two parts."),
        Q("Correct: 'The school principle announced a holiday.'",
          "The school principal announced a holiday.",
          [("The school principle announced a holiday.", "*Principle* means a rule."),
           ("The school principals announced a holiday.", "One head teacher is meant."),
           ("The school principle's announced a holiday.", "An apostrophe does not mend the word.")],
          "The principal is the head of a school.", T_CORRECT, "Application", "Which word means the head?"),
        Q("Which is correct?",
          "This hall is cheaper than the field.",
          [("This hall is more cheaper than the field.", "Double comparative."),
           ("This hall is more cheap than the field.", "*Cheap* takes -er, not *more*."),
           ("This hall is cheaperer than the field.", "A double -er form is not English.")],
          "One comparative form only.", T_CORRECT, "Concept", "Remove the double comparative."),
        Q("Which fragment is repaired by joining it to the sentence before it?\n'The match was moved indoors. Because it was raining.'",
          "The match was moved indoors because it was raining.",
          [("The match was moved indoors. Because it was raining!", "The fragment remains."),
           ("The match was moved indoors, because. It was raining.", "It breaks the sentence again."),
           ("The match was moved indoors. Raining.", "It is still a fragment.")],
          "A *because* clause depends on a main clause.", T_CORRECT, "Application", "A *because* clause cannot stand alone."),
        Q("Which sentence contains a redundancy (a word that repeats an idea)?",
          "We will repeat the exercise again next week.",
          [("We will repeat the exercise next week.", "No idea is repeated."),
           ("We will do the exercise again next week.", "No idea is repeated."),
           ("We will do the exercise next week.", "No idea is repeated.")],
          "*Repeat* already means do again, so *again* is redundant.", T_CORRECT, "Analysis", "Does any word say what another word already says?"),
    ]))



# ================================================================== 10. Condensing and reorganising
SETS.append(practice_set(
    module=M_EDIT, topic=T_CONDENSE, title="Condensing and reorganising texts", lesson="enu1-editing-condense-reorganise",
    questions=[
        Q("Which phrase can be replaced by the single word *much*?",
          "a great deal of",
          [("in addition to this", "That means *also*."),
           ("as a result of this", "That means *so*."),
           ("in the present day and age", "That means *today*.")],
          "a great deal of = much.", T_CONDENSE, "Recall", "Which phrase shows quantity?"),
        Q("Which is the best condensed version of: 'It is a fact that many students are tired every single day.'?",
          "Many students are tired daily.",
          [("It is a fact that students are tired.", "The empty opening remains and *many* is lost."),
           ("Students are tired.", "*Many* is lost; the meaning changes."),
           ("Many students are not tired daily.", "The meaning is reversed.")],
          "Delete the empty opening; every single day becomes daily; keep many.", T_CONDENSE, "Application", "Delete the opening and shorten the time phrase."),
        N("How many words does the condensed text have?\n\n" + E3_SHORT, wc(E3_SHORT),
          "Count the words. The total is %d, inside the limit of 45 used in the lesson." % wc(E3_SHORT), T_CONDENSE, "Calculation", "Count carefully."),
        Q("When you reorganise a mixed text about the benefits and the problems of a new market, you should",
          "group the benefits in one paragraph and the problems in another",
          [("delete the problems", "Facts must not be dropped."),
           ("put the longest sentences first", "Length is not a logical order."),
           ("make each sentence a paragraph", "That breaks paragraph unity.")],
          "Group by theme, one idea per paragraph.", T_CONDENSE, "Concept", "What makes a paragraph clear?"),
        Q("When condensing, which must NOT change?",
          "The main ideas and the meaning",
          [("The empty opening phrases", "They can be deleted."),
           ("The wordy phrases", "They can be shortened."),
           ("The repeated ideas", "Repetition can be cut.")],
          "Condense the words, never the meaning.", T_CONDENSE, "Concept", "What is the point of the text?"),
        Q("Which phrase is the best short form of 'in spite of the fact that'?",
          "although",
          [("because", "It gives a reason, not contrast."),
           ("so", "It gives a result."),
           ("also", "It adds a point.")],
          "In spite of the fact that = although.", T_CONDENSE, "Recall", "Which shows contrast?"),
        Q("Which edit loses a main point when condensing 'Pupils are late because taxis are full, so the council bought two buses'?",
          "Pupils are late.",
          [("Pupils are late because taxis are full, so the council bought buses.", "It keeps all main points."),
           ("Taxis are full, so the council bought two buses for late pupils.", "It keeps all main points."),
           ("The council bought two buses because pupils were late.", "It keeps the main points.")],
          "The cause and the action have both been lost.", T_CONDENSE, "Analysis", "Which version keeps the least?"),
        Q("In reorganising, the sentence 'However, they are also dangerous' is best used",
          "as the topic sentence of a paragraph about disadvantages",
          [("as the last sentence of the essay", "It introduces a new theme, so it fits at the start of a paragraph."),
           ("in the middle of a list of advantages", "It would break the group."),
           ("as a title", "It is a sentence, not a title.")],
          "It signals a change of theme.", T_CONDENSE, "Application", "What does *however* signal?"),
    ]))



# ================================================================== 11. Text structures and language features
SETS.append(practice_set(
    module=M_EDIT, topic=T_STRUCT, title="Identifying and explaining language features", lesson="enu1-text-structures-language-features",
    questions=[
        Q("Which feature is typical of a persuasive text?",
          "Questions and commands addressed to the reader",
          [("A neutral tone with technical terms", "That is informative."),
           ("A long description with similes", "That is imaginative."),
           ("Numbered findings in the passive voice", "That is report style.")],
          "Persuasion speaks to the reader.", T_STRUCT, "Recall", "Think of an advertisement."),
        Q("'The sun, a pale coin, rolled over the roofs.' The words 'a pale coin' are",
          "a metaphor",
          [("a simile", "A simile uses *like* or *as*."),
           ("a rhetorical question", "It is not a question."),
           ("a command", "It is not an instruction.")],
          "The sun is said to be a coin without *like*.", T_STRUCT, "Concept", "Is there *like* or *as*?"),
        Q("Why would an informative text use the present tense?\n\n" + F_INF,
          "It states facts that are generally true",
          [("It tells a story in the past", "That is an imaginative text."),
           ("It makes the reader afraid", "That is not its purpose."),
           ("It copies the speech of a person", "That is not shown.")],
          "General facts are in the present tense.", T_STRUCT, "Reasoning", "Are the facts true now?"),
        Q("In 'Do you want your children to sleep safely tonight?', the question",
          "involves the reader and makes them think of their own family",
          [("gives a fact about children", "It is a question, not a fact."),
           ("describes the weather", "It does not."),
           ("reports what someone said", "It is a direct question to the reader.")],
          "A rhetorical question draws in the reader.", T_STRUCT, "Interpretation", "Who is being asked?"),
        Q("'a torch, a whistle and a brave heart' is an example of",
          "a list of three",
          [("a simile", "No comparison with *like* or *as*."),
           ("a metaphor", "No thing is said to be another."),
           ("reported speech", "No report of speech.")],
          "A list of three gives rhythm.", T_STRUCT, "Recall", "Count the items."),
        Q("Which sentence explains a language feature BEST?",
          "The command *join us* gives the reader something to do and urges them to act.",
          [("The writer uses a command.", "It names the feature but does not explain its effect."),
           ("*Join us* is a sentence.", "It does not identify or explain the feature."),
           ("The writer wants people to join.", "It says what the writer wants but does not name the feature.")],
          "Feature + example + effect.", T_STRUCT, "Reasoning", "Does it name the feature and the effect?"),
        Q("Which pair is correct?",
          "News article: lead with key facts; Story: opening, problem, ending",
          [("News article: ends with the key facts; Story: starts with the moral", "Reverse order."),
           ("News article: written in the first person; Story: has headings and numbered findings", "Those belong to other types."),
           ("News article: no facts; Story: only facts", "The reverse of the truth.")],
          "Each type has its own order.", T_STRUCT, "Concept", "Recall the structure of each."),
        Q("An editor must make a persuasive notice more persuasive. Which change helps most?",
          "Add a rhetorical question addressed to the reader",
          [("Remove all verbs", "A text without verbs is hard to read."),
           ("Add many technical terms", "That suits an informative text."),
           ("Change it into a long description of weather", "That suits an imaginative text.")],
          "Persuasion uses direct appeal.", T_STRUCT, "Application", "Which feature involves the reader?"),
    ]))



# ================================================================== 12. Paper 3 strategy
SETS.append(practice_set(
    module=M_EXAM, topic=T_P3, title="Paper 3 strategy check", lesson="enx3-paper-3-strategy",
    questions=[
        Q("How long is Paper 3 of English Language 0730?",
          "2 hours 15 minutes",
          [("1 hour 30 minutes", "That is the length of Paper 1."),
           ("3 hours", "Paper 3 is shorter."),
           ("45 minutes", "That is the time suggested for one section.")],
          "Paper 3 lasts 2 hours 15 minutes.", T_P3, "Recall", "Recall the paper structure."),
        Q("Which are the three sections of Paper 3?",
          "Summary writing, Text reconstruction and Editing",
          [("Composition, Prescribed texts and Creative writing", "Those are the sections of Paper 2."),
           ("Reading comprehension, Speech work and Grammar", "Those are sections of Paper 1."),
           ("Summary writing, Prescribed texts and Grammar", "These are not the sections of Paper 3.")],
          "Paper 3 = Summary writing, Text reconstruction, Editing.", T_P3, "Recall", "Paper 3 is the language production paper."),
        Q("How are the sections of Paper 3 answered?",
          "All three are compulsory",
          [("Answer any two", "No choice of sections is offered."),
           ("Answer one section only", "All three sections are compulsory."),
           ("Choose either Section A or Section B, then C", "No choice of sections is offered.")],
          "All compulsory, 15 marks each.", T_P3, "Recall", "Recall the paper structure."),
        Q("A summary question says: 'one paragraph of not more than 120 words'. Which is the best answer?",
          "One paragraph of 115 words, no title, plan crossed out",
          [("Three short paragraphs of 40 words each", "It breaks the paragraph limit."),
           ("A title, an introduction and a paragraph of 100 words", "Titles and introductions were not asked for."),
           ("A list of bullet points of 90 words", "Bullet points are not continuous prose.")],
          "Follow the instruction to the letter.", T_P3, "Application", "Check paragraphs, words, extras."),
        Q("In a letter task the name given is 'Ayuk Bih'. Which sign-off is correct?",
          "Yours faithfully, Ayuk Bih (for a letter beginning Dear Sir)",
          [("Yours faithfully, your own real name", "Identity must be concealed."),
           ("Yours sincerely, Ayuk Bih (for a letter beginning Dear Sir)", "*Sincerely* goes with a named receiver."),
           ("Your friend, Ayuk", "It is informal.")],
          "Use the name given; match the closing to the greeting.", T_P3, "Application", "Recall the rule on identity."),
        Q("According to the Board's report on a reconstruction task, a candidate who lists only the missing words, instead of writing out the passage,",
          "loses half of the marks scored in that section",
          [("receives extra marks", "It is penalised."),
           ("is marked as for a full answer", "The report says marks are lost."),
           ("has the answer ignored", "It is marked, but half of the marks are lost.")],
          "Write out the passage when asked.", T_P3, "Recall", "Recall the penalty."),
        Q("About how long does the syllabus table allow for each section of Paper 3?",
          "45 minutes",
          [("15 minutes", "That is too short."),
           ("90 minutes", "That would use the whole paper for two sections."),
           ("135 minutes", "That is the length of the whole paper.")],
          "Three sections of about 45 minutes fill 135 minutes.", T_P3, "Recall", "Divide 135 by 3."),
        Q("Which action is NOT allowed in Paper 3?",
          "Using your own name and school in a letter",
          [("Planning and crossing out the plan", "That is good practice."),
           ("Using the name and address provided", "That is required."),
           ("Checking your work at the end", "That is good practice.")],
          "Candidates must conceal their identity.", T_P3, "Reasoning", "Which action reveals identity?"),
    ]))



# ================================================================== 13. Paper 3 skills check A (mock)
_count[0] = 0
_J = ("a. Then the owner repaired it.\nb. A shop roof leaked last year.\nc. Now customers stay dry.\n\n")
_Q = []
_Q += [  # ---- Summary: 8
    Q("**Passage (invented)**\n\n" + P_BUS + "\n\nWhich is a MAIN point for a short summary?",
      "Late arrivals fell and parents say children are safer",
      [("The buses were bought in January", "It is a small detail of time."),
       ("Pupils wait by the roadside every morning", "It sets the scene and can be shortened."),
       ("The drivers were hired", "It is a detail of the action.")],
      "The result is a main point.", T_SELECT, "Application", "Which one is a result?"),
    Q("**Passage (invented)**\n\n" + P_BUS + "\n\nWhich is the best paraphrase of 'Many arrive late because the taxis are already full'?",
      "A lot of pupils get to school after the start because every taxi is already taken.",
      [("Many arrive late because the taxis are already full.", "It is lifted."),
       ("All pupils arrive late because taxis are expensive.", "It changes *many* to *all* and adds a new reason."),
       ("Pupils never arrive on time.", "It exaggerates.")],
      "Keep many and the reason; change the words.", T_SELECT, "Application", "Keep the cause and the strength."),
    Q("A summary should NOT contain",
      "the summariser's own opinion",
      [("the main points of the passage", "A summary must contain them."),
       ("words of the summariser", "Own words are expected."),
       ("key figures that matter", "They may be kept.")],
      "No opinions.", T_SELECT, "Concept", "What must stay out?"),
    Q("Which is the best opening of a summary of a speech?",
      "The speaker urges parents to support a school bus fund.",
      [("Dear parents, today I want to speak to you.", "It copies the speaker's style."),
       ("I like this speech.", "It gives an opinion."),
       ("The speech began at ten o'clock.", "It is an irrelevant detail.")],
      "A reporting verb in the third person.", T_TYPES, "Application", "Report the message."),
    Q("In a summary of minutes, which detail is LEAST important?",
      "The time the meeting ended",
      [("A decision to spend 60,000 FCFA", "It is a main decision."),
       ("Who will write to the other club", "It is an action."),
       ("The date of the friendly match", "It is a key date.")],
      "Decisions and actions matter most.", T_TYPES, "Analysis", "Which one is routine?"),
    Q("A summary of a debate must",
      "give the main arguments of both sides",
      [("give only the side the summariser prefers", "It would be unfair."),
       ("include the names of the audience", "It is irrelevant."),
       ("end with the summariser's vote", "It adds an opinion.")],
      "Neutral and balanced.", T_TYPES, "Concept", "Think of balance."),
    Q("A question asks for a summary of 'not more than 60 words'. Which answer follows the instruction?",
      "A paragraph of 57 words",
      [("A paragraph of 75 words", "It exceeds the limit."),
       ("A title and a paragraph of 57 words", "A title was not asked for."),
       ("Five bullet points of 12 words each", "It is not continuous prose and has 60 words but breaks the format.")],
      "One paragraph within the limit.", T_LIMITS, "Application", "Check words and format."),
    Q("Which is a transition marker of result?",
      "consequently",
      [("although", "It shows contrast."),
       ("furthermore", "It adds a point."),
       ("meanwhile", "It shows time.")],
      "Consequently shows result.", T_LIMITS, "Recall", "Cause and effect."),
]
_Q += [  # ---- Reconstruction: 8
    Q(_J + "Put the sentences in order.",
      "b, a, c",
      [("a, b, c", "The leak must be mentioned before the repair."),
       ("c, a, b", "*Now* belongs at the end."),
       ("b, c, a", "The repair must come before the result.")],
      "Problem, action (then), result (now).", T_SEQ, "Application", "Find the problem first."),
    Q("Which sentence is most likely to open a news report?",
      "A new school opened in Bamenda on Monday.",
      [("However, the school was not ready.", "However needs an earlier sentence."),
       ("This pleased the parents.", "*This* refers back."),
       ("Consequently, pupils came early.", "Consequently needs an earlier sentence.")],
      "An opening introduces a new topic.", T_SEQ, "Concept", "Which sentence needs nothing before it?"),
    Q("Which gap-word fits? 'The market was crowded. (______) traders had come early, the buyers came later.'",
      "While",
      [("Because", "It gives a cause that does not fit."),
       ("Unless", "It sets a condition."),
       ("Since", "It would suggest a cause or time, not a contrast.")],
      "The two groups are in contrast.", T_SEQ, "Application", "Contrast."),
    Q("Why does 'The bridge' in sentence 2 come after 'A new bridge' in sentence 1?",
      "The first mention uses *a* and later mentions use *the*",
      [("*The* is always used first", "*A* is used for first mention."),
       ("Because sentence 2 is longer", "Length does not decide it."),
       ("Because bridges are always definite", "The article depends on mention.")],
      "A then the.", T_SEQ, "Concept", "Which article is used first?"),
    Q("Which paragraph usually comes first in the body of a formal letter?",
      "The purpose of the letter",
      [("The polite ending", "It comes last."),
       ("The request for help", "It follows the reasons and plan."),
       ("The details of the plan", "They follow the purpose.")],
      "State the purpose first.", T_RTYPES, "Recall", "What must the reader know first?"),
    Q("Report: Bih said, 'I need 100,000 FCFA.' (past reporting verb)",
      "Bih said that she needed 100,000 FCFA.",
      [("Bih said that she needs 100,000 FCFA.", "No backshift."),
       ("Bih said that I needed 100,000 FCFA.", "The pronoun is unchanged."),
       ("Bih said, that she needed 100,000 FCFA?", "A report has no question mark.")],
      "need becomes needed; I becomes she.", T_RTYPES, "Application", "Change tense and pronoun."),
    Q("Which sentence is in the correct style for minutes?",
      "It was agreed that the match would be held on 5 July.",
      [("We agree that the match is on 5 July.", "It is in the first person and the present tense."),
       ("I think the match should be on 5 July.", "It gives an opinion."),
       ("The match will be fun.", "It is not a record of a decision.")],
      "Past tense, passive for decisions.", T_RTYPES, "Concept", "Past tense and impersonal."),
    Q("A news article ends with which kind of sentence?",
      "A look to the future, such as a plan to repeat the event",
      [("The key facts: who, what, where, when", "That is the lead."),
       ("The headline", "The headline comes first."),
       ("The introduction of the writer", "News articles do not introduce the writer.")],
      "Lead first; future or reaction last.", T_RTYPES, "Recall", "Where do key facts come?"),
]
_Q += [  # ---- Editing: 9
    Q("Which sentence is correct?",
      "Each of the girls has her book.",
      [("Each of the girls have their book.", "*Each* is singular."),
       ("Each of the girls are having her book.", "The verb and the form are wrong."),
       ("Each of the girl has her book.", "*Of the* is followed by a plural noun.")],
      "Each takes a singular verb.", T_CORRECT, "Application", "Check agreement."),
    Q("Correct: 'The informations were very useful.'",
      "The information was very useful.",
      [("The informations was very useful.", "*Informations* is still wrong."),
       ("The information were very useful.", "The verb should be singular."),
       ("The an information was very useful.", "It is ungrammatical.")],
      "Information is uncountable.", T_CORRECT, "Application", "Is it countable?"),
    Q("Which is a comma splice?",
      "The hall was cheap, we booked it.",
      [("The hall was cheap, so we booked it.", "Correct with a conjunction."),
       ("The hall was cheap; we booked it.", "Correct with a semicolon."),
       ("The hall was cheap. We booked it.", "Correct with a full stop.")],
      "Two sentences joined by a comma.", T_CORRECT, "Concept", "Which has only a comma?"),
    Q("Choose the correct word: 'Heavy rain may (______) the match.'",
      "affect",
      [("effect", "It is usually a noun."),
       ("affects", "After *may* the base form is used."),
       ("effects", "It is a plural noun.")],
      "Affect is a verb.", T_CORRECT, "Application", "A verb is needed."),
    Q("Which phrase is the best short form of 'in spite of the fact that'?",
      "although",
      [("because", "It is a reason."),
       ("so", "It is a result."),
       ("also", "It adds a point.")],
      "Contrast.", T_CONDENSE, "Recall", "Contrast."),
    Q("When you reorganise a text about benefits and problems, you should",
      "group the benefits together and the problems together",
      [("delete the problems", "Facts must not be lost."),
       ("put each sentence in its own paragraph", "It breaks unity."),
       ("change the facts", "Meaning must not change.")],
      "Group by theme.", T_CONDENSE, "Concept", "One idea per paragraph."),
    Q("Which feature is typical of a persuasive text?",
      "A rhetorical question to the reader",
      [("Numbered findings", "Report style."),
       ("A neutral tone and technical terms", "Informative."),
       ("A long description of scenery", "Imaginative.")],
      "Persuasion addresses the reader.", T_STRUCT, "Recall", "Think of an advertisement."),
    Q("'The wind came down like a dry hand.' The phrase 'like a dry hand' is",
      "a simile",
      [("a metaphor", "A metaphor has no *like*."),
       ("a command", "It is not an instruction."),
       ("a list of three", "It has no list.")],
      "Simile: *like* or *as*.", T_STRUCT, "Concept", "Is there *like*?"),
    Q("Which sentence explains a language feature BEST?",
      "The command *join us* urges the reader to act.",
      [("The writer uses a command.", "It does not explain the effect."),
       ("*Join us* is a sentence.", "It does not identify the feature."),
       ("The writer wants people to join.", "It does not name the feature.")],
      "Feature, example and effect.", T_STRUCT, "Reasoning", "Does it explain the effect?"),
]
assert len(_Q) == 25

SETS.append(practice_set(
    module=M_EXAM, topic=T_P3, title="Paper 3 skills check A", lesson="enx3-paper-3-strategy",
    mock=True, time_limit_minutes=135, questions=_Q))
