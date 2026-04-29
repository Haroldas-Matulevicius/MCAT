# BB Chapter 10 — Carbohydrate Metabolism 2 (Aerobic Respiration)

Scope: Acetyl-CoA, citric acid cycle (TCA/Krebs), electron transport chain, oxidative phosphorylation.

**Section:** Bio/Biochem (BB)
**AAMC FC mapping:** FC1D (Metabolism)
**Kaplan Reference:** Biochemistry Chapter 10
**Yield:** Extremely high.

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

→ Glycolysis, PDC, gluconeogenesis, glycogen, PPP: see Ch 9
→ Thermodynamics, role of ATP, integrative metabolism, hormonal control, tissue-specific metabolism: see Ch 12
