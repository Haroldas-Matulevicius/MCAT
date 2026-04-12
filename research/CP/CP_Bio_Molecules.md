# FC5D: Biologically Relevant Molecules

> Chem/Phys Deep Dive -- Organic Chemistry meets Biochemistry

This file bridges orgo and biochem for the CP section. Every topic here is high-yield. The MCAT loves testing whether you understand the **chemistry** behind biological molecules, not just their names.

---

## 1. Amino Acids (The Organic Chemistry Perspective)

### General Structure

Every amino acid has the same core:

- **Alpha-carbon** (the central carbon)
- **Amino group** (-NH2) bonded to the alpha-carbon
- **Carboxyl group** (-COOH) bonded to the alpha-carbon
- **Hydrogen** bonded to the alpha-carbon
- **R group** (side chain) -- this is what makes each amino acid unique

The alpha-carbon in all amino acids except glycine is a **chiral center** (4 different substituents). All biological amino acids are **L-amino acids** (S-configuration for most, except cysteine which is R due to sulfur priority).

**MCAT trap:** Glycine is the only achiral amino acid (R group = H, so two substituents are the same).

### Zwitterion Form and pI

At **physiological pH (~7.4)**, amino acids exist as **zwitterions**: the amino group is protonated (-NH3+) and the carboxyl group is deprotonated (-COO-). The molecule has no net charge but carries both a positive and a negative charge simultaneously.

**Why?** The carboxyl group has a pKa around 2 (gives up its proton easily), and the amino group has a pKa around 9 (holds onto its proton at neutral pH). At pH 7.4, the carboxyl is deprotonated and the amino is protonated.

**Isoelectric point (pI)** = the pH at which the amino acid has zero net charge.

Calculation rules:

- **No ionizable side chain:** pI = (pKa1 + pKa2) / 2 (average of the two backbone pKas)
- **Acidic side chain (Asp, Glu):** pI = (pKa1 + pKaR) / 2 (average of the two lowest pKas -- both acidic groups)
- **Basic side chain (Lys, Arg, His):** pI = (pKa2 + pKaR) / 2 (average of the two highest pKas -- both basic groups)

**The rule:** Average the two pKas that flank the zwitterion (zero net charge) form. Draw out the charge states if you're unsure.

**MCAT application:** Electrophoresis and isoelectric focusing. At a pH below pI, the amino acid carries a net positive charge and migrates toward the cathode (negative electrode). At a pH above pI, net negative charge, migrates toward the anode.

### Peptide Bond Formation

The **peptide bond** forms via a **condensation (dehydration) reaction** between the carboxyl group of one amino acid and the amino group of another, releasing water.

Key properties of the peptide bond:

1. **Partial double bond character** -- The lone pair on nitrogen delocalizes into the carbonyl (C=O), giving the C-N bond roughly 40% double bond character. This is resonance stabilization.

2. **Planarity** -- Because of the partial double bond character, the six atoms of the peptide bond unit (C-alpha, C=O, N-H, C-alpha) all lie in the same plane. Rotation is restricted around the C-N bond.

3. **Trans configuration** -- The two alpha-carbons (and their substituents) are on opposite sides of the peptide bond. Trans is favored because it minimizes steric clash. Exception: **proline** can adopt cis configuration more readily because its cyclic side chain reduces the energy difference between cis and trans.

4. **Rigidity** -- Phi (phi) and psi angles (rotations around bonds to the alpha-carbon) can rotate freely, but omega (the peptide bond itself) is locked at ~180 degrees (trans).

**MCAT trap:** The peptide bond is NOT a true double bond. It has partial double bond character due to resonance. Don't confuse "planar" with "completely rigid" -- the backbone still has flexibility at phi/psi angles.

### Peptide Bond Hydrolysis

The reverse of condensation: water breaks the peptide bond, regenerating the free amino and carboxyl groups. This is:

- **Catalyzed by proteases** in vivo (e.g., trypsin, chymotrypsin, pepsin)
- Thermodynamically favorable (peptide bonds are kinetically stable but thermodynamically unstable -- they persist only because the activation energy is high)
- **Acid hydrolysis** (6M HCl, 110 degrees C, 24 hrs) breaks ALL peptide bonds -- used in amino acid analysis
- **Base hydrolysis** also works but can cause racemization

---

## 2. Proteins: The Chemistry

This section focuses on the **chemical interactions** that build protein structure. The biology of protein function is BB territory.

### Levels of Structure

| Level | What defines it | Key bonds/forces |
|-------|----------------|-----------------|
| **Primary** | Linear sequence of amino acids | Peptide bonds (covalent) |
| **Secondary** | Local folding patterns (alpha-helices, beta-sheets) | Hydrogen bonds between backbone N-H and C=O |
| **Tertiary** | Overall 3D shape of one polypeptide | Hydrophobic interactions, H-bonds, ionic bonds (salt bridges), disulfide bonds, van der Waals |
| **Quaternary** | Assembly of multiple polypeptide subunits | Same forces as tertiary, between subunits |

### Disulfide Bonds

- Formed between two **cysteine** residues (the thiol -SH groups oxidize to form -S-S-)
- This is a **covalent bond** -- much stronger than the noncovalent forces
- Common in extracellular proteins (the extracellular environment is oxidizing)
- Can be reduced (broken) by agents like beta-mercaptoethanol or DTT

### Denaturation

**Denaturation** = loss of secondary, tertiary, and quaternary structure. The protein unfolds.

**What is NOT lost:** Primary structure. Peptide bonds remain intact. The amino acid sequence is unchanged.

**Denaturing agents:** Heat, extreme pH, urea, guanidinium chloride, detergents (SDS), heavy metals, organic solvents.

**MCAT trap:** "Denaturation breaks all bonds in the protein" is FALSE. It breaks noncovalent interactions (and disulfide bonds in some conditions), but peptide bonds survive denaturation. To break peptide bonds you need hydrolysis.

---

## 3. Nucleotides and Nucleic Acids

### Nucleotide Structure

A nucleotide has three components:

1. **Nitrogenous base** -- purine or pyrimidine
2. **Pentose sugar** -- ribose (RNA) or deoxyribose (DNA)
3. **Phosphate group(s)** -- 1, 2, or 3 (mono-, di-, triphosphate)

A **nucleoside** = base + sugar only (no phosphate). Naming: adenosine (nucleoside) vs adenosine monophosphate/AMP (nucleotide).

### Purines vs Pyrimidines

- **Purines (A, G):** Two fused rings (a 6-membered ring fused to a 5-membered ring). **Pu**re **A**s **G**old -- purines are the bigger bases.
- **Pyrimidines (C, T, U):** One 6-membered ring. **CUT** the **py** -- pyrimidines are smaller.

Mnemonic: Pur**i**nes have **i** -- but actually, think of it as "pure" = two rings. Or: the longer word (pyrimidine) has the smaller molecule.

Base pairing (Watson-Crick):
- **A = T** (or A = U in RNA): 2 hydrogen bonds
- **G triple bond C**: 3 hydrogen bonds

**MCAT application:** More G-C content = higher melting temperature (Tm) of DNA because 3 H-bonds > 2 H-bonds per pair.

### Ribose vs Deoxyribose

- **Ribose** (RNA): has an -OH at the 2' carbon
- **Deoxyribose** (DNA): has only -H at the 2' carbon ("deoxy" = missing an oxygen)

The 2'-OH in RNA makes it more susceptible to **base-catalyzed hydrolysis** (the 2'-OH acts as an internal nucleophile attacking the phosphodiester bond). This is why DNA is more chemically stable than RNA -- a smart design choice for long-term genetic storage.

### Phosphodiester Bonds

Nucleotides are linked by **phosphodiester bonds**: the phosphate group connects the 3'-OH of one sugar to the 5'-OH of the next sugar. This creates the **sugar-phosphate backbone**.

The linkage is called 3'-5' phosphodiester bond. The backbone is negatively charged at physiological pH (each phosphate carries a negative charge).

**MCAT point:** The negative charge of the backbone means DNA migrates toward the positive electrode (anode) in gel electrophoresis. Smaller fragments migrate faster.

### DNA Double Helix

Key features:

- **Antiparallel** strands: one runs 5' to 3', the other runs 3' to 5'
- **Right-handed helix** (B-form DNA is the standard)
- **Major groove** and **minor groove**: proteins bind here to read the DNA sequence without unwinding it. The major groove contains more chemical information and is the primary site for protein-DNA recognition.
- Bases are stacked inside the helix; sugar-phosphate backbone is on the outside
- **Stabilized by:** H-bonds between base pairs AND base stacking interactions (van der Waals/hydrophobic forces between the flat aromatic rings)

### RNA Types and Structure

| Type | Function | Key feature |
|------|----------|-------------|
| **mRNA** | Carries genetic code from DNA to ribosome | Linear, has 5' cap and 3' poly-A tail in eukaryotes |
| **tRNA** | Delivers amino acids to ribosome | Cloverleaf (2D), L-shaped (3D), has anticodon loop |
| **rRNA** | Structural and catalytic component of ribosomes | Most abundant RNA, has catalytic activity (ribozyme) |

RNA can form complex secondary structures through intramolecular base pairing (hairpins, stem-loops, pseudoknots). Unlike DNA, RNA is usually single-stranded but can fold back on itself.

---

## 4. Lipids

Lipids are defined by their **solubility** (soluble in nonpolar organic solvents, insoluble in water), not by a single structural motif.

### Fatty Acids

A long hydrocarbon chain with a carboxyl group (-COOH) at one end.

**Saturated:** No C=C double bonds. Straight chains that pack tightly. **Higher melting point.** Solid at room temperature (think: butter, animal fat).

**Unsaturated:** One or more C=C double bonds, almost always in the **cis** configuration in nature. Cis double bonds create **kinks** in the chain, preventing tight packing. **Lower melting point.** Liquid at room temperature (think: olive oil).

**MCAT connection:** Trans fats have double bonds in trans configuration -- they behave more like saturated fats (straight chains, high melting point) and are associated with cardiovascular disease.

**Essential fatty acids:** Linoleic acid (omega-6) and alpha-linolenic acid (omega-3) -- the body cannot synthesize these.

### Triacylglycerols (Triglycerides)

**Structure:** Glycerol + 3 fatty acids linked by **ester bonds**.

Formation: Each -OH of glycerol undergoes a condensation reaction with the -COOH of a fatty acid, producing an ester linkage and releasing water. Three ester bonds total.

**Function:** Primary energy storage in animals. More energy-dense than carbohydrates because fats are more reduced (more C-H bonds to oxidize).

**Saponification:** Base hydrolysis of a triacylglycerol.

TAG + 3 NaOH --> Glycerol + 3 Fatty acid sodium salts (soap)

The fatty acid salts are **amphipathic** (hydrophilic carboxylate head + hydrophobic hydrocarbon tail), which is why they work as soap -- they form micelles around grease particles.

**MCAT trap:** Saponification is irreversible (unlike acid-catalyzed hydrolysis which is an equilibrium). The strong base deprotonates the fatty acid, driving the reaction forward.

### Phospholipids

**Structure:** Glycerol + 2 fatty acids + 1 phosphate group (often with an additional head group attached to the phosphate: choline, serine, ethanolamine, inositol).

**Amphipathic:** The phosphate head is hydrophilic; the two fatty acid tails are hydrophobic. This drives spontaneous formation of:

- **Micelles** (single layer, hydrophobic core) -- forms when lipid concentration exceeds the critical micelle concentration
- **Bilayers** (two layers, tails facing inward) -- this is the basis of all biological membranes
- **Liposomes** (bilayer forming a sphere)

**Membrane fluidity** depends on:
- Unsaturated fatty acids (more = more fluid -- kinks prevent packing)
- Cholesterol (at high temps it decreases fluidity; at low temps it prevents crystallization -- it's a fluidity buffer)
- Chain length (shorter = more fluid)
- Temperature (higher = more fluid)

### Sphingolipids

Built on a **sphingosine backbone** (an amino alcohol with a long hydrocarbon chain) instead of glycerol.

- **Ceramide:** sphingosine + 1 fatty acid (via amide bond)
- **Sphingomyelin:** ceramide + phosphocholine (found in myelin sheaths)
- **Glycosphingolipids:** ceramide + sugar(s) -- includes cerebrosides (1 sugar) and gangliosides (oligosaccharide with sialic acid)

**MCAT relevance:** Sphingolipid storage diseases (Tay-Sachs, Gaucher, Niemann-Pick) are tested in BB/biochem contexts. For CP, just know the structural difference from glycerophospholipids.

### Steroids

**Core structure:** Four fused rings -- three **cyclohexane** rings (A, B, C) + one **cyclopentane** ring (D). All steroids share this skeleton.

**Cholesterol** is the precursor to:
- **Steroid hormones:** cortisol, aldosterone, testosterone, estrogen, progesterone
- **Bile salts:** amphipathic molecules that emulsify dietary fats in the intestine
- **Vitamin D:** cholesterol in skin is converted to vitamin D3 by UV light

Cholesterol has a hydroxyl group (making one end slightly polar), a rigid ring system, and a hydrocarbon tail. In membranes, it inserts between phospholipids with the -OH near the polar heads.

### Prostaglandins

- Derived from **arachidonic acid** (a 20-carbon polyunsaturated fatty acid)
- Contain a **5-membered ring** within the carbon chain
- Function as **local signaling molecules** (autocrine/paracrine) -- not transported in blood like hormones
- Roles: inflammation, pain, fever, blood clotting, smooth muscle contraction
- **NSAIDs** (aspirin, ibuprofen) block cyclooxygenase (COX), the enzyme that makes prostaglandins from arachidonic acid
- Aspirin specifically **irreversibly** inhibits COX (acetylates a serine residue)

### Fat-Soluble Vitamins: A, D, E, K

Mnemonic: "**ADEK**" -- these are absorbed with dietary fat and can accumulate in adipose tissue (risk of toxicity, unlike water-soluble vitamins which are excreted in urine).

| Vitamin | Key function | Notes |
|---------|-------------|-------|
| **A** (retinol) | Vision (retinal in rhodopsin), cell differentiation | Deficiency: night blindness |
| **D** (cholecalciferol) | Calcium and phosphate absorption, bone mineralization | Made from cholesterol + UV light; acts like a hormone |
| **E** (tocopherol) | Antioxidant (protects membranes from lipid peroxidation) | Scavenges free radicals |
| **K** (phylloquinone) | Blood clotting (required for clotting factor synthesis) | Made by gut bacteria; "K" for "Koagulation" |

---

## 5. Carbohydrates

### Monosaccharides

General formula: (CH2O)n -- literally "hydrate of carbon."

**Aldoses vs Ketoses:**
- **Aldose:** carbonyl at C1 (aldehyde). Example: glucose, galactose
- **Ketose:** carbonyl at C2 (ketone). Example: fructose

**D vs L configuration:**
- Look at the **highest-numbered chiral carbon** (the chiral center farthest from the carbonyl)
- If the -OH points to the **right** in a Fischer projection: **D-sugar**
- If the -OH points to the **left**: **L-sugar**
- Almost all biological sugars are **D-sugars**

**MCAT trap:** D and L do NOT tell you about optical rotation (+/-). D-glucose happens to be dextrorotatory (+), but D-fructose is levorotatory (-). You cannot predict the sign of rotation from the D/L designation.

### Anomers and Epimers

**Epimers:** Two sugars that differ at exactly **one** chiral center.
- Glucose and galactose are **C4 epimers** (they differ only at carbon 4)
- Glucose and mannose are **C2 epimers**

**Anomers:** Sugars that differ at the **anomeric carbon** (C1 for aldoses, C2 for ketoses) -- the new chiral center formed during cyclization.
- **Alpha anomer:** the -OH on the anomeric carbon is **axial** (pointing down in a Haworth projection, trans to the CH2OH group in D-sugars)
- **Beta anomer:** the -OH on the anomeric carbon is **equatorial** (pointing up in a Haworth projection, cis to the CH2OH group)

**Mutarotation:** In solution, alpha and beta anomers interconvert through the open-chain form until equilibrium is reached. This is why a pure sample of alpha-D-glucose will show a changing optical rotation over time until it reaches an equilibrium value.

### Cyclization (Ring Closure)

When a monosaccharide cyclizes, the carbonyl reacts with an -OH group on the same molecule (intramolecular hemiacetal or hemiketal formation):

- **Aldehyde + OH --> hemiacetal** (aldose cyclization)
- **Ketone + OH --> hemiketal** (ketose cyclization)

Ring sizes:
- **Pyranose:** 6-membered ring (5 carbons + 1 oxygen). Glucose typically forms a pyranose ring.
- **Furanose:** 5-membered ring (4 carbons + 1 oxygen). Fructose typically forms a furanose ring.

**Haworth projections:** The ring is drawn as a flat polygon. Groups on the right in a Fischer projection point down in a Haworth projection; groups on the left point up.

### Glycosidic Bonds

Formed between the **anomeric carbon** of one sugar and an -OH of another sugar. This is an acetal/ketal formation (condensation reaction, releases water).

**Alpha-1,4 glycosidic bond:** Found in starch and glycogen. The anomeric -OH is in the alpha position, linking C1 of one glucose to C4 of another.

**Beta-1,4 glycosidic bond:** Found in cellulose. Same linkage but with beta configuration at the anomeric carbon.

**Why humans can't digest cellulose:** We have alpha-amylase (breaks alpha linkages) but lack cellulase (which breaks beta-1,4 linkages). Cows and termites can digest cellulose because their gut bacteria produce cellulase.

**Alpha-1,6 glycosidic bond:** Found at branch points in glycogen and amylopectin.

### Key Disaccharides

| Disaccharide | Components | Bond | Notes |
|-------------|------------|------|-------|
| **Maltose** | Glucose + Glucose | alpha-1,4 | Product of starch digestion |
| **Lactose** | Galactose + Glucose | beta-1,4 | Milk sugar; lactose intolerance = deficiency of lactase |
| **Sucrose** | Glucose + Fructose | alpha-1,2 | Table sugar; non-reducing sugar (both anomeric carbons are involved in the bond) |

**Reducing vs non-reducing sugars:** A reducing sugar has a free anomeric carbon that can open to an aldehyde and reduce another compound. Sucrose is a **non-reducing** sugar because both anomeric carbons participate in the glycosidic bond -- neither can open.

### Polysaccharides

| Polysaccharide | Monomer | Linkage | Branching | Function |
|---------------|---------|---------|-----------|----------|
| **Amylose** | Glucose | alpha-1,4 | None (linear) | Plant energy storage (component of starch) |
| **Amylopectin** | Glucose | alpha-1,4 + alpha-1,6 | Branched every ~25 residues | Plant energy storage (component of starch) |
| **Glycogen** | Glucose | alpha-1,4 + alpha-1,6 | Highly branched (every ~10 residues) | Animal energy storage (liver and muscle) |
| **Cellulose** | Glucose | beta-1,4 | None (linear) | Structural (plant cell walls) |
| **Chitin** | N-acetylglucosamine | beta-1,4 | None (linear) | Structural (arthropod exoskeletons, fungal cell walls) |

**MCAT connection:** Glycogen is more branched than amylopectin. More branch points = more non-reducing ends = faster glucose mobilization (enzymes work at the ends). This makes glycogen ideal for rapid energy needs.

---

## 6. Organic Reactions Tested on the MCAT

### SN1 / SN2 / E1 / E2 Decision Framework

This is one of the most-tested orgo topics. You MUST be able to predict the dominant mechanism given a set of conditions.

#### The Four Mechanisms at a Glance

| Feature | SN2 | SN1 | E2 | E1 |
|---------|-----|-----|-----|-----|
| **Mechanism** | One step, concerted | Two steps (carbocation intermediate) | One step, concerted | Two steps (carbocation intermediate) |
| **Rate law** | Rate = k[substrate][nucleophile] | Rate = k[substrate] | Rate = k[substrate][base] | Rate = k[substrate] |
| **Stereochemistry** | Inversion (Walden inversion) | Racemization (+ some inversion) | Anti-periplanar elimination | No stereospecificity |
| **Substrate preference** | Methyl > 1 degrees > 2 degrees (3 degrees = no) | 3 degrees > 2 degrees (1 degrees/methyl = no) | 3 degrees > 2 degrees > 1 degrees | 3 degrees > 2 degrees |
| **Rearrangements** | No | Yes (carbocation can rearrange) | No | Yes |

#### The Decision Tree

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

#### Key Variables Explained

**Nucleophile strength** (favors substitution):
- Strong nucleophiles: CN-, RS-, I-, HO-, RO-, NH3, N3-
- Weak nucleophiles: H2O, ROH, RCOOH
- Rule: Charged species are generally stronger nucleophiles than their neutral counterparts

**Base strength** (favors elimination):
- Strong bases: OH-, RO-, NaH, LDA, tBuOK
- Weak bases: H2O, ROH
- Bulky strong bases (tBuOK, LDA) strongly favor E2 over SN2

**Solvent:**
- **Polar protic** (water, alcohols, carboxylic acids): Stabilize carbocations through solvation. Favor SN1/E1. Also hinder SN2 by solvating the nucleophile.
- **Polar aprotic** (DMSO, DMF, acetone, acetonitrile): Do NOT solvate nucleophiles well. Favor SN2 (nucleophile is "naked" and reactive).

**Temperature:**
- Higher temperature favors elimination (E1, E2) over substitution. Elimination has a higher activation entropy (Delta-S is more positive because you're making more molecules from fewer).

#### Quick-Fire MCAT Rules

1. Methyl/1 degrees + strong nuc + polar aprotic solvent = **SN2**
2. 3 degrees + strong base = **E2**
3. 3 degrees + weak nuc/base + polar protic = **SN1/E1 mix** (heat tips toward E1)
4. 2 degrees = **look at everything** (default: strong nuc = SN2, strong base = E2, weak nuc + protic = SN1/E1)
5. Bulky base = **always E2**
6. Heat = **favors elimination**
7. SN2: **inversion**. SN1: **racemization**.
8. SN1/E1 intermediates can **rearrange** (hydride shifts, methyl shifts to form more stable carbocation)

---

### Carbonyl Chemistry

The C=O is the most important functional group in organic chemistry. The carbon is **electrophilic** (delta+) due to the electronegativity of oxygen. Nucleophiles attack the carbonyl carbon.

#### Nucleophilic Addition (Aldehydes and Ketones)

The nucleophile attacks the carbonyl carbon, breaking the pi bond. The oxygen picks up a proton (or remains as an alkoxide, depending on conditions).

**Why aldehydes are more reactive than ketones:**
1. **Steric:** Ketones have two R groups flanking the carbonyl; aldehydes have only one R group and one H. Less steric hindrance = easier nucleophilic attack.
2. **Electronic:** Alkyl groups are electron-donating (inductive effect), which partially stabilizes the partial positive charge on the carbonyl carbon. Ketones have two electron-donating groups, making the carbon less electrophilic.

Key nucleophilic addition reactions:

| Nucleophile | Product | Conditions |
|-------------|---------|------------|
| ROH (1 equiv) | **Hemiacetal/hemiketal** | Acid catalyst |
| ROH (2 equiv) | **Acetal/ketal** | Acid catalyst, remove water |
| RNH2 (primary amine) | **Imine (Schiff base)** | Mild acid, remove water |
| R2NH (secondary amine) | **Enamine** | Mild acid, remove water |
| HCN | **Cyanohydrin** | Base catalyst (CN- is nucleophile) |
| RMgBr (Grignard) | **Alcohol** (after protonation) | Anhydrous conditions, then H3O+ |
| NaBH4 or LiAlH4 | **Alcohol** (reduction) | NaBH4 for mild, LiAlH4 for strong |

**MCAT-critical:** Hemiacetal/hemiketal formation is exactly what happens during **sugar cyclization**. Glucose (aldehyde) forms an intramolecular hemiacetal. This connects orgo to carbohydrate chemistry directly.

**Acetals as protecting groups:** Acetals are stable under basic and neutral conditions but cleave under acidic conditions (aqueous acid). This means acetals can protect carbonyls during reactions performed in base.

#### Imine and Enamine Formation

- **Imine:** Primary amine attacks carbonyl, water leaves. Product has C=N. Reversible under aqueous acid conditions.
- **Enamine:** Secondary amine attacks carbonyl, water leaves. Product has C=C adjacent to nitrogen. Also reversible.

**MCAT connection:** Transamination reactions in amino acid metabolism use Schiff base (imine) intermediates with PLP (pyridoxal phosphate) as the coenzyme. This is where orgo meets metabolism.

---

### Enolate Chemistry

**Alpha-hydrogen:** A hydrogen on the carbon adjacent to a carbonyl. It is **acidic** (pKa ~20 for ketones, ~25 for esters) because the conjugate base -- the **enolate** -- is stabilized by resonance (negative charge delocalized between carbon and oxygen).

**Enol:** The tautomer of a ketone/aldehyde where the proton has shifted to oxygen and a C=C double bond forms. Keto-enol tautomerism is catalyzed by both acid and base.

**MCAT rule:** The keto form is almost always more stable and predominant at equilibrium (exception: 1,3-dicarbonyl compounds where the enol is stabilized by intramolecular H-bonding and extended conjugation).

#### Aldol Condensation

1. Base removes the alpha-hydrogen, forming an enolate
2. The enolate (nucleophile) attacks the carbonyl carbon of another aldehyde/ketone molecule
3. Product: **beta-hydroxy carbonyl** (aldol product)
4. If heated, dehydration occurs: loss of water gives an **alpha,beta-unsaturated carbonyl** (aldol condensation product)

**Retro-aldol:** The reverse reaction -- a beta-hydroxy carbonyl breaks into two smaller carbonyl compounds. This is important in **glycolysis** (fructose-1,6-bisphosphate is split by aldolase into DHAP and G3P via a retro-aldol mechanism).

**MCAT connection:** Aldol and retro-aldol reactions appear in multiple metabolic pathways. Recognizing these reaction types in a biochemical context is high-yield.

---

### Alcohol Reactions

#### Oxidation of Alcohols

This is tested frequently. Know the pattern:

| Alcohol type | Oxidation product | Reagent examples |
|-------------|-------------------|-----------------|
| **Primary (1 degrees)** | **Aldehyde** (mild oxidation) | PCC (pyridinium chlorochromate) -- stops at aldehyde |
| **Primary (1 degrees)** | **Carboxylic acid** (full oxidation) | KMnO4, CrO3/H2SO4 (Jones), Na2Cr2O7/H2SO4 |
| **Secondary (2 degrees)** | **Ketone** | PCC, KMnO4, CrO3, Na2Cr2O7 (all work -- ketones resist further oxidation) |
| **Tertiary (3 degrees)** | **No oxidation** | Cannot be oxidized without breaking C-C bonds |

**Why can't tertiary alcohols be oxidized?** Oxidation of an alcohol requires removing a hydrogen from the carbon bearing the -OH. Tertiary carbons have no such hydrogen.

**MCAT mnemonic:** Oxidation = loss of H or gain of O (or loss of electrons). Going from alcohol to aldehyde to carboxylic acid, you are progressively losing hydrogen or gaining oxygen.

#### Reduction

The reverse of oxidation:
- Carboxylic acid --> aldehyde --> primary alcohol (using LiAlH4)
- Ketone --> secondary alcohol (using NaBH4 or LiAlH4)

**NaBH4 vs LiAlH4:**
- **NaBH4:** Milder. Reduces aldehydes and ketones only. Does NOT reduce esters or carboxylic acids.
- **LiAlH4:** Stronger. Reduces aldehydes, ketones, esters, carboxylic acids, amides, epoxides. Requires anhydrous conditions (reacts violently with water).

---

### Carboxylic Acid Derivatives

These are all compounds with a carbonyl bonded to a heteroatom-containing leaving group. They undergo **nucleophilic acyl substitution** (not just nucleophilic addition like aldehydes/ketones).

#### Reactivity Ranking

**Acyl halide > Anhydride > Ester > Amide**

(Most reactive --------------------------------> Least reactive)

**Why this order?** It comes down to **leaving group ability**:

- **Acyl halide (RCOX):** Halide (Cl-, Br-) is an excellent leaving group -- very stable anion, weak base. Also, the halogen is electronegative and withdraws electron density from the carbonyl, making it more electrophilic.
- **Anhydride (RCO-O-COR):** Leaving group is a carboxylate (RCOO-), which is resonance-stabilized. Good leaving group.
- **Ester (RCOOR'):** Leaving group is an alkoxide (RO-), which is a moderately strong base. Decent but not great leaving group.
- **Amide (RCONHR'):** Leaving group would be an amine/amide ion (RNH- or NH2-), which is a strong base and terrible leaving group. Nitrogen also donates its lone pair into the carbonyl (strong resonance), making the carbonyl carbon less electrophilic.

**MCAT principle:** The better the leaving group and the less resonance stabilization of the carbonyl by the heteroatom, the more reactive the derivative.

#### Nucleophilic Acyl Substitution Mechanism

1. **Nucleophile attacks** the carbonyl carbon (tetrahedral intermediate forms)
2. **Leaving group departs**, regenerating the C=O

This differs from nucleophilic addition (aldehydes/ketones) because aldehydes/ketones have -H or -R as substituents, which are NOT leaving groups. Carboxylic acid derivatives have leaving groups that can depart, so the tetrahedral intermediate collapses back to a carbonyl.

**You can always go DOWN the reactivity ladder, but not up** (without special activation):
- Acyl halide can be converted to anhydride, ester, or amide
- Anhydride can be converted to ester or amide
- Ester can be converted to amide
- Amide requires special conditions to convert to anything else (it's the most stable)

**MCAT application:** Peptide bond formation is technically making an amide from an amine and a carboxylic acid (or activated derivative). The ribosome uses the high energy of aminoacyl-tRNA (activated ester) to drive amide bond formation.

#### Key Reactions of Carboxylic Acid Derivatives

**Transesterification:** One ester is converted to another by reaction with a different alcohol (catalyzed by acid or base). Exchange of the -OR group.

**Hydrolysis (acid):** Ester + H2O (H+ catalyst) --> Carboxylic acid + Alcohol. This is an equilibrium (Le Chatelier: excess water drives it forward).

**Hydrolysis (base = saponification):** Ester + OH- --> Carboxylate + Alcohol. This is irreversible because the carboxylate ion is resonance-stabilized and does not react with the alcohol under basic conditions.

**Fischer esterification:** Carboxylic acid + Alcohol (H+ catalyst, heat) --> Ester + Water. The reverse of acid hydrolysis. Equilibrium reaction -- remove water to drive forward.

**Amide hydrolysis:** Requires harsh conditions (strong acid or base, heat) because the amide bond is so stable. This is why peptide bonds persist under physiological conditions -- they are kinetically stable even though hydrolysis is thermodynamically favorable.

---

## High-Yield Summary: What the MCAT Loves to Test in This Topic Area

1. **Amino acid properties** -- recognizing charges at different pH, calculating pI, peptide bond characteristics
2. **Sugar chemistry** -- anomers vs epimers, alpha vs beta linkages, reducing vs non-reducing sugars, cyclization as hemiacetal formation
3. **SN1/SN2/E1/E2** -- predicting the mechanism from substrate + nucleophile/base + solvent + temperature
4. **Carbonyl reactivity** -- why aldehydes > ketones, nucleophilic addition products (especially hemiacetal and imine)
5. **Carboxylic acid derivative ranking** -- know the order and WHY (leaving group stability)
6. **Lipid structure** -- saturated vs unsaturated, saponification, phospholipid amphipathicity, cholesterol's dual role in membrane fluidity
7. **Connecting orgo to biochem** -- hemiacetal formation in sugars, aldol/retro-aldol in glycolysis, imine formation in transamination, amide bonds in proteins

Master the "why" behind each reaction, not just the "what." The MCAT rewards mechanistic reasoning over memorization.
