# FC2B: Prokaryotes and Viruses -- Deep Dive

**Section:** Bio/Biochem (BB)
**Yield:** HIGH -- Expect 3-5 discrete questions plus integration into passage-based Qs
**Connections:** Antibiotics (CP/BB), immune response (BB), genetics/central dogma (BB), experimental design (passages using phage or bacteria)

---

## 1. Prokaryotic Cell Structure

### Cell Wall and Gram Staining

The **cell wall** is the defining structural feature that separates prokaryotic taxonomy on the MCAT. It is made of **peptidoglycan** (also called murein) -- a polymer of alternating **NAG** (N-acetylglucosamine) and **NAM** (N-acetylmuramic acid) sugars cross-linked by short peptide bridges. This mesh-like structure gives the cell mechanical strength against osmotic lysis.

**Gram-positive bacteria:**
- **Thick peptidoglycan layer** (20-80 nm), sitting outside the plasma membrane
- Contains **teichoic acids** embedded in the wall (important for adhesion and antigenicity)
- When hit with **crystal violet** stain followed by iodine, the dye-iodine complex gets trapped in the thick mesh
- After alcohol wash, the dye stays -- cell stains **purple/violet**
- Single membrane (just the plasma membrane)

**Gram-negative bacteria:**
- **Thin peptidoglycan layer** (5-10 nm) sandwiched between two membranes
- Has an **outer membrane** containing **lipopolysaccharide (LPS)**
- LPS has three components: Lipid A (the endotoxin -- triggers septic shock/fever), core polysaccharide, and O-antigen (variable, used for serotyping)
- The space between inner and outer membranes = **periplasmic space** (contains enzymes, including beta-lactamases that degrade penicillin)
- Crystal violet washes out during alcohol decolorization because the thin wall cannot retain the complex
- Takes up **safranin** counterstain -- cell appears **pink/red**

**Clinical significance for the MCAT:** Gram staining is the fastest way to narrow down a bacterial infection. Gram-negative infections tend to be harder to treat because (1) the outer membrane acts as a permeability barrier blocking many antibiotics, (2) beta-lactamases in the periplasm degrade penicillins, and (3) LPS release during bacterial death can trigger endotoxic shock. When a passage describes "endotoxin," think Gram-negative outer membrane.

**Lysozyme** -- found in tears, saliva, and nasal secretions -- cleaves the bond between NAG and NAM, destroying peptidoglycan. This is a first-line innate immune defense. MCAT loves testing this as a connection between biochemistry (enzyme specificity) and immunology.

### Ribosomes: 70S vs 80S

Prokaryotic ribosomes are **70S**, composed of a **30S small subunit** and a **50S large subunit**. Eukaryotic ribosomes are **80S** (40S + 60S). The "S" stands for **Svedberg units** -- a measure of sedimentation rate during centrifugation, not molecular weight (they do not add linearly because sedimentation depends on shape and density).

This structural difference is clinically critical because many antibiotics selectively target 70S ribosomes without affecting 80S, making them toxic to bacteria but relatively safe for human cells:

| Antibiotic | Target | Mechanism |
|-----------|--------|-----------|
| **Aminoglycosides** (gentamicin, streptomycin) | 30S subunit | Cause mRNA misreading, block initiation |
| **Tetracyclines** | 30S subunit | Block aminoacyl-tRNA from binding A site |
| **Chloramphenicol** | 50S subunit | Blocks peptidyl transferase (peptide bond formation) |
| **Macrolides** (erythromycin) | 50S subunit | Block translocation |
| **Linezolid** | 50S subunit | Blocks formation of initiation complex |

**MCAT trap:** Mitochondria and chloroplasts also have 70S ribosomes (endosymbiotic theory). This is why some antibiotics targeting 70S ribosomes can have side effects -- they can also affect mitochondrial protein synthesis. Chloramphenicol toxicity to bone marrow is partly due to this.

### Flagella, Pili, and Plasmids

**Flagella** are long, whip-like protein structures made of **flagellin** (not tubulin -- that is eukaryotic). They provide **motility** through rotation driven by a proton motive force (H+ gradient across the membrane powers the basal body motor). Prokaryotic flagella rotate like a propeller; eukaryotic flagella/cilia undulate in a wave-like motion (powered by dynein + ATP).

**Chemotaxis** is the movement toward (attractant) or away from (repellent) chemical signals. Bacteria alternate between "runs" (straight swimming) and "tumbles" (random reorientation). When moving toward an attractant, tumble frequency decreases -- the bacterium runs longer in the favorable direction. This is a signal transduction pathway involving **methylation** of chemoreceptors.

**Pili (fimbriae):**
- **Common pili** -- short, hair-like surface projections for **attachment** to host cells and surfaces. Critical for colonization and pathogenesis (e.g., uropathogenic E. coli uses pili to adhere to bladder epithelium).
- **Sex pilus (F-pilus)** -- longer, used in **conjugation** to transfer genetic material between bacteria. Only **F+ cells** (carrying the F plasmid) produce the sex pilus.

**Plasmids** are small, circular, extrachromosomal DNA molecules that replicate independently. They carry genes that are not essential for basic survival but confer advantages:
- **Antibiotic resistance genes** (R plasmids) -- the major driver of the antibiotic resistance crisis
- **Virulence factors** (toxins, adhesins)
- **Metabolic enzymes** (e.g., ability to degrade unusual carbon sources)

Plasmids can be transferred by conjugation, which is a huge deal for horizontal gene transfer and the rapid spread of resistance.

### Nucleoid Region

Prokaryotes have no membrane-bound nucleus. Their genome is a single, circular, double-stranded DNA molecule located in the **nucleoid region** -- a concentrated area of DNA in the cytoplasm. The DNA is supercoiled with the help of **DNA gyrase** (a type II topoisomerase) and **histone-like proteins** (HU proteins, not true histones like eukaryotes use).

**MCAT connection:** Fluoroquinolone antibiotics (ciprofloxacin) target **DNA gyrase**, preventing DNA replication. Also remember: the absence of a nuclear membrane means **transcription and translation are coupled** in prokaryotes -- ribosomes begin translating mRNA while it is still being transcribed. This is impossible in eukaryotes, where mRNA must be processed and exported from the nucleus first.

### Endospores

**Endospores** are dormant, highly resistant structures formed by certain Gram-positive bacteria (notably **Bacillus** and **Clostridium**) when environmental conditions become unfavorable (nutrient depletion, desiccation). They are NOT reproductive structures -- one cell makes one spore, which later germinates into one cell.

Properties of endospores:
- Extremely resistant to heat, UV radiation, desiccation, chemical disinfectants
- Contain **dipicolinic acid** (complexed with Ca2+) which stabilizes DNA
- Have a thick **cortex** of modified peptidoglycan and a tough **spore coat**
- Can remain viable for centuries

**Clinical significance:**
- **Clostridium botulinum** -- produces botulinum toxin (causes flaccid paralysis by blocking ACh release at NMJ). Spores survive improper canning.
- **Clostridium tetani** -- tetanus toxin (spastic paralysis by blocking inhibitory neurotransmitter release -- glycine/GABA)
- **Clostridium difficile** -- pseudomembranous colitis after antibiotic use (spores persist in hospital environments)
- **Bacillus anthracis** -- anthrax. Spores can be weaponized.
- Sterilization requires **autoclaving** (121 degrees C, 15 psi, 15 min) -- boiling at 100 degrees C is NOT sufficient to kill endospores.

### Biofilms

A **biofilm** is a structured community of bacteria enclosed in a self-produced **extracellular polymeric substance (EPS)** matrix -- essentially a slime layer of polysaccharides, proteins, and DNA. Bacteria in biofilms behave very differently from free-floating (planktonic) cells.

Key features:
- Bacteria communicate via **quorum sensing** -- small signaling molecules (autoinducers) accumulate as population density increases, triggering coordinated gene expression (including biofilm formation genes)
- Biofilms are **up to 1000x more resistant to antibiotics** than planktonic cells because: the EPS matrix physically blocks drug penetration, cells in the interior are metabolically dormant (antibiotics work best on actively dividing cells), and there are persister cells that tolerate antibiotics
- Clinically significant on medical devices: catheters, prosthetic joints, heart valves (endocarditis), dental plaque

---

## 2. Prokaryotic Reproduction and Genetic Transfer

### Binary Fission

Prokaryotes reproduce by **binary fission** -- a simple, asexual process:

1. DNA replication begins at the **origin of replication (oriC)** on the circular chromosome
2. The two copies are separated toward opposite poles (no mitotic spindle -- uses proteins like FtsZ that are structural analogs of tubulin)
3. The cell elongates
4. A **septum** (cross-wall) forms at midcell, dividing the cytoplasm
5. Two genetically identical daughter cells result

**Comparison to mitosis:** Binary fission is faster (E. coli divides every ~20 min under optimal conditions), does not involve a spindle apparatus, has no condensation of chromosomes, and produces two identical cells from one circular chromosome. There is no S/G2/M phase in the eukaryotic sense, though there are checkpoints. FtsZ ring formation at the division site is the prokaryotic equivalent of the contractile ring.

**Growth curve** (MCAT loves this):
1. **Lag phase** -- adapting to new medium, synthesizing enzymes, no increase in cell number
2. **Log (exponential) phase** -- rapid, constant-rate division; most susceptible to antibiotics here
3. **Stationary phase** -- nutrients depleting, waste accumulating; growth rate = death rate
4. **Death phase** -- cell death exceeds division

### Horizontal Gene Transfer

Prokaryotes do not undergo meiosis or sexual reproduction, but they have three mechanisms of **horizontal gene transfer** that increase genetic diversity. This is critical for adaptation and resistance evolution.

#### Transformation

**Transformation** is the uptake of free ("naked") DNA from the environment by a **competent** bacterium. The DNA typically comes from dead, lysed cells.

- Only certain species are naturally competent (e.g., Streptococcus pneumoniae, Haemophilus influenzae)
- Competence can be induced in the lab with CaCl2 treatment or electroporation (creating transient membrane pores)
- **Griffith's experiment (1928):** Heat-killed virulent (smooth, S) pneumococci + live avirulent (rough, R) pneumococci injected into mice --> mice died, and live S-type bacteria were recovered. The R cells had taken up DNA from the dead S cells, transforming them into virulent bacteria. This was the first demonstration that a "transforming principle" (later shown to be DNA by Avery, MacLeod, and McCarty) could alter heredity.

**MCAT connection:** Transformation is the basis for molecular cloning -- inserting plasmid DNA into competent bacteria in the lab.

#### Transduction

**Transduction** is the transfer of bacterial DNA from one cell to another via a **bacteriophage** (bacterial virus).

**Generalized transduction:**
- During the **lytic cycle**, the phage accidentally packages a random fragment of the host's chromosomal DNA into a phage head (instead of phage DNA)
- This defective phage particle infects a new bacterium and injects the bacterial DNA
- The new host can incorporate this DNA by homologous recombination
- **Any gene** can be transferred -- it is random

**Specialized transduction:**
- Occurs during the switch from the **lysogenic to lytic cycle**
- The prophage (integrated phage DNA) excises imprecisely, taking adjacent bacterial genes with it
- Only genes **near the prophage insertion site** are transferred
- When this phage infects a new cell, those specific bacterial genes come along

**Mnemonic:** Generalized = random Grab bag; Specialized = Specific genes near the Site.

#### Conjugation

**Conjugation** is the direct transfer of DNA between two bacterial cells through a **sex pilus** (a physical bridge). It requires cell-to-cell contact.

- **F+ cells** carry the **F (fertility) plasmid**, which encodes genes for the sex pilus and transfer machinery
- F+ cell extends sex pilus to an **F- cell** (no F plasmid), retracts it to bring cells together
- A single strand of the F plasmid is transferred; both cells synthesize the complementary strand
- Result: both cells are now F+ (the recipient has gained the F plasmid)

**Hfr (High frequency recombination) cells:**
- The F plasmid has **integrated into the bacterial chromosome**
- During conjugation, the Hfr cell begins transferring chromosomal DNA (starting from the integrated F factor origin of transfer)
- Transfer is rarely complete (the connection usually breaks before the entire chromosome is transferred)
- Result: recipient gets some chromosomal genes but usually NOT the complete F plasmid, so it remains F-
- Transferred genes can recombine into the recipient's chromosome

**MCAT loves asking:** Why does an Hfr x F- cross give recombinants but the F- cells usually stay F-? Because the trailing end of the F plasmid (the part that would complete F transfer) is transferred last and the bridge almost always breaks before that happens.

---

## 3. Viruses

### Structure and Classification

Viruses are **obligate intracellular parasites** -- they cannot reproduce outside a host cell. They lack ribosomes, metabolic machinery, and cannot generate their own ATP.

**Basic structure:**
- **Nucleic acid core** -- the genome. Can be DNA or RNA, single-stranded (ss) or double-stranded (ds), linear or circular, segmented or non-segmented
- **Capsid** -- protein coat made of repeating **capsomere** subunits. Symmetry is either **icosahedral** (20-sided, roughly spherical) or **helical** (rod-shaped, e.g., tobacco mosaic virus)
- **Envelope** (some viruses) -- lipid bilayer derived from the host cell membrane during budding. Contains viral glycoproteins for attachment. Enveloped viruses are **more susceptible to detergents and desiccation** (the lipid envelope is fragile). Naked (non-enveloped) viruses are tougher outside the body.

**Classification by genome type (Baltimore classification):**

| Class | Genome | Example | Notes |
|-------|--------|---------|-------|
| I | dsDNA | Herpes, Adenovirus, Pox | Most replicate in nucleus (except pox) |
| II | ssDNA | Parvovirus | |
| III | dsRNA | Rotavirus | Segmented genome |
| IV | (+) ssRNA | Poliovirus, Coronavirus, Hepatitis C | (+) sense = can directly serve as mRNA |
| V | (-) ssRNA | Influenza, Ebola, Rabies | (-) sense = must be converted to (+) by RNA-dependent RNA polymerase (must carry this enzyme) |
| VI | (+) ssRNA-RT | HIV (retrovirus) | Uses reverse transcriptase to make DNA |
| VII | dsDNA-RT | Hepatitis B | Reverse transcribes an RNA intermediate |

**Key MCAT distinction:** (+) sense RNA can be directly translated by ribosomes (it IS the mRNA). (-) sense RNA is complementary to mRNA and must first be transcribed by an RNA-dependent RNA polymerase that the virus brings along in the virion.

### Lytic Cycle

The **lytic cycle** is a productive infection that ends with destruction of the host cell:

1. **Attachment (adsorption)** -- viral surface proteins bind to specific receptors on the host cell. This determines **host range** and **tissue tropism** (HIV gp120 binds CD4 on T-helper cells; influenza hemagglutinin binds sialic acid on respiratory epithelium)
2. **Penetration (entry)** -- injection of nucleic acid (bacteriophages), endocytosis (animal viruses), or membrane fusion (enveloped viruses)
3. **Biosynthesis** -- the host cell's machinery is hijacked to replicate the viral genome and translate viral proteins. Early genes encode enzymes for genome replication; late genes encode structural proteins
4. **Assembly (maturation)** -- new viral particles are assembled in the cytoplasm or nucleus
5. **Release (lysis)** -- the host cell bursts open, releasing progeny virions. Bacteriophages use **lysozyme** to degrade the bacterial cell wall. Enveloped animal viruses may instead **bud** from the host membrane (not always lytic)

### Lysogenic Cycle

In the **lysogenic cycle**, the phage integrates its DNA into the host chromosome, becoming a **prophage**:

- The prophage is replicated passively every time the host cell divides
- The bacterium is now a **lysogen** and is immune to superinfection by the same phage type
- Prophage genes are mostly repressed by a **repressor protein** (lambda phage uses the cI repressor)
- **Lysogenic conversion:** the prophage can carry genes that alter the host phenotype, sometimes conferring virulence factors (e.g., the toxin genes in Corynebacterium diphtheriae and Clostridium botulinum are encoded by prophages)

**Trigger for lytic switch:** Environmental stress (UV radiation, chemical damage) activates the **SOS response**, which inactivates the repressor protein, de-repressing lytic genes. The prophage excises and enters the lytic cycle.

**MCAT reasoning point:** The lysogenic-to-lytic switch is an example of gene regulation. Passages may present data about repressor mutations or environmental conditions and ask you to predict whether the phage will remain integrated or enter lytic replication.

### Retroviruses

**Retroviruses** (Class VI) are unique because their RNA genome is converted to DNA:

1. (+) ssRNA genome enters the host cell
2. **Reverse transcriptase** (an RNA-dependent DNA polymerase, carried in the virion) synthesizes a DNA copy from the RNA template
3. Reverse transcriptase also has **RNase H** activity -- it degrades the RNA strand of the RNA-DNA hybrid
4. Reverse transcriptase then synthesizes the second DNA strand, producing dsDNA
5. **Integrase** (also carried by the virus) inserts the dsDNA into the host genome -- this integrated form is called a **provirus**
6. The provirus is transcribed by host RNA polymerase II, producing viral mRNA and new genomic RNA
7. Viral proteins are translated, assembled, and new virions bud from the cell

**HIV specifics:**
- gp120 binds **CD4** receptor; gp41 mediates membrane fusion
- Co-receptors: **CCR5** (macrophage-tropic) or **CXCR4** (T-cell-tropic)
- Targets CD4+ T-helper cells --> progressive immune destruction --> AIDS
- High mutation rate due to reverse transcriptase lacking proofreading (no 3' to 5' exonuclease activity) -- this is why drug resistance develops quickly and why combination therapy (HAART) is necessary

**Drug targets in retroviral lifecycle:**
- **NRTIs/NNRTIs** -- inhibit reverse transcriptase
- **Integrase inhibitors** -- block integration into host DNA
- **Protease inhibitors** -- block cleavage of polyprotein precursors into functional viral proteins
- **Fusion inhibitors** -- block gp41-mediated membrane fusion

### Why Viruses Are Not "Alive"

Viruses lack the properties of life:
- No metabolism (cannot generate ATP or synthesize proteins independently)
- No ribosomes
- Cannot reproduce independently -- require host cell machinery
- Do not maintain homeostasis
- However: they DO evolve (mutation, natural selection), they DO have genetic material, and they DO reproduce (with help)

The MCAT does not expect a definitive "alive or not alive" answer -- it expects you to reason about which properties of life they possess and which they lack.

### Bacteriophages and Transduction

Bacteriophages are viruses that specifically infect bacteria. They are the workhorses of molecular biology:
- **Phage display** -- library screening technique
- **Transduction** -- natural mechanism of horizontal gene transfer (see Section 2)
- T-even phages (T2, T4) are classic lytic phages (Hershey-Chase experiment used T2 phage with radiolabeled protein [35S] and DNA [32P] to prove DNA is the genetic material)
- **Lambda phage** is the classic temperate phage (can do lytic or lysogenic)

---

## 4. Prions

**Prions** are infectious agents that are pure protein -- they contain **no nucleic acid** whatsoever. This is what makes them conceptually radical: they challenge the central dogma's assumption that information flows from nucleic acid to protein.

**Mechanism:**
- Normal cellular prion protein = **PrPC** (C for cellular). It is a glycoprotein normally found on neuronal cell surfaces, predominantly alpha-helical in structure. Its exact function is debated (possibly involved in cell signaling, copper binding).
- Misfolded pathogenic form = **PrPSc** (Sc for scrapie). It has a high beta-sheet content, making it extremely stable and resistant to proteases, heat, UV, and standard sterilization.
- **PrPSc acts as a template**, inducing conformational change in normal PrPC molecules, converting them to PrPSc. This is autocatalytic -- one misfolded protein begets more misfolded protein.
- Accumulation of PrPSc forms **amyloid plaques** in brain tissue, causing **spongiform encephalopathy** (the brain develops sponge-like holes).

**Key prion diseases:**
- **Creutzfeldt-Jakob disease (CJD)** -- humans. Rapid dementia, myoclonus, death within a year. Can be sporadic, familial, or acquired (iatrogenic from contaminated surgical instruments or variant CJD from consuming BSE-infected beef).
- **Bovine spongiform encephalopathy (BSE / mad cow disease)** -- cattle
- **Scrapie** -- sheep and goats (the first identified prion disease)
- **Kuru** -- historically found in the Fore people of Papua New Guinea, transmitted through ritualistic cannibalism

**Why prions matter for the MCAT:**
- They are the only known infectious agent that is purely protein -- no DNA, no RNA
- They demonstrate that protein conformation (tertiary/quaternary structure) can be "infectious"
- They cannot be destroyed by autoclaving, UV, or formaldehyde (you need NaOH or bleach at high concentration, or incineration)
- MCAT may present a passage about a novel neurodegenerative disease and ask you to identify prion-like properties based on experimental data

---

## 5. Fungi Basics

Fungi are **eukaryotic** organisms (not prokaryotes, not plants, not animals). They are heterotrophs that obtain nutrients by **absorption** (secreting enzymes externally and absorbing digested products). The MCAT tests fungi primarily as a point of comparison.

### Cell Wall: Chitin

| Organism | Cell Wall Component |
|----------|-------------------|
| Bacteria | **Peptidoglycan** |
| Fungi | **Chitin** (polymer of N-acetylglucosamine) |
| Plants | **Cellulose** (polymer of glucose with beta-1,4 linkages) |
| Animals | **No cell wall** |

Chitin is also found in the exoskeletons of arthropods (insects, crustaceans). This is a classic comparison question.

### Membrane: Ergosterol

Fungal cell membranes contain **ergosterol** instead of the **cholesterol** found in animal cell membranes. Both are sterols that modulate membrane fluidity, but the structural difference creates a drug target:

- **Amphotericin B** -- binds ergosterol, forms pores in the fungal membrane --> ion leakage and cell death. Toxic because it has some affinity for cholesterol too (nephrotoxicity).
- **Azoles** (fluconazole, ketoconazole) -- inhibit **14-alpha-demethylase**, an enzyme in the ergosterol biosynthesis pathway (a cytochrome P450 enzyme). Without ergosterol, the membrane loses integrity.
- **Nystatin** -- similar mechanism to amphotericin B, used topically

**MCAT reasoning:** If a passage describes a drug that targets a sterol unique to fungal membranes, you should identify ergosterol as the target. If it describes membrane disruption in both fungal and human cells, think about the shared sterol-binding properties.

### Morphological Types

- **Yeasts** -- unicellular fungi that reproduce by **budding** (asymmetric division). Saccharomyces cerevisiae (baker's yeast) is the model organism. Candida albicans is a pathogenic yeast.
- **Molds** -- multicellular, filamentous fungi. Grow as **hyphae** (tubular filaments) that form a mesh called a **mycelium**. Hyphae can be septate (divided by cross-walls) or coenocytic (multinucleate, no septa).
- **Dimorphic fungi** -- can switch between yeast and mold forms depending on temperature. At **37 degrees C** (body temperature) they grow as **yeast**; at **25 degrees C** (environmental temperature) they grow as **mold**. Mnemonic: "mold in the cold, yeast in the heat." Clinically important: Histoplasma, Blastomyces, Coccidioides.

### Reproduction

Fungi reproduce both asexually (spores produced by mitosis -- conidia) and sexually (spores produced after fusion of hyphae from compatible mating types, involving meiosis). The MCAT is unlikely to test detailed fungal reproductive cycles, but knowing that fungi can be haploid for much of their life cycle distinguishes them from most animals.

---

## High-Yield Summary Table

| Feature | Prokaryotes | Viruses | Prions | Fungi |
|---------|------------|---------|--------|-------|
| Cell type | Prokaryotic | Acellular | N/A (protein only) | Eukaryotic |
| Genetic material | Circular dsDNA + plasmids | DNA or RNA | None | Linear DNA in nucleus |
| Ribosomes | 70S | None (use host's) | None | 80S |
| Reproduction | Binary fission | Host-dependent replication | Conformational conversion | Budding, spores, hyphae |
| Cell wall | Peptidoglycan | Capsid (not a cell wall) | N/A | Chitin |
| Drug targets | Cell wall synthesis, 70S ribosomes, DNA gyrase, folate synthesis | Reverse transcriptase, protease, integrase, neuraminidase | No effective drugs | Ergosterol, chitin synthesis |

---

## Quick-Fire MCAT Connections

- **Endosymbiotic theory:** Mitochondria have 70S ribosomes, circular DNA, and divide by fission -- bacterial ancestry
- **Hershey-Chase experiment:** Phage + radiolabeling --> DNA is the genetic material
- **Griffith's experiment:** Transformation --> "transforming principle" is DNA
- **Antibiotics and selective toxicity:** Every antibiotic mechanism on the MCAT traces back to a structural difference between prokaryotes and eukaryotes
- **HIV and immunology:** Retroviral lifecycle is a bridge between virology, molecular biology, and immune system content
- **Central dogma exceptions:** Reverse transcriptase (RNA to DNA) and prions (protein to protein "information" transfer) are the two big exceptions you must know
- **Biofilms and quorum sensing:** Testable as passage-based experimental design questions about bacterial communication
