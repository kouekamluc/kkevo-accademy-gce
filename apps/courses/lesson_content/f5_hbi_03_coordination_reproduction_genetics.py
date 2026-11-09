"""Form 5 Human Biology (0565), module 5: Coordination, Reproduction & Human Genetics.

10 lessons, one practice set each. Figures are KKEVO's own schematic drawings (static/lessons/diagrams/f5hbi3-*.svg).
Genetics crosses (monohybrid, sex determination, sickle-cell, haemophilia) were checked by script.
Family planning and reproduction are taught factually; choices are personal and advice comes from a health worker.
"""

from .dsl import *  # noqa: F403

COURSE = ("human-biology", "form-5")

MODULE = "Coordination, Reproduction & Human Genetics"
NS = "The nervous system"
RA = "The reflex arc"
EYE = "The eye"
EAR = "The ear"
ENDO = "Endocrine glands and hormones"
RS = "The reproductive systems"
MC_ = "The menstrual cycle and fertilization"
ANC = "Antenatal care and family planning"
MEN = "Mendelian genetics"
SEX = "Sex determination and genetic disorders"

LESSONS = []

# ------------------------------------------------------------------ 1. The nervous system
LESSONS.append(lesson(
    module=MODULE, topic=NS,
    title="The nervous system: brain, spinal cord, nerves and neurones",
    slug="hbi3-nervous-system",
    minutes=22,
    summary="The nervous system has a central part (brain and spinal cord) and a peripheral part (nerves). Neurones carry electrical impulses; sensory, relay and motor neurones link receptors to effectors, and the main brain parts each have a job.",
    objectives=[
        "Distinguish the central nervous system from the peripheral nervous system",
        "Describe the structure of a motor neurone and the functions of sensory, relay and motor neurones",
        "State the functions of the cerebrum, cerebellum and medulla oblongata",
        "Describe how an impulse crosses a synapse and how the brain and cord are protected",
    ],
    key_concepts=["Central nervous system", "Peripheral nervous system", "Neurone", "Impulse", "Synapse", "Cerebrum", "Cerebellum", "Medulla oblongata"],
    blocks=[
        H("Introduction"),
        T("A footballer in Bafoussam sees the ball coming, decides to kick it, swings the leg and keeps his balance, all in a "
          "fraction of a second. At the same time his heart beats and he breathes without thinking about it. The system that makes "
          "this possible is the **nervous system**."),
        T("This lesson shows how the nervous system is organised, how a single nerve cell works, and what the main parts of the brain do."),
        H("Two parts of one system"),
        D("The **central nervous system (CNS)** is the brain and the spinal cord. It receives information, makes decisions and sends out instructions.",
          title="Central nervous system"),
        D("The **peripheral nervous system (PNS)** is all the nerves that run between the CNS and the rest of the body. Humans have 12 pairs of "
          "cranial nerves (joined to the brain) and 31 pairs of spinal nerves (joined to the spinal cord).", title="Peripheral nervous system"),
        T("A **nerve** is a bundle of many long nerve fibres wrapped together, like the wires inside an electric cable. "
          "A **receptor** is a cell or organ that detects a **stimulus** (a change such as light, sound, heat or touch). "
          "An **effector** is a muscle or a gland that carries out a **response**."),
        H("The neurone"),
        D("A **neurone** (nerve cell) is a cell specialised to carry electrical signals called **impulses**.", title="Neurone"),
        IMG("f5hbi3-neurone.svg",
            alt="A motor neurone drawn from left to right: dendrites and a cell body with a nucleus on the left, a long axon covered with myelin sheath sections separated by small gaps called nodes of Ranvier, and axon endings touching a muscle fibre on the right.",
            caption="Figure 1. A motor neurone (schematic). The impulse travels from the cell body along the axon to the muscle."),
        KEY("Parts of a motor neurone", "Learn each part with its job.", cards=[
            ["Cell body", "Contains the nucleus and most of the cytoplasm. It keeps the cell alive."],
            ["Dendrites", "Short branches that receive impulses from other neurones."],
            ["Axon", "A very long fibre that carries impulses away from the cell body. In a leg it can be about a metre long."],
            ["Myelin sheath", "A fatty insulating layer around the axon. It speeds up the impulse. The tiny gaps between sheath sections are the nodes of Ranvier."],
            ["Axon endings", "Branches at the end of the axon that pass the signal to a muscle, a gland or the next neurone."],
        ]),
        T("There are three kinds of neurone. They differ in shape and in the job they do."),
        KEY("Three types of neurone", "Think of a message travelling in one direction.", cards=[
            ["Sensory neurone", "Carries impulses from a receptor (for example in the skin or eye) towards the CNS."],
            ["Relay (intermediate) neurone", "Lies inside the CNS. It connects sensory neurones to motor neurones."],
            ["Motor neurone", "Carries impulses from the CNS to an effector (a muscle or a gland)."],
        ]),
        H("The synapse"),
        D("A **synapse** is the tiny gap between the end of one neurone and the next neurone (or an effector).", title="Synapse"),
        T("An impulse cannot jump across the gap as electricity. The axon ending releases a chemical called a **neurotransmitter**. "
          "It spreads across the gap, joins the next cell and starts a new impulse there. Because the chemical is released only from one side, "
          "impulses travel in **one direction only**."),
        H("The brain"),
        KEY("Main parts of the brain", "The brain is protected by the skull and has three main regions for this lesson.", cards=[
            ["Cerebrum", "The largest part, with two halves. It controls thinking, memory, learning, speech, voluntary movement, and it receives sensations from the senses."],
            ["Cerebellum", "Lies at the back, below the cerebrum. It controls balance, posture and the smooth coordination of movement."],
            ["Medulla oblongata", "Joins the brain to the spinal cord. It controls involuntary actions such as breathing rate and heart rate."],
        ]),
        T("**Voluntary actions** are under your control and are started by the cerebrum, such as kicking a ball or writing. "
          "**Involuntary actions** happen without you deciding, such as the beating of the heart and digestion."),
        T("The brain and cord are protected in three ways. The brain sits inside the **skull**, and the cord runs inside the **vertebral column** (backbone). "
          "Both are covered by three thin membranes called the **meninges**. Between the membranes is **cerebrospinal fluid**, which acts as a cushion against shocks."),
        TIP("**Exam link.** Paper 1 (multiple choice) asks which part of the brain controls balance or breathing, or what a sensory neurone does. "
            "Paper 2 Section A can ask you to describe the structure of a neurone or to compare the three types. The Board's 2023 report lists co-ordination among the "
            "Paper 2 areas, so know this topic well."),
        EX("Worked example 1: following one message", intro="Describe how a message travels when you decide to kick a ball. (A model answer.)", steps=[
            S("Decision", text="The cerebrum decides to kick. This is a voluntary action."),
            S("Down the cord", text="Impulses travel from the brain down the spinal cord."),
            S("Motor neurone", text="A motor neurone carries the impulses from the cord to the muscles of the leg (the effector)."),
            S("Response and balance", text="The muscles contract and the leg swings. The cerebellum coordinates the movement and keeps balance."),
        ]),
        EX("Worked example 2: naming the type of neurone", intro="A hot spoon touches the skin of a finger. Name the neurone that carries the first impulse and the neurone that finally acts on the muscle.", steps=[
            S("Start at the receptor", text="Heat receptors in the skin detect the stimulus. The first neurone carries the impulse from the receptor to the spinal cord, so it is a sensory neurone."),
            S("Inside the cord", text="A relay neurone connects the sensory neurone to the next cell."),
            S("To the effector", text="A motor neurone carries the impulse from the cord to the muscle of the arm. It is the last neurone."),
        ]),
        MISTAKE("Saying the brain is the whole nervous system", "The brain is only one part of the CNS. The spinal cord is the other. The nerves that run out to the body belong to the peripheral system."),
        MISTAKE("Confusing sensory and motor", "Sensory neurones carry impulses IN to the CNS. Motor neurones carry impulses OUT to the effector. Remember: Motor makes the Movement."),
        QUIZ("Which part of the brain controls balance and the coordination of movement?", ["Cerebrum", "Cerebellum", "Medulla oblongata", "Spinal cord"], 1,
             "The cerebellum coordinates movement and balance.",
             hint="It lies at the back of the brain, below the cerebrum.",
             feedback=["The cerebrum controls thinking, memory and voluntary actions.", "", "The medulla controls breathing and heart rate.", "The spinal cord is not part of the brain. It carries impulses to and from the brain."]),
        QUIZ("Which neurone carries impulses from the CNS to a muscle?", ["Sensory neurone", "Relay neurone", "Motor neurone", "Receptor"], 2,
             "A motor neurone carries impulses away from the CNS to an effector such as a muscle.",
             hint="Which neurone makes the muscle move?",
             feedback=["A sensory neurone carries impulses towards the CNS.", "A relay neurone stays inside the CNS.", "", "A receptor detects a stimulus. It is not a neurone."]),
        PQ("Name the two parts of the central nervous system.", "The brain and the spinal cord."),
        PQ("State two functions of the myelin sheath, or explain why it is useful.", "It is a fatty insulating layer around the axon. It speeds up the impulse, and it insulates the axon so that impulses do not leak into neighbouring fibres."),
        PQ("Explain why impulses cross a synapse in one direction only.", "The neurotransmitter is released only from the axon ending of the first neurone. It spreads across the gap and starts a new impulse in the next cell. The next cell cannot release it back, so the signal goes one way."),
        PQ("State the function of the cerebrum, the cerebellum and the medulla oblongata.", "Cerebrum: thinking, memory and voluntary actions. Cerebellum: balance and coordination of movement. Medulla oblongata: involuntary actions such as breathing and heart rate."),
        SUM("The CNS is the brain and spinal cord. The PNS is the nerves running between the CNS and the body.",
            "A neurone has a cell body, dendrites, an axon (with a myelin sheath) and axon endings.",
            "Sensory neurones carry impulses to the CNS, relay neurones link inside the CNS, motor neurones carry impulses to effectors.",
            "At a synapse a neurotransmitter crosses the gap, so impulses travel one way.",
            "Cerebrum: thinking and voluntary action. Cerebellum: balance. Medulla: breathing and heart rate. Skull, backbone, meninges and fluid protect the CNS."),
    ],
))


# ------------------------------------------------------------------ 2. The reflex arc
LESSONS.append(lesson(
    module=MODULE, topic=RA,
    title="The reflex arc and reflex actions",
    slug="hbi3-reflex-arc",
    minutes=20,
    summary="A reflex action is a fast, automatic, protective response. It follows a reflex arc: stimulus, receptor, sensory neurone, relay neurone in the spinal cord, motor neurone, effector, response.",
    objectives=[
        "Define a reflex action and a reflex arc",
        "Name the parts of a spinal reflex arc in order",
        "Compare reflex actions with voluntary actions",
        "Give examples of reflexes and explain why they protect the body",
    ],
    key_concepts=["Reflex action", "Reflex arc", "Receptor", "Effector", "Spinal cord", "Voluntary action"],
    blocks=[
        H("Introduction"),
        T("A girl cooking on a wood fire in Ngaoundere touches the hot handle of a pot. Her hand is pulled away before she even feels the pain. "
          "If she had to think first, her skin would be burnt. This fast, automatic protection is called a **reflex action**."),
        H("Definitions"),
        D("A **reflex action** is a quick, automatic response to a stimulus. It does not need a decision from the brain, and it protects the body.",
          title="Reflex action"),
        D("A **reflex arc** is the pathway of neurones along which the impulse travels in a reflex action, from the receptor to the effector.",
          title="Reflex arc"),
        T("Examples of reflexes: pulling your hand away from something hot or sharp, the knee-jerk when the tendon below the knee is tapped, "
          "blinking when something comes near the eye, the pupil getting smaller in bright light, coughing and sneezing."),
        H("The parts of a spinal reflex arc"),
        IMG("f5hbi3-reflex-arc.svg",
            alt="A section of the spinal cord. A sensory neurone (blue) runs from a receptor in the skin to the cord, where it passes the impulse to a short relay neurone (orange) in the grey matter. A motor neurone (green) leaves the cord and ends in a muscle, the effector.",
            caption="Figure 1. A reflex arc through the spinal cord (schematic)."),
        KEY("The path of the impulse", "Learn the order. Each step names what is involved.", cards=[
            ["1. Stimulus", "A change in the environment, for example heat on a finger."],
            ["2. Receptor", "Cells in the skin detect the stimulus and start an impulse."],
            ["3. Sensory neurone", "Carries the impulse to the spinal cord. It enters the cord by the dorsal (back) root."],
            ["4. Relay neurone", "In the grey matter of the cord, it passes the impulse to a motor neurone."],
            ["5. Motor neurone", "Carries the impulse out of the cord by the ventral (front) root."],
            ["6. Effector", "A muscle (or a gland) that carries out the response."],
            ["7. Response", "The muscle contracts and the hand is pulled away."],
        ]),
        T("The impulse goes through only a few neurones and does not have to travel to the brain and back. That is why a spinal reflex is so fast. "
          "Other impulses from the relay neurone also go up to the brain, so you feel the pain a moment later."),
        T("Inside the spinal cord, the **grey matter** (the middle, butterfly-shaped part) contains cell bodies and synapses. The **white matter** around it contains the "
          "long nerve fibres that carry impulses up and down the cord."),
        H("Reflex or voluntary?"),
        CODE("Reflex action                    Voluntary action\n"
             "Automatic, no decision           Decided by the brain (cerebrum)\n"
             "Very fast                        Slower\n"
             "Same response every time         Response can change\n"
             "Protects the body                Any purpose: writing, walking\n"
             "Does not need learning           Often learned and practised",
             "text", title="Comparison"),
        D("A **conditioned reflex** is a learned reflex. A hungry person's mouth waters when they smell food cooking. The response became linked to the smell through experience.",
          title="Conditioned reflex"),
        TIP("**Exam link.** Paper 1 often asks you to put the parts of a reflex arc in order or to name the effector. Paper 2 Section A can ask you to define a "
            "reflex action and describe a reflex arc with a labelled diagram. Draw the arc with arrows showing the direction of the impulse."),
        EX("Worked example 1: the hot pot", intro="Describe the pathway when a person touches a hot pot and pulls the hand away. (A model answer.)", steps=[
            S("Stimulus and receptor", text="Heat is the stimulus. Heat receptors in the skin of the finger detect it and start an impulse."),
            S("Sensory neurone", text="The impulse travels along a sensory neurone to the spinal cord."),
            S("Relay neurone", text="In the grey matter of the cord, a relay neurone passes the impulse to a motor neurone."),
            S("Motor neurone and effector", text="The motor neurone carries the impulse to the arm muscle (the effector)."),
            S("Response", text="The muscle contracts and pulls the hand away. The brain is told afterwards, so the pain is felt a little later."),
        ]),
        EX("Worked example 2: pupil reflex", intro="Explain why the pupil gets smaller when you walk from a dark room into bright sunshine, and say why this is a reflex.", steps=[
            S("Stimulus and receptor", text="Bright light is the stimulus. Light-sensitive cells in the retina detect it."),
            S("Pathway", text="Impulses pass along sensory neurones to the brain, then along motor neurones to the muscles of the iris."),
            S("Response", text="The circular muscles of the iris contract and the pupil gets smaller. Less light enters the eye."),
            S("Why it is a reflex", text="It is automatic, fast and protective: it protects the retina from damage by too much light."),
        ]),
        MISTAKE("Saying the brain decides in a reflex", "In a spinal reflex the relay neurone in the cord passes the impulse straight to the motor neurone. The brain is informed later. Do not write that the brain sends the instruction."),
        MISTAKE("Writing 'receptor' for the muscle", "The receptor detects the stimulus (skin, eye). The effector produces the response (a muscle or a gland). They are at opposite ends of the arc."),
        QUIZ("Which is the correct order of the parts of a reflex arc?",
             ["Receptor, motor neurone, relay neurone, sensory neurone, effector", "Receptor, sensory neurone, relay neurone, motor neurone, effector",
              "Effector, sensory neurone, relay neurone, motor neurone, receptor", "Receptor, relay neurone, sensory neurone, effector, motor neurone"], 1,
             "The impulse goes from the receptor along the sensory neurone to the relay neurone, then along the motor neurone to the effector.",
             hint="Start with the part that detects the stimulus and end with the part that responds.",
             feedback=["The motor neurone cannot come before the sensory neurone.", "", "This is the reverse order.", "The sensory neurone must come before the relay neurone and the motor neurone before the effector."]),
        QUIZ("Why are reflex actions important?", ["They let us think carefully", "They protect the body quickly from danger", "They make muscles bigger", "They are decided by the cerebrum"], 1,
             "Reflex actions are fast and automatic, so they protect the body before there is time to think.",
             hint="Think of pulling your hand from a hot object.",
             feedback=["Reflexes happen without thinking.", "", "Reflexes do not build muscle.", "Reflexes do not need the cerebrum to decide."]),
        PQ("Define a reflex action.", "A reflex action is a quick, automatic response to a stimulus that does not need a decision by the brain and that protects the body."),
        PQ("Name the structures through which an impulse passes in a reflex arc, in order, from the receptor.", "Receptor, sensory neurone, relay neurone (in the spinal cord), motor neurone, effector."),
        PQ("Give two differences between a reflex action and a voluntary action.", "A reflex is automatic, voluntary needs a decision; a reflex is faster; a reflex gives the same response each time; a reflex protects the body (any two)."),
        PQ("Give two examples of reflex actions in humans.", "Pulling the hand from a hot object, blinking, the pupil getting smaller in bright light, the knee jerk, coughing, sneezing (any two)."),
        SUM("A reflex action is a fast, automatic, protective response. The pathway is the reflex arc.",
            "Order: stimulus, receptor, sensory neurone, relay neurone, motor neurone, effector, response.",
            "The sensory neurone enters the cord by the dorsal root. The motor neurone leaves by the ventral root.",
            "A spinal reflex does not wait for a brain decision, so it is fast; the brain is told afterwards.",
            "Reflex: automatic, fast, same each time. Voluntary: decided by the brain, can change."),
    ],
))


# ------------------------------------------------------------------ 3. The eye
LESSONS.append(lesson(
    module=MODULE, topic=EYE,
    title="The eye: structure, focusing and defects of sight",
    slug="hbi3-the-eye",
    minutes=24,
    summary="The eye focuses light on the retina using the cornea and lens. The iris controls the pupil, the ciliary muscles change the shape of the lens, and defects such as short sight and long sight are corrected with lenses.",
    objectives=[
        "Name the parts of the eye and state the function of each",
        "Explain how the pupil responds to bright and dim light",
        "Explain accommodation: how the eye focuses on near and distant objects",
        "Describe short sight, long sight and cataract and how they are corrected or treated",
    ],
    key_concepts=["Cornea", "Lens", "Iris", "Pupil", "Retina", "Accommodation", "Rods and cones", "Short sight", "Long sight"],
    blocks=[
        H("Introduction"),
        T("A student at the back of a classroom in Garoua cannot read the blackboard, although he reads his textbook easily. A teacher advises him to "
          "see an eye nurse. To understand why, we must see how the eye forms a clear picture."),
        H("Parts of the eye"),
        IMG("f5hbi3-eye.svg",
            alt="Section of the eye: cornea, aqueous humour, iris and pupil, lens held by suspensory ligaments to the ciliary muscle, vitreous humour behind, and the retina at the back with the fovea and the blind spot where the optic nerve leaves.",
            caption="Figure 1. The human eye in section (schematic)."),
        KEY("Parts and functions", "Learn the structure and the job of each part.", cards=[
            ["Sclera", "Tough white outer coat. It protects the eye and keeps its shape."],
            ["Cornea", "Clear front window. It does most of the bending (refraction) of light."],
            ["Iris and pupil", "The iris is a coloured ring of muscle. The pupil is the hole in its centre that lets light in."],
            ["Lens", "A clear, flexible, curved structure. It fine-focuses light on the retina."],
            ["Ciliary muscle and suspensory ligaments", "The ciliary muscle is a ring of muscle round the lens. The ligaments connect it to the lens and change its shape."],
            ["Aqueous and vitreous humour", "Clear fluids. Aqueous humour fills the front chamber; vitreous humour is a jelly that fills the large chamber and keeps the eyeball round."],
            ["Retina", "The inner layer at the back, with light-sensitive cells (rods and cones). It forms the image."],
            ["Fovea and blind spot", "The fovea is the part of the retina with the sharpest vision. The blind spot is where the optic nerve leaves; it has no light-sensitive cells."],
            ["Optic nerve", "Carries impulses from the retina to the brain, which interprets the image."],
        ]),
        T("Light from an object is bent by the cornea and the lens and brought to a point on the retina. The image on the retina is **upside down**, "
          "and the brain turns it the right way up. Rods and cones change light into impulses."),
        KEY("Rods and cones", "The two kinds of light-sensitive cell.", cards=[
            ["Rods", "Work in dim light. They give black-and-white vision. Most of them are away from the fovea."],
            ["Cones", "Work in bright light. They detect colour and fine detail. They are concentrated at the fovea."],
        ]),
        H("The pupil reflex"),
        T("The iris controls how much light enters. This is a reflex action (see the lesson on the reflex arc)."),
        CODE("Bright light  : circular muscles of the iris contract,\n"
             "               radial muscles relax  -> pupil gets smaller\n"
             "Dim light     : radial muscles contract,\n"
             "               circular muscles relax -> pupil gets bigger",
             "text", title="Iris and the pupil"),
        H("Accommodation: focusing near and far"),
        D("**Accommodation** is the change in the shape of the lens so that light from objects at different distances is focused on the retina.",
          title="Accommodation"),
        CODE("Looking at a NEAR object (reading):\n"
             "  ciliary muscles contract -> suspensory ligaments slacken\n"
             "  -> lens becomes thicker (more curved) -> light bent more\n\n"
             "Looking at a DISTANT object:\n"
             "  ciliary muscles relax -> suspensory ligaments pulled tight\n"
             "  -> lens becomes thinner (less curved) -> light bent less",
             "text", title="How the lens changes"),
        TIP("**Exam link.** Paper 1 often asks what happens to the ciliary muscle or lens when looking at a near object. Paper 2 Section A (co-ordination) can ask you to name and "
            "label the parts of the eye, explain accommodation and the pupil reflex, or describe an eye defect and its correction. A frequent slip is reversing "
            "contract and relax, so learn: near object, ciliary muscle contracts, lens fat."),
        H("Defects of sight"),
        KEY("Short sight and long sight", "Both are focusing defects and are corrected with spectacle lenses.", cards=[
            ["Short sight (myopia)", "Near objects are clear, distant objects are blurred. The eyeball is too long, or the lens is too strong, so light focuses in front of the retina. Corrected with a concave (diverging) lens."],
            ["Long sight (hypermetropia)", "Distant objects are clear, near objects are blurred. The eyeball is too short, or the lens too weak, so light would focus behind the retina. Corrected with a convex (converging) lens."],
            ["Cataract", "The lens becomes cloudy, so vision is misty. It is treated by an operation that replaces the lens."],
        ]),
        T("Eating foods rich in vitamin A, such as carrots, red palm oil, mangoes and green leafy vegetables, helps to protect the eyes. "
          "Lack of vitamin A can cause night blindness. Other care: do not rub the eyes with dirty hands, wear protection when working with dust or chemicals, "
          "do not read in very poor light, and have the eyes tested if sight becomes blurred. Colour blindness is an inherited condition (see the genetics lessons)."),
        EX("Worked example 1: reading a book", intro="Explain how the eye changes when a student looks up from the blackboard to read a book. (A model answer.)", steps=[
            S("Change of object", text="The object is now near. Light from it spreads out more, so the lens must bend it more."),
            S("Ciliary muscle", text="The ciliary muscles contract. This releases the tension, so the suspensory ligaments slacken."),
            S("Lens", text="The lens, which is elastic, becomes thicker and more curved."),
            S("Result", text="Light is bent more and the image of the page is focused on the retina."),
        ]),
        EX("Worked example 2: choosing the lens", intro="A girl sees her textbook clearly but cannot read the road signs. Name her defect, its cause and the lens used to correct it. (A model answer.)", steps=[
            S("Identify", text="Near objects are clear and distant objects are blurred, so she is short sighted (myopic)."),
            S("Cause", text="The eyeball is too long (or the lens too strong), so distant light is focused in front of the retina."),
            S("Correction", text="A concave (diverging) lens spreads the light a little before it enters the eye, so the image falls on the retina."),
        ]),
        MISTAKE("Mixing up contract and relax", "For NEAR objects the ciliary muscles CONTRACT and the lens gets FATTER. For DISTANT objects they RELAX and the lens gets THINNER."),
        MISTAKE("Naming the lens as the part that does all the focusing", "The cornea does most of the bending of light. The lens only fine-tunes the focus by changing shape."),
        QUIZ("A person looks at a distant tree. What happens in the eye?", ["Ciliary muscles contract and the lens becomes thicker", "Ciliary muscles relax and the lens becomes thinner", "Ciliary muscles relax and the lens becomes thicker", "The pupil moves forward"], 1,
             "For distant objects the ciliary muscles relax, the ligaments are pulled tight and the lens becomes thinner.",
             hint="Distant objects need the lens to bend light less.",
             feedback=["That is what happens for a near object.", "", "A relaxed ciliary muscle gives a thinner lens, not a thicker one.", "The pupil is a hole in the iris. It does not move."]),
        QUIZ("Which defect is corrected with a concave lens?", ["Cataract", "Long sight", "Short sight", "Night blindness"], 2,
             "A concave lens corrects short sight because it spreads the light before it enters the eye.",
             hint="Think of the person who cannot see distant objects clearly.",
             feedback=["Cataract is treated by an operation.", "Long sight is corrected by a convex lens.", "", "Night blindness is linked to a lack of vitamin A."]),
        PQ("State the functions of the cornea, the iris and the retina.", "Cornea: lets light in and bends it. Iris: controls the size of the pupil and so the amount of light entering. Retina: contains the light-sensitive cells that detect light and send impulses to the brain."),
        PQ("Explain why the pupil gets smaller in bright light.", "The circular muscles of the iris contract (and the radial muscles relax). A smaller pupil lets in less light, which protects the retina from damage."),
        PQ("State two differences between rods and cones.", "Rods work in dim light and give black-and-white vision; cones work in bright light and detect colour and fine detail. Cones are concentrated at the fovea."),
        PQ("Explain what causes long sight and how it is corrected.", "The eyeball is too short or the lens too weak, so light from near objects would focus behind the retina and near objects look blurred. A convex lens bends the light inwards before it enters the eye and brings the image to the retina."),
        SUM("Cornea and lens bend light to form an upside-down image on the retina; the brain interprets it.",
            "The iris controls the pupil: bright light, smaller pupil; dim light, larger pupil.",
            "Near object: ciliary muscles contract, ligaments slacken, thicker lens. Distant object: the reverse.",
            "Rods work in dim light; cones give colour vision and are dense at the fovea. The blind spot has no receptors.",
            "Short sight (concave lens), long sight (convex lens), cataract (cloudy lens, operation)."),
    ],
))


# ------------------------------------------------------------------ 4. The ear
LESSONS.append(lesson(
    module=MODULE, topic=EAR,
    title="The ear: hearing, balance and care of the ear",
    slug="hbi3-the-ear",
    minutes=22,
    summary="The ear has an outer, middle and inner part. Sound makes the eardrum vibrate, the ossicles pass the vibrations to the cochlea, and impulses go to the brain. The semicircular canals detect head movement and help balance.",
    objectives=[
        "Name the parts of the outer, middle and inner ear and state their functions",
        "Describe how sound is detected, step by step, from the pinna to the brain",
        "Explain the role of the semicircular canals and the Eustachian tube",
        "Describe common causes of deafness and how to care for the ears",
    ],
    key_concepts=["Pinna", "Eardrum", "Ossicles", "Cochlea", "Semicircular canals", "Eustachian tube", "Auditory nerve", "Balance"],
    blocks=[
        H("Introduction"),
        T("A drummer at a village festival near Bamenda hears the beat, tells whether it comes from the left or right, and stays upright while he dances. "
          "The ears do two jobs: they detect **sound** and they help the body keep its **balance**."),
        T("The Board's report on the 2023 Human Biology paper said that the ear was not well taught, so this topic is worth studying carefully."),
        H("Three parts of the ear"),
        IMG("f5hbi3-ear.svg",
            alt="Section of the ear: pinna and ear canal lead to the eardrum; three ossicles in the middle ear reach the oval window; a Eustachian tube leads down; the semicircular canals, coiled cochlea and auditory nerve are on the right.",
            caption="Figure 1. The human ear (schematic)."),
        KEY("Outer ear", "Collects sound and sends it inwards.", cards=[
            ["Pinna", "The flap of cartilage and skin on the side of the head. It collects sound waves."],
            ["Ear canal", "A short tube that carries sound to the eardrum. Its wall makes ear wax, which traps dust and germs."],
            ["Eardrum", "A thin membrane at the end of the canal. It vibrates when sound waves hit it."],
        ]),
        KEY("Middle ear", "An air-filled space.", cards=[
            ["Ossicles", "Three tiny bones: the malleus (hammer), the incus (anvil) and the stapes (stirrup). They pass the vibrations across the middle ear and make them stronger."],
            ["Oval window", "A small membrane in the wall of the inner ear. The stapes pushes on it."],
            ["Eustachian tube", "Joins the middle ear to the throat. It lets air in or out, so the air pressure is the same on both sides of the eardrum."],
        ]),
        KEY("Inner ear", "Fluid-filled spaces in the bone of the skull.", cards=[
            ["Cochlea", "A coiled tube shaped like a snail shell. It contains sensory hair cells that detect vibrations in the fluid and start impulses."],
            ["Semicircular canals", "Three fluid-filled loops, at right angles to each other. They detect movement and rotation of the head and help balance."],
            ["Auditory nerve", "Carries impulses from the cochlea (and from the balance organs) to the brain."],
        ]),
        H("How we hear"),
        CODE("1. Sound waves are collected by the pinna and pass down the ear canal.\n"
             "2. The sound waves make the eardrum vibrate.\n"
             "3. The three ossicles carry (and strengthen) the vibrations.\n"
             "4. The stapes pushes on the oval window.\n"
             "5. The fluid in the cochlea moves and the hair cells are stimulated.\n"
             "6. Impulses pass along the auditory nerve to the brain, which\n"
             "   interprets them as sound.",
             "text", title="From sound to sensation"),
        T("The brain compares the sounds that reach the two ears. This is how you can tell where a sound comes from."),
        H("Balance"),
        T("When the head moves, the fluid in the semicircular canals moves too. Sensory cells detect this and send impulses to the brain. "
          "The cerebellum uses this information, together with information from the eyes and muscles, to keep the body balanced. "
          "Rotating quickly and then stopping can make you dizzy because the fluid keeps moving for a moment."),
        TIP("**Exam link.** Paper 1 asks for the function of a part (for example the Eustachian tube or the semicircular canals) or the order of events in hearing. Paper 2 Section A can ask "
            "you to draw and label the ear and to describe how sound is heard. Always write the steps in order, from the pinna to the brain."),
        H("Deafness and care of the ears"),
        KEY("Causes of hearing loss", "Two broad kinds.", cards=[
            ["Conduction problems", "Sound is not passed on well: a blockage with ear wax, fluid or infection in the middle ear, or damaged ossicles or eardrum."],
            ["Nerve damage", "The hair cells or the auditory nerve are damaged, for example by very loud noise over a long time, some infections or ageing."],
        ]),
        T("**Care of the ears:** do not push sticks, pins or cotton buds into the ear canal, because they can push wax further in or damage the eardrum. "
          "Keep the volume of headphones low and avoid long exposure to very loud music or machinery. "
          "Treat ear infections early, because untreated infections can harm hearing. See a health worker if there is pain, discharge or loss of hearing. "
          "Do not blow the nose too hard during a cold."),
        EX("Worked example 1: the path of sound", intro="Describe how a sound from a radio reaches the brain. (A model answer.)", steps=[
            S("Outer ear", text="Sound waves are collected by the pinna and travel down the ear canal to the eardrum, which vibrates."),
            S("Middle ear", text="The vibrations are passed across the ossicles (malleus, incus, stapes), which strengthen them. The stapes pushes on the oval window."),
            S("Inner ear", text="The movement makes the fluid in the cochlea move. This stimulates the hair cells, which start impulses."),
            S("To the brain", text="The impulses travel along the auditory nerve to the brain, which interprets them as sound."),
        ]),
        EX("Worked example 2: pressure on a hill", intro="Why do your ears 'pop' when a bus climbs quickly up a mountain road such as the one to Mount Cameroon? (A model answer.)", steps=[
            S("Air pressure changes", text="Outside air pressure falls as the bus climbs. The air in the middle ear is at the old, higher pressure."),
            S("The eardrum bulges", text="The higher pressure inside pushes the eardrum outwards, which feels uncomfortable."),
            S("The Eustachian tube", text="Swallowing opens the Eustachian tube. Air flows between the middle ear and the throat, so the pressure becomes equal and the eardrum returns to normal. This is the 'pop'."),
        ]),
        MISTAKE("Mixing up the ossicles and the cochlea", "The ossicles are three bones in the MIDDLE ear. The cochlea is the coiled organ of hearing in the INNER ear. The semicircular canals are for balance, not hearing."),
        MISTAKE("Missing the middle steps", "Do not write that the eardrum sends sound to the brain. The eardrum vibrates, the ossicles carry the vibrations, the cochlea starts impulses, and the nerve carries them."),
        QUIZ("Which structure changes vibrations into nerve impulses?", ["Eardrum", "Ossicles", "Hair cells in the cochlea", "Eustachian tube"], 2,
             "The sensory hair cells in the cochlea are the receptors: they change the movement of fluid into impulses.",
             hint="Which part of the ear contains the sensory cells?",
             feedback=["The eardrum only vibrates.", "The ossicles pass on and strengthen vibrations.", "", "The Eustachian tube equalises air pressure."]),
        QUIZ("What is the function of the semicircular canals?", ["To collect sound", "To detect movement of the head and help balance", "To make ear wax", "To join the ear to the throat"], 1,
             "The semicircular canals are balance organs: fluid in them moves when the head moves.",
             hint="Think of what happens when you spin and become dizzy.",
             feedback=["The pinna collects sound.", "", "Ear wax is made in the ear canal.", "The Eustachian tube joins the ear to the throat."]),
        PQ("Name the three ossicles in the middle ear.", "The malleus (hammer), the incus (anvil) and the stapes (stirrup)."),
        PQ("State the function of the Eustachian tube.", "It connects the middle ear to the throat and lets air pass, so that the air pressure on the two sides of the eardrum stays equal."),
        PQ("Describe what happens in the cochlea when the stapes pushes on the oval window.", "The movement makes the fluid in the cochlea move. This stimulates the sensory hair cells, which start impulses that travel along the auditory nerve to the brain."),
        PQ("Give two ways of protecting your hearing.", "Avoid loud noise or keep headphone volume low; do not put objects into the ear canal; treat ear infections early; see a health worker for ear pain or hearing loss (any two)."),
        SUM("Outer ear: pinna, ear canal, eardrum. Middle ear: three ossicles, oval window, Eustachian tube. Inner ear: cochlea, semicircular canals, auditory nerve.",
            "Sound path: pinna, canal, eardrum, ossicles, oval window, cochlear fluid, hair cells, auditory nerve, brain.",
            "The semicircular canals detect movement of the head and help balance.",
            "The Eustachian tube equalises air pressure on the two sides of the eardrum.",
            "Care: avoid loud noise, do not push objects into the ear, treat infections early."),
    ],
))


# ------------------------------------------------------------------ 5. Endocrine glands and hormones
LESSONS.append(lesson(
    module=MODULE, topic=ENDO,
    title="Endocrine glands and hormones",
    slug="hbi3-endocrine-hormones",
    minutes=22,
    summary="Endocrine glands make hormones, chemical messengers carried by the blood to target organs. The pituitary, thyroid, adrenal glands, pancreas, ovaries and testes each produce hormones with set effects, and hormones act more slowly than nerves.",
    objectives=[
        "Define an endocrine gland and a hormone",
        "Compare nervous and hormonal control",
        "State the main hormone of each major gland and its effect",
        "Explain how insulin and glucagon control blood sugar and what happens in diabetes",
    ],
    key_concepts=["Endocrine gland", "Hormone", "Target organ", "Pituitary gland", "Thyroxine", "Adrenaline", "Insulin", "Glucagon", "Diabetes"],
    blocks=[
        H("Introduction"),
        T("When a motorbike taxi swerves close to you on a road in Douala, your heart pounds and your hands shake. Nerves started the quick reaction, "
          "but the pounding heart is kept going by a chemical in the blood: **adrenaline**. The body has two control systems, the nervous system and the "
          "**hormonal (endocrine) system**."),
        H("Definitions"),
        D("An **endocrine gland** is a gland that has no duct. It releases its product straight into the blood.", title="Endocrine gland"),
        D("A **hormone** is a chemical messenger made by an endocrine gland. It is carried by the blood and changes the activity of its **target organ**.",
          title="Hormone"),
        T("Hormones travel everywhere in the blood but only affect the organs that have the right receptors, the target organs. "
          "Glands with ducts, such as salivary glands, are **exocrine glands**: they send their juice along a tube to a particular place."),
        H("Nervous and hormonal control compared"),
        CODE("Nervous system                  Hormonal system\n"
             "Electrical impulses (and         Chemical hormones in the blood\n"
             "neurotransmitters)\n"
             "Travels along nerves             Travels in the blood\n"
             "Very fast                        Slower\n"
             "Short-lived effect               Often longer-lasting effect\n"
             "Acts on a precise muscle or      Can act on many organs\n"
             "gland",
             "text", title="Comparison"),
        H("The main endocrine glands"),
        KEY("Glands, hormones and effects", "Learn one hormone and one effect for each gland.", cards=[
            ["Pituitary gland (under the brain)", "Called the master gland because its hormones control other glands. Makes growth hormone, FSH and LH (control the ovaries and testes) and ADH (water balance in the kidney)."],
            ["Thyroid gland (neck)", "Makes thyroxine, which controls the rate of metabolism. It needs iodine. Lack of iodine causes goitre, a swollen neck."],
            ["Adrenal glands (above the kidneys)", "Make adrenaline, the 'fight or flight' hormone: faster heart rate and breathing, more glucose in the blood, wider pupils, blood sent to the muscles."],
            ["Pancreas", "Makes insulin and glucagon, which control blood glucose. (It also makes digestive juice, so it is both an endocrine and an exocrine gland.)"],
            ["Ovaries (in females)", "Make oestrogen and progesterone, which control the female sex characteristics and the menstrual cycle."],
            ["Testes (in males)", "Make testosterone, which controls the male sex characteristics and sperm production."],
        ]),
        T("At **puberty** (about the ages of 10 to 16) the pituitary gland sends hormones to the ovaries or testes. The sex hormones cause the "
          "changes of adolescence: in girls, breast development, wider hips and the start of the periods; in boys, a deeper voice, facial hair and broader shoulders. "
          "In both, hair appears under the arms and in the pubic region, and the reproductive organs mature."),
        H("Controlling blood glucose"),
        T("The cells need a steady level of glucose in the blood. The pancreas detects the level and releases the right hormone. "
          "This is an example of **negative feedback**: a change is detected and the body acts to reverse it."),
        CODE("After a meal, blood glucose rises:\n"
             "   pancreas releases INSULIN\n"
             "   -> liver and muscles change glucose to glycogen and store it\n"
             "   -> cells take up glucose -> blood glucose falls\n\n"
             "Between meals or in exercise, blood glucose falls:\n"
             "   pancreas releases GLUCAGON\n"
             "   -> liver changes glycogen back to glucose\n"
             "   -> blood glucose rises",
             "text", title="Insulin and glucagon"),
        D("**Diabetes mellitus** is a disease in which the body does not make enough insulin, or the cells do not respond to it. Blood glucose stays too high. "
          "Signs include great thirst, frequent urination, tiredness and weight loss. It is managed with diet, exercise, tablets or insulin injections, under a health worker's advice.",
          title="Diabetes"),
        TIP("**Exam link.** Paper 1 asks you to match a gland to its hormone or a hormone to its effect (for example insulin to lowering blood glucose, adrenaline to fight or flight). "
            "Paper 2 Section A can ask you to define a hormone, compare nerves and hormones, or discuss blood sugar control. Use the word 'glycogen' for the stored form of glucose."),
        EX("Worked example 1: nerves or hormones?", intro="State three differences between control by the nervous system and by hormones. (A model answer.)", steps=[
            S("Medium", text="Nerves carry electrical impulses along neurones. Hormones are chemicals carried in the blood."),
            S("Speed", text="Nervous responses are very fast. Hormonal responses are slower."),
            S("Duration", text="Nervous effects are short-lived. Hormonal effects usually last longer."),
        ]),
        EX("Worked example 2: a student after a race", intro="A student eats a large plate of rice and a sweet drink. Explain how the body keeps blood glucose steady. (A model answer.)", steps=[
            S("Glucose rises", text="Glucose from the food is absorbed and the blood glucose level rises."),
            S("Insulin", text="The pancreas detects this and releases insulin into the blood."),
            S("Effect", text="Insulin makes the liver and muscles store glucose as glycogen, and the cells take up more glucose."),
            S("Result", text="Blood glucose falls back to normal. This is negative feedback."),
        ]),
        MISTAKE("Mixing up insulin and glucagon", "Insulin LOWERS blood glucose (stores it as glycogen). Glucagon RAISES blood glucose (turns glycogen back to glucose)."),
        MISTAKE("Calling the pancreas only a digestive gland", "The pancreas has both roles: it releases digestive juice along a duct (exocrine) and insulin and glucagon into the blood (endocrine)."),
        QUIZ("Which hormone prepares the body for 'fight or flight'?", ["Insulin", "Thyroxine", "Adrenaline", "Oestrogen"], 2,
             "Adrenaline, from the adrenal glands, raises the heart rate and blood glucose and sends blood to the muscles.",
             hint="This gland sits above the kidney.",
             feedback=["Insulin lowers blood glucose.", "Thyroxine controls the rate of metabolism.", "", "Oestrogen is a female sex hormone."]),
        QUIZ("What does insulin do?", ["Raises blood glucose", "Lowers blood glucose by helping it to be stored as glycogen", "Controls the heart rate", "Makes the body grow"], 1,
             "Insulin lowers blood glucose. The liver and muscles store the excess as glycogen.",
             hint="After a meal, blood glucose rises. Which hormone brings it back?",
             feedback=["That is glucagon.", "", "That is adrenaline.", "Growth hormone from the pituitary does that."]),
        PQ("Define a hormone.", "A hormone is a chemical messenger made by an endocrine gland and carried by the blood to a target organ, where it changes the activity of the organ."),
        PQ("State the gland that makes each of these hormones: insulin, thyroxine, testosterone.", "Insulin: pancreas. Thyroxine: thyroid gland. Testosterone: testes."),
        PQ("Explain why a lack of iodine in the diet can cause a swollen neck (goitre).", "The thyroid gland needs iodine to make thyroxine. Without iodine the gland cannot make enough thyroxine and it enlarges, causing a swollen neck."),
        PQ("Describe how the body responds when blood glucose falls too low.", "The pancreas releases glucagon. It makes the liver change glycogen back to glucose, which enters the blood, so blood glucose rises again."),
        SUM("Endocrine glands have no ducts. They release hormones into the blood, which act on target organs.",
            "Nervous control is fast and short-lived; hormonal control is slower and lasts longer.",
            "Pituitary (master gland), thyroid (thyroxine), adrenals (adrenaline), pancreas (insulin, glucagon), ovaries and testes (sex hormones).",
            "Insulin lowers blood glucose; glucagon raises it. This is negative feedback.",
            "In diabetes the blood glucose stays too high; health workers advise on treatment."),
    ],
))


# ------------------------------------------------------------------ 6. The reproductive systems
LESSONS.append(lesson(
    module=MODULE, topic=RS,
    title="The male and female reproductive systems",
    slug="hbi3-reproductive-systems",
    minutes=24,
    summary="The male system makes sperm in the testes and delivers them in semen through the sperm duct and urethra. The female system makes egg cells in the ovaries, carries them in the oviducts and nourishes the embryo in the uterus.",
    objectives=[
        "Name the parts of the male reproductive system and state their functions",
        "Name the parts of the female reproductive system and state their functions",
        "Describe how a sperm cell and an egg cell are adapted to their jobs",
        "Compare sperm and egg cells",
    ],
    key_concepts=["Testis", "Sperm duct", "Prostate gland", "Ovary", "Oviduct", "Uterus", "Gamete", "Sperm cell", "Egg cell"],
    blocks=[
        H("Introduction"),
        T("Reproduction is how living things make new individuals of their own kind. In humans a new life starts when two special cells, "
          "one from each parent, join. This lesson names the organs that make and carry these cells. It is taught here as science, "
          "in the way a health worker or biology teacher explains it."),
        D("A **gamete** is a sex cell. The male gamete is the **sperm cell** and the female gamete is the **egg cell (ovum)**. Each has half the number of chromosomes of an ordinary body cell.",
          title="Gamete"),
        H("The male reproductive system"),
        IMG("f5hbi3-male.svg",
            alt="Front view of the male reproductive system. Two testes lie in the scrotum, each with an epididymis on top. A sperm duct runs from each testis up and round to join the urethra near the prostate gland, below the bladder. Seminal vesicles join the ducts. The urethra runs through the penis.",
            caption="Figure 1. The male reproductive system (schematic)."),
        KEY("Parts and functions", "Follow the path of the sperm from the testis outwards.", cards=[
            ["Testes (one is a testis)", "Make sperm cells and the hormone testosterone."],
            ["Scrotum", "The skin bag that holds the testes outside the body, where it is a little cooler than the body, the best temperature for making sperm."],
            ["Epididymis", "A coiled tube on each testis. Sperm are stored here while they mature."],
            ["Sperm duct", "Carries sperm from the epididymis towards the urethra."],
            ["Seminal vesicles and prostate gland", "Make the fluids that mix with the sperm to form semen. The fluid gives the sperm food and helps them swim."],
            ["Urethra", "A tube through the penis that carries semen out of the body. It also carries urine from the bladder (but not at the same time)."],
            ["Penis", "The organ that places semen inside the female body during sexual intercourse."],
        ]),
        H("The female reproductive system"),
        IMG("f5hbi3-female.svg",
            alt="Front view of the female reproductive system. Two ovaries lie at the sides of a pear-shaped uterus. An oviduct runs from each ovary to the top of the uterus. The inner wall of the uterus is the lining. The narrow cervix at the bottom of the uterus leads to the vagina.",
            caption="Figure 2. The female reproductive system (schematic)."),
        KEY("Parts and functions", "Follow the path of the egg from the ovary.", cards=[
            ["Ovaries", "Two organs that make egg cells and the hormones oestrogen and progesterone. One egg is usually released about once a month."],
            ["Oviducts (Fallopian tubes)", "Tubes that carry the egg towards the uterus. Cilia (tiny hairs) and muscles move it along. Fertilization usually happens here."],
            ["Uterus (womb)", "A muscular bag with a soft lining. An embryo is fixed to the lining and grows here."],
            ["Cervix", "The narrow ring of muscle at the lower end of the uterus. It keeps the uterus closed during pregnancy and opens at birth."],
            ["Vagina", "The muscular tube from the cervix to the outside. It receives sperm and is the birth canal."],
        ]),
        H("The gametes"),
        KEY("Sperm cell", "Adaptations for swimming and entering the egg.", cards=[
            ["Head", "Holds the nucleus with the father's genes. The tip has enzymes (the acrosome) that help the sperm enter the egg."],
            ["Middle piece", "Packed with mitochondria that release energy for swimming."],
            ["Tail", "A whip-like flagellum that moves the sperm. The cell is very small."],
        ]),
        KEY("Egg cell", "Adaptations for storing food and protecting the embryo.", cards=[
            ["Large size", "The biggest cell in the body, with a cytoplasm that contains a store of food (yolk-like material)."],
            ["Nucleus", "Holds the mother's genes (half the normal number of chromosomes)."],
            ["Jelly coat", "A protective layer round the egg. After one sperm enters, the coat changes so that no other sperm can get in."],
        ]),
        CODE("                 Sperm cell               Egg cell\n"
             "Size             very small               large\n"
             "Movement         swims (tail)             cannot move, is carried\n"
             "Food store       none                     yes, in the cytoplasm\n"
             "Numbers          millions made daily      about one released a month\n"
             "Made in          testes                   ovaries\n"
             "Chromosomes      23                       23",
             "text", title="Comparison of the gametes"),
        TIP("**Exam link.** Paper 1 asks for the function of a part (for example, where sperm are made or where fertilization happens). Paper 2 Section A can ask for a labelled "
            "diagram of the male or female system, with the function of each part. Question 5 in the Board's 2023 Paper 2 covered reproduction and genetics and was "
            "the most popular and best answered, so these marks are worth getting."),
        EX("Worked example 1: the path of the sperm", intro="Name, in order, the parts through which a sperm cell passes from where it is made to the outside of the male body. (A model answer.)", steps=[
            S("Made", text="Sperm are made in the testis."),
            S("Stored", text="They pass into the epididymis, where they are stored while they mature."),
            S("Carried", text="They travel along the sperm duct, where the fluids from the seminal vesicles and prostate gland are added to form semen."),
            S("Out", text="Semen passes through the urethra in the penis to the outside."),
        ]),
        EX("Worked example 2: adaptations of the sperm", intro="State three ways in which a sperm cell is adapted to its function. (A model answer.)", steps=[
            S("Tail", text="The tail (flagellum) lets the sperm swim to the egg."),
            S("Mitochondria", text="The middle piece has many mitochondria that release energy for swimming."),
            S("Acrosome", text="The head contains enzymes that digest a way through the jelly coat of the egg."),
        ]),
        MISTAKE("Saying that the testis carries the sperm out", "The testis only MAKES sperm. The sperm duct and the urethra carry them out."),
        MISTAKE("Saying the egg is made in the uterus", "Eggs are made in the ovary. They are fertilised in the oviduct. The uterus is where the embryo grows."),
        QUIZ("Where are sperm cells made?", ["Epididymis", "Prostate gland", "Testis", "Urethra"], 2,
             "Sperm are made in the testes. The epididymis stores them.",
             hint="This organ also makes testosterone.",
             feedback=["The epididymis stores sperm; it does not make them.", "The prostate gland makes part of the seminal fluid.", "", "The urethra is only a tube."]),
        QUIZ("In which part of the female system does the embryo grow?", ["Ovary", "Oviduct", "Cervix", "Uterus"], 3,
             "The embryo is fixed to the soft lining of the uterus and grows there.",
             hint="Another name for it is the womb.",
             feedback=["The ovary makes eggs.", "Fertilization usually happens in the oviduct, but the embryo does not grow there.", "The cervix is the narrow opening of the uterus.", ""]),
        PQ("State the functions of the scrotum and the prostate gland.", "The scrotum holds the testes outside the body at a slightly cooler temperature, which suits sperm production. The prostate gland makes fluid that is added to the sperm to form semen."),
        PQ("State the functions of the ovary and the oviduct.", "The ovary makes egg cells and the hormones oestrogen and progesterone. The oviduct carries the egg towards the uterus and is where fertilization usually happens."),
        PQ("Give three differences between a sperm cell and an egg cell.", "A sperm is much smaller; a sperm has a tail and swims while an egg cannot move; an egg has a food store, a sperm does not; sperm are produced in millions, eggs about one a month (any three)."),
        PQ("Explain why the testes are in the scrotum outside the body.", "Sperm production needs a temperature slightly lower than the temperature inside the body. The scrotum keeps the testes a little cooler."),
        SUM("Gametes are the sperm cell (male) and the egg cell (female); each has half the normal number of chromosomes.",
            "Male: testis (makes sperm), epididymis (stores), sperm duct, glands (add fluid), urethra and penis.",
            "Female: ovary (makes eggs), oviduct (carries egg; fertilization), uterus (embryo grows), cervix, vagina.",
            "A sperm has a tail, mitochondria and an acrosome; an egg is large with a food store and a jelly coat.",
            "Sex hormones are made in the testes (testosterone) and ovaries (oestrogen, progesterone)."),
    ],
))


# ------------------------------------------------------------------ 7. The menstrual cycle and fertilization
LESSONS.append(lesson(
    module=MODULE, topic=MC_,
    title="The menstrual cycle, ovulation and fertilization",
    slug="hbi3-menstrual-cycle-fertilization",
    minutes=24,
    summary="The menstrual cycle (about 28 days) is controlled by FSH, LH, oestrogen and progesterone. An egg is released at ovulation; if a sperm fertilises it in the oviduct, the embryo implants in the thickened uterus lining, otherwise the lining is shed as a period.",
    objectives=[
        "Describe the main events of the menstrual cycle in a 28-day cycle",
        "State the roles of FSH, LH, oestrogen and progesterone",
        "Describe fertilization, early development and implantation",
        "Explain what happens to the uterus lining with and without fertilization, and how twins form",
    ],
    key_concepts=["Menstrual cycle", "Ovulation", "Fertilization", "Zygote", "Implantation", "Oestrogen", "Progesterone", "Menstruation"],
    blocks=[
        H("Introduction"),
        T("From puberty until the menopause (usually around the age of 50), the body of a healthy woman repeats a monthly series of changes that prepares the uterus for a possible pregnancy. "
          "This is the **menstrual cycle**. It is a normal, healthy process, and it is controlled by hormones."),
        D("The **menstrual cycle** is the series of changes in the ovary and uterus that repeats about every 28 days. Cycle length varies from person to person "
          "and can be shorter or longer. Day 1 is the first day of bleeding.", title="Menstrual cycle"),
        D("**Ovulation** is the release of an egg cell from the ovary.", title="Ovulation"),
        H("The cycle day by day"),
        IMG("f5hbi3-menstrual.svg",
            alt="Graph of a 28-day cycle. The uterus lining is thin on days 1 to 5, then builds up and stays thick to about day 26. Oestrogen peaks just before ovulation on day 14. Progesterone rises after day 14, peaks near day 21 and falls.",
            caption="Figure 1. A teaching diagram of a 28-day cycle (schematic, not measured data; real cycles vary)."),
        KEY("Stages of a 28-day cycle", "Learn the days as typical examples.", cards=[
            ["Days 1 to 5: period (menstruation)", "The thick lining of the uterus breaks down and passes out through the vagina with a little blood. Oestrogen and progesterone levels are low."],
            ["Days 6 to 13: lining rebuilds", "FSH from the pituitary gland makes a follicle (a small bag holding an egg) grow in the ovary. The follicle makes oestrogen, which rebuilds the lining of the uterus."],
            ["Day 14: ovulation", "A sudden rise in LH, also from the pituitary, makes the follicle burst and release the egg into the oviduct."],
            ["Days 15 to 28: thick lining", "The empty follicle becomes a body that makes progesterone. Progesterone keeps the lining thick, soft and rich in blood vessels, ready for an embryo."],
            ["If no pregnancy", "Progesterone falls. The lining breaks down and the next period begins."],
        ]),
        T("The four hormones work together. **FSH** (follicle stimulating hormone) grows the follicle. **LH** (luteinising hormone) triggers ovulation. "
          "**Oestrogen** rebuilds the lining. **Progesterone** maintains the lining. If a woman becomes pregnant, progesterone stays high and periods stop during the pregnancy."),
        T("The time from ovulation to the next period is fairly constant, about 14 days. So in a 28-day cycle ovulation is around day 14, "
          "but in a 30-day cycle it is around day 16 (30 minus 14)."),
        H("Fertilization"),
        D("**Fertilization** is the joining of the nucleus of a sperm cell with the nucleus of an egg cell. The result is a **zygote**, with the full number of 46 chromosomes (23 from each parent).",
          title="Fertilization"),
        T("An egg lives only about a day after ovulation. Sperm placed in the female body can survive for a few days. Fertilization happens in the **oviduct**. "
          "Many sperm reach the egg, but only one enters. The jelly coat then changes so that no other sperm can enter."),
        CODE("Fertilization (oviduct): zygote\n"
             "   -> cell divides repeatedly while moving down the oviduct\n"
             "   -> ball of cells (embryo) reaches the uterus after a few days\n"
             "   -> about a week after fertilization it sinks into the thick\n"
             "      lining: this is IMPLANTATION\n"
             "   -> the placenta forms; the embryo becomes a foetus\n"
             "   -> birth after about 40 weeks (nine months) of pregnancy",
             "text", title="From fertilization to pregnancy"),
        T("**Twins**: if two eggs are released and both are fertilised, the twins are **fraternal (non-identical)** and can be different sexes. "
          "If one zygote splits into two embryos early on, the twins are **identical**, have the same genes and are of the same sex."),
        TIP("**Exam link.** Paper 1 may give a diagram of the cycle and ask on what day ovulation occurs, or which hormone keeps the lining thick. Paper 2 Section A can ask you to describe the "
            "menstrual cycle, the role of the hormones, or to explain fertilization and implantation. Quote typical days only as examples and say that cycle length varies."),
        EX("Worked example 1: reading the graph", intro="Using Figure 1 (a 28-day cycle), state when ovulation occurs, which hormone is highest just before it, and which hormone keeps the lining thick after it. (A model answer.)", steps=[
            S("Ovulation", text="The dashed line shows ovulation at about day 14."),
            S("Hormone before ovulation", text="Oestrogen is at its peak just before ovulation."),
            S("Hormone after ovulation", text="Progesterone rises after ovulation and keeps the lining thick until about day 26."),
        ]),
        EX("Worked example 2: dating ovulation", intro="A teaching case (invented for practice): a student's cycle is 30 days long and her last period began on 3 June. About when did ovulation occur? (A model answer.)", steps=[
            S("Rule", text="Ovulation is about 14 days before the next period starts."),
            S("Calculate", math=r"30 - 14 = 16", text="So ovulation is on about day 16 of the cycle."),
            S("Date", text="Day 1 is 3 June, so day 16 is 3 + 15 = 18 June. Real cycles vary, so this is only an estimate."),
        ]),
        MISTAKE("Thinking ovulation is the start of the period", "Ovulation is the release of the egg, around the middle of the cycle. The period is the shedding of the uterus lining at the start of a cycle."),
        MISTAKE("Confusing fertilization and implantation", "Fertilization is the joining of sperm and egg (in the oviduct). Implantation is the embedding of the embryo in the uterus lining about a week later."),
        QUIZ("Which hormone triggers ovulation?", ["Progesterone", "LH", "Oestrogen", "Insulin"], 1,
             "A surge of LH from the pituitary gland makes the follicle release the egg.",
             hint="It is made in the pituitary gland, not in the ovary.",
             feedback=["Progesterone keeps the lining thick after ovulation.", "", "Oestrogen rebuilds the lining.", "Insulin controls blood glucose."]),
        QUIZ("What happens to the lining of the uterus if no fertilization takes place?", ["It stays thick for the next year", "It breaks down and is shed as a period", "It turns into an egg", "It makes more progesterone"], 1,
             "When progesterone falls, the lining breaks down and is shed. This is menstruation.",
             hint="Think of the start of the next cycle.",
             feedback=["It is shed.", "", "Eggs are made in the ovary.", "The progesterone level falls."]),
        PQ("Define ovulation.", "Ovulation is the release of an egg cell from the ovary, at about the middle of the menstrual cycle."),
        PQ("State the roles of FSH and progesterone in the cycle.", "FSH makes a follicle grow in the ovary. Progesterone keeps the lining of the uterus thick and ready for an embryo."),
        PQ("Describe what happens from fertilization to implantation.", "The sperm and egg nuclei join in the oviduct to form a zygote. The zygote divides repeatedly into a ball of cells as it moves to the uterus. About a week after fertilization the embryo sinks into the thick uterus lining (implantation)."),
        PQ("Explain the difference between identical and fraternal twins.", "Identical twins come from one fertilised egg that splits in two; they have the same genes and the same sex. Fraternal twins come from two eggs fertilised by two sperm; they differ genetically and may be of different sexes."),
        SUM("The menstrual cycle is about 28 days; day 1 is the first day of the period. Cycles vary.",
            "FSH grows the follicle; oestrogen rebuilds the lining; LH triggers ovulation; progesterone keeps the lining thick.",
            "Ovulation is about 14 days before the next period.",
            "Fertilization (oviduct) gives a zygote of 46 chromosomes. The embryo implants in the lining about a week later.",
            "No fertilization: progesterone falls and the lining is shed. Twins: identical (one egg splits) or fraternal (two eggs)."),
    ],
))


# ------------------------------------------------------------------ 8. Antenatal care and family planning
LESSONS.append(lesson(
    module=MODULE, topic=ANC,
    title="Pregnancy, antenatal and postnatal care, and family planning",
    slug="hbi3-antenatal-family-planning",
    minutes=24,
    summary="The placenta, umbilical cord and amniotic fluid support the foetus. Antenatal and postnatal care protect mother and baby, and family planning means deciding if and when to have children; such choices are personal and a health worker gives advice.",
    objectives=[
        "Describe the functions of the placenta, umbilical cord and amniotic fluid",
        "Explain why antenatal care matters and list its main parts",
        "Describe postnatal care, including breastfeeding and immunization",
        "Define family planning, state its health benefits and name the main kinds of method",
    ],
    key_concepts=["Placenta", "Umbilical cord", "Amniotic fluid", "Antenatal care", "Postnatal care", "Breastfeeding", "Family planning"],
    blocks=[
        H("Introduction"),
        T("In a health centre in Kumba, a pregnant woman waits for her check-up. A nurse measures her blood pressure and weight, tests her urine and blood, "
          "and gives her tablets. These visits, and the care after birth, save the lives of mothers and babies. This lesson explains how the baby is "
          "supported before birth and how families and health workers care for both."),
        H("How the baby is supported before birth"),
        T("After implantation the embryo grows for about 40 weeks. From about the eighth week it is called a **foetus**."),
        KEY("Support structures", "Learn the job of each one.", cards=[
            ["Placenta", "A disc-shaped organ attached to the uterus wall. Oxygen, glucose, amino acids and other nutrients pass from the mother's blood to the foetus. Carbon dioxide and urea pass from the foetus to the mother. The two blood supplies stay separate; substances cross by diffusion and other transport. The placenta also makes hormones."],
            ["Umbilical cord", "A tube joining the foetus to the placenta. It contains blood vessels that carry blood between them."],
            ["Amniotic sac and amniotic fluid", "A bag of fluid round the foetus. The fluid cushions it against knocks, keeps the temperature steady and allows it to move."],
        ]),
        T("The placenta lets some harmful things through. Alcohol, nicotine from smoking, some drugs, and some germs (for example the viruses that cause HIV infection and rubella) can reach the foetus. "
          "That is why a pregnant woman should only take medicines that a health worker has approved."),
        H("Antenatal care"),
        D("**Antenatal (prenatal) care** is the health care a woman receives during pregnancy, before the birth.", title="Antenatal care"),
        KEY("What antenatal care includes", "A health worker explains the visits to attend; the number of visits is set by national guidelines, so check with the clinic.", cards=[
            ["Check-ups", "Measuring weight and blood pressure, checking the position and growth of the baby, and urine and blood tests (for anaemia, infections and other problems)."],
            ["Protection from disease", "Tetanus vaccination, and malaria prevention such as sleeping under an insecticide-treated net and preventive medicine given at the clinic."],
            ["Supplements", "Iron and folic acid tablets help to prevent anaemia and some birth defects."],
            ["Good diet and rest", "A balanced diet with extra energy and protein, clean safe water, and enough rest."],
            ["Avoiding harm", "No alcohol, smoking or unapproved medicines. Treat illness early."],
            ["Planning the birth", "A plan to give birth with a trained health worker at a health facility, and to know the signs that need urgent help."],
        ]),
        H("Postnatal care"),
        D("**Postnatal care** is the care of the mother and baby after the birth.", title="Postnatal care"),
        T("The mother is checked for bleeding, infection and other problems, and the baby is weighed, examined and kept warm and clean. "
          "The baby's cord stump is kept clean and dry. The baby is registered and starts **immunization** (vaccination) on the national schedule. "
          "Growth is checked at the clinic."),
        T("**Breastfeeding** is recommended by health authorities. The first milk, **colostrum**, is rich in antibodies that protect the baby from infections. "
          "Breast milk is clean, at the right temperature, free, and contains everything a baby needs. Health workers advise **exclusive breastfeeding** (breast milk only) for the first six months, "
          "then adding other foods while breastfeeding continues."),
        H("Family planning"),
        D("**Family planning** means deciding if, when and how many children to have, so that births are spaced and wanted.", title="Family planning"),
        T("Health benefits: spacing births (for example by a few years) lets the mother's body recover and gives each child time and care; it lowers the risk of illness "
          "for both mother and children; and it helps families plan their food, school fees and income. Choices about family planning are **personal**. "
          "A couple decides what suits them, and a trained health worker gives advice and explains the choices."),
        KEY("Main kinds of method", "A health worker explains how each works and which is suitable. No method is right for everybody.", cards=[
            ["Natural methods", "Based on knowing the fertile days of the menstrual cycle, or on breastfeeding patterns. Need good knowledge and are less reliable."],
            ["Barrier methods", "Male and female condoms stop sperm reaching the egg. Condoms also reduce the risk of sexually transmitted infections, which the other methods do not."],
            ["Hormonal methods", "Pills, injections and implants that stop ovulation or make fertilization less likely. They need a health worker's advice."],
            ["Intra-uterine device (IUD)", "A small device placed in the uterus by a trained health worker."],
            ["Permanent methods", "Operations (sterilization) for people who are sure they do not want more children."],
        ]),
        TIP("**Exam link.** Paper 1 asks for the function of the placenta or amniotic fluid, or why colostrum is important. Paper 2 Section A can ask about antenatal care or the benefits of "
            "family planning. Answer factually: list the care given and say who gives it. Write that choices are personal and that a health worker advises."),
        EX("Worked example 1: the placenta", intro="Describe two functions of the placenta. (A model answer.)", steps=[
            S("Supply", text="It passes oxygen and nutrients from the mother's blood to the foetus."),
            S("Removal", text="It passes carbon dioxide and urea from the foetus to the mother's blood to be removed."),
            S("Extra", text="It also makes hormones, and the two blood supplies do not mix."),
        ]),
        EX("Worked example 2: advice for a pregnant woman", intro="State five things a pregnant woman should do to stay healthy and keep her baby healthy. (A model answer.)", steps=[
            S("Care", text="Attend the antenatal clinic for check-ups and tests, and get the tetanus vaccine."),
            S("Protection", text="Sleep under an insecticide-treated net and take the iron, folic acid and malaria prevention that the clinic gives."),
            S("Food", text="Eat a balanced diet and drink clean safe water."),
            S("Avoid", text="Avoid alcohol, smoking and medicines not approved by a health worker."),
            S("Plan", text="Plan to give birth with a trained health worker."),
        ]),
        MISTAKE("Saying the mother's blood and the baby's blood mix", "They do not mix. Substances pass between them across the thin walls in the placenta."),
        MISTAKE("Treating family planning as a duty or a ban", "Family planning means a family's own informed choice about when to have children. A health worker gives advice; nobody should be forced."),
        QUIZ("What is the function of the amniotic fluid?", ["To feed the foetus", "To protect the foetus against knocks", "To carry oxygen", "To make hormones"], 1,
             "The amniotic fluid cushions the foetus and keeps its temperature steady.",
             hint="Think of the fluid as a water cushion.",
             feedback=["Food comes through the placenta and umbilical cord.", "", "Oxygen passes through the placenta.", "The placenta makes hormones."]),
        QUIZ("Why is breast milk, especially colostrum, good for a newborn?", ["It contains antibodies that protect from infection", "It has no water", "It makes the baby sleep", "It replaces vaccines"], 0,
             "Colostrum is rich in antibodies. Breast milk is also clean and has the right nutrients.",
             hint="Think about protection against germs.",
             feedback=["", "Breast milk is mostly water.", "It is not meant to make the baby sleep.", "Breast milk helps but vaccination is still needed."]),
        PQ("State the functions of the umbilical cord.", "It joins the foetus to the placenta and its blood vessels carry blood between them, bringing oxygen and nutrients to the foetus and taking away carbon dioxide and urea."),
        PQ("Give three things that happen during antenatal care.", "Check weight and blood pressure; tests of blood and urine; tetanus vaccination; iron and folic acid; malaria prevention; advice on diet (any three)."),
        PQ("Explain two health benefits of spacing births.", "The mother's body has time to recover, so there is less risk of anaemia and complications; each child receives more care and food; babies are less likely to be born too early or too small (any two)."),
        PQ("Name the kinds of family planning method.", "Natural methods, barrier methods (condoms), hormonal methods, intra-uterine devices and permanent methods. A health worker advises which suits a person."),
        SUM("The placenta passes oxygen and nutrients to the foetus and wastes away; the cord joins them; the amniotic fluid cushions the foetus.",
            "Harmful substances such as alcohol, nicotine and some germs can cross the placenta.",
            "Antenatal care: check-ups, tests, tetanus vaccine, malaria prevention, iron, good food, a planned safe birth.",
            "Postnatal care: checks for mother and baby, immunization, colostrum and breastfeeding.",
            "Family planning is a personal choice about spacing children. A health worker gives advice on methods."),
    ],
))


# ------------------------------------------------------------------ 9. Mendelian genetics
LESSONS.append(lesson(
    module=MODULE, topic=MEN,
    title="Mendelian genetics: genes, alleles and monohybrid crosses",
    slug="hbi3-mendelian-genetics",
    minutes=25,
    summary="Characteristics are controlled by genes that come in forms called alleles. Dominant alleles show in heterozygotes; a monohybrid cross between two heterozygotes gives a 3:1 phenotype ratio, and a test cross with a homozygous recessive gives 1:1 or all dominant.",
    objectives=[
        "Define gene, allele, dominant, recessive, genotype, phenotype, homozygous and heterozygous",
        "Draw a Punnett square for a monohybrid cross and read off the genotypes and phenotypes",
        "State the 3:1 and 1:1 ratios and calculate probabilities",
        "Explain what a test cross shows",
    ],
    key_concepts=["Gene", "Allele", "Dominant", "Recessive", "Genotype", "Phenotype", "Homozygous", "Heterozygous", "Punnett square", "Test cross"],
    blocks=[
        H("Introduction"),
        T("Why does a child have the same dimples as the mother but the height of the father? Characteristics are passed from parents to children by units "
          "called **genes**. The rules of inheritance were first worked out by a monk, Gregor Mendel, who bred garden pea plants in the 1800s and counted their offspring. "
          "We use his ideas today, in plants, animals and people."),
        H("Key terms"),
        D("A **gene** is a section of DNA on a chromosome that controls a characteristic. Different forms of the same gene are called **alleles**. "
          "A body cell has two alleles of each gene, one from each parent.", title="Gene and allele"),
        D("A **dominant** allele shows its effect even when there is only one copy (written as a capital letter, such as T). "
          "A **recessive** allele shows its effect only when there are two copies (a small letter, such as t).", title="Dominant and recessive"),
        D("The **genotype** is the pair of alleles an organism has (for example Tt). The **phenotype** is the characteristic you can see (for example tall).",
          title="Genotype and phenotype"),
        D("**Homozygous** means the two alleles are the same (TT or tt). **Heterozygous** means they are different (Tt).", title="Homozygous and heterozygous"),
        T("**Gametes** have only one allele of each gene, because the pairs separate when gametes are made (meiosis). When a sperm and an egg join, the pair is restored. "
          "The offspring of a cross between two parents are called the **F1** generation (first filial); the offspring of two F1 individuals are the **F2**."),
        H("A monohybrid cross"),
        D("A **monohybrid cross** studies how one pair of contrasting characteristics is inherited, for example tall plants and short plants.", title="Monohybrid cross"),
        T("Rule for setting out a cross: write the parents' phenotypes and genotypes, then their gametes, then use a **Punnett square** to show every possible fertilization."),
        EX("Worked example 1: tall x short (pure breeding)", intro="Tallness (T) is dominant to shortness (t). A homozygous tall pea plant is crossed with a short pea plant. Find the F1.", steps=[
            S("Parents", text="Tall TT x short tt."),
            S("Gametes", text="TT can only make T gametes. tt can only make t gametes."),
            S("Punnett square", text="Every box is Tt."),
            S("Result", text="All of the F1 are Tt, so all are tall (heterozygous). The recessive allele is hidden."),
        ]),
        CODE("               Gametes of tt parent\n"
             "                  t         t\n"
             "Gametes   T      Tt        Tt\n"
             "of TT     T      Tt        Tt\n\n"
             "F1: all Tt = all tall",
             "text", title="Cross 1: TT x tt"),
        EX("Worked example 2: two heterozygotes", intro="Two of the tall F1 plants (Tt) are crossed. Find the genotypes and phenotypes of the F2.", steps=[
            S("Parents", text="Tt x Tt, both tall."),
            S("Gametes", text="Each parent makes T and t gametes in equal numbers."),
            S("Punnett square", text="The four boxes are TT, Tt, Tt, tt."),
            S("Genotype ratio", math=r"1\,TT : 2\,Tt : 1\,tt"),
            S("Phenotype ratio", math=r"\text{3 tall} : \text{1 short}", text="TT and Tt are both tall, so 3 out of 4 are tall (75 percent) and 1 out of 4 is short (25 percent)."),
        ]),
        CODE("               Gametes of Tt parent\n"
             "                  T         t\n"
             "Gametes   T      TT        Tt\n"
             "of Tt     t      Tt        tt\n\n"
             "Genotypes: 1 TT : 2 Tt : 1 tt\n"
             "Phenotypes: 3 tall : 1 short",
             "text", title="Cross 2: Tt x Tt"),
        T("These are **probabilities**, not guarantees. Each child (or seed) has the same chance every time. A family of four children from two Tt parents might have 1, 2, 3 or all 4 tall "
          "children. The 3 to 1 ratio only appears reliably in a large number of offspring."),
        H("The test cross"),
        T("A tall plant could be TT or Tt, because both look tall. To find out, breed it with a short plant (tt). This is a **test cross**."),
        CODE("If the tall plant is TT:  TT x tt -> all Tt (all tall)\n"
             "If the tall plant is Tt:  Tt x tt -> 1 Tt : 1 tt\n"
             "                                  (1 tall : 1 short)",
             "text", title="Test cross results"),
        D("A **test cross** crosses an organism of unknown genotype (showing the dominant phenotype) with a homozygous recessive. If any offspring show the recessive phenotype, the unknown parent was heterozygous.",
          title="Test cross"),
        KEY("Ratios to remember", "Ratios of offspring in monohybrid crosses.", cards=[
            ["TT x tt", "All Tt: all show the dominant characteristic."],
            ["Tt x Tt", "1 TT : 2 Tt : 1 tt; phenotypes 3 dominant : 1 recessive."],
            ["Tt x tt", "1 Tt : 1 tt; phenotypes 1 dominant : 1 recessive."],
            ["TT x Tt", "1 TT : 1 Tt; all show the dominant characteristic."],
        ]),
        TIP("**Exam link.** Paper 1 gives a cross and asks for the genotype of the offspring or the ratio or probability. Paper 2 Section A (Question 5 in the Board's 2023 paper covered reproduction and genetics) "
            "can ask you to complete a Punnett square and explain the results. Always show the parents, the gametes, the square and a clear final statement."),
        MISTAKE("Writing the ratio of genotypes when asked for phenotypes", "Tt x Tt gives the genotype ratio 1:2:1 but the phenotype ratio 3:1, because TT and Tt look the same."),
        MISTAKE("Putting two alleles in one gamete", "Each gamete carries one allele only. Tt gives T gametes and t gametes, not Tt gametes."),
        MISTAKE("Saying a ratio is certain", "3:1 is the expected ratio. Say 'a 1 in 4 chance (25 percent) that each child will be short', not 'exactly one child will be short'."),
        QUIZ("Two heterozygous tall plants (Tt x Tt) are crossed. What fraction of the offspring are expected to be short?", ["Three quarters", "One half", "One quarter", "None"], 2,
             "Only tt is short. One of the four boxes in the square is tt, so one quarter (25 percent).",
             hint="Which genotype is short, and how many boxes show it?",
             feedback=["Three quarters are tall.", "One half is the proportion of heterozygous Tt offspring.", "", "Short plants appear because both parents carry the recessive allele."]),
        QUIZ("A tall plant is crossed with a short plant. Half the offspring are tall and half are short. What is the genotype of the tall parent?", ["TT", "Tt", "tt", "It cannot be known"], 1,
             "A 1:1 ratio shows that the tall parent was heterozygous (Tt x tt gives 1 Tt : 1 tt).",
             hint="If it were TT all the offspring would be tall.",
             feedback=["TT x tt gives all tall offspring.", "", "A tt plant would be short.", "The ratio of offspring shows the genotype."]),
        PQ("Explain the meaning of the terms genotype and phenotype, with one example of each.", "Genotype is the combination of alleles an organism has, for example Tt. Phenotype is the visible characteristic, for example tall."),
        PQ("In pea plants, tall (T) is dominant to short (t). Show the cross between a homozygous tall plant and a short plant, and give the genotype and phenotype of the F1.", "Parents TT x tt. Gametes: T and t. All offspring Tt. All F1 are tall (heterozygous)."),
        PQ("Two heterozygous tall plants are crossed. What is the probability that a seed chosen at random will be tall? What is the probability that two seeds chosen in turn will both be short?", "Tall (TT or Tt) = 3 out of 4, or 3/4 (75 percent). Short = 1/4. Both short = 1/4 x 1/4 = 1/16."),
        PQ("Explain how a test cross shows whether a tall plant is TT or Tt.", "Cross it with a short plant (tt). If all offspring are tall the tall plant was TT. If about half are short, the plant was Tt."),
        SUM("A gene is a section of DNA; alleles are forms of a gene. The dominant allele shows in a heterozygote.",
            "Genotype = alleles; phenotype = appearance. Homozygous = two alleles the same; heterozygous = different.",
            "Gametes carry one allele. Use a Punnett square to find every fertilization.",
            "Tt x Tt: 1 TT : 2 Tt : 1 tt, or 3 dominant : 1 recessive (probability of recessive is 1/4).",
            "Test cross with tt: all dominant means TT; 1:1 means Tt."),
    ],
))


# ------------------------------------------------------------------ 10. Sex determination and genetic disorders
LESSONS.append(lesson(
    module=MODULE, topic=SEX,
    title="Sex determination, sickle-cell anaemia, haemophilia and Down syndrome",
    slug="hbi3-sex-determination-disorders",
    minutes=25,
    summary="Sex is determined by the X and Y chromosomes: a child has an equal chance of being a girl or a boy. Sickle-cell anaemia is recessive, haemophilia is X-linked recessive, and Down syndrome is caused by an extra chromosome 21.",
    objectives=[
        "Explain how sex is determined and why the chance of a boy or a girl is equal",
        "Work out the genotypes and probabilities in sickle-cell crosses",
        "Explain why haemophilia is more common in males and work out a cross",
        "Describe the cause of Down syndrome",
    ],
    key_concepts=["Sex chromosomes", "XX and XY", "Sickle-cell anaemia", "Carrier", "Haemophilia", "Sex-linked", "Down syndrome", "Mutation"],
    blocks=[
        H("Introduction"),
        T("A family in Maroua has three girls and the parents hope for a boy; another family in Buea has twin brothers. In both families the sex of each child "
          "was decided by chance at fertilization. In this lesson we use the rules from the last lesson to explain how sex is decided and how some "
          "inherited conditions pass through families. Genetic conditions are nobody's fault and are not infectious. A health worker or genetic counsellor can advise families."),
        H("Sex determination"),
        T("A human body cell has 46 chromosomes in 23 pairs. Twenty-two pairs are the same in males and females. The 23rd pair is the pair of **sex chromosomes**. "
          "Females have two X chromosomes (**XX**). Males have one X and one smaller Y chromosome (**XY**)."),
        T("Every egg carries an X chromosome. Half of the sperm carry an X and half carry a Y. So the sex of the child depends on the **sperm** that fertilises the egg."),
        CODE("               Sperm from father (XY)\n"
             "                  X         Y\n"
             "Eggs     X       XX        XY\n"
             "from     X       XX        XY\n"
             "mother\n\n"
             "XX = girl (1/2)     XY = boy (1/2)",
             "text", title="Sex determination"),
        T("The chance of a girl is 1 in 2 (50 percent) and the chance of a boy is 1 in 2 (50 percent) at every pregnancy, whatever the sex of earlier children. "
          "Women do not decide the sex of the baby: the father's sperm does."),
        H("Sickle-cell anaemia"),
        D("**Sickle-cell anaemia** is an inherited blood disease. The gene for haemoglobin (the red pigment that carries oxygen) has a faulty allele, S, that makes the red blood cells "
          "bend into a sickle shape. These cells carry less oxygen and can block small blood vessels, causing pain, tiredness and anaemia.", title="Sickle-cell anaemia"),
        T("The normal allele is A (haemoglobin A) and the faulty allele is S. S is recessive for the disease. The three genotypes are:"),
        KEY("Genotypes in sickle-cell inheritance", "Learn what each genotype means.", cards=[
            ["AA", "Normal haemoglobin. Healthy."],
            ["AS (sickle-cell trait, a carrier)", "One normal and one faulty allele. Usually healthy. The person can pass S to children."],
            ["SS", "Two faulty alleles. Has sickle-cell anaemia."],
        ]),
        T("People with the AS genotype are more resistant to severe malaria than people with AA. In places where malaria is common, such as much of Africa, this is why the S allele is "
          "fairly common. Malaria is covered in the public health module."),
        CODE("Carrier x carrier:  AS x AS\n"
             "               A         S\n"
             "        A     AA        AS\n"
             "        S     AS        SS\n"
             "1 AA : 2 AS : 1 SS\n"
             "25% normal, 50% carriers, 25% sickle-cell anaemia\n\n"
             "Carrier x normal:  AS x AA\n"
             "        A     AA        AA\n"
             "        S     AS        AS\n"
             "50% AA, 50% AS (no child has the disease)",
             "text", title="Sickle-cell crosses"),
        H("Haemophilia"),
        D("**Haemophilia** is an inherited condition in which the blood does not clot properly, so a person bleeds for a long time after even a small cut. "
          "The faulty allele (Xh) is **recessive** and is carried on the **X chromosome**. Such a condition is **sex-linked** (X-linked).", title="Haemophilia"),
        T("The Y chromosome does not carry this gene. A male has only one X, so one faulty allele (XhY) is enough to cause the disease. A female needs two (XhXh), "
          "so females with one Xh (XHXh) are healthy **carriers**. For this reason haemophilia is much more common in males."),
        KEY("Genotypes", "H = normal allele, h = haemophilia allele.", cards=[
            ["XHXH", "Normal female"],
            ["XHXh", "Carrier female (healthy)"],
            ["XhXh", "Female with haemophilia (very rare)"],
            ["XHY", "Normal male"],
            ["XhY", "Male with haemophilia"],
        ]),
        CODE("Carrier mother (XHXh) x normal father (XHY)\n"
             "                 XH        Y\n"
             "         XH     XHXH      XHY\n"
             "         Xh     XHXh      XhY\n"
             "Daughters: 1 normal, 1 carrier (none affected)\n"
             "Sons: 1 normal, 1 with haemophilia\n"
             "Each child: 1/4 normal girl, 1/4 carrier girl, 1/4 normal boy, 1/4 boy with haemophilia\n"
             "Probability a son is affected: 1/2. Probability a child is affected: 1/4.",
             "text", title="Haemophilia cross"),
        T("If a man with haemophilia (XhY) has children with a woman who is not a carrier (XHXH), all the daughters are carriers (XHXh) and all the sons are normal (XHY). "
          "A son gets his Y from his father and his X from his mother, so a father cannot pass haemophilia to his sons."),
        H("Down syndrome"),
        D("**Down syndrome** is caused by an extra copy of chromosome 21, so the person has 47 chromosomes instead of 46. It happens when the chromosomes fail to separate properly while "
          "the egg or sperm is made. It is not inherited from a faulty allele in the usual way, and nobody is to blame.", title="Down syndrome"),
        T("People with Down syndrome have some typical physical features and some learning difficulty and may have heart or other health problems, "
          "but they can enjoy life and learn with support. The chance of having a child with Down syndrome rises as the mother's age increases. Families get help from health workers and schools."),
        TIP("**Exam link.** Paper 1 gives a cross and asks for the probability, or the number of chromosomes in Down syndrome. Paper 2 Section A can ask you to explain the inheritance of sex, sickle-cell anaemia or haemophilia with a "
            "genetic diagram. Write the parents' genotypes, the gametes and the Punnett square, then the ratio, and always define your symbols (for example A and S, or XH and Xh)."),
        EX("Worked example 1: a sickle-cell family", intro="Both parents are carriers of the sickle-cell allele (AS). Find the probability that a child has sickle-cell anaemia. (A model answer.)", steps=[
            S("Gametes", text="Each parent makes A gametes and S gametes."),
            S("Square", text="The four boxes are AA, AS, AS and SS."),
            S("Answer", math=r"P(\text{SS}) = \frac{1}{4} = 25\%", text="The chance is 1 in 4 for each child."),
        ]),
        EX("Worked example 2: a haemophilia cross", intro="A carrier woman (XHXh) and a normal man (XHY) have a child. What is the chance that it is a boy with haemophilia? (A model answer.)", steps=[
            S("Gametes", text="Mother: XH and Xh. Father: XH and Y."),
            S("Square", text="The four boxes are XHXH, XHY, XHXh, XhY."),
            S("Answer", math=r"P(X^hY) = \frac{1}{4}", text="One of the four equally likely children is a boy with haemophilia. (Among sons only, the chance is one half.)"),
        ]),
        MISTAKE("Saying haemophilia only affects males", "It affects males mostly. A female can be a carrier, or very rarely have the disease if she inherits Xh from both parents."),
        MISTAKE("Thinking the baby's sex is decided by the mother", "Every egg has an X. The sex depends on whether an X-sperm or Y-sperm fertilises it."),
        QUIZ("A normal woman (AA) and a man with sickle-cell trait (AS) have a child. What is the chance the child has sickle-cell anaemia (SS)?", ["0 (none)", "One quarter", "One half", "All"], 0,
             "AA x AS gives AA and AS only, so no child can be SS. Half will be carriers.",
             hint="The mother has no S allele to give.",
             feedback=["", "A quarter is the chance when both parents are AS.", "One half is the chance of being a carrier.", "SS needs an S from each parent."]),
        QUIZ("How many chromosomes does a person with Down syndrome have in each body cell?", ["23", "45", "46", "47"], 3,
             "There is an extra chromosome 21, so 46 + 1 = 47.",
             hint="The normal number is 46.",
             feedback=["23 is the number in a gamete.", "45 is one fewer than normal.", "46 is the normal number.", ""]),
        PQ("Explain why the chance that a baby is a girl is one half.", "Every egg carries an X. Half the sperm carry an X and half carry a Y. An X sperm gives XX (girl) and a Y sperm gives XY (boy), so each is equally likely."),
        PQ("Both parents have sickle-cell trait (AS). Draw a genetic diagram and state the ratio of genotypes in the children.", "Gametes A and S from each parent. The square gives AA, AS, AS, SS: 1 AA : 2 AS : 1 SS (25 percent normal, 50 percent carriers, 25 percent with sickle-cell anaemia)."),
        PQ("Explain why haemophilia is more common in males than in females.", "The allele for haemophilia is recessive and carried on the X chromosome. A male has only one X, so one faulty allele causes the disease. A female needs two faulty alleles, and females with one are healthy carriers."),
        PQ("State the cause of Down syndrome.", "An extra copy of chromosome 21, giving 47 chromosomes in each body cell, caused by chromosomes failing to separate when the egg or sperm is formed."),
        SUM("Females are XX and males are XY. The father's sperm decides the sex. The chance of a girl or boy is 1/2.",
            "Sickle-cell anaemia: SS. AS is a carrier. AS x AS gives 1 AA : 2 AS : 1 SS. AS gives some protection from severe malaria.",
            "Haemophilia is X-linked recessive: XhY is affected; XHXh is a healthy carrier. Carrier mother x normal father: 1/2 of the sons are affected.",
            "Down syndrome: three copies of chromosome 21 (47 chromosomes).",
            "Genetic conditions are not infectious; a health worker gives advice and support."),
    ],
))

