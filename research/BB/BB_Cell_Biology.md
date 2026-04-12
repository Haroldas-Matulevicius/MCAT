# FC2A: Cell Structure and Membranes -- Deep Dive

> BB Section | High-Yield | Connects to: metabolism, signal transduction, genetics, pathology

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

## 3. Membrane Structure

### The Fluid Mosaic Model

Proposed by Singer and Nicolson (1972). The membrane is a **fluid** (lipids and proteins move laterally) **mosaic** (a patchwork of different proteins embedded in the lipid bilayer).

Key features:
- Phospholipids form a **bilayer** with hydrophobic tails facing inward and hydrophilic heads facing outward (toward aqueous environments on both sides).
- Proteins are embedded in or attached to this bilayer.
- The membrane is **asymmetric**: the inner and outer leaflets have different lipid and protein compositions. For example, **phosphatidylserine (PS)** is normally on the inner leaflet only. When a cell undergoes **apoptosis**, PS flips to the outer leaflet -- this is an "eat me" signal for macrophages.

### Phospholipid Bilayer

Phospholipids are **amphipathic**: they have a hydrophilic head (phosphate + polar group) and two hydrophobic fatty acid tails.

**Spontaneous assembly**: In an aqueous environment, phospholipids self-assemble into bilayers, micelles, or liposomes to minimize contact between hydrophobic tails and water. This is driven by the **hydrophobic effect** (entropy-driven -- water molecules become more disordered when freed from ordering around hydrophobic surfaces). No energy input needed.

**What can cross the bare lipid bilayer?**
- **Can cross**: Small nonpolar molecules (O2, CO2, N2), small uncharged polar molecules (H2O -- slowly, ethanol, urea).
- **Cannot cross**: Ions (Na+, K+, Cl-, Ca2+), large polar molecules (glucose, amino acids), charged molecules. These need transport proteins.

### Cholesterol

Cholesterol inserts into the membrane with its **hydroxyl group** near the phospholipid heads and its **rigid steroid ring** interacting with the hydrophobic tails.

**Cholesterol is a fluidity buffer** -- it has a dual effect depending on temperature:
- **At HIGH temperature**: Cholesterol **reduces fluidity** by restraining phospholipid movement (its rigid rings restrict tail motion).
- **At LOW temperature**: Cholesterol **prevents crystallization** (phase transition to gel phase) by disrupting regular packing of fatty acid tails, thus maintaining some fluidity.

Net effect: cholesterol **broadens the temperature range** over which the membrane remains in a functional, liquid-crystalline state.

> **MCAT connection**: Cholesterol does NOT make membranes more or less fluid in a simple way -- it **stabilizes** fluidity. If an MCAT question asks what happens to membrane fluidity when cholesterol is added, the answer depends on the starting temperature/conditions.

### Membrane Proteins

**Integral (transmembrane) proteins**:
- Span the entire bilayer (one or more times). Have hydrophobic transmembrane domains (usually **alpha-helices**) that interact with the lipid tails.
- Can only be removed by **disrupting the bilayer**: detergents (like SDS or Triton X-100) or organic solvents.
- Examples: ion channels, receptors (GPCRs, receptor tyrosine kinases), transporters.

**Peripheral proteins**:
- Attached to the membrane surface through **non-covalent interactions** (electrostatic, hydrogen bonds) with integral proteins or lipid head groups.
- Can be removed by **mild conditions**: changes in pH, high salt concentration, or chelating agents (like EDTA, which removes divalent cations that may bridge the protein to the membrane).
- Examples: spectrin (cytoskeletal support in RBCs), some signaling proteins.

**Lipid-anchored proteins**: Attached via a covalent lipid anchor (GPI anchor on the extracellular side, or farnesyl/palmitoyl groups on the cytoplasmic side).

### Factors Affecting Membrane Fluidity

| Factor | Effect on Fluidity |
|--------|-------------------|
| **More unsaturated fatty acids** | **Increases** fluidity -- cis double bonds introduce kinks, preventing tight packing |
| **Shorter fatty acid chains** | **Increases** fluidity -- fewer van der Waals interactions between tails |
| **Higher temperature** | **Increases** fluidity -- more kinetic energy, more movement |
| **More cholesterol** | **Moderates** fluidity -- reduces at high temp, increases at low temp |
| **More saturated fatty acids** | **Decreases** fluidity -- straight chains pack tightly |

> **MCAT connection**: Bacteria and poikilotherms (cold-blooded organisms) adjust membrane composition to maintain fluidity. At lower temperatures, they increase the proportion of unsaturated fatty acids. This is called **homeoviscous adaptation**.

---

## 4. Transport Across Membranes

### Passive Transport (No ATP, moves DOWN concentration gradient)

**Simple diffusion**: Direct passage through the lipid bilayer. Only for small, nonpolar or small uncharged polar molecules. Rate depends on the **concentration gradient**, membrane **permeability**, **surface area**, and **membrane thickness** (Fick's Law: J = -DA(dC/dx)).

**Facilitated diffusion**: Uses **transport proteins** but still moves down the gradient. No ATP.
- **Channel proteins**: Form a hydrophilic pore. Can be **gated** (ligand-gated, voltage-gated, mechanically gated) or ungated (leak channels). Very fast -- ions flow through at near-diffusion rates. **Selective** based on size and charge.
- **Carrier proteins (transporters)**: Bind the solute, undergo a conformational change, and release it on the other side. Slower than channels. Show **saturation kinetics** (like enzymes -- Vmax when all carriers are occupied). Example: **GLUT transporters** for glucose.

**Osmosis**: Movement of **water** across a semipermeable membrane from a region of **lower solute concentration** (higher water concentration) to **higher solute concentration** (lower water concentration). Driven by differences in **osmotic pressure**.

- **Aquaporins**: Channel proteins that greatly increase the rate of osmosis. Found in kidney collecting duct cells (regulated by **ADH/vasopressin** -- ADH causes aquaporin-2 insertion into the apical membrane, increasing water reabsorption).

### Tonicity

Tonicity describes the effect of a solution on cell volume, considering only **non-penetrating solutes**.

| Solution | Cell Behavior | Mechanism |
|----------|--------------|-----------|
| **Hypertonic** | Cell **shrinks** (crenation in RBCs) | Water moves OUT of the cell by osmosis |
| **Hypotonic** | Cell **swells** (may lyse -- hemolysis in RBCs) | Water moves INTO the cell by osmosis |
| **Isotonic** | No net change in cell volume | No net water movement |

> Important distinction: **Osmolarity** is a property of the solution (total solute concentration). **Tonicity** depends on the **membrane permeability** to those solutes. Urea is osmotically active but freely crosses membranes, so a urea solution is effectively hypotonic (the cell swells because water follows urea in, and urea doesn't create a lasting osmotic gradient).

### Active Transport: Primary

Uses ATP directly to move solutes **against** their concentration gradient.

**Na+/K+ ATPase (sodium-potassium pump)**:
- Pumps **3 Na+ out** and **2 K+ in** per ATP hydrolyzed.
- **Electrogenic**: Moves a net +1 charge out per cycle, contributing to the **resting membrane potential** (makes the inside more negative). The pump itself contributes about -5 to -10 mV of the ~-70 mV resting potential. The larger contribution comes from K+ leak channels.
- Present in virtually all animal cells. Consumes ~25% of the cell's total ATP in many cell types.
- Maintains the **Na+ and K+ concentration gradients** that are essential for nerve impulse transmission, secondary active transport, and cell volume regulation.

Other primary active transport examples:
- **Ca2+-ATPase (SERCA)**: Pumps Ca2+ into the SER/SR.
- **H+/K+-ATPase**: In stomach parietal cells, pumps H+ into the gastric lumen (acidifies stomach). Target of **proton pump inhibitors (PPIs)** like omeprazole.
- **V-type H+-ATPase**: Acidifies lysosomes and endosomes.

### Active Transport: Secondary (Cotransport)

Uses the **electrochemical gradient** of one solute (usually Na+ flowing DOWN its gradient, established by the Na+/K+ ATPase) to drive the transport of another solute AGAINST its gradient. No direct ATP use, but indirectly depends on ATP (because the Na+ gradient was built by the Na+/K+ ATPase).

**Symport (cotransport)**: Both solutes move in the **same direction**.
- **SGLT1 (sodium-glucose linked transporter)**: Na+ and glucose both move into the intestinal epithelial cell. The Na+ gradient provides the energy to pull glucose in against its gradient. Found in the **apical membrane** of intestinal enterocytes and kidney proximal tubule cells.
- **Na+/amino acid symporters**: Similar principle.

**Antiport (exchange)**: Solutes move in **opposite directions**.
- **Na+/Ca2+ exchanger (NCX)**: Na+ in, Ca2+ out. Important in cardiac muscle -- this is how digoxin works indirectly (inhibits Na+/K+ ATPase -> Na+ accumulates inside -> NCX can't export Ca2+ effectively -> Ca2+ rises inside -> stronger heart contraction).
- **Na+/H+ exchanger (NHE)**: Na+ in, H+ out. Helps regulate intracellular pH.
- **Cl-/HCO3- exchanger (Band 3)**: In red blood cells, exchanges Cl- for HCO3- (the **chloride shift** -- important for CO2 transport in the blood).

> **MCAT connection**: **Cystic fibrosis** -- mutation in the **CFTR chloride channel** (a Cl- channel, technically also a regulator of other channels). Most common mutation is **deltaF508** (deletion of phenylalanine at position 508, causing misfolding and ER retention). Thick, dehydrated mucus accumulates in lungs, pancreatic ducts, and other epithelia because Cl- (and therefore water) secretion is impaired.

### Endocytosis

Bringing material INTO the cell by membrane invagination.

**Phagocytosis** ("cell eating"): Large particles (bacteria, dead cells). The cell extends **pseudopods** around the particle and engulfs it into a **phagosome**. Macrophages and neutrophils are the primary phagocytes. The phagosome fuses with a lysosome for degradation.

**Pinocytosis** ("cell drinking"): Non-specific uptake of extracellular fluid and dissolved solutes. The membrane invaginates to form small vesicles. Continuous and non-selective.

**Receptor-mediated endocytosis**: Highly specific. Ligands bind to specific **receptors** on the cell surface. The receptor-ligand complexes cluster in **clathrin-coated pits**. The pit invaginates and pinches off (with the help of **dynamin**, a GTPase that wraps around the neck of the pit and severs it) to form a **clathrin-coated vesicle**. The clathrin coat is then removed, and the vesicle becomes an **early endosome**, which acidifies to separate ligand from receptor. Receptors are often recycled; ligands are degraded in lysosomes.
- Example: **LDL receptor pathway** -- LDL binds LDL receptors, is internalized via clathrin-coated pits, cholesterol is extracted in lysosomes. **Familial hypercholesterolemia** -- defective LDL receptors, LDL accumulates in the blood.

### Exocytosis

Bringing material OUT of the cell. Vesicles fuse with the plasma membrane, releasing contents to the extracellular space.
- **Constitutive**: Continuous, unregulated (e.g., secretion of ECM components).
- **Regulated**: Triggered by a signal, often a rise in intracellular Ca2+ (e.g., neurotransmitter release at synapses, insulin secretion from beta cells). Vesicles dock at the membrane via **SNARE proteins** (v-SNAREs on the vesicle, t-SNAREs on the target membrane). NSF and alpha-SNAP disassemble SNARE complexes for recycling.

> **MCAT connection**: **Botulinum toxin** cleaves SNARE proteins, preventing neurotransmitter release -> flaccid paralysis. **Tetanus toxin** blocks inhibitory neurotransmitter release -> spastic paralysis. Both target SNAREs but in different neurons.

---

## 5. Cell Junctions

### Tight Junctions (Zonula Occludens)

- **Location**: Near the **apical surface** of epithelial cells. Form a continuous band around each cell.
- **Structure**: **Claudins** and **occludins** (transmembrane proteins) from adjacent cells interact to seal the intercellular space.
- **Function**: Create a **paracellular barrier** -- prevent solutes from leaking between cells. This forces substances to go *through* the cell (transcellular route), allowing selective absorption and secretion.
- Also maintain **cell polarity** by preventing mixing of apical and basolateral membrane proteins (the tight junction acts as a "fence").
- **Permeability varies**: Tight junctions in the kidney proximal tubule are "leaky" (allow some paracellular transport), while those in the **blood-brain barrier** are very tight.

> **MCAT connection**: The blood-brain barrier relies on tight junctions between brain capillary endothelial cells. Only small lipophilic molecules and molecules with specific transporters can cross. This is why many drugs can't reach the brain.

---

### Gap Junctions

- **Structure**: Each cell contributes a **connexon** (hemichannel) made of 6 **connexin** protein subunits. Two connexons from adjacent cells align to form a complete **gap junction channel**.
- **Function**: Allow direct passage of **ions, small molecules (< ~1 kDa), and second messengers** (cAMP, IP3, Ca2+) between cells. This enables **electrical and chemical coupling**.
- **Key locations**:
  - **Cardiac muscle**: Gap junctions in **intercalated discs** allow rapid ion flow between cardiomyocytes, enabling the heart to function as a **functional syncytium** (coordinated contraction).
  - **Smooth muscle**: Coordinate contraction in the uterus, GI tract.
  - **Neurons**: Electrical synapses (faster than chemical synapses but less common and less modulatable).
- Gap junctions can be **gated** -- they close when intracellular Ca2+ or H+ rises (e.g., if a cell is damaged, gap junctions close to isolate it and prevent damage from spreading).

---

### Desmosomes (Macula Adherens)

- **Structure**: Transmembrane **cadherins** (desmoglein and desmocollin) from adjacent cells interact in a Ca2+-dependent manner. On the cytoplasmic side, cadherins connect to **desmosomal plaques** (desmoplakin, plakoglobin), which anchor to **intermediate filaments** (typically keratins in epithelia, desmin in cardiac muscle).
- **Function**: Act like **rivets or spot welds** -- provide strong mechanical adhesion between cells. Resist **shearing forces**.
- **Location**: Abundant in tissues that experience mechanical stress: **skin**, **cardiac muscle**, **cervix**.

> **MCAT connection**: **Pemphigus vulgaris** -- autoimmune disease where antibodies target desmoglein (desmosome cadherin). Loss of cell-cell adhesion in the epidermis causes severe blistering. This demonstrates the importance of desmosomes in maintaining tissue integrity.

---

### Hemidesmosomes

- **Structure**: Look like half a desmosome but are **molecularly distinct**. Use **integrins** (not cadherins) as the transmembrane protein. Integrins connect to the **basement membrane** (extracellular matrix) on the outside and to **intermediate filaments** (keratin) on the inside via plectin.
- **Function**: Anchor epithelial cells to the **basal lamina/basement membrane**. Resist forces that would detach the epithelium from the underlying connective tissue.

> **MCAT connection**: Distinguish carefully:
> - **Desmosomes**: cell-to-cell, cadherins, intermediate filaments.
> - **Hemidesmosomes**: cell-to-basement membrane, integrins, intermediate filaments.
> - **Focal adhesions**: cell-to-ECM, integrins, **actin** filaments (not IFs). Important for cell motility and signaling.

---

## Junction Summary Table

| Junction | Connection | Key Proteins | Cytoskeletal Link | Primary Function |
|----------|-----------|-------------|-------------------|-----------------|
| **Tight junction** | Cell-cell | Claudins, occludins | Actin (indirectly) | Seal/barrier, polarity |
| **Gap junction** | Cell-cell | Connexins (connexons) | None | Communication (ions, small molecules) |
| **Desmosome** | Cell-cell | Cadherins (desmoglein, desmocollin) | Intermediate filaments | Mechanical strength |
| **Hemidesmosome** | Cell-basement membrane | Integrins | Intermediate filaments | Anchoring to ECM |
| **Adherens junction** | Cell-cell | Cadherins (E-cadherin) | Actin | Adhesion belt, tissue integrity |

---

## High-Yield Takeaways for MCAT

1. **Know what happens where in the mitochondrion** -- TCA/beta-ox in matrix, ETC on inner membrane, protons in IMS.
2. **Signal sequence + SRP pathway** for targeting proteins to the ER.
3. **N-linked glycosylation starts in the ER; O-linked happens in the Golgi.**
4. **M6P tags** direct enzymes to lysosomes. Failure = I-cell disease.
5. **COPII goes forward (ER->Golgi), COPI goes backward (Golgi->ER), clathrin sorts at the Golgi and internalizes at the plasma membrane.**
6. **Kinesin = + end (out), Dynein = - end (in).** Kartagener syndrome = dynein defect.
7. **Cholesterol moderates fluidity** -- it doesn't simply increase or decrease it.
8. **Na+/K+ ATPase: 3 Na+ out, 2 K+ in** -- electrogenic, drives secondary active transport.
9. **CFTR = Cl- channel. DeltaF508 = misfolding = cystic fibrosis.**
10. **Gap junctions = connexons = electrical coupling (heart!). Tight junctions = barrier. Desmosomes = mechanical strength.**
