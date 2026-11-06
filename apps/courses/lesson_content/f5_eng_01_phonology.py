"""Form 5 English Language: Phonology & Listening Comprehension (9 lessons, one practice set each)."""

from .dsl import *  # noqa: F403

COURSE = ("english-language", "form-5")

M = "Phonology & Listening Comprehension"
T_MONO = "Pure vowel sounds (monophthongs)"
T_DIPH = "Diphthongs and triphthongs"
T_CONS = "Consonant sounds and clusters"
T_SILENT = "Silent letters and homophones"
T_STRESS = "Word stress and sentence stress"
T_INTON = "Intonation patterns"
T_LISTEN = "Listening comprehension strategies and note-taking"

NOAUDIO = ("**A note before we start.** This is a written lesson, so it cannot play sounds. We teach each sound with a keyword "
           "you already know, a description of the mouth, spelling patterns and rules. Always check a sound in a dictionary "
           "that has audio, and ask your teacher or a good English speaker to say the words for you.")

LESSONS = []

# ------------------------------------------------------------------ 1. Short vowels
LESSONS.append(lesson(
    module=M,
    topic=T_MONO,
    title="Short vowels: /ɪ e æ ʌ ɒ ʊ ə/",
    slug="eph-short-vowels",
    minutes=22,
    summary="English has twelve pure vowel sounds. Seven are short: /ɪ e æ ʌ ɒ ʊ ə/. Learn each one by a keyword, the mouth position and the spellings, and do not trust the five vowel letters.",
    objectives=[
        "Explain the difference between a vowel letter and a vowel sound",
        "Say and recognise the seven short vowels using keywords",
        "Use minimal pairs to hear the difference between /ɪ/ and /e/, /e/ and /æ/, /æ/ and /ʌ/, and /ʌ/ and /ɒ/",
        "Use the weak vowel /ə/ (schwa) in unstressed syllables",
    ],
    key_concepts=["Vowel sound", "Monophthong", "Minimal pair", "Short vowels", "Schwa /ə/"],
    blocks=[
        H("Introduction"),
        T("At the beach in Limbe, a boy says, 'I want to see the ship.' His friend laughs and says, 'A sheep? On the sea?' "
          "One small sound changed the meaning. The boy meant /ʃɪp/. His friend heard /ʃiːp/."),
        T("Sounds like these are the subject of this module. Good pronunciation helps you understand people, be understood, and "
          "answer the sound questions in the examination."),
        T(NOAUDIO),
        T("We write sounds between slashes, for example /ɪ/. These symbols come from the **International Phonetic Alphabet** (IPA). "
          "We follow standard British English (often called Received Pronunciation, or RP), which most dictionaries use. "
          "A few words are said differently in different places. We mark doubtful ones 'check your dictionary'."),
        H("Letters are not sounds"),
        D("A **vowel sound** is a speech sound made with the air flowing freely through the mouth, with nothing blocking it. "
          "English writing has only five vowel **letters** (a, e, i, o, u), but standard British English has **twelve pure vowel sounds** "
          "and eight gliding ones (the next lesson).", title="Vowel sound"),
        D("A **monophthong** (or **pure vowel**) is a vowel sound that stays steady from start to finish. "
          "The tongue and the lips do not move while you say it. The word comes from Greek: 'mono' means one.", title="Monophthong"),
        T("Five letters cannot show twelve sounds, so spelling often misleads us. Look at the letter u: it is /ʌ/ in 'cut' but /ʊ/ in 'put'. "
          "Those two words do **not** rhyme. The letter o is /ʌ/ in 'son', /ɒ/ in 'gone' and /ʊ/ in 'woman'."),
        KEY("Four things describe a vowel", "Every vowel can be described by four questions.", cards=[
            ["Tongue height", "Is the tongue high (mouth nearly closed, as in /iː/) or low (mouth wide open, as in /æ/)?"],
            ["Tongue position", "Is the highest part of the tongue at the front, the centre or the back of the mouth?"],
            ["Lips", "Are the lips spread, relaxed or rounded?"],
            ["Length", "Is the sound short or long? (Long vowels are in the next lesson.)"],
        ]),
        IMG("f5en-ph-vowel-chart.svg",
            alt="A vowel chart shaped like a four-sided figure. Close vowels are at the top and open vowels at the bottom; front vowels on the left and back vowels on the right. The twelve pure vowels are placed in their positions.",
            caption="Figure 1. The twelve pure vowels of British English. Moving up means the tongue rises. Moving left means the tongue moves forward. Short vowels are in blue and long vowels in green."),
        H("The seven short vowels"),
        T("Here are the seven short vowels with a keyword and other examples. Say the keyword first. Then say the others and listen for the same sound."),
        CODE("""Symbol  Keyword  More examples
/ɪ/     kit      sit, big, fish, village, women
/e/     dress    bed, ten, head, said, friend, many
/æ/     trap     cat, man, bag, plan, stand
/ʌ/     strut    cup, bus, love, come, money
/ɒ/     lot      hot, dog, box, want, watch
/ʊ/     foot     put, book, good, could, woman
/ə/     about    banana, teacher, today, doctor""", "text", title="Table 1. The short vowels"),
        T("**/ɪ/ (kit).** The tongue is high and forward but relaxed, and the lips are relaxed. It is short. Do not stretch it: /ɪ/ in 'ship' is shorter "
          "and more relaxed than /iː/ in 'sheep'."),
        T("**/e/ (dress).** The mouth is half open and the tongue is in the middle front. It is the vowel of 'bed' and 'ten'."),
        T("**/æ/ (trap).** The mouth is wide open and the tongue is low and forward. Some learners say /e/ here, so 'bad' sounds like 'bed'. "
          "Open the mouth wider for /æ/. Compare: man /mæn/ and men /men/; pan /pæn/ and pen /pen/; sat /sæt/ and set /set/."),
        T("**/ʌ/ (strut).** The mouth is half open, the tongue is in the centre, and the lips are relaxed. It is spelled u in 'cup' and 'bus', "
          "and o in 'come', 'love', 'money', 'son', 'some', 'month', 'mother' and 'brother'. Compare: cup /kʌp/ and cop /kɒp/; cut /kʌt/ and cot /kɒt/; luck /lʌk/ and lock /lɒk/."),
        T("**/ɒ/ (lot).** The mouth is open, the tongue is low and at the back, and the lips are slightly rounded. It is the vowel of 'hot', 'dog' and 'box'. "
          "Compare: hot /hɒt/, hat /hæt/ and hut /hʌt/ are three different words."),
        T("**/ʊ/ (foot).** The lips are rounded and the tongue is high at the back, but relaxed. It is short. It is spelled oo in 'book' and 'good', "
          "u in 'put' and 'full', ou in 'could' and 'would'. Compare: full /fʊl/ and fool /fuːl/; pull /pʊl/ and pool /puːl/."),
        T("**/ə/ (schwa).** This is the weakest vowel. The mouth is relaxed, the tongue is in the centre, and the sound is very short and quiet. "
          "It is the most common vowel in English, but it only appears in **unstressed** syllables: the 'a' of 'about', the 'er' of 'teacher'."),
        D("**Schwa** /ə/ is the neutral, weak vowel of unstressed syllables. It can be spelled in many ways: a in 'about', e in 'taken', "
          "i in 'possible', o in 'lemon', u in 'support', ar in 'sugar', our in 'colour', er in 'teacher'.",
          title="Schwa"),
        T("Notice that in standard British English the letter r is **not** pronounced when no vowel follows it. So 'teacher' is /ˈtiːtʃə/, 'doctor' is /ˈdɒktə/ and 'sugar' is /ˈʃʊɡə/. "
          "Some accents pronounce the r. Both are understood. Be consistent."),
        H("Worked examples"),
        EX("Worked example 1: sort by vowel sound", intro="Sort these words into two groups by their vowel sound: put, cut, foot, but, good, love, book, money.", steps=[
            S("Say each word", text="Say the keywords: 'foot' has /ʊ/. 'Strut' has /ʌ/."),
            S("Group with 'foot' /ʊ/", text="put, foot, good, book. Lips are rounded, the sound is short."),
            S("Group with 'strut' /ʌ/", text="cut, but, love, money. The mouth is half open, lips relaxed. 'Love' and 'money' are spelled with o, but the sound is /ʌ/."),
            S("Answer", text="/ʊ/: put, foot, good, book. /ʌ/: cut, but, love, money."),
        ]),
        EX("Worked example 2: a sound question in Paper 1 style", intro="Which word has the same vowel sound as 'cut'? A. put  B. love  C. hot  D. foot", steps=[
            S("Find the vowel in 'cut'", text="'Cut' is /kʌt/. The vowel is /ʌ/."),
            S("Say each option", text="put /pʊt/, love /lʌv/, hot /hɒt/, foot /fʊt/."),
            S("Compare", text="Only 'love' has /ʌ/. 'Put' and 'foot' have /ʊ/. 'Hot' has /ɒ/."),
            S("Answer", text="B. love."),
        ]),
        MISTAKE("Trusting the letter", "Do not decide a vowel from the spelling alone. 'Put' and 'cut' look alike but rhyme with 'foot' and 'strut'. "
                "Say the word aloud and compare it with a keyword."),
        MISTAKE("Merging two vowels into one", "If 'men' and 'man', or 'cup' and 'cop', sound the same when you say them, the listener may not know which word you mean. "
                "Practise the minimal pairs slowly. A **minimal pair** is two words that differ by one sound only, such as pen and pan."),
        MISTAKE("Saying every vowel at full strength", "In 'teacher', 'banana' and 'today', unstressed syllables use schwa /ə/. "
                "Do not say 'tee-chair'. The word is /ˈtiːtʃə/."),
        QUIZ("Which word has the vowel /ʌ/ (as in 'strut')?",
             ["hot", "foot", "money", "pen"], 2,
             "'Money' is /ˈmʌni/. The letter o stands for /ʌ/ here.",
             hint="Say the keyword 'strut' and then each word. Spelling with o can be tricky.",
             feedback=["'Hot' is /hɒt/ with the rounded vowel /ɒ/.", "'Foot' is /fʊt/ with the short rounded vowel /ʊ/.", "", "'Pen' is /pen/ with /e/."]),
        QUIZ("'Bad' and 'bed' are a minimal pair. Which vowels make the difference?",
             ["/æ/ and /e/", "/ɪ/ and /e/", "/ʌ/ and /æ/", "/ɒ/ and /ʌ/"], 0,
             "'Bad' is /bæd/ and 'bed' is /bed/. Open the mouth wider for /æ/.",
             hint="Say both words slowly. In which one is the mouth more open?",
             feedback=["", "That pair is in 'bid' and 'bed'.", "That pair is in 'bud' and 'bad'.", "That pair is in 'cot' and 'cut'."]),
        TIP("Sound questions appear in Paper 1 (multiple choice): which word has the same vowel as another, or which word has a different sound from the others. "
            "The skill also helps with spelling and with the listening comprehension part.", title="Exam link"),
        PQ("Write three words spelled with the letter o that have the same vowel sound as 'cup'.",
           "Any three of: come, love, money, son, some, month, mother, brother, other, none, done, Monday. All have /ʌ/."),
        PQ("Write one minimal pair for /ɪ/ and /e/ and one for /æ/ and /e/.",
           "/ɪ/ and /e/: bit and bet, sit and set, pin and pen, tin and ten. /æ/ and /e/: man and men, pan and pen, sat and set, bad and bed."),
        PQ("Which is the odd one out, and why? book, good, food, foot.",
           "'Food' is /fuːd/ with the long vowel /uː/. The others have the short vowel /ʊ/."),
        PQ("Mark the schwa /ə/ in 'banana'. How many syllables are there and which one is stressed?",
           "Banana /bəˈnɑːnə/ has three syllables. The first and the last have schwa /ə/. The stressed syllable is the middle one, with the long vowel /ɑː/."),
        SUM("Letters are not sounds: five vowel letters stand for twelve pure vowel sounds in standard British English.",
            "The seven short vowels are /ɪ/ (kit), /e/ (dress), /æ/ (trap), /ʌ/ (strut), /ɒ/ (lot), /ʊ/ (foot) and /ə/ (about).",
            "Minimal pairs such as pen and pan, cup and cop, full and fool show why careful vowels matter.",
            "Schwa /ə/ is the weak vowel of unstressed syllables and is the most common vowel in English."),
    ],
))

# ------------------------------------------------------------------ 2. Long vowels
LESSONS.append(lesson(
    module=M,
    topic=T_MONO,
    title="Long vowels: /iː ɑː ɔː uː ɜː/",
    slug="eph-long-vowels",
    minutes=22,
    summary="The five long pure vowels are /iː ɑː ɔː uː ɜː/. This lesson teaches each with a keyword, mouth position and spelling patterns, and shows how length separates words such as ship and sheep.",
    objectives=[
        "Say and recognise the five long vowels using keywords",
        "Contrast short and long vowels in minimal pairs (ship and sheep, full and fool, cot and caught)",
        "Use common spelling patterns to predict /ɑː/, /ɔː/, /uː/ and /ɜː/",
        "Explain why vowel length helps the listener tell words apart",
    ],
    key_concepts=["Long vowel", "Vowel length mark /ː/", "Short and long contrast", "Spelling patterns", "Silent r in British English"],
    blocks=[
        H("Introduction"),
        T("A girl in Bamenda tells her friend, 'I will leave on Monday.' Her friend writes in her diary, 'She will live on Monday.' "
          "The words 'leave' /liːv/ and 'live' /lɪv/ differ only in the vowel. The first is long and the second is short."),
        T("In the last lesson we met seven short vowels. English has five **long** vowels as well. We mark a long vowel with the length mark /ː/ after the symbol."),
        T(NOAUDIO),
        D("A **long vowel** is a pure vowel that is held longer than a short vowel. It has the mark /ː/ in its symbol: /iː/, /ɑː/, /ɔː/, /uː/, /ɜː/. "
          "Length is not the only difference. A long vowel is usually also made with the tongue in a slightly different position, "
          "so 'sheep' has a longer and also a tenser vowel than 'ship'.", title="Long vowel"),
        IMG("f5en-ph-vowel-chart.svg",
            alt="The vowel chart again. The long vowels (in green) are /iː/ at the top front, /uː/ at the top back, /ɜː/ in the centre, /ɔː/ at the back and /ɑː/ at the bottom back.",
            caption="Figure 1. The long vowels are in green. Notice /iː/ and /uː/ are higher than /ɪ/ and /ʊ/."),
        H("The five long vowels"),
        CODE("""Symbol  Keyword  More examples
/iː/    fleece   see, tea, key, people, machine, receive
/ɑː/    start    car, father, park, large, class, laugh
/ɔː/    thought  more, door, four, saw, call, talk, water
/uː/    goose    food, moon, blue, too, true, fruit, group
/ɜː/    nurse    bird, girl, turn, work, learn, word, world""", "text", title="Table 1. The long vowels"),
        T("**/iː/ (fleece).** The tongue is high and forward and the lips are spread, as in a smile. It is spelled ee (see), ea (tea), ey (key), ie (field), "
          "and e-e (these). Compare ship /ʃɪp/ and sheep /ʃiːp/; sit /sɪt/ and seat /siːt/; fill /fɪl/ and feel /fiːl/."),
        T("**/ɑː/ (start).** The mouth is wide open and the tongue is low and at the back. It is spelled ar (car, park), "
          "a before s, f, th or n plus a consonant (class, last, path, dance), and al (calm, half). Compare cat /kæt/ and cart /kɑːt/; "
          "back /bæk/ and bark /bɑːk/. In some words the British and American pronunciations differ, so 'check your dictionary' for words such as 'dance' and 'answer'."),
        T("**/ɔː/ (thought).** The lips are rounded and the tongue is back, mid-height. It is spelled or (more, sport), aw and au (saw, daughter), "
          "all (call, all), al (talk, walk) and our or oor (four, door). After w, the letters 'ar' also give /ɔː/ in 'war', 'warm' and 'water'. "
          "Compare cot /kɒt/ and caught /kɔːt/; shot /ʃɒt/ and short /ʃɔːt/."),
        T("**/uː/ (goose).** The lips are rounded and the tongue is high at the back. It is spelled oo (food, moon), ue (blue, true), ui (fruit, juice), "
          "o (do, to), ou (soup, group) and ew (grew). Compare full /fʊl/ and fool /fuːl/; pull /pʊl/ and pool /puːl/; look /lʊk/ and Luke /luːk/."),
        T("**/ɜː/ (nurse).** The tongue is in the centre, the lips are relaxed and not rounded, and the vowel is long. It is spelled er (her, serve), ir (bird, girl), "
          "ur (turn, hurt), ear (learn, early, earth) and **or after w** (work, word, world, worm). Compare bud /bʌd/ and bird /bɜːd/; hut /hʌt/ and hurt /hɜːt/; "
          "heart /hɑːt/ and hurt /hɜːt/; shirt /ʃɜːt/ and short /ʃɔːt/."),
        KEY("Silent r", "In standard British English the letter r after a vowel is not pronounced unless another vowel follows.", cards=[
            ["Not pronounced", "car /kɑː/, more /mɔː/, bird /bɜːd/, her /hɜː/, door /dɔː/"],
            ["Pronounced", "carry /ˈkæri/, more of /ˈmɔːr əv/ (joined), red /red/, around /əˈraʊnd/"],
        ], note="Some English accents, including the speech of many Cameroonians, do pronounce this r. Both are understood; keep one style."),
        H("Length depends on the next sound"),
        T("A vowel is shorter before a voiceless consonant and longer before a voiced one. So the vowel in 'seat' /siːt/ is shorter than the vowel in 'seed' /siːd/. "
          "Listeners use this length to decide whether you said 'seat' or 'seed', 'bet' or 'bed', 'back' or 'bag'. "
          "(Voiced and voiceless consonants are explained in the lesson on consonants.)"),
        H("Worked examples"),
        EX("Worked example 1: same vowel as 'bird'", intro="Which word has the same vowel sound as 'bird'? A. beard  B. board  C. word  D. bad", steps=[
            S("Find the vowel in 'bird'", text="'Bird' is /bɜːd/. The vowel is /ɜː/."),
            S("Say each option", text="beard /bɪəd/, board /bɔːd/, word /wɜːd/, bad /bæd/."),
            S("Compare", text="'Word' is spelled with or after w. That pattern gives /ɜː/."),
            S("Answer", text="C. word."),
        ]),
        EX("Worked example 2: or after w", intro="Say the vowel in: for, work, sport, word, short, world. Which words have /ɜː/?", steps=[
            S("Spot the pattern", text="The spelling 'or' normally gives /ɔː/: for /fɔː/, sport /spɔːt/, short /ʃɔːt/."),
            S("Look for w before or", text="'Work' /wɜːk/, 'word' /wɜːd/ and 'world' /wɜːld/ have w before 'or'. In these words 'or' is /ɜː/."),
            S("Remember exceptions", text="Some words with wor- do not follow the rule: 'worn' is /wɔːn/. Also 'sword' is /sɔːd/ (the w is silent). 'Check your dictionary' when in doubt."),
            S("Answer", text="work, word and world have /ɜː/. for, sport and short have /ɔː/."),
        ]),
        MISTAKE("Making long vowels short", "If 'sheep' sounds like 'ship', 'fool' like 'full' or 'leave' like 'live', the listener may choose the wrong word. "
                "Hold the long vowel a little longer and spread the lips for /iː/."),
        MISTAKE("Saying 'work' like 'walk'", "'Work' /wɜːk/ has the central vowel /ɜː/. 'Walk' /wɔːk/ has a rounded back vowel and a silent l. "
                "Do not round the lips in 'work', 'word' and 'world'."),
        MISTAKE("Using the same vowel for /ɑː/ and /æ/", "'Cart' /kɑːt/ and 'cat' /kæt/ are different words. For /ɑː/, open the mouth wide and hold it. "
                "For /æ/, the sound is shorter and the tongue is further forward."),
        QUIZ("Which word has the vowel /ɜː/ as in 'nurse'?",
             ["walk", "wake", "work", "woke"], 2,
             "'Work' is /wɜːk/. The spelling 'or' after w gives /ɜː/.",
             hint="Look for a w followed by 'or'.",
             feedback=["'Walk' is /wɔːk/. It has the rounded vowel /ɔː/ and a silent l.", "'Wake' is /weɪk/, a diphthong.", "", "'Woke' is /wəʊk/, a diphthong."]),
        QUIZ("Which pair is a short-vowel and long-vowel minimal pair?",
             ["pull and pool", "bed and bad", "bird and word", "cheap and sheep"], 0,
             "'Pull' /pʊl/ has the short vowel /ʊ/ and 'pool' /puːl/ has the long vowel /uː/. Only the vowel changes.",
             hint="A minimal pair differs by ONE sound, and here that sound must be a short vowel against a long one.",
             feedback=["", "Both vowels in 'bed' /e/ and 'bad' /æ/ are short.", "Both have /ɜː/. They differ only in the first consonant.", "They differ in the first consonant, not in the vowel."]),
        TIP("Questions on long and short vowels appear in Paper 1 (multiple choice): same-sound questions, odd-one-out and homophone choices. "
            "A spelling rule such as 'or after w' saves time because you can work out the sound without hearing it.", title="Exam link"),
        PQ("Explain the difference in meaning between 'I live in Buea' and 'I leave in Buea', and give the vowel sounds.",
           "'Live' is /lɪv/ with the short vowel /ɪ/ and means to have your home there. 'Leave' is /liːv/ with the long vowel /iː/ and means to go away. "
           "'I leave in Buea' would be an odd sentence, so the speaker needs the correct vowel."),
        PQ("Write four words that have the vowel /ɑː/, and say two spelling patterns that give it.",
           "For example: car, park, large, father, class, laugh, calm, half. Patterns: ar (car, park) and al before m or f (calm, half), or a before s, f, th or n plus a consonant (class, path, dance)."),
        PQ("Which word is the odd one out and why? short, port, work, door.",
           "'Work' is /wɜːk/ with /ɜː/. The others have /ɔː/: short /ʃɔːt/, port /pɔːt/, door /dɔː/."),
        PQ("Is the vowel in 'seed' longer or shorter than the vowel in 'seat'? Why does this matter?",
           "It is longer, because it comes before a voiced consonant /d/. Listeners use the vowel length to tell 'seed' and 'seat' apart."),
        SUM("The five long pure vowels are /iː/ (fleece), /ɑː/ (start), /ɔː/ (thought), /uː/ (goose) and /ɜː/ (nurse).",
            "Pairs like ship and sheep, full and fool, cot and caught change meaning only by vowel length and quality.",
            "Spelling patterns help: ar gives /ɑː/, or gives /ɔː/ (but /ɜː/ after w), ir and ur give /ɜː/, oo and ue often give /uː/.",
            "A vowel is longer before a voiced consonant (seed) than before a voiceless one (seat)."),
    ],
))

# ------------------------------------------------------------------ 3. Diphthongs and triphthongs
LESSONS.append(lesson(
    module=M,
    topic=T_DIPH,
    title="Diphthongs and triphthongs: gliding vowels",
    slug="eph-diphthongs-triphthongs",
    minutes=24,
    summary="A diphthong glides from one vowel to another inside one syllable. English has eight: /eɪ aɪ ɔɪ əʊ aʊ ɪə eə ʊə/. A triphthong adds schwa to a closing diphthong, as in fire, hour, player, royal and lower.",
    objectives=[
        "Define diphthong and triphthong and say what makes them different from pure vowels",
        "Name the eight diphthongs with a keyword for each",
        "Use spelling patterns and minimal pairs (no and now, here and hair) to choose the right diphthong",
        "Recognise the five triphthongs in words such as fire, hour, player, royal and lower",
    ],
    key_concepts=["Diphthong", "Closing and centring diphthongs", "Triphthong", "Glide", "Spelling and sound"],
    blocks=[
        H("Introduction"),
        T("At a bus station in Yaoundé, the ticket seller shouts, 'Now!' The driver understands 'No!' and refuses to start the bus. "
          "The two words are /naʊ/ and /nəʊ/. They differ in the vowel, and both vowels are **gliding** vowels."),
        T(NOAUDIO),
        D("A **diphthong** is a vowel sound that glides from one vowel position to another inside one syllable. "
          "The word comes from Greek: 'di' means two. The tongue and lips move while you say it. In the word 'boy', the mouth starts at /ɔ/ and glides towards /ɪ/.",
          title="Diphthong"),
        T("The first part is longer, louder and clearer. The second part is short and weak. It shows the direction of the glide."),
        H("The eight diphthongs"),
        T("Standard British English has eight diphthongs. They fall into three groups according to where the glide goes."),
        CODE("""Group                 Symbol  Keyword  More examples
Glide towards /ɪ/     /eɪ/    face     day, make, rain, eight, they, great
                      /aɪ/    price    my, time, night, die, buy, high
                      /ɔɪ/    choice   boy, toy, coin, oil, enjoy, voice
Glide towards /ʊ/     /əʊ/    goat     go, no, home, road, know, slow
                      /aʊ/    mouth    now, house, out, down, brown, town
Glide towards /ə/     /ɪə/    near     here, ear, beer, idea, cheer
                      /eə/    square   hair, care, there, chair, where, bear
                      /ʊə/    cure     poor, tour, pure, cure, jury""", "text", title="Table 1. The eight diphthongs"),
        T("**Closing diphthongs** (towards /ɪ/ or /ʊ/): the mouth closes a little as the vowel moves. "
          "**Centring diphthongs** (towards /ə/): the glide ends in the centre of the mouth."),
        T("**A note on /ʊə/.** Many speakers now say /ɔː/ in words such as 'poor', 'sure' and 'your' (so 'sure' is /ʃɔː/). Others keep /ʊə/. "
          "Both are accepted: check your dictionary. 'Tour' and 'cure' usually keep /ʊə/."),
        H("Spelling patterns"),
        T("Several spellings give the same diphthong, and one spelling can give different sounds. These patterns help you decide."),
        KEY("Common spellings of the diphthongs", "Learn the patterns, then check each word.", cards=[
            ["/eɪ/", "a-e (make, name), ai (rain), ay (day), ey (they), ei (eight), ea (great, break)"],
            ["/aɪ/", "i-e (time), y (my), igh (night), ie (die), uy (buy)"],
            ["/ɔɪ/", "oy (boy, enjoy) and oi (coin, oil)"],
            ["/əʊ/", "o (go, no), o-e (home), oa (road, boat), ow (know, slow), ough (though)"],
            ["/aʊ/", "ow (now, down, brown) and ou (house, out)"],
            ["/ɪə/", "ere (here), ear (ear, near), eer (beer, cheer)"],
            ["/eə/", "air (hair), are (care), ere (there, where), ear (bear)"],
        ]),
        T("Watch the spelling **ow**. It is /aʊ/ in 'now' and 'down' but /əʊ/ in 'know' and 'slow'. Watch **ear** too: "
          "it is /ɪə/ in 'near', /eə/ in 'bear' and /ɜː/ in 'learn'."),
        H("Minimal pairs for diphthongs"),
        CODE("""no    /nəʊ/   now     /naʊ/
day   /deɪ/   die     /daɪ/
bay   /beɪ/   boy     /bɔɪ/
here  /hɪə/   hair    /heə/
code  /kəʊd/  cord    /kɔːd/
boat  /bəʊt/  bought  /bɔːt/
wait  /weɪt/  white   /waɪt/
pier  /pɪə/   pear    /peə/""", "text", title="Table 2. Pairs to practise"),
        T("Some speakers of English in Cameroon say 'day' and 'go' with a single steady vowel, like /e/ or /o/. This is easily understood in conversation, "
          "but the full glide makes the pairs above clearer. Practise by starting at the first vowel and sliding to the second."),
        H("Triphthongs"),
        D("A **triphthong** is a vowel sound with three parts: a closing diphthong plus schwa /ə/. "
          "There are five, and they sound like two syllables squeezed into one or like a diphthong followed by a very short schwa.", title="Triphthong"),
        CODE("""Sounds        Symbol   Examples
/eɪ/ + /ə/    /eɪə/    player, layer
/aɪ/ + /ə/    /aɪə/    fire, tyre, higher
/ɔɪ/ + /ə/    /ɔɪə/    royal, loyal, employer
/əʊ/ + /ə/    /əʊə/    lower, slower, grower
/aʊ/ + /ə/    /aʊə/    hour, flower, power, tower""", "text", title="Table 3. The five triphthongs"),
        T("In quick speech, many people smooth the triphthong. 'Fire' /faɪə/ may sound like /faə/, and 'hour' /aʊə/ may sound like /ɑː/. "
          "Dictionaries also differ on whether 'fire' and 'hour' have one or two syllables, so check your dictionary. "
          "'Hour' and 'our' are usually said the same way, and 'flower' and 'flour' sound the same."),
        H("Worked examples"),
        EX("Worked example 1: same diphthong", intro="Which word has the same vowel sound as 'late'? A. let  B. eight  C. light  D. lot", steps=[
            S("Find the vowel in 'late'", text="'Late' is /leɪt/. The vowel is the diphthong /eɪ/."),
            S("Say each option", text="let /let/, eight /eɪt/, light /laɪt/, lot /lɒt/."),
            S("Compare", text="'Eight' has /eɪ/. 'Let' has the short vowel /e/, 'light' has /aɪ/ and 'lot' has /ɒ/."),
            S("Answer", text="B. eight. The spelling is different (ei) but the sound is the same."),
        ]),
        EX("Worked example 2: name the vowel sound", intro="Name the vowel sound in each word: boat, buy, bear, hour, near.", steps=[
            S("boat", text="/bəʊt/. The vowel is /əʊ/."),
            S("buy", text="/baɪ/. The vowel is /aɪ/. The spelling uy gives /aɪ/."),
            S("bear", text="/beə/. The vowel is the centring diphthong /eə/."),
            S("hour", text="/ˈaʊə/. It is the triphthong /aʊə/, which is /aʊ/ with /ə/ added."),
            S("near", text="/nɪə/. The vowel is /ɪə/. Compare with 'bear'."),
        ]),
        MISTAKE("Making a diphthong a pure vowel", "If 'late' becomes /let/ ('let') or 'go' becomes /ɡo/ without the glide, you may produce a different word, "
                "or listeners may take longer to understand. Start at the first vowel and glide to the second."),
        MISTAKE("Mixing /ɪə/ and /eə/", "'Here' /hɪə/ and 'hair' /heə/ are different words. For /ɪə/ the glide starts with /ɪ/. For /eə/ it starts with /e/. "
                "Practise: beer and bear, cheer and chair, pier and pear."),
        MISTAKE("Giving one sound to one spelling", "The spelling ea has at least seven sounds: tea /iː/, head /e/, great /eɪ/, bear /eə/, near /ɪə/, heart /ɑː/ and learn /ɜː/. "
                "Learn the word, not only the spelling."),
        QUIZ("Which word has the same vowel as 'now'?",
             ["go", "saw", "show", "town"], 3,
             "'Now' is /naʊ/ and 'town' is /taʊn/. Both have the diphthong /aʊ/.",
             hint="Say 'now' slowly. The mouth starts open and the lips round at the end.",
             feedback=["'Go' is /ɡəʊ/. It glides towards /ʊ/ too, but from a different starting vowel.", "'Saw' is /sɔː/, a long pure vowel.",
                       "'Show' is /ʃəʊ/. The spelling ow is the same as in 'now' but the sound is /əʊ/.", ""]),
        QUIZ("A triphthong is a diphthong with which sound added?",
             ["/ɪ/", "/ʊ/", "/ə/", "/iː/"], 2,
             "A triphthong is a closing diphthong plus schwa: /eɪə/, /aɪə/, /ɔɪə/, /əʊə/, /aʊə/.",
             hint="Think of fire /faɪə/, hour /aʊə/ and player /pleɪə/. What is the last sound?",
             feedback=["/ɪ/ is the end of the first part (the diphthong), not the added sound.", "/ʊ/ is the end of /əʊ/ and /aʊ/, not the added sound.", "", "/iː/ is a long pure vowel."]),
        TIP("Questions on diphthongs and triphthongs come in Paper 1 (multiple choice): same-sound and odd-one-out items, and choosing the word that has a given sound. "
            "Spelling patterns help: learn the common ones so you can decide even when you cannot hear the word.", title="Exam link"),
        PQ("Name the eight diphthongs and give one keyword for each.",
           "/eɪ/ face, /aɪ/ price, /ɔɪ/ choice, /əʊ/ goat, /aʊ/ mouth, /ɪə/ near, /eə/ square, /ʊə/ cure. "
           "(/ʊə/ is increasingly replaced by /ɔː/ in words such as 'poor' and 'sure'.)"),
        PQ("Write the minimal pair that shows a difference between /əʊ/ and /aʊ/, and say how the two vowels differ.",
           "No /nəʊ/ and now /naʊ/. In /əʊ/ the mouth starts in the centre and glides back and up with rounded lips. "
           "In /aʊ/ the mouth starts wide open and then glides towards /ʊ/."),
        PQ("Give three words that have the spelling 'ea' but three different sounds, and write each sound.",
           "For example: tea /iː/, head /e/, great /eɪ/, bear /eə/, near /ɪə/, heart /ɑː/. Any three."),
        PQ("Which two words sound the same: hour, our, hair, her? What kind of vowel sound do they share?",
           "'Hour' and 'our' sound the same (usually /ˈaʊə/). They share the triphthong /aʊə/, which is the diphthong /aʊ/ followed by schwa."),
        SUM("A diphthong is a gliding vowel in one syllable. English has eight: /eɪ aɪ ɔɪ/ (towards /ɪ/), /əʊ aʊ/ (towards /ʊ/) and /ɪə eə ʊə/ (towards /ə/).",
            "A triphthong is a closing diphthong plus schwa: /eɪə aɪə ɔɪə əʊə aʊə/, as in player, fire, royal, lower and hour.",
            "The same spelling can give different sounds (ow in now and know; ea in tea, great, bear, near), so learn the word.",
            "Minimal pairs such as no and now, here and hair, wait and white show that the glide changes meaning."),
    ],
))

# ------------------------------------------------------------------ 4. Consonant sounds
LESSONS.append(lesson(
    module=M,
    topic=T_CONS,
    title="The 24 consonant sounds",
    slug="eph-consonant-sounds",
    minutes=24,
    summary="English has 24 consonant sounds. Learn them by voicing (voiced or voiceless), place and manner, and pay special attention to /θ ð ʃ ʒ tʃ dʒ ŋ/, which are written with two letters or are not like any letter of the alphabet.",
    objectives=[
        "Define a consonant sound and say what voiced and voiceless mean",
        "Name the 24 consonants and group them as plosives, fricatives, affricates, nasals and approximants",
        "Distinguish easily confused pairs such as /θ/ and /t/, /ð/ and /d/, /v/ and /b/, /ʃ/ and /tʃ/, /l/ and /r/",
        "Link spelling to sound for th, ch, sh, s, g, c and ng",
    ],
    key_concepts=["Consonant sound", "Voiced and voiceless", "Plosive, fricative, affricate, nasal", "Minimal pair", "Spelling and sound"],
    blocks=[
        H("Introduction"),
        T("A market woman in Mbouda says, 'Three tomatoes, please.' If the seller hears 'tree tomatoes', the customer may get a very odd order. "
          "The sound /θ/ at the start of 'three' is one that many learners replace with /t/ or /s/ or /f/."),
        T("Consonants carry much of the meaning in English. This lesson gives you the whole set of 24."),
        T(NOAUDIO),
        D("A **consonant sound** is a speech sound made when the air is partly or fully blocked in the mouth or throat. "
          "English has 24 consonant sounds but only 21 consonant letters, so some sounds need two letters (sh, ch, th, ng) and some letters have more than one sound (c, g, s, x).",
          title="Consonant sound"),
        H("Voiced and voiceless"),
        D("A consonant is **voiced** when the vocal cords (in the throat) vibrate while you say it. It is **voiceless** when they do not vibrate. "
          "Test: put your fingers on your throat and say /s/ and then /z/. With /z/ you feel a buzz. With /s/ you do not. You can also close your ears with your hands and listen.",
          title="Voiced and voiceless"),
        T("Many consonants come in pairs that are made in exactly the same way. They differ only by voice."),
        CODE("""Voiceless   Voiced     Example pair
/p/         /b/        pin / bin
/t/         /d/        ten / den
/k/         /ɡ/        came / game
/f/         /v/        fan / van
/θ/         /ð/        thigh / thy
/s/         /z/        sue / zoo
/ʃ/         /ʒ/        (no common pair)
/tʃ/        /dʒ/       cheap / jeep""", "text", title="Table 1. Pairs that differ by voice"),
        H("All 24 consonants"),
        T("Grouping them by **manner** (how the air is released) makes them easier to remember."),
        CODE("""Group          Voiceless          Voiced
Plosives       p  t  k            b  d  g
Fricatives     f  θ  s  ʃ  h      v  ð  z  ʒ
Affricates     tʃ                 dʒ
Nasals                            m  n  ŋ
Approximants                      l  r  j  w""", "text", title="Table 2. The 24 consonants (IPA symbols)"),
        KEY("What each group means", "The names tell you how the air moves.", cards=[
            ["Plosives", "The air is stopped completely and then released with a small burst: p, b, t, d, k, g."],
            ["Fricatives", "The air is squeezed through a narrow gap and makes friction: f, v, θ, ð, s, z, ʃ, ʒ, h."],
            ["Affricates", "A plosive followed at once by a fricative: tʃ (church) and dʒ (judge)."],
            ["Nasals", "The air goes out through the nose: m, n, ŋ."],
            ["Approximants", "The mouth is nearly open and the air flows freely: l, r, j (yes) and w."],
        ]),
        H("The harder sounds, with keywords"),
        T("**/θ/ and /ð/.** Put the tip of the tongue lightly between or just behind the upper teeth and let the air pass. /θ/ is voiceless: think, three, thank, thin, bath, mouth. "
          "/ð/ is voiced: this, that, the, they, mother, brother, weather. Do not say 'tink' or 'dis'. Compare: thin /θɪn/ and tin /tɪn/; three /θriː/ and tree /triː/; then /ðen/ and den /den/."),
        T("**/ʃ/ and /tʃ/.** /ʃ/ (sh) is a long hiss: ship, she, wash, nation, sugar, machine. /tʃ/ (ch) is a short stop plus hiss: chin, church, watch, teacher. "
          "Compare: ship /ʃɪp/ and chip /tʃɪp/; sheep /ʃiːp/ and cheap /tʃiːp/; wash /wɒʃ/ and watch /wɒtʃ/."),
        T("**/ʒ/ and /dʒ/.** /ʒ/ is the voiced partner of /ʃ/. It is rare at the beginning of English words and is heard in measure, vision, television, pleasure and usual. "
          "/dʒ/ is spelled j, g or dge: judge, jam, age, bridge, giant, major. Compare: cheap /tʃiːp/ and jeep /dʒiːp/; chin /tʃɪn/ and gin /dʒɪn/."),
        T("**/v/ and /b/, /f/ and /p/.** For /v/ and /f/ the top teeth touch the lower lip. For /b/ and /p/ the two lips close. Compare: very /ˈveri/ and berry /ˈberi/; vote /vəʊt/ and boat /bəʊt/; "
          "leaf /liːf/ and leave /liːv/; fan /fæn/ and pan /pæn/."),
        T("**/ŋ/.** The back of the tongue touches the soft part of the roof of the mouth and the air goes through the nose. It is the sound of ng in 'sing' and n before k in 'sink' /sɪŋk/. "
          "At the end of 'sing', 'long' and 'thing' there is **no** /ɡ/. Compare: sin /sɪn/ and sing /sɪŋ/. "
          "Some words do have /ɡ/ after /ŋ/: finger /ˈfɪŋɡə/ and hungry /ˈhʌŋɡri/, but singer is /ˈsɪŋə/."),
        T("**/l/ and /r/.** For /l/ the tip of the tongue touches the ridge behind the upper teeth. For /r/ the tongue tip curls back near the ridge and does not touch it. "
          "Compare: light /laɪt/ and right /raɪt/; lock /lɒk/ and rock /rɒk/; play /pleɪ/ and pray /preɪ/."),
        T("**/h/ and /j/.** /h/ is a breath of air from the throat: hair, hat, who. Do not drop it ('hair' is not 'air'), and do not add it to words that start with a vowel ('air' is not 'hair'). "
          "/j/ is the first sound in 'yes' /jes/, 'you' /juː/ and also in 'use' /juːz/ and 'university'."),
        H("Spelling and sound"),
        KEY("Patterns to remember", "One spelling, more than one sound. Check unusual words.", cards=[
            ["th", "/ð/ in this, that, the, they, mother, brother; /θ/ in think, three, thank, bath. Pairs: breath /breθ/ (noun) and breathe /briːð/ (verb)."],
            ["ch", "/tʃ/ in chair, church, teacher; /k/ in school and chemistry; /ʃ/ in machine."],
            ["c", "/s/ before e, i or y (city, face, cycle); /k/ before a, o, u (cat, cold, cut)."],
            ["g", "/dʒ/ before e, i or y in many words (giant, age, magic); /ɡ/ in get, give, girl, go."],
            ["s", "/s/ in see, bus; /z/ in rose, easy, dogs; /ʃ/ in sugar, sure; /ʒ/ in measure and vision."],
        ]),
        H("Worked examples"),
        EX("Worked example 1: voiced or voiceless?", intro="Say whether each sound is voiced or voiceless: /s/, /z/, /ʃ/, /dʒ/, /m/, /f/.", steps=[
            S("Use the throat test", text="Put your fingers on your throat. If you feel a buzz, the sound is voiced."),
            S("Voiceless", text="/s/ (see), /ʃ/ (she) and /f/ (fan). Only air, no buzz."),
            S("Voiced", text="/z/ (zoo), /dʒ/ (judge) and /m/ (man). You feel the vibration."),
            S("Answer", text="Voiceless: /s/, /ʃ/, /f/. Voiced: /z/, /dʒ/, /m/."),
        ]),
        EX("Worked example 2: same consonant sound", intro="Which word has the same sound as 'th' in 'mother'? A. think  B. thin  C. brother  D. bath", steps=[
            S("Find the sound", text="'Mother' is /ˈmʌðə/. The 'th' is the voiced /ð/."),
            S("Say each option", text="think /θɪŋk/, thin /θɪn/, brother /ˈbrʌðə/, bath /bɑːθ/."),
            S("Compare", text="Only 'brother' has the voiced /ð/. The others have voiceless /θ/."),
            S("Answer", text="C. brother."),
        ]),
        MISTAKE("Replacing /θ/ and /ð/ with /t/, /d/, /s/ or /z/", "'Think' is not 'tink' or 'sink', and 'this' is not 'dis'. "
                "For both sounds, put the tongue tip lightly against the teeth and let the air pass. Practise three, tree and free in turn."),
        MISTAKE("Adding a /ɡ/ to -ng words", "'Sing', 'long' and 'bring' end with /ŋ/ only. Do not say 'sing-g'. "
                "Remember that the letter g in these words is part of the symbol ng, not a separate sound."),
        MISTAKE("Counting letters instead of sounds", "'Church' has six letters but only three sounds: /tʃ/ /ɜː/ /tʃ/. Write sounds by listening, not by counting letters. "
                "In 'ship' the letters s and h make one sound /ʃ/."),
        QUIZ("Which word begins with the voiced consonant /ð/?",
             ["thank", "this", "three", "thin"], 1,
             "'This' /ðɪs/ begins with voiced /ð/. In the other three the 'th' is voiceless /θ/.",
             hint="Put your fingers on your throat. Which word starts with a buzz?",
             feedback=["'Thank' /θæŋk/ begins with voiceless /θ/.", "", "'Three' /θriː/ begins with voiceless /θ/.", "'Thin' /θɪn/ begins with voiceless /θ/."]),
        QUIZ("Which pair of words differs ONLY in voicing (voiced and voiceless consonant)?",
             ["pin and pen", "ship and sheep", "light and right", "cheap and jeep"], 3,
             "'Cheap' /tʃiːp/ has voiceless /tʃ/ and 'jeep' /dʒiːp/ has voiced /dʒ/. Everything else is the same.",
             hint="Look for two consonants made in the same place and the same way, one with a buzz.",
             feedback=["'Pin' and 'pen' differ in the vowel (/ɪ/ and /e/).", "'Ship' and 'sheep' differ in the vowel (/ɪ/ and /iː/).",
                       "'Light' and 'right' differ in the consonant itself: /l/ and /r/ are different sounds in different places.", ""]),
        TIP("Consonant questions in Paper 1 (multiple choice) ask which word has the same sound as another, or which letters stand for a given sound (for example the 'th' in 'this' and 'thin'). "
            "Say each word, check the keyword, and do not trust the spelling.", title="Exam link"),
        PQ("Explain how to tell whether a consonant is voiced or voiceless.",
           "Put your fingers on your throat (or cover your ears) and say the sound. If the vocal cords vibrate (a buzz), the consonant is voiced, for example /z/ and /v/. If not, it is voiceless, for example /s/ and /f/."),
        PQ("Sort these words by the sound of 'th': think, this, brother, bath, the, three.",
           "/θ/ (voiceless): think, bath, three. /ð/ (voiced): this, brother, the."),
        PQ("Write one minimal pair for each: /v/ and /b/, /l/ and /r/, /s/ and /z/.",
           "For example: very and berry, vote and boat; light and right, lock and rock; sue and zoo, bus and buzz."),
        PQ("How many sounds are there in 'ship', 'church' and 'sing'? Name the consonants.",
           "'Ship' /ʃɪp/ has three sounds (/ʃ/, /ɪ/, /p/). 'Church' /tʃɜːtʃ/ has three sounds (/tʃ/, /ɜː/, /tʃ/). 'Sing' /sɪŋ/ has three sounds (/s/, /ɪ/, /ŋ/). "
           "The letters are more than the sounds."),
        SUM("English has 24 consonants: 6 plosives, 9 fricatives, 2 affricates, 3 nasals and 4 approximants.",
            "A voiced consonant has vocal cord vibration (a buzz). Pairs like /p b/, /t d/, /s z/ and /tʃ dʒ/ differ only in voice.",
            "Practise the sounds that are not like any one letter: /θ ð ʃ ʒ tʃ dʒ ŋ/.",
            "Letters and sounds do not match one for one: th, ch, c, g and s each have more than one sound."),
    ],
))

# ------------------------------------------------------------------ 5. Consonant clusters
LESSONS.append(lesson(
    module=M,
    topic=T_CONS,
    title="Consonant clusters and the -s and -ed endings",
    slug="eph-consonant-clusters",
    minutes=22,
    summary="A consonant cluster is two or more consonant sounds together with no vowel between them, as in street, test and texts. Say the whole cluster without adding or dropping a sound, and choose the right ending for -s and -ed.",
    objectives=[
        "Define consonant cluster and count the consonant sounds in initial and final clusters",
        "Say clusters such as str-, spl-, -nd, -st and -sts without inserting or dropping a vowel or consonant",
        "Explain why dropped final consonants change meaning (told and toll, cold and coal)",
        "Choose /s/, /z/ or /ɪz/ for -s endings and /t/, /d/ or /ɪd/ for -ed endings",
    ],
    key_concepts=["Consonant cluster", "Initial and final cluster", "Voicing", "-s endings /s z ɪz/", "-ed endings /t d ɪd/"],
    blocks=[
        H("Introduction"),
        T("A teacher in Kumba reads the word 'street' aloud. One student writes 'sitreet' and another writes 'treet'. Many languages of Cameroon have few "
          "groups of consonants together, so English words like 'street', 'test' and 'texts' need extra practice. This is normal, and it can be trained."),
        T(NOAUDIO),
        D("A **consonant cluster** is a group of two or more consonant sounds said one after the other with no vowel sound between them. "
          "We count **sounds**, not letters: 'box' /bɒks/ ends in the cluster /ks/ because the letter x stands for two sounds, but 'ship' /ʃɪp/ starts with one sound /ʃ/ because the letters sh stand for one sound.",
          title="Consonant cluster"),
        H("Clusters at the start of a word"),
        T("English can begin a word with two or even three consonant sounds. With three, the first is always /s/."),
        CODE("""Pattern                       Examples
s + p, t, k, m, n, l, w      spot, stop, sky, small, snow, slow, swim
p, b, k, g, f + l            play, blue, clean, glad, flag
p, b, t, d, k, g, f, th + r  pray, brown, tree, dress, cry, green, free, three
t, k + w                     twin, queen (qu is said /kw/)
s + p, t, k + l, r, w        split, spring, street, scream, square""", "text", title="Table 1. Initial clusters"),
        T("The three-consonant clusters are /spl/ (split), /spr/ (spring), /str/ (street), /skr/ (scream) and /skw/ (square). "
          "Say them slowly and then speed up. Do **not** add a vowel before them or inside them: 'school' is /skuːl/, not 'sukul' or 'iskul'."),
        H("Clusters at the end of a word"),
        T("Final clusters are common in English, especially from verbs and plurals: hand /hænd/, best /best/, ask /ɑːsk/, help /help/, "
          "act /ækt/, cats /kæts/, tests /tests/, months /mʌnθs/. The longest usual cluster has four consonant sounds: texts /teksts/ ends in /ksts/."),
        T("It matters to say every sound, because final consonants carry meaning. Here are pairs that sound the same when the final consonant is dropped:"),
        CODE("""told /təʊld/   and  toll /təʊl/
cold /kəʊld/   and  coal /kəʊl/
mend /mend/    and  men /men/
build /bɪld/   and  bill /bɪl/
wind /wɪnd/    and  win /wɪn/
past /pɑːst/   and  pass /pɑːs/""", "text", title="Table 2. Do not drop the last sound"),
        H("The -s ending: three sounds"),
        T("The ending -s (plural nouns, third person singular verbs, possessive 's) is said in three ways. "
          "**Look at the last sound of the word, not at the last letter.**"),
        KEY("-s endings", "The choice depends on the final sound.", cards=[
            ["/s/", "After voiceless sounds p, t, k, f, θ: cups, cats, books, laughs, months, he works."],
            ["/z/", "After voiced consonants and after vowels: dogs, bags, pens, boys, tomatoes, she plays, he goes."],
            ["/ɪz/", "After /s z ʃ ʒ tʃ dʒ/: buses, noses, dishes, watches, judges, she teaches, houses."],
        ]),
        T("Why /ɪz/? You cannot say /s/ or /z/ straight after another hissing sound, so English adds the short vowel /ɪ/. "
          "Note that 'laugh' ends in the letter h but the sound /f/, so 'laughs' is /lɑːfs/. 'House' ends in the sound /s/ so 'houses' is /ˈhaʊzɪz/."),
        H("The -ed ending: three sounds"),
        T("The ending -ed (regular past tense and past participle) is also said in three ways. Again, look at the last **sound** of the verb."),
        KEY("-ed endings", "The choice depends on the final sound.", cards=[
            ["/t/", "After voiceless sounds (not t): walked /wɔːkt/, helped, washed /wɒʃt/, watched /wɒtʃt/, laughed /lɑːft/, stopped."],
            ["/d/", "After voiced sounds (not d) and vowels: played /pleɪd/, called, listened, loved /lʌvd/, planned, stayed."],
            ["/ɪd/", "After /t/ or /d/: wanted /ˈwɒntɪd/, needed, decided, visited, started."],
        ]),
        T("Only the third group adds a syllable. 'Walked' has one syllable but 'wanted' has two. Do not say 'walk-id' or 'help-id'."),
        H("Worked examples"),
        EX("Worked example 1: the -s ending", intro="Say the plural or -s form of: cat, dog, bus, book. Which ending does each take?", steps=[
            S("Find the last sound", text="cat /kæt/ ends in /t/. dog /dɒɡ/ ends in /ɡ/. bus /bʌs/ ends in /s/. book /bʊk/ ends in /k/."),
            S("Apply the rule", text="/t/ and /k/ are voiceless, so /s/. /ɡ/ is voiced, so /z/. /s/ is a hissing sound, so /ɪz/."),
            S("Answer", text="cats /kæts/, dogs /dɒɡz/, buses /ˈbʌsɪz/, books /bʊks/."),
        ]),
        EX("Worked example 2: the -ed ending", intro="Say the past tense of: walk, play, want, wash. Which ending does each take?", steps=[
            S("Find the last sound", text="walk ends in /k/ (voiceless). play ends in the vowel /eɪ/. want ends in /t/. wash ends in /ʃ/ (voiceless)."),
            S("Apply the rule", text="Voiceless: /t/. Vowel: /d/. After /t/: /ɪd/."),
            S("Answer", text="walked /wɔːkt/, played /pleɪd/, wanted /ˈwɒntɪd/, washed /wɒʃt/."),
        ]),
        MISTAKE("Adding a vowel inside a cluster", "Do not say 'sukul' or 'iskul' for school /skuːl/, or 'siteet' for street /striːt/. "
                "Practise the cluster by holding the first sound: ssss-treet."),
        MISTAKE("Dropping the final consonant", "'Told' becoming 'toll', 'mend' becoming 'men' and 'cold' becoming 'coal' can change the meaning. "
                "Practise by saying the last sound clearly, then the next word: 'cold water'."),
        MISTAKE("One ending for all", "Not every -ed is /ɪd/ and not every -s is /s/. 'Walked' is /wɔːkt/ and 'dogs' is /dɒɡz/. "
                "Remember: voiceless then /s/ or /t/, voiced then /z/ or /d/, and /ɪz/ or /ɪd/ for the exceptions."),
        QUIZ("What is the ending sound of 'watched' /wɒtʃt/?",
             ["/ɪd/", "/t/", "/d/", "/z/"], 1,
             "'Watch' ends in the voiceless sound /tʃ/. After a voiceless sound (not t), the -ed ending is /t/.",
             hint="Is the last sound of 'watch' voiced or voiceless?",
             feedback=["/ɪd/ is used only after /t/ or /d/. 'Watch' ends in /tʃ/.", "", "/d/ follows voiced sounds. /tʃ/ is voiceless.", "/z/ is a -s ending, not an -ed ending."]),
        QUIZ("How many consonant sounds are there at the start of 'spring'?",
             ["One", "Two", "Three", "Four"], 2,
             "'Spring' is /sprɪŋ/. The three sounds /s/, /p/ and /r/ come before the vowel.",
             hint="Say the word and count the sounds before the vowel /ɪ/.",
             feedback=["There is more than one consonant before the vowel.", "Two are /s/ and /p/ but /r/ is also before the vowel.", "",
                       "After the vowel there is /ŋ/, but at the start there are only three."]),
        TIP("Questions on endings come in Paper 1 (multiple choice): which word ends with the same sound as 'watched', or which word has a different -s or -ed sound from the others. "
            "Apply the voiced/voiceless rule to the last SOUND.", title="Exam link"),
        PQ("Explain why dropping the last sound of 'told' can cause a misunderstanding.",
           "'Told' /təʊld/ without the final /d/ becomes 'toll' /təʊl/, a different word (a charge for passing a road). The final consonant carries the past tense meaning, so the listener may not know the sentence is in the past."),
        PQ("Give the ending sound of each: helped, played, needed.",
           "helped /helpt/ ends in /t/ (after voiceless /p/). played /pleɪd/ ends in /d/ (after a vowel). needed /ˈniːdɪd/ ends in /ɪd/ (after /d/)."),
        PQ("Give the -s sound for each: watches, books, pens.",
           "watches /ˈwɒtʃɪz/ takes /ɪz/ (after /tʃ/). books /bʊks/ takes /s/ (after /k/). pens /penz/ takes /z/ (after /n/)."),
        PQ("Write the final cluster of 'texts' and say how many consonant sounds it has.",
           "'Texts' is /teksts/. The final cluster is /ksts/, with four consonant sounds (/k/, /s/, /t/, /s/)."),
        SUM("A consonant cluster is two or more consonant sounds together, counted by sound and not by letter. Words can begin with up to three and end with up to four.",
            "Do not add a vowel inside a cluster (school is /skuːl/) and do not drop a final consonant (told and toll are different words).",
            "The -s ending is /s/ after voiceless sounds, /z/ after voiced sounds and vowels, and /ɪz/ after /s z ʃ ʒ tʃ dʒ/.",
            "The -ed ending is /t/ after voiceless sounds, /d/ after voiced sounds and vowels, and /ɪd/ after /t/ and /d/."),
    ],
))

# ------------------------------------------------------------------ 6. Silent letters and homophones
LESSONS.append(lesson(
    module=M,
    topic=T_SILENT,
    title="Silent letters and homophones",
    slug="eph-silent-letters-homophones",
    minutes=24,
    summary="Some letters in English words are not pronounced (knife, lamb, hour), and some words sound alike but are spelled and used differently (write and right, their and there). Learn the patterns and use meaning to choose the spelling.",
    objectives=[
        "Name the main groups of silent letters (kn, wr, gn, mb, mn, lk, alm, h, t, gh, ps) and give examples",
        "Explain why a or an depends on the first sound and not the first letter",
        "Define homophone and homograph and give examples of each",
        "Choose the correct word in common homophone sets (their, there, they're; to, too, two; its, it's)",
    ],
    key_concepts=["Silent letter", "Homophone", "Homograph", "a or an before a sound", "Near-homophones"],
    blocks=[
        H("Introduction"),
        T("A Form 3 student in Bamenda writes, 'The nife is on the table.' Another writes, 'I will meet you at the whole.' Both mistakes come from the "
          "same problem: English spelling does not always match the sound. In the first sentence, a silent letter k was left out. In the second, "
          "the student chose the wrong word of two that sound alike: 'hole' and 'whole'."),
        T(NOAUDIO),
        H("Silent letters"),
        D("A **silent letter** is a letter that is written in a word but not pronounced. 'Knife' is /naɪf/: the k is silent. "
          "Many silent letters are the result of old spelling, from the time when the letter was still pronounced.", title="Silent letter"),
        T("Silent letters are not random. Many of them appear in the same letter groups, so a few patterns cover a large number of words."),
        CODE("""Letters  Silent  Examples
kn-      k       know, knee, knife, knock, knight, knot
wr-      w       write, wrong, wrist, wrap, wreck
gn-, -gn g       gnat, gnaw, sign, design, foreign, reign
-mb      b       lamb, comb, climb, bomb, thumb, plumber
-bt      b       debt, doubt, subtle
-mn      n       autumn, column, hymn, condemn
-alk     l       walk, talk, chalk (also calm, half, could, should, would)
ps-      p       psychology, psalm (also pn-: pneumonia)
-gh-     gh      night, light, high, thought, daughter, though
h        h       hour, honest, honour, heir, rhyme, rhythm, ghost
-st(l)-  t       castle, listen, whistle, fasten, Christmas
sc       c       science, scissors, scene, muscle
other    -       Wednesday (d), island (s), answer (w), two (w), cupboard (p), receipt (p), biscuit (u), guess (u)""",
             "text", title="Table 1. Common silent letters"),
        T("**Watch the exceptions.** In 'number', 'member' and 'bamboo' the b IS pronounced. In 'silk', 'milk' and 'film' the l is pronounced. "
          "In 'enough' /ɪˈnʌf/, 'laugh' /lɑːf/ and 'cough' /kɒf/ the letters gh are not silent: they stand for the sound /f/. "
          "The t in 'often' is pronounced by some speakers and silent for others, so check your dictionary."),
        H("A or an: sounds, not letters"),
        T("We use **an** before a vowel **sound** and **a** before a consonant **sound**. This rule depends on the first sound, not the first letter. "
          "So we say **an hour** (the h is silent, so the word begins with the vowel sound /aʊ/), **an honest man**, **an heir**. "
          "We say **a university** (it begins with the consonant sound /j/), **a European** and **a one-way street** (it begins with /w/)."),
        H("Homophones and homographs"),
        D("**Homophones** are words that sound the same but have different meanings and usually different spellings: write and right, "
          "hear and here, two, to and too.", title="Homophone"),
        D("**Homographs** are words with the same spelling but different pronunciations and meanings: lead /liːd/ (to guide) and lead /led/ (a metal); "
          "tear /tɪə/ (from the eye) and tear /teə/ (to rip); wind /wɪnd/ (moving air) and wind /waɪnd/ (to turn). "
          "(Words with the same spelling AND the same sound, like 'bank', are called homonyms and are studied in the vocabulary module.)", title="Homograph"),
        CODE("""/tuː/     to, too, two
/ðeə/     there, their, they're
/raɪt/    write, right
/baɪ/     buy, by, bye
/hɪə/     here, hear
/nəʊ/     no, know
/njuː/    new, knew
/həʊl/    hole, whole
/piːs/    peace, piece
/pleɪn/   plain, plane
/reɪn/    rain, reign
/siː/     sea, see
/sʌn/     sun, son
/teɪl/    tale, tail
/weɪt/    wait, weight
/wiːk/    weak, week
/miːt/    meat, meet
/red/     red, read (past tense)
/kɔːt/    caught, court
/peə/     pair, pear
/ˈflaʊə/  flour, flower
/ˈaʊə/    hour, our
/ˈprɪnsəpl/  principal, principle
/ˈsteɪʃənri/ stationary, stationery""",
             "text", title="Table 2. Homophones to know"),
        T("A few words are not exact homophones but sound so alike in fast speech that they are often confused: **affect** (verb) and **effect** (noun), and **accept** and **except**. "
          "Learn the meanings and the spellings separately."),
        T("In British English, **practise** (verb) and **practice** (noun) are also said the same way, /ˈpræktɪs/. Choose by the part of speech: "
          "'I practise every day' (verb) and 'football practice' (noun)."),
        H("Choosing the correct homophone"),
        KEY("Three sets that cause the most mistakes", "Use meaning and grammar, not sound, to choose.", cards=[
            ["their / there / they're", "their = belonging to them (their books). there = a place, or 'there is' (over there). they're = they are (they're late)."],
            ["to / too / two", "to = direction or part of a verb (to school). too = also, or more than needed (too much). two = the number 2."],
            ["its / it's", "its = belonging to it (the dog wagged its tail). it's = it is or it has (it's raining). Test: if you can say 'it is', use it's."],
            ["whose / who's", "whose = belonging to whom (whose bag?). who's = who is or who has (who's coming?)."],
        ]),
        H("Worked examples"),
        EX("Worked example 1: find the silent letters", intro="Write the silent letter in each word: knife, lamb, hour, listen, answer, island.", steps=[
            S("Say the word and compare with the spelling", text="knife /naɪf/, lamb /læm/, hour /ˈaʊə/, listen /ˈlɪsn/, answer /ˈɑːnsə/, island /ˈaɪlənd/."),
            S("Find the letter with no sound", text="k in knife, b in lamb, h in hour, t in listen, w in answer, s in island."),
            S("Answer", text="k, b, h, t, w, s."),
        ]),
        EX("Worked example 2: choose the correct homophone", intro="Choose the right word in each sentence. 1. (Their / There / They're) going to (hear / here) the speech. 2. Please (write / right) your name on the (hole / whole) page.", steps=[
            S("Sentence 1, first gap", text="The meaning is 'they are going', so use they're."),
            S("Sentence 1, second gap", text="The meaning is to listen with the ears, so hear."),
            S("Sentence 2", text="To put words on paper, we write. 'The whole page' means all of the page. A 'hole' is an opening."),
            S("Answer", text="1. They're going to hear the speech. 2. Please write your name on the whole page."),
        ]),
        MISTAKE("Leaving the silent letter out of the spelling", "Write 'knife', 'island', 'answer' and 'Wednesday', even though some letters are silent. "
                "A good way is to say the word in your head with the silent letter ('Wed-nes-day') when you spell it."),
        MISTAKE("Choosing a homophone by sound", "The ear cannot tell 'their' from 'there' or 'its' from 'it's'. "
                "Ask what the word means in the sentence, and use the rules above."),
        MISTAKE("Thinking gh is always silent", "In 'night' and 'though' it is silent, but in 'enough', 'laugh' and 'cough' it is /f/. "
                "Learn the common words one by one."),
        QUIZ("Which word has a silent b?",
             ["number", "climb", "member", "bag"], 1,
             "'Climb' is /klaɪm/. A b after m at the end of a word is silent: lamb, comb, thumb.",
             hint="Look for -mb at the end of the word.",
             feedback=["In 'number' the b is pronounced: /ˈnʌmbə/.", "", "In 'member' the b is pronounced: /ˈmembə/.", "The b in 'bag' is the first sound and is pronounced."]),
        QUIZ("Which pair are homophones?",
             ["bad and bed", "live and leave", "weak and week", "lose and loose"], 2,
             "'Weak' and 'week' are both /wiːk/ with different spellings and meanings.",
             hint="Homophones sound exactly the same. Say each pair and listen.",
             feedback=["'Bad' /bæd/ and 'bed' /bed/ have different vowels.", "'Live' /lɪv/ and 'leave' /liːv/ have different vowels.", "",
                       "'Lose' /luːz/ and 'loose' /luːs/ end in different consonants."]),
        TIP("This topic appears in Paper 1 (multiple choice) in questions on silent letters, words that sound alike, and gap-filling with the correct homophone. "
            "Correct spelling of homophones also protects your marks in Paper 2, where a wrong word such as 'their' for 'there' is a grammar error.", title="Exam link"),
        PQ("Write five words with a silent letter and say which letter is silent.",
           "For example: knee (k), write (w), lamb (b), hour (h), castle (t), autumn (n), island (s), Wednesday (d), science (c)."),
        PQ("Write a or an: ___ hour, ___ university, ___ honest man, ___ European.",
           "an hour (the h is silent, so the word begins with a vowel sound), a university (begins with /j/), an honest man (silent h), a European (begins with /j/)."),
        PQ("Explain the difference between a homophone and a homograph, with one example of each.",
           "Homophones sound the same but are spelled differently and mean different things, for example write and right. "
           "Homographs are spelled the same but are said differently and mean different things, for example lead /liːd/ and lead /led/."),
        PQ("Fill in the gaps: (its / it's) a pity that the dog lost (its / it's) bone.",
           "It's a pity (it is a pity) that the dog lost its bone (belonging to the dog)."),
        SUM("Silent letters follow patterns: kn, wr, gn, -mb, -mn, -alk, ps, and h in hour and honest. There are exceptions, such as the pronounced b in number.",
            "Use a before a consonant sound and an before a vowel sound: an hour, a university.",
            "Homophones sound alike but differ in spelling and meaning (write and right). Homographs look alike but differ in sound (lead /liːd/ and /led/).",
            "Choose a homophone by meaning: their, there, they're; to, too, two; its, it's."),
    ],
))

# ------------------------------------------------------------------ 7. Word stress and sentence stress
LESSONS.append(lesson(
    module=M,
    topic=T_STRESS,
    title="Word stress and sentence stress",
    slug="eph-word-and-sentence-stress",
    minutes=25,
    summary="In every English word of two or more syllables one syllable is stressed, and in every sentence the important words are stressed while small grammar words are weak. Learn the stress rules and use them to hear and speak clearly.",
    objectives=[
        "Count syllables and find the stressed syllable in a word",
        "Apply the main rules for two-syllable words, noun and verb pairs, suffixes and compound nouns",
        "Distinguish content words (stressed) from function words (weak) in a sentence",
        "Use contrastive stress to change the focus of a sentence",
    ],
    key_concepts=["Syllable", "Word stress", "Stress rules", "Content and function words", "Weak forms", "Contrastive stress"],
    blocks=[
        H("Introduction"),
        T("Two passengers in a taxi in Douala talk about the price. One says, 'It is thirteen thousand.' The other says, 'It is thirty thousand.' "
          "On the phone these two numbers can sound alike. The difference is the **stress**: thirTEEN and THIRty."),
        T(NOAUDIO),
        T("In this lesson, **capital letters show the stressed syllable**, for example baNAna. In dictionaries the stress mark ˈ comes before the stressed syllable: /bəˈnɑːnə/."),
        H("Syllables"),
        D("A **syllable** is a unit of speech with one vowel sound, which may have consonants before and after it. "
          "'Cat' has one syllable. 'Ba-na-na' has three. 'Ed-u-ca-tion' has four. A good test: put your hand under your chin and count how many times your chin drops as you say the word.",
          title="Syllable"),
        D("**Word stress** means that one syllable of a word is said with more force. The stressed syllable is **louder, longer, higher in pitch** and has a clear vowel. "
          "The other syllables are shorter, quieter and often use the weak vowel /ə/.", title="Word stress"),
        T("Compare 'photograph' PHOtograph /ˈfəʊtəɡrɑːf/, 'photographer' phoTOgrapher /fəˈtɒɡrəfə/ and 'photographic' photoGRAPHic /ˌfəʊtəˈɡræfɪk/. "
          "The stress moves, and the vowels change with it. Wrong stress can make a word hard to recognise, even if every sound is correct."),
        H("Stress rules"),
        T("English stress has no single rule, but these patterns are useful. They are guides, so 'check your dictionary' for exceptions."),
        KEY("Patterns for word stress", "Learn the rule and a few examples for each.", cards=[
            ["Two-syllable nouns and adjectives", "Usually the FIRST syllable: TEAcher, MARket, TAble, HAPpy, CLEver, DOCtor."],
            ["Two-syllable verbs", "Usually the SECOND syllable: beGIN, deCIDE, reLAX, forGET, aGREE, proTECT. Exceptions: ANswer, VISit, LISten, OPen, ENter, HAPpen."],
            ["Noun and verb pairs", "Noun: first syllable. Verb: second syllable. REcord (noun) and reCORD (verb); PREsent and preSENT; IMport and imPORT; INcrease and inCREASE; PROgress and proGRESS."],
            ["Suffixes that pull the stress", "The stress falls on the syllable BEFORE -tion, -sion, -ic, -ical, -ity, -ial, -cian, -cious: eduCAtion, deCIsion, ecoNOMic, poLItical, aBIlity, ofFIcial, muSIcian, deLIcious."],
            ["Suffixes that do not move the stress", "-ing, -ed, -er, -ly, -ness, -ful, -less, -ment, -ship: HAPpy and HAPpiness; deVELop and deVELopment; CAREful; FRIENDship."],
            ["Compound nouns", "Usually the FIRST part: BLACKboard, CLASSroom, FOOTball, BOOKshop. Compare a GREENhouse (for plants) with a green HOUSE (a house that is green)."],
            ["Numbers", "-teen: stress the end: thirTEEN, fourTEEN, fifTEEN. -ty: stress the start: THIRty, FORty, FIFty."],
        ]),
        T("**Other useful facts.** The prefixes un-, mis- and re- are usually not stressed: unHAPpy, misTAKE, reTURN. The stress can shift when a suffix is added: "
          "eCONomy /ɪˈkɒnəmi/, eCONomist /ɪˈkɒnəmɪst/ and ecoNOMic /ˌiːkəˈnɒmɪk/."),
        T("**Listening tip.** English listeners find the stressed syllable first and then work out the rest of the word. If you stress the wrong syllable, "
          "they may not recognise the word even if all the sounds are right."),
        T("**Names you know.** 'Cameroon' is said CameROON /ˌkæməˈruːn/, with the main stress on the last syllable. 'Cameroonian' is CameROONian /ˌkæməˈruːniən/. "
          "Say them with the stress on 'roon', not on the first syllable."),
        H("Sentence stress"),
        D("**Sentence stress** means that in a sentence, some words are stressed (said clearly and with more force) and others are weak. "
          "The stressed words are the **content words**, which carry the meaning. The weak words are the **function words**, which hold the grammar together.",
          title="Sentence stress"),
        CODE("""Stressed (content words)        Weak (function words)
nouns          teacher, school    articles        a, an, the
main verbs     want, bring        prepositions    to, in, at, of, for
adjectives     big, new           auxiliary verbs is, are, was, have, can
adverbs        quickly, always    pronouns        he, she, it, them
negatives      not, can't, never  conjunctions    and, but, or
question words what, where
demonstratives this, that""",
             "text", title="Table 1. Content and function words"),
        T("Read this sentence, with the stressed words in capitals: **The TEAcher WANTS the STUdents to BRING their BOOKS toMORrow.** "
          "Only five or six words are stressed. The other words are said quickly and quietly. Notice how weak words often use /ə/: "
          "'to' becomes /tə/, 'the' becomes /ðə/, 'of' becomes /əv/, 'and' becomes /ən/, 'can' becomes /kən/, 'for' becomes /fə/."),
        T("**Rhythm.** English is said with roughly equal time between the stressed syllables. So 'BOYS eat FISH' and 'The BOYS are EAting the FISH' take nearly the same time. "
          "The extra weak syllables are squeezed in. Speakers of French and many languages of Cameroon often give every syllable the same weight, which can make English "
          "sound very slow or unclear to listeners. Try to stress the content words and say the others quickly."),
        H("Contrastive stress"),
        T("A speaker can stress any word to show what is important or to correct something. This is called **contrastive stress**, and it changes the focus of the sentence."),
        CODE("""SHE bought the phone.     (not he)
She BOUGHT the phone.     (she did not borrow it)
She bought the PHONE.     (not the radio)""", "text", title="Table 2. One sentence, three meanings"),
        H("Worked examples"),
        EX("Worked example 1: find the stress", intro="Mark the stressed syllable: begin, teacher, education, thirteen.", steps=[
            S("begin", text="Two-syllable verb: stress the second syllable. beGIN."),
            S("teacher", text="Two-syllable noun: stress the first syllable. TEAcher."),
            S("education", text="The suffix -tion pulls the stress to the syllable before it. eduCAtion."),
            S("thirteen", text="-teen takes the stress. thirTEEN. Compare THIRty."),
            S("Answer", text="beGIN, TEAcher, eduCAtion, thirTEEN."),
        ]),
        EX("Worked example 2: sentence stress", intro="Mark the stressed words in: 'She is going to the market to buy some tomatoes.'", steps=[
            S("Find the content words", text="going (main verb), market (noun), buy (main verb), tomatoes (noun)."),
            S("Find the function words", text="She, is, to, the, to, some. These are weak."),
            S("Answer", text="She is GOing to the MARket to BUY some toMAtoes. The word 'tomatoes' is stressed on the second syllable."),
        ]),
        MISTAKE("Equal stress on every syllable", "If every syllable is loud and long, English sounds unclear. Stress one syllable in each word clearly and say the others lightly: "
                "baNAna, not BA-NA-NA."),
        MISTAKE("Stressing function words", "Do not stress 'the', 'to', 'of' and 'and' in every sentence. Stress the words that carry the meaning, "
                "unless you want to correct someone (contrastive stress)."),
        MISTAKE("Changing the stress of noun and verb pairs", "'REcord' (noun) and 'reCORD' (verb) are different. 'The IMports are rising' and 'We imPORT rice' both need the right syllable stressed."),
        QUIZ("Where is the stress in 'decision'?",
             ["DEcision", "deCIsion", "deciSION", "All syllables are stressed equally"], 1,
             "The suffix -sion pulls the stress to the syllable before it: de-CI-sion.",
             hint="Which suffix does the word end with? Where does that suffix put the stress?",
             feedback=["That would be the pattern for many two-syllable nouns, but 'decision' ends in -sion.", "",
                       "The stress does not fall ON the suffix -sion. It falls on the syllable before it.", "In English one syllable carries the stress."]),
        QUIZ("In the sentence 'The doctor will see you tomorrow', which words are normally stressed?",
             ["the, will, you", "all words equally", "will, see, you", "doctor, see, tomorrow"], 3,
             "Content words (doctor, see, tomorrow) are stressed. 'The', 'will' and 'you' are weak function words.",
             hint="Which words carry the meaning: nouns, main verbs, adverbs?",
             feedback=["These are articles, auxiliaries and pronouns, which are normally weak.", "English stresses the important words and says the others quickly.",
                       "'Will' and 'you' are function words and normally weak.", ""]),
        TIP("Stress appears in Paper 1 (multiple choice) as questions that ask which syllable is stressed, or which word has the stress in a different place from the others. "
            "It also helps in the listening part, where the stressed words carry the main information.", title="Exam link"),
        PQ("Mark the stressed syllable in each: computer, tomorrow, university, chemistry.",
           "comPUter, toMORrow, uniVERsity, CHEMistry."),
        PQ("Explain how stress changes the word 'record' when it is a noun and a verb. Give a sentence for each.",
           "As a noun it is stressed on the first syllable: 'He broke the school REcord.' As a verb it is stressed on the second: 'Please reCORD the lesson.'"),
        PQ("Mark the stressed words in: 'My brother is buying a new phone.'",
           "My BROther is BUYing a NEW PHONE. The words my, is and a are weak function words."),
        PQ("How can you use stress in 'I want the red bag' to show that you do not want the blue one?",
           "Stress 'red': 'I want the RED bag.' This is contrastive stress."),
        SUM("A syllable has one vowel sound. In a word of two or more syllables one syllable is stressed (louder, longer, clearer).",
            "Rules: two-syllable nouns and adjectives are stressed on the first syllable, verbs on the second; the suffixes -tion, -ic and -ity pull the stress to the syllable before; -teen takes the stress.",
            "In sentences, content words are stressed and function words are weak, often with /ə/.",
            "Contrastive stress puts the focus on any word you want to emphasise or correct."),
    ],
))

# ------------------------------------------------------------------ 8. Intonation
LESSONS.append(lesson(
    module=M,
    topic=T_INTON,
    title="Intonation: falling and rising patterns",
    slug="eph-intonation-patterns",
    minutes=22,
    summary="Intonation is the rise and fall of the voice across a sentence. Statements, wh-questions and commands usually fall; yes/no questions rise; lists rise on each item and fall on the last; a fall-rise can show doubt.",
    objectives=[
        "Define intonation and say how it differs from stress",
        "Predict the usual pattern (fall or rise) for statements, wh-questions, yes/no questions, commands and greetings",
        "Use the correct pattern in lists, alternative questions and question tags",
        "Explain how a change of intonation changes the speaker's meaning or attitude",
    ],
    key_concepts=["Intonation", "Falling tone", "Rising tone", "Fall-rise", "Lists and alternative questions", "Attitude"],
    blocks=[
        H("Introduction"),
        T("A woman at a market in Bafoussam looks at a customer who has picked up a bag of rice. She says, 'You are buying?' with her voice going **up** at the end. "
          "It is a question. If she says 'You are buying.' with her voice going **down**, it is a statement: she is sure. "
          "The words are the same. Only the movement of the voice has changed."),
        T(NOAUDIO),
        D("**Intonation** is the rise and fall of the voice (its **pitch**) across a sentence or a group of words. "
          "**Stress** is about which syllables are strong. Intonation is about the **direction** of the voice on the most important syllable.", title="Intonation"),
        T("In each group of words there is one syllable where the pitch movement begins. It is usually the stressed syllable of the **last important word**. "
          "We call it the **nucleus** and, in this lesson, write it in capitals."),
        KEY("The main tunes", "English uses a small number of tunes.", cards=[
            ["Fall", "The voice goes down on the nucleus. It sounds finished, certain, definite."],
            ["Rise", "The voice goes up. It sounds unfinished, open, questioning, polite or friendly."],
            ["Fall-rise", "The voice goes down and then up. It sounds doubtful or has a 'but' behind it."],
        ]),
        IMG("f5en-ph-intonation.svg",
            alt="Three pitch contours. In the first, the voice falls on the last word of a statement. In the second, it rises on the last word of a yes or no question. In the third, it rises on three list items and falls on the last.",
            caption="Figure 1. Three common patterns. The orange word carries the main pitch movement."),
        H("The rules, with examples"),
        T("In the examples, 'fall' and 'rise' in brackets show the direction of the voice on the capital word."),
        CODE("""Statements        I live in BUEA.               (fall)
Wh-questions      Where do you LIVE?            (fall)
Commands          Open your BOOKS.              (fall)
Greetings         Good MORning.                 (fall)
Yes/no questions  Do you live in BUEA?          (rise)
Polite requests   Could you open the WINdow?    (rise)
Echo questions    You are LEAVing?              (rise)""",
             "text", title="Table 1. The usual patterns"),
        T("**Wh-questions** (who, what, where, when, why, how) usually fall: 'Where is the TEAcher?' A wh-question can also rise to sound friendly or interested: "
          "'What is your NAME?' with a rise sounds warm. Books differ on this, so treat the fall as the neutral pattern."),
        T("**Yes/no questions** (questions that can be answered with yes or no) usually rise. A yes/no question that falls can sound cold, abrupt or like an order."),
        H("Lists and alternatives"),
        T("In a list, the voice **rises** on each item and **falls** on the last. The rise tells the listener that more is coming. The fall tells them the list is finished."),
        CODE("""We sell TOmatoes (rise), ONions (rise), PEPper (rise) and GARlic (fall).
Would you like TEA (rise) or COFfee (fall)?""", "text", title="Lists and alternative questions"),
        T("The same idea works in a sentence with a **comma**. The part before the comma rises slightly because the sentence is not finished: "
          "'When the BELL rings (rise), you may GO (fall).' 'If you STUdy (rise), you will PASS (fall).'"),
        H("Question tags"),
        T("A question tag is a short question added to a statement: 'It is hot, isn't it?' Its intonation shows the speaker's purpose."),
        CODE("""You are a STUdent, aren't you?   (rise)  A real question: I do not know.
It's HOT, isn't it?              (fall)  I expect you to agree.""", "text", title="Question tags"),
        H("Fall-rise: doubt and reservation"),
        T("A **fall-rise** shows doubt, hesitation or a hidden 'but'. If someone asks, 'Is the food good?' and you answer 'It's CHEAP' with a fall-rise, "
          "you suggest 'It is cheap, but...' It can also show polite disagreement: 'WELL, it's POSsible...'"),
        H("Why it matters"),
        T("Intonation helps listeners know whether you are asking, telling, finishing or continuing, and also whether you are sure, polite, bored or surprised. "
          "In writing we use punctuation for the same job: the question mark for a rising question, the full stop for a falling statement, and the comma for a pause with a slight rise."),
        T("**A note on varieties.** English around the world has different tunes. Many speakers of English in Cameroon use patterns influenced by their first language, "
          "and this is natural. The patterns in this lesson are the standard British ones that examination listening texts follow. "
          "Listen to the BBC or a good teacher for the real sound, and ask your teacher to read the examples aloud."),
        H("Worked examples"),
        EX("Worked example 1: choose the pattern", intro="Choose fall or rise for: (a) 'What time is the match?' (b) 'Is the match at four?' (c) 'Close the door.'", steps=[
            S("(a)", text="A wh-question: usually a fall. What time is the MATCH? (fall)."),
            S("(b)", text="A yes/no question: a rise. Is the match at FOUR? (rise)."),
            S("(c)", text="A command: a fall. Close the DOOR. (fall)."),
            S("Answer", text="(a) fall, (b) rise, (c) fall."),
        ]),
        EX("Worked example 2: a list", intro="Show the intonation in: 'I bought plantains, cassava, beans and fish.'", steps=[
            S("Find the items", text="plantains, cassava, beans, fish. The nucleus is on the main stressed syllable of each."),
            S("Rise on the first items", text="PLANtains (rise), casSAva (rise), BEANS (rise)."),
            S("Fall on the last item", text="and FISH (fall)."),
            S("Answer", text="I bought PLANtains (rise), casSAva (rise), BEANS (rise) and FISH (fall)."),
        ]),
        MISTAKE("Using a rise for every question", "Wh-questions are usually neutral with a fall. 'Where do you LIVE?' with a rise sounds friendly or like a repeat of something you did not hear. "
                "The strong rise belongs to yes/no questions."),
        MISTAKE("Falling on every item of a list", "If your voice falls on each item, the listener thinks the list has ended. Rise on each item except the last."),
        MISTAKE("Using a flat voice", "If the voice stays on one level, listeners cannot tell whether you are asking, telling or finishing. "
                "Let the pitch move on the nucleus."),
        QUIZ("Which question normally has a rising intonation?",
             ["Where do you live?", "What is your name?", "How old are you?", "Do you live in Limbe?"], 3,
             "A yes/no question normally rises at the end: Do you live in LIMbe? (rise).",
             hint="Which one can be answered with just 'yes' or 'no'?",
             feedback=["A wh-question normally falls.", "A wh-question normally falls.", "A wh-question normally falls.", ""]),
        QUIZ("In 'We need pens, books and rulers', how does the voice move?",
             ["Falls on every item", "Rises on pens and books, falls on rulers", "Rises on every item", "Stays level throughout"], 1,
             "In a list the voice rises on every item except the last and falls on the last item.",
             hint="Think about what the rise tells the listener about the list.",
             feedback=["A fall on every item makes the list sound finished too soon.", "", "A rise on the last item makes the list sound unfinished.", "A level voice does not mark the list."]),
        TIP("Intonation is tested in Paper 1 (multiple choice) in questions that ask which intonation pattern fits a sentence, and in listening questions where the speaker's attitude is asked "
            "(sure, doubtful, polite). Learn the usual patterns and notice a speaker's tone when the listening text is read.", title="Exam link"),
        PQ("State the usual intonation of: (a) a statement, (b) a yes/no question, (c) a command.",
           "(a) A fall. (b) A rise. (c) A fall."),
        PQ("Mark the intonation in 'Would you like rice or yam?'",
           "Would you like RICE (rise) or YAM (fall)? An alternative question rises on the first choice and falls on the last."),
        PQ("Explain the difference in meaning between 'It's hot, isn't it?' with a fall and with a rise.",
           "With a fall, the speaker is almost sure and expects you to agree. With a rise, the speaker is genuinely asking and does not know."),
        PQ("What does a fall-rise on 'It's cheap' suggest?",
           "It suggests doubt or a hidden 'but': the speaker is saying the item is cheap but perhaps not good, or not what you want."),
        SUM("Intonation is the rise and fall of the voice. Stress marks strong syllables; intonation marks the direction of the pitch on the nucleus.",
            "Statements, wh-questions, commands and greetings usually fall. Yes/no questions and polite requests usually rise.",
            "In lists, the voice rises on each item and falls on the last. In alternative questions it rises on the first choice and falls on the last.",
            "A fall-rise shows doubt, and a question tag rises for a real question or falls when the speaker expects agreement."),
    ],
))

# ------------------------------------------------------------------ 9. Listening strategies and note-taking
LESSONS.append(lesson(
    module=M,
    topic=T_LISTEN,
    title="Listening comprehension: strategies and note-taking",
    slug="eph-listening-strategies-notes",
    minutes=28,
    summary="Good listening is planned: read the questions first, listen for key words and signal words, watch for corrections and numbers, and write short notes with abbreviations. Practise with a text read aloud by your teacher.",
    objectives=[
        "Use before-, during- and after-listening strategies for multiple-choice listening questions",
        "Recognise signal words, corrections and number traps (thirteen and thirty)",
        "Take short, clear notes using key words, abbreviations and symbols",
        "Answer questions on a listening text read aloud",
    ],
    key_concepts=["Gist and detail listening", "Predicting", "Signal words", "Distractors", "Note-taking", "Abbreviations"],
    blocks=[
        H("Introduction"),
        T("A radio announcer in Buea says, 'The ferry will leave at half past six on Friday, not Saturday.' A listener writes down 'Saturday, 6.30'. "
          "He hears everything but he misses the correction. He arrives on Saturday morning and the ferry is gone. "
          "Listening is not only hearing. It is choosing what to keep, and understanding it."),
        T("Paper 1 of the examination (50 multiple-choice questions) includes listening comprehension: a text is spoken and you answer questions about it. "
          "Follow the instructions on the day about how many times the text is read, and when you may read the questions."),
        T(NOAUDIO),
        T("For listening practice in the written lessons, ask a teacher, a friend or a parent to read the practice text aloud to you at normal speed. "
          "If you are alone, read it aloud once and cover it before you answer."),
        H("Three kinds of listening"),
        KEY("What the questions can ask", "Different questions need different listening.", cards=[
            ["Gist", "What is the whole text about? Who is speaking and why?"],
            ["Detail", "A name, a number, a date, a place, a reason."],
            ["Inference and attitude", "What does the speaker feel? Is the speaker sure, worried, polite, angry? What is the purpose?"],
        ]),
        H("Before, during and after"),
        D("**Before listening**: use any time you are given. Read the questions and options. Underline the key words (who, when, how many, why). "
          "Guess what kind of text it is (an announcement, a news item, a conversation) and what words you may hear.", title="Before listening"),
        D("**During listening**: listen first for the gist, then for the details you need. Do not stop at a word you missed: keep following. "
          "Write short notes. Watch for signal words and corrections.", title="During listening"),
        D("**After listening**: check each answer against your notes. Choose the option that matches the meaning, not the option that repeats a word from the text.", title="After listening"),
        H("Signal words and number traps"),
        T("Speakers use small words to tell you how the ideas are joined. These words tell you where the important information is."),
        KEY("Signal words", "Notice them and note what follows.", cards=[
            ["Order", "first, then, next, after that, finally, at last"],
            ["Contrast", "but, however, although, on the other hand, not... but..."],
            ["Reason and result", "because, so, as a result, therefore, that is why"],
            ["Correction and emphasis", "sorry, I mean, actually, no, wait, most important, remember, please note"],
        ]),
        T("**Corrections** are the most common trap. When a speaker says 'sorry, I mean Thursday', the second item is the answer. "
          "**Distractors** are other things the speaker mentions that are not the answer. If the text says 'not Wednesday but Thursday', Wednesday is a distractor."),
        T("**Numbers** need special care. Stress helps you: thirTEEN (13) has the stress at the end, but THIRty (30) at the beginning. The same holds for fourTEEN and FORty, fifTEEN and FIFty."),
        CODE("""thirTEEN = 13        THIRty = 30
fifTEEN  = 15        FIFty  = 50
quarter past two = 2.15       ten to three = 2.50
four thousand five hundred = 4,500
double five = 55     oh or zero = 0 (in phone numbers)
nineteen ninety-six = 1996""", "text", title="Number traps"),
        H("Note-taking"),
        T("While you listen you cannot write full sentences. Write **key words only**: names, numbers, days, places, reasons, and the words after signal words. "
          "Use abbreviations and symbols that you understand. Leave space on the page."),
        CODE("""w/      = with                  b/c   = because
w/o     = without               &     = and
=       = means, is the same    ->    = leads to, becomes
up/down = increase/decrease     no.   = number
Mon, Fri = days                 am, pm = morning, afternoon
FCFA or F = francs              approx. = about
e.g.    = for example           NB    = note well, important""", "text", title="Useful note-taking shorthand"),
        T("A good note keeps the facts and drops the grammar. For the sentence 'The bus leaves Bamenda at half past six on Friday morning, not Saturday, and the fare is four thousand five hundred francs', the note is:"),
        CODE("""Bus: Bamenda 6.30 Fri am (NOT Sat). Fare 4,500 F""", "text", title="Model note"),
        H("Worked examples"),
        EX("Worked example 1: take notes", intro="Write notes for: 'The school library will be open from eight o'clock to four o'clock on Monday and Tuesday only. Students must bring their identity cards.'", steps=[
            S("Find the facts", text="What: library open. When: 8 to 4. Which days: Monday and Tuesday only. What to bring: identity cards."),
            S("Drop the grammar", text="Remove 'the school', 'will be', 'from', 'to', 'students must'."),
            S("Write", text="Library: 8-4, Mon & Tue only. Bring ID cards."),
            S("Check", text="Every fact is still there: place, times, days, requirement."),
        ]),
        EX("Worked example 2: a correction", intro="You hear: 'I thought of taking the seven o'clock bus. Actually, no, that will be too late. I will take the six o'clock bus.' Which bus will the speaker take?", steps=[
            S("Spot the signal", text="'Actually, no' is a correction signal."),
            S("Find the first idea", text="The seven o'clock bus was an idea, but the speaker rejected it."),
            S("Find the final decision", text="'I will take the six o'clock bus.'"),
            S("Answer", text="The six o'clock bus. The seven o'clock bus is a distractor."),
        ]),
        MISTAKE("Trying to write everything", "You cannot write full sentences and listen at the same time. Write key words only, and use shorthand."),
        MISTAKE("Choosing the first thing you hear", "Speakers correct themselves: 'Tuesday, sorry, Thursday'. Wait for the final answer."),
        MISTAKE("Choosing an option because it repeats a word", "Wrong options often use words from the text but with a different meaning. Check the whole meaning of the option against your notes."),
        MISTAKE("Mixing -teen and -ty numbers", "Thirteen and thirty sound alike. Use the stress and the context (a price, an age, a number of students) to decide."),
        QUIZ("A speaker says, 'The meeting is on Tuesday. Sorry, I mean Thursday.' When is the meeting?",
             ["Tuesday", "Wednesday", "Thursday", "Friday"], 2,
             "'Sorry, I mean' signals a correction. The final information is Thursday.",
             hint="Look for the correction signal.",
             feedback=["Tuesday is the speaker's mistake, which was corrected.", "Wednesday is not mentioned at all.", "", "Friday is not mentioned at all."]),
        QUIZ("Which is the best note for: 'The school will close at four o'clock because of heavy rain'?",
             ["The school will close at four o'clock because of heavy rain.", "School closes 4 pm: heavy rain", "School, rain", "Closes"], 1,
             "The best note is short and keeps the key facts: what (school closes), when (4 pm) and why (heavy rain).",
             hint="A good note keeps the facts and drops the grammar, but loses nothing important.",
             feedback=["This copies the whole sentence. It takes too long to write.", "", "This is too short. It does not say what happens or when.", "This keeps only one word and loses the time and the reason."]),
        H("Practice: a text read aloud by your teacher"),
        T("**Instructions for the reader (teacher, friend or parent):** read the text below twice, at a normal speed, with natural pauses. "
          "The listener should **not** look at the text. The listener may take notes and then answer the four questions.", title="Practice text: school announcement"),
        T("'Good morning, students. This is an announcement from the Principal's office. The Inter-School Science Fair will be held on Thursday, not Wednesday as we first said. "
          "Sorry for the change. It will start at nine o'clock in the school hall. Each class may send two projects. The projects must be about water, energy or farming. "
          "Students should arrive at half past eight and bring their projects in a box. The entry fee is five hundred francs for each project, and it must be paid to the class prefect on Monday. "
          "The best three projects will win prizes: a dictionary, a calculator and a book of experiments. Please remember: no mobile phones in the hall. Thank you.'",
          title="Text to be read aloud"),
        TIP("This topic appears in Paper 1 (multiple choice): the listening comprehension questions test gist, detail and the speaker's attitude. "
            "Reading the questions first, taking short notes and noticing corrections are the skills to practise.", title="Exam link"),
        PQ("On which day will the Science Fair be held? Why is Wednesday a distractor?",
           "Thursday. The speaker first said Wednesday and then corrected it ('not Wednesday as we first said'). Wednesday is the old information, so it is a distractor."),
        PQ("At what time should students arrive, and at what time does the fair start?",
           "Students should arrive at half past eight (8.30). The fair starts at nine o'clock (9.00)."),
        PQ("How many projects may each class send, and what must the projects be about?",
           "Two projects. They must be about water, energy or farming."),
        PQ("Write short notes for the text, using abbreviations.",
           "A possible note: Sci Fair: THURS (not Wed), 9 am, school hall. 2 projects/class; topics: water, energy, farming. Arrive 8.30, box. Fee 500 F/project, pay prefect Mon. "
           "Prizes: dictionary, calculator, exp. book. NB no phones. Your own wording is fine if the facts are right."),
        SUM("Before listening, read the questions and predict. During listening, follow the gist and note the details. After listening, check your answers against your notes.",
            "Signal words (but, however, sorry, I mean, actually) show where the important information or a correction comes.",
            "Take key-word notes with abbreviations (w/, b/c, &, ->, no., F) and not full sentences. Watch number traps such as thirteen and thirty.",
            "Choose the option that matches the meaning, not the one that repeats a word from the text."),
    ],
))
