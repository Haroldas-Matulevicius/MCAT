# BB Chapter 6 — DNA & Biotechnology

Scope: DNA structure, eukaryotic chromosome organization, DNA replication, DNA repair, recombinant DNA / biotech techniques.

**Section:** Bio/Biochem (BB)
**AAMC FC mapping:** FC1B (Gene Expression)
**Kaplan Reference:** Biochemistry Chapter 6
**Yield:** Extremely high -- DNA/RNA/protein questions appear on virtually every MCAT

---

## 1. DNA Structure and Organization

### The Double Helix

DNA is a **double-stranded polymer** of nucleotides. Each nucleotide has three parts: a **deoxyribose sugar**, a **phosphate group**, and a **nitrogenous base**. The backbone is formed by **phosphodiester bonds** linking the 3' hydroxyl of one sugar to the 5' phosphate of the next. This means each strand has inherent **directionality** -- a 5' end (free phosphate) and a 3' end (free hydroxyl).

The two strands run **antiparallel**: one strand runs 5'->3' while the complementary strand runs 3'->5'. This is not just a structural detail -- it has massive functional consequences for replication (leading vs lagging strand problems exist entirely because of antiparallel orientation).

**Base pairing rules (Watson-Crick):**
- **Adenine pairs with Thymine** via **2 hydrogen bonds**
- **Guanine pairs with Cytosine** via **3 hydrogen bonds**
- Purines (A, G) always pair with pyrimidines (T, C) -- this keeps the helix width uniform

**MCAT trap:** Higher G-C content = higher melting temperature (Tm). Three H-bonds per G-C pair vs two per A-T pair means more energy is needed to separate the strands. If a passage describes DNA with a high Tm, think high G-C content. Also, Chargaff's rules: %A = %T and %G = %C in double-stranded DNA. This does NOT hold for single-stranded DNA or RNA.

### Major and Minor Grooves

The double helix is not symmetrical -- it creates two grooves of different widths. The **major groove** is wider and exposes more of the base pair edges, making specific base pairs identifiable from the groove surface without unwinding the helix. The **minor groove** is narrower and provides less chemical information.

**Why proteins bind the major groove:** Transcription factors, repressors, and other DNA-binding proteins need to "read" the DNA sequence to find their target sites. The major groove presents a unique pattern of hydrogen bond donors, acceptors, and hydrophobic patches for each base pair. In the minor groove, A-T and T-A look nearly identical, as do G-C and C-G, so sequence recognition is ambiguous. The major groove gives proteins enough chemical information to distinguish specific sequences without melting the DNA.

**MCAT relevance:** If a passage describes a protein recognizing a specific DNA sequence, it is almost certainly binding the major groove. Minor groove binding proteins exist (some drugs, histones) but sequence-specific recognition = major groove.

### Chromosome Organization

DNA must be packaged efficiently -- the human genome is roughly 2 meters of DNA crammed into a nucleus about 6 micrometers wide. The packaging hierarchy:

1. **Bare DNA** (~2 nm diameter) -- the naked double helix
2. **Nucleosomes** (~11 nm) -- DNA wraps ~1.65 turns (about 147 bp) around a **histone octamer** (two copies each of H2A, H2B, H3, H4). The linker histone **H1** sits at the entry/exit point and stabilizes the wrap. This "beads on a string" structure is the first level of compaction.
3. **30 nm fiber** -- nucleosomes coil into a more compact fiber (exact structure debated, but the MCAT treats it as established)
4. **Looped domains** (~300 nm) -- the 30 nm fiber forms loops anchored to a **protein scaffold**
5. **Metaphase chromosome** (~1400 nm) -- maximally condensed during mitosis, visible under light microscope

**MCAT tip:** You need to know the hierarchy and approximate sizes. The key principle: more condensation = less accessible for transcription.

### Heterochromatin vs Euchromatin

This distinction is directly tied to gene regulation:

- **Heterochromatin** -- tightly packed, transcriptionally **silent**. The DNA is too condensed for RNA polymerase and transcription factors to access. Examples: centromeres, telomeres, Barr body (inactivated X chromosome). There are two subtypes:
  - **Constitutive heterochromatin** -- always condensed (centromeres, telomeres). Never transcribed.
  - **Facultative heterochromatin** -- conditionally condensed. Can be converted to euchromatin when those genes need to be expressed. This is the basis of epigenetic regulation.
- **Euchromatin** -- loosely packed, transcriptionally **active** (or at least accessible). This is where most gene expression occurs.

**The connection:** Histone modifications control the switch. **Acetylation of histones** (by histone acetyltransferases, HATs) loosens DNA-histone interactions by neutralizing the positive charge on lysine residues, converting heterochromatin to euchromatin and **activating** transcription. **Deacetylation** (by HDACs) reverses this, silencing genes. **DNA methylation** (adding -CH3 to cytosine, typically at CpG islands) recruits proteins that condense chromatin and **silences** transcription.

**Mnemonic:** Acetylation = Activation. Methylation (of DNA) = Muting.

---

## 2. DNA Replication

### Semiconservative Replication

Each daughter DNA molecule contains **one original (parent) strand and one newly synthesized strand**. This was proven by the **Meselson-Stahl experiment** (1958):

1. Grew *E. coli* in medium with **heavy nitrogen (15-N)** until all DNA was "heavy-heavy" (HH)
2. Switched to **light nitrogen (14-N)** medium and let cells divide
3. After **one generation**: all DNA was **intermediate density** (HL) -- one heavy strand, one light strand. This ruled out **conservative** replication (which would have produced one HH and one LL).
4. After **two generations**: half intermediate (HL), half light (LL). This ruled out **dispersive** replication (which would have produced all molecules at intermediate density, gradually getting lighter).

**MCAT trap:** You might see a passage describing a density gradient centrifugation experiment. Recognize the Meselson-Stahl setup. The key result: generation 1 = all intermediate density. That single observation eliminates conservative replication.

### The Replication Fork -- Enzyme by Enzyme

Replication begins at an **origin of replication** (prokaryotes have one, eukaryotes have many -- this speeds up replication of much larger genomes). The fork is **bidirectional**: two replication forks move in opposite directions from each origin.

| Enzyme | Function | Key Details |
|--------|----------|-------------|
| **Helicase** | Unwinds the double helix by breaking H-bonds | Uses ATP; creates the replication fork |
| **Single-strand binding proteins (SSBs)** | Stabilize unwound single-stranded DNA | Prevent re-annealing and degradation by nucleases |
| **Topoisomerase** (gyrase in prokaryotes) | Relieves supercoiling ahead of the replication fork | Cuts and rejoins DNA strands; target of fluoroquinolone antibiotics |
| **Primase** | Synthesizes short **RNA primers** (~10 nt) | DNA polymerase CANNOT start from scratch -- it can only add to an existing 3'-OH |
| **DNA polymerase III** (prokaryotes) | Main replication enzyme; extends the primer with deoxyribonucleotides | Synthesizes 5'->3'; has **3'->5' proofreading** (exonuclease) activity |
| **DNA polymerase I** | Removes RNA primers and replaces them with DNA | Has 5'->3' exonuclease activity (removes primers) AND polymerase activity (fills gaps) |
| **DNA ligase** | Seals **nicks** (gaps in the phosphodiester backbone) | Joins Okazaki fragments on lagging strand; joins where pol I finished filling |

**Critical concept:** All DNA polymerases synthesize in the **5' to 3' direction only**. They add nucleotides to the **3'-OH** of the growing strand. They CANNOT synthesize 3' to 5'. This single constraint creates the entire leading/lagging strand problem.

### Leading vs Lagging Strand

Because the two template strands are antiparallel and DNA pol can only synthesize 5'->3':

- **Leading strand:** Template runs 3'->5', so the new strand is synthesized 5'->3' **continuously** in the direction of fork movement. Needs only **one primer**.
- **Lagging strand:** Template runs 5'->3', so synthesis must go **away from the fork**. It is synthesized in short fragments called **Okazaki fragments** (~1000-2000 nt in prokaryotes, ~100-200 nt in eukaryotes). Each fragment needs its own RNA primer. These are later processed: **DNA pol I** removes primers and fills gaps, and **ligase** seals the remaining nicks.

**Why Okazaki fragments exist:** The lagging strand template is oriented such that continuous synthesis would require 3'->5' polymerization, which no known DNA polymerase can do. The cell's solution: synthesize in short 5'->3' bursts moving backward, then stitch them together.

### Telomeres and Telomerase

**The end-replication problem:** At the very end of a linear chromosome, when the last RNA primer on the lagging strand is removed, DNA pol I cannot fill the gap because there is no upstream 3'-OH to extend from. Each round of replication therefore **shortens the chromosome slightly**.

**Telomeres** are repetitive, non-coding sequences (TTAGGG in humans, repeated thousands of times) at chromosome ends. They act as a **disposable buffer** -- their gradual loss does not sacrifice coding DNA.

**Telomerase** is a **reverse transcriptase** (it carries its own RNA template) that extends the 3' overhang of the telomere, allowing primase and DNA pol to fill in the complementary strand. It maintains telomere length.

**MCAT connections:**
- **Aging:** Most somatic cells lack telomerase. Telomere shortening acts as a "molecular clock" -- after enough divisions, critically short telomeres trigger **senescence** (cell cycle arrest) or apoptosis. This is the Hayflick limit.
- **Cancer:** ~90% of cancers reactivate telomerase, enabling unlimited proliferation (one of the hallmarks of cancer). Telomerase inhibitors are being explored as anti-cancer drugs.
- **Stem cells and germ cells:** Express telomerase to maintain their telomeres across many divisions.

### DNA Repair Mechanisms

The MCAT expects you to distinguish three major repair systems:

**Mismatch repair (MMR):**
- Fixes **base-base mismatches** and **insertion/deletion loops** that escaped proofreading
- The system distinguishes the newly synthesized strand from the template (in prokaryotes, by **methylation** -- the template strand is methylated, the new strand is not yet). It nicks the unmethylated strand, excises the error, and resynthesizes
- Defects cause **hereditary nonpolyposis colorectal cancer (Lynch syndrome)**

**Base excision repair (BER):**
- Fixes **damaged or abnormal bases** (e.g., deamination of cytosine to uracil, oxidative damage)
- A **DNA glycosylase** recognizes and removes the damaged base, creating an **AP site** (apurinic/apyrimidinic site). An **AP endonuclease** nicks the backbone. DNA pol fills in, ligase seals
- Handles single-base damage events

**Nucleotide excision repair (NER):**
- Fixes **bulky, helix-distorting lesions** such as **thymine dimers** (caused by UV radiation) and chemical adducts
- An endonuclease complex cuts the damaged strand on both sides of the lesion, removing a ~12-13 nt (prokaryotes) or ~24-32 nt (eukaryotes) patch. DNA pol fills, ligase seals
- Defects cause **xeroderma pigmentosum** (extreme UV sensitivity, high skin cancer risk)

**MCAT tip:** If a question describes UV exposure and DNA damage, think thymine dimers and NER. If it describes spontaneous deamination, think BER. If it asks about replication errors that slip past proofreading, think mismatch repair.

---

## 6. Biotechnology

### PCR (Polymerase Chain Reaction)

PCR amplifies a specific DNA sequence exponentially in vitro. Three steps per cycle, repeated 25-40 times:

1. **Denaturation (94-98C):** Heat separates the double-stranded DNA into single strands
2. **Annealing (50-65C):** Short DNA **primers** (designed to flank the target sequence) bind to complementary sequences on each strand
3. **Extension (72C):** **Taq polymerase** (from *Thermus aquaticus*, a thermophilic bacterium) extends the primers, synthesizing new DNA

**Why Taq?** It is heat-stable. Normal DNA pol would be denatured at 95C during the denaturation step. Taq survives repeated heating cycles.

**Amplification math:** After n cycles, you get approximately **2^n copies** of the target. After 20 cycles: ~1 million copies. After 30 cycles: ~1 billion. This is why PCR is so sensitive -- in theory, it can amplify from a single DNA molecule.

**MCAT trap:** Taq polymerase lacks 3'->5' proofreading activity, so PCR products have a higher error rate than in vivo replication. If a passage discusses error rates in amplified DNA, this is why.

**What you need for PCR:** template DNA, two primers, Taq polymerase, dNTPs (dATP, dTTP, dGTP, dCTP), buffer with Mg2+.

### RT-PCR and qPCR

**RT-PCR (Reverse Transcription PCR):**
- First step: **reverse transcriptase** converts mRNA into **cDNA** (complementary DNA)
- Then standard PCR amplifies the cDNA
- Purpose: detect and amplify **RNA** sequences. Used to study gene expression (is this gene being transcribed?)
- The cDNA has no introns (because it was made from processed mRNA)

**qPCR (Quantitative PCR / Real-Time PCR):**
- PCR with **fluorescent reporters** that increase in signal as product accumulates
- Measures DNA amount **in real time** during amplification
- The **threshold cycle (Ct)** is the cycle number at which fluorescence crosses a set threshold. Lower Ct = more starting template
- Can be combined with RT (RT-qPCR) to **quantify** specific mRNA levels -- the gold standard for measuring gene expression levels

**MCAT trap:** "RT-PCR" stands for reverse transcription PCR, NOT real-time PCR. Real-time PCR = qPCR. These are commonly confused.

### Blotting Techniques

**Mnemonic: SNoW DRoP** -- Southern/Northern/Western for DNA/RNA/Protein

| Technique | Target | Probe/Detection | Key Steps |
|-----------|--------|-----------------|-----------|
| **Southern blot** | **DNA** | Labeled DNA probe (complementary to target) | Digest DNA with restriction enzymes -> gel electrophoresis -> transfer to membrane -> hybridize with probe -> detect |
| **Northern blot** | **RNA** | Labeled nucleic acid probe | Extract RNA -> gel electrophoresis -> transfer to membrane -> hybridize -> detect. Tells you mRNA size and expression level |
| **Western blot** | **Protein** | **Antibodies** (primary Ab binds target, secondary Ab binds primary and carries detection label) | SDS-PAGE -> transfer to membrane -> block -> primary Ab -> secondary Ab -> detect. Tells you protein size and expression |

**MCAT tip:** Southern was named after Edwin Southern. Northern and Western are puns on the name, not compass directions. A "Southwestern blot" (yes, it exists) detects DNA-binding proteins.

### Gel Electrophoresis

- **Agarose gel:** Used for DNA and RNA. Molecules migrate toward the **positive electrode** (DNA/RNA are negatively charged due to phosphate backbone). **Smaller fragments migrate farther** (they pass through the gel pores more easily).
- **SDS-PAGE:** Used for proteins. SDS denatures proteins and coats them with uniform negative charge, so separation is by **molecular weight only**. Smaller proteins migrate farther.
- **Native PAGE:** No SDS. Proteins separate by charge, size, and shape. Used when you want to preserve native structure/activity.

**MCAT math:** In agarose gel, you may need to predict fragment sizes from a restriction digest. Count base pairs between cut sites on a map. Fragments are typically visualized using **ethidium bromide** (intercalates DNA, fluoresces under UV) or safer alternatives like SYBR dyes.

### Restriction Enzymes and Cloning

**Restriction enzymes (restriction endonucleases):** Cut DNA at specific **palindromic recognition sequences** (read the same 5'->3' on both strands).

Two types of cuts:
- **Sticky ends:** Staggered cuts leaving single-stranded overhangs. These can base-pair with complementary sticky ends from other DNA fragments, making them ideal for cloning.
- **Blunt ends:** Straight cuts, no overhangs. Less efficient for ligation but can join any two blunt-ended fragments.

**Cloning workflow:**
1. Cut target gene and **vector** (plasmid) with the **same restriction enzyme** (producing compatible sticky ends)
2. Mix and ligate with **DNA ligase**
3. Transform into host bacteria (e.g., electroporation, heat shock)
4. Select for successful transformants using **selectable markers** (antibiotic resistance gene on the plasmid)
5. Screen for correct insert (blue-white screening with lacZ, colony PCR, restriction analysis)

### CRISPR-Cas9

A revolutionary **gene-editing** tool adapted from a bacterial immune system:
- A **guide RNA (gRNA)** is designed to be complementary to the target DNA sequence
- **Cas9** (an endonuclease) is directed to the target by the gRNA, where it creates a **double-strand break (DSB)**
- The cell repairs the DSB by either **non-homologous end joining (NHEJ)** -- error-prone, often disrupts the gene -- or **homology-directed repair (HDR)** -- if a template is provided, precise edits can be introduced

**MCAT relevance:** CRISPR appears in passages describing experimental gene knockouts, gene therapy, or ethical discussions about germline editing. Know the mechanism and the difference between NHEJ (disrupts gene) and HDR (precise correction).

### Sanger Sequencing

Also called **chain termination sequencing** or **dideoxy sequencing**:
- Uses **ddNTPs (dideoxynucleoside triphosphates)** -- these lack the 3'-OH needed for the next phosphodiester bond, so incorporation of a ddNTP **terminates the growing chain**
- Reaction contains normal dNTPs + a small amount of fluorescently labeled ddNTPs
- Result: fragments of every possible length, each terminated with a labeled ddNTP
- Fragments are separated by capillary electrophoresis, and the fluorescent label at each position reveals the base
- Read the sequence from shortest to longest fragment

### Microarrays (DNA/Gene Chips)

- A chip with thousands of known DNA sequences (**probes**) attached at specific positions
- Fluorescently labeled cDNA (made from mRNA of interest) is hybridized to the chip
- Spots that light up indicate genes that are being expressed
- Used for **genome-wide expression profiling** -- comparing gene expression between two conditions (e.g., cancer vs normal tissue)

### ELISA (Enzyme-Linked Immunosorbent Assay)

Detects and quantifies a specific **protein (antigen) or antibody** in a sample using antibody-enzyme conjugates:

| Type | Setup | Use |
|------|-------|-----|
| **Direct** | Antigen bound to plate -> enzyme-linked primary antibody detects it | Simplest; detect antigen |
| **Indirect** | Antigen bound -> unlabeled primary Ab -> enzyme-linked secondary Ab | Detect antibodies in patient serum (e.g., HIV test) |
| **Sandwich** | Capture Ab on plate -> binds antigen from sample -> detection Ab (enzyme-linked) -> signal | Most sensitive; quantify antigen in solution (e.g., pregnancy test measures hCG) |

**MCAT tip:** Sandwich ELISA is the most commonly tested. The key concept: two antibodies "sandwich" the antigen. One captures, one detects. Signal intensity is proportional to antigen concentration.

### FISH (Fluorescence In Situ Hybridization)

- A **fluorescently labeled DNA probe** hybridizes to a specific chromosomal location in **intact cells or tissue sections**
- Visualized under fluorescence microscopy
- Used to: detect chromosomal abnormalities (translocations, deletions, duplications), map genes to chromosomes, diagnose genetic disorders, identify specific species in mixed microbial communities

**Key distinction from blotting:** FISH works on intact cells/chromosomes (in situ = "in place"), preserving spatial information. Southern blot works on extracted, purified DNA.

---

## High-Yield Summary Table (Ch 6)

| Topic | Must-Know Fact | Common Trap |
|-------|---------------|-------------|
| Base pairing | G-C = 3 H-bonds, A-T = 2 | Chargaff's rules only apply to dsDNA |
| Replication direction | All DNA pol = 5'->3' only | Do not confuse synthesis direction with proofreading direction (3'->5') |
| Meselson-Stahl | Gen 1 = all intermediate density | This eliminates conservative, not dispersive (need gen 2 for that) |
| Telomerase | Reverse transcriptase with own RNA template | Active in cancer/stem cells, not most somatic cells |
| PCR primer need | DNA template, two primers, dNTPs, Taq, Mg2+ | Taq has no proofreading |
| RT-PCR vs qPCR | RT = reverse transcription, q = quantitative | RT-PCR is NOT real-time PCR |
| SNoW DRoP | Southern-DNA, Northern-RNA, Western-Protein | Western uses antibodies, not nucleic acid probes |

→ Transcription, translation, gene regulation: see Ch 7
