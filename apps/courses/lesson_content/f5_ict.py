"""Form 5 ICT (O Level): web design, legal, ethical and social aspects, and practical skills.

Draft content for review. These lessons are written for ICT students: more hands-on, built around
small practical tasks. Legal statements about Cameroon are kept general where the exact wording
of the law was not checked; reviewers should confirm them against the official texts.
"""

from .dsl import *  # noqa: F403

COURSE = ("ict", "form-5")

LESSONS = []

# ---------------------------------------------------------------------------
# Web Design & Publishing / HTML5 structure
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Web Design & Publishing",
    topic="HTML5 structure",
    title="Making a web page for a small business with HTML5",
    slug="ict-html5-business-web-page",
    minutes=30,
    summary="Create, save and view an HTML5 page for a small business, using headings, formatted text, links, images, a price table and an order form.",
    objectives=[
        "Create an HTML file in a text editor, save it with the .html extension and open it in a browser",
        "Use the correct tag hierarchy with html, head and body",
        "Format text with headings, paragraphs, bold, italic and lists",
        "Insert hyperlinks and images",
        "Build a price table and a simple order form",
    ],
    key_concepts=["HTML", "Tag", "Attribute", "Web browser", "Text editor", "Hyperlink", "Table", "Form"],
    blocks=[
        H("Introduction"),
        T("Mama Ngono runs a small pastry shop in Akwa, Douala. Her customers keep asking for her prices and "
          "opening hours. Her nephew, a Form 5 ICT student, offers to make her a simple web page.\n\n"
          "In this lesson you will do the same job step by step. You only need a text editor (such as Notepad) "
          "and a web browser. No internet connection is needed to build and test the page."),
        D("**HTML** (HyperText Markup Language) is the language used to build web pages. It marks up content with "
          "**tags** in angle brackets, such as <h1> and </h1>. A **web browser** (Chrome, Firefox, Edge) reads the "
          "tags and shows the page.", title="Definition"),
        KEY("Practical workflow", "Follow these steps every time you build a page.",
            cards=[["1. Write", "Type the HTML in a plain text editor such as Notepad, not in a word processor."],
                   ["2. Save", "Save as index.html with the encoding UTF-8. The extension must be .html, not .txt."],
                   ["3. View", "Double-click the file to open it in a browser."],
                   ["4. Edit and refresh", "Change the code, save, then press F5 in the browser to see the change."]]),
        H("The page skeleton"),
        T("Every page starts with <!DOCTYPE html>. The <html> element contains the <head>, which holds information "
          "such as the page title shown on the browser tab, and the <body>, which holds everything visitors see. "
          "Tags must be nested correctly: the last tag opened is the first one closed."),
        H("Formatting, links and images"),
        T("Use <h1> to <h6> for headings, <p> for paragraphs, <strong> for bold, <em> for italic and <br> for a "
          "line break. <ul> makes a bulleted list and <ol> a numbered list, with each item in <li>.\n\n"
          "A link uses <a href=\"address\">text</a>. An image uses <img src=\"file.jpg\" alt=\"description\">. Keep "
          "the image file in the same folder as the HTML file, or give its folder in src."),
        EX("Worked example 1: the top of the shop page", intro=(
            "Create the top part of the page: the tab title Ngono Pastries, a main heading, a photo cakes.jpg, a "
            "paragraph with the opening hours in bold, a bulleted list of three products and a link to a second "
            "page called contact.html."), steps=[
            S("Open Notepad and type the skeleton", text="<!DOCTYPE html>, then <html>, <head> with <title>Ngono Pastries</title>, and <body>."),
            S("Add the heading and image", text="<h1>Ngono Pastries</h1> then <img src=\"cakes.jpg\" alt=\"Tray of cakes\" width=\"300\">."),
            S("Add the hours", text="A <p> with the hours inside <strong> so they appear in bold."),
            S("Add the list and link", text="<ul> with three <li> items, then <a href=\"contact.html\">Contact us</a>."),
            S("Save and test", text="Save as index.html in the same folder as cakes.jpg, then open it in the browser. See Listing 1."),
        ]),
        CODE("""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Ngono Pastries</title>
  </head>
  <body>
    <h1>Ngono Pastries</h1>
    <img src="cakes.jpg" alt="Tray of cakes" width="300">
    <p>Open <strong>Monday to Saturday, 7 am to 7 pm</strong></p>
    <ul>
      <li>Beignets</li>
      <li>Meat pies</li>
      <li>Birthday cakes</li>
    </ul>
    <p><a href="contact.html">Contact us</a></p>
  </body>
</html>
""", "html", title="Listing 1: index.html"),
        H("Tables and forms"),
        T("A table is written row by row: <table> for the table, <tr> for each row, <th> for heading cells and <td> "
          "for data cells. A form uses <form> to hold controls such as <input type=\"text\">, <input type=\"number\">, "
          "<select> with <option> for a drop-down list, and <input type=\"submit\"> for the button."),
        EX("Worked example 2: a price table and an order form", intro=(
            "Add a table showing Item and Price (FCFA) with two products, Meat pie at 300 and Birthday cake at "
            "15000, and a form where a customer types a name, chooses an item from a drop-down list, enters a "
            "quantity and clicks Order."), steps=[
            S("Table heading row", text="<tr> with <th>Item</th> and <th>Price (FCFA)</th>."),
            S("Two data rows", text="Each is a <tr> with two <td> cells."),
            S("Form controls", text="A text box for the name, a <select> with two <option> items, a number box for the quantity."),
            S("Button and test", text="<input type=\"submit\" value=\"Order\">. Save, refresh and check the layout. See Listing 2."),
        ]),
        CODE("""
<h2>Prices</h2>
<table border="1">
  <tr><th>Item</th><th>Price (FCFA)</th></tr>
  <tr><td>Meat pie</td><td>300</td></tr>
  <tr><td>Birthday cake</td><td>15000</td></tr>
</table>

<h2>Order</h2>
<form action="order.php" method="post">
  <label for="cname">Your name:</label>
  <input type="text" id="cname" name="cname"><br>
  <label for="item">Item:</label>
  <select id="item" name="item">
    <option>Meat pie</option>
    <option>Birthday cake</option>
  </select><br>
  <label for="qty">Quantity:</label>
  <input type="number" id="qty" name="qty" min="1"><br>
  <input type="submit" value="Order">
</form>
""", "html", title="Listing 2: price table and order form (inside the body)",
             caption="The form needs a program on a web server (here order.php) to actually receive the order."),
        H("Common mistakes"),
        MISTAKE("Saving as index.html.txt", "Notepad may add .txt. Choose Save as type: All files and type the name "
                "index.html, or turn on file extensions in File Explorer to check."),
        MISTAKE("Image does not appear", "Check that the file name in src matches exactly, including capitals and "
                "the extension (cakes.jpg is not Cakes.JPG), and that the image is in the right folder."),
        MISTAKE("Closing tags in the wrong order", "<strong><em>Hi</strong></em> is wrong; close the inner tag first: "
                "<strong><em>Hi</em></strong>."),
        QUIZ("Which attribute of the <img> tag gives the name of the image file?",
             ["alt", "src", "href", "title"], 1,
             "src (source) gives the file name or address of the image.",
             feedback=["alt gives a text description of the image, not the file.", "",
                       "href is used in links, not images.", "title gives a tooltip, not the file."]),
        QUIZ("Which form control is best for choosing one item from a long list of products?",
             ["<input type=\"text\">", "<textarea>", "<select> with <option>", "<input type=\"password\">"], 2,
             "A drop-down list made with <select> and <option> lets the user pick one item and avoids spelling errors.",
             feedback=["A text box lets the user type anything, so spelling mistakes are likely.",
                       "A text area is for long free text such as a message.", "",
                       "A password box hides what is typed; it is for secrets, not choices."]),
        H("Practice questions"),
        PQ("Describe the steps to create a web page in Notepad and view it in a browser.",
           "Open Notepad and type the HTML code. Click File, Save As, choose All files, type a name ending in .html "
           "(e.g. index.html) and choose UTF-8 encoding. Open the saved file by double-clicking it, which opens it in "
           "the default web browser. After any change, save again and refresh the browser."),
        PQ("Write the HTML to show the text Call us on 6XX XX XX XX as a level 2 heading, followed by a link with the "
           "text Our menu that opens the page menu.html.",
           "<h2>Call us on 6XX XX XX XX</h2> followed by <a href=\"menu.html\">Our menu</a>. The link can be placed "
           "inside a <p> element."),
        PQ("A tailor in Bamenda wants a table on her web page with headings Garment and Price, and one row for a "
           "Kabba at 8000 FCFA. Write the HTML.",
           "<table border=\"1\"> <tr><th>Garment</th><th>Price</th></tr> <tr><td>Kabba</td><td>8000 FCFA</td></tr> "
           "</table>. The heading row uses <th> cells and the data row uses <td> cells."),
        SUM("Write HTML in a plain text editor, save with the .html extension, open in a browser and refresh after changes.",
            "Every page has <!DOCTYPE html>, then <html> with <head> and <body>; tags close in reverse order.",
            "Use headings, paragraphs, <strong>, <em> and lists to organise text.",
            "Links use <a href> and images use <img src alt>; check file names and folders carefully.",
            "Tables use <table>, <tr>, <th>, <td>; forms use <form>, <input>, <select> and a submit button."),
    ],
))


# ---------------------------------------------------------------------------
# Web Design & Publishing / CSS styling
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Web Design & Publishing",
    topic="CSS styling",
    title="Giving a website a consistent look with CSS",
    slug="ict-css-styling-a-website",
    minutes=30,
    summary="Style a small business website with CSS: choose inline, internal or external CSS, use selectors, set fonts and colours, and space elements with the box model.",
    objectives=[
        "Add CSS to a page inline, internally and with an external style sheet",
        "Choose the right method for a given task",
        "Write rules with element, class and id selectors",
        "Set fonts, text colour, background colour and alignment",
        "Use padding, border and margin to space out content",
    ],
    key_concepts=["CSS", "Selector", "Property and value", "External style sheet", "Class", "Id", "Box model"],
    blocks=[
        H("Introduction"),
        T("The Ngono Pastries website now has three pages: home, menu and contact. The owner wants all of them in "
          "her shop colours, brown and cream, with the same font. If the colour is typed into every page and she "
          "later changes her mind, every page must be edited again.\n\n"
          "**CSS** lets you write the design once, in one file, and apply it to every page."),
        D("**CSS** (Cascading Style Sheets) controls how HTML elements look: colours, fonts, sizes, spacing and "
          "layout. A CSS **rule** is a selector followed by declarations in curly brackets, each written as "
          "property, colon, value, semicolon.", title="Definition"),
        CODE("""
body {
  background-color: cornsilk;
  font-family: Arial, sans-serif;
}
""", "css", title="Listing 1: a rule with two declarations",
             caption="Selector: body. Each declaration ends with a semicolon."),
        H("Three places to put CSS"),
        KEY("Inline, internal, external", "Choose the method that fits the job.",
            cards=[["Inline", "style attribute on one tag. Use for a one-off change to a single element."],
                   ["Internal", "<style> element in the <head>. Use when only one page needs those styles."],
                   ["External", "A separate file such as style.css, linked from every page with <link rel=\"stylesheet\" href=\"style.css\">. Use for a whole website."]],
            note="When styles conflict, inline wins over internal and external; among rules of equal strength the last one wins."),
        KEY("Selectors", "Selectors choose which elements a rule styles.",
            cards=[["Element", "h1 { ... } styles every <h1>."],
                   ["Class", ".price { ... } styles every element with class=\"price\". Reusable."],
                   ["Id", "#logo { ... } styles the one element with id=\"logo\". Unique on the page."]]),
        EX("Worked example 1: an external style sheet for the whole site", intro=(
            "Create style.css so that every page has a cream background and Arial text, all h1 headings are brown "
            "and centred, and any element with class price is bold and red. Link it to index.html."), steps=[
            S("Create a new file in Notepad", text="Type the rules from Listing 2 and save it as style.css in the same folder as the HTML pages."),
            S("Element rules", text="body sets the background and font; h1 sets colour and alignment."),
            S("Class rule", text=".price { font-weight: bold; color: red; } applies to any element with class=\"price\"."),
            S("Link the sheet", text="In the <head> of each page add <link rel=\"stylesheet\" href=\"style.css\">."),
            S("Use the class", text="In the HTML write, for example, <td class=\"price\">300</td>. Save and refresh."),
        ]),
        CODE("""
/* style.css */
body {
  background-color: cornsilk;
  font-family: Arial, Helvetica, sans-serif;
}
h1 {
  color: saddlebrown;
  text-align: center;
}
.price {
  font-weight: bold;
  color: red;
}
""", "css", title="Listing 2: style.css"),
        CODE("""
<head>
  <meta charset="UTF-8">
  <title>Ngono Pastries</title>
  <link rel="stylesheet" href="style.css">
</head>
""", "html", title="Listing 3: linking the style sheet in each page"),
        H("Text and colour properties"),
        T("Useful properties: color (text colour), background-color, font-family, font-size (e.g. 18px), "
          "font-weight (bold), font-style (italic), text-align (left, center, right, justify), text-decoration "
          "(underline or none, often used to remove underlines from links) and line-height."),
        H("The box model: spacing things out"),
        D("Each element is a box with four layers from the inside out: **content**, **padding** (space inside the "
          "border), **border** (the line) and **margin** (space outside the border). Width sets the content only, so "
          "the total width is width plus padding, border and margin on both sides.", title="The box model"),
        EX("Worked example 2: an offer box", intro=(
            "Style a box with id offer for a special offer: content width 250px, padding 15px, a 3px solid brown "
            "border and a margin of 10px. (a) Write the CSS rule. (b) Calculate the total width."), steps=[
            S("Choose the selector", text="It is a single, unique element, so use an id selector: #offer."),
            S("Write the declarations", text="width: 250px; padding: 15px; border: 3px solid saddlebrown; margin: 10px;"),
            S("Total width", text="250 + (2 x 15) + (2 x 3) + (2 x 10) = 250 + 30 + 6 + 20 = 306px."),
        ]),
        CODE("""
#offer {
  width: 250px;
  padding: 15px;
  border: 3px solid saddlebrown;
  margin: 10px;
}
""", "css", title="Listing 4: the offer box",
             caption="In HTML: <div id=\"offer\">Buy 5 meat pies, get 1 free!</div>"),
        H("Common mistakes"),
        MISTAKE("Style sheet not linked or wrong file name", "If nothing changes, check the <link> tag is in the "
                "<head>, that href matches the file name exactly, and that style.css is in the same folder."),
        MISTAKE("Writing a full stop in the HTML class", "In CSS write .price; in HTML write class=\"price\", without "
                "the full stop."),
        MISTAKE("Using British spelling for properties", "CSS uses color and center. colour: red; and "
                "text-align: centre; are ignored by the browser."),
        QUIZ("A web designer wants all 12 pages of a site to share the same fonts and colours. Which method is best?",
             ["Inline CSS on every element", "Internal CSS on every page", "One external style sheet linked from every page", "Using <font> tags"], 2,
             "One external style sheet controls all pages, so the design is consistent and easy to change.",
             feedback=["Inline styles must be repeated on every element: slow and hard to change.",
                       "Internal styles must be copied into all 12 pages and kept the same by hand.", "",
                       "The <font> tag is obsolete in HTML5; styling should be done with CSS."]),
        H("Practice questions"),
        PQ("State one situation where each type of CSS is the best choice: inline, internal and external.",
           "Inline: changing the colour of one single word or element on one page. Internal: a single page that needs "
           "its own special styles, such as a one-page event poster. External: a website with several pages that must "
           "all share the same design."),
        PQ("Write CSS so that all paragraphs use font size 16px and grey text, and all links have no underline.",
           "p { font-size: 16px; color: grey; } and a { text-decoration: none; }"),
        PQ("An element has width 400px, padding 20px, border 1px and margin 25px on all sides. What is its total width?",
           "400 + (2 x 20) + (2 x 1) + (2 x 25) = 400 + 40 + 2 + 50 = 492px."),
        SUM("CSS controls the look of HTML; a rule is a selector plus property: value; declarations.",
            "Inline is for one element, internal for one page, external for a whole site.",
            "Element selectors style all tags of a type, classes (.name) style many chosen elements, ids (#name) style one.",
            "Use color, background-color, font-family, font-size and text-align for text.",
            "Box model: content, padding, border, margin; add them all on both sides for total width."),
    ],
))


# ---------------------------------------------------------------------------
# Legal, Ethical & Social Aspects / Intellectual property
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Legal, Ethical & Social Aspects",
    topic="Intellectual property",
    title="Using software and online content legally",
    slug="ict-copyright-piracy-licences",
    minutes=25,
    summary="Apply copyright rules in everyday ICT work: recognise software piracy, read software licences, choose legal software for a business and reuse online content correctly.",
    objectives=[
        "Explain copyright and intellectual property in simple terms",
        "Recognise software piracy in real situations and state its effects",
        "Read a licence and say what it allows: proprietary, freeware, shareware, open source",
        "Choose legal, affordable software for a school or business",
        "Reuse images and text correctly, giving credit where required",
    ],
    key_concepts=["Intellectual property", "Copyright", "Software piracy", "Licence", "Open-source software",
                  "Creative Commons", "Plagiarism"],
    blocks=[
        H("Introduction"),
        T("You are setting up the computers of a new cyber café in Buea. A friend offers you a USB key with "
          "\"all the programs, already cracked\" for 2000 FCFA. Later, a customer asks you to print a flyer using "
          "a photo he found on the internet.\n\n"
          "Both situations involve **intellectual property**. An ICT worker must know what is legal, because the "
          "business can be punished and its computers put at risk."),
        D("**Intellectual property** is a creation of the mind, such as software, music, a photo, a book or a logo. "
          "**Copyright** is the right of the creator to decide who may copy, share, sell or change the work. It "
          "exists automatically from the moment the work is created.", title="Definitions"),
        D("**Software piracy** is copying, installing, sharing or selling software without the copyright owner's "
          "permission. Using cracked programs, using one licence on many computers and selling copied discs are all "
          "piracy.", title="Software piracy"),
        KEY("Why piracy is a bad deal", "Piracy looks cheap but costs a lot.",
            cards=[["For the business", "Legal penalties, malware that damages machines or steals customer data, no updates and no support."],
                   ["For developers", "Lost income, so less new software, including from young Cameroonian developers."],
                   ["For the country", "Lost tax and a weaker local software industry."]]),
        H("Reading a licence"),
        D("A **licence** is the agreement that says how software or content may be used. You accept it when you "
          "install the program, usually by ticking I agree. Always check how many computers it covers and whether "
          "commercial use is allowed.", title="Licence"),
        KEY("Licence types at a glance", "What can you do with it?",
            cards=[["Proprietary", "Pay for a licence; no copying or changing. E.g. Microsoft Office, Adobe Photoshop."],
                   ["Freeware", "Free to use; code closed; may limit commercial use."],
                   ["Shareware", "Free trial, then pay to keep using or unlock features."],
                   ["Open source", "Free to use, study, change and share under conditions. E.g. LibreOffice, GIMP, Firefox, Linux. GPL keeps changes open; MIT allows almost any reuse if credit is kept."]]),
        KEY("Creative Commons for images and text", "Many photos and articles online carry a Creative Commons (CC) licence.",
            cards=[["BY", "Give credit to the creator."],
                   ["SA", "Share your new work under the same licence."],
                   ["NC", "Non-commercial use only."],
                   ["ND", "No changes allowed."]],
            note="CC0 means the creator has given up rights, so the work can be used freely."),
        EX("Worked example 1: equipping a cyber café legally on a small budget", intro=(
            "The Buea cyber café has 8 computers. The owner needs an operating system, an office suite, a web browser "
            "and an image editor, but has little money. Advise him."), steps=[
            S("Refuse the cracked programs", text="They are pirated: illegal, often infected with malware, and cannot be updated."),
            S("Office suite", text="Install LibreOffice, which is open source and free on all 8 computers, or buy enough licences for a paid suite."),
            S("Browser and image editor", text="Use Firefox or Chrome (free) and GIMP (open source) for image editing."),
            S("Operating system", text="Use the licensed system that came with each computer, or a free Linux distribution such as Ubuntu."),
            S("Keep records", text="Keep receipts and licence keys for any paid software to prove it is legal."),
        ]),
        EX("Worked example 2: a photo for a customer's flyer", intro=(
            "A customer wants to sell rice and asks you to print 200 flyers using a photo of rice bags found on the "
            "internet. The photo's page says CC BY-NC. What should you do?"), steps=[
            S("Read the licence", text="BY means credit the photographer. NC means non-commercial use only."),
            S("Apply it", text="A flyer to sell rice is commercial use, so this photo cannot be used."),
            S("Legal options", text="Take your own photo of the customer's rice, or find a photo marked CC0 or CC BY, and give credit if BY is required."),
        ]),
        H("Common mistakes"),
        MISTAKE("If I bought it, I can copy it", "Buying software usually buys a licence for one computer or user. "
                "Installing it on other computers needs more licences."),
        MISTAKE("Found on Google means free to use", "Search engines only find images; they do not give permission. "
                "Check the licence on the page where the image is published."),
        MISTAKE("Copying text into an assignment without credit", "This is plagiarism. Put the words in your own "
                "words, or quote and name the source."),
        QUIZ("A shop installs one copy of a paid accounting program, bought for one computer, on all five of its computers. This is:",
             ["Legal, because the program was paid for", "Software piracy", "Open-source use", "Allowed if the computers are in the same building"], 1,
             "The licence covers one computer. The other four copies are used without permission, which is piracy.",
             feedback=["Paying for one licence allows use on one computer only.", "",
                       "The program is proprietary, not open source.",
                       "The location of the computers does not change the number of licences needed."]),
        H("Practice questions"),
        PQ("Give three effects of software piracy on a business that uses pirated programs.",
           "Any three of: the business may be fined or prosecuted; pirated programs may contain viruses or spyware "
           "that damage computers or steal data; the software cannot receive security updates; there is no technical "
           "support; the business's reputation can suffer."),
        PQ("Name one open-source program that could replace each of these paid programs: (a) a word processor and "
           "spreadsheet suite (b) a photo editor.",
           "(a) LibreOffice (Writer and Calc). (b) GIMP. Both are open source, free to install on any number of computers."),
        PQ("Explain what each part of the licence CC BY-SA means for a student who wants to use a diagram in a school project.",
           "BY: the student must credit the creator of the diagram. SA: if the student changes the diagram and shares "
           "the new version, it must be shared under the same CC BY-SA licence."),
        SUM("Copyright gives creators control over copying and sharing of their work, automatically.",
            "Software piracy includes cracked programs, one licence on many machines and selling copies; it is illegal and risky.",
            "Check every licence: number of computers, cost and whether commercial use is allowed.",
            "Open-source programs such as LibreOffice and GIMP are legal low-cost choices.",
            "Online images and text need permission or a suitable Creative Commons licence, with credit given."),
    ],
))


# ---------------------------------------------------------------------------
# Legal, Ethical & Social Aspects / Cameroon legal framework
# REVIEW: legal details kept general on purpose. Confirm against the official texts of
# Law No. 2010/012 and Law No. 2010/013 of 21 December 2010, and check whether a newer
# personal data protection law should be named.
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Legal, Ethical & Social Aspects",
    topic="Cameroon legal framework",
    title="Staying safe and legal online in Cameroon",
    slug="ict-cameroon-cybersecurity-rules",
    minutes=25,
    summary="Know the Cameroonian laws and institutions on cybersecurity and cybercrime, spot common online scams, and handle personal data responsibly at school, in a cyber café or in a small business.",
    objectives=[
        "Name Law No. 2010/012 and Law No. 2010/013 and say what each covers",
        "State the roles of ANTIC and MINPOSTEL",
        "Recognise common cybercrimes such as phishing and mobile money scams",
        "Handle customers' personal data safely and lawfully",
        "Know what to do when you are a victim of cybercrime",
    ],
    key_concepts=["Cybercrime", "Cybersecurity", "Phishing", "Personal data", "ANTIC", "MINPOSTEL",
                  "Law No. 2010/012", "Law No. 2010/013"],
    blocks=[
        H("Introduction"),
        T("Brenda works at a cyber café in Molyko, Buea. Customers scan ID cards, print bank forms and log in to "
          "their email on the café's computers. One day a customer forgets to log out of his social media account, "
          "and another customer starts reading his messages.\n\n"
          "Who is responsible? What does the law say? This lesson gives you the practical rules for working "
          "safely and legally with ICT in Cameroon."),
        D("**Cybercrime** is an offence committed using computers, phones or networks, or against them. "
          "**Cybersecurity** is everything done to protect systems, networks and data from attacks and misuse.",
          title="Definitions"),
        H("The law and the institutions"),
        KEY("Two laws of 21 December 2010", "These are the main Cameroonian laws in this area.",
            cards=[["Law No. 2010/012", "Relating to cybersecurity and cybercrime. It defines offences such as unauthorised access to systems, interception of communications, damaging data and online fraud, and sets penalties."],
                   ["Law No. 2010/013", "Governing electronic communications: the organisation and regulation of telecommunication networks and services."]],
            note="Rules on personal data protection are developing; your teacher will confirm the current texts."),
        KEY("Institutions", "Know who does what.",
            cards=[["MINPOSTEL", "Ministry of Posts and Telecommunications: government policy on posts, telecoms and ICT."],
                   ["ANTIC", "National Agency for Information and Communication Technologies: regulates and promotes ICT activities and is responsible for the security of networks and information systems, including responding to security incidents."]]),
        H("Spotting common cybercrimes"),
        KEY("Warning signs", "Most scams follow the same patterns.",
            cards=[["Too good to be true", "\"You have won\" a prize or a job you never applied for."],
                   ["Urgency", "\"Send money now or your account will be blocked.\""],
                   ["Asking for secrets", "Any message asking for your PIN, password or a code sent to your phone."],
                   ["Odd links", "Links to addresses that look almost like a real bank or company."]]),
        D("**Phishing** is a trick where a criminal pretends to be a trusted organisation, by SMS, call, email or "
          "fake website, to make you reveal passwords, PINs or money.", title="Phishing"),
        H("Handling personal data at work"),
        T("**Personal data** is any information that identifies a person: name, phone number, ID card number, "
          "photo, address, bank details. Anyone who handles it at work should collect only what is needed, use it "
          "only for that purpose, keep it secure, and never share it without the person's consent or a legal reason."),
        EX("Worked example 1: a cyber café privacy routine", intro=(
            "Write a short routine Brenda should follow to protect customers' data at the cyber café."), steps=[
            S("After each customer", text="Log out of all accounts, close the browser and clear the browsing history and saved passwords."),
            S("Scanned documents", text="Delete scanned ID cards and forms from the computer and the Recycle Bin once the customer has their copy."),
            S("Printing", text="Never keep or reuse spoiled prints with personal details; shred or tear them."),
            S("Protect the machines", text="Keep antivirus updated, use a standard (not administrator) account for customers, and do not install unknown programs."),
            S("Inform customers", text="Put up a notice reminding customers to log out and not to save passwords."),
        ]),
        EX("Worked example 2: responding to a mobile money scam", intro=(
            "A student in Bafoussam receives a call: \"I am from your mobile money service. Give me the code we just "
            "sent you so we can reverse a wrong transfer.\" What should she do, and what if she already gave the code?"), steps=[
            S("Recognise the scam", text="A real operator never asks for your PIN or a secret code. This is phishing."),
            S("Do not give the code", text="Hang up and call the operator's official customer service number yourself."),
            S("If the code was given", text="Contact the operator immediately to block the account, and change the PIN."),
            S("Report it", text="Report the number to the operator and to the police or gendarmerie, keeping screenshots and details of the call as evidence."),
        ]),
        H("Common mistakes"),
        MISTAKE("Sharing a code because the caller sounds official", "Criminals copy the names and language of real "
                "companies. Never share PINs, passwords or one-time codes with anyone."),
        MISTAKE("Keeping customers' scans just in case", "Storing personal data you no longer need increases the risk of "
                "theft. Delete it when the job is done."),
        MISTAKE("Thinking a joke hack is harmless", "Logging into a friend's account without permission is still "
                "unauthorised access, which the cybercrime law treats as an offence."),
        QUIZ("Which of the following is a sign of a phishing message?",
             ["It comes from a friend you were expecting to hear from",
              "It asks you urgently to send your PIN to unblock your account",
              "It is a receipt for a payment you just made",
              "It is written in French"], 1,
             "Urgency plus a request for a secret such as a PIN is a classic sign of phishing.",
             feedback=["An expected message from a known person is not, by itself, a warning sign.", "",
                       "A receipt for a payment you really made is normal.",
                       "The language of a message does not show whether it is a scam."]),
        QUIZ("What is ANTIC?",
             ["The Ministry of Posts and Telecommunications",
              "The National Agency for Information and Communication Technologies",
              "A mobile network operator",
              "An antivirus program"], 1,
             "ANTIC is the National Agency for Information and Communication Technologies.",
             feedback=["That is MINPOSTEL.", "", "ANTIC is a public agency, not a company that sells network services.",
                       "The name sounds similar, but ANTIC is a government agency."]),
        H("Practice questions"),
        PQ("Name the Cameroonian law that deals with cybersecurity and cybercrime, and give two acts it treats as offences.",
           "Law No. 2010/012 of 21 December 2010 relating to cybersecurity and cybercrime in Cameroon. Offences include, "
           "for example, accessing a computer system without permission, intercepting communications, damaging or "
           "changing data without permission, and fraud using networks."),
        PQ("List four things a cyber café attendant should do to protect customers' personal data.",
           "Any four of: log out of accounts and clear history after each customer; delete scanned documents after use; "
           "destroy spoiled prints containing personal details; keep antivirus updated; give customers limited user "
           "accounts; never share customers' information; remind customers not to save passwords."),
        PQ("Define phishing and give two ways to protect yourself from it.",
           "Phishing is pretending to be a trusted organisation in order to trick people into revealing passwords, PINs "
           "or money. Protection: never share PINs, passwords or codes; check the sender and web address carefully; call "
           "the organisation on its official number; do not click links in unexpected messages."),
        SUM("Law No. 2010/012 covers cybersecurity and cybercrime; Law No. 2010/013 governs electronic communications.",
            "MINPOSTEL sets ICT and telecom policy; ANTIC regulates ICT activity and handles network security.",
            "Phishing and mobile money scams use urgency and requests for secrets; never share PINs or codes.",
            "Collect only needed personal data, keep it secure and delete it when no longer needed.",
            "Report cybercrime quickly to the service provider and the police, keeping evidence."),
    ],
))


# ---------------------------------------------------------------------------
# Legal, Ethical & Social Aspects / Social and economic impact
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Legal, Ethical & Social Aspects",
    topic="Social and economic impact",
    title="How ICT changes work and communities",
    slug="ict-social-economic-impact",
    minutes=25,
    summary="Look at the digital divide, automation, e-waste and remote collaboration through practical Cameroonian situations, and learn to write balanced answers.",
    objectives=[
        "Explain the digital divide and propose practical solutions for a community",
        "Describe how automation changes jobs in banks, shops and offices",
        "Dispose of old ICT equipment responsibly",
        "Set up and evaluate remote collaboration for a team",
        "Write balanced answers with specific examples",
    ],
    key_concepts=["Digital divide", "Automation", "E-waste", "Recycling", "Remote collaboration", "Teleworking"],
    blocks=[
        H("Introduction"),
        T("A cooperative of cocoa farmers near Kumba wants to sell directly to buyers using phones and a shared "
          "spreadsheet. Some members have smartphones, others have only basic phones, and the village gets network "
          "only on a hill. Meanwhile the cooperative's old computer has died, and someone suggests burning it with "
          "the rubbish.\n\n"
          "ICT brings new chances to earn and work together, but it also creates new problems. This lesson looks at "
          "four of them."),
        H("The digital divide"),
        D("The **digital divide** is the gap between people who can access and use ICT (devices, internet, skills) "
          "and people who cannot. In Cameroon it is often seen between towns and villages, rich and poor, and young "
          "and old.", title="Definition"),
        T("Practical ways to narrow the gap include community telecentres and school labs, solar charging, cheaper "
          "data bundles, offline apps and content, training programmes for adults, and services that also work on "
          "basic phones (for example by SMS or USSD codes)."),
        H("Automation"),
        D("**Automation** means using machines and software to do tasks that people used to do. It can lead to "
          "**job displacement**, where workers lose jobs, but it also creates new jobs.", title="Definition"),
        KEY("Automation in everyday Cameroon", "Some examples of tasks that are now automated.",
            cards=[["Banking", "Cash machines and mobile money reduce queues and some cashier work."],
                   ["Shops", "Barcode scanners and computerised tills speed up sales and stock control."],
                   ["Offices", "Spreadsheets and accounting software do calculations once done by hand."],
                   ["New jobs", "Technicians, mobile money agents, phone repairers, web designers, data clerks."]]),
        H("E-waste"),
        D("**E-waste** is discarded electronic equipment such as phones, computers, chargers and batteries. It "
          "contains toxic substances (for example lead and mercury) and valuable materials.", title="Definition"),
        KEY("Reduce, reuse, recycle", "The responsible order of actions for old equipment.",
            cards=[["Reduce", "Buy durable devices and look after them so they last longer."],
                   ["Reuse and repair", "Repair faults, upgrade parts, or donate working devices to schools."],
                   ["Recycle", "Take dead devices to a proper collection or recycling point. Never burn them."]],
            note="Before giving away or recycling a device, back up and then erase personal data from it."),
        H("Remote collaboration"),
        D("**Remote collaboration** is working together from different places using tools such as shared online "
          "documents, video calls, email and messaging groups.", title="Definition"),
        EX("Worked example 1: the cooperative's plan", intro=(
            "Suggest a practical ICT plan so that all members of the Kumba cocoa cooperative can share sales "
            "information, including those with basic phones."), steps=[
            S("Central record", text="The secretary keeps one shared online spreadsheet of sales and prices, updated when there is network."),
            S("Reach basic phones", text="Send weekly prices to all members by SMS, which works on any phone."),
            S("Power", text="Buy a small solar panel to charge the phones used for the cooperative's work."),
            S("Skills", text="Run a short training day so more members can read and update the records."),
        ]),
        EX("Worked example 2: disposing of the old computer", intro=(
            "Explain why the cooperative should not burn the old computer, and describe what it should do instead."), steps=[
            S("Why not burn it", text="Burning releases toxic smoke and leaves metals such as lead in the soil and water near farms and homes."),
            S("Protect data", text="Remove or wipe the hard disk, which may hold members' personal and financial data."),
            S("Reuse parts", text="Ask a technician whether parts such as memory or the screen can be reused."),
            S("Recycle the rest", text="Take what remains to a proper e-waste collection or recycling point."),
        ]),
        H("Common mistakes"),
        MISTAKE("Answers with only advantages", "Questions that ask you to discuss or evaluate expect both sides. Give "
                "at least one benefit and one problem."),
        MISTAKE("Forgetting data when disposing of devices", "An old phone or computer may still hold photos, contacts "
                "and passwords. Back up and erase before donating or recycling."),
        MISTAKE("Thinking remote collaboration needs no rules", "Teams need agreed times, one shared version of each "
                "file and clear roles, or work is duplicated and lost."),
        QUIZ("Which is the most responsible way to deal with a broken laptop that cannot be repaired?",
             ["Burn it with household rubbish", "Throw it in a river",
              "Erase the data, then take it to a proper e-waste collection or recycling point", "Leave it in a corner of the office"], 2,
             "Erasing data protects privacy, and proper recycling keeps toxic materials out of the environment.",
             feedback=["Burning releases toxic smoke and pollutes the soil.", "Toxic metals would poison the water.", "",
                       "It takes space and its useful materials and data are not handled properly."]),
        QUIZ("Which service helps reduce the digital divide for people with basic phones only?",
             ["A video-calling app", "Services that work by SMS or USSD codes", "A high-resolution streaming site", "A desktop-only program"], 1,
             "SMS and USSD services work on any mobile phone, without a smartphone or internet data.",
             feedback=["Video calls need a smartphone and a strong internet connection.", "",
                       "Streaming needs a smartphone and lots of data.", "Desktop programs need a computer."]),
        H("Practice questions"),
        PQ("A bank in Garoua installs cash machines and a mobile banking app. Give two benefits for customers and one "
           "effect on bank workers.",
           "Benefits: customers can withdraw money or check balances at any time, including weekends; shorter queues "
           "and less travel. Effect on workers: fewer cashiers may be needed, so some may lose their jobs or need "
           "retraining for other roles, while new technical jobs appear."),
        PQ("Give three practical steps a school can take to reduce the digital divide among its students.",
           "Any three of: open the computer lab after classes; provide offline learning resources; use solar power for "
           "the lab; give ICT training to students and parents; lend devices; negotiate cheaper data for students."),
        PQ("State two advantages and two disadvantages of remote collaboration for a small business team.",
           "Advantages: less travel time and cost; team members in different towns can work on the same document; "
           "work can continue when someone cannot come to the office. Disadvantages: needs reliable power and internet; "
           "less face-to-face contact; risk of data leaks if accounts are not secured; harder to supervise work."),
        SUM("The digital divide is unequal access to ICT; telecentres, solar power, cheap data, offline content and SMS services help.",
            "Automation speeds up work in banks, shops and offices; it removes some jobs and creates others.",
            "E-waste is toxic: reduce, reuse and repair, then recycle properly, never burn; erase data first.",
            "Remote collaboration uses shared files, messaging and video calls but needs power, internet and clear rules.",
            "Discussion answers need both sides and specific local examples."),
    ],
))


# ---------------------------------------------------------------------------
# Practical skills / Office productivity
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Practical skills",
    topic="Office productivity",
    title="Word processing and spreadsheet modelling",
    slug="ict-word-processing-spreadsheets",
    minutes=30,
    summary="Produce well-formatted documents and mail-merged letters, and build a spreadsheet model with formulas, functions, relative and absolute references and what-if changes.",
    objectives=[
        "Format a document with styles, headers and footers, tables and page setup",
        "Explain and carry out a mail merge",
        "Enter formulas and functions such as SUM, AVERAGE, MAX, MIN and IF",
        "Distinguish relative and absolute cell references when copying formulas",
        "Use a spreadsheet model to answer what-if questions",
    ],
    key_concepts=["Word processor", "Mail merge", "Spreadsheet", "Cell reference", "Formula", "Function",
                  "Absolute reference", "Spreadsheet model"],
    blocks=[
        H("Introduction"),
        T("Mr Tabi runs a small provision store in Limbe. Every term he writes the same letter to parents who buy "
          "school supplies on credit, and every evening he adds up his sales by hand in an exercise book. Both jobs "
          "take hours and mistakes are common.\n\n"
          "A **word processor** (such as Microsoft Word or LibreOffice Writer) and a **spreadsheet** (such as "
          "Microsoft Excel or LibreOffice Calc) can do these jobs in minutes. In the practical exam you are expected "
          "to use both confidently."),
        H("Word processing essentials"),
        KEY("Features you should use", "Good documents are consistent and easy to read.",
            cards=[["Styles", "Apply Heading 1, Heading 2 and Normal styles instead of formatting each line by hand; a table of contents can then be made automatically."],
                   ["Page setup", "Margins, orientation (portrait or landscape) and paper size (A4)."],
                   ["Headers and footers", "Text repeated on every page, such as the business name and page numbers."],
                   ["Tables", "Rows and columns for lists such as price lists; borders and shading make them clear."]]),
        D("**Mail merge** combines a **main document** (a standard letter with placeholders called merge fields) with "
          "a **data source** (a list such as a table of names and amounts) to produce one personalised copy for each "
          "record in the list.", title="Mail merge"),
        EX("Worked example 1: mail-merged reminder letters", intro=(
            "Mr Tabi wants to send a personal reminder to each of 40 parents showing their name, child's name and "
            "amount owed. Describe the steps using mail merge."), steps=[
            S("Create the data source", text="Make a table (in a spreadsheet or word processor) with columns ParentName, ChildName and Amount, one row per parent."),
            S("Write the main document", text="Type the letter once, leaving gaps where the personal details go."),
            S("Insert merge fields", text="Using the Mailings (or Mail Merge) tool, connect the data source and insert the fields ParentName, ChildName and Amount in the gaps."),
            S("Preview", text="Preview the results to check that names and amounts appear correctly."),
            S("Merge", text="Finish the merge to a new document or straight to the printer: 40 personalised letters are produced."),
        ]),
        H("Spreadsheet basics"),
        D("A **spreadsheet** is a grid of **cells**, each named by its column letter and row number, such as B3. A "
          "**formula** starts with an equals sign and calculates a value, for example =B2+C2. A **function** is a "
          "ready-made formula such as SUM, AVERAGE, MAX, MIN, COUNT and IF.", title="Definitions"),
        T("In formulas, the plus sign adds, the minus sign subtracts, the asterisk multiplies and the forward slash "
          "divides. Functions take a range such as B2:B6, meaning all cells from B2 to B6."),
        D("When you copy a formula, a **relative reference** (such as B2) changes to match the new position. An "
          "**absolute reference** stays fixed: it is written with a dollar sign before the column letter and before "
          "the row number, as shown in the listings below. Use it for a single cell that every formula must use, "
          "such as a discount rate.", title="Relative and absolute references"),
        EX("Worked example 2: a daily sales model", intro=(
            "Mr Tabi's sheet has items in column A, unit prices (FCFA) in column B and quantities sold in column C, "
            "in rows 2 to 6. Cell F1 holds a discount rate of 10%. Create formulas for the total, discounted total, "
            "grand total, best sale and a restock warning."), steps=[
            S("Total for row 2", text="In D2 multiply price by quantity: =B2 times C2 (see Listing 1). Copy down to D6; the references change row by row."),
            S("Discounted total", text="In E2 use the fixed discount cell F1 as an absolute reference, then copy down. Every row still points at F1."),
            S("Grand total and best sale", text="In D7 use SUM over D2:D6. In D8 use MAX over D2:D6."),
            S("Restock warning", text="Column G holds stock left. In H2 use IF: if G2 is less than 5, show Restock, otherwise OK."),
            S("What-if", text="Change F1 to 15% and every discounted total updates instantly. This is the power of a model."),
        ]),
        CODE("""
D2:  =B2*C2
E2:  =D2*(1-$F$1)
D7:  =SUM(D2:D6)
D8:  =MAX(D2:D6)
H2:  =IF(G2<5,"Restock","OK")

After copying row 2 down to row 3:
D3:  =B3*C3            (relative: row number changed)
E3:  =D3*(1-$F$1)      (absolute part $F$1 did not change)
""", "text", title="Listing 1: formulas for the sales model",
             caption="The asterisk means multiply. The dollar signs in $F$1 make the reference absolute."),
        T("A **spreadsheet model** is a sheet that represents a real situation with data and formulas, so you can "
          "change an input (price, quantity, rate) and immediately see the effect on the outputs. Asking what "
          "happens if an input changes is called **what-if analysis**."),
        H("Common mistakes"),
        MISTAKE("Forgetting the equals sign", "Typing B2+C2 shows the text itself. A formula must start with =."),
        MISTAKE("Using a relative reference for a fixed cell", "If the discount formula uses F1 without dollar signs, "
                "copying it down changes it to F2, F3 and so on, which are empty, giving wrong results."),
        MISTAKE("Typing numbers instead of cell references", "A formula such as =300 times 4 does not update when the "
                "price changes. Refer to the cells (=B2 times C2) so the model stays correct."),
        MISTAKE("Formatting headings by hand", "Making each heading bold and size 16 manually is slow and "
                "inconsistent. Use heading styles."),
        QUIZ("Cell E2 contains a formula with the reference F1 made absolute. It is copied to E5. What does the reference become?",
             ["F4", "F5", "It stays F1", "E5"], 2,
             "An absolute reference is fixed, so it still points to F1 after copying.",
             feedback=["That would happen to a relative reference copied down 3 rows.", "That mixes up the reference with the destination row.", "",
                       "The reference does not become the address of the cell it is copied into."]),
        QUIZ("Which function finds the largest value in the range C2:C20?",
             ["SUM(C2:C20)", "MAX(C2:C20)", "COUNT(C2:C20)", "AVERAGE(C2:C20)"], 1,
             "MAX returns the largest value in a range.",
             feedback=["SUM adds all the values.", "", "COUNT counts how many cells contain numbers.", "AVERAGE gives the mean."]),
        H("Practice questions"),
        PQ("(a) What is mail merge? (b) Name the two files needed and give one advantage of mail merge.",
           "(a) Mail merge combines a standard document with a list of data to produce a personalised copy for each "
           "person in the list. (b) The main document (letter with merge fields) and the data source (list of records). "
           "Advantage: many personalised letters are produced quickly from one letter, with fewer typing errors."),
        PQ("Cells B2 to B11 hold the marks of 10 students. Write formulas to find (a) the total, (b) the average, (c) "
           "the highest mark. (d) In C2, write a formula that shows Pass if B2 is 50 or more, otherwise Fail.",
           "(a) =SUM(B2:B11) (b) =AVERAGE(B2:B11) (c) =MAX(B2:B11) (d) =IF(B2>=50,\"Pass\",\"Fail\")"),
        PQ("Explain the difference between a relative and an absolute cell reference, and say when an absolute "
           "reference is needed.",
           "A relative reference changes when a formula is copied to another cell, so it always points to the cell in "
           "the same relative position. An absolute reference, written with dollar signs before the column and row, "
           "stays the same when copied. It is needed when every copied formula must use the same single cell, such as "
           "a tax rate, discount rate or exchange rate."),
        SUM("Use styles, page setup, headers and footers and tables for professional documents.",
            "Mail merge joins a main document with a data source to make personalised copies.",
            "Formulas start with =; functions such as SUM, AVERAGE, MAX, MIN and IF save time.",
            "Relative references change when copied; absolute references (with dollar signs) stay fixed.",
            "A spreadsheet model lets you change inputs and see results instantly: what-if analysis."),
    ],
))


# ---------------------------------------------------------------------------
# Practical skills / Databases
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Practical skills",
    topic="Databases",
    title="Creating and querying a relational database",
    slug="ict-relational-database-queries",
    minutes=30,
    summary="Design tables with suitable fields, data types and keys, link them in a relational database, and query them with SQL and query design tools.",
    objectives=[
        "Define database, table, record, field, primary key and foreign key",
        "Choose suitable field names and data types",
        "Create tables and enter records",
        "Link two tables with a relationship",
        "Write queries with SELECT, WHERE, ORDER BY and simple calculations",
    ],
    key_concepts=["Database", "Table", "Record", "Field", "Data type", "Primary key", "Foreign key", "Query", "SQL"],
    blocks=[
        H("Introduction"),
        T("The library of a secondary school in Bamenda records its books and borrowers in a big register. To find "
          "which students have not returned books, the librarian must read through hundreds of lines.\n\n"
          "A **database** stores the same information in an organised way so that the computer can find, sort and "
          "count it in seconds. Programs such as Microsoft Access, LibreOffice Base or MySQL are used to build them."),
        D("A **database** is an organised collection of related data. In a **relational database** the data is stored "
          "in **tables** that are linked to each other.", title="Definition"),
        KEY("Parts of a table", "Every table is made of rows and columns.",
            cards=[["Field", "A column: one item of information, such as Surname or DateOfBirth."],
                   ["Record", "A row: all the information about one thing, such as one student or one book."],
                   ["Primary key", "A field whose value is unique for every record, such as StudentID. It identifies each record."],
                   ["Foreign key", "A field in one table that is the primary key of another table. It creates the link between them."]]),
        KEY("Common data types", "Choose the type that matches the data.",
            cards=[["Text (VARCHAR)", "Names, addresses, and also phone numbers, which are not used in calculations."],
                   ["Number (INTEGER, DECIMAL)", "Quantities and prices used in calculations."],
                   ["Date/Time", "Dates such as DateBorrowed."],
                   ["Boolean (Yes/No)", "Only two values, such as Returned: Yes or No."]]),
        H("Designing and creating the tables"),
        EX("Worked example 1: designing the library database", intro=(
            "Design two linked tables for the library: one for students and one for loans. State the primary key of "
            "each, the foreign key and the data type of every field."), steps=[
            S("Students table", text="StudentID (text, primary key), Surname (text), FirstName (text), Class (text)."),
            S("Loans table", text="LoanID (integer, primary key), StudentID (text), BookTitle (text), DateBorrowed (date), Returned (Boolean)."),
            S("Identify the foreign key", text="StudentID in Loans is a foreign key: it matches the primary key of Students."),
            S("Describe the relationship", text="One student can have many loans, so it is a one-to-many relationship from Students to Loans."),
        ]),
        CODE("""
CREATE TABLE Students (
  StudentID  VARCHAR(10) PRIMARY KEY,
  Surname    VARCHAR(30),
  FirstName  VARCHAR(30),
  Class      VARCHAR(10)
);

CREATE TABLE Loans (
  LoanID       INTEGER PRIMARY KEY,
  StudentID    VARCHAR(10),
  BookTitle    VARCHAR(60),
  DateBorrowed DATE,
  Returned     BOOLEAN,
  FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);

INSERT INTO Students VALUES ('S001', 'Nfor', 'Grace', 'F5A');
INSERT INTO Loans VALUES (1, 'S001', 'Things Fall Apart', '2026-10-02', FALSE);
""", "sql", title="Listing 1: creating the tables and adding records",
             caption="In Access or Base you can do the same in Design View, then type records in Datasheet View."),
        TIP("Use a validation rule to stop bad data, for example a quantity that must be greater than 0, or a Class "
            "that must be chosen from a list."),
        H("Querying the database"),
        D("A **query** asks the database a question and returns only the matching records and fields. In SQL the "
          "basic form is SELECT (which fields), FROM (which table), WHERE (which records) and ORDER BY (how to sort).",
          title="Query"),
        EX("Worked example 2: finding overdue books", intro=(
            "Write queries to (a) list the titles and dates of loans that have not been returned, oldest first, "
            "(b) list the surname of each student with a book not yet returned, and (c) count the loans not yet returned."), steps=[
            S("(a) One table", text="SELECT BookTitle, DateBorrowed FROM Loans WHERE Returned is FALSE, sorted by DateBorrowed ascending."),
            S("(b) Two tables", text="Join Students and Loans where the StudentID values match, then keep only records not returned."),
            S("(c) Count", text="Use the aggregate function COUNT with the same condition."),
            S("Check", text="Run each query and compare a few results with the data you entered. See Listing 2."),
        ]),
        CODE("""
-- (a) loans not returned, oldest first
SELECT BookTitle, DateBorrowed
FROM Loans
WHERE Returned = FALSE
ORDER BY DateBorrowed ASC;

-- (b) students who still have a book
SELECT Students.Surname, Loans.BookTitle
FROM Students
JOIN Loans ON Students.StudentID = Loans.StudentID
WHERE Loans.Returned = FALSE;

-- (c) how many loans are not returned
SELECT COUNT(*) FROM Loans WHERE Returned = FALSE;
""", "sql", title="Listing 2: queries for worked example 2"),
        T("Conditions can use comparison operators (equals, not equal, greater than, less than) and combine with AND "
          "and OR. Text values go in single quotes, for example WHERE Class = 'F5A'. In a design grid, you type the "
          "same condition in the Criteria row under the field."),
        H("Common mistakes"),
        MISTAKE("Choosing a primary key that can repeat", "Surname is not a good primary key because two students can "
                "share a surname. Use a unique code such as StudentID."),
        MISTAKE("Storing phone numbers as numbers", "Phone numbers are not used in calculations and may start with a "
                "zero or a plus sign. Store them as text."),
        MISTAKE("Forgetting quotes around text in conditions", "WHERE Class = F5A fails; write WHERE Class = 'F5A'. "
                "Numbers do not need quotes."),
        QUIZ("In the Loans table, StudentID links each loan to a student in the Students table. In Loans, StudentID is a:",
             ["Primary key", "Foreign key", "Record", "Data type"], 1,
             "A field that holds the primary key of another table is a foreign key; it creates the relationship.",
             feedback=["The primary key of Loans is LoanID; StudentID can repeat in Loans.", "",
                       "A record is a whole row, not one field.", "A data type describes what kind of value a field holds."]),
        QUIZ("Which SQL clause chooses which records are returned?", ["SELECT", "FROM", "WHERE", "ORDER BY"], 2,
             "WHERE gives the condition that records must meet.",
             feedback=["SELECT chooses the fields (columns), not the records.", "FROM names the table.", "",
                       "ORDER BY sorts the results; it does not filter them."]),
        H("Practice questions"),
        PQ("Define the terms (a) field (b) record (c) primary key, using a pharmacy's Medicines table as an example.",
           "(a) A field is one column of data, e.g. MedicineName or Price. (b) A record is one row holding all the data "
           "about one medicine. (c) A primary key is a field with a unique value for each record, e.g. MedicineCode, "
           "used to identify each medicine."),
        PQ("A table Products has fields Code, Name, Price and Quantity. Write an SQL query to show the Name and Price "
           "of products costing more than 1000 FCFA, sorted from the most expensive.",
           "SELECT Name, Price FROM Products WHERE Price > 1000 ORDER BY Price DESC;"),
        PQ("Suggest a suitable data type for each field of a Customers table: CustomerID, FullName, PhoneNumber, "
           "DateJoined, IsMember.",
           "CustomerID: text (or auto-number). FullName: text. PhoneNumber: text, because it is not used in "
           "calculations and may start with 6, 0 or a plus sign. DateJoined: date. IsMember: Boolean (Yes/No)."),
        SUM("A relational database stores data in linked tables made of fields (columns) and records (rows).",
            "Every table needs a primary key with unique values; a foreign key links to another table's primary key.",
            "Choose data types carefully: text for names and phone numbers, numbers for calculations, dates for dates.",
            "Queries use SELECT, FROM, WHERE and ORDER BY; JOIN combines linked tables and COUNT counts records.",
            "Put text values in single quotes and check query results against the data."),
    ],
))
