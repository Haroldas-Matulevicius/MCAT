# FC1D: Metabolism -- Deep-Dive Study Guide

**Section:** Bio/Biochem (BB)
**Kaplan Reference:** Biochemistry Ch 9--12
**Yield:** One of the single most tested topics on the MCAT. Expect 8--12 questions directly or indirectly on metabolism per exam. Integration questions are especially common.

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

Why are these irreversible? Because each has a large negative delta-G -- they release so much free energy that the reverse reaction is thermodynamically unfavorable under cellular conditions. This matters because **gluconeogenesis must use different enzymes to bypass these steps** (covered in Section 7).

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

Key point: Lactate is NOT a metabolic dead end. It is exported to the blood and taken up by the liver, where it is converted back to pyruvate and then to glucose via gluconeogenesis. This glucose is sent back to muscle. This is the **Cori cycle** (see Section 7).

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

---

## 4. TCA Cycle (Krebs Cycle / Citric Acid Cycle)

**Location:** Mitochondrial matrix
**Function:** Fully oxidize acetyl-CoA, harvesting electrons as NADH and FADH2, releasing CO2.

### Per Acetyl-CoA Yield

| Product | Amount |
|---------|--------|
| NADH | 3 |
| FADH2 | 1 |
| GTP | 1 (substrate-level phosphorylation, equivalent to 1 ATP) |
| CO2 | 2 |

**Per glucose** (2 acetyl-CoA): 6 NADH, 2 FADH2, 2 GTP, 4 CO2.

### The 3 Regulated Enzymes

These are all **irreversible** steps and are the control points of the cycle:

| Enzyme | Reaction | Activators | Inhibitors |
|--------|----------|-----------|------------|
| **Citrate synthase** | OAA + Acetyl-CoA --> Citrate | ADP, substrate availability | ATP, NADH, citrate (product) |
| **Isocitrate dehydrogenase** | Isocitrate --> alpha-ketoglutarate + CO2 | ADP, Ca2+ | ATP, NADH |
| **Alpha-ketoglutarate dehydrogenase** | alpha-KG --> Succinyl-CoA + CO2 | Ca2+ | ATP, NADH, succinyl-CoA (product) |

Pattern to notice: **ATP and NADH inhibit all three regulated enzymes.** When the cell has plenty of energy, TCA slows down. When energy is low (high ADP, high NAD+), TCA speeds up. This is a unifying principle of metabolic regulation.

Alpha-ketoglutarate dehydrogenase structurally resembles PDC and uses the same 5 cofactors (TPP, lipoic acid, CoA, FAD, NAD+).

### Why Is It a Cycle? Oxaloacetate Regeneration

The last step of the TCA cycle regenerates **oxaloacetate (OAA)**, which combines with a new acetyl-CoA to form citrate and restart the cycle. If OAA is depleted, the cycle stalls. This is why **anaplerotic reactions** exist.

### Anaplerotic Reactions (Refilling Reactions)

These replenish TCA intermediates that get siphoned off for biosynthesis:

- **Pyruvate carboxylase:** Pyruvate + CO2 --> OAA (the most important one; requires biotin as a cofactor; activated by acetyl-CoA)
- Glutamate --> alpha-ketoglutarate (via transamination or glutamate dehydrogenase)
- Aspartate --> OAA (via transamination)

MCAT logic: "If a cell is using TCA intermediates for amino acid synthesis, what happens to TCA flux?" It decreases unless anaplerotic reactions compensate.

---

## 5. Electron Transport Chain (ETC)

**Location:** Inner mitochondrial membrane
**Function:** Transfer electrons from NADH and FADH2 to O2, using the released energy to pump H+ from the matrix into the intermembrane space (IMS), creating a proton gradient (proton-motive force).

### The Complexes

| Complex | Name | Electron Donor | Electron Acceptor | H+ Pumped | Notes |
|---------|------|----------------|-------------------|-----------|-------|
| **I** | NADH dehydrogenase | NADH | CoQ (ubiquinone) | **4** | Contains FMN and Fe-S clusters |
| **II** | Succinate dehydrogenase | FADH2 | CoQ | **0** | Also a TCA enzyme (step 6); no H+ pumping |
| **III** | Cytochrome bc1 | CoQH2 | Cytochrome c | **4** | Q cycle mechanism |
| **IV** | Cytochrome c oxidase | Cytochrome c | **O2** --> H2O | **2** | Final electron acceptor; 4 electrons reduce O2 |

**Mobile carriers:**
- **Coenzyme Q (CoQ/ubiquinone):** lipid-soluble, shuttles electrons from Complex I and II to Complex III within the membrane
- **Cytochrome c:** water-soluble protein in the IMS, shuttles electrons from III to IV

### Why FADH2 Yields Less ATP Than NADH

NADH donates electrons to Complex I, which pumps 4 H+. FADH2 donates electrons to Complex II, which pumps **zero** H+. After Complex II, both pathways converge at CoQ and then Complexes III and IV. So FADH2 misses one round of proton pumping. Fewer protons pumped = less driving force for ATP synthase = fewer ATP.

- NADH: 4 + 4 + 2 = **10 H+ pumped** --> ~2.5 ATP
- FADH2: 0 + 4 + 2 = **6 H+ pumped** --> ~1.5 ATP

### ETC Inhibitors (High-Yield -- Memorize These)

| Inhibitor | Target | Effect |
|-----------|--------|--------|
| **Rotenone** | Complex I | Blocks NADH electron transfer; FADH2-linked substrates still work |
| **Antimycin A** | Complex III | Blocks electron flow from CoQH2 to Cyt c |
| **Cyanide (CN-)** | Complex IV | Binds Fe3+ in cytochrome a3; blocks O2 reduction |
| **Carbon monoxide (CO)** | Complex IV | Same target as cyanide |
| **Oligomycin** | ATP synthase (F0 subunit) | Blocks the proton channel; H+ cannot flow through; gradient builds but no ATP is made; ETC also backs up because gradient too high |

**What happens when you block a complex?** All complexes upstream of the block become fully reduced (cannot pass their electrons). All complexes downstream become fully oxidized (no electrons arrive). NADH accumulates, NAD+ drops, TCA slows, glycolysis may speed up (Pasteur effect).

### Uncouplers: DNP and Thermogenin

**Uncouplers** dissipate the proton gradient by allowing H+ to leak across the inner membrane **without going through ATP synthase**. The result:

- ETC runs at **maximum rate** (no back-pressure from gradient)
- O2 consumption **increases**
- ATP production **decreases** (no gradient to drive ATP synthase)
- Energy is released as **heat**

| Uncoupler | Context |
|-----------|---------|
| **2,4-Dinitrophenol (DNP)** | Chemical uncoupler; was used as a diet drug (caused dangerous hyperthermia) |
| **Thermogenin (UCP1)** | Natural uncoupling protein in **brown adipose tissue**; generates heat in newborns and hibernating animals (non-shivering thermogenesis) |

MCAT question pattern: "A drug increases O2 consumption but decreases ATP production. What is its mechanism?" Answer: uncoupler.

Contrast with oligomycin: oligomycin **decreases** both O2 consumption and ATP production (ETC backs up). An uncoupler **increases** O2 consumption but **decreases** ATP production.

---

## 6. Oxidative Phosphorylation

### Chemiosmotic Theory (Peter Mitchell, Nobel Prize 1978)

The energy stored in the electrochemical proton gradient (proton-motive force) across the inner mitochondrial membrane drives ATP synthesis. The gradient has two components:
1. **Chemical gradient (delta-pH):** higher H+ concentration in the IMS
2. **Electrical gradient (membrane potential):** IMS is more positive

H+ flows down this gradient through **ATP synthase** (Complex V), a molecular rotary motor. The F0 subunit is the proton channel embedded in the membrane. The F1 subunit is the catalytic head that protrudes into the matrix and synthesizes ATP.

As protons flow through F0, it rotates, causing conformational changes in the F1 beta subunits that catalyze: ADP + Pi --> ATP.

### P/O Ratios

The P/O ratio is the number of ATP molecules produced per atom of oxygen consumed (per pair of electrons transferred):

- **NADH:** P/O = ~2.5 (10 H+ pumped / ~4 H+ per ATP)
- **FADH2:** P/O = ~1.5 (6 H+ pumped / ~4 H+ per ATP)

Note: Older textbooks use 3 and 2. The MCAT uses ~2.5 and ~1.5 (or sometimes "approximately 3" and "approximately 2"). Know both conventions.

### Total ATP Yield Per Glucose (~30--32 ATP)

Let us trace every ATP-generating event:

| Source | Yield | ATP Equivalent |
|--------|-------|----------------|
| Glycolysis: substrate-level phosphorylation | 2 ATP | 2 |
| Glycolysis: 2 NADH | 2 NADH | ~3--5 (depends on shuttle; see below) |
| PDC: 2 NADH | 2 NADH | 5 |
| TCA: 6 NADH | 6 NADH | 15 |
| TCA: 2 FADH2 | 2 FADH2 | 3 |
| TCA: 2 GTP | 2 GTP | 2 |
| **Total** | | **~30--32** |

### Why the Range (30 vs. 32)?

The 2 NADH produced in glycolysis are in the **cytoplasm** and cannot cross the inner mitochondrial membrane directly. They must use shuttle systems:

- **Malate-aspartate shuttle** (liver, heart): transfers electrons to mitochondrial NAD+ --> produces NADH in the matrix --> 2.5 ATP each = **5 ATP total**
- **Glycerol-3-phosphate shuttle** (skeletal muscle, brain): transfers electrons to mitochondrial FAD --> produces FADH2 in the matrix --> 1.5 ATP each = **3 ATP total**

If the malate-aspartate shuttle is used: 32 ATP. If the glycerol-3-phosphate shuttle is used: 30 ATP. Most cells use a mix, so we say ~30--32.

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

## 10. Lipid Metabolism

### Beta-Oxidation (Fatty Acid Degradation)

**Location:** Mitochondrial matrix
**Function:** Break down fatty acids into acetyl-CoA units, generating NADH and FADH2

**Step 1 -- Activation (cytoplasm):**
Fatty acid + CoA --> **Fatty acyl-CoA** (costs 2 ATP equivalents -- ATP --> AMP + PPi, and PPi is hydrolyzed)

**Step 2 -- Carnitine Shuttle (into mitochondria):**
Long-chain fatty acyl-CoA cannot cross the inner mitochondrial membrane. The carnitine shuttle transfers it:
1. **CPT-I (carnitine palmitoyltransferase I)** on the outer membrane: fatty acyl-CoA + carnitine --> fatty acyl-carnitine + CoA
2. **Translocase** moves fatty acyl-carnitine across the inner membrane
3. **CPT-II** on the inner membrane: regenerates fatty acyl-CoA in the matrix

**CPT-I is the rate-limiting step of beta-oxidation.** It is inhibited by **malonyl-CoA** (the first committed intermediate of fatty acid synthesis). This is reciprocal regulation -- when the cell is making fat, it blocks fat breakdown.

**Step 3 -- Beta-oxidation spiral:** Each cycle clips off a 2-carbon acetyl-CoA and produces:
- 1 FADH2
- 1 NADH
- 1 Acetyl-CoA

**Per-cycle yield for a 16-carbon fatty acid (palmitate):**
- 7 cycles (n/2 - 1 cycles for an even-chain FA)
- 8 Acetyl-CoA
- 7 FADH2
- 7 NADH

**Total ATP from palmitate:**
- 8 Acetyl-CoA x 10 ATP (from TCA + ETC) = 80
- 7 FADH2 x 1.5 = 10.5
- 7 NADH x 2.5 = 17.5
- Subtract 2 ATP for activation
- **Total: ~106 ATP** (compare to ~30--32 from glucose -- FAs are much more energy-dense)

**Odd-chain fatty acids:** The final cycle produces **propionyl-CoA** (3C) instead of acetyl-CoA. Propionyl-CoA is converted to **succinyl-CoA** (a TCA intermediate) via methylmalonyl-CoA. This requires **vitamin B12**. Since succinyl-CoA is a TCA intermediate that can form OAA, odd-chain FAs can technically contribute to gluconeogenesis (the only exception to "fats cannot make glucose").

### Fatty Acid Synthesis

**Location:** Cytoplasm
**Rate-limiting enzyme:** **Acetyl-CoA carboxylase (ACC)** -- converts acetyl-CoA to malonyl-CoA (requires biotin)

| Feature | Beta-Oxidation | FA Synthesis |
|---------|---------------|--------------|
| Location | Mitochondrial matrix | Cytoplasm |
| Carrier | CoA | ACP (acyl carrier protein) |
| 2C units | Acetyl-CoA removed | Malonyl-CoA added |
| Electron carrier | NAD+, FAD (oxidized) | NADPH (reduced) |
| Rate-limiting enzyme | CPT-I | Acetyl-CoA carboxylase |

**ACC regulation:**
- Activated by: **insulin**, **citrate**
- Inhibited by: **glucagon**, **epinephrine** (via AMPK phosphorylation), **palmitoyl-CoA** (product feedback)

**Citrate shuttle:** Acetyl-CoA is produced in the mitochondrial matrix (from PDC or beta-oxidation) but FA synthesis occurs in the cytoplasm. Acetyl-CoA cannot cross the membrane directly. Instead:
1. Acetyl-CoA + OAA --> Citrate (citrate synthase, in matrix)
2. Citrate exits to cytoplasm via citrate transporter
3. **ATP-citrate lyase** cleaves citrate --> acetyl-CoA + OAA (in cytoplasm)

### Ketogenesis

**Location:** Liver mitochondria (ONLY the liver makes ketone bodies; the liver CANNOT use them because it lacks beta-ketoacyl-CoA transferase/thiophorase)

**When:** Prolonged fasting, starvation, uncontrolled diabetes (high glucagon/insulin ratio, high acetyl-CoA from beta-oxidation, OAA diverted to gluconeogenesis so TCA slows, acetyl-CoA accumulates)

**Ketone bodies produced:**
1. **Acetoacetate**
2. **Beta-hydroxybutyrate** (the most abundant in blood, technically not a ketone)
3. **Acetone** (volatile, exhaled -- "fruity breath" in diabetic ketoacidosis)

**Who uses ketone bodies?**
- **Heart** (preferred fuel even in fed state)
- **Brain** (after several days of starvation, adapts to use ketones for up to ~75% of energy needs, sparing glucose and reducing the need for muscle protein catabolism)
- **Skeletal muscle** (uses them during early starvation)
- **NOT the liver** and **NOT RBCs** (RBCs lack mitochondria)

**Ketone body utilization:**
Beta-hydroxybutyrate --> acetoacetate --> acetoacetyl-CoA (via thiophorase/succinyl-CoA-acetoacetate CoA transferase) --> 2 Acetyl-CoA --> TCA cycle

**Diabetic ketoacidosis (DKA):** In type 1 diabetes, the absence of insulin causes uncontrolled lipolysis and beta-oxidation. Massive ketone body production overwhelms buffering capacity, dropping blood pH (metabolic acidosis with increased anion gap). Key findings: Kussmaul breathing (deep, rapid -- respiratory compensation), fruity breath (acetone), hyperglycemia, ketonuria.

---

## 11. Amino Acid Metabolism

### Transamination

**Aminotransferases (transaminases)** transfer an amino group from an amino acid to **alpha-ketoglutarate**, producing a new alpha-keto acid and **glutamate**.

- All transaminases require **PLP (pyridoxal phosphate)**, the active form of **vitamin B6**
- Clinically important: **ALT** (alanine aminotransferase, liver-specific) and **AST** (aspartate aminotransferase, liver + heart + muscle)
- Elevated ALT/AST = liver damage (hepatitis, etc.)

The **alanine cycle** (glucose-alanine cycle) is the amino acid equivalent of the Cori cycle:
1. Muscle breaks down amino acids during exercise/fasting
2. The amino group is transferred to pyruvate --> **alanine** (via ALT)
3. Alanine travels to the liver
4. Liver ALT converts alanine --> pyruvate + glutamate
5. Pyruvate enters gluconeogenesis --> glucose returns to muscle
6. Glutamate's amino group enters the urea cycle

### Oxidative Deamination

**Glutamate dehydrogenase** removes the amino group from glutamate, releasing **NH4+ (ammonium)** and regenerating alpha-ketoglutarate.

Glutamate --> alpha-ketoglutarate + NH4+ + NADH (or NADPH)

This is the main pathway by which amino groups are funneled into NH4+ for disposal via the urea cycle.

### The Urea Cycle

**Location:** Begins in the mitochondrial matrix (first 2 steps), continues in the cytoplasm (remaining steps) -- liver only

**Purpose:** Detoxify ammonia (NH3/NH4+), which is neurotoxic, by converting it to **urea** (2 NH2 groups + CO2) for renal excretion.

**Cost:** 3 ATP per urea (technically 4 high-energy phosphate bonds: 2 ATP --> 2 ADP + 2 Pi in the first step, and 1 ATP --> AMP + PPi in the argininosuccinate synthetase step)

Key steps:
1. **Carbamoyl phosphate synthetase I (CPS-I)** -- rate-limiting, mitochondrial matrix, activated by **N-acetylglutamate**
2. OTC (ornithine transcarbamylase) -- still in matrix
3. Argininosuccinate synthetase -- cytoplasm
4. Argininosuccinate lyase -- cytoplasm, also produces fumarate (links to TCA!)
5. Arginase -- cleaves arginine into **urea** + ornithine (ornithine re-enters the cycle)

**Hyperammonemia:** If the urea cycle is impaired (genetic deficiency, liver failure), NH4+ accumulates --> brain swelling, confusion, coma, death. The most common inherited deficiency is **OTC deficiency** (X-linked).

### Glucogenic vs. Ketogenic Amino Acids

| Category | Definition | Carbon skeleton enters as... |
|----------|-----------|------------------------------|
| **Glucogenic** | Can be converted to glucose | Pyruvate or TCA intermediates (OAA, alpha-KG, succinyl-CoA, fumarate) |
| **Ketogenic** | Can be converted to ketone bodies | Acetyl-CoA or acetoacetyl-CoA |
| **Both** | Can go either way | Parts go to both |

**Only leucine (Leu) and lysine (Lys) are purely ketogenic.** Mnemonic: the **LL** amino acids are **L**ocked into **L**ipid metabolism.

**Both glucogenic and ketogenic:** Isoleucine, Phenylalanine, Tryptophan, Tyrosine, Threonine (mnemonic: **I** **P**hone **T**hree -- Ile, Phe, Trp, Tyr, Thr).

All remaining amino acids are purely glucogenic.

---

## 12. Metabolic Integration

This is the most MCAT-relevant section. The exam rarely tests isolated pathways -- instead, it presents a physiological scenario and asks you to predict which pathways are active, which hormones are dominant, and what happens in specific tissues.

### The Three Metabolic States

#### Fed State (Absorptive, ~0--4 hours after a meal)

**Dominant hormone:** Insulin (secreted by pancreatic beta-cells in response to high blood glucose, amino acids, and GI hormones like GLP-1 and GIP)

**Insulin's effects:**

| Pathway | Status | Mechanism |
|---------|--------|-----------|
| Glycolysis | **ON** | Insulin induces glucokinase, PFK-1 (via F-2,6-BP), pyruvate kinase |
| Glycogenesis | **ON** | Insulin activates PP1 --> dephosphorylates/activates glycogen synthase |
| Fatty acid synthesis | **ON** | Insulin activates ACC, induces FA synthase, induces ATP-citrate lyase |
| Protein synthesis | **ON** | Insulin activates mTOR pathway |
| Gluconeogenesis | **OFF** | F-2,6-BP inhibits F-1,6-BPase; insulin represses PEPCK gene expression |
| Glycogenolysis | **OFF** | PP1 dephosphorylates/inactivates glycogen phosphorylase |
| Beta-oxidation | **OFF** | Malonyl-CoA (from active ACC) inhibits CPT-I |
| Lipolysis | **OFF** | Insulin activates phosphodiesterase (degrades cAMP) and phosphoprotein phosphatase, inactivating hormone-sensitive lipase |

**Big picture:** Store everything. Glucose is taken up and stored as glycogen (liver, muscle) or converted to fat (liver, adipose). Amino acids are used for protein synthesis. Dietary fat is stored as TAG.

#### Fasting State (~4--24 hours without eating)

**Dominant hormone:** Glucagon (secreted by pancreatic alpha-cells in response to low blood glucose)

**Glucagon's effects (mainly on the liver via Gs-coupled GPCR --> cAMP --> PKA):**

| Pathway | Status | Mechanism |
|---------|--------|-----------|
| Glycogenolysis | **ON** | PKA cascade activates glycogen phosphorylase |
| Gluconeogenesis | **ON** | PKA activates phosphatase domain of PFK-2, reducing F-2,6-BP; glucagon induces PEPCK gene |
| Beta-oxidation | **ON** | Low insulin means ACC is off, malonyl-CoA drops, CPT-I is disinhibited |
| Glycolysis | **OFF** | F-2,6-BP low, PFK-1 less active |
| Glycogenesis | **OFF** | PKA phosphorylates/inactivates glycogen synthase |
| FA synthesis | **OFF** | ACC phosphorylated/inactivated by AMPK |

**Big picture:** Maintain blood glucose for the brain. Liver breaks down glycogen (first 4--12 hours) and then increasingly relies on gluconeogenesis (after 12+ hours). Adipose tissue releases fatty acids (lipolysis) as an alternative fuel for muscle, heart, and liver.

#### Starvation (>24 hours, extending to days/weeks)

**Dominant hormones:** Glucagon (still high) + **Cortisol** (from adrenal cortex, stimulated by ACTH)

Changes from fasting state:
- Liver glycogen is **depleted** (within 24--48 hours)
- **Gluconeogenesis** becomes the sole source of blood glucose, using:
  - Glycerol from TAG hydrolysis
  - Amino acids from muscle protein breakdown (cortisol promotes proteolysis)
  - Lactate from anaerobic glycolysis in other tissues
- **Ketogenesis** ramps up significantly in the liver as beta-oxidation produces excess acetyl-CoA that cannot enter TCA (OAA is diverted to gluconeogenesis)
- **Brain adaptation:** After 3--5 days, the brain upregulates enzymes for ketone body utilization, getting ~60--75% of its energy from ketones. This is critical because it **reduces the need for gluconeogenesis from amino acids**, sparing muscle protein.

**Starvation timeline:**
1. Hours 0--4: Fed state, insulin high
2. Hours 4--18: Glycogenolysis dominant
3. Hours 18--48: Glycogenolysis declining, gluconeogenesis increasing
4. Days 2--7: Gluconeogenesis from amino acids peaks, ketogenesis increasing
5. Weeks 2+: Ketone bodies are the primary fuel for most tissues, gluconeogenesis decreases (sparing protein), muscle shifts from amino acid breakdown to minimal protein loss

### Tissue-Specific Metabolism

This is where integration questions come from. Each tissue has a unique metabolic profile:

#### Liver (The Metabolic Hub)

- Has ALL major metabolic pathways
- Maintains blood glucose: gluconeogenesis, glycogenolysis, glucose-6-phosphatase
- Detoxifies ammonia via the urea cycle
- Makes ketone bodies but CANNOT use them (lacks thiophorase)
- Makes VLDL to export TAG to other tissues
- First-pass metabolism of drugs, alcohol, toxins
- Makes bile salts from cholesterol
- Responds to both insulin and glucagon

#### Skeletal Muscle

- Major glucose consumer during exercise (GLUT4, insulin-dependent)
- Stores glycogen for LOCAL use only (lacks glucose-6-phosphatase, cannot export glucose)
- Uses fatty acids at rest, glucose + glycogen during exercise
- Cannot perform gluconeogenesis
- Exports lactate (Cori cycle) and alanine (glucose-alanine cycle) to liver
- In starvation: protein is broken down for amino acids (gluconeogenic substrates)

#### Brain

- **Obligate glucose user** under normal conditions (~120 g/day)
- Cannot use fatty acids (FAs cannot cross the blood-brain barrier efficiently, and brain lacks significant beta-oxidation capacity)
- CAN adapt to use ketone bodies during starvation (after 3--5 days)
- Highly sensitive to hypoglycemia -- confusion, seizures, coma, death
- Uses GLUT1 and GLUT3 (insulin-independent -- brain always gets glucose)

#### Adipose Tissue

- Stores TAG (triglycerides) in the fed state via lipoprotein lipase (LPL) on capillary endothelium
- Releases fatty acids + glycerol during fasting via **hormone-sensitive lipase (HSL)**, activated by glucagon/epinephrine (PKA phosphorylates HSL)
- Insulin inhibits HSL (anti-lipolytic)
- Glycerol goes to liver for gluconeogenesis (adipose lacks glycerol kinase to reuse it)
- Brown adipose: contains thermogenin (UCP1), generates heat

#### Red Blood Cells

- **No mitochondria** -- rely entirely on glycolysis for ATP
- Produce lactate as the end product (Cori cycle substrate)
- Active PPP for NADPH (ROS defense via glutathione)
- Cannot use fatty acids, ketone bodies, or amino acids for energy

#### Heart

- Aerobic powerhouse with abundant mitochondria
- **Preferred fuels (in order):** fatty acids > ketone bodies > lactate > glucose
- CAN use lactate as fuel (has LDH that runs in reverse: lactate --> pyruvate)
- During exercise, the heart actually benefits from elevated blood lactate

### Predicting Active Pathways from a Scenario

When the MCAT gives you a clinical or experimental scenario, use this framework:

1. **What is the metabolic state?** (Fed, fasting, starving, exercising?)
2. **What is the dominant hormone?** (Insulin = anabolic/storage; Glucagon/Epi/Cortisol = catabolic/mobilization)
3. **What tissue are we asking about?** (Each has a unique enzyme profile)
4. **What are the energy signals?** (High ATP/NADH = slow catabolism; Low ATP/high AMP = speed up catabolism)

**Example question framework:**

*"A patient has been fasting for 36 hours. Which pathway is most active in the liver?"*

Analysis: 36 hours = liver glycogen mostly depleted, gluconeogenesis is the primary pathway maintaining blood glucose. Beta-oxidation is also very active (providing acetyl-CoA for energy and OAA consumption for gluconeogenesis). Ketogenesis is ramping up.

Answer: Gluconeogenesis.

*"After a carbohydrate-rich meal, what happens to PFK-1 activity in the liver?"*

Analysis: Fed state = insulin up, glucagon down. Insulin activates PFK-2 kinase domain --> increased F-2,6-BP --> allosteric activation of PFK-1. Also, ATP/citrate may be elevated (inhibiting PFK-1), but the F-2,6-BP signal dominates.

Answer: PFK-1 activity increases.

### Hormonal Summary Table

| Hormone | Source | Trigger | Key Metabolic Effects |
|---------|--------|---------|----------------------|
| **Insulin** | Beta-cells (pancreas) | High glucose, AAs, GLP-1 | Promotes storage: glycogenesis, lipogenesis, protein synthesis, glycolysis, glucose uptake (GLUT4) |
| **Glucagon** | Alpha-cells (pancreas) | Low glucose, high AAs (especially arginine) | Promotes mobilization: glycogenolysis, gluconeogenesis, beta-oxidation, ketogenesis |
| **Epinephrine** | Adrenal medulla | Stress, exercise | Like glucagon but also acts on muscle: glycogenolysis, lipolysis, increased cardiac output |
| **Cortisol** | Adrenal cortex | Stress, ACTH (from pituitary) | Proteolysis (muscle), gluconeogenesis (liver), lipolysis, anti-inflammatory, immunosuppressive |
| **Insulin-like Growth Factor (IGF)** | Liver | Growth hormone | Promotes protein synthesis and growth |
| **Thyroid hormones (T3/T4)** | Thyroid | TSH | Increase basal metabolic rate, increase O2 consumption, synergize with catecholamines |

---

## Quick-Reference: ATP Accounting Per Glucose

| Stage | Location | ATP | NADH | FADH2 | GTP |
|-------|----------|-----|------|-------|-----|
| Glycolysis | Cytoplasm | +2 (net) | +2 | -- | -- |
| Pyruvate dehydrogenase (x2) | Mito matrix | -- | +2 | -- | -- |
| TCA cycle (x2) | Mito matrix | -- | +6 | +2 | +2 |
| **Subtotal** | | **2 ATP + 2 GTP** | **10 NADH** | **2 FADH2** | |
| ETC/Ox Phos | Inner mito membrane | 10 x 2.5 = 25 | | 2 x 1.5 = 3 | 2 GTP = 2 |
| **Grand Total** | | **~30--32 ATP** | | | |

The range (30 vs 32) depends on the NADH shuttle used for the 2 glycolytic NADH (see Section 6).

---

## Quick-Reference: Key Enzyme Regulators

| Enzyme | Pathway | Activators | Inhibitors |
|--------|---------|-----------|------------|
| **PFK-1** | Glycolysis | AMP, F-2,6-BP | ATP, citrate, H+ |
| **Pyruvate kinase** | Glycolysis | F-1,6-BP (feedforward) | ATP, alanine, glucagon (liver) |
| **PDC** | Pyruvate --> Acetyl-CoA | NAD+, CoA, ADP | NADH, acetyl-CoA, ATP |
| **Citrate synthase** | TCA | ADP | ATP, NADH, citrate |
| **Isocitrate DH** | TCA | ADP, Ca2+ | ATP, NADH |
| **Alpha-KG DH** | TCA | Ca2+ | ATP, NADH, succinyl-CoA |
| **Pyruvate carboxylase** | Gluconeogenesis | Acetyl-CoA | ADP |
| **F-1,6-bisphosphatase** | Gluconeogenesis | Citrate, ATP | AMP, F-2,6-BP |
| **Acetyl-CoA carboxylase** | FA synthesis | Insulin, citrate | Glucagon (AMPK), palmitoyl-CoA |
| **CPT-I** | Beta-oxidation | -- | Malonyl-CoA |
| **Glycogen synthase** | Glycogenesis | Insulin (dephos), G6P | Glucagon/epi (phosphorylation via PKA) |
| **Glycogen phosphorylase** | Glycogenolysis | Glucagon/epi (phosphorylation), AMP (muscle) | Insulin (dephos), ATP, G6P |
| **G6P dehydrogenase** | PPP | High NADP+/NADPH ratio | NADPH |
| **HMG-CoA reductase** | Cholesterol synthesis | Insulin | Glucagon, statins, cholesterol |

---

## High-Yield Integration Concepts to Memorize

1. **Fatty acids cannot be converted to glucose** (PDC is irreversible; 2C acetyl-CoA carbons are lost as CO2 in TCA). Only exception: odd-chain FAs via propionyl-CoA --> succinyl-CoA.

2. **Muscle cannot export glucose** (lacks glucose-6-phosphatase). Muscle glycogen is for muscle only.

3. **Liver makes but cannot use ketone bodies** (lacks thiophorase). Brain, heart, and muscle use them.

4. **RBCs depend entirely on glycolysis** (no mitochondria). They produce lactate, not CO2.

5. **The brain is normally glucose-dependent but ketone-adaptable.** This adaptation is what allows survival during starvation lasting weeks.

6. **Malonyl-CoA is the metabolic switch** between FA synthesis and beta-oxidation. When ACC is active (fed state), malonyl-CoA accumulates, inhibiting CPT-I and blocking beta-oxidation. When ACC is off (fasting), malonyl-CoA drops and beta-oxidation proceeds.

7. **F-2,6-BP is the metabolic switch** between glycolysis and gluconeogenesis. Controlled by the insulin/glucagon ratio via PFK-2.

8. **Acetyl-CoA activates pyruvate carboxylase.** When beta-oxidation floods the matrix with acetyl-CoA, pyruvate carboxylase is activated, converting pyruvate to OAA for gluconeogenesis. This links fat breakdown to glucose production.

9. **Citrate is a crossover signal.** In the mitochondria, high citrate inhibits PFK-1 (slows glycolysis). In the cytoplasm, citrate activates ACC (promotes FA synthesis). Citrate exits via the citrate shuttle.

10. **The urea cycle and TCA cycle are linked** through fumarate (produced by argininosuccinate lyase in the urea cycle, enters TCA as an intermediate). This connection is called the **Krebs bicycle**.

---

*Last updated: April 12, 2026*
*Source alignment: Kaplan Biochemistry Ch 9--12, AAMC Content Outline FC1D*
