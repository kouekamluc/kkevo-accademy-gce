"""Form 5 ICT: Web Design & Publishing (6 lessons, one practice set each)."""

from .dsl import *  # noqa: F403

COURSE = ("ict", "form-5")

MODULE = "Web Design & Publishing"
HTML = "HTML5 structure"
CSS = "CSS styling"

LESSONS = []

# ------------------------------------------------------------------ 1. Planning and building your first page
LESSONS.append(lesson(
    module=MODULE,
    topic=HTML,
    title="Planning and building your first web page",
    slug="web-plan-and-first-page",
    minutes=20,
    summary="Plan a small website on paper, then build its first page with the html, head, title and body structure, headings and paragraphs, and test it in a browser.",
    objectives=[
        "Explain what a website and a web page are and plan a small site on paper",
        "Write the basic structure of an HTML5 page: doctype, html, head, title and body",
        "Add headings and paragraphs and close every tag in the correct order",
        "Save a page as an .html file and test it in a browser, refreshing after each change",
    ],
    key_concepts=["Website", "Web page", "HTML", "Tag", "Element", "Web browser", "Page title"],
    blocks=[
        H("Introduction"),
        T("Mama Ngono sells cakes, beignets and meat pies from a small shop in Akwa, Douala. "
          "Every day customers ask the same questions: what do you sell, how much is it, and when are you open?\n\n"
          "A web page can answer these questions all day, even when the shop is closed. "
          "In this lesson you will build the first page of her website. "
          "You need only a text editor, such as Notepad, and a web browser. "
          "You do not need an internet connection to build and test a page."),
        D("A **website** is a group of web pages that belong together, usually linked to each other. "
          "A **web page** is one document you open in a **web browser** such as Chrome, Firefox or Edge. "
          "Web pages are written in **HTML** (HyperText Markup Language), which marks up the content with **tags**.",
          title="Definitions"),
        H("Plan before you type"),
        T("Good web designers do not start by typing. They first decide what the site is for and who will read it. "
          "A pencil and a sheet of paper are enough."),
        KEY("Four questions for your plan", "Answer these on paper before you open the editor.", cards=[
            ["1. Purpose", "What should the site do? For example: tell people what the shop sells and where it is."],
            ["2. Readers", "Who will visit? Customers on phones, with slow connections? Parents? Tourists?"],
            ["3. Pages", "Which pages do you need? Keep a small site small: usually three to five pages."],
            ["4. Content", "What goes on each page: text, pictures, a price list, a phone number?"],
        ]),
        EX("Worked example 1: a paper plan for Ngono Pastries", intro=(
            "Make a plan for the Ngono Pastries website. The owner wants customers to see what she sells, "
            "see the prices and find her shop."), steps=[
            S("Write the purpose", text="Help customers learn what Ngono Pastries sells and how to reach the shop."),
            S("Name the readers", text="Customers in Douala who look on a phone, often on a slow connection."),
            S("List the pages", text="Home (index.html), Menu (menu.html) and Contact (contact.html)."),
            S("List the content of each page", text="Home: shop name, a short welcome, opening hours. Menu: products and prices. Contact: address and phone number."),
            S("Draw a sketch", text="Draw a box for each page and arrows for the links between them. The sketch is your map."),
        ]),
        H("The structure of every HTML5 page"),
        T("Every HTML page has the same skeleton. A tag such as <p> opens an **element** and a closing tag such as </p> ends it. "
          "Elements can sit inside other elements, which makes a family tree."),
        IMG("f5i-html-page-tree.svg",
            alt="Tree diagram: html contains head and body. Head contains meta and title. Body contains h1, p and ul.",
            caption="Figure 1. The html element holds two children: head (information about the page) and body (what visitors see)."),
        KEY("What each part does", "Learn these five parts.", cards=[
            ["<!DOCTYPE html>", "The first line. It tells the browser this is an HTML5 page."],
            ["<html>", "Wraps the whole page. Everything else sits inside it."],
            ["<head>", "Information about the page that is not shown in the page itself."],
            ["<title>", "Goes inside the head. Shown on the browser tab and in search results."],
            ["<body>", "Everything that visitors see: headings, text, pictures, links."],
        ]),
        CODE("""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Ngono Pastries - Douala</title>
  </head>
  <body>
    <h1>Ngono Pastries</h1>
    <p>Fresh cakes, beignets and meat pies in Akwa, Douala.</p>
  </body>
</html>
""", "html", title="Listing 1: the smallest useful page (index.html)",
             caption="The meta line with UTF-8 lets the browser show accents such as e with an acute accent correctly. The lang attribute tells the browser the page is in English."),
        H("Headings and paragraphs"),
        T("Use **headings** to give the page an outline. <h1> is the main heading: use it once per page. "
          "<h2> is for sections, <h3> for parts of a section, down to <h6>. "
          "Choose a heading level for its meaning, not because it looks big or small. CSS controls the looks later.\n\n"
          "Use <p> for each paragraph. The browser adds space between paragraphs. "
          "Use <br> only when you need a line break inside a paragraph, such as in an address."),
        EX("Worked example 2: build, save and test the page", intro=(
            "Create index.html for Ngono Pastries with the title Ngono Pastries - Douala, a main heading, "
            "a welcome paragraph, a level 2 heading called Opening hours and a paragraph with the hours."), steps=[
            S("Create a folder", text="Make a folder called ngono-site on the desktop. All the files of the site will live here."),
            S("Type the skeleton", text="Open Notepad. Type the first lines of Listing 1 from the doctype to the opening body tag."),
            S("Add the content", text="Between the body tags type the h1, the welcome p, then <h2>Opening hours</h2> and <p>Monday to Saturday, 7 am to 7 pm.</p>."),
            S("Save with the right name", text="Choose File, Save As. Set Save as type to All files, type the name index.html and choose UTF-8 encoding."),
            S("Open in the browser", text="Double-click index.html in the folder. The page opens in your default browser."),
            S("Edit and refresh", text="Change a word in Notepad, save, then press F5 in the browser. The browser shows only the last saved version."),
        ]),
        TIP("Turn on file extensions in File Explorer (View, Show, File name extensions). "
            "Then you can see at once whether your file is called index.html or by mistake index.html.txt."),
        H("Common mistakes"),
        MISTAKE("Saving as index.html.txt", "Notepad may add .txt after the name. Choose Save as type: All files and check the name ends in .html only."),
        MISTAKE("Closing tags in the wrong order", "The last tag opened must be the first one closed. <p><strong>Hi</strong></p> is correct. <p><strong>Hi</p></strong> is wrong."),
        QUIZ("Where do you put the <title> element?",
             ["Inside the body", "Inside the head", "Before the doctype line", "Inside the h1 element"], 1,
             "The title is information about the page, so it goes in the head. The browser shows it on the tab.",
             hint="Is the title shown inside the page or on the tab?",
             feedback=["Text in the body is shown in the page. The title is shown on the browser tab.", "",
                       "Nothing goes before the doctype line, which must come first.",
                       "A heading is content in the body, and title is a separate element in the head."]),
        QUIZ("You change a word in Notepad but the browser still shows the old word. What should you do first?",
             ["Delete the file and type the page again", "Save the file in Notepad, then press F5 in the browser",
              "Connect to the internet", "Change the heading level"], 1,
             "The browser shows the last saved version. Save in Notepad, then refresh the browser.",
             hint="Where does the browser get the page from?",
             feedback=["Retyping is not needed; the file is fine.", "",
                       "Pages saved on your computer open without the internet.",
                       "The heading level has nothing to do with old text showing."]),
        H("Practice questions"),
        PQ("A school club in Buea wants a website to advertise its meetings. Write four questions the club should answer on paper before building it.",
           "Any four of: What is the purpose of the site (advertise meetings)? Who are the readers (students, parents)? "
           "Which pages are needed (home, meetings, contact)? What goes on each page (dates, place, a contact number)? "
           "A sketch of the pages and the links between them is also a good answer."),
        PQ("Name the part of the page that each line belongs to: (a) the line <title>Ngono Pastries</title> (b) the line <h1>Welcome</h1>. State what the visitor sees.",
           "(a) It belongs in the head. The visitor sees the text Ngono Pastries on the browser tab, not in the page. "
           "(b) It belongs in the body. The visitor sees the word Welcome as the main heading of the page."),
        PQ("Find and correct the mistakes: <html><body><h1>My shop<p>We sell cakes.</h1></p></body></html>",
           "The h1 is never closed before the p starts, and the closing tags are in the wrong order. Correct: "
           "<h1>My shop</h1><p>We sell cakes.</p>. The page also needs a doctype, a head and a title."),
        PQ("Describe how to save a page you typed in Notepad and open it in a browser. Say how you see a later change.",
           "Choose File, Save As. Set Save as type to All files and type a name that ends in .html, such as index.html. "
           "Double-click the file to open it in the browser. After you change the code, save the file again and refresh the browser with F5."),
        SUM("A website is a group of linked web pages. Plan it on paper first: purpose, readers, pages and content.",
            "Every HTML5 page starts with the doctype, then html containing head and body.",
            "The title goes in the head and shows on the browser tab. Visible content goes in the body.",
            "Use h1 once for the main heading, h2 and below for sections, and p for paragraphs.",
            "Save as .html, open in a browser, and after each change save and refresh. Close tags in reverse order."),
    ],
))

# ------------------------------------------------------------------ 2. Links, images, lists and media
LESSONS.append(lesson(
    module=MODULE,
    topic=HTML,
    title="Links, images, lists and media",
    slug="web-links-images-lists-media",
    minutes=22,
    summary="Link pages together with relative and external links, add images with alt text and sensible file sizes, write lists, and meet the audio and video elements.",
    objectives=[
        "Write hyperlinks between your own pages and to other websites",
        "Insert an image with src, alt and width, keeping the files in the right folder",
        "Choose image sizes and formats that load quickly on a slow connection",
        "Write unordered and ordered lists and describe the audio and video elements",
    ],
    key_concepts=["Hyperlink", "href", "Relative address", "Alt text", "Image file size", "Ordered list", "Unordered list", "Audio and video elements"],
    blocks=[
        H("Introduction"),
        T("In the previous lesson you built index.html for Ngono Pastries. "
          "A single page is not yet a website. Customers need to move from the home page to the menu and to the contact page.\n\n"
          "Today you will link the pages together, add a photograph of the cakes, and list the products. "
          "You will also learn why picture size matters when many of your visitors use a phone on a slow connection."),
        H("Hyperlinks"),
        D("A **hyperlink** (link) is text or a picture that takes the visitor to another page when clicked. "
          "It is written with the anchor element <a>. The **href** attribute holds the address to go to; "
          "the text between the tags is what the visitor clicks.", title="Definition"),
        KEY("Two kinds of address", "The address in href depends on where the other page is.", cards=[
            ["Link to your own page", "Give only the file name if it is in the same folder: href=\"menu.html\". This is a relative address."],
            ["Link to another website", "Give the full address, starting with https://, for example href=\"https://www.example.com\"."],
            ["Link into a folder", "Give the path: href=\"pages/menu.html\" means the file menu.html inside the folder pages."],
            ["Link to a phone number", "href=\"tel:+237600000000\" lets a visitor on a phone tap to call. Use the real number."],
        ]),
        EX("Worked example 1: link the three pages", intro=(
            "The folder ngono-site holds index.html, menu.html and contact.html. "
            "Add a row of links to the top of the body of every page so that visitors can go to any page, "
            "then add a link to a news website."), steps=[
            S("Pick the text", text="Use clear words that say where the link goes: Home, Menu, Contact."),
            S("Write the three links", text="<a href=\"index.html\">Home</a>, <a href=\"menu.html\">Menu</a> and <a href=\"contact.html\">Contact</a>. The names must match the file names exactly."),
            S("Copy them to every page", text="Paste the same row at the top of menu.html and contact.html, so the visitor can always go back."),
            S("Add the outside link", text="Write <a href=\"https://www.example.com\">Read the news</a>. An outside link needs the full address."),
            S("Test every link", text="Open each page in the browser and click each link. Fix any link that shows an error."),
        ]),
        CODE("""
<p>
  <a href="index.html">Home</a> |
  <a href="menu.html">Menu</a> |
  <a href="contact.html">Contact</a>
</p>
<p><a href="tel:+237600000000">Call the shop</a></p>
""", "html", title="Listing 1: links at the top of every page",
             caption="The telephone number is an example. Use the real number of the business."),
        H("Images and alt text"),
        T("The <img> element shows a picture. It has no closing tag. It needs three attributes in practice:\n\n"
          "**src**: the file name or path of the picture. **alt**: a short text that describes the picture. "
          "**width**: how wide to show the picture, in pixels.\n\n"
          "The alt text is read aloud to visitors who cannot see the image. "
          "It is also shown when the picture does not load, which happens often on a poor connection. "
          "Describe what the picture shows, in a few words."),
        CODE("""
<img src="images/cakes.jpg" alt="Tray of fresh cakes at Ngono Pastries" width="300">
""", "html", title="Listing 2: an image stored in a folder called images",
             caption="Keep the pictures in an images folder inside ngono-site, and write src=\"images/cakes.jpg\"."),
        H("Image file size on slow connections"),
        T("A photo taken with a phone camera can be several megabytes (MB). "
          "A visitor must download the whole file before it appears. On a slow connection, a heavy page takes a long time, "
          "costs the visitor mobile data, and many visitors leave.\n\n"
          "Making the picture small on the screen with width does not make the file smaller. "
          "You must resize the picture itself before you put it on the site."),
        KEY("How to keep pictures light", "Do these before you add a picture to the page.", cards=[
            ["Resize", "A picture shown 300 pixels wide does not need to be 4000 pixels wide. Resize it in a photo editor or on the phone."],
            ["Choose the format", "Use JPG for photographs. Use PNG for logos and drawings with flat colours."],
            ["Compress", "Save the JPG at a lower quality. Stop when the picture still looks good."],
            ["Use fewer pictures", "Five good pictures are better than twenty heavy ones."],
        ]),
        EX("Worked example 2: how much will a page download?", intro=(
            "Mama Ngono's page has 5 photographs, each 2 MB straight from the phone. "
            "After resizing and compressing, each is about 200 KB. Take 1 MB = 1000 KB. "
            "Compare the total download before and after."), steps=[
            S("Before: total in MB", text="5 photographs x 2 MB = 10 MB."),
            S("After: total in KB", text="5 photographs x 200 KB = 1000 KB."),
            S("Change 1000 KB to MB", text="1000 KB = 1 MB."),
            S("Compare", text="10 MB divided by 1 MB = 10. The page downloads 10 times less data, so it opens much faster and costs the visitor less data."),
        ]),
        H("Lists, audio and video"),
        T("Use a list when you have several short items. "
          "<ul> makes an **unordered list** with bullets, for items in no special order. "
          "<ol> makes an **ordered list** with numbers, for steps that must be done in order. "
          "Each item is written inside <li>."),
        CODE("""
<h2>Our products</h2>
<ul>
  <li>Beignets</li>
  <li>Meat pies</li>
  <li>Birthday cakes</li>
</ul>

<h2>How to order</h2>
<ol>
  <li>Choose your cake from the menu.</li>
  <li>Call the shop.</li>
  <li>Collect the cake at the shop.</li>
</ol>
""", "html", title="Listing 3: one bulleted list and one numbered list"),
        T("HTML5 can play sound and film without extra software. "
          "<audio> plays a sound file and <video> plays a film. Add the word controls so that the visitor gets play and pause buttons. "
          "The file is named in the src attribute, in the same way as for an image.\n\n"
          "Sound and video files are much larger than pictures. A short film can be many megabytes. "
          "For a site with slow-connection visitors, use them rarely, keep clips short, and never start them automatically."),
        CODE("""
<audio controls src="sounds/welcome.mp3">
  Your browser does not support audio.
</audio>

<video controls width="320" src="films/shop-tour.mp4">
  Your browser does not support video.
</video>
""", "html", title="Listing 4: the audio and video elements",
             caption="The text inside the elements is shown only by old browsers that cannot play the file."),
        H("Common mistakes"),
        MISTAKE("Wrong file name in a link or image", "Compare the name in href or src with the real file name letter by letter. Capital letters and the extension must match."),
        MISTAKE("Shrinking with width only", "width changes the size on the screen. The visitor still downloads the full file. Resize the file itself."),
        QUIZ("Which line links the text Menu to the file menu.html in the same folder?",
             ["<a src=\"menu.html\">Menu</a>", "<a href=\"menu.html\">Menu</a>", "<a href=\"Menu\">menu.html</a>", "<link href=\"menu.html\">Menu</link>"], 1,
             "A link uses the anchor element with the address in href and the clickable text between the tags.",
             hint="Which attribute holds the address of a link?",
             feedback=["src is for images, audio and video. A link uses href.", "",
                       "The address and the clickable text are swapped.",
                       "The link element is not for clickable text. Clickable links use a."]),
        QUIZ("A shop page loads very slowly on phones. It has four photographs of 3 MB each, shown with width=\"200\". What is the best fix?",
             ["Make the width smaller, such as 100", "Delete the alt text", "Resize and compress the photographs before adding them", "Change the photographs to a numbered list"], 2,
             "The visitor downloads the whole file, whatever width is set. The fix is to make the files themselves smaller.",
             hint="Does width change the size of the file?",
             feedback=["A smaller width changes only how big the picture looks. The file is still 3 MB.",
                       "Alt text is tiny and is not the cause of the delay. It also helps visitors.", "",
                       "A list shows text items. It does not make photographs lighter."]),
        H("Practice questions"),
        PQ("Write the HTML for a link with the text Our prices that opens prices.html, which is in the same folder.",
           "<a href=\"prices.html\">Our prices</a>. The address goes in href and the clickable text goes between the tags."),
        PQ("Write the HTML to show the picture file logo.png, which is inside the folder images, with a width of 150 pixels and a suitable alt text for a bakery called Ngono Pastries.",
           "<img src=\"images/logo.png\" alt=\"Ngono Pastries logo\" width=\"150\">. The path includes the folder name, and the alt text says what the picture shows."),
        PQ("A web page has 6 pictures of 1.5 MB each. After resizing each is 150 KB. Take 1 MB = 1000 KB. How much data does the page download before and after?",
           "Before: 6 x 1.5 MB = 9 MB. After: 6 x 150 KB = 900 KB, which is 0.9 MB. The page is 10 times lighter, because 9 divided by 0.9 = 10."),
        SUM("A link is <a href=\"address\">text</a>. Use only the file name for a page in the same folder, and the full https address for another website.",
            "An image is <img src=\"file\" alt=\"description\" width=\"300\">. Write useful alt text. Images need no closing tag.",
            "Resize and compress pictures before using them: width on the page does not make the file smaller.",
            "Use ul for bullet lists, ol for numbered steps, and li for each item.",
            "audio and video need controls and a src. They are heavy, so use them rarely on slow connections."),
    ],
))

# ------------------------------------------------------------------ 3. Tables and forms
LESSONS.append(lesson(
    module=MODULE,
    topic=HTML,
    title="Tables and forms for a small business",
    slug="web-tables-and-forms-for-business",
    minutes=24,
    summary="Build a price list with an HTML table and an order form with labelled input fields and a submit button, and explain in simple terms where the form data goes.",
    objectives=[
        "Build a table with table, tr, th and td and give it a caption",
        "Build a form with labelled text, telephone and number fields, a drop-down list and a submit button",
        "Link each label to its field and give every field a name",
        "Explain in simple terms what happens to form data when the button is clicked",
    ],
    key_concepts=["Table", "Table row", "Heading cell", "Form", "Input type", "Label", "Name attribute", "Submit button", "Web server"],
    blocks=[
        H("Introduction"),
        T("Ngono Pastries now has linked pages with pictures. Two jobs remain. "
          "Customers want a clear price list, and they want to order a cake without walking to the shop.\n\n"
          "Prices are a good job for a **table**, because they come in rows and columns. "
          "An order is a good job for a **form**, because the customer must type information for the shop to receive."),
        H("Tables"),
        D("An HTML **table** shows data in rows and columns. <table> holds the whole table. "
          "<tr> (table row) holds one row. <th> is a heading cell and <td> is a data cell. "
          "<caption> gives the table a title.", title="Definition"),
        T("You write a table one row at a time, from left to right. "
          "The first row usually holds the headings. Every row must have the same number of cells, "
          "or the table will look broken."),
        CODE("""
<table>
  <caption>Prices at Ngono Pastries</caption>
  <tr>
    <th>Item</th>
    <th>Price (FCFA)</th>
  </tr>
  <tr>
    <td>Meat pie</td>
    <td>300</td>
  </tr>
  <tr>
    <td>Beignets (5)</td>
    <td>500</td>
  </tr>
  <tr>
    <td>Birthday cake</td>
    <td>15000</td>
  </tr>
</table>
""", "html", title="Listing 1: a price table with three products",
             caption="Without CSS the table has no lines. You can add a quick border with table border=1, or use CSS in lesson 4."),
        EX("Worked example 1: add a row to the table", intro=(
            "Mama Ngono now sells a loaf of bread for 250 FCFA. Add it to the price table so that it appears as the last row."), steps=[
            S("Find the end of the table", text="The last row ends with </tr>, and then comes </table>."),
            S("Open a new row after the last row", text="Type <tr> between the last </tr> and </table>."),
            S("Write one cell for each column", text="The table has two columns, so write <td>Bread loaf</td> and <td>250</td>."),
            S("Close the row and test", text="Type </tr>. Save and refresh. The table shows a fourth row with two cells."),
        ]),
        H("Forms"),
        D("A **form** collects information from the visitor. <form> holds the form. Inside it, "
          "<input> and similar elements are the **fields** the visitor fills in, and a **submit button** sends the information. "
          "A <label> is the text that tells the visitor what to type in a field.", title="Definition"),
        KEY("Choose the right field", "The type attribute of <input> decides what kind of field appears.", cards=[
            ["type=\"text\"", "One line of ordinary text, such as a name."],
            ["type=\"email\"", "An email address. Phone browsers show a keyboard with the @ sign."],
            ["type=\"tel\"", "A phone number. Phone browsers show a number keyboard."],
            ["type=\"number\"", "A number, such as a quantity. Use min=\"1\" to refuse zero."],
            ["select with option", "A drop-down list: the visitor picks one item, so spelling mistakes cannot happen."],
            ["textarea", "A larger box for a long message."],
            ["type=\"submit\"", "The button that sends the form."],
        ]),
        T("Two attributes are very important.\n\n"
          "The **name** attribute gives each field a name. The shop's program receives the information as name and value pairs, "
          "such as qty and 3. A field without a name sends nothing.\n\n"
          "The **for** attribute of a label must match the **id** of its field. Then the label and the field are joined: "
          "clicking the label puts the cursor in the field, and a screen reader reads the label when the visitor reaches the field."),
        EX("Worked example 2: build the order form", intro=(
            "Build a form for Ngono Pastries. The customer gives a name and a phone number, chooses an item from a list, "
            "enters a quantity of at least 1, and clicks a button called Send order."), steps=[
            S("Open the form", text="Write <form action=\"order.php\" method=\"post\"> and close it with </form> at the end. The meaning of action and method comes below."),
            S("Add the name field", text="A label with for=\"cname\" and an input with type=\"text\", id=\"cname\" and name=\"cname\"."),
            S("Add the phone field", text="Use type=\"tel\", with id and name both equal to phone."),
            S("Add the drop-down list", text="A select with id and name equal to item, and one option for each product."),
            S("Add the quantity", text="Use type=\"number\" with min=\"1\", and id and name equal to qty."),
            S("Add the button", text="Write <input type=\"submit\" value=\"Send order\">. See Listing 2."),
        ]),
        CODE("""
<form action="order.php" method="post">
  <p>
    <label for="cname">Your name</label><br>
    <input type="text" id="cname" name="cname" required>
  </p>
  <p>
    <label for="phone">Phone number</label><br>
    <input type="tel" id="phone" name="phone">
  </p>
  <p>
    <label for="item">Item</label><br>
    <select id="item" name="item">
      <option>Meat pie</option>
      <option>Beignets (5)</option>
      <option>Birthday cake</option>
    </select>
  </p>
  <p>
    <label for="qty">Quantity</label><br>
    <input type="number" id="qty" name="qty" min="1" value="1">
  </p>
  <p>
    <label for="note">Message (optional)</label><br>
    <textarea id="note" name="note" rows="3" cols="30"></textarea>
  </p>
  <input type="submit" value="Send order">
</form>
""", "html", title="Listing 2: the order form",
             caption="The word required stops the visitor from sending the form with that field empty."),
        H("What happens to the form data?"),
        T("When the visitor clicks the submit button, the browser collects every field that has a name. "
          "It packs them as name and value pairs and sends them to the address in the form's **action** attribute. "
          "That address is a program running on a **web server**, a computer that is always connected to the internet.\n\n"
          "The program reads the pairs and does something with them: it saves the order in a file or database or sends an email. "
          "Then it sends a reply, such as a thank-you page."),
        IMG("f5i-form-data-flow.svg",
            alt="Arrow from the browser to a web server carrying name and value pairs cname, item and qty, and a reply arrow coming back.",
            caption="Figure 1. The form data travels as name and value pairs to a program on the web server, which sends back a reply."),
        KEY("get or post?", "The method attribute says how the data is sent.", cards=[
            ["get", "The data is added to the page address, where anyone can see it. Use it for searches."],
            ["post", "The data is sent inside the request and not added to the address. Use it for orders, names and phone numbers."],
        ], note="The HTML page alone cannot receive an order. A program on the server must be waiting at the action address. "
                "Your teacher or the web host will tell you which program or service to use. Without one, the Send order button does nothing useful."),
        EX("Worked example 3: repair a broken form field", intro=(
            "A student wrote this field: <label>Quantity</label> <input type=\"number\" id=\"qty\">. "
            "Customers' quantities never reach the shop, and clicking the label does nothing. Repair the field."), steps=[
            S("Find why nothing arrives", text="The input has an id but no name. Only fields with a name are sent."),
            S("Add the name", text="Write name=\"qty\" so that the program receives qty and its value."),
            S("Find why the label does not work", text="The label has no for attribute, so it is not joined to any field."),
            S("Join the label to the field", text="Write <label for=\"qty\">. It matches id=\"qty\" on the input."),
            S("Write the repaired field", text="<label for=\"qty\">Quantity</label> <input type=\"number\" id=\"qty\" name=\"qty\" min=\"1\">."),
        ]),
        H("Common mistakes"),
        MISTAKE("Fields without a name", "id is for joining the label and for CSS. Only name makes the data travel with the form."),
        MISTAKE("Rows with different numbers of cells", "If one row has two cells and the next has three, the table looks broken. Count the cells in every row."),
        QUIZ("In a price table, which element holds the word Price in the first row?",
             ["<td>", "<th>", "<tr>", "<caption>"], 1,
             "<th> is a heading cell. Use it for the labels at the top of each column.",
             hint="Which cell type is for headings?",
             feedback=["<td> is a data cell. It is used for the prices and items below the headings.", "",
                       "<tr> is the whole row, not a single cell.",
                       "<caption> is the title of the whole table, not a column heading."]),
        QUIZ("A visitor fills in and submits an order form, but the shop receives no phone number. The phone field is <input type=\"tel\" id=\"phone\">. What is the cause?",
             ["The type should be text", "The field has no name attribute", "The label is missing a closing tag", "The form should use get"], 1,
             "Only fields with a name attribute are sent. Add name=\"phone\".",
             hint="Which attribute does the browser use to send the value?",
             feedback=["type=\"tel\" is a good choice for a phone number and does not stop it from being sent.", "",
                       "A missing closing tag would break the page layout, not remove one value.",
                       "get versus post changes how the data is sent, not whether a field is sent."]),
        H("Practice questions"),
        PQ("Write the HTML for a table with the headings Garment and Price (FCFA) and one row for a Kabba at 8000.",
           "<table> <tr><th>Garment</th><th>Price (FCFA)</th></tr> <tr><td>Kabba</td><td>8000</td></tr> </table>. "
           "The heading row uses th cells and the data row uses td cells, and both rows have two cells."),
        PQ("Write the HTML for a field that asks for an email address, with the label Your email, so that clicking the label puts the cursor in the field and the value is sent to the server.",
           "<label for=\"email\">Your email</label> <input type=\"email\" id=\"email\" name=\"email\">. "
           "The for value matches the id, which joins the label to the field, and the name makes the value travel with the form."),
        PQ("Explain in simple terms what happens when a customer clicks Send order on a form whose action is order.php and method is post.",
           "The browser collects every field that has a name and packs the values as name and value pairs. "
           "It sends them to order.php, a program on a web server. The program reads the pairs, saves or sends the order, "
           "and replies, for example with a thank-you page. With post, the data is not shown in the page address."),
        SUM("A table uses table, tr, th and td. Every row needs the same number of cells.",
            "A form holds fields (input, select, textarea), labels and a submit button.",
            "Choose the input type for the data: text, email, tel, number. Use a select list for a fixed choice.",
            "Give every field a name, and join each label to its field with for and id.",
            "On submit, the browser sends name and value pairs to the action address, where a server program receives them. Use post for orders."),
    ],
))

# ------------------------------------------------------------------ 4. Styling a page with CSS
LESSONS.append(lesson(
    module=MODULE,
    topic=CSS,
    title="Styling a page with CSS",
    slug="css-style-pages-and-keep-a-consistent-look",
    minutes=22,
    summary="Write CSS rules with selectors, properties and values to set colours, fonts and text, and keep one look across all pages with an external style sheet.",
    objectives=[
        "Write a CSS rule made of a selector and declarations",
        "Choose between inline, internal and external CSS",
        "Style elements with element, class and id selectors",
        "Set text colour, background colour, font and alignment, and use one style sheet for every page",
    ],
    key_concepts=["CSS", "Selector", "Property and value", "Inline CSS", "Internal CSS", "External style sheet", "Class", "Id"],
    blocks=[
        H("Introduction"),
        T("The Ngono Pastries website has three pages: Home, Menu and Contact. "
          "They work well, but they look plain: black text on a white page. "
          "Mama Ngono wants her shop colours, brown and cream, and the same font on every page.\n\n"
          "HTML says what each part of a page **is**: a heading, a paragraph, a list. "
          "**CSS** says how each part should **look**. Keeping the two apart makes the work easier to change."),
        D("**CSS** (Cascading Style Sheets) is the language that controls colours, fonts, sizes, spacing and layout of HTML elements. "
          "A CSS **rule** has a **selector** that chooses what to style, and **declarations** in curly brackets. "
          "Each declaration is a **property**, a colon, a **value** and a semicolon.", title="Definition"),
        CODE("""
body {
  background-color: cornsilk;
  color: #333333;
  font-family: Arial, Helvetica, sans-serif;
}
""", "css", title="Listing 1: one rule with three declarations",
             caption="Selector: body. Properties: background-color, color and font-family. Each declaration ends with a semicolon."),
        H("Three places to write CSS"),
        KEY("Inline, internal, external", "The same rule can live in three places.", cards=[
            ["Inline", "A style attribute on one tag: <p style=\"color: red;\">. It changes that one element only. Use it rarely."],
            ["Internal", "A <style> element inside the head of one page. It styles that page only."],
            ["External", "A separate file such as style.css, linked from the head of every page. One file styles the whole site."],
        ], note="If rules clash, inline CSS wins over internal and external CSS. Among rules of equal strength, the one written last wins."),
        CODE("""
<!-- Inline: on the element -->
<p style="color: red;">Offer today only</p>

<!-- Internal: in the head of one page -->
<head>
  <title>Ngono Pastries</title>
  <style>
    h1 { color: saddlebrown; }
  </style>
</head>

<!-- External: a link in the head of every page -->
<head>
  <title>Ngono Pastries</title>
  <link rel="stylesheet" href="style.css">
</head>
""", "html", title="Listing 2: the three ways to add CSS"),
        EX("Worked example 1: style one page with internal CSS", intro=(
            "Make the home page of Ngono Pastries have a cream background, dark grey text and a centred brown main heading."), steps=[
            S("Open the head", text="In index.html find the <head> section, after the title line."),
            S("Add a style element", text="Type <style> and </style> inside the head."),
            S("Write the body rule", text="Inside the style element write body { background-color: cornsilk; color: #333333; }."),
            S("Write the heading rule", text="Add h1 { color: saddlebrown; text-align: center; }."),
            S("Save and refresh", text="The page now has a cream background and a centred brown heading. Only this page changed."),
        ]),
        H("An external style sheet for the whole site"),
        T("If you copy the same <style> block into every page, a change means editing every page. "
          "Better: put the rules in one file called style.css and link it from every page. "
          "Change the file once and all the pages change.\n\n"
          "A style sheet contains only CSS: no HTML tags and no style element. "
          "Save it in the same folder as the pages, for example ngono-site/style.css."),
        EX("Worked example 2: move the rules into style.css", intro=(
            "The rules from the last example are inside index.html. Move them into an external style sheet and use it on index.html, menu.html and contact.html."), steps=[
            S("Create the file", text="In Notepad, choose Save As, choose All files and type the name style.css in the ngono-site folder."),
            S("Move the rules", text="Cut the two rules from the style element of index.html and paste them into style.css."),
            S("Remove the old style element", text="Delete the empty <style> and </style> lines from index.html."),
            S("Link the sheet", text="In the head of every page write <link rel=\"stylesheet\" href=\"style.css\">."),
            S("Test all three pages", text="Open Home, Menu and Contact. All three have the same background and heading style."),
        ]),
        H("Selectors: choosing what to style"),
        KEY("Three common selectors", "A selector decides which elements a rule applies to.", cards=[
            ["Element", "h1 { ... } styles every h1 on the page. Write the tag name."],
            ["Class", ".price { ... } styles every element with class=\"price\". Reusable. Start with a full stop in CSS only."],
            ["Id", "#logo { ... } styles the one element with id=\"logo\". An id must be used once per page. Start with a hash."],
        ]),
        CODE("""
.price {
  font-weight: bold;
  color: firebrick;
}
""", "css", title="Listing 3: a class rule (in style.css)"),
        CODE("""
<table>
  <tr><td>Meat pie</td><td class="price">300</td></tr>
  <tr><td>Birthday cake</td><td class="price">15000</td></tr>
</table>
""", "html", title="Listing 4: using the class in the HTML",
             caption="In the HTML write class=\"price\" without the full stop."),
        H("Colours, fonts and text"),
        T("A colour value can be a name, such as saddlebrown or cornsilk, or a code that starts with #. "
          "For example #8B4513 is saddlebrown and #FFF8DC is cornsilk. Colour names are easier to remember. "
          "Codes give you thousands of choices.\n\n"
          "Useful text properties are color for the text colour, background-color, font-family, font-size, "
          "font-weight (normal or bold), font-style (italic), text-align (left, center or right), "
          "text-decoration (none removes the underline of links) and line-height."),
        EX("Worked example 3: finish the look of the site", intro=(
            "Add to style.css: paragraphs with font size 18px and line height 1.5; links in saddlebrown with no underline; a class called price that is bold and dark red."), steps=[
            S("Write the paragraph rule", text="p { font-size: 18px; line-height: 1.5; }"),
            S("Write the link rule", text="a { color: saddlebrown; text-decoration: none; }"),
            S("Write the class rule", text=".price { font-weight: bold; color: firebrick; }"),
            S("Use the class in the HTML", text="Add class=\"price\" to the price cells, then save the CSS and the HTML and refresh each page."),
        ]),
        H("Common mistakes"),
        MISTAKE("The style sheet is not linked", "If nothing changes, check that the link element is in the head, that href matches the file name exactly, and that style.css is in the right folder."),
        MISTAKE("Forgetting the colon or semicolon", "Write property, colon, value, semicolon. One missing semicolon can make the next declaration fail."),
        QUIZ("A website has 12 pages that must share the same colours and fonts. Which is the best way?",
             ["Inline styles on every element", "A style element in the head of each page", "One external style sheet linked from every page", "Make each page look similar by eye"], 2,
             "One external sheet means one place to change. All 12 pages follow it.",
             hint="Which method lets you change one file instead of twelve?",
             feedback=["Inline styles must be repeated on every element and are very slow to change.",
                       "You would have to copy the block into 12 pages and update all 12 for every change.", "",
                       "Pages made by eye drift apart. CSS applies the same rules exactly."]),
        QUIZ("Which rule makes every element with class=\"note\" italic?",
             ["#note { font-style: italic; }", ".note { font-style: italic; }", "note { font-style: italic; }", ".note { font-style: italique; }"], 1,
             "A class selector starts with a full stop in CSS, and italic is written font-style: italic.",
             hint="What character starts a class selector?",
             feedback=["A hash starts an id selector, for the one element with id=\"note\".", "",
                       "Without a full stop this selects elements called note, and there is no such HTML element.",
                       "The value must be written in English: italic."]),
        H("Practice questions"),
        PQ("State one situation where each of these is the best choice: inline CSS, internal CSS, external CSS.",
           "Inline: a one-off change to a single element on one page. Internal: one page that needs its own special style, such as a poster page. "
           "External: a website with several pages that must all share the same design."),
        PQ("Write CSS so that all paragraphs have a font size of 16px and dark grey text, and all links have no underline.",
           "p { font-size: 16px; color: #333333; } and a { text-decoration: none; }. Any dark grey value is acceptable."),
        PQ("Mama Ngono wants a heading to be centred, brown and in Arial. Write the rule for the h1 element and say where it should be written so that all her pages use it.",
           "h1 { text-align: center; color: saddlebrown; font-family: Arial, sans-serif; }. It should be written in an external style sheet, style.css, "
           "and every page should link to the sheet with <link rel=\"stylesheet\" href=\"style.css\"> in its head."),
        SUM("CSS controls how the page looks. A rule is a selector plus declarations: property, colon, value, semicolon.",
            "Inline CSS changes one element, internal CSS styles one page, external CSS styles the whole site.",
            "Link style.css from the head of every page with a link element. Change the file once to change every page.",
            "Element selectors style a tag, class selectors (.name) style chosen elements, and id selectors (#name) style one element.",
            "Use color, background-color, font-family, font-size, text-align and text-decoration. Use American spelling."),
    ],
))

# ------------------------------------------------------------------ 5. Spacing, layout and the box model
LESSONS.append(lesson(
    module=MODULE,
    topic=CSS,
    title="Spacing, layout and the box model",
    slug="css-box-model-spacing-and-page-layout",
    minutes=25,
    summary="Use padding, border, margin and width to space out content, centre a box, turn a list into a navigation bar and arrange a simple two-column page.",
    objectives=[
        "Name the four layers of the box model and calculate the total width of a box",
        "Use padding, border, margin and width to space out elements",
        "Centre text and centre a box on the page",
        "Make a navigation bar from a list and a simple two-column layout",
    ],
    key_concepts=["Box model", "Content", "Padding", "Border", "Margin", "Navigation bar", "Two-column layout"],
    blocks=[
        H("Introduction"),
        T("In the previous lesson you gave Ngono Pastries its colours and fonts. "
          "But the page still looks crowded: the text touches the edge of the screen, the links are in a plain row and everything is in one long column.\n\n"
          "In this lesson you will give each part of the page room to breathe. "
          "You will also turn the row of links into a proper menu bar and put the page into two columns."),
        H("The box model"),
        IMG("f5i-box-model.svg",
            alt="Nested rectangles: content in the middle, then padding, then a border line, then margin outside.",
            caption="Figure 1. The four layers of the box model, from the inside out: content, padding, border, margin."),
        D("The browser treats every HTML element as a rectangular box. The **box model** describes its four layers, from the inside out: "
          "**content** (the text or picture), **padding** (space between the content and the border), "
          "**border** (the line round the box) and **margin** (space outside the border, between this box and its neighbours).",
          title="Definition"),
        T("You can set the four sides separately with padding-top, padding-right, padding-bottom and padding-left (the same for margin). "
          "A shorter way is to give several values. Two values, such as padding: 10px 20px; mean top and bottom 10px, left and right 20px. "
          "Four values go round the box clockwise: top, right, bottom, left."),
        EX("Worked example 1: the offer box", intro=(
            "Style a box with id offer: content width 250px, padding 15px, a 3px solid brown border and a margin of 10px. "
            "Write the rule and calculate the total width the box takes on the page."), steps=[
            S("Choose the selector", text="One special box on the page, so use an id selector: #offer."),
            S("Write the declarations", text="width: 250px; padding: 15px; border: 3px solid saddlebrown; margin: 10px;"),
            S("Add the content and both sides of padding", text="250 + 15 + 15 = 280px."),
            S("Add both sides of the border", text="280 + 3 + 3 = 286px."),
            S("Add both sides of the margin", text="286 + 10 + 10 = 306px. The box takes 306px of the width of the page."),
        ]),
        CODE("""
#offer {
  width: 250px;
  padding: 15px;
  border: 3px solid saddlebrown;
  margin: 10px;
}
""", "css", title="Listing 1: the offer box",
             caption="In the HTML: <div id=\"offer\">Buy 5 meat pies, get 1 free!</div>. A div is a plain box with no special meaning."),
        TIP("Plain width sets the content only, so padding and border make the box wider than the width you wrote. "
            "Many designers add box-sizing: border-box; so that width includes the padding and the border. "
            "Then width: 250px; means the box is 250px wide. Its content is smaller: 250 - 30 - 6 = 214px."),
        H("Centring"),
        T("There are two different jobs.\n\n"
          "To centre **text** (or pictures) inside a box, use text-align: center; on the box.\n\n"
          "To centre a **box** on the page, give it a width and set its left and right margins to auto: margin: 0 auto;. "
          "The browser shares the free space equally on both sides. Without a width, a box fills the whole line, so there is nothing to centre."),
        CODE("""
h1 {
  text-align: center;
}

.page {
  width: 600px;
  margin: 0 auto;
  padding: 20px;
}
""", "css", title="Listing 2: centred heading text and a centred page box",
             caption="The two values of margin: 0 auto; mean zero above and below, auto on the left and right."),
        H("A navigation bar made from a list"),
        T("HTML5 has elements that name the main parts of a page: <header> for the top, <nav> for the menu links, "
          "<main> for the main content, <aside> for a side column, and <footer> for the bottom. "
          "A menu is a list of links, so write it as a <ul> with one <li> and one <a> for each page, inside <nav>. "
          "Then use CSS to remove the bullets and put the items side by side."),
        CODE("""
<nav>
  <ul>
    <li><a href="index.html">Home</a></li>
    <li><a href="menu.html">Menu</a></li>
    <li><a href="contact.html">Contact</a></li>
  </ul>
</nav>
""", "html", title="Listing 3: the menu as a list in nav"),
        CODE("""
nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
  background-color: saddlebrown;
}
nav li {
  display: inline-block;
}
nav a {
  display: block;
  padding: 12px 20px;
  color: white;
  text-decoration: none;
}
nav a:hover {
  background-color: #5c3317;
}
""", "css", title="Listing 4: styling the list as a bar",
             caption="inline-block puts the items on one row. display: block on the link makes the whole padded area clickable. a:hover styles the link when the pointer is over it."),
        EX("Worked example 2: turn the plain links into a menu bar", intro=(
            "Each page of Ngono Pastries has three links in a paragraph. Change them into a brown menu bar with white text."), steps=[
            S("Change the HTML", text="Replace the paragraph by the nav and ul of Listing 3. Do this on every page."),
            S("Remove the bullets and spacing", text="In style.css write nav ul with list-style: none; margin: 0; padding: 0;, so the list starts at the edge."),
            S("Put the items in a row", text="Write nav li { display: inline-block; }."),
            S("Make the links roomy", text="Write nav a with display: block; padding: 12px 20px; white text and no underline."),
            S("Test", text="Refresh each page. The menu is a brown bar and the whole padded area of each link can be clicked."),
        ]),
        H("A simple two-column page"),
        T("A main column for the content and a narrower side column for opening hours is a common layout. "
          "Put both inside one wrapper box, then give the wrapper display: flex;. "
          "The children then sit side by side. Give each a width as a percentage so that they share the line, for example 70% and 30%."),
        CODE("""
<div class="columns">
  <main>
    <h2>Welcome</h2>
    <p>Fresh cakes and pies every day.</p>
  </main>
  <aside>
    <h2>Opening hours</h2>
    <p>Monday to Saturday, 7 am to 7 pm.</p>
  </aside>
</div>
""", "html", title="Listing 5: two columns in the HTML"),
        CODE("""
* {
  box-sizing: border-box;
}
.columns {
  display: flex;
}
main {
  width: 70%;
  padding: 15px;
}
aside {
  width: 30%;
  padding: 15px;
  background-color: cornsilk;
}
""", "css", title="Listing 6: two columns in CSS",
             caption="The first rule is the universal selector: it applies to every element. With border-box, 70% plus 30% fits exactly in the line even with padding."),
        H("Common mistakes"),
        MISTAKE("Mixing up padding and margin", "Padding is inside the border and takes the background colour. Margin is outside the border and is always see-through."),
        MISTAKE("margin: 0 auto on a box without a width", "A box with no width already fills the line, so it cannot be centred. Give it a width first."),
        QUIZ("Which rule centres a box 600px wide in the middle of the page?",
             ["text-align: center;", "margin: 0 auto;", "padding: 0 auto;", "border: center;"], 1,
             "Equal automatic left and right margins share the free space equally. The box must have a width.",
             hint="Which property controls space outside the box?",
             feedback=["That centres the text inside the box, not the box itself.", "",
                       "padding is inside the border. It does not take auto in this way.",
                       "border does not centre anything; center is not a border value."]),
        H("Practice questions"),
        PQ("Name the four layers of the box model from the inside out, and say what each one is.",
           "Content: the text or picture itself. Padding: space between the content and the border. "
           "Border: the line round the box. Margin: space outside the border that separates the box from other boxes."),
        PQ("A box has width 400px, padding 20px, border 1px and margin 25px on all sides. Calculate its total width.",
           "400 + (2 x 20) + (2 x 1) + (2 x 25) = 400 + 40 + 2 + 50 = 492px."),
        PQ("Describe, with the CSS properties you would use, how to turn a list of three links into a horizontal menu bar.",
           "Put the links in a ul inside a nav, one li each. Remove the bullets with list-style: none and set margin and padding of the ul to 0. "
           "Put the items on one row with display: inline-block on the li. Give each link padding and display: block, a background colour, white text and text-decoration: none."),
        SUM("Every element is a box: content, then padding, border and margin. Total width adds both sides of every layer.",
            "padding is inside the border; margin is outside it. border-box makes width include padding and border.",
            "text-align: center centres text inside a box. margin: 0 auto centres a box that has a width.",
            "A menu bar is a list of links in nav, with list-style: none and the items set to inline-block.",
            "For two columns, use a wrapper with display: flex and give the columns percentage widths that add to 100%."),
    ],
))

# ------------------------------------------------------------------ 6. Accessibility and publishing
LESSONS.append(lesson(
    module=MODULE,
    topic=CSS,
    title="Designing for readers: accessibility and publishing",
    slug="web-accessible-design-and-publishing",
    minutes=22,
    summary="Make a web page easy to read and use for everyone, including visitors on phones, then test it and publish the site to a web host or a school server.",
    objectives=[
        "Choose text and background colours with enough contrast, and readable font sizes",
        "Write good alt text, page titles, headings and link text",
        "Make a page work on a phone and test it there",
        "Describe in plain terms how a site is published to a web host or a school server",
    ],
    key_concepts=["Accessibility", "Contrast", "Alt text", "Page title", "Viewport", "Web host", "Upload", "School server"],
    blocks=[
        H("Introduction"),
        T("The Ngono Pastries site now has links, pictures, a price table, an order form and a brown and cream design. "
          "Two questions remain. Can everyone read and use it? And how do customers reach it?\n\n"
          "Think about your visitors. One reads on a small phone in bright sunshine in Bonaberi. "
          "One is an older relative who cannot read small print. One cannot see the screen and listens to a screen reader. "
          "One has a slow connection that sometimes drops. A good designer thinks of all of them."),
        D("**Accessibility** means designing a page so that as many people as possible can use it, "
          "including people with poor sight, hearing or movement, people using screen readers, and people on small screens or slow connections. "
          "Most accessibility work is simply good, careful HTML and CSS.", title="Definition"),
        H("Contrast, text and good HTML"),
        T("**Contrast** is the difference in brightness between the text colour and the background colour. "
          "Low contrast, such as light grey on white, is hard to read for everyone and impossible for some. "
          "Contrast is measured as a ratio. A common guideline for normal text (WCAG) asks for at least 4.5 to 1."),
        CODE("""
Text colour   Background   Contrast   Result
#333333       white        12.6 : 1   very good
white         #8B4513      7.1 : 1    good
#767676       white        4.5 : 1    just acceptable
#999999       white        2.9 : 1    too low
#CCCCCC       white        1.6 : 1    very hard to read
""", "text", title="Table 1: some colour pairs, from a contrast checker",
             caption="Free contrast checkers on the web will test any two colours for you. Check your colours before you choose them."),
        KEY("Make the text easy to read", "Check these settings in style.css.", cards=[
            ["Size", "Use at least 16px for body text. Small text is hard to read on a phone."],
            ["Font", "Use a plain font such as Arial. Add sans-serif at the end of the list as a back-up."],
            ["Line spacing", "line-height: 1.5; gives the lines room."],
            ["Colour alone", "Do not use colour alone to give a message, such as red for a wrong answer. Add words as well."],
            ["Capitals", "Avoid long text in all capital letters. It is slower to read."],
        ]),
        KEY("What a screen reader and a search engine need", "Do these on every page.", cards=[
            ["Alt text", "Describe each picture that carries meaning. A decorative picture can have an empty alt attribute, alt=\"\"."],
            ["Page title", "Give every page its own clear title, such as Menu - Ngono Pastries. The title is the first thing a screen reader says."],
            ["Headings in order", "One h1, then h2 for sections, then h3 for parts. Do not skip levels to make text look bigger."],
            ["Clear link text", "Write Read the menu, not click here. Link text should make sense on its own."],
            ["Labels", "Join every form field to a label with for and id, as you did in lesson 3."],
        ]),
        EX("Worked example 1: repair the accessibility problems", intro=(
            "A student wrote the BEFORE page in Listing 1. Find five accessibility problems and repair them."), steps=[
            S("Page title", text="The title is just Page. Change it to Menu - Ngono Pastries."),
            S("Picture", text="The image has no alt. Add alt=\"Tray of fresh cakes\"."),
            S("Link text", text="click here says nothing. Change it to See our full menu."),
            S("Text colour", text="Light grey #999999 on white has a contrast of only 2.9 to 1. Change to #333333."),
            S("Text size", text="11px is too small. Change to 16px. See Listing 1 for the page before and after."),
        ]),
        CODE("""
<!-- BEFORE: a page with accessibility problems -->
<head>
  <title>Page</title>
  <style> p { color: #999999; font-size: 11px; } </style>
</head>
<body>
  <h1>Menu</h1>
  <img src="cakes.jpg">
  <p>Cakes, pies and beignets.
     <a href="menu.html">click here</a></p>
</body>

<!-- AFTER: the repaired page -->
<head>
  <title>Menu - Ngono Pastries</title>
  <style> p { color: #333333; font-size: 16px; } </style>
</head>
<body>
  <h1>Menu</h1>
  <img src="cakes.jpg" alt="Tray of fresh cakes">
  <p>Cakes, pies and beignets.
     <a href="menu.html">See our full menu</a></p>
</body>
""", "html", title="Listing 1: the page before and after the repair"),
        H("Designing for phones"),
        T("Most visitors will open the Ngono Pastries site on a phone. A page made for a wide computer screen can force them to scroll sideways. "
          "Three small changes help.\n\n"
          "First, add the viewport line to the head of every page. It tells a phone browser to use the real width of the phone screen."),
        CODE("""
<meta name="viewport" content="width=device-width, initial-scale=1">
""", "html", title="Listing 2: the viewport line (put it in the head)"),
        T("Second, do not fix the width of the page in pixels. A box with width: 800px is wider than a phone screen. "
          "Use max-width instead: the box is as wide as the screen but never wider than the limit.\n\n"
          "Third, stop pictures from sticking out of the screen."),
        CODE("""
.page {
  max-width: 800px;
  margin: 0 auto;
  padding: 10px;
}
img {
  max-width: 100%;
  height: auto;
}
""", "css", title="Listing 3: a page box and pictures that fit any screen",
             caption="max-width: 100% means a picture is never wider than the space it sits in. height: auto keeps its shape."),
        H("Testing before you publish"),
        KEY("A test list", "Do these checks on every page, on a computer and on a phone.", cards=[
            ["Links", "Click every link, including the links back to the home page. Fix any error page."],
            ["Pictures", "Check that every picture appears and loads quickly."],
            ["Forms", "Fill in and submit the form to make sure the answer arrives."],
            ["Phone", "Open the page on a real phone. Copy the site folder to the phone by cable, Bluetooth or memory card and open index.html, or open the real address once published. Check that you can read the text without zooming or sideways scrolling."],
            ["Narrow window", "On a computer, make the browser window narrow to see roughly how the page will look on a phone."],
            ["Read it aloud", "Read the text again for spelling mistakes and check the prices and phone number."],
        ]),
        H("Publishing a site"),
        D("So far the site exists only on your computer. To **publish** it, you copy the files to a **web server**, a computer that is connected to the internet all the time and shares them with visitors. A **web host** is a company that rents space on its web servers to keep websites online. "
          "You **upload** your site's files to the host. A visitor then reaches the site by typing its web address, "
          "which is often a **domain name** such as www.nameofshop.example.", title="Definition"),
        EX("Worked example 2: publish the Ngono Pastries site to a web host", intro=(
            "The pages and pictures are finished and tested on the computer. Describe the steps to put them on the internet."), steps=[
            S("Choose a host and a name", text="Compare hosts: ask about the price, the space, the support and whether they work well from Cameroon. Choose a short domain name that customers can remember."),
            S("Get your upload details", text="The host gives you a way to upload. It may be a file manager in a web page, or a program with an address, a user name and a password. Keep the password private."),
            S("Upload the whole folder", text="Copy index.html, menu.html, contact.html, style.css and the images folder. Keep the same folders, because the links use those paths."),
            S("Check the home page name", text="The home page file must be called index.html, because the server shows it when a visitor types only the web address."),
            S("Test the live site", text="Type the real address on a computer and on a phone. Click every link again and check the pictures."),
            S("Keep a copy and update later", text="Keep the original folder on your computer. To change the site, edit the file on your computer, test it, then upload it again."),
            S("If you use the school server instead", text="A technician gives you a folder on the school server and the address to use. Copy the same site into that folder. Only people on the school network may be able to see it, unless the server is also connected to the internet. Ask your teacher or the technician."),
        ]),
        H("Common mistakes"),
        MISTAKE("Changing the folder layout on upload", "A link to images/cakes.jpg fails if the images folder is not uploaded with the same name."),
        MISTAKE("Putting private information on a public page", "Anyone on the internet can read a published page. Never put passwords or customers' personal details in it."),
        QUIZ("Which text and background pair is the best for body text?",
             ["Light grey text on white", "Yellow text on white", "Dark grey text on cream", "White text on orange"], 2,
             "Dark grey on cream has strong contrast, around 12 to 1. The other pairs have low contrast, below the 4.5 to 1 guideline.",
             hint="Which pair has the biggest difference in brightness?",
             feedback=["Light grey on white is faint, about 2.9 to 1 or lower.",
                       "Yellow on white is almost invisible: its ratio is only about 1.1 to 1.", "",
                       "White on bright orange is also too weak, with a ratio of about 2 to 1."]),
        H("Practice questions"),
        PQ("State four things you can do to make a web page more accessible.",
           "Any four of: use enough contrast between text and background; use at least 16px text and a plain font; write alt text for pictures; "
           "give each page a clear title; use headings in order; write clear link text instead of click here; join form fields to labels; make the page fit a phone screen."),
        PQ("Write the line that you add to the head of a page so that it fits a phone screen, and write the CSS that stops a picture from being wider than its space.",
           "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"> in the head, and img { max-width: 100%; height: auto; } in the CSS."),
        PQ("A student wants to publish a site for a school club. Put these steps in the correct order: test the live site, upload the files, choose a host, get the upload details.",
           "Choose a host, get the upload details, upload the files, test the live site."),
        SUM("Accessible design helps everyone: strong contrast (at least 4.5 to 1 for normal text), body text of at least 16px, and a plain font.",
            "Write alt text, a clear page title for every page, headings in order, clear link text, and labels for form fields.",
            "For phones add the viewport line, use max-width instead of a fixed width, and give images max-width: 100%.",
            "Test every link, picture and form on a computer and on a phone before publishing.",
            "To publish, upload the whole site, with its folders, to a web host or school server. The home page must be index.html. Test the live address."),
    ],
))
