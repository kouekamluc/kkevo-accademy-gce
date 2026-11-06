"""Form 5 English Language (O Level 0530): Composition & Directed Writing (eight lessons) and Examination (three lessons).

Draft content. Exam facts stated are only those of the Board's 2023 Ordinary Level report: Paper 1 is 50 multiple-choice
questions (listening comprehension, reading comprehension, grammar and vocabulary) in 1 hour 30 minutes, marked
electronically; Paper 2 has Section A Directed Writing and Section B Composition, with word and paragraph limits,
use of the stimulus only, no disclosure of identity, black or blue ink. No mark splits are stated. Model letters,
speeches, reports and minutes are KKEVO examples written for teaching; every name, address and place in them is
invented. Layouts of letters differ between textbooks (blocked or indented): the lessons say "check your teacher's
preferred layout".
"""

from .dsl import *  # noqa: F403

COURSE = ("english-language", "form-5")

M_WRITE = "Composition & Directed Writing"
M_EXAM = "Examination"

LESSONS = [
    # ------------------------------------------------------------------ 1. Narrative essays
    lesson(
        module=M_WRITE, topic="Narrative and descriptive essays",
        title="Narrative essays: telling a story that works",
        slug="ewr-narrative-essays",
        minutes=22,
        summary="How to plan and write a narrative essay: a clear story shape, one consistent tense, a strong ending that matches "
                "the question, dialogue that is correctly punctuated, and paragraphs that each do one job.",
        objectives=[
            "Describe the five parts of a story: opening, problem, build-up, climax and ending",
            "Keep one tense through the story and punctuate dialogue correctly",
            "Plan a narrative essay that answers the exact task, including a required last sentence",
            "Avoid thinking in a home language, Pidgin or French and translating word for word",
        ],
        key_concepts=["Narrative essay", "Plot", "Climax", "Tense consistency", "Dialogue", "Paragraph unity"],
        blocks=[
            H("Introduction"),
            T("Everyone in Cameroon knows how to tell a story. An aunt tells one by the fire. A taxi driver tells one about a "
              "road accident he almost had. A narrative essay is a story written down, but it has to be told in a way an examiner "
              "can follow and enjoy.\n\n"
              "In Paper 2, Section B (Composition), you meet topics of several kinds. One kind says, \"Tell a story that ends "
              "with these words...\". This lesson shows you how to answer that kind of task."),
            D("A **narrative essay** tells a story: events happen to characters in a place, in an order, and lead to an ending. "
              "It is written in continuous prose, in paragraphs, in good English.", title="Definition"),
            H("The shape of a story"),
            KEY("Five parts of a narrative", "Most good stories follow this shape. Each part is one paragraph or more.", cards=[
                ["1. Opening", "Who? Where? When? Introduce the main character and the place in a few lines."],
                ["2. Problem", "Something goes wrong or a choice must be made. The story really starts here."],
                ["3. Build-up", "Events make the problem bigger. Actions have results."],
                ["4. Climax", "The most exciting or serious moment. The turning point."],
                ["5. Ending", "What happens in the end, and what the character learns."],
            ]),
            T("Now read the plan below. It is for a story about a boy called Ayuk who skips school to follow friends to a "
              "football viewing centre. Notice that the plan is short: words and not sentences."),
            CODE("""Task: Tell a story that ends with: "...I should have listened."

Opening   : Ayuk, Form 4, Buea. Teacher warns him about friends who skip class.
Problem   : Friends invite him to skip the Friday exam revision.
Build-up  : He skips 3 days. Marks fall. Mother is not told.
Climax    : He fails the mock exam. Mother hears from the principal.
Ending    : He repeats the class. Last line: "I should have listened."
""", "text", title="A story plan (words, not sentences)"),
            TIP("In the exam, write your plan on the answer booklet, then **cross it out neatly** before you hand in. An "
                "uncancelled plan can cost you; a plan crossed out is simply rough work. Cross out only when you have written "
                "the real answer.", title="Plan, then cancel"),
            H("Obey the task exactly"),
            T("Read the title twice. Ask three questions. What kind of essay is it (story, not description)? Who tells it "
              "(\"I\" or a character)? Is there a **required ending**? If the task gives the last words, your story must lead "
              "to them naturally and must end with them. A story that wanders and then pastes the sentence on the end loses marks."),
            MISTAKE("Telling a story that does not match the ending",
                    "If the ending says the narrator wishes he had listened to advice, the story must contain advice that is "
                    "given and then ignored, and the bad results that follow. Do not write only about the bad behaviour and "
                    "forget the advice. Check each paragraph: does it help the reader reach the last line?"),
            H("Tense and voice"),
            T("Most narratives use the **simple past**: \"Ayuk walked to school.\" Choose it and keep it. Do not jump between "
              "\"he walked\" and \"he walks\" in the same scene. The past perfect (\"he had warned\") shows what happened "
              "**earlier** than the main story."),
            EX("Worked example 1: repair the tenses", intro="The sentence below mixes tenses. Rewrite it in one past tense: "
               "\"Ayuk opens the door, and he saw that his mother was waiting.\"", steps=[
                S("Find the main time of the story", text="The story is told in the past: \"saw\" and \"was waiting\"."),
                S("Find the verb that does not fit", text="\"opens\" is present."),
                S("Change it", text="\"Ayuk opened the door, and he saw that his mother was waiting.\""),
            ]),
            H("Dialogue"),
            T("Speech makes a story alive, but use it a little. Put the spoken words in speech marks. Start a **new line** each "
              "time a different person speaks. Put the comma, full stop or question mark **inside** the speech marks."),
            CODE("""\"Where were you?\" asked his mother.
\"At school,\" Ayuk answered, looking at his shoes.
\"Do not lie to me,\" she said quietly.""", "text", title="Dialogue: new line for each speaker"),
            QUIZ("Which sentence is punctuated correctly?",
                 ["\"Come here\" said the teacher.", "\"Come here,\" said the teacher.", "\"Come here\", said the teacher.",
                  "Come here, said the teacher."], 1,
                 "A comma goes inside the speech marks before the speaker tag: \"Come here,\" said the teacher.",
                 hint="Where does the comma go, inside or outside the speech marks?",
                 feedback=["The comma is missing after \"here\".", "", "The comma is outside the speech marks.",
                           "The speech marks are missing, so the reader cannot see who spoke."]),
            H("Words, paragraphs and language"),
            T("Use details that the reader can see, hear and feel: \"the zinc roof rattled in the rain\" is better than \"it was "
              "raining\". Show feelings by actions: \"his hands shook\" is stronger than \"he was afraid\".\n\n"
              "Each paragraph has **one main job** (paragraph unity). Start a new paragraph when the time, place, speaker or "
              "idea changes. Do not write the whole story in one paragraph, and do not write one-sentence paragraphs all "
              "through. Write in continuous prose: do not list events."),
            MISTAKE("Translating from your home language, Pidgin or French",
                    "Thinking in another language and writing it word for word puts the wrong grammar into English: \"I am "
                    "having fifteen years\" (French) is wrong; say \"I am fifteen years old\". Pidgin forms such as \"he don go\" "
                    "are not Standard English: write \"he has gone\". Think in short, simple English sentences you are sure of."),
            TIP("Composition is in Paper 2, Section B. You choose **one** topic from those offered and write only on it. Writing "
                "on two topics, or copying the instructions again and again, wastes time. Never give your real name, school or "
                "town as a clue to who you are.", title="Exam link"),
            EX("Worked example 2: plan a story from a topic", intro="Plan a story that ends with the words, \"I will never "
               "lie again.\"", steps=[
                S("Decide the problem", text="A girl, Nchang, lies to her trader mother about money for school fees and spends it on clothes."),
                S("Build the story", text="Her mother borrows to pay the fees; the lie is discovered at the school office; she is ashamed."),
                S("Climax", text="The head teacher calls her mother, and Nchang watches her mother’s face."),
                S("Ending", text="Nchang confesses and promises to repay. The last sentence is the required one: \"I will never lie again.\""),
            ]),
            QUIZ("A story must end with the words \"...and I have never forgotten that day.\" What should you do?",
                 ["Write the sentence at the start and then tell any story.", "Tell a story about one important day and end exactly with the sentence.",
                  "Describe a place in detail and add the sentence at the end.", "Write two stories and choose the better one at the end."], 1,
                 "The last words are part of the task. The story must build to them and end with them.",
                 hint="The required words belong to which part of the story?",
                 feedback=["The words are required at the end, not the start.", "",
                           "A description is a different kind of essay, and the sentence would not fit naturally.",
                           "Write one story only. Two stories waste time and may be penalised."]),
            PQ("Write a plan, in five short lines, for a story called \"The Market Day Accident\". Name the five parts.",
               "Opening: Mbella and her aunt go to Mile 17 Market early. Problem: Mbella chases a runaway goat into the road. "
               "Build-up: A motorbike swerves and a trader falls. Climax: Mbella is blamed; she tells the truth. Ending: The trader "
               "forgives her, and she learns to listen to her aunt. (Any logical plan with the five parts is correct.)"),
            PQ("Correct the tenses: \"The rain stopped, and Tabe walks out. He looked up and sees the rainbow.\"",
               "The rain stopped, and Tabe walked out. He looked up and saw the rainbow. (Keep the simple past throughout.)"),
            PQ("Punctuate the dialogue and put it on separate lines: Where are you going asked Mama I am going to the stream said Ngum",
               "\"Where are you going?\" asked Mama.\n\"I am going to the stream,\" said Ngum."),
            SUM("A narrative essay tells a story in continuous prose with an opening, a problem, a build-up, a climax and an ending.",
                "Read the task exactly. If the ending is given, build the story to it and finish with it.",
                "Choose one tense, usually the simple past, and keep it. Use the past perfect for earlier events.",
                "Start a new line for each speaker; put commas and full stops inside the speech marks.",
                "Plan, then cross out the plan. Write in good English, not translated Pidgin or French. Choose only one topic."),
        ],
    ),
    # ------------------------------------------------------------------ 2. Descriptive essays
    lesson(
        module=M_WRITE, topic="Narrative and descriptive essays",
        title="Descriptive essays: painting a picture in words",
        slug="ewr-descriptive-essays",
        minutes=21,
        summary="How to describe one person, place or event so the reader can see it: using the five senses, a clear order, "
                "precise words and fresh comparisons, and staying with description instead of drifting into a story.",
        objectives=[
            "Tell the difference between description and narration",
            "Use the five senses and exact words to describe a place or a person",
            "Organise a description in a clear order (near to far, or by time of day)",
            "Use similes and metaphors without overdoing them",
        ],
        key_concepts=["Descriptive essay", "Five senses", "Spatial order", "Simile", "Metaphor", "Dominant impression"],
        blocks=[
            H("Introduction"),
            T("Imagine you are telling a friend who has never been there about Limbe beach in the late afternoon. You would not "
              "say what time the bus left or who you met. You would say how the black sand looks, how the waves sound, how fried "
              "fish smells. That is **description**.\n\n"
              "A descriptive essay does one thing: it lets the reader see, hear, smell, taste and feel something as if they were there."),
            D("A **descriptive essay** describes a person, a place, an object or an event. It shows what the thing is like, "
              "using details and comparisons. It does not tell a plot.", title="Definition"),
            KEY("Description and narration are different", "Many candidates start to describe and then slip into a story.", cards=[
                ["Narration", "Answers: What happened? Uses events in time order. Verbs of action."],
                ["Description", "Answers: What is it like? Uses details of sight, sound, smell, touch, taste."],
            ]),
            TIP("A Composition topic may say, \"Describe a famous place you have visited.\" Describe **one** place only. Do "
                "not tell about the journey, and do not describe many places. The word \"describe\" tells you what the "
                "examiner expects.", title="Exam link"),
            H("Use the five senses"),
            T("Good writers do not rely on sight alone. Collect details under each sense before you write."),
            CODE("""Topic: Describe a busy market on Saturday morning.

Sight   : red tomatoes in pyramids; blue plastic basins; women in bright wrappers
Sound   : bargaining voices; a radio playing makossa; a motorbike horn
Smell   : roasting corn; wet earth; smoked fish
Touch   : heat of the sun; crowd pushing against my arm
Taste   : the sweetness of fresh pineapple slices
""", "text", title="Sense plan"),
            H("Choose an order"),
            T("A description needs a path for the reader’s eyes. Three orders work well:\n\n"
              "**Space:** near to far, left to right, bottom to top. **Time:** morning, noon, evening. "
              "**Importance:** from small details to the most striking one.\n\n"
              "Say which order you use at the start of each paragraph: \"At the gate...\", \"Further in...\", \"At the far end...\"."),
            H("Make the picture exact"),
            T("Replace weak, general words with exact ones. \"A big house\" tells nothing. \"A two-storey house of red brick, with a "
              "green zinc roof\" shows the house. Use adjectives that add meaning, and strong verbs: \"the vendors "
              "shouted\", not \"the vendors said loudly\"."),
            D("A **simile** compares two things using *like* or *as*: \"The crowd moved like a river.\" A **metaphor** says "
              "one thing is another: \"The market was a beehive.\" Use a few fresh ones; do not fill every sentence with them.",
              title="Similes and metaphors"),
            EX("Worked example 1: improve a weak sentence", intro="Improve: \"The market was very noisy and full of people.\"",
               steps=[
                S("Find the weak words", text="\"very\", \"noisy\", \"full of people\" are general."),
                S("Add sound and sight details", text="Traders shouted prices, radios played, and children ran between the stalls."),
                S("Join them", text="\"The market was a roar of shouted prices, loud radios and running children.\""),
            ]),
            MISTAKE("Describing many places",
                    "If the topic says \"a place\", choose one. A shallow tour of five towns gives each place only one line "
                    "and no detail. Depth beats number."),
            MISTAKE("Slipping into narration",
                    "\"We left at six, then the bus broke down, and we...\" is a story. If a sentence answers \"What happened next?\", "
                    "it probably does not belong. Use present or past tense consistently and keep to \"what it is like\"."),
            H("Describing a person"),
            T("When describing a person, give first the **overall impression** (kind, strict, cheerful), then details of face, "
              "clothes, voice and habits that prove it. Show, do not only tell: \"She hummed while she sorted beans, and every "
              "neighbour went away smiling\" shows kindness."),
            QUIZ("Which sentence is **descriptive** rather than narrative?",
                 ["Then we left the market and went home.", "The stalls leaned together, bright with oranges, tomatoes and plastic basins.",
                  "I bought a bag of rice and paid 2,000 FCFA.", "After lunch, my uncle called me."], 1,
                 "Only the second sentence tells what the place looks like. The others tell events.",
                 hint="Which one answers 'What is it like?' and not 'What happened?'",
                 feedback=["It reports an event in time.", "", "It reports an action.", "It reports an event in time."]),
            EX("Worked example 2: plan a description of a place", intro="Plan an essay: Describe your village or neighbourhood at dawn.",
               steps=[
                S("Dominant impression", text="Calm waking: quiet but starting to move."),
                S("Order", text="By time: first light, then early workers, then the full morning."),
                S("Senses", text="Sight: mist on the hills. Sound: cocks crowing. Smell: wood smoke. Touch: cold air."),
                S("Paragraphs", text="One paragraph for each stage of dawn, then a short ending that returns to the impression."),
            ]),
            QUIZ("Which is the best simile?", ["The sun was hot.", "The sun was a hot.", "The sun burned the roof like a coal oven.",
                                                 "The sun burn very much."], 2,
                 "A simile uses *like* or *as* to compare two different things, and here the sun and a coal oven.",
                 hint="Look for a comparison with like or as.",
                 feedback=["It is a plain statement, not a comparison.", "It is ungrammatical and not a comparison.", "",
                           "It is ungrammatical, and no comparison is made."]),
            PQ("List two details for each of sight, sound and smell for the topic: A bus park at five in the afternoon.",
               "Sight: buses with painted names; passengers waving. Sound: conductors shouting destinations; horns. "
               "Smell: diesel smoke; roasting plantain. (Any sensible details that fit the scene are correct.)"),
            PQ("Rewrite with an exact picture: \"My mother is a nice woman.\"",
               "Example: \"My mother greets everyone with a wide smile, and she always saves a bowl of food for the "
               "hungry child at our gate.\" (The sentence shows kindness with details.)"),
            PQ("Name two orders you can use to organise a description and say when each is useful.",
               "Space order (near to far) for a place or object; time order (morning to evening) for a place that changes. "
               "Order of importance can also be used."),
            SUM("A descriptive essay shows what something is like. It does not tell a plot.",
                "Describe only what the topic asks: one place, one person or one event.",
                "Use the five senses and exact words. Replace general words by details.",
                "Choose an order (space, time or importance) and show it with clear paragraph openings.",
                "Use a few fresh similes and metaphors, and keep a single tense."),
        ],
    ),
    # ------------------------------------------------------------------ 3. Expository essays
    lesson(
        module=M_WRITE, topic="Expository and argumentative essays",
        title="Expository essays: explaining clearly",
        slug="ewr-expository-essays",
        minutes=21,
        summary="How to explain a topic in an expository essay: a clear introduction, body paragraphs built on topic sentences "
                "and support, links to your own locality, balanced treatment, and a conclusion that does not repeat.",
        objectives=[
            "Say what an expository essay does and how it differs from an argument",
            "Build a body paragraph with a topic sentence, explanation and example",
            "Link ideas to a given locality or situation instead of writing in general",
            "Use linking words correctly and avoid non-existent connectives",
        ],
        key_concepts=["Expository essay", "Topic sentence", "Supporting detail", "Transitional words", "Conclusion"],
        blocks=[
            H("Introduction"),
            T("When electricity or piped water reaches a village, people ask, \"What will change?\" A good answer explains the "
              "change step by step: before, after, results. That is what an **expository essay** does. It **explains** or "
              "**informs**. It does not try to win an argument."),
            D("An **expository essay** explains a topic, a process, a cause and effect, or a situation, using facts, examples and "
              "clear reasoning. The writer informs; the writer does not just give opinions.", title="Definition"),
            KEY("Kinds of expository task", "The words of the topic show what is needed.", cards=[
                ["Explain how", "A process: steps in order (how to make palm oil, how to apply for an ID card)."],
                ["Explain why", "Causes: reasons something happens (why students drop out)."],
                ["What are the effects", "Results: before and after, good and bad (new road in your town)."],
                ["What is", "A definition with examples (what is corruption)."],
            ]),
            H("Structure"),
            T("An expository essay has three parts. The **introduction** names the subject, gives a short background, and says "
              "what the essay will show. Each **body paragraph** deals with one idea. The **conclusion** sums up the main "
              "point in new words and may look ahead."),
            CODE("""Introduction : topic + background + what will be explained (2-4 sentences)
Body 1       : first idea (topic sentence, explanation, example)
Body 2       : second idea
Body 3       : third idea
Conclusion   : the main point in a few sentences; no brand-new ideas""", "text", title="Layout of the essay"),
            H("The body paragraph"),
            T("Each body paragraph begins with a **topic sentence**: one sentence that gives the main idea. The rest of the "
              "paragraph explains it with a reason and an example. A useful pattern is Point, Explain, Example."),
            EX("Worked example 1: one body paragraph", intro="Topic: Electricity has just been installed in your village. How has "
               "this affected life? Write one paragraph on night-time activities.", steps=[
                S("Topic sentence", text="\"Electricity has changed life after dark in our village.\""),
                S("Explain", text="Before, families used kerosene lamps and went to bed at seven; now students can study at night."),
                S("Example", text="Mama Eyong now sells cold drinks until nine at her small shop beside the road."),
                S("Join them", text="Electricity has changed life after dark in our village. Before, families used kerosene lamps and "
                  "went to bed early; now students study at night. For example, Mama Eyong sells cold drinks until nine at her shop."),
            ]),
            TIP("A topic about \"your locality\" asks you to use the **local** picture: your own area before and after. If you write only "
                "general advantages of electricity, you have not answered the question. Include difficulties too, such as "
                "bills or accidents, so that the picture is complete and fair.", title="Link to your locality"),
            H("Linking your ideas"),
            T("Transitional words guide the reader. Use them correctly:\n\n"
              "**Adding:** firstly, secondly, also, moreover, furthermore, in addition. **Contrast:** however, nevertheless, on the "
              "other hand. **Cause and result:** therefore, as a result, consequently. **Example:** for instance, for example."),
            MISTAKE("Using connectives that do not exist",
                    "Write firstly, also, however, nevertheless, moreover, furthermore, in addition. Do not write \"nextly\", "
                    "\"better still\", \"more still\", \"more again\" or \"further still\"; these are not accepted English "
                    "connectives. Also, \"moreso\" is wrong; write \"more so\" when you mean \"even more\". Do not use two "
                    "connectives for the same idea in one sentence, such as \"However, but...\"."),
            MISTAKE("Listing instead of writing continuous prose",
                    "Do not write \"1. Advantages: good light. 2. Disadvantages: bills\". Use paragraphs with full sentences. Do not "
                    "put titles inside paragraphs, and do not write headings such as \"Content\", \"Expression\" or \"Accuracy\"."),
            QUIZ("Which sentence is the best topic sentence for a paragraph about the effect of a new road on trade in a village?",
                 ["Roads are long.", "The new road has made it easier for farmers to sell their crops in town.",
                  "My uncle drives a truck.", "There are many roads in Cameroon."], 1,
                 "A topic sentence names the one main idea of the paragraph, and here that the road helps farmers sell crops.",
                 hint="Which sentence sums up an effect on trade?",
                 feedback=["It is a general statement and gives no main idea about trade.", "",
                           "It is a personal detail that does not state an effect.", "It is too general and does not link to the village."]),
            EX("Worked example 2: plan the whole essay", intro="Topic: Explain why some students drop out of school.", steps=[
                S("Introduction", text="Define the problem; say that causes are money, early marriage or pregnancy, and loss of interest."),
                S("Body 1", text="Money: school fees and uniforms are hard for some families. Example: a child sent to trade."),
                S("Body 2", text="Home pressure: work on farms, early marriage. Body 3: school factors, such as long distances or weak teaching."),
                S("Conclusion", text="Sum up the causes and say that education helps families and the nation."),
            ]),
            PQ("Write a topic sentence for a paragraph on the effect of mobile money on small traders.",
               "Example: \"Mobile money has made it safer and faster for small traders to receive payment.\" (A single sentence "
               "naming one clear effect.)"),
            PQ("Correct the connectives: \"Firstly, the road is bad. Nextly, it is dusty. Moreso, it floods in rain.\"",
               "Firstly, the road is bad. Secondly, it is dusty. Moreover, it floods in rain. (\"Nextly\" and \"moreso\" are not "
               "acceptable.)"),
            PQ("What is the difference between an expository essay and an argumentative essay?",
               "An expository essay explains or informs; it gives facts, causes, effects or steps. An argumentative essay takes a "
               "side on a debatable statement and tries to convince the reader."),
            SUM("An expository essay explains or informs, using facts and examples.",
                "It has an introduction, body paragraphs (one idea each) and a conclusion.",
                "Begin each paragraph with a topic sentence, then explain and give an example.",
                "Link ideas with real connectives (firstly, moreover, however) and never with \"nextly\" or \"moreso\".",
                "Use your own locality when the topic says so, and give a balanced picture."),
        ],
    ),
    # ------------------------------------------------------------------ 4. Argumentative essays
    lesson(
        module=M_WRITE, topic="Expository and argumentative essays",
        title="Argumentative and debate essays: persuading with reasons",
        slug="ewr-argumentative-essays",
        minutes=23,
        summary="How to write an argumentative essay on a motion: take a clear side, acknowledge the opposing view, refute it, give "
                "developed arguments for your side, and finish with a firm conclusion. Also how a debate speech differs.",
        objectives=[
            "Recognise motions that ask for an argument (Do you agree? Discuss.) and those that ask for a list of advantages and disadvantages",
            "Use the sequence: introduction, opposing view, refutation, arguments for, conclusion",
            "Develop each argument with reason and example, and not only state it",
            "Write the opening and closing of a debate speech",
        ],
        key_concepts=["Motion", "Thesis", "Counter-argument", "Refutation", "Evidence", "Debate speech"],
        blocks=[
            H("Introduction"),
            T("At a family meeting someone says, \"Girls should not go to school beyond Form 3.\" Several people disagree. The "
              "person who speaks best does not shout: that speaker gives reasons, answers the other side, and ends with a "
              "clear position. An **argumentative essay** works the same way, in writing."),
            D("An **argumentative essay** takes a side on a debatable statement (a **motion**) and uses reasons and examples to "
              "convince the reader. A debate essay is an argumentative essay written as a speech or in debate form.",
              title="Definition"),
            H("Read the motion carefully"),
            T("Typical forms of the task: \"Do you agree?\", \"Discuss\", \"To what extent...?\", \"Write a speech for or against "
              "the motion...\". In each case you must **take a side**. Do not write the \"advantages and disadvantages\" of "
              "the thing unless the topic asks for that. They are two different tasks."),
            MISTAKE("Writing advantages and disadvantages when asked \"Do you agree?\"",
                    "A motion such as \"The teaching of mother tongue in schools is necessary. Do you agree?\" needs a decision and "
                    "arguments to support it. A list of good and bad points without a position does not answer it. Also, "
                    "know the key terms: *mother tongue* means the first language a person learns from the family."),
            KEY("The order of an argument", "A reliable pattern for most motions:", cards=[
                ["1. Introduction", "Explain key terms and state your position (your thesis)."],
                ["2. Opposing view", "Say fairly what the other side believes."],
                ["3. Refutation", "Show why the opposing view is weak or incomplete."],
                ["4. Your arguments", "Two or three paragraphs: point, reason, example, link back to the motion."],
                ["5. Conclusion", "Restate your position in new words and end firmly."],
            ]),
            IMG("f5en-wr-argument-order.svg", alt="Five boxes joined by arrows: introduction with position, opposing view, refutation, your arguments, conclusion.", caption="Figure 1. The order of an argumentative essay."),
            TIP("Do not write a one-sided essay in which the other side is never mentioned. A strong writer shows that "
                "the opposing view was considered and then explains why it is not convincing. Arguments for your side must "
                "be **developed**: say why, give an example, and connect it to the motion.", title="Exam link"),
            H("A model outline"),
            CODE("""Motion: Mobile phones should be banned in secondary schools. Do you agree?
Position: I disagree. (Phones should be controlled, not banned.)

Intro    : Define "banned"; state position.
Other side: Phones distract students and are used for cheating.
Refute   : Distraction is a discipline matter; rules (phones locked in bags in class) solve it.
Argument 1: Phones give access to lessons and past questions (example: free revision on educational websites).
Argument 2: Safety: parents can contact children on the road home.
Argument 3: Digital skills are needed for work in Cameroon.
Conclusion: Control with rules, do not ban.""", "text", title="Outline of an argumentative essay"),
            EX("Worked example 1: write a refutation", intro="The opposing view: \"A ban will stop cheating.\" Write two sentences "
               "that refute it.", steps=[
                S("State their view fairly", text="\"Some people say that a ban would stop cheating.\""),
                S("Give the weakness", text="\"However, students can hide phones, so a ban is difficult to enforce.\""),
                S("Give a better solution", text="\"Strong exam supervision is a better way to stop cheating than a total ban.\""),
            ]),
            H("Developing an argument"),
            T("An argument has four parts: **Point** (the claim), **Reason** (why), **Example** (a real case), **Link** (back "
              "to the motion). Compare:"),
            CODE("""Weak   : Phones help students.

Strong : Phones help students to revise on their own. For example, a student in
         a village with no library can read past questions on a phone. This
         shows that a ban would remove an important learning tool.""", "text", title="Undeveloped and developed"),
            H("Debate speech"),
            T("If the task is a speech for or against a motion, add the speech opening and closing: address the audience "
              "(\"Madam Chairperson, honourable judges, fellow students\"), state which side you speak for, then use the same "
              "argument order. End with a clear call: \"For these reasons I strongly oppose the motion. Thank you.\""),
            QUIZ("A candidate writes only the benefits of the motion and never mentions the opposing view. What is the main weakness?",
                 ["The essay is too short.", "The essay is one-sided; it does not acknowledge and refute the other side.",
                  "The essay has too many examples.", "The essay uses formal language."], 1,
                 "A strong argument deals with the opposing view, for example by acknowledging it and then refuting it.",
                 hint="What should come after your introduction and before your own arguments?",
                 feedback=["Length is not the main weakness here.", "", "Examples are good; they develop an argument.",
                           "Formal language is suitable in an argument."]),
            EX("Worked example 2: choose the right approach", intro="Which task needs an argument: (a) \"Discuss the advantages and "
               "disadvantages of village markets\", or (b) \"Village markets should be moved out of town. Do you agree?\"",
               steps=[
                S("Read the key words", text="(a) asks for advantages and disadvantages. (b) asks \"Do you agree?\"."),
                S("Decide", text="(b) is a motion, so you must choose a side and argue."),
                S("Answer", text="Task (b) needs an argumentative essay; task (a) needs a balanced expository discussion."),
            ]),
            QUIZ("Which sentence is a good thesis (position) for \"Students should wear school uniform. Do you agree?\"",
                 ["School uniforms are cloth.", "I strongly agree that students should wear school uniform because it builds equality and discipline.",
                  "Some students like uniform and some do not.", "Uniform is sold in the market."], 1,
                 "A thesis states a clear position and gives a reason in one sentence.",
                 hint="Which one clearly takes a side?",
                 feedback=["It states a fact but no position.", "", "It is neutral and takes no side.", "It states a fact but no position."]),
            PQ("Write the opening sentence of a debate speech against the motion \"Homework should be abolished\".",
               "Example: \"Madam Chairperson, honourable judges and fellow students, I stand firmly against the motion that "
               "homework should be abolished.\""),
            PQ("Write a developed argument (three sentences) for the statement: \"Students should learn practical skills at school.\"",
               "Example: \"Practical skills prepare students for work. For instance, a student who learns tailoring or computer "
               "repair can earn a living after Form 5 if there is no job. This shows that practical lessons must be part of school.\""),
            PQ("List the five parts of an argumentative essay in order.",
               "Introduction with position; the opposing view; refutation; arguments for your side (developed); conclusion."),
            SUM("An argumentative essay takes a side on a motion and persuades with reasons and examples.",
                "\"Do you agree?\" needs a position, not a list of advantages and disadvantages.",
                "Use the order: introduction, opposing view, refutation, arguments for, conclusion.",
                "Develop each argument: point, reason, example, link to the motion.",
                "A debate speech adds a greeting to the audience and a closing such as \"Thank you\"."),
        ],
    ),
    # ------------------------------------------------------------------ 5. Formal letters
    lesson(
        module=M_WRITE, topic="Formal letters",
        title="Formal letters: applications, complaints and letters to an editor",
        slug="ewr-formal-letters",
        minutes=25,
        summary="The layout, tone and endings of a formal letter, with model letters of application, complaint and to an editor "
                "shown in full. Use only the names and addresses given in the task and never your own.",
        objectives=[
            "Lay out a formal letter: sender's address, date, receiver, salutation, heading, body, ending, signature",
            "Match Yours faithfully to Dear Sir or Madam, and Yours sincerely to a named person",
            "Write an application, a complaint and a letter to an editor in a formal tone",
            "Use only the names and addresses in the task and never disclose your own identity",
        ],
        key_concepts=["Formal letter", "Salutation", "Subject heading", "Yours faithfully", "Formal tone", "Letter to an editor"],
        blocks=[
            H("Introduction"),
            T("When a school leaver in Douala wants a job in a bank, or a customer wants a faulty phone replaced, or a "
              "citizen wants to tell the public that a road is dangerous, each person writes to someone they may never meet. "
              "The letter must be clear, polite and correctly set out. That is a **formal letter**."),
            D("A **formal letter** is written to a person or office with whom you have no close personal relationship: an employer, "
              "a head of institution, an official or a newspaper editor. It is polite, direct, free from slang and from short forms.",
              title="Definition"),
            TIP("Formal letters are written in Paper 2, as a directed writing task or a composition. The task gives you the "
                "names and addresses to use. **Use exactly those.** Do not write your own name, school or telephone number: "
                "disclosing identity is penalised. Your layout, tone and format all count.", title="Exam link"),
            H("The layout"),
            T("There are two usual layouts: **blocked** (every line starts at the left) and **indented**. Ask your teacher which is "
              "preferred and use it consistently. The parts are the same in both."),
            CODE("""                                   P.O. Box 214, Mankon
                                   Bamenda
                                   12th March 2026

The Manager,
Green Valley Supplies Ltd,
P.O. Box 88, Bamenda.

Dear Sir,                                   <- salutation

APPLICATION FOR THE POST OF SALES ASSISTANT <- subject heading

First paragraph: why you are writing.
Second paragraph: your qualifications and experience.
Third paragraph: other details, and thanks.

Yours faithfully,                           <- ending
(signature)
Nkeng Atabong                               <- name (the one given in the task)""", "text", title="Layout of a formal letter"),
            IMG("f5en-wr-letter-layout.svg", alt="A letter page showing, from top to bottom: sender's address and date on the right, receiver's name and address, salutation, subject heading, three body paragraphs, the ending and the signed name.", caption="Figure 1. The parts of a formal letter, top to bottom."),
            KEY("Salutation and ending must match", "This is a point examiners look for.", cards=[
                ["Dear Sir / Dear Madam / Dear Sir or Madam", "End with Yours faithfully."],
                ["Dear Mr Ayuk / Dear Mrs Ewane", "End with Yours sincerely."],
            ]),
            H("Model 1: letter of application"),
            T("An application letter says which job you want, why you are suitable and what you can offer. Keep it to the point."),
            CODE("""                                   P.O. Box 214, Mankon
                                   Bamenda
                                   12th March 2026

The Manager,
Green Valley Supplies Ltd,
P.O. Box 88,
Bamenda.

Dear Sir,

APPLICATION FOR THE POST OF SALES ASSISTANT

I write to apply for the post of sales assistant advertised on Radio Hill FM
on 8th March 2026.

I hold the GCE Ordinary Level in six subjects, including English Language
and Mathematics. I worked for two months as a shop assistant in my uncle's
store, where I learned to keep records and serve customers politely. I can
use a computer and mobile money.

I am hardworking and honest, and I will be available for interview at any
time. I have enclosed copies of my certificates and two references.

I hope that my application will be considered favourably.

Yours faithfully,
(signature)
Nkeng Atabong""", "text", title="Model letter 1: application"),
            H("Model 2: letter of complaint"),
            T("A complaint says what went wrong, when, what it caused, and what you want done. Stay calm and polite, however angry you feel."),
            CODE("""                                   12 Mile 3 Road
                                   Limbe
                                   4th May 2026

The Customer Service Manager,
Blue Wave Electronics,
P.O. Box 410, Douala.

Dear Sir or Madam,

COMPLAINT ABOUT A FAULTY LAPTOP

On 20th April 2026 I bought a laptop (model BW-15) from your Limbe shop
for 285,000 FCFA. The receipt number is 0412.

Within five days the screen began to flicker, and it now goes black without
warning. I took it back on 29th April, and the salesperson promised to repair
it in three days. It has still not been repaired.

I therefore request a replacement or a full refund within seven days.
I look forward to your quick reply.

Yours faithfully,
(signature)
Fonyuy Ndifor""", "text", title="Model letter 2: complaint"),
            H("Model 3: letter to an editor"),
            T("A letter to a newspaper editor shares an opinion on a public matter in order to influence readers. It names the "
              "problem, gives reasons and suggests a solution. The editor's title is the receiver."),
            CODE("""                                   Box 56, Kumba
                                   2nd June 2026

The Editor,
The Daily Voice,
P.O. Box 1001, Douala.

Dear Sir,

DANGEROUS ROAD AT KUMBA JUNCTION

I wish to draw the attention of the authorities, through your newspaper, to the
state of the road at Kumba Junction.

Deep holes have formed after the rains. Last week a motorbike rider fell and
was injured, and taxis now drive on the wrong side to avoid the holes.
Children who walk to school are in danger.

I urge the Council to repair the road quickly, and drivers to slow down.

Yours faithfully,
(signature)
Mbua Enow""", "text", title="Model letter 3: to an editor"),
            MISTAKE("Mixing up the endings",
                    "\"Dear Sir\" followed by \"Yours sincerely\" is wrong. Use Yours faithfully with Dear Sir or Madam, and Yours sincerely only "
                    "when you use the person's name (Dear Mr Ayuk). Also write \"Yours faithfully\" with a small f in faithfully."),
            MISTAKE("Using your own details",
                    "If the task gives \"Your name is Fonyuy Ndifor, P.O. Box 214, Mankon\", use that. Never write your own name, "
                    "school, parents' names or phone number. Use the receiver's address as given, too."),
            QUIZ("A letter begins \"Dear Madam,\". Which ending is correct?",
                 ["Yours sincerely,", "Yours faithfully,", "Your loving friend,", "Best wishes,"], 1,
                 "Dear Sir or Madam goes with Yours faithfully in a formal letter.",
                 hint="Is the person named in the salutation?",
                 feedback=["That ending is for a named person, such as Dear Mr Ayuk.", "", "It is informal, for a friend.",
                           "It is not suitable in a formal letter."]),
            QUIZ("Which line is the best subject heading for a letter of complaint about late delivery?",
                 ["I am very angry!", "COMPLAINT ABOUT LATE DELIVERY OF MY ORDER", "Hello", "Please help me, sir, I beg"], 1,
                 "A subject heading is short and names the matter, often in capitals or underlined.",
                 hint="The heading should tell the reader what the letter is about.",
                 feedback=["It is an emotion and not a subject.", "", "It says nothing about the matter.", "It is a request, too long and emotional for a heading."]),
            EX("Worked example 1: choose the right ending", intro="You write to \"The Principal, Government Bilingual High School, "
               "Kribi\" and you do not know the name. Which ending do you choose?", steps=[
                S("Look at the salutation", text="\"Dear Sir or Madam\" has no name."),
                S("Match", text="No name means Yours faithfully."),
                S("Write", text="Yours faithfully, then your signature and the name given in the task."),
            ]),
            EX("Worked example 2: plan a letter of complaint", intro="Plan a complaint about noise from a night club near your school.",
               steps=[
                S("Receiver and heading", text="The Divisional Officer; \"COMPLAINT ABOUT NOISE NEAR THE SCHOOL\"."),
                S("Paragraph 1", text="Say who you are in role (a concerned resident, using the name given) and why you write."),
                S("Paragraph 2", text="The problem: noise until 2 a.m., students cannot study; give dates."),
                S("Paragraph 3", text="Request: restrict opening hours; thank the officer."),
            ]),
            PQ("Write the opening paragraph of an application for the post of laboratory assistant.",
               "I write to apply for the post of laboratory assistant advertised in The Daily Voice of 10th June 2026. "
               "(State the post, where you saw it and the date.)"),
            PQ("Why should the tone of a letter to an editor be polite even when the writer is angry?",
               "A polite, calm letter is taken seriously and is more likely to be published and acted on. Angry or insulting "
               "language weakens the case and is not formal."),
            PQ("A letter begins \"Dear Mr Ewane,\". Write the closing and the name line (the writer is Tabe Mofor).",
               "Yours sincerely,\n(signature)\nTabe Mofor"),
            SUM("A formal letter has: sender's address, date, receiver, salutation, subject heading, body, ending, name.",
                "Dear Sir or Madam goes with Yours faithfully. Dear Mr Ayuk goes with Yours sincerely.",
                "An application states the post, your qualifications and your availability; a complaint states the facts and what you want.",
                "A letter to an editor names a public problem, gives reasons and suggests action.",
                "Use only the names and addresses in the task. Never write your own identity. Check your teacher's preferred layout."),
        ],
    ),
    # ------------------------------------------------------------------ 6. Informal and semi-formal letters
    lesson(
        module=M_WRITE, topic="Informal and semi-formal letters",
        title="Informal and semi-formal letters",
        slug="ewr-informal-letters",
        minutes=22,
        summary="How to write to a friend or relative (informal) and to a respected person you know, such as a teacher or an elder "
                "(semi-formal): layout, opening, news about yourself, family and town, convincing advice, and endings.",
        objectives=[
            "Lay out an informal letter and use warm, natural but correct English",
            "Tell the difference between informal and semi-formal tone",
            "Include news about yourself, your family and your town when the task asks",
            "Persuade a friend or relative with reasons and encouragement",
        ],
        key_concepts=["Informal letter", "Semi-formal letter", "Tone", "Opening and closing", "News", "Persuasion"],
        blocks=[
            H("Introduction"),
            T("In many villages in Cameroon, a young person who left home writes to a cousin still in the village. The words are "
              "warm and personal, and the cousin is told news and given advice. Another letter is written to the school "
              "headmaster or the village chief by a former student. It is friendly but respectful. These are **informal** and "
              "**semi-formal** letters."),
            D("An **informal letter** is written to a friend, a brother or sister, a cousin or another close person. The tone is "
              "friendly and natural. A **semi-formal letter** is written to a person you know but must respect, such as a teacher, "
              "an uncle, an elder or a family friend. It is warm, but polite and without slang.", title="Definitions"),
            KEY("Compare the three kinds of letter", "", cards=[
                ["Formal", "To an office or stranger. Dear Sir. Yours faithfully. No contractions."],
                ["Semi-formal", "To a known, respected person. Dear Uncle / Dear Mr Njoh. Polite, warm, few contractions."],
                ["Informal", "To a friend or relative. Dear Emblem. Friendly, natural, contractions allowed."],
            ]),
            TIP("In Paper 2, an informal letter task usually gives the names and the address of the writer. Use **exactly** those. "
                "Also read what the letter must contain: news about yourself, your family and your town, and then the purpose (such "
                "as convincing a relative to return to school). A letter that forgets the purpose, or the news, loses marks.",
                title="Exam link"),
            H("Layout of an informal letter"),
            T("The receiver's address is **not** written; only the sender's address and the date. The greeting uses the first name."),
            CODE("""                                   P.O. Box 77, Dimba
                                   9th November 2026

Dear Emblem,                                <- greeting (first name)

How are you? I hope you and everyone at home are well. I am well.    <- warm opening

Main paragraphs: news, then the purpose of the letter.

Closing paragraph: greetings and a promise to write.

Your cousin,                                <- ending: Yours, / Your friend, / Your loving cousin,
Dada                                        <- the name given in the task""", "text", title="Layout of an informal letter"),
            H("Model: a letter to persuade"),
            T("A cousin has left school to farm in the village. The writer encourages him to return."),
            CODE("""                                   P.O. Box 77, Dimba
                                   9th November 2026

Dear Emblem,

How are you? I hope you and everyone at home are well. I am fine, and so are
Mum and Dad. My little brother has just started primary school, and he is
already teaching us songs.

Dimba is growing. A new bridge is being built over the stream, and our
neighbours opened a small bakery near the junction.

Now to my reason for writing. I was sad to hear that you left school. I know that
farming is hard work and that school fees are a problem, but your education
is the best investment you can make. With a certificate you can learn a trade,
train as a teacher or nurse, or even manage a farm better. Without it, your
choices will be very few. Besides, you can ask the school about payment
in parts, and I will gladly send you my old books.

Please think seriously about it and come back to school next term.

Greet your parents for me. Write soon.

Your cousin,
Dada""", "text", title="Model informal letter"),
            H("Model: a semi-formal letter"),
            CODE("""                                   Hostel 4, Buea
                                   5th February 2026

Dear Mr Njoh,

I hope you and the staff of the school are well. I am writing to thank you
for your advice in my last year in school, and to ask for your help.

I am now studying in Buea. I would like you to write a short testimonial
about my conduct for a scholarship application. I shall be grateful if you
could send it by the end of this month.

Thank you once again for all you did for me.

Yours sincerely,
Atem Ndong""", "text", title="Model semi-formal letter"),
            MISTAKE("Writing like a text message",
                    "Even in a letter to a friend, write full words: \"you\", not \"u\"; \"because\", not \"coz\". Slang, "
                    "abbreviations and mixing Pidgin or French into English are not accepted in an examination letter."),
            MISTAKE("Forgetting the news or the purpose",
                    "If the task says to give news about yourself, your family and your town and then to convince the relative, "
                    "write about all of them. Spending the whole letter on the news, or the whole letter on persuasion, "
                    "leaves out part of the task."),
            H("Persuading kindly"),
            T("To convince a friend, use three steps: show you understand the person's problem, give two or three reasons, and "
              "offer help. Use encouraging words (\"I know you can do it\") and not blame (\"you were foolish\")."),
            QUIZ("Which closing is suitable for a letter to your cousin?",
                 ["Yours faithfully,", "Your cousin,", "Respectfully yours, Sir,", "Yours truly, The Principal,"], 1,
                 "A personal ending such as Your cousin or Your friend suits an informal letter.",
                 hint="Who is the receiver: an office or a close relative?",
                 feedback=["It belongs to formal letters with Dear Sir or Madam.", "", "It is too distant for a cousin.",
                           "It is formal and wrongly names an office."]),
            QUIZ("A letter to your old teacher, Mr Njoh, is best written in which tone?",
                 ["Very slangy and funny, as for a classmate", "Polite and warm, without slang", "Cold and official as to a stranger", "Angry"], 1,
                 "A teacher is known but respected, so a semi-formal tone is correct.",
                 hint="Is Mr Njoh a stranger, a friend or a respected person you know?",
                 feedback=["Slang is disrespectful to a teacher.", "", "Cold language is too distant for someone you know.",
                           "Anger is not suitable."]),
            EX("Worked example 1: sort the openings", intro="Which opening suits an informal letter: (a) \"I write to complain\", (b) "
               "\"How are you? I hope the family is well.\", (c) \"With reference to your advertisement\"?", steps=[
                S("Think about the receiver", text="A close person: warm greeting."),
                S("Eliminate", text="(a) and (c) are formal."),
                S("Answer", text="(b)."),
            ]),
            EX("Worked example 2: plan a letter of news and advice", intro="Plan a letter to your friend Ngum, who plans to leave school "
               "and travel to town.", steps=[
                S("Paragraph 1", text="Greeting, health, thanks for his last letter."),
                S("Paragraph 2", text="News: yourself, family, the town (use details from the task)."),
                S("Paragraph 3", text="Purpose: show the risks of leaving school, give reasons to stay, offer help."),
                S("Paragraph 4", text="Greetings to family; \"Your friend, (given name)\"."),
            ]),
            PQ("Write the first paragraph of an informal letter to a friend called Ayuk.",
               "Dear Ayuk,\n\nHow are you? I hope you and your family are well. I am fine, and I was happy to get your letter last week."),
            PQ("Name one difference between an informal and a semi-formal letter.",
               "An informal letter is friendly and natural and may use contractions; a semi-formal letter is respectful and "
               "warm, and does not use slang. (Greeting and ending may also differ.)"),
            PQ("Correct: \"Dear friend, u should come to school coz it's gud for ur future.\"",
               "Dear friend, you should come to school because it is good for your future."),
            SUM("Informal letters are to close people; semi-formal letters are to respected people you know.",
                "Write the sender's address and date; the receiver's address is not needed in an informal letter.",
                "Open warmly, give the news the task asks for, then state the purpose and persuade with reasons.",
                "Use full words, no text language, no slang, no Pidgin or French.",
                "Use only the names and address in the task; never your own."),
        ],
    ),
    # ------------------------------------------------------------------ 7. Speeches, talks, articles
    lesson(
        module=M_WRITE, topic="Speeches, articles, reports and minutes",
        title="Speeches, talks and articles from a stimulus",
        slug="ewr-speeches-and-articles",
        minutes=25,
        summary="How to write a speech, a talk or a newspaper article in a directed writing task: format, role and audience, "
                "selecting all relevant material from the stimulus, using your own words and keeping to the limits, with a model answer.",
        objectives=[
            "Set out a speech or talk with a greeting, theme and closing, and an article with headline and introduction",
            "Identify role, audience, purpose and tone from a task",
            "Select ALL relevant points from a stimulus and use nothing else",
            "Write in your own words, without lifting, and respect the word and paragraph limits",
        ],
        key_concepts=["Speech", "Talk", "Article", "Role and audience", "Selecting material", "Lifting", "Slanting"],
        blocks=[
            H("Introduction"),
            T("At a market association meeting, the chairman stands and says, \"Fellow traders, today I want to talk about "
              "keeping our market clean.\" He greets his listeners, states his theme, makes his points, and ends politely. A "
              "good written speech follows the same path. A newspaper article is different: it has a headline and it "
              "informs a reader in print.\n\n"
              "In Paper 2, Section A (Directed Writing), you are given a stimulus (a passage, notes, a table or a notice) and a "
              "task. You must write a talk, speech, article, letter or report using **only** that stimulus."),
            D("**Directed writing** is a task in which you use information from a stimulus to produce a text of a stated "
              "kind for a stated audience, within stated word and paragraph limits.", title="Definition"),
            TIP("Typical Board advice: select ALL relevant material; use only the stimulus and not your own knowledge; "
                "obey the word and paragraph limits; write in your own words; do not give your name, school or other identity; "
                "write in black or blue ink; plan and cross out the plan.", title="Exam link"),
            H("Step 1: read the task, find the role"),
            T("Underline four things in the task: **role** (who you are), **audience** (who you speak or write to), **purpose** "
              "(to persuade, inform, advise), and **format** (speech, talk, article). The role matters. If you are the workers' "
              "representative, write as one worker speaking to workers, not as the manager."),
            H("Step 2: the format of a speech or talk"),
            CODE("""Greeting  : Fellow workers, ladies and gentlemen,   (address the audience)
Theme     : Today I wish to speak about keeping our market clean.   (state the topic)
Body      : points from the stimulus, in connected paragraphs
Closing   : Thank you for listening.""", "text", title="Speech or talk: the parts"),
            T("The greeting and the theme are often together at the start. The closing thanks the audience. Do not add a "
              "title, a date, a name or a signature. A speech is meant to be spoken, so use \"we\", \"you\" and a few direct "
              "appeals, but keep the language correct."),
            H("Step 3: select ALL relevant material"),
            T("Read the stimulus slowly. Underline every point that helps the task. Then check the list against the "
              "task: are any points missing? Are any off-topic? Examiners mark the **content points** you gave, so missing a "
              "point costs marks. Do not add your own ideas: even correct ideas that are not in the stimulus are not credited."),
            H("Step 4: your own words"),
            T("**Lifting** is copying phrases or sentences from the stimulus. Change the words and sentence shape while keeping the "
              "meaning. Use synonyms, change the order and join points with transitional words."),
            CODE("""Stimulus  : Traders throw waste on the ground, which blocks the drains.
Lifted    : Traders throw waste on the ground, which blocks the drains.
Own words : When we dump rubbish carelessly, it chokes the gutters.""", "text", title="Lifting and rewriting"),
            H("A model: stimulus and answer"),
            CODE("""STIMULUS (invented for practice)
The market association chairperson wants to talk to traders about waste.
Points noted: rubbish is dumped between stalls; drains are blocked and water
floods the stalls in rain; flies and bad smells keep customers away; the council
collects waste on Mondays and Fridays only; a skip is placed at the market gate;
the association will fine traders 1,000 FCFA for dumping; each trader should
sweep in front of the stall every evening.

TASK
You are the chairperson. Write a short talk to the traders. Use the information
above. (Not more than 130 words; one paragraph.)""", "text", title="Directed writing task"),
            CODE("""Fellow traders, today I wish to speak about keeping our market clean. Dumping rubbish
between the stalls blocks the drains, so water floods our goods when it rains.
Besides, flies and bad smells chase customers away from us. The council collects
waste on Mondays and Fridays, and a skip stands at the gate. Moreover, each of us must sweep in front of the stall every
evening. Anyone who dumps rubbish will pay a fine of 1,000 FCFA. If we do these
things, we shall protect our health and our business. Thank you for listening.""", "text", title="Model answer (about 95 words)"),
            T("Check the model. It has a greeting-and-theme opening and a closing. It contains all the points (dumping, drains, "
              "flooding, flies and smell, collection days, skip, fine, daily sweeping). It does not copy sentences, and it adds "
              "nothing from outside. It is one paragraph, in continuous prose, with real connectives (besides, moreover). "
              "The role (chairperson) is clear: \"our market\", \"each of us\"."),
            MISTAKE("Adding your own knowledge",
                    "You may know many other ways to keep a market clean, but the task says to use the stimulus. Extra ideas earn no "
                    "credit and can use up your word limit."),
            MISTAKE("Wrong paragraph or word limit",
                    "If the task says one paragraph, write one. If it says 130 words, do not write 200 or 70. Count your words "
                    "while you plan, not only at the end."),
            H("Writing an article"),
            T("A newspaper article has a **headline** (short and catchy), an **introduction** that answers who, what, where and when, "
              "body paragraphs with the details and a short ending. It is usually in the third person and in a formal, objective "
              "tone. If the task asks you to write as a reporter, never put your own name as the writer: use only what the "
              "task gives."),
            CODE("""HEADLINE : MARKET TRADERS TO FACE FINES FOR DUMPING WASTE
Intro    : Traders at the central market will pay a fine of 1,000 FCFA from next week if they
           dump rubbish between the stalls, the market association has announced.
Body     : reasons, the council collection days, the new skip, the daily sweeping rule
Ending   : a quote or a hopeful line, in your own words""", "text", title="Article: parts"),
            QUIZ("A task says: \"Write a talk to your co-workers.\" Which opening is best?",
                 ["Dear Sir, I write to...", "Fellow workers, today I wish to speak about...", "Once upon a time...",
                  "The following is a report of..."], 1,
                 "A talk begins with a greeting to the listeners and a statement of the theme.",
                 hint="A talk is spoken to an audience.",
                 feedback=["That begins a letter.", "", "That begins a story.", "That begins a report."]),
            QUIZ("You know an excellent point about recycling that is not in the stimulus. What should you do?",
                 ["Add it, because it is correct.", "Leave it out, because only the stimulus is used.", "Add it at the end only.",
                  "Replace one stimulus point with it."], 1,
                 "In directed writing, use the stimulus only. Your own knowledge earns no credit.",
                 hint="Where must all your points come from?",
                 feedback=["Correct is not enough; the task says to use the stimulus.", "", "Putting it at the end does not change the rule.",
                           "You would then lose a stimulus point."]),
            PQ("Write the opening sentence of a talk by a school prefect to students about punctuality.",
               "Fellow students, today I wish to speak to you about the importance of coming to school on time."),
            PQ("Rewrite in your own words: \"Many farmers lose their crops because roads are poor.\"",
               "Example: Bad roads cause many farmers to lose their harvest. (Any accurate rewording in your own words.)"),
            PQ("Give two things that an article needs that a speech does not.",
               "A headline and an introduction that answers who, what, where and when. (A speech uses a greeting and a "
               "closing of thanks instead.)"),
            SUM("In directed writing, use the stimulus only, select ALL relevant points and write in your own words.",
                "A talk or speech begins with a greeting to the audience and the theme, and ends with thanks for listening.",
                "An article has a headline, an introduction, a body and a short ending.",
                "Respect the word and paragraph limits, assume the role you are given and never disclose your identity.",
                "Plan, cross out the plan, write in continuous prose with real connectives, and write in black or blue ink."),
        ],
    ),
    # ------------------------------------------------------------------ 8. Reports and minutes
    lesson(
        module=M_WRITE, topic="Speeches, articles, reports and minutes",
        title="Reports and minutes of meetings",
        slug="ewr-reports-and-minutes",
        minutes=24,
        summary="The format of a report (title, introduction, findings, conclusion, recommendations) and of minutes of a meeting "
                "(heading, attendance, numbered items, adjournment, signatures), with model texts in impersonal, past-tense style.",
        objectives=[
            "Set out a report with a title, introduction, findings, conclusion and recommendations",
            "Set out minutes with heading, attendance, agenda items and signatures",
            "Use the past tense, the third person and reported speech in minutes",
            "Write in continuous prose when a task sets a paragraph limit",
        ],
        key_concepts=["Report", "Terms of reference", "Findings", "Recommendation", "Minutes", "Agenda", "Reported speech"],
        blocks=[
            H("Introduction"),
            T("A school Parent-Teacher Association (PTA) meets to discuss repairs to the school fence. Two weeks later, a parent "
              "who missed the meeting asks, \"What was decided?\" The answer is in the **minutes**. A head of department who "
              "has visited a school farm to see if it is safe will write a **report**. Both documents record facts for people "
              "who were not there. They must be clear, fair and in the right format."),
            D("A **report** is an organised account of what was investigated, what was found and what is recommended. "
              "**Minutes** are the official record of what was said and decided at a meeting.", title="Definitions"),
            TIP("Reports and minutes can be set as directed writing in Paper 2, so you must know the format. When the task gives a "
                "stimulus, use only the stimulus, respect the limits and do not use your own name or any identity. Check the task "
                "for the names, roles and dates to use.", title="Exam link"),
            H("The format of a report"),
            CODE("""TITLE : REPORT ON THE STATE OF THE SCHOOL LIBRARY
TO    : The Principal
FROM  : The Librarian (use only the role/name given in the task)
DATE  : 15th October 2026

1. Introduction (terms of reference): why the report was written and how facts were collected
2. Findings: what was discovered, in logical order (paragraphs or short numbered points)
3. Conclusion: what the findings mean
4. Recommendations: what should be done

(signature)
The Librarian""", "text", title="Report layout"),
            T("Reports are written in a formal, **impersonal** style, usually in the past tense for what was done and found, "
              "and in the present for the conclusion. Facts come first, then opinion."),
            H("Model report"),
            CODE("""REPORT ON THE STATE OF THE SCHOOL LIBRARY

To: The Principal
From: The Librarian
Date: 15th October 2026

Introduction
This report was written at the request of the Principal to describe the condition of the
school library. Information was gathered by counting books and by interviewing
twelve students.

Findings
The library has 450 books, but only 120 are in good condition. Most textbooks are more
than ten years old. The roof leaks near the shelves. Students said that the library
is too hot and that there are too few chairs.

Conclusion
The library does not fully meet the needs of students.

Recommendations
It is recommended that the roof be repaired, that new textbooks be bought and
that more chairs be provided.

(signature)
The Librarian""", "text", title="Model report (invented figures)"),
            MISTAKE("Mixing facts and personal feelings",
                    "Write \"Twelve students said the room was hot\", not \"I hate the library, it is terrible\". Keep opinion for "
                    "the recommendation and give a reason."),
            H("The format of minutes"),
            CODE("""MINUTES OF THE MEETING OF THE PTA HELD ON 12TH MARCH 2026 AT 3 P.M. IN THE SCHOOL HALL

Present: Mr Ayuk (Chairman), Mrs Ewane (Secretary), Mr Mbah, Mrs Tabe, ten other members
Absent with apology: Mr Enow
In attendance: The Principal

1. Call to order
The Chairman called the meeting to order at 3.10 p.m. and led an opening prayer.

2. Minutes of the last meeting
The minutes of the last meeting were read, corrected and adopted. Mrs Tabe proposed and
Mr Mbah seconded.

3. Matters arising
There were none.

4. Repair of the school fence
Mr Mbah reported that part of the fence had fallen. It was agreed that each parent
should pay 2,000 FCFA. The Treasurer would collect the money before 30th March.

5. Any other business
Mrs Tabe asked that parents be reminded about the end-of-term date.

6. Adjournment
There being no other business, the meeting was adjourned at 4.30 p.m.

Signed: ................ (Secretary)    ................ (Chairman)
Date: ................""", "text", title="Model minutes (invented names)"),
            T("Notice the style of minutes. They use the **past tense** and **reported speech** (\"Mr Mbah reported that...\"). They are in the "
              "third person. They record decisions and who must act (\"It was agreed that...\", \"The Treasurer would collect...\"). "
              "They give the substance of the talk, not every word."),
            KEY("Useful phrases for minutes", "", cards=[
                ["Opening", "The meeting was called to order at..."],
                ["Reporting", "The Chairman reported that... / Mrs Tabe suggested that..."],
                ["Decisions", "It was agreed that... / It was resolved that..."],
                ["Closing", "There being no other business, the meeting was adjourned at..."],
            ]),
            QUIZ("Which sentence is written in the correct style for minutes?",
                 ["Mr Mbah says, \"The fence is broken!\"", "Mr Mbah reported that part of the fence had fallen.",
                  "I think the fence is broken, said Mr Mbah.", "Mr Mbah will report about the fence."], 1,
                 "Minutes use the past tense and reported speech in the third person.",
                 hint="Minutes record what happened at a meeting that is over.",
                 feedback=["It is in the present tense and direct speech.", "", "It is in the first person and direct speech, with wrong punctuation.",
                           "It is in the future tense, but the meeting is over."]),
            QUIZ("Which section of a report gives a list of suggested actions?",
                 ["Introduction", "Findings", "Conclusion", "Recommendations"], 3,
                 "Recommendations state what should be done.",
                 hint="Which part looks forward and suggests action?",
                 feedback=["The introduction states the purpose.", "The findings give facts discovered.", "The conclusion says what the findings mean.", ""]),
            EX("Worked example 1: change direct speech to minutes", intro="At a meeting, the treasurer said, \"We have 80,000 FCFA in "
               "the account.\" Write this for the minutes.", steps=[
                S("Use the third person and past tense", text="\"The Treasurer reported that...\""),
                S("Shift the tense back", text="\"we have\" becomes \"the association had\"."),
                S("Write", text="\"The Treasurer reported that the association had 80,000 FCFA in the account.\""),
            ]),
            EX("Worked example 2: plan a report", intro="Plan a report for the Principal on student lateness.", steps=[
                S("Title and headings", text="REPORT ON LATENESS AMONG STUDENTS; To the Principal; From the Discipline Master; date."),
                S("Introduction", text="Purpose and method (a register check for two weeks)."),
                S("Findings", text="Number of latecomers, main reasons given (distance, transport), days with most lateness."),
                S("Conclusion and recommendations", text="Lateness is mostly caused by transport; start with an earlier assembly check and a punctuality prize."),
            ]),
            PQ("What are the four main parts of a report?",
               "Introduction (purpose and method), findings, conclusion, recommendations (with a title and To/From/Date above)."),
            PQ("Write in reported speech for minutes: The Secretary said, \"The next meeting will be on 5th May.\"",
               "The Secretary announced that the next meeting would be on 5th May."),
            PQ("Why do minutes end with signatures?",
               "The signatures of the Secretary (who wrote them) and the Chairman (who approved them) show that the record "
               "is official and accepted."),
            SUM("A report has a title, To/From/Date, introduction, findings, conclusion and recommendations.",
                "Use an impersonal, formal style: facts first, opinion only in the conclusion and recommendations.",
                "Minutes have a heading, a list of those present and absent, numbered items, adjournment and signatures.",
                "Minutes use the past tense, the third person and reported speech.",
                "If a task sets a paragraph or word limit, obey it and write in continuous prose; use only the names and facts given."),
        ],
    ),
    # ------------------------------------------------------------------ 9. Paper 1 strategy
    lesson(
        module=M_EXAM, topic="Paper 1",
        title="Paper 1: multiple-choice strategies for English Language",
        slug="eex-paper-1-strategy",
        minutes=22,
        summary="How English Paper 1 works (50 multiple-choice questions, 1 hour 30 minutes, marked electronically) and how to "
                "manage time, read passages, check grammar, handle stress and sound questions, and listen for key words.",
        objectives=[
            "Describe the structure of Paper 1 and calculate the average time for each question",
            "Use a two-pass method and elimination in multiple-choice questions",
            "Read a passage and its questions in an efficient order",
            "Answer grammar, vocabulary and phonology items by testing each option",
        ],
        key_concepts=["Paper 1", "Time per question", "Two-pass method", "Elimination", "Skimming", "Electronic marking"],
        blocks=[
            H("Introduction"),
            T("A candidate in Ebolowa sits down and sees an answer sheet and a question paper with fifty questions. There is no "
              "essay, only choices: A, B, C and D. It looks easy, and that is why many candidates lose marks: they hurry, "
              "or they spend ten minutes on one difficult question and then run out of time.\n\n"
              "This lesson gives you a **method** for Paper 1."),
            D("English Language **Paper 1** is **50 multiple-choice questions** covering **listening comprehension, reading "
              "comprehension, grammar and vocabulary**. The time allowed is **1 hour 30 minutes**. It is marked "
              "**electronically**.", title="Paper 1: the official facts"),
            T("Because the paper is marked by a machine, a clear answer is the only thing it can read. Follow the "
              "invigilator's instruction about how to mark the answer sheet. Mark one answer for each question. If you change "
              "your mind, erase the first mark completely as instructed. Check that the number on the sheet matches the "
              "number of the question you are answering."),
            TIP("Your English course gives you skills for each part of Paper 1: phonology and listening, grammar, vocabulary and "
                "register, and reading comprehension. This lesson shows how to use them under time pressure.", title="Exam link"),
            H("Time: about 1.8 minutes a question"),
            T("90 minutes divided by 50 questions is 1.8 minutes for each question. Some questions are quick (a sound or "
              "a word meaning, 20 seconds). Reading passages take longer, but they carry several questions at once. Do not "
              "let one question steal time from the others."),
            CODE("""Total time       : 90 minutes
First pass       : about 60 minutes. Answer every question you are sure of; skip the hard ones.
Second pass      : about 20 minutes. Return to skipped questions; eliminate and guess.
Final check      : about 10 minutes. Check the answer sheet for blanks and shifted numbers.""", "text", title="A time plan (KKEVO study advice)"),
            H("The two-pass method and elimination"),
            T("On the first pass, answer what you know and mark the doubtful ones. On the second, return to them. "
              "**Elimination** means crossing out options that cannot be right until one remains. There is usually one "
              "correct answer and three that are wrong for a reason. Never leave a question blank; a guess from two options is "
              "better than a blank."),
            H("Reading comprehension items"),
            T("Do this: (1) Read the **questions first** quickly, to know what to look for. (2) Read the passage once for the "
              "main idea. (3) Go back for each question and find the line that answers it. (4) Choose the option that "
              "matches the **passage**, not your own opinion. Watch words such as *only*, *always*, *never* and *mainly*; "
              "they change the meaning."),
            MISTAKE("Answering from your own opinion",
                    "A question asks what the passage says or suggests. An option may be true in life but not in the passage. Choose the one "
                    "the text supports."),
            H("Grammar and vocabulary items"),
            T("Put each option into the sentence and read it. The correct one sounds right **and** obeys the rule. Look for "
              "the grammar point being tested: tense, agreement, article, preposition, conjunction. In vocabulary questions, "
              "use context to choose the meaning and not the first word that looks similar."),
            EX("Worked example 1: test each option", intro="\"Neither the teacher nor the students ___ ready.\" A. is B. was C. were D. has been",
               steps=[
                S("Find the rule", text="With neither...nor, the verb agrees with the nearer subject: \"students\" (plural)."),
                S("Test the options", text="A \"is\" and B \"was\" are singular. D \"has been\" is singular."),
                S("Answer", text="C \"were\"."),
            ]),
            H("Phonology items"),
            T("Say the words quietly to yourself (without making noise in the hall). For stress, find the syllable you say "
              "loudest and longest. For sounds, compare the **sound**, not the spelling: *through* and *threw* look different but "
              "sound the same. When a question gives the stress in capitals, read each word with that stress."),
            EX("Worked example 2: a sound question", intro="Which word has the same vowel sound as \"boot\"? A. foot B. fruit C. blood D. both",
               steps=[
                S("Say each word", text="boot /buːt/, foot /fʊt/, fruit /fruːt/, blood /blʌd/, both /bəʊθ/."),
                S("Match", text="Only \"fruit\" has the long /uː/ sound."),
                S("Answer", text="B."),
            ]),
            H("Listening items"),
            T("In a listening test, the passage is read aloud and you answer questions. Before the reading, look at the "
              "questions. While you listen, note **key words**: names, numbers, times, places, reasons. Do not try to write "
              "everything. If you miss an item, move on; do not lose the next one thinking about the last."),
            QUIZ("A passage question asks what the writer says about farming in the first paragraph. Where do you look?",
                 ["In the last paragraph only", "In the first paragraph", "In your own memory", "In the question numbers"], 1,
                 "Look at the part of the passage that the question names.",
                 hint="The question tells you which paragraph.",
                 feedback=["The question names the first paragraph.", "", "The answer must come from the passage.",
                           "Question numbers do not hold the answer."]),
            QUIZ("You have 30 minutes left and 12 unanswered questions. What is the best plan?",
                 ["Leave them blank", "Answer them all quickly by elimination, using about two minutes each", "Spend the whole 30 minutes on one", "Change all your earlier answers"],
                 1, "Use the time to answer each remaining question using elimination. A blank scores nothing.",
                 hint="Is there time for all 12?",
                 feedback=["A blank cannot score.", "", "That leaves the other 11 unanswered.",
                           "Changing sure answers can lose marks."]),
            MISTAKE("Marking the wrong row on the answer sheet",
                    "If you skip a question, make sure you skip the same line on the sheet. A shift of one row makes every later "
                    "answer wrong. Check the number every five questions."),
            PQ("How many minutes per question does Paper 1 give on average? Show the working.",
               "90 minutes divided by 50 questions equals 1.8 minutes (about 1 minute 48 seconds) for each question."),
            PQ("A sentence says: \"The audience was moved to tears.\" Option C says \"The audience did not care.\" Why can you eliminate C?",
               "\"Moved to tears\" means very touched, which is the opposite of \"did not care\", so option C contradicts the sentence."),
            PQ("Give three things to listen for when you take notes in a listening item.",
               "Names, numbers (dates, prices), times and places, and reasons. (Any three key facts.)"),
            SUM("Paper 1 has 50 multiple-choice questions (listening, reading, grammar and vocabulary) in 1 hour 30 minutes, "
                "marked electronically.",
                "That is about 1.8 minutes per question; use a two-pass method.",
                "Eliminate options that are wrong for a clear reason; never leave a blank.",
                "For passages, read questions first and answer from the text, not from your opinion.",
                "For grammar, test each option in the sentence; for sound and stress, say the words quietly."),
        ],
    ),
    # ------------------------------------------------------------------ 10. Paper 2 Section A
    lesson(
        module=M_EXAM, topic="Paper 2",
        title="Paper 2, Section A: Directed Writing step by step",
        slug="eex-paper-2-directed-writing",
        minutes=26,
        summary="A seven-step method for Directed Writing: read the task, find role and format, select ALL relevant points, plan "
                "and cross out, write in your own words with real connectives, respect the limits, and check. With a model answer.",
        objectives=[
            "Apply a seven-step method to a directed writing task",
            "Select all relevant points from a stimulus and use nothing else",
            "Use correct transitional words and avoid made-up connectives",
            "Avoid the errors that the Board reports: lifting, identity, uncancelled plans, wrong paragraphing",
        ],
        key_concepts=["Directed writing", "Stimulus", "Role", "Lifting", "Slanting", "Transitional words", "Paragraph limit"],
        blocks=[
            H("Introduction"),
            T("Paper 2 has two sections. **Section A** is Directed Writing. **Section B** is Composition. This lesson is about "
              "Section A, which is often the more predictable section: the facts are given, so your job is to read well, "
              "choose well and write well.\n\n"
              "The Board reports that candidates lose marks for these reasons: not understanding the task; not knowing the format "
              "of the text; ignoring word and paragraph limits; missing relevant points; lifting from the stimulus; poor expression; "
              "adding their own knowledge; wrong or missing connectives; an uncancelled plan; and disclosing their identity."),
            D("**Directed writing** (Paper 2, Section A) gives you a stimulus and a task. You write a text of a stated "
              "type (talk, speech, article, letter, report, minutes) for a stated audience in a stated role, **using only "
              "the stimulus**, and respecting the word and paragraph limits.", title="Section A"),
            KEY("Seven steps", "Follow them in order every time.", cards=[
                ["1. Read twice", "Read the task, then the stimulus, then the task again."],
                ["2. Role and format", "Who am I? To whom? What type of text? What tone?"],
                ["3. Select ALL points", "Underline every relevant point in the stimulus."],
                ["4. Plan", "Group points into paragraphs; then cross out the plan."],
                ["5. Write", "Own words, continuous prose, real connectives."],
                ["6. Limits", "Obey the word and paragraph limits."],
                ["7. Check", "Grammar, spelling, points covered, no identity, ink colour."],
            ]),
            TIP("Write the final answer in black or blue ink. Do not use pencil for your answer. If you make a plan, cross it "
                "out neatly after writing. Do not cross out your whole answer without writing another one.", title="Exam link"),
            H("A task to work on"),
            CODE("""STIMULUS (invented for practice)
A secondary school wants to improve how students use the library.
Notes: the library opens only from 2 p.m. to 4 p.m.; there are 30 seats for 600
students; many reference books are old; students talk loudly; books are returned
late or lost; a library club could help with order; students may donate one
book each at the end of the year; the head teacher will extend opening hours
if students behave well.

TASK
You are the school prefect. Write a talk to students persuading them to use the
library well. Use the information above. Write one paragraph of 110 to 130 words.""", "text", title="Task"),
            H("Steps 1-3: read, role, select"),
            T("The role is the **prefect**: a student speaking to students, so use \"we\" and \"our library\". The format is a **talk**: "
              "greeting and theme at the start, thanks at the end. The purpose is to **persuade**. The limit is **one paragraph** "
              "of 110-130 words."),
            CODE("""Relevant points selected:
1. opening hours 2-4 p.m. only
2. 30 seats for 600 students
3. old reference books
4. loud talking
5. books returned late or lost
6. library club to help with order
7. each student may donate one book at year end
8. head teacher will extend hours if behaviour good""", "text", title="All eight points"),
            H("Steps 4-7: plan, write, check"),
            CODE("""Fellow students, today I wish to talk to you about how we can improve our library.
At present, it opens for only two hours a day, from 2 to 4 p.m., and it has just thirty
seats for six hundred of us. Many of its reference books are old, and some are
lost or returned late. In addition, loud talking disturbs those who are reading.
However, we can change this. Firstly, we can form a library club to keep order.
Secondly, each of us can give one book at the end of the year. Moreover, the head
teacher has promised longer opening hours if we behave well. If we cooperate, we
shall all benefit. Thank you for listening.""", "text", title="Model answer (one paragraph)"),
            T("Check the model against the steps. Greeting and theme: yes. Role: a student speaking to students (\"we\", \"our\"). All "
              "eight points are covered. Nothing from outside. One paragraph. Connectives are real: in addition, however, firstly, "
              "secondly, moreover. Closing: \"Thank you for listening\". No name, school or place is given."),
            MISTAKE("Using connectives that do not exist or are repeated",
                    "Use firstly, secondly, also, however, nevertheless, moreover, furthermore and in addition. Do not use "
                    "\"nextly\", \"better still\", \"more still\", \"more again\" or \"further still\". Write \"more so\" (two words), "
                    "not \"moreso\". Do not repeat the same connective for the same idea in one sentence."),
            MISTAKE("Lifting",
                    "\"Many reference books are old\" copied word for word is lifting. Change the words and shape: \"much of our "
                    "reading material is out of date\". Lifting earns little credit because it shows no understanding."),
            MISTAKE("Listing points or splitting the answer",
                    "If the task says one paragraph, do not write a numbered list, subtitles or several paragraphs. Do not leave "
                    "blank lines inside the paragraph."),
            H("Other formats in Section A"),
            T("The task may ask for a letter, report, article or minutes. Use the format taught in the writing lessons. A talk "
              "or speech needs a greeting or theme and a closing. A letter needs the given names and addresses. In every "
              "case, **do not disclose your own identity**."),
            QUIZ("A candidate adds an extra tip about cleaning the library from his own experience. What is the problem?",
                 ["It is too short.", "It is not in the stimulus, so it earns no credit and may waste words.", "It uses too many connectives.", "It is in the wrong ink."],
                 1, "Directed writing must use the stimulus only.",
                 hint="Where must all the points come from?",
                 feedback=["Length is not the issue.", "", "The problem is not connectives.", "Ink has nothing to do with this."]),
            QUIZ("Which is the correct connective for adding an idea?", ["Nextly", "More again", "In addition", "Better still"], 2,
                 "\"In addition\" is an accepted connective for adding; the others are not.",
                 hint="Which one is a standard English linking phrase?",
                 feedback=["\"Nextly\" is not accepted.", "\"More again\" is not accepted.", "", "\"Better still\" is not accepted as a connective."]),
            EX("Worked example 1: improve an answer", intro="A candidate writes: \"The library is open for only two hours. Also, the "
               "library is small. Also, books are lost.\" Improve it.", steps=[
                S("Join sentences", text="Avoid repeating the same word and short sentences."),
                S("Use varied connectives", text="\"The library opens for only two hours; moreover, it is small. In addition, some books are lost.\""),
                S("Check", text="No lifting, one idea per clause, and real connectives."),
            ]),
            EX("Worked example 2: choose the role", intro="The task says: \"You are the Head of the Sports Club. Write a talk to club members.\" "
               "Which opening is best?", steps=[
                S("Find the role", text="Head of the Sports Club speaks to club members."),
                S("Check the format", text="A talk needs a greeting and a theme."),
                S("Write", text="\"Fellow club members, today I wish to speak about how we can improve our training.\""),
            ]),
            PQ("List four things you must underline or note when you first read a directed writing task.",
               "Role, audience, format of the text, and the limits (words and paragraphs). Also the purpose and tone."),
            PQ("Rewrite in your own words: \"Students talk loudly in the library.\"",
               "Example: \"Some of us make too much noise where others are trying to read.\""),
            PQ("A task asks for 120 words in one paragraph. Your answer has three paragraphs and 90 words. Name two faults.",
               "It does not obey the paragraph limit (three instead of one) and it is too short for the word limit, so it probably "
               "misses some points."),
            SUM("Directed writing uses only the stimulus. Select ALL relevant points and write in your own words.",
                "Identify role, audience, format and limits before you plan.",
                "Plan, then cross out the plan; write in black or blue ink; do not disclose identity.",
                "Use real connectives (firstly, however, moreover, in addition, nevertheless) and avoid made-up ones.",
                "Obey word and paragraph limits and write in continuous prose, without lists or subtitles."),
        ],
    ),
    # ------------------------------------------------------------------ 11. Paper 2 Section B
    lesson(
        module=M_EXAM, topic="Paper 2",
        title="Paper 2, Section B: Composition step by step",
        slug="eex-paper-2-composition",
        minutes=24,
        summary="How to choose one composition topic, read its scope, plan in the order of the task, write in continuous paragraphs "
                "with consistent tenses and good English, and avoid the errors the Board reports.",
        objectives=[
            "Choose one topic and decide the type of essay it needs",
            "Read the scope of the topic and plan to cover every part of it",
            "Write in continuous paragraphs with consistent tense and correct English",
            "Avoid errors the Board reports: several topics, copying, segmenting by rubric, one-paragraph essays",
        ],
        key_concepts=["Composition", "Choice of topic", "Scope of the topic", "Plan", "Paragraph unity", "Continuous prose"],
        blocks=[
            H("Introduction"),
            T("In Section B of Paper 2, you are given several composition topics and you write on **one**. Look at the "
              "choices: a story ending with a fixed sentence, a description, a letter, a title of one word, a question about "
              "your area, a motion to argue. The choice is yours, and the quality of your choice affects your result.\n\n"
              "Candidates are often good at content but weaker at expression and accuracy: tenses change, words come "
              "from Pidgin or French, and paragraphs are missing."),
            D("**Composition** (Paper 2, Section B) is an essay on one topic of your choice from those set. It is "
              "written in continuous prose, in paragraphs, in correct English, within the length required.",
              title="Section B"),
            TIP("Write on only **one** topic. Do not write two answers and forget to cancel one. Do not copy the instructions again "
                "and again. Do not copy parts of the Directed Writing text. Write in black or blue ink, plan and cross out the plan, "
                "and never reveal your name, school or other identity.", title="Exam link"),
            H("Step 1: choose the right topic"),
            T("Spend about three minutes on choosing. Pick the topic for which you have **ideas, vocabulary and structure**, "
              "not the one with the most exciting title. Ask: Do I know how to write this type of essay (story, "
              "description, letter, argument)? Can I write at least four paragraphs on it?"),
            CODE("""Type of task            | Key signal in the topic
Narrative               | "Tell a story..." / a given last sentence
Descriptive             | "Describe..."
Informal / formal letter| names and addresses are given; "Write a letter to..."
Expository              | "How has...?" / "Explain..." / "What are the effects?"
Argumentative           | "Do you agree?" / "Discuss" / a motion
Single-word title       | you decide the type; define the scope""", "text", title="Read the signal words"),
            H("Step 2: read the scope"),
            T("The **scope** is exactly what the topic asks. Underline every part. If the topic says, \"How has electricity "
              "affected life in your area?\", the scope has three parts: electricity, effects on life, **your area** (before "
              "and after). If it says \"Describe a famous place...\", it means **one** place described, not a story. If it is a single "
              "word, for example \"Courage\", decide how you will limit it: a story about courage, or an explanation of what courage is."),
            MISTAKE("Missing the scope",
                    "A story about bad behaviour that ignores the advice mentioned in the title, or an essay on the advantages of "
                    "electricity that never says how a place changed, is off the scope. Check every paragraph against the topic."),
            H("Step 3: plan and cross out"),
            T("Spend about five minutes on a short plan: four to six paragraph lines in words. Number them. Then write. At the "
              "end, cross out the plan with a single neat line. Do not cross out your essay."),
            CODE("""Topic: Electricity has just been installed in your locality. How has it affected life?
1. Intro: village before (lamps, early sleep); electricity arrives
2. Business: shops, cold drinks, welding, phone charging
3. School: evening study, lights in classrooms
4. Home: cooking, TV, safety
5. Problems: bills, cuts, accidents
6. Conclusion: overall change and a hope""", "text", title="A paragraph plan"),
            H("Step 4: write in paragraphs and good English"),
            T("**One idea per paragraph.** The first sentence says the idea (topic sentence). Do not write the whole essay in "
              "one paragraph, and do not put a single sentence in each paragraph. Do not use headings such as \"Introduction\" "
              "or write one paragraph for \"content\", another for \"expression\". Do not list points: use full sentences.\n\n"
              "Keep one **tense** unless the meaning requires a change. Think in English: do not translate from French, Pidgin or a home language."),
            MISTAKE("Thinking in another language",
                    "\"He has done three years in the village\" (from French) is wrong; say \"He has spent three years in the village\". "
                    "Pidgin structures such as \"The boy wey I see\" are not accepted in Standard English. Use short, correct sentences "
                    "that you are sure of."),
            MISTAKE("Pre-prepared and out-of-topic essays",
                    "Learning an essay by heart and forcing it into any topic is easy for the examiner to see and brings poor marks. "
                    "Learn structures and vocabulary, not whole essays."),
            H("Step 5: check"),
            T("In the last minutes, read your work. Fix tenses, spelling, punctuation and missing words. Make sure you gave "
              "the required ending or format. Make sure that no part carries your name or any clue of identity."),
            QUIZ("A candidate writes two compositions on different topics and cancels neither. What is the likely result?",
                 ["Extra marks for effort", "A penalty, because only one topic is wanted and the choice is unclear", "No effect", "Full marks for both"], 1,
                 "Candidates write on one topic. Writing on two without cancelling one wastes time and causes problems.",
                 hint="How many topics are you asked to write on?",
                 feedback=["Effort is not marked in this way.", "", "It does matter.", "Only one answer is wanted."]),
            QUIZ("A topic says: \"The use of mobile phones in schools should be allowed. Do you agree?\" What type of essay is it?",
                 ["A narrative", "A description", "An argumentative essay", "A report"], 2,
                 "\"Do you agree?\" signals an argument with a position.",
                 hint="Which signal words are in the topic?",
                 feedback=["It does not ask for a story.", "It does not ask to describe a place or person.", "", "A report has a different format."]),
            EX("Worked example 1: read the scope", intro="Topic: \"Describe a market you know well.\" Which essay stays within the scope: (a) "
               "a journey to the market and an argument with a trader, (b) the sights, sounds and smells of the market, "
               "(c) a comparison of five markets?", steps=[
                S("Find the key word", text="\"Describe\" and \"a market\" (one)."),
                S("Test each", text="(a) is narration; (c) is many markets."),
                S("Answer", text="(b) describes one market with the senses."),
            ]),
            EX("Worked example 2: choose between two topics", intro="You can choose a story with a fixed ending, or an argument on a motion. You "
               "have strong examples for the motion but no idea for the story. Which do you choose?", steps=[
                S("Think about ideas", text="You have strong examples for the argument."),
                S("Think about structure", text="You know the argument order: intro, opposing view, refutation, arguments, conclusion."),
                S("Decide", text="Choose the argument, and plan it carefully."),
            ]),
            PQ("Write a one-line plan for each of four paragraphs of a story for the topic \"A Day I Will Never Forget\".",
               "1. A normal morning in the village. 2. A sudden problem (a flood). 3. How people helped each other. "
               "4. The ending and what I learned. (Any logical four-part plan.)"),
            PQ("Why should you not write headings like \"Content\" and \"Accuracy\" in your essay?",
               "They are marking terms, not parts of an essay. A composition must be written in continuous prose, with "
               "paragraphs for ideas, not for marking categories."),
            PQ("Name three things to do in the last minutes of the paper.",
               "Cross out the plan neatly, read through to correct tenses, spelling and punctuation, and check that nothing reveals your identity."),
            SUM("In Section B, choose and write on only one topic.",
                "Read the scope: every part of the topic must be answered.",
                "Plan in words, then cross out the plan; write in continuous paragraphs with one idea each.",
                "Keep tenses consistent; think in English, not in Pidgin, French or a home language.",
                "Do not copy the instructions, the Directed Writing text or a memorised essay; never reveal your identity."),
        ],
    ),
]
