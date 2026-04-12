# FC1B: Gene Expression -- Deep Dive Study Guide

**Section:** Bio/Biochem (BB)
**Foundational Concept 1B:** Gene Expression
**Kaplan References:** Biochem Ch 6-7, Bio Ch 1
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

## 3. Transcription

### Overview: DNA to mRNA

Transcription is the synthesis of RNA from a DNA template by **RNA polymerase**. Key differences from replication:

| Feature | Replication | Transcription |
|---------|-------------|---------------|
| Enzyme | DNA polymerase | RNA polymerase |
| Primer required? | Yes (RNA primer) | **No** -- RNA pol can initiate de novo |
| Template | Both strands copied | Only **template strand** (3'->5') copied |
| Product | DNA (deoxyribose, thymine) | RNA (ribose, **uracil** replaces thymine) |
| Proofreading | Yes (3'->5' exonuclease) | Limited (lower fidelity, but errors are less consequential since RNA is temporary) |

**Terminology trap:**
- **Template strand** (antisense strand): read 3'->5' by RNA pol
- **Coding strand** (sense strand, non-template): has the same sequence as the mRNA (except T instead of U). When the MCAT gives you a DNA sequence and asks for the mRNA, use the coding strand and swap T for U. If they give you the template strand, take the complement and swap T for U.

### Prokaryotic vs Eukaryotic Transcription

| Feature | Prokaryotes | Eukaryotes |
|---------|-------------|------------|
| RNA polymerase | Single RNA pol (one enzyme does it all) | **Three RNA pols:** RNA pol I (rRNA), RNA pol II (mRNA, snRNA), RNA pol III (tRNA, 5S rRNA) |
| Promoter recognition | **Sigma factor** binds directly to promoter (-10 and -35 regions) | **General transcription factors** (TFIID binds TATA box, then TFIIA, B, F, E, H assemble) |
| Coupled transcription/translation | **Yes** -- ribosomes begin translating mRNA while it is still being transcribed (no nucleus) | **No** -- transcription in nucleus, translation in cytoplasm. mRNA must be processed and exported first |
| mRNA processing | None (or minimal) | Extensive: 5' cap, 3' poly-A tail, splicing |

### Promoters and Transcription Factors

The **promoter** is the DNA sequence upstream of a gene where RNA polymerase binds and initiates transcription.

**In eukaryotes:**
- The **TATA box** (consensus sequence TATAAA) is located approximately **25-35 bp upstream** of the transcription start site
- **TFIID** (specifically its subunit **TBP**, TATA-binding protein) recognizes and binds the TATA box
- Other general transcription factors (TFIIA, B, F, E, H) assemble in a specific order, forming the **preinitiation complex** along with RNA pol II
- **TFIIH** has helicase activity (unwinds DNA at the start site) and kinase activity (phosphorylates the C-terminal domain of RNA pol II, allowing it to begin elongation and leave the promoter)

**Terminators:**
- In prokaryotes: **rho-dependent** (rho protein catches up to RNA pol and unwinds the RNA-DNA hybrid) or **rho-independent** (GC-rich palindrome forms a hairpin in the RNA, followed by a poly-U stretch that destabilizes the RNA-DNA hybrid)
- In eukaryotes: termination is coupled to **polyadenylation** -- cleavage at the poly-A signal (AAUAAA) triggers addition of the poly-A tail, and the remaining RNA still attached to polymerase is degraded, causing pol II to dissociate

### mRNA Processing (Eukaryotes Only)

Before leaving the nucleus, pre-mRNA undergoes three modifications:

**1. 5' Cap:**
- A **7-methylguanosine (m7G)** is added to the 5' end via an unusual **5'-5' triphosphate linkage**
- Functions: protects from exonuclease degradation, recognized by the ribosome for translation initiation, aids in nuclear export and splicing

**2. 3' Poly-A Tail:**
- **Poly-A polymerase** adds ~200 adenine nucleotides to the 3' end (no DNA template needed)
- Functions: protects from 3' exonuclease degradation, aids nuclear export, affects mRNA stability and translation efficiency
- Longer poly-A tail = more stable mRNA = more protein produced

**3. Splicing:**
- **Introns** (intervening sequences) are removed; **exons** (expressed sequences) are joined together
- Performed by the **spliceosome**, a large complex of **snRNPs** (small nuclear ribonucleoproteins, pronounced "snurps") and other proteins
- Intron removal follows precise signals: **GU at the 5' splice site**, **AG at the 3' splice site**, and a branch point adenosine (A) within the intron
- The mechanism involves two transesterification reactions forming a **lariat** intermediate

**Mnemonic:** "**EX**ons are **EX**pressed, **IN**trons are **IN**tervening (stay **IN** the nucleus)."

### Alternative Splicing

Different combinations of exons can be included or excluded in the final mRNA, meaning **one gene can produce multiple different proteins** (called **isoforms**). This is a major reason the human proteome (~100,000+ proteins) is much larger than the gene count (~20,000 genes).

**MCAT significance:** Alternative splicing is a form of **post-transcriptional gene regulation**. A passage might describe a tissue-specific protein variant -- think alternative splicing. It is also a known Kaplan gap, so study it independently.

---

## 4. Translation

### Ribosome Structure

Ribosomes are the molecular machines that translate mRNA into protein. They are made of **rRNA + protein**.

| Feature | Prokaryotic | Eukaryotic |
|---------|-------------|------------|
| Complete ribosome | **70S** | **80S** |
| Small subunit | **30S** (16S rRNA) | **40S** (18S rRNA) |
| Large subunit | **50S** (23S + 5S rRNA) | **60S** (28S + 5.8S + 5S rRNA) |
| Location | Free in cytoplasm | Free in cytoplasm OR bound to rough ER |

**MCAT trap:** Svedberg units (S) are NOT additive because they measure sedimentation rate, which depends on shape and size in a nonlinear way. 30S + 50S = 70S, not 80S. 40S + 60S = 80S, not 100S. Expect this as a "trick" answer choice.

**Clinical connection:** Mitochondria and chloroplasts have **70S ribosomes** (evidence for endosymbiotic theory). This is why certain antibiotics that target 70S ribosomes (e.g., chloramphenicol, tetracycline, aminoglycosides, macrolides) can have mitochondrial side effects but are safe to use against bacteria without destroying our 80S cytoplasmic ribosomes.

### tRNA and Aminoacyl-tRNA Synthetases

**tRNA** is the adapter molecule that "reads" the mRNA codon and delivers the correct amino acid. It has a **cloverleaf secondary structure** (2D) and an **L-shaped tertiary structure** (3D).

Key features:
- **Anticodon loop** -- three bases complementary to the mRNA codon (antiparallel pairing)
- **3' CCA acceptor stem** -- amino acid attaches here via an ester bond to the 3'-OH of the terminal adenosine
- Modified bases throughout (important for stability and function)

**Aminoacyl-tRNA synthetases** are the enzymes that "charge" tRNAs -- they attach the correct amino acid to the correct tRNA. There is **one synthetase for each amino acid** (20 total). This is where the actual translation of the genetic code happens. The ribosome just facilitates codon-anticodon base pairing; the synthetase is the one making the critical amino acid-tRNA match.

The charging reaction: **Amino acid + tRNA + ATP -> aminoacyl-tRNA + AMP + PPi**. The hydrolysis of PPi to 2 Pi drives the reaction forward (a total of 2 high-energy phosphate bonds consumed per amino acid loaded).

**MCAT trap:** If a question asks what determines which amino acid is incorporated into a protein, the answer is the **aminoacyl-tRNA synthetase**, not the ribosome. If you experimentally change the amino acid on a charged tRNA, the ribosome will incorporate the wrong amino acid because it only checks the codon-anticodon interaction.

### Wobble Base Pairing

The genetic code has 61 sense codons but only ~45 different tRNAs in most organisms. The discrepancy is resolved by **wobble**: the **3rd position of the codon** (which pairs with the **1st position of the anticodon**) allows non-standard base pairs. For example, inosine (I) in the anticodon can pair with U, C, or A in the codon.

This is why the third codon position is often **degenerate** -- mutations at this position frequently do not change the amino acid (**silent/synonymous mutations**).

### The Genetic Code

Key properties:
- **Universal** (nearly) -- same code in almost all organisms (minor exceptions: mitochondria, some protists)
- **Degenerate/redundant** -- most amino acids are encoded by more than one codon (e.g., leucine has 6 codons)
- **Unambiguous** -- each codon specifies only ONE amino acid
- **Non-overlapping** -- each nucleotide belongs to only one codon
- **Commaless** -- read continuously with no gaps; the reading frame is set by the start codon
- **Start codon: AUG** (methionine in eukaryotes, **fMet** [formyl-methionine] in prokaryotes)
- **Stop codons: UAA, UAG, UGA** -- do not code for amino acids; recognized by **release factors** (protein, not tRNA)

**Stop codon mnemonic:** U Are Annoying, U Are Gone, U Go Away.

### The Three Phases of Translation

**Initiation:**
1. The **small ribosomal subunit** binds the mRNA. In prokaryotes, the **Shine-Dalgarno sequence** (upstream of AUG) positions the ribosome. In eukaryotes, the **5' cap** is recognized and the ribosome scans until it finds the first AUG (**Kozak sequence** context helps).
2. The **initiator tRNA** (carrying Met or fMet) base-pairs with AUG in the **P site**
3. The **large subunit** joins, forming the complete ribosome with the initiator tRNA in the P site and an empty **A site**
4. Requires **initiation factors** and **GTP**

**Elongation:**
1. **Codon recognition:** A charged aminoacyl-tRNA enters the **A site** (aminoacyl site), guided by **EF-Tu** (prokaryotes) or **eEF-1A** (eukaryotes). Costs 1 GTP for proofreading.
2. **Peptide bond formation:** The **peptidyl transferase** activity of the large subunit rRNA (it is a **ribozyme** -- RNA, not protein, catalyzes this reaction) transfers the growing peptide chain from the tRNA in the P site to the amino acid on the tRNA in the A site.
3. **Translocation:** The ribosome shifts one codon toward the 3' end of the mRNA. The empty tRNA moves to the **E site** (exit) and leaves. The peptidyl-tRNA moves from A to P. Requires **EF-G** (prokaryotes) or **eEF-2** (eukaryotes) and 1 GTP.

**Energy cost per amino acid added:** 1 GTP (codon recognition) + 1 GTP (translocation) = **2 GTP per elongation cycle**. Plus 2 ATP equivalents for tRNA charging = **4 high-energy phosphate bonds total per amino acid**.

**Termination:**
1. A **stop codon** (UAA, UAG, UGA) enters the A site
2. **Release factors** (proteins shaped like tRNA) bind the stop codon
3. The peptidyl transferase activity hydrolyzes the bond between the polypeptide and the final tRNA, releasing the completed protein
4. Ribosomal subunits dissociate and can be recycled

**MCAT tip:** Peptidyl transferase is a **ribozyme** -- the catalytic activity comes from rRNA, not protein. This supports the **RNA world hypothesis** (RNA preceded proteins in evolution). This is a favorite MCAT topic.

### Post-Translational Modifications (PTMs)

After (or during) translation, proteins are modified to become functional:

| Modification | What Happens | Purpose |
|-------------|-------------|---------|
| **Phosphorylation** | Kinase adds phosphate group (usually to Ser, Thr, Tyr) | Signal transduction, enzyme activation/deactivation |
| **Glycosylation** | Sugar chains added (N-linked in ER, O-linked in Golgi) | Protein folding, stability, cell signaling, targeting |
| **Ubiquitination** | Ubiquitin tags added (poly-ubiquitin) | Marks for destruction by **proteasome** |
| **Proteolytic cleavage** | Precursor protein is cut | Activation of zymogens (e.g., trypsinogen -> trypsin), insulin processing |
| **Lipid modification** | Lipid groups attached (prenylation, myristoylation) | Membrane anchoring |
| **Disulfide bond formation** | Cysteine residues oxidized | Stabilizes extracellular proteins (occurs in ER) |
| **Acetylation** | Acetyl group added (often N-terminal or lysine) | Histone regulation, protein stability |
| **Methylation** | Methyl group added | Histone regulation, signaling |

---

## 5. Gene Regulation

### Prokaryotic Gene Regulation: Operons

Prokaryotes organize related genes into **operons** -- clusters of genes under a single promoter, producing a **polycistronic mRNA** (one mRNA encoding multiple proteins). This allows coordinated regulation.

#### The Lac Operon (Inducible System)

The lac operon encodes enzymes for **lactose metabolism**: **lacZ** (beta-galactosidase, cleaves lactose into glucose + galactose), **lacY** (permease, transports lactose in), and **lacA** (transacetylase).

**Components:**
- **Promoter** -- where RNA pol binds
- **Operator** -- where the repressor binds (between promoter and structural genes)
- **lacI gene** -- constitutively expressed; encodes the **lac repressor**

**Regulation has two levels -- you need BOTH for full expression:**

**1. Negative control (repressor):**
- **No lactose:** The lac repressor binds the operator, physically blocking RNA polymerase. Genes are OFF.
- **Lactose present:** **Allolactose** (an isomer of lactose) binds the repressor, causing a conformational change that releases it from the operator. RNA polymerase can now transcribe. Genes are ON (if glucose is absent).

**2. Positive control (CAP-cAMP):**
- **Glucose absent:** cAMP levels are HIGH (because adenylyl cyclase is active). cAMP binds to **CAP (catabolite activator protein)**. The CAP-cAMP complex binds upstream of the promoter and **enhances** RNA polymerase binding. Transcription is maximal.
- **Glucose present:** cAMP levels are LOW. CAP cannot bind. Even without the repressor, RNA pol binds weakly. Transcription is low.

**The four conditions:**

| Glucose | Lactose | cAMP | Repressor | Transcription |
|---------|---------|------|-----------|---------------|
| + | - | Low | On operator | **OFF** (no inducer, no CAP) |
| + | + | Low | Released | **LOW** (basal -- no CAP boost) |
| - | - | High | On operator | **OFF** (repressor blocks) |
| **-** | **+** | **High** | **Released** | **MAXIMAL** (both controls active) |

**MCAT trap:** The most common mistake is thinking lactose alone is sufficient for full expression. You need lactose present (to remove repressor) AND glucose absent (to activate CAP). The cell preferentially uses glucose -- this is called **catabolite repression** or the **glucose effect**.

#### The Trp Operon (Repressible System)

The trp operon encodes enzymes for **tryptophan biosynthesis**. It works in the opposite direction:

- **Tryptophan absent:** The repressor protein is **inactive** (cannot bind operator). Genes are ON -- the cell makes its own tryptophan.
- **Tryptophan present:** Tryptophan acts as a **corepressor** -- it binds to the repressor protein, activating it. The activated repressor binds the operator, blocking transcription. Genes are OFF -- no need to synthesize what is already available.

**Additional regulation -- attenuation:** The trp operon has a **leader sequence** that can form a hairpin terminator when tryptophan-charged tRNAs are abundant, causing premature termination. When tryptophan is scarce, ribosomes stall on the leader sequence, preventing terminator formation, allowing transcription to continue. This is a fine-tuning mechanism on top of repressor control.

**Key distinction:** Lac = inducible (substrate turns genes ON). Trp = repressible (product turns genes OFF). Both use negative control (repressor binding operator = genes off).

### Eukaryotic Gene Regulation

Eukaryotic regulation is far more complex, occurring at **every level** from chromatin structure to protein degradation.

**1. Epigenetic / Chromatin level:**
- **DNA methylation** (at CpG dinucleotides by DNA methyltransferases): adds methyl group to cytosine. Generally **silences** gene expression. Methylation patterns can be inherited across cell divisions (maintenance methylation). Important in X-inactivation, genomic imprinting, and cancer (tumor suppressor hypermethylation).
- **Histone acetylation** (by HATs -- histone acetyltransferases): neutralizes positive charges on lysine residues of histones, weakening histone-DNA interaction, opening chromatin. **Activates** transcription. Reversed by **HDACs** (histone deacetylases).
- **Histone methylation**: can be activating OR silencing depending on which residue is methylated. H3K4me3 = active. H3K9me3 = silent. H3K27me3 = silent. (This level of detail is lower-yield but shows up in passages.)
- **Chromatin remodeling complexes** (e.g., SWI/SNF): use ATP to reposition nucleosomes, exposing or hiding promoter regions.

**2. Transcriptional level:**
- **Transcription factors (TFs):** proteins that bind specific DNA sequences and either recruit or block RNA pol II. **Activators** bind **enhancers** (can be thousands of bp away from the promoter -- DNA looping brings them close). **Repressors** bind **silencers**.
- **Enhancers and silencers:** regulatory sequences that can be upstream, downstream, or even within introns. They function regardless of orientation. Enhancers work through **mediator complexes** that bridge the activator to the general transcription machinery.
- **Combinatorial control:** A given gene is regulated by multiple TFs simultaneously. The specific combination of active TFs determines whether a gene is expressed -- this allows ~1,500 TFs to regulate ~20,000 genes in diverse patterns across cell types.

**3. Post-transcriptional level:**
- **Alternative splicing** (discussed above)
- **mRNA stability**: longer poly-A tail = more stable. AU-rich elements (AREs) in the 3' UTR promote degradation. mRNA half-life ranges from minutes to days.
- **miRNA (microRNA):** small ~22 nt RNA molecules that bind complementary sequences in the 3' UTR of target mRNAs. Result: **mRNA degradation or translational repression**. One miRNA can regulate hundreds of genes.
- **siRNA (small interfering RNA):** similar mechanism but typically from exogenous double-stranded RNA (viral defense, experimental tool). Processed by **Dicer** into ~21 nt fragments, loaded into **RISC (RNA-induced silencing complex)**, which degrades complementary mRNA.
- **RNA interference (RNAi)** is the umbrella term for miRNA and siRNA-mediated silencing.

**4. Translational and post-translational level:**
- Regulation of initiation factor activity (e.g., phosphorylation of eIF2 blocks translation under stress)
- **Ubiquitin-proteasome pathway** controls protein turnover: proteins tagged with poly-ubiquitin chains are fed into the **26S proteasome** and degraded into peptides

**MCAT tip:** Passages often describe a novel regulatory mechanism and ask you to identify what level of regulation it represents. The answer framework: is it affecting DNA accessibility? Transcription initiation? mRNA processing/stability? Translation rate? Protein degradation? Know examples at each level.

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

## High-Yield Summary Table

| Topic | Must-Know Fact | Common Trap |
|-------|---------------|-------------|
| Base pairing | G-C = 3 H-bonds, A-T = 2 | Chargaff's rules only apply to dsDNA |
| Replication direction | All DNA pol = 5'->3' only | Do not confuse synthesis direction with proofreading direction (3'->5') |
| Meselson-Stahl | Gen 1 = all intermediate density | This eliminates conservative, not dispersive (need gen 2 for that) |
| Telomerase | Reverse transcriptase with own RNA template | Active in cancer/stem cells, not most somatic cells |
| RNA pol vs DNA pol | RNA pol needs NO primer | DNA pol absolutely requires a primer (RNA primer from primase) |
| Template vs coding strand | mRNA matches coding strand (with U for T) | If given template strand, complement it first |
| Svedberg units | 30S + 50S = 70S (not additive) | 40S + 60S = 80S, not 100S |
| Aminoacyl-tRNA synthetase | Determines which AA goes on which tRNA | The ribosome does NOT select the amino acid |
| Peptidyl transferase | It is a ribozyme (rRNA) | Not a protein enzyme |
| Lac operon maximal expression | Need lactose present AND glucose absent | Lactose alone gives only basal expression |
| DNA methylation | Silences genes | Histone acetylation activates genes |
| PCR primer need | DNA template, two primers, dNTPs, Taq, Mg2+ | Taq has no proofreading |
| RT-PCR vs qPCR | RT = reverse transcription, q = quantitative | RT-PCR is NOT real-time PCR |
| SNoW DRoP | Southern-DNA, Northern-RNA, Western-Protein | Western uses antibodies, not nucleic acid probes |

---

## MCAT Strategy Notes for FC1B

1. **Passage-based questions** in this area often describe an experiment and ask you to interpret gel results, predict operon behavior under new conditions, or identify a mutation type. Practice reading gel images and restriction maps.

2. **Discrete questions** frequently test enzyme functions in replication (which enzyme does X?), the genetic code (reading a codon table), and regulation logic (what happens to lac operon expression if you mutate the operator so the repressor cannot bind?).

3. **Cross-topic connections:**
   - Gene expression connects to **cancer biology** (oncogenes, tumor suppressors, telomerase)
   - Epigenetics connects to **development and cell differentiation** (PS section: nature vs nurture)
   - Biotechnology connects to **experimental design** (Research Methods) -- know what each technique measures and when you would use it
   - Antibiotics targeting bacterial ribosomes (70S) connect to **microbiology** and explain selective toxicity

4. **Error analysis:** If you miss questions in this area, categorize your mistakes:
   - Did you confuse template vs coding strand? (Content gap)
   - Did you misread a gel image? (Practice gap -- do more passage-based work)
   - Did you not know what an enzyme does? (Memorization gap -- Anki it)
   - Did you understand the concept but pick the wrong answer? (Reasoning/elimination gap)
