# Lab Techniques — MCAT Deep-Dive Study Guide

These show up constantly in passage-based questions on both BB and CP. The MCAT does not just ask "what is gel electrophoresis" — it gives you an experimental passage and expects you to interpret results, predict what would happen if a step changed, or pick the right technique for a given goal. You need to understand the **mechanism**, not just the name.

---

## 1. Separation and Purification Techniques

### SDS-PAGE (Sodium Dodecyl Sulfate — Polyacrylamide Gel Electrophoresis)

**What it does:** Separates proteins by **molecular weight only**.

**How it works:**
- **SDS** is an anionic detergent that **denatures** proteins and coats them with a uniform negative charge. The binding ratio is approximately **1 SDS molecule per 2 amino acid residues**. This overwhelms any intrinsic charge the protein had — so charge differences between proteins no longer matter.
- Because every protein now has the same charge-to-mass ratio, the only thing that determines how fast it moves through the gel is **size**. The polyacrylamide gel acts as a molecular sieve.
- **Reducing agents** like **beta-mercaptoethanol (BME)** or **dithiothreitol (DTT)** are added to break **disulfide bonds**. Without these, a multi-subunit protein held together by disulfide bonds would migrate as one large complex instead of individual subunits.
- Proteins migrate toward the **positive electrode (anode)** because SDS gives them all a net negative charge.
- **Smaller proteins migrate farther** down the gel. Larger proteins get stuck earlier in the gel matrix.

**How to interpret results:**
- A **molecular weight standards ladder** (proteins of known MW) is run alongside your sample. You compare how far your unknown band migrated relative to the standards.
- **Staining:** Coomassie Brilliant Blue (standard sensitivity) or silver stain (10-100x more sensitive, detects ng quantities).
- Band thickness/intensity is proportional to the amount of protein present.

**MCAT traps:**
- If a question says "non-reducing SDS-PAGE," disulfide bonds are intact — you will see a larger band for a multi-subunit protein held by S-S bonds.
- SDS-PAGE tells you nothing about function, charge, or quaternary structure (it is denatured).

---

### Native PAGE

**What it does:** Separates proteins by **charge, size, AND shape** — without denaturing them.

**How it works:**
- No SDS, no reducing agents. The protein keeps its native conformation and biological activity.
- Migration depends on the protein's **net charge at the running buffer pH**, its **size**, and its **shape** (compact vs. elongated).
- A globular protein and a fibrous protein of the same MW will migrate differently.

**When to use it:**
- When you need to preserve **biological activity** (e.g., testing if an enzyme is still active after purification).
- When studying **protein complexes** — since nothing is denatured, intact complexes migrate together.
- When you want to see **charge variants** (e.g., different phosphorylation states of the same protein).

**Key contrast with SDS-PAGE:** SDS-PAGE = MW only. Native PAGE = charge + size + shape. If the MCAT asks "which technique separates proteins while preserving their biological activity," it is native PAGE.

---

### Isoelectric Focusing (IEF)

**What it does:** Separates proteins by their **isoelectric point (pI)**.

**How it works:**
- A gel with an **immobilized pH gradient** is set up (acidic end to basic end).
- An electric field is applied. A protein placed in this system migrates until it reaches the pH where its **net charge = 0** — that is its pI. At that point, it stops moving.
- **If pH < pI:** the protein has a net **positive** charge (protonated), so it migrates toward the **cathode (negative electrode)**.
- **If pH > pI:** the protein has a net **negative** charge (deprotonated), so it migrates toward the **anode (positive electrode)**.
- The protein effectively "focuses" into a tight band at its pI.

**MCAT applications:**
- Determining the pI of an unknown protein.
- Distinguishing proteins that have identical MW but different pI values (e.g., post-translational modifications like phosphorylation lower pI).
- First dimension of 2D gel electrophoresis.

**Key concept to internalize:** pI is the pH at which the protein has zero net charge and will not migrate in an electric field. This principle also applies to amino acid behavior at different pH values — a concept the MCAT loves.

---

### 2D Gel Electrophoresis

**What it does:** Resolves **thousands of proteins** simultaneously in a complex mixture.

**How it works:**
1. **First dimension = IEF** — separates proteins by pI (horizontal axis).
2. The IEF strip is then laid on top of an SDS-PAGE gel.
3. **Second dimension = SDS-PAGE** — separates by MW (vertical axis).
4. Result: each protein occupies a unique spot defined by its pI (x) and MW (y).

**When to use it:**
- Comparing protein expression between two samples (e.g., diseased vs. healthy tissue). You overlay the two 2D gels and look for spots present in one but not the other.
- Proteomics research — identifying all proteins in a cell lysate.

**MCAT note:** If a passage describes separating a complex protein mixture and asks how to identify individual proteins, 2D gel electrophoresis followed by mass spectrometry is the classic workflow.

---

### Agarose Gel Electrophoresis

**What it does:** Separates **DNA and RNA** fragments by size.

**How it works:**
- DNA and RNA have a **negatively charged phosphate backbone** — they ALWAYS migrate toward the **positive electrode (anode)**. No SDS needed.
- Agarose forms a porous matrix. **Smaller fragments migrate farther** (same logic as SDS-PAGE).
- Larger pore size than polyacrylamide — suited for nucleic acids and large DNA fragments (100 bp to ~50 kb).
- **Visualization:** Ethidium bromide (intercalates into DNA, fluoresces under UV — this is a mutagen, handle carefully) or **SYBR Green/SYBR Safe** (less toxic alternatives).
- **Size estimation:** Run a **DNA ladder** (fragments of known size) alongside your sample.

**Applications on the MCAT:**
- Verifying PCR product size.
- Analyzing restriction enzyme digestion products.
- Confirming successful cloning (insert present or not).

**Key detail:** Supercoiled DNA migrates faster than linear DNA of the same size because of its compact shape. If you see multiple bands from a plasmid prep, this is why.

---

### Size-Exclusion Chromatography (Gel Filtration)

**What it does:** Separates molecules by **size (hydrodynamic radius)**.

**How it works:**
- Column is packed with **porous beads** (cross-linked polymers like Sephadex).
- **Large molecules CANNOT enter the pores** — they are excluded, travel through the void volume between beads, and **elute FIRST**.
- **Small molecules ENTER the pores**, travel a longer tortuous path through the bead interior, and **elute LATER**.

**MCAT trap — this is the big one:** Students instinctively think bigger = slower. In size-exclusion chromatography, it is the **opposite**. Big comes out first. Memorize this.

**Applications:**
- **Desalting/buffer exchange:** Protein (large) elutes first, salt (small) elutes later — cleanly separated.
- **Native MW estimation:** Compare elution volume of unknown protein to standards of known MW. (Note: this estimates native MW, so it can detect quaternary structure — a dimer elutes earlier than a monomer.)
- Separating protein from small-molecule contaminants.

**No binding involved** — this is purely a sieving mechanism based on physical size.

---

### Ion-Exchange Chromatography

**What it does:** Separates proteins by **net charge**.

**How it works:**
- **Cation exchanger (e.g., CM-cellulose):** Beads are **negatively charged**. They bind **positively charged proteins** (cations).
- **Anion exchanger (e.g., DEAE-cellulose):** Beads are **positively charged**. They bind **negatively charged proteins** (anions).
- **Elution:** Increase **salt concentration** gradually (NaCl gradient). Salt ions compete with the protein for binding sites on the beads. Weakly bound proteins elute first; tightly bound proteins elute at higher salt.
- Alternatively, change the **pH** to alter the protein's charge and release it.

**Connecting to pI:**
- At **pH below the protein's pI**, the protein carries a net positive charge — it binds to a cation exchanger.
- At **pH above the protein's pI**, the protein carries a net negative charge — it binds to an anion exchanger.
- At **pH = pI**, the protein has zero net charge and will not bind to either exchanger.

**MCAT-style reasoning:** "A protein has a pI of 6.5. At pH 8.0, which type of ion-exchange column would you use to bind it?" Answer: At pH 8.0 > pI 6.5, the protein is negatively charged, so use an **anion exchanger** (positive beads bind negative protein).

---

### Affinity Chromatography

**What it does:** Purifies a **specific target protein** based on its biological binding properties.

**How it works:**
- A **ligand** is covalently attached to the column beads. This ligand specifically binds your target protein.
  - Examples: antibody on beads to capture antigen; Ni-NTA beads to capture **His-tagged** recombinant proteins; substrate analog to capture an enzyme.
- Pour your cell lysate through the column. **Target protein binds; everything else flows through.**
- Wash to remove nonspecific binders.
- **Elute** the target with a competing ligand (e.g., excess imidazole for His-tag), low pH, or high salt.

**Why it matters:** Affinity chromatography provides the **highest purity in a single step** of any chromatographic technique. If the MCAT asks "which technique gives the most specific purification," this is the answer.

**His-tag system (very common in MCAT passages):**
- A string of 6+ histidine residues is genetically fused to the protein of interest.
- His-tag binds Ni2+ ions on the column.
- Elute with imidazole (structurally similar to histidine side chain, competes for Ni2+ binding).

---

### Thin-Layer Chromatography (TLC)

**What it does:** Quick, cheap method to monitor reaction progress or identify compounds.

**How it works:**
- **Stationary phase:** Silica gel on a glass/plastic plate — this is **polar**.
- A small spot of sample is placed near the bottom of the plate.
- The plate is placed in a developing chamber with a shallow layer of solvent (**mobile phase** — typically less polar than silica).
- Solvent travels up by capillary action, carrying compounds with it.

**Rf value = distance traveled by compound / distance traveled by solvent front**

**Key principle:**
- In **normal-phase TLC** (silica = polar stationary phase): **Less polar compounds have higher Rf** (they spend more time in the nonpolar mobile phase and travel farther). **More polar compounds have lower Rf** (they interact with the polar silica and stay behind).
- In **reversed-phase TLC** (nonpolar stationary phase, polar mobile phase): The opposite — more polar compounds travel farther.

**MCAT application:** A passage shows a TLC plate with spots at different Rf values and asks you to identify which compound is most polar (lowest Rf in normal phase) or to determine if a reaction went to completion (disappearance of starting material spot, appearance of product spot).

---

### Column Chromatography / HPLC / Gas Chromatography

**Column chromatography:** Gravity-driven, bulk preparative technique. Same principles as TLC but in column format. Used for large-scale purification. Lower resolution than HPLC.

**HPLC (High-Performance Liquid Chromatography):**
- Uses **high pressure** to push solvent through a tightly packed column.
- Much higher resolution than gravity-fed column chromatography.
- Primarily an **analytical** technique (can be preparative, but MCAT treats it as analytical).
- Common in MCAT passages: "the sample was analyzed by HPLC and the following chromatogram was obtained" — peaks represent different compounds, retention time reflects interactions with stationary phase.

**Gas Chromatography (GC):**
- Sample must be **volatile** (or made volatile by derivatization).
- Sample is vaporized and carried through a column by an inert carrier gas.
- Separation depends on **boiling point** and **polarity**.
- Often coupled with mass spectrometry (**GC-MS**) for compound identification.

---

### Centrifugation

**Differential Centrifugation:**
- Sequential spins at **increasing speed** to pellet progressively smaller organelles.
- **Low speed (~1,000g):** Pellets **nuclei, whole cells, cell debris**.
- **Medium speed (~10,000g):** Pellets **mitochondria, lysosomes, peroxisomes**.
- **High speed (~100,000g):** Pellets **microsomes (ER fragments), ribosomes**.
- **Very high speed (~300,000g):** Pellets **ribosomes, large macromolecules**.
- Supernatant at each step contains everything smaller than what pelleted.

**Density Gradient Ultracentrifugation:**
- **CsCl gradient** or **sucrose gradient** is pre-formed in the tube.
- Sample is layered on top (or mixed in for CsCl).
- Components migrate to the position in the gradient that matches their **buoyant density** and form bands.
- Used in the classic **Meselson-Stahl experiment** (15N vs. 14N DNA separated by density).

**MCAT note:** If a passage describes isolating mitochondria, they are using differential centrifugation at ~10,000g. If they are separating DNA species by density, it is CsCl gradient ultracentrifugation.

---

### Other Purification Techniques (Brief Coverage)

**Distillation:**
- Separates liquids by **boiling point differences**. Heat mixture, lower-BP component vaporizes first, condense the vapor to collect it.
- **Simple distillation:** For liquids with BP differences > 25 degrees C.
- **Fractional distillation:** For liquids with closer BPs; uses a fractionating column for multiple vaporization-condensation cycles.

**Liquid-Liquid Extraction:**
- Uses two **immiscible solvents** (e.g., water and dichloromethane). Compounds partition between layers based on solubility ("like dissolves like").
- Separatory funnel technique. Denser solvent on bottom.
- Adjust pH to change ionization state and shift compounds between layers (e.g., deprotonate an organic acid to make it water-soluble).

**Recrystallization:**
- Dissolve impure solid in hot solvent, then cool slowly. Target compound crystallizes out as it becomes less soluble at lower temperature. Impurities remain in solution (because they are present in smaller amounts and do not reach their saturation point).

**Filtration:**
- **Gravity filtration:** Slow, removes insoluble impurities from a solution.
- **Vacuum filtration (Buchner funnel):** Faster, collects a solid precipitate/crystal from a solution.

**Dialysis:**
- Uses a **semipermeable membrane** with a defined molecular weight cutoff.
- Small molecules (salts, small metabolites) pass through the membrane; large molecules (proteins) are retained.
- Used for buffer exchange and removing small-molecule contaminants from protein solutions.
- Same principle as kidney dialysis — small waste products cross the membrane, proteins and blood cells stay.

---

## 2. Molecular Biology Techniques

### PCR (Polymerase Chain Reaction)

**What it does:** Amplifies a specific DNA region millions of times.

**Three steps per cycle:**
1. **Denature (94-95 degrees C):** Double-stranded DNA melts into single strands.
2. **Anneal (55-65 degrees C):** Short **primers** (15-30 nt) bind to complementary sequences flanking the target region. Primers define WHAT gets amplified.
3. **Extend (72 degrees C):** **Taq polymerase** (from *Thermus aquaticus*, a thermophilic bacterium) synthesizes new DNA starting from the primers, adding dNTPs in the 5' to 3' direction.

**After n cycles: 2^n copies.** 20 cycles = ~1 million copies. 30 cycles = ~1 billion.

**Requirements:** Template DNA, two primers (forward and reverse), Taq polymerase, dNTPs (dATP, dTTP, dCTP, dGTP), Mg2+ (cofactor for Taq), buffer.

**Why Taq polymerase?** It survives the 95 degrees C denaturation step because it evolved in hot springs. Regular DNA polymerase would be destroyed.

**MCAT note:** Taq has **no proofreading ability** (no 3' to 5' exonuclease activity), so PCR introduces errors at a low rate. High-fidelity polymerases (e.g., Pfu) are used when accuracy is critical.

---

### RT-PCR (Reverse Transcriptase PCR)

**What it does:** Detects gene **expression** — whether a gene is being transcribed into mRNA.

**How it works:**
1. Extract **mRNA** from cells.
2. **Reverse transcriptase** converts mRNA into **complementary DNA (cDNA)**.
3. Use cDNA as template for standard **PCR amplification**.

**Critical MCAT distinction:**
- **RT-PCR** = Reverse Transcriptase PCR. Measures whether mRNA is present.
- **qPCR** = quantitative PCR (also called real-time PCR). Measures HOW MUCH.
- **RT-qPCR** = both combined. Convert mRNA to cDNA, then quantify by real-time PCR. This is the gold standard for measuring gene expression levels.

**Why cDNA and not genomic DNA?**
- cDNA lacks **introns** (mRNA was already spliced). This is why cDNA libraries represent only **expressed genes**.
- If you PCR from genomic DNA, you detect the gene whether or not it is expressed. RT-PCR specifically tells you about transcription.

---

### qPCR (Quantitative / Real-Time PCR)

**What it does:** Quantifies the amount of a specific DNA (or cDNA) sequence in real time as amplification occurs.

**How it works:**
- Uses **fluorescent reporters** that increase signal proportionally to the amount of PCR product.
  - **SYBR Green:** Binds any double-stranded DNA, fluoresces. Cheap but nonspecific (detects primer dimers too).
  - **TaqMan probes:** Sequence-specific fluorescent probe. More specific and more expensive.
- A fluorescence threshold is set. The cycle number at which the fluorescence crosses this threshold = **Ct (threshold cycle)**.

**Interpreting Ct values:**
- **Lower Ct = more starting template.** The sample had so much DNA/cDNA that it reached the threshold quickly.
- **Higher Ct = less starting template.** Took more cycles to produce enough product.
- A Ct difference of ~3.3 corresponds to approximately a **10-fold difference** in starting template (because 2^3.3 is approximately 10).

**MCAT application:** "Gene X has a Ct of 18 in tissue A and a Ct of 24 in tissue B. Which tissue expresses more of gene X?" Tissue A — lower Ct means more starting mRNA (via cDNA).

---

### Blotting Techniques — SNoW DRoP

This mnemonic is non-negotiable for the MCAT:

| Technique | Target Molecule | Probe/Detection |
|-----------|----------------|-----------------|
| **S**outhern blot | **D**NA | Labeled DNA/RNA probe |
| **N**orthern blot | **R**NA | Labeled DNA/RNA probe |
| **W**estern blot | **P**rotein | Labeled antibody |

**General workflow (Southern and Northern):**
1. **Separate** by gel electrophoresis (agarose for DNA/RNA).
2. **Transfer** to a membrane (nitrocellulose or PVDF) — this is the "blotting" step.
3. **Probe** with a labeled complementary nucleic acid sequence. The probe hybridizes to its target.
4. **Detect** — autoradiography (if radioactive label) or chemiluminescence/fluorescence.

**Western blot specifics:**
1. Separate proteins by **SDS-PAGE**.
2. Transfer to membrane.
3. Block membrane (with milk proteins or BSA to prevent nonspecific antibody binding).
4. Incubate with **primary antibody** (specific to target protein).
5. Incubate with **secondary antibody** (binds the primary; conjugated to enzyme like HRP or alkaline phosphatase).
6. Add substrate — enzyme produces detectable signal (color or light).

**MCAT scenarios:**
- "Researchers wanted to determine if gene X is present in the genome" = Southern blot.
- "Researchers measured mRNA levels of gene X" = Northern blot (or RT-qPCR).
- "Researchers detected protein X in cell lysate" = Western blot.

---

### ELISA (Enzyme-Linked Immunosorbent Assay)

**What it does:** Detects and **quantifies** a specific protein (antigen) or antibody in a sample using antibody-antigen interactions and an enzyme-mediated color change.

**Three main formats:**

**Direct ELISA:**
1. Coat plate with **antigen**.
2. Add **enzyme-labeled primary antibody** that binds the antigen.
3. Add substrate — color change proportional to antigen amount.

**Indirect ELISA:**
1. Coat plate with **antigen**.
2. Add **unlabeled primary antibody**.
3. Add **enzyme-labeled secondary antibody** (binds the primary).
4. Add substrate — detect.
- Advantage: signal amplification (multiple secondary Abs bind each primary).

**Sandwich ELISA (most specific and common on MCAT):**
1. Coat plate with **capture antibody**.
2. Add sample — **antigen binds** to capture antibody.
3. Add **enzyme-labeled detection antibody** (binds a different epitope on the antigen).
4. Add substrate — detect.
- Most specific because the antigen must be recognized by TWO different antibodies.

**MCAT note:** Pregnancy tests and HIV antibody tests are based on ELISA principles. If a question describes a plate-based assay with antibodies and color change, it is ELISA.

---

### Sanger Sequencing (Chain Termination Method)

**What it does:** Determines the **nucleotide sequence** of a DNA fragment.

**How it works:**
- Reaction contains: template DNA, primer, DNA polymerase, normal dNTPs, and a small amount of **ddNTPs (dideoxynucleotides)**.
- **ddNTPs lack the 3'-OH group** needed to form the next phosphodiester bond. When a ddNTP is incorporated, the chain **terminates**.
- Because ddNTPs are present at low concentration, termination occurs randomly at every position, generating fragments of every possible length.
- Each of the four ddNTPs (ddATP, ddTTP, ddCTP, ddGTP) is labeled with a **different fluorescent dye**.
- Fragments are separated by **capillary electrophoresis** (by size, single-nucleotide resolution).
- A laser reads the fluorescent color of each fragment as it passes the detector. The sequence is read from **shortest to longest fragment**.

**MCAT trap:** Know the difference between dNTPs (normal, chain continues) and ddNTPs (no 3'-OH, chain terminates). The MCAT may show you the chemical structure and ask why it causes termination.

---

### CRISPR-Cas9

**What it does:** Precise **gene editing** — can knock out, insert, or modify specific genes.

**How it works:**
1. A **guide RNA (gRNA)** is designed to be complementary to the target DNA sequence (~20 nt).
2. The gRNA associates with the **Cas9 nuclease** and directs it to the target site.
3. Cas9 makes a **double-strand break (DSB)** at the target location.
4. The cell repairs the break by one of two pathways:
   - **NHEJ (Non-Homologous End Joining):** Error-prone, often introduces insertions or deletions (indels) that disrupt the gene. Used for **gene knockout**.
   - **HDR (Homology-Directed Repair):** If a donor DNA template is provided, the cell uses it to make a precise edit. Used for **gene correction or insertion**.

**MCAT relevance:**
- CRISPR is now the standard answer to "how would you edit a specific gene."
- Understand that specificity comes from the gRNA sequence — change the gRNA, target a different gene.
- Off-target effects occur when the gRNA has partial complementarity to other genomic locations.

---

### Other Key Molecular Biology Techniques

**Restriction Enzymes:**
- Bacterial enzymes that cut DNA at specific **palindromic recognition sequences** (4-8 bp).
- **Sticky ends:** Staggered cuts leaving single-stranded overhangs. Easier to ligate because complementary overhangs can base-pair.
- **Blunt ends:** Straight cuts with no overhang. Harder to ligate (no complementary pairing to hold pieces together).
- Used in **gene cloning**, restriction mapping, and Southern blotting.

**Gene Cloning Workflow:**
1. Cut target gene and vector (plasmid) with the **same restriction enzyme**.
2. Mix — sticky ends anneal.
3. **DNA ligase** seals the phosphodiester backbone.
4. **Transform** into bacteria (heat shock or electroporation).
5. Select for transformants (antibiotic resistance on plasmid).
6. Screen for insert (blue-white screening, colony PCR).

**Microarrays (DNA/Gene Chips):**
- Thousands of known DNA sequences (probes) spotted on a chip.
- Fluorescently labeled cDNA from a sample hybridizes to complementary probes.
- Measures **expression levels of thousands of genes simultaneously**.
- Compare two conditions: one labeled green, one red. Yellow spots = equal expression; green or red = differential expression.

**Flow Cytometry / FACS:**
- Cells pass single-file through a laser beam.
- **Flow cytometry** measures properties: size (forward scatter), granularity (side scatter), fluorescence (from labeled antibodies or fluorescent proteins).
- **FACS (Fluorescence-Activated Cell Sorting):** Sorts cells into separate populations based on fluorescent markers. Physical separation of cell types.

**Immunoprecipitation (IP) and Co-IP:**
- **IP:** Use an antibody attached to beads to "pull down" a specific protein from cell lysate.
- **Co-IP:** Pull down your target protein AND any proteins physically associated with it. Used to identify **protein-protein interactions**.
- MCAT scenario: "To determine if protein A interacts with protein B, researchers performed co-immunoprecipitation..."

**ChIP (Chromatin Immunoprecipitation):**
- Cross-link proteins to DNA (formaldehyde), shear chromatin, immunoprecipitate with antibody to protein of interest, reverse cross-links, analyze the bound DNA.
- Identifies **which DNA sequences a protein (e.g., transcription factor, histone) binds to**.
- ChIP-seq = ChIP followed by sequencing.

**FISH (Fluorescence In Situ Hybridization):**
- Fluorescently labeled DNA or RNA probes hybridize to complementary sequences on **chromosomes or in cells**.
- Visualize where a gene is located on a chromosome.
- Detect chromosomal abnormalities (deletions, translocations, duplications).
- Can be done on metaphase spreads or interphase nuclei.

**Edman Degradation:**
- Sequentially removes and identifies amino acids from the **N-terminus** of a protein, one at a time.
- Alternative to mass spectrometry for protein sequencing.
- Limited to ~50 residues from the N-terminus.

**Bradford Assay:**
- Measures **total protein concentration** in a solution.
- Uses Coomassie dye that shifts absorbance from 465 nm to **595 nm** when bound to protein.
- Quick, cheap, standard lab technique. Compare to a standard curve of known protein concentrations (usually BSA).

**Karyotyping:**
- Arrests cells in **metaphase** (using colchicine to disrupt spindle formation), stains chromosomes, and photographs them.
- Chromosomes are arranged by size and banding pattern.
- Detects **aneuploidy** (trisomy 21, monosomy X), large deletions, translocations.

**Radioactive Labeling:**
- Incorporate radioactive isotopes (32P, 35S, 3H, 14C) into molecules to track them.
- **32P** labels DNA/RNA (phosphate backbone).
- **35S** labels proteins (methionine and cysteine contain sulfur).
- Detected by autoradiography or scintillation counting.

**X-Ray Crystallography:**
- Determines 3D structure of proteins and other molecules at **atomic resolution**.
- Requires growing a crystal of the purified protein, then bombarding it with X-rays.
- Diffraction pattern is mathematically converted to an electron density map, then a 3D model.
- Most protein structures in the PDB were solved by this method.

---

## 3. Spectroscopy Quick Reference

This is covered in more depth in CP Spectroscopy. Here is the essential summary table:

| Technique | What It Measures | Key Information Obtained |
|-----------|-----------------|------------------------|
| **IR (Infrared)** | Bond vibrations (stretching/bending) | Identifies **functional groups**. Look for: broad O-H (~3200-3600), sharp C=O (~1700), N-H (~3300). |
| **1H NMR** | Hydrogen nuclei in magnetic field | Number of **unique H environments** (# of peaks), number of H per environment (integration), neighboring H (splitting: n+1 rule), chemical shift (electronegativity of nearby groups). |
| **13C NMR** | Carbon nuclei in magnetic field | Number of **unique C environments**. No splitting in decoupled spectra. Fewer peaks than 1H NMR. |
| **Mass Spectrometry (MS)** | Mass-to-charge ratio (m/z) | **Molecular weight** of compound (molecular ion peak, M+). Fragmentation pattern helps identify structure. |
| **UV-Vis** | Electronic transitions (pi to pi*, n to pi*) | **Conjugation** (more conjugation = longer wavelength absorption). **Concentration** via Beer-Lambert: A = epsilon * l * c. |

**MCAT priorities:** Know what each technique tells you, not the detailed physics. If a passage shows a spectrum, you need to identify the technique and extract the relevant information.

---

## 4. Decision Guide: "Which Technique Would You Use To...?"

This is the single most testable concept pattern in lab techniques. Memorize these associations:

| Goal | Technique | Why |
|------|-----------|-----|
| Determine **protein molecular weight** | SDS-PAGE | Separates denatured proteins by MW only |
| Determine **protein pI** | Isoelectric focusing (IEF) | Protein migrates to its pI and stops |
| Separate proteins by charge, size, and shape (native) | Native PAGE | No denaturation, preserves all properties |
| Resolve a complex protein mixture by both pI and MW | 2D gel electrophoresis | IEF (1st) + SDS-PAGE (2nd) |
| Separate DNA fragments by size | Agarose gel electrophoresis | Standard for nucleic acids |
| Detect a **specific DNA sequence** in a genome | Southern blot | Gel + membrane + labeled DNA probe |
| Detect a **specific RNA** (measure transcription) | Northern blot | Gel + membrane + labeled probe |
| Detect a **specific protein** in a cell lysate | Western blot | SDS-PAGE + membrane + antibody |
| **Quantify** gene expression (mRNA levels) | RT-qPCR | Most sensitive and quantitative method |
| **Quantify** a specific protein in solution | ELISA (sandwich) | Antibody-based, plate assay, enzyme readout |
| Measure **total protein concentration** | Bradford assay | Coomassie dye binding at 595 nm |
| **Amplify** a specific DNA region | PCR | Exponential amplification (2^n) |
| **Sequence** DNA | Sanger sequencing | ddNTP chain termination |
| **Edit** a gene | CRISPR-Cas9 | Guide RNA + Cas9 nuclease |
| Purify a **specific protein** (highest purity) | Affinity chromatography | Ligand-specific binding, single-step |
| Separate proteins by **size** in native conditions | Size-exclusion chromatography | Large elutes first, no denaturation |
| Separate proteins by **charge** | Ion-exchange chromatography | Charge-based binding, salt gradient elution |
| Identify **protein-protein interactions** | Co-immunoprecipitation (Co-IP) | Pull down complex with antibody |
| Identify **DNA-protein interactions** | ChIP (Chromatin IP) | Cross-link, IP, identify bound DNA |
| Visualize a **gene's location on a chromosome** | FISH | Fluorescent probe hybridizes to chromosome |
| Profile **expression of thousands of genes** | Microarray (DNA chip) | Genome-wide expression snapshot |
| **Sort live cells** by surface markers | FACS | Fluorescent antibodies + cell sorting |
| Determine **3D protein structure** | X-ray crystallography | Atomic resolution |
| Detect **chromosomal abnormalities** | Karyotyping | Metaphase chromosome spread |
| Separate **cell organelles** | Differential centrifugation | Sequential spins at increasing g-force |
| Separate molecules by **density** | Density gradient ultracentrifugation | CsCl or sucrose gradient |
| Remove small molecules from protein solution | Dialysis or size-exclusion | Membrane cutoff or pore-based separation |
| Monitor **reaction progress** (organic chemistry) | TLC | Quick, visual Rf comparison |
| Identify **functional groups** | IR spectroscopy | Characteristic absorption frequencies |
| Determine **molecular weight** of small molecule | Mass spectrometry | M+ peak gives MW |

---

## High-Yield Connections Across Topics

**Electrophoresis and charge behavior** — The same amino acid acid-base chemistry that governs pI/pKa problems governs protein behavior in IEF and ion-exchange chromatography. If you understand Henderson-Hasselbalch, you understand why a protein is positive below its pI and negative above it. This is one concept tested in at least three different guises.

**Gene expression analysis hierarchy:**
- Is the gene in the genome? **Southern blot** or **PCR on genomic DNA**.
- Is the gene being transcribed? **Northern blot** or **RT-PCR**.
- How much mRNA? **RT-qPCR** (quantitative).
- Is the protein being made? **Western blot** or **ELISA**.
- Where is the protein in the cell? **Immunofluorescence microscopy**.
- Is the protein active? **Native PAGE** + activity assay, or functional assay.

**Passage strategy:** When you see a lab technique in a passage, immediately ask yourself three questions:
1. What molecule is being studied (DNA, RNA, protein, small molecule)?
2. What property is being measured (size, charge, sequence, quantity, location, interaction)?
3. What is the expected result if the hypothesis is correct vs. incorrect?

These three questions will get you through nearly every technique-based passage on the MCAT.
