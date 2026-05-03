# Physics & Math Chapter 2 — Work, Energy & Simple Machines

Scope: Kinetic and potential energy; conservation of energy; work (W = Fd cos θ, dot product); power; simple machines and mechanical advantage (pulleys, levers, inclined planes).

**Section:** Chemical/Physical (CP) — Physics & Math
**Book:** Kaplan Physics and Math Strategies 2024 — Chapter 2
**AAMC FC mapping:** FC4A (Translational motion, forces, work, energy, equilibrium)
**Yield:** Very high. Energy conservation is one of the most efficient problem-solving tools on the MCAT.

---

## 1. Work

### Definition

**W = Fd cos θ**

Where θ is the angle between the force vector and the displacement vector.

- **Positive work** (θ < 90°): Force has a component in the direction of motion. Object speeds up or is pushed along.
- **Negative work** (θ > 90°): Force has a component opposing motion. Object slows down. Friction: θ = 180°, cos(180°) = −1.
- **Zero work** (θ = 90°): Force is perpendicular to displacement. Normal force on flat surface. Centripetal force in uniform circular motion (force always perpendicular to velocity — this is why speed doesn't change in uniform circular motion).

**Units:** Joules (J) = N·m = kg·m²/s²

### Work Done by Gravity

W_gravity = mgh (positive when object drops, h is vertical displacement downward).

Gravity is a **conservative force** — work depends only on start and end heights, not the path.

### Work-Energy Theorem

**W_net = ΔKE = KE_final − KE_initial**

The net work done on an object equals its change in kinetic energy. This lets you bypass kinematics entirely for many problems.

**Example:** 2 kg object starts at rest. Net force does 100 J of work. Final speed?
100 = ½(2)v² → v² = 100 → v = 10 m/s.

---

## 2. Kinetic Energy

**KE = ½mv²**

- Always positive (m and v² are positive).
- Depends on the SQUARE of velocity: double the speed → 4× the KE.
- **MCAT application:** A car going 60 mph has 4× the KE of the same car at 30 mph → needs 4× the stopping distance (if braking force is constant).

---

## 3. Potential Energy

### Gravitational PE

**PE_grav = mgh**

Where h is height above your chosen reference point. Reference is arbitrary — pick what makes the problem easiest (usually the lowest point = 0).

### Elastic PE (Spring)

**PE_spring = ½kx²**

Where k = spring constant (stiffness, units: N/m) and x = displacement from equilibrium.

### Conservative Forces

Potential energy is associated with **conservative forces** (gravity, springs, electrostatics). Conservative = work depends only on start and end positions, not path.

**Non-conservative forces** (friction, air resistance) do NOT have associated potential energy — they convert mechanical energy into heat (irreversible).

---

## 4. Conservation of Energy

### When Only Conservative Forces Act

**KE_i + PE_i = KE_f + PE_f**

Total mechanical energy is conserved. One of the most powerful tools on the MCAT.

### When Non-Conservative Forces (like Friction) Also Act

**KE_i + PE_i + W_nc = KE_f + PE_f**

Or: W_friction = ΔE_mechanical (always negative — friction removes mechanical energy).

### Problem-Solving Strategy

1. Identify initial and final states.
2. Set reference point for PE (lowest point = 0 usually).
3. Are there non-conservative forces? If no → use KE_i + PE_i = KE_f + PE_f.
4. Write out each term. Many will be zero (object at rest → KE = 0; at reference height → PE = 0).
5. Solve.

**Classic result to memorize:** Object dropped from height h:
mgh = ½mv² → **v = √(2gh)**

For h = 5 m: v = √(100) = 10 m/s.

**Corollary:** Object rolling down any frictionless ramp from height h — speed at the bottom is ALSO √(2gh), regardless of ramp shape. Conservative forces → only height matters.

---

## 5. Power

**P = W/t** (average power)

**P = Fv** (instantaneous power, when F is along direction of motion)

Units: Watts (W) = J/s

**MCAT application:** Motor lifts mass m through height h in time t:
P = mgh/t

To find the force the motor exerts at constant velocity: P = Fv, where F = mg (constant velocity → net force = 0 → motor force = mg).

---

## 6. Simple Machines

Simple machines trade force for distance. **They do NOT reduce total work** — in an ideal frictionless machine, work in = work out.

**W_in = W_out → F_in · d_in = F_out · d_out**

**Mechanical Advantage (MA):**

MA = F_out / F_in = d_in / d_out

Higher MA → less force needed, but must apply it over greater distance.

**Efficiency (real machines):**

Efficiency = (W_out / W_in) × 100%

Real machines always have efficiency < 100% due to friction.

### Pulleys

- **Fixed pulley (single, ceiling-mounted):** Changes direction only. MA = 1. You pull down with T, object goes up with T.
- **Moveable pulley (attached to load):** MA = 2. Apply half the force, pull twice the distance.
- **General rule:** Count the number of rope segments supporting the load = MA.

**Example:** 3 ropes supporting the load → MA = 3. To lift 300 N object, need 100 N force. To lift it 1 m, pull 3 m of rope.

### Levers

Three classes based on positions of fulcrum (F), effort (E), and load (L):

| Class | Arrangement | MA | Examples |
|-------|-------------|-----|---------|
| 1 | F between E and L | Variable (>1 or <1) | Seesaw, scissors |
| 2 | L between F and E | Always >1 | Wheelbarrow, nutcracker |
| 3 | E between F and L | Always <1 (speed/range trade) | Tweezers, baseball bat |

**MA for levers:** MA = d_effort / d_load (distance from fulcrum to effort / distance from fulcrum to load).

### Inclined Planes as Simple Machines

MA = L/h = 1/sin θ (L = length of ramp, h = height).

To push a mass up a frictionless ramp to height h: apply force mg sin θ over distance L = h/sin θ.
Work = mg sin θ × h/sin θ = mgh. Same as lifting straight up — less force, longer distance.

---

## MCAT Strategy Summary

### Energy Conservation vs Kinematics

**Use energy conservation when:** The problem involves heights, speeds, or springs without specifying time or asking for time.

**Use kinematics when:** The problem involves time, or asks about motion at a specific instant.

**Pattern recognition:**
- "Speed at the bottom of a ramp" → energy conservation → v = √(2gh)
- "How much energy is lost" → KE before − KE after
- "How long does it take" → kinematics
- "Motor pulls load at constant velocity" → P = Fv with F = mg

### Common Traps

1. **Work is zero for perpendicular forces.** Normal force does no work. Centripetal force does no work. Students forget this.
2. **Reference point for PE.** Always pick the lowest point = 0 unless the problem specifies otherwise.
3. **KE depends on v², not v.** Tripling speed means 9× the KE, not 3×.
4. **Friction always removes mechanical energy.** W_friction is always negative. If the problem asks "how much energy was lost to friction," that's |W_friction|.
5. **Mechanical advantage ≠ energy advantage.** MA trades force for distance. Total work is the same (ideal machine).

### Quick Reference

**Work:** W = Fd cos θ | W_grav = mgh (downward positive)
**Work-energy theorem:** W_net = ΔKE
**Energy:** KE = ½mv² | PE_grav = mgh | PE_spring = ½kx²
**Conservation (no friction):** KE_i + PE_i = KE_f + PE_f
**Power:** P = W/t = Fv
**Mechanical advantage:** MA = F_out/F_in = d_in/d_out
**Key result:** v = √(2gh) (object falling from height h or at bottom of frictionless ramp)
