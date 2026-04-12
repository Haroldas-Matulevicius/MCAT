# FC5C: Separation and Purification Techniques

> **Section:** Chem/Phys | **Yield:** HIGH -- separation techniques show up in passages constantly, often as the experimental backbone you need to interpret to answer 2-3 questions.

---

## 1. Extraction

### Liquid-Liquid Extraction

The core idea: you have two **immiscible solvents** (they don't mix, like oil and water). When you shake a compound with both solvents, it **partitions** between them based on its relative solubility in each layer. The **partition coefficient (K)** describes this:

> K = concentration in organic layer / concentration in aqueous layer

A compound that is more soluble in the organic solvent will preferentially dissolve there. After shaking and letting the layers separate in a **separatory funnel**, you drain the bottom layer (whichever is denser -- usually water) and collect the top layer separately.

**Key detail for the MCAT:** The organic layer is usually on top (most organic solvents are less dense than water), but **dichloromethane (DCM) and chloroform are denser than water** and sit on the bottom. Know this -- it shows up in passage-based questions.

### Acid-Base Extraction

This is where extraction gets strategic. The principle: **charged molecules are water-soluble; uncharged molecules are organic-soluble.** You can toggle a molecule between charged and uncharged forms by changing the pH.

**The rules:**

| Compound Type | To move it INTO aqueous layer | To move it INTO organic layer |
|---|---|---|
| **Carboxylic acid** (weak acid, pKa ~4-5) | Add strong base (NaOH) -- deprotonates to COO- (charged, water-soluble) | Add strong acid (HCl) -- protonates to COOH (neutral, organic-soluble) |
| **Amine** (weak base, pKa ~10-11 for conjugate acid) | Add strong acid (HCl) -- protonates to NH3+ (charged, water-soluble) | Add strong base (NaOH) -- deprotonates to NH2 (neutral, organic-soluble) |
| **Neutral compound** (no ionizable groups) | Cannot be moved by pH changes | Stays in organic layer regardless of pH |

### Step-by-Step: Separating a Mixture of Acidic, Basic, and Neutral Compounds

Suppose you have a mixture of benzoic acid (acidic), aniline (basic), and naphthalene (neutral) dissolved in an organic solvent like diethyl ether.

1. **Wash with dilute HCl (aqueous acid).** The amine (aniline) gets protonated to its ammonium salt -- it becomes charged and moves into the aqueous layer. Drain and save this aqueous layer ("aqueous acid extract"). The carboxylic acid and neutral compound stay in the organic layer.

2. **Wash the organic layer with dilute NaOH (aqueous base).** The carboxylic acid (benzoic acid) gets deprotonated to its carboxylate salt -- charged, moves into the aqueous layer. Drain and save this aqueous layer ("aqueous base extract"). The neutral compound stays in the organic layer.

3. **The organic layer now contains only the neutral compound** (naphthalene). Evaporate the solvent to recover it.

4. **To recover the amine:** Add NaOH to the aqueous acid extract. This deprotonates the ammonium salt back to the free amine, which precipitates or can be extracted into organic solvent.

5. **To recover the carboxylic acid:** Add HCl to the aqueous base extract. This reprotonates the carboxylate back to the free acid, which precipitates or can be extracted.

**MCAT trap:** Students forget that you add acid first (to pull out the base) and base second (to pull out the acid). The logic is straightforward -- you use the opposite reagent to ionize your target.

---

## 2. Distillation

Distillation separates compounds based on differences in **boiling point**. You heat a liquid mixture; the component with the lower boiling point vaporizes first, rises into a condenser, and is collected as a separate liquid (the **distillate**).

### Simple Distillation

Use when the boiling points differ by **more than ~25 degrees C**. One vaporization-condensation cycle is enough to get reasonable separation. The setup is straightforward: round-bottom flask, distillation head, condenser, collection flask.

**How it works:** As you heat the mixture, vapor enriched in the lower-boiling component rises. The thermometer at the distillation head reads the temperature of the vapor. You collect liquid while the temperature is near the BP of the first component, then swap collection flasks when the temperature rises toward the BP of the second component.

### Fractional Distillation

Use when boiling points are **close together** (difference < 25 degrees C). A **fractionating column** (packed with glass beads or steel wool) sits between the flask and the distillation head. This column provides a large surface area where vapor condenses and re-vaporizes **multiple times** as it rises.

Each condensation-vaporization cycle further enriches the vapor in the lower-boiling component. Think of each cycle as a "theoretical plate." More plates = better separation. This is why the column is tall and packed -- more surface area means more effective plates.

### Vacuum Distillation

The boiling point of a liquid **decreases at lower pressure** (this is straight from the Clausius-Clapeyron equation / phase diagrams). By applying a vacuum, you can distill compounds at temperatures well below their normal boiling points.

**When to use it:** Compounds that **decompose at high temperatures** or that have very high normal boiling points. If the passage mentions a heat-sensitive compound, think vacuum distillation.

### Connection to Vapor Pressure and Raoult's Law

**Raoult's Law:** For an ideal solution, the partial vapor pressure of each component equals its mole fraction times its pure vapor pressure:

> P_A = X_A * P_A^0

The component with the **higher pure vapor pressure** (lower boiling point) contributes more to the total vapor pressure. The vapor above the solution is enriched in this more volatile component -- and that is exactly why distillation works.

**Deviations from Raoult's Law:**
- **Positive deviation:** Intermolecular forces between A and B are weaker than A-A and B-B. Molecules escape more easily. Can form a **minimum-boiling azeotrope** (e.g., ethanol-water at 95.6% ethanol) that cannot be further separated by distillation.
- **Negative deviation:** A-B forces are stronger. Can form a **maximum-boiling azeotrope**.

**MCAT relevance:** Azeotropes are a common wrong-answer trap. If a passage mentions an azeotrope, know that you cannot separate the mixture further by simple or fractional distillation alone.

---

## 3. Chromatography

This is the **most heavily tested** separation topic on the MCAT. Every chromatography technique relies on the same fundamental principle:

> A mixture is carried by a **mobile phase** across a **stationary phase**. Components that interact more strongly with the stationary phase move more slowly. Components that spend more time in the mobile phase move faster and **elute first**.

The selectivity comes from how different molecules partition between these two phases.

### Thin-Layer Chromatography (TLC)

**Setup:** A thin layer of **silica gel** (SiO2, very polar) or **alumina** (Al2O3, polar) coated on a glass or plastic plate. You spot your mixture near the bottom, then place the plate in a chamber with a shallow pool of solvent (the mobile phase, called the **eluent**). Solvent travels up by **capillary action**.

**Rf value:**

> Rf = distance traveled by compound / distance traveled by solvent front

- Rf ranges from 0 to 1
- **Higher Rf = compound traveled farther = less polar** (in normal-phase TLC with polar stationary phase)
- **Lower Rf = compound stuck near the origin = more polar** (stronger interaction with polar silica)

**Adjusting Rf:** Increasing the polarity of the mobile phase increases Rf for all compounds (polar solvent competes with polar stationary phase for binding the compounds, pushing them along faster). If all your spots ran to the solvent front, use a less polar solvent. If nothing moved, use a more polar solvent.

**Visualization:** Many compounds are colorless. Use UV light (if compounds have conjugation), or stain with iodine, KMnO4, or other reagents.

**Reversed-phase TLC:** The stationary phase is **nonpolar** (C18 chains bonded to silica). Now **more polar compounds travel farther** (higher Rf) and nonpolar compounds stick. Everything flips. The MCAT will specify if the system is reversed-phase -- if it doesn't say, assume normal phase.

### Column Chromatography

This is TLC scaled up for **preparative purification** (you actually collect fractions). A glass column is packed with silica gel, and solvent is poured through by gravity (or low pressure). You load the mixture on top and collect fractions as they drip out.

- **Normal phase:** Silica (polar) stationary phase, nonpolar-to-moderately-polar mobile phase. Less polar compounds elute first.
- **Reversed phase:** C18-modified silica (nonpolar) stationary phase, polar mobile phase (water/acetonitrile). More polar compounds elute first.

**Gradient elution:** Gradually increase mobile phase polarity (normal phase) or decrease polarity (reversed phase) to elute increasingly strongly retained compounds. This improves resolution and prevents late-eluting compounds from taking forever.

### High-Performance Liquid Chromatography (HPLC)

Same principle as column chromatography but with **high pressure** forcing solvent through tightly packed, small-particle columns. This gives **much higher resolution** and speed.

- Can be normal phase or reversed phase (reversed phase is more common in modern practice)
- Connected to a detector (UV-Vis absorbance, fluorescence, mass spec)
- Output is a **chromatogram**: peaks at different retention times correspond to different compounds
- Peak area is proportional to the amount of compound

**MCAT relevance:** You won't need to know the instrumentation details, but you must be able to interpret chromatograms -- identify which peak is which, explain why one compound elutes before another based on polarity.

### Gas Chromatography (GC)

For **volatile compounds** (must be in the gas phase). The mobile phase is an inert carrier gas (helium, nitrogen). The stationary phase is a liquid coating inside a long, coiled capillary column housed in a temperature-controlled oven.

Compounds separate based on:
- **Boiling point** (lower BP = faster through column)
- **Polarity** (depends on the stationary phase)

Often coupled with mass spectrometry (**GC-MS**) for identification. This is the gold standard for analyzing small volatile organic molecules.

### Size-Exclusion Chromatography (Gel Filtration)

This one is **counterintuitive** and the MCAT loves testing it.

**Setup:** Column packed with porous beads. The pores have a defined size range.

**How it works:**
- **Large molecules** cannot enter the pores. They are excluded and travel around the beads in the void volume. They elute **FIRST**.
- **Small molecules** enter the pores, taking a longer, winding path through the column. They elute **LAST**.
- **Medium molecules** partially enter pores. They elute in between.

> **Memory trick:** Big comes out first. Small gets stuck in pores and comes out last. This is the opposite of gel electrophoresis (where small goes fastest) -- don't confuse them.

**Uses:**
- Separate proteins by molecular weight
- Estimate native molecular weight (if you run standards of known MW)
- Buffer exchange / desalting (protein is big, salt is small -- collect the first peak)

### Ion-Exchange Chromatography

Separates molecules based on **net charge**.

**Two types of resins:**

| Resin Type | Beads Have | Binds | Example |
|---|---|---|---|
| **Cation exchange** | Negative charges (e.g., sulfonate, -SO3-) | Positive molecules (cations) | Positively charged proteins at the running pH |
| **Anion exchange** | Positive charges (e.g., quaternary amine, -NR3+) | Negative molecules (anions) | Negatively charged proteins (e.g., most proteins above their pI) |

**Elution strategies:**
- **Salt gradient:** Increase NaCl concentration. The Na+ or Cl- ions compete for binding sites, displacing the protein. Weakly bound proteins elute first; strongly bound proteins need higher salt.
- **pH change:** Alter the pH to change the protein's net charge. At its pI, a protein has no net charge and will not bind the resin.

**Key concept:** A protein's charge depends on pH relative to its pI.
- If pH > pI, protein has net negative charge (will bind anion exchanger)
- If pH < pI, protein has net positive charge (will bind cation exchanger)
- At pH = pI, net charge is zero (will not bind either)

### Affinity Chromatography

The **most specific** chromatographic technique. The stationary phase has a **ligand** covalently attached that specifically binds the target molecule (like a lock and key).

**Examples:**
- Antibody attached to beads to capture a specific antigen
- Ni-NTA column to capture **His-tagged** recombinant proteins (very common in biochemistry research)
- Substrate analog to capture an enzyme
- Lectin column to capture glycoproteins

**How it works:**
1. Load the crude mixture onto the column
2. Wash with buffer -- everything that doesn't bind flows through
3. **Elute** the target by adding a competing ligand (e.g., excess free ligand, imidazole for His-tag) or by changing pH/ionic strength to disrupt binding

**Affinity chromatography gives the highest purity in a single step.** If a passage says "one-step purification" or "high specificity," think affinity.

---

## 4. Electrophoresis

Electrophoresis separates charged molecules in an **electric field**. Molecules migrate toward the electrode with the opposite charge. The rate of migration depends on **charge, size, and shape** (unless you control for some of those variables).

### Agarose Gel Electrophoresis

Used for **DNA and RNA** (nucleic acids).

- DNA has a uniform negative charge from its phosphate backbone (charge is proportional to length)
- Since the charge-to-mass ratio is roughly constant for all DNA fragments, separation is based almost entirely on **size**
- **Smaller fragments migrate faster** (navigate through the agarose pores more easily)
- **Larger fragments migrate slower** (impeded by the gel matrix)

**Loading:** Samples are mixed with loading dye (for visibility and to add density) and loaded into wells at the **negative electrode (cathode) end**. DNA migrates toward the **positive electrode (anode)** because it's negatively charged.

**Visualization:** Ethidium bromide (intercalates into DNA, fluoresces under UV) or safer alternatives like SYBR Green.

**Size determination:** Run a **molecular weight ladder** (standards of known sizes) alongside your samples. Compare migration distance.

### Native PAGE (Polyacrylamide Gel Electrophoresis)

For **proteins** under **non-denaturing conditions**.

- Proteins keep their native folded structure
- Separation depends on **charge, size, AND shape**
- Useful when you need to preserve enzyme activity or protein-protein interactions
- More difficult to interpret because multiple variables affect migration

### SDS-PAGE

The **workhorse** of protein analysis. This is extremely high-yield for the MCAT.

**SDS (sodium dodecyl sulfate)** is an anionic detergent that does two critical things:
1. **Denatures** the protein (unfolds it into a linear chain)
2. **Coats** the protein with a uniform negative charge proportional to its length (~1 SDS molecule per 2 amino acids)

Because every protein now has the same charge-to-mass ratio and the same shape (linear), separation is based on **molecular weight only**.

- **Smaller proteins migrate faster** (just like smaller DNA fragments)
- **Larger proteins migrate slower**

**Reducing conditions:** Adding **beta-mercaptoethanol** (BME) or **dithiothreitol** (DTT) breaks **disulfide bonds**. This is important for multi-subunit proteins:
- Without reducing agent: a dimer held by disulfide bonds runs as one large band
- With reducing agent: the subunits separate and you see two smaller bands

**MCAT trap:** If a passage shows SDS-PAGE under reducing vs. non-reducing conditions and asks you to interpret the band pattern, you need to know that the difference reveals disulfide-bonded subunits.

**Molecular weight estimation:** Run standards, plot log(MW) vs. migration distance. This gives a roughly linear relationship.

### Isoelectric Focusing (IEF)

Separates proteins by their **isoelectric point (pI)** -- the pH at which the protein has zero net charge.

**Setup:** A gel with an immobilized **pH gradient** (acidic on one end, basic on the other). Proteins are loaded and an electric field is applied.

**How it works:**
- A protein in a region more acidic than its pI will be positively charged and migrate toward the cathode (negative end)
- A protein in a region more basic than its pI will be negatively charged and migrate toward the anode (positive end)
- When it reaches the pH equal to its pI, it has **zero net charge and stops moving**

Each protein **focuses** into a sharp band at its pI. Beautiful separation.

### 2D Gel Electrophoresis

Combines **IEF (first dimension)** and **SDS-PAGE (second dimension)** for maximum resolution.

1. **First dimension:** Separate by pI using IEF (horizontal)
2. **Rotate the gel 90 degrees**, lay it on top of an SDS-PAGE gel
3. **Second dimension:** Separate by molecular weight using SDS-PAGE (vertical)

Result: Each protein is resolved as a **spot** defined by its unique pI and MW. This can resolve **thousands of proteins** in a single experiment. Used in proteomics.

---

## 5. Centrifugation

Centrifugation separates particles based on **size, shape, and density** by spinning them at high speed. The centrifugal force pushes denser/larger particles to the bottom of the tube (the **pellet**), while lighter/smaller material stays in the liquid above (the **supernatant**).

### Differential Centrifugation

**Sequential spins at increasing speeds** to fractionate cell components:

| Spin | Speed | What pellets |
|---|---|---|
| 1st (low speed) | ~1,000 x g | Whole cells, nuclei, large debris |
| 2nd | ~10,000 x g | Mitochondria, lysosomes, peroxisomes |
| 3rd | ~100,000 x g | Microsomes (ER fragments), plasma membrane fragments |
| 4th (ultracentrifugation) | >100,000 x g | Ribosomes, viruses, large macromolecules |

After each spin, you **pour off the supernatant** and spin it again at higher speed. Each pellet is enriched in a particular organelle fraction.

**MCAT application:** Passages love to describe a fractionation experiment and ask which enzyme activity you'd find in which pellet. Cytochrome c oxidase? Mitochondrial pellet (2nd spin). Glucose-6-phosphatase? ER fraction (3rd spin). Know where your key enzymes live.

### Density Gradient Ultracentrifugation

Instead of just pelleting, you separate components through a **pre-formed density gradient** (usually sucrose or cesium chloride).

**Two types:**

- **Rate-zonal (sucrose gradient):** Particles sediment through the gradient at different rates based on size and shape. You stop before anything reaches the bottom. Separates by **sedimentation coefficient (S value)** -- larger S = sediments faster.

- **Isopycnic (equilibrium, CsCl gradient):** Spin until every particle reaches the position in the gradient where **its density matches the surrounding medium density**. Separation is purely by **buoyant density**, regardless of size. This is how Meselson and Stahl separated 14N-DNA from 15N-DNA in the famous semiconservative replication experiment.

---

## 6. Other Techniques

### Recrystallization

A purification technique for **solids**.

**Principle:** Most solids are more soluble in hot solvent than cold solvent. Impurities are present in small amounts.

**Procedure:**
1. Dissolve the impure solid in a **minimum amount** of hot solvent
2. **Hot-filter** if there are insoluble impurities
3. **Cool slowly** -- the desired compound crystallizes out as pure crystals (slow cooling = larger, purer crystals)
4. The impurities remain dissolved in the **mother liquor** (because they're in low concentration, below their saturation point even when cold)
5. **Filter** to collect pure crystals; wash with cold solvent

**Choosing the solvent:** The ideal solvent dissolves your compound well when hot but poorly when cold. The compound should have a steep **solubility-temperature curve**.

### Filtration

- **Gravity filtration:** Pour liquid through filter paper in a funnel. Used to remove insoluble impurities from a hot solution (e.g., during recrystallization).
- **Vacuum filtration (Buchner funnel):** Apply vacuum to pull solvent through faster. Used to collect a solid product (like crystals from recrystallization) quickly while minimizing loss of product in residual solvent.

### Dialysis

Separates molecules based on **size** using a **semipermeable membrane** with a defined molecular weight cutoff (MWCO).

**How it works:** Place your protein solution in a dialysis bag (membrane), then submerge it in a large volume of buffer.
- **Small molecules** (salts, small metabolites, urea) pass through the membrane pores and equilibrate with the surrounding buffer
- **Large molecules** (proteins, DNA) are too big to pass through and are retained

**Uses:**
- **Buffer exchange:** Change the buffer composition around a protein
- **Desalting:** Remove salt after an ammonium sulfate precipitation
- **Remove small-molecule contaminants**

Dialysis relies on **diffusion down a concentration gradient**. Using a large volume of buffer (or changing the buffer multiple times) drives more complete removal of the small molecule.

---

## Decision Table: Which Technique for Which Purpose?

| Goal | Best Technique | Why |
|---|---|---|
| Separate organic compounds by acid/base properties | **Acid-base extraction** | Toggle charge with pH, exploit aqueous vs. organic solubility |
| Separate liquids with different boiling points | **Distillation** (simple if delta-BP > 25C, fractional if close) | Based on vapor pressure differences |
| Purify heat-sensitive liquid compounds | **Vacuum distillation** | Lowers BP, avoids decomposition |
| Quick check of reaction progress / purity | **TLC** | Fast, uses tiny amount of sample, visual |
| Bulk purification of organic mixture by polarity | **Column chromatography** | Preparative scale, polarity-based separation |
| High-resolution analytical separation of small molecules | **HPLC** | High pressure = fine separation, quantitative |
| Analyze volatile compounds | **Gas chromatography (GC)** | Separates by BP and polarity in gas phase |
| Separate proteins by size (native conditions) | **Size-exclusion chromatography** | Big elutes first, no denaturation |
| Separate proteins by charge | **Ion-exchange chromatography** | Binds by charge, elute with salt or pH gradient |
| Purify a specific protein from crude mixture | **Affinity chromatography** | Highest specificity and purity in one step |
| Separate DNA fragments by size | **Agarose gel electrophoresis** | Uniform charge-to-mass ratio, separates by size |
| Determine protein molecular weight (denatured) | **SDS-PAGE** | Uniform charge from SDS, separation by MW only |
| Separate proteins by pI | **Isoelectric focusing** | Proteins stop at their pI in pH gradient |
| Resolve complex protein mixtures (proteomics) | **2D gel electrophoresis** | IEF (pI) + SDS-PAGE (MW) = two-dimensional resolution |
| Fractionate cell organelles | **Differential centrifugation** | Sequential spins pellet increasingly smaller organelles |
| Separate by buoyant density | **Isopycnic ultracentrifugation (CsCl)** | Particles band at matching density |
| Purify a solid organic product | **Recrystallization** | Hot dissolve, slow cool, impurities stay in solution |
| Remove salt / exchange buffer for proteins | **Dialysis** or **size-exclusion chromatography** | Both separate by size; dialysis is simpler for buffer exchange |

---

## High-Yield Comparison: Don't Confuse These

| Concept | Technique A | Technique B | Key Difference |
|---|---|---|---|
| "Small elutes first" vs. "Big elutes first" | **Gel electrophoresis** -- small migrates faster through gel | **Size-exclusion chromatography** -- big elutes first (excluded from pores) | Opposite outcomes! |
| Normal phase vs. Reversed phase | Polar stationary phase (silica); nonpolar elutes first | Nonpolar stationary phase (C18); polar elutes first | Everything flips |
| SDS-PAGE vs. Native PAGE | Denatures + uniform charge = MW only | Native structure preserved = charge + size + shape | SDS simplifies interpretation |
| Cation vs. anion exchange | Negative beads bind cations (+) | Positive beads bind anions (-) | Named for what they exchange, not what the beads are |
| Differential vs. density gradient centrifugation | Sequential pellets at increasing speed | Continuous separation through gradient | Differential = crude fractions; gradient = finer resolution |

---

## Quick-Fire MCAT Connections

- **Acid-base extraction** connects to pKa, Henderson-Hasselbalch, and protonation states -- if pH is 2 units below the pKa of a carboxylic acid, the acid is >99% protonated (neutral, organic-soluble).
- **Distillation** connects to phase diagrams, Clausius-Clapeyron, intermolecular forces (stronger IMFs = higher BP), and colligative properties.
- **Chromatography polarity reasoning** connects to functional groups, hydrogen bonding, dipole-dipole interactions, and London dispersion forces. If the MCAT shows two structures and asks which has a higher Rf on TLC, compare polarity.
- **SDS-PAGE** connects to protein structure, disulfide bonds (cysteine), quaternary structure, and post-translational modifications.
- **IEF and ion exchange** connect to amino acid charge, pI calculations, and Henderson-Hasselbalch at the molecular level.
- **Centrifugation** connects to cell biology -- you need to know which organelles are in which fraction, and therefore which metabolic pathways are in which compartment.
- **Meselson-Stahl** = isopycnic CsCl ultracentrifugation. This is a crossover between DNA replication and separation techniques. Know it cold.

---

*Last updated: April 12, 2026 -- Phase 1 Content Review*
