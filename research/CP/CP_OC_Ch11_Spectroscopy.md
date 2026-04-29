# CP Orgo Chapter 11 — Spectroscopy

Scope: IR spectroscopy (functional group ID); ¹H NMR (chemical shift, integration, splitting, n+1 rule, D₂O shake); ¹³C NMR (counting unique carbons); mass spectrometry (M+, fragmentation, isotope patterns, nitrogen rule); UV-Vis (Beer-Lambert, conjugation, biological applications); integrated problem-solving.

**Section:** Chemical/Physical (CP)
**Book:** Kaplan Organic Chemistry — Chapter 11
**AAMC FC mapping:** FC5C (analytical methods) and FC5D (structure determination)
**Yield:** HIGH — passages frequently give a molecular formula plus 2-3 spectra and ask you to deduce structure.

---

## 1. Infrared (IR) Spectroscopy

### What It Measures

IR spectroscopy measures **bond vibrations** -- specifically, the absorption of infrared light that causes bonds to stretch (symmetric and asymmetric) and bend. Different functional groups absorb at characteristic frequencies, so IR tells you **what functional groups are present** in a molecule.

The x-axis is **wavenumber** (cm⁻¹), which is inversely proportional to wavelength. Higher wavenumber = higher energy = stronger/stiffer bonds. The y-axis is **% transmittance** -- dips (valleys) represent absorptions.

**Key physics concept:** A bond absorbs IR radiation when the vibration causes a change in **dipole moment**. Symmetric molecules like O₂ and N₂ are IR-inactive. This is why CO₂'s symmetric stretch is IR-inactive but its asymmetric stretch and bends are IR-active.

### How to Read an IR Spectrum

Divide the spectrum into two zones:

- **Functional group region (4000-1500 cm⁻¹):** This is where you identify specific bonds. Almost all your diagnostic information comes from here.
- **Fingerprint region (1500-400 cm⁻¹):** Complex pattern unique to each molecule. You will almost never need to interpret this region on the MCAT — it is used for exact compound matching, not functional group ID.

**Your MCAT strategy:** Scan left to right through the functional group region. Look for the "big three" in this order:

1. **Broad O-H?** (the most visually distinctive feature)
2. **Sharp C=O?** (the strongest, most recognizable single peak)
3. **N-H peaks?** (medium intensity, check for one vs. two peaks)

### Key IR Absorptions -- Must Memorize

| Bond | Wavenumber (cm⁻¹) | Appearance | What It Tells You |
|------|-------------------|------------|-------------------|
| **O-H (alcohol)** | 3200-3550 | Broad, rounded | Alcohol or phenol. Broadening from H-bonding. |
| **O-H (carboxylic acid)** | 2500-3300 | Very broad, often overlaps C-H region | Carboxylic acid. The broadest O-H you will see — practically swallows the C-H peaks. If you see this AND a C=O near 1710, it is a carboxylic acid. |
| **N-H** | 3300-3500 | Medium, sharper than O-H | **2 peaks = primary amine** (NH₂, symmetric + asymmetric stretch). **1 peak = secondary amine** (NH). Amides also show N-H here. |
| **C-H (sp³)** | 2850-3000 | Medium, always present in organic molecules | Alkane C-H. Present in almost everything — not very diagnostic on its own. |
| **C-H (sp²)** | 3000-3100 | Slightly above 3000 | Vinyl or aromatic C-H. If you see absorption just above 3000, think unsaturation. |
| **C-H (sp, alkyne)** | ~3300 | Sharp | Terminal alkyne C-H. Can overlap with N-H region — context matters. |
| **C=O** | 1700-1750 | **Sharp, strong, unmistakable** | Carbonyl. The single most important peak on the MCAT. Present in aldehydes, ketones, carboxylic acids, esters, amides, anhydrides. Exact position varies slightly. |
| **C=C (alkene)** | 1600-1680 | Medium | Often weak or absent if symmetric. Not always diagnostic. |
| **C=C (aromatic)** | ~1450-1600 | Two peaks often visible | Aromatic ring. Not heavily tested. |
| **C-O** | 1000-1250 | Strong | Alcohols, ethers, esters. Confirms oxygen but not specific alone. |
| **C≡C** | 2100-2260 | Weak to medium | Alkyne. May be absent if internal (symmetric). |
| **C≡N** | 2200-2260 | Medium, sharp | Nitrile. Overlaps slightly with alkyne region but nitriles tend to be sharper and stronger. |

### Fine-Tuning the Carbonyl (C=O) Position

The MCAT rarely asks you to distinguish these, but knowing the trend helps:

| Carbonyl Type | Approximate cm⁻¹ | Why |
|---------------|-------------------|-----|
| Anhydride | 1800-1830 (two peaks) | Two C=O groups, high frequency |
| Ester | 1735-1750 | Resonance with O donates some electron density |
| Aldehyde | 1720-1740 | Also look for two C-H stretches near 2720 and 2850 |
| Ketone | 1705-1720 | "Standard" carbonyl |
| Carboxylic acid | 1700-1725 | Pair with very broad O-H |
| Amide | 1630-1690 | Nitrogen resonance lowers frequency significantly |

**The trend:** More electron donation into the C=O (resonance) lowers the stretching frequency. Amides have the most resonance donation (nitrogen's lone pair), so they absorb at the lowest frequency.

### IR Decision Tree for the MCAT

```
Is there a broad absorption in the 2500-3550 range?
  |
  YES --> Is it VERY broad (2500-3300), swallowing C-H peaks?
  |         YES --> Carboxylic acid (confirm with C=O ~1710)
  |         NO  --> Alcohol (broad but centered ~3300-3400)
  |
  NO --> Is there a sharp, strong peak at 1700-1750?
           YES --> Carbonyl compound. Check for:
           |       - Aldehyde C-H at ~2720 --> aldehyde
           |       - C-O at 1000-1250 --> ester
           |       - N-H at 3300-3500 --> amide
           |       - None of above --> ketone
           NO --> Check for N-H, C≡N, C≡C, or C-O to narrow down
```

---

## 2. ¹H NMR Spectroscopy (Proton NMR)

This is the **most tested spectroscopy topic on the MCAT**. You need to be able to read a spectrum and extract structural information. There are four pieces of information from every ¹H NMR spectrum: number of signals, chemical shift, integration, and splitting.

### What It Measures

¹H NMR detects the magnetic environments of **hydrogen atoms** in a molecule. When placed in a strong magnetic field, hydrogen nuclei (protons) absorb radiofrequency radiation at frequencies that depend on their electronic environment. Protons in different chemical environments appear at different positions in the spectrum.

**Reference standard:** Tetramethylsilane (TMS), (CH₃)₄Si, is defined as **0 ppm**. All other signals are reported relative to TMS.

### The Four Pieces of Information

#### A. Number of Signals (How many unique H environments?)

Each **chemically distinct** group of protons gives one signal. To determine equivalence, ask: "Can I swap these two hydrogens by a symmetry operation (rotation, mirror plane) and get the same molecule?"

**Examples:**
- **Ethanol (CH₃CH₂OH):** Three signals — CH₃, CH₂, OH all different.
- **Dimethyl ether (CH₃-O-CH₃):** One signal — all six H's equivalent by symmetry.
- **Para-disubstituted benzene:** Two signals from aromatic H's.

**MCAT trap:** Molecules with high symmetry have fewer signals than expected. Always check for mirror planes and rotational axes.

#### B. Chemical Shift (δ, ppm) — Where Does the Signal Appear?

Chemical shift tells you **what is near that proton**. The key concept is **shielding vs. deshielding:**

- **Shielded protons:** Surrounded by electron density. Electrons generate a small magnetic field opposing the external field, so the nucleus "feels" less field and resonates at lower frequency. Appears **upfield** (closer to 0 ppm).
- **Deshielded protons:** Near electronegative atoms (O, N, halogens) or pi systems that withdraw electron density. Appears **downfield** (higher ppm).

**Mnemonic:** Deshielded = Downfield = higher Delta (all start with D).

### Chemical Shift Reference Table — Memorize This

| Chemical Shift (ppm) | Proton Type | Examples |
|-----------------------|-------------|----------|
| **0-1** | Alkyl, R-CH₃ far from EN groups | Methyl on long carbon chain |
| **1-2** | Alkyl, R-CH₂-R | Generic methylene |
| **2-2.5** | Adjacent to C=O (α protons) | CH₃ next to ketone |
| **2-3** | Allylic (next to C=C) | -CH₂-CH=CH₂ |
| **3-4** | Adjacent to O, N, or halogen | -OCH₃, -NCH₂-, -CH₂Cl |
| **3.5-4** | Ether, ester OCH | -OCH₂- in esters |
| **4.5-6.5** | Vinyl (on C=C) | -CH=CH- |
| **6.5-8** | Aromatic | Benzene ring H's |
| **9-10** | Aldehyde | R-CHO |
| **10-12** | Carboxylic acid O-H | R-COOH |
| **1-5 (variable)** | Alcohol O-H | R-OH (variable due to H-bonding, exchange) |

**Critical conceptual points:**
- Electronegativity effect is **additive** and **distance-dependent**. CH₂Cl₂ is further downfield than CH₃Cl.
- Aromatic protons appear far downfield (6.5-8 ppm) because of **ring current** (circulating π electrons deshield ring protons).
- Aldehyde protons very far downfield (~9.5 ppm) — sit on carbonyl C AND sp² hybridized.

#### C. Integration (How many protons in each environment?)

The **area under each peak** is proportional to the number of protons in that environment.

**Example:** C₃H₇Cl shows two signals with ratio 6:1 → 6H and 1H → (CH₃)₂CHCl (isopropyl chloride: two equivalent CH₃ + one CH).

#### D. Splitting Pattern (n+1 Rule) — How Many Neighbors?

When protons on adjacent carbons are non-equivalent, they cause each other's signals to split into multiple peaks.

**The n+1 rule:** A proton with **n** equivalent neighboring protons (on adjacent carbons) splits into **n+1** peaks.

| n (neighbors) | Pattern | Name |
|---------------|---------|------|
| 0 | 1 peak | Singlet (s) |
| 1 | 2 peaks | Doublet (d) |
| 2 | 3 peaks | Triplet (t) |
| 3 | 4 peaks | Quartet (q) |
| 4 | 5 peaks | Quintet |
| 5 | 6 peaks | Sextet |

**The classic ethyl pattern:** -CH₂CH₃ gives a **quartet** (CH₂, 3 neighbors) and a **triplet** (CH₃, 2 neighbors) with integration ratio 2:3.

**Rules for splitting:**
- Only **non-equivalent** neighbors cause splitting.
- Equivalent protons do not split each other.
- O-H and N-H protons **usually do not show splitting** (rapid exchange averages out coupling). Typically broad singlets.
- Splitting is reciprocal: if Hₐ splits H_b, then H_b also splits Hₐ.

### The D₂O Shake

Adding D₂O causes **exchangeable protons** (O-H, N-H) to swap with deuterium. Since deuterium does not show up in ¹H NMR, these peaks **disappear**.

**MCAT application:** "A peak at 2.1 ppm disappears after D₂O shake" → was an O-H or N-H proton.

### ¹H NMR Problem-Solving Strategy

1. **Count signals** — how many unique proton environments?
2. **Read integration** — what is the ratio of protons?
3. **Read splitting** — how many neighbors does each group have?
4. **Read chemical shift** — what functional groups are nearby?
5. **Piece it together** — combine all four data points with the molecular formula.

**Example:** C₃H₆O₂. DoU = 1. NMR: singlet 3.7 ppm (3H), singlet 2.1 ppm (3H).
- 3H singlet at 3.7 ppm = OCH₃ (adjacent to O, no neighbors)
- 3H singlet at 2.1 ppm = CH₃ next to C=O
- Structure: **methyl acetate** (CH₃COOCH₃).

---

## 3. ¹³C NMR Spectroscopy

### What It Measures

¹³C NMR detects ¹³C atoms (~1.1% natural abundance, less sensitive than ¹H). Provides complementary structural info.

### Key Differences from ¹H NMR

- **Number of peaks = number of unique carbon environments** (the primary information).
- **No splitting** in routine ¹³C NMR (broadband decoupled — collapses C-H splitting). Don't apply n+1 rule.
- **Integration is NOT reliable** in ¹³C NMR (different relaxation rates).
- Chemical shift range is much wider (0-220 ppm vs 0-12 ppm for ¹H).

### ¹³C Chemical Shift Ranges

| Chemical Shift (ppm) | Carbon Type |
|-----------------------|-------------|
| **0-50** | Alkyl carbons (sp³, no electronegative substituents) |
| **50-90** | C bonded to O or N (C-O, C-N) |
| **100-150** | Aromatic and vinyl (sp² C=C) |
| **170-185** | Carboxylic acid, ester, amide C=O |
| **190-220** | Aldehyde and ketone C=O |

**MCAT application:**
- Count peaks vs total carbons → assess **molecular symmetry**. Benzene: 1 ¹³C signal (all 6 equivalent). Para-xylene: 3 signals.
- Peak >170 ppm confirms **carbonyl**.
- Peak 100-150 ppm = **aromatic or alkene**.

---

## 4. Mass Spectrometry (MS)

### What It Measures

MS measures the **mass-to-charge ratio (m/z)** of ionized molecules and their fragments. Tells you molecular weight + structure clues from fragmentation. (Not actually a spectroscopy — no EM absorption — but grouped here.)

### How It Works (Simplified)

1. Sample is **ionized** (commonly by electron impact: knocks off one electron → M+ molecular ion).
2. Ions are **separated** by m/z in a magnetic/electric field.
3. Detector records **abundance** vs m/z.

### Key Features

**Molecular ion peak (M+ or M+•):** Corresponds to intact molecule (minus one electron). Gives **molecular weight**. Not always tallest peak; may be absent if molecule fragments easily.

**Base peak:** **Tallest peak** (most abundant ion = most stable fragment). Set to 100% relative abundance. May or may not be the molecular ion.

**Fragmentation peaks:** Lower m/z values represent pieces of the molecule. Analyzing what was lost helps identify functional groups.

### Common Fragment Losses — Memorize

| Mass Lost | Fragment Lost | Suggests |
|-----------|-------------|----------|
| **15** | CH₃ | Methyl group |
| **17** | OH | Hydroxyl group |
| **18** | H₂O | Alcohol (dehydration) |
| **28** | CO or CH₂=CH₂ | Carbonyl or ethylene |
| **29** | CHO or C₂H₅ | Formyl or ethyl |
| **31** | OCH₃ | Methoxy |
| **44** | CO₂ | Carboxylic acid / ester |
| **45** | OC₂H₅ (OEt) | Ethoxy |

If M+ = 88 and you see a strong peak at 73, the loss is 15 (methyl group). If you also see m/z = 59, that's another loss of 14 from 73 (CH₂) or m/z = 88 - 29 = 59 (loss of 29 from M+, so CHO or ethyl).

### Isotope Patterns

**M+1 peak:** Due to natural ¹³C abundance (~1.1% per carbon). A 6-carbon molecule has M+1 ~6.6% of M+. Won't calculate precisely; know it exists.

**M+2 peak for halogens — High Yield:**

| Halogen | Isotope Pattern (M : M+2) | Why |
|---------|--------------------------|-----|
| **Chlorine** | **3 : 1** | ³⁵Cl (75%) and ³⁷Cl (25%) |
| **Bromine** | **1 : 1** | ⁷⁹Br (50.5%) and ⁸¹Br (49.5%) |

**MCAT application:** Two peaks of nearly equal height separated by 2 mass units = **bromine**. 3:1 ratio = **chlorine**. Two chlorines give a triplet pattern (M : M+2 : M+4 ≈ 9:6:1).

### The Nitrogen Rule

A molecule with an **odd molecular weight** contains an **odd number of nitrogen atoms**.

(N has valence 3 but even atomic mass 14. Each N requires one more H for valence, net odd change in MW.)

**Examples:**
- Aniline (C₆H₇N): MW = 93 (odd) → one N.
- Urea (CH₄N₂O): MW = 60 (even) → two N's.
- Glycine (C₂H₅NO₂): MW = 75 (odd) → one N.

---

## 5. UV-Vis Spectroscopy

### What It Measures

UV-Vis measures absorption of UV/visible light, causing **electronic transitions** (electrons jump from bonding/nonbonding orbitals to antibonding orbitals: π→π*, n→π*, etc.).

x-axis = **wavelength (nm)**; y-axis = **absorbance**. Wavelength of max absorption = **λ_max**.

### Beer-Lambert Law — Must Memorize

A = ε · l · c

| Variable | Meaning | Units |
|----------|---------|-------|
| **A** | Absorbance | unitless |
| **ε** | Molar absorptivity (extinction coefficient) | L / (mol·cm) |
| **l** | Path length (cuvette length) | cm |
| **c** | Concentration | mol/L |

**Key relationships:**
- A is **directly proportional** to concentration (this is why UV-Vis is used for quantitation).
- A is **directly proportional** to path length.
- A = -log(T) where T is transmittance — log ratio, no units.
- Linear only at low concentrations; deviations at high.

**Example:** ε = 6000 L/(mol·cm), l = 1 cm, c = 0.002 M → A = 6000 × 1 × 0.002 = 12. (In practice, A > 3 is unreliable.)

### Conjugation and λ_max

The more **conjugated** a molecule, the **longer the wavelength** it absorbs (lower energy). This is a **red shift** or **bathochromic shift**.

- **Ethylene** (1 C=C): λ_max ~170 nm (deep UV)
- **1,3-Butadiene** (2 conjugated C=C): λ_max ~217 nm
- **β-carotene** (11 conjugated C=C): λ_max ~450 nm (absorbs blue, appears orange)

**Why?** Conjugation narrows the HOMO-LUMO energy gap. Smaller gap → less energy needed → longer wavelength.

### Biological Applications — High Yield

| Application | Wavelength | What's Detected |
|-------------|-----------|-----------------|
| **Protein concentration** | **280 nm** | Aromatic AAs: **tryptophan** (strongest), **tyrosine**, phenylalanine (weakest) |
| **DNA/RNA concentration** | **260 nm** | Nucleotide bases (conjugated rings) |
| **DNA purity (260/280 ratio)** | 260 and 280 nm | Pure DNA: ~1.8. Protein contamination lowers ratio. Pure RNA: ~2.0. |
| **Enzyme kinetics** | Various | Track substrate/product (e.g., NADH at 340 nm) |

**NADH absorbs at 340 nm; NAD+ does not.** Used to monitor dehydrogenase reactions — track NADH formation by ↑ A₃₄₀.

---

## 6. Integrated Problem-Solving

The MCAT loves passages with multiple spectra. Systematic approach:

### Step 1: Molecular Formula from MS
- Find M+ → MW.
- Check halogen isotope patterns.
- Apply nitrogen rule.

### Step 2: Degrees of Unsaturation (DoU)

For CnHmNpOqXr (X = halogen):

**DoU = (2n + 2 - m + p - r) / 2**

(O doesn't appear; halogens count as H; N adds +1.)

| DoU | Possible Structural Feature |
|-----|----------------------------|
| 0 | Fully saturated, no rings |
| 1 | One double bond OR one ring |
| 2 | Two double bonds, two rings, one triple bond |
| 4 | Benzene ring (3 C=C + 1 ring) |

### Step 3: IR — Functional Groups
Apply IR decision tree. Constrains possibilities.

### Step 4: NMR — Connectivity

**¹H NMR:** Count signals, chemical shifts, integration, splitting.
**¹³C NMR:** Count peaks (symmetry); ID >170 ppm (carbonyl) and 100-150 ppm (aromatic/vinyl).

### Step 5: Propose Structure and Verify

Verify:
- MF matches?
- DoU matches?
- Every IR absorption assigned?
- Every NMR signal assigned?
- Major MS fragments accounted for?

### Worked Example

**Data:** MS M+ = 74; molecular formula C₃H₆O₂; DoU = 1; IR strong sharp 1745 cm⁻¹, C-O at 1200 cm⁻¹, no broad O-H; ¹H NMR: singlet 3.7 ppm (3H), singlet 2.0 ppm (3H); ¹³C NMR: 3 peaks (20, 52, 171 ppm).

**Analysis:**
1. DoU = 1 → one C=O (IR confirms 1745).
2. IR 1745 = ester range; C-O present; no O-H → **ester**.
3. ¹H: Two 3H singlets, no splitting → no adjacent H's. 3.7 ppm = OCH₃; 2.0 ppm = CH₃ next to C=O.
4. ¹³C: 20 (alkyl), 52 (C-O), 171 (ester C=O). Three unique C's.
5. **Structure: Methyl acetate (CH₃COOCH₃).**

---

## High-Yield Takeaways

1. **IR — broad O-H + C=O = carboxylic acid;** broad O-H alone = alcohol; sharp C=O ~1700-1750 = carbonyl.
2. **¹H NMR four pieces:** # signals, chemical shift, integration, splitting (n+1 rule).
3. **D₂O shake** removes exchangeable O-H/N-H peaks.
4. **¹³C NMR:** count peaks for symmetry; >170 ppm = carbonyl.
5. **MS:** M+ gives MW; halogen patterns (Cl 3:1, Br 1:1); nitrogen rule (odd MW = odd # N).
6. **Beer-Lambert:** A = εlc; protein 280 nm (Trp), DNA 260 nm.
7. **Conjugation → red shift in UV-Vis** (longer λ_max).
8. **Workflow:** MS (formula) → DoU → IR (FGs) → NMR (connectivity) → propose structure.

---

→ Conjugation theory (HOMO-LUMO): `CP_OC_Ch03_Bonding.md`
→ Functional groups for IR matching: `CP_OC_Ch01_Nomenclature.md`
→ DNA/RNA absorbance: `BB_Ch06_DNA_Biotech.md`
→ Enzyme kinetics by absorbance: `BB_Ch02_Enzymes.md`
