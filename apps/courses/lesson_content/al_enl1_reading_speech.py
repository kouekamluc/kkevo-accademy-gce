"""A Level English Language (0730), Lower Sixth: Reading Comprehension (8 lessons) and Speech Work (7 lessons).

All reading passages are original and invented for teaching (names, places and figures are invented).
IPA is British Received Pronunciation (RP). The written lessons cannot play audio.
"""

from .dsl import *  # noqa: F403

COURSE = ("english-language", "lower-sixth")

M_R = "Reading Comprehension"
M_S = "Speech Work"
T_MAIN = "Main ideas and supporting details"
T_PURP = "Writer's purpose, point of view and attitude"
T_INFER = "Inference and deduction"
T_WORDS = "Words and figures of speech in context"
T_FACT = "Facts, opinions and sequence"
T_DISC = "Discourse markers and cohesion"
T_CRIT = "Critical reasoning and evaluation"
T_SOUNDS = "English consonant and vowel sounds"
T_TRANS = "Phonemic transcription"
T_STRESS = "Word stress"
T_SENT = "Sentence stress and intonation"
T_CONN = "Connected speech and spelling of unknown words"

NOAUDIO = ("**A note before we start.** These lessons are written, so they cannot play sounds. We teach each sound with keywords you "
           "already know, descriptions of the mouth, spelling patterns and rules. Always check a sound in a dictionary that has "
           "audio, and ask your teacher or a confident speaker to say the words for you. Where dictionaries disagree, we write "
           "'check your dictionary'.")

PA = (
    "**A Borehole for Mbouda Road Quarter** (an invented news article)\n\n"
    "Last month, the women of Mbouda Road quarter in Bafoussam stopped queuing for water at dawn. A new community borehole, "
    "paid for by the quarter's own savings group, now supplies clean water within five minutes' walk of every house.\n\n"
    "The project began two years ago, when the savings group counted how much time its members spent fetching water. Most "
    "families walked about forty minutes each way to a spring, and some children arrived late for school because of the queue. "
    "The group decided that water was the problem to solve first.\n\n"
    "Members paid a small sum every week. After eighteen months they had enough to hire a drilling team and buy a pump. Local "
    "masons built the tank stand, and a committee of six volunteers now collects a modest monthly fee to pay for repairs. The "
    "fee is the same for every household.\n\n"
    "The borehole has changed daily life. Mothers report that they have more time for farming and trading. Teachers at the "
    "nearby primary school say fewer pupils are late. A health worker adds that cases of stomach illness, which are often "
    "linked to unsafe water, have fallen, although she says it is too early to be certain of the reason.\n\n"
    "There are still challenges. The pump needs fuel or electricity, the tank must be cleaned regularly, and the committee "
    "must keep honest records. Nevertheless, the group believes that careful management will keep the borehole working for "
    "many years.\n\n"
    "Other quarters have already asked how the savings group began. Its president says the answer is simple: start with a "
    "shared problem, save patiently, and share the work."
)

PB = (
    "**A letter to a newspaper** (invented)\n\n"
    "The Editor, The Kumba Weekly Review, P.O. Box 114, Kumba\n\n"
    "Dear Sir,\n\n"
    "I write in response to your report of 4 March on the state of Kumba Main Market. I have sold fruit there for twenty-two "
    "years, and I have watched with growing worry as thin plastic bags have replaced baskets and banana leaves.\n\n"
    "Plastic bags are cheap and convenient, and I do not blame the customers who ask for them. However, after every market day "
    "the drains behind the fruit section are blocked, and when the rains arrive the water floods our stalls. Last August I "
    "lost two baskets of pawpaw this way. Surely no trader can call that a small matter.\n\n"
    "The council deserves credit for the new bins near the entrance, but bins alone are not enough. I therefore suggest that "
    "traders sell sturdy reusable bags at a low price, that the market association collect used bags for recycling every "
    "Saturday, and that customers be reminded politely to bring their own baskets.\n\n"
    "I am confident that Kumba can lead the way in keeping markets clean if everyone does a little. I thank you for giving "
    "this matter the attention it deserves.\n\n"
    "Yours faithfully,\n\nRuth Ewane"
)

PC = (
    "**A speech to a school assembly** (invented)\n\n"
    "Good morning, Madam Principal, respected teachers and my dear fellow students.\n\n"
    "How many of you read a book for pleasure last week? Please be honest. I see only a few hands, and that is exactly why I "
    "am standing here this morning.\n\n"
    "My topic is simple: our school needs a reading culture. I will give you three reasons. First, reading widens your "
    "vocabulary, and a wide vocabulary helps you in every subject, not only in English. Second, reading teaches you to follow "
    "an argument from beginning to end, and this skill will serve you in the examination hall and in the workplace. Third, "
    "reading is one of the cheapest forms of entertainment we have, because a single book can be shared by a whole class.\n\n"
    "Some of you will say that you have no time. I understand, because I also have homework and chores. But even ten minutes "
    "a day adds up to more than sixty hours in a year.\n\n"
    "Therefore, I appeal to every class to start a reading corner, and I appeal to every student to borrow one book from the "
    "library this week. Let us make our school known not only for football and fine results, but also for readers.\n\n"
    "Thank you for listening."
)

PD = (
    "**From a short story** (invented)\n\n"
    "By half past five the sky over the motor park had turned the colour of a bruise. Nadine pulled her bag closer and looked "
    "again at the ticket in her hand. The bus had been due at four. Around her, the other passengers had stopped asking the "
    "clerk questions; he had answered the first ten with the same shrug.\n\n"
    "A woman beside her unwrapped a small parcel of roasted groundnuts and offered her some. 'You will need strength,' the "
    "woman said kindly. 'These roads do not forgive.'\n\n"
    "Nadine thanked her, but she could not eat. Tomorrow at eight her cousin would be waiting at the gate of the university "
    "in Douala with the form that had to be submitted before noon. She tried her phone again. The screen showed one bar and "
    "then none.\n\n"
    "Thunder rolled somewhere beyond the hills. The clerk looked up at the clouds, closed his ledger, and for the first time "
    "that afternoon he spoke without being asked. 'Everyone, please move under the shed,' he said. As the first heavy drops "
    "struck the tin roof, Nadine counted the people around her and was surprised to find that she was no longer afraid of "
    "the delay. She was afraid of the road."
)

PE = (
    "**Dawn at the beach market** (an invented descriptive passage)\n\n"
    "Dawn arrived at the beach market like a latecomer, slipping in after the work had already begun. The canoes rocked at "
    "the shore, heavy with the night's catch, and the sea breathed gently against them. On the sand, the women of the market "
    "were a flock of bright wrappers, bargaining in voices as sharp as the knives they used to scale the fish.\n\n"
    "'Fresh! Fresh!' cried one trader, holding up a silver mackerel. 'It was swimming an hour ago!' A customer smiled. She "
    "had heard the same claim for years, and she had long ago learned to inspect the gills and the eyes for herself.\n\n"
    "Smoke rose from the drying racks, and the smell of it, salty and sweet together, hung over the beach. A thousand gulls "
    "seemed to hover above the scene, scolding the traders for every dropped scrap. By the time the sun was high, the sand "
    "was crowded, and the first buyers were already hauling away their baskets, weary but content."
)

PF = (
    "**Report on the school science fair** (an invented report)\n\n"
    "The annual science fair took place on Friday 14 June in the school hall. Registration began at 8.00 a.m. and the "
    "Principal opened the fair at 9.00 a.m. Thirty projects from Form 3 to Upper Sixth were displayed.\n\n"
    "Judging took place between 10.00 a.m. and 12.00 noon. The judges, who included two teachers from a neighbouring college "
    "and a local pharmacist, visited each stall in turn. During the lunch break, visitors were invited to vote for their "
    "favourite project, and the prize-giving followed at 1.30 p.m.\n\n"
    "The first prize went to a Lower Sixth team for a solar-powered phone charger, which was, in my opinion, the best "
    "presented project of the day. The second prize went to a Form 5 team that compared how well three kinds of local clay "
    "filter muddy water. The third prize was won by two Form 4 students who built a model of a water pump.\n\n"
    "About 400 visitors attended. The hall was far too small, and the heat made the afternoon uncomfortable. The committee "
    "should therefore move the fair to the sports field next year. The head of science believes that the fair is the most "
    "valuable event in the school calendar, because pupils learn by doing. Before the fair, the participants had spent six "
    "weeks preparing their projects."
)

PG = (
    "**A talk on revision** (invented)\n\n"
    "Good afternoon, everyone. Today I want to talk about why a revision timetable works. There are three main benefits.\n\n"
    "First, a timetable stops you from avoiding difficult subjects. Many students revise the topics they enjoy, and as a "
    "result they leave the hard ones until the night before the paper. A timetable gives every subject its turn.\n\n"
    "Second, a timetable makes the work smaller. 'Revise chemistry' is a huge task, whereas 'revise the mole concept for "
    "forty minutes' is something you can finish. In other words, you turn a mountain into steps.\n\n"
    "In addition, a timetable protects your rest. Students who plan breaks, for example a short walk after each hour of "
    "study, usually concentrate better than those who study for six hours without stopping.\n\n"
    "However, a timetable is useful only if it is realistic. Do not plan to study from 4.00 a.m. to midnight; you will give up "
    "after two days. Finally, review your timetable every Sunday and change whatever did not work. Thank you."
)

PH = (
    "**Two speakers in a school debate** (invented): 'Mobile phones should be allowed in school.'\n\n"
    "Speaker 1 (for): Phones are tools, not toys. With a phone, a student can look up a word, check a formula or watch a "
    "short lesson on a topic the teacher explained too quickly. In my class, three students who own phones improved their "
    "marks in Mathematics after they began to use a free revision application. Furthermore, a phone keeps students safe, "
    "because a child who is stranded after school can call a parent. Everybody knows that the modern world runs on phones, "
    "so schools that ban them are simply living in the past.\n\n"
    "Speaker 2 (against): I do not deny that a phone can be useful. But a phone in a classroom is a temptation. When my "
    "elder brother's school allowed phones, his teacher told him that lessons were often interrupted by messages and "
    "games. I have also noticed that students who check their phones every few minutes find it hard to concentrate on one "
    "task. Parents who truly want to be reached in an emergency can phone the school office, which has always been "
    "available. A ban is therefore the sensible choice for a place of study."
)

LESSONS = []

# ------------------------------------------------------------------ R1. Main ideas and supporting details
LESSONS.append(lesson(
    module=M_R,
    topic=T_MAIN,
    title="Finding the main idea and the supporting details",
    slug="enl1-main-ideas-supporting-details",
    minutes=22,
    summary="Every paragraph and every passage makes one central point, the main idea, and backs it with supporting details. Learn to find the main idea, rank the details and reject answers that are too narrow, too broad or unsupported.",
    objectives=[
        "Distinguish topic, main idea and supporting detail",
        "Find the main idea of a paragraph and of a whole passage",
        "Separate major details from minor details",
        "Reject answer options that are too narrow, too broad or not in the text",
    ],
    key_concepts=["Topic", "Main idea", "Topic sentence", "Supporting detail", "Major and minor details"],
    blocks=[
        H("Introduction"),
        T("A trader in Kumba reads a notice pinned at the market gate. In ten seconds she knows what it is mainly about: new opening hours. "
          "She does not need every number on it to know that. Skilled readers do the same with every text. They look for the one central "
          "point and then see how the rest of the text supports it."),
        T("In Paper 1, Section A, you read passages totalling about 750 to 1,000 words and answer ten multiple-choice questions. "
          "Questions about the main idea and about details are among the most common. The passages can be articles, letters, speeches, "
          "reports or stories, and they may not be on the same subject."),
        H("Topic, main idea and supporting details"),
        D("The **topic** is what a text is about, in a word or a short phrase (for example, 'a community borehole'). "
          "The **main idea** is the most important thing the writer says about the topic, in a full sentence "
          "(for example, 'A community paid for its own borehole, and it improved daily life').", title="Topic and main idea"),
        D("A **supporting detail** is a fact, example, reason, number or explanation that backs up the main idea. "
          "**Major details** directly prove or explain the main idea. **Minor details** add colour or extra information but could be "
          "removed without losing the point.", title="Supporting details"),
        D("A **topic sentence** is the sentence in a paragraph that states its main idea. It is often the first sentence, "
          "but it can come in the middle or at the end, and sometimes it is not written at all and you must put it together yourself.",
          title="Topic sentence"),
        IMG("al-enl1-main-idea-umbrella.svg",
            alt="An umbrella with the words main idea on top of the canopy and three handles hanging underneath labelled detail 1, detail 2 and detail 3.",
            caption="Figure 1. The main idea is the umbrella. Every major detail must fit under it."),
        H("A method for finding the main idea"),
        KEY("Four steps", "Use these steps on any paragraph.", cards=[
            ["1. Find the topic", "Ask: who or what is this paragraph about? Look for the word or idea that returns again and again."],
            ["2. Ask what is said about it", "Ask: what is the writer's point about this topic? That point is the main idea."],
            ["3. Test with the details", "Do the facts, examples and reasons support your sentence? If a detail does not fit, change your sentence."],
            ["4. Check the shape", "A good main idea is not too narrow (one detail only), not too broad (a whole subject) and not something the text never says."],
        ]),
        H("The passage"),
        T("Read this invented news article carefully. We use it for the examples in this lesson."),
        T(PA),
        H("Worked examples"),
        EX("Worked example 1: the main idea of one paragraph",
           intro="Give the main idea of paragraph 2, which begins 'The project began two years ago'.",
           steps=[
               S("Find the topic", text="The paragraph is about how the project began: the savings group, the water problem and the decision."),
               S("Ask what is said about it", text="The group counted the time lost fetching water, saw that families walked about forty minutes each way and that children were late, and chose water as the first problem."),
               S("Write the sentence", text="The savings group began the project because fetching water was costing families a great deal of time."),
               S("Test with details", text="'Forty minutes each way' and 'children arrived late' are the reasons. They fit under the sentence. Good."),
           ]),
        EX("Worked example 2: choosing the main idea of the whole passage",
           intro="Which sentence best states the main idea of the whole passage? "
                 "A. Children in Bafoussam are often late for school. "
                 "B. A community used its own savings to build a borehole that improved daily life, though it must be managed carefully. "
                 "C. Clean water is important to everybody in the world. "
                 "D. Savings groups can do more than the government.",
           steps=[
               S("Test A", text="Too narrow. Late children are one detail in paragraph 2 and one result in paragraph 4."),
               S("Test C", text="Too broad. The passage is about one quarter and one borehole, not about the whole world."),
               S("Test D", text="Not in the text. The passage never compares the group with the government. Do not bring in your own opinion."),
               S("Test B", text="It covers the funding (paragraphs 1 and 3), the benefits (paragraph 4) and the challenges (paragraph 5)."),
               S("Answer", text="B."),
           ]),
        EX("Worked example 3: major or minor detail?",
           intro="The main idea of paragraph 4 is 'The borehole has changed daily life.' Which detail does NOT support it? "
                 "A. Mothers have more time for farming. B. Fewer pupils are late. C. Members paid a small sum every week. D. Stomach illness has fallen.",
           steps=[
               S("Ask of each option", text="Does it show a change after the borehole was built?"),
               S("Check A, B and D", text="More time for farming, fewer late pupils and less stomach illness are all changes."),
               S("Check C", text="Weekly payments happened before the borehole existed. They explain how it was funded (paragraph 3), not how life changed."),
               S("Answer", text="C."),
           ]),
        MISTAKE("Choosing the first sentence automatically",
                "Many paragraphs begin with their main idea, but not all. In paragraph 5 the first sentence ('There are still challenges') is "
                "only half of the point. The last sentence adds that careful management should keep the pump working. Read the whole paragraph."),
        MISTAKE("Choosing the most interesting detail",
                "A striking detail, such as 'forty minutes each way', is easy to remember but it is a detail. Ask whether the sentence covers "
                "most of the paragraph. If it covers only one sentence, it is too narrow."),
        MISTAKE("Using your own knowledge",
                "An option can be true in real life and still wrong in the exercise. If the passage does not say it, it is not the main idea of the passage."),
        QUIZ("A paragraph says: 'Cassava is a hardy crop. It grows in poor soil, needs little rain and can stay in the ground for months after it is ready. "
             "A farmer can therefore expect a harvest even in a dry year.' What is the main idea?",
             ["Cassava needs little rain.", "Cassava is a reliable crop because it is hardy.", "Farmers in Cameroon grow many crops.", "Dry years are common."],
             1,
             "The details (poor soil, little rain, stays in the ground) all support the idea that cassava is reliable. Option A is only one of those details.",
             hint="Which sentence do all the other sentences support?",
             feedback=["That is one supporting detail, so it is too narrow.", "", "Too broad: the paragraph is about cassava only.", "Not stated as the point; the paragraph is about why cassava is dependable."]),
        QUIZ("Which of these is the best definition of a 'supporting detail'?",
             ["A sentence that repeats the title", "A fact, example or reason that backs up the main idea", "The first sentence of every paragraph", "The writer's opinion about the reader"],
             1,
             "A supporting detail proves, explains or illustrates the main idea.",
             hint="Think of the umbrella in Figure 1.",
             feedback=["A repeated title adds no support.", "", "That describes a topic sentence in many paragraphs, not a detail.", "Details support the idea, not an opinion about the reader."]),
        TIP("In Paper 1, a main-idea question often uses words such as 'main idea', 'central point', 'mainly about' or 'best summarises'. "
            "Check each option against the whole passage or paragraph named in the question. 'EXCEPT' and 'NOT' questions ask you to find the odd one out.",
            title="Exam link"),
        PQ("In one sentence, state the main idea of paragraph 3 of the passage (beginning 'Members paid a small sum every week').",
           "The savings group raised the money, built the borehole with local workers and set up a committee and a fee to pay for repairs. "
           "(Accept any sentence that covers saving, building and the committee.)"),
        PQ("Give two supporting details for the main idea of paragraph 4, 'The borehole has changed daily life.'",
           "Any two of: mothers have more time for farming and trading; fewer pupils are late for school; stomach illness has fallen (although the health worker is not yet sure of the cause)."),
        PQ("A learner says the main idea of the whole passage is 'Water is important.' Give two reasons why this answer is poor.",
           "It is too broad, because it says nothing about this quarter, the savings group or the borehole. It is also too vague: it does not say what the writer says about water. "
           "A good main idea names the community, what it did and the result."),
        PQ("Read: 'The market opened late. Several traders had not yet arrived. The few customers who came went away empty-handed. In short, the day's trade was poor.' "
           "Where is the topic sentence, and how do you know?",
           "It is the last sentence, 'In short, the day's trade was poor.' The phrase 'in short' signals a conclusion, and the earlier sentences are details that support it."),
        SUM("The topic is what the text is about; the main idea is the key point the writer makes about it, written as a full sentence.",
            "Supporting details prove or explain the main idea. Major details support it directly; minor details only add colour.",
            "Find the topic, ask what is said about it, test your sentence against the details and check that it is neither too narrow nor too broad.",
            "Do not rely on the first sentence, the most interesting detail or your own knowledge."),
    ],
))

# ------------------------------------------------------------------ R2. Writer's purpose, point of view and attitude
LESSONS.append(lesson(
    module=M_R,
    topic=T_PURP,
    title="Purpose, point of view and attitude",
    slug="enl1-purpose-point-of-view-attitude",
    minutes=23,
    summary="Writers have a purpose, a point of view and an attitude. Learn to name each one from the choice of words, the structure and the content, and to describe tone with accurate words.",
    objectives=[
        "Identify a writer's purpose (to inform, persuade, entertain, instruct, warn, criticise)",
        "Distinguish point of view (who is speaking) from attitude (how the writer feels)",
        "Read tone from word choice, punctuation and sentence patterns",
        "Choose the best tone word and reject extreme options",
    ],
    key_concepts=["Purpose", "Point of view", "Attitude", "Tone", "Bias", "Audience"],
    blocks=[
        H("Introduction"),
        T("Two people write about the same new road. One writes, 'The road will carry our cocoa to market in half the time.' The other writes, "
          "'The road will tear through our farms and leave us with dust.' The facts overlap, yet the writers want different things from their readers "
          "and feel differently about the road. Understanding **why** a text was written, **who** is speaking and **how** the writer feels is a core reading skill."),
        D("The **purpose** is the reason a writer writes. Common purposes are to inform, to persuade, to entertain, to instruct, to warn, "
          "to criticise, to complain, to praise, to describe and to explain. A text can have a main purpose and a secondary one.", title="Purpose"),
        D("**Point of view** is the position from which the text is told or argued. In a story it is the narrator: first person ('I', 'we'), "
          "or third person ('she', 'they'). In an argument it is the side or opinion the writer takes.", title="Point of view"),
        D("**Attitude** is the writer's feeling about the subject, such as admiration, concern, doubt or contempt. **Tone** is the way that "
          "attitude sounds in the words, such as formal, humorous, bitter, sympathetic or urgent.", title="Attitude and tone"),
        H("How to find them"),
        KEY("Clues to purpose and attitude", "Look at four things.", cards=[
            ["Word choice", "'Disgraceful', 'worrying' and 'encouraging' carry feelings. Facts alone ('forty minutes') carry little."],
            ["Sentence type and punctuation", "Questions, exclamations, commands and short blunt sentences create tone. A command such as 'Move under the shed' warns or instructs."],
            ["Structure", "A letter that states a problem, gives reasons and ends with suggestions is trying to persuade."],
            ["What is left out", "A text that gives only one side may be biased. Notice what the writer does not mention."],
        ]),
        T("Here are some tone words you should know. Positive: admiring, optimistic, appreciative, hopeful, enthusiastic. "
          "Negative: critical, bitter, scornful, cynical, resentful, pessimistic. Neutral or balanced: objective, factual, matter-of-fact, detached, formal. "
          "Mixed: concerned, anxious, regretful, wistful, ironic."),
        H("The passage"),
        T("Read this invented letter to a newspaper. We use it for the examples."),
        T(PB),
        H("Worked examples"),
        EX("Worked example 1: the purpose",
           intro="What is the main purpose of the letter?",
           steps=[
               S("Look at the structure", text="Paragraph 1 states why she writes. Paragraphs 2 and 3 describe a problem, give an example (two lost baskets of pawpaw) and give suggestions."),
               S("Look at the language", text="'I therefore suggest' shows she wants action. 'Surely no trader can call that a small matter' tries to win agreement."),
               S("Decide", text="The main purpose is to persuade readers and the council to reduce plastic waste in the market. A secondary purpose is to propose solutions."),
           ]),
        EX("Worked example 2: the writer's attitude",
           intro="Which two words best describe the writer's attitude? A. angry and scornful B. concerned and constructive C. amused and careless D. indifferent and hopeless",
           steps=[
               S("Evidence of concern", text="'Growing worry', the blocked drains and the lost pawpaw show real concern."),
               S("Evidence of constructive thinking", text="She praises the council ('deserves credit'), excuses customers ('I do not blame'), and offers three practical suggestions."),
               S("Reject the extremes", text="She is not angry or scornful, because she is polite and fair. She is not hopeless, because she ends with confidence."),
               S("Answer", text="B."),
           ]),
        EX("Worked example 3: point of view",
           intro="From whose point of view is the letter written, and what is that person's position?",
           steps=[
               S("Find the pronoun", text="She uses 'I' throughout, so it is first person."),
               S("Find the experience", text="She has sold fruit in the market for twenty-two years, so she writes as a trader who is directly affected."),
               S("Name the position", text="She takes the side of reducing plastic bags, but she also recognises the council's effort. Her view is firm but balanced."),
           ]),
        MISTAKE("Choosing an extreme tone word",
                "If a writer is polite and gives suggestions, 'furious' or 'disgusted' is too strong. Choose the word that fits most of the evidence, and prefer the milder one when the text is courteous."),
        MISTAKE("Mixing up point of view and opinion",
                "Point of view is the position from which a text is told or argued (for example, first person, or the traders' side). Opinion is a statement of belief. "
                "A story can be told in the first person without the narrator expressing an opinion about anything."),
        MISTAKE("Assuming the writer is the person in the text",
                "In a story, the narrator or a character may be unkind or foolish. Their attitude is not always the author's. Ask whether the text itself invites us to agree."),
        QUIZ("A writer says: 'Anyone who still burns plastic in the open has no thought for children.' What is the writer's attitude to people who burn plastic?",
             ["Neutral", "Critical", "Admiring", "Puzzled"], 1,
             "The sentence blames and judges people who burn plastic, so the attitude is critical.",
             hint="Look at the words 'no thought for children'.",
             feedback=["A neutral writer would simply report the facts.", "", "Nothing is praised in the sentence.", "There is no question or sign of confusion."]),
        QUIZ("Which is the best description of the purpose of a notice reading 'Beware of the dog. Visitors must ring the bell and wait at the gate'?",
             ["To entertain", "To warn and instruct", "To describe a pet", "To complain"], 1,
             "It warns of a danger and tells visitors what to do.",
             hint="Notice the commands and the word 'beware'.",
             feedback=["There is no humour or story.", "", "The dog is mentioned only as a danger.", "Nothing is criticised."]),
        TIP("Paper 1 asks questions such as 'The writer's attitude to ... is best described as ...' or 'The main purpose of the passage is ...'. "
            "Test each option against the words of the passage, and be careful with options containing extreme words such as 'always', 'furious' or 'hopeless'.",
            title="Exam link"),
        PQ("State two purposes of a speech made by a head teacher at the start of a new school year.",
           "To welcome pupils and inform them of the year's rules or plans; to motivate or encourage them to work hard. (Accept inform, welcome, motivate, advise or persuade.)"),
        PQ("Choose the best word for the tone of this sentence, and explain: 'After three hours in the sun, the queue at the bank had not moved an inch, and the manager had still not appeared.' "
           "A. joyful B. frustrated C. admiring D. mysterious",
           "B, frustrated. The long wait, the lack of movement and the missing manager create a feeling of irritation, though the sentence itself is only a report. "
           "(The tone is mildly critical of the bank.)"),
        PQ("In Mrs Ewane's letter, quote or paraphrase two phrases that show she is trying to be fair to other people.",
           "She says 'I do not blame the customers who ask for them' (fair to customers) and 'The council deserves credit for the new bins' (fair to the council). "
           "(Paraphrase is acceptable.)"),
        PQ("Write one sentence of about fifteen words on the same road topic in a scornful tone, and one in a hopeful tone.",
           "Scornful (for example): 'Another road promised, another year of mud; only the speeches are ever finished on time.' "
           "Hopeful (for example): 'If the work begins this dry season, our farmers may reach the market before the fruit is ripe.' "
           "(Any suitable sentences, with tone words in the vocabulary.)"),
        SUM("Purpose is why the text was written; point of view is the position from which it is told or argued; attitude is the writer's feeling; tone is how that feeling sounds.",
            "Look at word choice, sentence types, structure and what is left out.",
            "Choose tone words that fit most of the evidence and avoid extreme options for courteous writing.",
            "Do not confuse the author with the narrator or a character."),
    ],
))


# ------------------------------------------------------------------ R2b. Text types and parts of a speech
LESSONS.append(lesson(
    module=M_R,
    topic=T_PURP,
    title="Text types and the parts of a speech",
    slug="enl1-text-types-parts-of-a-speech",
    minutes=22,
    summary="Each text type (letter, report, speech, article, minutes, debate, lecture, story) has its own features. Learn to recognise them and to name the parts and persuasive devices of a speech.",
    objectives=[
        "Identify a text type from its layout, language and purpose",
        "Name the parts of a speech and say what each does",
        "Recognise common persuasive devices in a speech",
        "Link text type to audience, register and purpose",
    ],
    key_concepts=["Text type", "Register", "Audience", "Salutation", "Rhetorical question", "Call to action"],
    blocks=[
        H("Introduction"),
        T("Every day you meet different kinds of writing: a message from a friend, a notice at the school gate, a report in a newspaper, a speech at an assembly. "
          "You know at once which is which, because each kind has its own look and sound. In the examination you must be able to name the text type, because "
          "the same skills are tested again in Paper 3, where you summarise and reconstruct texts of these types."),
        D("A **text type** (or **genre**) is a kind of text with a typical purpose, audience, layout and language. The types in this course include informal and formal letters, "
          "newspaper articles, reports, speeches, debates, talks and lectures, minutes of a meeting, discourse (continuous argument or discussion) and stories.", title="Text type"),
        D("**Register** is the level of formality of language, chosen to suit the audience and purpose. 'Hi Aunty, I'm fine' is informal. 'I write to enquire about the vacancy' is formal.", title="Register"),
        H("Features of common text types"),
        CODE("""Text type        Typical features
Informal letter  Address and date, 'Dear Ngu', friendly words, contractions, 'Yours', 'Love'
Formal letter    Both addresses, date, 'Dear Sir/Madam', subject line, polite formal words, 'Yours faithfully'
Newspaper        Headline, byline, short opening paragraph with the key facts, quotations from people,
article          past tense, facts given first
Report           Title, headings, introduction, findings, conclusion, recommendations, objective language
Speech           Greeting to the audience, direct address ('you', 'we'), rhetorical questions,
                 signposts ('first', 'finally'), an appeal, thanks
Debate           A motion, speakers for (proposition) and against (opposition), 'Honourable members',
                 arguments, rebuttals, a closing summary
Talk / lecture   Spoken style, signposting, examples, explanation, often a question to the audience
Minutes          Date, place, 'Present', 'Absent with apologies', numbered items, resolutions,
                 time the meeting ended, signatures
Story            Characters, setting, plot, dialogue in quotation marks, narrative tense""", "text", title="Table 1. Text types and their features"),
        T("A note on closings. In British practice, 'Dear Sir' or 'Dear Madam' ends with 'Yours faithfully', and 'Dear Mr Ndi' ends with 'Yours sincerely'. "
          "Some local textbooks differ on this, so check your textbook and follow the rule your teacher uses."),
        H("The parts of a speech"),
        KEY("A speech has a shape", "Most speeches follow this order, though a short one may combine parts.", cards=[
            ["1. Salutation", "Greets the audience and respects rank: 'Madam Principal, respected teachers and fellow students'."],
            ["2. Opening or hook", "Wins attention: a question, a surprising fact, a short story."],
            ["3. Topic or thesis", "States what the speech is about or what the speaker believes."],
            ["4. Body", "Gives the reasons, examples and evidence, often signposted: first, second, third."],
            ["5. Answer to objections", "Admits the other side's view and replies to it."],
            ["6. Conclusion and call to action", "Repeats the main point and tells the audience what to do."],
            ["7. Thanks", "Closes politely: 'Thank you for listening'."],
        ]),
        T("Speakers also use **persuasive devices**. A **rhetorical question** is a question asked for effect, not for an answer. **Direct address** uses 'you' and 'we' to include the audience. "
          "The **rule of three** lists three reasons or examples because three feels complete. **Repetition** hammers a key phrase. An **appeal** asks the audience to act."),
        H("The speech"),
        T(PC),
        H("Worked examples"),
        EX("Worked example 1: label the parts of the speech",
           intro="Match each part of the speech to its job.",
           steps=[
               S("Salutation", text="'Good morning, Madam Principal, respected teachers and my dear fellow students.'"),
               S("Hook", text="'How many of you read a book for pleasure last week? Please be honest.' This is a rhetorical question that involves the audience."),
               S("Thesis", text="'Our school needs a reading culture.'"),
               S("Body", text="Three reasons are signposted with First, Second and Third (rule of three): vocabulary, following an argument, cheap entertainment."),
               S("Answer to an objection", text="'Some of you will say that you have no time.' The speaker replies with the ten-minutes-a-day figure."),
               S("Call to action and thanks", text="'I appeal to every class to start a reading corner' and 'Thank you for listening'."),
           ]),
        EX("Worked example 2: name the text type",
           intro="Name the text type of each extract. (a) 'Present: Mr Tabi (Chairman), Ms Nji (Secretary). Apologies for absence: Mrs Fon.' "
                 "(b) 'Dear Aunty Mercy, I hope this letter finds you in good health.' "
                 "(c) 'Honourable members of the house, I rise to oppose the motion.' "
                 "(d) 'By a staff reporter. Heavy rain destroyed two bridges in the district on Monday, officials said.'",
           steps=[
               S("(a)", text="Minutes of a meeting: 'Present' and 'Apologies for absence' are standard headings."),
               S("(b)", text="Informal letter: a family name, a warm greeting and a friendly wish for good health."),
               S("(c)", text="Debate: 'Honourable members', 'the house' and 'the motion' belong to formal debate."),
               S("(d)", text="Newspaper article: a byline, the key facts first, and a report attributed to officials."),
           ]),
        EX("Worked example 3: why use the rule of three?",
           intro="The speaker gives three reasons for reading. Why three, and what does it show about her audience?",
           steps=[
               S("Effect", text="Three feels complete and is easy to remember. A listener cannot go back and re-read, so the speaker must be easy to follow."),
               S("Audience", text="The speaker addresses students, so her reasons are practical (vocabulary, examinations, cost) and her language is simple and direct."),
           ]),
        MISTAKE("Naming the text type from the topic",
                "A text about reading is not necessarily an essay. Decide from the layout and the language: a greeting to an audience and an appeal suggest a speech; headings and recommendations suggest a report."),
        MISTAKE("Mixing up a speech and a lecture",
                "A speech tries to persuade or inspire, usually with an appeal. A lecture or talk mainly explains a subject, and its signposts help note-taking. Both are spoken styles."),
        MISTAKE("Ignoring the audience",
                "The same message changes with the audience. A speech to students uses short, lively sentences. A formal letter to a ministry uses a formal register. Always ask who the readers or listeners are."),
        QUIZ("'Good morning, ladies and gentlemen. Have you ever wondered why the sky is blue?' This opening is most likely from",
             ["A formal letter", "A set of minutes", "A talk or speech", "A newspaper headline"], 2,
             "The greeting to an audience and the direct question are features of spoken talks and speeches.",
             hint="Who is being greeted, and is the text spoken or written?",
             feedback=["A formal letter has addresses and 'Dear Sir/Madam'.", "Minutes list who was present and what was decided.", "", "A headline is short and has no greeting."]),
        QUIZ("What is the main job of a call to action at the end of a speech?",
             ["To thank the audience", "To tell the audience what to do", "To greet the principal", "To introduce the topic"], 1,
             "A call to action asks the audience to act on the speaker's message.",
             hint="Think of 'I appeal to every student to borrow one book'.",
             feedback=["Thanks come after the appeal.", "", "Greetings come at the start.", "The topic is introduced near the start."]),
        TIP("Paper 1 may ask you to identify a text type or a part of a speech from a short extract, and Paper 3 will ask you to summarise or reconstruct texts of these types. "
            "Learn the features in Table 1 and the seven parts of a speech.", title="Exam link"),
        PQ("Name three persuasive devices in the speech about reading and give an example of each.",
           "Rhetorical question: 'How many of you read a book for pleasure last week?' Rule of three: the three reasons for reading. Direct address: 'you' and 'us/our' ('Let us make our school known'). "
           "Also accept: appeal ('I appeal to every class') and repetition."),
        PQ("In which part of a speech would you expect the phrase 'To sum up'? Give one more phrase that belongs in the same part.",
           "The conclusion. Other phrases: 'In conclusion', 'Finally', 'Therefore'."),
        PQ("Give two differences between a formal letter and an informal letter.",
           "A formal letter has both addresses, a subject line, a formal register without contractions and a closing like 'Yours faithfully'. An informal letter has the writer's address and date only, "
           "a friendly tone with contractions and a closing like 'Yours' or 'Love'."),
        PQ("What would you expect to find under the heading 'Recommendations' in a report?",
           "A list of actions the writer advises, based on the findings. For example, 'The school should buy more textbooks' or 'The fair should be moved to the sports field'."),
        SUM("Each text type has typical layout, language and purpose. Learn Table 1 and identify the type from those clues, not from the topic.",
            "A speech has seven parts: salutation, hook, thesis, body, answer to objections, call to action and thanks.",
            "Persuasive devices include the rhetorical question, direct address, the rule of three, repetition and the appeal.",
            "Always ask who the audience is and which register suits it."),
    ],
))

# ------------------------------------------------------------------ R3. Inference and deduction
LESSONS.append(lesson(
    module=M_R,
    topic=T_INFER,
    title="Reading between the lines: inference and deduction",
    slug="enl1-inference-and-deduction",
    minutes=22,
    summary="An inference is a conclusion the text supports but does not state. Learn a four-step method for inferring, how deduction differs from inference, and how to avoid over-reading.",
    objectives=[
        "Explain the difference between what a text states and what it implies",
        "Use clues in the text to draw a supported inference",
        "Distinguish inference, deduction and unsupported assumption",
        "Choose the best inference and reject over-reading",
    ],
    key_concepts=["Inference", "Implication", "Deduction", "Clue", "Assumption", "Over-reading"],
    blocks=[
        H("Introduction"),
        T("You arrive at a friend's house in Bamenda and the compound is full of plastic chairs and a tent is going up. Nobody says, 'There is an event here today', but you know. "
          "You inferred it from the clues. Writers also leave things unsaid and trust readers to work them out. Examiners love inference because it shows whether you truly understood."),
        D("An **inference** is a conclusion that you draw from clues in the text and from what you already know about the world. The text suggests it but does not state it. "
          "A good inference is **supported by the text**; a poor one is only a guess.", title="Inference"),
        D("**Implication** is what a writer suggests without saying it directly. A writer implies; the reader infers.", title="Implication"),
        D("A **deduction** is a conclusion that follows with certainty from given facts (premises). Example: 'All applicants must be over sixteen. Joel is applying. So Joel is over sixteen.' "
          "An inference from a story is usually 'most likely', while a deduction from clear premises is 'must be'.", title="Deduction"),
        H("A four-step method"),
        KEY("How to infer", "Follow these steps in order.", cards=[
            ["1. Read the clue", "Find the exact words in the text that matter: an action, a word, a detail."],
            ["2. Ask what it suggests", "What does a person who acts or speaks like this feel, want or know?"],
            ["3. Add what you know", "Use ordinary knowledge of people and the world: a deadline causes worry; rain makes roads dangerous."],
            ["4. Test against the text", "Does anything in the passage contradict your idea? Can you point to the words that support it?"],
        ]),
        T("Key phrases in questions: 'it can be inferred that', 'the writer implies', 'suggests', 'most likely', 'we can conclude'. "
          "All of them ask for an answer that the passage supports but does not state."),
        H("The passage"),
        T(PD),
        H("Worked examples"),
        EX("Worked example 1: why is Nadine so anxious?",
           intro="Which is the best explanation of why Nadine is anxious? A. She dislikes the clerk. B. She must submit a form by noon the next day and the bus is very late. "
                 "C. She has lost her ticket. D. She is afraid of her cousin.",
           steps=[
               S("Read the clue", text="'Tomorrow at eight her cousin would be waiting ... with the form that had to be submitted before noon.' The bus 'had been due at four' and it is half past five."),
               S("What does it suggest?", text="A late bus threatens the deadline."),
               S("Test the others", text="Nothing shows dislike of the clerk, a lost ticket (she 'looked again at the ticket in her hand') or fear of her cousin."),
               S("Answer", text="B."),
           ]),
        EX("Worked example 2: what is implied about the woman with the groundnuts?",
           intro="What can be inferred about her from 'You will need strength. These roads do not forgive'?",
           steps=[
               S("Read the clue", text="She is kind ('said kindly') and she warns of the roads."),
               S("What does it suggest?", text="She has travelled this road before, knows it is hard and dangerous, especially in rain, and expects a long journey."),
               S("Careful limit", text="We cannot infer her job, her age or that she has had an accident. The text does not give that."),
           ]),
        EX("Worked example 3: the last sentence",
           intro="'She was no longer afraid of the delay. She was afraid of the road.' What does this tell us about how Nadine's feelings have changed?",
           steps=[
               S("Contrast", text="Before: she worried about being late. Now: she worries about the journey itself."),
               S("Cause", text="The storm has come. Rain makes the road dangerous, as the woman warned."),
               S("Inference", text="Nadine's concern has shifted from losing time to personal safety. The writer builds tension without saying 'she was frightened'."),
           ]),
        EX("Worked example 4: a deduction",
           intro="Premises: 'The shed holds only passengers who have a ticket. Nadine is inside the shed.' What follows with certainty?",
           steps=[
               S("Read the premises", text="Only ticket holders are in the shed, and Nadine is in the shed."),
               S("Conclusion", text="Nadine has a ticket. (This follows by necessity, so it is a deduction.)"),
               S("Be careful", text="'Nadine is rich' does not follow, and neither does 'every ticket holder is in the shed'."),
           ]),
        MISTAKE("Over-reading",
                "Do not add facts the text cannot support. From the passage we cannot infer that the bus crashed, that Nadine will fail, or that the clerk is dishonest. "
                "If you cannot point to the words that point that way, do not choose it."),
        MISTAKE("Under-reading",
                "Do not pick an option only because it repeats the passage word for word. When the question says 'infer' or 'imply', the correct answer usually restates the idea in different words."),
        MISTAKE("Using personal opinion",
                "Your own view ('clerks should be more polite') is not evidence. An inference must come from the text, not from what you wish was true."),
        QUIZ("Which is the best inference from 'The clerk looked up at the clouds, closed his ledger, and for the first time that afternoon he spoke without being asked'?",
             ["He was angry with the passengers.", "He had noticed the coming storm and had to act.", "He had finished his work for the day and was going home.", "He was afraid of the thunder."],
             1,
             "He looks at the clouds, then speaks to the passengers about moving under the shed. The storm is the reason he speaks.",
             hint="What does he say immediately after looking at the clouds?",
             feedback=["There is no sign of anger; he speaks politely.", "", "He closes the ledger but he stays to organise passengers.", "Nothing says he is afraid; he gives clear directions."]),
        QUIZ("'All GCE candidates must carry an ID card. Marie is a GCE candidate.' Which statement follows with certainty?",
             ["Marie is clever.", "Marie must carry an ID card.", "All who carry ID cards are candidates.", "Marie will pass."],
             1,
             "It follows directly from the two premises. The others do not.",
             hint="Which one repeats the rule applied to Marie?",
             feedback=["Nothing is said about her ability.", "", "That reverses the first premise, and it does not follow.", "A future result is not stated."]),
        TIP("Inference questions are common in Paper 1, Section A. Underline the clue in the passage before you read the options, and choose the option that is supported by the clue "
            "and nothing more. Be especially careful when two options are both possible: the better one uses more of the evidence.", title="Exam link"),
        PQ("Read: 'Kofi checked his pockets for the third time. He glanced at the clock above the examiner's desk and then at the blank page.' "
           "What can be inferred about Kofi? Give your reason.",
           "He is worried or nervous, probably because he is short of time or cannot remember the answer. Reasons: checking his pockets repeatedly, glancing at the clock and the blank page all suggest anxiety. "
           "(We cannot infer that he will cheat or that he has failed.)"),
        PQ("In the passage, what is suggested by the colour 'of a bruise' to describe the sky?",
           "The sky is dark purple-grey and heavy with storm clouds, and the comparison to a bruise suggests something painful or threatening is coming."),
        PQ("Explain the difference between inference and deduction in two sentences.",
           "An inference is a likely conclusion from clues in a text plus general knowledge; it may be reasonable but not certain. "
           "A deduction follows with certainty from premises that are given, so if the premises are true, the conclusion must be true."),
        PQ("From the passage, can we infer that Nadine has travelled this route before? Say yes or no and give a reason.",
           "No. The text does not say so. She may be a first-time traveller; the woman, not Nadine, shows knowledge of the roads. The text supports only that Nadine is travelling to Douala for a university form."),
        SUM("An inference is a conclusion supported by clues in the text but not stated; a deduction follows with certainty from given premises.",
            "Method: find the clue, ask what it suggests, add what you know, test it against the text.",
            "Avoid over-reading (adding facts), under-reading (copying words) and personal opinion.",
            "When two options seem possible, choose the one with more support from the passage."),
    ],
))


# ------------------------------------------------------------------ R4. Words and figures of speech in context
LESSONS.append(lesson(
    module=M_R,
    topic=T_WORDS,
    title="Meaning in context: unfamiliar words and figures of speech",
    slug="enl1-words-figures-in-context",
    minutes=24,
    summary="Use clues in the sentence to work out unfamiliar words, choose the right meaning of words with several meanings, and explain the effect of simile, metaphor, personification, hyperbole and other figures of speech.",
    objectives=[
        "Work out the meaning of an unfamiliar word from context clues",
        "Choose the meaning of a word that fits the sentence, not just a dictionary meaning",
        "Identify and explain simile, metaphor, personification, hyperbole, irony, understatement and other figures",
        "Say what effect a figure of speech has on the reader",
    ],
    key_concepts=["Context clue", "Connotation", "Simile", "Metaphor", "Personification", "Hyperbole", "Irony"],
    blocks=[
        H("Introduction"),
        T("You will meet words in an examination passage that you have never seen. You cannot use a dictionary, so you must do what good readers do: use the words around the unknown word. "
          "In the same way, writers often say one thing and mean another, comparing a market crowd to a flock of birds or saying that the sun 'smiled'. "
          "These comparisons are **figures of speech**. The syllabus asks you to find the meaning of words and expressions in context and to interpret figures of speech."),
        H("Working out unfamiliar words"),
        KEY("Five kinds of context clue", "Look at the sentence and the sentences next to it.", cards=[
            ["Definition", "The writer explains the word: 'a drought, that is, a long period without rain'."],
            ["Synonym or restatement", "'The trader was frugal, careful with every franc.' Frugal means careful with money."],
            ["Contrast", "'Unlike his talkative brother, Samuel was taciturn.' The word 'unlike' tells you taciturn means quiet."],
            ["Example", "'She grew staple crops such as maize, cassava and plantains.' Staple means basic, widely eaten."],
            ["Inference from the situation", "'The roof leaked, the floor was cracked, and the walls had not seen paint in years; the house was dilapidated.' It means in poor condition."],
        ]),
        D("**Denotation** is the dictionary meaning of a word. **Connotation** is the feeling or idea attached to it. 'Thin', 'slim' and 'skinny' all denote a small body, "
          "but 'slim' sounds positive and 'skinny' sounds negative.", title="Denotation and connotation"),
        T("Many words have more than one meaning. 'Scale' can mean 'remove the scales from a fish', 'climb', or 'an instrument for weighing'. "
          "The best meaning is the one that fits the whole sentence. A test: replace the word with your meaning and read the sentence again. If it still makes sense, you are probably right."),
        H("Figures of speech"),
        D("A **figure of speech** uses words in a non-literal way to create an effect: to make a picture in the reader's mind, to emphasise, or to show feeling. "
          "The meaning is not the dictionary meaning of the words.", title="Figure of speech"),
        CODE("""Figure           What it does                          Example
Simile           Compares using 'like' or 'as'         'as sharp as a knife'
Metaphor         Says one thing IS another              'The market was a beehive'
Personification  Gives human actions to non-humans     'The wind whispered'
Hyperbole        Deliberate exaggeration                'I have told you a million times'
Understatement   Says less than the truth               'It was a bit of a storm' (a huge one)
Irony            Says the opposite of what is meant,    'What lovely weather!' (during a flood)
                 or a result opposite to expectation
Oxymoron         Joins opposites                        'a deafening silence'
Alliteration     Repeats the first consonant sound      'busy buses bump by'
Onomatopoeia     Sound imitates the sense               'buzz', 'hiss', 'splash'
Euphemism        Gentle word for an unpleasant thing    'passed away' for 'died'
Idiom            Fixed expression with a fixed meaning 'under the weather' (ill)""", "text", title="Table 1. Figures of speech"),
        T("Always describe the **effect**. 'It is a simile' scores little. 'The simile compares the traders' voices to knives, which suggests sharp, piercing sounds' explains how it works."),
        H("The passage"),
        T(PE),
        H("Worked examples"),
        EX("Worked example 1: meaning of an unfamiliar word",
           intro="What does 'hauling' mean in 'the first buyers were already hauling away their baskets'? A. dancing B. dragging or carrying with effort C. selling D. guarding",
           steps=[
               S("Read the sentence", text="The buyers are leaving with baskets, and they are 'weary but content'."),
               S("Test the options", text="'Dancing' does not fit weary people with baskets. 'Selling' does not fit buyers. 'Guarding' is not moving away."),
               S("Answer", text="B. The buyers take away heavy baskets of fish with effort."),
           ]),
        EX("Worked example 2: name the figure and explain the effect",
           intro="(a) 'Dawn arrived ... like a latecomer.' (b) 'the sea breathed gently.' (c) 'a flock of bright wrappers.' (d) 'A thousand gulls.'",
           steps=[
               S("(a) Simile and personification", text="Dawn is compared to a person arriving late. The picture is of daylight slipping in quietly after the work began."),
               S("(b) Personification", text="The sea is given the human action of breathing, so the gentle movement of waves seems alive and calm."),
               S("(c) Metaphor", text="The women are not literally birds. The metaphor suggests many bright colours moving together and making a lot of noise."),
               S("(d) Hyperbole", text="'A thousand' exaggerates to show a very large crowd of gulls. We should not count them."),
           ]),
        EX("Worked example 3: interpreting a comparison",
           intro="What does 'bargaining in voices as sharp as the knives they used to scale the fish' tell us about the traders' voices?",
           steps=[
               S("Identify", text="It is a simile, using 'as ... as'."),
               S("The link", text="Knives are sharp and cut. The voices are therefore loud, clear and piercing."),
               S("Effect", text="The simile makes the noise physical, and it fits the setting because the same women are holding knives."),
           ]),
        EX("Worked example 4: irony",
           intro="'It was swimming an hour ago!' cried the trader. The customer smiled. Is the trader's claim ironic? Explain what the customer's smile suggests.",
           steps=[
               S("Read the clue", text="'She had heard the same claim for years, and she had long ago learned to inspect the gills and eyes for herself.'"),
               S("Interpret", text="The customer does not believe the exaggeration but is amused, not angry. The smile shows friendly experience."),
               S("Name it", text="The trader's claim is an exaggeration (a sales line), and the situation is lightly humorous. It is not strict irony, because the trader means what he says."),
           ]),
        MISTAKE("Taking a figure literally",
                "'The sea breathed' does not mean the sea has lungs. When a statement cannot be literally true, look for a figure of speech and ask what it suggests."),
        MISTAKE("Confusing simile and metaphor",
                "A simile uses 'like' or 'as' ('as sharp as knives'). A metaphor states that one thing is another ('a flock of bright wrappers'). Check for the words 'like' and 'as' first."),
        MISTAKE("Choosing a meaning that is true in a dictionary but wrong here",
                "'Content' can be a noun (the contents of a box) or an adjective meaning satisfied. In 'weary but content' it is the adjective: the buyers are satisfied. Replace and test."),
        QUIZ("'The classroom was a furnace.' This is",
             ["a simile", "a metaphor", "an understatement", "onomatopoeia"], 1,
             "It says directly that the classroom IS a furnace, without 'like' or 'as'. It suggests extreme heat.",
             hint="Is there the word 'like' or 'as'?",
             feedback=["A simile would say 'like a furnace'.", "", "An understatement would reduce the heat: 'a little warm'.", "Onomatopoeia imitates a sound."]),
        QUIZ("'Unlike his talkative brother, Samuel was taciturn.' The word 'taciturn' most nearly means",
             ["rude", "silent by habit", "angry", "tall"], 1,
             "'Unlike' signals a contrast with talkative, so taciturn means not talkative: quiet.",
             hint="What does the word 'unlike' tell you?",
             feedback=["Nothing suggests bad manners.", "", "Talkative people are not necessarily calm; 'unlike' contrasts talking, not temper.", "Height is not mentioned."]),
        TIP("Paper 1 asks things like 'As used in the passage, the word X means ...' and 'The expression Y suggests ...'. Go back to the line, replace the word with each option and read the sentence. "
            "The best option is both accurate and natural in the sentence.", title="Exam link"),
        PQ("Explain the meaning of 'scale' in 'the knives they used to scale the fish'.",
           "To scale a fish is to remove its scales (the small plates on its skin) before cooking or selling it."),
        PQ("Identify the figure of speech in 'Smoke rose from the drying racks, and the smell of it, salty and sweet together, hung over the beach' and explain what 'hung' suggests.",
           "There is a contrast ('salty and sweet together') and the verb 'hung' is used for a smell, which cannot literally hang. It suggests the smell was thick and stayed in the air like a cloud. "
           "(Accept a short explanation of the effect.)"),
        PQ("Write a sentence using each: a simile about a market and a personification of rain.",
           "Simile: 'The market was as noisy as a school at break time.' Personification: 'The rain drummed on the roof as if it wanted to come in.' (Any suitable sentences.)"),
        PQ("What is the difference between denotation and connotation? Use 'slim' and 'skinny' as examples.",
           "Denotation is the dictionary meaning; connotation is the feeling attached to a word. Both words denote a thin body, but 'slim' suggests an attractive, healthy figure while 'skinny' suggests too thin."),
        SUM("Use the five clues (definition, synonym, contrast, example, situation) to work out unfamiliar words, then test the meaning in the sentence.",
            "Words have denotation (dictionary meaning) and connotation (feeling). Choose the meaning that fits the context.",
            "Know the main figures: simile, metaphor, personification, hyperbole, understatement, irony, oxymoron, alliteration, onomatopoeia, euphemism and idiom.",
            "Always explain the effect, not just the name."),
    ],
))

# ------------------------------------------------------------------ R5. Facts, opinions and sequence
LESSONS.append(lesson(
    module=M_R,
    topic=T_FACT,
    title="Facts, opinions and the order of events",
    slug="enl1-facts-opinions-sequence",
    minutes=22,
    summary="Tell facts (which can be checked) from opinions (judgements and beliefs), notice whose view is reported, and put events in chronological order using time markers, including events told out of order.",
    objectives=[
        "Distinguish facts from opinions and from reported opinions",
        "Recognise words that signal opinion",
        "Put events in chronological order using time markers",
        "Spot events told out of order (flashback or later mention)",
    ],
    key_concepts=["Fact", "Opinion", "Reported opinion", "Chronological order", "Time marker", "Flashback"],
    blocks=[
        H("Introduction"),
        T("A seller at Mokolo market says, 'These tomatoes cost 500 FCFA a basket and they are the sweetest in town.' The first half can be checked. The second half is the seller's view. "
          "Examiners test whether you can separate the two, and whether you can follow the order in which things happened, which may be different from the order in which a writer tells them."),
        D("A **fact** is a statement that can be checked or proved true or false, such as a date, number, event or measurement. A false statement of this kind is still a statement of fact: it can be checked.", title="Fact"),
        D("An **opinion** is a belief, feeling or judgement. Reasonable people can disagree about it, and it cannot be proved the way a fact can. "
          "It may be well supported by evidence, but it is still a judgement.", title="Opinion"),
        KEY("Signals of opinion", "Opinions often contain these.", cards=[
            ["Judgement words", "best, worst, beautiful, boring, too small, excellent, disgraceful, valuable"],
            ["Belief words", "I think, in my opinion, I believe, we feel, it seems, probably, perhaps"],
            ["Advice and obligation", "should, ought to, must, it would be better, needs to"],
            ["Predictions", "will improve, is likely to, will certainly"],
        ]),
        T("Facts are not guaranteed by these words, and opinion is not guaranteed to be wrong. 'The hall seats 200' is a fact. 'The hall is too small' is an opinion, even if many people agree. "
          "To decide, ask: **Can I check this with a measurement, a record or an observation?**"),
        D("A **reported opinion** attributes a view to someone: 'The head of science believes that the fair is the most valuable event.' "
          "It is a **fact** that she believes this (you could ask her), but what she believes is an **opinion**.", title="Reported opinions"),
        H("Sequence"),
        T("Events in a text are usually told in **chronological order** (the order in which they happened), but not always. Look for time markers."),
        CODE("""Before    earlier, previously, before, prior to, until, once, at first
During    while, as, meanwhile, during, at the same time
After     then, next, afterwards, later, following, soon, by the time, eventually
End       finally, at last, in the end, ultimately
Out of order    'had spent' (past perfect), 'earlier that week', 'years before'""", "text", title="Table 1. Time markers"),
        H("The passage"),
        T(PF),
        H("Worked examples"),
        EX("Worked example 1: fact or opinion?",
           intro="Classify each sentence: (a) 'Registration began at 8.00 a.m.' (b) 'The project was the best presented of the day.' "
                 "(c) 'About 400 visitors attended.' (d) 'The hall was far too small.' (e) 'The committee should move the fair to the sports field.' "
                 "(f) 'The head of science believes that the fair is the most valuable event.'",
           steps=[
               S("(a) Fact", text="A time that can be checked in the programme."),
               S("(b) Opinion", text="'Best presented' is a judgement. The writer even signals it with 'in my opinion' in the passage."),
               S("(c) Fact", text="A number that can be checked against a register or count (it says 'about', so it is an estimate, but still checkable)."),
               S("(d) Opinion", text="'Far too small' is a judgement of size against need. The seating capacity would be a fact."),
               S("(e) Opinion", text="'Should' gives advice."),
               S("(f) Reported opinion", text="The sentence reports her belief. What she believes is an opinion; that she holds it is a fact."),
           ]),
        EX("Worked example 2: put the events in order",
           intro="Put these in order: judging, the vote by visitors, registration, prize-giving, the Principal opens the fair.",
           steps=[
               S("Use the times", text="Registration 8.00 a.m.; opening 9.00 a.m.; judging 10.00 a.m. to 12 noon."),
               S("Vote and prizes", text="The vote was held during the lunch break, after judging, and prize-giving followed at 1.30 p.m."),
               S("Order", text="Registration, the Principal opens the fair, judging, the vote by visitors, prize-giving."),
           ]),
        EX("Worked example 3: the event told last that happened first",
           intro="The last sentence says that the participants 'had spent six weeks preparing'. Where does this fit in the sequence?",
           steps=[
               S("Notice the tense", text="'Had spent' is past perfect: it describes something finished before the fair day."),
               S("Place it", text="It is the earliest event. The preparation came before registration, even though it is mentioned last."),
           ]),
        EX("Worked example 4: whose view?",
           intro="Whose opinion is 'which was, in my opinion, the best presented project of the day'?",
           steps=[
               S("Pronoun", text="'My' refers to the writer of the report. The passage does not say whether the writer was one of the judges."),
               S("Careful point", text="A report should be objective. A personal opinion in a report is acceptable only if it is clearly marked, as here."),
           ]),
        MISTAKE("Treating a statement that sounds sure as a fact",
                "'Everyone knows the fair is the best event' sounds sure but cannot be checked. Opinions can be strongly worded. Ask whether it can be proved."),
        MISTAKE("Thinking a fact must be true",
                "'The fair took place on a Sunday' is a statement of fact (it can be checked), but here it would be false. Do not confuse 'fact' with 'true'."),
        MISTAKE("Ordering events by where they are in the text",
                "A writer may mention an earlier event later. Use time words and tenses ('had', 'before', 'earlier') to build the real order."),
        QUIZ("Which of these is an opinion?",
             ["The market opens at 6.00 a.m.", "The market is the busiest in the region.", "The market has 300 stalls.", "The market is closed on Sundays."],
             1,
             "'The busiest' is a judgement that depends on how we measure, so it is an opinion unless the writer gives data. The others can be checked.",
             hint="Which one cannot be settled simply by looking at a record?",
             feedback=["An opening time can be checked.", "", "A count of stalls can be checked.", "A closing day can be checked."]),
        QUIZ("'By the time the rescuers arrived, the water had already reached the roof.' Which happened first?",
             ["The rescuers arrived.", "The water reached the roof.", "Both at the same time.", "Cannot be told."],
             1,
             "'Had already reached' (past perfect) marks the earlier event.",
             hint="Which verb is in the past perfect?",
             feedback=["They arrived after the water reached the roof.", "", "'By the time' means one event was already finished.", "The tense and 'already' make the order clear."]),
        TIP("Paper 1 may ask you to pick the sentence that is a fact or an opinion, the order of events, or the view of a named person. "
            "In Paper 3 (Text reconstruction) you rebuild a text in the right order, so time markers are valuable there too.", title="Exam link"),
        PQ("State whether each is a fact or an opinion: (a) 'The fair was held on a Friday.' (b) 'The solar charger deserved the first prize.'",
           "(a) Fact: the day can be checked. (b) Opinion: 'deserved' is a judgement."),
        PQ("Rewrite this sentence so that it becomes a clear opinion: 'The hall holds 200 people.'",
           "For example: 'In my opinion, a hall that holds only 200 people is not big enough for a school fair.' (Any sentence with a judgement or 'should'.)"),
        PQ("Give the order of these events from the passage: the second prize is announced; the judges visit each stall; registration begins; visitors vote.",
           "Registration begins; the judges visit each stall; visitors vote (lunch break); the second prize is announced at the prize-giving."),
        PQ("Explain why 'The head of science believes that the fair is the most valuable event' contains both a fact and an opinion.",
           "That she believes it is a fact, which could be checked by asking her. What she believes (that the fair is the most valuable event) is an opinion, because it is a judgement."),
        SUM("A fact can be checked; an opinion is a judgement or belief. A reported opinion is a fact that someone holds an opinion.",
            "Look for judgement words (best, too), belief words (I think) and advice words (should).",
            "Use time markers and tenses to place events in order, and remember that an event mentioned last may have happened first.",
            "Do not confuse 'fact' with 'true' or a confident tone with proof."),
    ],
))


# ------------------------------------------------------------------ R6. Discourse markers and cohesion
LESSONS.append(lesson(
    module=M_R,
    topic=T_DISC,
    title="Discourse markers and how a text holds together",
    slug="enl1-discourse-markers-cohesion",
    minutes=23,
    summary="Discourse markers signal addition, contrast, cause, example, explanation and sequence. Cohesive devices (pronoun reference, substitution, repetition, synonyms) link sentences into one text.",
    objectives=[
        "Name the function of common discourse markers",
        "Choose the marker that fits the relationship between two ideas",
        "Identify what a pronoun or substituting word refers to",
        "Recognise lexical cohesion and redundant repetition",
    ],
    key_concepts=["Discourse marker", "Cohesion", "Reference", "Substitution", "Lexical cohesion", "Redundancy"],
    blocks=[
        H("Introduction"),
        T("Read this: 'The bus was late. We missed the meeting.' You supply the link: the bus was late, **so** we missed the meeting. "
          "Writers rarely leave such links to chance. They place small signal words that tell the reader how one idea connects to the next. "
          "In the examination you must recognise those signals, choose the right one and see what a word like 'it' or 'this' points back to."),
        D("A **discourse marker** (or **linking word**) is a word or phrase that shows how a sentence or idea relates to the one before or after it. "
          "Examples: however, for example, therefore, in addition, finally.", title="Discourse marker"),
        D("**Cohesion** is the way the parts of a text are linked on the surface by grammar and vocabulary, so that it reads as one connected text. "
          "**Coherence** is the way the ideas make sense together. A text can be cohesive and still not make sense, but a good text has both.", title="Cohesion and coherence"),
        H("Markers and their jobs"),
        CODE("""Job              Markers
Addition         also, and, furthermore, moreover, in addition, besides, as well as
Contrast         but, yet, however, although, whereas, while, on the other hand, nevertheless, in contrast
Cause            because, since, as, due to, owing to
Result           so, therefore, thus, consequently, as a result, hence
Example          for example, for instance, such as, namely, like
Explanation      in other words, that is, that is to say, to put it simply
Sequence         first, second, next, then, after that, finally, lastly
Conclusion       in conclusion, to sum up, in short, overall
Concession       admittedly, of course, granted, even so
Emphasis         indeed, above all, in fact, especially""", "text", title="Table 1. Discourse markers"),
        T("A marker must match the relation. 'The road was flooded; **however**, we arrived late' is wrong, because there is no contrast: the flood explains the lateness. "
          "The right marker is 'therefore' or 'so'. Ask: is the second idea an addition, a contrast, a result or an example of the first?"),
        H("Cohesive devices"),
        KEY("Grammatical cohesion", "Grammar words that point to other words.", cards=[
            ["Reference", "Pronouns and demonstratives point back or forward: 'Marie sold fish. **She** sold **it** early.' ('She' = Marie, 'it' = fish.) 'This', 'that', 'these', 'those' can refer to a whole idea."],
            ["Substitution", "A word replaces another: 'Choose the red bag or the blue **one**.' 'He said he would help and he did **so**.'"],
            ["Ellipsis", "Words are left out because they are understood: 'Kofi plays football and Ama [plays] netball.'"],
            ["Conjunction", "Links clauses: and, but, because, although."],
        ]),
        KEY("Lexical cohesion", "Vocabulary that links sentences.", cards=[
            ["Repetition", "The same word or its forms: timetable, timetables."],
            ["Synonym", "A word with a similar meaning: task, job, work."],
            ["General word or hyponym", "A general word for a group: 'Maize, cassava and plantain. These **crops**...'"],
            ["Collocation", "Words that go together: revise, exam, paper, mark."],
        ]),
        D("**Redundancy** means words or ideas that repeat meaning that is already there ('return back', 'free gift'). In a passage, redundant parts such as restatements, repetitions and explanations "
          "('in other words, ...') repeat an idea so the reader will not miss it. Spotting them helps you find the main point and remove padding when you summarise.", title="Redundancy"),
        H("The talk"),
        T(PG),
        H("Worked examples"),
        EX("Worked example 1: the job of each marker",
           intro="Say what job each marker does in the talk: 'as a result', 'whereas', 'In other words', 'In addition', 'However', 'Finally'.",
           steps=[
               S("As a result", text="Result: students avoid hard subjects, so they leave them to the last night."),
               S("Whereas", text="Contrast between a huge task ('revise chemistry') and a small one ('forty minutes')."),
               S("In other words", text="Explanation: restates the idea that a timetable makes the task smaller."),
               S("In addition", text="Adds a third benefit, protecting rest."),
               S("However", text="Introduces a limit: a timetable is useful only if realistic."),
               S("Finally", text="Sequence: the last advice."),
           ]),
        EX("Worked example 2: choose the marker",
           intro="'Students who plan breaks concentrate better. ___, they should not stop for too long.' A. Moreover B. However C. Therefore D. For example",
           steps=[
               S("Find the relation", text="The first sentence praises breaks. The second warns about limits: a contrast."),
               S("Test", text="'Moreover' adds a similar idea. 'Therefore' gives a result. 'For example' gives an instance. None fits."),
               S("Answer", text="B. However."),
           ]),
        EX("Worked example 3: what does the word refer to?",
           intro="'Many students revise the topics they enjoy, and as a result they leave the hard ones until the night before the paper.' What does 'ones' stand for? What does 'they' (the second) stand for?",
           steps=[
               S("Substitution", text="'Hard ones' replaces 'hard topics'."),
               S("Reference", text="Both 'they' refer to the 'many students'."),
           ]),
        EX("Worked example 4: lexical cohesion",
           intro="Find words that keep the idea of time and plan in the talk.",
           steps=[
               S("Repetition", text="'Timetable' occurs many times in the talk."),
               S("Related words", text="'Revise', 'study', 'breaks' and 'Sunday' belong to the same area."),
               S("Effect", text="They keep the reader focused on one topic and link the paragraphs."),
           ]),
        MISTAKE("Choosing a marker from its look, not its meaning",
                "'Although' and 'because' can both appear in a sentence about the weather, but they signal opposite relations. Say the two ideas in plain words first, then choose the marker."),
        MISTAKE("Wrong reference",
                "A pronoun refers to the nearest suitable noun that agrees with it. In 'The teacher told the pupil that she was late', 'she' could refer to either person. Check the passage for clues."),
        MISTAKE("Using 'but' and 'although' together",
                "'Although it rained, but we went' is wrong. Use one: 'Although it rained, we went' or 'It rained, but we went.'"),
        QUIZ("'The generator broke down. ___, the shop closed early.' Which marker fits best?",
             ["However", "For example", "As a result", "In contrast"], 2,
             "The breakdown caused the shop to close, so a result marker is needed.",
             hint="Is the second sentence a contrast, an example or a result?",
             feedback=["There is no contrast.", "The second sentence is not an example of the first.", "", "No two things are being compared."]),
        QUIZ("'Kofi bought a bicycle and Ama bought one too.' What does 'one' refer to?",
             ["Kofi", "A bicycle", "The shop", "Ama"], 1,
             "'One' substitutes for 'a bicycle'.",
             hint="What did Ama buy?",
             feedback=["Kofi is a person, but 'one' replaces the thing bought.", "", "The shop is not mentioned.", "Ama is the subject, not the thing bought."]),
        TIP("Paper 1 asks about linking words and reference (for example, 'The word *this* in line 8 refers to...'). In Paper 3 (Summary, Text reconstruction and Editing) you must also use markers to join your own ideas. "
            "The Board's examiners have reported that candidates should be taught transition markers such as first, furthermore, in addition and besides.", title="Exam link"),
        PQ("Which marker shows contrast? (a) moreover (b) whereas (c) consequently (d) for instance",
           "(b) whereas."),
        PQ("Join with a suitable marker: 'The road was muddy. We arrived on time.'",
           "For example: 'The road was muddy; nevertheless, we arrived on time.' (Or 'although the road was muddy, we arrived on time.' Contrast markers.)"),
        PQ("In 'Maize, cassava and plantain are grown here. These crops feed the town', which cohesive device is 'these crops'?",
           "A general word (lexical cohesion). 'Crops' is a general word that sums up the three names."),
        PQ("Explain why 'Although the rain stopped, but the road stayed muddy' is wrong, and correct it.",
           "'Although' and 'but' both mark contrast, so using both is a double link. Correct: 'Although the rain stopped, the road stayed muddy' or 'The rain stopped, but the road stayed muddy.'"),
        SUM("Discourse markers show the relation between ideas: addition, contrast, cause, result, example, explanation, sequence or conclusion.",
            "Choose the marker by the relation between the two ideas, not by its sound.",
            "Cohesion comes from reference (it, they, this), substitution (one, so), ellipsis and from repeated, related or general words.",
            "Redundant restatements are the passage repeating itself; use them to find the main point."),
    ],
))

# ------------------------------------------------------------------ R7. Critical reasoning and evaluation
LESSONS.append(lesson(
    module=M_R,
    topic=T_CRIT,
    title="Evaluating arguments: evidence, fallacies and solutions",
    slug="enl1-critical-reasoning-evaluation",
    minutes=24,
    summary="Break an argument into claim, evidence and reasoning, test the evidence, spot common fallacies, compare two sources and propose a balanced solution to a problem.",
    objectives=[
        "Identify the claim, the evidence and the reasoning in an argument",
        "Judge whether evidence is relevant, enough and reliable",
        "Name common fallacies such as bandwagon, false cause, hasty generalisation and personal attack",
        "Compare two texts and propose a reasoned solution to the problem they discuss",
    ],
    key_concepts=["Claim", "Evidence", "Reasoning", "Fallacy", "Bias", "Synthesis"],
    blocks=[
        H("Introduction"),
        T("A seller says, 'Everyone in town buys this soap, so it must be good.' Should you believe her? Millions of people may buy a bad soap, and 'everyone' is probably an exaggeration. "
          "Critical reasoning is the habit of asking: what is being claimed, what supports it, and does the support really work? "
          "The syllabus asks you to use critical reasoning to evaluate texts, to provide solutions to problems and to bring together information from more than one source."),
        D("An **argument** is a claim supported by reasons and evidence. The **claim** is what the writer wants you to accept. **Evidence** is the facts, examples or expert opinion that support it. "
          "**Reasoning** is the link that explains why the evidence supports the claim.", title="Parts of an argument"),
        KEY("Three tests of evidence", "Ask these questions of any piece of evidence.", cards=[
            ["Relevant?", "Does it concern the claim? A student's football skill does not show that phones help Mathematics."],
            ["Enough?", "Is there enough of it? One story or three students is a weak basis for 'all schools'."],
            ["Reliable?", "Who says it? Do they know the facts? Do they gain by persuading you? Is it a measured fact or an impression?"],
        ]),
        H("Common fallacies"),
        CODE("""Fallacy                What goes wrong                                  Example
Bandwagon              'Everyone does it, so it is right'               'Everybody knows the modern world runs on phones...'
Hasty generalisation   Large claim from too few cases                   'Three students improved, so phones help all'
False cause            'After this, therefore because of this'          'He started the app and his marks rose, so the app did it'
Personal attack        Attacks the person, not the argument             'People who disagree are living in the past'
False dilemma          Pretends only two options exist                  'Either ban phones or lose all discipline'
Appeal to authority    Uses a famous name outside their field            'A footballer says this medicine works'
Emotional appeal       Uses fear or pity in place of evidence           'Think of the poor children!' (with no facts)""", "text", title="Table 1. Fallacies"),
        T("A fallacy means a **weakness in the reasoning**, not that the conclusion is false. A conclusion may be true even if the argument for it is weak."),
        D("**Bias** is a leaning towards one side that makes the writer's presentation unfair, such as leaving out opposing facts or using loaded words. "
          "Everyone has views. Look for **one-sided** evidence and **loaded** language.", title="Bias"),
        H("The two speakers"),
        T(PH),
        H("Worked examples"),
        EX("Worked example 1: claim, evidence, reasoning",
           intro="Break down Speaker 1's argument.",
           steps=[
               S("Claim", text="Phones should be allowed in school."),
               S("Evidence", text="Phones help students look up words and formulas; three students' marks rose after using an app; phones help students call parents; the modern world runs on phones."),
               S("Reasoning", text="Phones are tools, so allowing them helps learning and safety."),
           ]),
        EX("Worked example 2: find the weaknesses in Speaker 1",
           intro="Name two weaknesses in Speaker 1's argument.",
           steps=[
               S("Hasty generalisation / false cause", text="Three students whose marks rose after using an app do not prove that phones improve marks in general, or that the app was the cause."),
               S("Bandwagon / personal attack", text="'Everybody knows' and 'schools that ban them are simply living in the past' use popularity and ridicule in place of evidence."),
               S("Fairness", text="Speaker 1 does not discuss how phones can distract students, which is the other side."),
           ]),
        EX("Worked example 3: compare the two sources",
           intro="Give one similarity and one difference between the speakers.",
           steps=[
               S("Similarity", text="Both rely mainly on personal experience (a class and a brother's school) rather than data, and both admit phones can be useful."),
               S("Difference", text="Speaker 1 stresses learning and safety; Speaker 2 stresses distraction and concentration. Speaker 2 offers an alternative (phoning the school office)."),
           ]),
        EX("Worked example 4: propose a solution",
           intro="Suggest a balanced solution that uses ideas from both speakers.",
           steps=[
               S("Combine the strong points", text="Phones are useful as tools (Speaker 1) but distracting in lessons (Speaker 2)."),
               S("Proposal", text="Phones stay switched off in a bag during lessons, but students may use them in the library for study at set times, and parents may contact the school office in emergencies."),
               S("Support", text="Each part answers a worry raised in the speeches. A trial period with a review would give real evidence."),
           ]),
        MISTAKE("Rejecting a conclusion because the argument is weak",
                "A weak argument does not prove the opposite. Say 'this argument does not prove the claim', not 'the claim is false'."),
        MISTAKE("Treating a personal story as proof",
                "A story about one brother's school or three students is an example, not proof. It becomes strong only when many cases or a measured survey point the same way."),
        MISTAKE("Taking sides in your answer",
                "In an examination you are asked to evaluate, not to say which side you like. Judge the reasoning, using the text."),
        QUIZ("'Our village football team won last year when we wore green shirts, so green shirts bring victory.' This is mostly a",
             ["bandwagon fallacy", "false cause", "personal attack", "false dilemma"], 1,
             "It assumes that because the win followed the shirts, the shirts caused it.",
             hint="What does the speaker say caused the win?",
             feedback=["No appeal to popularity.", "", "No one is attacked.", "No claim that only two options exist."]),
        QUIZ("Which piece of evidence is strongest for 'Homework improves results'?",
             ["My cousin does homework and passes.", "Everyone says it does.", "A survey of 500 students in four schools comparing marks of homework-doing and non-homework-doing classes.", "A famous footballer recommends it."],
             2,
             "A large, varied, measured sample is relevant, plentiful and reliable. The others are an anecdote, the bandwagon, and an unrelated authority.",
             hint="Which is largest, measured and related to the claim?",
             feedback=["One case is not enough.", "'Everyone says' is the bandwagon fallacy.", "", "A footballer is not an authority on school results."]),
        TIP("Paper 1 critical-reasoning questions ask which statement weakens or supports an argument, which piece of evidence is strongest, or what is wrong with a line of reasoning. "
            "The Board also expects candidates to give solutions to a problem and bring together ideas from more than one text, so practise comparing short passages.", title="Exam link"),
        PQ("Name the fallacy in 'Don't listen to her suggestion; she failed Mathematics last year.'",
           "Personal attack (ad hominem): it attacks the person rather than the suggestion."),
        PQ("Which would weaken Speaker 2's argument most? (a) a survey showing students with phones in class scored higher (b) a statement that phones are expensive (c) a statement that school offices have telephones",
           "(a). It gives direct evidence against the claim that phones harm concentration. (b) and (c) do not touch the claim."),
        PQ("In two sentences, say which speaker's evidence is stronger and why.",
           "Neither is strong, because both depend on personal stories and a small number of cases. Speaker 2's alternative for emergencies (the school office) answers one of Speaker 1's points, so on that issue Speaker 2 is stronger; "
           "Speaker 1's example of improved marks is hasty, since three students are not enough to show the app was the cause."),
        PQ("A town has a problem: litter in the market. Suggest two solutions and say who must act.",
           "For example: (1) put bins near each section, with the council emptying them every day; (2) the traders' association fines or warns stallholders who leave rubbish and educates customers. (Any two reasonable solutions with actors.)"),
        SUM("Break an argument into claim, evidence and reasoning, then test the evidence for relevance, sufficiency and reliability.",
            "Learn the common fallacies: bandwagon, hasty generalisation, false cause, personal attack, false dilemma, authority and emotion.",
            "A weak argument does not make a conclusion false; and one-sided evidence or loaded words suggest bias.",
            "To compare sources, note similarities and differences; to solve a problem, combine strong points from each."),
    ],
))


# ------------------------------------------------------------------ S1. Vowel sounds
LESSONS.append(lesson(
    module=M_S,
    topic=T_SOUNDS,
    title="English vowel sounds: monophthongs, diphthongs and triphthongs",
    slug="enl1-vowel-sounds-rp",
    minutes=25,
    summary="British English has twelve pure vowels, eight diphthongs and five triphthongs. Learn how to tell vowel sounds from vowel letters, how each vowel is made, and how to avoid the most common confusions.",
    objectives=[
        "Distinguish vowel sounds from vowel letters, and vowel sounds from consonant sounds",
        "Name the twelve pure vowels, eight diphthongs and five triphthongs with a keyword for each",
        "Describe a vowel by tongue height, tongue position, lip shape and length",
        "Recognise the main contrasts that cause misunderstanding, using minimal pairs",
    ],
    key_concepts=["Vowel sound", "Monophthong", "Diphthong", "Triphthong", "Schwa", "Minimal pair"],
    blocks=[
        H("Introduction"),
        T("Look at the first sound of these words: 'hour', 'university', 'one', 'honest'. Only one of them begins with a vowel **letter** and a vowel **sound**, and that is 'hour'. "
          "'University' begins with the consonant sound /j/, 'one' with /w/, and 'honest' begins with the vowel sound /ɒ/ because the letter h is silent. "
          "This is why we say 'an hour' and 'an honest man' but 'a university' and 'a one-way street'. The sound, not the spelling, decides."),
        T("Speech work is Section B of Paper 1: ten multiple-choice questions on sounds, stress and intonation. This lesson builds the foundation, which is a clear map of the vowel sounds. "
          "We use the standard British pronunciation known as Received Pronunciation (RP) that most dictionaries record. It is a reference accent, not a better or worse one; "
          "your own accent is a valuable part of who you are, and the examination uses the reference system."),
        T(NOAUDIO),
        D("A **vowel sound** is a speech sound made with the air flowing freely through the mouth, with no blockage and no friction. A **consonant sound** is made with some blockage or narrowing. "
          "Vowel and consonant **letters** are a different matter: English has five vowel letters (a, e, i, o, u, and sometimes y) but about twenty vowel sounds.", title="Vowel sound and consonant sound"),
        D("A **monophthong** (pure vowel) stays steady from start to finish. A **diphthong** glides from one vowel to another within one syllable. A **triphthong** glides through three vowel positions "
          "(a diphthong plus schwa). Each counts as one syllable.", title="Monophthong, diphthong and triphthong"),
        H("Describing a vowel"),
        KEY("Four questions", "Every vowel can be described like this.", cards=[
            ["Tongue height", "Close (high, mouth nearly shut): /iː/, /uː/. Open (low, mouth wide): /æ/, /ɑː/."],
            ["Tongue position", "Front (towards the teeth): /iː/, /e/. Back (towards the throat): /uː/, /ɔː/. Central: /ə/, /ɜː/."],
            ["Lips", "Spread for front vowels such as /iː/. Rounded for back vowels such as /uː/ and /ɔː/."],
            ["Length", "Long vowels are marked with a colon-like sign /ː/ and are held longer."],
        ]),
        IMG("al-enl1-vowel-chart.svg",
            alt="A vowel chart shaped like a four-sided figure. Close vowels are at the top and open vowels at the bottom; front vowels on the left and back vowels on the right. Twelve pure vowels are placed at their approximate positions, each with a keyword.",
            caption="Figure 1. The twelve pure vowels of British English (approximate positions). Short vowels are in blue and long vowels in green."),
        H("The twelve pure vowels"),
        CODE("""Symbol  Keyword  More examples
/iː/    fleece   see, key, me, meat, receive
/ɪ/     kit      sit, women, busy, village
/e/     dress    bed, said, many, friend, head
/æ/     trap     cat, hand, stand, black
/ɑː/    bath     father, car, calm, laugh, bath (check your dictionary)
/ɒ/     lot      hot, want, watch, because
/ɔː/    thought  law, door, four, water, all
/ʊ/     foot     put, good, could, woman
/uː/    goose    food, blue, two, move, you
/ʌ/     strut    cup, love, son, blood, country
/ɜː/    nurse    bird, turn, work, learn, first
/ə/     schwa    about, teacher, today, doctor""", "text", title="Table 1. The twelve pure vowels (a keyword is a word that stands for a whole set)"),
        T("**Schwa /ə/** is the weakest vowel and the most common sound in English. It occurs only in **unstressed** syllables and can be spelled in many ways: a in 'about', er in 'teacher', or in 'doctor', ou in 'famous', "
          "e in 'taken'. When you say 'banana' /bəˈnɑːnə/, the first and last syllables are schwa."),
        T("Notice that RP is **non-rhotic**: the letter r is not pronounced unless a vowel sound follows it. So 'teacher' is /ˈtiːtʃə/, 'car' is /kɑː/ and 'bird' is /bɜːd/. "
          "Many accents of English pronounce the r everywhere, and both are understood."),
        T("**'Bath' words.** In RP, words such as 'bath', 'laugh', 'ask' and 'dance' have /ɑː/. Some varieties of British English use /æ/. Check your dictionary and be consistent."),
        H("The eight diphthongs"),
        CODE("""Symbol  Keyword  More examples
/eɪ/    face     day, make, rain, eight, they
/aɪ/    price    my, time, high, eye, buy
/ɔɪ/    choice   boy, coin, toy, join
/əʊ/    goat     go, home, boat, know, though
/aʊ/    mouth    now, house, out, brown
/ɪə/    near     here, ear, idea, beer
/eə/    square   air, care, there, bear, where
/ʊə/    cure     poor, tour, pure (check your dictionary: many speakers say /pɔː/, /tɔː/)""", "text", title="Table 2. The eight diphthongs"),
        T("Three of them end in schwa and are called **centring diphthongs**: /ɪə/, /eə/, /ʊə/. The other five glide towards /ɪ/ (closing to /ɪ/: /eɪ/, /aɪ/, /ɔɪ/) or towards /ʊ/ (/əʊ/, /aʊ/)."),
        T("**Triphthongs** are diphthongs plus schwa: /eɪə/ in 'player', /aɪə/ in 'fire', /ɔɪə/ in 'royal', /əʊə/ in 'lower' and /aʊə/ in 'hour'. In quick speech the middle glide is often smoothed, "
          "so that 'fire' sounds like /faə/. For the examination, treat them as a syllable with a diphthong plus schwa; a dictionary will show them either way."),
        H("Worked examples"),
        EX("Worked example 1: vowel sound or consonant sound at the beginning?",
           intro="Choose the correct article, a or an: ___ umbrella, ___ university, ___ hour, ___ European.",
           steps=[
               S("Say the first sound", text="'Umbrella' begins /ʌ/ (vowel). 'University' begins /j/ (consonant). 'Hour' begins /aʊ/ (vowel; h is silent). 'European' begins /j/ (consonant)."),
               S("Apply the rule", text="Use 'an' before a vowel sound and 'a' before a consonant sound."),
               S("Answer", text="an umbrella, a university, an hour, a European."),
           ]),
        EX("Worked example 2: choose the word with the same vowel",
           intro="Which word has the same vowel as 'bird'? A. bed B. work C. board D. beard",
           steps=[
               S("Find the vowel", text="'Bird' is /bɜːd/. The vowel is /ɜː/."),
               S("Say each option", text="bed /bed/, work /wɜːk/, board /bɔːd/, beard /bɪəd/."),
               S("Compare", text="Only 'work' has /ɜː/. The spelling is different (or, not ir), but the sound is the same."),
               S("Answer", text="B."),
           ]),
        EX("Worked example 3: minimal pairs",
           intro="Why do 'ship' and 'sheep' sound different, and what is the difference?",
           steps=[
               S("Transcribe", text="'Ship' is /ʃɪp/. 'Sheep' is /ʃiːp/."),
               S("Describe the difference", text="/ɪ/ is short and relaxed; /iː/ is longer, with the tongue higher and the lips more spread."),
               S("Name the contrast", text="They form a minimal pair, two words that differ in one sound only, and a listener depends on that sound to know which word you mean."),
           ]),
        EX("Worked example 4: count the syllables and vowel sounds",
           intro="How many syllables and vowel sounds are in 'family' /ˈfæməli/?",
           steps=[
               S("Syllables", text="fam-i-ly: three."),
               S("Vowel sounds", text="/æ/, /ə/ and /i/: one in each syllable."),
               S("Letters", text="The vowel letters are a, i and y. Here the letters and the sounds happen to match in number, but the sounds /ə/ and /i/ are spelled i and y, which you cannot guess from the letters alone."),
           ]),
        MISTAKE("Trusting the letter",
                "The letter u is /ʌ/ in 'cut' and /ʊ/ in 'put'; the letter o is /ʌ/ in 'son', /ɒ/ in 'gone' and /uː/ in 'do'. Say the word aloud and compare it with a keyword."),
        MISTAKE("Saying every vowel at full strength",
                "Unstressed syllables use schwa. 'Teacher' is /ˈtiːtʃə/, not 'tee-chair', and 'banana' begins /bə-/, not /bæ-/."),
        MISTAKE("Merging pairs that must stay apart",
                "Many learners need extra practice with /ɪ/ and /iː/ (ship, sheep), /ʌ/ and /ɒ/ (cup, cop), /æ/ and /e/ (man, men), and /ɜː/ and /ɔː/ (bird, board). "
                "If two words sound the same when you say them, practise the pair slowly with a good speaker."),
        QUIZ("Which word has a different vowel sound from the others?",
             ["love", "son", "come", "gone"], 3,
             "'Gone' is /ɡɒn/ with /ɒ/. 'Love', 'son' and 'come' all have /ʌ/.",
             hint="Say each word and compare it with 'strut'.",
             feedback=["'Love' is /lʌv/.", "'Son' is /sʌn/.", "'Come' is /kʌm/.", ""]),
        QUIZ("The word 'hour' begins with",
             ["a consonant sound", "a vowel sound", "the sound /h/", "the sound /w/"], 1,
             "The letter h is silent and the word begins with the diphthong /aʊ/ (or /aʊə/): 'an hour'.",
             hint="Which article do we use with 'hour'?",
             feedback=["The first sound is not a consonant.", "", "The h is silent in this word.", "There is no /w/ sound."]),
        TIP("Section B of Paper 1 asks which word has the same vowel as another, which word is the odd one out, how many syllables or vowel sounds a word has, and which option shows the correct transcription. "
            "The keywords in Table 1 are your best tool: say the keyword, then say each option.", title="Exam link"),
        PQ("Write the keyword vowel for each word: (a) boat (b) bird (c) boy (d) bear.",
           "(a) boat: /əʊ/ (goat). (b) bird: /ɜː/ (nurse). (c) boy: /ɔɪ/ (choice). (d) bear: /eə/ (square)."),
        PQ("Give one minimal pair for each contrast: (a) /ɪ/ and /e/ (b) /æ/ and /e/ (c) /ʌ/ and /ɒ/.",
           "(a) bit and bet (b) man and men (c) cup and cop (also cut and cot). Any valid pair is accepted."),
        PQ("Explain why we say 'a university' but 'an umbrella'.",
           "The article depends on the first sound, not the first letter. 'University' begins with the consonant sound /j/, so we use 'a'. 'Umbrella' begins with the vowel sound /ʌ/, so we use 'an'."),
        PQ("Which of these contains a triphthong? A. boy B. hour C. door D. beer",
           "B. 'Hour' is /ˈaʊə/ (diphthong /aʊ/ plus schwa). 'Boy' is a diphthong /bɔɪ/, 'door' has the pure vowel /ɔː/ and 'beer' has the centring diphthong /ɪə/."),
        SUM("Sound, not spelling, decides whether a word begins with a vowel or consonant: an hour, a university.",
            "British English has twelve pure vowels, eight diphthongs and five triphthongs; learn them by keyword.",
            "Vowels are described by tongue height, tongue position, lip shape and length; schwa is the weak vowel of unstressed syllables.",
            "Practise the pairs that cause misunderstanding, and write 'check your dictionary' where books differ."),
    ],
))

# ------------------------------------------------------------------ S2. Consonant sounds
LESSONS.append(lesson(
    module=M_S,
    topic=T_SOUNDS,
    title="English consonant sounds: voicing, place and manner",
    slug="enl1-consonant-sounds-rp",
    minutes=24,
    summary="English has twenty-four consonant sounds. Learn them by voicing, place and manner, the rules for the endings -s and -ed, and the spelling traps that make letters and sounds disagree.",
    objectives=[
        "Name the 24 consonant sounds and give a keyword for each",
        "Tell voiced from voiceless consonants and describe place and manner of articulation",
        "Apply the pronunciation rules for -s and -ed endings",
        "Avoid spelling traps such as ch, gh, c, g, x and silent letters",
    ],
    key_concepts=["Voiced and voiceless", "Place of articulation", "Manner of articulation", "Plosive", "Fricative", "Affricate"],
    blocks=[
        H("Introduction"),
        T("A teacher in Limbe writes 'think' and 'sink' on the board and asks the class to say them. Some say the same word twice. "
          "The two words differ in one consonant, /θ/ and /s/, but that one sound changes the meaning. English has twenty-four consonant sounds, and the consonants carry much of the information in a word. "
          "This lesson gives you a clear map of them."),
        T(NOAUDIO),
        D("A consonant is described by three features: **voicing** (are the vocal folds vibrating?), **place** (where in the mouth the air is blocked or narrowed) and **manner** (how it is blocked or narrowed).", title="Describing a consonant"),
        KEY("Voicing test", "Put two fingers on your throat. Say a long /sss/ and then a long /zzz/.", cards=[
            ["Voiceless", "No vibration: /p t k f θ s ʃ h tʃ/"],
            ["Voiced", "You feel a buzz: /b d ɡ v ð z ʒ dʒ m n ŋ l r j w/"],
        ]),
        H("The 24 consonants"),
        CODE("""Manner            Voiceless / Voiced pairs and others
Plosives          p b    t d    k ɡ
Affricates        tʃ dʒ
Fricatives        f v    θ ð    s z    ʃ ʒ    h
Nasals            m      n      ŋ
Approximants      l   r   j   w""", "text", title="Table 1. Consonants by manner"),
        CODE("""Place            Sounds
Bilabial         p b m w         (both lips)
Labiodental      f v             (lower lip and upper teeth)
Dental           θ ð             (tongue tip between or behind teeth)
Alveolar         t d s z n l     (tongue tip on the ridge behind the upper teeth)
Post-alveolar    ʃ ʒ tʃ dʒ r     (just behind the ridge)
Palatal          j               (front of the tongue to the hard palate)
Velar            k ɡ ŋ           (back of the tongue to the soft palate)
Glottal          h               (the glottis, in the throat)""", "text", title="Table 2. Consonants by place"),
        CODE("""Symbol  Keyword  Examples
/p/ /b/   pen, ben    pat, bat, cap, cab
/t/ /d/   tea, day    ten, den, cat, bed
/k/ /ɡ/   key, go     cat, gat, back, bag
/tʃ/ /dʒ/ church, judge  chip, jeep, watch, bridge
/f/ /v/   fan, van    safe, save
/θ/ /ð/   thin, this  think, those, bath, bathe
/s/ /z/   sip, zip    face, phase
/ʃ/ /ʒ/   ship, vision  sure, pleasure, measure
/h/       hat         hello, behind
/m/ /n/ /ŋ/   man, no, sing   some, sun, song
/l/ /r/   leg, red    lamp, rain
/j/ /w/   yes, we     young, one""", "text", title="Table 3. Keywords"),
        T("**/ŋ/** is one sound spelled with two letters. It never begins an English word. 'Sing' is /sɪŋ/ (no /ɡ/ at the end), 'singer' is /ˈsɪŋə/, but 'finger' is /ˈfɪŋɡə/ with /ŋɡ/. "
          "**/θ/ and /ð/** are made with the tongue tip between or just behind the teeth. /θ/ is voiceless ('thin') and /ð/ is voiced ('this'). "
          "Learners who replace them with /t/, /d/, /s/ or /z/ are often still understood, but the sounds are in the standard system and examinations use them."),
        H("Endings: -s and -ed"),
        D("**Plural, third person -s:** pronounced /s/ after voiceless sounds (cats /kæts/, books /bʊks/), /z/ after voiced sounds and vowels (dogs /dɒɡz/, plays /pleɪz/), and /ɪz/ after /s z ʃ ʒ tʃ dʒ/ (buses /ˈbʌsɪz/, wishes /ˈwɪʃɪz/, judges /ˈdʒʌdʒɪz/).",
          title="The -s rule"),
        D("**Past tense -ed:** pronounced /t/ after voiceless sounds (walked /wɔːkt/, watched /wɒtʃt/), /d/ after voiced sounds and vowels (played /pleɪd/, loved /lʌvd/), and /ɪd/ after /t/ or /d/ (wanted /ˈwɒntɪd/, needed /ˈniːdɪd/).",
          title="The -ed rule"),
        T("The spelling does not change, but the sound does. Look at the sound **before** the ending, not at the letter."),
        H("Spelling traps"),
        CODE("""Letters   Possible sounds
ch        /tʃ/ church   /k/ school   /ʃ/ chef
c         /k/ cat       /s/ city
g         /ɡ/ go        /dʒ/ giant
s         /s/ sit       /z/ is, rose   /ʃ/ sure   /ʒ/ measure
x         /ks/ box      /ɡz/ exam
gh        silent in night, /f/ in laugh, /ɡ/ in ghost
th        /θ/ thin      /ð/ this
Silent letters: knife, write, gnat, psychology, lamb, honest, hour, island, castle, listen""", "text", title="Table 4. One letter, many sounds"),
        H("Worked examples"),
        EX("Worked example 1: pronounce the -s ending",
           intro="How is the ending pronounced in: cabs, maps, buses?",
           steps=[
               S("cabs", text="The sound before is /b/ (voiced), so the ending is /z/: /kæbz/."),
               S("maps", text="The sound before is /p/ (voiceless), so the ending is /s/: /mæps/."),
               S("buses", text="The sound before is /s/ (a sibilant), so the ending is /ɪz/: /ˈbʌsɪz/, a new syllable."),
           ]),
        EX("Worked example 2: pronounce the -ed ending",
           intro="Say the ending in: stopped, raised, visited, laughed.",
           steps=[
               S("stopped", text="After voiceless /p/: /t/. /stɒpt/."),
               S("raised", text="After voiced /z/: /d/. /reɪzd/."),
               S("visited", text="After /t/: /ɪd/. /ˈvɪzɪtɪd/, with one extra syllable."),
               S("laughed", text="After voiceless /f/: /t/. /lɑːft/."),
           ]),
        EX("Worked example 3: find the voiced partner",
           intro="Which word contains the voiced partner of the consonant at the start of 'ship'? A. chip B. vision C. judge D. yes",
           steps=[
               S("'Ship' begins /ʃ/", text="A voiceless post-alveolar fricative."),
               S("Voiced partner", text="/ʒ/, as in 'measure', 'pleasure' and 'vision'. It almost never begins an English word."),
               S("Check the options", text="'Chip' begins /tʃ/ (voiceless), 'judge' begins and ends with /dʒ/ and 'yes' begins with /j/. Only 'vision' /ˈvɪʒən/ contains /ʒ/."),
               S("Answer", text="B."),
           ]),
        EX("Worked example 4: how many consonant sounds?",
           intro="How many consonant SOUNDS are in 'church' /tʃɜːtʃ/ and in 'box' /bɒks/?",
           steps=[
               S("church", text="/tʃ/ + vowel + /tʃ/: two consonant sounds (although there are five consonant letters c, h, r, c, h)."),
               S("box", text="/b/, /k/, /s/: three consonant sounds from two consonant letters (x is two sounds)."),
           ]),
        MISTAKE("Counting letters as sounds",
                "'Thought' has seven letters but only three sounds: /θ/, /ɔː/, /t/. Always count sounds, not letters."),
        MISTAKE("Adding /ɡ/ to /ŋ/",
                "In 'sing', 'long' and 'bring' the ending is the single sound /ŋ/. Do not pronounce a /ɡ/ after it, except in words like 'finger' and 'longer' /ˈlɒŋɡə/."),
        MISTAKE("Saying every -ed as a separate syllable",
                "Only after /t/ or /d/ does -ed add a syllable (wanted, needed). In 'walked' and 'played' it is part of the same syllable."),
        QUIZ("How is the final -s pronounced in 'books'?",
             ["/s/", "/z/", "/ɪz/", "It is not pronounced"], 0,
             "The sound before is /k/ (voiceless), so the ending is /s/: /bʊks/.",
             hint="Is the sound before the s voiced or voiceless?",
             feedback=["", "/z/ follows voiced sounds, such as the /ɡ/ in 'bags'.", "/ɪz/ follows /s z ʃ ʒ tʃ dʒ/.", "The ending is always pronounced."]),
        QUIZ("The -ed in 'wanted' is pronounced",
             ["/t/", "/d/", "/ɪd/", "/ed/"], 2,
             "After /t/ the ending is /ɪd/: /ˈwɒntɪd/.",
             hint="What is the sound just before the ending?",
             feedback=["/t/ follows other voiceless sounds, such as /k/ in 'walked'.", "/d/ follows voiced sounds, such as /l/ in 'called'.", "", "The vowel is /ɪ/, not /e/."]),
        TIP("In Paper 1 you may be asked which word has a different final sound, which word has the same beginning consonant, or whether a letter is silent. "
            "The voiced/voiceless test and the -s and -ed rules cover many of those questions.", title="Exam link"),
        PQ("Sort into /s/, /z/ and /ɪz/: cats, dogs, houses (plural), dishes, plays, books.",
           "/s/: cats, books. /z/: dogs, plays. /ɪz/: houses, dishes."),
        PQ("Write the pronunciation of the -ed ending: asked, loved, ended, wished.",
           "asked /ɑːskt/ (/t/); loved /lʌvd/ (/d/); ended /ˈendɪd/ (/ɪd/); wished /wɪʃt/ (/t/)."),
        PQ("Name the voiced partner of each: /p/, /f/, /s/, /tʃ/.",
           "/p/ pairs with /b/; /f/ with /v/; /s/ with /z/; /tʃ/ with /dʒ/."),
        PQ("Give the number of consonant sounds in 'thought' and in 'singer'.",
           "'Thought' /θɔːt/: two consonant sounds (/θ/ and /t/). 'Singer' /ˈsɪŋə/: two consonant sounds (/s/ and /ŋ/)."),
        SUM("English has 24 consonant sounds, described by voicing, place and manner.",
            "Use the voicing test: a buzz in the throat means voiced.",
            "Plural and third-person -s is /s/, /z/ or /ɪz/; past -ed is /t/, /d/ or /ɪd/ depending on the last sound of the word.",
            "Count sounds, not letters, and remember that one letter may have several sounds."),
    ],
))


# ------------------------------------------------------------------ S3. Phonemic transcription
LESSONS.append(lesson(
    module=M_S,
    topic=T_TRANS,
    title="Phonemic transcription: writing and reading sounds",
    slug="enl1-phonemic-transcription",
    minutes=25,
    summary="Phonemic transcription writes the sounds of a word with IPA symbols between slashes. Learn the conventions, a six-step method, and how to read a transcription back into a word.",
    objectives=[
        "Explain what phonemic transcription is and why spelling cannot replace it",
        "Transcribe common words and short phrases into British English IPA",
        "Mark primary stress correctly",
        "Read a transcription and say which word it represents",
    ],
    key_concepts=["Phoneme", "Transcription", "IPA", "Stress mark", "Non-rhotic", "Citation form"],
    blocks=[
        H("Introduction"),
        T("A visitor to Douala asks how to say the name of a new friend. You could write it in spelling, but spelling is a poor guide: 'though', 'through', 'tough' and 'thought' share most letters and almost no sounds. "
          "Dictionaries solve this with a special alphabet, the **International Phonetic Alphabet (IPA)**, where each symbol stands for exactly one sound. "
          "The syllabus asks you to do phonemic transcription well, and Section B of Paper 1 often shows a transcription and asks you to choose the right word or the correct transcription."),
        T(NOAUDIO),
        D("A **phoneme** is the smallest sound unit that can change the meaning of a word. 'Pat' and 'bat' differ in one phoneme (/p/ and /b/). "
          "A **phonemic transcription** writes each phoneme of a word or phrase with one symbol between slashes: pat is /pæt/.", title="Phoneme and transcription"),
        H("Conventions"),
        KEY("Rules for writing transcription", "Follow these exactly in the examination.", cards=[
            ["Slashes", "Write the transcription between slashes: /kæt/."],
            ["One symbol, one sound", "Write sounds, not letters. 'Knife' is /naɪf/ and has no /k/. The symbol ː (as in /iː/) belongs to the vowel symbol."],
            ["No capital letters, no punctuation", "Even the first word of a sentence and names are written in lower-case symbols. Spaces separate words."],
            ["Stress mark", "Put ˈ at the start of the syllable that carries primary stress, in words of two or more syllables: /ˈtiːtʃə/. A lower mark ˌ shows secondary stress."],
            ["RP is non-rhotic", "Write /r/ only when a vowel sound follows it. 'Car' is /kɑː/ but 'red' is /red/ and 'very' is /ˈveri/."],
        ]),
        CODE("""Consonants      p b t d k ɡ  tʃ dʒ  f v θ ð s z ʃ ʒ h  m n ŋ  l r j w
Short vowels    ɪ e æ ʌ ɒ ʊ ə
Long vowels     iː ɑː ɔː uː ɜː
Diphthongs      eɪ aɪ ɔɪ əʊ aʊ ɪə eə ʊə""", "text", title="Table 1. The symbols you need (RP)"),
        T("Use /ɡ/ for the sound in 'go' (the single-storey g, not a looped letter that may be read as another symbol), /j/ for the sound in 'yes' (not /y/), and /dʒ/ for the sound in 'judge'. "
          "Note that /j/ is not the letter j."),
        H("A six-step method"),
        KEY("How to transcribe a word", "Do these in order.", cards=[
            ["1. Say it", "Say the word slowly and naturally. Do not look at the spelling."],
            ["2. Count syllables", "Each vowel sound (including diphthongs) is one syllable."],
            ["3. Find the stress", "Which syllable is the strongest? Put ˈ before it."],
            ["4. Write each sound", "Match each sound to a symbol using your keywords."],
            ["5. Check the endings", "-s is /s/, /z/ or /ɪz/; -ed is /t/, /d/ or /ɪd/."],
            ["6. Read it back", "Say your transcription aloud. Does it match the word?"],
        ]),
        T("In unstressed syllables, most dictionaries show the weak vowel /ə/ or /ɪ/. The ending of words like 'little' or 'garden' is written /ˈlɪtl/ or /ˈlɪtəl/, /ˈɡɑːdn/ or /ˈɡɑːdən/ depending on the dictionary. "
          "In this course we write the schwa (/əl/, /ən/) form. Check your dictionary and follow your teacher's convention."),
        T("The ending -y at the end of 'happy' is shown as /i/ in most dictionaries (/ˈhæpi/); some write /ɪ/. Check your dictionary."),
        H("Worked examples"),
        EX("Worked example 1: transcribe a word with silent letters",
           intro="Transcribe 'knowledge' (British English).",
           steps=[
               S("Say it", text="Two syllables, stress on the first: NOL-ij."),
               S("Sounds", text="k is silent, so the first sound is /n/. The vowel is /ɒ/. Then /l/, then the weak vowel /ɪ/, then /dʒ/ (spelled dge)."),
               S("Write", text="/ˈnɒlɪdʒ/"),
           ]),
        EX("Worked example 2: transcribe a word with a diphthong and -ed",
           intro="Transcribe 'played' and 'wanted'.",
           steps=[
               S("played", text="/p/ + /l/ + the diphthong /eɪ/ + the voiced ending /d/ (after a vowel): /pleɪd/."),
               S("wanted", text="Stress on the first syllable. /w/ + /ɒ/ + /n/ + /t/, then -ed after /t/ is /ɪd/: /ˈwɒntɪd/."),
           ]),
        EX("Worked example 3: transcribe a phrase",
           intro="Transcribe 'the boys played football' as it would appear in a dictionary-style list of words.",
           steps=[
               S("the", text="/ðə/ (the weak form before a consonant)."),
               S("boys", text="/bɔɪz/: diphthong /ɔɪ/ + the voiced ending /z/."),
               S("played", text="/pleɪd/."),
               S("football", text="Compound, stress on the first part: /ˈfʊtbɔːl/."),
               S("Whole", text="/ðə bɔɪz pleɪd ˈfʊtbɔːl/ (no capital letters, no full stop)."),
           ]),
        EX("Worked example 4: read a transcription",
           intro="Which word is /ˈkɒlɪdʒ/? Which is /ˈwenzdeɪ/? Which is /ˈsʌmə/?",
           steps=[
               S("/ˈkɒlɪdʒ/", text="/k/ + /ɒ/ + /l/ + /ɪ/ + /dʒ/ = college."),
               S("/ˈwenzdeɪ/", text="/w/ + /e/ + /n/ + /z/ + /d/ + /eɪ/ = Wednesday (some speakers say /ˈwenzdi/: check your dictionary)."),
               S("/ˈsʌmə/", text="The ending is schwa, so the r in the spelling is silent: summer."),
           ]),
        CODE("""Word        Transcription      Note
thought     /θɔːt/             3 sounds, 7 letters
through     /θruː/
though      /ðəʊ/
tough       /tʌf/
cough       /kɒf/
church      /tʃɜːtʃ/
queen       /kwiːn/            qu = /kw/
exam        /ɪɡˈzæm/           x = /ɡz/
science     /ˈsaɪəns/          2 syllables (sci-ence)
honest      /ˈɒnɪst/           h silent
women       /ˈwɪmɪn/           plural of woman /ˈwʊmən/
school      /skuːl/            ch = /k/
bought      /bɔːt/
laugh       /lɑːf/             check your dictionary (/læf/ in some accents)
measure     /ˈmeʒə/
finger      /ˈfɪŋɡə/           ŋ + ɡ
singer      /ˈsɪŋə/            ŋ only""", "text", title="Table 2. Useful models"),
        MISTAKE("Transcribing the spelling",
                "A candidate who writes /nɪf/ for 'knife' has copied the letters. Transcribe what you hear: /naɪf/."),
        MISTAKE("Forgetting length and diphthongs",
                "/ɪ/ and /iː/, /ɒ/ and /ɔː/ are different symbols. Dropping the ː turns 'sheep' /ʃiːp/ into 'ship' /ʃɪp/. Write the full diphthong, for example /eɪ/ for 'play', not /e/."),
        MISTAKE("Using spelling punctuation or capitals",
                "Do not write capital letters, hyphens, apostrophes or full stops inside a transcription. A stress mark goes before the stressed syllable, not after the vowel."),
        QUIZ("Which is the correct transcription of 'cheap'?",
             ["/ʃiːp/", "/tʃiːp/", "/tʃɪp/", "/dʒiːp/"], 1,
             "'Cheap' begins with the affricate /tʃ/ and has the long vowel /iː/: /tʃiːp/.",
             hint="Which consonant begins 'chair' and 'church'?",
             feedback=["That is 'sheep'.", "", "That is 'chip'; the vowel is short.", "That is 'jeep'."]),
        QUIZ("How many sounds are in the word 'night' /naɪt/?",
             ["5", "4", "3", "2"], 2,
             "/n/, /aɪ/ and /t/. The letters gh are silent and the letter i is part of the diphthong.",
             hint="Count the symbols in the transcription, not the letters.",
             feedback=["That counts the letters.", "That counts a diphthong as two sounds.", "", "One sound is missing."]),
        TIP("Paper 1 shows a transcription and asks for the word or shows a word and asks for the correct transcription. Eliminate options by checking one thing at a time: the first consonant, the vowel, "
            "the last consonant, then the stress mark.", title="Exam link"),
        PQ("Transcribe: (a) ship (b) sheep (c) think (d) judge.",
           "(a) /ʃɪp/ (b) /ʃiːp/ (c) /θɪŋk/ (d) /dʒʌdʒ/."),
        PQ("Write the words for: (a) /ˈbɪzi/ (b) /θruː/ (c) /kɒf/ (d) /ˈwɪmɪn/.",
           "(a) busy (b) through (c) cough (d) women."),
        PQ("A student writes /sɪŋɡ/ for 'sing'. What is the mistake and what is correct?",
           "The student added /ɡ/ after /ŋ/ because of the spelling ng. The word has the single sound /ŋ/ at the end: /sɪŋ/."),
        PQ("Transcribe 'The cat sat on the mat' as separate words with no capitals.",
           "/ðə kæt sæt ɒn ðə mæt/ (the weak form /ðə/ before a consonant). Some teachers show the stressed words with ˈ; follow the convention in your dictionary or class."),
        SUM("Transcription writes sounds, not letters, between slashes, with no capitals or punctuation.",
            "Use the six steps: say, count syllables, find stress, write sounds, check endings, read back.",
            "RP is non-rhotic: write /r/ only before a vowel sound. Watch length marks, diphthongs and silent letters.",
            "Where dictionaries differ (happy, little, laugh), write 'check your dictionary' and be consistent."),
    ],
))

# ------------------------------------------------------------------ S4. Word stress
LESSONS.append(lesson(
    module=M_S,
    topic=T_STRESS,
    title="Word stress: rules and patterns",
    slug="enl1-word-stress-rules",
    minutes=24,
    summary="Every English word of two or more syllables has one strongest syllable. Learn the main rules for nouns, verbs, suffixes and compounds, and see how stress changes the meaning and the vowels of a word.",
    objectives=[
        "Explain what word stress is and how a stressed syllable differs from an unstressed one",
        "Apply the rules for two-syllable words, noun-verb pairs, suffixes and compounds",
        "Mark primary stress in a word and predict the vowel weakening that follows",
        "Say when a rule has exceptions or when dictionaries differ",
    ],
    key_concepts=["Syllable", "Primary stress", "Secondary stress", "Weak vowel", "Compound", "Stress shift"],
    blocks=[
        H("Introduction"),
        T("Say 'photograph', 'photographer' and 'photographic' aloud. The strongest syllable moves: PHO-to-graph, pho-TOG-ra-pher, pho-to-GRAPH-ic. "
          "When the stress moves, the vowels also change. In English, stress is part of the word, like its letters, and a word said with the wrong stress can be hard to recognise. "
          "The syllabus asks for work on word stress, and Section B of Paper 1 tests it directly."),
        T(NOAUDIO),
        D("A **syllable** is a unit of sound that has one vowel sound (a pure vowel, diphthong or triphthong), possibly with consonants around it. "
          "'Teacher' has two syllables, 'banana' three and 'photographer' four.", title="Syllable"),
        D("**Word stress** is the extra prominence given to one syllable in a word. A stressed syllable is **louder, longer, higher in pitch and clearer** than the others. "
          "**Primary stress** is the strongest; **secondary stress** is a weaker prominence in longer words. In a transcription primary stress is ˈ and secondary is ˌ.", title="Word stress"),
        T("In this lesson, capital letters show the stressed syllable: beGIN. Remember that one-syllable words have no word stress; their prominence depends on the sentence."),
        H("The main rules"),
        CODE("""Rule 1  Two-syllable nouns and adjectives: stress the FIRST syllable
        TEAcher, TAble, PRETty, CLEver, HAPpy
        Exceptions: hoTEL, poLICE, maCHINE, guiTAR (nouns); aLONE, aSLEEP (adjectives)

Rule 2  Two-syllable verbs: stress the SECOND syllable
        beGIN, deCIDE, reLAX, aGREE, forGET, preFER
        Exceptions (weak second syllable): ENter, OPen, VISit, ANswer, SUFfer

Rule 3  Noun-verb pairs: noun first, verb second
        REcord (n) / reCORD (v)    PREsent / preSENT    IMport / imPORT
        OBject / obJECT            INcrease / inCREASE  PERmit / perMIT
        Note the vowel changes: DEsert (n) /ˈdezət/, deSERT (v) /dɪˈzɜːt/

Rule 4  Suffixes that put stress on the syllable BEFORE them
        -tion -sion -cian: eduCAtion, deCIsion, muSIcian
        -ic -ical:          ecoNOMic, poLITical
        -ity:               abILity, elecTRIcity
        -ial:               esSENtial, offiCIal
        -graphy:            phoTOgraphy, geOgraphy

Rule 5  Suffixes that carry the stress themselves
        -ee: refuGEE, trainEE    -eer: engiNEER, volunTEER
        -ese: JapaNESE, ChiNESE  -ique: techNIQUE

Rule 6  Suffixes that do NOT change stress
        -ful -less -ness -ment -er -or -ly -ing -ed -s
        HAPpy, HAPpiness; BEAUty, BEAUtiful; GOVern, GOVernment
        Prefixes un- dis- mis-: unHAPpy, disAPpear

Rule 7  Compounds
        Noun + noun: first part. BLACKboard, TOOTHbrush, POSToffice
        Adjective + noun (two words): the noun. a black BOARD, a green HOUSE
        Verb compounds and adjective compounds: second. underSTAND, bad-TEMpered""", "text", title="Table 1. Word stress rules"),
        T("Rule 4 has a tidy shape: the stress falls on the syllable immediately before these endings (education, economic, ability, essential). "
          "The ending itself is weak. Learning this one rule helps with hundreds of long words."),
        H("Stress and the vowel"),
        T("Unstressed syllables often contain **schwa /ə/** or another weak vowel. 'Photograph' is /ˈfəʊtəɡrɑːf/, but 'photographer' is /fəˈtɒɡrəfə/, and its first vowel has weakened to /ə/. "
          "When you stress the wrong syllable, you usually also use the wrong vowel, and listeners lose the word."),
        CODE("""photograph     /ˈfəʊtəɡrɑːf/      PHOtograph
photographer   /fəˈtɒɡrəfə/       phoTOgrapher
photographic   /ˌfəʊtəˈɡræfɪk/    photoGRAPHic   (secondary stress on the first syllable)
economy        /ɪˈkɒnəmi/         eCOnomy
economic       /ˌiːkəˈnɒmɪk/      ecoNOMic       (also /ˌekə-/: check your dictionary)
economist      /ɪˈkɒnəmɪst/       eCOnomist
education      /ˌedʒuˈkeɪʃn/      eduCAtion      (/ˈkeɪʃən/ in some dictionaries; check your dictionary)""", "text", title="Table 2. Stress moves inside a word family"),
        T("Stress can also change meaning. 'A BLACKbird' is a kind of bird; 'a black BIRD' is any bird that is black. 'The GREENhouse' is a glass building for plants; 'a green HOUSE' is a house painted green."),
        H("Where books and dictionaries differ"),
        T("Stress is not always settled. These words are said in more than one way in standard British English: 'magazine' (/ˌmæɡəˈziːn/ or /ˈmæɡəziːn/), 'adult', 'research' (noun), 'harass', "
          "'controversy', 'garage' and 'cigarette'. If a question depends on one of them, check your dictionary. In the examination, the Board's questions avoid disputed words or use clear ones."),
        H("Worked examples"),
        EX("Worked example 1: apply the rules",
           intro="Mark the primary stress: (a) decide (b) teacher (c) engineer (d) education.",
           steps=[
               S("(a) decide", text="Two-syllable verb: second syllable. deCIDE /dɪˈsaɪd/."),
               S("(b) teacher", text="Two-syllable noun: first syllable. TEAcher /ˈtiːtʃə/."),
               S("(c) engineer", text="-eer carries the stress. engiNEER /ˌendʒɪˈnɪə/ (secondary stress on the first syllable)."),
               S("(d) education", text="-tion takes stress on the syllable before: eduCAtion /ˌedʒuˈkeɪʃn/."),
           ]),
        EX("Worked example 2: noun or verb?",
           intro="Which pronunciation of 'record' fits each sentence? (a) 'Please ___ the meeting.' (b) 'She broke the world ___.'",
           steps=[
               S("(a)", text="After 'please', a verb is needed: reCORD /rɪˈkɔːd/ (stress on the second syllable)."),
               S("(b)", text="After 'the world', a noun is needed: REcord /ˈrekɔːd/ (stress on the first syllable)."),
               S("Rule", text="Noun-verb pairs: noun first, verb second. The vowel in the first syllable also weakens in the verb."),
           ]),
        EX("Worked example 3: stress shift in a word family",
           intro="Mark the stress in 'politics', 'political' and 'politician'.",
           steps=[
               S("politics", text="PO-li-tics /ˈpɒlətɪks/: first syllable."),
               S("political", text="-ical takes stress on the syllable before: poLIT-i-cal /pəˈlɪtɪkl/."),
               S("politician", text="-ian takes stress on the syllable before: poli-TI-cian /ˌpɒləˈtɪʃn/."),
           ]),
        EX("Worked example 4: compound or phrase?",
           intro="Explain the difference between 'a HOT dog' and 'a hot DOG'.",
           steps=[
               S("Compound noun", text="'A HOT dog' (stress on the first part) is the food, a sausage in bread."),
               S("Phrase", text="'A hot DOG' (stress on the noun) is a dog that is hot, for example after a run."),
               S("Rule", text="Stress on the first part signals one compound noun. Stress on the noun signals an adjective plus noun."),
           ]),
        MISTAKE("Stressing the last syllable of every long word",
                "Learners of English often stress the ending ('educaTION'). The ending -tion is weak; stress comes before it. Say eduCAtion."),
        MISTAKE("Giving all syllables equal strength",
                "In a word of three syllables like 'banana', two syllables are weak (/bəˈnɑːnə/). Equal strength makes words sound like a list of separate syllables and reduces clarity."),
        MISTAKE("Applying a rule where there is an exception",
                "'Hotel', 'police' and 'machine' are two-syllable nouns with stress on the second syllable. 'Visit' and 'enter' are verbs with stress on the first. Learn exceptions as you meet them."),
        QUIZ("Which word has its primary stress on the second syllable?",
             ["teacher", "table", "begin", "happy"], 2,
             "'Begin' is a two-syllable verb: beGIN /bɪˈɡɪn/. The others are nouns or adjectives stressed on the first syllable.",
             hint="Which one is a verb?",
             feedback=["TEAcher is stressed on the first syllable.", "TAble is stressed on the first syllable.", "", "HAPpy is stressed on the first syllable."]),
        QUIZ("In 'photographer', the stressed syllable is",
             ["pho", "to", "gra", "pher"], 1,
             "Stress is on the second syllable: phoTOgrapher /fəˈtɒɡrəfə/.",
             hint="Compare it with 'photograph'; the stress moves.",
             feedback=["That is the stress in 'photograph'.", "", "That is the stress in 'photographic'.", "That is the last syllable, which is weak."]),
        TIP("Stress questions in Paper 1 can show the word in capitals (for example 'beGIN') and ask which word has the same pattern, or give the transcription with stress marks. "
            "Learn the suffix rules, because they give you the answer for long words.", title="Exam link"),
        PQ("Mark the stress in: (a) refugee (b) comfortable (c) information (d) volunteer.",
           "(a) refuGEE (the suffix -ee carries stress; /ˌrefjuˈdʒiː/). (b) COMfortable /ˈkʌmftəbl/ (check your dictionary: stress is on the first syllable). (c) informAtion /ˌɪnfəˈmeɪʃn/. (d) volunTEER /ˌvɒlənˈtɪə/."),
        PQ("Give the stress pattern of 'record' as a noun and as a verb, with a transcription.",
           "Noun: REcord /ˈrekɔːd/. Verb: reCORD /rɪˈkɔːd/."),
        PQ("Explain why 'a BLACKbird' and 'a black BIRD' mean different things.",
           "Stress on the first part marks a compound noun, a particular species of bird. Stress on 'bird' marks an adjective plus noun, any bird that is black."),
        PQ("Which word in this list does not follow the 'noun and adjective: first syllable' rule? pretty, clever, hotel, table",
           "'Hotel' (hoTEL /həʊˈtel/) has stress on the second syllable. The others are stressed on the first."),
        SUM("Word stress is the strongest syllable of a word; unstressed syllables often weaken to schwa.",
            "Two-syllable nouns and adjectives usually take stress on the first syllable, verbs on the second, with exceptions.",
            "Endings -tion, -ic, -ical, -ity and -ian put stress on the syllable before; -ee, -eer, -ese and -ique carry it.",
            "Stress can change meaning (BLACKbird, black BIRD) and some words differ by dictionary: check your dictionary."),
    ],
))


# ------------------------------------------------------------------ S5. Sentence stress and rhythm
LESSONS.append(lesson(
    module=M_S,
    topic=T_SENT,
    title="Sentence stress, weak forms and rhythm",
    slug="enl1-sentence-stress-rhythm",
    minutes=23,
    summary="In a sentence, content words are stressed and function words are weak. Learn which words carry stress, the common weak forms, how rhythm follows the stressed beats, and how contrastive stress changes meaning.",
    objectives=[
        "Separate content words from function words and predict which are stressed",
        "Use the weak forms of common function words",
        "Explain stress-timed rhythm and mark the beats in a sentence",
        "Show how moving the main stress changes the meaning of a sentence",
    ],
    key_concepts=["Content word", "Function word", "Weak form", "Stress-timed rhythm", "Nuclear stress", "Contrastive stress"],
    blocks=[
        H("Introduction"),
        T("A telegram used to cost by the word, so people wrote only the words that mattered: 'ARRIVE FRIDAY NEED MONEY'. Everyone understood. "
          "Spoken English works in a similar way. The speaker gives strength to the words that carry the message and says the small grammar words quickly and lightly. "
          "If you give every word the same strength, listeners find it hard to pick out what matters, and the examination (which tests stress and intonation) expects you to know which words carry it."),
        T(NOAUDIO),
        D("**Content words** carry the meaning: nouns, main verbs, adjectives, adverbs, question words (who, where), negatives (not, never, don't) and demonstratives (this, that). They are normally **stressed**. "
          "**Function words** do the grammar: articles, prepositions, auxiliary verbs, pronouns, conjunctions. They are normally **unstressed** and have **weak forms**.", title="Content and function words"),
        T("In the sentences below, capital letters show the stressed words."),
        CODE("""The TEAcher WANTS the STUdents to BRING their BOOKS.
She's GOing to the MARket on SATurday.
I DON'T want to GO.
WHERE have you COME from?""", "text", title="Examples of sentence stress"),
        H("Weak forms"),
        T("Most common function words have two forms. The **strong form** is used when the word is stressed, alone, or at the end of a sentence. The **weak form** is used in normal connected speech and contains /ə/, /ɪ/ or fewer sounds."),
        CODE("""Word    Weak form    Strong form    Example
a       /ə/          /eɪ/           a cat      /ə kæt/
the     /ðə/ or /ði/ /ðiː/          the book   /ðə bʊk/; the egg /ði eɡ/
and     /ən/ /n/     /ænd/          bread and butter
but     /bət/        /bʌt/          I tried but failed
can     /kən/        /kæn/          I can swim /aɪ kən swɪm/; Yes, I can /kæn/
for     /fə/         /fɔː/          wait for me
from    /frəm/       /frɒm/         from home; Where from? /frɒm/
to      /tə/         /tuː/          going to town
of      /əv/         /ɒv/           a cup of tea
was     /wəz/        /wɒz/          he was late
have    /həv/        /hæv/          I have eaten; Yes, I have /hæv/
her     /hə/         /hɜː/          I saw her yesterday
them    /ðəm/        /ðem/          tell them
that    /ðət/ (conjunction)  /ðæt/  I know that he came""", "text", title="Table 1. Some weak forms"),
        T("Saying 'I can swim' with a strong /kæn/ gives it a different meaning: it suggests that someone doubted it. Use weak forms in normal speech, but remember that the strong form is correct when the word is stressed or stands at the end (Yes, I can)."),
        H("Rhythm"),
        D("English is said to be a **stress-timed** language: the stressed syllables come at roughly regular intervals, and the unstressed syllables between them are squeezed to fit. "
          "A sentence with few unstressed syllables between beats is spoken at about the same pace as one with many. Many other languages, and many varieties of English around the world, give syllables closer to equal time (**syllable-timed**). "
          "The reference pronunciation tested in the examination is stress-timed.", title="Stress-timed rhythm"),
        CODE("""Beats:            1          2           3
Sentence 1:       BOYS       PLAY        FOOTball
Sentence 2:       The BOYS   will PLAY   FOOTball
Sentence 3:       The BOYS   were PLAYing    FOOTball""", "text", title="Table 2. Three beats in each sentence"),
        T("Sentence 2 and sentence 3 have more syllables but the same three beats, so the extra syllables (the, will, were, -ing) are said very quickly."),
        H("Nuclear stress and contrastive stress"),
        D("In every stretch of speech there is one syllable that stands out most. It is called the **nucleus** or **tonic syllable**. In a neutral sentence it falls on the **last content word**: "
          "'I'm going to the MARket.' When a speaker wants to **contrast** one idea with another, or to correct something, the nucleus moves to that word.", title="Nuclear (main) stress"),
        EX("Worked example 1: mark the stressed words",
           intro="Mark the stressed words in: 'My brother is going to the market on Saturday.'",
           steps=[
               S("Content words", text="brother, going, market, Saturday."),
               S("Function words", text="my, is, to, the, on. They are weak."),
               S("Marked", text="My BROTHer is GOing to the MARket on SATurday."),
               S("Nuclear stress", text="The last content word: SATurday."),
           ]),
        EX("Worked example 2: contrastive stress",
           intro="How does the meaning change? (a) 'KOFI bought the red bag.' (b) 'Kofi BOUGHT the red bag.' (c) 'Kofi bought the RED bag.' (d) 'Kofi bought the red BAG.'",
           steps=[
               S("(a)", text="Kofi, not someone else, bought it."),
               S("(b)", text="He bought it (he did not borrow or steal it)."),
               S("(c)", text="The red one, not the blue one."),
               S("(d)", text="A bag, not a different item, such as a hat."),
           ]),
        EX("Worked example 3: the classic meaning change",
           intro="'I didn't say he stole it.' Give a meaning for each stress: (a) I didn't SAY... (b) ...say HE... (c) ...say he STOLE it.",
           steps=[
               S("(a) SAY", text="I did not say it aloud; I only hinted or wrote it."),
               S("(b) HE", text="Somebody else stole it, not him."),
               S("(c) STOLE", text="He did something else to it: he borrowed or damaged it, for example."),
           ]),
        EX("Worked example 4: weak forms",
           intro="Write a transcription of 'I can swim' and answer 'Can you swim?' with 'Yes, I can.'",
           steps=[
               S("Statement", text="'Can' is unstressed in the middle: /aɪ kən swɪm/."),
               S("Short answer", text="'Can' is the last word and stressed: /jes aɪ kæn/."),
           ]),
        MISTAKE("Stressing every word",
                "If every word is strong, the main message is lost and the rhythm sounds like a list. Choose the content words and keep the others short."),
        MISTAKE("Stressing a function word without a reason",
                "Words like 'the', 'of' and 'to' are weak. They may be stressed only for contrast or at the end of a sentence (Where are you from?)."),
        MISTAKE("Putting the nucleus on the wrong word",
                "'I'm going to the MARket' is neutral. 'I'm going to the market on SATurday' is neutral. Move the nucleus only when you mean a contrast."),
        QUIZ("In 'She has been waiting for the bus', which words are normally stressed?",
             ["she, has, been", "waiting, bus", "for, the", "has, the"], 1,
             "The content words are 'waiting' and 'bus'. 'She', 'has', 'been', 'for' and 'the' are function words.",
             hint="Which words carry the meaning?",
             feedback=["These are all function words.", "", "These are function words.", "These are function words."]),
        QUIZ("Which strong form is correct in 'Yes, I do' (answering 'Do you like tea?')?",
             ["/də/", "/duː/", "/dɒ/", "/dəʊ/"], 1,
             "In a short answer the verb is stressed and so takes its strong form /duː/.",
             hint="Is 'do' stressed here?",
             feedback=["That is the weak form, used in the middle of a sentence.", "", "No such pronunciation.", "That is the word 'dough'."]),
        TIP("Paper 1 can ask which word in a sentence carries the main stress, what a stress change implies, or which word has a weak form. Look for the new or contrasted information.", title="Exam link"),
        PQ("Mark the stressed words: 'Please bring your textbooks tomorrow.'",
           "Please BRING your TEXTbooks toMORrow. (Please is often weak; accept stress on content words.)"),
        PQ("Give a context in which the stress falls on BLUE: 'She wore a BLUE dress.'",
           "When someone asks 'Did she wear a red dress?' or when we contrast with another colour: she wore a blue one, not a red one."),
        PQ("Write the weak forms of 'and' and 'of' in the phrase 'a cup of tea and bread'.",
           "'of' /əv/ and 'and' /ən/: /ə kʌp əv tiː ən bred/."),
        PQ("Explain 'stress-timed rhythm' in two sentences.",
           "In stress-timed rhythm, stressed syllables come at roughly regular intervals, and unstressed syllables between them are shortened to fit. This is why English sentences with the same number of stresses take about the same time, however many small words are in them."),
        SUM("Stress content words (nouns, main verbs, adjectives, adverbs, question words, negatives) and weaken function words.",
            "Function words have weak forms in connected speech and strong forms when stressed or sentence-final.",
            "English rhythm follows the stressed beats; unstressed syllables are squeezed.",
            "The nucleus is normally on the last content word and moves for contrast, which changes the meaning."),
    ],
))

# ------------------------------------------------------------------ S6. Intonation
LESSONS.append(lesson(
    module=M_S,
    topic=T_SENT,
    title="Intonation: the tunes of English",
    slug="enl1-intonation-tunes",
    minutes=23,
    summary="Intonation is the rise and fall of the voice. Learn the four main tunes (fall, rise, fall-rise, rise-fall), where English normally uses each, and how a change of tune changes the meaning.",
    objectives=[
        "Define intonation, tone unit and nucleus",
        "Recognise the fall, rise, fall-rise and rise-fall tunes",
        "Say which tune normally goes with statements, questions, lists and tags",
        "Explain how the same words can mean different things with different tunes",
    ],
    key_concepts=["Intonation", "Tone unit", "Nucleus", "Fall", "Rise", "Fall-rise", "Rise-fall"],
    blocks=[
        H("Introduction"),
        T("Say the word 'yes' three ways: as a firm answer, as a question ('Yes?'), and as a doubtful 'Yeees...'. The word is the same, but each means something different. "
          "The difference is the tune of your voice. We call this **intonation**, and it helps the listener to know if you are finished, asking, doubtful or pleased."),
        T(NOAUDIO + " Because tunes cannot be heard in print, we use arrows and diagrams, and you must practise by saying the sentences aloud."),
        D("**Intonation** is the pattern of rises and falls in the pitch of the voice across a stretch of speech. A **tone unit** is a stretch of speech with one main pitch movement, often a short phrase or a clause. "
          "The **nucleus** (or tonic syllable) is the syllable where the main pitch movement begins, usually the last stressed word, as in the previous lesson.", title="Intonation"),
        IMG("al-enl1-intonation-contours.svg",
            alt="Four small graphs of voice pitch against time. The fall starts high and ends low. The rise starts low and ends high. The fall-rise goes down and up again. The rise-fall goes up and down again.",
            caption="Figure 1. The four main nuclear tunes. The line shows the pitch of the voice; the heavy dot marks the nucleus."),
        H("The four tunes and what they usually mean"),
        KEY("Tunes", "These are tendencies in standard British English, not laws.", cards=[
            ["Fall ↘", "Finality and certainty. Used for statements, commands, wh-questions and goodbyes: 'I live in Douala ↘'. 'Where do you live? ↘'"],
            ["Rise ↗", "Openness, continuation or a request for a reply. Used for yes/no questions and for items in a list that is not finished: 'Are you coming? ↗'"],
            ["Fall-rise ↘↗", "Reservation or doubt. 'It's good ↘↗' (but there is a problem). Also polite, apologetic or warm tones: 'Sorry ↘↗'"],
            ["Rise-fall ↗↘", "Strong feeling, surprise or definiteness: 'Really? ↗↘' (impressed), 'Lovely ↗↘'."],
        ]),
        H("Statements, questions, lists and tags"),
        CODE("""Statements         I'm going to the MARket ↘
Wh-questions       WHERE are you GOing? ↘
Yes/no questions   Are you going to the MARket? ↗
Commands           Close the DOOR ↘
Lists              We bought MAIZE ↗, BEANS ↗, PLANtains ↗ and RICE ↘
Tag, real question You're coming, aren't YOU? ↗   (I do not know the answer)
Tag, checking      It's hot, isn't IT? ↘             (I expect you to agree)
Incomplete         If you COME ↗ , we can start.""", "text", title="Table 1. Common uses of the tunes"),
        T("Notice the list. The rise on the first items signals 'there is more', and the fall on the last signals 'this is the end'. "
          "The tag question shows how the same words can mean two things: a rise asks a real question, and a fall asks for agreement."),
        T("A flat, narrow voice can sound bored. A wide pitch range sounds interested and warm. Different varieties of English, including those spoken in Cameroon, use tunes in their own ways; "
          "the patterns above are the standard ones tested in the examination."),
        H("Worked examples"),
        EX("Worked example 1: choose the tune",
           intro="Which tune is the best for (a) 'What is your name?' (b) 'Is this your bag?' (c) 'Close the window.'",
           steps=[
               S("(a) wh-question", text="Fall: WHAT is your NAME? ↘"),
               S("(b) yes/no question", text="Rise: Is this your BAG? ↗"),
               S("(c) command", text="Fall: Close the WINdow. ↘"),
           ]),
        EX("Worked example 2: mark a list",
           intro="Mark the intonation: 'I need a pen, a ruler, a notebook and a calculator.'",
           steps=[
               S("Non-final items", text="Rise on each: PEN ↗, RULer ↗, NOTEbook ↗."),
               S("Final item", text="Fall: and a calCUlator ↘."),
           ]),
        EX("Worked example 3: the same words, different meanings",
           intro="What does the speaker mean by 'It's OK' with (a) a fall and (b) a fall-rise?",
           steps=[
               S("(a) Fall ↘", text="'It's OK.' Plain agreement: it is fine."),
               S("(b) Fall-rise ↘↗", text="'It's OK...' It is acceptable, but something could be better; the speaker has a reservation."),
           ]),
        EX("Worked example 4: the tag question",
           intro="Explain the difference between 'You're a teacher, aren't you?' with a rise and with a fall.",
           steps=[
               S("Rising tag ↗", text="The speaker does not know and asks a real question."),
               S("Falling tag ↘", text="The speaker thinks the answer is yes and seeks agreement or confirmation."),
           ]),
        MISTAKE("Rising at the end of every sentence",
                "A rise suggests the speaker has not finished or is asking. If you rise at the end of a statement, listeners may wait for more or think you are unsure. Use a fall for finality."),
        MISTAKE("Using a single tune for everything",
                "A flat voice makes it hard to tell a statement from a question and can sound uninterested. Vary the pitch with the meaning."),
        MISTAKE("Treating the rules as laws",
                "Wh-questions can rise to sound friendly ('What's your name? ↗'), and yes/no questions can fall to sound firm. The tunes in the table are the neutral patterns; the examination uses the neutral ones."),
        QUIZ("The best tune for the last item in 'We bought rice, beans and oil' is",
             ["fall", "rise", "fall-rise", "rise-fall"], 0,
             "The last item of a complete list takes a fall to show the list is finished.",
             hint="Does the list continue after 'oil'?",
             feedback=["", "A rise would suggest that more items follow.", "A fall-rise suggests doubt or reservation.", "A rise-fall suggests strong feeling."]),
        QUIZ("Which question normally has a rising tune?",
             ["Where do you live?", "Are you ready?", "What time is it?", "How old are you?"], 1,
             "'Are you ready?' is a yes/no question, which normally rises. The others are wh-questions, which normally fall.",
             hint="Which question can be answered by yes or no?",
             feedback=["A wh-question normally falls.", "", "A wh-question normally falls.", "A wh-question normally falls."]),
        TIP("Paper 1 usually shows a sentence with arrows or the word 'rising' or 'falling' and asks which tune is correct, or what a speaker means. "
            "Think of the speaker's purpose (finished, asking, doubtful, surprised) and then choose the tune.", title="Exam link"),
        PQ("Which tune goes with each: (a) 'Good morning!' (b) 'Is it raining?' (c) 'Who is that?'",
           "(a) fall (b) rise (c) fall."),
        PQ("Explain what a fall-rise on 'Maybe' tells the listener.",
           "It shows doubt or reservation: the speaker is not saying yes and is not saying no. It can also soften a refusal."),
        PQ("Mark the intonation: 'We visited Limbe, Kribi and Garoua.'",
           "We visited LIMbe ↗, KRIbi ↗ and GaROua ↘. (Rise on the non-final items, fall on the last.)"),
        PQ("A friend says 'It's cold, isn't it?' with a fall. Does she want information or agreement?",
           "Agreement. A falling tag expects the listener to say yes."),
        SUM("Intonation is the rise and fall of the voice. A tone unit has one nucleus, usually on the last content word.",
            "Neutral tunes: fall for statements, commands and wh-questions; rise for yes/no questions and unfinished lists; fall-rise for doubt; rise-fall for strong feeling.",
            "The same words can mean different things with different tunes (tag questions, 'It's OK').",
            "These are tendencies; varieties of English differ, but the examination tests the standard patterns."),
    ],
))

# ------------------------------------------------------------------ S7. Connected speech and spelling of unknown words
LESSONS.append(lesson(
    module=M_S,
    topic=T_CONN,
    title="Connected speech, and reading and spelling unknown words",
    slug="enl1-connected-speech-unknown-words",
    minutes=25,
    summary="In fluent speech words join, shrink and change shape: linking, elision, assimilation and contractions. Then use sound-spelling patterns and syllable splitting to read and spell words you have not met.",
    objectives=[
        "Recognise linking, elision and assimilation in connected speech",
        "Read contractions and understand why 'can't' and 'cannot' sound different",
        "Split an unknown word into syllables and sound it out",
        "Spell an unknown word using sound-spelling patterns and spelling rules",
    ],
    key_concepts=["Linking", "Elision", "Assimilation", "Contraction", "Syllable splitting", "Sight word"],
    blocks=[
        H("Introduction"),
        T("When a friend says 'Whatcha doin?' you understand, though the words have fused. In real speech we do not say words one at a time. We run them together, drop some sounds and change others. "
          "Knowing how this works helps you to understand fast speech and to transcribe it; knowing sound-spelling patterns helps you to read and spell words you have never seen. "
          "Both skills are named in the syllabus: connected speech is part of analysing authentic speech, and the objectives include reading and spelling unknown words."),
        T(NOAUDIO),
        H("Part 1: connected speech"),
        D("**Linking** joins the end of one word to the start of the next. When a consonant ends one word and a vowel begins the next, the consonant moves across: 'pick it up' sounds like /ˈpɪkɪtʌp/.", title="Linking"),
        D("**Elision** is the dropping of a sound in fluent speech: the /t/ in 'next day' /neks deɪ/, and the /d/ in 'friendship' /ˈfrenʃɪp/.", title="Elision"),
        D("**Assimilation** is the change of a sound to be more like a neighbouring sound: 'ten pence' becomes /tem pens/, 'good boy' becomes /ɡʊb bɔɪ/ and 'in case' becomes /ɪŋ keɪs/. "
          "In **coalescence**, two sounds blend into one: 'did you' becomes /dɪdʒu/ and 'meet you' becomes /miːtʃu/.", title="Assimilation"),
        CODE("""Process          Words              In connected speech
Linking          pick it up         /ˈpɪkɪtʌp/
Linking r        far away           /ˌfɑːr əˈweɪ/ (the r is heard because a vowel follows)
Glides           go on, see it      /ɡəʊ wɒn/, /siː jɪt/ (a small /w/ or /j/ joins vowels)
Elision          next day           /neks deɪ/
Elision          friendship         /ˈfrenʃɪp/
Assimilation     ten pence          /tem pens/
Assimilation     this shop          /ðɪʃ ʃɒp/
Coalescence      did you            /dɪdʒu/
Weak forms       a cup of tea       /ə kʌp əv tiː/
Contractions     I'm, don't, can't  /aɪm/, /dəʊnt/, /kɑːnt/""", "text", title="Table 1. Connected speech"),
        T("**Linking r and intrusive r.** In RP, 'far' is /fɑː/, but in 'far away' the r is heard, because a vowel follows: /fɑːr əˈweɪ/. Some speakers also insert an /r/ where there is no r in the spelling, as in 'law and order' /lɔːr ən ˈɔːdə/. "
          "This 'intrusive r' is common in speech, but teachers differ on whether to teach it: check your dictionary and your teacher's guidance."),
        T("**Contractions** such as I'm, don't, he's and they'll are the normal spoken forms of 'I am', 'do not', 'he is' and 'they will'. "
          "In formal writing they are usually avoided, but in speech they are normal. Informal spoken forms such as 'gonna' and 'wanna' are not used in formal writing or in the examination."),
        H("Part 2: reading and spelling unknown words"),
        KEY("Reading an unknown word", "Do these steps in order.", cards=[
            ["1. Look for known parts", "Prefix (un-, re-, dis-), suffix (-tion, -ment, -ful) and root. Cover them and read the root first."],
            ["2. Split into syllables", "Between two consonants (rab-bit, sun-set); before a single consonant after a long vowel (ta-ble); after it after a short vowel (cab-in, rob-in) - usually."],
            ["3. Sound out the vowels", "Use the patterns in Table 2, then try the alternative if the word does not sound real."],
            ["4. Put the stress", "Use the stress rules from the previous lessons, then put schwa in the weak syllables."],
        ]),
        CODE("""Sound  Common spellings and examples
/eɪ/   a-e make    ai rain    ay day    ei eight    ey they    ea great
/iː/   ee see      ea eat     e-e these  ie field    ei receive
/aɪ/   i-e time    igh high   y my       ie pie
/əʊ/   o-e home    oa boat    ow know    o go
/uː/   oo food     ue blue    u-e rule   ew new
/ɜː/   er her      ir bird    ur turn    or work     ear learn
/ɔː/   or for      aw law     au cause   ore more    ough thought
/ʃ/    sh ship     ti nation  ci special ssi session ch chef
/tʃ/   ch church   tch watch
/dʒ/   j jump      g giant    dge bridge
/f/    f fan       ph phone   gh laugh
/k/    c cat       k king     ck back    ch school   qu queen (kw)""", "text", title="Table 2. Sound-spelling patterns"),
        H("Spelling rules that help"),
        CODE("""Silent e        hop -> hope, cut -> cute (the e makes the vowel long)
Dropping e      hope -> hoping, make -> making (drop e before -ing)
Doubling        stop -> stopped, begin -> beginning (stressed last syllable, short vowel, one consonant)
No doubling     visit -> visited, open -> opened (stress is not on the last syllable)
y to i          study -> studies, happy -> happiness (consonant + y)
i before e      believe, field; after c: receive, ceiling (exceptions: weird, seize)
Prefix + root   un + necessary = unnecessary; dis + appear = disappear (no letter lost)""", "text", title="Table 3. Spelling rules"),
        T("Some words must be learned by sight because their spelling does not match the sound: said, because, people, friend, again, would, though, through. These are **sight words**, and a bigger sight vocabulary makes reading faster. "
          "A memory trick (mnemonic) helps: 'necessary' has one collar (c) and two sleeves (ss); 'separate' has 'a rat' in the middle."),
        H("Worked examples"),
        EX("Worked example 1: rewrite in connected speech",
           intro="Show how 'ten pence' and 'good boy' change.",
           steps=[
               S("ten pence", text="/n/ before the lip sound /p/ becomes /m/: /tem pens/."),
               S("good boy", text="/d/ before /b/ becomes /b/: /ɡʊb bɔɪ/."),
               S("Name", text="Both are assimilation: a sound copies the place of articulation of the next sound."),
           ]),
        EX("Worked example 2: read an unknown word",
           intro="Read the long word 'unreliability' by splitting it into parts.",
           steps=[
               S("Parts", text="un + rely + able + ity -> un-re-li-a-bil-i-ty."),
               S("Syllables", text="seven: un, re, li, a, bil, i, ty."),
               S("Stress", text="The suffix -ity puts stress on the syllable before: unreliaBIlity. Transcription /ˌʌnrɪˌlaɪəˈbɪləti/ (secondary stresses; check your dictionary)."),
           ]),
        EX("Worked example 3: spell from sound",
           intro="Spell the word that sounds like /ˈbjuːtɪfl/ (check your dictionary: some write /ˈbjuːtɪfʊl/).",
           steps=[
               S("Syllables", text="/ˈbjuː/ - /tɪ/ - /fl/."),
               S("First syllable", text="/bjuː/ is spelled beau, a spelling you must know. Other examples: beauty."),
               S("Rest", text="/tɪ/ is ti, and -ful is the usual ending for /fl/ (one l)."),
               S("Answer", text="beautiful."),
           ]),
        EX("Worked example 4: apply a spelling rule",
           intro="Add -ed or -ing: (a) stop + ed (b) visit + ed (c) hope + ing (d) refer + ed.",
           steps=[
               S("(a) stopped", text="One-syllable word ending in a short vowel plus one consonant: double the consonant."),
               S("(b) visited", text="Stress is on the first syllable (VISit), so the last consonant is not doubled."),
               S("(c) hoping", text="Drop the silent e before -ing."),
               S("(d) referred", text="Stress is on the last syllable (reFER), so the r is doubled."),
           ]),
        MISTAKE("Pronouncing a word the way it is spelled",
                "'Wednesday' /ˈwenzdeɪ/ has no /d/ before /n/, and 'cupboard' /ˈkʌbəd/ has no /p/. Learn the common irregular words; do not read them letter by letter."),
        MISTAKE("Mishearing 'can' and 'can't'",
                "In connected speech 'can' is weak, /kən/, and 'can't' is /kɑːnt/ with a clear long vowel. Listen for the vowel, not for the final /t/, which is often hard to hear. In writing, avoid contractions in formal letters."),
        MISTAKE("Spelling by sound alone",
                "Several spellings can stand for one sound (/eɪ/: make, rain, day, eight). Use the rules, patterns and your memory of the word, and check in a dictionary."),
        QUIZ("In fast speech, 'good boy' is most likely said as",
             ["/ɡʊd bɔɪ/ every time", "/ɡʊb bɔɪ/", "/ɡʊt bɔɪ/", "/ɡʊ bɔɪ/ only"], 1,
             "/d/ takes on the lip position of the next sound /b/, giving /ɡʊb bɔɪ/ (assimilation).",
             hint="What happens to a /d/ before a lip sound?",
             feedback=["It can be said that way, but in fast speech the /d/ changes.", "", "The /t/ would be unvoiced; /d/ stays voiced.", "The /d/ is changed, not just dropped."]),
        QUIZ("Which word is correctly spelled?",
             ["recieve", "receive", "receeve", "reseive"], 1,
             "After c the rule is e before i: receive.",
             hint="Remember 'i before e except after c'.",
             feedback=["Wrong order: after c it is ei.", "", "The /iː/ here is ei, not ee.", "The first sound is /s/, but the spelling uses c."]),
        TIP("In Paper 1 you can meet questions that show a transcription of a word spoken in connected speech and ask what was said, or ask you to pick the correctly spelled form. "
            "Note that Paper 2 and Paper 3 mark accuracy of spelling too, so spelling rules help beyond Paper 1.", title="Exam link"),
        PQ("Give the assimilated pronunciation of 'in case' and say what changed.",
           "/ɪŋ keɪs/. The /n/ before the back sound /k/ became /ŋ/."),
        PQ("Add the ending: (a) begin + ing (b) happy + ness (c) study + es (d) open + ed.",
           "(a) beginning (b) happiness (c) studies (d) opened."),
        PQ("Explain the difference between linking r and the r in the spelling of 'car' in RP.",
           "In RP, 'car' on its own is /kɑː/ with no r. In 'car engine', a vowel follows, so the r is heard: /kɑːr ˈendʒɪn/. This is linking r."),
        PQ("Split 'information' into syllables, mark the stress and give the pronunciation.",
           "in-for-ma-tion; the suffix -tion puts the stress on the syllable before: inforMAtion /ˌɪnfəˈmeɪʃn/."),
        SUM("Connected speech joins words (linking), drops sounds (elision), changes sounds to fit neighbours (assimilation) and blends them (coalescence).",
            "Contractions and weak forms are normal in speech and are avoided in formal writing.",
            "To read an unknown word, find prefix, root and suffix, split into syllables, sound out vowels with the patterns and apply stress rules.",
            "To spell, use sound-spelling patterns, the rules (silent e, doubling, y to i, i before e) and sight words, and check a dictionary."),
    ],
))
