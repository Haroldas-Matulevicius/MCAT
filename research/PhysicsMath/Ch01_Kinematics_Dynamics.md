# Physics & Math Chapter 1 — Kinematics & Dynamics

Scope: Units and measurement; vectors vs scalars; displacement, velocity, acceleration; Newton's 1st/2nd/3rd laws; constant-acceleration kinematics (Big 5); friction; inclined planes; circular motion; torque and static equilibrium.

**Section:** Chemical/Physical (CP) — Physics & Math
**Book:** Kaplan Physics and Math Strategies 2024 — Chapter 1
**AAMC FC mapping:** FC4A (Translational motion, forces, work, energy, equilibrium)
**Yield:** Very high. Newton's laws, kinematics equations, and equilibrium appear on nearly every MCAT.

---

## 1. Units and Measurement

### SI Base Units

The MCAT assumes SI units unless otherwise specified. You need to know these cold.

| Quantity | Unit | Symbol |
|----------|------|--------|
| Mass | kilogram | kg |
| Length | meter | m |
| Time | second | s |
| Electric current | ampere | A |
| Temperature | kelvin | K |
| Amount of substance | mole | mol |

**Derived units you must know:**
- Force: Newton (N) = kg·m/s²
- Energy: Joule (J) = kg·m²/s²
- Pressure: Pascal (Pa) = N/m² = kg/(m·s²)
- Power: Watt (W) = J/s

### Vectors vs Scalars

**Scalar:** Magnitude only. Examples: mass, speed, distance, time, energy, temperature.

**Vector:** Magnitude AND direction. Examples: displacement, velocity, acceleration, force, momentum.

**MCAT consequence:** When a problem involves vectors, you must consider direction. Two forces of equal magnitude can cancel (if opposite) or add (if same direction).

**Adding vectors:** In 1D, just use signs (+/-). In 2D, break into components, add x- and y-components separately, then use the Pythagorean theorem to find the resultant magnitude.

---

## 2. Kinematics

Kinematics describes *how* objects move without caring *why* they move.

### Key Definitions

- **Displacement** (Δx): vector — how far you end up from where you started, with direction. If you walk 3 m east then 3 m west, Δx = 0.
- **Distance**: scalar — total path length. Same walk = 6 m.
- **Velocity** (v): vector, rate of change of displacement. v = Δx/Δt.
- **Speed**: scalar, rate of change of distance. Always positive.
- **Acceleration** (a): vector, rate of change of velocity. a = Δv/Δt. On the MCAT, acceleration almost always means *constant* acceleration.

**MCAT trap:** "The car travels at constant speed around a curve" → acceleration = 0? NO. Direction is changing, so velocity is changing, so there IS acceleration (centripetal).

### The Big 5 Kinematic Equations

These only work for **constant acceleration**. Each equation is missing one variable.

| Equation | Missing Variable |
|----------|-----------------|
| v = v₀ + at | Δx |
| Δx = v₀t + ½at² | v (final) |
| Δx = vt − ½at² | v₀ (initial) |
| v² = v₀² + 2aΔx | t |
| Δx = ½(v₀ + v)t | a |

**Problem-solving strategy:**
1. List what you know: v₀, v, a, t, Δx.
2. Identify what you want.
3. You'll know three variables and want a fourth. The fifth is irrelevant — pick the equation missing it.

**When you see "how far before stopping"** → v_final = 0, want Δx, don't need t. Use **v² = v₀² + 2aΔx**.

**When you see "how long to reach..."** → want t, know v₀/v/a. Use **v = v₀ + at**.

### Free Fall

Free fall = only acceleration is gravity. a = g = 9.8 m/s² downward (use 10 m/s² on the MCAT).

- Object dropped from rest: v₀ = 0, a = −g (taking up as positive).
- Object thrown upward: at the peak, v = 0. Time up = time down (same height). Speed at launch = speed at landing.

**Quick estimation:** Object in free fall for 2 s: drops ~20 m, reaches ~20 m/s.

### Projectile Motion

Key insight: **horizontal and vertical motions are independent.** They share only time.

- Horizontal: a_x = 0 (no air resistance on MCAT unless stated). x = v₀ₓt.
- Vertical: a_y = −g. Use Big 5 with a = −g.

**Decomposing initial velocity:**
- v₀ₓ = v₀ cos θ
- v₀ᵧ = v₀ sin θ

**Solving projectile problems:**
1. Break v₀ into components.
2. Use vertical equations to find time (often set y = 0 for landing, or vᵧ = 0 for max height).
3. Plug that time into the horizontal equation.

**MCAT facts to know:**
- Max range occurs at 45°.
- Complementary angles (30° and 60°) give the same range.
- At the top of the arc, vᵧ = 0 but vₓ is still there — the object is NOT at rest at the top.

---

## 3. Newton's Laws of Motion

### First Law (Inertia)

An object at rest stays at rest; an object in motion stays in motion at constant velocity, **unless acted on by a net external force**. Mass is the measure of inertia.

### Second Law (F = ma)

**The workhorse equation of mechanics.** Net force = mass × acceleration.

**F means the NET force — the vector sum of ALL forces.** If two forces cancel, net F = 0, so a = 0 (constant velocity, not necessarily rest).

**Problem-solving with F = ma:**
1. Draw a free body diagram (FBD).
2. Choose a coordinate system.
3. Sum forces in each direction.
4. Set ΣF_x = ma_x and ΣF_y = ma_y.
5. Solve for unknowns.

### Third Law (Action-Reaction)

For every action, there is an equal and opposite reaction. **The forces act on DIFFERENT objects.** They don't cancel each other because they're on different objects.

**Example:** Small car hits large truck. Equal forces on each. Car accelerates more because smaller mass (a = F/m).

### Free Body Diagrams

Forces to consider for any object:
- **Weight (mg):** straight down from center of mass.
- **Normal force (N):** perpendicular to contact surface. NOT always equal to mg.
- **Friction (f):** parallel to surface, opposing motion.
- **Tension (T):** along a rope/string, pulling away from the object.
- **Applied force (F_app):** external push/pull.

### Friction

**Static friction (f_s):** Acts when the object is NOT sliding. f_s ≤ μ_s · N. Variable — only at maximum right before sliding begins.

**Kinetic friction (f_k):** Acts when the object IS sliding. f_k = μ_k · N. Fixed value.

**Key relationship:** μ_s > μ_k always. Harder to start sliding than to keep sliding.

**MCAT trap:** Static friction on a stationary object with a small applied force ≠ μ_s · N. That's the MAXIMUM. Actual friction = applied force (since net force = 0).

### Inclined Planes

Set axes: x-axis along the plane, y-axis perpendicular.

Weight decomposition:
- **Parallel to incline** (down the slope): mg sin θ
- **Perpendicular to incline** (into surface): mg cos θ

Normal force: N = mg cos θ.

**Memory trick:** At θ = 0 (flat), no component along surface. sin(0) = 0. ✓

**Frictionless incline:** a = g sin θ. At 30°, a = g/2 = 5 m/s².

### Circular Motion

Any object moving in a circle at constant speed has **centripetal acceleration** toward the center.

- a_c = v²/r
- F_c = mv²/r (NET force toward the center — NOT a new kind of force)

**Centripetal force is not a separate force.** It's whichever real force(s) point toward the center. For a ball on a string = tension. For a car turning = friction. For a planet orbiting = gravity.

**Common pattern:** "Minimum speed to maintain contact at top of loop" → at the top, N = 0 at minimum, so mg = mv²/r, giving v = √(gr).

---

## 4. Torque and Static Equilibrium

### Torque

**τ = rF sin θ**

Where r = distance from pivot, F = force magnitude, θ = angle between r and F vectors.

**Equivalently:** τ = r · F_⊥ (perpendicular component of force) or τ = r_⊥ · F (moment arm).

**Sign convention:** CCW = positive, CW = negative.

Units: N·m (NOT Joules — torque is not energy).

**Maximizing torque:** Apply force perpendicular to the lever arm (θ = 90°, sin = 1). Why door handles are at the edge.

### Static Equilibrium

An object in static equilibrium satisfies BOTH:
1. **ΣF = 0** (translational equilibrium — no linear acceleration)
2. **Στ = 0** (rotational equilibrium — no angular acceleration)

**Problem-solving strategy:**
1. Draw FBD.
2. Choose a pivot point (pick where the most unknowns act → their torques = 0).
3. Set up ΣF_x = 0, ΣF_y = 0, and Στ = 0.
4. Solve.

**Classic seesaw problem:**
A 4 m beam supported at center. 60 kg person sits 1.5 m from center left. Where must 40 kg person sit on right?
Στ = 0: (60)(g)(1.5) = (40)(g)(d) → d = 2.25 m. Note: g cancels.

**Beam with mass:** Weight of beam acts at its center of mass (geometric center for uniform beam).

### Center of Mass

**x_cm = (m₁x₁ + m₂x₂ + ...) / (m₁ + m₂ + ...)**

The center of mass moves as if all external forces act on a single particle of total mass there.

**Stability:** Object is stable when its center of mass is over its base of support. Wider stance = larger base = more stable.

---

## 5. Momentum and Impulse

### Momentum

**p = mv**

Momentum is a vector. A 2 kg ball moving at 3 m/s east has momentum 6 kg·m/s east.

### Impulse

**J = F·Δt = Δp = m·Δv**

**Key insight (huge on MCAT):** F = Δp/Δt. For a given change in momentum, increasing time DECREASES average force.

This explains:
- Why airbags work (increase collision time, decrease force on body)
- Why you bend your knees landing from a jump
- Why catching an egg requires soft hands

### Conservation of Momentum

**In any collision, if no external forces act, total momentum is conserved.**

m₁v₁ᵢ + m₂v₂ᵢ = m₁v₁f + m₂v₂f

Applies to ALL collision types. In 2D, conserve x and y separately.

### Collision Types

| Type | Momentum Conserved? | KE Conserved? | Objects After |
|------|---------------------|---------------|---------------|
| Elastic | Yes | Yes | Bounce apart |
| Inelastic | Yes | No (KE decreases) | Bounce apart |
| Perfectly inelastic | Yes | No (max KE loss) | Stick together |

**Perfectly inelastic:** m₁v₁ᵢ + m₂v₂ᵢ = (m₁ + m₂)vf

**Special elastic cases to memorize:**
- Equal masses, one at rest: moving one stops completely, stationary one moves off at original speed.
- Small object bounces off massive wall: bounces back with nearly same speed.

**KE lost in inelastic collision:** Calculate KE before and after, subtract. Goes to heat, sound, deformation.

---

## MCAT Strategy Summary

### Pattern Recognition — What to Do When You See...

| Trigger | Action |
|---------|--------|
| "Object dropped from rest" | v₀ = 0, a = g downward. Free fall equations. |
| "Projectile at angle" | Decompose into components. Horizontal = constant v, vertical = free fall. |
| "Inclined plane" | mg sin θ along incline, mg cos θ perpendicular. |
| "Constant velocity / steady speed" | a = 0, net force = 0. |
| "Just barely starts to slide" | f_s = μ_s · N (at maximum). |
| "How fast at bottom of ramp" | Use energy conservation (see Ch02). |
| "Collision" | Conserve momentum. Check elastic vs inelastic. |
| "Airbag / cushion / padding" | Impulse: same Δp, more time, less force. |
| "Beam / plank supported" | Torque equilibrium. Pick support as pivot. |
| "Moving in a circle" | F_c = mv²/r toward center. Identify real force providing it. |

### Common Traps

1. **Normal force ≠ mg on inclines.** N = mg cos θ on inclines.
2. **Centrifugal force doesn't exist** in an inertial frame. Always use centripetal (toward center).
3. **Weight vs mass:** Weight = mg (Newtons). Mass = kg. Astronaut in orbit is weightless but has mass.
4. **Static friction is NOT always μ_s · N.** Only at maximum on verge of sliding.
5. **Action-reaction pairs act on DIFFERENT objects** — they don't cancel.

### Quick Reference Formulas

**Kinematics (constant a):**
v = v₀ + at | Δx = v₀t + ½at² | v² = v₀² + 2aΔx

**Forces:**
F_net = ma | f_s(max) = μ_s N | f_k = μ_k N | F_c = mv²/r

**Torque & Equilibrium:**
τ = rF sin θ | ΣF = 0 AND Στ = 0

**Momentum:**
p = mv | J = FΔt = Δp | m₁v₁ᵢ + m₂v₂ᵢ = m₁v₁f + m₂v₂f

**Derived results to memorize:**
a = g sin θ (frictionless incline) | v = √(gr) (minimum speed at top of loop)
