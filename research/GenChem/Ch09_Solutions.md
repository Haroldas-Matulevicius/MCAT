# CP Gen Chem Chapter 9 — Solutions

Scope: Nature of solutions; solute/solvent; concentration units; dilution; solubility & Ksp; common-ion effect; selective precipitation; complex ion formation; colligative properties (vapor pressure / Raoult's law, BP elevation, FP depression, osmotic pressure).

**Section:** Chemical/Physical (CP)
**Book:** Kaplan General Chemistry — Chapter 9
**AAMC FC mapping:** FC5A (solutions portion)
**Yield:** HIGH — colligative properties + Ksp + dilution math show up across CP and BB.

---

## 1. Nature of Solutions

A **solution** is a homogeneous mixture: solute dissolved in solvent.

**"Like dissolves like":** Polar solvents (water) dissolve polar/ionic solutes; nonpolar solvents (hexane) dissolve nonpolar solutes. This follows from IMF compatibility — solute-solvent interactions must approximate the strength of solute-solute and solvent-solvent interactions.

**Saturation:**
- **Unsaturated:** less than equilibrium amount of solute dissolved.
- **Saturated:** at equilibrium with undissolved solute (Q = Ksp for ionic compounds).
- **Supersaturated:** metastable; more solute dissolved than equilibrium allows. A small disturbance (seed crystal, shock) precipitates excess solute.

---

## 2. Concentration Units

| Unit | Definition | When Used |
|------|-----------|-----------|
| **Molarity (M)** | mol solute / L solution | Most common. Default for MCAT. |
| **Molality (m)** | mol solute / kg solvent | Colligative properties. Does NOT change with temperature. |
| **Mole fraction (X)** | mol component / total mol all components | Raoult's law, gas mixtures. |
| **Mass percent (w/w%)** | (mass solute / mass solution) x 100 | Labels on commercial reagent bottles. |
| **ppm / ppb** | parts per million / billion | Environmental chemistry, trace concentrations. |
| **Normality (N)** | equivalents / L (= M × n) | Polyprotic acids, multi-electron redox. See Ch04. |

**Molarity vs. Molality:** Molarity uses volume of solution (which changes with temperature because liquids expand/contract). Molality uses mass of solvent (which is temperature-independent). For dilute aqueous solutions, they're numerically very similar because 1 L water ≈ 1 kg.

---

## 3. Dilution

> **M1V1 = M2V2**

The total moles of solute don't change when you dilute -- you're just adding solvent.

**Worked example:** You have 50 mL of 6 M HCl and want to make 2 M HCl. How much total solution do you need?

(6)(50) = (2)(V2) → V2 = 150 mL total volume.

So you add 100 mL of water to the 50 mL of concentrated acid.

**Safety note the MCAT may reference:** Always add acid to water, not water to acid ("do as you oughta, add acid to water"). Adding water to concentrated acid can cause violent boiling and spattering due to the exothermic dissolution.

---

## 4. Solubility and Ksp

### Solubility Product (Ksp)

For a sparingly soluble salt dissolving in water:

**AgCl(s) ↔ Ag+(aq) + Cl-(aq)**

**Ksp = [Ag+][Cl-]**

Note: the solid is NOT included in the expression (activity of a pure solid = 1).

For a salt like Ca3(PO4)2:

Ca3(PO4)2 ↔ 3Ca2+ + 2PO4^3-

**Ksp = [Ca2+]^3 [PO4^3-]^2**

### Calculating Solubility from Ksp

**Worked example:** Ksp of AgCl = 1.8 x 10^-10. Find the molar solubility.

Let s = molar solubility (mol/L of AgCl that dissolves). [Ag+] = s, [Cl-] = s.

Ksp = s^2 = 1.8 x 10^-10 → s ≈ 1.3 x 10^-5 M.

**Worked example:** Ksp of PbI2 = 9.8 x 10^-9. Find molar solubility.

PbI2 ↔ Pb2+ + 2I-. [Pb2+] = s, [I-] = 2s.

Ksp = (s)(2s)^2 = 4s^3 → s = (Ksp/4)^(1/3) ≈ 1.4 x 10^-3 M.

**MCAT shortcut:** You can compare solubilities of salts with the SAME stoichiometry (like AgCl vs. AgBr, both 1:1) by directly comparing Ksp values. Higher Ksp = more soluble. But you CANNOT compare salts of different stoichiometries (AgCl vs. PbI2) by Ksp alone -- you must calculate actual solubility.

### Ion Product (Q_sp) vs Ksp

- Q_sp < Ksp: unsaturated, more salt can dissolve
- Q_sp = Ksp: saturated, equilibrium
- Q_sp > Ksp: supersaturated, precipitation occurs

### Common-Ion Effect

Adding a common ion DECREASES solubility. This is Le Chatelier's principle in action.

**Example:** AgCl in 0.1 M NaCl:

Ksp = [Ag+][Cl-] = (s)(0.1 + s) ≈ (s)(0.1)

s = Ksp / 0.1 = 1.8 x 10^-9 M.

Compare to 1.3 x 10^-5 M in pure water — that's a ~7000-fold decrease. The common-ion effect is powerful.

### Selective Precipitation

If a solution contains multiple ions, you can selectively precipitate one by adding an ion that forms an insoluble salt with it. The salt with the smallest Ksp precipitates first.

**Example:** Solution contains Cl- and I-. Slowly add Ag+. AgI (Ksp = 8.5 x 10^-17) precipitates first because it's far less soluble than AgCl (Ksp = 1.8 x 10^-10).

### Complex Ion Formation

Some metal ions form soluble complex ions with ligands (NH3, CN-, OH-). This INCREASES solubility by removing the free metal ion from solution, pulling the equilibrium to the right.

AgCl(s) ↔ Ag+ + Cl-
Ag+ + 2NH3 ↔ [Ag(NH3)2]+    (Kf is large)

Removing Ag+ shifts the dissolution equilibrium right — AgCl dissolves more in NH3 solution than in pure water.

---

## 5. Colligative Properties

**Colligative properties depend on the NUMBER of dissolved particles, not their identity.** A particle is a particle -- the solution doesn't care if it's Na+, glucose, or Cl-.

### The van't Hoff Factor (i)

**i = number of particles a solute produces in solution**

| Solute | i (ideal) | Notes |
|--------|----------|-------|
| Glucose (C6H12O6) | 1 | Molecular, doesn't dissociate |
| NaCl | 2 | Na+ and Cl- |
| CaCl2 | 3 | Ca2+ and 2 Cl- |
| Al2(SO4)3 | 5 | 2 Al3+ and 3 SO4^2- |
| Acetic acid (weak) | ~1 | Barely dissociates; treat as 1 |

**MCAT trap #1:** Forgetting to include i. A 0.1 m NaCl solution has an effective particle concentration of 0.2 m because NaCl fully dissociates into 2 ions.

**MCAT trap #2:** Using i = 2 for a weak electrolyte. Weak acids/bases barely dissociate, so i ≈ 1.

**MCAT trap #3:** Real solutions have i values slightly lower than ideal because of ion pairing. If "ideal" or "dilute," use the integer value.

### Boiling Point Elevation

**ΔT_b = i · K_b · m**

- K_b = ebullioscopic constant (water: 0.512 °C/m)
- m = molality
- Adding solute RAISES the boiling point

**Why?** Solute particles in the liquid phase lower the vapor pressure. You need a higher temperature to reach a vapor pressure of 1 atm.

### Freezing Point Depression

**ΔT_f = i · K_f · m**

- K_f = cryoscopic constant (water: 1.86 °C/m)
- Adding solute LOWERS the freezing point

**Why?** Solute particles disrupt crystal packing.

**Practical:** Road salt (NaCl) lowers FP of water. CaCl2 even better (i = 3).

**Worked example:** FP of 0.5 m NaCl?

ΔT_f = 2 × 1.86 × 0.5 = 1.86 °C. FP = 0 - 1.86 = **-1.86 °C**.

### Osmotic Pressure

**π = iMRT**

- π = osmotic pressure
- M = molarity
- R = 0.0821 L·atm/(mol·K)
- T = Kelvin

Osmotic pressure is the pressure needed to PREVENT osmosis (net solvent flow from dilute to concentrated side across a semipermeable membrane).

**Higher solute concentration = higher osmotic pressure.**

Biology connections:
- **Isotonic:** Same osmotic pressure as the cell. No net water movement. (0.9% NaCl = normal saline.)
- **Hypertonic:** Higher solute outside. Water flows OUT of cell. Cell crenates (shrivels).
- **Hypotonic:** Lower solute outside. Water flows INTO cell. Cell lyses (bursts).

**Worked example:** π of 0.15 M NaCl at 37°C (310 K)?

π = (2)(0.15)(0.0821)(310) ≈ **7.6 atm**.

### Vapor Pressure Lowering (Raoult's Law)

**P_solution = X_solvent · P°_solvent**

Adding a non-volatile solute lowers the vapor pressure of the solution because fewer solvent molecules are at the surface to evaporate.

For volatile solutes (two miscible liquids):

**P_total = X_A · P°_A + X_B · P°_B**

**Positive deviation from Raoult's law:** Interactions between A and B are WEAKER than A-A and B-B. Molecules escape more easily. Vapor pressure is HIGHER than predicted. Example: ethanol + hexane. Can form a **minimum-boiling azeotrope** (e.g., 95.6% ethanol/water).

**Negative deviation from Raoult's law:** Interactions between A and B are STRONGER (like H-bonding). Vapor pressure is LOWER than predicted. Example: acetone + chloroform. Can form a **maximum-boiling azeotrope**.

**MCAT relevance:** Azeotropes cannot be separated further by simple/fractional distillation alone.

---

## High-Yield Takeaways

1. **Like dissolves like.**
2. **M1V1 = M2V2** for dilution (moles conserved).
3. **Ksp:** product of ion concentrations; pure solids/liquids excluded.
4. **Common-ion effect:** decreases solubility (Le Chatelier).
5. **Colligative properties:** ΔT_b = iK_bm, ΔT_f = iK_fm, π = iMRT.
6. **van't Hoff factor i** = particles per formula unit; weak electrolytes ≈ 1.
7. **Raoult's law:** P_soln = X_solvent · P°. Deviations lead to azeotropes.

---

→ Acid-base & buffers: `CP_GC_Ch10_Acids_Bases.md`
→ Distillation & vapor pressure: `CP_OC_Ch12_Separations_Purifications.md`
→ Stoichiometry & molarity context: `CP_GC_Ch04_Compounds_Stoichiometry.md`
→ Osmosis in physiology: `BB_Ch08_Membranes.md`, `BB_Bio_Ch10_Homeostasis.md`
