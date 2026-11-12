"""Practice sets for A Level Religious Studies (0785), Lower Sixth: New Testament: Gospel Theology (5 sets), Alternative Track: Early Church History or
Philosophy of Religion (4 sets) and Examination (Paper 1, Paper 2, Paper 3: 3 sets), one set per lesson (12 sets), plus 'Paper 1 mock exam A'
(50 four-option questions across all five Lower Sixth modules in proportion to their topic counts) and 'Paper 2 practice paper A'
(25 auto-markable parts on essay planning, key arguments and command words; essays cannot be marked automatically). Paper 3 has a lesson and set only.
Facts follow the Board's 2023 report (paraphrased) and the lessons of the same course; the Old Testament and Synoptic questions follow the Lower Sixth lessons of the
other writer (al_rsl1_pentateuch_monarchy_synoptic.py). Scholarly theories are presented as theories; the time limits of the mocks are KKEVO practice settings.
"""

import random

from .dsl import *  # noqa: F403

COURSE = ("religious-studies", "lower-sixth")

M1 = "Old Testament: Pentateuchal Criticism & Early Israel"
M2 = "Old Testament: Rise of the Monarchy & Cultic Institutions"
M3 = "New Testament: Intertestamental Period & the Synoptic Problem"
M4 = "New Testament: Gospel Theology"
M5 = "Alternative Track: Early Church History or Philosophy of Religion"
MX = "Examination"

T_DH = "The Documentary Hypothesis"
T_GEN = "Genesis 1 to 11 and the ancient Near East"
T_PAT = "The patriarchal covenants"
T_EXO = "The Exodus"
T_MOS = "The Mosaic covenant"
T_HOL = "The Holiness Code"
T_JUD = "From the judges to the monarchy"
T_SAUL = "Saul"
T_DAV = "David and the Davidic covenant"
T_SOL = "Solomon"
T_TEM = "The Temple, priesthood and festivals"
T_BG = "The Jewish and Greco-Roman background"
T_GRP = "Jewish groups and institutions"
T_ORAL = "Oral tradition and Form and Redaction criticism"
T_SYN = "The Synoptic problem"
T_CHR = "Christological titles"
T_KING = "The Kingdom of God"
T_PAR = "Parables and miracles"
T_JOHN = "The Gospel of John"
T_PASS = "The passion and resurrection narratives"
T_SPREAD = "The spread of Christianity and the persecutions"
T_APOL = "Apologists and heresies"
T_COUN = "The Councils of Nicaea and Chalcedon"
T_ARG = "Arguments for the existence of God"


def K(prompt, right, wrongs, step, concept, skill, hint, feedback=""):
    """Question spec: the right option first, then three (text, why) wrong options. Positions are assigned by build()."""
    assert len(wrongs) == 3, prompt
    assert len(concept) <= 80
    return {"prompt": prompt, "right": right, "wrongs": wrongs, "step": step, "concept": concept, "skill": skill,
            "hint": hint, "feedback": feedback}


def build(specs, seed):
    n = len(specs)
    pos = [i % 4 for i in range(n)]
    random.Random(seed).shuffle(pos)
    out = []
    for sp, p in zip(specs, pos):
        opts = [C(w, why=y) for w, y in sp["wrongs"]]
        opts.insert(p, C(sp["right"], correct=True))
        steps = [S("Reasoning", text=s) for s in ([sp["step"]] if isinstance(sp["step"], str) else sp["step"])]
        out.append(MC(sp["prompt"], opts, steps, concept=sp["concept"], skill=sp["skill"], hint=sp["hint"], feedback=sp["feedback"]))
    return out


def SET(module, topic, title, lesson, specs, seed, **kw):
    assert len(specs) == 8, title
    SETS.append(practice_set(module=module, topic=topic, title=title, lesson=lesson, questions=build(specs, seed), **kw))


SETS = []


# ================================================================== 1. Christological titles
SET(M4, T_CHR, "Christological titles: Messiah, Son of God, Son of Man and Logos", "rsl2-christological-titles", [
    K("The English word 'Christ' comes from the Greek word Christos. What does it mean?", "Anointed one (the Greek form of Messiah)", [
        ("The Word of God", "That is Logos, the title in the Prologue of John."), ("Lord", "Lord translates the Greek Kyrios."), ("Servant", "A servant is not what Christos means.")],
      "Messiah is Hebrew for 'anointed one' and Christos is its Greek translation.", T_CHR, "Recall", "Think of the oil used to mark kings."),
    K("In Mark 8, Peter answers Jesus' question 'Who do you say that I am?' with which title?", "The Christ (Messiah)", [
        ("Son of Man", "Jesus himself uses this title when he goes on to speak of suffering."), ("The Word (Logos)", "Logos is found in John's Prologue, not in Peter's confession."), ("Lord of the Sabbath", "This is a saying of Jesus in Mark 2, not Peter's answer.")],
      "Peter's confession at Caesarea Philippi names Jesus as the Christ.", T_CHR, "Recall", "Look at the confession scene in the middle of Mark."),
    K("Which scholar introduced the idea of the 'messianic secret' in Mark?", "William Wrede", [
        ("Rudolf Bultmann", "He is linked with form criticism and the programme of demythologising."), ("Albert Schweitzer", "He is linked with consistent (future) eschatology."), ("C. H. Dodd", "He is linked with realised eschatology.")],
      "Wrede (1901) argued that Mark's silencing of demons and others explained why Jesus was not recognised as Messiah in his lifetime.", T_CHR, "Recall", "He wrote at the beginning of the twentieth century."),
    K("Who uses the title 'Son of Man' in the Gospels?", "Almost always Jesus, speaking about himself", [
        ("The disciples, about Jesus", "The Gospels do not show the disciples using it as a title."), ("The Roman centurion at the cross", "He is said to speak of the 'Son of God', not the Son of Man."), ("John the Baptist, in his preaching", "The Gospels do not present the Baptist using this title.")],
      "The phrase is found on the lips of Jesus, with very few exceptions.", T_CHR, "Concept", "Who is speaking when the phrase occurs?"),
    K("Which Old Testament passage is usually named as the background of the heavenly 'Son of Man'?", "Daniel 7:13-14", [
        ("Genesis 1:1-3", "This is a background of the Logos idea (God creating by his word)."), ("Psalm 2", "This is a royal psalm which calls the king God's son."), ("Exodus 3", "This is the story of the burning bush and the divine name.")],
      "In Daniel 7 a figure 'like a son of man' comes with the clouds and receives rule.", T_CHR, "Recall", "Think of the visions of the book of Daniel."),
    K("Which title does the Prologue of John use of Jesus but the Synoptic Gospels do not?", "Logos (the Word)", [
        ("Son of Man", "This appears in all four Gospels."), ("Messiah", "This appears in the Synoptic Gospels (for example Mark 8:29)."), ("Son of God", "This appears in the Synoptic Gospels (for example Mark 15:39).")],
      "Logos is used in John 1:1-18, and not as a title of Jesus in the Synoptics.", T_CHR, "Concept", "Which title is a Greek word meaning word or reason?"),
    K("Who says 'Truly this man was the Son of God' in Mark 15:39?", "The Roman centurion at the cross", [
        ("Peter at Caesarea Philippi", "Peter's confession uses the title Christ."), ("The high priest at the trial", "He asks whether Jesus is the Christ, the Son of the Blessed."), ("The voice at the baptism", "The voice uses the title, but it is the centurion who says it at the cross.")],
      "The centurion's words at the death of Jesus are the climax of Mark's use of the title.", T_CHR, "Recall", "Think of the person who saw how Jesus died."),
    K("Which statement best summarises scholarly work on the Son of Man sayings?", "Scholars usually sort them into present, suffering and future sayings and debate which go back to Jesus", [
        ("All scholars agree that Jesus never used the phrase", "Many scholars think he did use it; the debate is about which sayings are his."), ("All scholars agree that every saying was spoken by Jesus", "Some doubt the origin of some groups of sayings."), ("The phrase only means 'God' in Aramaic", "It can mean 'a human being' or be a way of speaking of oneself; it does not mean 'God'.")],
      "A good answer gives the three groups and the debate, without claiming that the debate is settled.", T_CHR, "Reasoning", "The question is about scholarly debate."),
], 201)

# ================================================================== 2. Kingdom of God
SET(M4, T_KING, "The Kingdom of God: meaning, timing and demands", "rsl2-kingdom-of-god", [
    K("What does the Greek word basileia (kingdom) mainly mean in the preaching of Jesus?", "The rule or reign of God", [
        ("A territory with fixed borders", "The word describes God's kingship more than a place."), ("The Temple in Jerusalem", "The Temple is a building; the Kingdom is God's rule."), ("Life in heaven after death only", "It includes a future completion but it is first God's active rule.")],
      "The Kingdom is God acting as king.", T_KING, "Recall", "Think of 'reign' as the verb 'to rule'."),
    K("Mark 1:15 joins the announcement of the Kingdom to which call?", "Repent and believe the good news", [
        ("Pay the temple tax", "That is not what Mark 1:15 says."), ("Fast for forty days", "Fasting is not the call of Mark 1:15."), ("Join the Pharisees", "The call is to repent and believe, not to join a party.")],
      "The call is to turn around and trust.", T_KING, "Recall", "Recall the summary of Jesus' preaching in Mark 1."),
    K("Which scholar is associated with 'realised eschatology', the view that the Kingdom has already come in Jesus' ministry?", "C. H. Dodd", [
        ("Albert Schweitzer", "He argued that the Kingdom was expected in the near future."), ("William Wrede", "He is known for the messianic secret."), ("Adolf Julicher", "He is known for his work on parables.")],
      "Dodd stressed the present Kingdom.", T_KING, "Recall", "He wrote 'The Parables of the Kingdom'."),
    K("A scholar says that the Kingdom has begun in the ministry of Jesus but is still to be completed. Which view is this?", "Inaugurated eschatology ('already but not yet')", [
        ("Futurist (consistent) eschatology", "This says the Kingdom is entirely in the future."), ("Realised eschatology", "This says the Kingdom has already fully come."), ("No eschatology", "The view is about the 'last things'; it is eschatology.")],
      "Inaugurated means begun but not yet complete.", T_KING, "Concept", "Which view has both a 'begun' and a 'not yet'?"),
    K("Why does Matthew usually write 'kingdom of heaven'?", "Probably from Jewish reverence in avoiding the divine name", [
        ("It is a different kingdom from the Kingdom of God", "The phrases are generally regarded as meaning the same."), ("Matthew thought that the Kingdom is only in the sky", "The phrase does not mean a place in the sky."), ("Luke used the phrase first", "Luke usually writes 'kingdom of God'.")],
      "'Heaven' is a respectful way of speaking of God.", T_KING, "Concept", "Think of the Jewish audience of Matthew."),
    K("Luke 11:20 says that if Jesus drives out demons by the finger of God, then what has happened?", "The Kingdom of God has come upon them", [
        ("The end of the age has arrived completely", "The saying speaks of the Kingdom coming upon them, not the full end of the age."), ("The Temple has been destroyed", "The saying is not about the Temple."), ("The Pharisees are right to doubt him", "Jesus' reply to his critics supports his claim.")],
      "The exorcisms are a sign of the Kingdom at work.", T_KING, "Application", "Which part of the ministry is being explained?"),
    K("Which is given in Luke 7:22 as a sign of the Kingdom, in reply to John the Baptist's question?", "The blind see, the lame walk and the poor hear good news", [
        ("The Romans are driven from Palestine", "The signs are healing and good news, not a political victory."), ("The Temple is rebuilt", "This is not in the reply."), ("The Sabbath is abolished", "The reply does not say this.")],
      "Jesus points to his works of healing.", T_KING, "Recall", "Think of Jesus' answer to the messengers from John."),
    K("Why do many scholars prefer 'among you' to 'within you' in Luke 17:21?", "Jesus speaks to Pharisees and the Kingdom is present in his own ministry", [
        ("The Greek can only mean 'among'", "The Greek allows both meanings; this is why scholars debate it."), ("'Within you' would deny that God rules", "That is not the reason given."), ("Luke never speaks of the inner life", "This is not the argument; the reason is the context of the saying.")],
      "The Greek is ambiguous, and context decides.", T_KING, "Reasoning", "Who is Jesus addressing in the verse?"),
], 202)

# ================================================================== 3. Parables and miracles
SET(M4, T_PAR, "Parables and miracles: kinds, meaning and interpretation", "rsl2-parables-and-miracles", [
    K("What is a parable?", "A short story or comparison from daily life told to make a point", [
        ("A long poem about creation", "A parable is short and makes a point; it is not a long poem."), ("A list of laws", "Laws are not parables."), ("A miracle of healing", "A miracle is a deed; a parable is a story.")],
      "The Greek parabole means a comparison placed beside something.", T_PAR, "Recall", "Think of the Sower or the Good Samaritan."),
    K("Which parable is told in answer to the question 'Who is my neighbour?'", "The Good Samaritan", [
        ("The Prodigal Son", "It is told to answer complaints about eating with sinners."), ("The Sower", "It describes the different responses to the word."), ("The Talents", "It is about use of gifts and readiness.")],
      "Luke 10:29-37 follows the lawyer's question.", T_PAR, "Recall", "Look for a Samaritan."),
    K("Which scholar insisted that each parable normally has one main point and is not an allegory?", "Adolf Julicher", [
        ("C. H. Dodd", "He linked parables to the Kingdom now at work."), ("William Wrede", "He is known for the messianic secret."), ("Rudolf Bultmann", "He is known for form criticism.")],
      "Julicher reacted against allegorical reading.", T_PAR, "Recall", "He wrote at the end of the nineteenth century."),
    K("Which word does John's Gospel normally use for a miracle?", "Semeion (sign)", [
        ("Dunamis (power)", "This is the common word in the Synoptics."), ("Parabole (parable)", "This means a parable."), ("Logos (word)", "This means word.")],
      "John selects seven 'signs'.", T_PAR, "Recall", "John teaches by signs."),
    K("The parable of the Prodigal Son is told in answer to what?", "The Pharisees' complaint that Jesus welcomes sinners and eats with them", [
        ("A question about paying taxes", "That is a different pronouncement story."), ("The disciples' request to pray", "The Lord's Prayer is given in that setting."), ("The question 'Who is my neighbour?'", "That is the Good Samaritan.")],
      "Luke 15:1-2 gives the setting.", T_PAR, "Application", "See the opening verses of Luke 15."),
    K("Which of the following is a nature miracle?", "Calming the storm", [
        ("Healing a leper", "This is a healing miracle."), ("The Gerasene man", "This is an exorcism."), ("Jairus' daughter", "This is a raising of a dead person.")],
      "Nature miracles show authority over the natural world.", T_PAR, "Concept", "Which story deals with wind and sea?"),
    K("Form critics note a common pattern in many healing stories. Which order is correct?", "Description of the problem, request, word or touch, cure, response of the crowd", [
        ("Cure, request, problem, word, crowd", "The cure cannot come before the problem is described."), ("Crowd, cure, problem, request, touch", "The crowd's response comes at the end."), ("Word, touch, problem, cure, request", "The request follows the problem and precedes the healing.")],
      "The pattern helps scholars see how the stories were told.", T_PAR, "Concept", "Think of the natural order of a healing story."),
    K("A Paper 3 question on Luke asks whether recipients of miracles believed in them as genuine. What is the best approach?", "Use specific miracles and show both faith and other responses", [
        ("Retell all the miracles in order", "A narration does not answer the question about belief."), ("Argue that miracles are impossible", "This does not use the text or answer the question."), ("Name one miracle and stop", "One example without response or explanation is too little.")],
      "The report says the question asked about belief by the recipients.", T_PAR, "Reasoning", "The command is about the response of people."),
], 203)

# ================================================================== 4. The Gospel of John
SET(M4, T_JOHN, "The Gospel of John: purpose, signs and themes", "rsl2-gospel-of-john", [
    K("What does John 20:31 say is the purpose of the Gospel?", "That readers may believe that Jesus is the Christ, the Son of God, and have life", [
        ("To list the ancestors of Jesus", "This is the work of the genealogies in Matthew and Luke."), ("To record all the parables of Jesus", "John has no parables."), ("To describe the journeys of Paul", "That is the subject of Acts.")],
      "John states his purpose near the end of chapter 20.", T_JOHN, "Recall", "Look for belief and life."),
    K("Which of these is NOT found in the Gospel of John?", "The parable of the Sower", [
        ("The conversation with Nicodemus", "This is only in John."), ("The raising of Lazarus", "This is only in John."), ("The Samaritan woman at the well", "This is only in John.")],
      "John has no parables.", T_JOHN, "Recall", "Which Gospel has no parables?"),
    K("How many miracles does John call 'signs' in his main selection?", "Seven", [
        ("Three", "This is not the usual count."), ("Twelve", "Twelve is the number of the disciples."), ("Forty", "This is not a count of the signs.")],
      "Water into wine, official's son, paralysed man, five thousand, walking on water, man born blind, Lazarus.", T_JOHN, "Recall", "Count the signs in the lesson."),
    K("Which 'I am' saying is spoken before the raising of Lazarus?", "I am the resurrection and the life", [
        ("I am the bread of life", "This follows the feeding of the five thousand."), ("I am the vine", "This is in the farewell discourse."), ("I am the door", "This is in the shepherd discourse.")],
      "John 11:25 is said to Martha.", T_JOHN, "Application", "Which saying is about death and life?"),
    K("What does John the Baptist say about himself in John 1:20?", "That he is not the Christ", [
        ("That he is the Christ", "He denies this."), ("That he is the Son of Man", "He does not say this."), ("That he is the king of Israel", "This is a title used of Jesus by Nathanael.")],
      "The Baptist's denial is the key fact in the question on Jesus' identity at the start of the ministry.", T_JOHN, "Recall", "Think of the priests' question to John."),
    K("In John 9, which theme is shown by the healing of the man born blind?", "Light of the world and spiritual blindness", [
        ("The Kingdom as a mustard seed", "That is a Synoptic parable."), ("The Temple tax", "This is not the theme of chapter 9."), ("The Last Supper meal", "This is not the theme of chapter 9.")],
      "The man comes to sight while the Pharisees stay blind.", T_JOHN, "Concept", "Think of sight and blindness."),
    K("Which is a difference between John and the Synoptic Gospels?", "In John the cleansing of the Temple comes early in the ministry", [
        ("In John it comes at the very end of the ministry", "That is the Synoptic placing."), ("John has no Temple cleansing", "John 2 describes it."), ("Only Luke has it", "All four Gospels have the story.")],
      "John 2 has the cleansing near the start.", T_JOHN, "Concept", "Compare the order of events."),
    K("Which statement about the authorship of John is the fairest?", "Tradition names John son of Zebedee, and many scholars suggest a Johannine community behind the Gospel", [
        ("All scholars agree that John son of Zebedee wrote it", "Scholars disagree."), ("The Gospel names Luke as its author", "Luke is the author of the third Gospel."), ("No one has ever proposed an author", "Tradition and scholars have proposed several.")],
      "A good answer presents both views.", T_JOHN, "Reasoning", "The debate has two sides."),
], 204)


# ================================================================== 5. Passion and resurrection
SET(M4, T_PASS, "The passion and resurrection narratives: emphases and questions", "rsl2-passion-and-resurrection", [
    K("Who was the Roman governor before whom Jesus was tried?", "Pontius Pilate", [
        ("Herod the Great", "He had died long before the ministry of Jesus ended."), ("Caiaphas", "He was the Jewish high priest."), ("Pompey", "He took Jerusalem for Rome in 63 BC.")],
      "All four Gospels name Pilate.", T_PASS, "Recall", "Think of the Roman who handed Jesus over."),
    K("Which Gospel ends with the Great Commission on a mountain in Galilee?", "Matthew", [
        ("Mark", "Mark's shortest ending has the women at the empty tomb, afraid."), ("Luke", "Luke ends with the ascension and joy in the Temple."), ("John", "John ends with an appearance at the lake and the restoration of Peter.")],
      "Matthew 28:16-20.", T_PASS, "Recall", "Think of 'make disciples of all nations'."),
    K("In which Gospel does Pilate wash his hands before the crowd?", "Matthew", [
        ("Mark", "Mark has no handwashing."), ("Luke", "Luke stresses Pilate's declarations of innocence but has no handwashing."), ("John", "John has the long dialogue about kingship but no handwashing.")],
      "Matthew 27:24 is the only account of the handwashing.", T_PASS, "Recall", "Which Gospel stresses fulfilment and the responsibility of the crowd?"),
    K("What is Emmaus, in Luke 24?", "A village about seven miles from Jerusalem", [
        ("A disciple of Jesus", "The two disciples are Cleopas and another, not Emmaus."), ("A mountain in Galilee", "The mountain is in Matthew's ending."), ("The name of the high priest", "The high priest was Caiaphas.")],
      "The Board's report notes that some candidates took Emmaus to be a person.", T_PASS, "Recall", "It is a place name."),
    K("Which Gospel gives Jesus' last word on the cross as 'It is finished'?", "John", [
        ("Mark", "Mark has the cry of distress."), ("Matthew", "Matthew follows Mark's cry."), ("Luke", "Luke has the prayer 'Father, into your hands'.")],
      "John 19:30 presents Jesus as in control.", T_PASS, "Recall", "Which Gospel shows Jesus in control?"),
    K("How does the shortest ending of Mark (16:8) end the Gospel?", "With the women fleeing from the empty tomb afraid", [
        ("With the Great Commission", "That is Matthew."), ("With the ascension", "That is Luke (and Acts)."), ("With Thomas's confession", "That is John 20.")],
      "The longer ending (16:9-20) is thought by most scholars to have been added later.", T_PASS, "Recall", "Think of how Mark's abrupt ending is described."),
    K("Which words are said by Thomas in John 20?", "My Lord and my God", [
        ("Truly this man was the Son of God", "Said by the centurion in Mark 15."), ("It is finished", "Said by Jesus in John 19."), ("Father, forgive them", "A saying of Jesus in Luke 23 in many manuscripts.")],
      "The confession of Thomas is the high point of John's resurrection stories.", T_PASS, "Recall", "He had doubted until he saw."),
    K("Which statement about responsibility for the death of Jesus is the most careful?", "Crucifixion was a Roman punishment, the Gospels show some Jewish leaders and Pilate involved, and the whole Jewish people are not to be blamed", [
        ("The Jewish people as a whole are responsible", "This is rejected by responsible scholars and has caused great harm."), ("Only Pilate was involved, and the Gospels do not mention the Jewish leaders", "The Gospels describe both."), ("No one was responsible, because the event is legend", "Historians generally accept the crucifixion under Pilate as historical.")],
      "A careful answer is historical and fair.", T_PASS, "Reasoning", "Which option avoids blaming a whole people?"),
], 205)

# ================================================================== 6. Spread and persecutions
SET(M5, T_SPREAD, "Spread and persecutions: causes, events and results", "rsl2-spread-and-persecutions", [
    K("What does 'Pax Romana' mean?", "A long period of relative peace and order under Roman rule", [
        ("The Roman law on religion", "It is a general word for peace, not a law."), ("The Council of Rome", "It is not a council."), ("The Roman army's rule in Palestine only", "It refers to the empire as a whole.")],
      "The peace and roads helped travel and missions.", T_SPREAD, "Recall", "Pax means peace."),
    K("Which of the following is NOT usually given as a reason for the spread of Christianity?", "State support from the emperors in the first century", [
        ("Roman roads and sea routes", "These helped travel."), ("The common use of Greek", "This helped preaching and writing."), ("Jewish synagogues in the Diaspora", "These gave a first audience.")],
      "Emperors began to favour the Church only with Constantine in the fourth century.", T_SPREAD, "Concept", "Which factor came much later?"),
    K("Which emperor ordered the first persecution planned for the whole empire, requiring all citizens to sacrifice?", "Decius", [
        ("Nero", "His persecution was local, in Rome."), ("Trajan", "He ordered that Christians be not sought out."), ("Constantine", "He ended persecution.")],
      "Decius (249-251) required certificates of sacrifice.", T_SPREAD, "Recall", "Remember the certificates (libelli)."),
    K("What was Nero's persecution (AD 64) connected with?", "The great fire at Rome", [
        ("A rebellion in Judaea", "The Jewish revolt began in AD 66."), ("The refusal to pay taxes", "It was not about taxes."), ("The Council of Nicaea", "This was in 325.")],
      "Tacitus reports that Nero blamed Christians for the fire.", T_SPREAD, "Recall", "Think of an event in Rome in 64."),
    K("In what year did Constantine and Licinius agree a policy of toleration (the Edict of Milan)?", "AD 313", [
        ("AD 64", "This is the date of Nero's persecution."), ("AD 325", "This is the date of the Council of Nicaea."), ("AD 380", "This is the date associated with Theodosius and the Nicene faith.")],
      "311 was Galerius's edict; 313 is Milan.", T_SPREAD, "Recall", "A date a little before Nicaea."),
    K("Who were the 'lapsi'?", "Christians who gave way and sacrificed or denied the faith under persecution", [
        ("Bishops who were martyred", "Martyrs were those who died for the faith."), ("Christians who fled abroad as missionaries", "They are not described as lapsi."), ("Pagan priests", "Lapsi were members of the Church.")],
      "The question of how to receive them back caused disputes.", T_SPREAD, "Concept", "The word means 'those who fell'."),
    K("Why were Christians often accused of atheism?", "They refused to worship the gods of Rome and the emperor", [
        ("They denied that God existed", "They believed in one God; the charge was about the Roman gods."), ("They refused to pay taxes", "This was not the reason given."), ("They did not attend their own churches", "They did meet, often in houses.")],
      "Refusal to sacrifice to the gods and to the emperor seemed disloyal.", T_SPREAD, "Reasoning", "Think of which gods they refused."),
    K("What did Trajan reply when Pliny asked how to treat Christians (about AD 112)?", "Do not seek them out, but punish those brought forward who refuse to worship the gods", [
        ("Arrest all Christians at once", "He told Pliny not to hunt them out."), ("Accept anonymous accusations", "He said anonymous charges were not to be accepted."), ("Release all Christians as lawful", "Those who refused to obey were to be punished.")],
      "This shows that the name of Christian could be punished, but there was no search policy.", T_SPREAD, "Application", "Think of the cautious policy."),
], 206)

# ================================================================== 7. Apologists and heresies
SET(M5, T_APOL, "Apologists, Gnostics, Marcion and Montanus", "rsl2-apologists-and-heresies", [
    K("What is an apologist?", "A writer who defends the Christian faith with reasoned arguments", [
        ("A Christian who says sorry for the faith", "The word comes from apologia, 'a defence'."), ("A bishop who runs a council", "This is a different role."), ("A teacher of heresy", "Apologists defended the faith.")],
      "The Greek word apologia means defence.", T_APOL, "Recall", "Think of 'apology' in the old sense."),
    K("In which city did Tertullian live and work?", "Carthage", [
        ("Rome", "Justin Martyr taught in Rome."), ("Alexandria", "Origen's school was there."), ("Lyons", "Irenaeus was bishop there.")],
      "He wrote in Latin in North Africa.", T_APOL, "Recall", "Think of Africa."),
    K("Which is a common feature of Gnosticism?", "Salvation through secret knowledge (gnosis)", [
        ("Salvation through the sacraments only", "That is not the heart of Gnosticism."), ("The belief that the material world is good", "Many Gnostics viewed matter as flawed or evil."), ("Strict obedience to bishops", "Gnostic teaching stressed knowledge, not church authority.")],
      "Gnosis means knowledge.", T_APOL, "Concept", "The name Gnostic comes from a Greek word."),
    K("What does 'docetism' teach?", "That Christ only seemed to have a human body", [
        ("That Christ had two natures in one person", "That is the Chalcedonian teaching."), ("That Christ was a creature", "This is Arianism."), ("That Christ was only human", "Docetism denies the true humanity.")],
      "It comes from the Greek verb 'to seem'.", T_APOL, "Concept", "Think of 'seeming'."),
    K("What did Marcion teach about the Old Testament?", "He rejected it and said its God was different from the Father of Jesus", [
        ("He said it should be read as an allegory only", "He rejected it rather than interpreting it."), ("He added more books to it", "He cut the Scriptures down."), ("He taught that it was written by Paul", "This is not part of his teaching.")],
      "He kept an edited Luke and ten letters of Paul.", T_APOL, "Recall", "Think of two Gods."),
    K("What did Montanus and his prophetesses claim?", "That the Holy Spirit was speaking in a new prophecy through them", [
        ("That the Son was a creature", "This was Arius."), ("That matter is evil", "This is a Gnostic teaching."), ("That the Old Testament should be dropped", "This is Marcion.")],
      "The New Prophecy began in Phrygia.", T_APOL, "Recall", "Think of Priscilla and Maximilla."),
    K("What happened at Nag Hammadi in 1945?", "A collection of Gnostic and related texts was found in Egypt", [
        ("The first Gospel manuscripts were found", "Gospel manuscripts were known earlier."), ("The Council of Nicaea took place", "This was in 325."), ("Marcion was excluded from the Church", "This was about AD 144.")],
      "It allows scholars to read Gnostic texts in their own words.", T_APOL, "Recall", "Think of Egyptian discoveries."),
    K("How did Marcion's challenge contribute to the formation of the New Testament canon?", "It made the Church state more clearly which books it accepted and keep the Old Testament", [
        ("It led the Church to drop the Old Testament", "The Church kept it."), ("It produced the list of the twenty-seven books at once", "The canon was settled over a longer period."), ("It had no effect on the canon", "Many scholars say it made the question urgent.")],
      "The Church replied to Marcion's list with its own wider canon.", T_APOL, "Reasoning", "Think of cause and response."),
], 207)

# ================================================================== 8. Nicaea and Chalcedon
SET(M5, T_COUN, "Arius, Nicaea, Ephesus and Chalcedon", "rsl2-nicaea-chalcedon", [
    K("Which emperor called the Council of Nicaea (AD 325)?", "Constantine", [
        ("Nero", "He reigned in the first century."), ("Decius", "He persecuted in the third century."), ("Marcian", "He called the Council of Chalcedon in 451.")],
      "Constantine wanted unity in the Church and the empire.", T_COUN, "Recall", "He had recently ended persecution."),
    K("What did Arius teach?", "That the Son is a creature made by the Father, not eternal in the same sense", [
        ("That the Son is equal to the Father", "This was the view of Alexander and Athanasius."), ("That Christ had only one nature", "This is linked with Eutyches."), ("That Mary should not be called Theotokos", "This is linked with Nestorius.")],
      "Arius said that there was a time when the Son did not exist.", T_COUN, "Recall", "He was a presbyter of Alexandria."),
    K("What does the Greek word homoousios mean in the Nicene Creed?", "Of one substance (being) with the Father", [
        ("Of like substance with the Father", "That is homoiousios, the word of a middle party."), ("Created by the Father", "That is the Arian view."), ("Born of the Virgin Mary", "That is a different statement of the creed.")],
      "It was chosen to exclude the view of Arius.", T_COUN, "Concept", "Homo means same."),
    K("Who defended the teaching of Nicaea most strongly in the following decades?", "Athanasius, bishop of Alexandria", [
        ("Arius", "He was the opponent."), ("Nestorius", "He was a patriarch of Constantinople in the fifth century."), ("Eutyches", "He was a monk and opponent of Nestorius.")],
      "Athanasius was exiled several times for his stand.", T_COUN, "Recall", "He succeeded Alexander in Alexandria."),
    K("What was the main issue at the Council of Ephesus (431)?", "The teaching of Nestorius and the title Theotokos for Mary", [
        ("The date of Easter", "This was discussed at Nicaea."), ("The books of the New Testament", "The canon was not settled at Ephesus."), ("The Holy Spirit and the creed", "This was Constantinople (381).")],
      "Nestorius was understood to divide Christ into two persons.", T_COUN, "Recall", "Think of 'God-bearer'."),
    K("What did the Definition of Chalcedon (451) teach?", "That Christ is one person in two natures, fully God and fully human", [
        ("That Christ has one nature only", "This was the view opposed at Chalcedon."), ("That the Son is a creature", "This was Arianism, condemned at Nicaea."), ("That Christ's body was only an appearance", "This is docetism.")],
      "The natures are united without confusion, change, division or separation.", T_COUN, "Recall", "One person, two natures."),
    K("Which church is among those that did not accept Chalcedon?", "The Ethiopian Orthodox Tewahedo Church", [
        ("The Church of Rome", "It accepted Chalcedon."), ("The Greek Orthodox Church of Constantinople", "It accepted Chalcedon."), ("The Lutheran churches", "They began in the sixteenth century.")],
      "Oriental Orthodox churches include Coptic, Ethiopian, Syriac and Armenian.", T_COUN, "Application", "Think of the Oriental Orthodox group."),
    K("'The Council of Nicaea ended the Arian controversy.' Which comment is best?", "It condemned Arius, but the dispute continued for decades and was settled at Constantinople in 381", [
        ("It is entirely correct, since nothing more was said about Arius", "The dispute went on for many years."), ("It is wrong, because Nicaea never discussed Arius", "Nicaea was called because of Arius."), ("It is wrong, because the Arians won at Nicaea", "Arius was condemned at Nicaea.")],
      "Good evaluation notes the limits of a decision.", T_COUN, "Reasoning", "Think of the dates 325 and 381."),
], 208)


# ================================================================== 9. Arguments for the existence of God
SET(M5, T_ARG, "Ontological, cosmological, teleological and moral arguments", "rsl2-arguments-for-god", [
    K("What is an a posteriori argument?", "One that starts from something observed in the world", [
        ("One that uses reason alone without observation", "That describes an a priori argument."), ("One that has no premises", "Every argument has premises."), ("One that always proves its conclusion", "No kind of argument is guaranteed to persuade everyone.")],
      "Cosmological, teleological and moral arguments start from experience.", T_ARG, "Concept", "Posteriori means 'from what comes after' experience."),
    K("The ontological argument of Anselm starts from", "the definition of God as the greatest being that can be conceived", [
        ("the order of the natural world", "That is the teleological argument."), ("the existence of motion", "That is Aquinas's first way."), ("the experience of conscience", "That is the moral argument.")],
      "It is an a priori argument from the idea of God.", T_ARG, "Recall", "Which argument starts from an idea, not an observation?"),
    K("What was Gaunilo's objection to Anselm?", "The same reasoning would seem to prove that a perfect island exists", [
        ("Existence is not a predicate", "That is Kant's criticism."), ("Every member of a series has a cause", "That is part of the cosmological argument."), ("Conscience comes from upbringing", "That is Freud's view of conscience.")],
      "Gaunilo tried to show that the form of argument is faulty.", T_ARG, "Recall", "He wrote 'on behalf of the fool'."),
    K("What is Kant's main objection to the ontological argument?", "Existence is not a property that adds to the concept of a thing", [
        ("It starts from an observation of the world", "It is an a priori argument, not an observation."), ("It cannot be understood by non-believers", "That is not his objection."), ("It depends on the Big Bang", "Kant lived long before the Big Bang theory.")],
      "A hundred real coins contain no more than a hundred possible ones in the concept.", T_ARG, "Concept", "Think of existence as a 'real predicate'."),
    K("Which of Aquinas's Ways argues that if everything were contingent, nothing would exist now?", "The third way (contingency and necessity)", [
        ("The first way (motion)", "This argues from change to an unmoved mover."), ("The second way (efficient causes)", "This argues from a series of causes to a first cause."), ("The fifth way (design)", "This argues from order and direction.")],
      "The third way ends with a necessary being.", T_ARG, "Application", "The key word is contingent."),
    K("Russell's objection that 'every human has a mother, but that does not mean humanity has a mother' is an example of criticising", "the fallacy of composition in the cosmological argument", [
        ("the argument from design", "This criticism is about parts and wholes, not design."), ("Kant's moral argument", "This is not about morality."), ("Anselm's definition of God", "This is about causes of a whole.")],
      "What is true of each part is not necessarily true of the whole.", T_ARG, "Reasoning", "Think of parts and wholes."),
    K("Which writer used the image of a watch found on the ground in the design argument?", "William Paley", [
        ("David Hume", "He criticised the design argument."), ("Immanuel Kant", "He gave the moral argument."), ("Anselm", "He gave the ontological argument.")],
      "The watch needs a maker; so does the world.", T_ARG, "Recall", "He wrote in 1802."),
    K("In Kant's moral argument, why is belief in God needed?", "To make sense of the highest good in which virtue and happiness go together", [
        ("Because God is observed in nature", "That is a design argument."), ("Because everything has a cause", "That is a cosmological argument."), ("Because existence is a perfection", "That is Descartes's ontological argument.")],
      "God is a postulate of practical reason, not a conclusion of theoretical proof.", T_ARG, "Concept", "Think of duty, virtue and happiness."),
], 209)

# ================================================================== 10. Paper 1
SET(MX, "Paper 1", "Paper 1: format and technique", "rsl2-exam-paper-1", [
    K("According to the Board's 2023 report, how many multiple-choice questions are in Religious Studies Paper 1?", "50", [
        ("18", "This is the number of essay questions in Paper 2."), ("36", "This is the number of structural questions in Paper 3."), ("100", "This is the maximum raw mark of Papers 2 and 3.")],
      "Paper 1 had 50 questions and a maximum raw mark of 50.", "Paper 1", "Recall", "Think of Paper 1 in the report."),
    K("What weighting does the report give for Paper 1?", "About 34 per cent", [
        ("About 10 per cent", "This is far too low."), ("About 50 per cent", "This is too high."), ("About 70 per cent", "This is too high.")],
      "Papers 2 and 3 are about 33 per cent each.", "Paper 1", "Recall", "The three papers are nearly equal."),
    K("A stem says 'Which of the following is NOT a feature of the Gospel of John?' What should you do?", "Check every option and choose the one that is not found in John", [
        ("Choose the first true statement about John", "The question asks for the exception."), ("Choose the longest option", "Length is not a clue."), ("Skip it, because negative questions are unfair", "They are legitimate; read carefully.")],
      "A NOT question reverses the usual task.", "Paper 1", "Application", "Underline the word NOT."),
    K("The Board recommends that students prepare for Paper 1 by", "studying widely and comparing religions", [
        ("studying only the section they like", "Paper 1 covers the syllabus as a whole."), ("learning past answers by heart", "The report does not recommend this."), ("ignoring the key terms", "Key terms are the main material of Paper 1.")],
      "The report urges wide reading and comparative study.", "Paper 1", "Recall", "Think of the Board's recommendation."),
    K("You are unsure of an answer. Which is the best next step?", "Remove the options you know are wrong and choose from the rest", [
        ("Leave the question blank", "A blank cannot score."), ("Choose the option with the most words every time", "Length is not a reliable guide."), ("Change all your earlier answers", "This is not a sound technique.")],
      "Elimination improves your chance and uses what you know.", "Paper 1", "Reasoning", "Use what you know first."),
    K("A distractor in a multiple-choice question is", "a wrong option that looks right to someone with a common confusion", [
        ("the correct option", "That is the key."), ("the question stem", "The stem is the question."), ("an option left blank", "Distractors are written options.")],
      "Examiners write distractors from real confusions, such as mixing two Gospels.", "Paper 1", "Concept", "A distractor distracts."),
    K("A student reads 'Which Gospel includes the 'I am' sayings with a picture, such as the bread of life?' and chooses Mark because Mark mentions bread. What went wrong?", "The student chose an option that sounded familiar without checking the Gospel named", [
        ("Nothing: Mark has these sayings", "These sayings are characteristic of John."), ("The student should have chosen Luke", "Luke does not have them either."), ("The question has no correct answer", "The correct answer is John.")],
      "Check the name, the religion and the book before choosing.", "Paper 1", "Application", "Which Gospel has the seven I am sayings?"),
    K("In KKEVO's practice Paper 1 mock for this course, what is the time limit?", "90 minutes (a KKEVO practice setting)", [
        ("30 minutes", "This is too short for 50 questions."), ("3 hours", "This is for the longer papers in some subjects."), ("No time limit", "The mock is timed.")],
      "The Board's report does not state the time, so check your timetable.", "Paper 1", "Recall", "It is stated in the lesson."),
], 210)

# ================================================================== 11. Paper 2
SET(MX, "Paper 2", "Paper 2: choosing a section and planning essays", "rsl2-exam-paper-2", [
    K("According to the Board's 2023 report, how many questions must a candidate answer in Paper 2?", "Four, all from one section", [
        ("Two from each section", "The instruction is to choose all from one section."), ("Eighteen", "There are 18 questions in the paper, not 18 answers."), ("Six, one from each of six sections", "The paper has three sections of six questions.")],
      "Each section has six questions; candidates choose four from one section.", "Paper 2", "Recall", "Think of 'one section'."),
    K("Which three sections did the 2023 Paper 2 contain?", "The Old Testament, Islam and African Traditional Religious Beliefs and Practices", [
        ("Luke, John and Acts", "These are Paper 3 sections."), ("Philosophy of Religion, Ethics and Islam", "Philosophy of Religion and Ethics are Paper 3 sections."), ("Hinduism, Buddhism and Judaism", "The report does not name these as Paper 2 sections.")],
      "The report names them as Sections 1.1, 5.3 and 5.5.", "Paper 2", "Recall", "Paper 2 is the essay paper."),
    K("What is the main fault the report describes in many answers on the Exodus and Ramadan?", "Narrating or describing instead of explaining the significance or the demand", [
        ("Writing too much about the future", "This is not the fault described."), ("Answering in the wrong language", "This is not described."), ("Refusing to answer the question", "The candidates attempted the question.")],
      "Examiners want importance, roles and meaning, not a retelling.", "Paper 2", "Interpretation", "Think of 'importance' versus 'story'."),
    K("A question says 'Examine the importance of the Exodus to Israel'. What should most of the answer do?", "Explain what the Exodus meant for Israel's faith, covenant and worship", [
        ("Retell the plagues in order", "This is narration."), ("List the names of the Egyptian kings", "This is not asked."), ("Describe the geography of Sinai only", "This does not answer the question about importance.")],
      "The command is about importance.", "Paper 2", "Application", "What does 'importance' ask for?"),
    K("Why must you check all six questions in a section before choosing it?", "Because you must answer four from the same section", [
        ("Because every section has the same questions", "The sections differ."), ("Because you may only answer the first four", "You may choose any four in the section."), ("Because marks are given for the section chosen", "Marks are given for the answers.")],
      "A section with one favourite question and three weak ones is a poor choice.", "Paper 2", "Reasoning", "Count the questions you can answer well."),
    K("If the paper has a maximum raw mark of 100 and four answers are required, how many marks does each answer carry on average?", "25", [
        ("10", "Four answers of 10 marks would total 40."), ("20", "Four answers of 20 marks would total 80."), ("50", "Four answers of 50 marks would total 200.")],
      "100 divided by 4 gives 25.", "Paper 2", "Calculation", "Divide the total by the number of answers."),
    K("Which is the best use of the first minutes spent on each essay?", "Write a short plan with a thesis, four or five points and a conclusion", [
        ("Write the conclusion first and stop", "A conclusion alone is not an essay."), ("Copy the question twice", "This wastes time."), ("Begin writing without thinking", "Unplanned essays often wander.")],
      "A plan keeps the essay on the demand.", "Paper 2", "Application", "Think of structure."),
    K("Which thesis best answers 'Explain why the Exodus is central to the religion of Israel'?", "The Exodus is the founding act of Israel's relationship with God and shapes covenant, worship and identity", [
        ("The Exodus is a long story with many plagues", "This describes, but does not explain centrality."), ("Moses was born in Egypt", "This is a single fact."), ("Pharaoh was a strong king", "This is a fact, not an answer.")],
      "A thesis states the answer in one sentence.", "Paper 2", "Reasoning", "Which option gives a reason?"),
], 211)

# ================================================================== 12. Paper 3
SET(MX, "Paper 3", "Paper 3: structural questions on Luke, John, Acts and philosophy", "rsl2-exam-paper-3", [
    K("According to the Board's 2023 report, how many questions must a candidate answer in Paper 3?", "Four, from one section of choice", [
        ("Six, one from each section", "There are six sections but you answer from one."), ("Thirty-six", "This is the number of questions in the paper."), ("Two from each of two sections", "The instruction is four from one section.")],
      "The paper has six sections of six questions.", "Paper 3", "Recall", "Think of 'a section of their choice'."),
    K("Which of these is a section named for Paper 3 in the 2023 report?", "John, the Fourth Gospel", [
        ("The Old Testament", "This is a Paper 2 section."), ("African Traditional Religious Beliefs and Practices", "This is a Paper 2 section."), ("Hinduism", "It is not named as a Paper 3 section.")],
      "Paper 3 sections: Luke, John, Acts and 1 Corinthians, Philosophy of Religion, Ethics and Morality, Historical Development of Islam.", "Paper 3", "Recall", "The Gospels are in Paper 3."),
    K("The report says that a few candidates took Emmaus to be", "a person", [
        ("a mountain", "This was not mentioned."), ("a book of the Bible", "This was not mentioned."), ("a festival", "This was not mentioned.")],
      "Emmaus is a village.", "Paper 3", "Recall", "Check the Luke comments."),
    K("In a Paper 3 answer on the attitude of Jesus to those he ministered to, the report says many candidates did not", "place their answers in the Palestinian context", [
        ("write in complete sentences", "This is not what the report says."), ("mention the Pharisees at all", "Many wrote about the Pharisees instead."), ("answer in time", "This is not what the report says.")],
      "Context means the setting in Palestine.", "Paper 3", "Interpretation", "Think of 'situate'."),
    K("A question on John 9 and the light of the world should bring out", "the theme of spiritual blindness and sight", [
        ("only the order of the miracles", "This does not explain the theme."), ("the history of the pool of Siloam only", "This is a detail, not the theme."), ("the Temple tax", "This is not in chapter 9.")],
      "The report expects the theme of spiritual blindness.", "Paper 3", "Application", "Sight and blindness."),
    K("How much should you write for a part worth two marks?", "Two clear points, briefly", [
        ("A full page", "This wastes time."), ("One word", "Too little for two marks."), ("An essay with a conclusion", "It does not suit a two-mark part.")],
      "Match length to the marks.", "Paper 3", "Application", "Marks signal the length."),
    K("In a structured question the last part says 'Assess'. What does it require?", "A reasoned judgement supported by evidence", [
        ("A list of facts", "A list does not judge."), ("A retelling of the story", "This is narration."), ("A one-word answer", "An assessment needs reasons.")],
      "Assess means weigh and judge.", "Paper 3", "Concept", "Which command word asks for a judgement?"),
    K("For the Good Samaritan, the report says candidates should concentrate on", "love and discipleship", [
        ("the geography of the road to Jericho", "This is background only."), ("the history of the Samaritans in full", "This is too much detail."), ("a full retelling of the story", "This is the narration the report criticises.")],
      "The teaching is about love for neighbour and the way of discipleship.", "Paper 3", "Recall", "Think of Luke 10."),
], 212)


# ================================================================== Paper 1 mock exam A (50 questions)
P1 = [
    # --- Module 1 (13): Documentary Hypothesis 3, Genesis 1 to 11 2, patriarchal covenants 2, Exodus 2, Mosaic covenant 2, Holiness Code 2
    K("The Documentary Hypothesis proposes that the Pentateuch was made by combining", "four main written sources, usually called J, E, D and P", [
        ("one work written by Moses alone, with no later additions", "This is the traditional view that the theory questions."), ("oral stories only, never written down until the exile", "The theory is about written sources."), ("two sources, called Mark and Q", "These are Synoptic Gospel sources.")],
      "The sources are the Yahwist, Elohist, Deuteronomist and Priestly writers.", T_DH, "Recall", "Name the four letters."),
    K("Which source is thought to use the name Yahweh from the beginning of Genesis?", "J, the Yahwist", [
        ("E, the Elohist", "E uses Elohim until the name is revealed to Moses."), ("D, the Deuteronomist", "D is the source of Deuteronomy."), ("P, the Priestly source", "P is linked with worship, genealogies and laws.")],
      "J is named from the German form of Yahweh.", T_DH, "Recall", "The letter J is for Jahwe."),
    K("Which source is linked with the book of Deuteronomy and, by many scholars, with the reform of Josiah?", "D", [
        ("J", "J is linked with Judah and Genesis stories."), ("E", "E is linked with the northern kingdom."), ("P", "P is linked with priestly material.")],
      "Josiah's reform was in about 621 BC.", T_DH, "Recall", "D stands for Deuteronomist."),
    K("The Enuma Elish is", "a Babylonian creation epic", [
        ("an Egyptian account of the Exodus", "It is not Egyptian and not about the Exodus."), ("a Hittite treaty", "A treaty is a different kind of text."), ("a Canaanite law code", "It is a creation story, not a law code.")],
      "It is often compared with Genesis 1.", T_GEN, "Recall", "It is from Mesopotamia."),
    K("A main difference between the Genesis flood story and the Mesopotamian flood stories is that Genesis", "presents one God who sends the flood for moral reasons", [
        ("names many gods who quarrel", "That describes the Mesopotamian accounts."), ("has no ark", "Genesis has the ark of Noah."), ("does not mention a hero who survives", "Noah survives in Genesis.")],
      "Genesis stresses human violence and wickedness and one God.", T_GEN, "Concept", "Think of 'moral'."),
    K("Which promises are made to Abraham in Genesis?", "Land, descendants and blessing", [
        ("A king and a temple", "These belong to the later promise to David and Solomon."), ("The law at Sinai", "This belongs to Moses."), ("A new covenant written on hearts", "This is in Jeremiah.")],
      "The three promises are repeated to the patriarchs.", T_PAT, "Recall", "Genesis 12, 15 and 17."),
    K("What is the sign of the covenant with Abraham in Genesis 17?", "Circumcision", [
        ("The Sabbath", "This is linked with creation and the Sinai covenant."), ("The rainbow", "This is the sign of the covenant with Noah."), ("The Passover lamb", "This is linked with the Exodus.")],
      "Every male is to be circumcised.", T_PAT, "Recall", "Think of Genesis 17."),
    K("The Merneptah Stele (about 1208 BC) is important because it", "names Israel as a people in Canaan", [
        ("describes the ten plagues", "It does not mention the plagues."), ("names Moses", "It does not name Moses."), ("describes the crossing of the sea", "It does not mention a crossing.")],
      "It is the oldest known text outside the Bible to mention Israel.", T_EXO, "Recall", "It is an Egyptian victory inscription."),
    K("The early date of the Exodus (about 1446 BC) is based mainly on", "1 Kings 6:1, which gives 480 years before Solomon's Temple", [
        ("the name Raamses in Exodus 1:11", "This is used for the late date."), ("the Merneptah Stele", "This is used for the later limit, not for 1446 BC."), ("the Dead Sea Scrolls", "These are much later.")],
      "Solomon's fourth year is about 966 BC.", T_EXO, "Reasoning", "Add 480 years."),
    K("Where did Israel make the covenant with Yahweh through Moses?", "Mount Sinai", [
        ("Mount Carmel", "This is the scene of Elijah's contest."), ("Bethel", "This is a place linked with Jacob."), ("Jerusalem", "The covenant was made before Jerusalem was Israel's city.")],
      "Exodus 19 to 24.", T_MOS, "Recall", "Think of the mountain of the law."),
    K("The treaty-form theory compares the Sinai covenant with", "Hittite suzerainty treaties", [
        ("Roman wills", "These are much later."), ("Greek plays", "These are not treaties."), ("Egyptian proverbs", "These are wisdom texts.")],
      "The comparison notes the preamble, history, laws, blessings and curses.", T_MOS, "Concept", "A treaty between a great king and a vassal."),
    K("Where is the Holiness Code found?", "Leviticus 17 to 26", [
        ("Exodus 20 to 24", "This is the Book of the Covenant."), ("Deuteronomy 12 to 26", "This is the Deuteronomic code."), ("Numbers 1 to 10", "These are the census chapters.")],
      "It calls Israel to be holy as God is holy.", T_HOL, "Recall", "A chapter range in Leviticus."),
    K("Which command is found in the Holiness Code?", "You shall love your neighbour as yourself", [
        ("Hear, O Israel, the Lord our God, the Lord is one", "This is in Deuteronomy 6."), ("Let my people go", "This is in the story of Moses and Pharaoh in Exodus."), ("The Lord is my shepherd", "This is Psalm 23.")],
      "Leviticus 19:18.", T_HOL, "Recall", "Think of Leviticus 19."),
    # --- Module 2 (11): judges 2, Saul 2, David 3, Solomon 2, Temple 2
    K("In the book of Judges, a 'judge' was", "a leader raised up by God to deliver Israel and guide the tribes", [
        ("a hereditary king", "Judges did not found dynasties."), ("the high priest", "The high priest was a different office."), ("a Roman governor", "The judges were long before Rome.")],
      "Most judges are called charismatic leaders.", T_JUD, "Recall", "Think of Gideon or Deborah."),
    K("Which scholar proposed the amphictyony theory of the tribal confederacy?", "Martin Noth", [
        ("Julius Wellhausen", "He is linked with the Documentary Hypothesis."), ("B. H. Streeter", "He is linked with the Four-Source Hypothesis."), ("Rudolf Bultmann", "He is linked with form criticism.")],
      "The theory compares the tribes with Greek and Italian leagues around a shrine.", T_JUD, "Recall", "A German scholar of the 1930s."),
    K("Who anointed Saul as the first king of Israel?", "Samuel", [
        ("Nathan", "He is the prophet of David's reign."), ("Eli", "He was the priest at Shiloh before Samuel."), ("Zadok", "He was a priest in David's and Solomon's time.")],
      "1 Samuel 9 and 10.", T_SAUL, "Recall", "The last judge."),
    K("Saul died in battle with the Philistines at", "Mount Gilboa", [
        ("Mount Carmel", "This is the scene of Elijah's contest."), ("Jericho", "This is the first city of the conquest."), ("Hebron", "This is the city where David was first made king.")],
      "1 Samuel 31.", T_SAUL, "Recall", "A mountain in the north."),
    K("The Davidic covenant of 2 Samuel 7 promises", "a house (dynasty) for David that will last", [
        ("land to Abraham", "That is in Genesis."), ("laws at Sinai", "That is the Mosaic covenant."), ("a new covenant written on hearts", "That is in Jeremiah.")],
      "Nathan's oracle says the throne will be established.", T_DAV, "Recall", "Think of Nathan's message."),
    K("Which prophet confronted David over Bathsheba and Uriah?", "Nathan", [
        ("Samuel", "He had anointed David but was dead by then."), ("Elijah", "He lived much later."), ("Amos", "He lived much later.")],
      "2 Samuel 12.", T_DAV, "Recall", "He is also the prophet of 2 Samuel 7."),
    K("David captured which city and made it his capital?", "Jerusalem", [
        ("Hebron", "David ruled from Hebron at first, over Judah."), ("Shiloh", "This was the shrine before the monarchy."), ("Samaria", "This was built later as the capital of the northern kingdom.")],
      "He then brought the ark to the city.", T_DAV, "Recall", "The city of Zion."),
    K("Which of the following was a problem of Solomon's reign that is linked to the division of the kingdom?", "Forced labour and heavy burdens on the people", [
        ("The loss of the ark to the Philistines", "That happened in the time of Eli and Samuel."), ("Defeat by Babylon", "That happened much later."), ("The rejection of Saul", "That was before David.")],
      "The northern tribes complained to Rehoboam about heavy burdens.", T_SOL, "Concept", "1 Kings 11 and 12."),
    K("In 1 Kings 3, Solomon asks God for", "an understanding mind to govern the people", [
        ("long life", "He did not ask for long life."), ("riches", "He did not ask for riches."), ("victory over his enemies", "He did not ask for victory.")],
      "Because he asked for wisdom, God also gave him other gifts.", T_SOL, "Recall", "Think of his reputation."),
    K("Who could enter the Holy of Holies, and when?", "The high priest, once a year on the Day of Atonement", [
        ("Any priest, every Sabbath", "Only the high priest entered."), ("The king at his coronation", "The king did not enter."), ("The Levites at Passover", "The Levites did not enter.")],
      "Leviticus 16.", T_TEM, "Recall", "Think of the most holy room."),
    K("Which offering was entirely burned on the altar?", "The burnt offering", [
        ("The peace offering", "Part of this was eaten by the worshipper."), ("The grain offering", "Only a portion was burned."), ("The guilt offering", "This was for restitution and part went to the priest.")],
      "It signified complete dedication.", T_TEM, "Recall", "The name says it."),
    # --- Module 3 (8): background 2, groups 2, oral/form/redaction 2, Synoptic problem 2
    K("The Maccabean revolt began as a response to", "Antiochus IV's attempt to ban Jewish practices and his defiling of the Temple", [
        ("Herod's building of the Temple", "This was after the Maccabean period."), ("the destruction of the Temple in AD 70", "This was much later."), ("the decree of Cyrus", "This allowed the return from exile in 538 BC.")],
      "The revolt began in 167 BC.", T_BG, "Recall", "Think of Hanukkah."),
    K("The Septuagint is", "a Greek translation of the Hebrew Scriptures", [
        ("a Latin translation of the Gospels", "The Latin Bible came later."), ("an Aramaic paraphrase of the Law", "That describes a Targum."), ("a collection found near the Dead Sea", "That describes the Dead Sea Scrolls.")],
      "It was made for Jews who spoke Greek.", T_BG, "Recall", "Think of 'seventy'."),
    K("Which Jewish group centred on the Temple, accepted only the written law and denied the resurrection?", "The Sadducees", [
        ("The Pharisees", "They accepted the oral tradition and believed in the resurrection."), ("The Essenes", "They withdrew from Temple worship."), ("The Zealots", "They are known for revolt against Rome.")],
      "Mark 12:18 and Acts 23:8.", T_GRP, "Recall", "Priests and wealthy families."),
    K("Which group do many scholars link with Qumran and the Dead Sea Scrolls?", "The Essenes", [
        ("The Pharisees", "They are linked with the synagogue and the oral tradition."), ("The Sadducees", "They are linked with the Temple."), ("The Herodians", "They supported the family of Herod.")],
      "The link is debated, so say 'many scholars'.", T_GRP, "Recall", "A community that withdrew to the desert."),
    K("Which pair of scholars is associated with the beginnings of form criticism?", "Martin Dibelius and Rudolf Bultmann", [
        ("Willi Marxsen and Hans Conzelmann", "They are associated with redaction criticism."), ("B. H. Streeter and Austin Farrer", "They are associated with the Synoptic problem."), ("William Wrede and Albert Schweitzer", "They are associated with studies of Mark and the historical Jesus.")],
      "Form criticism arose in Germany in the 1910s and 1920s.", T_ORAL, "Recall", "Think of the study of 'forms'."),
    K("Redaction criticism studies", "how each evangelist edited and arranged his material to express his own aims", [
        ("the form of small units of oral tradition", "That is form criticism."), ("the Greek manuscripts and their differences", "That is textual criticism."), ("how stories were passed on by memory", "That concerns oral tradition.")],
      "It treats the evangelists as authors and theologians.", T_ORAL, "Concept", "Redaction means editing."),
    K("What is Q in the Two-Source Hypothesis?", "A source of sayings used by Matthew and Luke but not found in Mark", [
        ("A lost version of Mark", "Q is not a version of Mark."), ("A source used only by Matthew", "That is M."), ("A source used only by Luke", "That is L.")],
      "The name comes from the German Quelle, source.", T_SYN, "Recall", "The double tradition."),
    K("Which is an argument for Markan priority?", "Matthew and Luke follow Mark's order but never agree with each other against it", [
        ("Mark is the longest Gospel", "Matthew and Luke are longer."), ("Mark contains the Sermon on the Mount", "Mark does not."), ("All three Gospels have identical wording throughout", "They differ in many places.")],
      "This pattern is hard to explain if Matthew and Luke used each other.", T_SYN, "Reasoning", "Think of the order of events."),
    # --- Module 4 (10): titles 2, Kingdom 2, parables and miracles 2, John 2, passion 2
    K("Which Christological title means 'word, reason or plan' and is used in the Prologue of John?", "Logos", [
        ("Messiah", "This means anointed one."), ("Kyrios", "This means Lord."), ("Son of Man", "This is a title from Daniel 7 used in all four Gospels.")],
      "John 1:1-18.", T_CHR, "Recall", "A Greek word for word."),
    K("In Mark 14:61-62, the high priest asks Jesus whether he is", "the Christ, the Son of the Blessed", [
        ("the Logos", "This is not in Mark."), ("a teacher of the law", "This is not the question."), ("Elijah returned", "This was a question asked by others earlier.")],
      "Mark joins the title Messiah to suffering.", T_CHR, "Recall", "Recall the trial before the council."),
    K("Which view of the Kingdom of God is held by many scholars today?", "It has begun in Jesus' ministry and will be completed in the future", [
        ("It is entirely in the future", "This is the futurist view of Schweitzer."), ("It has been fully realised in the ministry of Jesus", "This is Dodd's realised view."), ("It is a political programme to expel the Romans", "The Gospels do not present it this way.")],
      "This is called inaugurated eschatology.", T_KING, "Concept", "Already but not yet."),
    K("The petition 'your kingdom come' in the Lord's Prayer suggests that the Kingdom is", "still to come in fullness as well as present in part", [
        ("entirely in the past", "The prayer asks for something to come."), ("only an inner feeling", "The prayer speaks of God's rule."), ("only a political state", "The prayer speaks of God's rule.")],
      "It supports the 'already but not yet' view.", T_KING, "Application", "A prayer asks for something that is not yet complete."),
    K("Which parable shows a father welcoming a returning son?", "The Prodigal (Lost) Son", [
        ("The Good Samaritan", "This is about helping a neighbour."), ("The Sower", "This is about responses to the word."), ("The Talents", "This is about use of gifts.")],
      "Luke 15:11-32.", T_PAR, "Recall", "Think of the feast."),
    K("Which of these is an exorcism?", "The healing of the Gerasene man", [
        ("Calming the storm", "This is a nature miracle."), ("The feeding of the five thousand", "This is a nature miracle."), ("The raising of the widow's son at Nain", "This is a raising of the dead.")],
      "An exorcism drives out an unclean spirit.", T_PAR, "Concept", "A man with a legion of demons."),
    K("What is the first of the seven signs in John?", "Water changed into wine at Cana", [
        ("The feeding of the five thousand", "This is the fourth sign."), ("The raising of Lazarus", "This is the seventh sign."), ("The healing of the man born blind", "This is the sixth sign.")],
      "John 2:1-11.", T_JOHN, "Recall", "A wedding."),
    K("In which passage does Jesus say 'I am the good shepherd'?", "John 10", [
        ("Luke 15", "That is the parable of the lost sheep, not an 'I am' saying."), ("Mark 10", "Mark has no 'I am' saying of this kind."), ("Matthew 25", "This chapter has the parable of the sheep and the goats, not this saying.")],
      "John 10:11.", T_JOHN, "Recall", "The chapter after the man born blind."),
    K("Which Gospel includes the Emmaus story?", "Luke", [
        ("Mark", "Mark has no appearance stories in its shortest ending."), ("Matthew", "Matthew's ending is in Galilee."), ("John", "John has the appearance at the lake and to Thomas.")],
      "Luke 24:13-35.", T_PASS, "Recall", "The Gospel that continues in Acts."),
    K("Which Gospel includes the appearance to Thomas?", "John", [
        ("Mark", "Mark's shortest ending has no appearance."), ("Matthew", "Matthew has the Great Commission."), ("Luke", "Luke has Emmaus and the ascension.")],
      "John 20:24-29.", T_PASS, "Recall", "Think of 'My Lord and my God'."),
    # --- Module 5 (8): spread 2, apologists 2, councils 2, arguments 2
    K("Which persecution began in AD 303 and is often called the Great Persecution?", "The persecution under Diocletian", [
        ("The persecution under Nero", "Nero's was in AD 64."), ("The persecution under Decius", "Decius' was in AD 249 to 251."), ("The policy of Trajan", "Trajan's reply to Pliny was about AD 112.")],
      "It ended with the edict of Galerius in 311.", T_SPREAD, "Recall", "Think of the early fourth century."),
    K("The edict of toleration of AD 311 was issued by", "Galerius", [
        ("Nero", "He reigned in the first century."), ("Decius", "He persecuted in the third century."), ("Theodosius", "He reigned in the late fourth century.")],
      "Galerius had been a leading persecutor.", T_SPREAD, "Recall", "A co-emperor of Diocletian."),
    K("Irenaeus of Lyons wrote Against Heresies mainly against", "Gnostic teachers", [
        ("the Arians", "Arius came in the fourth century."), ("Nestorius", "He lived in the fifth century."), ("the Donatists", "They arose after the Great Persecution.")],
      "He argued for one God and for apostolic teaching.", T_APOL, "Recall", "A second-century bishop."),
    K("Which scholar of Alexandria wrote a reply to the pagan critic Celsus?", "Origen", [
        ("Justin Martyr", "He taught in Rome."), ("Tertullian", "He worked in Carthage."), ("Irenaeus", "He was bishop of Lyons.")],
      "Origen worked in Alexandria and Caesarea.", T_APOL, "Recall", "Think of Alexandria."),
    K("Which council defined Christ as one person in two natures?", "Chalcedon (451)", [
        ("Nicaea (325)", "Nicaea dealt with Arius."), ("Constantinople (381)", "This council extended the creed on the Holy Spirit."), ("Ephesus (431)", "This council condemned Nestorius.")],
      "Called by the emperor Marcian.", T_COUN, "Recall", "The last of the four councils."),
    K("The Greek term Theotokos means", "God-bearer (mother of God)", [
        ("Son of God", "That is another title."), ("Word made flesh", "That is Logos made flesh in John 1:14."), ("of one substance", "That is homoousios.")],
      "It was the title in dispute at Ephesus.", T_COUN, "Recall", "Think of Mary."),
    K("Paley's watch is used to illustrate which argument?", "The teleological (design) argument", [
        ("The ontological argument", "This starts from the idea of God."), ("The cosmological argument", "This starts from the existence of the world."), ("The moral argument", "This starts from duty and conscience.")],
      "A watch implies a watchmaker.", T_ARG, "Recall", "Think of purpose in nature."),
    K("Which philosopher criticised the design argument by questioning the analogy between the world and a machine?", "David Hume", [
        ("Anselm", "He gave the ontological argument."), ("William Paley", "He defended the design argument."), ("John Henry Newman", "He argued from conscience.")],
      "Hume's Dialogues raised several objections.", T_ARG, "Recall", "A Scottish philosopher."),
]
assert len(P1) == 50, len(P1)
SETS.append(practice_set(module=MX, topic="Paper 1", title="Paper 1 mock exam A", lesson="rsl2-exam-paper-1",
                         mock=True, time_limit_minutes=90, questions=build(P1, 213)))



# ================================================================== Paper 2 practice paper A (25 parts)
P2 = [
    # Question 1: The Exodus (essay: 'Explain why the Exodus is central to the religion of Israel')
    K("Question 1 is the essay 'Explain why the Exodus is central to the religion of Israel.' (a) Which opening sentence best answers the question?", "The Exodus is central because it is the saving act by which Yahweh made Israel his people, and later worship and law remember it", [
        ("The Exodus is the story of how the Hebrews left Egypt after the ten plagues", "This begins a narration and does not answer 'why central'."), ("The Exodus happened in Egypt a long time ago", "It states a fact without any explanation."), ("Moses was a great leader of Israel", "It is true but does not answer the question.")],
      "A good opening sentence is a thesis that answers the question.", T_EXO, "Reasoning", "Which sentence says why?"),
    K("Question 1 (b) Which point should an essay on this question include to show the centrality of the Exodus?", "The Passover festival is kept each year to remember the deliverance", [
        ("The names of the Egyptian taskmasters", "No names are given that can support the centrality."), ("The exact size of the pyramids", "This is not related to the question."), ("The length of Moses' beard", "This is irrelevant.")],
      "Festival memory is evidence of centrality.", T_EXO, "Application", "Think of a yearly act of memory."),
    K("Question 1 (c) A candidate adds that scholars disagree about the date of the Exodus (about 1446 BC or in the thirteenth century BC). This is useful mainly as", "evaluation: it shows awareness of scholarly debate", [
        ("narration: it tells more of the story", "It adds debate, not narrative."), ("a conclusion", "It would belong in the body of the essay."), ("a mistake, because dates should be avoided", "Dates are useful when used correctly.")],
      "Evaluation shows the limits or debates around a point.", T_EXO, "Evaluation", "What kind of paragraph discusses debate?"),
    # Question 2: judges to monarchy
    K("Question 2 asks about 'the religious and political roles of the judges'. Which plan fits the demand best?", "Religious role (calling the people back to Yahweh), political and military role (delivering the tribes), named leaders, and limits", [
        ("A story of Samson from birth to death", "It covers one judge only and no roles."), ("A list of the twelve tribes", "It does not answer the question."), ("A comparison of Saul and David", "It is about a later period.")],
      "A plan should match the two roles asked for.", T_JUD, "Application", "Underline 'religious and political roles'."),
    K("Question 2 (b) Which judge is correctly matched with an enemy?", "Gideon with the Midianites", [
        ("Samson with the Ammonites", "Samson fought the Philistines; Jephthah fought the Ammonites."), ("Deborah with the Philistines", "Deborah's story involves the Canaanite commander Sisera."), ("Ehud with the Midianites", "Ehud killed Eglon, king of Moab.")],
      "Learn name, enemy and a detail for each judge.", T_JUD, "Recall", "Gideon had three hundred men."),
    K("Question 2 (c) Which point best links the period of the judges to the coming of the monarchy?", "The weakness and local nature of the leadership of the judges led the people to ask for a king", [
        ("The judges were all kings", "They were not kings."), ("The monarchy was established before the judges", "The monarchy came after the judges."), ("The judges ruled with the help of Rome", "Rome did not exist as a power in that period.")],
      "A transition question needs a link.", T_JUD, "Reasoning", "Think of why Israel wanted a king."),
    # Question 3: Saul
    K("Question 3 asks you to 'assess Saul as king of Israel'. Which approach is best?", "Give his achievements and failures, then a reasoned judgement", [
        ("Describe only his rejection by Yahweh", "This gives one side only."), ("Describe only his victories", "This gives one side only."), ("Retell his whole life with no evaluation", "This is narration.")],
      "Assess requires balance and judgement.", T_SAUL, "Evaluation", "What does 'assess' demand?"),
    K("Question 3 (b) Which pair of incidents is usually given as the reasons for Saul's rejection?", "The unlawful offering at Gilgal and the failure to carry out the ban against Amalek", [
        ("The census and the affair with Bathsheba", "These are linked with David."), ("The Temple building and the forced labour", "These are linked with Solomon."), ("The golden calf and the plagues", "These are not about Saul.")],
      "1 Samuel 13 and 15.", T_SAUL, "Recall", "Both involve disobedience to Samuel's instructions."),
    # Question 4: David
    K("Question 4 is 'David was a flawed king, yet a man after God's heart. Discuss.' Which plan answers both parts?", "His sins, his strengths and why he is still honoured, and a judgement", [
        ("Only his sins with Bathsheba and Uriah", "This answers one part."), ("Only the story of Goliath", "This is not the focus."), ("Only the Psalms", "This does not give a balanced answer.")],
      "The Board's report notes that both sides were expected.", T_DAV, "Reasoning", "Check both halves of the title."),
    K("Question 4 (b) Which evidence best shows that David was a man after God's heart?", "He repented when Nathan confronted him", [
        ("He never sinned", "The tradition records his sins."), ("He built the Temple himself", "Solomon built the Temple."), ("He was the first king", "Saul was the first king.")],
      "Repentance is the key to the tradition.", T_DAV, "Reasoning", "Think of 2 Samuel 12."),
    K("Question 4 (c) Which statement about the Davidic covenant should be included in a strong answer?", "God promised David a house that would last, and this fed later messianic hope", [
        ("God promised David the land of Egypt", "This is not in 2 Samuel 7."), ("God made David high priest", "David was a king, not high priest."), ("God cancelled the promise to Abraham", "The covenants are not presented as cancelling each other.")],
      "2 Samuel 7 is the key text.", T_DAV, "Concept", "Think of a dynasty."),
    # Question 5: covenants
    K("Question 5 asks you to 'compare the covenants with Abraham and with Moses'. Which is a correct contrast?", "The Abrahamic covenant stresses promise, while the Sinai covenant stresses law and obedience", [
        ("The Abrahamic covenant is a law code, while Sinai is a promise", "This reverses them."), ("Only Abraham's covenant has a sign", "Sinai has signs, such as the Sabbath in Exodus 31."), ("Both are the same covenant with no differences", "A comparison needs differences as well as similarities.")],
      "A standard point of comparison.", T_PAT, "Concept", "Think of 'promise' and 'law'."),
    K("Question 5 (b) Which is a similarity between the two covenants?", "Both rest on God's initiative and call for a response of faithfulness", [
        ("Both were made at Mount Sinai", "Abraham's covenant was made long before Sinai."), ("Both require circumcision", "Circumcision belongs to Abraham's covenant."), ("Both were made with Solomon", "They were not made with Solomon.")],
      "Both stress that God acts first.", T_PAT, "Concept", "Think of who begins the covenant."),
    K("Question 5 (c) Which comparison supports the view that the Sinai covenant has the form of an ancient treaty?", "Preamble, historical prologue, laws, blessings and curses", [
        ("A list of kings and dates", "These are not the treaty parts."), ("A genealogy only", "A genealogy is not a treaty."), ("A story with no laws", "A treaty includes terms.")],
      "The pattern is like Hittite suzerainty treaties.", T_MOS, "Concept", "Treaties have terms and sanctions."),
    K("Question 5 (d) Which evaluation point is usually made about the treaty-form theory?", "It is helpful, but the parallels may be general, and the dating of the texts is debated", [
        ("It is accepted by all scholars without question", "It is debated."), ("It proves that Moses wrote the whole Pentateuch", "It does not prove this."), ("It has been shown to be entirely false", "Many scholars find it helpful.")],
      "Evaluate by giving strengths and limits.", T_MOS, "Evaluation", "Check the word 'debated'."),
    # Question 6: Temple and festivals
    K("Question 6 asks for 'the importance of the Day of Atonement in Israel'. Which approach is best?", "State the meaning (cleansing the sanctuary and people), the role of the high priest and the scapegoat, and its place in worship", [
        ("Describe only the clothing of the priest", "This is too narrow."), ("Retell the festival without explaining its meaning", "This is narration."), ("Compare it with the Sabbath only", "This does not address the question.")],
      "Importance requires meaning and function.", T_TEM, "Application", "Which approach states meaning?"),
    K("Question 6 (b) Which festival remembers the years in the wilderness when the people lived in tents?", "Tabernacles (Booths)", [
        ("Passover", "This remembers the deliverance from Egypt."), ("Weeks (Pentecost)", "This celebrates the wheat harvest."), ("Day of Atonement", "This is a day of fasting and cleansing.")],
      "Leviticus 23.", T_TEM, "Recall", "Think of 'booths'."),
    # Question 7: other modules (planning and key arguments)
    K("Question 7 (a) An essay asks 'Examine the use of the title Son of Man in the Gospels.' The best plan includes", "the background in Daniel 7, the three groups of sayings, and a debate about their origin", [
        ("only the birth of Jesus", "The birth stories do not use the title."), ("only Paul's letters", "The question is about the Gospels."), ("only the Prologue of John", "The Prologue uses Logos.")],
      "A plan should name the groups and the debate.", T_CHR, "Application", "Think of the three classes of sayings."),
    K("Question 7 (b) An essay on the Kingdom of God should include which scholarly contrast?", "Schweitzer's future Kingdom and Dodd's realised Kingdom", [
        ("Wrede and Bultmann on the messianic secret", "This is about Mark's secret."), ("Julicher and Jeremias on allegory", "This is about parables."), ("Noth and Wellhausen on the sources", "This is about the Old Testament.")],
      "These two positions frame the debate.", T_KING, "Concept", "Think of present and future."),
    K("Question 7 (c) In an essay on the parables, why should the retelling of the Good Samaritan be short?", "Because the question asks for meaning, such as love and discipleship", [
        ("Because the parable is not in Luke", "It is in Luke 10."), ("Because examiners dislike parables", "This is not the reason."), ("Because the parable has no meaning", "It has an important meaning.")],
      "The report notes that narration displaced explanation.", T_PAR, "Reasoning", "Think of what is asked."),
    K("Question 7 (d) For an essay on the Gospel of John, which pair of references should be used to show the purpose and a key theme?", "John 20:31 for the purpose, and the Prologue for light and life", [
        ("Mark 1:15 and Luke 10", "These are in other Gospels."), ("Genesis 1 and Exodus 20", "These are in the Old Testament."), ("Acts 2 and 1 Corinthians 15", "These are not in John.")],
      "Name the passage with the point.", T_JOHN, "Application", "Which verse states the purpose?"),
    K("Question 7 (e) In an essay on the passion narratives, which point shows Luke's particular emphasis?", "Pilate declares Jesus innocent three times, and the centurion calls him righteous", [
        ("The Great Commission on a mountain in Galilee", "This is Matthew."), ("The cry of abandonment as the last word", "This is Mark's emphasis."), ("Pilate washes his hands", "This is Matthew's emphasis.")],
      "Luke 23:4, 14, 22 and 47.", T_PASS, "Recall", "Think of innocence."),
    K("Question 7 (f) In an essay on the spread of Christianity, which of these is a political or social factor rather than a purely religious one?", "The Roman roads and the Pax Romana", [
        ("The preaching of the apostles", "This is a religious cause."), ("The courage of martyrs", "This is a religious and moral cause."), ("The Christian teaching about eternal life", "This is a religious cause.")],
      "Good answers combine several kinds of cause.", T_SPREAD, "Concept", "Which factor is about travel and order?"),
    K("Question 7 (g) In an essay on the Council of Nicaea, which pair of terms must be explained?", "Arianism and homoousios", [
        ("Theotokos and Monophysitism", "These belong to the later disputes."), ("Docetism and Montanism", "These belong to earlier movements."), ("Pax Romana and Diaspora", "These belong to the spread of Christianity.")],
      "They name the question and the answer.", T_COUN, "Recall", "Think of the dispute and the creed's key word."),
    K("Question 7 (h) In an essay on the cosmological argument, which pairing is the strongest for evaluation?", "Aquinas's argument and Russell's objection about the fallacy of composition", [
        ("Aquinas's argument and Paley's watch", "Paley's watch is a design argument."), ("Anselm's argument and Gaunilo's island", "These belong to the ontological argument."), ("Kant's moral argument and Freud", "These belong to the moral argument.")],
      "Pair an argument with an objection to the same argument.", T_ARG, "Evaluation", "Match argument and objection."),
]
assert len(P2) == 25, len(P2)
SETS.append(practice_set(module=MX, topic="Paper 2", title="Paper 2 practice paper A", lesson="rsl2-exam-paper-2",
                         mock=True, time_limit_minutes=150, questions=build(P2, 214)))

