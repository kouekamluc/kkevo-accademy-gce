"""Form 5 Religious Studies (O Level 0585), part 2: practice sets for Synoptic Gospels II, the Early Church (Acts),
Islamic Religious Studies and the Examination module (two exam-technique sets and two mocks).

Draft content, descriptive and respectful. Facts are paraphrased from well-established teaching; check dates and
details against the textbook. Religious Studies is not in the Board's 2023 report; the mocks use KKEVO practice
settings (Paper 1: 50 multiple-choice questions, 90 minutes; Paper 2 practice paper: auto-markable parts, 150 minutes),
not official settings.
"""

from .dsl import *  # noqa: F403

COURSE = ("religious-studies", "form-5")

M_S2 = "Synoptic Gospels II: Transfiguration, Passion & Resurrection"
M_AC = "The Early Church: Acts of the Apostles"
M_IS = "Islamic Religious Studies"
M_EX = "Examination"

_PAT = [2, 0, 3, 1, 1, 3, 0, 2]


def Q(prompt, correct, wrongs, step, hint, concept=None, skill="Recall"):
    """Raw question: `wrongs` = [(text, why)] x3; the position of the correct option is set when the set is built."""
    return {"prompt": prompt, "correct": correct, "wrongs": wrongs, "step": step, "hint": hint, "concept": concept, "skill": skill}


def _mc(q, pos, concept):
    choices = [C(t, why=w) for t, w in q["wrongs"]]
    choices.insert(pos, C(q["correct"], correct=True))
    return MC(q["prompt"], choices, steps=[S("Why this is right", text=q["step"])], concept=(q["concept"] or concept),
              skill=q["skill"], hint=q["hint"])


_n = [0]


def ps(module, topic, title, lesson, concept, qs):
    """Practice set (8 questions); the correct option moves around A-D, rotated per set."""
    _n[0] += 1
    return practice_set(module=module, topic=topic, title=title, lesson=lesson,
                        questions=[_mc(q, (_PAT[i] + _n[0]) % 4, concept) for i, q in enumerate(qs)])


def mock(module, topic, title, lesson, minutes, qs):
    pat = [1, 3, 0, 2]
    return practice_set(module=module, topic=topic, title=title, lesson=lesson, mock=True, time_limit_minutes=minutes,
                        questions=[_mc(q, pat[i % 4], "") for i, q in enumerate(qs)])


# ---------------------------------------------------------------------------------------------
# 1. Peter's confession and the Transfiguration
# ---------------------------------------------------------------------------------------------
SET1 = ps(M_S2, "Peter's confession and the Transfiguration", "Peter's confession and the Transfiguration: check your understanding", "rel2-peters-confession-transfiguration", "Peter's confession and the Transfiguration", [
    Q("In which area did Jesus ask his disciples, \"Who do you say that I am?\"", "Around Caesarea Philippi",
      [("Around Capernaum on the lake", "Capernaum was a base for Jesus' Galilean ministry; the confession was in the north."), ("In the Temple in Jerusalem", "This happened long before the last week in Jerusalem."), ("On the Mount of Olives", "The Mount of Olives belongs to the last week.")],
      "The question and Peter's answer came near Caesarea Philippi, a town in the north.", "Think of a town in the north named after Caesar.", skill="Recall"),
    Q("What did Peter say that Jesus is?", "The Messiah",
      [("John the Baptist raised from the dead", "That was an opinion of some of the people, not Peter's answer."), ("Elijah", "That was another opinion of the crowds."), ("A teacher of the law", "Peter's answer was much stronger than this.")],
      "Peter answered that Jesus is the Messiah (in Matthew, the Son of the living God).", "The word means the anointed one.", skill="Recall"),
    Q("Who were the three disciples taken up the mountain at the Transfiguration?", "Peter, James and John",
      [("Peter, Andrew and Philip", "Andrew and Philip were not with Jesus on the mountain."), ("James, John and Judas", "Judas was not one of the three."), ("Peter, Thomas and Matthew", "Thomas and Matthew were not on the mountain.")],
      "The three closest disciples, Peter, James and John, went with Jesus.", "Two of them were brothers, the sons of Zebedee.", skill="Recall"),
    Q("Which two figures appeared with Jesus on the mountain?", "Moses and Elijah",
      [("Abraham and David", "Neither appeared in the account."), ("Isaiah and Jeremiah", "These prophets are not named in the story."), ("Moses and John the Baptist", "John the Baptist is not in the story; the prophet is Elijah.")],
      "Moses and Elijah appeared and talked with Jesus.", "One stands for the Law and one for the prophets.", skill="Recall"),
    Q("What did the voice from the cloud tell the disciples to do?", "Listen to Jesus, God's beloved Son",
      [("Build three shelters", "That was Peter's suggestion, not the voice's command."), ("Go down and tell everyone at once", "Jesus told them to tell no one until after the resurrection."), ("Pray for forty days", "The account says nothing like this.")],
      "The voice said that Jesus is the Son and that they should listen to him.", "What does a voice that speaks from a cloud ask the disciples to do with Jesus' words?", skill="Concept"),
    Q("Why did Jesus tell the disciples not to tell anyone yet that he is the Messiah?", "Many expected a political ruler, and he wished them to understand his mission of suffering first",
      [("He was afraid of the disciples", "The Gospels never say this."), ("He wished to remain unknown for ever", "He taught publicly and wished the message to spread after his resurrection."), ("The Romans had forbidden the title", "The reason given is about the meaning of his mission, not a Roman ban.")],
      "The people's idea of a Messiah was different from the suffering Messiah Jesus taught.", "Think about what people expected a Messiah to do.", skill="Reasoning"),
    Q("What do Christians say the Transfiguration shows?", "That Jesus is God's Son whose glory prepares his followers for the cross",
      [("That Moses was greater than Jesus", "Moses and Elijah point to Jesus; the voice commands listening to Jesus."), ("That the disciples were to build a new Temple", "Peter's offer of shelters was not accepted as a plan."), ("That Jesus would not suffer", "The conversation was about his departure at Jerusalem (Luke).")],
      "It confirms his identity and prepares the disciples for the Passion.", "Link the glory on the mountain to the first prediction of suffering.", skill="Application"),
    Q("Which is the correct order of events?", "Peter's confession, first prediction of suffering, Transfiguration",
      [("Transfiguration, Peter's confession, first prediction of suffering", "The confession comes before the Transfiguration."), ("First prediction of suffering, Transfiguration, Peter's confession", "The prediction follows the confession."), ("Peter's confession, Transfiguration, first prediction of suffering", "The first prediction comes before the mountain, a week or so earlier.")],
      "Confession, prediction of suffering, then the mountain about a week later.", "Which question did Jesus ask first?", skill="Reasoning"),
])

# ---------------------------------------------------------------------------------------------
# 2. Triumphal Entry and the Temple
# ---------------------------------------------------------------------------------------------
SET2 = ps(M_S2, "The Triumphal Entry and the Temple", "Entry into Jerusalem and the Temple: check your understanding", "rel2-triumphal-entry-temple", "The Triumphal Entry and the Temple", [
    Q("On what animal did Jesus ride into Jerusalem?", "A colt",
      [("A white horse", "A horse would suggest war; the Gospels say a colt."), ("A camel", "A camel is not mentioned."), ("A chariot drawn by oxen", "No chariot is mentioned.")],
      "He rode a colt that had never been ridden.", "Think of a young donkey.", skill="Recall"),
    Q("What did the crowd shout as Jesus entered?", "Hosanna",
      [("Amen", "Amen means so be it; the crowd shouted Hosanna."), ("Hallelujah only", "The Gospels record Hosanna."), ("Crucify him", "That was the later cry before Pilate.")],
      "They shouted Hosanna and blessed the one who comes in the name of the Lord.", "The word means save us.", skill="Recall"),
    Q("On which hill was Jesus when he sent two disciples to fetch the colt?", "The Mount of Olives",
      [("Mount Sinai", "Sinai belongs to the story of Moses."), ("Mount Carmel", "Carmel belongs to the story of Elijah."), ("Mount Hermon", "Hermon is not named in the entry.")],
      "The two disciples were sent from near Bethphage and Bethany on the Mount of Olives.", "Think of the hill east of Jerusalem.", skill="Recall"),
    Q("What did Jesus do in the Temple?", "Drove out buyers and sellers and overturned the tables of the money changers",
      [("Burnt the Temple down", "He did not destroy the building."), ("Paid the Temple tax for everyone", "No such story is part of the cleansing."), ("Taught in silence", "He acted and spoke about a house of prayer.")],
      "He cleansed the Temple courts of traders.", "Think of tables and doves.", skill="Recall"),
    Q("What did Jesus say about the Temple when he cleansed it?", "It should be a house of prayer, but they had made it a den of robbers",
      [("It must be rebuilt in seven days", "That is not the cleansing speech."), ("It belongs to the Romans", "He did not say this."), ("It was no longer needed", "He called it a house of prayer.")],
      "He quoted Scripture about a house of prayer.", "Think of prayer and robbers.", skill="Concept"),
    Q("Why do Christians see the colt as important?", "A king on a young donkey comes in peace and humility",
      [("A colt was faster than a horse", "Speed is not the point."), ("Only soldiers rode colts", "The point is the opposite: a sign of peace."), ("It showed Jesus wished to hide", "He entered openly to cheers.")],
      "The animal signals a peaceful king and links to Zechariah's prophecy (Matthew).", "Compare a colt with a war horse.", skill="Application"),
    Q("What was the main message of the Eschatological Discourse on the Mount of Olives?", "Be watchful and faithful because no one knows the day or the hour",
      [("Pay taxes to Caesar", "That was a different question put to Jesus."), ("The Temple would stand for ever", "He said not one stone would be left on another."), ("Stop preaching to the nations", "He said the good news must be preached to all nations.")],
      "Jesus warned of troubles and told them to stay alert.", "Think of the word watchful.", skill="Concept"),
    Q("Why did the Temple leaders plot against Jesus after the cleansing?", "They saw his action as a challenge to their authority and feared the crowd",
      [("They wished to buy the Temple", "No such motive is given."), ("Jesus asked them to leave Jerusalem", "He did not ask this."), ("The Romans ordered it", "The Gospels point to the chief priests and teachers of the law.")],
      "The chief priests and teachers of the law looked for a way to kill him but feared the people.", "Who benefited from the Temple trading?", skill="Reasoning"),
])

# ---------------------------------------------------------------------------------------------
# 3. Last Supper and Gethsemane
# ---------------------------------------------------------------------------------------------
SET3 = ps(M_S2, "The Last Supper and Gethsemane", "The Last Supper and Gethsemane: check your understanding", "rel2-last-supper-gethsemane", "The Last Supper and Gethsemane", [
    Q("Which festival meal did Jesus share with the Twelve before his arrest?", "The Passover meal",
      [("The harvest feast of Pentecost", "Pentecost comes fifty days after Passover."), ("The feast of Tabernacles", "The Synoptic Gospels link the meal to Passover."), ("A wedding feast", "A wedding feast belongs to Cana and parables.")],
      "The Synoptic Gospels describe the Last Supper as a Passover meal.", "It remembers the escape from Egypt.", skill="Recall"),
    Q("What did Jesus say about the bread?", "It is his body",
      [("It is manna from heaven", "Manna belongs to the story of the desert."), ("It is only for the Twelve to eat in secret", "The words are about his body, not secrecy."), ("It is a tax for the Temple", "The bread was not a tax.")],
      "He took bread, gave thanks, broke it and said that it is his body.", "Look at the cup and the bread together.", skill="Recall"),
    Q("What did Jesus call the cup?", "His blood of the covenant",
      [("The wine of the Passover lamb", "He gave it a new meaning."), ("The cup of the Sabbath", "No such term is used."), ("The cup of Moses", "Moses is not mentioned here.")],
      "He said that it is his blood of the covenant, poured out for many.", "Think of the link between covenant and blood at Sinai.", skill="Recall"),
    Q("Who was the disciple who betrayed Jesus?", "Judas Iscariot",
      [("Peter", "Peter denied Jesus but did not hand him over."), ("James", "James was one of the three at Gethsemane."), ("Thomas", "Thomas is remembered for doubting after the resurrection.")],
      "Judas agreed with the chief priests to hand Jesus over.", "He identified Jesus with a kiss.", skill="Recall"),
    Q("What did Jesus foretell about Peter at the Last Supper?", "That Peter would deny him three times that night",
      [("That Peter would betray him for money", "That was Judas."), ("That Peter would run away alone", "All would fall away, and Peter would deny him."), ("That Peter would be crucified at once", "Nothing of that is said here.")],
      "Peter insisted that he would never deny Jesus, but he did.", "The cock crowed.", skill="Concept"),
    Q("What did Jesus pray in Gethsemane?", "That the cup might be taken away if possible, yet God's will be done",
      [("That Judas would be forgiven", "The prayer in Gethsemane was about his own trial."), ("That the disciples would fight", "He told the disciple to put away the sword."), ("That the Temple would be saved", "That is not the theme of the prayer.")],
      "He accepted God's will despite his distress.", "The prayer ends with obedience.", skill="Concept"),
    Q("What were the disciples doing while Jesus prayed in Gethsemane?", "They fell asleep",
      [("They prayed with him all night", "He found them asleep."), ("They kept guard with swords", "Only one used a sword, later, at the arrest."), ("They had already fled", "They fled after the arrest.")],
      "He came back three times and found them sleeping.", "Think of the words 'watch and pray'.", skill="Recall"),
    Q("Which is the best reason why Holy Communion matters to Christians?", "It remembers the death of Jesus and the new covenant and unites believers",
      [("It is a Jewish tax", "It has nothing to do with taxes."), ("It replaces baptism entirely", "Churches understand both as separate acts."), ("It is the same as the Passover meal in every detail", "It began at a Passover meal but has a new meaning for Christians.")],
      "Christians share bread and wine in memory of Jesus.", "Think of memory, covenant and fellowship.", skill="Application"),
])

# ---------------------------------------------------------------------------------------------
# 4. The trials and the crucifixion
# ---------------------------------------------------------------------------------------------
SET4 = ps(M_S2, "The trials and the crucifixion", "The trials and the crucifixion: check your understanding", "rel2-trials-crucifixion", "The trials and the crucifixion", [
    Q("Who was the high priest at the trial of Jesus before the council?", "Caiaphas",
      [("Pilate", "Pilate was the Roman governor."), ("Herod Antipas", "Herod ruled Galilee and appears only in Luke."), ("Barabbas", "Barabbas was a prisoner.")],
      "Caiaphas was the high priest.", "He led the Sanhedrin.", skill="Recall"),
    Q("What did Peter do in the courtyard?", "He denied Jesus three times",
      [("He fought the guards", "He had used a sword at the arrest, not in the courtyard."), ("He spoke for Jesus before the council", "He was in the courtyard, not before the council."), ("He prayed in silence", "He was warming himself and denied Jesus.")],
      "A cock crowed and he wept bitterly.", "Think of the cock.", skill="Recall"),
    Q("Who was the Roman governor who tried Jesus?", "Pontius Pilate",
      [("Caiaphas", "He was the high priest."), ("Julius", "He was the centurion in Acts."), ("Felix", "Felix was a governor in the story of Paul.")],
      "Only the Roman governor could order an execution.", "He asked, Are you the king of the Jews?", skill="Recall"),
    Q("Who was released instead of Jesus?", "Barabbas",
      [("Simon of Cyrene", "He carried the cross."), ("Joseph of Arimathea", "He buried Jesus."), ("Herod", "He was a ruler.")],
      "The crowd chose Barabbas.", "It was the custom to free a prisoner at the festival.", skill="Recall"),
    Q("Which Gospel alone tells of Jesus being sent to Herod Antipas?", "Luke",
      [("Mark", "Mark does not mention Herod at the trial."), ("Matthew", "Matthew does not mention Herod at the trial."), ("All three Synoptic Gospels", "Only Luke has it.")],
      "Luke tells that Pilate sent Jesus to Herod, who mocked him.", "It is the Gospel with the Emmaus road.", skill="Recall"),
    Q("What is the correct order?", "Before the council, Peter's denial, before Pilate, the crucifixion",
      [("Before Pilate, before the council, Peter's denial, the crucifixion", "The Jewish council came first."), ("Peter's denial, the crucifixion, before Pilate, before the council", "The crucifixion came last."), ("The crucifixion, before the council, before Pilate, Peter's denial", "The crucifixion was the end.")],
      "Council, denial in the courtyard, Pilate, the cross.", "Place the cross at the end.", skill="Reasoning"),
    Q("What happened at the death of Jesus according to the Synoptic Gospels?", "Darkness fell and the Temple curtain was torn in two",
      [("The Temple fell", "The curtain was torn, not the whole Temple."), ("The sun shone brightly", "Darkness fell from noon until three."), ("Barabbas was crucified", "He had been released.")],
      "Darkness from noon till three; the curtain of the Temple was torn.", "Two signs: one in the sky, one in the Temple.", skill="Recall"),
    Q("Which statement about responsibility for the death of Jesus is the most accurate and fair?", "The Gospels name particular leaders, the crowd and Pilate; no whole people is to be blamed",
      [("All Jewish people of every age are to blame", "Jesus and his disciples were Jewish, and the Gospels name particular individuals."), ("Only Peter is to blame", "Peter denied Jesus but did not condemn him."), ("The Romans had nothing to do with it", "Pilate gave the order and Roman soldiers carried it out.")],
      "A fair answer names the people involved and does not blame whole groups.", "Look for the answer that names individuals.", skill="Reasoning"),
])

# ---------------------------------------------------------------------------------------------
# 5. The burial and the Resurrection
# ---------------------------------------------------------------------------------------------
SET5 = ps(M_S2, "The burial and the Resurrection", "The burial and the Resurrection: check your understanding", "rel2-burial-resurrection", "The burial and the Resurrection", [
    Q("Who asked Pilate for the body of Jesus?", "Joseph of Arimathea",
      [("Simon of Cyrene", "He carried the cross."), ("Caiaphas", "He was the high priest."), ("Barabbas", "He had been released.")],
      "Joseph, a member of the council, asked Pilate for the body.", "He had a new tomb.", skill="Recall"),
    Q("Where was Jesus buried?", "In a tomb cut out of rock, closed by a large stone",
      [("In the Temple", "He was not buried in the Temple."), ("On Golgotha with the two criminals", "He was laid in a tomb belonging to Joseph."), ("In the river", "He was buried in a rock tomb.")],
      "The body was wrapped in linen and the stone rolled across the entrance.", "Think of the stone.", skill="Recall"),
    Q("When did the women go to the tomb?", "Very early on the first day of the week",
      [("On the Sabbath day", "They rested on the Sabbath."), ("On Thursday evening", "That was the night of the Last Supper."), ("Three weeks later", "They went on the first day of the week.")],
      "They came early on the first day of the week with spices.", "The Sabbath came first.", skill="Recall"),
    Q("What did the women find at the tomb?", "The stone rolled away and the tomb empty",
      [("Soldiers guarding the open tomb", "The guards are in Matthew, and they did not find an empty tomb with the women there."), ("Joseph of Arimathea waiting", "He is not mentioned at the empty tomb."), ("The body wrapped and ready for burial", "They found the tomb empty.")],
      "The tomb was empty; a messenger told them that he was risen.", "What had happened to the stone?", skill="Recall"),
    Q("Which Gospel tells of the walk to Emmaus?", "Luke",
      [("Mark", "The oldest manuscripts of Mark end with the women's fear."), ("Matthew", "Matthew ends with the commission on a mountain."), ("None of them", "It is in Luke.")],
      "Two disciples met Jesus on the road and knew him when he broke bread.", "It is the Gospel that continues in Acts.", skill="Recall"),
    Q("What is the Great Commission?", "The command to go and make disciples of all nations",
      [("The command to build a new Temple", "That is not the Great Commission."), ("The command to stay in Jerusalem and not teach", "The command is to go to all nations."), ("The command to avoid the Gentiles", "The command is for all nations.")],
      "In Matthew the risen Jesus sent them to all nations, baptising and teaching.", "Think of a mountain in Galilee.", skill="Concept"),
    Q("Which detail is found only in Matthew?", "The guards at the tomb",
      [("The walk to Emmaus", "That is in Luke."), ("The two criminals", "The two criminals are in all three Gospels."), ("The women watching the burial", "All three have the women.")],
      "Only Matthew has the guards and the sealed stone.", "Think of the chief priests and Pilate.", skill="Reasoning"),
    Q("Why is the Resurrection central for Christians?", "They believe God raised Jesus from the dead, so death is not the end and his message is confirmed",
      [("It proves that the Temple was rebuilt", "The Temple is not the focus of the Resurrection."), ("It ended the Passover festival", "The Resurrection did not end Passover."), ("It showed that Pilate was right", "The Resurrection reverses the verdict on the cross.")],
      "It is the central belief of the Christian faith.", "Think of life after death.", skill="Application"),
])
# ---------------------------------------------------------------------------------------------
# 6. The Ascension and Pentecost
# ---------------------------------------------------------------------------------------------
SET6 = ps(M_AC, "The Ascension and Pentecost", "The Ascension and Pentecost: check your understanding", "rel2-ascension-pentecost", "The Ascension and Pentecost", [
    Q("Who is traditionally said to have written the Acts of the Apostles?", "Luke",
      [("Mark", "Mark wrote the earliest Gospel, not Acts."), ("Paul", "Paul wrote letters; Acts is about his journeys."), ("Peter", "Peter is a main figure in the early chapters but is not named as the author.")],
      "Christian tradition says Luke wrote both his Gospel and Acts.", "Acts continues the story of the third Gospel.", skill="Recall"),
    Q("From which hill did the apostles return to Jerusalem after the Ascension?", "The Mount of Olives",
      [("Mount Sinai", "Sinai is in the story of Moses."), ("Mount Zion in Samaria", "The text names the Mount of Olives."), ("Mount Carmel", "Carmel belongs to Elijah.")],
      "They returned from the Mount of Olives.", "The same hill was in the story of the entry.", skill="Recall"),
    Q("Who replaced Judas among the Twelve?", "Matthias",
      [("Barnabas", "Barnabas was not chosen to replace Judas."), ("Stephen", "Stephen was one of the Seven."), ("Saul", "Saul was chosen by the Lord on the road to Damascus, much later.")],
      "The lot fell on Matthias.", "The other candidate was Joseph Barsabbas.", skill="Recall"),
    Q("How was Matthias chosen?", "After prayer, by casting lots between two men",
      [("By a vote of the Sanhedrin", "The apostles and believers chose, not the Sanhedrin."), ("By Pilate", "Pilate had no part."), ("By a decree of Peter alone", "They prayed and cast lots.")],
      "They prayed and cast lots.", "Two names were put forward.", skill="Recall"),
    Q("How many days after Passover was the festival of Pentecost?", "Fifty",
      [("Seven", "Seven days is a week."), ("Forty", "Forty days is the time from the resurrection to the Ascension."), ("Ten", "Ten days is the gap between the Ascension and Pentecost.")],
      "Pentecost was fifty days after Passover.", "Pente means fifty.", skill="Recall"),
    Q("Which signs accompanied the coming of the Spirit at Pentecost?", "A sound like a strong wind and tongues like fire",
      [("An earthquake and a flood", "The earthquake is in the Philippi prison story."), ("A cloud and a voice", "That was the Transfiguration."), ("A star and angels singing", "That is the Christmas story.")],
      "Wind, fire and speaking in other languages.", "Think of wind and flames.", skill="Recall"),
    Q("What did Peter tell the crowd to do?", "Repent and be baptised in the name of Jesus",
      [("Leave Jerusalem at once", "Peter told them to repent and be baptised."), ("Return to the Temple sacrifices only", "He called them to repentance and baptism."), ("Wait for forty days in silence", "No such command is given.")],
      "About three thousand people were baptised.", "He spoke about the forgiveness of sins.", skill="Concept"),
    Q("Why is Pentecost sometimes called the birthday of the church?", "The Spirit came, Peter preached and about three thousand joined the believers",
      [("Jesus was born on that day", "Christians celebrate the birth of Jesus at Christmas."), ("The Temple was built then", "The Temple is not linked to Pentecost in this way."), ("The Twelve were first chosen then", "The Twelve were chosen during the ministry of Jesus.")],
      "It was the day when the church began to grow rapidly.", "Think of the number baptised.", skill="Application"),
])

# ---------------------------------------------------------------------------------------------
# 7. Life in the early church
# ---------------------------------------------------------------------------------------------
SET7 = ps(M_AC, "Life in the early church", "Life in the early church: check your understanding", "rel2-life-early-church", "Life in the early church", [
    Q("Which of these was NOT one of the four things the first believers devoted themselves to?", "Building a new Temple",
      [("The apostles' teaching", "This was one of the four."), ("The breaking of bread", "This was one of the four."), ("Prayer", "This was one of the four.")],
      "The four were the teaching, fellowship, the breaking of bread and the prayers.", "Look for the odd one out.", skill="Recall"),
    Q("What does the name Barnabas mean?", "Son of encouragement",
      [("Son of thunder", "That name was given to James and John."), ("Man of the rock", "That describes Peter."), ("Son of the law", "It does not mean this.")],
      "Joseph, called Barnabas, sold a field and gave the money.", "The apostles gave him this name.", skill="Recall"),
    Q("What was the sin of Ananias and Sapphira?", "Lying about the price of the land they sold",
      [("Refusing to sell their land", "Nobody forced them to sell."), ("Stealing from the Temple", "They kept part of their own money."), ("Not attending the prayers", "Attendance is not mentioned.")],
      "They pretended to give the whole amount.", "Peter said the land was theirs to keep.", skill="Recall"),
    Q("Where was the lame man healed by Peter and John?", "At the Temple gate called Beautiful",
      [("At Lystra", "Paul healed a lame man in Lystra."), ("At the pool of Siloam", "That is a different story."), ("At Lydda", "Peter healed Aeneas at Lydda.")],
      "He was begging at the gate and Peter said, in the name of Jesus, walk.", "The gate's name is an adjective.", skill="Recall"),
    Q("What did Peter and John answer when the council told them to stop speaking about Jesus?", "That they must obey God rather than human beings",
      [("That they would stop at once", "They refused to stop."), ("That the council was above God", "They said the opposite."), ("That they would ask Rome", "No such reply is given.")],
      "They said they could not stop speaking about what they had seen and heard.", "Who must be obeyed first?", skill="Concept"),
    Q("Why were the Seven chosen?", "To manage the daily distribution to widows while the apostles preached",
      [("To replace Judas", "Matthias replaced Judas."), ("To lead the Temple worship", "The Seven did not do this."), ("To travel to Rome", "They worked in Jerusalem first.")],
      "The Greek-speaking widows complained of being overlooked.", "Think of serving at tables.", skill="Concept"),
    Q("Who were two of the Seven?", "Stephen and Philip",
      [("Peter and John", "They were among the Twelve."), ("Barnabas and Saul", "These came to Antioch later."), ("Ananias and Sapphira", "They died after lying.")],
      "Stephen and Philip are named among the seven.", "One was later stoned, the other preached in Samaria.", skill="Recall"),
    Q("What does the story of Ananias and Sapphira teach the church?", "The importance of honesty before God and the community",
      [("That all property must be sold", "Peter said the property was theirs to keep."), ("That giving is wrong", "The story is praised for generosity such as Barnabas'."), ("That the apostles should be rich", "Nothing like this is taught.")],
      "The sin was the lie, not the amount.", "Compare them with Barnabas.", skill="Application"),
])

# ---------------------------------------------------------------------------------------------
# 8. Stephen and the conversion of Saul
# ---------------------------------------------------------------------------------------------
SET8 = ps(M_AC, "Stephen and the conversion of Saul", "Stephen and the conversion of Saul: check your understanding", "rel2-stephen-conversion-saul", "Stephen and the conversion of Saul", [
    Q("What is a martyr?", "A person who dies because of their faith",
      [("A person who teaches in a synagogue", "A teacher is not necessarily a martyr."), ("A person who travels to Rome", "This has no link with the word."), ("A person who is baptised", "Baptism is different.")],
      "The Greek word means witness; Stephen is the first Christian martyr.", "Think of what happened to Stephen.", skill="Recall"),
    Q("How did Stephen die?", "He was stoned outside the city",
      [("He was beheaded by Herod", "James was killed with the sword."), ("He was crucified", "That was the death of Jesus."), ("He was drowned in a shipwreck", "That does not appear in Acts.")],
      "The crowd dragged him out of the city and stoned him.", "The witnesses laid their coats at someone's feet.", skill="Recall"),
    Q("Who approved of the killing of Stephen and held the coats?", "Saul",
      [("Barnabas", "Barnabas later introduced Saul to the apostles."), ("Philip", "Philip was one of the Seven."), ("Ananias", "Ananias healed Saul later.")],
      "The witnesses laid their coats at the feet of a young man named Saul.", "He was a Pharisee from Tarsus.", skill="Recall"),
    Q("What did Stephen pray as he died?", "That the Lord would not hold the sin against them",
      [("That God would destroy his enemies", "He prayed the opposite."), ("That the Temple would be rebuilt", "This is not part of the prayer."), ("That Saul would be blinded", "Saul was blinded on the road later, not by Stephen's prayer.")],
      "He also asked the Lord Jesus to receive his spirit.", "His prayer echoed the forgiveness of Jesus.", skill="Concept"),
    Q("Where was Saul going when he met the risen Jesus?", "To Damascus",
      [("To Rome", "He reached Rome as a prisoner much later."), ("To Antioch in Pisidia", "That was on the first journey."), ("To Caesarea", "Not on this journey.")],
      "He went with letters from the high priest to arrest believers.", "A city in Syria.", skill="Recall"),
    Q("What happened to Saul after the vision?", "He was blind for three days",
      [("He lost his voice", "He was blind."), ("He was struck lame", "No such thing is recorded."), ("He was put in prison by Ananias", "Ananias healed him.")],
      "Ananias laid hands on him and he could see again and was baptised.", "Think of the scales that fell from his eyes.", skill="Recall"),
    Q("Who introduced Saul to the apostles in Jerusalem?", "Barnabas",
      [("Peter", "The apostles were afraid of Saul until Barnabas spoke for him."), ("Stephen", "Stephen had already been killed."), ("Philip", "Philip was in Samaria and on the Gaza road.")],
      "Barnabas told them how Saul had seen the Lord and preached boldly.", "The name means son of encouragement.", skill="Recall"),
    Q("What is the best summary of the importance of Saul's conversion?", "A persecutor became the apostle to the Gentiles",
      [("The Twelve became thirteen", "Paul was not added to the Twelve."), ("The Council of Jerusalem was held", "That was a later event."), ("Rome gave citizenship to believers", "Saul was already a Roman citizen.")],
      "His change led to the mission to the Gentiles.", "Think of what Saul was before and after.", skill="Application"),
])

# ---------------------------------------------------------------------------------------------
# 9. Peter's ministry and the Council of Jerusalem
# ---------------------------------------------------------------------------------------------
SET9 = ps(M_AC, "Peter's ministry and the Council of Jerusalem", "Peter's ministry and the Council: check your understanding", "rel2-peter-ministry-council-jerusalem", "Peter's ministry and the Council of Jerusalem", [
    Q("Who was the paralysed man healed by Peter at Lydda?", "Aeneas",
      [("Tabitha", "Tabitha was raised at Joppa."), ("Cornelius", "Cornelius was a centurion."), ("Eutychus", "Eutychus fell from a window in Troas.")],
      "Peter said, Jesus Christ heals you.", "Eight years in bed.", skill="Recall"),
    Q("Whom did Peter raise to life at Joppa?", "Tabitha (Dorcas)",
      [("Aeneas", "Aeneas was healed at Lydda."), ("Eutychus", "Paul restored Eutychus."), ("Rhoda", "Rhoda was the servant girl at Mary's house.")],
      "She was known for helping the poor.", "She made clothes.", skill="Recall"),
    Q("Who was Cornelius?", "A Roman centurion in Caesarea who feared God",
      [("A Pharisee in Jerusalem", "He was a Gentile."), ("The high priest", "Caiaphas was the high priest."), ("The governor of Judea", "He was a centurion.")],
      "He sent for Peter after an angel told him to.", "Think of his rank and his town.", skill="Recall"),
    Q("What did Peter's vision of the sheet teach him?", "Not to call anyone impure whom God has made clean",
      [("That he should stop eating meat", "The voice told him to eat."), ("That he should leave Joppa for ever", "The vision led him to Cornelius."), ("That Gentiles must be circumcised", "The vision led to the opposite conclusion.")],
      "God shows no favouritism.", "Think of the Gentiles.", skill="Concept"),
    Q("Who killed James the brother of John and arrested Peter?", "Herod Agrippa I",
      [("Pilate", "Pilate had gone long before."), ("Festus", "Festus was a governor in Paul's story."), ("Caiaphas", "Caiaphas was a high priest during the trial of Jesus.")],
      "An angel freed Peter from prison.", "He was a king.", skill="Recall"),
    Q("Why was the Council of Jerusalem held?", "To decide whether Gentile believers had to be circumcised and keep the law of Moses",
      [("To choose a replacement for Judas", "Matthias was chosen earlier."), ("To try Paul for blasphemy", "Paul was a delegate."), ("To plan the voyage to Rome", "The council took place before the voyage.")],
      "Some insisted that Gentiles must become Jews.", "Think of Antioch.", skill="Concept"),
    Q("Which of these was NOT among the requests in the council's letter?", "To keep the whole law of Moses",
      [("To avoid food offered to idols", "This was in the letter."), ("To avoid blood and the meat of strangled animals", "This was in the letter."), ("To avoid sexual immorality", "This was in the letter.")],
      "The letter burdened the Gentiles with only a few necessary things.", "The council reduced the requirements.", skill="Reasoning"),
    Q("Who gave the final verdict at the Council?", "James, the leader of the Jerusalem church",
      [("Cornelius", "He was a Gentile in Caesarea."), ("Herod", "Herod had no part."), ("Stephen", "Stephen was dead.")],
      "James quoted the prophets and said not to make it difficult for the Gentiles.", "Not the apostle John's brother.", skill="Recall"),
])

# ---------------------------------------------------------------------------------------------
# 10. Paul's missionary journeys and the voyage to Rome
# ---------------------------------------------------------------------------------------------
SET10 = ps(M_AC, "Paul's missionary journeys and the voyage to Rome", "Paul's journeys and the voyage to Rome: check your understanding", "rel2-paul-journeys-voyage-rome", "Paul's missionary journeys and the voyage to Rome", [
    Q("From which city did Paul's journeys begin?", "Antioch in Syria",
      [("Jerusalem", "The church at Jerusalem was the centre of the early church, but the journeys began in Antioch."), ("Rome", "He reached Rome at the end."), ("Corinth", "He stayed in Corinth during the second journey.")],
      "The church at Antioch sent out Barnabas and Saul.", "Believers were first called Christians there.", skill="Recall"),
    Q("Who went with Paul on the first journey?", "Barnabas, with John Mark as helper",
      [("Silas and Timothy", "That was the second journey."), ("Luke and Aristarchus", "They were with him on the voyage to Rome."), ("Aquila and Priscilla", "He met them in Corinth.")],
      "Barnabas and Saul were sent out, with John Mark.", "The second journey was with Silas.", skill="Recall"),
    Q("At Lystra the people thought Paul and Barnabas were:", "Gods",
      [("Roman officials", "They were taken for gods."), ("Thieves", "They were healers, not thieves."), ("Soldiers", "Not in this story.")],
      "Paul healed a lame man.", "Zeus and Hermes.", skill="Recall"),
    Q("Who was the woman at Philippi, a dealer in purple cloth, who was baptised?", "Lydia",
      [("Priscilla", "Priscilla was a tentmaker in Corinth."), ("Tabitha", "Tabitha was in Joppa."), ("Sapphira", "Sapphira died after lying to Peter.")],
      "She and her household were baptised.", "A seller of purple cloth.", skill="Recall"),
    Q("What led the jailer at Philippi to ask what he must do to be saved?", "An earthquake opened the doors while Paul and Silas prayed and sang",
      [("A voice from the cloud", "That was the Transfiguration."), ("The riot in Ephesus", "That is a different story."), ("A shipwreck", "That is on the voyage to Rome.")],
      "The jailer and his family were baptised.", "It was midnight.", skill="Concept"),
    Q("Why was there a riot in Ephesus?", "Silversmiths feared that Paul's preaching would harm the trade in shrines of Artemis",
      [("Paul had insulted Caesar", "That is not the reason."), ("The Council of Jerusalem had failed", "That is not the reason."), ("Paul had refused to pay taxes", "No such thing is stated.")],
      "Demetrius made silver shrines of Artemis.", "Think of money.", skill="Reasoning"),
    Q("What right did Paul use when he said 'I appeal to Caesar'?", "His right as a Roman citizen to be tried by the emperor",
      [("The right of a priest", "He was not a priest."), ("The right of a king", "He was not a king."), ("The right of the Sanhedrin", "The Sanhedrin was the Jewish council.")],
      "Festus would have sent him back to Jerusalem.", "Think of his citizenship.", skill="Concept"),
    Q("What happened to the ship carrying Paul to Rome?", "It ran aground in a storm and all 276 on board reached land at Malta",
      [("It reached Rome in a few days", "There was a long storm and a shipwreck."), ("It sank with all on board", "All reached land safely."), ("It returned to Caesarea", "It was wrecked at Malta.")],
      "Everyone survived and Paul later reached Rome.", "Fourteen days of storm.", skill="Recall"),
])
# ---------------------------------------------------------------------------------------------
# 11. Pre-Islamic Arabia
# ---------------------------------------------------------------------------------------------
SET11 = ps(M_IS, "Pre-Islamic Arabia", "Arabia before Islam: check your understanding", "rel2-pre-islamic-arabia", "Pre-Islamic Arabia", [
    Q("What does the word Jahiliyyah refer to?", "The period in Arabia before Islam",
      [("The Muslim calendar", "The calendar is the Hijri calendar."), ("The month of fasting", "That is Ramadan."), ("The pilgrimage to Mecca", "That is the Hajj.")],
      "Muslims use the word for the time of ignorance of God's guidance before Islam.", "It refers to the time before the revelation.", skill="Recall"),
    Q("Who were the Bedouin?", "Nomadic Arabs who moved with camels and flocks in the desert",
      [("Merchants who lived in Mecca all year", "Those were settled townspeople."), ("Soldiers of the Persian Empire", "The Bedouin were Arab nomads."), ("Priests of the Kaaba", "They were not priests.")],
      "They moved in search of water and pasture.", "Think of the desert and camels.", skill="Recall"),
    Q("Which tribe controlled Mecca at the time of the Prophet's birth?", "The Quraysh",
      [("The Aws", "The Aws were a tribe in Yathrib."), ("The Khazraj", "The Khazraj were also in Yathrib."), ("The Ghassan", "The Ghassan were a kingdom near Syria.")],
      "The Prophet belonged to the Quraysh.", "They were merchants and guardians of the Kaaba.", skill="Recall"),
    Q("Why was the tribe so important in Arabian society?", "It gave protection and identity in a land without a strong central state",
      [("It collected taxes for a king", "There was no king over all Arabia."), ("It controlled the schools", "Tribal loyalty was about protection."), ("It decided which prophet to follow", "Religion was not decided in this way.")],
      "A person without a tribe was in danger.", "Think of safety.", skill="Concept"),
    Q("What was the Kaaba before Islam, in the Muslim view?", "A shrine built by Ibrahim and Ismail for the worship of the One God, later filled with idols",
      [("A Persian palace", "It was a shrine."), ("A Roman fort", "It was not a fort."), ("The tomb of the Quraysh leader", "It is not a tomb.")],
      "Muslims believe the Arabs later turned to idols.", "Which two prophets built it?", skill="Concept"),
    Q("Who were the hanifs?", "People who looked for the pure faith of Ibrahim and worshipped one God",
      [("Traders from Persia", "The term refers to monotheists."), ("The guardians of the idols", "They rejected idols."), ("Roman soldiers", "They were not soldiers.")],
      "A few Arabs rejected idols before Islam.", "One God.", skill="Recall"),
    Q("Which statement about religion in Arabia before Islam is most accurate?", "Most Arabs worshipped many gods, and there were also hanifs, Jews and Christians",
      [("All Arabs believed in one God", "Many worshipped idols."), ("There were no Jews or Christians in Arabia", "There were Jewish and Christian communities."), ("All Arabs were Christians", "Christians were present in places only.")],
      "The picture was mixed.", "Choose the answer that gives a mixed picture.", skill="Reasoning"),
    Q("Why was Mecca an important town before Islam?", "It lay on trade routes and had the Kaaba, which drew pilgrims",
      [("It was the capital of an Arab empire", "There was no single Arab empire."), ("It was the centre of the Roman army", "It was not a Roman base."), ("It had the largest army in Arabia", "Its importance was trade and the shrine.")],
      "The Quraysh were merchants who cared for pilgrims.", "Think of caravans and pilgrims.", skill="Application"),
])

# ---------------------------------------------------------------------------------------------
# 12. The life and prophethood of Muhammad
# ---------------------------------------------------------------------------------------------
SET12 = ps(M_IS, "The life and prophethood of Muhammad", "The life of the Prophet Muhammad: check your understanding", "rel2-life-prophethood-muhammad", "The life and prophethood of Muhammad", [
    Q("In which city was the Prophet Muhammad, peace be upon him, born?", "Mecca",
      [("Medina", "He migrated to Medina and died there."), ("Jerusalem", "Jerusalem is not his birthplace."), ("Cairo", "He was never born in Cairo.")],
      "He was born in Mecca in the tribe of the Quraysh.", "The town of the Kaaba.", skill="Recall"),
    Q("What was the Prophet called before his prophethood because of his honesty?", "Al-Amin, the trustworthy",
      [("Al-Siddiq", "That title is linked to Abu Bakr."), ("Al-Farooq", "That title is linked to Umar."), ("Al-Bukhari", "That is the name of a hadith collector.")],
      "People trusted him with their goods.", "Think of trust.", skill="Recall"),
    Q("Who was the first person to accept Islam, according to Muslim tradition?", "Khadija",
      [("Abu Jahl", "He opposed the Prophet."), ("Abu Lahab", "He opposed the Prophet."), ("Bilal ibn Rabah", "Bilal accepted Islam but the first was Khadija.")],
      "She comforted him after the first revelation.", "His wife.", skill="Recall"),
    Q("Where did the first revelation come?", "In the cave of Hira, near Mecca",
      [("In the Kaaba", "It was not in the Kaaba."), ("In Medina", "Medina came after the Hijra."), ("On Mount Sinai", "Sinai belongs to Moses.")],
      "Jibril said, Read.", "A cave on a mountain.", skill="Recall"),
    Q("Why did the Quraysh leaders oppose the Prophet's message?", "He rejected idols, which threatened their trade and their role as guardians of the Kaaba",
      [("He demanded all their wealth", "He called for justice and charity, not the seizure of wealth."), ("He allied with the Persians", "There was no such alliance."), ("He asked them to leave Arabia", "He did not.")],
      "The Quraysh benefited from pilgrims to the Kaaba.", "Think of money and honour.", skill="Reasoning"),
    Q("What is the Hijra?", "The migration from Mecca to Medina in 622 CE",
      [("The first pilgrimage", "The pilgrimage is the Hajj."), ("The conquest of Mecca", "The return to Mecca came later."), ("The Night of Power", "That is the night of the first revelation.")],
      "It is the start of the Islamic calendar.", "The word means migration.", skill="Concept"),
    Q("What were the Ansar?", "The helpers of Medina who welcomed the Muslims from Mecca",
      [("The Muslims who migrated from Mecca", "They were the Muhajirun."), ("The Quraysh leaders", "They were the opponents in Mecca."), ("The Persian soldiers", "No.")],
      "The Muhajirun were the emigrants.", "Helpers.", skill="Recall"),
    Q("Which is the correct order of events?", "First revelation, Hijra to Medina, return to Mecca, death of the Prophet",
      [("Hijra to Medina, first revelation, return to Mecca, death of the Prophet", "The first revelation came before the Hijra."), ("First revelation, return to Mecca, Hijra to Medina, death of the Prophet", "The return to Mecca came after the Hijra."), ("Return to Mecca, first revelation, Hijra to Medina, death of the Prophet", "The first revelation came much earlier.")],
      "Revelation, opposition, Hijra, return, death.", "Medina is the second home.", skill="Reasoning"),
])

# ---------------------------------------------------------------------------------------------
# 13. The Quran
# ---------------------------------------------------------------------------------------------
SET13 = ps(M_IS, "The Quran", "The Quran: check your understanding", "rel2-the-quran", "The Quran", [
    Q("Through which angel do Muslims believe the Quran was revealed?", "Jibril (Gabriel)",
      [("Mikail", "Mikail is another angel."), ("Israfil", "Israfil is the angel linked with the trumpet."), ("Azrail", "Azrail is linked with death.")],
      "Jibril brought the revelation to the Prophet.", "The angel who came to the cave of Hira.", skill="Recall"),
    Q("About how long did the revelation of the Quran last?", "About 23 years",
      [("One night only", "The first revelation was in one night, but it continued."), ("About 5 years", "It lasted much longer."), ("About 40 years", "He began to receive revelation at about forty years of age.")],
      "It was revealed piece by piece.", "More than twenty.", skill="Recall"),
    Q("How many surahs are there in the Quran?", "114",
      [("30", "30 is the number of juz."), ("99", "99 is the number of the names of God."), ("124", "Not the number of surahs.")],
      "There are 114 surahs.", "More than 100.", skill="Recall"),
    Q("What is a hafiz?", "A person who has memorised the whole Quran",
      [("A scribe who copies manuscripts", "A hafiz memorises it."), ("A person who calls to prayer", "That is a muezzin."), ("A caliph", "A caliph is a leader.")],
      "Memorisation has continued to the present day.", "Think of memory.", skill="Concept"),
    Q("Who collected the Quran into one volume under the first caliph?", "Zayd ibn Thabit",
      [("Uthman", "Uthman had standard copies made later."), ("Bilal", "Bilal called to prayer."), ("Abu Talib", "He was the Prophet's uncle.")],
      "Zayd compared the written pieces with the memory of the reciters.", "A scribe of the Prophet.", skill="Recall"),
    Q("What did Uthman do?", "Had standard copies prepared and sent to the main cities",
      [("Wrote the Quran himself", "Muslims believe it was revealed to the Prophet."), ("Burned all copies", "He had other versions set aside, but standard copies were sent out."), ("Translated it into Latin", "That was not his action.")],
      "A committee led by Zayd prepared the copies.", "Think of the third caliph.", skill="Concept"),
    Q("Which is the first surah in the Quran?", "Al-Fatiha",
      [("Al-Baqarah", "Al-Baqarah is the second and longest surah."), ("Al-Ikhlas", "Al-Ikhlas is near the end."), ("Al-Nas", "Al-Nas is the last surah.")],
      "It is recited in every prayer.", "The Opening.", skill="Recall"),
    Q("Why do Muslims treat the Arabic text as the Quran, and not a translation?", "They believe the words revealed in Arabic are God's word, and translations help to explain the meaning",
      [("Translations are forbidden", "Translations are used for understanding."), ("Arabic is the only language that exists", "That is false."), ("The Arabic text is a later addition", "Muslims believe the Arabic is the original revelation.")],
      "Muslims distinguish the revealed text from explanations.", "Think of what was revealed.", skill="Reasoning"),
])

# ---------------------------------------------------------------------------------------------
# 14. Hadith
# ---------------------------------------------------------------------------------------------
SET14 = ps(M_IS, "Hadith", "Hadith: check your understanding", "rel2-hadith", "Hadith", [
    Q("What is a hadith?", "A report of what the Prophet said, did or approved",
      [("A chapter of the Quran", "A chapter is a surah."), ("A prayer said at dawn", "That is fajr."), ("A pilgrimage rite", "That is part of the Hajj.")],
      "Hadith are reports passed on by narrators.", "The Prophet's words and actions.", skill="Recall"),
    Q("What is the sunnah?", "The example or practice of the Prophet",
      [("The month of fasting", "That is Ramadan."), ("A collection of prayers", "The sunnah is his example."), ("The call to prayer", "That is the adhan.")],
      "It is known through the hadith.", "The way of the Prophet.", skill="Recall"),
    Q("What is the isnad?", "The chain of narrators",
      [("The text of the hadith", "That is the matn."), ("The date of the hadith", "Not the isnad."), ("The book that contains hadith", "Not the isnad.")],
      "Each narrator names the one he heard it from.", "The other part is the matn.", skill="Recall"),
    Q("Which grade means a hadith with a continuous chain of reliable narrators?", "Sahih",
      [("Daif", "Daif means weak."), ("Hasan", "Hasan means good, slightly lower."), ("Matn", "Matn is the text.")],
      "Sahih means sound.", "Sound.", skill="Concept"),
    Q("Who compiled Sahih al-Bukhari?", "Muhammad al-Bukhari",
      [("Muslim ibn al-Hajjaj", "He compiled Sahih Muslim."), ("Zayd ibn Thabit", "He was a scribe of the Quran."), ("Uthman", "He was a caliph.")],
      "It is one of the best-known collections.", "The name is in the title.", skill="Recall"),
    Q("Why were scholars careful to check the narrators of hadith?", "Some reports were weak or invented, so they tested honesty, memory and the continuity of the chain",
      [("To prove that the Quran was incomplete", "That is not their aim."), ("To forbid the use of hadith", "The aim was to separate reliable reports from weak ones."), ("To translate hadith", "Not the reason.")],
      "Reliability matters because hadith guide worship and conduct.", "Think of reliability.", skill="Reasoning"),
    Q("How do hadith help Muslims perform the prayer?", "They show the details of how the Prophet prayed",
      [("They replace the Quran in the prayer", "The Quran is recited in prayer."), ("They say that prayer is optional", "The Quran commands prayer."), ("They give the number of surahs", "That is not the purpose.")],
      "The Quran commands prayer and the sunnah shows the way.", "Think of details.", skill="Application"),
    Q("Which statement about the Quran and hadith is correct?", "The Quran is the first source of guidance and the hadith, the sunnah, is the second",
      [("They are the same book", "They are different."), ("Hadith are the word of God like the Quran", "Muslims regard the Quran as God's word; hadith report the Prophet."), ("Hadith came before the Quran", "The Quran was revealed first.")],
      "The two are used together.", "Order of importance.", skill="Concept"),
])

# ---------------------------------------------------------------------------------------------
# 15. The Five Pillars of Islam
# ---------------------------------------------------------------------------------------------
SET15 = ps(M_IS, "The Five Pillars of Islam", "The Five Pillars of Islam: check your understanding", "rel2-five-pillars-islam", "The Five Pillars of Islam", [
    Q("Which pillar is the declaration of faith?", "Shahada",
      [("Salat", "Salat is prayer."), ("Zakat", "Zakat is almsgiving."), ("Sawm", "Sawm is fasting.")],
      "There is no god but God and Muhammad is his Messenger.", "The pillar that is a statement.", skill="Recall"),
    Q("How many times a day do Muslims pray?", "Five",
      [("Three", "Some prayers have three units, but the daily prayers are five in number."), ("Seven", "Seven is the number of circuits round the Kaaba, not of daily prayers."), ("Once", "Friday has a weekly congregational prayer, but the daily prayers are five.")],
      "Fajr, dhuhr, asr, maghrib and isha.", "Name the prayers.", skill="Recall"),
    Q("What is the direction that Muslims face to pray?", "The qibla, towards the Kaaba in Mecca",
      [("Towards Medina", "The qibla is the Kaaba in Mecca."), ("Towards Jerusalem", "That was an earlier direction; the qibla is the Kaaba."), ("Towards the East", "Not in every place.")],
      "Muslims face the Kaaba.", "A shrine in Mecca.", skill="Recall"),
    Q("About what share of qualifying savings is paid as zakat?", "2.5 per cent",
      [("1 per cent", "Too low; the usual rate is one-fortieth."), ("10 per cent", "Ten per cent is a tithe in some traditions, not the usual zakat rate on savings."), ("50 per cent", "Zakat is a small fixed share, not half of savings.")],
      "One-fortieth of qualifying savings held for a year.", "One-fortieth.", skill="Recall"),
    Q("In which month do Muslims fast?", "Ramadan",
      [("Dhul-Hijjah", "Dhul-Hijjah is the month of the Hajj."), ("Muharram", "Muharram is the first month."), ("Rajab", "Rajab is a different month.")],
      "Ramadan is the ninth month.", "The month of the first revelation.", skill="Recall"),
    Q("Which of these is excused from fasting?", "A person who is ill",
      [("A healthy adult at home", "A healthy adult must fast."), ("A shopkeeper who is busy", "Work does not excuse the fast."), ("A student with an exam", "An exam does not excuse the fast.")],
      "Sick people, travellers, young children, elderly and pregnant women may be excused.", "Think of health.", skill="Application"),
    Q("What are the main rites of the Hajj?", "Wearing ihram, walking round the Kaaba, standing at Arafat",
      [("Fasting for forty days", "Not a rite of the Hajj."), ("Giving 2.5 per cent of savings", "That is zakat."), ("Reciting the shahada once", "Not a rite of the Hajj.")],
      "Tawaf, sai, Arafat, Muzdalifah and Mina.", "Think of white clothes and the Kaaba.", skill="Concept"),
    Q("Why do pilgrims wear simple white clothes in ihram?", "To show that all believers are equal before God",
      [("To show that they are rich", "It does the opposite."), ("To hide from enemies", "Not the reason."), ("Because the clothes are the uniform of Mecca", "It is a sign of purity and equality.")],
      "Rich and poor dress alike.", "Think of equality.", skill="Reasoning"),
])
# ---------------------------------------------------------------------------------------------
# 16. Paper 1 strategy
# ---------------------------------------------------------------------------------------------
SET16 = ps(M_EX, "Paper 1", "Paper 1 multiple-choice technique: check your understanding", "relx-paper-1-multiple-choice-strategy", "Paper 1 technique", [
    Q("How many questions does the Paper 1 mock on this platform contain?", "50",
      [("25", "That is about the size of the Paper 2 practice paper."), ("100", "Paper 1 has fifty questions, not one hundred."), ("40", "The number is fifty.")],
      "Paper 1 is fifty multiple-choice questions.", "A round number between 40 and 60.", skill="Recall"),
    Q("A multiple-choice question has one correct option and three:", "Distractors",
      [("Commands", "A command word is in the stem of an essay question."), ("Hadith", "A hadith is a report of the Prophet."), ("Parables", "A parable is a story of Jesus.")],
      "The wrong options are called distractors.", "They look attractive but are wrong.", skill="Concept"),
    Q("What should you do first when reading a question with the word NOT in it?", "Underline NOT and look for the one option that does not fit",
      [("Choose the first name you recognise", "That is probably one that does fit."), ("Skip all such questions", "Never leave a blank."), ("Ignore the word NOT", "Ignoring NOT reverses the meaning.")],
      "NOT reverses the question.", "Find the key word.", skill="Application"),
    Q("A candidate meets a sequence question: which came first, Pentecost or the stoning of Stephen? What is the best method?", "Place the events on a quick timeline in your head or on paper",
      [("Choose the more important event", "Importance is not order."), ("Choose the longer option", "Length is not a guide."), ("Leave it for ever", "Sequences are among the easiest marks.")],
      "Pentecost came first, then Stephen's death.", "Draw a line.", skill="Application"),
    Q("Which revision method best prepares you for 'who' and 'where' questions?", "Writing lists of people and places with one fact for each",
      [("Reading the notes once the night before", "Lists and testing work better than one reading."), ("Memorising only the dates", "Names and places matter just as much."), ("Learning only one module", "Paper 1 may draw on the whole syllabus.")],
      "Active recall helps names stick.", "Lists.", skill="Application"),
    Q("You can eliminate two options in a question but are unsure about the other two. What should you do?", "Choose the better of the two remaining options and move on",
      [("Leave it blank", "A blank cannot gain a mark."), ("Choose the longer option automatically", "Length is not a reliable guide."), ("Change all your other answers", "There is no reason to.")],
      "A reasoned choice from two options gives a good chance.", "Do not leave a blank.", skill="Reasoning"),
    Q("A question says: 'Who led the Jewish council at the trial of Jesus?' The options are Pilate, Caiaphas, Herod and Barabbas. Which approach is best?", "Think of the answer first, then match it to the options",
      [("Read the options first and pick the most familiar name", "All four names are familiar, which is why they are distractors."), ("Pick Pilate because he was in charge", "Pilate was the Roman governor, not the leader of the council."), ("Pick Barabbas because he was involved", "Barabbas was a prisoner.")],
      "The high priest led the council: Caiaphas.", "Who is the high priest?", skill="Application"),
    Q("What is the most sensible use of time in a 50-question paper?", "Answer the questions you know first, mark the hard ones, and return to them",
      [("Spend ten minutes on the first hard question", "This wastes time that could earn marks elsewhere."), ("Answer only the first half", "Every question carries a mark."), ("Stop when you feel tired", "Check every question has an answer.")],
      "Under two minutes a question on average in our practice setting.", "Do not get stuck.", skill="Reasoning"),
])

# ---------------------------------------------------------------------------------------------
# 17. Paper 2 strategy
# ---------------------------------------------------------------------------------------------
SET17 = ps(M_EX, "Paper 2", "Paper 2 planning and writing: check your understanding", "relx-paper-2-essay-planning", "Paper 2 planning", [
    Q("In a Paper 2 question what does the command word 'describe' ask for?", "Tell what happened or what believers do, in order, with names and details",
      [("Give your personal opinion", "Opinions are not asked."), ("Write one word", "A word is too short for describe."), ("Compare two religions", "Not asked and could rank faiths.")],
      "Describe means tell what happened.", "Think of telling a story.", skill="Concept"),
    Q("What does 'explain the importance of' ask for?", "Give reasons and show why it matters to believers",
      [("List names only", "That is for 'name' or 'state'."), ("Describe in a diary form", "Explain is about meaning."), ("Give a date", "Not required.")],
      "Importance means meaning and effects.", "Why does it matter?", skill="Concept"),
    Q("Before writing a Paper 2 answer, what should you do?", "Underline the command word and plan four to six points in order",
      [("Begin writing at once", "A plan saves time and keeps you on the question."), ("Write the conclusion first", "Plan the points first."), ("Copy the question", "This wastes time.")],
      "A short plan gives your answer a shape.", "Plan first.", skill="Application"),
    Q("Which phrase is most suitable when writing about Islamic belief?", "Muslims believe that...",
      [("Everyone knows that...", "It is not respectful or exact."), ("I think the Quran is...", "Opinions are not asked."), ("The truth is that...", "Describe what believers hold.")],
      "Use 'Muslims believe' and 'Christians believe'.", "Describe the belief.", skill="Application"),
    Q("How should the name of the Prophet Muhammad be written in an answer?", "With 'peace be upon him' or PBUH after it",
      [("Without any addition", "It is respectful to add the phrase."), ("In capital letters only", "Capital letters are not the practice."), ("With a nickname", "Use a respectful form.")],
      "The phrase is a sign of respect.", "Think of respect.", skill="Application"),
    Q("A candidate has studied only the Gospels and Islam. What should they do in Paper 2?", "Answer questions from the sections they have studied",
      [("Answer on the Old Testament as well", "Answer only on the sections studied."), ("Leave the paper blank", "They may answer the sections they studied."), ("Write about all religions in general", "The question sets the section.")],
      "Candidates answer the sections they have studied; check the format with the teacher.", "Which sections?", skill="Reasoning"),
    Q("Which plan best answers: 'Describe the conversion of Saul'?", "Persecution after Stephen's death, the road to Damascus, the light and voice, blindness, Ananias and baptism",
      [("The three journeys of Paul", "That is a different topic."), ("The Council of Jerusalem and its letter", "This is a later event."), ("The shipwreck at Malta", "This is a later event.")],
      "The plan follows the order of the story.", "Order of events.", skill="Application"),
    Q("What should you do when you are unsure of a detail in an essay?", "Leave it out or write only what you are certain of",
      [("Invent a detail that sounds right", "Wrong details lose credibility."), ("Write several different guesses", "This confuses the answer."), ("Stop writing", "Write what you know.")],
      "Accuracy matters more than length.", "Be accurate.", skill="Reasoning"),
])
# ---------------------------------------------------------------------------------------------
# Mock exams. concept = exact topic title of the outline.
# ---------------------------------------------------------------------------------------------
T = {
    "cre": "Creation accounts and the Fall", "noah": "Noah and the Flood", "abr": "The Abrahamic covenant",
    "jj": "Jacob and Joseph", "mos": "Moses, the Passover and the Exodus", "sin": "The Sinai covenant",
    "sam": "Samuel and Saul", "dav": "David", "sol": "Solomon", "div": "The divided kingdom",
    "eli": "Elijah and Ahab", "p8": "The eighth-century prophets",
    "ann": "The Annunciation and the birth of John and Jesus", "bap": "The Baptism and the Temptation",
    "twe": "The Twelve and the Sermon on the Mount", "mir": "Miracles of Jesus", "par": "Parables of the Kingdom",
    "con": "Peter's confession and the Transfiguration", "ent": "The Triumphal Entry and the Temple",
    "sup": "The Last Supper and Gethsemane", "tri": "The trials and the crucifixion", "res": "The burial and the Resurrection",
    "asc": "The Ascension and Pentecost", "life": "Life in the early church", "ste": "Stephen and the conversion of Saul",
    "pet": "Peter's ministry and the Council of Jerusalem", "pau": "Paul's missionary journeys and the voyage to Rome",
    "pre": "Pre-Islamic Arabia", "mu": "The life and prophethood of Muhammad", "qur": "The Quran",
    "had": "Hadith", "pil": "The Five Pillars of Islam",
}


def Qm(t, prompt, correct, wrongs, step, hint, skill="Recall"):
    return Q(prompt, correct, wrongs, step, hint, concept=T[t], skill=skill)


P1_QUESTIONS = [
    # --- Old Testament I (9)
    Qm("cre", "In the Bible's first creation account, what did God do on the seventh day?", "He rested and blessed the day",
       [("He created human beings", "Human beings were created on the sixth day."), ("He created the sun and moon", "The sun and moon were made on the fourth day."), ("He sent the flood", "The flood belongs to the story of Noah.")],
       "God rested on the seventh day and blessed it; Christians and Jews remember this in the Sabbath.", "Think of the word Sabbath."),
    Qm("cre", "Who, in the Genesis story of the Fall, was tempted to eat the fruit of the tree of the knowledge of good and evil, and by whom?", "Eve, by the serpent",
       [("Adam, by Cain", "Cain is the son of Adam and Eve and was not in the garden."), ("Eve, by Abel", "Abel was her son."), ("Noah, by the serpent", "Noah comes much later.")],
       "The serpent tempted Eve and she and Adam ate; they were sent out of the garden of Eden.", "Which creature spoke to Eve?"),
    Qm("noah", "What did God give as the sign of his promise never again to destroy the earth by flood?", "A rainbow",
       [("The ark", "The ark saved Noah's family; it was not the sign."), ("A burning bush", "That is in the story of Moses."), ("The stars", "The stars are in the promise to Abraham.")],
       "The rainbow in the clouds was the sign of the covenant with Noah.", "Look for a sign in the sky after the rain."),
    Qm("abr", "What did God promise Abraham?", "Land and many descendants, and that all nations would be blessed through him",
       [("A kingdom with a Temple built by his sons", "The Temple belongs to Solomon's time."), ("A place in the Egyptian court", "That is Joseph's story."), ("An end to all famine", "No such promise is made.")],
       "God promised the land of Canaan, many descendants and blessing.", "Land, people and blessing."),
    Qm("abr", "Which sign of the covenant was given to Abraham and his descendants?", "Circumcision",
       [("The rainbow", "That is the sign for Noah."), ("The Sabbath", "That is linked to creation and Sinai."), ("The Passover lamb", "That belongs to the Exodus.")],
       "Circumcision was the sign of the covenant with Abraham.", "A bodily sign.", skill="Recall"),
    Qm("jj", "How did Joseph come to be in Egypt?", "His brothers sold him to traders who took him there",
       [("He was sent as an ambassador by Jacob", "His brothers sold him."), ("He fled from Pharaoh", "He had not yet met Pharaoh."), ("He followed Moses out of Canaan", "Moses came much later.")],
       "Joseph's brothers were jealous and sold him to traders going to Egypt.", "Think of the jealous brothers."),
    Qm("jj", "How did Joseph rise to a high position in Egypt?", "He interpreted Pharaoh's dreams and was made governor, second to Pharaoh",
       [("He led the Egyptian army", "He rose by interpreting dreams."), ("He built the pyramids", "No such story is told."), ("He was adopted by Pharaoh's daughter", "That was Moses.")],
       "He advised Pharaoh to store grain against a coming famine.", "Dreams of cows and ears of grain."),
    Qm("mos", "What was done with the blood of the lamb at the first Passover?", "It was put on the doorposts of the Israelites' houses",
       [("It was poured into the Nile", "The Nile turned to blood in the first plague, not at the Passover."), ("It was sprinkled on Pharaoh's palace", "It marked the Israelites' houses."), ("It was drunk by the priests", "Not part of the story.")],
       "The blood on the doorposts marked the houses that the destroyer would pass over.", "Think of doors."),
    Qm("sin", "Where did Moses receive the Ten Commandments?", "On Mount Sinai",
       [("On Mount Carmel", "Carmel is Elijah's mountain."), ("On the Mount of Olives", "That is in the Gospels."), ("On Mount Hira", "Hira is the cave of the Prophet Muhammad.")],
       "The covenant at Sinai includes the Ten Commandments.", "A mountain in the desert.", skill="Recall"),
    # --- Old Testament II (9)
    Qm("sam", "Who anointed Saul as the first king of Israel?", "Samuel",
       [("Nathan", "Nathan rebuked David."), ("Elijah", "Elijah lived later."), ("Eli", "Eli was the priest whom Samuel served as a boy.")],
       "Samuel anointed Saul at God's direction.", "The last of the judges."),
    Qm("sam", "Why did Samuel say Saul would lose the kingdom?", "Saul disobeyed God's command",
       [("He lost a battle with Egypt", "The failure was disobedience."), ("He built a Temple", "Solomon built the Temple."), ("He refused to be king", "He accepted the kingship at first.")],
       "Saul disobeyed and the kingdom was to pass to another.", "Think of obedience."),
    Qm("dav", "Whom did David defeat with a sling and a stone?", "Goliath the Philistine",
       [("Pharaoh", "Pharaoh belongs to Egypt."), ("Ahab", "Ahab was a later king."), ("Jeroboam", "Jeroboam was a later king.")],
       "David was a young shepherd when he faced Goliath.", "The giant of Gath."),
    Qm("dav", "Which city did David make his capital?", "Jerusalem",
       [("Bethlehem", "He was born in Bethlehem."), ("Samaria", "Samaria was a later capital of the north."), ("Shiloh", "Shiloh was an earlier shrine.")],
       "David captured Jerusalem and brought the ark there.", "Later the site of the Temple.", skill="Recall"),
    Qm("sol", "What did Solomon ask of God at the start of his reign?", "Wisdom to govern the people",
       [("Long life and wealth", "God gave wealth because he did not ask for it."), ("Victory over Egypt", "He did not ask for victory."), ("A new law", "He asked for wisdom.")],
       "He asked for an understanding mind.", "The wise king."),
    Qm("sol", "What was Solomon's greatest building achievement?", "The Temple in Jerusalem",
       [("The walls of Jericho", "Jericho's walls fell in Joshua's time."), ("The ark of Noah", "The ark was Noah's."), ("The tabernacle", "The tabernacle was the tent from the time of Moses.")],
       "Solomon built the Temple in Jerusalem.", "A house for God.", skill="Recall"),
    Qm("div", "What happened to the kingdom after the death of Solomon?", "It divided into Israel in the north and Judah in the south",
       [("It united with Egypt", "It divided."), ("It became a Roman province", "That was centuries later."), ("It was ruled by Saul's family", "It divided under Rehoboam and Jeroboam.")],
       "Rehoboam ruled Judah and Jeroboam ruled the north.", "Two kingdoms."),
    Qm("eli", "On which mountain did Elijah challenge the prophets of Baal?", "Mount Carmel",
       [("Mount Sinai", "Sinai is Moses' mountain."), ("Mount Hermon", "Hermon is not the setting."), ("Mount Zion", "Zion is Jerusalem.")],
       "Elijah challenged the prophets of Baal on Mount Carmel in the time of King Ahab.", "A mountain by the sea.", skill="Recall"),
    Qm("p8", "Which prophet of the eighth century BC is known for calling for justice for the poor?", "Amos",
       [("Elijah", "Elijah lived before the writing prophets."), ("Noah", "Noah is not a prophet of the eighth century."), ("Samuel", "Samuel lived earlier.")],
       "Amos called for justice and spoke against the oppression of the poor.", "A shepherd from Tekoa."),
    # --- Synoptic Gospels I (8)
    Qm("ann", "Which angel announced to Mary that she would bear a son?", "Gabriel",
       [("Michael", "Michael is not the angel in the story."), ("Raphael", "Raphael is not named in the Gospels."), ("Uriel", "Uriel is not named in the Gospels.")],
       "Gabriel was sent to Mary in Nazareth.", "Luke names him."),
    Qm("ann", "Who were the parents of John the Baptist?", "Zechariah and Elizabeth",
       [("Joseph and Mary", "They were the parents of Jesus."), ("Joachim and Anna", "They are named in later tradition, not the Gospels."), ("Joseph and Elizabeth", "Joseph was the husband of Mary.")],
       "Zechariah was a priest and Elizabeth was Mary's relative.", "A priest and his wife."),
    Qm("bap", "At the baptism of Jesus, what descended like a dove?", "The Holy Spirit",
       [("An angel", "It was the Spirit."), ("A cloud", "A cloud belongs to the Transfiguration."), ("A star", "A star is in the Christmas story.")],
       "A voice said that Jesus was God's beloved Son.", "The Jordan."),
    Qm("bap", "For how long was Jesus tempted in the wilderness?", "Forty days",
       [("Seven days", "Not the number."), ("Three days", "He rose on the third day."), ("Ten days", "Ten days is the gap between the Ascension and Pentecost.")],
       "He fasted forty days and was tempted by the devil.", "Think of the number in the story of Moses and Elijah."),
    Qm("twe", "Which of these was a fisherman called by Jesus beside the Sea of Galilee?", "Peter",
       [("Matthew the tax collector", "Matthew was a tax collector."), ("Judas Iscariot", "Judas was not called at the lake."), ("Nathanael", "Nathanael is named in John.")],
       "Peter, Andrew, James and John were fishermen.", "The first of the Twelve to confess Jesus."),
    Qm("twe", "Which of these is part of the Sermon on the Mount in Matthew?", "The Beatitudes",
       [("The Parable of the Sower", "That is a parable."), ("The Last Supper", "That is later."), ("The Great Commission", "That is at the end of the Gospel.")],
       "The Beatitudes begin 'Blessed are the poor in spirit'.", "Blessed are..."),
    Qm("mir", "Which miracle shows Jesus' power over nature?", "Calming the storm on the lake",
       [("Healing the paralysed man", "That is a healing."), ("Raising Jairus' daughter", "That is a raising."), ("Healing the leper", "That is a healing.")],
       "The wind and the waves obeyed him.", "A boat and the Sea of Galilee."),
    Qm("par", "Which parable speaks of seed falling on different kinds of soil?", "The Sower",
       [("The Good Samaritan", "That is about neighbourly love."), ("The Prodigal Son", "That is about a father and two sons."), ("The Talents", "That is about money and trust.")],
       "The seed is the word of the kingdom and the soils are the hearers.", "Think of farmers."),
    # --- Synoptic Gospels II (8)
    Qm("con", "What did Peter say when Jesus asked who he was?", "You are the Messiah",
       [("You are a prophet", "That was a view of the crowd."), ("You are John the Baptist", "That was a view of the crowd."), ("You are only a teacher", "Peter said more than this.")],
       "Peter confessed Jesus as Messiah near Caesarea Philippi.", "The anointed one."),
    Qm("con", "Which two figures appeared with Jesus at the Transfiguration?", "Moses and Elijah",
       [("Abraham and David", "They did not appear."), ("Isaiah and Jeremiah", "They did not appear."), ("John the Baptist and Moses", "John was not there.")],
       "They stand for the Law and the prophets.", "Law and prophets."),
    Qm("ent", "What did the crowd put on the road for Jesus to ride on?", "Their cloaks and branches",
       [("Palm tree trunks", "They used branches and cloaks."), ("Gold and silver", "Not mentioned."), ("Red carpets", "Not mentioned.")],
       "They shouted Hosanna.", "Cloaks."),
    Qm("ent", "Whose tables did Jesus overturn in the Temple?", "The money changers",
       [("The scribes", "He did not overturn their tables."), ("The Roman soldiers", "No Roman soldiers were involved."), ("The Pharisees", "It was the money changers and dove sellers.")],
       "He drove out those buying and selling.", "Money."),
    Qm("sup", "Which festival was being celebrated at the Last Supper?", "Passover",
       [("Pentecost", "Pentecost was fifty days later."), ("Tabernacles", "The Gospels point to Passover."), ("Hanukkah", "Not in the Synoptic story.")],
       "Jesus ate the Passover meal with the Twelve.", "Escape from Egypt."),
    Qm("sup", "Which disciple betrayed Jesus with a kiss?", "Judas Iscariot",
       [("Peter", "Peter denied Jesus."), ("John", "John stayed close."), ("Andrew", "Andrew did not betray him.")],
       "He led the crowd to Gethsemane.", "One of the Twelve."),
    Qm("tri", "Who was released instead of Jesus?", "Barabbas",
       [("Simon of Cyrene", "He carried the cross."), ("Caiaphas", "He was the high priest."), ("Herod", "He was a ruler.")],
       "The crowd asked for Barabbas.", "A prisoner."),
    Qm("res", "Who asked Pilate for the body of Jesus?", "Joseph of Arimathea",
       [("Simon of Cyrene", "He carried the cross."), ("Peter", "Peter was in hiding."), ("Nicodemus alone", "The Synoptic Gospels name Joseph.")],
       "He put the body in a new rock tomb.", "A member of the council."),
    # --- Acts (8)
    Qm("asc", "How many days after Passover was Pentecost?", "Fifty",
       [("Forty", "Forty is the time between Easter and the Ascension."), ("Ten", "Ten days is the time from Ascension to Pentecost."), ("Seven", "Seven is a week.")],
       "Pentecost means fiftieth.", "Pente."),
    Qm("asc", "Who replaced Judas among the apostles?", "Matthias",
       [("Barnabas", "Not chosen."), ("Stephen", "One of the Seven."), ("Philip", "One of the Seven.")],
       "The lot fell on Matthias.", "Casting lots."),
    Qm("life", "Who sold a field and laid the money at the apostles' feet?", "Barnabas",
       [("Ananias", "Ananias kept some back."), ("Stephen", "Stephen was one of the Seven."), ("Philip", "Philip was one of the Seven.")],
       "Barnabas means son of encouragement.", "Joseph from Cyprus."),
    Qm("life", "Why were Ananias and Sapphira punished?", "They lied about the price of the land",
       [("They stole from the Temple", "They kept their own money."), ("They refused to share anything", "Sharing was voluntary."), ("They denied Jesus", "They lied about their gift.")],
       "The sin was lying to the Holy Spirit.", "Peter's question."),
    Qm("ste", "Who held the coats of those who stoned Stephen?", "Saul",
       [("Barnabas", "Barnabas was a friend of the apostles."), ("Philip", "Philip was one of the Seven."), ("Peter", "Peter was with the apostles.")],
       "Saul approved of Stephen's death.", "The future apostle to the Gentiles."),
    Qm("ste", "Who laid hands on Saul in Damascus so that he regained his sight?", "Ananias",
       [("Barnabas", "Barnabas introduced him in Jerusalem."), ("Silas", "Silas travelled with him later."), ("Peter", "Peter was elsewhere.")],
       "He called him Brother Saul.", "A disciple in Damascus."),
    Qm("pet", "What did the Council of Jerusalem decide about Gentile believers?", "They need not be circumcised",
       [("They must keep the whole law of Moses", "That was the view of some Pharisees."), ("They must leave the church", "No."), ("They must be baptised twice", "No.")],
       "A letter went to Antioch.", "James gave the verdict."),
    Qm("pau", "Which companion travelled with Paul on his second journey?", "Silas",
       [("Barnabas", "He went with Paul on the first journey."), ("Cornelius", "Cornelius was a centurion in Caesarea."), ("Matthias", "Matthias replaced Judas.")],
       "Paul and Silas were jailed at Philippi.", "After Paul and Barnabas disagreed."),
    # --- Islamic Religious Studies (8)
    Qm("pre", "Which tribe controlled Mecca at the Prophet's birth?", "The Quraysh",
       [("The Aws", "A tribe of Yathrib."), ("The Khazraj", "A tribe of Yathrib."), ("The Ghassan", "A kingdom near Syria.")],
       "The Prophet belonged to the Quraysh.", "Guardians of the Kaaba."),
    Qm("pre", "What does Jahiliyyah mean?", "The period before Islam, the time of ignorance",
       [("The Muslim calendar", "That is the Hijri calendar."), ("The month of fasting", "That is Ramadan."), ("The pilgrimage", "That is the Hajj.")],
       "It refers to Arabia before the revelation.", "Before Islam."),
    Qm("mu", "In which cave did the Prophet receive the first revelation?", "Hira",
       [("Thawr", "He hid in a cave on the Hijra; it was not the first revelation."), ("Uhud", "Uhud is a mountain and a battle."), ("Sinai", "Sinai belongs to Moses.")],
       "Jibril said, Read.", "Near Mecca."),
    Qm("mu", "What was the Hijra?", "The migration from Mecca to Medina in 622 CE",
       [("The return to Mecca", "That came later."), ("The first pilgrimage", "That is the Hajj."), ("The conquest of Persia", "No.")],
       "It started the Muslim calendar.", "Migration."),
    Qm("qur", "Who ordered that standard copies of the Quran be sent to the main cities?", "Uthman",
       [("Abu Bakr", "He had the Quran collected."), ("Umar", "He advised collecting."), ("Ali", "He was the fourth caliph.")],
       "The third caliph standardised the text.", "Third caliph."),
    Qm("had", "What is the chain of narrators of a hadith called?", "The isnad",
       [("The matn", "The matn is the text."), ("The sunnah", "The sunnah is the example."), ("The surah", "A surah is a chapter.")],
       "Each narrator names the previous one.", "Chain."),
    Qm("pil", "About what share of qualifying savings is paid as zakat?", "2.5 per cent",
       [("1 per cent", "Too low."), ("10 per cent", "Too high."), ("20 per cent", "Far too high.")],
       "One-fortieth after a year above the nisab.", "One-fortieth."),
    Qm("pil", "In which month do Muslims fast from dawn to sunset?", "Ramadan",
       [("Dhul-Hijjah", "The month of the Hajj."), ("Muharram", "The first month."), ("Rajab", "Not the month of fasting.")],
       "Ramadan is the ninth month.", "The month of the Quran."),
]

NOTE = " (KKEVO practice paper. In the real Paper 2 candidates answer the sections they have studied; here, if you have not studied a section, you may skip its parts.)"

P2_QUESTIONS = [
    # --- Sequence of events
    Qm("tri", "Part A1. Put these in order: (i) Peter's denial, (ii) the trial before Pilate, (iii) the arrest at Gethsemane, (iv) the crucifixion." + NOTE,
       "iii, i, ii, iv",
       [("i, iii, ii, iv", "The arrest came before the denial."), ("iii, ii, i, iv", "Peter denied Jesus while the council questioned him, before the trial before Pilate."), ("ii, iii, i, iv", "Pilate's trial came after the arrest.")],
       "Arrest, denial in the courtyard, Pilate, cross.", "Start with the garden.", skill="Reasoning"),
    Qm("sup", "Part A2. Which order is correct in the last week of Jesus?", "Triumphal Entry, cleansing of the Temple, Last Supper, Gethsemane",
       [("Last Supper, Triumphal Entry, Gethsemane, cleansing of the Temple", "The entry came first."), ("Triumphal Entry, Last Supper, cleansing of the Temple, Gethsemane", "The cleansing came before the Last Supper."), ("Cleansing of the Temple, Triumphal Entry, Gethsemane, Last Supper", "The entry came before the cleansing, and the Supper before Gethsemane.")],
       "Entry, Temple, teaching, Supper, Gethsemane.", "Start with the colt.", skill="Reasoning"),
    Qm("res", "Part A3. Which is the correct order?", "Burial by Joseph of Arimathea, the Sabbath, the women at the empty tomb, the commission to the disciples",
       [("The women at the empty tomb, burial, the Sabbath, the commission", "The burial came first."), ("The commission, burial, the Sabbath, the women at the tomb", "The commission came after the Resurrection."), ("The Sabbath, burial, the commission, the women at the tomb", "The burial was before the Sabbath.")],
       "Burial on Friday, Sabbath, empty tomb on the first day, then the appearances.", "Friday first.", skill="Reasoning"),
    Qm("asc", "Part A4. Which is the correct order?", "Ascension, choice of Matthias, Pentecost, Peter's sermon",
       [("Pentecost, Ascension, choice of Matthias, Peter's sermon", "Pentecost came after the Ascension."), ("Ascension, Pentecost, choice of Matthias, Peter's sermon", "Matthias was chosen before Pentecost."), ("Choice of Matthias, Ascension, Pentecost, Peter's sermon", "The Ascension came first.")],
       "Ascension, upper room, Matthias, Pentecost, sermon.", "Jesus is taken up first.", skill="Reasoning"),
    Qm("pau", "Part A5. Which is the correct order of Paul's travels?", "First journey with Barnabas, second journey with Silas, third journey with Ephesus, voyage to Rome",
       [("Second journey, first journey, third journey, voyage to Rome", "The first journey was with Barnabas and came first."), ("First journey, third journey, second journey, voyage to Rome", "The second journey comes before the third."), ("Voyage to Rome, first journey, second journey, third journey", "The voyage came last.")],
       "Barnabas, then Silas, then Ephesus, then Rome.", "Companions.", skill="Reasoning"),
    Qm("mu", "Part A6. Which is the correct order in the life of the Prophet?", "First revelation at Hira, Hijra to Medina, return to Mecca, death in Medina",
       [("Hijra, first revelation, return to Mecca, death", "The first revelation came before the Hijra."), ("First revelation, return to Mecca, Hijra, death", "The return came after the Hijra."), ("Return to Mecca, Hijra, first revelation, death", "The return came much later.")],
       "Revelation, opposition, Hijra, return, death.", "Start in the cave.", skill="Reasoning"),
    # --- Characters
    Qm("con", "Part B1. Which three disciples were with Jesus at the Transfiguration?", "Peter, James and John",
       [("Peter, Andrew and Philip", "Not these."), ("Peter, Judas and Thomas", "Not these."), ("James, Matthew and John", "Matthew was not there.")],
       "The three who were closest.", "Sons of Zebedee and Peter.", skill="Recall"),
    Qm("tri", "Part B2. Who is matched to the correct role?", "Caiaphas: high priest; Pilate: Roman governor",
       [("Caiaphas: Roman governor; Pilate: high priest", "The roles are reversed."), ("Barabbas: high priest; Caiaphas: prisoner", "Barabbas was the prisoner."), ("Herod: high priest; Pilate: prisoner", "Herod was ruler of Galilee.")],
       "Caiaphas led the council; Pilate governed Judea.", "Jewish and Roman roles.", skill="Recall"),
    Qm("ste", "Part B3. Which statement about Ananias is correct?", "Ananias of Damascus laid hands on Saul; the husband of Sapphira was another man of the same name",
       [("The same Ananias lied to Peter and healed Saul", "They were two different men."), ("Ananias was one of the Twelve", "He was not."), ("Ananias introduced Saul to the apostles", "That was Barnabas.")],
       "Two different men had the same name.", "Different Ananias.", skill="Reasoning"),
    Qm("pet", "Part B4. Who is matched correctly?", "Cornelius: a Roman centurion in Caesarea; Tabitha: a disciple at Joppa",
       [("Cornelius: a disciple at Joppa; Tabitha: a centurion", "The roles are reversed."), ("Cornelius: leader of the council; Tabitha: Herod's servant", "Not correct."), ("Cornelius: a Pharisee; Tabitha: a priest", "Not correct.")],
       "Cornelius was a Gentile centurion; Tabitha was a disciple known for good works.", "Gentile and woman disciple.", skill="Recall"),
    Qm("life", "Part B5. Which two were among the seven chosen to serve the widows?", "Stephen and Philip",
       [("Peter and John", "They were apostles."), ("Barnabas and Saul", "They went on the first journey."), ("Matthias and Barsabbas", "They were candidates for Judas' place.")],
       "The Seven were chosen so that the apostles could preach.", "One was stoned.", skill="Recall"),
    Qm("had", "Part B6. Which compiler is matched correctly to his collection?", "Muslim ibn al-Hajjaj: Sahih Muslim",
       [("Muslim ibn al-Hajjaj: Sahih al-Bukhari", "He did not compile that."), ("Zayd ibn Thabit: Sahih Muslim", "He was a scribe of the Quran."), ("Uthman: Sahih al-Bukhari", "Uthman was a caliph.")],
       "Each collection bears its compiler's name.", "Name in the title.", skill="Recall"),
    # --- Significance
    Qm("con", "Part C1. Why is the Transfiguration important for Christians?", "It confirms Jesus as God's Son and prepares the disciples for his suffering",
       [("It shows that Moses and Elijah were greater than Jesus", "The voice told them to listen to Jesus."), ("It proves that Jesus would not die", "It came with talk of his departure."), ("It was the day the church began", "That was Pentecost.")],
       "Glory and suffering belong together.", "Link to the confession.", skill="Application"),
    Qm("sup", "Part C2. Why does the Last Supper matter to Christians today?", "It is the origin of Holy Communion, which remembers Jesus' death and the new covenant",
       [("It is the origin of baptism", "Baptism is linked with John and Jesus."), ("It created the Sabbath", "The Sabbath is linked with creation."), ("It ended the Passover", "The Passover meal continued.")],
       "Bread and cup are shared in worship.", "A meal in memory.", skill="Application"),
    Qm("res", "Part C3. What is the main meaning of the Resurrection for Christians?", "God has power over death and confirms Jesus' message, and gives hope of life after death",
       [("The Temple was rebuilt", "Not the meaning."), ("The Romans were defeated", "Not the meaning."), ("The Sabbath was abolished", "Not the meaning.")],
       "The Resurrection is the central Christian belief.", "Life after death.", skill="Application"),
    Qm("asc", "Part C4. Why is Pentecost called the birthday of the church?", "The Spirit came, Peter preached and thousands joined the believers",
       [("Jesus was born that day", "That is Christmas."), ("The Temple was dedicated", "No."), ("Paul became an apostle", "That was later.")],
       "The church began to grow.", "Spirit and sermon.", skill="Application"),
    Qm("pet", "Part C5. Why was the Council of Jerusalem important?", "It decided that Gentile believers need not become Jews, so the church could be one for all nations",
       [("It chose the twelve apostles", "Jesus chose them."), ("It sent Paul to Rome", "It did not."), ("It rebuilt the Temple", "It did not.")],
       "A letter went to the Gentile churches.", "Circumcision.", skill="Application"),
    Qm("pil", "Part C6. Why do pilgrims wear simple white clothes in ihram?", "To show that all believers are equal before God",
       [("To show their rank", "It does the opposite."), ("To protect them from the sun", "It is a sign of purity and equality."), ("To mark the end of Ramadan", "It is for the Hajj.")],
       "Rich and poor dress alike.", "Equality.", skill="Application"),
    # --- Essay planning
    Qm("sup", "Part D1. A question asks: 'Describe the arrest of Jesus.' Which plan is best?", "Gethsemane prayer, sleeping disciples, Judas and the crowd, the kiss, the sword, the disciples flee",
       [("The trial before Pilate, Barabbas, the cross", "These are later events."), ("The Beatitudes and the parables", "These are other teachings."), ("The Pentecost sermon", "That is in Acts.")],
       "Follow the order of the story.", "Start in the garden.", skill="Application"),
    Qm("ste", "Part D2. Which plan best answers 'Describe the conversion of Saul'?", "Persecution of the church, the road to Damascus, the light and voice, blindness, Ananias, baptism",
       [("The Council of Jerusalem and its letter", "This is another topic."), ("The shipwreck at Malta", "This is a later event."), ("The Passover and the Exodus", "This is an Old Testament topic.")],
       "Keep to the order of events.", "Persecutor first.", skill="Application"),
    Qm("pau", "Part D3. A question asks you to describe one of Paul's journeys. Which advice is best?", "Choose the journey you know best and give companions, places and key events in order",
       [("Mix all three journeys in one paragraph", "This causes confusion."), ("Give only the dates", "Dates differ and are not the point."), ("Leave out all names", "Names and places earn marks.")],
       "Accuracy and order.", "Choose a journey.", skill="Reasoning"),
    Qm("qur", "Part D4. A question asks: 'Explain how the Quran was preserved.' Which plan is best?", "Memorisation, writing by scribes, collection under Abu Bakr, standard copies under Uthman",
       [("Hijra, Badr, return to Mecca", "This is the life of the Prophet."), ("Zakat, sawm, hajj", "These are pillars."), ("Isnad and matn", "These are parts of a hadith.")],
       "Follow the order of preservation.", "From memory to copies.", skill="Application"),
    Qm("pil", "Part D5. Which plan best answers 'Explain the importance of the Five Pillars to Muslims'?", "Name each pillar, give one practice and one meaning, then conclude about unity and worship",
       [("Retell the life of the Prophet", "This is another question."), ("Describe the cleansing of the Temple", "This is a Christian topic."), ("List dates for the Hijra", "Not asked.")],
       "Each pillar needs practice and meaning.", "Five parts.", skill="Application"),
    Qm("mu", "Part D6. Which opening sentence is most suitable for an answer on the Prophet's life?", "Muslims believe that Muhammad, peace be upon him, was born in Mecca and received the Quran as God's final message.",
       [("Muhammad was just a trader from Mecca.", "This is not respectful and ignores belief."), ("I think Islam is better than other religions.", "No ranking of religions."), ("Everybody knows about Muhammad.", "This gives no content.")],
       "Use 'Muslims believe' and the respectful phrase.", "Respect and accuracy.", skill="Application"),
    Qm("ent", "Part D7. A question asks: 'Why did Jesus cleanse the Temple?' Which answer plan is best?", "Describe what he did, quote his words about prayer, give reasons and state the result",
       [("List the twelve disciples", "Not asked."), ("Describe the birth of Jesus", "Not asked."), ("Write about the Council of Jerusalem", "Not asked.")],
       "Describe and then explain.", "Think of describe plus explain.", skill="Application"),
]


SETS = [
    SET1, SET2, SET3, SET4, SET5, SET6, SET7, SET8, SET9, SET10, SET11, SET12, SET13, SET14, SET15, SET16, SET17,
    mock(M_EX, "Paper 1", "Paper 1 mock exam A", "relx-paper-1-multiple-choice-strategy", 90, P1_QUESTIONS),
    mock(M_EX, "Paper 2", "Paper 2 practice paper A", "relx-paper-2-essay-planning", 150, P2_QUESTIONS),
]
