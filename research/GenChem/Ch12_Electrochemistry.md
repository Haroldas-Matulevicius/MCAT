# CP Gen Chem Chapter 12 — Electrochemistry

Scope: Galvanic (voltaic) cells; electrolytic cells; standard reduction potentials; cell potential calculation; Nernst equation; concentration cells; ΔG° = -nFE°; Faraday's law of electrolysis.

**Section:** Chemical/Physical (CP)
**Book:** Kaplan General Chemistry — Chapter 12
**AAMC FC mapping:** FC4C (electrochemistry portion)
**Yield:** HIGH — galvanic vs electrolytic cells, sign conventions, and Nernst reasoning appear constantly.

> Note: Electrostatics, magnetism, and electrical circuits live in physics legacy `CP_Phy_Circuits.md`.

---

## 1. Galvanic (Voltaic) Cells

A **galvanic cell** converts chemical energy into electrical energy through a **spontaneous** redox reaction. This is the "regular battery" you use in everyday life.

**Key identifiers:**
- **Spontaneous** (reaction proceeds without external energy input)
- **ΔG < 0**
- **E_cell > 0**
- **Anode is negative**, cathode is positive

**Cell anatomy:**
- **Anode:** Oxidation occurs here. Electrons leave the anode. The anode loses mass as metal atoms are oxidized into solution.
- **Cathode:** Reduction occurs here. Electrons arrive at the cathode. The cathode gains mass as metal ions in solution are reduced and deposited.
- **Salt bridge:** Allows ions to flow between half-cells to maintain electrical neutrality. Cations migrate toward the cathode compartment; anions migrate toward the anode compartment.
- **External wire:** Electrons flow from anode to cathode through the wire. Conventional current flows from cathode to anode through the wire.

**Memory aid:** **An Ox** (anode = oxidation), **Red Cat** (reduction = cathode). Also: alphabetically, A comes before C, and O comes before R.

---

## 2. Electrolytic Cells

An **electrolytic cell** uses electrical energy to drive a **non-spontaneous** reaction. Think electrolysis of water, electroplating, purifying metals.

**Key identifiers:**
- **Non-spontaneous** (requires external voltage source)
- **ΔG > 0**
- **E_cell < 0**
- **Anode is positive**, cathode is negative

The processes at the electrodes are the same: oxidation still happens at the anode, reduction still happens at the cathode. The "An Ox, Red Cat" mnemonic works for both cell types. What changes is the sign convention on the electrodes.

---

## 3. Standard Reduction Potentials

The **standard reduction potential** (E°) is measured for each half-reaction written as a reduction. The table is always given on the MCAT. A more positive E° means the species has a greater tendency to be reduced.

**How to use the table:**
1. Identify which species gets **reduced** (higher E° = better oxidizing agent, wants electrons).
2. Identify which species gets **oxidized** (lower E° = better reducing agent, gives up electrons).
3. The species with the more positive reduction potential is the cathode (reduction).
4. The species with the more negative reduction potential is the anode (oxidation).

**Critical rule:** When you reverse a half-reaction (to write it as oxidation), you flip the sign of E° for conceptual purposes, but when calculating cell potential, use the formula below -- do NOT flip and add.

---

## 4. Cell Potential Calculation

> **E°_cell = E°_cathode - E°_anode**

Always cathode minus anode, using the reduction potentials as given in the table. Do not reverse signs manually and add -- just subtract.

**Worked example:** Given:
- Cu²⁺ + 2e⁻ → Cu, E° = +0.34 V
- Zn²⁺ + 2e⁻ → Zn, E° = -0.76 V

Cu has the higher reduction potential, so Cu²⁺ is reduced (cathode). Zn is oxidized (anode).

E°_cell = (+0.34) - (-0.76) = **+1.10 V**

Positive cell potential confirms this is spontaneous as a galvanic cell.

**MCAT tip:** If your calculated E°_cell comes out negative, either you have the cathode and anode backwards, or the reaction is non-spontaneous as written (electrolytic conditions).

**Important:** E° is intensive — doubling coefficients does NOT change E°. If Cu²⁺ + 2e⁻ → Cu has E° = +0.34 V, then 2Cu²⁺ + 4e⁻ → 2Cu also has E° = +0.34 V.

---

## 5. The Nernst Equation

> **E = E° - (RT/nF) · ln Q**

At 25°C, this simplifies to:

> **E = E° - (0.0592/n) · log Q**

where:
- n = number of moles of electrons transferred
- F = Faraday's constant = 96,485 C/mol (≈ 10⁵ for estimation)
- Q = reaction quotient (products/reactants)

**What this tells you:** The cell potential changes as concentrations deviate from standard conditions.
- Q < 1 (more reactants): E > E° (cell potential increases)
- Q > 1 (more products): E < E° (cell potential decreases)
- At equilibrium: Q = K, E = 0 (battery dead)

**MCAT approach:** You rarely need to compute Nernst numerically. Understand the direction:
- ↑ reactant → ↑ E
- ↑ product → ↓ E
- At equilibrium, E = 0 and Q = K.

---

## 6. Concentration Cells

A **concentration cell** is a galvanic cell where both half-cells have the same electrode material but different ion concentrations. E°_cell = 0 (same half-reactions), but E_cell is not zero because Q is not 1.

The cell generates voltage purely from the concentration difference.
- **More concentrated side** is the cathode (reduction occurs there, depositing metal to reduce ion concentration).
- **More dilute side** is the anode (oxidation occurs there, dissolving metal to increase ion concentration).

The cell runs until concentrations equalize → Q = 1 → E = 0.

---

## 7. Free Energy and Cell Potential

> **ΔG° = -nFE°**

This connects thermodynamics to electrochemistry.

| Condition | ΔG | E_cell | Reaction |
|-----------|------|--------|----------|
| Spontaneous (galvanic) | Negative | Positive | Proceeds forward |
| Equilibrium | Zero | Zero | No net reaction |
| Non-spontaneous (electrolytic) | Positive | Negative | Requires external energy |

**Notice the signs are always opposite.** Positive E means negative ΔG, and vice versa. The factor -nF just converts between energy units and voltage.

You can also connect to equilibrium:

> **ΔG° = -RT · ln K**

So: **-nFE° = -RT ln K**, which gives **E° = (RT/nF) ln K**. A large positive E° means a large K (products strongly favored at equilibrium).

---

## 8. Faraday's Law of Electrolysis

This is about calculating how much substance is deposited or consumed during electrolysis.

> **moles of electrons = It / F**

where I is current (Amperes), t is time (seconds), F is Faraday's constant.

**Step-by-step approach:**
1. Calculate total charge: Q = It (coulombs)
2. Convert to moles of electrons: mol e⁻ = Q / F
3. Use stoichiometry of the half-reaction (e.g., Cu²⁺ + 2e⁻ → Cu means 2 mol e⁻ per mol Cu).
4. Convert moles of substance to grams using molar mass.

**Worked example:** How many grams of Cu are deposited when 5 A flows for 3860 seconds?
- Q = It = 5 × 3860 = 19,300 C
- mol e⁻ = 19,300 / 96,500 = 0.2 mol e⁻
- Cu²⁺ + 2e⁻ → Cu, so mol Cu = 0.2/2 = 0.1 mol
- Mass = 0.1 × 63.5 g/mol = **6.35 g**

---

## 9. MCAT Traps

### Trap 1: Galvanic vs. Electrolytic Anode/Cathode Signs

| | Galvanic Cell | Electrolytic Cell |
|---|---|---|
| Anode | Negative (-) | Positive (+) |
| Cathode | Positive (+) | Negative (-) |
| Oxidation at anode? | Yes | Yes |
| Reduction at cathode? | Yes | Yes |

**An Ox, Red Cat** always applies. What changes is the **charge sign** on the electrodes.

**How to avoid the trap:** Don't memorize electrode signs. Reason from first principles — identify which species is oxidized/reduced, then assign anode/cathode.

### Trap 2: E_cell Calculation Sign Error

Always use E°_cell = E°_cathode - E°_anode with both values directly from the reduction potential table. Don't flip and add — just subtract.

### Trap 3: Standard Reduction Potentials Are Intensive

Doubling coefficients in a half-reaction does **not** change E°.

### Trap 4: Current Direction vs. Electron Flow

Conventional current flows from + to - (high to low potential) through the external circuit. Electrons actually flow from - to + (anode to cathode in a galvanic cell). Read carefully.

---

## High-Yield Takeaways

1. **An Ox, Red Cat** — anode is oxidation, cathode is reduction (regardless of cell type).
2. **Galvanic:** spontaneous, E > 0, ΔG < 0, anode = (-), cathode = (+).
3. **Electrolytic:** non-spontaneous, E < 0, ΔG > 0, anode = (+), cathode = (-).
4. **E°_cell = E°_cathode − E°_anode** (always subtract; don't flip-and-add).
5. **Nernst:** ↑[reactant] → ↑E; ↑[product] → ↓E; at eq, E = 0.
6. **ΔG° = -nFE°** — signs always opposite.
7. **Faraday's law:** mol e⁻ = It/F; convert via half-reaction stoichiometry.

---

## Quick Reference Equations

| Equation | Use |
|---|---|
| E°_cell = E°_cathode - E°_anode | Cell potential |
| E = E° - (0.0592/n) log Q | Nernst @ 25°C |
| ΔG° = -nFE° | Free energy ↔ EMF |
| ΔG° = -RT ln K | Free energy ↔ K |
| mol e⁻ = It/F | Electrolysis stoichiometry |

---

→ Redox half-reaction balancing: `CP_GC_Ch11_Redox.md`
→ Thermodynamics & ΔG: `CP_GC_Ch07_Thermochemistry.md`
→ Equilibrium & Q vs K: `CP_GC_Ch06_Equilibrium.md`
→ Electrostatics & circuits: `CP_Phy_Circuits.md`
