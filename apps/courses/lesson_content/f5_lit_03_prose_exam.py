"""Form 5 Literature in English (O Level 0535): Non-African Prose Fiction (Lord of the Flies, Silas Marner) and Examination.

Draft content. Exam facts are only those of the Board's 2023 Ordinary Level report: Paper 1 is 50 multiple-choice questions;
Paper 2 has four sections (A Drama, B African literature, C Poetry, D Prose) with two questions in each. The report names
the texts of the new syllabus (Macbeth, The Crown of Thorns, a modern anthology, Lord of the Flies) and of the old one
(As You Like It, The Immortal Seed, a Cameroon anthology, Silas Marner). No mark splits are stated.
Plot, character and theme statements for Lord of the Flies (William Golding, 1954) and Silas Marner (George Eliot, 1861) are
paraphrased general knowledge; chapter numbers are given only where well established and are marked "check your text" when
editions may differ. No passage is quoted except a few words of titles. The student must use their own copy of each book.
"""

import itertools

from .dsl import *  # noqa: F403

COURSE = ("literature-in-english", "form-5")

M_PROSE = "Non-African Prose Fiction"
M_EXAM = "Examination"

_POS = itertools.cycle([1, 3, 0, 2, 2, 0, 3, 1])


def qz(question, right, wrongs, explanation, hint=""):
    """QUIZ helper: `wrongs` is a list of (text, why) pairs; the correct choice goes to a rotating position."""
    pos = next(_POS)
    choices = [w[0] for w in wrongs]
    feedback = [w[1] for w in wrongs]
    choices.insert(pos, right)
    feedback.insert(pos, "")
    return QUIZ(question, choices, pos, explanation, hint=hint, feedback=feedback)


LESSONS = [
    # ------------------------------------------------------------------ 1. Lord of the Flies: plot 1
    lesson(
        module=M_PROSE, topic="Lord of the Flies: plot and setting",
        title="Lord of the Flies: the island and chapters 1 to 6",
        slug="lit3-lotf-plot-one",
        minutes=24,
        summary="The setting of William Golding's Lord of the Flies and the story from the plane crash to the fear of the beast: "
                "the conch, Ralph's election, the signal fire, the missed ship and the first deaths of order.",
        objectives=[
            "Describe the setting of the novel and why it matters to the story",
            "Retell the events of chapters 1 to 6 in the right order",
            "Explain how the conch and the signal fire show the boys' hopes for order and rescue",
            "Keep events apart and avoid mixing up one episode with another",
        ],
        key_concepts=["Setting", "Plot", "Conch", "Signal fire", "Assembly", "The beast"],
        blocks=[
            H("Introduction"),
            T("Imagine a school trip where the bus breaks down far from any town, there is no phone signal, and every teacher "
              "is gone. Who leads? Who decides the rules? Who makes the fire? William Golding asks this question in an extreme form "
              "in his novel *Lord of the Flies* (1954). A group of British schoolboys are alone on an island with no adults at all.\n\n"
              "This lesson gives you the setting and the first half of the story. The next lesson gives the second half. "
              "Read your own copy of the book beside these notes: the Board's report says that candidates should own the text."),
            D("The **plot** is the chain of events in a story, told in an order that makes one event cause the next. "
              "The **setting** is the place and the time in which the story happens.", title="Definitions"),
            H("The setting"),
            KEY("Where and when", "The novel is set during an imagined atomic war. A plane carrying British boys, away from "
                "danger at home, is shot down or crashes. It falls on an uninhabited tropical island in the Pacific. The pilot is dead "
                "and the boys, aged about six to twelve, are alone.", cards=[
                ["The island", "Shaped roughly like a boat: a beach and lagoon, a coral reef, thick jungle, a mountain, and a rocky end called Castle Rock."],
                ["The scar", "The path of broken trees left by the crashed plane. It marks the place where the adult world landed on the island."],
                ["The time", "Not stated exactly. It is the time of war, so the 'safe' adult world is also violent."],
            ]),
            T("The island is first described as a beautiful place with food, water and warmth. It looks like paradise, so the story "
              "is also about how a paradise is spoilt. The setting is important for two reasons. First, there are no adults to "
              "make rules. Second, the island is small: the boys cannot escape from one another or from their own fears."),
            IMG("f5lit-3-lotf-descent.svg", alt="A diagram of the story of Lord of the Flies as six stages going from order to savagery, with the chapters for each stage.",
                caption="Figure 1. The story moves from order (the conch) to savagery (the hunt). The chapters are given as a guide: check your edition."),
            H("Chapters 1 to 3: order begins"),
            T("**Chapter 1 (The Sound of the Shell).** Ralph, a fair boy of about twelve, climbs out of the wreck and meets Piggy, "
              "a fat, short-sighted boy with asthma. Piggy asks Ralph not to tell the others his nickname, but Ralph does. Ralph "
              "sees a shell in the lagoon, Piggy knows it is a conch and tells him how to use it, and Ralph blows it. The boys come together. Last come the choirboys, "
              "marching in two lines and led by Jack Merridew. A vote is held and Ralph is elected chief. Jack is angry but "
              "is given command of the choir, who will be the hunters. Ralph, Jack and Simon explore and climb the mountain. "
              "Jack raises his knife over a trapped piglet but cannot bring himself to kill it."),
            T("**Chapter 2 (Fire on the Mountain).** At an assembly, Ralph sets the rule that only the boy holding the conch may speak. "
              "A small boy with a birthmark on his face says he saw a 'snake-thing' in the dark, and the older boys laugh it away: the "
              "fear of a beast is born. Ralph proposes a signal fire so that passing ships can see them. Piggy's glasses are used "
              "to focus the sun and start it. The dry wood catches and the fire runs wild across the mountain. Later, the boy with the birthmark "
              "is not seen again. The reader understands that he has been burnt."),
            T("**Chapter 3 (Huts on the Beach).** Jack is learning to hunt and thinks only of killing a pig. Ralph tries to build shelters, "
              "but the boys drift away to play. Only Simon helps him. Simon also helps the small boys reach fruit, then walks "
              "alone into a quiet green clearing in the jungle. Ralph and Jack quarrel for the first time: one wants safety and rescue, "
              "the other wants meat and the thrill of the hunt."),
            H("Chapters 4 to 6: the first cracks"),
            T("**Chapter 4 (Painted Faces and Long Hair).** The small boys play on the beach. Roger throws stones at Henry, but "
              "deliberately misses: the old rules of the adult world still hold him back, for the moment. A ship passes on the horizon. "
              "The signal fire is out, because Jack and the hunters have left it to hunt. Ralph is furious. The hunters come back with a dead pig "
              "and are happy. Piggy criticises them, and Jack hits him, breaking one lens of his glasses. Jack, with a painted face, "
              "has found that a mask frees him from shame."),
            T("**Chapter 5 (Beast from Water).** Ralph calls an assembly. He says the boys are not living by the rules, "
              "the fire is neglected and fear is spreading. The littluns say they are afraid of the dark and of a beast. "
              "Simon suggests that the beast may just be something in themselves, but nobody understands. Jack leaves the meeting. "
              "Ralph wishes that grown-ups would come.\n\n"
              "**Chapter 6 (Beast from Air).** During the night, a dead parachutist drifts down onto the mountain top. Sam and Eric, on "
              "fire duty, see the shape move in the wind and run away in terror. The boys now believe a real beast lives on the mountain. Ralph, Jack "
              "and Roger decide to go and see."),
            TIP("A good summary keeps events in order. Learn the chapter groups: 1 to 3 order is set up, 4 to 6 order starts to break, "
                "7 to 9 fear and the first killings, 10 to 12 the end of the civilised group and the rescue. Chapter numbers can differ "
                "slightly between editions: check your text."),
            H("Worked model answers"),
            EX("How does Ralph become leader?", intro="Write a plan for an answer to: 'How does Ralph become the leader of the boys, "
               "and what challenge does he face from the start?'", steps=[
                S("Point 1", text="Ralph meets Piggy and blows the conch, which gathers the boys: the conch gives him a voice and a position."),
                S("Point 2", text="At the first assembly the boys vote and choose Ralph. They choose him because of his size, his looks "
                  "and, above all, because he holds the conch, the symbol of order."),
                S("Point 3", text="Jack is the challenger. He wanted to be chief because he leads the choir. Ralph gives him the hunters as a "
                  "compromise, but the two will keep opposing each other."),
                S("Point 4", text="Conclude: Ralph is elected, which shows the boys' wish for order, but his leadership depends on the shell and on the "
                  "boys' agreement, not on force."),
            ]),
            EX("Why does the first ship not rescue the boys?", intro="Plan an answer to: 'Explain how the boys fail to be rescued by the first "
               "ship that passes the island.'", steps=[
                S("Set the scene", text="Ralph has made the fire the first priority so that passing ships will see the smoke."),
                S("The cause", text="Jack and the hunters leave the fire to go hunting. They let the fire go out, leaving it unwatched. The ship passes on the horizon."),
                S("The result", text="Ralph is furious. Jack is pleased with his kill. Piggy complains and gets hit, and one lens of his glasses is broken."),
                S("Conclude", text="The episode shows that hunting (meat, excitement) is replacing the boys' hope of rescue."),
            ]),
            MISTAKE("Mixing up the beast episodes", "Chapter 2 gives the first rumour of a beast (the 'snake-thing'). Chapter 5 is the "
                    "assembly about the beast 'from water'. Chapter 6 is the real dead parachutist, 'from air'. The Board's report says that "
                    "candidates mixed up events in questions on a play, so always check which scene or chapter the question names."),
            MISTAKE("Retelling from films or videos", "The report asks candidates to read the original book and not to rely on videos. "
                    "A film leaves out or changes details, and an answer using them will not match the text."),
            qz("Who finds and blows the conch in chapter 1?",
               "Ralph sees it in the lagoon, Piggy knows what it is, and Ralph blows it",
               [("Jack finds it and blows it for the choir", "Jack arrives later with the choir and hears the conch; he does not find or blow it."),
                ("Simon finds it near the mountain", "Simon is the quiet boy who helps the littluns and goes to the clearing; he does not find the conch."),
                ("Roger finds it on the beach", "Roger is a choirboy who appears later; he is not linked to the conch's discovery.")],
               "Ralph finds the shell and Piggy tells him it is a conch; Ralph blows it and so calls the boys together. (Check your text for the small details.)",
               hint="Think of the two boys who meet first."),
            qz("Why does the first ship pass without rescuing the boys?",
               "The signal fire has gone out because the hunters left it",
               [("The ship cannot see the island in the mist", "There is no mist in the story; the problem is that no smoke is rising."),
                ("Ralph refuses to light the fire", "Ralph is the one who wants the fire: he is angry when it is out."),
                ("The boys hide from the ship", "They want to be rescued; nobody hides.")],
               "The fire is Ralph's way of calling for rescue. When the hunters leave it unattended, the smoke stops and the ship does not notice them.",
               hint="Think about what the hunters were doing instead."),
            PQ("Where is the story set, and how does the setting help the story?",
               "A small, uninhabited tropical island in the Pacific, after a plane carrying British boys crashes during an atomic war. "
               "There are no adults, so the boys must make their own rules. The island is small, so the boys cannot escape each other. "
               "It looks like a paradise at first, which makes its later fall into violence more shocking."),
            PQ("Describe the main events of chapter 1 in order.",
               "Ralph and Piggy meet after the crash. They find the conch and Ralph blows it. The boys gather, and the choir arrives led by Jack. "
               "A vote makes Ralph chief and Jack is given charge of the hunters. Ralph, Jack and Simon explore the island and climb the mountain, "
               "and Jack fails to kill a piglet. (Check your text for the order of the smaller details.)"),
            PQ("What does the loss of the boy with the birthmark in chapter 2 show?",
               "The signal fire gets out of control because the boys are careless, and the small boy who first spoke of a beast is lost. "
               "It shows that the boys' lack of discipline has real and deadly results, and that the first death is covered by nobody's responsibility."),
            SUM("Lord of the Flies is set on an uninhabited Pacific island after a plane crash in a time of atomic war.",
                "The conch brings the boys together, Ralph is elected chief, and Jack leads the hunters.",
                "The signal fire stands for rescue; the boys let it burn out and a ship passes by.",
                "Fear of a beast grows from chapter 2 to chapter 6, when a dead parachutist lands on the mountain.",
                "Keep events in order and use your own copy of the book, not a film."),
        ],
    ),

    # ------------------------------------------------------------------ 2. Lord of the Flies: plot 2
    lesson(
        module=M_PROSE, topic="Lord of the Flies: plot and setting",
        title="Lord of the Flies: chapters 7 to 12 and the rescue",
        slug="lit3-lotf-plot-two",
        minutes=24,
        summary="The second half of Lord of the Flies: the hunt for the beast, Jack's tribe, the killing of Simon and then Piggy, "
                "the manhunt for Ralph and the naval officer who ends it.",
        objectives=[
            "Retell chapters 7 to 12 in order",
            "Explain how Jack's tribe separates from Ralph's group",
            "Describe the deaths of Simon and Piggy and what each shows",
            "Explain how the rescue happens and why its irony matters",
        ],
        key_concepts=["Tribe", "Lord of the Flies (the pig's head)", "Castle Rock", "Rescue", "Irony", "Climax"],
        blocks=[
            H("Introduction"),
            T("In the first half of the book, the boys lose their fire and their calm. In the second half they lose their "
              "innocence. The Board's report records that in a question about the island, many candidates could not show how the "
              "boys' difficulties on the island were overcome. To answer well you need to know the second half in order, "
              "including the ending. This lesson goes through it."),
            D("The **climax** is the high point of a story, where the conflict is strongest. In *Lord of the Flies* the death of Piggy "
              "and the shattering of the conch are usually seen as the climax; the rescue in the last chapter is the resolution.",
              title="Definition"),
            H("Chapters 7 to 9: fear and the first killing"),
            T("**Chapter 7 (Shadows and Tall Trees).** Ralph, Jack and Roger climb to look for the beast. On the way, the boys hunt a wild boar, "
              "and in a game Robert plays the pig and is badly hurt by the others. Ralph feels the excitement too. Climbing the mountain top "
              "in the dark, they see the great shape, think it is the beast, and run.\n\n"
              "**Chapter 8 (Gift for the Darkness).** Jack tries to remove Ralph as chief. When the boys do not agree, he walks out and "
              "goes to Castle Rock to set up a new tribe. Many boys follow him, drawn by meat and by fear. The hunters kill a sow, cut off its head "
              "and leave it on a sharpened stick as an offering to the beast. Simon, alone in his clearing, sees the head buzzing with flies. "
              "In his mind it speaks to him, saying that the beast is part of the boys. This is the Lord of the Flies of the title (the name "
              "is a translation of Beelzebub, a name for the devil)."),
            T("**Chapter 9 (A View to a Death).** Simon climbs the mountain and finds the truth: the beast is only a dead airman tangled in his parachute. "
              "He frees the body and runs down to tell the others. Meanwhile Jack's tribe is holding a feast and a ritual dance on the beach "
              "in a storm. Ralph and Piggy, who have gone to the feast, are on the edge. Simon staggers out of the forest. The boys, "
              "in the frenzy of the dance, take him for the beast and kill him. Ralph and Piggy have joined in the circle. "
              "The wind then carries the dead airman out to sea."),
            H("Chapters 10 to 12: the end of order"),
            T("**Chapter 10 (The Shell and the Glasses).** Ralph's group is now only Ralph, Piggy, Sam and Eric (called Samneric). "
              "They try to pretend that Simon's death was an accident. Jack's hunters raid their camp at night and take Piggy's glasses, "
              "the only way to make fire. Piggy can hardly see, and the group has lost its only means of lighting a signal fire.\n\n"
              "**Chapter 11 (Castle Rock).** Ralph, Piggy, Sam and Eric go to Castle Rock to demand the glasses. Piggy holds the conch and "
              "tries to speak sense. Roger, standing above, pushes a boulder. It hits Piggy, who falls to his death, and the conch is smashed. "
              "Ralph escapes. Sam and Eric are seized and forced to join Jack's tribe."),
            T("**Chapter 12 (Cry of the Hunters).** Ralph is alone and hunted. Jack's tribe sharpens a stick to a point at both ends and "
              "wants Ralph's head. They set the island on fire to drive him out. Ralph runs through the burning forest and falls on the beach. "
              "He looks up and sees a naval officer: a ship has seen the smoke. The boys stop. The officer is amazed to find British boys "
              "so wild, and he expects to hear of fun and games. Ralph weeps for the loss of innocence, for the darkness in people, and "
              "for the death of his friend Piggy. The adult world has come, but the officer's ship is a warship in a war."),
            IMG("f5lit-3-lotf-descent.svg", alt="The six stages of the story from order to savagery with the chapters for each stage.",
                caption="Figure 1 again. Stages 4 to 6 are the subject of this lesson."),
            H("Worked model answers"),
            EX("How is the island's fire important at the end?", intro="Plan an answer to: 'Show how fire is used in different ways in the novel.'", steps=[
                S("The signal fire", text="In the early chapters the fire is a symbol of hope and of Ralph's wish to be rescued."),
                S("The wild fire", text="The first fire on the mountain gets out of control and kills a small boy, showing the danger of carelessness."),
                S("The stolen fire", text="In chapter 10 Jack steals the glasses to make fire for cooking, not for rescue."),
                S("The hunting fire", text="In chapter 12 the tribe burns the forest to flush Ralph out. The same fire, by chance, brings the ship."),
                S("Conclude", text="The fire shows the move from hope to destruction, and its final irony: a fire set to kill saves Ralph."),
            ]),
            EX("The killing of Simon", intro="Plan an answer to: 'Why is the death of Simon a turning point?'", steps=[
                S("Who he is", text="Simon is gentle and perceptive. He alone finds out the truth about the beast."),
                S("How it happens", text="He tries to bring the news in the middle of a storm and a frenzied dance. The boys, Ralph and Piggy included, kill him."),
                S("What it shows", text="Fear and the crowd's excitement have overcome reason; good people can take part in evil."),
                S("Consequence", text="After this, Ralph and Piggy feel guilt, Jack's tribe grows stronger, and there is no way back to the first rules."),
            ]),
            MISTAKE("Calling the pig's head 'the beast'", "The beast is the boys' fear: first imagined, then confused with the dead parachutist. The head on the stick "
                    "is the Lord of the Flies. Simon learns that the beast is within the boys. Do not use the two names for one thing."),
            MISTAKE("Saying Ralph kills Piggy", "Roger releases the boulder that kills Piggy. Ralph, Piggy and the twins are on the other side. "
                    "Keep track of who does what in each scene: examiners mark mixed-up events as errors."),
            qz("How does Simon die?",
               "The boys, in a frenzy during a storm, mistake him for the beast and kill him",
               [("He falls from the mountain while looking for the beast", "He climbs the mountain and finds the dead airman, but he is killed later, on the beach."),
                ("Roger pushes a rock on him at Castle Rock", "The rock kills Piggy, not Simon, and at a later time."),
                ("He is lost in the forest fire", "The forest fire is in chapter 12 and is set to drive out Ralph; Simon is already dead.")],
               "Simon runs out of the forest during the feast dance and the excited boys kill him, thinking he is the beast.",
               hint="Think of the feast and the storm."),
            qz("How is Ralph finally rescued?",
               "A naval officer arrives because a ship sees the smoke of the burning island",
               [("Ralph lights the signal fire again with Piggy's glasses", "The glasses were stolen, and the fire that brings the ship is the tribe's hunting fire."),
                ("Sam and Eric swim to the ship and call for help", "Sam and Eric are held by Jack's tribe; they do not call the ship."),
                ("Jack asks the officer to take them away", "Jack is among the boys who stop when the officer appears, but the ship comes because of the smoke.")],
               "The tribe sets fire to the forest to catch Ralph; the smoke is seen by a naval ship and an officer lands on the beach.",
               hint="Remember what the tribe did to force Ralph out."),
            PQ("Describe the events that lead to the death of Piggy.",
               "Jack's tribe steals Piggy's glasses in chapter 10. In chapter 11 Ralph, Piggy, Sam and Eric go to Castle Rock to demand them. "
               "Piggy speaks holding the conch, and Roger, from above, lets a boulder fall. It kills Piggy and shatters the conch. "
               "Ralph escapes and the twins are captured."),
            PQ("What is ironic about the rescue?",
               "The fire that brings the rescue was set to kill Ralph, not to call a ship. The officer who comes is a part of the adult world, "
               "which is itself at war, and he is disappointed by the boys' behaviour while his own world is as violent as theirs."),
            PQ("Why does Ralph cry at the end?",
               "He weeps for the end of innocence, for the evil that he has seen in the boys, and in himself, and for the death of Piggy. "
               "He is safe, but he now understands the darkness in human nature."),
            SUM("In chapters 7 to 9 the hunt for the beast leads to Jack's split from Ralph and the killing of Simon.",
                "The pig's head on a stick is the Lord of the Flies; Simon learns the beast is within the boys.",
                "In chapters 10 and 11 the tribe steals Piggy's glasses, Roger kills Piggy, and the conch is smashed.",
                "In chapter 12 Ralph is hunted; the burning forest brings a naval officer and the rescue.",
                "Keep who did what in order: Roger kills Piggy, the frenzied crowd kills Simon."),
        ],
    ),
]

LESSONS += [
    # ------------------------------------------------------------------ 3. Lord of the Flies: characters
    lesson(
        module=M_PROSE, topic="Lord of the Flies: characters",
        title="Lord of the Flies: Ralph, Jack, Piggy, Simon and the others",
        slug="lit3-lotf-characters",
        minutes=23,
        summary="The main boys of Lord of the Flies: what each is like, what each stands for, how each changes, and how to "
                "write about a character with proof from the text.",
        objectives=[
            "Describe Ralph, Jack, Piggy, Simon and Roger with their key traits",
            "Say what each main boy stands for in the novel",
            "Explain how Ralph and Jack are rivals and why that matters",
            "Support a character point with an event from the book",
        ],
        key_concepts=["Protagonist", "Antagonist", "Foil", "Direct and indirect characterisation", "Round character", "Allegory"],
        blocks=[
            H("Introduction"),
            T("In a school class in Douala or Bamenda, there is often one pupil who leads, one who is clever but laughed at, one who "
              "is loud and bossy, and one who is quiet and kind. Golding uses types like these. His boys are individuals, but each "
              "also stands for an idea about human beings: reason, power, intelligence, goodness, cruelty."),
            D("A **protagonist** is the main character. An **antagonist** is the character who opposes the protagonist. "
              "A **foil** is a character who, by contrast, shows up the qualities of another.", title="Definitions"),
            D("**Characterisation** is how a writer shows a character. It is **direct** when the narrator tells us what the character is like, "
              "and **indirect** when we learn from the character's actions, speech, thoughts and the reactions of others.", title="Characterisation"),
            H("Ralph"),
            T("Ralph is about twelve, fair-haired, sporty and friendly. He is the protagonist. He is elected chief because of his size, his "
              "manner and his hold on the conch. He believes in rules, meetings, shelters and, above all, the signal fire. "
              "He is practical but not always clever: he often loses his thought in the middle of a speech and has to depend on Piggy's mind.\n\n"
              "Ralph changes. At first he is a boy who thinks of the island as a game. By the end he has joined in the killing "
              "of Simon, has been hunted like an animal and has come to understand how much evil there is in human beings. "
              "He stands for democracy, order and the hope of civilisation."),
            H("Jack Merridew"),
            T("Jack is the head of the choir and the antagonist. He is tall, thin, red-haired and proud. He demands to be chief and, when "
              "he is not, turns his anger to hunting. He says the hunters are the ones who keep the boys alive, which gives him power. "
              "A painted mask frees him from shame, and he rules by fear, rewards of meat and violence. By chapter 8 he is a chief of "
              "his own tribe at Castle Rock; in chapter 12 he leads the hunt for Ralph.\n\n"
              "Jack stands for the love of power and the natural drive to hunt and kill. He is a foil to Ralph: Ralph persuades and "
              "calls meetings, Jack commands and punishes."),
            H("Piggy"),
            T("Piggy is fat, asthmatic and short-sighted. We never learn his real name. He is the thinker of the group: he knows what a conch is, he "
              "understands how to use the glasses to make fire, and he tries to remind the boys of the rules. But the others laugh at him and "
              "Jack bullies him. He is not trusted as a leader because he is not strong or popular. His glasses are broken in chapter 4 "
              "and stolen in chapter 10. He is killed in chapter 11.\n\n"
              "Piggy stands for reason, science and the voice of the adult world. Because he is killed while holding the conch, his death "
              "shows how weak reason becomes when force takes over."),
            H("Simon"),
            T("Simon is a quiet, gentle choirboy who often walks alone to a clearing in the forest. He helps the littluns, helps Ralph build the "
              "shelters and speaks the truth that the beast may be inside the boys. He faces the Lord of the Flies in his own mind and finds the "
              "truth about the dead parachutist. He is killed by the others before he can tell it. Simon stands for goodness, insight and "
              "spiritual truth. Many readers compare him to a prophet or saint, but check with your teacher how far you should push such comparisons."),
            H("Roger and the others"),
            KEY("The supporting boys", "Each minor boy has a job in the story.", cards=[
                ["Roger", "A quiet, sinister choirboy. He throws stones near Henry in chapter 4 but misses on purpose. He grows into a torturer and, in chapter 11, releases the boulder that kills Piggy. He shows cruelty with no restraint."],
                ["Sam and Eric", "Twins, called Samneric. They keep the fire, see the parachutist, stay loyal to Ralph, but are forced to join Jack's tribe."],
                ["The littluns", "The youngest boys. They are afraid and cannot protect themselves. They spread rumours of the beast."],
                ["Maurice and Robert", "Older boys who play, and are caught up in the hunting game."],
            ]),
            EX("Compare Ralph and Jack", intro="Plan an answer to: 'Compare the leadership of Ralph and Jack.'", steps=[
                S("Ralph's method", text="He is chosen by a vote and holds meetings with the conch, so the boys can speak in turn. He puts the fire and shelters first."),
                S("Jack's method", text="He takes power by force. He offers meat and the thrill of the hunt, uses a mask, and punishes boys who disobey."),
                S("Their goals", text="Ralph wants rescue and order. Jack wants hunting, pleasure and power."),
                S("Conclude", text="The contrast shows two kinds of leadership, one based on agreement and one on fear. Most boys follow Jack in the end."),
            ]),
            EX("Show Piggy's importance", intro="Plan an answer to: 'What is the importance of Piggy to the group?'", steps=[
                S("His ideas", text="He supplies ideas Ralph does not have: how to use the conch, that the fire needs the glasses, that names matter."),
                S("His glasses", text="They are the only way to make fire, so Piggy holds the group's chance of rescue."),
                S("His treatment", text="Jack bullies him, breaks a lens, then steals the glasses. The rejection of Piggy is a rejection of reason."),
                S("His death", text="He dies holding the conch. The end of the conch is the end of order."),
            ]),
            MISTAKE("Calling Jack evil from the start", "Jack is a choirboy who at first cannot kill a piglet. His change is gradual: hunting, then the mask, then "
                    "the power over the other boys. Show the change with events. A straight label with no proof earns few marks."),
            MISTAKE("Writing about yourself instead of the character", "The Board's report says candidates bring in personal experience when they should stay with the "
                    "text. Do not write 'In my school there was a boy like Piggy'. Write what Piggy does in the book."),
            TIP("A good character paragraph has three parts: a point (Ralph is a democratic leader), proof (he holds meetings and uses the conch so that each boy may speak) "
                "and meaning (this shows his belief in order). Paper 1 may ask who said or did something, so know the boys well."),
            qz("Which boy is killed because he tries to bring news about the truth of the beast?",
               "Simon",
               [("Piggy", "Piggy is killed later by Roger's boulder; he is not the one who finds the dead airman."),
                ("Ralph", "Ralph survives to the end and is rescued."),
                ("Roger", "Roger is one of Jack's hunters, who kills Piggy, and survives.")],
               "Simon finds that the beast is a dead airman. He runs to tell the others and the frenzied boys kill him.",
               hint="Which boy goes up the mountain alone?"),
            qz("What does Piggy mainly stand for in the novel?",
               "Reason and intelligence",
               [("Brutal strength", "Piggy is physically weak; strength belongs to Jack and Roger."),
                ("Love of hunting", "Piggy never hunts; he is a thinker."),
                ("Fear of the beast", "Piggy is not afraid of a beast. He thinks life has a scientific explanation.")],
               "Piggy is the thinker and protector of the rules; his death shows how reason is crushed when violence takes over.",
               hint="Think of his glasses."),
            PQ("Describe Jack's character and how it changes.",
               "Jack is proud, bossy and eager to lead. At first he is held back by his upbringing: in chapter 1 he cannot kill a piglet. He becomes a hunter, then "
               "paints his face and feels freed from shame. He gives up the signal fire for hunting, hits Piggy, forms his own tribe and finally hunts Ralph. "
               "He changes from a choirboy into a cruel chief."),
            PQ("Why is Ralph a good choice as the main character?",
               "Ralph is the protagonist who stands for order. His efforts to keep the fire, build shelters and hold meetings give the story its centre. "
               "His change from innocence to understanding at the end carries the novel's message about the darkness in human nature."),
            PQ("What part does Roger play?",
               "Roger is a quiet, cruel choirboy. In chapter 4 he throws stones but misses on purpose because the old rules still hold him. "
               "Later he enjoys hurting others, becomes Jack's torturer, and in chapter 11 he releases the boulder that kills Piggy. "
               "He shows how savagery grows when rules disappear."),
            SUM("Ralph (order, democracy) is the protagonist; Jack (power, hunting) is the antagonist and his foil.",
                "Piggy stands for reason; Simon for goodness and truth; Roger for cruelty.",
                "Sam and Eric stay loyal but are forced to join Jack; the littluns show fear.",
                "Show character with proof from the book: actions, speech and others' reactions.",
                "Stay with the text; leave out your own experience."),
        ],
    ),

    # ------------------------------------------------------------------ 4. Lord of the Flies: themes
    lesson(
        module=M_PROSE, topic="Lord of the Flies: themes and symbolism",
        title="Lord of the Flies: civilisation, savagery and loss of innocence",
        slug="lit3-lotf-themes",
        minutes=23,
        summary="The main themes of Lord of the Flies: civilisation against savagery, loss of innocence, the use and abuse of power, "
                "fear and the evil inside people, with a method for writing a theme answer.",
        objectives=[
            "Name and explain four main themes of the novel",
            "Support each theme with events from the book",
            "Explain how the ending links the themes",
            "Write a theme paragraph with a point, proof and meaning",
        ],
        key_concepts=["Theme", "Civilisation and savagery", "Loss of innocence", "Power and leadership", "Fear", "Human nature"],
        blocks=[
            H("Introduction"),
            T("A **theme** is the main idea that a story is about. It is not the plot (what happens) but the meaning behind it. "
              "A story about a goat in Bamenda market may be about greed or loyalty. In *Lord of the Flies*, the plot is a story of boys on an island. "
              "The themes are about all of us."),
            D("A **theme** is a central idea or message in a text, shown through events, characters and images.", title="Definition"),
            H("Civilisation versus savagery"),
            T("The most famous theme. **Civilisation** is life under rules, with order, cooperation and care for others. **Savagery** is life "
              "ruled by instinct, violence and fear. At the start, the boys try to copy the adult world: they vote, they have meetings, "
              "and they plan a fire. Little by little the rules lose power. By the end a tribe with painted faces hunts a boy for sport.\n\n"
              "Golding's message is that civilisation is thin. It must be kept up. Take away the adult rules and it can quickly break."),
            EX("Show how civilisation breaks down", intro="Plan an answer to: 'How does Golding show the collapse of civilisation on the island?'", steps=[
                S("Beginning", text="The conch is used for assemblies; Ralph is elected; rules are made about fire, shelters and speaking in turn."),
                S("Middle", text="Hunters neglect the fire. Jack paints his face and the boys follow him. Simon is killed in a frenzy."),
                S("End", text="Piggy is killed, the conch is destroyed, and the tribe hunts Ralph."),
                S("Conclude", text="Each step shows rules losing to fear and appetite. The collapse is gradual, which makes it believable."),
            ]),
            H("Loss of innocence"),
            T("The boys are children when they arrive. Their innocence is lost step by step: the first fire that kills a small boy, the "
              "hunting game that hurts Robert, the killing of Simon, the murder of Piggy. Ralph's tears at the end are for this loss. "
              "He knows now what people, including he, are capable of.\n\n"
              "The island itself is like a garden that is spoilt, and the word 'beast' stands partly for the evil that the boys find inside themselves."),
            H("Power, leadership and conflict"),
            T("Ralph and Jack show two ways to lead. Ralph is elected, holds meetings and thinks of the group's long-term safety (rescue). "
              "Jack uses fear, offers meat and excitement and punishes the weak. The novel asks which way gains followers. "
              "Many boys prefer Jack because he gives them fun and protection from fear. Golding does not say that "
              "democracy is easy: he shows that it needs everyone's discipline."),
            H("Fear and the beast"),
            T("Fear starts as a story told by a littlun, grows in the dark, and becomes a belief. The boys make up a beast, then a dead parachutist seems to prove it. "
              "Simon understands that the beast is inside them. The boys' fear leads them to kill Simon, which proves his point. "
              "The theme shows how fear makes people cruel and unreasonable."),
            KEY("Human nature", "Golding believed that evil comes from within people, not from outside. The island is calm, but the boys are the danger. "
                "The adult world is no better: it is fighting an atomic war, and the rescuing officer arrives on a warship.", cards=[
                ["Civilisation", "Rules, meetings, the conch, shelters, the signal fire."],
                ["Savagery", "Hunting, face paint, chants, the stolen glasses, the boulder."],
                ["Innocence", "Lost in stages; shown by Ralph's tears."],
                ["Power", "Ralph by vote and persuasion; Jack by fear and meat."],
            ]),
            EX("A paragraph on loss of innocence", intro="Write a model paragraph for: 'Discuss loss of innocence in Lord of the Flies.'", steps=[
                S("Point", text="The novel shows children losing their innocence and learning about the evil in themselves."),
                S("Proof", text="At first the boys play, but later a hunting game injures Robert, Simon is killed in a frenzy and Piggy is killed by a boulder."),
                S("Meaning", text="This shows that the boys do not need to be taught evil: it grows when rules disappear."),
                S("Link", text="At the end Ralph weeps for innocence ended, and the reader sees that the officer's world, at war, is not innocent either."),
            ]),
            MISTAKE("Retelling the story instead of discussing a theme", "A theme question asks what the book says about an idea. Use events as proof, "
                    "but explain what each event shows. A list of events, with no meaning, will not answer the question."),
            MISTAKE("Using your own opinion with no proof", "The report warns about personal experience. 'Children are naughty' is not enough. Cite an event from the book and then explain."),
            TIP("Paper 1 may ask what a passage or event is about, or which theme it shows. Learn each theme with two or three events. In Paper 2 (Section D), "
                "theme questions need a clear plan: theme, events, meaning, and a closing link."),
            qz("Which of these is the best statement of a theme of the novel?",
               "Without rules and fear of punishment, people can quickly become violent",
               [("A group of boys are shipwrecked on an island", "That is a statement of the plot, not a theme."),
                ("Ralph blows the conch", "That is one event, not an idea."),
                ("The island is hot and has fruit and pigs", "This describes the setting.")],
               "A theme is a general idea the story explores. The novel shows civilisation breaking down.",
               hint="A theme is an idea, not an event."),
            qz("What does Ralph weep for at the end?",
               "The end of innocence, the darkness in human hearts and Piggy's death",
               [("The loss of the conch only", "The conch is lost, but his tears are for something larger."),
                ("The fact that Jack has won", "Ralph is hunted, but Jack's victory is not what he weeps for."),
                ("The island, which he hated", "Ralph's feelings are about people, not the island itself.")],
               "Ralph understands the evil that the boys, and humans in general, are capable of, and he mourns his friend.",
               hint="Think about what he has learned."),
            PQ("Explain the theme of civilisation against savagery with two examples.",
               "Civilisation: the conch, the assemblies and the fire show order. Savagery: the hunt, the painted faces and the killing of Simon show the opposite. "
               "As the book goes on, the rules lose strength. The death of Piggy and the destruction of the conch are the end of civilisation on the island."),
            PQ("How does fear affect the boys?",
               "Fear begins with a small boy's story of a snake-thing and grows into the belief in a beast. It makes the boys stop thinking: they "
               "follow Jack for protection and kill Simon in a frenzy because they take him for the beast. The fear is really of themselves."),
            PQ("What does the novel suggest about leadership?",
               "It contrasts Ralph, who leads by agreement and thinks of rescue, with Jack, who leads by fear and the promise of meat. "
               "Many boys prefer Jack, which suggests that leadership by force can be attractive in times of fear. But it ends in cruelty and the hunt for Ralph."),
            SUM("A theme is a central idea shown through events and characters.",
                "The main themes are civilisation versus savagery, loss of innocence, power and leadership, and fear.",
                "Golding suggests that evil comes from within people and that civilisation is thin.",
                "Prove each theme with events from the book and explain what they show.",
                "Do not retell the story or use personal experience instead of the text."),
        ],
    ),

    # ------------------------------------------------------------------ 5. Lord of the Flies: symbols and style
    lesson(
        module=M_PROSE, topic="Lord of the Flies: themes and symbolism",
        title="Symbols and style in Lord of the Flies",
        slug="lit3-lotf-symbols",
        minutes=22,
        summary="The main symbols of Lord of the Flies (conch, glasses, fire, beast, the pig's head, face paint) and the author's style: "
                "narration, imagery, irony, foreshadowing and allegory.",
        objectives=[
            "Explain what the conch, Piggy's glasses, the fire, the beast and the pig's head stand for",
            "Show how a symbol changes through the story",
            "Describe Golding's narrative style, imagery and use of irony",
            "Write about a symbol using point, proof and meaning",
        ],
        key_concepts=["Symbol", "Allegory", "Irony", "Imagery", "Foreshadowing", "Third-person narrator"],
        blocks=[
            H("Introduction"),
            T("In Cameroon a flag, a drum or a staff of office stands for something larger than itself. A chief's staff stands for authority. "
              "In literature this is called a **symbol**. Golding fills his novel with symbols. When you can explain them, you can answer theme and extract questions with confidence."),
            D("A **symbol** is an object, person or place that stands for an idea beyond itself. "
              "An **allegory** is a story whose events and characters stand for a bigger meaning, often moral or political.", title="Definitions"),
            H("The main symbols"),
            KEY("What each symbol stands for", "Learn each symbol with its meaning and its fate.", cards=[
                ["The conch", "Order, law and democracy. Only the boy holding it may speak. It loses power as the boys lose respect for rules, and it is shattered when Piggy dies."],
                ["Piggy's glasses", "Reason, science and the power to make fire. They are broken, then stolen, so the group's intelligence is lost."],
                ["The signal fire", "Hope of rescue and link to civilisation. It is neglected for hunting, then replaced by fires of destruction."],
                ["The beast", "The boys' fear, which is finally shown to be inside themselves."],
                ["The pig's head (Lord of the Flies)", "Evil and the dark side of human nature. It speaks to Simon in his mind."],
                ["Face paint", "A mask that frees the boys from shame, so they can act cruelly."],
            ]),
            T("Other symbols you may meet: the island (a paradise that is spoilt), the scar left by the plane (the mark of the adult world's violence), "
              "Castle Rock (the fortress of the tribe, a symbol of force) and Simon's clearing (a quiet place of beauty and truth)."),
            EX("The conch as a symbol", intro="Plan an answer to: 'What is the importance of the conch?'", steps=[
                S("Meaning", text="It stands for order and democratic rule. It calls the boys to meetings."),
                S("Proof", text="Only the holder may speak. Ralph's authority and Piggy's confidence depend on it."),
                S("Change", text="Its power falls as the boys mock it; Jack's tribe does not need it; it is shattered when Piggy is killed."),
                S("Conclude", text="Its destruction marks the end of civilisation on the island."),
            ]),
            EX("The fire as a symbol", intro="Plan an answer to: 'Show how the fire changes in meaning.'", steps=[
                S("Hope", text="The signal fire is the boys' hope of rescue."),
                S("Danger", text="The first fire runs wild and a small boy disappears."),
                S("Neglect", text="The fire is allowed to go out while hunters hunt; a ship is missed."),
                S("Destruction", text="At the end the tribe sets the whole forest alight to kill Ralph. The smoke brings a ship."),
            ]),
            H("Golding's style"),
            KEY("Features of style", "Be ready to name a feature and give an example from the book.", cards=[
                ["Narrator", "Third-person and omniscient: the narrator can tell us what many boys think, but mostly follows Ralph. Past tense."],
                ["Imagery", "Vivid pictures of the island: heat, the sea, the jungle, the sun, the storm. Light and darkness show good and evil."],
                ["Irony", "Events turn out the opposite to what we expect. The choirboys in black robes become hunters. The officer expects fun and games. A fire to kill Ralph saves him."],
                ["Foreshadowing", "Early hints of later events: the stones thrown at Henry, the first fire, and Jack's failure to kill the piglet."],
                ["Allegory", "The island is a small model of the world, and the boys' story a lesson about humankind."],
            ]),
            T("The language is simple and direct, with the speech of English schoolboys of the time. The mood changes from bright and playful to dark and fearful. "
              "The language of the hunt becomes repetitive, with chanting, to show a crowd losing its reason."),
            TIP("When asked about a symbol, never only name what it stands for. Say how it appears, what happens to it, and what that shows. Ending with its loss "
                "(for the conch, glasses and fire) gives your answer a strong shape."),
            MISTAKE("Saying the conch 'is' democracy", "An object cannot be an idea. Say it 'stands for' or 'represents' order and democracy. Use words like 'symbolises'."),
            MISTAKE("Naming a feature without an example", "'Golding uses irony' earns little. Give the example: a fire lit to kill Ralph saves him. "
                    "Then explain why it is ironic."),
            qz("What does the breaking of the conch stand for?",
               "The end of order and rules on the island",
               [("The start of the rescue", "The rescue comes later and by chance, through smoke."),
                ("Jack's defeat", "Jack is not defeated at that moment; it is Piggy who dies."),
                ("Simon's courage", "Simon is already dead; the conch is shattered with Piggy's death.")],
               "The conch is the symbol of order. When it is destroyed with Piggy, no rule is left.",
               hint="What did the conch let the boys do?"),
            qz("Which of these is an example of irony?",
               "The fire set to kill Ralph brings the ship that saves him",
               [("Ralph blows the conch", "This is an ordinary event, not an ironic one."),
                ("Piggy wears glasses", "This is a description, not irony."),
                ("The boys build a shelter", "This is an ordinary event.")],
               "Irony is the gap between what is expected and what happens. A fire meant to destroy brings rescue.",
               hint="Look for the opposite of what was intended."),
            PQ("Explain what Piggy's glasses stand for and what happens to them.",
               "The glasses stand for reason and science, and the power to make fire. They are used to light the signal fire, broken by Jack in chapter 4 and "
               "stolen by the tribe in chapter 10. Losing them shows the boys losing intelligence and the chance of rescue."),
            PQ("What is the Lord of the Flies?",
               "It is the pig's head on a stick, offered to the beast. Simon imagines it speaking to him. It stands for evil within the boys. "
               "The name is also a translation of Beelzebub, a name for the devil."),
            PQ("Name two features of Golding's style and give an example of each.",
               "Imagery: vivid descriptions of the island's heat and the storm. Irony: the rescue by the same fire that was set to kill Ralph. "
               "Other features are foreshadowing (Roger's stones that miss) and allegory (the island as the world)."),
            SUM("Symbols stand for ideas: the conch (order), glasses (reason), fire (hope, then destruction), beast (fear), pig's head (evil).",
                "A symbol changes through the story; its loss often marks a turning point.",
                "Golding uses a third-person narrator, vivid imagery, irony, foreshadowing and allegory.",
                "Always add an example and a meaning when you name a feature of style.",
                "Say 'stands for' or 'symbolises', not 'is'."),
        ],
    ),
]

LESSONS += [
    # ------------------------------------------------------------------ 6. Silas Marner: plot 1
    lesson(
        module=M_PROSE, topic="Silas Marner: plot and setting",
        title="Silas Marner: Lantern Yard, Raveloe and the stolen gold",
        slug="lit3-silas-plot-one",
        minutes=24,
        summary="The setting and first half of George Eliot's Silas Marner: Silas's betrayal at Lantern Yard, his lonely life in Raveloe, "
                "the Cass family, the secret marriage of Godfrey and the theft of Silas's gold by Dunstan.",
        objectives=[
            "Describe the two settings: Lantern Yard and Raveloe",
            "Explain why Silas leaves Lantern Yard and how it changes him",
            "Explain the secrets and problems of Godfrey and Dunstan Cass",
            "Retell how Silas's gold is stolen and what the village does",
        ],
        key_concepts=["Setting", "Exile", "Miser", "Squire", "Subplot", "Raveloe"],
        blocks=[
            H("Introduction"),
            T("Think of a person from a village in the North West who is falsely accused, thrown out by his church and his friends, and who moves "
              "alone to a village in the South where nobody knows him. He closes his door, works all day and trusts nobody. "
              "That is how George Eliot's *Silas Marner* begins. The novel was published in 1861. George Eliot is the pen name of a woman, Mary Ann Evans. "
              "The full title is *Silas Marner: The Weaver of Raveloe*."),
            D("A **setting** is the time and place of a story. *Silas Marner* is set in the English countryside in the early nineteenth century "
              "(check your text for the exact period), in a farming village called Raveloe, with a flashback to a town chapel called Lantern Yard.",
              title="Setting"),
            KEY("Two places, two worlds", "The novel contrasts a narrow town sect and a lively country village.", cards=[
                ["Lantern Yard", "A small chapel community in a northern industrial town. Strict, religious, and ready to judge by a drawing of lots. This is where Silas is betrayed."],
                ["Raveloe", "A rich, rural farming village in the Midlands. Church-going, with squires, farmers, an inn called the Rainbow, folk sayings, and old ways. At first it is suspicious of Silas."],
                ["The stone-pits", "Silas's cottage stands at the edge of the village, near an old stone-pit. It is a lonely place."],
            ]),
            IMG("f5lit-3-silas-timeline.svg", alt="A timeline of Silas Marner: Lantern Yard, move to Raveloe, theft of the gold, arrival of Eppie, sixteen years later, the return of the gold.",
                caption="Figure 1. The shape of the story. The novel has two parts, with a gap of sixteen years between them."),
            H("Silas at Lantern Yard"),
            T("Silas is a weaver and a devout member of the Lantern Yard chapel. He has a close friend, William Dane, and is engaged to a young woman, Sarah. "
              "Silas, who has fits, sits up with the dying deacon and falls into one. When the deacon is found dead, the church's money is missing. "
              "Silas's own knife and the empty money bag are found, and the reader is made to see that William Dane has planted the evidence. "
              "The community draws lots to decide, and the lot says Silas is guilty. Silas is "
              "sure that God will show his innocence. He is shocked. Sarah breaks off the engagement and soon marries William. "
              "Silas loses faith in his friend, in the church and in God. He leaves."),
            H("Silas in Raveloe"),
            T("Silas settles in Raveloe. He is a stranger, pale and short-sighted, and he has fits in which he stands stiff and silent for a long time "
              "(a condition called catalepsy). The villagers fear him and think he has strange powers. He talks to nobody, works at his loom, "
              "and for fifteen years does nothing but weave. Because he has lost love and faith, he finds comfort in gold. He is paid in guineas, hides them under the "
              "floor, and counts them each night. He becomes a **miser**: a person who loves money for its own sake."),
            H("The Cass family"),
            T("Squire Cass is the biggest landowner. His eldest son, Godfrey, is pleasant but weak. Godfrey is secretly married to Molly Farren, "
              "a poor woman who is addicted to opium, and she has a child. His younger brother, Dunstan (Dunsey), knows the secret and "
              "blackmails him. Godfrey loves Nancy Lammeter, a good, respected young woman, and cannot marry her while his secret remains. "
              "Dunstan is lazy, spiteful and dishonest. Godfrey, afraid of exposure, has handed him rent money that he collected from a tenant."),
            T("Dunstan offers to sell Godfrey's horse, Wildfire. He rides it in a hunt, the horse is killed, and Dunstan walks home in the dark and rain. "
              "On the way he sees the light of Silas's cottage and remembers the old weaver's hidden gold. He finds the cottage empty "
              "as Silas has gone out, takes the gold and vanishes. Nobody knows where he has gone."),
            H("The robbery and the village"),
            T("Silas comes home to find his gold gone. He is broken. The villagers meet at the Rainbow inn, where they discuss the robbery in comic "
              "and gossipy ways, and a pedlar is first suspected. Many neighbours begin to visit Silas, bringing kindness, including Dolly Winthrop. "
              "Silas is not able to accept their warmth, but the visits are a first step back to the community. "
              "(The Rainbow scene and the robbery are in the first part, in the middle chapters: check your text for numbers.)"),
            TIP("Exam extracts from the early chapters can show Silas alone at his loom, the Rainbow inn scene, or Godfrey and Dunstan quarrelling. "
                "Know who is speaking and whose secret is at stake. The Board's report notes that candidates did not enjoy style and theme questions in this text, so practise those too."),
            EX("Why is Silas a lonely man?", intro="Plan an answer to: 'Explain why Silas Marner lives alone in Raveloe.'", steps=[
                S("The cause", text="At Lantern Yard William Dane betrays Silas, and the chapel finds him guilty by lot. Sarah leaves him."),
                S("The effect on faith", text="He loses faith in God, friends and the church."),
                S("In Raveloe", text="He is a stranger with fits, and the villagers distrust him. He keeps away from them."),
                S("The substitute", text="He turns to his loom and to gold, which cannot love him back."),
            ]),
            EX("How is Silas's gold stolen?", intro="Plan an answer to: 'Describe how the robbery of Silas's gold takes place.'", steps=[
                S("Dunstan's need", text="He owes Godfrey and has taken Godfrey's rent money. He sells Wildfire, the horse, for gain."),
                S("The accident", text="He rides the horse in a hunt and it is killed."),
                S("The chance", text="He sees Silas's cottage lit and empty and remembers the gold."),
                S("The theft", text="He takes the guineas and leaves the village. Nobody knows what has happened to him."),
            ]),
            MISTAKE("Confusing the two brothers", "Godfrey is the older, weak but kind-hearted son with the secret marriage. Dunstan is the younger, spiteful brother who steals the gold. "
                    "Examiners see answers where the brothers' actions are swapped, just as in the report's comment on mixed-up events."),
            MISTAKE("Saying Silas stole the money at Lantern Yard", "Silas is innocent: William Dane framed him. The 'guilty' verdict is a false one, made by lot. Say 'falsely accused'."),
            qz("Why does Silas leave Lantern Yard?",
               "He is falsely accused of theft and loses faith in his church and his friend",
               [("He is sent to prison for stealing", "He is not imprisoned: the church community decides by lot and he leaves."),
                ("He wants to find gold elsewhere", "He leaves in shame and sorrow, not for money; the love of gold comes later."),
                ("He marries Sarah and moves away", "Sarah leaves him and marries William Dane.")],
               "The false accusation, the lot and Sarah's rejection make Silas leave in despair.",
               hint="Think about William Dane."),
            qz("Who steals Silas's gold?",
               "Dunstan Cass",
               [("Godfrey Cass", "Godfrey is the older brother, who is weak but not a thief of Silas's gold."),
                ("William Dane", "William Dane is at Lantern Yard and has no part in the robbery."),
                ("A pedlar", "The pedlar is suspected by the villagers, but he is innocent.")],
               "Dunstan, who needs money, sees the cottage empty and takes the gold.",
               hint="Whose horse has just been killed?"),
            PQ("Describe Silas's life in Raveloe before the robbery.",
               "Silas lives alone in a cottage by the stone-pits, works at his loom, speaks to nobody and is feared because of his fits. "
               "He earns guineas and hides them under his floor. He counts them every night, and they replace the love and faith he has lost."),
            PQ("What is the secret that Godfrey Cass keeps?",
               "He is secretly married to Molly Farren, a poor woman who is addicted to opium, and they have a child. "
               "He hides this because he wants to marry Nancy Lammeter, and his brother Dunstan blackmails him."),
            PQ("What does the village do after the robbery?",
               "The men discuss it at the Rainbow inn and suspect a pedlar. Neighbours such as Dolly Winthrop visit Silas with kindness. "
               "Their visits start to break his loneliness."),
            SUM("The novel contrasts Lantern Yard, a narrow chapel community, with Raveloe, a farming village.",
                "Silas is falsely accused by William Dane, judged by lot, and leaves, losing faith.",
                "In Raveloe he lives alone, weaves and hoards gold.",
                "Godfrey's secret marriage and Dunstan's blackmail lead to the theft of Silas's gold.",
                "The villagers' kindness after the robbery begins Silas's return to people."),
        ],
    ),

    # ------------------------------------------------------------------ 7. Silas Marner: plot 2
    lesson(
        module=M_PROSE, topic="Silas Marner: plot and setting",
        title="Silas Marner: Eppie and the sixteen years after",
        slug="lit3-silas-plot-two",
        minutes=24,
        summary="The second half of Silas Marner: the golden-haired child who appears at Silas's hearth, how Silas raises Eppie, "
                "Godfrey's secret, and the return of the gold sixteen years later.",
        objectives=[
            "Retell the arrival of the child and Silas's decision to keep her",
            "Explain what Godfrey does and does not do about the child",
            "Describe the events sixteen years later, including the finding of the gold",
            "Explain Eppie's choice and the ending",
        ],
        key_concepts=["Coincidence", "Adoption", "Confession", "Choice", "Resolution", "Time gap"],
        blocks=[
            H("Introduction"),
            T("Silas has lost his gold. What can fill the empty place? Eliot's answer is a surprise: a small child. "
              "This lesson follows the story from that night to the end. Many exam extracts come from these chapters, "
              "so you need to know the order of events and who is speaking. The Board's report notes that the character Silas "
              "attracted most candidates (a popular, likeable character) in the questions that were set. A question on Silas is likely to be the safe choice."),
            D("A **coincidence** is an event that happens by chance but seems to have meaning. Eliot uses a few big coincidences, "
              "but she explains them through the characters' choices.", title="Definition"),
            H("The child at the hearth"),
            T("On a snowy New Year's Eve (check your text: the date is near Christmas and New Year), Godfrey is at the Squire's party. Molly Farren, "
              "carrying her small daughter, sets out to the Red House to tell everyone she is Godfrey's wife. She takes opium, falls in the snow and "
              "dies. The little girl, with golden curls, wanders towards the light of Silas's cottage. Silas has the door open and is in one of his "
              "fits. When he recovers, he sees the golden curls on his hearth and thinks his gold has come back. Then he realises it is a child."),
            T("Silas decides to keep her. He names her Eppie, after his mother and sister (Hephzibah). The next morning, Molly's body is found, and "
              "Godfrey sees it and knows the child is his. He says nothing, because he is relieved that the secret is safe and he can marry Nancy. "
              "Godfrey does not claim her. This is the great moral failing of Godfrey's life."),
            KEY("Silas and Eppie", "Eppie changes Silas's life.", cards=[
                ["Care", "He cares for her and learns to wash, feed and teach her. He is helped by Dolly Winthrop."],
                ["Community", "Dolly's advice and Aaron, Dolly's son, bring Silas into village life. He starts to go to church."],
                ["Love instead of gold", "His love for Eppie replaces his love for money. His fits become less severe."],
            ]),
            H("Sixteen years later"),
            T("Part Two begins sixteen years after Eppie's arrival. Eppie is a lively young woman. She loves Silas and will marry Aaron Winthrop, Dolly's son. "
              "Godfrey and Nancy are married but have no children of their own. Then the stone-pit is drained and a skeleton is found: Dunstan, "
              "with Silas's gold beside him. The gold is returned. Silas is glad, but now it is only money."),
            T("The discovery makes Godfrey confess to Nancy that Eppie is his daughter. They go to Silas to offer to adopt Eppie and give her a life in a larger house. "
              "Silas is hurt but says Eppie must choose. Eppie refuses. She cannot leave the man who brought her up, and she is happy among the people who know her. "
              "Godfrey, who had never claimed her, has no right to take her now. Nancy and Godfrey leave. Eppie marries Aaron, and the wedding is a happy village occasion."),
            T("Silas takes Eppie to Lantern Yard to find some trace of his past, and to clear his name. But the little chapel is gone: a factory stands where it was, and nobody "
              "can tell him anything. He accepts that he must trust in the goodness of those around him, without needing an answer. (Check your text for the chapter of this visit.)"),
            IMG("f5lit-3-silas-relations.svg", alt="A diagram of relationships: Silas and Eppie at the centre, Godfrey and Nancy Cass on one side, Dunstan and Molly Farren linked to Godfrey, Dolly and Aaron Winthrop on the other.",
                caption="Figure 2. The main characters and how they are linked."),
            EX("Why does Eppie refuse Godfrey?", intro="Plan an answer to: 'Why does Eppie choose to stay with Silas?'", steps=[
                S("Silas's love", text="He found her as a baby, cared for her through her childhood and gave her love instead of gold."),
                S("Godfrey's failure", text="He saw his dead wife and kept silent; he did nothing for sixteen years. His offer comes too late."),
                S("Her life", text="She is happy with Silas, Dolly, Aaron and the village, and does not want to be a lady."),
                S("Conclude", text="Duty and love, not blood, make a family. Eppie chooses love."),
            ]),
            EX("The return of the gold", intro="Plan an answer to: 'What is the importance of the finding of Dunstan's body?'", steps=[
                S("The facts", text="The draining of the stone-pit reveals a skeleton and Silas's gold."),
                S("For Silas", text="He has his gold again, but it no longer matters to him; he has Eppie."),
                S("For Godfrey", text="The robbery is solved, and he feels forced to confess his own secret."),
                S("Theme", text="Wrongdoing is eventually revealed; Dunstan's theft ends in his own death."),
            ]),
            MISTAKE("Saying Godfrey adopts Eppie", "Godfrey and Nancy offer to take Eppie, but she refuses. She stays with Silas. Do not end the story with Eppie in the Red House."),
            MISTAKE("Using personal experience", "The report says candidates lost marks by writing about their own experiences in the poetry answers, and the same advice holds for prose. "
                    "Write about the people in the book, not the people you know."),
            qz("What does Silas think when he first sees the child on his hearth?",
               "That it is his lost gold come back",
               [("That it is a ghost from Lantern Yard", "He sees golden curls and thinks of the gold, not of a ghost."),
                ("That it is Godfrey's child", "He does not know whose child she is."),
                ("That it is a pedlar's child", "No such idea is in the story.")],
               "Silas's sight is poor, and the golden hair looks like his guineas.",
               hint="Think of what he has lost."),
            qz("Why does Eppie refuse to go with Godfrey and Nancy?",
               "She prefers to stay with Silas, who has loved and raised her",
               [("She dislikes Nancy", "Nancy is kind. Eppie's choice is about Silas."),
                ("She is afraid of the Squire", "Fear plays no part in her answer."),
                ("Silas forbids her to go", "Silas lets her choose; he does not forbid her.")],
               "Eppie chooses love and loyalty over wealth and blood-ties.",
               hint="Who was there for her for sixteen years?"),
            PQ("Describe how Eppie comes to live with Silas.",
               "Eppie's mother, Molly Farren, dies in the snow on her way to the Red House. The golden-haired child wanders into Silas's open cottage while he is in a fit. "
               "Silas thinks she is his gold returned. He keeps her, names her Eppie, and with help from Dolly Winthrop raises her. "
               "Godfrey sees the dead mother but does not claim the child."),
            PQ("How is Silas's gold returned?",
               "Sixteen years later the stone-pit is drained and the skeleton of Dunstan is found with the gold. "
               "It shows that Dunstan stole it and died in the pit. Silas receives the gold but values Eppie far more."),
            PQ("What does Silas find when he returns to Lantern Yard?",
               "The chapel has been replaced by a factory, and there is nobody to tell him about the past. He does not learn the truth about the accusation, "
               "but he accepts that his life is now in Raveloe with Eppie."),
            SUM("A golden-haired child enters Silas's cottage on the night her mother dies in the snow.",
                "Silas keeps and loves Eppie; Godfrey sees his dead wife and says nothing.",
                "Sixteen years later Dunstan's skeleton and the gold are found when the stone-pit is drained.",
                "Godfrey confesses and offers to adopt Eppie; she refuses and stays with Silas, then marries Aaron.",
                "Lantern Yard has gone: Silas has to live by trust and love, not by proof."),
        ],
    ),

    # ------------------------------------------------------------------ 8. Silas Marner: characters
    lesson(
        module=M_PROSE, topic="Silas Marner: characters",
        title="Silas Marner: Silas, Eppie, Godfrey, Dunstan and the village",
        slug="lit3-silas-characters",
        minutes=23,
        summary="The main characters of Silas Marner: Silas, Eppie, Godfrey, Dunstan, Nancy, Dolly Winthrop and Aaron. What each is like, "
                "what each does, how Silas changes, and how to write about them.",
        objectives=[
            "Describe Silas Marner and the change in him",
            "Compare Godfrey and Dunstan Cass",
            "Explain the roles of Eppie, Nancy, Dolly and Aaron",
            "Support points about character with events",
        ],
        key_concepts=["Dynamic character", "Contrast", "Round and flat character", "Moral choice", "Foil", "Minor character"],
        blocks=[
            H("Introduction"),
            T("In *Silas Marner* the characters matter more than any single event. George Eliot cared about how people's choices make them who they are. "
              "A question on a character is usually the most popular in the exam, as the Board's report notes for Silas himself. So you need to "
              "know him very well, and also the people around him."),
            D("A **dynamic character** changes during the story. A **static character** stays the same. Silas is a dynamic character.", title="Definition"),
            H("Silas Marner"),
            T("At the start Silas is a devout, trusting young man at Lantern Yard. After the false accusation he is bitter, withdrawn and in love with gold. "
              "He is hard-working, honest and skilled, but lonely and fearful. The villagers see him as a strange creature because of his fits and his habits.\n\n"
              "Eppie changes him. He learns tenderness, patience and trust. He joins the church again and finds friends. At the end he is a "
              "gentle, content old man whose home is full of love. His life shows redemption: he is rescued by love and community."),
            H("Eppie"),
            T("Eppie is the golden-haired child. As a young woman she is loving, open, loyal and practical. She chooses love over wealth when she refuses Godfrey. "
              "She represents the new life that comes into Silas's world and the power of love. She is also a symbol: her golden hair replaces the lost gold."),
            H("Godfrey Cass"),
            T("Godfrey is the eldest son of Squire Cass. He is kind-hearted but weak. He fears his father, hides his marriage to Molly, and puts off every hard "
              "decision. He lets chance solve his problems and does not claim Eppie. He is sorry for it later but too late. He is not a villain, but his weakness "
              "does harm to others. His punishment is that he has no children of his own, and that Eppie refuses him."),
            H("Dunstan Cass"),
            T("Dunstan (Dunsey) is Godfrey's younger brother: selfish, idle and cruel. He blackmails Godfrey, borrows money, wastes it, and steals Silas's gold. "
              "He is a **foil** to Godfrey (a character who contrasts with another): Godfrey is weak but has a conscience, Dunstan has neither. "
              "His end is to die in the stone-pit, where his skeleton lies hidden for sixteen years."),
            KEY("The supporting characters", "They carry the themes of community and goodness.", cards=[
                ["Nancy Lammeter", "Godfrey's wife. Good, sensible and principled. She would like a child, and she and Godfrey have none of their own."],
                ["Dolly Winthrop", "The kind neighbour who teaches Silas to care for a child and brings him into the church and the village. She stands for simple, warm goodness."],
                ["Aaron Winthrop", "Dolly's son. A good, steady young man who marries Eppie."],
                ["Squire Cass", "The rich, easy-going landowner of the Red House, whose indulgence helps ruin his sons."],
                ["William Dane", "Silas's false friend at Lantern Yard, who framed him."],
                ["Mr Macey and the Rainbow men", "The village chorus: gossipy, comic, but shrewd. They show the life of Raveloe."],
            ]),
            EX("How does Silas change?", intro="Plan an answer to: 'Trace the changes in the character of Silas Marner.'", steps=[
                S("Lantern Yard", text="A trusting man, who is betrayed and loses faith."),
                S("Early Raveloe", text="A recluse who works day and night and loves his gold."),
                S("After the theft", text="Empty and desolate, but he begins to accept kindness from neighbours."),
                S("With Eppie", text="He is awakened by love, goes back to church and joins the community."),
                S("Conclude", text="He ends happy, which shows that love and human company heal."),
            ]),
            EX("Compare Godfrey and Dunstan", intro="Plan an answer to: 'Compare the two Cass brothers.'", steps=[
                S("Likeness", text="Both are sons of the Squire and both are tied by the secret; both cause suffering to others."),
                S("Godfrey", text="Weak, kind, with a conscience; hopes his problems will solve themselves; does not claim Eppie."),
                S("Dunstan", text="Selfish and spiteful; blackmails and steals; has no remorse."),
                S("Consequences", text="Dunstan dies in disgrace; Godfrey is punished by childlessness and Eppie's refusal."),
            ]),
            MISTAKE("Saying Godfrey is as bad as Dunstan", "Eliot treats them differently. Godfrey has a conscience and suffers; Dunstan is a thief and a blackmailer. Show the difference with events."),
            MISTAKE("Mixing up Nancy and Dolly", "Nancy Lammeter becomes Godfrey's wife and lives at the Red House. Dolly Winthrop is the village neighbour who helps Silas. "
                    "The report shows that mixed-up characters lose marks."),
            TIP("A strong character answer uses a few words about what the person is like, then an event that proves it, then what it shows about the story's themes. "
                "In Paper 1 you may be asked who said something, or who did something: know each character's main actions."),
            qz("Which character is a foil to Godfrey Cass?",
               "Dunstan, his selfish and dishonest brother",
               [("Silas Marner", "Silas is a contrast to Godfrey in some ways, but a foil in the story is closest in rank and family, which is Dunstan."),
                ("Aaron Winthrop", "Aaron is a good, steady young man but is not paired with Godfrey in the plot."),
                ("Squire Cass", "The Squire is Godfrey's father, not his foil.")],
               "Dunstan has no conscience, while Godfrey has one, which sets off Godfrey's weakness.",
               hint="Think of the two brothers."),
            qz("Who helps Silas to care for the child and to join village life?",
               "Dolly Winthrop",
               [("Nancy Lammeter", "Nancy lives in the Red House and is Godfrey's wife; she does not raise Eppie."),
                ("Molly Farren", "Molly is Eppie's mother, who dies in the snow."),
                ("Sarah", "Sarah is at Lantern Yard, where she left Silas.")],
               "Dolly, a kind neighbour, advises Silas and takes Eppie to learn her letters and manners.",
               hint="She is Aaron's mother."),
            PQ("Describe Silas Marner's character at the start and at the end.",
               "At the start he is hard-working and devout, then bitter and shut away, loving gold. At the end he is a content man who loves Eppie, "
               "belongs to the church and neighbours, and trusts people again. The change is caused by love and community."),
            PQ("Why is Godfrey Cass a weak character?",
               "He fears his father and the loss of Nancy, so he hides his marriage, lets Dunstan blackmail him and does not claim Eppie. "
               "He puts things off and waits for chance to help. He regrets it later, but it is too late."),
            PQ("What is Dolly Winthrop's role in the story?",
               "Dolly is a kind, simple village woman. She comforts Silas after the theft, helps him with Eppie, and invites him back into the church and the village. "
               "She stands for neighbourly goodness."),
            SUM("Silas changes from a trusting man to a lonely miser, then to a loving father and neighbour.",
                "Eppie stands for love and chooses Silas over wealth.",
                "Godfrey is weak but has a conscience; Dunstan is selfish and a thief; they contrast.",
                "Nancy, Dolly and Aaron stand for goodness and community.",
                "Prove each character point with events from the book."),
        ],
    ),

    # ------------------------------------------------------------------ 9. Silas Marner: themes and style
    lesson(
        module=M_PROSE, topic="Silas Marner: themes and style",
        title="Silas Marner: redemption, community, money and the narrator's style",
        slug="lit3-silas-themes",
        minutes=24,
        summary="The main themes of Silas Marner (redemption through love, community, wealth against affection, consequences of "
                "choices, faith and class) and Eliot's style: omniscient narrator, irony, humour, dialect and imagery.",
        objectives=[
            "Explain redemption, community, money and love, consequences and faith as themes",
            "Show how the gold and the golden hair work as images",
            "Describe George Eliot's narrative style with examples",
            "Write a theme or style paragraph with point, proof and meaning",
        ],
        key_concepts=["Redemption", "Community", "Consequence", "Omniscient narrator", "Irony", "Dialect", "Realism"],
        blocks=[
            H("Introduction"),
            T("The Board's report says that candidates were not comfortable with questions on style and themes in *Silas Marner*, "
              "while they enjoyed questions on a popular character. This lesson fills that gap. It will help you answer both Paper 1 questions "
              "on the novel's ideas and Paper 2 essay questions."),
            D("**Redemption** means being saved or set free from a bad state, such as despair, selfishness or guilt. "
              "In *Silas Marner* Silas is redeemed by love and by being part of a community.", title="Definition"),
            H("Redemption through love"),
            T("Silas loses faith and love, and so replaces them with gold. The gold is cold, and he gets no happiness from it. "
              "When the child comes, his heart opens. He feels warmth, responsibility and joy. Eliot suggests that human love, "
              "not wealth, is what heals people. The golden hair of the child replaces the golden coins."),
            H("Community"),
            T("Raveloe is not perfect, but its people (Dolly, Aaron, Mr Macey, the Rainbow men) are a community. At first it fears Silas. After the theft and "
              "the arrival of Eppie, it welcomes him. By the end, he is part of village life. Eliot's message is that a person alone becomes twisted; "
              "people need one another."),
            H("Money and love"),
            T("Silas loves gold at first. Dunstan steals for money. Godfrey's Squire family values wealth and rank. But Eppie "
              "chooses love and plain home life over a rich home. The contrast shows that money is not the right measure of happiness."),
            H("Consequences of choices"),
            T("Eliot believed that actions have results which cannot be escaped. Godfrey's lie leads him to lose his daughter. Dunstan's theft ends in his death. "
              "William Dane's lie ends in the loss of the chapel's trust. Silas's kindness to Eppie brings him love. In the novel nobody escapes the effects "
              "of what they do, but kindness has good effects."),
            H("Faith, chance and rank"),
            T("Silas's faith is broken by the drawing of lots, which seems unjust. Later he finds a new, simpler kind of trust in goodness, shown in Dolly's plain belief "
              "and in his own care for Eppie. Chance (the lot, the open door, the snow) plays a large part, but Eliot shows people responding to chance well or badly. "
              "Rank is also a concern: the Squire's family is rich but troubled, while the weaver and Dolly's son are happier."),
            KEY("Images to learn", "Symbols and images carry the themes.", cards=[
                ["Gold and golden hair", "Silas mistakes the golden curls for his gold. Gold means cold wealth; golden hair means warm love."],
                ["The loom", "Silas's work and his isolation: he weaves alone, day after day."],
                ["The hearth and open door", "The place where the child enters: home, warmth, a chance for change."],
                ["The stone-pits", "Dunstan's grave and secret, kept for sixteen years."],
                ["Lantern Yard's disappearance", "Silas can no longer look to the past for answers; he must live by trust."],
            ]),
            H("George Eliot's style"),
            KEY("Features of style", "Learn each with an example.", cards=[
                ["Omniscient narrator", "A third-person narrator who knows everything, explains the characters' thoughts and comments on their actions, often kindly and wisely."],
                ["Realism", "Everyday country people and places shown truthfully and in detail: farms, inns, weaving, church."],
                ["Humour and irony", "The Rainbow inn conversations are comic. Irony arises, for instance, when the gold is lost and a child is found."],
                ["Dialect", "The villagers speak in rural speech, which gives colour and truth."],
                ["Sympathy", "The narrator treats even Godfrey and Silas with understanding."],
                ["Folk-tale quality", "A lonely man, a lost treasure and a magic child: the story feels like an old tale set in real life."],
            ]),
            EX("A theme paragraph", intro="Write a model paragraph for: 'Show how love is more valuable than money in Silas Marner.'", steps=[
                S("Point", text="The novel shows that love is worth more than wealth."),
                S("Proof", text="Silas hoards gold and is miserable. When the gold is stolen and the child arrives he finds happiness. Later, when the gold returns, Eppie matters more to him."),
                S("More proof", text="Eppie refuses the comfort of Godfrey's house to stay with Silas."),
                S("Meaning", text="Eliot suggests that happiness comes from affection and belonging, not from possessions."),
            ]),
            EX("A style paragraph", intro="Write a model paragraph for: 'Comment on George Eliot's use of the narrator.'", steps=[
                S("Point", text="Eliot uses an omniscient narrator who is close to the characters and comments on them."),
                S("Proof", text="The narrator tells us what Silas feels at the hearth and judges the weak decisions of Godfrey."),
                S("Meaning", text="This lets the reader sympathise with the characters, and shows that the author cares about moral choices."),
            ]),
            MISTAKE("Calling the ending 'unrealistic and magic' without proof", "Eliot uses coincidence, but she makes the results depend on characters' choices. Argue from the text."),
            MISTAKE("Naming style features with no example", "'The author uses irony' is only half an answer. Give an example, such as the thief who dies where he hid the gold."),
            qz("Which of these is the best statement of a main theme of Silas Marner?",
               "Love and community can redeem a person who has been hurt",
               [("Weavers are poor workers", "This is not a theme in the novel."),
                ("Horses are dangerous in a hunt", "Wildfire's death is an event, not a theme."),
                ("Villages are always kind to strangers", "The villagers first fear Silas, so this does not fit.")],
               "Silas is healed by Eppie's love and the neighbours' kindness.",
               hint="What heals Silas?"),
            qz("What do the golden curls of the child suggest to Silas?",
               "His lost gold",
               [("The face of Sarah", "He does not link the child with Sarah."),
                ("The light of the Rainbow inn", "The inn is not part of the scene."),
                ("A ghost of his mother", "The story does not suggest a ghost.")],
               "Silas has poor sight and, in the firelight, the golden hair looks like the guineas he lost.",
               hint="What has he been missing?"),
            PQ("Explain the theme of redemption in Silas Marner.",
               "Silas is broken by the false accusation and becomes a recluse who loves gold. The theft of the gold and the arrival of Eppie change him. "
               "He learns to love and trust, rejoins the church and neighbours, and is redeemed by love and community."),
            PQ("Name two features of George Eliot's style with an example of each.",
               "Omniscient narrator: she tells us what Silas and Godfrey think and comments on them. Humour and dialect: the Rainbow inn conversations show comic village talk. "
               "Another feature is irony: the gold is lost, but a greater treasure, a child, arrives."),
            PQ("What does the novel say about money?",
               "Money gives Silas no happiness and leads Dunstan to crime. Eppie, who could have wealth with Godfrey, chooses a poor home with Silas. "
               "The novel says that love and belonging matter more than money."),
            SUM("Redemption through love is the central theme: Eppie heals Silas.",
                "Community, money against love, consequences of choices and faith are other themes.",
                "Gold and golden hair are linked images: cold wealth and warm love.",
                "Eliot's style: omniscient narrator, realism, humour, irony, dialect, sympathy.",
                "Use point, proof and meaning, and always give an example from the book."),
        ],
    ),
]

LESSONS += [
    # ------------------------------------------------------------------ 10. Exam: Paper 1
    lesson(
        module=M_EXAM, topic="Paper 1",
        title="Paper 1 strategy: 50 multiple-choice questions in Literature",
        slug="litx-paper1-strategy",
        minutes=22,
        summary="How to prepare for and sit Paper 1, the 50 multiple-choice questions: what is tested, how to revise each text, how to "
                "read a passage, how to remove wrong options and how to use your time.",
        objectives=[
            "State what Paper 1 is and what kinds of knowledge it tests",
            "Make a revision plan that covers the general skills and every prescribed text",
            "Read a passage and answer questions on technique with evidence",
            "Use elimination and time well, without leaving blanks",
        ],
        key_concepts=["Paper 1", "Multiple choice", "Elimination", "Context clue", "Revision grid", "Technique"],
        blocks=[
            H("Introduction"),
            T("Paper 1 is quick to take but cannot be passed by guessing. Fifty questions, each with four options, test what you have read and how well "
              "you can read. In Literature, they test two kinds of knowledge: general skills (genres, devices, tone, form) and the prescribed texts "
              "(who, what, where, why)."),
            D("**Paper 1** of the Ordinary Level Literature in English examination has 50 multiple-choice questions. All are to be answered. "
              "The Board's 2023 report says Paper 1 was marked electronically, so you must fill the answer sheet exactly as instructed.", title="What the Board says"),
            T("The report says the examination as a whole tests knowledge (about 60 percent), comprehension (about 30 percent) and application (about 10 percent). "
              "That means most questions ask you to recall facts about the texts and techniques, a good number ask you to understand a passage, and some ask you to apply what you "
              "know to something new. Because exact arrangements can change, check the instructions printed on your paper and ask your teacher about the current syllabus."),
            H("Two sets of knowledge"),
            KEY("What to revise", "Make a revision grid with both rows.", cards=[
                ["General skills", "Genres; plot structure; characterisation; setting; point of view; diction, tone and mood; irony and figures of speech; poetry terms (imagery, rhythm, rhyme, form, voice)."],
                ["Drama", "Macbeth (new) or As You Like It (old): plot, characters, themes, language, theatre."],
                ["African prose", "The Crown of Thorns or The Immortal Seed: events, characters, themes, techniques. Use your own copy."],
                ["Non-African prose", "Lord of the Flies or Silas Marner: events, characters, symbols, themes and style."],
                ["Poetry", "The prescribed anthology: speaker, subject, devices, tone and theme of each poem."],
            ]),
            TIP("Always check which texts your school teaches. The Board's 2023 report names an old set of texts and a new set. Revise the set your teacher has told you to study."),
            H("Reading a passage question"),
            T("Many Paper 1 questions give a short passage or poem and ask about it. Follow these steps."),
            EX("Read, mark, answer", intro="Read this short invented passage and answer the question that follows. "
               "'The market was loud with voices. Mama Ngozi sold her tomatoes as if each one were a small red sun, polished it, held it up, and sang its praise. "
               "Yet when the rain came she folded her stall in silence, and her face was the grey of the sky.' "
               "Question: What device is used in 'each one were a small red sun'?", steps=[
                S("Read the whole passage once", text="It is about a market seller who is lively, then silent in the rain."),
                S("Find the words in the question", text="'each one were a small red sun': a tomato is compared to a sun, using 'as if'."),
                S("Name the device", text="A tomato is compared with a sun, using the words 'as if'. A comparison that uses 'like', 'as' or 'as if' is a simile. "
                  "Personification (giving human actions to things) and irony (saying the opposite) do not fit."),
                S("Check", text="The tomato is not given human actions, and nothing is said opposite to what is meant. Choose simile."),
            ]),
            EX("Eliminate the wrong options", intro="Question: 'In the passage, the change from "
               "loud voices to silence shows a change in...' Options: A the market's prices; B Mama Ngozi's mood and fortune; C the number of buyers; D the colour of the sky.", steps=[
                S("Cross out what the passage does not say", text="Prices and numbers of buyers are not mentioned: remove A and C."),
                S("Compare the rest", text="The colour of the sky is described, but it is used to describe her face, not to answer a question about change in the voices."),
                S("Choose", text="B. The loud selling, then the silent folding of the stall, shows her mood changing with her luck."),
            ]),
            H("Questions on the prescribed texts"),
            T("Text questions are mostly short and factual. They may ask who said or did something, where an event takes place, the order of events, what a symbol stands for, "
              "or which theme a scene shows. The best preparation is to read the book, then to make short notes on each chapter or act: who, where, what happens, why it matters. "
              "The Board's report adds that teachers and students should own the original book and avoid substituting videos."),
            MISTAKE("Relying on a film or a summary", "Summaries and videos leave out details. A multiple-choice option often differs by one detail, and a film may change the detail."),
            MISTAKE("Choosing the first option that looks right", "Read all four. One option may be a half truth: right place, wrong character. Eliminate wrong options one at a time before choosing."),
            MISTAKE("Leaving blanks", "There is no reason to leave a question empty on a multiple-choice paper. If you are unsure, remove the options you know are wrong and choose from the rest. "
                    "Check the paper's instructions about marking."),
            TIP("Keep to a time plan. Our KKEVO practice settings use 90 minutes for a 50-question paper, which gives under two minutes a question. Answer the easy ones first, mark the hard ones and return."),
            qz("A question asks which option is NOT a feature of poetry. What should you do first?",
               "Read the question again and note the word NOT",
               [("Pick the first option you recognise", "With a NOT question, the first familiar feature is likely to be the wrong answer to choose."),
                ("Skip the question and leave it blank", "Blanks earn nothing; read carefully and answer."),
                ("Choose the longest option", "Length is not a sign of correctness.")],
               "Words like NOT, EXCEPT and LEAST change the question. Notice them first, then test each option.",
               hint="One small word reverses the question."),
            qz("Which is the best way to prepare for text questions in Paper 1?",
               "Read your own copy of each text and make notes on who, where, what and why",
               [("Watch a film of the story only", "The Board's report advises against relying on videos."),
                ("Learn only the characters' names", "Paper 1 asks about events, themes and techniques as well."),
                ("Learn the general skills only", "Paper 1 includes the prescribed texts.")],
               "Detailed knowledge of the actual book is the base of Paper 1 and Paper 2.",
               hint="Think about what the Board advises."),
            PQ("List the two kinds of knowledge tested in Paper 1 and give one example of each.",
               "General literary skills, for example naming a device such as irony or metaphor in a passage. Knowledge of the prescribed texts, for example knowing which character kills Piggy or which brother steals Silas's gold."),
            PQ("Explain how to answer a multiple-choice question when you are not sure.",
               "Read the question carefully, note words such as NOT, remove options that are clearly wrong, compare the rest with the passage or your knowledge of the text, then choose the best option. "
               "Do not leave it blank."),
            PQ("Why should students own and read the prescribed texts?",
               "The Board's 2023 report advises it. Paper 1 and Paper 2 test details and events that films and summaries leave out or change, and candidates who did not know the book mixed up events."),
            SUM("Paper 1 has 50 multiple-choice questions and is marked electronically.",
                "It tests general literary skills and the prescribed texts; most questions are on knowledge and comprehension.",
                "Revise with a grid: genres and devices, then each text.",
                "Read passages carefully, notice NOT and EXCEPT, and remove wrong options.",
                "Own and read the original books; do not rely on videos or summaries."),
        ],
    ),

    # ------------------------------------------------------------------ 11. Exam: Paper 2
    lesson(
        module=M_EXAM, topic="Paper 2",
        title="Paper 2 strategy: four sections, extracts and essays",
        slug="litx-paper2-strategy",
        minutes=24,
        summary="How to tackle Paper 2: the four sections (Drama, African literature, Poetry, Prose), planning an answer, "
                "reading an extract, staying with the text and avoiding the mistakes the Board reported.",
        objectives=[
            "Describe the structure of Paper 2 and the aim of each section",
            "Plan an answer with point, proof and meaning in a few minutes",
            "Place an extract in the text and answer its parts without mixing them up",
            "Avoid personal experience, retelling and mixed-up events",
        ],
        key_concepts=["Paper 2", "Extract", "Essay plan", "Point, proof, meaning", "Staying with the text", "Section A-D"],
        blocks=[
            H("Introduction"),
            T("Paper 2 is where you write. A mark in Paper 1 comes from choosing, but a mark in Paper 2 comes from explaining. "
              "The Board's report gives clear advice on what pleases examiners and what loses marks. This lesson turns that advice into a method."),
            D("**Paper 2** of Literature in English has four sections: **A** Drama (Shakespeare), **B** African literature (a novel), **C** Poetry (an anthology) and **D** Prose (a non-African novel). "
              "There are two questions in each section. The report says the paper is divided equally among the sections, and that most candidates in 2023 attempted questions from all four. "
              "Check the instructions on your paper for how many questions to answer.", title="The structure"),
            KEY("Texts by section", "The Board's 2023 report names these texts.", cards=[
                ["A Drama", "New syllabus: Macbeth. Old syllabus: As You Like It."],
                ["B African literature", "New: The Crown of Thorns (Linus T. Asong). Old: The Immortal Seed (Tah Protus)."],
                ["C Poetry", "New: a modern anthology (Hans Bokwe Itoe). Old: a Cameroon anthology (Bole Butake)."],
                ["D Prose", "New: Lord of the Flies (William Golding). Old: Silas Marner (George Eliot)."],
            ]),
            H("What the Board noticed"),
            KEY("Reasons for lost marks", "These points come from the Board's 2023 report, paraphrased.", cards=[
                ["Personal experience", "In poetry answers, candidates wrote about their own experiences or about the continent in general, instead of describing the poem."],
                ["Mixed-up events", "In a question on a play, candidates put the answer for one part into another part."],
                ["Cannot place the extract", "Candidates could not say where an account began and ended, for example an encounter at a river in an African novel."],
                ["Not knowing the whole text", "Questions on later parts of a text, or on style and themes, were avoided or done badly."],
                ["Weak knowledge of the book", "Candidates who did not own or read the text could not answer details. Videos are not a substitute."],
            ]),
            H("A method for essay questions"),
            EX("Plan in four steps", intro="Question: 'How does Golding show the conflict between Ralph and Jack?' Use this plan.", steps=[
                S("1. Read the question", text="Underline the key words: 'conflict', 'Ralph and Jack'. The answer is about the two boys, not about the whole story."),
                S("2. Collect points", text="Their aims differ (rescue and rules against hunting and power); the fire left unattended; Jack breaks Piggy's glasses; Jack leaves and forms a tribe; the hunt for Ralph."),
                S("3. Order the points", text="Use the order of the book: start, middle, end. One paragraph for each."),
                S("4. Write", text="Open with one sentence that answers the question. Each paragraph gives a point, proof from the text, and what it shows. Close with a short conclusion."),
            ]),
            TIP("Cross out your plan after finishing the answer, so it is not read as part of it (the Board's English Language report gives this advice for composition; check with your teacher for Literature). Keep the plan short: a few words for each point."),
            H("A method for extract questions"),
            T("An extract question gives a passage from the text and asks several parts. The first part usually asks where the extract comes from or what has just happened. "
              "Later parts ask about meaning, character, language or what happens next. The report noted that answers for different parts were mixed up, so label each part and read the wording carefully."),
            EX("Answer an extract question", intro="Invented extract (not from any set text): 'Efua put down the water pot and looked at the closed door. "
               "She had promised to wait, but the shadows were long and her brother had not returned.' Question: (a) What is Efua's mood? (b) Which words show it?", steps=[
                S("Part (a)", text="Anxious and worried: she is alone, waiting and watching."),
                S("Part (b)", text="'Looked at the closed door' shows her attention is fixed on the entry; 'the shadows were long' shows time passing; 'had not returned' states the cause of worry."),
                S("Keep the parts apart", text="Mood goes in (a), evidence in (b). Do not put the answer for one part in the other."),
                S("Stay with the passage", text="Do not write about a time when you waited for someone. Write about Efua."),
            ]),
            MISTAKE("Retelling the whole book", "An essay is an answer to a question. Use only the events that prove your point and explain what they show."),
            MISTAKE("Telling your own story", "Do not use personal experience or general talk about Africa or society as the main part of your answer. Use the text."),
            MISTAKE("Mixing up parts or characters", "Label (a), (b), (c) in your answer. Before writing, check which character and which scene each part asks about."),
            MISTAKE("Skipping a section", "Because the paper is divided into four equal sections, revise all four texts and do not rely on one."),
            qz("An invented poem describes a speaker who names her mother and her land with pride. A question asks for its theme. Which answer stays with the text?",
               "The poem shows pride in one's identity, as the speaker names her mother and her land",
               [("In my village we also love our land, and I remember my childhood", "This is personal experience; the question asks about the poem."),
                ("Africa is a continent with many people", "This is a general remark, not about the poem."),
                ("Poems are written in lines and stanzas", "This is true but does not answer the question.")],
               "A good answer names the theme and points to words or lines in the poem.",
               hint="Which answer talks about the poem itself?"),
            qz("Why should you label parts (a), (b) and (c) clearly in an extract answer?",
               "So that each answer is placed under the right question and not mixed up",
               [("Because examiners give marks for labels", "Labels help, but marks are for content."),
                ("So you can write less", "Labels do not reduce the work."),
                ("Because the paper requires roman numerals", "There is no such rule here.")],
               "The Board noted answers that were placed against the wrong part. Labels help you and the examiner.",
               hint="Think of the Macbeth mix-up in the report."),
            PQ("List the four sections of Paper 2 with the type of text in each.",
               "A Drama (a Shakespeare play), B African literature (a novel), C Poetry (an anthology), D Prose (a non-African novel). There are two questions in each section."),
            PQ("Describe a good method for planning an essay answer.",
               "Read the question and underline the key words. Collect points from the book. Put them in order. Write an opening sentence that answers the question, then paragraphs with point, proof and meaning, "
               "and a short conclusion. Cross out the plan afterwards."),
            PQ("Name two mistakes mentioned by the Board and say how to avoid them.",
               "Personal experience in place of the text: describe the poem or scene itself. Mixed-up events or parts: label your answers and check the scene each part asks about. "
               "Another mistake is not knowing where an extract begins and ends: know the order of events in your text."),
            SUM("Paper 2 has four sections (Drama, African literature, Poetry, Prose) with two questions in each; follow the instructions on your paper.",
                "Plan briefly: key words, points, order, then point-proof-meaning paragraphs.",
                "Place every extract in the story and answer each part separately.",
                "Stay with the text: no personal experience, no general talk.",
                "Own and know the books; the Board advises it."),
        ],
    ),
]
