"""Practice sets for A Level Religious Studies (0785), Upper Sixth: New Testament: Ethics & Eschatology (3 sets), Alternative Track: Church History,
Ethics or Islam (5 sets) and Examination (3 sets), one set per lesson (11 sets), plus 'Paper 1 mock exam A' (50 multiple-choice questions across all
five Upper Sixth modules in proportion to their topic counts) and 'Paper 2 practice paper A' (25 auto-markable parts on planning, key arguments and
facts; essays cannot be auto-marked). Descriptive and scholarly; scripture is paraphrased; Cameroon church history is limited to well-established
outlines. Facts about the papers come from the Board's 2023 report (paraphrased). Scenarios are invented for practice.
"""

import random

from .dsl import *  # noqa: F403

COURSE = ("religious-studies", "upper-sixth")

M_PRO = "Old Testament: Prophecy in Israel & the Eighth-Century Prophets"
M_EXI = "Old Testament: Exilic Prophecy & Wisdom Literature"
M_APO = "New Testament: Apostolic History & the Pauline Epistles"
M_ETH = "New Testament: Ethics & Eschatology"
M_ALT = "Alternative Track: Church History, Ethics or Islam"
M_EXAM = "Examination"

# topic titles (exact)
T_HEB = "Hebrew prophecy"
T_ELI = "Elijah"
T_AMO = "Amos"
T_HOS = "Hosea"
T_ISA = "Isaiah of Jerusalem"
T_JER = "Jeremiah"
T_EZE = "Ezekiel"
T_DEU = "Deutero-Isaiah and the Suffering Servant"
T_JOB = "Job and the problem of theodicy"
T_ACT = "The Acts of the Apostles"
T_MIS = "Paul's missionary strategy"
T_COR = "1 Corinthians"
T_GAL = "Galatians and Romans"
T_SER = "The ethics of the Sermon on the Mount"
T_STA = "The Christian and the state, wealth and marriage"
T_ESC = "Eschatology and the Parousia"
T_REF = "The Reformation"
T_CAM = "Christianity in Cameroon"
T_EVL = "The problem of evil and religious language"
T_BIO = "Bioethics"
T_ISL = "Islamic theology and jurisprudence"


def K(prompt, right, wrongs, step, concept, skill, hint, feedback="", passage=""):
    """Question spec: the right option first, then three (text, why) wrong options. Positions are assigned by build()."""
    assert len(wrongs) == 3, prompt
    assert len(concept) <= 80, concept
    return {"prompt": (passage + "\n\n" + prompt) if passage else prompt, "right": right, "wrongs": wrongs,
            "step": step, "concept": concept, "skill": skill, "hint": hint, "feedback": feedback}


def N(prompt, answer, step, concept, skill, hint, unit="", tol=0):
    assert len(concept) <= 80, concept
    return {"num": True, "prompt": prompt, "answer": answer, "step": step, "concept": concept, "skill": skill,
            "hint": hint, "unit": unit, "tol": tol}


def build(specs, seed):
    mc = [i for i, s in enumerate(specs) if not s.get("num")]
    pos = {}
    cyc = [j % 4 for j in range(len(mc))]
    random.Random(seed).shuffle(cyc)
    for i, p in zip(mc, cyc):
        pos[i] = p
    out = []
    for i, sp in enumerate(specs):
        steps = [S("Reasoning", text=s) for s in ([sp["step"]] if isinstance(sp["step"], str) else sp["step"])]
        if sp.get("num"):
            out.append(NUM(sp["prompt"], sp["answer"], steps, tolerance=sp["tol"], unit=sp["unit"], concept=sp["concept"],
                           skill=sp["skill"], hint=sp["hint"]))
            continue
        opts = [C(w, why=y) for w, y in sp["wrongs"]]
        opts.insert(pos[i], C(sp["right"], correct=True))
        out.append(MC(sp["prompt"], opts, steps, concept=sp["concept"], skill=sp["skill"], hint=sp["hint"], feedback=sp["feedback"]))
    return out


def SET(module, topic, title, lesson, specs, seed, **kw):
    assert len(specs) == 8, title
    SETS.append(practice_set(module=module, topic=topic, title=title, lesson=lesson, questions=build(specs, seed), **kw))


SETS = []

# ================================================================== 1. Sermon on the Mount
SET(M_ETH, T_SER, "The Sermon on the Mount: Beatitudes, antitheses and interpretations", "rsu2-sermon-on-the-mount", [
    N("Matthew's Sermon on the Mount begins in chapter number:", 5, "The Sermon fills Matthew chapters 5 to 7, starting in chapter 5.", "Outline of the Sermon", "Recall", "It is the first of three chapters (5 to 7)."),
    K("What is a beatitude?", "A statement of blessing beginning 'Blessed are ...'", [
        ("A command to fast", "Fasting is taught in Matthew 6, but a beatitude is a statement of blessing."),
        ("A prayer that closes the Sermon", "The Lord's Prayer is in Matthew 6; beatitudes open the Sermon."),
        ("A parable about builders", "The builders at the end of the Sermon are a parable, not a beatitude.")],
      "The word comes from a Latin word for 'blessed'; each beatitude names a group that God favours.", "Beatitudes", "Recall", "Think of the words that begin each one."),
    K("Which is the pattern of the antitheses in Matthew 5:21-48?", "'You have heard that it was said ... but I say to you ...'", [
        ("'Woe to you, scribes and Pharisees'", "This is a pattern of condemnation in Matthew 23, not in the antitheses."),
        ("'Truly I say to you, the kingdom has come near'", "This is a proclamation, not the pattern of contrast."),
        ("'Go and make disciples'", "This is the closing command of the Gospel.")],
      "Each of the six contrasts quotes an old teaching and then states Jesus' deeper meaning.", "Antitheses", "Recall", "Think of the contrast between the old and the new teaching."),
    K("In the antithesis on anger, what does Jesus do with the commandment 'You shall not murder'?", "He traces it back to anger and contempt in the heart", [
        ("He abolishes it", "Jesus says in 5:17 that he has not come to abolish the Law."),
        ("He limits it to the courts", "He widens it beyond the act that courts judge."),
        ("He makes it apply only to disciples", "The teaching concerns all who hear, not a narrow group.")],
      "The antitheses move from the outward deed to the inner attitude.", "Antitheses", "Concept", "Ask what lies behind a murder.",),
    K("Who is linked with the 'interim ethic' reading of the Sermon?", "Albert Schweitzer", [
        ("C. H. Dodd", "Dodd is linked with realized eschatology."),
        ("Thomas Aquinas", "Aquinas is linked with natural law and analogy, not the interim ethic."),
        ("Joseph Fletcher", "Fletcher is linked with situation ethics.")],
      "Schweitzer argued that Jesus expected the kingdom soon, so the demands fit a short crisis period.", "Interpretations of the Sermon", "Recall", "He is also linked with futuristic eschatology."),
    K("A student says that a believer who never strikes anyone but is full of hatred has obeyed the Sermon. Which teaching answers this?", "The antitheses, which treat anger and contempt as serious", [
        ("The Beatitudes, which only list rewards", "The Beatitudes name the blessed; the antithesis on anger answers the claim directly."),
        ("The Lord's Prayer, which concerns bread", "The prayer concerns relations with God and forgiveness but not this case directly."),
        ("The two ways, which concern a gate", "The two ways teach a choice, not a ruling on anger.")],
      "The antithesis shows that the root of murder is the hostile heart, so refraining from violence is not enough.", "Righteousness of the heart", "Application", "Which part of the Sermon contrasts act and attitude?"),
    K("Which objection is made against the 'impossible ideal' interpretation?", "The Sermon ends by telling hearers to do the words, like the builder on rock", [
        ("The Sermon was written by Luke", "Matthew contains the Sermon; Luke has a shorter parallel."),
        ("The Sermon has no demands", "The Sermon contains many demands."),
        ("The Sermon was spoken to the priests only", "It is addressed to disciples with crowds listening.")],
      "A reading that says the commands are impossible clashes with the call to put them into practice.", "Interpretations of the Sermon", "Reasoning", "Look at how the Sermon ends."),
    K("Which statement is the best evaluation of the kingdom ethic interpretation?", "It explains the demands as a way of life made possible by God's rule, but it may seem vague about practice", [
        ("It proves that the Sermon is only for monks", "That is the counsels-of-perfection view, which is a different reading."),
        ("It shows that the Sermon expired after one generation", "That is the interim view, which is a different reading."),
        ("It shows that Jesus rejected the Law completely", "Jesus says he came to fulfil it.")],
      "The kingdom ethic joins demand and enabling, but critics say that it can be hard to apply exactly.", "Interpretations of the Sermon", "Reasoning", "Look for an option that gives both a strength and a limit."),
], 301)

# ================================================================== 2. State, wealth, marriage
SET(M_ETH, T_STA, "The Christian and the state, wealth and marriage", "rsu2-state-wealth-marriage", [
    K("Which text tells believers to be subject to the governing authorities?", "Romans 13:1-7", [
        ("Acts 5:29", "This text says to obey God rather than people."),
        ("Revelation 13", "This chapter describes a beast that demands worship."),
        ("Mark 10:2-12", "This is the teaching on divorce.")],
      "Paul in Romans 13 describes the authorities as under God's order and calls for tax and respect.", "Christian and the state", "Recall", "It is in a letter to Rome."),
    K("What did Peter and the apostles say to the council in Acts 5:29?", "They must obey God rather than people", [
        ("Give to Caesar what is Caesar's", "That is Jesus' answer in Mark 12."),
        ("Honour the emperor", "That is from 1 Peter 2."),
        ("Pay taxes to all", "This is the teaching of Romans 13.")],
      "The apostles refused the order to stop preaching.", "Christian and the state", "Recall", "The council had forbidden preaching."),
    K("Why do scholars find a tension between Romans 13 and Revelation 13?", "One calls for subjection to authority, the other pictures a power that demands worship", [
        ("Both were written by the same author in one year", "They have different authors; the tension is in their attitudes."),
        ("Romans 13 forbids all taxes", "It teaches paying taxes."),
        ("Revelation 13 is about marriage", "It is about a beast and false worship.")],
      "Romans gives a positive picture of the state in its role, Revelation a picture of a state that claims what belongs to God.", "Christian and the state", "Reasoning", "Compare the two attitudes to authority."),
    K("What does 1 Timothy 6:10 say?", "The love of money is a root of all kinds of evil", [
        ("Money is evil in itself", "The text speaks of loving money, not of money as such."),
        ("The poor are blessed because they are poor", "That is not the point of this verse."),
        ("Tithing is a commandment for all", "The verse does not mention tithing.")],
      "The warning is about desire and attachment.", "Wealth", "Recall", "Look at what is loved."),
    K("In Mark 10:17-31, why did the rich man go away sad?", "He could not give up his many possessions", [
        ("He had not kept any commandments", "He said that he had kept them from youth."),
        ("Jesus refused to speak with him", "Jesus looked at him and spoke to him."),
        ("He feared the Roman tax", "The story is about his wealth, not tax.")],
      "Jesus asked him to sell and give to the poor, and the man was attached to his wealth.", "Wealth", "Concept", "Look at the instruction Jesus gave him."),
    K("Which reason does Jesus give in Mark 10 for his teaching on divorce?", "God's purpose in creation: the two become one flesh", [
        ("Moses commanded divorce as an ideal", "Jesus says Moses allowed it because of hardness of heart."),
        ("Roman law forbade divorce", "Jesus argues from creation, not from Roman law."),
        ("Marriage is only a temporary contract", "He teaches that what God has joined must not be separated.")],
      "Jesus points back to creation rather than to Moses' concession.", "Marriage and divorce", "Concept", "He quotes from Genesis."),
    K("A student writes a general essay about modern marriage problems in answer to a question on Paul's teaching in 1 Corinthians 7. What is the main weakness?", "It does not link Paul's words to the Corinthian situation and questions", [
        ("It mentions marriage", "Marriage is the topic of the question."),
        ("It is too short in the introduction", "The main issue is the missing link to the situation in Corinth."),
        ("It quotes the Bible", "Quoting is good if it is applied to the context.")],
      "The Board's report says that candidates wrote about marriage in general and did not link Paul's teaching to the church in Corinth.", "Marriage and divorce", "Application", "What does the report say about this question?"),
    K("Which comment best evaluates the claim that the New Testament demands obedience to the state in every case?", "It is too strong, because Acts 5:29 and Revelation 13 set limits", [
        ("It is correct, because Romans 13 is the only text on the subject", "Other texts such as Acts 5:29 and Mark 12 also speak to the subject."),
        ("It is correct, because Jesus paid no taxes", "Jesus' answer about taxes in Mark 12 does not mean that obedience is without limit."),
        ("It is false, because the New Testament never mentions the state", "It does, for example in Mark 12 and Romans 13.")],
      "The New Testament shows respect for the state and also limits on its claims.", "Christian and the state", "Reasoning", "Think of texts on both sides."),
], 302)

# ================================================================== 3. Eschatology
SET(M_ETH, T_ESC, "Eschatology and the Parousia", "rsu2-eschatology-parousia", [
    K("What does the Greek word 'Parousia' mean in Christian use?", "The coming or arrival of Christ at the end of the age", [
        ("The baptism of Jesus", "The word concerns his future coming."),
        ("The last meal of Jesus", "That is the Last Supper."),
        ("The resurrection of Lazarus", "Lazarus' story is in John 11.")],
      "Parousia is Greek for presence or arrival, applied to the return of Christ.", "Parousia", "Recall", "It means arrival."),
    K("Which scholar is linked with realized eschatology?", "C. H. Dodd", [
        ("Albert Schweitzer", "Schweitzer argued for a mainly future kingdom."),
        ("Johannes Weiss", "Weiss is also linked with the futuristic view."),
        ("Ignatius of Loyola", "Ignatius belongs to the Counter-Reformation.")],
      "Dodd argued that the kingdom came in the ministry of Jesus.", "Realized eschatology", "Recall", "Think of 'realized' as 'already happened'."),
    K("Which passage warns that no one knows the day or hour of the end?", "Mark 13", [
        ("Matthew 5", "This chapter opens the Sermon on the Mount."),
        ("Luke 2", "This chapter is about the birth of Jesus."),
        ("Romans 1", "This chapter opens Paul's letter and is not about the day or hour.")],
      "Mark 13:32 says that only the Father knows.", "Parousia", "Recall", "It is called the little apocalypse."),
    K("Why did Paul write about the dead in 1 Thessalonians 4?", "Some believers feared that those who had died would miss Christ's coming", [
        ("He wanted to give the date of the Parousia", "He said it will come like a thief."),
        ("He wanted to deny that Christ would return", "He teaches that Christ will return."),
        ("He wanted to answer Greek philosophers on the soul", "The text deals with worry in the church.")],
      "Paul comforted the church with the hope that the dead in Christ would rise first.", "Parousia", "Concept", "Read it as a pastoral letter."),
    K("Which saying best supports a present, realized kingdom?", "'The kingdom of God has come near' (Mark 1:15)", [
        ("'You do not know the day or the hour'", "This speaks of an unknown future time."),
        ("'They will see the Son of Man coming'", "This points to a future coming."),
        ("'Your kingdom come'", "This is a prayer for a coming that is not yet complete.")],
      "Mark 1:15 announces that the kingdom is at hand in the ministry of Jesus.", "Realized eschatology", "Application", "Which saying says that it is near now?"),
    K("The 'already and not yet' view says that the kingdom is", "begun in Jesus but completed only at the end", [
        ("entirely in the future", "That is the futuristic view."),
        ("entirely in the past", "That is closer to a purely realized view."),
        ("only an idea in the mind", "This is not the view of those who use the phrase.")],
      "It joins the two groups of sayings in the Gospels.", "Inaugurated eschatology", "Concept", "It holds both sides."),
    K("Which is a criticism of Dodd's realized eschatology?", "It does not do justice to sayings that speak of a future coming", [
        ("It denies that the kingdom is spoken of at all", "Dodd stressed the kingdom."),
        ("It places the kingdom after the year 2000", "Dodd's view was that it had already come."),
        ("It rejects the resurrection", "Dodd did not reject the resurrection.")],
      "Critics say that Dodd explained away Mark 13 and similar texts.", "Realized eschatology", "Reasoning", "Think of the future sayings."),
    K("How does 2 Peter 3 respond to those who ask where the promised coming is?", "It says the Lord is patient and gives time for repentance", [
        ("It says the coming happened already in the past", "It still looks to the future."),
        ("It gives a firm date", "No date is given."),
        ("It says the question must not be asked", "It answers the question.")],
      "The writer explains that God's patience explains the delay.", "Delay of the Parousia", "Concept", "Find the reason for the delay."),
], 303)

# ================================================================== 4. Reformation
SET(M_ALT, T_REF, "The Reformation", "rsu2-the-reformation", [
    N("In which year did Luther write the Ninety-five Theses (the traditional date)?", 1517, "The theses are traditionally dated to 31 October 1517.", "Luther", "Recall", "It was early in the sixteenth century."),
    K("What were indulgences?", "Certificates reducing the punishment for sin, sold by the church", [
        ("Prayers said by Luther", "Indulgences were not prayers composed by Luther."),
        ("Taxes paid to the English king", "They were linked with the church's practice."),
        ("Books that explained the Bible", "They were not books of explanation.")],
      "Luther's Theses attacked the sale of indulgences.", "Causes of the Reformation", "Recall", "They began the controversy."),
    K("Which teaching is at the centre of Luther's thought?", "Justification by faith", [
        ("Predestination as the first article", "That is more strongly linked with Calvin."),
        ("The pope's supreme authority", "Luther rejected it."),
        ("Salvation by many pilgrimages", "Luther rejected salvation by works.")],
      "Luther read Paul as teaching that a person is made right with God by faith, through grace.", "Luther", "Concept", "Connect it to Romans."),
    K("What did Zwingli teach about the Lord's Supper?", "The bread and wine are signs that recall Christ's sacrifice", [
        ("Christ's body is physically present", "That is closer to Luther's view."),
        ("The bread becomes Christ's body in substance", "That is the Catholic teaching."),
        ("The Supper should be abolished", "Zwingli kept the Supper.")],
      "Zwingli saw the Supper as a memorial.", "Zwingli", "Concept", "Think of remembrance."),
    K("Which book did Calvin write?", "Institutes of the Christian Religion", [
        ("The Ninety-five Theses", "That is Luther's work."),
        ("The Book of Common Prayer", "This is an English church book, first issued in 1549."),
        ("The Decrees of Trent", "These were decrees of a council.")],
      "Calvin published the first edition in 1536.", "Calvin", "Recall", "It is a title with 'Institutes'."),
    K("What did the Act of Supremacy (1534) establish?", "The English king as head of the Church of England", [
        ("The Council of Trent", "Trent was a Catholic council from 1545."),
        ("The authority of the pope in England", "It removed the pope's authority."),
        ("The first English Bible", "It dealt with the headship of the church.")],
      "Parliament recognised Henry VIII as head of the Church of England.", "English Reformation", "Recall", "Think of the king's role."),
    K("Which statement best describes the Council of Trent?", "It defended Catholic teaching and reformed clergy training and discipline", [
        ("It accepted justification by faith alone", "It rejected that Protestant formula, stressing both faith and works."),
        ("It abolished the sacraments", "It confirmed seven sacraments."),
        ("It was held in England under Elizabeth I", "It was a Catholic council held in Trent in Italy.")],
      "Trent met from 1545 to 1563 and clarified doctrine and ordered reforms such as seminaries.", "Counter-Reformation", "Concept", "Think of the Catholic response."),
    K("Which comment best evaluates the claim that the Reformation was caused only by Luther?", "It is too narrow, because abuses, printing, new learning and politics also played a part", [
        ("It is correct, since nothing else changed", "Several causes are given by historians."),
        ("It is correct, because Luther was the first and only reformer", "Zwingli and Calvin, among others, also reformed."),
        ("It is wrong, because the Reformation began in the nineteenth century", "It began in the sixteenth century.")],
      "Historians give several causes, including those listed.", "Causes of the Reformation", "Reasoning", "Look for several causes."),
], 304)

# ================================================================== 5. Christianity in Cameroon
SET(M_ALT, T_CAM, "Christianity in Cameroon", "rsu2-christianity-in-cameroon", [
    K("Which Baptist missionary settled at Douala in 1845 (check your textbook for the date your course uses)?", "Alfred Saker", [
        ("Joseph Merrick", "Merrick began work at Bimbia in 1843."),
        ("Martin Luther", "Luther was a sixteenth-century German reformer."),
        ("Ignatius of Loyola", "Ignatius founded the Jesuits in the sixteenth century.")],
      "Saker worked at Douala, translated parts of the Bible into Duala and founded Victoria in 1858.", "Baptist missions", "Recall", "He was English and Baptist."),
    K("Which settlement did Saker found in 1858 for freed slaves and converts?", "Victoria (now Limbe)", [
        ("Buea", "Buea became a colonial town later."),
        ("Yaounde", "Yaounde is a capital city founded later."),
        ("Bamenda", "Bamenda is a town in the grassfields.")],
      "Victoria, now Limbe, was founded on the coast.", "Baptist missions", "Recall", "It is a coastal town."),
    K("Which mission took over the Baptist work under German rule in 1886?", "The Basel Mission", [
        ("The Paris Evangelical Mission", "It took over parts of the work after 1916 in the French zone."),
        ("The Mill Hill Missionaries", "They are a Catholic society that worked in the British zone from the 1920s."),
        ("The Salvation Army", "It is not the mission named in the usual outline.")],
      "Germany declared a protectorate in 1884 and the Basel Mission, a Swiss Protestant mission, took over.", "Basel Mission", "Recall", "Think of a Swiss mission."),
    K("Which Catholic group began work in German Kamerun in 1890?", "The Pallottine Fathers", [
        ("The Spiritans", "They expanded after the First World War in the French zone."),
        ("The Mill Hill Missionaries", "They came to the British zone later."),
        ("The Jesuits of Trent", "The Jesuits are not the group named in this outline.")],
      "The Pallottines came from Germany (check your textbook for details).", "Catholic missions", "Recall", "They were German."),
    K("What happened to the German missions after the First World War?", "German missionaries were removed and other missions took over", [
        ("They were given more land", "Germany lost its colonies."),
        ("They became the national church", "They were replaced in the territory."),
        ("They left no schools", "Their schools and churches continued under other missions.")],
      "Britain and France divided the territory and other missions took over.", "Missions after 1916", "Concept", "Think of Germany's defeat."),
    K("Which is a contribution of the missions to Cameroonian society?", "Schools, hospitals and writing in local languages", [
        ("The creation of the national constitution", "That was a political matter."),
        ("The building of all railways", "Railways were mostly colonial projects."),
        ("The abolition of all traditional beliefs", "Traditional beliefs continued.")],
      "Missions set up schools and health centres, and wrote languages such as Duala.", "Contributions of missions", "Concept", "Think of education and health."),
    K("Which statement is the best evaluation of the link between missions and colonial rule?", "It was mixed: some missions helped colonial aims, and others educated Africans who later led independence", [
        ("Missions were always opposed to colonial rule", "Some cooperated with the authorities."),
        ("Missions were always agents of colonial rule", "Some missionaries criticised abuses."),
        ("There was no link at all", "Their work took place in the colonial setting.")],
      "A good essay shows both sides.", "Missions and colonial rule", "Reasoning", "Look for a balanced option."),
    K("Why should a student write 'check your textbook' next to some mission dates?", "Dates and details differ between books, and only well-established facts are safe", [
        ("Because missions did not exist", "They did exist."),
        ("Because the Board forbids dates", "The point is accuracy."),
        ("Because all dates are the same", "Books differ in details.")],
      "Accuracy depends on using the dates your course uses.", "Using sources", "Application", "What is the lesson's advice about dates?"),
], 305)

# ================================================================== 6. Evil and religious language
SET(M_ALT, T_EVL, "The problem of evil and religious language", "rsu2-evil-and-religious-language", [
    K("What is natural evil?", "Suffering with natural causes such as earthquakes and disease", [
        ("Suffering caused by human choices", "That is moral evil."),
        ("A kind of good", "Natural evil is a kind of suffering."),
        ("An illusion", "The problem of evil takes suffering as real.")],
      "Natural evil is suffering that does not come from human choice.", "Moral and natural evil", "Recall", "Think of a flood."),
    K("Mackie's inconsistent triad claims that these three cannot all be true: an all-powerful God, an all-good God and", "the existence of evil", [
        ("the existence of angels", "Angels do not appear in the triad."),
        ("the existence of free will", "Free will is used in the free-will defence, not the triad."),
        ("the existence of prayer", "Prayer is not in the triad.")],
      "Evil exists is the third claim.", "Inconsistent triad", "Recall", "Look at the figure in the lesson."),
    K("Augustine said that evil is", "a privation, a lack of good", [
        ("a created substance", "He denied this."),
        ("an eternal rival to God", "This is a dualist idea he rejected."),
        ("a necessary part of God", "He did not teach this.")],
      "Evil is like darkness, an absence of light.", "Augustinian theodicy", "Recall", "Think of a lack."),
    K("Which theodicy is linked with Irenaeus and John Hick?", "Soul-making: suffering helps humans to grow", [
        ("The Fall of humanity as the sole cause of all suffering", "That is the Augustinian view."),
        ("Evil is an illusion", "This is not the soul-making view."),
        ("God is not good", "It does not deny God's goodness.")],
      "Humans start immature and grow through freely chosen responses to challenge.", "Irenaean theodicy", "Concept", "Think of growth."),
    K("What does the free-will defence claim?", "A world with free beings who can choose wrongly may be better than one without them", [
        ("God cannot do anything", "The defence accepts God's power."),
        ("There is no evil", "It accepts that evil exists."),
        ("Natural disasters are caused by people", "It explains moral evil better than natural evil.")],
      "Plantinga used it to answer the logical problem.", "Free-will defence", "Concept", "Link to Plantinga."),
    K("What does Flew's falsification challenge say about religious claims?", "A claim that means something must rule something out, and religious claims seem to be qualified until nothing counts against them", [
        ("They are true by definition", "That is the status of mathematical statements."),
        ("They can be checked by a microscope", "Flew's challenge is that nothing seems to count against them."),
        ("They are always scientific", "Flew said that they lose meaning if nothing counts against them.")],
      "The parable of the gardener shows claims dying by qualifications.", "Falsification", "Concept", "Remember the parable of the gardener."),
    K("How did R. M. Hare reply to Flew?", "Religious beliefs are bliks: basic ways of seeing the world, not tested like scientific claims", [
        ("He said that religious claims are false", "Hare defended their significance."),
        ("He said that only science is meaningful", "That is the verification view."),
        ("He agreed with Flew completely", "He replied to Flew.")],
      "A blik shapes how a person lives and sees all evidence.", "Religious language", "Reasoning", "Think of a way of seeing."),
    K("Which statement about the verification principle is a fair criticism?", "The principle itself cannot be checked by observation", [
        ("It was never used by philosophers", "Ayer popularised it."),
        ("It proves God exists", "It was used to challenge religious language."),
        ("It was made by Aquinas", "Aquinas is linked with analogy.")],
      "A principle that says only checkable statements are meaningful fails its own test.", "Verification principle", "Reasoning", "Apply the principle to itself."),
], 306)

# ================================================================== 7. Bioethics
SET(M_ALT, T_BIO, "Bioethics", "rsu2-bioethics", [
    K("What is bioethics?", "The study of moral questions raised by biology and medicine", [
        ("The study of plants", "That is botany."),
        ("The history of hospitals", "It concerns moral questions, not history."),
        ("A branch of chemistry", "It is a branch of ethics.")],
      "Bioethics deals with life, health and medicine.", "Bioethics", "Recall", "Look at the word 'ethics'."),
    K("The sanctity of life principle says that", "human life is sacred and has special value", [
        ("quality of life is the only thing that matters", "That is a different principle."),
        ("a life is worth only what it earns", "That is not what sanctity means."),
        ("only adults have value", "Sanctity does not exclude any stage.")],
      "Many religious traditions teach that life is a gift from God.", "Sanctity of life", "Recall", "Think of life as sacred."),
    K("Which approach judges acts by the greatest happiness for the greatest number?", "Utilitarianism", [
        ("Natural law", "It starts from natural purposes."),
        ("Kantian ethics", "It starts from universal duties."),
        ("Divine command", "It starts from God's commands.")],
      "Bentham and Mill held that the right act brings the best total consequences.", "Ethical theories", "Recall", "Think of Bentham."),
    K("What does passive euthanasia mean?", "Allowing death by withholding or withdrawing treatment", [
        ("Giving a lethal injection", "That is active euthanasia."),
        ("Helping with a will", "It is unrelated."),
        ("Prolonging life at any cost", "That is the opposite.")],
      "Passive means not acting to prolong life.", "Euthanasia", "Concept", "Passive means not acting."),
    K("What does the doctrine of double effect allow, in natural law thought?", "An act with a good aim and a foreseen but unintended bad side effect, under conditions", [
        ("Any act if the result is good", "That is a consequentialist idea."),
        ("An act with a bad aim if the result is good", "The aim must be good."),
        ("Ignoring all side effects", "Side effects must be weighed.")],
      "For example, pain relief that may shorten life is allowed if the aim is relief.", "Natural law", "Concept", "Aim and side effect are different."),
    K("A patient who is competent refuses a treatment after being informed. Which of the four principles stresses respect for this choice?", "Autonomy", [
        ("Beneficence", "It is about doing good."),
        ("Justice", "It is about fair sharing."),
        ("Non-maleficence", "It is about avoiding harm.")],
      "Autonomy means respect for the patient's right to choose.", "Four principles", "Application", "Whose choice is it?"),
    K("Which statement is a fair description of Christian and Muslim teaching on euthanasia?", "Both traditions generally teach that life is a gift or trust from God, so deliberate killing is wrong", [
        ("Both teach that active euthanasia is a duty", "They generally oppose it."),
        ("Both have no teaching on the subject", "They have teaching."),
        ("Both teach that one religion is better", "The course does not rank religions.")],
      "The traditions generally agree on the principle, while details differ.", "Euthanasia", "Application", "Think of life as a gift."),
    K("Which criticism is made of situation ethics?", "It may allow almost anything and love is hard to measure", [
        ("It is too rigid", "It is accused of being too flexible."),
        ("It has never been used", "It was developed by Fletcher."),
        ("It is based on natural purposes", "That is natural law.")],
      "Critics say that it is too flexible and hard to apply.", "Situation ethics", "Reasoning", "Think of its flexibility."),
], 307)

# ================================================================== 8. Islamic theology and jurisprudence
SET(M_ALT, T_ISL, "Islamic theology and jurisprudence", "rsu2-islamic-theology-jurisprudence", [
    K("What is tawhid?", "The belief in the oneness of God", [
        ("The pilgrimage to Mecca", "That is Hajj."),
        ("The fast of Ramadan", "That is sawm."),
        ("A school of law", "Tawhid is a belief, not a school.")],
      "Tawhid means that God is one, with no partner.", "Tawhid", "Recall", "Think of 'one'."),
    K("What is kalam?", "Islamic theology that uses reasoning to explain and defend belief", [
        ("The call to prayer", "That is the adhan."),
        ("The collection of Hadith", "Hadith are reports of the Prophet."),
        ("A kind of fasting", "It is not a form of worship.")],
      "Kalam literally means speech.", "Kalam", "Recall", "It is theology."),
    K("Which school of kalam taught that the Quran is God's uncreated speech and that humans 'acquire' their acts?", "Ash'ari", [
        ("Mu'tazila", "They taught that the Quran was created."),
        ("Hanafi", "This is a school of law."),
        ("Shia Ja'fari", "This is a school of law.")],
      "The Ash'ari school became widely accepted among Sunni Muslims.", "Kalam", "Concept", "It is a school of kalam."),
    K("What is the difference between Sharia and fiqh?", "Sharia is God's way; fiqh is scholars' understanding of it", [
        ("They are the same", "They are distinguished."),
        ("Fiqh is the Quran; Sharia is the Hadith", "These are sources, not the definitions."),
        ("Sharia is a school of law; fiqh is a prayer", "This confuses the terms.")],
      "Fiqh is a human effort and can differ between schools.", "Sharia and fiqh", "Concept", "One is divine, one is human effort."),
    K("Which is the first source of Islamic law?", "The Quran", [
        ("Ijma", "It is the third."),
        ("Qiyas", "It is the fourth."),
        ("The opinion of any individual", "It is not one of the four sources.")],
      "The order is the Quran, the Sunna, ijma, qiyas.", "Sources of law", "Recall", "It is God's word."),
    K("Which scholar founded the Maliki school, widely followed in West and North Africa?", "Malik ibn Anas", [
        ("Abu Hanifa", "He is linked with the Hanafi school."),
        ("Al-Shafi'i", "He is linked with the Shafi'i school."),
        ("Ahmad ibn Hanbal", "He is linked with the Hanbali school.")],
      "Malik ibn Anas stressed the practice of Medina.", "Schools of law", "Recall", "The school has his name."),
    K("In qiyas, how would a scholar treat a new intoxicating drink?", "By analogy with wine, because the cause (intoxication) is shared", [
        ("As permitted because it is not mentioned", "Qiyas extends rulings by shared cause."),
        ("By asking the caliph to decide at random", "Qiyas is reasoned analogy."),
        ("By ignoring the Quran", "It begins from the text.")],
      "The shared cause leads to the same ruling.", "Sources of law", "Application", "Look for a shared cause."),
    K("Which statement about ijtihad is correct?", "It is independent reasoning by a qualified scholar on questions not clearly settled by the texts", [
        ("It is the pilgrimage", "That is Hajj."),
        ("It is a list of forbidden foods", "It is a method, not a list."),
        ("It is only for non-Muslims", "It is a scholarly method inside Islam.")],
      "Scholars debate its extent, but it is the effort to reach a ruling.", "Ijtihad", "Concept", "Think of effort and reasoning."),
], 308)

# ================================================================== 9. Paper 1 strategy
SET(M_EXAM, "Paper 1", "Paper 1 strategy: multiple choice", "rsu2-paper-1-strategy", [
    N("How many multiple-choice questions were in Paper 1 in the Board's 2023 report?", 50, "The report says Paper 1 was made up of 50 multiple-choice questions.", "Paper 1 structure", "Recall", "The report gives a round number."),
    K("What did the Board's report say Paper 1 tested?", "The fundamental concepts of the world religions in the syllabus", [
        ("Only the Old Testament", "The report says that the paper covered the religions of the syllabus."),
        ("Long essays on one religion", "It is a multiple-choice paper."),
        ("Practical skills in a laboratory", "Religious Studies has no laboratory paper.")],
      "The report describes Paper 1 as testing the fundamental concepts across the syllabus.", "Paper 1 structure", "Recall", "Think of breadth."),
    K("Which study habit does the report encourage to help with Paper 1?", "Comparative study of the religions", [
        ("Studying one religion only", "The advice is to study widely."),
        ("Memorising one essay", "That does not help with multiple choice."),
        ("Skipping the syllabus", "The report asks for work within the syllabus.")],
      "The report urges candidates to do comparative studies.", "Revision", "Recall", "It is in the recommendations."),
    K("What should you do first when you meet a multiple-choice question?", "Read the question and think of the answer before reading the options", [
        ("Choose the longest option", "Length is not a clue."),
        ("Choose option C every time", "That is guessing without thought."),
        ("Read only the options", "The stem holds the clues.")],
      "Thinking first protects you from options designed to sound right.", "Technique", "Application", "Do the thinking before the options."),
    K("A question asks which prophet warned about social injustice. One option is 'Amos' and another is 'Elijah'. What is the best step?", "Recall what each is known for and choose the one linked with social justice", [
        ("Pick the first name in the list", "That is guessing."),
        ("Pick the name you have heard most", "Familiarity is not evidence."),
        ("Pick the name with more letters", "That has no meaning.")],
      "Amos is known for social justice, while Elijah is linked with the contest on Carmel.", "Technique", "Application", "Match the person to the fact."),
    K("Which option is a common trap?", "A true statement that does not answer the question asked", [
        ("An option that matches every clue in the stem", "That is likely the answer."),
        ("An option with a person correctly matched to a fact", "That may be the answer."),
        ("The stem of the question", "The stem is the question itself.")],
      "Check that the option answers this stem.", "Technique", "Reasoning", "Re-read the stem after you choose."),
    K("About how much of the examination did Paper 1 carry, according to the report?", "About 34%", [
        ("About 10%", "It is much more than this."),
        ("About 66%", "That is the weight of Papers 2 and 3 together."),
        ("About 50%", "No paper carries half.")],
      "The report gives weights of 34%, 33% and 33%.", "Paper 1 structure", "Recall", "The three papers are close to equal."),
    K("A student revises only the Old Testament. Why is this risky for Paper 1?", "The paper covers the fundamental concepts of several religions", [
        ("Paper 1 has no Old Testament questions", "It may have some."),
        ("Multiple choice never tests facts", "It tests facts and concepts."),
        ("Candidates must answer only one question", "There are 50 questions.")],
      "Breadth is needed.", "Revision", "Reasoning", "Think of coverage."),
], 309)

# ================================================================== 10. Paper 2 strategy
SET(M_EXAM, "Paper 2", "Paper 2 strategy: essays in one section", "rsu2-paper-2-strategy", [
    N("How many questions did candidates answer in Paper 2 in the Board's 2023 report?", 4, "Candidates answered four questions, all from one section.", "Paper 2 structure", "Recall", "All from one section."),
    N("How many questions were there in each section of Paper 2?", 6, "There were 18 questions in three sections of six.", "Paper 2 structure", "Recall", "18 questions divided by three sections."),
    K("What was the most common fault the report names in Paper 2 answers on the Exodus?", "Narrating the story without showing its significance", [
        ("Writing about the wrong religion", "The fault was in how the topic was treated."),
        ("Writing too many numbers", "The fault was about explanation."),
        ("Leaving the question blank", "Many candidates attempted it.")],
      "Candidates told the story but did not explain why it was central to Israel.", "Significance", "Recall", "Story versus meaning."),
    K("Which opening of an essay on Ramadan is best?", "A definition of Ramadan as the month of fasting, with a statement of what will be argued", [
        ("The word 'Introduction' only", "A heading is not an introduction."),
        ("A story about a family meal", "It does not define or answer."),
        ("A list of all Muslim festivals", "The question is about one feast.")],
      "Define, then state the answer to be developed.", "Essay planning", "Application", "An introduction states the focus."),
    K("A question asks about Id-ul-Adha. A candidate also writes at length about Ramadan and the Hajj. What is the problem?", "The answer drifts away from the feast asked", [
        ("It shows too much knowledge", "Knowledge must be used to answer the question."),
        ("It uses paragraphs", "Paragraphs are good."),
        ("It uses a conclusion", "A conclusion is good.")],
      "The report notes candidates who referred to other feasts and narrated processes.", "Focus", "Reasoning", "Stay with the feast in the question."),
    K("Which is the best way to choose a section?", "Pick the section where at least four of the six questions are ones you can answer well", [
        ("Pick the section with the first question that looks easy", "Four answers are needed from one section."),
        ("Pick the section with the shortest questions", "Length is not a guide."),
        ("Pick a different section for each answer", "All four answers must come from the same section.")],
      "You must answer four from one section.", "Choosing a section", "Application", "You answer four, not one."),
    K("What did the report say candidates confused in African Traditional Religion questions on sacred places?", "Sacred places and ordinary social places", [
        ("Prayer and fasting", "That was not stated."),
        ("Kings and chiefs", "That was not stated."),
        ("Hills and mountains in the Bible", "The confusion was about social and sacred places.")],
      "Sacred places include caves, hills and lakes.", "Focus", "Recall", "Look at the word 'sacred'."),
    K("A candidate writes only the story of Saul's rejection in an answer about the confederacy of tribes. What is missing?", "How the confederacy worked and its dynamics", [
        ("The date of Saul's birth", "That is not the focus."),
        ("A list of Saul's descendants", "That is not the focus."),
        ("A comparison with Islam", "It is not required.")],
      "The report says that many commented only on Saul's rejection.", "Focus", "Application", "Read the focus of the question."),
], 310)

# ================================================================== 11. Paper 3 strategy
SET(M_EXAM, "Paper 3", "Paper 3 strategy: structural questions", "rsu2-paper-3-strategy", [
    N("How many questions were there in Paper 3 in the Board's 2023 report?", 36, "The report says there were 36 structural questions in six sections of six.", "Paper 3 structure", "Recall", "Six sections of six questions."),
    N("How many questions did a candidate answer in Paper 3?", 4, "Candidates answered four questions from one section of their choice.", "Paper 3 structure", "Recall", "From one section."),
    K("Which of these was a named section of Paper 3 in 2023?", "Philosophy of Religion", [
        ("Ancient Egyptian religion", "It is not in the named sections."),
        ("Hinduism", "It is not among the named sections."),
        ("Computer ethics", "It is not a section.")],
      "The sections were Luke, John, Acts and 1 Corinthians, Philosophy of Religion, Ethics and Morality, and the Historical Development of Islam.", "Paper 3 structure", "Recall", "Think of the six sections."),
    K("What should a candidate do before answering a structural question?", "Read all its parts first", [
        ("Answer only the last part", "Each part may be marked."),
        ("Write the longest answer to part (a)", "Length should match the marks."),
        ("Skip the command words", "Command words say what to do.")],
      "Parts build on each other.", "Technique", "Application", "Structural questions are connected."),
    K("On Paul's teaching about marriage in 1 Corinthians, what did the report say candidates failed to do?", "Link his teaching to the situation in the Corinthian church", [
        ("Write enough paragraphs", "The fault was the missing link."),
        ("Mention Jesus at all", "The comment was about the Corinthian context."),
        ("Memorise the whole letter", "Context was what was missing.")],
      "Candidates wrote about the ills of marriage in general.", "Context", "Recall", "Think of Corinth."),
    K("In a question on the Good Samaritan, what should the answer bring out?", "The teaching on love and discipleship", [
        ("Only the route from Jerusalem to Jericho", "That is part of the setting, not the teaching."),
        ("Only the names of the characters", "The parable does not give names for them."),
        ("Only a retelling in the candidate's words", "The report criticised retelling.")],
      "The report says that candidates concentrated on narration, not on love and discipleship.", "Context", "Application", "What is the parable teaching?"),
    K("In Philosophy of Religion, which skill does the report suggest is needed on Aquinas' arguments?", "Setting out the Five Ways as arguments for God's existence, such as motion and causation", [
        ("Giving a personal opinion with no reasons", "Opinion alone is not enough."),
        ("Telling a story of Aquinas' life", "The focus is the arguments."),
        ("Listing the books of the Bible", "That is unrelated.")],
      "The report names the arguments from motion, efficient causes and contingency.", "Philosophy of Religion", "Application", "Think of the arguments."),
    K("Why must a candidate match the length of an answer to the marks for a part?", "A short part needs a short answer and a longer part needs developed points, so time is used well", [
        ("Examiners never read long answers", "They read all answers."),
        ("Marks are given for handwriting", "Marks are for content."),
        ("Only part (a) is marked", "Each part is marked.")],
      "Good use of time protects marks across four questions.", "Technique", "Reasoning", "Think of time."),
], 311)

# ================================================================== Paper 1 mock exam A (50 questions: 12 + 10 + 10 + 7 + 11)
P1 = [
    # ---- Module 1: Prophecy in Israel and the eighth-century prophets (12)
    K("What is the main task of a Hebrew prophet?", "To speak for God to the people, calling them to faithfulness", [
        ("To rule the nation as king", "Kings ruled; prophets spoke for God, sometimes against the king."),
        ("To offer the daily sacrifices", "That was the role of priests."),
        ("To copy the Law in the temple", "That was the work of scribes.")],
      "A prophet receives and delivers God's message.", T_HEB, "Recall", "Think of a messenger."),
    K("Which term describes prophets whose words were collected in books, such as Amos and Isaiah?", "Classical or writing prophets", [
        ("Ecstatic bands only", "Ecstatic prophecy was an earlier pattern in groups."),
        ("Temple musicians", "Musicians are not the writing prophets."),
        ("Court scribes", "Scribes are not defined as prophets.")],
      "Classical prophets spoke messages that were later collected and written.", T_HEB, "Recall", "Think of prophetic books."),
    K("Which is a test of a true prophet suggested in the Old Testament?", "Whether the message is fulfilled and agrees with Yahweh's covenant teaching", [
        ("How loud the prophet speaks", "Loudness is not a test."),
        ("Whether the prophet is popular", "False prophets were often popular."),
        ("The prophet's family name", "Family name is not a test.")],
      "Deuteronomy 18 and later prophets stress fulfilment and faithfulness to Yahweh.", T_HEB, "Concept", "Truth is not about popularity."),
    K("On which mountain did Elijah challenge the prophets of Baal?", "Mount Carmel", [
        ("Mount Sinai", "Sinai is where Moses received the covenant."),
        ("Mount Zion", "Zion is Jerusalem's hill."),
        ("Mount Nebo", "Nebo is where Moses viewed the land.")],
      "The contest on Carmel tested who is the true God.", T_ELI, "Recall", "A mountain in northern Israel by the sea."),
    K("What was the main religious issue of Elijah's time?", "Worship of Baal, supported by the royal house, in place of Yahweh", [
        ("The sale of indulgences", "That is a sixteenth-century issue."),
        ("The ending of the Jerusalem temple", "This was later."),
        ("The translation of the Quran", "Unrelated to Elijah's time.")],
      "Ahab and Jezebel promoted Baal worship in Israel.", T_ELI, "Concept", "Think of Jezebel."),
    K("Amos came from", "Tekoa in Judah, where he was a shepherd and farmer", [
        ("Bethel, as a priest", "He was challenged by the priest at Bethel."),
        ("Samaria, as a prince", "He was not a prince."),
        ("Egypt, as an exile", "He was a Judean.")],
      "Amos preached in the northern kingdom though he came from Judah.", T_AMO, "Recall", "A village in the south."),
    K("What was Amos' main complaint against Israel?", "Injustice to the poor, joined to empty religious ritual", [
        ("Lack of temple buildings", "Amos attacked the empty worship, not the lack of buildings."),
        ("Too much study of the Law", "That is not his complaint."),
        ("Failure to pay taxes to Assyria", "That is not his complaint.")],
      "Amos called for justice to roll down like waters.", T_AMO, "Concept", "Think of social justice."),
    K("For Amos, the 'Day of the Lord' would be", "a day of judgement on Israel, not a simple victory", [
        ("a day of certain victory for all Israel", "Amos reversed that popular hope."),
        ("a feast of rest", "It is not described as a feast."),
        ("a day for tax collection", "It is not about taxes.")],
      "Amos warned that the day would be darkness and not light for an unjust people.", T_AMO, "Concept", "He reversed popular hope."),
    K("What is the meaning of the Hebrew word hesed in Hosea?", "Steadfast covenant love and loyalty", [
        ("Military power", "Hesed is about love and loyalty."),
        ("Temple tax", "It is not a tax."),
        ("A kind of sacrifice", "It is not a ritual term.")],
      "Hosea says God desires hesed rather than sacrifice.", T_HOS, "Recall", "A word for faithful love."),
    K("In Hosea's marriage to Gomer, what does the marriage picture?", "God's faithful love for unfaithful Israel", [
        ("The perfect obedience of Israel", "Israel is pictured as unfaithful."),
        ("The power of Assyria", "Assyria is not the picture."),
        ("The unity of the priesthood", "It is a picture of covenant love.")],
      "The prophet's marriage is an acted picture of the covenant relationship.", T_HOS, "Concept", "Who is unfaithful in the story?"),
    K("Where did Isaiah of Jerusalem receive his call, according to Isaiah 6?", "In the temple, in a vision of the holy God", [
        ("In Babylon by the river", "That is Ezekiel's setting."),
        ("At a burning bush", "That is Moses' call."),
        ("In a field of sheep", "That is not the call of Isaiah.")],
      "Isaiah saw the Lord and heard the call 'holy, holy, holy'.", T_ISA, "Recall", "A holy place in Jerusalem."),
    K("What does the name Immanuel (Isaiah 7) mean?", "God with us", [
        ("God is judge", "That is not the meaning of the name."),
        ("The land is lost", "It is not about loss."),
        ("A remnant will return", "That is the meaning of Shear-jashub in Isaiah 7:3.")],
      "The sign was given to Ahaz as a promise that God is with his people.", T_ISA, "Recall", "Look at the Hebrew words in the name."),
    # ---- Module 2: Exilic prophecy and wisdom literature (10)
    K("What does Jeremiah promise in chapter 31?", "A new covenant written on the heart", [
        ("A new temple of stone", "He criticised trust in the temple building."),
        ("A return to the Sinai covenant unchanged", "It is described as new."),
        ("The end of all covenants", "He promises a new covenant.")],
      "The new covenant stresses inner change and forgiveness.", T_JER, "Recall", "Think of heart."),
    K("What was the message of Jeremiah's Temple Sermon?", "Do not trust in the temple building while living unjustly", [
        ("The temple will protect the city whatever the people do", "He denied this."),
        ("Build a larger temple", "The sermon did not ask for this."),
        ("Stop all worship", "He demanded true worship.")],
      "He warned that the temple was not a charm against disaster.", T_JER, "Concept", "Think of false security."),
    K("What are Jeremiah's 'confessions'?", "Personal prayers in which he complains to God about his task and suffering", [
        ("Public announcements of sin by the king", "They are the prophet's own prayers."),
        ("A list of the commandments", "They are not a list of laws."),
        ("Letters to the exiles", "The letter to the exiles is a separate passage.")],
      "They show the cost of being a prophet.", T_JER, "Recall", "Think of personal prayers."),
    K("In which place did Ezekiel prophesy to the exiles?", "Babylon", [
        ("Egypt", "Jeremiah was taken to Egypt."),
        ("Samaria", "Samaria fell earlier to Assyria."),
        ("Rome", "Unrelated period.")],
      "Ezekiel was among those taken to Babylon.", T_EZE, "Recall", "He was among the exiles."),
    K("What does Ezekiel 18 teach about responsibility?", "Each person is responsible for their own sin and not punished for ancestors' sin", [
        ("Children always inherit their parents' guilt", "He denied this proverb."),
        ("Only kings are responsible", "Each individual is."),
        ("No one is responsible", "He stressed responsibility.")],
      "The chapter answers the saying that children's teeth are set on edge by the fathers' sour grapes.", T_EZE, "Concept", "Think of individual responsibility."),
    K("What does the vision of the valley of dry bones (Ezekiel 37) symbolise?", "The restoration of Israel by God's spirit", [
        ("The end of all hope", "The vision gives hope."),
        ("A plague in Egypt", "It is not about Egypt."),
        ("The sacrifice at the temple", "It is not a sacrifice.")],
      "The bones live again when the breath of God enters them.", T_EZE, "Concept", "Think of life from death."),
    K("In Isaiah 40 to 55, who is named as the foreign ruler used by God to free the exiles?", "Cyrus", [
        ("Nebuchadnezzar", "He conquered Jerusalem."),
        ("Pharaoh", "Pharaoh is the ruler of the Exodus."),
        ("Ahab", "Ahab was king of Israel.")],
      "Cyrus of Persia is called God's anointed in Isaiah 45.", T_DEU, "Recall", "A Persian ruler."),
    K("The Suffering Servant in Isaiah 53 is described as one who", "bears the suffering of others", [
        ("conquers the nations by force", "The Servant is pictured as suffering."),
        ("rules from Babylon", "That is not the Servant."),
        ("is not mentioned in any Song", "He is the figure of the Songs.")],
      "Scholars debate whether the Servant is Israel, a prophet or a future figure; Christians later saw Jesus here.", T_DEU, "Concept", "He suffers for others."),
    K("Why do scholars call chapters 40 to 55 'Deutero-Isaiah'?", "Many think a later prophet wrote them in the time of the exile", [
        ("They were written by a Roman governor", "That is incorrect."),
        ("They are from the Gospel of Mark", "That is unrelated."),
        ("They were written before Isaiah of Jerusalem", "Scholars place them later.")],
      "The setting is the exile and the end of the Babylonian era.", T_DEU, "Concept", "Think of 'second'."),
    K("What is theodicy, as in the book of Job?", "An attempt to justify God's goodness in the face of suffering", [
        ("A study of the temple", "It is about suffering and God's goodness."),
        ("A type of sacrifice", "It is not a ritual."),
        ("A list of the prophets", "It is not a list.")],
      "Job asks why the righteous suffer.", T_JOB, "Recall", "Think of God and suffering."),
    # ---- Module 3: Apostolic history and Pauline epistles (10)
    K("Which feature supports the view that the author of Acts was a companion of Paul?", "The 'we' passages, where the narrator joins the account", [
        ("The use of Hebrew poetry", "Hebrew poetry is not the argument."),
        ("The absence of any travel", "Acts is full of travel."),
        ("The letters to Timothy", "These are not in Acts.")],
      "Scholars debate their meaning, but many see them as the author's own presence.", T_ACT, "Concept", "Look for a change of pronoun."),
    K("What happened at Pentecost, according to Acts 2?", "The Holy Spirit came upon the disciples, and Peter preached", [
        ("Paul was converted", "That is Acts 9."),
        ("The Jerusalem council decided on circumcision", "That is Acts 15."),
        ("Stephen was stoned", "That is Acts 7.")],
      "The Spirit's coming empowered the disciples for mission.", T_ACT, "Recall", "A feast fifty days after Passover."),
    K("What did the Jerusalem council in Acts 15 decide, in outline?", "Gentile believers did not have to be circumcised to be part of the church", [
        ("All believers must be circumcised", "That was the demand the council rejected."),
        ("Missions must stop", "Missions continued."),
        ("Paul must leave Antioch", "That was not the decision.")],
      "The decision opened the way to the Gentile mission.", T_ACT, "Recall", "Think of Gentiles and the Law."),
    K("What was Paul's usual first step when he arrived in a new city?", "To go to the synagogue and speak there, where there was one", [
        ("To build a church building", "The early churches met in homes."),
        ("To seek the governor's permission", "That was not his usual practice."),
        ("To rest for a year", "He moved on quickly.")],
      "Acts shows him preaching in synagogues first and then turning to Gentiles.", T_MIS, "Recall", "Think of Jews and God-fearers."),
    K("Why did Paul work in major cities?", "They were centres of trade and travel, so the message could spread from them", [
        ("Because villages were forbidden", "Not a reason given."),
        ("Because cities had no temples", "Cities had many temples."),
        ("Because he disliked travel", "He travelled widely.")],
      "Cities such as Corinth and Ephesus were on busy routes.", T_MIS, "Concept", "Think of roads and trade."),
    K("Which problem in Corinth does 1 Corinthians 1 to 4 address?", "Divisions in the church around favourite leaders", [
        ("Persecution by Rome", "That is not the topic of these chapters."),
        ("Lack of any leaders", "The problem was the opposite."),
        ("The sale of indulgences", "That is from the Reformation.")],
      "Members said 'I follow Paul' or 'I follow Apollos'.", T_COR, "Recall", "Think of party spirit."),
    K("What does Paul say in 1 Corinthians 15 about the resurrection?", "Christ's resurrection is the basis for the hope of the resurrection of believers", [
        ("The resurrection is only a symbol with no hope attached", "Paul teaches real hope."),
        ("There will be no resurrection", "He opposes those who deny it."),
        ("Only the apostles will rise", "He speaks of believers in general.")],
      "Paul links the resurrection of Christ with the future resurrection.", T_COR, "Concept", "Think of 'first fruits'."),
    K("How did Paul answer the question about food offered to idols in 1 Corinthians 8?", "Idols are nothing, but believers must not harm the conscience of weaker members", [
        ("All meat must be refused always", "He did not say this."),
        ("Anyone may eat anything with no concern for others", "He urged concern for the weak."),
        ("Only priests may eat it", "That is not his teaching.")],
      "Love limits freedom.", T_COR, "Application", "Think of the weaker conscience."),
    K("What is 'justification by faith' in Romans and Galatians?", "Being declared right with God through trust in Christ and not by works of the Law", [
        ("Earning salvation by keeping every law", "Paul argues against this."),
        ("Being baptised by a bishop", "It is not about a bishop."),
        ("A promise of wealth", "It is not about wealth.")],
      "Paul argues from Abraham that faith, not law, makes one right with God.", T_GAL, "Concept", "Think of Abraham's faith."),
    K("In Galatians, why does Paul oppose those who require circumcision?", "They add works of the Law to faith in Christ, which he says undermines grace", [
        ("They deny that Christ lived", "That is not his charge."),
        ("They wish to abolish all faith", "They added requirements."),
        ("They require no baptism", "That is not the argument.")],
      "He defends the gospel of grace for Gentiles.", T_GAL, "Reasoning", "Think of Law versus grace."),
    # ---- Module 4: Ethics and eschatology (7)
    K("Which of the following is one of the Beatitudes' blessings?", "Blessed are the peacemakers", [
        ("Blessed are the rich in grain", "That is not a beatitude."),
        ("Blessed are those who refuse tax", "That is not in the text."),
        ("Blessed are the wise scribes", "That is not in the text.")],
      "Peacemakers are named in Matthew 5:9.", T_SER, "Recall", "Look for a character quality."),
    K("What does 'fulfil the Law' mean in Matthew 5:17 in the view of many scholars?", "To bring out its deepest meaning and complete it", [
        ("To abolish all commandments", "Jesus says he does not abolish it."),
        ("To make the Law easier for everyone", "The Sermon makes demands deeper."),
        ("To replace the Law with a new nation", "That is not the saying.")],
      "Jesus goes behind the rule to the attitude of the heart.", T_SER, "Concept", "He did not come to abolish."),
    K("Which text says that Christians must obey God rather than human authority?", "Acts 5:29", [
        ("Romans 13:1", "It calls for subjection to authorities."),
        ("Matthew 5:3", "It is the first Beatitude."),
        ("1 Timothy 6:10", "It is about the love of money.")],
      "Peter and the apostles said it to the council.", T_STA, "Recall", "Think of the council."),
    K("What does Jesus say about divorce in Mark 10?", "He points to creation and says that what God joined must not be separated", [
        ("He urges easy divorce", "He argues against casual divorce."),
        ("He says nothing about marriage", "He teaches on it."),
        ("He says only Romans may divorce", "That is not his teaching.")],
      "He answers the Pharisees by quoting Genesis.", T_STA, "Concept", "Look at creation."),
    K("What is the message of the story of the rich man who went away sad (Mark 10)?", "Attachment to wealth can prevent a person from following Jesus", [
        ("Wealth is always evil in itself", "The text speaks of attachment."),
        ("Poor people never enter the kingdom", "That is not the claim."),
        ("The commandments should be ignored", "The man had kept them.")],
      "The man's wealth was what he could not give up.", T_STA, "Concept", "Think of attachment."),
    K("What does 'Parousia' refer to?", "The return of Christ at the end", [
        ("The birth of Christ", "It refers to a future coming."),
        ("The baptism of Christ", "It refers to the end."),
        ("The sending of the apostles", "It refers to the coming of Christ.")],
      "Parousia means presence or arrival.", T_ESC, "Recall", "A coming in the future."),
    K("Which view says that the kingdom arrived mostly in the ministry of Jesus?", "Realized eschatology", [
        ("Futuristic eschatology", "It stresses the future."),
        ("The interim ethic", "It concerns the Sermon's demands."),
        ("Counsels of perfection", "It concerns two levels of discipleship.")],
      "C. H. Dodd argued for it.", T_ESC, "Concept", "Realized means arrived."),
    # ---- Module 5: Alternative track (11)
    K("What was the main target of Luther's Ninety-five Theses?", "The sale of indulgences", [
        ("The Council of Trent", "Trent came later."),
        ("The English Prayer Book", "That is English."),
        ("Calvin's Institutes", "Calvin's work came later.")],
      "Luther attacked indulgences in 1517.", T_REF, "Recall", "Think of 1517."),
    K("Which reformer worked in Zurich and died at Kappel?", "Ulrich Zwingli", [
        ("John Calvin", "Calvin worked in Geneva."),
        ("Martin Luther", "Luther worked in Wittenberg."),
        ("Ignatius of Loyola", "He founded the Jesuits.")],
      "Zwingli died in battle in 1531.", T_REF, "Recall", "A Swiss city."),
    K("Which body decided the Catholic response to the Reformation between 1545 and 1563?", "The Council of Trent", [
        ("The Diet of Worms", "It met in 1521."),
        ("The Marburg colloquy", "It was in 1529."),
        ("The Jerusalem council", "It is in Acts.")],
      "Trent clarified doctrine and reformed clergy training.", T_REF, "Recall", "A Catholic council."),
    K("Who began the Baptist mission station at Bimbia in 1843?", "Joseph Merrick", [
        ("Alfred Saker", "Saker settled at Douala in 1845."),
        ("Martin Luther", "Luther was in Germany."),
        ("A Pallottine father", "The Pallottines came in 1890.")],
      "Merrick was a Jamaican Baptist missionary (check your textbook for dates).", T_CAM, "Recall", "A Jamaican missionary."),
    K("What did Alfred Saker do for the Duala people?", "Learned their language, worked on the Bible in Duala and ran a school and press", [
        ("Wrote the Cameroon constitution", "That was political."),
        ("Built the first railway", "That is not his work."),
        ("Led the Basel Mission in 1886", "The Basel Mission arrived after Baptists.")],
      "Saker settled at Douala in 1845 and founded Victoria in 1858.", T_CAM, "Concept", "Think of language."),
    K("Which argument says that a good God and evil are logically inconsistent?", "Mackie's inconsistent triad", [
        ("The free-will defence", "It is a reply, not the argument."),
        ("The soul-making theodicy", "It is a reply."),
        ("The via negativa", "It concerns religious language.")],
      "Mackie argued that three claims cannot all be true.", T_EVL, "Recall", "Think of three claims."),
    K("What does Flew's falsification challenge ask of a religious claim?", "What would count against it", [
        ("Whether it is popular", "Popularity is not the test."),
        ("Whether it is old", "Age is not the test."),
        ("Whether it is written in Hebrew", "Language is not the test.")],
      "A claim that rules out nothing seems to say nothing.", T_EVL, "Concept", "Think of the gardener."),
    K("Which framework judges acts by the greatest happiness of the greatest number?", "Utilitarianism", [
        ("Natural law", "It starts from natural purposes."),
        ("Kantian ethics", "It starts from universal duty."),
        ("Situation ethics", "It starts from love in each situation.")],
      "Bentham and Mill developed it.", T_BIO, "Recall", "Consequences."),
    K("In the four principles of medical ethics, which principle stresses respect for the patient's choice?", "Autonomy", [
        ("Justice", "It concerns fairness."),
        ("Non-maleficence", "It concerns avoiding harm."),
        ("Beneficence", "It concerns doing good.")],
      "Autonomy means self-rule.", T_BIO, "Concept", "Whose choice?"),
    K("Which is the correct order of the classical Sunni sources of law?", "Quran, Sunna, ijma, qiyas", [
        ("Qiyas, ijma, Sunna, Quran", "It is the reverse."),
        ("Sunna, Quran, qiyas, ijma", "The Quran comes first."),
        ("Ijma, Quran, qiyas, Sunna", "The Quran comes first.")],
      "The Quran is the first source.", T_ISL, "Recall", "Word of God first."),
    K("Who founded the Hanafi school of law?", "Abu Hanifa", [
        ("Malik ibn Anas", "He is linked with the Maliki school."),
        ("Al-Shafi'i", "He is linked with the Shafi'i school."),
        ("Ahmad ibn Hanbal", "He is linked with the Hanbali school.")],
      "The school is named after him.", T_ISL, "Recall", "The name of the school."),
]
assert len(P1) == 50, len(P1)
from collections import Counter
_cnt = Counter(s["concept"] for s in P1)
assert _cnt[T_HEB] == 3 and _cnt[T_ESC] == 2 and _cnt[T_STA] == 3 and _cnt[T_REF] == 3, _cnt
SETS.append(practice_set(module=M_EXAM, topic="Paper 1", title="Paper 1 mock exam A", lesson="rsu2-paper-1-strategy",
                         mock=True, time_limit_minutes=90, questions=build(P1, 312)))

# ================================================================== Paper 2 practice paper A (25 auto-markable parts)
# Essays cannot be auto-marked; these parts test planning, key arguments and the facts an essay needs, across the five Upper Sixth modules.
P2 = [
    # Question 1: Prophecy in Israel (essay: 'Examine the message of Amos to the northern kingdom')
    K("Question 1 (essay: 'Examine the message of Amos to the northern kingdom'). (a) Which point belongs in the plan?", "His attack on injustice to the poor and on worship without justice", [
        ("The conversion of Gentiles in Corinth", "That belongs to Paul in Acts and 1 Corinthians."),
        ("The invention of the printing press", "That is outside the question."),
        ("The decrees of the Council of Trent", "That is outside the question.")],
      "A plan stays inside the focus of the question.", T_AMO, "Application", "Stay with the prophet and the people he addressed."),
    K("Question 1 (b). Which is the best first sentence of an introduction?", "Amos was a shepherd from Tekoa in Judah who preached in the northern kingdom in a time of prosperity and injustice, and this essay examines his message of justice and judgement.", [
        ("Introduction.", "A heading is not a sentence that answers or defines."),
        ("Many people like prophets.", "It is vague and does not set the focus."),
        ("In the sixteenth century, Luther wrote.", "It is outside the question.")],
      "A good introduction places the prophet and states the focus.", T_AMO, "Application", "Define and set the scene."),
    K("Question 1 (c). Which evaluation point is strongest for a 'discuss' question on Amos?", "His message of judgement is balanced by the call to seek good and live, so his message has hope as well as warning", [
        ("He wrote nothing", "He is a writing prophet."),
        ("He is the only prophet", "Other prophets exist."),
        ("There is no reason to evaluate", "The command word may require evaluation.")],
      "Evaluation gives a balanced judgement with a reason.", T_AMO, "Reasoning", "Consider both warning and hope."),
    K("Question 2 (essay: 'Assess the importance of Hosea's marriage for his message'). (a) What does the marriage picture?", "God's faithful covenant love (hesed) for an unfaithful people", [
        ("The strength of the Assyrian army", "It is not about Assyria."),
        ("The perfection of Israel", "Israel is pictured as unfaithful."),
        ("The rules of the temple", "It is about relationship, not rules.")],
      "The marriage is an acted picture of the covenant.", T_HOS, "Concept", "Think of love and unfaithfulness."),
    K("Question 2 (b). Which is a suitable way of showing the significance of Hosea 11?", "God is pictured as a loving parent who cannot give up on Israel", [
        ("God is pictured as an absent king", "The chapter stresses care."),
        ("God is pictured as a merchant", "That is not the picture."),
        ("God is pictured as indifferent", "It shows love.")],
      "Hosea 11 uses a parent-child picture to express divine love.", T_HOS, "Interpretation", "Think of a father and child."),
    K("Question 3 (essay: 'Discuss the call and message of Isaiah of Jerusalem'). (a) Which theme is central to Isaiah's call in chapter 6?", "The holiness of God", [
        ("The power of Assyria", "Assyria is part of the later setting."),
        ("The cost of the temple", "The theme is holiness."),
        ("The decree of Caesar", "That is a New Testament setting.")],
      "The vision shows God as holy and the prophet as unclean.", T_ISA, "Recall", "A key word is repeated three times in the vision."),
    # Question 4: exile and wisdom
    K("Question 4 (essay: 'Examine Jeremiah's teaching on the new covenant'). (a) Which text is central?", "Jeremiah 31", [
        ("Genesis 1", "It is about creation."),
        ("Matthew 5", "It is the Sermon on the Mount."),
        ("Acts 2", "It is Pentecost.")],
      "Jeremiah 31 contains the promise of a new covenant.", T_JER, "Recall", "Think of 'new covenant'."),
    K("Question 4 (b). Which comparison makes the strongest point about the new covenant?", "It is written on the heart, with inner knowledge of God and forgiveness, where the Sinai covenant was written on stone", [
        ("It abolishes all worship", "It does not abolish worship."),
        ("It is exactly the same in every detail", "It is described as new."),
        ("It applies only to kings", "It is for the people.")],
      "The contrast between stone and heart shows what is new.", T_JER, "Reasoning", "Think of where the law is written."),
    K("Question 5 (essay: 'Explain the message of Ezekiel 18'). (a) Which proverb is Ezekiel answering?", "That the fathers eat sour grapes and the children's teeth are set on edge", [
        ("An eye for an eye", "That is a different saying from the Law."),
        ("Pride goes before a fall", "That is not the saying in the chapter."),
        ("A stitch in time", "It is not in the Bible.")],
      "The proverb blamed children's suffering on their parents.", T_EZE, "Recall", "A saying about grapes."),
    K("Question 5 (b). What is the main teaching?", "Each person is responsible for their own conduct before God", [
        ("Guilt always passes down the family", "Ezekiel denies this."),
        ("No one is accountable", "He stresses accountability."),
        ("Only the priests are accountable", "It applies to every person.")],
      "God judges each individual, and the wicked who turn may live.", T_EZE, "Concept", "Think of 'individual'."),
    K("Question 6 (essay: 'Discuss the Suffering Servant in Deutero-Isaiah'). (a) Which is a scholarly view on the identity of the Servant?", "Israel as a nation, the prophet himself, or a future individual", [
        ("Cyrus only, since he is the only person named", "Cyrus is called the anointed but not the Servant of the Songs in most views."),
        ("The Roman emperor", "Wrong period."),
        ("Moses only", "It is not a standard view.")],
      "Scholars debate; Christians later applied the Songs to Jesus.", T_DEU, "Concept", "Scholars debate more than one view."),
    K("Question 6 (b). Which is a key theme of the fourth Servant Song (Isaiah 52:13-53:12)?", "Innocent suffering that benefits others", [
        ("Military victory", "The Servant suffers."),
        ("Wealth for the Servant", "The Servant is despised and suffers."),
        ("A call to build a palace", "It is not about building.")],
      "The Servant bears the suffering of others.", T_DEU, "Interpretation", "Think of what the Servant bears."),
    K("Question 7 (essay: 'Explain how the book of Job deals with the problem of suffering'). (a) How does the book show that the friends' view is inadequate?", "They claim that suffering is always punishment for sin, but Job is innocent and the book rejects their claim", [
        ("They never speak", "They speak at length."),
        ("They agree with God from the start", "God criticises them at the end."),
        ("They explain everything correctly", "The book does not endorse their view.")],
      "The friends hold the retribution view, which the book challenges.", T_JOB, "Reasoning", "Think of retribution."),
    # Question 8-9: apostolic history and Pauline epistles
    K("Question 8 (essay: 'Assess the reliability of Acts as a history'). (a) Which argument supports reliability?", "The author gives detailed local knowledge of places, titles and travel", [
        ("Acts contains no speeches", "It contains many speeches."),
        ("Acts has no 'we' passages", "It has them."),
        ("Acts was written before Jesus", "It was written after.")],
      "Supporters point to accurate local detail; critics note purpose and speeches.", T_ACT, "Reasoning", "Think of evidence for a writer who knew the world."),
    K("Question 8 (b). Which is a limit on the reliability of Acts, as some scholars argue?", "Luke has a theological purpose and the speeches were composed in his own style", [
        ("Acts gives dates for each day", "It does not."),
        ("Acts never mentions Paul", "It features Paul."),
        ("Acts has no geographical detail", "It has much.")],
      "A fair assessment weighs purpose against detail.", T_ACT, "Reasoning", "Consider the writer's aims."),
    K("Question 9 (essay: 'Examine Paul's missionary strategy'). (a) Which approach is typical in Acts?", "He begins in the synagogue and then turns to Gentiles, often working in urban centres", [
        ("He avoids all cities", "He chose cities."),
        ("He teaches only in his home village", "He travelled widely."),
        ("He works only among the Romans in Rome", "He worked in many places.")],
      "The pattern is synagogue first, cities, house churches.", T_MIS, "Concept", "Think of where he starts."),
    K("Question 9 (b). Which fact about Paul's livelihood is stated in Acts?", "He worked as a tentmaker", [
        ("He was a fisherman", "That was the work of some disciples."),
        ("He was a governor", "He was not."),
        ("He was a priest in Jerusalem", "He was a Pharisee and a tentmaker.")],
      "Acts 18 says that he worked with Aquila and Priscilla at their trade.", T_MIS, "Recall", "A craft in cloth or leather."),
    K("Question 10 (essay: 'Explain Paul's teaching on the Lord's Supper in 1 Corinthians 11'). (a) What was wrong at the Corinthian meal?", "Some members ate and drank without sharing with the poor, so the church was divided", [
        ("No one came to the meal", "The problem was behaviour at the meal."),
        ("The meal took place in secret in the temple of Isis", "The issue was in the church's meal."),
        ("Paul forbade bread", "He told them what the Lord's Supper means.")],
      "Paul rebuked the divisions and selfishness.", T_COR, "Application", "Think of rich and poor."),
    K("Question 10 (b). Which point belongs in a plan on justification in Romans?", "Abraham was counted right with God by faith, which Paul uses to argue that Gentiles are included", [
        ("Abraham earned righteousness by circumcision", "Paul argues that Abraham was counted righteous before circumcision."),
        ("The Law gives life to all who keep it perfectly and no one needs grace", "Paul argues for grace."),
        ("Paul never mentions Abraham", "He often does.")],
      "Romans 4 and Galatians 3 use Abraham.", T_GAL, "Application", "He used an example from Genesis."),
    # Question 11-12: ethics, eschatology, alternative track
    K("Question 11 (essay: 'Discuss the view that the Sermon on the Mount is an impossible ideal'). (a) Which scholar's view would you place against it?", "Those who read it as an ethic of the kingdom to be lived in the power of God", [
        ("Those who read it as a joke", "Not a scholarly view."),
        ("Those who say Jesus never taught it", "That is a separate question about authorship."),
        ("Those who say it applies only to Rome", "It is addressed to disciples.")],
      "The kingdom ethic holds that the Sermon is to be lived.", T_SER, "Reasoning", "Choose the counterview."),
    K("Question 11 (b). Which text would you use to explain Christian attitudes to the state?", "Romans 13:1-7, balanced with Acts 5:29", [
        ("Genesis 1 only", "It does not deal with the state."),
        ("Psalm 23 only", "It does not deal with the state."),
        ("Luke 2 only", "It does not deal with the state.")],
      "A balanced answer uses texts for respect and for limits.", T_STA, "Application", "Use texts from both sides."),
    K("Question 12 (essay: 'Examine the Christian teaching on the Parousia'). (a) Which passage will you use to show that no one knows the day?", "Mark 13", [
        ("Genesis 3", "It is not about the Parousia."),
        ("Psalm 1", "It is not about the Parousia."),
        ("Matthew 1", "It is a genealogy.")],
      "Mark 13:32 says that only the Father knows.", T_ESC, "Recall", "The little apocalypse."),
    K("Question 12 (b). Which pair is correctly matched?", "Dodd with realized eschatology; Schweitzer with futuristic eschatology", [
        ("Dodd with futuristic; Schweitzer with realized", "The pairing is reversed."),
        ("Luther with realized; Calvin with futuristic", "They are reformers, not eschatology scholars here."),
        ("Mackie with realized; Hare with futuristic", "They are philosophers of religion.")],
      "Dodd argued the kingdom had come; Schweitzer that it was mainly future.", T_ESC, "Recall", "Match each scholar."),
    K("Question 13 (essay: 'Compare the teachings of Luther and Calvin'). (a) Which pairing is correct?", "Luther: justification by faith; Calvin: the sovereignty of God and predestination", [
        ("Luther: predestination as the main point; Calvin: indulgences", "Reversed and inaccurate."),
        ("Luther: Council of Trent; Calvin: Act of Supremacy", "These are different events."),
        ("Luther: the Prayer Book; Calvin: the Farewell Sermon", "These are unrelated.")],
      "Luther's centre was justification; Calvin stressed God's sovereignty.", T_REF, "Concept", "Match the emphasis."),
    K("Question 13 (b). Which statement about the Church in Cameroon is the best to include in an essay on the missions?", "The Baptist work of Merrick and Saker on the coast was followed by the Basel Mission and Catholic missions, and later by African-led churches", [
        ("Christianity reached Cameroon only after independence", "Missions arrived in the nineteenth century."),
        ("Only one mission ever worked in the country", "Several missions worked."),
        ("Missions did not found any schools", "They founded many schools.")],
      "The well-established outline is Baptist, Basel and Catholic, then African leadership.", T_CAM, "Application", "Choose the outline that fits the facts."),
]
assert len(P2) == 25, len(P2)
SETS.append(practice_set(module=M_EXAM, topic="Paper 2", title="Paper 2 practice paper A", lesson="rsu2-paper-2-strategy",
                         mock=True, time_limit_minutes=150, questions=build(P2, 313)))
