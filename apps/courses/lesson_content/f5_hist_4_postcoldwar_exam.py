"""Form 5 History (O Level 0560): Post-Cold War world, and the Examination module (Paper 1 and Paper 2).

Draft content. History facts come from the course lessons and from well-established general
knowledge; a reviewer must check them against the syllabus and standard textbooks. The only exam
facts stated are from the syllabus outline: Paper 1 is multiple choice and Paper 2 is structured
essays. Students are sent to the current GCE Board instructions for everything else.
"""

from .dsl import *  # noqa: F403

COURSE = ("history", "form-5")

M_WORLD = "World History since 1870"
M_EXAM = "Examination"

LESSONS = [
    # ------------------------------------------------------------------ 1. Changing world order
    lesson(
        module=M_WORLD, topic="Post-Cold War world",
        title="A changing world order after 1991",
        slug="history-post-cold-war-changing-world-order",
        minutes=20,
        summary="How the world changed after the USSR dissolved in December 1991: one superpower, new powers and "
                "blocs, the role of the United Nations, and what these changes meant for Africa.",
        objectives=[
            "Explain what unipolar and multipolar mean and why 1991 is a turning point",
            "Describe new powers and blocs that appeared after the Cold War",
            "Describe the role of the United Nations after 1991 in general terms",
            "Explain how the end of the Cold War affected Africa, including Cameroon",
        ],
        key_concepts=["Unipolar world", "Multipolar world", "Globalisation", "Gulf War 1991", "Democratisation", "African Union"],
        blocks=[
            H("Introduction"),
            T("In December 1991 the Soviet Union was dissolved. For more than forty years the world had been shaped by "
              "the rivalry of two superpowers, the USA and the USSR. Now one of them had gone.\n\n"
              "A student in Buea today lives in the world that followed: goods and news that travel across the world "
              "in seconds, many political parties, and organisations that join neighbouring countries together. "
              "This lesson explains the main features of that new world order and what they meant for Africa."),
            D("A **unipolar** world has one dominant power. A **multipolar** world has several powers of "
              "comparable influence. During the Cold War the world was **bipolar**, with two superpowers.",
              title="Unipolar and multipolar"),
            D("**Globalisation** is the growth of trade, travel, communication and investment across the whole world, "
              "so that countries depend on one another more and more.", title="Globalisation"),
            H("1991 and the unipolar moment"),
            T("The Cold War ended in two steps. In 1989 communist governments fell in Eastern Europe and the Berlin Wall "
              "was opened on 9 November. In December 1991 the USSR itself was dissolved. Students often mix the two: "
              "1989 freed Eastern Europe, 1991 ended the Soviet state.\n\n"
              "With the USSR gone, the USA was the only superpower. Many people described the early 1990s as a "
              "**unipolar** moment.\n\n"
              "The Gulf War of 1991 showed the new situation. A coalition led by the USA, with the authority of the "
              "United Nations, drove Iraq out of Kuwait.\n\n"
              "During the Cold War the USA and the USSR often disagreed about such actions. After 1991 it was "
              "easier for the main powers to act together, and the USA could lead a large coalition."),
            H("New powers and blocs"),
            T("The unipolar moment did not last unchanged. Other powers and groups grew in strength. "
              "The economy of **China** grew rapidly. The **European Union** grew and became an important economic bloc. "
              "In Africa, the **African Union (AU)** replaced the OAU in 2002. Because of these changes, many people now "
              "speak of a **multipolar** world.\n\n"
              "Historians do not agree on how unipolar the world really was, or for how long. Some stress the "
              "military strength of the USA. Others point to the growth of China and of regional blocs. A good "
              "answer gives both views."),
            H("The United Nations after 1991"),
            T("The **United Nations (UN)** is an organisation of states, founded in 1945. What it can do depends on what its "
              "member states agree to do.\n\n"
              "After 1991 the UN was in the spotlight. Supporters point to cases such as the Gulf War, where the UN "
              "authorised action by a coalition. Critics say the world, including the UN, was too slow to respond "
              "to some conflicts of the 1990s, such as the ethnic wars in Rwanda and in the former Yugoslavia. "
              "Both opinions are part of the story."),
            H("Effects on Africa"),
            T("The end of the Cold War changed Africa in several ways.\n\n"
              "**Less superpower rivalry.** During the Cold War the superpowers had supported rival sides in "
              "African conflicts, as in Angola. After 1991 this kind of competition was no longer the main force.\n\n"
              "**Democratisation.** In the early 1990s one-party states, including many in Africa, moved towards "
              "multiparty politics. In Cameroon the SDF was launched on 26 May 1990 and the liberty laws of "
              "December 1990 allowed political parties. Donor countries also linked aid to democratic reform.\n\n"
              "**New conflicts.** Ethnic wars, such as the one in Rwanda, showed that the end of the Cold War did not "
              "bring peace everywhere.\n\n"
              "**New cooperation.** The African Union, launched in Durban on 9 July 2002, was meant to be stronger than "
              "the OAU. Globalisation also brought African countries closer to world trade and communication, "
              "with both opportunities and difficulties."),
            KEY("Causes and effects at a glance", "Use these as paragraph points in essays.", cards=[
                ["Cause", "The collapse of the USSR in December 1991 left the USA as the only superpower."],
                ["Effects", "US leadership in the Gulf War; globalisation; multiparty politics in Africa; new "
                            "conflicts and terrorism; the rise of China and of regional blocs."],
            ], note="Historians disagree about how long the unipolar moment lasted. Show that you know there is more than one view."),
            EX("Model answer plan 1", intro="Explain how the end of the Cold War affected Africa.", steps=[
                S("Introduction", text="Say that the Cold War ended with the collapse of the USSR in December 1991, and that the change affected both politics and conflicts in Africa."),
                S("Less superpower rivalry", text="The USA and USSR had backed rival sides in conflicts such as Angola. After 1991 this competition was no longer the main force."),
                S("Democratisation", text="One-party states moved to multiparty politics. In Cameroon: the SDF launch (26 May 1990) and the liberty laws (December 1990)."),
                S("Outside pressure", text="Donor countries linked aid to democratic reform, which pushed governments to accept change."),
                S("New conflicts", text="Ethnic wars such as Rwanda showed that peace did not follow automatically."),
                S("New cooperation", text="The AU replaced the OAU in 2002; globalisation increased trade and communication."),
                S("Conclusion", text="The effects were mixed: new political freedoms and new organisations, but also new conflicts and slow reform."),
            ]),
            EX("Model answer plan 2", intro="To what extent was the world after 1991 dominated by one superpower?", steps=[
                S("Introduction", text="Define unipolar. State that after December 1991 the USA was the only superpower, and say you will weigh this against other powers."),
                S("For: US strength", text="The USA led the coalition in the Gulf War of 1991, with the authority of the UN."),
                S("For: no rival bloc", text="The Warsaw Pact had gone and the USSR no longer existed to oppose the USA."),
                S("Against: new powers", text="The economic rise of China and the growth of the European Union."),
                S("Against: new threats and blocs", text="The attacks of 11 September 2001 and the war on terror, and regional groups such as the AU."),
                S("Conclusion", text="Give a judgement: the USA was dominant in the early 1990s, but the world became more multipolar over time. Mention that historians differ."),
            ]),
            H("Common mistakes"),
            MISTAKE("Saying the Cold War ended only in 1989",
                    "1989 saw the fall of communist governments in Eastern Europe and the opening of the Berlin Wall. "
                    "The USSR was dissolved in December 1991."),
            MISTAKE("Thinking unipolar means the USA controlled everything",
                    "Unipolar means one dominant power. Other states and groups still acted independently, and over time China, "
                    "the EU and the AU gained importance."),
            MISTAKE("Listing features without explaining them",
                    "Writing 'globalisation, terrorism, China' earns little. For each feature say what it was and what it changed."),
            QUIZ("Which event is the best example of a US-led action with UN authority in 1991?",
                 ["The Cuban Missile Crisis", "The Berlin Airlift", "The Gulf War", "The Suez Crisis"], 2,
                 "In 1991 a US-led coalition, authorised by the UN, drove Iraq out of Kuwait.",
                 hint="Think about 1991 and the country of Kuwait.",
                 feedback=["That was in 1962 during the Cold War.", "That was in 1948-1949 during the Cold War.", "",
                           "That was in 1956 and involved Israel, Britain and France attacking Egypt."]),
            QUIZ("Which statement about Africa after the Cold War is best supported by the lesson?",
                 ["Every African country became peaceful.", "Many one-party states moved towards multiparty politics.",
                  "Africa no longer had any regional organisation.", "The OAU was founded in 1991."], 1,
                 "In the early 1990s many one-party states, including Cameroon, allowed multiparty politics.",
                 hint="Remember the liberty laws of December 1990 in Cameroon.",
                 feedback=["Ethnic wars such as Rwanda show this is false.", "",
                           "The African Union replaced the OAU in 2002.", "The OAU was founded in 1963."]),
            H("Practice questions"),
            PQ("Explain the difference between a unipolar and a multipolar world.",
               "A unipolar world has one dominant power; a multipolar world has several powers of comparable influence. "
               "After December 1991 the USA was the only superpower, but the rise of China and of blocs such as the EU "
               "and the AU led many people to speak of a multipolar world."),
            PQ("What happened in the Gulf War of 1991?",
               "A coalition led by the USA, with the authority of the United Nations, drove Iraq out of Kuwait."),
            PQ("Give two ways in which the end of the Cold War affected Cameroon.",
               "It added to pressure for democratic reform: the SDF was launched on 26 May 1990 and the liberty laws of "
               "December 1990 allowed political parties. Donor countries also linked aid to democratic reform."),
            PQ("State two different views about the UN's record after 1991.",
               "Supporters point to cases such as the Gulf War, where the UN authorised action. Critics say the world, "
               "including the UN, was too slow to respond to some conflicts, such as Rwanda and the former Yugoslavia."),
            SUM("The USSR was dissolved in December 1991; the Berlin Wall opened in 1989. Do not mix the two.",
                "The USA became the only superpower: a unipolar moment shown by the Gulf War of 1991.",
                "China's growth, the EU and the AU point to a multipolar world, and historians differ on how unipolar the world was.",
                "The UN had a larger role, and its record is judged differently by supporters and critics.",
                "In Africa the end of the Cold War brought multiparty politics, new conflicts and the African Union (2002)."),
        ],
    ),
    # ------------------------------------------------------------------ 2. Arab-Israeli conflict
    lesson(
        module=M_WORLD, topic="Post-Cold War world",
        title="The Arab-Israeli conflict: origins, wars and peace efforts",
        slug="history-arab-israeli-conflict-origins-wars-peace",
        minutes=22,
        summary="The origins of the Arab-Israeli conflict, the wars from 1948 to 1973, and the peace agreements of Camp David, "
                "Oslo and the Israel-Jordan treaty, presented from both sides.",
        objectives=[
            "Explain the origins of the conflict, from the Balfour Declaration to the 1947 partition plan",
            "Describe Israel's declaration of independence in 1948 and the main later wars",
            "Describe the Camp David Accords, the Oslo Accords and the Israel-Jordan treaty",
            "Present the Israeli and Palestinian views of events fairly",
        ],
        key_concepts=["Zionism", "Mandate", "Partition", "Refugees", "Intifada", "Peace process"],
        blocks=[
            H("Introduction"),
            T("The Arab-Israeli conflict is one of the longest conflicts of the modern world. It is about land, security, "
              "refugees and national identity for two peoples, Israelis and Palestinians. It has also drawn in neighbouring states.\n\n"
              "This is a sensitive subject. In an examination you must explain what happened and show how each side "
              "sees events. Do not take a side."),
            D("**Zionism** is the movement, begun in the late nineteenth century, for a Jewish national homeland in Palestine.",
              title="Zionism"),
            D("A **mandate** was territory that the League of Nations placed under the control of a European power after the "
              "First World War. Britain held the mandate for Palestine.", title="Mandate"),
            D("An **intifada** (Arabic for uprising or shaking off) is a Palestinian popular uprising against Israeli occupation. "
              "The first began in 1987 and the second in 2000.", title="Intifada"),
            H("Origins: the mandate and the partition plan"),
            T("After the First World War, Britain governed Palestine under a League of Nations mandate. In the **Balfour "
              "Declaration** (1917) Britain supported a national home for the Jewish people in Palestine, while also "
              "promising to respect the rights of the existing non-Jewish communities. Jewish immigration grew, and so did conflict with the Arab population.\n\n"
              "After the Holocaust, pressure for a Jewish state increased. In November 1947 the UN voted to partition Palestine into "
              "a Jewish state and an Arab state. Jewish leaders accepted the plan. Arab leaders rejected it."),
            H("1948 and the wars that followed"),
            T("Israel declared independence on 14 May 1948. Neighbouring Arab states attacked, and Israel won the war of 1948-1949. "
              "Hundreds of thousands of Palestinians fled or were expelled. This created a refugee problem that has never been "
              "fully resolved.\n\n"
              "In the **Suez Crisis** (1956) Israel, Britain and France attacked Egypt after Nasser nationalised the Suez Canal. "
              "Pressure from the USA and the USSR forced them to withdraw.\n\n"
              "In the **Six-Day War** (June 1967) Israel defeated Egypt, Jordan and Syria. It occupied the Sinai, Gaza, the West Bank, "
              "East Jerusalem and the Golan Heights.\n\n"
              "In the **Yom Kippur War** (October 1973) Egypt and Syria attacked Israel. Arab oil producers then raised prices and "
              "cut supplies to countries that supported Israel."),
            KEY("Two ways of seeing 1948", "A good answer presents both fairly.", cards=[
                ["The Israeli view", "Independence was the creation of a safe homeland for a people who had suffered persecution, "
                                     "and Israel had to defend itself when neighbouring states attacked in 1948."],
                ["The Palestinian view", "The same events meant the loss of homes and land and the start of the refugee problem. "
                                         "Palestinians call 1948 the Nakba, an Arabic word meaning catastrophe."],
            ], note="Neither account is complete alone. Examiners reward answers that describe both and avoid emotional or one-sided words."),
            IMG("f5h-arab-israeli-timeline.svg",
                alt="Vertical timeline: 1917 Balfour Declaration, November 1947 UN partition plan, 14 May 1948 Israel declares "
                    "independence, 1956 Suez Crisis, June 1967 Six-Day War, October 1973 Yom Kippur War, 1978-79 Camp David and "
                    "the Egypt-Israel treaty, 1993 Oslo Accords, 1994 Israel-Jordan peace treaty.",
                caption="Figure 1. Key dates of the conflict. Peace agreements are in blue."),
            H("The search for peace"),
            T("Through the **Camp David Accords** (1978), mediated by US President Carter, Egypt and Israel agreed to make peace. "
              "Their peace treaty of 1979 returned Sinai to Egypt. Egypt's President Sadat was assassinated in 1981.\n\n"
              "In the **Oslo Accords** (1993) Israel and the Palestine Liberation Organization (PLO) recognised each other, and a "
              "Palestinian Authority was created with limited self-rule. Jordan signed a peace treaty with Israel in 1994."),
            T("Key issues remained unsolved: borders, Jewish settlements in occupied territory, the status of Jerusalem, the return "
              "of refugees, and security. The Second Intifada (2000) and later wars in Gaza showed that the conflict continued.\n\n"
              "Israelis stress the need for security and for recognition of Israel. Palestinians stress an end to occupation, "
              "self-determination and the refugees. Both concerns appear in any serious discussion of peace."),
            EX("Model answer plan 1", intro="Explain the causes of the Arab-Israeli war of 1948-1949.", steps=[
                S("Introduction", text="Say that Israel declared independence on 14 May 1948 and that neighbouring Arab states attacked."),
                S("Competing claims", text="Zionists and Palestinian Arabs both claimed the same land."),
                S("British policy", text="The Balfour Declaration (1917) supported a Jewish national home while promising to respect existing communities; immigration grew and conflict grew with it."),
                S("Effect of the Holocaust", text="It increased international support for a Jewish state."),
                S("UN partition plan, November 1947", text="Jewish leaders accepted it; Arab leaders rejected it; tension rose."),
                S("Conclusion", text="Several causes combined. Add that Israelis and Palestinians describe the events differently."),
            ]),
            EX("Model answer plan 2", intro="(a) What was agreed at Camp David? (b) What happened later in the search for peace?", steps=[
                S("(a) Parties and mediator", text="Egypt and Israel, with US President Carter as mediator, in 1978."),
                S("(a) Result", text="A peace treaty followed in 1979 and Israel returned Sinai to Egypt. Sadat was assassinated in 1981."),
                S("(b) Oslo, 1993", text="Israel and the PLO recognised each other; a Palestinian Authority with limited self-rule was created."),
                S("(b) Jordan, 1994", text="Jordan signed a peace treaty with Israel."),
                S("(b) Unsolved issues", text="Borders, settlements, Jerusalem, refugees and security remained; the Second Intifada began in 2000."),
            ]),
            H("Common mistakes"),
            MISTAKE("Mixing up the 1967 and 1973 wars",
                    "1967: the Six-Day War, in which Israel occupied large territories. 1973: the Yom Kippur War, started by Egypt and Syria, followed by the oil price rise."),
            MISTAKE("Confusing Camp David and Oslo",
                    "Camp David (1978): Egypt and Israel. Oslo (1993): Israel and the PLO. Jordan made its own treaty in 1994."),
            MISTAKE("Writing from one side only",
                    "Using words that blame one side, or leaving out the other side's concerns, loses marks. Describe both views in neutral language."),
            QUIZ("Which agreement was signed between Egypt and Israel?",
                 ["The Oslo Accords", "The Camp David Accords and the treaty of 1979", "The Balfour Declaration", "The UN partition plan"], 1,
                 "Camp David (1978) led to the Egypt-Israel peace treaty of 1979.",
                 hint="Think of the US President who mediated.",
                 feedback=["Oslo involved Israel and the PLO.", "",
                           "The Balfour Declaration (1917) was a British statement.", "The UN plan of 1947 proposed two states."]),
            QUIZ("Why do historians present both an Israeli and a Palestinian view of 1948?",
                 ["Because the two peoples describe the same events very differently", "Because nothing happened in 1948",
                  "Because only one side kept records", "Because the UN banned discussing it"], 0,
                 "Israelis speak of independence; Palestinians speak of the Nakba. A balanced answer explains both.",
                 hint="Think about independence for one people and displacement for the other.",
                 feedback=["", "Israel was declared on 14 May 1948 and a war followed.", "This is not the reason given in the lesson.",
                           "No such ban exists."]),
            H("Practice questions"),
            PQ("State two things the Balfour Declaration (1917) said.",
               "Britain supported a national home for the Jewish people in Palestine, and promised to respect the rights of the existing non-Jewish communities."),
            PQ("Name three territories occupied by Israel in the Six-Day War of 1967.",
               "Any three of: the Sinai, Gaza, the West Bank, East Jerusalem, the Golan Heights."),
            PQ("State two results of the Camp David Accords.",
               "Egypt and Israel made peace; their treaty of 1979 returned Sinai to Egypt."),
            PQ("Give one difference between the Oslo Accords (1993) and the Camp David Accords (1978).",
               "Camp David was between Egypt and Israel and led to a peace treaty; Oslo was between Israel and the PLO and led to mutual recognition and a Palestinian Authority with limited self-rule."),
            SUM("Britain held the mandate; the Balfour Declaration (1917) and the UN partition plan (November 1947) led to 1948.",
                "Israel declared independence on 14 May 1948; wars followed in 1948-1949, 1956, 1967 and 1973.",
                "Camp David (1978) brought peace with Egypt; Oslo (1993) brought Israel-PLO recognition; Jordan signed in 1994.",
                "Borders, settlements, Jerusalem, refugees and security remained unsolved.",
                "Israelis and Palestinians describe 1948 differently: present both views without taking a side."),
        ],
    ),
    # ------------------------------------------------------------------ 3. Paper 1
    lesson(
        module=M_EXAM, topic="Paper 1",
        title="Paper 1: multiple-choice strategies for History",
        slug="history-paper-1-multiple-choice-strategies",
        minutes=22,
        summary="How to approach a multiple-choice History paper: plan your time, work in two passes, eliminate options, and avoid "
                "traps built from similar dates, party names and organisations.",
        objectives=[
            "Say what the syllabus tells us about Paper 1 and where to check the details",
            "Plan time with a two-pass method",
            "Eliminate wrong options using what you know about dates, people and periods",
            "Avoid traps from similar dates, similar party names and similar organisations",
        ],
        key_concepts=["Paper 1", "Multiple choice", "Two-pass method", "Elimination", "Distractor", "Similar dates"],
        blocks=[
            H("Introduction"),
            T("Paper 1 asks you to recognise the correct fact among several choices. It covers the whole course: Cameroon "
              "from 1945, and world history since 1870. A question may take you from a village in the Bamenda grassland in "
              "1961 to a crisis in Cuba in 1962 within a few lines, so you need a calm method as well as good knowledge."),
            D("The course outline says that Paper 1 is **multiple choice**. The outline does not state how long the paper is, "
              "how many questions it has, or how many marks it carries.",
              title="Paper 1 at a glance",
              note="Check the current GCE Board instructions and ask your teacher for the exact time, number of questions and "
                   "rules about marking. The mock exams on KKEVO use practice settings of our own."),
            KEY("A simple plan for the time", "Work out your own time per question from the real paper.", cards=[
                ["Time per question", "Divide the time you are given by the number of questions. In the KKEVO mock A there are 40 questions "
                                      "in 60 minutes, which gives 1.5 minutes each. These are KKEVO practice settings, not the official ones."],
                ["First pass", "Go through the paper once. Answer every question you can do quickly and mark the others."],
                ["Second pass", "Return to the marked questions with the time you saved. Make sure every question has an answer, "
                                "unless the official instructions say that wrong answers lose marks."],
            ]),
            T("In a multiple-choice question there is one correct option and several **distractors**. A distractor is a wrong "
              "option that looks reasonable, usually because it is a real fact that belongs to a different date, person or event.\n\n"
              "Do not search for the right answer first. Cross out the options that you know are wrong, then look at what is left. "
              "Each wrong option you remove improves your chance. Read the question twice, because one small word such as NOT, "
              "FIRST or ONLY can change the whole question."),
            EX("Worked example 1: eliminate by date", intro=(
                "In which year did the CNU become the CPDM at a congress in Bamenda? A: 1966. B: 1972. C: 1985. D: 1990."), steps=[
                S("Link each option to an event", text="1966: the CNU was formed. 1972: the referendum that created the unitary state. 1990: the SDF launch and the liberty laws."),
                S("Cross out", text="A, B and D are real dates but for different events, so they are distractors."),
                S("Check what remains", text="C, 1985, is the year the CNU became the CPDM at a congress in Bamenda."),
                S("Answer", text="**C**."),
            ]),
            H("Traps with similar dates, names and organisations"),
            T("History papers often place look-alike items side by side. Learn the pairs that are most often confused.\n\n"
              "**Similar dates.** 1 January 1959 (full internal autonomy) and 1 January 1960 (independence); 11 February 1961 "
              "(plebiscite), July 1961 (Foumban) and 1 October 1961 (reunification); 1989 (Berlin Wall) and 1991 (USSR dissolved)."),
            IMG("f5h-cameroon-dates-timeline.svg",
                alt="Vertical timeline of seven Cameroon dates: 1 January 1959 internal autonomy, 1 January 1960 independence, "
                    "11 February 1961 plebiscites, July 1961 Foumban Conference, 1 October 1961 reunification, 1 September 1966 "
                    "CNU formed, 20 May 1972 referendum.",
                caption="Figure 1. Cameroon dates that are easy to mix up."),
            T("**Similar party names.** KNC (Endeley) and KNDP (Foncha); UPC (Um Nyobè) and UC (Ahidjo's Union Camerounaise); "
              "CNU (1966) and CPDM (1985); OK (One Kamerun).\n\n"
              "**Similar organisations.** OAU (Addis Ababa, 25 May 1963) and AU (Durban, 9 July 2002); NATO (1949) and the Warsaw Pact "
              "(1955); the Camp David Accords (Egypt and Israel) and the Oslo Accords (Israel and the PLO)."),
            EX("Worked example 2: similar party names", intro=(
                "Which party was founded in 1955 by John Ngu Foncha after he left the KNC? A: KNC. B: KNDP. C: OK. D: CNU."), steps=[
                S("Underline the clues", text="'Founded in 1955', 'Foncha' and 'after he left the KNC'."),
                S("Eliminate", text="A: the KNC was the party he left. C: OK was founded by Ntumazah in 1957. D: the CNU was formed in 1966."),
                S("Answer", text="**B**, the KNDP."),
            ]),
            EX("Worked example 3: similar organisations", intro=(
                "Which organisation was founded in Addis Ababa on 25 May 1963? A: The AU. B: The OAU. C: NATO. D: The Warsaw Pact."), steps=[
                S("Use the place and date", text="The AU was launched in Durban on 9 July 2002, so A is wrong."),
                S("Eliminate the Cold War alliances", text="NATO was formed in 1949 and the Warsaw Pact in 1955."),
                S("Answer", text="**B**, the OAU."),
            ]),
            EX("Worked example 4: a NOT question", intro=(
                "Which of these was NOT a method used by the USA to contain communism? A: The Marshall Plan. B: The Truman Doctrine. "
                "C: The Warsaw Pact. D: The Berlin airlift."), steps=[
                S("Rewrite the question", text="Three options are US methods. One is not. Find the odd one out."),
                S("Test each", text="The Truman Doctrine and Marshall Plan (1947) and the Berlin airlift (1948-1949) were US responses. The Warsaw Pact was an alliance formed by the USSR and its allies in 1955."),
                S("Answer", text="**C**."),
            ]),
            EX("Worked example 5: similar agreements", intro=(
                "The Oslo Accords of 1993 were signed between which two parties? A: Egypt and Israel. B: Israel and the PLO. "
                "C: Jordan and Israel. D: Britain and Egypt."), steps=[
                S("Recall the pair of agreements", text="Camp David (1978) was Egypt and Israel. Jordan signed its own treaty with Israel in 1994."),
                S("Eliminate", text="A, C and D are linked to other events."),
                S("Answer", text="**B**: at Oslo, Israel and the PLO recognised each other."),
            ]),
            TIP("Read all four options before you choose. A familiar option at A is not always the best one. Beware of words "
                "such as always, never and only: they are rarely true in History. Also check the exact wording about contested "
                "topics: the correct option is the one that matches the facts, not the one that matches an opinion."),
            H("Common mistakes"),
            MISTAKE("Choosing the first familiar fact",
                    "Distractors are real facts from the course. Check that the fact answers THIS question, with this date and these people."),
            MISTAKE("Missing the word NOT",
                    "Underline NOT, EXCEPT, FIRST and ONLY when you read the question, then reread the options with that word in mind."),
            MISTAKE("Leaving gaps or running out of time",
                    "Do not spend too long on one question. Mark it, move on, and come back on the second pass."),
            QUIZ("What is a 'distractor' in a multiple-choice question?",
                 ["The correct answer", "A wrong option that looks reasonable", "A hint written by the examiner", "The question number"], 1,
                 "A distractor is a wrong option that looks reasonable, often a true fact belonging to another date or event.",
                 hint="Think of its name: it distracts you from the right answer.",
                 feedback=["The correct option is the key answer, not a distractor.", "", "Hints are not part of the question.", "It has nothing to do with numbering."]),
            QUIZ("Which pair of dates is easiest to mix up, according to this lesson?",
                 ["1 January 1959 and 1 January 1960", "1945 and 2002", "1963 and 1991", "1917 and 1996"], 0,
                 "1959 was full internal autonomy and 1960 was independence: both on 1 January, one year apart.",
                 hint="Look for two dates that share the same day and month.",
                 feedback=["", "These are far apart.", "These belong to different, unrelated events.", "These belong to different, unrelated events."]),
            H("Practice questions"),
            PQ("Which date is the date of reunification of Southern Cameroons and Cameroun? A: 11 February 1961. B: 1 June 1961. "
               "C: 1 October 1961. D: 20 May 1972.",
               "**C**. Reunification was on 1 October 1961. A is the plebiscite, B is the date northern Cameroons joined Nigeria, "
               "and D is the 1972 referendum."),
            PQ("Who led the Union Camerounaise? A: Um Nyobè. B: Ahmadou Ahidjo. C: Foncha. D: Endeley.",
               "**B**. Ahidjo led the Union Camerounaise. Um Nyobè led the UPC, Foncha the KNDP and Endeley the KNC."),
            PQ("The KKEVO Paper 1 mock A has 40 questions in 60 minutes. How many minutes per question does that average? "
               "A: 1. B: 1.5. C: 2. D: 2.5.",
               "**B**. 60 divided by 40 is 1.5 minutes. This is a KKEVO practice setting; check the official time on the real paper."),
            PQ("Which was NOT a result of the 1972 referendum? A: The United Republic of Cameroon was created. "
               "B: The two federated states were abolished. C: 20 May became National Day. D: The CNU was formed.",
               "**D**. The CNU was formed on 1 September 1966, long before the 1972 referendum. The others followed 1972."),
            SUM("The outline says only that Paper 1 is multiple choice. Check the Board instructions for time and number of questions.",
                "Divide the time by the number of questions, work in two passes, and answer every question unless the rules say otherwise.",
                "Eliminate options by linking each one to its own date, person or event.",
                "Learn look-alike pairs: 1959 and 1960; KNC and KNDP; OAU and AU; Camp David and Oslo.",
                "Underline words such as NOT and ONLY, and read all four options before choosing."),
        ],
    ),
    # ------------------------------------------------------------------ 4. Paper 2 planning
    lesson(
        module=M_EXAM, topic="Paper 2",
        title="Paper 2: planning a structured answer",
        slug="history-paper-2-planning-a-structured-answer",
        minutes=24,
        summary="How to read the command word and the marks, plan with point-evidence-explain paragraphs, and write clear "
                "introductions and conclusions with accurate dates and names.",
        objectives=[
            "Say what the syllabus tells us about Paper 2 and where to check the details",
            "Recognise the command words describe, explain, why and to what extent",
            "Use the marks as a guide to the length of an answer",
            "Plan a paragraph with point, evidence and explanation, and write a short introduction and conclusion",
        ],
        key_concepts=["Paper 2", "Command word", "Mark allocation", "Point-evidence-explain", "Introduction", "Conclusion"],
        blocks=[
            H("Introduction"),
            T("Paper 2 is the part of the examination where you write. A student who knows a lot of History can still lose "
              "marks by writing a long story that does not answer the question. A calm plan fixes this.\n\n"
              "In this lesson you learn to read the question, plan an answer in a few minutes, and set it out so that an examiner "
              "can find your points quickly."),
            D("The course outline says that Paper 2 is **structured essays**. It does not state the time, the number of questions "
              "to answer, or the marks. Questions often have parts, such as (a) and (b).",
              title="Paper 2 at a glance",
              note="Check the current GCE Board instructions and ask your teacher. In this course, essays cannot be marked by the computer, "
                   "so the practice sets test your technique by multiple choice."),
            H("Command words"),
            T("The **command word** is the word that tells you what to do. Underline it before you start."),
            KEY("Four command words", "Each one needs a different kind of answer.", cards=[
                ["Describe", "Say what happened, in order, with dates, names and details. You do not need to give reasons."],
                ["Explain", "Give reasons or causes. Use the word because and link each fact to the result."],
                ["Why", "The same as explain: give causes. A good answer gives several, with the most important developed."],
                ["To what extent", "Judge how far a statement is true. Give evidence for it and against it, then reach a conclusion."],
            ], note="Other words you may see include state, outline and compare. Read what each one asks and do exactly that."),
            H("Marks tell you how much to write"),
            T("Most parts of a structured question show the number of marks in brackets. Use the number as a guide, not as a "
              "target to match word for word. As a general idea, a part with few marks needs a short, direct answer, and a part "
              "with many marks needs several developed points.\n\n"
              "The GCE Board decides how marks are awarded. For practice, imagine that a (b) part worth 8 marks needs about "
              "four points, each with evidence and explanation. This imagined example is for practice only."),
            H("Point, evidence, explain"),
            T("A strong paragraph has three parts. Make the **point**, give the **evidence** (a date, name or fact), and **explain** "
              "how the evidence answers the question."),
            KEY("A model paragraph", "Question: Why was the UPC banned in 1955?", cards=[
                ["Point", "The French administration saw the UPC as a threat."],
                ["Evidence", "The UPC demanded reunification and a fixed date for independence. After riots in May 1955, the party was banned in July 1955."],
                ["Explain", "France was not ready to accept these demands, so it used a ban to stop the party."],
            ]),
            H("Introductions and conclusions"),
            T("For a long answer, write a short **introduction**: one or two sentences that show you understand the question, "
              "for example by defining a key term and saying what you will argue. Then write one paragraph for each point.\n\n"
              "End with a short **conclusion** that answers the question directly. In a to what extent question, the conclusion "
              "must give a judgement, not just repeat the paragraphs."),
            TIP("Use dates and names only when you are sure. If you cannot recall an exact date, give the year or the event "
                "instead of guessing. A wrong date can lose marks, and a correct fact with a clear explanation is better than "
                "a risky detail."),
            EX("Model answer plan 1", intro="Describe the events of the plebiscites of 11 February 1961 in the Southern and Northern Cameroons.", steps=[
                S("Command word", text="Describe: say what happened and in what order. No need for long reasons."),
                S("Introduction", text="A plebiscite is a direct vote on one question. The UN organised separate plebiscites in the two parts on 11 February 1961."),
                S("The choice", text="Voters had two options only: independence by joining Nigeria, or independence by joining the Republic of Cameroun. There was no option of separate independence."),
                S("Southern Cameroons", text="The south voted clearly to join the Republic of Cameroun."),
                S("Northern Cameroons", text="The north voted to join Nigeria and became part of Nigeria on 1 June 1961. Cameroun protested without success."),
                S("Conclusion", text="Reunification of the south with the Republic of Cameroun followed on 1 October 1961, after the Foumban Conference of July 1961."),
            ]),
            EX("Model answer plan 2", intro="To what extent did the end of the Cold War bring democracy to Africa?", steps=[
                S("Command word", text="To what extent: weigh evidence for and against, then judge."),
                S("Introduction", text="The Cold War ended with the collapse of the USSR in December 1991. Say that you will look at both the changes and their limits."),
                S("For: multiparty politics", text="In the early 1990s many one-party states moved to multiparty politics. In Cameroon the SDF was launched on 26 May 1990 and the liberty laws of December 1990 allowed political parties."),
                S("For: outside pressure", text="Donor countries linked aid to democratic reform, which pushed governments towards change."),
                S("Against: limited reform", text="Supporters of the changes say they were peaceful and gradual; critics say reforms were limited and slow. In Cameroon a 2008 amendment removed the limit on presidential terms."),
                S("Against: other causes and new conflicts", text="Internal pressure also mattered, and ethnic wars such as Rwanda show that change was not always peaceful."),
                S("Conclusion", text="Judge: the end of the Cold War encouraged multiparty politics, but the amount of democracy differed from country to country."),
            ]),
            H("Common mistakes"),
            MISTAKE("Telling the story instead of answering",
                    "A long story with no link to the question earns little. After each fact add a sentence that starts with 'This shows that' or 'This led to'."),
            MISTAKE("Ignoring the command word",
                    "A describe question needs events in order. An explain question needs reasons. A to what extent question needs both sides and a judgement."),
            MISTAKE("Writing a very long answer for a small part",
                    "Use the marks as a guide. A short part needs a short, direct answer. Save your time and energy for the parts with most marks."),
            QUIZ("A question begins 'Explain why ...'. What should your answer mainly contain?",
                 ["A list of dates", "Reasons and causes linked with the word because", "Your personal opinion about the topic", "A story with no reasons"], 1,
                 "Explain and why questions ask for reasons or causes. Link each fact to the result.",
                 hint="Which kind of answer says 'because'?",
                 feedback=["Dates are evidence, but a list does not explain.", "", "Opinion without evidence is weak.", "A story with no reasons does not answer an explain question."]),
            QUIZ("In a point-evidence-explain paragraph, what is the 'explain' part?",
                 ["Repeating the question", "A date or name", "A sentence showing how the evidence answers the question", "The final mark"], 2,
                 "The explain sentence links the evidence to the question: 'This shows that ...'.",
                 hint="Evidence is the fact. What do you do with the fact?",
                 feedback=["Repeating the question adds nothing.", "That is the evidence part.", "", "Marks are not part of an answer."]),
            H("Practice questions"),
            PQ("Rewrite this as a point-evidence-explain paragraph: 'The OAU was founded in 1963.' The question is: why was the OAU important?",
               "Point: The OAU was important because it brought African states together. Evidence: it was founded in Addis Ababa on 25 May 1963 with aims "
               "such as unity and ending colonialism. Explain: this shows that African states wanted to cooperate and to support liberation movements."),
            PQ("Which command word asks you to weigh both sides and make a judgement, and what must your conclusion do?",
               "To what extent. The conclusion must give a judgement that answers the question, not just repeat the points."),
            PQ("Write an introduction (two sentences) for: Explain why the Federal Republic of Cameroon became a unitary state in 1972.",
               "On 20 May 1972 a referendum replaced the federation of East and West Cameroon with a unitary state, the United Republic of Cameroon. "
               "This answer will explain the reasons given by the government, such as cost and national unity, and the factors that had already centralised power."),
            PQ("A (a) part is worth 2 marks and a (b) part 8 marks. How should they differ in length?",
               "The 2-mark part needs a short, direct answer of about two clear points. The 8-mark part needs several developed points with evidence and explanation. "
               "These are practice guidelines; check the real paper for the marks."),
            SUM("The outline says Paper 2 is structured essays. Check the Board instructions for time, number of questions and marks.",
                "Underline the command word: describe, explain, why, to what extent.",
                "Use the marks as a guide to length.",
                "Build paragraphs with point, evidence and explanation.",
                "Write a short introduction and a conclusion that answers the question, and use only dates you are sure of."),
        ],
    ),
    # ------------------------------------------------------------------ 5. Paper 2 model answers
    lesson(
        module=M_EXAM, topic="Paper 2",
        title="Paper 2: model answer plans and common errors",
        slug="history-paper-2-model-answers-and-common-errors",
        minutes=25,
        summary="Three full model answer plans (Cameroon, African decolonization, Cold War), a checklist to review your own answers, "
                "and the most common errors: narrative without explanation, wrong dates and one-sided answers.",
        objectives=[
            "Study model answer plans from three different parts of the course",
            "Use a checklist to review an answer",
            "Recognise narrative without explanation and rewrite it",
            "Avoid wrong dates and one-sided answers",
        ],
        key_concepts=["Model answer plan", "Checklist", "Narrative", "Explanation", "Accuracy", "Balance"],
        blocks=[
            H("Introduction"),
            T("In the previous lesson you learned to plan an answer. Here you will see three complete plans, each from a different "
              "part of the course. A plan lists the points of an answer in order. In the examination you write each point as "
              "a paragraph.\n\n"
              "The plans use only facts from the course lessons. The marks shown are examples for practice. The GCE Board decides the real marks."),
            EX("Model answer plan 1: Cameroon", intro=(
                "(a) Why was the UPC banned in July 1955? (b) What were the consequences of the ban? "
                "Suppose (a) is worth 6 marks and (b) 8 marks."), steps=[
                S("(a) Radical demands", text="The UPC demanded reunification and a fixed date for independence, which France would not accept."),
                S("(a) French view", text="The French administration favoured rival parties (ESOCAM, BDC) and saw the UPC as a threat."),
                S("(a) The May 1955 riots", text="Riots in towns including Douala and Yaoundé in May 1955; France banned the UPC in July 1955."),
                S("(b) Exile and the maquis", text="Leaders fled to Southern Cameroons and were expelled in 1957; some members took up arms in the maquis. Um Nyobè was killed in September 1958."),
                S("(b) Moderate parties in power", text="The UPC could not take part in the 1956 elections, and Mbida, then Ahidjo, led the government towards independence on 1 January 1960."),
                S("(b) Different views", text="Historians still debate how far the UPC's struggle sped up independence and how to judge the French repression. Mention more than one view."),
            ]),
            EX("Model answer plan 2: African decolonization", intro=(
                "Compare peaceful transfers of power and armed struggles in the decolonization of Africa, using examples."), steps=[
                S("Introduction", text="Decolonization is the process by which colonies gained independence. It happened by negotiation in some places and by war in others."),
                S("Peaceful transfers", text="Nationalist parties won elections and power was handed over at a fixed date. Ghana became independent on 6 March 1957 under Nkrumah; Nigeria and Senegal followed in 1960."),
                S("Armed struggles", text="In Algeria the FLN fought France from 1954 until independence in 1962. In Kenya the Mau Mau uprising began in 1952 and independence came in 1963."),
                S("Why they differed", text="Where there were many European settlers, or where the colonial power refused to leave, Africans turned to armed struggle. Portugal refused until a revolution in Lisbon in 1974; Angola and Mozambique won independence in 1974-1975 after long wars."),
                S("Similarity", text="In both cases nationalists demanded self-rule. Cameroon combined both methods: the constitutional route of Ahidjo and the armed struggle of the UPC."),
                S("Conclusion", text="The route depended on the colonial power and on settlers; both ended colonial rule, but armed struggles were longer and more costly."),
            ]),
            EX("Model answer plan 3: Cold War", intro=(
                "Explain why the USSR collapsed in 1991."), steps=[
                S("Introduction", text="The USSR was dissolved in December 1991 after a long rivalry with the USA. Say that several causes combined."),
                S("Economic weakness", text="A stagnant economy and shortages."),
                S("Cost of the arms race and Afghanistan", text="The huge cost of the arms race and of the war in Afghanistan (1979-1989)."),
                S("Gorbachev's reforms", text="From 1985 Gorbachev introduced glasnost (openness) and perestroika (restructuring); the reforms allowed criticism."),
                S("Events of 1989-1991", text="Communist governments fell across Eastern Europe in 1989 and the Berlin Wall was opened on 9 November. A failed coup in August 1991 was followed by declarations of independence in the republics."),
                S("Conclusion", text="Internal weakness and reform were the main causes, though historians also discuss the effect of Western pressure."),
            ]),
            H("A checklist for your own answer"),
            T("This checklist is a study tool written by KKEVO. It is not an official mark scheme, and we do not know how the GCE Board "
              "allocates its marks. Use it to check your practice answers before you show them to a teacher."),
            KEY("Review checklist", "Tick each item.", cards=[
                ["Question", "Did I follow the command word and answer every part, (a) and (b)?"],
                ["Facts", "Are my dates and names accurate and linked to the right event?"],
                ["Explanation", "Does each paragraph explain, with because or this led to, and not only tell the story?"],
                ["Balance and structure", "Did I give more than one view where the topic is debated, and end with a clear conclusion?"],
            ]),
            H("Common errors"),
            MISTAKE("Narrative without explanation",
                    "Weak: 'The UPC was banned in July 1955. Then leaders went to Kumba.' Better: 'France banned the UPC in July 1955 because it rejected its demands, "
                    "so many leaders went into exile and some members joined the maquis.' The better version links facts with reasons."),
            MISTAKE("Wrong dates",
                    "Mixing 1959 with 1960, or 1989 with 1991, changes the meaning of the answer. Revise date pairs, and when unsure give the year or the event."),
            MISTAKE("One-sided answers",
                    "On debated topics such as the 1961 plebiscite, Foumban, 1972 or the Arab-Israeli conflict, describe the different views and avoid emotional language."),
            QUIZ("Which sentence explains instead of only telling the story?",
                 ["The Berlin Wall was opened on 9 November 1989.", "Gorbachev became leader in 1985.",
                  "The cost of the arms race weakened the Soviet economy, so reforms were needed.", "The USSR was dissolved in December 1991."], 2,
                 "Only option C links a cause (the cost of the arms race) to a result (a weak economy and need for reform).",
                 hint="Look for the sentence that has a reason in it.",
                 feedback=["This is a fact, but it does not explain.", "This is a date and a fact only.", "", "This is a date and a fact only."]),
            QUIZ("Why is the checklist in this lesson not a mark scheme?",
                 ["Because KKEVO wrote it as a study tool, and the GCE Board decides the real marks", "Because marks do not matter",
                  "Because history has no right answers", "Because it is too long"], 0,
                 "The checklist helps you review, but only the GCE Board's own mark scheme decides the real marks.",
                 hint="Who decides how marks are awarded?",
                 feedback=["", "Marks matter, but we do not know the Board's scheme.", "History has accurate facts and good arguments.", "Length is not the reason."]),
            H("Practice questions"),
            PQ("Rewrite this to include a reason: 'Ahidjo became President in 1960.'",
               "Ahidjo became President in May 1960 after being leader of the government that took Cameroun to independence on 1 January 1960; "
               "this shows that the constitutional route was led by him."),
            PQ("List two things a conclusion in a to what extent answer must do.",
               "It must answer the question directly with a judgement and it must be based on the evidence given for and against."),
            PQ("Correct the date error: 'The Berlin Wall was opened in 1991 and the USSR collapsed in 1989.'",
               "The Berlin Wall was opened on 9 November 1989, and the USSR was dissolved in December 1991."),
            PQ("Write one balanced sentence about the 1961 plebiscite and Foumban.",
               "Many saw reunification as the fulfilment of the nationalist dream, chosen by a clear majority; others argue that the lack of an independence option "
               "and the short Foumban talks left Anglophones with weak guarantees."),
            SUM("A plan lists the points of an answer in order; each point becomes a paragraph.",
                "Three plans: the 1955 UPC ban, peaceful and armed decolonization, and the collapse of the USSR.",
                "Use a checklist to review: question, facts, explanation, balance and structure. It is not an official mark scheme.",
                "Avoid narrative without explanation, wrong dates and one-sided answers."),
        ],
    ),
]
