# BB Chapter 12 — Bioenergetics & Regulation of Metabolism

Scope: Thermodynamics/bioenergetics, role of ATP, biological oxidation/reduction, metabolic states (fed/fasting/starvation), hormonal regulation, tissue-specific metabolism, integrative metabolism.

**Section:** Bio/Biochem (BB)
**AAMC FC mapping:** FC1D (Metabolism)
**Kaplan Reference:** Biochemistry Chapter 12

---

## Thermodynamics / Bioenergetics

- **ΔG = ΔH − TΔS** (Gibbs free energy)
- ΔG < 0 → spontaneous (exergonic); ΔG > 0 → non-spontaneous (endergonic); ΔG = 0 → equilibrium
- **ΔG°'** = standard free energy at biological conditions (pH 7.0, 25°C, 1 M, 1 atm)
- Actual ΔG depends on concentrations: ΔG = ΔG°' + RT ln([products]/[reactants])
- Cells couple endergonic reactions to exergonic ones through **shared intermediates** (most commonly ATP)

## Role of ATP

- High-energy phosphoanhydride bonds; ΔG° hydrolysis of ATP → ADP + Pi ≈ **-7.3 kcal/mol** (standard); actual cellular ΔG is more negative (~-12 kcal/mol) due to concentration effects
- **ATP / ADP / AMP ratio** serves as an energy signal across metabolism
- **Substrate-level phosphorylation** — direct P transfer from phosphorylated substrate to ADP (glycolysis, TCA); anaerobic, small yield
- **Oxidative phosphorylation** — ATP synthase driven by proton gradient (see Ch 10); aerobic, large yield

## Biological Oxidation / Reduction

- **NAD+/NADH** — catabolic electron carrier; delivers electrons to Complex I of ETC
- **FAD/FADH2** — catabolic; delivers to Complex II (lower yield)
- **NADP+/NADPH** — anabolic/biosynthetic reducing power; used in FA synthesis, cholesterol synthesis, glutathione reduction, respiratory burst (phagocytes)
- The difference: NADH goes to ATP production; NADPH supplies electrons for biosynthesis and redox defense. Same nucleotide, different phosphate → different enzyme targeting.

---

## Metabolic Integration — The Three Metabolic States

This is the most MCAT-relevant section. The exam rarely tests isolated pathways -- instead, it presents a physiological scenario and asks you to predict which pathways are active, which hormones are dominant, and what happens in specific tissues.

### Fed State (Absorptive, ~0--4 hours after a meal)

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

### Fasting State (~4--24 hours without eating)

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

### Starvation (>24 hours, extending to days/weeks)

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

---

## Tissue-Specific Metabolism

This is where integration questions come from. Each tissue has a unique metabolic profile:

### Liver (The Metabolic Hub)

- Has ALL major metabolic pathways
- Maintains blood glucose: gluconeogenesis, glycogenolysis, glucose-6-phosphatase
- Detoxifies ammonia via the urea cycle
- Makes ketone bodies but CANNOT use them (lacks thiophorase)
- Makes VLDL to export TAG to other tissues
- First-pass metabolism of drugs, alcohol, toxins
- Makes bile salts from cholesterol
- Responds to both insulin and glucagon

### Skeletal Muscle

- Major glucose consumer during exercise (GLUT4, insulin-dependent)
- Stores glycogen for LOCAL use only (lacks glucose-6-phosphatase, cannot export glucose)
- Uses fatty acids at rest, glucose + glycogen during exercise
- Cannot perform gluconeogenesis
- Exports lactate (Cori cycle) and alanine (glucose-alanine cycle) to liver
- In starvation: protein is broken down for amino acids (gluconeogenic substrates)

### Brain

- **Obligate glucose user** under normal conditions (~120 g/day)
- Cannot use fatty acids (FAs cannot cross the blood-brain barrier efficiently, and brain lacks significant beta-oxidation capacity)
- CAN adapt to use ketone bodies during starvation (after 3--5 days)
- Highly sensitive to hypoglycemia -- confusion, seizures, coma, death
- Uses GLUT1 and GLUT3 (insulin-independent -- brain always gets glucose)

### Adipose Tissue

- Stores TAG (triglycerides) in the fed state via lipoprotein lipase (LPL) on capillary endothelium
- Releases fatty acids + glycerol during fasting via **hormone-sensitive lipase (HSL)**, activated by glucagon/epinephrine (PKA phosphorylates HSL)
- Insulin inhibits HSL (anti-lipolytic)
- Glycerol goes to liver for gluconeogenesis (adipose lacks glycerol kinase to reuse it)
- Brown adipose: contains thermogenin (UCP1), generates heat

### Red Blood Cells

- **No mitochondria** -- rely entirely on glycolysis for ATP
- Produce lactate as the end product (Cori cycle substrate)
- Active PPP for NADPH (ROS defense via glutathione)
- Cannot use fatty acids, ketone bodies, or amino acids for energy

### Heart

- Aerobic powerhouse with abundant mitochondria
- **Preferred fuels (in order):** fatty acids > ketone bodies > lactate > glucose
- CAN use lactate as fuel (has LDH that runs in reverse: lactate --> pyruvate)
- During exercise, the heart actually benefits from elevated blood lactate

---

## Predicting Active Pathways from a Scenario

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

## Hormonal Summary Table

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

The range (30 vs 32) depends on the NADH shuttle used for the 2 glycolytic NADH (malate-aspartate: 32; glycerol-3-phosphate: 30).

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

→ Individual pathways: see Ch 9 (glycolysis/PPP/glycogen/gluconeogenesis), Ch 10 (TCA/ETC/OxPhos), Ch 11 (lipid/AA metabolism)
