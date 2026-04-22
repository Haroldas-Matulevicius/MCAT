# BB Chapter 7 — RNA & Genetic Code

Scope: Genetic code, transcription, translation, prokaryotic and eukaryotic gene regulation.

**Section:** Bio/Biochem (BB)
**AAMC FC mapping:** FC1B (Gene Expression)
**Kaplan Reference:** Biochemistry Chapter 7

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

## High-Yield Summary Table (Ch 7)

| Topic | Must-Know Fact | Common Trap |
|-------|---------------|-------------|
| RNA pol vs DNA pol | RNA pol needs NO primer | DNA pol absolutely requires a primer (RNA primer from primase) |
| Template vs coding strand | mRNA matches coding strand (with U for T) | If given template strand, complement it first |
| Svedberg units | 30S + 50S = 70S (not additive) | 40S + 60S = 80S, not 100S |
| Aminoacyl-tRNA synthetase | Determines which AA goes on which tRNA | The ribosome does NOT select the amino acid |
| Peptidyl transferase | It is a ribozyme (rRNA) | Not a protein enzyme |
| Lac operon maximal expression | Need lactose present AND glucose absent | Lactose alone gives only basal expression |
| DNA methylation | Silences genes | Histone acetylation activates genes |

---

## MCAT Strategy Notes for Gene Expression (FC1B)

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

→ DNA structure, replication, biotech: see Ch 6
