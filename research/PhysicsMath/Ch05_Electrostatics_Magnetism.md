# Physics & Math Chapter 5 — Electrostatics & Magnetism

Scope: Electric charge, Coulomb's law, electric field, electric potential energy, electric potential, conductors vs insulators, parallel plates (uniform field), Gauss's law concepts, capacitors; magnetic force on moving charges and current-carrying wires.

**Section:** Chemical/Physical (CP) — Physics & Math
**Book:** Kaplan Physics and Math Strategies 2024 — Chapter 5
**AAMC FC mapping:** FC4C (Electrochemistry, electrical circuits, and magnetism)
**Yield:** High. Electrostatics, Coulomb's law, and capacitors appear frequently; magnetism is lower yield but conceptually testable.

> **Note on electrochemistry:** Electrochemical cells, galvanic/electrolytic cells, cell potential (E°_cell), Faraday's law, and the Nernst equation are NOT in this chapter. That content belongs in `research/GenChem/Ch12_Electrochemistry.md`. Any legacy electrochemistry material from Circuits.md has been moved there. Cross-reference Gen Chem Ch 12 for all electrochemical content.

---

## 1. Electric Charge

### The Basics

**Charge is quantized** — smallest unit is **e = 1.6 × 10⁻¹⁹ C**. Every charge is a whole-number multiple of e. Protons carry +e, electrons carry −e.

**Charge is conserved** — never created or destroyed, only transferred. When you rub a balloon on your hair, electrons move; total system charge stays the same.

### Conductors vs. Insulators

- **Conductors** (metals, electrolyte solutions): electrons move freely. In a conductor at electrostatic equilibrium: all excess charge sits on the outer surface; electric field inside = 0.
- **Insulators** (rubber, glass, plastic): electrons locked in place. Charge stays wherever you put it.

**MCAT application:** These distinctions matter for capacitors (dielectrics) and for understanding why metals form electrodes.

---

## 2. Coulomb's Law

**F = k(q₁q₂)/r²**

Where **k = 8.99 × 10⁹ N·m²/C²** (round to 9 × 10⁹).

Key features:
- **Inverse square law:** Double the distance → force drops to ¼. Triple → drops to 1/9.
- **Like charges repel, opposite charges attract.**
- **Comparison to gravity:** Both are inverse square. But gravity is always attractive; electrostatic force can attract or repel. Electrostatic force is enormously stronger at the atomic scale.

**MCAT tip:** You rarely compute Coulomb's law numerically. The test loves **proportional reasoning**. "Distance triples → force decreases by factor of 9." Practice this pattern.

---

## 3. Electric Field

**E = kQ/r²** (from a point charge Q)

The electric field is **force per unit positive test charge** at a point in space. Units: N/C or V/m (equivalent).

**Direction convention:** Electric field lines point **away from positive** charges and **toward negative** charges. Direction a positive test charge would move.

### Uniform Field Between Parallel Plates

The MCAT's most tested electrostatics setup:

**E = V/d** (between parallel plates)

Where V = voltage across plates, d = plate separation.

- Field is uniform in magnitude and direction everywhere between the plates.
- Field points from positive plate to negative plate.

**MCAT favorite:** A charged particle placed between parallel plates experiences a constant force F = qE. This is analogous to gravity — it creates parabolic motion like a projectile.

### Gauss's Law (Conceptual)

**Φ = Q_enclosed/ε₀**

The electric flux through any closed surface equals the enclosed charge divided by ε₀ (permittivity of free space = 8.85 × 10⁻¹² F/m).

**Key results from Gauss's law (know these without derivation):**
- Spherical conductor: all charge on outer surface; E = 0 inside.
- Outside a spherical charge distribution: field is the same as if all charge were at the center (E = kQ/r²).
- Uniform electric field between parallel plates: E = σ/ε₀ (σ = surface charge density).
- Inside a conductor in electrostatic equilibrium: E = 0.

---

## 4. Electric Potential Energy and Electric Potential

### Electric Potential Energy (U)

**U = kq₁q₂/r**

This is the energy stored in the system of two charges. Sign matters:
- Like charges (positive product q₁q₂): U > 0. You must do work to push them together.
- Opposite charges (negative product): U < 0. The system releases energy as they approach.

### Electric Potential (V)

**V = kQ/r** (from a point charge Q)

**Potential is a SCALAR, not a vector.** When computing potential at a point due to multiple charges, add algebraically (with signs). No vector components, no trig. This makes potential calculations far easier than force or field calculations.

- Positive charges create positive potential.
- Negative charges create negative potential.
- Potential decreases with distance from a positive charge.

**Potential vs potential energy:** V is the property of a point in space. U is the property of a charge placed at that point.

**U = qV = kq₁q₂/r**

**Movement:** A positive charge naturally moves from high potential to low potential (like a ball rolling downhill). A negative charge moves from low to high potential. Both move to lower potential energy.

### Equipotential Surfaces

**Equipotential lines/surfaces are always perpendicular to electric field lines.** No work is done moving a charge along an equipotential surface (force perpendicular to displacement).

- Around a point charge: equipotentials are concentric spheres.
- Between parallel plates: equipotentials are flat planes parallel to the plates.

---

## 5. Capacitors

A capacitor stores charge and energy in an electric field between two conductors. The MCAT focuses overwhelmingly on **parallel plate capacitors**.

### Capacitance

**C = ε₀(A/d)**

Where A = plate area, d = plate separation, ε₀ = 8.85 × 10⁻¹² F/m. Units: **Farads (F)**.

Bigger plates or closer spacing → more capacitance. Intuition: bigger plates hold more charge; closer plates have a stronger field pulling charge onto them.

### Charge-Voltage Relationship

**Q = CV**

Defining equation. Higher C → stores more charge for same voltage.

### Energy Stored

**U = ½CV² = Q²/(2C) = ½QV**

All three forms are equivalent. Which you use depends on what's held constant.

### Dielectrics

A **dielectric** is an insulating material inserted between plates. Increases capacitance by factor κ (kappa, the dielectric constant, always ≥ 1):

**C' = κC**

**The critical MCAT question:** What happens when you insert a dielectric?

**It depends on whether the capacitor is connected to a battery (V fixed) or isolated (Q fixed):**

| Scenario | V | Q | C | E (field) | U (energy) |
|----------|---|---|---|-----------|------------|
| **Battery connected** (V fixed) | Same | ↑ (Q=CV, C↑) | ↑ | Same (E=V/d) | ↑ (U=½CV²) |
| **Isolated** (Q fixed) | ↓ (V=Q/C, C↑) | Same | ↑ | ↓ | ↓ (U=Q²/2C) |

**MCAT trap:** Students constantly mix these scenarios. Always ask: "Is V fixed (battery connected) or Q fixed (isolated/disconnected)?"

### Capacitors in Circuits (brief)

See Chapter 6 (Circuits) for capacitors in series and parallel, RC time constants, and charging/discharging behavior.

**Quick rule:** Capacitors in series → add reciprocals (like resistors in parallel). Capacitors in parallel → add directly (like resistors in series). The rules are REVERSED compared to resistors.

---

## 6. Magnetism

### Force on a Moving Charge

**F = qvB sin θ**

A magnetic field exerts a force on a **moving** charge. If v = 0, no magnetic force. If charge moves parallel to B (θ = 0°), sin θ = 0, no force. Maximum force when charge moves perpendicular to B (θ = 90°).

### The Right-Hand Rule

1. **Point fingers** in the direction of velocity (v) of a positive charge.
2. **Curl fingers** toward the magnetic field (B).
3. **Thumb** points in the direction of force on a positive charge.

For a **negative charge**: apply right-hand rule, then **flip the direction**.

### Magnetic Force Does No Work

**The magnetic force is always perpendicular to the velocity.** W = Fd cos 90° = 0.

Magnetic force can change direction of motion but NEVER speed. A charged particle in a uniform magnetic field moves in a **circle** (constant speed, changing direction).

**MCAT consequence:** If a passage says a charged particle speeds up in a magnetic field, there must be an electric field doing the work. A magnetic field alone cannot change kinetic energy.

### Force on a Current-Carrying Wire

**F = BIL sin θ**

Where I = current, L = length of wire in the field. Use right-hand rule with current direction replacing velocity direction.

### Magnetic Field from a Long Straight Wire

**B = μ₀I/(2πr)**

Field wraps around wire in concentric circles. Right-hand rule for wires: thumb in direction of current → fingers curl in direction of B.

Lower yield on MCAT, but know: field is proportional to current, inversely proportional to distance.

---

## MCAT Strategy Summary

### Pattern Recognition

| Trigger | Action |
|---------|--------|
| "Distance between charges doubles" | F decreases by ¼ (Coulomb). V decreases by ½. U decreases by ½. |
| "Charge between parallel plates" | F = qE = qV/d (constant force → constant acceleration, like projectile). |
| "Conductor at equilibrium" | E = 0 inside. All charge on outer surface. |
| "Dielectric inserted, battery connected" | V same, Q and C increase, U increases. |
| "Dielectric inserted, capacitor isolated" | Q same, V and E decrease, C increases, U decreases. |
| "Charged particle in magnetic field" | Circular motion. Magnetic force ⊥ velocity, does no work. |
| "Particle speeds up in magnetic field" | Impossible by magnetic force alone — must have electric field. |

### Common Traps

1. **Coulomb vs gravity:** Both inverse square, but electrostatic can repel AND is far stronger at atomic scale.
2. **Potential is a scalar:** Add contributions from multiple charges algebraically (no trig needed).
3. **U = qV vs U = kq₁q₂/r:** Both are electric potential energy — just different ways to calculate it.
4. **Dielectric with battery vs isolated capacitor:** Opposite effects on V and U — know which scenario you're in.
5. **Magnetic force does no work:** Cannot change speed, only direction. This is a beloved MCAT conceptual point.

### Quick Reference

**Coulomb:** F = kq₁q₂/r² | k = 9 × 10⁹ N·m²/C²
**Electric field (point charge):** E = kQ/r²
**Electric field (parallel plates):** E = V/d
**Electric potential:** V = kQ/r (scalar)
**Potential energy:** U = qV = kq₁q₂/r
**Capacitance:** C = ε₀A/d | Q = CV | U = ½CV²
**Dielectric:** C' = κC
**Magnetic force (charge):** F = qvB sin θ
**Magnetic force (wire):** F = BIL sin θ
