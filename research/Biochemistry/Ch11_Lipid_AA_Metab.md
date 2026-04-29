# BB Chapter 11 — Lipid & Amino Acid Metabolism

Scope: Lipid digestion/absorption, lipid mobilization, lipid transport, cholesterol metabolism, fatty acids & triacylglycerols (β-oxidation, FA synthesis), ketone bodies, protein catabolism.

**Section:** Bio/Biochem (BB)
**AAMC FC mapping:** FC1D (Metabolism)
**Kaplan Reference:** Biochemistry Chapter 11

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

### Lipid Digestion and Absorption

- Dietary TAGs emulsified by **bile salts** (synthesized from cholesterol in liver, stored in gallbladder)
- **Pancreatic lipase** hydrolyzes TAG → 2-monoacylglycerol + 2 free fatty acids
- Products packaged into **mixed micelles** (with bile salts) → absorbed into enterocytes
- Inside enterocytes: TAG re-synthesized and packaged into **chylomicrons**
- Chylomicrons exit via the **lymphatic system** (not portal blood — bypass the liver first pass)

### Lipid Transport (Lipoproteins)

Lipoproteins are structured particles with a nonpolar core (TAG, cholesterol esters) surrounded by a phospholipid/cholesterol monolayer with apolipoproteins embedded.

| Lipoprotein | Source | Main Cargo | Role |
|-------------|--------|-----------|------|
| **Chylomicrons** | Intestine | Dietary TAG | Transport dietary TAG to peripheral tissues (via LPL) |
| **VLDL** | Liver | Liver-made TAG | Export liver TAG to tissues |
| **IDL** | VLDL remnants | Cholesterol/TAG | Intermediate; taken up by liver or converted to LDL |
| **LDL** | IDL | Cholesterol esters | Deliver cholesterol to peripheral tissues ("bad" — atherosclerosis) |
| **HDL** | Liver/intestine | Cholesterol | **Reverse cholesterol transport** from tissues to liver ("good") |

- **Lipoprotein lipase (LPL)** on capillary endothelium hydrolyzes TAG in chylomicrons and VLDL → releases FAs to tissues. Activated by apoC-II.
- LDL is taken up via **LDL receptor-mediated endocytosis** (clathrin-coated pits); **familial hypercholesterolemia** = defective LDL receptor → blood LDL accumulates → atherosclerosis.

### Cholesterol Metabolism

- **HMG-CoA reductase** is the rate-limiting enzyme of cholesterol synthesis (converts HMG-CoA → mevalonate, in SER)
- Target of **statins** (competitive inhibitors of HMG-CoA reductase)
- Cholesterol → **bile salts** (liver; emulsify dietary fat)
- Cholesterol → **steroid hormones** (adrenal cortex, gonads)
- Cholesterol → **vitamin D** (skin UV → liver → kidney activation)

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

→ Thermodynamics, metabolic states, hormonal regulation, tissue-specific metabolism, integrative metabolism: see Ch 12
