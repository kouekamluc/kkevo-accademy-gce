"""Form 5 Computer Science (O Level): Legal, Ethical & Social Aspects, deepened (7 lessons).

REVIEW: Cameroon legal facts are kept to Law No. 2010/012 and Law No. 2010/013 of 21 December 2010,
ANTIC, MINPOSTEL, ART and OAPI, in general terms only. No penalties and no personal-data or copyright
statute are named; lessons tell students to check current texts.
"""

from .dsl import *  # noqa: F403

COURSE = ("computer-science", "form-5")

MODULE = "Legal, Ethical & Social Aspects"
IP = "Intellectual property"
LAW = "Cameroon legal framework"
SOC = "Social and economic impact"

LESSONS = []

# ------------------------------------------------------------------ Intellectual property
LESSONS.append(lesson(
    module=MODULE, topic=IP,
    title="Copyright and software piracy",
    slug="ip-copyright-and-software-piracy",
    minutes=20,
    summary="Learn what intellectual property and copyright are, why copying software without permission (piracy) is illegal and harmful, and how to get software and content legally and honestly.",
    objectives=[
        "Define intellectual property and copyright",
        "Explain that copyright starts automatically when a work is created",
        "Define software piracy and describe its harms to creators, the country and users",
        "Name legal ways to get software and recognise plagiarism",
    ],
    key_concepts=["Intellectual property", "Copyright", "Software piracy", "Plagiarism", "Patent", "Trademark"],
    blocks=[
        H("Introduction"),
        T("Walk past some shops in Douala or Yaoundé and you may see discs or USB keys sold with expensive programs "
          "already installed, for a tiny price. A musician in Bamenda may find her new song shared on WhatsApp the "
          "day after she releases it, and she earns nothing from it.\n\n"
          "Both stories are about one question: who owns the work of a person's mind, and who is allowed to copy it?"),
        H("Intellectual property"),
        D("**Intellectual property** (IP) is a creation of the mind, such as a program, a song, a book, a design, an "
          "invention or a brand name, that the law treats as belonging to its creator.", title="Intellectual property"),
        T("Owning a work of the mind is different from owning a thing. If you buy a book, you own the paper. "
          "The author still owns the text. You may read it, lend it and resell your copy, but you may not print "
          "100 new copies and sell them."),
        D("**Copyright** is the legal right of the creator of an original work, such as software, music, text or a "
          "picture, to control how it is copied, shared, sold or changed.", title="Copyright"),
        T("Copyright starts **automatically** the moment the work is created. The creator does not need to "
          "register it or write a special sign on it. A program you write for a school project is already "
          "protected by copyright. It lasts for a long time, and the exact period is set by law."),
        KEY("Three kinds of intellectual property", "Copyright is only one kind. Do not mix them up.",
            cards=[["Copyright", "Protects the actual work: the code, the text, the song, the picture."],
                   ["Patent", "Protects an invention, such as a new machine or process, for a limited number of years."],
                   ["Trademark", "Protects a brand name or logo, such as the name and logo of a mobile network."]],
            note="Patents and trademarks are registered. Copyright is not. Check your teacher's notes for the national bodies."),
        H("Software piracy"),
        D("**Software piracy** is copying, sharing, selling or using software without the permission of the "
          "copyright owner.", title="Software piracy"),
        T("Piracy takes many forms. Installing one paid copy on ten computers is piracy. So is using a 'cracked' "
          "program, or selling copied discs. Giving a friend a copy of a paid program is also piracy, even if you "
          "charge nothing."),
        T("Who is harmed? **Creators** lose income and may stop making products. **The country** loses because "
          "local software companies find it hard to grow. **Users** are harmed too: cracked programs often "
          "carry viruses or spyware, cannot be updated safely and come with no help when something goes wrong."),
        H("Getting software legally"),
        T("You do not need to pirate to use good software. There are several legal routes. Buy a licence. Ask "
          "whether the maker has a cheaper student or school price. Use free software whose licence allows "
          "free use, such as an open-source office suite. The next lesson explains licences in detail."),
        H("Plagiarism"),
        D("**Plagiarism** is presenting someone else's work, words or code as your own without saying where it came "
          "from.", title="Plagiarism"),
        T("Plagiarism is an ethical wrong in school, even when no law is broken. Copying a classmate's "
          "project or pasting an article into your coursework is plagiarism. To avoid it, write in your own "
          "words, put quotation marks around copied text, and name your sources."),
        EX("Worked example 1: is it legal?", intro=(
            "A cyber cafe owner in Buea buys one licence for a paid office suite and installs it on all 10 "
            "computers. Is this legal? Suggest a legal alternative."), steps=[
            S("Find what the licence allows", text="A single licence normally allows installation on one computer only, unless it says otherwise."),
            S("Compare with what happened", text="The program is on 10 computers, but only one licence was paid for."),
            S("Conclude", text="Nine copies are used without permission. This is software piracy."),
            S("Give a legal alternative", text="Buy enough licences or a multi-user licence, or install a free open-source office suite on every computer."),
        ]),
        EX("Worked example 2: spot the wrong", intro=(
            "A Form 5 student copies three paragraphs from a website into her history project without saying "
            "where they came from. Another student buys a cracked game from a roadside seller. Name the wrong in each "
            "case."), steps=[
            S("First student", text="Plagiarism: she presents other people's words as her own. The fix is to rewrite in her own words and name the source."),
            S("Second student", text="Software piracy: the game is copied without the owner's permission. It may also carry malware."),
            S("Compare", text="Plagiarism is mainly an ethical and school offence. Piracy breaks copyright rules. Both are dishonest."),
        ]),
        H("Common mistakes"),
        MISTAKE("Thinking anything on the internet is free to copy", "Photos, songs and programs online are still protected by copyright unless the owner gives permission."),
        MISTAKE("Thinking copyright must be registered", "Copyright is automatic when the work is created. No form or stamp is needed."),
        MISTAKE("Thinking sharing for free is not piracy", "Piracy is about permission, not about money. Giving away a paid program without permission is still piracy."),
        QUIZ("A student writes a short program for the school science fair. When does copyright in the program begin?",
             ["When he registers it with the government", "When the work is created", "When the program is sold", "When it is published on the internet"], 1,
             "Copyright is automatic. It begins when the original work is created.",
             feedback=["Registration is not needed for copyright.", "",
                       "Copyright exists whether or not the program is ever sold.",
                       "Publishing is not required. The work is protected as soon as it is created."]),
        H("Practice questions"),
        PQ("(a) Define intellectual property. (b) State one example of intellectual property.",
           "(a) Intellectual property is a creation of the mind, such as a program, song, book, design, invention or brand, "
           "that the law treats as belonging to its creator. (b) Any one of: a computer program, a song, a book, a logo, an invention."),
        PQ("Define software piracy and give two examples.",
           "Software piracy is copying, sharing, selling or using software without the permission of the copyright owner. "
           "Examples: installing one paid copy on many computers; using a cracked program; selling copied discs."),
        PQ("Give three harms of software piracy, naming who is harmed.",
           "Creators lose income and may stop making software. The country's local software companies find it hard to grow. "
           "Users risk viruses and spyware in cracked copies and get no updates or support."),
        PQ("A friend offers you a free copy of a paid video editor. Give two reasons to refuse and one legal option.",
           "It is software piracy, which breaks copyright, and the copy may contain malware and cannot be updated safely. "
           "Legal option: use a free editor whose licence allows free use, or ask about a student price."),
        SUM("Intellectual property is a creation of the mind that the law treats as belonging to its creator.",
            "Copyright protects original works such as programs, music, text and pictures, and starts automatically on creation.",
            "Software piracy is copying, sharing, selling or using software without the owner's permission. It harms creators, the country and users.",
            "Get software legally: buy a licence, ask for student prices or use free software that is meant to be free.",
            "Plagiarism is presenting someone else's work as your own. Use your own words and name your sources."),
    ],
))

LESSONS.append(lesson(
    module=MODULE, topic=IP,
    title="Open-source and licences: GPL, MIT and Creative Commons",
    slug="ip-open-source-licences-gpl-mit-cc",
    minutes=22,
    summary="Compare proprietary and open-source software, see what the GPL and MIT licences allow, read Creative Commons labels (BY, SA, NC, ND, CC0) and choose a licence for a school project.",
    objectives=[
        "Explain what a software licence is and compare proprietary and open-source software",
        "State what the GPL and the MIT licence allow",
        "Explain the Creative Commons elements BY, SA, NC, ND and CC0",
        "Choose a suitable licence for a school project and give a reason",
    ],
    key_concepts=["Software licence", "Proprietary software", "Open source", "GPL", "MIT licence", "Creative Commons", "Copyleft"],
    blocks=[
        H("Introduction"),
        T("In the previous lesson you saw that copying software without permission is piracy. So how can a student "
          "in Bamenda legally use a free office suite, or a teacher share a diagram with the whole class? The answer "
          "is the **licence**. Many creators give clear permissions in advance, and the licence says exactly what "
          "you may do."),
        D("A **software licence** is a legal agreement that says how a program may be used, copied, changed and shared. "
          "When you buy software, you normally buy a licence to use it, not the program itself.", title="Software licence"),
        H("Proprietary and open source"),
        KEY("Two ends of the scale", "Licences range from closed to open.",
            cards=[["Proprietary", "Usually paid for. The source code (the instructions written by programmers) is secret. You may not copy or change it. Example: a paid office suite."],
                   ["Open source", "The source code is published. You may study it, change it and share it, following the licence. Examples: Linux, LibreOffice, Firefox."]]),
        T("Two other words appear often. **Freeware** costs nothing but its source code stays closed. **Shareware** "
          "is a free trial, with limits in time or features, before you must pay."),
        TIP("Free of cost is not the same as open source. Freeware is free to use, but you cannot see or change its code.", title="Free is not open"),
        H("GPL and MIT"),
        T("Open-source software still has a licence. Two common ones are the GPL and the MIT licence. Both let you use "
          "and change the code. They differ in what they ask when you share your changes."),
        KEY("GPL and MIT compared", "Same freedom to use. Different rules when sharing.",
            cards=[["GPL (GNU General Public Licence)", "You may use, change and share the code. If you share a changed version, you must share its source code under the GPL too. This rule is called **copyleft**: it keeps the code open."],
                   ["MIT licence", "Very permissive. You may do almost anything, even put the code in a closed, paid product. You only have to keep the original copyright notice."]]),
        H("Creative Commons"),
        T("Programs are not the only things people share. For photos, music, text and teaching materials, many "
          "creators use **Creative Commons** (CC) licences. A CC label is built from short elements."),
        CODE("BY  = Attribution: give credit to the creator\n"
             "SA  = ShareAlike: share your new work under the same licence\n"
             "NC  = NonCommercial: not for making money\n"
             "ND  = NoDerivatives: share it unchanged, do not edit it\n"
             "CC0 = creator gives up rights as far as the law allows;\n"
             "      you may use it freely, credit not required", "text", title="Creative Commons elements"),
        T("Elements are combined. A photo marked CC BY-NC may be used if you credit the photographer and your use "
          "is not commercial. A photo marked CC BY-ND may be shared with credit but not edited. Always read the "
          "licence name on the work."),
        EX("Worked example 1: using a photo", intro=(
            "A student finds a photo licensed CC BY-NC. He wants to put it on the cover of a school magazine that is "
            "sold for 500 FCFA. Has he the right to do so?"), steps=[
            S("Read the elements", text="BY means credit the photographer. NC means non-commercial use only."),
            S("Check the use", text="Selling the magazine is a commercial use, even for a small price."),
            S("Conclude", text="He may not use it, even with credit. He should ask for permission, or choose an image whose licence allows commercial use, such as CC BY or CC0."),
        ]),
        EX("Worked example 2: choosing a licence", intro=(
            "Three students write an app that shows market prices. They want anyone to improve it, but they do not "
            "want a company to take the code, close it and sell it. Which licence, GPL or MIT, suits them?"), steps=[
            S("What MIT allows", text="Anyone may reuse the code in a closed, paid product. That is what the students want to avoid."),
            S("What GPL requires", text="Anyone who shares a changed version must also share its source code under the GPL."),
            S("Conclude", text="The GPL suits them, because copyleft keeps every shared version open."),
        ]),
        H("Choosing for a school project"),
        T("Ask three questions. Do you want others to improve your work? Do you want to force them to share "
          "their changes? Do you mind if companies sell your work? If you want the widest use, MIT is simple. If you "
          "want improvements to stay open, choose the GPL. For a poster or lesson notes, choose a CC label. "
          "Always put a short licence notice in the project folder so others know what is allowed."),
        H("Common mistakes"),
        MISTAKE("Thinking open source means no rules", "Open-source software has a licence with conditions. Breaking those conditions is still a breach."),
        MISTAKE("Ignoring NC and ND", "NC forbids commercial use and ND forbids editing. A paid magazine or a cropped photo can break these."),
        MISTAKE("Thinking CC0 and CC BY are the same", "CC BY requires credit. CC0 does not, because the creator has given up their rights as far as the law allows."),
        QUIZ("Which licence requires that a shared, changed version stay open under the same licence?",
             ["MIT licence", "GPL", "Freeware licence", "Shareware licence"], 1,
             "The GPL is a copyleft licence. Changed versions that are shared must stay open under the GPL.",
             feedback=["The MIT licence is permissive. A changed version may be closed.", "",
                       "Freeware does not give you the source code to share.",
                       "Shareware is try-before-you-buy and its code is closed."]),
        QUIZ("A teacher shares notes marked CC BY-ND. Which use is allowed?",
             ["Sharing the notes unchanged and crediting the teacher", "Editing the notes and posting them without credit",
              "Selling an edited copy", "Removing the teacher's name"], 0,
             "BY requires credit and ND forbids changes, so sharing unchanged with credit is allowed.",
             feedback=["", "ND forbids editing and BY requires credit.", "ND forbids edited copies.", "BY requires the name to stay."]),
        H("Practice questions"),
        PQ("State two differences between proprietary software and open-source software.",
           "Proprietary software is usually paid for and its source code is secret. Open-source software publishes its source code. "
           "Users may not change or share proprietary software, but may change and share open-source software within its licence."),
        PQ("Explain the difference between the GPL and the MIT licence.",
           "Both let you use and change the code. The GPL is copyleft: if you share a changed version, you must share its source code "
           "under the GPL. The MIT licence is permissive: changed versions may be closed or sold, as long as the copyright notice is kept."),
        PQ("Explain what the elements BY, NC and ND mean in a Creative Commons licence.",
           "BY: give credit to the creator. NC: not for commercial use. ND: share the work unchanged, with no edits."),
        PQ("A group wants to share their school science poster so that anyone can print it but nobody can sell it. Which CC elements should they use?",
           "BY-NC: BY so they are credited, and NC so it cannot be sold. They may add ND if they do not want it edited."),
        SUM("A software licence says how a program may be used, copied, changed and shared.",
            "Proprietary software has secret code and strict limits. Open-source software publishes its code and allows study, change and sharing under its licence.",
            "GPL is copyleft: shared changes must stay open. MIT is permissive: only the notice must stay.",
            "Creative Commons: BY credit, SA share alike, NC non-commercial, ND no changes, CC0 rights given up.",
            "Pick a licence by asking who may change, share and sell your work, and add a licence notice to the project."),
    ],
))

# ------------------------------------------------------------------ Cameroon legal framework
LESSONS.append(lesson(
    module=MODULE, topic=LAW,
    title="Cybercrime and cybersecurity law in Cameroon",
    slug="law-cybercrime-and-cybersecurity-cameroon",
    minutes=20,
    summary="Know what cybercrime and cybersecurity mean, the two 2010 Cameroonian laws on cybersecurity and electronic communications, the kinds of offences in general terms, and what a student should and should not do.",
    objectives=[
        "Define cybercrime and cybersecurity",
        "Name Law No. 2010/012 and Law No. 2010/013 and say in general terms what each covers",
        "Recognise common examples of computer misuse and name the offence",
        "State what a student should do, and not do, to stay safe and lawful",
    ],
    key_concepts=["Cybercrime", "Cybersecurity", "Law No. 2010/012", "Law No. 2010/013", "Hacking", "Phishing", "Identity theft"],
    blocks=[
        H("Introduction"),
        T("A trader in Douala receives an SMS: 'You have won 500 000 FCFA. Send 10 000 FCFA by mobile money to "
          "claim your prize.' A student in Buea finds that someone has taken over his social media account and is "
          "asking his friends for money.\n\n"
          "These are not just bad luck. They are **crimes**. Cameroon has laws that treat such acts as offences."),
        D("**Cybercrime** is any illegal act done using a computer, a phone or a network, or aimed at them. "
          "**Cybersecurity** is the set of measures (technical, legal and human) that protect systems, networks and "
          "data from attack, damage or unauthorised access.", title="Definitions"),
        H("The two laws of 2010"),
        KEY("Two laws of 21 December 2010", "Cameroon passed two important laws on the same day.",
            cards=[["Law No. 2010/012", "Relates to cybersecurity and cybercrime in Cameroon. It deals with offences committed through electronic communication networks and information systems."],
                   ["Law No. 2010/013", "Governs electronic communications in Cameroon: how telecommunication networks and services are organised and regulated."]],
            note="Other texts also apply, and laws can change. Check the current texts with your teacher. You do not need to learn penalties."),
        T("Remember the pairing: 012 is about **cybersecurity and cybercrime**, and 013 is about **electronic "
          "communications**. A common slip is to swap them."),
        H("Kinds of offence"),
        T("In general terms, the cybersecurity and cybercrime law treats these kinds of act as offences: "
          "entering a computer system without permission, intercepting messages, damaging or changing data "
          "without permission, committing fraud through networks, and publishing certain illegal content."),
        KEY("Examples of computer misuse", "Learn to recognise each one in a short story.",
            cards=[["Hacking", "Entering a computer, account or network without permission. Looking is an offence even if nothing is changed."],
                   ["Phishing and scams", "Fake messages, calls or websites that trick people into giving PINs, passwords or money, such as a fake mobile money prize."],
                   ["Identity theft", "Using another person's name, photo or account details to pretend to be them."],
                   ["Malware", "Spreading viruses, ransomware or spyware that damage data or spy on users."],
                   ["Altering data", "Changing records without permission, such as school marks or account balances."]]),
        H("What a student should do and not do"),
        CODE("DO\n"
             "- Use only accounts and computers you are allowed to use\n"
             "- Keep passwords and mobile money PINs private\n"
             "- Report scams and strange messages to a teacher or an adult\n"
             "- Ask permission before testing any system\n"
             "\n"
             "DO NOT\n"
             "- Guess or use someone else's password\n"
             "- Change marks, records or files you do not own\n"
             "- Share a link or file you suspect is malware\n"
             "- Pretend to be another person online", "text", title="Student checklist"),
        EX("Worked example 1: name the offence", intro=(
            "A Form 5 student guesses the password of the school results system and changes his own marks. "
            "(a) Name the offences. (b) Name the law. (c) Suggest two measures the school should take."), steps=[
            S("(a) Offences", text="Unauthorised access to a computer system (hacking), and unauthorised alteration of data."),
            S("(b) The law", text="Law No. 2010/012 of 21 December 2010, which relates to cybersecurity and cybercrime."),
            S("(c) School measures", text="Any two of: strong passwords; separate user accounts with limited rights; a log of who changed which record; regular backups."),
        ]),
        EX("Worked example 2: a scam message", intro=(
            "A shopkeeper in Bafoussam gets a call from someone who says he works for a mobile money company and asks "
            "for the shopkeeper's PIN to 'fix a problem'. What is this, and what should the shopkeeper do?"), steps=[
            S("Identify it", text="It is a scam of the phishing type: a trick to get a secret PIN."),
            S("Respond", text="Never give a PIN to anyone. End the call."),
            S("Report", text="Tell the real company through its official line or an agent, and warn other shopkeepers."),
        ]),
        H("Common mistakes"),
        MISTAKE("Thinking cybercrime is only hacking", "Fraud, scams, identity theft and spreading malware are cybercrimes too."),
        MISTAKE("Swapping the two laws", "Law No. 2010/012 is cybersecurity and cybercrime. Law No. 2010/013 is electronic communications."),
        MISTAKE("Saying 'it is only a joke'", "Entering someone's account or changing data without permission is an offence even if you meant it as a joke."),
        QUIZ("Which law relates to cybersecurity and cybercrime in Cameroon?",
             ["Law No. 2010/012", "Law No. 2010/013", "The OHADA Uniform Act", "The Bangui Agreement"], 0,
             "Law No. 2010/012 of 21 December 2010 relates to cybersecurity and cybercrime.",
             feedback=["", "Law No. 2010/013 governs electronic communications.",
                       "OHADA Uniform Acts deal with business law.",
                       "The Bangui Agreement set up OAPI and deals with intellectual property."]),
        QUIZ("A student reads a friend's private messages by using her phone while she is away, without asking. What is this?",
             ["Harmless curiosity", "Unauthorised access to someone's account", "Phishing", "Malware"], 1,
             "Entering someone's account without permission is unauthorised access, even if nothing is changed.",
             feedback=["Looking without permission is still unauthorised.", "",
                       "Phishing tricks people into giving secrets. Here no one was tricked.",
                       "No harmful program was involved."]),
        H("Practice questions"),
        PQ("(a) Define cybercrime. (b) Give three examples.",
           "(a) Cybercrime is an illegal act done using a computer, phone or network, or aimed at them. "
           "(b) Any three of: hacking; phishing and mobile money scams; identity theft; spreading malware; altering data."),
        PQ("Name the Cameroonian law on cybersecurity and cybercrime and say what the other 2010 law covers.",
           "Law No. 2010/012 of 21 December 2010 relates to cybersecurity and cybercrime. Law No. 2010/013 of the same date governs electronic communications."),
        PQ("A student sends fake emails that look like they come from the school bank and asks parents for their card details. Name the offence and give two harms.",
           "Phishing and fraud. Parents may lose money, and their personal data may be used for identity theft. The student may also face legal action and school discipline."),
        PQ("List three things a student should do and two things a student should not do to stay safe and lawful online.",
           "Do: keep passwords and PINs private; use only accounts you are allowed to use; report scams to a teacher. "
           "Do not: guess or use someone else's password; change files or records you do not own."),
        SUM("Cybercrime is illegal activity using or aimed at computers, phones and networks. Cybersecurity protects them.",
            "Law No. 2010/012 (21 December 2010) relates to cybersecurity and cybercrime. Law No. 2010/013 governs electronic communications.",
            "Typical offences: unauthorised access, interception, altering data, fraud through networks and illegal content.",
            "Recognise hacking, phishing, identity theft and malware in short stories.",
            "Students should keep secrets private, use only their own accounts, report scams and check current texts for detail."),
    ],
))

LESSONS.append(lesson(
    module=MODULE, topic=LAW,
    title="Data privacy and the bodies that regulate ICT",
    slug="law-data-privacy-antic-minpostel",
    minutes=20,
    summary="Understand personal data and privacy, the roles of MINPOSTEL, ANTIC and the telecom regulator ART, why rules on personal data are still developing, and good habits with passwords, consent and photos.",
    objectives=[
        "Define personal data and data privacy",
        "State the roles of MINPOSTEL and ANTIC, and name ART",
        "Explain that personal data rules are developing and that current texts must be checked",
        "Apply good habits: strong passwords, consent and careful sharing of photos",
    ],
    key_concepts=["Personal data", "Data privacy", "Consent", "ANTIC", "MINPOSTEL", "ART", "Strong password"],
    blocks=[
        H("Introduction"),
        T("In the previous lesson you saw the 2010 laws. This lesson looks at two further ideas. First: who looks "
          "after ICT in Cameroon? Second: how do we protect information about people?\n\n"
          "Think of a school that keeps student names, phone numbers and results on a computer. Think of a mobile money "
          "agent who writes down ID numbers. This information is **personal data**."),
        D("**Personal data** is any information that identifies a person: name, phone number, address, ID card number, "
          "photo, school records or bank details. **Data privacy** is a person's right to control how their personal data "
          "is collected, used and shared.", title="Definitions"),
        H("The bodies that regulate ICT"),
        KEY("Who does what", "Learn one clear role for each body.",
            cards=[["MINPOSTEL", "The Ministry of Posts and Telecommunications. It prepares and carries out government policy on posts, telecommunications and ICT."],
                   ["ANTIC", "The National Agency for Information and Communication Technologies. It promotes and regulates ICT activities and is in charge of the security of electronic communication networks and information systems."],
                   ["ART", "The Telecommunications Regulatory Board. It is the regulator for telecom operators."]],
            note="Roles are described in general terms. Check the current texts and your teacher's notes."),
        T("A simple way to remember: the **ministry** makes policy, the **agency** (ANTIC) works on ICT "
          "development and network security, and the **regulator** (ART) watches the telecom operators."),
        H("Personal data rules are developing"),
        T("Rules on personal data protection are still developing in many countries, including Cameroon. This "
          "course does not give details of any particular text. If you need the exact rules, for example for a school "
          "project that collects data, check the current texts and ask your teacher."),
        T("Even without exact rules, good practice is clear. Collect only what you need. Say why you need it. "
          "Keep it safe. Do not share it without the person's **consent**, which means their clear permission. Delete "
          "it when it is no longer needed."),
        H("Good habits"),
        KEY("Three habits to practise", "Small habits protect you and others.",
            cards=[["Passwords", "Use a long password with letters, numbers and symbols. Use a different one for each important account. Never share it. Switch on two-step login if offered."],
                   ["Consent", "Ask before you collect or share someone's details. Ask before you post a photo of a friend."],
                   ["Photos", "A photo shows faces, places and uniforms. Before you post, think: who can see it, can it be copied, would the person mind?"]]),
        CODE("Weak:   school123           (short, guessable)\n"
             "Better: Bamenda-Rain-Mango-47   (long, easy to remember, not a real sentence from your life)\n"
             "Rule:   a different password for each important account", "text", title="Choosing a password"),
        EX("Worked example 1: protecting customer data", intro=(
            "A mobile money agent in Bafoussam keeps a notebook with each customer's name, phone number and ID "
            "number, and leaves it on the counter. Explain two risks and two ways to protect the data."), steps=[
            S("Risk 1", text="Anyone at the counter can read and copy the ID numbers and use them for fraud."),
            S("Risk 2", text="The notebook can be lost or stolen and there is no backup."),
            S("Protection 1", text="Keep it in a locked drawer, or in a password-protected computer file."),
            S("Protection 2", text="Record only the data really needed and let only the agent see it."),
        ]),
        EX("Worked example 2: a class photo", intro=(
            "A student wants to post a photo of the whole class, with names, on a public page. Give two things "
            "she should do first."), steps=[
            S("Ask for consent", text="Ask the people in the photo, and the teacher, whether they agree."),
            S("Limit the details", text="Leave out full names and school location, and post to a closed group if possible."),
            S("Be ready to remove it", text="If someone objects, take it down."),
        ]),
        H("Common mistakes"),
        MISTAKE("Mixing up ANTIC and MINPOSTEL", "MINPOSTEL is the ministry that makes policy. ANTIC is the agency for ICT regulation and network security."),
        MISTAKE("Naming laws you are not sure of", "Do not invent law names or details. If unsure, say rules on personal data are developing and should be checked."),
        MISTAKE("Using one password everywhere", "If one site is attacked, all your accounts are at risk. Use different passwords."),
        QUIZ("Which body prepares and carries out government policy on posts, telecommunications and ICT?",
             ["ANTIC", "MINPOSTEL", "ART", "A telecom operator"], 1,
             "MINPOSTEL is the Ministry of Posts and Telecommunications and handles government policy.",
             feedback=["ANTIC is the agency for ICT development and network security.", "",
                       "ART is the regulator for telecom operators.",
                       "Operators provide services. They do not set government policy."]),
        QUIZ("Which is the best way to post a friend's photo?",
             ["Post it at once, because it is a nice photo", "Ask the friend first and post only if she agrees",
              "Post it with her phone number", "Post it after changing her name"], 1,
             "Consent comes first. Asking shows respect for privacy.",
             feedback=["Nice photos can still embarrass or expose a person.", "",
                       "A phone number is personal data and should not be shared.",
                       "Changing a name does not remove her face or give her a say."]),
        H("Practice questions"),
        PQ("(a) Define personal data. (b) Give three examples.",
           "(a) Personal data is information that identifies a person. (b) Any three of: name, phone number, address, ID number, photo, school record, bank details."),
        PQ("State one role of MINPOSTEL and one role of ANTIC.",
           "MINPOSTEL prepares and carries out government policy on posts, telecommunications and ICT. ANTIC promotes and regulates ICT activities and is in charge of the security of electronic networks and information systems."),
        PQ("Give four ways a school can protect the personal data of students.",
           "Any four of: collect only the data needed; use strong passwords and limited user accounts; lock away paper records; make backups; "
           "do not share data without consent or a legal reason; train staff; delete data that is no longer needed."),
        PQ("Explain why students should check current texts about personal data and not rely only on their notes.",
           "Rules on personal data are still developing and laws can change, so notes may be out of date. Students should check current texts and ask their teacher."),
        SUM("Personal data identifies a person. Data privacy is the person's right to control how it is collected, used and shared.",
            "MINPOSTEL makes ICT and telecom policy. ANTIC promotes and regulates ICT and works on network security. ART regulates telecom operators.",
            "Rules on personal data are developing. Check current texts and your teacher's notes.",
            "Good habits: strong different passwords, ask consent, think before posting photos.",
            "Collect only what you need, keep it safe, share only with consent."),
    ],
))

# ------------------------------------------------------------------ Social and economic impact
LESSONS.append(lesson(
    module=MODULE, topic=SOC,
    title="The digital divide",
    slug="impact-the-digital-divide",
    minutes=18,
    summary="Understand the digital divide, its causes (access, cost, electricity, skills, language), the rural and urban gap, and practical ways to reduce it, with mobile phones and mobile money as examples.",
    objectives=[
        "Define the digital divide",
        "Explain causes: access, cost, electricity, skills and language",
        "Describe the rural and urban gap with examples",
        "Suggest ways to reduce the divide and explain how each helps",
    ],
    key_concepts=["Digital divide", "Access", "Infrastructure", "Digital skills", "Mobile money", "Telecentre"],
    blocks=[
        H("Introduction"),
        T("In Yaoundé, a student can follow an online lesson on a phone with a good data connection. In a village far "
          "from a main road, there may be no electricity at night, and the network may drop every few minutes. Two "
          "students of the same age and ability have very different chances to learn online."),
        D("The **digital divide** is the gap between people who have good access to computers, phones, the internet and "
          "the skills to use them, and people who do not.", title="Digital divide"),
        H("Causes of the divide"),
        KEY("Five causes to remember", "One cause often leads to another.",
            cards=[["Access and infrastructure", "No network signal or no broadband in some areas. Few computers at school."],
                   ["Cost", "Phones, computers and data bundles are expensive compared with many incomes."],
                   ["Electricity", "Power cuts or no power at all make charging and using devices difficult."],
                   ["Skills", "Many people have never been taught to use computers or to judge online information."],
                   ["Language and content", "Much online content is in one or two languages. Little is in home languages or about local needs."]]),
        T("The divide is not only between rural and urban areas. It also exists between rich and poor families, "
          "between men and women in some places, and between older and younger people."),
        H("Rural and urban"),
        T("Towns usually have better networks, more shops that repair phones, more cyber cafes and more schools "
          "with computers. Villages often have fewer of these. A rural student may need to travel to a town to use "
          "a computer or buy a data bundle."),
        H("Phones and mobile money"),
        T("Mobile phones have helped narrow the gap. Many people who never owned a computer now have a phone. "
          "Mobile money lets people send and receive money without a bank branch, which is useful where banks are "
          "far away. A phone can also give weather information to farmers or school notes to students."),
        T("But a basic phone does not remove the divide. A phone with a small screen and little data is hard to "
          "use for long documents. Mobile data is costly. Skills and trust are still needed to use mobile money safely."),
        H("Ways to reduce the divide"),
        KEY("Practical measures", "Match each measure to a cause.",
            cards=[["Extend networks and power", "More coverage and solar power for schools and health centres."],
                   ["Share resources", "School computer labs, community telecentres and libraries that anyone can use."],
                   ["Lower costs", "Cheaper devices, cheaper data, student bundles, second-hand devices kept in good order."],
                   ["Teach skills", "ICT lessons in school and short courses for adults."],
                   ["Local content", "Lessons and information that work offline and are in familiar languages."]]),
        EX("Worked example 1: three measures", intro=(
            "Suggest three measures to help students in a rural secondary school use computers, and explain how "
            "each helps."), steps=[
            S("Power", text="Install solar panels, because many villages have unreliable electricity."),
            S("Access", text="Equip a school computer lab or telecentre, because most families cannot buy computers."),
            S("Offline content", text="Provide lessons that work without the internet, because the connection is weak or costly."),
        ]),
        EX("Worked example 2: a balanced view of mobile money", intro=(
            "A farmer near Bamenda starts receiving payment for crops by mobile money. Explain one way this narrows "
            "the digital divide and one way a gap remains."), steps=[
            S("How it narrows the gap", text="The farmer can receive and send money without travelling to a bank."),
            S("Gap that remains", text="He needs network coverage, a charged phone, and the skills to avoid scams. Without these he cannot use it safely."),
            S("Conclude", text="Mobile money reduces the gap but does not remove it."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying the divide is only about computers", "It includes phones, internet, electricity, skills and useful content."),
        MISTAKE("Listing causes without explaining", "Say how: 'Data is costly, so students go online less.' One short reason earns the mark."),
        MISTAKE("Thinking phones solve everything", "Phones help, but cost, coverage, skills and language remain."),
        QUIZ("Which is the best example of the digital divide?",
             ["A student types faster than his friend", "Town students have a good connection while many village students have none",
              "A company buys a printer", "A virus deletes school files"], 1,
             "The digital divide is unequal access to ICT and the skills to use it, often between towns and villages.",
             feedback=["Typing speed is a personal skill difference, not a gap in access between groups.", "",
                       "Buying equipment is not a gap between groups.", "That is a security problem."]),
        H("Practice questions"),
        PQ("Define the digital divide and give two causes.",
           "The digital divide is the gap between those with good access to ICT and the skills to use it and those without. Causes: cost of devices and data; weak network and electricity; lack of skills; little local-language content."),
        PQ("Explain why some students in rural areas are on the wrong side of the digital divide.",
           "Networks may be weak, electricity unreliable, devices and data costly, few teachers trained, and few computers at school."),
        PQ("Give three ways to reduce the digital divide and say who could do each.",
           "Build networks and solar power (government and operators); open school labs and telecentres (schools and communities); lower costs and train people (government, operators and schools)."),
        PQ("Give one advantage and one limit of mobile money for people in villages.",
           "Advantage: sending and receiving money without a bank branch. Limit: needs network, charged phone and skills; scams are a risk."),
        SUM("The digital divide is the gap in access to ICT and the skills to use it.",
            "Causes include weak networks, cost, electricity, low skills and little local-language content.",
            "The gap is large between towns and villages, and also between rich and poor.",
            "Phones and mobile money help, but do not remove the divide.",
            "Ways to reduce it: networks and power, shared labs, lower costs, training and local content."),
    ],
))

LESSONS.append(lesson(
    module=MODULE, topic=SOC,
    title="Automation and job change",
    slug="impact-automation-and-job-change",
    minutes=18,
    summary="Understand automation, how it removes some jobs and creates others, the new skills people need, and how to write a balanced answer with examples from banking, farming, transport and retail.",
    objectives=[
        "Define automation and job displacement",
        "Give examples of jobs reduced and jobs created",
        "Explain the new skills workers need",
        "Write a balanced answer about the effects of automation",
    ],
    key_concepts=["Automation", "Job displacement", "Retraining", "New skills", "Balanced view"],
    blocks=[
        H("Introduction"),
        T("Ten years ago, a customer at a bank in Douala may have queued for a cashier. Today, many customers use a cash "
          "machine or a phone app. The cashier's work has changed, and the bank also needs people to look after the "
          "machines and the app.\n\n"
          "This lesson looks at how computers change jobs. It is not a story of only good news or only bad news."),
        D("**Automation** is the use of computers and machines to do tasks with little or no human help.",
          title="Automation"),
        D("**Job displacement** happens when workers lose their jobs, or part of their work, because a machine "
          "or a program now does it.", title="Job displacement"),
        H("Jobs reduced and jobs created"),
        T("Automation usually changes jobs in two ways. It reduces the need for people to do routine, repeated "
          "tasks. It creates new work in making, running, repairing and improving the machines and programs."),
        KEY("Examples by sector", "Look for both effects in each.",
            cards=[["Banking", "Cash machines and mobile apps reduce routine counter work. Banks need app developers, network staff and customer support."],
                   ["Farming", "Pumps, tractors and phone apps for prices or weather can reduce hand labour. New work: machine repair, drone or sensor use, and selling produce online."],
                   ["Transport", "Ticketing apps and GPS change how drivers and agencies work. New work: app support, booking and fleet tracking."],
                   ["Retail", "Barcode scanners, stock software and mobile payments reduce hand counting. New work: stock analysis and online shop management."]]),
        TIP("Do not say jobs simply disappear. Say which tasks a machine takes over and what new work appears.", title="Wording"),
        H("New skills"),
        T("When tasks change, workers must learn new skills. These include using computers and phones, "
          "working with data, fixing devices, communicating clearly and keeping learning. This is called "
          "**retraining**. A person who repairs radios may learn to repair phones. A clerk who used to file papers "
          "may learn to manage a database."),
        T("Not everyone can retrain easily. Training costs money and time, and some people have little access to "
          "courses. Good answers admit this."),
        H("A balanced view"),
        T("Automation can bring faster work, fewer errors, safer work and lower costs. It can also cause job "
          "loss, a need for new skills and a gap between those who can adapt and those who cannot. A fair answer "
          "gives both sides and names who is affected."),
        EX("Worked example 1: banking", intro=(
            "Explain how cash machines and mobile banking may affect bank workers in Cameroon. Give one "
            "advantage and one disadvantage."), steps=[
            S("Say what changes", text="Customers do simple deposits, withdrawals and balance checks by machine or phone."),
            S("Advantage", text="Shorter queues, service outside opening hours, and cashiers can help with harder tasks."),
            S("Disadvantage", text="Fewer routine counter jobs. Cashiers may need to retrain."),
            S("New jobs", text="Technicians, app developers and customer support."),
        ]),
        EX("Worked example 2: farming", intro=(
            "A cocoa farmer near Mbalmayo starts using a phone to check market prices and sell directly to buyers. "
            "State two benefits and one concern."), steps=[
            S("Benefit 1", text="He sees the current price and does not rely only on middlemen."),
            S("Benefit 2", text="He saves time and travel money."),
            S("Concern", text="He needs a phone, network and skills. Without them he may lose out to those who have them."),
        ]),
        H("Common mistakes"),
        MISTAKE("One-sided answers", "If a question says 'discuss', give advantages and disadvantages. One side loses marks."),
        MISTAKE("Saying computers only destroy jobs", "Automation also creates jobs. Name some, such as network technicians and phone repairers."),
        MISTAKE("Vague answers", "Do not write 'it is good for business'. Say how: 'Cash machines reduce queues.'"),
        QUIZ("Which is a job likely to be created by automation?",
             ["Cashier doing only hand counting", "Network technician", "Typist for handwritten letters", "Paper filing clerk"], 1,
             "Automated systems need technicians to install and repair them.",
             feedback=["Hand counting is a routine task that machines take over.", "",
                       "Word processors reduce this work.", "Digital records reduce paper filing."]),
        H("Practice questions"),
        PQ("Define automation and give one example in a shop.",
           "Automation is the use of computers and machines to do tasks with little or no human help. Example: a barcode scanner and stock program that count and record sales."),
        PQ("Explain, with examples, how automation can cause both job losses and job creation.",
           "Losses: cash machines and mobile banking reduce routine counter work. Creation: technicians, app developers, phone repairers and mobile money agents are needed."),
        PQ("Name two skills workers need to adapt to automation and explain why.",
           "Computer or phone skills, because more tasks use them; problem solving and learning new tools, because tasks change often."),
        PQ("Give a balanced conclusion on whether automation helps or harms workers.",
           "Automation can make work faster, safer and cheaper and create new jobs, but it can remove routine jobs. Workers who retrain benefit most; those without access to training may lose out. Support for retraining makes the change fairer."),
        SUM("Automation is the use of computers and machines to do tasks with little human help.",
            "Job displacement is job loss because a machine or program does the work.",
            "Automation reduces routine work and creates new work in banking, farming, transport and retail.",
            "Workers need new skills and retraining, which is not equally available to all.",
            "Give both sides, with examples, in discussion answers."),
    ],
))

LESSONS.append(lesson(
    module=MODULE, topic=SOC,
    title="E-waste and remote collaboration",
    slug="impact-e-waste-and-remote-collaboration",
    minutes=20,
    summary="Understand what e-waste is, why it is hazardous, and how to reuse, repair and recycle; then weigh the benefits and problems of remote work and learning tools such as video calls and shared documents.",
    objectives=[
        "Define e-waste and explain why it is hazardous",
        "Describe reuse, repair and recycling",
        "Define remote collaboration and name common tools",
        "Give benefits and problems of remote work and learning, including connectivity and distraction",
    ],
    key_concepts=["E-waste", "Reuse", "Repair", "Recycle", "Remote collaboration", "Teleworking", "Connectivity"],
    blocks=[
        H("Introduction"),
        T("In a Douala market you may see a pile of broken phones, screens and old computers behind a repair stall. "
          "They have served their owners and now must go somewhere. At the same time, a student in Buea may join a "
          "class by video call, and a company may let staff work from home.\n\n"
          "This lesson covers two sides of the digital world: what to do with old devices, and how people work and "
          "learn together at a distance."),
        H("E-waste"),
        D("**E-waste** (electronic waste) is thrown-away electrical and electronic equipment, such as old phones, "
          "computers, screens, chargers and batteries.", title="E-waste"),
        T("E-waste is hazardous because many devices contain harmful substances such as lead, mercury and "
          "cadmium. If devices are burnt or dumped in the open, these substances can pollute soil, water and air and "
          "harm the people who handle them. E-waste also contains useful materials that are lost when it is dumped."),
        KEY("Three ways to manage e-waste", "Think in this order: repair, reuse, recycle.",
            cards=[["Repair", "Fix a broken device so it lasts longer. Phone repairers in town markets already do this."],
                   ["Reuse", "Give working devices to a younger sibling or school. Sell or swap them."],
                   ["Recycle", "Take dead devices to a collection point so that safe handling can recover materials. Do not burn them."]],
            note="Exact collection points differ by town. Ask your teacher or local authority."),
        H("Remote collaboration"),
        D("**Remote collaboration** is people working or learning together from different places using ICT tools. "
          "**Teleworking** is doing a job from home or another place away from the office.", title="Remote collaboration"),
        T("Common tools are email, messaging apps, video calls, shared online documents and cloud storage. "
          "Teachers can send notes to a class group. Students can edit a project together without meeting."),
        KEY("Benefits and problems", "Always look at both.",
            cards=[["Benefits", "Saves travel time and money. Lets people join from far away. Flexible hours. Shared documents keep everyone on one version."],
                   ["Problems", "Poor connectivity and power cuts. Data costs. Distraction at home. Feeling alone. Harder to see if someone is stuck."]]),
        H("Making remote work better"),
        T("Plan for the connection. Download notes before the call. Choose audio-only if video is too heavy. Agree "
          "a time and an agenda. Put your phone on silent and close other apps to reduce distraction. Save work "
          "often, because power can fail."),
        EX("Worked example 1: a balanced answer on teleworking", intro=(
            "A company in Douala lets its accountants work from home three days a week. Give two advantages and two "
            "disadvantages."), steps=[
            S("Advantage 1", text="Less money and time spent on taxis in traffic."),
            S("Advantage 2", text="More flexible hours, so family and work are easier to balance."),
            S("Disadvantage 1", text="Power cuts and weak internet can stop work."),
            S("Disadvantage 2", text="Distraction at home and less contact with colleagues."),
        ]),
        EX("Worked example 2: a phone repairer and e-waste", intro=(
            "A repairer in Bamenda keeps broken phones. Explain how repair, reuse and recycling together reduce "
            "e-waste."), steps=[
            S("Repair", text="He fixes phones with a cracked screen or a bad battery, so they stay in use."),
            S("Reuse", text="Parts from phones that cannot be fixed are used to repair others."),
            S("Recycle", text="What cannot be reused goes to a proper collection point and is not burnt."),
        ]),
        H("Common mistakes"),
        MISTAKE("Vague answers about the environment", "Be specific: e-waste releases harmful metals like lead and mercury into soil and water when burnt or dumped."),
        MISTAKE("Burning old devices to get rid of them", "Burning releases poisonous smoke. Repair, reuse or take devices to a collection point."),
        MISTAKE("Listing only benefits of remote work", "Give problems too, such as connectivity and distraction."),
        QUIZ("Why is burning old phone batteries dangerous?",
             ["It uses too much power", "It releases poisonous substances into air and soil", "It makes the phone slower", "It is cheaper than recycling"], 1,
             "Burning releases harmful substances that can damage health and the environment.",
             feedback=["The danger is toxic smoke and residue, not power use.", "",
                       "The phone is already being thrown away.", "Cost is not the main reason. Safety is."]),
        H("Practice questions"),
        PQ("(a) What is e-waste? (b) Give two dangers of e-waste.",
           "(a) E-waste is discarded electrical and electronic equipment such as phones, computers and batteries. (b) Harmful metals like lead and mercury pollute soil and water; burning gives poisonous smoke that harms health."),
        PQ("Give three ways to reduce e-waste.",
           "Repair devices; reuse or donate working ones; recycle through proper collection points; buy durable devices."),
        PQ("Define remote collaboration and name two tools.",
           "Remote collaboration is working or learning together from different places using ICT. Tools: video calls, shared online documents, messaging apps, email."),
        PQ("A school plans online lessons for students at home. Give two problems and one way to reduce each.",
           "Weak connectivity: send notes in advance or use audio only. Distraction: agree a timetable, silence phones and close other apps."),
        SUM("E-waste is discarded electronic equipment such as phones, computers and batteries.",
            "It is hazardous because lead, mercury and cadmium can pollute and harm health. Do not burn it.",
            "Manage e-waste by repairing, reusing and recycling.",
            "Remote collaboration uses email, video calls, shared documents and messaging apps.",
            "Give both benefits and problems: travel savings versus connectivity, cost and distraction."),
    ],
))
