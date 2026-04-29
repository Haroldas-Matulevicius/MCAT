# BB Bio Chapter 1 — The Cell

Scope: Cell theory; eukaryotic cell structure (organelles, cytoskeleton, endomembrane system); classification & structure of prokaryotic cells; genetics & growth of prokaryotic cells; viruses, prions, fungi.

**Section:** Bio/Biochem (BB)
**AAMC FC mapping:** FC2A (Cell structure -- organelles, cytoskeleton portion); FC2B (Prokaryotes & viruses)
**Kaplan Reference:** Biology Chapter 1
**Yield:** Very high. Organelle function, prokaryote/eukaryote contrasts, and viral lifecycles are nearly guaranteed exam content.

> Note: Membrane structure and transport (formerly part of FC2A) now lives in `BB_Ch08_Membranes.md` (biochem chapter). Cross-load both for cell-membrane topics.

---

## 1. Organelles

### Nucleus

The nucleus is the cell's command center -- it houses DNA and coordinates gene expression.

**Nuclear envelope**: A **double membrane** (inner + outer) continuous with the rough ER. The outer membrane often has ribosomes studding its cytoplasmic face. Between the two membranes is the **perinuclear space**, which is continuous with the ER lumen. This matters because it means the nuclear envelope is part of the endomembrane system.

**Nuclear pore complex (NPC)**: Large protein assemblies (~30+ nucleoporins) that span both membranes. They are **selective gates**:
- Small molecules and ions diffuse freely through the pore.
- Large molecules (proteins, ribosomal subunits, mRNA) require **active transport** using **importins/exportins** and a **Ran-GTP gradient**. Ran-GTP is concentrated in the nucleus; Ran-GDP in the cytoplasm. This gradient drives directionality of transport.
- **Nuclear localization signals (NLS)** on proteins tag them for import. **Nuclear export signals (NES)** tag molecules for export.

**Nucleolus**: A dense, non-membrane-bound region inside the nucleus. Its job is **rRNA synthesis and ribosomal subunit assembly**. rRNA genes are transcribed here, rRNA is processed and combined with ribosomal proteins (imported from the cytoplasm), and the assembled subunits are exported through nuclear pores. The nucleolus disappears during mitosis (chromatin condenses, transcription halts) and reforms in telophase.

> **MCAT connection**: Questions love testing what goes through nuclear pores and in which direction. mRNA goes OUT. Ribosomal proteins go IN, then assembled subunits come back OUT. DNA polymerase and transcription factors go IN.

---

### Mitochondria

Mitochondria are the **powerhouse** -- but more importantly for the MCAT, you need to know *where* each metabolic process occurs within them.

**Double membrane**:
- **Outer membrane**: Fairly permeable (has **porins**). Allows most small molecules through.
- **Inner membrane**: Highly **impermeable** -- this is critical. The impermeability is what allows the **proton gradient** (electrochemical gradient) to be maintained. The inner membrane is folded into **cristae** to increase surface area for the electron transport chain (ETC) and ATP synthase.
- **Intermembrane space (IMS)**: The space between outer and inner membranes. Protons are pumped here by Complexes I, III, and IV, making it **acidic** relative to the matrix (~pH 7.0 in IMS vs ~pH 7.8 in matrix).
- **Matrix**: The innermost compartment.

**Where things happen**:
| Process | Location |
|---------|----------|
| TCA cycle (Krebs) | Matrix |
| Pyruvate dehydrogenase | Matrix |
| Fatty acid beta-oxidation | Matrix |
| ETC (Complexes I-IV) | Inner membrane |
| ATP synthase (Complex V) | Inner membrane |
| Proton accumulation | IMS |

**Mitochondrial DNA**: Mitochondria have their own **circular DNA** (like bacteria -- supports endosymbiotic theory). Key facts:
- **Maternal inheritance** -- sperm mitochondria are tagged with ubiquitin and degraded after fertilization.
- Encodes 13 ETC proteins, 22 tRNAs, and 2 rRNAs. Most mitochondrial proteins are still nuclear-encoded and imported.
- Mitochondrial DNA has a **higher mutation rate** than nuclear DNA (no histones, limited repair mechanisms, proximity to ROS from the ETC).

> **MCAT connection**: Diseases with maternal inheritance patterns = think mitochondrial. Example: **Leber hereditary optic neuropathy (LHON)**. Also, cyanide and carbon monoxide poison the ETC at Complex IV -- they work because the inner membrane must maintain its proton gradient to make ATP.

---

### Endoplasmic Reticulum (ER)

**Rough ER (RER)**:
- Studded with **ribosomes** on the cytoplasmic face.
- Function: Synthesis of **secretory proteins**, **membrane proteins**, and **lysosomal enzymes**.
- The **signal recognition particle (SRP)** binds the signal sequence on a nascent polypeptide, pauses translation, and docks the ribosome-mRNA complex to the **SRP receptor** on the RER. Translation resumes, and the protein is threaded into the ER lumen through a **translocon**.
- Inside the ER lumen: **N-linked glycosylation** begins (oligosaccharide added to asparagine residues), **disulfide bond formation** (oxidizing environment in the lumen), and **protein folding** with chaperones (e.g., BiP).
- Misfolded proteins are targeted for **ER-associated degradation (ERAD)** -- sent back to the cytoplasm and degraded by proteasomes.

**Smooth ER (SER)**:
- No ribosomes.
- **Lipid synthesis**: phospholipids, steroids (important in steroid-producing cells like adrenal cortex and gonads).
- **Detoxification**: cytochrome P450 enzymes oxidize drugs and toxins (abundant in hepatocytes -- this is why the liver detoxifies).
- **Calcium storage**: The SER sequesters Ca2+ via **SERCA pumps** (Ca2+-ATPases). Release of Ca2+ from the SER is a key signaling event (e.g., IP3 triggers Ca2+ release). In muscle cells, the SER is called the **sarcoplasmic reticulum (SR)**, and Ca2+ release triggers contraction.

> **MCAT connection**: Signal sequence, SRP pathway, and the distinction between N-linked (ER, asparagine) vs O-linked (Golgi, serine/threonine) glycosylation are high-yield.

---

### Golgi Apparatus

Think of the Golgi as the **post office** -- it receives, modifies, sorts, and ships proteins.

**Structure**: Stacked, flattened membrane sacs (**cisternae**). Has polarity:
- **Cis face** (receiving): faces the ER. Receives transport vesicles from the ER.
- **Medial cisternae**: middle processing layers.
- **Trans face** (shipping): faces the plasma membrane. Sends vesicles to their final destinations.

**Modifications in the Golgi**:
- **O-linked glycosylation**: Addition of sugars to serine or threonine residues (happens ONLY in the Golgi, unlike N-linked which starts in the ER).
- **Trimming and modification of N-linked glycans**: The oligosaccharide chains added in the ER are further processed.
- **Phosphorylation of mannose residues**: Adding **mannose-6-phosphate (M6P)** tags to lysosomal enzymes. M6P receptors in the trans-Golgi network recognize these tags and direct the enzymes into vesicles bound for lysosomes. This is a critical sorting mechanism.
- **Proteolytic processing**: Some proteins are cleaved to their active forms.

**Sorting at the trans-Golgi network**:
- Constitutive secretory pathway: default, continuous secretion (e.g., ECM proteins, antibodies).
- Regulated secretory pathway: stored in secretory granules, released on signal (e.g., insulin from beta cells, neurotransmitters).
- Lysosomal pathway: M6P-tagged enzymes sent to lysosomes.

> **MCAT connection**: **I-cell disease** (mucolipidosis II) -- failure to add M6P tags. Lysosomal enzymes are secreted outside the cell instead of being delivered to lysosomes. Lysosomes fill with undigested material ("inclusion bodies"). This is a classic example they can test.

---

### Lysosomes

**Lysosomes** are membrane-bound organelles filled with **acid hydrolases** (~50 different enzymes) that break down macromolecules: proteins, lipids, carbohydrates, nucleic acids.

**Optimal pH ~5** (acidic). The cytoplasm is ~pH 7.2. How is this gradient maintained?
- **V-type H+ ATPases** (vacuolar proton pumps) in the lysosomal membrane actively pump H+ into the lysosome using ATP. This keeps the interior acidic.
- The acidic pH serves as a **safety mechanism**: if a lysosome ruptures, its enzymes are mostly inactive at cytoplasmic pH 7.2, limiting damage. (Though massive lysosome rupture can trigger apoptosis.)

**Functions**:
- **Autophagy**: Digestion of the cell's own damaged organelles. An **autophagosome** (double-membrane vesicle) engulfs the organelle and fuses with a lysosome.
- **Phagocytic digestion**: Macrophages engulf pathogens into a **phagosome**, which fuses with a lysosome to form a **phagolysosome** where the pathogen is destroyed.
- **Receptor recycling**: After receptor-mediated endocytosis, the endosome acidifies, causing ligand release. Receptors can be recycled back to the membrane; ligands are sent to lysosomes for degradation (e.g., LDL receptor pathway).

**Lysosomal storage diseases**: When a specific lysosomal enzyme is deficient or absent, its substrate accumulates. Examples:
| Disease | Missing Enzyme | Accumulated Substrate |
|---------|---------------|----------------------|
| **Tay-Sachs** | Hexosaminidase A | GM2 ganglioside |
| **Gaucher** | Glucocerebrosidase | Glucocerebroside |
| **Niemann-Pick** | Sphingomyelinase | Sphingomyelin |
| **Hurler syndrome** | alpha-L-iduronidase | Heparan/dermatan sulfate |
| **Pompe** | Acid maltase (acid alpha-glucosidase) | Glycogen |

> **MCAT connection**: Tay-Sachs is the most commonly tested. Cherry-red macula, neurodegeneration, autosomal recessive, more common in Ashkenazi Jewish populations. Know the general principle: enzyme deficiency leads to substrate accumulation.

---

### Peroxisomes

**Peroxisomes** are single-membrane organelles involved in **oxidative reactions** that produce **hydrogen peroxide (H2O2)** as a byproduct.

- **Catalase** is the key enzyme: it breaks down H2O2 into water and oxygen (2H2O2 -> 2H2O + O2). This protects the cell from oxidative damage.
- **Very long chain fatty acid (VLCFA) beta-oxidation**: Peroxisomes shorten VLCFAs that are too long for mitochondrial beta-oxidation. The shortened chains are then transferred to mitochondria for complete oxidation.
- **Plasmalogen synthesis**: Important membrane lipids, especially in the brain and heart.
- Peroxisomes are NOT part of the endomembrane system -- they self-replicate by division and import their proteins from the cytoplasm using **peroxisomal targeting signals (PTS)**.

> **MCAT connection**: **Zellweger syndrome** -- failure to import peroxisomal enzymes due to defective PEX genes. VLCFAs accumulate. Severe neurological defects, usually fatal in infancy. Also know that peroxisomes and mitochondria both do beta-oxidation but on different substrates.

---

### The Endomembrane System: Protein Trafficking

The endomembrane system connects the ER, Golgi, lysosomes, endosomes, and plasma membrane through **vesicular transport**.

**The secretory pathway** (for a newly synthesized secretory protein):
1. Protein synthesized on **RER** ribosomes, enters ER lumen via SRP pathway.
2. Protein folds, gets N-linked glycosylation in the ER.
3. **COPII-coated vesicles** bud from the ER and carry the protein to the **cis-Golgi**.
4. Protein moves through Golgi cisternae (cis -> medial -> trans), receiving further modifications.
5. At the **trans-Golgi network**, the protein is sorted:
   - **Clathrin-coated vesicles** carry lysosomal enzymes (M6P-tagged) to late endosomes/lysosomes.
   - Secretory vesicles carry proteins to the plasma membrane for secretion or membrane insertion.

**Retrograde transport**: **COPI-coated vesicles** carry proteins backwards (Golgi -> ER) to retrieve escaped ER-resident proteins. ER-resident proteins have a **KDEL sequence** (Lys-Asp-Glu-Leu) that acts as an ER retrieval signal.

**Coat proteins summary**:
| Coat | Direction | Function |
|------|-----------|----------|
| **COPII** | ER -> Golgi | Anterograde transport |
| **COPI** | Golgi -> ER | Retrograde retrieval |
| **Clathrin** | Trans-Golgi -> lysosomes; plasma membrane -> endosomes | Sorting to lysosomes; receptor-mediated endocytosis |

> **MCAT connection**: COPII = forward (think: II looks like arrows pointing forward). COPI = backward. Clathrin is used at two places: Golgi sorting and receptor-mediated endocytosis at the cell surface.

---

## 2. Cytoskeleton

The cytoskeleton provides **structure, movement, and intracellular transport**. Three types of filaments, each with distinct properties.

### Microfilaments (Actin Filaments)

- **Composition**: Polymerized **G-actin** (globular) monomers form **F-actin** (filamentous) strands. Two strands twist into a helix.
- **Diameter**: ~7 nm (thinnest).
- **Polarity**: Yes -- has a **plus end** (fast-growing, barbed end) and **minus end** (slow-growing, pointed end).
- **Functions**:
  - **Muscle contraction**: Actin thin filaments interact with myosin thick filaments (sliding filament model).
  - **Cytokinesis**: The **contractile ring** (actin + myosin II) pinches the cell in two during cell division.
  - **Cell motility**: Actin polymerization at the leading edge pushes the membrane forward (lamellipodia, filopodia).
  - **Cell shape and microvilli**: Actin cores stiffen microvilli in intestinal epithelial cells (increases absorptive surface area).
  - **Cell cortex**: A meshwork of actin just beneath the plasma membrane, giving mechanical support.

**Drug target**: **Cytochalasin B/D** -- caps the plus end of actin filaments, preventing polymerization. Disrupts cytokinesis, cell motility, and phagocytosis. **Phalloidin** -- stabilizes actin filaments, preventing depolymerization (used in research, not tested as heavily).

---

### Intermediate Filaments (IFs)

- **Diameter**: ~10 nm (intermediate between actin and microtubules).
- **Composition**: Varies by cell type -- this is the defining feature. They are tissue-specific:
  - **Keratins**: Epithelial cells (also hair, nails).
  - **Vimentin**: Mesenchymal cells (fibroblasts, endothelial cells, white blood cells).
  - **Desmin**: Muscle cells.
  - **Neurofilaments**: Neurons (caliber of axon).
  - **Lamins**: Nuclear lamina (lines the inner nuclear membrane, provides structural support).
  - **GFAP**: Glial cells (astrocytes).
- **NO polarity**: Unlike actin and microtubules, IFs are **non-polar**. This means no motor proteins walk along them.
- **Purely structural**: They resist **tensile (stretching) forces**. They don't participate in cell motility or intracellular transport.
- **Most stable** of the three filament types -- they don't undergo the dynamic treadmilling or dynamic instability that actin and microtubules do.

**Anchoring**: IFs attach to **desmosomes** and **hemidesmosomes** (cell junctions that resist shearing forces).

> **MCAT connection**: **Epidermolysis bullosa simplex** -- mutation in keratin genes. Skin blisters easily because epithelial IFs can't resist mechanical stress. Also, lamins disassemble during mitosis (phosphorylation by CDKs causes nuclear envelope breakdown).

---

### Microtubules

- **Composition**: Heterodimers of **alpha-tubulin** and **beta-tubulin** polymerize into a hollow tube of 13 protofilaments.
- **Diameter**: ~25 nm (largest).
- **Polarity**: Yes -- **plus end** (beta-tubulin exposed, fast-growing) and **minus end** (alpha-tubulin exposed, anchored at the **centrosome/MTOC**).
- **Dynamic instability**: Microtubules rapidly switch between growing and shrinking phases. This is powered by **GTP hydrolysis** -- tubulin dimers bind GTP, and after incorporation, GTP is hydrolyzed to GDP. GDP-tubulin is less stable, so if the GTP cap is lost, the microtubule rapidly depolymerizes (**catastrophe**). Regrowth = **rescue**.

**Functions**:
- **Mitotic spindle**: Separates chromosomes during cell division. Kinetochore microtubules attach to chromosomes; astral microtubules position the spindle; polar microtubules push the poles apart.
- **Intracellular transport**: Motor proteins carry cargo along microtubules.
- **Cilia and flagella**: **9+2 arrangement** of microtubule doublets (9 outer pairs + 2 central singlets). Powered by **axonemal dynein**. The base is the **basal body** (modified centriole, 9+0 triplet arrangement).

### Motor Proteins on Microtubules

| Motor Protein | Direction | Mnemonic | Function |
|---------------|-----------|----------|----------|
| **Kinesin** | Toward **+ end** (away from nucleus, toward periphery) | "Kinesin Kicks things out" | Anterograde transport: moves vesicles, organelles toward the cell periphery |
| **Dynein** (cytoplasmic) | Toward **- end** (toward nucleus/MTOC) | "Dynein Drags things in" | Retrograde transport: moves cargo toward the cell center; also moves chromosomes during mitosis |
| **Dynein** (axonemal) | -- | -- | Powers ciliary/flagellar beating by sliding microtubule doublets |

> **MCAT connection**: **Kartagener syndrome (primary ciliary dyskinesia)** -- defect in **dynein arms** of cilia. Results in immotile cilia: chronic respiratory infections (can't clear mucus), male infertility (immotile sperm), and **situs inversus** (reversed organ placement, because cilia determine left-right asymmetry during embryogenesis).

### Cytoskeletal Drug Targets

| Drug | Target | Effect |
|------|--------|--------|
| **Colchicine** | Tubulin dimers (prevents polymerization) | Blocks mitotic spindle formation -- arrests cells in metaphase. Used to treat gout. |
| **Taxol (paclitaxel)** | Microtubules (prevents depolymerization) | Stabilizes microtubules -- spindle can't disassemble, so cells can't complete mitosis. Chemotherapy drug. |
| **Vincristine/Vinblastine** | Tubulin (prevents polymerization) | Similar to colchicine -- blocks mitosis. Chemotherapy. |
| **Cytochalasin B** | Actin (caps + end, prevents polymerization) | Blocks cytokinesis, phagocytosis, cell movement. |

> Both colchicine and taxol block mitosis, but by **opposite mechanisms** (preventing assembly vs preventing disassembly). The MCAT loves this distinction.

---

## 3. Prokaryotic Cell Structure

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

## 4. Prokaryotic Reproduction and Genetic Transfer

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

## 5. Viruses

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
- **Transduction** -- natural mechanism of horizontal gene transfer (see Section 4)
- T-even phages (T2, T4) are classic lytic phages (Hershey-Chase experiment used T2 phage with radiolabeled protein [35S] and DNA [32P] to prove DNA is the genetic material)
- **Lambda phage** is the classic temperate phage (can do lytic or lysogenic)

---

## 6. Prions

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

## 7. Fungi Basics

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

## High-Yield Summary Table -- Cell Types

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

## High-Yield Takeaways for MCAT (Eukaryotic Cell)

1. **Know what happens where in the mitochondrion** -- TCA/beta-ox in matrix, ETC on inner membrane, protons in IMS.
2. **Signal sequence + SRP pathway** for targeting proteins to the ER.
3. **N-linked glycosylation starts in the ER; O-linked happens in the Golgi.**
4. **M6P tags** direct enzymes to lysosomes. Failure = I-cell disease.
5. **COPII goes forward (ER->Golgi), COPI goes backward (Golgi->ER), clathrin sorts at the Golgi and internalizes at the plasma membrane.**
6. **Kinesin = + end (out), Dynein = - end (in).** Kartagener syndrome = dynein defect.

→ Membrane structure & transport / cell junctions: see `BB_Ch08_Membranes.md`
→ Cell cycle, mitosis, apoptosis, cancer: see `BB_Bio_Ch02_Reproduction.md`
