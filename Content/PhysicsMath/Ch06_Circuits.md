# CP — Physics Ch 6: Circuits

Kaplan Physics Ch 6 | FC4C

> Electrochemical cells (galvanic/electrolytic), E°_cell, Nernst equation, Faraday's law → research/GenChem/Ch12_Electrochemistry.md

---

CURRENT:
- I = ΔQ/Δt (amperes = C/s)
- Conventional current: + to − (direction positive charges would flow; electrons flow opposite)

RESISTANCE:
- R = ρL/A (ρ = resistivity, L = length, A = cross-section area; Ω = ohms)
- Longer → more R; thicker → less R; higher resistivity material → more R

OHM'S LAW:
- V = IR (use V = IR for any single resistor; I = V/R_total for whole circuit)

POWER:
- P = IV = I²R = V²/R
- Series (same I): P ∝ R → largest R gets most power
- Parallel (same V): P ∝ 1/R → smallest R gets most power

SERIES CIRCUITS (one path):
- Same I everywhere: I₁ = I₂ = I₃
- Resistance adds: R_total = R₁ + R₂ + R₃
- Voltage divides proportional to R: V₁ = IR₁, V₂ = IR₂
- V_total = ΣV_i

PARALLEL CIRCUITS (multiple paths):
- Same V across each branch: V₁ = V₂ = V₃
- Reciprocal resistances: 1/R_total = 1/R₁ + 1/R₂
- Two resistors: R_total = (R₁·R₂)/(R₁+R₂) (product over sum shortcut)
- Adding any resistor in parallel DECREASES total R; total R < smallest individual R
- Current divides: I₁ = V/R₁, I₂ = V/R₂

RESISTORS VS CAPACITORS — OPPOSITE RULES:
- Series: R adds directly | C adds reciprocally (1/C_total = 1/C₁ + 1/C₂)
- Parallel: R adds reciprocally | C adds directly (C_total = C₁ + C₂)

KIRCHHOFF'S RULES (HIGH YIELD):
- KCL (Junction): ΣI_in = ΣI_out (charge conservation)
- KVL (Loop): ΣV = 0 around any closed loop (energy conservation)
  - Crossing battery − to +: gain (+EMF)
  - Crossing resistor in current direction: loss (−IR)
  - Crossing resistor against current: gain (+IR)

INTERNAL RESISTANCE & EMF:
- Real battery: V_terminal = ε − Ir
- Full circuit: I = ε/(R + r)
- Ideal battery: r = 0, V_terminal = ε

RC CIRCUITS:
- Time constant: τ = RC (seconds)
- Charging: Q(t) = Q_max(1 − e^(−t/RC)), current starts max (I₀ = V/R) and decays
  - At t = τ: 63% of max charge
  - At t = 5τ: ~99% charged (treat as fully charged)
- Discharging: Q(t) = Q₀e^(−t/RC), ~37% remains at t = τ
- Steady-state DC: capacitor = open circuit (no current through it)
- At t = 0 (uncharged capacitor): acts as short circuit (wire)

METERS:
- Ammeter: in SERIES; very LOW resistance (so it doesn't change current)
- Voltmeter: in PARALLEL; very HIGH resistance (so it draws no current)
- Ammeter in parallel → short circuit (wrong, damaging)
- Voltmeter in series → blocks current (wrong reading)

KEY TRAPS:
- Capacitors: series/parallel rules are REVERSED vs resistors
- Adding parallel resistors DECREASES total resistance
- Power in series: biggest R gets most (P = I²R). In parallel: smallest R gets most (P = V²/R)
- RC circuit at steady state: capacitor = open circuit, no current through it

Kaplan: Physics Ch 6
→ Deep dive: research/PhysicsMath/Ch06_Circuits.md
