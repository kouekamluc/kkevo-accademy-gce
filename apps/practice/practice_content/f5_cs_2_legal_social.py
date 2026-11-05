"""Form 5 Computer Science: practice sets for Legal, Ethical & Social Aspects (one per lesson)."""

from .dsl import *  # noqa: F403

COURSE = ("computer-science", "form-5")

MODULE = "Legal, Ethical & Social Aspects"
IP = "Intellectual property"
LAW = "Cameroon legal framework"
SOC = "Social and economic impact"

SETS = []

# ------------------------------------------------------------------ 1 Copyright and piracy
SETS.append(practice_set(
    module=MODULE, topic=IP,
    title="Copyright, piracy and plagiarism", lesson="ip-copyright-and-software-piracy",
    questions=[
        MC("What is intellectual property?", [
            C("Land and buildings owned by a school", why="That is physical property. Intellectual property is a creation of the mind."),
            C("A creation of the mind, such as a program, song or design, that the law treats as belonging to its creator", correct=True),
            C("Any file stored on a computer", why="Storing a file does not make it your intellectual property. Someone else may own the work."),
            C("Only inventions that have a patent", why="Patents are one kind of intellectual property. Copyright and trademarks are also included."),
        ], steps=[S("Recall the definition", text="Intellectual property is a creation of the mind that the law treats as belonging to its creator.")],
           concept="Intellectual property", skill="Recall", hint="Think of the word 'intellect': it is about the mind.",
           feedback="Correct. Programs, songs, books and brand names are all intellectual property."),
        MC("When does copyright in a student's original program begin?", [
            C("When the student pays a registration fee", why="Copyright does not need a fee or registration."),
            C("When the program is sold for the first time", why="Copyright exists whether or not the work is sold."),
            C("When the program is created", correct=True),
            C("After the student is 18 years old", why="Age does not decide whether copyright exists."),
        ], steps=[S("Recall the rule", text="Copyright is automatic. It begins when the original work is created.")],
           concept="Copyright is automatic", skill="Recall", hint="Does the law ask you to fill in a form first?",
           feedback="Copyright starts automatically on creation."),
        MC("Which of these is software piracy?", [
            C("Using a free open-source office suite whose licence allows it", why="The licence gives permission, so this is legal."),
            C("Buying a licence and using the program on the computer named in it", why="This follows the licence, so it is legal."),
            C("Installing a program from a legal store on your own phone", why="A normal install from a legal store is allowed."),
            C("Installing one paid copy on ten computers when the licence covers one", correct=True),
        ], steps=[S("Check permission", text="Piracy means copying or using software without the owner's permission."),
                  S("Compare", text="Only the ten-computer case goes beyond the licence.")],
           concept="Software piracy", skill="Concept", hint="Ask: does the owner's permission cover this use?",
           feedback="Using more copies than the licence allows is piracy."),
        MC("Which is a harm of using a cracked program?", [
            C("It is always faster", why="Speed is not a result of cracking. Cracked copies often have problems."),
            C("It may carry viruses and cannot be updated safely", correct=True),
            C("It gives you a longer licence", why="A cracked copy has no valid licence."),
            C("It helps the developer to earn money", why="The developer earns nothing from a cracked copy."),
        ], steps=[S("Think about users", text="Cracked copies often hide malware and miss updates and support.")],
           concept="Harms of piracy", skill="Concept", hint="Where does a cracked copy come from, and who checks it?",
           feedback="Malware and no updates are the main risks to users."),
        MC("A Buea student gives a friend a copy of a paid game but charges nothing. Is this piracy?", [
            C("No, because no money changed hands", why="Piracy is about permission, not payment."),
            C("No, because they are friends", why="Friendship does not give permission to copy."),
            C("Yes, only if the friend sells it", why="Copying without permission is already piracy."),
            C("Yes, because copying without the owner's permission is piracy even if free", correct=True),
        ], steps=[S("Look for permission", text="The owner did not allow copies."),
                  S("Decide", text="So giving a copy is piracy even if it is free.")],
           concept="Piracy and money", skill="Reasoning", hint="Does piracy depend on money, or on permission?",
           feedback="Permission is what matters."),
        MC("Which action is plagiarism?", [
            C("Quoting a sentence in quotation marks and naming the book", why="This gives credit, so it is not plagiarism."),
            C("Copying a classmate's project and handing it in as your own", correct=True),
            C("Writing your own summary after reading an article and listing the article", why="This is honest use of a source."),
            C("Using a CC BY image with credit", why="Credit is given as the licence asks."),
        ], steps=[S("Recall", text="Plagiarism is presenting someone else's work as your own."),
                  S("Match", text="Only copying and handing it in as your own fits.")],
           concept="Plagiarism", skill="Application", hint="Who is said to have made the work?",
           feedback="Plagiarism is claiming other people's work."),
        MC("A Douala cyber cafe owner wants 8 computers to run a paid editor but has money for only one licence. Which is the best legal choice?", [
            C("Copy the program onto 8 computers and hide it", why="This is piracy even if hidden."),
            C("Ask a friend to crack it", why="Cracking is illegal and risky."),
            C("Use a free editor whose licence allows free use, or ask about a multi-user or school price", correct=True),
            C("Install it on 8 computers but only use 1 at a time", why="The licence terms still decide, and one licence usually means one install."),
        ], steps=[S("List legal routes", text="Buy more licences, ask for a lower price, or use a free program that is meant to be free.")],
           concept="Legal ways to get software", skill="Application", hint="Which choice follows the owner's permission?",
           feedback="Legal alternatives exist."),
        MC("Which statement about copyright is correct?", [
            C("It protects ideas, not the way they are written", why="Copyright protects the work itself, such as the code or text, not the bare idea."),
            C("It must be registered before it applies", why="It is automatic."),
            C("It stops all copying in every case", why="Licences or permission can allow copying."),
            C("It protects the creator's control over copying and sharing of the work", correct=True),
        ], steps=[S("Recall", text="Copyright gives the creator control over how the work is copied, shared, sold or changed.")],
           concept="What copyright protects", skill="Concept", hint="Think of what the creator can control.",
           feedback="Copyright is the creator's control over the work."),
    ]))

# ------------------------------------------------------------------ 2 Licences
SETS.append(practice_set(
    module=MODULE, topic=IP,
    title="Open-source licences: GPL, MIT and CC", lesson="ip-open-source-licences-gpl-mit-cc",
    questions=[
        MC("What is a software licence?", [
            C("The program itself", why="The licence is the agreement about use, not the program."),
            C("A legal agreement that says how a program may be used, copied, changed and shared", correct=True),
            C("A password for the program", why="A licence is not a password, though some programs ask for a key."),
            C("A guarantee that the program has no errors", why="A licence says nothing about errors."),
        ], steps=[S("Recall", text="A licence states what you may and may not do with a program.")],
           concept="Software licence", skill="Recall", hint="Think of a permission document.",
           feedback="A licence sets out your permissions."),
        MC("Which statement describes open-source software?", [
            C("Its source code is secret", why="That describes proprietary software."),
            C("Its source code is published and may be studied, changed and shared under the licence", correct=True),
            C("It must always be free of cost", why="Open source is about code access. Some people charge for support or copies."),
            C("It has no licence", why="Open source software has a licence."),
        ], steps=[S("Recall", text="Open source means the code is available under a licence that allows study, change and sharing.")],
           concept="Open source", skill="Recall", hint="What is open about open source?",
           feedback="The code is open."),
        MC("Which is the difference between freeware and open-source software?", [
            C("Freeware is free to use but its code is closed, while open source publishes its code", correct=True),
            C("Freeware always has its code open", why="Freeware keeps the code closed."),
            C("Open source always costs money", why="Many open-source programs are free of cost."),
            C("There is no difference", why="Free of cost and open code are different ideas."),
        ], steps=[S("Compare", text="Freeware: free to use, code closed. Open source: code published.")],
           concept="Freeware versus open source", skill="Concept", hint="One is about price, the other about code.",
           feedback="Free of cost is not the same as open source."),
        MC("A licence says: if you share a changed version, you must share its source code under the same licence. This is called", [
            C("Permissive licensing", why="A permissive licence does not force changed code to stay open."),
            C("Shareware", why="Shareware is a try-before-you-buy model."),
            C("Copyleft, as in the GPL", correct=True),
            C("Freeware", why="Freeware is about no cost, not the rule on shared changes."),
        ], steps=[S("Recall", text="The GPL uses copyleft to keep shared changes open.")],
           concept="Copyleft and the GPL", skill="Concept", hint="Which licence keeps changes open?",
           feedback="That is copyleft."),
        MC("Which licence allows code to be used inside a closed, paid product as long as the copyright notice is kept?", [
            C("GPL", why="The GPL requires shared changed versions to stay open."),
            C("CC BY-ND", why="CC is mostly for content, and ND forbids changes."),
            C("Proprietary licence", why="A proprietary licence does not give such freedom."),
            C("MIT licence", correct=True),
        ], steps=[S("Recall", text="MIT is permissive: only the copyright notice must be kept.")],
           concept="MIT licence", skill="Concept", hint="Which licence is the most permissive?",
           feedback="MIT is permissive."),
        MC("A poster is licensed CC BY-SA. A student wants to edit it and share his new version. What must he do?", [
            C("Credit the creator and share his version under the same licence", correct=True),
            C("Nothing, because editing is always free", why="BY and SA add conditions."),
            C("Remove the creator's name", why="BY requires credit."),
            C("Sell it without any conditions", why="SA requires the same licence on the new work."),
        ], steps=[S("Read the elements", text="BY: credit. SA: share the new work under the same licence.")],
           concept="Creative Commons elements", skill="Application", hint="What do BY and SA ask?",
           feedback="BY plus SA."),
        MC("A student wants to print a CC BY-NC photo on a T-shirt to sell for 3 000 FCFA. What is the correct decision?", [
            C("Allowed, because he credits the photographer", why="NC forbids commercial use even with credit."),
            C("Allowed, because the price is small", why="Any commercial use is excluded."),
            C("Not allowed without permission, because NC means non-commercial", correct=True),
            C("Allowed if he changes the colours", why="Editing does not remove the NC condition."),
        ], steps=[S("Read NC", text="NC allows only non-commercial use."),
                  S("Check the use", text="Selling T-shirts is commercial.")],
           concept="NonCommercial", skill="Application", hint="Is selling a commercial use?",
           feedback="NC blocks sales."),
        MC("Three students want their app to be free to improve and want every shared version to stay open. Which licence do they choose?", [
            C("MIT licence", why="MIT allows closed versions."),
            C("A proprietary licence", why="It would stop others from improving the code."),
            C("CC0", why="CC0 gives up rights, so closed versions are allowed."),
            C("GPL", correct=True),
        ], steps=[S("Match need to licence", text="Copyleft keeps shared versions open, and that is the GPL.")],
           concept="Choosing a licence", skill="Reasoning", hint="Which licence uses copyleft?",
           feedback="GPL fits."),
    ]))

# ------------------------------------------------------------------ 3 Cybercrime law
SETS.append(practice_set(
    module=MODULE, topic=LAW,
    title="Cybercrime law and computer misuse", lesson="law-cybercrime-and-cybersecurity-cameroon",
    questions=[
        MC("What is cybercrime?", [
            C("Any illegal act done using a computer, phone or network, or aimed at them", correct=True),
            C("Any use of a computer at night", why="Time of use does not make an act a crime."),
            C("Only the theft of a physical computer", why="Cybercrime is mainly about acts using or aimed at systems and data."),
            C("Only spreading viruses", why="That is one kind. Fraud, hacking and identity theft are also cybercrimes."),
        ], steps=[S("Recall the definition", text="Illegal acts using or aimed at computers, phones and networks.")],
           concept="Cybercrime definition", skill="Recall", hint="Think of crime plus computers and networks.",
           feedback="Correct."),
        MC("Which Cameroonian law of 21 December 2010 relates to cybersecurity and cybercrime?", [
            C("Law No. 2010/013", why="That law governs electronic communications."),
            C("Law No. 2010/012", correct=True),
            C("The OHADA Uniform Act", why="OHADA acts deal with business law."),
            C("The Bangui Agreement", why="That set up OAPI and concerns intellectual property."),
        ], steps=[S("Recall", text="Law No. 2010/012 relates to cybersecurity and cybercrime.")],
           concept="Law No. 2010/012", skill="Recall", hint="The cybersecurity law ends in 012.",
           feedback="012 is cybersecurity and cybercrime."),
        MC("What does Law No. 2010/013 of 21 December 2010 govern?", [
            C("Copyright in music", why="Not the topic of this law."),
            C("School examinations", why="Not the topic of this law."),
            C("Electronic communications in Cameroon", correct=True),
            C("Road traffic", why="Not the topic of this law."),
        ], steps=[S("Recall", text="Law No. 2010/013 governs electronic communications.")],
           concept="Law No. 2010/013", skill="Recall", hint="The two 2010 laws are about different things.",
           feedback="013 is electronic communications."),
        MC("A student guesses a classmate's password and reads her messages without asking. This is", [
            C("Phishing", why="Phishing tricks a person into giving a secret. Here the student guessed."),
            C("Harmless, because nothing was changed", why="Entering without permission is an offence even if nothing is changed."),
            C("Malware", why="No harmful program was used."),
            C("Unauthorised access to an account", correct=True),
        ], steps=[S("Look for permission", text="She did not allow access."),
                  S("Name it", text="This is unauthorised access (hacking).")],
           concept="Unauthorised access", skill="Application", hint="Did the owner give permission?",
           feedback="Looking without permission is still unauthorised."),
        MC("An SMS says: 'You won 500 000 FCFA. Send 10 000 FCFA by mobile money to get your prize.' What is it?", [
            C("A genuine prize", why="Real prizes do not ask you to pay first."),
            C("A scam of the phishing type", correct=True),
            C("A lawful bank notice", why="Banks do not ask for payment to release a prize by SMS."),
            C("A firewall alert", why="It is not a security alert."),
        ], steps=[S("Spot the sign", text="It asks you to pay before you receive anything."),
                  S("Name it", text="It is a scam of the phishing type.")],
           concept="Scams and phishing", skill="Application", hint="Real prizes do not charge first.",
           feedback="Never pay to win."),
        MC("A caller says he works for a mobile money company and asks for your PIN. What should you do?", [
            C("Give the PIN to fix the problem", why="Giving a PIN allows theft."),
            C("Give half the PIN", why="Even part of a PIN helps a thief."),
            C("End the call and tell the real company through its official line", correct=True),
            C("Tell him your password instead", why="Never give any secret."),
        ], steps=[S("Protect secrets", text="Never give a PIN to anyone."),
                  S("Report", text="Use the official line to report.")],
           concept="Safe behaviour", skill="Application", hint="Who should ever know your PIN?",
           feedback="Keep the PIN private."),
        MC("A student changes his marks in the school results system after guessing the password. Which offences are involved?", [
            C("Only plagiarism", why="Plagiarism is about copying work, not altering records."),
            C("Only software piracy", why="No software was copied."),
            C("None, because they are his own marks", why="Records belong to the school and he had no permission."),
            C("Unauthorised access and unauthorised alteration of data", correct=True),
        ], steps=[S("List the acts", text="He entered the system without permission and changed data."),
                  S("Name the offences", text="Unauthorised access and alteration of data.")],
           concept="Computer misuse", skill="Reasoning", hint="Count what he did: entered, then changed.",
           feedback="Two acts, two offences."),
        MC("Which is the best advice for a student to stay lawful online?", [
            C("Use only accounts and computers you are allowed to use", correct=True),
            C("Try other people's passwords to test them", why="Testing without permission is an offence."),
            C("Share suspicious links so friends can check them", why="This may spread malware."),
            C("Pretend to be someone else for a joke", why="Pretending to be another person can be identity misuse."),
        ], steps=[S("Choose the lawful option", text="Permission is the key idea.")],
           concept="Student do and do not", skill="Application", hint="Which option relies on permission?",
           feedback="Only use what you are allowed to use."),
    ]))

# ------------------------------------------------------------------ 4 Data privacy and bodies
SETS.append(practice_set(
    module=MODULE, topic=LAW,
    title="Data privacy, ANTIC and MINPOSTEL", lesson="law-data-privacy-antic-minpostel",
    questions=[
        MC("Which of these is personal data?", [
            C("The colour of the school building", why="This does not identify a person."),
            C("A student's name, photo and phone number", correct=True),
            C("The price of bread", why="This does not identify a person."),
            C("The weather forecast", why="This does not identify a person."),
        ], steps=[S("Test", text="Personal data identifies a person.")],
           concept="Personal data", skill="Recall", hint="Which item points to a real person?",
           feedback="Names, photos and phone numbers identify people."),
        MC("What is data privacy?", [
            C("A person's right to control how their personal data is collected, used and shared", correct=True),
            C("Keeping all computers locked", why="That is physical security, not the right over personal data."),
            C("Deleting all files every night", why="Privacy is not about deleting everything."),
            C("Using a very fast network", why="Speed has no link to privacy."),
        ], steps=[S("Recall", text="Data privacy is about the person's control over their data.")],
           concept="Data privacy", skill="Recall", hint="Whose control is it?",
           feedback="It is the person's control."),
        MC("MINPOSTEL is", [
            C("The agency in charge of the security of electronic networks", why="That describes ANTIC."),
            C("The telecom regulator", why="That describes ART."),
            C("An international body for patents", why="This is not MINPOSTEL."),
            C("The Ministry of Posts and Telecommunications, which handles government policy on posts, telecommunications and ICT", correct=True),
        ], steps=[S("Recall", text="MINPOSTEL is a ministry. It prepares and carries out government policy.")],
           concept="MINPOSTEL", skill="Recall", hint="Think 'ministry'.",
           feedback="Ministry means policy."),
        MC("ANTIC stands for", [
            C("National Association of Teachers in Cameroon", why="This is not what ANTIC stands for."),
            C("Agency for Network Trade in Cameroon", why="This is not what ANTIC stands for."),
            C("National Agency for Information and Communication Technologies", correct=True),
            C("Association for Telecom Investment", why="This is not what ANTIC stands for."),
        ], steps=[S("Recall", text="ANTIC is the National Agency for Information and Communication Technologies.")],
           concept="ANTIC", skill="Recall", hint="It is an agency for ICT.",
           feedback="ANTIC is the ICT agency."),
        MC("Which statement about personal data rules in Cameroon is the safest to write in an exam?", [
            C("The rules are complete and never change", why="Rules on personal data are still developing."),
            C("Rules on personal data are developing, so current texts should be checked", correct=True),
            C("There is no need to protect personal data", why="Good practice still applies."),
            C("Only banks must protect data", why="Schools, shops and agents also hold personal data."),
        ], steps=[S("Stay safe", text="Do not invent details. State that rules are developing and should be checked.")],
           concept="Developing rules", skill="Reasoning", hint="Avoid claims you cannot support.",
           feedback="Honest and careful."),
        MC("Which password is the best choice?", [
            C("12345", why="Very short and easy to guess."),
            C("The student's own name", why="Names are easy to guess."),
            C("A long phrase with letters, numbers and symbols, used for one account only", correct=True),
            C("The same simple password for all accounts", why="If one account is attacked, all are at risk."),
        ], steps=[S("Compare", text="Longer and different for each account is stronger.")],
           concept="Strong passwords", skill="Application", hint="Think length and uniqueness.",
           feedback="Length and uniqueness help."),
        MC("A student wants to post a class photo with names on a public page. What should she do first?", [
            C("Ask the people in the photo and the teacher, and limit the details", correct=True),
            C("Post at once, because it is a nice photo", why="Consent comes before posting."),
            C("Add everyone's phone numbers", why="Phone numbers are personal data and should not be shared."),
            C("Post it and delete only if someone complains", why="Ask first, not after."),
        ], steps=[S("Ask consent", text="Ask those in the photo."),
                  S("Limit details", text="Leave out names and locations.")],
           concept="Consent and photos", skill="Application", hint="Who should say yes before you post?",
           feedback="Ask first."),
        MC("A shop keeps customer ID numbers in a notebook on the counter. Which is the best fix?", [
            C("Leave it open so customers can check it", why="Others could read and copy the numbers."),
            C("Post the numbers on the wall", why="This exposes the data to everyone."),
            C("Write the numbers in a bigger notebook", why="Size does not protect data."),
            C("Keep only the data needed and store it locked or password-protected", correct=True),
        ], steps=[S("Reduce and protect", text="Collect less, and lock it away.")],
           concept="Protecting data", skill="Application", hint="Who should be able to read it?",
           feedback="Collect less and lock it."),
    ]))

# ------------------------------------------------------------------ 5 Digital divide
SETS.append(practice_set(
    module=MODULE, topic=SOC,
    title="The digital divide and ways to reduce it", lesson="impact-the-digital-divide",
    questions=[
        MC("The digital divide is", [
            C("A fault that splits a screen in two", why="This is about hardware, not social access."),
            C("The gap between people who have good access to ICT and the skills to use it and those who do not", correct=True),
            C("A way to divide numbers on a computer", why="This is a different meaning of divide."),
            C("The gap between two network operators", why="The divide is between groups of people."),
        ], steps=[S("Recall", text="Unequal access to ICT and the skills to use it.")],
           concept="Digital divide definition", skill="Recall", hint="It is a gap between groups of people.",
           feedback="A gap in access and skills."),
        MC("Which is a cause of the digital divide?", [
            C("Fast internet everywhere", why="Fast internet everywhere would reduce the divide."),
            C("Low cost of data", why="Low cost helps access."),
            C("Free computer training for all", why="Training reduces the divide."),
            C("High cost of devices and data bundles", correct=True),
        ], steps=[S("Find the barrier", text="High cost keeps many people offline.")],
           concept="Causes: cost", skill="Concept", hint="Which option makes access harder?",
           feedback="Cost is a major barrier."),
        MC("Why can a lack of electricity widen the digital divide?", [
            C("Electricity makes phones slower", why="Electricity does not slow devices."),
            C("It makes data bundles free", why="It has no such effect."),
            C("Devices cannot be charged or used reliably", correct=True),
            C("It improves network signals", why="It does not improve signals."),
        ], steps=[S("Link cause and effect", text="No power means no charging and no computer use.")],
           concept="Causes: electricity", skill="Reasoning", hint="What does every device need?",
           feedback="Power is basic."),
        MC("Which is the best example of a rural and urban gap?", [
            C("A town school with a computer lab and a village school with none", correct=True),
            C("Two students in the same town with different phone brands", why="This is not a rural and urban gap."),
            C("Two cyber cafes with different prices", why="Price differences alone are not a rural and urban gap."),
            C("A teacher with a laptop", why="One person is not a gap between areas."),
        ], steps=[S("Find the comparison", text="Town versus village access.")],
           concept="Rural and urban gap", skill="Application", hint="Look for two places being compared.",
           feedback="Town and village differ in access."),
        MC("How can mobile money help reduce the divide?", [
            C("It gives every person a free computer", why="It does not give free computers."),
            C("It removes the need for network coverage", why="It still needs a network."),
            C("It makes all scams impossible", why="Scams still exist."),
            C("It lets people send and receive money without a bank branch", correct=True),
        ], steps=[S("Match the benefit", text="Money transfers without a bank branch reach more people.")],
           concept="Mobile money", skill="Application", hint="Think of villages far from banks.",
           feedback="It widens financial access."),
        MC("Which measure best helps students with weak internet?", [
            C("Lessons only available by live video", why="Live video needs a good connection."),
            C("Lessons that can be downloaded and used offline", correct=True),
            C("Banning phones", why="Banning phones does not help access."),
            C("Adding more advertisements", why="Adverts do not help."),
        ], steps=[S("Choose the fit", text="Offline content works without a connection.")],
           concept="Reducing the divide", skill="Application", hint="What works without a signal?",
           feedback="Offline content helps."),
        MC("A village school gets solar panels and ten computers but no trained teacher. What is likely?", [
            C("The divide is fully solved", why="Without skills the equipment may stay unused."),
            C("Computers will teach themselves", why="People need training."),
            C("Power and equipment help, but the lack of skills still limits use", correct=True),
            C("The solar panels will fix the network", why="Panels give power, not network."),
        ], steps=[S("Weigh", text="Power and devices are needed. So are skills.")],
           concept="Skills", skill="Reasoning", hint="List what is present and what is missing.",
           feedback="Skills matter too."),
        MC("Which answer is a balanced statement about phones and the divide?", [
            C("Phones have helped narrow the gap, but cost, coverage and skills still matter", correct=True),
            C("Phones have removed the divide completely", why="Costs, coverage and skills remain."),
            C("Phones make no difference", why="Phones have helped many people."),
            C("Only computers matter", why="Phones are the main device for many people."),
        ], steps=[S("Pick the fair view", text="Phones help but do not remove all barriers.")],
           concept="Balanced view", skill="Reasoning", hint="Avoid always and never.",
           feedback="Balanced answers earn marks."),
    ]))

# ------------------------------------------------------------------ 6 Automation
SETS.append(practice_set(
    module=MODULE, topic=SOC,
    title="Automation and changing jobs", lesson="impact-automation-and-job-change",
    questions=[
        MC("Automation is", [
            C("Writing a program without a keyboard", why="Automation is about tasks done by machines."),
            C("Buying a new computer", why="Buying a computer is not automation by itself."),
            C("Working very fast by hand", why="Automation uses machines."),
            C("Using computers and machines to do tasks with little or no human help", correct=True),
        ], steps=[S("Recall", text="Tasks done by machines with little human help.")],
           concept="Automation", skill="Recall", hint="Who or what does the task?",
           feedback="Machines do the work."),
        MC("Job displacement is", [
            C("Moving to a new office", why="That is a change of place, not job loss."),
            C("Workers losing jobs because a machine or program now does the work", correct=True),
            C("A rise in salary", why="This is not displacement."),
            C("A job that was never advertised", why="This is unrelated."),
        ], steps=[S("Recall", text="Loss of work caused by a machine or program.")],
           concept="Job displacement", skill="Recall", hint="Displace means push out.",
           feedback="Work is taken over."),
        MC("Which job is most likely to be created by automation in banking?", [
            C("Hand-counting cashier", why="Counting is the task being automated."),
            C("Paper form filer", why="Digital systems reduce paper filing."),
            C("App developer", correct=True),
            C("Ledger writer", why="Software replaces ledgers."),
        ], steps=[S("Think", text="Apps need people to build and maintain them.")],
           concept="Jobs created", skill="Application", hint="Who builds the app?",
           feedback="New systems need builders."),
        MC("Which task is most likely to be automated?", [
            C("Counting stock using a barcode scanner and software", correct=True),
            C("Comforting a worried customer", why="This needs human care."),
            C("Planning a new shop layout", why="This needs judgement."),
            C("Negotiating a contract", why="This needs human judgement."),
        ], steps=[S("Pick the routine task", text="Repeated, rule-based tasks are easier to automate.")],
           concept="Routine tasks", skill="Concept", hint="Which is repeated and rule-based?",
           feedback="Routine tasks go first."),
        MC("Why is retraining important when jobs change?", [
            C("It stops all technology", why="Retraining does not stop technology."),
            C("It helps workers learn skills for new or changed work", correct=True),
            C("It guarantees a higher salary", why="It helps but does not guarantee."),
            C("It removes the need for schools", why="Education is still needed."),
        ], steps=[S("Link", text="New tasks need new skills.")],
           concept="Retraining", skill="Concept", hint="What do changed jobs ask of workers?",
           feedback="Skills must change too."),
        MC("A farmer uses a phone to check market prices. What is a benefit?", [
            C("He cannot be cheated ever", why="Scams and bad information still exist."),
            C("He no longer needs to farm", why="He still needs to produce crops."),
            C("The price of crops will always rise", why="Prices depend on the market."),
            C("He can compare prices before selling and save travel", correct=True),
        ], steps=[S("Link", text="Price information helps decisions and saves trips.")],
           concept="Automation in farming", skill="Application", hint="What does the phone give him?",
           feedback="Information helps choice."),
        MC("Which is a concern about automation that should appear in a balanced answer?", [
            C("Automation can reduce routine jobs and some workers may find retraining hard", correct=True),
            C("Automation makes every job better", why="This ignores the problems."),
            C("Automation never needs electricity", why="Automation needs power."),
            C("Automation affects only banks", why="Many sectors are affected."),
        ], steps=[S("Pick the fair concern", text="Job loss and difficulty of retraining.")],
           concept="Balanced view", skill="Reasoning", hint="Look for a real problem.",
           feedback="State real problems."),
        MC("Which conclusion is balanced?", [
            C("Automation only destroys jobs", why="It also creates jobs."),
            C("Automation only creates jobs", why="It also removes some."),
            C("Automation removes some routine jobs and creates others, so retraining and access to training are important", correct=True),
            C("Automation does not affect work", why="It changes many jobs."),
        ], steps=[S("Check both sides", text="A balanced answer names losses, gains and the need for skills.")],
           concept="Balanced conclusion", skill="Reasoning", hint="Does the option mention both sides?",
           feedback="Both sides."),
    ]))

# ------------------------------------------------------------------ 7 E-waste and remote
SETS.append(practice_set(
    module=MODULE, topic=SOC,
    title="E-waste and remote work and learning", lesson="impact-e-waste-and-remote-collaboration",
    questions=[
        MC("E-waste is", [
            C("Waste paper from a school office", why="E-waste is electronic equipment, not paper."),
            C("Food waste from a canteen", why="This is not e-waste."),
            C("Waste water from a laboratory", why="This is not e-waste."),
            C("Thrown-away electrical and electronic equipment such as old phones and batteries", correct=True),
        ], steps=[S("Recall", text="Discarded electronic and electrical equipment.")],
           concept="E-waste", skill="Recall", hint="What kind of items?",
           feedback="Phones, computers, batteries."),
        MC("Why is e-waste hazardous?", [
            C("It is always too heavy to carry", why="Weight is not the main hazard."),
            C("It contains harmful substances such as lead and mercury that can pollute soil and water", correct=True),
            C("It makes noise", why="Noise is not the main hazard."),
            C("It attracts insects only", why="The main hazard is toxic substances."),
        ], steps=[S("Recall", text="Toxic metals harm health and the environment.")],
           concept="E-waste hazards", skill="Concept", hint="Think of what is inside a battery.",
           feedback="Toxic substances."),
        MC("Which is the best first step to reduce e-waste?", [
            C("Throw phones into a fire", why="Burning releases poisonous smoke."),
            C("Bury batteries near a well", why="This can pollute water."),
            C("Repair a faulty phone so it can keep working", correct=True),
            C("Leave old chargers on the roadside", why="This adds to waste."),
        ], steps=[S("Order the steps", text="Repair first, then reuse, then recycle.")],
           concept="Repair, reuse, recycle", skill="Application", hint="Which keeps the device in use?",
           feedback="Repair extends life."),
        MC("Which is an example of reuse?", [
            C("Giving a working old laptop to a school club", correct=True),
            C("Burning a dead laptop", why="This is harmful disposal."),
            C("Throwing it in a river", why="This pollutes."),
            C("Taking it apart and leaving the pieces outside", why="This is unsafe dumping."),
        ], steps=[S("Match", text="Reuse means another person uses the working device.")],
           concept="Reuse", skill="Application", hint="Reuse means someone else keeps using it.",
           feedback="Pass it on."),
        MC("Remote collaboration means", [
            C("Using a remote control for a television", why="This is a different meaning of remote."),
            C("People working or learning together from different places using ICT tools", correct=True),
            C("Working alone with no tools", why="Collaboration involves others and tools."),
            C("Meeting only in person", why="Remote means at a distance."),
        ], steps=[S("Recall", text="Working together at a distance with ICT.")],
           concept="Remote collaboration", skill="Recall", hint="Remote means far.",
           feedback="Together at a distance."),
        MC("Which tool is used for remote collaboration?", [
            C("A printed notice board only", why="A notice board is not remote."),
            C("A pencil", why="A pencil is not an ICT tool."),
            C("A blackboard", why="A blackboard is in one room."),
            C("A shared online document", correct=True),
        ], steps=[S("Pick the ICT tool", text="Shared documents let many people edit at a distance.")],
           concept="Collaboration tools", skill="Recall", hint="Which one works across places?",
           feedback="Shared documents."),
        MC("Which is a benefit of teleworking?", [
            C("Less travel time and cost", correct=True),
            C("Power cuts disappear", why="Power cuts remain a problem at home."),
            C("No need for a connection", why="A connection is still needed."),
            C("No distractions", why="Home has distractions."),
        ], steps=[S("Choose the benefit", text="Not travelling saves time and money.")],
           concept="Benefits of remote work", skill="Concept", hint="What do you not do when you stay home?",
           feedback="Travel savings."),
        MC("A class starts online lessons and many students have poor connections. Which action helps most?", [
            C("Cancel all lessons forever", why="This ignores solutions."),
            C("Require high-quality video for everyone", why="This excludes students with weak connections."),
            C("Share notes in advance and offer audio-only or a recording", correct=True),
            C("Ban questions", why="This does not help the connection."),
        ], steps=[S("Plan for weak connections", text="Light formats work better.")],
           concept="Remote learning problems", skill="Application", hint="Make it lighter.",
           feedback="Plan for the weakest connection."),
    ]))
