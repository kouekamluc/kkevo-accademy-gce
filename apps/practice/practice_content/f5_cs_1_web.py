"""Form 5 Computer Science: practice sets for Web Design & Publishing (HTML5 structure, CSS styling), one per lesson."""

from .dsl import *  # noqa: F403

COURSE = ("computer-science", "form-5")

MODULE = "Web Design & Publishing"
HTML = "HTML5 structure"
CSS = "CSS styling"

SETS = []

# ------------------------------------------------------------------ 1. The structure of an HTML5 page
SETS.append(practice_set(
    module=MODULE, topic=HTML,
    title="Structure of an HTML5 page", lesson="html5-structure-first-web-page",
    questions=[
        MC("Which line must come first in an HTML5 page?", [
            C("<html>", why="The html element comes after the doctype line, not before it."),
            C("<!DOCTYPE html>", correct=True),
            C("<head>", why="The head is inside the html element, so it cannot be the first line."),
            C("<title>", why="The title is inside the head. It is not the first line."),
        ], steps=[S("Recall the skeleton", text="The doctype tells the browser the page uses HTML5, so it is the first line."),
                  S("Then the root element", text="After it comes <html>, which holds the head and the body.")],
           concept="Doctype", skill="Recall", hint="One line tells the browser which version of HTML the page uses.",
           feedback="The doctype comes first, then the html element."),
        MC("Which element holds the name shown on the browser tab?", [
            C("<h1>", why="An h1 is a heading shown inside the page area, not on the tab."),
            C("<body>", why="The body holds visible content, not the tab name."),
            C("<title>", correct=True),
            C("<p>", why="A p element is a paragraph shown inside the page."),
        ], steps=[S("Find the page name element", text="The <title> element, written inside <head>, gives the page its tab name.")],
           concept="Head and title", skill="Recall", hint="It is written inside the head, not the body."),
        MC("In <p>Hello</p>, the whole piece from <p> to </p> is called", [
            C("an element", correct=True),
            C("a tag", why="A tag is only one marker, such as <p> or </p>. The whole unit is the element."),
            C("an attribute", why="An attribute is extra information inside the opening tag, such as lang=\"en\"."),
            C("a document", why="The document is the whole HTML file, not one paragraph."),
        ], steps=[S("Separate the words", text="Tags are the markers. The element is opening tag + content + closing tag.")],
           concept="Tag and element", skill="Concept", hint="Think of what the opening tag, content and closing tag make together."),
        MC('In <a href="news.html">News</a>, which word is the name of an attribute?', [
            C("a", why="a is the name of the element (the tag name), not an attribute."),
            C("News", why="News is the content of the element, the text the visitor sees."),
            C("news.html", why="news.html is the value of the attribute."),
            C("href", correct=True),
        ], steps=[S("Look inside the opening tag", text="An attribute is a name = value pair inside the opening tag."),
                  S("Identify the parts", text="href is the name, and news.html is its value.")],
           concept="Attributes", skill="Recall", hint="An attribute is written as name=value inside the opening tag."),
        MC("Which line is correctly nested?", [
            C("<p><strong>Hi</p></strong>", why="The tags cross: p is closed before strong, which was opened second."),
            C("<p><strong>Hi</strong></p>", correct=True),
            C("<strong><p>Hi</strong></p>", why="The tags cross: strong is closed before p, which was opened second."),
            C("</p><strong>Hi</strong><p>", why="The closing p tag appears before its opening tag."),
        ], steps=[S("Apply the rule", text="The last element opened is the first one closed."),
                  S("Check each option", text="Only <p><strong>Hi</strong></p> closes strong before p.")],
           concept="Nesting", skill="Application", hint="Close the inner element before the outer element."),
        MC("Which of these belongs in the body of a page rather than the head?", [
            C("The title element", why="The title is information about the page and sits in the head."),
            C("The meta charset line", why="This sets the character set for the page and sits in the head."),
            C("A paragraph of text", correct=True),
            C("A link to a style sheet", why="A link to a style sheet goes in the head."),
        ], steps=[S("Sort by purpose", text="The head holds information about the page. The body holds what the visitor sees."),
                  S("Decide", text="A paragraph is visible content, so it goes in the body.")],
           concept="Head and body", skill="Concept", hint="Which one would a visitor see on the page itself?"),
        NUM("Count the elements in this page: <html><head><title>T</title></head><body><h1>H</h1><p>P</p></body></html>. How many elements are there in total?", 6,
            steps=[S("List the elements", text="html, head, title, body, h1 and p."),
                   S("Count", text="That is 6 elements. The doctype is not an element, and the text T, H and P are content.")],
            concept="Elements and the document tree", skill="Calculation",
            hint="Count the opening tags, one per element."),
        MC("A student saves her page as index.html.txt and double-clicks it. The browser shows the code as plain text. What is the best explanation?", [
            C("The file ends in .txt, so it is opened as a text file, not a web page", correct=True),
            C("The doctype line is spelt in capital letters", why="The doctype is normally written in capitals. This is not the cause."),
            C("The body element is missing", why="A missing body would not make the browser show the tags as text."),
            C("The page was not indented", why="Indentation is only for people. The browser ignores it."),
        ], steps=[S("Look at the file name", text="The last part of the name is .txt, which means a text file."),
                  S("Fix it", text="Save the file again with the name index.html (on Windows, choose Save as type: All files).")],
           concept="Saving and opening a page", skill="Reasoning", hint="Look at the very end of the file name."),
    ]))

# ------------------------------------------------------------------ 2. Text, links and images
SETS.append(practice_set(
    module=MODULE, topic=HTML,
    title="Headings, lists, links and images", lesson="html5-text-links-images",
    questions=[
        MC("Which element is used for the most important heading on a page?", [
            C("<h6>", why="h6 is the least important heading, not the most."),
            C("<head>", why="head is the part of the page that holds information about it, not a heading."),
            C("<h1>", correct=True),
            C("<title>", why="title names the page on the tab. It is not a heading inside the page."),
        ], steps=[S("Recall the heading levels", text="Headings run from h1 (most important) down to h6 (least important).")],
           concept="Headings", skill="Recall", hint="Heading levels start at 1."),
        MC("Which element is normally displayed in bold to show strong importance?", [
            C("<strong>", correct=True),
            C("<em>", why="em is for emphasis and is normally shown in italics."),
            C("<br>", why="br makes a line break. It has no content to make bold."),
            C("<li>", why="li is a list item. It does not make text bold."),
        ], steps=[S("Match the element to its effect", text="strong is shown in bold, em is shown in italics.")],
           concept="Strong and em", skill="Recall", hint="One of the two emphasis elements is bold, the other italic."),
        MC("Which tags make a bulleted list with two items?", [
            C("<ol> with two <li> elements", why="ol gives numbers, not bullets."),
            C("<ul> with two <p> elements", why="The items must be li elements, not paragraphs."),
            C("<li> with two <ul> elements", why="The order is the wrong way round. The list element holds the items."),
            C("<ul> with two <li> elements", correct=True),
        ], steps=[S("Choose the list type", text="Bullets mean unordered, so ul."),
                  S("Add the items", text="Each item is an li inside the ul.")],
           concept="Lists", skill="Concept", hint="U stands for unordered."),
        MC("Which attribute of the anchor element holds the address of the link?", [
            C("src", why="src is the attribute of img, giving the file of the picture."),
            C("href", correct=True),
            C("alt", why="alt is the text description of an image."),
            C("link", why="link is not an attribute of the anchor element."),
        ], steps=[S("Recall the link syntax", text="<a href=\"address\">text</a>. The address goes in href.")],
           concept="Hyperlinks", skill="Recall", hint="It stands for hypertext reference."),
        MC("Which of these is a relative address?", [
            C("https://www.example.com/news.html", why="This starts with https:// and is complete, so it is an absolute address."),
            C("https://www.example.com", why="This is a full website address, so it is absolute."),
            C("contact.html", correct=True),
            C("http://localhost/contact.html", why="It starts with http:// and names the host, so it is absolute."),
        ], steps=[S("Look at the beginning", text="An absolute address starts with https:// and names the website."),
                  S("Identify the other", text="contact.html gives only a file name from the current page, so it is relative.")],
           concept="Absolute and relative addresses", skill="Concept", hint="A relative address does not name the website."),
        MC("A phone has no signal and a picture cannot load. Which attribute makes the browser show a description in its place?", [
            C("src", why="src says which file to load. It cannot supply words when the file is missing."),
            C("width", why="width sets the size and does not give a description."),
            C("title", why="title is a different attribute, and it is not what browsers rely on when an image fails."),
            C("alt", correct=True),
        ], steps=[S("Find the alternative text", text="alt is the alternative text shown if the image cannot load. Screen readers also read it.")],
           concept="Alt text", skill="Application", hint="Think of text as an alternative to the picture."),
        NUM("A page has one ordered list with 5 items and one unordered list with 3 items. How many of the items are shown with a number?", 5,
            steps=[S("Only the ordered list shows numbers", text="The ol list is numbered, and the ul list shows bullets."),
                   S("Count", text="The ordered list has 5 items, so 5 items are numbered.")],
            concept="Ordered and unordered lists", skill="Application", hint="Which list type shows numbers?"),
        MC("Which image element is fully correct?", [
            C('<img href="lab.jpg" alt="Our lab">', why="The file is given with src, not href."),
            C('<img src="lab.jpg" alt="Our lab">', correct=True),
            C('<img src="lab.jpg"></img>', why="img is empty and has no closing tag, and the alt attribute is missing."),
            C('<img alt="Our lab">', why="Without src there is no file to show."),
        ], steps=[S("Check the required attributes", text="An image needs src for the file and alt for the description."),
                  S("Check the tag", text="img is an empty element, so there is no closing tag.")],
           concept="Images", skill="Application", hint="Which two attributes does every image need?"),
    ]))

# ------------------------------------------------------------------ 3. HTML tables
SETS.append(practice_set(
    module=MODULE, topic=HTML,
    title="Building HTML tables", lesson="html5-tables-rows-cells-spans",
    questions=[
        MC("Which element creates one row of a table?", [
            C("<td>", why="td creates one data cell, not a whole row."),
            C("<tr>", correct=True),
            C("<th>", why="th creates one heading cell inside a row."),
            C("<row>", why="There is no row element in HTML. The table row is tr."),
        ], steps=[S("Recall", text="tr stands for table row. Cells go inside it.")],
           concept="Table rows", skill="Recall", hint="The letters stand for table row."),
        MC("Which element makes a bold, centred heading cell?", [
            C("<td>", why="td is an ordinary cell, not bold or centred by default."),
            C("<tr>", why="tr is a row, not a cell."),
            C("<caption>", why="caption is the title of the whole table."),
            C("<th>", correct=True),
        ], steps=[S("Recall", text="th is the table heading cell. Browsers show it bold and centred.")],
           concept="Heading cells", skill="Recall", hint="Th stands for table heading."),
        MC("Where is the caption element placed?", [
            C("Straight after the opening table tag", correct=True),
            C("In the head of the page", why="The head holds information about the page. A caption belongs to a table."),
            C("After the closing table tag", why="A caption must be inside the table, right after the table opens."),
            C("Inside every tr", why="One caption names the whole table, not each row."),
        ], steps=[S("Recall", text="The caption is the first thing inside the table. It displays above the table.")],
           concept="Caption", skill="Recall", hint="The caption names the whole table, so it comes first."),
        MC("A cell must stretch across two columns. Which attribute does this?", [
            C('rowspan="2"', why="rowspan stretches the cell down two rows, not across two columns."),
            C('width="2"', why="width sets a size and does not merge cells."),
            C('colspan="2"', correct=True),
            C('columns="2"', why="There is no columns attribute for a cell."),
        ], steps=[S("Match direction to name", text="colspan = columns, going across. rowspan = rows, going down.")],
           concept="colspan", skill="Concept", hint="Across is columns."),
        MC("A cell on Monday must cover the 10:00 and 11:00 rows of a timetable. Which attribute is used?", [
            C('colspan="2"', why="colspan stretches across columns. Here the cell must stretch down."),
            C('rowspan="2"', correct=True),
            C('rowspan="1"', why="rowspan 1 is the normal size and covers only one row."),
            C('colspan="1"', why="colspan 1 is the normal size and does not merge anything."),
        ], steps=[S("Decide the direction", text="The cell goes down two rows, so rowspan is needed."),
                  S("Choose the number", text="Two rows means the value is 2.")],
           concept="rowspan", skill="Application", hint="The cell stretches down the page."),
        MC("A table has 3 columns. A row has the cells: td, then th with colspan=\"2\". How many columns does the row fill?", [
            C("2", why="You counted the two cells. The second cell covers two columns by itself."),
            C("3", correct=True),
            C("4", why="You counted the spanning cell twice. A colspan of 2 covers two columns in total."),
            C("5", why="You added the table width of 3 to the 2 columns of the span."),
        ], steps=[S("Count each cell's columns", text="The td covers 1 column and the th with colspan 2 covers 2 columns."),
                  S("Add", text="1 + 2 = 3 columns, which fills the row.")],
           concept="Counting cells", skill="Calculation", hint="Add the columns each cell covers."),
        NUM("A table has 4 columns. In row 2, the first cell has rowspan=\"2\" and there are three other cells. How many cells must row 3 contain?", 3,
            steps=[S("Find what row 3 already has", text="The rowspan cell from row 2 takes the first column of row 3."),
                   S("Subtract", text="4 columns - 1 column = 3 cells are still needed in row 3.")],
            concept="rowspan and cell counting", skill="Calculation", hint="Which column of row 3 is already filled by the cell above?"),
        MC("Which table code has an error?", [
            C("<table><tr><th>Name</th></tr></table>", why="This is correct: th is inside tr, and tr is inside table."),
            C("<table><tr><td>A</td><td>B</td></tr></table>", why="This is correct: the row holds two cells."),
            C("<table><td>A</td></table>", correct=True),
            C("<table><caption>Fees</caption><tr><td>5</td></tr></table>", why="This is correct: the caption is straight after table."),
        ], steps=[S("Check the nesting", text="A cell must be inside a tr, and tr inside table."),
                  S("Find the fault", text="In the third option the td is directly inside table, with no tr.")],
           concept="Correct table structure", skill="Reasoning", hint="Check where each cell is placed."),
    ]))

# ------------------------------------------------------------------ 4. HTML forms
SETS.append(practice_set(
    module=MODULE, topic=HTML,
    title="Forms and input controls", lesson="html5-forms-input-controls",
    questions=[
        MC("Which input type shows the characters the user types as dots?", [
            C('type="text"', why="A text box shows the characters exactly as typed."),
            C('type="radio"', why="radio makes a round selection button, not a typing area."),
            C('type="password"', correct=True),
            C('type="submit"', why="submit makes a button that sends the form."),
        ], steps=[S("Match the type", text="password hides what is typed behind dots or stars.")],
           concept="Input types", skill="Recall", hint="One type has the name of the thing it protects."),
        MC("Which control lets the visitor choose only one option from a group?", [
            C("Radio buttons", correct=True),
            C("Checkboxes", why="Checkboxes allow none, one or several to be ticked."),
            C("A text box", why="A text box is for typing, not for choosing from options."),
            C("A textarea", why="A textarea is a larger box for typing several lines."),
        ], steps=[S("Compare", text="Radio buttons in a group allow one choice. Checkboxes allow many.")],
           concept="Radio buttons and checkboxes", skill="Concept", hint="Think of a round button in a group."),
        MC('A label is written as <label for="city">. Which attribute must the matching control have?', [
            C('name="for"', why="name is the data name. The label connects through id."),
            C('class="city"', why="class is used for styling, not for linking a label."),
            C('type="city"', why="type chooses the kind of control. It does not link the label."),
            C('id="city"', correct=True),
        ], steps=[S("Link label and control", text="The for value of the label must equal the id of the control."),
                  S("Result", text="Clicking the label then selects the control.")],
           concept="Labels", skill="Concept", hint="The label's for must equal another attribute of the control."),
        MC("Which element creates a box for typing several lines, such as a message?", [
            C('<input type="text">', why="A text input is a one-line box."),
            C("<textarea>", correct=True),
            C("<select>", why="select makes a drop-down list for choosing, not typing."),
            C("<option>", why="option is one choice inside a select element."),
        ], steps=[S("Pick by purpose", text="Several lines of text need textarea.")],
           concept="Textarea", skill="Recall", hint="The name suggests an area of text."),
        MC("Why do radio buttons in the same group need the same name attribute?", [
            C("So that the browser treats them as one group and allows only one choice", correct=True),
            C("So that they all show the same label", why="Labels are set separately with the label element."),
            C("So that they are sent to the server twice", why="Only the chosen value is sent, once."),
            C("So that they become checkboxes", why="The type attribute decides the control. Name does not change it."),
        ], steps=[S("Recall how grouping works", text="The browser groups radio buttons by name."),
                  S("Effect", text="Choosing one clears the others, so only one value is sent.")],
           concept="name and value", skill="Concept", hint="The browser groups radio buttons by one attribute."),
        MC("A cyber cafe registration form asks for a password. Which method is better in the form tag?", [
            C('method="get"', why="get adds the data to the page address, where the password could be seen."),
            C('method="show"', why="show is not a valid method."),
            C('method="post"', correct=True),
            C('method="type"', why="type is not a valid method. Valid methods are get and post."),
        ], steps=[S("Compare the methods", text="get puts data in the address. post sends it inside the request."),
                  S("Choose", text="Private data such as a password should use post.")],
           concept="get and post", skill="Application", hint="Which method keeps data out of the address bar?"),
        NUM("A form has two text boxes, one password box, one group of three radio buttons and one drop-down list. The visitor fills in everything. How many name and value pairs are sent?", 5,
            steps=[S("Count each control", text="Two text boxes send 2 pairs and the password sends 1 pair."),
                   S("Count the groups", text="The radio group sends 1 pair (only the chosen button) and the drop-down sends 1 pair."),
                   S("Add", text="2 + 1 + 1 + 1 = 5 pairs.")],
            concept="name and value", skill="Calculation", hint="A group of radio buttons sends only one value."),
        MC('A visitor chooses the button <input type="radio" name="delivery" value="home">. What does the form send?', [
            C("home=delivery", why="The pair is name=value, so the name comes first."),
            C("radio=home", why="radio is the type of the control, not its name."),
            C("delivery=radio", why="radio is the type. The value sent is the value attribute."),
            C("delivery=home", correct=True),
        ], steps=[S("Find the name", text="name is delivery."),
                  S("Find the value", text="value is home."),
                  S("Combine", text="The pair sent is delivery=home.")],
           concept="name and value", skill="Application", hint="Data is sent as name, then value."),
    ]))

# ------------------------------------------------------------------ 5. Adding CSS
SETS.append(practice_set(
    module=MODULE, topic=CSS,
    title="Inline, internal and external CSS", lesson="css-adding-inline-internal-external",
    questions=[
        MC("What does CSS stand for?", [
            C("Computer Style Software", why="CSS is a language, not software, and the words are different."),
            C("Cascading Style Sheets", correct=True),
            C("Creative Site Structure", why="Structure is the job of HTML. CSS controls appearance."),
            C("Coded Screen Symbols", why="These words do not make up the name CSS."),
        ], steps=[S("Recall", text="CSS means Cascading Style Sheets. It describes how HTML elements look.")],
           concept="What CSS is", skill="Recall", hint="The middle word is Style."),
        MC('Which is an example of inline CSS?', [
            C('<p style="color: red;">Hello</p>', correct=True),
            C("p { color: red; } inside a style element in the head", why="This is internal CSS because it is written in a style element in the page."),
            C("p { color: red; } in a file called style.css", why="This is external CSS because it is in a separate .css file."),
            C('<link rel="stylesheet" href="style.css">', why="This links an external style sheet. It is not itself inline CSS."),
        ], steps=[S("Look for the style attribute", text="Inline CSS is written in the style attribute of one element.")],
           concept="Inline CSS", skill="Concept", hint="Inline CSS is written inside the opening tag of the element."),
        MC("Where does a style element for internal CSS normally go?", [
            C("In the head", correct=True),
            C("In the body, after the last paragraph", why="It could work, but the normal place is the head, so the rules load before the content."),
            C("Inside a .css file", why="A .css file contains rules only. It has no style element."),
            C("Before the doctype line", why="The doctype must be the first line of the page."),
        ], steps=[S("Recall", text="The style element is part of the information about the page, so it sits in the head.")],
           concept="Internal CSS", skill="Recall", hint="It is information about the page, not visible content."),
        MC("Which element joins a page to an external style sheet?", [
            C("<style>", why="style holds internal rules written in the page itself."),
            C("<a>", why="a makes a link that a visitor clicks. It does not load a style sheet."),
            C("<link>", correct=True),
            C("<css>", why="There is no css element in HTML."),
        ], steps=[S("Recall", text='<link rel="stylesheet" href="style.css"> in the head connects the file.')],
           concept="External CSS", skill="Recall", hint="It is an empty element in the head."),
        MC("Which statement about a .css file is true?", [
            C("It contains HTML tags and CSS rules", why="A .css file should hold only CSS rules. HTML tags do not belong in it."),
            C("It contains only CSS rules", correct=True),
            C("It must be saved as .html", why="A style sheet is saved as .css so that the link can find it."),
            C("It must be written in the body", why="It is a separate file and is not written in any page's body."),
        ], steps=[S("Remember the file type", text="The file contains rules such as h1 { color: red; } and nothing else.")],
           concept="External CSS", skill="Concept", hint="Think about what a style sheet needs."),
        MC('An internal rule says p { color: blue; }, and one paragraph has style="color: red;". What colour is that paragraph?', [
            C("Red", correct=True),
            C("Blue", why="The internal rule is overridden for this paragraph by the inline style."),
            C("Purple", why="Colours are never mixed. The browser picks one winning value."),
            C("Black", why="Black is the browser default and is used only when no rule sets a colour."),
        ], steps=[S("Compare strength", text="Inline is more specific than internal."),
                  S("Decide", text="The inline style wins, so the paragraph is red.")],
           concept="Which rule wins", skill="Reasoning", hint="Which of the two is the most specific?"),
        NUM("How many declarations are in this rule? p { color: red; font-size: 14px; text-align: center; }", 3,
            steps=[S("Find the declarations", text="A declaration is a property, a colon, a value and a semicolon."),
                   S("Count", text="color: red; font-size: 14px; text-align: center; makes 3 declarations.")],
            concept="Rule structure", skill="Interpretation", hint="Count the semicolons that end each declaration."),
        MC('A page has this head: <link rel="stylesheet" href="style.css"> (style.css says p { color: green; }) followed by <style> p { color: blue; } </style>. A paragraph has no inline style. What colour is it?', [
            C("Green", why="The external rule comes first. When rules are equally specific, the later one wins, not the earlier one."),
            C("Black", why="Black is the browser default, used only when no rule sets a colour."),
            C("Blue", correct=True),
            C("Green and blue mixed", why="Colours are never mixed. The browser picks one winning value."),
        ], steps=[S("Compare the specificity", text="Both rules select p, so they are equally strong."),
                  S("Use the order", text="The style element comes after the link, so its rule is the last one. The paragraph is blue.")],
           concept="Which rule wins", skill="Reasoning", hint="Both rules are equally strong. Which one comes last?"),
    ]))

# ------------------------------------------------------------------ 6. Selectors, colours and typography
SETS.append(practice_set(
    module=MODULE, topic=CSS,
    title="Selectors, colours and fonts", lesson="css-selectors-colours-typography",
    questions=[
        MC("Which symbol starts a class selector?", [
            C("A full stop (.)", correct=True),
            C("A hash sign (#)", why="A hash sign starts an id selector, not a class selector."),
            C("A colon (:)", why="A colon separates a property from its value in a declaration."),
            C("A semicolon (;)", why="A semicolon ends a declaration."),
        ], steps=[S("Recall", text=".name selects a class and #name selects an id.")],
           concept="Class selectors", skill="Recall", hint="Class and id use different symbols."),
        MC("Which selector styles the element with id=\"logo\"?", [
            C(".logo", why="A full stop selects a class, not an id."),
            C("logo", why="This would select an element named logo, which does not exist in HTML."),
            C("#logo", correct=True),
            C("id.logo", why="This is not valid CSS."),
        ], steps=[S("Use the id symbol", text="A hash sign followed by the id name: #logo.")],
           concept="Id selectors", skill="Recall", hint="Think of the symbol for an id."),
        MC("Which rule styles both h1 and h2 headings in the same way?", [
            C("h1 h2 { color: navy; }", why="Without a comma this means an h2 inside an h1, which is not what you want."),
            C("h1.h2 { color: navy; }", why="This means an h1 with the class h2."),
            C("h1 + h2 { color: navy; }", why="This is a different kind of selector for an h2 directly after an h1."),
            C("h1, h2 { color: navy; }", correct=True),
        ], steps=[S("Group with a comma", text="Selectors separated by commas share the declarations.")],
           concept="Grouping selectors", skill="Concept", hint="Selectors that share a rule are separated by a comma."),
        MC("Which property sets the colour of the text?", [
            C("background-color", why="This sets the colour behind the element, not the text."),
            C("color", correct=True),
            C("font-color", why="font-color is not a CSS property. The text colour property is color."),
            C("text-style", why="text-style is not a CSS property."),
        ], steps=[S("Recall", text="color sets the text. background-color sets the background.")],
           concept="Colour properties", skill="Recall", hint="It is the shortest name."),
        MC("Which hex code is pure red?", [
            C("#00FF00", why="This has green full, so it is green."),
            C("#0000FF", why="This has blue full, so it is blue."),
            C("#FF0000", correct=True),
            C("#FFFFFF", why="All three colours at full make white."),
        ], steps=[S("Read the three pairs", text="Order is red, green, blue."),
                  S("Match", text="Red full and the others zero is #FF0000.")],
           concept="Hex colours", skill="Concept", hint="The first pair is the amount of red."),
        MC("Which declaration removes the underline from links?", [
            C("text-decoration: underline;", why="This adds an underline."),
            C("text-align: none;", why="text-align controls left, centre or right. It has nothing to do with underlines."),
            C("font-style: none;", why="font-style sets italic or normal. It does not change underlines."),
            C("text-decoration: none;", correct=True),
        ], steps=[S("Pick the property", text="Underlines are text decorations."),
                  S("Pick the value", text="none removes the decoration.")],
           concept="Typography", skill="Application", hint="Underlines are a kind of text decoration."),
        NUM("In a hex colour, each pair of digits runs from 00 to FF. What is FF in decimal?", 255,
            steps=[S("Convert", text="F is 15 in decimal. FF = 15 x 16 + 15."),
                   S("Calculate", text="15 x 16 = 240, and 240 + 15 = 255.")],
            concept="Hex colours", skill="Calculation", hint="F stands for 15 and the first digit is worth 16 times as much."),
        MC('Look at this CSS and HTML. CSS: .alert, #total { color: red; }. HTML: <p class="alert">Fees</p> <p>Receipt</p> <p id="total">Due</p> <p class="alert">Exam</p>. Which paragraphs are red?', [
            C("Fees and Due only", why="The second paragraph with class alert, Exam, is also selected."),
            C("Fees, Due and Exam", correct=True),
            C("All four paragraphs", why="Receipt has neither the class alert nor the id total, so it is not selected."),
            C("Due only", why="The class selector also matches every element with class alert."),
        ], steps=[S("Read the grouped selector", text=".alert and #total are both selected, separated by a comma."),
                  S("Match", text="Fees and Exam have class alert. Due has id total. Receipt has neither.")],
           concept="Class, id and grouping", skill="Reasoning", hint="Find every element with class alert, and every element with id total."),
    ]))

# ------------------------------------------------------------------ 7. The box model and simple layout
SETS.append(practice_set(
    module=MODULE, topic=CSS,
    title="Box model, display and layout", lesson="css-box-model-display-layout",
    questions=[
        MC("In the CSS box model, which part is the space between the content and the border?", [
            C("Margin", why="Margin is outside the border."),
            C("Padding", correct=True),
            C("Display", why="display decides whether an element is block or inline. It is not part of the box."),
            C("Border", why="The border is the line around the padding."),
        ], steps=[S("Order the parts", text="From the inside out: content, padding, border, margin.")],
           concept="Box model parts", skill="Recall", hint="From the inside out: content, then which one?"),
        MC("Which element is a block element by default?", [
            C("<p>", correct=True),
            C("<span>", why="span is inline: it stays inside a line of text."),
            C("<a>", why="a is inline by default."),
            C("<em>", why="em is inline."),
        ], steps=[S("Recall", text="Block elements such as p, h1 and div start on a new line and fill the width.")],
           concept="Block and inline", skill="Recall", hint="Which one starts on a new line?"),
        MC("Which CSS centres a block that has a width of 500px?", [
            C("text-align: center;", why="This centres text inside an element. It does not move the block itself."),
            C("display: center;", why="center is not a value of display."),
            C("margin: 0 auto;", correct=True),
            C("padding: auto;", why="Padding is inside the border. Auto margins are what centre a block."),
        ], steps=[S("Use automatic margins", text="Left and right margins set to auto share the leftover space equally.")],
           concept="Centring a block", skill="Application", hint="The leftover space is shared by the left and right margins."),
        MC("What does box-sizing: border-box do?", [
            C("It removes the border", why="It does not remove anything. It changes how width is counted."),
            C("It adds a border to every element", why="The border property does that. box-sizing only changes how width is counted."),
            C("It turns the element into an inline element", why="Block or inline is set with the display property."),
            C("It makes padding and border count inside the width", correct=True),
        ], steps=[S("Compare the two ways", text="By default width is the content only. With border-box it includes padding and border.")],
           concept="box-sizing", skill="Concept", hint="Think about what width includes with it."),
        NUM("A box has content width 200px, padding 20px and border 5px on every side, with the default box sizing. What is the width of the visible box in pixels?", 250,
            steps=[S("Add padding on both sides", text="20 + 20 = 40."),
                   S("Add border on both sides", text="5 + 5 = 10."),
                   S("Add the content", text="200 + 40 + 10 = 250 pixels.")],
            unit="px", concept="Width calculation", skill="Calculation", hint="Padding and border are on the left and also on the right."),
        MC("A box has content width 120px, padding 10px, border 1px and margin 5px, all on every side, with the default box sizing. How much horizontal space does the box use, including its margins?", [
            C("120 pixels", why="That is only the content width."),
            C("142 pixels", why="That is the visible box (120 + 20 + 2). The margins use extra space."),
            C("152 pixels", correct=True),
            C("136 pixels", why="You counted the padding, border and margin on one side only."),
        ], steps=[S("Visible box", text="120 + 2 x 10 + 2 x 1 = 120 + 20 + 2 = 142."),
                  S("Add the margins", text="2 x 5 = 10, so 142 + 10 = 152 pixels.")],
           concept="Width calculation", skill="Calculation", hint="First find the visible box, then add the margins on both sides."),
        NUM("With box-sizing: border-box, a box has width 300px, padding 20px and border 5px on every side. What is the content width in pixels?", 250,
            steps=[S("Take padding and border from the width", text="Padding on both sides is 40 and border on both sides is 10."),
                   S("Subtract", text="300 - 40 - 10 = 250 pixels.")],
            unit="px", concept="box-sizing", skill="Calculation", hint="With border-box, padding and border are part of the width."),
        MC("A page has a menu column and a main column side by side. Which pair of widths could they use so they fit exactly in one row?", [
            C("30% and 80%", why="30 + 80 = 110, which is more than 100 percent, so the second column drops below."),
            C("30% and 70%", correct=True),
            C("50% and 60%", why="50 + 60 = 110, which is more than 100 percent."),
            C("20% and 90%", why="20 + 90 = 110, which is more than 100 percent."),
        ], steps=[S("Add the widths", text="The two widths must add up to 100 percent or less."),
                  S("Check each option", text="Only 30 + 70 = 100 fits exactly.")],
           concept="Two-column layout", skill="Application", hint="Add the two percentages in each option."),
    ]))
