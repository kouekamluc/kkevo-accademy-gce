"""A Level English Language (0730), Upper Sixth: Paper 3 skills. Summary Writing, Text Reconstruction, Editing and the Paper 3 exam lesson.

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

LESSONS = []


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


# ================================================================== 1. Summary: selecting points
LESSONS.append(lesson(
    module=M_SUM, topic=T_SELECT,
    title="Summary writing: finding the points that matter",
    slug="enu1-summary-select-points",
    minutes=22,
    summary="A summary keeps the main points of a passage and drops examples, repetition and detail. Read for the task, mark every possible point, sort main points from support, then list the points before you write.",
    objectives=["Say what a summary is and what Section A of Paper 3 asks you to do",
                "Read a passage for the task and mark the points that answer it",
                "Sort main points from examples, repetition and figures of little value",
                "Make a short numbered list of points that is ready to be written in your own words"],
    key_concepts=["Summary", "Main point", "Supporting detail", "Task wording", "Plan"],
    blocks=[
        H("Introduction"),
        T("Every day we summarise. When you tell your mother what happened at school, you do not repeat every word the teacher said. You give the **main things** and leave out the rest. Paper 3, Section A asks for exactly this skill. It has **one compulsory question worth 15 marks**, and you answer it in the time given for the whole of Paper 3 (2 hours 15 minutes for three sections)."),
        T("The Board's syllabus says that the aim of this section is to summarise a text **without altering the meaning of the original**. Its objective adds that you should **paraphrase** (use your own words) where necessary. In this lesson you learn the first half of the skill: *finding* the points. The next lesson teaches the second half: *putting them in your own words*."),
        D("A **summary** is a shorter text that gives the main points of a longer text, in your own words, in a stated length, without adding your own opinions and without changing the meaning.", title="Definition"),
        TIP("The Board's report on the 2023 examination says that candidates did better when they planned, used their own words and linked ideas with transition markers, and lost marks when they ignored the instructions: for example, writing several paragraphs when one was asked for, adding a title or an introduction paragraph, or writing in point form. Always follow the instruction exactly. Check the exact marking scheme with your teacher.", title="Exam link"),
        H("The five-step route"),
        KEY("From passage to summary", "Do these in order every time. Steps 1 to 3 are this lesson.", cards=[
            ["1. Read the task", "What exactly must the summary cover? How many words? How many paragraphs?"],
            ["2. Read the passage", "Read once for the general idea, then again with a pencil."],
            ["3. Mark and sort", "Mark every point that answers the task. Drop examples and repetition."],
            ["4. Paraphrase", "Write the points in your own words (next lesson)."],
            ["5. Link and check", "Join with linking words, count the words, cross out the plan."]]),
        IMG("al-enu1-summary-route.svg", alt="A flow of five boxes: read the task, read the passage, mark and sort, paraphrase, link and check.", caption="Figure 1. The five-step route from passage to summary."),
        H("Step 1: let the task decide"),
        T("A summary is never 'everything in a short form'. The task tells you **which** points you need. Compare two tasks on the same passage. 'Summarise how the villagers got clean water' needs the money, the work and the system. 'Summarise the problems the villagers had before' needs only the long walk, missed school and illness. Underline the key words of the task before you read the passage."),
        H("Step 2 and 3: mark and sort"),
        T("Here is a passage (invented for practice). Read it with this task: **Summarise in one paragraph of not more than 90 words how Mbeng got clean water and what has changed.**"),
        CODE(P_WATER + "\n\n(" + str(wc(P_WATER)) + " words)", "text", title="Passage: Water at last in Mbeng (invented)"),
        KEY("Keep or drop?", "Use these questions on every sentence.", cards=[
            ["Keep", "A main point that answers the task: a cause, a result, a reason, a decision, a main fact."],
            ["Keep (short)", "A key figure when it is part of the answer, such as the amount of money raised."],
            ["Drop", "An example given only to illustrate (the nurse's exact numbers)."],
            ["Drop", "Repetition, comments by the writer, and small details (who dug, how long the trench was)."]]),
        EX("Worked example 1: marking the points", intro="Task: how Mbeng got clean water and what has changed.", steps=[
            S("Paragraph 1: the problem", text="Long walk of three kilometres to a muddy stream; children missed school; diarrhoea. These explain *why* the village needed water, so keep them briefly."),
            S("Paragraph 2: the action", text="Committee collected 1,200,000 FCFA from families; the farmers' union added 3,000,000 FCFA; pipes, tank and two taps. Keep. The unpaid trench digging is a small detail; keep it only if there is room."),
            S("Paragraph 3: the result", text="Water from a protected spring; a caretaker and monthly fee; better attendance; fewer stomach illnesses; other villages visiting. Keep the main results."),
            S("Drop", text="The exact figures 'four cases' and 'twenty' are an example of the improvement. 'Fewer cases of illness' is enough. Also drop the population of 900 and the saving of 800,000 FCFA."),
            S("Make the list", text="1 Dirty water, far away: school missed, illness. 2 Committee raised 1,200,000 FCFA; union gave 3,000,000 FCFA. 3 Pipes, tank, two taps from a protected spring. 4 Caretaker, small fee for repairs. 5 More school attendance, less illness. 6 Other villages interested.")]),
        MISTAKE("Taking points in the order of the passage without checking the task", "Some candidates copy the passage from the top and stop when they run out of words. Choose points first. If the question asks for the changes, the end of the passage matters more than the beginning."),
        QUIZ("In the Mbeng passage, which sentence is an EXAMPLE that can be dropped from a 90-word summary?",
             ["Young men from the village dug the trench for the pipes without pay.", "The farmers' union agreed to add 3,000,000 FCFA.", "For example, the nurse recorded only four cases last month, compared with about twenty a month before the project.", "A caretaker keeps the taps clean and collects a monthly fee."],
             2, "The sentence beginning 'For example' only illustrates the point that illness has fallen. The point itself ('fewer cases of illness') is what you keep.",
             hint="Look for words such as 'for example'.",
             feedback=["This is a small detail about how the pipes were laid, but it is not introduced as an example of something else.", "This is a main fact: where the money came from.", "", "This is a main point about how the system is kept running."]),
        H("Step 3 again: the paragraph test"),
        T("When a passage is long, find the **main idea of each paragraph** in one short phrase. Then ask what supports it. If a sentence only repeats the main idea or gives a case, it is support. In the Mbeng passage the three paragraph ideas are: *the problem*, *the action* and *the result*. A summary that has one or two points for each has a good shape."),
        EX("Worked example 2: from list to one sentence per idea", intro="Turn the six listed points into a plan of three sentences.", steps=[
            S("Group the points", text="Problem (1), action (2, 3, 4), result (5, 6)."),
            S("Choose a linking idea for each group", text="Problem: *because*. Action: *therefore*. Result: *consequently*."),
            S("Check the plan against the limit", text="Three sentences of about 25 to 30 words give a paragraph of about 80 to 90 words. The plan fits.")]),
        T("Here is a model summary of the Mbeng passage for you to compare with your own. It has " + str(wc(M_WATER)) + " words, so it keeps within 90:"),
        CODE(M_WATER, "text", title="Model summary (" + str(wc(M_WATER)) + " words)"),
        PQ("Read this passage (invented). Task: list the main points in a numbered list of not more than five points.\n\n" + P_BUS,
           "1 Pupils were late because the taxis were full. 2 The council bought two buses. 3 The fare is 100 FCFA, under half the taxi fare. 4 Lateness has fallen and parents say children are safer. 5 Two buses are too few; the council wants three more. The January date and the number of pupils are details that can be dropped."),
        PQ("Which of these are main points and which are details, in the Foumban passage? (a) hundreds of pupils wait each morning (b) pupils pay 100 FCFA, less than half a taxi fare (c) the buses were bought in January.",
           "(b) is a main point because it explains why the buses help. (a) sets the scene and can be shortened to 'many pupils'. (c) is a detail of time that can be dropped unless the task asks when."),
        PQ("Write a summary of the Foumban passage in one sentence of not more than 35 words.\n\nHint: use the plan of problem, action, result.",
           M_BUS + "  (" + str(wc(M_BUS)) + " words.) Other correct answers are possible if they keep the problem, the action and the result in your own words."),
        SUM("A summary gives the main points of a passage, in your own words, within a limit, without opinions.",
            "Read the task first: it decides which points you need.",
            "Mark the points that answer the task; drop examples, repetition and small details.",
            "Find the main idea of each paragraph, then list the points in a short numbered plan.",
            "Follow the instructions exactly: one paragraph means one paragraph, and no title unless asked.")
    ]))


# ================================================================== 2. Paraphrasing
LESSONS.append(lesson(
    module=M_SUM, topic=T_SELECT,
    title="Paraphrasing: same meaning, your own words",
    slug="enu1-paraphrase-own-words",
    minutes=22,
    summary="To paraphrase is to say the same thing in different words and a different structure. Change what can be changed, keep names, figures and key terms, and never change the meaning or add anything.",
    objectives=["Explain why paraphrasing is needed and what it must not do",
                "Use synonyms, change of word class, active and passive, and a new sentence structure",
                "Recognise words that should not be changed",
                "Avoid lifting and avoid changing the meaning"],
    key_concepts=["Paraphrase", "Lifting", "Synonym", "Word class change", "Meaning shift", "Strength of a statement"],
    blocks=[
        H("Introduction"),
        T("A friend tells you that her uncle's shop has closed. You repeat it to your mother: 'Her uncle has stopped trading.' You have **paraphrased**. The meaning is the same, but the words are yours. The Board's syllabus lists this as an objective of Section A: *paraphrase where necessary, using their own words*."),
        D("To **paraphrase** is to express the meaning of a text in different words (and often in a different sentence structure) so that the meaning is exactly the same. **Lifting** is copying words or phrases from the passage instead.", title="Definition"),
        T("The Board's report on the 2023 examination gave two warnings that pull in opposite directions. Candidates who **copied** the passage lost marks for expression. But candidates who tried too hard to use their own words sometimes **changed the content** of the passage, and so lost marks for content. A good paraphrase avoids both mistakes."),
        TIP("In a summary, long stretches copied word for word from the passage are 'lifting'. Short, essential words (names, figures, technical terms) may be kept. Ask your teacher how the marking scheme treats them.", title="Exam link"),
        H("Six ways to change a sentence"),
        KEY("Your paraphrasing toolkit", "Use more than one way in a sentence.", cards=[
            ["1. Synonyms", "*purchase* for *buy*; *small* for *limited*. The word must fit the sense."],
            ["2. Word class", "*The council decided* becomes *the council's decision*; *a rapid rise* becomes *rose rapidly*."],
            ["3. Voice", "Active to passive or back: *The council bought two buses* becomes *Two buses were bought by the council*."],
            ["4. Structure", "Change the order of clauses: *Because X, Y* becomes *Y, since X*."],
            ["5. Combine or split", "Join two short sentences, or split a long one."],
            ["6. Negative form", "*not rich* is not always *poor*, so use this only when the meaning is the same: *seldom* for *not often*."]]),
        H("What NOT to change"),
        T("Some words have no good substitute, or changing them would alter the meaning."),
        KEY("Keep these as they are", "", cards=[
            ["Names and places", "Mbeng, Foumban, the council, the farmers' union"],
            ["Figures and money", "1,200,000 FCFA, three kilometres, 90%"],
            ["Technical or exact terms", "diarrhoea, protected spring, committee"],
            ["Very common words", "water, school, people, village: you cannot replace these without sounding odd"]]),
        H("Meaning is stronger than style"),
        T("A paraphrase can fail even when every word is different. These small changes alter the meaning:"),
        CODE("""Passage                      Faulty paraphrase           Why it is wrong
-----------------------------------------------------------------------
some children missed school  all pupils were absent      some -> all
may cause illness            causes illness              possible -> certain
a few cases                  many cases                  few -> many
the committee decided        the village chose           committee -> whole village
he said he would help        he helped                   promise -> fact""", "text", title="Words that shift the meaning"),
        MISTAKE("Changing the strength of a statement", "Words such as *some, most, all, may, will, a few, many, often, always* show how strong a claim is. Keep the strength: if the passage says *may*, your summary must not say *will*."),
        EX("Worked example 1: one sentence, three tries", intro="Paraphrase: \"The sudden rise in the price of fuel forced many taxi drivers to increase their fares.\"", steps=[
            S("Try 1: change a few words only", text="'The sudden rise in the price of petrol forced many cab drivers to increase their fares.' This is still almost the original. It would be called lifting."),
            S("Try 2: change word class and structure", text="'Fuel suddenly became much more expensive, so many cab drivers raised what they charged.' *Rise in price* becomes *became more expensive* (noun to adjective); *forced* becomes the link *so*; *fares* becomes *what they charged*."),
            S("Check the meaning", text="Sudden: *suddenly*. Many drivers: *many cab drivers*. Cause and result are kept. Nothing is added. Good."),
            S("Try 3 (faulty)", text="'Fuel prices went up, so all drivers doubled their fares.' This changes *many* to *all* and invents *doubled*. It must be rejected.")]),
        EX("Worked example 2: a short paragraph", intro="Paraphrase this passage in about half the words: \"The caretaker, who was chosen by the committee, keeps the taps clean and collects a small monthly fee of 500 FCFA from each household for repairs.\"", steps=[
            S("Find the ideas", text="(1) A caretaker was chosen by the committee. (2) He or she keeps the taps clean. (3) The fee is 500 FCFA a month per household. (4) The fee pays for repairs."),
            S("Choose what to keep", text="Keep all four ideas; keep 500 FCFA exactly. Change the verbs and the order."),
            S("Write", text="'Households pay 500 FCFA a month towards repairs, and a caretaker appointed by the committee cleans the taps.'"),
            S("Check", text="Appointed for chosen, cleans for keeps clean, towards repairs for for repairs. Every idea is present; nothing is added.")]),
        QUIZ("Which is the best paraphrase of \"Many students stay awake until very late at night\"?",
             ["Many students stay awake until very late at night.", "A good number of students do not go to sleep until the small hours.", "All students sleep very late each night.", "Many students never sleep."],
             1, "It keeps the strength (*a good number* for *many*) and the idea of a late bedtime.",
             hint="One option is not a paraphrase at all. Two change the meaning.",
             feedback=["This is lifting: it repeats the sentence exactly.", "", "*All* is stronger than *many*.", "*Never sleep* is untrue and extreme."]),
        QUIZ("Which word in a passage should be kept unchanged in a summary?",
             ["quickly", "1,200,000 FCFA", "decided", "important"],
             1, "Figures and amounts of money are exact and have no synonym. Words such as *quickly*, *decided* and *important* can usually be replaced.",
             hint="Which one cannot be said in another way without losing exactness?",
             feedback=["It can be replaced, for example by *rapidly*.", "", "It can be replaced, for example by *resolved*.", "It can be replaced, for example by *significant*."]),
        H("A routine for the exam room"),
        T("**Read the point, cover the sentence, say it aloud in your head, then write.** If you do not look at the passage while you write, you will not copy it. Then compare your sentence with the passage to check that no idea has been lost or added."),
        PQ("Paraphrase: \"Young men from the village dug the trench for the pipes without pay.\"",
           "For example: 'Unpaid youths from the village dug the channel for the pipes.' (A good answer keeps the ideas: young men, the village, digging, the trench for pipes, no payment. *Trench* and *pipes* may be kept.)"),
        PQ("Paraphrase and shorten: \"Within a term, late arrivals fell sharply, and parents say their children are safer.\"",
           "For example: 'Lateness dropped quickly, and parents feel their children are safer.' (*Within a term* may be kept or shortened to *within months* only if the passage allows it; do not change the time.)"),
        PQ("A candidate paraphrases \"the clinic reports fewer cases of stomach illness\" as \"the clinic has no more cases of stomach illness\". What is wrong?",
           "*Fewer* means a smaller number; *no more* means none. The meaning has changed. A correct version is 'the clinic is seeing less stomach illness'."),
        SUM("To paraphrase is to keep the meaning and change the words and structure.",
            "Use synonyms, change word class, change voice or sentence order, combine or split sentences.",
            "Keep names, figures, technical terms and very common words.",
            "Never change the strength of a statement (some, many, all, may, will) and never add ideas.",
            "Copying whole phrases is lifting; changing the meaning is also penalised. Look away from the passage while you write.")
    ]))


# ================================================================== 3. Summarising different text types
LESSONS.append(lesson(
    module=M_SUM, topic=T_TYPES,
    title="Summarising letters, speeches, debates, minutes and stories",
    slug="enu1-summary-text-types",
    minutes=24,
    summary="Each text type has its own shape: a speech argues, minutes record decisions, a debate has two sides, a letter makes a request, a story follows events. Summarise the shape, with consistent tense and a neutral voice.",
    objectives=["Identify the text type and say what its summary must keep",
                "Summarise a speech, minutes, a debate, a letter and a story in one or two sentences",
                "Choose reporting verbs and a consistent tense for the summary",
                "Keep your own opinion out of the summary"],
    key_concepts=["Text type", "Reporting verb", "Neutral voice", "Tense consistency", "Decisions and actions", "Both sides of a debate"],
    blocks=[
        H("Introduction"),
        T("The Board's syllabus says that the texts used in Paper 3 are of different types: **letters, newspaper articles, reports, speeches, debates, talks and lectures, minutes, discourse and stories**. The Board's report on the 2023 examination described that year's summary text as informative, but the syllabus allows any of the types, so be ready for each of them."),
        T("The method you learnt in the first two lessons does not change. What changes is **what the text is trying to do**. A summary must keep that purpose visible."),
        D("A **text type** (or genre) is a kind of text with a recognisable purpose and form: for example a letter asks, informs or complains; a speech persuades an audience; minutes record what a meeting decided; a story tells events in order.", title="Definition"),
        KEY("What to keep for each type", "Ask: what would the reader of my summary NEED to know?", cards=[
            ["Speech or talk", "The speaker's main message, the reasons given, the call to action."],
            ["Debate", "Each side's main arguments, kept fair and balanced."],
            ["Minutes", "Who, when, what was decided, who will do what."],
            ["Letter", "The writer's purpose (request, complaint, application) and the main facts."],
            ["Story", "Main events in order, the turning point and the outcome."],
            ["Article or report", "The main facts, causes, results and any recommendation."]]),
        H("Tense and voice in a summary"),
        T("Whatever the text, your summary should have **one consistent tense**. Use the **present tense** for the message of a speech, a debate or a general article ('The speaker argues...'). Use the **past tense** for events that have finished, such as minutes or a story ('The club agreed...'; 'Tabe crossed the river'). Use **third person** and a **neutral voice**: 'the speaker argues', not 'I think the speaker is right'."),
        TIP("Useful reporting verbs: *argues, proposes, claims, warns, urges, explains, requests, complains, agrees, decides, approves, replies, concludes*. Choose the verb that matches what the speaker is doing.", title="Language"),
        H("A speech"),
        CODE(X_SPEECH + "\n\n(" + str(wc(X_SPEECH)) + " words)", "text", title="Text 1: a speech (invented)"),
        EX("Worked example 1: summarising a speech", intro="Summarise the speech in one sentence of not more than 35 words.", steps=[
            S("Identify the type and purpose", text="A speech to persuade: the speaker wants the market made clean."),
            S("List the points", text="Danger: overflowing drains, children play near. Some blame the council, some blame traders. Solution: council gives bins, traders pay a small weekly fee. Result: clean in a month."),
            S("Drop", text="'Fellow citizens', 'Let us work together' and 'start this Saturday' are the speaker's style and can go."),
            S("Write", text=M_SPEECH + " (" + str(wc(M_SPEECH)) + " words)")]),
        H("Minutes of a meeting"),
        CODE(X_MINUTES + "\n\n(" + str(wc(X_MINUTES)) + " words)", "text", title="Text 2: minutes (invented)"),
        T("Minutes are already a record of decisions. Keep **decisions, amounts, dates and who will act**. Drop the routine items: the time, who was present, and the reading of the last minutes."),
        EX("Worked example 2: summarising minutes", intro="Summarise the decisions in not more than 35 words.", steps=[
            S("Find the decisions", text="Spend 60,000 FCFA (of 85,000) on balls and nets; friendly match against Bali on 5 July; the Secretary will write to Bali."),
            S("Choose the tense", text="Past, because the meeting has ended: 'agreed', 'approved'. The future action stays in the future: 'will write'."),
            S("Write", text=M_MINUTES + " (" + str(wc(M_MINUTES)) + " words)")]),
        H("A debate"),
        CODE(X_DEBATE + "\n\n(" + str(wc(X_DEBATE)) + " words)", "text", title="Text 3: a debate (invented)"),
        T("In a debate summary, **both** sides must appear and neither is favoured. Use contrast words such as *whereas, while, however, but*."),
        CODE(M_DEBATE + "  (" + str(wc(M_DEBATE)) + " words)", "text", title="Model summary of the debate"),
        MISTAKE("Summarising only one side of a debate", "A summary that gives only the proposer's arguments, or ends with 'so uniforms are good', is incomplete and shows the summariser's own opinion. Give each side its main points."),
        H("A letter and a story"),
        CODE(X_LETTER + "\n\n(" + str(wc(X_LETTER)) + " words)", "text", title="Text 4: a formal letter (invented)"),
        CODE(M_LETTER + "  (" + str(wc(M_LETTER)) + " words)", "text", title="Model summary of the letter"),
        T("For the letter the summary keeps the purpose (complaint and request), the key facts (the price, the five days), the writer's denial and the deadline. It drops the greeting, the sign-off and the receipt."),
        CODE(X_STORY + "\n\n(" + str(wc(X_STORY)) + " words)", "text", title="Text 5: a story (invented)"),
        CODE(M_STORY + "  (" + str(wc(M_STORY)) + " words)", "text", title="Model summary of the story"),
        T("A story summary follows the order of events and keeps the problem and its solution. It drops description such as 'trembling', the lamp and the smile unless the question asks for feelings."),
        QUIZ("Which sentence would be the best start for a summary of a speech?",
             ["I think the speaker is right that the market should be cleaned.", "Fellow citizens, the speaker said that our market is dangerous.", "The speaker argues that the market is dangerous and proposes a way to clean it.", "The speech was very good and everybody clapped."],
             2, "It uses a reporting verb, the third person and the present tense, and it covers the message and the proposal.",
             hint="A summary of a speech reports the speaker's message neutrally.",
             feedback=["It gives your own opinion.", "It copies the speaker's address to the audience and mixes the audience's point of view.", "", "It describes the audience's reaction, which is not in the speech."]),
        QUIZ("A summary of minutes should keep",
             ["the exact time each item started", "the decisions and who will act", "the names of everybody present", "the Secretary's feelings about the meeting"],
             1, "Minutes exist to record decisions and actions. The time and the attendance list are routine details.",
             hint="Think of the reader who missed the meeting.",
             feedback=["Routine detail.", "", "Usually routine detail unless the question asks for it.", "Minutes record no feelings."]),
        PQ("Summarise in one sentence of not more than 30 words:\n\n\"Fellow students, our library opens for only two hours a day. Books are returned late or lost. I propose a library club to keep order, and every student giving one book at the end of the year. If we behave well, the head teacher will extend the hours.\"",
           "The speaker proposes a library club and a book gift from every student, so that, if students behave well, the head teacher will extend the library's opening hours. (28 words. Other answers are correct if they keep the proposals and the condition.)"),
        PQ("Summarise the story: \"Ayuk found a purse on the road. It held 10,000 FCFA and a school card. He ran to the school and gave it to the headmaster, who found the owner, a first-year girl. She thanked him and gave him a pencil.\"",
           "Ayuk found a purse with 10,000 FCFA and a school card and gave it to the headmaster, who returned it to its owner, a first-year girl. (The thank-you and the pencil are small details and can be dropped.)"),
        PQ("Why should a summary of a debate not end with a sentence such as 'Therefore uniforms are a good thing'?",
           "Because it gives the summariser's opinion, which is not in the text, and it favours one side. The summary must remain neutral and keep the meaning of the original."),
        SUM("Identify the text type first; it tells you what to keep.",
            "Speech: message, reasons, call to action. Debate: both sides. Minutes: decisions, amounts, dates, actions. Letter: purpose and key facts. Story: events in order.",
            "Use one consistent tense, the third person and reporting verbs.",
            "Never add your own opinion or comments.",
            "Drop greetings, style and decoration; keep the substance.")
    ]))


# ================================================================== 4. Word and paragraph limits
LESSONS.append(lesson(
    module=M_SUM, topic=T_LIMITS,
    title="Word and paragraph limits: writing to size",
    slug="enu1-summary-word-paragraph-limits",
    minutes=22,
    summary="Obey the limit in the question exactly: count your words, keep to the stated number of paragraphs, add no title or introduction unless asked, and trim by cutting detail, merging sentences and replacing phrases with single words.",
    objectives=["Count words in a summary using a clear rule",
                "Respect a word limit and a paragraph limit exactly as set",
                "Trim an over-long draft without losing main points",
                "Link points with transition markers inside one paragraph"],
    key_concepts=["Word limit", "Paragraph limit", "Counting rule", "Trimming", "Transition markers", "Plan crossed out"],
    blocks=[
        H("Introduction"),
        T("The syllabus lists, among the general objectives of Paper 3, that you should **respect word and paragraph limits**. A question may say, for example, *'Summarise in one paragraph of not more than 150 words'*. That is an instruction, not advice."),
        T("The Board's report on the 2023 examination says that some candidates scored poorly because they did not follow instructions: they wrote more than one paragraph, or they added titles and introductory paragraphs of their own. Others wrote in point form or fragments. The Board's recommendation was: follow the instructions to the letter. If you are not asked for a title, do not provide one."),
        KEY("Four rules about limits", "", cards=[
            ["1. Obey the number", "'Not more than 90 words' means 90 is the top. Stay at or below it."],
            ["2. Obey the paragraphs", "'One paragraph' means one block of connected sentences."],
            ["3. No extras", "No title, no introduction, no heading, no list or bullet points, unless the question asks."],
            ["4. Plan, then cross out", "Write a short plan if you need one, then cross out the plan, not your answer."]]),
        TIP("In Paper 3 Section A you have one compulsory question for 15 marks. The syllabus table suggests about 45 minutes for each of the three sections. Spend your time on reading, marking and planning, because a clear plan makes the writing fast.", title="Exam link"),
        H("How to count words"),
        D("In this course we count every group of letters or figures with a space on each side as **one word**. A hyphenated word (*two-hour*) is one word; a figure (*1,200,000*) is one word; *FCFA* is one word; *don't* is one word. Check your textbook and ask your teacher whether your examiner counts differently.", title="Counting rule"),
        CODE("""Sentence:  The committee collected 1,200,000 FCFA from families.
Words:     The(1) committee(2) collected(3) 1,200,000(4) FCFA(5) from(6) families(7)
Total:     7 words""", "text", title="Counting a sentence"),
        T("In the exam, count line by line. Mark every tenth word with a small tick in the margin, and write the total at the end in brackets if the question allows. Do not count the plan."),
        H("Planning to the limit"),
        T("Divide the limit by the number of points. If you have **six points** and a limit of **90 words**, each point gets about **15 words**. A point that needs 40 words is too big: make it smaller."),
        CODE("""Limit 90 words, 6 points  ->  about 15 words each
Aim for 80-90 words. Do not stop at 50: you will lose points.
Do not go over 90: you will lose marks for not following the instruction.""", "text", title="Words per point"),
        H("Trimming an over-long draft"),
        T("A first draft is often too long. Here is a draft of 104 words for a limit of **55 words**. We shall trim it in steps."),
        CODE(D_LONG + "\n\n(" + str(wc(D_LONG)) + " words: far too long for 55)", "text", title="First draft"),
        KEY("Six ways to cut", "Try them in this order.", cards=[
            ["1. Delete detail", "The population of the village, the trench digging."],
            ["2. Merge sentences", "Join short sentences with linking words."],
            ["3. Shorten phrases", "*because of this* to *so*; *in order to* to *to*."],
            ["4. Use figures well", "Keep the money figures that matter; drop the rest."],
            ["5. Cut repetition", "Do not say the same idea twice."],
            ["6. Choose strong words", "*walked three kilometres* is stronger than *went a long way*."]]),
        EX("Worked example 1: from 104 words to a limit of 55", intro="Task: summarise the Mbeng article in one paragraph of not more than 55 words.", steps=[
            S("Cut the detail", text="Remove 'which has about 900 people', 'every morning', 'very common', 'put up' and the free labour."),
            S("Merge", text="Join the problem and its results: '...walked three kilometres to a muddy stream for twenty years, so children missed school and illness spread.'"),
            S("Shorten phrases", text="'With this money, they bought pipes, built a concrete tank and put up two taps' becomes 'Pipes, a tank and two taps now bring spring water'."),
            S("Result", text=D_TRIM + " (" + str(wc(D_TRIM)) + " words: inside the limit of 55)")]),
        MISTAKE("Cutting by deleting the last sentences", "Do not simply stop writing when you reach the limit. The end of a passage often carries the result. Cut detail all through the draft instead of cutting the end."),
        H("Linking inside one paragraph"),
        T("One paragraph does not mean a pile of separate sentences. Use **transition markers** to show how the points connect. The Board's report names *first, furthermore, in addition, also* and *besides* as examples of the markers that good candidates used."),
        CODE("""Adding:       also, in addition, furthermore, besides, moreover
Contrast:     but, however, whereas, although, yet
Cause:        because, since, as, for this reason
Result:       so, therefore, consequently, as a result
Sequence:     first, then, next, finally, afterwards""", "text", title="Transition markers by job"),
        QUIZ("A question says: 'Summarise in one paragraph of not more than 80 words.' Which answer follows the instruction?",
             ["A title, then two paragraphs of 40 words each", "A numbered list of five points, 70 words", "One paragraph of 78 words with no title", "One paragraph of 95 words"],
             2, "One paragraph, inside the limit, with no title or list.",
             hint="Check the number of paragraphs, the word limit and the extras.",
             feedback=["A title was not asked for and the answer is in two paragraphs.", "A list is not continuous prose and is not one paragraph.", "", "It is one paragraph, but it exceeds the limit."]),
        QUIZ("The first draft is 120 words and the limit is 90. What is the best first thing to do?",
             ["Delete the last two sentences", "Delete examples and small details, and merge sentences", "Write smaller so that it looks shorter", "Add a title to show you understood"],
             1, "Cut detail and repetition throughout and merge sentences; this keeps the main points.",
             hint="Which cut keeps the main points?",
             feedback=["The ending may hold a main point.", "", "Size of handwriting does not change the word count.", "A title adds words and was not asked for."]),
        PQ("Count the words: \"Pupils in Foumban were often late because taxis were full, so the council bought two cheap buses.\"",
           "Pupils(1) in(2) Foumban(3) were(4) often(5) late(6) because(7) taxis(8) were(9) full,(10) so(11) the(12) council(13) bought(14) two(15) cheap(16) buses(17). Total: 17 words."),
        PQ("Trim this to not more than 20 words: \"It is a fact that, in spite of the fact that the buses are cheap, the council says that there are not enough of them.\"",
           "For example: 'Although the buses are cheap, the council says there are too few.' (12 words.) The empty opening 'It is a fact that' and the repeated 'the fact that' add nothing."),
        PQ("Write a summary of the Foumban passage in one paragraph of not more than 40 words. Count your words.\n\n" + P_BUS,
           M_BUS + "  (" + str(wc(M_BUS)) + " words.) Your wording will differ; check that it has the problem, the action and the result and that it is under 40 words."),
        SUM("Follow the limit in the question exactly: words and paragraphs.",
            "Do not add a title, an introduction or bullet points unless asked.",
            "Plan: limit divided by the number of points gives words per point.",
            "Trim by deleting detail, merging sentences and shortening phrases, not by cutting the end.",
            "Link the points with transition markers and cross out the plan, not your answer.")
    ]))


# ================================================================== 5. Sequencing and cohesion
LESSONS.append(lesson(
    module=M_REC, topic=T_SEQ,
    title="Putting a text in order: sequencing clues and cohesion",
    slug="enu1-reconstruction-sequencing-cohesion",
    minutes=24,
    summary="To rebuild a text, use seven clues: the opening sentence, reference words, time markers, linking words, repeated vocabulary, logical order and the closing sentence. Then fill gaps by asking what job the missing word does.",
    objectives=["Explain what text reconstruction asks you to do",
                "Use reference words, time markers and linking words to find the order of sentences",
                "Fill the gaps of a damaged text with words that fit the grammar and the meaning",
                "Write out the reconstructed text in full when the task asks you to"],
    key_concepts=["Text reconstruction", "Cohesion", "Coherence", "Reference", "Discourse marker", "Sequence"],
    blocks=[
        H("Introduction"),
        T("Imagine that a page of your exercise book is torn into strips and the strips fall on the floor. You pick them up and put them in order so that the page makes sense again. That is the idea of **text reconstruction**: Section B of Paper 3, **one compulsory question worth 15 marks**."),
        T("The Board's syllabus says that, in this section, candidates *retell, summarise or build different text types in a proper sequence* and *make inferences and determine sequence*. The Board's report on the 2023 examination described that year's task as a **mutilated text with blank spaces to be filled with appropriate words and expressions**, and a dialogue to be turned into reported speech in prose. The format may change from year to year, so practise several forms. In this lesson we practise the two most useful: ordering sentences and filling gaps."),
        D("**Cohesion** is the set of language links that bind sentences together (reference words, linkers, repeated words). **Coherence** is the sense of the whole: the ideas follow one another logically. A reconstructed text must have both.", title="Definition"),
        TIP("The Board's report says that candidates lost half of the marks for this section when they only listed the correct words instead of copying the passage and filling in the words. Follow the instruction: if the task says to rewrite or complete the text, write the whole text out.", title="Exam link"),
        H("Seven clues for sequencing"),
        KEY("Look for these in every sentence", "", cards=[
            ["1. The opening", "The first sentence introduces the topic with *a/an*, a greeting, a title or a general statement. It cannot begin with *this*, *then* or *he*."],
            ["2. Reference words", "*This, that, these, they, it, he, she, the former, such* point back to something already named."],
            ["3. Time markers", "*First, then, later, since then, afterwards, at last, the next day* show the order of events."],
            ["4. Linking words", "*But, however, so, therefore, for example, in addition, finally* show how the sentence connects to the one before."],
            ["5. Word chains", "The same word or a synonym appears again: *footbridge*, then *the bridge*, then *the new structure*."],
            ["6. Logical order", "General to particular; problem then solution; cause then result; description then opinion."],
            ["7. The ending", "A conclusion, a future plan, a prediction, a thank-you, or a closing formula."]]),
        T("One rule of grammar helps a great deal. A noun is usually introduced with **a/an** the first time and is then called **the** (*a new bridge... the bridge*). If a sentence has *the bridge* and no earlier sentence mentions a bridge, you have found a sentence that must come later."),
        IMG("al-enu1-sequencing-clues.svg", alt="Two sentence boxes joined by arrows: the first introduces 'a new footbridge', the second says 'The bridge' and 'which', showing reference links.", caption="Figure 1. Reference words link a sentence to the one before it."),
        H("Worked example: ordering a news report"),
        T("Put these eight sentences in order. (The text is invented.)"),
        CODE(BR_SHOWN, "text", title="Jumbled sentences"),
        EX("Worked example 1: finding the order", intro="Use the seven clues, one sentence at a time.", steps=[
            S("Find the opening", text="B says *A new footbridge...* It introduces a thing with *a* and tells us when and where. It is the opening."),
            S("Follow the reference", text="F says *The bridge, which is 40 metres long, replaces a wooden one*. *The bridge* refers to the footbridge in B. F comes second."),
            S("Follow the time", text="D says *Since then*. 'Then' means the time of the collapse mentioned in F ('two years ago'). D comes third."),
            S("Look for the next topic", text="G says *The new structure was paid for...*. *New structure* is another name for the bridge. It adds a new idea (money), so it follows."),
            S("Order the ceremony", text="A (*At the opening ceremony*) must come after the bridge has been introduced as 'opened'. H (*Afterwards*) follows the ceremony."),
            S("Choose the ending", text="C reports what the market women said and E ends with the council's future inspection. C gives people's reaction; E is a closing promise."),
            S("Answer", text="B F D G A H C E.")],
              check=r"\text{B F D G A H C E}"),
        MISTAKE("Judging by one clue only", "A time word such as *then* can mislead you. Check at least two clues for each sentence: for example reference *and* logic. Then read the whole text aloud in your head to test whether it flows."),
        H("Worked example 2: filling gaps"),
        T("A gap is not a puzzle of vocabulary only. First decide the **job** of the missing word: is it a connector of contrast, a time word, a quantifier, a reference word? Then choose the word that fits that job and the grammar around it."),
        CODE(GAP_TEXT, "text", title="Text with gaps (invented)"),
        EX("Worked example 2: reasoning for each gap", intro="Fill each gap with one suitable word.", steps=[
            S("Gap 1", text="'(1) ______ traders had arrived early... the buyers came later.' The plural noun needs a quantifier. *Most* (or *Many*) fits."),
            S("Gap 2", text="The two parts are in contrast (traders early, buyers later). *While* or *whereas* shows contrast."),
            S("Gap 3", text="A time clause: 'When the rain began...' *When* or *As soon as*."),
            S("Gap 4", text="'___ of the stalls were destroyed.' *Some* of the stalls (plural verb *were*). *Much* would not fit a plural."),
            S("Gap 5", text="The traders' decision is a result of the damage. *Consequently* (or *As a result* / *Therefore*)."),
            S("Answer", text="1 Most; 2 while; 3 When; 4 some; 5 Consequently. Write out the whole text with the words in place.")]),
        QUIZ("In a jumbled text, which sentence is most likely to be the OPENING?",
             ["However, the council has not yet replied.", "This was a great surprise to the villagers.", "A new school opened in Bamenda last week.", "Therefore, the work was finished on time."],
             2, "It introduces something new (*a new school*) and has no reference back. The others begin with a link or a reference word that needs an earlier sentence.",
             hint="Which sentence needs no sentence before it?",
             feedback=["*However* contrasts with an earlier statement.", "*This* refers to something already mentioned.", "", "*Therefore* gives a result of something earlier."]),
        QUIZ("Which word best fills the gap? 'The road was narrow. (_____), many drivers avoided it.'",
             ["Nevertheless", "Consequently", "Meanwhile", "For instance"],
             1, "The second sentence is a result of the first. *Consequently* shows result. *Nevertheless* shows an unexpected contrast; *meanwhile* shows simultaneous events; *for instance* introduces an example.",
             hint="Is the second sentence a result, a contrast, a time link or an example?",
             feedback=["It would suggest that drivers used the road in spite of it being narrow.", "", "It would suggest that something else was happening at the same time.", "The second sentence is not an example of the first."]),
        H("Practice"),
        PQ("Put these sentences in order.\n\na. As a result, the shop now closes at six.\nb. Last year, thieves broke into the shop twice.\nc. The owner then installed two lights and a strong door.\nd. Mr Ngu runs a small shop near the junction.",
           "D B C A. d introduces Mr Ngu and the shop; b gives the problem (*last year*); c gives the action (*then*); a gives the result (*as a result*)."),
        PQ("Fill the gaps: 'The road was repaired in June. (1) ______ it had been full of holes for years, drivers now drive safely. (2) ______, accidents have fallen.'",
           "(1) Although (or *Even though*) shows contrast between past and present. (2) Consequently, or *As a result* or *Therefore*, shows result."),
        PQ("Why must the sentence 'The council says that it will inspect the bridge every year' come near the end of the news report?",
           "It looks to the future and finishes the story with a promise; it also uses *the council* and *the bridge*, which are already known. Reports often end with a future plan or a conclusion."),
        SUM("Text reconstruction asks you to rebuild a text in proper order, or to complete a damaged text, in a way that makes sense.",
            "Use seven clues: opening, reference words, time markers, linkers, word chains, logical order and ending.",
            "A noun is introduced with a/an and later called the; a sentence with 'the' and no earlier mention comes later.",
            "For a gap, decide the job of the word first (contrast, result, time, quantity), then fit it into the grammar.",
            "When the task says to rewrite or fill in the text, write the whole text out; do not only list the words.")
    ]))


# ================================================================== 6. Reconstructing letters, articles, reports
LESSONS.append(lesson(
    module=M_REC, topic=T_RTYPES,
    title="Reconstructing letters, news articles and reports",
    slug="enu1-reconstruct-letters-articles-reports",
    minutes=24,
    summary="Each written text type has an expected order. A formal letter moves from purpose to reasons to details to request; a news article from the key facts to the details; a report from introduction to findings to conclusion and recommendations.",
    objectives=["State the usual order of parts of a formal letter, a news article and a report",
                "Reconstruct a letter, an article and a report from jumbled paragraphs",
                "Turn notes into continuous text in full sentences",
                "Respect layout rules, including the name and address given in the question"],
    key_concepts=["Text type", "Layout", "Inverted pyramid", "Report sections", "Notes into prose", "Concealed identity"],
    blocks=[
        H("Introduction"),
        T("The syllabus says that Text Reconstruction uses *different text types*. Knowing the usual **shape** of each type is a powerful clue: if you know that a report ends with recommendations, you know where to put the sentence that begins *It is recommended that...*."),
        T("This lesson looks at the three main written types: the **formal letter**, the **news article** and the **report**. The next lesson looks at dialogue, minutes, stories and speeches."),
        KEY("The usual shape of each type", "", cards=[
            ["Formal letter", "Address of the writer, date, address of the receiver, greeting, subject line, body (purpose, reasons, details, request), closing, signature."],
            ["News article", "Headline, then the key facts (who, what, where, when) in the first sentence, then details, background, comments, and a look to the future."],
            ["Report", "Title, introduction (purpose), findings, conclusion, recommendations."]]),
        TIP("Candidates must conceal their identity: use the name and address provided in the question and never your own. If the question gives you a name and an address, use them exactly. Do not use obscene language in any text.", title="Exam rule"),
        H("The formal letter"),
        CODE("""                                   Box 12, Bamenda        <- writer's address (the one given)
                                   20 November 2025       <- date
The Principal,                                            <- receiver's title
Mbeng Secondary School.                                   <- receiver's address

Dear Sir,                                                 <- greeting

                  REQUEST FOR A CLEAN-UP CAMPAIGN         <- subject line

(paragraph 1: the purpose)
(paragraph 2: the reasons)
(paragraph 3: the plan, in detail)
(paragraph 4: what you need)
(paragraph 5: the polite close)

Yours faithfully,                                         <- closing
(Signature)  Name                                         <- the name given""", "text", title="Layout of a formal letter (invented addresses)"),
        T("*Dear Sir* or *Dear Madam* is closed with **Yours faithfully**. A named person (*Dear Mr Ekema*) is closed with **Yours sincerely**. Check your textbook for the layout style your teacher uses; the order of the parts is what matters."),
        H("Worked example 1: the body of a formal letter"),
        T("These five paragraphs of the body of a letter have been mixed up. Put them in order."),
        CODE(LT_SHOWN, "text", title="Jumbled paragraphs"),
        EX("Worked example 1: reasoning", intro="Use the order of a letter: purpose, reasons, plan, request, close.", steps=[
            S("The purpose", text="B: *I am writing to ask permission...* This is the usual first paragraph of a request letter."),
            S("The reasons", text="E: *At present...* gives the problem that justifies the request."),
            S("The plan", text="D: *Firstly... Secondly... Finally...* The sequence markers organise the plan. It must follow the problem."),
            S("The request for help", text="A: *We should be grateful if the school could provide...* The request for the school's help comes after the plan."),
            S("The close", text="C: *I hope that you will approve this request... thank you in advance* is the polite ending. *This request* also refers to the first paragraph."),
            S("Answer", text="B E D A C (" + LT_ANS + ").")]),
        H("The news article"),
        T("A news article is written so that a reader who stops after one sentence still knows the key event. This is sometimes called the **inverted pyramid**: the most important facts come first, and the details follow in order of decreasing importance."),
        CODE(AR_SHOWN, "text", title="Jumbled sentences of an article (headline: Students clean up their school)"),
        EX("Worked example 2: ordering the article", intro="Clues: key facts first; then who organised; then reports and details; then outcome; reaction; future.", steps=[
            S("The lead", text="C says what happened, who did it, where and when, and gives the result: it is the lead (the first sentence)."),
            S("Background", text="F: *The campaign, organised by the Environment Club, began at 8 a.m.* *The campaign* refers back to the cleaning in C."),
            S("A person's words", text="B: *Club president Miss Lum Fonyuy said that...* The club's president is named for the first time here."),
            S("Her work", text="E: *Her team cleared them first and then...* *Her* and *them* (the drains) refer back to B."),
            S("The result", text="G: *By noon the compound was clean...* The time marker follows the sequence of the day."),
            S("Reaction and future", text="A: the principal thanks the volunteers. D: the club plans to repeat the exercise; it looks to the future, so it ends the article."),
            S("Answer", text="C F B E G A D (" + AR_ANS + ").")]),
        H("The report"),
        CODE(RP_SHOWN, "text", title="Jumbled paragraphs of a report (invented)"),
        T("A report has fixed sections. The first one tells the reader the **purpose** (*This report examines...*). The facts come next (*A survey... was carried out*), then the explanation, then the **conclusion** (*It is clear that...*) and the **recommendation** (*It is recommended that...*)."),
        CODE("""Introduction  -> purpose           ("This report examines...")
Findings      -> facts, figures    ("A survey was carried out...")
               -> reasons          ("Students gave three reasons...")
Conclusion    -> what it means     ("It is clear that...")
Recommendation-> what to do        ("It is recommended that...")""", "text", title="Order of a report"),
        T("The correct order of the jumbled report is **D B E A C** (" + RP_ANS + "): introduction (D), survey (B), reasons (E), conclusion (A), recommendation (C)."),
        H("Notes into continuous text"),
        T("Sometimes reconstruction means **building** a text from notes, as the syllabus puts it: *build different text types*. Write full sentences, add small words (articles, prepositions, linkers), put verbs in a consistent tense and keep every fact."),
        CODE(NOTES, "text", title="Notes"),
        EX("Worked example 3: from notes to prose", intro="Write the notes as a short news paragraph.", steps=[
            S("Choose the tense", text="The repair is finished, so the past tense: *was repaired, paid, finished, opened*."),
            S("Join facts with linkers", text="The two payments become one sentence: *The villagers paid 2,000,000 FCFA and the government paid the remaining 5,000,000 FCFA.*"),
            S("Write numbers carefully", text="Keep all figures exactly; *14* may be written as *Fourteen* at the start of a sentence."),
            S("Result", text=NOTES_TEXT)],
              check=r"2\,000\,000 + 5\,000\,000 = 7\,000\,000"),
        MISTAKE("Adding facts that are not in the notes", "When you build a text from notes, you may add linking words but not new facts. Do not invent the name of the Divisional Officer or the day of the opening."),
        QUIZ("Which sentence would be the best LEAD of a news article?",
             ["The principal thanked the volunteers.", "Forty students cleaned the school compound on Saturday and removed sixty sacks of waste.", "The club plans to repeat the exercise.", "She said that the drains had been blocked."],
             1, "A lead gives the key facts: who, what, where, when and the result. The other sentences give a reaction, a plan and a quotation.",
             hint="Which sentence tells the whole story in one go?",
             feedback=["A reaction usually comes later.", "", "A future plan comes at the end.", "*She* has no earlier mention."]),
        QUIZ("In a formal letter, which paragraph comes immediately after the greeting and subject line?",
             ["The request for help", "The purpose of the letter", "The polite close", "The reasons"],
             1, "State the purpose first, so the reader knows at once why you are writing.",
             hint="What must the reader know first?",
             feedback=["The request usually follows the reasons and the plan.", "", "The close comes last.", "The reasons support the purpose, so they follow it."]),
        PQ("Put these report sentences in order.\n\na. It is recommended that the council should repair the road before the rains.\nb. This report examines the condition of the road to Nkwen.\nc. The road has 14 holes in 3 kilometres.\nd. It is clear that the road is unsafe.",
           "B C D A: introduction (purpose), finding, conclusion, recommendation."),
        PQ("Write the notes as one sentence of continuous text: 'Market, Saturday, 200 traders, rain, 3 stalls destroyed.'",
           "On Saturday, 200 traders were at the market when rain destroyed three stalls. (Keep the numbers exact and add no new facts.)"),
        PQ("A question says: 'Your name is Ayuk Bih, of Box 45, Bamenda. Write a formal letter.' A candidate signs with his own real name. What is wrong?",
           "Candidates must conceal their identity and use the name and address provided. The letter should be signed with the name given, Ayuk Bih, and use the given address."),
        SUM("Each text type has a usual order: knowing it gives you clues for sequencing.",
            "Formal letter: purpose, reasons, plan, request, close; end with Yours faithfully or Yours sincerely as the greeting requires.",
            "News article: the lead gives the key facts; details, quotations and results follow; the ending looks ahead.",
            "Report: introduction, findings, conclusion, recommendations.",
            "When you build text from notes, use full sentences and one tense, keep all facts and add none.")
    ]))


# ================================================================== 7. Reconstructing dialogue, minutes, stories, speeches
LESSONS.append(lesson(
    module=M_REC, topic=T_RTYPES,
    title="Reconstructing dialogues, minutes, stories and speeches",
    slug="enu1-reconstruct-dialogue-minutes-stories-speeches",
    minutes=25,
    summary="Turn a dialogue into reported speech in prose with correct backshift, turn notes into minutes in the past tense and reported speech, and order the sentences of a story and a speech by their sequence signals.",
    objectives=["Turn a dialogue into continuous reported speech, with the correct tense and pronouns",
                "Write minutes from notes in the conventional style",
                "Order the sentences of a story by time and event signals",
                "Order the parts of a speech: greeting, theme, body, call to action, thanks"],
    key_concepts=["Reported speech", "Backshift", "Reporting verb", "Minutes", "Narrative sequence", "Speech structure"],
    blocks=[
        H("Introduction"),
        T("In the previous lesson you rebuilt letters, articles and reports. Here we deal with the four types that most often cause trouble: the **dialogue** (turned into reported speech), **minutes**, **stories** and **speeches**. The Board's report on the 2023 examination described a task in which candidates turned a dialogue between two speakers into reported speech in prose, mostly in the simple present tense. Candidates did well when they followed instructions, used the right tense, gave the right option in reporting and spelt correctly."),
        TIP("When the task asks you to rewrite a dialogue as a report, write a **continuous prose passage**. The Board's report says that candidates lost marks when they listed words or used point form instead of writing out the passage.", title="Exam link"),
        H("Dialogue into reported speech"),
        D("In **reported (indirect) speech** we give the meaning of what was said, not the exact words. There are no quotation marks. The reporting verb (*said, asked, replied, promised*) introduces the report.", title="Definition"),
        KEY("Changes when the reporting verb is in the past", "Say in prose what was said, and change these things.", cards=[
            ["Tense (backshift)", "am/is becomes was; have becomes had; want becomes wanted; will becomes would; can becomes could."],
            ["Pronouns", "I becomes he or she; you becomes I, he or she; we becomes they."],
            ["Time words", "now becomes then; today becomes that day; tomorrow becomes the next day; next month becomes the following month."],
            ["Questions", "Do you have...? becomes asked whether (or if) she had...; no question mark, normal word order."]]),
        T("When the reporting verb is in the **present tense** (*says, asks*), there is usually no backshift: *Bih says that she wants...*. Follow the tense in the instruction."),
        CODE(DIALOGUE, "text", title="A dialogue (invented)"),
        EX("Worked example 1: the report in the past tense", intro="Turn the dialogue into a passage of reported speech. Begin: 'Bih said that...'.", steps=[
            S("Line 1", text="'I want to start a poultry farm.' becomes *Bih said that she wanted to start a poultry farm.* (I to she; want to wanted)."),
            S("Line 2", text="'Do you have enough money?' becomes *Tanyi asked whether she had enough money.* (a question: whether, normal order)."),
            S("Line 3", text="*Bih replied that she had 200,000 FCFA but needed 100,000 more.* (have to had; need to needed; figures unchanged)."),
            S("Line 4", text="*Tanyi said that he lent money to friends at no interest and could give her the rest the following month.* (can to could; next month to the following month)."),
            S("Line 5", text="*Bih thanked him and promised to repay him after the first sale.* 'Thank you' becomes *thanked him*. Use a verb for the act."),
            S("Full report", text=REPORT_PAST + " (" + str(wc(REPORT_PAST)) + " words)")]),
        EX("Worked example 2: the same report in the present tense", intro="If the instruction says to use the simple present tense, there is no backshift.", steps=[
            S("Rule", text="Reporting verbs are *says, asks, replies, thanks, promises*. The verbs inside the report stay in the present tense."),
            S("Report", text=REPORT_PRES + " (" + str(wc(REPORT_PRES)) + " words)"),
            S("Check", text="Pronouns still change (I to she, you to her). *Next month* stays *next month* because the time has not moved.")]),
        MISTAKE("Half-reported speech", "Do not mix direct and reported speech. 'Bih said that I want to start a poultry farm' keeps the speaker's pronoun and tense and is wrong. Change the pronouns and the tense together, and follow the tense given in the instruction."),
        H("Minutes from notes"),
        T("**Minutes** are the official record of a meeting. They are written in the **past tense**, in the **third person**, mostly in **reported speech** (*The Chairperson proposed that...*), with decisions in the passive (*It was agreed that...*). Future actions use *will*. They keep a fixed order: heading with date, time and place, persons present, then the items in order, and the time the meeting ended."),
        CODE(MIN_NOTES, "text", title="Notes (invented)"),
        EX("Worked example 3: minutes", intro="Write the minutes of the meeting from the notes.", steps=[
            S("Heading", text="*Minutes of the meeting of the Parents' Association held on 8 March at 3 p.m. in the school hall.*"),
            S("Attendance", text="*Present: Mrs Njong (Chairperson) and 42 parents.*"),
            S("Item 1", text="Reported speech and a decision: *The Chairperson proposed an increase... The parents rejected this, and it was agreed to raise the fees by 1,000 FCFA.*"),
            S("Item 2", text="*It was reported that the roof of Block B would cost 1,500,000 FCFA. It was agreed to hold a fundraising match on 22 March.* (A report in the past with *would*.)"),
            S("Close", text="*The meeting ended at 4.30 p.m.*"),
            S("Full text", text=MIN_TEXT)]),
        H("A story: sequence signals"),
        CODE(ST_SHOWN, "text", title="Jumbled story (invented)"),
        EX("Worked example 4: ordering the story", intro="Stories follow time: opening situation, development, complication, resolution, ending.", steps=[
            S("Opening", text="B: *It was market day in Bafut...* sets the scene (place, person, time)."),
            S("Development", text="F: *By midday...* follows dawn. D: *Suddenly she noticed...* is the complication."),
            S("Search", text="G: *She searched...* is her reaction to the loss."),
            S("Resolution", text="A: *Then a small boy ran up...* solves the problem. E: *Nkeng thanked him...* is her reaction."),
            S("Ending", text="C: *That evening...* closes the story."),
            S("Answer", text="B F D G A E C (" + ST_ANS + ").")]),
        H("A speech: its parts"),
        CODE(SP_SHOWN, "text", title="Jumbled sentences of a speech (invented)"),
        T("A speech has recognisable parts: **greeting**, **theme** (what the speaker will talk about), **body** with reasons and facts, **call to action**, **thanks**. The correct order is " + SP_ANS + ": D (greeting), B (theme), E (the fact that supports the theme), A (the call to action) and C (thanks)."),
        QUIZ("Which is the correct report of: Ayuk said to Neba, \"I will visit you tomorrow.\"?",
             ["Ayuk told Neba that he will visit him tomorrow.", "Ayuk told Neba that he would visit him the next day.", "Ayuk told Neba that I would visit you the next day.", "Ayuk told Neba that Neba would visit him the next day."],
             1, "The reporting verb is in the past, so will becomes would and tomorrow becomes the next day. I becomes he (Ayuk) and you becomes him (Neba).",
             hint="Check the tense, the time word and both pronouns.",
             feedback=["There is no backshift and *tomorrow* is kept; after the past reporting verb *told*, will should become would.", "", "The pronouns I and you have not been changed.", "The pronouns are reversed: Ayuk, not Neba, will visit."]),
        QUIZ("In the minutes of a meeting, which sentence is in the correct style?",
             ["The Chairperson says that the fence is broken.", "It was agreed that the fence would be repaired.", "We agree that we shall repair the fence.", "I think the fence must be repaired quickly."],
             1, "Minutes use the past tense, the third person and the passive for decisions.",
             hint="Past tense, third person, formal.",
             feedback=["Present tense is not used for a finished meeting.", "", "First person plural and present tense do not suit minutes.", "Minutes do not record the writer's own opinion."]),
        PQ("Report in the past tense: Neba said to Tabe, \"I am tired, but I can finish the work tomorrow.\"",
           "Neba told Tabe that he was tired but could finish the work the next day. (am to was; can to could; tomorrow to the next day; I to he. Another correct answer: *Neba said to Tabe that...*)"),
        PQ("Put the sentences of the speech in order.\n\na. I therefore ask you to bring your own bags to the market.\nb. Good afternoon, everyone.\nc. Thank you very much.\nd. I wish to speak about plastic waste in our market.\ne. Plastic bags blocked the drains twelve times last year.",
           "B D E A C. Greeting, theme, a supporting fact, the call to action, thanks."),
        PQ("Rewrite as the opening of minutes: 'Mr Fon said the meeting is open. We agree to meet again on 5 July.'",
           "Mr Fon opened the meeting. It was agreed that the next meeting would be held on 5 July. (Minutes use the past tense and the passive for agreements.)"),
        SUM("Reported speech has no quotation marks; after a past reporting verb, backshift the tense and change pronouns and time words.",
            "Questions become whether/if clauses with normal word order. In a present-tense report, no backshift.",
            "Write the dialogue as continuous prose; do not list or use point form.",
            "Minutes: past tense, third person, reported speech, decisions as 'It was agreed that...'; fixed order of heading, attendance and items.",
            "Stories follow the order of events; speeches follow greeting, theme, body, call to action and thanks.")
    ]))


# ================================================================== 8. Editing: grammar errors
LESSONS.append(lesson(
    module=M_EDIT, topic=T_CORRECT,
    title="Editing for grammar: tense, agreement, articles, prepositions",
    slug="enu1-editing-grammar-errors",
    minutes=24,
    summary="Edit a text sentence by sentence with a fixed checklist: verb tense, subject-verb agreement, nouns that have no plural, articles, prepositions and pronouns. Change only what is wrong and keep the meaning.",
    objectives=["Use a checklist to find grammar errors in a text",
                "Correct errors of tense, agreement, countable and uncountable nouns, prepositions and repeated pronouns",
                "Make minimal corrections that keep the meaning",
                "Avoid changing words that are already correct"],
    key_concepts=["Editing", "Checklist", "Tense consistency", "Subject-verb agreement", "Uncountable noun", "Resumptive pronoun"],
    blocks=[
        H("Introduction"),
        T("An editor reads a text and repairs it before it is published. Section C of Paper 3, **Editing**, is **one compulsory question worth 15 marks**. The Board's syllabus says that candidates should *correct, condense, organise or modify given material to produce correct, consistent, accurate and complete work*, and that grammar is taught as *a resource in shaping accurate and effective communication*."),
        T("The exact form of the editing task may vary from year to year (for example finding and correcting errors, condensing, reorganising, or identifying features of a text), so this course covers each. In this lesson and the next, we work on **correcting errors**."),
        D("**Editing** is reading a text carefully and making the changes that make it correct, clear, consistent and complete, without changing what the writer means.", title="Definition"),
        TIP("The syllabus table gives Section C about 45 minutes. Do not rush: reading a text twice is better than correcting half the errors in one fast pass. Write corrections legibly and, when asked to rewrite the text, copy every sentence, including those with no error.", title="Exam link"),
        H("The grammar checklist"),
        KEY("Six checks for every sentence", "Read one sentence at a time and ask:", cards=[
            ["1. Tense", "Does the verb match the time of the text? Is the tense consistent?"],
            ["2. Agreement", "Does the verb agree with its real subject (*Each of the students* is singular)?"],
            ["3. Nouns", "Is the noun countable? *information, advice, furniture, luggage, news, equipment* have no plural."],
            ["4. Articles and determiners", "*a, an, the* or none? *much/many, few/little*"],
            ["5. Prepositions", "*returned home* (no *at*), *discussed it* (no *about*), *arrived at/in*, *reply to*."],
            ["6. Pronouns", "Is any pronoun repeated or unclear? *a visit we will never forget it* repeats the object."]]),
        CODE("""Error                          Correction                  Rule
--------------------------------------------------------------------------
our class go on a visit        our class went              past tense
we arrive at nine              we arrived                  past tense
many informations              a lot of information        no plural
each of the students were      each of the students was    each = singular
returned at home               returned home               no preposition
discussed about it             discussed it                no preposition
a visit we will never forget it a visit we would never forget   backshift; no repeated 'it'""", "text", title="Typical errors and their corrections"),
        T("Some of these forms are common in everyday speech in many places, but written examinations ask for **standard written English**. Where books and teachers differ on a small point, check your textbook."),
        H("Worked example: a full passage"),
        CODE(E1_ERR, "text", title="Text with errors (invented)"),
        EX("Worked example 1: the eight corrections", intro="Edit the passage. There are eight errors.", steps=[
            S("Sentence 1", text="*go* should be *went*. The text tells of last Saturday, so it uses the past tense."),
            S("Sentence 2", text="*arrive* should be *arrived*: it is joined by *and* to *left*."),
            S("Sentence 3", text="*explain* should be *explained*: it is joined by *and* to *welcomed*."),
            S("Sentence 4", text="*many informations* should be *a lot of information* (or *much information*). *Information* has no plural."),
            S("Sentence 5", text="*Each of the students were* should be *was*. The subject is *each*, which is singular."),
            S("Sentence 6", text="*returned at home* should be *returned home*. *Home* is an adverb here, so no preposition."),
            S("Sentence 7", text="*we will never forget it* has two errors: *will* should be *would* (the reporting verb *said* is in the past) and the final *it* is repeated: *a visit we would never forget*."),
            S("Corrected text", text=E1_FIX)]),
        MISTAKE("Correcting only the first errors", "Eight errors in a short text means about one per sentence. Check each sentence for every item on the checklist, even when you have already corrected one error in it. Sentence 7 has two errors."),
        MISTAKE("Changing words that are correct", "Do not rewrite sentences that are right. In the passage, *the water was cleaned* is correct. Changing it may introduce a new error and shows that you did not understand the task."),
        H("A second look at agreement and tense"),
        T("Two classes of error deserve special attention."),
        KEY("Agreement traps", "", cards=[
            ["Subject far from the verb", "*The cost of the new desks are high* is wrong: the subject is *cost*, so *is*."],
            ["Each, every, neither, either, none", "*Each of the girls has her book.* They are followed by a singular verb in careful writing."],
            ["Collective nouns", "*The committee has decided* (as one body); check your textbook for the plural use."],
            ["Quantity expressions", "*A number of students are late*; *the number of students is large*."]]),
        KEY("Tense traps", "", cards=[
            ["Past story", "Keep the whole narrative in the past: *went, saw, said*."],
            ["Reported speech", "After a past reporting verb, backshift: *said that he would come*."],
            ["Time clues", "*Last week, yesterday, in 2020* need a past tense; *since 2020* needs the present perfect."],
            ["General truths", "Use the present tense: *Water boils at 100 degrees Celsius.*"]]),
        QUIZ("Which sentence has NO error?",
             ["The children has finished their lunch.", "She gave me many advices.", "Each of the boys was given a prize.", "We discussed about the problem."],
             2, "*Each* takes a singular verb: *was*.",
             hint="Check agreement, plural nouns and prepositions.",
             feedback=["*Children* is plural: *have* finished.", "*Advice* is uncountable: *a lot of advice*.", "", "*Discuss* takes a direct object: *discussed the problem*."]),
        QUIZ("Edit: 'Yesterday, the driver stop the bus and ask us to get out.'",
             ["Yesterday, the driver stopped the bus and asked us to get out.", "Yesterday, the driver stops the bus and asks us to get out.", "Yesterday, the driver has stopped the bus and asking us to get out.", "Yesterday, the driver stop the bus and asked us to get out."],
             0, "*Yesterday* needs the past tense and both verbs must agree in tense.",
             hint="Look at the time word.",
             feedback=["", "Present tense does not match *yesterday*.", "The tenses are mixed and *asking* is not a finite verb.", "The first verb is still wrong."]),
        PQ("Edit: 'The informations that the teacher give us was very useful.'",
           "The information that the teacher gave us was very useful. (informations to information; give to gave; the verb *was* agrees with *information*.)"),
        PQ("Edit: 'My uncle returned back at home after he was discussing about the farm.'",
           "My uncle returned home after he had discussed the farm. (returned back at home: *back* and *at* are not needed; was discussing about: the earlier action needs the past perfect and *discuss* takes no *about*.)"),
        PQ("Find and correct the errors: 'Each of the girls have finish their homework, and the teacher were pleased.'",
           "Each of the girls has finished her homework (or *their* in informal usage), and the teacher was pleased. (have to has; finish to finished; were to was.)"),
        SUM("Editing means correcting a text so that it is accurate, consistent and complete, without changing the meaning.",
            "Use six checks on every sentence: tense, agreement, nouns, articles, prepositions, pronouns.",
            "Some nouns have no plural: information, advice, furniture, luggage, equipment, news.",
            "Do not change what is right; a sentence may have more than one error.",
            "When asked to rewrite, copy the whole text with the corrections.")
    ]))


# ================================================================== 9. Editing: punctuation, spelling, word choice
LESSONS.append(lesson(
    module=M_EDIT, topic=T_CORRECT,
    title="Editing for punctuation, spelling and word choice",
    slug="enu1-editing-punctuation-spelling-words",
    minutes=24,
    summary="After grammar, edit the surface of a text: comma splices and fragments, apostrophes, spelling of common words, confused words such as principal and principle, double comparatives and extra words, and a formal register.",
    objectives=["Repair comma splices and sentence fragments in three ways",
                "Use the apostrophe correctly for contractions and possession",
                "Spot confused words and common misspellings",
                "Remove double comparatives, redundant words and informal phrases"],
    key_concepts=["Comma splice", "Fragment", "Apostrophe", "Confused words", "Double comparative", "Register"],
    blocks=[
        H("Introduction"),
        T("A text can have perfect grammar and still be hard to read if it has no clear sentence boundaries, wrong spellings or the wrong word. In the previous lesson you edited grammar. Now you edit **punctuation, spelling and word choice**."),
        T("The syllabus asks for work that is *correct, consistent, accurate and complete*, and the Board's report on the 2023 examination mentions spelling and legible writing as reasons why candidates did well or badly in Paper 3. These errors cost marks in every section of Paper 3."),
        TIP("Take care of your handwriting when you edit. If your correction cannot be read, it cannot be credited. Write the corrected word clearly above or in place of the wrong one, as the question instructs.", title="Exam link"),
        H("Sentence boundaries"),
        D("A **comma splice** joins two complete sentences with only a comma: *The hall was cheap, we booked it.* A **fragment** is a group of words punched out as a sentence which is not complete: *Because the hall was cheap.*", title="Definitions"),
        KEY("Three ways to mend a comma splice", "Use the one that fits the meaning.", cards=[
            ["1. Full stop", "The hall was cheap. We booked it."],
            ["2. Semicolon", "The hall was cheap; we booked it."],
            ["3. Conjunction", "The hall was cheap, so we booked it."]]),
        T("A fragment is repaired by **joining** it to the sentence it belongs to, or by completing it. In the text below, *Because the hall is cheaper to prepare than the field* depends on the sentence before it, so it is joined to it."),
        H("Apostrophes and confused words"),
        KEY("Apostrophe rules", "", cards=[
            ["Contraction", "An apostrophe replaces missing letters: *don't* (do not), *it's* (it is or it has), *they're* (they are)."],
            ["Possession (singular)", "*the principal's office*; *Ayuk's book*."],
            ["Possession (plural)", "*the students' books*; *children's* (irregular plural)."],
            ["No apostrophe", "Plurals never take one: *two buses*; *its* (belonging to it) has none."]]),
        CODE("""principal  = head of a school (also: main)       principle = a rule or belief
affect     = verb: to influence                  effect    = noun: a result
their      = belonging to them                   there     = place / 'there is'     they're = they are
its        = belonging to it                     it's      = it is / it has
advice     = noun                                advise    = verb
practice   = noun (British)                      practise  = verb (British; check your textbook)
lose       = to misplace                         loose     = not tight
quite      = fairly                              quiet     = silent""", "text", title="Words often confused"),
        T("Commonly misspelt words in student writing include: *forecast, receive, separate, definitely, necessary, government, environment, accommodation, committee, occurrence, February, beginning*. Keep a list of your own mistakes and learn it."),
        H("Word choice"),
        KEY("Common word-choice errors", "", cards=[
            ["Double comparatives", "*more cheaper* should be *cheaper*; *more better* should be *better*."],
            ["Extra prepositions", "*discuss about*, *enter into the room*, *return back*."],
            ["Redundancy", "*repeat again*, *free gift*, *close proximity* say the same thing twice."],
            ["Informal language", "*u, 2, gonna, wanna, kids, guys, lots of* may be wrong in a formal text; use *you, to, going to, children*."]]),
        H("Worked example"),
        CODE(E2_ERR, "text", title="Text with errors (invented)"),
        EX("Worked example 1: eight corrections", intro="Edit the text. Note: not every underlined-looking word is wrong.", steps=[
            S("principle", text="*principle* (a rule) should be *principal* (the head of the school)."),
            S("First comma splice", text="'...on Friday, all students must wear...' has two sentences joined by a comma. Use a semicolon (or a full stop)."),
            S("dont", text="Missing apostrophe: *don't*."),
            S("forcast", text="Spelling: *forecast*."),
            S("discussed about", text="*discuss* takes no preposition: *discussed moving it indoors*."),
            S("The fragment", text="'Because the hall is more cheaper...' is not a sentence. Join it to the sentence before it, with a comma."),
            S("more cheaper", text="Double comparative: *cheaper*."),
            S("Second comma splice", text="'Parents are welcome, the entrance is free.' Use a semicolon."),
            S("A word that is correct", text="*affect* (to influence) is correct: rain may *influence* the match. Do not change it to *effect*."),
            S("Corrected text", text=E2_FIX)]),
        MISTAKE("Over-correcting", "In the text, *affect* is correct and *there will be* is correct (*there* is the place word). If you change right words to wrong ones, you lose marks. Check the meaning before you change a word."),
        MISTAKE("Mending a comma splice with another comma", "Adding more commas does not repair a sentence boundary. Choose a full stop, a semicolon or a conjunction."),
        QUIZ("Which sentence is correctly punctuated?",
             ["The students' books are on the table.", "The student's books are on the table (there are many students).", "The students book's are on the table.", "The students books are on the table."],
             0, "For a plural noun ending in s, the apostrophe comes after the s: *students'*.",
             hint="Whose books? Many students.",
             feedback=["", "This puts the apostrophe before the s, meaning one student, which conflicts with the bracket.", "The apostrophe is in the wrong word: *books* is a plain plural.", "The possessive apostrophe is missing."]),
        QUIZ("Choose the correct word: 'The new rule will ______ all students.'",
             ["effect", "affect", "affects", "effects"],
             1, "*Affect* is the verb meaning to influence. After *will* the verb is in the base form.",
             hint="You need a verb after *will*.",
             feedback=["*Effect* is usually a noun (a result).", "", "After *will* the verb has no -s.", "*Effects* is the plural noun."]),
        PQ("Correct the comma splice in three ways: 'The road was flooded, we stayed at home.'",
           "The road was flooded. We stayed at home. / The road was flooded; we stayed at home. / The road was flooded, so we stayed at home."),
        PQ("Edit: 'The principle said that the childrens books was more better than last years.'",
           "The principal said that the children's books were better than last year's. (principle to principal; childrens to children's; was to were; more better to better; years to year's.)"),
        PQ("Edit and explain: 'We will repeat the exercise again, it will be a great succes.'",
           "We will repeat the exercise; it will be a great success. (*Repeat again* repeats the idea of again; comma splice repaired with a semicolon; *success* has two c's and two s's.) Another correct answer keeps *again* and removes *repeat*: We will do the exercise again; it will be a great success."),
        SUM("Check sentence boundaries: repair comma splices and fragments.",
            "Use the apostrophe for contractions and possession, never for ordinary plurals.",
            "Learn the pairs: principal and principle, affect and effect, its and it's, their and there.",
            "Remove double comparatives and needless words; keep the register formal.",
            "Do not change correct words, and write your corrections clearly.")
    ]))


# ================================================================== 10. Condensing and reorganising
LESSONS.append(lesson(
    module=M_EDIT, topic=T_CONDENSE,
    title="Condensing and reorganising a text",
    slug="enu1-editing-condense-reorganise",
    minutes=23,
    summary="To condense, delete empty phrases and repetition, replace phrases by single words and merge sentences, keeping every main point. To reorganise, group ideas by theme, put them in a logical order and give each group a paragraph.",
    objectives=["Condense a wordy text to a stated length without losing main points",
                "Replace wordy phrases by single words",
                "Group mixed ideas by theme and arrange them in paragraphs",
                "Check that the edited text keeps the original meaning"],
    key_concepts=["Condensing", "Wordiness", "Redundancy", "Reorganising", "Grouping by theme", "Paragraph"],
    blocks=[
        H("Introduction"),
        T("Sometimes a text says too much, or says things in the wrong order. The Board's syllabus lists, as objectives of Section C, that you can *condense, organise or modify* given material and *sort out and sift appropriate material*. **Condensing** shortens a text but keeps its message. **Reorganising** keeps the content but changes the order and grouping."),
        D("To **condense** a text is to make it shorter by removing words and details that do not carry the message, while keeping every main idea. To **reorganise** is to rearrange the ideas into a clearer order and paragraphs.", title="Definitions"),
        TIP("Condensing is close to summary writing, but in editing you usually keep the writer's voice and point of view and the order of ideas. Read the task: it may give a word limit, a number of paragraphs, or a purpose (for example, for a notice board).", title="Exam link"),
        H("Condensing"),
        KEY("Five ways to cut", "", cards=[
            ["1. Empty openings", "*It is a fact that*, *it is my opinion that*, *in the present day and age* usually add nothing."],
            ["2. Wordy phrases", "*a great deal of* becomes *much*; *in spite of the fact that* becomes *although*; *as a result of this* becomes *so*."],
            ["3. Repetition", "*very common habit* said twice; *every single day* becomes *daily*."],
            ["4. Merge sentences", "Join sentences that share a subject."],
            ["5. Cut small details", "Keep the main points and the figures that matter."]]),
        CODE("""in the present day and age   ->  today
a very large number of       ->  many
a great deal of              ->  much
every single day             ->  daily
in addition to this          ->  also
as a result of this          ->  so / therefore
it is my opinion that        ->  (delete) I think / I believe""", "text", title="Wordy phrases and their short forms"),
        CODE(E3_LONG + "\n\n(" + str(wc(E3_LONG)) + " words)", "text", title="A wordy text (invented)"),
        EX("Worked example 1: condense to not more than 45 words", intro="Condense the text, keeping all the main points.", steps=[
            S("Find the main points", text="(1) Students spend too much time on their phones. (2) They stay awake late and are tired in class. (3) Teachers complain about attention and marks have fallen. (4) Suggested rule: phones handed in at the start of each day."),
            S("Cut", text="Delete *It is a fact that*, *in the present day and age*, *a very large number of*, *This is a habit that has become very common* (repetition) and *It is therefore my opinion that*."),
            S("Merge", text="Join the effects with *so*: tired and inattentive; marks fallen."),
            S("Result", text=E3_SHORT + " (" + str(wc(E3_SHORT)) + " words)"),
            S("Check", text="All four points are present, the meaning is unchanged, and the limit of 45 is respected.")]),
        MISTAKE("Cutting the main point", "A short text is not better if it has lost the proposal. In this text the final recommendation (the phone rule) is the main point and must stay."),
        H("Reorganising"),
        T("A text can have good sentences in a poor order. A reader who finds advantages, then disadvantages, then more advantages is confused. Reorganise by **grouping the ideas by theme** and giving each theme a paragraph, with a topic sentence."),
        CODE(E4_MIX, "text", title="A mixed text (invented)"),
        EX("Worked example 2: reorganising into two paragraphs", intro="Sort the sentences into advantages and disadvantages.", steps=[
            S("Label each sentence", text="cheap: advantage. dangerous (helmets): disadvantage. narrow streets: advantage. accidents: disadvantage. jobs: advantage. traffic lights: disadvantage."),
            S("Group", text="Paragraph 1: cheap, narrow streets, jobs. Paragraph 2: helmets, traffic lights, accidents."),
            S("Add a topic sentence and a link", text="Paragraph 1 begins *have clear advantages*; paragraph 2 begins *However, they are also dangerous*."),
            S("Join sentences", text="Use lists of three joined by commas and *and*; keep all the facts."),
            S("Result", text=E4_ORG)]),
        MISTAKE("Changing the meaning when reorganising", "You may move and join sentences, but not add new facts, drop facts or change the strength of a statement (*seldom*, *some*, *many*). Count the facts before and after."),
        QUIZ("Which phrase can be replaced by the single word *although*?",
             ["as a result of this", "in spite of the fact that", "in addition to this", "a great deal of"],
             1, "*In spite of the fact that* introduces a contrast, like *although*.",
             hint="Which phrase shows contrast?",
             feedback=["That phrase means *so*.", "", "That phrase means *also*.", "That phrase means *much*."]),
        QUIZ("A text mixes sentences about the benefits and the problems of a new market. What is the best way to reorganise it?",
             ["Put the longest sentences first", "Group the benefits in one paragraph and the problems in another", "Delete the problems", "Put each sentence in its own paragraph"],
             1, "Group ideas by theme so that each paragraph has one idea.",
             hint="Which way makes the text clearer without losing content?",
             feedback=["Length is not a logical order.", "", "Deleting facts changes the meaning.", "One-sentence paragraphs break the unity of each idea."]),
        PQ("Condense in not more than 12 words: 'It is a fact that, in the present day and age, a great deal of people use the internet every single day.'",
           "Today, many people use the internet daily. (7 words.) *A great deal of people* is also an error: *a great many people* or *many people*."),
        PQ("Replace the wordy phrase: 'In spite of the fact that it was raining, the match was played.'",
           "Although it was raining, the match was played."),
        PQ("Reorganise into two paragraphs (reasons for, reasons against): 'The fee is low. Parking is difficult. The centre is near. There is little shade.'",
           "Paragraph 1 (for): The fee is low and the centre is near. Paragraph 2 (against): However, parking is difficult and there is little shade. (All four facts kept.)"),
        SUM("Condense by deleting empty openings, wordy phrases, repetition and small details; merge sentences.",
            "Keep every main idea, the key figures and the original meaning.",
            "Reorganise by grouping ideas by theme, one theme per paragraph, with topic sentences and links.",
            "Do not add or drop facts and do not change the strength of statements.",
            "Always check the stated word limit.")
    ]))


# ================================================================== 11. Text structures and language features
LESSONS.append(lesson(
    module=M_EDIT, topic=T_STRUCT,
    title="Text structures and language features: informative, persuasive, imaginative",
    slug="enu1-text-structures-language-features",
    minutes=24,
    summary="Informative texts state facts in the present tense with technical words; persuasive texts address the reader with questions, commands and repetition; imaginative texts use imagery and the senses. Identify the feature, then explain its effect.",
    objectives=["Tell informative, persuasive and imaginative texts apart",
                "Name the main language features of each type",
                "Explain the effect of a feature, not only name it",
                "Keep the features of the type when you edit or modify a text"],
    key_concepts=["Informative text", "Persuasive text", "Imaginative text", "Language feature", "Effect", "Audience and purpose"],
    blocks=[
        H("Introduction"),
        T("The syllabus says that, in Section C, candidates should *identify and explain text structures and language features used in different texts like informative, persuasive and imaginative texts*. Two verbs matter: **identify** (name the feature) and **explain** (say what it does)."),
        D("A **text structure** is how a text is organised (headline, paragraphs, sections). A **language feature** is a choice of words or grammar that serves the writer's purpose (for example a question, a command, a simile, a technical term).", title="Definitions"),
        TIP("When asked to explain a feature, use the pattern: the feature, a short quotation or reference, the effect on the reader. Example: 'The question *Do you want your children to sleep safely tonight?* involves the reader and makes them think about their own family.'", title="Exam link"),
        KEY("Three kinds of text", "Purpose decides the features.", cards=[
            ["Informative", "Purpose: to tell facts. Features: present tense, facts and figures, technical words, neutral tone, headings, logical order."],
            ["Persuasive", "Purpose: to make the reader act or agree. Features: questions, commands, *you* and *we*, repetition, emotive words, lists of three."],
            ["Imaginative", "Purpose: to create a picture or a story. Features: imagery, similes and metaphors, the five senses, varied sentences, usually the past tense."]]),
        H("An informative text"),
        CODE(F_INF + "\n\n(an invented description)", "text", title="Text A"),
        EX("Worked example 1: features of Text A", intro="Identify and explain three features.", steps=[
            S("Present tense", text="*lie, makes, grow, is*: the text states facts that are generally true, which suits a text that informs."),
            S("Figures", text="*between 1,000 and 2,000 metres* is exact information that the reader can trust."),
            S("Cause and effect structure", text="*Their height... makes the climate cooler* and *For this reason* link cause and result and organise the facts in a logical order."),
            S("Tone", text="There are no opinions or emotions: the neutral tone presents the writer as reliable.")]),
        H("A persuasive text"),
        CODE(F_PER, "text", title="Text B"),
        EX("Worked example 2: features of Text B", intro="Identify and explain four features.", steps=[
            S("Rhetorical question", text="*Do you want your children to sleep safely tonight?* The question draws the reader in and expects the answer yes."),
            S("Short sentences", text="*Of course you do. Then join us.* The short sentences add pressure and show confidence."),
            S("Imperative", text="*join us* is a command that gives the reader something to do."),
            S("List of three", text="*a torch, a whistle and a brave heart* gives a rhythm and makes the effort sound small."),
            S("Inclusive pronoun", text="*Together we can* brings the reader into the group.")]),
        H("An imaginative text"),
        CODE(F_IMG, "text", title="Text C"),
        EX("Worked example 3: features of Text C", intro="Identify and explain three features.", steps=[
            S("Simile", text="*like a dry hand*: compares the wind to a hand; it gives a touch image of dryness and makes the wind seem alive."),
            S("Metaphor", text="*a pale coin*: the sun is described as a coin without saying *like*; the colour and flatness are pictured."),
            S("Sensory and personification detail", text="*wiping the colour from the hills* shows the effect of the wind and gives the wind a human action.")]),
        MISTAKE("Naming without explaining", "Writing 'the writer uses a simile' earns little. Always add the effect: what picture, feeling or action the feature creates in the reader."),
        MISTAKE("Using the wrong features in your own text", "If you are asked to edit or write a persuasive text, do not make it a list of cold facts; if you are asked for an informative text, do not fill it with exclamations and opinions."),
        H("Structure and features in other text types"),
        CODE("""News article    headline, lead, details, quotations; past tense; third person
Report          headings, numbered findings; formal; passive voice
Letter          address, greeting, closing; tone suits the reader
Speech          greeting, theme, appeals to the audience, thanks
Story           opening, problem, climax, ending; dialogue; past tense""", "text", title="Structure and features at a glance"),
        QUIZ("Which feature is typical of a persuasive text?",
             ["A neutral tone with technical terms", "Commands and questions addressed to the reader", "A long description of scenery with similes", "Passive voice and numbered findings"],
             1, "Persuasive texts speak to the reader with questions and commands. The other options describe informative, imaginative and report-style writing.",
             hint="Think of an advertisement.",
             feedback=["That is informative.", "", "That is imaginative.", "That is report style."]),
        QUIZ("'The sun, a pale coin, rolled slowly over the roofs.' The phrase 'a pale coin' is",
             ["a simile", "a metaphor", "a rhetorical question", "a command"],
             1, "A metaphor says one thing *is* another without *like* or *as*.",
             hint="Is there a word like *like* or *as*?",
             feedback=["A simile uses *like* or *as*.", "", "It is not a question.", "It is not an instruction."]),
        PQ("Identify two features of this sentence and say what they do: 'Stop! Think of the children, the old, the sick: they cannot run from the fire.'",
           "Features: the short command *Stop!* grabs attention and shows urgency; the list of three *the children, the old, the sick* stresses how many people are helpless and appeals to pity. Imperatives and emotive lists are persuasive features."),
        PQ("Why would present tense and figures suit a text that informs, but not a story?",
           "The present tense states facts that remain true, and figures give exact information. A story tells events that happened, so it uses the past tense and description to create pictures."),
        PQ("Edit this sentence for a persuasive notice by adding one feature: 'The clinic needs blood donors.'",
           "For example: 'Could you spare one hour to save a life? The clinic needs you.' (rhetorical question and direct address)."),
        SUM("Identify the purpose of the text first: to inform, to persuade or to create a picture.",
            "Informative: present tense, facts, technical words, neutral tone. Persuasive: questions, commands, you and we, repetition, lists of three. Imaginative: imagery, similes, metaphors, senses.",
            "When asked to explain a feature, give the feature, the example and its effect.",
            "Keep the right features when you edit or write a text of each type.")
    ]))


# ================================================================== 12. Exam lesson: Paper 3
LESSONS.append(lesson(
    module=M_EXAM, topic=T_P3,
    title="Paper 3 strategy: Summary, Text reconstruction and Editing in 2 h 15 min",
    slug="enx3-paper-3-strategy",
    minutes=22,
    summary="Paper 3 has three compulsory sections of 15 marks each in 2 hours 15 minutes. Plan about 45 minutes for each, follow every instruction to the letter, write in your own words, conceal your identity and check your work.",
    objectives=["State the structure of Paper 3 and what each section tests",
                "Plan the time for the three sections",
                "Apply a method to each section and avoid the errors the Board reports",
                "Follow the examination rules on identity and language"],
    key_concepts=["Paper 3", "Compulsory sections", "Time plan", "Instructions", "Concealed identity", "Checking"],
    blocks=[
        H("Introduction"),
        T("Paper 3 of the English Language examination (0730) lasts **2 hours 15 minutes**. It has **three sections, all compulsory**, of **15 marks each**: **Section A Summary writing**, **Section B Text reconstruction** and **Section C Editing**. Because every section is compulsory and carries the same marks, you cannot skip the one you find hard. A balanced plan matters."),
        KEY("The paper at a glance", "", cards=[
            ["Section A: Summary writing", "One question, 15 marks. Select the main points and write them in your own words within the limits."],
            ["Section B: Text reconstruction", "One question, 15 marks. Rebuild a text in a proper sequence, fill gaps or turn one form into another."],
            ["Section C: Editing", "One question, 15 marks. Correct, condense, organise or modify a text; identify text structures and language features."]]),
        T("The syllabus table gives about 45 minutes to each section. This is a sensible plan, but use your own judgement: a section that you find quicker can give time to one that is harder."),
        CODE("""Suggested plan (2 h 15 min = 135 min)
Section A Summary          45 min  (reading and plan 15, writing 25, checking 5)
Section B Reconstruction   45 min  (read 10, reconstruct 30, check 5)
Section C Editing          45 min  (first reading 10, correction 30, check 5)""", "text", title="A time plan (KKEVO suggestion)"),
        H("Rules that apply to the whole paper"),
        KEY("Examination rules", "", cards=[
            ["Identity", "Candidates must conceal their identity: use the name and address provided, never your own."],
            ["Language", "Do not use obscene language, in any text type."],
            ["Instructions", "Follow them to the letter: number of words, number of paragraphs, tense, text type."],
            ["Plan", "Write the plan on the paper and cross it out; do not cross out your answer."]]),
        TIP("The Board's report on the 2023 examination says that candidates lost marks for ignoring instructions, not planning, writing in point form, changing the meaning while paraphrasing, and (in reconstruction) only listing words instead of rewriting the passage. These errors are avoidable.", title="What the Board reports"),
        H("Section A: summary in six steps"),
        KEY("Method", "", cards=[
            ["1", "Read the task: what, how many words, how many paragraphs."],
            ["2", "Read the passage; mark every relevant point."],
            ["3", "List the points; drop examples and details."],
            ["4", "Write in your own words, with transition markers."],
            ["5", "Count the words; stay within the limit."],
            ["6", "Cross out the plan; add no title or introduction unless asked."]]),
        H("Section B: reconstruction in five steps"),
        KEY("Method", "", cards=[
            ["1", "Identify the text type and the task: order, gap filling, or conversion."],
            ["2", "Read the whole text once."],
            ["3", "Use the clues: opening, reference words, time markers, linkers, logical order, ending."],
            ["4", "Write out the full text if asked; keep tense and pronouns correct in reported speech."],
            ["5", "Read it again to check that it flows."]]),
        H("Section C: editing in five steps"),
        KEY("Method", "", cards=[
            ["1", "Read the instruction: correct, condense, reorganise or identify features?"],
            ["2", "Read the text once for sense."],
            ["3", "Check sentence by sentence: tense, agreement, nouns, prepositions, punctuation, spelling."],
            ["4", "Change only what is wrong; keep the meaning."],
            ["5", "For features, name the feature and explain its effect."]]),
        H("Worked example: a mini-paper"),
        EX("Worked example: the three tasks in miniature", intro="You have 9 minutes for three tiny tasks. Show the method on each.", steps=[
            S("A: summarise in not more than 20 words", text="Passage: 'Pupils in Foumban were late because taxis were full. The council bought two buses. Pupils pay 100 FCFA, and lateness has fallen.' Points: late; buses; cheap fare; lateness fallen. Summary: 'The council's two cheap buses have reduced lateness among Foumban pupils who used to find taxis full.' (" + str(wc("The council's two cheap buses have reduced lateness among Foumban pupils who used to find taxis full.")) + " words)"),
            S("B: order", text="a. Then the owner repaired it. b. A shop roof leaked last year. c. Now customers stay dry. Answer: B A C: opening with *a*, then *Then*, then *Now*."),
            S("C: edit", text="'The informations were very useful.' becomes 'The information was very useful.'")]),
        MISTAKE("Spending all the time on the first section", "A perfect summary and two unfinished sections is a poor result: each section carries 15 marks. Move on when your planned time is up."),
        MISTAKE("Identifying yourself", "Never write your real name, school or address in a letter or any text. Use the details provided. A signature with your own name is a breach of the rules."),
        QUIZ("How many sections does Paper 3 have, and are they compulsory?",
             ["Two sections, choose one", "Three sections, all compulsory", "Three sections, answer two", "Four sections, all compulsory"],
             1, "Paper 3 has Summary writing, Text reconstruction and Editing; all are compulsory and carry 15 marks each.",
             hint="Recall the three titles.",
             feedback=["There are three.", "", "No choice is offered.", "There are three, not four."]),
        QUIZ("The question says: 'Summarise in one paragraph of not more than 80 words.' Which action is wrong?",
             ["Writing a plan and crossing it out", "Adding a title and an introduction paragraph", "Using transition markers", "Counting the words"],
             1, "Titles and introductory paragraphs were not asked for and may break the paragraph limit.",
             hint="Follow the instruction to the letter.",
             feedback=["Good practice.", "", "Good practice.", "Good practice."]),
        PQ("List the three sections of Paper 3 and a sensible time for each.",
           "Section A Summary writing, Section B Text reconstruction, Section C Editing; about 45 minutes each for 2 hours 15 minutes in all, all compulsory, 15 marks each."),
        PQ("Give three errors that the Board reports in summary writing.",
           "Examples: not following the instruction (more than one paragraph, adding a title or introduction); changing the meaning when using their own words; writing in point form or fragments; not planning, or crossing out the answer instead of the plan."),
        PQ("In a reconstruction task you must fill gaps in a passage. Why should you write the whole passage out?",
           "Because the Board's report says that candidates who only listed the missing words instead of copying the passage and filling in the words lost half of the marks in that section. Follow the instruction and write the full text."),
        SUM("Paper 3: three compulsory sections of 15 marks each in 2 hours 15 minutes: Summary, Text reconstruction and Editing.",
            "Plan about 45 minutes for each and read the instructions carefully.",
            "Summary: own words, within the limits, no title or introduction unless asked, plan crossed out.",
            "Reconstruction: use sequence clues and write the full text when asked.",
            "Editing: check tense, agreement, nouns, punctuation and spelling; change only what is wrong.",
            "Conceal your identity and avoid obscene language.")
    ]))
