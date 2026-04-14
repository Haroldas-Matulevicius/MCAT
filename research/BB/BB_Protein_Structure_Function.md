# FC1A: Protein Structure and Function -- Deep Dive

**Section:** Bio/Biochem (BB)
**Kaplan Reference:** Biochemistry Chapters 1--3
**Yield:** Extremely high. Amino acids, protein folding, and signal transduction appear on virtually every MCAT.

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

### 1.4 Acid-Base Behavior and pI Calculations

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

> **MCAT Tip:** A common question format shows electrophoresis or isoelectric focusing and asks which direction a peptide migrates at a given pH. If pH < pI, the molecule carries net positive charge and migrates toward the cathode (negative electrode). If pH > pI, net negative charge, migrates toward the anode (positive electrode). At pH = pI, no net migration.

### 1.5 Peptide Bond Formation

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

## 3. Non-Enzymatic Protein Functions

### 3.1 Structural Proteins

**Collagen:**
- The most abundant protein in the human body.
- Structure: three left-handed polyproline-II helices wind around each other to form a right-handed **triple helix** (a "rope").
- Sequence: repeating **Gly-X-Y** triplet, where X is often proline and Y is often hydroxyproline. Glycine MUST be every third residue because only its hydrogen side chain is small enough to fit inside the triple helix.
- **Hydroxyproline** is formed by post-translational hydroxylation of proline by **prolyl hydroxylase**, which requires **vitamin C (ascorbic acid)** as a cofactor. Without vitamin C, hydroxyproline cannot form, collagen is unstable, and the result is **scurvy** (bleeding gums, poor wound healing, fragile blood vessels).
- Collagen fibrils are cross-linked by **lysyl oxidase** (requires copper), which forms covalent cross-links between modified lysine residues on adjacent collagen molecules.

**Keratin:**
- Alpha-helical coiled-coil structure. Found in hair, nails, outer skin layer.
- Rich in cysteine -- extensive disulfide bonds provide mechanical strength.
- This is why hair perming works: reduce disulfide bonds with a chemical, reshape the hair, then re-oxidize to lock in the new shape.

**Elastin:**
- Found in lungs, blood vessels, skin -- tissues that need to stretch and recoil.
- Rich in glycine, proline, and hydrophobic residues. Has random coil regions and cross-linked regions (desmosine cross-links between four lysine residues).
- Cross-links allow elastic recoil -- like a rubber band.

### 3.2 Motor Proteins

All motor proteins use **ATP hydrolysis** to generate mechanical force along cytoskeletal tracks.

| Protein | Track | Direction | Key Function |
|---------|-------|-----------|--------------|
| **Myosin** | Actin (microfilaments) | Toward + end | Muscle contraction, cytokinesis |
| **Kinesin** | Microtubules | Toward + end (away from cell body) | Anterograde transport (moves cargo toward cell periphery) |
| **Dynein** | Microtubules | Toward - end (toward cell body) | Retrograde transport, moves cilia/flagella, spindle positioning in mitosis |

> **MCAT Mnemonic:** "Kin-away" -- kinesin walks away from the nucleus (toward the + end). Dynein is the "return trip" motor.

- **Cytoplasmic dynein** moves vesicles and organelles toward the centrosome.
- **Axonemal dynein** powers ciliary and flagellar beating (the "9+2" microtubule arrangement).
- In muscle contraction, myosin heads bind actin, undergo a **power stroke** (driven by Pi release), then release upon fresh ATP binding. This is the cross-bridge cycle.

### 3.3 Cell Adhesion Molecules

- **Cadherins:** Calcium-dependent homophilic adhesion. Cadherins on one cell bind cadherins of the same type on another cell. Connect to the actin cytoskeleton via catenins. E-cadherin loss is a hallmark of epithelial-to-mesenchymal transition (metastasis) -- high-yield for cancer questions.
- **Integrins:** Heterodimeric transmembrane proteins (alpha + beta subunit). Connect the **extracellular matrix (ECM)** to the intracellular **actin cytoskeleton**. They signal bidirectionally: outside-in (ECM binding triggers intracellular signaling) and inside-out (intracellular signals change integrin conformation to modulate ECM binding). Important in wound healing, immune cell migration, and platelet aggregation.

### 3.4 Immune Proteins

**Antibodies (Immunoglobulins):**
- Y-shaped structure with two heavy chains and two light chains, linked by disulfide bonds.
- **Variable regions** (tips of the Y) form the **antigen-binding site** -- two per antibody. Diversity generated by V(D)J recombination and somatic hypermutation.
- **Constant region** (stem of the Y, Fc region) determines the antibody class (IgG, IgA, IgM, IgD, IgE) and effector function (complement activation, opsonization, mast cell degranulation).
- IgG: most abundant in blood, crosses the placenta. IgM: first responder, pentamer. IgA: mucosal immunity (saliva, breast milk), dimer. IgE: allergy and parasites, binds mast cells.

**Complement system:**
- A cascade of plasma proteins that enhances antibody function. Three outcomes: (1) **opsonization** (coating pathogens for phagocytosis), (2) **inflammation** (C3a, C5a recruit immune cells), (3) **membrane attack complex (MAC)** -- C5b-C9 punch holes in pathogen membranes, causing lysis.

---

## 4. Signal Transduction

This is one of the most heavily tested topics in BB. You need to know the major pathways step-by-step and understand the logic of how signals are amplified and terminated.

### 4.1 General Principles

1. **Ligand** (signal molecule) binds a **receptor**.
2. Receptor activates an **intracellular signaling cascade**.
3. Cascade produces a **cellular response** (gene expression, metabolic change, cytoskeletal rearrangement, etc.).
4. The signal is **amplified** at multiple steps (one receptor activates many G-proteins, each adenylyl cyclase makes many cAMP, each PKA phosphorylates many targets).
5. The signal is **terminated** (ligand dissociation, receptor internalization, GTPase activity, phosphodiesterases degrade cAMP, phosphatases remove phosphate groups).

> **MCAT Tip:** Signal amplification is why hormones work at nanomolar concentrations. One hormone molecule can trigger the production of millions of product molecules through cascading activation.

### 4.2 G-Protein Coupled Receptors (GPCRs)

GPCRs are **seven-transmembrane-domain** receptors (the polypeptide crosses the membrane seven times). They are the largest family of cell surface receptors and the target of ~30% of all drugs.

The associated **heterotrimeric G-protein** has three subunits: alpha, beta, and gamma. In the inactive state, G-alpha is bound to **GDP**. Activation proceeds as follows:

1. Ligand binds the GPCR.
2. GPCR changes conformation and acts as a **GEF** (guanine nucleotide exchange factor) for the G-alpha subunit.
3. G-alpha **exchanges GDP for GTP** and dissociates from the beta-gamma complex.
4. The GTP-bound G-alpha (and sometimes beta-gamma) activates downstream effectors.
5. **Termination:** G-alpha has intrinsic **GTPase activity** -- it hydrolyzes GTP back to GDP, then reassociates with beta-gamma. The system resets.

#### Gs Pathway (Stimulatory)

Gs-alpha activates **adenylyl cyclase**, which converts ATP to **cAMP** (cyclic AMP).

cAMP activates **Protein Kinase A (PKA)**, which phosphorylates serine/threonine residues on downstream targets.

Examples:
- **Epinephrine** binding beta-adrenergic receptors in the heart: increases heart rate and contractility.
- **Glucagon** binding hepatocyte receptors: activates PKA, which phosphorylates glycogen phosphorylase kinase, which activates glycogen phosphorylase, leading to **glycogenolysis** (glycogen breakdown).
- **ACTH** stimulates cortisol release via the Gs pathway.

cAMP is degraded by **phosphodiesterase (PDE)** to AMP (inactive). Caffeine inhibits PDE, prolonging cAMP signaling. This is why caffeine increases alertness and heart rate.

#### Gi Pathway (Inhibitory)

Gi-alpha **inhibits** adenylyl cyclase, decreasing cAMP levels.

Example: Acetylcholine binding M2 muscarinic receptors in the heart decreases heart rate. (Note: the beta-gamma subunit of Gi also directly opens K+ channels in cardiac pacemaker cells, hyperpolarizing them.)

**Pertussis toxin** (from Bordetella pertussis) locks Gi in the inactive GDP-bound state by ADP-ribosylating the alpha subunit. This prevents Gi from inhibiting adenylyl cyclase, so cAMP levels stay high.

**Cholera toxin** locks Gs in the active GTP-bound state (prevents GTP hydrolysis). cAMP stays permanently high in intestinal epithelial cells, causing massive Cl- and water secretion -- resulting in the severe watery diarrhea of cholera.

> **MCAT Tip:** Cholera toxin = Gs always ON = cAMP always high. Pertussis toxin = Gi always OFF = cAMP stays high. Both result in elevated cAMP, but by different mechanisms. This is a very commonly tested distinction.

#### Gq Pathway

Gq-alpha activates **Phospholipase C (PLC)**, which cleaves **PIP2** (a membrane phospholipid) into two second messengers:

1. **IP3** (inositol 1,4,5-trisphosphate): Diffuses to the **endoplasmic reticulum**, binds IP3 receptors (ligand-gated Ca2+ channels), and triggers **Ca2+ release** from ER stores into the cytoplasm.
2. **DAG** (diacylglycerol): Stays in the membrane and activates **Protein Kinase C (PKC)**, which phosphorylates downstream targets. PKC activation also requires Ca2+, so IP3 and DAG cooperate.

The released Ca2+ often binds **calmodulin** (CaM), forming a Ca2+-calmodulin complex that activates **CaM-kinase (CaMK)** and other Ca2+-dependent enzymes (including calcineurin, myosin light chain kinase, and nitric oxide synthase).

Example: Alpha-1 adrenergic receptor activation by epinephrine in vascular smooth muscle triggers the Gq pathway, causing vasoconstriction through Ca2+-dependent smooth muscle contraction.

### 4.3 Receptor Tyrosine Kinases (RTKs)

RTKs are **single-pass transmembrane receptors** with intrinsic kinase activity. They are the main receptors for growth factors (EGF, PDGF, FGF, insulin, IGF-1).

**Activation mechanism:**

1. Ligand binding causes receptor **dimerization** (two RTK monomers come together).
2. The two intracellular kinase domains **trans-autophosphorylate** each other (each monomer phosphorylates tyrosine residues on the other). This is a critical concept: autophosphorylation means the receptor phosphorylates itself, trans means each monomer phosphorylates its partner.
3. Phosphorylated tyrosines serve as **docking sites** for signaling proteins containing **SH2 domains** (Src homology 2 domains), which specifically recognize phosphotyrosine.

#### The Ras-MAPK Cascade (step by step)

This is the prototypical RTK downstream pathway and extremely high-yield:

1. Adaptor protein **Grb2** binds phosphorylated RTK via its SH2 domain.
2. Grb2 recruits **SOS** (a GEF) via its SH3 domain.
3. SOS activates **Ras** (a small monomeric G-protein) by promoting the exchange of GDP for GTP.
4. GTP-bound Ras activates **Raf** (a MAP kinase kinase kinase, MAPKKK).
5. Raf phosphorylates and activates **MEK** (MAPKK).
6. MEK phosphorylates and activates **ERK** (MAPK).
7. ERK enters the nucleus and phosphorylates **transcription factors** that drive gene expression for cell growth, proliferation, and differentiation.

**Ras** is a G-protein, so it has intrinsic GTPase activity for self-termination. **GAPs** (GTPase-activating proteins) accelerate this hydrolysis. Mutations in Ras that abolish GTPase activity lock Ras in the ON state -- this is one of the most common oncogenic mutations (found in ~30% of human cancers, especially pancreatic, colorectal, and lung).

> **MCAT Tip:** Ras mutations are constitutively active gain-of-function mutations. They produce an oncoprotein from a proto-oncogene. Do not confuse with tumor suppressors (which require loss-of-function mutations).

#### Insulin Receptor Pathway

The insulin receptor is an RTK (technically pre-dimerized -- it exists as a disulfide-bonded alpha2-beta2 tetramer even before insulin binds). Insulin binding triggers autophosphorylation, which recruits **IRS-1** (insulin receptor substrate-1). IRS-1 activates **PI3K** (phosphoinositide 3-kinase), which produces **PIP3**. PIP3 activates **Akt (PKB)**, which promotes GLUT4 transporter translocation to the cell surface, glycogen synthesis, and cell survival. This PI3K/Akt pathway is a second major RTK branch separate from Ras-MAPK.

### 4.4 Second Messengers Summary

| Second Messenger | Produced By | Activates | Pathway |
|-----------------|-------------|-----------|---------|
| **cAMP** | Adenylyl cyclase (from ATP) | PKA | Gs/Gi GPCRs |
| **IP3** | PLC (from PIP2) | ER Ca2+ release | Gq GPCRs |
| **DAG** | PLC (from PIP2) | PKC | Gq GPCRs |
| **Ca2+** | Released from ER (via IP3) or enters through channels | CaM-kinase, calcineurin, PKC | Multiple |
| **cGMP** | Guanylyl cyclase (from GTP) | PKG | ANP, NO signaling |
| **PIP3** | PI3K (from PIP2) | Akt/PKB | RTKs (insulin) |

> **cGMP note:** Nitric oxide (NO) activates soluble guanylyl cyclase in smooth muscle cells, producing cGMP, which activates PKG, causing smooth muscle relaxation and vasodilation. This is the mechanism behind nitroglycerin (angina treatment) and sildenafil (PDE5 inhibitor that blocks cGMP degradation).

### 4.5 Ligand-Gated Ion Channels

These receptors are the fastest signaling mechanism. The receptor IS the channel. Ligand binding opens the channel directly, allowing ions to flow down their electrochemical gradient.

Examples:
- **Nicotinic acetylcholine receptor (nAChR):** ACh binds, Na+ flows in, causing depolarization. Found at the neuromuscular junction and in the CNS.
- **GABA-A receptor:** GABA binds, Cl- flows in, causing hyperpolarization (inhibitory). Benzodiazepines and barbiturates enhance GABA-A activity.
- **NMDA receptor:** Glutamate + glycine bind, Ca2+ and Na+ flow in. Requires both ligand binding AND membrane depolarization to remove the Mg2+ block. Important for learning and memory (long-term potentiation).

The key distinction from GPCRs: ligand-gated channels produce responses in **milliseconds** (direct ion flow), while GPCRs take **seconds to minutes** (multi-step cascade).

### 4.6 Intracellular Receptors

Lipophilic signaling molecules can **cross the plasma membrane** without a surface receptor. These include:

- **Steroid hormones:** cortisol, aldosterone, estrogen, testosterone, progesterone (all derived from cholesterol)
- **Thyroid hormones** (T3/T4): despite being amino acid derivatives, they are nonpolar enough to cross membranes (carried by transport proteins in blood)
- **Retinoids** (vitamin A derivatives) and **vitamin D**

These ligands bind **intracellular receptors** (often in the cytoplasm or nucleus) that function as **transcription factors**. The receptor-ligand complex enters the nucleus, binds to **hormone response elements (HREs)** on DNA, and directly activates or represses gene transcription.

Key distinction: intracellular receptor signaling is **slow** (hours -- requires new mRNA and protein synthesis) but **long-lasting** compared to cell-surface receptor signaling.

> **MCAT Tip:** If a question describes a hormone with effects that take hours to manifest and persist for a long time, think intracellular receptor. If the effects are rapid (seconds to minutes), think cell-surface receptor (GPCR, RTK, or ion channel).

### 4.7 Signal Amplification

This concept ties the whole section together. Each step in a signaling cascade can amplify the signal:

- One GPCR activates multiple G-proteins.
- One adenylyl cyclase produces many cAMP molecules.
- One PKA phosphorylates many target proteins.
- Each target may activate many downstream effectors.

The result: a single hormone molecule binding a single receptor can trigger the production of **millions** of product molecules inside the cell. The glycogen phosphorylase cascade is the classic textbook example of amplification: epinephrine -> Gs -> adenylyl cyclase -> cAMP -> PKA -> phosphorylase kinase -> glycogen phosphorylase -> glucose release. Each arrow represents a ~100-1000x amplification.

Signal termination is equally important and occurs at every level: receptor desensitization (phosphorylation by GRKs, arrestin binding, internalization), GTPase activity, phosphodiesterases (degrade cAMP/cGMP), phosphatases (remove phosphate groups from proteins), and proteasomal degradation of signaling components.

---

## Quick-Reference: Highest-Yield Facts for Test Day

1. **Histidine pKa ~6** -- acid-base catalyst, only amino acid that ionizes near pH 7.
2. **Hydrophobic effect** is the dominant force driving protein folding; **disulfide bonds** are the strongest individual interactions.
3. **Cholera toxin** = Gs locked ON = high cAMP. **Pertussis toxin** = Gi locked OFF = high cAMP.
4. **Ras** is the most commonly mutated oncogene -- locked in GTP-bound (active) state.
5. RTK activation requires **dimerization** then **trans-autophosphorylation**.
6. **cAMP -> PKA. IP3 -> Ca2+ release. DAG -> PKC. Ca2+ -> Calmodulin -> CaMK.**
7. Steroid hormones cross the membrane and bind intracellular receptors that act as transcription factors.
8. Alpha-helix: i to i+4 H-bonds, 3.6 residues/turn. Pro and Gly break helices.
9. Collagen: Gly-X-Y repeat, triple helix, requires vitamin C for hydroxyproline.
10. **Anfinsen's experiment:** Primary structure determines 3D fold. Denaturation is reversible when peptide bonds are intact.
