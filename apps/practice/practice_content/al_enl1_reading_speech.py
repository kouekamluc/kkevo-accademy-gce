"""Practice sets for A Level English Language, Lower Sixth: Reading Comprehension and Speech Work (one set per lesson).

All passages are original and invented for teaching. IPA is British Received Pronunciation (RP).
"""

from .dsl import *  # noqa: F403

COURSE = ("english-language", "lower-sixth")

M_R = "Reading Comprehension"
M_S = "Speech Work"
T_MAIN = "Main ideas and supporting details"
T_PURP = "Writer's purpose, point of view and attitude"
T_INFER = "Inference and deduction"
T_WORDS = "Words and figures of speech in context"
T_FACT = "Facts, opinions and sequence"
T_DISC = "Discourse markers and cohesion"
T_CRIT = "Critical reasoning and evaluation"
T_SOUNDS = "English consonant and vowel sounds"
T_TRANS = "Phonemic transcription"
T_STRESS = "Word stress"
T_SENT = "Sentence stress and intonation"
T_CONN = "Connected speech and spelling of unknown words"


def Q(prompt, options, ans, whys, step, concept, skill, hint, feedback="", diagram="", diagram_alt="", passage=""):
    """4-option multiple choice. `ans` is the 0-based index of the right option; `whys` has one line per option ("" for the right one).
    `passage` is repeated in full in front of the question."""
    choices = [C(o, correct=(i == ans), why="" if i == ans else whys[i]) for i, o in enumerate(options)]
    steps = [S("Reasoning", text=s) for s in ([step] if isinstance(step, str) else step)]
    text = (passage + "\n\n" + prompt) if passage else prompt
    return MC(text, choices, steps, concept=concept, skill=skill, hint=hint, feedback=feedback, diagram=diagram, diagram_alt=diagram_alt)


def N(prompt, answer, step, concept, skill, hint, feedback="", unit="", tolerance=0):
    steps = [S("Working", text=s) for s in ([step] if isinstance(step, str) else step)]
    return NUM(prompt, answer, steps, tolerance=tolerance, unit=unit, concept=concept, skill=skill, hint=hint, feedback=feedback)


SETS = []

# ================================================================== R1. Main ideas
G1 = (
    "**The Garden That Feeds a School** (an invented article)\n\n"
    "When the canteen at Government Secondary School, Ndop, ran short of money last year, the principal faced a hard choice: serve "
    "smaller meals or ask parents for more. Instead, a group of students suggested a third way. They proposed to grow vegetables on "
    "the unused plot behind the science laboratory.\n\n"
    "The idea was simple, but it needed hard work. Students cleared the land during their games periods, and the agriculture teacher "
    "showed them how to prepare beds and make compost from food scraps. Within three months, the first tomatoes, huckleberry leaves "
    "and cabbages were ready.\n\n"
    "Today the garden supplies about half of the vegetables used in the school's meals. The principal says the cost of food has fallen "
    "noticeably, and the cook says the vegetables are fresher than those bought at the market. Several students admit that they now "
    "eat more vegetables than they did at home.\n\n"
    "The project is not perfect. In the dry season, carrying water from the school tap takes up valuable time, and thieves once took a "
    "whole bed of cabbages. Even so, the students believe the garden is worth the effort, and two neighbouring schools have asked to visit."
)
SETS.append(practice_set(
    module=M_R, topic=T_MAIN, title="Main ideas: the school garden and other passages",
    lesson="enl1-main-ideas-supporting-details",
    questions=[
        Q("Read this paragraph.\n\n'Mobile money has changed how people in many towns pay their bills. A customer no longer needs to travel to the electricity office. "
          "She can pay from her phone in a minute. Traders also receive payment without carrying heavy cash.'\n\nWhich sentence states the main idea?",
          ["Traders carry heavy cash.", "The electricity office is far from town.", "Mobile money makes paying and receiving money easier.", "Phones are expensive to buy."], 2,
          ["That is one detail, so it is too narrow.", "That is one reason, not the point of the whole paragraph.", "", "The paragraph does not say this."],
          "The details (no travel, one-minute payment, no heavy cash) all show that mobile money makes payments easier. That is the umbrella idea.",
          "Main idea of a paragraph", "Concept", "Which sentence do all the other sentences support?"),
        Q("Which sentence best states the main idea of the whole article?",
          ["Students at Ndop dislike school meals.", "Students started a school garden that lowered food costs, although it has some difficulties.", "Agriculture is the most important school subject.", "Thieves are a major problem in schools."], 1,
          ["The article never says students dislike meals; the problem was lack of money.", "", "Not stated; too broad and unsupported.", "Thieves are only one detail in the last paragraph, so this is too narrow."],
          "The article covers the idea (paragraph 1), the work (2), the results (3) and the difficulties (4). Only the second option covers all of them.",
          "Main idea of a passage", "Concept", "Choose the option that covers the beginning, the results and the difficulties.", passage=G1),
        Q("Which sentence best states the main idea of paragraph 2 (beginning 'The idea was simple')?",
          ["The principal faced a hard choice.", "Tomatoes grow quickly.", "Compost is made from food scraps.", "The garden needed hard work and the teacher's help before it produced food."], 3,
          ["That belongs to paragraph 1.", "Too narrow: the paragraph is not about tomatoes only.", "Too narrow: this is one detail about method.", ""],
          "Paragraph 2 describes clearing land, learning from the teacher and waiting three months. The sentence about hard work and help covers these.",
          "Main idea of one paragraph", "Concept", "What do clearing land, preparing beds and waiting three months have in common?", passage=G1),
        Q("Which of the following is NOT a result of the garden?",
          ["The cost of food has fallen.", "Vegetables are fresher.", "Students eat more vegetables.", "The canteen ran short of money."], 3,
          ["Paragraph 3 says this.", "The cook says this.", "Students say this.", ""],
          "The canteen's shortage of money was the problem that led to the garden, not a result of it.",
          "Cause and result", "Reasoning", "Which option happened before the garden and caused it?", passage=G1),
        Q("Which is the best title for the article?",
          ["Thieves Strike a School", "A Cook Complains", "Growing Their Own Lunch: Students Turn Waste Land into Vegetables", "Why Water Is Scarce in the Dry Season"], 2,
          ["Too narrow: thieves appear in one sentence.", "The cook makes a positive remark; this is not the topic.", "", "Too narrow: water is one difficulty."],
          "A good title covers the whole text. Only the third option mentions the students, the land and the vegetables.",
          "Title and main idea", "Application", "Which title would still fit if you removed the last paragraph?", passage=G1),
        Q("The main idea is: 'Reading aloud helps young children learn language.' Which is a supporting detail?",
          ["Many children enjoy cartoons.", "Children who are read to hear new words every day.", "Libraries are closed on Sundays.", "Parents are often busy."], 1,
          ["Not about reading aloud or language.", "", "Not related to language learning.", "Not related to the claim."],
          "A supporting detail gives a reason or example for the main idea. Hearing new words is a reason why reading aloud helps language.",
          "Supporting details", "Concept", "Which option explains WHY reading aloud helps language?"),
        Q("Which sentence best states the main idea of the last paragraph (beginning 'The project is not perfect')?",
          ["The garden has failed.", "Thieves and water problems have ended the project.", "Two neighbouring schools disliked the garden.", "The garden has problems, but the students still think it is worth the effort."], 3,
          ["The students still support it.", "The paragraph does not say the project has ended.", "They asked to visit, which shows interest.", ""],
          "The paragraph names two difficulties and then says 'Even so, the students believe the garden is worth the effort'.",
          "Main idea of one paragraph", "Interpretation", "Notice the words 'Even so'.", passage=G1),
        Q("A summary of the article would NOT need which of these details?",
          ["A thief once took a whole bed of cabbages.", "The garden supplies about half of the vegetables.", "Food costs have fallen.", "Students cleared the land and made compost."], 0,
          ["", "This is a major result.", "This is a major result.", "This is a major step in how the garden began."],
          "The theft is a minor detail that illustrates the difficulties. The other three are major details that a summary needs.",
          "Major and minor details", "Analysis", "Which detail could be dropped without losing the main point?", passage=G1),
    ]))

# ================================================================== R2. Purpose, point of view, attitude
G2 = (
    "**A Quieter Street?** (an invented newspaper column)\n\n"
    "Every morning at six, the music begins. Three shops on our street compete for customers with loudspeakers, and each one tries "
    "to be louder than the others. I do not blame the owners; business is hard, and a lively street can bring in buyers. But I wonder "
    "whether anyone has asked the people who live above the shops.\n\n"
    "My neighbour, a nurse who works nights, now sleeps with cotton wool in her ears. A student down the road told me, with a tired "
    "smile, that he studies with a towel wrapped around his head. These are not complaints from people who dislike music. They are the "
    "quiet pleas of people who simply cannot rest.\n\n"
    "A sensible agreement should not be hard to reach. The shops could set their speakers lower, play music only after nine o'clock, or "
    "take turns on different days. Surely a street can be both busy and bearable. I hope the shop owners will meet and talk, and I hope "
    "they will do it soon."
)
SETS.append(practice_set(
    module=M_R, topic=T_PURP, title="Purpose, point of view and attitude: a newspaper column",
    lesson="enl1-purpose-point-of-view-attitude",
    questions=[
        Q("A text begins: 'Dear Madam, I am writing to complain about the damaged goods that I received on Monday.' The main purpose of the text is",
          ["to complain", "to entertain", "to give instructions", "to congratulate"], 0,
          ["", "Nothing in the sentence is meant to amuse.", "No steps are given.", "The writer is unhappy, not pleased."],
          "The words 'to complain' are stated directly in the opening sentence.",
          "Purpose of a text", "Recall", "What does the writer say she is doing in the first sentence?"),
        Q("What is the writer's main purpose in the column?",
          ["To entertain readers with a funny story", "To teach how loudspeakers work", "To persuade shop owners to agree on quieter practices", "To advertise the shops"], 2,
          ["The tone is serious and concerned, not comic.", "The column does not explain technology.", "", "The writer criticises the noise, not promotes it."],
          "The writer describes a problem, gives examples of those affected and suggests compromises: she is trying to persuade.",
          "Purpose", "Concept", "Look at the third paragraph, where she suggests what shops could do.", passage=G2),
        Q("The writer's attitude to the shop owners is best described as",
          ["angry and insulting", "understanding but concerned", "admiring", "indifferent"], 1,
          ["She says 'I do not blame the owners', so she is not insulting.", "", "She does not praise them.", "She cares enough to write the column."],
          "'I do not blame the owners; business is hard' shows understanding. Her worry about residents shows concern.",
          "Attitude", "Interpretation", "Find the sentence where she speaks about the owners directly.", passage=G2),
        Q("Why does the writer mention the nurse and the student?",
          ["To show that they dislike music", "To prove that the shops are breaking the law", "To praise their hard work", "To give examples of people affected by the noise"], 3,
          ["The writer says the opposite: 'These are not complaints from people who dislike music.'", "No law is mentioned.", "The text does not praise them.", ""],
          "They are specific cases that support her concern that residents cannot rest.",
          "Purpose of details", "Analysis", "What do the nurse and the student have in common?", passage=G2),
        Q("The tone of the last paragraph is mainly",
          ["hopeful and conciliatory", "bitter and sarcastic", "fearful", "humorous"], 0,
          ["", "There is no bitterness; she suggests solutions.", "She does not express fear.", "There is nothing comic in it."],
          "She proposes agreements ('sensible', 'meet and talk') and ends with 'I hope', so the tone is hopeful and conciliatory (willing to find agreement).",
          "Tone", "Interpretation", "Notice the verbs 'hope' and the word 'sensible'.", passage=G2),
        Q("'I stood at the gate and watched them leave. My heart sank.' This extract is told from the point of view of",
          ["a third-person narrator", "the reader", "a first-person narrator", "a writer who is not in the story"], 2,
          ["There is an 'I', so it is not third person.", "Readers are not narrators.", "", "The 'I' is inside the story."],
          "The pronouns 'I' and 'my' show a first-person narrator.",
          "Point of view", "Recall", "Look at the pronouns."),
        Q("What does 'Surely a street can be both busy and bearable' show about the writer?",
          ["She doubts that agreement is possible.", "She is confident and invites readers to agree.", "She is angry.", "She is giving a command."], 1,
          ["'Surely' signals confidence, not doubt.", "", "The sentence is calm.", "It is a statement, not a command."],
          "'Surely' appeals to the reader's good sense and suggests that she expects agreement.",
          "Tone and word choice", "Interpretation", "How does 'surely' differ from 'perhaps'?", passage=G2),
        Q("Which statement shows that the writer tries to be fair?",
          ["'Every morning at six, the music begins.'", "'Three shops on our street compete for customers.'", "'My neighbour ... now sleeps with cotton wool in her ears.'", "'I do not blame the owners; business is hard.'"], 3,
          ["It is a plain statement of the problem.", "It describes the situation but does not consider the owners' side.", "It supports her concern for residents.", ""],
          "Only the fourth statement gives the owners' side. It shows that she understands why they use loudspeakers.",
          "Fairness and bias", "Analysis", "Which statement considers someone's reasons for acting?", passage=G2),
    ]))

# ================================================================== R2b. Text types and parts of a speech
G2B = (
    "**A speech at a youth club meeting** (invented)\n\n"
    "Good evening, Mr Chairman, members of the executive and dear friends.\n\n"
    "Who here has ever walked past a heap of rubbish and said, 'Someone should clean that'? Tonight I ask you to be that someone.\n\n"
    "I stand before you to propose a monthly clean-up of the lane beside our meeting hall. My reasons are three. First, the lane floods when "
    "the drain is blocked. Second, a clean lane will protect our children from infection. Third, our club will earn the respect of our neighbours.\n\n"
    "Let me be clear that the work is not heavy. Twenty members with brooms can finish the lane in one morning. I have also spoken to the "
    "caretaker, who has promised to lend us two wheelbarrows and to keep the hall open for refreshments afterwards.\n\n"
    "Some people may say that cleaning is the council's job. That is partly true. However, we live here, and we need not wait.\n\n"
    "Therefore, I urge each member to bring a broom or a bucket on the first Saturday of every month, starting this week.\n\n"
    "Thank you for your attention."
)
SETS.append(practice_set(
    module=M_R, topic=T_PURP, title="Text types and the parts of a speech: a club speech",
    lesson="enl1-text-types-parts-of-a-speech",
    questions=[
        Q("Which extract is most likely to be the opening of the minutes of a meeting?",
          ["Dear Aunty, I hope you are well.", "Honourable members, I rise to propose the motion.", "Heavy rain destroyed two bridges on Monday, officials said.", "Present: Mr Ako (Chair), Ms Bih (Secretary). Minutes of the meeting held on 3 May."], 3,
          ["That is the start of an informal letter.", "That is typical of a debate.", "That is the opening of a news report.", ""],
          "'Present' followed by names and a date is the standard layout of minutes.",
          "Identifying text types", "Recall", "Which extract lists who attended?"),
        Q("'Who here has ever walked past a heap of rubbish and said, \"Someone should clean that\"?' This sentence is",
          ["a hook using a rhetorical question", "a note of thanks", "a conclusion", "a formal greeting"], 0,
          ["", "Thanks come at the end.", "A conclusion would come at the end.", "The greeting is the first sentence."],
          "The speaker asks a question to capture attention; he does not expect an answer.",
          "Parts of a speech", "Concept", "Where in a speech would you ask the audience a question?", passage=G2B),
        Q("Which sentence states the speaker's main proposal?",
          ["'Good evening, Mr Chairman.'", "'Thank you for your attention.'", "'I stand before you to propose a monthly clean-up of the lane beside our meeting hall.'", "'Some people may say that cleaning is the council's job.'"], 2,
          ["That is the salutation.", "That is the closing thanks.", "", "That is an objection the speaker will answer."],
          "The third sentence announces what the speech is about and what the speaker wants.",
          "Thesis of a speech", "Concept", "Which sentence begins 'I stand before you to...'?", passage=G2B),
        Q("What is the job of the sentences beginning 'Some people may say that cleaning is the council's job'?",
          ["To open the speech", "To answer a possible objection", "To call the audience to act", "To thank the audience"], 1,
          ["The speech opens with the greeting and hook.", "", "The call to action is the sentence beginning 'Therefore'.", "Thanks come at the end."],
          "The speaker mentions what others might say and replies ('However, we live here').",
          "Answering objections", "Analysis", "Does the speaker agree completely with the view in these sentences?", passage=G2B),
        Q("Which feature shows that the speaker uses the rule of three?",
          ["The speaker tells three jokes.", "The speech ends with three questions.", "The speaker thanks the audience three times.", "The speaker gives three reasons: First, Second and Third."], 3,
          ["The speech contains no jokes.", "There is only one question.", "There is one expression of thanks.", ""],
          "'My reasons are three. First... Second... Third...' is a clear rule of three.",
          "Persuasive devices", "Recall", "Count the signposts First, Second, Third.", passage=G2B),
        Q("Which text type is most likely to have the headings 'Findings' and 'Recommendations'?",
          ["A report", "A story", "A speech", "An informal letter"], 0,
          ["", "A story has plot and characters, not headings like these.", "A speech has no headings.", "An informal letter has no such headings."],
          "Reports present findings and then recommend actions.",
          "Features of a report", "Recall", "Which text type presents results and advice?"),
        Q("In the speech, the word 'Therefore' introduces",
          ["a contrast", "an example", "a call to action that follows from the reasons", "a question"], 2,
          ["A contrast would use 'however' or 'but'.", "An example would use 'for example'.", "", "The sentence is a request, not a question."],
          "'Therefore' marks a result or conclusion. Here it leads to the speaker's appeal to members.",
          "Discourse in speeches", "Interpretation", "The speaker has just given his reasons. What follows from them?", passage=G2B),
        Q("Which statement about the audience is best supported by the speech?",
          ["Strangers in a market", "Members of a club that meets in a hall", "Primary school children", "Council officials"], 1,
          ["The speech says 'dear friends' and 'our club'.", "", "The vocabulary and the hall do not fit children.", "The speaker mentions the council in the third person, as people outside the room."],
          "'Mr Chairman, members of the executive' and 'our meeting hall' show that the audience belongs to the club.",
          "Audience", "Analysis", "Whom does the speaker greet, and what does 'our' refer to?", passage=G2B),
    ]))

# ================================================================== R3. Inference and deduction
G3 = (
    "**The Lamp** (an invented story)\n\n"
    "When Tabi returned from the farm, the compound was quiet. The cooking fire, which his mother always lit before dusk, was cold. "
    "The pot sat upside down on the stones, and the washing still hung on the line though the sun had set.\n\n"
    "Tabi put down his hoe and listened. From inside the house came a soft, uneven cough. He took the small oil lamp from its shelf, "
    "shook it to check how much oil remained, and carried it in. His mother lay on the mat with a cloth over her eyes. Beside her, the "
    "bowl of water he had filled that morning was untouched.\n\n"
    "'You should have called me,' he said. She smiled weakly. 'The farm needed you more,' she answered.\n\n"
    "Tabi said nothing. He set the lamp down, hurried to the neighbour's door and knocked twice. When Madam Fonyuy opened it, he did "
    "not greet her. He only said, 'Please, can you come? And is your son home with the motorbike?'"
)
SETS.append(practice_set(
    module=M_R, topic=T_INFER, title="Inference and deduction: the story of the lamp",
    lesson="enl1-inference-and-deduction",
    questions=[
        Q("All members of the football club pay a fee. Ama is a member of the football club. Which conclusion follows with certainty?",
          ["Ama is the captain.", "Ama pays a fee.", "Ama is a good player.", "Everyone who pays a fee is a member."], 1,
          ["Nothing is said about a captain.", "", "Nothing is said about her skill.", "That reverses the first statement and does not follow."],
          "The first statement is a rule for all members. Ama is a member, so the rule applies to her. This is a deduction.",
          "Deduction", "Reasoning", "Apply the rule about members to Ama."),
        Q("Why was the compound quiet and the fire cold?",
          ["Tabi's mother was unwell.", "His mother had gone to the market.", "His mother was angry with him.", "There was no wood."], 0,
          ["", "She is at home, in the house.", "She speaks kindly to him.", "Nothing about wood is mentioned."],
          "The cough, the mat, the cloth over her eyes and the untouched water show that she was unwell and had not lit the fire.",
          "Inference from clues", "Reasoning", "Find where the mother is when Tabi enters.", passage=G3),
        Q("Why does Tabi ask whether Madam Fonyuy's son is home with the motorbike?",
          ["He wants to go to the farm quickly.", "He wants to sell crops.", "He wants to visit the son.", "He wants to take his mother quickly to get medical help."], 3,
          ["His work at the farm is finished for the day.", "No selling is mentioned.", "The visit is not his purpose.", ""],
          "He hurries to the neighbour's door and asks for transport right after seeing his mother ill. The most likely reason is to get her to a health centre.",
          "Inference of purpose", "Application", "What has Tabi just seen that makes him hurry?", passage=G3),
        Q("What does the mother's reply, 'The farm needed you more', suggest?",
          ["She dislikes the farm.", "She is angry with Tabi.", "She puts others first and makes light of her own illness.", "She wants him to leave."], 2,
          ["Nothing suggests this.", "She smiles weakly and speaks gently.", "", "She does not send him away."],
          "She did not call him because she thought his work was more important, and she smiles despite being weak. This shows self-sacrifice.",
          "Character from dialogue", "Interpretation", "Notice 'smiled weakly'.", passage=G3),
        Q("What can be inferred from the untouched bowl of water beside her?",
          ["The water was dirty.", "She was too unwell to drink or to move easily.", "She refused out of anger.", "She had water elsewhere."], 1,
          ["The text does not say so.", "", "Nothing suggests anger.", "Nothing suggests this."],
          "Tabi had filled the bowl that morning, and she lay beside it all day without drinking. She was probably too weak to reach it.",
          "Inference from detail", "Reasoning", "What would a healthy person do with a bowl of water placed nearby?", passage=G3),
        Q("Kofi arrives at school with wet shoes and a dripping umbrella. The most reasonable inference is that",
          ["he was late.", "he had been swimming.", "he was ill.", "it had been raining."], 3,
          ["Nothing says he was late.", "An umbrella points to rain, not swimming.", "Nothing says he was ill.", ""],
          "A dripping umbrella and wet shoes together are strong clues of rain.",
          "Inference from everyday clues", "Application", "What is an umbrella used for?"),
        Q("Which of these CANNOT be safely inferred from the passage?",
          ["Tabi's mother has malaria.", "Tabi works on a farm.", "Tabi is worried.", "The neighbour lives close by."], 0,
          ["", "He 'returned from the farm' and put down his hoe.", "His hurry and silence show worry.", "He 'hurried to the neighbour's door'."],
          "The text never names the illness. We may suspect an illness, but malaria is an unsupported guess (over-reading).",
          "Over-reading", "Analysis", "Which option names something that the text does not state or hint at?", passage=G3),
        Q("Why does Tabi not greet Madam Fonyuy?",
          ["He dislikes her.", "He is shy.", "He is in a hurry and anxious.", "He has forgotten her name."], 2,
          ["Nothing shows dislike; he asks for her help.", "He knocks and speaks directly.", "", "No evidence of forgetting."],
          "He 'did not greet her' and 'only said' what he needed. In the situation, urgency explains his lack of greeting.",
          "Inference of feeling", "Interpretation", "How does the writer describe how he walked to the door?", passage=G3),
    ]))

# ================================================================== R4. Words and figures in context
G4 = (
    "**The First Rains** (an invented descriptive passage)\n\n"
    "For weeks the land had lain parched and silent. The red earth cracked like old pottery, and the leaves on the mango trees hung limp. "
    "Every afternoon the clouds gathered, only to drift away, and farmers watched them with weary eyes. The river beside the school had "
    "shrunk to a muddy thread, and the cattle stood at its edge, patient and thin.\n\n"
    "Then, one evening, the sky darkened with sudden menace. The wind arrived first, rattling the tin roofs and chasing dust along the road. "
    "Thunder grumbled in the distance, a hungry giant clearing its throat. At last the rain fell, drumming on the zinc, and the whole "
    "village seemed to exhale.\n\n"
    "Children raced into the yard, shrieking with delight. Their mothers, pretending to scold, stood laughing in the doorways. By morning the "
    "dust had vanished, and the fields wore a coat of new green. Somewhere a radio played, and an old man sat on his step, turning his face "
    "up to the sky. Hope, which had been shrinking for weeks, had grown again."
)
SETS.append(practice_set(
    module=M_R, topic=T_WORDS, title="Words and figures in context: the first rains",
    lesson="enl1-words-figures-in-context",
    questions=[
        Q("'His voice was so faint that the people at the back found his words inaudible.' The word 'inaudible' means",
          ["angry", "loud", "impossible to hear", "full of mistakes"], 2,
          ["Nothing in the sentence points to anger.", "'Faint' is the opposite of loud.", "", "The sentence is about hearing, not errors."],
          "'So faint that people at the back...' is the clue. Inaudible means not able to be heard.",
          "Context clues", "Application", "What does 'so faint that...' tell you?"),
        Q("In the passage, 'parched' means",
          ["wet", "extremely dry", "burning", "dusty and noisy"], 1,
          ["The land has gone without rain.", "", "Nothing is on fire.", "The word 'silent' contradicts noisy."],
          "The weeks without rain and the cracked earth show extreme dryness.",
          "Context clues", "Application", "What happens to the earth when there is no rain?", passage=G4),
        Q("'The red earth cracked like old pottery' is an example of",
          ["a metaphor", "personification", "hyperbole", "a simile"], 3,
          ["A metaphor would say the earth WAS pottery.", "The earth is not given human actions.", "It does not exaggerate.", ""],
          "The comparison uses 'like', so it is a simile. It shows how dry and brittle the ground was.",
          "Simile", "Recall", "Look for the word 'like'.", passage=G4),
        Q("What does the comparison of the thunder to 'a hungry giant clearing its throat' suggest?",
          ["A deep, threatening rumble", "A joyful sound", "Silence", "The sound of children"], 0,
          ["", "'Hungry' and 'giant' suggest menace, not joy.", "Thunder 'grumbled'; it is not silent.", "The children come later."],
          "A giant clearing its throat makes a low, rough sound. 'Hungry' adds a threatening feeling.",
          "Figurative meaning", "Interpretation", "Think of the sound that a very large person makes when clearing the throat.", passage=G4),
        Q("'The whole village seemed to exhale.' This suggests",
          ["everyone fell ill", "the villagers were angry", "a feeling of relief after long waiting", "the village was noisy"], 2,
          ["Exhale means breathe out; nothing suggests sickness.", "There is no anger in the sentence.", "", "Breathing out is quiet."],
          "We breathe out when tension ends. The rain ends weeks of waiting, so the figure shows relief.",
          "Personification", "Interpretation", "When do people sigh or breathe out slowly?", passage=G4),
        Q("'I've told you a thousand times to close the door!' is an example of",
          ["a simile", "hyperbole", "irony", "onomatopoeia"], 1,
          ["There is no 'like' or 'as'.", "", "The speaker does not say the opposite of what she means.", "It does not imitate a sound."],
          "'A thousand times' deliberately exaggerates to show annoyance. This is hyperbole.",
          "Hyperbole", "Concept", "Has the speaker really counted a thousand?"),
        Q("In 'the sky darkened with sudden menace', the word 'menace' is closest in meaning to",
          ["threat", "joy", "silence", "colour"], 0,
          ["", "The sky darkens before a storm; it is not joyful.", "The wind and thunder follow.", "Menace is not a colour."],
          "The darkening sky, the rattling roofs and the thunder show a threatening mood. 'Menace' means threat.",
          "Context clues", "Application", "What follows the darkening of the sky?", passage=G4),
        Q("'Hope, which had been shrinking for weeks, had grown again.' This is mainly",
          ["a simile", "an oxymoron", "hyperbole", "a metaphor that treats hope like something that can change in size"], 3,
          ["There is no 'like' or 'as'.", "Shrinking and growing are not joined as a contradiction in one phrase.", "It does not exaggerate.", ""],
          "Hope is not a physical object, but it is described as shrinking and growing. This implied comparison is a metaphor.",
          "Metaphor", "Analysis", "Can an idea like hope literally shrink?", passage=G4),
    ]))

# ================================================================== R5. Facts, opinions and sequence
G5 = (
    "**Report on the Clean-up Day at Mimbo Primary School** (an invented report)\n\n"
    "On Saturday 8 March, parents, teachers and pupils of Mimbo Primary School held a clean-up day. The headmistress, Mrs Ngong, "
    "welcomed everyone at 7.30 a.m. and shared the work among five groups. Before the event, the Parents' Association had bought "
    "twenty brooms and ten wheelbarrows.\n\n"
    "By 9.00 a.m. the first group had cleared the football field. The second group then trimmed the hedge along the front fence, while the "
    "third group painted the wall of the Class One building. The pupils worked harder than I expected. After a break for tea and buns at "
    "11.00 a.m., the groups collected sixty-two bags of rubbish, which the council lorry removed at noon.\n\n"
    "The day was a great success, and every school should hold one every term. Mrs Ngong said that the school looked cleaner than it had "
    "for years. Afterwards the Parents' Association proposed to hold the next clean-up on 14 June. By evening, many parents were tired, "
    "yet nearly everyone was happy."
)
SETS.append(practice_set(
    module=M_R, topic=T_FACT, title="Facts, opinions and sequence: a clean-up day report",
    lesson="enl1-facts-opinions-sequence",
    questions=[
        Q("Which of these statements is a fact?",
          ["Mount Cameroon is more than 4,000 metres high.", "Mount Cameroon is the most beautiful mountain.", "Everyone should climb Mount Cameroon.", "Mount Cameroon is too difficult for children."], 0,
          ["", "'Most beautiful' is a judgement.", "'Should' gives advice.", "'Too difficult' is a judgement."],
          "Height can be measured and checked. The other options contain judgements or advice.",
          "Fact and opinion", "Concept", "Which statement could be checked with a measurement?"),
        Q("Which statement from the report is an opinion?",
          ["The Parents' Association bought twenty brooms.", "Mrs Ngong welcomed everyone at 7.30 a.m.", "The pupils worked harder than I expected.", "The groups collected sixty-two bags of rubbish."], 2,
          ["A number that can be checked.", "A time that can be checked.", "", "A count that can be checked."],
          "'Harder than I expected' depends on the writer's expectation. It is a personal judgement.",
          "Fact and opinion", "Concept", "Which statement depends on what the writer thinks?", passage=G5),
        Q("Which event happened FIRST?",
          ["The council lorry removed the rubbish.", "The Parents' Association bought the brooms.", "The groups had tea and buns.", "The second group trimmed the hedge."], 1,
          ["That was at noon.", "", "That was at 11.00 a.m.", "That happened after 9.00 a.m."],
          "'Before the event, the Parents' Association had bought...' places the purchase before the clean-up day. The past perfect 'had bought' also marks an earlier event.",
          "Sequence", "Reasoning", "Look for 'before' and the tense 'had bought'.", passage=G5),
        Q("Which event happened at 11.00 a.m.?",
          ["The rubbish was removed.", "Mrs Ngong welcomed everyone.", "The football field was cleared.", "The groups had a break for tea and buns."], 3,
          ["That was at noon.", "That was at 7.30 a.m.", "That was by 9.00 a.m.", ""],
          "'After a break for tea and buns at 11.00 a.m.' gives the time.",
          "Sequence", "Recall", "Find the time 11.00 a.m. in the report.", passage=G5),
        Q("'Every school should hold one every term.' This sentence is",
          ["an opinion (advice)", "a fact", "a time marker", "a report of a past event"], 0,
          ["", "It cannot be checked as true or false in the way a fact can.", "It has no time marker that orders events.", "It speaks about the future, not the past."],
          "'Should' gives advice, and advice is a judgement about what is best.",
          "Signals of opinion", "Concept", "What does the word 'should' tell you?", passage=G5),
        Q("'The minister believes that the new market will create jobs.' In this sentence, what is a fact?",
          ["The new market will create jobs.", "Jobs are good for towns.", "The minister holds this belief.", "The new market is the best in the region."], 2,
          ["That is the belief itself, a prediction.", "That is a general opinion.", "", "That is not stated in the sentence."],
          "Whether the minister holds the belief can be checked by asking her. What she believes is an opinion.",
          "Reported opinion", "Analysis", "Separate who believes from what is believed."),
        Q("Which is the correct order? (1) The council lorry removed the rubbish. (2) The groups had tea. (3) The first group cleared the football field. (4) Mrs Ngong welcomed everyone.",
          ["3, 4, 2, 1", "4, 2, 3, 1", "4, 1, 3, 2", "4, 3, 2, 1"], 3,
          ["Welcome came first (7.30 a.m.).", "The field was cleared by 9.00, before tea at 11.00.", "Rubbish was removed at noon, after tea.", ""],
          "Welcome 7.30; field by 9.00; tea at 11.00; removal at noon: 4, 3, 2, 1.",
          "Ordering events", "Reasoning", "Give each event its time.", passage=G5),
        Q("Which sentence mixes a fact with a reported opinion?",
          ["The headmistress welcomed everyone at 7.30 a.m.", "Mrs Ngong said that the school looked cleaner than it had for years.", "The council lorry removed the bags at noon.", "The Parents' Association bought twenty brooms."], 1,
          ["It is a fact only.", "", "It is a fact only.", "It is a fact only."],
          "It is a fact that Mrs Ngong said this; what she said ('cleaner than for years') is a judgement, an opinion.",
          "Fact and reported opinion", "Analysis", "Which sentence reports what a person thinks?", passage=G5),
    ]))

# ================================================================== R6. Discourse markers and cohesion
G6 = (
    "**A talk on farmers' cooperatives** (an invented talk)\n\n"
    "Good morning. Many small farmers struggle to earn a fair price for their crops. One reason is that each farmer sells alone, and a lone "
    "seller has little power. For example, a trader may offer a very low price to a farmer who has no other buyer.\n\n"
    "A cooperative solves part of this problem. In a cooperative, farmers combine their harvests and sell together. As a result, they can bargain "
    "for a better price. Moreover, they can share the cost of transport, which is often high. In other words, they spend less to reach the market.\n\n"
    "However, a cooperative is not magic. It works only if members trust their leaders and keep honest records. Some cooperatives have failed "
    "because money was badly managed. Therefore, a new group should choose its treasurer carefully and publish its accounts regularly.\n\n"
    "Finally, remember that a cooperative belongs to its members. If they take part, it can grow; if they do not, it will fade."
)
SETS.append(practice_set(
    module=M_R, topic=T_DISC, title="Discourse markers and cohesion: a talk on cooperatives",
    lesson="enl1-discourse-markers-cohesion",
    questions=[
        Q("'It rained all night; ___, the match was cancelled.' Which word fits best?",
          ["however", "therefore", "for example", "although"], 1,
          ["'However' marks contrast, but the cancellation is a result.", "", "The second clause is not an example.", "'Although' would make the sentence ungrammatical here."],
          "The rain caused the cancellation, so a result marker is needed. 'Therefore' is correct.",
          "Cause and result markers", "Application", "Is the match's cancellation a contrast, an example or a result?"),
        Q("In the talk, 'For example' introduces",
          ["a contrast", "a result", "a conclusion", "an illustration of the point"], 3,
          ["Contrast would use 'however'.", "Result would use 'as a result'.", "Conclusion would use 'finally' or 'in conclusion'.", ""],
          "The trader offering a low price illustrates the point that a lone seller has little power.",
          "Exemplification", "Concept", "What does the sentence after 'For example' do?", passage=G6),
        Q("'As a result, they can bargain for a better price.' The phrase 'As a result' shows",
          ["cause and effect", "contrast", "addition", "sequence"], 0,
          ["", "Nothing is being contrasted.", "'Moreover' adds; 'as a result' does not.", "It does not give an order of time."],
          "Combining the harvests is the cause; bargaining better is the effect.",
          "Result markers", "Concept", "What leads to the better price?", passage=G6),
        Q("'In other words, they spend less to reach the market.' The phrase 'In other words' introduces",
          ["a contrast", "a new topic", "a restatement that explains the previous idea", "a question"], 2,
          ["It repeats rather than contrasts.", "It stays on the same topic.", "", "It is not a question."],
          "The speaker restates 'share the cost of transport' in simpler terms.",
          "Explanation markers", "Concept", "Does the sentence say something new?", passage=G6),
        Q("'However, a cooperative is not magic.' 'However' marks",
          ["an addition", "a limit or contrast with what came before", "a result", "an example"], 1,
          ["An addition would use 'moreover'.", "", "Not a result.", "No example follows."],
          "The previous paragraph praised cooperatives. 'However' introduces a limit.",
          "Contrast markers", "Concept", "How does the third paragraph differ from the second?", passage=G6),
        Q("In 'If they take part, it can grow', who or what does 'they' refer to?",
          ["Farmers in general", "Traders", "Leaders", "Members of the cooperative"], 3,
          ["The sentence is about the cooperative's members.", "Traders are not mentioned in the last paragraph.", "The leaders are not the subject here.", ""],
          "The sentence before says 'a cooperative belongs to its members'. 'They' points back to members.",
          "Pronoun reference", "Application", "Which noun in the previous clause is plural?", passage=G6),
        Q("'The teacher gave out the books. ___ she asked the class to open them.' Which marker fits?",
          ["Then", "However", "Although", "For example"], 0,
          ["", "There is no contrast.", "'Although' needs a contrasting idea.", "The second sentence is not an example."],
          "The sentences describe actions in order, so a sequence marker is needed: 'Then'.",
          "Sequence markers", "Application", "Does the second action come after the first?"),
        Q("In 'If they take part, it can grow', what does 'it' refer to?",
          ["The market", "The treasurer", "The cooperative", "The price"], 2,
          ["The market is not the subject.", "The treasurer is not mentioned in this sentence.", "", "The price is not what grows."],
          "'A cooperative belongs to its members. If they take part, it can grow': 'it' refers to the cooperative.",
          "Pronoun reference", "Application", "What belongs to its members?", passage=G6),
    ]))

# ================================================================== R7. Critical reasoning
G7 = (
    "**Two views on moving the Saturday market** (invented)\n\n"
    "Source A (a shopkeeper): The Saturday market should move to the edge of town. I have run my shop on Main Street for fifteen years, "
    "and I know what happens there. Last month my customers could not park, and two "
    "ambulances were delayed on Main Street. Every town that has moved its weekly market has become calmer and safer. Anyone who "
    "opposes the move simply does not care about public safety. A market at the edge of town would also have room for proper stalls and a car park.\n\n"
    "Source B (a market trader): The Saturday market should stay where it is. My regular customers know where to find me, and many of "
    "them walk from nearby streets. If we move to the edge of town, they will have to pay for taxis, and I will lose sales. I sold more "
    "last Saturday than in the whole of the previous month. A town-centre market is also where many elderly shoppers feel safe, because "
    "everything they need is close by."
)
SETS.append(practice_set(
    module=M_R, topic=T_CRIT, title="Critical reasoning: two views on a market",
    lesson="enl1-critical-reasoning-evaluation",
    questions=[
        Q("Which piece of evidence best supports the claim 'Regular reading improves exam results'?",
          ["My cousin reads a lot and passed.", "Everyone knows it is true.", "A study of 400 students found higher marks among regular readers.", "A radio presenter says so."], 2,
          ["One case is not enough.", "'Everyone knows' is the bandwagon appeal.", "", "A presenter's statement is weaker than measured data."],
          "A large, measured sample is relevant, plentiful and reliable.",
          "Judging evidence", "Concept", "Which source is largest and measured?"),
        Q("What is wrong with 'Anyone who opposes the move simply does not care about public safety'?",
          ["It attacks the people who disagree instead of answering their reasons.", "It follows the crowd.", "It confuses cause and effect.", "It generalises from a single case."], 0,
          ["", "It does not appeal to popularity.", "No cause is claimed.", "It does not rely on one case."],
          "It is a personal attack (and a false dilemma): it assumes opponents must be careless about safety.",
          "Fallacy: personal attack", "Reasoning", "Does it answer the opponents' reasons?", passage=G7),
        Q("What is the main weakness of 'Every town that has moved its weekly market has become calmer and safer'?",
          ["It is too polite.", "It is a question.", "It gives full statistics.", "It makes a sweeping claim about all towns without evidence."], 3,
          ["Politeness is not the problem.", "It is a statement.", "No statistics are given.", ""],
          "It is a hasty generalisation: no towns are named and no data are offered.",
          "Fallacy: hasty generalisation", "Analysis", "How many towns have been checked?", passage=G7),
        Q("What do the two sources have in common?",
          ["Both want the market moved.", "Both rely mainly on personal experience.", "Both give detailed statistics.", "Both ignore customers."], 1,
          ["Source B wants the market to stay.", "", "Neither gives statistics.", "Source B talks about customers."],
          "Source A uses what happened to his customers last month; Source B uses his own sales.",
          "Comparing sources", "Reasoning", "What kind of evidence does each use?", passage=G7),
        Q("Which finding would most weaken Source B's argument?",
          ["Taxis cost money.", "Regular customers like to walk.", "A survey found that in towns that moved their markets, traders' sales stayed the same or rose.", "The market is old."], 2,
          ["That supports Source B.", "That supports Source B.", "", "Age is irrelevant to the claim."],
          "Source B's claim is that moving will lose sales. Evidence that sales did not fall after moves contradicts it.",
          "Weakening an argument", "Reasoning", "Which option directly contradicts 'I will lose sales'?", passage=G7),
        Q("'Either we build a new road or the town will die.' This is mainly",
          ["a false dilemma", "a bandwagon appeal", "a personal attack", "a false cause"], 0,
          ["", "It does not say everyone supports the road.", "No person is attacked.", "No earlier event is wrongly treated as a cause."],
          "It presents only two options and ignores others.",
          "Fallacy: false dilemma", "Concept", "Are there only two possible futures?"),
        Q("Which proposal best answers the concerns of both sources?",
          ["Ban all markets.", "Move the market without asking anyone.", "Do nothing.", "Keep the market where it is, close one street to cars and agree an ambulance route, then review after three months."], 3,
          ["It ignores both sources.", "It ignores Source B's customers.", "It ignores Source A's safety concern.", ""],
          "The proposal responds to Source A's safety and parking concern and Source B's customer concern, and the review gives real evidence.",
          "Proposing solutions", "Application", "Which option respects both safety and customers?", passage=G7),
        Q("Which statement from Source A is a specific, checkable piece of evidence?",
          ["'Every town that has moved its weekly market has become calmer and safer.'", "'Two ambulances were delayed on Main Street.'", "'Anyone who opposes the move simply does not care.'", "'The Saturday market should move.'"], 1,
          ["It is a sweeping claim.", "", "It is a personal attack.", "It is the claim, not evidence."],
          "Two ambulances delayed on a named street in a given month can be checked against records, though one month is a small sample.",
          "Evidence and claim", "Analysis", "Which statement gives a particular event rather than a general claim?", passage=G7),
    ]))

# ================================================================== S1. Vowel sounds
SETS.append(practice_set(
    module=M_S, topic=T_SOUNDS, title="Vowel sounds: monophthongs, diphthongs and triphthongs",
    lesson="enl1-vowel-sounds-rp",
    questions=[
        Q("Which word has the same vowel sound as 'bird' /bɜːd/?",
          ["beard", "heard", "board", "bed"], 1,
          ["'Beard' is /bɪəd/ with the diphthong /ɪə/.", "", "'Board' is /bɔːd/ with /ɔː/.", "'Bed' is /bed/ with the short vowel /e/."],
          "'Heard' is /hɜːd/. The spelling ear and ir differ, but the vowel is /ɜː/ in both.",
          "Vowel /ɜː/", "Recall", "Say the keyword 'nurse' and compare each option with it."),
        Q("Which word begins with a consonant SOUND?",
          ["hour", "honest", "university", "umbrella"], 2,
          ["'Hour' is /ˈaʊə/ and begins with a vowel sound (the h is silent).", "'Honest' is /ˈɒnɪst/ and begins with a vowel sound.", "", "'Umbrella' is /ʌmˈbrelə/ and begins with a vowel sound."],
          "'University' begins with /j/, a consonant sound, so we say 'a university'.",
          "Vowel and consonant sounds", "Concept", "Ask whether you say 'a' or 'an' before the word.",
          feedback="Sounds, not letters, decide."),
        Q("Which word has a different vowel sound from the others?",
          ["cup", "cop", "love", "blood"], 1,
          ["'Cup' is /kʌp/.", "", "'Love' is /lʌv/.", "'Blood' is /blʌd/."],
          "'Cop' is /kɒp/ with /ɒ/. The other three have /ʌ/, even though 'love' and 'blood' are not spelled with u.",
          "Vowels /ʌ/ and /ɒ/", "Reasoning", "Say each word and compare it with 'strut'."),
        Q("Which symbol represents a diphthong?",
          ["/eɪ/", "/iː/", "/ɑː/", "/ɜː/"], 0,
          ["", "/iː/ is a long pure vowel.", "/ɑː/ is a long pure vowel.", "/ɜː/ is a long pure vowel."],
          "A diphthong is written with two vowel symbols for a gliding sound. /eɪ/ glides from /e/ to /ɪ/ as in 'face'.",
          "Diphthongs", "Recall", "Which symbol has two vowel letters joined?"),
        Q("Which pair of words differs ONLY in /ɪ/ and /iː/?",
          ["bad and bed", "cup and cop", "ship and sheep", "bird and board"], 2,
          ["That pair differs in /æ/ and /e/.", "That pair differs in /ʌ/ and /ɒ/.", "", "That pair differs in /ɜː/ and /ɔː/."],
          "'Ship' is /ʃɪp/ and 'sheep' is /ʃiːp/. They form a minimal pair.",
          "Minimal pairs /ɪ/ and /iː/", "Concept", "Find the pair with a short vowel and a long vowel of similar quality."),
        N("How many syllables are in the word 'photographer'?", 4,
          ["Split the word: pho-to-gra-pher.", "The transcription /fəˈtɒɡrəfə/ has four vowel sounds (/ə/, /ɒ/, /ə/, /ə/), so there are four syllables."],
          "Syllables", "Calculation", "Count the vowel sounds, not the letters.", unit="syllables"),
        Q("Which word is usually transcribed with a triphthong (a diphthong plus schwa)?",
          ["hour", "hair", "house", "here"], 0,
          ["", "'Hair' is /heə/, a diphthong.", "'House' is /haʊs/, a diphthong.", "'Here' is /hɪə/, a diphthong."],
          "'Hour' is /ˈaʊə/: the diphthong /aʊ/ plus schwa. In quick speech it may be smoothed (check your dictionary).",
          "Triphthongs", "Recall", "Which word has a diphthong followed by an extra weak vowel?"),
        Q("Which statement about schwa /ə/ is correct?",
          ["It is a long vowel.", "It is always spelled with the letter a.", "It occurs in the word 'cat'.", "It occurs only in unstressed syllables."], 3,
          ["Schwa is short and weak.", "Schwa can be spelled a, e, o, u, er, or and more.", "'Cat' is /kæt/, a stressed syllable with /æ/.", ""],
          "Schwa is the weak vowel of unstressed syllables, such as the first and last syllables of 'banana'.",
          "Schwa", "Concept", "Where in a word is the vowel weak?"),
    ]))

# ================================================================== S2. Consonant sounds
SETS.append(practice_set(
    module=M_S, topic=T_SOUNDS, title="Consonant sounds: voicing, place, -s and -ed",
    lesson="enl1-consonant-sounds-rp",
    questions=[
        Q("How is the final -s pronounced in 'dogs'?",
          ["/z/", "/s/", "/ɪz/", "It is not pronounced."], 0,
          ["", "/s/ follows voiceless sounds such as /k/ in 'books'.", "/ɪz/ follows /s z ʃ ʒ tʃ dʒ/.", "The ending is always pronounced."],
          "'Dogs' is /dɒɡz/. The sound before is the voiced /ɡ/, so the ending is /z/.",
          "-s endings", "Recall", "Is the sound before the s voiced or voiceless?"),
        Q("Which word contains the sound /ʒ/?",
          ["ship", "judge", "church", "measure"], 3,
          ["'Ship' has /ʃ/ (voiceless).", "'Judge' has /dʒ/.", "'Church' has /tʃ/.", ""],
          "'Measure' is /ˈmeʒə/. /ʒ/ is the voiced partner of /ʃ/.",
          "Consonant /ʒ/", "Recall", "Which sound is in 'pleasure' and 'vision'?"),
        N("How many consonant SOUNDS are in 'strong' /strɒŋ/?", 4,
          ["The sounds are /s/, /t/, /r/, /ɒ/, /ŋ/.", "/ɒ/ is a vowel. The consonants are /s/, /t/, /r/ and /ŋ/: four."],
          "Counting sounds", "Calculation", "Count the sounds, not the letters, and leave out the vowel.", unit="consonant sounds"),
        Q("How is the -ed ending pronounced in 'asked' /ɑːskt/?",
          ["/t/", "/d/", "/ɪd/", "/ed/"], 0,
          ["", "/d/ follows voiced sounds.", "/ɪd/ follows /t/ or /d/ only.", "The ending is never /ed/."],
          "After the voiceless /k/ the ending is /t/.",
          "-ed endings", "Application", "Is the sound before the ending voiced or voiceless?"),
        Q("Which sound is the voiced partner of /f/?",
          ["/p/", "/b/", "/v/", "/θ/"], 2,
          ["/p/ is voiceless and made with both lips.", "/b/ is voiced but made with both lips.", "", "/θ/ is voiceless."],
          "/f/ and /v/ are made in the same place (lip and teeth); /v/ is voiced.",
          "Voiced and voiceless pairs", "Concept", "Which sound is made in the same place with the throat buzzing?"),
        Q("In which word do you hear /ŋ/ followed by /ɡ/?",
          ["singer", "finger", "ginger", "hanger"], 1,
          ["'Singer' is /ˈsɪŋə/ with /ŋ/ only.", "", "'Ginger' is /ˈdʒɪndʒə/ with /n/ and /dʒ/.", "'Hanger' is /ˈhæŋə/ with /ŋ/ only."],
          "'Finger' is /ˈfɪŋɡə/. Most -ng- words have no /ɡ/, but 'finger' and 'longer' do.",
          "The sound /ŋ/", "Application", "Compare 'finger' with 'singer'."),
        Q("Which word has NO silent consonant letter?",
          ["knife", "write", "gnat", "table"], 3,
          ["The k is silent.", "The w is silent.", "The g is silent.", ""],
          "'Table' /ˈteɪbl/ pronounces all its consonant letters. The others begin with a silent letter.",
          "Silent letters", "Recall", "Which word begins with all its letters sounded?"),
        Q("Which is the correct transcription of 'watches'?",
          ["/ˈwɒtʃs/", "/ˈwɒtʃɪs/", "/ˈwɒtʃɪz/", "/ˈwɒtʃz/"], 2,
          ["The ending cannot follow /tʃ/ without a vowel.", "After a sibilant the ending is /ɪz/, not /ɪs/.", "", "The ending needs the extra vowel /ɪ/ after /tʃ/."],
          "After /tʃ/ the plural is /ɪz/: /ˈwɒtʃɪz/, a new syllable.",
          "-s after sibilants", "Application", "What follows /s z ʃ ʒ tʃ dʒ/ in the -s rule?"),
    ]))

# ================================================================== S3. Phonemic transcription
SETS.append(practice_set(
    module=M_S, topic=T_TRANS, title="Phonemic transcription: writing and reading sounds",
    lesson="enl1-phonemic-transcription",
    questions=[
        Q("Which is the correct transcription of 'jam'?",
          ["/jæm/", "/dʒæm/", "/ʒæm/", "/tʃæm/"], 1,
          ["The symbol /j/ is the sound in 'yes', not the letter j.", "", "/ʒ/ is the sound in 'measure'.", "/tʃ/ is the sound in 'church'."],
          "'Jam' begins with the affricate /dʒ/ (as in 'judge').",
          "Symbols /dʒ/ and /j/", "Recall", "Which symbol stands for the first sound of 'judge'?"),
        N("How many SOUNDS (phonemes) are in 'thought' /θɔːt/?", 3,
          ["The sounds are /θ/, /ɔː/ and /t/.", "Seven letters, but three sounds."],
          "Counting phonemes", "Calculation", "Count the symbols in the transcription.", unit="sounds"),
        Q("Which word is /θruː/?",
          ["through", "though", "thorough", "true"], 0,
          ["", "'Though' is /ðəʊ/.", "'Thorough' is /ˈθʌrə/.", "'True' is /truː/."],
          "'Through' begins with /θ/, then /r/ and the long vowel /uː/.",
          "Reading a transcription", "Application", "Say each option slowly. Which one begins with the sound /θ/ and ends with /uː/?"),
        Q("Which is the correct transcription of 'wanted'?",
          ["/wɒnˈtɪd/", "/ˈwɒntɪt/", "/ˈwɒntd/", "/ˈwɒntɪd/"], 3,
          ["The stress is on the first syllable, not the second.", "After /t/ the ending is /ɪd/, not /ɪt/.", "A vowel is needed between /t/ and /d/.", ""],
          "'Wanted' has stress on the first syllable and the ending /ɪd/ after /t/: /ˈwɒntɪd/.",
          "Stress and -ed in transcription", "Application", "Where is the stress mark, and what follows /t/ in the -ed rule?"),
        Q("Which word is /ˈnɒlɪdʒ/?",
          ["noble", "novelist", "knowledge", "college"], 2,
          ["'Noble' is /ˈnəʊbl/.", "'Novelist' is /ˈnɒvəlɪst/.", "", "'College' is /ˈkɒlɪdʒ/, which begins with /k/."],
          "'Knowledge' begins with /n/ because the k is silent.",
          "Silent letters", "Application", "Which word has a silent first letter?"),
        Q("Which is the correct transcription of 'about'?",
          ["/ˈəbaʊt/", "/æˈbaʊt/", "/əˈbɒt/", "/əˈbaʊt/"], 3,
          ["The stress is on the second syllable.", "The first vowel is schwa /ə/, not /æ/.", "The last vowel is the diphthong /aʊ/.", ""],
          "'About' has a weak first syllable /ə/ and the stressed syllable /ˈbaʊt/.",
          "Stress mark and schwa", "Application", "Which syllable is the strong one in 'about'?"),
        Q("A student writes /sɪŋɡ/ for 'sing'. What is the mistake?",
          ["He added /ɡ/ after /ŋ/ because of the spelling.", "He used the wrong vowel.", "He forgot the stress mark.", "He left out the slashes."], 0,
          ["", "/ɪ/ is correct.", "A one-syllable word needs no stress mark.", "The slashes are present."],
          "'Sing' is /sɪŋ/ with the single sound /ŋ/ at the end.",
          "Common errors", "Analysis", "Count the sounds you hear at the end of 'sing'."),
        Q("Which is the correct transcription of 'exam'?",
          ["/ˈeksæm/", "/ɪɡzˈæm/", "/ɪɡˈzæm/", "/ɪkˈsæm/"], 2,
          ["The x is /ɡz/ and the stress is on the second syllable.", "The stress mark goes before the stressed syllable, not inside it.", "", "The x here is /ɡz/, not /ks/."],
          "'Exam' has a weak first syllable /ɪɡ/ and the stressed syllable /ˈzæm/: /ɪɡˈzæm/.",
          "Stress and the sound /ɡz/", "Application", "Where does the x become /ɡz/, and which syllable is stronger?"),
    ]))

# ================================================================== S4. Word stress
SETS.append(practice_set(
    module=M_S, topic=T_STRESS, title="Word stress: rules and patterns",
    lesson="enl1-word-stress-rules",
    questions=[
        Q("Which word has its primary stress on the second syllable?",
          ["teacher", "table", "begin", "happy"], 2,
          ["TEAcher is stressed on the first syllable.", "TAble is stressed on the first syllable.", "", "HAPpy is stressed on the first syllable."],
          "'Begin' is a two-syllable verb, beGIN /bɪˈɡɪn/. Two-syllable nouns and adjectives take first-syllable stress.",
          "Two-syllable words", "Recall", "Which of the words is a verb?"),
        N("In the word 'photographer', which syllable (counting from the left) has the primary stress?", 2,
          ["The syllables are pho-TO-gra-pher.", "Primary stress falls on the second syllable: /fəˈtɒɡrəfə/."],
          "Stress in word families", "Calculation", "Compare it with PHOtograph, where the stress is on the first syllable.", unit="(syllable number)"),
        Q("In 'Cameroon will export more cocoa', where is the stress on the verb 'export'?",
          ["on the first syllable (EXport)", "on the second syllable (exPORT)", "equally on both", "on neither"], 1,
          ["That is the noun pattern.", "", "A word has one primary stress.", "Every English word of two or more syllables has a primary stress."],
          "Verbs in noun-verb pairs take stress on the second syllable: exPORT /ɪkˈspɔːt/.",
          "Noun-verb pairs", "Application", "Is 'export' used as a noun or as a verb in the sentence?"),
        Q("Where is the primary stress in 'education'?",
          ["EDucation", "eDUcation", "educaTION", "eduCAtion"], 3,
          ["The first syllable has only secondary stress.", "The syllable before -cation is stressed, not this one.", "The ending -tion is weak.", ""],
          "Words ending in -tion take stress on the syllable before it: eduCAtion /ˌedʒuˈkeɪʃn/.",
          "Suffix -tion", "Application", "Which syllable comes just before -tion?"),
        Q("Which syllable of 'engineer' has the primary stress?",
          ["the first syllable", "the second syllable", "the last syllable", "none; all are equal"], 2,
          ["The first syllable has only secondary stress, /ˌendʒɪˈnɪə/.", "The second syllable is weak (/dʒɪ/).", "", "A word has one primary stress."],
          "The suffix -eer carries the stress: engiNEER.",
          "Suffix -eer", "Recall", "Which suffixes carry the stress themselves?"),
        Q("The speaker says 'a BLACKbird' (stress on the first part). The speaker means",
          ["any bird that is black", "a particular kind of bird (the blackbird)", "a bird painted black", "a bird seen at night"], 1,
          ["That meaning goes with 'a black BIRD'.", "", "No painting is suggested.", "Time of day is not signalled by stress."],
          "Stress on the first part marks a compound noun with its own meaning.",
          "Compound stress and meaning", "Interpretation", "How does 'a black BIRD' differ?"),
        Q("Which of these two-syllable nouns is stressed on the FIRST syllable?",
          ["hotel", "police", "machine", "table"], 3,
          ["Hotel is hoTEL, stressed on the second syllable.", "Police is poLICE, stressed on the second syllable.", "Machine is maCHINE, stressed on the second syllable.", ""],
          "'Table' (TAble) follows the usual rule for two-syllable nouns. 'Hotel', 'police' and 'machine' are exceptions with second-syllable stress.",
          "Exceptions to stress rules", "Analysis", "Three of the words are exceptions. Which one is regular?"),
        Q("Which pair shows the correct stress for these related words?",
          ["eCOnomy – ecoNOMic", "ECOnomy – ECOnomic", "eCOnomy – ECOnomic", "ecoNOMy – ecoNOMic"], 0,
          ["", "In 'economy' the stress is on the second syllable.", "In 'economic' the stress is on the third syllable, before -ic.", "In 'economy' the stress is on the second syllable."],
          "'Economy' is /ɪˈkɒnəmi/ (second syllable). The suffix -ic puts stress before it: ecoNOMic (third syllable).",
          "Stress shift in word families", "Analysis", "Which suffix rule applies to words ending in -ic?"),
    ]))

# ================================================================== S5. Sentence stress and rhythm
SETS.append(practice_set(
    module=M_S, topic=T_SENT, title="Sentence stress, weak forms and rhythm",
    lesson="enl1-sentence-stress-rhythm",
    questions=[
        Q("Which words are normally stressed in 'The children are playing outside'?",
          ["the, are", "the, children", "are, playing, outside", "children, playing, outside"], 3,
          ["These are function words.", "'The' is a function word.", "'Are' is a function word.", ""],
          "Nouns, main verbs and adverbs carry the meaning: CHILdren, PLAYing, outSIDE.",
          "Content and function words", "Concept", "Which words carry the meaning?"),
        Q("What is the weak form of 'and' in 'bread and butter'?",
          ["/ænd/", "/ən/", "/aʊnd/", "/eɪnd/"], 1,
          ["That is the strong form.", "", "That does not exist.", "That does not exist."],
          "In connected speech 'and' reduces to /ən/ (or /n/).",
          "Weak forms", "Recall", "Is 'and' stressed in this phrase?"),
        Q("In the neutral sentence 'She is going to the market', which word carries the nuclear (main) stress?",
          ["she", "going", "market", "to"], 2,
          ["'She' is a pronoun.", "'Going' is a content word, but it is not the last.", "", "'To' is a function word."],
          "In a neutral sentence the main stress falls on the last content word: MARket.",
          "Nuclear stress", "Application", "Which is the last content word?"),
        Q("Which answer to 'Did Kofi buy the red bag?' stresses that someone else bought it?",
          ["No, ANA bought the red bag.", "No, Ana bought the RED bag.", "No, Ana bought the red BAG.", "No, Ana BOUGHT the red bag."], 0,
          ["", "This contrasts the colour.", "This contrasts the item.", "This contrasts the action."],
          "Stress goes on the new or contrasted information. Here the contrast is the person: ANA, not Kofi.",
          "Contrastive stress", "Application", "What is the correction: the person, the colour or the action?"),
        N("How many stressed syllables (beats) are in 'The teacher wants the students to bring their books'?", 5,
          ["The content words are teacher, wants, students, bring, books.", "Each has one stressed syllable (TEAcher, WANTS, STUdents, BRING, BOOKS), so five beats."],
          "Counting beats", "Calculation", "Count only the content words.", unit="beats"),
        Q("In the answer 'Yes, I can', how is 'can' pronounced?",
          ["/kən/", "/kn/", "/kɑːn/", "/kæn/"], 3,
          ["That is the weak form used in the middle of a sentence.", "No such form.", "That is the vowel of 'can't'.", ""],
          "At the end of a short answer the word is stressed, so it takes its strong form /kæn/.",
          "Strong and weak forms", "Application", "Is 'can' stressed in a short answer?"),
        Q("'Stress-timed rhythm' means that",
          ["every syllable has the same length", "stressed syllables come at roughly regular intervals", "every word is stressed", "sentences are always short"], 1,
          ["That describes syllable-timed rhythm.", "", "In stress-timed speech only some words are stressed.", "Length of the sentence is not the point."],
          "In stress-timed speech the beats are roughly evenly spaced and unstressed syllables are squeezed in between.",
          "Rhythm", "Concept", "What stays about equal in time?"),
        Q("'I didn't say HE stole it.' This stress suggests that",
          ["somebody else stole it", "he borrowed it", "the speaker said nothing", "the speaker said it quietly"], 0,
          ["", "That meaning would stress STOLE.", "That meaning would stress SAY.", "Stress does not show loudness of speech in this way."],
          "Stress on HE contrasts him with another person: the speaker did not say he was the thief.",
          "Contrastive stress", "Interpretation", "Which word is contrasted with someone else?"),
    ]))

# ================================================================== S6. Intonation
SETS.append(practice_set(
    module=M_S, topic=T_SENT, title="Intonation: the tunes of English",
    lesson="enl1-intonation-tunes",
    questions=[
        Q("What is the normal tune for 'What is your name?'",
          ["rise", "fall", "fall-rise", "rise-fall"], 1,
          ["A rise is normal for yes/no questions.", "", "A fall-rise shows doubt.", "A rise-fall shows strong feeling."],
          "Wh-questions normally end with a fall.",
          "Intonation of questions", "Recall", "Does the question begin with a question word such as what, where or who?"),
        Q("What is the normal tune for 'Are you ready?'",
          ["fall", "fall-rise", "rise", "rise-fall"], 2,
          ["A fall is normal for wh-questions and statements.", "A fall-rise suggests doubt or reservation.", "", "A rise-fall suggests strong feeling."],
          "A yes/no question normally ends with a rise.",
          "Intonation of questions", "Recall", "Can the question be answered by yes or no?"),
        Q("In 'We bought rice, beans and oil', which tune is normal on 'oil'?",
          ["rise", "fall-rise", "rise-fall", "fall"], 3,
          ["A rise would suggest that more items follow.", "A fall-rise suggests doubt.", "A rise-fall suggests strong feeling.", ""],
          "The last item of a complete list falls to show that the list is finished.",
          "Intonation in lists", "Application", "Does the list continue after 'oil'?"),
        Q("A speaker says the single word 'Maybe' with the pitch pattern shown in the graph. Which description is correct?",
          ["a fall-rise, suggesting doubt or reservation", "a plain fall, suggesting certainty", "a plain rise, asking a question", "a rise-fall, suggesting delight"], 0,
          ["", "A plain fall would only go down.", "A plain rise would only go up.", "A rise-fall would go up and then down."],
          "The line goes down and then up again: a fall-rise, which signals doubt or reservation.",
          "Reading a pitch contour", "Interpretation", "Follow the line from left to right. Does it only go down, only go up or both?",
          diagram="al-enl1-pitch-contour-q.svg",
          diagram_alt="A line graph of the pitch of the voice over the length of one short reply. The line starts high, falls to a low point and then rises again towards the end. A dot marks the main stressed syllable."),
        Q("'It's cold, isn't it?' is said with a falling tag. The speaker wants",
          ["information because she does not know", "agreement because she expects the listener to say yes", "to give an order", "to apologise"], 1,
          ["A rising tag asks a real question.", "", "Nothing in the tag gives an order.", "Nothing signals an apology."],
          "A falling tag expects agreement; a rising tag asks a real question.",
          "Tag questions", "Concept", "Which tune shows that the speaker expects the answer yes?"),
        Q("'Really?' said with a rise-fall most likely shows",
          ["strong feeling, such as surprise or being impressed", "boredom", "doubt", "a plain statement"], 0,
          ["", "Boredom sounds flat.", "Doubt is the job of the fall-rise.", "A plain statement falls."],
          "A rise-fall adds emphasis and feeling.",
          "Rise-fall tune", "Interpretation", "Which tune shows strong feeling?"),
        Q("Which sentence would normally end with a fall?",
          ["Are you coming?", "Is it raining?", "Where do you live?", "Can you help me?"], 2,
          ["A yes/no question normally rises.", "A yes/no question normally rises.", "", "A yes/no question normally rises."],
          "'Where do you live?' is a wh-question, which normally falls.",
          "Falls and rises", "Application", "Which one begins with a question word?"),
        Q("In 'When you finish, call me', the voice usually rises on 'finish'. Why?",
          ["The sentence is not complete.", "It is a yes/no question.", "The speaker is angry.", "The sentence is an order."], 0,
          ["", "It is not a question.", "A rise does not signal anger.", "The final part is an order, but the rise comes earlier."],
          "A rise on an incomplete clause signals that more is to come; the fall comes at the end.",
          "Rise on incomplete clauses", "Reasoning", "Is the first part of the sentence a complete idea?"),
    ]))

# ================================================================== S7. Connected speech and unknown words
SETS.append(practice_set(
    module=M_S, topic=T_CONN, title="Connected speech and spelling of unknown words",
    lesson="enl1-connected-speech-unknown-words",
    questions=[
        Q("In fast speech, 'ten pence' is usually said as",
          ["/ten pens/ every time", "/tem pens/", "/teŋ pens/", "/tel pens/"], 1,
          ["That is possible in careful speech, but it is not what usually happens in fast speech.", "", "/ŋ/ goes with back sounds like /k/, not with /p/.", "/l/ is not a lip sound."],
          "/n/ takes the lip position of /p/ and becomes /m/ (assimilation).",
          "Assimilation", "Application", "Which sound is made with both lips like /p/?"),
        Q("Which is the correct spelling?",
          ["beleive", "belive", "beleave", "believe"], 3,
          ["The rule is i before e (except after c).", "The long vowel needs ie.", "The spelling ea would give a different word pattern.", ""],
          "'Believe' has ie after l, not after c, so the rule 'i before e' applies.",
          "Spelling rule i before e", "Recall", "Is there a c before the vowels?"),
        N("How many syllables are in 'unnecessary'?", 5,
          ["Split: un-nec-es-sa-ry.", "Five syllables."],
          "Syllable splitting", "Calculation", "Split the word into prefix un- and the rest.", unit="syllables"),
        Q("What is the correct past tense of 'visit'?",
          ["visitted", "visitd", "visited", "visiteed"], 2,
          ["The consonant is not doubled because the stress is on the first syllable.", "A vowel is needed before d.", "", "No extra e is needed."],
          "VISit has stress on the first syllable, so the final t is not doubled: visited.",
          "Doubling rule", "Application", "Where is the stress in 'visit'?"),
        Q("In 'far away' /ˌfɑːr əˈweɪ/, the r is heard because",
          ["a vowel sound follows the r", "r is always pronounced in RP", "the word 'far' is stressed", "the spelling is irregular"], 0,
          ["", "RP is non-rhotic; r is silent unless a vowel follows.", "Stress does not decide whether r is heard.", "Spelling is not the reason."],
          "This is linking r: the r joins to the vowel at the start of the next word.",
          "Linking r", "Concept", "What sound begins the word 'away'?"),
        Q("'Did you' becoming /dɪdʒu/ in fast speech is an example of",
          ["elision", "coalescence", "linking r", "a contraction"], 1,
          ["Elision drops a sound; here two sounds blend.", "", "No r is involved.", "A contraction writes two words as one with an apostrophe."],
          "/d/ and /j/ blend into /dʒ/ (coalescence).",
          "Connected speech", "Concept", "Do two sounds merge into a new one?"),
        Q("Which is the correct spelling of the word pronounced /ˈbjuːtɪfl/?",
          ["butiful", "beutiful", "beautiful", "beautyful"], 2,
          ["The /bjuː/ sound is spelled beau.", "The /bjuː/ sound is spelled beau, not beu.", "", "The ending -ful has i before it, not y."],
          "'Beautiful' uses the beau spelling of /bjuː/ and the ending -ful.",
          "Spelling from sound", "Application", "Which spelling gives /bjuː/ in 'beauty'?"),
        Q("Which sound is usually dropped in the everyday pronunciation of 'friendship' /ˈfrenʃɪp/?",
          ["/f/", "/r/", "/n/", "/d/"], 3,
          ["/f/ begins the word.", "/r/ is kept.", "/n/ is kept.", ""],
          "The /d/ is lost between /n/ and /ʃ/ (elision): /ˈfrenʃɪp/.",
          "Elision", "Recall", "Which written consonant does the transcription leave out?"),
    ]))
