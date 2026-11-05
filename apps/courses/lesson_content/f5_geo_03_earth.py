"""Form 5 Geography: The Earth as a Planet (8 lessons, one practice set each)."""

from .dsl import *  # noqa: F403

COURSE = ("geography", "form-5")

MODULE = "The Earth as a Planet"
SOLAR = "The earth in the solar system"
LOC = "Location and time"
ROT = "Rotation and revolution"

LESSONS = []

# ------------------------------------------------------------------ 1. Solar system and planets
LESSONS.append(lesson(
    module=MODULE,
    topic=SOLAR,
    title="The solar system and the planets",
    slug="earth-solar-system-and-planets",
    minutes=18,
    summary="The solar system is the Sun and everything that moves around it. Learn the eight planets in order outward from the Sun, and the moons, asteroids and other members, with a sketch.",
    objectives=[
        "Define the solar system",
        "Name the eight planets in order from the Sun",
        "Illustrate the solar system with a labelled sketch",
        "Describe moons and asteroids and the position of the earth",
    ],
    key_concepts=["Solar system", "Sun", "Planet", "Moon (satellite)", "Asteroid belt", "Orbit"],
    blocks=[
        H("Introduction"),
        T("At dawn in Buea you can watch the Sun rise behind Mount Cameroon. At night, from a village with no electric light, "
          "you can see the Moon and a few bright 'stars' that do not twinkle. Those bright points are usually planets."),
        T("The Sun, the Moon and the planets are all part of one family in space. In this lesson you will learn what that family is "
          "called, who its members are, and where the earth fits in."),
        D("The **solar system** is the Sun together with all the bodies that travel around it: planets, their moons, asteroids "
          "and other smaller bodies. The Sun's gravity holds the whole system together.", title="Definition: solar system"),
        H("The Sun and the planets"),
        T("The **Sun** is a star. It is a huge ball of very hot gas that gives out light and heat. It is at the centre of the solar "
          "system, and it is much bigger than everything else in the system put together."),
        D("A **planet** is a large body that travels around the Sun in a fixed path called an **orbit**. A planet does not give out "
          "light of its own. We see it because it reflects sunlight.", title="Definition: planet and orbit"),
        T("There are **eight planets**. Starting from the Sun and moving outwards, the order is: Mercury, Venus, Earth, Mars, "
          "Jupiter, Saturn, Uranus and Neptune."),
        IMG("f5g-earth-solar-system.svg",
            alt="The Sun on the left and the eight planets in order from Mercury to Neptune, with the asteroid belt between Mars and Jupiter. The figure is not to scale.",
            caption="Figure 1. The solar system. NOT to scale: in reality the distances are enormous and the Sun is far bigger than any planet."),
        KEY("Two groups of planets", "The four planets nearest the Sun are small and rocky. The four furthest from the Sun are much larger.", cards=[
            ["Inner planets (1 to 4)", "Mercury, Venus, Earth, Mars. Small, rocky, with solid surfaces."],
            ["Outer planets (5 to 8)", "Jupiter, Saturn, Uranus, Neptune. Very large, made mostly of gas and ice."],
        ], note="Jupiter is the largest planet. Mercury is the smallest and the closest to the Sun."),
        T("A sentence helps you remember the order. Make your own, using the first letter of each planet: M, V, E, M, J, S, U, N. "
          "For example: 'My Very Elegant Mother Just Sent Us Nuts.' A rhyme in your own language works just as well."),
        H("Moons, asteroids and other members"),
        D("A **moon** (also called a **natural satellite**) is a body that orbits a planet. The earth has one moon. Mercury and "
          "Venus have none. Mars has two small moons. Jupiter and Saturn have many.", title="Definition: moon"),
        D("The **asteroid belt** is a wide band of thousands of small rocky bodies called **asteroids**. They orbit the Sun between "
          "the orbits of **Mars** and **Jupiter**.", title="Definition: asteroids"),
        T("The solar system also has **dwarf planets** such as Pluto, and **comets**, which are balls of ice and dust. Pluto was "
          "called the ninth planet until 2006, when scientists placed it in the dwarf-planet group. Today we count eight planets."),
        T("The earth is the **third planet** from the Sun, between Venus and Mars. It is about 150 million kilometres from the Sun. "
          "Sunlight takes about 8 minutes to reach us. It is the only planet known to have life. Its distance from the Sun, "
          "its liquid water and its air all help to make that possible."),
        H("Worked examples: how to answer"),
        EX("Model answer 1: define and list", intro="Define the solar system and name the planets in order from the Sun. [4 marks]", steps=[
            S("Definition (point)", text="The solar system is the Sun and all the bodies that move around it."),
            S("Add the members (detail)", text="These include planets, their moons, asteroids and comets. The Sun's gravity holds them in orbit."),
            S("The order of the planets", text="Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus and Neptune."),
            S("Finish with a fact (example)", text="The asteroid belt lies between Mars and Jupiter."),
        ]),
        EX("Model answer 2: draw a sketch", intro="Draw and label a sketch to show the solar system. [5 marks]", steps=[
            S("Draw the Sun first", text="Draw a large circle on the left and write 'Sun' inside it."),
            S("Draw a straight line for the orbits", text="Mark eight small circles along it in order. Make Jupiter and Saturn the biggest, and Mercury the smallest."),
            S("Label every planet", text="Write the names in order: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune."),
            S("Show the asteroid belt", text="Draw small dots between Mars and Jupiter and label them 'asteroid belt'."),
            S("Add a title and a note", text="Write 'The solar system' and 'not to scale'."),
        ]),
        EX("Model answer 3: the earth's position", intro="Describe the position of the earth in the solar system. [3 marks]", steps=[
            S("Say where it is in the order", text="The earth is the third planet from the Sun."),
            S("Name its neighbours", text="Venus is closer to the Sun and Mars is further away."),
            S("Add a fact", text="It is about 150 million kilometres from the Sun and has one moon."),
        ]),
        MISTAKE("Calling the Moon or the Sun a planet", "The Sun is a star. The Moon is a satellite of the earth, not a planet. Only the eight bodies in the list are planets."),
        MISTAKE("Mixing up the order", "Mars comes before Jupiter, and Uranus comes before Neptune. Learn your own sentence and write the first letters before you answer."),
        QUIZ("Which planet is the fifth from the Sun?", ["Mars", "Jupiter", "Saturn", "Earth"], 1,
             "The order is Mercury 1, Venus 2, Earth 3, Mars 4, Jupiter 5.",
             hint="Count out from the Sun and remember that the asteroid belt comes after the fourth planet.",
             feedback=["Mars is the fourth planet.", "", "Saturn is the sixth planet.", "Earth is the third planet."]),
        QUIZ("Where is the asteroid belt?", ["Between Earth and Mars", "Between Mars and Jupiter", "Between Saturn and Uranus", "Beyond Neptune"], 1,
             "The asteroid belt lies between the orbits of Mars (fourth planet) and Jupiter (fifth planet).",
             hint="Look at Figure 1.",
             feedback=["Earth and Mars have no belt between them.", "", "There is no belt between Saturn and Uranus.", "Pluto and other dwarf planets are beyond Neptune, but that is not the asteroid belt."]),
        TIP("In Paper 1 you may be asked to name a planet from its position, or to pick the correct order. In Paper 2 Section B a sketch of the "
            "solar system is a quick way to earn marks, but only if you write the names in the right order.", title="Exam link"),
        H("Practice questions"),
        PQ("Define the term 'planet'. [2 marks]", "A planet is a large body that travels around the Sun in a fixed path called an orbit. It does not make light of its own; it reflects sunlight."),
        PQ("Name the four inner planets in order from the Sun. [2 marks]", "Mercury, Venus, Earth and Mars."),
        PQ("(a) What is a moon? (b) How many moons does the earth have? [2 marks]", "(a) A moon is a natural body that orbits a planet. (b) The earth has one moon."),
        PQ("Describe the position of the asteroid belt in the solar system. [2 marks]", "The asteroid belt is a band of small rocky bodies. It lies between the orbits of Mars and Jupiter."),
        SUM("The solar system is the Sun and everything that orbits it.",
            "There are eight planets: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, in that order from the Sun.",
            "The inner planets are small and rocky. The outer planets are very large.",
            "Moons orbit planets. The asteroid belt lies between Mars and Jupiter.",
            "The earth is the third planet, with one moon."),
    ],
))

# ------------------------------------------------------------------ 2. Shape and evidence
LESSONS.append(lesson(
    module=MODULE,
    topic=SOLAR,
    title="The shape of the earth and the evidence for it",
    slug="earth-shape-and-evidence",
    minutes=20,
    summary="The earth is an oblate spheroid: almost a sphere, slightly flattened at the poles. Learn the main evidence, from ships disappearing over the horizon to lunar eclipses and photographs from space.",
    objectives=[
        "Describe the shape of the earth as an oblate spheroid",
        "Describe the evidence that the earth is round",
        "Explain how ships, lunar eclipses and circumnavigation show that the earth is curved",
        "State how the earth differs from a perfect sphere",
    ],
    key_concepts=["Oblate spheroid", "Sphere", "Horizon", "Lunar eclipse", "Circumnavigation", "Satellite photograph"],
    blocks=[
        H("Introduction"),
        T("Stand on the beach at Limbe and watch a cargo ship leave for the open sea. First the whole ship is visible. Later the bottom "
          "of the ship disappears and only the top is left. At last even that is gone, yet the ship is still sailing and has not sunk."),
        T("This simple observation is one of the clues that tell us the shape of the earth. In this lesson you will learn what the "
          "shape is called and why we are sure about it."),
        D("The earth is an **oblate spheroid**. This means it is almost a **sphere** (a perfectly round ball) but is slightly "
          "flattened at the North and South Poles and slightly bulging at the equator.", title="Definition: shape of the earth"),
        T("The flattening is caused by the earth's rotation. A spinning ball of rock pushes outwards at its middle. The difference is "
          "small. If you could see the earth from space, it would look like a perfect ball."),
        KEY("How flat is it?", "Measurements of the earth's diameter (the distance straight through the middle).", cards=[
            ["Through the equator", "about 12 756 km"],
            ["Pole to pole", "about 12 714 km"],
            ["Difference", "about 42 km, or about 0.3 percent"],
        ], note="The earth is slightly wider at the equator than from pole to pole."),
        H("Evidence 1: ships and the horizon"),
        T("A ship sailing away does not just get smaller. Its **hull** (the body of the ship) disappears first, then the mast. "
          "The reason is that the surface of the sea is curved. The curve hides the lower part of the ship from the observer."),
        IMG("f5g-earth-ship-horizon.svg",
            alt="An observer on a curved earth sees only the mast and sail of a distant ship because the hull is hidden by the curve of the sea",
            caption="Figure 1. The curve of the sea hides the hull while the mast is still in view."),
        H("Evidence 2: the shadow in a lunar eclipse"),
        T("A **lunar eclipse** happens when the earth lies between the Sun and the Moon. The earth's shadow falls on the Moon. "
          "Whatever the position of the Moon, the edge of the shadow is **always curved**. Only a sphere always makes a round shadow. "
          "A flat disc would make a thin line or an oval shadow when it is turned."),
        IMG("f5g-earth-eclipse.svg",
            alt="The Sun, the Earth and the Moon in line, with the Earth's round shadow falling on the Moon and a curved shadow edge shown on the Moon's disc",
            caption="Figure 2. The earth's shadow on the Moon is always round."),
        H("More evidence"),
        T("**Circumnavigation.** In the early 1500s a Spanish fleet led first by Ferdinand Magellan sailed west and returned to Spain "
          "from the east. Today ships and aircraft travel round the world. A traveller who goes on in one direction, without turning back, "
          "comes back to the starting point. On a flat earth with edges this could not happen."),
        T("**Photographs from space.** Satellites and astronauts have photographed the whole earth as a ball. Weather satellites show "
          "clouds over Cameroon and the Atlantic on a curved disc. This is direct evidence."),
        T("**Different times and stars.** The Sun does not light the whole earth at once. When it is noon in Douala it is night on "
          "the opposite side of the world. Also, the Pole Star is seen higher in the sky as you travel north, and lower as you travel south. "
          "Both facts need a curved surface."),
        CODE("""Evidence                 What we observe                    What it shows
-----------------------  ---------------------------------  ----------------------
Ships over the horizon   Hull vanishes before the mast      Sea surface is curved
Lunar eclipse            Shadow on Moon has a curved edge   The earth is round
Circumnavigation         Travel one way, return to start    No edge, closed surface
Satellite photographs    Whole earth appears as a ball      Direct proof of shape
Time and stars           Different times; Pole Star height  Curved surface""", "text", title="Summary of the evidence"),
        H("Worked examples: how to answer"),
        EX("Model answer 1: two pieces of evidence", intro="Describe two pieces of evidence that show that the earth is round. [4 marks]", steps=[
            S("Evidence 1 (point)", text="When a ship sails away, the hull disappears before the mast."),
            S("Explain it", text="This happens because the surface of the sea is curved and hides the lower part of the ship."),
            S("Evidence 2 (point)", text="During a lunar eclipse the earth's shadow on the Moon always has a curved edge."),
            S("Explain it", text="Only a sphere always casts a round shadow, so the earth must be round."),
        ]),
        EX("Model answer 2: how the earth differs from a sphere", intro="State how the shape of the earth differs from a perfect sphere. [3 marks]", steps=[
            S("Name the shape", text="The earth is an oblate spheroid."),
            S("Describe the difference", text="It is slightly flattened at the poles and bulges at the equator."),
            S("Give the effect", text="The diameter through the equator (about 12 756 km) is about 42 km more than from pole to pole (about 12 714 km)."),
        ]),
        EX("Model answer 3: using a sketch", intro="Draw a labelled sketch to show why the hull of a ship disappears first. [4 marks]", steps=[
            S("Draw the curved sea", text="Draw part of a large circle for the earth's surface."),
            S("Draw the observer and the ship", text="Put a small observer on the left and a ship on the right, far along the curve."),
            S("Draw the line of sight", text="Draw a straight line from the observer. It passes above the hull but touches the mast."),
            S("Label it", text="Label 'observer', 'line of sight', 'hull hidden' and 'mast visible'."),
        ]),
        MISTAKE("Saying the earth is a perfect sphere", "The earth is an oblate spheroid. Say 'almost spherical but flattened at the poles'."),
        MISTAKE("Weak evidence", "'We do not fall off' or 'maps are round' is not evidence. Use the observations in this lesson: ships, lunar eclipse, circumnavigation, photographs."),
        MISTAKE("Mixing eclipses", "In a lunar eclipse the earth's shadow falls on the Moon. The Moon's shadow on the earth belongs to a solar eclipse."),
        QUIZ("What is the shape of the earth?", ["A perfect sphere", "An oblate spheroid", "A flat disc", "A cube"], 1,
             "The earth is almost a sphere but slightly flattened at the poles: an oblate spheroid.",
             hint="Think of a ball that has been gently pressed at the top and bottom.",
             feedback=["The earth is very close to a sphere, but not perfect.", "", "A flat disc cannot explain ships, eclipses or satellite photographs.", "The earth has no corners or flat faces."]),
        QUIZ("Which observation best shows that the sea surface is curved?", [
            "The sea looks blue", "A ship's hull disappears before its mast", "Waves reach the beach", "Fish live in deep water"], 1,
             "The hull disappears first because the curve of the sea hides the lower part of the ship.",
             hint="Which observation depends on shape and not on colour or life?",
             feedback=["Colour does not show shape.", "", "Waves tell us about wind and energy, not shape.", "Fish live in the sea but say nothing about its shape."]),
        TIP("Evidence of the earth's shape appears in Paper 1 as multiple-choice questions on ships, shadows and photographs, and in Paper 2 Section B as a "
            "describe-and-explain question. Always give an observation AND the reason it shows the earth is curved.", title="Exam link"),
        H("Practice questions"),
        PQ("Name the shape of the earth. [1 mark]", "An oblate spheroid (almost a sphere, slightly flattened at the poles)."),
        PQ("Explain why the hull of a ship disappears before the mast when the ship sails away. [3 marks]",
           "The surface of the sea is curved. As the ship moves away, the curve of the sea rises between the observer and the ship and hides the lowest part, the hull, first. The tall mast is still above the line of sight, so it can still be seen."),
        PQ("Describe how a lunar eclipse provides evidence of the earth's shape. [3 marks]",
           "In a lunar eclipse the earth lies between the Sun and the Moon and casts its shadow on the Moon. The edge of the shadow is always curved. Only a sphere always casts a round shadow, so the earth must be a sphere or nearly one."),
        PQ("Give two pieces of evidence, other than ships and lunar eclipses, that the earth is round. [2 marks]",
           "Any two of: photographs from satellites and astronauts show the earth as a ball; travellers can sail or fly round the world (circumnavigation) and return to the start; the Pole Star appears higher as you travel north; different places have different times because the Sun lights only half the earth at once."),
        SUM("The earth is an oblate spheroid: almost a sphere, slightly flattened at the poles.",
            "The equatorial diameter is about 42 km more than the pole-to-pole diameter.",
            "Ships disappear hull first because the sea surface is curved.",
            "The earth's shadow in a lunar eclipse is always curved.",
            "Circumnavigation, satellite photographs, time differences and the Pole Star also show that the earth is round."),
    ],
))

# ------------------------------------------------------------------ 3. Latitude and longitude
LESSONS.append(lesson(
    module=MODULE,
    topic=LOC,
    title="Lines of latitude and longitude",
    slug="earth-latitude-and-longitude",
    minutes=24,
    summary="Latitudes and longitudes form a grid that fixes the position of every place. Learn their characteristics and importance, the key lines, how to give a position and how to calculate north-south distances.",
    objectives=[
        "Define and illustrate lines of latitude and longitude",
        "State the characteristics and importance of latitudes and longitudes",
        "Distinguish between lines of latitude and lines of longitude",
        "Calculate distances from latitudes",
    ],
    key_concepts=["Latitude", "Longitude", "Equator", "Prime Meridian", "Tropics", "Polar circles", "Degree"],
    blocks=[
        H("Introduction"),
        T("Suppose you tell a pilot that you live 'near the coast in Cameroon'. That is not enough to find your house. "
          "A pilot, a ship's captain or a mobile phone needs an exact position."),
        T("Geographers solve this with an imaginary grid of lines drawn on the globe. Every place on earth sits at the meeting point "
          "of two lines. In this lesson you will learn what the lines are, how to read a position, and how to use latitudes to find "
          "north-south distances."),
        H("Latitude"),
        D("**Latitude** is the angular distance of a place **north or south of the equator**, measured in degrees (°). "
          "A **line of latitude** (also called a **parallel**) joins all places with the same latitude.", title="Definition: latitude"),
        KEY("Characteristics of lines of latitude", "Learn these five points.", cards=[
            ["Direction", "They run east to west, and are parallel to the equator."],
            ["Spacing", "They never meet. Neighbouring lines are the same distance apart."],
            ["Numbering", "0° at the equator to 90°N at the North Pole and 90°S at the South Pole."],
            ["Length", "The equator is the longest. They get shorter towards the poles."],
            ["Measured", "As an angle from the centre of the earth. Always say N or S."],
        ]),
        H("Longitude"),
        D("**Longitude** is the angular distance of a place **east or west of the Prime Meridian**, measured in degrees (°). "
          "A **line of longitude** (also called a **meridian**) joins all places with the same longitude.", title="Definition: longitude"),
        KEY("Characteristics of lines of longitude", "Learn these five points.", cards=[
            ["Direction", "They run north to south, from pole to pole."],
            ["Spacing", "They meet at the poles and are furthest apart at the equator."],
            ["Numbering", "0° at the Prime Meridian to 180°E and 180°W on the opposite side."],
            ["Length", "All meridians are the same length (half a great circle)."],
            ["Measured", "As an angle east or west of Greenwich. Always say E or W."],
        ]),
        T("The **Prime Meridian** (0° longitude) passes through **Greenwich**, near London, in the United Kingdom. "
          "It was chosen by international agreement. The meridian on the opposite side of the earth is 180°."),
        IMG("f5g-earth-lat-long.svg",
            alt="A globe showing the equator, the tropics of Cancer and Capricorn, the Arctic and Antarctic circles and the Prime Meridian",
            caption="Figure 1. The main lines on the globe."),
        H("The special lines"),
        KEY("Five important lines of latitude", "They matter because they mark changes in the sun's heat.", cards=[
            ["Equator", "0°. Divides the earth into the Northern and Southern Hemispheres."],
            ["Tropic of Cancer", "23.5°N. The furthest north the Sun is ever overhead."],
            ["Tropic of Capricorn", "23.5°S. The furthest south the Sun is ever overhead."],
            ["Arctic Circle", "66.5°N. Marks the area near the North Pole."],
            ["Antarctic Circle", "66.5°S. Marks the area near the South Pole."],
        ], note="The Prime Meridian (0°) divides the Eastern from the Western Hemisphere. Cameroon lies north of the equator, in the tropics (about 2°N to 13°N) and east of Greenwich (about 9°E to 16°E). Check your textbook for exact limits."),
        CODE("""                Latitude                 Longitude
--------------  -----------------------  ------------------------
Direction       East-west                North-south
Also called     Parallels                Meridians
Starts at       Equator (0°)             Prime Meridian (0°)
Greatest value  90°N / 90°S              180°E / 180°W
Lines meet?     Never (parallel)         At the poles
Same length?    No (shorter to poles)    Yes (all equal)
Says N or S     Yes                      No: says E or W""", "text", title="Latitude and longitude compared"),
        H("Why they are important"),
        T("**Position.** They fix the exact position of any place, so we can locate it on a map or globe.\n\n"
          "**Navigation.** Ships, aircraft and satellite systems use latitude and longitude to find and follow routes.\n\n"
          "**Time.** Longitude is used to work out local time and time zones (see the next lessons).\n\n"
          "**Climate.** Latitude shows whether a place is in the hot tropics, the cooler middle latitudes or the cold polar regions."),
        H("Giving a position"),
        D("Give **latitude first**, then **longitude**. For example, 10°N, 20°E means 10 degrees north of the equator and 20 degrees east "
          "of the Prime Meridian.", title="How to write a position"),
        IMG("f5g-earth-grid-positions.svg",
            alt="A grid with latitude lines from 20 degrees south to 20 degrees north and longitude lines from 0 to 40 degrees east, with points A to E",
            caption="Figure 2. A grid (not a real map) with five points."),
        EX("Worked example 1: reading positions", intro="Give the position of points A, C and E in Figure 2. [3 marks]", steps=[
            S("Point A", text="A is on the line 10°N and on the line 10°E. Position: 10°N, 10°E."),
            S("Point C", text="C is south of the equator (10°S) and on the line 30°E. Position: 10°S, 30°E."),
            S("Point E", text="E is on the equator (0°) and on the line 20°E. Position: 0°, 20°E."),
        ]),
        H("Calculating distances from latitudes"),
        T("Lines of latitude are the same distance apart. The earth's circumference is about 40 000 km and there are 360 degrees "
          "in a circle, so one degree of latitude is about 40 000 divided by 360, which is about 111 km."),
        D("Distance (km) north-south = difference in latitude (degrees) × 111", title="Rule: north-south distance",
          formula=r"\text{distance} = \Delta\text{latitude} \times 111\ \text{km}"),
        KEY("Finding the difference in latitude", "Look at the hemispheres first.", cards=[
            ["Same hemisphere", "Both north or both south: SUBTRACT the latitudes."],
            ["Opposite hemispheres", "One north and one south: ADD the latitudes."],
        ]),
        EX("Worked example 2: same hemisphere", intro="Town X is at 4°N and town Y is at 11°N on the same meridian. Find the north-south distance between them. [3 marks]", steps=[
            S("Same hemisphere, so subtract", math=r"11 - 4 = 7^\circ"),
            S("Multiply by 111 km", math=r"7 \times 111 = 777"),
            S("State the answer", text="The distance is 777 km."),
        ]),
        EX("Worked example 3: opposite hemispheres", intro="Town P is at 5°N and town Q is at 3°S on the same meridian. Find the distance between them. [3 marks]", steps=[
            S("Opposite hemispheres, so add", math=r"5 + 3 = 8^\circ"),
            S("Multiply by 111 km", math=r"8 \times 111 = 888"),
            S("State the answer", text="The distance is 888 km."),
        ]),
        MISTAKE("Giving longitude first", "Always give the latitude first, then the longitude: 10°N, 20°E, not 20°E, 10°N."),
        MISTAKE("Wrong sign for the equator", "Across the equator you ADD the two latitudes. 5°N and 3°S are 8° apart, not 2°."),
        MISTAKE("Using 111 km for longitude", "The 111 km rule is for latitude. Degrees of longitude get shorter in kilometres towards the poles. They are about 111 km apart only at the equator."),
        QUIZ("Which lines run from pole to pole?", ["Lines of latitude", "Lines of longitude", "Both", "Neither"], 1,
             "Lines of longitude (meridians) run north-south from pole to pole.",
             hint="Think of the lines that meet at the poles.",
             feedback=["Latitudes run east-west and never meet.", "", "Only meridians run from pole to pole.", "Meridians do run from pole to pole."]),
        QUIZ("What is the distance between 12°S and 8°N on the same meridian?", ["444 km", "2220 km", "4440 km", "1332 km"], 1,
             "They are in opposite hemispheres, so add: 12 + 8 = 20 degrees. 20 × 111 = 2220 km.",
             hint="Are the two places in the same hemisphere?",
             feedback=["That is 4 degrees, found by subtracting 12 - 8.", "", "That is 40 degrees, double the real value.", "That is 12 degrees, using only the southern latitude."]),
        TIP("Latitude and longitude are tested in Paper 1 (map skills and the earth as a planet) and used in Paper 2 Section A when you give a grid or "
            "geographical position. Always write the degree sign, the N/S or E/W and give latitude first.", title="Exam link"),
        H("Practice questions"),
        PQ("Define 'latitude'. [2 marks]", "Latitude is the angular distance of a place north or south of the equator, measured in degrees."),
        PQ("State two characteristics of lines of longitude. [2 marks]", "Any two of: they run north to south; they meet at the poles; they are furthest apart at the equator; they are all the same length; they are numbered from 0° at the Prime Meridian to 180° east and west."),
        PQ("Calculate the north-south distance between two places on the same meridian, one at 9°N and one at 2°N. [3 marks]", "Same hemisphere, so subtract: 9 - 2 = 7 degrees. Distance = 7 × 111 = 777 km."),
        PQ("Give two reasons why lines of latitude and longitude are important. [2 marks]", "They fix the exact position of any place; they are used in navigation by ships and aircraft; longitude is used to calculate time; latitude shows the climate zone."),
        SUM("Latitude is the angle north or south of the equator (0° to 90°). Lines of latitude are parallel and run east-west.",
            "Longitude is the angle east or west of the Prime Meridian (0° to 180°). Meridians run from pole to pole.",
            "Key lines: equator 0°, tropics 23.5°N and S, polar circles 66.5°N and S, Prime Meridian 0°.",
            "Give a position as latitude first, then longitude.",
            "One degree of latitude is about 111 km. Subtract within a hemisphere; add across the equator."),
    ],
))

# ------------------------------------------------------------------ 4. Great circles and the date line
LESSONS.append(lesson(
    module=MODULE,
    topic=LOC,
    title="Great circles and the International Date Line",
    slug="earth-great-circles-and-the-date-line",
    minutes=20,
    summary="A great circle cuts the earth into two equal halves and gives the shortest route between two places. The International Date Line, near 180 degrees, is where the calendar date changes.",
    objectives=[
        "Define and illustrate great circles and the International Date Line",
        "State the importance of great circles",
        "State the importance of the International Date Line",
        "Explain what happens to the date when the line is crossed",
    ],
    key_concepts=["Great circle", "Small circle", "Shortest route", "International Date Line", "180° meridian", "Calendar date"],
    blocks=[
        H("Introduction"),
        T("A long-distance flight from Africa to North America does not follow a straight line on a flat wall map. "
          "On the map it seems to bend north. This looks strange, but the pilot is following the shortest path over the curved earth."),
        T("In this lesson you will learn about the circles that give these shortest paths, and about a special line in the "
          "Pacific Ocean where the date changes."),
        H("Great circles"),
        D("A **great circle** is a circle drawn on the surface of the earth whose centre is the **centre of the earth**. "
          "It divides the earth into two equal halves.", title="Definition: great circle"),
        KEY("Characteristics of a great circle", "Learn these points.", cards=[
            ["Equal halves", "It cuts the earth into two equal hemispheres."],
            ["Longest circle", "It is the largest circle possible on the earth, about 40 000 km round."],
            ["Examples", "The equator, and any meridian together with the opposite meridian (for example 0° and 180°)."],
            ["Bisect each other", "Two great circles cross at two points exactly opposite each other."],
        ], note="Every other line of latitude is NOT a great circle. It is a small circle: its centre is not the centre of the earth."),
        T("A **small circle** does not cut the earth into equal halves. The Tropic of Cancer and the Arctic Circle are small circles. "
          "Only the equator is a great circle among the parallels."),
        T("Each meridian is only half a great circle, from pole to pole. A meridian and the one on the opposite side of the earth "
          "together form a full great circle."),
        H("Why great circles matter: the shortest route"),
        D("The **shortest distance between two places** on the earth's surface lies along the great circle that passes through both places. "
          "This path is called a **great-circle route**.", title="Rule: shortest route"),
        IMG("f5g-earth-great-circle-route.svg",
            alt="View from above the North Pole of two places A and B on latitude 50 degrees north, 100 degrees apart. The great-circle route bends towards the pole and is shorter than the route along the latitude.",
            caption="Figure 1. Two places on the same line of latitude. The great-circle route is shorter than following the latitude."),
        T("In Figure 1, A and B are both on 50°N and are 100° of longitude apart. The route along the line of latitude is about 7150 km. "
          "The great-circle route is about 6560 km. That is about 590 km shorter. Aircraft and ships follow great-circle routes to save "
          "time and fuel."),
        T("On a flat map, a great-circle route often looks like a curve. On a globe it is the straightest possible path. "
          "A piece of string pulled tight between two places on a globe lies along the great circle."),
        EX("Worked example 1: distance along a great circle", intro="Two places lie on the equator, 60° of longitude apart. Using 1° = 111 km, find the distance along the equator between them. [3 marks]", steps=[
            S("The equator is a great circle", text="Along a great circle, 1 degree of arc is about 111 km."),
            S("Multiply", math=r"60 \times 111 = 6660"),
            S("State the answer", text="The distance is about 6660 km."),
        ]),
        EX("Worked example 2: model answer", intro="State two reasons why great circles are important. [2 marks]", steps=[
            S("Reason 1", text="The shortest distance between two places lies along a great circle, so aircraft and ships use great-circle routes."),
            S("Reason 2", text="Shorter routes save time and fuel, and great circles such as the equator and meridians divide the earth into equal halves and are used for measuring position and distance."),
        ]),
        H("The International Date Line"),
        T("The earth turns once in about 24 hours. At any moment it is a different time in different places, and a new day must begin "
          "somewhere. People agreed that the new day would begin along a line in the Pacific Ocean."),
        D("The **International Date Line** is an imaginary line that follows the **180° meridian** (the meridian opposite Greenwich) "
          "from the North Pole to the South Pole. When you cross it, the **calendar date changes** by one day.", title="Definition: International Date Line"),
        IMG("f5g-earth-date-line.svg",
            alt="A world strip from 180 degrees west to 180 degrees east. The International Date Line is at both edges. The side east of the line has the earlier date and the side west of it has the later date.",
            caption="Figure 2. The International Date Line near 180°. East of the line the date is earlier; west of it the date is later."),
        T("The line sits in the middle of the Pacific Ocean, where there is little land. It is not perfectly straight at 180°. It bends "
          "around some island groups and countries so that each place has one date throughout."),
        KEY("Crossing the date line", "Remember: east means go back a day, west means go forward a day.", cards=[
            ["Going EAST (towards the Americas)", "Subtract one day. A Wednesday becomes the Tuesday before."],
            ["Going WEST (towards Asia and Australia)", "Add one day. A Wednesday becomes Thursday."],
        ], note="The time of day on your clock does not jump by hours. Only the date changes."),
        EX("Worked example 3: crossing the line", intro="A ship sails east across the International Date Line on Wednesday morning. What day is it just after crossing? [2 marks]", steps=[
            S("Going east", text="Moving east across the line, the date goes back by one day."),
            S("Subtract one day", text="Wednesday becomes Tuesday."),
            S("State the answer", text="It is Tuesday morning after the crossing."),
        ]),
        EX("Worked example 4: model answer", intro="State two reasons why the International Date Line is important. [2 marks]", steps=[
            S("Reason 1", text="It gives the whole world one agreed place where the calendar date changes, so places do not have confusing dates."),
            S("Reason 2", text="It keeps the date the same within each country or island group by bending away from 180°, and lets travellers know when to change their calendar."),
        ]),
        MISTAKE("Thinking every parallel is a great circle", "Only the equator is a great circle among the parallels. The Tropics and Polar circles are small circles."),
        MISTAKE("Adding a day when going east", "East means go back. A common memory trick is 'East, least': a day less."),
        MISTAKE("Mixing the date line and the Prime Meridian", "The Prime Meridian is 0° at Greenwich. The International Date Line is about 180°, on the opposite side of the earth."),
        QUIZ("Which of these is a great circle?", ["The Tropic of Cancer", "The equator", "The Arctic Circle", "The 30°N line of latitude"], 1,
             "Only the equator is a great circle among the lines of latitude. Its centre is the centre of the earth.",
             hint="A great circle must cut the earth into two equal halves.",
             feedback=["The Tropic of Cancer is a small circle.", "", "The Arctic Circle is a small circle.", "30°N is a small circle: it does not cut the earth into equal halves."]),
        QUIZ("A plane flies west across the International Date Line on Monday. What happens to the date?", [
            "It goes back to Sunday", "It moves forward to Tuesday", "It stays Monday", "It changes by 12 hours only"], 1,
             "Going west across the date line, add one day, so Monday becomes Tuesday.",
             hint="Going west means forward a day.",
             feedback=["That is what happens when going east.", "", "The date does change when the line is crossed.", "The date changes by a whole day, not by half a day."]),
        TIP("Great circles and the date line appear in Paper 1 as short knowledge questions and in Paper 2 Section B as 'define and state the importance'. "
            "Remember the key phrases: 'shortest distance' for great circles and 'calendar date changes' for the date line.", title="Exam link"),
        H("Practice questions"),
        PQ("Define a great circle. [2 marks]", "A great circle is a circle on the earth's surface whose centre is the centre of the earth. It divides the earth into two equal halves."),
        PQ("Name one great circle on the earth. [1 mark]", "The equator (or a meridian together with the opposite meridian, such as 0° and 180°)."),
        PQ("Explain why aircraft follow great-circle routes. [2 marks]", "A great-circle route is the shortest distance between two places on the earth's surface, so it saves time and fuel."),
        PQ("(a) Near which meridian is the International Date Line? (b) What happens to the date when a traveller crosses it going east? [2 marks]", "(a) The 180° meridian. (b) The date goes back by one day."),
        SUM("A great circle has its centre at the earth's centre and divides the earth into two equal halves.",
            "The equator and a meridian with its opposite meridian are great circles. Other parallels are small circles.",
            "The shortest route between two places lies along a great circle.",
            "The International Date Line follows the 180° meridian, bending around some islands.",
            "Cross the date line going east: go back a day. Going west: go forward a day."),
    ],
))

# ------------------------------------------------------------------ 5. Local time and longitude
LESSONS.append(lesson(
    module=MODULE,
    topic=LOC,
    title="Local time and longitude",
    slug="earth-local-time-and-longitude",
    minutes=24,
    summary="Local time depends on longitude: every 15 degrees is one hour and every degree is 4 minutes. Learn to find local time from a longitude and a longitude from local times, using Greenwich as the reference.",
    objectives=[
        "Define local time",
        "Calculate local time from lines of longitude",
        "Calculate longitude from local time",
        "Explain why places east of Greenwich are ahead and places west are behind",
    ],
    key_concepts=["Local time", "Noon", "Greenwich Mean Time", "15° = 1 hour", "1° = 4 minutes", "Ahead and behind"],
    blocks=[
        H("Introduction"),
        T("The Sun rises in Maroua a little before it rises in Douala. A farmer in the Far North sees the Sun reach its highest point "
          "in the sky earlier than a fisherman at the coast. Maroua is further east than Douala, so the Sun reaches it first."),
        T("This difference is small, but over long distances it is large. When it is morning in Cameroon it is already afternoon "
          "in Asia and still night in the Americas. Local time depends on longitude."),
        D("**Local time** is the time at a place, worked out from the position of the Sun. At **12 noon local time** the Sun is at "
          "its highest point in the sky at that place. All places on the same meridian have the same local time.", title="Definition: local time"),
        H("Why time changes with longitude"),
        T("The earth turns through 360° in about 24 hours, from west to east. So the Sun reaches places in turn, from east to west."),
        KEY("Two facts to learn", "These come from 360° ÷ 24 hours.", cards=[
            ["15° = 1 hour", "360 degrees ÷ 24 hours = 15 degrees every hour."],
            ["1° = 4 minutes", "60 minutes ÷ 15 degrees = 4 minutes for each degree."],
        ]),
        T("We use **Greenwich**, on the Prime Meridian (0°), as the reference. Time at Greenwich is called **Greenwich Mean Time (GMT)**. "
          "Every other place is compared with it."),
        D("Places **east** of Greenwich are **ahead** (their time is later). Places **west** of Greenwich are **behind** (their time is earlier). "
          "To work out the time difference, **add** for east and **subtract** for west.", title="Rule: east add, west subtract"),
        IMG("f5g-earth-local-time-strip.svg",
            alt="A strip of longitudes from 60 degrees west to 60 degrees east. When it is 12:00 at Greenwich the local times increase by one hour for every 15 degrees east and decrease by one hour for every 15 degrees west.",
            caption="Figure 1. Local time at each 15° of longitude when it is 12:00 noon at Greenwich."),
        H("Calculating local time from longitude"),
        KEY("Four steps", "Use them every time.", cards=[
            ["1", "Find the longitude difference in degrees (add if on opposite sides of Greenwich, subtract if on the same side)."],
            ["2", "Convert to time: divide by 15 for hours, or multiply by 4 for minutes."],
            ["3", "East of the known place: ADD the time. West: SUBTRACT it."],
            ["4", "Write the answer on the 24-hour clock and check the day."],
        ]),
        EX("Worked example 1: east of Greenwich", intro="When it is 08:00 at Greenwich, what is the local time at longitude 30°E? [3 marks]", steps=[
            S("Longitude difference", text="30° east of Greenwich."),
            S("Convert to time", math=r"30 \div 15 = 2\ \text{hours}"),
            S("East, so add", math=r"\text{08:00} + 2\ \text{h} = \text{10:00}"),
            S("State the answer", text="The local time is 10:00."),
        ]),
        EX("Worked example 2: west of Greenwich", intro="When it is 15:00 at Greenwich, what is the local time at longitude 75°W? [3 marks]", steps=[
            S("Convert to time", math=r"75 \div 15 = 5\ \text{hours}"),
            S("West, so subtract", math=r"\text{15:00} - 5\ \text{h} = \text{10:00}"),
            S("State the answer", text="The local time is 10:00."),
        ]),
        EX("Worked example 3: degrees that are not multiples of 15", intro="Yaoundé is at about 12°E. When it is 12:00 noon at Greenwich, what is the local time in Yaoundé? [3 marks]", steps=[
            S("Convert degrees to minutes", math=r"12 \times 4 = 48\ \text{minutes}"),
            S("East, so add", math=r"\text{12:00} + 48\ \text{min} = \text{12:48}"),
            S("State the answer", text="The local time in Yaoundé is about 12:48."),
        ]),
        H("Calculating longitude from local time"),
        T("To find a longitude, work backwards. Find the time difference from Greenwich, change it to minutes, then divide by 4 "
          "(or change it to hours and multiply by 15)."),
        D("If local time is **later** than Greenwich time, the place is **east**. If it is **earlier**, the place is **west**.", title="Rule: east or west?"),
        EX("Worked example 4: a place east of Greenwich", intro="When it is 12:00 noon at Greenwich, the local time at a place is 15:20. Find its longitude. [3 marks]", steps=[
            S("Time difference", math=r"\text{15:20} - \text{12:00} = 3\ \text{h}\ 20\ \text{min} = 200\ \text{min}"),
            S("Convert to degrees", math=r"200 \div 4 = 50^\circ"),
            S("Local time is later, so east", text="The longitude is 50°E."),
        ]),
        EX("Worked example 5: a place west of Greenwich", intro="When it is 12:00 noon at Greenwich, the local time at a place is 07:40. Find its longitude. [3 marks]", steps=[
            S("Time difference", math=r"\text{12:00} - \text{07:40} = 4\ \text{h}\ 20\ \text{min} = 260\ \text{min}"),
            S("Convert to degrees", math=r"260 \div 4 = 65^\circ"),
            S("Local time is earlier, so west", text="The longitude is 65°W."),
        ]),
        EX("Worked example 6: two places on opposite sides", intro="Place P is at 20°W and place Q is at 40°E. When the local time at P is 08:00, find the local time at Q. [3 marks]", steps=[
            S("They are on opposite sides of Greenwich, so add the longitudes", math=r"20 + 40 = 60^\circ"),
            S("Convert to time", math=r"60 \div 15 = 4\ \text{hours}"),
            S("Q is east of P, so add", math=r"\text{08:00} + 4\ \text{h} = \text{12:00}"),
            S("State the answer", text="The local time at Q is 12:00 noon."),
        ]),
        MISTAKE("Adding when you should subtract", "Test your answer: east places are always ahead. If your answer for a place east of Greenwich is earlier than the Greenwich time, you made an error."),
        MISTAKE("Confusing hours and minutes", "15° is one HOUR but 1° is 4 MINUTES. For 12°, do 12 × 4 = 48 minutes, not 12 hours."),
        MISTAKE("Subtracting longitudes on opposite sides", "20°W and 40°E are on opposite sides of Greenwich, so the difference is 20 + 40 = 60°, not 40 - 20 = 20°."),
        QUIZ("What is the local time at 45°E when it is 06:00 at Greenwich?", ["03:00", "09:00", "10:30", "06:45"], 1,
             "45° ÷ 15 = 3 hours. East is ahead, so 06:00 + 3 h = 09:00.",
             hint="Divide 45 by 15 first.",
             feedback=["This subtracts 3 hours, as if the place were west of Greenwich.", "", "This divides 45 by 10 instead of 15, giving 4.5 hours.", "This adds 45 minutes: treating 45 as minutes, not degrees."]),
        QUIZ("A place has a local time 2 hours behind Greenwich time. Where is it?", ["30°E", "30°W", "2°W", "120°E"], 1,
             "2 hours × 15 = 30 degrees. Behind means west, so 30°W.",
             hint="Behind means earlier, so on which side of Greenwich?",
             feedback=["East places are ahead, not behind.", "", "2 degrees would be only 8 minutes behind.", "120°E would be 8 hours ahead."]),
        TIP("Local time calculations are a favourite in Paper 1 and Paper 2 Section B. Show every step: difference in longitude, conversion, then add or subtract. "
            "Even if the final answer is wrong, you can earn method marks.", title="Exam link"),
        H("Practice questions"),
        PQ("Define 'local time'. [2 marks]", "Local time is the time at a place, based on the position of the Sun. It is 12 noon local time when the Sun is at its highest point. All places on the same meridian have the same local time."),
        PQ("When it is 12:00 noon at Greenwich, find the local time at 60°E. [2 marks]", "60 ÷ 15 = 4 hours. East, so add: 12:00 + 4 h = 16:00."),
        PQ("When it is 12:00 noon at Greenwich, the local time at a place is 14:40. Find the longitude. [3 marks]", "Time difference = 2 h 40 min = 160 minutes. 160 ÷ 4 = 40 degrees. The local time is later, so the longitude is 40°E."),
        PQ("Explain why places east of Greenwich are ahead of Greenwich time. [3 marks]", "The earth rotates from west to east. So the Sun reaches places in the east before it reaches Greenwich. Their noon is earlier than noon at Greenwich, so their clocks are ahead of Greenwich time."),
        SUM("Local time is the time at a place based on the Sun: noon when the Sun is highest.",
            "The earth turns 360° in 24 hours: 15° = 1 hour and 1° = 4 minutes.",
            "East of Greenwich is ahead (add). West of Greenwich is behind (subtract).",
            "To find longitude: time difference in minutes divided by 4. Later means east, earlier means west.",
            "Places on opposite sides of Greenwich: add their longitudes to find the difference."),
    ],
))

# ------------------------------------------------------------------ 6. Standard time and time zones
LESSONS.append(lesson(
    module=MODULE,
    topic=LOC,
    title="Standard time and time zones",
    slug="earth-standard-time-and-time-zones",
    minutes=22,
    summary="Standard time is one official time used across a whole country or zone. Learn how the world is divided into 24 time zones, why countries use them, and how to work out times in different zones, including Cameroon's.",
    objectives=[
        "Define standard time",
        "Illustrate and describe time zones",
        "Explain why countries use standard time and time zones",
        "Calculate the time in different zones, using Cameroon's standard time",
    ],
    key_concepts=["Standard time", "Time zone", "Standard meridian", "UTC / GMT", "Cameroon time (UTC+1)", "Time difference"],
    blocks=[
        H("Introduction"),
        T("Douala and Maroua do not have exactly the same local time, because they are on different meridians. "
          "If every town set its clocks by its own Sun, a bus leaving Douala at 8:00 would arrive at a Maroua clock that "
          "reads a different time. Radio, banks, schools and airlines could not work."),
        T("To solve this, each country, or each part of a large country, agrees to use one official time. "
          "This lesson explains how that works."),
        D("**Standard time** is the official time used throughout a country or region. It is the local time of one chosen meridian, "
          "called the **standard meridian**.", title="Definition: standard time"),
        D("A **time zone** is a region of the earth that uses the same standard time. The world is divided into **24 time zones**, "
          "each about **15° of longitude** wide, because 360° ÷ 24 = 15°.", title="Definition: time zone"),
        H("How the zones work"),
        T("The standard meridian of each zone is a multiple of 15°: 0°, 15°E, 30°E, 45°E and so on, and 15°W, 30°W and so on. "
          "A zone reaches 7.5° on each side of its standard meridian. For example, the zone centred on 15°E runs from 7.5°E to 22.5°E."),
        T("The time at Greenwich (0°) is **Greenwich Mean Time (GMT)**. It is also the basis of **Coordinated Universal Time (UTC)**, "
          "which is used as the world's time reference. Each zone is described as a number of hours **ahead of (+)** or **behind (−)** UTC."),
        IMG("f5g-earth-time-zones.svg",
            alt="A world strip divided into 24 time zones. Greenwich is zero, the zone containing Cameroon is plus one, and five example cities are marked: New York minus 5, Accra 0, Yaounde plus 1, Nairobi plus 3, Tokyo plus 9.",
            caption="Figure 1. Time zones from −12 to +12 (simplified). Cameroon is in the yellow zone, UTC +1."),
        T("In real life, time-zone borders do not follow meridians exactly. They follow country and regional borders so that people "
          "in one region keep the same time."),
        H("Why countries use standard time"),
        KEY("Reasons for standard time and zones", "Four main reasons.", cards=[
            ["Avoid confusion", "Everyone in a country uses the same time instead of many local times."],
            ["Transport", "Train, bus and air timetables can be planned and understood."],
            ["Communication and business", "Radio, TV, banks and telephone calls are scheduled at fixed times."],
            ["Easy comparison", "Time differences between countries are whole hours, easy to calculate."],
        ], note="Large countries may use several zones. Small countries, like Cameroon, use one."),
        H("Cameroon's standard time"),
        T("Cameroon uses **one standard time for the whole country**. It is **UTC +1**, one hour ahead of Greenwich. "
          "It is based on the meridian 15°E. Nigeria and Gabon use the same zone. The whole of Cameroon (about 9°E to 16°E) fits inside "
          "the zone 7.5°E to 22.5°E, so a single standard time works well."),
        T("A clock in Douala (about 10°E) and a clock in Maroua (about 14°E) both show Cameroon time. The local Sun time at each place "
          "is slightly different from this standard time."),
        CODE("""Place           Zone     When it is 09:00 in Yaounde
--------------  -------  ---------------------------
Accra           UTC +0   08:00
Yaounde         UTC +1   09:00
Johannesburg    UTC +2   10:00
Nairobi         UTC +3   11:00
Tokyo           UTC +9   17:00
New York        UTC -5   03:00""", "text", title="Zones and times (standard time, no summer clocks)"),
        T("Some countries move their clocks one hour in summer. Cameroon does not, and in this course you are always given the "
          "zone number, so you can ignore summer time."),
        H("Calculating time in different zones"),
        KEY("Method", "Work from the zone numbers.", cards=[
            ["1", "Find the difference between the two zone numbers (subtract if both + or both −; add if one is + and one is −)."],
            ["2", "If the place you want has the larger number, ADD the difference. If the smaller number, SUBTRACT it."],
            ["3", "Check the day: crossing midnight changes the date."],
        ]),
        EX("Worked example 1: times in other zones", intro="It is 09:00 in Yaoundé (UTC +1). Find the time in (a) Nairobi (UTC +3) and (b) New York (UTC −5). [4 marks]", steps=[
            S("(a) Difference between +1 and +3", math=r"3 - 1 = 2\ \text{hours}"),
            S("Nairobi has the larger number, so add", math=r"\text{09:00} + 2\ \text{h} = \text{11:00}"),
            S("(b) Difference between +1 and −5", math=r"1 + 5 = 6\ \text{hours}"),
            S("New York has the smaller number, so subtract", math=r"\text{09:00} - 6\ \text{h} = \text{03:00}"),
        ]),
        EX("Worked example 2: the date changes", intro="It is 22:00 on Tuesday in Yaoundé (UTC +1). What is the time and day in Tokyo (UTC +9)? [3 marks]", steps=[
            S("Difference", math=r"9 - 1 = 8\ \text{hours}"),
            S("Tokyo is ahead, so add", math=r"\text{22:00} + 8\ \text{h} = \text{30:00}"),
            S("Subtract 24 hours and move to the next day", math=r"\text{30:00} - \text{24:00} = \text{06:00 on Wednesday}"),
            S("State the answer", text="It is 06:00 on Wednesday in Tokyo."),
        ]),
        EX("Worked example 3: local time and standard time", intro="Douala is at about 10°E. Cameroon's standard meridian is 15°E. By how many minutes is Douala's local Sun time different from Cameroon time? [3 marks]", steps=[
            S("Difference in longitude", math=r"15 - 10 = 5^\circ"),
            S("Convert to minutes", math=r"5 \times 4 = 20\ \text{minutes}"),
            S("Decide the direction", text="Douala is west of 15°E, so its local Sun time is 20 minutes behind Cameroon time."),
        ]),
        MISTAKE("Using the wrong sign", "Zones east of Greenwich are plus, zones west are minus. New York is UTC −5 (behind), Tokyo is UTC +9 (ahead)."),
        MISTAKE("Forgetting to add when one zone is plus and the other is minus", "From +1 to −5 the difference is 1 + 5 = 6 hours, not 4 hours."),
        MISTAKE("Forgetting the date", "If the answer is 24:00 or more, subtract 24 and move to the next day. If it is below 00:00, add 24 and go back a day."),
        QUIZ("Cameroon's standard time is:", ["UTC +0", "UTC +1", "UTC +2", "UTC -1"], 1,
             "Cameroon uses UTC +1, based on the meridian 15°E.",
             hint="It is one hour ahead of Greenwich.",
             feedback=["UTC +0 is the time at Greenwich, used for example in Accra.", "", "UTC +2 is used, for example, in South Africa.", "UTC −1 would be behind Greenwich, which is west."]),
        QUIZ("How wide is one time zone in degrees of longitude?", ["7.5°", "15°", "24°", "30°"], 1,
             "360° ÷ 24 zones = 15° per zone.",
             hint="Divide the degrees in a circle by the number of zones.",
             feedback=["7.5° is the half-width, from the centre of the zone to its edge.", "", "24 is the number of zones, not the width.", "30° would give only 12 zones."]),
        TIP("Standard time and time zones appear in Paper 1 and Paper 2 Section B. Questions may ask you to explain WHY we need zones as well as to calculate. "
            "Learn two reasons and show your zone-number working.", title="Exam link"),
        H("Practice questions"),
        PQ("Define 'standard time'. [2 marks]", "Standard time is the official time used throughout a country or region. It is the local time of one chosen standard meridian."),
        PQ("Give two reasons why countries use standard time. [2 marks]", "To avoid confusion from many local times; to make timetables for transport possible; to organise communication and business such as radio, TV and banking; to make it easy to compare times between countries."),
        PQ("It is 14:00 in Yaoundé (UTC +1). What is the time in New York (UTC −5)? [3 marks]", "Difference = 1 + 5 = 6 hours. New York is behind, so subtract: 14:00 − 6 h = 08:00."),
        PQ("State (a) the standard time of Cameroon and (b) the number of time zones in the world. [2 marks]", "(a) UTC +1 (one hour ahead of Greenwich). (b) 24 time zones."),
        SUM("Standard time is the official time of a country or zone, based on one standard meridian.",
            "There are 24 time zones, each about 15° wide, numbered from UTC −12 to +12 with Greenwich at 0.",
            "Zones avoid confusion and help transport, communication and business.",
            "Cameroon uses one standard time, UTC +1, based on 15°E.",
            "To find time in another zone: find the difference in zone numbers, add if ahead, subtract if behind, check the date."),
    ],
))

# ------------------------------------------------------------------ 7. Rotation and its effects
LESSONS.append(lesson(
    module=MODULE,
    topic=ROT,
    title="Rotation of the earth and its effects",
    slug="earth-rotation-and-its-effects",
    minutes=20,
    summary="Rotation is the earth's spin on its axis, once in about 24 hours from west to east. Learn the difference between rotation and revolution and the effects of rotation: day and night, time differences, and deflection of winds and currents.",
    objectives=[
        "Differentiate between rotation and revolution of the earth",
        "Describe the rotation of the earth on its axis",
        "Describe and illustrate the effects of rotation: day and night, time differences",
        "Describe the deflection of winds and ocean currents caused by rotation",
    ],
    key_concepts=["Rotation", "Revolution", "Axis", "Day and night", "Deflection of winds and currents", "West to east"],
    blocks=[
        H("Introduction"),
        T("Every morning the Sun rises over the hills of Bamenda and every evening it sets behind the Atlantic at Limbe. "
          "It seems that the Sun is moving across the sky. In fact the Sun is not moving round us. The earth is turning."),
        T("The earth makes two main movements. This lesson separates them and then explains the effects of the first, rotation."),
        D("**Rotation** is the spinning of the earth on its **axis**. The **axis** is an imaginary line through the earth from the "
          "North Pole to the South Pole.", title="Definition: rotation"),
        D("**Revolution** is the movement of the earth in its **orbit** around the Sun.", title="Definition: revolution"),
        KEY("Rotation compared with revolution", "Do not mix them up.", cards=[
            ["Rotation", "Spinning on its axis. Takes about 24 hours (one day). Gives day and night."],
            ["Revolution", "Travelling round the Sun. Takes about 365 days (one year). Gives the seasons (next lesson)."],
        ]),
        H("How the earth rotates"),
        KEY("Facts about rotation", "Learn all four.", cards=[
            ["Direction", "From west to east. Seen from above the North Pole, the earth turns anticlockwise."],
            ["Time", "One turn takes about 24 hours."],
            ["Speed", "360° ÷ 24 h = 15° per hour. At the equator the surface moves at about 1670 km per hour. The speed falls to zero at the poles."],
            ["Axis", "The axis is tilted by 23.5° from the line at right angles to the flat plane of the earth's orbit."],
        ]),
        T("The axis always points to the same place in space, near the Pole Star. We will come back to this tilt in the next lesson."),
        H("Effect 1: day and night"),
        T("The Sun lights only half of the earth at a time. The lit half has day and the dark half has night. "
          "The boundary between them is called the **circle of illumination**."),
        IMG("f5g-earth-day-night.svg",
            alt="View from above the North Pole. The half of the earth facing the sun is day and the other half is night. The earth rotates anticlockwise so that a place at the top moves into daylight at sunrise and a place at the bottom moves into darkness at sunset.",
            caption="Figure 1. Rotation gives day and night. A place moves from night into day at sunrise and from day into night at sunset."),
        T("As the earth turns, each place moves through daylight and then darkness once in 24 hours. Because the earth turns from west to east, "
          "the Sun seems to rise in the **east** and set in the **west**. Near the equator, day and night each last about 12 hours all year."),
        H("Effect 2: differences in time"),
        T("The earth turns through 15° every hour. So places on different meridians have the Sun overhead at different moments. "
          "Places to the east see noon first. This gives **local time** (15° = 1 hour). To avoid confusion, the world uses "
          "**time zones**. You studied both in the last lessons."),
        H("Effect 3: deflection of winds and ocean currents"),
        T("A wind or ocean current that moves over the rotating earth does not travel in a straight line. It is turned to one side. "
          "This turning is called **deflection**."),
        D("Because of the earth's rotation, moving winds and currents are **deflected to the right in the Northern Hemisphere** "
          "and **to the left in the Southern Hemisphere**. There is no deflection at the equator.", title="Rule: deflection"),
        IMG("f5g-earth-deflection.svg",
            alt="Two arrows heading north. In the Northern Hemisphere the actual path bends to the right. In the Southern Hemisphere it bends to the left. There is no deflection at the equator.",
            caption="Figure 2. Deflection. 'Right' and 'left' mean right and left of the direction in which the wind or current is moving."),
        T("This has big effects. Winds blowing from the south into the Northern Hemisphere bend to the right. Over Cameroon, "
          "the humid wind from the Atlantic arrives from the south-west for this reason. Ocean currents also turn: in the North Atlantic "
          "the large circulation of water goes clockwise, and in the South Atlantic it goes anticlockwise."),
        H("Worked examples: how to answer"),
        EX("Model answer 1: day and night", intro="Explain how the rotation of the earth causes day and night. [4 marks]", steps=[
            S("State the cause", text="The earth rotates on its axis once in about 24 hours."),
            S("Only half is lit", text="The Sun lights only half of the earth at a time. The lit half has day and the dark half has night."),
            S("Movement through the cycle", text="As the earth turns, each place moves from the dark side to the lit side (sunrise) and later back to the dark side (sunset)."),
            S("Conclude", text="This gives one day and one night every 24 hours. A sketch such as Figure 1 earns extra marks."),
        ]),
        EX("Model answer 2: deflection", intro="Describe the effect of the earth's rotation on winds and ocean currents. [3 marks]", steps=[
            S("State what happens", text="Winds and currents are turned from a straight path. This is called deflection."),
            S("Give the directions", text="In the Northern Hemisphere they are deflected to the right. In the Southern Hemisphere they are deflected to the left."),
            S("Add the exception", text="There is no deflection at the equator."),
        ]),
        EX("Worked example 3: calculation", intro="Through how many degrees does the earth rotate in 7 hours? [2 marks]", steps=[
            S("Rate of rotation", text="The earth rotates 15° each hour."),
            S("Multiply", math=r"7 \times 15 = 105"),
            S("State the answer", text="It rotates through 105°."),
        ]),
        MISTAKE("Saying rotation causes the seasons", "Rotation gives day and night. The seasons come from the earth's revolution and the tilt of its axis."),
        MISTAKE("Saying the Sun moves around the earth", "The Sun only seems to move. It is the earth that rotates from west to east."),
        MISTAKE("Using the wrong direction of rotation", "The earth rotates from WEST to EAST (anticlockwise from above the North Pole). The Sun seems to move from east to west."),
        QUIZ("How long does one rotation of the earth take?", ["About 12 hours", "About 24 hours", "About 7 days", "About 365 days"], 1,
             "One rotation takes about 24 hours, which is one day.",
             hint="Think of the time from one sunrise to the next.",
             feedback=["12 hours is half a rotation: day or night alone.", "", "7 days is a week, not related to rotation.", "365 days is one revolution round the Sun."]),
        QUIZ("A wind moving north in the Southern Hemisphere is deflected to the:", ["Right", "Left", "South", "It is not deflected"], 1,
             "In the Southern Hemisphere, moving winds are deflected to the left.",
             hint="Right in the north, and the opposite in the south.",
             feedback=["Right is the direction in the Northern Hemisphere.", "", "Deflection is a sideways turn, not a reversal.", "There is deflection everywhere except at the equator."]),
        TIP("Rotation and its effects appear in Paper 1 and in Paper 2 Section B as 'describe and illustrate'. A neat sketch of the earth with the "
            "Sun's rays, the day and night halves and an arrow for the direction of rotation earns marks quickly.", title="Exam link"),
        H("Practice questions"),
        PQ("Differentiate between rotation and revolution of the earth. [2 marks]", "Rotation is the spinning of the earth on its axis, once in about 24 hours. Revolution is the movement of the earth in its orbit round the Sun, once in about 365 days."),
        PQ("State the direction of rotation of the earth. [1 mark]", "From west to east (anticlockwise when seen from above the North Pole)."),
        PQ("Describe two effects of the earth's rotation. [4 marks]", "Day and night: the Sun lights half of the earth, and rotation takes each place through light and darkness once in 24 hours. Differences in time: the earth turns 15° each hour, so places on different meridians have noon at different times (local time and time zones). Also acceptable: winds and ocean currents are deflected to the right in the Northern Hemisphere and to the left in the Southern Hemisphere."),
        PQ("Through how many degrees does the earth rotate in 5 hours? [2 marks]", "15° each hour, so 5 × 15 = 75°."),
        SUM("Rotation is the earth's spin on its axis; revolution is its movement round the Sun.",
            "The earth rotates from west to east in about 24 hours, at 15° each hour.",
            "Rotation gives day and night and makes the Sun seem to rise in the east and set in the west.",
            "Rotation causes time differences between meridians and the use of time zones.",
            "Moving winds and currents are deflected right in the Northern Hemisphere and left in the Southern Hemisphere; none at the equator."),
    ],
))

# ------------------------------------------------------------------ 8. Revolution and the seasons
LESSONS.append(lesson(
    module=MODULE,
    topic=ROT,
    title="Revolution of the earth and the seasons",
    slug="earth-revolution-and-the-seasons",
    minutes=24,
    summary="The earth travels round the Sun in about 365 days with its axis tilted at 23.5 degrees. Learn how this gives the solstices and equinoxes, changing day length, the seasons, and the overhead Sun between the tropics.",
    objectives=[
        "Describe the revolution of the earth in its orbit",
        "Illustrate the solstices and equinoxes with a diagram of the earth's four positions",
        "Describe the effects of revolution: seasons and changing day length",
        "Explain the movement of the overhead Sun between the tropics",
    ],
    key_concepts=["Revolution", "Orbit", "Tilt of the axis (23.5°)", "Solstice", "Equinox", "Overhead Sun", "Seasons"],
    blocks=[
        H("Introduction"),
        T("A farmer near Bafoussam knows when to plant: the rains begin and the dry season ends in a regular pattern each year. "
          "A student in Europe sees something different: long bright days in summer and short days in winter."),
        T("Near the equator, day length changes very little all year. Further from the equator, it changes a lot. "
          "These patterns come from the earth's second movement, revolution, and from the tilt of its axis."),
        D("**Revolution** is the movement of the earth in its **orbit** round the Sun. One revolution takes about **365¼ days**. "
          "We use a year of 365 days and add one extra day (29 February) every four years to make up the quarter days.", title="Definition: revolution"),
        D("The earth's **axis** is tilted at **23.5°** from the line at right angles to the plane of its orbit. As the earth revolves, "
          "the axis always points in the same direction in space (towards the Pole Star).", title="Definition: tilt of the axis"),
        H("The earth's four positions"),
        IMG("f5g-earth-seasons-orbit.svg",
            alt="The earth at four positions round the Sun: 22 December (overhead sun at 23.5 degrees south), 21 March (equator), 21 June (23.5 degrees north) and 23 September (equator). The axis is tilted the same way in every position.",
            caption="Figure 1. The earth's orbit (not to scale). The tilt of the axis stays the same, but its direction relative to the Sun changes."),
        KEY("Solstices and equinoxes", "Dates are 'on or about' because they change by a day from year to year.", cards=[
            ["Solstice (21 June, 22 December)", "The noon Sun is overhead at its furthest from the equator: 23.5°N in June, 23.5°S in December."],
            ["Equinox (21 March, 23 September)", "The noon Sun is overhead at the equator. Day and night are equal (about 12 hours) everywhere."],
        ]),
        CODE("""Date            Overhead Sun    Northern Hemisphere   Southern Hemisphere
--------------  --------------  --------------------  --------------------
21 March        Equator         Spring (equinox)      Autumn (equinox)
21 June         23.5°N          Summer (solstice)     Winter (solstice)
23 September    Equator         Autumn (equinox)      Spring (equinox)
22 December     23.5°S          Winter (solstice)     Summer (solstice)""", "text", title="The year in four positions"),
        H("The overhead Sun and the tropics"),
        T("During the year the place where the noon Sun is directly overhead moves north and south. It is overhead at the equator "
          "on 21 March, moves north to 23.5°N on 21 June, returns to the equator on 23 September, moves south to 23.5°S on 22 December, "
          "and returns north again."),
        IMG("f5g-earth-overhead-sun.svg",
            alt="A graph with months along the bottom and latitude up the side. The curve rises from the equator in March to 23.5 degrees north in June, falls to the equator in September and to 23.5 degrees south in December.",
            caption="Figure 2. The latitude of the overhead noon Sun through the year (approximate curve)."),
        T("This is why the **Tropic of Cancer (23.5°N)** and the **Tropic of Capricorn (23.5°S)** are important: they are the furthest limits "
          "of the overhead Sun. The Sun is never overhead beyond them. The Arctic and Antarctic Circles (66.5°N and S) mark the limits "
          "of 24-hour day and night. Note that 90° − 23.5° = 66.5°."),
        T("All of Cameroon (about 2°N to 13°N) lies between the tropics, so the noon Sun is overhead twice a year at every place in Cameroon: "
          "once as it moves north and once as it moves south. This is one reason why Cameroon is hot all year. Its seasons are mainly "
          "wet and dry, not hot and cold."),
        H("Effects of revolution"),
        KEY("1. The seasons", "Summer is in the hemisphere tilted TOWARDS the Sun.", cards=[
            ["Tilted towards the Sun", "The Sun is higher in the sky, its rays are more direct and days are longer: summer."],
            ["Tilted away from the Sun", "The Sun is lower in the sky, its rays are spread and days are shorter: winter."],
        ], note="The two hemispheres have opposite seasons: when it is summer in the north it is winter in the south."),
        CODE("""Latitude         Day length on 21 June    Day length on 22 December
---------------  -----------------------  -------------------------
Equator          about 12 hours           about 12 hours
Middle north     longer than 12 hours     shorter than 12 hours
Arctic Circle    24 hours of daylight     no sunrise
Middle south     shorter than 12 hours    longer than 12 hours
Antarctic Circle no sunrise               24 hours of daylight""", "text", title="2. Changing day length (all places at the equinox have about 12 hours)"),
        T("Day length changes most at high latitudes and least at the equator. At the equinoxes the day is about 12 hours everywhere."),
        MISTAKE("Thinking seasons come from distance to the Sun", "The earth is actually nearest the Sun in early January (about 147 million km) and furthest in early July (about 152 million km). Seasons come from the tilt of the axis."),
        H("Worked examples: how to answer"),
        EX("Model answer 1: summer in the north", intro="Explain why the Northern Hemisphere has summer in June. [4 marks]", steps=[
            S("Tilt and position", text="The earth's axis is tilted at 23.5°. On 21 June the North Pole is tilted towards the Sun."),
            S("Overhead Sun", text="The noon Sun is overhead at the Tropic of Cancer (23.5°N), so the Sun is high in the sky in the Northern Hemisphere."),
            S("Effect on heat", text="The Sun's rays are concentrated on a small area and pass through less air, so the heating is greater."),
            S("Day length", text="Days are longer than nights, so there is more time for heating. A sketch like Figure 1 helps."),
        ]),
        EX("Model answer 2: twice overhead", intro="Explain why the noon Sun is overhead twice a year at Douala (about 4°N). [3 marks]", steps=[
            S("Movement of the overhead Sun", text="During the year the overhead Sun moves between 23.5°N and 23.5°S."),
            S("First crossing", text="It crosses 4°N once as it moves north (between 21 March and 21 June)."),
            S("Second crossing", text="It crosses 4°N again as it returns south (between 21 June and 23 September)."),
        ]),
        EX("Worked example 3: calculation", intro="The earth's axis is tilted at 23.5°. Calculate the latitude of the Arctic Circle. [2 marks]", steps=[
            S("Use the rule", text="The polar circles are 90° minus the tilt from the equator."),
            S("Subtract", math=r"90 - 23.5 = 66.5"),
            S("State the answer", text="The Arctic Circle is at 66.5°N."),
        ]),
        MISTAKE("Thinking the axis changes direction", "The axis always points the same way in space. It is the position of the earth in its orbit that changes what the Sun lights."),
        MISTAKE("Using northern seasons for the whole earth", "Seasons are opposite in the two hemispheres. In December it is summer in the south and winter in the north."),
        QUIZ("On about which date is the noon Sun overhead at the Tropic of Cancer?", ["21 March", "21 June", "23 September", "22 December"], 1,
             "The Sun is overhead at 23.5°N on 21 June, the June solstice.",
             hint="This is the summer solstice for the Northern Hemisphere.",
             feedback=["On 21 March it is overhead at the equator.", "", "On 23 September it is overhead at the equator.", "On 22 December it is overhead at the Tropic of Capricorn."]),
        QUIZ("Which best explains why there are seasons?", [
            "The earth moves closer to and further from the Sun",
            "The earth's axis is tilted and the earth revolves round the Sun",
            "The earth rotates once in 24 hours",
            "The Sun moves north and south"], 1,
             "The tilted axis and the revolution together change which hemisphere is tilted towards the Sun.",
             hint="Which two things are needed: a tilt and a movement round the Sun?",
             feedback=["The distance changes only slightly and the earth is closest in January.", "", "Rotation gives day and night, not seasons.", "The Sun does not move north and south: it only appears to as the earth moves in its orbit."]),
        TIP("Revolution, the solstices, equinoxes and seasons are among the most tested ideas in Paper 1 and Paper 2 Section B. Always draw the four positions of the earth, "
            "with the tilted axis and the Sun, and label the dates and the overhead Sun.", title="Exam link"),
        H("Practice questions"),
        PQ("Define 'revolution' of the earth. [2 marks]", "Revolution is the movement of the earth in its orbit round the Sun. One revolution takes about 365¼ days (a year)."),
        PQ("State the latitude where the noon Sun is overhead on (a) 21 March and (b) 22 December. [2 marks]", "(a) The equator (0°). (b) The Tropic of Capricorn (23.5°S)."),
        PQ("Explain why the Southern Hemisphere has summer in December. [4 marks]", "The earth's axis is tilted at 23.5° and always points in the same direction. In December the South Pole is tilted towards the Sun. The overhead Sun is at 23.5°S, the Sun is high in the sky in the south, days are longer and heating is greater, so it is summer in the Southern Hemisphere."),
        PQ("Describe what happens to day length at the Arctic Circle on 21 June. [2 marks]", "At the Arctic Circle the Sun does not set on 21 June, so there are 24 hours of daylight."),
        SUM("Revolution is the earth's movement in its orbit round the Sun in about 365¼ days.",
            "The axis is tilted at 23.5° and always points the same way in space.",
            "Solstices (21 June, 22 December) have the Sun overhead at 23.5°N and S. Equinoxes (21 March, 23 September) have it overhead at the equator.",
            "The tilt and the revolution cause the seasons and changing day length: summer is in the hemisphere tilted towards the Sun.",
            "The overhead Sun moves between the tropics. Cameroon lies between the tropics, so the Sun is overhead there twice a year."),
    ],
))
