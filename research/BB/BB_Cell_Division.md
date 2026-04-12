# FC2C: Cell Division and Differentiation -- Deep Dive

This guide covers the full scope of cell division, cell death, cancer biology, and stem cells as tested on the MCAT Bio/Biochem section. Every mechanism here is fair game. Master the logic, not just the labels.

---

## 1. The Cell Cycle

The cell cycle is how one cell becomes two. It has four main phases -- **G1, S, G2, and M** -- plus a resting state called **G0**. The "G" stands for "gap," the "S" for "synthesis," and the "M" for "mitosis." Together, G1 + S + G2 make up **interphase**, which is where the cell spends most of its life.

### G1 Phase (Gap 1)

This is the cell's main working phase. The cell is:
- **Growing in size** (accumulating cytoplasm, organelles, proteins)
- Carrying out its **normal differentiated functions** (a liver cell is doing liver things)
- **Synthesizing the machinery** it will need for DNA replication (enzymes, nucleotides, etc.)

G1 is the most variable phase in length. A rapidly dividing cell (like a gut epithelial cell) has a short G1. A slowly dividing cell has a long G1. Cells that stop dividing altogether exit the cycle from G1 into **G0**.

**MCAT trap:** During G1, each chromosome exists as a single chromatid. The cell is **diploid (2n)** with **2n DNA content (2C)**. Do not confuse ploidy (number of chromosome sets) with DNA content (amount of DNA).

### S Phase (Synthesis)

This is when **DNA replication** occurs. Every chromosome is duplicated, so each one now consists of **two sister chromatids** joined at the **centromere** by **cohesin proteins**.

- DNA content doubles: the cell goes from **2C to 4C**
- Ploidy stays the same: still **2n** (the sister chromatids are considered one chromosome)
- **Centrosomes also duplicate** during S phase (you need two to form the mitotic spindle)
- Histones are synthesized in large quantities to package the new DNA

**Key concept:** Replication errors that slip past proofreading and mismatch repair here are exactly how mutations accumulate. This is why checkpoint control around S phase matters so much.

### G2 Phase (Gap 2)

The cell prepares to divide:
- Continues to **grow and synthesize proteins** (especially tubulin for the mitotic spindle)
- **Error-checking**: the cell verifies that DNA replication is complete and repairs any remaining damage
- Mitochondria and other organelles continue to be produced so both daughter cells get enough

DNA content is **4C**, ploidy is **2n**. The cell has twice the normal DNA but is still considered diploid.

### M Phase (Mitosis + Cytokinesis)

The actual division event. Mitosis divides the **nucleus**; cytokinesis divides the **cytoplasm**. Covered in detail in Section 2 below.

### G0 Phase (Quiescence)

Some cells exit the cell cycle and enter **G0**, a resting state where they are metabolically active but **not preparing to divide**.

- **Neurons** -- permanently in G0 (this is why brain damage is largely irreversible)
- **Cardiac muscle cells (cardiomyocytes)** -- permanently in G0 (this is why heart attacks cause permanent damage; dead cardiac tissue is replaced by scar tissue, not new muscle)
- **Skeletal muscle fibers** -- in G0 but can be stimulated to divide via satellite cells
- **Hepatocytes (liver cells)** -- normally in G0 but can re-enter the cycle if the liver is damaged (this is why the liver can regenerate)

**MCAT connection:** When a question asks "which cell type cannot regenerate," think G0-permanent cells: neurons and cardiomyocytes.

---

## Cell Cycle Checkpoints

Checkpoints are **surveillance mechanisms** that halt the cell cycle if conditions are not met. Think of them as quality control gates. There are three major ones.

### G1/S Checkpoint (The Restriction Point)

This is the **most important checkpoint** and the one the MCAT cares about the most.

**What it checks:**
- Is the cell **large enough** to divide?
- Is there **adequate nutrition** and **growth factor signaling**?
- Is the **DNA intact** (no damage)?

**How it works:**
- Growth factor signaling activates the **Ras-MAPK pathway**, which drives expression of **Cyclin D**
- **Cyclin D binds CDK4/6**, forming an active complex
- Cyclin D-CDK4/6 **phosphorylates Rb (retinoblastoma protein)**
- Unphosphorylated Rb normally **sequesters E2F** (a transcription factor), keeping it inactive
- Phosphorylated Rb **releases E2F**, which then drives transcription of genes needed for S phase entry, including **Cyclin E**
- **Cyclin E binds CDK2**, which pushes the cell past the restriction point and commits it to DNA replication

**Why the restriction point matters:** Once a cell passes this checkpoint, it is committed to dividing. It no longer needs external growth factor signals. This is exactly where cancer goes wrong -- oncogenic mutations that constitutively activate this pathway push cells past the restriction point without proper signaling.

### G2/M Checkpoint

**What it checks:**
- Is **DNA replication complete**?
- Is there **unrepaired DNA damage**?

**How it works:**
- **Cyclin B accumulates** during G2 and binds **CDK1** (also called Cdc2)
- Cyclin B-CDK1 is the **"Maturation Promoting Factor" (MPF)** -- this is the master switch for mitotic entry
- If DNA damage is detected, **p53 activates p21**, which **inhibits CDK activity**, arresting the cell in G2

### Spindle Assembly Checkpoint (SAC)

**What it checks:**
- Are **all chromosomes properly attached** to spindle fibers via kinetochores?
- Is there **proper bipolar tension** (each sister chromatid attached to opposite poles)?

**How it works:**
- Unattached kinetochores generate a **"wait" signal** via the **Mad2 protein**
- Mad2 inhibits the **Anaphase-Promoting Complex/Cyclosome (APC/C)**
- Once all chromosomes are properly attached and under tension, Mad2 signal ceases, **APC/C activates**, and it triggers anaphase by targeting **securin** for degradation (which frees **separase** to cleave cohesin -- more on this in Section 2)

**MCAT logic:** If the SAC fails, you get **aneuploidy** (wrong chromosome number) -- a hallmark of many cancers.

---

## Cyclins and CDKs

**Cyclin-dependent kinases (CDKs)** are enzymes that phosphorylate target proteins to drive the cell cycle forward. They are **constitutively expressed** but **inactive without their cyclin partners**. Cyclins are the regulatory subunits whose levels **rise and fall** at specific phases.

| Phase Transition | Cyclin | CDK | Key Target |
|---|---|---|---|
| G1 progression | **Cyclin D** | **CDK4/6** | Rb (phosphorylation releases E2F) |
| G1 to S | **Cyclin E** | **CDK2** | Rb (further phosphorylation), replication machinery |
| S phase | **Cyclin A** | **CDK2** | Replication fork proteins |
| G2 to M | **Cyclin B** | **CDK1** | Nuclear lamins, condensins (triggers mitosis) |

**CDK inhibitors (CKIs)** are the brakes:
- **p21** -- activated by p53, broadly inhibits CDKs (especially at G1/S and G2/M)
- **p27** -- inhibits Cyclin E-CDK2 at G1/S
- **p16 (INK4a)** -- specifically inhibits CDK4/6, preventing Rb phosphorylation

**The key concept:** Cancer is fundamentally a disease of cell cycle deregulation. Oncogenes are like a stuck accelerator (cyclins, CDKs, growth factor receptors). Tumor suppressors are like broken brakes (p53, Rb, CKIs).

---

## p53 -- Guardian of the Genome

**p53** is a transcription factor and the most frequently mutated gene in human cancers (~50% of all cancers). It sits at the center of the DNA damage response.

**What p53 does when activated by DNA damage:**
1. **Cell cycle arrest** -- activates p21, which inhibits CDKs, halting the cell in G1 or G2
2. **DNA repair** -- upregulates DNA repair enzymes to fix the damage
3. **Apoptosis** -- if damage is irreparable, p53 activates pro-apoptotic genes (Bax, PUMA) to trigger programmed cell death

**Regulation of p53:**
- Normally, p53 levels are kept low by **MDM2**, which ubiquitinates p53 and targets it for proteasomal degradation
- When DNA damage occurs, kinases like **ATM/ATR** phosphorylate p53, preventing MDM2 binding, and p53 accumulates

**MCAT reasoning:** If a question describes a cell that continues to divide despite DNA damage, think **p53 loss of function**. If a question describes a cell that never enters S phase even with growth signals, think **constitutively active p53 or Rb**.

---

## 2. Mitosis (PMAT)

Mitosis is the division of the nucleus into two genetically identical daughter nuclei. Use the mnemonic **PMAT**: Prophase, Metaphase, Anaphase, Telophase. Some sources split Prometaphase out separately.

### Prophase

- **Chromatin condenses** into visible chromosomes (driven by condensin complexes and histone phosphorylation)
- Each chromosome consists of **two sister chromatids** joined at the centromere
- The **mitotic spindle begins to form**: centrosomes (each with two centrioles) migrate to opposite poles and nucleate microtubules
- The **nucleolus disappears** (rRNA transcription shuts down)

### Prometaphase

- The **nuclear envelope breaks down** (nuclear lamins are phosphorylated by Cyclin B-CDK1, causing disassembly)
- **Kinetochores** assemble on the centromeric DNA of each sister chromatid
- Spindle microtubules **attach to kinetochores** -- each sister chromatid's kinetochore faces opposite poles
- Chromosomes are pushed and pulled as they begin moving toward the cell center
- Three types of spindle microtubules: **kinetochore fibers** (attach to chromosomes), **polar/interpolar fibers** (overlap at the center, push poles apart), **astral fibers** (anchor spindle to cell cortex)

### Metaphase

- All chromosomes are aligned at the **metaphase plate** (the cell's equator)
- The **spindle assembly checkpoint** operates here: every kinetochore must be attached with proper bipolar tension before the cell proceeds
- This is the best stage to create a **karyotype** because chromosomes are maximally condensed and aligned

### Anaphase

Anaphase has two sub-stages:

**Anaphase A:**
- **APC/C** (activated after SAC is satisfied) ubiquitinates **securin**, targeting it for degradation
- This releases **separase**, which cleaves **cohesin** holding sister chromatids together
- Sister chromatids are pulled to **opposite poles** by shortening of kinetochore microtubules (motor proteins depolymerize tubulin at the kinetochore end)

**Anaphase B:**
- Polar microtubules slide past each other, **elongating the cell**
- Astral microtubules pull poles further apart

**MCAT point:** After anaphase, each separated chromatid is now considered an individual chromosome. The cell temporarily has **4n chromosomes** (but each has only one chromatid, so DNA content is still 4C total, split 2C per future daughter cell).

### Telophase

- **Nuclear envelopes reform** around each set of chromosomes (nuclear lamins are dephosphorylated)
- Chromosomes **decondense** back into chromatin
- **Nucleoli reappear**
- The spindle disassembles

### Cytokinesis

**In animal cells:**
- A **contractile ring** of **actin and myosin** filaments assembles at the cell's equator
- The ring contracts, forming a **cleavage furrow** that pinches the cell in two
- The position of the cleavage furrow is determined by the **spindle midzone** signaling to the cell cortex

**In plant cells:**
- A **cell plate** forms from the center outward
- **Vesicles from the Golgi** carrying cell wall material fuse at the midline
- The cell plate eventually becomes the new **cell wall** separating the two daughter cells

**MCAT trap:** Plant cells do NOT have centrioles or cleavage furrows. They still form a mitotic spindle (from microtubule-organizing centers without centrioles).

**End result:** Two genetically identical diploid (2n, 2C) daughter cells.

---

## 3. Apoptosis (Programmed Cell Death)

### Apoptosis vs. Necrosis

This distinction is a favorite MCAT question.

| Feature | **Apoptosis** | **Necrosis** |
|---|---|---|
| Trigger | Internal signals or specific death signals | Injury, toxin, ischemia |
| Process | Orderly, energy-dependent | Chaotic, uncontrolled |
| Cell size | Cell **shrinks** | Cell **swells** |
| Membrane | Stays intact (forms blebs, "apoptotic bodies") | **Ruptures**, contents leak |
| Inflammation | **No** (clean death, phagocytes eat apoptotic bodies) | **Yes** (leaked contents trigger immune response) |
| DNA | Cleaved into regular fragments ("DNA ladder" on gel) | Random degradation ("smear" on gel) |
| Energy | Requires ATP | No ATP required |

**MCAT connection:** If a question describes cell swelling and inflammation in surrounding tissue, that is necrosis. If it describes cell shrinkage with no inflammatory response, that is apoptosis.

### Caspases

**Caspases** are cysteine proteases that cleave after aspartate residues (hence the name: **c**ysteine-**asp**artic prote**ases**). They are the executors of apoptosis.

- **Initiator caspases** (caspase-8, caspase-9): activated first, they cleave and activate executioner caspases
- **Executioner caspases** (caspase-3, caspase-6, caspase-7): carry out the actual destruction -- cleaving structural proteins, activating DNases, dismantling the cell

All caspases exist as **inactive zymogens (procaspases)**. They are activated by proteolytic cleavage in an **amplifying cascade** (similar logic to the complement system or clotting cascade).

### Intrinsic (Mitochondrial) Pathway

This pathway is triggered by **internal cellular stress**: DNA damage, oxidative stress, growth factor withdrawal, or ER stress.

**The mechanism step by step:**
1. Stress signals activate **pro-apoptotic Bcl-2 family members**: **Bax** and **Bak**
2. Bax and Bak **oligomerize in the outer mitochondrial membrane**, forming pores
3. These pores allow **cytochrome c** to leak from the **intermembrane space** into the cytoplasm
4. Cytoplasmic cytochrome c binds **Apaf-1** (apoptotic protease activating factor-1)
5. Cytochrome c + Apaf-1 assemble into a heptameric wheel-shaped complex called the **apoptosome**
6. The apoptosome recruits and activates **procaspase-9** (initiator caspase)
7. Active **caspase-9** then cleaves and activates **caspase-3** (executioner caspase)
8. Caspase-3 dismantles the cell

**Anti-apoptotic proteins (Bcl-2, Bcl-xL)** sit in the outer mitochondrial membrane and **prevent Bax/Bak from forming pores**. They are survival signals. When the balance tips toward pro-apoptotic members, the cell dies.

**MCAT connection:** Cytochrome c normally functions in the electron transport chain (Complex III to Complex IV). Its release into the cytoplasm is a death signal. This is a beautiful example of compartmentalization -- the same molecule has completely different functions depending on where it is.

### Extrinsic (Death Receptor) Pathway

This pathway is triggered by **external signals** -- specifically, **death ligands** binding to **death receptors** on the cell surface.

**The mechanism step by step:**
1. A **death ligand** (FasL, TNF, TRAIL) binds its corresponding **death receptor** (Fas, TNFR, DR4/5) on the target cell
2. The death receptor's intracellular **death domain** recruits adaptor proteins (FADD)
3. FADD recruits **procaspase-8**, forming the **DISC (death-inducing signaling complex)**
4. Procaspase-8 is activated by proximity-induced auto-cleavage
5. Active **caspase-8** directly cleaves and activates **caspase-3** (executioner)

**Cross-talk:** Caspase-8 can also cleave **Bid** (a Bcl-2 family member), producing **tBid**, which activates Bax/Bak and triggers the intrinsic pathway. This amplifies the death signal.

**MCAT example:** Cytotoxic T cells kill virus-infected cells via FasL-Fas interaction (extrinsic pathway). This is also how the immune system eliminates autoreactive lymphocytes during negative selection.

### Why Apoptosis Matters

- **Development:** Sculpting fingers and toes (removing webbing), eliminating excess neurons
- **Immune system:** Negative selection of autoreactive T and B cells, killing virus-infected cells
- **Cancer prevention:** Cells with irreparable DNA damage are eliminated before they can proliferate
- **Homeostasis:** Balancing cell production and cell death to maintain tissue size

**When apoptosis fails:** Cells that should die survive instead -- this is a hallmark of cancer (resistance to cell death). Overexpression of **Bcl-2** is seen in many lymphomas.

---

## 4. Cancer Biology

Cancer is fundamentally a disease of **uncontrolled cell proliferation** caused by accumulated mutations in genes that regulate the cell cycle, apoptosis, and tissue integrity.

### Oncogenes

An **oncogene** is a mutated version of a normal gene (called a **proto-oncogene**) that drives cell growth. The mutation is a **gain-of-function** -- the protein is either overactive, overexpressed, or constitutively active.

**Key principle:** Oncogenes are **dominant** -- mutation of **one allele** is sufficient to promote cancer. Think of it as a stuck gas pedal.

**High-yield oncogene examples:**

| Oncogene | Normal Function | What Goes Wrong |
|---|---|---|
| **Ras** | Small GTPase in growth factor signaling (Ras-MAPK pathway) | Point mutation locks Ras in GTP-bound (ON) state; cannot hydrolyze GTP back to GDP. Constitutive proliferative signaling. **Most commonly mutated oncogene in human cancer (~30%).** |
| **Myc** | Transcription factor driving cell cycle entry and growth | Overexpressed (often by gene amplification or translocation); pushes cells through G1 into S phase regardless of signals. Burkitt lymphoma: t(8;14) translocation puts Myc under control of the immunoglobulin heavy chain promoter. |
| **Src** | Non-receptor tyrosine kinase | Constitutively active kinase; first oncogene discovered (Rous sarcoma virus). |
| **HER2/ErbB2** | Receptor tyrosine kinase (EGFR family) | Gene amplification leads to overexpression; receptor is always active. Seen in ~20% of breast cancers. Target of trastuzumab (Herceptin). |
| **Bcl-2** | Anti-apoptotic protein | Overexpression prevents apoptosis; cells that should die survive. Follicular lymphoma: t(14;18) translocation. |

**Ways proto-oncogenes become oncogenes:**
- **Point mutation** (Ras -- single amino acid change)
- **Gene amplification** (HER2 -- extra copies of the gene)
- **Chromosomal translocation** (Myc in Burkitt lymphoma, Bcl-2 in follicular lymphoma, BCR-ABL "Philadelphia chromosome" in CML)
- **Viral insertion** near a proto-oncogene (retroviral oncogenesis)

### Tumor Suppressors

**Tumor suppressor genes** encode proteins that **restrain** cell growth, promote DNA repair, or trigger apoptosis. They require **loss-of-function** mutations, and typically **both alleles** must be knocked out for the effect -- this is **Knudson's two-hit hypothesis**.

**Key principle:** Tumor suppressors are **recessive** at the cellular level. Losing one copy still leaves one functional copy (haploinsufficiency is sometimes enough, but classically you need both hits). Think of it as losing your brakes.

**High-yield tumor suppressor examples:**

| Gene | Normal Function | Consequence of Loss |
|---|---|---|
| **p53** | Transcription factor: activates p21 (cell cycle arrest), DNA repair genes, pro-apoptotic genes (Bax) | Cells with DNA damage are not arrested or killed; mutations accumulate. **Li-Fraumeni syndrome** (germline p53 mutation -- one hit inherited, cancers develop early). |
| **Rb** | Binds and sequesters E2F; prevents transcription of S-phase genes | E2F is constitutively free; cells enter S phase without growth signals. **Retinoblastoma** (childhood eye cancer, often bilateral if inherited). Knudson literally developed the two-hit hypothesis studying this cancer. |
| **BRCA1/BRCA2** | DNA double-strand break repair via homologous recombination | DNA damage accumulates; genomic instability. Increased risk of breast, ovarian, prostate cancer. |
| **APC** | Promotes degradation of beta-catenin in the Wnt pathway | Beta-catenin accumulates, activates transcription of proliferative genes. **Familial adenomatous polyposis** -- hundreds of colon polyps, virtually guaranteed colorectal cancer without prophylactic colectomy. |
| **p16/INK4a** | CDK4/6 inhibitor; prevents Rb phosphorylation | CDK4/6 is constitutively active, Rb is always phosphorylated (inactivated), cell cycle is deregulated. |

### Knudson's Two-Hit Hypothesis

Alfred Knudson studied retinoblastoma and noticed two patterns:
- **Hereditary form:** One mutant Rb allele is **inherited** (first hit from birth). Only one additional **somatic mutation** is needed (second hit). Cancer appears **early** in life, often in **both eyes** (bilateral).
- **Sporadic form:** Both hits must occur **somatically** in the same cell. This is much less likely, so cancer appears **later** in life, usually in **one eye** (unilateral).

**MCAT takeaway:** Inherited cancer syndromes follow this pattern -- one hit is inherited, so cancer develops earlier and in multiple sites. Sporadic cancers need both hits by chance.

### Hallmarks of Cancer (Hanahan & Weinberg)

The MCAT expects you to know the six original hallmarks and recognize them in passage contexts:

1. **Sustaining proliferative signaling** -- oncogenes (Ras, Myc) provide constant "grow" signals
2. **Evading growth suppressors** -- loss of Rb, p53, or other tumor suppressors
3. **Resisting cell death** -- overexpression of Bcl-2, loss of p53-mediated apoptosis
4. **Enabling replicative immortality** -- activation of **telomerase** (normal somatic cells cannot divide indefinitely because telomeres shorten with each division; cancer cells reactivate telomerase to maintain telomere length)
5. **Inducing angiogenesis** -- tumors secrete **VEGF** (vascular endothelial growth factor) to recruit new blood vessels for oxygen and nutrient supply
6. **Activating invasion and metastasis** -- cancer cells break free from the primary tumor and colonize distant organs

### Metastasis

The process by which cancer spreads from the primary site to distant organs.

**Step by step:**
1. **Epithelial-to-Mesenchymal Transition (EMT):** Carcinoma cells lose epithelial characteristics (cell-cell adhesion via E-cadherin) and gain mesenchymal characteristics (motility, invasiveness). **Loss of E-cadherin** is a hallmark of EMT.
2. **Local invasion:** Cells degrade the basement membrane using **matrix metalloproteinases (MMPs)** and invade surrounding tissue.
3. **Intravasation:** Cancer cells enter blood or lymphatic vessels.
4. **Survival in circulation:** Most circulating tumor cells die (shear stress, immune attack), but some survive.
5. **Extravasation:** Surviving cells exit the vessel at a distant site.
6. **Colonization:** Cells establish a new tumor (metastatic lesion) at the distant site. This is the rate-limiting step -- most cells that reach a distant site fail to colonize.

**MCAT connection:** Common metastatic routes -- lung, liver, bone, brain. Colon cancer often metastasizes to liver first (portal circulation). Sarcomas tend to spread hematogenously to lungs.

---

## 5. Stem Cells and Differentiation

### The Potency Hierarchy

**Potency** describes how many different cell types a stem cell can give rise to.

| Potency Level | Definition | Example |
|---|---|---|
| **Totipotent** | Can become **any cell type** including extraembryonic tissue (placenta) | **Zygote** and cells up to ~4-cell stage |
| **Pluripotent** | Can become **any cell type of the body** (all three germ layers) but NOT extraembryonic tissue | **Inner cell mass** of blastocyst (embryonic stem cells) |
| **Multipotent** | Can become **several related cell types** within a lineage | **Hematopoietic stem cells** (all blood cell types), **mesenchymal stem cells** (bone, cartilage, fat), **neural stem cells** |
| **Oligopotent** | Can become a **few cell types** | **Myeloid progenitor** (several types of white blood cells, but not lymphocytes) |
| **Unipotent** | Can become **only one cell type** but can still self-renew | **Spermatogonial stem cells**, **epidermal stem cells** (keratinocytes only) |

**Key concept:** As potency decreases, the cell becomes more **differentiated** (more specialized). Differentiation is driven by **differential gene expression** -- all cells have the same genome, but different genes are turned on/off via transcription factors, epigenetic modifications (DNA methylation, histone modifications), and signaling pathways.

### Embryonic Stem Cells (ESCs)

- Derived from the **inner cell mass (ICM)** of the **blastocyst** (day 5-6 embryo)
- **Pluripotent**: can differentiate into any cell type of the three germ layers (ectoderm, mesoderm, endoderm)
- Can be grown indefinitely in culture while maintaining pluripotency
- Ethical concerns: deriving ESCs destroys the blastocyst

### Adult (Somatic) Stem Cells

- Found in specific **niches** throughout the body
- Typically **multipotent** (more restricted than ESCs)
- Examples: hematopoietic stem cells (bone marrow), intestinal crypt stem cells, neural stem cells (subventricular zone, hippocampus), satellite cells (skeletal muscle)
- Function: replenish cells lost to normal turnover, injury, or disease

### Induced Pluripotent Stem Cells (iPSCs)

This was a breakthrough by **Shinya Yamanaka** (2006, Nobel Prize 2012).

**The concept:** Take a fully differentiated adult cell (like a skin fibroblast) and reprogram it back to a pluripotent state by introducing **four transcription factors** known as the **Yamanaka factors**:
- **Oct4**
- **Sox2**
- **Klf4**
- **c-Myc** (note: this is an oncogene, which raises safety concerns)

**Why iPSCs matter:**
- They bypass the ethical issues of ESCs (no embryo destruction)
- They can be derived from a **patient's own cells**, meaning tissues grown from them are **immunologically compatible** (no transplant rejection)
- Potential for personalized regenerative medicine, drug testing, and disease modeling

**MCAT connection:** iPSCs demonstrate that differentiation is **reversible** -- the genome of a differentiated cell still contains all the information needed for pluripotency. The difference between cell types is **epigenetic**, not genetic.

### Differentiation and Gene Expression

A few additional concepts the MCAT may test:

- **Determination:** The commitment of a cell to a particular fate before it shows visible differentiation. Determined cells look undifferentiated but are locked into a lineage.
- **Induction:** Signaling from one cell group that influences the developmental fate of neighboring cells (key concept in embryology).
- **Asymmetric division:** Stem cells often divide to produce one daughter that remains a stem cell (self-renewal) and one that differentiates. This maintains the stem cell pool.
- **Epigenetic regulation:** DNA methylation (generally silences genes), histone acetylation (generally activates genes), histone methylation (can activate or silence depending on which residue). These are heritable changes in gene expression without changes to the DNA sequence.

---

## High-Yield Summary Table

| Concept | Key Detail | MCAT Trap/Connection |
|---|---|---|
| G1/S checkpoint | Restriction point; most important | Rb/E2F pathway, Cyclin D-CDK4/6 |
| p53 | Guardian of the genome; activates p21, Bax | Lost in ~50% of cancers |
| Cyclin B-CDK1 | MPF; triggers mitotic entry | Phosphorylates lamins, condensins |
| Anaphase | APC/C degrades securin, separase cleaves cohesin | SAC failure causes aneuploidy |
| Apoptosis vs necrosis | Apoptosis = shrink, no inflammation; necrosis = swell, inflammation | DNA ladder vs smear |
| Intrinsic apoptosis | Bax/Bak pores, cytochrome c, apoptosome, caspase-9 | Cytochrome c moonlights from ETC |
| Extrinsic apoptosis | FasL/Fas, caspase-8 | T cell killing, negative selection |
| Oncogenes | Gain-of-function, dominant, one allele | Ras (stuck ON), Myc (overexpressed) |
| Tumor suppressors | Loss-of-function, two-hit hypothesis | p53, Rb, BRCA, APC |
| Telomerase | Maintains telomeres in cancer | Normal somatic cells lack it |
| Totipotent vs pluripotent | Totipotent = any cell + placenta; pluripotent = any body cell | Zygote vs ICM |
| iPSCs | Yamanaka factors: Oct4, Sox2, Klf4, c-Myc | Differentiation is reversible (epigenetic) |

---

*Study tip: When you see a cell division question on the MCAT, first identify what phase or checkpoint is involved, then think about which regulatory proteins are relevant. The exam rarely asks you to just name the phases -- it tests whether you understand the molecular logic of why a cell divides, stops, or dies.*
