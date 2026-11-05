"""Form 5 Logic: Informal Fallacies (7 lessons, one practice set each)."""

from .dsl import *  # noqa: F403

COURSE = ("logic", "form-5")

MODULE = "Informal Fallacies"
T1 = "Definition, classification and significance of fallacies"
T2 = "Fallacies of relevance: fallacies of no evidence"
T3 = "Fallacies of relevance: fallacies of little evidence"
T4 = "Fallacies of ambiguity"

LESSONS = []

# ------------------------------------------------------------------ 1. What are fallacies
LESSONS.append(lesson(
    module=MODULE, topic=T1,
    title="What fallacies are and how we classify them",
    slug="fal-what-are-fallacies",
    minutes=20,
    summary="A fallacy is a mistake in reasoning that looks convincing. This lesson separates formal from informal fallacies, shows why fallacies persuade, gives the three groups used in this course and shows how to challenge a fallacy politely.",
    objectives=[
        "Define a fallacy and distinguish formal from informal fallacies",
        "Explain why fallacies often persuade people",
        "Name the three groups of informal fallacies used in this course",
        "Challenge a fallacious argument politely and clearly",
    ],
    key_concepts=["Fallacy", "Formal fallacy", "Informal fallacy", "Relevance", "Ambiguity", "Classification"],
    blocks=[
        H("Introduction"),
        T("At the market in Mokolo, a seller says: 'Everybody in this town buys my soap, so it must be good.' The sentence sounds "
          "strong. But the fact that many people buy something does not prove that it is good. The seller has made a mistake in reasoning "
          "that looks like a good reason."),
        T("Logic gives such mistakes a name and teaches us to spot them. This lesson explains what a fallacy is, how fallacies are "
          "sorted into groups, and why this skill matters in school, at home and at work."),
        D("An **argument** is a group of statements in which some statements (the **premises**) are offered as reasons for another "
          "statement (the **conclusion**).", title="Argument"),
        D("A **fallacy** is a mistake in reasoning: an argument that seems to support its conclusion but does not support it as well as it appears to.",
          title="Fallacy"),
        H("Formal and informal fallacies"),
        D("A **formal fallacy** is a mistake in the FORM (the pattern) of an argument. You can find it without knowing what the words mean.",
          title="Formal fallacy"),
        T("Here is a formal fallacy. 'If it rains, the road is wet. The road is wet. So it rained.' In symbols: p ⊃ q, q, therefore p. "
          "This pattern is called **affirming the consequent**. It is invalid. The road can be wet because a lorry washed it. "
          "The pattern fails whatever p and q stand for."),
        D("An **informal fallacy** is a mistake in the CONTENT of an argument: its meaning, its relevance or the amount of evidence. "
          "You find it by thinking about what the statements say, not only about their pattern.", title="Informal fallacy"),
        T("This module is about informal fallacies. Earlier modules (the syllogism and the dilemma) dealt with form."),
        H("Why fallacies persuade"),
        T("If fallacies were obvious, nobody would use them. They persuade for four common reasons. They appeal to feelings such as "
          "fear, pity or pride. They look like a good argument because the premises seem related to the conclusion. They use words "
          "with more than one meaning. And they are often said with confidence, by someone we like or respect."),
        KEY("Remember", "A fallacy can have true premises and even a true conclusion. The fault is that the premises do not give enough "
            "reason for the conclusion.", cards=[
                ["A true conclusion is possible", "A conclusion can be true even when the argument for it is bad."],
                ["Bad reasoning is not bad character", "A fallacy is a fault in the argument. It does not prove that the speaker is dishonest."],
            ]),
        H("Classification: the three groups used in this course"),
        T("The GCE Board lists three groups: fallacies of relevance with **no evidence**, fallacies of relevance with **little evidence**, "
          "and fallacies of **ambiguity**. These headings are the Board's own. Textbooks such as Copi and Hurley use other headings "
          "(for example 'relevance', 'weak induction', 'presumption' and 'ambiguity'). So a few fallacies are placed in a different group "
          "in your textbook. Where this can happen, the lesson says **check your textbook**."),
        IMG("f5l-fal-classification.svg",
            alt="Tree: Fallacies split into formal and informal; informal splits into no evidence, little evidence and ambiguity",
            caption="Figure 1. The groups used in this course."),
        KEY("The three groups", "How this course uses the Board's labels.", cards=[
            ["No evidence", "The premises offer no real evidence for the conclusion. Examples: appeal to force, argument against the person, straw man, begging the question."],
            ["Little evidence", "The premises give some evidence, but far too little. Examples: hasty generalization, false cause, weak analogy."],
            ["Ambiguity", "A word, phrase or sentence changes meaning in the argument. Examples: equivocation, amphiboly, accent."],
        ]),
        H("Why this matters"),
        T("Fallacies are everywhere: in advertisements, in football arguments, in family discussions and in the news. Knowing them helps you "
          "in three ways. You make better decisions, for example when you choose a school, a phone or a business partner. You are harder "
          "to trick. And you write clearer arguments in your own essays and exams."),
        H("How to challenge a fallacy politely"),
        KEY("Four steps", "Attack the reasoning, never the person.", cards=[
            ["1. Listen", "Find the conclusion and the reason given for it."],
            ["2. Name the gap", "Say what is missing: 'Your reason is about X, but your conclusion is about Y.'"],
            ["3. Ask a question", "'What evidence shows that?' is gentler than 'You are wrong.'"],
            ["4. Offer a repair", "Say what evidence WOULD support the conclusion."],
        ]),
        EX("Worked example: spot and challenge", intro="A student says: 'My cousin failed the mathematics exam after he bought a new pen. So new pens cause failure.' How do you respond?", steps=[
            S("Find the conclusion", text="New pens cause failure in mathematics."),
            S("Find the reason", text="One event (the pen) came before another (the failure)."),
            S("Name the gap", text="Coming before is not the same as causing. This is the fallacy of false cause (post hoc), taught in a later lesson."),
            S("Challenge politely", text="'Many students use new pens and pass. What else could explain your cousin's result, for example how much he revised?'"),
        ]),
        MISTAKE("Calling every weak argument a fallacy", "Not every disagreement is a fallacy. First check that the argument really fails to support its conclusion. Then name the exact fallacy."),
        MISTAKE("Thinking a fallacy makes the conclusion false", "A fallacious argument does not prove its conclusion, but the conclusion may still be true. Say 'this reason is not enough', not 'you are wrong'."),
        TIP("Paper 1 asks you to name the fallacy in a short passage. Paper 2 may ask you to define 'fallacy', distinguish formal from informal fallacies, and "
            "identify and explain fallacies in a passage. Always give the name, then the reason.", title="Exam link"),
        QUIZ("Which of these is an INFORMAL fallacy?", [
            "An argument whose pattern is invalid, whatever the words mean",
            "An argument that uses a word in two different meanings",
            "An argument with a false conclusion",
            "An argument with three premises",
        ], 1, "A shift in the meaning of a word depends on content, so it is informal.",
            hint="Informal fallacies depend on what the words mean.",
            feedback=["That describes a formal fallacy.", "", "A fallacy can have a true conclusion. Truth or falsity of the conclusion is not the test.", "The number of premises does not decide whether an argument is fallacious."]),
        QUIZ("'Everybody buys it, so it must be good' is best described as", [
            "a formal fallacy only",
            "a mistake because the reason does not support the conclusion",
            "a good argument because it has a premise",
            "a true statement about the market",
        ], 1, "Popularity is a reason about what people do, not about quality. The premise does not give enough support.",
            hint="Does the number of buyers show the quality of the soap?",
            feedback=["It is not a matter of form.", "", "Having a premise does not make the argument good.", "We are judging the reasoning, not whether people really buy it."]),
        PQ("Define 'fallacy' and give one difference between a formal and an informal fallacy.",
           "A fallacy is a mistake in reasoning: an argument that seems to support its conclusion but does not. A formal fallacy is a fault in the pattern of the argument (for example affirming the consequent), found without knowing the meaning of the words. An informal fallacy is a fault in content, such as meaning or relevance."),
        PQ("Give two reasons why fallacies persuade people.",
           "Any two of: they appeal to feelings such as fear or pity; they look related to the conclusion; they use words with more than one meaning; they are said with confidence by someone people trust."),
        PQ("'If the school is closed, there are no lessons. There are no lessons. So the school is closed.' Is this a formal or an informal fallacy? Give the name and say why.",
           "It is a formal fallacy: affirming the consequent (p ⊃ q, q, so p). The pattern is invalid because there are other reasons why lessons may not hold, for example a teachers' meeting."),
        SUM("A fallacy is a mistake in reasoning that looks like good reasoning.",
            "A formal fallacy is a fault in the pattern; an informal fallacy is a fault in content such as meaning, relevance or amount of evidence.",
            "Fallacies persuade through feelings, resemblance to good arguments, ambiguous words and confident speakers.",
            "This course groups informal fallacies as no evidence, little evidence and ambiguity. Textbooks group them differently: check your textbook.",
            "Challenge a fallacy by naming the gap and asking for evidence, not by attacking the person."),
    ],
))

# ------------------------------------------------------------------ 2. No evidence: appeals
LESSONS.append(lesson(
    module=MODULE, topic=T2,
    title="No evidence I: appeals to force, pity, the people and the person",
    slug="fal-no-evidence-appeals",
    minutes=22,
    summary="Four fallacies that give no real evidence for a conclusion: appeal to force, appeal to pity, appeal to the people (popularity) and argument against the person (abusive, circumstantial and tu quoque).",
    objectives=[
        "Define appeal to force, appeal to pity and appeal to the people",
        "Define argument against the person and separate its three kinds",
        "Identify each fallacy in an everyday passage",
        "Say when a similar appeal is NOT a fallacy",
    ],
    key_concepts=["Appeal to force", "Appeal to pity", "Appeal to the people", "Argument against the person", "Abusive", "Circumstantial", "Tu quoque"],
    blocks=[
        H("Introduction"),
        T("Two friends argue about which football team is better. One says: 'Say that my team is better, or I will not lend you my bicycle.' "
          "The bicycle has nothing to do with football. The speaker gives you a reason to SAY something, not a reason to BELIEVE it."),
        T("This is the first group of fallacies of relevance. The Board calls it **fallacies of no evidence**: the premises give no real "
          "evidence for the conclusion. Textbooks group the fallacies differently, so the group names here follow the Board's headings only."),
        D("A **fallacy of relevance** is an argument whose premises are not logically relevant to the conclusion, "
          "although they may move our feelings or attention.", title="Fallacy of relevance"),
        H("Appeal to force (argumentum ad baculum)"),
        D("**Appeal to force** uses a threat of harm, or a hint of one, in place of evidence that the conclusion is true.",
          title="Appeal to force"),
        T("Example: 'You must agree that my plan for the class party is the best. If you do not, some of the older students "
          "will remember it.' A threat can make people keep quiet. It cannot make a claim true."),
        H("Appeal to pity (argumentum ad misericordiam)"),
        D("**Appeal to pity** uses sympathy for a person as if it were evidence for a claim.", title="Appeal to pity"),
        T("Example: 'Madam, please mark my answer as correct. I have had a very hard year and my family is struggling.' "
          "We may feel sorry for the student. But the feeling is not evidence that the answer is correct."),
        TIP("Pity can be a good reason to be kind, for example to give extra time or to forgive a fine. It becomes a fallacy only "
            "when sympathy is used to show that a claim is TRUE.", title="Not always a fallacy"),
        H("Appeal to the people (argumentum ad populum)"),
        D("**Appeal to the people** (the bandwagon) argues that something is true or good because many people believe it or do it.",
          title="Appeal to the people"),
        T("Example: 'Most of the class bought this brand of exercise book, so it must be the best.' How many people choose "
          "something shows what is popular. It does not show what is true or best. Popular opinion has been wrong many times."),
        H("Argument against the person (argumentum ad hominem)"),
        D("An **argument against the person** rejects a claim by attacking the person who makes it, not the reasons the person gives.",
          title="Argument against the person"),
        T("It has three standard kinds."),
        KEY("Three kinds", "Each one attacks the speaker, not the argument.", cards=[
            ["Abusive", "Insults the person. 'You are too young to know anything about farming, so your advice on the maize is wrong.'"],
            ["Circumstantial", "Points to the person's situation or interests. 'Of course the pharmacist says to take this medicine. She sells it.'"],
            ["Tu quoque ('you too')", "Says the person does not follow their own advice. 'You tell me to be on time, but you were late yesterday.'"],
        ]),
        T("In each case the question stays open. Is the farming advice good? Is the medicine suitable? Is being on time a good rule? "
          "The attack on the person does not answer it."),
        MISTAKE("Rejecting every attack on a person",
                "If a witness's honesty or interest really matters to how far we can trust what they say, questioning it is reasonable. "
                "It is a fallacy when the attack is used to say that the claim itself is false, without looking at the reasons."),
        EX("Worked example 1: name the fallacy", intro="A teacher says: 'Smoking harms health.' A student replies: 'You smoked in your youth, so why should I listen to you?' Which fallacy is this?", steps=[
            S("Find the claim", text="Smoking harms health."),
            S("Find the reply", text="The student attacks the teacher's own past behaviour, not the claim."),
            S("Name it", text="Argument against the person, kind: tu quoque. The teacher's past habit does not make the claim false."),
        ]),
        EX("Worked example 2: separate three arguments", intro="Which of these is an appeal to pity, which an appeal to the people and which an appeal to force? (a) 'Everyone in the village trusts this healer, so the remedy works.' (b) 'Agree with me or you will have no friends in this school.' (c) 'Buy my tomatoes at this price, please. My children have not eaten.'", steps=[
            S("(a)", text="Appeal to the people: the reason is how many trust the healer."),
            S("(b)", text="Appeal to force: a threat, not evidence."),
            S("(c)", text="Appeal to pity: sympathy for the seller, not a reason about the quality or price."),
        ]),
        TIP("Paper 1 usually gives a short passage and asks you to name the fallacy. Ask: what reason is given, and does it really have to do with the claim? "
            "In Paper 2 you may be asked to define the fallacy, name it and explain why it is a fallacy.", title="Exam link"),
        QUIZ("'You say we should save money, but you spent a lot on your phone, so we will ignore your advice.' This is", [
            "appeal to force",
            "appeal to pity",
            "argument against the person (tu quoque)",
            "appeal to the people",
        ], 2, "The reply attacks the speaker's conduct. It does not say whether saving money is a good idea.",
            hint="Whose behaviour is being attacked?",
            feedback=["There is no threat.", "Nobody asks for sympathy.", "", "Nobody says that many people think so."]),
        QUIZ("A seller says: 'This radio is the best because everybody in the neighbourhood owns one.' This is", [
            "argument against the person",
            "appeal to force",
            "appeal to pity",
            "appeal to the people",
        ], 3, "The reason is popularity. Many owners show that it is common, not that it is the best.",
            hint="What is the reason: a threat, a feeling of sorrow, an attack, or a count of people?",
            feedback=["Nobody is attacked.", "No threat.", "No sorrow story.", ""]),
        PQ("Define 'appeal to force' and give an example of your own.",
           "Appeal to force uses a threat in place of evidence that a claim is true. Example: 'Agree that the match was unfair or you will not be invited to my party.' The threat gives no reason to think the match was unfair."),
        PQ("A speaker says: 'Do not believe the report on road safety. The author was once fined for speeding.' Name the fallacy and explain.",
           "Argument against the person (abusive or tu quoque, depending on the speaker's aim). The author's fine does not show that the report's evidence is wrong. The report should be judged by its facts."),
        PQ("Give one situation in which pity is NOT a fallacy.",
           "When pity is a reason for kindness or mercy, not for the truth of a claim: for example, giving a student with a broken arm extra time to write. The pity is relevant to the decision about extra time, not used to prove that an answer is correct."),
        SUM("Fallacies of no evidence give no real evidence for the conclusion.",
            "Appeal to force uses a threat; appeal to pity uses sympathy; appeal to the people uses popularity.",
            "An argument against the person attacks the speaker, not the reasons. Its kinds are abusive, circumstantial and tu quoque.",
            "A feeling, a threat, a crowd or a fault in the speaker can matter in other ways, but they do not show that a claim is true.",
            "The Board's group names differ from textbook headings: check your textbook."),
    ],
))

# ------------------------------------------------------------------ 3. No evidence: diversions and begging
LESSONS.append(lesson(
    module=MODULE, topic=T2,
    title="No evidence II: straw man, red herring, begging the question and complex question",
    slug="fal-no-evidence-diversions-and-begging-the-question",
    minutes=22,
    summary="Four more fallacies: the straw man and the red herring (missing the point) divert from the real issue; begging the question assumes what it must prove; the complex question hides an unproved assumption inside a question.",
    objectives=[
        "Define straw man, red herring, begging the question and complex question",
        "Distinguish a straw man from a red herring",
        "Spot an argument that goes in a circle",
        "Answer a complex question without accepting its hidden assumption",
    ],
    key_concepts=["Straw man", "Red herring", "Missing the point", "Begging the question", "Circular argument", "Complex question"],
    blocks=[
        H("Introduction"),
        T("In a family meeting, one person says: 'I think we should spend less on weddings.' Another replies: 'So you want us to "
          "never celebrate anything!' That is not what was said. The answer attacks a position that nobody holds."),
        T("This lesson continues the Board's group **fallacies of no evidence**. The first two fallacies change the subject. The last two "
          "hide an assumption. In some textbooks begging the question and complex question belong to another group called presumption: **check your textbook**."),
        H("Straw man"),
        D("The **straw man** fallacy distorts someone's position (making it weaker, simpler or more extreme) and then attacks the distorted version, "
          "as if it were the real position.", title="Straw man"),
        T("Example: Ama says: 'Homework should be shorter on Fridays.' Kofi replies: 'Ama thinks students should do no work at all. "
          "That would be a disaster.' Kofi has attacked a position Ama does not hold."),
        H("Red herring and missing the point"),
        D("A **red herring** introduces a different topic to draw attention away from the real issue. The name comes from the image of a strong smell "
          "drawing hunters or dogs off the trail.", title="Red herring"),
        D("**Missing the point** (irrelevant conclusion) is an argument whose premises support one conclusion but a different conclusion is drawn.",
          title="Missing the point"),
        T("Example of a red herring: asked why the exam fees were increased, a leader replies: 'Look at the great new library we built.' "
          "The library may be good. It does not explain the fees."),
        KEY("Straw man or red herring?", "A quick test.", cards=[
            ["Straw man", "The reply attacks a distorted version of YOUR claim."],
            ["Red herring", "The reply drops your claim and talks about something else."],
        ]),
        H("Begging the question (petitio principii)"),
        D("**Begging the question** is an argument in which the conclusion is assumed in the premises. The argument goes in a circle.",
          title="Begging the question"),
        T("Example: 'Our school is the best, because no school is better than ours.' The reason only repeats the claim in other words. "
          "Another example: 'The rule is fair because it is a just rule.' 'Fair' and 'just' mean nearly the same."),
        TIP("To test for circularity, ask: could someone who doubts the conclusion accept the premise? If not, the premise already assumes the conclusion.", title="Test"),
        H("Complex question"),
        D("A **complex question** is a question that contains a hidden, unproved assumption. Any direct answer seems to accept it.",
          title="Complex question"),
        T("Example: 'Have you stopped copying homework?' If you answer yes, you admit you copied before. If you answer no, you say you still copy. "
          "The question assumes you did copy. Good reply: 'I have not copied homework, so the question does not apply.'"),
        EX("Worked example 1: straw man", intro="Person A: 'The town council should plant more trees along the main road.' Person B: 'A wants to cut down the market and turn the town into a forest.' Which fallacy is this, and why?", steps=[
            S("A's position", text="Plant more trees along the main road."),
            S("B's version", text="Destroy the market for a forest: far more extreme."),
            S("Name it", text="Straw man. B attacks a distorted position, so A's real reasons are left unanswered."),
        ]),
        EX("Worked example 2: circular argument", intro="'Honest people always tell the truth, because it is part of being honest.' Is this a good argument?", steps=[
            S("Conclusion", text="Honest people always tell the truth."),
            S("Premise", text="Telling the truth is part of being honest."),
            S("Compare", text="The premise says almost the same as the conclusion. Nothing new is offered."),
            S("Verdict", text="It begs the question. We need independent reasons or evidence."),
        ]),
        MISTAKE("Calling any repeated statement circular", "Repeating a point for emphasis is not always begging the question. The fallacy is when the repetition is offered AS the proof."),
        MISTAKE("Answering a complex question directly", "A plain yes or no accepts the hidden assumption. First reject the assumption, then answer."),
        TIP("In Paper 1, a passage with a question such as 'Have you stopped...?' or 'Why did you...?' is often a complex question. A passage that "
            "changes the subject is a red herring or missing the point. Paper 2 may ask you to define and illustrate two of these.", title="Exam link"),
        QUIZ("Asked about the high price of tomatoes, a seller says: 'Why are you looking at tomatoes? Look at my fine onions.' This is", [
            "a straw man",
            "a red herring",
            "begging the question",
            "a complex question",
        ], 1, "The seller drops the issue (the price) and turns to another topic (onions).",
            hint="Is the claim distorted, or is the topic changed?",
            feedback=["The customer's claim is not distorted.", "", "No premise repeats a conclusion.", "No question hides an assumption."]),
        QUIZ("Which question is a complex question?", [
            "Did you pass the mathematics test?",
            "Why did you steal the pencil?",
            "What time does the bus leave?",
            "Is the school open on Saturday?",
        ], 1, "It assumes the person stole the pencil, which has not been shown.",
            hint="Which question assumes something that has not been proved?",
            feedback=["It asks plainly.", "", "No hidden assumption.", "No hidden assumption."]),
        PQ("Distinguish a straw man from a red herring.",
           "A straw man replaces the opponent's real position with a distorted one and attacks that. A red herring changes the subject and does not attack any version of the position."),
        PQ("'Prayer is useful because praying always helps people.' Which fallacy? Explain.",
           "Begging the question (circular). 'Useful' and 'always helps' mean almost the same, so the premise assumes the conclusion. Independent evidence would be needed."),
        PQ("Reply to 'Have you stopped being rude to your neighbours?' without accepting the hidden assumption.",
           "The question is a complex question that assumes you were rude. A good reply: 'I have not been rude to my neighbours, so there is nothing to stop.'"),
        SUM("A straw man attacks a distorted version of an opponent's claim.",
            "A red herring changes the subject; missing the point draws a conclusion that the premises do not support.",
            "Begging the question assumes the conclusion in the premises, going in a circle.",
            "A complex question hides an unproved assumption; reject the assumption before you answer.",
            "Begging the question and complex question are placed under presumption in some textbooks: check your textbook."),
    ],
))

# ------------------------------------------------------------------ 4. Little evidence: generalisations, causes
LESSONS.append(lesson(
    module=MODULE, topic=T3,
    title="Little evidence I: hasty generalization, false cause and slippery slope",
    slug="fal-little-evidence-generalisations-and-causes",
    minutes=22,
    summary="Three fallacies in which the premises give some evidence but far too little: hasty generalization from too few cases, false cause (post hoc) and the slippery slope.",
    objectives=[
        "Define hasty generalization, false cause (post hoc) and slippery slope",
        "Explain why a small or unrepresentative sample is weak evidence",
        "Distinguish a real cause from a coincidence or a later event",
        "Say what extra evidence would repair each argument",
    ],
    key_concepts=["Hasty generalization", "Sample", "False cause", "Post hoc ergo propter hoc", "Slippery slope"],
    blocks=[
        H("Introduction"),
        T("A traveller spends one night in a town and the taxi driver is rude. She says: 'Taxi drivers in this town are rude.' "
          "She has some evidence: one driver. But one case is far too little for a statement about all the drivers of a town."),
        T("This is the second group in the Board's headings: **fallacies of little evidence**. Here the premises DO give some support. "
          "The fault is that the support is too weak for the conclusion drawn. Textbooks use other headings (Hurley calls most of them weak induction), "
          "so some of these fallacies sit elsewhere in your book. **Check your textbook.**"),
        H("Hasty generalization"),
        D("A **generalization** is a statement about all or most members of a group, based on some of them. "
          "A **sample** is the part of the group that we actually look at.", title="Generalization and sample"),
        D("A **hasty generalization** (converse accident) draws a general conclusion from a sample that is too small or not "
          "representative of the whole group.", title="Hasty generalization"),
        T("Two things can go wrong. The sample may be **too small**: two students from one class say the new timetable is bad. "
          "Or it may be **unrepresentative**: asking only the players of a team whether the football field is good."),
        KEY("Questions to ask", "How good is the sample?", cards=[
            ["How many?", "Is the number large enough for the size of the group?"],
            ["Which ones?", "Were the cases chosen fairly, or only the easy or extreme ones?"],
        ]),
        H("False cause"),
        D("The fallacy of **false cause** claims that one thing causes another without good evidence for a causal link.",
          title="False cause"),
        D("**Post hoc ergo propter hoc** (Latin: 'after this, therefore because of this') is the false cause that treats an event that came "
          "first as the cause of the event that followed.", title="Post hoc"),
        T("Example: 'The cock crowed and the sun rose, so the cock made the sun rise.' Or: 'Since the new principal arrived, the "
          "river has flooded twice. So the principal caused the flooding.' Something happening before is not enough."),
        T("Other false causes: **coincidence** (two things happen together by chance) and **common cause** (both are caused by a third thing). "
          "Ice cream sales and drowning cases both rise in hot months, but the heat, not ice cream, is the common cause."),
        H("Slippery slope"),
        D("A **slippery slope** argument says that one small step will start a chain of events ending in a terrible result, "
          "without showing that each step really follows.", title="Slippery slope"),
        T("Example: 'If we let students wear sandals on Friday, soon they will not wear uniform at all, and then the school will have no discipline.' "
          "Each link in the chain needs evidence. Without it, the fear does the work that reasons should do."),
        MISTAKE("Rejecting every cause-and-effect claim", "Some events that follow others ARE caused by them. Look for evidence of a link: repeated cases, a mechanism, "
                "and the absence of other likely causes."),
        MISTAKE("Calling every warning a slippery slope", "A warning is reasonable when each step is likely and shown. It is a fallacy only when the chain is assumed without support."),
        EX("Worked example 1: sample", intro="'I asked three students on the school bus, and all said the school canteen is too expensive. So all students think so.' Evaluate this.", steps=[
            S("Conclusion", text="All students think the canteen is too expensive."),
            S("Evidence", text="Three students, all from one bus."),
            S("Problem", text="Three is very small and the bus group may not represent the school."),
            S("Name it", text="Hasty generalization. A fairer survey would ask students at random from every class."),
        ]),
        EX("Worked example 2: false cause", intro="'After our team changed its jerseys, we lost three matches. The new jerseys make us lose.' Evaluate this.", steps=[
            S("Pattern", text="The jersey change came first. The losses followed."),
            S("Other causes", text="An injured goalkeeper, stronger opponents, fewer practices."),
            S("Name it", text="False cause (post hoc). To support the claim, compare matches with the old and new jerseys while other things stay equal."),
        ]),
        TIP("Fallacies of this group often appear in Paper 1 as short everyday statements. Look for the words 'so', 'therefore' and 'because' and ask whether the reason is enough. "
            "In Paper 2 you may be asked to define, give an example and explain why it is fallacious.", title="Exam link"),
        QUIZ("'The first two nurses I met at the clinic were unfriendly, so nurses are unfriendly.' This is", [
            "hasty generalization",
            "slippery slope",
            "begging the question",
            "appeal to force",
        ], 0, "Two cases are far too few for a statement about all nurses.",
            hint="What size is the sample compared with the whole group?",
            feedback=["", "No chain of results is predicted.", "The premise does not repeat the conclusion.", "No threat."]),
        QUIZ("'Rainfall dropped after the new mast was built, so the mast stopped the rain.' The best criticism is that", [
            "the premise is false",
            "something coming before another event does not show that it caused it",
            "the conclusion is too long",
            "the speaker attacks the person",
        ], 1, "Order in time is not enough to show a cause. This is post hoc.",
            hint="Think of the Latin name 'after this, therefore because of this'.",
            feedback=["The premise may be true. The fault is the link.", "", "Length does not decide.", "No person is attacked."]),
        PQ("Define 'hasty generalization' and say what makes a sample weak.",
           "A hasty generalization draws a general conclusion from too few or unrepresentative cases. A sample is weak when it is too small or when it was chosen unfairly, for example only from one place or one kind of person."),
        PQ("'If the government allows one new market stall tax, soon it will tax everything and the economy will collapse.' Name the fallacy and say what is missing.",
           "Slippery slope. It claims a chain of results without showing that each step is likely. Evidence is needed for every link, for example reasons why one tax would lead to the next."),
        PQ("Explain 'post hoc ergo propter hoc' with an example.",
           "It means 'after this, therefore because of this': assuming that an earlier event caused a later one. Example: 'I wore my green shirt and then I won the game, so the shirt made me win.' The order of events is not evidence of cause."),
        SUM("Fallacies of little evidence give some support, but far too little.",
            "Hasty generalization uses a sample that is too small or not representative.",
            "False cause takes order or coincidence for cause; post hoc is 'after this, therefore because of this'.",
            "Slippery slope predicts a chain of disasters without evidence for each link.",
            "Where these fallacies sit in your textbook can differ: check your textbook."),
    ],
))

# ------------------------------------------------------------------ 5. Little evidence: analogies, authority, ignorance
LESSONS.append(lesson(
    module=MODULE, topic=T3,
    title="Little evidence II: weak analogy, unqualified authority, appeal to ignorance and false dichotomy",
    slug="fal-little-evidence-analogies-authority-and-ignorance",
    minutes=23,
    summary="Four more fallacies of little evidence: a weak analogy, citing an unqualified authority, an appeal to ignorance and a false dichotomy that offers only two options.",
    objectives=[
        "Define weak analogy, appeal to unqualified authority, appeal to ignorance and false dichotomy",
        "Decide whether an analogy is strong or weak",
        "Tell when relying on an authority is reasonable",
        "Find a third option in a false dichotomy",
    ],
    key_concepts=["Analogy", "Weak analogy", "Authority", "Appeal to ignorance", "False dichotomy", "Burden of proof"],
    blocks=[
        H("Introduction"),
        T("A family chooses a school. The father says: 'A man we know who sells phones says this school is best.' He may know phones. "
          "Does he know schools? The advice has some value, but not much for this decision."),
        T("This lesson finishes the Board's group of fallacies of little evidence. As before, textbooks sort them differently: appeal to ignorance "
          "and authority, for example, may sit under relevance in one book and under weak induction in another, and false dichotomy is often called a fallacy of presumption. **Check your textbook.**"),
        H("Weak analogy"),
        D("An **analogy** compares two things and says that because they are alike in some ways, they are alike in another way too.",
          title="Analogy"),
        D("A **weak analogy** is an argument from analogy in which the things compared differ in important respects, so the comparison gives little support.",
          title="Weak analogy"),
        T("Example: 'A school is like a business. A business must make a profit, so a school must make a profit.' "
          "A school and a business are alike in having staff and budgets. They differ in the very point that matters: their main purpose."),
        KEY("Testing an analogy", "Three questions.", cards=[
            ["Similar?", "Are the two things alike in ways that matter for the conclusion?"],
            ["Different?", "Is there an important difference that breaks the link?"],
            ["Enough?", "Do many similarities support the conclusion, or only one?"],
        ]),
        H("Appeal to unqualified authority (argumentum ad verecundiam)"),
        D("**Appeal to unqualified authority** supports a claim by citing a person who has no real expertise in the subject, "
          "or who is not reliable on it.", title="Unqualified authority"),
        T("Example: 'A famous footballer says this herbal drink cures malaria, so it does.' Skill at football is not expertise in medicine."),
        T("Appeal to authority is not always a fallacy. We often rely on doctors, engineers and teachers. An appeal is reasonable when "
          "the person is an expert in the right field, the experts agree, and the person is not biased."),
        H("Appeal to ignorance (argumentum ad ignorantiam)"),
        D("**Appeal to ignorance** argues that a claim is true because no one has proved it false, or false because no one has proved it true.",
          title="Appeal to ignorance"),
        T("Example: 'Nobody has proved that there is no gold under this field, so there is gold.' Lack of proof either way leaves the question open."),
        T("Take care. In some settings, failing to find evidence after a proper search does count. If a careful medical test finds no sign of a "
          "disease, that counts against the claim that the disease is present. The fallacy is when no search has been made."),
        H("False dichotomy (false dilemma)"),
        D("A **false dichotomy** presents only two options as if they were the only ones, when there are others.", title="False dichotomy"),
        T("Example: 'Either we build a new road or the village will stay poor.' There may be other ways: a better bridge, a market, a mobile clinic."),
        TIP("The word 'either ... or' is a clue. Check whether the two options really cover every possibility.", title="Clue"),
        EX("Worked example 1: analogy", intro="'A teacher is like a driver. A driver can stop a car, so a teacher can stop a student's mind from wandering.' Evaluate this.", steps=[
            S("Find the comparison", text="Teacher and driver."),
            S("Look for relevant differences", text="A driver controls a machine. A student's attention is a person's own choice."),
            S("Verdict", text="Weak analogy. The similarity is slight and the differences matter."),
        ]),
        EX("Worked example 2: authority", intro="'A famous musician says a certain phone is the best in the world.' Is this a good reason?", steps=[
            S("Field of the speaker", text="Music."),
            S("Field of the claim", text="Technology and phones."),
            S("Other points", text="The musician may be paid to say it."),
            S("Verdict", text="Unqualified authority. A phone review by testing experts would be stronger."),
        ]),
        MISTAKE("Saying every use of an expert is a fallacy", "Check three things: Is the person an expert in THIS field? Do other experts agree? Is there a reason for bias?"),
        MISTAKE("Seeing a false dichotomy in every either-or", "Some either-or statements are true, such as 'Either the light is on or it is off'. The fallacy is when other options exist."),
        TIP("Paper 1 passages with 'either ... or', 'it is like ...' or 'the expert says' hint at this lesson. Name the fallacy and give your reason in one sentence. In Paper 2, "
            "a longer passage can contain two or three fallacies: name each and explain.", title="Exam link"),
        QUIZ("'Either you support our club or you are against football.' This is", [
            "appeal to ignorance",
            "weak analogy",
            "false dichotomy",
            "appeal to unqualified authority",
        ], 2, "It offers only two options. A person may like football and support a different club, or none.",
            hint="How many options does the speaker allow?",
            feedback=["Nothing is said about lack of proof.", "No comparison is made.", "", "No authority is cited."]),
        QUIZ("Which is the best example of reasonable appeal to authority?", [
            "A famous singer advises on medical treatment",
            "A qualified surgeon advises on a surgical operation, as other surgeons agree",
            "A neighbour says it because he is older",
            "Everybody says so",
        ], 1, "An expert in the right field, supported by other experts, gives good support.",
            hint="Which source is both qualified and in the right field?",
            feedback=["Singing is not medicine.", "", "Age alone is not expertise.", "That is an appeal to the people."]),
        PQ("Give an example of a weak analogy and say why it is weak.",
           "Example: 'A country is like a family. A family should not spend more than it earns, so a country should never borrow.' It is weak because a country can earn, tax and invest in ways a family cannot, so the two differ in relevant respects."),
        PQ("Explain the fallacy in: 'No one has shown that the new drink is unsafe, so it is safe.'",
           "Appeal to ignorance. The lack of proof of danger does not prove safety, especially when no proper test has been done. Careful testing that finds no harm would be real evidence."),
        PQ("When is an appeal to authority reasonable?",
           "When the person is an expert in the exact field, when other experts agree and when the person has no clear bias. Without these it becomes the fallacy of unqualified authority."),
        SUM("A weak analogy compares things that differ in ways that matter.",
            "An appeal to unqualified authority cites someone with no expertise in the field; appeals to real experts can be reasonable.",
            "An appeal to ignorance treats lack of proof as proof; careful searches that find nothing can be real evidence.",
            "A false dichotomy offers only two options when there are more.",
            "Different textbooks place these four in different groups: check your textbook."),
    ],
))

# ------------------------------------------------------------------ 6. Ambiguity: equivocation, amphiboly
LESSONS.append(lesson(
    module=MODULE, topic=T4,
    title="Ambiguity I: equivocation and amphiboly",
    slug="fal-ambiguity-equivocation-and-amphiboly",
    minutes=20,
    summary="Fallacies of ambiguity arise when meaning slips. Equivocation uses a word in two senses; amphiboly rests on a sentence whose grammar allows two readings.",
    objectives=[
        "Define ambiguity, equivocation and amphiboly",
        "Find the word that changes meaning in an equivocation",
        "Find the two readings of an amphibolous sentence",
        "Remove ambiguity by rewriting",
    ],
    key_concepts=["Ambiguity", "Equivocation", "Amphiboly", "Meaning", "Grammatical structure"],
    blocks=[
        H("Introduction"),
        T("A trader says: 'I have no change.' The customer says: 'Then you will never change.' The word 'change' is used in two meanings: "
          "small money and becoming different. The joke works because the word shifts."),
        T("When such a shift happens inside an argument, the argument may look strong without being strong. The Board lists these as "
          "**fallacies of ambiguity**. Textbooks agree on this group."),
        D("A word or sentence is **ambiguous** if it has more than one possible meaning in the context.", title="Ambiguity"),
        H("Equivocation"),
        D("**Equivocation** is the fallacy of using a key word in two different meanings in the same argument, "
          "so that the conclusion seems to follow when it does not.", title="Equivocation"),
        T("Example: 'Nothing is better than good health. A plate of rice is better than nothing. So a plate of rice is better than good health.' "
          "In the first sentence 'nothing' means 'no thing at all is better'. In the second it means 'having no food'. The word changes meaning."),
        T("Another: 'A bank keeps money safe. The river has a bank. So the river keeps money safe.' 'Bank' means a money institution in the first sentence "
          "and the side of a river in the second."),
        KEY("How to find an equivocation", "Three steps.", cards=[
            ["1. Pick the key word", "Choose the word that links the premises to the conclusion."],
            ["2. Test its meaning", "Replace it with its meaning in each place."],
            ["3. Compare", "If the meanings differ, the argument equivocates."],
        ]),
        H("Amphiboly"),
        D("**Amphiboly** is the fallacy that arises from a badly built sentence, whose grammar allows two readings. The words themselves are clear; "
          "the way they are arranged is not.", title="Amphiboly"),
        T("Example: 'Pupils and teachers with phones must hand them in.' Does it mean teachers and pupils who have phones, or only teachers who have phones "
          "plus all pupils? Another: 'I saw the girl with the binoculars.' Who has the binoculars?"),
        T("In an argument, the speaker takes one reading in the premise and the other in the conclusion, or uses the sentence for whichever reading suits."),
        TIP("The difference: in equivocation a single WORD shifts. In amphiboly the sentence STRUCTURE allows two readings.", title="Equivocation or amphiboly?"),
        EX("Worked example 1: equivocation", intro="'A bat is a mammal that sleeps in the day. The batsman holds a bat. So the batsman holds a mammal that sleeps in the day.' Evaluate.", steps=[
            S("Key word", text="'Bat'."),
            S("Meaning in the first premise", text="An animal."),
            S("Meaning in the second premise", text="A wooden club used in cricket."),
            S("Verdict", text="The word changes meaning, so the conclusion does not follow. This is equivocation."),
        ]),
        EX("Worked example 2: amphiboly", intro="A notice reads: 'Free tickets for students and teachers who pass the entrance test.' Explain the ambiguity.", steps=[
            S("First reading", text="Free tickets for all students, and for teachers who pass the test."),
            S("Second reading", text="Free tickets only for those students and teachers who pass the test."),
            S("Repair", text="'Free tickets for all students, and for teachers who pass the test.' or 'Free tickets for students and teachers, provided they pass the test.'"),
        ]),
        MISTAKE("Thinking every double meaning is a fallacy", "Wordplay and jokes use double meanings on purpose. It is a fallacy only when the shift is used to support a conclusion."),
        MISTAKE("Confusing equivocation with vagueness", "A vague word has unclear limits, like 'tall'. An equivocal word has distinct meanings, like 'bank'."),
        TIP("In Paper 1, if one word appears in both premises and the conclusion, test whether it keeps the same meaning. If a sentence can be read two ways because of "
            "its grammar, it is amphiboly.", title="Exam link"),
        QUIZ("'A bat is a mammal that flies at night. The batsman holds a bat. So the batsman holds a mammal that flies at night.' The word that changes meaning is", [
            "'mammal'",
            "'bat'",
            "'holds'",
            "'night'",
        ], 1, "'Bat' means an animal in the first sentence and a club in the second.",
            hint="Which word has two ordinary meanings?",
            feedback=["'Mammal' keeps its meaning.", "", "'Holds' keeps its meaning.", "'Night' keeps its meaning."]),
        QUIZ("'Visiting relatives can be tiresome.' This sentence is ambiguous because", [
            "a word has two dictionary meanings",
            "the grammar allows two readings",
            "it is vague",
            "it begs the question",
        ], 1, "It can mean that going to visit relatives is tiring, or that relatives who visit you are tiring. The grammar allows both.",
            hint="Are the words the problem, or their arrangement?",
            feedback=["The words are clear.", "", "It is not vague; it has two clear readings.", "No conclusion is assumed."]),
        PQ("Define equivocation and give an example of your own.",
           "Equivocation is using a key word in two different meanings in one argument. Example: 'A pen is a place to keep animals. My pen is in my pocket. So my pocket is a place to keep animals.'"),
        PQ("Explain the difference between equivocation and amphiboly.",
           "In equivocation, a word is used in two meanings. In amphiboly, the grammatical structure of a sentence allows two readings, even if every word has one meaning."),
        PQ("Rewrite 'Wanted: a driver for a big family with a clean licence' to remove the ambiguity.",
           "'Wanted: a driver with a clean licence for a big family.' The original may suggest that the family has the licence."),
        SUM("A word or sentence is ambiguous if it has more than one possible meaning.",
            "Equivocation: a key word changes meaning inside the argument.",
            "Amphiboly: a badly built sentence allows two readings.",
            "To find equivocation, test the key word's meaning each time; to find amphiboly, look for two ways of reading the grammar.",
            "Rewrite to remove the ambiguity."),
    ],
))

# ------------------------------------------------------------------ 7. Ambiguity: accent, composition, division
LESSONS.append(lesson(
    module=MODULE, topic=T4,
    title="Ambiguity II: accent, composition and division",
    slug="fal-ambiguity-accent-composition-and-division",
    minutes=20,
    summary="Accent changes meaning by stress or emphasis or by quoting out of context. Composition wrongly moves from parts to the whole; division wrongly moves from the whole to its parts.",
    objectives=[
        "Define accent, composition and division",
        "Show how stress can change the meaning of a sentence",
        "Distinguish composition from division",
        "Say when reasoning from parts to whole (or whole to parts) is sound",
    ],
    key_concepts=["Accent", "Emphasis", "Composition", "Division", "Whole and part", "Distributive and collective"],
    blocks=[
        H("Introduction"),
        T("Read this sentence aloud, stressing a different word each time: 'I did not say Ama stole the money.' If you stress 'I', "
          "someone else said it. If you stress 'say', you may have only hinted. If you stress 'stole', Ama may have borrowed it. One sentence has several meanings."),
        T("This lesson covers the last three fallacies in the Board's group of **fallacies of ambiguity**: accent, composition and division."),
        H("Accent"),
        D("The fallacy of **accent** arises when the meaning of a statement changes because of a shift in emphasis, or because words are "
          "quoted out of context, so that a different meaning is drawn.", title="Accent"),
        T("Example: A rule says: 'We should not speak ill of our friends.' If the stress falls on 'friends', it seems to allow speaking ill of others. "
          "That meaning was not intended. Another example: a shop advertises 'Prices from 500 FCFA' in large print and 'on selected items only' in tiny print. "
          "The big print gives an impression that the small print takes back."),
        T("Accent also happens when a sentence is cut from its context. 'We will not do the work' might come from 'We will not do the work for free'."),
        H("Composition"),
        D("The fallacy of **composition** argues that what is true of the parts is also true of the whole.", title="Composition"),
        T("Example: 'Each player on the team is excellent, so the team is excellent.' A team can have excellent players who do not work together. "
          "Another: 'Each brick is light, so the wall is light.'"),
        H("Division"),
        D("The fallacy of **division** argues that what is true of the whole is also true of its parts.", title="Division"),
        T("Example: 'The school is large, so every classroom is large.' Another: 'The bus is heavy, so each seat is heavy.'"),
        KEY("Composition and division are opposites", "The direction of the move is different.", cards=[
            ["Composition", "Parts to whole. Each player is excellent, so the team is excellent."],
            ["Division", "Whole to parts. The team is excellent, so each player is excellent."],
        ]),
        T("Some reasoning from parts to whole IS sound. 'Every part of the shirt is cotton, so the shirt is cotton.' Whether the move is sound depends on the property. "
          "Properties such as 'made of cotton' pass from parts to whole. Properties such as 'light' or 'excellent as a team' may not."),
        D("A property is **distributive** when it is true of each member separately ('each student is under 20'). It is **collective** when it is true of the group as a group "
          "('the students are a large group'). Mixing the two is the root of these fallacies.", title="Distributive and collective"),
        EX("Worked example 1: accent", intro="A notice reads: 'Buy two get one FREE' and underneath, in small print, 'cheapest item free, for orders over 50 000 FCFA'. What is the fallacy?", steps=[
            S("Big message", text="Buy two, get one free (for everyone)."),
            S("Small print", text="Only the cheapest item, and only for large orders."),
            S("Name it", text="Accent. Emphasis creates a meaning that the full statement does not support."),
        ]),
        EX("Worked example 2: composition or division?", intro="(a) 'The football team is the best in the region, so its goalkeeper is the best goalkeeper in the region.' (b) 'Each of the 11 players of our team cost little, so our team cost little.' Name each.", steps=[
            S("(a)", text="From the whole (the team) to a part (the goalkeeper): division."),
            S("(b)", text="From the parts (the players) to the whole (the team): composition. The cost of 11 people can add up to a lot."),
        ]),
        MISTAKE("Mixing up composition and division", "Ask: does the argument start with the parts or with the whole? Parts to whole is composition; whole to parts is division."),
        MISTAKE("Calling every move from parts to whole a fallacy", "It is sound for some properties, such as material (all cotton, so cotton). Test the property each time."),
        TIP("Paper 1 passages often give one sentence about a group and one about its members. Name the direction. For accent, look for emphasis, headlines, small print or a quotation cut short.",
            title="Exam link"),
        QUIZ("'Our class is the noisiest in the school, so every student in our class is noisy.' This is", [
            "composition",
            "division",
            "accent",
            "equivocation",
        ], 1, "It moves from a property of the whole class to every member. That is division.",
            hint="Does the argument move from whole to parts, or from parts to whole?",
            feedback=["That would move from the members to the class.", "", "No emphasis is involved.", "No word changes meaning."]),
        QUIZ("A headline says: 'Local school WINS' and the full story reads 'Local school wins one point in a match it lost'. The fallacy that best fits is", [
            "division",
            "false dichotomy",
            "accent",
            "composition",
        ], 2, "Emphasis on one part of the message creates a different meaning from the full statement.",
            hint="What does the headline emphasise?",
            feedback=["No whole-to-part move.", "No two options are offered.", "", "No parts-to-whole move."]),
        PQ("Define composition and division, and give one example of each.",
           "Composition argues from the parts to the whole: 'Each seat is cheap, so the car is cheap.' Division argues from the whole to the parts: 'The car is expensive, so each seat is expensive.'"),
        PQ("Show how changing the stress in 'I did not say that you were late' changes the meaning.",
           "Stress on 'I': someone else said it. Stress on 'say': I hinted it. Stress on 'you': someone else was late. Stress on 'late': you may have been absent or early. This is why accent can mislead."),
        PQ("Give one example where reasoning from parts to the whole is sound.",
           "'Every plank of this table is wood, so the table is wooden.' The property 'made of wood' passes from the parts to the whole."),
        SUM("Accent: the meaning changes through emphasis, small print or quotation out of context.",
            "Composition: what is true of the parts is wrongly said to be true of the whole.",
            "Division: what is true of the whole is wrongly said to be true of the parts.",
            "Some moves between part and whole are sound, depending on the property.",
            "Always name the direction of the move."),
    ],
))
