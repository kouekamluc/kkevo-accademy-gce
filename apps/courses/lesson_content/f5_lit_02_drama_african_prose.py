"""Form 5 Literature in English: Shakespearean Drama and African Prose Fiction (14 lessons, one practice set each)."""

from .dsl import *  # noqa: F403

COURSE = ("literature-in-english", "form-5")

DRAMA = "Shakespearean Drama"
AFRICAN = "African Prose Fiction"

LESSONS = []

# ------------------------------------------------------------------ 1. Shakespeare's theatre
LESSONS.append(lesson(
    module=DRAMA,
    topic="Shakespeare's theatre and Elizabethan context",
    title="Shakespeare's theatre and the Elizabethan world",
    slug="lit2-shakespeare-theatre-elizabethan-context",
    minutes=20,
    summary="How an open-air playhouse, boy actors, verse and the beliefs of the age shaped Shakespeare's plays, and how to use this background to read Macbeth and As You Like It.",
    objectives=[
        "Describe the main features of an Elizabethan playhouse such as the Globe",
        "Explain how words, not scenery, created place and time on Shakespeare's stage",
        "Name the main beliefs of the age (order, kingship, witchcraft) that matter for Macbeth",
        "Distinguish tragedy from comedy and verse from prose in a Shakespeare play",
    ],
    key_concepts=["Elizabethan and Jacobean", "Groundlings", "Blank verse and prose", "Tragedy", "Comedy", "Divine right of kings"],
    blocks=[
        H("Introduction"),
        T("Think of a storyteller at night in a village compound. There is no electricity, no microphone and no painted backdrop. "
          "The storyteller uses voice and words, and the listeners build the scene in their minds. Shakespeare's theatre worked in a "
          "similar way. The words of the play did the work that scenery, lighting and cameras do today."),
        T("This lesson gives you the background you need for the two Shakespeare plays on the syllabus, Macbeth and As You Like It. "
          "Keep it short and practical: its purpose is to help you understand what you read on the page."),
        D("**Elizabethan** means belonging to the reign of Queen Elizabeth I (1558 to 1603). **Jacobean** means belonging to the reign of "
          "King James I (1603 to 1625). Shakespeare (1564 to 1616) wrote in both periods.", title="Elizabethan and Jacobean"),
        T("As You Like It is usually dated to about 1599, in Elizabeth's reign. Macbeth is usually dated to about 1606, in James's reign. "
          "Dates of plays are estimates, so write 'about' or 'c.' in an answer."),
        H("The playhouse"),
        D("A **groundling** was a spectator who paid a small price to stand in the open space in front of the stage, called the yard. "
          "Wealthier spectators paid more to sit in the covered galleries.", title="Groundling"),
        IMG("f5lit-2-globe-theatre.svg", alt="Schematic of an open-air playhouse: raised stage with trap door, back wall with doors and an upper level, a roof over the stage, galleries at the sides and the yard in front",
            caption="Figure 1. A schematic playhouse. The Globe, used by Shakespeare's company, was of this open-air type."),
        KEY("Features of the stage", "Learn these five and say what each allowed the playwright to do.", cards=[
            ["Raised platform stage", "Pushed out into the yard so that actors were close to spectators on three sides. A soliloquy felt like a private talk with the crowd."],
            ["Back wall with doors", "Two main doors for entrances and exits. Characters could arrive and leave in groups or alone."],
            ["Upper level", "Used as a balcony, a castle wall or a window. Scenes could happen high and low at the same time."],
            ["Trap door", "Used for ghosts, spirits and graves. Useful for plays about witches and apparitions."],
            ["The Heavens", "A painted roof over part of the stage, so that gods, thunder and cannon sounds seemed to come from above."],
        ]),
        T("Plays were performed in daylight, so there was no darkness on stage. Women's parts were played by boys, because professional "
          "actresses did not appear on the English public stage in Shakespeare's time. There was no front curtain and very little scenery."),
        H("How words replaced scenery"),
        EX("Worked example 1: showing night on a daylight stage", intro="Explain how a playwright in an open-air daylight theatre could make the audience believe a scene takes place at night.", steps=[
            S("Name the problem", text="The sun is shining on actors and spectators, so lighting cannot make darkness."),
            S("Use the words", text="Characters say what time it is and describe the dark. The audience accepts the information."),
            S("Use simple props", text="An actor carries a torch, which tells the audience it is dark."),
            S("Give a text example", text="In Macbeth Act 2 Scene 1, Banquo and his son Fleance talk about the hour and the moon while a torch is carried. The audience understands that it is night."),
        ]),
        H("The beliefs of the age"),
        D("The **divine right of kings** was the belief that a king is chosen by God, so killing a king is a sin against God as well as a "
          "crime against the state.", title="Divine right of kings"),
        D("The **chain of being** was the belief that God made an ordered world, from God and angels at the top, through kings, nobles and "
          "ordinary people, to animals and objects. Breaking the order of any link was thought to disturb the whole.", title="Chain of being"),
        T("Many people in Shakespeare's England also believed in witches, ghosts and omens. King James I had written a book about "
          "witchcraft (Daemonologie, 1597). Scholars often link this interest to the witches in Macbeth. They also note that James was "
          "Scottish and believed he was descended from Banquo, which may be why Macbeth is set in Scotland and treats Banquo with respect. "
          "These links are views of scholars: say 'it is thought that' in an answer."),
        KEY("Why this matters for Macbeth", "An Elizabethan or Jacobean audience would feel that killing Duncan, a king, breaks every kind of order.", cards=[
            ["In the play", "After the murder, the night is strange, birds and animals behave oddly, and the whole country suffers."],
            ["The link", "Disorder in the king's life becomes disorder in nature. Look for this when you study the play's imagery."],
        ]),
        H("Verse, prose and kinds of play"),
        T("Shakespeare mixes **verse** and **prose**. Noble characters usually speak verse, especially in serious moments. Verse in his plays is "
          "mostly **blank verse**: lines of ten syllables that do not rhyme, with a rhythm of five beats. Comic characters, letters and "
          "some emotional breakdowns are often in prose. Rhyming couplets (two lines that rhyme) often close a scene or a speech."),
        D("A **tragedy** is a serious play about the fall of a person who is great or high in rank. It ends in disaster, usually death. "
          "The hero often has a **tragic flaw**, a weakness that leads to the fall. Macbeth is a tragedy.", title="Tragedy"),
        D("A **comedy** is a play whose problems are solved and which ends happily, often in marriage and reconciliation. "
          "As You Like It is a comedy. A comedy is not always only funny: it can have serious moments and danger.", title="Comedy"),
        MISTAKE("Writing about the author's life instead of the text", "The Board's 2023 report advises teachers to focus on contextual analysis, "
                "which means studying how an extract works within the text. Facts about Shakespeare's life or the playhouse earn credit only "
                "when you use them to explain something in the play."),
        QUIZ("Why did Shakespeare's characters often tell the audience what time of day it was?", [
            "Because actors forgot their lines",
            "Because the plays were performed in daylight with little scenery, so words had to show time and place",
            "Because the law forbade plays at night and in the day",
            "Because the audience could not see the stage",
        ], 1, "Words did the work of scenery and lighting.", hint="Think about the sun shining on an open-air stage.",
             feedback=["Characters speak this way on purpose, to build the scene.", "",
                       "There was no such law; the point is the theatre's design.", "Spectators could see the stage well; the problem was darkness."]),
        QUIZ("A play ends with the death of its hero after a fall caused by a weakness. What is it?", [
            "A comedy", "A tragedy", "A pastoral", "A masque",
        ], 1, "A tragedy shows the fall of a great person, often through a flaw.", hint="Which kind of play ends in disaster?",
             feedback=["A comedy ends happily.", "", "A pastoral is set among shepherds and the country; it is not defined by a sad ending.", "A masque was a courtly entertainment with music and dance."]),
        TIP("Exam link: Macbeth and As You Like It appear in Paper 1 (multiple choice) and in Paper 2, Section A, Drama. This background helps you explain "
            "extracts, but answers must be built on the text. Use the Board's report as a reminder to own a copy of the play."),
        PQ("Name three features of an Elizabethan open-air playhouse.", "Any three of: a raised stage pushed into the yard, groundlings standing in the yard, galleries for seated spectators, a back wall with doors, an upper level, a trap door, a roof over the stage (the Heavens)."),
        PQ("Explain why boys played women's parts in Shakespeare's theatre.", "Professional actresses did not perform on the English public stage in his time, so boys in female costume took women's parts. This matters for As You Like It, in which Rosalind, played by a boy, disguises herself as a boy."),
        PQ("What is the difference between verse and prose in a Shakespeare play? Give one use of prose.", "Verse is lines with a regular rhythm (mostly blank verse of ten syllables); prose is ordinary speech without rhythm or rhyme. Prose is often used by comic or low-ranking characters, for letters and for some breakdowns."),
        PQ("In two sentences, explain why the murder of a king would shock an audience in Shakespeare's time.", "They believed in the divine right of kings, so killing a king was a sin against God. They also believed in a chain of being, so disorder at the top would disturb all of nature."),
        SUM("Shakespeare's open-air playhouse had a raised stage, a back wall with doors, an upper level, a trap door and a yard for groundlings; performances were in daylight.",
            "Words, torches and costumes created time and place; boys played women's parts.",
            "Elizabethan and Jacobean beliefs include the divine right of kings, the chain of being and belief in witches and omens.",
            "Tragedy shows a great person's fall; comedy ends in reconciliation and marriage; blank verse and prose have different uses.",
            "Use background only to explain the text: the Board stresses contextual analysis."),
    ],
))

# ------------------------------------------------------------------ 2. Macbeth plot, Acts 1-2
LESSONS.append(lesson(
    module=DRAMA,
    topic="Macbeth: plot and structure",
    title="Macbeth, Acts 1 and 2: prophecy and murder",
    slug="lit2-macbeth-plot-acts-1-2",
    minutes=22,
    summary="Act by act, from the witches' meeting and the battle report to the murder of King Duncan and Macbeth's crowning, with the events you must keep in the right order.",
    objectives=[
        "Retell the events of Acts 1 and 2 of Macbeth in the right order",
        "Explain how the witches' prophecies, Lady Macbeth and Macbeth's ambition lead to Duncan's murder",
        "Say who is present and what is said in the key scenes (Act 1 Scene 3, Act 1 Scene 7, Act 2 Scene 2)",
        "Avoid mixing up events from different scenes, as the Board's report says candidates do",
    ],
    key_concepts=["Thane", "Prophecy", "Prince of Cumberland", "Dagger scene", "Porter scene", "Flight of Malcolm and Donalbain"],
    blocks=[
        H("Introduction"),
        T("Imagine a trusted senior prefect who is told, by strangers, that one day he will be head of the school. At first it is only a "
          "strange idea, but then the first part of what they said comes true, and the idea grows. Macbeth begins in the same way: "
          "a brave soldier hears a prophecy, and then slowly decides to make it come true by crime."),
        T("The Board's 2023 report says questions in the new syllabus were set mostly on the early part of Macbeth. Knowing Acts 1 and 2 "
          "in order and in detail is therefore valuable."),
        D("A **thane** is a Scottish noble who holds land from the king. Macbeth is Thane of Glamis. The title **Thane of Cawdor** is "
          "given to him in Act 1.", title="Thane"),
        D("A **prophecy** is a statement about what will happen in the future. In Macbeth the witches' prophecies set the plot moving.", title="Prophecy"),
        H("Act 1: the temptation"),
        KEY("Act 1 in order", "Scene numbers follow most school editions; check your text.", cards=[
            ["Scene 1", "Three witches meet on a heath in thunder and agree to meet Macbeth. They end with the idea that fair is foul and foul is fair."],
            ["Scene 2", "At King Duncan's camp a wounded Captain reports how Macbeth fought bravely against the rebel Macdonwald and a Norwegian army. Ross says the Thane of Cawdor betrayed Scotland. Duncan orders his death and gives the title to Macbeth."],
            ["Scene 3", "Macbeth and Banquo meet the witches on the heath. The witches greet Macbeth as Thane of Glamis, Thane of Cawdor and a future king. They tell Banquo he will be lesser and greater than Macbeth and that his descendants will be kings. Ross and Angus bring news that Macbeth is Thane of Cawdor. Macbeth speaks aside, afraid of his own thoughts."],
            ["Scene 4", "Duncan thanks Macbeth and Banquo and names his son Malcolm Prince of Cumberland, his heir. Macbeth speaks aside: Malcolm is a step he must get past. Duncan will stay at Macbeth's castle at Inverness."],
            ["Scene 5", "At Inverness Lady Macbeth reads Macbeth's letter. She fears he is too kind to take the crown by crime and calls on spirits to remove her womanly feelings. Macbeth arrives and she tells him to leave the plan to her."],
            ["Scene 6", "Duncan and his lords arrive. He praises the castle's pleasant air and thanks Lady Macbeth."],
            ["Scene 7", "Macbeth considers the murder in a soliloquy and gives reasons against it: Duncan is his kinsman, his king and his guest, and a good ruler. Lady Macbeth mocks his courage and plans to make the chamberlains drunk and blame them. Macbeth agrees."],
        ]),
        T("Three points are often confused. First, Macbeth is already Thane of Glamis. Second, he is made Thane of Cawdor in Scene 2 by Duncan, and learns it in Scene 3. Third, the witches' third greeting, 'king hereafter', is the prophecy that starts the temptation."),
        H("Act 2: the murder"),
        KEY("Act 2 in order", "The murder happens off stage; the audience learns of it from Macbeth and Lady Macbeth.", cards=[
            ["Scene 1", "Banquo and his son Fleance meet Macbeth in the night. Banquo has dreamed of the witches. Alone, Macbeth sees a dagger in the air in a soliloquy. A bell rings, Lady Macbeth's signal, and he goes to kill Duncan."],
            ["Scene 2", "Lady Macbeth has drugged the guards' drink. Macbeth returns with the daggers, shaken, hearing a voice that says he has murdered sleep. Lady Macbeth takes the daggers back to place them with the guards. A knocking begins at the gate."],
            ["Scene 3", "The drunken Porter, slow to open the gate, pretends to be the porter of hell. Macduff and Lennox arrive. Macduff finds the dead king and raises the alarm. Macbeth kills the guards, saying anger made him act. Malcolm and Donalbain decide to flee, Malcolm to England and Donalbain to Ireland."],
            ["Scene 4", "Ross and an Old Man discuss the strange events since the murder. Macduff reports that the guards are blamed, that Malcolm and Donalbain seem suspect because they fled, and that Macbeth will be crowned at Scone."],
        ]),
        H("Worked examples"),
        EX("Worked example 1: a model answer plan", intro="Question: Describe how Macbeth's meeting with the witches affects him in Act 1. Plan a paragraph answer from the text.", steps=[
            S("Point 1: what they say", text="The witches hail him as Thane of Glamis, Thane of Cawdor and king hereafter."),
            S("Point 2: the first part comes true", text="Ross and Angus bring news that he is Thane of Cawdor. Macbeth sees that one prophecy has come true."),
            S("Point 3: his reaction", text="He speaks in an aside and is frightened by his thoughts of murder. The audience sees ambition already working."),
            S("Point 4: link to what follows", text="He writes to his wife. In Scene 4 Malcolm is named heir, and Macbeth sees him as an obstacle."),
        ]),
        EX("Worked example 2: how Lady Macbeth persuades him", intro="Question: In Act 1 Scene 7, how does Lady Macbeth persuade Macbeth to kill Duncan?", steps=[
            S("Start with his doubts", text="Macbeth gives reasons against the murder: loyalty to his king, his role as host, and Duncan's goodness."),
            S("Attack his manhood", text="She questions his courage and says that if he loved her he would act."),
            S("Make a plan", text="She tells him how: make the guards drunk and put the blame on them."),
            S("Conclude", text="Macbeth agrees. The scene shows her strong will and his lack of resolve."),
        ]),
        MISTAKE("Mixing up the scenes", "The Board's report says that in one Macbeth question candidates wrote about the three witches where the answer concerned war, and the other way round. "
                "Keep a clear list: war and the Captain are in Act 1 Scene 2; the witches are in Scene 1 and Scene 3."),
        MISTAKE("Saying Macbeth kills Duncan on stage", "The murder takes place off stage. We hear about it from Macbeth and Lady Macbeth in Act 2 Scene 2."),
        QUIZ("Who tells Macbeth that he has been named Thane of Cawdor?", [
            "The Captain", "Banquo", "Ross and Angus", "Lady Macbeth",
        ], 2, "Ross and Angus bring Duncan's message in Act 1 Scene 3.", hint="Two thanes bring the news on the heath.",
             feedback=["The Captain reports the battle, not the title.", "Banquo is with Macbeth and hears the news too.", "", "She learns of it by letter, after the news."]),
        QUIZ("Where do Malcolm and Donalbain go after their father's death?", [
            "Both go to England", "Malcolm to England and Donalbain to Ireland", "Both go to Norway", "They stay at Inverness",
        ], 1, "Malcolm goes to England and Donalbain to Ireland (Act 2 Scene 3).", hint="They go in different directions.",
             feedback=["Only Malcolm goes to England.", "", "Norway is the invading country in Act 1, not the princes' refuge.", "They flee because they fear for their lives."]),
        TIP("Exam link: plot and extract questions on Macbeth appear in Paper 1 and in Paper 2, Section A. Most extract questions want you to place the extract: say who is speaking, "
            "to whom, where in the play, what has just happened and what happens next."),
        PQ("Name the two thane titles in the story of Act 1 and the future title the witches promise.", "Macbeth is already Thane of Glamis. He is made Thane of Cawdor after the old Thane of Cawdor is condemned as a traitor. The witches promise that he will be king hereafter."),
        PQ("Why does Macbeth hesitate before killing Duncan? Give two reasons from Act 1 Scene 7.", "Duncan is his kinsman and his king, and Macbeth is his host, so he should protect him. Duncan is also a good king, so murder would bring judgement."),
        PQ("Describe what happens in Act 2 Scene 2 in four sentences.", "Lady Macbeth waits while Macbeth kills Duncan. Macbeth returns shaken, still holding the daggers, and says he heard a voice cry that he has murdered sleep. Lady Macbeth takes the daggers back and smears the guards with blood. A knocking is heard at the gate."),
        PQ("What does the Porter scene in Act 2 Scene 3 do for the play?", "It gives comic relief after the murder, and by imagining himself the porter of hell it hints that Macbeth's castle has become a place of evil. It also delays the discovery and increases tension."),
        SUM("Act 1: witches, report of Macbeth's bravery, Cawdor title, Malcolm made heir, Lady Macbeth's plan, Macbeth's soliloquy and decision.",
            "Act 2: dagger soliloquy, murder off stage, knocking, Porter, discovery, killing of the guards, flight of Malcolm and Donalbain, Macbeth to be crowned.",
            "The witches start the temptation; Lady Macbeth supplies the push; Macbeth makes the choice.",
            "Place every extract: speaker, listener, setting, what happens before and after.",
            "Scene numbers vary in some editions: check your text."),
    ],
))

# ------------------------------------------------------------------ 3. Macbeth plot, Acts 3-5
LESSONS.append(lesson(
    module=DRAMA,
    topic="Macbeth: plot and structure",
    title="Macbeth, Acts 3 to 5: tyranny and downfall, and the play's structure",
    slug="lit2-macbeth-plot-acts-3-5",
    minutes=24,
    summary="From Banquo's murder and the banquet to the apparitions, the killing of Macduff's family, Lady Macbeth's sleepwalking and Macbeth's death, plus the five-part structure of a tragedy.",
    objectives=[
        "Retell the events of Acts 3, 4 and 5 of Macbeth in the right order",
        "Explain how each of the three apparitions is fulfilled in the final act",
        "Describe the structure of the play: exposition, rising action, climax, falling action, catastrophe",
        "Recognise where editions differ on scene numbers and mark these 'check your text'",
    ],
    key_concepts=["Banquet scene", "Apparitions", "Birnam Wood", "Sleepwalking", "Climax", "Catastrophe"],
    blocks=[
        H("Introduction"),
        T("In Acts 1 and 2 Macbeth gets the crown. In Acts 3 to 5 he finds that having it does not bring peace. One crime needs another, "
          "enemies grow, and an army marches against him. A useful way to remember the second half is: he kills to feel safe, but each killing makes him less safe."),
        H("Act 3: Macbeth the king"),
        KEY("Act 3 in order", "Scene numbers can vary; check your text, especially for Scene 5.", cards=[
            ["Scene 1", "Banquo suspects that Macbeth killed Duncan, but also hopes his own children will be kings. Macbeth, now king, fears Banquo and invites him to a feast. He asks where Banquo and Fleance are riding that evening and hires two murderers, persuading them that Banquo is their enemy."],
            ["Scene 2", "Lady Macbeth sees that he is troubled. He says that Duncan's murder has not made him safe and that a deed is planned for the night. He tells her to be innocent of the knowledge."],
            ["Scene 3", "The murderers, joined by a third man, attack Banquo and Fleance. Banquo dies, but Fleance escapes."],
            ["Scene 4", "At the banquet, a murderer tells Macbeth that Banquo is dead and Fleance has escaped. Banquo's ghost sits in Macbeth's place. Only Macbeth sees it, and he speaks wildly. Lady Macbeth sends the guests away. Macbeth decides to visit the witches again."],
            ["Scene 5", "Hecate, the goddess of witchcraft, scolds the witches. Many editors think this scene was added by another writer: check your text."],
            ["Scene 6", "Lennox and another lord speak in cautious irony about the deaths and say that Macduff has gone to England to join Malcolm."],
        ]),
        H("Act 4: the apparitions and the cruelty"),
        KEY("Act 4 in order", "", cards=[
            ["Scene 1", "In a cave the witches prepare a cauldron. Macbeth demands answers and sees three apparitions: an armed head that warns him to beware Macduff; a bloody child that says no man born of woman will harm him; and a crowned child with a tree that says he will not be beaten until Birnam Wood comes to Dunsinane Hill. A show of kings follows, ending with Banquo's descendants. Macbeth learns that Macduff has fled to England and decides to kill Macduff's family."],
            ["Scene 2", "Lady Macduff is angry that her husband has gone. She talks with her young son. Murderers enter and kill the boy and, we understand, his mother."],
            ["Scene 3", "In England Malcolm tests Macduff's loyalty by pretending to have terrible vices. Macduff is horrified, and Malcolm reveals he was testing him. Ross brings news that Macduff's family is dead. Macduff is overcome with grief, and Malcolm urges him to turn it into anger. English forces under Siward are ready."],
        ]),
        H("Act 5: the fall"),
        KEY("Act 5 in order", "Scene numbers differ between editions; this lesson gives events, not exact numbers. Check your text.", cards=[
            ["Sleepwalking", "A doctor and a gentlewoman watch Lady Macbeth walk in her sleep, rubbing her hands as if to wash away blood and speaking of what she has done."],
            ["Scotland's lords", "Scottish lords march towards Birnam to join the English army against Macbeth."],
            ["Macbeth in Dunsinane", "He is full of false confidence because of the apparitions, but hears of the English forces and orders his armour."],
            ["Birnam Wood", "Malcolm orders every soldier to cut a branch and carry it to hide the army's size."],
            ["Lady Macbeth's death", "Macbeth hears a cry of women and is told that the queen is dead. His reply is the speech beginning 'Tomorrow, and tomorrow'. A messenger reports that Birnam Wood seems to move."],
            ["The battle", "Macbeth kills young Siward. He meets Macduff, who says he was 'untimely ripped' from his mother's womb. Macbeth realises the witches have deceived him, but fights on and is killed. Macduff brings in his head. Malcolm is hailed as King of Scotland and invites all to his coronation at Scone."],
        ]),
        H("The structure of the play"),
        D("**Exposition** introduces the people and situation. **Rising action** builds the conflict. The **climax** is the high point or turning point. "
          "**Falling action** follows the results. In a tragedy the **catastrophe** is the final disaster that ends the hero's story.", title="Parts of a tragic plot"),
        IMG("f5lit-2-macbeth-arc.svg", alt="An arch with Exposition, Rising action, Climax, Falling action and Catastrophe, labelled with the five acts of Macbeth", caption="Figure 1. A five-part shape for Macbeth. Textbooks differ on where exactly the climax falls: check your textbook."),
        T("Some textbooks choose the murder of Duncan as the climax because it is the central crime. Others choose the banquet scene (Act 3 Scene 4) as the turning point where Macbeth's control begins to slip. Either answer can score if you explain it with evidence."),
        H("Worked examples"),
        EX("Worked example 1: the apparitions and their fulfilment", intro="Question: Show how the three apparitions are fulfilled in the last act.", steps=[
            S("Armed head", text="It warns him to beware Macduff. In the final fight, Macduff is the man who kills him."),
            S("Bloody child", text="It says no man born of woman can harm him. Macduff says he was 'untimely ripped' from his mother, so he was not born in the usual way."),
            S("Crowned child with a tree", text="Birnam Wood will come to Dunsinane. Malcolm's soldiers carry branches, so the wood seems to move."),
            S("Conclusion", text="Each promise is true in a way Macbeth did not expect. His overconfidence is part of his fall."),
        ]),
        EX("Worked example 2: Macduff's family", intro="Question: Why does Macbeth have Macduff's family killed, and what is the effect?", steps=[
            S("Cause", text="Macbeth is told to beware Macduff, then hears that Macduff has fled to England."),
            S("Action", text="He decides to strike at once and sends murderers to Macduff's castle."),
            S("Effect on Macduff", text="Macduff is shattered but turns grief into determination to take revenge."),
            S("Effect on the audience", text="Macbeth now seems a tyrant who kills the innocent, so sympathy for him is reduced."),
        ]),
        MISTAKE("Saying Macbeth is killed by Malcolm or Siward", "Macduff kills Macbeth. Young Siward is killed by Macbeth earlier in the same battle."),
        MISTAKE("Giving exact Act 5 scene numbers without checking", "Editions divide the final act into different numbers of scenes. If you are not sure, name the event (the sleepwalking scene, the final battle) or write 'check your text'."),
        QUIZ("Which character sees Banquo's ghost at the banquet?", [
            "All the lords", "Lady Macbeth only", "Macbeth only", "Macduff only",
        ], 2, "Only Macbeth sees the ghost, which is why the lords think he is ill and Lady Macbeth sends them away.", hint="The others see an empty seat.",
             feedback=["The lords see nothing and are puzzled.", "Lady Macbeth sees nothing and tells him it is a fit.", "", "Macduff is not at the banquet."]),
        QUIZ("Why does Macbeth feel safe from Macduff's attack late in the play?", [
            "He believes no man born of woman can harm him", "He has an army of thousands", "Macduff is in prison", "Banquo's ghost guards him",
        ], 0, "The second apparition says no man born of woman will harm him.", hint="Think of the second apparition.",
             feedback=["", "He has some forces but the confidence comes from the prophecy.", "Macduff is free and in England.", "The ghost frightens him; it does not protect him."]),
        TIP("Exam link: Paper 2, Section A questions use extracts from any part of the play, but the Board's report says early extracts were popular in its first session on the new syllabus. Study the whole play, and do not skip Acts 4 and 5."),
        PQ("Describe in four sentences what happens at the banquet in Act 3 Scene 4.", "Macbeth has Banquo killed and hears that Fleance escaped. At the feast Banquo's ghost sits in Macbeth's seat, and only Macbeth sees it. He speaks wildly to it in front of the guests. Lady Macbeth sends the guests away and Macbeth decides to see the witches again."),
        PQ("Why does Malcolm test Macduff in England in Act 4 Scene 3?", "Malcolm does not know if Macduff is loyal or a spy sent by Macbeth. He pretends to have terrible vices to see Macduff's reaction. When Macduff cries out in horror, Malcolm knows he is honest."),
        PQ("Explain how Lady Macbeth's end is shown in Act 5.", "She walks in her sleep, rubbing her hands as if trying to wash away blood and speaking of the murders. The doctor cannot help her. Later Macbeth is told she is dead, and Malcolm's final speech suggests she died by her own hand (check your text)."),
        PQ("Name the five parts of a tragic plot and say where you would put the murder of Duncan.", "Exposition, rising action, climax, falling action and catastrophe. The murder can be placed at or near the climax (Act 2). Some textbooks put the climax at the banquet in Act 3 instead, so give a reason."),
        SUM("Act 3: Banquo is murdered, Fleance escapes, and Banquo's ghost disturbs the banquet.",
            "Act 4: the apparitions mislead Macbeth, Macduff's family is killed, and Malcolm and Macduff prepare an English attack.",
            "Act 5: Lady Macbeth's sleepwalking and death, Birnam Wood moves, Macduff kills Macbeth, Malcolm is hailed king.",
            "Structure: exposition, rising action, climax, falling action, catastrophe. Where the climax falls is a matter for argument.",
            "Where editions differ on scene numbers, name the event or write 'check your text'."),
    ],
))

# ------------------------------------------------------------------ 4. Macbeth characters
LESSONS.append(lesson(
    module=DRAMA,
    topic="Macbeth: characters",
    title="The characters of Macbeth",
    slug="lit2-macbeth-characters",
    minutes=22,
    summary="Who is who in Macbeth, how Macbeth and Lady Macbeth change, how Banquo, Duncan, Macduff and Malcolm act as contrasts, and how to prove a character trait from the text.",
    objectives=[
        "Describe Macbeth, Lady Macbeth, Banquo, Duncan, Macduff and Malcolm with evidence from the play",
        "Explain how Macbeth and Lady Macbeth change between Act 1 and Act 5",
        "Use Banquo and Macduff as foils (contrasting characters) in an answer",
        "Use the four ways of showing character: what a person says, does, is said to be, and how the writer names them",
    ],
    key_concepts=["Tragic hero", "Foil", "Characterization", "Loyalty", "Conscience", "Tyrant"],
    blocks=[
        H("Introduction"),
        T("In a school you may know a pupil who is clever and popular, but who is tempted to cheat by a friend. The pupil is not simply good or bad: "
          "he has strengths and a weakness. Shakespeare's Macbeth is built in this way. He begins as a hero and ends as a tyrant, and the play makes us watch how."),
        T("The Board's report notes that candidates are good when the question is on a main character, as with The Immortal Seed's Assi and The Crown of Thorns' D.O., "
          "and weak when they confuse characters. In Macbeth, learn who is who."),
        H("Who is who?"),
        KEY("The main characters", "", cards=[
            ["Macbeth", "A brave general and Thane of Glamis, later Cawdor and then king. The hero of the play, and also its villain."],
            ["Lady Macbeth", "His wife. Ambitious and strong-willed, she persuades him to murder Duncan. Later she is destroyed by guilt."],
            ["Banquo", "Macbeth's fellow general. Loyal and honourable. The witches say his descendants will be kings. Father of Fleance."],
            ["Duncan", "The King of Scotland. A gentle, trusting and generous ruler. Father of Malcolm and Donalbain."],
            ["Macduff", "Thane of Fife. Loyal to Scotland. He discovers Duncan's body, leaves his family to join Malcolm, and kills Macbeth."],
            ["Malcolm", "Duncan's elder son. He flees, builds an army in England and becomes king. He is cautious, wise and fair."],
        ]),
        T("Minor characters to know: Fleance (Banquo's son, who escapes), Donalbain (Duncan's younger son), Lady Macduff and her son, Ross, Lennox, Angus, "
          "Siward (English general) and young Siward, the Porter, the doctor and gentlewoman, Hecate, and the three witches."),
        H("Macbeth: a tragic hero"),
        D("A **tragic hero** is a person of high rank and real qualities whose fall comes from a weakness (a **tragic flaw**) and from his own choices. "
          "We pity him and also fear what he does.", title="Tragic hero"),
        T("In Act 1 Scene 2 others praise Macbeth as brave and loyal. His flaw is ambition, which his wife and the witches work on. "
          "He is imaginative (he sees a dagger and a ghost) and he feels guilt. These make him human, and it is why we do not hate him completely."),
        T("As the play goes on, Macbeth becomes more ruthless: he kills Banquo, has Macduff's family killed, and rules by fear. Yet at the end he fights bravely to the last, "
          "so some sympathy returns."),
        EX("Worked example 1: the change in Macbeth", intro="Question: How does Macbeth change between Act 1 and Act 5? Plan an answer.", steps=[
            S("Act 1", text="He is a loyal soldier, praised by Duncan, but frightened by his own thoughts of murder after the witches."),
            S("Middle of the play", text="He kills Duncan in Act 2, Banquo in Act 3 and Macduff's family in Act 4. Each time the guilt appears to be less."),
            S("Act 5", text="He is isolated, his wife is dead and he sees life as meaningless. He is brave in the final fight."),
            S("Conclusion", text="He changes from a loyal hero to a tyrant, though some courage remains."),
        ]),
        H("Lady Macbeth"),
        T("In Act 1 she is the stronger partner. She calls on dark spirits to take away her softness, she mocks Macbeth's courage and she makes the plan. "
          "She is hard on the night of the murder, saying that a little water clears them of the deed."),
        T("By Act 5 she is a different woman. She sleepwalks, tries to wash invisible blood from her hands and cannot sleep without a light. "
          "Guilt that she tried to push aside has broken her. She dies off stage; Malcolm's final speech suggests she took her own life (check your text)."),
        MISTAKE("Calling Lady Macbeth simply evil", "Examiners prefer a balanced answer. She is ambitious and cruel in planning the murder, but she shows limits (Duncan looked like her father) and she suffers terribly from guilt."),
        H("Banquo, Duncan, Macduff and Malcolm as foils"),
        D("A **foil** is a character who is a contrast to another, so that each shows the other more clearly.", title="Foil"),
        KEY("Contrasts", "", cards=[
            ["Banquo and Macbeth", "Both hear the prophecies. Banquo is troubled but refuses to act against the king; Macbeth acts. Banquo shows what Macbeth might have been."],
            ["Duncan and Macbeth", "Duncan is a trusting, generous king. Macbeth is a fearful tyrant. Duncan's goodness makes his murder a worse crime."],
            ["Macduff and Macbeth", "Macduff puts country before family and comes back as the avenger. He is loyal where Macbeth is treacherous."],
            ["Malcolm and Macbeth", "Malcolm is careful and clever and tests Macduff; Macbeth is reckless. Malcolm becomes the ruler Scotland needs."],
        ]),
        H("Proving a character trait"),
        T("When you say a character is ambitious, prove it. There are four ways to find evidence. What the person **says**, what the person **does**, "
          "what **others say** about him or her, and how the writer shows his or her inner thoughts (for example in a soliloquy)."),
        EX("Worked example 2: proving that Banquo is honourable", intro="Question: What kind of man is Banquo? Support your answer with the play.", steps=[
            S("Says", text="After the witches' prophecies he warns that evil may use small truths to lead people astray."),
            S("Does", text="He does not act against Duncan. He stays loyal in Act 2 even though he is uneasy."),
            S("Others say", text="Duncan praises him and honours him as a loyal friend."),
            S("Conclusion", text="Banquo is honest, loyal and cautious. His murder shows that Macbeth fears goodness."),
        ]),
        MISTAKE("Mixing up Macbeth and Macduff", "The names are similar. Macbeth is the king-killer. Macduff is the thane who kills him. Write the full name, and learn the pair as a contrast."),
        QUIZ("Which word best describes Banquo?", [
            "Treacherous", "Loyal and cautious", "Ambitious to be king", "Cowardly",
        ], 1, "Banquo is loyal and honourable, though uneasy about the prophecy.", hint="He is the foil to Macbeth.",
             feedback=["It is Macbeth who betrays.", "", "Banquo's family is promised the throne, but he does nothing wrong to get it.", "He is not a coward."]),
        QUIZ("What is a foil?", [
            "A character who is a contrast to another", "A character who dies in Act 1", "A servant of the king", "A character with no lines",
        ], 0, "A foil shows another character more clearly by contrast.", hint="Think of contrast.",
             feedback=["", "Death in Act 1 has no link to the word.", "A servant is a rank, not a literary role.", "The number of lines is not the point."]),
        TIP("Exam link: character questions appear in Paper 1 (who said what to whom) and in Paper 2 Section A (for example on Macbeth or Lady Macbeth). Name the character, give one trait, and back it with an event or a few words from the text."),
        PQ("Give three qualities of Macbeth in Act 1 and one event that shows each.", "Brave: he fights well against Macdonwald and the Norwegians. Ambitious: he reacts with fear and desire to the prophecy. Loyal but tempted: he feels the duties of kinsman, subject and host before he agrees to kill Duncan."),
        PQ("How does Lady Macbeth change in the course of the play?", "In Act 1 she is strong, planning the murder and urging Macbeth. By Act 5 she is haunted by guilt, sleepwalks and tries to wash blood from her hands, and later dies."),
        PQ("Why is Macduff important in Macbeth?", "He discovers Duncan's body and does not attend Macbeth's coronation. He joins Malcolm, loses his family to Macbeth and kills the tyrant at the end."),
        PQ("Choose one foil pair and explain the contrast.", "Banquo and Macbeth: both hear the witches but Banquo refuses to murder for a throne, while Macbeth gives in. This shows Macbeth's choice was not forced."),
        SUM("Macbeth is a tragic hero: brave at first, ruined by ambition, still brave at the end.",
            "Lady Macbeth begins strong and ends broken by guilt.",
            "Banquo, Duncan, Macduff and Malcolm are foils that highlight Macbeth's fall.",
            "Prove traits from what a character says, does, is said to be and thinks.",
            "Keep the names apart: Macbeth, Macduff, Malcolm, Banquo, Fleance, Donalbain."),
    ],
))

# ------------------------------------------------------------------ 5. Macbeth themes
LESSONS.append(lesson(
    module=DRAMA,
    topic="Macbeth: themes",
    title="The themes of Macbeth",
    slug="lit2-macbeth-themes",
    minutes=23,
    summary="Ambition, fate and free will, kingship and tyranny, guilt and conscience, appearance and reality, and order and disorder in Macbeth, each tied to scenes and written up in point-evidence-explain paragraphs.",
    objectives=[
        "Define and explain the main themes of Macbeth: ambition, fate and free will, kingship, guilt, appearance and reality",
        "Link each theme to specific scenes and events",
        "Write a point-evidence-explain paragraph on a theme",
        "Show how several themes are connected, not separate",
    ],
    key_concepts=["Theme", "Ambition", "Fate and free will", "Kingship", "Guilt", "Appearance and reality"],
    blocks=[
        H("Introduction"),
        T("A **theme** is a central idea that a work keeps returning to. It is not the plot, which says what happens. A theme says what the story is about underneath. "
          "A road accident story has the plot of a collision, but its theme might be carelessness. In Macbeth, the plot is a murder and its aftermath, "
          "and the themes include what ambition does to a person."),
        D("A **theme** is an idea that runs through a work and is shown by events, characters and language. Writers rarely state the theme directly; the reader works it out.", title="Theme"),
        H("Ambition"),
        T("Ambition is the strong desire to gain power or rank. In Macbeth it begins as natural but becomes destructive. Macbeth's own speech before the murder admits that "
          "nothing except 'vaulting ambition' pushes him on. Lady Macbeth is also ambitious, for her husband and for herself."),
        T("The play shows that ambition without conscience leads to murder, fear and loss. Macbeth gains the crown but loses sleep, friends, his wife and finally his life."),
        H("Fate and free will"),
        D("**Fate** is the idea that events are fixed in advance. **Free will** is the power to choose. The play asks whether Macbeth was destined to be king, or whether he chose to kill.", title="Fate and free will"),
        T("The witches' prophecies suggest fate. But they never tell Macbeth to murder Duncan. Banquo hears the same prophecy and does not kill anyone. "
          "Macbeth makes his own choices, so most readers say he is responsible, even though the witches tempt him."),
        EX("Worked example 1: a point-evidence-explain paragraph", intro="Question: Does Macbeth have free will? Write one paragraph.", steps=[
            S("Point", text="Macbeth is responsible for his crimes, because the witches only tell him what will happen."),
            S("Evidence", text="They do not order the murder. Banquo hears prophecies too, and stays loyal in Act 2."),
            S("Explain", text="So the temptation is shared by both men, but only Macbeth chooses violence. The prophecies offer a possibility, and he turns it into action."),
            S("Link", text="This shows that ambition and choice, not fate alone, bring about his fall."),
        ]),
        H("Kingship and tyranny"),
        T("The play compares a good king and a tyrant. Duncan is generous and trusted. Macbeth rules by fear: he kills Banquo and Macduff's family, and Scotland suffers. "
          "In Act 4 Scene 3, Malcolm and Macduff discuss the qualities of a good ruler, and the play praises the English king for his holiness. "
          "(Check your text for the lines.)"),
        KEY("Good king and tyrant", "", cards=[
            ["Duncan", "Gentle, trusted, rewards loyalty. Disorder follows his death."],
            ["Macbeth", "Rules by fear and violence, trusts no one, and is hated by his subjects."],
            ["Malcolm", "Cautious and fair. He becomes king in the final scene and promises to restore order."],
        ]),
        H("Guilt and conscience"),
        T("**Guilt** is the painful feeling of having done wrong. **Conscience** is the inner voice that judges our actions. Macbeth hears a voice that says he has murdered sleep, and he is afraid of his own hands. "
          "At the banquet he sees Banquo's ghost. Lady Macbeth, who seemed hard, sleepwalks and tries to wash imaginary blood from her hands."),
        T("The play shows that guilt follows crime into the mind, even when no one can prove who did it."),
        H("Appearance and reality"),
        T("In this play things are not what they seem. The first scene has witches who say that fair is foul and foul is fair. Macbeth's prophecies seem hopeful but lead to ruin. "
          "Duncan trusts those who look loyal. Lady Macbeth tells her husband to look like the innocent flower and be the snake under it (a paraphrase, check your text). "
          "Macbeth also hides his guilt by acting a host's welcome at his banquet."),
        T("The apparitions show the same theme in a different way. They seem to promise safety but hide a trap. This is called **equivocation**: a statement with a hidden second meaning."),
        H("Order and disorder"),
        T("Because kingship was believed to be part of a natural order, the murder of Duncan brings disorder into the world. In Act 2 Scene 4 an Old Man and Ross describe strange events: "
          "darkness in daytime, and Duncan's horses turning wild. The state recovers its order only when Macbeth is removed and Malcolm becomes king."),
        MISTAKE("Retelling the plot instead of discussing the theme", "A theme answer must say what the play suggests about an idea such as ambition, and must use events as evidence. "
                "If your answer begins 'First Macbeth meets the witches...' and never mentions the theme, it will score poorly."),
        MISTAKE("Treating each theme as separate", "The themes are connected: ambition leads to guilt, appearance hides reality, and fate and free will explain who is to blame. Say so in the conclusion."),
        QUIZ("Which theme is shown by the witches' idea that fair is foul and foul is fair?", [
            "Guilt", "Appearance and reality", "Loyalty", "Kingship",
        ], 1, "The line suggests that things are not what they seem.", hint="Think about what looks good but is bad.",
             feedback=["Guilt is the painful feeling after the crime.", "", "Loyalty is shown by Banquo and Macduff.", "Kingship is the question of who rules and how."]),
        QUIZ("A student says the witches forced Macbeth to kill Duncan. What is the best reply?", [
            "The witches never tell him to murder anyone; he chooses to act", "Duncan forced himself to die", "Banquo ordered it", "It happened in a dream",
        ], 0, "The witches offer a prophecy, not an order. Banquo hears the same and stays loyal.", hint="Does any witch say 'kill the king'?",
             feedback=["", "This makes no sense.", "Banquo does not order it.", "The murder happens in the story, not in a dream."]),
        TIP("Exam link: the Board's 2023 report shows that questions test themes (for example love and rescue in As You Like It) as well as characters and extracts. Always begin a theme answer with a sentence that names the theme and gives your point; then give events as evidence."),
        PQ("Explain how ambition leads to Macbeth's fall.", "Macbeth is tempted by the prophecy and his wife. He kills Duncan, then Banquo, then Macduff's family to protect himself. These crimes bring guilt, fear and enemies. At the end he loses his wife, his crown and his life."),
        PQ("Give two examples of the theme of appearance and reality.", "The witches' statement that fair is foul and foul is fair; Lady Macbeth telling Macbeth to look like an innocent flower; the apparitions that seem to promise safety but hide a trap; Macbeth's act of welcome at the banquet."),
        PQ("How does the play contrast good kingship and tyranny?", "Duncan is gentle and trusted, and his reign is peaceful. Macbeth rules by fear and murder, and Scotland suffers. Malcolm, after Macbeth's fall, promises to restore order."),
        SUM("A theme is an idea shown through events, characters and language, not the plot itself.",
            "Ambition drives Macbeth, but he chooses to act: fate tempts and free will decides.",
            "Duncan, Macbeth and Malcolm show good kingship and tyranny.",
            "Guilt shows in the dagger, the ghost and the sleepwalking.",
            "Appearance and reality: fair is foul; the apparitions deceive.",
            "Use point-evidence-explain, and link the themes."),
    ],
))

# ------------------------------------------------------------------ 6. Macbeth language and techniques
LESSONS.append(lesson(
    module=DRAMA,
    topic="Macbeth: language and dramatic techniques",
    title="Macbeth: language, imagery and dramatic techniques",
    slug="lit2-macbeth-language-techniques",
    minutes=24,
    summary="Soliloquy, aside, dramatic irony, foreshadowing, symbols and the imagery of blood, darkness, sleep and clothing in Macbeth, with a method for explaining how a device creates an effect.",
    objectives=[
        "Identify and define soliloquy, aside, dramatic irony, foreshadowing, symbolism and imagery",
        "Name the main image patterns in Macbeth (blood, darkness, sleep, clothes) and say what each suggests",
        "Give an example of each technique from a named scene",
        "Write an answer that links a technique to its effect on the audience",
    ],
    key_concepts=["Soliloquy", "Aside", "Dramatic irony", "Foreshadowing", "Imagery", "Symbol", "Pathetic fallacy"],
    blocks=[
        H("Introduction"),
        T("When your friend tells you a story, you listen to the story, but you also notice how he tells it: his pauses, his voice, his jokes. "
          "A playwright has similar tools. In an exam, it is not enough to say what happens. You must also say how Shakespeare makes it powerful. "
          "That is the topic of this lesson."),
        H("Dramatic devices"),
        D("A **soliloquy** is a speech in which a character, alone on stage, speaks his or her thoughts aloud to the audience.", title="Soliloquy"),
        D("An **aside** is a short remark that the audience hears but other characters on stage are supposed not to hear.", title="Aside"),
        D("**Dramatic irony** is when the audience knows something that a character does not.", title="Dramatic irony"),
        D("**Foreshadowing** is a hint of what will happen later in the story.", title="Foreshadowing"),
        KEY("Where to find them in Macbeth", "Scene references follow common editions; check your text.", cards=[
            ["Soliloquy", "Lady Macbeth calls on spirits to unsex her (Act 1 Scene 5). Macbeth weighs the murder (Act 1 Scene 7), sees the dagger (Act 2 Scene 1) and speaks 'Tomorrow, and tomorrow' on hearing of his wife's death (Act 5)."],
            ["Aside", "Macbeth, after the witches' news of Cawdor (Act 1 Scene 3), and when Malcolm is named heir (Act 1 Scene 4), speaks aside of his hidden thoughts."],
            ["Dramatic irony", "Duncan praises the pleasant look of Macbeth's castle (Act 1 Scene 6) and thanks Lady Macbeth, while the audience knows they plan to kill him."],
            ["Foreshadowing", "The witches' first scene ends with fair is foul and foul is fair. It warns that nothing is what it seems."],
        ]),
        EX("Worked example 1: a soliloquy and its effect", intro="Question: What does the dagger soliloquy (Act 2 Scene 1) show about Macbeth's state of mind?", steps=[
            S("Name the device", text="It is a soliloquy: Macbeth is alone and speaks his thoughts to the audience."),
            S("Say what happens", text="He sees a dagger in the air that seems to lead him to Duncan, and asks whether it is real."),
            S("Say what it shows", text="His imagination is overheated and his mind is troubled by guilt and fear, even before the murder."),
            S("Effect", text="The audience is shown his inner struggle and feels both fear and pity."),
        ]),
        H("Imagery"),
        D("**Imagery** is language that creates pictures or sensations in the mind. A **recurring image** is one that returns again and again and builds meaning.", title="Imagery"),
        D("A **symbol** is an object or image that stands for an idea. The dagger can stand for violent ambition, and blood for guilt.", title="Symbol"),
        KEY("Four image patterns", "", cards=[
            ["Blood", "Starts as a sign of bravery in the battle report, then becomes the sign of guilt that cannot be washed off. Macbeth says he is so far in blood that going back is as hard as going on. Lady Macbeth cannot clean her hands in Act 5."],
            ["Darkness and night", "Crimes happen at night. Macbeth and Lady Macbeth call on night to hide their deeds. Light stands for goodness and truth; Lady Macbeth cannot bear to be without a light in her last days."],
            ["Sleep", "Sleep means peace and innocence. After the murder Macbeth hears a voice that says he has murdered sleep. From then on neither Macbeth nor his wife can rest."],
            ["Clothes", "Macbeth's titles are spoken of as borrowed robes that do not fit him. They show that he is not the natural king."],
        ]),
        T("Other images: the animals (an owl kills a falcon, snakes and birds), the idea that evil things happen in the world of nature, and water that cannot clean the guilty."),
        T("**Pathetic fallacy** is when the weather or nature reflects human feeling. The storm in the opening scene and the unnatural night after Duncan's death reflect disorder in the human world."),
        EX("Worked example 2: blood imagery across the play", intro="Question: Trace the imagery of blood in Macbeth.", steps=[
            S("Beginning", text="The Captain describes the battle: Macbeth is covered in blood for Scotland, a sign of honour."),
            S("Middle", text="After Duncan's murder, Macbeth's hands are covered in blood he cannot wash away. Blood now means guilt."),
            S("Later", text="Banquo's ghost has blood on its head. Macbeth says he has gone so far in blood that there is no way back."),
            S("End", text="Lady Macbeth sees blood on her hands that no one else sees. The image shows that guilt cannot be cleaned."),
        ]),
        H("How to write about a technique"),
        KEY("Name it, show it, explain the effect", "Use three steps in a paragraph.", cards=[
            ["Name", "Say which device it is: soliloquy, aside, irony, imagery."],
            ["Show", "Give the scene and a few words, or describe the action."],
            ["Effect", "Say what the audience feels or understands as a result."],
        ]),
        MISTAKE("Naming the device without the effect", "Writing 'This is dramatic irony' earns little. Add what the audience knows and how it feels, for example tension, pity or fear."),
        MISTAKE("Confusing an aside with a soliloquy", "An aside is short and happens while others are on stage. A soliloquy is longer and is spoken by a character who is alone."),
        QUIZ("Duncan praises Macbeth's castle while the audience knows the Macbeths plan to kill him. This is", [
            "A soliloquy", "Dramatic irony", "An aside", "Pathetic fallacy",
        ], 1, "The audience knows more than Duncan, so it is dramatic irony.", hint="Who knows what?",
             feedback=["Duncan is not alone, so this is not a soliloquy.", "", "No character whispers to the audience here.", "The weather is not mentioned in this passage."]),
        QUIZ("Which image pattern is most linked to guilt that cannot be removed?", [
            "Blood", "Songs", "Feasting", "Animals",
        ], 0, "Blood on the hands is a main image of guilt.", hint="Think of Lady Macbeth's sleepwalking.",
             feedback=["", "Songs are not a main image pattern in Macbeth.", "The feast scene has a ghost but its main image is not feasting.", "Animals do occur but are not the main sign of guilt."]),
        TIP("Exam link: Paper 1 asks you to identify devices, and Paper 2 Section A asks how language and dramatic devices create effects. Always name the device, quote a few words if you are sure, and then explain the effect."),
        PQ("Define a soliloquy and give one example from Macbeth.", "A soliloquy is a speech by a character who is alone, speaking thoughts aloud. Examples: the dagger speech (Act 2 Scene 1) and the 'Tomorrow, and tomorrow' speech (Act 5)."),
        PQ("Explain the effect of the Porter scene.", "It is comic relief after the murder, but the idea of the gate of hell hints that evil is inside Macbeth's castle."),
        PQ("Choose one image pattern and say what it suggests about Macbeth.", "Sleep: after the murder Macbeth hears that he has murdered sleep, which shows that his crime destroys his peace of mind. He and his wife lose rest, which is a sign of guilt."),
        PQ("What is dramatic irony? Give one example of it in Act 1.", "It is when the audience knows more than a character. Example: Duncan praises Macbeth's castle and thanks Lady Macbeth warmly, while the audience knows they are planning his murder."),
        SUM("A soliloquy is a speech by a character alone; an aside is a short remark to the audience.",
            "Dramatic irony and foreshadowing make the audience look ahead and feel tension.",
            "Recurring images in Macbeth: blood, darkness, sleep and clothes.",
            "Pathetic fallacy links weather and disorder.",
            "In answers, name the device, show it and explain the effect."),
    ],
))

# ------------------------------------------------------------------ 7. As You Like It, Acts 1-2
LESSONS.append(lesson(
    module=DRAMA,
    topic="As You Like It: plot and characters",
    title="As You Like It, Acts 1 and 2: court, quarrel and flight",
    slug="lit2-ayli-plot-acts-1-2",
    minutes=22,
    summary="The family quarrels, the wrestling match, Rosalind's banishment and the flight of Rosalind, Celia, Touchstone, Orlando and Adam to the forest of Arden, with the characters met so far.",
    objectives=[
        "Retell the events of Acts 1 and 2 of As You Like It in order",
        "Explain the two family quarrels: Oliver and Orlando, Duke Frederick and Duke Senior",
        "Describe Rosalind, Celia, Orlando, Oliver, Touchstone, Adam and Jaques as they first appear",
        "Say how and why each character reaches the forest of Arden",
    ],
    key_concepts=["Usurper", "Banishment", "Disguise", "Arden", "Foil", "Fool"],
    blocks=[
        H("Introduction"),
        T("Many families have a story of two brothers who do not get along, especially when property and position are involved. "
          "As You Like It starts with such a story, and then moves the characters out of danger into a forest where a different, more playful life is possible. "
          "It is a comedy: problems are serious at first, but the play ends in reconciliation and marriage."),
        T("The Board's 2023 report names As You Like It among the Shakespeare texts of the old syllabus. Questions on love were popular and were answered well; "
          "questions on rescue were less popular. So learn the love stories and also the episodes of rescue."),
        D("A **usurper** is a person who takes a throne or position that belongs to someone else.", title="Usurper"),
        H("The two quarrels"),
        T("The play has two pairs of brothers in conflict. Duke Frederick has taken the dukedom from his older brother, Duke Senior, and driven him into exile in the forest of Arden. "
          "Oliver, the eldest son of the late Sir Rowland de Boys, has taken charge of the family and treats his youngest brother Orlando badly."),
        T("The two quarrels are mirrors. In both, an older and a younger brother are at odds, a wrong is done by the one in power, and in the end the wrongdoer changes. Learn both."),
        H("Act 1"),
        KEY("Act 1 in order", "Scene numbers follow common editions; check your text.", cards=[
            ["Scene 1", "In Oliver's orchard Orlando tells the old servant Adam that Oliver gives him no education and treats him like a servant. They quarrel and Orlando seizes Oliver. Oliver plans to harm Orlando by arranging a wrestling match with Charles, the Duke's wrestler."],
            ["Scene 2", "At Duke Frederick's court Rosalind, the daughter of the banished Duke Senior, is comforted by her cousin Celia, Frederick's daughter. The court fool Touchstone joins them. Orlando wrestles Charles and wins. Rosalind and Orlando fall in love; she gives him a chain."],
            ["Scene 3", "Duke Frederick, suspicious of Rosalind, banishes her. Celia says she will go with her. Rosalind decides to dress as a young man called Ganymede, Celia as a shepherdess called Aliena, and they take Touchstone."],
        ]),
        H("Act 2"),
        KEY("Act 2 in order", "", cards=[
            ["Scene 1", "In the forest of Arden Duke Senior speaks of the sweet uses of adversity, finding good in hardship. A lord reports that the melancholy Jaques wept over a wounded deer."],
            ["Scene 2", "At court Frederick learns that Celia and Rosalind have gone and sends men after them."],
            ["Scene 3", "Adam warns Orlando that Oliver plans to burn his lodging and offers his life savings. They leave together."],
            ["Scene 4", "Rosalind, Celia and Touchstone arrive in Arden, tired and hungry. They meet the shepherds Corin and Silvius and buy a cottage."],
            ["Scene 5", "Amiens sings under the greenwood tree; Jaques adds cynical comments to the song."],
            ["Scene 6", "Orlando carries the weak Adam on his back."],
            ["Scene 7", "Jaques tells of meeting a fool in the forest and gives the speech on the seven ages of man. Orlando bursts in with his sword, demanding food. Duke Senior treats him kindly and welcomes him and Adam."],
        ]),
        IMG("f5lit-2-ayli-journey.svg", alt="Two boxes: the court and Oliver's house on the left, the forest of Arden on the right, with an arrow of flight to Arden in Acts 1 and 2 and an arrow of return in Act 5", caption="Figure 1. The movement of the play: from a hostile court to the forest, and back to order in Act 5."),
        H("The characters so far"),
        KEY("Who is who", "", cards=[
            ["Rosalind", "Clever, witty and brave. She loves Orlando and, disguised as Ganymede, becomes the play's leader."],
            ["Celia", "Rosalind's cousin and loyal friend. She gives up her father's court for the sake of friendship."],
            ["Orlando", "Strong, noble and honest, but with little education. He suffers under Oliver, and becomes a gentle lover in Arden."],
            ["Oliver", "Orlando's elder brother. Jealous and cruel in Act 1, he changes later."],
            ["Touchstone", "The court fool. Witty and practical, he follows Celia and Rosalind to Arden."],
            ["Duke Senior", "The exiled rightful duke. Kind and philosophical, he finds good in the forest."],
            ["Jaques", "A melancholy lord with Duke Senior. He is a cynic who sees the world as foolish."],
            ["Adam", "An old and faithful servant of the de Boys family."],
        ]),
        EX("Worked example 1: why does Rosalind go to Arden?", intro="Question: Explain why Rosalind leaves the court and how she prepares for the journey.", steps=[
            S("Cause", text="Duke Frederick is suspicious of her because she is the daughter of the exiled Duke Senior and is popular, and so he banishes her."),
            S("Celia's response", text="Celia refuses to be parted from her and decides to go with her."),
            S("The plan", text="They agree to disguise themselves for safety: Rosalind as Ganymede and Celia as Aliena. Touchstone goes with them."),
            S("Result", text="The disguise sets up the plot of the play and its comedy."),
        ]),
        EX("Worked example 2: Orlando's trouble with Oliver", intro="Question: Describe the relationship between Orlando and Oliver in Act 1.", steps=[
            S("Orlando's complaint", text="He says Oliver has kept him from a gentleman's education and treats him like a servant."),
            S("The quarrel", text="Orlando seizes Oliver by the throat. Oliver is angry and humiliated."),
            S("Oliver's plan", text="He asks the wrestler Charles to harm Orlando in the match."),
            S("Result", text="Orlando defeats Charles. Later Adam warns him of a new plot and they flee."),
        ]),
        MISTAKE("Mixing up the two dukes and the two Olivers", "Duke Senior is the exiled duke and Duke Frederick is his usurping brother. Oliver is Orlando's elder brother. There is also a clergyman called Sir Oliver Martext in Act 3. Name the full title."),
        MISTAKE("Saying Rosalind is Orlando's cousin", "Rosalind is Celia's cousin. Orlando and Rosalind are not related."),
        QUIZ("Why does Duke Frederick banish Rosalind?", [
            "She wins a wrestling match", "He distrusts her as the daughter of his banished brother", "She asks to leave", "She refuses to marry Oliver",
        ], 1, "Frederick sees Rosalind as a threat because she is Duke Senior's daughter and is liked by the people.", hint="Whose daughter is Rosalind?",
             feedback=["Orlando wins the match, not Rosalind.", "", "She does not choose to leave.", "No marriage to Oliver is planned."]),
        QUIZ("Who offers his savings to help Orlando in Act 2?", [
            "Touchstone", "Corin", "Adam", "Silvius",
        ], 2, "Old Adam offers his savings and goes with Orlando.", hint="He is a faithful old servant.",
             feedback=["Touchstone follows Rosalind and Celia.", "Corin is a shepherd in the forest.", "", "Silvius is a young shepherd in love with Phebe."]),
        TIP("Exam link: As You Like It appears in Paper 1 and in Paper 2, Section A of the old syllabus. The Board's report notes that love was a popular question; learn how Rosalind and Orlando fall in love in Act 1 Scene 2 and how their story develops."),
        PQ("Why does Orlando have to leave Oliver's house?", "Oliver has already treated him badly and plans to harm him. In Act 2 Adam warns Orlando that Oliver intends to destroy him, so he flees with Adam."),
        PQ("List the people who go to Arden with Rosalind, and the names they take.", "Celia goes with her as Aliena and Rosalind as Ganymede; Touchstone the fool goes with them."),
        PQ("What does Duke Senior say about life in the forest in Act 2 Scene 1?", "He finds good in hardship: the cold wind and the forest teach him humility. He says that adversity has its sweet uses."),
        PQ("Compare the two quarrels between brothers in the play.", "Frederick has usurped Senior's dukedom and exiled him; Oliver has deprived his younger brother Orlando of education and tries to kill him. Both are brothers in conflict and both will be resolved in the end."),
        SUM("Act 1: Orlando and Oliver quarrel, Orlando defeats Charles and meets Rosalind, Frederick banishes Rosalind.",
            "Rosalind and Celia disguise themselves as Ganymede and Aliena and go to Arden with Touchstone.",
            "Act 2: Orlando and Adam flee Oliver and join the exiles in the forest.",
            "Two quarrels between brothers mirror each other.",
            "Keep names apart: Duke Senior and Duke Frederick; Oliver and Sir Oliver Martext."),
    ],
))

# ------------------------------------------------------------------ 8. As You Like It, Acts 3-5
LESSONS.append(lesson(
    module=DRAMA,
    topic="As You Like It: plot and characters",
    title="As You Like It, Acts 3 to 5: love in Arden and the happy ending",
    slug="lit2-ayli-plot-acts-3-5",
    minutes=24,
    summary="Rosalind as Ganymede, the love stories of Silvius and Phebe and of Touchstone and Audrey, the rescue of Oliver by Orlando, and the weddings and reconciliations of the last act.",
    objectives=[
        "Retell the main events of Acts 3 to 5 of As You Like It",
        "Explain how Rosalind in disguise tests Orlando's love",
        "Describe the rescue of Oliver and its effect on both brothers",
        "Name the four couples and describe the ending, marking doubtful scene numbers 'check your text'",
    ],
    key_concepts=["Ganymede", "Love-test", "Rescue", "Reconciliation", "Hymen", "Epilogue"],
    blocks=[
        H("Introduction"),
        T("Imagine a friend who tells you she is in love but cannot decide whether her admirer is serious. If she could secretly test him, she would. "
          "That is Rosalind's situation. In the forest of Arden she dresses as a young man and spends many scenes with Orlando, testing and teaching him how to love. "
          "Meanwhile other characters fall in love in different ways."),
        H("Act 3"),
        KEY("Act 3 in order", "Scene numbers vary in a few editions; check your text.", cards=[
            ["Scene 1", "At court, Duke Frederick orders Oliver to find Orlando."],
            ["Scene 2", "Orlando hangs love poems for Rosalind on trees. Touchstone mocks them. Rosalind finds a poem and then meets Orlando, who does not know her. As Ganymede she offers to cure his love by playing Rosalind and making him woo her."],
            ["Scene 3", "Touchstone arranges to marry the goat girl Audrey with the help of Sir Oliver Martext, a vicar. Jaques, who overhears, advises them to be properly married."],
            ["Scene 4", "Rosalind worries that Orlando has not come. Corin offers to show her and Celia the shepherd Silvius and the shepherdess Phebe."],
            ["Scene 5", "The shepherd Silvius loves the shepherdess Phebe, who rejects him. Rosalind, as Ganymede, scolds Phebe, but Phebe falls in love with Ganymede."],
        ]),
        H("Act 4"),
        KEY("Act 4 in order", "", cards=[
            ["Scene 1", "Jaques talks with Rosalind about his melancholy. Orlando arrives an hour late. Rosalind teases him, and in play she has Celia marry them in a mock wedding."],
            ["Scene 2", "The lords sing about the hunting of a deer."],
            ["Scene 3", "Silvius brings Phebe's letter to Ganymede. Oliver arrives, repentant, and tells how Orlando, in the forest, saved him from a lioness while he lay asleep. Rosalind faints when she sees the cloth stained with Orlando's blood and says she was only pretending."],
        ]),
        H("Act 5"),
        KEY("Act 5 in order", "The last scenes are short and closely linked. Check your text for exact numbers.", cards=[
            ["Touchstone and William", "Touchstone drives away a country fellow, William, who loves Audrey."],
            ["Oliver's love", "Oliver tells Orlando that he has fallen in love with Aliena and wants to marry her. Rosalind promises Orlando that she will bring his love to the wedding."],
            ["The wedding", "Rosalind arranges that Phebe will marry Silvius if she cannot marry Ganymede, and that Orlando will marry Rosalind. Hymen, the god of marriage, leads in Rosalind and Celia in their own clothes."],
            ["Four couples", "Rosalind and Orlando, Celia and Oliver, Phebe and Silvius, Touchstone and Audrey."],
            ["News", "Jaques de Boys, the second brother of Oliver and Orlando, tells that Duke Frederick, on the way to attack the forest, met a religious man, repented and gave the dukedom back to Duke Senior."],
            ["Jaques and the epilogue", "The melancholy Jaques decides to join the changed Frederick in his new religious life. Rosalind speaks the epilogue."],
        ]),
        H("Worked examples"),
        EX("Worked example 1: Rosalind and Orlando in the forest", intro="Question: How does Rosalind, disguised as Ganymede, test Orlando's love?", steps=[
            S("The offer", text="She offers to cure him of love by playing Rosalind and making him woo her every day."),
            S("The lessons", text="She teases him and points out his faults as a lover, such as being late. She tests his seriousness."),
            S("The mock wedding", text="In Act 4 Scene 1 she has Celia marry them in play, so that Orlando says the words, while she hides her real love."),
            S("The result", text="Orlando shows that he is sincere. Rosalind learns that his love is real, and in the last act she reveals herself."),
        ]),
        EX("Worked example 2: the rescue of Oliver", intro="Question: Describe the rescue of Oliver in Act 4 Scene 3 and its effect.", steps=[
            S("The danger", text="Oliver is asleep in the forest, and a lioness crouches near him."),
            S("The rescue", text="Orlando finds him. He remembers how cruel Oliver was but chooses to fight the lioness and save him."),
            S("The change", text="Oliver is deeply moved. He asks forgiveness and the brothers are reconciled."),
            S("The effect", text="Oliver then falls in love with Celia (as Aliena), and the quarrel in Act 1 is resolved."),
        ]),
        MISTAKE("Skipping the rescue episodes", "The Board's 2023 report says the question on rescue was less popular and less well done than the question on love. Learn the rescue of Oliver from the lioness and its results, and think about other rescues in the play, such as the welcome Duke Senior gives to Orlando and Adam and Frederick's change of heart."),
        MISTAKE("Mixing up the weddings", "The four couples are Rosalind and Orlando, Celia and Oliver, Phebe and Silvius, and Touchstone and Audrey. Write them down and learn them as a list of four."),
        QUIZ("What does Orlando do when he finds Oliver asleep with a lioness nearby?", [
            "He walks away", "He fights the lioness and saves Oliver", "He calls Rosalind", "He kills Oliver",
        ], 1, "Despite Oliver's cruelty, Orlando saves him, and this reconciles the brothers.", hint="He is generous to his brother.",
             feedback=["Orlando chooses to help.", "", "Rosalind is not present.", "He chooses mercy."]),
        QUIZ("Who falls in love with Rosalind in her disguise as Ganymede?", [
            "Audrey", "Celia", "Phebe", "Adam",
        ], 2, "Phebe falls in love with Ganymede and rejects Silvius.", hint="She is a shepherdess.",
             feedback=["Audrey marries Touchstone.", "Celia marries Oliver.", "", "Adam is an old servant."]),
        TIP("Exam link: both love and rescue appear in the Board's report on this play. Prepare an answer on how Rosalind and Orlando's love develops, one on the rescue, and one on the final reconciliations."),
        PQ("How does Phebe's love story create comedy?", "Phebe rejects the shepherd Silvius who adores her, and falls in love with Ganymede, who is really a woman. This creates a chain of unanswered love in which each person loves the wrong one."),
        PQ("What is the importance of the mock wedding in Act 4 Scene 1?", "Rosalind makes Orlando say wedding words to her disguised as Ganymede, with Celia as the priest. It shows his love and prepares the real weddings."),
        PQ("Name the four couples at the end of the play.", "Rosalind and Orlando; Celia and Oliver; Phebe and Silvius; Touchstone and Audrey."),
        PQ("How are the problems of the play resolved at the end?", "Rosalind reveals herself, and the couples are joined. Oliver reforms after the rescue. Duke Frederick repents and gives back the dukedom to Duke Senior. Everyone returns to order, except Jaques, who goes to join Frederick."),
        SUM("Act 3: Orlando's poems, Rosalind as Ganymede offers a cure, Touchstone and Audrey, Silvius and Phebe.",
            "Act 4: the mock wedding, Oliver's repentance and the rescue.",
            "Act 5: Oliver and Celia fall in love, Rosalind reveals herself, Hymen blesses four weddings.",
            "News that Frederick has repented restores Duke Senior.",
            "The love and rescue topics matter, as the Board's report shows."),
    ],
))

# ------------------------------------------------------------------ 9. As You Like It themes and techniques
LESSONS.append(lesson(
    module=DRAMA,
    topic="As You Like It: themes and techniques",
    title="As You Like It: themes, language and dramatic techniques",
    slug="lit2-ayli-themes-techniques",
    minutes=24,
    summary="Love in its many forms, court and country, disguise and identity, family conflict and forgiveness, and the techniques (songs, wit, prose and verse, dramatic irony, the epilogue) that make the comedy work.",
    objectives=[
        "Explain the main themes of As You Like It: love, court and country, disguise, family conflict and reconciliation",
        "Compare the court with the forest of Arden using evidence from the play",
        "Identify techniques: songs, prose and verse, wit, dramatic irony, soliloquy, foil and the epilogue",
        "Write a point-evidence-explain paragraph on a theme or technique",
    ],
    key_concepts=["Pastoral", "Disguise and identity", "Dramatic irony", "Foil", "Wit", "Reconciliation"],
    blocks=[
        H("Introduction"),
        T("A comedy ends in harmony. But a good comedy takes its time and shows problems first: jealous brothers, banished friends, cold weather and the pain of love. "
          "The themes of As You Like It are these problems and how the play resolves them."),
        T("Remember that the Board's report says questions on love were popular in the 2023 session. A theme question may be about love, but it can also be about rescue, family or disguise, so learn them all."),
        H("Love in many forms"),
        T("Love appears in several kinds and the play compares them. Rosalind and Orlando: love at first sight that grows through testing. "
          "Silvius and Phebe: a lover who adores a woman who scorns him, until she falls for the wrong person. "
          "Touchstone and Audrey: a down-to-earth, comic match. Celia and Oliver: a sudden love after a change of heart."),
        T("Jaques and Touchstone make fun of love, while Rosalind sees it clearly: she knows that love is partly foolish but also real. The play suggests that true love needs sense as well as feeling."),
        EX("Worked example 1: love as a theme", intro="Question: How does Shakespeare show different kinds of love in As You Like It?", steps=[
            S("Name the theme", text="Love is shown in four pairs, which allow comparison."),
            S("Rosalind and Orlando", text="Love at first sight, tested and strengthened in Arden, with Rosalind's wit and common sense."),
            S("Silvius and Phebe", text="One-sided and exaggerated love, which makes fun of the language of pastoral love."),
            S("Touchstone and Audrey", text="A plain, comic love with no romance, which contrasts with the poetry of the others."),
            S("Conclusion", text="The play suggests that love can be wise or foolish, but it ends in harmony."),
        ]),
        H("Court and country"),
        D("**Pastoral** is a style of writing set in the countryside among shepherds, which presents country life as simple and peaceful compared with the court.", title="Pastoral"),
        IMG("f5lit-2-ayli-journey.svg", alt="Court and Oliver's house on one side and the forest of Arden on the other, with arrows for flight and return", caption="Figure 1. Court and forest: danger on one side, freedom and learning on the other."),
        T("At court, Frederick rules by suspicion, and Oliver by jealousy. In Arden Duke Senior finds that adversity has its sweet uses, and people grow honest and kind. "
          "But Arden is not perfect: there is cold wind, hunger, and a shepherd's hard life. Corin is poor and works for a master. The play does not simply say that country life is better; it shows that the forest gives space for people to change."),
        D("**Contrast** is the placing of two things side by side so that their differences stand out. In this play the contrast between court and forest is a way of discussing how to live well.", title="Contrast"),
        H("Disguise and identity"),
        T("Rosalind's disguise as Ganymede gives her freedom to speak openly and to guide Orlando. It also produces **dramatic irony**: the audience knows she is Rosalind, "
          "while Orlando, Phebe and others do not. Phebe's love for Ganymede is funny because the audience knows who is behind the disguise."),
        T("The disguise also adds layers. In Shakespeare's theatre a boy actor played Rosalind, who plays Ganymede, who in the mock wedding plays Rosalind again. Gender and identity are playful."),
        H("Family conflict and forgiveness"),
        T("Frederick wrongs his brother, and Oliver wrongs his. The play shows how a wrong can be forgiven. Orlando saves Oliver from the lioness, and Oliver repents. "
          "Frederick meets a holy man and repents offstage. These changes of heart end the family conflicts. This is the theme of **reconciliation**."),
        KEY("Fortune and nature", "A short exchange between Rosalind and Celia in Act 1 Scene 2 (check your text) discusses whether people are shaped by Fortune or by Nature.", cards=[
            ["Fortune", "Chance and luck, which can raise or lower people without reason, as in the exile and the wrestling match."],
            ["Nature", "Natural qualities such as wit and goodness, which stay when circumstances change."],
        ]),
        H("Techniques"),
        KEY("Main techniques", "", cards=[
            ["Songs", "Amiens and others sing in the forest (for example under the greenwood tree). Songs build the mood and praise simple life."],
            ["Prose and verse", "Rosalind speaks both. Verse is used for serious feeling and prose for wit, teasing and everyday talk. The shift shows the mood."],
            ["Wit and word play", "Rosalind and Touchstone use puns and quick replies. This makes the comedy and shows intelligence."],
            ["Dramatic irony", "The audience knows Ganymede is Rosalind, so every conversation with Orlando has two levels."],
            ["Soliloquy and set speeches", "Jaques's speech on the seven ages of man (Act 2 Scene 7) compares life to a play with many parts."],
            ["Foil", "Jaques's gloom contrasts with Rosalind's joy; Touchstone's practical love contrasts with Silvius's romantic love."],
            ["Epilogue", "Rosalind addresses the audience directly at the end and asks them to enjoy the play."],
        ]),
        EX("Worked example 2: Jaques as a foil", intro="Question: What is the effect of Jaques's melancholy in the play?", steps=[
            S("Describe him", text="Jaques is a melancholy lord who takes pleasure in his sadness and mocks the world."),
            S("Contrast", text="Rosalind is lively and hopeful, and Duke Senior accepts hardship. Jaques's gloom makes them look brighter."),
            S("Speech", text="In his seven ages speech he sees life as a play, which is gloomy but also reminds us of the play's own theatrical world."),
            S("Effect", text="He adds variety and thought to the comedy, and at the end he leaves to join the changed Frederick."),
        ]),
        MISTAKE("Saying Arden is perfect", "Arden is a place of freedom and learning, but it has hardship too. A balanced answer notes both."),
        MISTAKE("Confusing the epilogue with a soliloquy", "The epilogue is a closing speech to the audience after the action. A soliloquy is a character alone with his or her thoughts."),
        QUIZ("Which technique is at work when the audience knows that Ganymede is really Rosalind but Orlando does not?", [
            "Soliloquy", "Dramatic irony", "Epilogue", "Narration",
        ], 1, "The audience knows more than Orlando, which is dramatic irony.", hint="Who knows what?",
             feedback=["A soliloquy is a speech by a character alone.", "", "The epilogue is the closing speech.", "There is no narrator in a play."]),
        QUIZ("What does the contrast between court and forest help the play to discuss?", [
            "How to live well and how people change", "How to wrestle", "How to farm sheep", "How to make shoes",
        ], 0, "The contrast helps the play discuss the values of power and simplicity, and how people change.", hint="Think of the themes, not of the setting alone.",
             feedback=["", "Wrestling is a single event.", "Shepherds are part of the setting only.", "Shoes are not a theme."]),
        TIP("Exam link: the Board's 2023 report says love was a popular question and rescue was less popular. In Paper 2 Section A, write about themes with evidence, and in Paper 1 expect questions on techniques such as songs, disguise and irony."),
        PQ("Explain how disguise creates humour in As You Like It.", "Rosalind disguised as Ganymede teases Orlando and receives Phebe's love, while the audience knows the truth. The gap between what characters know and what the audience knows makes dramatic irony and comedy."),
        PQ("Compare the court and the forest of Arden.", "At court there is jealousy, banishment and danger. In Arden, Duke Senior and his lords live simply, and characters grow wise and kind. But Arden has cold and hunger too."),
        PQ("Give two examples of family conflict being resolved.", "Orlando saves Oliver from the lioness and Oliver repents. Frederick, who meets a holy man, gives back the dukedom to Duke Senior."),
        SUM("Love appears in four pairs and is compared: wise, foolish, plain and sudden.",
            "The court is dangerous and the forest offers freedom and learning, but Arden is not perfect.",
            "Disguise produces dramatic irony and questions about identity.",
            "Family conflict is resolved by forgiveness and repentance.",
            "Techniques: songs, prose and verse, wit, dramatic irony, foil, set speeches and the epilogue."),
    ],
))

# ------------------------------------------------------------------ 10. Reading an African novel
LESSONS.append(lesson(
    module=AFRICAN,
    topic="Reading an African novel",
    title="How to read and study an African novel",
    slug="lit2-reading-an-african-novel",
    minutes=22,
    summary="A practical method for reading a prescribed novel with your own copy: a chapter log, character and conflict notes, placing an extract, and avoiding the mistakes the Board's report describes.",
    objectives=[
        "Use a reading method with a chapter log, character list, conflict log and theme log",
        "Place an extract: who speaks, where, when, what came before and what follows",
        "Explain why answers must stay with the text and not with personal experience",
        "Define key terms: novel, narrator, setting, episode and extract",
    ],
    key_concepts=["Novel", "Narrator", "Setting", "Episode", "Extract", "Chapter log"],
    blocks=[
        H("Introduction"),
        T("A novel is like a long road trip. If you notice nothing on the way, you will not remember where you were. If you note each town, each person you meet and each turn in the road, "
          "you can describe the journey later. Studying a novel for the GCE is the same: you must read it in your own copy and take notes as you go."),
        T("The Board's 2023 report says clearly that candidates should own their individual copies of the texts and read them. It also says that candidates did badly when they "
          "mixed up characters or events, could not say where an account started and ended, or brought in their own experiences instead of the text."),
        D("A **novel** is a long work of fiction in prose. It tells a story through characters, events and setting.", title="Novel"),
        D("A **narrator** is the voice that tells the story. A **setting** is the place and time in which the story happens.", title="Narrator and setting"),
        D("An **episode** is a part of the story that forms a unit, such as a meeting, a journey or a quarrel. An **extract** is a passage taken from the text for a question.", title="Episode and extract"),
        H("Step 1: read with a notebook"),
        T("Read the novel at least twice. On the first reading, enjoy the story and note the main events. On the second reading, look for details: who says what, how the characters change, and where the themes appear."),
        KEY("Four logs to keep", "Make one page for each.", cards=[
            ["Chapter log", "After each chapter write two or three sentences: place, time, who appears, what happens."],
            ["Character list", "For each person: name, role, links to others, traits, and one event that proves each trait."],
            ["Conflict log", "Who is in conflict with whom or what, how it starts, and how it ends or continues."],
            ["Theme log", "When you notice an idea (for example power, tradition, change), write the page or chapter and what it shows."],
        ]),
        CODE("""Chapter log
Chapter / pages : ____
Place and time  : ____
Who appears     : ____
What happens    : ____ (2-3 sentences)
Change or turn  : ____
Words worth keeping (a few): ____""", "text", title="A chapter log template (copy it into your notebook)"),
        H("Step 2: place an extract"),
        T("In Paper 2, many questions give an extract and ask about it. The first job is to place it. Ask five questions: who is speaking, to whom, where and when, what has just happened, and what happens next."),
        T("Here is an **invented passage for practice**. It is not from any prescribed novel."),
        CODE("""The sun was already high when Elder Tamba reached the meeting
house. The men had left their hoes at the door. Nobody spoke
until the kola nut was broken. "The road to the river is closed,"
said Tamba at last, "and the one who closed it has not shown his
face." Mama Eka sat by the wall with her basket of groundnuts and
said nothing, but she looked at the young teacher who stood by the
door, his notebook pressed to his chest.""", "text", title="Invented passage (for practice)"),
        EX("Worked example 1: placing the invented passage", intro="Use the five questions on the invented passage.", steps=[
            S("Who speaks", text="Elder Tamba, an older man with authority, speaks. Mama Eka and the teacher are present but silent."),
            S("To whom, where", text="He speaks to the men gathered in the meeting house of the village."),
            S("When", text="Mid-morning: the sun is high and the men have come from their farms."),
            S("What happened before", text="A road to the river has been closed by someone who is not named (the passage does not say who). The novel would have told us earlier."),
            S("What matters", text="Mama Eka's silent look at the teacher suggests that she suspects him, though the passage does not say so. This is a clue about relationships."),
        ]),
        EX("Worked example 2: a three-sentence summary of an episode", intro="Summarise the invented passage as if it were a chapter.", steps=[
            S("Sentence 1: setting", text="The men of a village meet in the meeting house after the kola nut is broken."),
            S("Sentence 2: problem", text="Elder Tamba announces that the road to the river has been closed by someone who has not come forward."),
            S("Sentence 3: hint", text="A silent glance from Mama Eka towards the young teacher hints at a possible suspect."),
        ]),
        MISTAKE("Bringing in personal experience", "The Board's report notes that in some questions candidates brought in their own experiences, which was irrelevant. "
                "Your own village or family can help you understand a custom, but an answer must be about what happens in the novel."),
        MISTAKE("Mixing up characters and events", "The report says candidates mixed characters or events. Keep a character list with page references and use it before the exam."),
        MISTAKE("Not knowing where an episode starts and ends", "Mark the first sentence and the last sentence of important episodes in your own copy, as in Figure 1."),
        IMG("f5lit-2-novel-episode-map.svg", alt="Five boxes in a row: Before, START, Actions, Outcome and END, for mapping one episode in a novel", caption="Figure 1. A map for any episode: mark where it starts and ends."),
        QUIZ("What is the best first step when you meet an extract in an exam question?", [
            "Write about your own village", "Place it: who speaks, to whom, where, when and what came before", "Copy it out in full", "Skip it",
        ], 1, "Placing the extract shows that you know the text and prepares your answer.", hint="The Board says to stay with the text.",
             feedback=["Personal experience is not what the question asks for.", "", "Copying earns no marks without comment.", "Skipping gives no marks."]),
        QUIZ("Which of these is an episode?", [
            "A single word", "A meeting in which a decision is made", "The title page", "The author's name",
        ], 1, "An episode is a unit of the story, such as a meeting, quarrel or journey.", hint="It is part of the story.",
             feedback=["A word is too small.", "", "The title page is not part of the story.", "The author is not part of the story."]),
        TIP("Exam link: African prose appears in Paper 1 (multiple choice) and in Paper 2, Section B. The Board's report says to own your copy. Practise by placing extracts from your own novel."),
        PQ("List four logs you should keep when studying a novel.", "A chapter log, a character list, a conflict log and a theme log."),
        PQ("Why must answers stay with the text and not personal experience?", "The question tests how well you know the prescribed work. Personal experience is not part of the text, so it earns no marks. The Board's report says candidates lost marks by doing this."),
        PQ("Write a three-sentence summary of an episode in a novel you have read.", "Model: sentence 1 describes the setting, sentence 2 the problem or event, and sentence 3 the result or turn. Use your own copy, names and pages."),
        PQ("What five questions help you to place an extract?", "Who is speaking, to whom, where and when, what has just happened, and what happens next."),
        SUM("Own your copy and read it at least twice, with a notebook.",
            "Keep a chapter log, a character list, a conflict log and a theme log.",
            "Place every extract: speaker, listener, place, time, before and after.",
            "Mark where each important episode starts and ends.",
            "Stay with the text; do not bring in personal experience."),
    ],
))

# ------------------------------------------------------------------ 11. The Crown of Thorns
LESSONS.append(lesson(
    module=AFRICAN,
    topic="The Crown of Thorns",
    title="The Crown of Thorns: a study framework",
    slug="lit2-crown-of-thorns-framework",
    minutes=20,
    summary="A framework for studying Linus T. Asong's The Crown of Thorns with your own copy: what the Board's report says, and templates for the D.O., Chief Nchindia and the council of elders, themes and chapters.",
    objectives=[
        "State what the Board's 2023 report says about the novel's questions",
        "Build a profile of the D.O. from your own copy, with evidence",
        "Build a conflict log of the disagreements between Chief Nchindia and the council of elders",
        "Use a chapter tracker and theme log to prepare for Paper 2 Section B",
    ],
    key_concepts=["The D.O.", "Chief Nchindia", "Council of elders", "Conflict log", "Character profile", "Chapter tracker"],
    blocks=[
        H("Introduction"),
        T("This lesson does not retell the novel. KKEVO Academy does not give a plot summary of The Crown of Thorns, because the Board's report says "
          "students must own the text and read it, and because a summary written by someone else can mislead you. Instead you will receive a framework: "
          "questions to ask and tables to fill in as you read your own copy."),
        T("**Use your own copy of the novel** for every fact, name and page reference in the activities below."),
        H("What the Board's report tells us"),
        KEY("Facts from the 2023 report", "These are the only facts about the novel stated in this lesson.", cards=[
            ["Author and status", "The Crown of Thorns, by Linus T. Asong, is the prescribed African novel of the new syllabus named in the report (Paper 2, Section B)."],
            ["The D.O.", "A question on the D.O., described as one of the main characters, was popular and well answered."],
            ["Chief Nchindia and the elders", "A question asked for instances of disagreement between Chief Nchindia and the council of elders. It was unpopular and poorly answered because candidates found it hard to pick out instances."],
        ]),
        T("The lesson of these two facts is useful. A question on a main character is a question you can prepare for with a character profile. "
          "A question on disagreements needs you to find specific moments in the text, so you need a log with page references."),
        D("**D.O.** normally stands for Divisional Officer (older usage: District Officer), a government officer in charge of an administrative unit. Check in your copy how the novel uses the title and what the D.O. does.", title="D.O."),
        D("A **council of elders** is a group of senior people who advise or check a chief. Check in your copy who sits on it and what powers it has.", title="Council of elders"),
        H("Template 1: profile of the D.O."),
        CODE("""The D.O. : character profile (use your own copy)
Role / position in the story : ____
Where he first appears (page) : ____
Three traits, each with proof:
  Trait 1 : ____   Proof (event, page) : ____
  Trait 2 : ____   Proof (event, page) : ____
  Trait 3 : ____   Proof (event, page) : ____
His relationships (with Chief Nchindia, the elders, others) : ____
Key decisions or actions (page) : ____
How others see him : ____
Does he change? How? : ____""", "text", title="Character profile"),
        H("Template 2: Chief Nchindia and the council of elders"),
        CODE("""Disagreement log (use your own copy)
No. | Page/chapter | What is the issue? | Who says what? | Outcome
1   | ____         | ____               | ____           | ____
2   | ____         | ____               | ____           | ____
3   | ____         | ____               | ____           | ____
Pattern: what does the chief want? What do the elders want?
What does each disagreement reveal about power?""", "text", title="Disagreement log"),
        T("Aim to find at least three instances. For each, record the page, the issue, the positions of both sides and the result. "
          "After that, write one sentence on the pattern: what the log shows about who holds power in the community."),
        H("Template 3: chapter tracker and theme log"),
        CODE("""Chapter tracker
Chapter | Place/time | Main characters | What happens | Theme or issue
1       | ____       | ____            | ____         | ____
2       | ____       | ____            | ____         | ____""", "text", title="Chapter tracker"),
        T("Use the theme log from the previous lesson. Typical areas to watch for are power and leadership, tradition and change, and the relationship between traditional rulers and government officials. "
          "These are prompts for your reading, not statements about the novel: confirm each one with evidence from your own copy."),
        EX("Worked example 1: how to fill the disagreement log (invented example)", intro="Here is a log for an invented chief, Chief Mbeng, who is not in the novel. Use it only to see how an entry is written.", steps=[
            S("Page and issue", text="Page 00, a dispute about who should pay for repairing the village bridge."),
            S("Who says what", text="Chief Mbeng says the villagers must pay; the elders say the chief should use the stored levy."),
            S("Outcome", text="The elders win after other chiefs side with them."),
            S("Pattern sentence", text="Mbeng wants quick control, and the elders want shared decisions."),
        ]),
        EX("Worked example 2: turning a profile into a paragraph (invented)", intro="Use the profile of an invented officer, Mr Ayuk, to write one paragraph.", steps=[
            S("Point", text="Mr Ayuk is firm in carrying out orders."),
            S("Evidence", text="In an invented scene he closes a market that broke a rule, despite the traders' protest."),
            S("Explain", text="The scene shows that he puts the rule before popularity."),
            S("Replace with your text", text="For the real D.O., build the same paragraph from your own notes and pages."),
        ]),
        MISTAKE("Trusting a summary from a friend or a video", "The Board's report advises students to avoid watching literature videos on the texts. Summaries leave out details and can mix up characters, which the report says candidates did."),
        MISTAKE("Giving a general answer about chiefs and elders", "A question on disagreements needs specific instances from the novel, not a general account of how chiefs and elders behave in Cameroon."),
        QUIZ("Why is a disagreement log useful for the question on Chief Nchindia and the elders?", [
            "It lets you find specific instances with page references", "It replaces reading the novel", "It tells you the author's age", "It lets you skip chapters",
        ], 0, "The report says candidates could not pick out instances; a log solves that.", hint="Think about 'specific instances'.",
             feedback=["", "A log supports reading, not replaces it.", "Not relevant.", "You still must read the chapters."]),
        QUIZ("According to the Board's report, which character's question was popular and well answered?", [
            "Chief Nchindia", "The council of elders", "The D.O.", "None of these",
        ], 2, "The question on the D.O. was popular, with a high performance rate.", hint="It was a main character.",
             feedback=["The report mentions Chief Nchindia in the unpopular question on disagreements.", "The council appears in the unpopular question.", "", "The report names the D.O."]),
        TIP("Exam link: The Crown of Thorns is an African prose text for Paper 2, Section B in the new syllabus (with Macbeth, and the Board's other new texts). Ask your teacher which syllabus applies to your class."),
        PQ("Which two facts about the novel does the Board's 2023 report mention?", "That a question on the D.O., a main character, was popular and well answered; and that a question on disagreements between Chief Nchindia and the council of elders was unpopular because candidates could not pick out instances."),
        PQ("Describe how you would prepare an answer on the D.O. using your own copy.", "Fill in a character profile: his role, three traits with proof and page numbers, his relationships, key actions and whether he changes. Then write a point-evidence-explain paragraph for each trait."),
        PQ("Explain how a log helps with a question on disagreements.", "It records each disagreement with page, issue, positions and outcome, so that you can name several instances quickly and also see a pattern."),
        PQ("Why is it unwise to rely on a plot summary written by someone else?", "A summary can leave out details, mix up characters and events, and give wrong page references. The Board advises candidates to read the original text."),
        SUM("Use your own copy: this lesson gives only a framework.",
            "The Board's 2023 report: a question on the D.O. was popular and well answered; a question on disagreements between Chief Nchindia and the council of elders was unpopular.",
            "Build a profile of the D.O. with traits, proof and pages.",
            "Keep a disagreement log with pages, issues, positions and outcomes.",
            "Add a chapter tracker and a theme log, and confirm every prompt with your own text."),
    ],
))

# ------------------------------------------------------------------ 12. The Immortal Seed
LESSONS.append(lesson(
    module=AFRICAN,
    topic="The Immortal Seed",
    title="The Immortal Seed: a study framework",
    slug="lit2-immortal-seed-framework",
    minutes=20,
    summary="A framework for studying Tah Protus's The Immortal Seed with your own copy: what the Board's report says about Assi and about Fon Jiggang and Tebene at the River Juajua, and how to mark where an episode starts and ends.",
    objectives=[
        "State what the Board's 2023 report says about questions on The Immortal Seed",
        "Build a profile of Assi covering traits and the role he or she plays, using your own copy",
        "Mark the start and end of the encounter between Fon Jiggang and Tebene at the River Juajua",
        "Write a clear account of an episode in order, without adding or leaving out parts",
    ],
    key_concepts=["Assi", "Fon Jiggang", "Tebene", "River Juajua", "Episode boundaries", "Character traits and role"],
    blocks=[
        H("Introduction"),
        T("This lesson does not retell The Immortal Seed. The Board's report asks students to own and read the text, so KKEVO Academy gives you a study framework instead: "
          "prompts and templates that you fill in with your own copy. Any detail you write must come from the book itself."),
        T("**Use your own copy of the novel** for every name, event and page reference."),
        H("What the Board's report tells us"),
        KEY("Facts from the 2023 report", "These are the only facts about the novel stated in this lesson.", cards=[
            ["Author and syllabus", "The Immortal Seed, by Tah Protus, appears in the report as the African novel of the old syllabus (Paper 2, Section B). Ask your teacher whether it is on your class's list."],
            ["Assi", "A question on the main character, Assi, asked for character traits and the role played. It was very popular and very well answered."],
            ["Fon Jiggang and Tebene", "A question asked for a detailed account of the encounter between Fon Jiggang and Tebene at the River Juajua. It was unpopular and poorly answered because candidates could not tell where the account started and ended."],
        ]),
        T("These facts suggest two skills to practise. First, describe a main character by traits and by role, with evidence. "
          "Second, recount a particular episode in full, from its first moment to its last, and nothing more."),
        H("Template 1: Assi, traits and role"),
        D("A **character trait** is a quality of a person, such as brave, selfish or loyal. A character's **role** is the job the character does in the story, for example hero, helper or opponent. "
          "A good answer gives both and proves them.", title="Trait and role"),
        CODE("""Assi : character profile (use your own copy)
First appearance (page) : ____
Description / position in the community : ____
Trait 1 : ____   Evidence (event, page) : ____
Trait 2 : ____   Evidence (event, page) : ____
Trait 3 : ____   Evidence (event, page) : ____
Role in the plot : what does Assi do that moves the story? ____
Role in the themes : what idea does Assi stand for? ____
Relationships : ____
Does Assi change? How? ____""", "text", title="Character profile"),
        H("Template 2: mark the episode at the River Juajua"),
        T("The Board's report says candidates could not tell where the account of the encounter started and ended. Use the episode map to fix that in your own copy."),
        IMG("f5lit-2-novel-episode-map.svg", alt="Five boxes in a row: Before, START, Actions, Outcome and END, for mapping one episode in a novel", caption="Figure 1. Use this map for the encounter between Fon Jiggang and Tebene."),
        CODE("""Episode : encounter between Fon Jiggang and Tebene at the River Juajua
Before (what led to it, pages) : ____
START: first sentence/page that begins the encounter : ____
Actions in order:
  1. ____
  2. ____
  3. ____
  4. ____
Outcome (what changed) : ____
END: last sentence/page of the encounter : ____
After (what happens next, so you do not add it to the account) : ____""", "text", title="Episode map for your own copy"),
        T("Why mark the 'before' and 'after'? A common error is to start the account too early (adding events that led up to it) or to carry on too late (adding events that come after). "
          "When you know the first and last pages, you can write only what belongs inside."),
        EX("Worked example 1: the method on an invented episode", intro="Use the method on this invented episode (not from the novel): a young man named Kofi meets the village head at a stream to settle a quarrel over a fishing net.", steps=[
            S("Before", text="Two fishermen argued over a net at the market (this is before the episode: do not include it)."),
            S("START", text="The episode begins when Kofi arrives at the stream at dawn."),
            S("Actions", text="He greets the head, states his side, the head listens, asks a question, and both agree on a compromise."),
            S("Outcome and END", text="The quarrel is settled. The episode ends when they leave the stream."),
            S("After", text="The next chapter begins at the market (do not include)."),
        ]),
        EX("Worked example 2: turning trait notes into a paragraph (invented)", intro="Use the notes on an invented character, Ma Nkeng, to write one paragraph on her trait of generosity.", steps=[
            S("Point", text="Ma Nkeng is generous."),
            S("Evidence", text="In an invented scene, she shares her harvest with a hungry neighbour although she has little."),
            S("Explain", text="The scene proves her trait and shows her role as the helper of the community."),
            S("Replace with your text", text="For Assi, use your own profile with real events and pages."),
        ]),
        MISTAKE("Giving only traits and no role", "The report says the question on Assi asked for traits and the role played. State what the character is like and also what he or she does in the story."),
        MISTAKE("Not knowing where the account starts and ends", "Candidates were not able to determine where the account of the River Juajua encounter began and ended. Fix the first and last pages in your copy before the exam."),
        QUIZ("What did the Board's report say about the question on Assi?", [
            "It was very popular and very well answered", "It was unpopular and poorly answered", "It was not set", "It was set on the poetry paper",
        ], 0, "The question on Assi's traits and role was popular and very well answered.", hint="Think of a main character.",
             feedback=["", "This describes the question on the River Juajua encounter.", "The report records that it was set.", "The novel is in Section B."]),
        QUIZ("Why did candidates do badly on the question about the encounter at the River Juajua?", [
            "They could not tell where the account started and ended", "They disliked the author", "They had no paper", "They answered in French",
        ], 0, "The report says they could not determine the start and end of the account.", hint="It is about boundaries.",
             feedback=["", "This is not mentioned.", "This is not mentioned.", "This is not mentioned."]),
        TIP("Exam link: The Immortal Seed is in the old syllabus in the Board's 2023 report. Paper 2 Section B asks about this type of text. Confirm with your teacher which African novel your class will sit."),
        PQ("Name the author of The Immortal Seed and two characters the Board's report mentions.", "Tah Protus. The report mentions Assi (the main character) and Fon Jiggang and Tebene (who meet at the River Juajua)."),
        PQ("What is the difference between a character trait and a character's role?", "A trait is a quality of the person (brave, selfish). A role is the part the character plays in the story, such as hero, helper or opponent."),
        PQ("Describe how you would prepare to give an account of the River Juajua encounter.", "Find the start and end in your copy, note the before and after, list the actions in order, and record the outcome. Then practise retelling it in your own words, keeping within the first and last pages."),
        PQ("Write the structure of a paragraph proving a trait of Assi.", "Point: Assi is (trait). Evidence: an event or a few words from your copy with page. Explain: how this proves the trait and what role it shows. Fill in from your own notes."),
        SUM("Use your own copy: this lesson is a framework, not a summary.",
            "Board's report: the question on Assi (traits and role) was popular and well answered; the account of Fon Jiggang and Tebene at the River Juajua was poorly answered because candidates could not tell where it started and ended.",
            "Profile Assi by traits, role, evidence and pages.",
            "Mark START and END of the River Juajua encounter and the actions in order.",
            "Keep out events that come before or after the episode."),
    ],
))

# ------------------------------------------------------------------ 13. Narrative technique and style
LESSONS.append(lesson(
    module=AFRICAN,
    topic="Narrative technique and style",
    title="Narrative technique and style in the African novel",
    slug="lit2-narrative-technique-style",
    minutes=22,
    summary="Narrator and point of view, structure and flashback, dialogue, proverbs and oral-tradition style, imagery, irony and tone, explained with invented passages and a method for writing about style.",
    objectives=[
        "Identify the narrator and point of view in a passage",
        "Recognise structure devices such as flashback and foreshadowing",
        "Explain how proverbs, dialogue and imagery create style and meaning",
        "Write a short paragraph on a technique and its effect, using a passage from your own text",
    ],
    key_concepts=["Narrator", "Point of view", "Flashback", "Proverb", "Dialogue", "Irony", "Tone"],
    blocks=[
        H("Introduction"),
        T("When an elder tells a story under a tree, the way he tells it matters as much as the story: his voice, a proverb at the right moment, a pause before the ending. "
          "Many African novels use similar methods, put into writing. This lesson helps you to name those methods and explain what they do. "
          "All examples are invented for practice and are not taken from the prescribed novels."),
        H("Narrator and point of view"),
        D("**Point of view** is the position from which the story is told. In **first-person** narration the narrator is a character and says 'I'. In **third-person** narration the narrator stands outside and says 'he', 'she' or 'they'.", title="Point of view"),
        D("An **omniscient** narrator (all-knowing) can enter the minds of many characters. A **limited** narrator follows one character and shows only what he or she knows.", title="Omniscient and limited"),
        KEY("Spot the point of view", "Invented sentences for practice.", cards=[
            ["First person", "'I did not tell my mother where I had been.' The narrator is a character; we know only what he or she tells."],
            ["Third person, limited", "'Ebot did not tell his mother where he had been.' We follow Ebot and share his view."],
            ["Third person, omniscient", "'Ebot hid the truth, and his mother, who guessed it, said nothing.' The narrator knows both minds."],
        ]),
        T("Ask what the choice of narrator does. A first-person narrator can feel close and honest, but may be unreliable. An omniscient narrator can compare many views and comment on them."),
        H("Structure"),
        D("A **flashback** is a part of the story that goes back to earlier events. **Foreshadowing** is a hint of events to come. **Chronological order** follows time from start to end.", title="Structure terms"),
        T("Some novels follow a straight line from beginning to end. Others move back and forth. A narrator may stop to tell the history of a village or a family before returning to the present. "
          "When you study structure, note where the story jumps in time and why."),
        H("Style: proverbs, dialogue, imagery and tone"),
        D("A **proverb** is a short, traditional saying that states a general truth. In oral cultures proverbs are valued as wisdom, and in novels they show a character's culture and good speech.", title="Proverb"),
        D("**Dialogue** is the conversation between characters. It reveals character, moves the plot and shows status (who may speak first, who interrupts).", title="Dialogue"),
        D("**Imagery** is language that creates pictures. **Irony** is a contrast between what is said or expected and what is meant or happens. **Tone** is the writer's attitude, such as serious, humorous or critical.", title="Imagery, irony and tone"),
        T("Here is an **invented passage for practice**."),
        CODE("""Old Mbeng liked to say that a river does not forget its source.
On the day the new road reached the village, he sat on his
stool and watched the lorries pass. "A fast road is a fine
thing," he told the children, "but it carries away whatever
is not tied down." Then he laughed, and went back to cracking
his groundnuts, and nobody could tell whether he was joking.""", "text", title="Invented passage (for practice)"),
        EX("Worked example 1: analysing the invented passage", intro="Question: Comment on the narrator, the proverbs and the tone of the passage.", steps=[
            S("Narrator", text="The narrator is third person: he says 'Old Mbeng' and describes him from outside. The narrator does not enter Mbeng's mind: the last line says nobody could tell whether he was joking."),
            S("Proverbs and sayings", text="Mbeng uses sayings (the river and the source; the fast road that carries away what is not tied down). They show an elder's wisdom and a worry about change."),
            S("Imagery", text="The road that carries things away is an image of change that takes away old values."),
            S("Tone", text="The tone is gentle and humorous on the surface, but there is a note of warning. This is a sort of irony: laughter hides a serious message."),
        ]),
        EX("Worked example 2: writing a technique paragraph", intro="Question: How does the writer use proverbs in the invented passage? Write one paragraph.", steps=[
            S("Point", text="Proverbs show Mbeng's role as an elder and express a theme."),
            S("Evidence", text="He says that a fast road carries away what is not tied down."),
            S("Explain", text="The saying suggests that progress can damage tradition. It gives the theme of change without a long explanation."),
            S("Effect", text="The reader feels both respect for the elder and concern for the village."),
        ]),
        MISTAKE("Naming a technique without its effect", "Saying 'the writer uses a proverb' earns little. Say what the proverb shows about the character, the culture or the theme."),
        MISTAKE("Confusing the narrator with the author", "The narrator is the voice inside the book. Do not say 'the author says' when you mean the narrator or a character."),
        QUIZ("'Ebot hid the truth, and his mother, who guessed it, said nothing.' What point of view is this?", [
            "First person", "Third person, omniscient", "Second person", "Not a story",
        ], 1, "The narrator knows what both Ebot and his mother think.", hint="Whose thoughts do we hear?",
             feedback=["There is no 'I'.", "", "There is no 'you'.", "It is narration of events."]),
        QUIZ("What is a flashback?", [
            "A hint of what will happen later", "A part of the story that goes back to earlier events", "A speech by a character alone", "A comic scene",
        ], 1, "A flashback is a return to an earlier time.", hint="Flash back means to go back.",
             feedback=["That is foreshadowing.", "", "That is a soliloquy (in plays).", "Humour is not what the word means."]),
        TIP("Exam link: Paper 1 tests devices such as point of view, flashback and proverbs; Paper 2 Section B may ask about style. For each device in your own novel, record one example with the page and its effect."),
        PQ("Define first-person and third-person narration with a short example of each.", "In first person the narrator is a character who says 'I', for example 'I went to the market'. In third person the narrator stands outside and says 'he' or 'she', for example 'She went to the market'."),
        PQ("Why do writers use proverbs in African novels?", "Proverbs show a culture's wisdom, mark the speech of elders and others, and express themes briefly and memorably."),
        PQ("Explain the effect of a flashback in a novel.", "It gives background, explains a character's present behaviour, and can build suspense or sympathy."),
        PQ("Use the three-step method (name, show, effect) on a device from your own prescribed novel.", "Model: name the device (for example, a proverb); show it with the page and a few words; explain what it reveals about the character or theme. Use your own copy."),
        SUM("Point of view: first person, third person limited or omniscient; each changes what we know.",
            "Structure: chronological order, flashback and foreshadowing.",
            "Style: proverbs, dialogue, imagery, irony and tone.",
            "Always link a technique to its effect.",
            "Use your own novel's pages for examples."),
    ],
))

# ------------------------------------------------------------------ 14. Cultural and post-colonial themes
LESSONS.append(lesson(
    module=AFRICAN,
    topic="Cultural and post-colonial themes",
    title="Cultural and post-colonial themes in African fiction",
    slug="lit2-cultural-postcolonial-themes",
    minutes=22,
    summary="Tradition and change, authority and leadership, colonial rule and its effects, identity and language: how to recognise these themes in an African novel and write about them with evidence from your own text.",
    objectives=[
        "Define culture, tradition, colonialism and post-colonial",
        "Recognise themes of tradition and change, authority, justice and identity in a passage",
        "Use a theme log with questions to find evidence in your own prescribed novel",
        "Write a balanced point-evidence-explain paragraph on a cultural theme",
    ],
    key_concepts=["Culture", "Tradition and change", "Colonialism", "Post-colonial", "Authority", "Identity"],
    blocks=[
        H("Introduction"),
        T("Think of a family where grandparents speak one language at home, the parents use another at work, and the children use a third with friends. "
          "Each generation keeps something and changes something. Many African novels are about this meeting of old and new, and about the effects of foreign rule. "
          "This lesson gives you the terms and a method. It does not tell you what happens in your prescribed novel: you will find that in your own copy."),
        D("**Culture** is the shared way of life of a group: language, customs, beliefs, food, dress, music and ways of settling disputes.", title="Culture"),
        D("**Tradition** is a custom or belief passed from one generation to the next.", title="Tradition"),
        D("**Colonialism** is the control of one territory by another state, which brings its own government, laws and language. **Post-colonial** describes the period after colonial rule and the writing that deals with its effects.", title="Colonialism and post-colonial"),
        H("Common themes"),
        KEY("Themes to look for", "These are prompts for reading. Confirm each one in your own text.", cards=[
            ["Tradition and change", "How do characters hold on to customs, and how do they change? What is gained and what is lost?"],
            ["Authority and leadership", "Who has power: chiefs, elders, officials, teachers, heads of families? How do they use it, and who checks them?"],
            ["Justice and law", "How are disputes settled: by custom, by elders, by government officers? Are the results fair?"],
            ["Identity and language", "Which languages do characters use, and with whom? Who feels divided between worlds?"],
            ["Colonial and foreign influence", "Where does the novel show the effects of foreign rule: in offices, schools, courts, trade or religion?"],
            ["Community and the individual", "When do duties to the community clash with a person's own wishes?"],
        ]),
        T("A good novel rarely says that one side is simply right. A balanced answer shows what the novel presents as strong or wise in tradition, what it shows as harmful, and the same for the new ways."),
        H("Reading an invented passage"),
        CODE("""The District Office stood at the end of the new road, its roof
shining like a coin. Inside, Mr Fuh signed papers in English that
the elders in the waiting room could not read. Old Chief Tamba sat
very straight on the bench, his cap on his knee. When his name was
called, he answered in his own language, and the clerk, who knew
it well, answered back in English.""", "text", title="Invented passage (for practice)"),
        EX("Worked example 1: identifying themes in the invented passage", intro="Question: Which cultural themes does the passage suggest? Give evidence.", steps=[
            S("Authority", text="An office with paperwork and an officer stands next to an old chief. Two kinds of authority meet."),
            S("Language", text="The papers are in English, but the chief answers in his own language. The clerk knows the chief's language, but replies in English. This shows language as a sign of power and of distance."),
            S("Tradition and change", text="The chief sits straight with his cap on his knee, a picture of dignity in an unfamiliar place."),
            S("Balanced conclusion", text="The passage does not say the office is bad or good. It shows the difficulty of two systems meeting."),
        ]),
        EX("Worked example 2: a point-evidence-explain paragraph", intro="Write one paragraph on language and power in the invented passage.", steps=[
            S("Point", text="Language shows who holds power in the District Office."),
            S("Evidence", text="The papers are in English, which the elders cannot read, while the chief answers in his own language and the clerk replies in English."),
            S("Explain", text="The elders depend on others to understand what is decided about them. This suggests that the new system gives more power to those who command its language."),
            S("Link", text="This is a theme of authority and identity in a post-colonial setting."),
        ]),
        H("A method for your own novel"),
        CODE("""Theme log (use your own copy)
Theme              | Page/chapter | What happens or is said | What it shows
Tradition/change   | ____         | ____                    | ____
Authority          | ____         | ____                    | ____
Justice/law        | ____         | ____                    | ____
Identity/language  | ____         | ____                    | ____
Foreign influence  | ____         | ____                    | ____
One-sentence balance: what does the novel present as good
and as harmful in each way of life?""", "text", title="Theme log with questions"),
        MISTAKE("Giving a lecture on history instead of using the novel", "The Board's report warns that candidates lose marks when they bring in personal experience instead of the text. Use the history of colonialism only to explain a term, then go back to the novel."),
        MISTAKE("Writing one-sided answers", "Saying 'tradition is good and change is bad' (or the opposite) without evidence is weak. Show both sides as the novel shows them."),
        QUIZ("Which of these is the best definition of tradition?", [
            "A new law made this year", "A custom or belief passed from one generation to the next", "A kind of road", "A type of book",
        ], 1, "Tradition is passed on over generations.", hint="Think of grandparents and customs.",
             feedback=["A new law is not passed on over generations.", "", "A road is not a custom.", "A book is not a tradition."]),
        QUIZ("A passage shows an elder speaking his own language to an officer who replies in English. Which theme does this most suggest?", [
            "Language and power", "A hunting story", "Weather", "Food",
        ], 0, "The choice of language shows differences of power and identity.", hint="Which language belongs to whom?",
             feedback=["", "No hunting is described.", "No weather is described.", "No food is described."]),
        TIP("Exam link: themes in the African novel are tested in Paper 2 Section B and in Paper 1. The Board's report shows that candidates who stay with the text score best. Pick a few themes and prepare evidence with page references."),
        PQ("Define colonialism and post-colonial.", "Colonialism is the control of a territory by another state, which brings its own laws, government and language. Post-colonial describes the period after colonial rule and writing that deals with its effects."),
        PQ("Give two questions you could ask of a novel to find the theme of authority.", "Who holds power (chiefs, elders, officers, heads of families) and how do they use it? Who checks them, and what happens when they disagree?"),
        PQ("Why is it better to show both sides of a theme such as tradition and change?", "Novels usually show good and bad in both. A balanced answer reflects the novel and earns more credit than a one-sided opinion."),
        PQ("Write a three-line plan for a paragraph on identity and language in your own prescribed novel.", "Point: language shows a character's identity. Evidence: a scene from your copy, with page, where a character chooses a language. Explain: what the choice reveals about belonging or power."),
        SUM("Culture is a shared way of life; tradition is passed on; colonialism is foreign control; post-colonial deals with its aftermath.",
            "Look for tradition and change, authority, justice, identity and language, and foreign influence.",
            "Balance: show what the novel presents as strong and weak in each way of life.",
            "Use a theme log with page references from your own copy.",
            "Use history only to explain a term, then return to the text."),
    ],
))
