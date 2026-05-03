# Physics & Math Chapter 6 — Circuits

Scope: Current, resistance, Ohm's law, resistivity; series and parallel circuits; Kirchhoff's laws (HIGH YIELD); power dissipation; capacitors in circuits; RC circuits; EMF and internal resistance; ammeters and voltmeters.

**Section:** Chemical/Physical (CP) — Physics & Math
**Book:** Kaplan Physics and Math Strategies 2024 — Chapter 6
**AAMC FC mapping:** FC4C (Electrochemistry, electrical circuits, and magnetism)
**Yield:** Very high. Circuits and Kirchhoff's laws appear on nearly every MCAT.

> **Note on electrochemistry:** Galvanic/electrolytic cells, standard reduction potentials, E°_cell, Nernst equation, Faraday's law of electrolysis, and concentration cells are NOT in this chapter. That content belongs in `research/GenChem/Ch12_Electrochemistry.md`. Cross-reference Gen Chem Ch 12 for all electrochemical content.

---

## 1. Current

**I = ΔQ/Δt**

**Current** = rate of charge flow. Units: **Amperes (A)** = Coulombs per second.

By convention, current flows from high potential (+) to low potential (−). This is conventional current — the direction positive charges would move. Electrons actually flow the opposite way (from − to +), but the MCAT uses conventional current unless explicitly stated otherwise.

---

## 2. Resistance

**R = ρL/A**

Where ρ = **resistivity** (intrinsic property of the material, units: Ω·m), L = length, A = cross-sectional area.

- Longer wire → more resistance
- Thicker wire → less resistance
- Higher resistivity material → more resistance

Units: **Ohms (Ω)**

**Resistivity vs resistance:** Resistivity (ρ) is an intrinsic material property (like density). Resistance (R) depends on the material AND the geometry.

---

## 3. Ohm's Law

**V = IR**

The voltage drop across a resistor equals current through it × resistance. **Single most used equation in circuit problems.** Know it cold and know how to rearrange: I = V/R and R = V/I.

---

## 4. Power

**P = IV = I²R = V²/R**

All three forms come from combining P = IV with V = IR.

**Which form to use:**
- Same current through all elements (series) → use **P = I²R** (power ∝ R; largest R dissipates most power in series)
- Same voltage across all elements (parallel) → use **P = V²/R** (power ∝ 1/R; smallest R dissipates most power in parallel)

---

## 5. Series Circuits

Components connected end-to-end, single path for current.

**Rules:**
- **Current is the same** through every component: I_total = I₁ = I₂ = I₃
- **Resistances add:** R_total = R₁ + R₂ + R₃
- **Voltage divides** proportional to resistance: V₁ = IR₁, V₂ = IR₂
- V_total = V₁ + V₂ + V₃

**Worked example — voltage divider:** 12 V battery, 3 Ω and 6 Ω in series.
- R_total = 9 Ω
- I = 12/9 = 4/3 A
- V across 3 Ω: (4/3)(3) = 4 V
- V across 6 Ω: (4/3)(6) = 8 V
- Check: 4 + 8 = 12 V ✓

---

## 6. Parallel Circuits

Components connected across the same two nodes, multiple paths for current.

**Rules:**
- **Voltage is the same** across every branch: V_total = V₁ = V₂ = V₃
- **Reciprocal resistances add:** 1/R_total = 1/R₁ + 1/R₂ + 1/R₃
- **Current divides** inversely proportional to resistance: I₁ = V/R₁, I₂ = V/R₂
- I_total = I₁ + I₂ + I₃

**Key fact:** Adding a resistor in parallel always **decreases** total resistance. Total R < smallest individual R in the parallel combination.

**Two-resistor shortcut:** R_total = (R₁ × R₂)/(R₁ + R₂) — product over sum. Faster than reciprocal method for two resistors.

**Resistors vs capacitors — the reversal:**

| | Resistors | Capacitors |
|---|---|---|
| **Series** | Add directly: R_total = R₁ + R₂ | Add reciprocals: 1/C_total = 1/C₁ + 1/C₂ |
| **Parallel** | Add reciprocals: 1/R_total = 1/R₁ + 1/R₂ | Add directly: C_total = C₁ + C₂ |

Rules are **exactly reversed**. This is a major MCAT trap. Intuition for capacitors in parallel: effectively bigger plate area → C increases. In series: effectively thicker gap → C decreases.

---

## 7. Kirchhoff's Laws — HIGH YIELD

### Junction Rule (KCL — Conservation of Charge)

**ΣI_in = ΣI_out** at any junction.

Charge does not pile up at a node. What flows in must flow out.

### Loop Rule (KVL — Conservation of Energy)

**ΣV = 0 around any closed loop.**

What you gain from batteries, you lose across resistors.

**How to apply the loop rule:**
1. Pick a direction to traverse the loop (CW or CCW — doesn't matter).
2. Crossing a battery from − to +: **voltage gain** (+EMF).
3. Crossing a resistor in the direction of current: **voltage drop** (−IR).
4. Crossing a resistor opposite to current direction: voltage gain (+IR).
5. Set sum = 0 and solve.

**MCAT use:** Kirchhoff's laws are how you solve any multi-loop circuit. For a single loop, KVL alone suffices. For multiple loops with multiple unknowns, use both KCL (for currents at junctions) and KVL (for loops).

---

## 8. Internal Resistance and EMF

A real battery has **internal resistance (r)**. The **EMF (ε)** is the ideal voltage with no internal resistance. The actual **terminal voltage** is:

**V_terminal = ε − Ir**

Where I = current drawn from battery. As current increases, more voltage is wasted inside the battery.

**Full circuit (battery + external load R):**

**I = ε/(R + r)**

**MCAT tip:** "Ideal battery" → r = 0, V_terminal = EMF. "Real battery" or given internal resistance → use equations above.

When the battery is short-circuited (R = 0): I_max = ε/r. Terminal voltage drops to zero — all EMF is lost across internal resistance.

---

## 9. Capacitors in Circuits

### RC Circuits

A resistor-capacitor circuit has a **time constant:**

**τ = RC** (units: seconds — verify: Ω × F = (V/A)(C/V) = C/A = s)

**Charging** (capacitor connected to battery through resistor):
- Charge builds up exponentially: Q(t) = Q_max(1 − e^(−t/RC))
- Current starts at maximum I₀ = V/R and decays: I(t) = I₀e^(−t/RC)
- At t = RC: capacitor has ~63% of final charge.
- At t = 5RC: capacitor is ~99% charged (treat as fully charged).

**Discharging** (capacitor releases charge through resistor):
- Charge decays: Q(t) = Q₀e^(−t/RC)
- Current decays: I(t) = I₀e^(−t/RC)
- At t = RC: ~37% of original charge remains.

**MCAT tip:** You won't need to calculate exact exponential values. Know: the shape of the curves (exponential charge-up, exponential decay), the meaning of τ = RC, and that larger R or larger C means the circuit charges/discharges more slowly.

**Fully charged capacitor in a DC circuit:** Acts as an **open circuit** (no current flows through the capacitor branch). All voltage appears across the capacitor.

**Uncharged capacitor at t = 0:** Acts as a **short circuit** (wire). Capacitor initially has zero voltage across it.

---

## 10. Ammeters and Voltmeters

**Ammeter** — measures current:
- Connected in **series** with the component.
- Must have very **low internal resistance** (ideally zero) so it doesn't significantly change the current.

**Voltmeter** — measures voltage:
- Connected in **parallel** with the component.
- Must have very **high internal resistance** (ideally infinite) so it draws negligible current.

**MCAT trap:** Ammeter in parallel = short circuit (damages the meter, large current spike). Voltmeter in series = essentially open circuit (blocks current, reads nearly the full battery voltage instead of the component voltage).

---

## MCAT Strategy Summary

### Circuit Problem Approach

1. **Identify series vs parallel.** In series: single path. In parallel: multiple paths between same two nodes.
2. **Find total resistance.** Add series resistors directly. Use reciprocal method (or product/sum for two) for parallel.
3. **Find total current** from the battery: I = V/R_total.
4. **Work outward** to individual components. For series: all have same I. For parallel: all have same V.
5. **For multi-loop circuits:** Set up KCL at junctions, KVL for each loop. Solve the system.

### Pattern Recognition

| Trigger | Action |
|---------|--------|
| "Same wire connecting two resistors" | Series — same current through both. |
| "Connected across the same two points" | Parallel — same voltage across both. |
| "Add another resistor in parallel" | Total resistance DECREASES. Total current INCREASES. |
| "Which resistor dissipates most power in series?" | Largest R (P = I²R, same I). |
| "Which resistor dissipates most power in parallel?" | Smallest R (P = V²/R, same V). |
| "Capacitor in DC circuit, steady state" | Open circuit. No current through capacitor. |
| "Capacitor at t=0 (uncharged)" | Short circuit. Acts like a wire. |
| "Real vs ideal battery" | Real: V_terminal = ε − Ir (drops under load). |

### Common Traps

1. **Series vs parallel resistance rules for capacitors are REVERSED.** Series C → reciprocals. Parallel C → add directly.
2. **Adding resistors in parallel always decreases total resistance.** Total < smallest individual.
3. **Power in series vs parallel:** Largest R gets most power in series; smallest R gets most power in parallel.
4. **Ammeter in parallel / voltmeter in series:** Both wrong configurations — know the correct connections.
5. **KVL sign conventions:** Going through a battery from − to + is a gain. Going through a resistor in current direction is a loss.

### Quick Reference

**I = ΔQ/Δt | R = ρL/A | V = IR**
**P = IV = I²R = V²/R**
**Series:** R_total = R₁ + R₂ | 1/C_total = 1/C₁ + 1/C₂
**Parallel:** 1/R_total = 1/R₁ + 1/R₂ | C_total = C₁ + C₂
**KCL:** ΣI_in = ΣI_out | **KVL:** ΣV = 0
**V_terminal = ε − Ir | I = ε/(R + r)**
**RC time constant:** τ = RC (63% charged at t = τ; 5τ ≈ fully charged)
