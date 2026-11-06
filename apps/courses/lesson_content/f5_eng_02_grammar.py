"""Form 5 English Language (O Level 0530), module "Grammar & Structural Accuracy".
Draft content: check against the official syllabus and your textbook."""

from .dsl import *  # noqa: F403

COURSE = ("english-language", "form-5")

MODULE = "Grammar & Structural Accuracy"

LESSONS = []

# ---------------------------------------------------------------------- 1. Nouns, pronouns, determiners
LESSONS += [
    lesson(
        module=MODULE,
        topic="Nouns, pronouns and determiners",
        title="Nouns, pronouns and determiners",
        slug="egr-nouns-pronouns-determiners",
        minutes=22,
        summary="Nouns name things and can be countable or uncountable. Pronouns replace nouns, and determiners such as a, the, much and few introduce them. Many common errors come from treating uncountable nouns as countable.",
        objectives=[
            "Identify common, proper, abstract and collective nouns, and countable and uncountable nouns",
            "Form plurals correctly and avoid errors such as 'a news' and 'many informations'",
            "Choose the correct pronoun (subject, object, possessive, reflexive)",
            "Use articles and quantifiers (a, an, the, much, many, few, little, fewer, less) correctly",
        ],
        key_concepts=["Common noun", "Proper noun", "Abstract noun", "Uncountable noun", "Pronoun", "Determiner", "Article", "Quantifier"],
        blocks=[
            H("Introduction"),
            T("A trader at Mokolo Market says, \"I have good news. I sold all my tomatoes, and I got some advice from the woman at the next stall.\" "
              "Every word that names something (trader, market, tomatoes, news, advice) is a noun. Words such as *I* and *she* stand in for nouns. "
              "Words such as *some*, *the* and *all* tell us which or how many."),
            T("These three word classes appear in almost every sentence. Small mistakes with them, such as *a news* or *many informations*, "
              "are among the most common errors in writing. In this lesson you will learn the rules that prevent them."),
            H("Nouns"),
            D("A **noun** is a word that names a person, place, thing, idea or group. A **pronoun** is a word used in place of a noun. "
              "A **determiner** is a word placed before a noun to show which one or how many.",
              title="Definitions"),
            KEY("Four kinds of noun", "Learn to recognise these types.", cards=[
                ["Common noun", "Names any person, place or thing: girl, market, taxi, farm."],
                ["Proper noun", "Names one particular person or place and begins with a capital letter: Ama, Limbe, Mount Cameroon."],
                ["Abstract noun", "Names an idea or feeling you cannot touch: honesty, hunger, freedom, friendship."],
                ["Collective noun", "Names a group as one unit: team, class, flock, committee."],
            ]),
            D("A **countable noun** can be counted and has a plural form: one mango, two mangoes. "
              "An **uncountable noun** is treated as a mass and has no plural form: rice, water, advice, news.",
              title="Countable and uncountable nouns"),
            T("Uncountable nouns take a singular verb, and we cannot put *a*, *an* or a number directly before them. "
              "To count them, we use an expression such as *a piece of*. The table shows the most important ones."),
            CODE("""Uncountable noun   How to count it
information        a piece of information
advice             a piece of advice
news               a piece of news
furniture          a piece of furniture
luggage            a piece of luggage, a bag
equipment          an item of equipment
homework           an assignment
evidence           a piece of evidence""", "text", title="Uncountable nouns (no plural form)"),
            MISTAKE("Common error: 'a news', 'an advice', 'many informations'",
                    "Because *news*, *advice* and *information* are uncountable, there is no *a* and no plural *-s*. "
                    "Write *some news*, *a piece of advice*, *a lot of information*. "
                    "The same applies to *furniture*, *luggage*, *equipment* and *homework*: not *furnitures* or *luggages*. "
                    "Many languages count these words, which is why the error is so common."),
            MISTAKE("Common error: 'peoples' and 'childrens'",
                    "*People* is already a plural: *The people are waiting.* *Children* is the plural of *child*, so *childrens* is wrong. "
                    "For possession, write *children's books* (apostrophe before the s because *children* is already plural). "
                    "Other irregular plurals to know: man, men; woman, women; tooth, teeth; leaf, leaves; knife, knives. "
                    "*Sheep* and *fish* do not change."),
            H("Pronouns"),
            T("A pronoun changes its form according to its job in the sentence. Use a **subject pronoun** before the verb and an **object pronoun** after a verb or a preposition."),
            CODE("""Subject   Object   Possessive   Reflexive
I         me       mine         myself
you       you      yours        yourself
he        him      his          himself
she       her      hers         herself
it        it       -            itself
we        us       ours         ourselves
they      them     theirs       themselves""", "text", title="Personal pronouns"),
            EX("Worked example 1: choosing the correct pronoun", intro="Correct the pronoun mistakes: (a) Me and Ngu went to the farm. (b) The money was shared between Ama and I.", steps=[
                S("Sentence (a)", text="'Me' cannot be the subject of 'went'. Use the subject pronoun I. It is polite to name the other person first."),
                S("Corrected (a)", text="Ngu and I went to the farm."),
                S("Sentence (b)", text="'Between' is a preposition, so the pronoun after it must be in the object form: me."),
                S("Corrected (b)", text="The money was shared between Ama and me."),
            ]),
            H("Determiners"),
            T("**Articles** are the commonest determiners. Use **a** before a consonant *sound* and **an** before a vowel *sound*. "
              "The rule depends on the sound, not the spelling."),
            EX("Worked example 2: a or an?", intro="Choose a or an: (1) ___ hour (2) ___ university (3) ___ uniform (4) ___ honest trader (5) ___ umbrella.", steps=[
                S("Listen to the first sound", text="Say each word aloud and ask whether it begins with a vowel sound."),
                S("Apply the rule", text="hour starts with a vowel sound (the h is silent): an hour. university starts with the sound 'yoo', a consonant sound: a university. uniform also starts with 'yoo': a uniform. honest has a silent h: an honest trader. umbrella starts with a vowel sound: an umbrella."),
                S("Answer", text="(1) an (2) a (3) a (4) an (5) an"),
            ]),
            T("Use **the** when both speaker and listener know which one is meant (*Pass me the book on the table.*). "
              "Do not use *the* when you speak about things in general: write *Life is hard*, not *The life is hard*; "
              "write *Cameroonians love football*, not *The Cameroonians love football* (unless you mean a particular group)."),
            KEY("Quantifiers: how many, how much?", "Check whether the noun is countable or uncountable.", cards=[
                ["Countable nouns", "many, few, a few, fewer, several, a number of: many mangoes, few chairs, fewer students."],
                ["Uncountable nouns", "much, little, a little, less, a great deal of: much rice, little water, less money."],
                ["Both kinds", "some, any, a lot of, plenty of, enough, all, no."],
            ]),
            T("*Few* and *little* mean 'hardly any' (a negative idea): *Few people came.* *A few* and *a little* mean 'some' (a positive idea): *A few people came.*"),
            EX("Worked example 3: quantifiers", intro="Choose the correct word: (1) There are (many / much) tomatoes on the stall. (2) We have (few / little) rice left, so we must buy more. (3) There were (fewer / less) pupils in class today.", steps=[
                S("Countable or uncountable?", text="Tomatoes is countable. Rice is uncountable. Pupils is countable."),
                S("Choose", text="(1) many, because tomatoes can be counted. (2) little, because rice is uncountable. (3) fewer, because pupils can be counted."),
                S("Answer", text="(1) many (2) little (3) fewer"),
            ]),
            MISTAKE("Common error: 'much' and 'less' with countable nouns",
                    "*Much people* and *less students* are common errors. Use *many people* and *fewer students*. "
                    "Use *much* and *less* only with uncountable nouns: *much money*, *less water*."),
            TIP("Exam link: noun, pronoun and determiner choices appear in the grammar questions of Paper 1 (multiple choice), "
                "and the accuracy of your writing in Paper 2 depends on them too. When in doubt about *a* or *an*, say the word aloud.",
                title="Where this appears in the exam"),
            QUIZ("Which sentence is correct?",
                 ["The news are very good today.", "We received an advice from the headmaster.",
                  "She gave me some useful information.", "They bought many furnitures for the new house."], 2,
                 "News, advice, information and furniture are uncountable. Only the third sentence treats an uncountable noun correctly.",
                 hint="Look for an uncountable noun with no plural -s and no a/an.",
                 feedback=["News is singular: 'The news is very good today.'", "Advice is uncountable: 'some advice' or 'a piece of advice'.", "",
                           "Furniture is uncountable: 'a lot of furniture'."]),
            QUIZ("Choose the correct completion: 'There is ___ water in the bucket, so we must fetch more.'",
                 ["few", "little", "fewer", "many"], 1,
                 "Water is uncountable, so we need little (meaning hardly any).",
                 hint="Is water countable?",
                 feedback=["Few is for countable nouns.", "", "Fewer is for countable nouns.", "Many is for countable nouns."]),
            PQ("Rewrite correctly: 'He gave me an advice, and I wrote many informations in my notebook.'",
               "He gave me a piece of advice (or some advice), and I wrote a lot of information in my notebook. Advice and information are uncountable."),
            PQ("Correct the pronoun: 'The teacher called Kum and I to the staffroom.'",
               "The teacher called Kum and me to the staffroom. 'Called' is followed by an object, so the object pronoun me is needed."),
            PQ("Write a or an before each word: ___ European, ___ hour, ___ one-way ticket, ___ egg.",
               "a European (sounds like 'yoo'), an hour (silent h), a one-way ticket (sounds like 'wun'), an egg."),
            SUM("A noun names; a pronoun replaces a noun; a determiner introduces a noun.",
                "Uncountable nouns (news, advice, information, furniture, luggage) have no plural and no a/an.",
                "Use subject pronouns before verbs (Ngu and I) and object pronouns after verbs and prepositions (between you and me).",
                "Use a or an according to the sound, not the spelling: an hour, a university.",
                "Use many, few and fewer with countable nouns; much, little and less with uncountable nouns."),
        ],
    ),
]

# ---------------------------------------------------------------------- 2a. Tenses: simple and continuous
LESSONS += [
    lesson(
        module=MODULE,
        topic="Verb tenses, aspect and mood",
        title="Present and past: simple and continuous forms",
        slug="egr-tenses-simple-and-continuous",
        minutes=22,
        summary="The simple forms describe habits, facts and finished actions; the continuous forms describe actions in progress. Verbs of state such as know, want and believe are not normally used in the continuous form.",
        objectives=[
            "Use the present simple for habits and facts and the present continuous for actions in progress",
            "Use the past simple and past continuous correctly",
            "Explain why verbs such as know, want and understand are not used in the continuous form",
            "Form questions and negatives with do, does and did without errors such as 'he didn't went'",
        ],
        key_concepts=["Tense", "Present simple", "Present continuous", "Past simple", "Past continuous", "Stative verb", "Auxiliary verb"],
        blocks=[
            H("Introduction"),
            T("A taxi driver in Yaoundé says: \"I drive to Mvan every morning. Today I am driving to Mendong because the road is closed.\" "
              "The two sentences use the same verb in two different forms. The first describes a habit. The second describes something happening now. "
              "The form of the verb tells the listener when and how the action happens."),
            T("This lesson covers the four forms you meet most often: the present simple, the present continuous, the past simple and the past continuous."),
            H("The present tenses"),
            D("A **tense** is the form of a verb that shows when an action happens. "
              "An **auxiliary verb** (such as *do*, *does*, *did*, *is*, *are*, *was*, *were*) helps the main verb to form questions, negatives and continuous forms.",
              title="Definitions"),
            KEY("Present simple and present continuous", "Compare their uses.", cards=[
                ["Present simple", "Habits, facts and timetables: Mama Ngo sells fish every day. Water boils at 100 degrees Celsius. Add -s or -es for he, she and it."],
                ["Present continuous", "Actions happening now or around now: The driver is waiting for passengers. Formed with am, is or are + verb-ing."],
            ]),
            T("Time words help. With the present simple we often see *always*, *usually*, *every day*, *never*. "
              "With the present continuous we see *now*, *at the moment*, *these days*, *today*."),
            MISTAKE("Common error: 'She sell' and 'He don't know'",
                    "With *he*, *she*, *it* or a singular noun, the present simple verb takes -s: *She sells*, *He works*. "
                    "In negatives and questions, *does* carries the -s and the main verb stays plain: *He does not know.* *Does she sell fish?* "
                    "Not *He doesn't knows* or *Does she sells?*"),
            H("Verbs that are not used in the continuous"),
            T("Some verbs describe a **state** (a condition) rather than an action. They are called **stative verbs**. "
              "They are normally used in the simple form, even when we mean 'now'."),
            CODE("""Stative verbs (normally not used with -ing)
know       understand   believe     remember
want       need         like        love        hate
prefer     belong       own         seem
see        hear         smell       taste (as perception)""", "text", title="Common stative verbs"),
            MISTAKE("Common error: 'I am knowing' and 'I am understanding'",
                    "Write *I know the answer* and *I understand the question*, not *I am knowing* or *I am understanding*. "
                    "Likewise *I want a bag*, not *I am wanting a bag*. "
                    "Some verbs have both a state meaning and an action meaning: *I have a phone* (possession, simple) but *I am having lunch* (an action, continuous)."),
            H("The past tenses"),
            T("Use the **past simple** for an action that is finished, usually with a time word such as *yesterday*, *last week*, *in 2019*. "
              "Regular verbs add -ed. Irregular verbs change form, and you must learn them."),
            CODE("""Base        Past simple    Base        Past simple
go          went           bring       brought
buy         bought         teach       taught
sell        sold           catch       caught
pay         paid           think       thought
leave       left           write       wrote""", "text", title="Some irregular verbs"),
            T("Use the **past continuous** (was or were + verb-ing) for an action that was in progress at a moment in the past, "
              "often interrupted by a shorter action: *While I was walking to school, it began to rain.* "
              "The longer action is continuous; the shorter, interrupting action is simple."),
            MISTAKE("Common error: 'He didn't went' and 'Did you saw?'",
                    "After *did* or *didn't*, the main verb returns to its plain (base) form, because *did* already shows the past: "
                    "*He didn't go.* *Did you see him?* Not *He didn't went* or *Did you saw him?* "
                    "Also avoid regular endings on irregular verbs: *buyed*, *teached*, *goed* are wrong. Say *bought*, *taught*, *went*."),
            EX("Worked example 1: simple or continuous?", intro="Choose the correct form: (a) Ndi (plays / is playing) football every Saturday. (b) Listen! The baby (cries / is crying). (c) I (am knowing / know) your brother.", steps=[
                S("Sentence (a)", text="'Every Saturday' shows a habit, so the present simple: plays."),
                S("Sentence (b)", text="'Listen!' shows it is happening now, so the present continuous: is crying."),
                S("Sentence (c)", text="Know is a stative verb, so the simple form: know."),
                S("Answer", text="(a) plays (b) is crying (c) know"),
            ]),
            EX("Worked example 2: past simple or past continuous?", intro="Put the verbs in the correct form: 'When the rain (start), the farmers (harvest) the maize.'", steps=[
                S("Find the two actions", text="Starting is a short action. Harvesting was already in progress."),
                S("Choose forms", text="Short action: past simple, started. Longer background action: past continuous, were harvesting."),
                S("Answer", text="When the rain started, the farmers were harvesting the maize."),
            ]),
            EX("Worked example 3: negatives and questions in the past", intro="Make the sentence negative and then a question: 'Ama bought a phone.'", steps=[
                S("Negative", text="Use did not and the plain verb: Ama did not buy a phone."),
                S("Question", text="Put did first and keep the plain verb: Did Ama buy a phone?"),
                S("Check", text="The past form 'bought' appears only in the positive sentence. After did, use 'buy'."),
            ]),
            TIP("Exam link: tense questions appear in the grammar section of Paper 1 (multiple choice). "
                "The Board's report on the written paper notes that many candidates change tense without reason inside one composition, "
                "so choose one tense for a story and keep to it. Reread each verb in your final check.",
                title="Where this appears in the exam"),
            QUIZ("Which sentence is correct?",
                 ["I am wanting a new school bag.", "She don't like fish.", "He didn't went to the market.", "My father is working in Bamenda this month."], 3,
                 "Only the last sentence is correct: a temporary situation uses the present continuous.",
                 hint="Check each verb: is it stative? Is the verb after did in plain form?",
                 feedback=["Want is a stative verb: 'I want a new school bag.'", "With she, use does not: 'She does not like fish.'",
                           "After did not, use the plain verb: 'He didn't go.'", ""]),
            QUIZ("Choose the correct sentence.",
                 ["While I walked home, I was meeting my teacher.", "While I was walking home, I met my teacher.",
                  "While I was walking home, I was meeting my teacher.", "While I walked home, I meet my teacher."], 1,
                 "The longer action (walking) is continuous and the interrupting action (meeting) is simple past.",
                 hint="Which action was already going on, and which one interrupted it?",
                 feedback=["The longer action is the continuous one: 'was walking'. 'Meeting' is a short action in the past simple.", "",
                           "A short event is not normally continuous here: 'I met my teacher'.", "Meet must be in the past: 'met'."]),
            PQ("Correct the errors: 'My sister is knowing the answer, but she don't want to tell us.'",
               "My sister knows the answer, but she does not want to tell us. 'Know' is stative, so no -ing; with 'she', the negative uses 'does not'."),
            PQ("Rewrite in the past simple: 'Mama Ngo sells fish and pays the transport fare.'",
               "Mama Ngo sold fish and paid the transport fare. Sell and pay are irregular: sold, paid."),
            PQ("Complete the sentence: 'When we arrived at the church, the choir (sing) a hymn.'",
               "When we arrived at the church, the choir was singing a hymn. The singing was already in progress, so the past continuous is used."),
            SUM("Present simple: habits and facts (she sells). Present continuous: actions in progress now (she is selling).",
                "Stative verbs (know, want, understand, believe) are not normally used with -ing: say I know, not I am knowing.",
                "Past simple: finished actions (went, bought). Past continuous: an action in progress when another happened.",
                "After do, does and did, the main verb is in its plain form: He didn't go. Does she sell?",
                "Choose one tense for a story and keep to it."),
        ],
    ),
]

# ---------------------------------------------------------------------- 2b. Tenses: perfect, future, mood
LESSONS += [
    lesson(
        module=MODULE,
        topic="Verb tenses, aspect and mood",
        title="Perfect forms, future time and mood",
        slug="egr-tenses-perfect-future-mood",
        minutes=24,
        summary="The present perfect links the past to now, the past perfect shows an earlier past, and the future uses will, going to and other forms. Mood shows whether a sentence states, commands or imagines.",
        objectives=[
            "Use the present perfect with for and since and the past perfect for an earlier past",
            "Express future time with will, going to, the present continuous and the present simple",
            "Distinguish tense from aspect and name the three moods: indicative, imperative and subjunctive",
            "Keep tenses consistent in a piece of writing",
        ],
        key_concepts=["Present perfect", "Past perfect", "Aspect", "Future time", "Mood", "Indicative", "Imperative", "Subjunctive", "Tense consistency"],
        blocks=[
            H("Introduction"),
            T("A student at the bus station in Bamenda says: \"I have waited for two hours.\" "
              "She is still waiting, and the sentence connects the past to now. If she says, \"I waited for two hours yesterday,\" the waiting is finished. "
              "The small change from *waited* to *have waited* changes the meaning."),
            T("In this lesson you will meet the perfect forms, learn how to talk about the future, and see what grammarians mean by **aspect** and **mood**."),
            H("Tense, aspect and mood"),
            D("**Tense** shows the time of an action (present or past). **Aspect** shows how the action is viewed: "
              "as finished or connected to now (perfect), or as in progress (continuous). **Mood** shows the speaker's attitude: "
              "stating a fact, giving a command, or imagining something unreal.",
              title="Definitions",
              note="Textbooks differ on how many tenses English has. Many say two by form (present and past), with the future shown by will and other forms. Check your textbook."),
            H("The present perfect"),
            T("Form: **have or has + past participle** (lived, gone, written, eaten). Use it for an action that began in the past and continues to now, "
              "or for a past action whose result matters now. Do not use it with a finished time such as *yesterday*, *last year* or *in 2020*."),
            KEY("For and since", "Both are used with the present perfect.", cards=[
                ["for + a length of time", "for six years, for two hours, for a long time: I have lived in Limbe for six years."],
                ["since + a starting point", "since 2019, since Monday, since I was a child: She has taught here since 2018."],
            ]),
            MISTAKE("Common error: 'I am living here since 2019'",
                    "For an action that began in the past and continues now, English uses the present perfect, not the present continuous: "
                    "*I have lived here since 2019.* Also avoid the present perfect with a finished time: "
                    "*I saw him yesterday*, not *I have seen him yesterday*."),
            T("The **present perfect continuous** (have been + verb-ing) stresses the activity and its duration: *I have been waiting for two hours.*"),
            H("The past perfect"),
            T("Form: **had + past participle**. Use it for an action that happened before another past action or time: "
              "*When we reached the station, the bus had left.* The leaving came first, so it takes the past perfect. The arriving is in the past simple."),
            EX("Worked example 1: perfect or simple?", intro="Choose the correct form: (a) Ngu (has lived / lived) in Douala since 2015. (b) We (have visited / visited) Mount Cameroon last December. (c) When I arrived, the match (already started / had already started).", steps=[
                S("Sentence (a)", text="'Since 2015' links the past to now: has lived."),
                S("Sentence (b)", text="'Last December' is a finished time, so the past simple: visited."),
                S("Sentence (c)", text="The match started before I arrived, so the past perfect: had already started."),
                S("Answer", text="(a) has lived (b) visited (c) had already started"),
            ]),
            H("Talking about the future"),
            T("English has no single future tense. We use several forms."),
            CODE("""will + base verb         decisions, promises, predictions
                         I will call you tonight.
am/is/are going to       plans and clear evidence
                         It is going to rain. Look at the clouds.
present continuous       fixed arrangements
                         I am meeting my uncle at 4 pm tomorrow.
present simple           timetables
                         The bus leaves at 6 a.m.""", "text", title="Ways to refer to the future"),
            MISTAKE("Common error: 'when he will arrive' and 'if it will rain'",
                    "After *if*, *when*, *before*, *after*, *as soon as* and *until*, we use the **present simple** to refer to the future, not *will*: "
                    "*When he arrives, I will call you.* *If it rains, we will stay at home.* Use *will* only in the main clause."),
            H("Mood"),
            KEY("Three moods", "Mood shows the purpose of the verb form.", cards=[
                ["Indicative", "Statements and questions about facts: The market opens at six. Does the market open at six?"],
                ["Imperative", "Commands, requests and instructions; the verb is in its plain form: Close the door. Please be quiet."],
                ["Subjunctive", "Wishes and unreal situations: If I were you, I would apologise. I wish I had a bicycle."],
            ]),
            T("In the **subjunctive** for unreal situations, use *were* for all persons: *If I were rich...*, *If she were here...* "
              "(In everyday speech, *was* is heard, but *were* is the standard written form.)"),
            H("Keeping tenses consistent"),
            T("Choose the time frame of your writing and keep to it. A story told in the past should stay in the past tense, except for general truths or direct speech. "
              "Shifting without reason confuses the reader. The Board's report notes that this is a frequent weakness."),
            EX("Worked example 2: correcting a shift in tense", intro="Correct the passage: 'Last Sunday we went to the farm. We plant cassava, and then my uncle tells us a story. After that we eat and returned home.'", steps=[
                S("Find the time frame", text="'Last Sunday' tells us the story is in the past."),
                S("Correct each verb", text="plant becomes planted, tells becomes told, eat becomes ate."),
                S("Answer", text="Last Sunday we went to the farm. We planted cassava, and then my uncle told us a story. After that we ate and returned home."),
            ]),
            TIP("Exam link: tense and mood questions appear in the grammar section of Paper 1 (multiple choice). In Paper 2, "
                "marks for accuracy are lost when tenses shift without reason. Underline the time word in a multiple-choice question first: "
                "yesterday, since, already, tomorrow.",
                title="Where this appears in the exam"),
            QUIZ("Choose the correct sentence.",
                 ["I am waiting here since eight o'clock.", "I have waited here since eight o'clock.",
                  "I waited here since eight o'clock.", "I wait here since eight o'clock."], 1,
                 "Since eight o'clock links the past to now, so the present perfect is used (a continuous form, 'have been waiting', would also be acceptable).",
                 hint="Which tense joins a past starting point to the present?",
                 feedback=["The present continuous cannot be used with since.", "", "The past simple suggests the waiting is finished.", "The present simple cannot be used with since."]),
            QUIZ("Choose the correct sentence.",
                 ["If I will see her, I will tell her.", "If I see her, I will tell her.", "If I would see her, I would tell her.", "If I saw her, I will tell her."], 1,
                 "After if, we use the present simple to refer to the future: 'If I see her, I will tell her.'",
                 hint="Which verb form follows if when we talk about a likely future event?",
                 feedback=["Do not use will after if.", "", "This mixes 'if + would' which is not standard.", "A past form after if with 'will' in the main clause is a mismatch."]),
            PQ("Correct the error: 'I am staying in this town since last year.'",
               "I have stayed (or have been staying) in this town since last year. Since links a past start to the present."),
            PQ("Join the actions in the right order using the past perfect: 'The teacher entered. The pupils finished the test.' (Pupils finished first.)",
               "By the time the teacher entered, the pupils had finished the test. The earlier action takes the past perfect."),
            PQ("Complete: 'As soon as the results (be) out, I (call) you.'",
               "As soon as the results are out, I will call you. After 'as soon as', use the present simple for future time."),
            SUM("The present perfect (have/has + past participle) links the past to now: use for and since, not a finished time.",
                "The past perfect (had + past participle) shows the earlier of two past actions.",
                "The future can be shown by will, going to, the present continuous and the present simple.",
                "After if, when, before, after and as soon as, use the present simple for future meaning.",
                "Moods: indicative (facts), imperative (commands), subjunctive (unreal: If I were you).",
                "Keep tenses consistent within a piece of writing."),
        ],
    ),
]

# ---------------------------------------------------------------------- 3a. Concord: basic rules
LESSONS += [
    lesson(
        module=MODULE,
        topic="Subject-verb concord",
        title="Subject-verb agreement: the basic rules",
        slug="egr-concord-basic-rules",
        minutes=20,
        summary="A verb must agree in number with its subject. Find the real subject, ignore the words between subject and verb, and treat each, every, everyone and nobody as singular.",
        objectives=[
            "Find the true subject of a sentence and make the verb agree with it",
            "Ignore interrupting phrases such as 'of the pupils' and 'together with'",
            "Apply the rules for subjects joined by and, or, either...or and neither...nor",
            "Use there is and there are correctly",
        ],
        key_concepts=["Concord", "Subject", "Singular", "Plural", "Compound subject", "Indefinite pronoun"],
        blocks=[
            H("Introduction"),
            T("At a bus park in Bafoussam a loudspeaker says, \"The bus to Douala leaves at nine.\" "
              "If it said, \"The buses to Douala leaves at nine,\" listeners would notice something wrong. "
              "The verb must match the subject. This matching is called **concord** (or agreement)."),
            T("In this lesson you will learn the basic rules. They look simple, but exam questions often hide the subject in a long sentence."),
            H("The basic rule"),
            D("**Concord** is the agreement between a subject and its verb in number (singular or plural) and in person. "
              "A singular subject takes a singular verb; a plural subject takes a plural verb.",
              title="Definition"),
            T("In the present simple, the verb for *he*, *she*, *it* and singular nouns ends in -s: *The farmer grows cocoa.* "
              "A plural subject takes the verb without -s: *The farmers grow cocoa.* With the verb *be*: *is* and *was* are singular, *are* and *were* are plural. "
              "(*I* takes *am* and *was*; *you* takes *are* and *were*.)"),
            H("Find the real subject"),
            T("Words between the subject and the verb do not change the verb. Cross them out in your mind and ask: who or what does the action?"),
            CODE("""The price of tomatoes has risen.          (subject: price)
The pupils in the hall are noisy.         (subject: pupils)
The box of mangoes is heavy.              (subject: box)
The teacher, together with her pupils,
  is going to Limbe.                      (subject: teacher)""", "text", title="Interrupting phrases"),
            T("Phrases beginning with *together with*, *along with*, *as well as* and *with* do not make the subject plural. "
              "Only *and* joins two subjects into a plural."),
            MISTAKE("Common error: 'The price of tomatoes have risen'",
                    "The verb agrees with the head noun *price*, not with the nearer noun *tomatoes*. "
                    "Write *The price of tomatoes has risen.* In the same way, *The result of the tests were announced* should be "
                    "*The result of the tests was announced*, because the subject is *result*."),
            H("Joined subjects"),
            KEY("How to join subjects", "Look at the joining word.", cards=[
                ["and", "Two subjects joined by and take a plural verb: Ama and Ngu are friends."],
                ["or, nor, either...or, neither...nor", "The verb agrees with the nearer subject: Neither the driver nor the passengers were hurt. Neither the passengers nor the driver was hurt."],
                ["together with, as well as, along with", "These do not change the number: The principal, as well as the teachers, is present."],
            ]),
            H("Words that are always singular"),
            T("*Each*, *every*, *either*, *neither*, *everyone*, *everybody*, *someone*, *nobody* and *anything* take a singular verb, "
              "even when a plural noun follows: *Each of the girls has a uniform.* *Everybody is here.* *Neither of the answers is correct.*"),
            MISTAKE("Common error: 'Each of the students have a book'",
                    "*Each* is the subject, and it is singular. Write *Each of the students has a book.* "
                    "Similarly: *Everyone was happy*, not *Everyone were happy*."),
            H("There is and there are"),
            T("In sentences beginning with *there*, the real subject comes after the verb, and the verb agrees with it: "
              "*There is a taxi at the gate.* *There are three taxis at the gate.* "
              "Do not write *There is many people in the hall*; write *There are many people in the hall.*"),
            EX("Worked example 1: find the subject", intro="Choose the correct verb: 'The list of names (is / are) on the notice board.'", steps=[
                S("Find the subject", text="Ask: what is on the notice board? The list, not the names."),
                S("Number", text="List is singular, so the verb is singular."),
                S("Answer", text="The list of names is on the notice board."),
            ]),
            EX("Worked example 2: joined subjects", intro="Choose the correct verb: 'Either the manager or the cashiers (was / were) responsible for the missing money.'", steps=[
                S("Rule", text="With either...or, the verb agrees with the nearer subject."),
                S("Nearer subject", text="The nearer subject is 'cashiers', which is plural."),
                S("Answer", text="Either the manager or the cashiers were responsible for the missing money."),
            ]),
            EX("Worked example 3: there is and there are", intro="Choose the correct verb: 'There (is / are) forty pupils in Ama's class.'", steps=[
                S("Find the real subject", text="The subject comes after the verb: 'forty pupils'."),
                S("Number", text="Forty pupils is plural, so the verb is plural."),
                S("Answer", text="There are forty pupils in Ama's class."),
            ]),
            TIP("Exam link: concord is tested in the grammar section of Paper 1 (multiple choice), usually with a long subject or a phrase between subject and verb. "
                "Cross out the interrupting phrase, find the subject, and then decide.",
                title="Where this appears in the exam"),
            QUIZ("Which sentence is correct?",
                 ["The bag of oranges are on the table.", "Neither of the boys have finished.",
                  "The teacher, together with her pupils, are on the bus.", "Each of the farmers owns a plot."], 3,
                 "Each is singular, so owns is correct. In the other sentences the verb has been matched to the wrong word.",
                 hint="Find the head word of each subject.",
                 feedback=["The subject is bag (singular), so the verb should be 'is'.", "Neither is singular: 'has finished'.",
                           "The subject is teacher (singular): 'is on the bus'. Together with does not make it plural.", ""]),
            QUIZ("Choose the correct verb: 'Neither the girls nor the boy ___ ready.'",
                 ["are", "were", "is", "have been"], 2,
                 "With neither...nor, the verb agrees with the nearer subject. The boy is singular, so is.",
                 hint="Which subject is nearer the verb?",
                 feedback=["Are would match a plural subject; the nearer subject is boy.", "Were is plural.", "", "Have been is plural."]),
            PQ("Correct the sentence: 'The cost of the new desks were high.'",
               "The cost of the new desks was high. The subject is cost (singular)."),
            PQ("Correct the sentence: 'There is many students in the library.'",
               "There are many students in the library. The real subject, students, is plural."),
            PQ("Choose the correct verb: 'Neither the principal nor the teachers (was/were) present.'",
               "were. With neither...nor, the verb agrees with the nearer subject, teachers (plural)."),
            SUM("The verb agrees with its real subject, not with the noun nearest to it.",
                "Two subjects joined by and take a plural verb.",
                "With or, nor, either...or and neither...nor the verb agrees with the nearer subject.",
                "Each, every, everyone, somebody, nobody, neither and either take a singular verb.",
                "In there is and there are the verb agrees with the noun that follows."),
        ],
    ),
]

# ---------------------------------------------------------------------- 3b. Concord: tricky cases
LESSONS += [
    lesson(
        module=MODULE,
        topic="Subject-verb concord",
        title="Concord: tricky nouns, quantities and collectives",
        slug="egr-concord-tricky-cases",
        minutes=22,
        summary="Some nouns look plural but are singular (news, mathematics), some look singular but are plural (police, cattle), and amounts, fractions and collective nouns follow special rules.",
        objectives=[
            "Treat news, mathematics, physics and similar nouns as singular",
            "Treat police, people, cattle, trousers and scissors as plural",
            "Use singular verbs with amounts of money, time and distance, and decide with fractions",
            "Distinguish 'a number of' from 'the number of' and handle collective nouns",
        ],
        key_concepts=["Singular noun ending in -s", "Plural-only noun", "Collective noun", "A number of", "The number of", "Fraction"],
        blocks=[
            H("Introduction"),
            T("A radio presenter in Buea says, \"The news is read by Ama Fon.\" A listener who writes it down as \"The news are read\" has been misled by the final -s. "
              "The form of a noun does not always show its number. In this lesson you will learn the cases where the rule from the last lesson needs extra care."),
            H("Singular nouns that end in -s"),
            T("Some nouns end in -s but are singular. They take a singular verb."),
            CODE("""news            The news is good.
mathematics     Mathematics is my favourite subject.
physics         Physics was taught in Form Five.
economics       Economics is about money and choices.
politics        Politics is not discussed in the dormitory.
measles         Measles is a serious disease.
athletics       Athletics is popular in our school.""", "text", title="Singular, though they look plural"),
            H("Plural nouns"),
            T("Some nouns are always plural, even when they refer to one object or group: "
              "**trousers**, **jeans**, **shorts**, **scissors**, **spectacles**, **pliers**. We say *My trousers are dirty.* "
              "To speak about one, use *a pair of*: *A pair of scissors is on the desk.* (The singular noun *pair* takes the verb.)"),
            T("The words **police**, **people** and **cattle** have no singular form with -s and always take a plural verb: "
              "*The police are investigating.* *The people were waiting.* *The cattle are grazing.*"),
            MISTAKE("Common error: 'The police is' and 'The news are'",
                    "Remember: *police* is plural (*The police are here*), and *news* is singular (*The news is good*). "
                    "Learn these as pairs. The same warning applies to *Mathematics are* (wrong) and *My trouser is* (wrong; use *My trousers are*)."),
            H("Amounts and quantities"),
            T("An amount of money, time, distance or weight is treated as one quantity, so it takes a singular verb: "
              "*Ten thousand francs is a lot of money.* *Two weeks is a long time.* *Five kilometres is too far to walk.* "
              "But when we mean separate people or things that we count, the verb is plural: *Ten pupils are absent.*"),
            H("A number of and the number of"),
            KEY("Two similar expressions", "The first word decides.", cards=[
                ["A number of + plural noun", "Means 'several'. Takes a plural verb: A number of students are absent."],
                ["The number of + plural noun", "Means 'the total'. Takes a singular verb: The number of students is increasing."],
            ]),
            T("The phrase **one of the** + plural noun takes a singular verb, because *one* is the subject: *One of the boys is late.*"),
            H("Fractions and portions"),
            T("With fractions, percentages and words like *some*, *most* and *all*, the verb agrees with the noun after *of*: "
              "*Half of the rice is cooked.* (rice is uncountable) *Half of the pupils are absent.* (pupils is plural) "
              "*Two-thirds of the land is under cocoa.* *Most of the farmers are women.*"),
            H("Collective nouns"),
            T("A **collective noun** names a group (team, committee, class, family). In British English it takes a singular verb when the group acts as one unit, "
              "and a plural verb when we think of the members acting separately. A later pronoun shows which one you have chosen: "
              "*The committee has made its decision.* *The committee have gone to their homes.* Keep the verb and the pronoun consistent."),
            T("Names of books, films and organisations are also singular: *Things Fall Apart is a famous novel.* *The United Nations is based in New York.*"),
            EX("Worked example 1: singular or plural?", intro="Choose the correct verb: (a) The news (was / were) broadcast at seven. (b) The scissors (is / are) on the table. (c) The cattle (is / are) near the river.", steps=[
                S("(a)", text="News is singular: was."),
                S("(b)", text="Scissors is always plural: are."),
                S("(c)", text="Cattle is always plural: are."),
                S("Answer", text="(a) was (b) are (c) are"),
            ]),
            EX("Worked example 2: a number of or the number of", intro="Choose the correct verb: (a) A number of farmers (was / were) at the meeting. (b) The number of farmers (has / have) grown this year.", steps=[
                S("(a)", text="'A number of' means several, so it takes a plural verb: were."),
                S("(b)", text="'The number of' means the total, which is singular: has."),
                S("Answer", text="(a) were (b) has")
            ]),
            EX("Worked example 3: amounts and fractions", intro="Choose the correct verb: (a) Five hundred francs (is / are) not enough for a taxi to Limbe. (b) Three-quarters of the water (was / were) wasted. (c) Three-quarters of the pupils (was / were) present.", steps=[
                S("(a)", text="An amount of money is one quantity: is."),
                S("(b)", text="Water is uncountable: was."),
                S("(c)", text="Pupils is plural: were."),
                S("Answer", text="(a) is (b) was (c) were"),
            ]),
            TIP("Exam link: concord traps such as news, mathematics, police and a number of are favourite items in the grammar section of Paper 1 (multiple choice). "
                "Learn the short lists in this lesson by heart; they appear again and again.",
                title="Where this appears in the exam"),
            QUIZ("Which sentence is correct?",
                 ["Mathematics are taught every day.", "The police is searching the house.", "A pair of trousers were left on the bus.", "The number of taxis in the town has doubled."], 3,
                 "The number of takes a singular verb: has doubled. The others use the wrong verb form.",
                 hint="Remember which words are singular and which are plural.",
                 feedback=["Mathematics is singular: 'is taught'.", "Police is plural: 'are searching'.", "A pair of ... is singular: 'was left'.", ""]),
            QUIZ("Choose the correct completion: 'One of my cousins ___ in Kumba.'",
                 ["live", "lives", "have lived", "are living"], 1,
                 "The subject is one, which is singular, so lives.",
                 hint="Which word is the subject: one or cousins?",
                 feedback=["Live is plural: the subject is 'one'.", "", "Have lived is plural.", "Are living is plural."]),
            PQ("Correct the sentence: 'The news about the exams are on the notice board.'",
               "The news about the exams is on the notice board. News is singular."),
            PQ("Choose the correct verb: 'A number of passengers (was/were) injured in the accident.'",
               "were. A number of means several, so the verb is plural."),
            PQ("Choose the correct verb: 'Fifty thousand francs (is/are) what the njangi collected.'",
               "is. An amount of money is treated as one quantity."),
            SUM("News, mathematics, physics, economics, politics and measles are singular.",
                "Police, people, cattle, trousers and scissors are plural.",
                "An amount of money, time or distance takes a singular verb.",
                "A number of takes a plural verb; the number of takes a singular verb; one of the + plural takes a singular verb.",
                "With fractions, the verb agrees with the noun after of.",
                "A collective noun is singular when the group acts as one, plural when its members act separately."),
        ],
    ),
]

# ---------------------------------------------------------------------- 4. Adjectives, adverbs, comparatives
LESSONS += [
    lesson(
        module=MODULE,
        topic="Adjectives, adverbs and comparatives",
        title="Adjectives, adverbs and degrees of comparison",
        slug="egr-adjectives-adverbs-comparison",
        minutes=24,
        summary="Adjectives describe nouns and adverbs describe verbs, adjectives and other adverbs. Comparison uses -er and -est or more and most, with a few irregular forms such as better and worse.",
        objectives=[
            "Tell adjectives from adverbs and use good and well correctly",
            "Form comparatives and superlatives, regular and irregular",
            "Avoid double comparatives such as 'more better' and 'most tallest'",
            "Place adverbs of frequency and put adjectives in the usual order",
        ],
        key_concepts=["Adjective", "Adverb", "Comparative", "Superlative", "Linking verb", "Adverb of frequency"],
        blocks=[
            H("Introduction"),
            T("A customer at a market in Bamenda says, \"These plantains are bigger than those, but the other stall sells the biggest ones.\" "
              "She is comparing. She uses *big* in two other forms: *bigger* and *the biggest*. "
              "She could also describe how the seller works: *She sells plantains quickly.* "
              "Adjectives and adverbs give detail, and comparison helps us choose."),
            H("Adjectives and adverbs"),
            D("An **adjective** describes a noun or pronoun (a *ripe* mango; she is *kind*). "
              "An **adverb** describes a verb, an adjective or another adverb (she walks *slowly*; *very* kind; *quite* slowly).",
              title="Definitions"),
            T("Many adverbs are formed by adding -ly to an adjective: slow, slowly; careful, carefully; happy, happily (y becomes i). "
              "Some adverbs have no -ly or have a different form."),
            CODE("""Adjective   Adverb      Example
good        well        She sings well.
fast        fast        He drives fast.
hard        hard        They work hard.
late        late        She arrived late.
early       early       We left early.""", "text", title="Irregular adverbs"),
            T("Watch out: *hardly* means 'almost not' (*He hardly slept*), and *lately* means 'recently'. They are different from *hard* and *late*."),
            MISTAKE("Common error: 'He sings good' and 'She runs quick'",
                    "Use an adverb to describe a verb: *He sings well.* *She runs quickly* (or *fast*). "
                    "*Good* is an adjective (*a good singer*)."),
            KEY("Linking verbs take adjectives", "After be, seem, look, feel, taste, smell, sound and become, use an adjective.", cards=[
                ["Correct", "The soup tastes delicious. The room smells fresh. She looks tired."],
                ["Incorrect", "The soup tastes deliciously. She looks tiredly."],
            ]),
            H("Comparison"),
            T("Adjectives and adverbs have three degrees. The **positive** is the plain form (*tall*). "
              "The **comparative** compares two things (*taller*). The **superlative** picks one out of three or more (*the tallest*)."),
            CODE("""One syllable:        add -er / -est          tall, taller, tallest
Ending in one vowel + consonant: double it   big, bigger, biggest
Ending in -y:        change y to i           happy, happier, happiest
Longer words:        use more / most         expensive, more expensive, most expensive""", "text", title="Regular forms"),
            CODE("""good / well   better    best
bad / badly   worse     worst
much / many   more      most
little        less      least
far           farther / further    farthest / furthest""", "text", title="Irregular forms"),
            T("Use *than* after a comparative: *Ngu is taller than Kum.* Use *the* before a superlative: *Ngu is the tallest boy in the class.* "
              "To say two things are equal, use *as ... as*: *Ama is as tall as Ngu.* In a negative, *not as ... as* or *not so ... as*."),
            MISTAKE("Common error: 'more better', 'most tallest', 'more bigger'",
                    "Do not use *more* or *most* with a word that already has -er or -est. "
                    "Write *better* (not *more better*), *the tallest* (not *the most tallest*), *bigger* (not *more bigger*). "
                    "Also write *than*, not *that*: *taller than Kum*."),
            H("Position of adverbs and order of adjectives"),
            T("Adverbs of frequency (*always, usually, often, sometimes, never*) go before the main verb but after *be*: "
              "*She always arrives early.* *He is never late.*"),
            T("When several adjectives come before a noun, the usual order is opinion, size, age, colour, origin, material: "
              "*a lovely big old brown wooden table.* You rarely need more than two or three adjectives."),
            EX("Worked example 1: adjective or adverb?", intro="Choose the correct word: (a) The student answered (correct / correctly). (b) The fish smells (bad / badly). (c) He works very (hard / hardly).", steps=[
                S("(a)", text="'Answered' is a verb, so we need an adverb: correctly."),
                S("(b)", text="'Smells' here is a linking verb (describing the fish), so an adjective: bad."),
                S("(c)", text="'Works hard' means works with effort. 'Hardly' means almost not, so hard."),
                S("Answer", text="(a) correctly (b) bad (c) hard"),
            ]),
            EX("Worked example 2: forming comparatives and superlatives", intro="Write the comparative and superlative of: (a) heavy (b) beautiful (c) good (d) thin.", steps=[
                S("(a) heavy", text="Ends in -y: heavier, heaviest."),
                S("(b) beautiful", text="A long word: more beautiful, most beautiful."),
                S("(c) good", text="Irregular: better, best."),
                S("(d) thin", text="One vowel + one consonant, so double the consonant: thinner, thinnest."),
            ]),
            EX("Worked example 3: correcting errors", intro="Correct: 'Of the two sisters, Ama is the most intelligent, and she speaks English more better than her brother.'", steps=[
                S("Of the two", text="With two things, use the comparative: the more intelligent."),
                S("More better", text="Better is already comparative: she speaks English better than her brother."),
                S("Answer", text="Of the two sisters, Ama is the more intelligent, and she speaks English better than her brother."),
            ]),
            TIP("Exam link: adjective, adverb and comparison items appear in the grammar section of Paper 1 (multiple choice). "
                "In Paper 2, correct comparison and adverb forms support the accuracy of your writing. Check every 'more' and 'most' you write.",
                title="Where this appears in the exam"),
            QUIZ("Which sentence is correct?",
                 ["This is the most cheapest shop in the market.", "Her handwriting is more better than mine.", "The taxi driver drove careful.", "He is the tallest of the three brothers."], 3,
                 "Only the last sentence is correct. Tallest is a regular superlative used with three or more.",
                 hint="Check for double comparatives and wrong adverb forms.",
                 feedback=["Cheapest already shows the superlative: 'the cheapest shop'.", "Better is already comparative: 'better than mine'.", "Use the adverb 'carefully'.", ""]),
            QUIZ("Choose the correct completion: 'The soup tastes ___.'",
                 ["well", "deliciously", "delicious", "deliciousness"], 2,
                 "Taste is a linking verb here and is followed by an adjective: delicious.",
                 hint="Is the word describing the soup or the way somebody tastes?",
                 feedback=["Well is an adverb (or an adjective only for health).", "An adverb cannot follow a linking verb here.", "", "That is a noun."]),
            PQ("Write the comparative and superlative of 'bad', 'far' and 'noisy'.",
               "bad: worse, worst. far: farther (or further), farthest (or furthest). noisy: noisier, noisiest."),
            PQ("Correct the sentence: 'She is more taller than her brother, and she sings good.'",
               "She is taller than her brother, and she sings well. Taller already shows the comparative; the verb sings needs an adverb."),
            PQ("Place the adverb in the sentence: 'Mr Ndi arrives at school before seven.' (always)",
               "Mr Ndi always arrives at school before seven. An adverb of frequency goes before the main verb."),
            SUM("Adjectives describe nouns; adverbs describe verbs, adjectives and adverbs.",
                "Linking verbs (be, seem, look, feel, taste) take adjectives: The soup tastes delicious.",
                "Good is an adjective and well an adverb: She sings well.",
                "Comparatives and superlatives: tall, taller, tallest; beautiful, more beautiful, most beautiful; good, better, best.",
                "Never combine more or most with -er or -est: not more better, not most tallest.",
                "Use the comparative for two things and the superlative for three or more."),
        ],
    ),
]

# ---------------------------------------------------------------------- 5. Prepositions and conjunctions
LESSONS += [
    lesson(
        module=MODULE,
        topic="Prepositions and conjunctions",
        title="Prepositions and conjunctions",
        slug="egr-prepositions-conjunctions",
        minutes=24,
        summary="Prepositions link nouns to the rest of the sentence (at, in, on, to), and some verbs take none at all (discuss, enter). Conjunctions join words and clauses, and only one is needed in each link.",
        objectives=[
            "Use at, in and on for time and place, and for and since for duration",
            "Use the correct preposition after common verbs and adjectives, and avoid 'discuss about' and 'enter into the room'",
            "Choose coordinating and subordinating conjunctions correctly",
            "Avoid double conjunctions such as 'although ... but' and non-standard connectives",
        ],
        key_concepts=["Preposition", "Dependent preposition", "Conjunction", "Coordinating conjunction", "Subordinating conjunction", "Connective"],
        blocks=[
            H("Introduction"),
            T("A taxi driver says, \"I will drop you at the junction, on Monday, in the morning, because the road is bad.\" "
              "Each small word (*at*, *on*, *in*) is a preposition, and *because* is a conjunction. "
              "These short words are easy to overlook, but they carry the meaning of time, place and reason."),
            H("Prepositions"),
            D("A **preposition** shows the relationship of a noun or pronoun to another word: time, place, direction or manner. "
              "It is followed by a noun, a pronoun or an -ing form (*in the market*, *with her*, *after eating*).",
              title="Definition"),
            CODE("""Time    at   clock times and points: at 6 a.m., at night, at noon
        on   days and dates: on Monday, on 11 February
        in   months, years, seasons, parts of the day: in May, in 2020, in the morning
        for  a length of time: for two hours      since  a starting point: since Monday
Place   at   a point: at the gate, at the bus stop
        in   inside: in the classroom, in Douala
        on   on a surface: on the table, on the wall
Motion  to   towards a place: go to Limbe       into  entering: walk into the room""", "text", title="Prepositions of time, place and movement"),
            H("Verbs that take no preposition"),
            T("Some verbs already contain the idea and need no preposition. Adding one is a common error."),
            CODE("""Say this                      Not this
discuss the problem           discuss about the problem
enter the hall                enter into the hall
reach Bamenda                 reach at / reach to Bamenda
attend the meeting            attend to the meeting
emphasise the point           emphasise on the point
marry her                     marry with her
explain it to me              explain me""", "text", title="No preposition"),
            MISTAKE("Common error: 'discuss about' and 'emphasize on'",
                    "*Discuss*, *enter*, *reach*, *attend*, *emphasise* and *marry* take a direct object without a preposition. "
                    "Write *We discussed the plan*, *He entered the hall*, *They reached Bamenda at noon*. "
                    "Notice also *explain to*: *Please explain the question to me*, not *explain me the question*. "
                    "Also avoid *return back* and *repeat again*: *return* and *repeat* already include the idea."),
            H("Fixed pairs"),
            T("Many adjectives and verbs go with a particular preposition. Learn them as pairs."),
            CODE("""good at maths          afraid of snakes         interested in music
depend on rain         listen to the radio      responsible for the shop
angry with a person    angry about a decision   aware of the danger
congratulate on        prefer tea to coffee     different from the others
arrive at a place (small)   arrive in a city    approve of the plan""", "text", title="Common pairs"),
            H("Conjunctions"),
            D("A **conjunction** joins words, phrases or clauses. **Coordinating conjunctions** (and, but, or, so, for, nor, yet) join equal parts. "
              "**Subordinating conjunctions** (because, although, when, if, unless, while, since, so that) join a dependent clause to a main clause.",
              title="Definition"),
            KEY("Choose the right conjunction", "The meaning decides.", cards=[
                ["Addition", "and, as well as, both...and: She sells fish and plantains."],
                ["Contrast", "but, yet, although, though, while: Although it was raining, we played."],
                ["Reason and result", "because, since, as, so: He was late because the taxi broke down. The taxi broke down, so he was late."],
                ["Condition", "if, unless, provided that: Unless you pay, you will not get the ticket."],
                ["Purpose and time", "so that, in order that, when, before, after, until: She saved money so that she could buy a phone."],
            ]),
            MISTAKE("Common error: 'Although it rained, but we went' and 'Because he was ill, so he stayed'",
                    "One link needs one conjunction. Write *Although it rained, we went* or *It rained, but we went*. "
                    "Write *Because he was ill, he stayed* or *He was ill, so he stayed*. "
                    "Also write *despite* or *in spite of*, never *despite of*."),
            MISTAKE("Common error: non-standard connectives",
                    "Words such as *moreso*, *nextly*, *better still*, *more still* and *further still* are not standard English connectives. "
                    "Use *moreover*, *furthermore*, *in addition*, *also*, *next*, *finally*. "
                    "(*More so* as two words is acceptable to mean 'even more': *It is cold, and more so at night*.) "
                    "The Board's report on the written paper mentions this problem."),
            T("Words such as *however*, *therefore*, *moreover* and *nevertheless* are connecting adverbs, not conjunctions. "
              "When they join two main clauses, put a semicolon or full stop before them and a comma after: "
              "*He was tired; however, he continued working.*"),
            EX("Worked example 1: removing unnecessary prepositions", intro="Correct: 'We discussed about the matter and then entered into the hall.'", steps=[
                S("Discuss", text="'Discuss' takes a direct object: discussed the matter."),
                S("Enter", text="'Enter' also takes a direct object: entered the hall."),
                S("Answer", text="We discussed the matter and then entered the hall."),
            ]),
            EX("Worked example 2: time prepositions", intro="Fill the gaps with at, on or in: (a) The meeting starts ___ 10 a.m. (b) She was born ___ 2008. (c) We play football ___ Saturday. (d) It rains a lot ___ August.", steps=[
                S("Rule", text="at: clock times; in: years and months; on: days."),
                S("Apply", text="(a) at 10 a.m. (b) in 2008 (c) on Saturday (d) in August."),
                S("Answer", text="(a) at (b) in (c) on (d) in"),
            ]),
            EX("Worked example 3: joining sentences", intro="Join with a suitable conjunction: 'It was raining. We went to the market.'", steps=[
                S("Relationship", text="The rain might have stopped us, but it did not. This is contrast."),
                S("Choose", text="Although, though, but, yet."),
                S("Answer", text="Although it was raining, we went to the market. (or: It was raining, but we went to the market.)"),
            ]),
            TIP("Exam link: prepositions and conjunctions are common in the grammar section of Paper 1 (multiple choice). "
                "In Paper 2, correct linking words help your paragraphs flow, but the Board's report warns against non-standard connectives. Use a small set you are sure about.",
                title="Where this appears in the exam"),
            QUIZ("Which sentence is correct?",
                 ["The committee discussed about the fees.", "Although she was tired, but she finished the work.", "We arrived in Douala on Monday at noon.", "He is good in mathematics."], 2,
                 "Only the third is correct: arrive in a city, on for a day, at for a clock time.",
                 hint="Check for an extra preposition or an extra conjunction.",
                 feedback=["Discuss takes no preposition.", "Use only one conjunction: although or but.", "", "The usual pair is 'good at'."]),
            QUIZ("Choose the correct completion: 'I prefer rice ___ plantains.'",
                 ["than", "to", "from", "over"], 1,
                 "Prefer is followed by to: prefer X to Y.",
                 hint="Prefer has its own preposition.",
                 feedback=["Than follows a comparative, not prefer.", "", "From follows different.", "Over is not used with prefer in this structure."]),
            PQ("Correct: 'She emphasised on the importance of honesty and returned back to her seat.'",
               "She emphasised the importance of honesty and returned to her seat. Emphasise takes no preposition; return already means go back."),
            PQ("Fill the gap with for or since: 'Ngu has lived in Buea ___ 2015, and his sister has lived there ___ ten years.'",
               "since 2015 (a starting point); for ten years (a length of time)."),
            PQ("Join with a suitable conjunction: 'You must study. You will not pass.'",
               "Unless you study, you will not pass. (Or: If you do not study, you will not pass.)"),
            SUM("At is for points and clock times, on for days, in for months, years and enclosed spaces.",
                "Discuss, enter, reach, attend and emphasise take no preposition.",
                "Many words go with fixed prepositions: good at, afraid of, depend on, prefer X to Y.",
                "Use one conjunction per link: not although...but, not because...so.",
                "Do not use moreso, nextly, better still or more still; use moreover, furthermore, in addition or next."),
        ],
    ),
]

# ---------------------------------------------------------------------- 6. Active and passive voice
LESSONS += [
    lesson(
        module=MODULE,
        topic="Active and passive voice",
        title="Active and passive voice",
        slug="egr-active-passive-voice",
        minutes=24,
        summary="In the active voice the doer is the subject; in the passive voice the receiver is the subject. Form the passive with a form of be plus the past participle, keeping the tense of the active verb.",
        objectives=[
            "Change active sentences to passive and passive to active in all common tenses",
            "Use the passive appropriately when the doer is unknown or unimportant",
            "Explain why intransitive verbs have no passive",
            "Handle sentences with two objects and questions",
        ],
        key_concepts=["Active voice", "Passive voice", "Agent", "Past participle", "Transitive verb", "Intransitive verb"],
        blocks=[
            H("Introduction"),
            T("At a school in Kumba the notice says: \"All fees must be paid before Friday.\" "
              "It does not say who must pay. The focus is on the fees. A newspaper writes: \"A suspect was arrested at the motor park.\" "
              "The police arrested him, but what matters is the arrest. This is the **passive voice**, and it is the topic of this lesson."),
            H("Voice"),
            D("In the **active voice** the subject does the action: *Mama Ngo sells fish.* "
              "In the **passive voice** the subject receives the action: *Fish is sold by Mama Ngo.* "
              "The doer of the action is called the **agent**.",
              title="Definitions"),
            T("Only **transitive verbs** (verbs that take an object) can have a passive. The object of the active sentence becomes the subject of the passive sentence."),
            D("To form the passive: **subject (old object) + a form of be + past participle (+ by + agent)**. "
              "The form of *be* shows the tense of the active verb.",
              title="Rule"),
            CODE("""Tense                 Active                  Passive
Present simple        writes a letter         a letter is written
Present continuous    is writing a letter     a letter is being written
Past simple           wrote a letter          a letter was written
Past continuous       was writing a letter    a letter was being written
Present perfect       has written a letter    a letter has been written
Past perfect          had written a letter    a letter had been written
Future (will)         will write a letter     a letter will be written
Modal (can, must)     can write a letter      a letter can be written""", "text", title="Active and passive in different tenses"),
            T("Use the passive when the doer is unknown (*My phone was stolen*), unimportant (*The road was repaired*), "
              "or when you want to put the receiver first or sound formal (*The results will be announced on Monday*)."),
            H("Steps for changing active to passive"),
            EX("Worked example 1: present simple", intro="Change to the passive: 'Mama Ngo sells fish in the market.'", steps=[
                S("Find the parts", text="Subject: Mama Ngo. Verb: sells (present simple). Object: fish."),
                S("Move the object to the front", text="Fish ..."),
                S("Add be (present) + past participle", text="Fish is sold ..."),
                S("Add the agent with by", text="Fish is sold in the market by Mama Ngo."),
            ]),
            EX("Worked example 2: present perfect", intro="Change to the passive: 'The farmers have harvested the cocoa.'", steps=[
                S("Parts", text="Verb: have harvested (present perfect). Object: the cocoa."),
                S("Passive pattern", text="has/have + been + past participle. The new subject, cocoa, is singular: has been harvested."),
                S("Answer", text="The cocoa has been harvested by the farmers."),
            ]),
            EX("Worked example 3: future", intro="Change to the passive: 'The headmaster will announce the results tomorrow.'", steps=[
                S("Parts", text="Verb: will announce. Object: the results."),
                S("Passive pattern", text="will + be + past participle: will be announced."),
                S("Answer", text="The results will be announced by the headmaster tomorrow."),
            ]),
            H("Special cases"),
            T("**Two objects.** Some verbs (give, send, show, tell) take two objects, so there are two passives: "
              "*The teacher gave Ama a prize.* becomes *Ama was given a prize.* or *A prize was given to Ama.* The first is more common."),
            T("**Questions.** *Did Ngu break the window?* becomes *Was the window broken by Ngu?* "
              "*Who wrote this letter?* becomes *By whom was this letter written?*"),
            MISTAKE("Common error: passive of intransitive verbs ('The accident was happened')",
                    "Verbs that take no object (*happen, arrive, die, occur, seem, fall, sleep*) cannot be made passive. "
                    "Write *The accident happened*, not *The accident was happened*. The same applies to *was arrived* and *was died*."),
            MISTAKE("Common error: wrong participle ('The window was broke')",
                    "The passive needs the **past participle**, not the past simple: *The window was broken*, *The letter was written*, *The cocoa was sold*, *The money was stolen*. "
                    "Learn the irregular participles: break, broken; write, written; steal, stolen; take, taken; give, given."),
            T("Do not overuse the passive. *Mama Ngo sold the fish* is shorter and clearer than *The fish was sold by Mama Ngo.* "
              "Use the passive when it has a reason."),
            TIP("Exam link: transformation between active and passive appears in the grammar section of Paper 1 (multiple choice), where you pick the correct passive form. "
                "In Paper 2, a formal report or letter often uses the passive appropriately. First find the tense, then build be + past participle in the same tense.",
                title="Where this appears in the exam"),
            QUIZ("Which is the correct passive of 'The taxi driver was taking the passengers to Limbe'?",
                 ["The passengers were taken to Limbe by the taxi driver.", "The passengers were being taken to Limbe by the taxi driver.",
                  "The passengers are being taken to Limbe by the taxi driver.", "The passengers have been taken to Limbe by the taxi driver."], 1,
                 "The active verb is in the past continuous (was taking), so the passive is was/were being + past participle.",
                 hint="Keep the tense: past continuous becomes was/were being + past participle.",
                 feedback=["That is the past simple passive, which loses the continuous meaning.", "",
                           "That is the present continuous passive.", "That is the present perfect passive."]),
            QUIZ("Which sentence is correct?",
                 ["The bus was arrived late.", "The thief was ran away.", "The money was stolen by two boys.", "The glass was broke."], 2,
                 "Only the third sentence uses a transitive verb in the passive with the correct participle.",
                 hint="Look for a transitive verb and a past participle.",
                 feedback=["Arrive is intransitive: 'The bus arrived late.'", "Run away is intransitive: 'The thief ran away.'", "", "The participle is 'broken'."]),
            PQ("Change to the passive: 'The headmaster has punished the boys.'",
               "The boys have been punished by the headmaster. (Present perfect: have been + past participle.)"),
            PQ("Change to the passive: 'Someone stole my phone at the market.'",
               "My phone was stolen at the market. The agent 'someone' is unknown and is dropped."),
            PQ("Change to the active: 'The match was cancelled by the referee because of the rain.'",
               "The referee cancelled the match because of the rain. The agent becomes the subject; the verb returns to the past simple."),
            SUM("In the active voice the doer is the subject; in the passive the receiver is the subject.",
                "Passive = a form of be (in the same tense as the active verb) + past participle (+ by + agent).",
                "Use the passive when the doer is unknown, unimportant or when you want a formal tone.",
                "Intransitive verbs (happen, arrive, die) cannot be passive.",
                "Use the past participle: was broken, not was broke."),
        ],
    ),
]

# ---------------------------------------------------------------------- 7. Direct and reported speech
LESSONS += [
    lesson(
        module=MODULE,
        topic="Direct and reported speech",
        title="Direct and reported speech",
        slug="egr-direct-reported-speech",
        minutes=26,
        summary="Reported speech tells what someone said without quoting the exact words. Change the tense (backshift), pronouns and time and place words, and use say or tell correctly.",
        objectives=[
            "Change statements, questions and commands from direct to reported speech",
            "Backshift tenses and change pronouns, time words and place words",
            "Use say and tell correctly and avoid 'he said me'",
            "Choose suitable reporting verbs",
        ],
        key_concepts=["Direct speech", "Reported speech", "Backshift", "Reporting verb", "Reporting clause", "Indirect question"],
        blocks=[
            H("Introduction"),
            T("A student comes home from school in Bamenda and tells her mother, \"The headmaster said that classes would end early on Friday.\" "
              "The headmaster actually said, \"Classes will end early on Friday.\" "
              "The student has reported his words. Notice that *will* became *would*. This lesson shows the changes."),
            H("What changes"),
            D("**Direct speech** gives the speaker's exact words in quotation marks. **Reported speech** (or indirect speech) tells what was said without quoting: "
              "the words are changed to fit the new situation and the quotation marks are removed.",
              title="Definitions"),
            T("When the reporting verb is in the past (*said*, *told*, *asked*), we usually **backshift**: the verb moves one step back in time."),
            CODE("""Direct                      Reported
present simple              past simple
  'I live here'               he said he lived there
present continuous          past continuous
  'I am working'              she said she was working
past simple                 past perfect
  'I bought it'               he said he had bought it
present perfect             past perfect
  'I have finished'           she said she had finished
will                        would
can                         could
may                         might
must                        had to (or must)
would, could, should, might   no change""", "text", title="Backshift"),
            CODE("""now             then
today           that day
tonight         that night
tomorrow        the next day / the following day
yesterday       the day before / the previous day
last week       the week before / the previous week
next week       the week after / the following week
ago             before
this            that
here            there""", "text", title="Time and place words"),
            T("**Pronouns** change according to the point of view: *\"I am tired,\" Ama said.* becomes *Ama said that she was tired.* "
              "Do not backshift if the statement is still true now or the reporting verb is in the present: *Ngu says that he is tired.*"),
            EX("Worked example 1: a statement", intro="Report: \"I am going to Bafoussam tomorrow,\" said Ngu.", steps=[
                S("Reporting clause", text="Ngu said that ..."),
                S("Pronoun", text="'I' becomes he."),
                S("Backshift", text="am going becomes was going."),
                S("Time word", text="tomorrow becomes the next day."),
                S("Answer", text="Ngu said that he was going to Bafoussam the next day."),
            ]),
            H("Questions and commands"),
            T("In reported **questions**, use statement word order (subject before verb), no question mark, and no *do*, *does* or *did*. "
              "For yes/no questions, use *if* or *whether*. For *wh*- questions, keep the question word."),
            EX("Worked example 2: questions", intro="Report: (a) \"Where do you sell your tomatoes?\" the customer asked Mama Ngo. (b) \"Have you paid the fees?\" the bursar asked me.", steps=[
                S("(a) Word order", text="Wh- question, so keep 'where'. Use statement order, backshift do you sell to she sold, you to she, your to her."),
                S("(a) Answer", text="The customer asked Mama Ngo where she sold her tomatoes."),
                S("(b) Yes/no question", text="Use if or whether. Present perfect backshifts to past perfect. You becomes I."),
                S("(b) Answer", text="The bursar asked me if (or whether) I had paid the fees."),
            ]),
            T("Reported **commands and requests** use a **to-infinitive**: *told/asked/ordered + person + (not) to + verb.*"),
            EX("Worked example 3: commands", intro="Report: (a) \"Don't be late for the njangi meeting,\" the president told us. (b) \"Please open the window,\" Ama asked Kum.", steps=[
                S("(a)", text="Negative command: told us not to be late."),
                S("(a) Answer", text="The president told us not to be late for the njangi meeting."),
                S("(b)", text="Request: asked Kum to open the window."),
                S("(b) Answer", text="Ama asked Kum to open the window."),
            ]),
            H("Say and tell"),
            KEY("Say and tell are used differently", "Watch the object.", cards=[
                ["say", "Not followed directly by a person: He said that he was tired. He said to me that he was tired."],
                ["tell", "Always followed by a person: He told me that he was tired."],
            ]),
            MISTAKE("Common error: 'He said me' and 'He told that'",
                    "*Said me* is not correct. Write *He told me* or *He said to me*. "
                    "And *told* needs a person: *He told me that he was tired*, not *He told that he was tired*. "
                    "Also avoid *suggested me to go*; write *suggested that I go (or should go)* or *suggested going*."),
            MISTAKE("Common error: keeping the question order in reported questions",
                    "Wrong: *She asked me where did I live.* Correct: *She asked me where I lived.* "
                    "The question form (did, do, does) and the question mark are used only in direct speech."),
            MISTAKE("Common error: forgetting to change time words and pronouns",
                    "Wrong: *He said that he would come tomorrow* (if the report is made on a later day). "
                    "Check *tomorrow*, *yesterday*, *here* and *now*, and make sure *I*, *you* and *my* match the new speaker."),
            TIP("Exam link: direct and reported speech transformations appear in the grammar section of Paper 1 (multiple choice), and the skill also helps in writing "
                "when you report what people said in a story or report. Always change the pronoun, the tense and the time word, then reread for word order.",
                title="Where this appears in the exam"),
            QUIZ("Choose the correct reported form of: \"I have finished my homework,\" Ama said.",
                 ["Ama said that she has finished her homework.", "Ama said that she had finished her homework.", "Ama said that I had finished my homework.", "Ama said me that she finished her homework."], 1,
                 "Present perfect becomes past perfect, and I becomes she.",
                 hint="Backshift the verb and change the pronouns.",
                 feedback=["Has finished is not backshifted.", "", "The pronouns were not changed.", "Said me is wrong, and the tense is wrong."]),
            QUIZ("Choose the correct reported form of: \"Where do you live?\" he asked her.",
                 ["He asked her where did she live.", "He asked her where she lived.", "He asked her where does she live.", "He asked her that where she lived."], 1,
                 "Use statement order, no do, and backshift: where she lived.",
                 hint="Reported questions use statement word order.",
                 feedback=["Did is not used in a reported question.", "", "Does is not used in a reported question.", "Do not add 'that' before a question word."]),
            PQ("Report: \"I will call you tonight,\" Kum said to Ama.",
               "Kum told Ama that he would call her that night. (will becomes would; tonight becomes that night; I becomes he; you becomes her.)"),
            PQ("Report: \"Do you like football?\" the teacher asked Ndi.",
               "The teacher asked Ndi if (or whether) he liked football."),
            PQ("Correct: 'The driver said me to sit down.'",
               "The driver told me to sit down. (Say cannot be followed directly by a person; tell can.)"),
            SUM("Reported speech removes the quotation marks and changes pronouns, tenses and time and place words.",
                "Backshift: present to past, past to past perfect, will to would, can to could.",
                "Reported questions use statement order, no do/did, and if/whether for yes/no questions.",
                "Reported commands use told/asked + person + (not) to + verb.",
                "Say is not followed directly by a person; tell is: He told me, not He said me."),
        ],
    ),
]

# ---------------------------------------------------------------------- 8a. Clauses: main, subordinate, relative
LESSONS += [
    lesson(
        module=MODULE,
        topic="Clauses",
        title="Main, subordinate and relative clauses",
        slug="egr-clauses-main-subordinate-relative",
        minutes=24,
        summary="A clause has a subject and a finite verb. A main clause can stand alone; a subordinate clause cannot. Relative clauses with who, which, whose and that describe nouns, with or without commas.",
        objectives=[
            "Identify a clause and tell main clauses from subordinate clauses",
            "Recognise noun, adverb and relative (adjective) clauses",
            "Use who, whom, whose, which and that correctly, with and without commas",
            "Avoid sentence fragments and double pronouns such as 'the boy who he came'",
        ],
        key_concepts=["Clause", "Main clause", "Subordinate clause", "Relative clause", "Relative pronoun", "Defining clause", "Sentence fragment"],
        blocks=[
            H("Introduction"),
            T("A woman at a market in Limbe says, \"I bought the fish that the fisherman brought this morning, and I will cook it when I get home.\" "
              "This one sentence contains four groups of words, each with its own verb. Each group is a clause. "
              "Understanding clauses helps you write long sentences without errors."),
            H("What a clause is"),
            D("A **clause** is a group of words that contains a subject and a finite verb (a verb with a tense). "
              "A **main clause** (independent clause) makes complete sense on its own. "
              "A **subordinate clause** (dependent clause) depends on a main clause and cannot stand alone.",
              title="Definitions"),
            CODE("""Main clause:          The farmer sold his cocoa.
Subordinate clause:   because the price was good
Together:             The farmer sold his cocoa because the price was good.""", "text", title="Main and subordinate"),
            T("A sentence with one main clause is **simple**. A sentence with two or more main clauses joined by and, but, or or so is **compound**. "
              "A sentence with a main clause and at least one subordinate clause is **complex**."),
            KEY("Three kinds of subordinate clause", "Ask what job the clause does.", cards=[
                ["Noun clause", "Works like a noun: I know that she is honest. (what I know)"],
                ["Adverb clause", "Tells when, where, why, how or under what condition: She left when the bell rang. We stayed home because it rained."],
                ["Relative (adjective) clause", "Describes a noun: The woman who sells plantains lives next door."],
            ]),
            H("Relative clauses"),
            D("A **relative clause** begins with a **relative pronoun** (who, whom, whose, which, that) or a relative adverb (where, when) and describes the noun before it.",
              title="Definition"),
            CODE("""who      for people (subject)        the teacher who marked my script
whom     for people (object)         the teacher whom we respect
whose    possession                  the boy whose bicycle was stolen
which    for things                  the book which I lost
that     people or things            the driver that took us / the car that broke down
where    place                       the village where I was born
when     time                        the day when we met""", "text", title="Relative pronouns"),
            T("**Defining** relative clauses identify which person or thing we mean. They have no commas and may use *that*: "
              "*The girl who won the prize is my cousin.* "
              "**Non-defining** relative clauses add extra information. They are separated by commas and never use *that*: "
              "*My uncle, who lives in Buea, is a doctor.* *The bridge, which was built in 1950, is closed.*"),
            MISTAKE("Common error: 'which' for people and 'who he'",
                    "Use *who* for people: *The man who sold me the phone* (not *which sold*). "
                    "Do not repeat the subject after the relative pronoun: *The boy who came yesterday is my cousin*, not *The boy who he came yesterday*. "
                    "Also: *This is the school where I studied*, not *where I studied there*."),
            MISTAKE("Common error: sentence fragments",
                    "A subordinate clause alone is not a sentence. *Because it was raining.* is a fragment. "
                    "Join it to a main clause: *We stayed indoors because it was raining.* "
                    "Read your sentence and ask: does it make complete sense on its own?"),
            EX("Worked example 1: identify the clauses", intro="Identify the main clause and the subordinate clause: 'The students who passed the test celebrated.'", steps=[
                S("Find verbs", text="There are two verbs: passed and celebrated."),
                S("Which clause stands alone?", text="'The students celebrated' is the main clause."),
                S("Subordinate clause", text="'who passed the test' is a relative clause describing students."),
            ]),
            EX("Worked example 2: choosing the relative pronoun", intro="Complete: (a) The teacher ___ taught us Physics has left. (b) The mango tree, ___ is very old, gives plenty of fruit. (c) The girl ___ bag was stolen reported to the principal.", steps=[
                S("(a)", text="A person, subject: who."),
                S("(b)", text="A thing, with commas (non-defining): which."),
                S("(c)", text="Possession: whose."),
                S("Answer", text="(a) who (b) which (c) whose"),
            ]),
            EX("Worked example 3: combining sentences", intro="Join using a relative clause: 'Mr Ndi is a farmer. He lives near the river.'", steps=[
                S("Decide which sentence is extra information", text="'He lives near the river' describes Mr Ndi."),
                S("Replace he with who", text="who lives near the river"),
                S("Answer", text="Mr Ndi, who lives near the river, is a farmer. (or: Mr Ndi, a farmer, lives near the river.)"),
            ]),
            TIP("Exam link: clause and relative pronoun items appear in the grammar section of Paper 1 (multiple choice). "
                "In Paper 2, using subordinate clauses well makes your sentences varied and accurate, while fragments cost accuracy.",
                title="Where this appears in the exam"),
            QUIZ("Which sentence is correct?",
                 ["The man which sold me the phone is gone.", "The boy who he came late was punished.", "The girl whose mother is a nurse won the prize.", "My brother, that lives in Douala, is a driver."], 2,
                 "Whose shows possession and is correctly used. The other sentences use which for a person, a repeated pronoun, and that with commas.",
                 hint="Check the relative pronoun for people and the commas.",
                 feedback=["Use 'who' for a person.", "Do not repeat the subject: 'The boy who came late'.", "", "A non-defining clause with commas cannot use 'that': 'who lives in Douala'."]),
            QUIZ("Which of these is a sentence fragment?",
                 ["Although she was tired, she kept working.", "When the bell rang.", "The bell rang.", "She left because it was late."], 1,
                 "'When the bell rang' is a subordinate clause and cannot stand alone.",
                 hint="Does the group of words make complete sense alone?",
                 feedback=["It has a main clause: 'she kept working'.", "", "It is a complete main clause.", "It has a main clause: 'She left'."]),
            PQ("Underline the relative clause: 'The pupils who arrived late waited outside.'",
               "who arrived late. It describes the pupils."),
            PQ("Join with who or which: 'This is the doctor. He treated my mother.'",
               "This is the doctor who treated my mother."),
            PQ("Correct: 'The school where I studied there has closed.'",
               "The school where I studied has closed. Where already means 'in which', so 'there' is repeated."),
            SUM("A clause has a subject and a finite verb; a main clause stands alone, a subordinate clause does not.",
                "Subordinate clauses can be noun, adverb or relative (adjective) clauses.",
                "Use who/whom/whose for people, which for things, that for either in defining clauses.",
                "Non-defining relative clauses use commas and never that.",
                "Do not write fragments or repeat the subject after who, which and where."),
        ],
    ),
]

# ---------------------------------------------------------------------- 8b. Conditional clauses
LESSONS += [
    lesson(
        module=MODULE,
        topic="Clauses",
        title="Conditional clauses",
        slug="egr-conditional-clauses",
        minutes=22,
        summary="Conditional sentences state a condition and its result. The zero and first conditionals are real, the second imagines the present, and the third imagines the past. Match the tense in each clause.",
        objectives=[
            "Form the zero, first, second and third conditionals",
            "Use unless, provided that and as long as",
            "Avoid errors such as 'If I will go' and 'If I would have known'",
            "Choose the right conditional for a situation",
        ],
        key_concepts=["Conditional clause", "If-clause", "Zero conditional", "First conditional", "Second conditional", "Third conditional", "Unless"],
        blocks=[
            H("Introduction"),
            T("A student in Bamenda says, \"If I pass my GCE, I will study medicine.\" Her friend says, \"If I won a million francs, I would build a house.\" "
              "A teacher says, \"If you had studied, you would have passed.\" Each sentence has a condition (*if ...*) and a result. "
              "But the verb forms are different, because the three speakers think about different kinds of situation."),
            H("Conditional clauses"),
            D("A **conditional sentence** has an **if-clause** (the condition) and a **main clause** (the result). "
              "The verb forms in the two clauses must match the kind of situation.",
              title="Definition"),
            CODE("""Type     If-clause              Main clause           Meaning
Zero     if + present simple    present simple        facts that are always true
         If you heat water to 100 degrees Celsius, it boils.
First    if + present simple    will + base verb      real, possible future
         If it rains, the match will be cancelled.
Second   if + past simple       would + base verb     unreal or unlikely present/future
         If I won a million francs, I would build a house.
Third    if + past perfect      would have + past     impossible past
         participle
         If we had left earlier, we would have caught the bus.""", "text", title="The four conditionals"),
            T("In the **second conditional**, use *were* for all persons in careful writing: *If I were you, I would apologise.* *If she were here, she would help.* "
              "The result clause with *would* describes what we imagine. The third conditional talks about something that did not happen, so we cannot change it now."),
            T("**Unless** means *if ... not*: *Unless you study, you will fail* = *If you do not study, you will fail.* Do not add another negative after *unless*. "
              "Other linking words: *provided that*, *as long as* (condition: only if): *You may go provided that you return before dark.*"),
            T("When the if-clause comes first, use a comma. When it comes second, no comma is needed: *If it rains, we will stay.* *We will stay if it rains.*"),
            MISTAKE("Common error: 'If I will go' and 'If it will rain'",
                    "Never use *will* or *would* directly after *if* in these conditionals. Use the present simple in the if-clause of a first conditional: "
                    "*If I go, I will call you.* *If it rains, we will stay.*"),
            MISTAKE("Common error: 'If I would have known'",
                    "For the third conditional, the if-clause takes the past perfect: *If I had known, I would have come.* "
                    "Not *If I would have known*. The same pattern: *If she had worked harder, she would have passed.*"),
            MISTAKE("Common error: 'Unless you don't study'",
                    "*Unless* already contains the negative idea. Write *Unless you study, you will fail* "
                    "(or *If you do not study, you will fail*), not *Unless you don't study*."),
            EX("Worked example 1: which conditional?", intro="Choose the correct form: (a) If I (see) him tomorrow, I (tell) him. (b) If I (be) a bird, I (fly) to Mount Cameroon.", steps=[
                S("(a)", text="Tomorrow is a real possibility: first conditional. If + present simple, will + base verb."),
                S("(a) Answer", text="If I see him tomorrow, I will tell him."),
                S("(b)", text="Being a bird is impossible: second conditional. If + past simple (were), would + base verb."),
                S("(b) Answer", text="If I were a bird, I would fly to Mount Cameroon."),
            ]),
            EX("Worked example 2: third conditional", intro="Complete: 'If the driver (drive) more carefully, the accident (not happen).'", steps=[
                S("Decide", text="The accident already happened, so the condition is impossible: third conditional."),
                S("Pattern", text="if + past perfect, would have + past participle."),
                S("Answer", text="If the driver had driven more carefully, the accident would not have happened."),
            ]),
            EX("Worked example 3: rewrite with unless", intro="Rewrite with unless: 'If you do not pay the fees, you cannot sit the exam.'", steps=[
                S("Replace if...not", text="Unless means if...not, so remove the negative in the if-clause."),
                S("Answer", text="Unless you pay the fees, you cannot sit the exam."),
            ]),
            TIP("Exam link: conditional sentences appear in the grammar section of Paper 1 (multiple choice) and are useful in Paper 2 for arguments and advice. "
                "Decide first whether the situation is real, imaginary or past, then choose the pattern. "
                "In formal writing you may meet the inverted third conditional, *Had I known, I would have come*, which means the same as *If I had known, ...*.",
                title="Where this appears in the exam"),
            QUIZ("Choose the correct sentence.",
                 ["If I would have time, I will visit you.", "If I had time, I would visit you.", "If I will have time, I would visit you.", "If I have time, I would visit you."], 1,
                 "Second conditional: if + past simple, would + base verb.",
                 hint="Match the tense in the if-clause with the verb in the main clause.",
                 feedback=["Do not use would after if.", "", "Do not use will after if.", "The tenses do not match: 'If I have time, I will visit you' (first) or 'If I had time, I would visit you' (second)."]),
            QUIZ("Choose the correct completion: 'If she ___ harder, she would have passed.'",
                 ["worked", "had worked", "would work", "has worked"], 1,
                 "The third conditional uses the past perfect in the if-clause: had worked.",
                 hint="The result clause is would have passed. Which pattern is this?",
                 feedback=["Past simple is for the second conditional.", "", "Would does not follow if here.", "Present perfect does not match would have."]),
            PQ("Correct: 'If it will rain tomorrow, we will cancel the match.'",
               "If it rains tomorrow, we will cancel the match. The if-clause of a first conditional uses the present simple."),
            PQ("Complete: 'If I (be) the headmaster, I (build) a library.'",
               "If I were the headmaster, I would build a library. (Second conditional.)"),
            PQ("Rewrite with unless: 'If you do not hurry, you will miss the bus.'",
               "Unless you hurry, you will miss the bus."),
            SUM("Zero: if + present, present (facts). First: if + present, will + base (real future).",
                "Second: if + past, would + base (unreal present). Third: if + past perfect, would have + past participle (impossible past).",
                "Never put will or would directly after if in these patterns.",
                "Unless means if not; do not add another negative.",
                "Use a comma when the if-clause comes first."),
        ],
    ),
]

# ---------------------------------------------------------------------- 9. Question tags and phrasal verbs
LESSONS += [
    lesson(
        module=MODULE,
        topic="Question tags and phrasal verbs",
        title="Question tags and phrasal verbs",
        slug="egr-question-tags-phrasal-verbs",
        minutes=24,
        summary="A question tag is a short question added to a statement; it repeats the auxiliary verb with the opposite polarity. A phrasal verb is a verb plus a particle with a special meaning, such as give up or look after.",
        objectives=[
            "Form question tags correctly, including the special cases (I am, let's, nobody)",
            "Avoid the common error 'isn't it?' for every sentence",
            "Explain the meaning of common phrasal verbs",
            "Place the object correctly with separable and inseparable phrasal verbs",
        ],
        key_concepts=["Question tag", "Auxiliary verb", "Polarity", "Phrasal verb", "Particle", "Separable phrasal verb"],
        blocks=[
            H("Introduction"),
            T("A seller in Douala says to a customer, \"You will buy two, won't you?\" The little question *won't you?* invites the customer to agree. "
              "It is called a question tag. In the same market, another seller says, \"I can't put up with this heat.\" "
              "*Put up with* is a phrasal verb: three words that together mean 'tolerate'."),
            H("Question tags"),
            D("A **question tag** is a short question added to the end of a statement to ask for agreement or confirmation. "
              "A positive statement takes a negative tag; a negative statement takes a positive tag. "
              "The tag repeats the auxiliary of the statement and a pronoun for the subject.",
              title="Definition"),
            CODE("""Mama Ngo sells fish, doesn't she?          (positive + negative)
She does not live here, does she?         (negative + positive)
You are coming, aren't you?               (be)
They haven't paid, have they?             (have)
He can swim, can't he?                    (modal)
She will come, won't she?                 (will becomes won't)
You did your homework, didn't you?        (no auxiliary: use do/does/did)""", "text", title="Basic question tags"),
            T("If the statement has no auxiliary verb, use *do*, *does* or *did* in the tag, matching the tense of the verb."),
            KEY("Special cases", "These appear in exams.", cards=[
                ["I am", "aren't I? I am late, aren't I?"],
                ["Let's", "shall we? Let's go, shall we?"],
                ["Commands", "will you? Open the window, will you?"],
                ["There is / there are", "isn't there? / aren't there? There is a bus, isn't there?"],
                ["Everybody, someone, nobody", "Use they. Everybody is ready, aren't they? Nobody called, did they?"],
                ["Nothing, nobody, never, hardly", "These are negative in meaning, so the tag is positive: Nobody called, did they?"],
            ]),
            T("The tag is spoken with **falling intonation** when the speaker expects agreement, and with **rising intonation** when the speaker is not sure and really asks."),
            MISTAKE("Common error: 'isn't it?' for every sentence",
                    "Many speakers use *isn't it?* after any statement. In standard English the tag must match the auxiliary and the subject: "
                    "*You are coming, aren't you?* not *You are coming, isn't it?* *She sells fish, doesn't she?* not *She sells fish, isn't it?* "
                    "(*Isn't it?* is correct only when the statement has *it* as subject: *It is hot, isn't it?*)"),
            H("Phrasal verbs"),
            D("A **phrasal verb** is a verb combined with a particle (a preposition or adverb such as *up*, *off*, *after*, *out*). "
              "The combination has a meaning that is often different from the separate words.",
              title="Definition"),
            CODE("""give up          stop trying, stop a habit
look after       take care of
look for         search for
look up          find in a dictionary or list
put off          postpone
call off         cancel
turn down        refuse
set off          begin a journey
carry on         continue
break down       stop working (a machine or vehicle)
run out of       have none left
put up with      tolerate
get over         recover from
fill in          complete (a form)
find out         discover
bring up         raise (a child)""", "text", title="Common phrasal verbs"),
            T("Some phrasal verbs are **separable**: the object can go between the verb and the particle, or after the particle. "
              "*She turned down the offer.* *She turned the offer down.* But a pronoun object must come in the middle: *She turned it down* (not *turned down it*). "
              "Others are **inseparable**: *look after*, *look for*, *get over*, *put up with*. The object comes after the whole phrasal verb: *She looked after the baby.* *She looked after him.*"),
            MISTAKE("Common error: 'turn down it' and 'give up it'",
                    "With separable phrasal verbs, a pronoun goes between the verb and the particle: *turn it down*, *give it up*, *switch it off*, *call it off*."),
            EX("Worked example 1: forming tags", intro="Add a question tag: (a) Ngu plays football. (b) The pupils haven't arrived. (c) Let's go home. (d) Nobody knows the answer.", steps=[
                S("(a)", text="Positive statement, present simple, no auxiliary: doesn't he?"),
                S("(b)", text="Negative statement with have: have they?"),
                S("(c)", text="Let's takes shall we?"),
                S("(d)", text="Nobody is negative in meaning, so use a positive tag with they: do they?"),
                S("Answer", text="(a) Ngu plays football, doesn't he? (b) The pupils haven't arrived, have they? (c) Let's go home, shall we? (d) Nobody knows the answer, do they?"),
            ]),
            EX("Worked example 2: replacing with a phrasal verb", intro="Replace the underlined meaning with a phrasal verb: 'The match was cancelled because of the rain.'", steps=[
                S("Find the meaning", text="'Cancelled' means call off."),
                S("Passive form", text="The match was called off because of the rain."),
            ]),
            EX("Worked example 3: pronoun objects", intro="Rewrite using a pronoun: 'He turned down the job.'", steps=[
                S("Is the verb separable?", text="Yes, turn down is separable."),
                S("Place the pronoun in the middle", text="He turned it down."),
                S("Check", text="Not 'He turned down it'."),
            ]),
            TIP("Exam link: question tags and phrasal verbs appear in the grammar and vocabulary section of Paper 1 (multiple choice). "
                "Phrasal verbs also add natural expression to Paper 2 writing, but use them only when you are sure of their meaning and keep your tone suited to the task.",
                title="Where this appears in the exam"),
            QUIZ("Choose the correct tag: 'You have finished the exercise, ___?'",
                 ["isn't it", "haven't you", "don't you", "aren't you"], 1,
                 "The statement uses have, so the tag repeats have in the negative: haven't you?",
                 hint="Repeat the auxiliary from the statement.",
                 feedback=["Isn't it? is not matched to the subject you.", "", "Do is not used when the statement already has an auxiliary (have).", "Be does not match this statement."]),
            QUIZ("Which sentence is correct?",
                 ["She turned down it.", "She turned it down.", "She turned it down it.", "She turned down."], 1,
                 "A pronoun object of a separable phrasal verb goes in the middle.",
                 hint="Where does a pronoun go with a separable phrasal verb?",
                 feedback=["Not with a pronoun.", "", "The pronoun is repeated.", "The object is missing."]),
            PQ("Add a tag: 'Kum doesn't live in Bamenda, ___?'",
               "does he? A negative statement takes a positive tag."),
            PQ("Add a tag: 'I am the winner, ___?'",
               "aren't I? (This is the special form for I am.)"),
            PQ("Replace the words in brackets with a phrasal verb: 'The bus (began its journey) at six, but the engine (stopped working) near Kumba.'",
               "The bus set off at six, but the engine broke down near Kumba."),
            SUM("A question tag has opposite polarity: positive statement, negative tag, and the reverse.",
                "Repeat the auxiliary of the statement; if there is none, use do, does or did.",
                "Special cases: I am, aren't I; Let's, shall we; Nobody, do they.",
                "Do not use isn't it? for every sentence.",
                "A phrasal verb is a verb plus a particle with its own meaning (give up, look after, put off).",
                "With separable phrasal verbs a pronoun goes in the middle: turn it down."),
        ],
    ),
]

# ---------------------------------------------------------------------- 10. Punctuation and capitalization
LESSONS += [
    lesson(
        module=MODULE,
        topic="Punctuation and capitalization",
        title="Punctuation and capital letters",
        slug="egr-punctuation-capitals",
        minutes=24,
        summary="Capital letters begin sentences and mark proper nouns. Full stops, commas, apostrophes, colons, semicolons and inverted commas show how to read a sentence and prevent comma splices.",
        objectives=[
            "Use capital letters correctly for sentences, names, days, months and titles",
            "Use full stops, question marks and exclamation marks",
            "Use commas, semicolons and colons correctly and avoid the comma splice",
            "Use apostrophes for possession and contraction and punctuate direct speech",
        ],
        key_concepts=["Capital letter", "Full stop", "Comma", "Comma splice", "Semicolon", "Colon", "Apostrophe", "Inverted commas"],
        blocks=[
            H("Introduction"),
            T("Compare two sentences: *Let's eat Grandma.* and *Let's eat, Grandma.* "
              "One small comma changes the meaning completely. "
              "Punctuation is not decoration. It tells the reader where a sentence stops, which words belong together, and who is speaking."),
            H("Capital letters"),
            T("Use a capital letter for: the first word of a sentence; the pronoun **I**; the names of people and places (Ama, Limbe, Mount Cameroon); "
              "days and months (Monday, February); languages and nationalities (English, French, Cameroonian); "
              "titles before names (Mr Ndi, Dr Fon, Madam Ngo); and the main words in the title of a book (*Things Fall Apart*)."),
            T("Do not use capitals for seasons (*the dry season*), for ordinary job titles used alone (*the teacher*, *the doctor*), or for directions (*north*, *south*) "
              "unless they are part of a name (*the Far North Region*)."),
            H("End marks"),
            T("A **full stop** ends a statement. A **question mark** ends a direct question: *Where is the market?* "
              "An **exclamation mark** shows strong feeling: *Stop!* Do not use a question mark for a reported question: *She asked where the market was.*"),
            H("The comma"),
            KEY("Main uses of the comma", "Learn these four.", cards=[
                ["Lists", "Separate items: We bought rice, beans, plantains and fish. (No comma before the final 'and' is usual in British English.)"],
                ["After an introductory word or clause", "However, he stayed. When the bell rang, we left."],
                ["Around extra information", "My uncle, who lives in Buea, is a doctor."],
                ["Before and, but, so joining main clauses", "It was raining, but we went to the market."],
            ]),
            MISTAKE("Common error: the comma splice",
                    "A **comma splice** joins two complete sentences with only a comma: *I was tired, I went to bed.* "
                    "Fix it by using a full stop (*I was tired. I went to bed.*), a semicolon (*I was tired; I went to bed.*), or a conjunction (*I was tired, so I went to bed.*)."),
            H("Semicolon and colon"),
            T("A **semicolon** joins two closely related main clauses: *The market was crowded; we bought quickly.* "
              "A **colon** introduces a list or an explanation after a complete clause: *Bring these items: a pen, a ruler and a calculator.* "
              "Do not put a colon straight after a verb or preposition: not *We bought: rice and beans.*"),
            H("Apostrophe"),
            T("The apostrophe has two jobs. It shows **possession**: *Ama's book* (one owner), *the girls' school* (more than one owner), *the children's books* (an irregular plural). "
              "It also shows **missing letters** in contractions: *don't* (do not), *it's* (it is or it has), *they're* (they are)."),
            CODE("""its      belongs to it:    The dog wagged its tail.
it's     it is / it has:   It's raining.
your     belongs to you:   Is this your bag?
you're   you are:          You're welcome.
their    belongs to them:  Their school is new.
they're  they are:         They're late.
whose    belongs to whom:  Whose phone is this?
who's    who is / who has: Who's calling?""", "text", title="Look-alike words"),
            MISTAKE("Common error: apostrophe in plurals and the wrong place",
                    "Do not add an apostrophe to a simple plural: write *tomatoes*, not *tomato's*. "
                    "The apostrophe shows possession or missing letters only. "
                    "Check the owner: *the student's book* (one student) but *the students' books* (many students)."),
            H("Direct speech"),
            T("Put the exact words in inverted commas (quotation marks) and begin each new speaker on a new line. "
              "The comma or end mark goes inside the closing inverted comma. British English may use single or double inverted commas; choose one and stay consistent."),
            CODE("""\"I am going to the market,\" said Ama.
Ngu asked, \"Can I come with you?\"
\"Yes,\" she replied. \"Hurry up!\"""", "text", title="Punctuating direct speech"),
            EX("Worked example 1: capitals", intro="Correct: 'on monday the english teacher from limbe visited mr ndi in the north west region.'", steps=[
                S("Sentence start", text="On."),
                S("Days, languages, places and titles", text="Monday, English, Limbe, Mr Ndi, North West Region."),
                S("Answer", text="On Monday the English teacher from Limbe visited Mr Ndi in the North West Region. (The word 'teacher' is not capitalised.)"),
            ]),
            EX("Worked example 2: fixing a comma splice", intro="Correct in two ways: 'The road was blocked, we took a different route.'", steps=[
                S("Recognise the problem", text="Two complete sentences are joined by a comma."),
                S("Option 1", text="The road was blocked; we took a different route."),
                S("Option 2", text="The road was blocked, so we took a different route."),
            ]),
            EX("Worked example 3: punctuating speech", intro="Punctuate: where are you going asked the driver", steps=[
                S("Mark the speech", text="The words spoken are 'where are you going'."),
                S("Capital and question mark", text="Start the speech with a capital, and use a question mark inside the closing inverted comma."),
                S("Answer", text="\"Where are you going?\" asked the driver."),
            ]),
            TIP("Exam link: punctuation and capital letter items appear in the grammar section of Paper 1 (multiple choice), and accuracy of punctuation matters in every piece of writing in Paper 2. "
                "The Board's report asks for continuous prose and correct paragraphs, so check each sentence for a capital letter and a full stop.",
                title="Where this appears in the exam"),
            QUIZ("Which sentence is correctly punctuated?",
                 ["The childrens books are on the table.", "The children's books are on the table.", "The childrens' books are on the table.", "The children books' are on the table."], 1,
                 "Children is an irregular plural, so possession is shown by 's: children's.",
                 hint="Is children already plural?",
                 feedback=["The apostrophe is missing.", "", "Children is already plural, so the apostrophe goes before the s.", "The apostrophe is in the wrong place."]),
            QUIZ("Which sentence has no punctuation error?",
                 ["Its raining, we will stay at home.", "It's raining, so we will stay at home.", "It's raining we will stay at home.", "Its' raining; so we will stay at home."], 1,
                 "It's = it is, and a conjunction (so) correctly joins the clauses after the comma.",
                 hint="Check its and it's and the join between the clauses.",
                 feedback=["It's needs the apostrophe, and the comma splice remains.", "", "Two clauses are joined without any punctuation or conjunction.", "Its' is never correct, and a semicolon is not followed by so."]),
            PQ("Correct the capitals: 'we visited mount cameroon in december with our english teacher.'",
               "We visited Mount Cameroon in December with our English teacher."),
            PQ("Correct the comma splice in two ways: 'Ama was late, she missed the bus.'",
               "Ama was late; she missed the bus. (or) Ama was late, so she missed the bus. (or) Ama was late. She missed the bus."),
            PQ("Punctuate: 'the teacher said the pupils must bring their books tomorrow' (as direct speech with the teacher speaking).",
               "The teacher said, \"The pupils must bring their books tomorrow.\" (or: \"The pupils must bring their books tomorrow,\" said the teacher.)"),
            SUM("Capital letters are used for sentence beginnings, I, names, days, months, languages and titles.",
                "A comma separates items, introduces clauses and surrounds extra information; it cannot join two sentences (comma splice).",
                "A semicolon joins related sentences; a colon introduces a list after a complete clause.",
                "Apostrophes show possession (Ama's, the girls', children's) and contractions (don't, it's), never plurals.",
                "In direct speech, put the spoken words in inverted commas with the punctuation inside."),
        ],
    ),
]
