# FC4A: Translational Motion, Forces, Work, Energy, Equilibrium

**Section:** Chem/Phys (CP)
**Yield:** HIGH -- expect 5-8 questions per exam touching these concepts
**Kaplan Reference:** Physics Ch. 1-4

---

## 1. Kinematics

Kinematics describes *how* objects move without caring *why* they move. You are tracking position, velocity, and acceleration over time.

### Key Definitions

- **Displacement** (delta x): vector quantity -- how far you end up from where you started, with direction. If you walk 3 m east then 3 m west, displacement = 0.
- **Distance**: scalar -- total path length traveled. Same walk = 6 m.
- **Velocity**: vector, rate of change of displacement. v = delta x / delta t.
- **Speed**: scalar, rate of change of distance. Always positive.
- **Acceleration**: vector, rate of change of velocity. a = delta v / delta t. On the MCAT, acceleration almost always means *constant* acceleration (gravity, uniform electric fields, etc.).

**MCAT trap:** A question says "the car travels at constant speed around a curve." Students pick "acceleration = 0" because speed is constant. Wrong. Direction is changing, so velocity is changing, so there IS acceleration (centripetal).

### The Big 5 Kinematic Equations

These only work for **constant acceleration**. Each equation is missing one variable. The trick on the MCAT is to figure out which variable you don't know and don't need, then pick the equation that leaves it out.

| Equation | Missing Variable |
|----------|-----------------|
| v = v_0 + at | delta x |
| delta x = v_0 t + 1/2 a t^2 | v (final) |
| delta x = vt - 1/2 a t^2 | v_0 (initial) |
| v^2 = v_0^2 + 2a(delta x) | t |
| delta x = 1/2 (v_0 + v) t | a |

**Problem-solving strategy:**
1. List what you know: v_0, v, a, t, delta x.
2. Identify what you want.
3. You'll know three variables and want a fourth. The fifth is irrelevant. Pick the equation missing the irrelevant one.

**When you see "how far does it travel before stopping"** -- that means v_final = 0, and you probably want delta x. You likely don't care about time. Use **v^2 = v_0^2 + 2a(delta x)**.

**When you see "how long does it take to reach..."** -- you want t, and you probably know v_0, v, and a. Use **v = v_0 + at**.

### Free Fall

Free fall = the only acceleration is gravity. a = g = 9.8 m/s^2 downward (use 10 m/s^2 on the MCAT for estimation).

- Object dropped from rest: v_0 = 0, a = -g (taking up as positive).
- Object thrown upward: at the peak, v = 0 (momentarily). Time up = time down (for same height). Speed at launch = speed at landing.

**Quick estimation:** An object in free fall for 2 seconds drops about 1/2 (10)(4) = 20 m and reaches a speed of about 20 m/s.

### Projectile Motion

The key insight: **horizontal and vertical motions are completely independent.** The only thing they share is time.

- Horizontal: a_x = 0 (no air resistance on MCAT unless stated). So x = v_0x * t.
- Vertical: a_y = -g. Use the Big 5 with a = -g.

**Decomposing initial velocity:**
- v_0x = v_0 cos(theta)
- v_0y = v_0 sin(theta)

**Solving projectile problems:**
1. Break v_0 into components.
2. Use vertical equations to find time (often set y = 0 for landing, or v_y = 0 for max height).
3. Plug that time into the horizontal equation to get range.

**MCAT facts to just know:**
- Max range occurs at 45 degrees (if launching and landing at same height).
- Complementary angles (e.g., 30 and 60 degrees) give the same range.
- At the top of the arc, v_y = 0 but v_x is still there -- the object is NOT at rest at the top (unless launched straight up).

**Estimation tip:** sin(30) = 0.5, cos(30) ~ 0.87, sin(45) = cos(45) ~ 0.7, sin(60) ~ 0.87, cos(60) = 0.5. Memorize these -- they show up constantly.

---

## 2. Newton's Laws of Motion

### First Law (Inertia)

An object at rest stays at rest, and an object in motion stays in motion at constant velocity, unless acted on by a net external force. **Mass is the measure of inertia** -- more mass means harder to accelerate.

MCAT relevance: this law explains why you need a seatbelt (your body wants to keep moving when the car stops), and why objects in space drift forever.

### Second Law (F = ma)

**This is the workhorse equation of mechanics.** The net force on an object equals its mass times its acceleration.

Critical point: **F means the NET force -- the vector sum of ALL forces on the object.** If two forces cancel, net force = 0, and a = 0 (constant velocity, not necessarily at rest).

**Problem-solving with F = ma:**
1. Draw a free body diagram (FBD).
2. Choose a coordinate system (usually: x along motion, y perpendicular).
3. Sum forces in each direction.
4. Set sum(F_x) = ma_x and sum(F_y) = ma_y.
5. Solve for unknowns.

### Third Law (Action-Reaction)

For every action, there is an equal and opposite reaction. **The forces act on DIFFERENT objects.** This is where students mess up.

Example: You push a wall with 50 N. The wall pushes you back with 50 N. But these forces are on different objects, so they don't cancel. They'd only cancel if they were both on the same object.

**MCAT application:** When a small car hits a large truck, the forces on each are equal in magnitude. The car accelerates more because it has less mass (F = ma, same F, smaller m means bigger a). This is why the small car gets wrecked.

### Free Body Diagrams

**Every mechanics problem on the MCAT starts here.** Even if you don't draw it on paper, think through it.

Forces to consider for any object:
- **Weight (mg)**: always straight down, from center of mass.
- **Normal force (N or F_N)**: perpendicular to the surface of contact. NOT always equal to mg.
- **Friction (f)**: parallel to the surface, opposing motion (or tendency of motion).
- **Tension (T)**: along a rope/string, pulling away from the object.
- **Applied force (F_app)**: whatever external push/pull is described.
- **Air resistance**: usually ignored on MCAT unless stated.

### Friction

**Static friction (f_s):** Acts when the object is NOT sliding. It matches the applied force up to a maximum. f_s is less than or equal to mu_s * N. It's variable -- it's only at maximum right before the object starts to slide.

**Kinetic friction (f_k):** Acts when the object IS sliding. f_k = mu_k * N. This is a fixed value (for a given normal force).

**Key relationship:** mu_s > mu_k always. It takes more force to START something sliding than to KEEP it sliding. This is why it's harder to push a heavy box from rest than to keep it moving.

**MCAT trap:** A question asks for the friction force on a stationary object with a small applied force. Students calculate mu_s * N and use that. Wrong -- that's the MAXIMUM static friction. The actual friction force equals the applied force (since the object isn't moving, net force = 0).

### Inclined Planes

**When you see an inclined plane, immediately decompose forces along the plane.**

Set your axes: x-axis along the plane surface (positive pointing up the incline), y-axis perpendicular to the plane surface (positive pointing away from the surface).

Weight decomposition:
- **Component parallel to incline (pulling object down the slope):** mg sin(theta)
- **Component perpendicular to incline (pushing object into surface):** mg cos(theta)

Normal force: N = mg cos(theta) (assuming no other forces in the perpendicular direction).

Friction on an incline: f = mu * N = mu * mg cos(theta).

**How to remember which is sin and which is cos:** At theta = 0 (flat surface), there should be no component along the surface and full weight into the surface. sin(0) = 0 and cos(0) = 1, which checks out. Parallel = sin, perpendicular = cos.

**For an object sliding down a frictionless incline:** a = g sin(theta). This is a must-know result. At theta = 30 degrees, a = g/2 = 5 m/s^2. At theta = 90 degrees (vertical), a = g. Makes sense.

### Circular Motion

Any object moving in a circle at constant speed has **centripetal acceleration** directed toward the center of the circle.

- a_c = v^2 / r
- F_c = mv^2 / r (this is the NET force toward the center, not a new kind of force)

**Centripetal force is not a separate force.** It's whatever force (or combination of forces) points toward the center. For a ball on a string, it's tension. For a car turning on a road, it's friction. For a planet orbiting the sun, it's gravity. For an electron orbiting a nucleus, it's the electrostatic force.

**MCAT problem pattern:** "What is the minimum speed to maintain contact at the top of a loop?" At the top of the loop, gravity points toward the center. Normal force also points toward the center (if there's still contact). At the minimum speed, N = 0, so mg = mv^2/r, giving v = sqrt(g*r).

---

## 3. Work and Energy

### Work

**W = Fd cos(theta)**

Where theta is the angle between the force vector and the displacement vector.

- **Positive work** (theta < 90 degrees): Force has a component in the direction of motion. The force speeds the object up or pushes it along. Example: pushing a box forward.
- **Negative work** (theta > 90 degrees): Force has a component opposing motion. The force slows the object down. Example: friction on a sliding box (theta = 180 degrees, cos(180) = -1).
- **Zero work** (theta = 90 degrees): Force is perpendicular to displacement. Example: normal force on a box sliding on a flat surface. Also: centripetal force on an object in uniform circular motion (force is always perpendicular to velocity).

**MCAT insight:** If an object moves in a circle at constant speed, the centripetal force does zero work. This is because the force is always perpendicular to the displacement. This is why speed doesn't change in uniform circular motion -- no net work is being done.

**Work done by gravity:** W_gravity = mgh (where h is the vertical displacement downward). This is positive if the object drops, negative if it rises. Gravity is a **conservative force** -- the work depends only on start and end heights, not the path.

### Work-Energy Theorem

**W_net = delta KE = KE_final - KE_initial**

The net work done on an object equals its change in kinetic energy. This is incredibly useful on the MCAT because it lets you bypass kinematics entirely.

Example: A 2 kg object starts at rest. A net force does 100 J of work on it. What's its final speed?
100 = 1/2 (2) v^2 - 0, so v^2 = 100, v = 10 m/s.

### Kinetic Energy

**KE = 1/2 mv^2**

- Always positive (mass and v^2 are both positive).
- Depends on the square of velocity -- double the speed, quadruple the KE.
- This v-squared relationship is testable: a car going 60 mph has 4 times the KE of the same car going 30 mph, so it needs 4 times the stopping distance (if braking force is constant).

### Potential Energy

**Gravitational PE:** PE = mgh (where h is height above your chosen reference point). The reference point is arbitrary -- pick whatever makes the problem easiest (usually the lowest point in the problem).

**Elastic PE:** PE = 1/2 kx^2 (where k is the spring constant and x is displacement from equilibrium). This is the energy stored in a compressed or stretched spring.

**Key concept:** Potential energy is stored energy associated with **conservative forces** (gravity, springs, electrostatics). Non-conservative forces like friction do NOT have associated potential energy -- they convert mechanical energy into heat.

### Conservation of Energy

**When only conservative forces act:**

KE_i + PE_i = KE_f + PE_f

Total mechanical energy is conserved. This is one of the most powerful tools on the MCAT.

**When non-conservative forces (like friction) also act:**

KE_i + PE_i + W_non-conservative = KE_f + PE_f

Or equivalently: W_friction = delta E_mechanical (the work done by friction equals the change in total mechanical energy, and it's always negative -- friction always removes mechanical energy).

**Problem-solving strategy for energy conservation:**
1. Identify initial and final states.
2. Set a reference point for PE (usually the lowest point = 0).
3. Are there non-conservative forces? If no, use KE_i + PE_i = KE_f + PE_f.
4. Write out each term. Many will be zero (object at rest means KE = 0; object at reference height means PE = 0).
5. Solve for the unknown.

**Classic example:** A ball is dropped from height h. What is its speed just before hitting the ground?

mgh + 0 = 0 + 1/2 mv^2

Mass cancels: v = sqrt(2gh). **Memorize this result.** It comes up constantly.

For h = 5 m: v = sqrt(2 * 10 * 5) = sqrt(100) = 10 m/s. Quick.

**Another classic:** A ball rolls down a frictionless ramp from height h. Speed at bottom? Same answer: v = sqrt(2gh). The shape of the ramp doesn't matter -- only the height difference matters because gravity is conservative.

### Power

**P = W / t** (average power = work done divided by time)

**P = Fv** (instantaneous power = force times velocity, when force is along the direction of motion)

Units: Watts (W) = J/s.

**MCAT application:** A motor lifts a mass m through height h in time t. Power = mgh / t. If the question asks for the force the motor exerts at constant velocity, use P = Fv, where F = mg (at constant velocity, the motor force balances gravity).

---

## 4. Simple Machines

Simple machines make work easier by trading force for distance. **They do NOT reduce the total work** -- in an ideal (frictionless) machine, work in = work out.

W_in = W_out
F_in * d_in = F_out * d_out

**Mechanical advantage (MA):** MA = F_out / F_in = d_in / d_out

A higher MA means you use less force, but you must apply it over a greater distance.

### Pulleys

- **Fixed pulley (single, attached to ceiling):** Changes direction of force only. MA = 1. You pull down with force T, object goes up with force T.
- **Moveable pulley (attached to the load):** MA = 2. You pull with half the force, but pull twice the distance.
- **General rule:** Count the number of rope segments supporting the load. That's the MA.

**Example:** A system has 3 ropes supporting the load. MA = 3. To lift a 300 N object, you need 100 N of force. But to lift it 1 m, you pull 3 m of rope.

### Levers

Three classes based on where the fulcrum, effort, and load are:
- **Class 1:** Fulcrum between effort and load (seesaw). Can have MA > 1 or < 1 depending on distances.
- **Class 2:** Load between fulcrum and effort (wheelbarrow). Always MA > 1.
- **Class 3:** Effort between fulcrum and load (tweezers, baseball bat). Always MA < 1 (sacrifices force for speed/range of motion).

For levers: MA = d_effort / d_load (distance from fulcrum to where effort is applied, divided by distance from fulcrum to the load).

### Inclined Planes as Simple Machines

MA = length of incline / height = L / h = 1 / sin(theta).

To push a mass up a frictionless ramp to height h, you apply a force of mg sin(theta) over a distance of L = h / sin(theta). Work = mg sin(theta) * h/sin(theta) = mgh. Same as lifting straight up -- but you used less force over a longer distance.

---

## 5. Torque and Equilibrium

### Torque

**Torque = r F sin(theta)**

Where r is the distance from the pivot to where the force is applied, F is the magnitude of the force, and theta is the angle between the r vector and the F vector.

Equivalently: torque = r * F_perpendicular, where F_perpendicular is the component of force perpendicular to the lever arm. Or: torque = r_perpendicular * F, where r_perpendicular is the "moment arm" (perpendicular distance from the pivot to the line of action of the force).

**Sign convention:** counterclockwise (CCW) = positive, clockwise (CW) = negative (standard convention unless told otherwise).

Units: N*m (NOT Joules, even though the units are dimensionally the same. Torque is not energy.)

**Maximizing torque:** Apply the force perpendicular to the lever arm (theta = 90 degrees, sin(90) = 1). This is why you push a door at its edge, perpendicular to the door -- maximum torque for a given force.

### Static Equilibrium

An object is in static equilibrium when:
1. **Sum of all forces = 0** (translational equilibrium -- no linear acceleration)
2. **Sum of all torques = 0** (rotational equilibrium -- no angular acceleration)

Both conditions must hold simultaneously.

**Problem-solving for equilibrium:**
1. Draw FBD.
2. Choose a pivot point. (Pro tip: choose the point where the most unknown forces act -- their torques become zero because r = 0, eliminating unknowns.)
3. Set up sum(F_x) = 0, sum(F_y) = 0, and sum(tau) = 0.
4. Solve the system of equations.

**Classic lever/seesaw problem:**

A 4 m beam of negligible mass is supported at its center. A 60 kg person sits 1.5 m from the center on the left. Where must a 40 kg person sit on the right to balance?

Sum of torques about the center = 0:
(60)(g)(1.5) = (40)(g)(d)
d = (60 * 1.5) / 40 = 90/40 = 2.25 m from center.

Note: g cancels. On the MCAT, if everything involves weight (mg), g often cancels and you can just work with masses.

**Beam problems (non-negligible mass):** The weight of the beam acts at its center of mass (usually the geometric center for a uniform beam). Treat it as a point force acting there.

### Center of Mass

**x_cm = (m_1 x_1 + m_2 x_2 + ...) / (m_1 + m_2 + ...)**

The center of mass is the "average position" weighted by mass. For a uniform object, it's at the geometric center. For a system of particles, calculate the weighted average.

**MCAT insight:** The center of mass of a system moves as if all forces act on a single particle of total mass located at that point. Even if parts of the system move in complicated ways (like fragments after an explosion), the center of mass follows a smooth parabolic path (projectile motion).

**Stability:** An object is stable when its center of mass is over its base of support. If the center of mass moves outside the base, the object tips. This connects to biology -- wider stance = larger base = more stable.

---

## 6. Momentum and Impulse

### Momentum

**p = mv**

Momentum is a vector -- it has both magnitude and direction. A 2 kg ball moving at 3 m/s east has momentum 6 kg*m/s east.

### Impulse

**J = F * delta t = delta p = m * delta v**

Impulse is the change in momentum. A force applied over time changes an object's momentum.

**The impulse-momentum connection is huge on the MCAT:**

Rearranging: F = delta p / delta t. For a given change in momentum (e.g., stopping a moving object), increasing the time of contact DECREASES the average force.

This explains:
- Why airbags work (increase collision time, decrease force on body)
- Why you bend your knees when landing from a jump
- Why a boxer "rolls with" a punch
- Why catching an egg requires soft hands

**Estimation example:** A 0.15 kg baseball moving at 40 m/s is caught by a mitt in 0.01 s. What average force does the mitt exert?

F = delta p / delta t = (0.15)(40) / 0.01 = 6 / 0.01 = 600 N. That's a significant force -- roughly 135 lbs.

### Conservation of Momentum

**In any collision (or explosion), if no external forces act, total momentum is conserved.**

m_1 v_1i + m_2 v_2i = m_1 v_1f + m_2 v_2f

This applies to ALL collision types. External forces like friction during the collision are usually negligible because the collision time is so short.

**Warning:** Momentum is a vector. In 2D problems, conserve momentum separately in x and y directions.

### Collision Types

| Type | Momentum Conserved? | KE Conserved? | Objects After |
|------|---------------------|---------------|---------------|
| Elastic | Yes | Yes | Bounce apart |
| Inelastic | Yes | No (KE decreases) | Bounce apart (with deformation) |
| Perfectly inelastic | Yes | No (maximum KE loss) | Stick together |

**Elastic collisions** -- both momentum and KE are conserved. Rare in real life (billiard balls are approximately elastic). Special cases to memorize:
- Equal masses, one at rest: the moving one stops completely, the stationary one moves with the original velocity.
- A small object hitting a massive stationary object: the small object bounces back with nearly the same speed, the massive object barely moves (like a ball bouncing off a wall).
- A massive object hitting a small stationary one: the massive object barely slows down, the small object flies off at about twice the massive object's speed.

**Perfectly inelastic collisions** -- objects stick together. Use:
m_1 v_1i + m_2 v_2i = (m_1 + m_2) v_f

This gives the maximum kinetic energy loss for a given initial configuration. The "lost" KE goes into deformation, heat, and sound.

**Where did the KE go?** In inelastic collisions, KE is converted to thermal energy, sound, deformation. The MCAT may ask you to calculate how much KE was lost -- find KE_total before and after, subtract.

**Worked approach -- perfectly inelastic collision:**

A 5 kg block moving at 4 m/s collides with and sticks to a 3 kg block at rest. Find the final velocity and the KE lost.

Momentum conservation: (5)(4) + (3)(0) = (5+3)(v_f)
20 = 8 v_f
v_f = 2.5 m/s

KE_initial = 1/2 (5)(4^2) = 40 J
KE_final = 1/2 (8)(2.5^2) = 1/2 (8)(6.25) = 25 J
KE lost = 40 - 25 = 15 J

That 15 J went into heat, sound, and deformation.

---

## MCAT Strategy Summary

### Estimation Without a Calculator

- g ~ 10 m/s^2 (not 9.8)
- sqrt(2) ~ 1.4, sqrt(3) ~ 1.7
- pi ~ 3
- sin(30) = 0.5, sin(45) ~ 0.7, sin(60) ~ 0.87
- cos(30) ~ 0.87, cos(45) ~ 0.7, cos(60) = 0.5
- When squaring numbers: 15^2 = 225, 25^2 = 625, etc. -- practice mental math.
- For division: 7/3 ~ 2.3, 100/7 ~ 14.3. Use fractions when possible, convert at the end.

### Pattern Recognition -- What to Do When You See...

| Trigger | Action |
|---------|--------|
| "Object dropped from rest" | v_0 = 0, a = g downward. Use free fall equations. |
| "Projectile launched at angle" | Decompose into components. Horizontal = constant velocity, vertical = free fall. |
| "Inclined plane" | Decompose mg: parallel = mg sin(theta), perpendicular = mg cos(theta). |
| "Constant velocity" or "moves at steady speed" | a = 0, so net force = 0. All forces balance. |
| "Just barely starts to slide" | Static friction is at maximum: f_s = mu_s * N. |
| "How fast at the bottom of..." | Conservation of energy: mgh = 1/2 mv^2, v = sqrt(2gh). |
| "Collision" | Conservation of momentum. Check if elastic or inelastic. |
| "Airbag / padding / cushion" | Impulse: same delta p, more time, less force. |
| "Beam / plank supported at a point" | Torque equilibrium. Pick the support point as pivot. |
| "Moving in a circle" | Centripetal force = mv^2/r toward center. Identify which real force provides it. |
| "No friction / frictionless" | Only conservative forces -- use conservation of energy freely. |
| "How much energy is lost" | Calculate KE before and after. Difference = energy lost to heat/deformation. |

### Common Traps

1. **Normal force equals mg?** Only on flat surfaces with no other vertical forces. On inclines, N = mg cos(theta). If someone pushes down on the object, N > mg.
2. **Centripetal vs centrifugal:** Centrifugal force doesn't exist in an inertial frame. On the MCAT, always use centripetal (toward center). If a question references centrifugal force, it's testing whether you know it's fictitious.
3. **Weight vs mass:** Weight = mg (force, in Newtons). Mass = intrinsic property (in kg). An astronaut in orbit is weightless (free fall) but still has mass.
4. **KE in collisions:** Momentum is ALWAYS conserved in collisions. KE is only conserved in elastic collisions. Many students confuse these.
5. **Work done by gravity on a curved path:** Gravity is conservative -- work depends only on vertical displacement, not the path shape. W = mgh regardless of how the object got from top to bottom.
6. **Static friction is not always mu_s * N.** It's only at that maximum when the object is on the verge of sliding. Otherwise, it adjusts to match the applied force.

---

## Quick Reference Formulas

**Kinematics (constant a):**
v = v_0 + at | delta x = v_0 t + 1/2 at^2 | v^2 = v_0^2 + 2a(delta x)

**Forces:**
F_net = ma | f_s (max) = mu_s N | f_k = mu_k N | F_c = mv^2/r

**Work & Energy:**
W = Fd cos(theta) | KE = 1/2 mv^2 | PE_grav = mgh | PE_spring = 1/2 kx^2
W_net = delta KE | P = W/t = Fv

**Torque & Equilibrium:**
tau = rF sin(theta) | Equilibrium: sum(F) = 0 and sum(tau) = 0

**Momentum:**
p = mv | J = F delta t = delta p | m_1v_1i + m_2v_2i = m_1v_1f + m_2v_2f

**Derived results to memorize:**
v = sqrt(2gh) (object falling from height h)
a = g sin(theta) (frictionless incline)
MA_pulley = number of supporting ropes
