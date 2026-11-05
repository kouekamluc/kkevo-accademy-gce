"""Form 5 ICT: Legal, Ethical & Social Aspects (7 lessons, one practice set each)."""

from .dsl import *  # noqa: F403

COURSE = ("ict", "form-5")

MODULE = "Legal, Ethical & Social Aspects"
IP = "Intellectual property"
LAW = "Cameroon legal framework"
SOCIAL = "Social and economic impact"

LESSONS = []

# ------------------------------------------------------------------ Intellectual property
LESSONS.append(lesson(
    module=MODULE,
    topic=IP,
    title="Copyright, piracy and your own work",
    slug="ip-copyright-piracy-and-your-work",
    minutes=20,
    summary="Understand what copyright protects, what you may and may not copy in school and at work, how to credit sources, and why pirated software and music are a bad deal.",
    objectives=[
        "Explain intellectual property and copyright in simple words",
        "Say what a student or worker may and may not copy",
        "Credit a source correctly and avoid plagiarism",
        "Explain the risks of pirated software and music and name legal alternatives",
    ],
    key_concepts=["Intellectual property", "Copyright", "Software piracy", "Plagiarism", "Citing a source"],
    blocks=[
        H("Introduction"),
        T("You are setting up a new cyber cafe in Buea. A friend offers you a USB key with \"all the programs, already cracked\" "
          "for 2000 FCFA. The same week, a customer asks you to burn 30 songs from the internet onto discs to sell at his stall.\n\n"
          "Both situations are about **intellectual property**. People who work with ICT meet these questions every day."),
        D("**Intellectual property** means creations of the mind: a program, a song, a photo, a book, a logo. "
          "**Copyright** is the right of the creator to decide who may copy, share, sell or change the work.",
          title="Definitions"),
        T("Copyright starts automatically when the work is created. The creator does not need to fill in a form. "
          "A photo you take with your phone is already yours. A song recorded in a Douala studio already belongs to the people who made it."),
        KEY("What copyright protects", "Copyright covers many things you use every day.", cards=[
            ["Software", "Programs and apps, including games and accounting programs."],
            ["Music and video", "Songs, films, series and videos made by others."],
            ["Text and images", "Books, articles, photos, drawings and web pages."],
            ["Ideas and facts", "A bare idea or a fact is free to use. The way someone writes or draws it is protected."],
        ]),
        H("What may you copy?"),
        T("The simple rule is: **ask who made it and what permission you have.** "
          "Some copying is fine. Some is not."),
        KEY("Usually fine", "Always keep the source in mind.", cards=[
            ["Your own work", "Your own essay, photo or program. You may copy and share it."],
            ["With permission", "The owner said yes, or a licence allows it."],
            ["A short quotation", "A few words used in your work, in quotation marks, with the source named."],
            ["A backup of software you bought", "Check the licence first. Some licences allow a backup copy."],
        ]),
        KEY("Usually not fine", "These break copyright.", cards=[
            ["Copying a whole book or a paid program", "Even for friends, even if you do not make money."],
            ["Selling copied music or films", "Burning discs to sell is piracy."],
            ["Handing in someone else's work", "Copying an essay and putting your name on it."],
            ["Using a found photo in a flyer", "Being on the internet does not give you permission."],
        ]),
        T("If you are not sure, check the licence or ask your teacher. Rules differ in details, "
          "so for exact legal wording follow your teacher's notes and the current official texts."),
        H("Giving credit"),
        D("**Plagiarism** is presenting someone else's words, ideas or work as your own. "
          "**Citing a source** means telling the reader where the information came from.", title="Plagiarism and citing"),
        T("When you use another person's text in a school project, do one of two things. "
          "Either write the idea **in your own words** and name the source. "
          "Or copy a short part **exactly**, put it in quotation marks and name the source."),
        CODE("What to note about a source:\n"
             "  1. Author or website name\n"
             "  2. Title of the page or book\n"
             "  3. The date you read it\n\n"
             "Example:\n"
             "  Ministry of Education website, \"Exam timetable\", read on 12 May.",
             "text", title="A simple way to name a source"),
        EX("Worked example 1: a project on cocoa farming", intro=(
            "Ngwa is writing a project about cocoa farming near Kumba. She finds a good paragraph on a website. "
            "How should she use it?"), steps=[
            S("Read and understand", text="She reads the paragraph, then closes the page."),
            S("Write it in her own words", text="She explains the main ideas in her own sentences, with examples from farms she knows."),
            S("Name the source", text="At the end she adds a list of sources with the website name and the date she read it."),
            S("Quote only if needed", text="If one sentence is very clear, she copies only that sentence, in quotation marks, and names the source next to it."),
        ]),
        EX("Worked example 2: the USB key of cracked programs", intro=(
            "The cyber cafe owner in Buea has 8 computers and little money. His friend offers the cracked USB key for 2000 FCFA. "
            "Advise him."), steps=[
            S("Name the problem", text="Cracked programs are copied and unlocked without the owner's permission. This is software piracy."),
            S("List the risks", text="Hidden viruses or spyware, no updates, no help when something fails, and customers' data put at risk."),
            S("Legal alternatives", text="Use free open-source programs such as LibreOffice, GIMP and Firefox. Or buy the licences he needs."),
            S("Decision", text="Refuse the key. Free legal programs cost nothing and are safer."),
        ]),
        H("Pirated software and music"),
        D("**Software piracy** is copying, installing, sharing or selling software without the owner's permission. "
          "Copying music and films without permission, then using or selling them, is also piracy.", title="Software piracy"),
        KEY("Why a cheap copy is a bad deal", "A free copy often costs more later.", cards=[
            ["For the user", "Viruses, lost files, no updates and no help. A cracked program may steal passwords."],
            ["For the business", "Trouble with the law, and a damaged name if customers find out."],
            ["For creators", "Musicians, artists and developers lose income, so less new work is made, including by young Cameroonian creators."],
        ]),
        T("There are legal ways to get what you need cheaply: free open-source software, free and paid streaming services, "
          "school or library copies, and music that the artist has chosen to share for free."),
        H("Common mistakes"),
        MISTAKE("It is on the internet, so it is free", "Being easy to find does not mean you have permission. "
                "Check who made it and what the page allows."),
        MISTAKE("I bought it, so I can copy it for everyone", "Buying usually gives you the right to use one copy. "
                "Making copies for others needs the owner's permission."),
        MISTAKE("Changing a few words is enough", "If you only change a few words of another person's text, it is still plagiarism. "
                "Rewrite the idea fully and name the source."),
        QUIZ("Which action is NOT a breach of copyright?",
             ["Burning 30 downloaded songs onto discs to sell", "Printing a photo that you took yourself on your own flyer",
              "Copying a classmate's essay and handing it in as yours", "Installing a cracked accounting program on five computers"], 1,
             "A photo you took yourself is your own work. You may print and share it.",
             feedback=["Selling copied music is piracy.", "",
                       "Handing in another person's work is plagiarism.", "A cracked program is pirated software."]),
        QUIZ("A student copies a paragraph from a website into her homework and does not name the website. What is this?",
             ["Plagiarism", "Citing a source", "Writing in her own words", "Open-source use"], 0,
             "Presenting someone else's words as your own, without naming the source, is plagiarism.",
             feedback=["", "Citing means naming the source, which she did not do.",
                       "Her own words would not be a copied paragraph.", "Open source describes a kind of software licence, not copied text."]),
        H("Practice questions"),
        PQ("Define intellectual property and copyright, and say when copyright starts.",
           "Intellectual property means creations of the mind such as programs, songs, photos and books. Copyright is the creator's right "
           "to decide who may copy, share, sell or change the work. It starts automatically when the work is created."),
        PQ("Give three risks of using pirated software in a small business.",
           "Any three of: viruses or spyware that damage computers or steal data; no updates or support; trouble with the law; "
           "loss of customers' trust; creators lose income, so less new software is made."),
        PQ("A pupil must write a short report on the school library. Describe how she can use a web article without plagiarising.",
           "She reads the article and writes the ideas in her own words, adding her own observations of the library. "
           "If she copies a short sentence, she puts it in quotation marks. She names the website and the date she read it in a list of sources."),
        SUM("Intellectual property is a creation of the mind; copyright gives the creator control over copying, sharing and selling, and starts automatically.",
            "You may copy your own work, work you have permission for and short quotations with the source named.",
            "Plagiarism is presenting someone else's work as yours; use your own words and name the source.",
            "Software and music piracy are risky and unfair to creators.",
            "Free open-source programs and legal music sources are safe, low-cost choices."),
    ],
))

LESSONS.append(lesson(
    module=MODULE,
    topic=IP,
    title="Software licences in practice",
    slug="ip-software-licences-in-practice",
    minutes=22,
    summary="Tell proprietary, free, open-source and Creative Commons licences apart in plain words, read a licence for the key limits, and choose software for a school or a small business.",
    objectives=[
        "Explain what a software licence is and why it matters",
        "Compare proprietary, freeware, shareware and open-source software",
        "Explain what BY, SA, NC and ND mean in a Creative Commons licence",
        "Pick suitable legal software for a school lab or small shop",
    ],
    key_concepts=["Licence", "Proprietary software", "Freeware", "Shareware", "Open-source software", "Creative Commons"],
    blocks=[
        H("Introduction"),
        T("In the previous lesson you saw that copying paid programs without permission is piracy. "
          "But what exactly are you allowed to do with a program you install? The answer is in its **licence**.\n\n"
          "Imagine the head of a school library in Bamenda. She has 12 old computers and a small budget. "
          "She needs a word processor, a browser and a photo editor. Which programs can she legally put on all 12 machines?"),
        D("A **software licence** is the agreement that says how a program may be used. "
          "It can say how many computers, who may use it, and whether you may copy it, change it or use it for business.",
          title="Licence"),
        T("When you install a program and tick **I agree**, you accept its licence. Always look at the main limits before you tick."),
        H("Four common kinds of software"),
        IMG("f5i-licence-spectrum.svg",
            alt="A line from most restricted to most open: proprietary, shareware, freeware, open source",
            caption="Figure 1. Kinds of software from most restricted to most open."),
        KEY("What each kind allows", "Ask two questions: do you pay, and can you see and change the code?", cards=[
            ["Proprietary", "You pay for a licence. You may not copy or change it. Examples: Microsoft Office, Adobe Photoshop."],
            ["Shareware", "Free trial first. You must pay to keep using it or to unlock all features."],
            ["Freeware", "Free to use, but the code is closed. You usually cannot change it. Some freeware forbids business use."],
            ["Open source", "The code is open. You may use, study, change and share it, under conditions. Examples: LibreOffice, GIMP, Firefox, Linux."],
        ]),
        D("**Free** can mean two different things. **Free of charge** means no price. **Free as in freedom** means you may study, change and share it. "
          "Open-source software is usually both. Freeware is only free of charge.", title="Two meanings of free"),
        T("Open-source licences have conditions too. Some, such as the GPL, say that if you share a changed copy, you must share it under the same open terms. "
          "Others, such as the MIT licence, allow almost any reuse as long as you keep the credit."),
        H("Creative Commons for images, music and text"),
        T("Photos, articles and diagrams are not programs, so they use other licences. "
          "**Creative Commons (CC)** licences are a simple set of labels that photographers, teachers and writers use to say how others may reuse their work."),
        KEY("The four letters", "Read the letters on the page where the work is published.", cards=[
            ["BY", "You must give credit to the creator."],
            ["SA", "If you share a changed version, share it under the same licence."],
            ["NC", "Non-commercial use only. No selling and no use in adverts for a business."],
            ["ND", "No changes. Use the work as it is."],
        ], note="CC0 means the creator has given up rights, so the work can be used freely."),
        H("Reading a licence"),
        T("Licences are often long. For everyday decisions, look for four things: **how many computers**, "
          "**who may use it** (home, school or business), **whether you may copy or change it**, and **what you pay after any trial**."),
        CODE("SAMPLE LICENCE (invented for practice)\n"
             "1. This licence lets you install the program on ONE computer.\n"
             "2. Use is for personal and school use only.\n"
             "3. You may not copy or sell the program.\n"
             "4. After 30 days a payment is required.",
             "text", title="Sample licence text"),
        EX("Worked example 1: reading a licence", intro=(
            "A shop owner in Douala reads the sample licence above. He wants to install the program on the shop's 3 till computers for his business. "
            "May he?"), steps=[
            S("Number of computers", text="The licence allows ONE computer. He needs three."),
            S("Type of use", text="It says personal and school use only. A shop is business use."),
            S("After the trial", text="After 30 days a payment is required, so it is shareware or proprietary."),
            S("Conclusion", text="He may not install it on the three tills. He should buy suitable licences or choose a different legal program."),
        ]),
        EX("Worked example 2: software for the school library", intro=(
            "The Bamenda school library has 12 computers and almost no money. It needs a word processor and spreadsheet, a browser and a simple photo editor. "
            "Which legal choices would you suggest?"), steps=[
            S("Office programs", text="LibreOffice is open source and free to install on all 12 computers."),
            S("Browser", text="Firefox is open source and free."),
            S("Photo editing", text="GIMP is open source and free."),
            S("Operating system", text="Keep the licensed system that came with each computer, or use a free Linux system."),
            S("Keep proof", text="Keep receipts and licence keys for anything bought, and a list of what is installed."),
        ]),
        EX("Worked example 3: an image for a poster", intro=(
            "A student wants to use a photo on a poster for a school fair. The photo page says CC BY-SA. "
            "She will change the colours and share the poster with other classes. What must she do?"), steps=[
            S("BY", text="She must give credit to the photographer on the poster."),
            S("SA", text="Her changed poster must be shared under the same CC BY-SA licence."),
            S("Check the rest", text="The licence has no NC or ND, so changes and non-commercial use are allowed."),
        ]),
        H("Common mistakes"),
        MISTAKE("Free means I can do anything", "Freeware can still forbid copying, changing or business use. Read the licence."),
        MISTAKE("Open source means no rules", "Open-source licences have conditions, such as keeping the credit or sharing changes under the same terms."),
        MISTAKE("A trial is a free program", "Shareware is only free for a trial. After that it must be paid for or removed."),
        QUIZ("A cyber cafe wants a word processor on 8 computers at no cost, legally. Which option fits best?",
             ["A cracked copy of a paid suite", "LibreOffice, which is open source", "One paid licence copied to all 8 computers", "A shareware trial reinstalled every month"], 1,
             "LibreOffice is open source and free to install on any number of computers.",
             feedback=["A cracked copy is pirated.", "", "One paid licence covers one computer.", "Shareware must be paid for after the trial. Reinstalling to avoid paying breaks the licence."]),
        QUIZ("A photo is marked CC BY-ND. What does this mean?",
             ["You may use it commercially without credit", "You must credit the creator and use it without changing it",
              "You may change it, but not share it", "Only non-commercial use is allowed"], 1,
             "BY means credit the creator. ND means no changes.",
             feedback=["BY always asks for credit.", "", "ND forbids changes, not sharing.", "Non-commercial is NC, which is not in this licence."]),
        H("Practice questions"),
        PQ("State two differences between proprietary software and open-source software.",
           "Proprietary software must be paid for and you may not copy or change it. Open-source software has open code: you may use, study, change "
           "and share it under conditions, and it is often free of charge."),
        PQ("Explain the difference between freeware and shareware.",
           "Freeware is free to use, usually with closed code. Shareware is free only as a trial; after that you must pay to keep using it or to unlock all features."),
        PQ("A school wants to share its science notes online so that other schools can reuse them but not sell them. Which two Creative Commons conditions should it choose, and why?",
           "BY, so that the school is credited, and NC, so that nobody may sell the notes. It may also add SA if it wants changed versions to stay under the same licence."),
        SUM("A licence is the agreement that says how a program or work may be used. Read the number of computers and the type of use.",
            "Proprietary: paid, closed. Shareware: trial, then pay. Freeware: free, closed. Open source: open code, shared under conditions.",
            "Creative Commons: BY credit, SA same licence, NC non-commercial, ND no changes.",
            "For schools and small businesses, open-source programs are a legal, low-cost choice.",
            "Keep receipts, licence keys and a list of installed programs as proof."),
    ],
))

# ------------------------------------------------------------------ Cameroon legal framework
# REVIEW: legal details kept general on purpose (Law No. 2010/012 and Law No. 2010/013 of 21 December 2010;
# ANTIC and MINPOSTEL roles). No penalties, article numbers or personal data law are named.
LESSONS.append(lesson(
    module=MODULE,
    topic=LAW,
    title="Cybersecurity rules for everyday users",
    slug="law-cybersecurity-rules-for-everyday-users",
    minutes=20,
    summary="Know Law No. 2010/012 on cybersecurity and cybercrime and Law No. 2010/013 on electronic communications in general terms, and see which everyday actions count as misuse.",
    objectives=[
        "Name Law No. 2010/012 and Law No. 2010/013 and say in general what each covers",
        "Recognise everyday actions that are misuse of computers and networks",
        "Describe phishing and mobile money fraud as examples of what the rules aim to stop",
        "Say what to do if you become a victim or see misuse",
    ],
    key_concepts=["Cybercrime", "Cybersecurity", "Unauthorised access", "Phishing", "Law No. 2010/012", "Law No. 2010/013"],
    blocks=[
        H("Introduction"),
        T("Brenda works at a cyber cafe in Molyko, Buea. One day a customer forgets to log out of his social media account. "
          "The next customer starts reading his messages \"just for fun\". Another customer sends fake messages to friends pretending to be a bank.\n\n"
          "Are these only bad manners, or do they break the law? In this lesson you learn the main rules in simple words. "
          "You are not expected to be a lawyer. You are expected to know what is allowed and what is not."),
        D("**Cybercrime** is an offence committed using computers, phones or networks, or against them. "
          "**Cybersecurity** is everything done to protect systems, networks and data from attacks and misuse.",
          title="Definitions"),
        H("Two laws of 2010"),
        KEY("Law No. 2010/012 and Law No. 2010/013", "Both are dated 21 December 2010.", cards=[
            ["Law No. 2010/012", "Relates to cybersecurity and cybercrime. It describes offences such as unauthorised access to systems, interception of communications, damaging data and online fraud."],
            ["Law No. 2010/013", "Governs electronic communications: the organisation and regulation of telecommunication networks and services."],
        ], note="Only the general idea of each law is needed here. For exact wording, check the current official texts and your teacher's notes."),
        T("Think of it this way. Law No. 2010/013 is about the networks and services that carry our calls and data. "
          "Law No. 2010/012 is about what people may and may not do on those networks and with computers."),
        H("What counts as misuse?"),
        T("Computers and networks are like other people's property. You need permission to enter, use or change them. "
          "The kinds of offences named in the cybercrime law include the following."),
        KEY("Kinds of misuse", "In everyday words.", cards=[
            ["Unauthorised access", "Logging in to an account or a computer system that is not yours, without permission. Guessing a friend's password counts, even as a joke."],
            ["Interception", "Secretly reading or recording other people's messages or calls."],
            ["Damaging or changing data", "Deleting, changing or locking someone's files or website without permission, including spreading harmful programs."],
            ["Online fraud", "Using the internet, a phone or a fake page to trick people out of money or information."],
        ]),
        TIP("If you are doing something with another person's account, device or data and you do not have their clear permission, stop and ask. "
            "Good intentions or a joke do not give permission."),
        H("Phishing and mobile money fraud"),
        D("**Phishing** is a trick where a criminal pretends to be a trusted organisation, by SMS, call, email or a fake website, "
          "to make you reveal passwords, PINs or money.", title="Phishing"),
        T("These tricks are examples of the kind of behaviour the cybercrime rules are meant to stop. "
          "They follow the same pattern almost every time."),
        KEY("Warning signs", "Learn the pattern, not the exact words.", cards=[
            ["Too good to be true", "\"You have won\" a prize, a visa or a job you never applied for."],
            ["Urgency", "\"Send money now or your account will be blocked today.\""],
            ["Asking for secrets", "Any request for your PIN, password or the code sent to your phone."],
            ["Odd links or numbers", "A web address that looks almost like a real bank, or a stranger's number."],
        ]),
        EX("Worked example 1: the call from \"mobile money\"", intro=(
            "A student in Bafoussam gets a call: \"I am from your mobile money service. A wrong transfer was made to you. "
            "Give me the code we just sent so we can reverse it.\" What should she do?"), steps=[
            S("Spot the pattern", text="The caller is in a hurry and asks for a secret code. These are warning signs."),
            S("Do not give the code", text="A genuine service never needs your PIN or one-time code. Hang up."),
            S("Check yourself", text="Call the operator's official customer service number. Do not call back the number that rang you."),
            S("If she already gave the code", text="Call the operator at once to block the account, change the PIN, and keep the call details and messages."),
            S("Report", text="Report the number to the operator and to the police or gendarmerie."),
        ]),
        EX("Worked example 2: is this misuse?", intro=(
            "Decide for each case whether it is misuse: (a) Brenda logs out of a customer's account that he left open. "
            "(b) A customer reads another customer's open messages. (c) A student sends an email pretending to be the head teacher to get money. "
            "(d) A shop owner installs antivirus on his own computer."), steps=[
            S("Case (a)", text="Not misuse. She is protecting the customer's privacy. She does not read or change anything."),
            S("Case (b)", text="Misuse. He enters someone else's private messages without permission."),
            S("Case (c)", text="Misuse. It is pretending to be someone else to trick people out of money, which is a form of online fraud."),
            S("Case (d)", text="Not misuse. It is normal protection of his own property."),
        ]),
        H("If something goes wrong"),
        T("If you are a victim, or you see misuse at your workplace, act quickly and keep evidence.\n\n"
          "First, protect yourself: change passwords, block accounts, tell the service provider. "
          "Second, keep evidence: screenshots, messages, numbers and times. "
          "Third, report to your school, your employer, and, where needed, the police or gendarmerie. Do not take revenge yourself."),
        H("Common mistakes"),
        MISTAKE("It is only a joke, so it is not a crime", "Entering a friend's account without permission is unauthorised access even if you meant no harm."),
        MISTAKE("Giving the code because the caller knows my name", "Criminals can find names easily. A real service never asks for your secret code."),
        MISTAKE("Mixing up the two laws", "Law No. 2010/012 is about cybersecurity and cybercrime. Law No. 2010/013 is about electronic communications networks and services."),
        QUIZ("Which law relates to cybersecurity and cybercrime?",
             ["Law No. 2010/013", "Law No. 2010/012", "Both are about the price of data bundles", "Neither: online acts are outside the law"], 1,
             "Law No. 2010/012 relates to cybersecurity and cybercrime. Law No. 2010/013 governs electronic communications.",
             feedback=["That law governs electronic communications.", "", "Neither law is about the price of bundles.", "Cameroon has rules covering online acts."]),
        QUIZ("A message says: \"Your account will be blocked in one hour unless you send your PIN.\" What is the best response?",
             ["Send the PIN quickly to save the account", "Ignore the warning signs because it uses your name",
              "Do not reply; check with the service on its official number", "Forward it to all your friends"], 2,
             "Urgency plus a request for a PIN is a warning sign. Verify by calling the official number.",
             feedback=["A real service never asks for your PIN.", "Using your name does not prove the sender is real.", "",
                       "Forwarding spreads the trick."]),
        H("Practice questions"),
        PQ("Name the law that relates to cybersecurity and cybercrime, and give two kinds of offence it deals with.",
           "Law No. 2010/012 of 21 December 2010. It deals with offences such as unauthorised access to a system, interception of communications, "
           "damaging or changing data without permission, and online fraud (any two)."),
        PQ("Is it misuse when a student logs in to a friend's account to read his messages, if the friend told him his password long ago? Explain.",
           "Yes. Knowing a password is not permission. Using it to enter the account without the friend's present permission is unauthorised access."),
        PQ("List three warning signs of a phishing message, and say what you should do when you receive one.",
           "Any three of: a prize you never expected; urgency; a request for a PIN, password or code; a link or number that looks odd. "
           "Do not reply or click. Contact the real organisation on its official number, and report the message."),
        SUM("Law No. 2010/012 relates to cybersecurity and cybercrime; Law No. 2010/013 governs electronic communications.",
            "Misuse includes unauthorised access, interception, damaging data and online fraud.",
            "Phishing and mobile money fraud use urgency and requests for secrets: never share a PIN or code.",
            "A joke or good intention does not give permission to enter someone's account.",
            "If something goes wrong: protect, keep evidence, report. Check current official texts for exact detail."),
    ],
))

LESSONS.append(lesson(
    module=MODULE,
    topic=LAW,
    title="Data, privacy and the regulators",
    slug="law-data-privacy-and-the-regulators",
    minutes=22,
    summary="Know the roles of ANTIC and MINPOSTEL, understand that personal data rules are developing, and handle customers' data responsibly with consent, strong passwords and backups.",
    objectives=[
        "State the roles of ANTIC and MINPOSTEL",
        "Define personal data and give examples from a cyber cafe or shop",
        "Apply simple rules: collect little, ask consent, keep it safe, delete it",
        "Use strong passwords and sensible backups",
    ],
    key_concepts=["Personal data", "Consent", "ANTIC", "MINPOSTEL", "Strong password", "Backup"],
    blocks=[
        H("Introduction"),
        T("In the previous lesson you learned the main rules about misuse. In this lesson you look at the other side: "
          "how to protect the information that people trust you with.\n\n"
          "Mr Tabi runs a store in Douala. He keeps a notebook of customers who buy on credit, with their names, phone numbers and home areas. "
          "He also keeps a mobile money record on his phone. One day his phone is stolen. Whose information is now at risk?"),
        H("Who looks after ICT in Cameroon?"),
        KEY("Two institutions", "Know who does what.", cards=[
            ["MINPOSTEL", "The Ministry of Posts and Telecommunications. It handles government policy on posts, telecommunications and ICT."],
            ["ANTIC", "The National Agency for Information and Communication Technologies. It regulates and promotes ICT activities and is responsible for the security of networks and information systems, including responding to security incidents."],
        ]),
        T("You do not need to memorise every duty. Remember that **MINPOSTEL is the ministry that sets policy** and "
          "**ANTIC is the agency that regulates ICT and handles security**."),
        H("Personal data"),
        D("**Personal data** is any information that identifies a person: name, phone number, ID card number, photo, address, bank or mobile money details.",
          title="Personal data"),
        T("Rules on personal data protection are still developing in Cameroon. "
          "Always check the current official texts and your teacher's notes for the exact legal position. "
          "The good habits below are right whatever the details."),
        KEY("Five good habits with other people's data", "Use them at school, in a cyber cafe or in a shop.", cards=[
            ["Collect little", "Ask only for what you really need."],
            ["Say why", "Tell the person what you will use the information for."],
            ["Get consent", "Ask permission before you share it or use it for something new."],
            ["Keep it safe", "Lock the notebook, protect the computer and phone with a password."],
            ["Delete it", "Remove it when you no longer need it."],
        ]),
        D("**Consent** means a person freely agrees, after you explain clearly what you want to do with their information.", title="Consent"),
        H("Passwords and backups"),
        T("Two simple tools protect almost everyone's data: strong passwords and backups."),
        KEY("A strong password", "Length and surprise matter more than tricks.", cards=[
            ["Long", "At least 10 or 12 characters. A short sentence works well."],
            ["Different", "Do not use the same password for your email, your phone and your bank."],
            ["Private", "Never share it. Never use your birth date, your name or 123456."],
            ["Extra step", "Where offered, switch on a second step, such as a code sent to your phone."],
        ]),
        D("A **backup** is a copy of important files kept somewhere else, so you can recover them if the original is lost, stolen, damaged or locked by a virus.", title="Backup"),
        T("A sensible habit is to keep **at least two copies** of important files, and keep **one of them in a different place**: "
          "for example, the shop computer, a flash drive kept at home, and a copy online if you have a connection."),
        EX("Worked example 1: Mr Tabi's customer book", intro=(
            "Mr Tabi wants to keep his credit customers' details safe and responsible. Suggest four steps."), steps=[
            S("Collect little", text="Keep only the name, phone number and amount owed. He does not need ID card numbers."),
            S("Tell customers", text="Explain that the details are only for reminding them about payments, and not for advertising."),
            S("Keep it safe", text="Keep the book locked. If it is on his phone, set a password and screen lock."),
            S("Delete old entries", text="When a customer has paid and has not bought for a long time, remove the details."),
        ]),
        EX("Worked example 2: a backup plan for a small shop", intro=(
            "The shop's sales records are on one computer. A power surge could damage it. Plan a simple backup."), steps=[
            S("Choose what to save", text="The sales file, customer list and prices. Not programs, which can be reinstalled."),
            S("Make a second copy", text="At the end of each week copy the files to a flash drive."),
            S("Keep one copy elsewhere", text="Take the flash drive home. If a fire or theft hits the shop, a copy survives."),
            S("Test", text="Once a month open the copy to check it works."),
        ]),
        H("Common mistakes"),
        MISTAKE("Using the same password everywhere", "If one site is attacked, criminals try that password on your other accounts."),
        MISTAKE("Backup on the same computer", "A copy kept on the same machine is lost with it. Keep at least one copy elsewhere."),
        MISTAKE("Sharing customer details without asking", "Giving a customer's number to another business, without consent, breaks trust and may break rules."),
        QUIZ("Which institution is responsible for the security of networks and information systems and regulates ICT activities?",
             ["MINPOSTEL", "ANTIC", "A mobile operator", "The school library"], 1,
             "ANTIC is the National Agency for Information and Communication Technologies. MINPOSTEL is the ministry that sets policy.",
             feedback=["MINPOSTEL is the ministry for posts and telecommunications policy.", "",
                       "An operator is a company that sells network services.", "A library is not a regulator."]),
        QUIZ("Which is the strongest password?",
             ["12345678", "mynameisjohn", "My1stGoat-Bakes-3Mangoes", "password"], 2,
             "It is long, mixes letters, numbers and symbols, and is not an obvious word or name.",
             feedback=["A simple number sequence is guessed first.", "A name and ordinary words are easier to guess.", "",
                       "Common words are tried first by attackers."]),
        H("Practice questions"),
        PQ("State the roles of ANTIC and MINPOSTEL.",
           "MINPOSTEL is the Ministry of Posts and Telecommunications; it handles government policy on posts, telecommunications and ICT. "
           "ANTIC is the National Agency for Information and Communication Technologies; it regulates and promotes ICT activities and is "
           "responsible for the security of networks and information systems."),
        PQ("Give four good habits for handling customers' personal data in a cyber cafe.",
           "Any four of: collect only what is needed; explain why; ask consent; log out and clear history after each customer; delete scanned documents after use; "
           "use strong passwords and keep antivirus updated; do not share information without permission."),
        PQ("Explain why a backup should not be kept only on the same computer, and suggest a better arrangement.",
           "If the computer is stolen, damaged or hit by a virus, the backup is lost too. Better: keep at least two copies, with one in a different place, "
           "such as a flash drive kept at home."),
        SUM("MINPOSTEL sets policy for posts, telecoms and ICT; ANTIC regulates ICT and is responsible for network and information security.",
            "Personal data identifies a person. Rules on personal data are developing, so check current official texts.",
            "Good habits: collect little, say why, get consent, keep it safe, delete it.",
            "Use long, different, private passwords and switch on a second step where offered.",
            "Keep at least two copies of important files, with one in a different place."),
    ],
))

# ------------------------------------------------------------------ Social and economic impact
LESSONS.append(lesson(
    module=MODULE,
    topic=SOCIAL,
    title="ICT at work and in business",
    slug="impact-ict-at-work-and-in-business",
    minutes=22,
    summary="See how mobile money, e-banking, online selling and remote work change business in Cameroon, and weigh the benefits against the problems for jobs and skills.",
    objectives=[
        "Describe how mobile money and e-banking help customers and businesses",
        "Explain how a small business can sell and advertise online and what can go wrong",
        "Describe remote work and the tools it uses",
        "Discuss the effects of ICT on jobs and skills, giving both sides",
    ],
    key_concepts=["Mobile money", "E-banking", "Online selling", "Remote work", "Automation", "Job displacement"],
    blocks=[
        H("Introduction"),
        T("A cocoa cooperative near Kumba sells to a buyer in Douala. Ten years ago, the cooperative's treasurer travelled with cash. "
          "Today the buyer sends money by mobile money, and the cooperative shares prices in a messaging group.\n\n"
          "ICT has changed how people earn, pay and work together. In this lesson you look at the main changes. "
          "As in every discussion question, keep both sides in mind: benefits and problems."),
        H("Money and banking"),
        D("**Mobile money** is a service that lets you store, send and receive money using a mobile phone, usually through an agent or an app. "
          "**E-banking** (electronic banking) lets you use bank services through a phone, the internet or a cash machine.", title="Definitions"),
        KEY("Benefits and problems", "Think about the customer and the business.", cards=[
            ["Benefits", "Pay without carrying cash. Send money to family in another town in minutes. Less queueing at the bank. A record of each payment."],
            ["Problems", "Fees on some transactions. Network or power failure stops the service. Fraud and phishing. People without phones or without ID are left out."],
        ]),
        T("A shop that accepts mobile money can sell to customers who have no cash on them. It must also protect itself. "
          "Check the confirmation message on the shop phone before handing over goods, never share the PIN, and keep records."),
        H("Selling and advertising online"),
        D("**Online selling** (e-commerce) means advertising and selling goods or services over the internet or through social media and messaging apps.", title="Online selling"),
        KEY("What a small seller needs", "A simple setup is enough to begin.", cards=[
            ["Clear pictures and prices", "Good photos with honest descriptions and prices in FCFA."],
            ["A way to pay", "Mobile money or cash on delivery. Keep proof of each payment."],
            ["Delivery", "Agree who delivers, how long it takes, and who pays."],
            ["Trust", "Answer messages quickly. Keep promises. Make clear how a customer can complain."],
        ]),
        H("Remote work"),
        D("**Remote work** (teleworking) means doing your job from a place other than the office, using tools such as email, shared online documents, messaging groups and video calls.", title="Remote work"),
        T("Remote work needs a reliable connection, a charged device and a quiet place. "
          "It saves travel time and cost and lets people in different towns work on the same document. "
          "It also has limits: less face-to-face contact, harder supervision and power cuts."),
        H("Jobs and skills"),
        D("**Automation** means using machines and software to do tasks that people once did by hand. "
          "**Job displacement** means workers lose or change jobs because of it.", title="Automation"),
        KEY("Jobs change, they do not just disappear", "Think about both columns.", cards=[
            ["Less routine work", "Typing pools, filing, hand-written accounts, some cashier tasks."],
            ["New or growing work", "Mobile money agents, phone repairers, web designers, data clerks, network technicians."],
            ["Skills that matter", "Using a keyboard, spreadsheets and the internet; clear writing; online safety; willingness to learn."],
        ]),
        EX("Worked example 1: a shop accepts mobile money", intro=(
            "A shop in Limbe wants to accept mobile money. Give two benefits and two safety rules."), steps=[
            S("Benefit 1", text="Customers can pay without having cash, so the shop may make more sales."),
            S("Benefit 2", text="The shop holds less cash, so there is less risk of theft."),
            S("Safety rule 1", text="Check the confirmation message on the shop phone before giving goods."),
            S("Safety rule 2", text="Never give a PIN or code to anyone, even a caller who says they are from the operator."),
        ]),
        EX("Worked example 2: selling clothes through social media", intro=(
            "A tailor in Bamenda wants to sell clothes through social media. Write a short plan and name one risk."), steps=[
            S("Show the products", text="Take clear photos in good light and post them with sizes and prices in FCFA."),
            S("Order and payment", text="Customers order by message and pay by mobile money. She keeps a list of orders and payments."),
            S("Delivery", text="She agrees the delivery by motorbike or bus and the price with each customer."),
            S("Risk", text="A customer may claim they paid or never received the item. She keeps screenshots and delivery proof to settle disputes."),
        ]),
        H("Common mistakes"),
        MISTAKE("Only writing the advantages", "Questions that say discuss or evaluate expect both benefits and problems. Give at least one of each."),
        MISTAKE("Saying that ICT only destroys jobs", "ICT removes some routine jobs and creates others. Name an example of each."),
        MISTAKE("Trusting a payment message that was not checked", "Fake messages exist. Check the confirmation on the shop phone before giving goods."),
        QUIZ("Which is a likely new job created by mobile money and phones?",
             ["Typing pool clerk", "Phone repairer", "Hand-written ledger clerk", "Manual switchboard operator"], 1,
             "Phone repairers and mobile money agents are jobs created as more people use phones.",
             feedback=["Typing pools have been reduced by computers.", "", "Computerised accounts have reduced hand-written ledgers.", "Switchboards are largely automated."]),
        QUIZ("Which is a problem of remote work for a small team in Cameroon?",
             ["It always costs more than the office", "It needs reliable power and internet", "It is illegal to work from home", "Nobody can use shared documents"], 1,
             "Power cuts and weak networks can stop remote work.",
             feedback=["It often saves travel costs.", "", "Working from home is not illegal.", "Shared documents are a key tool of remote work."]),
        H("Practice questions"),
        PQ("Give two benefits and two problems of mobile money for a small trader.",
           "Benefits: customers can pay without cash; the trader holds less cash and so has less risk of theft; payments are recorded. "
           "Problems: fees; network or power failure; fraud and phishing; customers without phones are left out."),
        PQ("A bank installs a cash machine and a mobile banking app. Describe one effect on customers and one effect on bank workers.",
           "Customers can check balances or withdraw money outside opening hours and queue less. Some routine cashier work is reduced, so some workers may need retraining, "
           "while technical support jobs are created."),
        PQ("Describe three things a small business needs to sell products online successfully.",
           "Any three of: clear photos and prices; a way to pay such as mobile money; a delivery plan; quick replies and honest service; records of orders and payments."),
        SUM("Mobile money and e-banking save time and cash handling, but have fees, fraud risks and access problems.",
            "Online selling needs clear photos and prices, a payment method, delivery and trust.",
            "Remote work saves travel but depends on power, internet and good habits.",
            "Automation reduces some routine jobs and creates new ones: reskilling matters.",
            "In discussion answers, give both sides and one local example."),
    ],
))

LESSONS.append(lesson(
    module=MODULE,
    topic=SOCIAL,
    title="The digital divide and access",
    slug="impact-digital-divide-and-access",
    minutes=20,
    summary="Explain the digital divide through cost, electricity, connectivity, skills and language, and suggest practical steps that schools and communities can take to narrow it.",
    objectives=[
        "Define the digital divide and give examples from Cameroon",
        "Name five barriers to access: cost, electricity, connectivity, skills and language",
        "Match a barrier to a practical solution",
        "Calculate simple costs when planning access for a school or community",
    ],
    key_concepts=["Digital divide", "Access", "Connectivity", "Digital skills", "Community telecentre", "Offline content"],
    blocks=[
        H("Introduction"),
        T("In the previous lesson you saw how mobile money and online selling help businesses. But not everyone can use them. "
          "A farmer in a village near Kumba may have a basic phone, a network only on the hill, and no electricity at home.\n\n"
          "Meanwhile a student in a Yaoundé school has a smartphone, fast internet and a computer lab. "
          "The gap between them is called the **digital divide**."),
        D("The **digital divide** is the gap between people who can access and use ICT (devices, internet and skills) and people who cannot. "
          "It is often seen between towns and villages, richer and poorer families, and younger and older people.", title="Digital divide"),
        H("Five barriers"),
        KEY("Why some people are left out", "A problem often has more than one cause.", cards=[
            ["Cost", "Devices, repairs and data bundles can be too expensive for some families."],
            ["Electricity", "Without power, you cannot charge a phone or run a computer."],
            ["Connectivity", "Network or internet may be weak, slow or missing in some villages."],
            ["Skills", "People need to know how to use a keyboard, a phone app, and how to stay safe online."],
            ["Language", "Much online content is in English or French. It is harder for people who speak mainly a home language."],
        ]),
        T("Disabilities and age can also be barriers. A tool that works only for people who can see a screen or read small text leaves others out."),
        H("What can schools and communities do?"),
        KEY("Practical answers", "Each barrier has a practical response.", cards=[
            ["Cost", "Share devices in a school lab or telecentre. Buy used, repaired devices. Choose cheaper data plans."],
            ["Electricity", "Use solar panels to charge phones and run computers."],
            ["Connectivity", "Use offline content: lessons and books saved on the computer. Download when the network is good, then use it without internet."],
            ["Skills", "Short training sessions for students, parents and traders. Older students teach younger ones."],
            ["Language", "Provide material in French, English and simple local explanations. Use pictures and audio."],
        ]),
        T("A **community telecentre** is a shared place, such as a school lab or cyber cafe, where people can use computers and the internet and learn. "
          "**Offline content** is information saved on a device so it can be used without internet."),
        EX("Worked example 1: the cocoa cooperative", intro=(
            "The Kumba cocoa cooperative has 60 members. Most have basic phones. The secretary has a smartphone. "
            "Network is available only on a hill. Suggest a plan so that all members receive weekly prices."), steps=[
            S("Identify the barrier", text="Basic phones and weak network. Apps and web pages will not reach most members."),
            S("Choose a method that works on any phone", text="Send the prices by SMS every week."),
            S("Use the secretary's phone", text="She collects the prices when she goes up the hill and sends the SMS from there."),
            S("Build skills", text="Teach a few young members to use a spreadsheet so that records are kept well."),
            S("Add power", text="Buy a small solar charger so that the phones are ready to receive messages."),
        ]),
        EX("Worked example 2: planning shared access for a school", intro=(
            "A school has 10 computers and 400 students. The lab is open 8 hours a day on 5 school days a week. "
            "If every student has one 1-hour session per week, will the computers have enough time? Work out the hours."), steps=[
            S("Hours available per week", text="10 computers x 8 hours x 5 days = 400 computer-hours."),
            S("Hours needed per week", text="400 students x 1 hour = 400 hours."),
            S("Compare", text="400 available and 400 needed: it just fits, if no time is lost."),
            S("Think about reality", text="Power cuts and teaching times make this tight. Open the lab after class or on Saturdays to give students extra time."),
        ]),
        H("Common mistakes"),
        MISTAKE("Thinking the divide is only about owning a phone", "People also need electricity, signal, money for data, skills and content they can understand."),
        MISTAKE("Offering a smartphone solution to a basic-phone problem", "A plan that needs a smartphone does not help people who only have a basic phone."),
        MISTAKE("Forgetting running costs", "A computer needs power, repairs and data. A plan must pay for them as well as the first purchase."),
        QUIZ("Which solution best helps people in a village with weak network and basic phones?",
             ["A video-streaming app", "Weekly prices sent by SMS", "A website that needs fast internet", "A desktop program"], 1,
             "SMS works on any phone, with very little network.",
             feedback=["Video needs a smartphone and lots of data.", "", "A fast internet connection is not available.", "A desktop program needs a computer."]),
        QUIZ("A school has frequent power cuts. Which choice helps most?",
             ["Buy more computers", "Install a small solar system for the lab", "Allow students to bring bigger bags", "Remove the internet"], 1,
             "Solar power gives the lab electricity when the grid fails.",
             feedback=["More computers do not help without power.", "", "Bag size has nothing to do with power.", "Removing the internet does not fix power."]),
        H("Practice questions"),
        PQ("Define the digital divide and name three groups between which it is often found in Cameroon.",
           "The digital divide is the gap between people who can access and use ICT and people who cannot. It is often found between towns and villages, richer and poorer families, and younger and older people."),
        PQ("Name five barriers to ICT access and give one solution for any two of them.",
           "Cost, electricity, connectivity, skills and language. Examples: solar panels for electricity; offline content for poor connectivity; shared labs to reduce cost; short training sessions for skills."),
        PQ("A school lab has 12 computers, open 6 hours a day for 5 days a week. How many computer-hours are available each week?",
           "12 x 6 x 5 = 360 computer-hours per week."),
        SUM("The digital divide is the gap between people who can and cannot access and use ICT.",
            "Five barriers: cost, electricity, connectivity, skills and language.",
            "Practical answers: shared labs and telecentres, solar power, offline content, training, and content in local languages.",
            "Choose solutions that work with the devices people really have, such as SMS for basic phones.",
            "Plan running costs, not only the first purchase."),
    ],
))

LESSONS.append(lesson(
    module=MODULE,
    topic=SOCIAL,
    title="Health, safety and the environment",
    slug="impact-health-safety-and-environment",
    minutes=22,
    summary="Use computers in a healthy and safe way, handle e-waste and old equipment responsibly, save energy, and understand how solar power helps in Cameroonian schools and businesses.",
    objectives=[
        "Set up a workstation to reduce strain, and manage screen time",
        "Use cables, sockets and equipment safely",
        "Explain why e-waste is a problem and how to reduce, reuse and recycle",
        "Save electricity and explain where solar power helps",
    ],
    key_concepts=["Ergonomics", "Screen time", "E-waste", "Recycling", "Energy saving", "Solar power"],
    blocks=[
        H("Introduction"),
        T("In the cyber cafe in Buea, students sit for four hours on hard stools, with the screen too high and cables across the floor. "
          "When a computer dies, the owner throws it behind the building. When the electricity goes off, he runs a noisy generator.\n\n"
          "ICT brings many benefits, but it also affects our health, our safety and our environment. "
          "This lesson shows simple ways to reduce those problems."),
        H("Health: ergonomics and screen time"),
        D("**Ergonomics** is arranging equipment and furniture so that people can work comfortably and without injury.", title="Ergonomics"),
        KEY("A healthy workstation", "Small changes prevent back, neck, eye and wrist problems.", cards=[
            ["Chair", "Feet flat on the floor. Back supported. Knees at about a right angle."],
            ["Screen", "About an arm's length away, with the top of the screen at or just below eye level. Avoid glare from windows."],
            ["Keyboard and mouse", "Wrists straight and relaxed, forearms level."],
            ["Breaks", "Stand, stretch and look at something far away often. A common rule is every 20 minutes look at something about 20 feet (6 metres) away for 20 seconds."],
        ]),
        T("Long hours on a screen can tire the eyes and keep you sitting still for too long. "
          "**Screen time** is the time spent looking at screens. Balance it with sleep, exercise, study and time with people. "
          "Take a break every hour, and avoid screens just before sleep."),
        H("Safety with electricity and cables"),
        KEY("Simple safety rules", "Most accidents are easy to prevent.", cards=[
            ["Cables", "Keep them out of walkways, or tape them down. Do not pull a plug by the cable."],
            ["Sockets", "Do not overload a socket or extension board with many devices."],
            ["Liquids and dust", "Keep drinks away from computers. Keep equipment clean and dry."],
            ["Surge protection", "Use a surge protector or voltage stabiliser where power is unstable. Unplug during storms."],
            ["Repairs", "Switch off and unplug before cleaning. Leave opening power supplies to trained technicians."],
        ]),
        H("E-waste"),
        D("**E-waste** is discarded electronic equipment such as phones, computers, printers, chargers and batteries. "
          "It contains harmful substances (for example lead and mercury) and useful materials.", title="E-waste"),
        T("Burning e-waste or throwing it in a river releases poisons into air, soil and water. Follow the order **reduce, reuse, recycle**."),
        IMG("f5i-reduce-reuse-recycle.svg",
            alt="Three steps from best to last: reduce, reuse and repair, recycle",
            caption="Figure 1. The order of actions for old equipment."),
        KEY("What to do", "Before you throw anything away, ask what else could happen to it.", cards=[
            ["Reduce", "Buy durable devices and look after them. Do not replace working devices only for fashion."],
            ["Reuse and repair", "Repair faults, add memory, or give working devices to a school."],
            ["Recycle", "Take what cannot be used to a proper collection or recycling point, if one exists nearby. Never burn it."],
        ], note="Before giving away or recycling a phone or computer, back up your files and erase your personal data."),
        H("Saving energy and using solar power"),
        T("Computers use electricity. Switching off equipment you are not using saves money and reduces pollution. "
          "Use sleep mode, lower the screen brightness, and unplug chargers when not in use."),
        F(r"\text{energy (kWh)} = \text{power (kW)} \times \text{time (hours)}", title="Energy used"),
        T("Here kWh is a **kilowatt-hour**, the unit electricity companies use to measure energy. 1 kilowatt (kW) is 1000 watts (W)."),
        EX("Worked example 1: the cost of a lab left on", intro=(
            "A school lab has 10 computers. Each uses about 60 watts when working. They are used for 8 hours a day. How much energy do they use in one day?"), steps=[
            S("Change watts to kilowatts", text="60 W = 0.06 kW."),
            S("One computer for 8 hours", math=r"0.06 \times 8 = 0.48 \text{ kWh}"),
            S("Ten computers", math=r"0.48 \times 10 = 4.8 \text{ kWh}"),
            S("Meaning", text="Switching the computers off at lunch time and when nobody is there reduces this."),
        ]),
        T("**Solar power** turns sunlight into electricity using panels. In Cameroon it can keep a school lab running, charge phones in villages without grid power, "
          "and run a small shop's lights and computers, with a battery for the evening. Panels and batteries cost money at the start, but the sunshine is free. "
          "Batteries must also be disposed of properly at the end of their life."),
        EX("Worked example 2: a plan for the cyber cafe", intro=(
            "Make a short plan to improve health, safety and the environment in the Buea cyber cafe."), steps=[
            S("Health", text="Use chairs with back support, place screens at eye level, and put a notice asking customers to take a short break each hour."),
            S("Safety", text="Tape down cables, use extension boards that are not overloaded, and use surge protectors."),
            S("E-waste", text="Repair or reuse parts. Send the dead computers to a recycling point instead of burning them."),
            S("Energy", text="Switch off idle computers, and consider solar panels with a battery to cut generator use."),
        ]),
        H("Common mistakes"),
        MISTAKE("Burning old equipment to save space", "Burning releases poisonous smoke and leaves metals in the soil. Take it to a proper collection point."),
        MISTAKE("Giving away a phone without erasing it", "Photos, messages and passwords may remain. Back up and erase first."),
        MISTAKE("Mixing up watts and kilowatt-hours", "Watts measure power at a moment. Kilowatt-hours measure energy used over time: power in kW times hours."),
        QUIZ("Which is the best way to deal with a dead computer that cannot be repaired?",
             ["Burn it with the rubbish", "Throw it into the river", "Take it to a proper collection or recycling point after erasing the data", "Keep it on the floor of the lab"], 2,
             "Recycling keeps poisons out of the environment, and erasing data protects privacy.",
             feedback=["Burning releases poisonous smoke.", "Poisons would enter the water.", "", "It takes space and wastes materials."]),
        QUIZ("Which setup is best for a computer screen?",
             ["Very close and well above eye level", "About an arm's length away, with the top at or just below eye level", "Behind a bright window", "Below knee level"], 1,
             "A comfortable distance and height reduces neck and eye strain.",
             feedback=["This strains the eyes and neck.", "", "Glare from a window tires the eyes.", "Looking down far strains the neck."]),
        H("Practice questions"),
        PQ("Give three ways to reduce the health problems caused by long computer use.",
           "Any three of: take regular breaks; sit with a supported back and feet flat; place the screen at an arm's length with the top near eye level; avoid glare; "
           "keep wrists straight; balance screen time with exercise and sleep."),
        PQ("Explain why e-waste should not be burned, and name the three steps for dealing with old equipment.",
           "Burning releases poisonous smoke and leaves metals such as lead in soil and water. The steps are reduce, reuse and repair, then recycle."),
        PQ("A shop has 5 computers that use 50 W each. They run for 10 hours a day. Calculate the energy used per day in kWh.",
           "50 W = 0.05 kW. For one computer: 0.05 x 10 = 0.5 kWh. For 5 computers: 0.5 x 5 = 2.5 kWh."),
        SUM("Ergonomics reduces strain: supported back, screen at eye level, relaxed wrists and regular breaks.",
            "Keep cables tidy, avoid overloaded sockets and liquids, and use surge protection.",
            "E-waste is harmful: reduce, reuse and repair, then recycle. Never burn it, and erase data first.",
            "Energy in kWh = power in kW x time in hours. Switch off what you are not using.",
            "Solar power helps schools, shops and villages with weak or no grid electricity."),
    ],
))
