# Spectroscopy (Organic Chemistry) -- MCAT Deep Dive

This guide covers all five spectroscopic methods tested on the MCAT: IR, 1H NMR, 13C NMR, mass spectrometry, and UV-Vis. NMR (especially 1H) is the most frequently tested, but the MCAT loves to give you a passage with multiple spectra and ask you to piece together a structure. Master all five.

---

## 1. Infrared (IR) Spectroscopy

### What It Measures

IR spectroscopy measures **bond vibrations** -- specifically, the absorption of infrared light that causes bonds to stretch (symmetric and asymmetric) and bend. Different functional groups absorb at characteristic frequencies, so IR tells you **what functional groups are present** in a molecule.

The x-axis is **wavenumber** (cm^-1), which is inversely proportional to wavelength. Higher wavenumber = higher energy = stronger/stiffer bonds. The y-axis is **% transmittance** -- dips (valleys) represent absorptions.

**Key physics concept:** A bond absorbs IR radiation when the vibration causes a change in **dipole moment**. Symmetric molecules like O2 and N2 are IR-inactive. This is why CO2's symmetric stretch is IR-inactive but its asymmetric stretch and bends are IR-active.

### How to Read an IR Spectrum

Divide the spectrum into two zones:

- **Functional group region (4000--1500 cm^-1):** This is where you identify specific bonds. Almost all your diagnostic information comes from here.
- **Fingerprint region (1500--400 cm^-1):** Complex pattern unique to each molecule. You will almost never need to interpret this region on the MCAT -- it is used for exact compound matching, not functional group ID.

**Your MCAT strategy:** Scan left to right through the functional group region. Look for the "big three" in this order:

1. **Broad O-H?** (the most visually distinctive feature)
2. **Sharp C=O?** (the strongest, most recognizable single peak)
3. **N-H peaks?** (medium intensity, check for one vs. two peaks)

### Key IR Absorptions -- Must Memorize

| Bond | Wavenumber (cm^-1) | Appearance | What It Tells You |
|------|-------------------|------------|-------------------|
| **O-H (alcohol)** | 3200--3550 | Broad, rounded | Alcohol or phenol. Broadening is caused by hydrogen bonding -- the more H-bonding, the broader and more shifted the peak. |
| **O-H (carboxylic acid)** | 2500--3300 | Very broad, often overlaps C-H region | Carboxylic acid. This is the broadest O-H you will see -- it practically swallows the C-H peaks. If you see this AND a C=O near 1710, it is a carboxylic acid. |
| **N-H** | 3300--3500 | Medium, sharper than O-H | **2 peaks = primary amine** (NH2, symmetric + asymmetric stretch). **1 peak = secondary amine** (NH). Amides also show N-H here. |
| **C-H (sp3)** | 2850--3000 | Medium, always present in organic molecules | Alkane C-H. Present in almost everything -- not very diagnostic on its own. |
| **C-H (sp2)** | 3000--3100 | Slightly above 3000 | Vinyl or aromatic C-H. If you see absorption just above 3000, think unsaturation. |
| **C-H (sp, alkyne)** | ~3300 | Sharp | Terminal alkyne C-H. Can overlap with N-H region -- context matters. |
| **C=O** | 1700--1750 | **Sharp, strong, unmistakable** | Carbonyl. The single most important peak on the MCAT. Present in aldehydes, ketones, carboxylic acids, esters, amides, anhydrides. Exact position varies slightly (see below). |
| **C=C (alkene)** | 1600--1680 | Medium | Often weak or absent if symmetric. Not always diagnostic. |
| **C=C (aromatic)** | ~1450--1600 | Two peaks often visible | Aromatic ring. Not heavily tested. |
| **C-O** | 1000--1250 | Strong | Alcohols, ethers, esters. Confirms oxygen but not specific alone. |
| **C≡C** | 2100--2260 | Weak to medium | Alkyne. May be absent if internal (symmetric). |
| **C≡N** | 2200--2260 | Medium, sharp | Nitrile. Overlaps slightly with alkyne region but nitriles tend to be sharper and stronger. |

### Fine-Tuning the Carbonyl (C=O) Position

The MCAT rarely asks you to distinguish these, but knowing the trend helps:

| Carbonyl Type | Approximate cm^-1 | Why |
|---------------|-------------------|-----|
| Anhydride | 1800--1830 (two peaks) | Two C=O groups, high frequency |
| Ester | 1735--1750 | Resonance with O donates some electron density |
| Aldehyde | 1720--1740 | Also look for two C-H stretches near 2720 and 2850 |
| Ketone | 1705--1720 | "Standard" carbonyl |
| Carboxylic acid | 1700--1725 | Pair with very broad O-H |
| Amide | 1630--1690 | Nitrogen resonance lowers frequency significantly |

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

## 2. 1H NMR Spectroscopy (Proton NMR)

This is the **most tested spectroscopy topic on the MCAT**. You need to be able to read a spectrum and extract structural information. There are four pieces of information from every 1H NMR spectrum: number of signals, chemical shift, integration, and splitting.

### What It Measures

1H NMR detects the magnetic environments of **hydrogen atoms** in a molecule. When placed in a strong magnetic field, hydrogen nuclei (protons) absorb radiofrequency radiation at frequencies that depend on their electronic environment. Protons in different chemical environments appear at different positions in the spectrum.

**Reference standard:** Tetramethylsilane (TMS), (CH3)4Si, is defined as **0 ppm**. All other signals are reported relative to TMS.

### The Four Pieces of Information

#### A. Number of Signals (How many unique H environments?)

Each **chemically distinct** group of protons gives one signal. To determine equivalence, ask: "Can I swap these two hydrogens by a symmetry operation (rotation, mirror plane) and get the same molecule?"

**Examples:**
- **Ethanol (CH3CH2OH):** Three signals -- the CH3, the CH2, and the OH are all in different environments.
- **Dimethyl ether (CH3-O-CH3):** One signal -- all six H's are equivalent by symmetry.
- **Para-disubstituted benzene:** Two signals from the aromatic H's (two pairs of equivalent H's).

**MCAT trap:** Molecules with high symmetry have fewer signals than you might expect. Always check for mirror planes and rotational axes.

#### B. Chemical Shift (delta, ppm) -- Where Does the Signal Appear?

Chemical shift tells you **what is near that proton**. The key concept is **shielding vs. deshielding:**

- **Shielded protons:** Surrounded by electron density. Electrons generate a small magnetic field opposing the external field, so the nucleus "feels" less field and resonates at lower frequency. Appears **upfield** (closer to 0 ppm).
- **Deshielded protons:** Near electronegative atoms (O, N, halogens) or pi systems that withdraw electron density. The nucleus "feels" more of the external field. Appears **downfield** (higher ppm).

**Mnemonic:** Deshielded = Downfield = higher Delta (all start with D).

### Chemical Shift Reference Table -- Memorize This

| Chemical Shift (ppm) | Proton Type | Examples |
|-----------------------|-------------|----------|
| **0--1** | Alkyl, R-CH3 far from electronegative groups | Methyl on long carbon chain |
| **1--2** | Alkyl, R-CH2-R | Generic methylene |
| **2--2.5** | Adjacent to C=O (alpha protons) | CH3 next to ketone |
| **2--3** | Allylic (next to C=C) | -CH2-CH=CH2 |
| **3--4** | Adjacent to O, N, or halogen | -OCH3, -NCH2-, -CH2Cl |
| **3.5--4** | Ether, ester OCH | -OCH2- in esters |
| **4.5--6.5** | Vinyl (on C=C) | -CH=CH- |
| **6.5--8** | Aromatic | Benzene ring H's |
| **9--10** | Aldehyde | R-CHO |
| **10--12** | Carboxylic acid O-H | R-COOH |
| **1--5 (variable)** | Alcohol O-H | R-OH (variable due to H-bonding, exchange) |

**Critical conceptual points:**
- Electronegativity effect is **additive** and **distance-dependent**. CH2Cl2 is further downfield than CH3Cl. Two carbons away from Cl is less deshielded than one carbon away.
- Aromatic protons appear far downfield (6.5--8 ppm) because of **ring current** -- the circulating pi electrons create a magnetic field that deshields protons on the outside of the ring.
- Aldehyde protons are very far downfield (~9.5 ppm) because they sit directly on a carbonyl carbon AND are sp2 hybridized.

#### C. Integration (How many protons in each environment?)

The **area under each peak** is proportional to the number of protons in that environment. Modern NMR software gives you integration values. On the MCAT, you will see either:

- Numerical integration ratios (e.g., 3:2:1)
- Step-function integration curves drawn over the peaks

**Example:** If a molecule with formula C3H7Cl shows two signals with integration ratio 6:1, the signals represent 6H and 1H -- think (CH3)2CHCl (isopropyl chloride: two equivalent CH3 groups and one CH).

#### D. Splitting Pattern (n+1 Rule) -- How Many Neighbors?

This is the most conceptually rich part of NMR. When protons on adjacent carbons are non-equivalent, they cause each other's signals to split into multiple peaks.

**The n+1 rule:** A proton with **n** equivalent neighboring protons (on adjacent carbons) splits into **n+1** peaks.

| n (neighbors) | Pattern | Name |
|---------------|---------|------|
| 0 | 1 peak | Singlet (s) |
| 1 | 2 peaks | Doublet (d) |
| 2 | 3 peaks | Triplet (t) |
| 3 | 4 peaks | Quartet (q) |
| 4 | 5 peaks | Quintet |
| 5 | 6 peaks | Sextet |

**Why does splitting happen?** Each neighboring proton can be aligned with or against the external field. This creates slightly different local environments for the proton you are observing. With one neighbor, you get two possible environments (doublet). With two neighbors, three possible combinations (triplet), etc.

**The classic ethyl pattern:** -CH2CH3 gives a **quartet** (CH2, 3 neighbors) and a **triplet** (CH3, 2 neighbors) with integration ratio 2:3. You will see this pattern constantly.

**Rules for splitting:**
- Only **non-equivalent** neighbors cause splitting.
- Equivalent protons do not split each other (e.g., the 6H of (CH3)2 in isopropyl are equivalent and appear as one signal).
- O-H and N-H protons **usually do not show splitting** because rapid exchange averages out coupling. They typically appear as broad singlets.
- Splitting is a reciprocal interaction: if Ha splits Hb, then Hb also splits Ha.

### The D2O Shake

Adding D2O (deuterium oxide) to the NMR sample causes **exchangeable protons** (O-H, N-H, and sometimes S-H) to swap with deuterium. Since deuterium does not show up in 1H NMR, these peaks **disappear**.

**MCAT application:** "A peak at 2.1 ppm disappears after D2O shake" -- this peak was an O-H or N-H proton. This is a classic question format.

### 1H NMR Problem-Solving Strategy

When given an NMR spectrum on the MCAT, work through these steps:

1. **Count the signals** -- how many unique proton environments?
2. **Read the integration** -- what is the ratio of protons?
3. **Read the splitting** -- how many neighbors does each group have?
4. **Read the chemical shift** -- what functional groups are nearby?
5. **Piece it together** -- combine all four data points with the molecular formula.

**Example walkthrough:**

Molecular formula: C3H6O2. Degrees of unsaturation = (2(3) + 2 - 6) / 2 = 1.
One degree of unsaturation -- likely a C=O (not a ring, since we need to account for two oxygens suggesting ester or carboxylic acid).

NMR shows:
- Singlet at 3.7 ppm, integration 3H
- Singlet at 2.1 ppm, integration 3H

Analysis:
- 3H singlet at 3.7 ppm = OCH3 (adjacent to oxygen, no neighbors to cause splitting)
- 3H singlet at 2.1 ppm = CH3 next to C=O (no neighbors)
- Structure: **methyl acetate** (CH3COOCH3)

---

## 3. 13C NMR Spectroscopy

### What It Measures

13C NMR detects the magnetic environments of **carbon-13 atoms** in a molecule. Only ~1.1% of natural carbon is 13C, so the technique is less sensitive than 1H NMR, but it provides complementary information.

### Key Differences from 1H NMR

- **Number of peaks = number of unique carbon environments.** This is the primary information you extract.
- **No splitting in routine 13C NMR.** Standard 13C spectra are **broadband decoupled** -- a technique that collapses all C-H splitting, so every carbon appears as a singlet. Do not apply the n+1 rule.
- **Integration is NOT reliable** in 13C NMR (different carbons relax at different rates). Do not use peak heights to count carbons.
- The chemical shift range is much wider (0--220 ppm vs. 0--12 ppm for 1H).

### 13C Chemical Shift Ranges

| Chemical Shift (ppm) | Carbon Type |
|-----------------------|-------------|
| **0--50** | Alkyl carbons (sp3, no electronegative substituents) |
| **50--90** | Carbon bonded to O or N (C-O, C-N) |
| **100--150** | Aromatic and vinyl carbons (sp2 C=C) |
| **170--185** | Carboxylic acid, ester, amide C=O |
| **190--220** | Aldehyde and ketone C=O |

**MCAT application of 13C NMR:**
- Count the peaks to determine **molecular symmetry**. Benzene has one 13C signal (all six carbons equivalent). Para-xylene has three (two unique ring carbons + one unique methyl carbon type). If a molecule has fewer 13C signals than total carbons, it has symmetry.
- The presence of a peak above 170 ppm confirms a **carbonyl** group.
- A peak between 100--150 ppm indicates **aromatic or alkene** carbons.

---

## 4. Mass Spectrometry (MS)

### What It Measures

Mass spectrometry is **not** a spectroscopy (it does not involve absorption of electromagnetic radiation), but the MCAT groups it with the spectroscopies. MS measures the **mass-to-charge ratio (m/z)** of ionized molecules and their fragments. It tells you the **molecular weight** and gives clues about the **structure** from fragmentation.

### How It Works (Simplified)

1. The sample is **ionized** (commonly by electron impact, which knocks off one electron to form M+, the molecular ion / radical cation).
2. Ions are **separated** by m/z in a magnetic or electric field.
3. A detector records the **abundance** of each m/z value.

### Key Features of a Mass Spectrum

**Molecular ion peak (M+ or M+.):** The peak corresponding to the intact molecule (minus one electron). This gives you the **molecular weight**. It is not always the tallest peak and may sometimes be absent if the molecule fragments easily.

**Base peak:** The **tallest peak** in the spectrum (most abundant ion = most stable fragment). Set to 100% relative abundance. The base peak may or may not be the molecular ion.

**Fragmentation peaks:** Peaks at lower m/z values represent pieces of the molecule after bonds break. Analyzing what was lost helps identify functional groups.

### Common Fragment Losses -- Memorize This Table

| Mass Lost | Fragment Lost | Suggests |
|-----------|-------------|----------|
| **15** | CH3 | Methyl group |
| **17** | OH | Hydroxyl group |
| **18** | H2O | Alcohol (dehydration) |
| **28** | CO or CH2=CH2 | Carbonyl (aldehyde/ketone) or ethylene |
| **29** | CHO or C2H5 | Formyl group or ethyl group |
| **31** | OCH3 | Methoxy group |
| **44** | CO2 | Carboxylic acid / ester |
| **45** | OC2H5 (OEt) | Ethoxy group |

**How to use this:** If M+ = 88 and you see a strong peak at m/z = 73, the loss is 88 - 73 = 15, meaning a methyl group was lost. If you also see m/z = 59 (loss of 29), a CHO or ethyl group was also cleaved.

### Isotope Patterns

**M+1 peak:** Due to the natural abundance of **13C** (~1.1% per carbon). A molecule with 6 carbons will have an M+1 peak that is ~6.6% the height of M+. You will not be asked to calculate this precisely, but know why it exists.

**M+2 peak for halogens -- High Yield:**

| Halogen | Isotope Pattern (M : M+2) | Why |
|---------|--------------------------|-----|
| **Chlorine** | **3 : 1** | 35Cl (75%) and 37Cl (25%) -- roughly 3:1 ratio |
| **Bromine** | **1 : 1** | 79Br (50.5%) and 81Br (49.5%) -- nearly equal |

**MCAT application:** If you see two peaks of nearly equal height separated by 2 mass units, the molecule contains **bromine**. If the ratio is approximately 3:1, it contains **chlorine**. Two chlorines give a triplet pattern (M : M+2 : M+4 in roughly 9:6:1).

### The Nitrogen Rule

A molecule with an **odd molecular weight** contains an **odd number of nitrogen atoms**.

This is because nitrogen has a valence of 3 but an even atomic mass (14). Every nitrogen added to a CxHy formula changes the molecular weight by an odd increment (adds 14 for N but requires one more H for valence, net change = odd).

**Examples:**
- Aniline (C6H7N): MW = 93 (odd) -- one nitrogen
- Urea (CH4N2O): MW = 60 (even) -- two nitrogens (even number)
- Glycine (C2H5NO2): MW = 75 (odd) -- one nitrogen

---

## 5. UV-Vis Spectroscopy

### What It Measures

UV-Vis spectroscopy measures the absorption of **ultraviolet and visible light** by molecules, which causes **electronic transitions** -- electrons jump from bonding/nonbonding orbitals to antibonding orbitals (pi to pi*, n to pi*, etc.).

The x-axis is **wavelength (nm)**, and the y-axis is **absorbance**. The wavelength of maximum absorption is called **lambda_max**.

### Beer-Lambert Law -- Must Memorize

$$A = \varepsilon \cdot l \cdot c$$

| Variable | Meaning | Units |
|----------|---------|-------|
| **A** | Absorbance (unitless) | -- |
| **epsilon** | Molar absorptivity (extinction coefficient) | L / (mol * cm) |
| **l** | Path length (length of the cuvette) | cm |
| **c** | Concentration | mol/L |

**Key relationships:**
- Absorbance is **directly proportional** to concentration (this is why UV-Vis is used for quantitation).
- Absorbance is **directly proportional** to path length.
- Absorbance has **no units** (it is a log ratio: A = -log(T), where T = transmittance).
- The relationship is **linear only at low concentrations**. At high concentrations, deviations occur.

**MCAT calculation example:** If epsilon = 6000 L/(mol*cm), l = 1 cm, and c = 0.002 M, then A = 6000 x 1 x 0.002 = 12. (In practice, A > 3 is unreliable, but the math is what they test.)

### Conjugation and Lambda_max

The more **conjugated** a molecule is (more alternating single and double bonds), the **longer the wavelength** it absorbs (lower energy transition). This is called a **red shift** or **bathochromic shift**.

- **Ethylene** (one C=C): lambda_max ~170 nm (deep UV)
- **1,3-Butadiene** (two conjugated C=C): lambda_max ~217 nm
- **Beta-carotene** (11 conjugated C=C): lambda_max ~450 nm (absorbs blue light, appears orange)

**Why?** Conjugation narrows the HOMO-LUMO energy gap. A smaller gap means less energy is needed for the transition, which corresponds to longer wavelength.

### Biological Applications -- High Yield

| Application | Wavelength | What's Detected |
|-------------|-----------|-----------------|
| **Protein concentration** | **280 nm** | Absorption by aromatic amino acids: **tryptophan** (strongest), **tyrosine**, and phenylalanine (weakest) |
| **DNA/RNA concentration** | **260 nm** | Absorption by nucleotide bases (conjugated ring systems) |
| **DNA purity (260/280 ratio)** | 260 and 280 nm | Pure DNA has A260/A280 ~ 1.8. Protein contamination lowers this ratio. Pure RNA ~ 2.0. |
| **Enzyme kinetics** | Various | Track substrate disappearance or product appearance by absorbance change over time (e.g., NADH at 340 nm) |

**NADH absorbs at 340 nm; NAD+ does not.** This is used to monitor dehydrogenase reactions. As NADH is produced, absorbance at 340 nm increases.

---

## 6. Integrated Problem-Solving: Putting It All Together

The MCAT loves to give you a passage describing an unknown compound and multiple pieces of spectroscopic data. Here is the systematic approach.

### Step 1: Molecular Formula from Mass Spectrometry

- Find M+ (molecular ion peak) to get the molecular weight.
- Check for isotope patterns (Cl, Br, N).
- Apply the nitrogen rule.
- If a molecular formula is given directly, skip to Step 2.

### Step 2: Degrees of Unsaturation (Index of Hydrogen Deficiency)

For a molecule CnHmNpOqXr (X = halogen):

**DoU = (2n + 2 - m + p - r) / 2**

(Oxygen does not appear in the formula. Halogens count as hydrogens for this calculation. Nitrogen adds one to the "2n+2" count.)

| DoU | Possible Structural Feature |
|-----|----------------------------|
| 0 | Fully saturated, no rings |
| 1 | One double bond OR one ring |
| 2 | Two double bonds, two rings, one triple bond, or combinations |
| 4 | Benzene ring (3 C=C + 1 ring) |

### Step 3: IR Spectroscopy -- Identify Functional Groups

Use the IR decision tree above. At this stage you are asking: does it have O-H? C=O? N-H? These constrain the possibilities enormously.

### Step 4: NMR -- Determine Connectivity

**1H NMR:**
1. Count signals (unique H environments).
2. Read chemical shifts (what is each group near?).
3. Read integration (how many H per signal? Must account for all H's in the molecular formula).
4. Read splitting (how many neighbors?).

**13C NMR:**
1. Count peaks (unique carbon environments -- compare to total carbons from molecular formula to assess symmetry).
2. Note any signals above 170 ppm (carbonyl) or 100-150 ppm (aromatic/vinyl).

### Step 5: Propose a Structure and Verify

Assemble a structure consistent with ALL the data. Then verify:
- Does the molecular formula match?
- Does the degree of unsaturation match?
- Does every IR absorption make sense?
- Does every NMR signal have an assignment?
- Can you account for the major MS fragments?

### Worked Example

**Data given:**
- MS: M+ = 74, nitrogen rule says even MW = even number (or zero) nitrogens
- Molecular formula: C3H6O2 (DoU = 1, so one C=O or one ring)
- IR: Strong, sharp absorption at 1745 cm^-1; C-O stretch at 1200 cm^-1; no broad O-H
- 1H NMR: Singlet at 3.7 ppm (3H), singlet at 2.0 ppm (3H)
- 13C NMR: Three peaks (at 20, 52, and 171 ppm)

**Analysis:**
1. DoU = 1 --> one degree of unsaturation. With IR showing C=O at 1745, this is a carbonyl.
2. IR: C=O at 1745 (ester range), C-O present, no O-H --> not a carboxylic acid. Consistent with **ester**.
3. 1H NMR: Two singlets, each 3H. No splitting means neither group has adjacent H's. 3.7 ppm = OCH3. 2.0 ppm = CH3 next to C=O.
4. 13C NMR: 20 ppm (alkyl C), 52 ppm (C-O), 171 ppm (ester C=O). Three unique carbons in C3H6O2 = no symmetry issue.
5. **Structure: Methyl acetate (CH3COOCH3).**

Verification: MW = 74 (matches M+). Formula C3H6O2 (correct). All data consistent.

---

## Quick-Reference Summary Tables

### IR at a Glance

| Look For | Wavenumber | Means |
|----------|-----------|-------|
| Very broad hump 2500--3300 | + sharp 1710 | Carboxylic acid |
| Broad hump 3200--3550 | No C=O | Alcohol |
| Two peaks 3300--3500 | Medium | Primary amine (NH2) |
| One peak 3300--3500 | Medium | Secondary amine (NH) |
| Sharp strong 1700--1750 | Alone | Ketone, aldehyde, ester, or amide (check other regions) |
| Peak ~2100--2260 | Weak/medium | Alkyne or nitrile |

### 1H NMR at a Glance

| Shift (ppm) | Environment |
|-------------|-------------|
| 0--2 | Alkyl (far from functional groups) |
| 2--2.5 | Alpha to C=O |
| 3--4 | Adjacent to O, N, or halogen |
| 4.5--6.5 | Vinyl (on C=C) |
| 6.5--8 | Aromatic |
| 9--10 | Aldehyde C-H |
| 10--12 | Carboxylic acid O-H |

### 13C NMR at a Glance

| Shift (ppm) | Carbon Type |
|-------------|-------------|
| 0--50 | Alkyl (sp3) |
| 50--90 | C-O, C-N |
| 100--150 | Aromatic, vinyl (sp2) |
| 170--220 | Carbonyl (C=O) |

### Common MS Losses

| Loss | Fragment |
|------|----------|
| 15 | CH3 |
| 17 | OH |
| 18 | H2O |
| 28 | CO |
| 29 | CHO or C2H5 |
| 31 | OCH3 |
| 45 | OEt |

---

## High-Yield MCAT Takeaways

1. **IR:** Broad O-H and sharp C=O are the two features you will be asked about most. If you can identify those, you can answer 80% of IR questions.
2. **1H NMR:** Master the four pieces of information (number of signals, chemical shift, integration, splitting). The n+1 rule and chemical shift table are non-negotiable.
3. **D2O shake** removes O-H and N-H peaks -- a classic MCAT question.
4. **13C NMR:** Count peaks for symmetry analysis. Know that carbonyl carbons appear above 170 ppm.
5. **MS:** M+ gives molecular weight. Know the halogen isotope patterns (Cl = 3:1, Br = 1:1) and the nitrogen rule.
6. **UV-Vis:** Beer-Lambert law is a calculation target. Know that proteins absorb at 280 nm and DNA at 260 nm.
7. **Degrees of unsaturation** is the bridge between MS (molecular formula) and structural analysis. Calculate it every time you are given a formula.
8. When combining techniques, always go: **MS (formula) --> DoU --> IR (functional groups) --> NMR (connectivity) --> propose structure.**
