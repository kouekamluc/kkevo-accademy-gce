"""Form 5 Computer Science (O Level 0595): practice set and mock exams for the Examination module.

* Paper 1 strategies practice set: 8 questions that follow the Paper 1 lesson.
* Paper 1 mock exam A: 50 multiple-choice questions (KKEVO practice length; the real number of questions
  is set by the GCE Board). Concept = the syllabus topic title, or "Paper 2" for the Paper 2 skills.
* Paper 2 mock exam A: 6 structured questions written as 29 separate parts (KKEVO practice timing).

Draft content: check against the official syllabus and the current GCE Board instructions.
Legal questions use only Law No. 2010/012, Law No. 2010/013 (both dated 21 December 2010), ANTIC and MINPOSTEL.
"""

import random

from .dsl import *  # noqa: F403

COURSE = ("computer-science", "form-5")


def _opts(right, wrongs, pos):
    """Four options with the correct one at index `pos`; `wrongs` is a list of (text, why)."""
    opts = [C(t, why=w) for t, w in wrongs]
    opts.insert(pos, C(right, correct=True))
    return opts


def Q(prompt, right, wrongs, pos, steps, concept, skill, hint):
    return MC(prompt, _opts(right, wrongs, pos), steps=steps, concept=concept, skill=skill, hint=hint)


# ======================================================================================
# Practice set for the lesson "Paper 1: multiple-choice strategies"
# ======================================================================================
LESSON_SET = [
    NUM("A practice paper has 45 multiple-choice questions and lasts 90 minutes. On average, how many minutes can you spend on each question?", 2,
        steps=[S("Divide the time by the number of questions", math=r"90 \div 45 = 2"),
               S("Answer", text="2 minutes per question on average.")],
        concept="Paper 1 time budget", skill="Calculation",
        hint="Divide the total minutes by the number of questions."),
    Q("In the two-pass method, what should you do with a question that is taking much longer than the average time?",
      "Mark it, move on, and return to it after the first pass",
      [("Keep working until it is solved", "This can use the time that easier questions need."),
       ("Leave it blank and never look at it again", "A question you forget can never earn a mark."),
       ("Go back and change the answers to the easy questions", "Changing correct answers without a reason can lose marks.")],
      1, [S("Collect the cheap marks first", text="Easy questions give the same marks as hard ones."),
          S("Return later", text="On the second pass you have the time you saved.")],
      "Paper 1 time budget", "Concept", "Which questions give you marks most cheaply?"),
    Q('In the tag <a href="news.html">News</a>, which word is the name of an attribute?',
      "href",
      [("a", "a is the tag name that comes straight after the angle bracket."),
       ("news.html", "This is the attribute value, written inside quotes."),
       ("News", "This is the content that the visitor reads and clicks.")],
      2, [S("Look for the word before the equals sign", text="An attribute name comes before the equals sign inside the opening tag."),
          S("Answer", text="href is the attribute name. news.html is its value.")],
      "HTML5 structure", "Recall", "The attribute name is followed by an equals sign and a value in quotes."),
    Q("Which law deals with electronic communications networks and services in Cameroon?",
      "Law No. 2010/013",
      [("Law No. 2010/012", "Law No. 2010/012 relates to cybersecurity and cybercrime."),
       ("ANTIC", "ANTIC is the National Agency for Information and Communication Technologies. It is a body, not a law."),
       ("MINPOSTEL", "MINPOSTEL is the Ministry of Posts and Telecommunications. It is a ministry, not a law.")],
      0, [S("Separate laws from bodies", text="Only options with 'Law No.' are laws. ANTIC and MINPOSTEL are public bodies."),
          S("Choose between the two laws", text="Both are dated 21 December 2010. Law No. 2010/013 governs electronic communications; Law No. 2010/012 covers cybersecurity and cybercrime.")],
      "Cameroon legal framework", "Recall", "Two options are institutions, so they cannot be laws."),
    Q("Which of these statements is NOT true?",
      "Anything you find on the internet is free to copy and use",
      [("Copyright applies automatically when an original work is created", "This is true: no registration is needed."),
       ("Freeware can be used free of charge, but its source code is closed", "This is true. Freeware is not the same as open source."),
       ("The GPL requires distributed changes to stay open", "This is true: the GPL is a copyleft licence.")],
      3, [S("Look for the absolute claim", text="'Anything' admits no exception."),
          S("Test it", text="A song or a photo on a website is still protected by copyright unless the owner gives permission, for example with a Creative Commons licence."),
          S("Check the other three", text="Each one matches the definitions you learned, so each is true.")],
      "Intellectual property", "Reasoning", "Which statement has a word that allows no exceptions?"),
    Q("An algorithm starts with x ← 2. Then FOR i ← 1 TO 3 repeats x ← x × 2. The algorithm then outputs x. What is output?",
      "16",
      [("6", "You added 2 + 2 + 2. The line multiplies the current value of x by 2."),
       ("8", "x is multiplied by 2 three times: 4, 8, 16. Stopping at 8 is only two passes."),
       ("12", "This is 2 × 6. The multiplication happens once per pass.")],
      1, [S("Pass 1", math=r"x = 2 \times 2 = 4"),
          S("Pass 2", math=r"x = 4 \times 2 = 8"),
          S("Pass 3", math=r"x = 8 \times 2 = 16")],
      "Paper 2", "Calculation", "Write x after each pass of the loop."),
    Q("X = (NOT A) AND B. For which inputs is X equal to 1?",
      "A = 0 and B = 1",
      [("A = 1 and B = 0", "The values are swapped. NOT 1 is 0, so the AND gate gives 0."),
       ("A = 1 and B = 1", "NOT 1 is 0, so the AND gate gives 0."),
       ("A = 0 and B = 0", "NOT 0 is 1, but B is 0, so the AND gate gives 0.")],
      2, [S("AND needs two 1s", text="Both inputs of the AND gate must be 1."),
          S("Work backwards", text="NOT A must be 1, so A = 0. B must be 1."),
          S("Check", text="A = 0 and B = 1: NOT 0 = 1, and 1 AND 1 = 1.")],
      "Paper 2", "Reasoning", "An AND gate gives 1 only when both its inputs are 1. What must A be to make NOT A equal to 1?"),
    NUM("A box has a content width of 150 px, padding of 10 px on each side and a border of 2 px on each side. What is the width of the box in px, including its padding and border?", 174,
        steps=[S("Add both sides of the padding", math=r"2 \times 10 = 20"),
               S("Add both sides of the border", math=r"2 \times 2 = 4"),
               S("Total", math=r"150 + 20 + 4 = 174")],
        concept="CSS styling", skill="Calculation",
        hint="Padding and border appear on the left and on the right."),
]

# ======================================================================================
# Paper 1 mock exam A: 50 questions, built from raw tuples then ordered and given a spread of correct options
# ======================================================================================
RAW = []


def R(concept, skill, prompt, right, wrongs, steps, hint):
    RAW.append(dict(concept=concept, skill=skill, prompt=prompt, right=right, wrongs=wrongs, steps=steps, hint=hint))


# ---------------------------------------------------------------- HTML5 structure (7)
H5 = "HTML5 structure"
R(H5, "Recall", "Which line must come first in an HTML5 page?", "<!DOCTYPE html>",
  [("<html>", "The html element comes after the doctype declaration."),
   ("<head>", "head is inside the html element and holds information about the page."),
   ("<body>", "body holds the visible content and comes after head.")],
  [S("The doctype tells the browser which kind of document follows", text="It is written before everything else."),
   S("Answer", text="<!DOCTYPE html> comes first, then <html>, <head> and <body>.")],
  "The browser needs to know the document type before it reads any element.")
R(H5, "Concept", "Which example is correctly nested?", "<p>Hello <b>world</b></p>",
  [("<p>Hello <b>world</p></b>", "The b tag was opened last, so it must be closed first. These tags overlap."),
   ("<p>Hello <b>world</b>", "The p element is never closed."),
   ("<b><p>Hello world</b></p>", "The p tag was opened last, so it must be closed first. These tags overlap.")],
  [S("Rule", text="Close tags in the reverse order of opening: last opened, first closed."),
   S("Check the right answer", text="b opens after p and closes before p. Nothing overlaps.")],
  "Last opened, first closed.")
R(H5, "Concept", 'In the link <a href="contact.html">Contact us</a>, what is href?',
  "An attribute that gives the address the link goes to",
  [("The name of the tag", "The tag name is a. href is written inside the opening tag."),
   ("The text the visitor clicks", "The clickable text is Contact us, the content of the element."),
   ("A closing tag", "A closing tag starts with a slash, as in </a>.")],
  [S("Find where href sits", text="It is inside the opening tag, followed by an equals sign and a value."),
   S("Name it", text="That makes it an attribute. Its value, contact.html, is the destination.")],
  "Look at where href is written and what follows it.")
R(H5, "Recall", "Which attribute of an img element gives text that is shown or read aloud when the picture cannot be seen?", "alt",
  [("src", "src gives the location of the picture file."),
   ("href", "href belongs to links (the a element), not to images."),
   ("width", "width sets the size of the picture.")],
  [S("Think of a visitor who cannot see the picture", text="A screen reader reads a text description instead."),
   S("Answer", text="The alt attribute holds that description.")],
  "The word is short for alternative text.")
R(H5, "Recall", "Which tag makes a table header cell?", "<th>",
  [("<tr>", "tr makes a table row."),
   ("<td>", "td makes an ordinary data cell."),
   ("<table>", "table makes the whole table.")],
  [S("Names to remember", text="table is the whole table, tr is a row, td is a data cell, th is a header cell."),
   S("Answer", text="<th>. Browsers show header cells bold and centred by default.")],
  "The tag name is short for table header.")
R(H5, "Application", 'A form needs a box where a visitor types a password so that the characters appear as dots. Which is correct?',
  '<input type="password">',
  [('<input type="text">', "The characters would be shown as they are typed."),
   ('<input type="hidden">', "A hidden field is not shown on the page at all, so nobody could type into it."),
   ('<input type="submit">', "This makes a button that sends the form.")],
  [S("Input types", text="The type attribute decides what kind of control the input is."),
   S("Answer", text="Only type=\"password\" hides what is typed.")],
  "The type attribute names the kind of control.")
R(H5, "Recall", "Which element holds the text that appears in the browser tab as the title of the page?", "<title> inside <head>",
  [("<h1> inside <body>", "h1 is a heading inside the page. It is not the tab title."),
   ("<header> inside <body>", "header is a section at the top of the visible page."),
   ("<body>", "body holds all the visible content of the page.")],
  [S("Head versus body", text="Information about the page goes in head. Visible content goes in body."),
   S("Answer", text="The tab text comes from the title element, which sits inside head.")],
  "Is the tab text information about the page or part of the visible page?")

# ---------------------------------------------------------------- CSS styling (7)
CS = "CSS styling"
R(CS, "Recall", "Which is a correct CSS rule?", "p { color: blue; }",
  [("p { color = blue; }", "CSS uses a colon between the property and the value, not an equals sign."),
   ("p ( color: blue; )", "Declarations go inside curly brackets, not round brackets."),
   ("p color: blue;", "Without curly brackets the browser cannot tell where the declarations begin and end.")],
  [S("Parts of a rule", text="Selector, then curly brackets holding declarations. Each declaration is property, colon, value, semicolon."),
   S("Answer", text="p { color: blue; }")],
  "Look for curly brackets and a colon.")
R(CS, "Recall", 'Which selector chooses the element with id="menu"?', "#menu",
  [(".menu", "A dot selects a class, not an id."),
   ("menu", "With no symbol this selects elements whose tag is menu."),
   ("@menu", "An at sign is not used to select elements.")],
  [S("Remember the symbols", text="Hash for id, dot for class, nothing for a tag name."),
   S("Answer", text="#menu")],
  "One symbol is for ids and a different symbol is for classes.")
R(CS, "Concept", "A school wants one CSS file to style all 40 pages of its website. Which method fits best?",
  "An external stylesheet linked from every page",
  [("An inline style attribute on each tag", "Inline styles affect only one element and would have to be repeated everywhere."),
   ("A style element inside the head of one page", "This internal CSS styles that one page only."),
   ("A script element", "Scripts run programs. They are not the way to style pages.")],
  [S("One file, many pages", text="The link element in each page points to the same .css file."),
   S("Benefit", text="Change the file once and every page changes.")],
  "Which method keeps the CSS in a separate file?")
R(CS, "Recall", "Which is the order of the box model layers from the inside to the outside?", "content, padding, border, margin",
  [("content, margin, border, padding", "Margin is the outermost layer."),
   ("padding, content, border, margin", "The content is the innermost layer."),
   ("content, border, padding, margin", "Padding sits between the content and the border.")],
  [S("Picture a parcel", text="The item is the content, the packing around it is the padding, the box is the border, and the space around the box is the margin."),
   S("Answer", text="content, padding, border, margin.")],
  "Start at the text and move outwards.")
R(CS, "Calculation", "A box has a content width of 200 px, padding of 10 px on each side, a border of 5 px on each side and a margin of 20 px on each side. What is its width including padding and border, but not the margin?",
  "230 px",
  [("200 px", "This is the content alone."),
   ("215 px", "You counted the padding and border on one side only."),
   ("270 px", "You also added the margins, which are outside the box.")],
  [S("Padding on both sides", math=r"2 \times 10 = 20"),
   S("Border on both sides", math=r"2 \times 5 = 10"),
   S("Add to the content", math=r"200 + 20 + 10 = 230 \text{ px}")],
  "Padding and border each appear twice, left and right.")
R(CS, "Recall", "Which CSS property changes the size of the text?", "font-size",
  [("text-size", "There is no such property in CSS."),
   ("font-style", "font-style makes text italic or normal."),
   ("text-align", "text-align sets left, right or centre alignment.")],
  [S("Font properties", text="font-size sets size, font-family sets the typeface, font-style sets italic."),
   S("Answer", text="font-size")],
  "The property name starts with font.")
R(CS, "Application", "Which rule makes all level-1 headings centred and green?", "h1 { text-align: center; color: green; }",
  [("h1 { text-align: centre; color: green; }", "CSS uses the American spelling center, so this value is not recognised."),
   ("h1 { text-align: center, color: green }", "Declarations are separated by semicolons, not commas."),
   ("h1 { align-text: center; color: green; }", "The property is called text-align, not align-text.")],
  [S("Check each part", text="Selector h1. Property text-align with value center. Property color with value green. A semicolon after each declaration."),
   S("Answer", text="h1 { text-align: center; color: green; }")],
  "Check spelling and punctuation in each declaration.")

# ---------------------------------------------------------------- Intellectual property (7)
IP = "Intellectual property"
R(IP, "Concept", "When does copyright protect a new original program?", "Automatically, when the work is created",
  [("Only after the creator pays to register it", "Copyright needs no registration."),
   ("Only after the program has been sold", "Protection does not wait for a sale."),
   ("Only after a patent has been granted", "A patent protects an invention and is a different kind of right.")],
  [S("Key fact", text="Copyright applies as soon as an original work is created."),
   S("Answer", text="No registration, payment or sale is needed.")],
  "Does the creator have to do anything before copyright exists?")
R(IP, "Application", "A cyber cafe in Buea buys one licence for a proprietary office suite and installs it on all 10 of its computers. This is an example of:",
  "software piracy",
  [("open-source sharing", "Open source needs a licence that allows sharing. This is a proprietary program."),
   ("a legal site licence", "A site licence would have to be bought. Here only one licence was bought."),
   ("freeware use", "Freeware is free of charge; this program was paid for.")],
  [S("Compare copies and licences", text="Ten copies in use, one licence bought."),
   S("Name it", text="Using more copies than the licence allows is software piracy.")],
  "How many copies are used and how many licences were bought?")
R(IP, "Recall", "Which description fits freeware?", "Free to use, but the source code is closed",
  [("The source code is published and may be changed and shared", "This describes open-source software."),
   ("A free trial for a short time, then you must pay", "This describes shareware."),
   ("Paid for, with secret source code", "This describes proprietary software.")],
  [S("Compare four kinds", text="Proprietary: paid, closed. Freeware: free, closed. Shareware: trial then pay. Open source: code published."),
   S("Answer", text="Freeware costs nothing to use, but you cannot study or change its code.")],
  "Freeware and open source both cost nothing, but they differ in what you can do with the code.")
R(IP, "Recall", "Which licence says that a distributed modified version must be released under the same open licence?", "GPL",
  [("MIT licence", "The MIT licence is permissive: a modified version may be closed."),
   ("Proprietary licence", "A proprietary licence does not give you the source code to modify."),
   ("Shareware licence", "Shareware is try-before-you-buy with closed code.")],
  [S("Name the idea", text="This rule is called copyleft."),
   S("Answer", text="The GNU General Public Licence (GPL) uses copyleft.")],
  "The idea is called copyleft.")
R(IP, "Recall", "In a Creative Commons licence, what does NC stand for?", "Non-commercial: the work may not be used to make money",
  [("No copying at all", "Creative Commons licences exist to allow sharing, with conditions."),
   ("No credit is needed", "Crediting the author is the BY condition."),
   ("No changes are allowed", "That is ND, no derivatives.")],
  [S("Letters to remember", text="BY credit the author. SA share alike. NC non-commercial. ND no derivatives."),
   S("Answer", text="NC means non-commercial use only.")],
  "Think of the word commercial.")
R(IP, "Concept", "What does copyright protect?", "The actual code, text, music or image that was created",
  [("The idea behind a program", "Copyright protects the expression of an idea, not the idea itself."),
   ("A brand name or logo", "Brand names and logos are protected as trademarks."),
   ("A new machine or process", "Inventions are protected by patents.")],
  [S("Three kinds of intellectual property", text="Copyright protects expression. A patent protects an invention. A trademark protects a brand."),
   S("Answer", text="Copyright covers the work itself.")],
  "Which kind of intellectual property fits code, text, music and pictures?")
R(IP, "Application", "A student sells a school magazine for 500 FCFA. It contains a photo licensed CC BY-NC, and the photographer is credited. Has the licence been respected?",
  "No, because selling the magazine is commercial use",
  [("Yes, because the photographer was credited", "Credit satisfies the BY condition, but NC is a second condition."),
   ("Yes, because the magazine is for a school", "The licence says non-commercial. Charging 500 FCFA is commercial."),
   ("No, because Creative Commons photos can never be used", "Creative Commons photos can be used, if the conditions are respected.")],
  [S("List the conditions", text="BY: credit the author. NC: no commercial use."),
   S("Test the use", text="The credit is given, but the magazine is sold, so NC is broken."),
   S("Answer", text="Ask permission or choose an image whose licence allows commercial use.")],
  "A licence can have more than one condition. Check both.")

# ---------------------------------------------------------------- Cameroon legal framework (7)
LG = "Cameroon legal framework"
R(LG, "Recall", "Law No. 2010/012 relates to:", "cybersecurity and cybercrime",
  [("electronic communications networks and services", "That is Law No. 2010/013."),
   ("business law, handled by the OHADA Uniform Acts", "Business law is dealt with by other texts."),
   ("registering patents and trademarks through OAPI", "OAPI and the Bangui Agreement deal with intellectual property.")],
  [S("Match law and subject", text="2010/012: cybersecurity and cybercrime. 2010/013: electronic communications."),
   S("Answer", text="Cybersecurity and cybercrime.")],
  "Both 2010 laws were passed on the same day. Which number goes with cybercrime?")
R(LG, "Recall", "Which law governs electronic communications in Cameroon?", "Law No. 2010/013",
  [("Law No. 2010/012", "Law No. 2010/012 relates to cybersecurity and cybercrime."),
   ("ANTIC", "ANTIC is the National Agency for Information and Communication Technologies. It is a body, not a law."),
   ("MINPOSTEL", "MINPOSTEL is the Ministry of Posts and Telecommunications. It is a ministry, not a law.")],
  [S("Recall", text="Law No. 2010/013 governs how electronic communications networks and services are organised and regulated.")],
  "The two laws have consecutive numbers.")
R(LG, "Recall", "Law No. 2010/012 and Law No. 2010/013 are both dated:", "21 December 2010",
  [("21 December 2012", "The number 2010 in the name shows the year."),
   ("12 October 2010", "The 12 in 2010/012 is the law number, not the day."),
   ("13 January 2011", "The 13 in 2010/013 is the law number, not the day, and the year is 2010.")],
  [S("Read the name", text="The year 2010 appears in the names of both laws."),
   S("Answer", text="Both are dated 21 December 2010.")],
  "The law number and the date are different things.")
R(LG, "Recall", "Which body prepares and carries out government policy on posts, telecommunications and ICT?", "MINPOSTEL",
  [("ANTIC", "ANTIC is an agency that promotes and regulates ICT activities and is in charge of network security."),
   ("OAPI", "OAPI is the African Intellectual Property Organization."),
   ("ART", "ART is the Telecommunications Regulatory Board.")],
  [S("A ministry makes policy", text="MINPOSTEL stands for the Ministry of Posts and Telecommunications."),
   S("Answer", text="MINPOSTEL.")],
  "Which name is a ministry?")
R(LG, "Recall", "Which body is in charge of the security of electronic communication networks and information systems and promotes and regulates ICT activities?", "ANTIC",
  [("MINPOSTEL", "MINPOSTEL is the ministry that prepares and carries out government policy."),
   ("OAPI", "OAPI is the African Intellectual Property Organization."),
   ("ART", "ART is the Telecommunications Regulatory Board.")],
  [S("An agency does the work", text="ANTIC is the National Agency for Information and Communication Technologies."),
   S("Answer", text="ANTIC.")],
  "The A in the abbreviation stands for agency.")
R(LG, "Application", 'A trader receives an SMS: "You have won 500 000 FCFA. Send 10 000 FCFA by mobile money to claim your prize." What type of cybercrime is this?',
  "A phishing scam",
  [("Hacking", "Hacking means entering a computer or account without permission."),
   ("Spreading malware", "Malware is a harmful program. This message contains no program."),
   ("Cyberbullying", "Cyberbullying means harassing a person online.")],
  [S("Spot the trick", text="A fake prize is used to make the victim send money."),
   S("Name it", text="Fake messages that trick people into giving money or details are phishing and scams.")],
  "What does the message want the trader to do?")
R(LG, "Application", "Which is good practice for a school that keeps its students' personal data?",
  "Collect only the data it needs and store it securely",
  [("Share the list with anyone who asks", "Data should not be shared without consent or a legal reason."),
   ("Keep it on an unprotected USB key forever", "Data must be stored securely, and not kept longer than needed."),
   ("Pin it on the notice board so parents can check", "This exposes personal details to everyone.")],
  [S("Principles", text="Collect only what is needed, use it for the stated purpose, store it securely, and do not share it without consent or a legal reason."),
   S("Answer", text="Collect only what is needed and store it securely. Rules on personal data are developing, so check the current texts.")],
  "Which option protects the data?")

# ---------------------------------------------------------------- Social and economic impact (7)
SE = "Social and economic impact"
R(SE, "Recall", "What is the digital divide?", "The gap between people who have good access to computers, the internet and the skills to use them, and people who do not",
  [("The price difference between a phone and a laptop", "The digital divide is about access and skills, not one price."),
   ("A fault line in a computer network", "It is a social gap, not a technical fault."),
   ("The space between two files on a disk", "It has nothing to do with disk storage.")],
  [S("Definition", text="The digital divide is a gap in access to ICT and the skills to use it."),
   S("Answer", text="It can be between regions, between rich and poor, or between generations.")],
  "It describes a gap between groups of people.")
R(SE, "Concept", "Which is a cause of the digital divide in rural areas?", "Weak electricity supply and poor network coverage",
  [("Cheap data bundles", "Cheap data would help to close the gap."),
   ("ICT training in every school", "Training reduces the gap."),
   ("A solar-powered computer centre", "This is a solution, not a cause.")],
  [S("Causes", text="Infrastructure, cost, skills, and lack of content in local languages."),
   S("Answer", text="Weak electricity and network coverage are infrastructure causes.")],
  "Which option makes access harder rather than easier?")
R(SE, "Application", "Which action would best help students in a village school without mains electricity to use computers?", "Install solar panels and set up a school computer lab",
  [("Ban phones in the village", "This removes access and does nothing to close the gap."),
   ("Close the school library", "This reduces access further."),
   ("Make data bundles more expensive", "Higher costs widen the gap.")],
  [S("Find the missing resource", text="No electricity and no computers."),
   S("Answer", text="Solar power plus a computer lab supplies both.")],
  "Which option adds a resource the school lacks?")
R(SE, "Concept", "Which job is most likely to be reduced by automation?", "A clerk who files paper records by hand",
  [("A network technician", "Technicians are needed to install and repair automated systems."),
   ("A web designer", "Web design is a job that automation and ICT have created."),
   ("A mobile money agent", "Mobile money agents are an example of jobs created by ICT.")],
  [S("Routine work is automated first", text="Typists, filing clerks and some cashiers are examples."),
   S("Answer", text="The filing clerk.")],
  "Automation replaces routine, repeated tasks.")
R(SE, "Concept", "Why is it dangerous to burn old computers and batteries?", "They release poisonous substances such as lead and mercury",
  [("The smoke makes the internet slower", "Smoke has no effect on the internet."),
   ("It uses too much electricity", "Burning does not use mains electricity."),
   ("Plastic cannot burn", "Plastic can burn, and the fumes are harmful.")],
  [S("What is inside", text="E-waste contains harmful substances such as lead, mercury and cadmium."),
   S("Answer", text="Burning or dumping them poisons soil, water and air.")],
  "Think about what e-waste contains.")
R(SE, "Application", "Which is the best way to deal with a working old phone?", "Repair, reuse or donate it",
  [("Burn it", "Burning releases poisonous substances."),
   ("Throw it into a river", "Dumping poisons water and harms health."),
   ("Bury it in the garden", "Buried e-waste can leak harmful substances into the soil.")],
  [S("Order of good practice", text="Repair and reuse first, donate working devices, and take dead ones to a collection or recycling point."),
   S("Answer", text="Repair, reuse or donate.")],
  "Which option keeps the device in use?")
R(SE, "Reasoning", "A company in Douala lets its accountants work from home. Which is a disadvantage of teleworking in a town with frequent power cuts?",
  "Work can stop when the power or the internet fails",
  [("Less time spent in traffic", "This is an advantage."),
   ("More flexible working hours", "This is an advantage."),
   ("Colleagues can work together from different places", "This is an advantage of remote collaboration.")],
  [S("Sort advantages and disadvantages", text="Three options describe benefits. One describes a problem."),
   S("Answer", text="Power cuts and weak internet can stop remote work.")],
  "Which option describes a problem rather than a benefit?")

# ---------------------------------------------------------------- Paper 2 skills (15): logic gates (5)
P2 = "Paper 2"
R(P2, "Recall", "Which logic gate gives output 0 only when both of its inputs are 1?", "NAND",
  [("AND", "An AND gate gives 1 when both inputs are 1."),
   ("NOR", "A NOR gate gives 1 only when both inputs are 0."),
   ("OR", "An OR gate gives 0 only when both inputs are 0.")],
  [S("Write the truth tables", text="AND: 0 0 0 1. NAND is the opposite: 1 1 1 0."),
   S("Answer", text="NAND, which means NOT AND.")],
  "It is the opposite of one of the basic gates.")
R(P2, "Reasoning", "X = NOT (A OR B). Which inputs make X equal to 1?", "A = 0 and B = 0",
  [("A = 1 and B = 0", "A OR B is 1, so NOT makes X equal to 0."),
   ("A = 0 and B = 1", "A OR B is 1, so NOT makes X equal to 0."),
   ("A = 1 and B = 1", "A OR B is 1, so NOT makes X equal to 0.")],
  [S("X is 1 only if A OR B is 0", text="NOT turns 0 into 1."),
   S("When is an OR gate 0?", text="Only when both inputs are 0."),
   S("Answer", text="A = 0 and B = 0.")],
  "For X to be 1, what must the output of the OR gate be?")
R(P2, "Application", "A circuit sends inputs A and B into an AND gate, and sends the output of that gate into a NOT gate. The final output is Q. Which expression describes Q?",
  "Q = NOT (A AND B)",
  [("Q = (NOT A) AND (NOT B)", "This applies NOT to each input first. It is a NOR gate."),
   ("Q = (NOT A) AND B", "NOT is applied to the output of the AND gate, not to input A."),
   ("Q = A AND B", "This leaves out the NOT gate.")],
  [S("Follow the wires", text="First gate: A AND B. Second gate: NOT of that result."),
   S("Answer", text="Q = NOT (A AND B), a NAND gate.")],
  "Write the gates in the order the signal passes through them.")
R(P2, "Concept", "A truth table has three inputs, A, B and C. How many rows does it need to show every combination?", "8",
  [("6", "You multiplied 3 by 2. Each extra input doubles the number of rows."),
   ("9", "You squared 3. The number of rows is 2 to the power 3."),
   ("3", "This is the number of inputs, not the number of combinations.")],
  [S("Each input has two values", text="So each input doubles the number of rows."),
   S("Calculate", math=r"2 \times 2 \times 2 = 2^3 = 8")],
  "Each input can be 0 or 1.")
R(P2, "Calculation", "Q = A AND (B OR C). For how many of the 8 possible input combinations is Q equal to 1?", "3",
  [("4", "That would also count A = 1, B = 0, C = 0, where B OR C is 0."),
   ("2", "You missed one of the three combinations where B OR C is 1."),
   ("5", "Q is 0 whenever A is 0, which removes half of the rows.")],
  [S("A must be 1", text="That leaves the 4 rows with A = 1."),
   S("B OR C must be 1", text="Among the four combinations of B and C, only 00 fails."),
   S("Count", text="A = 1 with BC = 01, 10 or 11: 3 rows.")],
  "Q is 0 whenever A is 0. Then count the rows with A = 1.")
# ---------------------------------------------------------------- pseudo-code and trace tables (5)
R(P2, "Calculation", "The algorithm runs x ← 3, then y ← 4, then x ← x + y, then y ← x − y. What are the final values of x and y?",
  "x = 7 and y = 3",
  [("x = 7 and y = 4", "The last line changes y: 7 − 4 = 3."),
   ("x = 7 and y = 11", "The last line subtracts. It does not add."),
   ("x = 3 and y = 4", "These are the starting values. The last two lines change them.")],
  [S("After x ← x + y", math=r"x = 3 + 4 = 7, \quad y = 4"),
   S("After y ← x − y", math=r"y = 7 - 4 = 3"),
   S("Final values", text="x = 7 and y = 3.")],
  "Write the values of x and y after each line, using the newest value of x in the last line.")
R(P2, "Calculation", "total starts at 0. FOR i ← 1 TO 6, IF i MOD 2 = 0 THEN total ← total + i. (MOD gives the remainder after division.) What is total at the end?",
  "12",
  [("9", "You added the odd numbers 1 + 3 + 5. The condition is for even values of i."),
   ("21", "You added every value of i. The IF statement filters them."),
   ("6", "You kept only the last even number. The total accumulates 2 + 4 + 6.")],
  [S("When is the condition true?", text="i MOD 2 = 0 for the even values 2, 4 and 6."),
   S("Add them", math=r"0 + 2 + 4 + 6 = 12")],
  "Which values of i leave remainder 0 when divided by 2?")
R(P2, "Calculation", "n starts at 20 and count starts at 0. WHILE n > 3: n ← n DIV 2 and count ← count + 1. (DIV is whole-number division.) What is count when the loop ends?",
  "3",
  [("2", "At that point n is 5, which is still greater than 3, so the loop runs again. (2 is the final value of n.)"),
   ("4", "After pass 3, n is 2, which is not greater than 3, so there is no fourth pass."),
   ("10", "10 is the value of n after the first pass, not count.")],
  [S("Pass 1", text="n = 20 is greater than 3. n becomes 10 and count becomes 1."),
   S("Pass 2", text="n = 10 is greater than 3. n becomes 5 and count becomes 2."),
   S("Pass 3", text="n = 5 is greater than 3. n becomes 2 and count becomes 3."),
   S("Stop", text="n = 2 is not greater than 3. The loop ends with count 3.")],
  "Write n and count after each pass, and test the condition before each pass.")
R(P2, "Recall", "What is a trace table used for?", "Recording the value of each variable as every line of an algorithm is carried out",
  [("Drawing a logic circuit", "Circuits are drawn with gate symbols."),
   ("Designing the fields of a database", "A table of values in a trace is not a database table."),
   ("Storing passwords safely", "A trace table is not a security tool.")],
  [S("Idea", text="Each column is a variable and each row is a step of the algorithm."),
   S("Use", text="It lets you check the output and find errors without a computer.")],
  "It follows the algorithm line by line.")
R(P2, "Application", 'mark ← 50. The algorithm runs IF mark > 50 THEN OUTPUT "Pass" ELSE OUTPUT "Fail". What is output?', "Fail",
  [("Pass", "50 is not greater than 50. A pass would need mark of 51 or more, or the symbol greater than or equal to."),
   ("Pass and Fail", "Only one branch of an IF statement runs."),
   ("Nothing is output", "There is an ELSE branch, so one of the two outputs always happens.")],
  [S("Test the condition", text="Is 50 greater than 50? No."),
   S("Take the ELSE branch", text='So the algorithm outputs "Fail".')],
  "Test the condition with the exact value, and watch the boundary.")
# ---------------------------------------------------------------- database design (5)
R(P2, "Application", "A table STUDENT has the fields StudentID, Name, Class and Phone. Which field is the best primary key?", "StudentID",
  [("Name", "Two students can have the same name."),
   ("Class", "Many students share the same class."),
   ("Phone", "A phone number can be shared by a family or can change.")],
  [S("A primary key must be unique", text="Every record needs a different value."),
   S("Answer", text="StudentID is given once to each student, so it is unique.")],
  "Which field is different for every record?")
R(P2, "Concept", "STUDENT(StudentID, Name, ClassID) and CLASS(ClassID, ClassName) are linked. ClassID is the primary key of CLASS. Which field is the foreign key?",
  "ClassID in the STUDENT table",
  [("StudentID in the STUDENT table", "StudentID is the primary key of STUDENT."),
   ("ClassName in the CLASS table", "ClassName is an ordinary field."),
   ("Name in the STUDENT table", "Name is an ordinary field.")],
  [S("What is a foreign key?", text="A field in one table that holds the primary key value of another table."),
   S("Answer", text="ClassID in STUDENT points to a row of CLASS.")],
  "Which field in STUDENT refers to the primary key of CLASS?")
R(P2, "Concept", "One class contains many students, and each student belongs to exactly one class. What type of relationship is this between CLASS and STUDENT?", "One-to-many",
  [("One-to-one", "In a one-to-one relationship each class would have exactly one student."),
   ("Many-to-many", "Here each student belongs to only one class."),
   ("No relationship", "The tables are linked through the class of each student.")],
  [S("From the class side", text="One class has many students."),
   S("From the student side", text="One student has one class."),
   S("Answer", text="One-to-many.")],
  "Count how many students one class can have.")
R(P2, "Application", "Students study many subjects, and each subject is studied by many students. How should this many-to-many relationship be stored in a database?",
  "In a linking table with StudentID and SubjectID",
  [("Put all of a student's subjects in one field, separated by commas", "A field should hold one value. Lists in one field are hard to search and update."),
   ("Repeat the student's details in a new row for every subject, with no keys", "This repeats data and has no way to identify records."),
   ("Use one table with no keys", "Without keys the records cannot be linked or identified.")],
  [S("Idea", text="A many-to-many relationship is split into two one-to-many relationships."),
   S("Answer", text="A third table, for example ENROLMENT(StudentID, SubjectID), joins STUDENT and SUBJECT.")],
  "A third table is needed.")
R(P2, "Concept", "Which data type is best for a phone number field, for example +237 6xx xx xx xx?", "Text",
  [("Number (integer)", "Phone numbers are not used in calculations, and an integer would lose a leading zero or a plus sign."),
   ("Date", "A phone number is not a date."),
   ("Currency", "A phone number is not an amount of money.")],
  [S("Ask whether you will calculate with it", text="You will never add or average phone numbers."),
   S("Answer", text="Store it as text so that signs and leading zeros are kept.")],
  "Will you do arithmetic on a phone number?")

assert len(RAW) == 50

# Mixed order (fixed seed, no two neighbours from the same topic) and an even spread of the correct option.
_rnd = random.Random(2026)
for _ in range(10000):
    ORDER = list(range(50))
    _rnd.shuffle(ORDER)
    if all(RAW[ORDER[i]]["concept"] != RAW[ORDER[i + 1]]["concept"] for i in range(49)):
        break
POS = [0] * 13 + [1] * 13 + [2] * 12 + [3] * 12
for _ in range(10000):
    _rnd.shuffle(POS)
    if all(not (POS[i] == POS[i + 1] == POS[i + 2]) for i in range(48)):
        break

P1_QUESTIONS = [
    Q(RAW[k]["prompt"], RAW[k]["right"], RAW[k]["wrongs"], POS[i], RAW[k]["steps"], RAW[k]["concept"], RAW[k]["skill"], RAW[k]["hint"])
    for i, k in enumerate(ORDER)
]

# ======================================================================================
# Paper 2 mock exam A: 6 structured questions, 29 parts, each part standing alone
# ======================================================================================
Q1 = ("In a logic circuit, inputs A and B go into an AND gate. Input C goes into a NOT gate. The outputs of the AND gate and the NOT gate "
      "go into an OR gate, and the output of the OR gate is X. ")
Q2 = ("A school store-room alarm has three inputs. D is 1 when the door is open. K is 1 when a valid key card has been used. N is 1 when it is night. "
      "The alarm output S is 1 when the door is open AND it is night AND no valid key card has been used. ")
Q3 = ("Marks for five students are read one at a time: 12, 7, 16, 9, 20. The algorithm is: "
      "(1) total ← 0. (2) count ← 0. (3) FOR i ← 1 TO 5. (4) READ mark. (5) IF mark >= 10 THEN. (6) total ← total + mark. "
      "(7) count ← count + 1. (8) ENDIF. (9) NEXT i. (10) average ← total / count. (11) OUTPUT average. ")
Q4 = ("An algorithm is: n ← 6, steps ← 0. WHILE n > 1: IF n MOD 2 = 0 THEN n ← n DIV 2 ELSE n ← 3 × n + 1, then steps ← steps + 1. "
      "After the loop, OUTPUT steps. (MOD gives the remainder after division. DIV is whole-number division.) ")
Q5 = ("A library in Bamenda stores its data in three tables. MEMBER(MemberID, Name, Phone). BOOK(BookID, Title, Author). "
      "LOAN(LoanID, MemberID, BookID, DateOut, DateDue). MemberID is the primary key of MEMBER, BookID is the primary key of BOOK, "
      "and LoanID is the primary key of LOAN. ")
Q5T = ("The LOAN table holds these rows (LoanID, MemberID, BookID): (1, M01, B05), (2, M02, B05), (3, M01, B09), (4, M03, B02), (5, M01, B05). ")
Q6 = ("A half adder circuit has two inputs, A and B. Its sum output is S = A XOR B (S is 1 only when the two inputs are different). "
      "Its carry output is C = A AND B. ")

P2_QUESTIONS = [
    # ------------------------------------------------------------- Question 1
    Q("Question 1(a). " + Q1 + "Which expression describes X?", "X = (A AND B) OR (NOT C)",
      [("X = (A AND B) AND (NOT C)", "The last gate is an OR gate, not an AND gate."),
       ("X = NOT ((A AND B) OR C)", "The NOT gate is applied to input C only."),
       ("X = (A OR B) AND (NOT C)", "The AND and OR gates have been swapped.")],
      0, [S("First level of gates", text="AND gate: A AND B. NOT gate: NOT C."),
          S("Final gate", text="The OR gate joins them: (A AND B) OR (NOT C).")],
      "Paper 2", "Application", "Write the output of each gate, then join them with the last gate."),
    NUM("Question 1(b). " + Q1 + "How many rows does the truth table need to show every combination of A, B and C?", 8,
        steps=[S("Three inputs, two values each", math=r"2^3 = 8")],
        concept="Paper 2", skill="Calculation", hint="Each input can be 0 or 1."),
    NUM("Question 1(c). " + Q1 + "Find X when A = 1, B = 0 and C = 1. Give 0 or 1.", 0,
        steps=[S("AND gate", text="1 AND 0 = 0."),
               S("NOT gate", text="NOT 1 = 0."),
               S("OR gate", text="0 OR 0 = 0, so X = 0.")],
        concept="Paper 2", skill="Calculation", hint="Work out the AND gate and the NOT gate first."),
    NUM("Question 1(d). " + Q1 + "Find X when A = 1, B = 1 and C = 1. Give 0 or 1.", 1,
        steps=[S("AND gate", text="1 AND 1 = 1."),
               S("NOT gate", text="NOT 1 = 0."),
               S("OR gate", text="1 OR 0 = 1, so X = 1.")],
        concept="Paper 2", skill="Calculation", hint="An OR gate gives 1 when at least one input is 1."),
    NUM("Question 1(e). " + Q1 + "For how many of the 8 input combinations is X equal to 0?", 3,
        steps=[S("OR gives 0 only when both inputs are 0", text="So A AND B must be 0 and NOT C must be 0."),
               S("NOT C = 0", text="C must be 1."),
               S("A AND B = 0", text="Three of the four combinations of A and B give 0: 00, 01 and 10."),
               S("Count", text="3 rows have X = 0.")],
        concept="Paper 2", skill="Reasoning", hint="When does an OR gate give 0? Then work backwards to A, B and C."),
    # ------------------------------------------------------------- Question 2
    Q("Question 2(a). " + Q2 + "Which expression gives S?", "S = D AND N AND (NOT K)",
      [("S = D AND N AND K", "The alarm must sound when no valid key card has been used, so K needs a NOT."),
       ("S = (D OR N) AND (NOT K)", "The alarm needs the door open AND night, so these two use AND."),
       ("S = NOT (D AND N AND K)", "This is a NAND gate. It gives 1 in almost every case.")],
      1, [S("Translate each condition", text="Door open: D. Night: N. No valid key card: NOT K."),
          S("Join with AND", text="All three must be true: S = D AND N AND (NOT K).")],
      "Paper 2", "Application", "Which of the three inputs needs a NOT gate?"),
    NUM("Question 2(b). " + Q2 + "Find S when D = 1, K = 0 and N = 1. Give 0 or 1.", 1,
        steps=[S("NOT K", text="NOT 0 = 1."),
               S("AND of all three", text="1 AND 1 AND 1 = 1, so S = 1.")],
        concept="Paper 2", skill="Calculation", hint="Find NOT K first."),
    NUM("Question 2(c). " + Q2 + "Find S when D = 1, K = 1 and N = 1. Give 0 or 1.", 0,
        steps=[S("NOT K", text="NOT 1 = 0."),
               S("AND of all three", text="1 AND 1 AND 0 = 0, so S = 0.")],
        concept="Paper 2", skill="Calculation", hint="A valid key card was used, so what is NOT K?"),
    NUM("Question 2(d). " + Q2 + "For how many of the 8 input combinations does the alarm sound (S = 1)?", 1,
        steps=[S("All three conditions must hold", text="D = 1, N = 1 and NOT K = 1, so K = 0."),
               S("Count", text="Only the combination D = 1, K = 0, N = 1 works, so 1 row.")],
        concept="Paper 2", skill="Reasoning", hint="An AND gate with three inputs gives 1 only when every input is 1."),
    # ------------------------------------------------------------- Question 3
    NUM("Question 3(a). " + Q3 + "What is the value of total after the third mark (16) has been read and processed?", 28,
        steps=[S("i = 1, mark 12", text="12 is at least 10. total = 12, count = 1."),
               S("i = 2, mark 7", text="7 is less than 10. Nothing changes."),
               S("i = 3, mark 16", text="16 is at least 10. total = 12 + 16 = 28, count = 2.")],
        concept="Paper 2", skill="Calculation", hint="Marks below 10 do not change total."),
    NUM("Question 3(b). " + Q3 + "What is the final value of total after the loop?", 48,
        steps=[S("Marks that pass the test", text="12, 16 and 20 are at least 10. 7 and 9 are not."),
               S("Add", math=r"12 + 16 + 20 = 48")],
        concept="Paper 2", skill="Calculation", hint="Add only the marks that are 10 or more."),
    NUM("Question 3(c). " + Q3 + "What is the final value of count?", 3,
        steps=[S("Count the marks that are 10 or more", text="12, 16 and 20, so count = 3.")],
        concept="Paper 2", skill="Calculation", hint="count goes up by one each time the IF test is true."),
    NUM("Question 3(d). " + Q3 + "What is output?", 16,
        steps=[S("Substitute", math=r"\text{average} = \frac{48}{3} = 16")],
        concept="Paper 2", skill="Calculation", hint="Divide total by count."),
    Q("Question 3(e). " + Q3 + "Suppose all five marks were below 10. What would go wrong?",
      "Line 10 would divide by zero, because count would be 0",
      [("The loop would run forever", "A FOR loop runs exactly five times."),
       ("The output would be 0", "Dividing by zero is an error. It does not give 0."),
       ("Line 6 would run five times", "Line 6 runs only when the mark is 10 or more.")],
      3, [S("Trace with all marks below 10", text="The IF test is always false, so total stays 0 and count stays 0."),
          S("Line 10", text="0 divided by 0 is an error. A good algorithm tests that count is not 0 first.")],
      "Paper 2", "Reasoning", "What would count be if the IF test was never true?"),
    # ------------------------------------------------------------- Question 4
    NUM("Question 4(a). " + Q4 + "What is the value of n after the first pass of the loop?", 3,
        steps=[S("Test", text="n = 6 is greater than 1 and 6 MOD 2 = 0."),
               S("Update", math=r"n = 6 \text{ DIV } 2 = 3")],
        concept="Paper 2", skill="Calculation", hint="Is 6 even or odd? Choose the matching branch."),
    NUM("Question 4(b). " + Q4 + "What is the value of n after the third pass?", 5,
        steps=[S("Pass 1", text="n = 6 is even, so n = 3."),
               S("Pass 2", text="n = 3 is odd, so n = 3 × 3 + 1 = 10."),
               S("Pass 3", text="n = 10 is even, so n = 5.")],
        concept="Paper 2", skill="Calculation", hint="Write n after each pass. Odd values use the ELSE branch."),
    NUM("Question 4(c). " + Q4 + "What is output?", 8,
        steps=[S("Values of n after each pass", text="3, 10, 5, 16, 8, 4, 2, 1."),
               S("Count the passes", text="There are 8 values, so the loop runs 8 times and steps = 8.")],
        concept="Paper 2", skill="Calculation", hint="Keep going until n becomes 1."),
    Q("Question 4(d). " + Q4 + "Besides sequence, which two programming constructs does this algorithm use?",
      "Iteration (the WHILE loop) and selection (the IF statement)",
      [("Sequence only", "The WHILE loop repeats lines, and the IF statement chooses a branch."),
       ("Selection only", "The WHILE loop is iteration, so selection is not the only one."),
       ("Iteration only", "The IF statement is selection, so iteration is not the only one.")],
      2, [S("WHILE", text="It repeats lines while a condition is true. This is iteration."),
          S("IF ... THEN ... ELSE", text="It chooses between two branches. This is selection.")],
      "Paper 2", "Concept", "What does a loop do? What does an IF statement do?"),
    NUM("Question 4(e). The algorithm is: n ← 1, steps ← 0. WHILE n > 1: IF n MOD 2 = 0 THEN n ← n DIV 2 ELSE n ← 3 × n + 1, then steps ← steps + 1. "
        "After the loop, OUTPUT steps. What is output?", 0,
        steps=[S("Test the condition before the first pass", text="n = 1 is not greater than 1."),
               S("The loop body never runs", text="steps stays 0, so 0 is output.")],
        concept="Paper 2", skill="Reasoning", hint="A WHILE loop tests its condition before every pass, including the first."),
    # ------------------------------------------------------------- Question 5
    Q("Question 5(a). " + Q5 + "Which field is the primary key of the MEMBER table?", "MemberID",
      [("Name", "Two members can have the same name."),
       ("Phone", "Phone numbers can be shared or can change."),
       ("LoanID", "LoanID is the primary key of the LOAN table.")],
      1, [S("Read the question", text="The question text states that MemberID is the primary key of MEMBER."),
          S("Why it suits", text="Each member gets a different MemberID.")],
      "Paper 2", "Recall", "Which field is different for every member?"),
    Q("Question 5(b). " + Q5 + "Which fields of the LOAN table are foreign keys?", "MemberID and BookID",
      [("LoanID", "LoanID is the primary key of LOAN."),
       ("DateOut and DateDue", "These are ordinary date fields."),
       ("LoanID and DateDue", "Neither of these points to another table.")],
      3, [S("A foreign key holds a primary key value from another table", text="MemberID refers to MEMBER. BookID refers to BOOK."),
          S("Answer", text="MemberID and BookID.")],
      "Paper 2", "Concept", "Which LOAN fields are the primary keys of other tables?"),
    Q("Question 5(c). " + Q5 + "A member can borrow many books over time, and each loan belongs to one member. What type of relationship is this between MEMBER and LOAN?",
      "One-to-many",
      [("One-to-one", "A one-to-one relationship would allow each member only one loan."),
       ("Many-to-many", "Each loan row names one member only."),
       ("Many-to-one from MEMBER to LOAN", "This reverses the direction. One member has many loans.")],
      2, [S("One member", text="A member can appear in many LOAN rows."),
          S("One loan", text="A LOAN row names one member."),
          S("Answer", text="One-to-many.")],
      "Paper 2", "Concept", "How many loans can one member have? How many members does one loan have?"),
    Q("Question 5(d). " + Q5 + "Why is there a separate LOAN table instead of putting each loan inside the MEMBER table?",
      "It avoids repeating the member's name and phone number on every loan",
      [("It makes the database use more memory", "Separate tables save space by avoiding repeated data."),
       ("A table may have only three fields", "A table can have as many fields as it needs."),
       ("A primary key cannot be stored in the same table as dates", "Tables can hold keys and dates together.")],
      0, [S("What would happen otherwise", text="Each loan row would repeat the member's name and phone number."),
          S("Problems of repeated data", text="It wastes space and a change would have to be made in many places."),
          S("Answer", text="Separate tables avoid repeating data.")],
      "Paper 2", "Reasoning", "What would be repeated if loans were stored in MEMBER?"),
    Q("Question 5(e). " + Q5 + "Which data type is best for the DateDue field?", "Date",
      [("Text", "Text would work for display, but it cannot be sorted or compared as dates."),
       ("Number (integer)", "A date is not a whole number."),
       ("Yes/No", "A date has many possible values.")],
      1, [S("Think about what you will do with DateDue", text="You will want to sort loans and find those that are overdue."),
          S("Answer", text="Use the Date data type.")],
      "Paper 2", "Application", "Will you compare dates?"),
    NUM("Question 5(f). " + Q5T + "How many rows of the LOAN table belong to member M01?", 3,
        steps=[S("Look in the MemberID column", text="M01 appears in rows 1, 3 and 5."),
               S("Count", text="3 rows.")],
        concept="Paper 2", skill="Interpretation", hint="Count the rows whose MemberID is M01."),
    NUM("Question 5(g). " + Q5T + "How many different books has member M01 borrowed?", 2,
        steps=[S("Books on M01's rows", text="B05, B09 and B05."),
               S("Count different books", text="B05 appears twice but is one book. The different books are B05 and B09, so 2.")],
        concept="Paper 2", skill="Interpretation", hint="A book borrowed twice is still one book."),
    # ------------------------------------------------------------- Question 6
    NUM("Question 6(a). " + Q6 + "Find S when A = 1 and B = 1. Give 0 or 1.", 0,
        steps=[S("Inputs are the same", text="A = 1 and B = 1 are not different, so S = 0.")],
        concept="Paper 2", skill="Calculation", hint="S is 1 only when the inputs are different."),
    NUM("Question 6(b). " + Q6 + "Find C when A = 1 and B = 1. Give 0 or 1.", 1,
        steps=[S("AND gate", text="1 AND 1 = 1, so C = 1.")],
        concept="Paper 2", skill="Calculation", hint="C = A AND B."),
    NUM("Question 6(c). " + Q6 + "For A = 1 and B = 1, write C and S side by side as a two-digit binary number (C first). What is its value in decimal?", 2,
        steps=[S("Binary number", text="C = 1 and S = 0 give 10 in binary."),
               S("Convert", math=r"10_2 = 1 \times 2 + 0 \times 1 = 2")],
        concept="Paper 2", skill="Application", hint="Binary 10 means one two and no ones."),
]

SETS = [
    practice_set(
        module="Examination", topic="Paper 1",
        title="Paper 1 strategies practice", lesson="paper-1-multiple-choice-strategies-cs",
        questions=LESSON_SET),
    practice_set(
        module="Examination", topic="Paper 1",
        title="Paper 1 mock exam A", lesson="paper-1-multiple-choice-strategies-cs",
        mock=True, time_limit_minutes=90,
        questions=P1_QUESTIONS),
    practice_set(
        module="Examination", topic="Paper 2",
        title="Paper 2 mock exam A", lesson="paper-2-logic-gates-and-truth-tables",
        mock=True, time_limit_minutes=90,
        questions=P2_QUESTIONS),
]
