"""Practice sets for Form 5 Literature in English: Shakespearean Drama and African Prose Fiction (one set per lesson)."""

from .dsl import *  # noqa: F403

COURSE = ("literature-in-english", "form-5")

DRAMA = "Shakespearean Drama"
AFRICAN = "African Prose Fiction"


def _q(prompt, opts, ans, solution, concept, skill, hint):
    """Four-option question: opts = [(text, why_wrong), ...]; ans = index of the correct option."""
    choices = [C(t, correct=(i == ans), why=("" if i == ans else w)) for i, (t, w) in enumerate(opts)]
    return MC(prompt, choices, steps=[S("Reasoning", text=solution)], concept=concept, skill=skill, hint=hint)


SETS = []

# ------------------------------------------------------------------ 1. Shakespeare's theatre
SETS.append(practice_set(
    module=DRAMA, topic="Shakespeare's theatre and Elizabethan context",
    title="Shakespeare's theatre and the Elizabethan world: check",
    lesson="lit2-shakespeare-theatre-elizabethan-context",
    questions=[
        _q("In Shakespeare's time, who usually played women's parts on the public stage?", [
            ("Professional actresses", "Women did not act professionally on the English public stage then."),
            ("Princesses invited from the court", "Court visitors were audience members, not actors."),
            ("Boys in female costume", ""),
            ("The playwright's family", "Casting was by professional companies, not by family."),
        ], 2, "Boys played the female roles in the companies of the time.", "Boy actors", "Recall", "Think about who was allowed to act professionally."),
        _q("What was a groundling?", [
            ("A spectator who stood in the yard in front of the stage", ""),
            ("An actor who played in the trap door", "The trap door was part of the stage, not a kind of spectator."),
            ("A servant who carried torches", "Torch carriers were stage hands or actors; a groundling was a spectator."),
            ("A wealthy spectator in the top gallery", "Wealthy spectators sat; groundlings stood and paid less."),
        ], 0, "Groundlings paid little and stood in the yard.", "Playhouse features", "Recall", "The word describes where someone stood."),
        _q("Which stage feature was most useful for the entrance of a ghost or spirit from below?", [
            ("The upper level", "The upper level was used for balconies and walls, not for rising from below."),
            ("The yard", "The yard was where the audience stood."),
            ("The gallery", "Galleries held seated spectators."),
            ("The trap door", ""),
        ], 3, "A trap door let characters appear from or vanish below the stage.", "Playhouse features", "Recall", "Look for the feature in the stage floor."),
        _q("Plays were performed in daylight. What is the most likely result for the playwright's writing?", [
            ("Scenes were never set at night", "Night scenes exist, for example in Macbeth; they were created by words and props."),
            ("Characters often said or showed what the time and place were", ""),
            ("Plays were very short", "Length did not depend on daylight."),
            ("Actors spoke only in prose", "Verse was widely used."),
        ], 1, "Words and torches replaced lighting and scenery.", "Words replace scenery", "Concept", "Ask how an audience could know it was night.", ),
        _q("A king in a Shakespeare play is murdered. For an audience who believed in the divine right of kings, the crime was serious because", [
            ("kings were always popular", "Popularity is not the belief in question."),
            ("kings owned the theatres", "The crime is about the belief in God's choice of the king."),
            ("it was seen as a sin against God as well as a crime against the state", ""),
            ("murder was unknown in England", "Murder was known; the point is the king's special position."),
        ], 2, "The king was thought to be chosen by God, so killing him was also a sin.", "Divine right of kings", "Concept", "What did divine mean in the phrase divine right?"),
        _q("In the chain of being, what did people believe happens if the order is broken at the top?", [
            ("Disorder spreads through the whole world, including nature", ""),
            ("Only the person who broke it suffers", "The belief was that the whole order is affected."),
            ("Nothing, because ranks do not matter", "The belief was that ranks mattered greatly."),
            ("The theatre must close", "This has nothing to do with the chain of being."),
        ], 0, "A break at the top was thought to disturb all of nature, which is why strange events follow Duncan's death.", "Chain of being", "Concept", "Think of one link failing in a chain."),
        _q("Which is the best description of blank verse?", [
            ("Prose written in short paragraphs", "Prose has no regular rhythm."),
            ("Unrhymed lines of about ten syllables with a rhythm of five beats", ""),
            ("Pairs of rhyming lines that close a scene", "That describes a rhyming couplet."),
            ("A speech spoken by one character alone", "That describes a soliloquy."),
        ], 1, "Blank verse is unrhymed, five-beat lines.", "Verse and prose", "Concept", "Blank means no rhyme."),
        _q("A student begins an answer on an extract from Macbeth with a long paragraph about the Globe theatre and the author's life. According to the Board's advice on contextual analysis, what is the best correction?", [
            ("Add more details about the author's schooling", "The advice points away from background for its own sake."),
            ("Replace the paragraph with a longer one on King James", "Background is useful only when it explains the text."),
            ("Delete the whole answer and write about modern theatre", "Modern theatre is not the task."),
            ("Use background only to explain what happens in the extract itself", ""),
        ], 3, "Answers earn credit for explaining the extract. Background facts help only when they explain what is on the page.", "Contextual analysis", "Reasoning", "What does the examiner want you to explain?"),
    ]))

# ------------------------------------------------------------------ 2. Macbeth plot, Acts 1-2
SETS.append(practice_set(
    module=DRAMA, topic="Macbeth: plot and structure",
    title="Macbeth Acts 1 and 2: events in order",
    lesson="lit2-macbeth-plot-acts-1-2",
    questions=[
        _q("In Act 1 Scene 3, Macbeth meets the witches together with", [
            ("Macduff", "Macduff is not on the heath in this scene."),
            ("Banquo", ""),
            ("King Duncan", "Duncan is at his camp, not on the heath."),
            ("Lady Macbeth", "She is at home and learns of the prophecy by letter."),
        ], 1, "Macbeth and Banquo are returning from battle when they meet the witches.", "Witches' prophecy", "Recall", "A fellow general walks with him."),
        _q("Who is the Thane of Cawdor condemned as a traitor at the start of the play?", [
            ("The old Thane of Cawdor, whose title is given to Macbeth", ""),
            ("Macdonwald", "Macdonwald is the rebel Macbeth defeats; Cawdor is a different traitor."),
            ("Banquo", "Banquo stays loyal."),
            ("Malcolm", "Malcolm is Duncan's son and heir."),
        ], 0, "Duncan orders the death of the old Thane of Cawdor and gives his title to Macbeth.", "Thane of Cawdor", "Recall", "His title is given to Macbeth."),
        _q("The witches tell Macbeth three things. Which one is NOT among their greetings to him?", [
            ("Thane of Glamis", "This is one of the greetings."),
            ("Thane of Cawdor", "This is one of the greetings."),
            ("King hereafter", "This is one of the greetings."),
            ("Prince of Cumberland", ""),
        ], 3, "Prince of Cumberland is the title Duncan gives to Malcolm in Act 1 Scene 4.", "Witches' prophecy", "Recall", "One title belongs to Duncan's heir."),
        _q("Why is Act 1 Scene 4 important for Macbeth's plan?", [
            ("Duncan names Malcolm as heir, so Macbeth sees an obstacle", ""),
            ("Duncan names Macbeth as heir", "Duncan names Malcolm, which troubles Macbeth."),
            ("Duncan decides to leave Scotland", "Duncan stays and goes to Inverness."),
            ("The witches are arrested", "The witches do not appear in this scene."),
        ], 0, "Naming Malcolm as heir makes Macbeth see that he must overcome this obstacle to become king.", "Plot development", "Concept", "Think about who will be the next king."),
        _q("In Act 2 Scene 2, why does Lady Macbeth say she did not kill Duncan herself?", [
            ("She feared the guards", "Her reason is a personal feeling, not fear of the guards."),
            ("He looked like her father as he slept", ""),
            ("She was not in the castle", "She is in the castle waiting."),
            ("She wanted Banquo to do it", "Banquo plays no part in the murder."),
        ], 1, "She says Duncan reminded her of her father as he slept. This shows a limit to her hardness.", "Lady Macbeth", "Recall", "Her feelings stop her at the last moment."),
        _q("Which event comes first?", [
            ("Duncan arrives at Inverness", ""),
            ("Macduff finds Duncan's body", "This comes in Act 2."),
            ("Macbeth kills the guards", "This comes after the discovery."),
            ("Macbeth is crowned at Scone", "This is reported at the end of Act 2."),
        ], 0, "Duncan arrives in Act 1 Scene 6; the other events are in Act 2.", "Order of events", "Reasoning", "Which event is in Act 1?"),
        _q("What is the main purpose of the Porter scene in Act 2 Scene 3?", [
            ("To show that the guards are innocent", "It does not clear the guards."),
            ("To introduce a new character who will rule", "The Porter does not rule or reappear in this way."),
            ("To give comic relief and hint that Macbeth's castle has become like hell", ""),
            ("To explain the witches' prophecy", "The prophecy is not discussed in this scene."),
        ], 2, "The Porter's drunken comedy relieves tension and his hell-gate joke hints at evil within the castle.", "Porter scene", "Application", "Think about the mood before and after the scene."),
        _q("After Duncan's death, why are Malcolm and Donalbain suspected by some?", [
            ("They were found with the daggers", "The guards are found with the daggers."),
            ("They inherited the guards' blame", "The princes were not blamed for the guards' crime."),
            ("They had argued with Macduff", "No such argument is part of this plot."),
            ("They fled, which looked like guilt", ""),
        ], 3, "Their flight to England and Ireland made them seem guilty, though they fled in fear.", "Flight of the princes", "Reasoning", "What does running away look like to others?"),
    ]))

# ------------------------------------------------------------------ 3. Macbeth plot, Acts 3-5
SETS.append(practice_set(
    module=DRAMA, topic="Macbeth: plot and structure",
    title="Macbeth Acts 3 to 5 and the structure of the play",
    lesson="lit2-macbeth-plot-acts-3-5",
    questions=[
        _q("Why does Macbeth have Banquo killed?", [
            ("Banquo stole Macbeth's crown", "Banquo has not taken anything from him."),
            ("Banquo knows the witches' prophecy and his descendants are promised the throne", ""),
            ("Banquo plans to leave Scotland", "Banquo is invited to a feast."),
            ("Duncan ordered it before he died", "Duncan plays no part in this."),
        ], 1, "The witches said Banquo's descendants would be kings, so Macbeth sees him and Fleance as a threat.", "Banquo's murder", "Concept", "Think about what the witches told Banquo."),
        _q("What happens to Fleance during the attack on Banquo?", [
            ("Fleance escapes", ""),
            ("Fleance is killed", "Fleance survives."),
            ("Fleance joins the murderers", "He is the target, not a partner."),
            ("Fleance is crowned", "He does not become king in the play."),
        ], 0, "Banquo dies, but Fleance escapes. This keeps Macbeth's fear alive.", "Banquo's murder", "Recall", "The murderers failed at part of their task."),
        _q("At the banquet in Act 3 Scene 4, who can see Banquo's ghost?", [
            ("All the guests", "The guests think Macbeth is ill because they see nothing."),
            ("Lady Macbeth", "She sees nothing and calls it a fit."),
            ("Macbeth only", ""),
            ("Macduff", "Macduff is not at the banquet."),
        ], 2, "Only Macbeth sees the ghost, which shows his guilt.", "Banquet scene", "Recall", "Think about why the lords thought Macbeth was ill."),
        _q("Which is the correct order of the three apparitions in Act 4?", [
            ("Child with a tree, armed head, bloody child", "The armed head is first."),
            ("Bloody child, armed head, child with a tree", "The armed head is first."),
            ("Armed head, child with a tree, bloody child", "The bloody child is second."),
            ("Armed head, bloody child, child with a tree", ""),
        ], 3, "The sequence is armed head, bloody child, crowned child with a tree.", "Apparitions", "Recall", "The first warns him about Macduff."),
        _q("How does Malcolm make Birnam Wood seem to move?", [
            ("His soldiers carry branches cut from the wood", ""),
            ("A storm uproots the trees", "The movement is a trick by the soldiers, not weather."),
            ("The witches enchant the forest", "The witches do not move the trees in this plot."),
            ("Macbeth dreams it", "Birnam Wood actually appears to move."),
        ], 0, "Malcolm orders each soldier to carry a branch to hide the army's size.", "Fulfilment of prophecy", "Concept", "A human army, not magic, does it."),
        _q("Why does the second apparition fail to protect Macbeth?", [
            ("It was a lie told by Banquo", "Banquo does not speak the prophecy."),
            ("Macduff was not born in the usual way", ""),
            ("Lady Macbeth blocks the door", "She is dead by this time."),
            ("Malcolm is born of no woman", "Malcolm is Duncan's son."),
        ], 1, "Macduff says he was untimely ripped from his mother's womb, so he is not born of woman in the usual sense.", "Fulfilment of prophecy", "Concept", "Think about how Macduff describes his birth."),
        _q("Which character kills Macbeth?", [
            ("Malcolm", "Malcolm becomes king but does not fight Macbeth."),
            ("Young Siward", "Macbeth kills young Siward."),
            ("Fleance", "Fleance does not return in the play."),
            ("Macduff", ""),
        ], 3, "Macduff kills Macbeth and brings his head to Malcolm.", "Final battle", "Recall", "The warning in Act 4 predicted this."),
        _q("Why do some textbooks place the climax of Macbeth at the banquet scene rather than at the murder of Duncan?", [
            ("Because Duncan is murdered off stage", "That alone is not the reason."),
            ("Because Banquo's ghost shows that Macbeth's control is slipping", ""),
            ("Because the witches appear at the banquet", "The witches do not appear at the banquet."),
            ("Because Lady Macbeth dies there", "She dies later."),
        ], 1, "The banquet is a turning point: Macbeth's power starts to unravel. Check your textbook for the choice it makes.", "Structure", "Reasoning", "Think about when Macbeth stops being in control."),
    ]))

# ------------------------------------------------------------------ 4. Macbeth characters
SETS.append(practice_set(
    module=DRAMA, topic="Macbeth: characters",
    title="Macbeth: who is who and how they change",
    lesson="lit2-macbeth-characters",
    questions=[
        _q("Who is the king of Scotland at the start of Macbeth?", [
            ("Malcolm", "Malcolm is the king's son and later king."),
            ("Macduff", "Macduff is a thane, not the king."),
            ("Duncan", ""),
            ("Banquo", "Banquo is a general."),
        ], 2, "Duncan is the king, killed by Macbeth in Act 2.", "Characters", "Recall", "He is the one murdered in Act 2."),
        _q("Who is the father of Fleance?", [
            ("Banquo", ""),
            ("Macduff", "Macduff's son is killed in Act 4 and he is not Fleance."),
            ("Duncan", "Duncan's sons are Malcolm and Donalbain."),
            ("Macbeth", "Macbeth is not Fleance's father; he is the one who wants Fleance dead."),
        ], 0, "Banquo's son Fleance escapes the murderers in Act 3.", "Characters", "Recall", "The witches promised his descendants kingship."),
        _q("Which pair of characters are Duncan's sons?", [
            ("Fleance and Siward", "Fleance is Banquo's son and Siward is an English general."),
            ("Malcolm and Donalbain", ""),
            ("Macduff and Ross", "These are thanes, not Duncan's sons."),
            ("Macbeth and Banquo", "These are generals, not Duncan's sons."),
        ], 1, "Malcolm and Donalbain flee after the murder.", "Characters", "Recall", "One goes to England, the other to Ireland."),
        _q("Which description best fits Macbeth at the start of the play?", [
            ("A coward who avoids battle", "Act 1 Scene 2 praises his courage."),
            ("A cruel tyrant", "The tyranny comes later."),
            ("A brave and honoured general", ""),
            ("A foolish servant", "He is a high-ranking soldier."),
        ], 2, "At the start, Macbeth is praised for his bravery in battle.", "Macbeth", "Concept", "Think about the Captain's report."),
        _q("What is the best explanation of Banquo as a foil to Macbeth?", [
            ("Banquo hears the same prophecy but does not murder for power", ""),
            ("Banquo is the king's son", "Banquo is a general, not a prince."),
            ("Banquo is a witch", "He is not a witch."),
            ("Banquo kills Duncan", "He does not kill Duncan."),
        ], 0, "A foil contrasts: both men are tempted, but only Macbeth acts.", "Foil", "Concept", "A foil shows by contrast."),
        _q("Which event in Act 5 shows Lady Macbeth's guilt?", [
            ("She leads an army", "She does not lead an army."),
            ("She sleepwalks and tries to wash imagined blood from her hands", ""),
            ("She attends the coronation of Malcolm", "She is dead by then."),
            ("She meets the witches", "The witches meet Macbeth, not her."),
        ], 1, "The sleepwalking scene shows the guilt she tried to ignore.", "Lady Macbeth", "Recall", "It happens at night, with a doctor and a gentlewoman watching."),
        _q("A student writes that Macduff is Macbeth's loyal friend who helps him to be king. What is wrong with this statement?", [
            ("Macduff is actually a king", "Macduff is a thane."),
            ("Macduff is Duncan's brother", "Macduff is not Duncan's brother."),
            ("Macduff is a witch", "He is not a witch."),
            ("Macduff does not support Macbeth; he joins Malcolm and kills Macbeth", ""),
        ], 3, "Macduff stays away from the coronation, joins Malcolm and kills Macbeth.", "Macduff", "Reasoning", "Whose side does he join in England?"),
        _q("Which statement best explains why Duncan's goodness matters to the play?", [
            ("It makes Macbeth's crime worse and shows the contrast between a good king and a tyrant", ""),
            ("It proves that Duncan is the hero", "The hero of the tragedy is Macbeth."),
            ("It shows that kings should never be trusted", "That is not the lesson drawn."),
            ("It has no connection with the plot", "It is an essential part of Macbeth's inner conflict."),
        ], 0, "Macbeth himself lists Duncan's virtues as reasons not to kill him. The contrast with Macbeth's later rule shows the cost.", "Duncan and Macbeth", "Reasoning", "Macbeth gives it as a reason against the murder."),
    ]))

# ------------------------------------------------------------------ 5. Macbeth themes
SETS.append(practice_set(
    module=DRAMA, topic="Macbeth: themes",
    title="Macbeth: ambition, fate, kingship, guilt and appearance",
    lesson="lit2-macbeth-themes",
    questions=[
        _q("Which statement best defines a theme?", [
            ("The order of events in the story", "That is the plot."),
            ("A central idea that runs through a work", ""),
            ("The place where a story happens", "That is the setting."),
            ("A character's name and rank", "That is characterization."),
        ], 1, "A theme is an idea that recurs through the work.", "Defining theme", "Recall", "It is an idea, not an event."),
        _q("Which theme is most clearly shown by Macbeth's reaction to the prophecy of kingship?", [
            ("Ambition", ""),
            ("Friendship", "The prophecy raises ambition, not friendship."),
            ("Comedy", "This is a tragedy, not a comedy."),
            ("Hospitality", "Hospitality appears in Act 1 but is not the main theme here."),
        ], 0, "The thought of being king awakens Macbeth's ambition.", "Ambition", "Concept", "He is tempted by a title."),
        _q("The witches tell Macbeth what will happen but never tell him to murder anyone. This supports the view that", [
            ("fate alone causes the murder", "The witches do not cause the murder."),
            ("Macbeth is not responsible for his actions", "The play stresses his choice."),
            ("Macbeth makes the choice to kill Duncan himself", ""),
            ("Duncan wanted to die", "There is no support for this."),
        ], 2, "Because no witch orders the murder, the choice is Macbeth's.", "Fate and free will", "Concept", "Who decides to act?"),
        _q("Banquo hears the same prophecies as Macbeth. What does his reaction show?", [
            ("All men will kill for power", "Banquo does not kill for power."),
            ("The prophecies were false", "The play shows many of them come true."),
            ("A man can hear a prophecy and still choose not to do evil", ""),
            ("Banquo was not tempted at all", "He is troubled, so he feels some temptation."),
        ], 2, "Banquo shows that hearing a prophecy does not force a person to act.", "Fate and free will", "Reasoning", "Compare what Banquo and Macbeth do next."),
        _q("Which scene shows Macbeth's guilt most clearly through a vision?", [
            ("The banquet with Banquo's ghost", ""),
            ("The scene with the Captain's report", "This shows Macbeth's bravery, not guilt."),
            ("The scene in which Duncan arrives at Inverness", "Duncan's arrival is a case of dramatic irony."),
            ("The scene in which Malcolm is named heir", "This shows Macbeth's ambition."),
        ], 0, "Banquo's ghost at the banquet is a vision of guilt (Act 3 Scene 4).", "Guilt", "Application", "Think of a ghost that only one person sees."),
        _q("The apparitions seem to promise safety but lead to Macbeth's defeat. This is an example of", [
            ("honest friendship", "They are not honest."),
            ("equivocation, a statement with a hidden meaning", ""),
            ("loyalty", "The apparitions are not loyal."),
            ("hospitality", "This has nothing to do with them."),
        ], 1, "The apparitions are true in a way Macbeth did not expect. This is equivocation and links to appearance and reality.", "Appearance and reality", "Concept", "Their words have a second meaning."),
        _q("Which pair best shows the contrast between good kingship and tyranny?", [
            ("Banquo and Fleance", "These are father and son, not a contrast of rulers."),
            ("Ross and Lennox", "They are thanes, not rulers."),
            ("The Porter and the doctor", "These are minor characters."),
            ("Duncan and Macbeth", ""),
        ], 3, "Duncan is a gentle king; Macbeth rules by fear.", "Kingship", "Application", "Which two characters are kings?"),
        _q("A student begins a theme answer by saying 'First Macbeth meets the witches, then he writes to his wife...' and never names the theme. What is the main weakness?", [
            ("It is too short", "Length is not the main issue."),
            ("It uses the text", "Using the text is good if it is used as evidence."),
            ("It retells the story without discussing the theme", ""),
            ("It names the characters correctly", "Correct names are a strength."),
        ], 2, "A theme answer must name the idea and use events as evidence, not retell the plot.", "Writing about themes", "Reasoning", "What is the question asking for?"),
    ]))

# ------------------------------------------------------------------ 6. Macbeth language and techniques
SETS.append(practice_set(
    module=DRAMA, topic="Macbeth: language and dramatic techniques",
    title="Macbeth: devices, imagery and effects",
    lesson="lit2-macbeth-language-techniques",
    questions=[
        _q("A character alone on stage speaks his thoughts aloud to the audience. This is a", [
            ("soliloquy", ""),
            ("aside", "An aside is short and others are on stage."),
            ("dialogue", "Dialogue is a conversation between characters."),
            ("couplet", "A couplet is two rhyming lines."),
        ], 0, "A speech by a character who is alone is a soliloquy.", "Soliloquy", "Recall", "He is alone."),
        _q("Which speech is a soliloquy?", [
            ("The Porter speaking to Macduff", "He speaks to another character."),
            ("The witches greeting Macbeth", "This is dialogue with others."),
            ("Macbeth seeing the dagger before Duncan's murder", ""),
            ("Ross speaking to Macduff in England", "He speaks to another character."),
        ], 2, "The dagger speech is spoken by Macbeth alone.", "Soliloquy", "Recall", "Macbeth is alone as he waits for the bell."),
        _q("An aside is best described as", [
            ("a long speech at the end of the play", "That does not define an aside."),
            ("a conversation between two lords", "That is dialogue."),
            ("a song by the witches", "This is a song."),
            ("a short remark heard by the audience but not by the other characters", ""),
        ], 3, "An aside is short and is spoken to the audience while others are present.", "Aside", "Concept", "Others are on stage but do not hear."),
        _q("Which is an example of dramatic irony?", [
            ("The storm in the first scene", "This is pathetic fallacy or foreshadowing."),
            ("Duncan praises the castle where he will be murdered", ""),
            ("The Porter makes a joke", "This is comic relief."),
            ("Malcolm tests Macduff", "This is a test, not irony."),
        ], 1, "The audience knows of the plan to kill Duncan but he does not.", "Dramatic irony", "Application", "Who knows more, Duncan or the audience?"),
        _q("What does the image of sleep suggest in Macbeth?", [
            ("The peace and innocence that guilt destroys", ""),
            ("The comedy in the play", "Sleep is not about comedy."),
            ("The wealth of the king", "Sleep is not linked to wealth."),
            ("The skill of a soldier", "Skill in battle is not what the image shows."),
        ], 0, "After the murder Macbeth says he has murdered sleep, which shows his peace is gone.", "Sleep imagery", "Concept", "What does a guilty person lose at night?"),
        _q("Lady Macbeth in Act 5 tries to wash blood that is not there. What does this show?", [
            ("She is a cleaner", "The scene is not about cleaning."),
            ("She is cold and happy", "She is deeply distressed."),
            ("Guilt that cannot be washed away", ""),
            ("A comic scene", "It is serious and tragic."),
        ], 2, "Blood imagery shows guilt in the sleepwalking scene.", "Blood imagery", "Application", "Think about what blood stands for."),
        _q("Macbeth's titles are described as borrowed clothes that do not fit. This clothes imagery suggests that", [
            ("Macbeth is a tailor", "It is a figure of speech."),
            ("Macbeth is not the natural king", ""),
            ("The titles are very comfortable", "The image says they do not fit."),
            ("Macbeth is poor", "It is not about money."),
        ], 1, "Borrowed clothes suggest that he holds rank he has not earned.", "Clothes imagery", "Interpretation", "Do borrowed clothes fit well?"),
        _q("A student writes only 'This is an aside' about a line in Macbeth. What should be added to gain more credit?", [
            ("The effect on the audience, such as revealing the character's hidden thoughts", ""),
            ("A list of all the characters", "This is irrelevant."),
            ("A story about the writer's life", "This is not asked."),
            ("A longer title for the answer", "Titles do not earn credit."),
        ], 0, "Naming a device is not enough; the answer must explain its effect.", "Writing about devices", "Reasoning", "What should the audience feel or understand?"),
    ]))

# ------------------------------------------------------------------ 7. As You Like It, Acts 1-2
SETS.append(practice_set(
    module=DRAMA, topic="As You Like It: plot and characters",
    title="As You Like It Acts 1 and 2: court and flight",
    lesson="lit2-ayli-plot-acts-1-2",
    questions=[
        _q("Who is Duke Senior's brother, who has taken the dukedom?", [
            ("Duke Frederick", ""),
            ("Oliver", "Oliver is Orlando's brother."),
            ("Jaques", "Jaques is a lord with Duke Senior."),
            ("Charles", "Charles is the wrestler."),
        ], 0, "Frederick usurped his elder brother Duke Senior.", "The usurpation", "Recall", "He rules at court."),
        _q("Who is Rosalind's cousin and closest friend?", [
            ("Phebe", "Phebe is a shepherdess in the forest."),
            ("Audrey", "Audrey is a country girl."),
            ("Celia", ""),
            ("Hymen", "Hymen is the god of marriage in the last act."),
        ], 2, "Celia is Duke Frederick's daughter and Rosalind's cousin.", "Characters", "Recall", "She is the daughter of the usurping duke."),
        _q("Whom does Orlando defeat in the wrestling match?", [
            ("Oliver", "Orlando quarrels with Oliver but does not wrestle him in the match."),
            ("Charles", ""),
            ("Frederick", "The duke watches the match."),
            ("Corin", "Corin is a shepherd."),
        ], 1, "Orlando defeats Charles, the Duke's wrestler.", "Wrestling match", "Recall", "He is the Duke's professional wrestler."),
        _q("What happens between Rosalind and Orlando after the wrestling match?", [
            ("They quarrel bitterly", "They fall in love."),
            ("Rosalind banishes him", "Frederick banishes Rosalind, not Orlando."),
            ("They agree to marry at once", "That happens much later."),
            ("They fall in love and Rosalind gives him a chain", ""),
        ], 3, "They fall in love at first sight, and she gives him a chain.", "Love at first sight", "Recall", "She gives him a token."),
        _q("Which two names do Rosalind and Celia use in disguise?", [
            ("Ganymede and Aliena", ""),
            ("Phebe and Audrey", "These are the names of other women in the play."),
            ("Corin and Silvius", "These are shepherds."),
            ("Amiens and Jaques", "These are lords in the forest."),
        ], 0, "Rosalind is Ganymede and Celia is Aliena.", "Disguise", "Recall", "One name is a young man's, the other a stranger's."),
        _q("Why does Adam go with Orlando in Act 2?", [
            ("Adam is Oliver's spy", "He is Orlando's friend."),
            ("Adam wants to be a wrestler", "This has nothing to do with the plot."),
            ("He warns Orlando of Oliver's plot and offers his savings", ""),
            ("He is banished by Frederick", "Adam is a servant of the de Boys family, not banished by Frederick."),
        ], 2, "Adam warns that Oliver plans harm, and faithfully goes with Orlando.", "Adam", "Concept", "He is loyal to the family."),
        _q("Why are the two quarrels in the play said to be like mirrors?", [
            ("Both involve a younger brother wronged by an older brother in power", ""),
            ("Both are about wrestling", "Only one involves a wrestling match."),
            ("Both take place in the forest", "Both begin outside the forest."),
            ("Both end with a death", "Both are resolved without death."),
        ], 0, "Frederick wrongs Senior and Oliver wrongs Orlando; both conflicts are resolved by a change of heart.", "Parallel plots", "Reasoning", "Compare the relationships between the brothers."),
        _q("A student says Duke Senior has the best title because he lives in luxury at court. What is wrong with the statement?", [
            ("He is not a duke", "He is the rightful duke."),
            ("He has been banished and lives in the forest of Arden", ""),
            ("He lives in Oliver's house", "He does not."),
            ("He is dead by Act 2", "He is alive."),
        ], 1, "Duke Senior is the exiled duke; he lives simply in Arden with his lords.", "Duke Senior", "Reasoning", "Where does he live in Act 2?"),
    ]))

# ------------------------------------------------------------------ 8. As You Like It, Acts 3-5
SETS.append(practice_set(
    module=DRAMA, topic="As You Like It: plot and characters",
    title="As You Like It Acts 3 to 5: love, rescue and ending",
    lesson="lit2-ayli-plot-acts-3-5",
    questions=[
        _q("What does Orlando hang on the trees of the forest?", [
            ("Love poems for Rosalind", ""),
            ("Flags for the wrestler", "There is no such action."),
            ("Hunting trophies", "The hunting song is sung by the lords."),
            ("Letters for Oliver", "He does not write to Oliver."),
        ], 0, "Orlando writes poems to Rosalind and hangs them on trees.", "Orlando's poems", "Recall", "He writes about someone he loves."),
        _q("Who falls in love with Ganymede, who is really Rosalind?", [
            ("Audrey", "Audrey marries Touchstone."),
            ("Celia", "Celia loves Oliver."),
            ("Adam", "Adam is an old servant."),
            ("Phebe", ""),
        ], 3, "Phebe falls in love with Ganymede and rejects Silvius.", "Love chains", "Recall", "She is a shepherdess whom Silvius loves."),
        _q("In Act 4 Scene 1, who plays the priest in the mock wedding?", [
            ("Jaques", "Jaques is not in that part of the scene."),
            ("Celia", ""),
            ("Touchstone", "Touchstone is not in the mock wedding."),
            ("Duke Senior", "He is not in that scene."),
        ], 1, "Celia says the words that join Rosalind (as Ganymede) and Orlando in play.", "The mock wedding", "Recall", "Rosalind's cousin does it."),
        _q("What does Orlando save Oliver from?", [
            ("A fire", "Adam's warning in Act 2 mentions burning the lodging, but the rescue is from an animal."),
            ("A flood", "No flood occurs."),
            ("A lioness", ""),
            ("A bear", "The animal is a lioness."),
        ], 2, "Orlando saves Oliver from a lioness while Oliver sleeps.", "The rescue", "Recall", "It is a large wild cat."),
        _q("What is the effect of the rescue on Oliver?", [
            ("He becomes more cruel", "He repents."),
            ("He asks forgiveness and falls in love with Celia (Aliena)", ""),
            ("He leaves Arden", "He stays and prepares to marry."),
            ("He kills Orlando", "He does not harm Orlando."),
        ], 1, "The rescue changes Oliver; he asks forgiveness and falls in love with Aliena.", "Reconciliation", "Concept", "Think of a change of heart."),
        _q("Which of these is NOT one of the four couples at the end?", [
            ("Rosalind and Orlando", "They are a couple."),
            ("Celia and Oliver", "They are a couple."),
            ("Touchstone and Audrey", "They are a couple."),
            ("Jaques and Phebe", ""),
        ], 3, "Phebe marries Silvius; Jaques does not marry.", "The four couples", "Reasoning", "One name belongs to the melancholy lord."),
        _q("How does the play restore the rightful duke?", [
            ("Duke Frederick repents after meeting a religious man and returns the dukedom", ""),
            ("Duke Senior fights a battle", "No battle takes place."),
            ("The wrestler Charles hands it over", "Charles is not involved."),
            ("Oliver buys the dukedom", "It is not bought."),
        ], 0, "Jaques de Boys reports that Frederick has repented and given back the dukedom.", "The ending", "Recall", "He changes his mind on the way."),
        _q("Who speaks the epilogue (closing speech to the audience) in the usual text of the play?", [
            ("Duke Senior", "Duke Senior speaks near the end but the epilogue is Rosalind's."),
            ("Jaques", "Jaques leaves to join Frederick before the epilogue."),
            ("Rosalind", ""),
            ("Touchstone", "Touchstone has no epilogue."),
        ], 2, "Rosalind, the play's leading figure, speaks to the audience at the end. Check your text.", "Epilogue", "Recall", "Who has led the plot?"),
    ]))

# ------------------------------------------------------------------ 9. As You Like It themes and techniques
SETS.append(practice_set(
    module=DRAMA, topic="As You Like It: themes and techniques",
    title="As You Like It: themes and techniques",
    lesson="lit2-ayli-themes-techniques",
    questions=[
        _q("As You Like It is best described as a", [
            ("tragedy", "A tragedy ends in disaster."),
            ("comedy", ""),
            ("history play", "It is not about a king's reign."),
            ("war story", "It is not mainly about war."),
        ], 1, "It is a comedy: problems are solved and it ends with marriages and reconciliation.", "Kind of play", "Recall", "It ends happily."),
        _q("Which pair of lovers shows love at first sight that is later tested?", [
            ("Rosalind and Orlando", ""),
            ("Silvius and Phebe", "Silvius loves Phebe, who first scorns him."),
            ("Touchstone and Audrey", "Their match is plain and comic."),
            ("Jaques and Celia", "These two are not a couple."),
        ], 0, "Rosalind and Orlando fall in love at once and are tested in Arden.", "Love", "Recall", "They meet at the wrestling match."),
        _q("Why is Phebe's love for Ganymede comic?", [
            ("Phebe is a king", "She is a shepherdess."),
            ("Ganymede is an animal", "Ganymede is Rosalind in disguise."),
            ("Phebe does not speak", "She speaks and refuses Silvius."),
            ("Ganymede is really Rosalind, so the audience knows the love cannot succeed", ""),
        ], 3, "The audience shares the secret with Rosalind and sees the mistake.", "Dramatic irony", "Concept", "Who knows that Ganymede is Rosalind?"),
        _q("A character speaks to the audience at the end of the play to ask for their approval. This is the", [
            ("prologue", "A prologue is spoken at the start."),
            ("soliloquy", "A soliloquy is in the middle of the story."),
            ("epilogue", ""),
            ("aside", "An aside is a short remark to the audience, not a closing speech."),
        ], 2, "An epilogue closes the play.", "Epilogue", "Recall", "It comes after the action."),
        _q("What does the contrast between court and forest mainly help the play to show?", [
            ("That the forest is perfect", "The forest has cold and hunger too."),
            ("That cities are always better", "The court is shown as dangerous."),
            ("Two ways of living and how people can change in the forest", ""),
            ("That shepherds are kings", "This is not a theme."),
        ], 2, "The contrast invites us to compare power and simplicity and shows change in Arden.", "Court and country", "Reasoning", "The contrast is a way of thinking about how to live."),
        _q("Which event best shows the theme of reconciliation between brothers?", [
            ("Orlando wrestles Charles", "This is not a reconciliation."),
            ("Oliver plans to burn Orlando's lodging", "This is conflict, not reconciliation."),
            ("Orlando saves Oliver from the lioness and Oliver repents", ""),
            ("Touchstone marries Audrey", "This is not a family reconciliation."),
        ], 2, "The rescue leads to Oliver's repentance and a new bond between the brothers.", "Family reconciliation", "Application", "A brother helps a brother who wronged him."),
        _q("Jaques's gloomy view of life makes Rosalind's cheerfulness more obvious. Jaques is therefore a", [
            ("usurper", "A usurper wrongfully takes a position."),
            ("narrator", "There is no narrator."),
            ("messenger", "He does not carry messages."),
            ("foil", ""),
        ], 3, "A foil contrasts with another character to bring out qualities.", "Foil", "Concept", "A foil shows by contrast."),
        _q("A student says that Arden is a perfect place without problems. What is the best correction?", [
            ("Arden is full of dangerous lions only", "A lioness appears but it is not the whole picture."),
            ("Arden has hardship, such as cold and hunger, as well as freedom", ""),
            ("Arden is a court of the Duke", "Arden is a forest."),
            ("Arden is another name for Oliver's house", "Arden is the forest."),
        ], 1, "Arden has winter wind and hunger and hard-working shepherds, so it is not simply perfect.", "Court and country", "Interpretation", "Remember how Duke Senior describes the winter wind."),
    ]))

# ------------------------------------------------------------------ 10. Reading an African novel
SETS.append(practice_set(
    module=AFRICAN, topic="Reading an African novel",
    title="Reading an African novel: method and extracts",
    lesson="lit2-reading-an-african-novel",
    questions=[
        _q("What does the Board's 2023 report advise students to do about the prescribed texts?", [
            ("Own individual copies and read them", ""),
            ("Watch videos instead of reading", "The report advises students to avoid watching literature videos on the texts."),
            ("Read only the first chapter", "Candidates must know the whole text."),
            ("Borrow notes from others", "The advice is to read the original texts."),
        ], 0, "The report advises students to own copies of the original texts and read them.", "Own copy", "Recall", "It is about the book itself."),
        _q("A chapter log records", [
            ("the author's birthday", "This is not part of a chapter log."),
            ("place, time, who appears and what happens in each chapter", ""),
            ("only the title of the book", "A chapter log is for each chapter."),
            ("the price of the book", "This is not a study note."),
        ], 1, "A chapter log is a short record of each chapter's events.", "Chapter log", "Recall", "It is done chapter by chapter."),
        _q("An episode is", [
            ("a unit of the story, such as a meeting or a journey", ""),
            ("the cover of the book", "The cover is not part of the story."),
            ("a letter of the alphabet", "This is unrelated."),
            ("an exam paper", "This is unrelated."),
        ], 0, "An episode is a part of the story that forms a unit.", "Episode", "Recall", "It is part of the plot."),
        _q("In the invented passage in the lesson (the meeting house), who speaks aloud?", [
            ("Mama Eka", "She says nothing."),
            ("The teacher", "He stands silently by the door."),
            ("Elder Tamba", ""),
            ("The narrator in the first person", "The passage is told in the third person, not by a character."),
        ], 2, "Elder Tamba speaks. Mama Eka and the teacher are silent.", "Placing an extract", "Application", "Who says the line about the road?"),
        _q("In that invented passage, what is the best reading of Mama Eka's look at the teacher?", [
            ("It proves the teacher closed the road", "The passage does not prove anything."),
            ("It hints at a link between them, but the passage does not say what", ""),
            ("It shows she loves the teacher", "There is nothing to suggest love."),
            ("It means she is blind", "Nothing suggests this."),
        ], 1, "Stay with the text: the look is a hint, not a proof.", "Reading carefully", "Interpretation", "How much does the text actually say?"),
        _q("A candidate answers a question on a character by writing about a relative in her own village. What is the main problem?", [
            ("The answer is too long", "Length is not the main problem."),
            ("The answer is in the wrong language", "Language is not the issue."),
            ("The answer does not use the text", ""),
            ("The answer is too formal", "Formality is not the issue."),
        ], 2, "The Board notes that personal experience is irrelevant to text questions.", "Staying with the text", "Reasoning", "What is the question testing?"),
        _q("Which set of questions helps you place an extract?", [
            ("What is the price, size and colour of the book?", "These do not place an extract."),
            ("How long is it and who published it?", "This is not placing."),
            ("Do I like the author?", "Personal likes do not place an extract."),
            ("Who speaks, to whom, where, when, what came before and what comes next?", ""),
        ], 3, "These questions show you know where the extract fits.", "Placing an extract", "Concept", "Think of speaker, listener, place and time."),
        _q("Why should you mark where important episodes start and end in your copy?", [
            ("Because the Board's report says candidates could not tell where an account started and ended", ""),
            ("Because it makes the book heavier", "This is not a reason."),
            ("Because the author asks you to", "The reason is exam practice."),
            ("Because it is forbidden to read twice", "Reading twice is advised."),
        ], 0, "The report says candidates could not determine where an account started and ended, which cost them marks.", "Episode boundaries", "Reasoning", "Think about what went wrong in one 2023 question."),
    ]))

# ------------------------------------------------------------------ 11. The Crown of Thorns
SETS.append(practice_set(
    module=AFRICAN, topic="The Crown of Thorns",
    title="The Crown of Thorns: framework and method",
    lesson="lit2-crown-of-thorns-framework",
    questions=[
        _q("Who is the author of The Crown of Thorns?", [
            ("Linus T. Asong", ""),
            ("Tah Protus", "Tah Protus wrote The Immortal Seed."),
            ("William Golding", "Golding wrote Lord of the Flies."),
            ("George Eliot", "Eliot wrote Silas Marner."),
        ], 0, "The Crown of Thorns is by Linus T. Asong.", "Author", "Recall", "He is named in the Board's list of new texts."),
        _q("In the Board's 2023 report, the Crown of Thorns belongs to which part of Paper 2?", [
            ("Section A, Drama", "Section A is Shakespeare."),
            ("Section B, African literature", ""),
            ("Section C, Poetry", "Section C is the poetry anthology."),
            ("Section D, Prose by a non-African author", "Section D is the non-African novel."),
        ], 1, "The African novel is tested in Section B.", "Exam structure", "Recall", "It is the African novel."),
        _q("The Board's report names which character as the subject of a popular, well-answered question?", [
            ("Chief Nchindia", "The report links Chief Nchindia to the unpopular question."),
            ("The council of elders", "This is part of the unpopular question."),
            ("The D.O.", ""),
            ("Assi", "Assi is in The Immortal Seed."),
        ], 2, "The report says the question on the D.O. was popular and well answered.", "Board's report", "Recall", "It is a main character."),
        _q("Why was the question on disagreements between Chief Nchindia and the council of elders unpopular?", [
            ("Candidates found it hard to pick out instances of disagreement", ""),
            ("The novel has no chief", "The report names Chief Nchindia."),
            ("There were no elders in the novel", "The report names the council of elders."),
            ("The question was in French", "This is not given as a reason."),
        ], 0, "The report says candidates had difficulty picking out instances.", "Board's report", "Recall", "It is about finding instances."),
        _q("A student has a log with the page, issue, positions of both sides and outcome for each disagreement. What will this log most help with?", [
            ("Writing a poem", "This is not what the log is for."),
            ("Reading the map", "A log is a text tool."),
            ("Solving a mathematics problem", "This is unrelated."),
            ("Answering a question that asks for instances of disagreement", ""),
        ], 3, "A log with page references lets you name instances quickly.", "Using a log", "Application", "The log lists instances."),
        _q("A friend tells you the plot of The Crown of Thorns in the playground. What should you do?", [
            ("Use it in place of your own reading", "The report advises owning and reading the text."),
            ("Check every point against your own copy", ""),
            ("Write the answer without opening the book", "This risks mixing up events."),
            ("Ignore the novel entirely", "You must know the text."),
        ], 1, "Other people's summaries may be inaccurate. Check against your own copy.", "Own copy", "Application", "Where should facts come from?"),
        _q("When you write a character profile for the D.O., each trait should be", [
            ("a guess", "A guess has no evidence."),
            ("a general remark about officials", "General remarks are not about the character."),
            ("supported by an event and a page reference from your copy", ""),
            ("copied from a classmate", "Copying risks error."),
        ], 2, "Each trait needs proof from the text.", "Character profile", "Concept", "A trait without proof earns little."),
        _q("A candidate answers a question on the chief and the elders with a general account of how chiefs behave in Cameroon. What is the weakness?", [
            ("It is too specific", "It is the opposite: it is too general."),
            ("It names the characters too often", "It does not name them."),
            ("It uses quotations too much", "It does not quote."),
            ("It does not give specific instances from the novel", ""),
        ], 3, "A question on the novel needs instances from the novel.", "Staying with the text", "Reasoning", "What was the question about?"),
    ]))

# ------------------------------------------------------------------ 12. The Immortal Seed
SETS.append(practice_set(
    module=AFRICAN, topic="The Immortal Seed",
    title="The Immortal Seed: framework and method",
    lesson="lit2-immortal-seed-framework",
    questions=[
        _q("Who wrote The Immortal Seed?", [
            ("Linus T. Asong", "Asong wrote The Crown of Thorns."),
            ("Hans Bokwe Itoe", "Itoe is named for the modern anthology of poetry."),
            ("Tah Protus", ""),
            ("Bole Butake", "Butake is named for the Cameroon anthology of poetry."),
        ], 2, "The Immortal Seed is by Tah Protus.", "Author", "Recall", "The author's name appears in the Board's list of old-syllabus texts."),
        _q("According to the Board's 2023 report, who is the main character in the question that candidates answered very well?", [
            ("Tebene", "Tebene is named in the poorly answered question."),
            ("Fon Jiggang", "Fon Jiggang is named in the poorly answered question."),
            ("The D.O.", "The D.O. belongs to The Crown of Thorns."),
            ("Assi", ""),
        ], 3, "The report names Assi as the main character in the popular, well-answered question.", "Board's report", "Recall", "It is the main character."),
        _q("The question on Assi asked about", [
            ("the price of the book", "This is not a literary question."),
            ("the author's life", "The question is about the character."),
            ("character traits and the role played", ""),
            ("the colour of the cover", "This is not a literary question."),
        ], 2, "The report says it tested character traits and the role played.", "Board's report", "Recall", "It is about the character, not the author."),
        _q("Where does the encounter between Fon Jiggang and Tebene take place, according to the report?", [
            ("At the River Juajua", ""),
            ("At the market", "The report names a river."),
            ("In a school", "The report names a river."),
            ("At the palace gate", "The report names a river."),
        ], 0, "The report names the River Juajua.", "Board's report", "Recall", "A river is named."),
        _q("Why did candidates do poorly on the River Juajua question?", [
            ("The question was too short", "Length is not the reason in the report."),
            ("They could not tell where the account started and ended", ""),
            ("The river was dry", "Not a reason in the report."),
            ("They gave too much detail", "The issue was boundaries and lack of detail."),
        ], 1, "The report says candidates could not determine where the account began and ended.", "Board's report", "Reasoning", "It is about boundaries."),
        _q("In the episode map, what goes under 'Before'?", [
            ("What happens after the episode", "That belongs under 'After'."),
            ("The last page of the book", "This is not part of the episode map."),
            ("Your own opinions", "Opinions are not part of the map."),
            ("Events that led to the episode, which you must not include in the account", ""),
        ], 3, "Before records what led to the episode, so that you can leave it out of the account.", "Episode map", "Concept", "It is about what comes first."),
        _q("A trait without a role would be incomplete because", [
            ("the question may ask what the character does in the story", ""),
            ("roles are not part of literature", "Roles are an important part."),
            ("traits are always wrong", "Traits can be right when proved."),
            ("a trait cannot be proved", "Traits can be proved by events."),
        ], 0, "A full answer says what the character is like and what part he or she plays.", "Trait and role", "Concept", "Think of the Board's question on Assi."),
        _q("A candidate writes an account of the River Juajua encounter that starts with events from the previous chapter and goes on into the next. What is the main fault?", [
            ("It has no beginning", "It has too much beginning."),
            ("It includes events that are outside the episode", ""),
            ("It is written in French", "Language is not the issue."),
            ("It is too short", "It is too long."),
        ], 1, "The account must stay within the first and last parts of the episode.", "Episode boundaries", "Reasoning", "What should you leave out?"),
    ]))

# ------------------------------------------------------------------ 13. Narrative technique and style
SETS.append(practice_set(
    module=AFRICAN, topic="Narrative technique and style",
    title="Narrative technique and style: point of view, proverbs and tone",
    lesson="lit2-narrative-technique-style",
    questions=[
        _q("In first-person narration, the narrator", [
            ("is always the author", "The narrator is a voice in the book, not the author."),
            ("never appears in the story", "That describes some third-person narrators."),
            ("is a character who says 'I'", ""),
            ("is a stranger who knows everything", "That describes an omniscient narrator."),
        ], 2, "A first-person narrator is a character who tells the story as 'I'.", "Point of view", "Recall", "Look for the word I."),
        _q("'The old man did not tell his son where the money was hidden.' This sentence is told in", [
            ("first person", "There is no 'I'."),
            ("second person", "There is no 'you'."),
            ("the future tense", "It describes past events."),
            ("third person", ""),
        ], 3, "It uses 'the old man' and 'his son', so it is third person.", "Point of view", "Application", "Who is speaking: a character or an outsider?"),
        _q("A narrator who can enter the minds of many characters is called", [
            ("limited", "A limited narrator follows one character."),
            ("omniscient", ""),
            ("silent", "This is not a point-of-view term."),
            ("comic", "This describes tone, not point of view."),
        ], 1, "An omniscient narrator is all-knowing.", "Point of view", "Recall", "Omni means all."),
        _q("A proverb is", [
            ("a short traditional saying that states a general truth", ""),
            ("a long speech by a character alone", "That is a soliloquy."),
            ("a poem of fourteen lines", "That is a sonnet."),
            ("a list of names", "This is not a proverb."),
        ], 0, "A proverb is a short saying of traditional wisdom.", "Proverbs", "Recall", "Think of an elder's wise saying."),
        _q("A novel stops its present-day story to tell what happened in a village twenty years earlier. This is a", [
            ("foreshadowing", "Foreshadowing hints at the future."),
            ("climax", "The climax is the high point."),
            ("flashback", ""),
            ("couplet", "A couplet is two lines of verse."),
        ], 2, "A flashback returns to earlier events.", "Structure", "Concept", "The story goes back in time."),
        _q("In the invented passage in the lesson, Old Mbeng says a fast road 'carries away whatever is not tied down'. What does this suggest about the theme?", [
            ("Progress can take away old values", ""),
            ("Roads are always bad", "This overstates the point."),
            ("Lorries are never safe", "The line is about change, not lorries."),
            ("Groundnuts are valuable", "This is not the theme."),
        ], 0, "The saying warns that change can sweep away what is not protected.", "Imagery and theme", "Interpretation", "What is the road a picture of?"),
        _q("In the same passage, nobody could tell whether Mbeng was joking. What does this show about the narrator?", [
            ("The narrator is first person", "The narrator uses 'he' and 'Old Mbeng'."),
            ("The narrator does not enter Mbeng's mind fully", ""),
            ("The narrator is Mbeng", "The passage speaks of Mbeng from outside."),
            ("The narrator is a child", "No sign of this."),
        ], 1, "The narrator reports what can be observed and does not reveal Mbeng's private thoughts.", "Narrator", "Reasoning", "Does the narrator say what Mbeng meant?"),
        _q("A student writes, 'The writer uses a proverb.' and says nothing more. How can the answer be improved?", [
            ("By adding the writer's birthday", "This is not relevant."),
            ("By listing more proverbs without comment", "A list without comment earns little."),
            ("By copying the whole chapter", "Copying earns no marks."),
            ("By saying what the proverb shows about the character, culture or theme", ""),
        ], 3, "Add the effect: what the proverb shows or makes the reader feel.", "Writing about style", "Reasoning", "Name it, show it, explain the effect."),
    ]))

# ------------------------------------------------------------------ 14. Cultural and post-colonial themes
SETS.append(practice_set(
    module=AFRICAN, topic="Cultural and post-colonial themes",
    title="Cultural and post-colonial themes: tradition, authority and identity",
    lesson="lit2-cultural-postcolonial-themes",
    questions=[
        _q("Culture is best defined as", [
            ("the shared way of life of a group, including language and customs", ""),
            ("a government building", "A building is not a culture."),
            ("a type of crop", "This is unrelated."),
            ("the price of goods", "This is unrelated."),
        ], 0, "Culture covers language, customs, beliefs and ways of life.", "Culture", "Recall", "It is a way of life."),
        _q("Colonialism means", [
            ("a group of villages choosing a chief", "That describes local government."),
            ("a kind of traditional dance", "This is unrelated."),
            ("trade between neighbours", "This is not colonial control."),
            ("the control of one territory by another state", ""),
        ], 3, "Colonialism is control of a territory by another state.", "Colonialism", "Recall", "Think of who rules whom."),
        _q("Post-colonial refers to", [
            ("the time before any foreign contact", "Post means after."),
            ("a type of poem", "This is unrelated."),
            ("the period after colonial rule and writing about its effects", ""),
            ("a kind of market", "This is unrelated."),
        ], 2, "Post means after; post-colonial deals with what follows colonial rule.", "Post-colonial", "Recall", "Post means after."),
        _q("In the invented passage in the lesson, why does the clerk's reply in English to the chief's own language matter?", [
            ("It shows that the clerk cannot speak", "The text says the clerk knew the chief's language well."),
            ("It suggests that English is the language of power in the office", ""),
            ("It shows that the chief has no language", "He answers in his own language."),
            ("It shows that the office is closed", "The office is open."),
        ], 1, "The choice of English although the clerk knows the other language shows who holds the power.", "Language and power", "Interpretation", "Who changes language, and why?"),
        _q("Which question would best help you find the theme of authority in a novel?", [
            ("How many pages does the book have?", "Length does not reveal a theme."),
            ("What is the price of the book?", "Price is irrelevant."),
            ("Who holds power and how do they use it?", ""),
            ("Who printed the book?", "The printer is irrelevant."),
        ], 2, "Authority is about who holds power and how it is used.", "Authority", "Application", "Think of chiefs, elders, officers."),
        _q("Why should an answer on tradition and change show both sides?", [
            ("Because novels usually present good and bad in both ways of life", ""),
            ("Because examiners dislike tradition", "Examiners do not favour a side."),
            ("Because change is always good", "This is a one-sided opinion."),
            ("Because tradition is always bad", "This is a one-sided opinion."),
        ], 0, "A balanced answer reflects the complexity the novel shows.", "Balance", "Reasoning", "Does a novel call one side perfect?"),
        _q("A student starts an answer on a cultural theme with a long paragraph on the history of colonial rule and does not mention the novel. What is the main problem?", [
            ("The answer is too balanced", "Balance is a strength."),
            ("The answer does not use the text", ""),
            ("The answer uses correct terms", "Correct terms are good."),
            ("The answer is in English", "English is the exam language."),
        ], 1, "History may explain a term, but the answer must be about the novel.", "Staying with the text", "Reasoning", "What was the question about?"),
        _q("Which entry in a theme log is most useful for the exam?", [
            ("'Tradition is important in Africa'", "This is a general statement without evidence."),
            ("'I like this theme'", "This is a personal opinion."),
            ("'See the film'", "The Board advises against relying on videos."),
            ("'Chapter 00: elders and officer meet; elders speak their language, officer replies in English; shows power'", ""),
        ], 3, "A good entry has the chapter or page, what happens, and what it shows.", "Theme log", "Application", "It needs a page, an event and an explanation."),
    ]))
