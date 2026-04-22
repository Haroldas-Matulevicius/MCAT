# BB Chapter 9 — Carbohydrate Metabolism 1

Scope: Glucose transport, glycolysis, other monosaccharides, pyruvate dehydrogenase, glycogenesis/glycogenolysis, gluconeogenesis, pentose phosphate pathway.

**Section:** Bio/Biochem (BB)
**AAMC FC mapping:** FC1D (Metabolism)
**Kaplan Reference:** Biochemistry Chapter 9
**Yield:** One of the single most tested topics on the MCAT.

---

## 1. Glycolysis

**Location:** Cytoplasm (every cell in the body)
**Function:** Oxidize glucose (6C) into 2 pyruvate (3C each), capturing a small amount of energy as ATP and NADH.

Glycolysis has 10 enzymatic steps. You do NOT need to memorize all 10 for the MCAT. What you need cold are the **3 irreversible, regulated steps** -- these are the control points, and the MCAT tests regulation heavily.

### The 3 Committed Steps

| Step | Enzyme | Reaction | ATP Cost/Gain |
|------|--------|----------|---------------|
| 1 | **Hexokinase** (or **Glucokinase** in liver/pancreatic beta-cells) | Glucose --> Glucose-6-phosphate (G6P) | -1 ATP |
| 3 | **PFK-1** (phosphofructokinase-1) | Fructose-6-phosphate --> Fructose-1,6-bisphosphate | -1 ATP |
| 10 | **Pyruvate kinase** | Phosphoenolpyruvate (PEP) --> Pyruvate | +1 ATP (x2) |

Why are these irreversible? Because each has a large negative delta-G -- they release so much free energy that the reverse reaction is thermodynamically unfavorable under cellular conditions. This matters because **gluconeogenesis must use different enzymes to bypass these steps** (covered below in Gluconeogenesis).

### PFK-1: THE Rate-Limiting Step

PFK-1 is the **committed step** of glycolysis -- the point of no return. Once fructose-1,6-bisphosphate is formed, the molecule is committed to glycolysis. This is why PFK-1, not hexokinase, is considered the true rate-limiting enzyme: G6P can still be diverted to glycogen synthesis or the pentose phosphate pathway, but F-1,6-BP cannot.

**Allosteric regulation of PFK-1 (memorize this table):**

| Activators | Inhibitors |
|-----------|------------|
| **AMP** (low energy signal) | **ATP** (high energy -- "we have enough") |
| **Fructose-2,6-bisphosphate** (F-2,6-BP) -- the MOST potent activator | **Citrate** (first TCA intermediate -- signals TCA is backed up) |
| ADP | H+ (low pH -- protects against lactic acidosis) |

**F-2,6-BP deserves special attention.** It is made by **PFK-2** (phosphofructokinase-2), a bifunctional enzyme that has both kinase and phosphatase activity. Insulin stimulates the kinase domain (makes F-2,6-BP, activating glycolysis). Glucagon stimulates the phosphatase domain (destroys F-2,6-BP, slowing glycolysis). This is a classic MCAT question -- they will describe a signaling cascade and ask you to predict its effect on glycolytic rate.

### Hexokinase vs. Glucokinase

This comparison is extremely testable. Both phosphorylate glucose to G6P, but they serve different physiological roles:

| Property | Hexokinase | Glucokinase |
|----------|-----------|-------------|
| **Location** | Most tissues (muscle, brain, etc.) | Liver and pancreatic beta-cells |
| **Km** | Low (~0.1 mM) -- high affinity | High (~10 mM) -- low affinity |
| **Vmax** | Low | High |
| **Product inhibition** | Yes -- inhibited by G6P | No -- not inhibited by G6P |
| **Function** | Traps glucose in cells even at low [glucose] | Only active when blood glucose is HIGH (after a meal) -- acts as a glucose sensor |

Why does this matter? Hexokinase's low Km means it is saturated at normal blood glucose levels -- it is always working. Glucokinase's high Km means it only kicks in when blood glucose rises (postprandial), allowing the liver to buffer excess blood glucose. In pancreatic beta-cells, glucokinase acts as a **glucose sensor**: when glucose is high, glucokinase activity rises, increasing ATP production, closing K-ATP channels, depolarizing the cell, opening voltage-gated Ca2+ channels, and triggering insulin exocytosis.

### Net Yield of Glycolysis

Per glucose molecule:
- **2 ATP** (net) -- invest 2 in the preparatory phase, generate 4 in the payoff phase via substrate-level phosphorylation
- **2 NADH** -- produced at glyceraldehyde-3-phosphate dehydrogenase (step 6)
- **2 Pyruvate**

### Substrate-Level Phosphorylation vs. Oxidative Phosphorylation

| Feature | Substrate-Level | Oxidative |
|---------|----------------|-----------|
| **Mechanism** | Direct transfer of a phosphate group from a substrate to ADP | ATP synthase uses proton gradient to make ATP |
| **Where** | Cytoplasm (glycolysis) and mitochondrial matrix (TCA -- GTP) | Inner mitochondrial membrane |
| **O2 required?** | No | Yes |
| **ATP yield** | Small (4 ATP in glycolysis, 2 GTP in TCA per glucose) | Large (~26 ATP per glucose) |

The MCAT loves asking: "If O2 is absent, which type of phosphorylation can still occur?" Answer: substrate-level.

---

## 2. Fermentation

### Why Cells Ferment

Glycolysis requires NAD+ as an electron acceptor at step 6. Under aerobic conditions, the ETC regenerates NAD+ from NADH. But when O2 is absent (or the ETC is overwhelmed), NADH accumulates and NAD+ is depleted. Without NAD+, glycolysis stalls at step 6 and ATP production halts.

Fermentation exists for one purpose: **to regenerate NAD+** so glycolysis can continue. It does NOT produce additional ATP -- the ATP still comes from substrate-level phosphorylation in glycolysis.

### Lactic Acid Fermentation

**Pyruvate + NADH --> Lactate + NAD+**

Enzyme: **Lactate dehydrogenase (LDH)**

Occurs in: exercising skeletal muscle, RBCs (no mitochondria), and any tissue under hypoxic conditions.

Key point: Lactate is NOT a metabolic dead end. It is exported to the blood and taken up by the liver, where it is converted back to pyruvate and then to glucose via gluconeogenesis. This glucose is sent back to muscle. This is the **Cori cycle** (see Gluconeogenesis section).

### Alcohol Fermentation

**Pyruvate --> Acetaldehyde + CO2 --> Ethanol + NAD+**

Occurs in yeast and some bacteria, not in humans. Two enzymes:
1. **Pyruvate decarboxylase** (removes CO2, requires TPP)
2. **Alcohol dehydrogenase** (reduces acetaldehyde to ethanol, regenerating NAD+)

MCAT relevance: low. But they can test the concept of NAD+ regeneration.

### The Cori Cycle (Lactate Shuttle)

This is a metabolic cooperation between muscle and liver:

1. Working muscle produces lactate (via LDH) under anaerobic conditions
2. Lactate is exported to blood, taken up by liver
3. Liver converts lactate --> pyruvate --> glucose (via gluconeogenesis, costs 6 ATP)
4. Glucose is released back into blood, taken up by muscle

**Net cost:** 6 ATP per glucose (paid by the liver). This allows muscle to function anaerobically while the liver pays the energetic cost. The MCAT tests this as a metabolic integration concept: "Which organ is primarily responsible for recycling lactate?"

---

## 3. Pyruvate Dehydrogenase Complex (PDC)

**Location:** Mitochondrial matrix
**Reaction:** Pyruvate --> **Acetyl-CoA** + CO2 + NADH

This is the **bridge** between glycolysis (cytoplasm) and the TCA cycle (matrix). It is **irreversible** -- once pyruvate becomes acetyl-CoA, it cannot be converted back to glucose. This is why fatty acids (which degrade to acetyl-CoA via beta-oxidation) cannot be used for gluconeogenesis.

### The 5 Cofactors (Mnemonic: "Tender Loving Care For Nancy")

| Cofactor | Derived From | Role |
|----------|-------------|------|
| **TPP** (thiamine pyrophosphate) | Vitamin B1 (thiamine) | Decarboxylation |
| **Lipoic acid** (lipoamide) | Lipoic acid | Acyl transfer |
| **CoA** (coenzyme A) | Vitamin B5 (pantothenic acid) | Carries acetyl group |
| **FAD** | Vitamin B2 (riboflavin) | Electron carrier (reduced then reoxidized within the complex) |
| **NAD+** | Vitamin B3 (niacin) | Final electron acceptor -- reduced to NADH |

MCAT connection: Beriberi (B1/thiamine deficiency) impairs PDC, causing pyruvate and lactate accumulation. They may describe symptoms and ask which enzymatic step is affected.

### Regulation of PDC

- **Activated by:** high NAD+, CoA, ADP (low energy signals)
- **Inhibited by:** high NADH, acetyl-CoA, ATP (high energy signals -- products inhibit)
- **Covalent modification:** PDC is active when **dephosphorylated** (unusual -- most enzymes are activated by phosphorylation, but PDC is the opposite). PDH kinase phosphorylates and inactivates it; PDH phosphatase dephosphorylates and activates it.

### Per-Glucose Yield at PDC

Since each glucose gives 2 pyruvates, the PDC step produces:
- **2 Acetyl-CoA**
- **2 NADH**
- **2 CO2**

→ TCA cycle, ETC, oxidative phosphorylation: see Ch 10

---

## 7. Gluconeogenesis

**Location:** Primarily **liver** (90%) and **kidney cortex** (10%)
**Function:** Synthesize glucose from non-carbohydrate precursors (lactate, glycerol, glucogenic amino acids, pyruvate, TCA intermediates)
**When:** Fasting, starvation, prolonged exercise

Gluconeogenesis is essentially glycolysis in reverse, but the 3 irreversible glycolytic steps must be bypassed by different enzymes.

### The 4 Bypass Enzymes (Memorize These)

| Glycolysis Enzyme (forward) | Gluconeogenesis Bypass Enzyme (reverse) | Reaction |
|-----------------------------|-----------------------------------------|----------|
| Pyruvate kinase | **Pyruvate carboxylase** (mitochondrial) + **PEPCK** (cytoplasmic) | Pyruvate --> OAA (carboxylase, requires biotin + ATP) --> PEP (PEPCK, requires GTP) |
| PFK-1 | **Fructose-1,6-bisphosphatase** (F-1,6-BPase) | F-1,6-BP --> F-6-P |
| Hexokinase/Glucokinase | **Glucose-6-phosphatase** (G-6-Pase) | G-6-P --> Glucose |

**Critical point about glucose-6-phosphatase:** This enzyme is found ONLY in the **liver and kidney**. Muscle LACKS G-6-Pase, which is why muscle glycogen **cannot** contribute to blood glucose. Muscle can break down glycogen to G6P, but G6P stays trapped in the muscle cell and enters glycolysis. This is a classic MCAT question.

### Reciprocal Regulation of Glycolysis and Gluconeogenesis

The cell never runs both pathways simultaneously at full speed (that would be a futile cycle, wasting ATP). Regulation is reciprocal:

| Condition | Glycolysis | Gluconeogenesis |
|-----------|-----------|-----------------|
| Fed (insulin, high F-2,6-BP) | **ON** -- PFK-1 activated | **OFF** -- F-1,6-BPase inhibited |
| Fasting (glucagon, low F-2,6-BP) | **OFF** -- PFK-1 inhibited | **ON** -- F-1,6-BPase activated |
| High ATP/citrate | OFF | ON |
| High AMP | ON (PFK-1 activated) | OFF (F-1,6-BPase inhibited) |

F-2,6-BP activates PFK-1 but **inhibits** F-1,6-bisphosphatase. This single molecule acts as a metabolic switch between glycolysis and gluconeogenesis, controlled by the insulin/glucagon ratio via PFK-2.

### Gluconeogenesis Substrates

- **Lactate** (Cori cycle) -- most important quantitatively
- **Glycerol** (from TAG hydrolysis in adipose) -- enters as DHAP
- **Glucogenic amino acids** -- converted to pyruvate or TCA intermediates, then to OAA, then to PEP --> glucose
- **NOT acetyl-CoA** -- cannot be converted to glucose because PDC is irreversible and there is no net conversion of acetyl-CoA to OAA (the 2 carbons entering TCA as acetyl-CoA are lost as 2 CO2). This is why **fatty acids cannot be converted to glucose** (except for odd-chain FAs, which yield propionyl-CoA --> succinyl-CoA, a minor exception).

### Cori Cycle (Detailed)

Muscle (glycolysis under anaerobic conditions):
Glucose --> 2 Pyruvate --> 2 Lactate (via LDH, regenerating NAD+)

Lactate travels to liver via blood.

Liver (gluconeogenesis):
2 Lactate --> 2 Pyruvate --> Glucose (costs 6 ATP)

Glucose returns to muscle via blood.

**Energy balance:** Muscle gains 2 ATP per glucose (glycolysis). Liver spends 6 ATP per glucose (gluconeogenesis). Net cost to the organism: 4 ATP per cycle. The liver "subsidizes" the muscle's anaerobic work.

---

## 8. Glycogen Metabolism

**Location:** Liver (maintains blood glucose) and skeletal muscle (fuel for contraction)
**Storage form:** Glycogen -- branched polymer of glucose with alpha-1,4 linkages (linear) and alpha-1,6 linkages (branch points every 8--12 residues)

### Glycogenesis (Glycogen Synthesis)

Key enzyme: **Glycogen synthase** -- forms alpha-1,4 bonds, adding glucose units to the non-reducing end of existing glycogen chains. Requires **UDP-glucose** as the activated glucose donor.

**Branching enzyme** creates alpha-1,6 branch points by transferring a block of ~7 glucose residues from a chain end to an internal position.

### Glycogenolysis (Glycogen Breakdown)

Key enzyme: **Glycogen phosphorylase** -- cleaves alpha-1,4 bonds by phosphorolysis (uses Pi, not H2O), releasing **glucose-1-phosphate (G1P)**. G1P is converted to G6P by phosphoglucomutase.

**Debranching enzyme** has two activities:
1. **Transferase** -- moves 3 residues from a branch to the main chain
2. **Alpha-1,6-glucosidase** -- cleaves the single remaining alpha-1,6 glucose as free glucose (not G1P)

### Hormonal Control (Very High-Yield)

This is a signaling cascade question favorite:

**Glucagon (liver) or Epinephrine (muscle and liver):**
1. Binds GPCR (Gs-coupled)
2. Activates adenylyl cyclase
3. Increases cAMP
4. Activates **PKA** (protein kinase A)
5. PKA phosphorylates:
   - **Glycogen phosphorylase kinase** --> activates it --> it phosphorylates glycogen phosphorylase --> **activates** glycogenolysis
   - **Glycogen synthase** --> **inactivates** it --> shuts down glycogenesis

**Insulin (fed state):**
1. Binds receptor tyrosine kinase (RTK)
2. Activates phosphoprotein phosphatase-1 (PP1)
3. PP1 **dephosphorylates**:
   - Glycogen phosphorylase --> **inactivates** it (slows glycogenolysis)
   - Glycogen synthase --> **activates** it (promotes glycogenesis)

**Summary of phosphorylation states:**

| Enzyme | Phosphorylated | Dephosphorylated |
|--------|---------------|------------------|
| Glycogen synthase | INACTIVE | ACTIVE |
| Glycogen phosphorylase | ACTIVE | INACTIVE |

Mnemonic: **Synthase** works like a **light switch** -- it is ON when phosphate is OFF. **Phosphorylase** is like a **phospho-phile** -- it loves being phosphorylated and is ON in that state.

### Glycogen Storage Diseases (Low-Yield but Testable)

- **Von Gierke disease (Type I):** glucose-6-phosphatase deficiency --> severe fasting hypoglycemia, hepatomegaly
- **McArdle disease (Type V):** muscle glycogen phosphorylase deficiency --> exercise intolerance, no rise in blood lactate after exercise
- **Pompe disease (Type II):** lysosomal alpha-1,4-glucosidase (acid maltase) deficiency --> glycogen accumulation in lysosomes, cardiomegaly

---

## 9. Pentose Phosphate Pathway (PPP / Hexose Monophosphate Shunt)

**Location:** Cytoplasm
**Function:** Produce **NADPH** and **ribose-5-phosphate** -- NOT an ATP-generating pathway

### Oxidative Phase (Irreversible)

**G6P --> 6-phosphogluconate --> Ribulose-5-phosphate**

- Rate-limiting enzyme: **Glucose-6-phosphate dehydrogenase (G6PD)**
- Produces: **2 NADPH** per glucose-6-phosphate
- CO2 is released

G6PD is activated when the NADP+/NADPH ratio is high (cell needs NADPH). Insulin also stimulates the PPP.

### Non-Oxidative Phase (Reversible)

Interconverts sugars:
- **Ribulose-5-phosphate** <--> **Ribose-5-phosphate** (used for nucleotide and nucleic acid synthesis -- critical for dividing cells)
- Also produces fructose-6-phosphate and glyceraldehyde-3-phosphate, which can feed back into glycolysis

Key enzymes: **transketolase** (requires TPP/B1) and **transaldolase**

### NADPH: Why It Matters

NADPH is NOT the same as NADH. While NADH feeds the ETC to make ATP, NADPH is a **biosynthetic reducing agent:**

| NADPH Use | Details |
|-----------|---------|
| **Fatty acid synthesis** | FA synthase complex requires NADPH |
| **Steroid synthesis** | Cholesterol and steroid hormone biosynthesis |
| **Glutathione reduction** | Glutathione reductase uses NADPH to regenerate reduced glutathione (GSH), which neutralizes reactive oxygen species (ROS) via glutathione peroxidase |
| **Respiratory burst** | NADPH oxidase in phagocytes produces superoxide (O2-) to kill bacteria |
| **Cytochrome P450 reactions** | Drug metabolism, detoxification in liver |

### G6PD Deficiency (Clinical Correlation)

The most common human enzyme deficiency worldwide (X-linked). Without adequate NADPH, RBCs cannot regenerate GSH and are vulnerable to oxidative damage. Exposure to oxidative stressors (fava beans, sulfonamides, primaquine, infections) causes **hemolytic anemia** with **Heinz bodies** (denatured hemoglobin aggregates) and **bite cells** (splenic macrophages remove Heinz bodies).

Why RBCs specifically? They lack mitochondria and have no alternative source of NADPH.

---

## Other Monosaccharides

- **Fructose** → phosphorylated to F1P by fructokinase (liver) → cleaved by aldolase B to DHAP + glyceraldehyde; enters glycolysis below PFK-1 (bypasses its regulation — why high fructose intake can overwhelm liver metabolism)
- **Galactose** → G1P via Leloir pathway (galactokinase, GALT, epimerase) → G6P; GALT deficiency = **classic galactosemia** (galactitol accumulation, cataracts, liver damage)
- **Mannose** → M6P → F6P (enters glycolysis)

→ TCA cycle, ETC, oxidative phosphorylation: see Ch 10
→ Bioenergetics integration, ATP accounting, metabolic states, hormonal regulation: see Ch 12
