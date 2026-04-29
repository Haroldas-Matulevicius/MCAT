# CP Orgo Chapter 5 — Alcohols

Scope: Alcohol description and properties; reactions of alcohols (SN1/SN2/E1/E2 substitution & elimination at sp³ carbons; oxidation of 1°/2°/3° alcohols; reduction routes back to alcohols); reactions of phenols.

**Section:** Chemical/Physical (CP)
**Book:** Kaplan Organic Chemistry — Chapter 5
**AAMC FC mapping:** FC5D (alcohol reactions)
**Yield:** HIGH — SN1/SN2/E1/E2 prediction is the canonical mechanism question on the MCAT.

---

## 1. Alcohol Properties

R-OH:
- **1° (primary):** -OH on a carbon bonded to one other C
- **2° (secondary):** -OH on a carbon bonded to two other C
- **3° (tertiary):** -OH on a carbon bonded to three other C

**Properties driven by H-bonding:**
- Higher BP than alkanes of similar MW (H-bonding network).
- Smaller alcohols water-soluble; solubility decreases as alkyl chain grows (hydrophobic).
- Acidic (pKa ~16-18). Phenols more acidic (pKa ~10) due to resonance stabilization of phenolate.

**Acidity ranking:**
- Carboxylic acid (4) > phenol (10) > water (15.7) > alcohol (16-18) > amine (36-38)
- Among alcohols: methanol (15.5) > primary > secondary > tertiary (steric and electronic — alkyl groups donate electron density, destabilizing alkoxide)
- Halogenated alcohols are more acidic (electron-withdrawing inductive effect): trichloroethanol pKa ~12.

---

## 2. SN1 / SN2 / E1 / E2 Decision Framework

This is one of the most-tested orgo topics. You MUST be able to predict the dominant mechanism given a set of conditions. (Setup framework discussed in Ch04; full mechanism details here.)

### The Four Mechanisms at a Glance

| Feature | SN2 | SN1 | E2 | E1 |
|---------|-----|-----|-----|-----|
| **Mechanism** | One step, concerted | Two steps (carbocation intermediate) | One step, concerted | Two steps (carbocation intermediate) |
| **Rate law** | Rate = k[substrate][nucleophile] | Rate = k[substrate] | Rate = k[substrate][base] | Rate = k[substrate] |
| **Stereochemistry** | Inversion (Walden inversion) | Racemization (+ some inversion) | Anti-periplanar elimination | No stereospecificity |
| **Substrate preference** | Methyl > 1° > 2° (3° = no) | 3° > 2° (1°/methyl = no) | 3° > 2° > 1° | 3° > 2° |
| **Rearrangements** | No | Yes (carbocation can rearrange) | No | Yes |

### The Decision Tree

Start with the **substrate**, then consider the nucleophile/base and solvent.

```
STEP 1: What is the substrate?
|
|-- METHYL or PRIMARY carbon
|     |
|     |-- Strong nucleophile present? --> SN2
|     |-- Strong bulky base (like tBuOK)? --> E2
|     |-- Weak nucleophile/base, heat? --> E2 (primary E1/SN1 almost never happen)
|     |
|     NOTE: SN1/E1 essentially DO NOT occur at methyl/primary carbons.
|           (Primary carbocations are too unstable.)
|
|-- SECONDARY carbon (this is the tricky one)
|     |
|     |-- Strong nucleophile (not bulky)? --> SN2 (major) with some E2
|     |-- Strong bulky base? --> E2
|     |-- Weak nucleophile/base, polar protic solvent? --> SN1 + E1 mixture
|     |-- Heat favors? --> Elimination (E2 or E1)
|     |
|     NOTE: Secondary substrates can go ANY pathway. Conditions decide.
|
|-- TERTIARY carbon
|     |
|     |-- Strong base present? --> E2 (SN2 is impossible -- too sterically hindered)
|     |-- Weak nucleophile/base, polar protic solvent? --> SN1 + E1 mixture
|     |-- Heat? --> Favors elimination (E1 or E2)
|     |
|     NOTE: SN2 NEVER happens at tertiary carbons.
```

### Key Variables Explained

**Nucleophile strength** (favors substitution):
- Strong: CN⁻, RS⁻, I⁻, HO⁻, RO⁻, NH₃, N₃⁻
- Weak: H₂O, ROH, RCOOH
- Charged > neutral counterparts.

**Base strength** (favors elimination):
- Strong bases: OH⁻, RO⁻, NaH, LDA, tBuOK
- Weak bases: H₂O, ROH
- Bulky strong bases (tBuOK, LDA) strongly favor E2 over SN2.

**Solvent:**
- **Polar protic** (water, alcohols, carboxylic acids): Stabilize carbocations through solvation. Favor SN1/E1. Also hinder SN2 by solvating the nucleophile.
- **Polar aprotic** (DMSO, DMF, acetone, acetonitrile): Do NOT solvate nucleophiles well. Favor SN2 (nucleophile is "naked" and reactive).

**Temperature:** Higher temperature favors elimination (E1, E2) over substitution. Elimination has a higher activation entropy (more molecules from fewer).

### Quick-Fire MCAT Rules

1. Methyl/1° + strong nuc + polar aprotic solvent = **SN2**
2. 3° + strong base = **E2**
3. 3° + weak nuc/base + polar protic = **SN1/E1 mix** (heat tips toward E1)
4. 2° = **look at everything** (default: strong nuc = SN2, strong base = E2, weak nuc + protic = SN1/E1)
5. Bulky base = **always E2**
6. Heat = **favors elimination**
7. SN2: **inversion**. SN1: **racemization**.
8. SN1/E1 intermediates can **rearrange** (hydride shifts, methyl shifts to form more stable carbocation)

---

## 3. Reactions of Alcohols (Substitution)

Alcohols themselves don't have great leaving groups (OH⁻ is a strong base). To make alcohols undergo SN1/SN2/E1/E2, you typically activate the OH:

### Acid Activation (protonate -OH → H₂O leaving group)

R-OH + HX (HCl, HBr, HI) → R-X + H₂O

- **3° alcohol + HX:** SN1 mechanism (carbocation forms, halide attacks). Fast.
- **1°/2° alcohol + HX:** SN2 mechanism (concerted halide attack, water leaves). Slower; works best with HI (best nucleophile).

### Sulfonate Esters (Ts, Ms)

R-OH + TsCl (or MsCl), pyridine → R-OTs (or R-OMs)

- Tosylate (-OTs) and mesylate (-OMs) are excellent leaving groups (stable as sulfonate anions).
- Subsequent SN2 displacement by any nucleophile is fast and clean.
- This is the standard way to convert an alcohol into "something usable" without going through a carbocation.

### PBr₃ and SOCl₂

- R-OH + PBr₃ → R-Br (1° and 2°; SN2-like; clean inversion).
- R-OH + SOCl₂ → R-Cl (1° and 2°; via chlorosulfite intermediate; clean inversion).

These are the workhorse reagents for converting alcohols to halides without the strong-acid conditions of HX.

---

## 4. Reactions of Alcohols (Elimination)

### Acid-Catalyzed Dehydration

R-OH + H₂SO₄ (or H₃PO₄), heat → alkene + H₂O

- **Mechanism:** E1 for 2°/3° alcohols (protonate OH, lose water → carbocation → lose β-H).
- **Mechanism:** E2 for 1° alcohols (concerted; less common).
- **Regiochemistry:** Zaitsev's rule — the **more substituted alkene is the major product** (most stable).
- **Carbocation rearrangements** can occur in E1 — watch for hydride/methyl shifts to form a more stable carbocation, leading to unexpected products.

### Other Dehydration Methods

- **POCl₃ + pyridine:** mild conditions; avoids rearrangement.

---

## 5. Oxidation of Alcohols

Tested frequently. Know the pattern:

| Alcohol type | Oxidation product | Reagent examples |
|-------------|-------------------|-----------------|
| **Primary (1°)** | **Aldehyde** (mild oxidation) | PCC (pyridinium chlorochromate) — stops at aldehyde |
| **Primary (1°)** | **Carboxylic acid** (full oxidation) | KMnO₄, CrO₃/H₂SO₄ (Jones), Na₂Cr₂O₇/H₂SO₄ |
| **Secondary (2°)** | **Ketone** | PCC, KMnO₄, CrO₃, Na₂Cr₂O₇ (all work — ketones resist further oxidation) |
| **Tertiary (3°)** | **No oxidation** | Cannot be oxidized without breaking C-C bonds |

**Why can't tertiary alcohols be oxidized?** Oxidation of an alcohol requires removing a hydrogen from the carbon bearing the -OH. Tertiary carbons have no such hydrogen.

**MCAT mnemonic:** Oxidation = loss of H or gain of O (or loss of electrons). Going from alcohol → aldehyde → carboxylic acid, you progressively lose H or gain O.

---

## 6. Reduction (Reverse of Oxidation)

(See `CP_OC_Ch06_Aldehydes_Ketones_I.md` and `CP_OC_Ch09_Carboxylic_Acid_Derivatives.md` for the detailed reduction mechanisms.)

- Carboxylic acid → aldehyde → primary alcohol (using LiAlH₄)
- Ketone → secondary alcohol (using NaBH₄ or LiAlH₄)

**NaBH₄ vs LiAlH₄:**
- **NaBH₄:** Milder. Reduces aldehydes and ketones only. Does NOT reduce esters or carboxylic acids.
- **LiAlH₄:** Stronger. Reduces aldehydes, ketones, esters, carboxylic acids, amides, epoxides. Requires anhydrous conditions (reacts violently with water).

---

## 7. Reactions of Phenols

Phenol (Ar-OH) chemistry is somewhat distinct:

- **Acidic** (pKa ~10): can be deprotonated by NaOH (but not NaHCO₃) → phenolate (resonance-stabilized into ring).
- **Activated toward electrophilic aromatic substitution (EAS)** at ortho and para positions (-OH is a strong activator/ortho-para director).
- **Oxidation:** Phenols easily oxidize to **quinones** (cyclic dienedione) by mild oxidizers — e.g., O₂, PhI(OAc)₂, K₂Cr₂O₇. Quinone/hydroquinone redox couple is biologically important (CoQ in ETC, vitamin K, vitamin E).
- **Williamson ether synthesis** with phenols: phenolate + R-X → Ar-O-R (e.g., methyl ether of phenol = anisole).

---

## High-Yield Takeaways

1. **Alcohol classification (1°/2°/3°)** determines reactivity.
2. **OH⁻ is a poor leaving group** — must be activated (protonate to H₂O, or convert to OTs/OMs/halide).
3. **SN1/SN2/E1/E2:** master the decision tree (substrate → nuc/base → solvent → temperature).
4. **PCC stops at aldehyde; KMnO₄/CrO₃ goes to carboxylic acid.** 3° doesn't oxidize.
5. **NaBH₄ (mild)** ≠ **LiAlH₄ (strong).**
6. **Zaitsev:** more substituted alkene is the major elimination product.
7. **Carbocation rearrangements** in E1/SN1 — watch for hydride/methyl shifts.
8. **Phenol pKa ~10** (resonance); oxidizes to quinone.

---

→ Mechanism framework intro: `CP_OC_Ch04_Analyzing_Reactions.md`
→ Aldehyde/ketone reactions (target of 1°/2° oxidation): `CP_OC_Ch06_Aldehydes_Ketones_I.md`
→ Carboxylic acid reactions: `CP_OC_Ch08_Carboxylic_Acids.md`
→ Acid-base / pKa: `CP_GC_Ch10_Acids_Bases.md`
