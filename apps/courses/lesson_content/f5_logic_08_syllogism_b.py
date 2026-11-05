"""Form 5 Logic (GCE O Level 0590), module "Mediate Inference (Arguments)", second half:
the moods, Venn testing, translation into standard form, and the general rules and fallacies of the
categorical syllogism (syllabus 1.7.5 to 1.7.8).

Every validity claim here was checked by brute force over all fillings of the eight Venn regions
(traditional view: the three terms are not empty; Boolean view: any region may be empty).
Draft content: check against the official syllabus and your textbook."""

from .dsl import *  # noqa: F403

COURSE = ("logic", "form-5")

MODULE = "Mediate Inference (Arguments)"

LESSONS = [
    # ------------------------------------------------------------------ The moods
    lesson(
        module=MODULE,
        topic="The moods of the categorical syllogism",
        title="What is a mood?",
        slug="syl-what-is-a-mood",
        minutes=18,
        summary="The mood of a categorical syllogism is the three letters (A, E, I, O) of its major premise, minor premise and conclusion, such as AAA; there are 64 moods and, with four figures, 256 forms.",
        objectives=[
            "Define the mood of a categorical syllogism and read it off an argument",
            "Write the mood in the correct order: major premise, minor premise, conclusion",
            "Explain why there are 64 moods in each figure and 256 forms in all",
            "Name a form with its mood and figure, such as AAA-1",
        ],
        key_concepts=["Mood", "Figure", "Form", "Major premise", "Minor premise", "A, E, I, O", "64 moods", "256 forms"],
        blocks=[
            H("Introduction"),
            T("A tailor in Bafoussam can sew a hundred different shirts, but each one starts from a **pattern**. "
              "If the pattern is good, every shirt cut from it fits. Arguments work in the same way. "
              "Many different arguments share one pattern, and the pattern decides whether the argument is valid."),
            T("In the categorical syllogism, one part of the pattern is the **mood**. In the earlier lessons you met the structure "
              "of the syllogism (three terms, two premises, a conclusion) and its four **figures** (the four possible positions of the middle term). "
              "This lesson adds the second part of the pattern, the mood."),
            D("A **categorical proposition** has one of four standard forms: **A** (All S are P), **E** (No S are P), "
              "**I** (Some S are P) and **O** (Some S are not P). "
              "The **mood** of a categorical syllogism is the three letters, taken in order, of the **major premise**, "
              "the **minor premise** and the **conclusion**.",
              title="Definition: mood"),
            KEY("The four letters", "Each sentence in a syllogism is one of these four.", cards=[
                ["A: universal affirmative", "All S are P."],
                ["E: universal negative", "No S are P."],
                ["I: particular affirmative", "Some S are P."],
                ["O: particular negative", "Some S are not P."],
            ]),
            T("Remember the order. The **major premise** is the premise that contains the **major term** (the predicate of the conclusion). "
              "The **minor premise** contains the **minor term** (the subject of the conclusion). "
              "In standard form the major premise is written first. So the mood is always read: major premise, minor premise, conclusion."),
            EX("Worked example 1: finding the mood", intro=(
                "Find the mood: All taxi drivers in Douala must carry a licence. "
                "All the drivers at the Bonaberi park are taxi drivers in Douala. "
                "So all the drivers at the Bonaberi park must carry a licence."), steps=[
                S("Find the conclusion", text="It is the sentence after \"So\": All the drivers at the Bonaberi park must carry a licence. Subject: drivers at the Bonaberi park (the minor term). Predicate: people who must carry a licence (the major term)."),
                S("Find the major premise", text="It contains the predicate of the conclusion: \"All taxi drivers in Douala must carry a licence.\" Starts with All: letter A."),
                S("Find the minor premise", text="It contains the subject of the conclusion: \"All the drivers at the Bonaberi park are taxi drivers in Douala.\" Letter A."),
                S("Read the conclusion", text="\"All ... must carry a licence\" is a universal affirmative: letter A."),
                S("Write the mood", text="Major, minor, conclusion: **AAA**."),
            ]),
            EX("Worked example 2: a mood with E, I and O", intro=(
                "Find the mood: No lions are plant eaters. Some animals in the park are lions. "
                "So some animals in the park are not plant eaters."), steps=[
                S("Conclusion", text="\"Some animals in the park are not plant eaters.\" Subject: animals in the park (minor term). Predicate: plant eaters (major term). It is a particular negative: O."),
                S("Major premise", text="It has \"plant eaters\": \"No lions are plant eaters.\" A universal negative: E."),
                S("Minor premise", text="It has \"animals in the park\": \"Some animals in the park are lions.\" A particular affirmative: I."),
                S("Write the mood", text="Major, minor, conclusion: **EIO**."),
            ]),
            H("How many moods are there?"),
            T("Each of the three sentences can be A, E, I or O. That gives four choices for the major premise, four for the minor premise "
              "and four for the conclusion."),
            CODE("""Major premise   4 choices (A, E, I, O)
Minor premise   4 choices
Conclusion      4 choices

4 x 4 x 4 = 64 moods
64 moods x 4 figures = 256 forms""", "text", title="Counting the moods and the forms"),
            D("A syllogism's **form** is its mood together with its **figure**. We write the figure number after the mood: **AAA-1** means mood AAA in the first figure. "
              "Since each of the 64 moods can be set in any of the 4 figures, there are 64 x 4 = **256 forms** in all.",
              title="Definition: form"),
            T("The two examples above are AAA-1 and EIO-1. The mood tells you the letters. The figure tells you where the middle term stands. "
              "You need both to say whether an argument is valid."),
            KEY("Most of the 256 forms are not valid", "Validity depends on the form, not on the topic. Only a small number of the 256 forms are valid: "
                "24 in the traditional (Aristotelian) view, and 15 without any doubt in the modern (Boolean) view. "
                "The next lesson lists them with their Latin names. Textbooks differ a little here: follow your teacher's textbook."),
            TIP("Exam link: Paper 1 (multiple choice) often asks you to read off the mood of a syllogism or to say how many moods or forms there are. "
                "Paper 2 may ask you to write an argument in standard form and state its mood and figure."),
            MISTAKE("Reading the letters in the wrong order", "Do not write the conclusion's letter first, and do not take the premises in the order they appear in the "
                    "paragraph. Always find the major premise (it has the major term, the predicate of the conclusion) and put it first."),
            MISTAKE("Mixing up mood and figure", "The mood is made of the letters A, E, I, O. The figure is a number from 1 to 4. "
                     "\"AAA\" is a mood. \"First figure\" is a figure. \"AAA-1\" is a form."),
            QUIZ("A syllogism has a universal negative major premise, a universal affirmative minor premise and a universal negative conclusion. Its mood is:",
                 ["AEE", "EAE", "EEA", "AAE"], 1,
                 "Major premise E (universal negative), minor premise A (universal affirmative), conclusion E: EAE.",
                 hint="Take the sentences in the order major, minor, conclusion.",
                 feedback=["That puts A first, but the major premise is the universal negative: E.", "",
                           "That puts the conclusion's letter in the wrong place and treats the minor premise as negative.",
                           "Here the major premise is written as affirmative and the conclusion's letter is wrong."]),
            QUIZ("How many different moods can be made from the letters A, E, I, O?",
                 ["12", "16", "64", "256"], 2,
                 "Four choices for each of three sentences: 4 x 4 x 4 = 64. The number 256 counts forms (moods times four figures).",
                 hint="Count the choices for each sentence, then multiply.",
                 feedback=["12 is 4 x 3: it adds up the sentences instead of multiplying the choices.",
                           "16 is only 4 x 4: it counts the two premises and forgets the conclusion.", "",
                           "256 is the number of forms (64 moods in each of 4 figures), not the number of moods."]),
            PQ("State the mood of: Every student of the school is a member of the library. Some prefects are students of the school. So some prefects are members of the library.",
               "Major premise (contains \"members of the library\"): Every student ... is a member: A. Minor premise: Some prefects are students: I. Conclusion: Some prefects are members: I. Mood: AII."),
            PQ("How many forms have a particular negative (O) conclusion?",
               "The conclusion is fixed as O, so 1 choice. The premises have 4 x 4 = 16 choices. That makes 16 moods with an O conclusion. With four figures: 16 x 4 = 64 forms."),
            PQ("A student says \"AAA-3 and AAA-1 are the same form because they have the same mood.\" Is the student right?",
               "No. The mood is the same (AAA) but the figure is different, so they are different forms. As you will see, AAA-1 is valid, while AAA-3 is not."),
            SUM("The mood of a syllogism is the three letters (A, E, I, O) of the major premise, minor premise and conclusion, in that order.",
                "There are 4 x 4 x 4 = 64 moods, and with 4 figures there are 64 x 4 = 256 forms.",
                "A form is a mood plus a figure, written like AAA-1.",
                "Most of the 256 forms are invalid. The valid ones are listed in the next lesson."),
        ],
    ),
    lesson(
        module=MODULE,
        topic="The moods of the categorical syllogism",
        title="The valid moods and their Latin names",
        slug="syl-valid-moods-and-their-names",
        minutes=22,
        summary="Of the 256 forms, 24 are valid in the traditional view (15 without any extra assumption, 9 which need one class to have members); each has a Latin name such as Barbara, Celarent, Darii or Ferio.",
        objectives=[
            "List the valid moods in each of the four figures",
            "Give the traditional Latin name of the main valid forms (Barbara, Celarent, Darii, Ferio and others)",
            "Say which valid forms need the assumption that a class has members",
            "Explain that a mood can be valid in one figure and invalid in another",
        ],
        key_concepts=["Valid form", "Barbara", "Celarent", "Darii", "Ferio", "Unconditionally valid", "Conditionally valid", "Existential assumption"],
        blocks=[
            H("Introduction"),
            T("Out of 256 possible forms, how many always give a true conclusion from true premises? "
              "We can find out by testing every form. Here the testing was done by computer: for each form, every possible way of filling the "
              "eight regions of a three-circle Venn diagram was tried. A form is **valid** if no filling makes the premises true and the conclusion false."),
            T("The answer depends on the view you take of universal statements. This course teaches both views, so we give both counts. "
              "Textbooks differ: if your teacher's book differs, follow your teacher's book."),
            KEY("Two views, two counts", "The two views of the categorical proposition give different answers.", cards=[
                ["Traditional (Aristotelian) view", "Universal statements imply particular ones (A implies I, E implies O), because every class is assumed to have members. Valid forms: 24."],
                ["Modern (Boolean) view", "A universal statement makes no claim that its class has members. Valid forms: 15. The other 9 need one extra assumption."],
            ]),
            D("A **valid form** is a form in which the conclusion must be true whenever the premises are true. "
              "A form valid in the Boolean view is **unconditionally valid**. "
              "A form that is valid only if one of the classes has members is **conditionally valid**. "
              "The assumption that a class has members is called the **existential assumption** (existential import).",
              title="Definition: valid and conditionally valid forms"),
            H("The 24 valid forms"),
            T("Each valid form has a traditional Latin name. The three vowels of the name are the mood: in Barbara they are a, a, a (AAA). "
              "The names were made up in the Middle Ages to help students remember the forms. "
              "Here are all 24, grouped by figure. The 15 unconditional forms come first in each line."),
            CODE("""FIGURE 1  (M-P, S-M)
  Barbara  AAA    Celarent  EAE    Darii  AII    Ferio  EIO
  weakened: Barbari AAI   Celaront EAO

FIGURE 2  (P-M, S-M)
  Cesare  EAE     Camestres  AEE   Festino  EIO   Baroco  AOO
  weakened: Cesaro EAO    Camestrop AEO

FIGURE 3  (M-P, M-S)
  Datisi  AII     Disamis  IAI     Ferison  EIO   Bocardo  OAO
  weakened: Darapti AAI   Felapton EAO

FIGURE 4  (P-M, M-S)
  Camenes  AEE    Dimaris  IAI     Fresison  EIO
  weakened: Bramantip AAI   Fesapo EAO   Camenop AEO""", "text", title="The 24 traditionally valid forms"),
            T("Count them. Figure 1: 4 + 2 = 6. Figure 2: 4 + 2 = 6. Figure 3: 4 + 2 = 6. Figure 4: 3 + 3 = 6. That makes 24 forms in the traditional view. "
              "The unconditional ones are 4 + 4 + 4 + 3 = 15."),
            TIP("Check your textbook for the exact spelling of the less common names. The names Barbara, Celarent, Darii, Ferio, Cesare, Camestres, Festino, Baroco, "
                "Datisi, Disamis, Ferison, Bocardo, Darapti and Felapton are standard. For Figure 4 and for the \"weakened\" forms (Barbari, Celaront, Cesaro, Camestrop, Camenop) "
                "books differ in spelling, and some leave the weakened forms out. Follow your teacher's list."),
            H("Which forms need an assumption?"),
            T("The 9 \"weakened\" forms draw a **particular** conclusion from **universal** premises. "
              "That is only safe if some member of a certain class really exists. "
              "Here is each one, with the class that must have members."),
            CODE("""Form            Mood   Class that must have members
Barbari   (1)   AAI    S  (the minor term)
Celaront  (1)   EAO    S
Cesaro    (2)   EAO    S
Camestrop (2)   AEO    S
Camenop   (4)   AEO    S
Darapti   (3)   AAI    M  (the middle term)
Felapton  (3)   EAO    M
Fesapo    (4)   EAO    M
Bramantip (4)   AAI    P  (the major term)""", "text", title="The 9 conditionally valid forms"),
            T("Example. Darapti says: All M are P; all M are S; so some S are P. "
              "If nothing is in M, the premises are true but empty, and the conclusion can fail. "
              "If M has members, the conclusion follows. That is why Darapti needs M to have members."),
            KEY("A mood alone does not decide validity", "AAA is valid only in Figure 1 (Barbara). In Figures 2, 3 and 4 the mood AAA is invalid. "
                "EIO is valid in all four figures (Ferio, Festino, Ferison, Fresison). So you must always check mood and figure together."),
            EX("Worked example 1: naming a form", intro=(
                "No lions are goats. All animals in the farm are goats. Therefore no animals in the farm are lions. Name the form."), steps=[
                S("Find the major term and the minor term", text="Conclusion: No animals in the farm (minor term) are lions (major term). So the middle term is goats."),
                S("Major premise", text="It has lions: \"No lions are goats.\" Letter E. Lions is the subject, goats the predicate: the major premise is P-M."),
                S("Minor premise", text="\"All animals in the farm are goats.\" Letter A. S-M."),
                S("Mood and figure", text="Mood EAE. The pattern P-M, S-M is Figure 2. So the form is EAE-2."),
                S("Look up the name", text="EAE-2 is **Cesare**: valid, and unconditional."),
            ]),
            EX("Worked example 2: writing an argument from a name", intro=(
                "Write an argument in the form Camestres (AEE-2) and say whether the premises need an existential assumption."), steps=[
                S("Mood and figure", text="Camestres is AEE in Figure 2: All P are M. No S are M. So no S are P."),
                S("Choose terms", text="P = lions, M = carnivores, S = goats."),
                S("Write the argument", text="All lions are carnivores. No goats are carnivores. Therefore no goats are lions."),
                S("Check", text="AEE-2 is on the list as unconditionally valid (in the Boolean view too). No assumption is needed."),
            ]),
            EX("Worked example 3: a conditionally valid form", intro=(
                "Is this valid? All students who scored full marks are students who passed. All students who scored full marks "
                "sat the test. So some students who sat the test passed."), steps=[
                S("Find the form", text="Middle term: students who scored full marks (M). Both premises have M as subject, so the figure is 3. Mood: A, A, I. The form is AAI-3: Darapti."),
                S("Check the list", text="Darapti is conditionally valid: it needs M to have members."),
                S("Apply it", text="If at least one student scored full marks, the argument is valid. If the test was so hard that nobody did, "
                                   "the two universal premises are true but empty, and the conclusion does not follow."),
                S("Say which view you use", text="In the traditional view (classes have members) it is valid. In the Boolean view it is invalid unless you add \"some students scored full marks\"."),
            ]),
            TIP("Exam link: Paper 1 may give a syllogism and ask for its name or for the number of valid forms; Paper 2 may ask you to show on a table which forms are valid and why. "
                "Learn the four names of Figure 1 (Barbara, Celarent, Darii, Ferio) first."),
            MISTAKE("Saying a mood is valid without the figure", "Never say \"AAA is valid\". Say \"AAA-1 (Barbara) is valid\". The same mood can be invalid in another figure."),
            MISTAKE("Forgetting the extra assumption", "If a form draws a particular conclusion from two universal premises, ask: is it valid only because we assume some members exist? "
                    "If so, say \"conditionally valid\" and state which class must have members."),
            QUIZ("How many valid forms are there in the Boolean view, without any extra assumption?",
                 ["9", "15", "24", "256"], 1,
                 "Of the 24 traditionally valid forms, 9 need an existential assumption. 24 - 9 = 15 are unconditionally valid.",
                 hint="Start from the 24 forms of the traditional view and remove the conditional ones.",
                 feedback=["9 is the number of conditionally valid forms.", "",
                           "24 is the traditional count, which includes the 9 conditional forms.",
                           "256 is the number of all forms, valid and invalid."]),
            QUIZ("Which of these is a form that is valid in the first figure?",
                 ["Barbara (AAA)", "Bocardo (OAO)", "Festino (EIO)", "Datisi (AII)"], 0,
                 "Barbara is in Figure 1. Bocardo and Datisi are in Figure 3, and Festino is in Figure 2.",
                 hint="The first four names, Barbara, Celarent, Darii, Ferio, belong to Figure 1.",
                 feedback=["", "Bocardo is a Figure 3 form.", "Festino is a Figure 2 form.", "Datisi is a Figure 3 form."]),
            PQ("Name the form: All birds are animals with feathers. No fish are animals with feathers. Therefore no fish are birds.",
               "The conclusion is \"No fish are birds\": minor term fish, major term birds, so the middle term is animals with feathers. Major premise (with birds): All birds are animals with feathers (A, P-M). Minor premise: No fish are animals with feathers (E, S-M). Figure 2. Mood AEE: Camestres. Valid and unconditional."),
            PQ("Which forms in Figure 1 need S to have members? Give their names and moods.",
               "Barbari (AAI) and Celaront (EAO). Both draw a particular conclusion from two universal premises in Figure 1."),
            PQ("Explain why Darapti is valid in the traditional view but not in the Boolean view.",
               "Darapti: All M are P; all M are S; so some S are P. The premises, in the Boolean view, do not say that M has members, so M may be empty and then there may be no S that are P. In the traditional view, every class has members, so there is a member of M that is both S and P. Hence it is valid only with the existential assumption."),
            SUM("Of the 256 forms, 24 are valid in the traditional view; 15 of them are unconditionally valid, and 9 need one class to have members.",
                "Each valid form has a Latin name whose three vowels give the mood: Barbara is AAA, Celarent EAE, Darii AII, Ferio EIO.",
                "The 24 are shared 6 per figure. The 9 conditional ones are Barbari, Celaront, Cesaro, Camestrop, Camenop, Darapti, Felapton, Fesapo and Bramantip.",
                "A mood is valid or invalid only with its figure: AAA is valid in Figure 1 only.",
                "Textbooks differ on names and on whether they teach the weakened forms: follow your teacher's list."),
        ],
    ),
    # ------------------------------------------------------------------ Venn diagrams of syllogisms
    lesson(
        module=MODULE,
        topic="Representing categorical syllogisms on the Venn diagram",
        title="The three-circle Venn diagram",
        slug="syl-three-circle-venn-diagrams",
        minutes=20,
        summary="Draw three overlapping circles for S, P and M, name the eight regions, and show each of the four standard propositions by shading (empty) or by an X (has a member).",
        objectives=[
            "Draw three overlapping circles for the minor, major and middle terms",
            "Name the eight regions exactly, including the region outside all three circles",
            "Shade the regions for an A or an E proposition",
            "Place an X for an I or an O proposition, and know when the X goes on a line",
        ],
        key_concepts=["Venn diagram", "Three circles", "Region", "Shading", "X (existence mark)", "Universal premise first"],
        blocks=[
            H("Introduction"),
            T("In Form 5 there is a choir, a football team and a group of prefects. Some students belong to only one group, some to two, some to all three, "
              "and some to none. A picture with three overlapping circles shows all these cases at once. "
              "That is a **Venn diagram**, named after the English logician John Venn."),
            T("In a syllogism there are exactly three terms, so three circles are enough: one for the minor term S, one for the major term P and one for the middle term M. "
              "In the next lesson you will use the diagram to test validity. This lesson teaches you to draw it and to put one premise on it."),
            D("A **Venn diagram for a syllogism** has three overlapping circles labelled **S** (minor term), **P** (major term) and **M** (middle term). "
              "Every part of the picture is a **region**: a possible kind of thing. The three circles make **eight regions**, including the area outside all three.",
              title="Definition: the three-circle diagram"),
            IMG("f5l-syl-three-circles.svg",
                alt="Three overlapping circles labelled S, P and M. The seven regions inside the circles are numbered 1 to 7, and 8 is outside all three.",
                caption="Figure 1. Three circles S, P and M with the regions numbered 1 to 7. Region 8 is outside all three circles."),
            CODE("""Region  Is in S?  Is in P?  Is in M?
  1       yes       no        no      (S only)
  2       no        yes       no      (P only)
  3       no        no        yes     (M only)
  4       yes       yes       no      (S and P, not M)
  5       yes       no        yes     (S and M, not P)
  6       no        yes       yes     (P and M, not S)
  7       yes       yes       yes     (all three)
  8       no        no        no      (outside all three)""", "text", title="The eight regions (numbers as in Figure 1)"),
            T("Check the count: each region is a yes or no for S, a yes or no for P and a yes or no for M. That is 2 x 2 x 2 = 8 regions. "
              "The eighth one (no, no, no) is the space around the circles. It is not needed for testing syllogisms, but it is there."),
            H("Putting a proposition on the diagram"),
            T("Every standard proposition is about two of the three circles. It tells us that some regions are **empty** or that some region has a **member**. "
              "We use two marks. **Shading** means \"nothing is in this region\". An **X** means \"at least one thing is in this region\"."),
            KEY("The four propositions as marks", "Take two circles, X and Y.", cards=[
                ["A: All X are Y", "Shade every part of X that is outside Y. (Nothing is X without being Y.)"],
                ["E: No X are Y", "Shade every part where X and Y overlap."],
                ["I: Some X are Y", "Put an X in the overlap of X and Y."],
                ["O: Some X are not Y", "Put an X in the part of X that is outside Y."],
            ]),
            T("With three circles, each of these parts is made of **two regions**, because the third circle cuts it in two. "
              "For example, the part of S outside P is region 1 (outside M too) and region 5 (inside M)."),
            CODE("""Part                 Regions
S outside P          1 and 5
S and P (overlap)    4 and 7
S outside M          1 and 4
S and M (overlap)    5 and 7
M outside P          3 and 5
M and P (overlap)    6 and 7
P outside M          2 and 4
M outside S          3 and 6
P outside S          2 and 6""", "text", title="Which two regions make each part"),
            KEY("Two rules for marking", "(1) Always draw the **universal** premises (A and E) first. Shading cannot be wrong, and it shows which regions an X may use. "
                "(2) An X goes in a region only if the other region of its pair is shaded. If both regions are open, the X goes **on the line** between them, "
                "meaning \"in one or the other, we do not know which\"."),
            EX("Worked example 1: an A proposition", intro="Draw the premise All M are P on the three circles.", steps=[
                S("Find the part", text="A: All X are Y means shade the part of X outside Y. Here X is M and Y is P: the part of M outside P."),
                S("Name the regions", text="From the table: M outside P is regions 3 and 5."),
                S("Shade", text="Shade regions 3 and 5. They are empty. Figure 2 shows the result."),
            ]),
            IMG("f5l-syl-all-m-are-p.svg",
                alt="Three overlapping circles S, P and M. The part of M outside P, regions 3 and 5, is shaded with green stripes.",
                caption="Figure 2. All M are P: the parts of M outside P are shaded."),
            EX("Worked example 2: an E proposition", intro="Draw the premise No S are M.", steps=[
                S("Find the part", text="E: No X are Y means shade the overlap of X and Y. Here: the overlap of S and M."),
                S("Name the regions", text="S and M overlap in regions 5 and 7."),
                S("Shade", text="Shade regions 5 and 7. Nothing is both S and M."),
            ]),
            EX("Worked example 3: two premises together", intro="Draw the two premises No M are P and Some S are M.", steps=[
                S("Universal premise first", text="No M are P: shade the overlap of M and P, regions 6 and 7."),
                S("Particular premise: find its two regions", text="Some S are M means an X in the overlap of S and M: regions 5 and 7."),
                S("Check the shading", text="Region 7 is shaded (empty), so the X cannot be there. Only region 5 is open."),
                S("Place the X", text="Put the X inside region 5: S and M, but not P. Reading it: there is something that is S and M and not P."),
            ]),
            TIP("Exam link: Paper 1 may show a Venn diagram and ask which proposition it represents, or which regions an X may occupy. "
                "Paper 2 asks you to draw the diagram for a given syllogism. Use a ruler or a coin for neat circles."),
            MISTAKE("Shading where you should put an X", "Shading means empty. An X means there is something. Do not shade for I or O propositions, and do not put an X for A or E propositions."),
            MISTAKE("Shading only one region", "On a three-circle diagram a universal premise nearly always empties **two** regions (the third circle splits the part in two). "
                    "Check the table before you shade."),
            QUIZ("To draw the proposition No P are M on the three circles you shade:",
                 ["regions 2 and 4", "regions 6 and 7", "regions 3 and 5", "regions 4 and 7"], 1,
                 "No P are M: the overlap of P and M is regions 6 and 7.",
                 hint="E means shade the overlap of the two circles named.",
                 feedback=["Regions 2 and 4 are the part of P outside M: that would be All P are M.", "",
                           "Regions 3 and 5 are the part of M outside P: that would be All M are P.",
                           "Regions 4 and 7 are the overlap of S and P, not of P and M."]),
            QUIZ("After shading regions 6 and 7 (No M are P), where may the X for Some S are M go?",
                 ["Region 7, inside all three circles", "Region 5, in S and M but outside P", "On the line between regions 6 and 7", "Region 4"], 1,
                 "S and M overlap in regions 5 and 7. Region 7 is shaded (empty), so the X goes in region 5.",
                 hint="Which two regions make the overlap of S and M? Is either of them already shaded?",
                 feedback=["Region 7 is shaded: nothing can be there.", "",
                           "The line between 6 and 7 belongs to the overlap of M and P, not S and M.",
                           "Region 4 is S and P outside M; it is not in M."]),
            PQ("Which regions do you shade for All P are M?",
               "A means shade the part of P outside M. From the table: regions 2 and 4."),
            PQ("Which two regions may hold the X for Some S are not P, and where does the X go if region 5 is shaded?",
               "Some S are not P: the part of S outside P is regions 1 and 5. If region 5 is shaded, the X goes in region 1."),
            PQ("A student draws All S are M by shading regions 5 and 7. What is the mistake?",
               "Regions 5 and 7 are the overlap of S and M. That is the picture of No S are M. For All S are M, shade the part of S outside M: regions 1 and 4."),
            SUM("A three-circle Venn diagram has circles S, P and M. They make eight regions, seven inside the circles and one outside.",
                "Shading means a region is empty. An X means there is at least one member.",
                "A: shade X outside Y. E: shade the overlap of X and Y. I: X in the overlap. O: X in the part of X outside Y.",
                "Draw universal premises first. Put an X in a region only when the other region of its pair is shaded; otherwise put it on the line."),
        ],
    ),
    lesson(
        module=MODULE,
        topic="Representing categorical syllogisms on the Venn diagram",
        title="Testing validity with Venn diagrams",
        slug="syl-testing-validity-with-venn-diagrams",
        minutes=24,
        summary="Draw the two premises on a three-circle diagram (universal first), then see whether the conclusion is already shown; the Boolean view needs no extra assumption, and the forms that need existential import show up as an X that is missing.",
        objectives=[
            "Test a syllogism by drawing only its premises on the Venn diagram",
            "Decide if the conclusion is already shown, without adding anything",
            "Deal with an X that falls on a line",
            "Explain, with a diagram, why some valid forms need the existential assumption",
        ],
        key_concepts=["Testing validity", "Premises only", "X on a line", "Boolean view", "Existential import", "Darapti"],
        blocks=[
            H("Introduction"),
            T("Is an argument valid? The rules in the next lessons give one answer. The Venn diagram gives another: it lets you **see** whether the conclusion is "
              "already contained in the premises. In an exam, many students find the diagram safer than the rules, because it is mechanical."),
            T("This lesson uses the **Boolean (modern) view**: a universal premise does not say that its class has any members. "
              "So only X marks you place by a particular premise create members. At the end we show what changes in the traditional view. "
              "Textbooks differ on this: follow your teacher's textbook."),
            KEY("The procedure", "Four steps.", cards=[
                ["Step 1", "Draw three circles S, P, M and check that the terms are the minor term, the major term and the middle term."],
                ["Step 2", "Draw the universal premise(s) first, by shading. Then draw the particular premise, by an X in an open region (or on a line)."],
                ["Step 3", "Do not draw the conclusion. Look at the diagram and ask: is the conclusion already shown?"],
                ["Step 4", "If yes, the form is valid. If not, it is invalid."],
            ]),
            D("**Reading a universal conclusion**: All S are P is shown if both regions of S outside P (regions 1 and 5) are shaded. No S are P is shown if both regions of the overlap of S and P (regions 4 and 7) are shaded. "
              "**Reading a particular conclusion**: Some S are P is shown if there is an X in S and P (region 4, or 7, or on the line between them). Some S are not P is shown if there is an X in S outside P (region 1, or 5, or on the line between them).",
              title="How to read the conclusion"),
            T("A word on the line. An X on the line between two regions means \"in one or the other\". It still shows the conclusion if **both** regions are inside the conclusion's part. "
              "For example an X on the line between regions 4 and 7 shows Some S are P, because both 4 and 7 are in S and P. "
              "But an X on the line between regions 6 and 7 does not show it: region 6 is outside S."),
            EX("Worked example 1: a valid form (Barbara, AAA-1)", intro=(
                "All taxi drivers are licensed people. All the drivers at the Mile 4 park are taxi drivers. Therefore all the drivers at the Mile 4 park are licensed people."), steps=[
                S("Terms", text="S = drivers at the Mile 4 park, P = licensed people, M = taxi drivers."),
                S("First premise: All M are P", text="Shade the part of M outside P: regions 3 and 5."),
                S("Second premise: All S are M", text="Shade the part of S outside M: regions 1 and 4."),
                S("Read the conclusion", text="All S are P needs regions 1 and 5 shaded. Both are shaded. The conclusion is already shown: **valid**."),
            ]),
            IMG("f5l-syl-barbara.svg",
                alt="Three overlapping circles S, P and M. All of S outside P, and the whole of M outside P, is shaded. The overlap of P and M and the part of P alone are open.",
                caption="Figure 3. Barbara: after shading the two premises, regions 1 and 5 (S outside P) are both empty."),
            EX("Worked example 2: a valid form with an X (Darii, AII-1)", intro=(
                "All people who pay school fees on time are parents who care. Some people in this village pay school fees on time. "
                "Therefore some people in this village are parents who care."), steps=[
                S("Terms", text="S = people in this village, P = parents who care, M = people who pay on time."),
                S("Universal premise first: All M are P", text="Shade regions 3 and 5."),
                S("Particular premise: Some S are M", text="The overlap of S and M is regions 5 and 7. Region 5 is shaded, so the X goes in region 7."),
                S("Read the conclusion", text="Region 7 is inside S and P. The X shows Some S are P. **Valid**."),
            ]),
            IMG("f5l-syl-darii.svg",
                alt="Three overlapping circles. The part of M outside P is shaded. An X stands in the middle region where S, P and M all overlap.",
                caption="Figure 4. Darii: the X is forced into region 7, which lies in S and P."),
            EX("Worked example 3: an invalid form (undistributed middle, AAA-2)", intro=(
                "All mangoes are fruits. All pawpaws are fruits. Therefore all pawpaws are mangoes."), steps=[
                S("Terms", text="S = pawpaws, P = mangoes, M = fruits."),
                S("Premise 1: All P are M", text="Shade the part of P outside M: regions 2 and 4."),
                S("Premise 2: All S are M", text="Shade the part of S outside M: regions 1 and 4."),
                S("Read the conclusion", text="All S are P needs regions 1 and 5 shaded. Region 1 is shaded, but **region 5 is open** (S and M, not P). "
                                              "There is room for a fruit that is a pawpaw and not a mango. The conclusion is not shown: **invalid**."),
            ]),
            IMG("f5l-syl-undistributed.svg",
                alt="Three overlapping circles S, P and M. The parts of S and of P outside M are shaded. The part of S and M outside P is highlighted in yellow and is still open.",
                caption="Figure 5. All P are M and all S are M: the yellow region 5 is open, so All S are P is not shown."),
            EX("Worked example 4: an X on a line (III-1)", intro=(
                "Some members of the club are footballers. Some students are members of the club. Therefore some students are footballers."), steps=[
                S("Terms", text="S = students, P = footballers, M = members of the club. Some M are P; some S are M."),
                S("No universal premise", text="Nothing can be shaded, so no region is ruled out."),
                S("Some M are P", text="The overlap of M and P is regions 6 and 7. Both are open, so the X goes on the line between them."),
                S("Some S are M", text="The overlap of S and M is regions 5 and 7. Both are open, so this X also goes on a line."),
                S("Read the conclusion", text="Some S are P needs an X in region 4 or 7 or between them. The first X may be in region 6 (outside S). The second may be in region 5 (outside P). "
                                              "So no X is forced into S and P: **invalid**."),
            ]),
            IMG("f5l-syl-two-particular.svg",
                alt="Three overlapping circles with nothing shaded and two X marks, each sitting on a circle line inside the overlap area.",
                caption="Figure 6. Two particular premises: each X sits on a line, so neither is forced into both S and P."),
            H("The Boolean view and existential import"),
            T("Some valid forms from the traditional list fail the Venn test. The reason is the **existential import** of the universal premises: "
              "the traditional view assumes that a class named in a universal premise has members. The Boolean view does not."),
            EX("Worked example 5: Darapti (AAI-3)", intro=(
                "All students who scored full marks are students who passed. All students who scored full marks sat the test. "
                "Therefore some students who sat the test passed."), steps=[
                S("Terms", text="M = students who scored full marks, P = students who passed, S = students who sat the test."),
                S("All M are P", text="Shade regions 3 and 5."),
                S("All M are S", text="Shade the part of M outside S: regions 3 and 6."),
                S("What remains of M", text="Only region 7 is open inside M. There is no X, because universal premises do not put anything in."),
                S("Read the conclusion", text="Some S are P needs an X in region 4 or 7. There is none. In the Boolean view the form is **invalid**."),
                S("The traditional view", text="It adds: M has members. Then the only open region of M, region 7, must hold an X. The conclusion follows: valid (conditionally)."),
            ]),
            IMG("f5l-syl-darapti.svg",
                alt="Three overlapping circles. All of M outside the middle region where all three circles overlap is shaded. A dashed blue X marks the assumption that the middle region has a member.",
                caption="Figure 7. Darapti: only region 7 is left in M. The dashed X is the extra assumption that some M exist."),
            KEY("Which forms need the extra X?", "Exactly the 9 conditionally valid forms of the previous lesson (Barbari, Celaront, Cesaro, Camestrop, Camenop, Darapti, Felapton, Fesapo, Bramantip). "
                "In each, the universal premises leave one region in a class open, and the conclusion needs an X there. The 15 unconditional forms need no extra X."),
            TIP("Exam link: In Paper 2 you may be asked to \"test the validity of the following syllogism by the Venn diagram method\". Say which view you use, draw the diagram, "
                "and write one sentence of reading, such as \"Region 5 is open, so the conclusion is not shown\". If your textbook uses the traditional view, state the existential assumption where it applies."),
            MISTAKE("Drawing the conclusion on the diagram", "Never add the conclusion to the diagram. Draw the premises only, then look. If you draw the conclusion, you will always find it there."),
            MISTAKE("Putting the X in a region that is already shaded", "A shaded region is empty. If the only region for the X is shaded, the two premises contradict each other. "
                    "In every other case, look at the other region of the pair."),
            QUIZ("After drawing the premises of a syllogism, the conclusion All S are P needs which regions to be shaded?",
                 ["Regions 2 and 4", "Regions 1 and 5", "Regions 4 and 7", "Regions 3 and 5"], 1,
                 "All S are P means the part of S outside P is empty: regions 1 and 5.",
                 hint="The part of S outside P.",
                 feedback=["Regions 2 and 4 are the part of P outside M.", "",
                           "Regions 4 and 7 are the overlap of S and P: shading them says No S are P.",
                           "Regions 3 and 5 are the part of M outside P."]),
            QUIZ("In the Boolean view, a syllogism with two universal premises and a particular conclusion is:",
                 ["always valid", "never valid", "invalid, because no premise puts an X anywhere", "valid only in the first figure"], 2,
                 "Universal premises only shade. They never place an X. So a particular conclusion cannot be shown. (The traditional view adds the assumption that the class has members.)",
                 hint="What do universal premises do on the diagram: shade or place an X?",
                 feedback=["That is the traditional view, which assumes the classes have members.",
                           "Not \"never\": the traditional view finds 9 such valid forms with the extra assumption.", "",
                           "Figure 1 does not escape this: Barbari (AAI-1) is only conditionally valid."]),
            PQ("Test by Venn diagram: No M are P. All S are M. Therefore no S are P (EAE-1).",
               "No M are P: shade regions 6 and 7. All S are M: shade regions 1 and 4. No S are P needs regions 4 and 7 shaded: 4 is shaded by the second premise and 7 by the first. Both are shaded, so the conclusion is shown. Valid (Celarent)."),
            PQ("Test: All P are M. Some S are M. Therefore some S are P (AII-2).",
               "All P are M: shade regions 2 and 4. Some S are M: regions 5 and 7 are both open, so the X goes on the line between them. Some S are P needs an X in 4 or 7. The X may be in region 5 (outside P). So the conclusion is not shown. Invalid (undistributed middle)."),
            PQ("Why does the Venn test treat Darapti as invalid in the Boolean view?",
               "After shading the two universal premises, region 7 is the only open region in M, but no X has been placed there. The conclusion Some S are P needs an X in region 4 or 7. Universal premises place no X. In the traditional view the assumption that M has members puts the X in region 7."),
            SUM("To test a syllogism, draw its two premises on three circles, universal premise first. Do not draw the conclusion.",
                "Then read the diagram: the conclusion must already be there. For All or No, the right regions are shaded. For Some, an X lies in the right part.",
                "An X on a line means \"one region or the other\". It shows a particular conclusion only if both regions are inside it.",
                "In the Boolean view universal premises place no X, so the 9 forms with a particular conclusion from universal premises need an extra assumption that a class has members.",
                "Textbooks differ: follow your teacher's view, and say which view you are using."),
        ],
    ),
    # ------------------------------------------------------------------ Translating into standard form
    lesson(
        module=MODULE,
        topic="Translating categorical arguments into standard forms",
        title="Putting arguments into standard form",
        slug="syl-putting-arguments-into-standard-form",
        minutes=24,
        summary="Turn an argument from everyday language into a standard-form categorical syllogism: find the conclusion and premises, supply a missing premise, translate each sentence into A, E, I or O, and put the major premise first.",
        objectives=[
            "Find the conclusion and the premises of an everyday argument",
            "Supply a missing premise that the argument takes for granted",
            "Translate everyday sentences into A, E, I or O sentences with a subject term, a predicate term and the words are or are not",
            "Order the premises (major first) and state the mood and figure",
        ],
        key_concepts=["Standard form", "Conclusion indicator", "Missing premise", "Translation into A, E, I, O", "Major premise", "Minor premise"],
        blocks=[
            H("Introduction"),
            T("People do not speak in syllogisms. At a market in Bamenda you may hear: \"Only members of the cooperative get the cheap fertiliser. Ndi is not a member. So Ndi will not get it.\" "
              "There is an argument here, but it is not in the neat form A, E, I, O that logic can test."),
            T("To test an argument we first **put it into standard form**. This lesson gives a step-by-step method. "
              "You met the standard forms A, E, I and O in the lessons on propositions. "
              "Here we apply them to whole arguments."),
            D("A categorical syllogism is in **standard form** when (1) it has exactly three terms; (2) both premises and the conclusion are A, E, I or O sentences, each written as "
              "**quantifier + subject term + are / are not + predicate term**; (3) the **major premise** comes first, then the **minor premise**, then the **conclusion**.",
              title="Definition: standard form"),
            KEY("The method in six steps", "Follow these steps in order.", cards=[
                ["1. Conclusion", "Find it. Words such as therefore, so, hence, thus, consequently and it follows that point to the conclusion."],
                ["2. Premises", "Find the reasons. Words such as because, since, for and as point to a premise. If a premise is missing, supply it (say so)."],
                ["3. Translate", "Rewrite each sentence as A, E, I or O. Each term must be a noun or noun phrase naming a class (people who ..., things that ...)."],
                ["4. Name the terms", "Major term = predicate of the conclusion. Minor term = subject of the conclusion. Middle term = the term that appears in both premises but not in the conclusion."],
                ["5. Order", "Major premise first (it has the major term), minor premise second, conclusion last."],
                ["6. Label", "State the mood (the letters), the figure (the place of the middle term), and then test validity."],
            ]),
            H("Translating the sentences"),
            T("Most of the work is in step 3. Everyday sentences use many words for all, none, and some. Here are the common patterns."),
            CODE("""Everyday sentence                     Standard form
Every / each / any S is P             All S are P            (A)
Whoever / anyone who is S is P        All persons who are S are P   (A)
Only S are P                          All P are S            (A, reversed!)
None but S are P                      All P are S            (A, reversed!)
No S is P / Nobody who is S is P      No S are P             (E)
There are no S that are P             No S are P             (E)
Some S are P / There are S that are P Some S are P            (I)
A few S are P / Many S are P          Some S are P            (I)
Some S are not P                      Some S are not P        (O)
Not all S are P / Not every S is P    Some S are not P        (O)
S is P (S a name)                     All persons identical with S are P  (A)
S is not P (S a name)                 No persons identical with S are P   (E)""", "text", title="Common translations"),
            T("Notes. \"Not all S are P\" is the same as \"Some S are not P\": if it is not the case that every S is P, then at least one S is not P. "
              "A name such as Ngu is treated as a class with one member: \"Ngu is a student\" becomes \"All persons identical with Ngu are students\". "
              "Some textbooks handle singular sentences in other ways, so follow your teacher's book. "
              "A sentence with a verb, like \"Dogs bark\", is rewritten with are: \"All dogs are animals that bark\"."),
            KEY("Watch the word \"only\"", "\"Only S are P\" and \"None but S are P\" are **not** \"All S are P\". "
                "\"Only members vote\" means that if someone votes, then he or she is a member: All voters are members. The subject and predicate are swapped.",
                note="Test it: \"Only adults may enter\" does not say that every adult may enter; it says that everyone who enters is an adult."),
            EX("Worked example 1: putting an argument into standard form", intro=(
                "Only registered voters may vote. Ngu is not a registered voter. So Ngu may not vote."), steps=[
                S("Step 1: the conclusion", text="\"So Ngu may not vote\" is the conclusion (the word \"so\")."),
                S("Step 3: translate the conclusion", text="No persons identical with Ngu are persons who may vote. Letter E. Minor term S = persons identical with Ngu. Major term P = persons who may vote."),
                S("Steps 2 and 3: translate the premises", text="\"Only registered voters may vote\" becomes All persons who may vote are registered voters (A, reversed). "
                                                              "\"Ngu is not a registered voter\" becomes No persons identical with Ngu are registered voters (E)."),
                S("Step 4: the middle term", text="Registered voters appears in both premises and not in the conclusion: it is the middle term M."),
                S("Step 5: order", text="Major premise (has P): All P are M. Minor premise (has S): No S are M. Conclusion: No S are P."),
                S("Step 6: label", text="The middle term is the predicate of both premises: Figure 2. The mood is AEE. The form is AEE-2, Camestres, which is valid."),
            ]),
            EX("Worked example 2: supplying a missing premise", intro=(
                "Every taxi driver must hold a licence, so Mbarga must hold a licence."), steps=[
                S("Find the conclusion", text="\"Mbarga must hold a licence\": All persons identical with Mbarga are persons who must hold a licence (A)."),
                S("Find the stated premise", text="\"Every taxi driver must hold a licence\": All taxi drivers are persons who must hold a licence (A). It has the predicate of the conclusion, so it is the major premise."),
                S("What is missing?", text="The minor premise: Mbarga is a taxi driver. The speaker takes it for granted. We write it out: All persons identical with Mbarga are taxi drivers."),
                S("Write the syllogism", text="All taxi drivers are persons who must hold a licence. All persons identical with Mbarga are taxi drivers. Therefore all persons identical with Mbarga are persons who must hold a licence."),
                S("Label", text="AAA-1: Barbara, valid. But the argument is good only if the supplied premise is true: check that Mbarga really is a taxi driver."),
            ]),
            EX("Worked example 3: premises in the wrong order", intro=(
                "Some players in the school team are prefects. So some players in the school team are students of the upper school, because all prefects are students of the upper school."), steps=[
                S("Conclusion and premises", text="Conclusion (after \"So\"): Some players are students of the upper school (I). Premises: \"Some players are prefects\" (I) and, after \"because\", \"All prefects are students of the upper school\" (A)."),
                S("Terms", text="Minor term S = players in the school team. Major term P = students of the upper school. Middle term M = prefects."),
                S("Order", text="The premise with P comes first: All M are P (All prefects are students of the upper school). Then the minor premise: Some S are M (Some players are prefects)."),
                S("Label", text="Mood AII, with the middle term as subject of the major and predicate of the minor premise: Figure 1. AII-1 is Darii: valid."),
            ]),
            TIP("Exam link: Paper 2 often gives a short everyday argument and asks you to (a) put it in standard form, (b) name the major, minor and middle terms, and (c) test its validity. "
                "Marks go to a correct translation of each sentence, so write each one out clearly."),
            MISTAKE("Translating \"only\" as \"all\"", "Only S are P is All P are S. Swapping them changes the meaning. \"Only students get a discount\" is not \"All students get a discount\"."),
            MISTAKE("Using adjectives as predicates", "A term must name a class. \"Mangoes are sweet\" should become \"All mangoes are sweet fruits\" (or \"things that are sweet\"). "
                    "Do not leave a bare adjective, or you will meet four terms by accident."),
            MISTAKE("Reading \"All S are not P\" without thinking", "This sentence is ambiguous. In most textbooks it is read as No S are P, but in speech it can also mean Not all S are P. "
                    "Look at the context, and ask your teacher what the textbook does."),
            QUIZ("\"Only members of the cooperative may sell at the stall.\" In standard form this is:",
                 ["All members of the cooperative are persons who may sell at the stall.", "All persons who may sell at the stall are members of the cooperative.",
                  "Some members of the cooperative are persons who may sell at the stall.", "No non-members of the cooperative are persons who may sell at the stall, and all members may sell."], 1,
                 "\"Only S are P\" means All P are S: everyone who may sell is a member.",
                 hint="Who is it that must be a member?",
                 feedback=["That is All S are P with the terms the wrong way round: it says every member may sell.", "",
                           "That is an I sentence. It is weaker than the original.",
                           "The extra claim that every member may sell is not in the original sentence."]),
            QUIZ("\"Not every student passed the test\" is the same as:",
                 ["All students did not pass", "No students passed", "Some students did not pass", "Some students passed"], 2,
                 "Not every student passed means that at least one student did not pass: Some students are not passers (O).",
                 hint="If it is false that every student passed, what must be true of at least one student?",
                 feedback=["\"All did not pass\" is usually read as none passed, which is much stronger.",
                           "That is the universal negative, a stronger claim.", "",
                           "Some may have passed, but this sentence does not say so."]),
            PQ("Translate into A, E, I or O: (a) Every cocoa farmer in the village sells to the cooperative. (b) Nobody who cheats is honest. (c) Not all traders pay tax.",
               "(a) All cocoa farmers in the village are persons who sell to the cooperative (A). (b) No persons who cheat are honest persons (E). (c) Some traders are not persons who pay tax (O)."),
            PQ("Name the conclusion, the minor term, the major term and the middle term: \"No lions are plant eaters, and some animals in the park are lions, so some animals in the park are not plant eaters.\"",
               "Conclusion: Some animals in the park are not plant eaters. Minor term (its subject): animals in the park. Major term (its predicate): plant eaters. Middle term: lions."),
            PQ("Put the argument in standard form and give its mood and figure: \"All prefects are students. Chi is a prefect. So Chi is a student.\"",
               "Major premise: All prefects are students (A). Minor premise: All persons identical with Chi are prefects (A). Conclusion: All persons identical with Chi are students (A). The middle term (prefects) is the subject of the major premise and the predicate of the minor premise: Figure 1. Form AAA-1, Barbara: valid."),
            PQ("A speaker says: \"All the shops in this street pay tax, so Mimi's shop pays tax.\" What premise is missing, and what must you check before accepting the argument?",
               "The missing premise: Mimi's shop is one of the shops in this street. With it the argument is AAA-1 (Barbara), which is valid. Before accepting it, check that the added premise is true: is Mimi's shop really in this street?"),
            SUM("To test an everyday argument, first put it in standard form: three terms, sentences in the form A, E, I or O, major premise first.",
                "Follow six steps: find the conclusion; find or supply the premises; translate each sentence; name the three terms; order the premises; label the mood and figure.",
                "Watch the translation of only and none but (Only S are P is All P are S), not all (which is O), and names (treated as one-member classes).",
                "A supplied missing premise must be written out, and its truth checked."),
        ],
    ),
    # ------------------------------------------------------------------ General rules and fallacies
    lesson(
        module=MODULE,
        topic="The general rules of the syllogism and fallacies",
        title="The general rules of the syllogism",
        slug="syl-the-general-rules-of-the-syllogism",
        minutes=24,
        summary="Six rules (three terms, middle term distributed, distribution in the conclusion, no two negative premises, negative premise if and only if negative conclusion, and, in the Boolean view, no particular conclusion from universal premises) test any categorical syllogism without a diagram.",
        objectives=[
            "Say which terms each of A, E, I and O distributes",
            "State the general rules of the categorical syllogism",
            "Apply the rules to a syllogism to decide whether it is valid",
            "Explain which rule separates the traditional view (24 valid forms) from the Boolean view (15)",
        ],
        key_concepts=["Distribution", "Rule of three terms", "Distributed middle", "Illicit process", "Negative premises", "Existential rule", "General rules"],
        blocks=[
            H("Introduction"),
            T("A football referee does not replay every match to check a goal. He knows the rules: offside, handball, the ball over the line. "
              "A logician does the same. Instead of drawing a diagram for each syllogism, we can check a short list of **general rules**. "
              "A syllogism that breaks any of them is invalid. One that keeps them all is valid."),
            T("The rules use one idea from the lessons on propositions: **distribution**. We recall it first."),
            D("A term is **distributed** in a proposition if the proposition says something about **all** members of the class the term names. "
              "A term is **undistributed** if the proposition says something only about **some** members.",
              title="Definition: distribution"),
            CODE("""Form   Sentence             Subject       Predicate
A      All S are P          distributed   undistributed
E      No S are P           distributed   distributed
I      Some S are P         undistributed undistributed
O      Some S are not P     undistributed distributed""", "text", title="Distribution of terms in A, E, I and O"),
            T("A short way to remember: **universal** propositions (A and E) distribute their **subject**. **Negative** propositions (E and O) distribute their **predicate**. "
              "Check: All dogs are mammals says something about every dog, but not about every mammal. No dogs are cats says something about every dog and every cat. "
              "Some cats are not dogs says something about every dog (none of them is that cat), but not about every cat."),
            KEY("The general rules", "Which rule list? This lesson follows the common list of Copi and Cohen and of Hurley: a form is valid if it keeps rules 1 to 5 (traditional view), "
                "or rules 1 to 6 (Boolean view). Books number and word the rules a little differently, and some add extra rules. Follow your teacher's list.", cards=[
                ["Rule 1: three terms", "The syllogism has exactly three terms, each used in the same sense throughout. (Breaking it: the fallacy of four terms.)"],
                ["Rule 2: middle term", "The middle term must be distributed in at least one premise. (Breaking it: undistributed middle.)"],
                ["Rule 3: distribution in the conclusion", "A term distributed in the conclusion must be distributed in the premise where it appears. (Breaking it: illicit major or illicit minor.)"],
                ["Rule 4: negative premises", "No syllogism has two negative premises. (Breaking it: exclusive premises.)"],
                ["Rule 5: quality", "A negative conclusion needs a negative premise, and a negative premise needs a negative conclusion."],
                ["Rule 6: existence (Boolean view only)", "Two universal premises cannot give a particular conclusion. In the traditional view this rule is dropped."],
            ]),
            T("Two more rules appear in many books: (a) two particular premises prove nothing; (b) if one premise is particular, the conclusion is particular. "
              "These are **consequences** of the rules above, so they need not be learned separately. "
              "Every one of these claims was checked by testing all 256 forms against all fillings of the eight Venn regions: "
              "the forms that keep rules 2 to 5 are exactly the 24 traditional valid forms, and the forms that also keep rule 6 are exactly the 15 Boolean valid forms. "
              "Rule 1 cannot be checked on the form: it is part of what we mean by a three-term syllogism."),
            KEY("How to apply the rules", "Write the mood and figure. Then, in order: (1) count the terms; (2) mark the distributed terms in each sentence; "
                "(3) check the middle term; (4) check each term distributed in the conclusion; (5) count the negative sentences; (6) look at universal premises with a particular conclusion."),
            EX("Worked example 1: a valid form (Barbara, AAA-1)", intro=(
                "All taxi drivers are licensed. All Mile 4 drivers are taxi drivers. So all Mile 4 drivers are licensed."), steps=[
                S("Terms", text="M = taxi drivers (middle), P = licensed people (major), S = Mile 4 drivers (minor). Three terms: Rule 1 kept."),
                S("Distribution", text="Major premise All M are P: M distributed, P not. Minor premise All S are M: S distributed, M not. Conclusion All S are P: S distributed, P not."),
                S("Rule 2", text="M is distributed in the major premise. Kept."),
                S("Rule 3", text="Only S is distributed in the conclusion; S is distributed in the minor premise. Kept."),
                S("Rules 4 and 5", text="No negative sentences. Both rules kept."),
                S("Rule 6", text="Two universal premises with a universal conclusion. Kept. Verdict: **valid**."),
            ]),
            EX("Worked example 2: an invalid form (AAA-2)", intro=(
                "All mangoes are fruits. All pawpaws are fruits. So all pawpaws are mangoes."), steps=[
                S("Form", text="M = fruits, P = mangoes, S = pawpaws. P-M, S-M: Figure 2. Mood AAA."),
                S("Distribution", text="All P are M: P distributed, M not. All S are M: S distributed, M not."),
                S("Rule 2", text="M (fruits) is the predicate of both A premises: not distributed anywhere. **Rule 2 is broken**: undistributed middle. The form is invalid."),
            ]),
            EX("Worked example 3: when the rules split the views (AAI-1)", intro=(
                "All people who cheat are disqualified. All candidates who bribed the invigilator are people who cheat. So some candidates who bribed the invigilator are disqualified."), steps=[
                S("Form", text="M = people who cheat, P = disqualified people, S = candidates who bribed. AAI-1 (Barbari)."),
                S("Rules 1 to 5", text="Three terms: Rule 1 kept. M is the subject of All M are P, so it is distributed in the major premise: Rule 2 kept. The conclusion (I) distributes no term: Rule 3 kept. There is no negative sentence: Rules 4 and 5 kept."),
                S("Rule 6", text="Two universal premises, particular conclusion: **Rule 6 is broken**."),
                S("Verdict", text="Traditional view (rules 1 to 5): valid, if some candidates did bribe the invigilator (S has members). Boolean view (rule 6 as well): invalid, because the premises do not say that any such candidate exists."),
            ]),
            TIP("Exam link: Paper 1 asks \"Which rule does this syllogism break?\" or \"Which term is distributed in ...?\". Paper 2 asks you to test a syllogism by the rules and name the rule broken. "
                "Always write the form (mood and figure) first, then go down the rules in order."),
            MISTAKE("Checking distribution in the wrong place", "Rule 3 says the term must be distributed in **the premise where it appears**. The major term is checked in the major premise, and the minor term in the minor premise. "
                    "A term distributed in the other premise does not help."),
            MISTAKE("Using Rule 6 in the traditional view", "Under the traditional view, an AAI or EAO form can be valid. Do not use Rule 6 unless your textbook follows the Boolean view. State the view you use."),
            MISTAKE("Thinking that I is negative", "A particular proposition (I, O) is not negative just because it says \"some\". Only E and O are negative. "
                    "I is affirmative."),
            QUIZ("Which terms does the proposition Some S are not P distribute?",
                 ["S only", "P only", "Both S and P", "Neither"], 1,
                 "O distributes only its predicate: Some S are not P says something about every P (none of them is that S).",
                 hint="O is both particular and negative: particular propositions leave the subject undistributed, negative propositions distribute the predicate.",
                 feedback=["S is the subject of a particular proposition, so it is undistributed.", "",
                           "Both terms are distributed only in E.", "Neither term is distributed only in I."]),
            QUIZ("Which rule does the syllogism All P are M, All S are M, so all S are P break?",
                 ["Rule 1: three terms", "Rule 2: the middle term must be distributed", "Rule 4: no two negative premises", "Rule 5: negative premise and negative conclusion"], 1,
                 "M is the predicate of both A premises, so it is never distributed: the middle term is undistributed.",
                 hint="Find the middle term and see whether it is a subject or a predicate of an A sentence.",
                 feedback=["The syllogism has three terms: S, P, M.", "",
                           "Both premises and the conclusion are affirmative: nothing negative.",
                           "No negative sentences at all: Rule 5 is kept."]),
            PQ("Mark the distributed terms in: (a) All taxis are cars. (b) No cars are bicycles. (c) Some roads are not tarred. (d) Some students are prefects.",
               "(a) A: taxis distributed, cars not. (b) E: cars and bicycles both distributed. (c) O: roads not, tarred things distributed. (d) I: neither distributed."),
            PQ("Test by the rules: No tomatoes are meat. All sausages are meat. So no sausages are tomatoes (EAE-2).",
               "Terms: M = meat, P = tomatoes, S = sausages. Three terms. Distribution: No P are M (E): P and M distributed. All S are M (A): S distributed. Conclusion No S are P (E): S and P distributed. Rule 2: M distributed in the major premise: kept. Rule 3: P distributed in the conclusion and in the major premise; S distributed in the conclusion and in the minor premise: kept. Rule 4: one negative premise: kept. Rule 5: one negative premise and a negative conclusion: kept. Rule 6: the conclusion is universal: kept. Valid (Cesare)."),
            PQ("Which rule do all of EEE, EEA and OOO break, whatever their figure?",
               "Rule 4: they all have two negative premises (E and E, or O and O)."),
            PQ("A syllogism has an E major premise and an A minor premise. What does Rule 5 say about its conclusion?",
               "One premise is negative (the E), so the conclusion must be negative: E or O. Which of the two can be valid depends on the figure (for example EAE-1 and EAE-2 are valid; in Figures 3 and 4 only EAO is valid, and only with the existential assumption)."),
            SUM("A term is distributed when the sentence speaks about all its members. A and E distribute the subject; E and O distribute the predicate.",
                "Rules: three terms; middle term distributed once; a term distributed in the conclusion must be distributed in its premise; no two negative premises; negative conclusion if and only if a negative premise; (Boolean view) no particular conclusion from two universal premises.",
                "The forms that keep rules 2 to 5 are the 24 traditional valid forms. Adding rule 6 leaves the 15 Boolean valid forms.",
                "Say which rule list and which view you follow: books number the rules differently."),
        ],
    ),
    lesson(
        module=MODULE,
        topic="The general rules of the syllogism and fallacies",
        title="Syllogistic fallacies",
        slug="syl-syllogistic-fallacies",
        minutes=24,
        summary="Each general rule has a fallacy named for breaking it: four terms, undistributed middle, illicit major, illicit minor, exclusive premises, affirmative conclusion from a negative premise (and the reverse), and the existential fallacy.",
        objectives=[
            "Name the fallacy that goes with each broken rule of the syllogism",
            "Recognise each fallacy in an everyday argument",
            "Show that a fallacious form is invalid by an argument of the same form with true premises and a false conclusion",
            "Say that one syllogism can commit more than one fallacy",
        ],
        key_concepts=["Formal fallacy", "Four terms", "Undistributed middle", "Illicit major", "Illicit minor", "Exclusive premises", "Existential fallacy"],
        blocks=[
            H("Introduction"),
            T("A trader tells you: \"All good shea butter is expensive. This butter is expensive. So it is good shea butter.\" It sounds right, but it is not. "
              "An expensive butter might be expensive for another reason. This is a **fallacy**, a mistake in reasoning that can look like good reasoning."),
            D("A **formal fallacy** is an invalid form of argument: its conclusion does not follow from its premises because of the **shape** of the argument, whatever the topic. "
              "For the categorical syllogism, every formal fallacy is the breaking of one of the general rules. "
              "The standard names, as used by Copi and Cohen and by Hurley, are given below.",
              title="Definition: formal fallacy"),
            CODE("""Rule broken                                  Fallacy
Rule 1: three terms                          Fallacy of four terms (equivocation)
Rule 2: middle term distributed              Undistributed middle
Rule 3: major term distributed in conclusion Illicit major
        but not in the major premise
Rule 3: minor term distributed in conclusion Illicit minor
        but not in the minor premise
Rule 4: two negative premises                Exclusive premises
Rule 5: negative premise, affirmative        Drawing an affirmative conclusion
        conclusion                           from a negative premise
Rule 5: affirmative premises, negative       Drawing a negative conclusion
        conclusion                           from affirmative premises
Rule 6: universal premises, particular       Existential fallacy
        conclusion (Boolean view only)""", "text", title="Each rule and its fallacy"),
            T("A good way to see that a form is invalid is to find another argument of the **same form** with true premises and a false conclusion. "
              "Each fallacy below comes with one. Every form named here was tested by computer against all fillings of the Venn regions."),
            H("The fallacies, one by one"),
            D("**The fallacy of four terms (equivocation).** A word is used with two meanings, so the argument has four terms, not three.\n\n"
              "Example: All bats are animals that fly at night. All cricket bats are bats. So all cricket bats are animals that fly at night. "
              "It looks like Barbara (AAA-1), but \"bat\" means an animal in the first premise and a piece of sports equipment in the second. "
              "The middle term is not one term, so nothing connects the premises.",
              title="Fallacy 1: four terms"),
            D("**Undistributed middle.** The middle term is not distributed in either premise, so the premises do not link S and P.\n\n"
              "Example (AAA-2): All mangoes are fruits. All pawpaws are fruits. So all pawpaws are mangoes. "
              "The premises are true and the conclusion is false. Fruits is the predicate of both A premises, so it is never distributed. "
              "The fruits mentioned in the two premises need not be the same fruits.",
              title="Fallacy 2: undistributed middle"),
            D("**Illicit major (illicit process of the major term).** The major term is distributed in the conclusion but not in the major premise.\n\n"
              "Example (AEE-1): All cocoa trees are plants that need rain. No oil palms are cocoa trees. So no oil palms are plants that need rain. "
              "The conclusion is E, so it speaks about **all** plants that need rain. The major premise is A, where its predicate is undistributed: it speaks only about cocoa trees. "
              "The premises are true and the conclusion is false.",
              title="Fallacy 3: illicit major"),
            D("**Illicit minor (illicit process of the minor term).** The minor term is distributed in the conclusion but not in the minor premise.\n\n"
              "Example (AAA-3): All goats are animals with four legs. All goats are farm animals. So all farm animals are animals with four legs. "
              "The conclusion is A, so it speaks about **all** farm animals. In the minor premise \"farm animals\" is the predicate of an A sentence, undistributed: it speaks only about goats. "
              "The premises are true and the conclusion is false (hens have two legs).",
              title="Fallacy 4: illicit minor"),
            D("**Exclusive premises.** Both premises are negative. Two exclusions do not connect S and P.\n\n"
              "Example (EEE-1): No rocks are mammals. No pets are rocks. So no pets are mammals. "
              "The premises are true and the conclusion is false (many pets are mammals). "
              "Even when the conclusion happens to be true, the argument is still invalid: \"No lorries are bicycles. No bicycles are canoes. So no lorries are canoes\" has a true conclusion but no reasoning that supports it.",
              title="Fallacy 5: exclusive premises"),
            D("**Drawing an affirmative conclusion from a negative premise.** One premise is negative but the conclusion is affirmative. "
              "(The twin fallacy, **drawing a negative conclusion from affirmative premises**, is the opposite mistake.)\n\n"
              "Example (EAA-1): No snakes are mammals. All pythons are snakes. So all pythons are mammals. "
              "A negative premise separates classes: it cannot join them in the conclusion.\n\n"
              "Twin example (AAE-1): All dogs are mammals. All puppies are dogs. So no puppies are mammals. "
              "Two affirmative premises join classes: they cannot separate them. This one also commits the illicit major.",
              title="Fallacy 6: affirmative from negative (and the reverse)"),
            D("**The existential fallacy (Boolean view).** Two universal premises are used to draw a particular conclusion. "
              "The particular conclusion says that something exists, but universal premises do not.\n\n"
              "Example (AAI-1): All people who cheat are disqualified. All candidates who bribed the invigilator are people who cheat. "
              "So some candidates who bribed the invigilator are disqualified. "
              "If no candidate bribed the invigilator, both premises are true and the conclusion is false. "
              "In the traditional view this form (Barbari) is valid if such candidates exist. Not every textbook lists this fallacy: follow your teacher's book.",
              title="Fallacy 7: existential fallacy"),
            EX("Worked example 1: naming the fallacy", intro=(
                "No snakes are mammals. All pythons are snakes. So all pythons are mammals. Name the fallacy."), steps=[
                S("Form", text="M = snakes, P = mammals, S = pythons. No M are P (E), All S are M (A), All S are P (A). EAA-1."),
                S("Run down the rules", text="Three terms: kept. Middle term: distributed in the major premise (E subject): kept. Conclusion A distributes S, which is distributed in the minor premise: kept. Two negative premises? No: kept."),
                S("Rule 5", text="One premise is negative but the conclusion is affirmative: **broken**."),
                S("Name it", text="Drawing an affirmative conclusion from a negative premise. The valid form with these premises is Celarent (EAE-1): no pythons are mammals."),
            ]),
            EX("Worked example 2: one argument, two fallacies", intro=(
                "All dogs are mammals. All puppies are dogs. So no puppies are mammals. Which fallacies does it commit?"), steps=[
                S("Form", text="M = dogs, P = mammals, S = puppies. All M are P (A), All S are M (A), No S are P (E). AAE-1."),
                S("Rule 5", text="Both premises are affirmative and the conclusion is negative: drawing a negative conclusion from affirmative premises."),
                S("Rule 3", text="The conclusion E distributes P (mammals). In the major premise, an A sentence, the predicate is undistributed: illicit major."),
                S("Report", text="Two fallacies. One argument can break several rules, and a full answer names all of them."),
            ]),
            EX("Worked example 3: telling the fallacy from the example", intro=(
                "All teachers are graduates. All teachers are adults. So all adults are graduates. Which rule is broken, and how can you show the form is invalid?"), steps=[
                S("Form", text="M = teachers, P = graduates, S = adults. All M are P, All M are S, All S are P: AAA-3."),
                S("Distribution", text="The conclusion A distributes S (adults). In the minor premise All M are S, S is the predicate, so it is undistributed."),
                S("Name it", text="Illicit minor."),
                S("Show invalidity", text="Same form, true premises, false conclusion: All goats are four-legged animals. All goats are farm animals. So all farm animals are four-legged animals."),
            ]),
            TIP("Exam link: Paper 1 may give a syllogism and ask \"Which fallacy does it commit?\". Paper 2 may ask you to name the rule broken and the fallacy, and to explain it. "
                "Use the standard names, give the rule number or wording, and quote the term that is wrongly distributed or undistributed."),
            MISTAKE("Calling an argument fallacious because its conclusion is false", "A valid argument can have a false conclusion if a premise is false. A fallacious argument can have a true conclusion. "
                    "A fallacy is a fault in the **form**, not in the facts."),
            MISTAKE("Naming only one fallacy when there are two", "Check all the rules. AAE-1 breaks Rule 5 and Rule 3, and the full answer names both."),
            MISTAKE("Mixing up illicit major and illicit minor", "Illicit major concerns the major term (the predicate of the conclusion) and the major premise. Illicit minor concerns the minor term (the subject of the conclusion) and the minor premise."),
            QUIZ("\"All lawyers are well-spoken. All politicians are well-spoken. So all politicians are lawyers.\" This commits:",
                 ["Illicit major", "Undistributed middle", "Exclusive premises", "The fallacy of four terms"], 1,
                 "Well-spoken people is the middle term and the predicate of both A premises: it is not distributed in either.",
                 hint="Which term appears in both premises, and is it a subject or a predicate?",
                 feedback=["The conclusion is an A sentence. It distributes only its subject (politicians), not the major term.", "",
                           "Neither premise is negative.", "There are three terms, each used in one sense."]),
            QUIZ("No fish are birds. Some birds are not swimmers. So some swimmers are not fish. Which fallacy?",
                 ["Illicit minor", "Existential fallacy", "Exclusive premises", "Undistributed middle"], 2,
                 "Both premises are negative (E and O): exclusive premises.",
                 hint="Count the negative premises.",
                 feedback=["The conclusion is O, which does not distribute its subject.", "The existential fallacy needs two universal premises; here only one premise is universal.", "",
                           "The middle term is the predicate of an E sentence in one premise, so it is distributed."]),
            PQ("Name the fallacy: \"Every student of the school wears uniform. Ewane wears uniform. So Ewane is a student of the school.\"",
               "Form: All P are M (All students wear uniform), All S are M (Ewane wears uniform), All S are P. AAA-2. The middle term (people who wear uniform) is the predicate of both A premises: undistributed middle."),
            PQ("Name the fallacy: \"No cats are dogs. All kittens are cats. So all kittens are dogs.\"",
               "EAA-1: one negative premise, affirmative conclusion. Drawing an affirmative conclusion from a negative premise."),
            PQ("Give an argument of the form AAA-2 with true premises and a false conclusion, and name its fallacy.",
               "All cars are vehicles. All bicycles are vehicles. So all bicycles are cars. The premises are true, the conclusion is false. Fallacy: undistributed middle (vehicles)."),
            PQ("In which view is the existential fallacy a fallacy, and why is the same form valid in the other view?",
               "In the Boolean view, which does not assume that classes have members. In the traditional view the classes are assumed to have members, so a form such as Barbari (AAI-1) is valid there."),
            SUM("Each general rule has a named fallacy: four terms, undistributed middle, illicit major, illicit minor, exclusive premises, affirmative conclusion from a negative premise (and the reverse), existential fallacy.",
                "A fallacy of form is shown by an argument of the same form with true premises and a false conclusion.",
                "One argument can commit more than one fallacy: name them all.",
                "The existential fallacy belongs to the Boolean view. Textbooks differ: follow your teacher's list and say which view you use."),
        ],
    ),
    # --- END LESSONS ---
]
