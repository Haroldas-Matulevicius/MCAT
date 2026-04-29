# BB Chapter 8 — Biological Membranes

Scope: Fluid mosaic model, membrane components (phospholipids, cholesterol, proteins), membrane transport (passive, active, endo/exocytosis), specialized membranes and cell junctions.

**Section:** Bio/Biochem (BB)
**AAMC FC mapping:** FC2A (Cell structure and membranes) — membrane portion
**Kaplan Reference:** Biochemistry Chapter 8

Note: Content migrated from the FC2A "Cell Structure and Membranes" deep-dive. Organelle, cytoskeleton, and endomembrane trafficking content remains in `BB_Cell_Biology.md` pending the Kaplan Biology chapter restructure (user handles next).

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

### Gap Junctions

- **Structure**: Each cell contributes a **connexon** (hemichannel) made of 6 **connexin** protein subunits. Two connexons from adjacent cells align to form a complete **gap junction channel**.
- **Function**: Allow direct passage of **ions, small molecules (< ~1 kDa), and second messengers** (cAMP, IP3, Ca2+) between cells. This enables **electrical and chemical coupling**.
- **Key locations**:
  - **Cardiac muscle**: Gap junctions in **intercalated discs** allow rapid ion flow between cardiomyocytes, enabling the heart to function as a **functional syncytium** (coordinated contraction).
  - **Smooth muscle**: Coordinate contraction in the uterus, GI tract.
  - **Neurons**: Electrical synapses (faster than chemical synapses but less common and less modulatable).
- Gap junctions can be **gated** -- they close when intracellular Ca2+ or H+ rises (e.g., if a cell is damaged, gap junctions close to isolate it and prevent damage from spreading).

### Desmosomes (Macula Adherens)

- **Structure**: Transmembrane **cadherins** (desmoglein and desmocollin) from adjacent cells interact in a Ca2+-dependent manner. On the cytoplasmic side, cadherins connect to **desmosomal plaques** (desmoplakin, plakoglobin), which anchor to **intermediate filaments** (typically keratins in epithelia, desmin in cardiac muscle).
- **Function**: Act like **rivets or spot welds** -- provide strong mechanical adhesion between cells. Resist **shearing forces**.
- **Location**: Abundant in tissues that experience mechanical stress: **skin**, **cardiac muscle**, **cervix**.

> **MCAT connection**: **Pemphigus vulgaris** -- autoimmune disease where antibodies target desmoglein (desmosome cadherin). Loss of cell-cell adhesion in the epidermis causes severe blistering. This demonstrates the importance of desmosomes in maintaining tissue integrity.

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

## High-Yield Takeaways for MCAT (Ch 8)

1. **Cholesterol moderates fluidity** -- it doesn't simply increase or decrease it.
2. **Na+/K+ ATPase: 3 Na+ out, 2 K+ in** -- electrogenic, drives secondary active transport.
3. **CFTR = Cl- channel. DeltaF508 = misfolding = cystic fibrosis.**
4. **Gap junctions = connexons = electrical coupling (heart!). Tight junctions = barrier. Desmosomes = mechanical strength.**
5. Small nonpolar molecules (O₂, CO₂) cross the bilayer freely; ions and polar molecules need transport proteins.
6. Phosphatidylserine flipping outward = apoptosis "eat me" signal.

→ Organelles, cytoskeleton, endomembrane trafficking: see `BB_Cell_Biology.md` (pending Kaplan Biology restructure)
