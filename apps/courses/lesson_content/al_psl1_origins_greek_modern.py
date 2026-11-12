"""A Level Philosophy (0790), Lower Sixth: origins and methods, Greek and medieval, modern Western philosophy (KKEVO draft, for reviewer checking against the syllabus and textbooks)."""

from .dsl import *  # noqa: F403

COURSE = ("philosophy", "lower-sixth")

M1 = "Nature, Origins & Methods of Philosophy"
M2 = "Ancient Greek & Medieval Philosophy"
M3 = "Modern Western Philosophy"

LESSONS = []


# ---------------------------------------------------------------------------
# M1 / From myth to logos
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M1, topic="From myth to logos",
    title="From myth to logos: how reasoned explanation began",
    slug="psl1-myth-to-logos",
    minutes=21,
    summary="What myth is and what it does for a community, what logos adds, how Greek thinkers began to explain the world by reasons, and why the 'miracle' story is questioned.",
    objectives=[
        "Define myth and logos and state the functions of myth",
        "Contrast mythical and rational (logos-based) ways of explaining the world",
        "Describe the conditions in Ionian Greece in which early philosophy appeared",
        "Evaluate the claim that philosophy began as a sudden 'Greek miracle'",
    ],
    key_concepts=["Myth", "Logos", "Cosmogony", "Rational explanation", "Greek miracle"],
    blocks=[
        H("Introduction"),
        T("Every community asks where the world came from, why the rains come, why people suffer and die, and how we ought to live. "
          "Long before schools and laboratories, people answered these questions with stories told by elders: how the river was made, "
          "why a clan keeps a taboo, how the first people came to the village. Such stories are found in every region of the world, "
          "including the oral traditions of Cameroon.\n\n"
          "Philosophy, as a Western school subject, usually begins with a change in the *kind* of answer people gave. "
          "This lesson studies that change: from **myth** to **logos**. Your syllabus calls it the nature and origins of philosophy."),
        D("A traditional story, usually about gods, heroes, ancestors or the first events of the world, handed down by a community. "
          "Myth tells how things came to be and what they mean. It is accepted on the authority of tradition, not tested by argument.",
          title="Myth"),
        D("A Greek word with several meanings: word, account, reason, argument, rational principle. In this topic it means "
          "**reasoned discourse**: giving reasons that anyone can examine, and explaining events by causes found in nature itself.",
          title="Logos"),
        H("What myth does for a community"),
        T("It would be a mistake to treat myth as 'silly stories'. Myth does serious work. Scholars list several functions, and the Board's Paper 1 "
          "has asked about the religious function of myth, so learn them."),
        KEY("Functions of myth", "Different textbooks use different labels. These four are widely accepted.", cards=[
            ["Explanatory", "It accounts for the origin of the world, of people, of fire, of death, of customs. It answers 'why is it so?'."],
            ["Religious", "It teaches religious values and is tied to ritual and worship. It tells people how to honour the gods or ancestors."],
            ["Social and moral", "It supports the order of the community: who rules, what is forbidden, what is shameful, what is honoured. It gives a shared identity."],
            ["Psychological", "It comforts. It gives meaning to suffering, fear and death by placing them in a larger story."],
        ]),
        H("What logos adds"),
        T("In the sixth century BCE, thinkers in the Greek cities of Ionia (the Aegean coast of present-day Turkey), above all in **Miletus**, "
          "began to explain the world differently. They asked: what is everything made of, and how does it change? "
          "And they answered without naming a god as the cause of each event. The answer had to be argued for, and others could criticise it."),
        KEY("Myth and logos compared", "Remember these contrasts, but see the warning below: they are tendencies, not a wall.", cards=[
            ["Source of authority", "Myth: tradition, inspired poet, priest or elder. Logos: reasons and evidence that any thinker can examine."],
            ["Type of cause", "Myth: persons and wills (a god is angry, so there is a storm). Logos: natural principles and processes (water, air, change)."],
            ["Attitude to criticism", "Myth: handed on, not questioned. Logos: open to objection and to rival theories; thinkers disagreed openly."],
            ["Form", "Myth: narrative, image, symbol. Logos: argument, definition, general principle."],
        ]),
        T("The first thinkers wanted an **arche**, a first principle, from which all things come. Thales is traditionally said to have proposed "
          "water; his successors proposed other principles. The details come in the lesson on the Pre-Socratics. What matters here is the "
          "*method*: a single natural principle, offered as a thesis that others could test and reject."),
        H("Why Ionia? Conditions that helped"),
        T("Historians offer several conditions, and you should present them as helpful factors, not as certain causes. "
          "Ionian cities were rich trading ports in contact with Egypt and the Near East, so travellers met many different customs and many different "
          "stories about the gods. Comparing them raised the question of which, if any, was true. Greek religion had no single holy book and no powerful priestly class "
          "controlling belief, so open debate was possible. Citizens of the independent city-states also practised public speaking and argument "
          "in assemblies. Finally, writing and the leisure of a prosperous class allowed some people to devote time to thinking."),
        H("Evaluating the 'Greek miracle'"),
        T("Older textbooks spoke of a 'Greek miracle': reason appearing suddenly in Greece out of nowhere. Most scholars today are more careful, "
          "for three reasons."),
        KEY("Objections to the 'miracle' story", "Use these when a question asks you to discuss or evaluate.", cards=[
            ["Borrowing", "Greek traders and thinkers knew Egyptian and Babylonian mathematics, astronomy and cosmology. Reasoned knowledge did not begin only in Greece."],
            ["Myth did not vanish", "Greek thinkers kept using myth. Plato, for example, wrote myths of his own to express ideas his arguments could not fully prove."],
            ["Reason elsewhere", "Other traditions, including African, Indian and Chinese ones, developed reasoned reflection. Calling only the Greek tradition 'rational' is a judgement that scholars now challenge."],
        ]),
        T("A balanced conclusion: something new and important happened in Ionia, namely the open, argued, competitive search for natural explanations, but it grew out of "
          "earlier cultures and kept ties to myth. Neither 'myth is nonsense' nor 'logos is cold and complete' is a fair summary. "
          "Modern thinkers also point out that myth is not simply a primitive science: it does jobs (meaning, identity, ritual) that logos alone does not do."),
        EX("Worked example 1: explaining thunder", intro="Compare a mythical and a rational explanation of thunder, and say what makes the second one an example of logos.", steps=[
            S("Mythical form", text="Thunder is the voice or weapon of an angry god. The cause is a person with a will. To stop it, you honour the god. No test is offered; the community accepts the story on the authority of tradition."),
            S("Early rational form", text="Thunder is produced by natural processes in the air, such as clouds striking one another. The cause is a natural process that every person can in principle observe and discuss."),
            S("What makes it logos", text="The second explanation gives a general reason, names no personal will as the cause, and can be criticised and replaced by a better account. It is open to argument."),
            S("A fair comment", text="The first account is not meaningless: it expresses fear, awe and a rule of conduct. It is a different kind of answer, not simply a bad scientific one."),
        ]),
        EX("Worked example 2: model essay plan", intro="'Philosophy began when Greeks stopped believing in myth.' Discuss.", steps=[
            S("Introduction", text="Define myth and logos. Thesis: philosophy began with a new method of explanation, but this was a shift of emphasis, not a clean break with myth."),
            S("For the claim", text="Thales and the Milesians explained nature by natural principles, argued for them and accepted criticism. They no longer named a god as the cause of each event."),
            S("Against the claim", text="The thinkers did not stop believing in gods; Heraclitus and Parmenides still use religious language. Plato used myth deliberately. Borrowing from the Near East shows the shift was gradual."),
            S("Evaluation", text="Myth continued to give meaning and values, which early logos did not supply. A better statement: Greek thinkers added a critical, argument-based tradition to a world full of myth."),
            S("Conclusion", text="The claim is half true: the new method is real, but 'stopped believing in myth' is too simple."),
        ]),
        TIP("Exam link: myth, logos and the origins of philosophy appear in Paper 1 multiple choice (the Board's report shows a question on the religious function of myth) and can feed Paper 2 essays on the nature of philosophy. Check the exact format with your teacher."),
        MISTAKE("Treating myth as simply false or stupid", "Examiners expect you to say what myth does (explain, teach religious and moral values, unify society, comfort). Saying 'myth is just lies' scores less than saying it is a different kind of discourse with its own functions."),
        MISTAKE("Saying that logos means 'logic' only", "Logos means word, reason, account and argument. In this topic it names reasoned, examinable explanation, not just formal logic."),
        MISTAKE("Dating philosophy to one day or one person with certainty", "Say 'traditionally' when you name Thales as the first philosopher. Our knowledge of the earliest thinkers comes from later writers such as Aristotle, and scholars treat details cautiously."),
        QUIZ("Which of these is a religious function of myth?",
             ["It proves scientific laws by experiment", "It teaches religious values and goes with ritual and worship", "It replaces all arguments by logic", "It abolishes tradition"], 1,
             "A religious function of myth is to teach religious values and to be tied to worship and ritual.",
             feedback=["Myth does not use experiment; that belongs to science.", "", "Replacing argument with logic describes logos, not myth.", "Myth preserves tradition."]),
        QUIZ("What mainly distinguishes logos from myth?",
             ["Logos is always shorter", "Logos explains by reasons and natural causes that others can examine and criticise", "Logos names more gods", "Logos was invented in Egypt only"], 1,
             "The key contrast is the kind of authority and cause: logos gives examinable reasons and natural causes.",
             feedback=["Length is irrelevant.", "", "Logos tends to avoid personal gods as direct causes of events.", "The Greek development took place in Ionia; the question is about method, not place alone."]),
        PQ("State two functions of myth and illustrate each with an example from any community.",
           "Model answer: (1) Explanatory: a story that tells how the river or the first people came to exist answers 'why is the world like this?'. (2) Social and moral: a story attached to a taboo tells people what is forbidden and so supports the order of the community. "
           "Other correct functions: religious (values and worship) and psychological (comfort in the face of death). Give a definition of myth first and name the function precisely."),
        PQ("Explain three differences between mythical and rational explanation.",
           "Model answer: (1) Authority: myth rests on tradition; logos rests on reasons anyone can examine. (2) Cause: myth appeals to gods or persons with wills; logos to natural principles. "
           "(3) Criticism: myth is handed down and not tested; logos invites objection and rival theories. A fourth difference: myth is narrative and image, logos is argument and general principle. End with the warning that the difference is one of emphasis."),
        PQ("'The Greek miracle' is a misleading description of the origins of philosophy. Discuss.",
           "Model plan: define the claim (reason arose suddenly in Greece). For misleading: borrowing from Egypt and Babylon; myth kept in Greek thought; reasoned reflection in other cultures. "
           "Against (some truth in it): the Milesians' open, competitive, argument-based search for natural principles was a new and influential style. Judgement: the description is exaggerated, but the new method is a real turning point."),
        SUM("Myth is a traditional story that explains, teaches religious and moral values, unifies the community and comforts.",
            "Logos is reasoned discourse: reasons and natural causes that others can examine and criticise.",
            "Early philosophy appeared in Ionian trading cities such as Miletus in the sixth century BCE, helped by contact with other cultures, open debate and leisure.",
            "Philosophy is better described as a shift from myth to logos than a clean break: myth survived and logos has borrowed roots.",
            "The 'Greek miracle' idea is challenged by borrowing, the survival of myth, and reasoned thought in other traditions."),
    ],
))

# ---------------------------------------------------------------------------
# M1 / The branches of philosophy
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M1, topic="The branches of philosophy",
    title="Metaphysics, epistemology, ethics, logic and aesthetics",
    slug="psl1-branches-of-philosophy",
    minutes=21,
    summary="The main branches of philosophy, the central questions each asks, how they overlap, and how to place any philosophical question in the right branch.",
    objectives=[
        "Define philosophy and name its main branches",
        "State the central questions of metaphysics, epistemology, ethics, logic and aesthetics",
        "Classify sample questions and thinkers by branch",
        "Explain why the branches overlap and are not sealed boxes",
    ],
    key_concepts=["Metaphysics", "Epistemology", "Ethics", "Logic", "Aesthetics", "Political philosophy"],
    blocks=[
        H("Introduction"),
        T("Is a rich man who got his money by fraud successful? Can I be sure the world is not a dream? Is a market painting beautiful, or does it only seem beautiful to me? "
          "Does a cause always produce its effect? These are different questions, and philosophers sort them into **branches**. Sorting helps you understand what kind of answer is needed, "
          "and the Paper 1 multiple choice often tests whether you can place a question or a thinker in its branch."),
        D("The critical, reasoned study of the most general questions about reality, knowledge, value and reasoning itself. The word comes from Greek *philosophia*, "
          "'love of wisdom'. Philosophy asks questions that cannot be settled only by experiment, and it asks for reasons.", title="Philosophy"),
        H("The five classical branches"),
        IMG("alpsl1-branches.svg", alt="A concept map with philosophy at the centre and five branches around it: metaphysics (what is real), epistemology (what can we know), ethics (what should we do), logic (what follows from what) and aesthetics (what is beautiful), with political philosophy shown as a sixth neighbour of ethics.",
            caption="Figure 1. The branches of philosophy and their central questions."),
        D("The study of the ultimate nature of reality: what exists, what kinds of things there are, what a substance is, whether there is a god, whether the mind is separate from the body, "
          "whether we are free. Its parts include **ontology** (the study of being) and **cosmology** (the study of the universe as a whole).", title="Metaphysics"),
        D("The study of knowledge: what knowledge is, how we get it, what its limits are, whether reason or sense experience is its source, and what counts as justification or truth.", title="Epistemology"),
        D("The study of right and wrong, good and bad, duty and virtue. **Moral philosophy** is another name. It asks how we ought to live and what makes an action right.", title="Ethics"),
        D("The study of correct reasoning: what makes an argument valid, how to detect fallacies, how to symbolise and test arguments. Logic does not tell us what to believe; it tells us what follows from what.", title="Logic"),
        D("The study of beauty, art and taste: what makes something beautiful, whether beauty is in the object or the viewer, what art is for.", title="Aesthetics"),
        T("**Political and social philosophy** studies the state, law, justice, rights and authority. Many syllabuses treat it as part of ethics, because it asks how a community ought to be organised. "
          "Other fields, such as the philosophy of science, mind, language, religion and history, apply these branches to a special subject. In your syllabus these appear later as epistemology and philosophy of science, "
          "and as moral, social and political philosophy."),
        H("Placing a question in its branch"),
        KEY("Quick test", "Ask what the question is really about.", cards=[
            ["About what exists", "'Is there a soul?', 'Is everything matter?', 'Do we have free will?' Metaphysics."],
            ["About knowing", "'How do I know the senses are reliable?', 'Is knowledge innate?' Epistemology."],
            ["About right and wrong", "'Is lying always wrong?', 'What do we owe the poor?' Ethics."],
            ["About reasoning", "'Is this argument valid?', 'What is a fallacy?' Logic."],
            ["About beauty and art", "'Can an ugly object be art?' Aesthetics."],
        ]),
        T("Notice that one topic can sit in two branches. Descartes' cogito is epistemology (what can I be certain of?) and also metaphysics (what am I?). "
          "Plato's Theory of Forms is metaphysics (what is real), epistemology (how we know) and political philosophy (who should rule). "
          "Place a question by its **main** concern and say so in your answer."),
        H("Why the branches overlap"),
        T("The branches depend on one another. An ethical theory needs a view of what a person is (metaphysics) and how we can know moral truths (epistemology). "
          "An epistemology needs logic to test its arguments. Every branch uses logic. This is a good point to make when a question asks you to evaluate a division of philosophy into branches: "
          "the division is a convenience for study, not a set of sealed boxes."),
        EX("Worked example 1: classify the questions", intro="Place each in its main branch: (a) Is it ever right to break a promise? (b) Does the world exist when nobody perceives it? (c) 'All birds fly; a penguin is a bird; so a penguin flies': is the form valid? (d) Is beauty a property of an object?", steps=[
            S("(a)", text="Ethics: it concerns rightness of action."),
            S("(b)", text="This could be metaphysics (does the object exist?) or epistemology (can we know?). Berkeley's idealism treats it as both. State your reason: the question about existence is metaphysical, the question about what we can know is epistemological."),
            S("(c)", text="Logic: the question is about the form of an argument. (Valid in form, but the first premise is false, so the argument is not sound.)"),
            S("(d)", text="Aesthetics: it concerns the nature of beauty."),
        ]),
        EX("Worked example 2: model essay plan", intro="'Philosophy is just logic with big words.' Discuss.", steps=[
            S("Introduction", text="Define philosophy and logic. Thesis: logic is an essential tool and a branch, but philosophy asks questions that logic alone cannot answer."),
            S("For", text="All philosophy uses argument, and the demand for valid reasoning is central. Some modern schools stress analysis of language and logic."),
            S("Against", text="Logic tests the form of reasoning, not the truth of premises. Metaphysics asks what exists, ethics what we ought to do, aesthetics what is beautiful: these need more than form."),
            S("Evaluation", text="Logic is the common tool, but each branch has its own subject matter."),
            S("Conclusion", text="The claim is partly right about method and wrong about content."),
        ]),
        TIP("Exam link: branches and their definitions are Paper 1 material, and they frame Paper 2 essays on the nature and scope of philosophy. In every essay, say which branch a theory belongs to; the Board's report notes the need for correct, orthodox wording and for care with the terms."),
        MISTAKE("Mixing ontology and epistemology", "Ontology asks what exists and what kinds of things there are. Epistemology asks what we can know and how. 'Does God exist?' is metaphysical; 'Can we know God exists?' is epistemological."),
        MISTAKE("Saying that logic decides what is true", "Logic decides whether a conclusion follows. A valid argument with a false premise can have a false conclusion. Truth of premises is a different matter."),
        QUIZ("'Is knowledge possible without sense experience?' belongs mainly to",
             ["Aesthetics", "Epistemology", "Ethics", "Political philosophy"], 1,
             "It asks about the source and limits of knowledge, which is epistemology.",
             feedback=["Aesthetics is about beauty and art.", "", "Ethics is about right and wrong.", "Political philosophy is about the state and justice."]),
        QUIZ("Which pair is correctly matched?",
             ["Metaphysics: what is beautiful", "Logic: what makes an argument valid", "Ethics: what is real", "Aesthetics: what is knowledge"], 1,
             "Logic studies the validity of arguments.",
             feedback=["Beauty belongs to aesthetics; metaphysics asks about reality.", "", "Reality is metaphysics; ethics is about right and wrong.", "Knowledge belongs to epistemology."]),
        PQ("Define philosophy and name the five branches with one question for each.",
           "Model answer: philosophy is the critical, reasoned study of the most general questions (love of wisdom). Metaphysics: what exists? Epistemology: what can we know? Ethics: how ought we to act? Logic: what makes reasoning valid? Aesthetics: what is beauty?"),
        PQ("Explain, with one example, why the branches of philosophy overlap.",
           "Model answer: an ethical theory depends on a view of human nature (metaphysics) and on how moral truths can be known (epistemology); and every branch uses logic. "
           "Example: Plato's Forms are metaphysical (what is real) but also give an account of knowledge and of who should rule. So the branches are tools for study, not separate boxes."),
        PQ("Distinguish metaphysics from epistemology, using one question for each, and say why Descartes' cogito belongs to both.",
           "Model answer: metaphysics asks what is real ('Is the mind separate from the body?'); epistemology asks what we can know and how ('Can I be certain of anything?'). "
           "The cogito answers an epistemological question (what survives doubt?) and then yields a metaphysical claim (I exist as a thinking thing)."),
        SUM("Philosophy is the reasoned study of the most general questions about reality, knowledge, value and reasoning.",
            "Metaphysics studies what exists (ontology, cosmology); epistemology studies knowledge; ethics studies right and wrong.",
            "Logic studies valid reasoning; aesthetics studies beauty and art; political philosophy studies the state, law and justice.",
            "Place a question by its main concern; many topics sit in more than one branch.",
            "The branches overlap and all use logic; the division is for convenience, not a wall."),
    ],
))

# ---------------------------------------------------------------------------
# M1 / Philosophical methods
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M1, topic="Philosophical methods",
    title="Socratic questioning, Cartesian doubt, dialectic and phenomenology",
    slug="psl1-philosophical-methods",
    minutes=22,
    summary="Four classic methods of philosophising (maieutics and elenchus, methodic doubt, dialectic, phenomenology): what each does, an example, and the strengths and limits of each.",
    objectives=[
        "Describe the Socratic method (elenchus and maieutics) and give an example",
        "Explain Descartes' methodic doubt and why it is called methodic",
        "Describe dialectic in its Platonic and Hegelian senses",
        "Describe Husserl's phenomenological method, including epoche, and evaluate each method",
    ],
    key_concepts=["Maieutics", "Elenchus", "Methodic doubt", "Dialectic", "Phenomenology", "Epoche"],
    blocks=[
        H("Introduction"),
        T("Science has laboratories. Philosophy has **methods**: disciplined ways of asking questions and testing answers. Your syllabus names four, and they appear again and again in the course: "
          "the Socratic method, Cartesian doubt, dialectic and phenomenology. Paper 1 asks you to recognise them, and the dissertation of Paper 3 uses dialectic in its structure."),
        H("Socratic method: elenchus and maieutics"),
        D("Socrates' method of **cross-examination**. He asked someone for a definition (for example, 'What is courage?'), then asked further questions that showed the definition conflicted with other things the person believed. "
          "The aim was to expose contradiction and false confidence. The Greek word *elenchus* means testing or refutation.", title="Elenchus"),
        D("Socrates compared his role to a midwife: he did not give the answer but helped the other person 'give birth' to ideas they already held. "
          "*Maieutics* is the art of drawing out ideas by questions. It was linked with the belief that knowledge can be reached by the person's own reasoning.", title="Maieutics"),
        T("We know Socrates mainly through Plato's dialogues, so the details of his method are partly Plato's presentation. The Board's Paper 1 has asked which process describes knowledge for Socrates; "
          "the answer centres on **dialectic**, conversation by question and answer, with irony (pretending ignorance) and elenchus as its parts."),
        EX("Worked example 1: a Socratic dialogue on a modern definition", intro="Show how elenchus works on the claim 'honesty means always telling everything you know'.", steps=[
            S("Step 1: the definition", text="Student: 'Honesty is telling everything you know.'"),
            S("Step 2: a test case", text="Teacher: 'Your friend asks if you know where a surprise gift is hidden. Do you tell?' Student: 'No, that would spoil it.'"),
            S("Step 3: the contradiction", text="So honesty does not mean telling everything. The first definition is refuted, or at least too broad."),
            S("Step 4: a better attempt", text="Student: 'Honesty is not deceiving people to harm them.' The process continues with new tests."),
            S("Result", text="No final answer is guaranteed, but the student has a clearer and better idea. This is the Socratic method: knowledge by dialogue."),
        ]),
        H("Cartesian doubt"),
        D("René Descartes (1596–1650) decided to doubt everything that could be doubted, in order to find something certain on which to build knowledge. "
          "It is **methodic** because doubt is a tool, used for a time on purpose, not a permanent attitude. It is **hyperbolic** (exaggerated) because he treats even a small reason for doubt as enough to reject a belief.", title="Methodic doubt"),
        T("He doubts the senses (they sometimes deceive), then doubts that he is awake (dreams can be vivid), and then imagines a powerful deceiving 'evil demon' who might make even mathematics seem true when it is false. "
          "One thing survives: the fact that I am doubting or thinking shows that I exist. The report's key for Paper 1 notes that in the Meditations the first indubitable truth is 'I am, I exist'. "
          "The famous 'I think, therefore I am' appears in his other works. Full treatment is in the Rationalism lesson."),
        KEY("Strengths and limits of Cartesian doubt", "Use both in an evaluation.", cards=[
            ["Strength", "It forces us to ask what we really know and builds knowledge on a foundation that cannot be shaken."],
            ["Limit 1", "Critics say it is artificial: nobody can really doubt everything, and the method assumes that certainty is the standard for knowledge."],
            ["Limit 2", "Some argue the cogito already depends on language and concepts that were not doubted."],
        ]),
        H("Dialectic"),
        D("From a Greek word for conversation. In **Plato**, dialectic is the method of moving by question and answer, and by classification and definition, towards the knowledge of the Forms. "
          "In **Hegel** (later in your course), dialectic names the development of thought or history through a conflict of opposed positions. It is often summarised as thesis, antithesis, synthesis; "
          "check your textbook, because Hegel himself did not use that exact formula.", title="Dialectic"),
        T("In the **philosophical dissertation** of Paper 3, you are asked to use a dialectical method in a simple form: state a thesis, examine the objections to it (the antithesis), "
          "and reach a reasoned position that takes both into account. This is a good example of a method being used as an exam skill."),
        H("Phenomenology"),
        D("A method founded by Edmund Husserl (1859–1938). It studies things *as they appear* in consciousness, describing experience carefully, without first deciding whether the things exist as science describes them. "
          "Husserl's slogan is 'to the things themselves'. A key step is the **epoche** (Greek for suspension): we put aside, or 'bracket', our assumptions about the world to describe pure experience. "
          "A related idea is **intentionality**: consciousness is always consciousness *of* something.", title="Phenomenology"),
        EX("Worked example 2: describing a mango phenomenologically", intro="How would a phenomenologist study the experience of seeing a ripe mango?", steps=[
            S("Bracket assumptions", text="Set aside questions such as how the fruit grew or what chemistry gives it its colour."),
            S("Describe the experience", text="Note the yellow-red colour, its smooth skin, the smell, the memory of the market, the desire to eat: how the mango is *given* to consciousness."),
            S("Find the structure", text="Notice that seeing is always seeing *of* something (intentionality), and that the mango appears from one side while I expect other sides."),
            S("Result", text="A careful description of experience, not an explanation by science. Phenomenology is later developed by existentialists."),
        ]),
        TIP("Exam link: philosophical methods are tested in Paper 1 multiple choice (the Board has set a question on the Socratic process) and are used inside Paper 2 essays and the Paper 3 dissertation. Always name the method and give its own technical term."),
        MISTAKE("Saying Socrates taught by lecturing", "Socrates claimed to know nothing and taught by questions. Lecturing the answer is the opposite of maieutics."),
        MISTAKE("Thinking Descartes was a permanent sceptic", "His doubt is **methodic**: a path to certainty. He ended with a firm foundation, not with despair. A sceptic such as Pyrrho (later lesson) differs."),
        MISTAKE("Treating dialectic as one fixed formula", "Plato's dialectic (question and answer towards the Forms) and Hegel's dialectic (movement through opposition) are different. Say which one you mean."),
        QUIZ("Socrates described his role as a midwife. This refers to his method called",
             ["Epoche", "Maieutics", "Hyperbolic doubt", "Synthesis"], 1,
             "Maieutics is the art of helping others bring their own ideas to birth by questioning.",
             feedback=["Epoche is Husserl's suspension of assumptions.", "", "Hyperbolic doubt is Descartes' method.", "Synthesis belongs to the Hegelian pattern."]),
        QUIZ("Why is Descartes' doubt called methodic?",
             ["Because he doubted everything for ever", "Because it is a deliberate procedure aimed at finding certainty", "Because it was invented by Socrates", "Because it proves that nothing exists"], 1,
             "It is a method: doubt is used on purpose to find an indubitable foundation.",
             feedback=["He did not stay a sceptic.", "", "It is Descartes' own method.", "He concluded the opposite: that I exist."]),
        PQ("Describe the Socratic method and give a short example.",
           "Model answer: Socrates questioned people about a concept such as courage. In the elenchus he tested each definition by examples that exposed contradiction. In maieutics he helped them reach their own better definition. "
           "Example: the definition 'honesty is telling everything you know' fails when the friend asks about a surprise gift; a better definition is then sought."),
        PQ("What is methodic doubt? Why did Descartes use it and what limits does it have?",
           "Model answer: Descartes doubted every belief that could be doubted (senses, waking state, even mathematics through the evil demon), in order to find a certain foundation. It is methodic because it is a tool. "
           "He found that the fact of his thinking could not be doubted. Limits: the standard of certainty is very high, the doubt is artificial, and the cogito may rely on assumed concepts."),
        PQ("Distinguish Platonic dialectic, Hegelian dialectic and Husserl's phenomenology.",
           "Model answer: Platonic dialectic is question-and-answer reasoning towards the Forms. Hegelian dialectic is the movement of thought or history through opposed positions to a higher unity (check the textbook on the thesis-antithesis-synthesis label). "
           "Phenomenology describes experience as it appears, after bracketing assumptions (epoche), and stresses intentionality."),
        SUM("Socratic method: dialogue using irony, elenchus (refutation) and maieutics (helping ideas be born).",
            "Cartesian doubt is methodic and hyperbolic: doubt used as a tool to find a certain foundation.",
            "Dialectic means conversation or the movement through opposition, in Plato and in Hegel; do not mix the two.",
            "Phenomenology describes experience as given in consciousness, using the epoche and the idea of intentionality.",
            "Each method has a strength and a limit; evaluation needs both."),
    ],
))

# ---------------------------------------------------------------------------
# M2 / The Pre-Socratics
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M2, topic="The Pre-Socratics",
    title="The Pre-Socratic cosmologists: arche, change and atoms",
    slug="psl1-pre-socratics",
    minutes=24,
    summary="The search for the arche from Thales to Democritus: monists and pluralists, Heraclitus on change, Parmenides and Zeno against change, and the atomists, with a verified check of Zeno's Achilles paradox.",
    objectives=[
        "Define arche, monism and pluralism and explain why the Pre-Socratics are called cosmologists",
        "State the main thesis of Thales, Anaximander, Anaximenes, Pythagoras, Heraclitus, Parmenides, Zeno and Democritus",
        "Explain the conflict between Heraclitus (change) and Parmenides (being)",
        "Explain Zeno's Achilles paradox and how modern mathematics answers it",
    ],
    key_concepts=["Arche", "Monism", "Flux", "Being", "Atoms and void", "Zeno's paradoxes"],
    blocks=[
        H("Introduction"),
        T("Stand on the coast at Limbe and look at the sea, the cloud and the volcano. What is all this made of, and why does it change? "
          "Greek thinkers of the sixth and fifth centuries BCE asked exactly this. We call them **Pre-Socratic** because they came before (or beside) Socrates, and **cosmologists** because they tried to explain the *cosmos*, the ordered world. "
          "We know their ideas only from fragments and from later writers, above all Aristotle, so every statement below is a traditional report. Check your textbook for disputed details."),
        D("The Greek word for the **first principle**: the original and underlying stuff, or source, from which all things come and into which they return. "
          "The Pre-Socratics searched for one or several arche.", title="Arche"),
        D("**Monism** (from Greek *monos*, one) holds that reality comes from a single principle or substance. **Pluralism** holds that there are several basic principles. "
          "The Board's Paper 1 treats monism and the search for a primary stuff as typical of the Pre-Socratics.", title="Monism and pluralism"),
        H("The Milesians: Thales, Anaximander, Anaximenes"),
        KEY("The Milesian monists", "Three thinkers of Miletus, three different arche.", cards=[
            ["Thales (early 6th century BCE)", "Traditionally: the arche is **water**. Everything comes from water and returns to it. Aristotle suggests reasons such as the role of moisture in life and nourishment, but this is his reconstruction."],
            ["Anaximander", "The arche is the **apeiron**, the boundless or indefinite. It has no definite quality such as wet or dry, so it can give rise to opposites."],
            ["Anaximenes", "The arche is **air**. Air changes by thinning (rarefaction, becoming fire) and thickening (condensation, becoming wind, cloud, water, earth). Difference in things is a difference in *density* of one stuff, which gives a mechanism of change."],
        ]),
        T("Notice the progress: Thales names a stuff; Anaximander sees that a definite stuff cannot be the source of its opposite; Anaximenes explains *how* one stuff can become many. This is a good example of the open, critical development of ideas you studied under myth and logos."),
        H("Pythagoras: number"),
        T("Pythagoras (late 6th century BCE) and his followers saw **number** as the arche. The Board's report explains the point carefully: it is not that every object literally consists of numbers, "
          "but that order and harmony, which result from numerical ratios, are the principle of things. A known example is that the musical intervals correspond to simple ratios of string lengths. "
          "Reality is structured by proportion. Many details of the early Pythagoreans are uncertain (it was a secretive school), so attribute with care."),
        H("Heraclitus: everything flows"),
        T("Heraclitus of Ephesus (about 500 BCE) held that **change is the basic fact**. All things are in flux; stability is only apparent, like the form of a river kept by its moving water. "
          "Fire is his symbol of this constant change. He taught that the world is a **unity of opposites** held together by tension (day and night, war and peace, up and down), and he spoke of a **logos**, "
          "a rational law or measure that governs all change. Reality is order in motion."),
        H("Parmenides and Zeno: being does not change"),
        T("Parmenides of Elea (early 5th century BCE) argued the opposite. In his poem he contrasts the 'way of truth' with the 'way of opinion' (the world of the senses). "
          "His argument: what **is** can only be; what is not cannot be thought or spoken of. So being is one, uncreated, indestructible, complete and unchanging, and change, coming-to-be and plurality are illusions of the senses. "
          "Reason, not the senses, leads to truth. This is a very influential kind of **rationalism**."),
        T("**Zeno of Elea**, his follower, defended him by showing that belief in motion and plurality leads to absurd results. His **paradoxes** are arguments of the form: if A, then absurdity; so not A."),
        KEY("Zeno's Achilles", "The fast runner Achilles can never overtake a slow tortoise that has a head start.", cards=[
            ["The argument", "To overtake, Achilles must first reach where the tortoise started. By then the tortoise has moved on a little. He must reach that new point, and by then it has moved again. There are infinitely many stages."],
            ["What it assumes", "That space (and the stretch of time) can be divided without end, and that covering infinitely many stages must take infinite time. Its conclusion: motion is impossible, so the senses deceive us."],
            ["Modern reply", "The infinitely many stages get smaller and smaller, and their sum can be finite. The times form a convergent series. Whether this fully answers Zeno is still discussed (check your textbook)."],
        ]),
        EX("Worked example 1: a verified check of the Achilles series",
           intro="Achilles runs at 10 metres per second and the tortoise at 1 metre per second, with a 100 metre head start. Show that Achilles does overtake it, and when.", steps=[
            S("Stage 1", text="Achilles runs 100 m in 10 s. The tortoise has moved 10 m."),
            S("Stage 2", text="Achilles runs 10 m in 1 s. The tortoise moves 1 m. Then 1 m in 0.1 s, and so on. The times are 10, 1, 0.1, 0.01, ... seconds."),
            S("Sum the series", math=r"10 + 1 + 0.1 + \dots = \dfrac{10}{1 - \tfrac{1}{10}} = \dfrac{100}{9} \approx 11.11 \text{ s}"),
            S("Check by algebra", math=r"10t = 100 + t \Rightarrow t = \dfrac{100}{9} \approx 11.11 \text{ s}"),
            S("Conclusion", text="The infinite sum is finite and equals the time given by ordinary algebra: Achilles overtakes at about 11.11 s, after running about 111.1 m. Zeno's conclusion fails if infinitely many stages can add to a finite time."),
        ]),
        H("Democritus: atoms and void"),
        T("The **atomists**, Leucippus and Democritus (5th century BCE), tried to save both change and reason. Reality consists of **atoms**, tiny, indivisible, eternal particles, moving in the **void** (empty space). "
          "Atoms differ in shape, size and arrangement. Things come to be and pass away when atoms combine and separate. So change is real (atoms move), but being does not come from nothing (atoms are eternal), which meets Parmenides' demand. "
          "This is a pluralist and materialist account, and it is an ancestor of modern atomic theory, although the Greek atomists had no experiments."),
        EX("Worked example 2: model essay plan", intro="'Heraclitus and Parmenides give opposite answers to one question.' Explain and evaluate.", steps=[
            S("The question", text="What is the nature of reality: change or stable being?"),
            S("Heraclitus", text="Flux is basic; opposites in tension; a logos governs the process."),
            S("Parmenides", text="Being cannot change or come from non-being; the senses show only opinion; reason shows being is one and unchanging. Zeno defends this with paradoxes."),
            S("Evaluation", text="Heraclitus matches everyday experience but needs the logos to avoid chaos; Parmenides is logically strict but denies the obvious fact of motion. The atomists and later Plato and Aristotle try to combine the two."),
            S("Conclusion", text="The opposition drove later Greek philosophy, which sought a view that explains both stability and change."),
        ]),
        TIP("Exam link: Pre-Socratic thinkers are examined in Paper 1 (the Board's report shows questions on monism, Anaximenes, Pythagoras and Zeno's Achilles argument) and in Paper 2 essays on ancient philosophy. The report advises evaluating individual philosophers, not whole groups."),
        MISTAKE("Saying the Pre-Socratics all chose water", "Only Thales is linked with water. Anaximander: apeiron; Anaximenes: air; Heraclitus: fire/flux; Pythagoras: number; Democritus: atoms and void."),
        MISTAKE("Saying Pythagoras believed numbers are physical things made of digits", "The better reading: number, as proportion and harmony, is the principle of order. Do not confuse 'number' with 'numbers'."),
        MISTAKE("Calling Zeno's paradoxes a proof that Achilles cannot run", "They are arguments against the assumptions of motion and plurality. The mathematical reply shows that an infinite series can have a finite sum."),
        QUIZ("Which Pre-Socratic is linked with the idea of the boundless (apeiron)?",
             ["Thales", "Anaximander", "Heraclitus", "Democritus"], 1,
             "Anaximander proposed the apeiron, an indefinite and unlimited source.",
             feedback=["Thales is linked with water.", "", "Heraclitus stressed flux and fire.", "Democritus proposed atoms and void."]),
        QUIZ("Zeno's Achilles argument presupposes that",
             ["time and space cannot be measured", "space can be divided without end and infinitely many stages cannot be completed", "Achilles was slower than the tortoise", "the senses never deceive"], 1,
             "It relies on infinite divisibility and on the claim that infinitely many stages require infinite time.",
             feedback=["Measurement is not the assumption.", "", "Achilles is the faster runner.", "Zeno uses the argument to say the senses deceive us."]),
        PQ("Define arche and monism, and contrast the arche of Thales and Anaximenes.",
           "Model answer: arche is the first principle of all things. Monism holds that there is one such principle. Thales: water. Anaximenes: air, which by rarefaction and condensation can become fire, wind, cloud, water and earth. "
           "Anaximenes adds a mechanism of change; Thales names the stuff only. Attribution to Thales rests mainly on Aristotle."),
        PQ("Explain the disagreement between Heraclitus and Parmenides about change.",
           "Model answer: Heraclitus holds that flux is fundamental, with a logos ordering the opposites. Parmenides argues that what is cannot come from nothing or change, so change is an illusion of the senses and reason shows being is one. "
           "Evaluation: one fits experience, the other fits strict logic; later thinkers (atomists, Plato, Aristotle) try to reconcile them."),
        PQ("Explain Zeno's Achilles paradox and one reply to it. Achilles runs at 10 m/s, the tortoise at 1 m/s, with a head start of 100 m: when does he catch it?",
           "Model answer: the paradox says he must complete infinitely many stages, so cannot overtake. Reply: the stage times 10, 1, 0.1, ... sum to 100/9 seconds, about 11.1 s, which agrees with 10t = 100 + t. "
           "An infinite series can have a finite sum, so the stages do not take infinite time. Whether that fully answers Zeno's underlying questions about the infinite is still discussed."),
        SUM("The Pre-Socratics sought the arche, the first principle; monists named one, pluralists several.",
            "Thales: water; Anaximander: apeiron; Anaximenes: air with condensation and rarefaction; Pythagoras: number as proportion and harmony.",
            "Heraclitus: flux, unity of opposites and a governing logos; Parmenides: being is one and unchanging; Zeno defends him by paradoxes.",
            "Democritus: atoms and void, an attempt to save both change and being.",
            "The Achilles series 10 + 1 + 0.1 + ... converges to 100/9, which answers the paradox mathematically."),
    ],
))

# ---------------------------------------------------------------------------
# M2 / The Sophists and Socrates
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M2, topic="The Sophists and Socrates",
    title="The Sophists, relativism and the philosophy of Socrates",
    slug="psl1-sophists-and-socrates",
    minutes=22,
    summary="The turn from nature to human beings: Protagoras, Gorgias and Thrasymachus, the nomos and physis debate, Socrates' search for definitions, his claim that virtue is knowledge, and his trial.",
    objectives=[
        "Explain who the Sophists were and why Athens needed them",
        "State the doctrines of Protagoras, Gorgias and Thrasymachus and explain relativism",
        "Explain Socrates' method, his claim that virtue is knowledge, and the charges at his trial",
        "Compare the Sophists and Socrates and evaluate each",
    ],
    key_concepts=["Sophist", "Relativism", "Nomos and physis", "Socratic ignorance", "Virtue is knowledge", "Socratic problem"],
    blocks=[
        H("Introduction"),
        T("In fifth-century BCE Athens, a democracy, success in public life depended on speaking well in the assembly and the law courts. Ambitious young men wanted teachers. "
          "Travelling teachers, the **Sophists**, offered to teach rhetoric (the art of persuasive speech) and 'excellence', for a fee. "
          "At the same time **Socrates** walked the market place asking questions for nothing. Both turned philosophy away from the study of the cosmos towards **human beings**: how we should live, what justice is, whether virtue can be taught."),
        D("Professional teachers of rhetoric and practical knowledge in Greek cities, such as Protagoras and Gorgias. "
          "The word first meant 'wise person'. Because Plato and Aristotle criticised them harshly, *sophistry* became an insult for clever but misleading argument. "
          "Historians are more balanced: the Sophists responded to a real need in democratic Athens.", title="Sophist"),
        D("The view that truth or value depends on the person, the group or the culture, so that there is no single standard valid for everyone. "
          "Relativism can be about truth (**epistemological**) or about morals (**ethical**).", title="Relativism"),
        H("The Sophists"),
        KEY("Three Sophists", "Learn one doctrine for each, in your own words.", cards=[
            ["Protagoras", "The human being is the measure of all things. In the usual interpretation: things are for each person as they appear to that person, so truth is relative. The report for Paper 1 treats this as the key relativist doctrine. Protagoras is also reported as agnostic about the gods."],
            ["Gorgias", "Usually presented as a thinker of three claims: nothing exists; if anything existed we could not know it; if we knew it we could not tell it to others. Scholars debate whether he was serious or showing the power of rhetoric. He stressed that **words persuade**, so rhetoric is powerful."],
            ["Thrasymachus", "Appears in Plato's Republic and argues that justice is what is to the advantage of the stronger: rulers make laws for their own benefit. We know him only through Plato, who opposes him."],
        ]),
        T("The Sophists also debated **nomos and physis**: is justice a matter of *nomos* (law and convention, made by people and different from place to place) or of *physis* (nature, fixed and the same everywhere)? "
          "Many Sophists stressed convention. This links with relativism: if laws are man-made, why obey them? Others argued that convention is a useful agreement. The debate returns in every discussion of natural law versus positive law."),
        T("Evaluation of Protagoras: if truth is relative to each person, then a person who says 'Protagoras is wrong' is also right *for himself*. "
          "Critics (Plato) say relativism refutes itself or makes disagreement pointless. Defenders say it expresses a sound respect for different perspectives and customs. "
          "Notice also that relativism about customs (different societies have different marriage rules) is not the same as relativism about truth (what is true differs for each person)."),
        H("Socrates"),
        T("Socrates (about 470–399 BCE) wrote nothing. Our knowledge comes mainly from Plato's dialogues, also from Xenophon and from Aristophanes' comedy. "
          "Scholars call the difficulty of knowing what the real Socrates thought the **Socratic problem**. The positions below are those that are standard in textbooks; check yours."),
        KEY("Core ideas of Socrates", "These are standard attributions.", cards=[
            ["Knowing one's ignorance", "He claimed not to have wisdom but to know that he lacked it. The oracle at Delphi was said to have called him the wisest, and he explained this as recognising his own ignorance. It is a starting point of enquiry, not a pose."],
            ["Definitions", "He asked 'What is justice?', 'What is courage?', seeking a universal definition, not a list of examples."],
            ["Virtue is knowledge", "No one knowingly does wrong; wrongdoing comes from ignorance of what is truly good. So virtue can be taught, if goodness is knowledge."],
            ["The soul and the examined life", "The care of the soul matters more than wealth or reputation. A life without self-examination, in the traditional summary of his attitude from Plato's Apology, is not worth living."],
        ]),
        T("The method is **dialectic**: elenchus (testing), irony (feigned ignorance) and maieutics (helping others bring ideas to birth), all described in the lesson on methods. "
          "The Board has asked which process describes knowledge for Socrates; the answer is dialectic."),
        H("The trial"),
        T("In 399 BCE Socrates was tried in Athens on charges of **impiety** (not honouring the city's gods) and **corrupting the young**. He was found guilty and sentenced to death by drinking hemlock. "
          "Plato's *Apology* gives his defence; *Crito* and *Phaedo* describe his refusal to escape and his last day. "
          "Historians discuss the political background: Athens had recently suffered defeat in war and civil strife, and Socrates had been associated with men who had turned against the democracy. Check your textbook for how much weight the political reading deserves."),
        H("Sophists and Socrates compared"),
        KEY("Similarities and differences", "A comparison question is likely; organise by theme.", cards=[
            ["Similarity", "Both turn attention to human affairs; both use argument; both criticise unreflective belief in tradition."],
            ["Truth", "Sophists (Protagoras): relative to the person or group. Socrates: there are real answers to questions like 'What is justice?', which we should keep seeking."],
            ["Aim and payment", "Sophists: practical success and rhetoric, for a fee. Socrates: care of the soul, for no fee."],
            ["Virtue", "Sophists: skills for success, or convention. Socrates: knowledge of the good, the same for everyone."],
        ]),
        EX("Worked example 1: apply relativism to a moral question", intro="A trader says: 'Giving short measure is fine here because everyone does it. It is only wrong where people think it is wrong.' Analyse using the Sophists and Socrates.", steps=[
            S("Identify the position", text="The trader uses ethical relativism: right and wrong depend on convention (nomos)."),
            S("Sophist support", text="Protagoras-style: what seems right in a community is right for that community. Different markets, different rules."),
            S("Socratic reply", text="Ask: What is justice? Does the buyer agree to be cheated? Does the trader want to be cheated? Elenchus may show that he accepts a rule (fair treatment) that his practice breaks."),
            S("Evaluation", text="Relativism rightly warns us about imposing local customs as universal. But if no practice can be called wrong, even cruelty is beyond criticism. A careful answer separates harmless differences of custom from basic wrongs."),
        ]),
        EX("Worked example 2: model essay plan", intro="'Socrates was a Sophist.' Discuss.", steps=[
            S("Introduction", text="Define Sophist. Thesis: Socrates resembled the Sophists in some ways, but differs on payment, aim and truth."),
            S("For", text="Athenians such as Aristophanes lumped him with them; both questioned tradition and used argument; both focused on human matters."),
            S("Against", text="No fees; no promise of success in politics; belief in objective definitions of virtue, against Protagoras' relativism; devotion to truth, not persuasion."),
            S("Evaluation", text="The distinction is clearer in Plato's picture of him; check how much of it is Plato's propaganda. We cannot be sure."),
            S("Conclusion", text="Socrates shared the Sophists' turn to ethics, but he was not a Sophist."),
        ]),
        TIP("Exam link: Sophists and Socrates appear in Paper 1 (the Board's report shows Protagoras and the Socratic process) and in Paper 2 essays on ancient thought. Quote doctrines in your own words and give one criticism per thinker, as the report advises evaluating individual thinkers."),
        MISTAKE("Saying the Sophists all taught that truth is relative", "That is Protagoras' position. Gorgias stressed the power of speech and made sceptical claims; Thrasymachus made a claim about justice. Treat each separately."),
        MISTAKE("Quoting Socrates as if his words were certain", "Socrates wrote nothing. Say 'in Plato's account'. Never invent quotations."),
        MISTAKE("Confusing 'virtue is knowledge' with 'everyone is good'", "Socrates held that people do wrong because they lack knowledge of the good, not that everyone already acts well."),
        QUIZ("Which doctrine is attributed to Protagoras?",
             ["The soul is tripartite", "Man is the measure of all things (relativism)", "Everything is made of atoms", "Justice is the advantage of the stronger"], 1,
             "Protagoras is linked with relativism: things are as they appear to each person.",
             feedback=["That is Plato.", "", "That is Democritus.", "That is Thrasymachus in the Republic."]),
        QUIZ("'Virtue is knowledge' means for Socrates that",
             ["only rich people can be good", "wrongdoing comes from ignorance of what is truly good", "virtue cannot be taught or understood", "knowledge is unimportant for morals"], 1,
             "No one knowingly does wrong; if people knew the good they would do it.",
             feedback=["Wealth plays no role.", "", "If virtue is knowledge it can be taught.", "Knowledge is central, not unimportant."]),
        PQ("Who were the Sophists, and why do historians treat them more fairly than Plato did?",
           "Model answer: professional teachers of rhetoric and practical skill in Greek cities who charged fees. Plato and Aristotle attacked them as clever but unconcerned with truth, so 'sophistry' became an insult. "
           "Historians stress that democratic Athens needed such teaching and that Sophists such as Protagoras raised real questions about convention, truth and education."),
        PQ("Explain Protagoras' relativism and give one objection and one reply.",
           "Model answer: things are as they appear to each person (or group). Objection: if all views are true for the one who holds them, the view that relativism is false is also true for its holder, so relativism cannot be argued for or against. "
           "Reply: relativism can be limited to customs and values, respecting differences, and does not need to claim that every statement of fact is only relative."),
        PQ("Discuss the view that Socrates' philosophy is a reaction against the Sophists.",
           "Model plan: Sophist positions (relative truth, rhetoric, fees, convention). Socrates' counter-positions: real definitions, virtue as knowledge, care of the soul, no fee. Also shared ground (turn to human affairs, critical questioning). "
           "Evaluation: our picture of Socrates comes mostly from Plato, who has his own reasons for the contrast. Judgement: partly a reaction, partly a shared movement."),
        SUM("The Sophists were paid teachers of rhetoric who turned thought towards human affairs.",
            "Protagoras: relativism; Gorgias: the power of speech and a sceptical argument; Thrasymachus: justice as the advantage of the stronger.",
            "Nomos and physis: convention against nature as the basis of law and justice.",
            "Socrates: dialectic, search for definitions, virtue is knowledge, the examined life; condemned in 399 BCE for impiety and corrupting the young.",
            "Socrates is known only through others (the Socratic problem), so attribute carefully."),
    ],
))

# ---------------------------------------------------------------------------
# M2 / Plato
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M2, topic="Plato",
    title="Plato: the Theory of Forms, the divided line and the Republic",
    slug="psl1-plato-forms-republic",
    minutes=25,
    summary="Plato's Forms, the divided line and the cave, recollection, the tripartite soul and the ideal city of the Republic with philosopher-rulers, together with the main objections.",
    objectives=[
        "Explain the Theory of Forms and why Plato held it",
        "Describe the four levels of the divided line and the allegory of the cave",
        "Outline Plato's tripartite soul and the ideal city with its three classes",
        "Evaluate the theory of Forms and the rule of philosopher-kings",
    ],
    key_concepts=["Form", "Divided line", "Allegory of the cave", "Recollection", "Tripartite soul", "Philosopher-king"],
    blocks=[
        H("Introduction"),
        T("Think of a hundred chairs in a school: wooden, plastic, broken, new. All are chairs. What do they share? And a perfectly round circle exists nowhere on a school blackboard, yet mathematicians reason about it. "
          "Plato (about 427–347 BCE), a pupil of Socrates and founder of the Academy in Athens, answered with a bold theory: there are **Forms**, perfect and unchanging patterns, and the things we see are copies. "
          "He wrote dialogues, and the best known works for your syllabus are the *Republic*, the *Phaedo* and the *Meno*."),
        D("In Plato, a **Form** (or Idea) is an eternal, unchanging, non-material reality that is the true nature of a kind of thing: the Form of Beauty, Justice, Equality, the Good. "
          "Particular things are called *beautiful* or *just* because they **participate** in (imitate) the Form. Forms are known by reason, not by the senses.", title="Form"),
        H("Why Forms?"),
        KEY("Three reasons for the theory", "Each answers a problem.", cards=[
            ["The One over many", "Many different things share one name (many beautiful things, one Beauty). Something must be common to them all."],
            ["Change and knowledge", "Physical things always change (Heraclitus), but knowledge must be stable and certain (Parmenides). So the objects of knowledge must be unchanging: the Forms."],
            ["Ethics and definition", "Socrates sought universal definitions of justice and courage. Plato holds that these definitions are of real, objective Forms, which answers the relativism of the Sophists."],
        ]),
        T("Plato also argued for **recollection** (*anamnesis*), especially in the *Meno*: since we can recognise perfect equality although no equal things we see are perfectly equal, "
          "the soul must have known the Forms before birth, and learning is recalling. This links with Socratic maieutics."),
        H("The divided line"),
        IMG("alpsl1-divided-line.svg", alt="A vertical line divided into four sections. From bottom to top: imagination (shadows and images), belief (physical things), thought (mathematical objects), understanding (the Forms). The two lower sections form the visible world, the two upper the intelligible world.",
            caption="Figure 1. Plato's divided line (names of the four levels differ slightly between translations)."),
        T("In the *Republic* Plato uses a line to show levels of reality and knowledge. The **visible world** (opinion) contains shadows and reflections (**imagination**) and the physical objects they copy (**belief**). "
          "The **intelligible world** (knowledge) contains mathematical objects reasoned about with diagrams and assumptions (**thought**, *dianoia*) and finally the Forms themselves, grasped by pure reason (**understanding**, *noesis*). "
          "The Board's report notes that the lowest level of reality is the image and the highest the Forms, matched to the mental states of imagining and the highest intelligence. Textbooks name the four states slightly differently, so check yours."),
        H("The allegory of the cave"),
        T("Prisoners chained in a cave since childhood see only shadows on a wall, cast by objects carried past a fire behind them. They think the shadows are the real things. "
          "A prisoner who is freed climbs out of the cave, is dazzled by the sun, and slowly learns to see real things; the sun stands for the **Form of the Good**, the source of all truth and being. "
          "If he returns to tell the others, they laugh at him and may kill him. The cave is an image of education: the soul turns from the world of appearance towards knowledge of the Forms."),
        H("The soul and the ideal city"),
        D("Plato divides the soul into three parts: **reason** (seeks truth and rules wisely), **spirit** (courage, anger, honour) and **appetite** (desires for food, money, pleasure). "
          "A person is just when each part does its own work, with reason in command and spirit as its ally.", title="Tripartite soul"),
        T("The city mirrors the soul. The *Republic* proposes three classes: **rulers** (guardians, with reason, trained for years in mathematics and dialectic until they know the Good), "
          "**auxiliaries** (soldiers and defenders, with spirit), and **producers** (farmers, artisans, traders, with appetite). Justice in the city is each class doing its own work without meddling in another's. "
          "The rulers must be **philosopher-kings**: only those who know the Good can rule well, in the way a trained doctor is better than a crowd at healing. Education is the key, and Plato was willing to give women who showed the ability the same training; he also proposed limits on property for the ruling class."),
        EX("Worked example 1: apply the divided line", intro="A Form of Justice, a courtroom, a painting of a courtroom, and a geometry proof: place each on the divided line.", steps=[
            S("Image", text="The painting of the courtroom is an image of a physical thing: the level of imagination."),
            S("Physical object", text="The actual courtroom belongs to belief, the world of changing things that we see and touch."),
            S("Mathematical object", text="The geometry proof uses ideal circles and triangles, grasped by reasoning from assumptions: the level of thought (dianoia)."),
            S("Form", text="The Form of Justice is known only by pure reason (noesis) and is the highest level."),
        ]),
        H("Evaluation: objections and replies"),
        KEY("Main criticisms", "Use these with the replies.", cards=[
            ["Third man argument", "If a Form of Man explains why men are alike, a further Form is needed to explain what the Form and the men share, and so on without end. Plato raises this problem himself in the Parmenides. Reply: Forms may not be 'men' in the same sense; scholars debate the answer."],
            ["Aristotle: forms are in things", "The Forms are separate and add a second world that explains nothing. Aristotle puts form inside substances. Reply: Plato needs separate Forms to guarantee stable knowledge."],
            ["Elitism and authority", "Philosopher-kings rule without consent and Plato allows censorship and a lie to keep order. Critics such as Karl Popper called this a dangerous authoritarian blueprint (scholars dispute his reading). Defenders point to Plato's aim of rule by knowledge and of justice for all."],
            ["Mystery of participation", "How exactly do things share in Forms? Plato uses images (copying, sharing) but gives no complete account."],
        ]),
        EX("Worked example 2: model essay plan", intro="'Plato's Theory of Forms is unnecessary.' Discuss.", steps=[
            S("Introduction", text="Explain the theory and the problems it solves: unity in diversity, stable knowledge, objective ethics."),
            S("For the claim", text="Third man regress; no clear account of participation; Aristotle explains kinds without a second world; empiricists say we learn concepts from experience."),
            S("Against the claim", text="It explains how knowledge of mathematics and ethics can be universal and certain; modern debates about universals and abstract objects show the problem is real."),
            S("Evaluation", text="The Forms may be too extravagant a solution, but the problems they address remain. Aristotle keeps the problem and moves the answer."),
            S("Conclusion", text="Not 'unnecessary' as a problem-solver, but contested as a solution."),
        ]),
        TIP("Exam link: Plato appears in Paper 1 (the Board's report shows a divided-line question) and often in Paper 2 essays. Know the line, the cave, the soul and the city, and give at least one criticism of each."),
        MISTAKE("Saying that Plato denies the physical world exists", "He holds that it is real but less real than the Forms: it changes and is only a copy. The Forms are the true objects of knowledge."),
        MISTAKE("Mixing the divided line with the cave", "They are different images with a similar message. The line gives levels of knowledge; the cave gives a story of education and the role of the Good. Say which you are using."),
        MISTAKE("Calling Plato a democrat or a modern totalitarian without argument", "Say what the text proposes (rule by the knowledgeable) and give the reading you defend. Avoid labels without evidence."),
        QUIZ("In Plato's divided line, which level corresponds to the Forms?",
             ["Imagination", "Belief", "Thought (mathematical reasoning)", "Understanding (noesis)"], 3,
             "The Forms are known by understanding, the highest state of mind.",
             feedback=["Imagination concerns shadows and images.", "Belief concerns physical things.", "Thought concerns mathematical objects, one level below the Forms.", ""]),
        QUIZ("According to the Republic, justice in the soul is",
             ["appetite ruling reason", "each part of the soul doing its own work with reason in command", "pleasure for the largest number", "obedience to law only"], 1,
             "In the just soul, reason rules, spirit supports it and appetite is controlled.",
             feedback=["That is the unjust soul.", "", "That is utilitarianism, not Plato.", "Plato's account is about the order of the soul, not mere obedience."]),
        PQ("Explain Plato's allegory of the cave and say what it teaches about knowledge.",
           "Model answer: prisoners see shadows and think them real; a freed prisoner climbs out and sees real things and the sun (Form of the Good); on returning he is mocked. "
           "It teaches that the visible world is like shadows, that real knowledge is of the Forms, that education is turning the soul around, and that the knower may meet hostility if he returns to teach."),
        PQ("Describe Plato's ideal city and its three classes, linking each to a part of the soul.",
           "Model answer: rulers (reason; philosopher-kings trained to know the Good), auxiliaries (spirit; courage and defence), producers (appetite; provision of needs). Justice is each class doing its own work. "
           "The city mirrors the soul, in which reason should rule spirit and appetite."),
        PQ("'Philosopher-kings should rule.' Evaluate Plato's argument.",
           "Model plan: argument: ruling is a skill requiring knowledge of the Good, like medicine, so those with knowledge should rule. For: expertise and education matter; ignorant or selfish rulers do harm. "
           "Against: no one has certain knowledge of the Good; rulers without accountability can abuse power; Plato's controls on thought and the family are severe. Judgement: the argument shows the value of expertise but does not show that experts should rule without consent."),
        SUM("Forms are eternal, non-material patterns known by reason; particulars participate in them.",
            "Plato's reasons: unity of many things under one name, stable knowledge in a world of change, objective ethics against relativism.",
            "Divided line: imagination, belief, thought, understanding; cave: education turning towards the Form of the Good.",
            "Tripartite soul (reason, spirit, appetite) mirrored in the three classes; justice is each doing its own work; philosopher-kings rule.",
            "Objections: the third man regress, separation of Forms (Aristotle), authoritarian rule, unexplained participation."),
    ],
))

# ---------------------------------------------------------------------------
# M2 / Aristotle
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M2, topic="Aristotle",
    title="Aristotle: hylomorphism, the four causes and virtue ethics",
    slug="psl1-aristotle",
    minutes=25,
    summary="Aristotle's reply to Plato (form in things), substance as matter plus form, potentiality and actuality, the four causes, and virtue ethics: eudaimonia, the mean and practical wisdom, with objections.",
    objectives=[
        "Explain Aristotle's criticism of Plato's Forms and his hylomorphism",
        "Apply the four causes, and potentiality and actuality, to examples",
        "Explain eudaimonia, the function argument, virtue as a mean and practical wisdom",
        "Evaluate virtue ethics with objections and replies",
    ],
    key_concepts=["Substance", "Hylomorphism", "Four causes", "Potentiality and actuality", "Eudaimonia", "The mean", "Phronesis"],
    blocks=[
        H("Introduction"),
        T("Aristotle (384–322 BCE) came from Stagira, studied twenty years in Plato's Academy, tutored the young Alexander of Macedon and founded his own school, the Lyceum. "
          "He wrote on logic, physics, biology, metaphysics, ethics, politics, rhetoric and poetry. Where Plato looked away from the changing world to the Forms, Aristotle looked closely at living things and ordinary objects. "
          "His thought dominated learning for centuries, including in the medieval world (Aquinas, later in this module)."),
        H("Against separate Forms; substance"),
        D("For Aristotle the basic reality is the individual **substance** (*ousia*): this man, this tree, this stone. The Board's report notes that the being of a thing, for Aristotle, is substance, "
          "a compound in which matter and form are co-principles, not substance as matter alone or form alone.", title="Substance"),
        T("Aristotle accepts that there are kinds (humans, trees) and that knowledge is of the general, but he denies that Forms exist apart from things. "
          "The form of a horse is not in another world; it is in each horse, as its shape, organisation and way of living. "
          "A separate Form, he argues, would explain nothing (it does not move or cause), and it raises the third man regress."),
        D("The view that every natural substance is a compound of **matter** (*hyle*, what it is made of) and **form** (*morphe*, what it is organised as, its structure and nature). "
          "Matter and form cannot be separated in reality. A bronze statue is bronze (matter) shaped as a person (form). A living thing's form is its soul (its way of living).", title="Hylomorphism"),
        H("Potentiality and actuality"),
        T("Change is explained by **potentiality** (*dynamis*, capacity to become something) and **actuality** (*energeia*, being it fully). "
          "An acorn is potentially an oak; the oak is the actual form. A child can potentially speak. Against Parmenides, who said change is impossible, Aristotle answers that nothing comes from sheer non-being: "
          "it comes from something that is potentially that thing. So change is real and intelligible."),
        H("The four causes"),
        KEY("Four answers to 'why?'", "A cause is a type of explanation. Use the standard bronze statue example.", cards=[
            ["Material cause", "What it is made of. Bronze."],
            ["Formal cause", "Its form, pattern or definition. The shape of the person."],
            ["Efficient cause", "What brings about the change. The sculptor and his tools."],
            ["Final cause", "The purpose or end for the sake of which. To honour the person, to be admired."],
        ]),
        T("The final cause shows Aristotle's **teleology**: natural things have ends. An acorn tends to grow into an oak; the eye is for seeing. Modern science mostly avoids final causes in nature, "
          "explaining adaptation by natural selection. A balanced essay notes that teleology is still natural when explaining artefacts and living functions, but contested for the whole of nature."),
        EX("Worked example 1: the four causes of a house", intro="Give the four causes of a house built in Buea.", steps=[
            S("Material", text="Cement blocks, timber, roofing sheets."),
            S("Formal", text="The plan: rooms arranged for dwelling, the structure of the design."),
            S("Efficient", text="The builders, masons and carpenters at work."),
            S("Final", text="Shelter and family life: the end for which it is built."),
        ]),
        H("Virtue ethics"),
        D("Aristotle's ethics asks 'what is the best life?'. His answer is **eudaimonia**, usually translated 'happiness', 'flourishing' or 'living well'. It is not a feeling but a way of living: "
          "activity of the soul in accordance with excellence (virtue) over a complete life, with enough external goods (health, friends, some wealth) to act well.", title="Eudaimonia"),
        T("The **function argument**: each kind of thing has a characteristic function (the function of a knife is to cut; a good knife cuts well). The characteristic function of humans is rational activity of the soul, "
          "so the good human life is the life of reason exercised well. Critics say it moves illegitimately from what a thing *does* to what it *ought* to do, and that humans may have no single function."),
        D("A **moral virtue** is a settled disposition of character, formed by habit, to choose the **mean** between two extremes, a mean relative to us and to the situation, not an exact arithmetic middle. "
          "Courage is the mean between cowardice (too little confidence) and rashness (too much). Generosity lies between meanness and wastefulness. "
          "Not every action has a mean: murder or adultery are wrong in themselves.", title="Virtue and the mean"),
        T("Virtues of character are acquired by **habituation**: we become just by doing just acts, as we learn the lyre by playing it. "
          "**Phronesis** (practical wisdom) is the intellectual virtue that sees what to do in a particular case. Without it, good intentions can go wrong. "
          "Aristotle also distinguishes intellectual virtues (taught) from moral virtues (habit)."),
        EX("Worked example 2: the mean in action", intro="Fatou sees a market fight and her friend is involved. Use the mean to describe courage.", steps=[
            S("Deficiency", text="Running away and leaving her friend: cowardice."),
            S("Excess", text="Throwing herself at several armed attackers without a plan: rashness."),
            S("The mean", text="Calling for the market guards and standing beside her friend while keeping herself out of needless danger: courage, as practical wisdom judges in the situation."),
            S("Note", text="The mean is relative to the person and the circumstances, and needs phronesis, not a fixed formula."),
        ]),
        H("Evaluation of virtue ethics"),
        KEY("Objections and replies", "A balanced answer uses both.", cards=[
            ["Action-guidance", "Objection: 'be virtuous' tells us little about what to do in a dilemma. Reply: the virtuous person (phronimos) and practical wisdom supply guidance in context; rules cannot cover every case."],
            ["Vagueness of the mean", "Objection: the mean is not precise. Reply: ethics is not as exact as mathematics, and Aristotle says so."],
            ["Cultural bias", "Objection: his list of virtues reflects Greek, male, slave-owning society and his views on women and slaves are widely criticised. Reply: the structure (character, flourishing) can be separated from those views."],
            ["Circularity", "Objection: the virtuous act is what the virtuous person does, and the virtuous person is the one who acts virtuously. Reply: virtue is tied to flourishing and the function of humans."],
        ]),
        TIP("Exam link: Aristotle is Paper 1 material (the Board's report shows a question on the being of a thing for Aristotle) and a popular Paper 2 topic (hylomorphism, causality, virtue ethics). Always give an example for each cause."),
        MISTAKE("Saying that 'substance' means matter only", "Substance is the individual composite of matter and form. Say 'matter and form are co-principles of substance'."),
        MISTAKE("Calling the final cause the last event in time", "The final cause is the purpose for the sake of which something happens, not the last moment."),
        MISTAKE("Taking the mean as 'always do the average'", "The mean is relative to the person and situation and needs practical wisdom; some acts have no mean."),
        QUIZ("According to Aristotle, the being of a thing is",
             ["matter alone", "form alone", "metaphysics", "substance, a compound of matter and form"], 3,
             "Substance is the compound in which matter and form are co-principles.",
             feedback=["Matter alone is only one principle.", "Form alone is only one principle (the Platonic mistake).", "Metaphysics is a branch of study, not a being.", ""]),
        QUIZ("The sculptor who carves a statue is its",
             ["material cause", "formal cause", "efficient cause", "final cause"], 2,
             "The efficient cause is what brings the change about.",
             feedback=["Material cause: the bronze or stone.", "Formal cause: the shape or design.", "", "Final cause: the purpose, such as honouring someone."]),
        PQ("Explain Aristotle's four causes with one example.",
           "Model answer: example of a bronze statue. Material cause: bronze. Formal cause: the shape of the figure. Efficient cause: the sculptor. Final cause: the purpose, for example to honour a person. "
           "Add that Aristotle held that a full explanation of a thing mentions all four."),
        PQ("Explain Aristotle's view that virtue is a mean, and illustrate it.",
           "Model answer: moral virtue is a settled disposition to choose the mean between excess and deficiency, relative to us and decided by practical wisdom. Courage lies between cowardice and rashness; generosity between meanness and wastefulness. "
           "Some acts, such as murder, have no mean. Virtues are formed by habit."),
        PQ("Compare Aristotle's view of form with Plato's Theory of Forms.",
           "Model plan: Plato: Forms are separate, eternal, more real than things; known by reason. Aristotle: form is in the individual substance with matter; knowledge is of the general in the particular. "
           "Aristotle's objections: separate Forms explain nothing and lead to a regress. Plato's reply: stable knowledge needs unchanging objects. Judgement: Aristotle's view is closer to experience; Plato's explains certain knowledge. Both agree knowledge is of what is general."),
        SUM("Aristotle rejects separate Forms: form is in things; substance is a compound of matter and form (hylomorphism).",
            "Change is explained by potentiality and actuality, against Parmenides.",
            "Four causes: material, formal, efficient, final; final causes express teleology.",
            "Eudaimonia is flourishing through rational activity and virtue; virtue is a habit of choosing the mean, guided by practical wisdom.",
            "Objections: vague action-guidance, the mean, cultural bias and circularity, each with possible replies."),
    ],
))

# ---------------------------------------------------------------------------
# M2 / The Hellenistic schools
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M2, topic="The Hellenistic schools",
    title="Epicureanism, Stoicism and Scepticism: philosophies for living",
    slug="psl1-hellenistic-schools",
    minutes=23,
    summary="Three schools of the Hellenistic age that offered ways to a calm life: Epicurus on pleasure and fear, the Stoics on nature, reason and control, and the Sceptics on suspending judgement, with a fair evaluation of each.",
    objectives=[
        "Explain why Hellenistic philosophy turned towards the art of living",
        "Describe Epicurean physics and ethics, including ataraxia and the view of death",
        "Describe Stoic logos, living according to nature and the dichotomy of control",
        "Describe Pyrrhonian scepticism and epoche, and compare the three schools",
    ],
    key_concepts=["Ataraxia", "Hedonism", "Logos", "Apatheia", "Epoche", "Scepticism"],
    blocks=[
        H("Introduction"),
        T("After the death of Alexander the Great in 323 BCE the independent Greek city-states lost power. Life became insecure: wars between his successors, large kingdoms, strangers in cities. "
          "People asked less 'what is the ideal city?' and more 'how can I live calmly and well in an uncertain world?'. This is the **Hellenistic** age (from about 323 BCE). "
          "Three schools offered answers: **Epicureanism**, **Stoicism** and **Scepticism**. Each links a view of the world (physics or logic) with a way of living, so each is a philosophy for life."),
        D("A state of freedom from disturbance, inner calm. It is the goal of all three schools, though each reaches it by a different route: by removing fear and needless desire (Epicurus), "
          "by accepting what cannot be controlled (Stoics), or by suspending judgement (Sceptics).", title="Ataraxia"),
        H("Epicureanism"),
        T("Epicurus (341–270 BCE) taught in a garden in Athens, open to friends of both sexes and to slaves. He adopted the **atomism** of Democritus: everything is atoms and void, "
          "including the soul, which dissolves at death. Gods, if they exist, do not interfere in the world. (A small 'swerve' of atoms allows free action; its details are debated.)"),
        KEY("Epicurean ethics", "Pleasure is the good, but it is understood carefully.", cards=[
            ["Hedonism", "Pleasure is the highest good and pain the greatest evil. But the highest pleasure is **absence of pain in the body (aponia) and of disturbance in the mind (ataraxia)**, not luxurious feasting."],
            ["Kinds of desire", "Natural and necessary (food, shelter, friendship), natural but unnecessary (luxury food), and empty (fame, great wealth). Satisfy the first, limit the second, avoid the third."],
            ["Death", "Death is nothing to us: when death is, we are not; while we are, death is not. Once the soul is atoms that disperse, there is no experience, so fear of death is groundless."],
            ["Friendship and prudence", "Friendship is the greatest source of security and joy. Prudent choice weighs pleasures against later pains."],
        ]),
        T("Critics say the theory sets the goal too low (pleasure), that 'death is nothing to us' ignores the loss of future goods, and that withdrawing from public life is selfish. "
          "Defenders reply that Epicurus values virtue and friendship as the means to a stable pleasure, and that his therapy of fear is psychologically wise."),
        H("Stoicism"),
        T("The Stoics take their name from the *Stoa* (painted porch) in Athens where **Zeno of Citium** (about 334–262 BCE) taught. Later Stoics include Seneca and Epictetus (a former slave) and the emperor Marcus Aurelius, all of the Roman period. "
          "The Stoics held that the universe is a rational, ordered whole governed by **logos** (reason, also called providence or fate). Everything happens by cause and necessity, and the wise person lives **according to nature**, that is, according to reason."),
        KEY("Core Stoic ideas", "These give the structure of an answer.", cards=[
            ["Virtue is sufficient for happiness", "Virtue (wisdom, courage, justice, self-control) is the only true good. Wealth, health and reputation are 'preferred indifferents': useful but not good in themselves."],
            ["Control", "Epictetus distinguishes what is up to us (our judgements, desires, choices) from what is not (body, property, reputation, others' actions). Peace comes from caring only about the first. This is often called the **dichotomy of control**."],
            ["Emotions", "Passions such as fear and anger are mistaken judgements. The wise person aims at **apatheia** (freedom from destructive passions), not at feeling nothing."],
            ["Cosmopolitanism", "All human beings share reason, so all belong to one world community."],
        ]),
        T("Criticisms: Stoicism may encourage passivity or accepting injustice; the claim that virtue alone suffices for happiness seems too strong for someone in extreme pain or loss; and fate seems to conflict with moral responsibility. "
          "Stoics reply that we are responsible for how we judge and act, and that Stoic influence led to political service and a belief in human equality."),
        H("Scepticism"),
        T("**Pyrrho** of Elis (about 360–270 BCE) is the founder of the school we call Pyrrhonian scepticism, known to us mainly through a later writer, Sextus Empiricus. "
          "The sceptic observes that for every argument there is an equally strong argument against, and so **suspends judgement** (*epoche*). "
          "Surprisingly, this leads to ataraxia: once we stop insisting that things must be one way, we are freed from the anxiety of dogmatic belief. "
          "A sceptic still lives by appearances, customs and needs: he can say 'honey seems sweet' without claiming how it is in itself. "
          "A different school, the Academic Sceptics, led by Arcesilaus and Carneades, argued that certain knowledge is impossible but that some beliefs are more probable than others."),
        T("Criticisms: if the sceptic suspends judgement on everything, can he act? Is the claim that 'nothing can be known' self-refuting? The Pyrrhonist replies that he does not assert it as a dogma, only reports how things seem to him now."),
        EX("Worked example 1: one event, three responses", intro="A trader in Douala loses all her stock in a flood. Show how each school would counsel her.", steps=[
            S("Epicurean", text="Do not add fear and regret to the loss. Return to natural and necessary needs, rely on friends, and rebuild simply. Pleasure comes from calm, not wealth."),
            S("Stoic", text="The flood was not in her control; her judgement about it is. Do not call the loss an evil in itself; focus on virtue and on what she can do now: plan, work, help others."),
            S("Sceptic", text="Suspend judgement on whether the loss is really good or bad overall. Live by common practice, avoid claims about how things must be, and so avoid extra anguish."),
        ]),
        EX("Worked example 2: model essay plan", intro="Compare Stoic and Epicurean accounts of the good life.", steps=[
            S("Similarities", text="Both aim at inner calm; both link ethics to a view of nature; both are open to all, including slaves and women; both reject the pursuit of wealth and fame."),
            S("Differences: the good", text="Epicurus: pleasure (as absence of disturbance). Stoics: virtue alone."),
            S("Differences: nature", text="Epicurus: atoms, no providence. Stoics: rational cosmos and providence."),
            S("Differences: public life", text="Epicureans withdraw to the garden; Stoics encourage service in public life."),
            S("Evaluation", text="Stoicism sets a demanding standard and risks passivity; Epicureanism is gentler but may seem too low in aim. Both give practical therapy for fear and anxiety."),
        ]),
        TIP("Exam link: the Hellenistic schools are tested in Paper 1 and in Paper 2 essays on ancient thought; they also link to later topics (Epicurean hedonism with utilitarianism, Stoic duty with Kant). Always name the goal (ataraxia) and the method of each school."),
        MISTAKE("Calling Epicureans 'people who eat and drink all day'", "Epicurus defended simple living; the highest pleasure is freedom from pain and disturbance. The popular use of 'epicure' misleads."),
        MISTAKE("Saying that Stoics feel no emotion at all", "Stoics aim to remove destructive passions that come from false judgements, and they allow good feelings such as joy in virtue and goodwill."),
        MISTAKE("Confusing scepticism with denial", "The Pyrrhonian suspends judgement; he does not assert that nothing exists or that nothing can be known."),
        QUIZ("For Epicurus, death is",
             ["the greatest evil", "nothing to us, since when we are, death is not, and when death is, we are not", "a punishment from the gods", "a reason to avoid friendship"], 1,
             "Because the soul is atoms that disperse, death brings no experience, so there is nothing to fear.",
             feedback=["He argues the opposite.", "", "The gods do not interfere.", "Friendship is a great good for Epicurus."]),
        QUIZ("The Stoic dichotomy of control says that we should",
             ["try to control everything", "concentrate on what is up to us (our judgements and choices) and accept the rest", "avoid all actions", "treat reputation as the highest good"], 1,
             "Peace comes from caring about our own judgements, desires and choices, not about what lies outside our power.",
             feedback=["Stoics warn against trying to control what cannot be controlled.", "", "Stoics encourage action in accord with virtue.", "Reputation is outside our control and is only an indifferent."]),
        PQ("Explain how Epicurus reaches the view that death is nothing to us.",
           "Model answer: Epicurus adopts atomism, so the soul is made of atoms that disperse at death. Experience needs a living soul. Where death is, we are not; where we are, death is not. "
           "So death cannot harm us and fear of it is groundless. Objection: death deprives us of the goods of future life. Reply: this deprivation is not felt, and our life can be complete when we have enjoyed it wisely."),
        PQ("What do the Stoics mean by living according to nature?",
           "Model answer: the universe is ordered by logos. Humans share reason, so living according to nature means living according to reason: practising virtue, judging rightly, accepting what is not in our control and acting for the common good. "
           "Evaluation: it gives courage in hardship, but critics say it can encourage passivity and that virtue alone may not suffice for happiness."),
        PQ("Discuss whether scepticism can lead to a calm life.",
           "Model plan: Pyrrhonian argument: equally strong arguments on both sides lead to suspension of judgement and then calm. For: it removes dogmatic anxiety and tolerates differences. "
           "Against: how can the sceptic act without beliefs; is the sceptical position itself self-refuting? Reply: he lives by appearances and custom and does not assert a dogma. Judgement: it gives a partial therapy but is hard to live consistently."),
        SUM("Hellenistic philosophy begins after Alexander's death (323 BCE) and focuses on the art of living and inner calm (ataraxia).",
            "Epicureanism: atomism, pleasure as freedom from pain and disturbance, natural and necessary desires, death is nothing to us.",
            "Stoicism: rational cosmos (logos), virtue sufficient for happiness, dichotomy of control, apatheia.",
            "Scepticism (Pyrrho, Sextus Empiricus): equal arguments on both sides, suspension of judgement (epoche), then calm.",
            "Each school has a clear aim and a standard objection; compare them by goal, view of nature and attitude to public life."),
    ],
))

# ---------------------------------------------------------------------------
# M2 / Augustine and Aquinas
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M2, topic="Augustine and Aquinas",
    title="Augustine, Aquinas, faith and reason, and the Five Ways",
    slug="psl1-augustine-aquinas",
    minutes=25,
    summary="Medieval philosophy in two thinkers: Augustine on faith, evil, will and time, and Aquinas on faith and reason and the Five Ways, with the standard objections to each.",
    objectives=[
        "Explain the relationship between faith and reason in Augustine and Aquinas",
        "Explain Augustine's account of evil as privation and of free will",
        "State each of Aquinas' Five Ways in your own words",
        "Evaluate the Five Ways with objections and replies, without taking a religious side",
    ],
    key_concepts=["Faith and reason", "Privation of good", "Free will", "Natural theology", "Five Ways", "First mover"],
    blocks=[
        H("Introduction"),
        T("Medieval philosophy (roughly the fifth to the fifteenth century) developed in Christian, Muslim and Jewish communities, which asked how reason relates to a faith received from scripture. "
          "In your syllabus the two great Christian figures are **Augustine of Hippo** (354–430), a North African bishop born in Thagaste (in present-day Algeria), and **Thomas Aquinas** (about 1225–1274), an Italian friar and teacher in Paris. "
          "This lesson explains their arguments as philosophy, not as preaching. You are asked to understand and evaluate them, and you may agree or disagree with their religious conclusions. "
          "The Board's 2023 report says Medieval Philosophy was not covered in Paper 2 that year, which does not mean it will not be asked, and Paper 1 covers the whole syllabus."),
        D("The question of how truths known by **faith** (accepting what is revealed on trust or authority) are related to truths known by **reason** (argument and evidence). "
          "Positions include conflict, independence, and harmony. For Aquinas, according to the Board's report, they are hierarchically related: reason serves theology (*ancilla theologiae*, handmaid of theology) while remaining its own source of truths.", title="Faith and reason"),
        H("Augustine"),
        KEY("Main Augustinian ideas", "Learn these four with an objection each.", cards=[
            ["Faith seeking understanding", "In the usual summary, Augustine holds that one believes in order to understand: faith prepares reason, and reason clarifies faith. He used Platonic (Neoplatonic) ideas to explain Christian belief."],
            ["Evil as privation", "God, the supreme good, made everything good. Evil is not a thing but a **lack or corruption of good**, like blindness as a lack of sight. This answers the question how a good God can allow evil: evil has no substance of its own."],
            ["Free will", "Moral evil comes from the misuse of free will: the will turns from the higher good to lower goods. Humans, not God, are responsible for it. Augustine also holds that human will is wounded by original sin and needs grace."],
            ["Time", "In the Confessions he asks what time is. We cannot grasp the past (gone) or the future (not yet) or a present with no length. He suggests time is a stretch of the mind: memory of the past, attention to the present, expectation of the future."],
        ]),
        T("Objections: the privation view seems to understate the reality of suffering, and critics ask why a good and all-powerful creator would create beings who could misuse freedom. "
          "Replies appeal to the value of freedom and to God's respect for it. The tension between human freedom and divine foreknowledge and grace remains a debated problem."),
        H("Aquinas: faith and reason"),
        T("Aquinas, working with the recovered works of Aristotle, defended the view that reason and faith are **complementary**, from the one source of truth. "
          "Some truths (that God exists, that the soul is rational) can be reached by reason: this is **natural theology**. Others (the Trinity, the Incarnation) are known only by revelation. "
          "Reason cannot contradict revealed truth, because truth cannot oppose truth. In this sense reason serves theology; in the Board's wording the relation is hierarchical, not one of mutual exclusion or of independence."),
        H("The Five Ways"),
        T("In the *Summa Theologiae* Aquinas gives five short arguments from features of the world to a first cause that people call God. They are called the **Five Ways** (*quinque viae*). The first three are arguments from causation and dependence; the fourth from degrees; the fifth from order."),
        KEY("Aquinas' five arguments", "Short statement of each; the core move is that an explanation must end somewhere.", cards=[
            ["1. Motion", "Things in the world are moved or changed. Whatever is moved is moved by another. This chain cannot go back for ever, so there must be a first unmoved mover, which we call God."],
            ["2. Efficient cause", "Things are caused by earlier causes. Nothing can cause itself, and the chain cannot be infinite, so there is a first uncaused cause."],
            ["3. Contingency", "Things can exist or not exist (they come and go). If everything were contingent, at some time nothing would have existed, and then nothing would exist now. So there must be a necessary being, whose existence is not dependent."],
            ["4. Degrees of perfection", "We compare things as more or less good, true or noble. This implies a maximum, the source of such qualities in all things, which is God."],
            ["5. Design (teleology)", "Things without intelligence, such as natural bodies, act regularly for ends. This needs a directing intelligence, which is God."],
        ]),
        EX("Worked example 1: lay out the first way", intro="Set out Aquinas' argument from motion step by step, then identify the key assumption.", steps=[
            S("Premise 1", text="Some things in the world are in motion (change). This is evident to the senses."),
            S("Premise 2", text="Whatever is moved is moved by something else, because nothing can move itself from potentiality to actuality at the same time and in the same respect (Aristotelian principle)."),
            S("Premise 3", text="A chain of movers, each moved by another, cannot go back to infinity, or there would be no first mover and so no motion now."),
            S("Conclusion", text="There is a first unmoved mover, and this is what people call God."),
            S("Key assumption", text="An infinite regress of movers is impossible. Aquinas means a regress that is *simultaneous and essentially ordered* (like a hand moving a stick that moves a stone), not a mere series back in time. Many critics doubt that the premise has been shown."),
        ]),
        H("Evaluating the Five Ways"),
        KEY("Objections and replies", "Give objections and replies, and avoid declaring a religious winner.", cards=[
            ["Infinite regress", "Objection: why can there not be an infinite series of causes? Reply: Aquinas needs essentially ordered series, where each cause depends on the one above now; without a first, nothing at all would operate."],
            ["Hume and Kant", "Objection: we cannot extend the notion of cause beyond the experience of the universe (Hume); the cosmological arguments depend on the ontological argument (Kant). Reply: defenders say the argument is metaphysical and does not rely on a purely empirical use of cause."],
            ["Modern physics", "Objection: modern physics changes our ideas of motion, causation and the beginning of the universe; the argument is not about the Big Bang in any case. Reply: Aquinas is not arguing about a first event in time but about continuing dependence."],
            ["Design and evolution", "Objection: Darwinian natural selection explains apparent design without a designer. Reply: the Fifth Way concerns the regularity of laws, which evolution presupposes. The debate continues."],
            ["The gap to God", "Objection: even if there is a first cause, why is it the one God of Christian belief, all-knowing and good? Reply: Aquinas adds further arguments for the divine attributes."],
        ]),
        EX("Worked example 2: model essay plan", intro="'The Five Ways prove the existence of God.' Discuss.", steps=[
            S("Introduction", text="State what Aquinas sets out to do (natural theology from the world to a first cause) and what 'prove' means: a deductive argument with premises we must accept."),
            S("For", text="The arguments rest on an old and powerful principle of sufficient explanation; many philosophers still consider cosmological arguments serious."),
            S("Against", text="Infinite regress may be possible; Hume on causation; Kant on limits of reason; evolution for the design argument; the gap between 'first cause' and God."),
            S("Evaluation", text="The arguments show that a certain view is coherent and reasonable for believers; most philosophers think they do not give a demonstration that compels all."),
            S("Conclusion", text="They are serious arguments but not a conclusive proof; their force depends on premises on which philosophers disagree."),
        ]),
        TIP("Exam link: Paper 1 tests the relation of faith and reason in Aquinas and other facts of the medieval topic, and Paper 2 essays may ask you to state and evaluate the Five Ways or Augustine on evil. In the 2023 report Medieval philosophy was left out of Paper 2, but you must still prepare."),
        MISTAKE("Saying that for Aquinas faith and reason contradict each other", "For Aquinas they cannot contradict: truth does not oppose truth. In the Board's wording they are hierarchically dependent."),
        MISTAKE("Taking the first way to be about the beginning of time", "It is about dependence now: what keeps things in motion at this moment. The first cause is a sustaining cause, not only a starter."),
        MISTAKE("Saying that Augustine denies that evil exists at all", "He says evil is real as a privation (a lack of good in a good thing), not as a created substance."),
        QUIZ("For Aquinas, faith and reason are",
             ["mutually exclusive", "hierarchically dependent, with reason serving theology", "independent of each other", "the same thing"], 1,
             "In Aquinas reason serves theology while remaining a real source of truth.",
             feedback=["He denies that they contradict.", "", "They are related, not independent.", "They are distinct sources of truths."]),
        QUIZ("Augustine explains evil as",
             ["a created substance opposed to God", "a privation, a lack or corruption of good", "an illusion with no effects", "an equal power to good"], 1,
             "Evil is not a thing but a lack of good, such as blindness is a lack of sight.",
             feedback=["That would make evil a second creation.", "", "He takes it to be real in its effects.", "That is a dualist view which he rejects."]),
        PQ("State two of Aquinas' Five Ways and one objection to each.",
           "Model answer: First way: things in motion are moved by another; the series cannot be infinite; so there is an unmoved mover. Objection: why can the series not be infinite? "
           "Third way: contingent things need a necessary being; if all things were contingent nothing would exist now. Objection: this may commit the fallacy of composition (what is true of each thing is not necessarily true of everything)."),
        PQ("Explain Augustine's account of the origin of evil.",
           "Model answer: God, the supreme good, made all things good. Evil is not a substance but a privation of good. Moral evil results from the will turning from higher to lower goods; free will is a real good, but it can be misused. "
           "Objection: this does not show why a good, all-powerful God allows the misuse. Reply: the value of freedom; the problem is still debated."),
        PQ("Compare how Augustine and Aquinas relate faith and reason.",
           "Model plan: Augustine: believe in order to understand, faith first, with Platonic ideas; reason clarifies faith. Aquinas: reason can reach some truths about God independently, revelation adds others, and the two cannot contradict; reason serves theology. "
           "Similarity: harmony, not conflict. Difference: Aquinas gives reason a more independent role and uses Aristotle. Evaluate: critics ask whether faith can be truly open to reason."),
        SUM("Medieval philosophy asks how faith and reason are related; do not argue as a preacher, argue as a philosopher.",
            "Augustine: faith seeking understanding; evil is privation of good; evil comes from misused free will; time is a stretch of the mind.",
            "Aquinas: reason and faith are harmonious and hierarchical; reason serves theology; natural theology and revelation.",
            "The Five Ways: motion, efficient cause, contingency, degrees of perfection, design.",
            "Standard objections: infinite regress, Hume and Kant, evolution, the gap between first cause and God."),
    ],
))

# ---------------------------------------------------------------------------
# M3 / Rationalism
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M3, topic="Rationalism",
    title="Rationalism: Descartes, Spinoza and Leibniz",
    slug="psl1-rationalism",
    minutes=26,
    summary="The rationalist claim that reason is the main source of knowledge: Descartes' doubt, cogito, dualism and proofs, Spinoza's one substance, Leibniz's monads and sufficient reason, with the standard objections.",
    objectives=[
        "Define rationalism and innate ideas, and contrast them with empiricism",
        "Explain Descartes' method, the cogito, the criterion of clear and distinct ideas and mind-body dualism",
        "Explain Spinoza's monism and Leibniz's monads and the principle of sufficient reason",
        "Evaluate rationalism through the Cartesian circle, the interaction problem and the empiricist reply",
    ],
    key_concepts=["Rationalism", "Innate ideas", "Cogito", "Dualism", "Substance", "Monad", "Principle of sufficient reason"],
    blocks=[
        H("Introduction"),
        T("The seventeenth century saw a scientific revolution: Galileo, Kepler, Newton. Mathematics seemed to give certain knowledge of nature. A group of philosophers, mostly on the European continent, asked whether all knowledge could be as certain as geometry. "
          "They concluded that **reason**, not the senses, is the main source of knowledge. They are the **rationalists**: Descartes (French), Spinoza (Dutch) and Leibniz (German)."),
        D("The view that reason, working independently of sense experience, is the main or only source of certain knowledge about reality. Rationalists usually admit **innate ideas** (ideas present in the mind from birth or by its nature, not derived from experience) "
          "and take mathematics as the model of knowledge. **Empiricism** (next lesson) holds that all knowledge comes from experience.", title="Rationalism"),
        H("Descartes (1596–1650)"),
        KEY("Descartes' route", "His Meditations on First Philosophy (1641) follow this order.", cards=[
            ["Methodic doubt", "Doubt the senses (they deceive), doubt that I am awake (dreaming), doubt even mathematics (a powerful deceiver, the evil demon)."],
            ["The cogito", "Even if deceived, I must exist to be deceived. The report's key says Meditation 2 reaches 'I am, I exist' as the first indubitable truth; 'I think, therefore I am' is the famous formulation from his other writings. I am a **thinking thing** (a mind)."],
            ["Clear and distinct ideas", "What I perceive as clearly and distinctly as the cogito is true. This becomes the criterion of truth."],
            ["God and the external world", "From the idea of a perfect being in my mind he argues that God exists, and that a good God would not deceive me when I use reason carefully. So I can trust my clear and distinct perceptions, and the existence of the material world is established."],
            ["Dualism", "Mind (thinking, unextended) and body (extended, not thinking) are two distinct substances."],
        ]),
        EX("Worked example 1: following the doubt", intro="Show how Descartes' doubt reaches a first certainty, step by step.", steps=[
            S("Doubt the senses", text="The senses sometimes deceive (a distant tower looks round). So I cannot fully trust them."),
            S("Doubt waking life", text="Dreams can feel real. I cannot be sure I am not dreaming now."),
            S("Doubt reason itself", text="Suppose a powerful deceiver makes me err even about simple sums."),
            S("What survives", text="Whatever else is false, I who am deceived must exist. Even doubting is thinking, and thinking needs a thinker."),
            S("Result", text="'I am, I exist' is certain every time I think it. Knowledge now has a foundation."),
        ]),
        T("**Evaluation of Descartes.** (1) The **Cartesian circle**: he proves God by clear and distinct ideas, and proves clear and distinct ideas are reliable by God. Reply: the cogito and the simplest truths are certain at the moment of thinking, and God is needed only for memory of earlier proofs; critics doubt this. "
          "(2) **Interaction problem**: if mind and body are completely different, how can the mind move the body or the body cause sensations? Princess Elisabeth of Bohemia pressed this question. Descartes pointed to the pineal gland, which few accept. "
          "(3) Is the 'I' proved, or only thinking? Later thinkers ask whether the cogito shows a substance or only that there are thoughts."),
        H("Spinoza (1632–1677)"),
        T("Spinoza wrote the *Ethics* in a **geometrical** form (definitions, axioms, propositions, proofs). His central claim is **monism**: there is only **one substance**, which he calls **God or Nature** (*Deus sive Natura*). "
          "Everything else is a **mode**, a way that substance exists. Substance has infinite attributes, of which we know two: **thought** and **extension**. "
          "Mind and body are not two substances but two aspects of one reality, which removes the interaction problem. Everything follows from the nature of substance with necessity, so Spinoza is a **determinist**, and freedom is understanding that necessity. "
          "His identification of God and Nature was condemned by many contemporaries as atheism, while others call it pantheism; textbooks differ, so check yours."),
        H("Leibniz (1646–1716)"),
        KEY("Leibniz in brief", "Three ideas to know.", cards=[
            ["Monads", "The world is made of countless simple, immaterial, mind-like substances called **monads**, each reflecting the whole universe from its own point of view. Bodies are appearances of monads."],
            ["Principle of sufficient reason", "Nothing is without a reason why it is so and not otherwise. This leads him to argue for a necessary being, God, as the reason for the world."],
            ["Truths of reason and of fact", "Truths of reason (mathematics, logic) are necessary, with contradiction as their test. Truths of fact (this book is on the table) are contingent and rest on sufficient reason. He also defended **pre-established harmony**: mind and body run in agreement because God set them so, not by causal interaction."],
        ]),
        T("Leibniz also argued that this is the best of all possible worlds, a view attacked later by Voltaire's satire. His claim that there are no two identical things (identity of indiscernibles) is a famous topic in metaphysics."),
        H("Comparing the three and the empiricist reply"),
        KEY("Three rationalists compared", "A table of differences helps in essays.", cards=[
            ["Descartes", "Two substances (mind and body) and God; method of doubt; innate ideas."],
            ["Spinoza", "One substance (God or Nature); everything necessary; mind and body as attributes."],
            ["Leibniz", "Infinitely many monads; pre-established harmony; sufficient reason; contingent truths of fact."],
        ]),
        T("The **empiricist reply** (Locke, Hume): there are no innate ideas; the mind begins like a blank sheet; mathematics gives certainty only because it states relations between ideas and tells us nothing about the world; "
          "pure reason cannot prove the existence of God or of substance. Rationalists reply that experience alone cannot explain necessary truths or the structure of our concepts. Kant, in the last lesson of this module, tries to resolve this dispute."),
        EX("Worked example 2: model essay plan", intro="'Descartes' cogito gives a secure foundation for knowledge.' Discuss.", steps=[
            S("Introduction", text="Explain the doubt and the cogito (I am, I exist; I am a thinking thing)."),
            S("For", text="It resists even the evil demon; it is immediate and cannot be doubted while I think it; it is a model of first-person certainty."),
            S("Against", text="It proves only that thinking exists, not a lasting self (Lichtenberg, Hume); the step to a substance is not obvious; it depends on concepts (thought, existence) which were not doubted; the later route to God and the world is circular."),
            S("Evaluation", text="The cogito is a fair starting point of certainty, but it gives much less than Descartes builds on it."),
            S("Conclusion", text="A secure but very narrow foundation."),
        ]),
        TIP("Exam link: Descartes is Paper 1 and Paper 2 material (the Board's report shows a question on the first indubitable truth in the Meditations, and in 2023 Modern Philosophy was tested twice in Paper 2). Name the work and the exact step you describe."),
        MISTAKE("Quoting 'I think, therefore I am' as the first step of the Meditations", "In the Meditations the first indubitable truth is 'I am, I exist'. The phrase 'I think, therefore I am' comes from his other works. Cite the correct work."),
        MISTAKE("Saying Descartes believed only the mind exists", "He is a dualist: mind and body are both real, distinct substances."),
        MISTAKE("Saying Spinoza and Descartes both hold two substances", "Spinoza is a monist: one substance, many modes. Mind and body are attributes of the one substance."),
        QUIZ("According to the Board's key, the first indubitable truth discovered by Descartes' methodic doubt in the Meditations is",
             ["I am, I exist", "Material things exist", "God exists", "The senses are reliable"], 0,
             "Meditation 2 reaches the certainty that I am, I exist, whenever I think it.",
             feedback=["", "The world is only established later.", "God's existence is argued after the cogito.", "The senses are the first target of the doubt."]),
        QUIZ("Spinoza's position on substance is",
             ["there are two substances", "there is one substance, God or Nature", "there are infinitely many monads", "there is no substance"], 1,
             "Spinoza is a monist: one substance with infinite attributes.",
             feedback=["That is Descartes' dualism.", "", "That is Leibniz.", "Spinoza affirms one substance."]),
        PQ("Explain Descartes' dualism and one problem it faces.",
           "Model answer: mind is a thinking, unextended substance and body an extended, non-thinking one; they are really distinct. Problem: how can two such different substances interact (mind moves body, body causes sensation)? "
           "Elisabeth pressed this; the pineal gland is not widely accepted. Spinoza and Leibniz are two responses."),
        PQ("State Leibniz's principle of sufficient reason and use it to explain why he believed in God.",
           "Model answer: nothing exists or happens without a reason. The universe is contingent, so the reason for it cannot be found within the series of contingent things; it must lie in a necessary being, which is God. "
           "Objection: why must everything have a reason? The principle is assumed. Reply: it is a basic condition of explanation."),
        PQ("Compare the rationalist and empiricist views of knowledge, and say what a rationalist would reply to the empiricist.",
           "Model plan: rationalism: reason is the main source; innate ideas; mathematics as model. Empiricism: all knowledge from experience; no innate ideas. Rationalist reply: experience cannot explain necessary truths (2 + 2 = 4, the principle of non-contradiction) or the concepts we use to interpret experience. "
           "Evaluation: Kant's later position tries to join the two."),
        SUM("Rationalists hold that reason, not sense experience, is the main source of certain knowledge, and they admit innate ideas.",
            "Descartes: methodic doubt, cogito, clear and distinct ideas, God, mind-body dualism; problems: the Cartesian circle and interaction.",
            "Spinoza: one substance (God or Nature) with infinite attributes, thought and extension; everything necessary.",
            "Leibniz: monads, sufficient reason, pre-established harmony, truths of reason and truths of fact.",
            "The empiricist reply: no innate ideas, and reason alone cannot reach substantive truths about the world."),
    ],
))

# ---------------------------------------------------------------------------
# M3 / British empiricism
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M3, topic="British empiricism",
    title="British empiricism: Locke, Berkeley and Hume",
    slug="psl1-british-empiricism",
    minutes=26,
    summary="The empiricist claim that experience is the source of knowledge: Locke on ideas and qualities, Berkeley's idealism, Hume's fork, causation, induction and the self, with objections.",
    objectives=[
        "Define empiricism and state Locke's account of ideas, sensation and reflection and of primary and secondary qualities",
        "Explain Berkeley's argument that to be is to be perceived and the role of God",
        "Explain Hume's impressions and ideas, his fork, his analysis of causation and his view of the self",
        "Evaluate the empiricist programme and its sceptical consequences",
    ],
    key_concepts=["Empiricism", "Tabula rasa", "Primary and secondary qualities", "Idealism", "Impression", "Hume's fork", "Causation"],
    blocks=[
        H("Introduction"),
        T("How do you know the mango in your hand is sweet? You taste it. How do you know the sun will rise tomorrow? Because it always has. British philosophers of the seventeenth and eighteenth centuries, John Locke, George Berkeley and David Hume, took such ordinary knowledge seriously. "
          "They held that **all our ideas and all our knowledge of the world come from experience**. This view is **empiricism**. It follows its own logic to some surprising and sceptical conclusions."),
        D("The view that sense experience (with, for Locke, the mind's reflection on its own operations) is the source of all ideas and of knowledge of the world. "
          "Empiricists reject **innate ideas**: the mind begins as a blank sheet (*tabula rasa*, Locke's picture) and is written on by experience.", title="Empiricism"),
        H("John Locke (1632–1704)"),
        T("Locke's *Essay Concerning Human Understanding* (1689/90) asks what the human mind can know and how. He says all the mind's materials, which he calls **ideas**, come from two sources of experience. "
          "The Board's key (Paper 1) states them: **sensation** (external senses give ideas of colour, sound, hardness) and **reflection** (the mind's notice of its own workings, such as thinking, doubting, willing)."),
        KEY("Locke's main distinctions", "Learn each with an example.", cards=[
            ["Simple and complex ideas", "Simple ideas (a colour, a taste) cannot be broken down. The mind combines them into complex ideas (a mango, a nation, the idea of justice)."],
            ["Primary and secondary qualities", "Primary qualities (solidity, extension, shape, motion, number) are really in objects and resemble our ideas. Secondary qualities (colour, taste, sound, smell) are powers in objects to produce sensations in us; they do not resemble the objects."],
            ["Substance", "We assume that qualities belong to something, a substance, but of the substance itself we have only a vague idea of an unknown support for qualities."],
            ["Representative realism", "Our ideas represent external objects, which cause them. We do not perceive objects directly, only ideas."],
        ]),
        T("**Objections to Locke.** If we perceive only ideas, how can we know the objects exist and resemble them (the veil of perception)? Berkeley also argues that primary qualities cannot be separated from secondary ones: no one can imagine an extended thing with no colour. "
          "Critics say the notion of substance is empty. Defenders say Locke gives a practical, science-friendly account in which the senses give reliable knowledge of the world, with limits."),
        H("George Berkeley (1685–1753)"),
        T("Berkeley, an Irish bishop, took empiricism further. If we know only ideas, he argues, there is no good reason to believe in a matter that is *beyond* ideas. "
          "His thesis is **immaterialism** (also called subjective idealism): **to be is to be perceived** (*esse est percipi*) for the things we know, and to be is also to perceive for minds. Only minds and their ideas exist."),
        KEY("Berkeley's arguments", "Know the steps and the reply to the obvious objection.", cards=[
            ["Against primary and secondary qualities", "Heat and colour depend on the perceiver (warm hand, cold hand); the same applies to shape and size, which also vary with the viewpoint. So there is no sound way to treat some qualities as mind-independent."],
            ["Against matter", "'Matter' as an unperceived, qualityless substance cannot be perceived or even clearly conceived. It does no work; it is an empty idea."],
            ["God and continuity", "Objection: when no human sees the tree, does it vanish? Reply: God, an infinite mind, always perceives everything, so objects have continuous existence. Critics say this is an ad hoc use of God."],
        ]),
        T("A common mistake is to say that Berkeley denies the tree exists: he says it exists as a collection of ideas ordered by God and by regular laws, so everyday life and science remain as they are. "
          "Critics say the view is hard to believe, that it makes the world dependent on perception, and that it cannot explain the difference between imagining and perceiving except by the vividness and order of ideas."),
        H("David Hume (1711–1776)"),
        T("Hume, a Scot, pushed empiricism to its limits in his *Treatise of Human Nature* and *Enquiry concerning Human Understanding*. He divides the contents of the mind into **impressions** (vivid sensations and feelings) and **ideas** (fainter copies of impressions). "
          "His **copy principle**: every simple idea is copied from an impression. An idea with no impression behind it is empty."),
        KEY("Hume's fork", "Hume divides all objects of reason into two kinds.", cards=[
            ["Relations of ideas", "Mathematics and logic. Certain, known by reasoning, true by the meaning of terms. Denying them is a contradiction. They tell us nothing about the world."],
            ["Matters of fact", "Claims about the world (the sun will rise). Based on experience. Their opposite is always conceivable without contradiction, so they are never certain."],
            ["The conclusion", "Any book that contains neither kind of reasoning is to be thrown on the fire, Hume says: it contains only sophistry and illusion. (Critics ask whether the fork itself passes its own test.)"],
        ]),
        T("**Causation.** We think that when a billiard ball strikes another, the first *makes* the second move. Hume asks what impression we have of this 'necessary connection'. We observe only that events of one kind are regularly followed by events of the other (**constant conjunction**) and that the mind, by **habit**, expects the second after the first. "
          "So causation is not something seen in the world but an expectation produced by repetition. This links to the **problem of induction**: no argument based on reason alone shows that the future will resemble the past. We cannot prove the sun will rise tomorrow."),
        T("**The self.** Looking inward, Hume finds only a stream of perceptions (a heat, a thought, a pain) and no impression of a permanent self. The self is a **bundle of perceptions** linked by memory and resemblance. "
          "Critics ask who or what is doing the bundling; Hume himself said he found this difficulty troubling."),
        EX("Worked example 1: Hume on the sunrise", intro="Why can't we prove that the sun will rise tomorrow, according to Hume?", steps=[
            S("The claim is a matter of fact", text="It is about the world, not about the meaning of words. Its denial ('the sun will not rise') is not a contradiction."),
            S("Experience is the only ground", text="We believe it because the sun has always risen. This assumes the future resembles the past."),
            S("The circle", text="To prove that the future resembles the past, we would appeal to past experience, which assumes the very thing to be proved."),
            S("Result", text="No rational proof. Our belief is produced by habit, not by demonstration. In practice we cannot help believing it."),
        ]),
        EX("Worked example 2: model essay plan", intro="'Empiricism leads to scepticism.' Discuss.", steps=[
            S("Introduction", text="Define empiricism and scepticism, and state the thesis: it leads to limited knowledge, more by Hume than by Locke."),
            S("Locke", text="Knowledge limited to ideas; substance unknown; veil of perception raises doubts about the external world."),
            S("Berkeley", text="Escapes scepticism about the world by idealism, but at the cost of denying matter."),
            S("Hume", text="No proof of causation, induction, the self or an independent world; belief rests on habit."),
            S("Evaluation", text="Hume's scepticism is about proof, not about practice; empiricists keep science as probable knowledge. Kant answers by claiming the mind contributes structure to experience."),
            S("Conclusion", text="Yes, in Hume, but the scepticism is mainly about what reason can prove, not about daily life."),
        ]),
        TIP("Exam link: Locke's two sources of experience are a Paper 1 fact (the Board's report shows a question on this), and the empiricists feature in Paper 2 essays on Modern Philosophy. Prepare comparisons: Locke against Descartes, Hume against Kant."),
        MISTAKE("Saying that Locke thinks the mind knows nothing before birth, or that he rejects reason", "Locke rejects innate ideas, not reason. Reflection is the mind's own activity in dealing with ideas from experience."),
        MISTAKE("Saying Berkeley denies that things exist", "He denies that matter exists apart from perception. Tables, trees and stones exist as ideas ordered by God."),
        MISTAKE("Saying Hume proves that causation does not exist", "He argues that our idea of necessary connection comes from habit, and that reason cannot prove it. He does not recommend dropping causal belief."),
        QUIZ("According to Locke, the forms of experience (sources of ideas) are",
             ["demonstration and intuition", "primary and secondary qualities", "sensation and intuition", "sensation and reflection"], 3,
             "Ideas come from sensation (outer sense) and reflection (the mind's observation of its own operations).",
             feedback=["Demonstration and intuition concern ways of knowing, not sources of ideas.", "Primary and secondary are kinds of quality.", "Intuition is not one of Locke's two sources.", ""]),
        QUIZ("Berkeley's slogan 'to be is to be perceived' means for the objects we know that",
             ["objects exist only as ideas perceived by minds", "matter is the only reality", "only the senses of animals count", "perception is always false"], 0,
             "He rejects matter apart from perception; objects are collections of ideas.",
             feedback=["", "He rejects matter as a mind-independent substance.", "The point is not about animals.", "He treats perception as reliable."]),
        PQ("Explain Hume's analysis of causation.",
           "Model answer: we see one event follow another (constant conjunction) but have no impression of a necessary connection; the sense of necessity arises from habit, the mind's expectation after repeated experience. "
           "So causal beliefs are not rationally proved. Evaluation: this matches science's reliance on regularities, but critics ask whether it explains why regularities hold."),
        PQ("Distinguish primary from secondary qualities in Locke and give one criticism.",
           "Model answer: primary qualities (shape, size, solidity, motion, number) are in objects and resemble our ideas; secondary (colour, taste, sound) are powers to produce sensations in us. "
           "Criticism (Berkeley): primary qualities depend on the perceiver as much as secondary ones, as the size and shape of a coin vary with the viewpoint, so the distinction cannot be sustained."),
        PQ("Compare Locke, Berkeley and Hume on how far experience can give us knowledge of the external world.",
           "Model plan: Locke: ideas represent real objects caused by them; knowledge probable. Berkeley: no matter; objects are ideas held in God's mind. Hume: reason cannot prove the external world, causation, or self; belief is natural habit. "
           "Show a progression in scepticism. Evaluate: each solves a problem of the previous one and creates another."),
        SUM("Empiricism: all ideas and knowledge come from experience; no innate ideas.",
            "Locke: ideas from sensation and reflection; simple and complex ideas; primary and secondary qualities; representative realism.",
            "Berkeley: to be is to be perceived; matter is rejected; God sustains the order of ideas.",
            "Hume: impressions and ideas; the fork of relations of ideas and matters of fact; causation as habit; induction; self as a bundle.",
            "Evaluation: empiricism gives a modest and science-friendly view but leads, especially with Hume, to scepticism about what reason can prove."),
    ],
))

# ---------------------------------------------------------------------------
# M3 / The social contract theorists
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M3, topic="The social contract theorists",
    title="Hobbes, Locke and Rousseau on the state and the social contract",
    slug="psl1-social-contract",
    minutes=24,
    summary="Why the state exists and what it may demand: Hobbes' state of nature and absolute sovereign, Locke's natural rights and limited government, Rousseau's general will, and the main criticisms of contract theory.",
    objectives=[
        "Define the state of nature and the social contract and explain why the idea was used",
        "Explain Hobbes, Locke and Rousseau on human nature, the contract and the limits of government",
        "Compare the three theories on rights, sovereignty and the right to resist",
        "Evaluate social contract theory with objections and replies",
    ],
    key_concepts=["State of nature", "Social contract", "Sovereign", "Natural rights", "Consent", "General will"],
    blocks=[
        H("Introduction"),
        T("Why should a citizen of Yaounde obey the law, pay taxes and accept the authority of the state? A group of seventeenth- and eighteenth-century thinkers answered with a thought experiment: "
          "imagine people **without any government**, and ask why they would agree to create one. The agreement they would make is the **social contract**. "
          "The idea explains the origin of political authority and also sets limits on it: a government that breaks the terms of the contract loses its claim to obedience. "
          "The three main contract theorists in your syllabus are **Hobbes**, **Locke** and **Rousseau**."),
        D("A thought experiment: the condition of human beings before or without government, law and political authority. Each thinker describes it differently, and the description determines his conclusion about what government is for.", title="State of nature"),
        D("The (real or hypothetical) agreement by which individuals give up some freedom or rights in return for the order and protection of a political community. "
          "Most scholars treat it as a hypothetical argument about **legitimacy**, not as a historical event.", title="Social contract"),
        H("Thomas Hobbes (1588–1679)"),
        T("Hobbes wrote *Leviathan* (1651) in the shadow of the English Civil War. He holds that people are roughly equal in strength and mind, driven by self-preservation and desire. "
          "In the state of nature there is no common power to keep them in awe, so there is **a war of every person against every person**: fear, competition for scarce goods and distrust make life insecure and no industry or trade can flourish. "
          "There are no moral rules of justice before the law, because there is no one to enforce agreements. Reason shows a way out: seek peace by agreeing to give up the right to all things."),
        KEY("Hobbes in brief", "Four steps.", cards=[
            ["State of nature", "No power to keep order: constant fear and conflict, but not because people are evil. It is the situation that is the problem."],
            ["The contract", "Everyone agrees to give up their natural right to govern themselves to one **sovereign**, a person or an assembly, in return for security."],
            ["The sovereign", "Absolute and undivided; the sovereign is not party to the contract and cannot break it, and subjects may not rebel, except to save their lives (the right of self-preservation remains)."],
            ["Why obey", "Because any order, even harsh, is better than the war of all. Obedience is rational self-interest."],
        ]),
        T("Criticisms: Hobbes gives too bleak a picture of human nature; an absolute sovereign may himself be the greatest danger to the people (Locke's point); and the argument shows why we need *some* government but not why it must be *absolute*."),
        H("John Locke (1632–1704)"),
        T("In his *Two Treatises of Government* (1689) Locke describes a state of nature governed by a **law of nature** known by reason: no one may harm another in life, health, liberty or possessions. People have **natural rights** to **life, liberty and property** before government. "
          "The state of nature is therefore not a war, but it is **inconvenient**: there is no impartial judge, no settled law, and no power to punish reliably, so each person is judge in his own case and quarrels arise. "
          "People consent to form a government to protect the rights they already have."),
        KEY("Locke in brief", "Compare each point with Hobbes.", cards=[
            ["State of nature", "Peaceful but insecure; people have natural rights and duties."],
            ["The contract", "Based on **consent**: people agree to create a community and a government with the specific task of protecting life, liberty and property."],
            ["Limited government", "Government is a **trust**. Power is divided (legislature above the executive). It must rule by settled laws and may not take property arbitrarily or tax without consent."],
            ["Resistance", "If government breaks the trust and becomes tyrannical, the people have the **right to resist** and to set up a new government."],
        ]),
        T("Criticisms: Locke's idea of consent is weak (what of those who never agreed? He speaks of tacit consent through living in a country); his ideas of property raised problems; and it was applied selectively: in his own time many people were excluded from the political community. "
          "Defenders note that his theory was later used to support constitutional government, rights and the justification of revolution."),
        H("Jean-Jacques Rousseau (1712–1778)"),
        T("Rousseau wrote the *Social Contract* (1762) after criticising civilised society in earlier works. For him humans in the state of nature are free and peaceful, moved by self-love and pity, and are corrupted by property, vanity and inequality in society. "
          "The problem is to find a form of association in which each person unites with all and yet obeys only himself and remains free. The solution is the contract in which each person gives themself entirely to the community under the **general will**."),
        KEY("Rousseau in brief", "His key concept is hard, so read it carefully.", cards=[
            ["General will", "What the community wills for the common good, as distinct from the **will of all**, the sum of private interests. Laws express the general will."],
            ["Sovereignty", "Sovereignty belongs to the people and cannot be handed over or divided. Government is only the agent of the sovereign people."],
            ["Freedom", "True freedom is obeying a law that we have given ourselves. He holds that a citizen who refuses the general will may be compelled to obey it, and that this compels him to be free: a paradox that has provoked many criticisms."],
            ["Politics", "Best in small states with direct participation; he is sceptical of representation."],
        ]),
        T("Criticisms: the general will can be used to silence minorities and justify tyranny in the name of the people; it is unclear how the general will is discovered; and direct democracy cannot work in large states. "
          "Defenders reply that Rousseau stresses equality, participation and the common good, and that his theory is the source of modern ideas of popular sovereignty."),
        IMG("alpsl1-contract-table.svg", alt="A comparison table with three columns, Hobbes, Locke and Rousseau, and rows for the state of nature, what is surrendered, the form of government and the right to resist.",
            caption="Figure 1. Hobbes, Locke and Rousseau compared."),
        EX("Worked example 1: apply the three theories", intro="A government in a country passes a law that takes land from villagers with no compensation. How would each theorist judge it?", steps=[
            S("Hobbes", text="Order must be kept; the sovereign is the judge, and subjects have no right to resist, except if their lives are at stake. The law would be unjust in the sense of unwise, but not illegitimate. Critics say this gives too much power."),
            S("Locke", text="Property is a natural right. Government is a trust and may not take property without consent. The law breaks the trust; resistance may be justified if the abuse is serious and repeated."),
            S("Rousseau", text="The law must express the general will, made by the people as sovereign with attention to the common good. A law that benefits a faction is not an expression of the general will. Ask who made the law and for whom."),
            S("Evaluation", text="The three give different tests: security (Hobbes), rights and consent (Locke), participation and the common good (Rousseau)."),
        ]),
        EX("Worked example 2: model essay plan", intro="'The social contract is a myth and so cannot justify the state.' Discuss.", steps=[
            S("Introduction", text="Define the contract and its use as a thought experiment about legitimacy."),
            S("For the claim", text="No such agreement ever happened (Hume's objection); most people never consented; those born into a state had no choice."),
            S("Against the claim", text="The contract is a test: would rational people agree to these institutions? Hypothetical consent can still give reasons. Contract ideas supported rights and constitutions."),
            S("Evaluation", text="The theory is weak as history, but strong as a way of judging whether government treats people as free and equal."),
            S("Conclusion", text="The contract need not be real to be useful, but its force depends on how consent is understood."),
        ]),
        TIP("Exam link: contract theory appears in Paper 1 and in Paper 2 essays (in the 2023 report Modern Philosophy was tested twice). It also links with the Upper Sixth topics on justice, the state and human rights. Present each theorist fairly and compare them on the same headings."),
        MISTAKE("Saying that for Hobbes people are evil", "He argues that the *situation* without government produces conflict, because everyone has equal reason to fear and to strike first. It is not a claim that humans are wicked by nature."),
        MISTAKE("Saying Locke supports an absolute ruler", "Locke defends limited, consent-based government and the right to resist tyranny. Absolute rule is Hobbes' view."),
        MISTAKE("Equating the general will with majority opinion", "Rousseau separates the general will (the common good) from the will of all (the sum of private interests). A majority can be wrong."),
        QUIZ("In Hobbes' state of nature, life is mainly characterised by",
             ["peaceful co-operation under natural law", "constant fear and conflict, because there is no common power", "perfect equality of property", "rule by a general will"], 1,
             "Without a common power, fear and competition lead to a war of all against all.",
             feedback=["That is closer to Locke's state of nature.", "", "Property and justice do not exist before the sovereign.", "That belongs to Rousseau's political society."]),
        QUIZ("Which thinker holds that people have the right to resist a government that breaks the trust placed in it?",
             ["Hobbes", "Locke", "Neither of them", "Hobbes and Locke equally"], 1,
             "Locke defends resistance to tyranny; Hobbes denies it except to save one's life.",
             feedback=["Hobbes defends an absolute sovereign.", "", "Locke does hold this.", "They disagree on this point."]),
        PQ("Compare Hobbes and Locke on the state of nature and the purpose of government.",
           "Model answer: Hobbes: no power, so a war of all against all; people give up their rights to an absolute sovereign for security. Locke: a state of nature governed by natural law and rights, insecure because there is no impartial judge; people consent to a limited government to protect life, liberty and property. "
           "The difference leads Hobbes to absolute power and Locke to limited government and a right of resistance."),
        PQ("Explain Rousseau's general will and one criticism of it.",
           "Model answer: the general will is what the community wills for the common good, as distinct from the will of all (the sum of private wishes). Laws express it, and obeying it is true freedom because citizens make the laws. "
           "Criticism: it can be used to override minority rights, and it is unclear how to discover it. Reply: it requires equal participation and concern for the common good."),
        PQ("'Consent is the only basis of legitimate government.' Evaluate, using the contract theorists.",
           "Model plan: Locke and Rousseau: government is legitimate only by consent of the governed; Hobbes: consent is a rational acceptance of the sovereign for security. For: respects persons as free and equal; limits tyranny. "
           "Against: few have given real consent; tacit consent is weak; legitimacy may also come from justice and protection of rights. Judgement: consent is important but difficult to define."),
        SUM("The state of nature and the social contract are thought experiments about why we should obey government.",
            "Hobbes: war of all against all, an absolute sovereign, order before liberty.",
            "Locke: natural rights to life, liberty and property, government by consent as a trust, right of resistance.",
            "Rousseau: sovereignty of the people, the general will, freedom as self-given law.",
            "Evaluation: weak as history, strong as a test of legitimacy; consent and minority rights are the main difficulties."),
    ],
))

# ---------------------------------------------------------------------------
# M3 / Kant's critical philosophy and ethics
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M3, topic="Kant's critical philosophy and ethics",
    title="Kant: the critical turn, phenomena and noumena, and the categorical imperative",
    slug="psl1-kant-critical-ethics",
    minutes=27,
    summary="Kant's reply to rationalists and empiricists (the mind shapes experience; phenomena and noumena), and his deontological ethics: good will, duty, the categorical imperative and its formulations, with objections.",
    objectives=[
        "Explain how Kant tries to reconcile rationalism and empiricism (synthetic a priori, categories, space and time)",
        "Distinguish phenomena from noumena and state the limits of knowledge",
        "Explain the good will, duty, hypothetical and categorical imperatives and the main formulations",
        "Apply the categorical imperative to cases and evaluate Kantian ethics",
    ],
    key_concepts=["Synthetic a priori", "Categories", "Phenomena and noumena", "Good will", "Duty", "Categorical imperative"],
    blocks=[
        H("Introduction"),
        T("Immanuel Kant (1724–1804) spent his whole life in Konigsberg in Prussia. He said that reading Hume woke him from a dogmatic sleep. "
          "Rationalists held that reason alone gives knowledge; empiricists that experience alone does. Hume's results seemed to destroy certain knowledge of causes. "
          "Kant's **Critique of Pure Reason** (1781, revised 1787) is his attempt at a way out: **critical philosophy**, which examines the powers and limits of reason itself. "
          "His ethics, in the *Groundwork of the Metaphysics of Morals* (1785), makes **duty** and **reason**, not consequences, the heart of morality."),
        H("Part 1: critical philosophy"),
        D("Kant uses two distinctions. A judgement is **analytic** if the predicate is contained in the subject ('all bachelors are unmarried'), and **synthetic** if it adds information ('this table is heavy'). "
          "It is **a priori** if known independently of experience, and **a posteriori** if it depends on experience. "
          "Empiricists accepted a priori analytic truths and a posteriori synthetic ones. Kant argues that there are also **synthetic a priori** judgements: informative and yet not derived from experience, such as the truths of mathematics ('7 + 5 = 12'), "
          "and the principle that every event has a cause.", title="Analytic, synthetic, a priori"),
        KEY("Kant's main moves", "Four ideas in his answer to the question 'How is synthetic a priori knowledge possible?'", cards=[
            ["Copernican revolution", "Instead of supposing that our knowledge must conform to objects, suppose that objects, as we experience them, must conform to the structure of our mind. The mind is an active shaper of experience."],
            ["Forms of intuition", "**Space and time** are not things in the world nor derived from experience; they are the mind's forms for receiving all sense experience. This makes geometry and arithmetic apply to all experience."],
            ["Categories", "The understanding has twelve concepts (categories), including **causality** and **substance**, which organise experience into knowledge. Without them, experience would be a jumble. This answers Hume: causation is not just habit; it is a condition of any experience of an ordered world."],
            ["Phenomena and noumena", "We know things as they **appear** to us (**phenomena**), shaped by our forms and categories. Things as they are **in themselves** (**noumena** or things in themselves) are unknowable by theoretical reason."],
        ]),
        T("Kant's famous summary, often reported, is that thoughts without content are empty and intuitions without concepts are blind: knowledge needs both **sensations** (the empiricist element) and **concepts** (the rationalist element). "
          "So Kant joins the two traditions. The limit is that **pure reason cannot know God, the soul or the world as a whole**, because these lie beyond possible experience; attempts to prove them lead to contradictions (the antinomies). "
          "He leaves room for belief on moral grounds."),
        T("**Evaluation.** Strengths: it explains how mathematics and science apply to the world; it answers Hume on causation; it respects both reason and experience. "
          "Objections: the noumenal realm seems unknowable yet Kant says it affects us (a possible contradiction); later geometry and physics (non-Euclidean geometry, relativity) challenged his claim that space and time are fixed forms; "
          "and some say the categories could be different for other minds or cultures."),
        H("Part 2: Kant's moral philosophy"),
        T("Kant asks what makes an action **morally good**. Not its consequences (luck can spoil a good plan), not talents like intelligence or wealth, which can be used badly. "
          "The only thing good without qualification is a **good will**: the will that acts from **duty**, that is, because the action is morally right."),
        D("A **good will** acts from respect for the moral law. Acting **from duty** is different from acting merely **in accordance with duty**. "
          "A shopkeeper who does not cheat customers because cheating would harm his reputation acts in accordance with duty; one who refuses to cheat because it is wrong acts from duty and shows moral worth.", title="Good will and duty"),
        D("A **hypothetical imperative** has the form 'If you want X, do Y' (study if you want to pass). Its force depends on a desire. A **categorical imperative** commands unconditionally, whatever you want: 'Do this because it is right.' Moral duties are categorical.", title="Imperatives"),
        KEY("Formulations of the categorical imperative", "These are three of Kant's formulations; textbooks may number them differently.", cards=[
            ["Universal law", "Act only on a maxim (a personal rule of action) that you could at the same time will to become a universal law for everyone."],
            ["Humanity as an end", "Treat humanity, in yourself and in others, always as an end and never merely as a means. Persons have dignity, not a price."],
            ["Autonomy and the kingdom of ends", "Act as if you were a lawmaking member of a community of rational beings, each giving the law to himself. Morality is **self-legislation** by reason, not obedience to outside authority."],
        ]),
        T("Duties are **perfect** (never to be broken, like not lying or not committing suicide) or **imperfect** (we must pursue them, but have latitude, like helping others or developing talents). "
          "A perfect duty fails the test by contradiction in conception (universal lying would destroy the practice of promising); an imperfect duty fails by a contradiction in the will (we could not will a world where no one helps anyone, because we would need help ourselves)."),
        EX("Worked example 1: the lying promise", intro="Mamadou needs money and is tempted to promise to repay a loan though he knows he cannot. Test the maxim by the universal law formula.", steps=[
            S("State the maxim", text="'When I need money, I will promise to repay while intending not to.'"),
            S("Universalise", text="Suppose everyone acted on this maxim."),
            S("Test", text="Promises would no longer be believed, so no one would lend on a promise. The maxim destroys the practice it depends on: a contradiction."),
            S("Conclusion", text="The maxim fails the test, so the action is forbidden. A second test: it also treats the lender merely as a means (humanity formula)."),
        ]),
        H("Evaluating Kantian ethics"),
        KEY("Objections and replies", "Use as pairs.", cards=[
            ["Rigidity", "Objection: Kant said that one may not lie even to a murderer asking where a friend is hiding (a famous example in a later essay, whose interpretation is debated). Reply: defenders say rules can be stated in more detailed forms, and that Kant's duty not to deceive is about one's own maxim; others accept the cost."],
            ["Conflict of duties", "Objection: what if two duties conflict (to keep a promise and to save a life)? Reply: Kant does not give a clear ranking; some Kantians use the humanity formula to weigh duties."],
            ["Consequences", "Objection: ignoring the outcomes seems absurd. Reply: Kant says outcomes cannot be the basis of moral worth, but he does not deny that they matter in deciding what duty requires."],
            ["Emotions", "Objection: acting from duty is cold; a friend who visits you from kindness seems better than one who comes from duty alone. Reply: Kant praises acting from duty where inclination is absent; compatible with kindness."],
            ["Strengths", "Equal respect for persons, universal rules, human dignity, rejects using people as mere tools, and basis for human rights."],
        ]),
        EX("Worked example 2: model essay plan", intro="'Morality is about duty, not consequences.' Discuss with reference to Kant.", steps=[
            S("Introduction", text="Define deontological and consequentialist theories; state Kant's view: moral worth lies in acting from duty."),
            S("For Kant", text="Consequences are partly beyond our control; respect for persons is protected from calculations that would sacrifice one for many; universal rules."),
            S("Against", text="Rigidity in the murderer case; conflict of duties; ignoring outcomes seems implausible. Utilitarians (later topic) say right action maximises welfare."),
            S("Evaluation", text="Many hold a mixed view: duties and rights set limits, and consequences matter within them."),
            S("Conclusion", text="Kant is right that morality includes duties that cannot be traded off for any good result, but wrong if he denies that consequences ever matter."),
        ]),
        TIP("Exam link: Kant is both Paper 1 and Paper 2 material (the section on Modern Philosophy) and connects to the Upper Sixth topics conscience and duty, utilitarianism and human rights. Put the epistemology and the ethics in separate paragraphs, and give an example when you apply the categorical imperative."),
        MISTAKE("Confusing 'a priori' with 'innate' or 'analytic'", "A priori means independent of experience; analytic means true by meaning. Kant's key claim is that some truths are both a priori and synthetic."),
        MISTAKE("Saying that Kant says we know nothing of the real world", "We know the world of appearances (phenomena) reliably and scientifically. The limit is the thing in itself, beyond experience."),
        MISTAKE("Treating the categorical imperative as a golden rule", "It is not 'do as you would be done by'. It tests whether your maxim can be willed as a universal law and whether it treats persons as ends."),
        QUIZ("A judgement that is informative and yet known independently of experience is, for Kant,",
             ["analytic a priori", "synthetic a posteriori", "synthetic a priori", "analytic a posteriori"], 2,
             "Kant's claim is that mathematics and the principle of causation are synthetic a priori.",
             feedback=["Analytic a priori truths are true by meaning, and add nothing new.", "Synthetic a posteriori judgements rest on experience.", "", "Analytic a posteriori is not a category that Kant uses."]),
        QUIZ("Which is a **categorical** imperative?",
             ["If you want to pass, study.", "Do not make promises you do not intend to keep, whatever you want.", "If you want to be rich, save money.", "Be polite so that people like you."], 1,
             "A categorical imperative commands unconditionally; the others depend on a desire.",
             feedback=["Hypothetical: depends on the wish to pass.", "", "Hypothetical: depends on the wish to be rich.", "Hypothetical: depends on the wish to be liked."]),
        PQ("Explain Kant's distinction between phenomena and noumena and say why it matters.",
           "Model answer: we know things as they appear to us, shaped by the forms of space and time and the categories (phenomena). Things as they are in themselves (noumena) are unknowable by theoretical reason. "
           "It matters because it explains how science can be certain about experience, while denying that pure reason can prove God, the soul or the world as a whole. Objection: Kant seems to say the thing in itself causes experience, though causation is a category that applies only to phenomena."),
        PQ("State the universal law and humanity formulations of the categorical imperative, and apply each to false promises.",
           "Model answer: universal law: act only on a maxim you can will as a universal law. A false promise cannot be universalised because promising would collapse. Humanity: treat persons as ends, never merely as means. "
           "A false promise uses the lender as a mere means to get money, without his rational consent."),
        PQ("Evaluate Kant's claim that moral worth lies in acting from duty.",
           "Model plan: explain acting from duty versus in accordance with duty (shopkeeper). For: it protects morality from luck and self-interest, and respects persons. Against: it ignores consequences; it can seem cold; duties may conflict. "
           "Judgement: a valuable account of motive and respect for persons, but incomplete without attention to consequences and the weighing of duties."),
        SUM("Kant answers rationalists and empiricists: knowledge needs both concepts and sensations; the mind shapes experience through space, time and the categories.",
            "Synthetic a priori judgements are possible; we know phenomena, not things in themselves (noumena).",
            "Moral worth belongs to the good will acting from duty, not to consequences.",
            "Hypothetical imperatives depend on desire; the categorical imperative commands unconditionally: universal law, humanity as an end, autonomy.",
            "Objections: rigidity, conflict of duties, neglect of consequences; strengths: equal respect and human dignity."),
    ],
))
