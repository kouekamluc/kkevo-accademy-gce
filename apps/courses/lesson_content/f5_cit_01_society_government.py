"""Form 5 Citizenship Education, part 1: the citizen in social and community life, administrative organization, constitutional and political organization. 14 lessons, one practice set each."""

from .dsl import *  # noqa: F403

COURSE = ("citizenship-education", "form-5")

M1 = "The Citizen in Social & Community Life"
M2 = "Administrative Organization of Cameroon"
M3 = "Constitutional & Political Organization"

LESSONS = []

# ------------------------------------------------------------------ 1. The family
LESSONS.append(lesson(
    module=M1,
    topic="The family",
    title="The family: types, roles and responsibilities",
    slug="cit1-the-family-types-and-roles",
    minutes=20,
    summary="What a family is, the main family types (nuclear, extended, single-parent, monogamous, polygamous), what families do for their members and what each member owes the others.",
    objectives=[
        "Define the family and name its main types",
        "Explain the functions of the family in society",
        "State the rights and duties of parents and children",
        "Explain how the family prepares a person to be a good citizen",
    ],
    key_concepts=["Family", "Nuclear family", "Extended family", "Single-parent family", "Socialisation", "Parental responsibility"],
    blocks=[
        H("Introduction"),
        T("Think of a Sunday meal in Bafoussam or Kumba. Parents, children, an aunt and perhaps a grandmother sit around one pot. "
          "Everyone has a part to play: someone cooks, someone fetches water, someone pays the school fees. This small group is where "
          "most of us first learn what it means to belong to a community."),
        T("Citizenship Education begins here because the family is the first school of citizenship. "
          "Respect, sharing, obedience to fair rules and care for others are all learned at home before they are learned in public life."),
        H("What is a family?"),
        D("A **family** is a group of people related by blood, marriage or adoption who usually live together, "
          "share resources and take care of one another, especially the children.", title="The family"),
        T("Notice the three links: **blood** (parents and their children), **marriage** (husband and wife) and **adoption** "
          "(a child legally taken into a family). A family is not always defined by living in one house. "
          "Many Cameroonian families keep strong ties across towns and villages."),
        H("Types of family"),
        D("A **nuclear family** is made up of parents and their children only.", title="Nuclear family"),
        D("An **extended family** includes other relatives such as grandparents, uncles, aunts and cousins, who live together or stay in close contact "
          "and share responsibilities.", title="Extended family"),
        T("In many Cameroonian communities the extended family is very important. An uncle may help pay school fees. "
          "A grandmother may look after children while their parents work. Relatives meet for funerals, weddings and village meetings."),
        D("A **single-parent family** is one in which a child or children live with only one parent, because of death, divorce, separation or "
          "other circumstances. Many single parents raise successful children.", title="Single-parent family"),
        T("Families are also described by the form of marriage. In a **monogamous** family a man has one wife (or a woman one husband). "
          "In a **polygamous** family a man has more than one wife. Customary law in some communities allows polygamy; "
          "the form of marriage chosen can matter under the law (see the next lessons, and check the current law)."),
        T("A family can also be a **foster family**, where children are looked after by adults who are not their parents, "
          "or a family headed by a child or a grandparent. Whatever the type, the aim is the same: care and protection."),
        KEY("Main functions of the family", "Use these as paragraph points in essays.", cards=[
            ["Reproduction and care", "Families bring up children and look after the sick and the elderly."],
            ["Socialisation", "Children learn language, values, manners and the rules of the community. This process is called **socialisation**."],
            ["Economic support", "Members share food, shelter, money and work. Many families farm or trade together."],
            ["Education and protection", "Parents guide their children, send them to school and protect them from harm."],
            ["Identity", "The family gives a name, a home community and a sense of belonging."],
        ], note="A strong answer names the function and then gives a short example."),
        H("Roles and responsibilities"),
        T("Every member has duties, and every member has rights. Parents have the greatest responsibility for children."),
        T("**Parents** should feed, clothe, house and protect their children; send them to school; give them love and guidance; "
          "and set a good example. **Children** should respect their parents, obey fair rules, help with household work and study hard. "
          "**Relatives** support one another in need."),
        T("The Constitution's preamble and Cameroon's laws recognise the family as a basic unit of society that the State protects. "
          "The State also protects children's rights (check the current text for the exact wording)."),
        EX("Model answer plan 1", intro="Explain three functions of the family.", steps=[
            S("Introduction", text="Define the family: people related by blood, marriage or adoption who live together or support one another."),
            S("Function 1: socialisation", text="Children learn values and manners at home. Example: a child taught to greet elders."),
            S("Function 2: economic support", text="Members share food, money and work. Example: a family farm or shop that feeds the household."),
            S("Function 3: protection and education", text="Parents pay school fees and keep children safe."),
            S("Conclusion", text="The family prepares young people to take a useful place in society."),
        ]),
        EX("Model answer plan 2", intro="Distinguish between a nuclear family and an extended family.", steps=[
            S("Nuclear family", text="Parents and their children only."),
            S("Extended family", text="Parents, children and other relatives: grandparents, uncles, aunts, cousins."),
            S("Example", text="A couple and three children in a rented house in Limbe are a nuclear family; add a grandmother and an uncle in the same compound and it becomes extended."),
            S("Difference", text="The extended family is larger and shares duties more widely; the nuclear family is smaller and more independent."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying the family is only people in one house", "Families are defined by relationship (blood, marriage, adoption), not only by living together. "
                "An uncle in another town is still part of the extended family."),
        MISTAKE("Mixing up nuclear and extended", "Nuclear = parents and children only. Extended = nuclear family plus other relatives."),
        MISTAKE("Listing functions without explaining them", "Examiners want a function and a short explanation or example, not a bare list of words."),
        QUIZ("Which of these is an extended family?",
             ["A mother and her two children only", "A father, a mother and their children only",
              "Parents, children and a grandmother and an uncle living with them", "A single child living alone"], 2,
             "An extended family includes relatives beyond the parents and children, such as grandparents and uncles.",
             hint="Look for the group that includes relatives beyond parents and children.",
             feedback=["This is a nuclear (single-parent) family.", "This is a nuclear family.", "",
                       "A person living alone is not a family."]),
        QUIZ("The process by which children learn the values and rules of their community is called",
             ["Migration", "Socialisation", "Taxation", "Delegation"], 1,
             "Socialisation is the learning of language, values and rules from the family and community.",
             hint="Think of the word 'social'.",
             feedback=["Migration means moving from one place to another.", "", "Taxation means collecting taxes.",
                       "Delegation means handing a task to someone else."]),
        H("Practice questions"),
        PQ("Define the family.", "A group of people related by blood, marriage or adoption who usually live together or support one another, especially the children."),
        PQ("Name three types of family.", "Any three of: nuclear; extended; single-parent; foster; monogamous; polygamous."),
        PQ("State three duties of parents to their children.",
           "Feed, clothe and house them; send them to school; protect them from harm; give love, guidance and a good example."),
        PQ("Give two functions of the family in society.",
           "Any two of: care and upbringing of children; socialisation (teaching values); economic support; education and protection; giving identity."),
        SUM("A family is a group related by blood, marriage or adoption.",
            "Types include nuclear, extended, single-parent and foster families; marriage forms are monogamous or polygamous.",
            "Main functions: care, socialisation, economic support, education and protection, identity.",
            "Parents have duties to children; children have duties to parents and relatives.",
            "The family is the first school of citizenship."),
    ],
))

# ------------------------------------------------------------------ 2. Marriage
LESSONS.append(lesson(
    module=M1,
    topic="Marriage and succession in Cameroon",
    title="Marriage in Cameroon: civil, customary and religious",
    slug="cit1-marriage-forms-and-bride-price",
    minutes=20,
    summary="The forms of marriage met in Cameroon (civil, customary, religious), the conditions for a valid civil marriage, the place of bride price, and why registration matters. Check the current law for details.",
    objectives=[
        "Define marriage and name the main forms practised in Cameroon",
        "State the general conditions for a valid civil marriage",
        "Explain the meaning and role of bride price in customary marriage",
        "Explain why a marriage certificate matters to a couple and their children",
    ],
    key_concepts=["Marriage", "Civil marriage", "Customary marriage", "Religious marriage", "Bride price", "Marriage certificate", "Consent"],
    blocks=[
        H("Introduction"),
        T("A wedding in Cameroon can be a large event: a meeting of two families, a ceremony at the council hall, a service at church or mosque, "
          "and a celebration with food, music and gifts. Behind the celebration, marriage also has legal effects: it affects the rights of husband, "
          "wife and children, and property and inheritance."),
        T("This lesson describes the main forms of marriage in general terms. Marriage rules are in written law and in custom, "
          "and the law can change, so always **check the current law** or your textbook for exact details."),
        H("What is marriage?"),
        D("**Marriage** is the union of a man and a woman recognised by law or custom, creating rights and duties between them and towards their children.",
          title="Marriage"),
        T("Free **consent** is the first condition of any valid marriage. This means each person agrees without pressure or force. "
          "Forced marriage is against the principles of Cameroon's laws and of international human rights texts."),
        H("The three forms of marriage"),
        KEY("Forms of marriage in Cameroon", "Many couples combine more than one form.", cards=[
            ["Civil marriage", "Celebrated in public before a civil status registrar (in practice a mayor or the registrar's representative) under the written law. It is recorded in the civil status register and a **marriage certificate** is issued."],
            ["Customary marriage", "Celebrated according to the traditions of the families' community: meetings of the families, gifts, **bride price** and rites. Rules differ between communities."],
            ["Religious marriage", "A blessing or ceremony in a church, mosque or other place of worship. It has religious value; check how far the law gives it legal effect without a civil ceremony."],
        ]),
        D("A **civil status registrar** is the official who records births, marriages and deaths (in Cameroon this is usually the mayor or his representative, "
          "in the council).", title="Civil status registrar"),
        H("Conditions for a valid civil marriage"),
        T("The law sets conditions. In general terms, check the current text for details:"),
        T("**Consent**: both people agree freely. **Minimum age**: the law sets a minimum age; older texts gave different minimum ages for girls and boys, "
          "and there have been discussions about equalising them, so check the current law. **No existing marriage**: a person already bound by a civil marriage "
          "cannot marry again at the same time. **No close family link**: close relatives cannot marry. "
          "**Publication of banns**: the intended marriage is announced publicly before the ceremony so that anyone with a legal objection can speak. "
          "**Presence and witnesses**: the ceremony is public, before the registrar, with witnesses."),
        T("The law also asks the couple to state their choice of marriage regime (monogamy or, where allowed, polygamy) and of property regime. "
          "Check the current law for the available options and effects."),
        T("A marriage certificate is the official proof of civil marriage. "
          "It is needed for many things: registering children, claiming certain benefits, and proving rights if there is a dispute or on a death."),
        H("Bride price"),
        D("The **bride price** (also called bride wealth or dowry in everyday speech) is the gifts or payment that the husband's family gives to "
          "the wife's family as part of a customary marriage.", title="Bride price"),
        T("In many communities the bride price is a sign of respect and of the bond between the two families. It is paid in goods, animals, money or other gifts, "
          "according to custom. Amounts and items differ widely from place to place."),
        T("Questions often asked: is bride price the \"price of a person\"? No. It is a customary token of gratitude and a way of making the union public. "
          "Misuse, such as excessive demands or treating a wife as property, is discouraged. In some places there have been calls for limits; check the current law and local custom."),
        EX("Model answer plan 1", intro="Distinguish between civil marriage and customary marriage in Cameroon.", steps=[
            S("Civil marriage", text="Celebrated before a civil status registrar under written law; recorded in a register; a certificate is issued."),
            S("Customary marriage", text="Celebrated according to the customs of the families' community, with rites, gifts and bride price; rules vary between communities."),
            S("Evidence", text="Civil marriage gives a certificate as proof; customary marriage is proved by custom and witnesses, so many couples also register their marriage."),
            S("Conclusion", text="The two forms may be combined: many couples have a customary ceremony and a civil ceremony."),
        ]),
        EX("Model answer plan 2", intro="Why is a marriage certificate important to a family?", steps=[
            S("Proof", text="It is official proof that the couple are married."),
            S("Children", text="It helps to register children and to prove their parentage."),
            S("Rights", text="It supports claims such as social security benefits and inheritance, and protects a spouse in a dispute."),
            S("Conclusion", text="Registration protects the rights of the husband, the wife and the children."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying bride price buys the wife", "Bride price is a customary gift between families that marks respect and the bond between them. It does not give ownership of a person."),
        MISTAKE("Treating the church wedding as the civil marriage", "A religious ceremony is not the same as the civil ceremony before the registrar. Check what the law says about the effects of each."),
        MISTAKE("Quoting an exact minimum age or article from memory", "If you are not sure, say 'the law sets a minimum age' and mention that you should check the current text."),
        QUIZ("Who normally celebrates a civil marriage in Cameroon?",
             ["The village chief", "A civil status registrar (usually the mayor or his representative)", "A school principal", "A church pastor acting alone"], 1,
             "A civil marriage is celebrated in public before a civil status registrar, usually the mayor or a representative.",
             hint="Which official keeps the register of births and marriages?",
             feedback=["A chief may take part in a customary marriage, not the civil one.", "",
                       "A principal runs a school.", "A pastor conducts a religious ceremony, which is not the civil marriage."]),
        QUIZ("Which of these is a condition of any valid marriage?",
             ["Payment of taxes", "Free consent of both people", "Ownership of land", "A university degree"], 1,
             "Both people must agree freely, without pressure or force.",
             hint="Think about the people being married.",
             feedback=["Taxes have nothing to do with the validity of a marriage.", "", "Land ownership is not a condition.",
                       "A degree is not required."]),
        H("Practice questions"),
        PQ("Name the three forms of marriage in Cameroon.", "Civil marriage, customary marriage and religious marriage."),
        PQ("State two conditions of a valid civil marriage.",
           "Any two of: free consent; minimum age set by law; no existing marriage; no close family link; public ceremony before the registrar with witnesses. Check the current law."),
        PQ("What is bride price?",
           "Gifts or payment given by the husband's family to the wife's family as part of a customary marriage, as a mark of respect and a link between families."),
        PQ("Give two reasons for registering a marriage.",
           "It gives official proof of marriage; it helps register children and protect rights of spouses and children, for example in inheritance and social security."),
        SUM("Marriage is a union recognised by law or custom, which needs free consent.",
            "The main forms are civil, customary and religious; couples often combine them.",
            "A civil marriage is celebrated before a registrar and leads to a marriage certificate.",
            "Bride price is a customary gift between families, not the purchase of a person.",
            "Check the current law for age, regimes and exact effects."),
    ],
))

# ------------------------------------------------------------------ 3. Wills and succession
LESSONS.append(lesson(
    module=M1,
    topic="Marriage and succession in Cameroon",
    title="Wills and succession: who inherits?",
    slug="cit1-wills-and-succession",
    minutes=20,
    summary="What succession is, what a will does, what happens when someone dies without a will, and why fairness to widows and children matters. General rules only: check the current law.",
    objectives=[
        "Define succession, a will, a testator, an heir and intestacy",
        "Explain the difference between succession with a will and without a will",
        "Describe in general terms the rules that guide inheritance in Cameroon",
        "Explain why peaceful and fair settlement of an estate matters",
    ],
    key_concepts=["Succession", "Estate", "Will", "Testator", "Heir", "Intestate", "Customary law"],
    blocks=[
        H("Introduction"),
        T("When a person dies, the house, land, savings, shop or farm they owned must pass to someone. If this is not settled clearly, "
          "families can quarrel for years, and widows and children can suffer. Succession rules exist to make the transfer orderly and fair."),
        T("Cameroon's rules on succession come from written law and from custom, and they differ depending on the legal system and the community "
          "concerned. This lesson gives the general ideas. **Check the current law** and your textbook for exact rules."),
        H("Key words"),
        D("**Succession** (or inheritance) is the passing of a dead person's property, rights and debts to other persons.", title="Succession"),
        D("The **estate** is everything a dead person owned and owed: property, money, land and debts.", title="Estate"),
        D("A **will** (testament) is a written document in which a person, the **testator**, says how their property should be shared after death.", title="Will"),
        D("An **heir** is a person who receives part of the estate. A person who dies without a valid will is said to die **intestate**.", title="Heir and intestate"),
        H("Succession with a will"),
        T("A will lets a person decide in advance who gets what. In general, a will must be made freely by an adult of sound mind. "
          "Written form, signatures and witnesses (or a notary) are normally required, and the law may protect certain close relatives so that "
          "they are not left with nothing. The exact formalities and protected shares must be checked in the current law."),
        T("A will can be changed or cancelled by the testator at any time while they are alive and of sound mind. A will takes effect only at death."),
        H("Succession without a will"),
        T("When there is no valid will, the property passes according to the rules of the law or of custom. "
          "In the written law, the nearest family members, such as the spouse and the children, are usually the first heirs. "
          "In customary law, the rules depend on the community: in some, property passes through the father's line; in others, through the mother's line; "
          "and rules about widows and daughters differ."),
        T("The meaning for citizens: customs that are unfair to widows or daughters are criticised, and the Constitution's preamble and Cameroon's "
          "international commitments support equality and the protection of women and children. If custom and these principles conflict, "
          "a court may decide. Check the current law for how this works."),
        KEY("Steps in settling an estate", "A general sequence, not a legal text.", cards=[
            ["1. Declare the death", "The death is declared and a death certificate is issued by the civil status office."],
            ["2. Identify the estate and the heirs", "The family lists what the dead person owned and owed, and who the heirs are."],
            ["3. Pay debts and costs", "Funeral costs and debts are settled from the estate according to the law."],
            ["4. Share the remainder", "According to the will, or to the law or custom if there is no will."],
            ["5. Go to a court or notary if there is a dispute", "A court can decide who the heirs are and how to share."],
        ]),
        EX("Model answer plan 1", intro="Distinguish between succession with a will and without a will.", steps=[
            S("With a will", text="The testator wrote how to share the property; the heirs named in the will receive it, within limits set by law."),
            S("Without a will", text="The person died intestate; the property is shared according to law or custom."),
            S("Example", text="A trader in Douala who wrote a will leaves the shop to his daughter; if he had no will, the law or custom would decide."),
            S("Conclusion", text="A will gives certainty and can prevent quarrels."),
        ]),
        EX("Model answer plan 2", intro="Explain why a family should settle an estate peacefully.", steps=[
            S("Protection of the vulnerable", text="Widows and young children can be left homeless if the estate is seized unfairly."),
            S("Family unity", text="Quarrels over land and houses divide families and can last for years."),
            S("Legal order", text="Courts and notaries exist to decide disputes lawfully; violence and self-help are wrong."),
            S("Conclusion", text="Fair and peaceful succession protects rights and keeps the community united."),
        ]),
        H("Common mistakes"),
        MISTAKE("Confusing a will with a marriage certificate", "A will says what happens to property after death. A marriage certificate proves a marriage."),
        MISTAKE("Saying property goes only to sons", "General principles of equality and the protection of widows and daughters apply. Customs differ, but they cannot simply override the law; check the current rules."),
        MISTAKE("Thinking a will takes effect at once", "A will takes effect only when the testator dies. Until then, the testator can change it."),
        QUIZ("A person who dies without a valid will is said to die",
             ["Testate", "Intestate", "Heir", "Delegated"], 1,
             "To die intestate means to die without a valid will.",
             hint="The word for 'with a will' is testate; what is the opposite?",
             feedback=["Testate means leaving a valid will.", "", "An heir is the person who inherits.", "Delegated is not used in succession."]),
        QUIZ("The person who writes a will is called",
             ["The heir", "The registrar", "The testator", "The magistrate"], 2,
             "The testator is the person who makes the will.",
             hint="The word is related to 'testament'.",
             feedback=["The heir receives the property.", "The registrar records civil events.", "", "A magistrate is a judge."]),
        H("Practice questions"),
        PQ("Define succession.", "The passing of a dead person's property, rights and debts to other persons."),
        PQ("What is a will, and who is a testator?", "A will is a written document in which a person says how their property is to be shared after death. The testator is the person who makes it."),
        PQ("Who usually inherits when there is no will, according to the general rules of written law?", "The nearest relatives, usually the surviving spouse and the children (check the current law for the exact order and shares)."),
        PQ("Give two reasons why it is important to settle an estate fairly and peacefully.",
           "It protects widows and children; it avoids family quarrels; it respects the law and keeps order in the community."),
        SUM("Succession is the passing of a dead person's estate to heirs.",
            "A will, made by the testator, tells how to share the property; it takes effect at death.",
            "Without a will (intestate), the law or custom decides.",
            "Fair and peaceful settlement protects widows, children and family unity.",
            "Check the current law for formalities and shares."),
    ],
))

# ------------------------------------------------------------------ 4. School and village
LESSONS.append(lesson(
    module=M1,
    topic="The school and the village",
    title="The school and the village: community life and traditional authority",
    slug="cit1-school-and-village-community",
    minutes=20,
    summary="The school as a community with rules and roles, the village and its traditional authorities, and how students can serve both through discipline, cooperation and community service.",
    objectives=[
        "Describe the people and rules that make a school community work",
        "Explain how school rules prepare students for citizenship",
        "Describe the role of the village or chiefdom and its traditional authority",
        "Give examples of community service and cooperation",
    ],
    key_concepts=["School community", "School rules", "Traditional ruler", "Chiefdom", "Community service", "Cooperation"],
    blocks=[
        H("Introduction"),
        T("Every morning a student in Bamenda or Bertoua walks to school, greets the gatekeeper, takes a seat in class and follows a timetable. "
          "After school, the same student may fetch water, farm, attend a village meeting or help clean a public space. "
          "The school and the village are two communities where citizenship is practised every day."),
        H("The school as a community"),
        D("A **school community** is made up of students, teachers, the principal, administrative and support staff, parents and the Parent-Teacher "
          "Association (PTA), all working so that students learn in a safe and orderly place.", title="School community"),
        T("Each member has a role. The **principal** leads the school and is answerable to the education authorities. "
          "**Teachers** teach and guide. **Students** learn and respect the rules. **Parents** pay fees where required, support learning and take part in the PTA. "
          "**Discipline masters or counsellors** help with conduct and personal problems."),
        KEY("Why school rules matter", "They prepare students for the laws of the wider society.", cards=[
            ["Order and safety", "Rules on punctuality, uniform and movement keep the school safe and calm."],
            ["Fairness", "The same rules apply to every student."],
            ["Respect", "Rules teach respect for teachers, other students and property."],
            ["Responsibility", "Students learn that actions have consequences, as with the law in society."],
        ], note="Link: obeying school rules is practice for obeying the laws of Cameroon."),
        T("Student participation also matters. Class prefects, club leaders and student councils let students practise leadership, "
          "election, representation and service. These roles train future citizens."),
        T("Examples of good school citizenship: arriving on time, taking care of desks and books, keeping the compound clean, "
          "helping weaker students, refusing cheating, bullying and drug use, and respecting people of other regions, languages and beliefs."),
        H("The village and its traditional authority"),
        D("A **village** (or quarter in a town) is a local community of families who share land, a meeting place and common customs. "
          "A **chiefdom** is a community under a **traditional ruler** (called a chief, fon, lamido or another title, according to the region).",
          title="Village and chiefdom"),
        T("Traditional rulers keep customs alive, settle small disputes, look after community land and guide their people. "
          "They are respected because they link the present to the past."),
        T("In Cameroon the law treats traditional chiefdoms as part of the administrative system: chiefs act as **auxiliaries** of the administration. "
          "This means they help officials, for example by passing on information, helping to collect certain data and keeping peace. "
          "Chiefdoms are classified by degree (first, second and third degree), and chiefs are expected to respect the law and the Constitution. "
          "Check the current texts for the exact rules."),
        IMG("f5cit-1-admin-chain.svg", alt="Administrative chain of Cameroon from the President down to villages, quarters and chiefdoms, where traditional authorities help",
            caption="Figure 1. Villages and chiefdoms sit at the base of the administrative chain; traditional authorities help the administration."),
        H("Community service and cooperation"),
        D("**Community service** is work done freely for the common good: cleaning drains, repairing a village road, building a classroom, "
          "planting trees or helping with a funeral or a flood emergency.", title="Community service"),
        T("In many villages this takes the form of **cooperation**: age groups, women's groups (njangi or other savings and work groups) and "
          "youth groups share work and money. Cooperation shows the value of unity: a task that is too heavy for one family becomes light for many."),
        EX("Model answer plan 1", intro="Explain three ways in which a student can be a good citizen at school.", steps=[
            S("Introduction", text="A good citizen respects rules and others and serves the community."),
            S("Obey school rules", text="Be punctual, wear the uniform, respect teachers; this builds a habit of obeying the law."),
            S("Respect others and property", text="No bullying or fighting; take care of desks, books and the compound."),
            S("Take part", text="Join clubs, serve as prefect, help to clean the compound."),
            S("Conclusion", text="A school where students behave well prepares good citizens."),
        ]),
        EX("Model answer plan 2", intro="Describe the role of a traditional ruler in his community.", steps=[
            S("Custom", text="Keeps and passes on the customs and values of the community."),
            S("Peace and disputes", text="Settles small disputes and keeps peace."),
            S("Community land and development", text="Guides use of community land and mobilises people for community projects."),
            S("Link with the administration", text="Acts as an auxiliary of the administration; helps officials; must respect the law."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying the chief is above the law", "A traditional ruler must obey the Constitution and the law like everyone else, and acts as an auxiliary of the administration."),
        MISTAKE("Writing only about discipline", "A school community is also about participation, cooperation and service, not just punishment."),
        MISTAKE("Confusing the PTA with the school staff", "The PTA brings parents and teachers together; parents are not school staff."),
        QUIZ("A traditional ruler in Cameroon is best described as",
             ["Above the law", "An auxiliary of the administration who must respect the law",
              "A judge of the Supreme Court", "The head of a region"], 1,
             "Traditional rulers help the administration and must respect the law; they are not above it.",
             hint="Think of how chiefs help the administration.",
             feedback=["No one is above the law.", "", "Judges of the Supreme Court are professional magistrates.",
                       "A region is headed by a Governor."]),
        QUIZ("Which is an example of community service?",
             ["Skipping school", "Cleaning a village drain with neighbours", "Selling goods in a market", "Watching television"], 1,
             "Community service is work done for the common good, such as cleaning a drain.",
             hint="It is done freely and helps everyone.",
             feedback=["Skipping school harms the student.", "", "Trading is private business.", "Television is leisure, not service."]),
        H("Practice questions"),
        PQ("Name four members of a school community.", "Any four of: students, teachers, the principal, administrative and support staff, parents, the PTA."),
        PQ("Give two reasons why school rules are important.", "They keep order and safety; they treat everyone fairly; they teach respect and responsibility; they prepare students to obey the law."),
        PQ("State two roles of a traditional ruler.", "Keeping customs; settling small disputes; guiding use of community land; helping the administration."),
        PQ("Define community service and give one example.", "Work done freely for the common good, for example cleaning a village drain or repairing a road."),
        SUM("The school community includes students, teachers, the principal, staff, parents and the PTA.",
            "School rules teach order, fairness, respect and responsibility, and prepare students for the law.",
            "Traditional rulers keep customs and peace and act as auxiliaries of the administration.",
            "Community service and cooperation serve the common good.",
            "Check the current texts on chiefdoms."),
    ],
))

# ------------------------------------------------------------------ 5. Road safety
LESSONS.append(lesson(
    module=M1,
    topic="Road safety",
    title="Road safety: traffic rules and responsible road use",
    slug="cit1-road-safety-rules",
    minutes=20,
    summary="Why road accidents happen, the main traffic rules for pedestrians, motorcyclists and drivers, how to read road signs by shape and colour, and what to do after an accident. Check the current rules.",
    objectives=[
        "Explain the main causes of road accidents",
        "State the basic rules for pedestrians, motorcyclists and drivers",
        "Recognise the main groups of road signs by shape and colour",
        "Describe what to do at the scene of an accident",
    ],
    key_concepts=["Road safety", "Traffic regulation", "Road signs", "Pedestrian", "Helmet and seat belt", "First aid"],
    blocks=[
        H("Introduction"),
        T("Moto-taxis in Douala, buses on the Yaounde-Bafoussam road, lorries on the way to Garoua: the roads carry life and trade, "
          "but they also carry danger. Road accidents injure and kill many people each year. Most are caused by human behaviour, "
          "and so most can be prevented."),
        T("Road safety rules protect everyone: drivers, passengers, motorcyclists, cyclists and pedestrians. "
          "The rules summarised here are general. Cameroon's Highway Code and decrees set the exact details, so check the current rules."),
        H("Causes of road accidents"),
        KEY("Main causes", "Group causes under human, vehicle and road factors.", cards=[
            ["Human factors", "Speeding, drunk or tired driving, using a phone while driving, ignoring signs and signals, not wearing a seat belt or helmet, overloading and careless crossing by pedestrians."],
            ["Vehicle factors", "Bad brakes or tyres, broken lights, poor maintenance, overloaded vehicles."],
            ["Road and weather factors", "Potholes, poor lighting, rain, fog, dust, animals on the road, work zones without warnings."],
        ], note="Most accidents involve human behaviour, so changing behaviour saves lives."),
        H("Basic rules"),
        T("**Vehicle traffic keeps to the right** in Cameroon, and overtaking is normally done on the left when the road ahead is clear."),
        T("**Drivers** must hold a valid driving licence and keep the vehicle's papers in order: registration document, insurance and technical inspection. "
          "They must obey speed limits, stop at red lights, give way where required, wear seat belts and never drive after drinking alcohol or when very tired."),
        T("**Motorcyclists and passengers** should wear a crash helmet. A rider should not carry more passengers than the law allows."),
        T("**Pedestrians** should walk on the footpath or the side of the road facing traffic where there is no pavement, cross at pedestrian crossings or where it is safe, "
          "look both ways, and not walk while looking at a phone. Children should cross with an adult."),
        T("**Passengers** should not distract the driver, should use seat belts and should speak up when a driver is reckless."),
        H("Road signs"),
        D("**Road signs** are standard symbols placed beside the road to tell users what to do or what to expect. Their **shape and colour** tell you the type "
          "of message before you read the symbol.", title="Road signs"),
        IMG("f5cit-1-sign-shapes.svg", alt="Four road signs: A a red circle with a bar meaning no entry, B a blue circle with an arrow meaning an order to follow, C a red triangle with an exclamation mark meaning warning, D a blue rectangle with the letter P meaning information about parking",
            caption="Figure 1. Common sign groups: red circle (prohibition), blue circle (order), red triangle (warning), blue rectangle (information)."),
        KEY("Reading sign shapes", "The general pattern in countries following common conventions; check the Highway Code.", cards=[
            ["Red circle", "Prohibition or limit: something you must not do (no entry, speed limit)."],
            ["Blue circle", "Obligation: something you must do (turn right, keep left)."],
            ["Red triangle", "Warning: danger ahead (bend, junction, pedestrians)."],
            ["Blue rectangle or square", "Information: parking, hospital, direction."],
        ]),
        T("Traffic lights: **red** means stop, **amber** means get ready to stop, **green** means go if the road is clear. "
          "Police officers' hand signals overrule lights."),
        H("What to do after an accident"),
        T("First, make sure you are safe. Then call for help (the emergency services and the police), do not move seriously injured people unless there is immediate danger (for example fire), "
          "give first aid if you are trained, warn other traffic, and stay at the scene until the police arrive. Do not run away. "
          "Fleeing the scene is against the law. In an emergency, check the current emergency telephone numbers."),
        EX("Model answer plan 1", intro="Explain three causes of road accidents in Cameroon and one way to prevent each.", steps=[
            S("Speeding", text="Prevention: obey speed limits; police speed checks."),
            S("Poor vehicle maintenance", text="Prevention: regular technical inspection of vehicles."),
            S("Bad roads or weather", text="Prevention: repair potholes, install signs and lights; drive slowly in rain."),
            S("Conclusion", text="Drivers, passengers and the State all share responsibility."),
        ]),
        EX("Model answer plan 2", intro="State the duties of a motorcyclist.", steps=[
            S("Licence and papers", text="Hold a valid licence and keep insurance and registration in order."),
            S("Helmet", text="Wear a crash helmet and make sure passengers do too if the law requires."),
            S("Respect the law", text="Obey signs and lights; keep to the right; do not carry too many passengers."),
            S("Behaviour", text="Never ride after drinking; avoid speed and overtaking in dangerous places."),
        ]),
        H("Common mistakes"),
        MISTAKE("Confusing sign shapes", "Triangle with red border = warning. Circle with red border = prohibition. Blue circle = order. Learn the pattern, then the symbol."),
        MISTAKE("Blaming only the driver", "Pedestrians, passengers, road owners and vehicle owners also share responsibility for safety."),
        MISTAKE("Quoting exact fines or speed limits from memory", "Fines and limits change. Say 'the law sets a speed limit' and check the current Highway Code."),
        QUIZ("A triangular sign with a red border usually means",
             ["Prohibition", "Warning of danger ahead", "Information about parking", "An order to turn left"], 1,
             "A red triangle warns of a danger ahead, such as a bend or a junction.",
             hint="Think of the shape that means 'watch out'.",
             feedback=["Prohibition is usually a red circle.", "", "Information is usually a blue rectangle.", "Orders are usually blue circles."]),
        QUIZ("In Cameroon, traffic normally keeps to the",
             ["Left", "Right", "Middle", "Side with fewer cars"], 1,
             "Vehicles keep to the right-hand side of the road.",
             hint="Which side is the driver's seat usually on?",
             feedback=["Left-hand traffic is used in some other countries.", "", "Keeping to the middle is dangerous.", "The side with fewer cars is not a rule."]),
        H("Practice questions"),
        PQ("State three causes of road accidents.", "Any three of: speeding; drunk or tired driving; phone use; faulty vehicles; bad roads; overloading; ignoring signs."),
        PQ("Give three rules for pedestrians.", "Use the footpath or walk facing traffic; cross at safe crossings; look both ways; do not walk while using a phone; children cross with an adult."),
        PQ("What do red, amber and green traffic lights mean?", "Red: stop; amber: get ready to stop; green: go if the road is clear."),
        PQ("Say what to do at the scene of an accident.", "Make the area safe; call for help; give first aid if trained; do not move serious casualties without need; stay until police arrive."),
        SUM("Most accidents are caused by human behaviour, so most can be prevented.",
            "Drivers need a licence and valid papers; riders should wear helmets; everyone should obey signs and lights.",
            "Sign shape tells the type: red circle prohibits, blue circle orders, red triangle warns, blue rectangle informs.",
            "After an accident: stay safe, call for help, give first aid if trained, stay at the scene.",
            "Check the current Highway Code for exact rules."),
    ],
))

# ------------------------------------------------------------------ 6. Deconcentration vs decentralization
LESSONS.append(lesson(
    module=M2,
    topic="Deconcentration and decentralization",
    title="Deconcentration and decentralization",
    slug="cit1-deconcentration-and-decentralization",
    minutes=20,
    summary="Two ways of spreading State power away from the capital: deconcentration (appointed officials who act for the centre) and decentralization (elected local authorities with their own powers). Differences, aims, advantages and limits.",
    objectives=[
        "Define deconcentration and decentralization",
        "Distinguish between the two with examples from Cameroon",
        "Explain why a State needs both",
        "State advantages and difficulties of decentralization",
    ],
    key_concepts=["Centralization", "Deconcentration", "Decentralization", "Local authority", "Legal personality", "Financial autonomy", "Supervision"],
    blocks=[
        H("Introduction"),
        T("Imagine that every decision in Cameroon, from repairing a bridge in Mamfe to opening a market in Maroua, had to be approved in Yaounde. "
          "Decisions would be slow and often unsuitable for local needs. States solve this problem by spreading power and responsibility to different levels. "
          "There are two main ways."),
        H("Centralization first"),
        D("**Centralization** is a system in which all important decisions are taken by the central government in the capital.", title="Centralization"),
        T("A State cannot run everything from the capital: officials far away do not know local needs, and citizens wait long for decisions. "
          "So the central government moves part of its work to local levels."),
        H("Deconcentration"),
        D("**Deconcentration** is the transfer of some tasks from the central government to its own officials working in the regions, divisions and sub-divisions. "
          "These officials are **appointed** and act on behalf of the central government, under its orders.", title="Deconcentration"),
        T("In Cameroon, the Governor in a region, the Senior Divisional Officer (SDO) in a division and the Divisional Officer (DO) in a sub-division "
          "represent the State and the central government. They carry out national policy, keep law and order, and supervise public services. "
          "They are appointed and are not chosen by local voters."),
        H("Decentralization"),
        D("**Decentralization** is the transfer of powers, resources and responsibilities from the State to **local authorities** that have their own legal personality "
          "and financial autonomy. Their leaders are usually **elected**.", title="Decentralization"),
        T("In Cameroon, the local authorities in this sense are the councils (municipal councils and city councils) and the regional councils. "
          "They run local matters such as markets, local roads, primary-school buildings, local health centres and the environment, within the law and with their own budget. "
          "The State keeps a supervisory role to make sure the law is respected. Check the current laws on decentralization for the exact powers."),
        IMG("f5cit-1-decon-vs-decent.svg", alt="Two columns: deconcentration, with appointed officials acting for the central government under orders, and decentralization, with elected councils having their own budget",
            caption="Figure 1. Deconcentration compared with decentralization."),
        KEY("Comparing the two", "Learn this contrast for essays and multiple-choice questions.", cards=[
            ["Who rules?", "Deconcentration: appointed State officials. Decentralization: elected councils and their executives."],
            ["Whose power?", "Deconcentration: the State's power, exercised locally. Decentralization: powers transferred to local authorities."],
            ["Legal status", "Deconcentrated offices are part of the State. Local authorities have their own legal personality and budget."],
            ["Control", "Deconcentration: hierarchical orders from above. Decentralization: supervision by the State, with the council deciding in its own areas."],
        ]),
        H("Advantages and difficulties"),
        T("**Advantages of decentralization**: decisions are closer to the people; citizens take part in local affairs; local needs are better known; "
          "development can be faster; and the central government is relieved of small tasks."),
        T("**Difficulties**: councils may lack money, trained staff or equipment; central government may be slow to transfer resources; "
          "local rivalries or mismanagement can occur; and responsibilities between the State and councils may overlap."),
        EX("Model answer plan 1", intro="Distinguish between deconcentration and decentralization.", steps=[
            S("Deconcentration", text="Transfer of tasks to appointed State officials in the field who act for the central government, for example a Governor or SDO."),
            S("Decentralization", text="Transfer of powers and resources to elected local authorities with their own legal personality and budget, for example a council."),
            S("Main difference", text="Deconcentration keeps power inside the State hierarchy; decentralization gives real powers to local bodies."),
            S("Conclusion", text="A State often uses both to bring government closer to citizens."),
        ]),
        EX("Model answer plan 2", intro="Explain three advantages of decentralization.", steps=[
            S("Closer to citizens", text="Decisions are taken near the people affected."),
            S("Participation", text="Citizens vote for councillors and can follow local affairs."),
            S("Local development", text="Councils can design projects that fit local needs: markets, roads, health posts."),
            S("Relief for the centre", text="The central government can focus on national matters."),
        ]),
        H("Common mistakes"),
        MISTAKE("Using the two words as synonyms", "Deconcentration moves tasks to appointed officials of the State. Decentralization moves powers to separate local authorities."),
        MISTAKE("Calling a Governor a decentralized authority", "The Governor is appointed and represents the State: that is deconcentration. Councils and regional councils are decentralized."),
        MISTAKE("Forgetting State supervision", "Decentralization does not mean independence. Local authorities remain inside the unitary State and are supervised."),
        QUIZ("An official appointed by the President to represent the State in a division is an example of",
             ["Decentralization", "Deconcentration", "Federalism", "Secession"], 1,
             "An SDO is appointed and acts for the central government, so this is deconcentration.",
             hint="Is the SDO elected by the people of the division?",
             feedback=["Decentralization involves elected local authorities.", "", "Federalism divides sovereignty between two levels of State.", "Secession means breaking away from a State."]),
        QUIZ("Which feature belongs to decentralization?",
             ["Officials are appointed and obey central orders", "Local authorities have their own budget and legal personality",
              "All decisions are taken in the capital", "There are no local elections"], 1,
             "Decentralized local authorities have legal personality and financial autonomy.",
             hint="Which statement describes councils?",
             feedback=["This describes deconcentration.", "", "This describes centralization.", "Decentralization normally involves local elections."]),
        H("Practice questions"),
        PQ("Define decentralization.", "The transfer of powers, resources and responsibilities from the State to local authorities with their own legal personality and financial autonomy, whose leaders are usually elected."),
        PQ("Give one example of deconcentration in Cameroon.", "The Governor of a region, the SDO of a division or the DO of a sub-division, appointed to represent the State."),
        PQ("State two advantages of decentralization.", "Decisions near the people; citizen participation; development suited to local needs; relief for the central government."),
        PQ("State two difficulties of decentralization.", "Lack of funds or trained staff; slow transfer of resources; mismanagement; overlap of responsibilities."),
        SUM("Centralization concentrates decisions in the capital.",
            "Deconcentration: appointed State officials act for the centre in the field.",
            "Decentralization: elected local authorities with legal personality and a budget run local affairs under State supervision.",
            "Cameroon uses both: Governors, SDOs and DOs; councils and regional councils.",
            "Advantages: closeness, participation, local development; difficulties: money, staff, overlaps."),
    ],
))

# ------------------------------------------------------------------ 7. Administrative units
LESSONS.append(lesson(
    module=M2,
    topic="Administrative units",
    title="Regions, divisions and sub-divisions",
    slug="cit1-administrative-units",
    minutes=20,
    summary="The administrative units of Cameroon (10 regions, divisions, sub-divisions), who heads each, how they relate, and the work of the Governor, the SDO and the DO.",
    objectives=[
        "Name Cameroon's ten regions and the head of each level of administration",
        "Describe the chain from the Governor to the Divisional Officer",
        "State the main duties of Governors, SDOs and DOs",
        "Distinguish administrative units from local authorities",
    ],
    key_concepts=["Region", "Division", "Sub-division", "Governor", "Senior Divisional Officer", "Divisional Officer", "Territorial administration"],
    blocks=[
        H("Introduction"),
        T("When you apply for a national identity card in a small town, you may meet the Divisional Officer. If a dispute spreads between two villages, "
          "the Senior Divisional Officer may call a meeting. If there is a regional emergency, the Governor takes charge. "
          "These officials form the State's local administration."),
        H("The structure"),
        D("The **administrative units** of Cameroon are the **region**, the **division** and the **sub-division**, arranged from the largest to the smallest. "
          "Each has an appointed head who represents the State.", title="Administrative units"),
        T("The national territory is divided into **ten regions**: Adamawa, Centre, East, Far North, Littoral, North, North-West, South, South-West and West. "
          "Each region is divided into **divisions** (about 58 in all) and each division into **sub-divisions** (about 360 in all). "
          "These numbers can change when new units are created, so check the current list."),
        IMG("f5cit-1-admin-chain.svg", alt="Administrative chain: President, then Governor of a region, then SDO of a division, then DO of a sub-division, then villages and chiefdoms",
            caption="Figure 1. The chain of deconcentrated administration."),
        KEY("Heads of the units", "Appointed by the President by decree; check the current rules.", cards=[
            ["Region: Governor", "Represents the President and the Government in the region; coordinates State services; keeps law and order; supervises the SDOs."],
            ["Division: Senior Divisional Officer (SDO)", "Represents the State in the division; leads the administration of the division; supervises the DOs."],
            ["Sub-division: Divisional Officer (DO)", "Represents the State in the sub-division; the closest State authority to many citizens; works with councils and chiefs."],
        ]),
        T("Region capitals (seats of the Governors) are: Ngaoundere (Adamawa), Yaounde (Centre), Bertoua (East), Maroua (Far North), Douala (Littoral), "
          "Garoua (North), Bamenda (North-West), Ebolowa (South), Buea (South-West) and Bafoussam (West)."),
        H("Duties of these officials"),
        T("In general terms, Governors, SDOs and DOs: keep **law and order**; protect people and property; carry out government policy; "
          "coordinate the work of State services (health, education, agriculture and others) in their area; supervise local authorities as the law provides; "
          "organise administrative duties such as meetings, civil protection and events; and report to the higher authorities. "
          "They work with traditional rulers, who are auxiliaries of the administration. Details are in the law, so check the current rules."),
        H("Units versus local authorities"),
        T("**Do not confuse** a division with a council. A division and a sub-division are administrative units headed by an appointed officer (deconcentration). "
          "A council is a decentralized local authority headed by elected people. In many places their areas overlap: the area of a council is often the same as, or close to, a sub-division. "
          "The next lesson studies councils."),
        EX("Model answer plan 1", intro="Describe the administrative organisation of Cameroon.", steps=[
            S("Regions", text="The country is divided into ten regions, each headed by a Governor."),
            S("Divisions", text="Each region has divisions headed by Senior Divisional Officers."),
            S("Sub-divisions", text="Each division has sub-divisions headed by Divisional Officers."),
            S("Chain", text="Officials are appointed by the President and represent the State; they work with traditional rulers at the base."),
            S("Conclusion", text="This is deconcentration: administration brought closer to citizens."),
        ]),
        EX("Model answer plan 2", intro="State the duties of a Senior Divisional Officer.", steps=[
            S("Representation", text="Represents the President and the Government in the division."),
            S("Law and order", text="Keeps public order and the safety of people and property."),
            S("Coordination", text="Coordinates State services in the division."),
            S("Supervision", text="Supervises Divisional Officers and, as the law provides, local authorities."),
        ]),
        H("Common mistakes"),
        MISTAKE("Writing the levels in the wrong order", "From the largest: region, division, sub-division. A division is bigger than a sub-division."),
        MISTAKE("Matching the wrong head to the unit", "Region: Governor. Division: SDO. Sub-division: DO."),
        MISTAKE("Saying the SDO is elected", "Governors, SDOs and DOs are appointed. Councillors and mayors are chosen through elections."),
        QUIZ("Who heads a division?",
             ["The Governor", "The Senior Divisional Officer", "The Divisional Officer", "The Mayor"], 1,
             "The Senior Divisional Officer (SDO) heads a division.",
             hint="The Divisional Officer is one level down.",
             feedback=["The Governor heads a region.", "", "The DO heads a sub-division.", "A mayor heads a council, a different type of unit."]),
        QUIZ("How many regions does Cameroon have?",
             ["Eight", "Ten", "Twelve", "Fifty-eight"], 1,
             "Cameroon has ten regions.",
             hint="Count the regions named in the lesson.",
             feedback=["Eight is too few: count the regions listed in the lesson.", "", "Twelve is not the number.", "Fifty-eight is about the number of divisions."]),
        H("Practice questions"),
        PQ("Name the three administrative units of Cameroon from largest to smallest.", "Region, division, sub-division."),
        PQ("Name the head of each unit.", "Region: Governor. Division: Senior Divisional Officer. Sub-division: Divisional Officer."),
        PQ("State three duties of a Governor.", "Represents the Government; keeps law and order; coordinates State services in the region; supervises SDOs."),
        PQ("Why is a division not the same as a council?", "A division is a State administrative unit headed by an appointed SDO (deconcentration); a council is a decentralized local authority run by elected councillors."),
        SUM("Cameroon has ten regions, divided into divisions (about 58) and sub-divisions (about 360); check current numbers.",
            "Region: Governor; division: SDO; sub-division: DO. All are appointed.",
            "They represent the State, keep law and order and coordinate State services.",
            "Traditional rulers help at village level.",
            "Administrative units are different from councils."),
    ],
))

# ------------------------------------------------------------------ 8. Decentralized local authorities
LESSONS.append(lesson(
    module=M2,
    topic="Decentralized local authorities",
    title="Councils and regional councils",
    slug="cit1-local-authorities-councils",
    minutes=20,
    summary="Municipal councils, city councils and regional councils: what they are, how they are chosen, what they do, how they are financed and how citizens take part. Check the current laws.",
    objectives=[
        "Name the decentralized local authorities in Cameroon",
        "Describe how a municipal council is organised and chosen",
        "List the main functions and sources of income of councils",
        "Explain how citizens can take part in local government",
    ],
    key_concepts=["Municipal council", "Mayor", "Councillor", "City council", "Regional council", "Local budget", "Civil status"],
    blocks=[
        H("Introduction"),
        T("When a baby is born, the birth is registered at the council office. When a market is built or a road is repaired in a town, the council may be responsible. "
          "When a trader pays a market fee, the money often goes to the council. Councils are the level of government that citizens meet most often."),
        H("Decentralized local authorities"),
        D("**Decentralized local authorities** (or local authorities) are bodies with their own legal personality and budget that manage local affairs "
          "through elected representatives. In Cameroon, these are the **councils** (municipal councils and city councils) and the **regional councils**.", title="Local authorities"),
        T("The Constitution (as revised in 1996) provides for regions and councils as decentralized authorities. "
          "Check the current General Code of Regional and Local Authorities for the exact organisation and powers."),
        H("The municipal council"),
        T("A **municipal council** (commune) covers a local area such as a town and the villages around it. "
          "Voters elect **councillors** in municipal elections. The councillors form the council and choose the **mayor** and deputy mayors from among themselves; check the current law on how this is done. "
          "A **city council** is the name for the council of a large city; in some large cities there are also sub-councils (arrondissements) headed by a mayor, "
          "and the city has an overall mayor or delegate depending on the law, so check the current rules."),
        IMG("f5cit-1-council-structure.svg", alt="Voters elect councillors, the municipal council decides, the mayor and deputy mayors carry out decisions with council staff, and State authority supervises",
            caption="Figure 1. Structure of a municipal council."),
        KEY("What councils do", "Functions in general terms.", cards=[
            ["Civil status", "Registering births, marriages and deaths (the mayor is the civil status registrar)."],
            ["Local services", "Markets, slaughterhouses, local roads, street lighting, waste collection, public toilets and water points where assigned."],
            ["Local development", "Planning and carrying out local projects; sometimes primary school and health centre buildings; protecting the local environment."],
            ["Local taxes and fees", "Collecting authorised local taxes and fees, such as market and licence fees, and receiving a share of national revenue."],
        ]),
        H("Regional councils"),
        T("A **regional council** is the decentralized authority at the level of a region. It is headed by a President of the Regional Council. "
          "Its members are regional councillors chosen as the law provides, and it deals with the region's economic, social, health, educational, cultural and sporting development. "
          "The regional authority is separate from the Governor, who represents the State (deconcentration). Check the current law on its organisation."),
        H("Money and control"),
        T("Councils have their own **budget**. Income comes from local taxes and fees, State transfers and other sources set by law. Councils must keep accounts and are supervised, so that they use public money properly."),
        T("Citizens can take part by voting, attending council meetings where the law allows, paying local taxes and fees, reporting problems, and taking part in local projects."),
        EX("Model answer plan 1", intro="State five functions of a municipal council in Cameroon.", steps=[
            S("Civil status", text="Registering births, marriages and deaths."),
            S("Markets", text="Building and managing markets and collecting market fees."),
            S("Roads and sanitation", text="Maintaining local roads and organising waste collection."),
            S("Social services", text="Helping with local schools, water points or health centres where the law gives this power."),
            S("Development planning", text="Preparing and carrying out local development projects."),
        ]),
        EX("Model answer plan 2", intro="Explain the difference between a Divisional Officer and a Mayor.", steps=[
            S("Appointment", text="The DO is appointed by the President; the mayor is chosen through local elections (councillors are elected)."),
            S("Role", text="The DO represents the State in the sub-division; the mayor runs the council."),
            S("Authority type", text="The DO is part of deconcentration; the council is a decentralized authority."),
            S("Relation", text="They work together; the State supervises the council."),
        ]),
        H("Common mistakes"),
        MISTAKE("Calling the Mayor a State representative", "The mayor is the executive of a decentralized authority, not an appointed representative of the State."),
        MISTAKE("Mixing the Regional Council with the Governor", "The Governor represents the State; the regional council is a decentralized authority headed by its own President."),
        MISTAKE("Giving exact figures or procedures from memory", "Say 'check the current law' for details such as the number of councillors or how mayors are chosen."),
        QUIZ("Which official registers births and marriages in a council?",
             ["The mayor, acting as civil status registrar", "The SDO", "The Governor", "A traditional ruler"], 0,
             "In councils the mayor (or a representative) is the civil status registrar.",
             hint="Think about the office where birth certificates are issued.",
             feedback=["", "The SDO is a State official, not the registrar.", "The Governor heads the region.", "Chiefs help the administration but do not register civil events."]),
        QUIZ("Which of these is a decentralized local authority?",
             ["A region headed by a Governor", "A municipal council", "A division", "A police station"], 1,
             "A municipal council has its own legal personality and an elected body.",
             hint="Which one is elected?",
             feedback=["A region as a State unit is headed by an appointed Governor.", "", "A division is an administrative unit.", "A police station is part of the State's administration."]),
        H("Practice questions"),
        PQ("Name two types of decentralized local authority in Cameroon.", "Municipal (city) councils and regional councils."),
        PQ("State three functions of a council.", "Civil status registration; markets; local roads and sanitation; local development projects; collecting local fees."),
        PQ("Give two sources of income of a council.", "Local taxes and fees (for example market fees); transfers from the State; other sources set by law."),
        PQ("How can citizens take part in local government?", "By voting in municipal elections; attending meetings; paying local taxes and fees; reporting problems; taking part in local projects."),
        SUM("Local authorities are councils and regional councils, with legal personality and a budget.",
            "Voters elect councillors; the council has a mayor who runs it and acts as civil status registrar.",
            "Councils handle civil status, markets, local roads and development.",
            "Regional councils work for the development of a region and are separate from the Governor.",
            "Check the current law for exact rules."),
    ],
))

# ------------------------------------------------------------------ 9. Constitutional evolution
LESSONS.append(lesson(
    module=M3,
    topic="Constitutional evolution of Cameroon",
    title="Constitutions of Cameroon from 1960 to 1996 and 2008",
    slug="cit1-constitutional-evolution",
    minutes=22,
    summary="What a constitution is and the main stages of Cameroon's constitutional history: the 1960 constitution, the federal constitution of 1961, the unitary State of 1972, the 1996 revision and the 2008 revision. Check dates and article numbers in the current text.",
    objectives=[
        "Define a constitution and state its purposes",
        "Place the main constitutional stages on a timeline",
        "Describe the change from a federal to a unitary State and its general meaning",
        "Name major features introduced by the 1996 revision",
    ],
    key_concepts=["Constitution", "Federation", "Unitary State", "Referendum", "Revision", "Separation of powers", "Decentralized unitary State"],
    blocks=[
        H("Introduction"),
        T("Every football match needs rules: the pitch, the number of players, the referee's powers. A country also needs a basic rulebook: "
          "how it is governed, who makes laws, what rights citizens have. This rulebook is the constitution."),
        D("A **constitution** is the highest law of a country. It sets out how the State is organised, the powers of its institutions and the rights and duties of citizens. "
          "All other laws must obey it.", title="Constitution"),
        H("Why does a country need a constitution?"),
        T("It gives the country a clear structure. It limits those who hold power so that they cannot rule just as they wish. "
          "It protects citizens' rights. And it gives stability: rules for the transfer of power and the settlement of disputes."),
        H("The main stages"),
        T("This is a summary at the level you need for O Level. **Dates and article numbers: check the current text and your textbook.**"),
        IMG("f5cit-1-constitution-timeline.svg", alt="Timeline of Cameroon constitutions in 1960, 1961, 1972, 1984, 1996 and 2008",
            caption="Figure 1. Main constitutional stages (check the dates in your textbook)."),
        KEY("Constitutional stages", "Learn each stage with one key feature.", cards=[
            ["1960", "French Cameroun became independent on 1 January 1960 as the Republic of Cameroon, under a constitution adopted in 1960 that set up a presidential-type system with a National Assembly."],
            ["1961", "After the plebiscites of February 1961 in the Southern Cameroons, the two parts joined on 1 October 1961. A federal constitution created the Federal Republic of Cameroon with two federated states, East and West Cameroon, and a federal government."],
            ["1972", "A referendum on 20 May 1972 replaced federalism with a unitary State, called the United Republic of Cameroon. 20 May became the National Day."],
            ["1984", "The name of the State became the Republic of Cameroon."],
            ["1996", "A major revision (law of 18 January 1996) introduced or confirmed, among other things: a decentralized unitary State, regional and local authorities, the creation of a Senate, a Constitutional Council and rules on the presidential term; check the current text."],
            ["2008", "A further revision (April 2008) changed provisions on the presidential term and certain other matters; check the current text for exact details."],
        ], note="Federal means two levels of State with their own powers. Unitary means one State with one central authority, even if power is decentralized."),
        D("A **federation** is a State made up of several federated states, each with its own government and powers, together with a federal government. "
          "A **unitary State** has one central government and one legal system for the whole territory; local authorities exist but within the unitary State.",
          title="Federal and unitary"),
        H("Key features of the current constitution"),
        T("The current text is the constitution of 1996 as revised. It declares Cameroon a **decentralized unitary State**, with **English and French** as official languages of equal status. "
          "It provides for separate executive, legislative and judicial powers; guarantees fundamental rights in its preamble; and sets out the role of institutions such as the President, Government, National Assembly, Senate, "
          "judiciary and Constitutional Council. A **referendum** is a direct vote by citizens on a question such as a constitutional change. The revision procedure is set out in the Constitution itself; check the current text."),
        EX("Model answer plan 1", intro="Explain why a country needs a constitution.", steps=[
            S("Definition", text="The highest law that sets out how the State is organised and the rights of citizens."),
            S("Structure and order", text="It states who does what: the executive, the legislature and the judiciary."),
            S("Limit on power", text="Rulers must obey it; it prevents abuse."),
            S("Rights", text="It protects citizens' fundamental rights and freedoms."),
            S("Stability", text="It provides rules for the transfer of power and for settling disputes."),
        ]),
        EX("Model answer plan 2", intro="Trace the change from a federal State to a unitary State in Cameroon.", steps=[
            S("1961", text="Reunification: federal constitution creating the Federal Republic with East and West Cameroon."),
            S("1972", text="Referendum of 20 May 1972 ended federalism and created the United Republic of Cameroon."),
            S("1984", text="The name became the Republic of Cameroon."),
            S("1996", text="The revision confirmed a decentralized unitary State with regions and councils."),
            S("Note", text="Check the exact dates and details in your textbook."),
        ]),
        H("Common mistakes"),
        MISTAKE("Mixing up federal and unitary", "Federal: federated states plus a federal government. Unitary: one central State; decentralization does not make it federal."),
        MISTAKE("Giving exact article numbers from memory", "If unsure, say what the constitution provides and note 'check the current text'."),
        MISTAKE("Mixing up 1961 and 1972", "1961: reunification and the federal constitution. 1972: referendum creating the unitary State."),
        QUIZ("The referendum of 20 May 1972 led to",
             ["Independence of French Cameroun", "A unitary State, the United Republic of Cameroon", "The creation of the Federal Republic", "The first Senate"], 1,
             "The 1972 referendum replaced federalism with a unitary State.",
             hint="Which form of State replaced federalism?",
             feedback=["Independence came on 1 January 1960.", "", "The Federal Republic dated from 1961.", "The Senate was provided for in the 1996 revision."]),
        QUIZ("A constitution is",
             ["A tax law", "The highest law of a country", "A court of appeal", "A local council"], 1,
             "A constitution is the supreme law that sets out how the State is organised.",
             hint="All other laws must obey it.",
             feedback=["A tax law is an ordinary law.", "", "A court of appeal is a court.", "A council is a local authority."]),
        H("Practice questions"),
        PQ("Define a constitution.", "The highest law of a country, setting out how the State is organised, the powers of institutions and the rights and duties of citizens."),
        PQ("Give two purposes of a constitution.", "To organise the State and divide powers; to limit rulers; to protect rights; to give stability."),
        PQ("Name the form of State created in 1961 and the one created in 1972.", "1961: a federal State (Federal Republic of Cameroon). 1972: a unitary State (United Republic of Cameroon)."),
        PQ("State two things introduced or confirmed by the 1996 revision.", "A decentralized unitary State with regions and councils; the Senate; the Constitutional Council (check the current text)."),
        SUM("A constitution is the highest law; it organises the State, limits power and protects rights.",
            "1960: independence constitution; 1961: federal constitution at reunification.",
            "1972: referendum creating a unitary State; 1984: name Republic of Cameroon.",
            "1996: major revision with decentralization, a Senate and a Constitutional Council; 2008: further revision.",
            "Check dates and article numbers."),
    ],
))

# ------------------------------------------------------------------ 10. National symbols
LESSONS.append(lesson(
    module=M3,
    topic="National symbols",
    title="National symbols: flag, anthem, motto, coat of arms and seal",
    slug="cit1-national-symbols",
    minutes=18,
    summary="The symbols of the State: the flag (green, red, yellow with a star), the national anthem, the motto 'Peace - Work - Fatherland', the coat of arms and the seal, what each stands for and how to treat them with respect.",
    objectives=[
        "Name the national symbols of Cameroon",
        "Describe the national flag and the national motto",
        "Explain the importance of national symbols",
        "State how citizens should respect the symbols",
    ],
    key_concepts=["National symbol", "Flag", "Anthem", "Motto", "Coat of arms", "Seal", "Patriotism"],
    blocks=[
        H("Introduction"),
        T("At school assembly, students stand to sing the national anthem while the flag rises. When an athlete wins a medal for Cameroon, "
          "the flag and the anthem move people to pride. National symbols show who we are as a country."),
        D("**National symbols** are official emblems that represent a country, its unity and its values. In Cameroon they include the flag, the anthem, "
          "the motto, the coat of arms and the seal.", title="National symbols"),
        H("The flag"),
        T("The national flag has **three vertical stripes of equal width: green, red and yellow**, from the hoist (the side nearest the pole). "
          "A **yellow star** is placed in the centre of the red stripe."),
        IMG("f5cit-1-flag.svg", alt="Schematic flag with three equal vertical stripes of green, red and yellow and a yellow star on the middle stripe",
            caption="Figure 1. The national flag, drawn schematically."),
        T("The meanings given to the colours are commonly taught like this (textbooks may vary, check yours): **green** for the forests and hope, "
          "**red** for unity (and the sacrifices that built it), **yellow** for the sun and the savannah (and happiness), and the **star** for unity of the nation. "
          "Pan-African colours (green, red, yellow) are shared by many African flags."),
        H("The motto"),
        D("The **national motto** of Cameroon is **Peace, Work, Fatherland** (in French: Paix, Travail, Patrie).", title="Motto"),
        T("It reminds citizens to live in peace, to work hard for development, and to love and serve their country."),
        H("The anthem"),
        T("The **national anthem** is a song that represents the nation on formal occasions. Its title is **O Cameroon, Cradle of our Forefathers** "
          "(in French: Ô Cameroun, berceau de nos ancêtres). It exists in English and French versions. "
          "It is sung at official ceremonies, at school, at sports events and at national celebrations, and everyone should stand and show respect."),
        H("The coat of arms and the seal"),
        T("The **coat of arms** is the official emblem of the State, used on official documents and buildings. It shows the national motto and symbols of the State; "
          "its exact design is described in law and your textbook (a shield, a star and elements representing justice are among the items commonly described; check the official description)."),
        T("The **seal of the State** is the official stamp used to certify important State documents."),
        KEY("Quick reference", "Learn these five.", cards=[
            ["Flag", "Green, red, yellow in vertical stripes; yellow star on the red stripe."],
            ["Motto", "Peace, Work, Fatherland."],
            ["Anthem", "O Cameroon, Cradle of our Forefathers."],
            ["Coat of arms", "Official emblem of the State, used on official documents."],
            ["Seal", "Official stamp of the State on important documents."],
        ]),
        H("Why do symbols matter? How should we treat them?"),
        T("Symbols give citizens a shared identity. They promote unity and patriotism and show Cameroon to the world. "
          "Respect them: stand for the anthem, do not tear, burn or dirty the flag, do not use the flag as a mat or decoration in a disrespectful way, and teach children to respect them. "
          "Rules on use of the flag and anthem are set by law; check the current rules."),
        EX("Model answer plan 1", intro="Describe the national flag of Cameroon.", steps=[
            S("Layout", text="Three equal vertical stripes."),
            S("Colours", text="Green, red and yellow, in that order from the hoist."),
            S("Star", text="A yellow star in the centre of the red stripe."),
            S("Meaning", text="Green: forests and hope; red: unity; yellow: sun and savannah; star: unity of the nation (check your textbook)."),
        ]),
        EX("Model answer plan 2", intro="Explain why national symbols are important.", steps=[
            S("Identity", text="They represent the nation at home and abroad."),
            S("Unity", text="They bring citizens together beyond region, language or religion."),
            S("Pride and patriotism", text="They create love for the country."),
            S("Respect", text="They must be used and treated with respect."),
        ]),
        H("Common mistakes"),
        MISTAKE("Putting the star on the wrong stripe", "The star is in the centre of the red (middle) stripe, not on the green or yellow stripe."),
        MISTAKE("Using the wrong motto", "The motto is Peace, Work, Fatherland. Do not confuse it with other mottos."),
        MISTAKE("Mixing symbols and institutions", "The flag and anthem are symbols; the National Assembly and Senate are institutions."),
        QUIZ("What colour is the middle stripe of the national flag?",
             ["Green", "Red", "Yellow", "White"], 1,
             "The red stripe is in the middle and carries the yellow star.",
             hint="The star is in the centre stripe.",
             feedback=["Green is on the hoist side.", "", "Yellow is on the fly side.", "White is not in the flag."]),
        QUIZ("The national motto of Cameroon is",
             ["Unity, Progress, Justice", "Peace, Work, Fatherland", "Freedom, Equality, Fraternity", "Faith, Hope, Charity"], 1,
             "The motto is Peace, Work, Fatherland.",
             hint="It starts with Peace.",
             feedback=["This is not the Cameroon motto.", "", "This is the French Republic's motto.", "This is not the motto of Cameroon."]),
        H("Practice questions"),
        PQ("Name four national symbols of Cameroon.", "Flag, anthem, motto, coat of arms (and seal)."),
        PQ("What is the national motto?", "Peace, Work, Fatherland."),
        PQ("Describe the national flag.", "Three equal vertical stripes of green, red and yellow, with a yellow star in the centre of the red stripe."),
        PQ("Give two ways to show respect for national symbols.", "Stand and keep quiet during the anthem; do not damage or insult the flag; use symbols properly."),
        SUM("The symbols are the flag, anthem, motto, coat of arms and seal.",
            "The flag is green, red, yellow with a star on the red stripe.",
            "The motto is Peace, Work, Fatherland.",
            "The anthem is O Cameroon, Cradle of our Forefathers.",
            "Symbols give identity and unity and must be respected."),
    ],
))

# ------------------------------------------------------------------ 11. The executive
LESSONS.append(lesson(
    module=M3,
    topic="The executive",
    title="The executive: the President, the Prime Minister and the Government",
    slug="cit1-the-executive",
    minutes=22,
    summary="The three arms of government and the executive in particular: the President of the Republic (head of State), the Prime Minister (head of Government) and ministers, with their main roles. Check the current text of the Constitution.",
    objectives=[
        "Explain the separation of powers and name the three arms of government",
        "Describe the role of the President of the Republic",
        "Describe the role of the Prime Minister and the Government",
        "Explain the work of ministries and how the executive is held to account",
    ],
    key_concepts=["Separation of powers", "Executive", "Head of State", "Head of Government", "Prime Minister", "Minister", "Decree"],
    blocks=[
        H("Introduction"),
        T("When a new school is opened, a road is built or a national exam is organised, someone must decide, plan and carry out the work. "
          "The institutions that do this are called the executive."),
        H("Three arms of government"),
        D("**Separation of powers** means dividing the work of government among three arms so that no one holds all power: the **executive** carries out laws and runs the State, "
          "the **legislature** makes laws, and the **judiciary** applies laws and settles disputes.", title="Separation of powers"),
        IMG("f5cit-1-three-powers.svg", alt="Three boxes: executive (President and Government, carries out the laws), legislature (National Assembly and Senate, makes the laws), judiciary (the courts, applies the laws)",
            caption="Figure 1. The three arms of government."),
        T("In practice the arms work together and check each other. For example, the legislature votes the budget that the executive spends. "
          "Check how the Constitution describes their cooperation."),
        H("The President of the Republic"),
        D("The **President of the Republic** is the **Head of State**. He represents the nation, ensures respect for the Constitution and the proper working of public institutions, "
          "and is the guarantor of national independence and territorial integrity.", title="President"),
        T("The President is elected by **direct universal suffrage** (all qualified adult citizens vote directly) for a term fixed in the Constitution. "
          "Check the current text for the term, the age and other conditions, and for what happens if the office becomes vacant."),
        KEY("Main powers of the President", "In general terms; check the exact articles.", cards=[
            ["Head of Government work", "Appoints the Prime Minister and, on the Prime Minister's proposal, the other members of the Government; sets the broad policy."],
            ["Laws and decrees", "Promulgates (signs into force) laws passed by Parliament and signs decrees."],
            ["Appointments", "Appoints to senior civil and military posts, including Governors, SDOs and DOs, and chairs the Higher Judicial Council."],
            ["Defence and foreign affairs", "Commander-in-chief of the armed forces; accredits and receives ambassadors; negotiates and signs treaties."],
            ["Special powers", "Pardons; may call a referendum; powers in a state of emergency or siege as the Constitution sets out."],
        ]),
        H("The Prime Minister and the Government"),
        D("The **Prime Minister** is the **Head of Government**. He is appointed by the President, directs and coordinates the Government's work and is responsible to the President.", title="Prime Minister"),
        T("The **Government** is made up of the Prime Minister and the ministers (including ministers delegate and secretaries of state). "
          "Each minister heads a **ministry**, for example Education or Health, which carries out policy in that area. "
          "Together they carry out national policy as the President sets it, prepare bills and the budget, and manage the civil service."),
        T("Ministers are assisted by civil servants who work in ministries, in regional and divisional offices (deconcentrated services) and in public institutions."),
        H("Accountability"),
        T("Executive power is not unlimited. The Constitution and the laws bind the President and Government. Parliament votes the budget and may question ministers "
          "(check the procedures in the current text). Courts may rule on whether administrative acts respect the law, and the media and citizens can criticise public policy within the law."),
        EX("Model answer plan 1", intro="State five powers of the President of the Republic.", steps=[
            S("Appointments", text="Appoints the Prime Minister and members of the Government; appoints senior officials such as Governors."),
            S("Laws", text="Promulgates laws and signs decrees."),
            S("Armed forces", text="Is commander-in-chief of the armed forces."),
            S("Foreign affairs", text="Accredits ambassadors and signs treaties."),
            S("Justice and emergencies", text="Chairs the Higher Judicial Council, has the right of pardon and special powers in emergencies."),
        ]),
        EX("Model answer plan 2", intro="Distinguish between the Head of State and the Head of Government.", steps=[
            S("Head of State", text="The President: represents the nation; ensures respect for the Constitution; has wide powers."),
            S("Head of Government", text="The Prime Minister: directs the Government's work; appointed by the President; responsible to the President."),
            S("Relation", text="The Prime Minister works under the President's policy direction."),
            S("Note", text="Check the exact wording in the current text."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying the Prime Minister is elected by the people", "The President is elected by direct universal suffrage. The Prime Minister is appointed by the President."),
        MISTAKE("Mixing the arms", "Making laws: legislature. Carrying them out: executive. Applying them in disputes: judiciary."),
        MISTAKE("Listing powers without links to the Constitution", "Explain each power briefly and note 'as the Constitution provides'."),
        QUIZ("Who appoints the Prime Minister?",
             ["The National Assembly", "The President of the Republic", "The Supreme Court", "The people by direct vote"], 1,
             "The Prime Minister is appointed by the President of the Republic.",
             hint="Who is the Head of State?",
             feedback=["The Assembly votes laws; it does not appoint the Prime Minister.", "", "Courts do not appoint the head of government.", "The President is elected directly; the Prime Minister is appointed."]),
        QUIZ("Which arm of government carries out laws and runs the State?",
             ["The legislature", "The judiciary", "The executive", "The press"], 2,
             "The executive (President and Government) carries out laws and runs the State.",
             hint="Think of the President and ministers.",
             feedback=["The legislature makes laws.", "The judiciary applies laws in disputes.", "", "The press is not an arm of government."]),
        H("Practice questions"),
        PQ("Name the three arms of government.", "The executive, the legislature and the judiciary."),
        PQ("Who is the Head of State?", "The President of the Republic."),
        PQ("State three powers of the President.", "Appoints the Prime Minister and the Government; promulgates laws and signs decrees; is commander-in-chief; signs treaties; appoints to senior posts."),
        PQ("What does the Government do?", "Carries out national policy under the President's direction; ministries manage public services; prepares bills and the budget."),
        SUM("Separation of powers divides government into executive, legislature and judiciary.",
            "The President is Head of State, elected by direct universal suffrage.",
            "The Prime Minister is Head of Government and is appointed by the President.",
            "Ministers head ministries and carry out policy.",
            "Executive power is limited by the Constitution and the laws."),
    ],
))

# ------------------------------------------------------------------ 12. The legislature
LESSONS.append(lesson(
    module=M3,
    topic="The legislature",
    title="The legislature: the National Assembly and the Senate",
    slug="cit1-the-legislature",
    minutes=22,
    summary="Parliament in Cameroon: the National Assembly and the Senate, how members are chosen, what they do (make laws, vote the budget, control the Government) and how a bill becomes law. Check the current text.",
    objectives=[
        "Define the legislature and name its two houses",
        "Describe how deputies and senators are chosen",
        "List the main functions of Parliament",
        "Describe the steps by which a bill becomes law",
    ],
    key_concepts=["Legislature", "Parliament", "National Assembly", "Senate", "Deputy", "Senator", "Bill", "Act of Parliament"],
    blocks=[
        H("Introduction"),
        T("Rules for taxes, the school curriculum, the Labour Code and many other subjects start as proposals and become law only after debate and a vote. "
          "The institution where this happens is Parliament, the legislature."),
        D("The **legislature** is the arm of government that makes laws, votes the budget and controls the Government. "
          "In Cameroon it is called **Parliament** and has two houses: the **National Assembly** and the **Senate**.", title="Legislature"),
        H("The National Assembly"),
        T("The National Assembly is made up of **deputies** elected by universal suffrage for a five-year term (check the current text and the current number of seats, which is around 180). "
          "Deputies represent the nation, not only their own constituency or party. A **constituency** is the area whose voters elect a deputy or deputies."),
        T("It is led by a **President of the National Assembly** and a bureau (a small group of officers) elected by the deputies; it works through committees that study bills in detail."),
        H("The Senate"),
        T("The Senate, created by the 1996 revision, represents the regions and local authorities. **Senators** serve a fixed term (five years; check the current text). "
          "There are **ten senators per region**: seven elected by regional councillors and three appointed by the President, giving a total of 100. "
          "Check the current numbers."),
        T("The Senate is led by the **President of the Senate**. Under the Constitution, the President of the Senate has a role in the interim if the office of President of the Republic becomes vacant; check the current text."),
        KEY("Functions of Parliament", "Learn these four.", cards=[
            ["Making laws", "Debating and voting bills; laws may be proposed by the President or the Government (government bills) or by members of Parliament (private members' bills)."],
            ["Voting the budget", "Examining and voting the State budget, which fixes planned income and spending."],
            ["Controlling the Government", "Questioning ministers (written and oral questions), setting up committees, following how laws are applied."],
            ["Representation", "Speaking for citizens, bringing local concerns to the national level and ratifying certain treaties."],
        ]),
        T("Parliament meets in **ordinary sessions** during the year (three sessions are usual, in March, June and November) and may also meet in extraordinary sessions. Check the current text."),
        H("How a bill becomes law"),
        T("A **bill** is a proposed law. In general terms the steps are: (1) a bill is **introduced** by the Government or by members of Parliament; "
          "(2) a **committee** studies it and may propose amendments; (3) it is **debated** and **voted** in the house or houses of Parliament as the Constitution provides; "
          "(4) once adopted, it is sent to the President for **promulgation**, which means signing it into force; (5) it is **published** in an official gazette. "
          "The procedure for each type of law is set by the Constitution and by the rules of procedure of each house; check the current text."),
        EX("Model answer plan 1", intro="Explain four functions of the National Assembly.", steps=[
            S("Law making", text="Debates and votes bills."),
            S("Budget", text="Examines and votes the State budget."),
            S("Control of the Government", text="Asks ministers questions; sets up committees."),
            S("Representation", text="Deputies represent the people's views."),
        ]),
        EX("Model answer plan 2", intro="Distinguish between the National Assembly and the Senate.", steps=[
            S("National Assembly", text="Deputies elected by the voters for a five-year term; the lower, popular house."),
            S("Senate", text="Created in 1996; represents regions and local authorities; most senators are chosen by regional councillors, and some are appointed by the President."),
            S("Common role", text="Both make up Parliament and take part in lawmaking."),
            S("Note", text="Check the current numbers and procedures."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying Parliament applies laws", "Parliament makes laws. The courts apply laws to cases and the executive carries them out."),
        MISTAKE("Saying all senators are elected by the people", "Senators are elected indirectly by regional councillors, and some are appointed by the President. Check the current text."),
        MISTAKE("Writing exact numbers as certain", "Seat numbers and term lengths can change with revisions. Say 'check the current text'."),
        QUIZ("Which institution is mainly responsible for making laws?",
             ["The courts", "Parliament", "The police", "Ministers alone"], 1,
             "Parliament, made up of the National Assembly and the Senate, makes laws.",
             hint="The word 'legislature' comes from 'legislate'.",
             feedback=["Courts apply laws.", "", "The police enforce laws.", "Ministers carry out policy; laws are made by Parliament."]),
        QUIZ("Which of these is a function of Parliament?",
             ["Judging criminal cases", "Voting the State budget", "Appointing Governors", "Commanding the army"], 1,
             "Parliament examines and votes the budget.",
             hint="Which function involves money?",
             feedback=["Judging is for the courts.", "", "Governors are appointed by the President.", "The President is commander-in-chief."]),
        H("Practice questions"),
        PQ("Name the two houses of Parliament in Cameroon.", "The National Assembly and the Senate."),
        PQ("Who are deputies and how are they chosen?", "Members of the National Assembly, elected by universal suffrage by voters."),
        PQ("State three functions of Parliament.", "Making laws; voting the budget; controlling the Government; representing citizens."),
        PQ("Describe the steps in making a law.", "Introduction of a bill; committee study; debate and vote; promulgation by the President; publication."),
        SUM("The legislature makes laws, votes the budget and controls the Government.",
            "Parliament has two houses: the National Assembly (deputies) and the Senate (senators).",
            "Senators are mostly chosen by regional councillors, with some appointed by the President; check the current text.",
            "A bill is introduced, studied, debated, voted, promulgated and published.",
            "Check numbers and procedures in the current text."),
    ],
))

# ------------------------------------------------------------------ 13. The judiciary
LESSONS.append(lesson(
    module=M3,
    topic="The judiciary",
    title="The judiciary: courts, judges and the Constitutional Council",
    slug="cit1-the-judiciary",
    minutes=22,
    summary="How justice is organised in Cameroon: customary courts, Courts of First Instance, High Courts, Courts of Appeal, the Supreme Court and the Constitutional Council; the independence of judges and the main principles of a fair trial.",
    objectives=[
        "Define the judiciary and state its role",
        "Arrange the main courts from the lowest to the highest",
        "Explain the role of the Constitutional Council and the Higher Judicial Council",
        "State principles of a fair trial and the independence of judges",
    ],
    key_concepts=["Judiciary", "Court", "Appeal", "Customary court", "Supreme Court", "Constitutional Council", "Fair trial", "Independence of judges"],
    blocks=[
        H("Introduction"),
        T("Two traders in Bamenda disagree about who owns a plot. A man is accused of stealing a motorbike in Douala. A family argues over an inheritance in Garoua. "
          "In each case, a neutral institution must decide according to the law: the courts."),
        D("The **judiciary** is the arm of government made up of courts and judges. It applies the law, settles disputes and punishes breaches of the law, "
          "independently of the executive and legislature.", title="Judiciary"),
        H("Kinds of case"),
        T("A **civil case** is a dispute between persons, such as a debt, land or a family matter. A **criminal case** is about an offence against the law, such as theft; "
          "the State prosecutes the accused. A **constitutional case** is about whether a law or an election respects the Constitution."),
        H("The ladder of courts"),
        IMG("f5cit-1-court-ladder.svg", alt="Ladder of courts from customary courts at the bottom to Courts of First Instance, High Courts, Courts of Appeal and the Supreme Court at the top",
            caption="Figure 1. The main courts from lowest to highest (check how your textbook describes the details)."),
        KEY("The main courts", "Check your textbook for exact powers and number of courts.", cards=[
            ["Customary courts", "Local courts that apply custom in matters such as marriage and family land, where custom applies; their decisions can be appealed."],
            ["Courts of First Instance", "Handle many ordinary civil and minor criminal cases."],
            ["High Courts", "Handle more serious cases; in each division (check the details)."],
            ["Courts of Appeal", "Hear appeals against decisions of lower courts; at region level."],
            ["Supreme Court", "The highest court of appeal in the ordinary system; in Yaounde. It also oversees public accounts through its audit bench (check)."],
        ]),
        D("An **appeal** is a request to a higher court to review the decision of a lower court. The higher the court, the wider its authority.", title="Appeal"),
        T("There are also military courts and, for some matters, specialised courts or tribunals. The legal system has two traditions: **common law** (rooted in the English system, "
          "used in the English-speaking regions) and **civil law** (rooted in the French system, used in the French-speaking regions). Check how they are combined today in the criminal and civil codes."),
        H("The Constitutional Council"),
        D("The **Constitutional Council** is the body that rules on whether laws and certain acts respect the Constitution.", title="Constitutional Council"),
        T("It was provided for in the 1996 revision and put in place later (check the date). In general terms it checks the constitutionality of laws, "
          "settles certain disputes between institutions and deals with disputes on elections such as presidential and legislative elections, and proclaims final results (check the current text for exact roles). "
          "It is a separate body from the ordinary courts."),
        H("Independence and fair trial"),
        T("The Constitution says that judicial power is independent of the executive and legislative powers. Judges are **magistrates**. "
          "The **Higher Judicial Council**, chaired by the President of the Republic, advises on the appointment and discipline of magistrates, which is meant to guarantee their independence (check the details)."),
        T("Principles of a **fair trial** include: **equality before the law** (everyone is judged by the same law); the **presumption of innocence** (a person is presumed innocent until proven guilty); "
          "the **right to defence** (the right to be heard and to have a lawyer); **public hearings** in most cases; and the **right to appeal**."),
        EX("Model answer plan 1", intro="Explain the role of the judiciary in a country.", steps=[
            S("Definition", text="Courts and judges that apply the law."),
            S("Settling disputes", text="Resolve civil disputes such as land and debts."),
            S("Punishing offences", text="Try criminal cases according to the law."),
            S("Protecting rights", text="Protect citizens against abuse and uphold the Constitution."),
            S("Independence", text="Judges must be independent to be fair."),
        ]),
        EX("Model answer plan 2", intro="Arrange the main courts of Cameroon from lowest to highest.", steps=[
            S("Lowest", text="Customary courts (where custom applies)."),
            S("Next", text="Courts of First Instance."),
            S("Next", text="High Courts, then Courts of Appeal."),
            S("Highest", text="Supreme Court. The Constitutional Council is separate and rules on constitutional matters."),
        ]),
        H("Common mistakes"),
        MISTAKE("Putting the Constitutional Council at the top of the ordinary ladder", "It is a separate body for constitutional questions. The Supreme Court is the highest ordinary court."),
        MISTAKE("Saying the President sentences criminals", "Judges decide cases. The President has the right of pardon but does not try cases."),
        MISTAKE("Confusing civil and criminal cases", "Civil: dispute between persons. Criminal: offence against the law prosecuted by the State."),
        QUIZ("Which is the highest court of appeal in the ordinary court system?",
             ["Court of First Instance", "High Court", "Court of Appeal", "Supreme Court"], 3,
             "The Supreme Court is the highest court in the ordinary system.",
             hint="Look at the top of the ladder.",
             feedback=["This is a lower court.", "A higher court may review its decisions.", "Decisions of the Court of Appeal can be taken further.", ""]),
        QUIZ("A person is presumed innocent until",
             ["He is arrested", "He is proved guilty by a court", "He is accused by a neighbour", "He is questioned by police"], 1,
             "A person is presumed innocent until a court proves guilt according to the law.",
             hint="Who decides on guilt?",
             feedback=["Arrest does not prove guilt.", "", "An accusation is not proof.", "Questioning does not prove guilt."]),
        H("Practice questions"),
        PQ("Define the judiciary.", "The arm of government made up of courts and judges that applies the law and settles disputes."),
        PQ("Name three courts in Cameroon.", "Any three of: customary court; Court of First Instance; High Court; Court of Appeal; Supreme Court; Constitutional Council."),
        PQ("State the role of the Constitutional Council.", "It checks that laws respect the Constitution and deals with election disputes as the Constitution provides (check the current text)."),
        PQ("State two principles of a fair trial.", "Equality before the law; presumption of innocence; right to defence; public hearing; right of appeal."),
        SUM("The judiciary applies the law and settles disputes independently.",
            "Courts from lowest to highest: customary, First Instance, High Court, Court of Appeal, Supreme Court.",
            "The Constitutional Council is separate and deals with constitutional matters and election disputes.",
            "Judges are independent; the Higher Judicial Council deals with magistrates' careers.",
            "A fair trial includes equality before the law, presumption of innocence and the right to a defence."),
    ],
))

# ------------------------------------------------------------------ 14. The electoral process
LESSONS.append(lesson(
    module=M3,
    topic="The electoral process",
    title="The electoral process and ELECAM",
    slug="cit1-the-electoral-process",
    minutes=22,
    summary="How elections work in Cameroon: types of election, the right to vote, registration, the role of ELECAM, the voting process, results and the Constitutional Council, and the duties of a responsible voter. Check the current Electoral Code.",
    objectives=[
        "Define an election and explain why elections matter in a democracy",
        "Name the types of election held in Cameroon",
        "Describe the main steps of an election and the role of ELECAM",
        "State the duties of a responsible voter",
    ],
    key_concepts=["Election", "Universal suffrage", "Secret ballot", "Voter registration", "ELECAM", "Polling station", "Electoral Code", "Voter card"],
    blocks=[
        H("Introduction"),
        T("On voting day, people in Maroua, Limbe or Ebolowa queue at polling stations, show their cards, enter a booth and drop a ballot paper in a box. "
          "This simple act is how citizens choose those who will speak and act for them."),
        D("An **election** is a process by which citizens choose their representatives or decide a public question by voting.", title="Election"),
        T("Elections matter because they give leaders their authority, let citizens influence government, and allow peaceful change of office. "
          "A good election is free, fair, regular and secret."),
        H("Principles and types of election"),
        T("Voting is by **universal suffrage** (all qualified adult citizens may vote), **equal** (one person, one vote) and **secret** (nobody should know how you voted). "
          "These principles are in the Constitution and the **Electoral Code**; check the current texts."),
        KEY("Main elections", "Types of election in Cameroon.", cards=[
            ["Presidential election", "Citizens elect the President of the Republic by direct vote."],
            ["Legislative elections", "Citizens elect deputies of the National Assembly."],
            ["Municipal elections", "Citizens elect councillors for the councils."],
            ["Regional and senatorial elections", "Regional councillors are elected as the law provides, and they in turn elect most senators (indirect election)."],
            ["Referendum", "Citizens vote directly on a question put to them."],
        ]),
        H("Who can vote?"),
        T("In general terms, you may vote if you are a Cameroonian citizen of the age fixed by law (check the current voting age), you are registered on the electoral list, "
          "you have your voter card or the document the law requires, and you have not lost your civic rights by a court decision."),
        H("ELECAM"),
        D("**ELECAM** (Elections Cameroon) is the independent body responsible for organising, managing and supervising elections and referendums in Cameroon. "
          "It was created by law in 2006 and started work soon after (check the dates).", title="ELECAM"),
        T("ELECAM's tasks include registering voters and updating the electoral lists, issuing voter cards, setting up polling stations, "
          "organising voting and counting, and publishing results from its level of responsibility. Other bodies also play roles under the Electoral Code: "
          "for example, administrative authorities, political parties and observers, and the Constitutional Council for disputes and final results of some elections. Check the current text."),
        IMG("f5cit-1-election-flow.svg", alt="Five steps of an election: voter registration, campaign, voting day, counting, results",
            caption="Figure 1. Main steps of an election."),
        KEY("From registration to results", "A general sequence.", cards=[
            ["1. Registration", "Voters register on the electoral list and get their cards."],
            ["2. Candidates and campaign", "Candidates are registered; they and their parties present programmes within the law."],
            ["3. Voting day", "Voters go to polling stations; identity is checked; each voter votes in secret and puts the ballot in the box."],
            ["4. Counting", "At the end of voting the ballots are counted in public, with representatives of candidates and observers present."],
            ["5. Results and disputes", "Results are compiled and announced; disputes go to the body set by law, such as the Constitutional Council for certain elections."],
        ]),
        H("The responsible voter"),
        T("A responsible voter registers, keeps the voter card safe, learns about the candidates' programmes, votes freely without being bought or forced, "
          "respects other people's choices, does not use violence or spread false news, and accepts results announced through lawful procedures or uses lawful channels to challenge them."),
        EX("Model answer plan 1", intro="Explain why voting is important in a democracy.", steps=[
            S("Choice of leaders", text="Voters choose who will represent them."),
            S("Authority", text="Elected leaders have the authority of the people's votes."),
            S("Accountability", text="Leaders know they will face voters again."),
            S("Peaceful change", text="Elections give a peaceful way to change office-holders."),
        ]),
        EX("Model answer plan 2", intro="Describe the role of ELECAM.", steps=[
            S("Identity", text="Independent body created by law to organise and supervise elections."),
            S("Registration", text="Updates the voter lists and issues voter cards."),
            S("Operations", text="Sets up polling stations and organises voting and counting."),
            S("Results", text="Publishes results from its level; disputes may go to the Constitutional Council or the courts as the law provides."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying ELECAM proclaims every final result", "Check the Electoral Code. The Constitutional Council proclaims final results for some elections."),
        MISTAKE("Confusing registration with voting", "Registration puts you on the list. Voting is the act on election day."),
        MISTAKE("Saying the secret ballot means nobody can watch", "The vote is secret, but counting is public, with observers and representatives, so people can check the process."),
        QUIZ("What does ELECAM do?",
             ["Makes laws", "Organises and supervises elections", "Tries criminal cases", "Collects taxes"], 1,
             "ELECAM is the body responsible for organising, managing and supervising elections.",
             hint="The name stands for Elections Cameroon.",
             feedback=["Parliament makes laws.", "", "Courts try criminal cases.", "Tax offices collect taxes."]),
        QUIZ("The secret ballot means that",
             ["Results are hidden", "Nobody should know how you voted", "Only some people may vote", "Voting happens at night"], 1,
             "Secrecy protects each voter's freedom to choose.",
             hint="The secret concerns the voter's choice.",
             feedback=["Results are published.", "", "Universal suffrage means all qualified adults may vote.", "Voting hours are set by law."]),
        H("Practice questions"),
        PQ("Define an election.", "A process by which citizens choose their representatives or decide a public question by voting."),
        PQ("Name three types of election in Cameroon.", "Presidential, legislative, municipal, regional (indirect senatorial) elections and referendums."),
        PQ("State two roles of ELECAM.", "Registering voters; organising polling and counting; supervising elections; publishing results from its level."),
        PQ("State three duties of a responsible voter.", "Register; vote freely; respect others' choices; avoid violence and false news; accept results through lawful procedures."),
        SUM("An election is a way for citizens to choose representatives or decide a question.",
            "Suffrage is universal, equal and secret.",
            "Elections include presidential, legislative, municipal, regional (and senatorial) elections and referendums.",
            "ELECAM organises and supervises elections; the Constitutional Council deals with disputes and final results of certain elections.",
            "A responsible voter registers, votes freely and respects the law."),
    ],
))

