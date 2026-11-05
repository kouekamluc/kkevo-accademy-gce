"""Form 5 Computer Science (O Level): web design and legal, ethical and social aspects.

Draft content for review. Legal statements about Cameroon are kept general where the exact
wording of the law was not checked; reviewers should confirm them against the official texts.
"""

from .dsl import *  # noqa: F403

COURSE = ("computer-science", "form-5")

LESSONS = []

# ---------------------------------------------------------------------------
# Web Design & Publishing / HTML5 structure
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Web Design & Publishing",
    topic="HTML5 structure",
    title="Building a web page with HTML5",
    slug="html5-page-structure",
    minutes=30,
    summary="Write a complete HTML5 document: the doctype, head and body, headings and text formatting, links, images, tables and forms.",
    objectives=[
        "Write the basic skeleton of an HTML5 document starting with <!DOCTYPE html>",
        "Explain the tag hierarchy: elements, nesting, opening and closing tags, attributes",
        "Use tags for headings, paragraphs, lists and text formatting",
        "Add hyperlinks and images with the correct attributes",
        "Build simple tables and forms",
    ],
    key_concepts=["HTML", "Tag and element", "Attribute", "Nesting", "Hyperlink", "Table", "Form"],
    blocks=[
        H("Introduction"),
        T("Imagine your school, GBHS Limbe, wants a simple website. It should show the school name, a welcome "
          "message, the principal's photo, a table of exam dates and a form where parents can send a message.\n\n"
          "Every page you open in a browser, from a school site to the GCE Board site, is built with **HTML** "
          "(HyperText Markup Language). In this lesson you will write such a page yourself."),
        D("**HTML** is a markup language that describes the structure of a web page. It uses **tags** written "
          "inside angle brackets, such as <p> and </p>, to mark up content. A browser reads the tags and displays "
          "the content.", title="Definition",
          note="HTML is not a programming language: it has no variables, loops or decisions. It only describes structure."),
        H("Tags, elements and attributes"),
        KEY("The parts of an HTML element", "Most elements have an opening tag, some content and a closing tag. "
            "The closing tag has a forward slash.",
            cards=[["Opening tag", "<p> starts a paragraph."],
                   ["Content", "The text or other elements inside."],
                   ["Closing tag", "</p> ends the paragraph."],
                   ["Attribute", "Extra information in the opening tag, e.g. href=\"page.html\" in a link."]],
            note="Some elements are empty and have no closing tag, for example <br> (line break) and <img> (image)."),
        D("**Nesting** means placing one element inside another. Elements must close in the reverse order they "
          "opened: the last one opened is the first one closed. This creates a tree, or **hierarchy**, of elements "
          "with <html> at the top.", title="Nesting and hierarchy"),
        H("The skeleton of an HTML5 document"),
        T("Every HTML5 page starts with the doctype declaration <!DOCTYPE html>. It tells the browser to use "
          "HTML5 rules. Then comes the <html> element, which contains two parts: the <head> (information about the "
          "page, such as its title) and the <body> (everything the visitor sees)."),
        CODE("""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>GBHS Limbe</title>
  </head>
  <body>
    <h1>Welcome to GBHS Limbe</h1>
    <p>We are a government bilingual high school in the South West Region.</p>
  </body>
</html>
""", "html", title="Listing 1: a minimal HTML5 page",
             caption="The text in <title> appears on the browser tab, not on the page itself."),
        H("Text formatting, lists and links"),
        T("Headings go from <h1> (most important, largest) down to <h6>. Paragraphs use <p>. For emphasis use "
          "<strong> (bold, strong importance) and <em> (italic, emphasis). Unordered (bulleted) lists use <ul>, "
          "ordered (numbered) lists use <ol>, and each item in either list is an <li>.\n\n"
          "A **hyperlink** uses the anchor tag <a>. Its href attribute gives the address to go to. An image uses "
          "<img> with the src attribute (the file) and the alt attribute (a text description for visitors who "
          "cannot see the image, and for when the image fails to load)."),
        EX("Worked example 1: a news section with a link and an image", intro=(
            "Write HTML for a section of the school site that has the heading Latest News, a photo called "
            "principal.jpg described as Photo of the principal, a numbered list of two events (Sports day and "
            "Open day) and a link with the text exam results page that opens https://www.example.com."), steps=[
            S("Choose the heading level", text="It is a section heading below the main page title, so use <h2>."),
            S("Add the image", text="Use <img> with src=\"principal.jpg\" and alt=\"Photo of the principal\". It is an empty element, so there is no closing tag."),
            S("Add the numbered list", text="Numbered means ordered, so use <ol> with one <li> for each event."),
            S("Add the link", text="Use <a href=\"https://www.example.com\">exam results page</a>. The visible text goes between the tags."),
            S("Check the nesting", text="Every opened tag is closed in reverse order. See Listing 2."),
        ]),
        CODE("""
<h2>Latest News</h2>
<img src="principal.jpg" alt="Photo of the principal" width="200">
<ol>
  <li>Sports day</li>
  <li>Open day</li>
</ol>
<p>Visit the <a href="https://www.example.com">exam results page</a>.</p>
""", "html", title="Listing 2: answer to worked example 1"),
        H("Tables and forms"),
        T("A **table** is built row by row. <table> holds the whole table, <tr> is a table row, <th> is a "
          "heading cell (bold and centred by default) and <td> is an ordinary data cell. The border attribute or "
          "CSS adds lines around the cells.\n\n"
          "A **form** collects information from the visitor. <form> holds the controls. Its action attribute says "
          "where the data is sent and its method attribute says how (get or post). Inside, <input> creates text "
          "boxes, password boxes, radio buttons, check boxes and submit buttons depending on its type attribute. "
          "<label> names a control, <textarea> is a box for several lines and <select> with <option> makes a drop-down list."),
        EX("Worked example 2: an exam timetable table and a contact form", intro=(
            "Write HTML for (a) a table with headings Subject and Date and two rows: Mathematics, 3 June and "
            "Computer Science, 5 June; (b) a form with a text box for the parent's name, a box for a message and "
            "a Send button."), steps=[
            S("Start the table and the heading row", text="<table border=\"1\"> then a <tr> containing two <th> cells."),
            S("Add one row per subject", text="Each row is a <tr> with two <td> cells."),
            S("Start the form", text="<form action=\"contact.php\" method=\"post\">. Post is used because a message should not appear in the address bar."),
            S("Add the controls", text="A <label> and an <input type=\"text\"> for the name, a <textarea> for the message, and <input type=\"submit\" value=\"Send\">."),
            S("Close everything", text="Close </table> and </form>. See Listing 3."),
        ]),
        CODE("""
<table border="1">
  <tr><th>Subject</th><th>Date</th></tr>
  <tr><td>Mathematics</td><td>3 June</td></tr>
  <tr><td>Computer Science</td><td>5 June</td></tr>
</table>

<form action="contact.php" method="post">
  <label for="pname">Parent's name:</label>
  <input type="text" id="pname" name="pname">
  <label for="msg">Message:</label>
  <textarea id="msg" name="msg" rows="4"></textarea>
  <input type="submit" value="Send">
</form>
""", "html", title="Listing 3: answer to worked example 2"),
        H("Common mistakes"),
        MISTAKE("Closing tags in the wrong order", "<p><strong>Hello</p></strong> is wrong. The last tag opened "
                "(<strong>) must be closed first: <p><strong>Hello</strong></p>."),
        MISTAKE("Putting visible content in the head", "Headings, paragraphs and images belong in the <body>. "
                "The <head> holds the title, character set and links to style sheets."),
        MISTAKE("Forgetting the alt attribute", "Always describe images with alt. It helps blind visitors using "
                "screen readers and shows text when a slow connection fails to load the image."),
        QUIZ("Which tag creates a hyperlink?", ["<link>", "<a>", "<href>", "<url>"], 1,
             "The anchor tag <a> creates a hyperlink; its href attribute holds the address.",
             hint="href is an attribute, not a tag.",
             feedback=["<link> goes in the head and connects files such as style sheets; it is not clickable.", "",
                       "href is the attribute inside <a>, not a tag of its own.", "There is no <url> tag in HTML."]),
        QUIZ("In a table, which tag starts a new row?", ["<td>", "<th>", "<tr>", "<row>"], 2,
             "<tr> stands for table row. Cells (<td> or <th>) go inside it.",
             feedback=["<td> is a data cell inside a row.", "<th> is a heading cell inside a row.", "",
                       "There is no <row> tag in HTML."]),
        H("Practice questions"),
        PQ("State the purpose of each of the following: (a) <!DOCTYPE html> (b) the <head> element (c) the alt attribute of <img>.",
           "(a) It tells the browser that the document uses HTML5. (b) It holds information about the page that is not "
           "displayed in the page area, such as the title shown on the tab, the character set and links to CSS files. "
           "(c) It gives a text description of the image, read by screen readers and shown if the image cannot load."),
        PQ("Distinguish between an ordered list and an unordered list, giving the tags used for each.",
           "An ordered list numbers its items (1, 2, 3...) and uses <ol>. An unordered list shows bullets and uses <ul>. "
           "In both, each item is written in an <li> element."),
        PQ("A cyber café in Buea wants a web page form that asks for a customer's name, a password and their choice of "
           "service (Printing or Browsing) using radio buttons. Name the HTML element and type attribute value used for "
           "each of the three controls, and for the submit button.",
           "Name: <input type=\"text\">. Password: <input type=\"password\">, which hides the characters typed. Service: "
           "two <input type=\"radio\"> elements with the same name attribute so only one can be chosen. Submit button: "
           "<input type=\"submit\">. All of them go inside a <form> element."),
        PQ("Find and correct the error in this line: <p>Our <em>new</em> lab opens in <strong>September</p></strong>",
           "The <strong> element was opened inside <p> but closed after </p>. Corrected: "
           "<p>Our <em>new</em> lab opens in <strong>September</strong></p>."),
        SUM("An HTML5 document starts with <!DOCTYPE html>, then <html> containing <head> and <body>.",
            "Elements have opening and closing tags; attributes in the opening tag add information.",
            "Nested elements must close in reverse order, forming a hierarchy.",
            "Use <h1> to <h6>, <p>, <strong>, <em>, <ul>, <ol> and <li> for text.",
            "<a href> makes links and <img src alt> shows images.",
            "Tables use <table>, <tr>, <th> and <td>; forms use <form>, <input>, <label>, <textarea> and <select>."),
    ],
))


# ---------------------------------------------------------------------------
# Web Design & Publishing / CSS styling
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Web Design & Publishing",
    topic="CSS styling",
    title="Styling web pages with CSS",
    slug="css-styling-selectors-box-model",
    minutes=30,
    summary="Use inline, internal and external CSS; write rules with element, class and id selectors; style text and apply the box model.",
    objectives=[
        "Explain what CSS is and why style is kept separate from structure",
        "Apply CSS in three ways: inline, internal and external, and compare them",
        "Write CSS rules using element, class and id selectors",
        "Style text with font, size, colour and alignment properties",
        "Describe and calculate with the box model: content, padding, border and margin",
    ],
    key_concepts=["CSS", "CSS rule", "Selector", "Inline CSS", "Internal CSS", "External CSS", "Box model"],
    blocks=[
        H("Introduction"),
        T("Your school website from the last lesson works, but it looks plain: black text on white, everything on "
          "the left. The school colours of a college in Bamenda might be green and gold, and the principal wants "
          "every page to use them.\n\n"
          "Changing the colour on fifty separate pages one by one would take hours. **CSS** solves this: you describe "
          "the look once and every page follows it."),
        D("**CSS** (Cascading Style Sheets) is a language that describes how HTML elements are displayed: colours, "
          "fonts, sizes, spacing and layout. HTML gives the structure; CSS gives the presentation.",
          title="Definition"),
        H("The CSS rule"),
        T("A CSS rule has a **selector**, which chooses the elements to style, and a **declaration block** in curly "
          "brackets. Each declaration is a property, a colon, a value and a semicolon."),
        CODE("""
h1 {
  color: darkgreen;
  font-size: 32px;
  text-align: center;
}
""", "css", title="Listing 1: one CSS rule",
             caption="Selector: h1. Properties: color, font-size, text-align. Note the American spelling color."),
        KEY("Three kinds of selector", "Selectors decide which elements a rule applies to.",
            cards=[["Element selector", "p { ... } styles every <p> on the page."],
                   ["Class selector", ".notice { ... } styles every element with class=\"notice\". It starts with a full stop and can be reused many times."],
                   ["Id selector", "#banner { ... } styles the one element with id=\"banner\". It starts with a hash; an id should be unique on a page."]]),
        H("Three ways to add CSS"),
        KEY("Inline, internal and external CSS", "The same style can be written in three places.",
            cards=[["Inline", "In a style attribute on one element: <p style=\"color:red;\">. Affects only that element."],
                   ["Internal", "In a <style> element inside the <head>. Affects only that page."],
                   ["External", "In a separate .css file linked from each page with <link rel=\"stylesheet\" href=\"style.css\">. One file styles the whole site."]],
            note="If rules conflict, inline styles win over internal and external ones, and a later rule wins over an earlier one of the same strength. This is the cascade."),
        EX("Worked example 1: one style, three methods", intro=(
            "Make the paragraph Welcome to our school appear in blue using (a) inline CSS, (b) internal CSS and "
            "(c) external CSS. State one advantage of the external method."), steps=[
            S("Inline", text="Put the declaration in the style attribute of the <p> tag itself."),
            S("Internal", text="In the <head>, write a <style> element containing the rule p { color: blue; }."),
            S("External", text="Write the same rule in a file style.css and add <link rel=\"stylesheet\" href=\"style.css\"> in the <head> of each page."),
            S("Advantage of external CSS", text="One file controls every page, so a change made once updates the whole site. Pages are also smaller and the browser can cache the file."),
        ]),
        CODE("""
<!-- (a) inline -->
<p style="color: blue;">Welcome to our school</p>

<!-- (b) internal: inside <head> -->
<style>
  p { color: blue; }
</style>

<!-- (c) external: inside <head> of every page -->
<link rel="stylesheet" href="style.css">
""", "html", title="Listing 2: the three methods in HTML"),
        H("Typography: styling text"),
        T("Common text properties are font-family (the typeface, e.g. Arial), font-size (e.g. 16px), font-weight "
          "(e.g. bold), font-style (e.g. italic), color (text colour), text-align (left, center, right, justify), "
          "text-decoration (e.g. underline or none) and line-height (space between lines). Background colour uses "
          "background-color."),
        TIP("Give font-family a list such as Arial, Helvetica, sans-serif. If the first font is missing on the "
            "computer, the browser tries the next one."),
        H("The box model"),
        D("In CSS every element is treated as a rectangular **box** made of four layers, from the inside out: the "
          "**content** (text or image), the **padding** (space between content and border), the **border** (a line "
          "around the padding) and the **margin** (space outside the border, separating the box from its neighbours). "
          "By default, width sets the content width only; the total width adds padding, border and margin on both sides.",
          title="The box model"),
        EX("Worked example 2: total width of a box", intro=(
            "A notice box on a Douala business website has this CSS: width 300px, padding 10px, border 2px solid, "
            "margin 20px (each value applies to all four sides). Calculate the total horizontal space it takes."), steps=[
            S("Content width", text="300px."),
            S("Add padding on both sides", text="10px + 10px = 20px, so 320px so far."),
            S("Add border on both sides", text="2px + 2px = 4px, so 324px so far."),
            S("Add margin on both sides", text="20px + 20px = 40px. Total = 300 + 20 + 4 + 40 = 364px."),
        ]),
        CODE("""
.notice {
  width: 300px;
  padding: 10px;
  border: 2px solid darkgreen;
  margin: 20px;
  background-color: lightyellow;
  font-family: Arial, Helvetica, sans-serif;
}
""", "css", title="Listing 3: the notice box from worked example 2",
             caption="In HTML: <div class=\"notice\">Shop closed on Sunday</div>"),
        H("Common mistakes"),
        MISTAKE("Missing semicolons or colons", "color blue is wrong. Each declaration needs a colon between the property "
                "and value and a semicolon at the end: color: blue;"),
        MISTAKE("Mixing up class and id symbols", "A class selector starts with a full stop (.notice); an id selector "
                "starts with a hash (#banner). In the HTML, write class=\"notice\" without the full stop."),
        MISTAKE("Confusing padding and margin", "Padding is inside the border (the background colour fills it). Margin "
                "is outside the border and is always transparent."),
        QUIZ("Which CSS method lets one file control the appearance of every page on a website?",
             ["Inline CSS", "Internal CSS", "External CSS", "A <title> element"], 2,
             "An external style sheet is linked from every page, so one change updates the whole site.",
             feedback=["Inline CSS affects only the single element it is written on.",
                       "Internal CSS affects only the page in whose head it is written.", "",
                       "<title> sets the text on the browser tab; it does not style anything."]),
        QUIZ("Which part of the box model is the space between the content and the border?",
             ["Margin", "Padding", "Outline", "Width"], 1,
             "Padding sits between the content and the border; margin is outside the border.",
             feedback=["Margin is outside the border, between this box and others.", "",
                       "An outline is drawn outside the border and is not one of the four box layers.",
                       "Width is the size of the content area itself."]),
        H("Practice questions"),
        PQ("Write a CSS rule that makes all level 2 headings red, centred and in the Verdana font.",
           "h2 { color: red; text-align: center; font-family: Verdana, sans-serif; }"),
        PQ("Explain the difference between a class selector and an id selector, giving an example of each.",
           "A class selector (e.g. .warning) can style many elements that have class=\"warning\". An id selector "
           "(e.g. #footer) styles the single element with id=\"footer\"; an id should appear only once on a page. "
           "In CSS a class starts with a full stop and an id with a hash."),
        PQ("A box has width 200px, padding 15px, border 5px and margin 10px on all sides. Calculate its total width.",
           "200 + (2 x 15) + (2 x 5) + (2 x 10) = 200 + 30 + 10 + 20 = 260px."),
        PQ("Give two advantages of external CSS over inline CSS.",
           "Any two of: one file styles every page, so changes are made once; HTML files stay shorter and easier to "
           "read because style is separate from structure; the site has a consistent look; the browser can cache the "
           "CSS file so later pages load faster."),
        SUM("CSS describes presentation; HTML describes structure.",
            "A rule is a selector plus declarations of the form property: value;",
            "Element selectors style all tags of a type, .class selectors style many chosen elements, #id selectors style one element.",
            "CSS can be inline, internal (in <style>) or external (a linked .css file); external is best for a whole site.",
            "The box model is content, padding, border and margin; total width adds all of them on both sides."),
    ],
))


# ---------------------------------------------------------------------------
# Legal, Ethical & Social Aspects / Intellectual property
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Legal, Ethical & Social Aspects",
    topic="Intellectual property",
    title="Intellectual property, piracy and software licences",
    slug="intellectual-property-and-licences",
    minutes=25,
    summary="Understand copyright, why software piracy is illegal and harmful, and how proprietary, freeware, shareware and open-source licences (GPL, MIT, Creative Commons) differ.",
    objectives=[
        "Define intellectual property and copyright",
        "Explain what software piracy is and give its effects",
        "Distinguish proprietary software, freeware, shareware and open-source software",
        "Compare the GPL, MIT and Creative Commons licences",
        "Decide whether a given use of software or content is legal",
    ],
    key_concepts=["Intellectual property", "Copyright", "Software piracy", "Software licence", "Open source",
                  "GPL", "MIT licence", "Creative Commons"],
    blocks=[
        H("Introduction"),
        T("Walk past some shops in Douala or Yaoundé and you may see discs or USB keys sold with expensive programs "
          "already installed for a tiny price. A musician in Bamenda may find her new song shared on WhatsApp the "
          "day after it is released, and she earns nothing from it.\n\n"
          "Both cases are about **intellectual property**: who owns the work of the mind, and who may copy it. "
          "As a computer user and future programmer, you must know your rights and the rights of others."),
        D("**Intellectual property** (IP) is a creation of the mind, such as a program, a song, a book, a design, an "
          "invention or a brand name, that the law treats as belonging to its creator.", title="Definition"),
        D("**Copyright** is the legal right of the creator of an original work (for example software, music, text or "
          "images) to control how it is copied, distributed, sold or changed. It applies automatically when the work "
          "is created; no registration is needed. It lasts for a long time, usually many years after the author's "
          "death, with the exact period set by law.", title="Copyright"),
        KEY("Other forms of intellectual property", "Copyright is not the only kind of IP.",
            cards=[["Patent", "Protects an invention, such as a new machine or process, for a limited number of years."],
                   ["Trademark", "Protects a brand name or logo, such as the name and logo of a mobile network."],
                   ["Copyright", "Protects the expression of an idea: the actual code, text, music or picture."]],
            note="In Cameroon, copyright is governed by national law, and patents and trademarks are registered through OAPI, the African Intellectual Property Organization, whose headquarters are in Yaoundé."),
        H("Software piracy"),
        D("**Software piracy** is the illegal copying, distribution, sale or use of software without the permission "
          "of the copyright owner, for example installing one licensed copy on many computers, using a cracked "
          "program or selling copied software.", title="Software piracy"),
        T("Piracy harms software developers, who lose income and may stop making products. It harms the country, "
          "because local software companies cannot grow and the state loses tax. It also harms the user: pirated "
          "and cracked programs often carry viruses and spyware, cannot be updated, and get no support."),
        H("Types of software licence"),
        D("A **software licence** is a legal agreement that states how a program may be used, copied and shared. "
          "When you buy software, you usually buy a licence to use it, not the program itself.", title="Software licence"),
        KEY("Four kinds of licence", "Licences range from very closed to very open.",
            cards=[["Proprietary (commercial)", "Paid for; source code is secret; copying and changing are forbidden. Example: Microsoft Office."],
                   ["Freeware", "Free to use, but source code is closed and you may not change it. Example: many free media players."],
                   ["Shareware", "Free trial for a limited time or with limited features, then you must pay."],
                   ["Open source", "Source code is published; you may study, change and share it under the licence terms. Examples: Linux, LibreOffice, Firefox."]]),
        KEY("Open licences compared", "Open licences differ in what they require when you share.",
            cards=[["GPL (GNU General Public Licence)", "You may use, change and share the code, but if you distribute a changed version you must release its source code under the GPL too. This is called copyleft."],
                   ["MIT licence", "Very permissive: you may do almost anything, even use the code in a closed, paid product, as long as you keep the original copyright notice."],
                   ["Creative Commons (CC)", "Used mainly for content such as text, images and music. Options include BY (credit the author), SA (share alike), NC (non-commercial) and ND (no derivatives)."]]),
        EX("Worked example 1: is it legal?", intro=(
            "A cyber café owner in Buea buys one licence for a proprietary office suite and installs it on all 10 "
            "computers in the café. Is this legal? Explain, and suggest a legal alternative."), steps=[
            S("Identify the licence type", text="It is proprietary software. The licence normally allows installation on one computer only (unless it is a multi-user licence)."),
            S("Compare with what happened", text="It was installed on 10 computers with only one licence."),
            S("Conclusion", text="This is software piracy: nine copies are used without permission. It breaks copyright law."),
            S("Legal alternatives", text="Buy 10 licences or a site licence, or install a free open-source office suite such as LibreOffice on every computer."),
        ]),
        EX("Worked example 2: choosing a licence", intro=(
            "Three students in Bamenda write a free app that shows market prices. They want anyone to be able to "
            "improve it, but they do not want a company to take their code, change it and sell it as a closed "
            "product. Which licence, GPL or MIT, suits them better? Explain."), steps=[
            S("What the MIT licence allows", text="Anyone may reuse the code in a closed, paid product as long as the copyright notice stays. That is what the students want to avoid."),
            S("What the GPL requires", text="Anyone who distributes a changed version must also publish its source code under the GPL."),
            S("Conclusion", text="The GPL suits them better, because its copyleft rule keeps every distributed version open."),
        ]),
        H("Common mistakes"),
        MISTAKE("Thinking free means open source", "Freeware costs nothing but its source code is closed. Open source "
                "means the code is available to study and change, even if someone charges for a copy."),
        MISTAKE("Thinking anything on the internet is free to use", "Images, songs and articles online are still "
                "protected by copyright unless the owner gives permission, for example with a Creative Commons licence."),
        MISTAKE("Saying copyright protects ideas", "Copyright protects the expression of an idea (the actual code or "
                "text), not the idea itself. Two people can write different programs that do the same job."),
        QUIZ("Which licence requires anyone who distributes a modified version to release the source code under the same licence?",
             ["MIT licence", "GPL", "Freeware licence", "Shareware licence"], 1,
             "The GPL is a copyleft licence: modified versions that are distributed must stay open under the GPL.",
             feedback=["The MIT licence is permissive: modified versions may be closed.", "",
                       "Freeware does not give you the source code to modify in the first place.",
                       "Shareware is a try-before-you-buy model; its code is closed."]),
        H("Practice questions"),
        PQ("(a) Define software piracy. (b) Give two reasons why software piracy is harmful.",
           "(a) Software piracy is copying, distributing, selling or using software without the permission of the "
           "copyright owner. (b) Any two of: developers lose income and may stop producing software; local software "
           "businesses cannot grow; the state loses tax revenue; pirated copies may contain malware; users get no "
           "updates or support."),
        PQ("Distinguish between freeware and open-source software.",
           "Both may be obtained free of charge, but freeware keeps its source code closed, so users may not study or "
           "change it. Open-source software publishes its source code and allows users to study, modify and share it "
           "under the terms of its licence."),
        PQ("A student downloads a photo from a website and uses it on the cover of a school magazine that is sold "
           "for 500 FCFA. The photo has the licence CC BY-NC. Has the student respected the licence? Explain.",
           "No. BY means the photographer must be credited, and NC means non-commercial use only. Selling the magazine "
           "is a commercial use, so it breaks the NC condition, even if the photographer is credited. The student "
           "should ask permission or choose an image whose licence allows commercial use."),
        PQ("State two differences between proprietary software and open-source software.",
           "Proprietary software usually has to be paid for and its source code is secret; open-source software makes "
           "its source code available. Users may not modify or redistribute proprietary software, but they may modify "
           "and share open-source software within the licence terms."),
        SUM("Intellectual property is a creation of the mind protected by law; copyright protects original works such as software.",
            "Software piracy is copying or using software without the owner's permission; it is illegal and harmful.",
            "Proprietary, freeware, shareware and open-source licences give users very different rights.",
            "The GPL keeps distributed changes open (copyleft); the MIT licence is permissive.",
            "Creative Commons licences let creators share content with conditions such as BY, SA, NC and ND."),
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
    title="Cybersecurity, cybercrime and data privacy in Cameroon",
    slug="cameroon-cyber-law-framework",
    minutes=25,
    summary="Know the main Cameroonian laws on cybersecurity, cybercrime and electronic communications, the roles of ANTIC and MINPOSTEL, common cybercrimes and good data privacy practice.",
    objectives=[
        "Name the 2010 Cameroonian laws on cybersecurity and cybercrime and on electronic communications",
        "State the roles of MINPOSTEL and ANTIC",
        "Define cybercrime and recognise common cybercrimes",
        "Explain why personal data must be protected and how to protect it",
        "Apply the law to simple scenarios",
    ],
    key_concepts=["Cybercrime", "Cybersecurity", "Law No. 2010/012", "Law No. 2010/013", "ANTIC", "MINPOSTEL",
                  "Personal data", "Data privacy"],
    blocks=[
        H("Introduction"),
        T("A trader in Douala receives an SMS: \"You have won 500 000 FCFA. Send 10 000 FCFA by mobile money to "
          "claim your prize.\" A student in Buea finds that someone has taken over his social media account and is "
          "asking his friends for money. These are not just bad luck: they are **crimes**.\n\n"
          "Cameroon has laws that define such acts as offences and public bodies that protect the country's "
          "networks. This lesson introduces them."),
        D("**Cybercrime** is any illegal act committed using a computer, a phone or a network, or aimed at them. "
          "**Cybersecurity** is the set of measures (technical, legal and human) used to protect systems, networks "
          "and data from attack, damage or unauthorised access.", title="Definitions"),
        H("The main laws"),
        KEY("Two key laws of 21 December 2010", "Cameroon passed two important laws on the same day.",
            cards=[["Law No. 2010/012", "Relating to cybersecurity and cybercrime in Cameroon. It defines offences committed through electronic communication networks and information systems, and sets out penalties."],
                   ["Law No. 2010/013", "Governing electronic communications in Cameroon: how telecommunication networks and services are organised and regulated."]],
            note="Other texts, such as the Penal Code and rules on personal data, also apply. Your teacher will confirm the latest texts."),
        T("In general terms, the cybersecurity and cybercrime law makes it an offence to, among other things, access "
          "a computer system without permission, intercept communications, damage or alter data, commit fraud "
          "using networks, and publish certain illegal content such as child abuse material. It also places "
          "security obligations on network operators and service providers."),
        H("The institutions"),
        KEY("Who does what", "Two public bodies are central to ICT regulation and security.",
            cards=[["MINPOSTEL", "The Ministry of Posts and Telecommunications. It prepares and carries out government policy on posts, telecommunications and ICT."],
                   ["ANTIC", "The National Agency for Information and Communication Technologies. It promotes and regulates ICT activities and is in charge of security of electronic communication networks and information systems, including running a team that responds to computer security incidents."]],
            note="Telecom operators are also regulated by a separate regulator, the Telecommunications Regulatory Board (ART)."),
        H("Common cybercrimes"),
        KEY("Examples you should recognise", "Most cybercrimes fall into a few groups.",
            cards=[["Hacking", "Entering a computer or account without permission."],
                   ["Phishing and scams", "Fake messages, calls or websites that trick people into giving PINs, passwords or money, e.g. fake mobile money prizes."],
                   ["Identity theft", "Using someone else's personal details or account to pretend to be them."],
                   ["Malware", "Spreading viruses, ransomware or spyware that damage data or steal information."],
                   ["Cyberbullying and illegal content", "Harassing people online or sharing illegal or defamatory material."]]),
        H("Data privacy"),
        D("**Personal data** is any information that identifies a person: name, phone number, address, ID card number, "
          "photo, school records or bank details. **Data privacy** is the right of a person to control how their "
          "personal data is collected, used and shared.", title="Personal data"),
        T("Organisations that collect personal data, such as a school, a hospital or a mobile money agent, should "
          "collect only what they need, use it only for the stated purpose, keep it accurate, store it securely "
          "(passwords, encryption, backups, locked rooms) and not share it without consent or a legal reason."),
        EX("Worked example 1: identifying the offence", intro=(
            "A Form 5 student guesses the password of the school's results system and changes his own marks. "
            "(a) Name the cybercrime. (b) Name the Cameroonian law that covers it. (c) Suggest two measures the "
            "school should take."), steps=[
            S("(a) Name the offence", text="Unauthorised access to a computer system (hacking), plus unauthorised alteration of data."),
            S("(b) Name the law", text="Law No. 2010/012 of 21 December 2010 relating to cybersecurity and cybercrime in Cameroon."),
            S("(c) Measures", text="Any two of: strong passwords changed regularly; different user accounts with limited access rights; an audit log of who changed which record; regular backups so altered data can be restored."),
        ]),
        EX("Worked example 2: protecting customer data", intro=(
            "A mobile money agent in Bafoussam keeps a notebook with each customer's name, phone number and ID card "
            "number, and leaves it on the counter. Explain two risks and two ways to protect the data."), steps=[
            S("Risk 1", text="Anyone at the counter can read and copy the ID numbers and use them for identity theft or fraud."),
            S("Risk 2", text="The notebook can be lost or stolen and there is no backup."),
            S("Protection 1", text="Keep the record in a locked drawer, or in a password-protected computer file."),
            S("Protection 2", text="Record only the data really needed and allow only authorised staff to see it."),
        ]),
        H("Common mistakes"),
        MISTAKE("Thinking cybercrime is only hacking", "Online fraud, scams, identity theft, spreading malware and "
                "cyberbullying are also cybercrimes."),
        MISTAKE("Mixing up ANTIC and MINPOSTEL", "MINPOSTEL is the ministry that makes policy. ANTIC is the agency that "
                "regulates ICT activity and handles network and information security."),
        MISTAKE("Thinking it is harmless if you only look", "Entering a system without permission is an offence even "
                "if you do not change or steal anything."),
        QUIZ("Which law deals with cybersecurity and cybercrime in Cameroon?",
             ["Law No. 2010/012", "Law No. 2010/013", "The OHADA Uniform Act", "The Bangui Agreement"], 0,
             "Law No. 2010/012 of 21 December 2010 relates to cybersecurity and cybercrime in Cameroon.",
             feedback=["", "Law No. 2010/013 governs electronic communications in general.",
                       "OHADA Uniform Acts deal with business law.",
                       "The Bangui Agreement set up OAPI and deals with intellectual property."]),
        QUIZ("Which body is the National Agency for Information and Communication Technologies?",
             ["MINPOSTEL", "ANTIC", "OAPI", "ART"], 1,
             "ANTIC stands for the National Agency for Information and Communication Technologies (Agence Nationale des Technologies de l'Information et de la Communication).",
             feedback=["MINPOSTEL is the Ministry of Posts and Telecommunications.", "",
                       "OAPI is the African Intellectual Property Organization.",
                       "ART is the Telecommunications Regulatory Board."]),
        H("Practice questions"),
        PQ("(a) Define cybercrime. (b) Give three examples of cybercrime common in Cameroon.",
           "(a) Cybercrime is an illegal act committed using a computer, phone or network, or targeting them. "
           "(b) Any three of: phishing and mobile money scams; hacking into accounts or systems; identity theft; "
           "spreading viruses or ransomware; cyberbullying; publishing illegal content."),
        PQ("State one role of MINPOSTEL and one role of ANTIC.",
           "MINPOSTEL prepares and carries out government policy on posts, telecommunications and ICT. ANTIC "
           "regulates and promotes ICT activities and is responsible for the security of electronic communication "
           "networks and information systems."),
        PQ("Give four ways a school can protect the personal data of its students.",
           "Any four of: collect only the data needed; use strong passwords and user accounts with limited access; "
           "encrypt or lock away records; make regular backups kept in a safe place; do not share data without "
           "consent or a legal reason; train staff about privacy; delete data that is no longer needed."),
        SUM("Cybercrime is illegal activity using or targeting computers and networks; cybersecurity protects them.",
            "Law No. 2010/012 of 21 December 2010 relates to cybersecurity and cybercrime; Law No. 2010/013 governs electronic communications.",
            "MINPOSTEL makes ICT and telecom policy; ANTIC regulates ICT activity and handles network security.",
            "Common cybercrimes include hacking, phishing and scams, identity theft and spreading malware.",
            "Personal data must be collected only when needed, kept secure and not shared without consent."),
    ],
))


# ---------------------------------------------------------------------------
# Legal, Ethical & Social Aspects / Social and economic impact
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Legal, Ethical & Social Aspects",
    topic="Social and economic impact",
    title="The social and economic impact of computers",
    slug="social-economic-impact-of-ict",
    minutes=25,
    summary="Examine the digital divide, automation and job displacement, e-waste and remote collaboration, with examples from Cameroon.",
    objectives=[
        "Define the digital divide and give its causes and possible solutions",
        "Explain how automation creates and removes jobs",
        "Describe the dangers of e-waste and how to manage it",
        "Give advantages and disadvantages of remote collaboration",
        "Write balanced answers that weigh benefits against problems",
    ],
    key_concepts=["Digital divide", "Automation", "Job displacement", "E-waste", "Remote collaboration", "Teleworking"],
    blocks=[
        H("Introduction"),
        T("In a city like Yaoundé, a student can follow online classes on a phone with 4G. In a village far from a "
          "main road, there may be no electricity at night and the network may drop every few minutes. At the same "
          "time, banks in Douala use machines and apps that do work once done by cashiers, and old phones and "
          "computers pile up in dumps.\n\n"
          "Computers change how people live, work and earn money, for better and for worse. GCE questions often ask "
          "you to discuss both sides."),
        H("The digital divide"),
        D("The **digital divide** is the gap between people who have good access to computers, the internet and "
          "the skills to use them, and people who do not.", title="Definition"),
        KEY("Causes of the digital divide", "The gap can be between regions, between rich and poor, or between generations.",
            cards=[["Infrastructure", "Weak electricity supply and poor network coverage in rural areas."],
                   ["Cost", "Devices and data bundles are expensive compared with many incomes."],
                   ["Skills", "Many people have never been trained to use computers."],
                   ["Language and content", "Little useful content exists in local languages."]]),
        T("Ways to reduce the divide include extending electricity and network coverage, community or school "
          "computer centres and telecentres, cheaper devices and data, solar power, and ICT training in schools."),
        H("Automation and jobs"),
        D("**Automation** is the use of computers and machines to do tasks with little or no human help. **Job "
          "displacement** happens when workers lose their jobs because a machine or program now does that work.",
          title="Definitions"),
        KEY("Jobs lost and jobs created", "Automation removes some jobs but creates others.",
            cards=[["Jobs reduced", "Routine work: typists, some bank cashiers, filing clerks, some factory workers."],
                   ["Jobs created", "Programmers, network technicians, web designers, phone repairers, mobile money agents, data analysts."]],
            note="Workers whose jobs are automated need retraining to move into the new jobs."),
        H("E-waste"),
        D("**E-waste** (electronic waste) is thrown-away electrical and electronic equipment such as old phones, "
          "computers, batteries and screens.", title="Definition"),
        T("E-waste contains harmful substances such as lead, mercury and cadmium. When it is burnt or dumped in the "
          "open, these poison the soil, water and air and damage the health of people who handle it. It also "
          "contains valuable metals that are lost if it is not recycled. Good practice is to repair and reuse "
          "devices, donate working ones, and take dead ones to proper collection and recycling points."),
        H("Remote collaboration"),
        D("**Remote collaboration** means people working together from different places using ICT tools such as "
          "email, video calls, shared documents and messaging apps. **Teleworking** is doing your job from home or "
          "another place away from the office using these tools.", title="Definition"),
        EX("Worked example 1: a balanced answer on teleworking", intro=(
            "A company in Douala lets its accountants work from home three days a week. Give two advantages and two "
            "disadvantages of this for the workers."), steps=[
            S("Advantage 1", text="Less time and money spent travelling in traffic, for example on taxis or bikes."),
            S("Advantage 2", text="More flexible hours, so it is easier to balance work and family."),
            S("Disadvantage 1", text="Power cuts and weak internet at home can stop work."),
            S("Disadvantage 2", text="Isolation from colleagues and difficulty separating work time from home time."),
        ]),
        EX("Worked example 2: reducing the digital divide", intro=(
            "Suggest three measures the government or a community could take so that students in a rural "
            "secondary school can use computers, and explain how each helps."), steps=[
            S("Power", text="Install solar panels, because many villages lack reliable electricity."),
            S("Access", text="Equip a school computer lab or community telecentre, because most families cannot buy computers."),
            S("Offline content", text="Provide lessons and resources that work offline, because the internet connection is weak or costly."),
        ]),
        H("Common mistakes"),
        MISTAKE("Giving only one side", "When asked to discuss or evaluate, give both benefits and problems. One-sided "
                "answers lose marks."),
        MISTAKE("Vague answers such as it is bad for the environment", "Be specific: e-waste releases toxic metals "
                "like lead and mercury into soil and water when burnt or dumped."),
        MISTAKE("Saying computers only destroy jobs", "Automation also creates new jobs. Say which jobs are lost and "
                "which are created."),
        QUIZ("Which of these is the best example of the digital divide?",
             ["A student types faster than his friend",
              "Urban students have 4G internet while many rural students have no connection",
              "A company buys a new printer",
              "A virus deletes files on a school computer"], 1,
             "The digital divide is unequal access to ICT and the skills to use it, often between urban and rural areas.",
             feedback=["Typing speed is a personal skill difference, not a gap in access between groups.", "",
                       "Buying equipment is not a gap between groups of people.",
                       "That is a security problem, not the digital divide."]),
        H("Practice questions"),
        PQ("(a) What is e-waste? (b) Give two dangers of e-waste and two ways of managing it.",
           "(a) E-waste is discarded electrical and electronic equipment such as phones, computers and batteries. "
           "(b) Dangers: toxic metals such as lead and mercury pollute soil and water; burning it releases poisonous "
           "smoke that harms health. Management: repair and reuse or donate devices; take dead devices to proper "
           "recycling or collection points instead of burning or dumping them."),
        PQ("Explain, with examples, how automation can lead to both job losses and job creation.",
           "Job losses: machines and software take over routine tasks, for example cash machines and mobile banking "
           "reduce the need for bank cashiers. Job creation: new technology needs people to build, run and repair it, "
           "for example programmers, network technicians, phone repairers and mobile money agents."),
        PQ("State three causes of the digital divide in Cameroon.",
           "Any three of: poor electricity supply in rural areas; weak or missing network coverage; high cost of "
           "devices and data compared with incomes; lack of ICT skills and training; little content in local languages."),
        PQ("Give two advantages of remote collaboration for a group of students preparing a project from different towns.",
           "Any two of: they can share and edit the same document without travelling; they save transport money and "
           "time; they can communicate at any time by messaging or video call; work is saved online so it is not lost "
           "if one computer fails."),
        SUM("The digital divide is the gap in ICT access and skills; causes include cost, power, network and training.",
            "Automation replaces some routine jobs but creates new ICT jobs; retraining is needed.",
            "E-waste contains toxic substances and should be reused, repaired or recycled, never burnt.",
            "Remote collaboration and teleworking save travel but depend on power and internet.",
            "In discussion questions, always give both advantages and disadvantages with specific examples."),
    ],
))
