# FC5A: Acid-Base Chemistry (Gen Chem / Biochem)

**Section:** Chem/Phys (CP)
**Yield:** THE single highest-yield gen chem topic. Expect 5-8 questions touching acid-base reasoning on any given exam. This stuff cross-links into biochem (amino acid charge, enzyme kinetics), biology (blood buffering, renal physiology), and even P/S (drug pharmacology). Master it cold.

---

## 1. Definitions of Acids and Bases

### Bronsted-Lowry (the default on MCAT)

- **Acid** = proton (H+) donor
- **Base** = proton (H+) acceptor

This is the definition you'll use 90% of the time. When the MCAT says "acid" or "base" without further context, they mean Bronsted-Lowry.

**Conjugate pairs** always differ by exactly one H+:
- HF donates a proton --> F- is its **conjugate base**
- NH3 accepts a proton --> NH4+ is its **conjugate acid**

Key relationship: **the stronger the acid, the weaker its conjugate base** (and vice versa). HCl is a strong acid, so Cl- is an absolutely terrible base -- it has zero tendency to grab a proton back. Acetic acid is a weak acid, so acetate (CH3COO-) is a decent (but still weak) base.

### Lewis (the broader definition)

- **Acid** = electron pair acceptor
- **Base** = electron pair donor

Lewis encompasses everything Bronsted-Lowry covers and then some. Use the Lewis definition when the question involves:
- **Metal coordination chemistry** (Fe3+ accepting lone pairs from water or CN-)
- **BF3, AlCl3** -- classic Lewis acids with empty orbitals, no H+ involved
- **Nucleophile/electrophile reasoning in orgo** -- a nucleophile IS a Lewis base; an electrophile IS a Lewis acid

**MCAT trap:** A question might describe a reaction where no proton transfer occurs and ask you to identify the acid. If you're stuck in Bronsted-Lowry mode, you'll miss it. Any species accepting an electron pair is a Lewis acid.

### Quick Decision Rule

| Situation | Use This Definition |
|-----------|-------------------|
| Proton transfer reaction | Bronsted-Lowry |
| Metal ion in solution | Lewis |
| BF3, AlCl3, or empty-orbital species | Lewis |
| Nucleophilic attack in orgo | Lewis |
| Buffer / titration / pH problem | Bronsted-Lowry |

---

## 2. Strong vs. Weak Acids and Bases

### Strong Acids -- Memorize These Six

| Acid | Formula |
|------|---------|
| Hydrochloric acid | HCl |
| Hydrobromic acid | HBr |
| Hydroiodic acid | HI |
| Sulfuric acid | H2SO4 |
| Nitric acid | HNO3 |
| Perchloric acid | HClO4 |

**100% dissociation.** If you dissolve 0.01 M HCl, you get 0.01 M H+ and 0.01 M Cl-. No equilibrium expression needed -- there's no "reverse reaction" to speak of.

Memory trick: "**H**ave **C**ourage, **HB**r **HI** -- **H**ot **S**ummer **N**ights **O**utside, **H**ow **Cl**ear **O**h **4**real." Or just brute-force memorize six acids. You'll see them constantly.

Note on H2SO4: The first proton is strong (full dissociation). The second proton is weak (Ka2 ~ 0.012). For MCAT purposes, unless they specifically ask about the second dissociation, treat sulfuric as donating 2 H+ per molecule in dilute solution.

### Strong Bases

Group 1 metal hydroxides: **NaOH, KOH, LiOH**. Also Group 2 hydroxides like Ba(OH)2 and Ca(OH)2 (though Ca(OH)2 has limited solubility). These dissociate completely: NaOH --> Na+ + OH-.

### Weak Acids and Bases -- Equilibria

A **weak acid** only partially dissociates:

HA <--> H+ + A-

The equilibrium constant for this is **Ka** (acid dissociation constant):

**Ka = [H+][A-] / [HA]**

A **weak base** partially accepts protons from water:

B + H2O <--> BH+ + OH-

**Kb = [BH+][OH-] / [B]**

### The Ka-Kb Relationship

For any conjugate acid-base pair:

**Ka x Kb = Kw = 1.0 x 10^-14 (at 25 C)**

This means: **pKa + pKb = 14**

Why this matters: if they give you the Kb of a base, you can find the Ka of its conjugate acid (and vice versa). This shows up constantly in buffer and titration problems.

### What Ka Tells You

| Ka Value | pKa | Acid Strength | Example |
|----------|-----|---------------|---------|
| ~10^-1 | ~1 | Moderately strong | HSO4- (second proton) |
| ~10^-5 | ~5 | Weak | CH3COOH (acetic acid, pKa 4.76) |
| ~10^-10 | ~10 | Very weak | NH4+ (pKa 9.25) |
| ~10^-14 | ~14 | Essentially non-acidic | Water |

**Larger Ka = smaller pKa = stronger acid = more dissociation.** Make sure you never confuse the direction. The MCAT loves to list four compounds with different pKa values and ask which is the strongest acid -- it's the one with the LOWEST pKa.

---

## 3. pH Calculations

### The Core Equations

- **pH = -log[H+]**
- **pOH = -log[OH-]**
- **pH + pOH = 14** (at 25 C)
- **pKa = -log(Ka)**
- **pKb = -log(Kb)**
- **[H+][OH-] = Kw = 1.0 x 10^-14**

### Estimating pH Without a Calculator

This is a critical MCAT skill. You will NOT have a calculator. Memorize these log approximations:

| Value | log(value) | How to remember |
|-------|-----------|-----------------|
| 1 | 0 | Exact |
| 2 | 0.3 | "log 2 is point 3" -- memorize this one cold |
| 3 | ~0.5 | Slightly less than 0.5, but 0.5 is close enough |
| 4 | 0.6 | = 2 x log 2 = 2(0.3) |
| 5 | 0.7 | = log(10/2) = 1 - 0.3 |
| 6 | ~0.78 | Use 0.8 |
| 7 | ~0.85 | Rarely needed |
| 8 | 0.9 | = 3 x log 2 |

**The Master Trick for pH:** Express [H+] in scientific notation, then use:

**pH = -log(A x 10^-n) = n - log(A)**

Worked example: [H+] = 3 x 10^-5 M
- pH = 5 - log(3) = 5 - 0.5 = **4.5**

Worked example: [H+] = 6 x 10^-3 M
- pH = 3 - log(6) = 3 - 0.78 ~ **2.2**

Worked example: [H+] = 2 x 10^-8 M
- pH = 8 - log(2) = 8 - 0.3 = **7.7** (slightly basic -- makes sense, less H+ than pure water)

**Going backwards (pH to [H+]):**

pH = 4.3 --> [H+] = 10^-4.3 = 10^-4 x 10^-0.3

Since 10^-0.3 = 1/10^0.3 = 1/2 = 0.5:

[H+] = 5 x 10^-5 M

This reverse calculation uses the fact that **10^0.3 ~ 2**, so **10^-0.3 ~ 0.5**.

### Strong Acid/Base pH -- Direct Calculation

For strong acids, [H+] = concentration of the acid (assuming monoprotic). No equilibrium needed.

- 0.001 M HCl --> [H+] = 10^-3 --> pH = 3
- 0.05 M NaOH --> [OH-] = 0.05 --> pOH = -log(5 x 10^-2) = 2 - 0.7 = 1.3 --> pH = 12.7

### Weak Acid pH -- ICE Table Approach

For weak acid HA with initial concentration C and dissociation constant Ka:

Set up: HA <--> H+ + A-

| | HA | H+ | A- |
|---|---|---|---|
| I | C | 0 | 0 |
| C | -x | +x | +x |
| E | C-x | x | x |

Ka = x^2 / (C - x)

**The 5% approximation:** If Ka is small relative to C (rule of thumb: C/Ka > 100), then C - x ~ C, and:

**x = [H+] = sqrt(Ka x C)**

Worked example: What is the pH of 0.1 M acetic acid (Ka = 1.8 x 10^-5)?

- Check: C/Ka = 0.1 / 1.8 x 10^-5 ~ 5500. Approximation is valid.
- [H+] = sqrt(1.8 x 10^-5 x 0.1) = sqrt(1.8 x 10^-6)
- sqrt(1.8) ~ 1.3, sqrt(10^-6) = 10^-3
- [H+] ~ 1.3 x 10^-3
- pH = 3 - log(1.3) ~ 3 - 0.1 = **2.9**

This is a bread-and-butter MCAT calculation. Practice it until it's automatic.

### Polyprotic Acids

Acids that can donate more than one proton: H3PO4, H2SO4, H2CO3, citric acid.

Key facts:
- Each successive dissociation is **harder** (Ka1 >> Ka2 >> Ka3)
- For pH calculations of the original solution, **only Ka1 matters** -- the second and third dissociations contribute negligible H+
- The **intermediate species** (like HCO3- or H2PO4-) are **amphoteric** -- they can act as either acid or base depending on what they're paired with

The pH of an amphoteric intermediate in a diprotic system:

**pH = (pKa1 + pKa2) / 2**

This shows up for amino acid isoelectric points too (average of the two pKa values flanking the zwitterion form).

---

## 4. Henderson-Hasselbalch Equation

This is the single most important equation in acid-base chemistry for the MCAT.

### The Equation

**pH = pKa + log([A-] / [HA])**

Where:
- [A-] = concentration of conjugate base
- [HA] = concentration of weak acid
- pKa = pKa of the weak acid

### Key Insights

**When [A-] = [HA]:** log(1) = 0, so **pH = pKa**. This is the half-equivalence point of a titration. It's also where buffer capacity is maximized.

**When [A-] > [HA]:** log term is positive, so pH > pKa (more basic). Makes sense -- excess conjugate base pushes pH up.

**When [A-] < [HA]:** log term is negative, so pH < pKa (more acidic).

**When [A-]/[HA] = 10:** log(10) = 1, so pH = pKa + 1.

**When [A-]/[HA] = 0.1:** log(0.1) = -1, so pH = pKa - 1.

### Buffer Capacity

A **buffer** is a solution of a weak acid and its conjugate base (or a weak base and its conjugate acid). It resists pH changes when small amounts of strong acid or strong base are added.

**Effective buffer range: pKa +/- 1** (corresponds to [A-]/[HA] ratios from 1:10 to 10:1)

Outside this range, you've essentially run out of one component and the buffer breaks.

**How buffers work (Le Chatelier reasoning):**
- Add strong acid (H+) --> H+ reacts with A- to form HA. The base component absorbs the acid.
- Add strong base (OH-) --> OH- reacts with HA to form A- + H2O. The acid component absorbs the base.
- The pH shifts slightly but doesn't crash because the ratio [A-]/[HA] changes slowly.

### Choosing a Buffer

To buffer at a target pH, pick an acid whose **pKa is close to the target pH**. Want a buffer at pH 7.4 (physiological)? Use an acid with pKa near 7.4.

Biological example: The bicarbonate buffer system (H2CO3/HCO3-) buffers blood at pH 7.4, even though pKa1 of carbonic acid is 6.1. It works because the system is **open** -- CO2 is continuously exhaled, which shifts the equilibrium. This is why it's effective outside the normal +/- 1 range. The MCAT loves asking about this.

### Worked Example: Buffer pH

You make a buffer with 0.2 M acetic acid and 0.3 M sodium acetate. pKa of acetic acid = 4.76. What's the pH?

pH = 4.76 + log(0.3/0.2)
pH = 4.76 + log(1.5)
log(1.5) = log(3/2) = log(3) - log(2) = 0.48 - 0.30 = 0.18
pH = 4.76 + 0.18 = **4.94**

### Worked Example: Adding Strong Acid to a Buffer

To the above buffer (total volume 1 L), you add 0.05 mol of HCl. What happens?

The HCl fully dissociates and reacts with A-:
- A- decreases: 0.3 - 0.05 = 0.25 M
- HA increases: 0.2 + 0.05 = 0.25 M

New pH = 4.76 + log(0.25/0.25) = 4.76 + log(1) = **4.76**

The pH only dropped from 4.94 to 4.76. Without the buffer, adding 0.05 mol HCl to 1 L of water would give pH = -log(0.05) = 1.3. That's the power of a buffer.

**MCAT trap:** Students forget to do the stoichiometry step (converting moles of strong acid/base consumed) before plugging into Henderson-Hasselbalch. ALWAYS do the neutralization reaction first, THEN use H-H with the new amounts.

---

## 5. Titrations

This is arguably the most tested acid-base subtopic. Know titration curves inside and out.

### Strong Acid + Strong Base Titration

Example: Titrating HCl with NaOH

- **Before equivalence:** Excess H+ in solution. pH is low and rises slowly.
- **Equivalence point:** All acid has been neutralized. Only NaCl and water remain. **pH = 7.00** (neutral salt, no hydrolysis).
- **After equivalence:** Excess OH-. pH rises sharply then levels off.

The curve has a very **steep, sharp jump** at the equivalence point (goes from ~pH 4 to ~pH 10 in a fraction of a mL). This makes it easy to detect with an indicator.

### Weak Acid + Strong Base Titration (HIGHEST YIELD)

Example: Titrating acetic acid (CH3COOH) with NaOH

This is the titration curve the MCAT loves most. Here's what happens at each key point:

**Starting point (no base added):**
- Weak acid in water. Use the ICE table / sqrt(Ka x C) to find pH.
- pH will be low but not as low as a strong acid of the same concentration.

**Buffer region (between start and equivalence):**
- Both HA and A- are present. This IS a buffer.
- pH rises gradually. Use Henderson-Hasselbalch.

**Half-equivalence point (halfway to equivalence):**
- Exactly half the acid has been neutralized: [A-] = [HA].
- **pH = pKa** (because log(1) = 0).
- This is how you experimentally determine pKa from a titration curve. Find the half-equivalence volume, read the pH -- that's pKa.
- Buffer capacity is maximal here.

**Equivalence point:**
- ALL the weak acid has been converted to its conjugate base (A-).
- **pH > 7** because A- is a weak base that hydrolyzes water: A- + H2O <--> HA + OH-
- The stronger the original acid (larger Ka), the weaker the conjugate base, and the closer the equivalence pH is to 7.
- For acetic acid: equivalence pH is typically around 8.7-8.9.

**After equivalence:**
- Excess NaOH dominates. pH rises and levels off.

### Weak Base + Strong Acid Titration

Mirror image of above:
- Equivalence point pH is **< 7** (conjugate acid of the weak base hydrolyzes to give H+).
- Half-equivalence point: **pOH = pKb**, which means **pH = 14 - pKb = pKa of the conjugate acid**.

### Reading Titration Curves -- What to Look For

Given a titration curve on the MCAT, you should be able to identify:

1. **Starting pH** -- tells you about the starting solution (strong vs weak, approximate concentration)
2. **Buffer region** -- the flat, gently rising portion. The flatter it is, the better the buffering.
3. **Half-equivalence point** -- middle of the buffer region. pH here = pKa.
4. **Equivalence point** -- center of the steep vertical rise. Read the pH here.
   - pH = 7 --> strong/strong
   - pH > 7 --> weak acid was being titrated (conjugate base present)
   - pH < 7 --> weak base was being titrated (conjugate acid present)
5. **Volume at equivalence** -- use this to calculate the unknown concentration: moles acid = moles base at equivalence, so Ma x Va = Mb x Vb (for monoprotic).

### Polyprotic Titration Curves

A diprotic acid (like H2CO3 or amino acids) shows **two equivalence points** and **two half-equivalence points**. Each buffer region corresponds to one of the Ka values.

For H3PO4 (triprotic), you'd see three equivalence points (though Ka3 is so small the third may be hard to see).

For amino acids:
- The titration curve of glycine shows two equivalence points (one for the carboxyl group, one for the amino group).
- The isoelectric point (pI) is the average of the two pKa values flanking the zwitterion: **pI = (pKa1 + pKa2) / 2**.
- For amino acids with ionizable side chains, you average the two pKa values flanking the form with zero net charge.

### Indicators

An indicator is itself a weak acid (HIn) whose acid and base forms have different colors. It changes color when pH ~ pKa of the indicator.

Choose an indicator whose pKa is close to the equivalence point pH:
- Strong/strong titration (equiv at pH 7): phenol red, bromothymol blue
- Weak acid/strong base (equiv at pH ~8-9): phenolphthalein (pKa ~ 9.1)

### Common MCAT Traps in Titrations

1. **Confusing equivalence point with half-equivalence point.** At equivalence, all acid is neutralized. At half-equivalence, half is neutralized and pH = pKa. Different things.
2. **Thinking equivalence always = pH 7.** Only true for strong/strong. For weak acid/strong base, it's above 7.
3. **Forgetting that at the equivalence point of a weak acid titration, you have a solution of the conjugate base.** It's not neutral -- the A- hydrolyzes.
4. **Not using moles for stoichiometry.** Always convert to moles (n = M x V) when doing titration math. Then convert back to concentration for H-H or pH calculations.

---

## 6. Solutions and Concentration Units

### Concentration Units

| Unit | Definition | When Used |
|------|-----------|-----------|
| **Molarity (M)** | mol solute / L solution | Most common. Default for MCAT. |
| **Molality (m)** | mol solute / kg solvent | Colligative properties. Does NOT change with temperature. |
| **Mole fraction (X)** | mol component / total mol all components | Raoult's law, gas mixtures. |
| **Mass percent (w/w%)** | (mass solute / mass solution) x 100 | Labels on commercial reagent bottles. |
| **ppm / ppb** | parts per million / billion | Environmental chemistry, trace concentrations. |

**Molarity vs. Molality:** Molarity uses volume of solution (which changes with temperature because liquids expand/contract). Molality uses mass of solvent (which is temperature-independent). For dilute aqueous solutions, they're numerically very similar because 1 L water ~ 1 kg.

### Dilution

**M1V1 = M2V2**

The total moles of solute don't change when you dilute -- you're just adding solvent.

Worked example: You have 50 mL of 6 M HCl and want to make 2 M HCl. How much total solution do you need?

(6)(50) = (2)(V2)
V2 = 150 mL total volume

So you add 100 mL of water to the 50 mL of concentrated acid.

**Safety note the MCAT may reference:** Always add acid to water, not water to acid ("do as you oughta, add acid to water"). Adding water to concentrated acid can cause violent boiling and spattering due to the exothermic dissolution.

---

## 7. Solubility and Ksp

### Solubility Product (Ksp)

For a sparingly soluble salt dissolving in water:

**AgCl(s) <--> Ag+(aq) + Cl-(aq)**

**Ksp = [Ag+][Cl-]**

Note: the solid is NOT included in the expression (activity of a pure solid = 1).

For a salt like Ca3(PO4)2:

Ca3(PO4)2 <--> 3Ca2+ + 2PO4^3-

**Ksp = [Ca2+]^3 [PO4^3-]^2**

### Calculating Solubility from Ksp

Worked example: Ksp of AgCl = 1.8 x 10^-10. Find the molar solubility.

Let s = molar solubility (mol/L of AgCl that dissolves).

[Ag+] = s, [Cl-] = s

Ksp = s^2 = 1.8 x 10^-10

s = sqrt(1.8 x 10^-10) ~ 1.3 x 10^-5 M

Worked example: Ksp of PbI2 = 9.8 x 10^-9. Find molar solubility.

PbI2 <--> Pb2+ + 2I-

[Pb2+] = s, [I-] = 2s

Ksp = (s)(2s)^2 = 4s^3

s = (Ksp/4)^(1/3) = (2.45 x 10^-9)^(1/3)

Cube root of ~2.5 x 10^-9: cube root of 2.5 ~ 1.36, cube root of 10^-9 = 10^-3

s ~ 1.4 x 10^-3 M

**MCAT shortcut:** You can compare solubilities of salts with the SAME stoichiometry (like AgCl vs. AgBr, both 1:1) by directly comparing Ksp values. Higher Ksp = more soluble. But you CANNOT compare salts of different stoichiometries (AgCl vs. PbI2) by Ksp alone -- you must calculate actual solubility.

### Common-Ion Effect

Adding a common ion DECREASES solubility. This is Le Chatelier's principle in action.

Example: What happens to the solubility of AgCl if you dissolve it in 0.1 M NaCl instead of pure water?

Now [Cl-] already starts at 0.1 M (from NaCl). The equilibrium shifts LEFT, meaning less AgCl dissolves.

Ksp = [Ag+][Cl-] = (s)(0.1 + s) ~ (s)(0.1)

s = Ksp / 0.1 = 1.8 x 10^-10 / 0.1 = 1.8 x 10^-9 M

Compare to 1.3 x 10^-5 M in pure water -- that's a ~7000-fold decrease in solubility. The common-ion effect is powerful.

### Selective Precipitation

If a solution contains multiple ions, you can selectively precipitate one by adding an ion that forms an insoluble salt with it. The salt with the smallest Ksp precipitates first.

Example: A solution contains Cl- and I-. You slowly add Ag+. AgI (Ksp = 8.5 x 10^-17) precipitates first because it's far less soluble than AgCl (Ksp = 1.8 x 10^-10).

### Complex Ion Formation

Some metal ions form soluble complex ions with ligands (NH3, CN-, OH-). This INCREASES solubility by removing the free metal ion from solution, pulling the equilibrium to the right.

AgCl(s) <--> Ag+ + Cl-
Ag+ + 2NH3 <--> [Ag(NH3)2]+    (Kf is large)

The overall effect: AgCl dissolves more in NH3 solution than in pure water because Ag+ is being consumed to form the complex.

This is a Le Chatelier argument: removing Ag+ shifts the dissolution equilibrium right.

---

## 8. Colligative Properties

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

**MCAT trap #2:** Using i = 2 for a weak electrolyte. Weak acids/bases barely dissociate, so i ~ 1.

**MCAT trap #3:** Real solutions have i values slightly lower than ideal because of ion pairing (ions briefly associate in solution). If the MCAT says "ideal" or "dilute," use the integer value. If they give you a measured i, use that.

### Boiling Point Elevation

**delta_Tb = i x Kb x m**

- Kb = ebullioscopic constant (for water, 0.512 C/m -- rarely need to memorize, usually given)
- m = molality of solute
- Adding solute RAISES the boiling point

Why? Solute particles in the liquid phase lower the vapor pressure (fewer solvent molecules at the surface can escape). You need a higher temperature to reach a vapor pressure of 1 atm.

### Freezing Point Depression

**delta_Tf = i x Kf x m**

- Kf = cryoscopic constant (for water, 1.86 C/m)
- Adding solute LOWERS the freezing point

Why? Solute particles disrupt crystal packing. The solution must be cooled further to freeze.

Practical example: Road salt (NaCl) lowers the freezing point of water on roads. CaCl2 is even better because i = 3 vs. i = 2.

Worked example: What is the freezing point of a 0.5 m NaCl solution?

delta_Tf = i x Kf x m = 2 x 1.86 x 0.5 = 1.86 C

Freezing point = 0 - 1.86 = **-1.86 C**

### Osmotic Pressure

**pi = iMRT**

- pi = osmotic pressure
- M = molarity
- R = 0.0821 L atm / mol K (ideal gas constant)
- T = temperature in Kelvin

Osmotic pressure is the pressure needed to PREVENT osmosis (net solvent flow from dilute to concentrated side across a semipermeable membrane).

**Higher solute concentration = higher osmotic pressure.**

This is critical for biology connections:
- **Isotonic:** Same osmotic pressure as the cell. No net water movement. (0.9% NaCl = normal saline)
- **Hypertonic:** Higher solute outside. Water flows OUT of cell. Cell crenates (shrivels).
- **Hypotonic:** Lower solute outside. Water flows INTO cell. Cell lyses (bursts).

Worked example: What is the osmotic pressure of 0.15 M NaCl at 37 C (body temp, 310 K)?

pi = iMRT = (2)(0.15)(0.0821)(310) = 2 x 0.15 x 25.5 ~ **7.6 atm**

That's a substantial pressure -- this is why osmosis is such a powerful driving force in biology.

### Vapor Pressure Lowering (Raoult's Law)

**P_solution = X_solvent x P_solvent^0**

- X_solvent = mole fraction of solvent
- P_solvent^0 = vapor pressure of pure solvent

Adding a non-volatile solute lowers the vapor pressure of the solution because fewer solvent molecules are at the surface to evaporate.

The more solute you add (decreasing X_solvent), the more the vapor pressure drops.

For volatile solutes (like two miscible liquids):

**P_total = X_A x P_A^0 + X_B x P_B^0**

Each component contributes to the total vapor pressure in proportion to its mole fraction.

**Positive deviation from Raoult's law:** Interactions between A and B are WEAKER than A-A and B-B interactions. Molecules escape more easily. Vapor pressure is HIGHER than predicted. Example: ethanol + hexane.

**Negative deviation from Raoult's law:** Interactions between A and B are STRONGER (like hydrogen bonding). Molecules are held more tightly. Vapor pressure is LOWER than predicted. Example: acetone + chloroform.

---

## High-Yield Summary Table

| Concept | Key Equation / Fact | Common Trap |
|---------|-------------------|-------------|
| pH of strong acid | pH = -log[H+] directly | Forgetting to adjust for diprotic (H2SO4 gives 2 H+) |
| pH of weak acid | [H+] = sqrt(Ka x C) | Using this formula for strong acids (they don't have Ka) |
| Henderson-Hasselbalch | pH = pKa + log([A-]/[HA]) | Forgetting to do stoichiometry before plugging in ratios |
| Half-equivalence | pH = pKa | Confusing with equivalence point |
| Equivalence (weak acid/strong base) | pH > 7 | Assuming pH = 7 for all titrations |
| Buffer range | pKa +/- 1 | Thinking buffers work at any pH |
| Ka x Kb | = Kw = 10^-14 | Mixing up which Ka goes with which Kb |
| Ksp | Product of ion concentrations | Comparing Ksp across different stoichiometries |
| Colligative properties | All include i factor | Forgetting i for ionic solutes |
| Raoult's law | P = X_solvent x P^0 | Confusing mole fraction of solvent vs. solute |

---

## MCAT Problem-Solving Strategy

When you see an acid-base question:

1. **Identify what you're dealing with:** Strong or weak? Acid or base? Buffer? Titration?
2. **Decide which tool to use:**
   - Strong acid/base in water --> direct pH calculation
   - Weak acid/base in water --> ICE table or sqrt(Ka x C)
   - Buffer (weak acid + conjugate base) --> Henderson-Hasselbalch
   - Titration --> identify where you are on the curve (before, at half-equiv, at equiv, after equiv)
3. **Watch your units:** Convert volumes to liters, use moles for stoichiometry, convert back to molarity for pH.
4. **Estimate before committing:** Use the log approximations. If an answer choice is pH = 3.2 and your estimate gives pH ~ 3, that's probably it.
5. **Check reasonableness:**
   - Acidic solutions: pH < 7
   - Basic solutions: pH > 7
   - Weak acid pH should be higher than strong acid of same concentration
   - Adding base should increase pH; adding acid should decrease pH
   - Buffer pH should be close to pKa

---

## Cross-Topic Connections

**Amino acid charge states:** Each amino acid has pKa values for its carboxyl, amino, and (possibly) side chain groups. The charge at a given pH is determined by comparing pH to each pKa -- if pH > pKa, the group is deprotonated. This is Henderson-Hasselbalch applied to biochemistry.

**Blood buffer system:** CO2 + H2O <--> H2CO3 <--> H+ + HCO3-. Hyperventilation blows off CO2, shifting equilibrium LEFT, decreasing H+, raising pH (respiratory alkalosis). Hypoventilation does the opposite. The kidneys regulate HCO3- reabsorption for long-term pH control. This integrates acid-base chemistry with respiratory and renal physiology.

**Enzyme kinetics:** Many enzymes have pH optima. The ionization state of active-site residues (determined by their pKa values and the local pH) affects substrate binding and catalysis. Pepsin works at pH 2 (stomach); trypsin at pH 8 (small intestine).

**Drug solubility and absorption:** Weak acid drugs are protonated (neutral, membrane-permeable) in the acidic stomach and absorbed there. Weak base drugs are protonated (charged, trapped) in the stomach but neutral and absorbable in the basic intestine. This is the "pH partition hypothesis" and it's a direct application of Henderson-Hasselbalch.

---

*This is a living document. Update as you encounter new question patterns or identify gaps in your understanding.*
