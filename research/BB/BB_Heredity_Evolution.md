# FC1C: Heredity and Genetic Diversity -- Deep Dive

> BB section | Kaplan Biology Ch. 12 (Genetics & Evolution) | High-yield for MCAT

---

## 1. Mendelian Genetics

### Law of Segregation

Every diploid organism carries **two alleles** for each gene -- one from mom, one from dad. During **meiosis I**, homologous chromosomes separate so that each gamete receives only **one allele** per gene.

**Mechanistic basis:** Homologous chromosomes pair up during prophase I and are pulled to opposite poles during anaphase I. The result is that each haploid gamete carries a single copy of every gene.

**MCAT takeaway:** Segregation explains why a heterozygote (Aa) produces gametes that are 50% A and 50% a -- not some blended intermediate.

### Law of Independent Assortment

Genes on **different chromosomes** sort independently during meiosis I. The orientation of one homologous pair on the metaphase plate has no effect on the orientation of another pair.

**Mechanistic basis:** At metaphase I, the way maternal and paternal chromosomes line up is random. With 23 homologous pairs in humans, there are **2^23 (~8.4 million)** possible gamete combinations from independent assortment alone.

**Critical caveat:** Independent assortment applies only to genes on **different chromosomes** (or genes far apart on the same chromosome). Linked genes violate this law -- covered below under genetic linkage.

### Punnett Squares and Test Crosses

A **Punnett square** is a grid that predicts offspring genotype and phenotype ratios by crossing the gametes of two parents.

**How to set one up:**
1. Determine the genotype of each parent.
2. List all possible gametes for each parent along the edges.
3. Fill in each box by combining the row gamete with the column gamete.
4. Count genotype and phenotype ratios.

**Worked example -- Monohybrid cross:**

Cross: Aa x Aa

|  | **A** | **a** |
|--|-------|-------|
| **A** | AA | Aa |
| **a** | Aa | aa |

- Genotype ratio: 1 AA : 2 Aa : 1 aa
- Phenotype ratio: **3 dominant : 1 recessive** (the classic 3:1 ratio)

**Test cross:** Cross the organism of unknown genotype with a **homozygous recessive** (aa). If any offspring show the recessive phenotype, the unknown parent must be heterozygous (Aa). If all offspring are dominant, the parent is likely homozygous dominant (AA) -- though you need a large sample size to be confident.

### Dihybrid Cross (9:3:3:1)

**Worked example:** AaBb x AaBb

Each parent produces 4 gamete types: AB, Ab, aB, ab (all equally likely -- this requires independent assortment).

The resulting 4x4 Punnett square gives:
- **9** A_B_ (both dominant)
- **3** A_bb (first dominant, second recessive)
- **3** aaB_ (first recessive, second dominant)
- **1** aabb (both recessive)

**When 9:3:3:1 does NOT hold:**
- Genes are **linked** (on the same chromosome)
- **Epistasis** -- one gene masks the other (modifies the ratio, e.g., 9:3:4 or 12:3:1)
- **Lethal alleles** -- certain genotypes are inviable (e.g., 2:1 instead of 3:1 in a monohybrid)
- **Non-Mendelian inheritance** patterns (incomplete dominance, codominance)

### Dominant vs Recessive -- Molecular Basis

**Dominant allele:** Usually encodes a functional protein. One working copy is often enough to produce the wild-type phenotype (the cell makes sufficient protein from one allele).

**Recessive allele:** Usually encodes a nonfunctional or absent protein. The phenotype only shows when **both** copies are nonfunctional (homozygous recessive) because there's no working copy to compensate.

**Why this matters for MCAT:** Many genetic diseases are autosomal recessive (CF, sickle cell, PKU) because carriers (heterozygotes) still make enough functional protein from their one good allele.

**Exception -- Dominant negative:** Some mutant proteins actively interfere with the normal protein's function, causing a dominant disease phenotype even in heterozygotes (e.g., some collagen mutations in osteogenesis imperfecta).

---

## 2. Non-Mendelian Genetics

### Incomplete Dominance

The heterozygote has a **blended, intermediate** phenotype between the two homozygotes.

**Classic example -- Snapdragons:**
- RR = red flowers
- R'R' = white flowers
- RR' = **pink** flowers (intermediate)

**Molecular explanation:** One copy of the functional allele produces only half the normal amount of pigment, resulting in a lighter color.

**Cross ratios:** RR' x RR' gives **1 red : 2 pink : 1 white** -- the phenotype ratio matches the genotype ratio (1:2:1), unlike complete dominance.

### Codominance

Both alleles are **fully expressed simultaneously** in the heterozygote. This is NOT blending -- both phenotypes are visible at the same time.

**Classic example -- ABO blood type:**
- I^A I^B individuals express **both** A and B antigens on their red blood cells = type AB blood.

**How to distinguish from incomplete dominance:** In codominance, you can detect both gene products independently. In incomplete dominance, there's a single intermediate phenotype.

### Multiple Alleles -- ABO Blood Type System

The ABO gene has **three alleles** in the population: **I^A, I^B, and i**.

| Genotype | Phenotype (Blood Type) | Antigens on RBC | Antibodies in Plasma |
|----------|----------------------|-----------------|---------------------|
| I^A I^A or I^A i | Type A | A antigen | Anti-B |
| I^B I^B or I^B i | Type B | B antigen | Anti-A |
| I^A I^B | Type AB | Both A and B | Neither |
| ii | Type O | Neither | Anti-A and Anti-B |

**Key relationships:**
- I^A and I^B are **codominant** with each other
- Both I^A and I^B are **dominant** over i
- Type O is the **universal donor** (no antigens to trigger reactions)
- Type AB is the **universal recipient** (no antibodies to attack donor cells)

**MCAT favorite:** A problem might give you parents' blood types and ask for possible offspring types, or give offspring and ask you to determine parental genotypes.

**Worked example:** A type A mother and a type B father have a type O child. What are the parents' genotypes?

The child is type O = ii. The child must have received one i from each parent. Therefore mom is **I^A i** and dad is **I^B i**.

### Sex-Linked Traits (X-Linked Recessive)

Genes on the **X chromosome** follow a distinct inheritance pattern because males (XY) have only **one X**.

**Key features of X-linked recessive inheritance:**
- **Males are affected more often** -- they only need one copy of the recessive allele (hemizygous)
- **Females are carriers** if heterozygous (X^A X^a) -- they're phenotypically normal but can pass the allele to sons
- **No male-to-male transmission** -- fathers pass their Y to sons, not their X
- Affected males get the allele from their **carrier mother**

**Classic examples:** Hemophilia A, Duchenne muscular dystrophy, red-green color blindness.

**Worked example:** A carrier female (X^H X^h) and a normal male (X^H Y) have children. What fraction of their sons will be hemophiliacs?

|  | X^H | X^h |
|--|-----|-----|
| X^H | X^H X^H | X^H X^h |
| Y | X^H Y | X^h Y |

**1/2 of sons** (X^h Y) will be hemophiliacs. 1/2 of daughters will be carriers.

### X-Inactivation and Barr Bodies

In every female cell, **one X chromosome is randomly inactivated** early in embryonic development. The inactivated X condenses into a dense structure called a **Barr body**.

**Key points:**
- Inactivation is **random** -- in some cells the maternal X is silenced, in others the paternal X
- Once inactivated in a cell, all daughter cells maintain the same inactivation (clonal)
- This creates a **mosaic** pattern of gene expression (e.g., calico cats)
- **Barr body count = number of X chromosomes minus 1** (e.g., XXX female has 2 Barr bodies; XY male has 0)

**MCAT connection:** X-inactivation is why female carriers of X-linked diseases are usually unaffected -- they have enough cells expressing the normal allele. However, skewed inactivation can occasionally cause carrier females to show mild symptoms.

### Epistasis

**Epistasis** occurs when one gene **masks or modifies** the expression of another gene at a different locus.

**Example -- Labrador coat color:**
- Gene 1 (E locus): EE or Ee = pigment deposited; ee = no pigment deposited (yellow lab regardless of Gene 2)
- Gene 2 (B locus): BB or Bb = black pigment; bb = brown pigment

An ee dog is **yellow** regardless of its B-locus genotype because no pigment is deposited. The E gene is **epistatic** to the B gene.

**Modified dihybrid ratios from epistasis:**
- 9:3:4 (recessive epistasis, like the lab example)
- 12:3:1 (dominant epistasis)
- 9:7 (duplicate recessive epistasis)

**MCAT tip:** If a genetics problem gives you a weird ratio that doesn't match 9:3:3:1, think epistasis. Add up the categories to see if they total 16 (which confirms a dihybrid cross with modification).

### Pleiotropy

A **single gene** affects **multiple, seemingly unrelated** phenotypic traits.

**Classic example:** Sickle cell disease -- the single point mutation in the beta-globin gene causes anemia, spleen damage, pain crises, and increased malaria resistance. One gene, many effects.

**Other example:** PKU (phenylketonuria) -- defective phenylalanine hydroxylase leads to intellectual disability, light skin/hair, musty odor, and eczema.

### Polygenic Inheritance

A **single trait** is controlled by **multiple genes**, producing a continuous distribution of phenotypes (bell curve).

**Examples:** Height, skin color, blood pressure, intelligence.

**Key features:**
- Phenotypes show a **continuous range** (not discrete categories)
- Environmental factors also contribute (nature + nurture)
- Follows a **normal distribution** in the population

**Contrast with pleiotropy:** Polygenic = many genes, one trait. Pleiotropy = one gene, many traits.

### Penetrance vs Expressivity

**Penetrance:** The **percentage of individuals** with a given genotype who actually show the phenotype.
- **Complete penetrance** = 100% of people with the genotype show the phenotype
- **Reduced penetrance** = Some individuals with the genotype appear phenotypically normal
- Example: BRCA1 mutations have ~70% penetrance for breast cancer -- not everyone with the mutation develops cancer

**Expressivity:** The **degree or severity** to which a phenotype is expressed among individuals who DO show it.
- **Variable expressivity** = same genotype, different severity
- Example: Neurofibromatosis type 1 -- some patients have mild cafe-au-lait spots, others have severe tumors

**Memory trick:** **Penetrance** = "does it **penetrate** at all?" (yes/no, all-or-nothing). **Expressivity** = "how much is **expressed**?" (spectrum of severity).

### Genetic Linkage and Recombination Frequency

Genes on the **same chromosome** tend to be inherited together -- they are **linked**.

**Recombination frequency** measures how often crossing over separates two linked genes:
- **Recombination frequency = (number of recombinant offspring / total offspring) x 100%**
- Expressed in **centiMorgans (cM)** or **map units** -- 1% recombination = 1 cM = 1 map unit
- Maximum recombination frequency is **50%** (at 50%, genes behave as if unlinked)
- Genes closer together on a chromosome have **lower** recombination frequencies

**Worked example:** In a testcross of AaBb x aabb, you observe:
- 42 AaBb (parental)
- 38 aabb (parental)
- 11 Aabb (recombinant)
- 9 aaBb (recombinant)

Recombination frequency = (11 + 9) / (42 + 38 + 11 + 9) = 20/100 = **20%** = **20 map units** apart.

**Three-point cross mapping:** If given three genes, calculate pairwise recombination frequencies and arrange them linearly. The gene in the middle can be identified because the double-crossover class is always the **least frequent**.

---

## 3. Meiosis

### Overview: Why Meiosis Matters

Meiosis produces **haploid gametes** (n) from **diploid cells** (2n). It consists of two sequential divisions:
- **Meiosis I** -- the reduction division (separates homologs; goes from 2n to n)
- **Meiosis II** -- similar to mitosis (separates sister chromatids)

### Meiosis I -- The Key Division

| Phase | What Happens |
|-------|-------------|
| **Prophase I** | Chromosomes condense. Homologs pair up (**synapsis**) forming **tetrads** (bivalents). **Crossing over** occurs at **chiasmata**. Nuclear envelope breaks down. |
| **Metaphase I** | Tetrads line up at the metaphase plate. Orientation is random (**independent assortment**). |
| **Anaphase I** | **Homologous chromosomes** separate (NOT sister chromatids). Each pole gets one chromosome from each homologous pair. |
| **Telophase I** | Two haploid cells form. Each chromosome still consists of two sister chromatids joined at the centromere. |

**Critical distinction:** In anaphase I, **homologs** separate. In anaphase II, **sister chromatids** separate. This is the single most tested distinction about meiosis.

### Meiosis II -- Looks Like Mitosis

| Phase | What Happens |
|-------|-------------|
| **Prophase II** | Chromosomes condense (if decondensed). No new DNA synthesis. |
| **Metaphase II** | Individual chromosomes line up at the metaphase plate. |
| **Anaphase II** | **Sister chromatids** separate at the centromere. |
| **Telophase II** | Four haploid daughter cells form (gametes). |

**End result:** One diploid cell (2n) produces **four** genetically unique haploid cells (n).

### Sources of Genetic Variation

| Source | When It Occurs | Mechanism |
|--------|---------------|-----------|
| **Crossing over** | Prophase I | Homologous chromosomes exchange segments, creating new allele combinations on a single chromatid |
| **Independent assortment** | Metaphase I | Random orientation of homologous pairs; 2^23 possible combinations in humans |
| **Random fertilization** | Fertilization | Any sperm can fuse with any egg; (2^23)^2 = ~70 trillion combinations |

**MCAT favorite:** "Which process generates the MOST genetic diversity?" -- The answer is usually **random fertilization** (highest number of combinations), but crossing over is unique in that it creates **new allele combinations that didn't exist on either parental chromosome**.

### Meiosis vs Mitosis -- Comparison Table

| Feature | Mitosis | Meiosis |
|---------|---------|---------|
| **Divisions** | 1 | 2 |
| **Daughter cells** | 2 | 4 |
| **Ploidy of products** | 2n (diploid) | n (haploid) |
| **Genetic identity** | Identical to parent | Genetically unique |
| **Crossing over** | No (extremely rare) | Yes, in prophase I |
| **Synapsis/tetrads** | No | Yes, in prophase I |
| **What separates** | Sister chromatids | Homologs (MI), then sister chromatids (MII) |
| **Purpose** | Growth, repair | Gamete production |

### Nondisjunction

**Nondisjunction** is the failure of chromosomes to separate properly during cell division.

**In Meiosis I:** Homologous chromosomes fail to separate. All four gametes are abnormal -- two have an extra chromosome (n+1) and two are missing one (n-1).

**In Meiosis II:** Sister chromatids fail to separate. Two gametes are normal (n), one has an extra chromosome (n+1), and one is missing one (n-1).

**MCAT test:** "How do you distinguish meiosis I from meiosis II nondisjunction?"
- **Meiosis I nondisjunction:** All gametes are abnormal (none are normal)
- **Meiosis II nondisjunction:** Two gametes are normal, two are abnormal

**Consequences of nondisjunction:**
- **Trisomy** (2n + 1): Three copies of a chromosome. Example: Down syndrome (trisomy 21)
- **Monosomy** (2n - 1): One copy of a chromosome. Example: Turner syndrome (45, X)
- Most autosomal monosomies are **lethal**
- Trisomy 13 (Patau), trisomy 18 (Edwards), and trisomy 21 (Down) are the viable autosomal trisomies

---

## 4. Mutations

### Point Mutations (Single Nucleotide Changes)

| Type | What Happens | Effect on Protein | Example |
|------|-------------|-------------------|---------|
| **Silent** | Codon changes but codes for the **same amino acid** | None -- protein is identical | GCU to GCC (both = alanine) |
| **Missense** | Codon changes to a **different amino acid** | May or may not affect function; depends on the amino acid change | Sickle cell: GAG to GUG (Glu to Val) |
| **Nonsense** | Codon changes to a **stop codon** | **Truncated protein** -- usually nonfunctional | UAC (Tyr) to UAA (Stop) |
| **Frameshift** (insertion or deletion) | Addition or removal of nucleotides (not in multiples of 3) | **Destroys the reading frame** -- every downstream codon is wrong | Most severe type |

**Conservative vs non-conservative missense:**
- **Conservative:** New amino acid has similar properties (e.g., Leu to Ile -- both nonpolar). Protein may still function.
- **Non-conservative:** New amino acid has different properties (e.g., Glu to Val -- charged to nonpolar). Likely disrupts protein. Sickle cell is a classic non-conservative missense.

**Why silent mutations exist:** The genetic code is **degenerate** (redundant). Most amino acids are coded by multiple codons, especially at the **third (wobble) position**. Changes at the wobble position are often silent.

### Chromosomal Mutations

| Type | Description | Consequence |
|------|-------------|-------------|
| **Deletion** | Loss of a chromosomal segment | Loss of genes; can be lethal (e.g., Cri-du-chat = deletion on chromosome 5) |
| **Duplication** | A segment is copied, appearing twice | Extra gene copies; can lead to gene family evolution or disease |
| **Inversion** | A segment is flipped 180 degrees within the chromosome | Usually no phenotypic effect unless it disrupts a gene at the breakpoint |
| **Translocation** | A segment moves to a **non-homologous chromosome** | Can create fusion genes (e.g., Philadelphia chromosome: t(9;22) producing BCR-ABL in CML) |

**Robertsonian translocation:** Two acrocentric chromosomes fuse at their centromeres, reducing chromosome number. A carrier (45 chromosomes) is usually phenotypically normal but has increased risk of producing offspring with trisomy. This is the mechanism behind familial Down syndrome (translocation between chromosomes 14 and 21).

### Connections to Disease

| Mutation Type | Disease | Details |
|---------------|---------|---------|
| Missense | **Sickle cell disease** | Glu to Val in beta-globin; HbS polymerizes under low O2 |
| Nonsense/frameshift | **Cystic fibrosis** (most common = deltaF508 deletion) | Loss of CFTR chloride channel function |
| Trinucleotide repeat expansion | **Huntington disease** | CAG repeats in huntingtin gene; autosomal dominant |
| Trinucleotide repeat expansion | **Fragile X syndrome** | CGG repeats in FMR1 gene; X-linked |
| Chromosomal translocation | **Chronic myelogenous leukemia** | Philadelphia chromosome t(9;22); BCR-ABL fusion |
| Trisomy | **Down syndrome** | Trisomy 21 (or Robertsonian translocation) |

**Anticipation:** In trinucleotide repeat disorders, the number of repeats can **increase** with each generation, causing earlier onset and greater severity in successive generations. This is high-yield for genetics passages.

---

## 5. Population Genetics and Evolution

### Hardy-Weinberg Equilibrium

The **Hardy-Weinberg principle** states that allele and genotype frequencies in a population remain **constant** from generation to generation in the **absence of evolutionary forces**.

**The two equations:**
- **p + q = 1** (allele frequencies; p = dominant allele frequency, q = recessive allele frequency)
- **p^2 + 2pq + q^2 = 1** (genotype frequencies; p^2 = homozygous dominant, 2pq = heterozygous, q^2 = homozygous recessive)

**Five conditions for Hardy-Weinberg equilibrium:**
1. **No natural selection** -- all genotypes have equal fitness
2. **No mutation** -- no new alleles are introduced
3. **No gene flow** (migration) -- no alleles entering or leaving the population
4. **No genetic drift** -- population must be infinitely large
5. **Random mating** -- no mate preference based on genotype

**MCAT reality:** No real population meets all five conditions. HW equilibrium is a **null hypothesis** -- deviations from it tell you which evolutionary forces are acting.

### Solving Hardy-Weinberg Problems

**The key strategy:** You almost always **start with q^2** because the homozygous recessive phenotype is the only genotype you can identify directly from the phenotype.

**Worked example:** In a population, 16% of individuals show the autosomal recessive phenotype. Find the carrier frequency.

1. **q^2 = 0.16** (frequency of homozygous recessive = frequency of recessive phenotype)
2. **q = sqrt(0.16) = 0.4**
3. **p = 1 - q = 1 - 0.4 = 0.6**
4. **Carrier frequency = 2pq = 2(0.6)(0.4) = 0.48 = 48%**

**Worked example 2:** 1 in 10,000 people has a certain autosomal recessive disease. What fraction of the population are carriers?

1. q^2 = 1/10,000 = 0.0001
2. q = 0.01
3. p = 0.99
4. 2pq = 2(0.99)(0.01) = 0.0198 = approximately **1 in 50 people are carriers**

**MCAT trap:** Students sometimes confuse "frequency of the recessive allele" (q) with "frequency of people showing the recessive phenotype" (q^2). Always be precise about what the question is asking.

**For X-linked traits:** Males are hemizygous, so:
- Frequency of affected males = **q** (not q^2, since males have only one X)
- Frequency of affected females = **q^2**

### Natural Selection Types

| Type | Effect on Distribution | Example |
|------|----------------------|---------|
| **Directional** | Shifts the mean toward **one extreme** | Antibiotic resistance; darker moth coloration during industrial revolution |
| **Stabilizing** | Narrows the distribution; favors the **intermediate** phenotype; reduces variance | Human birth weight (very small or very large babies have lower survival) |
| **Disruptive** | Favors **both extremes** over the intermediate; splits the distribution | Finch beak size (large and small beaks favored over medium; can lead to speciation) |
| **Sexual selection** | Traits that increase **mating success** are favored, even if they decrease survival | Peacock tail; elk antlers |

**Balancing selection:** Maintains multiple alleles in a population.
- **Heterozygote advantage:** Heterozygotes have higher fitness than either homozygote. Classic example: sickle cell trait (HbAS) confers malaria resistance, maintaining the HbS allele in malaria-endemic regions even though HbSS is harmful.
- **Frequency-dependent selection:** Rare phenotypes have a fitness advantage (e.g., rare prey coloration that predators don't recognize).

### Genetic Drift

**Genetic drift** is the **random** change in allele frequencies due to **chance events** in a small population. It is non-adaptive (does not lead to "better" organisms) and has the greatest effect in **small populations**.

**Bottleneck effect:** A dramatic reduction in population size (natural disaster, disease) randomly eliminates most individuals. The surviving population has a **non-representative sample** of the original gene pool. Allele frequencies shift by chance.
- Example: Northern elephant seals were hunted to ~20 individuals. The current population has very low genetic diversity.

**Founder effect:** A small group splits off and colonizes a new area. The new population's gene pool reflects only the alleles of the **founders**, not the original population.
- Example: Ellis-van Creveld syndrome (polydactyly, short stature) has high frequency in the Amish population due to a small founding group that happened to carry the allele.

**Key distinction:** Both bottleneck and founder effects involve small population size, but the mechanism differs -- bottleneck **reduces** an existing population, while founder effect **establishes** a new one.

### Gene Flow

**Gene flow** (migration) is the transfer of alleles between populations. It has two key effects:
1. **Increases genetic diversity** within a population (new alleles arrive)
2. **Decreases differences** between populations (makes populations more similar)

Gene flow is the main force that **prevents speciation** -- as long as populations exchange genes, they won't diverge enough to become separate species.

### Speciation

**Speciation** is the formation of new species. Two main types:

**Allopatric speciation:** A **geographic barrier** (river, mountain range, ocean) physically separates a population. Over time, the isolated groups diverge through mutation, natural selection, and drift. If they can no longer interbreed when reunited, they are separate species.
- This is the **most common** form of speciation
- Example: Darwin's finches on the Galapagos Islands

**Sympatric speciation:** Speciation occurs **without geographic separation**. Populations become reproductively isolated while occupying the same area.
- Mechanisms: polyploidy (especially in plants), habitat differentiation, temporal isolation
- Example: Polyploidy in plants -- an error in meiosis doubles the chromosome number, and the polyploid can only mate with other polyploids

**Reproductive isolation mechanisms:**
- **Prezygotic:** Prevent mating or fertilization (temporal, behavioral, mechanical, gametic isolation, habitat isolation)
- **Postzygotic:** Hybrid offspring have reduced fitness (hybrid inviability, hybrid sterility, hybrid breakdown)
- Example of postzygotic: Mule (horse x donkey) is sterile

### Fitness and Adaptive Radiation

**Fitness** in evolutionary biology means **reproductive success** -- the ability to survive and produce viable, fertile offspring. It does NOT mean physical strength.
- Fitness is always **relative** to the environment
- An allele that increases fitness in one environment may decrease it in another
- **Inclusive fitness** extends to helping relatives reproduce (kin selection) -- relevant for PS section too

**Adaptive radiation:** A single ancestral species rapidly diversifies into many new species, each adapted to a different ecological niche. This typically follows:
1. A **mass extinction** that opens up niches (e.g., dinosaur extinction allowed mammalian radiation)
2. Colonization of **new environments** with many open niches (e.g., finches arriving at Galapagos)

**Key examples:**
- Darwin's finches -- different beak shapes for different food sources
- Mammals after the K-Pg extinction (66 mya)
- Cichlid fish in African Great Lakes

**Convergent vs divergent evolution:**
- **Divergent evolution:** Related species evolve different traits (adaptive radiation is an example). Produces **homologous structures** (same origin, different function: human arm vs whale flipper).
- **Convergent evolution:** Unrelated species evolve similar traits due to similar environmental pressures. Produces **analogous structures** (different origin, similar function: bird wing vs butterfly wing).

---

## Quick-Reference: High-Yield MCAT Formulas

| Formula | Use |
|---------|-----|
| **p + q = 1** | Allele frequencies in a population |
| **p^2 + 2pq + q^2 = 1** | Genotype frequencies (HW equilibrium) |
| **Recombination frequency = recombinants / total x 100%** | Map distance between linked genes |
| **1 map unit = 1 cM = 1% recombination** | Genetic distance |
| **Barr bodies = X chromosomes - 1** | Number of inactivated X chromosomes |

---

## Common MCAT Traps in Genetics

1. **Confusing q with q^2.** q is the allele frequency; q^2 is the genotype frequency of homozygous recessives.
2. **Forgetting that X-linked male frequency = q, not q^2.** Males are hemizygous.
3. **Assuming independent assortment when genes are linked.** If the problem mentions genes on the same chromosome, expect altered ratios.
4. **Mixing up incomplete dominance and codominance.** Incomplete = blended intermediate. Codominance = both fully expressed.
5. **Nondisjunction in MI vs MII.** MI = all 4 gametes abnormal. MII = 2 normal, 2 abnormal.
6. **Penetrance vs expressivity.** Penetrance = does the phenotype appear at all? Expressivity = how severe is it?
7. **Fitness does not mean strength.** Fitness = reproductive success relative to the environment.
