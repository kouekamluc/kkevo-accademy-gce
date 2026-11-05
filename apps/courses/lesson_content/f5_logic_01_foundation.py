"""Form 5 Logic (O Level 0590), module "The Foundation of Logic".
Draft content: check against the official syllabus and your textbook."""

from .dsl import *  # noqa: F403

COURSE = ("logic", "form-5")

MODULE = "The Foundation of Logic"

LESSONS = [
    # ------------------------------------------------------------------ 1.1.1
    lesson(
        module=MODULE,
        topic="Definition and origin of Logic",
        title="What is logic? Definition and origin",
        slug="found-what-is-logic-definition-and-origin",
        minutes=18,
        summary="Logic is the science and art of correct reasoning. It began as a study in ancient Greece with Aristotle and developed through the Stoics, medieval scholars and, in the nineteenth century, Boole's symbolic logic.",
        objectives=[
            "Define logic as the science and art of correct reasoning",
            "Explain the difference between reasoning well and merely feeling sure",
            "Say who Aristotle was and why he is called the father of logic",
            "Outline in general terms the later history: the Stoics, medieval logic, Boole and symbolic logic",
        ],
        key_concepts=["Logic", "Reasoning", "Argument", "Science and art", "Aristotle", "Organon", "Symbolic logic"],
        blocks=[
            H("Introduction"),
            T("Two friends argue about football after a match in Douala. One says, \"Our team is the best, so it will win the cup.\" "
              "The other says, \"A team that has won all its home games and lost none away is likely to finish top.\" "
              "Both are trying to prove something. But only one of them gives a good reason."),
            T("How do we tell a good reason from a weak one? That is the question logic tries to answer. "
              "In this lesson you will learn what logic is, what it studies, and where it comes from."),
            H("What logic is"),
            D("**Logic** is the science and art of correct reasoning. It studies the rules that tell us when a conclusion "
              "really follows from the reasons given for it.",
              title="Definition: logic",
              note="The word comes from the Greek logos, which can mean word, reason or account."),
            T("**Reasoning** is the mental act of moving from one or more statements (the reasons) to another statement (the conclusion). "
              "When we put the reasons and the conclusion into words, we get an **argument**. "
              "For example: \"All students who pay fees may sit the exam. Ngwa paid her fees. So Ngwa may sit the exam.\""),
            KEY("Why \"science\" and why \"art\"?", "The definition has two parts.", cards=[
                ["Science", "Logic is a body of organised knowledge. It gives general laws and principles, and it explains WHY an argument is good or bad."],
                ["Art", "Logic is also a skill. Like football or cooking, you improve by practice: you learn to build good arguments and to spot bad ones."],
            ]),
            T("Notice the word **correct**. Logic does not ask \"Do I like this conclusion?\" or \"Is everyone saying it?\" "
              "It asks \"Do the reasons support the conclusion?\" A person can feel very sure and still reason badly."),
            MISTAKE("Logic is not the same as being clever or being right",
                    "A logician is not a person who always knows the facts. Logic checks the link between reasons and conclusion. "
                    "A conclusion can be true although it was reached badly, and false although it was reached by a careful process from false reasons."),
            H("The origin of logic"),
            T("People have always argued. But the first person to study reasoning in a **systematic** way (that is, "
              "step by step, with rules and technical terms) was **Aristotle** (384-322 BC), a Greek thinker who studied in Athens "
              "under Plato and later taught his own students."),
            D("**Aristotle** is traditionally called the father of logic because he was the first to write a full "
              "study of correct reasoning. His writings on the subject were later collected under the name **Organon** "
              "(Greek for \"tool\" or \"instrument\"), because logic was seen as the tool of all other knowledge.",
              title="Definition: Aristotle and the Organon",
              note="The collection was put together by later editors, not by Aristotle himself."),
            T("Aristotle gave special attention to the **syllogism**, a kind of argument with two reasons and one conclusion. "
              "Here is the classic example: \"All men are mortal. Socrates is a man. So Socrates is mortal.\" "
              "You will study syllogisms in later modules of this course."),
            H("A short history after Aristotle"),
            T("Logic did not stop with Aristotle. Here is the story in general terms. Exact dates and details differ between books, "
              "so use your textbook for more."),
            KEY("Four stages", "Learn this outline.", cards=[
                ["Ancient Greece", "Aristotle studies the syllogism and the structure of statements. The **Stoics**, a later school of Greek philosophers, study arguments built from whole statements joined by words such as \"if\", \"and\" and \"or\"."],
                ["Medieval period", "Scholars in the Middle Ages, in Europe and also in the Arab world, teach, copy and improve Aristotle's logic. It becomes a main subject in the universities."],
                ["Nineteenth century", "The English mathematician **George Boole** shows that reasoning can be written with symbols and worked like algebra. This starts **symbolic logic** (also called mathematical logic)."],
                ["Modern logic", "Thinkers such as Gottlob Frege build on this, and logic becomes closely linked with mathematics and later with computer science."],
            ]),
            TIP("Where this appears in the exam: Paper 1 often asks who started logic, what the Organon is, or to pick the best definition of logic. "
                "Paper 2 Section A may ask you to define logic and outline its origin in a few sentences. "
                "Learn the definition word for word and the four stages above."),
            H("Worked examples"),
            EX("Worked example 1: is it reasoning?", intro="Which of these is an example of reasoning in the logician's sense? "
               "(a) \"I am hungry.\" (b) \"The market opens on Monday. Today is Monday. So the market is open.\" (c) \"Good morning, madam.\"", steps=[
                S("Recall what reasoning needs", text="Reasoning moves from reasons to a conclusion. We need at least one reason and a conclusion that is claimed to follow."),
                S("Test (a)", text="\"I am hungry\" is a single statement. It gives no reason and draws no conclusion."),
                S("Test (c)", text="A greeting is not a statement that can be true or false, and it has no reasons."),
                S("Test (b)", text="Two reasons (opens on Monday; today is Monday) lead to a conclusion (the market is open). This is an argument. The answer is (b)."),
            ]),
            EX("Worked example 2: model answer on origin", intro="Question: Define logic and say briefly how the study began. (4 marks)", steps=[
                S("Definition (1 mark)", text="Logic is the science and art of correct reasoning."),
                S("Explain the key words (1 mark)", text="It is a science because it gives laws that explain why reasoning is good or bad. It is an art because it is a skill improved by practice."),
                S("Origin (1 mark)", text="The systematic study began in ancient Greece with Aristotle, whose works on reasoning were later collected as the Organon."),
                S("Later history (1 mark)", text="It was developed by the Stoics and medieval scholars and, in the nineteenth century, by Boole, who began symbolic logic."),
            ]),
            QUIZ("Who is traditionally called the father of logic?",
                 ["Plato", "Aristotle", "George Boole", "Socrates"], 1,
                 "Aristotle wrote the first full study of correct reasoning, later collected as the Organon.",
                 hint="Think of the Greek thinker whose collected works on reasoning are called the Organon.",
                 feedback=["Plato was Aristotle's teacher. He wrote about many topics but did not found the systematic study of reasoning.",
                           "",
                           "Boole lived in the nineteenth century. He started symbolic logic, but he came about 2000 years after Aristotle.",
                           "Socrates is a famous teacher of argument, but he left no writings. He is the man in the example syllogism, not its inventor."]),
            QUIZ("Which statement best explains why logic is called an ART?",
                 ["Because it deals with painting and music", "Because it is a skill that improves with practice",
                  "Because it has no rules", "Because it only studies feelings"], 1,
                 "An art is a practical skill. We become better at reasoning by practising it.",
                 hint="Think of other skills, such as football or tailoring.",
                 feedback=["In this definition, \"art\" means skill, not fine arts such as painting.", "",
                           "Logic has many rules. The word \"science\" in the definition points to them.",
                           "Logic studies reasoning, not feelings. Feelings may even get in the way of reasoning."]),
            H("Practice"),
            PQ("Define logic and explain the words \"science\" and \"art\" in your definition.",
               "Logic is the science and art of correct reasoning. It is a science because it is organised knowledge with general laws that explain why an argument is good or bad. "
               "It is an art because it is a skill: we get better at building and checking arguments by practice."),
            PQ("Who was Aristotle, and what is the Organon?",
               "Aristotle (384-322 BC) was a Greek philosopher, a pupil of Plato, who first studied reasoning in a systematic way. "
               "The Organon (\"tool\") is the name later given to the collection of his works on logic, because logic is the tool for all other knowledge."),
            PQ("Name the contribution to logic of each of these: (a) the Stoics, (b) medieval scholars, (c) George Boole.",
               "(a) The Stoics studied arguments built from whole statements joined by words such as if, and, or. "
               "(b) Medieval scholars taught, copied and improved Aristotle's logic in the schools and universities. "
               "(c) Boole showed that reasoning can be written in symbols and worked like algebra, which began symbolic logic."),
            PQ("A student says: \"Logic is about proving that I am right.\" Explain why this is a wrong idea of logic.",
               "Logic studies whether the reasons given really support the conclusion. It checks the link between reasons and conclusion for everyone, "
               "including the person who makes the argument. A logical person accepts that an argument is weak even if it supports the conclusion he likes."),
            SUM("Logic is the science and art of correct reasoning.",
                "Reasoning moves from reasons to a conclusion; put into words it is an argument.",
                "Logic is a science (laws and explanation) and an art (a skill improved by practice).",
                "Aristotle began the systematic study of reasoning; his works on it were collected as the Organon.",
                "Later stages: the Stoics, medieval logic, and Boole's symbolic logic in the nineteenth century."),
        ],
    ),
    # ------------------------------------------------------------------ 1.1.2
    lesson(
        module=MODULE,
        topic="Purpose (value) and division (types) of Logic",
        title="Why study logic, and the kinds of logic",
        slug="found-purpose-and-types-of-logic",
        minutes=20,
        summary="We study logic to think clearly, to spot errors and to argue well in daily life. Logic is commonly divided into traditional and symbolic, formal and informal, deductive and inductive, though textbooks group these differently.",
        objectives=[
            "Give at least three reasons why logic is worth studying",
            "Explain the divisions: traditional and symbolic, formal and informal, deductive and inductive",
            "Classify a simple argument as deductive or inductive",
            "Say why textbooks may divide logic in different ways",
        ],
        key_concepts=["Value of logic", "Traditional logic", "Symbolic logic", "Formal logic", "Informal logic", "Deductive argument", "Inductive argument"],
        blocks=[
            H("Introduction"),
            T("A trader at Mokolo market in Yaounde hears two offers. A supplier says: \"Buy my tomatoes, everybody buys them.\" "
              "A second supplier says: \"My tomatoes were delivered this morning, you can check the crate, and the price is 500 FCFA a kilo, "
              "lower than your usual supplier.\" The trader must decide. "
              "What helps her decide well? Clear thinking."),
            T("In the last lesson you learned that logic is the science and art of correct reasoning. "
              "Now we ask two questions. WHY should we study it (its purpose or value)? And what KINDS of logic are there (its division)?"),
            H("The purpose and value of logic"),
            KEY("Four benefits of studying logic", "Logic helps in school and in daily life.", cards=[
                ["Clear thinking", "Logic teaches us to say exactly what we mean, to break a problem into parts and to move step by step from reasons to a conclusion."],
                ["Spotting errors", "Logic teaches us to detect faulty reasoning, called **fallacies**, in what others say and in what we say ourselves."],
                ["Arguing well", "Logic helps us build strong arguments, give good reasons and answer an opponent fairly, in the classroom, in a meeting or in a court case."],
                ["Other subjects", "Mathematics, science, law, ethics and computer science all depend on correct reasoning. Logic is called the tool of the other sciences."],
            ]),
            T("Think of a family that must decide whether to send a child to a boarding school or a day school. "
              "Logic does not tell them what they value. But it helps them list their reasons, see which reasons really support each choice, "
              "and avoid mistakes such as choosing a school only because \"everyone is going there\"."),
            D("The **value of logic** is practical and mental. Practically, it helps us decide and argue well. "
              "Mentally, it gives discipline: accuracy, order and honesty in thought.",
              title="Definition: value of logic"),
            MISTAKE("Logic does not make you always right",
                    "Logic cannot give you facts. If your reasons are false, a perfectly reasoned argument can still lead to a false conclusion. "
                    "Logic helps you check the reasoning. Checking the facts is also your duty."),
            H("The division of logic"),
            T("Logic can be divided in several ways, depending on what we look at. "
              "**Textbooks do not all divide logic in the same way or use the same names.** "
              "Below are the common divisions. If your teacher's textbook uses a different grouping, follow your textbook."),
            IMG("f5l-found-divisions-of-logic.svg",
                alt="A tree with Logic at the top and three divisions below: method (traditional and symbolic), form or content (formal and informal), and strength of support (deductive and inductive).",
                caption="Figure 1. Three common ways of dividing logic. These are different angles on the same subject, not three separate subjects."),
            D("**Traditional logic** (also called classical or Aristotelian logic) is the logic that began with Aristotle. "
              "It works with ordinary-language statements about classes, such as \"All teachers are graduates\", and with the syllogism. "
              "**Symbolic logic** (also called modern or mathematical logic) uses symbols and rules, like algebra, "
              "for example p ⊃ q, to study arguments with exact precision.",
              title="Division 1: traditional and symbolic logic",
              note="The syllabus symbols are ~ (not), . (and), v (or), ⊃ (if...then) and ≡ (if and only if). You will learn them in a later module."),
            D("**Formal logic** studies the FORM (the pattern) of an argument, whatever it is about. "
              "**Informal logic** studies the content and context of everyday arguments: meaning of words, relevance, and fallacies of language and evidence.",
              title="Division 2: formal and informal logic"),
            T("Here is the idea of form. Compare: \"All mangoes are fruits. This is a mango. So this is a fruit\" and "
              "\"All taxi drivers are licensed. Ali is a taxi driver. So Ali is licensed.\" "
              "The topics differ, but the form is the same: All A are B. X is A. So X is B. Formal logic studies that pattern."),
            D("A **deductive argument** claims that the conclusion follows with certainty: if the reasons are true, the conclusion MUST be true. "
              "An **inductive argument** claims only that the conclusion is probable: if the reasons are true, the conclusion is LIKELY to be true.",
              title="Division 3: deductive and inductive logic",
              note="Deductive: from general to particular, with certainty. Inductive: usually from particular cases to a general claim, with probability."),
            TIP("Where this appears in the exam: Paper 1 asks you to classify an example as deductive or inductive, or to choose the correct pair of terms in a division of logic. "
                "Paper 2 Section A may ask you to state three values of logic and to distinguish two kinds of logic. "
                "Always give a short example."),
            H("Worked examples"),
            EX("Worked example 1: deductive or inductive?", intro="Classify each argument. "
               "(a) \"Every teacher at this school has a degree. Mr Fon teaches at this school. So Mr Fon has a degree.\" "
               "(b) \"The last five times it rained in the evening, the road to the farm was flooded the next morning. It rained this evening. So the road will probably be flooded tomorrow.\"", steps=[
                S("Ask: does the conclusion claim certainty or probability?", text="This question decides the type."),
                S("Argument (a)", text="If the two reasons are true, Mr Fon MUST have a degree. The conclusion is claimed with certainty. It is **deductive**."),
                S("Argument (b)", text="The word \"probably\" and the way the reasoning relies on past cases show that the conclusion is only likely. It is **inductive**."),
            ]),
            EX("Worked example 2: stating the values of logic", intro="A student council member is accused of causing a problem. "
               "Two classmates argue about it. Explain how logic could help them, in three points.", steps=[
                S("Clear thinking", text="Logic helps them state exactly what the accusation is and what reasons support it."),
                S("Spotting errors", text="They can notice faulty reasoning, for example attacking the person's character instead of answering the facts."),
                S("Arguing well", text="They can present reasons that really support their conclusion and answer the other side fairly, and so reach a conclusion the council can accept."),
            ]),
            QUIZ("Which kind of logic studies the pattern of an argument whatever its topic?",
                 ["Informal logic", "Inductive logic", "Formal logic", "Traditional logic only"], 2,
                 "Formal logic studies the form (pattern) of arguments, independent of their subject matter.",
                 hint="The key word is \"form\".",
                 feedback=["Informal logic studies the content and context of everyday arguments, including fallacies of language.",
                           "Inductive logic is about how strongly the reasons support the conclusion (probability), not about pattern in general.",
                           "",
                           "Traditional logic is a division by method (it began with Aristotle). It does study form, but the name \"formal\" names the form-based division."]),
            QUIZ("\"Every time I wash my clothes in this river they dry in two hours, so these clothes will dry in two hours today.\" This argument is mainly...",
                 ["Deductive, because it has a general statement", "Inductive, because it moves from past cases to a probable conclusion", "Symbolic, because it is about clothes", "Not an argument at all"], 1,
                 "The conclusion is only probable. The past cases make it likely but cannot make it certain.",
                 hint="Could the conclusion be false even if the reason is true?",
                 feedback=["A deductive argument guarantees its conclusion. Tomorrow's weather could change, so this argument does not.",
                           "",
                           "\"Symbolic\" refers to the use of symbols, not to the subject. This argument uses none.",
                           "It gives a reason and draws a conclusion from it, so it is an argument."]),
            H("Practice"),
            PQ("State three reasons why a student should study logic.",
               "(1) Logic improves clear thinking: it helps us state ideas exactly and move from reasons to a conclusion. "
               "(2) It helps us detect fallacies in our own reasoning and in what others say. "
               "(3) It helps us argue well in school, work and daily life, and supports other subjects such as mathematics and law."),
            PQ("Distinguish between traditional logic and symbolic logic.",
               "Traditional logic began with Aristotle. It uses ordinary language and studies statements about classes and the syllogism. "
               "Symbolic logic uses symbols and rules, like algebra, and began in the nineteenth century with Boole. It studies arguments with exact precision."),
            PQ("Distinguish a deductive argument from an inductive argument and give one example of each.",
               "A deductive argument claims that the conclusion follows with certainty if the reasons are true. "
               "Example: All nurses are trained. Ada is a nurse. So Ada is trained. "
               "An inductive argument claims only that the conclusion is probable. "
               "Example: The bus has been late on every wet day this month, so it will probably be late today, because it is raining."),
            PQ("A student says: \"All books divide logic in exactly the same way.\" Explain why this is not correct.",
               "Authors choose different ways to divide and name the branches of logic. "
               "One book may speak of traditional and symbolic logic, another of formal and informal logic, and another of deductive and inductive logic. "
               "These are different points of view, so a student should follow the textbook used in class."),
            SUM("Logic is valuable for clear thinking, spotting errors, arguing well and supporting other subjects.",
                "Logic does not give facts. It checks the link between reasons and conclusion.",
                "Division by method: traditional (Aristotelian) logic and symbolic (modern) logic.",
                "Division by form and content: formal logic (pattern) and informal logic (everyday content and fallacies).",
                "Division by support: deductive (certain) and inductive (probable) arguments.",
                "Textbooks differ in how they divide logic: follow your teacher's textbook."),
        ],
    ),
    # ------------------------------------------------------------------ 1.1.3
    lesson(
        module=MODULE,
        topic="Logic and related fields",
        title="How logic differs from psychology, philosophy, mathematics, language, rhetoric, ethics and law",
        slug="found-logic-and-related-fields",
        minutes=20,
        summary="Logic is related to psychology, philosophy, mathematics, grammar, rhetoric, ethics and law, but each asks a different question: logic asks whether the reasons support the conclusion.",
        objectives=[
            "Explain how logic differs from psychology, philosophy and mathematics",
            "Distinguish logic from grammar and language, rhetoric, ethics and law",
            "Say what logic offers to each of these fields",
            "Decide which field a given question belongs to",
        ],
        key_concepts=["Psychology", "Philosophy", "Mathematics", "Grammar", "Rhetoric", "Ethics", "Law"],
        blocks=[
            H("Introduction"),
            T("A court is hearing a land case in a Cameroonian town. The lawyer speaks with great skill and moves the crowd. "
              "A witness is nervous and forgets his words. The judge asks: \"Do the facts the lawyer gave really support his conclusion?\" "
              "Notice how many different things are happening: speech, feeling, law and reasoning."),
            T("Logic does not work alone. It touches many fields. To understand logic well, we must see what it shares with each field and what makes it different. "
              "The key question of logic is always: **do the reasons support the conclusion?**"),
            H("Logic and psychology"),
            D("**Psychology** is the study of the mind and of behaviour: how people think, feel, remember and act. "
              "**Logic** does not describe how people DO think. It states how people SHOULD reason if they want to reason correctly.",
              title="Logic and psychology",
              note="Psychology describes and explains. Logic judges and sets standards (it is called a normative science)."),
            T("Example: A student panics in an exam and reasons badly. Psychology asks WHY she panicked (fear, tiredness). "
              "Logic asks whether her answer was correct reasoning. A mind can be healthy and still reason badly, and a hurried mind can still reason well."),
            H("Logic and philosophy"),
            D("**Philosophy** asks the biggest questions: what is real, what can we know, how should we live. "
              "Logic is a part of philosophy in the traditional division and is its main tool: philosophers use logic to build and test arguments.",
              title="Logic and philosophy",
              note="Logic is a prerequisite for A Level Philosophy."),
            T("The difference: philosophy asks questions such as \"What is justice?\" or \"Can we be certain of anything?\" "
              "Logic does not answer these. It asks whether the arguments people give for their answers are correct."),
            H("Logic and mathematics"),
            D("**Mathematics** studies number, shape and quantity and uses strict proof. "
              "Logic and mathematics are close: mathematical proof uses logic, and since Boole, logic has been written in symbols. "
              "But mathematics studies quantities and structures, while logic studies reasoning in ANY subject.",
              title="Logic and mathematics"),
            H("Logic and grammar or language"),
            D("**Grammar** is the set of rules for forming correct sentences. "
              "**Logic** studies the correctness of reasoning, not of sentences.",
              title="Logic and grammar"),
            T("A sentence can be grammatically perfect and logically poor: \"The goat is a car, so it is made of metal.\" "
              "Another can be badly spelled but sound in reasoning. Still, language matters to logic. "
              "Words with two meanings can ruin an argument, and later modules study such fallacies of language."),
            H("Logic and rhetoric"),
            D("**Rhetoric** is the art of persuading an audience by speech or writing, using style, emotion and the speaker's character. "
              "Logic is concerned with the reasons that SHOULD persuade a reasonable person.",
              title="Logic and rhetoric"),
            T("A politician at a rally can move a crowd with a beautiful speech. Rhetoric measures whether he persuaded. "
              "Logic asks whether he gave good reasons. A speech can persuade and still be illogical."),
            H("Logic, ethics and law"),
            D("**Ethics** studies right and wrong conduct, and what we ought to do. **Law** is the set of rules a society enforces. "
              "Logic does not tell us what is right or what the law says. It checks the reasoning used to defend an ethical or legal conclusion.",
              title="Logic, ethics and law"),
            T("A judge may reason: \"Anyone who sells goods without paying tax breaks the tax law. The accused sold goods without paying tax. So the accused broke the tax law.\" "
              "The argument has a valid pattern. Whether the law is fair, or whether the facts are true, are questions for ethics and for evidence. "
              "Logic checks only the link between the reasons and the conclusion."),
            KEY("Summary table in words", "Each field asks its own question.", cards=[
                ["Psychology", "How do people actually think and feel?"],
                ["Philosophy", "What is real, what can we know, how should we live?"],
                ["Mathematics", "What follows about numbers and shapes?"],
                ["Grammar", "Is the sentence formed correctly?"],
                ["Rhetoric", "Does the speech persuade?"],
                ["Ethics and law", "What is right, and what do the rules say?"],
                ["Logic", "Do the reasons support the conclusion?"],
            ]),
            TIP("Where this appears in the exam: Paper 1 gives a situation or a question and asks which field it belongs to, or asks you to pick the correct difference between logic and another field. "
                "Paper 2 Section A may ask you to distinguish logic from two related fields. Always say what each field studies and what logic studies."),
            H("Worked examples"),
            EX("Worked example 1: which field asks the question?", intro="Match each question with the field that mainly asks it: "
               "(a) \"Why do some students feel afraid of speaking in class?\" (b) \"Does the conclusion follow from these two reasons?\" "
               "(c) \"Is it right to copy during an exam?\"", steps=[
                S("(a) Study of feelings and behaviour", text="This is a question about how people feel. It belongs to **psychology**."),
                S("(b) Link between reasons and conclusion", text="This is the central question of **logic**."),
                S("(c) Right and wrong conduct", text="This asks what we ought to do. It belongs to **ethics**."),
            ]),
            EX("Worked example 2: logic and rhetoric", intro="A seller shouts: \"Buy my soap! It is the soap of champions and the whole town loves it!\" Comment briefly from the points of view of rhetoric and logic.", steps=[
                S("Rhetoric", text="The speech uses a loud voice, a proud slogan and a claim about popularity. It may well persuade customers."),
                S("Logic", text="Logic asks for reasons. \"The whole town loves it\" does not show that the soap cleans well. The reasons given do not support the conclusion that the soap is good."),
                S("Conclusion", text="The speech may be persuasive but it is weak in reasoning. Persuasion and good reasoning are different things."),
            ]),
            QUIZ("Which statement correctly separates logic from psychology?",
                 ["Logic describes how people actually think; psychology says how they should think",
                  "Psychology describes how people think; logic sets standards for how they should reason",
                  "Both study only mathematical symbols",
                  "Logic studies feelings; psychology studies arguments"], 1,
                 "Psychology describes and explains mental processes. Logic judges whether reasoning is correct.",
                 hint="One of the two is descriptive and the other gives standards.",
                 feedback=["This reverses the two fields.", "",
                           "Neither field is limited to symbols. Symbolic logic is only one branch of logic.",
                           "This reverses the two fields. Psychology studies feelings and behaviour."]),
            QUIZ("Which question belongs to logic?",
                 ["Is this speech beautiful?", "Is it wrong to lie?", "Do these reasons support this conclusion?", "How do children learn to speak?"], 2,
                 "Checking whether reasons support a conclusion is the task of logic.",
                 hint="Look for the question about reasons and conclusion.",
                 feedback=["Beauty of speech is a matter for rhetoric and style.",
                           "Right and wrong are questions for ethics (and religion).",
                           "",
                           "How children learn language is a question for psychology and linguistics."]),
            H("Practice"),
            PQ("Distinguish between logic and psychology.",
               "Psychology studies how the mind actually works and how people behave. Logic studies how people should reason to reason correctly. "
               "Psychology describes; logic sets standards and judges the correctness of reasoning."),
            PQ("Explain how logic is related to mathematics and how it differs from it.",
               "Both use strict reasoning and proof, and since Boole logic can be written in symbols like algebra. "
               "But mathematics studies number, shape and quantity, while logic studies the correctness of reasoning in any subject."),
            PQ("Explain the difference between logic and rhetoric, using an example.",
               "Rhetoric is the art of persuading an audience, using style and emotion. Logic is concerned with the quality of reasons. "
               "Example: a speaker may persuade a crowd by shouting and flattering them, but if he gives no good reasons his argument is weak in logic."),
            PQ("A judge says: \"The law is unfair, so the accused did not break it.\" What would a logician say about this reasoning?",
               "A logician would note that the conclusion (the accused did not break the law) does not follow from the reason (the law is unfair). "
               "Whether a law is fair is an ethical question. Whether a person broke it depends on the facts and on what the law says."),
            SUM("Logic asks: do the reasons support the conclusion?",
                "Psychology describes how people think; logic says how they should reason.",
                "Philosophy asks the big questions; logic is its main tool for testing arguments.",
                "Mathematics studies quantity and structure; logic studies reasoning in any subject.",
                "Grammar checks sentences; rhetoric aims to persuade; logic checks the quality of reasons.",
                "Ethics and law ask what is right and what the rules say; logic checks the reasoning used to defend answers."),
        ],
    ),
    # ------------------------------------------------------------------ 1.1.4
    lesson(
        module=MODULE,
        topic="Laws of thought",
        title="The three laws of thought",
        slug="found-the-laws-of-thought",
        minutes=22,
        summary="The laws of thought are identity, non-contradiction and excluded middle: first principles that any clear reasoning must respect. Some books add the law of sufficient reason.",
        objectives=[
            "State the laws of identity, non-contradiction and excluded middle",
            "Apply each law to everyday and Cameroonian examples",
            "Mention the law of sufficient reason as an addition made by some books",
            "Avoid common mistakes, such as confusing contradiction with opposition",
        ],
        key_concepts=["Law of identity", "Law of non-contradiction", "Law of excluded middle", "Contradictory statements", "Contrary statements", "Sufficient reason"],
        blocks=[
            H("Introduction"),
            T("A man in Bamenda tells his wife, \"I was at the farm all day yesterday.\" "
              "Later he tells a neighbour, \"I spent yesterday in town at the bank.\" "
              "Both cannot be true. Whatever else we think, one of his statements must be false. "
              "Why are we so sure? Because we all rely on some basic principles of thought without even noticing them."),
            T("These principles are called the **laws of thought**. They are not laws made by a government. "
              "They are the starting points of all correct reasoning. Break them and thinking collapses."),
            D("The **laws of thought** are the basic principles that any clear and consistent thinking must respect. "
              "The traditional three are the law of **identity**, the law of **non-contradiction** and the law of **excluded middle**.",
              title="Definition: laws of thought",
              note="They are called first principles because other logical rules depend on them, and they cannot be proved from anything simpler."),
            H("1. The law of identity"),
            D("**Law of identity**: everything is what it is. In symbols: p is p, or if p is true then p is true. "
              "A word or idea must keep the same meaning throughout an argument.",
              title="Law of identity",
              note="In plain words: a thing is itself, and a term must not change its meaning in the middle of an argument."),
            T("Everyday example: if \"a bank\" means a place where we keep money, it must not suddenly mean the side of a river in the same argument. "
              "Cameroonian example: if a family agreed that \"the meeting is on Saturday\", then it is on Saturday for everyone."),
            H("2. The law of non-contradiction"),
            D("**Law of non-contradiction**: nothing can both be and not be, in the same respect and at the same time. "
              "A statement and its contradictory cannot both be true. In symbols: ~(p . ~p).",
              title="Law of non-contradiction",
              note="Notice the words \"in the same respect and at the same time\". They matter."),
            T("Example: a well in the village cannot be both full and not full of water at the same moment. "
              "But a well can be full in the rainy season and empty in the dry season. These are different times, so there is no contradiction."),
            H("3. The law of excluded middle"),
            D("**Law of excluded middle**: every statement is either true or false; there is no third possibility. "
              "Either p or not p. In symbols: p v ~p.",
              title="Law of excluded middle",
              note="\"Middle\" means a third option between a statement and its contradictory."),
            T("Example: \"Ngwa passed the exam\" is either true or false. If it is not true, then its contradictory \"Ngwa did not pass the exam\" is true. "
              "There is no middle option such as \"half passed\" for the statement as it stands."),
            T("Check with a truth table. We list every possible truth value of p, then of the whole statement. "
              "The first table shows p v ~p. The second shows ~(p . ~p)."),
            CODE("p    ~p   p v ~p   p . ~p   ~(p . ~p)\n"
                 "T    F      T        F          T\n"
                 "F    T      T        F          T", "text",
                 title="Truth table",
                 caption="p v ~p is true in every row, and so is ~(p . ~p). Both are always true."),
            H("A fourth law in some books"),
            T("Some textbooks add a fourth law: the **law of sufficient reason**. "
              "It says that everything that is true or happens has a reason, and a claim should not be accepted without a reason. "
              "The Board's syllabus lists the laws of thought without naming how many, so learn the three above and mention the fourth if your textbook gives it."),
            KEY("The three laws side by side", "Learn the key word for each.", cards=[
                ["Identity", "p is p. Keep the same meaning."],
                ["Non-contradiction", "Not both p and not p. Two contradictory statements cannot both be true."],
                ["Excluded middle", "Either p or not p. Two contradictory statements cannot both be false."],
            ]),
            MISTAKE("Confusing contradiction with opposition",
                    "Two statements that are only OPPOSED are not always contradictory. "
                    "\"All the students passed\" and \"No student passed\" are opposed, but both can be false (if some passed and some failed). "
                    "The contradictory of \"All the students passed\" is \"Some student did not pass\". "
                    "The laws of non-contradiction and excluded middle apply to true CONTRADICTORIES only."),
            MISTAKE("Using excluded middle to force a false choice",
                    "\"Either you are rich or you are poor\" is not an application of the law of excluded middle, because \"rich\" and \"poor\" are not contradictories: a person can be neither. "
                    "The law applies to a statement and its exact denial: \"He is rich\" and \"He is not rich\"."),
            TIP("Where this appears in the exam: Paper 1 asks you to name the law violated by an example, or to state a law. "
                "Paper 2 Section A may ask you to state the three laws with an example for each. "
                "Pick the law by testing: same meaning kept (identity), cannot both be true (non-contradiction), no third option (excluded middle)."),
            H("Worked examples"),
            EX("Worked example 1: which law is broken?", intro="Name the law broken in each case. "
               "(a) A witness says, \"I saw the thief, and I did not see the thief.\" "
               "(b) A speaker says, \"We must respect the law,\" then uses \"law\" to mean a rule of football in the first reason and a government law in the next. "
               "(c) A debater says, \"The statement is neither true nor false.\"", steps=[
                S("(a) Says something and its denial about the same event", text="The statement is p and not p at the same time and in the same respect. The law of **non-contradiction** is broken."),
                S("(b) The meaning of a term changes", text="The same word is used with two meanings in one argument. The law of **identity** is broken."),
                S("(c) A third possibility is claimed", text="A statement that is neither true nor false puts a middle between p and not p. The law of **excluded middle** is denied."),
            ]),
            EX("Worked example 2: contradiction or opposition?", intro="Are these pairs of statements contradictory? "
               "(a) \"Every farmer in the village grows maize.\" and \"No farmer in the village grows maize.\" "
               "(b) \"Every farmer in the village grows maize.\" and \"Some farmer in the village does not grow maize.\"", steps=[
                S("Test (a): can both be false?", text="Yes. If some farmers grow maize and some do not, both are false. So they are only opposed (contrary), not contradictory."),
                S("Test (b): can both be true? both false?", text="They cannot both be true, and they cannot both be false. If all grow maize, the second is false. If not all grow maize, the second is true."),
                S("Conclusion", text="Pair (b) is a contradictory pair. Pair (a) is not. The laws of non-contradiction and excluded middle apply to (b)."),
            ]),
            QUIZ("\"Either it is raining now or it is not raining now.\" Which law does this statement express?",
                 ["Identity", "Non-contradiction", "Excluded middle", "Sufficient reason"], 2,
                 "It states that p or not p, with no third option. That is the law of excluded middle.",
                 hint="Look at the pattern p or not p.",
                 feedback=["Identity says that a thing is itself, or that a term keeps its meaning.",
                           "Non-contradiction says p and not p cannot both be true. The sentence uses \"either...or\" with no claim about both being true.",
                           "",
                           "Sufficient reason says that everything has a reason, which is not stated here."]),
            QUIZ("\"The shop is open and the shop is not open, at this moment.\" What is wrong?",
                 ["It breaks the law of non-contradiction", "It breaks the law of excluded middle", "It breaks the law of identity", "Nothing is wrong"], 0,
                 "It says p and not p at the same time. The law of non-contradiction forbids this.",
                 hint="Can both parts be true together at the same moment?",
                 feedback=["",
                           "Excluded middle says that at least one of p and not p is true. The sentence does not deny this.",
                           "Identity is about meaning staying fixed. The problem here is two opposing claims at once.",
                           "Both parts cannot be true at once, so something is wrong."]),
            H("Practice"),
            PQ("State the three traditional laws of thought, each with a one-line example.",
               "Identity: a thing is what it is (the word \"bank\" keeps one meaning in an argument). "
               "Non-contradiction: nothing can both be and not be at the same time and in the same respect (a door cannot be open and closed now). "
               "Excluded middle: a statement is either true or false, with no third option (Either the market is open or it is not)."),
            PQ("Explain why \"All the girls passed\" and \"No girl passed\" do not break the law of non-contradiction when we say that both are false.",
               "These statements are contrary, not contradictory. They cannot both be true, but they can both be false (when some girls passed and some failed). "
               "The law of non-contradiction forbids only a statement and its true contradictory to both be true. "
               "The contradictory of \"All the girls passed\" is \"Some girl did not pass\"."),
            PQ("A student says: \"Either the policy is excellent or it is terrible, because of the law of excluded middle.\" Is the student correct? Explain.",
               "No. The law applies to a statement and its exact denial: the policy is excellent, or it is not excellent. "
               "\"Excellent\" and \"terrible\" are not contradictory, because a policy can be average, so the claimed choice is a false choice."),
            PQ("Mention one extra law that some textbooks add to the three laws of thought, and state it.",
               "The law of sufficient reason: everything that is true or that happens has a reason, and nothing should be accepted without a sufficient reason. "
               "Textbooks differ, so use the list in your own textbook."),
            SUM("The laws of thought are basic principles of clear thinking: identity, non-contradiction and excluded middle.",
                "Identity: a thing is itself, and terms keep their meaning in an argument.",
                "Non-contradiction: not both p and not p, in the same respect and at the same time.",
                "Excluded middle: either p or not p; no third option between a statement and its contradictory.",
                "Some books add the law of sufficient reason.",
                "Do not confuse contradictory pairs (cannot be both true or both false) with merely opposed or contrary pairs (may both be false)."),
        ],
    ),
    # ------------------------------------------------------------------ 1.1.5
    lesson(
        module=MODULE,
        topic="Operations of the mind",
        title="The three operations of the mind",
        slug="found-operations-of-the-mind",
        minutes=20,
        summary="Traditional logic describes three operations of the mind: simple apprehension (giving an idea, expressed as a term), judging (a proposition) and reasoning (an argument). The rest of the course follows these three.",
        objectives=[
            "Name the three operations of the mind and the product of each",
            "Explain how an idea, a term, a proposition and an argument are related",
            "Identify which operation a given example illustrates",
            "Explain how the modules of this course follow the three operations",
        ],
        key_concepts=["Simple apprehension", "Idea", "Term", "Judging", "Proposition", "Reasoning", "Argument"],
        blocks=[
            H("Introduction"),
            T("A girl at a market in Bafoussam sees a yellow fruit and thinks \"mango\". "
              "She touches it and says, \"This mango is ripe.\" "
              "She remembers that ripe mangoes are sweet, so she tells her friend, \"This mango will be sweet.\" "
              "In a few seconds her mind has done three different things."),
            T("Traditional logic describes the work of the mind in three steps, called the **three operations of the mind**. "
              "Each operation builds on the one before it. This map is also the plan of the whole Logic course."),
            H("The first operation: simple apprehension"),
            D("**Simple apprehension** is the mental act of grasping a thing, without saying anything about it. "
              "The product is an **idea** (a concept). When we put the idea into words, we get a **term**.",
              title="Definition: simple apprehension, idea, term",
              note="Examples: mango, teacher, justice, river. These are neither true nor false, because nothing is claimed."),
            T("\"Apprehension\" here means grasping with the mind. \"Simple\" means that we do not yet combine or compare anything: we only form the idea. "
              "A term can be one word (\"mango\") or several words (\"the oldest teacher in the school\")."),
            H("The second operation: judging"),
            D("**Judging** is the mental act of affirming or denying something about something else, that is, of joining or separating two ideas. "
              "The product is a **judgement**, and when it is put into words it is a **proposition** (a statement).",
              title="Definition: judging and proposition",
              note="Example: \"This mango is ripe\" joins the idea of this mango to the idea of being ripe."),
            T("A proposition is true or false. \"Mango\" alone is a term. \"Mangoes are fruits\" is a proposition. "
              "\"Mangoes are made of iron\" is also a proposition, because we say something that happens to be false."),
            H("The third operation: reasoning"),
            D("**Reasoning** is the mental act of moving from one or more known judgements to a new one that follows from them. "
              "The product is an **argument**: reasons (premises) and a conclusion put into words.",
              title="Definition: reasoning and argument",
              note="Example: \"Ripe mangoes are sweet. This mango is ripe. So this mango is sweet.\""),
            IMG("f5l-found-three-operations.svg",
                alt="Three boxes in a row for the operations of the mind: simple apprehension giving an idea or term (example mango), judging giving a proposition (example this mango is ripe), and reasoning giving an argument (example ripe fruit is sweet, this mango is ripe, so it is sweet).",
                caption="Figure 1. The three operations of the mind and what each produces. Each product is built from the one before it."),
            T("In the diagram, notice how the products build on each other. "
              "An argument is made of propositions. A proposition is made of terms. "
              "So we study the simplest unit first (terms), then propositions, then arguments."),
            KEY("The three operations at a glance", "Learn this chain.", cards=[
                ["Operation 1: simple apprehension", "In the mind: an idea. In words: a term. Not true or false."],
                ["Operation 2: judging", "In the mind: a judgement. In words: a proposition. True or false."],
                ["Operation 3: reasoning", "In the mind: an inference. In words: an argument. Valid or invalid (and sound or unsound)."],
            ]),
            H("How the rest of the course follows these operations"),
            T("The modules after this one follow the same order. "
              "The first operation leads to the study of terms (their properties and kinds), and then to definitions and logical division, which help us make our ideas and words clear. "
              "The second operation leads to the study of propositions: categorical propositions, hypothetical and disjunctive propositions, and an introduction to symbolic logic. "
              "The third operation leads to inference and arguments: opposition, syllogisms, other types of arguments such as the dilemma, and fallacies, which are faulty arguments."),
            MISTAKE("Mixing up a term and a proposition",
                    "A term is not true or false. \"A red car\" is a term. \"The car is red\" is a proposition. "
                    "A quick test: can you reply \"That is true\" or \"That is false\"? If yes, it is a proposition."),
            TIP("Where this appears in the exam: Paper 1 often gives an example and asks which operation or which product it is (idea, term, proposition, argument). "
                "Paper 2 Section A may ask you to name and define the three operations. "
                "Test: single word or phrase naming something, term; true-or-false statement, proposition; reasons plus conclusion, argument."),
            H("Worked examples"),
            EX("Worked example 1: name the operation", intro="Which operation of the mind does each example illustrate? "
               "(a) A child forms the idea of a goat. (b) A teacher says, \"Our school has a library.\" "
               "(c) \"All birds have wings. A hen is a bird. So a hen has wings.\"", steps=[
                S("(a) Forming an idea", text="The child grasps what a goat is without saying anything about it. This is **simple apprehension**."),
                S("(b) Affirming something about something", text="\"Our school has a library\" is a true-or-false statement. This is **judging**; its product is a proposition."),
                S("(c) Reasons and a conclusion", text="Two reasons lead to a conclusion. This is **reasoning**; its product is an argument."),
            ]),
            EX("Worked example 2: term, proposition or argument?", intro="Classify each: (a) \"the new bridge over the Wouri\" (b) \"The new bridge is open.\" "
               "(c) \"The bridge is open, so traffic will move faster.\"", steps=[
                S("(a)", text="It names something but says nothing true or false about it. It is a **term**."),
                S("(b)", text="It affirms something and can be true or false. It is a **proposition**."),
                S("(c)", text="It gives a reason (the bridge is open) and a conclusion (traffic will move faster). It is an **argument**."),
            ]),
            QUIZ("Which of the following is a proposition?",
                 ["Cocoa farmers", "Cocoa farmers of Mbalmayo", "Cocoa farmers are hard-working", "Hard-working cocoa farmers"], 2,
                 "\"Cocoa farmers are hard-working\" affirms something about cocoa farmers, so it is true or false.",
                 hint="Which one can you answer with \"true\" or \"false\"?",
                 feedback=["It names a group. It is a term, which is neither true nor false.",
                           "It names a more specific group. It is still only a term.",
                           "",
                           "It is a noun phrase naming a group. It is a term, not a statement."]),
            QUIZ("\"Every student must wear a uniform. Tabi is a student. So Tabi must wear a uniform.\" This is an example of...",
                 ["Simple apprehension", "Judging", "Reasoning", "A term"], 2,
                 "Reasons lead to a conclusion. This is reasoning, and in words it is an argument.",
                 hint="Count the statements. Is there a reason and a conclusion?",
                 feedback=["Simple apprehension gives only an idea, with no statement.",
                           "Judging gives one proposition. This example has three propositions joined by reasoning.",
                           "",
                           "A term is a word or phrase. This example is a set of sentences."]),
            H("Practice"),
            PQ("Name the three operations of the mind and the product of each.",
               "Simple apprehension, which produces an idea (expressed as a term). Judging, which produces a judgement (expressed as a proposition). Reasoning, which produces an inference (expressed as an argument)."),
            PQ("Explain the difference between a term and a proposition, with one example of each.",
               "A term is a word or group of words that names an idea. It is neither true nor false. Example: \"school fees\". "
               "A proposition affirms or denies something and is true or false. Example: \"School fees are paid in the first term.\""),
            PQ("Explain how an argument is related to propositions and terms.",
               "An argument is made of propositions (the reasons and the conclusion). Each proposition is made of terms. "
               "So terms are the simplest building blocks, propositions are built from terms, and arguments are built from propositions."),
            PQ("Say which operation is being used: \"Because all trained nurses have passed the exam, and Mary has not passed the exam, I conclude that Mary is not a trained nurse.\" Give a reason.",
               "Reasoning. A conclusion is drawn from two reasons, so the product is an argument."),
            SUM("Traditional logic describes three operations of the mind.",
                "Simple apprehension gives an idea, put into words as a term. A term is neither true nor false.",
                "Judging gives a judgement, put into words as a proposition. A proposition is true or false.",
                "Reasoning gives an inference, put into words as an argument. An argument is valid or invalid.",
                "Terms build propositions and propositions build arguments.",
                "The rest of the Logic course follows this order: terms, propositions, then inference and arguments."),
        ],
    ),
]
