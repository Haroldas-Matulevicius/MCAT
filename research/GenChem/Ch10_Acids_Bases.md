# CP Gen Chem Chapter 10 — Acids & Bases

Scope: Bronsted-Lowry & Lewis definitions; strong vs weak acids/bases; pH/pOH calculations; Henderson-Hasselbalch; buffer capacity & buffer choice; titrations (strong/strong, weak/strong, polyprotic); indicators; polyvalence/normality.

**Section:** Chemical/Physical (CP)
**Book:** Kaplan General Chemistry — Chapter 10
**AAMC FC mapping:** FC5A (acid-base)
**Yield:** THE single highest-yield gen chem topic. Expect 5-8 questions touching acid-base reasoning on any given exam. Cross-links into biochem (AA charge, enzyme kinetics), bio (blood buffering, renal physiology), P/S (pharmacology). Master cold.

---

## 1. Definitions of Acids and Bases

### Bronsted-Lowry (the default on MCAT)

- **Acid** = proton (H+) donor
- **Base** = proton (H+) acceptor

This is the definition you'll use 90% of the time. When the MCAT says "acid" or "base" without further context, they mean Bronsted-Lowry.

**Conjugate pairs** always differ by exactly one H+:
- HF donates a proton --> F- is its **conjugate base**
- NH3 accepts a proton --> NH4+ is its **conjugate acid**

Key relationship: **the stronger the acid, the weaker its conjugate base** (and vice versa). HCl is a strong acid, so Cl- is an absolutely terrible base. Acetic acid is a weak acid, so acetate (CH3COO-) is a decent (but still weak) base.

### Lewis (the broader definition)

- **Acid** = electron pair acceptor
- **Base** = electron pair donor

Lewis encompasses everything Bronsted-Lowry covers and then some. Use the Lewis definition when:
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

**100% dissociation.** If you dissolve 0.01 M HCl, you get 0.01 M H+ and 0.01 M Cl-. No equilibrium expression needed.

Note on H2SO4: The first proton is strong (full dissociation). The second proton is weak (Ka2 ~ 0.012). For MCAT purposes, treat sulfuric as donating 2 H+ per molecule in dilute solution.

### Strong Bases

Group 1 metal hydroxides: **NaOH, KOH, LiOH**. Also Group 2 hydroxides like Ba(OH)2 and Ca(OH)2 (limited solubility). These dissociate completely.

### Weak Acids and Bases -- Equilibria

A **weak acid** only partially dissociates:

HA ↔ H+ + A-

**Ka = [H+][A-] / [HA]**

A **weak base** partially accepts protons from water:

B + H2O ↔ BH+ + OH-

**Kb = [BH+][OH-] / [B]**

### The Ka-Kb Relationship

For any conjugate acid-base pair:

**Ka × Kb = Kw = 1.0 × 10^-14 (at 25°C)**

This means: **pKa + pKb = 14**

If they give you the Kb of a base, you can find the Ka of its conjugate acid (and vice versa). Constant in buffer/titration problems.

### What Ka Tells You

| Ka Value | pKa | Acid Strength | Example |
|----------|-----|---------------|---------|
| ~10^-1 | ~1 | Moderately strong | HSO4- (second proton) |
| ~10^-5 | ~5 | Weak | CH3COOH (acetic acid, pKa 4.76) |
| ~10^-10 | ~10 | Very weak | NH4+ (pKa 9.25) |
| ~10^-14 | ~14 | Essentially non-acidic | Water |

**Larger Ka = smaller pKa = stronger acid = more dissociation.** The MCAT loves to list four compounds with different pKa values and ask which is the strongest acid -- it's the one with the LOWEST pKa.

---

## 3. pH Calculations

### The Core Equations

- **pH = -log[H+]**
- **pOH = -log[OH-]**
- **pH + pOH = 14** (at 25°C)
- **pKa = -log(Ka)**
- **pKb = -log(Kb)**
- **[H+][OH-] = Kw = 1.0 × 10^-14**

### Estimating pH Without a Calculator

Critical MCAT skill. Memorize these log approximations:

| Value | log(value) | How to remember |
|-------|-----------|-----------------|
| 1 | 0 | Exact |
| 2 | 0.3 | "log 2 is point 3" -- memorize cold |
| 3 | ~0.5 | Slightly less than 0.5 |
| 4 | 0.6 | = 2 × log 2 = 2(0.3) |
| 5 | 0.7 | = log(10/2) = 1 - 0.3 |
| 6 | ~0.78 | Use 0.8 |
| 7 | ~0.85 | Rarely needed |
| 8 | 0.9 | = 3 × log 2 |

**The Master Trick for pH:** Express [H+] in scientific notation, then use:

**pH = -log(A × 10^-n) = n - log(A)**

Worked: [H+] = 3 × 10^-5 M → pH = 5 - log(3) = 5 - 0.5 = **4.5**.
Worked: [H+] = 6 × 10^-3 M → pH = 3 - 0.78 ≈ **2.2**.
Worked: [H+] = 2 × 10^-8 M → pH = 8 - 0.3 = **7.7** (slightly basic).

**Going backwards:** pH = 4.3 → [H+] = 10^-4 × 10^-0.3 = 10^-4 × 0.5 = 5 × 10^-5 M.

### Strong Acid/Base pH

For strong acids, [H+] = concentration (assuming monoprotic). No equilibrium needed.

- 0.001 M HCl → pH = 3
- 0.05 M NaOH → pOH = 1.3 → pH = 12.7

### Weak Acid pH -- ICE Table

For weak acid HA with concentration C and Ka:

HA ↔ H+ + A-

**The 5% approximation:** If C/Ka > 100, then C - x ≈ C, and:

**x = [H+] = √(Ka × C)**

Worked: pH of 0.1 M acetic acid (Ka = 1.8 × 10^-5)?
- C/Ka ~ 5500 ✓
- [H+] = √(1.8 × 10^-6) ≈ 1.3 × 10^-3
- pH ≈ 2.9

### Polyprotic Acids

Acids that donate >1 proton: H3PO4, H2SO4, H2CO3, citric acid.

- Each successive dissociation is harder (Ka1 >> Ka2 >> Ka3)
- For pH of original solution, **only Ka1 matters**
- **Intermediate species** (HCO3-, H2PO4-) are **amphoteric**

The pH of an amphoteric intermediate in a diprotic system:

**pH = (pKa1 + pKa2) / 2**

This is the same formula as amino acid isoelectric point.

---

## 4. Henderson-Hasselbalch Equation

Most important equation in acid-base chemistry for the MCAT.

**pH = pKa + log([A-] / [HA])**

### Key Insights

**When [A-] = [HA]:** log(1) = 0, so **pH = pKa**. Half-equivalence point. Buffer capacity maximum.

**When [A-] > [HA]:** pH > pKa.

**When [A-] < [HA]:** pH < pKa.

**When [A-]/[HA] = 10:** pH = pKa + 1.
**When [A-]/[HA] = 0.1:** pH = pKa - 1.

### Buffer Capacity

A **buffer** is a solution of a weak acid + conjugate base (or weak base + conjugate acid). It resists pH changes.

**Effective buffer range: pKa ± 1** (corresponds to [A-]/[HA] from 1:10 to 10:1)

**How buffers work (Le Chatelier):**
- Add H+ → reacts with A- → forms HA. Base absorbs acid.
- Add OH- → reacts with HA → forms A- + H2O. Acid absorbs base.
- pH shifts slightly because the ratio changes slowly.

### Choosing a Buffer

To buffer at a target pH, pick an acid whose **pKa is close to the target pH**. Want a buffer at pH 7.4? Use an acid with pKa near 7.4.

**Bicarbonate buffer system (H2CO3/HCO3-)** buffers blood at pH 7.4 even though pKa1 of carbonic acid is 6.1. It works because the system is **open** -- CO2 is continuously exhaled, shifting equilibrium. This is why it's effective outside the normal ±1 range. MCAT favorite.

### Worked Example: Buffer pH

Buffer of 0.2 M acetic acid + 0.3 M sodium acetate. pKa = 4.76. pH?

pH = 4.76 + log(0.3/0.2) = 4.76 + log(1.5) = 4.76 + 0.18 = **4.94**

### Worked Example: Adding Strong Acid

Add 0.05 mol HCl to 1 L of above buffer:
- A- decreases: 0.3 - 0.05 = 0.25 M
- HA increases: 0.2 + 0.05 = 0.25 M
- New pH = 4.76 + log(1) = **4.76**

Without buffer, 0.05 mol HCl in 1 L gives pH = 1.3. That's the power.

**MCAT trap:** ALWAYS do the neutralization stoichiometry first, THEN plug into H-H.

---

## 5. Titrations

### Strong Acid + Strong Base

Example: HCl + NaOH

- **Before equivalence:** Excess H+. pH low, rises slowly.
- **Equivalence:** All acid neutralized. Only NaCl + water. **pH = 7.00**.
- **After equivalence:** Excess OH-. pH rises sharply.

The curve has a very **steep, sharp jump** at equivalence (~pH 4 to ~pH 10 in a fraction of a mL).

### Weak Acid + Strong Base (HIGHEST YIELD)

Example: acetic acid + NaOH

**Starting point:** Weak acid in water. Use sqrt(Ka × C).

**Buffer region:** Both HA and A- present. This IS a buffer. pH rises gradually. Use H-H.

**Half-equivalence point:** [A-] = [HA]. **pH = pKa**. Buffer capacity max. This is how you experimentally determine pKa.

**Equivalence point:** ALL weak acid converted to A-. **pH > 7** because A- hydrolyzes: A- + H2O ↔ HA + OH-. For acetic acid: equivalence pH ~8.7-8.9.

**After equivalence:** Excess NaOH dominates.

### Weak Base + Strong Acid

Mirror image:
- Equivalence point pH **< 7** (conjugate acid hydrolyzes)
- Half-equivalence point: **pOH = pKb**, so pH = 14 - pKb = pKa of conjugate acid

### Reading Titration Curves

Identify:
1. **Starting pH** — strong vs weak, approximate concentration
2. **Buffer region** — the flat, gently rising portion
3. **Half-equivalence** — middle of buffer region. pH = pKa
4. **Equivalence** — center of steep rise. Read pH:
   - = 7 → strong/strong
   - > 7 → weak acid titrated
   - < 7 → weak base titrated
5. **Volume at equivalence** — Ma·Va = Mb·Vb (monoprotic)

### Polyprotic Titration Curves

Diprotic acid (H2CO3, AAs) shows **two equivalence points** and **two half-equivalence points**. Triprotic (H3PO4): three equivalence points (third may be hard to see).

**Amino acids:**
- Two equivalence points (carboxyl, amino)
- pI = (pKa1 + pKa2) / 2 (no ionizable side chain)
- For ionizable side chains: average two pKas flanking the zero-charge form

### Indicators

An indicator is itself a weak acid (HIn) whose acid and base forms have different colors. Color change at pH ≈ pKa of indicator.

Choose pKa close to equivalence pH:
- Strong/strong (pH 7): phenol red, bromothymol blue
- Weak acid/strong base (pH 8-9): phenolphthalein (pKa ~9.1)

### Common MCAT Traps

1. Confusing equivalence with half-equivalence.
2. Thinking equivalence = pH 7 always (only strong/strong).
3. Forgetting that equivalence of weak acid titration gives a basic solution (A- hydrolyzes).
4. Not using moles for stoichiometry — always n = M·V.

---

## 6. Polyvalence and Normality

(See Ch04 for full equivalents/normality treatment.)

For polyprotic acid titrations, normality cleans up the math:

**N_acid · V_acid = N_base · V_base**

H2SO4 has n = 2 (two protons), so 1 M H2SO4 = 2 N H2SO4 — accounts for both protons in the equivalence calculation directly.

---

## High-Yield Summary Table

| Concept | Key Equation / Fact | Common Trap |
|---------|-------------------|-------------|
| pH of strong acid | pH = -log[H+] | Forgetting diprotic (H2SO4 → 2 H+) |
| pH of weak acid | [H+] = √(Ka·C) | Using for strong acids |
| Henderson-Hasselbalch | pH = pKa + log([A-]/[HA]) | Forgetting stoichiometry first |
| Half-equivalence | pH = pKa | Confusing with equivalence |
| Equivalence (weak acid/SB) | pH > 7 | Assuming pH = 7 always |
| Buffer range | pKa ± 1 | Thinking buffers work at any pH |
| Ka × Kb | = Kw = 10^-14 | Mixing pairs |

---

## MCAT Problem-Solving Strategy

1. **Identify:** Strong/weak? Acid/base? Buffer? Titration?
2. **Tool:**
   - Strong → direct pH
   - Weak → ICE or √(Ka·C)
   - Buffer → H-H
   - Titration → identify location on curve
3. **Units:** convert to liters, use moles for stoichiometry, back to molarity.
4. **Estimate first** with log approximations.
5. **Sanity check:** acid pH < 7, base > 7; weak < strong of same conc; buffer ≈ pKa.

---

## Cross-Topic Connections

**Amino acid charge states:** Each AA has pKas. Charge at given pH determined by comparing pH to each pKa. Henderson-Hasselbalch applied to biochem.

**Blood buffer system:** CO2 + H2O ↔ H2CO3 ↔ H+ + HCO3-. Hyperventilation blows off CO2, shifts left, ↑pH (respiratory alkalosis). Hypoventilation opposite. Kidneys regulate HCO3- reabsorption for long-term control.

**Enzyme kinetics:** Pepsin pH 2 (stomach); trypsin pH 8 (intestine). Active-site residue pKas + local pH determine activity.

**Drug solubility/absorption:** Weak acid drugs neutral in stomach (absorbed there); weak base drugs neutral in intestine (absorbed there). pH partition hypothesis = Henderson-Hasselbalch applied.

---

→ Buffer-related kinetics (enzymes, AA pI): `BB_Ch01_AminoAcids_Proteins.md`, `BB_Ch02_Enzymes.md`
→ Solutions / colligative: `CP_GC_Ch09_Solutions.md`
→ Equilibrium: `CP_GC_Ch06_Equilibrium.md`
→ Acid-base extraction: `CP_OC_Ch12_Separations_Purifications.md`
