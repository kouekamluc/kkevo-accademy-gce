"""Form 5 Religious Studies (O Level 0585), part 2: Synoptic Gospels II, the Early Church (Acts), Islamic Religious Studies and the Examination module.

Draft content, descriptive and respectful ("Christians believe", "Muslims believe"). Scripture is paraphrased and chapters
are cited only where certain; textbooks differ on several details and dates (marked "check your textbook"). Religious Studies
is not in the Board's 2023 report, so Paper 1 (50 multiple-choice questions) and Paper 2 (written paper on the sections
studied) follow the KKEVO blueprint; the exact format should be checked with the teacher.
"""

from .dsl import *  # noqa: F403

COURSE = ("religious-studies", "form-5")

M_S2 = "Synoptic Gospels II: Transfiguration, Passion & Resurrection"
M_AC = "The Early Church: Acts of the Apostles"
M_IS = "Islamic Religious Studies"
M_EX = "Examination"

LESSONS = [
    # ------------------------------------------------------------------ Synoptic II
    lesson(
        module=M_S2, topic="Peter's confession and the Transfiguration",
        title="Who is Jesus? Peter's confession and the Transfiguration",
        slug="rel2-peters-confession-transfiguration", minutes=20,
        summary="Jesus asks his disciples who people say he is; Peter answers that he is the Messiah. Days later Peter, James and John see Jesus in glory on a mountain with Moses and Elijah.",
        objectives=[
            "Describe the scene at Caesarea Philippi and Peter's answer to Jesus' question",
            "Explain why Jesus began to speak of his suffering after the confession",
            "Describe the Transfiguration: who was present, what was seen and what the voice said",
            "Explain what the Transfiguration means for Christians",
        ],
        key_concepts=["Messiah (Christ)", "Caesarea Philippi", "Transfiguration", "Moses and Elijah", "Peter, James and John", "Suffering Messiah"],
        blocks=[
            H("Introduction"),
            T("Imagine a teacher who stops on a long walk between towns and asks his students, \"What are people saying about me?\" "
              "Then he asks a harder question: \"And you, what do you say?\" This is how the story of Peter's confession begins. "
              "It is found in all three Synoptic Gospels (Mark, Matthew and Luke).\n\n"
              "The word **Synoptic** means \"seen together\". Mark, Matthew and Luke tell many of the same stories in a similar way. "
              "Most scholars think Mark was written first and that Matthew and Luke knew it. Because the three tell this story "
              "with small differences, it is useful to know what is shared and what is special to one Gospel."),
            D("The **Messiah** (in Greek, **Christ**) means \"the anointed one\", the promised king and deliverer whom the Jewish people expected. "
              "Christians believe that Jesus is the Messiah.", title="Messiah / Christ"),
            D("The **Transfiguration** is the event on a high mountain when the appearance of Jesus was changed before three disciples: his face and clothes shone, and "
              "Moses and Elijah appeared with him.", title="Transfiguration"),
            H("Peter's confession at Caesarea Philippi"),
            T("Jesus and his disciples were in the villages around **Caesarea Philippi**, a town in the north, far from Jerusalem. "
              "Jesus asked, \"Who do people say that I am?\" The disciples answered that some said John the Baptist, others Elijah, "
              "and others one of the prophets.\n\n"
              "Then Jesus asked, \"But who do you say that I am?\" **Peter** answered that Jesus is the Messiah. In Matthew's Gospel the answer is "
              "longer: \"the Messiah, the Son of the living God\". Matthew alone also records Jesus' reply that Peter is blessed and that on this "
              "\"rock\" he will build his church. Christians read this passage in different ways, so use your own textbook for the explanation your teacher expects.\n\n"
              "In all three Gospels Jesus told the disciples **not to tell anyone** yet. Many people expected a Messiah who would be a military ruler. "
              "Jesus wanted them to understand his mission first."),
            H("The first prediction of suffering"),
            T("Immediately after the confession Jesus began to teach that the Son of Man must suffer, be rejected by the elders, chief priests and teachers of the law, "
              "be killed and rise again on the third day. This is the first of his predictions of the Passion (his suffering and death).\n\n"
              "**Peter** took Jesus aside and protested. In Mark and Matthew Jesus answered him sharply, saying that Peter was thinking in human terms and not as God does. "
              "Jesus then told the crowd that anyone who wants to follow him must deny themselves, take up their cross and follow. "
              "So the confession shows who Jesus is, and the prediction shows what kind of Messiah he will be: a suffering one."),
            H("The Transfiguration"),
            T("About a week later (Mark and Matthew say \"six days\", Luke says \"about eight days\") Jesus took **Peter, James and John** up a high mountain. "
              "The Gospels do not name the mountain; textbooks name different places, so check your textbook. In Luke, Jesus went up to pray.\n\n"
              "There Jesus was **transfigured**. His face shone and his clothes became dazzling white. **Moses and Elijah** appeared and spoke with him. "
              "Luke adds that they spoke about his departure, which he was about to complete at Jerusalem.\n\n"
              "Peter, not knowing what to say, offered to build three shelters, one each for Jesus, Moses and Elijah. A bright cloud covered them and a voice said "
              "that Jesus is God's beloved Son and that the disciples should **listen to him**. Suddenly Moses and Elijah were gone and Jesus was alone with them. "
              "As they came down Jesus told them to tell no one until the Son of Man had risen from the dead."),
            KEY("What the Transfiguration means for Christians", "Four ideas are often given in answers.", cards=[
                ["Jesus is God's Son", "The voice from the cloud confirms what was said at his baptism and what Peter had said at Caesarea Philippi."],
                ["Law and prophets agree", "Moses stands for the Law and Elijah for the prophets. Their presence shows that Jesus fulfils what they taught."],
                ["Glory and suffering", "The glory comes just after the prediction of suffering. It prepares the three disciples for the cross."],
                ["Listen to him", "The disciples are told to listen to Jesus, including his words about suffering."],
            ]),
            IMG("f5rel-2-passion-timeline.svg",
                alt="A timeline of the events of the last week of Jesus' life from the entry into Jerusalem to the Resurrection.",
                caption="Figure 1. The events of the last week of Jesus' ministry, the sequence studied in this module. Peter's confession and the Transfiguration come before it."),
            QUIZ("At Caesarea Philippi, how did Peter answer Jesus' question \"Who do you say that I am?\"", [
                "You are John the Baptist come back", "You are the Messiah", "You are Elijah", "You are a good teacher"], 1,
                 "Peter said that Jesus is the Messiah (in Matthew, the Messiah, the Son of the living God).",
                 hint="Remember the difference between what people said and what Peter said.",
                 feedback=["That was one of the answers the crowds gave.", "", "That was also an answer from the crowds.", "Peter's answer was stronger than this."]),
            EX("Model answer plan 1", intro="Describe the Transfiguration of Jesus.", steps=[
                S("Introduction", text="Say that Jesus took Peter, James and John up a high mountain, after the confession at Caesarea Philippi and the first prediction of suffering."),
                S("The change", text="His face shone and his clothes became dazzling white."),
                S("The visitors", text="Moses and Elijah appeared and talked with him (Luke: about his departure at Jerusalem)."),
                S("Peter's reaction", text="Peter offered to build three shelters."),
                S("The cloud and the voice", text="A cloud covered them and the voice said that Jesus is the beloved Son and that they should listen to him."),
                S("The ending", text="Jesus was alone again and told them to tell no one until he had risen."),
            ]),
            EX("Model answer plan 2", intro="What is the importance of the Transfiguration for Christians?", steps=[
                S("Point 1", text="It confirms that Jesus is the Son of God, as at his baptism."),
                S("Point 2", text="Moses and Elijah show that Jesus completes the Law and the prophets."),
                S("Point 3", text="It encouraged the disciples before the cross, since glory and suffering belong together."),
                S("Point 4", text="It is a command to listen to Jesus."),
                S("Conclusion", text="For Christians, it shows who Jesus is and prepares the way for the Passion and the Resurrection."),
            ]),
            MISTAKE("Mixing up the two events", "Peter's confession is at Caesarea Philippi, before the Transfiguration. The voice from the cloud is not Peter's confession. Keep them in order: question, confession, prediction of suffering, Transfiguration."),
            MISTAKE("Naming the wrong disciples or prophets", "The three disciples on the mountain were Peter, James and John, and the two who appeared were Moses and Elijah. Do not add Andrew, and do not replace Elijah with John the Baptist."),
            TIP("Religious Studies Paper 1 asks for names, places and order of events. Paper 2 essays ask you to describe and explain. Check with your teacher which sections you must answer, as the exam format may differ.", title="Exam link"),
            QUIZ("Which three disciples went up the mountain with Jesus at the Transfiguration?", [
                "Peter, Andrew and Philip", "Peter, James and John", "James, John and Judas", "Peter, Matthew and Thomas"], 1,
                 "Peter, James and John were the three disciples who were closest to Jesus on special occasions.",
                 hint="Think of the two brothers who were sons of Zebedee and the disciple who spoke first.",
                 feedback=["Andrew and Philip were not with Jesus on the mountain.", "", "Judas was not on the mountain.", "Matthew and Thomas were not on the mountain."]),
            PQ("Why did Jesus tell his disciples not to tell anyone that he is the Messiah?", "Many people expected the Messiah to be a political or military ruler. Jesus wanted the disciples to understand first that his mission included suffering, rejection and death, and that he would rise again."),
            PQ("Name the two figures who appeared with Jesus at the Transfiguration and say what each stands for.", "Moses, who stands for the Law, and Elijah, who stands for the prophets. Their presence shows that Jesus fulfils the Law and the prophets."),
            PQ("What did the voice from the cloud say?", "It said that Jesus is God's beloved Son and told the disciples to listen to him."),
            PQ("Why did Peter protest when Jesus first spoke of his suffering?", "Peter had just confessed Jesus as Messiah and expected glory, not suffering and death. Jesus told him that he was thinking in human terms, and taught that followers must take up their cross."),
            SUM("At Caesarea Philippi Peter said that Jesus is the Messiah; people thought Jesus was John the Baptist, Elijah or a prophet.",
                "Jesus then foretold his suffering, death and rising, and called disciples to take up their cross.",
                "On a high mountain Peter, James and John saw Jesus transfigured with Moses and Elijah.",
                "A voice from the cloud said that Jesus is the beloved Son and that they should listen to him.",
                "For Christians it confirms who Jesus is and prepares his followers for the cross."),
        ],
    ),
    lesson(
        module=M_S2, topic="The Triumphal Entry and the Temple",
        title="Entry into Jerusalem, the Temple and the teaching on the last things",
        slug="rel2-triumphal-entry-temple", minutes=22,
        summary="Jesus enters Jerusalem on a colt to shouts of Hosanna, drives traders from the Temple, and teaches about the destruction of the Temple and the need to be watchful.",
        objectives=[
            "Describe the Triumphal Entry into Jerusalem and what the crowds did",
            "Explain the meaning of the colt and of the cry Hosanna",
            "Describe the cleansing of the Temple and why Jesus acted",
            "Outline the Eschatological Discourse and its message of watchfulness",
        ],
        key_concepts=["Triumphal Entry", "Hosanna", "Cleansing of the Temple", "Money changers", "Eschatological discourse", "Watchfulness"],
        blocks=[
            H("Introduction"),
            T("Picture the road into a large city on a market day: crowds, noise and a man riding a young donkey while people spread their cloaks in front of him. "
              "That is how the Gospels describe Jesus' arrival in **Jerusalem** at the time of the Passover festival, the last week before his death.\n\n"
              "This lesson follows three linked events: the entry into the city, the cleansing of the Temple, and the long teaching Jesus gave on the Mount of Olives."),
            D("The **Triumphal Entry** is the event in which Jesus rode into Jerusalem on a colt while crowds welcomed him as the one who comes in the name of the Lord.", title="Triumphal Entry"),
            D("**Hosanna** is a shout of praise that originally meant \"save us\". The crowds shouted it as Jesus came into Jerusalem.", title="Hosanna"),
            H("The Triumphal Entry"),
            T("Jesus approached Jerusalem from the east, near **Bethphage and Bethany** on the **Mount of Olives**. He sent two disciples to a village to fetch a **colt** "
              "that had never been ridden. They were to say, if asked, that the Lord needed it. The disciples threw their cloaks on the colt and Jesus sat on it.\n\n"
              "Many people spread their cloaks on the road and others spread branches cut from the fields or trees. They shouted \"Hosanna! Blessed is he who comes in the name of the Lord\". "
              "Mark and Matthew also mention a blessing on the coming kingdom of David. In Luke some Pharisees told Jesus to rebuke his disciples, and he answered that if they were silent the stones would cry out.\n\n"
              "Christians see the colt as a sign. A king who comes on a young donkey and not a war horse comes in peace and humility. Matthew links the event to a prophecy of Zechariah."),
            H("The cleansing of the Temple"),
            T("The **Temple** in Jerusalem was the centre of Jewish worship. In its outer court pilgrims needed to change their money into Temple coins and to buy animals and doves for sacrifice. "
              "These businesses were run in the Temple courts.\n\n"
              "Jesus entered the Temple and drove out those who were buying and selling. He overturned the tables of the **money changers** and the seats of the dove sellers. "
              "He quoted Scripture, saying that the Temple should be a house of prayer, but they had made it a \"den of robbers\". "
              "He would not let anyone carry goods through the Temple courts. The chief priests and teachers of the law heard this and began to look for a way to kill him, but they feared the crowd.\n\n"
              "Mark places the cleansing on the day after the entry, and Matthew and Luke place it on the same day. Textbooks differ on the order, so check yours."),
            KEY("Why did Jesus cleanse the Temple?", "Answers often given in textbooks:", cards=[
                ["Respect for God's house", "He wanted the Temple to be a place of prayer and not of business."],
                ["Against injustice", "The trading in the Temple courts was a burden on the worshippers, especially the poor."],
                ["A claim to authority", "His action challenged the Temple leaders and led them to plot against him."],
            ]),
            H("The Eschatological Discourse"),
            T("**Eschatology** means teaching about the last things. As Jesus left the Temple, a disciple admired its great stones. Jesus said that not one stone would be left on another. "
              "Later, on the **Mount of Olives**, Peter, James, John and Andrew asked privately when this would happen. The long answer is called the **Eschatological Discourse** (Mark 13, with parallels in Matthew and Luke).\n\n"
              "Jesus warned about false teachers, wars, earthquakes and persecution, and said that the good news must be preached to all nations. "
              "He taught that no one knows the day or the hour, so his followers must be **watchful**. The central message is: stay alert, be faithful and do not be led astray."),
            IMG("f5rel-2-passion-timeline.svg", alt="Timeline of the last week of Jesus, showing the entry into Jerusalem and the cleansing of the Temple near the start.", caption="Figure 1. Where this lesson fits in the last week."),
            QUIZ("What did the crowds put on the road as Jesus rode into Jerusalem?", [
                "Gold coins", "Their cloaks and branches", "Fish and bread", "Burning torches"], 1,
                 "The Gospels say that people spread their cloaks and branches on the road.",
                 hint="Think of how a crowd honoured an important visitor.",
                 feedback=["Gold is not mentioned.", "", "Fish and bread belong to the feeding miracles.", "Torches are not part of the story."]),
            EX("Model answer plan 1", intro="Describe the Triumphal Entry of Jesus into Jerusalem.", steps=[
                S("Setting", text="Passover time, near Bethphage and Bethany on the Mount of Olives."),
                S("The colt", text="Two disciples fetched a colt that had never been ridden; they put their cloaks on it and Jesus sat on it."),
                S("The crowd", text="People spread cloaks and branches on the road and shouted Hosanna and a blessing on the one who comes in the Lord's name."),
                S("The meaning", text="A king coming on a colt shows peace and humility."),
            ]),
            EX("Model answer plan 2", intro="Why did Jesus cleanse the Temple?", steps=[
                S("Describe the scene", text="He drove out buyers and sellers and overturned the tables of the money changers and the seats of the dove sellers."),
                S("His words", text="The Temple should be a house of prayer, but it had become a den of robbers."),
                S("Reasons", text="Respect for God's house; the poor were burdened; he claimed authority over the Temple."),
                S("Result", text="The chief priests and the teachers of the law began to plot against him."),
            ]),
            MISTAKE("Calling the donkey a horse or a war animal", "The Gospels say a colt, a young donkey. The point is peace and humility. Do not write \"a white horse\"."),
            MISTAKE("Saying Jesus destroyed the Temple", "Jesus cleared out the traders; he did not destroy the building. His words about the stones refer to a future destruction of the Temple."),
            TIP("In order-of-events questions, remember: entry on the colt, cleansing of the Temple, teaching on the Mount of Olives, then the Last Supper. Check with your teacher how many days each Gospel gives.", title="Exam link"),
            QUIZ("What was the main message of the Eschatological Discourse?", [
                "Stop all worship in the Temple", "Be watchful, for no one knows the day or the hour", "Pay the Temple tax earlier", "Build a new Temple"], 1,
                 "Jesus warned of troubles and told his followers to stay awake, since no one knows when the end will come.",
                 hint="Think of the word watchful.",
                 feedback=["Jesus objected to the trading, not to worship.", "", "That belongs to another story.", "Nothing in the discourse asks for a new building."]),
            PQ("Name two things the crowd did when Jesus entered Jerusalem.", "They spread their cloaks and branches on the road and shouted Hosanna, blessing the one who comes in the name of the Lord."),
            PQ("Who was driven out of the Temple, and whose tables were overturned?", "Those who bought and sold in the Temple courts were driven out; the tables of the money changers and the seats of those selling doves were overturned."),
            PQ("What does the word Hosanna mean?", "It means \"save us\", and became a shout of praise."),
            PQ("Give two lessons Christians learn from the Eschatological Discourse.", "Be watchful and faithful, since no one knows the day or the hour; do not be led astray by false teachers; the good news must be preached to all nations; persecution may come."),
            SUM("Jesus rode into Jerusalem on a colt; the crowds spread cloaks and branches and shouted Hosanna.",
                "The colt shows a king who comes in peace and humility.",
                "He cleansed the Temple by driving out traders and overturning the tables of the money changers.",
                "He taught that the Temple would fall and told his followers to be watchful.",
                "These events led the Temple leaders to plot against him."),
        ],
    ),
    lesson(
        module=M_S2, topic="The Last Supper and Gethsemane",
        title="The Last Supper, Gethsemane and the arrest",
        slug="rel2-last-supper-gethsemane", minutes=22,
        summary="At the Passover meal Jesus gives bread and wine a new meaning and foretells betrayal; in Gethsemane he prays in distress and is arrested after Judas' kiss.",
        objectives=[
            "Describe the Last Supper and the words Jesus spoke over the bread and the cup",
            "Explain the importance of the Lord's Supper (Holy Communion) for Christians",
            "Describe the prayer in Gethsemane and the arrest",
            "Explain the roles of Judas, Peter and the other disciples",
        ],
        key_concepts=["Last Supper", "Passover", "Covenant", "Holy Communion", "Gethsemane", "Judas' betrayal", "Arrest"],
        blocks=[
            H("Introduction"),
            T("Many families in Cameroon share a special meal on a big occasion, and what is said at the table is remembered for years. "
              "On the night before he died, Jesus ate a meal with his twelve disciples in Jerusalem. What he said and did there is remembered by Christians in worship every week.\n\n"
              "After the meal he went to a garden to pray. In this lesson we follow the meal, the prayer and the arrest."),
            D("The **Last Supper** is the final meal Jesus shared with his disciples before his arrest. The Synoptic Gospels describe it as a **Passover** meal, the Jewish festival that remembers the escape from slavery in Egypt.", title="Last Supper"),
            D("**Holy Communion** (also called the Lord's Supper, the Eucharist or the Mass) is the act of worship in which Christians share bread and wine in memory of Jesus. Different churches understand it in different ways.", title="Holy Communion"),
            H("Preparing the meal"),
            T("Jesus sent two disciples into the city to find a man carrying a jar of water. They were to follow him and ask the owner of the house for a guest room. "
              "There they prepared the Passover. In the evening Jesus sat with the Twelve."),
            H("The betrayal and the words over bread and cup"),
            T("During the meal Jesus said that one of the Twelve would betray him. The disciples were upset and each asked whether it was he. "
              "The one who betrayed him was **Judas Iscariot**, who had agreed with the chief priests to hand Jesus over. "
              "The Synoptic Gospels do not all say at the same moment that Judas left, so follow your textbook.\n\n"
              "Jesus **took bread**, gave thanks, broke it and gave it to them saying that this is his **body**. (Luke adds that it is given for them and that they should do this in memory of him.) "
              "Then he took a **cup**, gave thanks and gave it to them. He said that it is his **blood of the covenant**, poured out for many (Matthew adds \"for the forgiveness of sins\"). "
              "He said he would not drink the fruit of the vine again until the day he drinks it new in the kingdom of God.\n\n"
              "Jesus also warned that all the disciples would fall away and that **Peter** would deny him three times that very night. Peter insisted that he would never do so."),
            KEY("What the Lord's Supper means", "Christians often give these ideas.", cards=[
                ["Memory", "They remember Jesus' death and all he did."],
                ["New covenant", "The cup is the blood of the covenant. As the old covenant at Sinai was sealed with blood, Christians believe the new one is sealed by the death of Jesus."],
                ["Fellowship", "Believers share one bread and one cup and so are united with Christ and one another."],
                ["Hope", "Jesus spoke of drinking the cup new in God's kingdom."],
            ], note="Churches differ in how they explain the bread and the cup. State what Christians believe without ranking one church above another."),
            H("Gethsemane"),
            T("After singing a hymn, Jesus and the disciples went out to the **Mount of Olives** and to a place called **Gethsemane**, a garden. "
              "He took **Peter, James and John** further with him and said that his soul was deeply troubled. He asked them to stay and watch.\n\n"
              "Jesus went a little further and prayed on the ground: \"Father, if it is possible, take this cup from me. Yet not what I will, but what you will.\" "
              "He came back three times and found the disciples **asleep**. He told them to watch and pray so as not to fall into temptation.\n\n"
              "Luke adds that an angel strengthened him and that his sweat fell like drops of blood. Check which details are in which Gospel."),
            H("The arrest"),
            T("Judas arrived with a crowd armed with swords and clubs, sent by the chief priests, teachers of the law and elders. "
              "He had arranged a signal: \"The one I kiss is the man.\" He kissed Jesus. Jesus was seized. "
              "One of the disciples drew a sword and struck the servant of the high priest, cutting off his ear. "
              "Jesus told him to put the sword away (Luke adds that he healed the man). He asked why they came with weapons as if he were a robber, when he taught daily in the Temple. "
              "Then all the disciples left him and ran away."),
            QUIZ("What did Jesus say about the cup at the Last Supper?", [
                "It is the cup of the Passover lamb", "It is his blood of the covenant", "It is a cup for kings only", "It must not be drunk"], 1,
                 "Jesus described the cup as his blood of the covenant, poured out for many.",
                 hint="Think of the link between covenant and blood.",
                 feedback=["The meal was the Passover, but Jesus gave the cup a new meaning.", "", "The cup was shared by all the disciples.", "They all drank from it."]),
            EX("Model answer plan 1", intro="Describe what happened at the Last Supper.", steps=[
                S("Setting", text="A Passover meal in an upper room prepared by two disciples."),
                S("Betrayal foretold", text="Jesus said that one of the Twelve would betray him."),
                S("Bread", text="He took bread, gave thanks, broke it and said that it was his body."),
                S("Cup", text="He gave the cup and said that it was his blood of the covenant, poured out for many."),
                S("Warnings", text="All would fall away; Peter would deny him three times."),
            ]),
            EX("Model answer plan 2", intro="Describe the arrest of Jesus.", steps=[
                S("Gethsemane", text="Jesus prayed and found the disciples asleep three times."),
                S("Judas arrives", text="With a crowd with swords and clubs from the chief priests, teachers of the law and elders."),
                S("The kiss", text="Judas greeted Jesus with a kiss as the agreed sign."),
                S("The sword", text="A disciple struck the high priest's servant; Jesus told him to put his sword away."),
                S("The result", text="All the disciples ran away."),
            ]),
            MISTAKE("Saying Judas betrayed Jesus by himself", "The Gospels say Judas agreed with the chief priests, who sent the crowd. Write that Judas led them and identified Jesus with a kiss."),
            MISTAKE("Forgetting who was awake", "The disciples were asleep while Jesus prayed. Peter, James and John were closest to him. Do not write that they prayed with him."),
            TIP("In Paper 1 expect questions on the names (Judas Iscariot, Peter), places (Mount of Olives, Gethsemane) and objects (bread, cup, kiss, sword). In essays, link the meal to the covenant.", title="Exam link"),
            QUIZ("What did Jesus pray in Gethsemane?", [
                "That the disciples would stay awake", "That the cup would be taken away if possible, yet God's will be done", "That Judas would be punished", "That he would be made king"], 1,
                 "He asked that the cup of suffering be taken away if possible, and accepted the will of the Father.",
                 hint="The prayer ends with obedience.",
                 feedback=["He asked them to stay awake but that was not the heart of the prayer.", "", "He did not pray against Judas.", "He did not ask to be king."]),
            PQ("Name the sign used by Judas to point out Jesus.", "He kissed Jesus."),
            PQ("What did Jesus tell Peter at the Last Supper?", "He said that all the disciples would fall away and that Peter would deny him three times before the cock crowed that night."),
            PQ("Give two reasons why Holy Communion is important to Christians.", "It remembers the death of Jesus; it renews the covenant; it unites believers with Christ and one another; it looks forward to God's kingdom."),
            PQ("What can Christians learn from the prayer in Gethsemane?", "That Jesus was truly human and troubled, that he prayed, and that he accepted God's will; Christians are encouraged to pray in hard times and to trust God."),
            SUM("The Last Supper was a Passover meal with the Twelve.",
                "Jesus foretold the betrayal by one of them and the denial by Peter.",
                "He gave the bread as his body and the cup as his blood of the covenant.",
                "In Gethsemane he prayed that God's will be done while the disciples slept.",
                "Judas led the crowd and kissed him; Jesus was arrested and the disciples fled."),
        ],
    ),
    lesson(
        module=M_S2, topic="The trials and the crucifixion",
        title="The trials of Jesus and the crucifixion",
        slug="rel2-trials-crucifixion", minutes=24,
        summary="Jesus is tried by the Jewish council and by Pilate, Peter denies him, Barabbas is released, and Jesus is crucified at Golgotha and dies.",
        objectives=[
            "Put the trials of Jesus in order: the Jewish council, Pilate (and Herod in Luke)",
            "Describe Peter's denial and the release of Barabbas",
            "Describe the crucifixion and the events at the cross",
            "Explain what the death of Jesus means for Christians",
        ],
        key_concepts=["Sanhedrin", "Caiaphas", "Pontius Pilate", "Peter's denial", "Barabbas", "Golgotha", "Crucifixion", "Centurion"],
        blocks=[
            H("Introduction"),
            T("The story of the last hours of Jesus is the centre of the Gospels. It is told with great care, and the order of events matters. "
              "In Paper 1 you may be asked who tried Jesus, who denied him, who was released instead of him and what happened at the cross.\n\n"
              "In this lesson we follow the story in order, from the night of the arrest to the death of Jesus. Read it calmly and respectfully, as many Christians in Cameroon do each year on Good Friday."),
            D("The **Sanhedrin** was the Jewish council in Jerusalem, made up of chief priests, elders and teachers of the law. Its head was the high priest, **Caiaphas** at the time of the trial of Jesus.", title="Sanhedrin"),
            D("**Pontius Pilate** was the Roman governor of Judea. Only the Roman governor could order an execution, so the leaders brought Jesus to him.", title="Pilate"),
            D("**Crucifixion** was a Roman form of execution in which a person was fixed to a cross.", title="Crucifixion"),
            H("Before the Jewish council"),
            T("Jesus was taken to the house of the high priest, where the chief priests, elders and teachers of the law gathered. "
              "Witnesses were called, but their accounts did not agree. At last the high priest asked, \"Are you the Messiah, the Son of the Blessed One?\" "
              "In Mark Jesus answered, \"I am\", and said that they would see the Son of Man seated at the right hand of the Power and coming with the clouds of heaven. "
              "The high priest tore his robes and the council declared that he deserved death. Some spat on him and struck him.\n\n"
              "In Luke the council meets at daybreak. Because the Romans controlled capital punishment, the council took Jesus to Pilate."),
            H("Peter's denial"),
            T("While Jesus was being questioned, **Peter** was in the courtyard of the high priest, warming himself at a fire. A servant girl said that he had been with Jesus. "
              "Peter denied it. He denied it **three times**, the third time with an oath. Then a **cock crowed**, Peter remembered Jesus' words and he went out and wept bitterly."),
            H("Before Pilate"),
            T("Early in the morning the leaders handed Jesus to Pilate. They accused him of claiming to be a king, which would be a charge against Rome. "
              "Pilate asked, \"Are you the king of the Jews?\" Jesus answered, \"You say so\". Pilate found no case worth the death penalty. "
              "In **Luke only**, Pilate sent Jesus to **Herod Antipas**, the ruler of Galilee, who was in Jerusalem; Herod mocked him and sent him back.\n\n"
              "It was the custom at the festival for the governor to release one prisoner. A prisoner named **Barabbas**, who had been jailed for rebellion and murder, was in prison. "
              "Pilate offered the crowd the choice. Stirred up by the chief priests, the crowd asked for Barabbas and shouted for Jesus to be crucified. "
              "Pilate, afraid of a riot, released Barabbas and had Jesus flogged and handed over to be crucified. In Matthew Pilate washed his hands and said he was innocent of this man's blood."),
            H("The way to the cross and the crucifixion"),
            T("The soldiers dressed Jesus in a purple robe, put a crown of thorns on his head and mocked him as king of the Jews. "
              "As they led him out, they forced **Simon of Cyrene**, who was coming in from the country, to carry his cross.\n\n"
              "At **Golgotha**, \"the place of the skull\", they crucified him with two criminals, one on each side. The soldiers divided his clothes by casting lots. "
              "The notice over his head said \"The King of the Jews\". Passers-by and the leaders mocked him. In **Luke only**, Jesus prayed, \"Father, forgive them\", and one of the criminals asked Jesus to remember him in his kingdom, and Jesus promised that he would be with him in paradise.\n\n"
              "From noon until three in the afternoon, **darkness** came over the land. Jesus cried out in a loud voice, in Mark and Matthew, \"My God, my God, why have you forsaken me?\", which opens a psalm. "
              "In Luke his last words are \"Father, into your hands I commit my spirit\". Then he died. The **curtain of the Temple** was torn in two. "
              "The Roman **centurion** who stood facing him said that this man was truly the Son of God (Luke: innocent). Women who had followed him from Galilee watched from a distance."),
            IMG("f5rel-2-passion-timeline.svg", alt="Timeline of the last week of Jesus; the trials and the crucifixion come near the end.", caption="Figure 1. The trials and the crucifixion in the sequence of the last week."),
            KEY("Why Christians say the death of Jesus matters", "Common points in answers:", cards=[
                ["Sacrifice for sins", "Christians believe Jesus died for the forgiveness of sins."],
                ["Obedience and love", "He accepted death in obedience to the Father and out of love."],
                ["Torn curtain", "Many Christians understand the torn Temple curtain as a sign that people can come close to God."],
                ["Example", "He forgave those who crucified him."],
            ]),
            QUIZ("Who was released instead of Jesus?", ["Simon of Cyrene", "Barabbas", "Caiaphas", "Joseph of Arimathea"], 1,
                 "Pilate released Barabbas, a prisoner charged with rebellion and murder, when the crowd asked for him.",
                 hint="The custom was to free a prisoner at the festival.",
                 feedback=["Simon carried the cross.", "", "Caiaphas was the high priest.", "Joseph of Arimathea buried Jesus."]),
            EX("Model answer plan 1", intro="Describe the trials of Jesus.", steps=[
                S("Before the council", text="Jesus was questioned by the Sanhedrin under the high priest; false witnesses disagreed; he was condemned for claiming to be the Messiah."),
                S("Peter's denial", text="Meanwhile Peter denied Jesus three times before the cock crowed."),
                S("Before Pilate", text="Jesus was accused of claiming to be king; Pilate found no case."),
                S("Herod (Luke only)", text="Pilate sent him to Herod Antipas, who mocked him."),
                S("The verdict", text="The crowd chose Barabbas; Pilate had Jesus flogged and handed over to be crucified."),
            ]),
            EX("Model answer plan 2", intro="Describe the crucifixion of Jesus.", steps=[
                S("The route", text="Soldiers mocked him; Simon of Cyrene carried his cross."),
                S("Golgotha", text="Jesus was crucified between two criminals; the notice said King of the Jews."),
                S("Darkness", text="Darkness fell from noon until three."),
                S("The death", text="He cried out and died; the Temple curtain was torn."),
                S("Witnesses", text="The centurion declared that he was the Son of God (Luke: innocent); the women watched."),
            ]),
            MISTAKE("Putting the order wrong", "The Jewish council came first, then Pilate. Herod appears only in Luke. Do not put Herod in an answer about Mark or Matthew."),
            MISTAKE("Blaming one group", "The Gospels name the temple leaders, the crowd and Pilate; Jesus himself was Jewish and so were his disciples. Do not say that all Jews or any people today are to blame. Write about the individuals named."),
            TIP("Expect Paper 1 questions on Caiaphas, Pilate, Barabbas, Simon of Cyrene and Golgotha, and Paper 2 essays on the significance of the death of Jesus. Learn the names carefully.", title="Exam link"),
            QUIZ("Who carried the cross of Jesus?", ["Peter", "Simon of Cyrene", "Barabbas", "Pilate's soldier"], 1,
                 "Soldiers forced Simon of Cyrene, who was coming in from the country, to carry it.",
                 hint="He came from Cyrene in North Africa.",
                 feedback=["Peter had denied Jesus and was in hiding.", "", "Barabbas was freed.", "The soldiers forced a passer-by to do it."]),
            PQ("Name the Jewish leader who presided over the council and the Roman governor who judged Jesus.", "The high priest Caiaphas and Pontius Pilate."),
            PQ("What were the three things Peter did in the courtyard?", "He denied that he knew Jesus three times; then the cock crowed and he wept bitterly."),
            PQ("Mention four events at the crucifixion.", "Soldiers divided his clothes; the notice King of the Jews; darkness from noon till three; the Temple curtain was torn; the centurion's confession; Jesus' last cry."),
            PQ("Why do Christians say that Jesus' death was important?", "Christians believe he died for the forgiveness of sins, in obedience and love, opening the way to God, and as an example of forgiveness."),
            SUM("Jesus was tried by the Jewish council, then by Pilate (and Herod in Luke).",
                "Peter denied him three times before the cock crowed.",
                "The crowd chose Barabbas and Pilate handed Jesus over to be crucified.",
                "He was crucified at Golgotha between two criminals; darkness fell and the Temple curtain was torn.",
                "Christians believe his death brings forgiveness and opens the way to God."),
        ],
    ),
    lesson(
        module=M_S2, topic="The burial and the Resurrection",
        title="The burial and the Resurrection of Jesus",
        slug="rel2-burial-resurrection", minutes=24,
        summary="Joseph of Arimathea buries Jesus; women find the tomb empty on the first day of the week and are told that he is risen; the Gospels tell of appearances and of the call to go to all nations.",
        objectives=[
            "Describe the burial of Jesus by Joseph of Arimathea",
            "Describe the discovery of the empty tomb by the women",
            "Outline the main appearances and commissions in the Synoptic Gospels",
            "Explain what the Resurrection means for Christians",
        ],
        key_concepts=["Joseph of Arimathea", "Empty tomb", "Resurrection", "Easter", "Emmaus road", "Great Commission", "Mary Magdalene"],
        blocks=[
            H("Introduction"),
            T("Easter is the most important festival for Christians. Churches in Cameroon hold services before dawn on Easter morning, with singing and the greeting that Christ is risen. "
              "This lesson studies the Gospel accounts of what happened after the death of Jesus.\n\n"
              "The Synoptic Gospels agree on the main points, the burial, the empty tomb and the message of the resurrection, but they differ in some details. Learn the common story first and then the special points of each Gospel."),
            D("The **Resurrection** is the Christian belief that God raised Jesus from the dead on the third day after his crucifixion. It is the central belief of the Christian faith.", title="Resurrection"),
            H("The burial"),
            T("It was Friday, the day of preparation before the Sabbath. **Joseph of Arimathea**, a respected member of the council who was waiting for the kingdom of God (Luke: a good and righteous man who had not agreed to the council's decision), went boldly to **Pilate** and asked for the body of Jesus. "
              "Pilate, surprised that Jesus was already dead, checked with the centurion and then allowed it.\n\n"
              "Joseph took down the body, wrapped it in **linen cloth** and laid it in a **tomb cut out of the rock**, in which no one had yet been laid. "
              "He rolled a **large stone** across the entrance. The women who had followed Jesus from Galilee, including Mary Magdalene, watched where the body was laid. "
              "Because the Sabbath was beginning, they planned to bring spices afterwards. In Matthew only, the chief priests and Pharisees asked Pilate for guards and sealed the stone."),
            H("The empty tomb"),
            T("Very early on the **first day of the week**, the women went to the tomb with spices. In Mark they are Mary Magdalene, Mary the mother of James and Salome. "
              "They wondered who would roll the stone away, but found it already rolled back. "
              "In Mark a young man in a white robe told them not to be afraid: Jesus of Nazareth, who was crucified, has risen and is not here. He told them to tell the disciples and Peter that Jesus is going ahead of them into Galilee. "
              "In Matthew an earthquake occurs and an angel rolls the stone back; in Luke two men in shining clothes speak to the women. "
              "The women left, afraid and amazed. Luke says they told the apostles, who thought it was nonsense; Peter ran to the tomb and saw the linen cloths.\n\n"
              "Most scholars note that the oldest manuscripts of Mark end at this point, with the fear of the women, and that the verses that follow were added later. Your textbook will tell you which verses to use; check with your teacher."),
            H("The risen Lord appears"),
            T("**Matthew:** the women met Jesus on the way and he told them to tell the disciples to go to Galilee. On a mountain in Galilee Jesus gave the **Great Commission**: go and make disciples of all nations, baptising them in the name of the Father, the Son and the Holy Spirit, and teaching them to obey his commands, and he promised to be with them always. "
              "The guards were bribed to say that the disciples had stolen the body.\n\n"
              "**Luke:** two disciples were walking to a village called **Emmaus** when Jesus joined them. They did not recognise him until he broke bread with them. They returned at once to Jerusalem. "
              "Then Jesus appeared to the group, showed his hands and feet and ate a piece of fish, to show he was not a ghost. He explained the Scriptures and told them to wait in Jerusalem until they were clothed with power from on high. "
              "Luke ends with the blessing and the Ascension at Bethany."),
            KEY("What the Resurrection means for Christians", "These ideas are often used in answers:", cards=[
                ["Victory over death", "Christians believe that God raised Jesus and that death does not have the last word."],
                ["Jesus is confirmed", "God confirmed that Jesus is the Son of God and that his teaching and sacrifice are true."],
                ["New life and hope", "Believers hope for life after death and for new life now."],
                ["Mission", "The risen Lord sends his followers to all nations."],
            ]),
            QUIZ("Who asked Pilate for the body of Jesus?", ["Simon of Cyrene", "Joseph of Arimathea", "Caiaphas", "Barabbas"], 1,
                 "Joseph of Arimathea, a member of the council, asked Pilate for the body and buried Jesus.",
                 hint="He came from the town of Arimathea and had a rock-cut tomb.",
                 feedback=["Simon carried the cross.", "", "Caiaphas was the high priest.", "Barabbas was freed instead of Jesus."]),
            EX("Model answer plan 1", intro="Describe the burial of Jesus.", steps=[
                S("When", text="On Friday, before the Sabbath began."),
                S("Joseph", text="Joseph of Arimathea, a member of the council, asked Pilate for the body."),
                S("The tomb", text="He wrapped the body in linen and laid it in a rock tomb, then rolled a large stone across the entrance."),
                S("The women", text="The women watched where he was laid."),
                S("Matthew only", text="Guards were posted and the stone sealed."),
            ]),
            EX("Model answer plan 2", intro="Describe the discovery of the empty tomb.", steps=[
                S("Time", text="Very early on the first day of the week."),
                S("The women", text="They came with spices; Mary Magdalene was among them."),
                S("The stone", text="They found it already rolled away."),
                S("The message", text="A young man or angel said that Jesus was risen and told them to tell the disciples."),
                S("Their response", text="They were afraid and amazed; in Luke they told the apostles, who did not believe at first."),
            ]),
            MISTAKE("Saying that the disciples first saw the tomb empty", "In all three Gospels the women came first. Do not say that Peter or the Twelve were the first to find it empty."),
            MISTAKE("Mixing up the details of the Gospels", "The guards at the tomb and the Great Commission on a mountain are in Matthew; the Emmaus road is in Luke. Learn which story belongs to which Gospel."),
            TIP("Paper 1 asks who, where and which Gospel; Paper 2 essays ask you to describe the story and to explain its meaning. Ask your teacher which longer ending of Mark your syllabus uses.", title="Exam link"),
            QUIZ("Which Gospel tells of the walk to Emmaus?", ["Mark", "Matthew", "Luke", "None of the Synoptic Gospels"], 2,
                 "The story of the two disciples on the road to Emmaus is in Luke.",
                 hint="It is the Gospel that ends with the Ascension at Bethany.",
                 feedback=["Mark's oldest text ends with the fear of the women.", "Matthew has the meeting on the mountain in Galilee.", "", "It is in Luke."]),
            PQ("Name the women who went to the tomb in Mark's Gospel.", "Mary Magdalene, Mary the mother of James, and Salome."),
            PQ("What did the Great Commission tell the disciples to do?", "To go and make disciples of all nations, baptising them in the name of the Father, the Son and the Holy Spirit, and teaching them to obey Jesus' commands."),
            PQ("Why did the two disciples at Emmaus recognise Jesus?", "They recognised him when he broke bread with them, after he had explained the Scriptures to them on the road."),
            PQ("State two reasons why the Resurrection is important for Christians.", "It shows that God has power over death and confirms Jesus as God's Son; it gives hope of life after death; it began the mission of the church."),
            SUM("Joseph of Arimathea buried Jesus in a rock tomb and a large stone was rolled across it.",
                "On the first day of the week the women found the tomb empty and were told that he was risen.",
                "Matthew ends with the Great Commission in Galilee; Luke tells of the Emmaus road and the Ascension.",
                "Christians believe in the Resurrection as God's victory over death.",
                "The risen Lord sends his followers to all nations."),
        ],
    ),
    # ------------------------------------------------------------------ Acts
    lesson(
        module=M_AC, topic="The Ascension and Pentecost",
        title="The Ascension and the day of Pentecost",
        slug="rel2-ascension-pentecost", minutes=20,
        summary="The risen Jesus is taken up into heaven after promising the Holy Spirit; ten days later, at Pentecost, the Spirit comes on the believers in Jerusalem and the church begins to grow.",
        objectives=[
            "Describe the Ascension and the promise of the Holy Spirit",
            "Describe how Matthias was chosen to replace Judas",
            "Describe the events of Pentecost and Peter's sermon",
            "Explain why Pentecost is called the birthday of the church",
        ],
        key_concepts=["Acts of the Apostles", "Ascension", "Holy Spirit", "Matthias", "Pentecost", "Tongues", "Peter's sermon"],
        blocks=[
            H("Introduction"),
            T("The **Acts of the Apostles** is the fifth book of the New Testament. It tells how the church grew from a small group in Jerusalem to communities around the Roman world. "
              "Christian tradition says that the author is **Luke**, the same person who wrote the third Gospel; the books are addressed to a man called Theophilus.\n\n"
              "Acts begins where Luke's Gospel ends: with the risen Jesus and his promise. In this lesson we study the Ascension, the choice of Matthias and the day of Pentecost."),
            D("The **Ascension** is the departure of the risen Jesus from his disciples, when he was taken up into heaven. Christians remember it on Ascension Day, forty days after Easter.", title="Ascension"),
            D("**Pentecost** was a Jewish harvest festival held fifty days after Passover. For Christians it is also the day when the Holy Spirit came on the believers.", title="Pentecost"),
            H("The Ascension"),
            T("For forty days after his suffering, Jesus appeared to the apostles and spoke about the kingdom of God. He told them not to leave Jerusalem but to wait for the gift his Father had promised, the **Holy Spirit**. "
              "He said, \"You will receive power when the Holy Spirit comes on you, and you will be my witnesses in Jerusalem, in all Judea and Samaria, and to the ends of the earth.\" "
              "This verse is often used as the outline of Acts.\n\n"
              "As they were watching, Jesus was taken up and a cloud hid him. Two men in white said that Jesus would come back in the same way as he had gone. "
              "The apostles returned to Jerusalem from the **Mount of Olives** and gathered in an upstairs room, where they prayed with the women, with Mary the mother of Jesus and with his brothers."),
            H("The choice of Matthias"),
            T("Judas, who had betrayed Jesus, was dead, so the group of Twelve had a place to fill. Peter explained that the replacement must be a man who had been with them from the baptism of John to the Ascension and who could be a witness to the resurrection. "
              "Two men were named: **Joseph called Barsabbas** and **Matthias**. After prayer they cast lots and the lot fell to Matthias, who was counted with the eleven apostles."),
            H("The day of Pentecost"),
            T("When the day of **Pentecost** came, the believers were all together in one place. Suddenly a sound like a strong wind filled the house. Tongues like fire appeared and rested on each of them. "
              "They were all filled with the **Holy Spirit** and began to speak in other languages, as the Spirit enabled them.\n\n"
              "Jews from many nations were in Jerusalem for the festival. They heard the believers speaking in their own languages about the wonders of God and were amazed. "
              "Some mocked and said the believers were drunk. Peter stood up with the eleven and said that it was only nine in the morning."),
            H("Peter's sermon"),
            T("Peter explained that this was the fulfilment of the prophecy of Joel, that God would pour out his Spirit on all people. "
              "He then spoke about Jesus of Nazareth, whom they had crucified and whom God had raised up, and said that God had made him Lord and Messiah. "
              "The people were deeply moved and asked what they should do. Peter told them to **repent and be baptised** in the name of Jesus for the forgiveness of sins, and they would receive the gift of the Holy Spirit. "
              "About **three thousand** people were baptised that day."),
            IMG("f5rel-2-acts-spread.svg", alt="A diagram showing the spread of the church in Acts: Jerusalem, Judea and Samaria, then the ends of the earth.", caption="Figure 1. The outline of Acts from the promise of Jesus: Jerusalem, Judea and Samaria, the ends of the earth."),
            KEY("Why Pentecost is important", "Christians often say that Pentecost is the birthday of the church because:", cards=[
                ["The Spirit came", "The believers were filled with the Holy Spirit as Jesus had promised."],
                ["Boldness", "Frightened disciples became brave witnesses."],
                ["All nations", "People of many languages heard the good news."],
                ["Growth", "About three thousand were baptised on the first day."],
            ]),
            QUIZ("How many days after Passover was the festival of Pentecost?", ["Seven", "Forty", "Fifty", "One hundred"], 2,
                 "The word Pentecost points to fifty days after Passover (forty days is the time from the resurrection to the Ascension).",
                 hint="Pente means fifty.",
                 feedback=["Seven is the number of days in a week.", "Forty is the time between resurrection and Ascension.", "", "Not the number used."]),
            EX("Model answer plan 1", intro="Describe the events of the day of Pentecost.", steps=[
                S("The gathering", text="The believers were together in one place."),
                S("The signs", text="A sound like a strong wind and tongues like fire resting on each of them."),
                S("The gift", text="They were filled with the Holy Spirit and spoke in other languages."),
                S("The crowd", text="Jews from many nations heard them in their own languages; some thought they were drunk."),
                S("The sermon", text="Peter preached and about three thousand were baptised."),
            ]),
            EX("Model answer plan 2", intro="Describe how Matthias became an apostle.", steps=[
                S("The need", text="Judas had died, so a replacement was needed."),
                S("The conditions", text="He had to be with them since John's baptism and a witness to the resurrection."),
                S("The candidates", text="Joseph Barsabbas and Matthias."),
                S("The choice", text="After prayer they cast lots and Matthias was chosen."),
            ]),
            MISTAKE("Giving the wrong number or festival", "Pentecost was fifty days after Passover and three thousand were baptised. Do not write forty days (the Ascension) or five thousand (the feeding miracle)."),
            MISTAKE("Saying Paul was chosen to replace Judas", "Matthias replaced Judas. Paul (Saul) appears later and was not one of the Twelve."),
            TIP("Paper 1 asks for names and numbers (Matthias, fifty days, three thousand). Paper 2 asks you to describe Pentecost and explain its meaning. Check with your teacher which sections you must answer.", title="Exam link"),
            QUIZ("What did Peter tell the crowd to do at Pentecost?", ["Return to their homes", "Repent and be baptised", "Leave Jerusalem", "Fast for forty days"], 1,
                 "Peter told them to repent and be baptised in the name of Jesus for the forgiveness of sins.",
                 hint="Think of what a person does to join the church.",
                 feedback=["He did not send them away.", "", "The apostles were told to stay in Jerusalem.", "No fasting is commanded in this passage."]),
            PQ("What did Jesus promise before he ascended?", "That the apostles would receive power when the Holy Spirit came on them and that they would be his witnesses in Jerusalem, Judea and Samaria and to the ends of the earth."),
            PQ("Who replaced Judas, and how was he chosen?", "Matthias; the believers prayed and cast lots between him and Joseph Barsabbas."),
            PQ("Name two signs at Pentecost.", "A sound like a strong wind; tongues like fire resting on each person; speaking in other languages."),
            PQ("Why is Pentecost called the birthday of the church?", "It was when the Spirit came on the believers, Peter preached boldly, and about three thousand were baptised, so the church began to grow."),
            SUM("Acts continues the story of Luke's Gospel and begins with the risen Jesus.",
                "Jesus promised the Holy Spirit and was taken up into heaven.",
                "Matthias replaced Judas among the Twelve.",
                "At Pentecost the Spirit came with wind and fire, the believers spoke in other languages, and Peter preached.",
                "About three thousand were baptised that day."),
        ],
    ),
    lesson(
        module=M_AC, topic="Life in the early church",
        title="Life in the early church: sharing, healing and conflict",
        slug="rel2-life-early-church", minutes=22,
        summary="The first believers met for teaching, fellowship, bread and prayer and shared their goods; Ananias and Sapphira lied about a gift; the apostles healed and were arrested; seven helpers were chosen.",
        objectives=[
            "Describe the daily life of the first Christians in Jerusalem",
            "Describe how they shared their property, including the example of Barnabas",
            "Tell the story of Ananias and Sapphira and what it teaches",
            "Describe the healing at the Beautiful Gate, the arrests and the appointment of the seven",
        ],
        key_concepts=["Fellowship", "Sharing property", "Barnabas", "Ananias and Sapphira", "The Beautiful Gate", "The Seven", "Persecution"],
        blocks=[
            H("Introduction"),
            T("In many Cameroonian communities, people in a village, a church or an association meet regularly, eat together and help a member in need. "
              "The first Christians in Jerusalem lived in a way that looks familiar. After Pentecost they formed a close community.\n\n"
              "This lesson studies how that community lived, how it was tested from inside (Ananias and Sapphira) and from outside (arrests), and how it was organised when it grew."),
            D("**Fellowship** (in Greek, *koinonia*) means sharing life together: shared worship, meals, goods and care for one another.", title="Fellowship"),
            H("A community of faith"),
            T("Acts 2 says that the believers devoted themselves to four things: the **apostles' teaching**, the **fellowship**, the **breaking of bread** and the **prayers**. "
              "Many wonders and signs were done through the apostles. They met in the Temple courts every day and broke bread in their homes. They praised God and enjoyed the favour of all the people. "
              "The Lord added to their number daily those who were being saved.\n\n"
              "They had everything in common. They sold property and possessions and gave to anyone who had need. Acts 4 says that no one among them was in need. "
              "A man named **Joseph**, a Levite from Cyprus whom the apostles called **Barnabas**, which means \"son of encouragement\", sold a field and laid the money at the apostles' feet."),
            H("Ananias and Sapphira"),
            T("**Ananias** and his wife **Sapphira** also sold a piece of property. But they kept back part of the money for themselves and brought the rest as if it were the whole amount. "
              "Peter said that the property was theirs to keep and the money theirs to use, so they had not been forced to give. Their sin was that they **lied** to the Holy Spirit and to God. "
              "When Ananias heard this he fell down and died. About three hours later Sapphira repeated the lie and she also died. "
              "Great fear seized the whole church and all who heard of it.\n\n"
              "The lesson is about honesty before God and the church, not about the size of the gift. Many Christians also see here a warning that hypocrisy harms the community. The story shows how seriously the early church took truthfulness."),
            H("The Beautiful Gate and the arrest"),
            T("Peter and John were going up to the Temple at the hour of prayer, about three in the afternoon. At the gate called **Beautiful** sat a man lame from birth who begged. "
              "Peter said, \"Silver and gold I do not have, but what I do have I give you. In the name of Jesus Christ of Nazareth, walk.\" He took the man's hand, and the man jumped up, walked and praised God. "
              "A crowd gathered and Peter preached to them in Solomon's Colonnade.\n\n"
              "The priests, the captain of the Temple guard and the Sadducees arrested Peter and John, who were teaching about the resurrection. Next day they were questioned by the council, the **Sanhedrin**. "
              "Peter, filled with the Holy Spirit, said that the man was healed in the name of Jesus and that there is no other name by which we must be saved. "
              "The council ordered them not to speak in the name of Jesus. Peter and John replied that they must obey God rather than people. They were released, because the people were praising God for the miracle."),
            H("The Seven"),
            T("As the number of disciples grew, the Greek-speaking Jewish believers complained that their widows were being overlooked in the daily distribution of food. "
              "The Twelve called the whole group and said that they should not give up preaching to wait on tables. They asked the community to choose **seven men** known to be full of the Spirit and wisdom. "
              "The seven, all with Greek names, included **Stephen** and **Philip**. The apostles prayed and laid hands on them. The word of God spread and the number of disciples increased greatly."),
            KEY("What can the church learn from the first community?", "Lessons often drawn by Christians:", cards=[
                ["Worship and prayer", "Teaching, fellowship, bread and prayer were the centre of their life."],
                ["Sharing", "They cared for the poor within the community."],
                ["Honesty", "Ananias and Sapphira show the need for truthfulness."],
                ["Courage", "Peter and John obeyed God even when threatened."],
                ["Organisation", "The Seven were chosen so that the apostles could preach."],
            ]),
            QUIZ("What was the sin of Ananias and Sapphira?", ["They refused to sell their land", "They lied about the amount they gave", "They stole from the apostles", "They stopped coming to the Temple"], 1,
                 "They sold a property but kept back part of the money while pretending they gave all.",
                 hint="Peter said the property was theirs to keep.",
                 feedback=["Nobody forced them to sell.", "", "The money was theirs.", "Attendance is not mentioned."]),
            EX("Model answer plan 1", intro="Describe the life of the early Christians in Jerusalem.", steps=[
                S("Activities", text="They devoted themselves to the apostles' teaching, fellowship, the breaking of bread and prayer."),
                S("Sharing", text="They sold property and gave to those in need; Barnabas sold a field."),
                S("Worship", text="They met in the Temple courts and broke bread in homes."),
                S("Growth", text="The Lord added to their number daily."),
            ]),
            EX("Model answer plan 2", intro="What happened at the Beautiful Gate?", steps=[
                S("Setting", text="Peter and John went to the Temple at the hour of prayer."),
                S("The man", text="A lame man begged at the gate called Beautiful."),
                S("The healing", text="Peter said, in the name of Jesus, walk; the man walked and praised God."),
                S("Result", text="A crowd gathered, Peter preached, and the two were arrested and questioned by the Sanhedrin."),
            ]),
            MISTAKE("Saying that sharing was compulsory", "Peter told Ananias that the land was his to keep. Sharing was voluntary; the sin was lying."),
            MISTAKE("Mixing up the Ananias of this story with the other Ananias", "Ananias the husband of Sapphira is in Acts 5. Another Ananias, a disciple in Damascus, later helped Saul. Do not confuse them."),
            TIP("Expect Paper 1 questions on Barnabas, Ananias and Sapphira, the Beautiful Gate and the Seven. In Paper 2, use these stories to describe and discuss Christian community. Ask your teacher about the format.", title="Exam link"),
            QUIZ("Why were the Seven chosen?", ["To replace Judas", "So that the apostles could keep preaching while others served the widows", "To lead the Temple worship", "To travel to Rome"], 1,
                 "A complaint about the neglect of widows led the apostles to appoint seven men to oversee the food distribution.",
                 hint="Think of the word waiting on tables.",
                 feedback=["Matthias replaced Judas.", "", "The Seven did not lead Temple worship.", "They were appointed in Jerusalem."]),
            PQ("What does the name Barnabas mean, and what did he do?", "It means son of encouragement; he sold a field and gave the money to the apostles."),
            PQ("Why did Ananias and Sapphira die?", "They lied to the Holy Spirit by pretending they had given the whole price of the land while secretly keeping back part."),
            PQ("What did Peter and John say to the Sanhedrin when they were told to stop speaking about Jesus?", "That they must obey God rather than human beings and could not stop speaking about what they had seen and heard."),
            PQ("Give two lessons about community from Acts 2 to 6.", "Believers shared with the poor; they met for prayer and teaching; they were honest; they organised service by choosing helpers."),
            SUM("The first Christians shared teaching, fellowship, bread and prayer and cared for the poor.",
                "Barnabas gave generously; Ananias and Sapphira lied about their gift and died.",
                "Peter healed a lame man at the Beautiful Gate in the name of Jesus.",
                "Peter and John were arrested and said they must obey God.",
                "Seven men were chosen to serve the widows, including Stephen and Philip."),
        ],
    ),
    lesson(
        module=M_AC, topic="Stephen and the conversion of Saul",
        title="Stephen the martyr and the conversion of Saul",
        slug="rel2-stephen-conversion-saul", minutes=24,
        summary="Stephen is stoned for his witness, with Saul approving; on the road to Damascus the risen Jesus meets Saul, who becomes Paul, the great missionary to the Gentiles.",
        objectives=[
            "Describe Stephen's arrest, speech and martyrdom",
            "Explain the role of Saul in Stephen's death and in the persecution",
            "Describe Saul's conversion on the road to Damascus",
            "Describe the part played by Ananias and Barnabas",
        ],
        key_concepts=["Martyr", "Stephen", "Saul of Tarsus", "Road to Damascus", "Ananias of Damascus", "Barnabas", "Gentiles"],
        blocks=[
            H("Introduction"),
            T("Some people change the direction of their lives completely. The story of Saul is one of the most famous. "
              "He began as a fierce opponent of the church and became its greatest missionary. His change began on the day a young man named Stephen was killed for his faith.\n\n"
              "This lesson studies the death of Stephen and the conversion of Saul."),
            D("A **martyr** is a person who dies because of their faith. The Greek word means \"witness\". Stephen is called the first Christian martyr.", title="Martyr"),
            D("**Gentiles** are people who are not Jews.", title="Gentiles"),
            H("Stephen"),
            T("**Stephen** was one of the Seven chosen in Jerusalem. He was full of faith and the Holy Spirit and did great wonders among the people. "
              "Members of a synagogue argued with him but could not match his wisdom. They then persuaded people to say that they had heard him speak against Moses and against God, and against the Temple and the Law. "
              "He was seized and brought before the Sanhedrin, where false witnesses spoke against him. His face looked like the face of an angel.\n\n"
              "Asked by the high priest if the charges were true, Stephen made a long speech. He went through the history of Israel, from Abraham to Moses and Solomon, and said that God's people had always resisted the Holy Spirit and had killed the prophets. "
              "He accused his hearers of having betrayed and murdered the Righteous One. They were furious."),
            H("The martyrdom of Stephen"),
            T("Stephen looked up and said he saw the heavens open and the Son of Man standing at the right hand of God. The crowd covered their ears, rushed at him, dragged him out of the city and **stoned** him. "
              "The witnesses laid their coats at the feet of a young man named **Saul**, who approved of his death.\n\n"
              "As they stoned him, Stephen prayed, \"Lord Jesus, receive my spirit\". He fell on his knees and cried out, \"Lord, do not hold this sin against them.\" Then he died. "
              "Godly men buried him and made great lamentation over him. On that day a great persecution broke out against the church in Jerusalem, and all except the apostles were scattered through Judea and Samaria. "
              "As they scattered, they preached the word wherever they went; for example, **Philip** preached in Samaria and met an Ethiopian official on the road to Gaza."),
            H("Saul of Tarsus"),
            T("Saul was born in **Tarsus** in Cilicia. He was a Jew of the tribe of Benjamin, a **Pharisee** who had studied in Jerusalem under the teacher **Gamaliel**. "
              "He was also a **Roman citizen**. His Hebrew name was Saul, and later he is called Paul in Acts, the name he used in the Greek-speaking world. "
              "After Stephen's death he tried to destroy the church, going from house to house to drag out men and women and put them in prison. He obtained letters from the high priest to the synagogues in **Damascus** so that he could arrest any followers of the Way and bring them back to Jerusalem."),
            H("The road to Damascus"),
            T("As Saul came near Damascus, suddenly a **light from heaven** flashed around him. He fell to the ground and heard a voice: \"Saul, Saul, why do you persecute me?\" "
              "He asked, \"Who are you, Lord?\" The voice answered, \"I am Jesus, whom you are persecuting. Now get up and go into the city, and you will be told what you must do.\" "
              "His companions heard the sound but saw no one. When Saul got up, he was **blind**. They led him by the hand into Damascus, and for three days he could not see and did not eat or drink.\n\n"
              "In Damascus there was a disciple named **Ananias** (not the husband of Sapphira). The Lord told him in a vision to go to Saul. Ananias was afraid because of Saul's reputation, but the Lord said that Saul was his chosen instrument to carry his name to the **Gentiles**, to kings and to the people of Israel. "
              "Ananias placed his hands on Saul, called him \"Brother Saul\", and something like scales fell from his eyes. Saul could see again, got up and was **baptised**. He soon began to preach in the synagogues that Jesus is the Son of God."),
            H("After the conversion"),
            T("The Jews in Damascus plotted to kill Saul, but his followers lowered him in a **basket** through an opening in the city wall by night. "
              "In Jerusalem the disciples were afraid of him until **Barnabas** took him to the apostles and told them how Saul had seen the Lord and spoken boldly in Damascus. "
              "Saul then preached boldly in Jerusalem, and when the Greek-speaking Jews tried to kill him the believers sent him off to Tarsus. The church throughout Judea, Galilee and Samaria then had peace and grew."),
            KEY("Why does the conversion of Saul matter?", "Points often made:", cards=[
                ["A real change", "A persecutor became a believer by an encounter with the risen Lord."],
                ["Grace", "Christians say that God's call can reach anyone."],
                ["Mission to the Gentiles", "Saul became the apostle to the Gentiles."],
                ["Stephen's influence", "Many readers see Stephen's death and prayer as a seed of this change."],
            ]),
            QUIZ("What was Saul doing when he met Jesus on the road?", ["Travelling to Damascus to arrest believers", "Preaching in Tarsus", "Sailing to Rome", "Leading the Seven"], 0,
                 "He was travelling to Damascus with letters from the high priest to arrest believers.",
                 hint="Think of his role after Stephen's death.",
                 feedback=["", "He was not yet preaching.", "That journey happened much later.", "He was an opponent of the church at the time."]),
            EX("Model answer plan 1", intro="Describe the death of Stephen.", steps=[
                S("Arrest", text="He was accused by false witnesses of speaking against Moses, the Temple and the Law."),
                S("Speech", text="He reviewed Israel's history and said that his hearers resisted the Holy Spirit."),
                S("Vision", text="He saw heaven open and the Son of Man at God's right hand."),
                S("Stoning", text="He was dragged out and stoned; the witnesses laid their coats at Saul's feet."),
                S("Last words", text="He asked the Lord to receive his spirit and not to hold the sin against them."),
            ]),
            EX("Model answer plan 2", intro="Describe the conversion of Saul.", steps=[
                S("Background", text="Saul persecuted the church after Stephen's death and went to Damascus to arrest believers."),
                S("The vision", text="A light from heaven; the voice said, Saul, why do you persecute me?"),
                S("The result", text="He was blind and was led into Damascus."),
                S("Ananias", text="Ananias laid hands on him, he regained sight and was baptised."),
                S("The mission", text="He began to preach that Jesus is the Son of God and became the apostle to the Gentiles."),
            ]),
            MISTAKE("Calling Paul one of the Twelve", "Paul was not one of the Twelve. He became an apostle through his meeting with the risen Lord."),
            MISTAKE("Saying the name changed on the road", "Acts does not say that his name was changed on the road to Damascus. Saul (Hebrew) and Paul (Roman) were both his names. Acts begins to use Paul in the story of the first journey."),
            TIP("Learn the order: Stephen's death, persecution, Saul on the road to Damascus, Ananias, the basket, Barnabas. In Paper 1 the name of the man who laid hands on Saul is often asked.", title="Exam link"),
            QUIZ("Who introduced Saul to the apostles in Jerusalem?", ["Ananias", "Barnabas", "Philip", "Stephen"], 1,
                 "Barnabas took Saul to the apostles and told them of his conversion.",
                 hint="The name means son of encouragement.",
                 feedback=["Ananias helped him in Damascus.", "", "Philip preached in Samaria.", "Stephen had already died."]),
            PQ("Why was Stephen arrested?", "He was accused of speaking against Moses, the Law and the Temple."),
            PQ("What part did Saul play in Stephen's death?", "He approved of it; the witnesses laid their coats at his feet."),
            PQ("Give three details of Saul's conversion.", "A light from heaven; a voice saying Saul, Saul, why do you persecute me; he was blind for three days; Ananias laid hands on him and baptised him."),
            PQ("What can Christians learn from Stephen's death?", "To be faithful to Christ even when they suffer, and to forgive enemies as Stephen prayed for those who killed him."),
            SUM("Stephen, one of the Seven, was accused falsely, spoke before the Sanhedrin and was stoned.",
                "Saul approved of his death and led the persecution of the church.",
                "On the road to Damascus Saul met the risen Jesus and was blinded.",
                "Ananias healed and baptised him and Barnabas introduced him to the apostles.",
                "Saul became the apostle to the Gentiles."),
        ],
    ),
    lesson(
        module=M_AC, topic="Peter's ministry and the Council of Jerusalem",
        title="Peter's ministry, Cornelius and the Council of Jerusalem",
        slug="rel2-peter-ministry-council-jerusalem", minutes=24,
        summary="Peter heals Aeneas and raises Tabitha, brings the good news to the Gentile Cornelius, is rescued from prison, and the Council of Jerusalem decides that Gentile believers need not be circumcised.",
        objectives=[
            "Describe Peter's miracles at Lydda and Joppa",
            "Describe the vision of Peter and the conversion of Cornelius",
            "Describe Peter's arrest and rescue under Herod Agrippa",
            "Explain why the Council of Jerusalem met and what it decided",
        ],
        key_concepts=["Aeneas and Tabitha", "Cornelius", "Peter's vision", "Gentile Christians", "Circumcision", "Council of Jerusalem", "James"],
        blocks=[
            H("Introduction"),
            T("A young church in a new country faces a big question: who belongs? In Cameroon, churches welcome people of many languages and communities. "
              "The first believers were all Jews, and many assumed that a person had to become a Jew to follow Jesus. Peter's meeting with a Roman officer and the Council of Jerusalem answered that question.\n\n"
              "This lesson studies Peter's ministry and the first great church meeting."),
            D("**Circumcision** is the cutting of the foreskin, the sign of the covenant with Abraham for Jewish men. The question was whether non-Jewish men who believed in Jesus had to be circumcised.", title="Circumcision"),
            D("A **Gentile** is a person who is not a Jew. **Gentile Christians** are non-Jewish believers.", title="Gentile Christians"),
            H("Peter's miracles at Lydda and Joppa"),
            T("Peter travelled round the country and visited believers at **Lydda**, where he found a man named **Aeneas**, paralysed for eight years. Peter said, \"Jesus Christ heals you. Get up.\" He got up at once, and all who lived in Lydda turned to the Lord.\n\n"
              "At the port of **Joppa** a disciple named **Tabitha** (in Greek, **Dorcas**) was known for helping the poor and making clothes. She became ill and died. The believers sent for Peter. In the upstairs room, widows showed him the clothes she had made. "
              "Peter sent them out, knelt and prayed, and then said, \"Tabitha, get up.\" She opened her eyes and sat up. Many believed in the Lord. Peter stayed a long time in Joppa with Simon, a tanner."),
            H("Cornelius and Peter's vision"),
            T("In **Caesarea** lived **Cornelius**, a Roman **centurion** who feared God, prayed and gave generously to the poor. An angel told him to send for Peter. "
              "Meanwhile, at about noon, Peter was praying on the roof in Joppa. He fell into a trance and saw a large sheet coming down from heaven with all sorts of animals, birds and reptiles. A voice told him to kill and eat. "
              "Peter refused, since he had never eaten anything impure. The voice said, \"Do not call anything impure that God has made clean.\" This happened three times.\n\n"
              "Messengers arrived from Cornelius, and the Spirit told Peter to go with them. In Caesarea Cornelius had gathered his relatives and close friends. Peter said that God had shown him that he should not call anyone impure or unclean, and that God shows no favouritism. "
              "While he was speaking about Jesus, the Holy Spirit came on all who heard. The Jewish believers who had come with Peter were astonished that the gift was poured out on Gentiles. Peter ordered that they be **baptised**. "
              "When Peter returned to Jerusalem some criticised him, but after he explained they praised God for granting repentance to the Gentiles."),
            H("Peter in prison"),
            T("King **Herod Agrippa I** began to persecute the church. He had **James**, the brother of John, killed with the sword and, seeing that this pleased the Jews, arrested Peter during the Festival of Unleavened Bread. "
              "Peter was guarded by four squads of soldiers and chained between two soldiers. The church prayed earnestly. The night before the trial an **angel** woke Peter, his chains fell off and he walked past the guards through an iron gate that opened by itself. "
              "He went to the house of Mary, the mother of John Mark, where many were praying. A servant girl named Rhoda recognised his voice, but in her joy forgot to open the door. At first they did not believe her. "
              "Peter told them to tell James and the others and left for another place."),
            H("The Council of Jerusalem"),
            T("At **Antioch**, in Syria, some men from Judea taught that Gentile believers could not be saved unless they were **circumcised** according to the law of Moses. After a sharp dispute, **Paul and Barnabas** and others were sent to Jerusalem to discuss it with the apostles and elders.\n\n"
              "At the council some believers who had been Pharisees insisted that Gentiles must be circumcised and keep the law of Moses. **Peter** reminded them that God had chosen him to bring the good news to the Gentiles and had given them the Holy Spirit, and that all are saved by the grace of the Lord Jesus. "
              "Barnabas and Paul reported the signs and wonders God had done among the Gentiles. **James**, the leader of the Jerusalem church, quoted the prophets and gave his judgement: they should not make it difficult for the Gentiles who turn to God.\n\n"
              "A letter was sent with Judas Barsabbas and Silas to Antioch. It said that the Gentile believers should not be burdened beyond a few necessary things: to **abstain from food offered to idols, from blood, from the meat of strangled animals and from sexual immorality**. "
              "The church at Antioch rejoiced at the encouragement. The date of the council is often given as around AD 49; check your textbook."),
            IMG("f5rel-2-acts-spread.svg", alt="A diagram of the spread of the church in Acts, from Jerusalem to Judea and Samaria and to the ends of the earth.", caption="Figure 1. The church moves outward, and the Council of Jerusalem settles whether Gentiles must become Jews."),
            KEY("Why did the council matter?", "Reasons often given:", cards=[
                ["One church", "Jews and Gentiles could belong together without Gentiles first becoming Jews."],
                ["Grace", "People are saved by the grace of the Lord Jesus, not by keeping the Law."],
                ["Unity and care", "A few simple requests helped Jews and Gentiles to eat together."],
                ["Mission", "It opened the way for Paul's journeys among the Gentiles."],
            ]),
            QUIZ("Who was the Roman centurion at Caesarea who received the Holy Spirit?", ["Cornelius", "Herod", "Sergius Paulus", "Julius"], 0,
                 "Cornelius was the centurion who feared God and sent for Peter.",
                 hint="His name begins with C.",
                 feedback=["", "Herod was a king.", "Sergius Paulus was the proconsul in Cyprus.", "Julius was the centurion who took Paul to Rome."]),
            EX("Model answer plan 1", intro="Describe Peter's vision at Joppa and its results.", steps=[
                S("The vision", text="On the roof, Peter saw a sheet with all kinds of animals and heard a voice telling him to kill and eat."),
                S("Peter's refusal", text="He said he had never eaten anything unclean; the voice said not to call anything impure that God has made clean."),
                S("The visitors", text="Messengers from Cornelius arrived and the Spirit told Peter to go."),
                S("At Caesarea", text="Peter preached; the Holy Spirit came on the Gentiles and they were baptised."),
                S("Meaning", text="God shows no favouritism; the Gentiles are welcome."),
            ]),
            EX("Model answer plan 2", intro="Why was the Council of Jerusalem held and what did it decide?", steps=[
                S("The problem", text="Some taught that Gentile believers had to be circumcised and keep the law of Moses."),
                S("The delegates", text="Paul and Barnabas went from Antioch to Jerusalem."),
                S("The speeches", text="Peter and Barnabas and Paul described God's work among the Gentiles, and James gave the verdict."),
                S("The decision", text="Gentiles need not be circumcised; they were asked to avoid food offered to idols, blood, strangled meat and sexual immorality."),
                S("The result", text="A letter was sent to Antioch and the church was glad."),
            ]),
            MISTAKE("Confusing the two Jameses", "James the brother of John was killed by Herod Agrippa. James the leader of the Jerusalem church gave the verdict at the council. Textbooks differ on who exactly this second James was, so check yours."),
            MISTAKE("Saying the council made the law of Moses binding", "The council decided that Gentiles did not need to be circumcised. It did not require them to keep the whole law."),
            TIP("Paper 1 may ask where Cornelius lived (Caesarea), who healed Aeneas (Peter) and what the council decided. For Paper 2, plan your answer in order of events.", title="Exam link"),
            QUIZ("What was the main decision of the Council of Jerusalem?", ["Gentile believers must be circumcised", "Gentile believers need not be circumcised", "Only Jews may be baptised", "Paul must leave Antioch"], 1,
                 "The council decided not to make it difficult for the Gentiles who turn to God; they were asked to follow a few simple requests.",
                 hint="Remember the words of James.",
                 feedback=["That was the view of the men who caused the dispute.", "", "Cornelius had already been baptised.", "Nothing like this was decided."]),
            PQ("Name the two people Peter healed or raised from the dead in Lydda and Joppa.", "Aeneas, a paralysed man, was healed at Lydda; Tabitha (Dorcas) was raised to life at Joppa."),
            PQ("What did the vision of the sheet teach Peter?", "That God had made Gentiles clean and that Peter should not call anyone impure or unclean."),
            PQ("Describe how Peter escaped from prison.", "An angel woke him, the chains fell off, he walked past the guards and the iron gate opened; he went to the house of Mary, where Rhoda recognised his voice."),
            PQ("List the things the Gentile Christians were asked to avoid.", "Food offered to idols, blood, the meat of strangled animals and sexual immorality."),
            SUM("Peter healed Aeneas at Lydda and raised Tabitha at Joppa.",
                "His vision of the sheet taught him that God had made Gentiles clean; he baptised Cornelius at Caesarea.",
                "Herod Agrippa killed James and arrested Peter, but an angel freed him.",
                "The Council of Jerusalem decided that Gentiles need not be circumcised.",
                "A letter asked them to avoid idol food, blood, strangled meat and sexual immorality."),
        ],
    ),
    lesson(
        module=M_AC, topic="Paul's missionary journeys and the voyage to Rome",
        title="Paul's three journeys and his voyage to Rome",
        slug="rel2-paul-journeys-voyage-rome", minutes=25,
        summary="Paul and his companions carry the good news from Antioch across Cyprus, Asia Minor, Greece and Ephesus; after his arrest in Jerusalem he appeals to Caesar and is shipwrecked on the way to Rome.",
        objectives=[
            "Outline the first journey with Barnabas: Cyprus, Pisidian Antioch, Iconium, Lystra and Derbe",
            "Outline the second journey: Philippi, Thessalonica, Athens and Corinth",
            "Outline the third journey: Ephesus and the farewell at Miletus",
            "Describe Paul's arrest, his appeal to Caesar and the voyage and shipwreck",
        ],
        key_concepts=["Antioch", "Barnabas and Silas", "Lystra", "Philippi", "Athens", "Ephesus", "Appeal to Caesar", "Shipwreck at Malta"],
        blocks=[
            H("Introduction"),
            T("Paul travelled thousands of kilometres by sea and on foot, often in danger. Today a journey from Douala to Yaounde takes a few hours by bus; for Paul, each journey took months and years. "
              "The book of Acts follows his three journeys and his journey to Rome as a prisoner.\n\n"
              "Learn each journey by its companions, its main places and one or two key events. Use the map or sketch in your textbook and check all the dates, which differ in books."),
            D("A **missionary journey** is a journey made to carry the Christian message to new places. Paul's journeys began from **Antioch** in Syria, where believers were first called Christians.", title="Missionary journey"),
            IMG("f5rel-2-paul-journeys.svg", alt="A flow chart of the three journeys of Paul, with the main places and companions for each, ending with the voyage to Rome.", caption="Figure 1. A schematic of Paul's journeys (not a map)."),
            H("The first journey"),
            T("The church at Antioch, guided by the Holy Spirit, sent out **Barnabas and Saul**, with **John Mark** as helper. They sailed to **Cyprus**, where Elymas the sorcerer tried to turn the proconsul **Sergius Paulus** from the faith. Elymas was struck blind and the proconsul believed. "
              "From this point Acts calls Saul **Paul**. John Mark left them and returned to Jerusalem.\n\n"
              "In **Pisidian Antioch** Paul preached in the synagogue; many believed, but jealous leaders drove them out, and they turned to the Gentiles. At **Iconium** they met opposition. "
              "At **Lystra** Paul healed a man lame from birth and the crowd took Paul and Barnabas for the gods Hermes and Zeus. Paul told them they were only human. Then Jews from Antioch and Iconium won over the crowd; Paul was **stoned** and left for dead, but he got up and went on to **Derbe**. "
              "They returned, strengthening the churches and appointing elders, and reported to Antioch. After this the Council of Jerusalem met."),
            H("The second journey"),
            T("Paul and Barnabas disagreed over taking John Mark. Barnabas took Mark to Cyprus and Paul chose **Silas**. At Lystra **Timothy** joined them. In **Troas** Paul saw a vision of a man of **Macedonia** asking for help, and they crossed to Europe.\n\n"
              "At **Philippi** they met **Lydia**, a dealer in purple cloth who worshipped God; she was baptised with her household. Paul and Silas were beaten and jailed after Paul freed a slave girl from a spirit. At midnight, while they were praying and singing, an earthquake opened the doors; the jailer asked what he must do to be saved and he and his family were baptised.\n\n"
              "In **Thessalonica** and **Berea** they preached in synagogues; the Bereans were praised for examining the Scriptures. In **Athens** Paul spoke at the **Areopagus**, referring to an altar \"to an unknown god\". Some mocked, some believed. "
              "In **Corinth** he stayed about eighteen months, working with **Aquila and Priscilla**, tentmakers. He then sailed back to Antioch via Ephesus."),
            H("The third journey"),
            T("Paul went through Galatia and Phrygia and settled in **Ephesus** for about three years. He taught daily in a lecture hall, and many miracles were done. Many who practised magic burned their scrolls. "
              "A silversmith named **Demetrius**, who made silver shrines of the goddess **Artemis (Diana)**, stirred up a riot because the new faith threatened his trade. The town clerk calmed the crowd.\n\n"
              "Paul then went to Macedonia and Greece. At **Troas** a young man named **Eutychus** fell asleep during a long sermon, fell from a window and was taken up dead; Paul restored him. "
              "At **Miletus** Paul called the elders of Ephesus and gave an emotional farewell speech, warning them to guard the flock. He wept with them and sailed for Jerusalem."),
            H("Arrest and appeal to Caesar"),
            T("In Jerusalem some Jews accused Paul of teaching against the Law and the Temple. A mob seized him in the Temple, and the Roman commander rescued him. Paul spoke to the crowd in Hebrew about his conversion, and used his **Roman citizenship** to avoid a flogging. "
              "He was taken to **Caesarea**, where he was kept for two years under the governors **Felix** and **Festus** and defended himself before **King Agrippa**. When Festus wanted to send him back to Jerusalem, Paul used his right as a Roman citizen and said, \"I appeal to Caesar!\""),
            H("The voyage to Rome"),
            T("Paul was put on a ship with other prisoners under a centurion named **Julius**. **Luke** and Aristarchus travelled with him. At Fair Havens in **Crete** Paul advised them to stay for the winter, but the officers decided to sail on. "
              "A fierce north-easterly storm, \"the northeaster\", drove the ship for fourteen days. Paul told them that an angel had promised that no life would be lost, though the ship would be wrecked.\n\n"
              "The ship ran aground and broke up. Everyone, 276 people, reached land safely on the island of **Malta**. The islanders were kind. A viper fastened on Paul's hand but he shook it into the fire and was not harmed, and the people thought he was a god. "
              "Paul healed the father of Publius, the chief official, and others. After three months they sailed in another ship, reached **Rome**, and Paul was allowed to live under guard in his own rented house for **two years**, welcoming all who came and preaching the kingdom of God with boldness. Acts ends there."),
            QUIZ("With whom did Paul begin the first missionary journey?", ["Silas and Timothy", "Barnabas and John Mark", "Luke and Aristarchus", "Aquila and Priscilla"], 1,
                 "Paul set out with Barnabas, helped by John Mark, from Antioch.",
                 hint="The second journey was with Silas.",
                 feedback=["That is the second journey.", "", "They were with Paul on the voyage to Rome.", "He worked with them in Corinth."]),
            EX("Model answer plan 1", intro="Describe the events of Paul's stay at Philippi.", steps=[
                S("Arrival", text="After the vision at Troas, Paul, Silas and Timothy crossed to Macedonia and reached Philippi."),
                S("Lydia", text="Lydia, a dealer in purple cloth, believed and was baptised with her household."),
                S("Imprisonment", text="After Paul freed a slave girl from a spirit, Paul and Silas were beaten and jailed."),
                S("Earthquake", text="At midnight, while they sang, an earthquake opened the doors."),
                S("The jailer", text="The jailer and his family believed and were baptised."),
            ]),
            EX("Model answer plan 2", intro="Describe the voyage of Paul to Rome.", steps=[
                S("Departure", text="Paul left Caesarea as a prisoner under the centurion Julius."),
                S("The storm", text="A fierce wind drove the ship for fourteen days."),
                S("The shipwreck", text="The ship ran aground and all 276 reached land at Malta."),
                S("At Malta", text="The viper did him no harm and he healed the sick."),
                S("Arrival", text="He reached Rome and preached under guard for two years."),
            ]),
            MISTAKE("Mixing up the journeys", "Barnabas is with Paul on the first, Silas on the second; Ephesus is the main place of the third. Match each companion and key place to the right journey."),
            MISTAKE("Giving exact dates and distances with confidence", "Textbooks give different dates for Paul's journeys. Write the order of events and the places, and do not invent dates."),
            TIP("Paper 1 asks who went with Paul, where something happened, and the order of journeys. Paper 2 may ask you to describe one journey in detail; choose the one you know best. Ask your teacher about the exact format.", title="Exam link"),
            QUIZ("Why did Paul appeal to Caesar?", ["He wanted to avoid a trial in Jerusalem and was a Roman citizen", "He wished to meet the emperor's family", "He was told to by the apostles", "He wanted to escape from Malta"], 0,
                 "As a Roman citizen he had the right to be tried by the emperor, and he used it when Festus wanted a trial in Jerusalem.",
                 hint="Think of his citizenship.",
                 feedback=["", "No such wish is stated.", "The apostles did not tell him to.", "This was before the voyage."]),
            PQ("Name the companions of Paul on his second journey.", "Silas, joined later by Timothy at Lystra (and Luke appears in the account from Troas)."),
            PQ("What happened to Paul at Lystra?", "He healed a lame man, the people took him and Barnabas for gods, and later he was stoned and left for dead, but he got up."),
            PQ("Why was there a riot in Ephesus?", "The silversmith Demetrius feared that Paul's preaching would ruin the trade in silver shrines of Artemis."),
            PQ("Describe what happened to Paul at Malta.", "After the shipwreck the islanders were kind; a viper bit his hand without harm; he healed the father of Publius and others."),
            SUM("Paul's first journey with Barnabas took him to Cyprus, Pisidian Antioch, Iconium, Lystra and Derbe.",
                "On the second journey, with Silas and Timothy, he went to Philippi, Thessalonica, Athens and Corinth.",
                "On the third he stayed in Ephesus about three years and gave a farewell speech at Miletus.",
                "He was arrested in Jerusalem, held at Caesarea and appealed to Caesar.",
                "The voyage included a storm and shipwreck on Malta, and Paul preached in Rome under guard for two years."),
        ],
    ),
    # ------------------------------------------------------------------ Islamic Religious Studies
    lesson(
        module=M_IS, topic="Pre-Islamic Arabia",
        title="Arabia before Islam: the Jahiliyyah",
        slug="rel2-pre-islamic-arabia", minutes=20,
        summary="The land, the tribes, the trade, the religion and the society of Arabia before the Prophet Muhammad, peace be upon him, and why Muslims call that age the Jahiliyyah.",
        objectives=[
            "Describe the geography of Arabia and the way of life of the Bedouin and the townspeople",
            "Explain the importance of tribe and kinship in Arabian society",
            "Describe the religion of Arabia, the Kaaba and the position of Mecca",
            "Explain the meaning of Jahiliyyah and describe other faiths present in Arabia",
        ],
        key_concepts=["Arabian Peninsula", "Bedouin", "Tribe and kinship", "Quraysh", "Mecca and the Kaaba", "Jahiliyyah", "Hanifs"],
        blocks=[
            H("Introduction"),
            T("A student in Maroua, in the north of Cameroon, knows what dry land and a long dry season mean: people must move to find water and pasture, and traders cross the Sahel with their goods. "
              "Arabia, where Islam began, was largely a dry land of this kind. To understand why the message of Islam was so important to the people who first heard it, we must first understand the world they lived in.\n\n"
              "This lesson describes Arabia before Islam: its land, people, trade and beliefs. We will use the terms Muslims use, and the dates are given only roughly. Check your textbook."),
            D("**Jahiliyyah** is the Arabic word Muslims use for the period in Arabia before the coming of Islam. It is usually translated as \"the time of ignorance\", meaning ignorance of the guidance of God.", title="Jahiliyyah"),
            D("A **Bedouin** is a member of an Arab nomadic people who move with their camels and flocks in the desert in search of water and pasture. People who lived in towns and oases are called settled people.", title="Bedouin"),
            H("The land"),
            T("Arabia is a large peninsula in south-west Asia, bounded by the Red Sea in the west, the Arabian Sea and the Indian Ocean in the south, and the Persian (Arabian) Gulf in the east. Much of it is desert with little rain. "
              "Life was possible around **oases**, where there was water, and in the higher regions of the south-west (Yemen) which received more rain.\n\n"
              "The Hijaz, the western region along the Red Sea, contained the towns of **Mecca** and **Yathrib** (later called Medina) and the town of Taif."),
            H("Tribe and kinship"),
            T("In a land with no strong central state, the **tribe** gave protection. Members of a tribe were related, real or by tradition, and owed loyalty to one another. "
              "A person without a tribe was in great danger. The leader of a tribe was the **shaykh**, usually chosen for his age, courage, wisdom and generosity.\n\n"
              "Honour, hospitality, courage and loyalty were highly valued virtues. Poetry was a great art; poets spoke for their tribes at fairs and were admired. "
              "When one member was harmed, the tribe was expected to take revenge, and this could lead to long feuds. Many Muslims later pointed to the unity of believers as a new loyalty that went beyond tribes."),
            H("Trade and Mecca"),
            T("Arabia lay on trade routes between the Indian Ocean, the Mediterranean and Africa. Caravans of camels carried goods such as incense, spices and leather. "
              "**Mecca** was a trading town in a dry valley. It had a well, Zamzam, and it was the home of the shrine called the **Kaaba**. The ruling tribe was the **Quraysh**.\n\n"
              "Pilgrims came to the Kaaba each year and the Quraysh took care of them. This brought both respect and trade to Mecca. The Quraysh were merchants, and the Prophet Muhammad, peace be upon him, belonged to this tribe."),
            H("Religion"),
            T("Most Arabs worshipped many gods and spirits. Idols stood around the Kaaba. Some tribes had their own idols and sacred places. People also believed in fate, magic and soothsayers.\n\n"
              "Muslims believe that the Kaaba was first built to worship the One God by the Prophet **Ibrahim** (Abraham) and his son **Ismail** (Ishmael), and that over time the Arabs turned to idols. Some people, called **hanifs**, looked for the pure faith of Ibrahim and worshipped only one God. "
              "There were also Jewish tribes, especially in Yathrib, and Christian communities in some regions, for example in the south. Neighbouring states, the Byzantine Empire and the Persian Empire, were powerful."),
            H("Society"),
            T("Society had good and bad features. Hospitality, courage and honour were praised. But the poor, orphans and slaves were often treated badly. "
              "Muslims believe that the Quran condemned practices such as the burial of newborn girls, and taught care for orphans, the poor and the weak. "
              "Women's position differed between tribes and over time. Use your textbook for the examples your teacher expects."),
            IMG("f5rel-2-muhammad-timeline.svg", alt="A simple timeline of the life of the Prophet Muhammad, from birth in Mecca to the return to Mecca and death in Medina.", caption="Figure 1. The timeline of the next lesson. This lesson describes the world before it."),
            KEY("Arabia before Islam at a glance", "Learn these headings:", cards=[
                ["Land", "Desert and oases; Mecca and Yathrib in the Hijaz."],
                ["People", "Bedouin nomads and settled traders; loyalty to the tribe."],
                ["Economy", "Camel caravans, trade and pilgrimage to the Kaaba."],
                ["Religion", "Many gods and idols; a few hanifs; Jews and Christians in places."],
                ["Society", "Honour and hospitality, but also feuds and the neglect of the weak."],
            ]),
            QUIZ("Which tribe controlled Mecca at the time of the Prophet's birth?", ["Aws", "Quraysh", "Khazraj", "Ghassan"], 1,
                 "The Quraysh were the leading tribe of Mecca and guardians of the Kaaba.",
                 hint="The Prophet himself belonged to this tribe.",
                 feedback=["The Aws were a tribe of Yathrib.", "", "The Khazraj were also a tribe of Yathrib.", "The Ghassan were an Arab kingdom on the Byzantine border."]),
            EX("Model answer plan 1", intro="Describe the way of life of the Arabs before Islam.", steps=[
                S("Land and movement", text="Desert land; Bedouin moved with camels and flocks; townspeople lived at oases and traded."),
                S("Tribes", text="Loyalty to the tribe; leaders called shaykhs; blood feuds and revenge."),
                S("Values", text="Hospitality, courage, honour, poetry."),
                S("Weak groups", text="Orphans, the poor and slaves were often neglected."),
            ]),
            EX("Model answer plan 2", intro="Why was Mecca important in Arabia before Islam?", steps=[
                S("Trade", text="It lay on caravan routes and the Quraysh were merchants."),
                S("The Kaaba", text="The shrine drew pilgrims every year."),
                S("The well", text="Zamzam supplied water in a dry valley."),
                S("Muslim belief", text="Muslims believe that Ibrahim and Ismail built the Kaaba for the worship of the One God."),
            ]),
            MISTAKE("Calling all Arabs Muslims or all Arabs idol worshippers", "Before Islam there were idol worshippers, a few hanifs, Jews and Christians. Equally, not all Muslims today are Arabs. Write carefully."),
            MISTAKE("Using Jahiliyyah as an insult to a people", "Muslims use the word for the lack of guidance before Islam, not as a judgement on the Arab people. Describe the term, as your textbook does, and avoid unkind language."),
            TIP("Paper 1 may ask about the tribe of the Prophet, the shrine in Mecca, the meaning of Jahiliyyah or the name for nomads. Paper 2 may ask you to describe conditions in Arabia. Check with your teacher if the Islamic section is part of your paper.", title="Exam link"),
            QUIZ("What does the word Jahiliyyah refer to?", ["The Muslim calendar", "The period of Arabia before Islam", "The month of fasting", "A Quran chapter"], 1,
                 "It is the term used for the time before Islam, usually translated as the time of ignorance.",
                 hint="It is about the time before the revelation.",
                 feedback=["The calendar is the Hijri calendar.", "", "That is Ramadan.", "It is not the title of a chapter."]),
            PQ("Who were the Bedouin?", "They were nomadic Arabs who moved with camels and flocks in the desert, looking for water and pasture."),
            PQ("Give three features of the society of Arabia before Islam.", "Loyalty to the tribe; honour and hospitality; blood feuds; poetry; neglect of the weak such as orphans and slaves."),
            PQ("Why did pilgrims come to Mecca before Islam?", "The Kaaba was a sacred shrine; pilgrims came each year, and it was cared for by the Quraysh."),
            PQ("What do Muslims believe about the origin of the Kaaba?", "Muslims believe that Ibrahim and his son Ismail built it for the worship of the One God."),
            SUM("Arabia was a mostly dry land where Bedouin and settled townspeople lived.",
                "The tribe gave protection and identity, and honour and hospitality were highly valued.",
                "Mecca was a trading and pilgrimage town ruled by the Quraysh, and home of the Kaaba.",
                "Most Arabs worshipped many gods; a few hanifs, Jews and Christians believed in one God.",
                "Muslims call this period before Islam the Jahiliyyah."),
        ],
    ),
    lesson(
        module=M_IS, topic="The life and prophethood of Muhammad",
        title="The life of the Prophet Muhammad, peace be upon him",
        slug="rel2-life-prophethood-muhammad", minutes=25,
        summary="From his birth in Mecca and the first revelation in the cave of Hira, through opposition, the Hijra to Medina, and the return to Mecca, to his death: the main events of the Prophet's life.",
        objectives=[
            "Describe the early life of Muhammad in Mecca and his marriage to Khadija",
            "Describe the first revelation in the cave of Hira",
            "Explain the opposition in Mecca and the Hijra to Medina",
            "Describe the life in Medina, the return to Mecca and the death of the Prophet",
        ],
        key_concepts=["Muhammad (peace be upon him)", "Khadija", "Cave of Hira", "Jibril", "Hijra", "Medina", "Return to Mecca"],
        blocks=[
            H("Introduction"),
            T("Muslims love and respect the Prophet Muhammad and, whenever they mention his name, add the words **peace be upon him**. In this lesson we describe the main events of his life as Muslims believe and as the sources tell them. "
              "Please write about him with the same respect in your answers. Dates are given as common approximate dates; **check your textbook** for the dates your syllabus uses.\n\n"
              "Muslims believe that Muhammad is the last Prophet of God, the one who received the Quran."),
            D("**Prophethood** (in Arabic *nubuwwa*) is the belief that God chooses people to receive His message and to guide others. Muslims believe that Muhammad is the final Prophet.", title="Prophethood"),
            D("The **Hijra** is the migration of the Prophet and his companions from Mecca to Medina in the year 622 CE. It is the starting point of the Islamic (Hijri) calendar.", title="Hijra"),
            H("Early life"),
            T("Muhammad was born in **Mecca**, in the tribe of the **Quraysh**, around the year 570 CE (check your textbook). His father, **Abdullah**, died before he was born. His mother, **Amina**, died when he was a young child. "
              "He was cared for first by his grandfather, **Abd al-Muttalib**, and then by his uncle **Abu Talib**.\n\n"
              "As a young man he worked as a trader and was known for his honesty and trustworthiness. People called him **al-Amin**, the trustworthy. "
              "At about twenty-five he married **Khadija**, a respected businesswoman, who was older than he was. They had children, and their marriage was happy."),
            H("The first revelation"),
            T("Muhammad often went to the **cave of Hira**, on a mountain near Mecca, to pray and think. Muslims believe that in one of the nights of **Ramadan**, when he was about forty years old, the angel **Jibril** (Gabriel) came to him and said \"Read!\" (*Iqra*). "
              "He answered that he could not read. The angel repeated the command, and Muhammad received the first verses of the Quran.\n\n"
              "He returned home frightened. **Khadija** comforted him and believed in him. She was the first to accept Islam. Others in the early circle included his cousin **Ali**, his friend **Abu Bakr** and his freed servant **Zayd**. "
              "Revelation continued for about twenty-three years."),
            H("Opposition in Mecca"),
            T("After a few years of private teaching, the Prophet began to preach openly that there is only one God and that idols should not be worshipped. He called for justice and care for the poor. "
              "Some people believed, mostly young people and the poor, but the leaders of the Quraysh opposed him. They feared the loss of the trade and their position as guardians of the Kaaba.\n\n"
              "The early Muslims suffered persecution, and some were tortured. Some went to Abyssinia (Ethiopia), where the Christian king gave them protection. The Quraysh also boycotted the Prophet's clan for a period. "
              "The Prophet lost his wife Khadija and his uncle Abu Talib, his protector, around the same time. Muslims remember this as a year of sorrow."),
            H("The Hijra to Medina"),
            T("People of Yathrib, who had come to Mecca for the pilgrimage, accepted Islam and invited the Prophet to their city. They hoped he would help settle their feuds. "
              "Finally, in 622 CE, the Muslims left Mecca in small groups. The Prophet left with his companion **Abu Bakr** and hid for some days in a cave before travelling to Yathrib, which became known as **Medina**, \"the city of the Prophet\". "
              "This migration is the **Hijra**, and the Islamic calendar counts years from it.\n\n"
              "In Medina the Muslims from Mecca, the **Muhajirun** (emigrants), were welcomed by the **Ansar** (helpers) of Medina. The Prophet built a mosque and set up an agreement to regulate relations among the people of the city, Muslims and others."),
            H("Medina, return to Mecca and death"),
            T("The Quraysh fought the Muslims in battles such as Badr and Uhud (check your textbook for the details and dates). In 628 CE the Prophet and his followers agreed the treaty of **Hudaybiyyah** with the Quraysh. "
              "Later, in about 630 CE, the Prophet returned to **Mecca** with a large following. The city surrendered with very little fighting, and the Prophet forgave most of his former enemies. The idols around the Kaaba were removed and the Kaaba was dedicated to the worship of one God.\n\n"
              "In 632 CE the Prophet performed his last pilgrimage, called the **Farewell Pilgrimage**, and gave an address calling for justice, equality of believers and care for the weak. He died shortly afterwards, in **Medina**, in 632 CE, and was buried there."),
            IMG("f5rel-2-muhammad-timeline.svg", alt="A timeline: birth in Mecca, first revelation at Hira, the Hijra to Medina in 622, return to Mecca, and death in Medina in 632.", caption="Figure 1. The main events in the life of the Prophet Muhammad, peace be upon him. Dates are approximate; check your textbook."),
            QUIZ("What is the Hijra?", ["The first revelation", "The migration from Mecca to Medina", "The pilgrimage to Mecca", "The month of fasting"], 1,
                 "The Hijra is the migration to Medina in 622 CE, the start of the Islamic calendar.",
                 hint="The word means migration.",
                 feedback=["That happened in the cave of Hira.", "", "That is the Hajj.", "That is Ramadan."]),
            EX("Model answer plan 1", intro="Describe the first revelation to the Prophet Muhammad, peace be upon him.", steps=[
                S("Setting", text="He used to pray in the cave of Hira, near Mecca."),
                S("The angel", text="In Ramadan, when he was about forty, Jibril came and said, Read."),
                S("His reaction", text="He was frightened and returned home."),
                S("Khadija", text="She comforted him and was the first to believe."),
                S("Continuation", text="Revelation continued for about twenty-three years."),
            ]),
            EX("Model answer plan 2", intro="Explain why the Hijra was important.", steps=[
                S("Reasons for leaving", text="Persecution by the Quraysh; the invitation from the people of Yathrib."),
                S("The journey", text="The Prophet left with Abu Bakr and the Muslims followed."),
                S("In Medina", text="The Muhajirun were welcomed by the Ansar; a mosque and a community were built."),
                S("Lasting importance", text="The Muslim calendar begins from the Hijra; the Muslim community took shape."),
            ]),
            MISTAKE("Using the wrong city or year", "The birth, the first revelation and the later return were all in or near Mecca. The Hijra of 622 CE ended in Medina, where he died in 632 CE. Check your textbook for all dates."),
            MISTAKE("Writing about the Prophet without respect", "Always write peace be upon him (or PBUH) after his name and use words such as the Prophet, not casual names. Examiners expect respectful language."),
            TIP("Learn the order: birth in Mecca, Khadija, Hira, opposition, Hijra, Medina, Hudaybiyyah, return to Mecca, Farewell Pilgrimage, death. Paper 1 asks for names, places and order.", title="Exam link"),
            QUIZ("Who was the first person to accept Islam, according to Muslim tradition?", ["Abu Bakr", "Khadija", "Umar", "Abu Talib"], 1,
                 "Muslim tradition says that Khadija, his wife, was the first to believe.",
                 hint="She comforted him after Hira.",
                 feedback=["Abu Bakr was among the first men.", "", "Umar accepted Islam later.", "Abu Talib protected the Prophet but did not accept Islam according to the common view."]),
            PQ("State four facts about the early life of the Prophet.", "He was born in Mecca in the Quraysh tribe; his father died before his birth and his mother in his childhood; he was cared for by Abd al-Muttalib and Abu Talib; he was a trader known as al-Amin; he married Khadija."),
            PQ("Why did the Quraysh oppose the Prophet?", "He taught that there is only one God and that idols should be abandoned, which threatened their trade, their position as guardians of the Kaaba and their traditions."),
            PQ("What was the importance of the return to Mecca?", "Mecca came under Muslim control with little fighting, the idols were removed from the Kaaba and it was devoted to the worship of one God."),
            PQ("Name the two groups of Muslims in Medina after the Hijra.", "The Muhajirun, the emigrants from Mecca, and the Ansar, the helpers of Medina."),
            SUM("Muhammad was born in Mecca in the Quraysh tribe and was known as al-Amin.",
                "He married Khadija and received the first revelation from Jibril in the cave of Hira.",
                "He met opposition in Mecca and migrated to Medina in the Hijra of 622 CE.",
                "He returned to Mecca with a large following and removed the idols.",
                "He died in Medina in 632 CE. Check your textbook for all dates."),
        ],
    ),
    lesson(
        module=M_IS, topic="The Quran",
        title="The Quran: revelation, collection and use",
        slug="rel2-the-quran", minutes=22,
        summary="Muslims believe the Quran is the word of God, revealed in Arabic through Jibril over about twenty-three years, memorised and written down in the Prophet's time and collected into one volume afterwards.",
        objectives=[
            "Explain what Muslims believe about the Quran and how it was revealed",
            "Describe how the Quran was memorised and written in the Prophet's lifetime",
            "Describe the collection under Abu Bakr and the standard copies under Uthman",
            "Describe the structure of the Quran and its place in the life of Muslims",
        ],
        key_concepts=["Revelation (wahy)", "Jibril", "Surah and ayah", "Memorisation (hafiz)", "Abu Bakr", "Uthman", "Zayd ibn Thabit"],
        blocks=[
            H("Introduction"),
            T("In many Cameroonian towns a Muslim child may begin learning the Quran by heart at a young age, in a Quranic school, and many people can recite long passages. "
              "The Quran is at the centre of Islam: it is recited in prayer, studied in schools, and respected so highly that it is kept in a clean place and handled with care.\n\n"
              "This lesson describes what Muslims believe about the Quran, how it was revealed and how it was preserved. We use the words 'Muslims believe' for statements of faith."),
            D("**Wahy** means revelation, God's communication to His prophets. Muslims believe that the Quran is the word of God, revealed to the Prophet Muhammad, peace be upon him, through the angel Jibril.", title="Revelation"),
            D("A **surah** is a chapter of the Quran. An **ayah** (plural *ayat*) is a verse. The Quran has **114 surahs**.", title="Surah and ayah"),
            H("The revelation"),
            T("Muslims believe that the Quran was revealed to the Prophet piece by piece over about **twenty-three years**, beginning with the first revelation at Hira when he was about forty. "
              "It was revealed in **Arabic**. Some parts were revealed in Mecca and others in Medina. The Meccan parts are usually shorter and stress belief in one God, the Day of Judgement and morals. The Medinan parts are often longer and deal more with the laws and the organisation of the community.\n\n"
              "The revelation often came in response to events or questions of the early community. The Prophet recited each portion to his companions and told them where it belonged in the order of the text."),
            H("Memorising and writing"),
            T("The first way of preserving the Quran was **memorisation**. The Prophet and his companions learned the verses by heart and recited them in prayer. A person who has memorised the whole Quran is called a **hafiz**. "
              "Memorisation has continued to this day, and Muslims all over the world memorise the same text.\n\n"
              "The Quran was also **written down** during the Prophet's lifetime by scribes, the best known of whom was **Zayd ibn Thabit**, on materials such as palm leaves, flat stones, bones and pieces of leather. These pieces were not yet collected in a single book."),
            H("Collection under Abu Bakr and Uthman"),
            T("After the death of the Prophet, **Abu Bakr** became the first caliph (leader of the community). Muslims relate that many reciters of the Quran were killed in a battle early in his rule, and **Umar** advised collecting the Quran so that none of it would be lost. "
              "Abu Bakr asked **Zayd ibn Thabit** to collect the written pieces and compare them with the memory of the reciters. The result was a complete copy, kept first by Abu Bakr, then by Umar and then by his daughter **Hafsa**.\n\n"
              "In the time of the third caliph, **Uthman**, Muslims lived in many lands and had differences in the way they recited. Uthman asked a committee, led by Zayd ibn Thabit, to prepare a standard written copy based on the earlier copy. Copies were sent to the main cities of the Muslim world, and other versions were put aside. "
              "This is why Muslims believe the Quran of today is the same as the one that was recited by the Prophet. Dates for these events differ in books; check your textbook."),
            H("Structure and use"),
            T("The Quran is arranged by surahs, not in the order of revelation. The first is **Al-Fatiha** (\"The Opening\"), a short prayer recited in every prayer, and the others are arranged broadly from longer to shorter chapters. Most begin with the words *Bismillah ar-Rahman ar-Rahim*, \"In the name of God, the Most Gracious, the Most Merciful\". "
              "For convenience the Quran is divided into 30 parts called **juz**, so that it can be read in a month.\n\n"
              "The Quran gives guidance on belief in one God, prophets, angels, the Day of Judgement, worship, family life, justice, honesty and care for the poor. It also tells stories of earlier prophets, such as Ibrahim, Musa (Moses) and Isa (Jesus). "
              "Muslims recite it in prayer, in Ramadan and at important times. Translations help people understand it, but Muslims consider the Arabic text itself to be the Quran."),
            IMG("f5rel-2-quran-compilation.svg", alt="A flow chart showing the revelation to the Prophet, memorising and writing, the collection under Abu Bakr and the standard copies under Uthman.", caption="Figure 1. From revelation to the standard copies of the Quran."),
            KEY("Respect for the Quran", "Muslims show respect in practical ways:", cards=[
                ["Cleanliness", "They perform wudu (ablution) before touching or reading the copy and keep it in a clean, high place."],
                ["Recitation", "They recite it carefully and beautifully, often with a teacher."],
                ["Memorisation", "Many children and adults memorise part or all of it."],
                ["Understanding", "They also study the meaning, using translations and commentary."],
            ]),
            QUIZ("Who was asked by Abu Bakr to collect the Quran in one volume?", ["Uthman", "Zayd ibn Thabit", "Ali", "Bilal"], 1,
                 "Zayd ibn Thabit, a scribe of the Prophet, collected the written pieces and checked them with the reciters.",
                 hint="He was also on the committee under Uthman.",
                 feedback=["Uthman ordered standard copies later.", "", "Ali was the Prophet's cousin and the fourth caliph.", "Bilal was the first muezzin who called to prayer."]),
            EX("Model answer plan 1", intro="Explain how the Quran was preserved.", steps=[
                S("Memorisation", text="The Prophet and the companions learned it by heart; there are huffaz (people who memorise) to this day."),
                S("Writing", text="Scribes such as Zayd ibn Thabit wrote it on palm leaves, stones and leather in the Prophet's lifetime."),
                S("Abu Bakr", text="The pieces were collected into one volume, checked by the reciters."),
                S("Uthman", text="A standard copy was made and copies were sent to the main cities."),
            ]),
            EX("Model answer plan 2", intro="Describe the structure of the Quran.", steps=[
                S("Chapters", text="114 surahs made of verses (ayat)."),
                S("Order", text="The first surah is Al-Fatiha; the rest are arranged broadly from longer to shorter."),
                S("Divisions", text="30 juz for reading over a month."),
                S("Types", text="Meccan and Medinan surahs."),
            ]),
            MISTAKE("Saying the Quran was written by the Prophet", "Muslims believe the Quran is the word of God revealed to the Prophet. The Prophet recited it and scribes wrote it down. Avoid saying that he composed it."),
            MISTAKE("Mixing up Abu Bakr and Uthman", "Abu Bakr had the Quran collected into one volume. Uthman had standard copies made and sent to the cities. Remember: collection first, standard copies later."),
            TIP("Paper 1 questions ask for numbers (114 surahs, 30 juz) and names (Jibril, Zayd, Abu Bakr, Uthman). In Paper 2 use the words 'Muslims believe'.", title="Exam link"),
            QUIZ("How many surahs are there in the Quran?", ["30", "99", "114", "124"], 2,
                 "The Quran has 114 surahs; 30 is the number of juz.",
                 hint="It is more than the 99 names of God.",
                 feedback=["30 is the number of parts (juz).", "99 is the number of the names of God.", "", "Not a number linked with the Quran."]),
            PQ("Through whom, and in what language, do Muslims believe the Quran was revealed?", "Through the angel Jibril to the Prophet Muhammad, peace be upon him, in Arabic."),
            PQ("Explain what a hafiz is.", "A hafiz is a person who has memorised the whole Quran."),
            PQ("Describe what Uthman did with the Quran.", "He had a standard written copy prepared by a committee led by Zayd ibn Thabit and sent copies to the main cities, so that Muslims would have one text."),
            PQ("Give three ways in which Muslims show respect for the Quran.", "They perform wudu before handling it; keep it in a clean high place; recite it carefully; memorise it; study its meaning."),
            SUM("Muslims believe that the Quran is God's word revealed in Arabic through Jibril over about 23 years.",
                "It was memorised and written down during the Prophet's lifetime.",
                "Abu Bakr had it collected into one volume; Uthman had standard copies sent to the cities.",
                "It has 114 surahs and 30 juz, beginning with Al-Fatiha.",
                "It guides Muslims in belief, worship and daily life."),
        ],
    ),
    lesson(
        module=M_IS, topic="Hadith",
        title="Hadith: the sayings and actions of the Prophet",
        slug="rel2-hadith", minutes=20,
        summary="Hadith are the reports of what the Prophet said, did and approved; Muslim scholars checked their chains of narrators and collected them in books such as those of al-Bukhari and Muslim.",
        objectives=[
            "Define hadith and sunnah and explain how they relate to the Quran",
            "Explain the parts of a hadith: the chain of narrators and the text",
            "Describe how scholars graded hadith as sahih, hasan or daif",
            "Name the best-known collections and collectors",
        ],
        key_concepts=["Hadith", "Sunnah", "Isnad and matn", "Sahih", "Al-Bukhari", "Muslim", "The six collections"],
        blocks=[
            H("Introduction"),
            T("A child who watches how an elder prepares for prayer learns by seeing and hearing. Early Muslims learned in the same way: they watched the Prophet pray, fast, deal with people and settle disputes, and they passed on what they saw and heard.\n\n"
              "These reports are called **hadith**. They are, for Muslims, the second main source of guidance after the Quran. This lesson explains what they are and how they were collected."),
            D("A **hadith** is a report of what the Prophet Muhammad, peace be upon him, said, did or approved. The plural is *ahadith*.", title="Hadith"),
            D("The **sunnah** is the example or practice of the Prophet. It is known through the hadith.", title="Sunnah"),
            H("Why hadith are needed"),
            T("The Quran tells Muslims to pray, give zakat, fast and go on pilgrimage, but the details of how to do these things are mainly learned from the sunnah. For example, the Quran commands prayer, while the hadith show how many units to pray at each time and what to recite. "
              "The Quran also tells Muslims to obey the Prophet. For this reason, the Muslims take the Quran as the first source and the sunnah as the second."),
            H("How a hadith is built"),
            T("A hadith has two parts. The **isnad** is the chain of narrators: A heard it from B, who heard it from C, back to a companion of the Prophet who heard or saw it. The **matn** is the text, the content of the report.\n\n"
              "Here is a famous example, paraphrased: the Prophet said that actions are judged by their intentions, and that each person will have what they intended. The report carries a chain of narrators back to the companion Umar."),
            H("Checking hadith"),
            T("After the Prophet's death, some reports were weak or even invented. Scholars therefore developed a science to check each hadith. They studied the narrators: Were they honest? Did they have a good memory? Did they actually meet the person they quote? "
              "They also checked whether the text agrees with the Quran and with other well-known reports.\n\n"
              "Reports were then graded. A **sahih** (sound) hadith has a continuous chain of reliable narrators and no hidden defect. A **hasan** (good) hadith is slightly lower in reliability. A **daif** (weak) hadith has a defect in its chain or text. The terms may be explained a little differently in some books; check your textbook."),
            H("The collections"),
            T("In the second and third centuries after the Hijra, scholars travelled to collect hadith and compiled them in books. The best-known are the two 'sound' collections of **Muhammad al-Bukhari** (*Sahih al-Bukhari*) and **Muslim ibn al-Hajjaj** (*Sahih Muslim*). Together with the books of **Abu Dawud**, **al-Tirmidhi**, **al-Nasai** and **Ibn Majah**, they form what Sunni Muslims call the **six major collections**. "
              "Shia Muslims have their own collections of reports which they also respect. Names and dates of the collectors, such as al-Bukhari in the ninth century CE, differ slightly between books; check your textbook.\n\n"
              "Hadith are often grouped by theme: faith, prayer, fasting, trade, family and manners. Many Muslims know short hadith by heart, such as the one about loving for your brother what you love for yourself."),
            KEY("Quran and hadith compared", "They work together:", cards=[
                ["Quran", "The word of God, revealed in Arabic, memorised and written during the Prophet's life."],
                ["Hadith", "Reports of the words, actions and approvals of the Prophet, passed on by narrators and collected in books."],
                ["Sunnah", "The example of the Prophet, learned from the hadith."],
                ["Use", "Muslim scholars use both when explaining worship and conduct."],
            ]),
            QUIZ("What is the isnad of a hadith?", ["Its text", "Its chain of narrators", "Its date", "Its translation"], 1,
                 "The isnad is the chain of narrators; the text is the matn.",
                 hint="The other part is the matn.",
                 feedback=["That is the matn.", "", "Dates are not the isnad.", "Translations are not part of a hadith."]),
            EX("Model answer plan 1", intro="Explain why hadith are important to Muslims.", steps=[
                S("Second source", text="After the Quran, the sunnah is the main source of guidance."),
                S("Details of worship", text="The hadith show how to pray, fast and perform the pilgrimage."),
                S("Example", text="They show how the Prophet treated family, neighbours and the poor."),
                S("Law and conduct", text="Scholars use them to explain rules and manners."),
            ]),
            EX("Model answer plan 2", intro="Describe how hadith were checked and collected.", steps=[
                S("Reason", text="Weak or invented reports had appeared."),
                S("The chain", text="Scholars studied narrators' honesty, memory and contact with each other."),
                S("The grades", text="Hadith were graded sahih, hasan or daif."),
                S("The books", text="Al-Bukhari and Muslim compiled the best-known collections, with four other books making the six."),
            ]),
            MISTAKE("Saying that hadith are part of the Quran", "The Quran and the hadith are different. The Quran is the word of God; the hadith report the words and actions of the Prophet."),
            MISTAKE("Naming only one collection", "The best-known are two sahih collections, by al-Bukhari and Muslim, and there are six major Sunni collections. Learn all six names if your syllabus asks for them."),
            TIP("Paper 1 asks for definitions (hadith, sunnah, isnad, sahih) and collectors (al-Bukhari, Muslim). In Paper 2 describe and explain; use the words 'Muslims believe'.", title="Exam link"),
            QUIZ("Which of these is a collector of hadith?", ["Zayd ibn Thabit", "Al-Bukhari", "Uthman", "Abu Talib"], 1,
                 "Muhammad al-Bukhari compiled Sahih al-Bukhari.",
                 hint="His book is called Sahih.",
                 feedback=["Zayd was a scribe of the Quran.", "", "Uthman was a caliph.", "Abu Talib was the Prophet's uncle."]),
            PQ("Define hadith and sunnah.", "A hadith is a report of what the Prophet said, did or approved; the sunnah is his example or way, known through the hadith."),
            PQ("What are the two parts of a hadith?", "The isnad, the chain of narrators, and the matn, the text."),
            PQ("Give two ways in which scholars checked the reliability of a hadith.", "They studied the honesty and memory of each narrator and whether they could have met; they compared the text with the Quran and other reports."),
            PQ("Name two major collections of hadith and their compilers.", "Sahih al-Bukhari by Muhammad al-Bukhari and Sahih Muslim by Muslim ibn al-Hajjaj."),
            SUM("A hadith is a report of the Prophet's words, actions or approvals; the sunnah is his example.",
                "The Quran is the first source of guidance and the sunnah is the second.",
                "A hadith has an isnad (chain) and a matn (text).",
                "Scholars graded hadith as sahih, hasan or daif.",
                "Al-Bukhari and Muslim made the best-known collections."),
        ],
    ),
    lesson(
        module=M_IS, topic="The Five Pillars of Islam",
        title="The Five Pillars: shahada, salat, zakat, sawm and hajj",
        slug="rel2-five-pillars-islam", minutes=28,
        summary="The five basic acts of worship of Muslims: the declaration of faith, the five daily prayers, charity, fasting in Ramadan and the pilgrimage to Mecca.",
        objectives=[
            "Name the Five Pillars and explain the meaning of each",
            "Describe the five daily prayers and their preparation",
            "Explain zakat, who gives it and who may receive it",
            "Describe fasting in Ramadan and the main rites of the Hajj",
        ],
        key_concepts=["Shahada", "Salat", "Wudu", "Qibla", "Zakat", "Sawm", "Ramadan", "Hajj", "Ihram", "Kaaba"],
        blocks=[
            H("Introduction"),
            T("A house stands on pillars. In a famous hadith, the Prophet said that Islam is built on five pillars. They are the basic acts of worship that every Muslim is expected to perform. "
              "Many Muslims in Cameroon pray five times a day, give charity, and fast in Ramadan, and some save for years to go on the pilgrimage to Mecca.\n\n"
              "In this lesson we study each pillar with its practical details. Remember to write 'Muslims believe' and to be respectful."),
            D("The **Five Pillars of Islam** are: **shahada** (declaration of faith), **salat** (prayer), **zakat** (almsgiving), **sawm** (fasting in Ramadan) and **hajj** (pilgrimage to Mecca).", title="The Five Pillars"),
            IMG("f5rel-2-five-pillars.svg", alt="Five columns labelled shahada, salat, zakat, sawm and hajj supporting a roof labelled Islam.", caption="Figure 1. The Five Pillars of Islam."),
            H("1. Shahada: the declaration of faith"),
            T("The shahada is the statement: \"There is no god but God (Allah), and Muhammad is the Messenger of God.\" Saying it sincerely, with understanding, makes a person a Muslim. "
              "It states belief in the oneness of God (**tawhid**) and in the prophethood of Muhammad, peace be upon him. It is repeated in the call to prayer and in the prayers."),
            H("2. Salat: prayer"),
            T("Muslims pray **five times a day**: before sunrise (**fajr**), after midday (**dhuhr**), in the afternoon (**asr**), after sunset (**maghrib**) and in the evening (**isha**). The call to prayer, the **adhan**, is given by the muezzin.\n\n"
              "Before praying, a Muslim performs **wudu**, washing the hands, mouth, nose, face, arms, wiping the head and washing the feet. The prayer is performed facing the **qibla**, the direction of the Kaaba in Mecca, on a clean place such as a prayer mat. "
              "It includes standing, bowing, prostrating and sitting, with recitation of the Quran, beginning with Al-Fatiha. "
              "On **Friday** at noon, men are expected to attend the congregational prayer (**Jumuah**) at the mosque, with a sermon (**khutba**). Muslims may pray alone or in a group; the group prayer is led by an imam."),
            H("3. Zakat: almsgiving"),
            T("Zakat means purification and growth. Muslims who own wealth above a minimum level (called the **nisab**) for a full year give a fixed part of it to those in need. The usual rate on savings is **2.5 per cent** (one-fortieth). "
              "Other rates apply to crops and livestock; ask a scholar or check your textbook for the current rules.\n\n"
              "The Quran names the groups who may receive zakat, including the poor, the needy, those who collect it, those in debt, the traveller in need and those in the cause of God. "
              "Zakat is different from voluntary charity (**sadaqah**), which can be given at any time and in any amount. Muslims believe that zakat purifies wealth and builds a caring society."),
            H("4. Sawm: fasting in Ramadan"),
            T("**Ramadan** is the ninth month of the Islamic calendar, the month in which Muslims believe the Quran began to be revealed. Healthy adult Muslims fast every day from **dawn until sunset**: no food, drink or marital relations during these hours. "
              "People who are ill, travelling, very old, pregnant or nursing, or young children, are excused, and may make up the fast or give food to the poor later. Check your textbook for details.\n\n"
              "The fast is also a time of prayer, reading the Quran, patience and generosity. The fast is usually broken at sunset with a meal called **iftar**, often beginning with dates, and a pre-dawn meal (**suhur**) is eaten before it begins. "
              "The month ends with the festival of **Eid al-Fitr**. The Night of Power (**Laylat al-Qadr**), thought to be one of the last odd nights, is remembered as the night when the Quran was first revealed."),
            H("5. Hajj: pilgrimage"),
            T("The hajj is the pilgrimage to **Mecca**, made in the twelfth month, **Dhul-Hijjah**. Every Muslim who is physically and financially able must perform it **once in a lifetime**. "
              "Pilgrims enter a state of purity called **ihram**; men wear two simple white unsewn cloths and women wear modest dress. This shows equality before God.\n\n"
              "The main rites include walking round the Kaaba seven times (**tawaf**), walking between the hills of **Safa and Marwa** (**sai**), standing on the plain of **Arafat** (the most important rite), spending the night at **Muzdalifah**, and throwing stones at pillars at **Mina**, followed by an animal sacrifice and a festival called **Eid al-Adha**. "
              "The visit to Mecca outside the Hajj season is called **umrah** and does not replace the Hajj."),
            QUIZ("About what percentage of qualifying savings is paid as zakat?", ["1 per cent", "2.5 per cent", "10 per cent", "20 per cent"], 1,
                 "The usual rate on savings above the nisab, held for a year, is 2.5 per cent.",
                 hint="It equals one-fortieth.",
                 feedback=["Too low.", "", "That is more like a tithe in some traditions.", "Too high."]),
            EX("Model answer plan 1", intro="Describe the practice of salat.", steps=[
                S("Times", text="Five times a day: fajr, dhuhr, asr, maghrib, isha."),
                S("Preparation", text="Wudu, a clean place, facing the qibla."),
                S("Actions", text="Standing, bowing, prostrating and sitting, with recitation of the Quran."),
                S("Friday", text="The congregational prayer, with a sermon, at the mosque."),
            ]),
            EX("Model answer plan 2", intro="Explain the importance of the Hajj.", steps=[
                S("Obedience", text="It is one of the Five Pillars, required once in a lifetime of those able."),
                S("Equality", text="Pilgrims wear simple white clothes and are equal before God."),
                S("Unity", text="Muslims from all over the world gather in one place."),
                S("Following the example", text="The rites remember Ibrahim, Hajar, Ismail and the Prophet Muhammad."),
            ]),
            MISTAKE("Mixing up the pillars", "Shahada is the declaration, salat the prayer, zakat the charity, sawm the fast, hajj the pilgrimage. The order of the five is usually given in this way."),
            MISTAKE("Saying everyone must fast or make the Hajj", "The sick, travellers and young children are excused from the fast, and the Hajj is required only of those able to afford it and travel. Write 'those who are able'."),
            TIP("Paper 1 asks for names, numbers and times (five prayers, 2.5 per cent, Ramadan, Dhul-Hijjah). Paper 2 asks you to describe and explain the importance of one or more pillars.", title="Exam link"),
            QUIZ("Which pillar is fulfilled in the month of Ramadan?", ["Shahada", "Zakat", "Sawm", "Hajj"], 2,
                 "Sawm is the fast during Ramadan.",
                 hint="Think of dawn to sunset.",
                 feedback=["The shahada can be said at any time.", "Zakat is given after a year of holding wealth.", "", "Hajj is in the month of Dhul-Hijjah."]),
            PQ("Write the meaning of the shahada.", "There is no god but God, and Muhammad is the Messenger of God."),
            PQ("Name the five daily prayers.", "Fajr, dhuhr, asr, maghrib and isha."),
            PQ("Who is excused from fasting in Ramadan?", "The sick, travellers, the very old, pregnant or nursing women, and young children; some may make up the days later."),
            PQ("Describe three rites of the Hajj.", "Wearing ihram; walking round the Kaaba seven times (tawaf); walking between Safa and Marwa (sai); standing at Arafat; throwing stones at Mina."),
            SUM("The Five Pillars are shahada, salat, zakat, sawm and hajj.",
                "Muslims pray five times a day, facing the qibla after wudu.",
                "Zakat is a yearly payment, usually 2.5 per cent of qualifying savings, to those in need.",
                "Sawm is fasting from dawn to sunset in Ramadan.",
                "Hajj is the pilgrimage to Mecca in Dhul-Hijjah, once in a lifetime for those able."),
        ],
    ),
    # ------------------------------------------------------------------ Examination
    lesson(
        module=M_EX, topic="Paper 1",
        title="Paper 1: answering the multiple-choice questions",
        slug="relx-paper-1-multiple-choice-strategy", minutes=20,
        summary="How to prepare for and answer the 50 multiple-choice questions of Religious Studies: learn names, places and order of events, read each question carefully, eliminate wrong options and manage your time.",
        objectives=[
            "Describe Paper 1 as 50 multiple-choice questions on the whole syllabus",
            "Use a revision method for names, places, sequences and meanings",
            "Use elimination and careful reading to choose the best answer",
            "Avoid the common mix-ups between Gospels, journeys, people and Islamic terms",
        ],
        key_concepts=["Paper 1", "Elimination", "Sequence of events", "Names and places", "Reading the question", "Time management"],
        blocks=[
            H("Introduction"),
            T("Paper 1 asks 50 multiple-choice questions. The blueprint used for this course says Paper 1 is 50 multiple-choice questions on the Religious Studies syllabus and Paper 2 is an essay paper; Religious Studies is not covered in the Board's 2023 report, so check the exact format with your teacher.\n\n"
              "A multiple-choice question gives four options. One is correct and three are wrong. The wrong options are not random: they are the mistakes that careless or half-prepared candidates make. This lesson shows how to avoid them."),
            D("A **distractor** is a wrong option that looks attractive, often because it is a real name, place or event from a different story.", title="Distractor"),
            H("What Paper 1 tests"),
            T("In Religious Studies the questions usually test whether you know **who** (a person), **where** (a place), **what** (an event or a teaching), **when** (the order of events), **why** (the meaning or significance) and **which** (a Gospel, a pillar, a collection, a journey).\n\n"
              "The course has six modules in the sections studied: Old Testament I and II, Synoptic Gospels I and II, the Early Church (Acts), and Islamic Religious Studies. Paper 1 may draw on the whole syllabus. Ask your teacher whether you must be ready for all sections."),
            H("How to revise for it"),
            KEY("A revision plan", "Use these four lists for each module.", cards=[
                ["People", "Make a list of the main people in each story and one fact for each: Cornelius, centurion at Caesarea; Barnabas, son of encouragement; Khadija, first to believe."],
                ["Places", "List places with the event: Caesarea Philippi, Gethsemane, Golgotha, Damascus, Hira, Medina."],
                ["Sequences", "Write events in order: for example the last week of Jesus, or the three journeys of Paul."],
                ["Meaning", "For each event write one reason why it matters to believers."],
            ]),
            T("Practise with timelines. Draw the last week of Jesus or the life of the Prophet Muhammad from memory and check against your notes. This helps you answer 'which came first' questions."),
            H("How to answer a question"),
            T("**Step 1: read the stem.** Underline the key word. Is it asking who, where, which, or why? Is it asking for an exception (NOT, EXCEPT)?\n\n"
              "**Step 2: think of your own answer** before you look at the options, so that the distractors do not confuse you.\n\n"
              "**Step 3: cross out the options you know are wrong.** If two are left, check which fits the exact words of the question.\n\n"
              "**Step 4: mark one answer.** Never leave a question blank. If you do not know, choose the best remaining option and move on. Do not choose by a pattern such as always C."),
            H("Time"),
            T("Fifty questions in the time your teacher gives you means you cannot spend long on any one. In our KKEVO practice settings the Paper 1 mock allows 90 minutes, which is an average of under two minutes a question; this is a practice setting and not an official timing. "
              "Answer the questions you know first, mark the others, and come back. Leave a few minutes at the end to check that every question has an answer."),
            IMG("f5rel-2-passion-timeline.svg", alt="Timeline of the last week of Jesus, as an example of a sequence to learn.", caption="Figure 1. Sequences such as the last week are easy marks if you can draw them from memory."),
            QUIZ("A question asks: 'Which of these was NOT with Jesus at the Transfiguration?' What should you do first?", [
                "Choose the first name you recognise", "Underline NOT and look for the one who was not there", "Skip it without answering", "Choose the longest option"], 1,
                 "Questions with NOT reverse the usual question. Underline the word and look for the odd one out.",
                 hint="Do not miss the word NOT.",
                 feedback=["That would probably be one of the three who were present.", "", "Never leave a blank.", "Length is not a guide to the right answer."]),
            EX("Worked example 1: eliminating options", intro="Who led the Jewish council at the trial of Jesus? Options: A Pilate, B Caiaphas, C Herod, D Barabbas.", steps=[
                S("Own answer first", text="The high priest led the council."),
                S("Cross out", text="Pilate was the Roman governor, Herod was the ruler of Galilee in Luke, and Barabbas was the prisoner who was released."),
                S("Choose", text="B, Caiaphas."),
            ]),
            EX("Worked example 2: sequence", intro="Which came first? A The Council of Jerusalem, B Pentecost, C Paul's first journey, D Stephen's death.", steps=[
                S("Order", text="Pentecost, then Stephen's death, then Paul's first journey, then the Council of Jerusalem."),
                S("Choose", text="B, Pentecost."),
            ]),
            MISTAKE("Mixing up Gospels", "Luke has the Emmaus road, Herod at the trial and the penitent criminal. Matthew has the guards at the tomb. Check which story belongs to which Gospel."),
            MISTAKE("Mixing up Islamic terms", "Hadith is not the Quran. Hijra is not Hajj. Zakat is not sawm. Read each word slowly."),
            MISTAKE("Spending too long", "If a question is taking more than about two minutes, mark it and come back."),
            TIP("Do not guess at details you have never learned. Use the lesson summaries and practice sets for every topic, then take the Paper 1 mock exam under timed conditions.", title="Exam link"),
            QUIZ("Which is the best way to answer a sequence question?", [
                "Choose the event you think is most important", "Put the events in order in your head or on paper and then choose", "Choose the option listed first", "Skip all sequence questions"], 1,
                 "Writing a quick order of events lets you see which comes first or last.",
                 hint="Make a timeline.",
                 feedback=["Importance and order are different things.", "", "The first option is not more likely to be correct.", "These are among the easiest marks if you have learned the order."]),
            PQ("List three kinds of fact you should learn for Paper 1.", "People and what they did; places and events at them; the order of events; the meaning or importance of each event; Islamic terms and their meanings."),
            PQ("What should you do when two options both look right?", "Check them against the exact words of the question, cross out any that mention a different person, place or Gospel, and choose the better fit."),
            PQ("Why should you never leave a question blank?", "There is no reason to lose a possible mark; a considered guess has a chance of being right."),
            SUM("Paper 1 is 50 multiple-choice questions; check the exact format with your teacher.",
                "Learn people, places, sequences and meanings for each module.",
                "Read the stem, think of your answer, then eliminate wrong options.",
                "Watch for distractors from similar stories, and for the words NOT and EXCEPT.",
                "Manage your time and answer every question."),
        ],
    ),
    lesson(
        module=M_EX, topic="Paper 2",
        title="Paper 2: planning and writing good answers",
        slug="relx-paper-2-essay-planning", minutes=22,
        summary="How to answer the written paper: choose the sections you have studied, read the command word, plan in points, use the right names and sources, write with respect and keep to time.",
        objectives=[
            "Explain that candidates answer the sections they have studied",
            "Recognise command words such as describe, explain and discuss",
            "Plan an answer in short points before writing",
            "Use respectful, accurate language for both Christian and Islamic topics",
        ],
        key_concepts=["Paper 2", "Command words", "Essay plan", "Describe and explain", "Respectful language", "Time"],
        blocks=[
            H("Introduction"),
            T("Paper 2 is the written paper of Religious Studies. According to the blueprint used for this course, candidates answer essay-type questions on the sections they have studied. Religious Studies is not covered in the Board's 2023 report, so check the exact format, number of questions and time with your teacher.\n\n"
              "The practice papers on this platform test planning and method using multiple-choice parts, because essays cannot be marked automatically. You should still write full practice essays by hand and ask your teacher to read them."),
            D("A **command word** tells you what to do in the answer: for example *describe*, *explain*, *state*, *outline* or *discuss*.", title="Command word"),
            H("Choosing your questions"),
            T("Before the exam, find out which sections you are expected to prepare: Old Testament, the Gospels, the Early Church (Acts) or Islamic Religious Studies. A candidate should answer the sections that were studied and should not answer questions on a section they have not studied. "
              "In the exam, read all the questions in your sections first. Choose the ones where you know the story well, and number your answers clearly."),
            H("Command words"),
            KEY("What each command word asks", "Match your answer to the word.", cards=[
                ["State / name / list", "Give short facts with no explanation."],
                ["Describe / outline", "Tell what happened, in order, with names and places."],
                ["Explain / why", "Give reasons and show the meaning or importance."],
                ["Discuss / how far", "Give more than one point of view or reason and reach a conclusion."],
            ]),
            H("Planning in five steps"),
            T("Spend two or three minutes on a plan.\n\n"
              "**1.** Read the question and underline the command word and the topic.\n\n"
              "**2.** List four to six points that answer it, using key names and places.\n\n"
              "**3.** Put the points in order, for example the order of events in the story.\n\n"
              "**4.** Write a short introduction that says what you will answer.\n\n"
              "**5.** Write one paragraph for each point, then a short conclusion that answers the question."),
            H("Writing about religion with respect"),
            T("In Christian topics use phrases such as 'Christians believe' and use accurate names. In the Islamic section write 'Muslims believe', and write 'peace be upon him' (or PBUH) after the name of the Prophet Muhammad. "
              "Do not compare religions to rank them, and do not use personal opinion to attack a faith. Describe what believers do and believe, and why it matters to them. "
              "If you are asked for your opinion, give reasons based on the material, not on feelings."),
            IMG("f5rel-2-paul-journeys.svg", alt="A flow chart of Paul's three journeys, as an example of an outline an answer can follow.", caption="Figure 1. An outline like this can become the plan of an essay."),
            H("Worked plans"),
            EX("Model answer plan 1", intro="Describe the conversion of Saul and explain its importance.", steps=[
                S("Introduction", text="State who Saul was and what he did after Stephen's death."),
                S("Describe", text="Road to Damascus, the light and voice, blindness, Ananias, baptism."),
                S("Explain", text="He became the apostle to the Gentiles; Christians see an example of God's grace."),
                S("Conclusion", text="Answer: why it matters to the church."),
            ]),
            EX("Model answer plan 2", intro="Explain the importance of the Five Pillars to Muslims.", steps=[
                S("Introduction", text="Name the five and say that Muslims believe they are the basis of the faith."),
                S("Each pillar", text="Give one sentence on practice and one on meaning."),
                S("Unity", text="Muslims of all nations share these acts."),
                S("Conclusion", text="They shape the daily and yearly life of a Muslim."),
            ]),
            MISTAKE("Retelling without answering", "If the question says explain the importance, a story alone gains little. Add a sentence on meaning to each point."),
            MISTAKE("Bringing in personal opinions or preaching", "Write as a student describing a religion, not as a preacher. Use 'believers hold that' and not 'I think'."),
            MISTAKE("Wrong details", "Do not mix up stories, people or Gospels. If you are not sure of a detail, leave it out rather than inventing it."),
            TIP("Write by hand under time pressure when you practise. Use paragraphs, name the people and places, and keep five minutes for checking. Timings in our practice papers are KKEVO settings, not official.", title="Exam link"),
            QUIZ("A question says: 'Describe the events of Pentecost.' What should your answer do?", [
                "Give a personal opinion about the Holy Spirit", "Tell what happened in order, with details", "List only one word", "Compare Pentecost with another religion"], 1,
                 "Describe means tell what happened, in order, with names and details.",
                 hint="Describe is not the same as explain.",
                 feedback=["Opinions are not asked for.", "", "A word is too short for describe.", "Comparison is not asked and could rank faiths."]),
            PQ("Write a five-point plan for 'Describe the trials of Jesus'.", "Before the council under Caiaphas; Peter's denial; before Pilate; Herod in Luke; Barabbas released and Jesus handed over to be crucified."),
            PQ("What is the difference between describe and explain?", "Describe tells what happened or what believers do; explain gives reasons or shows why it matters."),
            PQ("Give two rules for writing respectfully about the Prophet Muhammad.", "Add peace be upon him after his name; use 'Muslims believe' and avoid disrespectful or comparative language."),
            SUM("Paper 2 is a written paper; candidates answer the sections they have studied, and the exact format should be checked with the teacher.",
                "Read the command word: state, describe, explain or discuss.",
                "Plan four to six points in order before writing.",
                "Use accurate names and respectful words: Christians believe, Muslims believe.",
                "Answer the question set, and leave out details you are not sure of."),
        ],
    ),
]
