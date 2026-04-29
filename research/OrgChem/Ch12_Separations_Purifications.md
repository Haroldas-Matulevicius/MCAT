# CP Orgo Chapter 12 — Separations & Purifications

Scope: Solubility-based methods (extraction, acid-base extraction, recrystallization); distillation (simple, fractional, vacuum); chromatography (TLC, column, HPLC, GC, size-exclusion, ion-exchange, affinity); electrophoresis (agarose, native PAGE, SDS-PAGE, IEF, 2D); centrifugation (differential, density gradient); filtration; dialysis.

**Section:** Chemical/Physical (CP)
**Book:** Kaplan Organic Chemistry — Chapter 12
**AAMC FC mapping:** FC5C (separations and purification)
**Yield:** HIGH — separation techniques show up in passages constantly, often as the experimental backbone you need to interpret to answer 2-3 questions.

---

## 1. Extraction

### Liquid-Liquid Extraction

The core idea: you have two **immiscible solvents** (they don't mix, like oil and water). When you shake a compound with both solvents, it **partitions** between them based on its relative solubility in each layer. The **partition coefficient (K)** describes this:

> K = concentration in organic layer / concentration in aqueous layer

A compound that is more soluble in the organic solvent will preferentially dissolve there. After shaking and letting the layers separate in a **separatory funnel**, you drain the bottom layer (whichever is denser — usually water) and collect the top layer separately.

**Key detail for the MCAT:** The organic layer is usually on top (most organic solvents are less dense than water), but **dichloromethane (DCM) and chloroform are denser than water** and sit on the bottom. Know this — it shows up in passage-based questions.

### Acid-Base Extraction

This is where extraction gets strategic. The principle: **charged molecules are water-soluble; uncharged molecules are organic-soluble.** You can toggle a molecule between charged and uncharged forms by changing the pH.

**The rules:**

| Compound Type | To move it INTO aqueous layer | To move it INTO organic layer |
|---|---|---|
| **Carboxylic acid** (weak acid, pKa ~4-5) | Add strong base (NaOH) — deprotonates to COO⁻ (charged, water-soluble) | Add strong acid (HCl) — protonates to COOH (neutral, organic-soluble) |
| **Amine** (weak base, pKa ~10-11 for conjugate acid) | Add strong acid (HCl) — protonates to NH₃⁺ (charged, water-soluble) | Add strong base (NaOH) — deprotonates to NH₂ (neutral, organic-soluble) |
| **Neutral compound** (no ionizable groups) | Cannot be moved by pH changes | Stays in organic layer regardless of pH |

### Step-by-Step: Separating Acidic, Basic, and Neutral Compounds

Suppose you have benzoic acid (acidic), aniline (basic), and naphthalene (neutral) dissolved in diethyl ether.

1. **Wash with dilute HCl (aqueous acid).** Aniline gets protonated to ammonium salt → moves to aqueous. Drain the "aqueous acid extract."

2. **Wash organic layer with dilute NaOH (aqueous base).** Benzoic acid gets deprotonated to carboxylate → moves to aqueous. Drain the "aqueous base extract."

3. **Organic layer now contains only neutral naphthalene.** Evaporate solvent.

4. **To recover amine:** Add NaOH to aqueous acid extract → deprotonates back to free amine → extract into organic.

5. **To recover carboxylic acid:** Add HCl to aqueous base extract → reprotonates back to free acid.

**MCAT trap:** Add acid first (to pull out base) and base second (to pull out acid). The logic is straightforward — use the opposite reagent to ionize your target.

**Differentiating carboxylic acid from phenol:** Both are acidic, but carboxylic acid (pKa 4) is deprotonated by NaHCO₃ (pKa 6.4); phenol (pKa 10) is NOT. So 5% NaHCO₃ wash extracts carboxylic acids only, leaving phenols in the organic layer for a subsequent NaOH wash.

---

## 2. Distillation

Distillation separates compounds based on differences in **boiling point**. You heat a liquid mixture; the component with the lower boiling point vaporizes first, rises into a condenser, and is collected as a separate liquid (the **distillate**).

### Simple Distillation

Use when boiling points differ by **more than ~25°C**. One vaporization-condensation cycle is enough. Setup: round-bottom flask, distillation head with thermometer, condenser, collection flask.

**How it works:** As you heat, vapor enriched in the lower-boiling component rises. Thermometer reads vapor T. Collect liquid while T is near the BP of the first component, then swap collection flasks when T rises.

### Fractional Distillation

Use when boiling points are **close** (Δ < 25°C). A **fractionating column** (packed with glass beads or steel wool) sits between the flask and the distillation head. Vapor condenses and re-vaporizes **multiple times** as it rises.

Each condensation-vaporization cycle further enriches the vapor. Each cycle = "theoretical plate." More plates = better separation.

### Vacuum Distillation

The boiling point of a liquid **decreases at lower pressure** (Clausius-Clapeyron). By applying vacuum, you can distill compounds at temperatures well below their normal boiling points.

**When to use:** Compounds that **decompose at high temperatures** or that have very high normal boiling points. If a passage mentions a heat-sensitive compound, think vacuum distillation.

### Connection to Vapor Pressure and Raoult's Law

(See `CP_GC_Ch09_Solutions.md` for fundamentals.)

For ideal solutions: P_A = X_A · P°_A. Component with **higher pure vapor pressure** (lower BP) contributes more to total vapor pressure. Vapor enriched in more volatile component — this is why distillation works.

**Deviations:**
- **Positive deviation:** A-B IMFs weaker than A-A and B-B. Min-BP **azeotrope** (e.g., ethanol-water 95.6%) — cannot be further separated by distillation.
- **Negative deviation:** A-B stronger. Max-BP azeotrope.

---

## 3. Chromatography

This is the **most heavily tested** separation topic on the MCAT. Every chromatography technique relies on the same fundamental principle:

> A mixture is carried by a **mobile phase** across a **stationary phase**. Components that interact more strongly with the stationary phase move more slowly. Components that spend more time in the mobile phase move faster and **elute first**.

The selectivity comes from how different molecules partition between these two phases.

### Thin-Layer Chromatography (TLC)

**Setup:** Thin layer of **silica gel** (SiO₂, very polar) or **alumina** (Al₂O₃, polar) coated on a plate. Spot the mixture near the bottom; place in a chamber with shallow solvent (mobile phase / **eluent**). Solvent travels up by **capillary action**.

**Rf value:**

> Rf = distance traveled by compound / distance traveled by solvent front

- Rf 0 to 1
- **Higher Rf = compound traveled farther = less polar** (in normal-phase TLC)
- **Lower Rf = stuck near origin = more polar**

**Adjusting Rf:** Increasing mobile phase polarity increases Rf (polar solvent competes with polar stationary phase, pushing compounds along).

**Visualization:** UV light (if compounds have conjugation), or stain with iodine, KMnO₄.

**Reversed-phase TLC:** Stationary phase **nonpolar** (C18 chains on silica). Now **more polar compounds travel farther** (higher Rf) — everything flips. MCAT will specify; default is normal phase.

### Column Chromatography

TLC scaled up for **preparative purification** (collect fractions). Glass column packed with silica gel; load mixture on top, elute with solvent, collect fractions.

- **Normal phase:** Silica (polar), nonpolar-to-moderately-polar mobile phase. Less polar compounds elute first.
- **Reversed phase:** C18-silica (nonpolar), polar mobile phase. More polar compounds elute first.

**Gradient elution:** Gradually increase mobile phase polarity (normal) or decrease (reversed) to elute increasingly retained compounds.

### High-Performance Liquid Chromatography (HPLC)

Same principle as column chromatography but with **high pressure** through tightly packed, small-particle columns. **Higher resolution** and speed.

- Detector: UV-Vis, fluorescence, mass spec.
- Output: chromatogram with peaks at different retention times.
- Peak area ∝ amount of compound.

**MCAT relevance:** Interpret chromatograms — which peak is which, why one elutes before another based on polarity.

### Gas Chromatography (GC)

For **volatile compounds** (must be in gas phase). Mobile phase = inert carrier gas (He, N₂). Stationary phase = liquid coating inside a long, coiled capillary column in a temperature-controlled oven.

Separation based on:
- **Boiling point** (lower = faster through column)
- **Polarity** (depends on stationary phase)

Often coupled with mass spec (**GC-MS**).

### Size-Exclusion Chromatography (Gel Filtration)

This one is **counterintuitive**.

**Setup:** Column packed with porous beads.

**How it works:**
- **Large molecules** can't enter pores. Travel around beads in void volume. Elute **FIRST**.
- **Small molecules** enter pores, take longer winding path. Elute **LAST**.
- **Medium molecules** in between.

> **Memory trick:** Big out first. Small stuck in pores, out last. **Opposite of gel electrophoresis** (where small goes fastest).

**Uses:** Separate proteins by MW; estimate native MW (with standards); buffer exchange / desalting (protein big, salt small — collect first peak).

### Ion-Exchange Chromatography

Separates based on **net charge**.

**Two types:**

| Resin Type | Beads Have | Binds | Example |
|---|---|---|---|
| **Cation exchange** | Negative charges (e.g., -SO₃⁻) | Positive molecules | Proteins above pI |
| **Anion exchange** | Positive charges (e.g., -NR₃⁺) | Negative molecules | Proteins below pI (most proteins) |

Wait — recheck: cation exchanger binds CATIONS (positives). Anion exchanger binds ANIONS (negatives).

**Elution strategies:**
- **Salt gradient:** Increase NaCl. Na⁺ or Cl⁻ ions compete for binding sites, displacing protein.
- **pH change:** Alter pH to change protein's net charge. At pI, no net charge — won't bind.

**Key concept:** Charge depends on pH vs pI:
- pH > pI: net negative (binds anion exchanger)
- pH < pI: net positive (binds cation exchanger)
- pH = pI: zero net (won't bind either)

### Affinity Chromatography

The **most specific** chromatographic technique. Stationary phase has a **ligand** covalently attached that specifically binds the target (lock-and-key).

**Examples:**
- Antibody on beads → captures antigen
- Ni-NTA column → captures **His-tagged** recombinant proteins (very common)
- Substrate analog → captures enzyme
- Lectin column → captures glycoproteins

**How:**
1. Load crude mixture
2. Wash with buffer — non-binders flow through
3. **Elute** target by adding competing ligand (excess free ligand, imidazole for His-tag) or change pH/ionic strength.

**Affinity gives highest purity in a single step.** "One-step purification" = affinity.

---

## 4. Electrophoresis

Electrophoresis separates charged molecules in an **electric field**. Molecules migrate toward the electrode with opposite charge. Rate depends on **charge, size, and shape** (unless you control variables).

### Agarose Gel Electrophoresis

Used for **DNA and RNA**.
- DNA has uniform negative charge (phosphate backbone, charge ∝ length).
- Charge-to-mass ratio is constant for all DNA fragments → separation by **size only**.
- **Smaller fragments migrate faster** (navigate pores easier).
- **Larger fragments migrate slower**.

**Loading:** Wells at negative electrode (cathode); DNA migrates toward positive (anode).
**Visualization:** Ethidium bromide (intercalates, fluoresces UV) or SYBR Green.
**Size determination:** Run a **molecular weight ladder** alongside.

### Native PAGE

For **proteins** under **non-denaturing** conditions.
- Proteins keep native folded structure.
- Separation by **charge, size, AND shape**.
- Useful when preserving enzyme activity.
- Harder to interpret (multiple variables).

### SDS-PAGE

The **workhorse** of protein analysis. Extremely high-yield.

**SDS (sodium dodecyl sulfate)** is an anionic detergent that:
1. **Denatures** the protein (linear chain).
2. **Coats** the protein with uniform negative charge proportional to length (~1 SDS per 2 AAs).

Every protein has same charge-to-mass ratio and shape → separation by **molecular weight only**.

- **Smaller proteins migrate faster** (like agarose).
- **Larger proteins migrate slower**.

**Reducing conditions:** **β-mercaptoethanol (BME)** or **dithiothreitol (DTT)** breaks **disulfide bonds**. Important for multi-subunit proteins:
- Without reducing agent: dimer held by disulfide runs as one band.
- With reducing agent: subunits separate, two bands.

**MCAT trap:** SDS-PAGE under reducing vs non-reducing reveals disulfide-bonded subunits.

**MW estimation:** Plot log(MW) vs migration distance — roughly linear.

### Isoelectric Focusing (IEF)

Separates proteins by **pI** (pH at zero net charge).

**Setup:** Gel with immobilized **pH gradient** (acidic → basic). Apply electric field.

**How it works:**
- Protein in region more acidic than pI → positive → migrates toward cathode (negative end).
- More basic than pI → negative → migrates toward anode.
- At pI → zero net charge → **stops moving**.

Each protein **focuses** into a sharp band at its pI.

### 2D Gel Electrophoresis

**IEF (1st dim) + SDS-PAGE (2nd dim)** for max resolution.

1. IEF horizontally
2. Rotate 90°, run SDS-PAGE vertically
3. Each protein = spot defined by pI and MW

Resolves **thousands of proteins** in one experiment. Used in proteomics.

---

## 5. Centrifugation

Centrifugation separates particles based on **size, shape, and density** by spinning at high speed. Centrifugal force pushes denser/larger particles to the bottom (the **pellet**); lighter material stays in liquid (the **supernatant**).

### Differential Centrifugation

**Sequential spins at increasing speeds** to fractionate cell components:

| Spin | Speed | What pellets |
|---|---|---|
| 1st (low) | ~1,000 × g | Whole cells, nuclei, large debris |
| 2nd | ~10,000 × g | Mitochondria, lysosomes, peroxisomes |
| 3rd | ~100,000 × g | Microsomes (ER fragments), plasma membrane fragments |
| 4th (ultra) | >100,000 × g | Ribosomes, viruses, large macromolecules |

After each spin, **pour off supernatant** and spin at higher speed. Each pellet enriched in a particular fraction.

**MCAT application:** Passages describe fractionation and ask which enzyme is in which pellet. Cytochrome c oxidase → mitochondrial pellet (2nd spin). Glucose-6-phosphatase → ER fraction (3rd spin).

### Density Gradient Ultracentrifugation

Separates components through a **pre-formed density gradient** (sucrose or cesium chloride).

**Two types:**

- **Rate-zonal (sucrose gradient):** Particles sediment at different rates based on size and shape. Stop before anything reaches bottom. Separates by **sedimentation coefficient (S value)** — larger S = sediments faster.

- **Isopycnic (equilibrium, CsCl gradient):** Spin until every particle reaches the position in the gradient where **its density matches the surrounding medium density**. Separation purely by **buoyant density**, regardless of size.

**Famous example:** Meselson-Stahl separated ¹⁴N-DNA from ¹⁵N-DNA in semiconservative replication experiment.

---

## 6. Other Techniques

### Recrystallization

Purification for **solids**.

**Principle:** Most solids more soluble in hot solvent than cold. Impurities present in small amounts.

**Procedure:**
1. Dissolve impure solid in **minimum** hot solvent.
2. **Hot-filter** if insoluble impurities present.
3. **Cool slowly** — desired compound crystallizes (slow cooling = larger, purer crystals).
4. Impurities remain in **mother liquor** (low concentration, below saturation even cold).
5. **Filter** crystals; wash with cold solvent.

**Choosing solvent:** Dissolves compound when hot, poorly when cold. Steep solubility-temperature curve.

### Filtration

- **Gravity filtration:** Pour through filter paper in funnel. Removes insoluble impurities from hot solution.
- **Vacuum filtration (Buchner funnel):** Apply vacuum. Faster. Used to collect solid product (crystals from recrystallization).

### Dialysis

Separates by **size** using a **semipermeable membrane** with defined molecular weight cutoff (MWCO).

**How it works:** Place protein solution in dialysis bag, submerge in large volume of buffer.
- **Small molecules** (salts, urea) pass through pores → equilibrate with buffer.
- **Large molecules** (proteins, DNA) retained.

**Uses:**
- **Buffer exchange:** Change buffer composition around protein.
- **Desalting:** Remove salt after ammonium sulfate precipitation.
- Remove small-molecule contaminants.

Relies on diffusion down concentration gradient. Large buffer volume (or multiple changes) drives more complete removal.

---

## Decision Table: Which Technique?

| Goal | Best Technique |
|---|---|
| Separate organics by acid/base properties | **Acid-base extraction** |
| Separate liquids w/ different BPs | **Distillation** (simple if Δ>25°C, fractional if close) |
| Heat-sensitive liquid | **Vacuum distillation** |
| Quick reaction monitoring / purity | **TLC** |
| Bulk preparative orgo separation | **Column chromatography** |
| High-res analytical small molecules | **HPLC** |
| Volatile compounds | **GC** (often GC-MS) |
| Proteins by size (native) | **Size-exclusion** |
| Proteins by charge | **Ion-exchange** |
| Specific protein from crude mix | **Affinity** |
| DNA fragments by size | **Agarose gel** |
| Protein MW (denatured) | **SDS-PAGE** |
| Proteins by pI | **IEF** |
| Proteomics resolution | **2D gel (IEF + SDS-PAGE)** |
| Cell organelles | **Differential centrifugation** |
| Buoyant density (DNA, viruses) | **Isopycnic ultra (CsCl)** |
| Purify solid product | **Recrystallization** |
| Remove salt / change buffer | **Dialysis** or **size-exclusion** |

---

## High-Yield Comparison: Don't Confuse These

| Concept | Technique A | Technique B | Key Difference |
|---|---|---|---|
| Small first vs Big first | **Gel electrophoresis** — small migrates faster | **Size-exclusion** — big elutes first | Opposite outcomes |
| Normal vs Reversed phase | Polar stationary, nonpolar elutes first | Nonpolar stationary, polar elutes first | Everything flips |
| SDS-PAGE vs Native PAGE | Denatures + uniform charge → MW only | Native; charge + size + shape | SDS simpler |
| Cation vs Anion exchange | Negative beads bind cations | Positive beads bind anions | Named for what they exchange |
| Differential vs Density gradient | Sequential pellets, increasing speed | Continuous via gradient | Differential = crude; gradient = fine |

---

## Quick-Fire MCAT Connections

- **Acid-base extraction** ↔ pKa, Henderson-Hasselbalch (Ch10).
- **Distillation** ↔ phase diagrams, Clausius-Clapeyron, IMFs.
- **Chromatography polarity** ↔ functional groups, H-bonding, dipole-dipole (CP_GC_Ch03).
- **SDS-PAGE** ↔ protein structure, disulfide bonds, quaternary structure.
- **IEF and ion exchange** ↔ AA charge, pI, H-H at molecular level (CP_OC_Ch10).
- **Centrifugation** ↔ cell biology — which organelles, which metabolic pathways (BB_Bio_Ch01).
- **Meselson-Stahl** = isopycnic CsCl ultracentrifugation. DNA replication ↔ separation crossover (BB_Ch06).

---

## High-Yield Takeaways

1. **Acid-base extraction:** charged = water; uncharged = organic; toggle with pH.
2. **NaHCO₃ test:** distinguishes carboxylic acid (yes) from phenol (no).
3. **Distillation:** simple if ΔBP > 25°C, fractional if close, vacuum for heat-sensitive.
4. **TLC normal phase:** higher Rf = less polar.
5. **Size-exclusion:** **big elutes first** (opposite of gel electrophoresis where small is fastest).
6. **SDS-PAGE separates by MW only** (uniform charge from SDS).
7. **IEF separates by pI;** 2D = IEF + SDS-PAGE.
8. **Differential centrifugation** = sequential speeds; **isopycnic** = density match (Meselson-Stahl).
9. **Affinity chromatography = highest purity in one step** (His-tag/Ni-NTA most common).
10. **Recrystallization** for solids; **dialysis** for buffer exchange.

---

→ Acid-base extraction pKa logic: `CP_GC_Ch10_Acids_Bases.md`, `CP_OC_Ch08_Carboxylic_Acids.md`
→ Distillation phase-diagram logic: `CP_GC_Ch07_Thermochemistry.md`, `CP_GC_Ch09_Solutions.md`
→ Chromatography polarity reasoning: `CP_OC_Ch01_Nomenclature.md`, `CP_GC_Ch03_Bonding.md`
→ Protein structure & SDS-PAGE: `BB_Ch01_AminoAcids_Proteins.md`
→ Gel electrophoresis & DNA: `BB_Ch06_DNA_Biotech.md`
→ Cell organelles for centrifugation: `BB_Bio_Ch01_Cell.md`
