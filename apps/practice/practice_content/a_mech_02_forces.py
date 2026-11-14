"""Practice sets for A Level Pure Mathematics with Mechanics (Lower Sixth): Forces and Newton's laws.

All data are invented for practice. g = 9.8 m/s^2 unless a question says otherwise.
"""

from .dsl import *  # noqa: F403

COURSE = ("pure-mathematics-with-mechanics", "lower-sixth")

MODULE = "Forces & Newton's Laws"


def MCQ(prompt, correct, wrongs, pos, steps, **kw):
    """Multiple choice with the correct option at index `pos`; `wrongs` is a list of (text, why)."""
    choices = [C(t, why=w) for t, w in wrongs]
    choices.insert(pos, C(correct, correct=True))
    return MC(prompt, choices, steps, **kw)


SETS = []

# ---------------------------------------------------------------- 1. Forces and equilibrium
SETS.append(practice_set(
    module=MODULE, topic="Forces and equilibrium",
    title="Resolving forces and equilibrium of a particle", lesson="mel2-resolving-forces-equilibrium",
    questions=[
        MCQ(r"What is the weight of a 6 kg bag of rice? (Take $g = 9.8\ \text{m/s}^2$.)", r"$58.8$ N", [
            (r"$6$ N", "6 is the mass in kg. Weight is the force $mg$ in newtons."),
            (r"$0.61$ N", r"You divided by $g$ instead of multiplying: weight is $mg$."),
            (r"$60$ N", r"This uses $g = 10$. The question says $g = 9.8$."),
        ], 1, [S("Weight is mass times $g$", math=r"W = mg = 6 \times 9.8 = 58.8\ \text{N}")],
           concept="Weight W = mg", skill="Recall", hint="Weight is a force. Which formula connects mass and weight?"),
        MCQ(r"A force of 30 N acts at $35^\circ$ above the horizontal. What is its **vertical** component?", r"$17.2$ N", [
            (r"$24.6$ N", r"$30\cos 35^\circ$ is the horizontal component."),
            (r"$30$ N", "A component of a force at an angle is smaller than the force."),
            (r"$52.3$ N", r"You divided $30$ by $\sin 35^\circ$. A component is found by multiplying."),
        ], 2, [S("The angle is with the horizontal, so the vertical component is the side opposite it", math=r"30\sin 35^\circ = 17.2\ \text{N}")],
           concept="Resolving a force", skill="Calculation", hint="Sketch the right-angled triangle. Is the vertical side next to the $35^\\circ$ angle or opposite it?"),
        NUM(r"Two forces of 10 N and 6 N act on a particle at a point. The angle between their directions is $60^\circ$. Find the magnitude of the resultant, in newtons.", 14, [
            S("Take the 10 N force along the $x$-axis. Resolve the 6 N force", math=r"6\cos 60^\circ = 3, \qquad 6\sin 60^\circ = 5.196"),
            S("Add components", math=r"X = 10 + 3 = 13, \qquad Y = 5.196"),
            S("Resultant", math=r"R = \sqrt{13^2 + 5.196^2} = \sqrt{196} = 14\ \text{N}"),
        ], tolerance=0.05, unit="N", concept="Resultant of two forces", skill="Calculation", hint="Put one force along the $x$-axis and resolve the other into $x$ and $y$ components."),
        MCQ(r"A particle is in equilibrium under three forces: 12 N due east, 5 N due north and a force $F$. Which statement about $F$ is correct?", r"$13$ N, acting $22.6^\circ$ south of west", [
            (r"$13$ N, acting $22.6^\circ$ north of east", "That is the direction of the resultant of the other two forces. $F$ must act the opposite way."),
            (r"$17$ N, acting $22.6^\circ$ south of west", "You added $12 + 5$. The two forces are at right angles, so the resultant is found with Pythagoras."),
            (r"$13$ N, acting $67.4^\circ$ south of west", r"You measured the angle from the south line. $\tan\theta = 5/12$ gives $22.6^\circ$ from the west line."),
        ], 0, [
            S("The resultant of the 12 N and 5 N forces", math=r"\sqrt{12^2 + 5^2} = 13\ \text{N},\ \ \tan\alpha = \tfrac{5}{12},\ \alpha = 22.6^\circ\ \text{north of east}"),
            S("In equilibrium $F$ is equal and opposite to that resultant", text="So $F = 13$ N, $22.6^\\circ$ south of west."),
        ], concept="Equilibrium: balancing force", skill="Concept", hint="In equilibrium the three forces add up to zero. What must $F$ do to the other two?"),
        NUM(r"A lamp of mass 5 kg hangs from a horizontal beam by two light strings that each make $40^\circ$ with the beam (see the figure). Find the tension in one string, in newtons, to 3 significant figures.", 38.1, [
            S("The strings are symmetrical, so the tensions are equal, $T$. Weight", math=r"W = 5 \times 9.8 = 49\ \text{N}"),
            S("Resolve vertically", math=r"2T\sin 40^\circ = 49"),
            S("Solve", math=r"T = \frac{49}{2\sin 40^\circ} = 38.1\ \text{N}"),
        ], tolerance=0.2, unit="N", concept="Two strings in equilibrium", skill="Application", hint="Write down the vertical equilibrium equation. The horizontal parts cancel by symmetry.",
           diagram="apomel2-two-strings-q.svg", diagram_alt="A lamp of mass 5 kg hangs from a beam by two strings, each at 40 degrees to the horizontal"),
        NUM(r"A 15 kg block rests on a horizontal floor. A student pushes it with a force of 40 N directed $30^\circ$ **below** the horizontal. The block does not move. Find the normal reaction of the floor, in newtons.", 167, [
            S("Weight", math=r"15 \times 9.8 = 147\ \text{N}"),
            S(r"Resolve vertically. The push has a downward part $40\sin 30^\circ = 20$ N", math=r"R = 147 + 20 = 167\ \text{N}"),
        ], tolerance=0.5, unit="N", concept="Normal reaction with an angled force", skill="Application", hint="Which forces act vertically on the block? A push pointing downwards at an angle has a vertical part."),
        MCQ(r"A lamp hangs in equilibrium from two light strings. One string makes $30^\circ$ with the horizontal and the other makes $60^\circ$ (on the opposite side). What is the ratio $\dfrac{\text{tension in the }60^\circ\text{ string}}{\text{tension in the }30^\circ\text{ string}}$?", r"$\sqrt{3} \approx 1.73$", [
            (r"$\dfrac{1}{\sqrt{3}} \approx 0.577$", "You equated the vertical components. It is the **horizontal** components that are equal, because nothing else pulls sideways."),
            (r"$1$", "The tensions are equal only when the two strings make the same angle with the horizontal."),
            (r"$3$", r"You used $\tan 60^\circ \div \tan 30^\circ$. Equate the horizontal components $T_1\cos 30^\circ = T_2\cos 60^\circ$."),
        ], 3, [
            S("Horizontal components are equal", math=r"T_{30}\cos 30^\circ = T_{60}\cos 60^\circ"),
            S("Ratio", math=r"\frac{T_{60}}{T_{30}} = \frac{\cos 30^\circ}{\cos 60^\circ} = \frac{0.866}{0.5} = \sqrt{3} = 1.73"),
        ], concept="Horizontal balance of tensions", skill="Reasoning", hint="Only the strings pull sideways. What does equilibrium say about their horizontal components?"),
        NUM(r"A particle of weight 25 N hangs from a string. A horizontal force pulls the particle sideways until the string makes $50^\circ$ with the vertical and the particle is in equilibrium. Find the horizontal force, in newtons, to 3 significant figures.", 29.8, [
            S("Vertically, the string's vertical component supports the weight", math=r"T\cos 50^\circ = 25"),
            S("Horizontally", math=r"Q = T\sin 50^\circ"),
            S("Divide the two equations", math=r"Q = 25\tan 50^\circ = 29.8\ \text{N}"),
        ], tolerance=0.1, unit="N", concept="Force at an angle to the vertical", skill="Application", hint="The angle is measured from the **vertical**. Which component of the tension balances the weight?"),
    ]))

# ---------------------------------------------------------------- 2. Newton's second law and connected particles
SETS.append(practice_set(
    module=MODULE, topic="Newton's laws and connected particles",
    title="Newton's second law and particles in a line", lesson="mel2-newton-second-law-connected",
    questions=[
        MCQ(r"Which statement is Newton's second law of motion for a particle of mass $m$?", r"The **resultant** force on the particle equals $ma$, in the direction of the resultant force.", [
            (r"Any force acting on the particle equals $ma$.", "The law uses the resultant of **all** forces. A single force equals $ma$ only if it is the only force."),
            (r"The weight of the particle equals $ma$ whatever its motion.", r"The weight is $mg$. It equals $ma$ only in free fall, where $a = g$."),
            (r"The force on the particle equals its mass divided by its acceleration.", "The law is a product, $F = ma$, not a quotient."),
        ], 0, [S("State the law", text=r"Resultant force $= ma$, acting in the direction of the acceleration.")],
           concept="Newton's second law", skill="Recall", hint="Think about the word 'resultant': what is it the resultant of?"),
        NUM(r"A van of mass 1500 kg is driven along a straight horizontal road with a driving force of 4200 N. The total resistance to motion is 900 N. Find the acceleration of the van, in $\text{m/s}^2$.", 2.2, [
            S("Resultant force", math=r"4200 - 900 = 3300\ \text{N}"),
            S("Newton's second law", math=r"3300 = 1500a \;\Rightarrow\; a = 2.2\ \text{m/s}^2"),
        ], tolerance=0.01, unit="m/s^2", concept="F = ma on a level road", skill="Calculation", hint="Find the resultant force first: driving force minus resistance."),
        MCQ(r"A man of mass 70 kg stands in a lift that is moving upwards at a **constant** speed of $3\ \text{m/s}$. What is the reaction of the floor on him? (Use $g = 9.8$.)", r"$686$ N", [
            (r"$896$ N", "You used the speed $3$ as if it were an acceleration: $70 \\times 3 = 210$. Constant speed means zero acceleration."),
            (r"$476$ N", "You subtracted $70 \\times 3$. Speed does not change the reaction; only acceleration does."),
            (r"$0$ N", "The man is supported by the floor. The reaction is zero only in free fall."),
        ], 2, [
            S("Constant speed means $a = 0$, so the forces balance", math=r"R = mg = 70 \times 9.8 = 686\ \text{N}"),
        ], concept="Lift at constant speed", skill="Concept", hint="What is the acceleration of a lift that moves at constant speed?"),
        MCQ(r"The same man (70 kg) is in a lift that accelerates **upwards** at $1.5\ \text{m/s}^2$. What is the reaction of the floor on him?", r"$791$ N", [
            (r"$105$ N", "That is only $ma$, the resultant force. The reaction must also support the weight."),
            (r"$581$ N", "You used $m(g - a)$, which is for a lift accelerating downwards."),
            (r"$686$ N", "That is the reaction with no acceleration. The upward acceleration adds to it."),
        ], 3, [
            S("Take upwards as positive", math=r"R - 70(9.8) = 70(1.5)"),
            S("Solve", math=r"R = 686 + 105 = 791\ \text{N}"),
        ], concept="Lift accelerating upwards", skill="Calculation", hint="Write $R - mg = ma$ with upwards positive."),
        NUM(r"A tractor of mass 2000 kg pulls a trailer of mass 1000 kg along a straight horizontal road. The driving force is 5000 N. The resistances are 400 N on the tractor and 200 N on the trailer. Find the tension in the tow-bar, in newtons, to 3 significant figures.", 1670, [
            S("Whole system to find $a$", math=r"5000 - 400 - 200 = 3000a \;\Rightarrow\; a = 1.467\ \text{m/s}^2"),
            S("Trailer alone", math=r"T - 200 = 1000(1.467)"),
            S("Solve", math=r"T = 1667 \approx 1670\ \text{N}"),
        ], tolerance=5, unit="N", concept="Tension in a tow-bar", skill="Application", hint="Find the acceleration of the whole system first. The tension does not appear in that equation."),
        MCQ(r"A lorry of mass 2000 kg pulls a trailer of mass 800 kg. The driving force is 6000 N; the resistances are 300 N on the lorry and 100 N on the trailer; the tow-bar tension is $T$. Which equation is correct for the **whole system**, with acceleration $a$?", r"$6000 - 300 - 100 = 2800a$", [
            (r"$6000 - 300 - 100 - T = 2800a$", "The tension is an internal force. It acts on both parts with opposite signs and cancels in the whole-system equation."),
            (r"$6000 - 300 - T = 2800a$", "This mixes the lorry's equation with the total mass. Use either the lorry alone (mass 2000) or the whole system with all forces."),
            (r"$6000 = 2800a$", "You left out the resistances. The resultant force is the driving force minus **all** resistances."),
        ], 1, [
            S("Internal forces cancel; total mass $2000 + 800 = 2800$ kg", math=r"6000 - 300 - 100 = 2800a"),
        ], concept="Whole-system equation", skill="Concept", hint="Which forces on the system come from outside it?"),
        NUM(r"A crate of mass 6 kg is on a smooth horizontal floor. A rope pulls it with a force of 30 N at $35^\circ$ above the horizontal. Starting from rest, find the speed of the crate after 4 seconds, in $\text{m/s}$, to 3 significant figures.", 16.4, [
            S("Horizontal force and acceleration", math=r"30\cos 35^\circ = 6a \;\Rightarrow\; a = 4.096\ \text{m/s}^2"),
            S("Constant acceleration from rest", math=r"v = at = 4.096 \times 4 = 16.4\ \text{m/s}"),
        ], tolerance=0.1, unit="m/s", concept="Angled pull then v = u + at", skill="Application", hint="Only the horizontal component of the pull accelerates the crate. Find the acceleration, then use $v = u + at$."),
        NUM(r"A parcel of mass 12 kg hangs from a light rope and is raised so that the tension in the rope is 150 N. Find the upward acceleration of the parcel, in $\text{m/s}^2$ (take $g = 9.8$).", 2.7, [
            S("Weight", math=r"12 \times 9.8 = 117.6\ \text{N}"),
            S("Upwards is positive", math=r"150 - 117.6 = 12a"),
            S("Solve", math=r"a = \frac{32.4}{12} = 2.7\ \text{m/s}^2"),
        ], tolerance=0.02, unit="m/s^2", concept="Vertical motion on a rope", skill="Application", hint="Two forces act on the parcel: tension and weight. Which is larger?"),
    ]))

# ---------------------------------------------------------------- 3. Pulleys and tables
SETS.append(practice_set(
    module=MODULE, topic="Newton's laws and connected particles",
    title="Pulleys, tables and the force on a pulley", lesson="mel2-pulleys-and-tables",
    questions=[
        MCQ(r"A light inextensible string passes over a smooth pulley and joins two particles. Which statement about the string is correct while it is taut?", r"The tension is the same in both parts of the string, and the particles have accelerations of equal magnitude.", [
            (r"The tension is larger on the side of the heavier particle.", "That would need a rough pulley. A smooth pulley changes the direction of the tension but not its size."),
            (r"The tension equals the weight of the heavier particle.", "That is true only if nothing accelerates. The heavier particle moves down, so $T < mg$ for it."),
            (r"The lighter particle accelerates faster, because it has less mass.", "The string cannot stretch, so both particles have accelerations of the same magnitude."),
        ], 0, [S("Recall the standard model", text="Smooth pulley and light string give the same tension throughout; an inextensible string gives equal accelerations.")],
           concept="Assumptions: light string, smooth pulley", skill="Recall", hint="Which two properties of the string and the pulley make the tension the same on both sides?"),
        NUM(r"Particles of mass 9 kg and 5 kg hang from the ends of a light string over a smooth fixed pulley. They are released from rest. Find the magnitude of the acceleration, in $\text{m/s}^2$.", 2.8, [
            S("9 kg moves down, 5 kg moves up", math=r"9(9.8) - T = 9a, \qquad T - 5(9.8) = 5a"),
            S("Add", math=r"4(9.8) = 14a \;\Rightarrow\; a = 2.8\ \text{m/s}^2"),
        ], tolerance=0.02, unit="m/s^2", concept="Two hanging particles", skill="Calculation", hint="Write $F = ma$ for each particle separately and add the equations."),
        MCQ(r"Particles of mass 7 kg and 3 kg hang from the ends of a light string over a smooth fixed pulley and are released from rest. What is the tension in the string?", r"$41.2$ N", [
            (r"$68.6$ N", "That is the weight of the 7 kg particle. It is accelerating downwards, so the tension is less than its weight."),
            (r"$29.4$ N", "That is the weight of the 3 kg particle. It accelerates upwards, so the tension is greater than its weight."),
            (r"$49$ N", "You averaged the two weights. Find $a$ first, then use one particle's equation."),
        ], 2, [
            S("Find $a$", math=r"7g - 3g = 10a \;\Rightarrow\; a = 3.92\ \text{m/s}^2"),
            S("3 kg particle", math=r"T = 3(9.8 + 3.92) = 41.2\ \text{N}"),
        ], concept="Tension on a pulley", skill="Calculation", hint="Find the acceleration first, then use the equation of motion of one particle."),
        NUM(r"Particle A of mass 6 kg lies on a smooth horizontal table. A light string joins A over a smooth pulley at the edge of the table to particle B of mass 2 kg, which hangs freely (see the figure). The system is released from rest. Find the tension in the string, in newtons.", 14.7, [
            S("A: horizontal force is the tension", math=r"T = 6a"),
            S("B: down is positive", math=r"2(9.8) - T = 2a"),
            S("Add", math=r"19.6 = 8a \;\Rightarrow\; a = 2.45\ \text{m/s}^2"),
            S("Tension", math=r"T = 6 \times 2.45 = 14.7\ \text{N}"),
        ], tolerance=0.05, unit="N", concept="Table and pulley", skill="Application", hint="Write an equation for A (what force pulls it?) and one for B, then eliminate the acceleration.",
           diagram="apomel2-pulley-table-q.svg", diagram_alt="Particle A of mass 6 kg on a smooth table joined over a smooth pulley at the table edge to particle B of mass 2 kg hanging"),
        MCQ(r"A particle A of mass 6 kg on a smooth horizontal table is joined over a smooth pulley at the table edge to a hanging particle B of mass 2 kg (see the figure). While the system moves, the tension is 14.7 N. What is the magnitude of the force exerted by the string on the pulley?", r"$20.8$ N", [
            (r"$14.7$ N", "This is a single tension. The string pulls the pulley along both parts."),
            (r"$29.4$ N", "$2T$ is correct only if both parts of the string are parallel. Here they are at $90^\\circ$."),
            (r"$10.4$ N", r"You used $T/\sqrt{2}$. The resultant of two perpendicular forces $T$ is $T\sqrt{2}$."),
        ], 3, [
            S("The two parts are horizontal and vertical, so they are at $90^\\circ$", math=r"F = 2T\cos 45^\circ = T\sqrt{2} = 14.7\sqrt{2} = 20.8\ \text{N}"),
        ], concept="Force on a pulley", skill="Application", hint="Add the two tensions as vectors. What is the angle between the two parts of the string?",
           diagram="apomel2-pulley-table-q.svg", diagram_alt="Particle A of mass 6 kg on a smooth table joined over a smooth pulley at the table edge to particle B of mass 2 kg hanging"),
        MCQ(r"Particle A of mass 6 kg on a smooth horizontal table is joined over a smooth pulley at the table edge to a hanging particle B of mass 2 kg (see the figure). B is released from rest, falls, hits the floor and stays there. Which statement describes what happens next to A (assume A has not reached the pulley)?", r"The string is slack and A moves on at constant speed.", [
            (r"A stops immediately, because B has stopped.", "A has the speed of B at that instant. With no horizontal force on it, it keeps that velocity (Newton's first law)."),
            (r"A continues to accelerate at the same rate as before.", "The acceleration came from B's weight pulling through the string. With the string slack, there is no horizontal force on A."),
            (r"A decelerates, because the string now pulls it back.", "The string is slack, so it exerts no force. Also the table is smooth, so there is no friction."),
        ], 1, [
            S("When B stops, the string is no longer taut, so $T = 0$"),
            S("The table is smooth and there is no horizontal force on A", text="By Newton's first law, A moves on at constant velocity."),
        ], concept="String goes slack", skill="Reasoning", hint="When B lands, what happens to the tension? What force is then left acting on A horizontally?",
           diagram="apomel2-pulley-table-q.svg", diagram_alt="Particle A of mass 6 kg on a smooth table joined over a smooth pulley at the table edge to particle B of mass 2 kg hanging"),
        NUM(r"In the system of the figure (A of mass 6 kg on a smooth table, joined over a smooth pulley to B of mass 2 kg hanging), B is released from rest 0.5 m above the floor. Find the speed of B just before it hits the floor, in $\text{m/s}$, to 3 significant figures.", 1.57, [
            S("From the equations of motion, $a = 2.45\\ \\text{m/s}^2$"),
            S("Constant acceleration from rest over 0.5 m", math=r"v^2 = 2(2.45)(0.5) = 2.45 \;\Rightarrow\; v = 1.57\ \text{m/s}"),
        ], tolerance=0.01, unit="m/s", concept="Speed at the end of the taut stage", skill="Application", hint="You need the acceleration of the system first. Then use $v^2 = u^2 + 2as$.",
           diagram="apomel2-pulley-table-q.svg", diagram_alt="Particle A of mass 6 kg on a smooth table joined over a smooth pulley at the table edge to particle B of mass 2 kg hanging"),
        NUM(r"Particles of mass 3 kg and 1 kg hang from a light string over a smooth fixed pulley. The 3 kg particle is released from rest 0.8 m above the floor. After it hits the floor, find the further distance the 1 kg particle rises, in metres.", 0.4, [
            S("Taut stage", math=r"a = \frac{(3 - 1)(9.8)}{4} = 4.9\ \text{m/s}^2, \qquad v^2 = 2(4.9)(0.8) = 7.84"),
            S("String goes slack; the 1 kg particle moves under gravity", math=r"0 = 7.84 - 2(9.8)h \;\Rightarrow\; h = 0.4\ \text{m}"),
        ], tolerance=0.01, unit="m", concept="Slack string, motion under gravity", skill="Application", hint="Split into two stages. What is the speed of the 1 kg particle when the 3 kg particle lands, and what is its acceleration afterwards?"),
    ]))

# ---------------------------------------------------------------- 4. Friction
SETS.append(practice_set(
    module=MODULE, topic="Friction",
    title="Friction on rough horizontal surfaces", lesson="mel2-friction-law",
    questions=[
        MCQ(r"A particle rests on a rough horizontal surface with coefficient of friction $\mu$ and normal reaction $R$. Which statement about the friction force $F$ is correct?", r"$F \le \mu R$, with equality when the particle is about to slip.", [
            (r"$F = \mu R$ at all times.", r"This holds only when the particle is sliding or about to slide. A particle at rest and not about to move has $F < \mu R$."),
            (r"$F \ge \mu R$ when the particle moves.", "Friction never exceeds $\\mu R$. When sliding, $F = \\mu R$ exactly."),
            (r"$F = \mu W$, where $W$ is the weight, always.", "The law uses the normal reaction $R$. $R = W$ only when there is no other vertical force."),
        ], 2, [S("State the law", text=r"$F \le \mu R$; $F = \mu R$ in limiting equilibrium and while sliding.")],
           concept="The friction law", skill="Recall", hint="Think about the three cases: at rest, about to slip, sliding."),
        MCQ(r"A box of mass 8 kg rests on a rough horizontal floor with $\mu = 0.4$. A horizontal force of 25 N is applied. What is the friction force? (Take $g = 9.8$.)", r"$25$ N", [
            (r"$31.4$ N", r"This is the maximum friction $\mu R$. The push (25 N) is less than it, so the box is not about to move and friction only balances the push."),
            (r"$0$ N", "The push is trying to move the box, so friction must act to resist it."),
            (r"$6.4$ N", "You subtracted 25 from 31.4. Friction does not equal the gap between the push and the limit."),
        ], 0, [
            S("Maximum friction", math=r"\mu R = 0.4 \times 8(9.8) = 31.4\ \text{N}"),
            S("The push 25 N is less than 31.4 N, so the box does not move", text="Friction balances the push: $F = 25$ N."),
        ], concept="Friction at rest", skill="Concept", hint="Find the maximum friction first and compare it with the push."),
        NUM(r"A crate of mass 50 kg lies on a rough horizontal floor with coefficient of friction $0.3$. Find the smallest horizontal force that will make it move, in newtons.", 147, [
            S("Normal reaction", math=r"R = 50(9.8) = 490\ \text{N}"),
            S("On the point of moving, friction is limiting", math=r"P = \mu R = 0.3 \times 490 = 147\ \text{N}"),
        ], tolerance=0.5, unit="N", concept="Limiting friction", skill="Calculation", hint="The crate is on the point of moving when the push equals the maximum friction."),
        MCQ(r"A box of mass 20 kg is pulled along a rough horizontal floor by a rope that makes $30^\circ$ with the horizontal, above the floor. The tension is 60 N. What is the normal reaction of the floor? (Take $g = 9.8$.)", r"$166$ N", [
            (r"$226$ N", "You added the vertical part of the tension. The rope pulls **upwards**, so it reduces the reaction."),
            (r"$196$ N", "This is $mg$. The rope's upward pull means the floor supports less than the full weight."),
            (r"$144$ N", r"You used $60\cos 30^\circ$ as the vertical part. The vertical component of a force at $30^\circ$ above the horizontal is $60\sin 30^\circ = 30$."),
        ], 3, [
            S("Resolve vertically", math=r"R + 60\sin 30^\circ = 20(9.8)"),
            S("Solve", math=r"R = 196 - 30 = 166\ \text{N}"),
        ], concept="Normal reaction with an angled pull", skill="Application", hint="Does the vertical part of the tension push the box into the floor or lift it?"),
        NUM(r"A block of mass 15 kg is pulled from rest along a rough horizontal floor by a horizontal force of 60 N. It travels 9 m in 3 s. Find the coefficient of friction, to 3 significant figures.", 0.204, [
            S("Acceleration from $s = \\tfrac12 at^2$", math=r"9 = \tfrac12 a(3)^2 \;\Rightarrow\; a = 2\ \text{m/s}^2"),
            S("Newton's second law", math=r"60 - F = 15(2) \;\Rightarrow\; F = 30\ \text{N}"),
            S("Sliding, so $F = \\mu R$ with $R = 15(9.8) = 147$", math=r"\mu = \frac{30}{147} = 0.204"),
        ], tolerance=0.002, unit="", concept="Coefficient of friction from motion", skill="Application", hint="Find the acceleration from the distance and time. Then find the friction force from $F = ma$."),
        MCQ(r"A block is at rest on a rough horizontal floor. A horizontal force $P$ is applied and increased slowly from zero until the block starts to move. Which statement is correct?", r"The friction force equals $P$ until $P$ reaches $\mu R$, and the block then starts to slide.", [
            (r"The friction force is always $\mu R$, whatever the value of $P$.", "Friction is $\\mu R$ only at the point of slipping and after it. For smaller $P$ friction just balances $P$."),
            (r"The friction force is zero until $P$ exceeds $\mu R$.", "Friction is present as soon as there is a tendency to move: it equals $P$ from the start."),
            (r"The friction force keeps increasing above $\mu R$ as $P$ increases.", "$\\mu R$ is the maximum. Beyond it the block slides with friction $\\mu R$."),
        ], 1, [
            S("Block at rest", text="Friction balances the applied force: $F = P$, with $P \\le \\mu R$."),
            S("When $P = \\mu R$ friction is limiting; any larger $P$ makes the block slide", text="Friction stays at $\\mu R$."),
        ], concept="Friction against applied force", skill="Reasoning", hint="Picture the graph of friction against the applied force. Where does it level off?"),
        NUM(r"A box of mass 20 kg is pulled along a rough horizontal floor by a light rope inclined at $30^\circ$ above the horizontal. The tension is 70 N and the coefficient of friction is $0.25$. Find the acceleration of the box, in $\text{m/s}^2$, to 3 significant figures.", 1.02, [
            S("Resolve vertically", math=r"R + 70\sin 30^\circ = 196 \;\Rightarrow\; R = 161\ \text{N}"),
            S("Friction while sliding", math=r"F = 0.25 \times 161 = 40.25\ \text{N}"),
            S("Resolve horizontally", math=r"70\cos 30^\circ - 40.25 = 20a \;\Rightarrow\; 60.62 - 40.25 = 20a"),
            S("Solve", math=r"a = 1.02\ \text{m/s}^2"),
        ], tolerance=0.01, unit="m/s^2", concept="Sliding with an angled pull", skill="Application", hint="Find $R$ first; the vertical part of the tension changes it."),
        NUM(r"Particle A of mass 4 kg lies on a rough horizontal table with coefficient of friction $0.2$. It is joined by a light string over a smooth pulley at the edge of the table to particle B of mass 3 kg, which hangs freely. The system is released from rest. Find the tension in the string, in newtons, to 3 significant figures.", 20.2, [
            S("Friction on A (sliding)", math=r"F = 0.2 \times 4(9.8) = 7.84\ \text{N}"),
            S("A: $T - 7.84 = 4a$. B: $3(9.8) - T = 3a$. Add", math=r"29.4 - 7.84 = 7a \;\Rightarrow\; a = 3.08\ \text{m/s}^2"),
            S("Tension", math=r"T = 3(9.8 - 3.08) = 20.16 \approx 20.2\ \text{N}"),
        ], tolerance=0.1, unit="N", concept="Rough table and pulley", skill="Application", hint="Write one equation for each particle. Friction acts on A only, opposing its motion."),
    ]))

# ---------------------------------------------------------------- 5. Motion on an inclined plane
SETS.append(practice_set(
    module=MODULE, topic="Motion on an inclined plane",
    title="Smooth and rough inclined planes", lesson="mel2-inclined-plane-motion",
    questions=[
        MCQ(r"A block of mass 5 kg is on a plane inclined at $30^\circ$ to the horizontal. What is the component of its weight **down the slope**? (Take $g = 9.8$.)", r"$24.5$ N", [
            (r"$42.4$ N", r"$5(9.8)\cos 30^\circ$ is the component **perpendicular** to the slope."),
            (r"$49$ N", "This is the whole weight. Only part of it acts along the slope."),
            (r"$28.3$ N", r"You used $mg\tan 30^\circ$. The component along the slope is $mg\sin\theta$; $\tan$ appears only when comparing with $\mu$."),
        ], 0, [S("Along the slope the weight component is $mg\\sin\\theta$", math=r"5 \times 9.8 \times \sin 30^\circ = 24.5\ \text{N}")],
           concept="Weight component along a slope", skill="Calculation", hint="Draw the right-angled triangle for the weight. Is $\\theta$ the angle between the weight and the slope, or between the weight and the normal?"),
        NUM(r"A particle slides down a smooth plane inclined at $20^\circ$ to the horizontal. Find its acceleration, in $\text{m/s}^2$, to 3 significant figures.", 3.35, [
            S("Along the slope", math=r"mg\sin 20^\circ = ma"),
            S("The mass cancels", math=r"a = 9.8\sin 20^\circ = 3.35\ \text{m/s}^2"),
        ], tolerance=0.01, unit="m/s^2", concept="Acceleration on a smooth slope", skill="Calculation", hint="Write Newton's second law along the slope. Which forces act in that direction on a smooth slope?"),
        MCQ(r"A block of mass 10 kg rests on a rough plane inclined at $25^\circ$ to the horizontal (see the figure). What is the normal reaction of the plane on the block? (Take $g = 9.8$.)", r"$88.8$ N", [
            (r"$41.4$ N", r"You used $mg\sin 25^\circ$. The normal reaction balances the component **perpendicular** to the slope, $mg\cos 25^\circ$."),
            (r"$98$ N", "This is $mg$. On a slope the normal reaction is smaller than the weight."),
            (r"$108$ N", r"You divided $98$ by $\cos 25^\circ$. Multiply: $R = mg\cos 25^\circ$."),
        ], 2, [S("Perpendicular to the slope there is no acceleration", math=r"R = mg\cos 25^\circ = 98\cos 25^\circ = 88.8\ \text{N}")],
           concept="Normal reaction on a slope", skill="Calculation", hint="Resolve perpendicular to the slope.",
           diagram="apomel2-incline-block-q.svg", diagram_alt="A block of mass 10 kg on a rough slope inclined at 25 degrees to the horizontal"),
        MCQ(r"The block of mass 10 kg in the figure rests on the rough plane inclined at $25^\circ$, with coefficient of friction $\mu = 0.5$. It does not move. What is the friction force on the block?", r"$41.4$ N up the slope", [
            (r"$44.4$ N up the slope", r"This is $\mu R$, the **maximum** friction. The block is not on the point of slipping ($\tan 25^\circ = 0.47 < 0.5$), so friction is only what is needed."),
            (r"$88.8$ N up the slope", "This is the normal reaction, not the friction force."),
            (r"$41.4$ N down the slope", "Friction opposes the tendency to slide. The block tends to slide down, so friction acts up the slope."),
        ], 0, [
            S("The block is in equilibrium. Along the slope", math=r"F = mg\sin 25^\circ = 98\sin 25^\circ = 41.4\ \text{N}"),
            S("Check", text=r"The maximum friction is $\mu R = 0.5 \times 88.8 = 44.4$ N, so 41.4 N can be supplied. Friction acts up the slope."),
        ], concept="Friction at rest on a slope", skill="Concept", hint="Is the block about to slip? If not, what does equilibrium along the slope say about friction?",
           diagram="apomel2-incline-block-q.svg", diagram_alt="A block of mass 10 kg on a rough slope inclined at 25 degrees to the horizontal"),
        NUM(r"A block is released from rest on a rough plane inclined at $30^\circ$ to the horizontal. The coefficient of friction is $0.3$. Find the acceleration of the block down the plane, in $\text{m/s}^2$, to 3 significant figures.", 2.35, [
            S("Perpendicular to the slope", math=r"R = mg\cos 30^\circ"),
            S("Down the slope, friction up the slope", math=r"mg\sin 30^\circ - 0.3\,mg\cos 30^\circ = ma"),
            S("Mass cancels", math=r"a = 9.8(0.5 - 0.3 \times 0.8660) = 2.35\ \text{m/s}^2"),
        ], tolerance=0.01, unit="m/s^2", concept="Acceleration on a rough slope", skill="Calculation", hint="Which way does the block slide, and so which way does friction act?"),
        MCQ(r"A block is placed on a rough plane inclined at $35^\circ$ to the horizontal. The coefficient of friction is $0.6$. Which statement is correct?", r"The block slides down, because $\tan 35^\circ = 0.70$ is greater than $0.6$.", [
            (r"The block stays at rest, because friction on a rough slope is always large enough.", "Friction has a maximum, $\\mu R$. If the slope is steep enough the weight component exceeds it."),
            (r"The block stays at rest, because $\mu = 0.6$ is greater than $\sin 35^\circ = 0.57$.", r"The test is $\mu$ against $\tan\theta$, not $\sin\theta$: $mg\sin\theta$ is compared with $\mu mg\cos\theta$."),
            (r"The block slides only if it is pushed first.", "Whether it slides depends only on the slope and $\\mu$, not on a push. Here the weight component already exceeds the limiting friction."),
        ], 1, [
            S("It slides if $mg\\sin\\theta > \\mu mg\\cos\\theta$, that is if $\\tan\\theta > \\mu$"),
            S("Compare", math=r"\tan 35^\circ = 0.700 > 0.6"),
        ], concept="Will it slide? tan(theta) against mu", skill="Reasoning", hint=r"Compare $mg\sin\theta$ with the limiting friction $\mu mg\cos\theta$ and simplify."),
        NUM(r"A block of mass 12 kg is pulled up a rough plane inclined at $15^\circ$ by a force of 90 N acting parallel to the plane. The coefficient of friction is $0.25$. Find the acceleration of the block, in $\text{m/s}^2$, to 3 significant figures.", 2.60, [
            S("Perpendicular", math=r"R = 12(9.8)\cos 15^\circ = 113.6\ \text{N}"),
            S("Friction (acts down the slope) and weight component", math=r"F = 0.25 \times 113.6 = 28.4\ \text{N}, \qquad 12(9.8)\sin 15^\circ = 30.4\ \text{N}"),
            S("Up the slope", math=r"90 - 30.4 - 28.4 = 12a \;\Rightarrow\; a = 2.60\ \text{m/s}^2"),
        ], tolerance=0.02, unit="m/s^2", concept="Pulled up a rough slope", skill="Application", hint="Friction opposes the motion: which way is the block moving?"),
        NUM(r"Particle A of mass 5 kg is on a rough plane inclined at $30^\circ$ (see the figure). It is joined by a light string over a smooth pulley at the top of the plane to a hanging particle B of mass 2 kg. The system stays at rest. Find the **smallest** possible coefficient of friction between A and the plane, to 3 significant figures.", 0.115, [
            S("B at rest, so $T = 2(9.8) = 19.6$ N. A has a weight component down the slope of", math=r"5(9.8)\sin 30^\circ = 24.5\ \text{N}"),
            S("Friction up the slope must supply the difference", math=r"F = 24.5 - 19.6 = 4.9\ \text{N}"),
            S("The least $\\mu$ makes this friction limiting, with $R = 5(9.8)\\cos 30^\\circ = 42.44$", math=r"\mu = \frac{4.9}{42.44} = 0.115"),
        ], tolerance=0.002, unit="", concept="Equilibrium with a pulley on a slope", skill="Application", hint="Find the friction needed to keep A at rest, then compare it with $\\mu R$ for the smallest $\\mu$.",
           diagram="apomel2-incline-pulley-q.svg", diagram_alt="A block A of mass 5 kg on a rough slope at 30 degrees joined by a string over a smooth pulley at the top of the slope to a hanging block B of mass 2 kg"),
    ]))

