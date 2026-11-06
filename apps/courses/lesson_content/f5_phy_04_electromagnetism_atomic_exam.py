"""Form 5 Physics (O Level 0580): Electricity and Magnetism (second half), Atomic, Nuclear and Basic Electronics,
and the Examination module (Paper 1 and Paper 2).

Draft content written from KKEVO's master curriculum blueprint and the Board's 2023 Ordinary Level report; it is not a
Board syllabus booklet. A reviewer must check it against the Board's syllabus and the school textbooks. Constants used:
g = 10 m/s2, speed of light c = 3.0 x 10^8 m/s, mains about 220 V and 50 Hz (check your textbook), half-life of
carbon-14 taken as 5700 years (many books use 5730). Exam facts are only those of the Board's 2023 report. Time plans
and checklists are KKEVO study advice, not official rules.
"""

from .dsl import *  # noqa: F403

COURSE = ("physics", "form-5")

M_EM = "Electricity & Magnetism"
M_AT = "Atomic, Nuclear & Basic Electronics"
M_EX = "Examination"

LESSONS = [
    # ------------------------------------------------------------------ 1. Domestic wiring
    lesson(
        module=M_EM, topic="Domestic wiring and safety",
        title="Domestic wiring, fuses and earthing",
        slug="phd-domestic-wiring-fuses-earthing",
        minutes=22,
        summary="Live, neutral and earth wires; why the fuse and switch go in the live wire; choosing a fuse rating from I = P/V; "
                "circuit breakers; earthing; double insulation and the danger of overloading.",
        objectives=[
            "Name the live, neutral and earth wires and state the job of each",
            "Explain why fuses and switches are placed in the live wire",
            "Choose a suitable fuse rating by calculating the current an appliance takes",
            "Explain how earthing, a circuit breaker and double insulation make a house safer",
        ],
        key_concepts=["Live wire", "Neutral wire", "Earth wire", "Fuse", "Circuit breaker", "Earthing", "Overloading"],
        blocks=[
            H("Introduction"),
            T("A child in a house in Bamenda touches the metal case of a faulty iron. A neighbour's child does the same in a "
              "house where the iron is properly earthed. The first child gets a dangerous shock. In the second house, a fuse "
              "melts and the iron goes dead. The difference is the wiring.\n\n"
              "Mains electricity can kill. In this lesson you learn how a house is wired, what a fuse and an earth wire do, "
              "and how to choose a safe fuse."),
            T("Mains electricity in Cameroon is about 220 V alternating current at 50 Hz. We use 220 V in the calculations here. "
              "The colours of wires differ between countries and between old and new wiring. Learn the rule below and check "
              "the colour code in your textbook."),
            H("The three wires"),
            IMG("f5ph-d-wiring.svg",
                alt="A mains supply with live, neutral and earth wires going to an appliance. A fuse and a switch are in the live wire and the earth wire joins the metal case.",
                caption="Figure 1. The fuse and the switch are in the live wire. The earth wire joins the metal case."),
            D("The **live wire** carries the current to the appliance and is at a high potential (about 220 V compared with earth). "
              "The **neutral wire** completes the circuit and is near 0 V. The **earth wire** is a safety wire joined to the ground "
              "and to the metal case of the appliance. It carries no current when everything works well.",
              title="Live, neutral and earth"),
            T("Colour codes. In the newer international code the live wire is brown, the neutral wire is blue and the earth wire "
              "is green with a yellow stripe. Older wiring often uses red for live, black for neutral and green for earth. "
              "Check your textbook for the code your examiner expects."),
            H("The fuse"),
            D("A **fuse** is a thin wire in a small holder, put in the live wire. If the current becomes bigger than the rating of "
              "the fuse, the wire heats up, melts and breaks the circuit. The **rating** of a fuse is the largest current it "
              "allows (in amperes).",
              title="Fuse"),
            T("The fuse must be in the **live** wire. Then, when it melts, the appliance is cut off from the high potential. "
              "If the fuse were in the neutral wire, the appliance would still be joined to the live wire and would still be "
              "dangerous to touch after the fuse blew."),
            D("Fuse ratings are made in steps such as 1 A, 3 A, 5 A, 10 A and 13 A. Choose a fuse whose rating is **just above** the "
              "normal current of the appliance. Find the normal current from the power rating of the appliance.",
              title="Choosing a fuse", formula=r"I = \dfrac{P}{V}"),
            EX("Worked example 1: an electric kettle", intro="An electric kettle is marked 2.2 kW and the supply is 220 V. Which fuse should be fitted: 3 A, 5 A, 10 A or 13 A?", steps=[
                S("Change the power to watts", math=r"P = 2.2 \text{ kW} = 2200 \text{ W}"),
                S("Calculate the normal current", math=r"I = \dfrac{P}{V} = \dfrac{2200}{220} = 10 \text{ A}"),
                S("Choose the rating just above", text="A 10 A fuse would be at its limit and might melt in normal use. The 13 A fuse is just above 10 A, so choose the 13 A fuse."),
            ], check=r"10 \text{ A} < 13 \text{ A}"),
            EX("Worked example 2: a small television", intro="A television is marked 110 W on a 220 V supply. Choose a fuse from 1 A, 3 A, 5 A, 13 A.", steps=[
                S("Calculate the current", math=r"I = \dfrac{110}{220} = 0.5 \text{ A}"),
                S("Choose the rating just above 0.5 A", text="The 1 A fuse is just above 0.5 A. A 13 A fuse would be too large: it would let a harmful fault current flow before it melted."),
            ]),
            H("Circuit breakers and earthing"),
            D("A **circuit breaker** is an automatic switch. When the current is too large, an electromagnet pulls open a switch and "
              "breaks the circuit. After the fault is repaired, you press the switch to **reset** it. It does not need replacing "
              "like a fuse.",
              title="Circuit breaker"),
            T("Fuses are cheap but must be replaced. Circuit breakers act quickly and can be reset many times, so they are used in "
              "the main box of many modern buildings."),
            D("**Earthing** means joining the metal case of an appliance to the ground by the earth wire. If the live wire touches "
              "the case by accident, a large current flows through the earth wire to the ground. The large current melts the fuse "
              "and cuts off the supply. The case never stays at a high potential.",
              title="Earthing"),
            KEY("What if there is no earth wire?",
                "A loose live wire touches the metal case. The case is now at about 220 V. The fuse does not melt because the current "
                "is small. The next person who touches the case becomes the path to the ground and gets a serious shock.",
                cards=[["With earth wire", "Large fault current flows to the ground. The fuse melts. The case is safe."],
                       ["Without earth wire", "The case stays live. A person touching it gets a shock."]]),
            T("**Double insulation.** Many appliances have a plastic case and extra insulation inside, so that the user cannot reach "
              "any live part. They need no earth wire. A radio and a hair dryer are often made like this."),
            H("Overloading"),
            T("In a house the sockets are joined in **parallel**. Each socket gets the full 220 V and each appliance works "
              "independently. The currents of all appliances add up in the main wire. If too many appliances are plugged into one "
              "socket (an overloaded socket), the total current is very large and the wires get hot. This can start a fire."),
            EX("Worked example 3: an overloaded socket", intro="A 13 A fuse protects a socket. A kettle (2200 W), an iron (1100 W) and a television (110 W) are plugged into it with an adapter. The supply is 220 V. What happens?", steps=[
                S("Add the powers", math=r"P = 2200 + 1100 + 110 = 3410 \text{ W}"),
                S("Total current", math=r"I = \dfrac{3410}{220} = 15.5 \text{ A}"),
                S("Compare with the fuse", text="15.5 A is greater than 13 A, so the fuse melts. This is the fuse doing its job: it stops the wires overheating."),
            ]),
            MISTAKE("Putting the fuse or switch in the neutral wire",
                    "They go in the **live** wire. In the neutral wire, the appliance stays connected to the high potential when the fuse blows or the switch is off."),
            MISTAKE("Choosing a fuse far above the normal current",
                    "A very large fuse does not melt when it should, so it does not protect the wires. Choose the rating just above the normal current."),
            MISTAKE("Saying the earth wire carries the normal current",
                    "In normal use the earth wire carries no current. It carries a current only when there is a fault."),
            QUIZ("Why is the fuse placed in the live wire?",
                 ["So that the neutral wire carries more current", "So that the appliance is disconnected from the high potential when the fuse melts",
                  "So that the appliance uses less power", "So that the earth wire can be removed"], 1,
                 "A fuse in the live wire cuts the appliance off from the high potential when it melts.",
                 hint="Think about which wire is at 220 V.",
                 feedback=["The fuse does not change the current in the neutral wire.", "",
                           "A fuse protects the wiring. It does not lower the power used.", "The earth wire is still needed for safety."]),
            QUIZ("Which fuse is best for a 920 W iron on a 220 V supply? (Ratings available: 1 A, 3 A, 5 A, 13 A.)",
                 ["1 A", "3 A", "5 A", "13 A"], 2,
                 "I = 920/220 = 4.2 A. The rating just above 4.2 A is 5 A.",
                 hint="Calculate the current first with I = P/V.",
                 feedback=["1 A is below the normal current. It would melt at once.", "3 A is below 4.2 A, so it would melt in normal use.", "",
                           "13 A is too large. It would not protect the iron."]),
            TIP("**Exam link.** Wiring and safety appear in Paper 1 multiple choice (which wire has the fuse, what earthing does, which fuse to choose) "
                "and in Paper 2 calculations with I = P/V. In Paper 2 write the unit (A) and give a reason for your choice of fuse.",
                title="Where this appears"),
            PQ("A water heater is marked 3.3 kW and 220 V. (a) Calculate its normal current. (b) Choose a fuse from 5 A, 10 A, 13 A, 30 A.",
               r"(a) $I = P/V = 3300/220 = 15 \text{ A}$. (b) The fuse must be just above 15 A, so choose the 30 A fuse. (A 13 A fuse is too small and would melt.)"),
            PQ("Explain how an earth wire protects a person using a metal-cased cooker.",
               "The earth wire joins the metal case to the ground. If the live wire touches the case, a large current flows through the earth wire to the ground. "
               "This large current melts the fuse and cuts off the supply, so the case does not stay at a high potential and a person touching it is not shocked."),
            PQ("State two differences between a fuse and a circuit breaker.",
               "A fuse melts and must be replaced after it works; a circuit breaker is a switch that is reset by pressing it. A circuit breaker works with an electromagnet and acts faster than a fuse."),
            PQ("Why is it dangerous to plug many appliances into one socket?",
               "The currents add up, so the total current in the socket and wires is very large. The wires get hot and may start a fire. The fuse should melt, but an over-rated fuse would not."),
            SUM("The live wire is at high potential; the neutral wire completes the circuit; the earth wire is a safety wire.",
                "The fuse and the switch go in the live wire. A fuse melts when the current is too large.",
                "Choose a fuse just above the normal current, found from I = P/V.",
                "Earthing sends a fault current to the ground so that the fuse melts and the case is not left live.",
                "A circuit breaker is a resettable automatic switch. Double insulation needs no earth wire.",
                "Overloading means too much total current, which overheats wires."),
        ],
    ),
    # ------------------------------------------------------------------ 2. Magnetism
    lesson(
        module=M_EM, topic="Magnetism and magnetic fields",
        title="Magnets, magnetic fields and magnetization",
        slug="phd-magnets-fields-magnetization",
        minutes=22,
        summary="Magnetic materials and poles, the law of poles, field lines and the Earth's field, domains, making and removing magnetism, "
                "soft iron and steel, and the electromagnet.",
        objectives=[
            "State the law of magnetic poles and the only sure test for a magnet",
            "Draw magnetic field lines and describe how to plot them with a compass",
            "Describe how to magnetize and demagnetize a material and explain it with domains",
            "Compare soft iron and steel and say how an electromagnet works",
        ],
        key_concepts=["Magnetic material", "Pole", "Magnetic field", "Field line", "Domain", "Magnetization", "Soft iron", "Electromagnet"],
        blocks=[
            H("Introduction"),
            T("A fisherman on the Atlantic coast at Limbe uses a compass to keep direction when the shore is out of sight. A mechanic in "
              "Douala uses a small magnet to pick up steel screws from the floor. Both depend on the same property, **magnetism**.\n\n"
              "In this lesson you learn what magnets do, how to draw the field around them, and how magnetism is made and removed."),
            H("Magnets and poles"),
            D("A **magnetic material** is a material that is attracted by a magnet. The main ones are iron, steel, nickel and cobalt. "
              "Copper, aluminium, wood and plastic are not magnetic.",
              title="Magnetic materials"),
            D("The ends of a magnet, where the force is strongest, are called the **poles**. A freely hanging magnet turns so that one pole "
              "points to the north: this is its **north-seeking pole (N)**. The other end is the **south-seeking pole (S)**.",
              title="Poles"),
            KEY("The law of magnetic poles",
                "Like poles repel. Unlike poles attract.",
                cards=[["Like poles", "N and N, or S and S: they push each other away."],
                       ["Unlike poles", "N and S: they pull each other together."]]),
            TIP("**The only sure test for a magnet is repulsion.** A magnet attracts both a magnet and an unmagnetized piece of iron, so attraction "
                "does not prove that an object is a magnet. If two objects repel, both must be magnets.",
                title="Testing for a magnet"),
            H("Magnetic fields"),
            D("A **magnetic field** is the region around a magnet where a magnetic force acts on a magnetic material or on another magnet. "
              "We show it with **field lines**. The direction of the field at a point is the direction in which a north pole would move.",
              title="Magnetic field"),
            IMG("f5ph-d-bar-magnet-field.svg",
                alt="Curved field lines leave the N pole of a bar magnet and loop round to the S pole, with arrows pointing from N to S outside the magnet.",
                caption="Figure 1. The field of a bar magnet. The lines are closest together at the poles, where the field is strongest."),
            T("Rules for drawing field lines. (1) They run from the N pole to the S pole outside the magnet. (2) They never cross. "
              "(3) They are closest together where the field is strongest. (4) Between two unlike poles they link the poles; "
              "between two like poles they push away from each other and a point in the middle has no field."),
            T("**Plotting a field with a compass.** Place a bar magnet on paper. Put a small plotting compass near the N pole and mark the "
              "position of both ends of the needle with dots. Move the compass so that its tail is at the last dot, and mark again. "
              "Repeat until you reach the S pole, then join the dots. Start again at another point to draw more lines."),
            T("The Earth has a magnetic field like a huge bar magnet. A compass needle lines up with it, so its N end points roughly to the geographic north. "
              "Because unlike poles attract, the magnetic pole in the Earth's north behaves like a magnetic S pole. Do not worry about this detail "
              "in a multiple-choice question: the needle's N end points north."),
            H("Magnetization and demagnetization"),
            D("A magnetic material contains tiny regions called **domains**, each acting like a very small magnet. In an unmagnetized piece, "
              "the domains point in all directions and cancel. In a magnet, most domains point the same way.",
              title="Domain theory"),
            KEY("Ways to magnetize and demagnetize",
                "Magnetize: stroke the steel with one pole of a magnet in the same direction many times; or put it inside a solenoid carrying direct current; "
                "or hammer it while it lies in a north-south direction.\n\nDemagnetize: hammer it while it lies east-west; or heat it red hot; or place it in a solenoid carrying alternating current and slowly pull it out.",
                cards=[["Magnetize", "Stroking, a d.c. solenoid, hammering in the Earth's field."],
                       ["Demagnetize", "Hammering east-west, heating, an a.c. solenoid slowly withdrawn."]]),
            T("**Why does it work?** Stroking and the solenoid line up the domains. Hammering and heating shake the domains so that they point "
              "in random directions again. Heating, dropping and hammering also weaken magnets that you store badly."),
            T("**Soft iron and steel.** Soft iron is magnetized easily and loses its magnetism easily, so it is used for the cores of electromagnets and transformers. "
              "Steel is hard to magnetize but keeps its magnetism, so it is used for permanent magnets such as the needle of a compass. "
              "Store bar magnets in pairs with unlike poles together and with soft-iron keepers across their ends. "
              "A soft-iron ring around a delicate instrument can also act as a shield, because the field lines pass through the iron instead of the space inside."),
            H("The electromagnet"),
            D("An **electromagnet** is a coil of wire (a **solenoid**) wound on a soft-iron core. When current flows, the core becomes a strong magnet. "
              "When the current stops, the magnetism almost disappears.",
              title="Electromagnet"),
            T("**Right-hand grip rule for a solenoid.** Look at one end of the coil. If the current goes round **anticlockwise**, that end is a "
              "**north** pole. If the current goes round **clockwise**, that end is a **south** pole. "
              "The strength of an electromagnet increases with more turns, more current and a soft-iron core. "
              "It is used in scrapyard cranes, electric bells, relays and loudspeakers."),
            EX("Worked example 1: identifying poles", intro="A bar P repels one end of a compass needle and attracts the other end. A second bar Q attracts both ends of the needle. Which bar is a magnet?", steps=[
                S("Repulsion is the sure test", text="P repels one end of the needle, so P must be a magnet."),
                S("Attraction of both ends", text="Q attracts both ends. A magnet attracts a magnetic material such as unmagnetized iron, so Q can be an unmagnetized piece of iron or steel."),
                S("Conclusion", text="P is a magnet. Q is not shown to be a magnet."),
            ]),
            EX("Worked example 2: polarity of an electromagnet", intro="Current goes round the right end of a coil anticlockwise (seen from the right). What is the pole at that end? What if the current is reversed?", steps=[
                S("Use the grip rule", text="Anticlockwise gives a north pole."),
                S("Reverse the current", text="The direction becomes clockwise, so the same end becomes a south pole. Reversing the current reverses the poles."),
            ]),
            MISTAKE("Using attraction as proof of a magnet",
                    "A magnet attracts unmagnetized iron too. Only repulsion proves that both objects are magnets."),
            MISTAKE("Field lines that cross or point from S to N outside the magnet",
                    "Field lines never cross and outside the magnet they run from N to S."),
            QUIZ("A student hangs a bar magnet on a thread. It turns until one end points north. Another bar is brought near this north-pointing end, and they repel. The second bar is...",
                 ["A magnet with its north pole near the first bar", "A magnet with its south pole near the first bar", "An unmagnetized iron bar", "A copper bar"], 0,
                 "Repulsion means like poles face each other, so the second bar is a magnet with its N pole near the north-pointing end.",
                 hint="Repulsion happens only between like poles.",
                 feedback=["", "Unlike poles attract.", "Iron is attracted by a magnet and is never repelled.", "Copper is not magnetic and is not repelled."]),
            QUIZ("Which material is best for the core of an electromagnet?",
                 ["Steel", "Soft iron", "Copper", "Plastic"], 1,
                 "Soft iron is magnetized strongly and loses its magnetism when the current stops.",
                 hint="The core must switch on and off.",
                 feedback=["Steel stays magnetized after the current stops.", "", "Copper is not a magnetic material.", "Plastic is not a magnetic material."]),
            TIP("**Exam link.** Magnetism appears in Paper 1 multiple choice (poles, field lines, test for a magnet, soft iron and steel) and in Paper 2 "
                "in descriptions of how to magnetize or demagnetize. Draw field lines with arrows.",
                title="Where this appears"),
            PQ("State the law of magnetic poles and describe the only sure test to show that a bar is a magnet.",
               "Like poles repel and unlike poles attract. The sure test is repulsion: bring one end of the bar near a known pole of a magnet; if it is repelled, the bar is a magnet."),
            PQ("Explain, using domains, why hammering a magnet can demagnetize it.",
               "In a magnet the domains point mostly the same way. Hammering shakes the domains so that they turn and point in random directions. Their effects cancel, so the bar loses its magnetism."),
            PQ("Give two differences between soft iron and steel as magnetic materials, with one use of each.",
               "Soft iron is magnetized and demagnetized easily (use: the core of an electromagnet or a transformer). Steel is hard to magnetize but keeps its magnetism (use: a permanent magnet such as a compass needle)."),
            PQ("State three ways to increase the strength of an electromagnet.",
               "Increase the number of turns of the coil, increase the current, and use a soft-iron core (or a larger core)."),
            SUM("Iron, steel, nickel and cobalt are magnetic materials. Like poles repel; unlike poles attract. Repulsion is the sure test for a magnet.",
                "A magnetic field is the region where a magnet exerts a force. Field lines run from N to S outside the magnet, never cross and are closest where the field is strongest.",
                "Domains line up in a magnet. Stroking and a d.c. solenoid magnetize; hammering, heating and an a.c. solenoid demagnetize.",
                "Soft iron is for electromagnets and transformers; steel is for permanent magnets.",
                "An electromagnet is a coil on a soft-iron core; anticlockwise current gives a north pole at that end."),
        ],
    ),
    # ------------------------------------------------------------------ 3. Force on conductor and motor
    lesson(
        module=M_EM, topic="Electromagnetism and motors",
        title="Force on a current-carrying wire and the d.c. motor",
        slug="phd-force-on-conductor-and-dc-motor",
        minutes=24,
        summary="A current in a magnetic field feels a force. Fleming's left-hand rule gives its direction, F = BIL sin(theta) gives its size, "
                "and a coil with a split-ring commutator turns this force into a d.c. motor.",
        objectives=[
            "State what happens to a current-carrying wire in a magnetic field and use Fleming's left-hand rule",
            "Calculate the force from F = BIL, including the effect of the angle to the field",
            "Describe the parts and the action of a simple d.c. motor",
            "State how to increase the speed or reverse the turning of a motor",
        ],
        key_concepts=["Magnetic field of a current", "Fleming's left-hand rule", "Magnetic flux density (B)", "Tesla", "Force on a conductor", "D.C. motor", "Commutator"],
        blocks=[
            H("Introduction"),
            T("A taxi driver in Yaounde turns the key and the starter motor spins the engine. A fan cools a shop in Garoua. A pump lifts water "
              "to a tank. All these use an **electric motor**.\n\n"
              "A motor works because a wire carrying current in a magnetic field feels a force. This lesson explains that force and how a motor uses it."),
            H("The field of a current"),
            T("A current in a straight wire makes a magnetic field. The field lines are circles around the wire. "
              "The **right-hand grip rule** gives the direction: point the thumb of your right hand along the current; your curled fingers show the "
              "direction of the field. A coil (solenoid) gives a field like a bar magnet, as you saw in the last lesson."),
            H("The force on a current in a field"),
            D("A wire carrying current in a magnetic field, and not parallel to the field, feels a **force**. The force is at right angles to "
              "both the field and the current. The force is largest when the wire is at right angles to the field. There is no force if the wire is parallel to the field.",
              title="Force on a current-carrying conductor"),
            IMG("f5ph-d-coil-forces.svg",
                alt="End view of a coil between a north pole on the left and a south pole on the right. The left side has current out of the page and a force upwards. The right side has current into the page and a force downwards.",
                caption="Figure 1. The two sides of a coil carry current in opposite directions, so the forces are opposite and the coil turns."),
            KEY("Fleming's left-hand rule",
                "Hold the thumb, first finger and second finger of your LEFT hand at right angles to each other.",
                cards=[["First finger", "points along the magnetic Field (from N to S)."],
                       ["Second finger", "points along the Current (from + to -)."],
                       ["Thumb", "shows the direction of the force (the Motion)."]]),
            T("The force is changed in direction if you reverse the current **or** reverse the field. If you reverse both, the force stays the same."),
            H("The size of the force"),
            D("The strength of a magnetic field is called the **magnetic flux density**, $B$. Its unit is the **tesla (T)**. "
              "A field of 1 T exerts a force of 1 N on 1 m of wire carrying 1 A at right angles to the field.",
              title="Magnetic flux density and the tesla"),
            D("For a straight wire of length $L$ in the field, carrying current $I$, with the wire at an angle $\\theta$ to the field:",
              title="Force on a conductor", formula=r"F = BIL \sin\theta"),
            T(r"When the wire is at right angles to the field, $\theta = 90^\circ$ and $\sin 90^\circ = 1$, so $F = BIL$. "
              r"When the wire is parallel to the field, $\theta = 0^\circ$ and $\sin 0^\circ = 0$, so there is no force. "
              r"The force is in newtons (N) when $B$ is in tesla, $I$ in amperes and $L$ in metres."),
            EX("Worked example 1: the force on a wire", intro=r"A wire of length 0.25 m carries a current of 5.0 A at right angles to a field of 0.40 T. Find the force.", steps=[
                S("Write the formula", math=r"F = BIL"),
                S("Substitute", math=r"F = 0.40 \times 5.0 \times 0.25"),
                S("Answer", math=r"F = 0.50 \text{ N}"),
            ]),
            EX("Worked example 2: a wire at an angle", intro=r"A wire of length 0.30 m carries 4.0 A in a field of 0.50 T. The wire makes an angle of $30^\circ$ with the field. Find the force.", steps=[
                S("Write the formula", math=r"F = BIL \sin\theta"),
                S("Substitute", math=r"F = 0.50 \times 4.0 \times 0.30 \times \sin 30^\circ = 0.60 \times 0.5"),
                S("Answer", math=r"F = 0.30 \text{ N}"),
            ]),
            EX("Worked example 3: finding the field", intro=r"A force of 0.12 N acts on a 0.15 m wire carrying 2.0 A at right angles to a field. Find $B$.", steps=[
                S("Rearrange", math=r"B = \dfrac{F}{IL}"),
                S("Substitute", math=r"B = \dfrac{0.12}{2.0 \times 0.15} = \dfrac{0.12}{0.30}"),
                S("Answer", math=r"B = 0.40 \text{ T}"),
            ]),
            H("The d.c. motor"),
            IMG("f5ph-d-motor.svg",
                alt="A coil between a north pole and a south pole joined to a split-ring commutator that touches two brushes joined to a d.c. supply.",
                caption="Figure 2. A simple d.c. motor: coil, magnets, split-ring commutator and brushes."),
            D("A **d.c. motor** has a coil between the poles of a magnet. The coil's ends are joined to the two halves of a **split-ring commutator**. "
              "Two carbon **brushes** press on the commutator and join it to the d.c. supply.",
              title="Parts of a simple d.c. motor"),
            T("**How it works.** Current flows through the coil. The two long sides carry current in opposite directions, so the forces on them are opposite, "
              "and the coil turns. When the coil reaches the vertical position, the split ring changes over its contact with the brushes. "
              "The current in the coil reverses, so the forces still turn the coil the same way. Without the commutator the coil would swing to the vertical position and stop."),
            T("**Making it faster or stronger.** Use a stronger magnet, a larger current, more turns on the coil, or a soft-iron core in the coil. "
              "**Reversing the turning:** reverse the current or reverse the magnetic field (swap the poles), but not both."),
            MISTAKE("Mixing up the left-hand and right-hand rules",
                    "Use the LEFT hand for the force on a current in a field (a motor). The right hand is used for the field of a wire (the grip rule) and, in the next lesson, for the generator."),
            MISTAKE("Forgetting the angle",
                    "F = BIL is for a wire at right angles to the field. If the wire is at an angle, multiply by sin of that angle. There is no force when the wire is parallel to the field."),
            MISTAKE("Forgetting the unit",
                    "The force is in newtons (N), the field in tesla (T). Examiners take marks away for a missing or wrong unit."),
            QUIZ("A wire carries current into the page. The magnetic field runs from left to right. In which direction is the force on the wire?",
                 ["Up the page", "Down the page", "To the left", "To the right"], 1,
                 "First finger to the right (field), second finger into the page (current); the thumb points down the page.",
                 hint="Use Fleming's left-hand rule with the first finger to the right.",
                 feedback=["That would be the force if the current came out of the page.", "", "The force is at right angles to the field and to the current, so it cannot be along the field.",
                           "The force is at right angles to the field, so it cannot be along it."]),
            QUIZ("What is the job of the split-ring commutator in a d.c. motor?",
                 ["It makes the magnetic field stronger", "It reverses the current in the coil every half turn so that the coil keeps turning the same way",
                  "It changes the d.c. supply to a.c.", "It reduces friction at the axle"], 1,
                 "The commutator swaps the contacts each half turn, reversing the current so that the turning force keeps the same direction.",
                 hint="What would happen if the current did not change direction?",
                 feedback=["The magnets make the field. The commutator does not.", "",
                           "The supply is d.c. The commutator only switches the connection to the coil.", "Friction is reduced by lubrication, not by the commutator."]),
            TIP("**Exam link.** Expect F = BIL, Fleming's left-hand rule and the action of a motor in Paper 1 multiple choice and in Paper 2 calculations and descriptions. "
                "Always give the unit of the force (N) and of the field (T).",
                title="Where this appears"),
            PQ(r"A wire of length 0.40 m carries 3.0 A at right angles to a field of 0.25 T. Calculate the force on it.",
               r"$F = BIL = 0.25 \times 3.0 \times 0.40 = 0.30 \text{ N}$."),
            PQ(r"The force on a 0.20 m wire at right angles to a field is 0.060 N when the current is 1.5 A. Find the magnetic flux density.",
               r"$B = F/(IL) = 0.060/(1.5 \times 0.20) = 0.060/0.30 = 0.20 \text{ T}$."),
            PQ("State three ways to make a d.c. motor turn faster.",
               "Use a stronger magnet, increase the current, and use more turns on the coil (a soft-iron core also helps)."),
            PQ("Describe how the direction of rotation of a d.c. motor can be reversed.",
               "Reverse the current (swap the connections to the supply) or reverse the magnetic field (swap the magnet poles). Doing both together does not change the direction."),
            SUM("A current in a magnetic field feels a force at right angles to the field and to the current.",
                "Fleming's left-hand rule: First finger = Field, seCond finger = Current, thuMb = Motion (force).",
                r"The force on a wire is $F = BIL \sin\theta$; at right angles it is $F = BIL$. $B$ is in tesla (T).",
                "A d.c. motor has a coil, magnets, a split-ring commutator and brushes. The commutator reverses the current each half turn.",
                "A motor turns faster with a stronger magnet, a larger current or more turns. Reversing the current or the field reverses the turning."),
        ],
    ),
]

LESSONS += [
    # ------------------------------------------------------------------ 4. Induction and generators
    lesson(
        module=M_EM, topic="Electromagnetic induction and transformers",
        title="Electromagnetic induction, Lenz's law and the a.c. generator",
        slug="phd-induction-lenz-generators",
        minutes=24,
        summary="Moving a magnet and a coil past each other induces an emf. Faraday's law gives its size, Lenz's law its direction, "
                "and the a.c. generator and the dynamo use it to make electricity.",
        objectives=[
            "Describe experiments that show electromagnetic induction and the factors that change the induced emf",
            "State Faraday's law and Lenz's law and use Lenz's law to find a direction",
            "Describe the action of an a.c. generator and sketch its output",
            "Calculate the frequency and period of a generator from its speed of rotation",
        ],
        key_concepts=["Electromagnetic induction", "Induced emf", "Faraday's law", "Lenz's law", "A.c. generator", "Slip rings", "Frequency"],
        blocks=[
            H("Introduction"),
            T("A cyclist in Maroua switches on the lamp. A small dynamo presses on the wheel and the lamp glows, with no battery. "
              "At the Song Loulou and Edea power stations on the Sanaga river, falling water turns huge turbines, and the electricity "
              "that lights Douala and Yaounde is produced. Both use **electromagnetic induction**: making electricity from motion and magnetism."),
            H("Induction experiments"),
            D("**Electromagnetic induction** is the production of an emf (and a current if the circuit is complete) in a conductor when the "
              "magnetic field around it changes, or when the conductor cuts across magnetic field lines. The emf produced is called the **induced emf**.",
              title="Electromagnetic induction"),
            T("**Experiment.** Connect a coil of wire to a sensitive centre-zero galvanometer. Push a bar magnet into the coil. The needle flicks. "
              "Hold the magnet still inside the coil: the needle returns to zero. Pull the magnet out: the needle flicks the other way."),
            KEY("What the experiment shows",
                "An emf is induced only while the magnet and the coil are moving relative to each other, that is, while the field through the coil is changing.",
                cards=[["No movement", "No change in the field, so no emf."],
                       ["Push in or pull out", "The emf has opposite directions."],
                       ["Faster, stronger magnet, more turns", "A larger induced emf."]]),
            D("**Faraday's law:** the size of the induced emf is directly proportional to the rate at which the conductor cuts magnetic field lines "
              "(the rate of change of magnetic flux linked with the circuit).",
              title="Faraday's law"),
            T("So the induced emf is increased by: moving the magnet faster, using a stronger magnet, and using a coil with more turns. "
              "Using a soft-iron core in the coil also helps."),
            D("**Lenz's law:** the direction of an induced current is always such that it **opposes the change** that produces it.",
              title="Lenz's law"),
            T("When a north pole of a magnet is pushed towards a coil, the current in the coil makes the end of the coil nearest the magnet a north pole. "
              "The two north poles repel, so the magnet is pushed back. You must do work to push the magnet in. "
              "This work is the energy that appears as electrical energy. Lenz's law is the law of conservation of energy: you cannot get electricity for nothing."),
            EX("Worked example 1: Lenz's law", intro="The north pole of a bar magnet is pushed towards the left end of a coil. What is the polarity of the left end of the coil? In which direction does the current go round that end (seen from the magnet)?", steps=[
                S("Lenz's law", text="The coil opposes the approach of the magnet, so the end near the magnet must repel it."),
                S("Polarity", text="Repelling a north pole means that the left end becomes a north pole."),
                S("Direction", text="A north pole at the end is made by current going round anticlockwise as seen from that end. So the current is anticlockwise as seen from the magnet."),
            ]),
            T("**Direction of an induced current in a moving wire.** Use **Fleming's right-hand rule**: hold the thumb, first finger and second finger of the RIGHT hand "
              "at right angles. The First finger points along the Field, the thuMb along the Motion of the wire, and the seCond finger gives the direction of the induced Current. "
              "(Left hand for motors, right hand for generators.)"),
            H("The a.c. generator"),
            D("An **a.c. generator** (alternator) has a coil that turns between the poles of a magnet. The ends of the coil are joined to two **slip rings**. "
              "Carbon **brushes** press against the rings and carry the current to the outside circuit.",
              title="A.c. generator"),
            T("**How it works.** As the coil turns, its sides cut the field lines, and an emf is induced. When the coil is **parallel** to the field, the sides "
              "cut the lines fastest and the emf is greatest. When the coil is **perpendicular** to the field, the sides move along the lines and the emf is zero. "
              "After each half turn the sides swap places, so the emf and current change direction. The output is **alternating**."),
            IMG("f5ph-d-ac-generator-graph.svg",
                alt="A sine curve of emf against angle: zero at 0, 180 and 360 degrees, greatest positive at 90 degrees and greatest negative at 270 degrees.",
                caption="Figure 1. The emf of an a.c. generator is zero when the coil is perpendicular to the field and greatest when it is parallel."),
            T("To get a larger output: turn the coil faster, use a stronger magnet, or use more turns on the coil. Turning faster also makes the frequency higher, "
              "and the peak emf larger. A **d.c. generator** uses a split-ring commutator in place of slip rings, so that the output current always goes the same way."),
            D("The **frequency** $f$ of an a.c. generator is the number of complete cycles in one second, in hertz (Hz). One rotation of a simple coil is one cycle. "
              "The **period** $T$ is the time for one cycle.",
              title="Frequency and period", formula=r"f = \dfrac{1}{T}"),
            EX("Worked example 2: frequency from rotation", intro="A coil in a generator turns 25 times each second. Find the frequency and the period.", steps=[
                S("Frequency", math=r"f = 25 \text{ Hz}", text="Each rotation is one cycle."),
                S("Period", math=r"T = \dfrac{1}{f} = \dfrac{1}{25} = 0.04 \text{ s}"),
            ]),
            EX("Worked example 3: a turbine", intro="A hydroelectric turbine turns a generator at 3000 revolutions per minute. Find the frequency of the supply.", steps=[
                S("Change to revolutions per second", math=r"\dfrac{3000}{60} = 50 \text{ rev/s}"),
                S("Frequency", math=r"f = 50 \text{ Hz}", text="This is the frequency of the mains supply."),
            ]),
            MISTAKE("Thinking a stationary magnet in a coil induces a current",
                    "There must be a change. A magnet at rest, even inside the coil, induces no emf."),
            MISTAKE("Saying the emf is greatest when the coil is perpendicular to the field",
                    "The emf is greatest when the coil is parallel to the field, because the sides then cut the field lines fastest. It is zero when the coil is perpendicular to the field."),
            QUIZ("A magnet is held still inside a coil connected to a galvanometer. What does the galvanometer show?",
                 ["A steady deflection", "A deflection that increases", "Zero", "A deflection that alternates"], 2,
                 "No relative motion means no change of field, so there is no induced emf.",
                 hint="What must be changing for an emf to be induced?",
                 feedback=["A steady deflection would need a constant emf, but there is no change.", "The emf depends on the rate of change, which is zero.", "",
                           "Alternating deflections need continuous motion in and out."]),
            QUIZ("Which change would NOT increase the emf produced by a generator?",
                 ["Turning the coil faster", "Using a stronger magnet", "Using more turns on the coil", "Using thinner connecting wires"], 3,
                 "The emf depends on speed, field strength and number of turns, not on the thickness of the connecting wires.",
                 hint="Faraday's law lists speed, field strength and turns.",
                 feedback=["Faster turning cuts field lines faster, so the emf is larger.", "A stronger field gives a larger emf.", "More turns give a larger emf.", ""]),
            TIP("**Exam link.** Induction appears in Paper 1 multiple choice (what changes the emf, direction by Lenz's law, the output graph) and in Paper 2 descriptions of generators. "
                "When you state Faraday's and Lenz's laws, use the exact ideas: rate of cutting of field lines, and opposes the change.",
                title="Where this appears"),
            PQ("State Faraday's law and Lenz's law.",
               "Faraday's law: the induced emf is proportional to the rate at which the conductor cuts magnetic field lines (rate of change of flux linkage). "
               "Lenz's law: the induced current flows in a direction such that it opposes the change that produces it."),
            PQ("Describe how an a.c. generator produces an alternating emf. Name the parts that carry the current out.",
               "A coil turns in a magnetic field, so its sides cut the field lines and an emf is induced. Each half turn the sides swap places, so the emf reverses. "
               "Slip rings and carbon brushes carry the current to the outside circuit."),
            PQ("A generator makes 50 complete cycles each second. State its frequency and calculate its period.",
               r"$f = 50 \text{ Hz}$. $T = 1/f = 1/50 = 0.02 \text{ s}$."),
            PQ("State two ways to increase the emf of a generator.",
               "Turn the coil faster, use a stronger magnet or use more turns on the coil."),
            SUM("An emf is induced when a conductor cuts magnetic field lines or the field through a coil changes.",
                "Faraday's law: the emf is proportional to the rate of cutting of field lines. It is larger with more speed, a stronger field and more turns.",
                "Lenz's law: the induced current opposes the change that causes it. This is conservation of energy.",
                "An a.c. generator uses a coil, magnets, slip rings and brushes. The emf is zero when the coil is perpendicular to the field and greatest when it is parallel.",
                r"Frequency $f = 1/T$. A coil turning 50 times a second gives 50 Hz."),
        ],
    ),
    # ------------------------------------------------------------------ 5. Transformers
    lesson(
        module=M_EM, topic="Electromagnetic induction and transformers",
        title="Transformers and the transmission of electricity",
        slug="phd-transformers-transmission",
        minutes=24,
        summary="A transformer changes an a.c. voltage using two coils on a soft-iron core: Vs/Vp = Ns/Np. Power in equals power out for an ideal "
                "transformer, and high-voltage transmission lowers the power lost in cables.",
        objectives=[
            "Describe the structure and action of a transformer and explain why it needs a.c.",
            "Use Vs/Vp = Ns/Np to find voltages and numbers of turns",
            "Use VpIp = VsIs for an ideal transformer and calculate the efficiency of a real one",
            "Explain why electricity is transmitted at a high voltage and why a core is laminated",
        ],
        key_concepts=["Transformer", "Primary and secondary coil", "Step-up and step-down", "Turns ratio", "Efficiency", "Laminated core", "Power loss in cables"],
        blocks=[
            H("Introduction"),
            T("Your phone charger plugs into a 220 V socket and delivers about 5 V to the phone. Inside the charger is a small transformer. "
              "On the pylons that cross the countryside from a dam to a city, the voltage is many thousands of volts. "
              "A **transformer** is the device that changes an alternating voltage from one value to another."),
            H("How a transformer works"),
            IMG("f5ph-d-transformer.svg",
                alt="A laminated soft-iron core in a rectangle with a primary coil on the left leg connected to an a.c. input and a secondary coil on the right leg connected to the output.",
                caption="Figure 1. A transformer has a primary coil, a secondary coil and a laminated soft-iron core."),
            D("A **transformer** has two coils, the **primary** (input) and the **secondary** (output), wound on a **laminated soft-iron core**. "
              "An alternating current in the primary makes an alternating magnetic flux in the core. This changing flux passes through the secondary and induces an alternating emf in it.",
              title="Transformer"),
            KEY("A transformer works only with a.c.",
                "A direct current gives a steady flux. A steady flux does not change, so no emf is induced in the secondary. "
                "With a battery (d.c.) the secondary voltage is zero, apart from a brief flick when the circuit is switched on or off.",
                cards=[["a.c. in the primary", "Changing flux in the core, so an emf is induced in the secondary."],
                       ["d.c. in the primary", "Steady flux, so no emf is induced in the secondary."]]),
            D("The voltages are in the same ratio as the numbers of turns. $V_p$ and $N_p$ are the voltage and turns of the primary; $V_s$ and $N_s$ are those of the secondary.",
              title="The transformer equation", formula=r"\dfrac{V_s}{V_p} = \dfrac{N_s}{N_p}"),
            T("A **step-up** transformer has more turns on the secondary than on the primary ($N_s > N_p$), so it raises the voltage. "
              "A **step-down** transformer has fewer turns on the secondary ($N_s < N_p$), so it lowers the voltage."),
            EX("Worked example 1: a step-down transformer", intro="A phone-charger transformer has 1100 turns on the primary and 60 turns on the secondary. The primary is connected to 220 V a.c. Find the secondary voltage.", steps=[
                S("Write the equation", math=r"\dfrac{V_s}{V_p} = \dfrac{N_s}{N_p}"),
                S("Rearrange", math=r"V_s = V_p \times \dfrac{N_s}{N_p}"),
                S("Substitute", math=r"V_s = 220 \times \dfrac{60}{1100}"),
                S("Answer", math=r"V_s = 12 \text{ V}", text="The secondary voltage is lower than the primary, so it is a step-down transformer."),
            ]),
            EX("Worked example 2: a step-up transformer", intro="A transformer has 100 turns on the primary. It changes 12 V a.c. into 240 V a.c. How many turns are there on the secondary?", steps=[
                S("Rearrange", math=r"N_s = N_p \times \dfrac{V_s}{V_p}"),
                S("Substitute", math=r"N_s = 100 \times \dfrac{240}{12}"),
                S("Answer", math=r"N_s = 2000 \text{ turns}"),
            ]),
            H("Power and efficiency"),
            D("An **ideal transformer** has no energy loss, so the power out equals the power in. Power is voltage multiplied by current.",
              title="Ideal transformer", formula=r"V_p I_p = V_s I_s"),
            D("A real transformer wastes some energy as heat. Its **efficiency** is the useful power out divided by the power in, as a percentage.",
              title="Efficiency", formula=r"\text{efficiency} = \dfrac{V_s I_s}{V_p I_p} \times 100\%"),
            T("When the voltage goes up in a step-up transformer, the current goes **down** by the same ratio, so no energy is created. "
              "Energy is lost in a real transformer in four ways. (1) The coil wires have resistance and heat up. (2) Eddy currents are induced in the core. "
              "(3) The core is magnetized and demagnetized again and again, which heats it. (4) Some flux does not pass through the secondary coil (leakage). "
              "The core is made of thin **laminations** (layers of soft iron, insulated from each other) to cut the eddy currents."),
            EX("Worked example 3: the current of an ideal transformer", intro="An ideal transformer has 220 V across the primary. The secondary gives 12 V and 2.0 A. Find the current in the primary.", steps=[
                S("Power out", math=r"V_s I_s = 12 \times 2.0 = 24 \text{ W}"),
                S("Ideal, so power in equals power out", math=r"V_p I_p = 24 \text{ W}"),
                S("Primary current", math=r"I_p = \dfrac{24}{220} = 0.109 \text{ A} \approx 0.11 \text{ A}"),
            ]),
            EX("Worked example 4: efficiency", intro="A real transformer takes 0.12 A from the 220 V supply and gives 2.0 A at 12 V. Find its efficiency.", steps=[
                S("Power in", math=r"220 \times 0.12 = 26.4 \text{ W}"),
                S("Power out", math=r"12 \times 2.0 = 24 \text{ W}"),
                S("Efficiency", math=r"\dfrac{24}{26.4} \times 100\% = 90.9\% \approx 91\%"),
            ]),
            H("Why we transmit at high voltage"),
            T("Power stations are far from towns. The power $P = VI$ is sent along cables that have resistance $R$. The power lost as heat in the cables is $I^2 R$. "
              "If the voltage is raised, the same power is carried with a smaller current, and the loss falls with the **square** of the current."),
            EX("Worked example 5: loss in the cables", intro="A power station sends 2.2 MW (2 200 000 W) along cables of total resistance 2.0 ohm. Compare the power lost when it is sent at 11 000 V and at 110 000 V.", steps=[
                S("Current at 11 000 V", math=r"I = \dfrac{P}{V} = \dfrac{2\,200\,000}{11\,000} = 200 \text{ A}"),
                S("Loss at 11 000 V", math=r"I^2 R = 200^2 \times 2.0 = 80\,000 \text{ W}"),
                S("Current at 110 000 V", math=r"I = \dfrac{2\,200\,000}{110\,000} = 20 \text{ A}"),
                S("Loss at 110 000 V", math=r"I^2 R = 20^2 \times 2.0 = 800 \text{ W}", text="The voltage is 10 times higher, the current is 10 times smaller, and the loss is 100 times smaller."),
            ]),
            T("So step-up transformers raise the voltage at the power station, and step-down transformers lower it again near homes. "
              "That is why the grid uses a.c. A transformer cannot work with d.c."),
            MISTAKE("Using a transformer with a battery",
                    "A battery gives d.c. The flux does not change, so the secondary voltage is zero. A transformer needs a.c."),
            MISTAKE("Turning the ratio upside down",
                    "The secondary is on top: Vs/Vp = Ns/Np. A step-up transformer has more turns on the secondary. Check that your answer makes sense."),
            MISTAKE("Thinking a step-up transformer gives extra power",
                    "A higher voltage means a lower current. The power out cannot be greater than the power in."),
            QUIZ("A transformer has 500 turns on the primary and 100 turns on the secondary. Which statement is correct?",
                 ["It is a step-up transformer", "It is a step-down transformer and the secondary voltage is smaller", "It works with d.c.", "The secondary current is smaller than the primary current"], 1,
                 "Ns is less than Np, so the voltage is stepped down. The current in the secondary is larger for an ideal transformer.",
                 hint="Compare Ns and Np.",
                 feedback=["A step-up transformer has more turns on the secondary.", "", "A transformer does not work with d.c.", "With a lower voltage the secondary current is larger."]),
            QUIZ("Why is the core of a transformer made of thin insulated sheets of soft iron?",
                 ["To make it lighter", "To reduce eddy currents and heating", "To make the secondary voltage higher", "To allow d.c. to be used"], 1,
                 "Laminations make it hard for eddy currents to flow, so less energy is wasted as heat.",
                 hint="What do the sheets stop in the core?",
                 feedback=["Weight is not the reason.", "", "The turns ratio decides the voltage.", "A transformer never works with d.c."]),
            TIP("**Exam link.** Transformers appear in Paper 1 multiple choice and in Paper 2 calculations. The Board has noted that candidates fail to explain why a transformer does not work with d.c.: "
                "say that d.c. gives no changing magnetic flux, so no emf is induced in the secondary coil.",
                title="Where this appears"),
            PQ("A transformer has 2000 turns on the primary and 100 turns on the secondary. The primary voltage is 240 V a.c. Calculate the secondary voltage.",
               r"$V_s = V_p \times N_s/N_p = 240 \times 100/2000 = 12 \text{ V}$."),
            PQ("A transformer supplies 6.0 V and 3.0 A. It takes 0.10 A from a 220 V supply. Calculate the efficiency.",
               r"Power out $= 6.0 \times 3.0 = 18 \text{ W}$. Power in $= 220 \times 0.10 = 22 \text{ W}$. Efficiency $= 18/22 \times 100 = 81.8\% \approx 82\%$."),
            PQ("Explain why electrical power is transmitted at a very high voltage.",
               "For the same power, a higher voltage means a smaller current (I = P/V). The power lost in the cables is I squared times R, so a smaller current means much less power lost as heat."),
            PQ("Give two reasons why a real transformer is not 100% efficient.",
               "The resistance of the coils makes heat; eddy currents in the core make heat; the core's repeated magnetization wastes energy; some flux leaks (any two)."),
            SUM("A transformer has a primary coil, a secondary coil and a laminated soft-iron core. It works only with a.c.",
                r"$V_s/V_p = N_s/N_p$. More turns on the secondary: step-up. Fewer: step-down.",
                r"For an ideal transformer $V_p I_p = V_s I_s$. Efficiency $= (V_s I_s)/(V_p I_p) \times 100\%$.",
                "Losses: coil resistance, eddy currents, magnetizing the core and leakage of flux.",
                r"Transmission at high voltage means a small current, so the loss $I^2R$ in the cables is small."),
        ],
    ),
    # ------------------------------------------------------------------ 6. Atoms
    lesson(
        module=M_AT, topic="Atomic structure, nuclides and isotopes",
        title="Atomic structure, nuclide notation and isotopes",
        slug="phd-atomic-structure-nuclides-isotopes",
        minutes=22,
        summary="Atoms have a tiny dense nucleus of protons and neutrons with electrons around it. Atomic number Z, mass number A and nuclide "
                "notation tell you the particles, and isotopes are atoms of one element with different numbers of neutrons.",
        objectives=[
            "Describe the nuclear model of the atom and the charge and relative mass of the proton, neutron and electron",
            "Define atomic number, mass number and nucleon number and find the numbers of protons, neutrons and electrons",
            "Write and read nuclide notation",
            "Define isotopes and state how isotopes of one element are alike and different",
        ],
        key_concepts=["Nucleus", "Proton", "Neutron", "Electron", "Atomic number", "Mass number", "Nuclide", "Isotope"],
        blocks=[
            H("Introduction"),
            T("Everything in a market in Mokolo is made of atoms: the cloth, the water, the iron of a cooking pot. "
              "Atoms are so small that you cannot see them, but physicists have built a clear picture of what is inside. "
              "This picture is the base of radioactivity, nuclear power and electronics, so we start here."),
            H("The nuclear model"),
            T("In the early 1900s, physicists fired alpha particles (small, fast, positive particles) at a very thin sheet of gold foil. "
              "Most alpha particles went straight through. A few were deflected through large angles, and a very few bounced almost straight back. "
              "From this, Rutherford's team concluded that an atom is mostly empty space, with its positive charge and almost all its mass in a tiny, dense **nucleus**. "
              "The atom is about 100 000 times wider than its nucleus."),
            D("The **nucleus** is at the centre of the atom and contains **protons** and **neutrons**, which are together called **nucleons**. "
              "**Electrons** move around the nucleus. A neutral atom has equal numbers of protons and electrons.",
              title="Structure of the atom"),
            CODE("Particle    Relative charge    Relative mass\nProton           +1                1\nNeutron           0                1\nElectron         -1             1/1840 (very small)",
                 "text", title="Particles of the atom"),
            T("The mass of an electron is so small compared with the proton that the mass of an atom is almost all in the nucleus. "
              "Some books give the relative mass of the electron as 1/1836 or 1/2000: check your textbook, but remember that it is very small."),
            H("Atomic number, mass number and nuclide notation"),
            D("The **atomic number** $Z$ (proton number) is the number of protons in the nucleus. It decides which element the atom is. "
              "The **mass number** $A$ (nucleon number) is the total number of protons and neutrons in the nucleus.",
              title="Atomic number and mass number"),
            F(r"N = A - Z", title="Number of neutrons"),
            D(r"A **nuclide** is a particular kind of nucleus with a given number of protons and neutrons. It is written ${}^{A}_{Z}\text{X}$, where X is the chemical symbol, $A$ the mass number (top) and $Z$ the atomic number (bottom).",
              title="Nuclide notation"),
            EX("Worked example 1: carbon", intro=r"Carbon-12 is written ${}^{12}_{6}\text{C}$. State the numbers of protons, neutrons and electrons in a neutral atom.", steps=[
                S("Protons", math=r"Z = 6", text="Six protons."),
                S("Neutrons", math=r"N = A - Z = 12 - 6 = 6"),
                S("Electrons", text="A neutral atom has as many electrons as protons: 6."),
            ]),
            EX("Worked example 2: uranium", intro=r"Uranium-235 is ${}^{235}_{92}\text{U}$. Find the numbers of protons and neutrons.", steps=[
                S("Protons", math=r"Z = 92"),
                S("Neutrons", math=r"N = 235 - 92 = 143"),
            ]),
            H("Isotopes"),
            D("**Isotopes** are atoms of the same element (the same atomic number $Z$) that have **different numbers of neutrons**, so they have different mass numbers.",
              title="Isotopes"),
            T(r"Chlorine has two common isotopes, ${}^{35}_{17}\text{Cl}$ and ${}^{37}_{17}\text{Cl}$. Both have 17 protons and 17 electrons. "
              r"Chlorine-35 has 18 neutrons and chlorine-37 has 20. Carbon has isotopes ${}^{12}_{6}\text{C}$, ${}^{13}_{6}\text{C}$ and ${}^{14}_{6}\text{C}$."),
            KEY("Alike and different",
                "Isotopes of an element have the same number of electrons, so they have the same chemical properties. "
                "They have different numbers of neutrons, so they have different masses, and some isotopes are unstable (radioactive).",
                cards=[["Same", "Number of protons and electrons; chemical properties."],
                       ["Different", "Number of neutrons, mass number, mass and stability."]]),
            EX("Worked example 3: an ion", intro=r"An atom of magnesium ${}^{24}_{12}\text{Mg}$ loses two electrons to form an ion. How many protons, neutrons and electrons are in the ion?", steps=[
                S("Protons", text="The nucleus does not change: 12 protons."),
                S("Neutrons", math=r"24 - 12 = 12"),
                S("Electrons", text="12 - 2 = 10 electrons. The ion has a charge of 2+."),
            ]),
            MISTAKE("Confusing mass number with atomic number",
                    "The atomic number Z is the number of protons only. The mass number A counts protons and neutrons. N = A - Z."),
            MISTAKE("Saying that isotopes have different numbers of protons",
                    "Isotopes of one element have the same number of protons. Only the number of neutrons is different."),
            MISTAKE("Changing the number of protons when forming an ion",
                    "Ions form when electrons are gained or lost. The nucleus does not change."),
            QUIZ(r"How many neutrons are in ${}^{27}_{13}\text{Al}$?",
                 ["13", "14", "27", "40"], 1,
                 "N = A - Z = 27 - 13 = 14.",
                 hint="Subtract the bottom number from the top number.",
                 feedback=["13 is the number of protons.", "", "27 is the number of nucleons (protons plus neutrons).", "40 is A + Z, which has no meaning."]),
            QUIZ("Which pair are isotopes of the same element?",
                 [r"${}^{14}_{6}\text{X}$ and ${}^{14}_{7}\text{Y}$", r"${}^{35}_{17}\text{X}$ and ${}^{37}_{17}\text{Y}$", r"${}^{16}_{8}\text{X}$ and ${}^{17}_{9}\text{Y}$", r"${}^{23}_{11}\text{X}$ and ${}^{23}_{11}\text{Y}$"], 1,
                 "Isotopes have the same Z (17) and different A (35 and 37).",
                 hint="Isotopes: same proton number, different mass number.",
                 feedback=["The mass numbers are the same but the proton numbers differ, so they are different elements.", "",
                           "Both numbers differ, so they are different elements.", "These are identical nuclides, not different isotopes."]),
            TIP("**Exam link.** Atomic structure and isotopes appear in Paper 1 multiple choice (counting particles, nuclide notation, isotopes) and in Paper 2 short questions. "
                "State definitions precisely: isotopes have the same proton number but different neutron numbers.",
                title="Where this appears"),
            PQ(r"State the numbers of protons, neutrons and electrons in a neutral atom of ${}^{56}_{26}\text{Fe}$.",
               "Protons = 26, neutrons = 56 - 26 = 30, electrons = 26."),
            PQ("Define isotopes and give one example.",
               r"Isotopes are atoms of the same element with the same number of protons but different numbers of neutrons. Example: ${}^{12}_{6}\text{C}$ and ${}^{14}_{6}\text{C}$."),
            PQ("Explain why isotopes of an element have the same chemical properties but different masses.",
               "Chemical properties depend on the number of electrons, which equals the number of protons and is the same for all isotopes. The masses differ because the numbers of neutrons are different."),
            PQ("Describe what the alpha-scattering experiment showed about the atom.",
               "Most alpha particles went straight through, so an atom is mostly empty space. A few were deflected strongly and very few bounced back, so the positive charge and most of the mass are in a tiny, dense nucleus."),
            SUM("An atom has a tiny dense nucleus of protons and neutrons, with electrons around it; most of the atom is empty space.",
                "Proton: +1, relative mass 1. Neutron: 0, relative mass 1. Electron: -1, very small mass.",
                r"Atomic number $Z$ = number of protons; mass number $A$ = protons + neutrons; neutrons $= A - Z$. Nuclide: ${}^{A}_{Z}\text{X}$.",
                "Isotopes have the same Z and different numbers of neutrons: same chemistry, different mass."),
        ],
    ),
    # ------------------------------------------------------------------ 7. Radioactivity
    lesson(
        module=M_AT, topic="Radioactivity",
        title="Alpha, beta and gamma radiation",
        slug="phd-radioactivity-alpha-beta-gamma",
        minutes=24,
        summary="Unstable nuclei emit alpha, beta and gamma radiation at random. The three differ in nature, charge, ionising power and penetration. "
                "Background radiation, detection, uses and safety rules complete the topic.",
        objectives=[
            "Define radioactivity and state that decay is random and spontaneous",
            "Describe the nature, charge, penetration and ionising effect of alpha, beta and gamma radiation",
            "Explain how the radiations behave in electric and magnetic fields and how they are detected",
            "State uses of radioactive materials, sources of background radiation and safety precautions",
        ],
        key_concepts=["Radioactivity", "Alpha particle", "Beta particle", "Gamma ray", "Ionisation", "Background radiation", "Geiger-Muller tube"],
        blocks=[
            H("Introduction"),
            T("In hospitals, X-ray and cancer treatment machines use radiation. A smoke detector in a hotel corridor contains a tiny radioactive source. "
              "Rocks and the soil around us are slightly radioactive too. Radiation can help us and, if misused, can harm us. "
              "We must know what the radiations are, and how to stay safe."),
            D("**Radioactivity** is the spontaneous and random emission of radiation (alpha, beta or gamma) from the nuclei of unstable atoms. "
              "The unstable nucleus changes into a different nucleus, or into a more stable state, and this is called **radioactive decay**.",
              title="Radioactivity"),
            T("**Spontaneous** means that decay is not caused by heat, pressure or chemical changes. **Random** means that we cannot tell when a particular nucleus will decay, "
              "although we can predict the behaviour of a large number of nuclei."),
            H("The three radiations"),
            CODE("Radiation  Nature                    Charge  Stopped by            Ionising\nAlpha      helium nucleus (2p + 2n)    +2    paper, skin, 5 cm air  strongest\nBeta       fast electron               -1    few mm of aluminium    medium\nGamma      high-energy EM wave          0    thick lead, concrete   weakest",
                 "text", title="Properties of the radiations"),
            T("Ranges depend on the energy of the radiation and books give slightly different values: check your textbook. "
              "Alpha particles have a short range in air (a few centimetres). Beta particles travel further (up to a metre or more). Gamma rays travel very far and are only reduced, never fully stopped, by thick lead."),
            IMG("f5ph-d-radiation-penetration.svg",
                alt="Three arrows from a source: alpha stopped by a sheet of paper, beta stopped by aluminium, and gamma rays passing through paper and aluminium and mostly absorbed by thick lead.",
                caption="Figure 1. Alpha is stopped by paper, beta by a few millimetres of aluminium; thick lead strongly reduces gamma."),
            D("**Ionisation** is the removal of electrons from atoms, which makes charged ions. Alpha particles ionise most strongly because they are heavy and carry a +2 charge; "
              "they lose their energy quickly, so they have the shortest range. Gamma rays ionise least, so they penetrate furthest.",
              title="Ionising effect"),
            KEY("Fields",
                "Alpha particles are positive, so they bend towards the negative plate, but only a little because they are heavy. "
                "Beta particles are negative, so they bend towards the positive plate, and much more because they are very light. "
                "Gamma rays have no charge and are not deflected.",
                cards=[["Alpha", "Deflected a little, towards the negative plate."],
                       ["Beta", "Deflected a lot, towards the positive plate."],
                       ["Gamma", "Not deflected."]]),
            H("Detection and background radiation"),
            T("A **Geiger-Muller (GM) tube** with a counter detects radiation: each particle entering the tube causes a pulse, which is counted. "
              "A **cloud chamber** shows tracks of particles, and **photographic film** is blackened by radiation (a film badge). "
              "A **ratemeter** or counter shows the count rate in counts per second or per minute."),
            D("**Background radiation** is the radiation always present around us. It comes from natural sources such as rocks and soil, radon gas, cosmic rays from space and food, "
              "and a small part from man-made sources such as medical X-rays. Before you measure a source, measure the background count rate with the source far away, "
              "and subtract it from your readings to get the **corrected count rate**.",
              title="Background radiation"),
            EX("Worked example 1: which radiation is it?", intro="A source gives a count rate of 520 counts per minute. With the background at 20 counts per minute, the readings with absorbers are: paper 518, 3 mm of aluminium 270, 5 cm of lead 22. Which radiations does the source emit?", steps=[
                S("Correct for background", text="Subtract 20 from each reading: no absorber 500, paper 498, aluminium 250, lead 2."),
                S("Paper", text="The paper hardly changes the count (500 to 498), so there is no alpha radiation."),
                S("Aluminium", text="The count falls from 498 to 250, so about half of the radiation is stopped by a few mm of aluminium: beta radiation."),
                S("Lead", text="Lead nearly removes the rest (2), so the remainder is gamma radiation. The source emits beta and gamma."),
            ]),
            EX("Worked example 2: a field", intro="Three radiations pass between two charged plates. Radiation X bends strongly towards the positive plate, Y bends slightly towards the negative plate and Z goes straight. Name X, Y and Z.", steps=[
                S("X", text="It bends strongly to the positive plate, so it is negative and light: beta."),
                S("Y", text="It bends slightly to the negative plate, so it is positive and heavy: alpha."),
                S("Z", text="It has no charge: gamma."),
            ]),
            H("Uses and safety"),
            T("**Uses.** Smoke detectors use a weak alpha source: smoke reduces the ionisation current and sets off the alarm. "
              "A beta source gives the thickness of paper or metal sheet: more thickness, fewer betas pass through. "
              "Gamma rays sterilise medical tools and food and treat cancer. A tracer with a short half-life shows the flow of fluids in the body or in pipes."),
            T("**Safety.** Handle sources with long tongs and never touch them. Keep them in lead-lined boxes. Keep the time of exposure short and keep the distance large. "
              "Workers wear film badges to measure how much radiation they receive. Dispose of radioactive waste safely."),
            MISTAKE("Saying gamma is stopped by lead",
                    "Thick lead strongly reduces gamma rays but never stops them completely. Say reduced or absorbed, not stopped."),
            MISTAKE("Forgetting the background count",
                    "Always subtract the background count rate from your reading to find the count rate from the source itself."),
            QUIZ("Which radiation is a stream of electrons from the nucleus?",
                 ["Alpha", "Beta", "Gamma", "X-rays from the electron shells"], 1,
                 "A beta particle is a fast electron that comes from the nucleus.",
                 hint="Which radiation has charge -1 and a very small mass?",
                 feedback=["Alpha particles are helium nuclei.", "", "Gamma rays are electromagnetic waves.", "X-rays are not emitted by the nucleus; beta particles are."]),
            QUIZ("Which radiation is the most strongly ionising?",
                 ["Alpha", "Beta", "Gamma", "All three equally"], 0,
                 "Alpha particles are heavy and carry a +2 charge, so they ionise most strongly.",
                 hint="The most ionising radiation has the shortest range.",
                 feedback=["", "Beta ionises less than alpha.", "Gamma ionises least.", "Their ionising effects are very different."]),
            TIP("**Exam link.** Radioactivity is a favourite for Paper 1 multiple choice (properties table, deflection, absorbers, uses) and appears in Paper 2 structured questions. "
                "Learn the table of the three radiations and always mention background correction.",
                title="Where this appears"),
            PQ("State the nature, charge and one use of each of alpha, beta and gamma radiation.",
               "Alpha: helium nucleus, charge +2, use in smoke detectors. Beta: fast electron, charge -1, use in thickness gauges. Gamma: electromagnetic wave, no charge, use in sterilising tools or treating cancer."),
            PQ("A source gives 340 counts per minute. The background is 40 counts per minute. What is the corrected count rate?",
               "Corrected count rate = 340 - 40 = 300 counts per minute."),
            PQ("List four safety precautions for handling a radioactive source in a school laboratory.",
               "Use tongs and never touch the source; keep it in a lead-lined container when not in use; keep exposure time short and keep your distance; never point it at anyone or put it near your face."),
            PQ("Explain why alpha particles have a shorter range in air than gamma rays.",
               "Alpha particles are heavy with a +2 charge, so they ionise very strongly and lose their energy in a few centimetres. Gamma rays have no charge and ionise weakly, so they travel much further."),
            SUM("Radioactivity is the spontaneous and random emission of radiation from unstable nuclei.",
                "Alpha: helium nucleus (+2), stopped by paper. Beta: fast electron (-1), stopped by a few mm of aluminium. Gamma: electromagnetic wave (0), strongly reduced by thick lead.",
                "Alpha ionises most; gamma least. In fields: beta deflects a lot, alpha a little in the opposite way, gamma not at all.",
                "A GM tube and counter detect radiation. Subtract the background count rate to find the corrected rate.",
                "Uses: smoke detectors, thickness gauges, sterilising and cancer treatment, tracers. Safety: tongs, lead boxes, short time, large distance."),
        ],
    ),
]

LESSONS += [
    # ------------------------------------------------------------------ 8. Decay and half-life
    lesson(
        module=M_AT, topic="Radioactive decay and half-life",
        title="Decay equations, half-life and carbon dating",
        slug="phd-decay-equations-half-life",
        minutes=25,
        summary="Alpha and beta decay change A and Z by fixed rules. The half-life is the time for the activity, or the number of undecayed nuclei, "
                "to fall to half; it is used to calculate what remains and to date old objects with carbon-14.",
        objectives=[
            "Write and balance nuclear decay equations for alpha, beta and gamma emission",
            "Define half-life and use it to calculate the fraction or amount left after a given time",
            "Find a half-life from a table or from a decay graph",
            "Explain how carbon-14 is used to date organic remains",
        ],
        key_concepts=["Decay equation", "Alpha decay", "Beta decay", "Half-life", "Activity", "Count rate", "Carbon dating"],
        blocks=[
            H("Introduction"),
            T("A doctor in Yaounde gives a patient a tracer made from a radioactive material that loses half its activity every 6 hours. "
              "By the next day most of the radioactivity has gone, so the patient is safe, but the tracer lasted long enough to be seen on the scan. "
              "The time taken for the activity to halve is called the **half-life**. In this lesson you also learn how to write equations for radioactive decay."),
            H("Decay equations"),
            T("In a nuclear equation, the total of the mass numbers (top numbers) must be the same on both sides, and the total of the atomic numbers (bottom numbers) must be the same on both sides."),
            KEY("Rules for the three types of decay",
                "**Alpha decay:** the nucleus loses 2 protons and 2 neutrons, so $A$ decreases by 4 and $Z$ decreases by 2. "
                "**Beta decay:** a neutron changes into a proton and an electron (the beta particle), so $A$ stays the same and $Z$ increases by 1. "
                "**Gamma emission:** $A$ and $Z$ do not change; the nucleus gives out extra energy.",
                cards=[["Alpha", r"${}^{A}_{Z}\text{X} \to {}^{A-4}_{Z-2}\text{Y} + {}^{4}_{2}\text{He}$"],
                       ["Beta", r"${}^{A}_{Z}\text{X} \to {}^{A}_{Z+1}\text{Y} + {}^{0}_{-1}\text{e}$"],
                       ["Gamma", "No change in A or Z."]]),
            EX("Worked example 1: alpha decay", intro=r"Uranium-238 ${}^{238}_{92}\text{U}$ decays by emitting an alpha particle. Write the equation.", steps=[
                S("Daughter nucleus: mass number", math=r"238 - 4 = 234"),
                S("Daughter nucleus: atomic number", math=r"92 - 2 = 90", text="Element 90 is thorium (Th)."),
                S("Equation", math=r"{}^{238}_{92}\text{U} \to {}^{234}_{90}\text{Th} + {}^{4}_{2}\text{He}"),
            ], check=r"238 = 234 + 4, \quad 92 = 90 + 2"),
            EX("Worked example 2: beta decay", intro=r"Carbon-14 ${}^{14}_{6}\text{C}$ decays by beta emission. Write the equation.", steps=[
                S("Mass number", text="It does not change: 14."),
                S("Atomic number", math=r"6 + 1 = 7", text="Element 7 is nitrogen (N)."),
                S("Equation", math=r"{}^{14}_{6}\text{C} \to {}^{14}_{7}\text{N} + {}^{0}_{-1}\text{e}"),
            ], check=r"14 = 14 + 0, \quad 6 = 7 + (-1)"),
            EX("Worked example 3: find the missing nuclide", intro=r"${}^{214}_{83}\text{Bi}$ decays by beta emission to polonium (Po). Find the mass number and atomic number of the polonium.", steps=[
                S("Beta decay", text="The mass number stays at 214."),
                S("Atomic number", math=r"83 + 1 = 84"),
                S("Result", math=r"{}^{214}_{84}\text{Po}"),
            ]),
            H("Half-life"),
            D("The **half-life** of a radioactive substance is the time taken for the activity (or the count rate, or the number of radioactive nuclei) in a sample to fall to half of its original value.",
              title="Half-life"),
            IMG("f5ph-d-decay-curve.svg",
                alt="A decay curve starting at 1 and halving at every interval T: 1/2 at T, 1/4 at 2T and 1/8 at 3T.",
                caption="Figure 1. In every half-life T the activity falls to half of what it was at the start of that interval."),
            T("Half-life depends only on the substance (the nuclide). It does not change with temperature, pressure or chemical state. "
              "Half-lives range from a fraction of a second to billions of years."),
            D("After $n$ half-lives, the fraction that remains is:",
              title="Fraction remaining", formula=r"\left(\dfrac{1}{2}\right)^{n}, \qquad n = \dfrac{\text{time elapsed}}{\text{half-life}}"),
            CODE("Number of half-lives   0    1     2     3      4\nFraction remaining     1   1/2   1/4   1/8   1/16\nStarting at 800        800  400   200   100    50",
                 "text", title="Halving table"),
            EX("Worked example 4: counts left", intro="A sample has a corrected count rate of 640 counts per minute. After 12 hours it is 80 counts per minute. Find the half-life.", steps=[
                S("Fraction left", math=r"\dfrac{80}{640} = \dfrac{1}{8}"),
                S("Number of half-lives", math=r"\dfrac{1}{8} = \left(\dfrac{1}{2}\right)^3, \text{ so } n = 3"),
                S("Half-life", math=r"T_{1/2} = \dfrac{12}{3} = 4 \text{ hours}"),
            ]),
            EX("Worked example 5: mass left", intro="A sample has 160 g of a radioactive isotope with a half-life of 8 days. How much remains after 24 days?", steps=[
                S("Number of half-lives", math=r"n = \dfrac{24}{8} = 3"),
                S("Halve three times", math=r"160 \to 80 \to 40 \to 20"),
                S("Answer", math=r"20 \text{ g}"),
            ]),
            T("**From a graph.** On a decay curve, read the starting value, find half of it, go across to the curve and down to the time axis. "
              "That time is the half-life. Check with a second half: the time to fall from 1/2 to 1/4 should be the same."),
            H("Carbon dating"),
            T("Living plants and animals take in carbon dioxide and food that contain a small, constant fraction of radioactive **carbon-14**. "
              "The fraction stays the same while they live. When they die, no new carbon-14 is taken in, and the carbon-14 already present decays with a half-life of about 5700 years "
              "(some books give 5730 years). So the activity of a sample of wood, bone or charcoal gets smaller with time. "
              "By comparing it with the activity of a living sample, we can work out how old it is."),
            EX("Worked example 6: dating a charcoal sample", intro="A piece of charcoal from an old cooking fire has an activity one-quarter of that of the same mass of living wood. Use 5700 years for the half-life of carbon-14. How old is the charcoal?", steps=[
                S("Fraction left", text="One-quarter: $\\left(\\dfrac{1}{2}\\right)^2$, so $n = 2$ half-lives."),
                S("Age", math=r"2 \times 5700 = 11\,400 \text{ years}"),
            ]),
            MISTAKE("Dividing the amount by 2 only once",
                    "After 3 half-lives you halve three times (or divide by 8), not once. Find n = time / half-life first."),
            MISTAKE("Using the half-life as the time for all the activity to vanish",
                    "After two half-lives one quarter remains, not zero. The activity never reaches zero in theory."),
            MISTAKE("Defining half-life as half the time for decay",
                    "State it correctly: the time taken for the activity (or number of nuclei) to fall to half its original value."),
            QUIZ(r"Radium-226 ${}^{226}_{88}\text{Ra}$ emits an alpha particle. What are the mass number and atomic number of the new nucleus?",
                 ["222 and 86", "222 and 88", "226 and 89", "230 and 90"], 0,
                 "Alpha decay: A decreases by 4 (226 - 4 = 222) and Z decreases by 2 (88 - 2 = 86). This is radon.",
                 hint="Take 4 from A and 2 from Z.",
                 feedback=["", "The atomic number must also fall by 2.", "This is the result of beta decay for Z, but A is wrong.", "These numbers increased instead of decreasing."]),
            QUIZ("A sample has a half-life of 2 hours. What fraction of the original activity is left after 6 hours?",
                 ["1/2", "1/4", "1/6", "1/8"], 3,
                 "6 hours is 3 half-lives, and (1/2)^3 = 1/8.",
                 hint="First find the number of half-lives.",
                 feedback=["That is the fraction after only one half-life.", "That is the fraction after two half-lives.", "Dividing by 6 gives no halving rule.", ""]),
            TIP("**Exam link.** The Board has reported that candidates often fail to define half-life correctly. Decay equations and half-life calculations occur in Paper 1 multiple choice "
                "and in Paper 2 questions. Show n = time / half-life, then the halvings, and give the unit.",
                title="Where this appears"),
            PQ(r"Complete: ${}^{239}_{94}\text{Pu} \to {}^{A}_{Z}\text{U} + {}^{4}_{2}\text{He}$. State A and Z.",
               "A = 239 - 4 = 235 and Z = 94 - 2 = 92, so the nucleus is uranium-235."),
            PQ("A radioactive sample has an activity of 1200 counts per minute. Its half-life is 5 days. What is its activity after 15 days?",
               r"$n = 15/5 = 3$. Activity $= 1200/2^3 = 1200/8 = 150$ counts per minute."),
            PQ("Define half-life. A sample has a half-life of 30 years. How long will it take for 7/8 of the nuclei to decay?",
               "Half-life is the time taken for the activity (or number of radioactive nuclei) to fall to half its original value. If 7/8 have decayed, 1/8 remains, so three half-lives have passed: 3 x 30 = 90 years."),
            PQ("Explain how carbon-14 is used to find the age of an old wooden object.",
               "Living wood has a constant fraction of carbon-14. After death the carbon-14 decays with a half-life of about 5700 years. By measuring the activity of the wood and comparing it with living wood, we find how many half-lives have passed and so the age."),
            SUM("Alpha decay: A down 4, Z down 2. Beta decay: A same, Z up 1. Gamma: no change. Totals of A and Z balance.",
                "Half-life is the time for the activity (or number of nuclei) to fall to half its original value. It depends only on the nuclide.",
                r"After $n$ half-lives, the fraction left is $(1/2)^n$ with $n$ = time / half-life.",
                "Carbon dating compares the carbon-14 activity of old organic matter with that of living matter."),
        ],
    ),
    # ------------------------------------------------------------------ 9. Fission and fusion
    lesson(
        module=M_AT, topic="Nuclear fission and fusion",
        title="Nuclear fission, fusion and mass-energy equivalence",
        slug="phd-fission-fusion-mass-energy",
        minutes=22,
        summary="Fission splits a heavy nucleus and fusion joins light nuclei; both release energy because some mass disappears, with E = mc^2 "
                "(energy = mass lost x c squared). Reactors control the chain reaction.",
        objectives=[
            "Describe nuclear fission and the chain reaction, and how a reactor controls it",
            "Describe nuclear fusion and the conditions it needs",
            "Use E = mc^2 to calculate the energy released when mass is lost",
            "Balance fission and fusion equations by counting A and Z",
        ],
        key_concepts=["Nuclear fission", "Chain reaction", "Control rods", "Nuclear fusion", "Mass defect", "Mass-energy equivalence"],
        blocks=[
            H("Introduction"),
            T("The Sun has warmed the farms of Cameroon for millions of years, and it gets its energy from nuclear reactions. "
              "Some countries use nuclear reactors to make electricity, while Cameroon makes most of its electricity from water in dams such as Song Loulou. "
              "Nuclear reactions release enormous energy from very little matter. This lesson explains where that energy comes from."),
            H("Mass and energy"),
            D("Einstein showed that mass and energy are equivalent. When a system loses mass $\\Delta m$, it releases energy $E$, where $c$ is the speed of light, $c = 3.0 \\times 10^{8}$ m/s.",
              title="Mass-energy equivalence", formula=r"E = \Delta m \, c^{2}"),
            T("In nuclear reactions the total mass of the products is slightly smaller than the total mass before. The missing mass is the **mass defect** ($\\Delta m$), "
              "and it appears as energy, mostly as kinetic energy of the fragments and as gamma rays. "
              "Because $c^2 = 9.0 \\times 10^{16}$ m$^2$/s$^2$ is so large, a tiny mass gives a huge energy."),
            EX("Worked example 1: converting 1 gram", intro="How much energy would be released if 1.0 g of mass were completely converted into energy?", steps=[
                S("Convert to kilograms", math=r"\Delta m = 1.0 \text{ g} = 1.0 \times 10^{-3} \text{ kg}"),
                S("Substitute", math=r"E = 1.0 \times 10^{-3} \times (3.0 \times 10^{8})^2 = 1.0 \times 10^{-3} \times 9.0 \times 10^{16}"),
                S("Answer", math=r"E = 9.0 \times 10^{13} \text{ J}"),
            ]),
            H("Nuclear fission"),
            D("**Nuclear fission** is the splitting of a large nucleus, such as uranium-235, into two smaller nuclei (and 2 or 3 neutrons) when it absorbs a neutron. "
              "Energy is released.",
              title="Nuclear fission"),
            CODE("U-235 + n  ->  Ba-141 + Kr-92 + 3 n + energy\n\nMass number: 235 + 1 = 236   141 + 92 + 3 = 236\nAtomic number:     92       56 + 36 = 92", "text", title="A fission equation"),
            T(r"In symbols: ${}^{235}_{92}\text{U} + {}^{1}_{0}\text{n} \to {}^{141}_{56}\text{Ba} + {}^{92}_{36}\text{Kr} + 3\,{}^{1}_{0}\text{n} + \text{energy}$."),
            D("The neutrons released can split more nuclei, which release more neutrons, and so on. This is a **chain reaction**. If it is not controlled, it grows very fast, "
              "as in a bomb. In a reactor it is **controlled**, so that on average one neutron from each fission causes one more fission.",
              title="Chain reaction"),
            KEY("Parts of a nuclear reactor",
                "Fuel rods of uranium give the energy. **Control rods** (boron or cadmium) absorb neutrons: pushed in they slow or stop the reaction, pulled out they speed it up. "
                "The **moderator** (graphite or water) slows the neutrons so that they are more likely to cause fission. The **coolant** carries heat away to make steam for the turbines. "
                "Thick concrete shields people from the radiation.",
                cards=[["Control rods", "Absorb neutrons to control the rate."],
                       ["Moderator", "Slows neutrons down."],
                       ["Coolant", "Carries heat to a boiler to make steam."],
                       ["Shielding", "Concrete and steel absorb radiation."]]),
            H("Nuclear fusion"),
            D("**Nuclear fusion** is the joining of two light nuclei to make a heavier nucleus, with the release of energy. "
              "It needs a very high temperature (millions of degrees) and a very high pressure, so that the positive nuclei can overcome their repulsion and come close together.",
              title="Nuclear fusion"),
            CODE("H-2 + H-3  ->  He-4 + n + energy\n\nMass number: 2 + 3 = 5        4 + 1 = 5\nAtomic number: 1 + 1 = 2      2 + 0 = 2", "text", title="A fusion equation"),
            T("Fusion is the source of energy in the Sun and other stars, where hydrogen nuclei fuse into helium. "
              "Scientists are trying to build fusion reactors on Earth, because fusion uses abundant fuel and gives less long-lived waste, but it is very hard to keep matter so hot."),
            CODE("             Fission                    Fusion\nStarts with   one heavy nucleus          two light nuclei\nResult        two medium nuclei + n      one heavier nucleus\nConditions    neutron needed             very high temperature\nExample       reactors, bombs            the Sun", "text", title="Comparing the two"),
            EX("Worked example 2: a reactor's mass loss", intro=r"A reactor produces 900 MW ($9.0 \times 10^{8}$ J every second). How much mass is converted into energy each second? Use $c = 3.0 \times 10^{8}$ m/s.", steps=[
                S("Energy per second", math=r"E = 9.0 \times 10^{8} \text{ J}"),
                S("Rearrange", math=r"\Delta m = \dfrac{E}{c^2}"),
                S("Substitute", math=r"\Delta m = \dfrac{9.0 \times 10^{8}}{9.0 \times 10^{16}}"),
                S("Answer", math=r"\Delta m = 1.0 \times 10^{-8} \text{ kg each second}"),
            ]),
            EX("Worked example 3: energy from one fission", intro=r"In one fission the total mass falls by $3.6 \times 10^{-28}$ kg. Calculate the energy released.", steps=[
                S("Substitute", math=r"E = \Delta m \, c^2 = 3.6 \times 10^{-28} \times 9.0 \times 10^{16}"),
                S("Answer", math=r"E = 3.24 \times 10^{-11} \text{ J} \approx 3.2 \times 10^{-11} \text{ J}"),
            ]),
            MISTAKE("Using grams in E = mc squared",
                    "Convert the mass to kilograms first, because c is in m/s and the energy is then in joules."),
            MISTAKE("Mixing up fission and fusion",
                    "Fission splits one heavy nucleus. Fusion joins light nuclei. Fission needs a neutron; fusion needs a very high temperature."),
            QUIZ("Which statement about a nuclear reactor is correct?",
                 ["Control rods slow the neutrons down", "Control rods absorb neutrons to control the chain reaction", "The moderator absorbs neutrons", "The coolant starts the chain reaction"], 1,
                 "Control rods (boron or cadmium) absorb neutrons and so control the rate of fission.",
                 hint="Which part controls the rate?",
                 feedback=["The moderator slows the neutrons.", "", "The moderator slows neutrons down; it does not absorb them.", "The coolant carries heat away."]),
            QUIZ(r"A mass defect of $2.0 \times 10^{-30}$ kg releases how much energy? ($c = 3.0 \times 10^{8}$ m/s)",
                 [r"$6.0 \times 10^{-22}$ J", r"$1.8 \times 10^{-13}$ J", r"$1.8 \times 10^{-46}$ J", r"$6.0 \times 10^{-38}$ J"], 1,
                 r"$E = 2.0 \times 10^{-30} \times 9.0 \times 10^{16} = 1.8 \times 10^{-13}$ J.",
                 hint="E = mass x c squared.",
                 feedback=["That comes from multiplying by c only, not by c squared.", "", "This results from dividing by c squared.", "This results from dividing by c."]),
            TIP("**Exam link.** Fission, fusion and E = mc squared appear in Paper 1 multiple choice and in Paper 2. Show the conversion to kilograms and give the unit (J).",
                title="Where this appears"),
            PQ("Describe a chain reaction in a nuclear reactor and say how it is controlled.",
               "A neutron splits a uranium-235 nucleus, which releases 2 or 3 neutrons. These split other nuclei, so the reaction continues. Control rods of boron or cadmium absorb neutrons so that, on average, only one neutron per fission causes another fission."),
            PQ("State two differences between nuclear fission and nuclear fusion.",
               "Fission splits a heavy nucleus into smaller ones and needs a neutron; fusion joins light nuclei into a heavier one and needs a very high temperature and pressure. Fission is used in reactors; fusion powers the Sun."),
            PQ(r"A reaction loses a mass of $2.0 \times 10^{-29}$ kg. Calculate the energy released. ($c = 3.0 \times 10^8$ m/s.)",
               r"$E = \Delta m c^2 = 2.0 \times 10^{-29} \times 9.0 \times 10^{16} = 1.8 \times 10^{-12} \text{ J}$."),
            PQ(r"Complete: ${}^{235}_{92}\text{U} + {}^{1}_{0}\text{n} \to {}^{141}_{56}\text{Ba} + {}^{X}_{36}\text{Kr} + 3\,{}^{1}_{0}\text{n}$. Find X.",
               "Mass number: 235 + 1 = 236 on the left, and 141 + X + 3 = 236 gives X = 92."),
            SUM("E = mc squared: the energy released equals the mass lost times the speed of light squared (mass in kg, energy in J).",
                "Fission: a heavy nucleus splits after absorbing a neutron; released neutrons cause a chain reaction. Reactors use control rods, a moderator and a coolant.",
                "Fusion: light nuclei join at very high temperature and pressure, as in the Sun.",
                "In nuclear equations the totals of A and Z balance."),
        ],
    ),
    # ------------------------------------------------------------------ 10. Thermionic emission and CRO
    lesson(
        module=M_AT, topic="Thermionic emission and the cathode ray oscilloscope",
        title="Thermionic emission and the cathode ray oscilloscope",
        slug="phd-thermionic-emission-cro",
        minutes=22,
        summary="A hot filament emits electrons (thermionic emission). The cathode ray oscilloscope uses a beam of these electrons, deflected by the "
                "Y-plates and the time base, to display voltages and measure peak voltage, period and frequency.",
        objectives=[
            "Define thermionic emission and describe how an electron beam is produced in a vacuum tube",
            "Describe the main parts of a cathode ray oscilloscope and what each does",
            "Read the peak voltage and the period from a CRO trace and calculate the frequency",
            "Describe the trace for a d.c. and for an a.c. input",
        ],
        key_concepts=["Thermionic emission", "Electron gun", "Fluorescent screen", "Y-plates and time base", "Y-gain", "Time base", "Peak voltage"],
        blocks=[
            H("Introduction"),
            T("In a hospital workshop in Bamenda, a technician connects a heart monitor to an oscilloscope. A wavy line moves across the screen. "
              "The line shows how a voltage changes with time. The device that draws it, the **cathode ray oscilloscope (CRO)**, uses a beam of electrons."),
            H("Thermionic emission"),
            D("**Thermionic emission** is the release of electrons from the surface of a hot metal. The heat gives some free electrons in the metal enough energy to escape from the surface.",
              title="Thermionic emission"),
            T("Emission increases with a higher temperature and a larger surface area. To produce a beam, the heated metal (the **cathode**) is placed in a **vacuum**, "
              "so that the electrons are not stopped by air particles and the hot filament does not burn. "
              "A positive **anode** attracts the electrons and accelerates them towards it. Some pass through a hole in the anode as a narrow beam."),
            KEY("The electron gun",
                "A heater warms the cathode. The cathode emits electrons. A grid (negative) controls how many electrons go on, so it controls the brightness. "
                "Anodes (positive) accelerate and focus the electrons into a narrow beam.",
                cards=[["Heated cathode", "Gives off electrons by thermionic emission."],
                       ["Grid", "Controls the number of electrons: brightness."],
                       ["Anodes", "Accelerate and focus the beam."]]),
            H("The cathode ray oscilloscope"),
            T("After the electron gun, the beam passes between two pairs of metal plates. The **Y-plates** (above and below the beam) move the beam up and down. "
              "The **X-plates** (left and right) move the beam sideways. The beam then hits a **fluorescent screen**, which glows where electrons strike it, and the spot of light shows the position of the beam."),
            D("The **time base** is a circuit that applies a steadily increasing voltage to the X-plates. It makes the spot move across the screen at a steady speed and then flick back. "
              "The signal to be measured is connected to the Y-plates (through an amplifier, with a **Y-gain** control). So the screen shows voltage (up) against time (across).",
              title="Time base and Y-input"),
            KEY("Reading the controls",
                "The **Y-gain** says how many volts each vertical division stands for (for example 2 V/div). "
                "The **time base** says how much time each horizontal division stands for (for example 5 ms/div).",
                cards=[["Y-gain (V/div)", "Peak voltage = number of divisions x V/div."],
                       ["Time base (ms/div)", "Period T = divisions for one cycle x ms/div. Frequency f = 1/T."]]),
            IMG("f5ph-d-cro-trace1.svg",
                alt="A CRO screen with 8 by 6 divisions showing two cycles of a sine wave. The peak is 2 divisions above the centre and one cycle is 4 divisions wide. The Y-gain is 2 volts per division and the time base 5 milliseconds per division.",
                caption="Figure 1. A CRO trace. Y-gain 2 V/div, time base 5 ms/div."),
            EX("Worked example 1: reading an a.c. trace", intro="Use Figure 1. Find the peak voltage, the period and the frequency.", steps=[
                S("Peak voltage", math=r"2 \text{ div} \times 2 \text{ V/div} = 4 \text{ V}", text="The peak is 2 divisions above the centre line."),
                S("Period", math=r"T = 4 \text{ div} \times 5 \text{ ms/div} = 20 \text{ ms} = 0.020 \text{ s}", text="One complete cycle takes 4 divisions."),
                S("Frequency", math=r"f = \dfrac{1}{T} = \dfrac{1}{0.020} = 50 \text{ Hz}"),
            ]),
            IMG("f5ph-d-cro-dc.svg",
                alt="A CRO screen with a flat horizontal line 1.5 divisions above the centre. The Y-gain is 2 volts per division.",
                caption="Figure 2. A d.c. input (a battery) gives a flat line displaced from the centre."),
            EX("Worked example 2: a d.c. trace", intro="Figure 2 shows a battery connected to the Y-input. The Y-gain is 2 V/div. What is the voltage of the battery?", steps=[
                S("Count the divisions", text="The line is 1.5 divisions above the centre."),
                S("Voltage", math=r"1.5 \times 2 = 3 \text{ V}", text="A d.c. voltage gives a straight line. Reversing the battery moves the line below the centre."),
            ]),
            T("**Uses of the CRO.** It measures voltage (peak values), period and frequency, compares two signals, and shows the shape of a sound wave from a microphone. "
              "A trace that is taller means a bigger amplitude, and a trace with more cycles on the screen has a higher frequency."),
            MISTAKE("Reading the whole height as the peak voltage",
                    "The peak voltage is measured from the centre line to the top of the wave. The distance from the bottom to the top is the peak-to-peak value, twice the peak."),
            MISTAKE("Forgetting to convert ms to s",
                    "Convert the period to seconds before using f = 1/T. 20 ms = 0.020 s, so f = 50 Hz, not 0.05 Hz."),
            MISTAKE("Saying the screen shows voltage against distance",
                    "The vertical axis shows voltage and the horizontal axis shows time, because of the time base."),
            QUIZ("Why must the electron beam in a CRO travel in a vacuum?",
                 ["So that the electrons are heated", "So that the electrons are not stopped or scattered by air particles", "So that the screen can glow", "So that the anode is cooled"], 1,
                 "Air particles would collide with the electrons and stop them, and the hot filament would burn in air.",
                 hint="What would the electrons hit in air?",
                 feedback=["Electrons are released by the heating of the filament, not in the vacuum.", "", "The screen glows because electrons hit it, not because of the vacuum.", "The anode is not cooled by the vacuum."]),
            QUIZ("A CRO trace has a time base of 10 ms/div and one cycle covers 5 divisions. What is the frequency?",
                 ["2 Hz", "20 Hz", "50 Hz", "200 Hz"], 1,
                 "T = 5 x 10 ms = 50 ms = 0.050 s, so f = 1/0.050 = 20 Hz.",
                 hint="Find T first, then use f = 1/T.",
                 feedback=["2 Hz would need a period of 0.5 s, which is not what the trace shows.", "", "50 is the period in ms, not the frequency in Hz.", "200 Hz would need a period of 5 ms: this uses 1 division instead of 5 divisions."]),
            TIP("**Exam link.** Thermionic emission and the CRO appear in Paper 1 multiple choice (parts, a trace to read) and in Paper 2 (a trace is given and the peak voltage, period and frequency are required). "
                "Always give the units V, ms or s, and Hz.",
                title="Where this appears"),
            PQ("Define thermionic emission and state two conditions that make an electron beam in a tube.",
               "Thermionic emission is the release of electrons from the surface of a hot metal. A beam needs a heated cathode, a vacuum, and a positive anode to accelerate the electrons."),
            PQ("A CRO has a Y-gain of 5 V/div and a time base of 2 ms/div. The trace is a sine wave with a peak of 3 divisions and a period of 4 divisions. Find the peak voltage and the frequency.",
               r"Peak voltage $= 3 \times 5 = 15 \text{ V}$. $T = 4 \times 2 = 8 \text{ ms} = 0.008 \text{ s}$, so $f = 1/0.008 = 125 \text{ Hz}$."),
            PQ("Describe the trace seen when a 1.5 V cell is connected to the Y-input of a CRO with the time base on.",
               "A straight horizontal line, displaced above the centre line (or below it if the cell is reversed), because the voltage is constant with time."),
            PQ("State the job of (a) the time base, (b) the fluorescent screen.",
               "(a) The time base sweeps the spot across the screen at a steady speed, so the horizontal axis is time. (b) The screen glows where the electrons strike it so that the position of the beam can be seen."),
            SUM("Thermionic emission: a hot metal releases electrons. An electron gun in a vacuum makes a narrow beam.",
                "In a CRO, the Y-plates deflect the beam up and down by the signal; the time base moves it across the screen; the fluorescent screen shows the spot.",
                "Peak voltage = divisions x Y-gain. Period = divisions x time base. Frequency = 1/period.",
                "A d.c. input gives a flat line; an a.c. input gives a wave."),
        ],
    ),
    # ------------------------------------------------------------------ 11. Semiconductors, diodes, logic gates
    lesson(
        module=M_AT, topic="Semiconductors, diodes and logic gates",
        title="Semiconductors, diodes, rectification and logic gates",
        slug="phd-semiconductors-diodes-logic-gates",
        minutes=26,
        summary="Semiconductors such as silicon conduct by electrons and holes. A p-n junction diode lets current pass one way only and rectifies a.c.; "
                "logic gates (NOT, AND, OR, NAND, NOR) decide outputs from inputs and are described by truth tables.",
        objectives=[
            "Distinguish conductors, semiconductors and insulators and explain n-type and p-type semiconductors",
            "Describe a p-n junction diode, forward and reverse bias, and half-wave and full-wave rectification",
            "State the symbol and truth table of NOT, AND, OR, NAND and NOR gates",
            "Work out the output of a simple combination of gates",
        ],
        key_concepts=["Semiconductor", "Hole", "n-type and p-type", "p-n junction diode", "Rectification", "Logic gate", "Truth table"],
        blocks=[
            H("Introduction"),
            T("Your mobile phone, a calculator, a radio and a solar lamp are full of tiny electronic parts made of **semiconductors**. "
              "Two kinds of parts are especially important at this level: the **diode**, which lets current flow in one direction only, and **logic gates**, which make simple decisions. "
              "This lesson explains both."),
            H("Semiconductors"),
            D("A **semiconductor** is a material whose electrical conductivity is between that of a conductor (a metal) and an insulator. "
              "Silicon and germanium are semiconductors.",
              title="Semiconductor"),
            T("In a **metal**, current is carried by free electrons only. When a metal is heated, its atoms vibrate more and the electrons are scattered more, so its resistance goes up and its conductivity goes down.\n\n"
              "In a pure **semiconductor** at low temperature there are very few free charges. Heating frees more electrons from their bonds. "
              "Each freed electron leaves a **hole** (a missing electron that behaves like a positive charge). Both electrons and holes carry current, "
              "and the conductivity **increases** with temperature. The Board has noted that candidates fail to state these two differences."),
            KEY("Conductor against semiconductor",
                "In a conductor, only electrons carry current. In a semiconductor, electrons and holes both do. "
                "The conductivity of a conductor decreases when the temperature goes up; that of a semiconductor increases.",
                cards=[["Conductor (metal)", "Conduction by electrons; conductivity falls as temperature rises."],
                       ["Semiconductor", "Conduction by electrons and holes; conductivity rises as temperature rises."]]),
            D("**Doping** means adding a very small amount of another element to a pure semiconductor. **n-type** is made by adding atoms with 5 outer electrons (such as phosphorus); "
              "the extra electrons are free to move, so the charge carriers are mainly **electrons**. **p-type** is made by adding atoms with 3 outer electrons (such as boron); "
              "this makes gaps, or **holes**, and the charge carriers are mainly **holes**. Both types are electrically neutral.",
              title="n-type and p-type"),
            H("The p-n junction diode"),
            D("A **p-n junction diode** is a p-type and an n-type semiconductor joined together. At the junction a thin layer with no free charges forms. "
              "It lets current flow easily in one direction (**forward bias**) and hardly at all in the other (**reverse bias**).",
              title="p-n junction diode"),
            T("The diode symbol is a triangle with a bar. The triangle points in the direction of the conventional current in forward bias. "
              "The diode conducts when the p-side (the triangle side) is joined to the positive terminal of the supply, and it blocks when the connections are reversed."),
            IMG("f5ph-d-diode-circuits.svg",
                alt="Two circuits each with a cell, a diode and a lamp. In circuit P the diode triangle points in the direction of the conventional current. In circuit Q the diode is reversed.",
                caption="Figure 1. In circuit P the diode is forward biased and the lamp lights. In circuit Q it is reversed and the lamp stays off."),
            D("**Rectification** is the change of alternating current into direct current (one direction only). With one diode, only half of each cycle gets through: **half-wave rectification**. "
              "With four diodes joined as a bridge, both halves are used, with the second half turned upside down: **full-wave rectification**. A capacitor can then smooth the output.",
              title="Rectification"),
            IMG("f5ph-d-rectification.svg",
                alt="Three graphs: an a.c. sine wave, the half-wave output with only the positive halves, and the full-wave output with all halves positive.",
                caption="Figure 2. Half-wave and full-wave rectification of an a.c. input."),
            H("Logic gates"),
            D("A **logic gate** is an electronic circuit with one or more inputs and one output. Each input and the output are either **1** (high voltage, on) or **0** (low voltage, off). "
              "A **truth table** lists the output for every combination of inputs.",
              title="Logic gate"),
            CODE("NOT (1 input)      AND            OR             NAND           NOR\nA  Q              A B  Q         A B  Q         A B  Q         A B  Q\n0  1              0 0  0         0 0  0         0 0  1         0 0  1\n1  0              0 1  0         0 1  1         0 1  1         0 1  0\n                  1 0  0         1 0  1         1 0  1         1 0  0\n                  1 1  1         1 1  1         1 1  0         1 1  0",
                 "text", title="Truth tables"),
            T("**In words.** NOT changes 1 to 0 and 0 to 1. AND gives 1 only if **both** inputs are 1. OR gives 1 if **at least one** input is 1. "
              "NAND is AND followed by NOT: it gives 0 only when both inputs are 1. NOR is OR followed by NOT: it gives 1 only when both inputs are 0."),
            EX("Worked example 1: a security light", intro="A lamp must switch on only when it is dark AND someone is moving. A light sensor gives A = 1 in daylight. A motion sensor gives B = 1 when it detects movement. The signal A goes through a NOT gate, and the output of the NOT gate and B go to an AND gate. Write the truth table for the lamp Q.", steps=[
                S("Write the rule", text="Q = (NOT A) AND B."),
                S("A = 0, B = 0", text="NOT A = 1; 1 AND 0 = 0. Q = 0 (dark, no movement)."),
                S("A = 0, B = 1", text="NOT A = 1; 1 AND 1 = 1. Q = 1 (dark and movement: the lamp is on)."),
                S("A = 1, B = 0", text="NOT A = 0; 0 AND 0 = 0. Q = 0."),
                S("A = 1, B = 1", text="NOT A = 0; 0 AND 1 = 0. Q = 0 (daylight: the lamp is off)."),
            ]),
            EX("Worked example 2: a diode circuit", intro="A cell, a diode and a lamp are in series. In circuit P the diode triangle points away from the positive terminal of the cell, towards the lamp. Does the lamp light? What if the diode is reversed?", steps=[
                S("Direction of conventional current", text="Conventional current leaves the positive terminal and passes through the diode in the direction of the triangle."),
                S("Circuit P", text="The diode is forward biased, so the lamp lights."),
                S("Reversed diode", text="The diode is reverse biased and blocks the current, so the lamp stays off."),
            ]),
            MISTAKE("Saying a diode conducts in both directions",
                    "A diode conducts in one direction only (forward bias). In reverse bias a tiny current can pass, but we treat it as zero."),
            MISTAKE("Mixing up NAND and AND",
                    "NAND is the opposite of AND: it outputs 0 only when both inputs are 1."),
            MISTAKE("Saying a semiconductor is a poor conductor that gets worse when heated",
                    "A metal's conductivity falls when it is heated. A semiconductor's conductivity rises when it is heated."),
            QUIZ("In a p-n junction diode connected in forward bias, the...",
                 ["p-side is joined to the negative terminal", "p-side is joined to the positive terminal and a current flows", "diode never conducts", "n-side is joined to the positive terminal and a current flows"], 1,
                 "In forward bias the p-side connects to the positive terminal and the diode conducts.",
                 hint="Remember that the triangle points the way the conventional current goes.",
                 feedback=["That is reverse bias: the diode blocks the current.", "", "A diode conducts in forward bias.", "That is reverse bias."]),
            QUIZ("A gate gives output 1 only when both inputs are 0. Which gate is it?",
                 ["AND", "OR", "NAND", "NOR"], 3,
                 "NOR is OR followed by NOT, so it gives 1 only when both inputs are 0.",
                 hint="Compare the rows of the truth tables.",
                 feedback=["AND gives 1 only when both inputs are 1.", "OR gives 1 when any input is 1.", "NAND gives 0 only when both inputs are 1.", ""]),
            TIP("**Exam link.** The Board has reported that candidates fail to distinguish conductors from semiconductors. "
                "Semiconductors, diodes and logic gates appear in Paper 1 multiple choice and in Paper 2 short questions. Learn the five truth tables.",
                title="Where this appears"),
            PQ("State two ways in which the conduction in a semiconductor differs from that in a metal conductor.",
               "In a semiconductor, current is carried by electrons and holes (in a metal, by electrons only). The conductivity of a semiconductor rises as the temperature rises, but that of a metal falls."),
            PQ("Explain what is meant by an n-type semiconductor and how it is made.",
               "A pure semiconductor such as silicon is doped with a small amount of an element with 5 outer electrons, such as phosphorus. The extra electrons are free to move, so electrons are the main charge carriers."),
            PQ("Describe how a single diode and a resistor can change a.c. to d.c. What is the output called?",
               "The diode conducts only in the forward direction, so only half of each a.c. cycle passes to the resistor. The output is d.c. of a pulsating kind, called half-wave rectified."),
            PQ("Write the truth table of a two-input NAND gate.",
               "A=0, B=0 gives 1; A=0, B=1 gives 1; A=1, B=0 gives 1; A=1, B=1 gives 0."),
            SUM("Semiconductors (silicon, germanium) conduct by electrons and holes; their conductivity rises as temperature rises. n-type has extra electrons; p-type has holes.",
                "A p-n junction diode conducts in forward bias only; it is used to rectify a.c. Half-wave uses one diode; full-wave uses four.",
                "Logic gates: NOT inverts; AND needs both inputs 1; OR needs at least one input 1; NAND and NOR are the opposites of AND and OR.",
                "Truth tables list the output for every input combination."),
        ],
    ),
]

LESSONS += [
    # ------------------------------------------------------------------ X1. Paper 1
    lesson(
        module=M_EX, topic="Paper 1",
        title="Paper 1: multiple-choice strategies for Physics",
        slug="phx-paper-1-multiple-choice-strategies",
        minutes=22,
        summary="Paper 1 is 50 multiple-choice questions in 1 hour 30 minutes. Learn the time plan of 1.8 minutes a question, the two-pass method, "
                "elimination, unit checks and the traps that wrong options set.",
        objectives=[
            "State how Paper 1 is organised and calculate the average time per question",
            "Use the two-pass method and elimination to choose the best option",
            "Check units, powers and directions to catch the usual wrong options",
            "List the formulae and units to revise before Paper 1",
        ],
        key_concepts=["Paper 1", "Two-pass method", "Elimination", "Distractor", "Unit check", "Estimation"],
        blocks=[
            H("Introduction"),
            T("Imagine a candidate in an examination hall in Buea. The paper has 50 multiple-choice questions and 90 minutes. "
              "The questions come from the whole Physics course: measurement, mechanics, heat, waves and light, electricity and magnetism, and atomic physics and electronics. "
              "Good physics knowledge is the first half of success. Good paper technique is the second half."),
            D("Physics Paper 1 has **50 multiple-choice questions** and lasts **1 hour 30 minutes**. All questions cover the syllabus topics. "
              "According to the Board's 2023 report, the examination tests about 30% knowledge, 40% comprehension and 30% higher ability.",
              title="Paper 1: the official facts"),
            T("This means that only about a third of the questions are recall. The rest ask you to understand, apply a law or work out a result. "
              "The Board's report also says that almost all calculation questions need a calculator, so carry one that works, with fresh batteries."),
            TIP("**Exam link.** Everything in this course can be asked in Paper 1. Use the mock exam in this module to see your score by topic, and revise the weak topics first.",
                title="Where this appears"),
            H("Time: 1.8 minutes a question"),
            T("90 minutes divided by 50 questions is **1.8 minutes** for each question. A recall question takes 20 seconds. A calculation may take three minutes. "
              "The study plan below is KKEVO advice, not an official rule."),
            KEY("The two-pass method (KKEVO advice)",
                "Go through the paper twice. First collect the marks that are easy. Then use the remaining time for the hard questions.",
                cards=[["Pass 1 (about 55 minutes)", "Answer each question you can do in about a minute. Tick the doubtful ones and move on."],
                       ["Pass 2 (about 25 minutes)", "Go back to the ticked questions. Calculate, eliminate wrong options, choose."],
                       ["Check (about 10 minutes)", "Make sure every question has an answer. Re-read questions with NOT, only or except."]]),
            EX("Worked example 1: the time plan", intro="You spend 55 minutes on pass 1 and finish 38 questions. How many questions are left, and how long is available for each of them if you keep 10 minutes for the final check?", steps=[
                S("Questions left", math=r"50 - 38 = 12"),
                S("Time left for pass 2", math=r"90 - 55 - 10 = 25 \text{ minutes}"),
                S("Time per question", math=r"\dfrac{25}{12} = 2.1 \text{ minutes}", text="You have about 2 minutes for each remaining question, so use the time to calculate carefully."),
            ]),
            H("Reading and eliminating"),
            D("The **stem** is the question. The **key** is the correct option. The **distractors** are the wrong options. A good distractor is the answer that a student gets after making a typical mistake.",
              title="Stem, key and distractors"),
            T("Cover the options and try to answer from the stem alone. Then look for your answer. "
              "If it is not there, check for a different form of the same answer, such as 0.5 kg and 500 g. "
              "Cross out the options that must be wrong: a wrong unit, an impossible size, a wrong direction."),
            KEY("Quick checks before you choose",
                "(1) Units: does the unit match the quantity? (2) Size: is the answer sensible? A person weighing 6 N is not sensible. "
                "(3) Powers: did the formula need a square, a square root or a conversion to metres or kilograms? (4) Direction or sign: forward or backward, increase or decrease?",
                cards=[["Unit", "Joule is energy, watt is power, newton is force."],
                       ["Size", "Does the answer make sense in real life?"],
                       ["Power", "Check for squares: v squared, I squared, c squared."],
                       ["Direction", "Check for words like opposite, decrease, parallel."]]),
            EX("Worked example 2: a calculation", intro="A car travels 90 km in 1.5 hours. Its average speed is: A 135 km/h, B 60 km/h, C 0.017 km/h, D 91.5 km/h.", steps=[
                S("Choose the formula", math=r"\text{speed} = \dfrac{\text{distance}}{\text{time}}"),
                S("Substitute", math=r"\dfrac{90}{1.5} = 60 \text{ km/h}", text="The answer is B."),
                S("Why the others are wrong", text="A multiplies (90 x 1.5). C divides time by distance (1.5/90). D adds the two numbers."),
            ]),
            EX("Worked example 3: eliminating by units", intro="Which unit is the same as a joule per second? A newton, B watt, C pascal, D volt.", steps=[
                S("Recall", text="Power = energy / time, so the unit is joule per second."),
                S("Name the unit", text="The unit of power is the watt (W), so the answer is B. Newton is force, pascal is pressure and volt is joule per coulomb."),
            ]),
            EX("Worked example 4: a density question", intro="A block has a mass of 600 g and a volume of 200 cm cubed. What is its density in g/cm cubed? A 0.33, B 3.0, C 120 000, D 800.", steps=[
                S("Formula", math=r"\rho = \dfrac{m}{V} = \dfrac{600}{200} = 3.0 \text{ g/cm}^3"),
                S("Check the others", text="A inverts the formula (200/600). C multiplies the numbers. D adds them."),
            ]),
            H("Facts to know cold"),
            CODE("Quantity        Unit            Quantity       Unit\nForce           N (newton)      Pressure       Pa (N/m2)\nEnergy, work    J (joule)       Power          W (J/s)\nFrequency       Hz              Charge         C (A s)\nPotential diff. V (J/C)         Resistance     ohm (V/A)\nMagnetic field  T (tesla)       Activity       Bq or counts/s", "text", title="Units to learn"),
            T("Also learn the main formulae: $v = f\\lambda$, $P = IV$, $V = IR$, $\\rho = m/V$, $W = Fd$, $p = mv$, $Q = mc\\Delta\\theta$, $V_s/V_p = N_s/N_p$, $F = BIL$ and the equations of motion. "
              "In Paper 1 you do not need to remember rare constants: the question usually gives them."),
            MISTAKE("Spending five minutes on one hard question",
                    "One question is worth the same as any other. Tick it, move on and return in pass 2."),
            MISTAKE("Not converting units before calculating",
                    "Convert g to kg, cm to m and minutes to seconds first, unless the formula's units match. Most wrong options come from a missing conversion."),
            MISTAKE("Leaving questions blank",
                    "A blank gets no mark. Narrow the options down by elimination, then choose one."),
            QUIZ("After a minute you cannot decide on a question. What should you do, using the two-pass method?",
                 ["Keep working until you are sure", "Leave it blank for ever", "Tick it, move on and return in pass 2", "Choose any option and never think about it again"], 2,
                 "In pass 1 you collect the easy marks. Return to the ticked questions in pass 2.",
                 hint="Think about what is the best use of 90 minutes.",
                 feedback=["One hard question can cost the time of three easy ones.", "A blank earns nothing: return and choose in pass 2.", "",
                           "You may guess at the end, but first return and use elimination."]),
            QUIZ("A question asks for the force on a 2 kg object in newtons, using g = 10 m/s squared. One option is 0.2. What is the best way to check it?",
                 ["It is correct because it has a decimal", "A weight near 20 N is expected, so 0.2 N is too small and cannot be right", "Weights are always smaller than masses", "It is correct because 2 divided by 10 is 0.2"], 1,
                 "W = mg = 2 x 10 = 20 N. The option 0.2 comes from dividing instead of multiplying and fails the size check.",
                 hint="Compare the size with the real-life weight of a 2 kg object.",
                 feedback=["A decimal does not make an answer right.", "", "Weight and mass are different quantities, and the number depends on g.", "That divides, but the formula is W = mg."]),
            PQ("Calculate the average time per question in Paper 1, and explain what you would do if a question takes longer than three minutes.",
               "90 / 50 = 1.8 minutes. If a question takes more than about three minutes, tick it and move on, then return to it in the second pass."),
            PQ("Name two checks you can make on a numerical option before choosing it.",
               "Check the unit matches the quantity, and check that the size is sensible. You can also check whether a power (square) or a unit conversion was needed."),
            PQ("A student reads 'Which of the following is NOT a unit of energy?' and chooses the first option that is a unit of energy. What mistake was made?",
               "The student ignored the word NOT. The answer is the option that is not a unit of energy. Underline words such as NOT, only and except."),
            PQ("List three formulae with their units that you should revise for Paper 1.",
               "For example: P = IV (watts), F = BIL (newtons), Vs/Vp = Ns/Np (volts), E = mc squared (joules), v = f x wavelength (m/s)."),
            SUM("Paper 1 has 50 multiple-choice questions in 1 hour 30 minutes: about 1.8 minutes each.",
                "Use two passes: easy marks first (tick the doubtful ones), then the ticked questions, then a final check.",
                "Eliminate wrong options by unit, size, power and direction. Underline NOT, only and except.",
                "Learn the units and main formulae. Take a working calculator. Never leave a question blank."),
        ],
    ),
    # ------------------------------------------------------------------ X2. Paper 2 Section I
    lesson(
        module=M_EX, topic="Paper 2",
        title="Paper 2 Section I: compulsory questions, units, definitions and calculations",
        slug="phx-paper-2-section-i-units-definitions-calculations",
        minutes=24,
        summary="Section I is compulsory. The Board reports that marks are lost for missing units, poorly phrased definitions and laws, and weak calculations. "
                "Learn definitions word for word, write the unit every time and set out each calculation in four lines.",
        objectives=[
            "State what Section I of Paper 2 is and why accurate wording and units earn marks",
            "Write precise definitions of key physical quantities and laws",
            "Set out a calculation: formula, substitution, answer, unit",
            "Handle standard form, rounding and the value of g correctly",
        ],
        key_concepts=["Paper 2", "Section I", "Definition", "Unit", "Calculation layout", "Standard form", "Significant figures"],
        blocks=[
            H("Introduction"),
            T("A candidate in Bafoussam works out a correct answer of 84 000 for a heating problem, and writes 84 000 with no unit. "
              "The examiner cannot give the full mark. The Board's report for 2023 says that unit errors cost candidates a great many marks. "
              "This lesson teaches the habits that stop you losing marks in Paper 2 Section I."),
            D("Paper 2 lasts **2 hours 30 minutes**. **Section I** has compulsory questions (you answer them all) and takes about **1.5 hours**. "
              "**Section II** has either/or questions, where you choose one from each pair. "
              "In the 2023 paper, as the Board's report numbers it, Section I was questions 1 to 6. Check the exact format with your teacher.",
              title="Paper 2: the official facts"),
            T("From the Board's report, about the candidates of 2023: they did better on explanations and everyday situations than on calculations; they often failed to quote correct units; "
              "they phrased definitions and laws poorly; and they were better at plotting and reading graphs than before. Calculations needed a calculator."),
            TIP("**Exam link.** Section I covers many topics in short structured questions: definitions, laws, diagrams, graphs, descriptions of experiments and calculations. "
                "Revise definitions and units from every module.",
                title="Where this appears"),
            H("Definitions: say it exactly"),
            T("A definition has a fixed shape: the name of the quantity, then what it is in measurable terms. Learn these word for word. "
              "The Board's report named several that candidates wrote badly. Here are model answers."),
            KEY("Model definitions",
                "Learn the shape of each definition. Use the words 'per unit' where a quantity is divided by another.",
                cards=[["E.m.f.", "The work done per unit charge in converting other forms of energy into electrical energy in a source."],
                       ["Half-life", "The time taken for the activity (or count rate, or number of radioactive nuclei) in a sample to fall to half its original value."],
                       ["Specific heat capacity", "The energy needed to change the temperature of 1 kg of a substance by 1 K (or 1 degree Celsius)."],
                       ["Total internal reflection", "The complete reflection of light at the boundary between two media when it travels from a denser to a less dense medium and the angle of incidence is greater than the critical angle."],
                       ["Faraday's law", "The induced emf is proportional to the rate of cutting of magnetic field lines (rate of change of flux linkage)."],
                       ["Lenz's law", "The direction of the induced current opposes the change that produces it."]]),
            EX("Worked example 1: a definition", intro="Define half-life.", steps=[
                S("Shape", text="Name the quantity and say what happens to what, and how much."),
                S("Model answer", text="Half-life is the time taken for the activity (or the number of radioactive nuclei) in a sample to fall to half of its original value."),
                S("Common weak answers", text="'Half the time for decay' or 'the time for a substance to disappear' are wrong: they do not say what falls to half."),
            ]),
            H("Units: every number gets one"),
            T("A final answer without a unit, or with the wrong unit, loses the mark for the unit. Write the unit at the end of the answer **and** carry units in the substitution where it helps. "
              "Learn the unit and the symbol for each quantity."),
            CODE("Quantity               Symbol   Unit               Common wrong unit\nForce                  F        newton (N)         kg\nEnergy / work          E, W     joule (J)          W\nPower                  P        watt (W)           J\nPressure               p        pascal (Pa)        N\nSpecific heat capacity c        J/(kg K)           J/kg\nMagnetic flux density  B        tesla (T)          N\nFrequency              f        hertz (Hz)         s\nResistance             R        ohm                V", "text", title="Units and symbols"),
            H("Calculations: four lines"),
            KEY("Set out every calculation in four lines",
                "(1) Write the formula. (2) Substitute the values with the correct units (change to SI units first). (3) Calculate. (4) Give the answer with its unit and a sensible number of significant figures.",
                cards=[["Formula", "Write it first, so the examiner sees the method."],
                       ["Substitution", "Convert first: g to kg, cm to m."],
                       ["Calculation", "Use the calculator carefully; check the powers of ten."],
                       ["Answer", "Number + unit. Round to 2 or 3 significant figures."]]),
            EX("Worked example 2: electrical energy", intro="A motor takes 3.0 A from a 220 V supply for 2.0 minutes. Calculate the electrical energy supplied to the motor.", steps=[
                S("Formula", math=r"E = VIt"),
                S("Convert the time", math=r"t = 2.0 \text{ min} = 120 \text{ s}"),
                S("Substitute", math=r"E = 220 \times 3.0 \times 120"),
                S("Answer with unit", math=r"E = 79\,200 \text{ J} \approx 7.9 \times 10^{4} \text{ J}"),
            ]),
            EX("Worked example 3: heating water", intro="How much energy is needed to heat 0.50 kg of water from 20 degrees Celsius to 60 degrees Celsius? The specific heat capacity of water is 4200 J/(kg K).", steps=[
                S("Formula", math=r"Q = mc\Delta\theta"),
                S("Temperature change", math=r"\Delta\theta = 60 - 20 = 40 \text{ K}"),
                S("Substitute", math=r"Q = 0.50 \times 4200 \times 40"),
                S("Answer with unit", math=r"Q = 84\,000 \text{ J} = 8.4 \times 10^{4} \text{ J}"),
            ]),
            EX("Worked example 4: transformer and unit trap", intro="A transformer has 1200 turns on the primary and 60 turns on the secondary. The primary voltage is 240 V. Calculate the secondary voltage.", steps=[
                S("Formula", math=r"\dfrac{V_s}{V_p} = \dfrac{N_s}{N_p}"),
                S("Substitute", math=r"V_s = 240 \times \dfrac{60}{1200}"),
                S("Answer with unit", math=r"V_s = 12 \text{ V}"),
            ]),
            H("Standard form, rounding and g"),
            T("Write very large or very small numbers in **standard form**: $a \\times 10^n$ with $1 \\le a < 10$. For example, $84\\,000 = 8.4 \\times 10^4$ and $0.000\\,36 = 3.6 \\times 10^{-4}$. "
              "Use the calculator's EXP key correctly: $3.0 \\times 10^8$ is entered as 3.0 EXP 8, not as 3.0 x 10 x 8. "
              "Do not round in the middle of a calculation: round only the final answer. "
              "Use $g = 10$ m/s squared unless the question says 9.8 m/s squared, and say which value you use."),
            MISTAKE("A correct number with no unit, or a wrong unit",
                    "Write the unit every time. Joule for energy, watt for power, newton for force. Examiners take marks for a missing or wrong unit."),
            MISTAKE("A definition that only describes",
                    "Do not write what the quantity is used for. Write what it is: per unit mass, per unit charge, time to fall to half. Learn the standard wording."),
            MISTAKE("Rounding too early",
                    "If you round every step, the final answer drifts. Keep extra digits in the calculator and round at the end."),
            QUIZ("Which is the best definition of the specific heat capacity of a substance?",
                 ["The heat needed to heat the substance", "The energy needed to change the temperature of 1 kg of the substance by 1 K", "The temperature rise of the substance", "The energy stored in the substance"], 1,
                 "It must say the energy, per kilogram, per unit temperature change.",
                 hint="Which option includes both 'per kilogram' and 'per kelvin'?",
                 feedback=["It does not say per kilogram or per kelvin.", "", "A temperature rise is not an energy.", "Stored energy is not the same as the energy per kilogram per kelvin."]),
            QUIZ("A student finds the energy to heat water is 84 000 and writes only 84 000. What is the main problem?",
                 ["The number is too large", "The unit (J) is missing, so the answer is incomplete", "Standard form is not allowed", "Energy is measured in watts"], 1,
                 "The answer needs its unit, J.",
                 hint="Look at what is missing after the number.",
                 feedback=["The size of the number is fine.", "", "Standard form is allowed and often useful.", "Energy is measured in joules, not watts."]),
            PQ("Define e.m.f. and state its unit.",
               "E.m.f. is the work done per unit charge in converting other forms of energy into electrical energy in a source. Its unit is the volt (V), which is a joule per coulomb."),
            PQ("A kettle of power 2.0 kW is on for 3.0 minutes. Calculate the energy it transfers. State the unit.",
               r"$E = Pt = 2000 \times 180 = 360\,000 \text{ J} = 3.6 \times 10^{5} \text{ J}$."),
            PQ("A wire of length 0.20 m carries 2.5 A at right angles to a field of 0.40 T. Calculate the force. Give the unit.",
               r"$F = BIL = 0.40 \times 2.5 \times 0.20 = 0.20 \text{ N}$."),
            PQ("A radioactive sample of activity 640 counts per minute has a half-life of 2 hours. Calculate its activity after 6 hours.",
               r"$n = 6/2 = 3$. Activity $= 640/2^3 = 80$ counts per minute."),
            SUM("Paper 2: 2 hours 30 minutes. Section I is compulsory (about 1.5 hours); Section II is either/or.",
                "The Board reports that marks are lost for missing or wrong units and for poorly phrased definitions and laws.",
                "Learn definitions word for word: say what the quantity is, per unit, or what falls to half.",
                "Set out calculations in four lines: formula, substitution (SI units), calculation, answer with unit.",
                "Use standard form correctly, keep extra digits until the end, and say which value of g you use."),
        ],
    ),
    # ------------------------------------------------------------------ X3. Paper 2 Section II
    lesson(
        module=M_EX, topic="Paper 2",
        title="Paper 2 Section II: either/or choices and time planning",
        slug="phx-paper-2-section-ii-choice-and-time-planning",
        minutes=22,
        summary="In Section II you choose one of each Either/Or pair. KKEVO advice: read both options, choose the one where you can earn most sure marks, "
                "commit within three minutes, and keep to a time plan for the whole 2 hours 30 minutes.",
        objectives=[
            "Explain how the Either/Or choice in Section II works",
            "Use a checklist to choose between two alternatives",
            "Plan the time for Section I, Section II and checking",
            "Plan an answer to a structured question so that no part is left blank",
        ],
        key_concepts=["Section II", "Either/Or", "Time plan", "Checklist", "Structured question", "Command words"],
        blocks=[
            H("Introduction"),
            T("A candidate in Ngaoundere finishes Section I and still has an hour left. The Section II question 7 offers two alternatives. "
              "She reads the Either option and sees a long calculation on mechanics that she finds hard. The Or option asks for a diagram, a definition and a short calculation on heat. "
              "She chooses the Or option and earns good marks. Choosing well is a skill. This lesson teaches it."),
            D("In **Section II** of Paper 2, each question is given as a pair: an **Either** and an **Or**. You answer **one** of the two in each pair. "
              "In the Board's report for 2023, questions 7, 8 and 9 each had an Either and an Or. Check the exact format with your teacher.",
              title="Section II: the official facts"),
            T("The Board's report records that some alternatives were popular and well answered, and others were unpopular and badly answered. "
              "In 2023 the questions on mechanics, optics and static electricity were answered poorly, and those on temperature, energy and current electricity were answered better. "
              "This does not mean the same will happen again, but it reminds us that a choice made without reading both options is risky."),
            TIP("**Exam link.** All topics in the six modules can appear in Section II. The Either and the Or are not always on the same module. "
                "The advice below is KKEVO advice, not an official rule.",
                title="Where this appears"),
            H("Choosing between Either and Or"),
            KEY("A checklist for the choice (KKEVO advice)",
                "Read both alternatives fully. For each one, count the parts you can answer confidently. Pick the one with more sure marks, not the one that looks shorter or has more text.",
                cards=[["1. Read both", "Spend about 2 minutes. Do not start writing after the first line."],
                       ["2. Count the sure parts", "Mark each part: sure, partly sure or not sure."],
                       ["3. Look at the calculations", "Do you know the formula and unit? Can you do the arithmetic?"],
                       ["4. Decide in 3 minutes", "Cross out the other alternative so that you do not switch half way."]]),
            T("**Do not choose by topic alone.** A topic you like can still have a hard part. A topic you find hard can have easy parts, such as a definition or a diagram. "
              "Look at every part before you decide."),
            T("**Never answer both options of the same pair.** In the real paper you answer one of each pair. Only one will be marked, and the time you spend on the other is lost."),
            H("Planning the time"),
            CODE("Total time                       150 minutes\nSection I (compulsory)           about 90 minutes\nSection II (three pairs)         about 60 minutes\n\nSection I: 90 / 6 questions       = 15 minutes each\nSection II: 60 / 3 questions       = 20 minutes each (including 3 minutes to choose)", "text", title="A time plan (KKEVO advice, not an official rule)"),
            T("The Board states that Section I is allowed about 1.5 hours. The rest of the 2 hours 30 minutes is for Section II. "
              "If you divide the time in this way, you have about 15 minutes for each Section I question and about 20 minutes for each Section II question. "
              "Keep two minutes at the end for checking units."),
            EX("Worked example 1: the time calculation", intro="Using a 150-minute paper, 90 minutes for Section I with 6 questions and the rest for 3 Section II answers, find the minutes for each Section I answer and each Section II answer.", steps=[
                S("Section I", math=r"\dfrac{90}{6} = 15 \text{ minutes}"),
                S("Time left for Section II", math=r"150 - 90 = 60 \text{ minutes}"),
                S("Section II", math=r"\dfrac{60}{3} = 20 \text{ minutes}"),
            ]),
            EX("Worked example 2: choosing", intro="Either: (a) state Fleming's left-hand rule; (b) calculate the force on a wire (formula needed); (c) describe how to reverse a motor. Or: (a) define half-life; (b) calculate the activity after 3 half-lives; (c) state two uses of radioactive materials. Which is the better choice for a candidate who knows the topic of magnetism well but is unsure about nuclear physics?", steps=[
                S("Mark each part", text="Either: (a) sure, (b) sure, (c) sure. Or: (a) partly sure, (b) partly sure, (c) sure."),
                S("Count the sure marks", text="The Either option has three sure parts and the Or option has one."),
                S("Decide", text="Choose the Either option and cross out the Or. This choice is made from the parts, not from the title."),
            ]),
            H("Inside a structured question"),
            T("A structured question is split into parts (a), (b), (c) and so on. Parts lead from easy to hard, and a later part may use the answer of an earlier one. "
              "Read the **command word** of each part: **state** (a short fact), **define** (the exact definition), **describe** (say what happens), **explain** (give the reason with because), "
              "**calculate** (formula, working, unit) and **sketch or draw** (a neat labelled diagram). "
              "The Board's report notes improvement in the description of experiments: give the apparatus, the steps, the measurements and what you do with them."),
            EX("Worked example 3: a plan for a describe question", intro="Describe how to find the half-life of a radioactive source with a GM tube and counter.", steps=[
                S("Background", text="Measure the background count rate with the source far away."),
                S("Measure", text="Put the source at a fixed distance and record the count rate at regular times. Subtract the background."),
                S("Plot", text="Plot corrected count rate against time and draw a smooth curve."),
                S("Read", text="Read the time for the count rate to fall to half. Check with a second half. This time is the half-life."),
            ]),
            MISTAKE("Starting to write before reading both alternatives",
                    "You may find halfway that the part you chose is hard. Read both fully first."),
            MISTAKE("Changing your choice in the middle",
                    "Switching wastes the time already used. If you must switch, do it within the first five minutes."),
            MISTAKE("Leaving out the easy parts",
                    "A definition, a unit or a labelled diagram is often among the easiest marks. Attempt every part, including those you think are hard: a method may earn something."),
            QUIZ("In Section II, a candidate answers both the Either and the Or of question 7 and runs out of time. What went wrong?",
                 ["Nothing: answering both is required", "Only one alternative should be answered, so time was wasted on the other", "The candidate should have answered Section II before Section I", "The candidate should have skipped question 7"], 1,
                 "You answer one of each Either/Or pair. Time spent on the second option is wasted.",
                 hint="Remember what 'either/or' means.",
                 feedback=["The paper asks you to choose one of each pair.", "", "The order of sections is up to you, but this does not explain the problem.", "Skipping the question loses marks."]),
            QUIZ("Which is the best reason for choosing one alternative?",
                 ["It has fewer lines of text", "It is the topic of the lesson I enjoyed", "I have counted more parts that I can answer confidently", "It was the first alternative on the page"], 2,
                 "Choose by counting the parts you can answer confidently, not by length or order.",
                 hint="Think about how marks are earned part by part.",
                 feedback=["A short question can still be hard.", "A liked topic can still hide a hard part.", "", "The order says nothing about difficulty."]),
            PQ("A paper is 150 minutes long. Section I takes 90 minutes. How long is left for three Section II answers, and what is the time for each?",
               "150 - 90 = 60 minutes. 60 / 3 = 20 minutes for each answer."),
            PQ("Describe a checklist for choosing between an Either and an Or question.",
               "Read both alternatives fully; mark the parts you can answer confidently; check the formulae and units for calculations; decide within about three minutes and cross out the other alternative."),
            PQ("State what each command word asks for: (a) define, (b) explain, (c) calculate.",
               "(a) Define: give the exact definition. (b) Explain: give a reason, using because. (c) Calculate: write the formula, the substitution with units, and the answer with its unit."),
            PQ("Why should a candidate not start to write the Either answer before reading the Or?",
               "The Or may have more parts that the candidate can answer. Reading both first allows the better choice and avoids a switch that wastes time."),
            SUM("Section II: you answer one of each Either/Or pair. Check the exact format with your teacher.",
                "Read both options, count the sure parts, decide within about 3 minutes, and cross out the other option.",
                "KKEVO time plan: about 90 minutes for Section I (15 per question), about 60 for Section II (20 per answer).",
                "Read the command word of every part. Attempt every part and give units."),
        ],
    ),
]
