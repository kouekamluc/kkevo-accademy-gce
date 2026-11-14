"""A Level Pure Mathematics with Mechanics (Upper Sixth): practice sets for momentum, impulse, collisions, work, energy and power.

KKEVO draft material: one set per lesson in lesson_content/a_mech_03_momentum_energy.py. Unless a question says
otherwise, g = 9.8 m/s^2.
"""

from .dsl import *  # noqa: F403

COURSE = [("pure-mathematics-with-mechanics", "upper-sixth")]

MOMENTUM = "Momentum, Impulse & Collisions"
WORK = "Work, Energy & Power"
T_MOM = "Momentum and impulse"
T_COLL = "Collisions and loss of kinetic energy"
T_WORK = "Work and kinetic energy"
T_PE = "Potential energy and conservation of energy"
T_POWER = "Power and moving vehicles"

SETS = []

# ------------------------------------------------------------------ 1 Momentum and impulse
SETS.append(practice_set(
    module=MOMENTUM, topic=T_MOM,
    title="Momentum and impulse: calculations and rebounds", lesson="meu1-momentum-and-impulse",
    questions=[
        MC(r"A lorry of mass $1200$ kg moves at $15$ m/s. What is its momentum?", [
            C(r"$135\,000$ kg m/s", why=r"That is $\tfrac{1}{2}mv^2 = 135\,000$ J, the kinetic energy. Momentum is $mv$."),
            C(r"$18\,000$ kg m/s", correct=True),
            C(r"$80$ kg m/s", why=r"You divided the mass by the speed. Momentum is mass **times** velocity."),
            C(r"$9000$ kg m/s", why=r"You put in a factor $\tfrac{1}{2}$, which belongs to kinetic energy, not to momentum."),
        ], steps=[S("Use the definition", math=r"p = mv"), S("Substitute", math=r"p = 1200 \times 15 = 18\,000 \text{ kg m/s}")],
           concept="Momentum mv", skill="Recall", hint=r"Momentum is mass multiplied by velocity: no powers and no halves.",
           feedback="Momentum is mass times velocity."),
        NUM(r"A constant force of $50$ N acts on a trolley for $0.3$ s. Find the magnitude of its impulse.", 15, tolerance=0.01, unit="N s",
            steps=[S("Impulse of a constant force", math=r"I = Ft"), S("Substitute", math=r"I = 50 \times 0.3 = 15 \text{ N s}")],
            concept="Impulse Ft", skill="Recall", hint=r"Impulse is force multiplied by the time it acts.",
            feedback="Impulse is force times time."),
        NUM(r"A ball of mass $0.3$ kg hits a wall horizontally at $9$ m/s and rebounds along the same line at $6$ m/s. Find the magnitude of the impulse of the wall on the ball.", 4.5, tolerance=0.01, unit="N s",
            steps=[S("Take the rebound direction as positive", math=r"u = -9, \quad v = +6"),
                   S("Change of momentum", math=r"I = 0.3(6) - 0.3(-9) = 1.8 + 2.7 = 4.5 \text{ N s}")],
            concept="Impulse in a rebound", skill="Calculation", hint=r"Give the initial velocity a negative sign, then subtract: final minus initial.",
            feedback="The speeds add because the ball reverses."),
        MC(r"A particle of mass $4$ kg increases its speed from $3$ m/s to $11$ m/s in a straight line in $2$ s under a constant force. What is the force?", [
            C(r"$16$ N", correct=True),
            C(r"$22$ N", why=r"You used only the final momentum $4 \times 11$ and divided by $2$. You must subtract the initial momentum."),
            C(r"$28$ N", why=r"You added the speeds, $3 + 11$. The particle does not reverse, so you subtract: $11 - 3$."),
            C(r"$6$ N", why=r"You used only the initial momentum $4 \times 3$ divided by $2$."),
        ], steps=[S("Impulse-momentum principle", math=r"Ft = mv - mu"), S("Substitute", math=r"F \times 2 = 4(11) - 4(3) = 32"), S("Solve", math=r"F = 16 \text{ N}")],
           concept="Mean force from momentum change", skill="Calculation", hint=r"Write $Ft = mv - mu$ and fill in all four values.",
           feedback="Force times time equals the change of momentum."),
        MC(r"A particle of mass $5$ kg is at rest. A force acts on it with the force-time graph shown (the force rises, stays constant, then falls to zero at $t = 6$ s). What is the speed of the particle at $t = 6$ s?", [
            C(r"$12$ m/s", why=r"You used only the rectangle ($20 \times 3 = 60$ N s) and ignored the two triangles."),
            C(r"$24$ m/s", why=r"You took the peak force times the whole time, $20 \times 6 = 120$ N s. The force is not $20$ N all the time."),
            C(r"$18$ m/s", correct=True),
            C(r"$90$ m/s", why=r"$90$ N s is the impulse. You forgot to divide by the mass $5$ kg."),
        ], steps=[S("Impulse = area under the graph", math=r"\tfrac{1}{2}(1)(20) + (3)(20) + \tfrac{1}{2}(2)(20) = 10 + 60 + 20 = 90 \text{ N s}"),
                  S("Impulse-momentum principle", math=r"90 = 5v - 0"), S("Solve", math=r"v = 18 \text{ m/s}")],
           concept="Impulse as area under F-t graph", skill="Calculation", hint=r"Split the shape into two triangles and a rectangle, and add the areas.",
           feedback="You found the area (the impulse) and divided by the mass.",
           diagram="apomeu1-force-time-q.svg", diagram_alt="Force-time graph: the force rises from 0 to 20 newtons in the first second, stays at 20 newtons until t = 4 seconds, then falls to 0 at t = 6 seconds."),
        NUM(r"A girl of mass $50$ kg jumps from a wall $1.6$ m high and lands on firm ground. She stops in $0.25$ s. Find the mean force the ground exerts on her. (Take $g = 9.8$ m/s$^2$.)", 1610, tolerance=5, unit="N",
            steps=[S("Speed on landing", math=r"v^2 = 2gh = 2(9.8)(1.6) = 31.36 \Rightarrow v = 5.6 \text{ m/s}"),
                   S("Resultant upward force is $R - mg$", math=r"(R - 50 \times 9.8) \times 0.25 = 0 - 50(-5.6) = 280"),
                   S("Solve", math=r"R = 1120 + 490 = 1610 \text{ N}")],
            concept="Impulse with weight included", skill="Application", hint=r"The force acts for a noticeable time, so the weight must appear in the resultant.",
            feedback="You included her weight in the resultant force."),
        MC(r"A ball of mass $0.4$ kg moves east at $5$ m/s. A bat sends it back west at $5$ m/s. Which statement about the impulse of the bat on the ball is correct?", [
            C(r"It is zero, because the speed is the same before and after.", why=r"Speed is the same but velocity is not: the direction reversed, so the momentum changed."),
            C(r"It is $4$ N s towards the west.", correct=True),
            C(r"It is $2$ N s towards the west.", why=r"This is only one of the two momenta ($0.4 \times 5$). You need $2.0 - (-2.0)$, so the change is twice as large."),
            C(r"It is $4$ N s towards the east.", why=r"The size is right but the direction is wrong: the impulse acts in the direction of the **change** of momentum, which is westwards."),
        ], steps=[S("Take west as positive", math=r"u = -5, \quad v = +5"), S("Impulse", math=r"I = 0.4(5) - 0.4(-5) = 4 \text{ N s}"), S("Direction", text="The result is positive, so the impulse is towards the west.")],
           concept="Impulse direction on reversal", skill="Reasoning", hint=r"Compare the **velocities**, not the speeds, and note which direction you call positive.",
           feedback="Impulse equals the change of momentum, which has a direction."),
        MC(r"A particle of mass $3$ kg is at rest on a smooth horizontal surface. A force $F = 6t$ newtons (with $t$ in seconds) acts on it in a fixed direction for $0 \le t \le 2$. What is its speed at $t = 2$?", [
            C(r"$12$ m/s", why=r"$12$ N s is the impulse $\int_0^2 6t\,dt$. You forgot to divide by the mass $3$ kg."),
            C(r"$8$ m/s", why=r"You used the final force $F = 12$ N times $t = 2$, giving $24$ N s. The force grew from $0$, so the impulse is the integral, not force times time."),
            C(r"$1.33$ m/s", why=r"You divided by the mass twice. Dividing impulse by $m$ once gives the velocity."),
            C(r"$4$ m/s", correct=True),
        ], steps=[S("Impulse of a variable force", math=r"I = \int_0^2 6t\,dt = \left[3t^2\right]_0^2 = 12 \text{ N s}"), S("Impulse-momentum principle", math=r"12 = 3v - 0"), S("Solve", math=r"v = 4 \text{ m/s}")],
           concept="Impulse of a variable force by integration", skill="Calculation", hint=r"Integrate $F$ with respect to $t$ over the stated time to find the impulse.",
           feedback="You integrated the force and divided by the mass."),
    ],
))


# ------------------------------------------------------------------ 2 Direct collisions and restitution
SETS.append(practice_set(
    module=MOMENTUM, topic=T_COLL,
    title="Direct collisions and restitution: finding velocities", lesson="meu1-direct-collisions-and-restitution",
    questions=[
        MC(r"Two particles collide directly on a smooth horizontal surface. Which quantity has the same value just before and just after the collision?", [
            C(r"The total kinetic energy of the two particles", why=r"Kinetic energy is lost whenever $e < 1$. Only when $e = 1$ is it unchanged."),
            C(r"The speed of each particle", why=r"The speeds change: that is the whole point of the collision calculation."),
            C(r"The total momentum of the two particles", correct=True),
            C(r"The velocity of each particle", why=r"Each particle's velocity changes. Only the **sum** of the momenta stays fixed."),
        ], steps=[S("Newton's third law", text="The two particles exert equal and opposite impulses on each other."),
                  S("Consequence", text="The momentum gained by one equals the momentum lost by the other, so the total momentum is unchanged.")],
           concept="Conservation of momentum", skill="Concept", hint="Think about the impulses the two particles exert on each other.",
           feedback="Total momentum is conserved when no external impulse acts along the line."),
        NUM(r"A particle of mass $2$ kg moving at $3$ m/s hits a stationary particle of mass $4$ kg. They stick together. Find their common speed.", 1, tolerance=0.01, unit="m/s",
            steps=[S("Coalescing: $e = 0$, so a common velocity", math=r"2(3) + 4(0) = (2 + 4)v"), S("Solve", math=r"6 = 6v \Rightarrow v = 1 \text{ m/s}")],
            concept="Coalescing particles", skill="Calculation", hint=r"After they stick together, the two masses move as one body of mass $2 + 4$.",
            feedback="Momentum before equals momentum of the joined mass."),
        MC(r"Particle $A$ moving at $6$ m/s catches up with particle $B$ moving at $2$ m/s in the same direction. The coefficient of restitution is $0.5$. What is the speed of separation after the collision?", [
            C(r"$2$ m/s", correct=True),
            C(r"$4$ m/s", why=r"$4$ m/s is the speed of **approach** ($6 - 2$). You forgot to multiply by $e$."),
            C(r"$8$ m/s", why=r"You added the speeds $6 + 2$. Here they move the same way, so the approach speed is the **difference**."),
            C(r"$3$ m/s", why=r"You multiplied $e$ by one speed only ($0.5 \times 6$). The law uses the relative speed of the two particles."),
        ], steps=[S("Speed of approach", math=r"u_1 - u_2 = 6 - 2 = 4 \text{ m/s}"), S("Newton's law of restitution", math=r"\text{separation} = 0.5 \times 4 = 2 \text{ m/s}")],
           concept="Newton's law of restitution", skill="Calculation", hint=r"Find the speed of approach first: the particles move in the same direction.",
           feedback="Separation speed is e times approach speed."),
        NUM(r"A ball is dropped from rest from a height of $4.9$ m onto a horizontal floor. The coefficient of restitution is $0.6$. Find its speed just after the first impact. (Take $g = 9.8$ m/s$^2$.)", 5.88, tolerance=0.01, unit="m/s",
            steps=[S("Speed just before impact", math=r"v^2 = 2(9.8)(4.9) = 96.04 \Rightarrow v = 9.8 \text{ m/s}"), S("Restitution with the floor", math=r"0.6 \times 9.8 = 5.88 \text{ m/s}")],
            concept="Bounce on the floor", skill="Application", hint=r"First find the speed just before the ball hits the floor, from the free fall.",
            feedback="You applied e to the speed at impact."),
        MC(r"A particle $A$ of mass $3$ kg moving at $5$ m/s collides directly with a stationary particle $B$ of mass $2$ kg, as in the figure. The coefficient of restitution is $0.4$. What is the speed of $B$ after the collision?", [
            C(r"$2.2$ m/s", why=r"This is the speed of $A$ after the collision, not of $B$."),
            C(r"$3$ m/s", why=r"$3$ m/s would be the common speed if the particles stuck together ($e = 0$). Here they separate."),
            C(r"$7.5$ m/s", why=r"You gave all of $A$'s momentum, $15$, to $B$. But $A$ keeps moving, so the momentum is shared."),
            C(r"$4.2$ m/s", correct=True),
        ], steps=[S("Momentum", math=r"3(5) = 3v_1 + 2v_2 \quad (1)"), S("Restitution", math=r"v_2 - v_1 = 0.4(5 - 0) = 2 \Rightarrow v_1 = v_2 - 2 \quad (2)"),
                  S("Substitute", math=r"3(v_2 - 2) + 2v_2 = 15 \Rightarrow 5v_2 = 21"), S("Solve", math=r"v_2 = 4.2 \text{ m/s} \;(\text{and } v_1 = 2.2 \text{ m/s})")],
           concept="Two equations: momentum and restitution", skill="Calculation", hint=r"Write the momentum equation and the restitution equation, then eliminate $v_1$.",
           feedback="You solved the momentum and restitution equations together.",
           diagram="apomeu1-collision-q.svg", diagram_alt="Before the collision a 3 kg block moves right at 5 metres per second towards a 2 kg block at rest. After the collision both blocks move right with unknown speeds."),
        MC(r"Two particles collide directly with coefficient of restitution $e = 0$. Which statement is correct?", [
            C(r"The particles rebound with the same speeds they had before.", why=r"That describes $e = 1$ (perfectly elastic), not $e = 0$."),
            C(r"The particles move together with the same velocity after the impact.", correct=True),
            C(r"Both particles are at rest after the impact.", why=r"They are at rest only if the total momentum happened to be zero. In general they move together with a common velocity."),
            C(r"Momentum is not conserved in the collision.", why=r"Momentum is conserved for every direct collision on a smooth surface, whatever the value of $e$."),
        ], steps=[S("Speed of separation", math=r"e = 0 \Rightarrow v_2 - v_1 = 0 \Rightarrow v_1 = v_2"), S("Conclusion", text="The particles have the same velocity after impact: they move together.")],
           concept="Meaning of e = 0", skill="Concept", hint=r"Put $e = 0$ into 'speed of separation $= e \times$ speed of approach'.",
           feedback="With e = 0 the speed of separation is zero."),
        NUM(r"Particle $A$ (mass $3$ kg) moves right at $6$ m/s and particle $B$ (mass $2$ kg) moves left at $3$ m/s. After their direct collision $A$ is at rest. Find the coefficient of restitution.", 0.667, tolerance=0.005,
            steps=[S("Positive to the right", math=r"u_1 = 6, \; u_2 = -3, \; v_1 = 0"), S("Momentum", math=r"3(6) + 2(-3) = 2v_2 \Rightarrow v_2 = 6"),
                   S("Restitution", math=r"v_2 - v_1 = e(u_1 - u_2) \Rightarrow 6 = 9e"), S("Solve", math=r"e = \dfrac{2}{3} \approx 0.667")],
            concept="Finding e from the result of a collision", skill="Reasoning", hint=r"Use momentum first to find $v_2$, then restitution to find $e$.",
            feedback="You found B's velocity from momentum, then e from restitution."),
        MC(r"A truck of mass $8000$ kg moving at $4$ m/s runs into a truck of mass $2000$ kg moving in the same direction at $1$ m/s. They couple together. What is the magnitude of the impulse of the first truck on the second?", [
            C(r"$4800$ N s", correct=True),
            C(r"$6800$ N s", why=r"You used only the final momentum of the small truck, $2000 \times 3.4$. Subtract its initial momentum $2000 \times 1$."),
            C(r"$2000$ N s", why=r"This is only the initial momentum of the small truck. The impulse is the **change** of its momentum."),
            C(r"$9600$ N s", why=r"You added the two equal and opposite impulses. They have the same size ($4800$), so there is only one impulse of $4800$ N s."),
        ], steps=[S("Common speed ($e = 0$)", math=r"8000(4) + 2000(1) = 10\,000v \Rightarrow v = 3.4 \text{ m/s}"), S("Impulse on the 2000 kg truck", math=r"I = 2000(3.4 - 1) = 4800 \text{ N s}"),
                  S("Check on the 8000 kg truck", math=r"8000(3.4 - 4) = -4800 \text{ N s}")],
           concept="Impulse in a collision", skill="Application", hint=r"Find the common speed first, then the change of momentum of the smaller truck.",
           feedback="The impulse equals the change of momentum of one truck."),
    ],
))


# ------------------------------------------------------------------ 3 Kinetic energy lost in collisions
SETS.append(practice_set(
    module=MOMENTUM, topic=T_COLL,
    title="Kinetic energy lost in collisions and at walls", lesson="meu1-kinetic-energy-lost-in-collisions",
    questions=[
        MC(r"What is the kinetic energy of a particle of mass $3$ kg moving at $4$ m/s?", [
            C(r"$12$ J", why=r"That is $mv = 12$, the momentum, not the kinetic energy."),
            C(r"$24$ J", correct=True),
            C(r"$48$ J", why=r"You left out the factor $\tfrac{1}{2}$: $mv^2 = 48$."),
            C(r"$144$ J", why=r"You squared the momentum, $(mv)^2 = 144$. Only the speed is squared in $\tfrac{1}{2}mv^2$."),
        ], steps=[S("Definition", math=r"\text{KE} = \tfrac{1}{2}mv^2"), S("Substitute", math=r"\tfrac{1}{2}(3)(4)^2 = 24 \text{ J}")],
           concept="Kinetic energy formula", skill="Recall", hint=r"Square only the speed, then multiply by half the mass.",
           feedback="Kinetic energy is one half of mass times speed squared."),
        NUM(r"A ball of mass $0.5$ kg hits a smooth vertical wall at right angles at $8$ m/s. The coefficient of restitution is $0.5$. Find the kinetic energy lost.", 12, tolerance=0.01, unit="J",
            steps=[S("Rebound speed", math=r"0.5 \times 8 = 4 \text{ m/s}"), S("Energy before and after", math=r"\tfrac{1}{2}(0.5)(8)^2 = 16 \text{ J}, \qquad \tfrac{1}{2}(0.5)(4)^2 = 4 \text{ J}"), S("Energy lost", math=r"16 - 4 = 12 \text{ J}")],
            concept="Energy lost at a wall", skill="Calculation", hint=r"Find the rebound speed first, then the kinetic energy before and after.",
            feedback="You subtracted the kinetic energy after from the kinetic energy before."),
        MC(r"A ball hits a fixed wall at right angles. The coefficient of restitution is $0.8$. What fraction of its kinetic energy is lost?", [
            C(r"$20\%$", why=r"You used $1 - e$. The kinetic energy depends on the square of the speed, so the loss is $1 - e^2$."),
            C(r"$64\%$", why=r"$e^2 = 0.64$ is the fraction of the energy that is **kept**, not the fraction lost."),
            C(r"$80\%$", why=r"This is $e$ itself, which is a ratio of speeds, not of energies."),
            C(r"$36\%$", correct=True),
        ], steps=[S("Speed after is $0.8u$", math=r"\text{KE after} = \tfrac{1}{2}m(0.8u)^2 = 0.64 \times \text{KE before}"), S("Fraction lost", math=r"1 - 0.64 = 0.36 = 36\%")],
           concept="Fraction of energy lost is 1 - e squared", skill="Concept", hint=r"The kinetic energy is proportional to the square of the speed.",
           feedback="Fraction lost is 1 minus e squared."),
        NUM(r"Particle $A$ of mass $3$ kg moves right at $6$ m/s. Particle $B$ of mass $1$ kg moves left at $2$ m/s. They collide directly and $e = 0.5$. Find the kinetic energy lost.", 18, tolerance=0.01, unit="J",
            steps=[S("Momentum (positive to the right)", math=r"3(6) + 1(-2) = 3v_1 + v_2 \Rightarrow 16 = 3v_1 + v_2"), S("Restitution", math=r"v_2 - v_1 = 0.5(6 + 2) = 4"),
                   S("Solve", math=r"4v_1 + 4 = 16 \Rightarrow v_1 = 3, \; v_2 = 7"),
                   S("Energy before and after", math=r"\tfrac{1}{2}(3)(36) + \tfrac{1}{2}(1)(4) = 56 \text{ J}, \quad \tfrac{1}{2}(3)(9) + \tfrac{1}{2}(1)(49) = 38 \text{ J}"), S("Energy lost", math=r"56 - 38 = 18 \text{ J}")],
            concept="Energy lost between two particles", skill="Calculation", hint=r"Find both velocities after the collision first, using momentum and restitution.",
            feedback="You found the energy of both particles before and after."),
        MC(r"A truck of mass $2000$ kg moving at $5$ m/s hits a stationary truck of mass $3000$ kg and they couple together. How much kinetic energy is lost?", [
            C(r"$15\,000$ J", correct=True),
            C(r"$10\,000$ J", why=r"This is the kinetic energy **after** the collision ($\tfrac{1}{2}(5000)(2^2)$), not the energy lost."),
            C(r"$25\,000$ J", why=r"This is the kinetic energy **before** the collision. The energy lost is the difference."),
            C(r"$9000$ J", why=r"You used $\tfrac{1}{2}m(u - v)^2$ for the first truck. That is not a valid energy difference."),
        ], steps=[S("Common speed ($e = 0$)", math=r"2000(5) = 5000v \Rightarrow v = 2 \text{ m/s}"), S("Energy before and after", math=r"\tfrac{1}{2}(2000)(25) = 25\,000 \text{ J}, \qquad \tfrac{1}{2}(5000)(4) = 10\,000 \text{ J}"), S("Energy lost", math=r"25\,000 - 10\,000 = 15\,000 \text{ J}")],
           concept="Energy lost when particles coalesce", skill="Calculation", hint=r"Find the common speed from conservation of momentum, then compare the kinetic energies.",
           feedback="You subtracted the kinetic energy after from the kinetic energy before."),
        MC(r"A ball bounces off a horizontal floor and loses $51\%$ of its kinetic energy in the impact. What is the coefficient of restitution between the ball and the floor?", [
            C(r"$0.49$", why=r"$0.49$ is the fraction of energy that is **kept**, $e^2$. You need its square root."),
            C(r"$0.51$", why=r"You took the fraction of energy lost as $e$. The coefficient relates the speeds, not the energies."),
            C(r"$0.7$", correct=True),
            C(r"$0.3$", why=r"$0.3$ is the fraction of the **speed** that is lost ($1 - e$ with $e = 0.7$). The question asks for $e$ itself."),
        ], steps=[S("Fraction kept", math=r"e^2 = 1 - 0.51 = 0.49"), S("Take the square root", math=r"e = 0.7")],
           concept="Finding e from the energy lost", skill="Reasoning", hint=r"What fraction of the energy is kept? How is it related to $e$?",
           feedback="The fraction kept is e squared."),
        NUM(r"A particle $A$ collides directly with a stationary particle $B$ of the same mass. Afterwards $18\%$ of the original kinetic energy has been lost. Find the coefficient of restitution.", 0.8, tolerance=0.005,
            steps=[S("Speeds after (equal masses, $B$ at rest)", math=r"x = \tfrac{1}{2}(1 - e)u, \qquad y = \tfrac{1}{2}(1 + e)u"), S("Fraction of the energy kept", math=r"\dfrac{x^2 + y^2}{u^2} = \tfrac{1}{2}(1 + e^2)"),
                   S("Set equal to $0.82$", math=r"\tfrac{1}{2}(1 + e^2) = 0.82 \Rightarrow e^2 = 0.64"), S("Solve", math=r"e = 0.8")],
            concept="Finding e for equal masses", skill="Reasoning", hint=r"Momentum gives $x + y = u$ and restitution gives $y - x = eu$. Then compare $x^2 + y^2$ with $u^2$.",
            feedback="You compared the kinetic energy after with the kinetic energy before."),
        MC(r"A ball is dropped from a height of $2$ m onto a horizontal floor. The coefficient of restitution is $0.5$. To what height does it rise after the **second** bounce?", [
            C(r"$0.5$ m", why=r"$0.5$ m is the height after the **first** bounce ($e^2 \times 2$)."),
            C(r"$0.125$ m", correct=True),
            C(r"$1$ m", why=r"You multiplied the height by $e$ once. The height changes by the factor $e^2$ at each bounce."),
            C(r"$0.25$ m", why=r"You applied $e$ (not $e^2$) at the second bounce: $0.5 \times 0.5$. Each bounce multiplies the height by $e^2 = 0.25$."),
        ], steps=[S("Each bounce multiplies the height by $e^2$", math=r"e^2 = 0.25"), S("After two bounces", math=r"h = 2 \times 0.25^2 = 2 \times 0.0625 = 0.125 \text{ m}")],
           concept="Height after repeated bounces", skill="Application", hint=r"After each bounce the height is multiplied by $e^2$.",
           feedback="The height is multiplied by e squared at each bounce."),
    ],
))


# ------------------------------------------------------------------ 4 Work and kinetic energy
SETS.append(practice_set(
    module=WORK, topic=T_WORK,
    title="Work done by forces and the work-energy principle", lesson="meu1-work-done-and-kinetic-energy",
    questions=[
        MC(r"A force of $40$ N acts at $60^\circ$ above the horizontal on a box which moves $15$ m along a horizontal floor. What is the work done by the force?", [
            C(r"$600$ J", why=r"You used $Fs$ and ignored the angle. Only the component of the force along the motion does work."),
            C(r"$520$ J", why=r"You used $\cos 30^\circ$. The angle in the formula is between the force and the **motion**, which is $60^\circ$."),
            C(r"$300$ J", correct=True),
            C(r"$1200$ J", why=r"You divided by $\cos 60^\circ$ instead of multiplying."),
        ], steps=[S("Work done by a constant force", math=r"W = Fs\cos\theta"), S("Substitute", math=r"W = 40 \times 15 \times \cos 60^\circ = 40 \times 15 \times 0.5 = 300 \text{ J}")],
           concept="Work done Fs cos theta", skill="Calculation", hint=r"Identify the angle between the force and the direction of motion.",
           feedback="You multiplied by the cosine of the angle between force and motion."),
        NUM(r"Find the kinetic energy of a car of mass $1500$ kg travelling at $20$ m/s, in joules.", 300000, tolerance=1, unit="J",
            steps=[S("Definition", math=r"\text{KE} = \tfrac{1}{2}mv^2"), S("Substitute", math=r"\tfrac{1}{2}(1500)(20)^2 = 300\,000 \text{ J}")],
            concept="Kinetic energy", skill="Recall", hint=r"Square the speed first, then multiply by half the mass.",
            feedback="Kinetic energy is half of mass times speed squared."),
        MC(r"A porter carries a sack of mass $20$ kg along a level road for $30$ m at a constant speed. What is the work done by the porter's upward force on the sack? (Take $g = 9.8$ m/s$^2$.)", [
            C(r"$0$ J", correct=True),
            C(r"$5880$ J", why=r"You calculated $mgs$. The upward force is perpendicular to the horizontal motion, so $\cos 90^\circ = 0$."),
            C(r"$600$ J", why=r"You multiplied the mass by the distance ($20 \times 30$), so no force was used. Work needs a force and the angle between it and the motion."),
            C(r"$196$ J", why=r"$196$ N is the weight of the sack, which is a force, not a work. A vertical force on a horizontal movement does zero work."),
        ], steps=[S("Angle between force and motion", text=r"The porter's force is upward; the sack moves horizontally. So $\theta = 90^\circ$."), S("Work done", math=r"W = Fs\cos 90^\circ = 0")],
           concept="A perpendicular force does no work", skill="Concept", hint=r"What is the angle between an upward force and a horizontal displacement?",
           feedback="A force perpendicular to the motion does no work."),
        NUM(r"A car of mass $800$ kg moving at $15$ m/s brakes to rest. The braking force is a constant $3000$ N. How far does the car travel while braking?", 30, tolerance=0.1, unit="m",
            steps=[S("Work-energy principle", math=r"-3000s = 0 - \tfrac{1}{2}(800)(15)^2 = -90\,000"), S("Solve", math=r"s = \dfrac{90\,000}{3000} = 30 \text{ m}")],
            concept="Stopping distance by work-energy", skill="Application", hint=r"The work done by the braking force equals the change in kinetic energy.",
            feedback="You equated the work done by the brakes to the kinetic energy lost."),
        MC(r"A car of mass $1500$ kg slows from $24$ m/s to $10$ m/s. What is the total work done on it by the braking and resistance forces?", [
            C(r"$-147\,000$ J", why=r"You used $\tfrac{1}{2}m(v - u)^2$. The change of kinetic energy needs $v^2 - u^2$, not the square of the difference."),
            C(r"$-432\,000$ J", why=r"This is only the initial kinetic energy. The car still has kinetic energy at $10$ m/s."),
            C(r"$-75\,000$ J", why=r"This is only the final kinetic energy. You must subtract it from the initial value."),
            C(r"$-357\,000$ J", correct=True),
        ], steps=[S("Kinetic energies", math=r"\tfrac{1}{2}(1500)(10)^2 = 75\,000 \text{ J}, \qquad \tfrac{1}{2}(1500)(24)^2 = 432\,000 \text{ J}"), S("Work done = change", math=r"75\,000 - 432\,000 = -357\,000 \text{ J}")],
           concept="Work done equals change of kinetic energy", skill="Calculation", hint=r"Work done by the resultant force = final kinetic energy minus initial kinetic energy.",
           feedback="The work done is negative because the car loses kinetic energy."),
        MC(r"A block of mass $4$ kg is projected up a rough slope inclined at $30^\circ$ to the horizontal with speed $6$ m/s. The friction force is a constant $8$ N. How far up the slope does the block travel before stopping? (Take $g = 9.8$ m/s$^2$.)", [
            C(r"$3.67$ m", why=r"You ignored friction. The friction force also does negative work."),
            C(r"$2.61$ m", correct=True),
            C(r"$1.53$ m", why=r"You used the whole weight $mg$ instead of its component $mg\sin 30^\circ$ along the slope."),
            C(r"$9.0$ m", why=r"You included only friction and forgot the work done against the weight."),
        ], steps=[S("Initial kinetic energy", math=r"\tfrac{1}{2}(4)(6)^2 = 72 \text{ J}"), S("Work against weight and friction over a distance $d$", math=r"4(9.8)(\sin 30^\circ)d + 8d = 27.6d"),
                  S("Work-energy principle", math=r"-27.6d = 0 - 72"), S("Solve", math=r"d = 2.61 \text{ m}")],
           concept="Work-energy on a rough slope", skill="Application", hint=r"List the forces that do work along the slope: the weight component and friction.",
           feedback="You included both the weight component and friction."),
        NUM(r"A particle of mass $4$ kg moves on a smooth horizontal line. When it is at $x = 0$ its speed is $1$ m/s. A force $F = 3x^2$ newtons acts along the line. Find its speed at $x = 2$, in m/s to 3 significant figures.", 2.24, tolerance=0.01, unit="m/s",
            steps=[S("Work done by the force", math=r"\int_0^2 3x^2\,dx = \left[x^3\right]_0^2 = 8 \text{ J}"), S("Initial kinetic energy", math=r"\tfrac{1}{2}(4)(1)^2 = 2 \text{ J}"),
                   S("Work-energy principle", math=r"8 = \tfrac{1}{2}(4)v^2 - 2 \Rightarrow 2v^2 = 10"), S("Solve", math=r"v^2 = 5 \Rightarrow v = 2.24 \text{ m/s}")],
            concept="Work done by a variable force", skill="Calculation", hint=r"The work done is the integral of the force with respect to distance.",
            feedback="You integrated the force to get the work, then used the work-energy principle."),
        MC(r"A car brakes to rest on a straight level road. Which statement about the work done by the braking force is correct?", [
            C(r"It is positive, because the force acts on the car.", why=r"The braking force acts **against** the motion ($\theta = 180^\circ$), so its work is negative."),
            C(r"It is zero, because the car ends at rest.", why=r"The kinetic energy at the end is zero, but the force acts through a distance, so it does work. The work equals the **change** of kinetic energy."),
            C(r"It is negative and equal in size to the initial kinetic energy.", correct=True),
            C(r"It cannot be found without the braking force and the distance.", why=r"The work-energy principle gives it directly: $0 - \tfrac{1}{2}mu^2$, without the force or the distance."),
        ], steps=[S("Work-energy principle", math=r"W = \tfrac{1}{2}mv^2 - \tfrac{1}{2}mu^2 = 0 - \tfrac{1}{2}mu^2"), S("Conclusion", text="The work is negative and its size equals the initial kinetic energy.")],
           concept="Sign of the work done by a braking force", skill="Reasoning", hint=r"What is the final kinetic energy of a car that comes to rest?",
           feedback="The work done is minus the initial kinetic energy."),
    ],
))


# ------------------------------------------------------------------ 5 Potential energy and conservation of energy
SETS.append(practice_set(
    module=WORK, topic=T_PE,
    title="Potential energy and conservation of energy: heights and speeds", lesson="meu1-potential-energy-and-conservation-of-energy",
    questions=[
        MC(r"A sack of mass $12$ kg is $3$ m above the ground. Taking the ground as the reference level, what is its gravitational potential energy? (Take $g = 9.8$ m/s$^2$.)", [
            C(r"$36$ J", why=r"You multiplied mass by height and left out $g$."),
            C(r"$117.6$ J", why=r"This is the weight $mg$ in newtons. You did not multiply by the height."),
            C(r"$176.4$ J", why=r"You included a factor $\tfrac{1}{2}$, which belongs to kinetic energy, not to potential energy."),
            C(r"$352.8$ J", correct=True),
        ], steps=[S("Definition", math=r"\text{PE} = mgh"), S("Substitute", math=r"12 \times 9.8 \times 3 = 352.8 \text{ J}")],
           concept="Gravitational potential energy mgh", skill="Recall", hint=r"Multiply the mass, $g$ and the height.",
           feedback="Potential energy is mass times g times height."),
        NUM(r"A stone is dropped from rest from a point $10$ m above the ground. Find its speed on reaching the ground. Ignore air resistance. (Take $g = 9.8$ m/s$^2$.)", 14, tolerance=0.05, unit="m/s",
            steps=[S("Conservation of energy", math=r"mg(10) = \tfrac{1}{2}mv^2"), S("Solve", math=r"v^2 = 2(9.8)(10) = 196 \Rightarrow v = 14 \text{ m/s}")],
            concept="Speed from a fall by energy", skill="Calculation", hint=r"Equate the potential energy lost with the kinetic energy gained and cancel the mass.",
            feedback="The mass cancels in the energy equation."),
        MC(r"A ball is thrown vertically upwards from the ground at $21$ m/s. Ignoring air resistance, what is the greatest height it reaches? (Take $g = 9.8$ m/s$^2$.)", [
            C(r"$22.5$ m", correct=True),
            C(r"$45$ m", why=r"You used $h = v^2/g$ and left out the factor $2$ that comes from the $\tfrac{1}{2}$ in the kinetic energy."),
            C(r"$10.5$ m", why=r"You halved the speed instead of using $h = v^2/(2g)$."),
            C(r"$21$ m", why=r"You gave the initial speed as the height. The units do not match: height needs $v^2$ divided by $g$."),
        ], steps=[S("Energy: all the kinetic energy becomes potential energy", math=r"\tfrac{1}{2}m(21)^2 = mgh"), S("Solve", math=r"h = \dfrac{441}{2 \times 9.8} = 22.5 \text{ m}")],
           concept="Greatest height by conservation of energy", skill="Calculation", hint=r"At the top the speed is zero, so all the kinetic energy has become potential energy.",
           feedback="You equated the initial KE to the PE at the top."),
        MC(r"A particle is released from rest at the top of a smooth curved track, a vertical height of $3.6$ m above the bottom (see the figure). What is its speed at the bottom? (Take $g = 9.8$ m/s$^2$.)", [
            C(r"$5.94$ m/s", why=r"You used $v^2 = gh$ and forgot the factor $2$."),
            C(r"$8.4$ m/s", correct=True),
            C(r"$70.56$ m/s", why=r"$70.56$ is $v^2$. You did not take the square root."),
            C(r"$35.3$ m/s", why=r"$35.3$ is $gh$. You did not double it or take the square root."),
        ], steps=[S("The normal reaction does no work, so energy is conserved", math=r"mgh = \tfrac{1}{2}mv^2"), S("Solve", math=r"v^2 = 2(9.8)(3.6) = 70.56 \Rightarrow v = 8.4 \text{ m/s}")],
           concept="Speed at the bottom of a smooth track", skill="Calculation", hint=r"Equate $mgh$ and $\tfrac{1}{2}mv^2$. The shape of the track does not matter.",
           feedback="Only the vertical drop matters on a smooth track.",
           diagram="apomeu1-smooth-slide-q.svg", diagram_alt="A smooth curved track. A particle starts at rest at A, a height h above the lowest level, and slides down to the level part of the track at B."),
        NUM(r"A cyclist and bicycle of total mass $90$ kg descend a hill. The vertical drop is $12$ m. The speed at the top is $4$ m/s and at the bottom is $14$ m/s. Find the work done against resistances, in joules. (Take $g = 9.8$ m/s$^2$.)", 2484, tolerance=1, unit="J",
            steps=[S("Potential energy lost", math=r"mgh = 90 \times 9.8 \times 12 = 10\,584 \text{ J}"), S("Kinetic energy gained", math=r"\tfrac{1}{2}(90)(14^2 - 4^2) = 45 \times 180 = 8100 \text{ J}"),
                   S("Energy equation: PE lost = KE gained + work against resistances", math=r"10\,584 = 8100 + W \Rightarrow W = 2484 \text{ J}")],
            concept="Work against resistance by energy", skill="Application", hint=r"Compare the potential energy lost with the kinetic energy gained. What is the difference?",
            feedback="The missing energy was lost to resistances."),
        MC(r"A bob hangs from a light string of length $2.5$ m. It is released from rest with the string horizontal. What is its speed at the lowest point of the swing? (Take $g = 9.8$ m/s$^2$.)", [
            C(r"$4.95$ m/s", why=r"You used $v^2 = gL$ and forgot the factor $2$."),
            C(r"$49$ m/s", why=r"$49$ is $v^2$. You did not take the square root."),
            C(r"$7.0$ m/s", correct=True),
            C(r"$0$ m/s", why=r"You used $L(1 - \sin 90^\circ) = 0$ for the drop. The height lost from the horizontal position to the lowest point is $L(1 - \cos 90^\circ) = L$."),
        ], steps=[S("Vertical drop from horizontal to lowest point", math=r"h = L = 2.5 \text{ m}"), S("Tension does no work: conserve energy", math=r"mgL = \tfrac{1}{2}mv^2 \Rightarrow v^2 = 2(9.8)(2.5) = 49"), S("Solve", math=r"v = 7.0 \text{ m/s}")],
           concept="Pendulum by conservation of energy", skill="Application", hint=r"How far below its starting point is the lowest point of the swing?",
           feedback="The vertical drop equals the string length."),
        NUM(r"A crate of mass $20$ kg is released from rest at the top of a rough slope $8$ m long. The slope has $\sin\alpha = 0.6$ and the coefficient of friction is $0.25$. Find the speed of the crate at the bottom. (Take $g = 9.8$ m/s$^2$.)", 7.92, tolerance=0.02, unit="m/s",
            steps=[S("Vertical drop and normal reaction", math=r"h = 8(0.6) = 4.8 \text{ m}, \quad R = 20(9.8)(0.8) = 156.8 \text{ N}"),
                   S("PE lost and work against friction", math=r"20(9.8)(4.8) = 940.8 \text{ J}, \qquad (0.25 \times 156.8) \times 8 = 313.6 \text{ J}"),
                   S("Energy equation", math=r"940.8 = \tfrac{1}{2}(20)v^2 + 313.6 \Rightarrow 10v^2 = 627.2"), S("Solve", math=r"v^2 = 62.72 \Rightarrow v = 7.92 \text{ m/s}")],
            concept="Energy with friction on a slope", skill="Application", hint=r"PE lost = KE gained + work against friction. Find $R$ first.",
            feedback="You subtracted the work done against friction."),
        MC(r"Particles of mass $5$ kg and $3$ kg are joined by a light inextensible string over a smooth fixed pulley and hang vertically. They are released from rest. What is their speed after the heavier particle has fallen $2$ m? (Take $g = 9.8$ m/s$^2$.)", [
            C(r"$6.26$ m/s", why=r"You treated the heavier particle as falling freely ($v^2 = 2gs$). The string and the other particle slow it down."),
            C(r"$3.96$ m/s", why=r"You gave kinetic energy to the $5$ kg particle only. Both particles move at the same speed, so both have kinetic energy."),
            C(r"$2.21$ m/s", why=r"You left out the factor $\tfrac{1}{2}$ in the kinetic energy of the system."),
            C(r"$3.13$ m/s", correct=True),
        ], steps=[S("Net loss of potential energy", math=r"5(9.8)(2) - 3(9.8)(2) = 39.2 \text{ J}"), S("Gain of kinetic energy of both particles", math=r"\tfrac{1}{2}(5 + 3)v^2 = 4v^2"),
                  S("Energy equation", math=r"4v^2 = 39.2 \Rightarrow v^2 = 9.8"), S("Solve", math=r"v = 3.13 \text{ m/s}")],
           concept="Energy for connected particles", skill="Application", hint=r"The $5$ kg particle falls and the $3$ kg particle rises. Count the kinetic energy of both.",
           feedback="You included both particles in the energy equation."),
    ],
))


# ------------------------------------------------------------------ 6 Power and moving vehicles
SETS.append(practice_set(
    module=WORK, topic=T_POWER,
    title="Power and moving vehicles: driving force, resistance and speed", lesson="meu1-power-and-moving-vehicles",
    questions=[
        MC(r"Which of these is the unit of power?", [
            C(r"The watt, $\text{W} = \text{J/s}$", correct=True),
            C(r"The joule, $\text{J} = \text{N m}$", why=r"The joule is the unit of work and energy, not of the **rate** of working."),
            C(r"The newton second, $\text{N s}$", why=r"$\text{N s}$ is the unit of impulse (and of momentum)."),
            C(r"$\text{kg m/s}$", why=r"$\text{kg m/s}$ is the unit of momentum."),
        ], steps=[S("Definition", math=r"P = \dfrac{W}{t}"), S("Units", math=r"\text{J/s} = \text{W (watt)}")],
           concept="Unit of power", skill="Recall", hint=r"Power is work divided by time.",
           feedback="Power is measured in watts, one joule per second."),
        NUM(r"A crane lifts a load of mass $300$ kg vertically at a constant speed of $0.6$ m/s. Find the power it develops, in watts. (Take $g = 9.8$ m/s$^2$.)", 1764, tolerance=1, unit="W",
            steps=[S("Steady speed: lifting force = weight", math=r"F = 300 \times 9.8 = 2940 \text{ N}"), S("Power", math=r"P = Fv = 2940 \times 0.6 = 1764 \text{ W}")],
            concept="Power P = Fv for a lift", skill="Calculation", hint=r"At a steady speed the lifting force equals the weight.",
            feedback="You used power equals force times speed."),
        MC(r"A car engine works at $45$ kW while the car travels at $15$ m/s. What is the driving force?", [
            C(r"$3$ N", why=r"You divided $45$ by $15$ without converting $45$ kW to $45\,000$ W."),
            C(r"$675\,000$ N", why=r"You multiplied power by speed. Force $= P/v$, so divide."),
            C(r"$3000$ N", correct=True),
            C(r"$0.00033$ N", why=r"You divided the speed by the power. Force is power **divided by** speed."),
        ], steps=[S("Convert to watts", math=r"45 \text{ kW} = 45\,000 \text{ W}"), S("Use $P = Fv$", math=r"F = \dfrac{45\,000}{15} = 3000 \text{ N}")],
           concept="Driving force F = P/v", skill="Calculation", hint=r"Convert kW to W first, then divide by the speed in m/s.",
           feedback="Driving force is power divided by speed."),
        NUM(r"A car has an engine of power $45$ kW and a constant resistance to motion of $900$ N. Find its maximum speed on a level road.", 50, tolerance=0.1, unit="m/s",
            steps=[S("At maximum speed the acceleration is zero", math=r"F = R = 900 \text{ N}"), S("Use $P = Fv$", math=r"v = \dfrac{45\,000}{900} = 50 \text{ m/s}")],
            concept="Maximum speed on level ground", skill="Calculation", hint=r"At maximum speed the driving force equals the resistance.",
            feedback="At maximum speed the driving force equals the resistance."),
        MC(r"A lorry of mass $5000$ kg climbs a straight hill with $\sin\alpha = \dfrac{1}{10}$ at a steady $36$ km/h. The resistance to motion is $1500$ N. What power is the engine developing? (Take $g = 9.8$ m/s$^2$.)", [
            C(r"$15$ kW", why=r"You included only the resistance, $1500 \times 10$. The driving force must also overcome the weight component $mg\sin\alpha$."),
            C(r"$49$ kW", why=r"You included only the weight component ($4900$ N) and forgot the resistance."),
            C(r"$230.4$ kW", why=r"You used $36$ as the speed in m/s. First convert $36$ km/h to $10$ m/s."),
            C(r"$64$ kW", correct=True),
        ], steps=[S("Convert the speed", math=r"36 \text{ km/h} = 10 \text{ m/s}"), S("Steady speed: $a = 0$", math=r"F = 1500 + 5000(9.8)\tfrac{1}{10} = 1500 + 4900 = 6400 \text{ N}"), S("Power", math=r"P = Fv = 6400 \times 10 = 64\,000 \text{ W} = 64 \text{ kW}")],
           concept="Power needed on a hill", skill="Application", hint=r"List everything the driving force must overcome up the slope, and convert the speed to m/s.",
           feedback="The driving force overcomes the resistance and the weight component."),
        MC(r"A car of mass $1000$ kg moves at a steady $20$ m/s on a level road, with the engine working at $24$ kW. The engine power is suddenly reduced to $18$ kW. What is the car's deceleration immediately afterwards?", [
            C(r"$0.9$ m/s$^2$", why=r"You divided the new driving force ($900$ N) by the mass and forgot the resistance $1200$ N that still acts."),
            C(r"$0.3$ m/s$^2$", correct=True),
            C(r"$6.0$ m/s$^2$", why=r"You treated the drop in power ($6000$ W) as a force. Power must first be divided by the speed."),
            C(r"$0$ m/s$^2$", why=r"The **speed** cannot change instantly, but the driving force $P/v$ does, so the acceleration changes at once."),
        ], steps=[S("Steady speed before: $F = R$", math=r"R = \dfrac{24\,000}{20} = 1200 \text{ N}"), S("Driving force just after the change", math=r"F = \dfrac{18\,000}{20} = 900 \text{ N}"),
                  S("Newton's second law", math=r"900 - 1200 = 1000a \Rightarrow a = -0.3"), S("Conclusion", text=r"The deceleration is $0.3$ m/s$^2$.")],
           concept="Change of engine power", skill="Application", hint=r"Find the resistance from the steady speed, then the new driving force at the same speed.",
           feedback="You used the new driving force and the unchanged resistance."),
        NUM(r"A car of mass $1000$ kg has an engine of power $24$ kW and a maximum speed of $40$ m/s on a level road. Assuming a constant resistance, find its acceleration when its speed is $30$ m/s on the level, in m/s$^2$.", 0.2, tolerance=0.005, unit="m/s$^2$",
            steps=[S("Resistance from the maximum speed", math=r"R = \dfrac{24\,000}{40} = 600 \text{ N}"), S("Driving force at $30$ m/s", math=r"F = \dfrac{24\,000}{30} = 800 \text{ N}"), S("Newton's second law", math=r"800 - 600 = 1000a \Rightarrow a = 0.2 \text{ m/s}^2")],
            concept="Acceleration at a given speed", skill="Calculation", hint=r"The maximum speed tells you the resistance: at that speed $F = R$.",
            feedback="You found R first, then the acceleration."),
        MC(r"A car's engine works at a constant power on a level road and the resistance is constant. Starting from a low speed, which statement describes the car's acceleration?", [
            C(r"It is constant, because the power is constant.", why=r"Constant **power** does not mean constant force. $F = P/v$ falls as $v$ rises."),
            C(r"It increases, because the car has more kinetic energy.", why=r"Kinetic energy does not push the car forward. The driving force falls with speed, so the acceleration falls."),
            C(r"It decreases and becomes zero when $F = R$.", correct=True),
            C(r"It is zero from the start.", why=r"At low speed $F = P/v$ is large and exceeds $R$, so the acceleration is large and positive."),
        ], steps=[S("Driving force", math=r"F = \dfrac{P}{v}"), S("Resultant force", math=r"F - R = \dfrac{P}{v} - R \text{ decreases as } v \text{ increases}"), S("Conclusion", text="The acceleration decreases until $F = R$, where it is zero at the maximum speed.")],
           concept="Constant power and acceleration", skill="Reasoning", hint=r"How does $F = P/v$ change as $v$ grows?",
           feedback="The driving force falls as the speed rises."),
    ],
))
