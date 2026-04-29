# CP Orgo Chapter 10 — Nitrogen and Phosphorus in Organic Molecules

Scope: Amine chemistry; amino acid structure (zwitterion, pI, peptide bond formation/hydrolysis); synthesis of α-amino acids (Strecker, Gabriel); proteins as polymers; phosphorus compounds (phosphate esters, phosphoanhydrides, ATP).

**Section:** Chemical/Physical (CP)
**Book:** Kaplan Organic Chemistry — Chapter 10
**AAMC FC mapping:** FC5D (AA chemistry); FC1A (proteins crossover)
**Yield:** HIGH — AA charge states, peptide bond properties, and ATP/phosphate chemistry are tested constantly across CP and BB.

---

## 1. Amines (Brief)

(See `CP_OC_Ch01_Nomenclature.md` for naming.)

**Amines** are derivatives of NH₃ with one or more H replaced by R groups:
- Primary (1°): R-NH₂
- Secondary (2°): R₂NH
- Tertiary (3°): R₃N
- Quaternary (4°): R₄N⁺ (positive, no lone pair, always charged)

**Properties:**
- Lone pair on N → basic (pKa of conjugate acid R-NH₃⁺ ~10).
- N is sp³ in simple amines; sp² in amides (lone pair delocalized into C=O).
- Order of basicity in gas phase: 3° > 2° > 1° > NH₃ (alkyl groups donate). In water, hydration effects flatten this — typically 2° > 1° ≈ 3° > NH₃.
- Aromatic amines (aniline, pKa ~4.6) are much less basic (lone pair conjugated into ring).

**Amine reactions:**
- React with carbonyls (Ch06) to form imines or enamines.
- React with acyl chlorides/anhydrides to form amides (Ch09).
- Act as nucleophiles in SN2 (alkylation).
- Hofmann elimination (with quaternary ammonium): forms least substituted alkene (anti-Zaitsev).

---

## 2. Amino Acid Structure

Every amino acid has the same core:

- **α-carbon** (the central carbon)
- **Amino group** (-NH₂) bonded to the α-carbon
- **Carboxyl group** (-COOH) bonded to the α-carbon
- **Hydrogen** bonded to the α-carbon
- **R group** (side chain) — what makes each amino acid unique

The α-carbon in all amino acids except glycine is a **chiral center** (4 different substituents). All biological amino acids are **L-amino acids** (S-configuration for most, except cysteine which is R due to sulfur priority).

**MCAT trap:** Glycine is the only achiral amino acid (R group = H, so two substituents are the same).

(Full table of 20 AAs with pKas → see `BB_Ch01_AminoAcids_Proteins.md`.)

---

## 3. Zwitterion Form and pI

At **physiological pH (~7.4)**, amino acids exist as **zwitterions**: the amino group is protonated (-NH₃⁺) and the carboxyl group is deprotonated (-COO⁻). The molecule has no net charge but carries both a positive and a negative charge simultaneously.

**Why?** Carboxyl pKa ~2 (gives up its proton easily); amino pKa ~9 (holds onto its proton at neutral pH). At pH 7.4, carboxyl is deprotonated, amino is protonated.

**Isoelectric point (pI)** = the pH at which the amino acid has zero net charge.

### pI Calculation Rules

- **No ionizable side chain:** pI = (pKa1 + pKa2) / 2 (average of the two backbone pKas)
- **Acidic side chain (Asp, Glu):** pI = (pKa1 + pKaR) / 2 (average of the two lowest pKas — both acidic groups)
- **Basic side chain (Lys, Arg, His):** pI = (pKa2 + pKaR) / 2 (average of the two highest pKas — both basic groups)

**The rule:** Average the two pKas that flank the zwitterion (zero net charge) form. Draw out the charge states if you're unsure.

**MCAT application:** Electrophoresis and isoelectric focusing.
- At pH < pI, AA is net positive → migrates toward cathode (negative electrode).
- At pH > pI, net negative → migrates toward anode.
- At pH = pI, net charge zero → does not migrate.

---

## 4. Peptide Bond Formation

The **peptide bond** forms via a **condensation (dehydration) reaction** between the carboxyl group of one amino acid and the amino group of another, releasing water.

```
     O                O   H
     ||               ||  |
H₂N─CH─C─OH  +  H₂N─CH─COOH   →   H₂N─CH─C─N─CH─COOH  +  H₂O
    |                |                |       |
    R₁               R₂               R₁      R₂
                                      (peptide bond between)
```

### Key Properties of the Peptide Bond

1. **Partial double bond character** — the lone pair on nitrogen delocalizes into the carbonyl (C=O), giving the C-N bond roughly 40% double bond character. This is resonance stabilization.

2. **Planarity** — because of partial double bond character, the six atoms of the peptide bond unit (Cα, C, O, N, H, Cα) all lie in the same plane. Rotation is restricted around the C-N bond.

3. **Trans configuration** — the two α-carbons (and their substituents) are on opposite sides of the peptide bond. Trans is favored because it minimizes steric clash. **Exception:** proline can adopt cis configuration more readily (its cyclic side chain reduces the energy difference).

4. **Rigidity** — phi (φ) and psi (ψ) angles (rotations around bonds to the α-carbon) can rotate freely, but omega (the peptide bond itself) is locked at ~180° (trans).

**MCAT trap:** The peptide bond is NOT a true double bond. It has partial double bond character due to resonance. Don't confuse "planar" with "completely rigid" — the backbone still has flexibility at φ/ψ angles.

---

## 5. Peptide Bond Hydrolysis

The reverse of condensation: water breaks the peptide bond, regenerating the free amino and carboxyl groups.

- **Catalyzed by proteases** in vivo (e.g., trypsin, chymotrypsin, pepsin). See BB_Ch01.
- Thermodynamically favorable but kinetically stable (high activation energy).
- **Acid hydrolysis** (6M HCl, 110°C, 24 hrs) breaks ALL peptide bonds — used in amino acid analysis.
- **Base hydrolysis** also works but can cause racemization (loss of L-configuration).

---

## 6. Synthesis of α-Amino Acids

Two classic methods to know for the MCAT:

### 6.1 Strecker Synthesis

Aldehyde + NH₃ + HCN → α-aminonitrile → (hydrolyze) → α-amino acid

```
R-CHO + NH₃ → imine (R-CH=NH)
imine + HCN → α-aminonitrile (R-CH(NH₂)(CN))
α-aminonitrile + H₃O⁺/heat → α-amino acid (R-CH(NH₂)(COOH))
```

**Mechanism:** Imine formation (Ch06) → cyanide adds as nucleophile → nitrile hydrolyzes to carboxylic acid.

**Result:** Racemic α-amino acid (no chiral control).

### 6.2 Gabriel Synthesis

Used to make primary amines and α-amino acids cleanly without overalkylation.

**Mechanism:**
1. Phthalimide is deprotonated by KOH (NH pKa ~8.3, acidic due to two flanking carbonyls — resonance-stabilized anion).
2. Phthalimide anion + alkyl halide (SN2) → N-alkyl phthalimide.
3. Hydrolysis (with NH₂NH₂ hydrazine, or strong acid/base) → primary amine.

For amino acid synthesis: use diethyl bromomalonate as the alkyl halide → after hydrolysis and decarboxylation, you get an α-amino acid.

**Advantage over direct alkylation of NH₃:** Avoids polyalkylation (would form 2°, 3°, 4° amines).

---

## 7. Phosphorus Compounds

Phosphorus chemistry is critical for biology — DNA backbone, ATP, phospholipids, signaling.

### 7.1 Phosphate Group Structure

Phosphate (PO₄³⁻) is tetrahedral. P is sp³ with one P=O double bond and three P-O single bonds (some textbooks draw resonance structures distributing the double bond over all four O's — the four O's are equivalent in phosphate).

In neutral form: H₃PO₄ (phosphoric acid). pKa values: 2.1, 7.2, 12.4 (triprotic).
At physiological pH (7.4), phosphate is mostly H₂PO₄⁻ ↔ HPO₄²⁻ (1:1 ratio at pH = 7.2).

### 7.2 Phosphate Esters

R-O-PO(OH)₂ — a phosphate group bonded to an alcohol.

Examples:
- Glucose-6-phosphate (sugar phosphate)
- Glycerol-3-phosphate (glycerolipid intermediate)
- Phosphorylated amino acid side chains (regulation)

**Why are phosphate esters important biologically?**
1. **Negative charge** at physiological pH → traps molecules in cells (can't cross membranes easily).
2. **Hydrolysis is slightly exergonic** but kinetically slow → stable storage.
3. **Phosphorylation regulation** by kinases (add) and phosphatases (remove).

### 7.3 Phosphoanhydrides (ATP)

ATP = adenosine 5'-triphosphate. Structure:
- Adenine (base)
- Ribose (sugar)
- Three phosphate groups (α, β, γ from inside out)

The bonds between phosphate groups (β-γ and α-β) are **phosphoanhydride bonds** — analogous to anhydrides in carboxylic acid chemistry.

**ATP hydrolysis:**
- ATP + H₂O → ADP + P_i (γ-phosphate cleaved): ΔG° ≈ -30.5 kJ/mol
- ATP + H₂O → AMP + PP_i (α-β cleaved): ΔG° ≈ -45 kJ/mol (PP_i further hydrolyzed)

**Why exergonic?**
1. Charge repulsion relief (3 negative phosphates crowded).
2. Resonance stabilization of products (more delocalization in ADP + Pi than in ATP).
3. Better hydration of products.
4. Entropy increase (1 → 2 molecules).

(See `CP_GC_Ch07_Thermochemistry.md` for full bioenergetics treatment.)

### 7.4 DNA/RNA Phosphate Linkages

**Phosphodiester bond:** Phosphate connects 3'-OH of one sugar to 5'-OH of the next sugar. Two ester linkages (one to each sugar) on the same phosphate.

The backbone is **negatively charged** at physiological pH (each phosphate carries a negative charge), which:
- Makes DNA migrate toward the anode in gel electrophoresis (used to separate by size).
- Stabilizes interactions with positively charged histones (compaction).
- Is repelled by other phosphate-containing molecules (e.g., wouldn't pass through a hydrophobic membrane).

### 7.5 Phospholipids

Glycerol + 2 fatty acids + 1 phosphate + headgroup (choline, ethanolamine, serine, inositol).

The **phosphodiester linkage** to glycerol and the headgroup makes phospholipids amphipathic — driving membrane bilayer formation. (Detailed in BB_Ch05.)

---

## High-Yield Takeaways

1. **AA structure:** α-carbon bears -NH₂, -COOH, H, and R group. Glycine is achiral (R = H).
2. **All biological AAs are L-configuration.**
3. **Zwitterion** at physiological pH (-NH₃⁺ + -COO⁻).
4. **pI = average of two pKas flanking the zwitterion form.**
5. **Peptide bond:** ~40% double bond character → planar, trans, rigid (φ/ψ free, ω locked).
6. **Strecker synthesis:** RCHO + NH₃ + HCN → α-aminonitrile → α-amino acid.
7. **Gabriel synthesis:** clean primary amine via phthalimide.
8. **Phosphate at physiological pH** = H₂PO₄⁻/HPO₄²⁻ (1:1 at pH 7.2).
9. **ATP hydrolysis ΔG ≈ -30.5 kJ/mol;** drives biological reactions.
10. **DNA phosphodiester backbone** is negatively charged at physiological pH.

---

→ Amine basicity & amine chemistry (more): `CP_OC_Ch01_Nomenclature.md`, `CP_OC_Ch09_Carboxylic_Acid_Derivatives.md` (amides)
→ AA properties, full pKa table, protein structure: `BB_Ch01_AminoAcids_Proteins.md`
→ ATP & bioenergetics: `CP_GC_Ch07_Thermochemistry.md`
→ DNA structure: `BB_Ch06_DNA_Biotech.md`
→ Phospholipids & membranes: `BB_Ch05_Lipids.md`, `BB_Ch08_Membranes.md`
