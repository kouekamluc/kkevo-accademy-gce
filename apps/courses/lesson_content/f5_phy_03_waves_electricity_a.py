"""Form 5 Physics (O Level 0580): Waves, Optics & Sound, and the first four topics of Electricity & Magnetism.
Draft content for review in the studio."""
from .dsl import *  # noqa: F403

COURSE = ("physics", "form-5")

WAVES = "Waves, Optics & Sound"
ELEC = "Electricity & Magnetism"

LESSONS = [
    # ------------------------------------------------------------------ 1. Types of wave and wave terms
    lesson(
        module=WAVES,
        topic="Wave motion and the wave equation",
        title="Waves, wave types and wave terms",
        slug="phc-wave-types-and-terms",
        minutes=20,
        summary="A wave carries energy without carrying matter. Learn transverse and longitudinal waves and the words amplitude, wavelength, frequency and period.",
        objectives=[
            "Explain that a wave transfers energy without moving the material along",
            "Tell transverse waves from longitudinal waves and give examples",
            "Define amplitude, wavelength, frequency and period",
            "Use T = 1/f and f = 1/T with correct units",
        ],
        key_concepts=["Wave", "Transverse wave", "Longitudinal wave", "Amplitude", "Wavelength", "Frequency", "Period"],
        blocks=[
            H("Introduction"),
            T("Stand on the beach at Limbe and watch a cork or a fishing float on the sea. Waves come in, but the float does not "
              "travel to the shore. It only moves **up and down** in nearly the same place."),
            T("This shows the main idea of this lesson: a wave moves **energy** from one place to another, but the material "
              "(the water) does not travel with it. Sound, light, radio waves and the waves on a guitar string all work this way."),
            H("What is a wave?"),
            D("A **wave** is a disturbance that carries energy from one place to another without moving the material "
              "of the medium along with it. The **medium** is the material the wave travels through, such as water, air or a rope.",
              title="Definition: wave"),
            T("Some waves need a medium (water waves, sound). Light and other electromagnetic waves can travel through empty space."),
            KEY("Two types of wave", "The difference is how the particles move compared with the direction the wave travels.",
                cards=[["Transverse", "Particles vibrate at **right angles** to the direction of travel. Examples: water ripples, light, waves on a rope."],
                       ["Longitudinal", "Particles vibrate **along** (parallel to) the direction of travel. Examples: sound, a pushed and pulled spring."]]),
            IMG("f5ph-c-wave-transverse-longitudinal.svg",
                "Top: a transverse wave drawn as a sine curve with the wavelength measured from crest to crest and the amplitude measured from the centre line to a crest. Bottom: a longitudinal wave drawn as vertical lines that are bunched in compressions and spread out in rarefactions.",
                "Figure 1. A transverse wave (top) and a longitudinal wave (bottom)."),
            T("In a longitudinal wave the particles are squeezed together in places called **compressions** and spread apart in "
              "places called **rarefactions**. In a transverse wave the highest points are **crests** and the lowest points are **troughs**."),
            H("The words used to describe a wave"),
            D("The **amplitude** is the maximum distance of a point on the wave from its rest (centre) position. "
              "It is measured from the centre line to a crest, not from trough to crest. Larger amplitude means more energy.",
              title="Amplitude", note="Unit: metre (m)."),
            D(r"The **wavelength** $\lambda$ is the distance between two neighbouring points that are in step, for example from "
              "one crest to the next crest, or from one compression to the next compression.",
              title="Wavelength", note="Unit: metre (m). The symbol is the Greek letter lambda."),
            D("The **frequency** $f$ is the number of complete waves passing a point (or complete vibrations made by the source) in one second. "
              "The **period** $T$ is the time for one complete wave.",
              title="Frequency and period", formula=r"T = \dfrac{1}{f} \qquad f = \dfrac{1}{T}",
              note="Frequency is measured in hertz (Hz). 1 Hz means one wave per second. Period is measured in seconds (s)."),
            TIP(r"To find a frequency, count **complete waves** and divide by the time in seconds: "
                r"$f = \dfrac{\text{number of waves}}{\text{time}}$."),
            H("Worked examples"),
            EX("Worked example 1: frequency from counting", intro=(
                "A fishing float at Limbe bobs up and down 12 complete times in 30 seconds. Find its frequency and its period."),
               steps=[
                   S("Frequency = waves per second", math=r"f = \dfrac{12}{30\ \text{s}} = 0.40\ \text{Hz}"),
                   S("Period = 1 divided by the frequency", math=r"T = \dfrac{1}{f} = \dfrac{1}{0.40} = 2.5\ \text{s}"),
                   S("Answer", text="Frequency 0.40 Hz, period 2.5 s."),
               ], check=r"12 \times 2.5\ \text{s} = 30\ \text{s}"),
            EX("Worked example 2: the mains supply", intro=(
                "The electricity from a mains socket in Cameroon alternates 50 times every second (frequency 50 Hz). "
                "What is the period of one cycle?"),
               steps=[
                   S("Write the formula", math=r"T = \dfrac{1}{f}"),
                   S("Substitute", math=r"T = \dfrac{1}{50\ \text{Hz}} = 0.020\ \text{s}"),
                   S("Answer", text="One cycle takes 0.020 s (20 milliseconds)."),
               ]),
            EX("Worked example 3: wavelength from a rope", intro=(
                "Two students shake a rope. The distance from the first crest to the fourth crest is 1.8 m. Find the wavelength."),
               steps=[
                   S("Count the gaps, not the crests", text="From crest 1 to crest 4 there are 3 complete wavelengths."),
                   S("Divide", math=r"\lambda = \dfrac{1.8\ \text{m}}{3} = 0.60\ \text{m}"),
                   S("Answer", text="The wavelength is 0.60 m."),
               ]),
            MISTAKE("Amplitude is not trough to crest", "The amplitude is measured from the **centre line** to a crest (or to a trough). "
                    "The distance from trough to crest is **twice** the amplitude."),
            MISTAKE("Waves do not carry the medium", "Water waves do not push water along to the beach, and sound does not blow air from "
                    "the speaker to your ear. The particles only vibrate about a fixed position. The **energy** moves along."),
            QUIZ("Which of these is a longitudinal wave?", ["Light from the sun", "Ripples on a pond", "Sound from a drum", "A wave on a rope"], 2,
                 "In sound the air particles vibrate back and forth along the direction the sound travels, so it is longitudinal.",
                 hint="Think of the compressions and rarefactions in air.",
                 feedback=["Light is a transverse electromagnetic wave.", "Water ripples are transverse: the water moves up and down.", "",
                           "A rope wave is transverse: the rope moves at right angles to the direction of the wave."]),
            QUIZ("A source vibrates 200 times in 4 seconds. What is its frequency?", ["0.02 Hz", "50 Hz", "800 Hz", "200 Hz"], 1,
                 "Frequency = waves per second = 200 / 4 = 50 Hz.",
                 hint="Divide the number of vibrations by the time in seconds.",
                 feedback=["You divided time by vibrations (4 / 200). That is nearly the period, not the frequency.", "",
                           "You multiplied 200 by 4. Frequency is a rate, so divide.", "200 is the number of vibrations, not the number per second."]),
            TIP("Where this appears: waves are tested in Paper 1 (multiple choice), often with a diagram and a short calculation, "
                "and in Paper 2 (structured questions). Always write the unit: Hz for frequency, s for period, m for wavelength."),
            PQ("State two differences between a transverse wave and a longitudinal wave.",
               "In a transverse wave the particles vibrate at right angles to the direction of travel; in a longitudinal wave they vibrate "
               "parallel to the direction of travel. A transverse wave has crests and troughs; a longitudinal wave has compressions and rarefactions."),
            PQ("A student counts 45 complete ripples passing a stone in 15 s. Calculate the frequency and the period of the ripples.",
               r"$f = \dfrac{45}{15} = 3.0$ Hz. $T = \dfrac{1}{3.0} = 0.33$ s."),
            PQ("The period of a vibrating tuning fork is 0.0025 s. Find its frequency.",
               r"$f = \dfrac{1}{T} = \dfrac{1}{0.0025} = 400$ Hz."),
            PQ("A wave has crests 0.40 m apart and the centre line to a crest is 0.05 m. State its wavelength and amplitude.",
               "Wavelength = 0.40 m (crest to crest). Amplitude = 0.05 m (centre line to crest)."),
            SUM("A wave transfers energy without transferring the medium.",
                "Transverse waves vibrate at right angles to the direction of travel; longitudinal waves vibrate along it.",
                "Amplitude is centre line to crest; wavelength is crest to crest (or compression to compression).",
                r"Frequency $f$ is waves per second (Hz) and period $T$ is time for one wave (s): $T = 1/f$."),
        ],
    ),
    # ------------------------------------------------------------------ 2. The wave equation
    lesson(
        module=WAVES,
        topic="Wave motion and the wave equation",
        title="The wave equation v = f lambda",
        slug="phc-wave-equation",
        minutes=22,
        summary=r"The speed of a wave equals frequency times wavelength, $v = f\lambda$. Use it with the right units for sound, water waves and radio waves.",
        objectives=[
            "Explain why the speed of a wave is v = f x wavelength",
            "Use v = f lambda to find speed, frequency or wavelength",
            "Convert kHz and MHz into hertz before calculating",
            "Explain why a higher frequency means a shorter wavelength when the speed stays the same",
        ],
        key_concepts=["Wave speed", "Wave equation", "Frequency", "Wavelength", "Hertz"],
        blocks=[
            H("Introduction"),
            T("Turn the dial of a radio and you move from one station to another. Each station sends radio waves of a different "
              "**frequency**. Yet every radio wave travels at the same speed in air. How can that be?"),
            T("The answer is the **wave equation**. It joins three things: speed, frequency and wavelength. Once you know two of them, you can find the third."),
            H("Where the equation comes from"),
            T("In one period $T$, a wave moves forward exactly one wavelength $\\lambda$. Speed is distance divided by time, so"),
            F(r"v = \dfrac{\lambda}{T}"),
            T(r"But $\dfrac{1}{T} = f$, so we can write the speed in a second way."),
            D("The speed $v$ of a wave equals its frequency $f$ multiplied by its wavelength $\\lambda$.",
              title="The wave equation", formula=r"v = f \lambda",
              note="Units: v in metres per second (m/s), f in hertz (Hz), wavelength in metres (m)."),
            KEY("Three forms of the same equation", "Cover the quantity you want with your finger.",
                cards=[["Find the speed", r"$v = f\lambda$"],
                       ["Find the wavelength", r"$\lambda = \dfrac{v}{f}$"],
                       ["Find the frequency", r"$f = \dfrac{v}{\lambda}$"]]),
            T("The speed of a wave depends on the **medium** (and on its temperature). It does **not** depend on the frequency or on the amplitude. "
              "So if the source vibrates faster, the frequency goes up and the wavelength gets shorter, but the speed stays the same."),
            KEY("Units: change to hertz and metres first", "Many questions give the frequency in kilohertz or megahertz.",
                cards=[["kilohertz", r"1 kHz = 1000 Hz $= 10^3$ Hz"],
                       ["megahertz", r"1 MHz = 1 000 000 Hz $= 10^6$ Hz"]],
                note="Speed of sound in air about 340 m/s. Speed of radio waves and light in air or vacuum about $3.0 \\times 10^{8}$ m/s."),
            H("Worked examples"),
            EX("Worked example 1: a radio wave", intro=(
                "An FM radio station broadcasts at a frequency of 100 MHz. Radio waves travel at $3.0 \\times 10^{8}$ m/s. "
                "Find the wavelength."),
               steps=[
                   S("Change the frequency to hertz", math=r"f = 100\ \text{MHz} = 100 \times 10^{6} = 1.0 \times 10^{8}\ \text{Hz}"),
                   S("Rearrange", math=r"\lambda = \dfrac{v}{f}"),
                   S("Substitute", math=r"\lambda = \dfrac{3.0 \times 10^{8}}{1.0 \times 10^{8}} = 3.0\ \text{m}"),
                   S("Answer", text="The wavelength is 3.0 m."),
               ]),
            EX("Worked example 2: water waves", intro=(
                "Waves on a lake have a wavelength of 2.0 m and a period of 4.0 s. Find their speed."),
               steps=[
                   S("Frequency from the period", math=r"f = \dfrac{1}{T} = \dfrac{1}{4.0} = 0.25\ \text{Hz}"),
                   S("Use the wave equation", math=r"v = f\lambda = 0.25 \times 2.0 = 0.50\ \text{m/s}"),
                   S("Answer", text="The waves travel at 0.50 m/s."),
               ], check=r"\dfrac{\lambda}{T} = \dfrac{2.0}{4.0} = 0.50\ \text{m/s}"),
            EX("Worked example 3: sound", intro=(
                "A musical note has wavelength 0.68 m in air. The speed of sound in air is 340 m/s. Find the frequency of the note."),
               steps=[
                   S("Rearrange", math=r"f = \dfrac{v}{\lambda}"),
                   S("Substitute", math=r"f = \dfrac{340}{0.68} = 500\ \text{Hz}"),
                   S("Answer", text="The frequency is 500 Hz."),
               ]),
            EX("Worked example 4: changing the frequency", intro=(
                "A sound source of frequency 170 Hz makes sound of wavelength 2.0 m in air. The frequency is doubled to 340 Hz. "
                "What is the new wavelength?"),
               steps=[
                   S("The speed does not change", text="The speed is set by the air, so $v = 170 \\times 2.0 = 340$ m/s still."),
                   S("New wavelength", math=r"\lambda = \dfrac{340}{340} = 1.0\ \text{m}"),
                   S("Answer", text="Doubling the frequency halves the wavelength: 1.0 m."),
               ]),
            MISTAKE("Forgetting to convert MHz or kHz", r"If you put $f = 100$ for 100 MHz, your wavelength will be a million times too big. "
                    r"Write the frequency in hertz first: $100\ \text{MHz} = 1.0 \times 10^{8}$ Hz."),
            MISTAKE("Mixing up period and frequency", "A period is in seconds and a frequency is in hertz. If the question gives a period, find "
                    r"$f = 1/T$ first, or use $v = \lambda / T$ directly."),
            QUIZ("A wave has frequency 5 Hz and wavelength 3 m. What is its speed?", ["0.6 m/s", "8 m/s", "15 m/s", "1.7 m/s"], 2,
                 "v = f x wavelength = 5 x 3 = 15 m/s.",
                 hint="Multiply frequency and wavelength.",
                 feedback=["You divided 3 by 5. Speed is the product of f and wavelength.", "You added 5 and 3. Wave speed is a product.", "",
                           "You divided 5 by 3. Speed is the product of f and wavelength."]),
            QUIZ("The frequency of a wave on a string is doubled and the string stays the same. What happens to the wavelength?",
                 ["It doubles", "It stays the same", "It halves", "It becomes four times larger"], 2,
                 "The speed on the same string is fixed, so wavelength = v / f becomes half.",
                 hint="The speed does not change. Use wavelength = v / f.",
                 feedback=["That would need the speed to double as well.", "The wavelength changes when the frequency changes and the speed is fixed.", "",
                           "You doubled twice. Doubling the frequency halves the wavelength."]),
            TIP("Where this appears: the wave equation is one of the most common calculations in waves questions, in Paper 1 and Paper 2. "
                "Examiners expect the unit on the answer: m/s, Hz or m."),
            PQ("Ripples on a pond have a frequency of 8.0 Hz and a wavelength of 0.050 m. Calculate their speed.",
               r"$v = f\lambda = 8.0 \times 0.050 = 0.40$ m/s."),
            PQ(r"A radio station broadcasts at 600 kHz. Radio waves travel at $3.0 \times 10^{8}$ m/s. Calculate the wavelength.",
               r"$f = 600\ \text{kHz} = 6.0 \times 10^{5}$ Hz. $\lambda = \dfrac{3.0 \times 10^{8}}{6.0 \times 10^{5}} = 500$ m."),
            PQ("A sound of frequency 440 Hz travels at 340 m/s in air and 1500 m/s in water. Find the wavelength in each and say what stays the same.",
               r"In air: $\lambda = 340 / 440 = 0.77$ m. In water: $\lambda = 1500 / 440 = 3.4$ m. The frequency (440 Hz) stays the same; the speed and wavelength change."),
            SUM(r"Wave speed $v = f\lambda$, with $v$ in m/s, $f$ in Hz and $\lambda$ in m.",
                "The speed depends on the medium, not on frequency, so a higher frequency gives a shorter wavelength.",
                "Change kHz and MHz to hertz before you calculate.",
                r"If you are given the period, use $f = 1/T$."),
        ],
    ),
    # ------------------------------------------------------------------ 3. Wave properties
    lesson(
        module=WAVES,
        topic="Wave properties",
        title="Reflection, refraction, diffraction and interference of waves",
        slug="phc-wave-properties",
        minutes=24,
        summary="All waves can be reflected, refracted, diffracted and made to interfere. Learn what each word means and which of speed, wavelength and frequency change.",
        objectives=[
            "Define reflection, refraction, diffraction and interference",
            "State which of speed, wavelength and frequency change in each case",
            "Explain why diffraction is largest when the gap is about one wavelength",
            "State the conditions for constructive and destructive interference",
        ],
        key_concepts=["Reflection", "Refraction", "Diffraction", "Interference", "Ripple tank", "Path difference"],
        blocks=[
            H("Introduction"),
            T("You are inside a classroom with the door half open. You cannot see the teacher who is standing in the corridor, but you "
              "can hear every word. Light and sound are both waves, so why does sound reach you and light does not?"),
            T("The answer is a wave property called **diffraction**. In this lesson you meet four properties that **every** kind of wave "
              "shows: reflection, refraction, diffraction and interference. A **ripple tank** (a shallow tray of water with a vibrating dipper) "
              "is the standard way to see them."),
            H("Reflection and refraction"),
            D("**Reflection** is the bouncing of a wave back from a surface. The angle of incidence equals the angle of reflection.",
              title="Reflection"),
            D("**Refraction** is the change in the **speed** of a wave when it passes from one medium into another. If the wave meets the "
              "boundary at an angle, its direction changes as well.",
              title="Refraction"),
            T("When water waves move from deep water into shallow water they slow down. The frequency is fixed by the source, so from "
              r"$v = f\lambda$ the **wavelength becomes shorter** too. The waves bunch up closer together."),
            H("Diffraction"),
            D("**Diffraction** is the spreading of a wave as it passes through a gap or round the edge of an obstacle.",
              title="Diffraction"),
            IMG("f5ph-c-wave-diffraction.svg",
                "Two ripple-tank pictures. On the left, straight waves meet a wide gap and pass through almost unchanged. On the right, straight waves meet a gap about one wavelength wide and spread out as semicircles on the far side.",
                "Figure 1. Diffraction is greatest when the gap is about the same size as the wavelength."),
            T("Diffraction is **largest** when the size of the gap is about the **same as the wavelength**. A wide gap gives very little "
              "spreading. During diffraction the **speed, frequency and wavelength do not change**: only the direction of the wave changes."),
            T("Now we can answer the classroom puzzle. Sound has a wavelength of about 1 metre, which is close to the width of the doorway, "
              "so it spreads round the corner. Light has a wavelength of less than one thousandth of a millimetre, far smaller than the door, "
              "so it hardly diffracts at all and travels in straight lines."),
            H("Interference"),
            D("**Interference** happens when two (or more) waves meet and their effects add. Where the waves arrive in step, "
              "they make a bigger wave (**constructive** interference). Where they arrive out of step, they cancel (**destructive** interference).",
              title="Interference"),
            IMG("f5ph-c-wave-interference.svg",
                "Circular waves spreading from two sources S1 and S2 that are one above the other. The crests overlap at amber dots, which lie along green lines running out to the right from the sources.",
                "Figure 2. Two sources make a pattern. Along the green lines crest meets crest."),
            KEY("The conditions for interference", r"The **path difference** is how much farther one wave has travelled than the other to reach the same point. $\lambda$ is the wavelength.",
                cards=[["Constructive (loud, big wave)", r"Path difference $= 0,\ \lambda,\ 2\lambda,\ 3\lambda \dots$ (a whole number of wavelengths)"],
                       ["Destructive (quiet, calm water)", r"Path difference $= \tfrac{1}{2}\lambda,\ \tfrac{3}{2}\lambda,\ \tfrac{5}{2}\lambda \dots$ (an odd number of half wavelengths)"]]),
            CODE("""Property      Speed     Wavelength   Frequency
Reflection    same      same         same
Refraction    changes   changes      same
Diffraction   same      same         same""", "text", title="What changes?"),
            H("Worked examples"),
            EX("Worked example 1: refraction of water waves", intro=(
                "In a ripple tank, waves of frequency 4.0 Hz travel at 0.32 m/s in deep water. They move onto a shallow part where the "
                "speed is 0.20 m/s. Find the wavelength in the deep and in the shallow part."),
               steps=[
                   S("Deep part", math=r"\lambda = \dfrac{v}{f} = \dfrac{0.32}{4.0} = 0.080\ \text{m}"),
                   S("The frequency does not change at the boundary", text="It is still 4.0 Hz."),
                   S("Shallow part", math=r"\lambda = \dfrac{0.20}{4.0} = 0.050\ \text{m}"),
                   S("Answer", text="Deep: 0.080 m. Shallow: 0.050 m. The wavelength is shorter where the wave is slower."),
               ]),
            EX("Worked example 2: will it diffract?", intro=(
                "A sound of frequency 340 Hz travels at 340 m/s. It passes through a doorway 1.0 m wide. Will it diffract a lot? "
                "Visible light has a wavelength of about $5 \\times 10^{-7}$ m. Will light diffract a lot through the same door?"),
               steps=[
                   S("Wavelength of the sound", math=r"\lambda = \dfrac{340}{340} = 1.0\ \text{m}"),
                   S("Compare with the gap", text="The gap (1.0 m) is about the same size as the wavelength (1.0 m), so the sound diffracts a lot."),
                   S("Compare light", text=r"Light's wavelength is about $5 \times 10^{-7}$ m. The gap is two million times larger, so light diffracts almost not at all."),
               ]),
            EX("Worked example 3: two loudspeakers", intro=(
                "Two loudspeakers send out the same note of wavelength 1.0 m, exactly in step. A listener stands at a point 3.0 m from one speaker "
                "and 3.5 m from the other. Does the listener hear a loud or a quiet sound?"),
               steps=[
                   S("Path difference", math=r"3.5 - 3.0 = 0.5\ \text{m}"),
                   S("Compare with the wavelength", math=r"0.5\ \text{m} = \tfrac{1}{2}\lambda"),
                   S("Answer", text="Half a wavelength means destructive interference, so the listener hears a very quiet sound."),
               ]),
            MISTAKE("Diffraction does not change the wavelength", "Many candidates write that the wavelength changes when a wave diffracts. "
                    "It does not: the speed, frequency and wavelength stay the same and only the direction changes. "
                    "It is **refraction** that changes the speed and wavelength."),
            MISTAKE("Destructive does not destroy energy", "Where waves cancel, the energy is not lost. It goes to the places where the waves add up "
                    "(the loud places)."),
            QUIZ("Water waves move from deep water into shallow water. Which quantity does NOT change?", ["Wave speed", "Wavelength", "Frequency", "Direction (if the waves meet the boundary at an angle)"], 2,
                 "The frequency is fixed by the source. The speed and wavelength both decrease in shallow water.",
                 hint="Which quantity is decided by the source of the waves?",
                 feedback=["The speed decreases in shallow water.", "From v = f x wavelength, a smaller v with the same f gives a smaller wavelength.", "",
                           "The direction does change when the waves arrive at an angle."]),
            QUIZ("When is diffraction at a gap biggest?", ["Gap much wider than the wavelength", "Gap about equal to the wavelength", "Gap much narrower than the wavelength", "It does not depend on the gap"], 1,
                 "The spreading is greatest when the gap is about one wavelength wide.",
                 hint="Think of sound spreading through a door of width about 1 m.",
                 feedback=["A wide gap lets the waves pass almost straight through.", "",
                           "A very narrow gap lets very little through, though what does pass does spread. The best spreading is at about one wavelength.",
                           "It depends strongly on the gap compared with the wavelength."]),
            TIP("Where this appears: wave properties are tested in Paper 1 (which quantity changes?) and in Paper 2 (define diffraction, "
                "describe a ripple-tank experiment, explain interference). Learn the exact definitions and say that the **wavelength is unchanged** in diffraction."),
            PQ("Define diffraction of a wave and state what happens to the wavelength during diffraction.",
               "Diffraction is the spreading of a wave as it passes through a gap or round an obstacle. The wavelength does not change."),
            PQ("Water waves of frequency 5.0 Hz and speed 0.30 m/s move into shallower water where their speed is 0.15 m/s. Find the new wavelength.",
               r"$\lambda = v/f = 0.15 / 5.0 = 0.030$ m (it was 0.060 m)."),
            PQ("Two coherent sources give waves of wavelength 0.40 m. State the smallest path difference (other than zero) that gives constructive interference "
               "and the smallest that gives destructive interference.",
               "Constructive: one whole wavelength, 0.40 m. Destructive: half a wavelength, 0.20 m."),
            PQ("Explain why you can hear someone talking round a corner but cannot see them.",
               "Sound has a wavelength (about 1 m) similar to the size of doorways and corners, so it diffracts. Light has a very small wavelength, so it diffracts "
               "almost not at all and travels in straight lines."),
            SUM("Reflection, refraction, diffraction and interference happen with all waves.",
                "Refraction changes speed and wavelength; frequency stays the same.",
                "Diffraction is the spreading of a wave at a gap or edge: wavelength, speed and frequency do not change, and the effect is biggest when the gap is about one wavelength.",
                "Constructive interference: path difference is a whole number of wavelengths. Destructive: an odd number of half wavelengths."),
        ],
    ),
    # ------------------------------------------------------------------ 4. Light rays and plane mirrors
    lesson(
        module=WAVES,
        topic="Reflection of light and mirrors",
        title="Light rays, shadows and plane mirrors",
        slug="phc-plane-mirrors",
        minutes=22,
        summary="Light travels in straight lines. Use the law of reflection, i = r, to find where a plane mirror sends a ray and where its image appears.",
        objectives=[
            "Explain shadows and the pinhole camera using straight-line travel of light",
            "State and use the laws of reflection, measuring angles from the normal",
            "Describe the image formed by a plane mirror",
            "Find image distances and how the reflected ray turns when a mirror rotates",
        ],
        key_concepts=["Rectilinear propagation", "Ray", "Normal", "Law of reflection", "Virtual image", "Lateral inversion"],
        blocks=[
            H("Introduction"),
            T("At a barber's shop in Douala you look into a big mirror and see yourself sitting **behind** the glass. But there is "
              "only a wall behind the mirror. Where does the person you see come from?"),
            T("This lesson explains how mirrors work. First we need one simple fact about light."),
            H("Light travels in straight lines"),
            D("Light travels in **straight lines** in a transparent material that is the same all the way through. This is called "
              "**rectilinear propagation**. A **ray** is a thin straight line with an arrow that shows the direction light travels. "
              "A **beam** is a group of rays.",
              title="Rectilinear propagation"),
            T("Evidence: you cannot see round a corner, and the light from a torch makes a straight beam in dusty air. "
              "Shadows form because the light is blocked: a small source gives a sharp shadow, and a large source gives a shadow with "
              "a dark centre (**umbra**) and a lighter edge (**penumbra**). A solar eclipse happens when the Moon blocks the Sun's rays and its shadow falls on the Earth."),
            T("A **pinhole camera** also uses straight lines. Light from the top of a tree passes through the tiny hole and lands on the "
              "**bottom** of the screen, and light from the bottom lands on the top. So the image is upside down (inverted)."),
            H("The laws of reflection"),
            D("When a ray hits a smooth surface it bounces off. The **normal** is a line drawn at $90^\\circ$ to the surface at the point where the ray hits. "
              "Angles are always measured from the normal, never from the mirror.",
              title="Normal"),
            D("Law 1: the incident ray, the reflected ray and the normal all lie in the same plane. "
              "Law 2: the **angle of incidence $i$ equals the angle of reflection $r$**.",
              title="Laws of reflection", formula=r"i = r"),
            IMG("f5ph-c-plane-mirror-reflection.svg",
                "A ray comes down from the upper left to a horizontal mirror and bounces up to the upper right. A dashed vertical normal stands at the point of reflection. Equal arcs show i on the left of the normal and r on the right, both marked 40 degrees.",
                "Figure 1. The angle of incidence i and the angle of reflection r are measured from the normal."),
            T("A mirror or a polished surface gives **regular reflection**: parallel rays stay parallel, so you see a clear image. "
              "A rough surface such as paper or a wall gives **diffuse reflection**: the rays scatter in all directions, so you see the surface "
              "but no image. This is how you can see a non-shining object from any side."),
            H("The image in a plane mirror"),
            IMG("f5ph-c-plane-mirror-image.svg",
                "An object P in front of a vertical plane mirror. A ray from P reflects into an eye. The reflected ray, traced backwards with a dashed line, meets at the image P-prime, which is behind the mirror at the same distance d as the object is in front.",
                "Figure 2. The image is as far behind the mirror as the object is in front."),
            KEY("Image formed by a plane mirror", "Remember these five properties.",
                cards=[["Virtual", "It cannot be caught on a screen. The light only **seems** to come from it."],
                       ["Upright and same size", "The image is the same height as the object."],
                       ["Same distance", "The image is as far behind the mirror as the object is in front of it."],
                       ["Laterally inverted", "Left and right are swapped. Your right hand looks like the image's left hand. This is why AMBULANCE is written back to front on the front of the vehicle."]]),
            H("Worked examples"),
            EX("Worked example 1: angle with the mirror", intro=(
                "A ray hits a plane mirror and makes an angle of $30^\\circ$ with the **surface** of the mirror. Find the angle of incidence, the angle of reflection "
                "and the angle between the incident ray and the reflected ray."),
               steps=[
                   S("Measure from the normal", math=r"i = 90^\circ - 30^\circ = 60^\circ"),
                   S("Law of reflection", math=r"r = i = 60^\circ"),
                   S("Angle between the two rays", math=r"i + r = 60^\circ + 60^\circ = 120^\circ"),
                   S("Answer", text="i = 60 degrees, r = 60 degrees, and the rays are 120 degrees apart."),
               ]),
            EX("Worked example 2: distances to the image", intro=(
                "Mimi stands 2.0 m in front of a plane mirror. (a) How far is her image from the mirror? (b) How far is she from her image? "
                "(c) She steps 0.5 m towards the mirror. How far is she now from her image?"),
               steps=[
                   S("(a) Image distance equals object distance", text="The image is 2.0 m behind the mirror."),
                   S("(b) Add the two distances", math=r"2.0 + 2.0 = 4.0\ \text{m}"),
                   S("(c) New distance to the mirror", math=r"2.0 - 0.5 = 1.5\ \text{m}"),
                   S("New distance to the image", math=r"1.5 + 1.5 = 3.0\ \text{m}"),
                   S("Answer", text="(a) 2.0 m, (b) 4.0 m, (c) 3.0 m."),
               ], check=r"\text{The distance to the image changed by } 4.0 - 3.0 = 1.0\ \text{m, twice her step of } 0.5\ \text{m}"),
            EX("Worked example 3: turning the mirror", intro=(
                "A ray hits a plane mirror with an angle of incidence of $30^\\circ$. The mirror is turned through $10^\\circ$ while the incident ray stays still. "
                "By how many degrees does the reflected ray turn?"),
               steps=[
                   S("Before turning", text=r"$i = 30^\circ$, so the angle between incident and reflected rays is $2 \times 30^\circ = 60^\circ$."),
                   S("After turning by 10 degrees", text=r"The normal turns too, so $i = 40^\circ$ and the angle between the rays is $2 \times 40^\circ = 80^\circ$."),
                   S("Change in the reflected ray", math=r"80^\circ - 60^\circ = 20^\circ"),
                   S("Answer", text="The reflected ray turns through 20 degrees, which is **twice** the turn of the mirror."),
               ]),
            T("A **periscope** uses two plane mirrors, each at $45^\\circ$ to the tube. It lets you see over a wall or a crowd, or look out of a submarine."),
            MISTAKE("Measuring from the mirror", "The angles $i$ and $r$ are measured from the **normal**, not from the surface. If a question gives the angle with the mirror, "
                    r"subtract it from $90^\circ$ first."),
            MISTAKE("Thinking the image is real", "The image in a plane mirror is virtual. You cannot put a screen behind the mirror and see it. "
                    "A virtual image is drawn with **dashed** lines behind the mirror."),
            QUIZ("A ray hits a plane mirror at an angle of incidence of 25 degrees. What is the angle between the reflected ray and the mirror surface?", ["25 degrees", "50 degrees", "65 degrees", "90 degrees"], 2,
                 "r = i = 25 degrees from the normal, so the angle with the surface is 90 - 25 = 65 degrees.",
                 hint="Angles in the law of reflection are measured from the normal. How far is the normal from the surface?",
                 feedback=["That is the angle with the normal, not with the mirror.", "That is the angle between the two rays (i + r).", "",
                           "That is the angle between the normal and the surface."]),
            QUIZ("A girl stands 3.0 m from a plane mirror and walks 1.0 m towards it. How far is she now from her image?", ["2.0 m", "4.0 m", "5.0 m", "6.0 m"], 1,
                 "She is 2.0 m from the mirror, so her image is 2.0 m behind it: 2.0 + 2.0 = 4.0 m.",
                 hint="The image is as far behind the mirror as she is in front.",
                 feedback=["That is her distance from the mirror, not from the image.", "",
                           "5.0 m would be 3.0 + 2.0. The image is the same distance behind as she is in front.", "That is the distance before she moved (3.0 + 3.0)."]),
            TIP("Where this appears: reflection and plane mirrors are tested in Paper 1 (measure or calculate an angle, identify image properties) and in "
                "Paper 2 (complete a ray diagram). The Board's examiners ask candidates to practise drawing ray diagrams: use a sharp pencil and a ruler, and put arrows on the rays."),
            PQ("State the laws of reflection of light.",
               "(1) The incident ray, the reflected ray and the normal at the point of incidence all lie in the same plane. (2) The angle of incidence equals the angle of reflection."),
            PQ("A man 1.8 m from a plane mirror sees his image. Find the distance between the man and his image. He then moves 0.6 m away from the mirror. Find the new distance between him and his image.",
               "First distance = 1.8 + 1.8 = 3.6 m. New distance from the mirror = 2.4 m, so he is 2.4 + 2.4 = 4.8 m from his image."),
            PQ("List three properties of the image in a plane mirror.",
               "Any three of: virtual, upright, the same size as the object, as far behind the mirror as the object is in front, laterally inverted."),
            PQ("A ray makes an angle of 35 degrees with a plane mirror. By how many degrees must the mirror be turned so that the reflected ray turns through 20 degrees?",
               "The reflected ray turns twice as much as the mirror, so the mirror must turn through 10 degrees."),
            SUM("Light travels in straight lines. This explains shadows and the pinhole camera.",
                "The law of reflection: $i = r$, with both angles measured from the normal.",
                "A plane mirror gives a virtual, upright, same-size, laterally inverted image as far behind the mirror as the object is in front.",
                "If a mirror turns through an angle, the reflected ray turns through twice that angle."),
        ],
    ),
    # ------------------------------------------------------------------ 5. Curved mirrors
    lesson(
        module=WAVES,
        topic="Reflection of light and mirrors",
        title="Concave and convex mirrors",
        slug="phc-curved-mirrors",
        minutes=25,
        summary="Concave mirrors focus parallel rays at a point and can make real or virtual images; convex mirrors always make small virtual images. Draw the rays and use 1/f = 1/u + 1/v.",
        objectives=[
            "Name the pole, centre of curvature, principal axis and principal focus of a curved mirror",
            "Draw ray diagrams for concave and convex mirrors using the standard rays",
            "State the nature of the image for each object position",
            "Use f = R/2 and 1/f = 1/u + 1/v to find image distance and magnification",
        ],
        key_concepts=["Concave mirror", "Convex mirror", "Principal focus", "Centre of curvature", "Real and virtual image", "Magnification"],
        blocks=[
            H("Introduction"),
            T("A solar cooker in northern Cameroon is a curved shiny dish. It collects the Sun's rays and sends them to one small spot where a pot "
              "can be heated. The wing mirror of a taxi in Yaounde is also curved, but it does the opposite: it spreads the rays so the driver sees a wide view."),
            T("These are two kinds of curved mirror. They are parts of a **sphere**: the inside of a ball is **concave**, the outside of a ball is **convex**."),
            H("Words used for curved mirrors"),
            D("**Pole (P)**: the centre of the mirror surface. **Principal axis**: the straight line through the pole and the centre of curvature. "
              "**Centre of curvature (C)**: the centre of the sphere the mirror is part of. **Radius of curvature (R)**: the distance PC.",
              title="Mirror words"),
            D("**Principal focus (F)** of a concave mirror: the point where rays parallel to the principal axis meet after reflection. "
              "The **focal length $f$** is the distance from the pole to the principal focus. It is **half** the radius of curvature.",
              title="Focal length", formula=r"f = \dfrac{R}{2}"),
            T("In a **convex** mirror, rays parallel to the axis spread out after reflection. They seem to come from a point behind the mirror. "
              "That point is its (virtual) principal focus."),
            H("Drawing ray diagrams"),
            T("To find the image of a point on an object, draw two of these three rays from that point. Where they meet (or seem to meet) is the image of the point."),
            KEY("Three rays for a concave mirror", "Use a ruler, and put an arrow on every ray.",
                cards=[["Ray 1", "Parallel to the principal axis. It reflects **through F**."],
                       ["Ray 2", "Through F. It reflects **parallel** to the axis."],
                       ["Ray 3", "Through C. It hits the mirror along the normal, so it reflects **back along itself**."]]),
            IMG("f5ph-c-concave-mirror.svg",
                "A concave mirror with its axis. An object stands left of the centre of curvature C. A blue ray parallel to the axis reflects through F; an amber ray through C reflects back. They meet between F and C at a small inverted image.",
                "Figure 1. Object beyond C: the image is between F and C, real, inverted and smaller."),
            T("A **real image** is formed where rays really meet. It can be shown on a screen. A **virtual image** is where rays only **seem** to come from. It cannot be shown on a screen."),
            CODE("""Object position     Image position       Nature of the image
Beyond C            between F and C      real, inverted, smaller
At C                at C                 real, inverted, same size
Between C and F     beyond C             real, inverted, larger
At F                at infinity          (reflected rays are parallel)
Between F and P     behind the mirror    virtual, upright, larger""", "text", title="Image in a concave mirror"),
            IMG("f5ph-c-convex-mirror.svg",
                "A convex mirror with an object on its left. A blue ray parallel to the axis reflects as if from the focus F behind the mirror. An amber ray aimed at the pole reflects downwards. Dashed lines behind the mirror meet at a small upright virtual image.",
                "Figure 2. A convex mirror always gives a virtual, upright, smaller image behind the mirror."),
            KEY("Uses", "The use follows from the image.",
                cards=[["Concave", "Shaving and make-up mirrors and the dentist's mirror (object inside F gives a larger upright image). A torch or car headlight puts the lamp at F to send out a parallel beam. A solar cooker or dish collects parallel rays at F."],
                       ["Convex", "Driving mirrors and shop security mirrors: the image is smaller but the **field of view is wider**."]]),
            H("The mirror formula"),
            D("For mirrors we use $u$ for the object distance, $v$ for the image distance and $f$ for the focal length, all measured from the pole. "
              "The **mirror formula** and the **magnification** are given below.",
              title="Mirror formula", formula=r"\dfrac{1}{f} = \dfrac{1}{u} + \dfrac{1}{v} \qquad m = \dfrac{\text{image height}}{\text{object height}} = \dfrac{v}{u}",
              note="We use the real-is-positive convention: $f$ is positive for a concave mirror and negative for a convex mirror; a negative $v$ means a virtual image behind the mirror. Textbooks differ on signs, so check your textbook. In $m = v/u$ use the size of $v$."),
            H("Worked examples"),
            EX("Worked example 1: object beyond C", intro=(
                "A concave mirror has focal length 10 cm. A 4.0 cm tall object is placed 30 cm from the mirror. Find the image distance, the magnification and the image height."),
               steps=[
                   S("Write the formula", math=r"\dfrac{1}{v} = \dfrac{1}{f} - \dfrac{1}{u} = \dfrac{1}{10} - \dfrac{1}{30}"),
                   S("Work it out", math=r"\dfrac{1}{v} = \dfrac{3 - 1}{30} = \dfrac{2}{30} \ \Rightarrow \ v = 15\ \text{cm}"),
                   S("Magnification", math=r"m = \dfrac{v}{u} = \dfrac{15}{30} = 0.50"),
                   S("Image height", math=r"0.50 \times 4.0 = 2.0\ \text{cm}"),
                   S("Answer", text="The image is 15 cm from the mirror (between F and C), real, inverted and 2.0 cm tall."),
               ]),
            EX("Worked example 2: a shaving mirror", intro=(
                "A concave mirror has focal length 10 cm. A face is 5.0 cm from the mirror. Find the image distance and magnification and say what the image is like."),
               steps=[
                   S("Use the formula", math=r"\dfrac{1}{v} = \dfrac{1}{10} - \dfrac{1}{5} = \dfrac{1 - 2}{10} = -\dfrac{1}{10}"),
                   S("Image distance", math=r"v = -10\ \text{cm}"),
                   S("Magnification (use the size of v)", math=r"m = \dfrac{10}{5.0} = 2.0"),
                   S("Answer", text="The negative sign means the image is virtual, 10 cm behind the mirror, upright and twice as large. The object is inside F."),
               ]),
            EX("Worked example 3: a convex mirror", intro=(
                "A convex driving mirror has focal length 20 cm. An object is 60 cm from the mirror. Find the image distance and the magnification."),
               steps=[
                   S("Convex: f is negative", math=r"\dfrac{1}{v} = \dfrac{1}{f} - \dfrac{1}{u} = -\dfrac{1}{20} - \dfrac{1}{60} = -\dfrac{3 + 1}{60} = -\dfrac{1}{15}"),
                   S("Image distance", math=r"v = -15\ \text{cm}"),
                   S("Magnification", math=r"m = \dfrac{15}{60} = 0.25"),
                   S("Answer", text="The image is virtual, 15 cm behind the mirror, upright and one quarter of the size."),
               ]),
            MISTAKE("Wrong rays in the diagram", "The ray through the centre of curvature C goes **back along itself**. The ray through F goes out **parallel** to the axis. "
                    "Do not mix these up, and do not draw a ray bending without touching the mirror."),
            MISTAKE("Solid lines for a virtual image", "Behind a mirror the lines are **dashed** because no light really goes there. The image of a virtual point is drawn where the dashed lines meet."),
            QUIZ("An object is placed between a concave mirror and its principal focus F. The image is", ["real, inverted and smaller", "real, inverted and larger", "virtual, upright and larger", "virtual, upright and smaller"], 2,
                 "Inside F the reflected rays diverge. They seem to come from behind the mirror, giving a virtual, upright, larger image.",
                 hint="Think of a shaving mirror.",
                 feedback=["That is for an object beyond C.", "That is for an object between F and C.", "",
                           "A concave mirror gives a smaller image only for objects beyond C, and that image is real."]),
            QUIZ("A concave mirror has radius of curvature 40 cm. What is its focal length?", ["10 cm", "20 cm", "40 cm", "80 cm"], 1,
                 "f = R / 2 = 40 / 2 = 20 cm.",
                 hint="The focal length is half the radius.",
                 feedback=["You divided by four.", "", "You used R as the focal length.", "You doubled R. The focal length is half the radius."]),
            TIP("Where this appears: ray diagrams for curved mirrors and the image table appear in Paper 1 (multiple choice) and in Paper 2 (draw a diagram, "
                "name the uses). The Board's examiners report that many candidates are weak on optics and on ray diagrams, so practise drawing them neatly."),
            PQ("A concave mirror of focal length 15 cm forms an image of an object placed 30 cm away. State the position and nature of the image.",
               r"The object is at C ($R = 2f = 30$ cm), so the image is at C: 30 cm from the mirror, real, inverted and the same size. Check: $1/v = 1/15 - 1/30 = 1/30$, so $v = 30$ cm."),
            PQ("Why is a convex mirror used as a driving mirror?",
               "It gives an upright image and a wide field of view, so the driver sees more of the road behind. The image is smaller, but it is always upright."),
            PQ("A concave mirror has focal length 10 cm. An object is 15 cm from the mirror. Find the image distance and the magnification.",
               r"$1/v = 1/10 - 1/15 = 1/30$, so $v = 30$ cm. $m = 30/15 = 2.0$. The image is real, inverted and twice as large."),
            PQ("Describe where a lamp must be placed in a car headlight to give a parallel beam.",
               "The lamp must be at the principal focus of the concave reflector. Rays from the focus reflect parallel to the principal axis."),
            SUM("A concave mirror converges rays; a convex mirror diverges rays. The focal length is $f = R/2$.",
                "Standard rays: parallel to the axis then through F; through F then parallel; through C then back along itself.",
                "Concave mirror: image real and inverted for objects beyond F, virtual, upright and larger for objects inside F. Convex mirror: always virtual, upright and smaller.",
                r"Mirror formula $1/f = 1/u + 1/v$ and magnification $m = v/u$."),
        ],
    ),
    # ------------------------------------------------------------------ 6. Refraction and Snell's law
    lesson(
        module=WAVES,
        topic="Refraction and total internal reflection",
        title="Refraction of light and Snell's law",
        slug="phc-refraction-snell",
        minutes=24,
        summary=r"Light bends when it changes speed at a boundary. Use the refractive index $n = \sin i / \sin r = c / v$ and real and apparent depth.",
        objectives=[
            "Describe refraction and say whether the ray bends towards or away from the normal",
            "Use Snell's law n = sin i / sin r to find n or an angle",
            "Use n = speed in air / speed in the material",
            "Explain real and apparent depth and use n = real depth / apparent depth",
        ],
        key_concepts=["Refraction", "Refractive index", "Snell's law", "Normal", "Real depth", "Apparent depth"],
        blocks=[
            H("Introduction"),
            T("Put a straight spoon in a glass of water. Looking from the side, the spoon seems to **bend** where it enters the water. "
              "A swimming pool at a hotel in Kribi looks shallower than it really is. A fisherman who aims his spear at the fish he sees often misses."),
            T("All of these happen because light **changes speed** when it passes from one transparent material into another. This is **refraction**."),
            H("What happens at the boundary"),
            D("**Refraction** is the change in direction of a ray of light when it passes from one transparent medium into another, "
              "caused by the change in the speed of light.",
              title="Refraction of light"),
            KEY("Which way does the ray bend?", "Compare the speed of light in the two materials.",
                cards=[["Into a denser material (air to glass or water)", "Light slows down and bends **towards the normal**. The angle is smaller."],
                       ["Into a less dense material (glass or water to air)", "Light speeds up and bends **away from the normal**. The angle is larger."],
                       ["Along the normal ($i = 0^\\circ$)", "No change of direction. The ray goes straight through, though it still changes speed."]]),
            IMG("f5ph-c-refraction.svg",
                "A ray from the upper left meets a horizontal air-glass boundary with i equal to 50 degrees measured from the dashed normal. Inside the glass the ray bends towards the normal with r equal to about 31 degrees.",
                "Figure 1. Refraction from air into glass: the ray bends towards the normal."),
            T("The frequency of the light does not change. The speed and the wavelength both decrease in the denser material."),
            H("Snell's law and the refractive index"),
            D("For a ray passing from air (or a vacuum) into a material, the **refractive index** $n$ of the material is the ratio $\\sin i / \\sin r$. "
              "This is **Snell's law**. The angles $i$ and $r$ are measured from the normal.",
              title="Snell's law", formula=r"n = \dfrac{\sin i}{\sin r}"),
            D("The refractive index also equals the speed of light in air (or vacuum) divided by its speed in the material. "
              "It has **no unit**, and it is always greater than 1.",
              title="Refractive index and speed", formula=r"n = \dfrac{c}{v} = \dfrac{\text{speed in air}}{\text{speed in the material}}"),
            CODE("""Material    Refractive index n (about)
Air         1.00
Water       1.33
Glass       1.5
Diamond     2.4""", "text", title="Typical values"),
            T("The speed of light in air is about $3.0 \\times 10^{8}$ m/s. A larger $n$ means light travels more slowly in the material and bends more."),
            H("Worked examples"),
            EX("Worked example 1: find the refractive index", intro=(
                "A ray enters a glass block from air. The angle of incidence is $45^\\circ$ and the angle of refraction is $28^\\circ$. Find the refractive index of the glass."),
               steps=[
                   S("Write Snell's law", math=r"n = \dfrac{\sin i}{\sin r}"),
                   S("Substitute", math=r"n = \dfrac{\sin 45^\circ}{\sin 28^\circ} = \dfrac{0.7071}{0.4695}"),
                   S("Calculate", math=r"n = 1.5"),
                   S("Answer", text="The refractive index is 1.5 (it has no unit)."),
               ]),
            EX("Worked example 2: find the angle of refraction", intro=(
                "A ray goes from air into glass of refractive index 1.5. The angle of incidence is $60^\\circ$. Find the angle of refraction."),
               steps=[
                   S("Rearrange", math=r"\sin r = \dfrac{\sin i}{n} = \dfrac{\sin 60^\circ}{1.5} = \dfrac{0.8660}{1.5} = 0.5774"),
                   S("Take the inverse sine", math=r"r = \sin^{-1}(0.5774) = 35.3^\circ"),
                   S("Answer", text="The angle of refraction is $35^\\circ$ (to the nearest degree), smaller than 60 degrees: the ray bends towards the normal."),
               ]),
            EX("Worked example 3: speed of light in glass", intro=(
                r"The speed of light in air is $3.0 \times 10^{8}$ m/s. Find its speed in glass of refractive index 1.5."),
               steps=[
                   S("Rearrange n = c / v", math=r"v = \dfrac{c}{n}"),
                   S("Substitute", math=r"v = \dfrac{3.0 \times 10^{8}}{1.5} = 2.0 \times 10^{8}\ \text{m/s}"),
                   S("Answer", text="Light travels at $2.0 \\times 10^{8}$ m/s in the glass."),
               ]),
            H("Real and apparent depth"),
            T("When you look into a pool from above, rays from the bottom bend away from the normal as they leave the water. "
              "Your eye traces them back in straight lines and sees the bottom **higher up**."),
            D("The refractive index of a material is also the ratio of its **real depth** to its **apparent depth** when viewed from above (nearly along the normal).",
              title="Real and apparent depth", formula=r"n = \dfrac{\text{real depth}}{\text{apparent depth}}"),
            EX("Worked example 4: a swimming pool", intro=(
                "A pool is 2.0 m deep. The refractive index of water is 1.33. How deep does it appear when seen from directly above?"),
               steps=[
                   S("Rearrange", math=r"\text{apparent depth} = \dfrac{\text{real depth}}{n}"),
                   S("Substitute", math=r"\dfrac{2.0}{1.33} = 1.5\ \text{m}"),
                   S("Answer", text="The pool appears about 1.5 m deep."),
               ]),
            T("**Experiment to find $n$.** Shine a ray into a glass block at several angles of incidence, and measure $i$ and $r$ with a protractor. "
              "Plot a graph of $\\sin i$ (vertical) against $\\sin r$ (horizontal). The graph is a straight line through the origin and its **gradient** is $n$."),
            MISTAKE("Swapping sin i and sin r", "For light going **from air into** the material, $n = \\sin i / \\sin r$, with $i$ the angle in the air. If you swap them, "
                    "you get a number smaller than 1, which is impossible for ordinary materials."),
            MISTAKE("Using the angle with the surface", "Both angles are measured from the **normal**. If a question gives an angle with the surface, subtract it from $90^\\circ$ first."),
            QUIZ("Light passes from air into water. The ray", ["bends away from the normal", "bends towards the normal", "does not bend", "reflects completely"], 1,
                 "Water is denser than air, so light slows down and bends towards the normal.",
                 hint="Does light travel faster or slower in water?",
                 feedback=["It bends away only when going from a denser to a less dense material.", "",
                           "It bends unless it meets the boundary along the normal.", "Total reflection needs light going from a dense to a less dense material."]),
            QUIZ(r"The refractive index of a plastic is 1.6. What is the speed of light in it? (Speed in air $= 3.0 \times 10^{8}$ m/s)", [r"$4.8 \times 10^{8}$ m/s", r"$1.9 \times 10^{8}$ m/s", r"$3.0 \times 10^{8}$ m/s", r"$0.53 \times 10^{8}$ m/s"], 1,
                 r"$v = c / n = 3.0 \times 10^{8} / 1.6 = 1.9 \times 10^{8}$ m/s.",
                 hint="Divide the speed in air by the refractive index.",
                 feedback=["You multiplied by n. Light is slower in plastic, so the speed must be less than in air.", "",
                           "That is the speed in air. The speed changes in a new material.", "You divided n by c."]),
            TIP("Where this appears: refraction and Snell's law are tested in Paper 1 (find n or an angle) and in Paper 2 (a calculation, a ray diagram and a description "
                "of the experiment). Give the refractive index without a unit, and show your sine values."),
            PQ("A ray of light passes from air into a liquid. The angle of incidence is 50 degrees and the angle of refraction is 32 degrees. Calculate the refractive index of the liquid.",
               r"$n = \sin 50^\circ / \sin 32^\circ = 0.7660 / 0.5299 = 1.45$."),
            PQ("Light enters glass (n = 1.5) from air at an angle of incidence of 30 degrees. Find the angle of refraction.",
               r"$\sin r = \sin 30^\circ / 1.5 = 0.5 / 1.5 = 0.3333$, so $r = 19.5^\circ$ (about 19 degrees)."),
            PQ(r"The speed of light in diamond is $1.24 \times 10^{8}$ m/s. Find its refractive index. (Speed of light in air $= 3.0 \times 10^{8}$ m/s)",
               r"$n = c / v = 3.0 \times 10^{8} / 1.24 \times 10^{8} = 2.4$."),
            PQ("A fish in a river is 1.2 m below the surface. The refractive index of water is 1.33. How deep does it appear to a person looking straight down?",
               r"Apparent depth $= 1.2 / 1.33 = 0.90$ m."),
            SUM("Refraction is the bending of light when its speed changes at a boundary. The frequency does not change.",
                "Into a denser material light bends towards the normal; into a less dense material it bends away.",
                r"$n = \sin i / \sin r = c / v$. The refractive index has no unit and is more than 1.",
                r"$n = \text{real depth} / \text{apparent depth}$, so a pool looks shallower than it is."),
        ],
    ),
    # ------------------------------------------------------------------ 7. Total internal reflection
    lesson(
        module=WAVES,
        topic="Refraction and total internal reflection",
        title="Critical angle and total internal reflection",
        slug="phc-total-internal-reflection",
        minutes=22,
        summary=r"When light inside glass or water hits the surface beyond the critical angle $c$ it is totally reflected. Use $\sin c = 1/n$ and explain optical fibres and prisms.",
        objectives=[
            "State the two conditions for total internal reflection",
            "Define the critical angle and use sin c = 1/n",
            "Decide whether a ray refracts out or is totally reflected",
            "Explain optical fibres, prisms and reflectors",
        ],
        key_concepts=["Total internal reflection", "Critical angle", "Optical fibre", "Prism", "Refractive index"],
        blocks=[
            H("Introduction"),
            T("The internet reaches many towns in Cameroon through **optical fibres**: thin glass threads that carry flashes of light for hundreds of kilometres, even round bends. "
              "A diamond sparkles far more than a piece of glass of the same shape. A cat's eye in the road shines back at your headlights."),
            T("All three use the same idea: light can be trapped inside a transparent material by **total internal reflection**."),
            H("From partial reflection to total reflection"),
            T("When a ray inside glass meets the boundary with air, part of the light is reflected and part is refracted out. The refracted ray bends **away** from the normal. "
              "If we increase the angle of incidence, the refracted ray bends further and further from the normal, until it runs along the boundary."),
            D("The **critical angle** $c$ is the angle of incidence in the denser material for which the angle of refraction in the less dense material is $90^\\circ$ "
              "(the refracted ray runs along the boundary).",
              title="Critical angle"),
            D("**Total internal reflection** is the complete reflection of light at the boundary between two media, when light travels from a denser to a less dense medium "
              "and the angle of incidence is greater than the critical angle.",
              title="Total internal reflection"),
            KEY("Two conditions are both needed", "Check both before you say a ray is totally reflected.",
                cards=[["1. Dense to less dense", "The light must travel from the denser medium (glass or water) towards the less dense medium (air)."],
                       ["2. Beyond the critical angle", "The angle of incidence must be **greater than** the critical angle $c$."]]),
            IMG("f5ph-c-tir.svg",
                "Three panels of a ray inside glass meeting the glass-air boundary. With i less than c the ray refracts out and bends away from the normal. With i equal to c the refracted ray runs along the boundary. With i greater than c the ray is totally reflected back into the glass.",
                "Figure 1. Below, at and above the critical angle."),
            H("The critical angle formula"),
            T("At the critical angle the ray leaves along the boundary, so the angle in the air is $90^\\circ$. Light is going from the material into air, so by Snell's law, with the ray reversed, "
              r"$n = \dfrac{\sin 90^\circ}{\sin c}$, and $\sin 90^\circ = 1$."),
            D("The critical angle depends on the refractive index of the material. A larger $n$ gives a smaller critical angle.",
              title="Critical angle formula", formula=r"\sin c = \dfrac{1}{n}"),
            CODE("""Material    n (about)   Critical angle c
Water       1.33        48.8 degrees
Glass       1.5         41.8 degrees
Diamond     2.4         24.4 degrees""", "text", title="Critical angles (material to air)"),
            T("Diamond has a very small critical angle, so most of the light that enters is totally reflected many times inside before it leaves. That is why it sparkles."),
            H("Worked examples"),
            EX("Worked example 1: find the critical angle", intro=(
                "Find the critical angle of a plastic of refractive index 1.6, for light going from the plastic into air."),
               steps=[
                   S("Formula", math=r"\sin c = \dfrac{1}{n} = \dfrac{1}{1.6} = 0.625"),
                   S("Inverse sine", math=r"c = \sin^{-1}(0.625) = 38.7^\circ"),
                   S("Answer", text="The critical angle is $38.7^\\circ$."),
               ]),
            EX("Worked example 2: find n from c", intro=(
                "The critical angle of a glass is $45^\\circ$. Find its refractive index."),
               steps=[
                   S("Rearrange", math=r"n = \dfrac{1}{\sin c} = \dfrac{1}{\sin 45^\circ} = \dfrac{1}{0.7071}"),
                   S("Answer", math=r"n = 1.41"),
               ]),
            EX("Worked example 3: a 45 degree prism", intro=(
                "A ray enters one short face of a right-angled glass prism at $90^\\circ$ to that face, so it goes straight in. It then hits the long face at $45^\\circ$. "
                "The glass has $n = 1.5$ (critical angle $41.8^\\circ$). What happens to the ray at the long face?"),
               steps=[
                   S("Condition 1", text="The ray is going from glass (dense) to air (less dense). Yes."),
                   S("Condition 2", math=r"i = 45^\circ > c = 41.8^\circ"),
                   S("Answer", text="Both conditions are met, so the ray is **totally reflected** and turns through $90^\\circ$. Prisms like this work in periscopes and binoculars, and are better than silvered mirrors because no light is lost."),
               ]),
            KEY("Uses of total internal reflection", "Each use follows from the two conditions.",
                cards=[["Optical fibre", "A thin glass fibre with a core of higher n surrounded by a cladding of lower n. Light hitting the core boundary beyond the critical angle is totally reflected again and again, so it follows the bends. Used for internet, telephones and in endoscopes in medicine."],
                       ["Prism reflectors", "Right-angled prisms in binoculars and periscopes, and reflectors on bicycles, road signs and cat's eyes."],
                       ["Mirage", "On a hot road the air near the ground is hot and less dense. Light from the sky is refracted upwards towards your eye (and may be totally reflected near the ground), so you seem to see water on the road."]]),
            MISTAKE("Using total internal reflection from air into glass", "It can only happen when the light goes from a **denser** to a **less dense** medium. Light going from air into glass is always refracted."),
            MISTAKE("Equal to the critical angle is not total reflection", "At exactly $c$ the ray runs along the boundary. For total internal reflection the angle must be **greater than** $c$."),
            QUIZ("A ray in glass (critical angle 42 degrees) meets the glass-air boundary at 30 degrees. What happens?", ["Total internal reflection", "The ray refracts out of the glass (with some reflection)", "The ray runs along the boundary", "The ray is absorbed"], 1,
                 "30 degrees is less than the critical angle, so most of the light is refracted out into the air, away from the normal, and a little is reflected.",
                 hint="Compare the angle of incidence with the critical angle.",
                 feedback=["That would need an angle greater than 42 degrees.", "",
                           "That happens only exactly at the critical angle.", "Clear glass transmits most of the light."]),
            QUIZ("Which material has the smallest critical angle?", ["Water, n = 1.33", "Glass, n = 1.5", "Diamond, n = 2.4", "Air, n = 1.00"], 2,
                 "sin c = 1/n, so the largest n gives the smallest c. Diamond: c = 24.4 degrees.",
                 hint="Use sin c = 1/n. Which n gives the smallest sin c?",
                 feedback=["Water has the largest critical angle of these three.", "Glass is in between water and diamond.", "",
                           "Light in air cannot be totally reflected, because air is not denser than anything else here."]),
            TIP("Where this appears: total internal reflection is a favourite in Paper 1 and Paper 2. The Board's examiners report that many candidates cannot define it correctly. "
                "Write the definition with both conditions: from a denser to a less dense medium, and angle of incidence greater than the critical angle."),
            PQ("Define the critical angle and state the conditions for total internal reflection.",
               "The critical angle is the angle of incidence in the denser medium for which the angle of refraction in the less dense medium is 90 degrees. "
               "Total internal reflection needs (1) light going from a denser to a less dense medium and (2) an angle of incidence greater than the critical angle."),
            PQ("Calculate the critical angle for water of refractive index 1.33.",
               r"$\sin c = 1/1.33 = 0.752$, so $c = 48.8^\circ$ (about 49 degrees)."),
            PQ("Explain how light travels along an optical fibre.",
               "Light enters the core and hits the core-cladding boundary at an angle greater than the critical angle, going from the denser core to the less dense cladding. "
               "It is totally reflected and keeps being totally reflected along the fibre, so it follows the bends."),
            PQ("The critical angle for a certain glass is 40 degrees. Calculate its refractive index and say whether a ray inside the glass hitting the surface at 35 degrees is totally reflected.",
               r"$n = 1/\sin 40^\circ = 1/0.6428 = 1.56$. 35 degrees is less than the critical angle, so the ray is not totally reflected: it refracts out."),
            SUM("Total internal reflection needs light going from a denser to a less dense medium with $i$ greater than the critical angle $c$.",
                r"At the critical angle the refracted ray runs along the boundary. $\sin c = 1/n$.",
                "A larger refractive index gives a smaller critical angle, so diamond sparkles.",
                "Uses: optical fibres, prism reflectors in periscopes and binoculars, and cat's eyes."),
        ],
    ),
    # ------------------------------------------------------------------ 8. Thin lenses
    lesson(
        module=WAVES,
        topic="Lenses and optical instruments",
        title="Thin lenses and their images",
        slug="phc-thin-lenses",
        minutes=25,
        summary="A converging lens focuses parallel rays and can form real or virtual images; a diverging lens spreads rays. Draw the three standard rays and use 1/f = 1/u + 1/v.",
        objectives=[
            "Name the optical centre, principal axis, principal focus and focal length of a thin lens",
            "Draw ray diagrams for converging and diverging lenses",
            "State the nature and position of the image for each object position",
            "Use 1/f = 1/u + 1/v and m = v/u in calculations",
        ],
        key_concepts=["Converging lens", "Diverging lens", "Principal focus", "Focal length", "Real and virtual image", "Magnification"],
        blocks=[
            H("Introduction"),
            T("A seller at a market in Bafoussam holds a small glass lens over a tiny printed number on a phone box and the number looks big. "
              "In the dry season a boy can use a lens to focus sunlight on dry paper until it burns. In both cases a **converging lens** is doing the work."),
            T("A lens is a piece of transparent material (glass or plastic) with curved faces. It **refracts** the light at both faces. A thin lens is much thinner than its radius of curvature, "
              "so we draw it as a single line with arrow heads."),
            H("Two kinds of lens"),
            KEY("Converging and diverging", "Look at the shape: thick in the middle or thin in the middle.",
                cards=[["Converging (convex) lens", "Thicker in the middle. It brings parallel rays together at the principal focus."],
                       ["Diverging (concave) lens", "Thinner in the middle. It spreads parallel rays out so they seem to come from a point on the same side as the light."]]),
            D("The **optical centre** is the centre of the lens. The **principal axis** is the line through the optical centre at 90 degrees to the lens. "
              "The **principal focus F** of a converging lens is the point where rays parallel to the principal axis meet after refraction. The **focal length $f$** is the distance from the optical centre to F. "
              "A lens has **two** principal foci, one on each side, at the same distance from the lens.",
              title="Lens words"),
            H("The three standard rays"),
            KEY("Rays for a converging lens", "Draw any two to find the image of a point. Put arrows on the rays.",
                cards=[["Ray 1", "Parallel to the principal axis. After the lens it passes **through F** on the far side."],
                       ["Ray 2", "Through the **optical centre**. It goes **straight on** without bending."],
                       ["Ray 3", "Through the near F. After the lens it goes **parallel** to the axis."]]),
            IMG("f5ph-c-lens-converging.svg",
                "A converging lens with F and 2F marked on both sides. An object stands beyond 2F on the left. A blue ray parallel to the axis refracts through F on the right; an amber ray through the centre goes straight on. They meet between F and 2F at a small inverted real image.",
                "Figure 1. Object beyond 2F: the image is between F and 2F on the other side, real, inverted and smaller."),
            CODE("""Object position    Image position          Nature of the image
Beyond 2F          between F and 2F        real, inverted, smaller
At 2F              at 2F                   real, inverted, same size
Between F and 2F   beyond 2F               real, inverted, larger
At F               at infinity             (emerging rays are parallel)
Inside F           same side as object     virtual, upright, larger""", "text", title="Image in a converging lens"),
            T("When the object is **inside F** the lens is used as a **magnifying glass**. You look through it at an upright, enlarged, virtual image."),
            IMG("f5ph-c-lens-diverging.svg",
                "A diverging lens with an object on its left. A blue ray parallel to the axis bends away as if from the focus on the object's side (dashed). An amber ray through the centre goes straight on. Dashed lines meet at a small upright image on the object's side.",
                "Figure 2. A diverging lens always gives a virtual, upright, smaller image on the same side as the object."),
            H("The lens formula"),
            D("For a thin lens, with $u$ the object distance, $v$ the image distance and $f$ the focal length (all from the optical centre):",
              title="Lens formula and magnification",
              formula=r"\dfrac{1}{f} = \dfrac{1}{u} + \dfrac{1}{v} \qquad m = \dfrac{\text{image height}}{\text{object height}} = \dfrac{v}{u}",
              note="Real-is-positive convention: $f$ is positive for a converging lens and negative for a diverging lens; a negative $v$ means a virtual image. Sign conventions differ between textbooks: check yours. In $m = v/u$ use the size of $v$."),
            H("Worked examples"),
            EX("Worked example 1: a real image", intro=(
                "A converging lens has focal length 10 cm. An object 3.0 cm tall is 30 cm from the lens. Find the image distance, magnification and image height."),
               steps=[
                   S("Lens formula", math=r"\dfrac{1}{v} = \dfrac{1}{f} - \dfrac{1}{u} = \dfrac{1}{10} - \dfrac{1}{30} = \dfrac{2}{30}"),
                   S("Image distance", math=r"v = 15\ \text{cm}"),
                   S("Magnification", math=r"m = \dfrac{15}{30} = 0.50"),
                   S("Image height", math=r"0.50 \times 3.0 = 1.5\ \text{cm}"),
                   S("Answer", text="The image is real, inverted, 15 cm from the lens (between F and 2F) and 1.5 cm tall."),
               ]),
            EX("Worked example 2: a larger real image", intro=(
                "The same lens (f = 10 cm) is used with the object 15 cm from the lens. Find $v$ and $m$."),
               steps=[
                   S("Lens formula", math=r"\dfrac{1}{v} = \dfrac{1}{10} - \dfrac{1}{15} = \dfrac{3 - 2}{30} = \dfrac{1}{30}"),
                   S("Image distance", math=r"v = 30\ \text{cm}"),
                   S("Magnification", math=r"m = \dfrac{30}{15} = 2.0"),
                   S("Answer", text="The image is real, inverted and twice the size, 30 cm from the lens. The object is between F and 2F."),
               ]),
            EX("Worked example 3: a magnifying glass", intro=(
                "The same lens (f = 10 cm) is used as a magnifying glass with the object 5.0 cm from the lens. Find $v$ and $m$."),
               steps=[
                   S("Lens formula", math=r"\dfrac{1}{v} = \dfrac{1}{10} - \dfrac{1}{5} = \dfrac{1 - 2}{10} = -\dfrac{1}{10}"),
                   S("Image distance", math=r"v = -10\ \text{cm}"),
                   S("Magnification (size of v)", math=r"m = \dfrac{10}{5.0} = 2.0"),
                   S("Answer", text="The negative sign means the image is virtual and on the same side as the object. It is 10 cm from the lens, upright and twice as big."),
               ]),
            EX("Worked example 4: a diverging lens", intro=(
                "A diverging lens has focal length 10 cm. An object is 30 cm from it. Find the image distance and the magnification."),
               steps=[
                   S("f is negative", math=r"\dfrac{1}{v} = \dfrac{1}{f} - \dfrac{1}{u} = -\dfrac{1}{10} - \dfrac{1}{30} = -\dfrac{4}{30}"),
                   S("Image distance", math=r"v = -7.5\ \text{cm}"),
                   S("Magnification", math=r"m = \dfrac{7.5}{30} = 0.25"),
                   S("Answer", text="The image is virtual, 7.5 cm from the lens on the object's side, upright and one quarter of the size."),
               ]),
            TIP("To check a ray diagram, count: the image of an object beyond 2F is smaller; between F and 2F it is larger. If your picture disagrees, redraw the rays with a ruler."),
            MISTAKE("Bending the ray at the wrong place", "Draw a thin lens as a straight line and bend the ray **once**, at the line. "
                    "The ray through the optical centre does **not** bend."),
            MISTAKE("Forgetting the second focus", "A lens has a principal focus on **each** side. Mark F on both sides, and also 2F, so you can place the object correctly."),
            QUIZ("A converging lens forms a virtual, upright, magnified image. Where is the object?", ["Beyond 2F", "At 2F", "Between F and 2F", "Between F and the lens"], 3,
                 "A virtual, upright, larger image (a magnifying glass) needs the object inside the focal length.",
                 hint="Think of a magnifying glass held close to the object.",
                 feedback=["Beyond 2F the image is real, inverted and smaller.", "At 2F the image is real, inverted and the same size.",
                           "Between F and 2F the image is real, inverted and larger.", ""]),
            QUIZ("Which lens always forms a virtual, upright, smaller image of a real object?", ["A converging lens", "A diverging lens", "A plane mirror", "A concave mirror"], 1,
                 "The diverging lens spreads rays, so its image is always virtual, upright and smaller.",
                 hint="Which lens spreads the rays out?",
                 feedback=["A converging lens can make real images and enlarged images.", "",
                           "A plane mirror is not a lens, and its image is the same size.", "A concave mirror is a mirror, not a lens."]),
            TIP("Where this appears: lenses are one of the most tested parts of optics, in Paper 1 (image nature, calculations) and in Paper 2 (draw the rays, use the formula). "
                "The Board's examiners report that candidates were poor at drawing ray diagrams and at optics generally, so practise often."),
            PQ("State where the image is formed, and its nature, when an object is placed beyond 2F of a converging lens.",
               "The image is formed between F and 2F on the other side of the lens. It is real, inverted and smaller than the object."),
            PQ("A converging lens of focal length 20 cm forms an image of an object 50 cm away. Find the image distance.",
               r"$1/v = 1/20 - 1/50 = (5 - 2)/100 = 3/100$, so $v = 33$ cm (33.3 cm)."),
            PQ("An object 4.0 cm tall is placed 12 cm from a converging lens of focal length 8.0 cm. Calculate the position and height of the image.",
               r"$1/v = 1/8 - 1/12 = (3 - 2)/24 = 1/24$, so $v = 24$ cm. $m = 24/12 = 2.0$, so the image is 8.0 cm tall."),
            PQ("A converging lens of focal length 15 cm is used as a magnifying glass. State the range of object distances and describe the image.",
               "The object must be less than 15 cm from the lens (inside F). The image is virtual, upright and larger, on the same side of the lens as the object."),
            SUM("A converging lens (thick in the middle) brings parallel rays to the principal focus; a diverging lens spreads them.",
                "Standard rays: parallel to the axis then through F; through the optical centre straight on; through F then parallel.",
                "Converging lens: real, inverted images for objects beyond F; virtual, upright, larger image (magnifying glass) for objects inside F. Diverging lens: always virtual, upright, smaller.",
                r"Lens formula $1/f = 1/u + 1/v$ and $m = v/u$."),
        ],
    ),
    # ------------------------------------------------------------------ 9. Eye, camera and projector
    lesson(
        module=WAVES,
        topic="Lenses and optical instruments",
        title="The eye, the camera and the projector",
        slug="phc-eye-camera-projector",
        minutes=24,
        summary="The eye and the camera both form a real, inverted, smaller image with a converging lens; a projector forms a large real image on a screen. Learn the parts, the focusing and the common eye defects.",
        objectives=[
            "Name the main parts of the eye and of a simple camera and give their jobs",
            "Explain how the eye and the camera focus on near and far objects",
            "Describe short sight and long sight and how lenses correct them",
            "Describe how a projector makes a large image and use the lens formula for it",
        ],
        key_concepts=["Cornea", "Retina", "Accommodation", "Short sight", "Long sight", "Camera", "Projector"],
        blocks=[
            H("Introduction"),
            T("When you look at a friend across the football field, your eye forms a tiny picture of them on a screen at the back of the eye. "
              "A phone camera does the same thing with a tiny sensor. At the cinema, a projector makes a huge picture from a small film. "
              "All three instruments use a **converging lens** to form images."),
            H("The human eye"),
            IMG("f5ph-c-eye-camera.svg",
                "Left: the eye with cornea, iris, lens, retina and optic nerve, and two rays meeting on the retina. Right: a camera box with a lens, a diaphragm and a film or sensor at the back, with two rays focused on it.",
                "Figure 1. A simple eye and a simple camera: lens at the front, light-sensitive surface at the back."),
            KEY("Parts of the eye", "Light travels in through the front and is focused on the retina.",
                cards=[["Cornea", "The clear front surface. It does most of the bending (refraction) of the light."],
                       ["Iris and pupil", "The iris is a coloured ring of muscle. It changes the size of the hole (the **pupil**) to control how much light enters."],
                       ["Lens", "A flexible converging lens that **fine-focuses** the light onto the retina."],
                       ["Retina", "The light-sensitive layer at the back. It has cells that send signals along the **optic nerve** to the brain."]]),
            T("The image on the retina is **real, inverted and smaller** than the object. The brain turns it the right way up."),
            D("**Accommodation** is the ability of the eye to focus on objects at different distances by changing the shape of its lens. "
              "To see a **near** object, the ciliary muscles make the lens **fatter** (shorter focal length). To see a **far** object, the lens becomes **thinner** (longer focal length).",
              title="Accommodation"),
            T("A normal eye can focus from about 25 cm (the **near point**) to very far away (the **far point**, at infinity)."),
            H("Defects of vision"),
            KEY("Short sight and long sight", "Both defects mean the image does not fall exactly on the retina.",
                cards=[["Short sight (myopia)", "Far objects look blurred. The image forms **in front of** the retina because the lens is too strong or the eyeball too long. It is corrected with a **diverging** lens."],
                       ["Long sight (hypermetropia)", "Near objects look blurred (people need to hold the book far away). The image would form **behind** the retina. It is corrected with a **converging** lens."]]),
            H("The camera"),
            T("A simple camera has a **lens**, a **diaphragm** (a hole of adjustable size that controls how much light enters), a **shutter** (opens for a short time to let light in), "
              "and a light-sensitive **film or sensor** at the back. The inside of the box is black so that no stray light spoils the picture."),
            T("To focus, the lens is moved **forward** (for nearer objects) or **backward** (for distant objects), so that the image falls exactly on the film or sensor. "
              "The image is **real, inverted and smaller** than the object."),
            CODE("""Eye                      Camera
cornea and lens          lens
iris and pupil           diaphragm
retina                   film or sensor
focus: lens changes      focus: lens moves
shape                    in and out""", "text", title="Eye and camera compared"),
            H("The projector"),
            T("A projector shows a small slide (or an image on a small screen) as a **large** image on a wall or screen. A bright lamp and a **condenser lens** light the slide strongly. "
              "The **projection lens** is a converging lens. The slide is placed **between F and 2F** (just outside the focal length), upside down. "
              "The image on the screen is **real, inverted and magnified**, so the upside-down slide gives an upright picture."),
            IMG("f5ph-c-projector.svg",
                "A converging lens with F and 2F marked. A small slide stands between F and 2F on the left. A blue ray parallel to the axis and an amber ray through the centre meet beyond 2F on the right, at a screen, giving a large inverted real image.",
                "Figure 2. The slide is between F and 2F; the image on the screen is beyond 2F, real, inverted and magnified."),
            H("Worked examples"),
            EX("Worked example 1: a camera", intro=(
                "A camera lens has focal length 50 mm. It photographs a person 1.7 m tall standing 3.0 m away. Find the distance from the lens to the sensor and the height of the image on the sensor."),
               steps=[
                   S("Use the same units", text="u = 3.0 m = 3000 mm and f = 50 mm."),
                   S("Lens formula", math=r"\dfrac{1}{v} = \dfrac{1}{50} - \dfrac{1}{3000} = \dfrac{60 - 1}{3000} = \dfrac{59}{3000}"),
                   S("Image distance", math=r"v = 50.8\ \text{mm}"),
                   S("Magnification", math=r"m = \dfrac{50.8}{3000} = 0.01695"),
                   S("Image height", math=r"0.0169 \times 1700\ \text{mm} = 28.8\ \text{mm}"),
                   S("Answer", text="The sensor is 50.8 mm behind the lens (slightly more than f) and the image is 29 mm tall, real and inverted."),
               ]),
            EX("Worked example 2: a projector", intro=(
                "A projector lens has focal length 10 cm. A slide 2.4 cm tall is placed 12 cm from the lens. How far away must the screen be, and how tall is the image?"),
               steps=[
                   S("Lens formula", math=r"\dfrac{1}{v} = \dfrac{1}{10} - \dfrac{1}{12} = \dfrac{6 - 5}{60} = \dfrac{1}{60}"),
                   S("Screen distance", math=r"v = 60\ \text{cm}"),
                   S("Magnification", math=r"m = \dfrac{60}{12} = 5.0"),
                   S("Image height", math=r"5.0 \times 2.4 = 12\ \text{cm}"),
                   S("Answer", text="The screen is 60 cm from the lens. The image is 12 cm tall, real, inverted and five times bigger."),
               ]),
            MISTAKE("Mixing up the iris and the pupil", "The **pupil** is the hole. The **iris** is the coloured muscle around it that changes the size of the hole. In a camera the matching part is the diaphragm."),
            MISTAKE("Wrong lens for the eye defect", "Short sight needs a **diverging** lens, because the eye is focusing too strongly. Long sight needs a **converging** lens. "),
            QUIZ("Which part of the eye is like the film or sensor of a camera?", ["Cornea", "Iris", "Retina", "Pupil"], 2,
                 "The retina is the light-sensitive surface on which the image is formed, like the film or sensor.",
                 hint="Which part is at the back of the eye and detects the light?",
                 feedback=["The cornea is the front surface that bends the light.", "The iris controls the size of the pupil, like the diaphragm.", "",
                           "The pupil is the hole that lets light in."]),
            QUIZ("A person cannot read the board at the front of the class clearly but can read a book clearly. What is the defect and the correction?", ["Short sight, a diverging lens", "Short sight, a converging lens", "Long sight, a diverging lens", "Long sight, a converging lens"], 0,
                 "Far objects blurred means short sight (image in front of the retina). A diverging lens spreads the rays a little so the image moves back onto the retina.",
                 hint="Which objects does the person see badly: near or far?",
                 feedback=["", "A converging lens would make the image form even further in front of the retina.", "The person sees far objects badly, which is short sight, not long sight.", "The person sees far objects badly, which is short sight, not long sight."]),
            TIP("Where this appears: the eye, camera and projector are common in Paper 1 (compare the parts, name the defect) and in Paper 2 (describe the instrument, draw the rays). "
                "Say what the image is like: real, inverted and diminished in the camera and eye; real, inverted and magnified in the projector."),
            PQ("State the function of the iris and of the retina in the human eye.",
               "The iris controls the amount of light entering the eye by changing the size of the pupil. The retina is the light-sensitive layer on which the image is formed; it sends signals to the brain along the optic nerve."),
            PQ("Explain how the eye changes focus when you look from a distant tree to a book in your hand.",
               "The ciliary muscles make the eye lens fatter, which shortens its focal length. So the light from the near book is focused on the retina."),
            PQ("A projector lens has a focal length of 15 cm. A slide is 18 cm from the lens. Find the distance from the lens to the screen.",
               r"$1/v = 1/15 - 1/18 = (6 - 5)/90 = 1/90$, so $v = 90$ cm."),
            PQ("Why is the slide put into a projector upside down?",
               "The projector lens forms a real, inverted image on the screen. An upside-down slide gives an upright image."),
            SUM("The eye and the camera form a real, inverted, smaller image on the retina or sensor with a converging lens.",
                "The eye focuses by changing the shape of its lens (accommodation); a camera focuses by moving the lens.",
                "Short sight is corrected with a diverging lens; long sight with a converging lens.",
                "A projector places the slide between F and 2F, giving a real, inverted, magnified image on a screen."),
        ],
    ),
    # ------------------------------------------------------------------ 10. Dispersion and the electromagnetic spectrum
    lesson(
        module=WAVES,
        topic="Dispersion and the electromagnetic spectrum",
        title="Dispersion of light and the electromagnetic spectrum",
        slug="phc-dispersion-em-spectrum",
        minutes=24,
        summary="A prism splits white light into colours because each colour is refracted by a different amount. Visible light is one part of the electromagnetic spectrum, which runs from radio waves to gamma rays.",
        objectives=[
            "Explain dispersion of white light by a prism and name the order of the colours",
            "List the seven regions of the electromagnetic spectrum in order of wavelength and frequency",
            "State the properties that all electromagnetic waves share",
            "Give a source, a use and a danger for each region and calculate wavelength or frequency with v = f lambda",
        ],
        key_concepts=["Dispersion", "Spectrum", "Electromagnetic waves", "Wavelength", "Frequency", "Speed of light"],
        blocks=[
            H("Introduction"),
            T("After rain, with the Sun behind you, a rainbow can stretch over Mount Cameroon. The sunlight is **white**, yet the rainbow shows seven bands of colour. "
              "Where do the colours come from?"),
            T("In this lesson you learn how white light is split into colours, and then you meet the whole family of waves that visible light belongs to: "
              "the **electromagnetic spectrum**."),
            H("Dispersion of white light"),
            D("**Dispersion** is the splitting of white light into its colours when it passes through a glass prism (or raindrops). "
              "The band of colours is called a **spectrum**.",
              title="Dispersion"),
            IMG("f5ph-c-prism.svg",
                "A narrow beam of white light enters the left face of a triangular glass prism and leaves the right face as three diverging rays: red bent least, green in the middle and violet bent most.",
                "Figure 1. A prism disperses white light. The spread is exaggerated."),
            T("White light is a mixture of colours. In glass, each colour travels at a **slightly different speed**, so each has a slightly different refractive index. "
              "**Violet** light travels slowest in glass and is bent **most**. **Red** light travels fastest and is bent **least**. The colours leave the prism at different angles and spread out."),
            CODE("""Order of the colours (red to violet)
Red  Orange  Yellow  Green  Blue  Indigo  Violet

Red: longest wavelength, lowest frequency, bent least
Violet: shortest wavelength, highest frequency, bent most""", "text", title="Colours of the spectrum"),
            T("A rainbow is dispersion by millions of raindrops. Each drop refracts the sunlight, reflects it from its back inside the drop, and refracts it again as it leaves. "
              "If a second prism is placed the other way round, the colours can be combined to make white light again."),
            H("The electromagnetic spectrum"),
            D("**Electromagnetic (EM) waves** are transverse waves of changing electric and magnetic fields. They carry energy and can travel through a **vacuum**. "
              "The **electromagnetic spectrum** is the whole family of these waves, arranged by wavelength or frequency.",
              title="Electromagnetic spectrum"),
            IMG("f5ph-c-em-spectrum.svg",
                "A row of seven boxes from left to right: radio, microwave, infrared, visible, ultraviolet, X-ray and gamma. An arrow above shows frequency increasing and wavelength decreasing to the right.",
                "Figure 2. The seven regions of the electromagnetic spectrum."),
            KEY("Properties shared by all EM waves", "These are the facts to learn.",
                cards=[["Transverse", "They are all transverse waves."],
                       ["Same speed in a vacuum", r"All travel at $3.0 \times 10^{8}$ m/s in a vacuum (and almost the same in air)."],
                       ["No medium needed", "They can travel through empty space, which is how sunlight reaches Earth."],
                       ["Obey the wave equation", r"$v = f\lambda$: a longer wavelength means a lower frequency."]]),
            T("They differ in wavelength and frequency, and this decides how they behave and what they are used for. Higher frequency means more energy per wave, and so more danger to living cells."),
            KEY("Region by region, from long to short wavelength", "Approximate wavelength ranges. The boundaries differ a little between textbooks, so check yours.",
                cards=[["Radio waves", "Wavelength from about 0.1 m to over 1 km. Made by aerials. Used for radio, TV and mobile phone signals."],
                       ["Microwaves", "About 1 mm to 10 cm. Used in microwave ovens, mobile phone links and satellites. Danger: heat body tissue."],
                       ["Infrared", "About 700 nm to 1 mm. Given out by hot objects. Used in remote controls, grills and thermal cameras. Danger: skin burns."],
                       ["Visible light", "About 400 nm (violet) to 700 nm (red). Seen by the eye. Used for sight and in optical fibres."],
                       ["Ultraviolet", "About 10 nm to 400 nm. From the Sun and UV lamps. Used to sterilise water and tools and to check banknotes. Danger: sunburn, skin cancer, eye damage."],
                       ["X-rays", "About 0.01 nm to 10 nm. Made by X-ray tubes. Used to see bones and in airport security. Danger: damage cells, cancer."],
                       ["Gamma rays", "Shorter than about 0.01 nm. Given out by radioactive nuclei. Used to sterilise medical equipment and treat cancer. Danger: kill or damage cells."]]),
            T("Units: 1 nm (nanometre) $= 10^{-9}$ m. 1 mm $= 10^{-3}$ m. 1 GHz (gigahertz) $= 10^{9}$ Hz."),
            H("Worked examples"),
            EX("Worked example 1: microwaves", intro=(
                r"A microwave oven uses waves of frequency 2.45 GHz. Find their wavelength. (Speed $= 3.0 \times 10^{8}$ m/s)"),
               steps=[
                   S("Frequency in hertz", math=r"f = 2.45\ \text{GHz} = 2.45 \times 10^{9}\ \text{Hz}"),
                   S("Rearrange", math=r"\lambda = \dfrac{v}{f} = \dfrac{3.0 \times 10^{8}}{2.45 \times 10^{9}}"),
                   S("Answer", math=r"\lambda = 0.12\ \text{m}"),
               ]),
            EX("Worked example 2: ultraviolet", intro=(
                r"Ultraviolet light has a wavelength of $3.0 \times 10^{-7}$ m. Find its frequency."),
               steps=[
                   S("Rearrange", math=r"f = \dfrac{v}{\lambda} = \dfrac{3.0 \times 10^{8}}{3.0 \times 10^{-7}}"),
                   S("Answer", math=r"f = 1.0 \times 10^{15}\ \text{Hz}"),
               ]),
            EX("Worked example 3: red light", intro=(
                r"Red light has a frequency of $4.3 \times 10^{14}$ Hz. Find its wavelength in nanometres."),
               steps=[
                   S("Wavelength in metres", math=r"\lambda = \dfrac{3.0 \times 10^{8}}{4.3 \times 10^{14}} = 7.0 \times 10^{-7}\ \text{m}"),
                   S("Convert to nm", math=r"7.0 \times 10^{-7}\ \text{m} = 700\ \text{nm}"),
                   S("Answer", text="The wavelength is about 700 nm, which is at the red end of the visible spectrum."),
               ]),
            MISTAKE("Mixing up the order", "Going from radio waves to gamma rays the frequency **increases** and the wavelength **decreases**. "
                    "A memory aid for the order from long wavelength to short: Radio, Microwave, Infrared, Visible, Ultraviolet, X-ray, Gamma."),
            MISTAKE("Saying that some EM waves are faster", "All EM waves travel at the **same speed** in a vacuum. Gamma rays are not faster than radio waves. They differ in frequency and wavelength."),
            QUIZ("Which colour of visible light has the shortest wavelength?", ["Red", "Green", "Yellow", "Violet"], 3,
                 "Violet is at the short-wavelength (high-frequency) end of the visible spectrum.",
                 hint="Which colour is bent most by a prism?",
                 feedback=["Red has the longest wavelength.", "Green is in the middle.", "Yellow is nearer the red end.", ""]),
            QUIZ("Which of these has the highest frequency?", ["Microwaves", "Visible light", "X-rays", "Radio waves"], 2,
                 "Going along the spectrum from radio, the frequency rises. X-rays are higher than visible light, microwaves and radio waves.",
                 hint="Put the four in order from radio to gamma.",
                 feedback=["Microwaves are lower frequency than visible light.", "Visible light is lower than X-rays.", "", "Radio waves have the lowest frequency."]),
            TIP("Where this appears: the electromagnetic spectrum is common in Paper 1 (order, properties, uses) and in Paper 2. The Board's examiners report that candidates can name a member and its use, "
                "but often cannot state its wavelength range or the property that makes the use possible. Learn one property for each use, for example: infrared is given off by hot objects, so it is used in thermal cameras."),
            PQ("List the regions of the electromagnetic spectrum in order of increasing frequency.",
               "Radio waves, microwaves, infrared, visible light, ultraviolet, X-rays, gamma rays."),
            PQ("State two properties that all electromagnetic waves have in common.",
               "Any two of: they are transverse; they travel at the same speed in a vacuum (3.0 x 10^8 m/s); they can travel through a vacuum; they carry energy."),
            PQ(r"A radio station broadcasts at 90 MHz. Calculate the wavelength. (Speed of radio waves $= 3.0 \times 10^{8}$ m/s)",
               r"$\lambda = v/f = 3.0 \times 10^{8} / 9.0 \times 10^{7} = 3.3$ m."),
            PQ("Name one use and one danger of X-rays, and say why they are dangerous.",
               "Use: taking photographs of bones. Danger: X-rays can damage or kill cells and cause cancer, because they have high frequency and therefore high energy."),
            SUM("A prism disperses white light because each colour is refracted by a different amount: violet most, red least.",
                "The EM spectrum in order of increasing frequency: radio, microwave, infrared, visible, ultraviolet, X-ray, gamma.",
                r"All EM waves are transverse, travel through a vacuum and travel at $3.0 \times 10^{8}$ m/s there.",
                r"Use $v = f\lambda$ with $v = 3.0 \times 10^{8}$ m/s. Higher frequency means shorter wavelength and more energy."),
        ],
    ),
    # ------------------------------------------------------------------ 11. Speed of sound and echoes
    lesson(
        module=WAVES,
        topic="Sound waves",
        title="Production, speed of sound and echoes",
        slug="phc-sound-speed-echoes",
        minutes=22,
        summary=r"Sound is a longitudinal wave made by vibrations that needs a medium. Use $v = 2d/t$ for echoes, and know that sound travels faster in solids than in liquids and gases.",
        objectives=[
            "Explain how sound is produced and why it needs a medium",
            "Compare the speed of sound in solids, liquids and gases",
            "Use speed = distance / time and v = 2d/t for echoes",
            "Describe a method of measuring the speed of sound in air",
        ],
        key_concepts=["Sound", "Vibration", "Longitudinal wave", "Speed of sound", "Echo", "Sonar"],
        blocks=[
            H("Introduction"),
            T("During a storm over Douala you see the lightning flash first and hear the thunder several seconds later. The light has reached you almost at once. "
              "The sound is much slower. By counting the seconds between flash and thunder you can tell how far away the storm is."),
            T("This lesson looks at how sound is made, how fast it travels, and how we use echoes to measure distances."),
            H("How sound is made and how it travels"),
            D("Sound is produced by a **vibrating** object. The vibrating object pushes and pulls on the air (or other medium) around it, making a chain of "
              "**compressions and rarefactions**. So sound is a **longitudinal wave**.",
              title="Sound"),
            T("Sound needs a **medium** (solid, liquid or gas) because the vibrations are passed from particle to particle. It **cannot travel through a vacuum**. "
              "Evidence: if an electric bell rings inside a glass jar and the air is pumped out, the sound fades away although you can still see the hammer moving."),
            KEY("Speed of sound in different materials", "The values below are typical. They vary a little between textbooks and with temperature, so check your textbook.",
                cards=[["Air (about 20 degrees C)", "about 340 m/s"],
                       ["Water", "about 1500 m/s"],
                       ["Steel", "about 5000 m/s"]]),
            T("Sound travels fastest in **solids**, slower in **liquids** and slowest in **gases**, because the particles in a solid are closer together and pass the vibration on more quickly. "
              "In air the speed **increases with temperature**. It does not depend on the loudness or the pitch of the sound."),
            H("Echoes"),
            D("An **echo** is sound that has been **reflected** from a hard surface such as a wall, a cliff or the sea floor and then heard again. "
              "The sound travels to the surface and back, so the total distance is **twice** the distance to the surface.",
              title="Echo"),
            D("If a sound takes time $t$ to go to a reflecting surface and come back, the distance $d$ to the surface is found from the speed $v$:",
              title="Echo formula", formula=r"v = \dfrac{2d}{t} \qquad d = \dfrac{vt}{2}",
              note="d in metres (m), t in seconds (s), v in metres per second (m/s)."),
            T("Your ear can tell two sounds apart if they are at least about 0.1 s apart. In air this means a wall must be at least about 17 m away to hear a clear echo."),
            H("Worked examples"),
            EX("Worked example 1: a cliff", intro=(
                "A girl shouts near a cliff and hears the echo 1.5 s later. The speed of sound in air is 340 m/s. How far away is the cliff?"),
               steps=[
                   S("The sound goes there and back", text="Total distance = $v \\times t$ = 340 x 1.5 = 510 m."),
                   S("Halve it", math=r"d = \dfrac{340 \times 1.5}{2} = 255\ \text{m}"),
                   S("Answer", text="The cliff is 255 m away."),
               ]),
            EX("Worked example 2: lightning and thunder", intro=(
                "You hear thunder 6.0 s after you see the lightning. How far away is the lightning? (Speed of sound = 340 m/s. Light arrives almost at once.)"),
               steps=[
                   S("Only the sound travels the distance in 6 s", text="The time for the light is so small it can be ignored. There is no 'there and back' here."),
                   S("Distance = speed x time", math=r"d = vt = 340 \times 6.0 = 2040\ \text{m}"),
                   S("Answer", text="The lightning is about 2000 m (2.0 km) away."),
               ]),
            EX("Worked example 3: a fishing boat's sonar", intro=(
                "A fishing boat sends a pulse of sound straight down. The echo from the sea floor returns after 0.80 s. The speed of sound in sea water is 1500 m/s. Find the depth of the water."),
               steps=[
                   S("Echo formula", math=r"d = \dfrac{vt}{2} = \dfrac{1500 \times 0.80}{2}"),
                   S("Calculate", math=r"d = 600\ \text{m}"),
                   S("Answer", text="The water is 600 m deep."),
               ]),
            EX("Worked example 4: measuring the speed of sound", intro=(
                "A student stands 85 m from a tall wall and claps. A friend with a stopwatch finds that the echo returns 0.50 s later. Find the speed of sound."),
               steps=[
                   S("Total distance travelled", math=r"2 \times 85 = 170\ \text{m}"),
                   S("Speed = distance / time", math=r"v = \dfrac{170}{0.50} = 340\ \text{m/s}"),
                   S("Answer", text="The speed of sound is 340 m/s. Measuring a longer time (for example, 20 claps) and dividing makes the result more accurate."),
               ]),
            MISTAKE("Forgetting to halve", "In an echo problem the sound travels to the surface and back. If you use $d = vt$ you get **twice** the real distance. For an echo use $d = vt/2$. "
                    "For thunder and lightning the sound travels only one way, so $d = vt$."),
            MISTAKE("Saying sound travels faster in gases", "Sound travels **slowest** in gases and **fastest** in solids, the opposite of what many students guess."),
            QUIZ("Sound cannot travel through", ["a steel bar", "water", "air", "a vacuum"], 3,
                 "Sound is a vibration of particles. In a vacuum there are no particles, so sound cannot travel.",
                 hint="What does a sound wave need to pass from one place to another?",
                 feedback=["Sound travels very fast in steel.", "Sound travels well in water.", "Sound travels in air, though more slowly than in water.", ""]),
            QUIZ("An echo is heard 2.0 s after a shout. The speed of sound is 340 m/s. How far away is the reflecting wall?", ["170 m", "340 m", "680 m", "1360 m"], 1,
                 "d = vt / 2 = 340 x 2.0 / 2 = 340 m.",
                 hint="The sound goes to the wall and back, so halve the total distance.",
                 feedback=["You halved twice.", "", "You forgot to halve. 680 m is the total distance there and back.", "You multiplied by 2 instead of dividing."]),
            TIP("Where this appears: speed of sound and echo calculations appear in Paper 1 and Paper 2. Remember that echo questions need $d = vt/2$, and always quote the unit (m or km)."),
            PQ("Explain why sound cannot travel through a vacuum.",
               "Sound is a longitudinal wave in which particles pass the vibration on to their neighbours. A vacuum has no particles, so there is nothing to carry the vibration."),
            PQ("A ship sends a sound pulse to the sea bed and the echo returns after 0.40 s. The speed of sound in water is 1500 m/s. Find the depth of the sea.",
               r"$d = vt/2 = 1500 \times 0.40 / 2 = 300$ m."),
            PQ("A man stands 100 m from a wall and claps. He hears the echo 0.60 s later. Calculate the speed of sound.",
               r"Distance there and back $= 200$ m. $v = 200 / 0.60 = 333$ m/s (about 330 m/s)."),
            PQ("You hear thunder 4.0 s after seeing a lightning flash. Calculate how far away the lightning is. (Speed of sound = 340 m/s)",
               r"$d = vt = 340 \times 4.0 = 1360$ m (about 1.4 km)."),
            SUM("Sound is made by vibrations and is a longitudinal wave that needs a medium; it cannot travel through a vacuum.",
                "Sound is fastest in solids, slower in liquids, slowest in gases (about 340 m/s in air, about 1500 m/s in water).",
                r"For an echo, $d = vt/2$ because the sound travels there and back.",
                "Speed of sound in air increases with temperature; it does not depend on pitch or loudness."),
        ],
    ),
    # ------------------------------------------------------------------ 12. Pitch, loudness and timbre
    lesson(
        module=WAVES,
        topic="Sound waves",
        title="Pitch, loudness, quality and ultrasound",
        slug="phc-pitch-loudness-timbre",
        minutes=22,
        summary="Pitch depends on frequency, loudness on amplitude and quality (timbre) on the shape of the wave. Learn the range of hearing and the uses of ultrasound.",
        objectives=[
            "Link pitch to frequency, loudness to amplitude and timbre to wave shape",
            "Interpret simple oscilloscope-type sound traces",
            "State the range of human hearing and define ultrasound and infrasound",
            "Describe uses of ultrasound and calculate its wavelength or echo time",
        ],
        key_concepts=["Pitch", "Frequency", "Loudness", "Amplitude", "Timbre", "Ultrasound", "Infrasound"],
        blocks=[
            H("Introduction"),
            T("A flute and a drum can play the same loudness but sound very different. A talking drum changes its note when the player squeezes it. "
              "A hospital scanner uses sound you cannot even hear. How do we describe sounds?"),
            T("We use three properties: **pitch**, **loudness** and **timbre** (quality). Each is linked to a feature of the sound wave."),
            H("The three properties of a note"),
            KEY("Link each property to the wave", "Learn the pairs.",
                cards=[["Pitch", "How high or low a note sounds. It depends on the **frequency**. High frequency = high pitch."],
                       ["Loudness", "How loud or soft a sound is. It depends on the **amplitude**. Larger amplitude = louder sound (more energy). Loudness is measured in decibels (dB)."],
                       ["Timbre (quality)", "What makes a note on a flute sound different from the **same note** on a guitar. It depends on the **shape** of the waveform, because each instrument adds other frequencies (overtones)."]]),
            T("When a sound is shown on a microphone and an oscilloscope screen, a **higher pitch** shows **more waves** across the screen. A **louder** sound shows **taller** waves. "
              "A different instrument shows the same number of waves but a different shape."),
            CODE("""Compare two traces on the same screen settings:

Trace A: 4 waves, small height
Trace B: 8 waves, small height
Trace C: 4 waves, large height

B has double the frequency of A: higher pitch.
C has the same pitch as A but is louder.""", "text", title="Reading sound traces"),
            T("On a string instrument the pitch rises when the string is **shorter**, **tighter** or **thinner**. A guitar player presses the string against the neck to shorten it."),
            H("The range of hearing"),
            D("The normal human ear can hear sounds from about **20 Hz to 20 000 Hz** (20 kHz). Sound above 20 000 Hz is called **ultrasound**. "
              "Sound below 20 Hz is called **infrasound**.",
              title="Range of hearing"),
            KEY("Uses of ultrasound", "Ultrasound has a very short wavelength, so it can be directed in narrow beams and reflects from small details.",
                cards=[["Medical scans", "Pulses of ultrasound reflect from boundaries inside the body (for example a baby in the womb). The echo times build up a picture. Ultrasound does not harm the body as X-rays can."],
                       ["Sonar", "Ships measure the sea depth and find shoals of fish by timing echoes."],
                       ["Cleaning and testing", "Ultrasound vibrations clean jewellery and find cracks in metal."],
                       ["Animals", "Bats use ultrasound echoes to find insects in the dark. Elephants use infrasound to talk over long distances."]]),
            H("Worked examples"),
            EX("Worked example 1: a tuning fork", intro=(
                "A tuning fork vibrates at 256 Hz. Find its period and the wavelength of the sound in air. (Speed of sound = 340 m/s)"),
               steps=[
                   S("Period", math=r"T = \dfrac{1}{f} = \dfrac{1}{256} = 0.0039\ \text{s}"),
                   S("Wavelength", math=r"\lambda = \dfrac{v}{f} = \dfrac{340}{256} = 1.3\ \text{m}"),
                   S("Answer", text="The period is 0.0039 s (3.9 ms) and the wavelength is 1.3 m."),
               ]),
            EX("Worked example 2: an ultrasound scan", intro=(
                "A medical scanner uses ultrasound of frequency 3.0 MHz. The speed of sound in body tissue is 1540 m/s. Find the wavelength."),
               steps=[
                   S("Frequency in hertz", math=r"f = 3.0\ \text{MHz} = 3.0 \times 10^{6}\ \text{Hz}"),
                   S("Wavelength", math=r"\lambda = \dfrac{v}{f} = \dfrac{1540}{3.0 \times 10^{6}} = 5.1 \times 10^{-4}\ \text{m}"),
                   S("Answer", text="The wavelength is about 0.51 mm, short enough to show small details."),
               ]),
            EX("Worked example 3: a bat", intro=(
                "A bat sends out a pulse of ultrasound and hears the echo from an insect 0.010 s later. The speed of sound in air is 340 m/s. How far away is the insect?"),
               steps=[
                   S("Echo formula", math=r"d = \dfrac{vt}{2} = \dfrac{340 \times 0.010}{2}"),
                   S("Answer", math=r"d = 1.7\ \text{m}"),
               ]),
            MISTAKE("Mixing up pitch and loudness", "A **loud** sound has a large **amplitude**. A **high** sound has a high **frequency**. "
                    "A loud note can be low in pitch, and a quiet note can be high in pitch."),
            MISTAKE("Saying that a louder sound is faster", "Loudness does not change the speed of sound. It changes the amplitude, which is the energy of the wave."),
            QUIZ("A sound becomes higher in pitch but its loudness stays the same. Which quantity increases?", ["Amplitude", "Frequency", "Wavelength", "Speed"], 1,
                 "Pitch depends on frequency. Higher pitch means higher frequency.",
                 hint="Which quantity is linked to pitch?",
                 feedback=["Amplitude is linked to loudness, which stays the same.", "",
                           "The wavelength gets shorter when the frequency rises (same speed).", "The speed of sound in air does not change with pitch."]),
            QUIZ("The same note is played on a flute and a trumpet. They sound different because they have different", ["frequency", "amplitude", "wave shape (quality or timbre)", "speed"], 2,
                 "The same note means the same frequency. The different overtones give a different waveform shape, which we hear as a different timbre.",
                 hint="The two notes have the same pitch and can have the same loudness.",
                 feedback=["The same note means the same frequency.", "They can be equally loud.", "", "The speed of sound is the same for both in air."]),
            TIP("Where this appears: pitch, loudness and timbre are common in Paper 1 (link each to frequency, amplitude or shape; read a trace) and in Paper 2 (uses of ultrasound, echo calculations). "
                "The Board's examiners report that candidates can identify the use of a device (for example a microphone) but not always the energy change: a microphone changes sound energy into electrical energy."),
            PQ("State which property of a sound wave determines (a) the pitch and (b) the loudness of the sound.",
               "(a) The frequency of the wave determines the pitch. (b) The amplitude of the wave determines the loudness."),
            PQ("Two sound waves are displayed on the same oscilloscope settings. Wave A has 5 waves on the screen and wave B has 10 waves on the screen, both with the same height. Compare the sounds.",
               "B has twice the frequency of A, so it has a higher pitch. The waves have the same amplitude, so they have the same loudness."),
            PQ("Define ultrasound and give two uses.",
               "Ultrasound is sound of frequency above 20 000 Hz, higher than the human ear can hear. Uses: scanning an unborn baby, sonar to measure the depth of the sea, cleaning, testing metals for cracks."),
            PQ("A bat emits ultrasound of frequency 50 kHz. Find the wavelength in air. (Speed of sound = 340 m/s)",
               r"$\lambda = v/f = 340 / 50\,000 = 0.0068$ m = 6.8 mm."),
            SUM("Pitch depends on frequency; loudness depends on amplitude; timbre depends on the shape of the wave.",
                "The human ear hears about 20 Hz to 20 000 Hz. Ultrasound is above 20 kHz; infrasound is below 20 Hz.",
                "Ultrasound is used for medical scans, sonar, cleaning and crack testing.",
                r"Use $v = f\lambda$ and $d = vt/2$ for ultrasound calculations."),
        ],
    ),
    # ------------------------------------------------------------------ 13. Electrostatics
    lesson(
        module=ELEC,
        topic="Electrostatics",
        title="Static electricity, electric fields and lightning conductors",
        slug="phc-electrostatics",
        minutes=25,
        summary="Rubbing moves electrons from one material to another and leaves charges that attract or repel. Learn charging by friction and induction, electric fields, Coulomb's law and how a lightning conductor protects a building.",
        objectives=[
            "State the law of electric charges and explain charging by friction in terms of electrons",
            "Describe charging by induction and use a gold-leaf electroscope",
            "Describe electric fields and draw field lines",
            "Use Coulomb's law and explain how a lightning conductor works",
        ],
        key_concepts=["Electric charge", "Charging by friction", "Induction", "Electric field", "Coulomb's law", "Lightning conductor"],
        blocks=[
            H("Introduction"),
            T("In the dry harmattan season you touch a metal car door and feel a small shock. Rub a plastic ruler on dry hair and it picks up little pieces of paper. "
              "In a storm over Douala, lightning strikes the ground. All of these are **static electricity**: electric charge that stays in one place instead of flowing in a wire."),
            H("Electric charge"),
            T("Everything is made of atoms. An atom has **protons** (positive charge) in the nucleus and **electrons** (negative charge) around it. "
              "Normally an atom has equal numbers of both, so it is **neutral**. Only the **electrons** can move from one object to another."),
            D("Charge is measured in **coulombs (C)**. The charge of one electron is $-1.6 \\times 10^{-19}$ C. A material that has gained electrons is **negatively charged**; "
              "a material that has lost electrons is **positively charged**.",
              title="Charge"),
            KEY("The law of electric charges", "Remember the short rule.",
                cards=[["Like charges", "Two positive charges, or two negative charges, **repel** each other."],
                       ["Unlike charges", "A positive charge and a negative charge **attract** each other."]]),
            T("A **charged** object can also attract an **uncharged** one (that is why the ruler picks up paper). So repulsion is the only certain test for the sign of a charge."),
            H("Charging by friction"),
            T("When a polythene rod is rubbed with a cloth, electrons move from the cloth to the rod. The rod gains electrons and becomes **negative**. "
              "The cloth loses electrons and becomes **positive**. Both charges are **equal in size**. A perspex or glass rod rubbed with silk loses electrons and becomes **positive**."),
            D("A **conductor** (metals, graphite, the human body, damp air) lets charge move through it easily. An **insulator** (plastic, glass, dry air, rubber) does not. "
              "Only insulators can hold charge in one place when rubbed, which is why you hold a rubbed rod with an insulating handle.",
              title="Conductors and insulators"),
            H("Charging by induction"),
            T("A conductor can be charged **without touching** the charged rod. This is **induction**. A metal sphere on an insulating stand is used."),
            KEY("Steps for charging a metal sphere by induction", "Follow the steps in this exact order.",
                cards=[["1", "Bring a negative rod **near** (not touching) the sphere. The electrons in the sphere are repelled to the far side."],
                       ["2", "Touch the far side with a finger (earth the sphere). The repelled electrons flow to the earth."],
                       ["3", "Remove the finger (the earth connection) **first**, while the rod is still there."],
                       ["4", "Then remove the rod. The sphere is left with a **positive** charge, spread over its surface."]]),
            T("The charge left by induction is **opposite** to the charge on the rod. If you removed the rod before the earth connection, the electrons would flow back and the sphere would be neutral again."),
            T("A **gold-leaf electroscope** is a metal cap and rod with a thin gold leaf that stands out from a metal plate. If a charged object is brought near the cap, charge is spread on the plate and leaf, and the leaf rises because the **like charges repel**. "
              "To test the sign of the charge on an electroscope, bring up a rod of known sign. If the leaf rises **further**, the charges are the same sign. If it **falls**, they are opposite."),
            H("Electric fields"),
            D("An **electric field** is a region where a charged particle feels a force. The **direction** of the field at a point is the direction of the force on a small **positive** charge placed there. "
              "It is shown by **field lines**, which start on positive charges and end on negative charges.",
              title="Electric field"),
            IMG("f5ph-c-field-lines.svg",
                "Three diagrams. A positive charge with field lines pointing outwards. A negative charge with field lines pointing inwards. Two charged parallel plates, positive above and negative below, with evenly spaced parallel field lines pointing downwards between them.",
                "Figure 1. Field lines point away from positive charges and towards negative charges."),
            T("Where the lines are **close together** the field is **strong**. Between two parallel plates the lines are parallel and evenly spaced, so the field is the same everywhere (a uniform field)."),
            H("Coulomb's law"),
            D("The force between two small charged objects is **directly proportional to the product of the charges** and **inversely proportional to the square of the distance** between them.",
              title="Coulomb's law", formula=r"F = \dfrac{k\,Q_1 Q_2}{r^{2}}",
              note="F in newtons (N), charges in coulombs (C), r in metres (m). In air, $k \\approx 9.0 \\times 10^{9}$ N m² per C². Check whether your syllabus needs this formula in numbers or just in words."),
            H("Worked examples"),
            EX("Worked example 1: charge by friction", intro=(
                r"A polythene rod gains $3.0 \times 10^{10}$ electrons when it is rubbed. Find the charge on the rod. (Charge of one electron $= 1.6 \times 10^{-19}$ C)"),
               steps=[
                   S("Charge = number x charge of one electron", math=r"Q = 3.0 \times 10^{10} \times 1.6 \times 10^{-19}"),
                   S("Calculate", math=r"Q = 4.8 \times 10^{-9}\ \text{C}"),
                   S("Answer", text="The rod has a charge of $-4.8 \\times 10^{-9}$ C (negative, because it gained electrons)."),
               ]),
            EX("Worked example 2: force between two charges", intro=(
                r"Two small charged spheres have charges $3.0 \times 10^{-6}$ C and $2.0 \times 10^{-6}$ C and are 0.30 m apart in air. Find the force between them. "
                "What is the force if the distance is doubled to 0.60 m?"),
               steps=[
                   S("Coulomb's law", math=r"F = \dfrac{9.0 \times 10^{9} \times 3.0 \times 10^{-6} \times 2.0 \times 10^{-6}}{(0.30)^{2}}"),
                   S("Top line", math=r"9.0 \times 10^{9} \times 6.0 \times 10^{-12} = 5.4 \times 10^{-2}"),
                   S("Divide by 0.09", math=r"F = 0.60\ \text{N}"),
                   S("Distance doubled", text="The force depends on $1/r^2$. Doubling $r$ divides the force by $2^2 = 4$."),
                   S("Answer", math=r"F = \dfrac{0.60}{4} = 0.15\ \text{N}"),
               ]),
            H("Lightning conductors"),
            T("A thundercloud can build up a huge charge. Lightning is a very large spark between the cloud and the ground. It can start fires and kill. "
              "A **lightning conductor** protects a tall building."),
            IMG("f5ph-c-lightning.svg",
                "A building with a pointed metal rod on its roof. A thick copper strip runs from the rod down the wall to a metal plate buried in damp ground. A cloud above is marked with minus signs.",
                "Figure 2. A lightning conductor: pointed rod, thick copper strip and buried plate."),
            T("The rod has a **sharp point**, and charges build up and leak away most easily at sharp points. The negative cloud induces a positive charge on the building and on the point. "
              "The air near the point is ionised and the charge leaks off gradually. If lightning does strike, the **thick copper strip** (low resistance) carries the huge current safely to the **metal plate buried in damp earth**, "
              "and away from the building."),
            KEY("Other effects of static electricity", "Useful and dangerous.",
                cards=[["Useful", "Photocopiers and laser printers, paint sprayers (the paint droplets all have the same charge so they spread evenly), and dust collectors in chimneys."],
                       ["Dangerous", "Sparks can ignite petrol vapour. Fuel tankers are earthed with a chain or cable so that charge cannot build up while fuel is moving."]]),
            MISTAKE("Saying that protons move", "In charging, **electrons** move. A rod becomes positive because it **loses electrons**, not because it gains protons."),
            MISTAKE("Removing the rod before the earth connection", "In charging by induction, disconnect the earth connection **while the rod is still in place**. If the rod goes first, the electrons flow back in and the sphere is not charged."),
            QUIZ("A polythene rod is rubbed with a cloth and becomes negative. The cloth becomes", ["negative, because it gained electrons", "positive, because it lost electrons", "positive, because it gained protons", "neutral"], 1,
                 "Electrons move from the cloth to the rod. The cloth loses electrons and is left positive.",
                 hint="Where did the rod's extra electrons come from?",
                 feedback=["The cloth is the one that gave up electrons.", "", "Protons cannot move in rubbing.", "The charges on the rod and cloth are equal and opposite."]),
            QUIZ("Two charged spheres 4 cm apart repel with a force F. The distance is changed to 2 cm. The force is now", ["F/4", "F/2", "2F", "4F"], 3,
                 "The force is proportional to 1/r squared. Halving the distance makes the force four times larger.",
                 hint="Force depends on 1 over r squared.",
                 feedback=["That would be doubling the distance.", "The relationship is with r squared, not r.", "That is the effect of r^1. Square the factor.", ""]),
            TIP("Where this appears: electrostatics is in Paper 1 and Paper 2. The Board's examiners report that candidates did poorly on static electricity: many could not explain that damp cloth conducts charge away, "
                "or that the earth connection must be removed with the rod still in place. Learn the induction steps in order."),
            PQ("State the law of electric charges and describe what happens when a perspex rod is rubbed with a silk cloth.",
               "Like charges repel and unlike charges attract. Electrons move from the perspex to the silk, so the perspex becomes positive and the silk becomes negative."),
            PQ(r"A rod carries a charge of $-3.2 \times 10^{-9}$ C. How many extra electrons does it hold? (Charge of an electron $= 1.6 \times 10^{-19}$ C)",
               r"$n = Q/e = 3.2 \times 10^{-9} / 1.6 \times 10^{-19} = 2.0 \times 10^{10}$ electrons."),
            PQ("Describe how a metal sphere on an insulating stand can be given a positive charge using a negatively charged rod.",
               "Hold the negative rod near the sphere without touching it. Earth the far side with a finger so electrons flow away. Remove the earth connection first, then remove the rod. The sphere is left positive."),
            PQ("Explain how a lightning conductor protects a building.",
               "The pointed metal rod lets charge leak away gradually. If lightning strikes, the thick copper strip carries the large current to a metal plate buried in damp earth, so the current does not pass through the building."),
            SUM("Like charges repel and unlike charges attract. Only electrons move in charging.",
                "Rubbing transfers electrons by friction; induction charges a conductor without touching it, giving the opposite charge, with the earth removed before the rod.",
                "An electric field is a region where a charge feels a force; field lines point away from positive and towards negative charges.",
                r"Coulomb's law: $F = kQ_1Q_2/r^2$. A lightning conductor has a sharp point, a thick copper strip and a buried plate."),
        ],
    ),
    # ------------------------------------------------------------------ 14. Current, potential difference, EMF and Ohm's law
    lesson(
        module=ELEC,
        topic="Current, potential difference and Ohm's law",
        title="Current, potential difference, EMF and Ohm's law",
        slug="phc-current-pd-ohm",
        minutes=24,
        summary=r"Current is charge per second, potential difference is energy per coulomb, and Ohm's law links them: $V = IR$. Learn the meters, the units and how an EMF differs from a p.d.",
        objectives=[
            "Define electric current, potential difference and EMF with their units",
            "Use I = Q/t, V = W/Q and V = IR",
            "Connect an ammeter and a voltmeter correctly",
            "State Ohm's law and read a current-voltage graph",
        ],
        key_concepts=["Current", "Ampere", "Potential difference", "Volt", "EMF", "Resistance", "Ohm's law"],
        blocks=[
            H("Introduction"),
            T("When you charge a phone at home in Yaounde, the charger says 5 V and 2 A. What do these numbers mean? "
              "**Volts** tell you how much energy each unit of charge carries. **Amperes** tell you how much charge flows each second."),
            T("A good picture is water in a pipe. The **current** is how much water flows past each second. The **voltage** is the pressure that pushes it. "
              "In this lesson we make these ideas exact."),
            H("Electric current"),
            D("**Electric current** is the rate of flow of electric charge. It is the charge $Q$ passing a point each second.",
              title="Current", formula=r"I = \dfrac{Q}{t} \qquad Q = It",
              note="Current $I$ in amperes (A), charge $Q$ in coulombs (C), time $t$ in seconds (s). 1 A = 1 C per second."),
            T("In a metal wire the charge carriers are **electrons**, which flow from the negative terminal of the cell to the positive terminal. "
              "But we use **conventional current**, which is drawn as flowing from the **positive** terminal round the circuit to the **negative**, the opposite way to the electrons. "
              "Always draw arrows for current in the conventional direction."),
            T("An **ammeter** measures current. It is connected in **series** (in the same loop, so all the current passes through it) and has a very small resistance."),
            H("Potential difference and EMF"),
            D("The **potential difference (p.d.)** between two points is the energy (work done) changed from electrical energy to other forms when **one coulomb** of charge passes between the points.",
              title="Potential difference", formula=r"V = \dfrac{W}{Q}",
              note="V in volts (V), W in joules (J), Q in coulombs (C). 1 V = 1 J per C."),
            D("The **electromotive force (EMF)** of a source such as a cell is the energy (work done) changed from other forms (for example chemical energy) to electrical energy when **one coulomb** of charge is driven round the complete circuit.",
              title="EMF", formula=r"E = \dfrac{W}{Q}",
              note="EMF is measured in volts, but it is not a force. It is a property of the source."),
            KEY("EMF and p.d.", "Both are measured in volts, but they are different.",
                cards=[["EMF", "Energy **given** to each coulomb by the source (other forms into electrical)."],
                       ["Potential difference", "Energy **taken** from each coulomb by a component (electrical into heat, light and so on)."]]),
            T("A **voltmeter** measures p.d. It is connected in **parallel** across the component, and it has a very large resistance so it takes almost no current."),
            H("Resistance and Ohm's law"),
            D("The **resistance** $R$ of a conductor is the p.d. across it divided by the current through it. Its unit is the **ohm** ($\\Omega$). "
              "1 ohm is 1 volt per ampere.",
              title="Resistance", formula=r"R = \dfrac{V}{I}"),
            D("**Ohm's law**: the current through a metallic conductor is **directly proportional** to the p.d. across it, provided the temperature and other physical conditions stay constant.",
              title="Ohm's law", formula=r"V = IR"),
            IMG("f5ph-c-ohm-graphs.svg",
                "Two current-voltage graphs with current on the vertical axis and voltage on the horizontal axis. Left: a straight line through the origin for an ohmic conductor. Right: a curve through the origin that rises more and more gently for a filament lamp.",
                "Figure 1. An ohmic conductor gives a straight line; a filament lamp does not."),
            T("A conductor that obeys Ohm's law is called **ohmic**. Its I-V graph is a straight line through the origin, so its resistance is the same for every p.d. "
              "A **filament lamp** is **not** ohmic. As the filament gets hot, its resistance **increases**, so the graph bends over."),
            H("Worked examples"),
            EX("Worked example 1: charge and current", intro=(
                "A current of 0.50 A flows through a lamp for 2.0 minutes. How much charge passes through the lamp? How many electrons is that? (Charge of one electron $= 1.6 \\times 10^{-19}$ C)"),
               steps=[
                   S("Change the time to seconds", math=r"t = 2.0 \times 60 = 120\ \text{s}"),
                   S("Charge", math=r"Q = It = 0.50 \times 120 = 60\ \text{C}"),
                   S("Number of electrons", math=r"n = \dfrac{Q}{e} = \dfrac{60}{1.6 \times 10^{-19}} = 3.75 \times 10^{20}"),
                   S("Answer", text="60 C of charge, which is about $3.8 \\times 10^{20}$ electrons."),
               ]),
            EX("Worked example 2: a phone charger", intro=(
                "A phone charger supplies a current of 2.0 A for 30 minutes. Find the charge that flows."),
               steps=[
                   S("Time in seconds", math=r"t = 30 \times 60 = 1800\ \text{s}"),
                   S("Charge", math=r"Q = It = 2.0 \times 1800 = 3600\ \text{C}"),
               ]),
            EX("Worked example 3: energy and potential difference", intro=(
                "A 12 V battery drives 5.0 C of charge through a lamp. How much electrical energy is changed to heat and light?"),
               steps=[
                   S("Rearrange V = W/Q", math=r"W = QV"),
                   S("Substitute", math=r"W = 5.0 \times 12 = 60\ \text{J}"),
                   S("Answer", text="60 joules of electrical energy are changed in the lamp."),
               ]),
            EX("Worked example 4: using Ohm's law", intro=(
                "A resistor of 40 $\\Omega$ is connected across a 12 V supply. Find the current. "
                "A lamp has a p.d. of 6.0 V across it and a current of 0.30 A. Find its resistance."),
               steps=[
                   S("First part: rearrange V = IR", math=r"I = \dfrac{V}{R} = \dfrac{12}{40} = 0.30\ \text{A}"),
                   S("Second part", math=r"R = \dfrac{V}{I} = \dfrac{6.0}{0.30} = 20\ \Omega"),
                   S("Answer", text="The current is 0.30 A and the lamp's resistance is 20 ohms."),
               ]),
            TIP("Use the triangle V over I and R: cover the quantity you want. Cover V and you see I x R. Cover I and you see V over R. Cover R and you see V over I."),
            MISTAKE("Thinking current is used up", "Current is **not** used up by a lamp. The same current flows out of the lamp as flows in. What is used up (changed into other forms) is **energy**."),
            MISTAKE("Connecting the meters wrongly", "An **ammeter goes in series** and a **voltmeter goes in parallel**. If you put an ammeter across a cell, its tiny resistance causes a huge current and can damage the meter and the cell."),
            QUIZ("How is a voltmeter connected to measure the p.d. across a lamp?", ["In series with the lamp", "In parallel with the lamp", "Anywhere in the circuit", "Across the cell only"], 1,
                 "A voltmeter measures the p.d. between two points, so it is connected across (in parallel with) the lamp.",
                 hint="A voltmeter measures the difference between two points.",
                 feedback=["That is how an ammeter is connected.", "", "A voltmeter must be connected across the component being measured.", "That would measure the cell's p.d., not the lamp's."]),
            QUIZ("A current of 3.0 A flows for 10 s. How much charge passes?", ["0.30 C", "7.0 C", "13 C", "30 C"], 3,
                 "Q = It = 3.0 x 10 = 30 C.",
                 hint="Use Q = It.",
                 feedback=["You divided 3.0 by 10. Charge is current multiplied by time.", "You subtracted (10 - 3.0). Multiply instead.", "You added 3.0 and 10.", ""]),
            TIP("Where this appears: current electricity is tested every year. The Board's examiners report that candidates did better on current electricity than on most topics, but that many "
                "failed to define EMF correctly and to say that the sum of p.d.s in series equals the p.d. of the battery. Learn the definitions word for word, and write units on every answer."),
            PQ("Define (a) electric current and (b) potential difference, and state the unit of each.",
               "(a) Current is the rate of flow of charge, I = Q/t; unit ampere (A). (b) Potential difference between two points is the energy changed from electrical to other forms per coulomb of charge passing between them, V = W/Q; unit volt (V)."),
            PQ("A charge of 90 C passes through a wire in 30 s. Calculate the current.",
               r"$I = Q/t = 90/30 = 3.0$ A."),
            PQ("A kettle element has a resistance of 24 ohms and is connected to a 220 V supply. Calculate the current through it.",
               r"$I = V/R = 220/24 = 9.2$ A."),
            PQ("A cell has an EMF of 1.5 V. How much energy does it give to each coulomb of charge, and how much to 4.0 C?",
               "It gives 1.5 J to each coulomb. For 4.0 C: W = QE = 4.0 x 1.5 = 6.0 J."),
            SUM(r"Current is charge per second, $I = Q/t$, measured in amperes. It is drawn in the conventional direction (positive to negative).",
                r"Potential difference is energy per coulomb, $V = W/Q$, in volts. EMF is the energy given per coulomb by the source.",
                r"Ohm's law $V = IR$ for a constant temperature: an ohmic conductor gives a straight-line I-V graph.",
                "An ammeter is in series; a voltmeter is in parallel."),
        ],
    ),
    # ------------------------------------------------------------------ 15. Resistance, series and parallel circuits
    lesson(
        module=ELEC,
        topic="Resistance and circuits",
        title="Resistance, series circuits and parallel circuits",
        slug="phc-series-parallel",
        minutes=25,
        summary=r"Resistances add in series, $R = R_1 + R_2$; in parallel $1/R = 1/R_1 + 1/R_2$. Find the total resistance, the current and the p.d. across each part.",
        objectives=[
            "State the factors that affect the resistance of a wire",
            "State the rules for current and p.d. in series and parallel circuits",
            "Calculate the total resistance of resistors in series and in parallel",
            "Solve simple mixed circuits for current and p.d.",
        ],
        key_concepts=["Resistance", "Series circuit", "Parallel circuit", "Total resistance", "Potential difference", "Current"],
        blocks=[
            H("Introduction"),
            T("In a house in Bamenda, the lamps in every room are on separate switches. If one bulb blows, the others stay on. "
              "Old cheap strings of festival lights worked differently: when one bulb failed, the whole string went out. "
              "The difference is how the bulbs are connected: in **parallel** or in **series**."),
            H("What affects the resistance of a wire?"),
            T("Resistance is the opposition of a conductor to the flow of current. For a wire made of one material at a constant temperature:"),
            KEY("Factors affecting resistance", "Compare two wires of the same material.",
                cards=[["Length", "Resistance is **proportional to the length**. A wire twice as long has twice the resistance."],
                       ["Cross-sectional area", "Resistance is **inversely proportional to the area**. A thicker wire (twice the area) has half the resistance."],
                       ["Material", "Copper has a much lower resistance than nichrome of the same size. Copper is used for cables, nichrome for heating elements."],
                       ["Temperature", "For a metal, resistance **increases** when the temperature rises."]]),
            EX("Worked example 1: a wire", intro=(
                "A wire has a resistance of 10 $\\Omega$. A second wire of the same material is twice as long and has twice the cross-sectional area. What is its resistance?"),
               steps=[
                   S("Twice as long", text="This doubles the resistance: 20 ohms."),
                   S("Twice the area", text="This halves the resistance: 10 ohms."),
                   S("Answer", text="The resistance is still 10 ohms, because the two changes cancel."),
               ]),
            H("Resistors in series"),
            T("In a **series circuit** the components are joined one after the other in a single loop."),
            IMG("f5ph-c-circuit-series.svg",
                "A series circuit: a 6 V cell, a 2 ohm resistor R1, a 4 ohm resistor R2 and an ammeter, all in one closed loop.",
                "Figure 1. A series circuit."),
            KEY("Rules for a series circuit", "Learn all three.",
                cards=[["Current", "The **same current** flows through every component: $I = I_1 = I_2$."],
                       ["Potential difference", "The p.d.s **add up** to the p.d. of the supply: $V = V_1 + V_2$."],
                       ["Resistance", r"The total resistance is the **sum**: $R = R_1 + R_2 + R_3 \dots$"]]),
            EX("Worked example 2: a series circuit", intro=(
                "In the circuit of Figure 1, find the total resistance, the current, and the p.d. across each resistor."),
               steps=[
                   S("Total resistance", math=r"R = R_1 + R_2 = 2 + 4 = 6\ \Omega"),
                   S("Current from Ohm's law", math=r"I = \dfrac{V}{R} = \dfrac{6}{6} = 1.0\ \text{A}"),
                   S("p.d. across R1", math=r"V_1 = IR_1 = 1.0 \times 2 = 2.0\ \text{V}"),
                   S("p.d. across R2", math=r"V_2 = IR_2 = 1.0 \times 4 = 4.0\ \text{V}"),
                   S("Answer", text="Total resistance 6 ohms, current 1.0 A, and p.d.s of 2.0 V and 4.0 V."),
               ], check=r"2.0 + 4.0 = 6.0\ \text{V, the supply p.d.}"),
            H("Resistors in parallel"),
            T("In a **parallel circuit** there are separate branches, and the current has a choice of paths."),
            IMG("f5ph-c-circuit-parallel.svg",
                "A parallel circuit: a 6 V cell and an ammeter in the main wire, which splits into two branches containing a 6 ohm resistor R1 and a 3 ohm resistor R2.",
                "Figure 2. A parallel circuit."),
            KEY("Rules for a parallel circuit", "Learn all three.",
                cards=[["Potential difference", "The **same p.d.** is across every branch: $V = V_1 = V_2$."],
                       ["Current", "The currents in the branches **add up** to the current from the supply: $I = I_1 + I_2$."],
                       ["Resistance", r"$\dfrac{1}{R} = \dfrac{1}{R_1} + \dfrac{1}{R_2} + \dots$ The total is **smaller** than the smallest resistor."]]),
            T(r"For **two** resistors you can use $R = \dfrac{R_1 R_2}{R_1 + R_2}$ (product over sum)."),
            EX("Worked example 3: a parallel circuit", intro=(
                "In the circuit of Figure 2, find the total resistance, the current in each branch and the current in the main wire."),
               steps=[
                   S("Total resistance", math=r"\dfrac{1}{R} = \dfrac{1}{6} + \dfrac{1}{3} = \dfrac{1 + 2}{6} = \dfrac{1}{2} \Rightarrow R = 2\ \Omega"),
                   S("Branch 1 (6 V across 6 ohms)", math=r"I_1 = \dfrac{V}{R_1} = \dfrac{6}{6} = 1.0\ \text{A}"),
                   S("Branch 2 (6 V across 3 ohms)", math=r"I_2 = \dfrac{6}{3} = 2.0\ \text{A}"),
                   S("Main wire", math=r"I = I_1 + I_2 = 1.0 + 2.0 = 3.0\ \text{A}"),
               ], check=r"I = \dfrac{V}{R} = \dfrac{6}{2} = 3.0\ \text{A}"),
            H("A mixed circuit"),
            IMG("f5ph-c-circuit-mixed.svg",
                "A 12 V cell with a 4 ohm resistor R1 in series with two resistors in parallel, R2 of 6 ohms and R3 of 3 ohms, and an ammeter in the bottom wire.",
                "Figure 3. A resistor in series with a parallel pair."),
            EX("Worked example 4: series and parallel together", intro=(
                "In Figure 3 the cell has a p.d. of 12 V. Find the total resistance, the ammeter reading, the p.d. across the parallel pair and the current in each of the pair."),
               steps=[
                   S("First combine the parallel pair", math=r"R_{23} = \dfrac{6 \times 3}{6 + 3} = \dfrac{18}{9} = 2\ \Omega"),
                   S("Add the series resistor", math=r"R = 4 + 2 = 6\ \Omega"),
                   S("Ammeter reading", math=r"I = \dfrac{12}{6} = 2.0\ \text{A}"),
                   S("p.d. across the pair", math=r"V_{23} = I R_{23} = 2.0 \times 2 = 4.0\ \text{V}"),
                   S("Current in R2 and R3", math=r"I_2 = \dfrac{4.0}{6} = 0.67\ \text{A} \qquad I_3 = \dfrac{4.0}{3} = 1.33\ \text{A}"),
               ], check=r"0.67 + 1.33 = 2.0\ \text{A, and } 12 - 4.0 = 8.0\ \text{V is across R1 }(2.0 \times 4 = 8.0)"),
            T("**Why are house lamps in parallel?** Each lamp gets the full supply p.d. so it shines at its normal brightness, and each lamp can be switched on or off without affecting the others. "
              "In series, one broken lamp would break the whole circuit, and the p.d. would be shared between the lamps so they would be dim."),
            MISTAKE("Adding resistances in parallel", "Do not add parallel resistors. The total is **less** than the smallest one. If your answer for two parallel resistors is bigger than either, you have added them."),
            MISTAKE("Forgetting to invert", r"With $\dfrac{1}{R} = \dfrac{1}{6} + \dfrac{1}{3} = \dfrac{1}{2}$, the answer for $R$ is $2\ \Omega$, not $\dfrac{1}{2}$. Always turn the fraction upside down at the end."),
            QUIZ("Two resistors of 6 ohms and 12 ohms are connected in parallel. The total resistance is", ["18 ohms", "9 ohms", "4 ohms", "2 ohms"], 2,
                 "1/R = 1/6 + 1/12 = 2/12 + 1/12 = 3/12 = 1/4, so R = 4 ohms (less than the smallest).",
                 hint="Use 1/R = 1/R1 + 1/R2 then invert.",
                 feedback=["That is the series answer.", "That is the average, which is not how parallel resistors combine.", "", "You inverted 1/6 + 1/12 wrongly, or guessed. Check: 1/6 + 1/12 = 1/4."]),
            QUIZ("A 3 ohm and a 6 ohm resistor are in series with a 9 V supply. What is the p.d. across the 3 ohm resistor?", ["1.0 V", "3.0 V", "6.0 V", "9.0 V"], 1,
                 "R = 9 ohms, I = 9/9 = 1.0 A, so V across 3 ohms = 1.0 x 3 = 3.0 V.",
                 hint="Find the current first.",
                 feedback=["That is the current in amperes, not a p.d.", "", "That is the p.d. across the 6 ohm resistor.", "That is the whole supply p.d., shared between the two."]),
            TIP("Where this appears: series and parallel circuits are in Paper 1 and Paper 2 every year, often with a drawn circuit. The Board's examiners report that many candidates did not know that the p.d.s across series components "
                "add up to the battery p.d. Always say which rule you use, and write units."),
            PQ("Three resistors of 2 ohms, 3 ohms and 5 ohms are connected in series to a 20 V supply. Find the total resistance and the current.",
               r"$R = 2 + 3 + 5 = 10\ \Omega$. $I = V/R = 20/10 = 2.0$ A."),
            PQ("Two resistors of 12 ohms are connected in parallel. Find the total resistance.",
               r"$1/R = 1/12 + 1/12 = 2/12 = 1/6$, so $R = 6\ \Omega$."),
            PQ("A 6 ohm resistor and a 3 ohm resistor are in parallel across a 12 V battery. Find the current in the main wire.",
               r"$R = (6 \times 3)/(6 + 3) = 2\ \Omega$, so $I = 12/2 = 6.0$ A. (Check: 12/6 + 12/3 = 2.0 + 4.0 = 6.0 A.)"),
            PQ("Give two advantages of connecting the lamps in a house in parallel.",
               "Each lamp has the full p.d. of the supply, so it works at normal brightness. Each lamp can be switched off or can fail without affecting the others."),
            SUM("Resistance rises with length, falls with cross-sectional area, and depends on material and temperature.",
                r"Series: same current; p.d.s add to the supply p.d.; $R = R_1 + R_2 + \dots$.",
                r"Parallel: same p.d. across each branch; currents add; $1/R = 1/R_1 + 1/R_2 + \dots$, giving a total smaller than the smallest.",
                "In a mixed circuit, combine the parallel part first, then add the series resistors."),
        ],
    ),
    # ------------------------------------------------------------------ 16. EMF and internal resistance
    lesson(
        module=ELEC,
        topic="Resistance and circuits",
        title="EMF, internal resistance and terminal p.d.",
        slug="phc-internal-resistance",
        minutes=24,
        summary=r"Every cell has some resistance of its own. Use $E = V + Ir = I(R + r)$ to explain why a battery's terminal p.d. falls when it supplies current, and to find $E$ and $r$.",
        objectives=[
            "Explain internal resistance and lost volts",
            "Use E = I(R + r) and V = E - Ir",
            "Explain why a voltmeter across a cell reads less than the EMF when current flows",
            "Find E and r from two sets of readings or from a graph of V against I",
        ],
        key_concepts=["EMF", "Internal resistance", "Terminal p.d.", "Lost volts", "Short circuit"],
        blocks=[
            H("Introduction"),
            T("A torch battery that is almost flat can still show about 1.5 V on a voltmeter, but it will hardly light a bulb. "
              "A car's headlights dim for a moment when the starter motor is switched on. Both happen because a real battery **resists** the current going through it."),
            T("The resistance of the materials inside a cell is called its **internal resistance** $r$. We picture a real cell as a perfect source of EMF $E$ with a small resistor $r$ in series inside it."),
            H("The model of a real cell"),
            IMG("f5ph-c-circuit-internal.svg",
                "A circuit with a cell of EMF E and internal resistance r drawn inside a dashed box, connected to an external resistor R. A voltmeter is across R and an ammeter is in the main wire.",
                "Figure 1. The dashed box is the cell: an EMF E in series with its internal resistance r."),
            D("The **EMF** $E$ is the total energy given per coulomb by the cell. Some of it is wasted as heat in the internal resistance $r$. "
              "The rest is available to the external circuit. The p.d. across the cell's terminals (and across the external resistor $R$) is called the **terminal p.d.** $V$.",
              title="EMF and terminal p.d."),
            KEY("The equations", "Learn all three forms.",
                cards=[["Energy shared", r"$E = V + Ir$ (EMF = terminal p.d. + lost volts)"],
                       ["Whole circuit", r"$E = I(R + r)$ so $I = \dfrac{E}{R + r}$"],
                       ["Terminal p.d.", r"$V = E - Ir = IR$"]]),
            T("The quantity $Ir$ is called the **lost volts**. It is the energy per coulomb wasted inside the cell. "
              "When **no current** flows (an open circuit), $I = 0$, so the lost volts are zero and a voltmeter across the cell reads the full **EMF**. "
              "When current flows, the terminal p.d. is **less** than the EMF, and the bigger the current, the bigger the drop."),
            H("Worked examples"),
            EX("Worked example 1: a cell in a circuit", intro=(
                "A cell has an EMF of 1.5 V and an internal resistance of 0.50 $\\Omega$. It is connected to a 2.5 $\\Omega$ resistor. Find (a) the current, (b) the terminal p.d., (c) the lost volts."),
               steps=[
                   S("(a) Current", math=r"I = \dfrac{E}{R + r} = \dfrac{1.5}{2.5 + 0.50} = \dfrac{1.5}{3.0} = 0.50\ \text{A}"),
                   S("(b) Terminal p.d.", math=r"V = IR = 0.50 \times 2.5 = 1.25\ \text{V}"),
                   S("(c) Lost volts", math=r"Ir = 0.50 \times 0.50 = 0.25\ \text{V}"),
               ], check=r"1.25 + 0.25 = 1.50\ \text{V} = E"),
            EX("Worked example 2: finding E and r", intro=(
                r"A cell is connected to a resistor of 2.0 $\Omega$ and the current is 1.0 A. With a 5.0 $\Omega$ resistor, the current is 0.50 A. Find the EMF and the internal resistance of the cell."),
               steps=[
                   S("Write E = I(R + r) for each case", math=r"E = 1.0\,(2.0 + r) \qquad E = 0.50\,(5.0 + r)"),
                   S("Set them equal", math=r"2.0 + r = 2.5 + 0.50\,r"),
                   S("Solve for r", math=r"0.50\,r = 0.50 \Rightarrow r = 1.0\ \Omega"),
                   S("Find E", math=r"E = 1.0 \times (2.0 + 1.0) = 3.0\ \text{V}"),
               ], check=r"0.50 \times (5.0 + 1.0) = 3.0\ \text{V}"),
            H("Graph of terminal p.d. against current"),
            T("Rearranging $V = E - Ir$ gives $V = -r \\times I + E$, which is a straight line. If you vary the current with a rheostat (variable resistor) and measure $V$ and $I$, the graph of $V$ against $I$ "
              "has an **intercept on the V-axis equal to $E$** and a **gradient equal to $-r$**."),
            GRAPH([-1, 3], alt="Straight line starting at 3 volts on the vertical axis and falling to 0 volts at 3 amperes", caption="Figure 2. A cell with E = 3.0 V and r = 1.0 ohm: V = 3.0 - 1.0 I.",
                  xmin=0, xmax=3.5, ymin=0, ymax=3.5, label="V = 3 − I"),
            T("From Figure 2: the V-axis intercept is 3.0 V, so $E = 3.0$ V. The line falls by 3.0 V over 3.0 A, so the gradient is $-1.0$ V per A, so $r = 1.0\\ \\Omega$. "
              "When $V = 0$ the current is $E/r = 3.0$ A. This is the **short-circuit current**, which is what flows if the terminals are joined by a wire of negligible resistance."),
            EX("Worked example 3: short circuit", intro=(
                "A cell with EMF 1.5 V and internal resistance 0.50 $\\Omega$ is short-circuited with a thick copper wire. Find the largest current it can supply."),
               steps=[
                   S("The external resistance is about zero", math=r"I = \dfrac{E}{R + r} = \dfrac{1.5}{0 + 0.50}"),
                   S("Answer", math=r"I = 3.0\ \text{A}"),
               ]),
            T("Why does a car battery need a very small internal resistance? The starter motor takes a very large current (hundreds of amperes). With a large $r$, the lost volts $Ir$ would be so big that almost no p.d. would be left for the motor. "
              "This is also why a worn-out cell, whose $r$ has grown large, cannot light a lamp although its EMF is still about 1.5 V."),
            MISTAKE("Thinking the voltmeter always reads the EMF", "A voltmeter across the cell reads the EMF **only if no current flows**. When a current flows, it reads the smaller terminal p.d., $V = E - Ir$."),
            MISTAKE("Forgetting r in the total resistance", r"When finding the current, use the **total** resistance $R + r$, not just $R$. Then the terminal p.d. is $IR$, not $E$."),
            QUIZ("A cell of EMF 6.0 V and internal resistance 1.0 ohm is connected to an 11 ohm resistor. The current is", ["0.50 A", "0.55 A", "0.60 A", "6.0 A"], 0,
                 "I = E / (R + r) = 6.0 / (11 + 1.0) = 0.50 A.",
                 hint="Add the internal resistance to the external resistance.",
                 feedback=["", "You used 6.0 / 11. You forgot the internal resistance.", "You used E divided by R minus r, or made an arithmetic slip. The total resistance is 12 ohms.", "That would be the current for zero total resistance."]),
            QUIZ("A battery drives a larger and larger current. Its terminal p.d.", ["rises", "stays the same", "falls", "becomes equal to the EMF"], 2,
                 "V = E - Ir. As I increases, the lost volts Ir increase, so the terminal p.d. falls.",
                 hint="Use V = E - Ir.",
                 feedback=["The lost volts grow with the current, so V cannot rise.", "It stays the same only if r = 0.", "", "V equals E only when the current is zero."]),
            TIP("Where this appears: EMF and internal resistance appear in Paper 2 (calculation, a graph, an explanation of why the terminal voltage drops) and in Paper 1. "
                "The Board's examiners report that many candidates could not define EMF as the work done per unit charge in converting other energy into electrical energy in the source. Learn that sentence."),
            PQ("A battery has an EMF of 12 V and an internal resistance of 0.50 ohm. It supplies a current of 4.0 A. Find the terminal p.d.",
               r"Lost volts $= Ir = 4.0 \times 0.50 = 2.0$ V. $V = E - Ir = 12 - 2.0 = 10$ V."),
            PQ("A cell of EMF 9.0 V is connected to a 4.0 ohm resistor. The current is 2.0 A. Calculate the internal resistance of the cell.",
               r"$E = I(R + r)$ so $9.0 = 2.0\,(4.0 + r)$, so $4.5 = 4.0 + r$ and $r = 0.50\ \Omega$."),
            PQ("A voltmeter reads 1.50 V across a cell in an open circuit and 1.30 V when the cell supplies a current of 0.50 A. Find the internal resistance.",
               r"$E = 1.50$ V. Lost volts $= 1.50 - 1.30 = 0.20$ V. $r = 0.20/0.50 = 0.40\ \Omega$."),
            PQ("Explain why the lights in a car dim when the starter motor is switched on.",
               "The motor draws a very large current. The lost volts Ir inside the battery become large, so the terminal p.d. across the lights falls and they dim."),
            SUM(r"A real cell has an EMF $E$ and an internal resistance $r$, so $E = I(R + r)$.",
                r"Terminal p.d. $V = E - Ir$; the lost volts $Ir$ get bigger as the current gets bigger.",
                "A voltmeter across a cell reads the EMF only when no current flows.",
                r"A graph of $V$ against $I$ is a straight line with intercept $E$ and gradient $-r$. The short-circuit current is $E/r$."),
        ],
    ),
    # ------------------------------------------------------------------ 17. Electrical energy, power and the kilowatt-hour
    lesson(
        module=ELEC,
        topic="Electrical energy and power",
        title="Electrical energy, power and the kilowatt-hour",
        slug="phc-energy-power-kwh",
        minutes=25,
        summary=r"Power is energy per second: $P = IV = I^2R = V^2/R$. Electricity is sold in kilowatt-hours (kWh). Work out the energy an appliance uses and what it costs, using a stated tariff.",
        objectives=[
            "Use E = VIt and P = VI, I^2R and V^2/R",
            "Convert between joules and kilowatt-hours",
            "Calculate the energy used and the cost of running appliances",
            "Compare appliances and suggest ways to reduce an electricity bill",
        ],
        key_concepts=["Electrical energy", "Power", "Watt", "Kilowatt-hour", "Tariff", "Heating effect of a current"],
        blocks=[
            H("Introduction"),
            T("At the end of the month a prepaid meter or a bill tells you how many **units** of electricity you used. A unit is one **kilowatt-hour (kWh)**. "
              "An iron, a fan, a television and four lamps all use electricity at different rates. To control the bill you need to know how much energy each one uses."),
            T("**Tariff note:** the prices in this lesson are **assumed practice values**, mainly 80 FCFA per kWh. Real tariffs depend on the supplier and the customer category and change over time, "
              "so for a real bill always use the rate printed on your own bill or meter."),
            H("Electrical energy and power"),
            D("The **electrical energy** $E$ changed in a component is the charge that passes multiplied by the p.d.: $E = QV$. Since $Q = It$, this gives",
              title="Electrical energy", formula=r"E = VIt",
              note="E in joules (J), V in volts (V), I in amperes (A), t in seconds (s)."),
            D("**Power** is the rate at which energy is changed. Its unit is the **watt (W)**: 1 W is 1 joule per second. 1 kilowatt (kW) = 1000 W.",
              title="Power", formula=r"P = \dfrac{E}{t} = VI"),
            T("Using Ohm's law $V = IR$ in the power equation gives two more forms:"),
            F(r"P = VI \qquad P = I^{2}R \qquad P = \dfrac{V^{2}}{R}"),
            KEY("Which form should I use?", "Pick the one that uses the numbers you were given.",
                cards=[["P = VI", "When you know the p.d. and the current."],
                       ["P = I²R", "When you know the current and the resistance."],
                       ["P = V²/R", "When you know the p.d. and the resistance."]]),
            T("The **heating effect** of a current: when charges flow through a resistor, electrical energy is changed to heat, at the rate $I^2R$. "
              "This is how an electric kettle, an iron and a cooker work. A thin wire has high resistance and gets hot; a thick copper cable has low resistance and stays cool."),
            H("The kilowatt-hour"),
            D("The **kilowatt-hour (kWh)** is the energy used by a 1 kW appliance running for 1 hour. It is the unit of energy used on electricity bills.",
              title="Kilowatt-hour", formula=r"\text{energy (kWh)} = \text{power (kW)} \times \text{time (h)}",
              note=r"1 kWh = 1000 W x 3600 s = $3.6 \times 10^{6}$ J."),
            F(r"\text{cost} = \text{number of kWh} \times \text{cost per kWh}"),
            H("Worked examples"),
            EX("Worked example 1: a kettle", intro=(
                "An electric kettle is rated 2000 W, 220 V. Find the current it takes and the resistance of its heating element."),
               steps=[
                   S("Current from P = VI", math=r"I = \dfrac{P}{V} = \dfrac{2000}{220} = 9.1\ \text{A}"),
                   S("Resistance from P = V²/R", math=r"R = \dfrac{V^{2}}{P} = \dfrac{220^{2}}{2000} = 24.2\ \Omega"),
                   S("Check with P = I²R", math=r"I^{2}R = 9.09^{2} \times 24.2 = 2000\ \text{W}"),
               ]),
            EX("Worked example 2: energy in joules and kWh", intro=(
                "The same kettle (2000 W) runs for 3.0 minutes. Find the energy used in joules and in kWh, and the cost at 80 FCFA per kWh."),
               steps=[
                   S("Time in seconds", math=r"t = 3.0 \times 60 = 180\ \text{s}"),
                   S("Energy in joules", math=r"E = Pt = 2000 \times 180 = 360\,000\ \text{J}"),
                   S("Energy in kWh", math=r"E = 2.0\ \text{kW} \times \dfrac{3.0}{60}\ \text{h} = 0.10\ \text{kWh}"),
                   S("Cost", math=r"0.10 \times 80 = 8.0\ \text{FCFA}"),
               ], check=r"360\,000 \div 3\,600\,000 = 0.10\ \text{kWh}"),
            EX("Worked example 3: a monthly bill", intro=(
                "A household uses these appliances every day for 30 days: 4 lamps of 15 W for 6 h, a TV of 100 W for 4 h, an iron of 1000 W for half an hour and a fan of 50 W for 8 h. "
                "Find the energy used in the month and the cost at an assumed 80 FCFA per kWh."),
               steps=[
                   S("Lamps", math=r"4 \times 15 = 60\ \text{W} = 0.060\ \text{kW}: \ 0.060 \times 6 = 0.36\ \text{kWh}"),
                   S("Television", math=r"0.100 \times 4 = 0.40\ \text{kWh}"),
                   S("Iron", math=r"1.000 \times 0.5 = 0.50\ \text{kWh}"),
                   S("Fan", math=r"0.050 \times 8 = 0.40\ \text{kWh}"),
                   S("Energy in one day", math=r"0.36 + 0.40 + 0.50 + 0.40 = 1.66\ \text{kWh}"),
                   S("Energy in 30 days", math=r"1.66 \times 30 = 49.8\ \text{kWh}"),
                   S("Cost", math=r"49.8 \times 80 = 3984\ \text{FCFA}"),
               ]),
            EX("Worked example 4: saving money with a better lamp", intro=(
                "A 60 W filament lamp and a 9 W LED lamp give about the same light. Each is on for 5 hours a day for 30 days. Compare their monthly costs at an assumed 80 FCFA per kWh."),
               steps=[
                   S("Filament lamp energy", math=r"0.060 \times 5 \times 30 = 9.0\ \text{kWh}"),
                   S("LED energy", math=r"0.009 \times 5 \times 30 = 1.35\ \text{kWh}"),
                   S("Costs", math=r"9.0 \times 80 = 720\ \text{FCFA} \qquad 1.35 \times 80 = 108\ \text{FCFA}"),
                   S("Answer", text="The LED saves 720 - 108 = 612 FCFA a month for one lamp."),
               ]),
            T("A mobile phone battery stores about 15 Wh (0.015 kWh). A full charge costs only about 1 FCFA at 80 FCFA per kWh, so charging a phone is cheap. "
              "Heating appliances such as irons, kettles and cookers use the most energy."),
            TIP("To reduce a bill: switch off lamps and fans when nobody is in the room, use LED lamps, do not leave a TV on standby, and limit the time of heating appliances."),
            MISTAKE("Mixing units of time", "For joules, time must be in **seconds**. For kWh, power must be in **kilowatts** and time in **hours**. Change 2000 W to 2.0 kW and 30 minutes to 0.5 h before multiplying."),
            MISTAKE("Calling the kWh a unit of power", "The kilowatt-hour is a unit of **energy** (power x time). The kilowatt is the unit of power."),
            QUIZ("A 100 W lamp is switched on for 10 hours. How much energy does it use?", ["0.1 kWh", "1.0 kWh", "10 kWh", "1000 kWh"], 1,
                 "E = 0.100 kW x 10 h = 1.0 kWh.",
                 hint="Change 100 W to kilowatts first.",
                 feedback=["You forgot to multiply by 10 hours.", "", "You used 1 kW for 10 h. 100 W is only 0.1 kW.", "You multiplied watts by hours and forgot to convert to kilowatts."]),
            QUIZ("An appliance has a resistance of 5.0 ohms and a current of 2.0 A flows through it. Its power is", ["10 W", "20 W", "2.5 W", "0.40 W"], 1,
                 "P = I squared x R = 2.0 squared x 5.0 = 4.0 x 5.0 = 20 W.",
                 hint="Use P = I²R. Square the current first.",
                 feedback=["You used P = IR, forgetting to square the current.", "", "You divided 5.0 by 2.0.", "You divided 2.0 by 5.0."]),
            TIP("Where this appears: electrical energy, power and kWh costs are very common, in Paper 1 and Paper 2. The Board's examiners report that candidates did well on energy and current electricity, "
                "but that many lost marks for missing or wrong units. Always show the unit: W, kW, J, kWh or FCFA."),
            PQ("A heater is rated 2.0 kW and is used for 3 hours. Calculate the energy used in kWh and the cost at 80 FCFA per kWh (assumed tariff).",
               r"Energy $= 2.0 \times 3 = 6.0$ kWh. Cost $= 6.0 \times 80 = 480$ FCFA."),
            PQ("A bulb is marked 60 W, 220 V. Calculate the current through it and its resistance.",
               r"$I = P/V = 60/220 = 0.27$ A. $R = V^2/P = 220^2/60 = 807\ \Omega$ (about 810 ohms)."),
            PQ("Convert 1 kWh to joules, showing your working.",
               r"$1\ \text{kWh} = 1000\ \text{W} \times 3600\ \text{s} = 3.6 \times 10^{6}$ J."),
            PQ("An electric iron has a 1000 W element and is used for 2 hours each week. Find the energy used in 4 weeks and the cost at 80 FCFA per kWh (assumed tariff).",
               r"Energy per week $= 1.0 \times 2 = 2.0$ kWh. In 4 weeks: 8.0 kWh. Cost $= 8.0 \times 80 = 640$ FCFA."),
            SUM(r"Electrical energy $E = VIt$ and power $P = VI = I^2R = V^2/R$, in joules and watts.",
                r"1 kWh = 1 kW for 1 hour = $3.6 \times 10^{6}$ J. Energy (kWh) = power (kW) x time (h).",
                "Cost = number of kWh x cost per kWh. The tariff in this lesson (80 FCFA per kWh) is an assumed value for practice.",
                "Always convert W to kW and minutes to hours for kWh, and quote units."),
        ],
    ),
]
