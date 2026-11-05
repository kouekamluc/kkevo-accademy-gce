"""Form 5 Computer Science: Web Design & Publishing (HTML5 structure, CSS styling), one focused lesson at a time."""

from .dsl import *  # noqa: F403

COURSE = ("computer-science", "form-5")

MODULE = "Web Design & Publishing"
HTML = "HTML5 structure"
CSS = "CSS styling"

LESSONS = []

# ============================================================== 1. The structure of an HTML5 page
LESSONS.append(lesson(
    module=MODULE, topic=HTML,
    title="The structure of an HTML5 page",
    slug="html5-structure-first-web-page",
    minutes=20,
    summary="Learn what HTML is and write your first complete page: the doctype, html, head, title and body, with correct nesting, saved as an .html file and opened in a browser.",
    objectives=[
        "Explain what HTML is and what a tag, an element and an attribute are",
        "Write the skeleton of an HTML5 page starting with the doctype",
        "Say what belongs in the head and what belongs in the body",
        "Nest elements correctly and indent code so it is easy to read",
        "Save a page as an .html file and open it in a browser",
    ],
    key_concepts=["HTML", "Tag", "Element", "Attribute", "Doctype", "Head and body", "Nesting"],
    blocks=[
        H("Introduction"),
        T('''Your school in Limbe wants a website. Before anything is shown on a screen, someone must write a text file that tells the browser what the page contains: a title, a welcome message, a list of classes.

That file is written in **HTML**. Every web page you have ever opened on your phone, from a school site to a news site, started as an HTML file. In this lesson you write your first one.'''),
        T('''You do not need special software. A plain text editor and a web browser are enough. On a phone, any text-editor app and the browser work too.'''),
        H("What HTML is"),
        D('''**HTML** (HyperText Markup Language) is a language that describes the **structure** of a web page. It marks parts of the text as a heading, a paragraph, a list, a link or an image. The browser reads the marks and displays the page.''',
          title="Definition",
          note="HTML is a markup language, not a programming language. It has no calculations, loops or decisions. It only says what each part of the page is."),
        T('''The marks are called **tags**. A tag is a word inside angle brackets, such as <p>. HTML5 is the current version of the language.'''),
        H("Tags, elements and attributes"),
        KEY("The parts of an element", "Most elements are built from three things.", cards=[
            ["Opening tag", "<p> starts the element."],
            ["Content", "The text (or other elements) between the tags."],
            ["Closing tag", "</p> ends the element. It has a forward slash."],
        ], note="An **element** is the whole thing: opening tag, content and closing tag together."),
        CODE('''<p>Welcome to our school.</p>''', "html", title="Listing 1: one element",
             caption="The browser shows the words Welcome to our school. as one paragraph. The tags themselves are not shown."),
        T('''An **attribute** gives extra information about an element. It is written inside the opening tag as a name, an equals sign and a value in quotation marks.'''),
        CODE('''<p lang="en">Welcome to our school.</p>''', "html", title="Listing 2: an element with an attribute",
             caption="The attribute name is lang and its value is en (English). The page looks the same; the attribute helps browsers and screen readers."),
        T('''A few elements are **empty**. They have no content, so they have no closing tag. Examples are <br> (a line break) and <img> (an image).'''),
        H("The skeleton of an HTML5 page"),
        T('''Every HTML5 page has the same skeleton. First comes the **doctype** line, which tells the browser that the page uses HTML5. Then comes the <html> element, which holds everything else. Inside it are two parts.

The <head> holds information **about** the page. The <body> holds everything the visitor **sees** on the page.'''),
        CODE('''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>GBHS Limbe</title>
  </head>
  <body>
    <h1>Welcome to GBHS Limbe</h1>
    <p>We are a government bilingual high school.</p>
  </body>
</html>''', "html", title="Listing 3: a complete HTML5 page",
             caption="The browser tab shows GBHS Limbe. The page area shows a large heading, then one paragraph of text."),
        KEY("What each part does", "Read the page from top to bottom.", cards=[
            ["<!DOCTYPE html>", "Says the page is HTML5. It is not a tag and has no closing part."],
            ["<html>", "The root element. Everything else is inside it."],
            ["<head>", "Information about the page. Nothing in it appears in the page area."],
            ["<meta charset>", "Sets the character set so letters such as é and ç display correctly."],
            ["<title>", "The page name shown on the browser tab and in search results."],
            ["<body>", "All the visible content: headings, text, images, links."],
        ]),
        IMG("f5c-html-document-tree.svg",
            alt="A tree diagram. The html element at the top has two children, head and body. Head contains meta and title. Body contains h1, p and ul. Title, h1 and p each contain text.",
            caption="Figure 1. The HTML document tree for a small page. Each element sits inside its parent."),
        H("Nesting and indentation"),
        D('''**Nesting** means putting one element inside another. The inner element must be closed before the outer one. The last tag opened is the first tag closed.''',
          title="Definition", note="Think of boxes: a small box must be fully inside a bigger box, never half in and half out."),
        CODE('''<!-- Wrong: the tags cross over -->
<p>Our <strong>best</p> students</strong>

<!-- Right: strong is closed before p -->
<p>Our <strong>best</strong> students</p>''', "html", title="Listing 4: crossed tags and correct nesting",
             caption="The text between the markers <!-- and --> is a comment. The browser ignores it."),
        T('''**Indentation** means starting inner lines a little further to the right, usually two spaces. The browser does not need it, but people do. With indentation you can see the tree at a glance and spot a missing closing tag quickly.'''),
        H("Saving and opening your page"),
        T('''Follow these steps to see your page.

First, type the code in a plain text editor (Notepad on a computer, any text-editor app on a phone). Do not use a word processor such as Microsoft Word, because it adds hidden formatting.

Second, save the file with a name that ends in **.html**, for example index.html. On Windows, set "Save as type" to "All files", otherwise the file is saved as index.html.txt and will not work.

Third, open the file in a browser: double-click it, or open the browser and choose the file. To change the page, edit the text, save again and **refresh** the browser tab.'''),
        TIP('''Use only lowercase letters and no spaces in file names, for example school-home.html. Many web servers treat Index.html and index.html as different files. A page called index.html is normally the one shown first on a website.'''),
        EX("Worked example 1: read a page", intro='''Look at Listing 3. (a) What does the browser show on its tab? (b) Name the child elements of body. (c) Where would you put the meta charset line, and why?''', steps=[
            S("Find the title", text="The <title> element holds GBHS Limbe, so the tab shows GBHS Limbe."),
            S("Find the children of body", text="The elements directly inside <body> are <h1> and <p>."),
            S("Place the meta line", text="It goes in <head>, because it is information about the page and is not shown to the visitor."),
        ]),
        EX("Worked example 2: write a page", intro='''A cyber cafe in Buea needs a simple page. The tab must say Buea Net Cafe. The page must show the heading Buea Net Cafe and a paragraph: Open every day from 8 am to 10 pm.''', steps=[
            S("Start with the skeleton", text="Write the doctype, then <html>, <head> and <body>."),
            S("Fill the head", text="Add <meta charset=\"UTF-8\"> and <title>Buea Net Cafe</title>."),
            S("Fill the body", text="Add <h1>Buea Net Cafe</h1> and the paragraph in <p> tags."),
            S("Close and indent", text="Close <body> and <html>. Indent the inner lines. Save as index.html and open in a browser."),
        ]),
        CODE('''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Buea Net Cafe</title>
  </head>
  <body>
    <h1>Buea Net Cafe</h1>
    <p>Open every day from 8 am to 10 pm.</p>
  </body>
</html>''', "html", title="Listing 5: answer to worked example 2",
             caption="The browser tab shows Buea Net Cafe. The page shows a large heading and one line of text."),
        H("Common mistakes"),
        MISTAKE("Putting visible content in the head", "Headings, paragraphs and images belong in the body. The head holds the title and other information about the page."),
        MISTAKE("Closing tags in the wrong order", "Close the inner element first. <p><strong>Hi</p></strong> is wrong; <p><strong>Hi</strong></p> is right."),
        MISTAKE("Saving as .txt or typing the doctype wrongly", "If the file ends in .txt, the browser shows your code as plain text instead of a page. Make sure the name ends in .html and the first line is <!DOCTYPE html>."),
        QUIZ("Which element holds the text that appears on the browser tab?", ["<head>", "<title>", "<h1>", "<body>"], 1,
             "The <title> element, which sits inside <head>, gives the page its name on the tab.",
             hint="It is a small element inside the head.",
             feedback=["<head> holds the title but is not the title itself.", "", "<h1> is a heading shown inside the page area, not on the tab.", "<body> holds the visible page content, not the tab name."]),
        QUIZ("Which line is correctly nested?", ["<p><em>Hello</p></em>", "<p><em>Hello</em></p>", "<em><p>Hello</em></p>", "</p><em>Hello</em><p>"], 1,
             "The em element is closed before the p element that contains it.",
             hint="The last element opened must be the first one closed.",
             feedback=["The tags cross: p closes before em.", "", "The tags cross: em closes before p, which was opened second.", "The closing tag comes before the opening tag."]),
        H("Practice questions"),
        PQ("State two differences between the head and the body of an HTML page.",
           "The head holds information about the page (title, character set, links to style sheets) and none of it appears in the page area. The body holds the content the visitor sees (headings, text, images, links)."),
        PQ("Explain the difference between a tag and an element, using the paragraph tag as your example.",
           "A tag is only the marker in angle brackets, for example <p> or </p>. An element is the complete unit: the opening tag, the content and the closing tag, for example <p>Hello</p>."),
        PQ("A student saves her page as home.html.txt and double-clicks it. The browser shows all the tags as text. Give the cause and the fix.",
           "The file ends in .txt, so it is opened as plain text, not as an HTML page. Rename or save it again with a name ending in .html (on Windows choose Save as type: All files)."),
        PQ("Write the HTML for a complete page whose tab says My Class, with the heading Form 5 Science and the paragraph Welcome back.",
           "<!DOCTYPE html>, then <html><head><meta charset=\"UTF-8\"><title>My Class</title></head><body><h1>Form 5 Science</h1><p>Welcome back</p></body></html>. The title goes in the head and the heading and paragraph go in the body."),
        SUM("HTML describes the structure of a page using tags; the browser reads them and displays the page.",
            "An element is an opening tag, content and a closing tag. Attributes add information inside the opening tag.",
            "Every page starts with the doctype, then html containing head (about the page) and body (what is seen).",
            "Nest elements correctly: close the inner element first. Indent to show the tree.",
            "Save as .html in a plain text editor, open it in a browser and refresh after each change."),
    ],
))

# ============================================================== 2. Text, links and images
LESSONS.append(lesson(
    module=MODULE, topic=HTML,
    title="Text, links and images",
    slug="html5-text-links-images",
    minutes=22,
    summary="Format page content with headings, paragraphs, strong and em, lists, hyperlinks and images, and understand absolute and relative addresses and the alt attribute.",
    objectives=[
        "Use headings, paragraphs, line breaks, strong and em correctly",
        "Build ordered and unordered lists",
        "Write hyperlinks with absolute and relative addresses",
        "Add images using src and alt, and explain why alt matters",
    ],
    key_concepts=["Headings", "Paragraph", "Strong and em", "Lists", "Hyperlink", "Relative and absolute address", "Alt text"],
    blocks=[
        H("Introduction"),
        T('''In the previous lesson you built the skeleton of a page. Now you fill the body with real content.

Imagine the home page of a library in Bamenda. It needs a main heading, some paragraphs, a list of opening days, a link to another page and a photo of the building. Each of these has its own element.'''),
        H("Headings and paragraphs"),
        T('''HTML has six levels of heading, from <h1> (most important, largest) to <h6> (least important, smallest). Use <h1> once for the page title, then <h2> for main sections and <h3> for parts of a section.

Choose a heading level for its **meaning**, not for its size. Size can be changed later with CSS.

A paragraph is written with <p>. The browser puts space above and below each paragraph. Extra spaces and blank lines in your code are ignored: the browser joins them into one space.'''),
        T('''To break a line without starting a new paragraph, use <br>. It is an empty element. For a horizontal line use <hr>, also empty.'''),
        CODE('''<h1>Bamenda Community Library</h1>
<p>Welcome to the library.<br>
We lend books to every student.</p>
<h2>Opening hours</h2>''', "html", title="Listing 1: headings, paragraph and line break",
             caption="The browser shows a large heading, a paragraph on two lines, then a smaller heading."),
        H("Emphasis: strong and em"),
        D('''<strong> marks text as **strongly important**. Browsers show it in bold. <em> marks text as **emphasised**, as if you stressed it when speaking. Browsers show it in italics.''',
          title="Definition",
          note="Choose them for meaning. Older pages used <b> and <i> only for looks. In this course, use strong and em."),
        CODE('''<p>The library is <strong>closed on Sundays</strong>.
Please return books <em>on time</em>.</p>''', "html", title="Listing 2: strong and em",
             caption="The browser shows closed on Sundays in bold and on time in italics."),
        H("Lists"),
        T('''Use a list when items belong together. An **unordered list** <ul> shows bullets. An **ordered list** <ol> shows numbers, so use it when the order matters, such as steps. In both, each item is an <li> (list item) inside the list.'''),
        CODE('''<h2>Opening days</h2>
<ul>
  <li>Monday to Friday</li>
  <li>Saturday morning</li>
</ul>

<h2>How to borrow a book</h2>
<ol>
  <li>Show your library card</li>
  <li>Choose a book</li>
  <li>Sign the register</li>
</ol>''', "html", title="Listing 3: an unordered and an ordered list",
             caption="The first list shows two bullets. The second shows items numbered 1, 2 and 3."),
        TIP('''Only <li> elements may sit directly inside <ul> or <ol>. A list can also be nested: put a whole <ul> inside an <li> to make a sub-list.'''),
        H("Hyperlinks"),
        T('''A **hyperlink** takes the visitor to another page or file when clicked. It uses the anchor element <a>. The **href** attribute holds the address (the destination). The text between the tags is what the visitor clicks.'''),
        CODE('''<a href="https://www.example.com">Visit our partner</a>''', "html", title="Listing 4: a hyperlink",
             caption="The browser shows Visit our partner as underlined blue text. Clicking it opens the address."),
        D('''An **absolute address** is the full address, starting with https://, and works from any page. A **relative address** gives only the file name or path from the current page, such as contact.html. It works only for files on the same website.''',
          title="Absolute and relative addresses"),
        CODE('''<!-- absolute: a page on another website -->
<a href="https://www.example.com/news.html">News</a>

<!-- relative: a file in the same folder as this page -->
<a href="contact.html">Contact us</a>

<!-- relative: a file inside a folder called photos -->
<a href="photos/gallery.html">Photos</a>''', "html", title="Listing 5: absolute and relative links",
             caption="All three look like normal links. They differ in where the browser looks for the destination."),
        T('''Use relative links between pages of your own site. The site then still works if you move it to a new server or open it from a flash drive.'''),
        H("Images and alt text"),
        T('''An image uses the empty element <img>. Two attributes are needed. **src** (source) gives the file name or address of the picture. **alt** (alternative text) describes the picture in words.

Why does alt matter? A blind visitor using a screen reader hears the alt text. If the connection is slow or the file is missing, the browser shows the alt text instead of the picture. Search engines also read it.'''),
        CODE('''<img src="photos/library.jpg" alt="Front of Bamenda Community Library" width="300">''', "html", title="Listing 6: an image",
             caption="The browser shows the picture 300 pixels wide. If the file cannot load, it shows the alt text."),
        TIP('''Large photos use a lot of mobile data. Resize pictures before putting them on a page and use a small width for phone visitors.'''),
        EX("Worked example 1: a news item", intro='''Write the HTML for: a level 2 heading Library News; a paragraph with the word closed in strong; and a link with the text Contact us that opens the file contact.html in the same folder.''', steps=[
            S("The heading", text="Use <h2>Library News</h2>."),
            S("The paragraph", text="<p>The library is <strong>closed</strong> on Monday.</p>"),
            S("The link", text="The file is in the same folder, so a relative address is enough: <a href=\"contact.html\">Contact us</a>."),
            S("Check", text="Every opening tag has a matching closing tag, and the inner elements close first."),
        ]),
        EX("Worked example 2: a photo and a list", intro='''Show the picture hall.jpg, described as Reading hall, 250 pixels wide, then an ordered list with the steps Enter, Sit, Read.''', steps=[
            S("The image", text="<img src=\"hall.jpg\" alt=\"Reading hall\" width=\"250\"> uses both src and alt and has no closing tag."),
            S("The list", text="Steps have an order, so use <ol> with three <li> items."),
            S("Result", text="The browser shows the picture, then the numbers 1 to 3 with the words Enter, Sit and Read."),
        ]),
        CODE('''<img src="hall.jpg" alt="Reading hall" width="250">
<ol>
  <li>Enter</li>
  <li>Sit</li>
  <li>Read</li>
</ol>''', "html", title="Listing 7: answer to worked example 2"),
        H("Common mistakes"),
        MISTAKE("Leaving out alt", "An image without alt is not accessible to blind visitors and shows nothing useful when the image fails to load. Always write a short, meaningful alt."),
        MISTAKE("Using a heading to make text big", "Use headings for page structure. If you only want larger text, use CSS (a later lesson)."),
        MISTAKE("Typing the address in the wrong attribute", "In a link the address goes in href. In an image it goes in src. The attribute names are not interchangeable."),
        QUIZ("Which code makes a numbered list of two items?", [
            "<ul><li>Read</li><li>Write</li></ul>", "<ol><li>Read</li><li>Write</li></ol>", "<ol>Read<br>Write</ol>", "<list>Read Write</list>"], 1,
             "<ol> makes an ordered (numbered) list and each item is wrapped in <li>.",
             hint="Which letters stand for ordered?",
             feedback=["<ul> gives bullets, not numbers.", "", "Items must be in <li> elements; line breaks do not make a list.", "There is no <list> element in HTML."]),
        QUIZ("What is the main purpose of the alt attribute?", [
            "To make the image load faster", "To set the size of the image", "To describe the image for visitors who cannot see it", "To link the image to another page"], 2,
             "alt gives a text description used by screen readers and shown when the image cannot load.",
             hint="Think of a blind visitor or a very slow connection.",
             feedback=["alt does not change loading speed.", "Size is set with width and height.", "", "Linking uses an <a> element around the image."]),
        H("Practice questions"),
        PQ("Distinguish between the strong and em elements and say how a browser normally displays each.",
           "strong marks text as strongly important and is normally shown in bold. em marks text that is emphasised and is normally shown in italics."),
        PQ("Explain the difference between an absolute and a relative address in a hyperlink, with one example of each.",
           "An absolute address is complete and starts with https://, for example https://www.example.com/news.html; it works from any page. A relative address gives only the path from the current page, for example contact.html; it works only inside the same website."),
        PQ("An image on a school page does not load because the phone has no signal. Explain why the alt attribute is still useful here.",
           "The browser shows the alt text in place of the picture, so the visitor still knows what the image was. Screen readers also read the alt text to blind visitors."),
        PQ("Write HTML for a link with the text Past papers that opens the file papers.html in the same folder, inside a paragraph.",
           "<p><a href=\"papers.html\">Past papers</a></p>. The file name is a relative address in href; the words between the a tags are the clickable text."),
        SUM("Use h1 to h6 for headings by meaning, p for paragraphs, br for a line break.",
            "strong marks important text (bold) and em marks emphasis (italics).",
            "ul makes bulleted lists, ol makes numbered lists, and each item is an li.",
            "A hyperlink is an a element with an href address; relative addresses suit pages on the same site.",
            "An image needs src and alt. The alt text helps blind visitors and shows when the image fails to load."),
    ],
))

# ============================================================== 3. HTML tables
LESSONS.append(lesson(
    module=MODULE, topic=HTML,
    title="HTML tables",
    slug="html5-tables-rows-cells-spans",
    minutes=20,
    summary="Build tables with table, tr, th and td, add a caption, and use rowspan and colspan to merge cells in a timetable or price list.",
    objectives=[
        "Build a table row by row with table, tr, th and td",
        "Add a caption and a border to a table",
        "Merge cells across columns with colspan and across rows with rowspan",
        "Check that every row has the right number of cells",
    ],
    key_concepts=["Table", "Row", "Heading cell", "Data cell", "Caption", "colspan", "rowspan"],
    blocks=[
        H("Introduction"),
        T('''A school timetable, an exam list and the prices at a cyber cafe all have something in common: they are information arranged in rows and columns. In HTML this is done with a **table**.

In the previous lesson you placed text, lists, links and images one after another. A table puts data in a grid so the eye can compare values quickly. In this lesson you build tables and learn to merge cells.'''),
        H("Building a table row by row"),
        T('''A table is written **row by row**, not column by column. You never write a column. The columns appear because each row has its cells in the same order.'''),
        KEY("The table elements", "Four elements make a basic table.", cards=[
            ["<table>", "Holds the whole table."],
            ["<tr>", "Table row. One <tr> for each row."],
            ["<th>", "Table heading cell. Bold and centred by default."],
            ["<td>", "Table data cell. An ordinary cell with content."],
        ], note="<th> and <td> always go inside a <tr>, and <tr> always goes inside <table>."),
        CODE('''<table border="1">
  <tr>
    <th>Service</th>
    <th>Price (FCFA)</th>
  </tr>
  <tr>
    <td>Printing one page</td>
    <td>50</td>
  </tr>
  <tr>
    <td>One hour of internet</td>
    <td>300</td>
  </tr>
</table>''', "html", title="Listing 1: a price list",
             caption="The browser shows a grid with 3 rows and 2 columns. The first row has bold, centred headings. The border attribute draws thin lines around every cell."),
        T('''The attribute border="1" gives the table visible lines. Without it the table has no lines. Later, in the CSS lessons, you will draw borders with CSS, which is the modern way.'''),
        H("The caption"),
        D('''The <caption> element gives a table a title. It is placed straight after the opening <table> tag and is shown above the table. It also helps screen readers announce what the table is about.''', title="Definition"),
        CODE('''<table border="1">
  <caption>Cyber cafe prices</caption>
  <tr><th>Service</th><th>Price (FCFA)</th></tr>
  <tr><td>Printing one page</td><td>50</td></tr>
</table>''', "html", title="Listing 2: a table with a caption",
             caption="The words Cyber cafe prices appear above the grid."),
        TIP('''When a row is short, you may write all its cells on one line, as in Listing 2. The browser does not care. Choose the layout that you can read most easily.'''),
        H("Merging cells: colspan and rowspan"),
        T('''Sometimes one cell must be wider or taller than the others. Two attributes do this.

**colspan** makes a cell stretch across several **columns**. The value is the number of columns it covers.

**rowspan** makes a cell stretch down several **rows**. The value is the number of rows it covers.'''),
        D('''When a cell spans more than one column or row, you write **fewer cells** in the rows it covers. Each row, counting the spaces taken by spans, must fill the same number of columns.''',
          title="The counting rule",
          note="Row total = number of cells + extra columns from colspan + cells above that are held by a rowspan."),
        CODE('''<table border="1">
  <caption>Form 5 timetable</caption>
  <tr><th>Time</th><th>Monday</th><th>Tuesday</th></tr>
  <tr><td>8:00</td><td>Maths</td><td>English</td></tr>
  <tr><td>9:00</td><td colspan="2">Assembly</td></tr>
  <tr><td>10:00</td><td rowspan="2">Computer lab</td><td>Biology</td></tr>
  <tr><td>11:00</td><td>Chemistry</td></tr>
</table>''', "html", title="Listing 3: a timetable with colspan and rowspan",
             caption="The browser shows 3 columns. Assembly stretches across Monday and Tuesday at 9:00. Computer lab is one tall cell on Monday that covers 10:00 and 11:00."),
        T('''Check the counting rule in Listing 3. The 9:00 row has the Time cell plus one cell that spans 2 columns, so it fills 1 + 2 = 3 columns. The 11:00 row has only two cells, but the third column is already taken by Computer lab from the row above.'''),
        EX("Worked example 1: write a simple table", intro='''Write a table with a caption Exam dates, headings Subject and Date, and one row: Physics, 4 June.''', steps=[
            S("Start the table", text="Write <table border=\"1\"> and, straight after it, <caption>Exam dates</caption>."),
            S("Heading row", text="Add a <tr> containing <th>Subject</th> and <th>Date</th>."),
            S("Data row", text="Add a <tr> containing <td>Physics</td> and <td>4 June</td>."),
            S("Close", text="Write </table>. The browser shows 2 rows and 2 columns."),
        ]),
        CODE('''<table border="1">
  <caption>Exam dates</caption>
  <tr><th>Subject</th><th>Date</th></tr>
  <tr><td>Physics</td><td>4 June</td></tr>
</table>''', "html", title="Listing 4: answer to worked example 1"),
        EX("Worked example 2: merge cells", intro='''A shop in Douala shows this price list. The heading Drinks must stretch across both columns. Under it, two rows give Water 300 and Juice 500.''', steps=[
            S("Count the columns", text="The table has 2 columns: item and price."),
            S("Heading that spans", text="Use one <th colspan=\"2\">Drinks</th>. It fills the whole row, so no other cell is needed in this row."),
            S("Data rows", text="Each remaining row has 2 cells: the name and the price."),
            S("Check", text="Row 1: one cell covering 2 columns, total 2. Rows 2 and 3: two cells, total 2. All rows fill 2 columns."),
        ]),
        CODE('''<table border="1">
  <tr><th colspan="2">Drinks</th></tr>
  <tr><td>Water</td><td>300</td></tr>
  <tr><td>Juice</td><td>500</td></tr>
</table>''', "html", title="Listing 5: answer to worked example 2",
             caption="The browser shows Drinks in one wide heading cell above two rows of two cells."),
        H("Common mistakes"),
        MISTAKE("Wrong number of cells in a row", "After a colspan or rowspan, count carefully. If a row has too many or too few cells, the table looks broken."),
        MISTAKE("Using td or th outside a row", "Cells must be inside a tr. Write the row first, then the cells."),
        MISTAKE("Using a table for page layout", "A table is for data in rows and columns, such as a timetable. Do not use one just to position text and pictures. CSS is used for layout."),
        QUIZ("A table has 3 columns. A row contains one cell with colspan 2 and one ordinary cell. How many columns does the row fill?", ["2", "3", "4", "5"], 1,
             "The spanning cell covers 2 columns and the other cell covers 1, so 2 + 1 = 3.",
             hint="Add the columns covered by each cell.",
             feedback=["That counts the two cells, but the spanning cell covers two columns on its own.", "", "An ordinary cell covers one column, not two, so the total is 2 + 1.", "You added the table width (3) to the span (2). The row only has to fill the 3 columns."]),
        QUIZ("Which element gives a table a title that is shown above it?", ["<title>", "<th>", "<caption>", "<head>"], 2,
             "<caption> goes straight after <table> and displays above the table.",
             hint="Look at the word for a short text under or over a picture.",
             feedback=["<title> sets the tab name in the head, not a table title.", "<th> is a heading cell inside a row, not a title for the whole table.", "", "<head> holds page information, not a table title."]),
        H("Practice questions"),
        PQ("State the purpose of each of these elements: (a) <tr> (b) <th> (c) <td>.",
           "(a) <tr> creates a table row. (b) <th> creates a heading cell, shown bold and centred by default. (c) <td> creates an ordinary data cell."),
        PQ("Explain what colspan=\"3\" does to a cell.",
           "It makes the cell stretch across three columns, so the row needs correspondingly fewer cells."),
        PQ("A table has 4 columns. One row begins with a cell using rowspan=\"2\". Explain how many cells the row immediately below it needs to fill the table.",
           "The cell above takes up one column in the next row too, so the next row needs only 3 cells to fill the remaining 3 columns."),
        PQ("Write the HTML for a table with a border and two columns. The first row has headings Class and Teacher. The second row has Form 5 and Mr Tabi.",
           "<table border=\"1\"><tr><th>Class</th><th>Teacher</th></tr><tr><td>Form 5</td><td>Mr Tabi</td></tr></table>. Every cell is inside a tr, and the headings use th."),
        SUM("A table is built row by row: table holds tr rows, and each row holds th or td cells.",
            "th is a heading cell (bold, centred) and td is a data cell.",
            "caption gives the table a title above it. border=\"1\" draws simple lines.",
            "colspan merges cells across columns and rowspan merges them down rows.",
            "After merging, write fewer cells and check that every row fills the same number of columns."),
    ],
))

# ============================================================== 4. HTML forms
LESSONS.append(lesson(
    module=MODULE, topic=HTML,
    title="HTML forms",
    slug="html5-forms-input-controls",
    minutes=25,
    summary="Build a registration or order form with form, input types, labels, select, textarea and a submit button, and understand name, value, action and method.",
    objectives=[
        "Build a form with text, password, radio, checkbox and submit controls",
        "Link a label to its control and use select and textarea",
        "Explain the roles of name and value in the data a form sends",
        "Describe action and method in simple terms and choose get or post",
    ],
    key_concepts=["Form", "Input type", "Label", "Select and textarea", "name and value", "action and method"],
    blocks=[
        H("Introduction"),
        T('''Some websites only show information. Others collect it: a school registration page, a cyber cafe booking page or an online shop order page. They use an HTML **form**.

In the previous lesson you displayed data in a table. A form works the other way. The visitor types or chooses data, and the page sends it to a server. In this lesson you build the form. Processing the data needs a program on the server, which is outside this lesson.'''),
        H("The form element and the input element"),
        D('''A **form** is a part of a page that collects data from the visitor and sends it to a server. The <form> element contains the controls (boxes, buttons and choices) that the visitor uses.''', title="Definition"),
        T('''Most controls are made with the empty element <input>. Its **type** attribute decides what the control looks like.'''),
        KEY("Common input types", "The same element makes many controls.", cards=[
            ["text", "A one-line box for typing, such as a name."],
            ["password", "Like text, but the characters appear as dots."],
            ["radio", "A round button. The visitor picks only one from a group."],
            ["checkbox", "A square box. The visitor can tick none, one or several."],
            ["submit", "A button that sends the form."],
        ]),
        H("Labels, name and value"),
        T('''A **label** tells the visitor what a control is for. Link it to the control: give the control an **id**, and give the label a **for** attribute with the same text. Now clicking the label also selects the control, which is easier on a phone and helps screen readers.

The **name** attribute names the data. When the form is sent, each control's data goes with its name. The **value** is the data itself. For a text box the value is what the visitor typed. For a radio button or checkbox the value is written in the HTML.'''),
        CODE('''<form action="register.php" method="post">
  <label for="fullname">Full name:</label>
  <input type="text" id="fullname" name="fullname">

  <label for="pass">Password:</label>
  <input type="password" id="pass" name="pass">

  <input type="submit" value="Register">
</form>''', "html", title="Listing 1: a small registration form",
             caption="The browser shows two labelled boxes (the password box shows dots) and a button marked Register."),
        T('''If the visitor types Ngu and 4567, the form sends the pairs fullname=Ngu and pass=4567 to the server. Each pair is a name and a value.'''),
        H("Radio buttons and checkboxes"),
        T('''Radio buttons that belong together **must share the same name**. This makes them a group in which only one can be chosen. Each button has a different value. Checkboxes are used when more than one choice is allowed.'''),
        CODE('''<p>Service:</p>
<input type="radio" id="print" name="service" value="printing">
<label for="print">Printing</label>
<input type="radio" id="browse" name="service" value="browsing">
<label for="browse">Browsing</label>

<p>Extras:</p>
<input type="checkbox" id="scan" name="extra" value="scanning">
<label for="scan">Scanning</label>
<input type="checkbox" id="copy" name="extra" value="copying">
<label for="copy">Copying</label>''', "html", title="Listing 2: radio buttons and checkboxes",
             caption="The browser shows two round buttons, where ticking one clears the other, and two square boxes that can both be ticked."),
        H("Select and textarea"),
        T('''A **select** element makes a drop-down list. Each choice is an <option> inside it. The value of the option is sent when it is chosen. A **textarea** is a box for several lines, such as a message. Unlike input, it has an opening and a closing tag, and its size is set with rows and cols.'''),
        CODE('''<label for="town">Town:</label>
<select id="town" name="town">
  <option value="buea">Buea</option>
  <option value="douala">Douala</option>
  <option value="bamenda">Bamenda</option>
</select>

<label for="msg">Message:</label>
<textarea id="msg" name="msg" rows="4" cols="30"></textarea>''', "html", title="Listing 3: select and textarea",
             caption="The browser shows a drop-down list with three towns and a four-line message box."),
        H("Action and method"),
        T('''Two attributes in the opening <form> tag control the sending.

**action** is the address of the program on the server that receives and processes the data. **method** says how the data travels. The two methods are get and post.'''),
        KEY("get and post", "Choose by what you are sending.", cards=[
            ["get", "The data is added to the page address, where everyone can see it. Use it for searches."],
            ["post", "The data is sent inside the request, not shown in the address. Use it for passwords, registrations and orders."],
        ], note="A form on its own cannot save the data. A program on the server (named in action) does that. If you open your own file on your computer and press submit, nothing is saved."),
        EX("Worked example 1: a school registration form", intro='''Write a form that sends data by post to join.php. It asks for the student's name (a text box) and the class (a drop-down list with Form 4 and Form 5), and has a Send button.''', steps=[
            S("The form tag", text="<form action=\"join.php\" method=\"post\"> because passwords or personal data should use post."),
            S("The name box", text="A <label for=\"sname\"> and <input type=\"text\" id=\"sname\" name=\"sname\">."),
            S("The class list", text="A <select id=\"cls\" name=\"cls\"> with two <option> elements, Form 4 and Form 5."),
            S("The button", text="<input type=\"submit\" value=\"Send\"> and finally </form>."),
        ]),
        CODE('''<form action="join.php" method="post">
  <label for="sname">Name:</label>
  <input type="text" id="sname" name="sname">

  <label for="cls">Class:</label>
  <select id="cls" name="cls">
    <option value="form4">Form 4</option>
    <option value="form5">Form 5</option>
  </select>

  <input type="submit" value="Send">
</form>''', "html", title="Listing 4: answer to worked example 1",
             caption="The browser shows a name box, a class drop-down and a Send button."),
        EX("Worked example 2: an order form", intro='''A shop in Douala wants a form with: the customer name, a choice of delivery by radio buttons (Pickup or Delivery), and a tick box to receive an SMS. Which attributes make the radio buttons work as a group, and what is sent if the visitor types Ayuk, chooses Delivery and ticks the box?''', steps=[
            S("Group the radio buttons", text="Both buttons use name=\"delivery\", with values pickup and delivery."),
            S("Add the checkbox", text="<input type=\"checkbox\" name=\"sms\" value=\"yes\">."),
            S("Work out the data sent", text="name=Ayuk, delivery=delivery, sms=yes."),
            S("Check", text="If the checkbox is not ticked, nothing is sent for sms."),
        ]),
        H("Common mistakes"),
        MISTAKE("Different names on radio buttons", "If each radio button has its own name, they are not a group and the visitor can pick all of them. Give them one shared name."),
        MISTAKE("Forgetting the name attribute", "A control without a name sends no data to the server, even if it looks fine on the page."),
        MISTAKE("Using get for passwords", "With get the password appears in the address bar. Use post for private data."),
        QUIZ("Which input type hides the characters the visitor types?", ["text", "hidden", "password", "submit"], 2,
             "type=\"password\" shows the typed characters as dots.",
             hint="It is named after the thing it protects.",
             feedback=["A text box shows exactly what is typed.", "A hidden input is not shown at all and gives the visitor nothing to type in.", "", "submit makes a button; it has no typing area."]),
        QUIZ("Two radio buttons must let the visitor choose only one. What must be true?", [
            "They must have different name attributes", "They must have the same name attribute", "They must be inside a table", "They must use type=\"checkbox\""], 1,
             "Radio buttons with the same name form a group, and only one in the group can be chosen.",
             hint="The browser groups radio buttons by one attribute.",
             feedback=["Different names make separate groups, so both could be chosen.", "", "Tables have nothing to do with grouping.", "Checkboxes allow several choices, which is the opposite of what is wanted."]),
        H("Practice questions"),
        PQ("Give one difference between a radio button and a checkbox.",
           "From a group of radio buttons the visitor can choose only one. With checkboxes the visitor can tick none, one or several."),
        PQ("Explain the roles of the name and value attributes in a form.",
           "The name identifies the data, and the value is the data itself. The form sends them as name and value pairs, for example town=buea."),
        PQ("A school form asks for a password. State which method should be used and give a reason.",
           "post. It sends the data inside the request instead of adding it to the page address, so the password is not shown in the address bar."),
        PQ("Write the HTML for a labelled text box for an email address. The control has the id mail and the name mail.",
           "<label for=\"mail\">Email:</label> <input type=\"text\" id=\"mail\" name=\"mail\">. The for value of the label matches the id of the input."),
        SUM("A form element holds controls and sends their data to a server.",
            "input type decides the control: text, password, radio, checkbox or submit. select with option makes a drop-down, textarea a larger box.",
            "A label with a for attribute matching the control's id links text to its control.",
            "The data is sent as name and value pairs. Radio buttons in a group share one name.",
            "action is where the data goes; method is get (visible in the address) or post (not shown). Use post for private data."),
    ],
))

# ============================================================== 5. Adding CSS
LESSONS.append(lesson(
    module=MODULE, topic=CSS,
    title="Adding CSS: inline, internal and external",
    slug="css-adding-inline-internal-external",
    minutes=20,
    summary="Learn what CSS is, the shape of a CSS rule, and the three ways to add it to a page (inline, internal and external), which one wins in a conflict, and why external CSS is best.",
    objectives=[
        "Explain the purpose of CSS and read a rule: selector, property and value",
        "Add CSS with the style attribute, a style element and a link to a .css file",
        "Decide which rule wins when two rules conflict",
        "Give reasons why external CSS is the best choice for a website",
    ],
    key_concepts=["CSS", "Rule", "Inline CSS", "Internal CSS", "External CSS", "Which rule wins"],
    blocks=[
        H("Introduction"),
        T('''HTML pages without any styling look plain: black text on a white background, in the browser's default font. A school website in Limbe wants its pages to have the school colours and a neat look.

In the HTML lessons you described the **structure** of a page. In this lesson you start to control its **appearance** with CSS.'''),
        D('''**CSS** (Cascading Style Sheets) is a language that describes how HTML elements look: colours, fonts, sizes and spacing. HTML says what each part is. CSS says how it should be displayed.''', title="Definition",
          note="Keeping structure (HTML) and appearance (CSS) separate makes a site easier to change."),
        H("The shape of a CSS rule"),
        T('''A CSS **rule** has two parts. The **selector** says which elements to style. The **declaration block**, written inside curly brackets, says how. Each **declaration** is a **property**, a colon, a **value** and a semicolon.'''),
        CODE('''p {
  color: blue;
  font-size: 18px;
}''', "css", title="Listing 1: a CSS rule",
             caption="Every paragraph on the page is shown with blue text, 18 pixels tall."),
        KEY("Read the rule", "Take it part by part.", cards=[
            ["p", "The selector: all paragraph elements."],
            ["color", "A property: what to change."],
            ["blue", "A value: what to change it to."],
            ["; and { }", "Each declaration ends with a semicolon. The curly brackets hold the block."],
        ]),
        H("Way 1: inline CSS"),
        T('''**Inline** CSS is written in the **style attribute** of one HTML element. It changes only that element.'''),
        CODE('''<p style="color: red; font-size: 20px;">Fees are due on Friday.</p>''', "html", title="Listing 2: inline CSS",
             caption="The browser shows this one paragraph in red, 20 pixels tall. No other paragraph changes."),
        H("Way 2: internal CSS"),
        T('''**Internal** CSS is written inside a <style> element in the <head>. It styles the whole page.'''),
        CODE('''<head>
  <title>GBHS Limbe</title>
  <style>
    p {
      color: blue;
    }
    h1 {
      color: darkgreen;
    }
  </style>
</head>''', "html", title="Listing 3: internal CSS",
             caption="Every paragraph on this page is blue and every h1 heading is dark green."),
        H("Way 3: external CSS"),
        T('''**External** CSS is kept in a separate file whose name ends in **.css**. The file contains only rules, with no HTML tags. Each page links to it with a <link> element in the <head>.'''),
        CODE('''/* file: style.css */
p {
  color: blue;
}
h1 {
  color: darkgreen;
}''', "css", title="Listing 4: the file style.css",
             caption="The text between the markers /* and */ is a comment. The browser ignores it."),
        CODE('''<head>
  <title>GBHS Limbe</title>
  <link rel="stylesheet" href="style.css">
</head>''', "html", title="Listing 5: linking to the file",
             caption="The browser loads style.css and applies its rules. rel=\"stylesheet\" says the file is a style sheet and href gives its address."),
        T('''The link element is empty, so it has no closing tag. The address in href is a relative address, as in the links lesson. If the .css file is in another folder, write the path, for example css/style.css.'''),
        H("Which rule wins?"),
        T('''Rules from different places may disagree. For example, an external file may say paragraphs are green, while an inline style says red. The browser needs one answer.

Two simple ideas decide. First, a more specific rule beats a general one, and an **inline style is the most specific**, so it wins over internal and external rules. Second, when two rules are equally specific, the **one that comes last** wins.'''),
        KEY("Order of strength", "For the same element and the same property.", cards=[
            ["1. Inline", "style attribute. Wins."],
            ["2. Internal or external", "The one that comes later in the page wins."],
            ["3. Browser default", "Used only when nothing else says otherwise."],
        ], note="Properties that do not conflict all apply. Only a clash on the same property is settled by the rules above."),
        H("Why external CSS is best"),
        T('''Imagine a school site with 30 pages. With inline or internal CSS you would change 30 pages to alter one colour. With external CSS you change one file and all 30 pages update.

Other reasons help too. The browser downloads style.css once and keeps a copy, so the next pages load faster and use less mobile data. The HTML stays short and clean. Every page looks the same, which makes the site look professional.'''),
        EX("Worked example 1: three ways for the same style", intro='''Make all h2 headings orange, first with inline CSS on one heading, then with internal CSS, then with external CSS.''', steps=[
            S("Inline", text="<h2 style=\"color: orange;\">News</h2> affects only this heading."),
            S("Internal", text="Put h2 { color: orange; } inside a <style> element in the head. All h2 headings on this page become orange."),
            S("External", text="Put h2 { color: orange; } in style.css and add <link rel=\"stylesheet\" href=\"style.css\"> to each page. All h2 headings on all linked pages become orange."),
        ]),
        EX("Worked example 2: which colour wins?", intro='''A page links to style.css, which says p { color: green; }. Its head also has a style element saying p { color: blue; }, written after the link. One paragraph has style="color: red;". What colour is (a) that paragraph and (b) every other paragraph?''', steps=[
            S("Paragraph with the inline style", text="Inline is the strongest, so it is red."),
            S("Other paragraphs", text="The external rule (green) and the internal rule (blue) are equally specific, so the one that comes last wins."),
            S("Which comes last", text="The style element is written after the link, so it is blue."),
            S("Answer", text="(a) red; (b) blue. If the style element came before the link, the answer for (b) would be green."),
        ]),
        CODE('''<head>
  <link rel="stylesheet" href="style.css">
  <style>
    p { color: blue; }
  </style>
</head>
<body>
  <p style="color: red;">Fees are due on Friday.</p>
  <p>Classes start on Monday.</p>
</body>''', "html", title="Listing 6: the page in worked example 2",
             caption="The browser shows the first paragraph in red and the second in blue."),
        H("Common mistakes"),
        MISTAKE("Writing HTML tags inside the .css file", "A .css file contains only CSS rules. Never put <style> tags or any HTML in it."),
        MISTAKE("Forgetting the semicolon or colon", "Each declaration needs a colon between property and value and a semicolon at the end. One missing semicolon can stop the next declaration working."),
        MISTAKE("Linking to the wrong file name", "If href is style.css but the file is named styles.css, no styling appears. Check the spelling, capitals and folder."),
        QUIZ("Where is the link element for an external style sheet placed?", ["In the body", "In the head", "Inside the .css file", "After the closing html tag"], 1,
             "The link element goes in the head, so the rules are loaded before the page is displayed.",
             hint="Information about the page, not the visible content.",
             feedback=["The body holds visible content. The link belongs in the head.", "", "The .css file contains only rules. It does not link to itself.", "Nothing should come after the closing html tag."]),
        QUIZ("An internal rule makes paragraphs blue and an inline style on one paragraph makes it red. What colour is that paragraph?", ["Blue", "Red", "Purple", "Black"], 1,
             "The inline style is more specific than an internal rule, so it wins.",
             hint="Which of the three ways is strongest?",
             feedback=["The internal rule is overridden for this paragraph.", "", "Colours are not mixed. The browser picks one winning value.", "Black is the browser default and applies only when no rule sets colour."]),
        H("Practice questions"),
        PQ("Name the three ways of adding CSS to a web page.",
           "Inline CSS (the style attribute on one element), internal CSS (a style element in the head) and external CSS (a separate .css file linked with a link element)."),
        PQ("State two advantages of external CSS over internal CSS.",
           "One file styles many pages, so a change is made once. The browser can keep a copy of the file, so later pages load faster. Also the HTML stays shorter and the whole site looks consistent."),
        PQ("In this rule, name (a) the selector, (b) the property and (c) the value: h1 { color: red; }",
           "(a) The selector is h1. (b) The property is color. (c) The value is red."),
        PQ("Write the line that links a page to a style sheet called school.css, and say where it goes.",
           "<link rel=\"stylesheet\" href=\"school.css\"> placed inside the head element."),
        SUM("CSS controls appearance; HTML gives structure. A rule is a selector with declarations (property: value;).",
            "Inline CSS uses the style attribute, internal CSS uses a style element in the head, and external CSS uses a .css file linked with link.",
            "When rules clash, inline wins; between internal and external of equal strength, the later one wins.",
            "External CSS is best: change one file, many pages update, and the browser can reuse the file.",
            "Never put HTML in a .css file, and check semicolons and file names."),
    ],
))

# ============================================================== 6. Selectors, colours and typography
LESSONS.append(lesson(
    module=MODULE, topic=CSS,
    title="Selectors, colours and typography",
    slug="css-selectors-colours-typography",
    minutes=24,
    summary="Choose elements with element, class and id selectors, group selectors, set colours by name or hex code, and style text with font-family, font-size, text-align and text-decoration.",
    objectives=[
        "Write element, class, id and grouped selectors",
        "Set colours using names and hex codes",
        "Use font-family, font-size, text-align and text-decoration",
        "Choose between a class and an id",
    ],
    key_concepts=["Selector", "Class", "Id", "Grouping", "Hex colour", "font-family", "text-align", "text-decoration"],
    blocks=[
        H("Introduction"),
        T('''In the previous lesson you saw that a CSS rule starts with a selector. So far the selector was always an element name such as p. But a school page may have five paragraphs and you want only one of them to look like a warning.

This lesson shows how to pick exactly the elements you want, and how to set colours and text styles.'''),
        H("Element selectors"),
        T('''An **element selector** is the name of an HTML element. It styles every element of that kind on the page.'''),
        CODE('''h1 {
  color: darkgreen;
}''', "css", title="Listing 1: an element selector",
             caption="Every h1 heading is dark green."),
        H("Class selectors"),
        D('''A **class** is a label you add to HTML elements with the class attribute. In CSS, a class selector is a **full stop followed by the class name**. The same class can be used on many elements.''', title="Definition"),
        CODE('''<p class="notice">Fees are due on Friday.</p>
<p>Classes start on Monday.</p>
<p class="notice">Bring your own pen.</p>''', "html", title="Listing 2: the HTML", caption="Two paragraphs have the class notice."),
        CODE('''.notice {
  color: red;
  font-weight: bold;
}''', "css", title="Listing 3: the class selector",
             caption="The two paragraphs with class notice are red and bold. The middle paragraph is unchanged."),
        H("Id selectors"),
        D('''An **id** is a unique name for one element on a page, given with the id attribute. In CSS, an id selector is a **hash sign followed by the id**. An id must be used only once on a page.''', title="Definition"),
        CODE('''<h1 id="school-name">GBHS Limbe</h1>''', "html", title="Listing 4: the HTML"),
        CODE('''#school-name {
  text-align: center;
}''', "css", title="Listing 5: the id selector",
             caption="Only the element with id school-name is centred."),
        KEY("Class or id?", "Choose by how many elements you style.", cards=[
            ["Class (.)", "Used for a style shared by several elements. Reusable."],
            ["Id (#)", "Used for one unique element, such as the page logo."],
        ], note="If in doubt, use a class."),
        H("Grouping selectors"),
        T('''When several selectors share the same declarations, list them separated by **commas**. This is **grouping**. You write the declarations once.'''),
        CODE('''h1, h2, h3 {
  color: navy;
  font-family: Arial, sans-serif;
}''', "css", title="Listing 6: grouped selectors",
             caption="All level 1, 2 and 3 headings are navy and use Arial."),
        H("Colours"),
        T('''Colours can be given by **name**, such as red, blue, darkgreen or gold. There are about 140 names. For any other colour use a **hex code**.

A hex code starts with a hash sign and has six hexadecimal digits: two for red, two for green and two for blue. Each pair runs from 00 (none of that colour) to FF (the most). The browser mixes the three lights.'''),
        CODE('''#FF0000   red     (red full, green none, blue none)
#00FF00   lime    (green full)
#0000FF   blue    (blue full)
#000000   black   (all none)
#FFFFFF   white   (all full)
#1D4ED8   a strong blue''', "text", title="Table 1: some hex colours"),
        T('''Two properties use colours often. **color** sets the text colour. **background-color** sets the colour behind an element.'''),
        CODE('''.banner {
  color: white;
  background-color: #1D4ED8;
}''', "css", title="Listing 7: text and background colour",
             caption="Elements of class banner show white text on a blue background."),
        TIP('''Make sure the text and background colours contrast well. Light grey text on white is hard to read, especially on a phone in sunlight.'''),
        H("Typography"),
        KEY("Four text properties", "Used in almost every style sheet.", cards=[
            ["font-family", "The typeface. List a first choice and a fallback: Arial, sans-serif."],
            ["font-size", "The size of the letters, for example 16px (pixels)."],
            ["text-align", "left, center, right or justify."],
            ["text-decoration", "underline, line-through, or none (removes the underline from links)."],
        ]),
        CODE('''body {
  font-family: Arial, sans-serif;
  font-size: 16px;
}
h1 {
  text-align: center;
}
a {
  text-decoration: none;
}''', "css", title="Listing 8: text styling",
             caption="All text uses Arial at 16 pixels. The h1 headings are centred. Links lose their underline."),
        T('''The fallback matters. If the visitor's device does not have Arial, the browser tries the next name. The last name, sans-serif, is a general family that every device has.'''),
        EX("Worked example 1: write the rules", intro='''Write CSS so that (a) every h2 is dark blue, (b) paragraphs with class tip have a pale yellow background (#FEF3C7), and (c) the element with id footer has centred text.''', steps=[
            S("Element selector", text="h2 { color: darkblue; }"),
            S("Class selector", text="A full stop starts a class selector: .tip { background-color: #FEF3C7; }"),
            S("Id selector", text="A hash sign starts an id selector: #footer { text-align: center; }"),
        ]),
        EX("Worked example 2: which elements are affected?", intro='''Look at the HTML and CSS below. Which words are shown in red?''', steps=[
            S("Read the selector", text=".alert, #total means: any element with class alert, and the element with id total. The comma means both are styled."),
            S("Match the HTML", text="Fees (class alert) and 45 000 FCFA (id total) match."),
            S("Skip the rest", text="Receipt has neither class nor id, so it is not red."),
            S("Answer", text="Fees and 45 000 FCFA are red. Receipt is not."),
        ]),
        CODE('''<p class="alert">Fees</p>
<p>Receipt</p>
<p id="total">45 000 FCFA</p>''', "html", title="Listing 9: the HTML"),
        CODE('''.alert, #total {
  color: red;
}''', "css", title="Listing 10: the CSS"),
        H("Common mistakes"),
        MISTAKE("Using the wrong symbol", "A class selector starts with a full stop (.notice) and an id selector with a hash (#logo). Writing notice or logo alone selects an element named notice or logo, which does not exist."),
        MISTAKE("Using one id on several elements", "An id must be unique on a page. For a style shared by many elements, use a class."),
        MISTAKE("Writing the hex code without the hash", "ff0000 does nothing. Write #ff0000."),
        QUIZ("Which selector styles the element with id=\"menu\"?", ["menu", ".menu", "#menu", "id menu"], 2,
             "A hash sign followed by the id name selects the element with that id.",
             hint="Class and id use different symbols.",
             feedback=["That would select an element named menu, which is not an HTML element.", "A full stop selects a class, not an id.", "", "That is not valid CSS."]),
        QUIZ("Which hex code gives pure blue?", ["#FF0000", "#00FF00", "#0000FF", "#FFFFFF"], 2,
             "Hex codes are in the order red, green, blue. Blue full with no red or green is #0000FF.",
             hint="The three pairs are red, then green, then blue.",
             feedback=["That is red.", "That is green.", "", "That is white: all three at full."]),
        H("Practice questions"),
        PQ("State the difference between a class selector and an id selector in the way they are written and used.",
           "A class selector starts with a full stop (.notice) and can be used on many elements. An id selector starts with a hash sign (#logo) and is used on one unique element."),
        PQ("Rewrite the two rules as one rule: h1 { color: blue; } and h2 { color: blue; }",
           "h1, h2 { color: blue; }. The comma groups the two selectors so the declaration is written once."),
        PQ("Explain what each part of #1D4ED8 means.",
           "The hash sign shows a hex colour. 1D is the amount of red, 4E the amount of green and D8 the amount of blue. Each pair goes from 00 to FF."),
        PQ("Write CSS that centres all h1 headings, sets the font to Verdana with sans-serif as a fallback, and removes the underline from links.",
           "h1 { text-align: center; font-family: Verdana, sans-serif; } and a { text-decoration: none; }"),
        SUM("An element selector styles every element of that name; a class (.name) can be shared; an id (#name) is for one element.",
            "Group selectors with commas to write shared declarations once.",
            "Colours are given by name or by a hex code of three pairs: red, green and blue, from 00 to FF.",
            "color is the text colour and background-color is the colour behind it.",
            "font-family (with a fallback), font-size, text-align and text-decoration control text."),
    ],
))

# ============================================================== 7. The box model and simple layout
LESSONS.append(lesson(
    module=MODULE, topic=CSS,
    title="The box model and simple layout",
    slug="css-box-model-display-layout",
    minutes=25,
    summary="Understand that every element is a box with content, padding, border and margin, calculate widths, tell block and inline elements apart, centre a block and plan a two-column layout.",
    objectives=[
        "Name the four parts of the box model and say what each does",
        "Calculate the total width of a box",
        "Distinguish block and inline elements using display",
        "Centre a block and describe a simple two-column layout",
    ],
    key_concepts=["Box model", "Padding", "Border", "Margin", "Block and inline", "box-sizing", "Two-column layout"],
    blocks=[
        H("Introduction"),
        T('''To a browser, every element on a page is a rectangular **box**, even a single paragraph or a picture. To place things neatly, you must understand how that box is built.

A school notice board is a good picture. The notice is the content. The white edge between the text and the frame is padding. The frame is the border. The gap between this notice and the next one is the margin. CSS uses these same four words.'''),
        H("The four parts of the box"),
        KEY("The box model", "From the inside to the outside.", cards=[
            ["Content", "The text or image itself. Its size is set by width and height."],
            ["Padding", "Space between the content and the border, inside the box."],
            ["Border", "A line around the padding."],
            ["Margin", "Space outside the border, between this box and the others."],
        ]),
        IMG("f5c-css-box-model.svg",
            alt="Nested rectangles. In the middle is the green content box. Around it a light blue padding area, then a thick dark border, then a dashed outer margin area.",
            caption="Figure 1. The CSS box model: content, padding, border and margin."),
        CODE('''.card {
  width: 200px;
  padding: 20px;
  border: 5px solid black;
  margin: 10px;
}''', "css", title="Listing 1: a box with all four parts",
             caption="The content is 200 pixels wide. It has 20 pixels of padding, a black solid border 5 pixels thick and a 10-pixel gap outside."),
        T('''Padding, border and margin can be set for all four sides at once, as above, or for one side: padding-left, border-top, margin-bottom and so on.

A shorter way gives values for several sides. Two values, such as margin: 10px 30px;, mean top and bottom 10px, left and right 30px. Four values go clockwise from the top: top, right, bottom, left.'''),
        H("Calculating the width of a box"),
        D('''By default, the width property sets the width of the **content only**. Padding and border are added outside it. So the width of the visible box is the content width plus the left and right padding plus the left and right borders. Margins are extra space outside the box.''', title="The width rule",
          formula=r"\text{box width} = \text{content} + 2 \times \text{padding} + 2 \times \text{border}"),
        EX("Worked example 1: width of the card", intro='''Use Listing 1. Find (a) the width of the visible box and (b) the horizontal space the card takes up including margins.''', steps=[
            S("Add the padding", text="Padding is on both sides: 20 + 20 = 40."),
            S("Add the border", text="Border is on both sides: 5 + 5 = 10."),
            S("Visible box width", text="200 + 40 + 10 = 250 pixels."),
            S("Add the margins", text="Margin is on both sides: 10 + 10 = 20, so the total space is 250 + 20 = 270 pixels."),
        ]),
        T('''This can surprise beginners. A box set to width 300px with padding can end up wider than 300px and push outside its container on a small phone screen.

The property **box-sizing: border-box** fixes this. With it, width includes the padding and border, so the content shrinks to fit. Many web designers add it to every element.'''),
        CODE('''.card {
  box-sizing: border-box;
  width: 300px;
  padding: 20px;
  border: 5px solid black;
}''', "css", title="Listing 2: box-sizing: border-box",
             caption="The visible box is exactly 300 pixels wide. The content gets what is left: 300 - 40 - 10 = 250 pixels."),
        H("Block and inline elements"),
        D('''A **block** element starts on a new line and stretches across the full width available. Examples are p, h1, ul and div. An **inline** element stays inside a line of text and takes only the space it needs. Examples are a, strong, em, img and span.''', title="Definition"),
        T('''Width and height work on block elements. They are ignored on inline elements. You can change the type with the **display** property: display: block; makes an element block, display: inline; makes it inline, and display: none; hides it completely.

The element <div> is an empty block used to group other elements. The element <span> is an empty inline used to style a few words inside a paragraph.'''),
        H("Centring a block"),
        T('''To centre a block horizontally, give it a width and set its left and right margins to **auto**. The browser shares the leftover space equally.'''),
        CODE('''.page {
  width: 600px;
  margin: 0 auto;
}''', "css", title="Listing 3: a centred block",
             caption="The element with class page is 600 pixels wide, with no margin at top and bottom, and sits in the middle of the window."),
        T('''To centre text inside an element, use text-align: center; instead. The two do different jobs.'''),
        H("A simple two-column layout"),
        T('''A page often has a menu on the left and the main text on the right. The idea is to put two blocks side by side inside a container. A modern way is to give the container **display: flex**, which places its children in a row. Then give each column a width. The two widths should add up to 100 percent or less.'''),
        CODE('''<div class="row">
  <div class="menu">Menu</div>
  <div class="main">News</div>
</div>''', "html", title="Listing 4: the HTML"),
        CODE('''.row {
  display: flex;
}
.menu {
  width: 30%;
  background-color: #EFF6FF;
}
.main {
  width: 70%;
}''', "css", title="Listing 5: the CSS",
             caption="The browser shows Menu in a narrow pale blue column on the left, taking 30 percent of the width, and News in a wider column taking 70 percent."),
        TIP('''Test your layout on a narrow window. A two-column layout can be too tight for a phone. Later you may stack the columns on small screens.'''),
        EX("Worked example 2: does the box fit?", intro='''A phone screen leaves 360 pixels for the page. A box has width 300px, padding 30px and border 2px, with the default box sizing. Does it fit? What if box-sizing is border-box?''', steps=[
            S("Default box sizing", text="Width = 300 + 2 x 30 + 2 x 2 = 300 + 60 + 4 = 364 pixels."),
            S("Compare", text="364 is bigger than 360, so it does not fit and the page will scroll sideways."),
            S("With border-box", text="The width of the visible box is exactly 300 pixels, which is less than 360, so it fits."),
        ]),
        H("Common mistakes"),
        MISTAKE("Forgetting that padding and border add to the width", "With default sizing, width is only the content. Add padding and border when you calculate how much space the box needs."),
        MISTAKE("Confusing padding and margin", "Padding is inside the border (the background colour shows in it). Margin is outside the border and is always transparent."),
        MISTAKE("Using margin: auto on an inline element or a box with no width", "A block with no width already fills the line, so there is nothing left to share. Give the block a width first."),
        QUIZ("A box has content width 100px, padding 10px and border 2px on every side. What is the width of the visible box?", ["100px", "112px", "124px", "134px"], 2,
             "100 + 2 x 10 + 2 x 2 = 100 + 20 + 4 = 124 pixels.",
             hint="Add padding and border on both the left and the right.",
             feedback=["That is only the content.", "You added padding and border on one side only (100 + 10 + 2).", "", "You counted the padding on three sides instead of two."]),
        QUIZ("Which element is inline by default?", ["p", "div", "span", "h1"], 2,
             "span is inline: it sits inside a line of text. p, div and h1 are block elements.",
             hint="Which element is used to style a few words inside a paragraph?",
             feedback=["p is a block element: it starts on a new line.", "div is a block element used for grouping.", "", "h1 is a block element."]),
        H("Practice questions"),
        PQ("Name the four parts of the CSS box model, from the inside to the outside.",
           "Content, padding, border and margin."),
        PQ("Distinguish between padding and margin.",
           "Padding is the space between the content and the border, inside the box. Margin is the space outside the border, separating the box from other boxes."),
        PQ("A box has width 250px, padding 15px and border 3px with default box sizing. Calculate the width of the visible box.",
           "250 + 2 x 15 + 2 x 3 = 250 + 30 + 6 = 286 pixels."),
        PQ("Write CSS to centre a 500px wide block in the window, and explain how it works.",
           "div.page { width: 500px; margin: 0 auto; } (or any selector). Auto left and right margins share the leftover space equally, so the block sits in the middle."),
        SUM("Every element is a box: content, then padding, then border, then margin.",
            "With default sizing, box width = content width + padding on both sides + border on both sides. Margins are extra.",
            "box-sizing: border-box makes the width include padding and border.",
            "Block elements start on a new line and fill the width; inline elements stay in the line. Change this with display.",
            "Centre a block with a width and margin: 0 auto. A two-column layout can use display: flex and widths such as 30 percent and 70 percent."),
    ],
))
