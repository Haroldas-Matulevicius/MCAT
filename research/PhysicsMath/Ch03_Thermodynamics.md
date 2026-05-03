# Physics & Math Chapter 3 — Thermodynamics

Scope: Zeroth law (thermal equilibrium); open/closed/isolated systems; first law (ΔU = Q − W, sign conventions); second law (entropy, heat engines, Carnot efficiency).

**Section:** Chemical/Physical (CP) — Physics & Math
**Book:** Kaplan Physics and Math Strategies 2024 — Chapter 3
**AAMC FC mapping:** FC4A (partially) / FC5C (thermodynamics of living systems)
**Yield:** Moderate. Heat engines and entropy appear occasionally; thermodynamic reasoning about biological systems is more common.

> **[Content gap — this chapter represents a GENUINE gap in the source research files]**
>
> Current physics research files (Mechanics.md, Fluids.md, Circuits.md, Light_Sound.md, Nuclear.md, Math_Skills.md) contained no dedicated physics thermodynamics content. The chemistry-side thermodynamics (Hess's law, Gibbs free energy, enthalpy) already lives in `research/GenChem/Ch07_Thermochemistry.md`. The stubs below cover the **physics** thermodynamics that Kaplan Physics Ch 3 tests, which is distinct from the chemistry content.
>
> **Expand each section with full teaching content on first study session of this chapter.**

---

## 1. Temperature and Thermal Equilibrium

**[Content gap — expand on first study session of this chapter]**

The **zeroth law of thermodynamics** states: if system A is in thermal equilibrium with system B, and system B is in thermal equilibrium with system C, then A and C are in thermal equilibrium with each other.

**MCAT relevance:** This law justifies the use of thermometers. It defines thermal equilibrium as the condition where there is no net heat transfer between objects in contact.

Key concepts to master:
- Temperature is a measure of average kinetic energy of particles.
- Heat (Q) is energy transferred due to a temperature difference; it flows spontaneously from hot to cold.
- Thermal equilibrium means T_A = T_B (no net energy flow).
- Specific heat capacity (c): Q = mcΔT. Higher c means more heat required per degree of temperature change.
- Water has an exceptionally high specific heat (4.18 J/g·K) — biologically critical for temperature regulation.

---

## 2. Systems: Open, Closed, and Isolated

**[Content gap — expand on first study session of this chapter]**

Thermodynamic systems are classified by what can cross the boundary:

| System type | Matter exchange | Energy exchange | Example |
|-------------|-----------------|-----------------|---------|
| **Open** | Yes | Yes | Living organism, beaker open to air |
| **Closed** | No | Yes | Sealed gas cylinder (but can exchange heat) |
| **Isolated** | No | No | Ideal thermos, universe |

**MCAT relevance:** Living organisms are open systems — they exchange matter (food, O₂, CO₂, waste) and energy (heat, work) with their surroundings. The laws of thermodynamics still apply.

---

## 3. First Law of Thermodynamics

**[Content gap — expand on first study session of this chapter]**

**ΔU = Q − W**

- ΔU = change in internal energy of the system
- Q = heat added TO the system (positive when heat flows in)
- W = work done BY the system (positive when system pushes outward, expands)

**Sign convention table (MCAT standard):**

| | Q | W | ΔU |
|---|---|---|---|
| Heat added to system | + | | increases |
| Heat removed from system | − | | decreases |
| System does work on surroundings (expansion) | | + | decreases |
| Surroundings do work on system (compression) | | − | increases |

**Key scenarios:**
- **Isothermal process** (constant temperature): ΔU = 0 for ideal gas → Q = W.
- **Adiabatic process** (no heat exchange, Q = 0): ΔU = −W. System does work entirely at expense of internal energy.
- **Isochoric/isovolumetric process** (constant volume): W = 0 → ΔU = Q.
- **Isobaric process** (constant pressure): W = PΔV.

**MCAT tip:** The first law is just conservation of energy applied to thermodynamic systems. Internal energy can only change by adding/removing heat or doing/having work done.

> Cross-reference: `research/GenChem/Ch07_Thermochemistry.md` for enthalpy (H = U + PV), Hess's law, and bond energies — chemistry-side first law applications.

---

## 4. Second Law of Thermodynamics

**[Content gap — expand on first study session of this chapter]**

**The entropy of an isolated system always increases (or stays the same) in any spontaneous process.**

**ΔS_universe ≥ 0** (for any real process; = 0 only for reversible processes)

**Entropy (S)** is a measure of disorder or the number of available microstates. More disordered arrangements have higher entropy.

Key concepts:
- Heat spontaneously flows from hot to cold (never the reverse spontaneously).
- You cannot convert heat completely into work without any waste heat (Kelvin's statement).
- No process can be 100% efficient.

**Entropy in biological context:**
- Protein folding decreases the entropy of the protein chain — this is thermodynamically unfavorable and must be driven by other factors (hydrophobic effect, solvent entropy gain).
- ATP hydrolysis increases entropy of the system — drives non-spontaneous reactions.

### Heat Engines

A heat engine converts heat into work by operating between a hot reservoir (T_H) and a cold reservoir (T_C).

**Efficiency of any heat engine:**

e = W_out / Q_H = 1 − (Q_C / Q_H)

Where Q_H = heat absorbed from hot reservoir, Q_C = heat rejected to cold reservoir, W_out = net work output.

**Carnot efficiency (maximum possible for given temperatures):**

**e_Carnot = 1 − (T_C / T_H)** (temperatures in Kelvin)

This is the theoretical maximum. Real engines are always less efficient due to irreversibilities (friction, turbulence, heat loss).

**MCAT insight:** Carnot efficiency tells you the best possible performance. Increasing T_H or decreasing T_C improves efficiency. A heat engine can never be 100% efficient unless T_C = 0 K (absolute zero, unattainable).

**MCAT relevance of heat engines:** The heart as a pump, cellular respiration as an energy converter, and refrigerators (reverse heat engines) are all tested in the context of thermodynamic efficiency.

---

## 5. Connecting Thermodynamics to Chemistry and Biology

**[Content gap — expand on first study session of this chapter]**

The physics thermodynamics concepts in this chapter underpin the chemistry-side content in Gen Chem:

- **ΔG = ΔH − TΔS** connects enthalpy (first law) and entropy (second law) to spontaneity.
- Spontaneous reactions increase entropy of the universe (ΔG < 0 ↔ ΔS_universe > 0).
- ATP synthesis in the mitochondria couples a spontaneous process (proton gradient) to a non-spontaneous process (ATP synthesis) — thermodynamic coupling.

> Cross-reference: `research/GenChem/Ch07_Thermochemistry.md` for full thermochemistry content (ΔH, ΔG, ΔS in chemical context, Gibbs free energy, Hess's law, standard state).

---

## Quick Reference

**First Law:** ΔU = Q − W (heat IN is positive, work BY system is positive)

**Key processes:**
- Isothermal: ΔU = 0, Q = W
- Adiabatic: Q = 0, ΔU = −W
- Isochoric: W = 0, ΔU = Q

**Second Law:** ΔS_universe ≥ 0 always

**Carnot efficiency:** e_max = 1 − T_C/T_H (Kelvin!)

**Specific heat:** Q = mcΔT
