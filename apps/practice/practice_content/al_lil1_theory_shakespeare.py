"""Practice sets for A Level Literature in English (0735), Lower Sixth: Literary Theory & Practical Criticism (4 sets) and Shakespearean Drama (4 sets).

One set of 8 questions per lesson. All lines of verse, passages and scenarios are original and invented. Facts about Shakespeare are limited to
well-known outlines of Hamlet, Coriolanus, As You Like It, Twelfth Night and Henry V. Metre and counting items were checked by script.
"""

import random

from .dsl import *  # noqa: F403

COURSE = ("literature-in-english", "lower-sixth")

M_THEORY = "Literary Theory & Practical Criticism"
M_SHAKE = "Shakespearean Drama"


def K(prompt, right, wrongs, step, concept, skill, hint, feedback=""):
    """MC spec: right option first, then three (text, why) wrong options. Positions are assigned by build()."""
    assert len(wrongs) == 3, prompt
    assert len(concept) <= 80
    return {"kind": "mc", "prompt": prompt, "right": right, "wrongs": wrongs, "step": step, "concept": concept,
            "skill": skill, "hint": hint, "feedback": feedback}


def N(prompt, answer, step, concept, skill, hint, unit="", feedback=""):
    return {"kind": "num", "prompt": prompt, "answer": answer, "step": step, "concept": concept, "skill": skill,
            "hint": hint, "unit": unit, "feedback": feedback}


def build(specs, seed):
    mcs = [s for s in specs if s["kind"] == "mc"]
    pos = [i % 4 for i in range(len(mcs))]
    random.Random(seed).shuffle(pos)
    it = iter(pos)
    out = []
    for sp in specs:
        steps = [S("Reasoning", text=s) for s in ([sp["step"]] if isinstance(sp["step"], str) else sp["step"])]
        if sp["kind"] == "num":
            out.append(NUM(sp["prompt"], sp["answer"], steps, tolerance=0, unit=sp["unit"], concept=sp["concept"],
                           skill=sp["skill"], hint=sp["hint"], feedback=sp["feedback"]))
            continue
        opts = [C(w, why=y) for w, y in sp["wrongs"]]
        opts.insert(next(it), C(sp["right"], correct=True))
        out.append(MC(sp["prompt"], opts, steps, concept=sp["concept"], skill=sp["skill"], hint=sp["hint"], feedback=sp["feedback"]))
    return out


def SET(module, topic, title, lesson, specs, seed):
    assert len(specs) == 8, title
    SETS.append(practice_set(module=module, topic=topic, title=title, lesson=lesson, questions=build(specs, seed)))


SETS = []

# ================================================================== 1. Aristotle
SET(M_THEORY, "Aristotle's Poetics and tragedy", "Aristotle's Poetics: check your understanding", "lil1-aristotle-poetics", [
    K("Who wrote the Poetics, the early work that defines tragedy?", "Aristotle", [
        ("Plato", "Plato was Aristotle's teacher and wrote about poetry elsewhere, but the Poetics is Aristotle's."),
        ("Sophocles", "Sophocles wrote tragedies such as Oedipus the King, which Aristotle discusses; he did not write the Poetics."),
        ("Shakespeare", "Shakespeare lived about two thousand years later and never read the Poetics in the form we know.")],
      "The Poetics is by the Greek philosopher Aristotle (4th century BC).", "Aristotle and the Poetics", "Recall", "Think of the Greek philosopher who studied under Plato."),
    N("How many parts does Aristotle say every tragedy has?", 6,
      "The six parts are plot, character, thought, diction, melody and spectacle.", "The six parts of tragedy", "Recall", "List them: plot, character, ... and count."),
    K("Which of the six parts does Aristotle rank as the most important?", "Plot", [
        ("Spectacle", "Spectacle depends on the staging, not the poet's art, so Aristotle ranks it last."),
        ("Character", "Character comes second: it is shown through the actions that make up the plot."),
        ("Diction", "Diction is important but ranks below plot and character.")],
      "Aristotle says tragedy is an imitation of action, so the arrangement of events comes first.", "Plot as the soul of tragedy", "Recall", "Which part is about what happens?"),
    K("In the Poetics, hamartia is best understood as", "an error of judgement that begins the hero's fall", [
        ("a moment of recognition of the truth", "That is anagnorisis, not hamartia."),
        ("the audience's emotional release at the end", "That is catharsis."),
        ("a reversal of fortune in the action", "That is peripeteia.")],
      "Hamartia is a mistake or error in judgement; many people call it a tragic flaw, though scholars debate this.", "Hamartia", "Concept", "Which term names the cause of the fall?"),
    K("A messenger comes to bring good news but his words produce the opposite effect. Which term does this illustrate?", "Peripeteia", [
        ("Catharsis", "Catharsis is the audience's emotional release, not a turn in the action."),
        ("Hamartia", "Hamartia is the hero's error, not a turn of events."),
        ("Spectacle", "Spectacle is the visual side of staging.")],
      "A reversal of the action into its opposite is peripeteia.", "Peripeteia", "Application", "Look for a turn of events into its opposite."),
    K("In the invented story of Adaeze, who banishes an innocent young man after hearing a false report, which is her hamartia?", "Acting on a report without checking the facts", [
        ("Learning later that the young man was innocent", "That is her recognition (anagnorisis), not her error."),
        ("The young man's death in exile", "That is the catastrophe that follows from the error."),
        ("The audience's pity at the end", "That is part of catharsis, in the audience.")],
      "Her mistaken judgement, made in good faith, starts the fall.", "Hamartia", "Application", "Which action is the mistake that begins the chain?"),
    K("Which statement best explains why a critic should be careful in applying Aristotle's terms to Shakespeare?", "Aristotle described Greek tragedy and never saw Shakespeare's mixed, many-plotted plays", [
        ("Shakespeare wrote only comedies", "Shakespeare wrote tragedies, comedies and histories."),
        ("Aristotle's terms have only one agreed meaning", "Hamartia and catharsis are in fact disputed, which is another reason for care."),
        ("Shakespeare's plays have no tragic heroes", "Hamlet, Macbeth and others are tragic heroes; the issue is fit, not absence.")],
      "The terms are tools, not rules; they fit some features of Shakespeare and not others.", "Limits of applying Aristotle", "Reasoning", "Think about when and where each writer worked."),
    K("Which description of catharsis is most accurate?", "An effect of pity and fear on the audience, whose exact meaning scholars dispute", [
        ("A mistake by the hero", "That is hamartia."),
        ("The sudden discovery of a hidden identity", "That is anagnorisis."),
        ("The final scene's scenery", "That is spectacle, which is a different part of tragedy.")],
      "Catharsis is usually translated purgation or purification; some say clarification.", "Catharsis", "Concept", "Which term concerns the audience's feelings?"),
], 101)

# ================================================================== 2. Prosody
SET(M_THEORY, "Prosody and scansion", "Metre and form: scansion practice", "lil1-prosody-scansion", [
    N("How many syllables are there in a line of iambic pentameter with no variations?", 10,
      "Five feet, each of two syllables: 5 x 2 = 10.", "Iambic pentameter", "Calculation", "Count feet and syllables per foot."),
    K("Which pattern is a trochee?", "Stressed then unstressed (/ u)", [
        ("Unstressed then stressed (u /)", "That is an iamb."),
        ("Two unstressed then stressed (u u /)", "That is an anapaest."),
        ("Two stressed syllables (/ /)", "That is a spondee.")],
      "A trochee is a strong beat followed by a weak beat.", "Types of foot", "Recall", "Troch- starts with the strong beat."),
    K("Scan this invented line and name its metre: the LAMP-light FLIC-ker ON the SI-lent WALL (capitals are stressed)", "Iambic pentameter", [
        ("Trochaic tetrameter", "The line starts weak then strong (the LAMP), so feet are iambs, and it has ten syllables, five feet."),
        ("Anapaestic tetrameter", "There are not two weak syllables before each stress."),
        ("Dactylic trimeter", "A dactyl starts with a stress, and there are ten syllables, not nine.")],
      "Ten syllables in five weak-strong pairs: the LAMP / light FLIC / ker ON / the SI / lent WALL.", "Scanning a line", "Application", "Group the syllables in pairs from the start."),
    N("The invented line 'at the END of the DAY we came DOWN to the SHORE' is in anapaests. How many feet does it have?", 4,
      "Twelve syllables in groups of three (u u /): 12 / 3 = 4 feet, so anapaestic tetrameter.", "Counting feet", "Calculation", "Divide the syllables by the syllables in a foot."),
    K("The end words of four lines are dawn, sea, lawn, tree. What is the rhyme scheme?", "abab", [
        ("aabb", "That would need the first two lines to rhyme with each other."),
        ("abba", "That would need the last line to rhyme with the first."),
        ("abcd", "The words do rhyme in pairs, so letters must repeat.")],
      "dawn and lawn rhyme (a), sea and tree rhyme (b): a b a b.", "Rhyme scheme", "Application", "Give the same letter to words that rhyme."),
    K("In a Shakespearean sonnet, the last two lines form", "a rhyming couplet", [
        ("a sestet", "A sestet is the six-line part of a Petrarchan sonnet."),
        ("an octave", "An octave is the eight-line opening of a Petrarchan sonnet."),
        ("a blank verse paragraph", "Blank verse is unrhymed; the sonnet's ending rhymes (gg).")],
      "The pattern abab cdcd efef gg ends with a couplet.", "Sonnet forms", "Recall", "Count the pattern from abab."),
    K("A poet writes a galloping poem about a horse in anapaestic metre. What is the most likely effect?", "The quick run of weak syllables gives a feeling of speed", [
        ("A slow, heavy, solemn pace", "Spondees and long stressed runs slow a line; anapaests do the opposite."),
        ("A calm, speech-like steadiness only", "That is the effect of iambs, which are close to natural speech."),
        ("No effect, because metre is decoration", "Metre contributes to mood and meaning, which examiners expect you to explain.")],
      "Two weak syllables before each stress make the rhythm quick.", "Effect of metre", "Reasoning", "Think about how many weak syllables come between stresses."),
    K("A sentence begins in one line and runs on into the next line without a pause. What is this called?", "Enjambment", [
        ("Caesura", "A caesura is a pause inside a line."),
        ("End-stopping", "An end-stopped line finishes its sense at the line end."),
        ("Alliteration", "Alliteration is repeated initial consonant sounds.")],
      "Running on over the line end is enjambment.", "Enjambment", "Concept", "Does the sense stop at the end of the line?"),
], 102)

# ================================================================== 3. Narrative theory
SET(M_THEORY, "Narrative theory", "Narrative theory: check your understanding", "lil1-narrative-theory", [
    K("Which statement best describes the plot, as opposed to the story?", "The way the events are selected, ordered and linked by cause and effect", [
        ("All the events in strict time order", "That describes the story."),
        ("The narrator's opinion of the events", "Opinion is the narrator's commentary, not the plot itself."),
        ("The setting in which the events happen", "The setting is one element; the plot is the arrangement of events.")],
      "Story is the events in time order; plot is the writer's arrangement of them.", "Story and plot", "Concept", "Which one involves the writer's choices about order?"),
    N("Four events A, B, C, D happen in that order in time but are told in the order C, A, D, B. How many times does the telling go back to an earlier event?", 2,
      "Number the events 1 to 4. The telling is 3, 1, 4, 2. It goes back from 3 to 1 and from 4 to 2, so two times.", "Order in narrative", "Calculation", "Write the telling as numbers and count the decreases."),
    K("A narrator who gives an account that the reader cannot fully trust is called", "an unreliable narrator", [
        ("an omniscient narrator", "An omniscient narrator knows everything and is usually, though not always, trusted."),
        ("a chorus", "A chorus is a commenting group or speaker in drama."),
        ("a limited narrator", "A limited narrator knows only one character's thoughts, which is not the same as being untrustworthy.")],
      "The term unreliable narrator comes from Wayne Booth.", "Types of narrator", "Concept", "Look for the phrase about trust."),
    K("Focalization asks which question about a narrative?", "Who sees the events, which may differ from who tells them", [
        ("How long is the narrative?", "Length is not what focalization measures."),
        ("What is the moral of the narrative?", "That is the purpose or theme."),
        ("Which language is the narrative written in?", "Language is not what the term concerns.")],
      "Focalization (Genette) separates who sees from who speaks.", "Focalization", "Concept", "Think of a third-person narrator who tells a child's view."),
    K("In Todorov's pattern, a story begins with", "a stable equilibrium", [
        ("a disruption", "The disruption comes after the opening equilibrium."),
        ("a new equilibrium", "That is the end of the story."),
        ("a recognition of the disruption", "Recognition comes after the disruption.")],
      "Equilibrium, disruption, recognition, repair, new equilibrium.", "Plot shapes", "Recall", "What must exist before it can be disturbed?"),
    K("A short story with talking animals ends by stating a moral. Which oral prose form is it most likely to be?", "A fable", [
        ("A myth", "Myths explain origins or the work of gods and are not typically a short moral tale."),
        ("A legend", "Legends tell of heroes and founding events in a mix of history and wonder."),
        ("A riddle", "A riddle is a short question puzzle, not a story.")],
      "A fable is short, often with animals, and ends with an explicit moral.", "Oral prose forms", "Application", "Which form states its lesson directly?"),
    K("In an invented novel the greedy merchant loses everything and the narrator pities his wife. Which is the best statement of the writer's purpose?", "To warn that greed destroys families and community", [
        ("To describe a market fire", "That is part of the plot, not a purpose."),
        ("To tell the life of a merchant", "That is a summary, not a purpose."),
        ("To praise wealth", "The outcome punishes greed, so the clues point the other way.")],
      "Purpose is found from clues: reward and punishment and where the narrator's sympathy lies.", "A novelist's purpose", "Reasoning", "Where do the reward and the sympathy fall?"),
    K("In Freytag's pyramid, which stage comes straight after the climax?", "Falling action", [
        ("Exposition", "Exposition is the opening that sets up the situation."),
        ("Rising action", "Rising action leads up to the climax."),
        ("Complication", "Complications belong to the rising action before the climax.")],
      "Order: exposition, rising action, climax, falling action, denouement.", "Plot shapes", "Recall", "Order the five parts."),
], 103)

# ================================================================== 4. Critical approaches
SET(M_THEORY, "Critical approaches", "Critical approaches: check your understanding", "lil1-critical-approaches", [
    K("Which of these is a main purpose of literary criticism?", "To interpret and evaluate texts and show how they work", [
        ("To list the facts of the author's life only", "Biography can help, but criticism is about the text and its meaning."),
        ("To replace the text with a summary", "Summarising is not criticism."),
        ("To prove one reading to be the only correct one", "Critics offer reasoned readings; different approaches find different things.")],
      "Criticism explains, interprets and judges literature.", "Purpose of criticism", "Concept", "Think about what a critic does to a text."),
    K("Which approach asks about class, labour and power in a text?", "Marxist criticism", [
        ("Formalist criticism", "Formalism studies form: structure, language and imagery."),
        ("Psychoanalytic criticism", "That approach studies the unconscious mind."),
        ("Feminist criticism", "Feminist criticism focuses on gender.")],
      "Marxist critics follow Marx's idea that economic structures shape society and culture.", "Marxist approach", "Recall", "Which approach has to do with economic classes?"),
    K("Frantz Fanon is most closely connected with", "Post-Colonial criticism", [
        ("New Criticism and close reading", "New Critics such as I. A. Richards and Cleanth Brooks are linked to close reading."),
        ("Psychoanalytic reading of Hamlet's delay", "That reading is linked to Freud and Ernest Jones."),
        ("Russian Formalism", "Shklovsky is the name usually linked to defamiliarisation.")],
      "Fanon wrote about the psychology of colonial rule.", "Key thinkers", "Recall", "Fanon wrote about colonised peoples."),
    K("In an invented novel, the sons choose their careers while their sister is married off against her wishes. Which approach would most naturally focus on this?", "Feminist criticism", [
        ("Formalist criticism", "Formalism would study the way the passage is written, not its gender roles."),
        ("Psychoanalytic criticism", "That would look for hidden desires and conflicts in the mind."),
        ("Marxist criticism", "A Marxist critic might look at wealth and class, though the main contrast here is gender.")],
      "The contrast in freedom between sons and daughter points to gender roles.", "Feminist approach", "Application", "What differs between the sons and the sister?"),
    K("A critic argues that a play's hero delays action because of an unconscious conflict. Which approach is this?", "Psychoanalytic criticism", [
        ("Post-Colonial criticism", "That approach studies empire, language and identity."),
        ("Formalist criticism", "That approach studies form and technique."),
        ("Marxist criticism", "That approach studies class and economic power.")],
      "Hidden unconscious motives are the concern of psychoanalytic criticism (Freud and later critics).", "Psychoanalytic approach", "Application", "Find the word about the unconscious."),
    K("A critic ignores the author and history and studies only a poem's imagery, structure and sound. Which approach is closest?", "Formalist criticism", [
        ("Marxist criticism", "A Marxist critic would consider the social conditions of the poem."),
        ("Post-Colonial criticism", "A Post-Colonial critic would look at empire and identity."),
        ("Feminist criticism", "A feminist critic would look at gender.")],
      "Formalists and New Critics rely on close reading of the text itself.", "Formalist approach", "Application", "Which approach says the text is enough?"),
    K("Which is a fair limit of Marxist criticism?", "It can reduce a work to economics and overlook other themes", [
        ("It cannot be used on a play", "It can be used on any text; the limit is its focus."),
        ("It denies that class exists", "On the contrary, class is its central idea."),
        ("It studies only sounds in poems", "That is closer to formalism.")],
      "Every approach illuminates some features and misses others.", "Evaluating an approach", "Reasoning", "Think about what a focus on money and power may miss."),
    K("Which is the best way to use a critical approach in an essay?", "Ask its question of the text, support it with evidence and say what it cannot explain", [
        ("Name the approach in every sentence", "Naming without analysis earns little."),
        ("Apply it without reading the text closely", "Labels are not evidence."),
        ("Insist that it is the only valid reading", "Examiners value balance and comparison.")],
      "Strong essays use an approach as a tool and test it.", "Using approaches", "Evaluation", "Think of examiners' wish for evidence and balance."),
], 104)

# ================================================================== 5. Reading Shakespeare
SET(M_SHAKE, "Reading Shakespeare's plays", "Reading Shakespeare: theatre and language", "lil1-reading-shakespeare", [
    K("In Shakespeare's public theatre, female roles were played by", "boys", [
        ("women from noble families", "Women did not act on the public stage."),
        ("puppets", "Puppets were not used in the main theatre."),
        ("the chorus", "The chorus was a speaker who commented on the action; it did not play the women.")],
      "Women did not act on the public stage, so boys played women's parts.", "Elizabethan theatre", "Recall", "Who could act on the stage at that time?"),
    N("How many syllables are in a regular line of blank verse?", 10,
      "Blank verse is unrhymed iambic pentameter: 5 feet x 2 syllables = 10.", "Blank verse", "Calculation", "Remember what iambic pentameter means."),
    K("In a Shakespeare play, prose is most often spoken by", "comic characters and in ordinary talk", [
        ("kings in solemn moments", "Kings and nobles normally speak verse in serious moments."),
        ("the ghost in every play", "Ghosts speak verse in the plays where they appear."),
        ("no one, because prose is never used", "Prose is used frequently in the plays.")],
      "Prose is used for comic and lower-status characters, letters, and sometimes madness.", "Verse and prose", "Concept", "Think about who speaks in rhythm and who does not."),
    K("A paraphrase of a line into modern English prose should", "stay in direct speech with the same person and tense and cover all the meaning", [
        ("change into reported speech", "The Board's report says the paraphrase must stay in direct speech."),
        ("switch the person from I to he", "Changing the person changes the meaning of the speech."),
        ("omit any difficult word", "All the sense of the original must be covered.")],
      "These are the rules the Board's report describes.", "Modern English paraphrase", "Concept", "Recall the three rules about person, tense and speech."),
    K("Which is the best modern English version of the invented line 'Thou hast mistook me, sir'?", "You have mistaken me, sir.", [
        ("He has mistaken me, sir.", "The speaker addresses 'thou' (you), not a third person."),
        ("You mistook me, sir, yesterday.", "This adds a time that is not in the line and changes the tense."),
        ("Thou have mistaken me.", "This keeps old 'thou' and has the wrong verb form.")],
      "Thou hast is you have; mistook is mistaken.", "Modern English paraphrase", "Application", "Translate thou hast first."),
    K("A character alone on stage tells the audience his private thoughts. This is", "a soliloquy", [
        ("an aside", "An aside is a short remark that others on stage do not hear, usually with other characters present."),
        ("a chorus", "A chorus is a commenting speaker or group."),
        ("a stage direction", "A stage direction is an instruction in the text, not a speech.")],
      "A soliloquy is a speech to oneself and the audience.", "Soliloquy", "Recall", "Solo means alone."),
    K("Why would the murder of a king be shown as especially horrifying to an Elizabethan audience?", "Many believed the king ruled by God's order, so killing him broke the natural order", [
        ("Kings were the poorest people in society", "Kings were at the top, not the bottom."),
        ("Murder was legal in many cases", "Murder was a crime; the horror came from the rank of the victim."),
        ("The theatre did not allow such scenes", "Such scenes were common; the point is why they shocked.")],
      "The Great Chain of Being placed the king under God and above all others.", "Elizabethan world view", "Reasoning", "Think about the place of kings in the chain of being."),
    K("Before answering tasks on an extract, which question should you settle first?", "Who is speaking, to whom, and where the extract falls in the play", [
        ("What the examiner's opinion is", "Examiners want your reasoned answer, not a guess at theirs."),
        ("How many lines the extract has", "Line count does not help with understanding."),
        ("Which other play has a similar title", "That would only distract from the text.")],
      "Placing the extract guards against mixing characters, a fault the Board names.", "Placing an extract", "Application", "Think about the Board's complaint about mixing up characters."),
], 105)

# ================================================================== 6. Tragedy
SET(M_SHAKE, "Tragedy in Shakespeare", "Hamlet and Coriolanus: tragedy practice", "lil1-shakespeare-tragedy", [
    K("In Coriolanus, who leads the group that finally kills the hero?", "Tullus Aufidius, with his supporters", [
        ("The tribune Brutus", "The tribunes cause his banishment but are not his killers."),
        ("His mother Volumnia", "She persuades him to spare Rome; she does not kill him."),
        ("Menenius, his friend", "Menenius is a friend of Coriolanus and pleads for him.")],
      "Aufidius and the conspirators kill him after he has spared Rome.", "Coriolanus: plot", "Recall", "Who is the Volscian general?"),
    K("Who pleads successfully with Coriolanus to spare Rome?", "His mother Volumnia, with his wife and son", [
        ("Aufidius", "Aufidius is the Volscian leader who is displeased by his decision."),
        ("The tribune Sicinius", "The tribunes are his enemies and do not plead with him."),
        ("The Roman crowd", "The crowd banished him earlier and does not plead.")],
      "His family's plea moves him to yield.", "Coriolanus: plot", "Recall", "Think of his family ties."),
    K("In Hamlet, who is Claudius?", "Hamlet's uncle, who becomes king after the old king's death", [
        ("Hamlet's father", "Hamlet's father is the dead king whose ghost appears."),
        ("Hamlet's friend who survives to tell the story", "That is Horatio."),
        ("The king of Norway", "Norway's prince is Fortinbras.")],
      "Claudius has murdered his brother and married Gertrude.", "Hamlet: characters", "Recall", "Who sits on the throne in Denmark?"),
    K("Which feature is typical of Shakespearean tragedy but unlike Aristotle's single tight action?", "Comic scenes and subplots mixed with the serious plot", [
        ("A hero of high rank", "Aristotle too wants a hero of high standing."),
        ("A fall from good fortune to misfortune", "Aristotle describes this change too."),
        ("Pity and fear in the audience", "These are central to Aristotle's account.")],
      "Shakespeare mixes comic relief and several plots.", "Tragedy compared with Aristotle", "Concept", "Which feature is about structure, not feelings?"),
    K("A student writes: 'Only Aufidius is responsible for the death of Coriolanus.' What is the best criticism of that claim?", "It ignores other causes such as the tribunes, his family's influence and his own temper", [
        ("Aufidius is never present in the play", "Aufidius is a major character."),
        ("Coriolanus is not killed in the play", "He is killed."),
        ("It is too long for an essay", "Length is not the problem; the claim is too narrow.")],
      "A balanced answer weighs several causes and decides which is greatest.", "Arguing causes", "Evaluation", "Think about who else pushed events towards the death."),
    K("In a stage killing of the hero, which prop is the most significant?", "A sword or dagger", [
        ("A crown", "A crown may belong to other scenes but not the killing itself."),
        ("A book", "A book plays no part in the killing."),
        ("A lantern", "Lighting may help the mood, but the killing weapon is the key prop.")],
      "The Board's report notes that most candidates correctly named the sword (or dagger).", "Stagecraft", "Application", "What is used to kill?"),
    K("Which comment best shows that the hero's death is a tragic loss?", "It points to his courage and skill as well as his death", [
        ("It lists the characters on stage at his death", "Listing characters does not explain the loss."),
        ("It states that he dies and moves on", "Stating the death alone does not show loss."),
        ("It says the play has five acts", "Structure is irrelevant to the loss.")],
      "We feel loss when we recall the greatness that is wasted.", "Tragic loss", "Reasoning", "What do we feel we have lost?"),
    K("In Hamlet, why does Hamlet stage a play before the court?", "To test whether Claudius shows guilt", [
        ("To entertain the guests", "Entertainment is not his purpose."),
        ("To announce his marriage", "He is not marrying in the play."),
        ("To honour his father with a feast", "The play is a trap, not a feast.")],
      "The play within the play is his test of the ghost's claim.", "Hamlet: plot", "Recall", "He wants proof."),
], 106)

# ================================================================== 7. Comedy and history
SET(M_SHAKE, "Comedy and history in Shakespeare", "Comedy and history: check your understanding", "lil1-shakespeare-comedy-history", [
    N("Into how many groups did the First Folio of 1623 sort Shakespeare's plays (comedies, histories and ...)?", 3,
      "Comedies, Histories and Tragedies: three groups.", "First Folio and genre", "Recall", "Name the groups and count them."),
    K("Which of these is a typical feature of Shakespearean comedy?", "Confusion and disguise followed by a harmonious ending", [
        ("A hero who dies alone", "That belongs to tragedy."),
        ("A strict single plot with no humour", "Comedies have several plots and much wit."),
        ("A battle in every scene", "That is more typical of history plays.")],
      "Comedy moves from confusion to harmony, often with marriages.", "Comedy conventions", "Concept", "Think of how a comedy ends."),
    K("In As You Like It, Rosalind disguises herself as a young man in the Forest of Arden. What name does she use?", "Ganymede", [
        ("Cesario", "Cesario is the name Viola uses in Twelfth Night."),
        ("Malvolio", "Malvolio is the steward tricked in Twelfth Night."),
        ("Orlando", "Orlando is the young man she loves.")],
      "Rosalind becomes Ganymede.", "As You Like It", "Recall", "Check the name given to the page."),
    K("In Twelfth Night, who disguises herself as the page Cesario?", "Viola", [
        ("Rosalind", "Rosalind is the heroine of As You Like It."),
        ("Olivia", "Olivia is the countess whom Cesario is sent to woo for the Duke."),
        ("Celia", "Celia is Rosalind's cousin in As You Like It.")],
      "Viola, shipwrecked, dresses as a page.", "Twelfth Night", "Recall", "She is shipwrecked at the start."),
    K("Shakespeare's English history plays were based mainly on", "chronicles such as those of Holinshed", [
        ("newspaper reports", "Newspapers as we know them did not exist."),
        ("his own diary", "His chief sources were published histories."),
        ("film scripts", "Film did not exist.")],
      "He drew on printed chronicles and changed events for the stage.", "History plays", "Recall", "Think of printed books of the 1500s."),
    N("In what year was the battle of Agincourt, which Henry V presents on stage?", 1415,
      "Agincourt was fought in 1415.", "Henry V", "Recall", "Fifteenth century.", unit="year"),
    K("Why is Coriolanus hard to place as only a tragedy or only a history play?", "It follows a tragic hero's fall but is based on Roman history and politics", [
        ("It is a comedy about marriage", "It is not a comedy."),
        ("It was written by a different author", "It is by Shakespeare."),
        ("It has no plot", "It has a clear plot.")],
      "It is often called a Roman play or political tragedy; its source was Plutarch in North's translation.", "Blurred genres", "Reasoning", "Think about its source and its shape."),
    K("Which statement about a history play is correct?", "It changes and compresses real events to make a better drama", [
        ("It is an exact record of events", "Shakespeare shortened and changed events."),
        ("It never discusses kingship", "Kingship and power are central themes."),
        ("It was written for a modern audience", "It was written for Elizabethan audiences.")],
      "Write about the play's version of events, not about real history.", "History plays", "Concept", "Think about the difference between a play and a chronicle."),
], 107)

# ================================================================== 8. Writing
SET(M_SHAKE, "Writing about a Shakespeare play", "Writing about Shakespeare: method practice", "lil1-writing-shakespeare", [
    K("In the question 'To what extent is X responsible for Y?', which part is the focus?", "The responsibility of X for Y", [
        ("The words 'To what extent'", "These words are the command, telling you to weigh and judge."),
        ("The question mark", "A punctuation mark is not a focus."),
        ("The length of the answer", "The question does not set length; the focus is the issue to discuss.")],
      "Command words tell you what to do; the focus tells you what to write about.", "Reading the question", "Concept", "What is the question about?"),
    K("Which is the best topic sentence for a paragraph on the tribunes' influence on Coriolanus' fall?", "The tribunes manipulate the crowd so that Coriolanus is banished.", [
        ("Coriolanus is a play by Shakespeare.", "This is a fact that does not answer the question."),
        ("In Act 3 there is a scene in Rome.", "This places a scene but makes no point."),
        ("The tribunes are called Brutus and Sicinius.", "This gives information, not an argument.")],
      "A topic sentence makes a point that answers the question.", "Paragraph structure", "Application", "Which sentence makes a claim?"),
    K("A quotation sub-task asks for two phrases from the extract that show a tragic loss. What should you write?", "Two short phrases copied exactly, in quotation marks", [
        ("A paragraph from memory", "Memory may bring errors; the task is to quote the extract."),
        ("A summary of the extract", "A summary is not a quotation."),
        ("One long speech", "The task asks for two phrases, not one long passage.")],
      "The Board's report notes that candidates lost marks for inaccurate quotation and missing quotation marks.", "Context questions", "Application", "Think about accuracy and marks of quotation."),
    N("In the suggested 45-minute essay plan in the lesson (a KKEVO practice setting), how many minutes are given to the body paragraphs?", 25,
      "45 - 5 (read) - 5 (plan) - 5 (introduction) - 5 (conclusion) = 25.", "Planning time", "Calculation", "Subtract the other four stages from 45."),
    K("A stagecraft sub-task asks you to name the most significant stage prop in a killing scene. What is the best response?", "Name one prop, the sword or dagger, and then explain its use", [
        ("List ten props", "The question asks for the most significant one."),
        ("Describe the plot of the scene", "That is narration, not the task."),
        ("Name the actor who holds it", "The task asks for a prop.")],
      "The Board's report notes that about one in ten candidates ignored 'most significant' and listed other props.", "Stagecraft", "Application", "Read the superlative in the question."),
    K("According to the Board's report, what happens to a paragraph with only one sketchy illustration?", "It earns only a low mark", [
        ("It earns full marks", "More focused illustrations are needed for a fuller paragraph."),
        ("It is ignored by the examiner", "It is read, but scores little."),
        ("It is better than a paragraph with several examples", "Several focused illustrations improve the paragraph.")],
      "More, and more focused, illustrations earn more.", "Illustration", "Recall", "Think about quantity and focus."),
    K("When putting an extract line into modern English, which change is NOT allowed?", "Switching the speaker's person (for example from I to he)", [
        ("Replacing old words with modern ones", "This is the purpose of the task."),
        ("Keeping direct speech", "This is required."),
        ("Keeping the same tense", "This is required.")],
      "The Board's report says no switching of person, tense or voice.", "Modern English paraphrase", "Concept", "Which change breaks a rule?"),
    N("According to the Board's report, how many compulsory questions are there in Paper 3, each divided into sub-tasks a to e?", 4,
      "The report describes four compulsory questions: context questions on drama texts and unseen prose and poetry.", "Exam format", "Recall", "Recall the structure of Paper 3."),
], 108)
