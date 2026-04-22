# BB Chapter 1 — Amino Acids, Peptides, Proteins

Scope: The 20 amino acids, acid-base behavior, peptide bond formation/hydrolysis, 1°/2°/3°/4° structure, denaturation, chaperones.

**Section:** Bio/Biochem (BB)
**AAMC FC mapping:** FC1A (Protein Structure and Function)
**Kaplan Reference:** Biochemistry Chapter 1
**Yield:** Extremely high. Amino acids and protein folding appear on virtually every MCAT.

---

## 1. Amino Acids

This is the single highest-yield topic in the entire BB section. You need every amino acid's structure internalized -- not just memorized, but understood well enough that you can predict behavior in novel scenarios. The MCAT will not ask you to draw tryptophan from memory. It will show you a peptide sequence and ask you to predict its behavior at a given pH, or which residues would face inward in an aqueous environment, or why a single mutation disrupts function. That requires understanding, not flashcards alone.

### 1.1 General Amino Acid Structure

Every amino acid shares the same backbone: a central **alpha-carbon** bonded to (1) an amino group (-NH3+ at physiological pH), (2) a carboxyl group (-COO- at physiological pH), (3) a hydrogen, and (4) an R-group (side chain) that determines the amino acid's identity.

At physiological pH (~7.4), the amino group is protonated (positive) and the carboxyl group is deprotonated (negative). This simultaneously charged species is called a **zwitterion** -- it carries both a positive and a negative charge, giving it a net charge of zero (for amino acids with uncharged side chains). This is critical: at its pI, an amino acid is a zwitterion, not an uncharged molecule. It still has charges, they just cancel out.

### 1.2 Stereochemistry: L vs D

The alpha-carbon of every amino acid except glycine is a **chiral center** (four different groups). Biological proteins use exclusively **L-amino acids**. The naming convention comes from the **Fischer projection**:

```
        COO⁻          (carboxyl group on TOP)
         |
  H₃N⁺—Cα—H          (amino group on the LEFT = L-amino acid)
         |
         R             (side chain on BOTTOM)
```

**How to read it:** In a Fischer projection, the horizontal bonds point **toward you** (out of the page) and the vertical bonds point **away from you** (into the page). For **L-amino acids**, the amino group (-NH₃⁺) is on the **left** side. For D-amino acids, it would be on the right. The "L" literally stands for *levo* (Latin for left). Remember: **L = Left = Life** (all biological amino acids are L).

By the Cahn-Ingold-Pratt system, most L-amino acids are (S)-configured. The exception is **L-cysteine**, which is (R) because the sulfur in the side chain changes the priority ranking. This is a classic MCAT trap -- they love to test whether you understand that L/D and R/S are independent naming systems.

**Why only L-amino acids?** Ribosomes are chiral machines. The peptidyl transferase active site of the ribosome physically cannot accommodate D-amino acids in the A-site. This is a consequence of evolutionary selection for one enantiomer, not a chemical necessity. D-amino acids do exist in nature (bacterial cell walls contain D-alanine), but they are never incorporated by ribosomal translation.

### 1.3 Classifications and Side Chain Properties

You need to know these groupings cold. The logic behind the grouping matters more than rote memorization because the MCAT tests application. Classifications below follow Kaplan's system: grouped by side chain properties at physiological pH (7.4).

#### Nonpolar, Nonaromatic (G, A, V, L, I, M, P)

Aliphatic side chains -- mostly carbon and hydrogen. Driven into the **interior** of globular proteins in aqueous solution by the **hydrophobic effect** (the thermodynamic driving force is the increase in entropy of water molecules released from ordered cages around the nonpolar surface).

- **Glycine (G, Gly):** R-group is just a hydrogen. The simplest amino acid. It is the only **achiral** amino acid (two hydrogens on the alpha-carbon). Its small size gives the backbone extraordinary flexibility -- glycine is found in tight turns and loops where other residues would cause steric clashes. It is abundant in **collagen** (every third residue is Gly because the triple helix interior has no room for anything larger). Also an **inhibitory neurotransmitter** in the spinal cord.
- **Alanine (A, Ala):** Methyl group. The "default" nonpolar amino acid. The strongest **alpha-helix former**.
- **Valine (V, Val), Leucine (L, Leu), Isoleucine (I, Ile):** Branched-chain amino acids. Bulky hydrophobic side chains. Valine and isoleucine are **beta-branched** (the branching occurs at C-beta), which sterically hinders alpha-helix formation and favors **beta-sheets**. Leucine is the strongest alpha-helix former of this group because its branching starts at C-gamma, one carbon further out. Isoleucine has a **second chiral center** at C-beta (like threonine).
- **Methionine (M, Met):** Contains a thioether (sulfur flanked by two carbons). The **start codon (AUG)** codes for methionine, so every protein begins with Met (though it is often cleaved post-translationally). The sulfur can be oxidized but does not form disulfide bonds (unlike cysteine) because it is in a thioether, not a thiol.
- **Proline (P, Pro):** The side chain cyclizes back to the backbone nitrogen, creating a rigid five-membered ring. This has two huge consequences: (1) proline is a **helix breaker** because the ring locks the phi angle and prevents the backbone from adopting alpha-helical geometry; (2) proline introduces a fixed **kink** or bend in the chain, making it common in turns. Proline is technically an imino acid (secondary amine), not an amino acid, though the MCAT often ignores this distinction. In collagen, proline and its hydroxylated derivative **hydroxyproline** (requires vitamin C for the hydroxylation reaction) are critical for stability.

#### Aromatic (F, W, Y)

All three have ring systems and absorb UV light. They are grouped together because the aromatic ring dominates their chemistry, but they differ in polarity.

- **Phenylalanine (F, Phe):** Benzyl side chain. **Nonpolar** aromatic. Absorbs UV at ~257 nm but weakly. Accumulated in **phenylketonuria (PKU)** when phenylalanine hydroxylase is defective (cannot convert Phe to Tyr).
- **Tryptophan (W, Trp):** The largest amino acid. Indole ring system (bicyclic). **Nonpolar** aromatic. The dominant contributor to **UV absorbance at 280 nm** -- this is how protein concentration is estimated spectrophotometrically. Also the precursor to **serotonin** and **melatonin**.
- **Tyrosine (Y, Tyr):** Phenol side chain (--OH on an aromatic ring). **Polar** aromatic -- the hydroxyl group makes it polar, ionizable, and functionally distinct from Phe and Trp. Absorbs UV at ~275 nm (contributes to the 280 nm protein absorbance reading alongside Trp). The --OH has a pKa of ~10.5: uncharged at physiological pH, but deprotonates to --O⁻ at high pH. This ionizable side chain means Tyr is one of the 7 amino acids (D, E, C, Y, H, K, R) whose side chain pKa must be considered in pI calculations. Tyrosine is the target for **tyrosine kinases** (RTKs phosphorylate Tyr, distinct from Ser/Thr kinases). Synthesized from phenylalanine by phenylalanine hydroxylase (the reaction blocked in PKU).

> **Key within-group distinction:** Phe and Trp are hydrophobic aromatics. Tyr's --OH makes it polar, ionizable, and a phosphorylation target -- functionally very different despite being in the same structural family. The three phosphorylation targets across all categories are Ser, Thr (polar), and Tyr (aromatic).

#### Polar (S, T, C, N, Q)

These have side chains capable of hydrogen bonding but do not carry a formal charge at pH 7.4.

- **Serine (S, Ser) and Threonine (T, Thr):** Hydroxyl (-OH) groups. Key targets for **phosphorylation** by kinases (serine/threonine kinases are the most common class). Threonine has a second chiral center at C-beta (the only common amino acid with two stereocenters besides isoleucine). Serine is found in enzyme active sites (e.g., serine proteases like trypsin, chymotrypsin, elastase -- the catalytic triad is Ser-His-Asp).
- **Cysteine (C, Cys):** Thiol (-SH) side chain. Two cysteines can be oxidized to form a **disulfide bond** (-S-S-), a covalent cross-link that stabilizes tertiary and quaternary structure. Disulfide bonds are most common in **extracellular** proteins (the cytoplasm is a reducing environment that keeps cysteines reduced). The pKa of the thiol is ~8.3, so it is mostly protonated at pH 7 -- but in enzyme active sites, the local environment can lower this pKa. Cysteine is also found in the catalytic site of cysteine proteases. Note: Cys is classified as polar (uncharged at pH 7.4), but its ionizable side chain means it is one of the 7 amino acids whose side chain pKa matters for charge calculations.
- **Asparagine (N, Asn) and Glutamine (Q, Gln):** Amide-containing side chains (carboxamide). They are the amide derivatives of aspartate and glutamate, respectively. They can donate AND accept hydrogen bonds. Asparagine is the attachment point for **N-linked glycosylation** (sugar attached to the nitrogen of the amide).

> **MCAT Trap:** Do not confuse Asn/Gln (amides, uncharged) with Asp/Glu (carboxylates, negatively charged at pH 7). The difference is one oxygen vs one nitrogen on the side chain, but the charge consequences are enormous.

> **Truly never-charged polar residues:** Ser, Thr, Asn, and Gln -- their side chains do not ionize at any biologically relevant pH. Cys (pKa ~8.3) and Tyr (pKa ~10.5) are polar at pH 7.4 but can become charged under different pH conditions.

#### Positively Charged at pH 7.4 (K, R, H)

These have side chains with pKa values above 7 (for K and R, far above), so they are protonated and carry a +1 charge under physiological conditions.

- **Lysine (K, Lys):** pKa ~10.5 (epsilon-amino group). Long flexible side chain ending in -NH3+. Target for **acetylation** (histone acetylation neutralizes the positive charge, loosening DNA binding, promoting transcription) and **ubiquitination** (ubiquitin is attached via the lysine epsilon-amino group).
- **Arginine (R, Arg):** pKa ~12.5 (guanidinium group). The **most basic** amino acid. The guanidinium group is stabilized by resonance across three nitrogens, making it almost always protonated under any physiological condition. It forms strong salt bridges and is often found in active sites where it stabilizes negatively charged substrates or transition states.
- **Histidine (H, His):** pKa ~6.0 (imidazole ring). This is the most testable pKa on the exam. Because the pKa is near physiological pH, histidine can act as both a **proton donor and acceptor** at pH 7 -- making it perfect for **acid-base catalysis** in enzyme active sites. Found in the catalytic triad of serine proteases (His acts as a general base), in hemoglobin (proximal and distal His coordinate the heme iron), and in carbonic anhydrase (three His residues coordinate the Zn2+ ion).

#### Negatively Charged at pH 7.4 (D, E)

- **Aspartate (D, Asp):** pKa ~3.65. Carboxylate side chain, one carbon shorter than glutamate.
- **Glutamate (E, Glu):** pKa ~4.25. Carboxylate side chain. Glutamate is also a major **excitatory neurotransmitter** in the CNS and a metabolic intermediate (alpha-ketoglutarate link).

Both are fully deprotonated (negatively charged) at pH 7.4 because their pKa values are well below 7. They form **salt bridges** with positively charged residues (Lys, Arg) and coordinate metal ions in metalloenzymes. Aspartate is part of the catalytic triad in serine proteases.

### 1.4 Hydrophobicity Spectrum and Protein Localization

Understanding where residues end up in a folded protein requires thinking beyond the simple "polar vs nonpolar" binary. Residues fall on a **spectrum** of hydrophobicity, and their position on that spectrum determines whether they are driven to the protein interior, surface, or can go either way.

| Category | Residues | Typical location | Why |
|----------|----------|------------------|-----|
| **Hydrophobic** | A, V, L, I, F, W, M, P | Protein interior | Large nonpolar surface area; burying them maximizes the entropic hydrophobic effect |
| **In between** | S, T, C, Y, G | Either — context-dependent | Small polar groups (-OH, -SH) can H-bond but lack the pull to demand surface exposure |
| **Hydrophilic** | D, E, K, R, H, N, Q | Protein surface | Full ionic charges or large polar amide groups interact strongly with water; burying a charge in the low-dielectric protein interior is thermodynamically very costly |

**Why "polar" does not automatically mean "hydrophilic" in this context:**

The polar uncharged residues Ser, Thr, Cys, and Tyr have small polar groups — a single -OH or -SH. A single hydroxyl can hydrogen bond, but that interaction alone is not strong enough to force the residue to the protein surface. These residues are regularly found **both** on the surface and buried in the interior. This is functionally important: when Ser, Thr, or Cys are buried in an enzyme active site, their polar groups are what make them catalytically useful (e.g., the serine in the catalytic triad is buried, not surface-exposed). Cys residues forming disulfide bonds are often in the protein core.

By contrast, burying a fully charged residue like Glu in the hydrophobic protein interior almost never happens unless it serves a very specific catalytic role, because placing a full charge in a low-dielectric environment is extremely unfavorable.

Glycine lands in the middle as well — it is so small it has almost no hydrophobic or hydrophilic preference.

> **MCAT Tip:** The exam most often tests the extremes (charged = surface, hydrophobic = core). But passages may describe a mutation that replaces a buried hydrophobic residue with a charged one — recognize that this destabilizes the protein because you are forcing a hydrophilic residue into the interior.

### 1.5 Acid-Base Behavior and pI Calculations

Every amino acid has at least two ionizable groups: the alpha-amino group (pKa ~9-10) and the alpha-carboxyl group (pKa ~2). Amino acids with ionizable side chains (D, E, C, Y, H, K, R) have a third pKa.

**Henderson-Hasselbalch:** pH = pKa + log([A-]/[HA])

At a pH equal to the pKa of a given group, that group is exactly 50% protonated. This is the point of maximum buffering capacity for that group.

**Calculating pI (Isoelectric Point):**

The pI is the pH at which the amino acid has a net charge of zero. The rule:

1. **Draw out all the charged species at very low pH** (everything protonated -- full positive charge).
2. **Identify the two pKa values that flank the zero-charge species** (the zwitterion or the form where positive and negative charges cancel).
3. **Average those two pKa values.** That average is the pI.

For amino acids with no charged side chain:
- pI = (pKa1 + pKa2) / 2 = (~2 + ~9.5) / 2 = ~5.75

For amino acids with an acidic side chain (Asp, Glu):
- The zero-charge form has the side chain deprotonated and the amino group protonated, so you average the two lowest pKa values: pI = (pKa1 + pKaR) / 2. For Asp: ~(2.0 + 3.65) / 2 = ~2.8.

For amino acids with a basic side chain (Lys, Arg, His):
- You average the two highest pKa values: pI = (pKa2 + pKaR) / 2. For Lys: ~(9.5 + 10.5) / 2 = ~10.0.

### 1.5b Electrophoresis and pI — Predicting Migration Direction

This is a high-frequency MCAT question type. They give you a peptide's pI and the gel pH, and ask which direction it migrates. The rule:

- **pH < pI** → the molecule has **net positive charge** (solution is more acidic than the neutral point, so extra protons keep it protonated) → migrates toward the **cathode (negative electrode)**
- **pH > pI** → the molecule has **net negative charge** (solution is more basic, protons stripped off) → migrates toward the **anode (positive electrode)**
- **pH = pI** → net zero charge → **no migration**

**The intuition:** pI is the pH where the molecule is neutral. If the actual pH is lower (more acidic), there are more H⁺ in solution pushing the equilibrium toward protonation — the molecule becomes more positive. If the pH is higher (more basic), the molecule loses protons and becomes more negative. Opposite charges attract: positive molecules move toward the negative electrode, negative molecules toward the positive electrode.

**Worked example:** A peptide with pI = 5.5 is placed in a gel at pH 8.0. Since pH (8.0) > pI (5.5), the peptide carries a net negative charge and migrates toward the anode (positive electrode).

> **Isoelectric focusing (IEF):** A technique that separates proteins by pI. The gel has an immobilized pH gradient. Each protein migrates until it reaches the zone where pH = its pI, at which point it has zero net charge and stops. Proteins with different pI values stop at different positions.

### 1.6 Peptide Bond Formation

Amino acids link through **peptide bonds** -- a condensation reaction between the carboxyl group of one amino acid and the amino group of the next, releasing water. The peptide bond has **partial double-bond character** due to resonance (the lone pair on nitrogen delocalizes into the carbonyl), which means:

- The bond is **planar** (no free rotation around C-N).
- The bond is almost always in the **trans** configuration (the bulky R-groups on adjacent alpha-carbons are on opposite sides). The only common exception is **proline**, which has a significant population of cis peptide bonds because its cyclic side chain reduces the energy difference between cis and trans.
- The six atoms of the peptide unit (Ca-C-O-N-H-Ca) all lie in the same plane.
- Rotation IS allowed around the N-Ca bond (phi angle) and the Ca-C bond (psi angle). These torsion angles determine the secondary structure.

---

## 2. Protein Structure

### 2.1 Primary Structure

The linear sequence of amino acids from N-terminus to C-terminus. Determined by the gene. This is the ONLY level of structure that involves **covalent bonds** (peptide bonds and disulfide bonds). All higher levels of structure are ultimately dictated by the primary sequence.

**Denaturation** destroys secondary, tertiary, and quaternary structure but leaves primary structure (peptide bonds) intact. **Degradation** (proteolysis) actually cleaves peptide bonds. This distinction is a frequent MCAT question.

### 2.2 Secondary Structure

Local, regular folding patterns stabilized by **backbone hydrogen bonds** (between the C=O of one residue and the N-H of another). The R-groups are NOT involved in secondary structure hydrogen bonds -- this is a key concept.

#### Alpha-Helix
- **Right-handed** coil (like a standard screw).
- Hydrogen bonds form between the C=O of residue **i** and the N-H of residue **i+4** (the bond spans 4 residues).
- ~3.6 residues per turn. R-groups project **outward** from the helix.
- Stabilized by residues with small, uncharged side chains. **Alanine** is the best helix former.
- **Helix breakers:** Proline (rigid ring prevents proper phi angle), Glycine (too flexible -- entropically disfavored in the ordered helix).
- Alpha-helices are common in **transmembrane domains** (hydrophobic residues face outward into the lipid bilayer, ~20 residues span the membrane).

#### Beta-Sheet
- Extended strands connected by hydrogen bonds **between** strands (not within a single strand).
- Can be **parallel** (strands run in the same N-to-C direction) or **antiparallel** (strands alternate direction). Antiparallel sheets have straighter, stronger H-bonds and are more stable.
- R-groups alternate above and below the plane of the sheet.
- **Beta-branched** amino acids (Val, Ile, Thr) actually favor beta-sheets because the branching fits better in the extended conformation than in the tight helix.

#### Turns and Loops
- Reverse the direction of the polypeptide chain. **Beta-turns** are tight, often involving proline (introduces a kink) and glycine (small enough to fit tight angles).
- Loops are on the protein surface, often contain charged/polar residues, and are frequently the sites of antigen recognition in antibodies (complementarity-determining regions).

### 2.3 Tertiary Structure

The overall 3D shape of a single polypeptide. This is where the R-groups come into play. The forces that stabilize tertiary structure, ranked roughly from strongest to weakest:

1. **Disulfide bonds** (covalent, ~60 kcal/mol) -- between two cysteine residues. The strongest individual interaction. Mainly in extracellular proteins.
2. **Electrostatic interactions / salt bridges** (~3-7 kcal/mol) -- between oppositely charged side chains (e.g., Lys(+)...Asp(-)). Disrupted by changes in pH or high salt concentration.
3. **Hydrogen bonds** (~1-5 kcal/mol) -- between polar side chains, or between side chains and backbone. Individually weak but numerous.
4. **Hydrophobic interactions** (~1-3 kcal/mol per contact, but cumulatively the dominant driving force for folding) -- nonpolar side chains cluster in the protein interior to minimize contact with water. The **hydrophobic effect** is the single most important force driving protein folding overall, even though individual hydrophobic contacts are weak. The driving force is entropic: burying hydrophobic residues releases ordered water molecules.
5. **Van der Waals forces** (London dispersion, ~0.5-1 kcal/mol) -- weak but occur between all atoms in close contact. Their large number contributes significantly to stability in the tightly packed core.

> **MCAT Tip:** The exam loves to ask "What is the most important force for protein folding?" The answer is **hydrophobic interactions** (cumulative). But if asked "What is the strongest single bond?" the answer is **disulfide bonds** (covalent). Do not confuse these two questions.

### 2.4 Quaternary Structure

Multiple polypeptide **subunits** associate into a functional complex. Stabilized by the same non-covalent forces as tertiary structure (hydrophobic interactions, H-bonds, salt bridges, van der Waals) plus sometimes disulfide bonds between subunits.

**Cooperativity** is the hallmark testable concept for quaternary structure. **Hemoglobin** is the classic example:

- Hemoglobin is a **tetramer** (alpha2-beta2). Each subunit contains a heme group with an Fe2+ ion that binds O2.
- When the first O2 binds, it triggers a **conformational change** (T-state to R-state) that increases the affinity of the remaining subunits for O2. This is **positive cooperativity**.
- The oxygen-binding curve is **sigmoidal** (S-shaped), in contrast to myoglobin's **hyperbolic** curve (myoglobin is a monomer, no cooperativity).
- **Bohr effect:** Increased CO2, H+, temperature, or 2,3-BPG shifts the curve to the **right** (decreased affinity, promotes O2 unloading in active tissues). Decreased CO2, H+, temperature shifts left (increased affinity, promotes O2 loading in the lungs).
- **Fetal hemoglobin (HbF)** has gamma subunits instead of beta. Gamma subunits bind 2,3-BPG less strongly, so HbF has a **higher O2 affinity** than adult HbA (curve shifted left). This allows the fetus to extract O2 from maternal blood.

> **MCAT Trap:** The sigmoidal curve represents cooperativity. If a mutation abolishes quaternary structure (e.g., hemoglobin dissociates into monomers), the curve becomes hyperbolic like myoglobin's.

### 2.5 Denaturation

Loss of 3D structure (secondary, tertiary, quaternary) while the primary sequence stays intact. Caused by:

- **Heat:** disrupts H-bonds and hydrophobic interactions.
- **Extreme pH:** alters charge states of side chains, disrupts salt bridges.
- **Detergents (SDS):** coat proteins with negative charges, disrupt hydrophobic interactions.
- **Urea / guanidinium chloride:** disrupt hydrogen bonds.
- **Beta-mercaptoethanol (BME) or DTT:** reduce disulfide bonds specifically.
- **Mechanical agitation** (e.g., whipping egg whites).

Some proteins can **refold** spontaneously after denaturant is removed (Anfinsen's experiment with ribonuclease A showed this), demonstrating that all the information needed for folding is contained in the primary sequence. But many proteins require assistance from chaperones.

### 2.6 Chaperones and Chaperonins

- **Hsp70** (Heat Shock Protein 70): Binds to exposed hydrophobic regions of partially folded or misfolded proteins. Uses ATP hydrolysis to cycle between binding and release, giving the protein repeated chances to fold correctly. Works on proteins one-at-a-time. It does NOT provide a folding template -- it prevents aggregation.
- **Hsp60 / GroEL-GroES** (chaperonin): A large barrel-shaped complex. The unfolded protein enters the GroEL chamber, GroES caps it, and ATP hydrolysis drives conformational changes that give the protein a protected environment to fold. This is for proteins that cannot fold in the crowded cytoplasm. The key difference from Hsp70: chaperonins provide an **enclosed chamber**, while Hsp70 works in the open.

---

## Quick-Reference: Highest-Yield Facts for Test Day (Ch 1)

1. **Histidine pKa ~6** -- acid-base catalyst, only amino acid that ionizes near pH 7.
2. **Hydrophobic effect** is the dominant force driving protein folding; **disulfide bonds** are the strongest individual interactions.
3. Alpha-helix: i to i+4 H-bonds, 3.6 residues/turn. Pro and Gly break helices.
4. **Anfinsen's experiment:** Primary structure determines 3D fold. Denaturation is reversible when peptide bonds are intact.

→ Non-enzymatic protein function (collagen, keratin, elastin details), signal transduction, motor proteins: see Ch 3
→ Enzyme kinetics / catalysis: see Ch 2 (primary coverage in CP FC5E)
