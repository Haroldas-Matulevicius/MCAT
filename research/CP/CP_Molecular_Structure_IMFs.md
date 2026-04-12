# FC5B: Molecular Structure and Intermolecular Forces

**Section:** Chem/Phys (CP)
**Source Disciplines:** General Chemistry, Organic Chemistry
**Yield:** HIGH -- this material underlies virtually every CP passage that involves molecules

---

## 1. Lewis Structures

Lewis structures are the starting point for predicting geometry, polarity, reactivity, and intermolecular forces. The MCAT will not ask you to "draw a Lewis structure" as a standalone question, but you absolutely need to construct them mentally to answer questions about molecular shape, dipole moments, acidity, and resonance stabilization.

### Step-by-Step Method

1. **Count total valence electrons.** Sum the group numbers for each atom. Add one electron for each negative charge; subtract one for each positive charge.
2. **Identify the central atom.** Usually the least electronegative atom (never H). If there is a tie, it is typically the atom written first in the formula or the atom that can form the most bonds.
3. **Draw single bonds** from the central atom to each surrounding atom. Each bond uses 2 electrons.
4. **Distribute remaining electrons as lone pairs**, starting with the outer atoms to satisfy their octets (or duet for H).
5. **Check the central atom's octet.** If it is short, convert lone pairs on adjacent atoms into double or triple bonds.
6. **Calculate formal charges** to verify the best structure.

### Formal Charge

$$\text{FC} = \text{valence electrons} - \text{lone pair electrons} - \tfrac{1}{2}(\text{bonding electrons})$$

Key rules:
- The best Lewis structure **minimizes formal charges** on all atoms (ideally all zeros).
- If formal charges are unavoidable, **negative formal charge should sit on the more electronegative atom**.
- Formal charges that place a positive charge on a highly electronegative atom (like O or F) represent a poor structure.

**MCAT Tip:** Formal charge questions often appear in discrete (standalone) questions. Memorize the formula cold and practice applying it fast -- it takes about 10 seconds per atom once you are fluent.

### Resonance Structures

Resonance occurs when you can draw two or more valid Lewis structures that differ only in the placement of electrons (not atoms). The real molecule is a **resonance hybrid** -- a weighted average of all contributing structures.

**Which resonance structure contributes most?**
- The one with the **fewest formal charges**.
- If formal charges are unavoidable, the one where **negative charge is on the more electronegative atom**.
- Structures where every atom has a complete octet are favored over those with incomplete octets.

**Delocalization and stability:** The more resonance structures you can draw, the more delocalized the electrons, and the more stable the species. This is why:
- Carboxylate anions (COO-) are more stable than alkoxide anions (RO-) -- two equivalent resonance structures spread the charge over two oxygens.
- Benzene is exceptionally stable -- six equivalent C-C bonds, not alternating singles and doubles.
- Allylic and benzylic carbocations/radicals are stabilized by resonance.

**MCAT Tip:** Resonance is a top-tier concept for explaining acidity differences. When asked "why is compound A more acidic than compound B?", the answer is almost always about resonance stabilization of the conjugate base.

### Exceptions to the Octet Rule

| Exception | Examples | Explanation |
|-----------|----------|-------------|
| **Incomplete octet** | BF3, BeH2, BH3 | Boron (6e-) and beryllium (4e-) are stable with fewer than 8 electrons. B is a Lewis acid precisely because it has an empty p orbital. |
| **Expanded octet** | PCl5, SF6, SO4^2-, H2SO4 | Elements in **period 3 and below** can use d orbitals to accommodate more than 8 electrons. This is why phosphorus can form 5 bonds and sulfur can form 6. |
| **Odd-electron species** | NO, NO2 | Free radicals with an unpaired electron -- cannot satisfy the octet on every atom. |

**MCAT Tip:** When you see sulfur or phosphorus as a central atom, do NOT force an octet. Expanded octets on these atoms often give a structure with lower formal charges, which is the preferred structure.

---

## 2. VSEPR Theory

**Valence Shell Electron Pair Repulsion** theory predicts 3D molecular shape by assuming that electron groups (bonding pairs and lone pairs) repel each other and arrange themselves to maximize their distance apart.

### Critical Distinction: Electron Geometry vs. Molecular Geometry

- **Electron geometry** is determined by the total number of electron groups around the central atom (count bonding pairs AND lone pairs).
- **Molecular geometry** describes the arrangement of **atoms only** (lone pairs are invisible to molecular geometry naming).

This distinction is tested constantly. A molecule with 4 electron groups has **tetrahedral electron geometry**, but if one of those groups is a lone pair, the molecular geometry is **trigonal pyramidal** (like NH3), not tetrahedral.

### The Master Table

| Electron Groups | Electron Geometry | Lone Pairs | Molecular Geometry | Bond Angle | Example |
|:-:|---|:-:|---|:-:|---|
| 2 | Linear | 0 | **Linear** | 180 | CO2, BeCl2 |
| 3 | Trigonal planar | 0 | **Trigonal planar** | 120 | BF3 |
| 3 | Trigonal planar | 1 | **Bent** | ~117 | SO2 |
| 4 | Tetrahedral | 0 | **Tetrahedral** | 109.5 | CH4, CCl4 |
| 4 | Tetrahedral | 1 | **Trigonal pyramidal** | ~107 | NH3 |
| 4 | Tetrahedral | 2 | **Bent** | ~104.5 | H2O |
| 5 | Trigonal bipyramidal | 0 | **Trigonal bipyramidal** | 90/120 | PCl5 |
| 5 | Trigonal bipyramidal | 1 | **Seesaw** | ~90/~120 | SF4 |
| 5 | Trigonal bipyramidal | 2 | **T-shaped** | ~90 | ClF3 |
| 5 | Trigonal bipyramidal | 3 | **Linear** | 180 | XeF2 |
| 6 | Octahedral | 0 | **Octahedral** | 90 | SF6 |
| 6 | Octahedral | 1 | **Square pyramidal** | ~90 | BrF5 |
| 6 | Octahedral | 2 | **Square planar** | 90 | XeF4 |

### Why Lone Pairs Compress Bond Angles

Lone pairs are held closer to the nucleus than bonding pairs (they are not shared with another atom). This means they occupy **more angular space** and push bonding pairs closer together. The ranking of repulsion:

**Lone pair-lone pair > Lone pair-bonding pair > Bonding pair-bonding pair**

This is why:
- H2O (2 lone pairs) has a bond angle of ~104.5, well below the tetrahedral 109.5.
- NH3 (1 lone pair) has a bond angle of ~107, slightly below 109.5.

**MCAT Tip:** For trigonal bipyramidal electron geometry, lone pairs always go in **equatorial** positions (not axial) because equatorial positions have only two 90-degree neighbors, while axial positions have three. This minimizes lone pair-bonding pair repulsion.

---

## 3. Hybridization

Hybridization explains bonding geometry by mixing atomic orbitals into hybrid orbitals of equal energy. For the MCAT, this is essentially a shortcut: **count the electron groups, and you know the hybridization.**

### The Core Pattern

| Electron Groups | Hybridization | Geometry | Bond Angle | Bond Types |
|:-:|---|---|:-:|---|
| 2 | **sp** | Linear | 180 | 2 sigma bonds (+ up to 2 pi bonds) |
| 3 | **sp2** | Trigonal planar | 120 | 3 sigma bonds (+ up to 1 pi bond) |
| 4 | **sp3** | Tetrahedral | 109.5 | 4 sigma bonds (no pi bonds) |

**The number of electron groups = the number of hybrid orbitals = the number in the superscript plus 1.**
- sp = 2 hybrid orbitals (1 s + 1 p)
- sp2 = 3 hybrid orbitals (1 s + 2 p)
- sp3 = 4 hybrid orbitals (1 s + 3 p)

Leftover unhybridized p orbitals form **pi bonds**:
- sp3: 0 unhybridized p orbitals, so no pi bonds.
- sp2: 1 unhybridized p orbital, so up to 1 pi bond (one double bond).
- sp: 2 unhybridized p orbitals, so up to 2 pi bonds (one triple bond, or two double bonds).

### Sigma vs. Pi Bonds

| Property | Sigma (sigma) | Pi (pi) |
|----------|------|------|
| **Overlap** | Head-on (along bond axis) | Lateral/sideways (above and below bond axis) |
| **Rotation** | Free rotation around bond | Restricted rotation -- breaking pi bond costs energy |
| **Strength** | Stronger individually | Weaker individually |
| **Per bond** | Every bond has exactly 1 sigma | Double bond = 1 sigma + 1 pi; Triple = 1 sigma + 2 pi |
| **Formed by** | Hybrid orbitals | Unhybridized p orbitals |

**Quick bond-counting method:**
- Single bond = 1 sigma, 0 pi
- Double bond = 1 sigma, 1 pi
- Triple bond = 1 sigma, 2 pi
- Total sigma bonds in a molecule = total number of bonds drawn as lines in a skeletal structure (every connection is at least 1 sigma)

**MCAT Tip:** A question that asks "how many sigma and pi bonds are in this molecule?" is really just asking you to count single, double, and triple bonds. Do not overthink it.

### Hybridization in Common Functional Groups

| Functional Group | Carbon Hybridization | Notes |
|-----------------|---------------------|-------|
| Alkane C-C | sp3 | All single bonds |
| Alkene C=C | sp2 | One pi bond, planar around the double bond |
| Alkyne C(triple)C | sp | Two pi bonds, linear |
| Carbonyl C=O | sp2 | Aldehydes, ketones, carboxylic acids, esters, amides |
| Aromatic ring C | sp2 | Delocalized pi system |
| Nitrile C(triple)N | sp | Linear |

**MCAT Tip:** Nitrogen and oxygen hybridization follows the same electron-group counting rules. The nitrogen in an amine (R-NH2) is sp3 (4 electron groups: 3 bonds + 1 lone pair). The nitrogen in an amide is sp2 (the lone pair is delocalized into the pi system by resonance).

---

## 4. Bond Polarity and Dipole Moments

### Bond Polarity

A covalent bond is polar when the two atoms have **different electronegativities**. The more electronegative atom pulls electron density toward itself, creating a partial negative charge (delta-) on that atom and a partial positive charge (delta+) on the other.

**Electronegativity trend:** Increases going up and to the right on the periodic table (excluding noble gases). The most electronegative element is fluorine (4.0), followed by oxygen (3.5), nitrogen/chlorine (3.0).

- **Nonpolar covalent:** Electronegativity difference ~0-0.4 (C-H is essentially nonpolar for MCAT purposes)
- **Polar covalent:** Electronegativity difference ~0.5-1.7
- **Ionic:** Electronegativity difference >1.7 (but this is a guideline, not a hard cutoff)

### Molecular Dipole Moment

The **molecular dipole moment** is the **vector sum** of all individual bond dipoles. This means molecular geometry matters enormously:

- **CO2:** Each C=O bond is polar, but the molecule is linear, so the two bond dipoles point in opposite directions and cancel. **Net dipole = 0.** Nonpolar molecule.
- **H2O:** Each O-H bond is polar, and the bent geometry means the dipoles do NOT cancel. **Net dipole is not zero.** Polar molecule.

**Symmetric molecules with identical polar bonds have no net dipole:**
- CO2 (linear, 2 identical bonds) -- nonpolar
- BF3 (trigonal planar, 3 identical bonds) -- nonpolar
- CCl4 (tetrahedral, 4 identical bonds) -- nonpolar
- SF6 (octahedral, 6 identical bonds) -- nonpolar
- XeF4 (square planar, 4 identical bonds) -- nonpolar

**Asymmetric arrangements produce a net dipole:**
- H2O (bent) -- polar
- NH3 (trigonal pyramidal) -- polar
- CHCl3 (tetrahedral but not all groups identical) -- polar
- CH2Cl2 -- polar

**MCAT Tip:** The question "is this molecule polar?" is really asking two things: (1) are there polar bonds? and (2) does the geometry allow the bond dipoles to cancel? You need both answers.

---

## 5. Intermolecular Forces (IMFs)

IMFs are the forces BETWEEN molecules (not within them -- those are intramolecular/covalent bonds). They are dramatically weaker than covalent bonds but they determine virtually all physical properties.

### Types of IMFs (Weakest to Strongest)

#### London Dispersion Forces (LDFs)

- **Present in:** ALL molecules, including nonpolar ones.
- **Origin:** Temporary, instantaneous dipoles caused by random fluctuations in electron density. A temporary dipole in one molecule induces a dipole in a neighboring molecule, creating an attractive force.
- **Strength depends on:**
  - **Polarizability** -- how easily the electron cloud can be distorted. Larger atoms/molecules are more polarizable.
  - **Molecular weight** -- more electrons = stronger LDFs. This is why boiling points generally increase with molecular weight in a homologous series.
  - **Surface area** -- more contact area = stronger LDFs. Straight-chain alkanes have higher boiling points than their branched isomers because they can pack more closely.

**MCAT Tip:** Never say "nonpolar molecules have no intermolecular forces." They have London dispersion forces, and for large nonpolar molecules (like fats or long-chain hydrocarbons), these forces can be substantial.

#### Dipole-Dipole Interactions

- **Present in:** Polar molecules (molecules with a net dipole moment).
- **Origin:** The partial positive end of one molecule is attracted to the partial negative end of another.
- **Strength depends on:** The magnitude of the dipole moment. Greater electronegativity difference and less symmetric geometry = stronger dipole-dipole forces.

#### Hydrogen Bonding

- **Present in:** Molecules where H is bonded to **N, O, or F**.
- **Origin:** This is a special, extra-strong case of dipole-dipole interaction. It occurs because:
  1. N, O, and F are **very electronegative** -- they pull electron density strongly away from H.
  2. H has **no inner electron shells** -- when its one electron is pulled away, the bare proton is exposed.
  3. N, O, and F are **small atoms with concentrated lone pairs** -- they can get close to the exposed H.
- **Hydrogen bond donor:** The molecule providing the H (must be N-H, O-H, or F-H).
- **Hydrogen bond acceptor:** Any atom with a lone pair (usually N, O, or F, but technically any electronegative atom with lone pairs).

**Why is hydrogen bonding so important on the MCAT?**
- It explains water's anomalously high boiling point (100C for MW 18, vs. H2S at -60C for MW 34).
- It governs protein secondary structure (alpha-helices and beta-sheets are held together by H-bonds between backbone N-H and C=O groups).
- It governs DNA base pairing (A-T has 2 H-bonds, G-C has 3 H-bonds).
- It determines the solubility of biological molecules.

#### Ion-Dipole Forces

- **Present in:** Ions interacting with polar molecules (e.g., Na+ dissolved in water).
- **Strongest IMF type.** This is why ionic compounds dissolve in polar solvents -- the ion-dipole interactions with the solvent are strong enough to overcome the lattice energy of the ionic solid.

### IMFs and Physical Properties

| Property | Stronger IMFs cause... | Reasoning |
|----------|----------------------|-----------|
| **Boiling point** | Higher BP | Need more energy to overcome attractions and enter gas phase |
| **Melting point** | Higher MP | Need more energy to disrupt ordered solid arrangement |
| **Viscosity** | Higher viscosity | Stronger attractions resist flow |
| **Surface tension** | Higher surface tension | Molecules at the surface are pulled inward more strongly |
| **Vapor pressure** | Lower vapor pressure | Fewer molecules have enough energy to escape into gas phase |
| **Solubility** | "Like dissolves like" | Polar/H-bonding solutes dissolve in polar solvents; nonpolar solutes dissolve in nonpolar solvents |

### Ranking IMFs -- A Practical Framework

When asked to rank boiling points or solubilities, follow this order:

1. **Is there hydrogen bonding?** (N-H, O-H, F-H) -- if yes, this is a strong force.
2. **Is the molecule polar?** -- if yes, dipole-dipole interactions are present.
3. **Compare molecular weight and surface area** -- heavier and less branched = stronger LDFs.

Example ranking of boiling points:
- Butane (C4H10, MW 58, nonpolar, LDF only): BP = -1C
- Propanal (C3H6O, MW 58, polar, dipole-dipole + LDF): BP = 49C
- 1-Propanol (C3H8O, MW 60, H-bonding + dipole-dipole + LDF): BP = 97C

Similar molecular weights, but the type of IMF makes a huge difference.

**MCAT Tip:** Ion-dipole forces are often forgotten. If a passage describes something dissolving in water, and the answer choices include "ion-dipole interactions," that is frequently the correct answer for explaining solvation of ionic species.

---

## 6. Stereochemistry

Stereochemistry is one of the most heavily tested orgo topics on the MCAT. It requires careful, systematic thinking -- not memorization. The key is to have a clear decision framework.

### Isomer Classification

```
                    Same molecular formula?
                           |
                    YES -- Isomers
                           |
              Same connectivity (bonding)?
                    /              \
                  NO                YES
                  |                  |
        Constitutional         Stereoisomers
        (structural)               |
         isomers          Mirror images?
                          /            \
                        YES             NO
                        |               |
                   Enantiomers    Diastereomers
                                 (includes cis/trans,
                                  E/Z isomers, and
                                  compounds with
                                  multiple stereocenters
                                  that are not mirror images)
```

### Constitutional (Structural) Isomers

Same molecular formula, **different connectivity**. The atoms are bonded to different partners.
- Butane vs. isobutane (same formula C4H10, different carbon skeleton)
- 1-propanol vs. 2-propanol (OH on different carbons)
- Ethanol vs. dimethyl ether (C2H6O -- completely different functional groups)

These can have **very different** physical and chemical properties.

### Chirality and Chiral Centers

A molecule is **chiral** if it is non-superimposable on its mirror image. The most common source of chirality is a **chiral center** (stereocenter): a carbon bonded to **four different substituents**.

How to identify chiral centers:
1. Look at each carbon in the molecule.
2. Check if it has 4 different groups attached. If yes, it is a chiral center.
3. A carbon with a double bond, or bonded to two identical groups, is NOT a chiral center.

**Important:** Chirality is a property of the whole molecule, not just the atom. A molecule can have chiral centers but still be achiral if it has an internal plane of symmetry (meso compound -- see below).

### R/S Configuration (Cahn-Ingold-Prelog Rules)

This is the system for assigning absolute configuration to each chiral center. It is heavily tested.

**Step 1: Assign priorities (1-4) to the four substituents.**
- Higher atomic number = higher priority.
- If two substituents start with the same atom, move outward along the chain until you find a point of difference. Compare at the first point of difference.
- Double bonds count as two single bonds to the same atom (a C=O is treated as if C is bonded to O twice, and O is bonded to C twice). Triple bonds count as three.

**Step 2: Orient the molecule so priority 4 (lowest) points away from you** (into the page/back).

**Step 3: Trace a path from priority 1 to 2 to 3.**
- **Clockwise = R** (rectus, Latin for "right")
- **Counterclockwise = S** (sinister, Latin for "left")

**Shortcut when #4 is not pointing away from you:** If #4 is pointing toward you (coming out of the page as a wedge), determine the apparent rotation 1->2->3 and then **reverse** your answer. If it looks clockwise, it is actually S; if it looks counterclockwise, it is actually R.

**MCAT Tip:** CIP priority mistakes are the #1 source of errors on stereochemistry questions. Practice this until it is automatic. The most common traps:
- Forgetting that deuterium (D) has higher priority than hydrogen (H) because D has a higher mass number (atomic number is the same, so mass is the tiebreaker).
- Forgetting the double bond expansion rule.
- Rushing the comparison and not going far enough along the chain.

### Enantiomers

**Enantiomers** are non-superimposable mirror images. They have the **opposite configuration at every chiral center** (all R become S, all S become R).

Properties of enantiomers:
- **Same** melting point, boiling point, density, solubility (in achiral solvents), Rf value (on TLC).
- **Same** chemical reactivity with achiral reagents.
- **Opposite** optical rotation (if one is +30 degrees, the other is -30 degrees).
- **Different** reactivity with chiral reagents (e.g., enzymes, which are chiral).
- **Different** biological activity (one enantiomer of a drug may be active, the other inactive or toxic).

### Diastereomers

**Diastereomers** are stereoisomers that are NOT mirror images. They arise when:
- A molecule has **2 or more chiral centers** and the configurations differ at **some but not all** centers.
- **Cis-trans (E/Z) isomers** around a double bond or ring.

Properties of diastereomers:
- **Different** physical properties (different melting points, boiling points, solubilities).
- **Different** chemical reactivities.
- This makes them **separable** by standard techniques (distillation, chromatography, crystallization), unlike enantiomers which require chiral resolution methods.

### Meso Compounds

A **meso compound** has chiral centers but possesses an **internal plane of symmetry**, making the molecule achiral overall. The chiral centers effectively cancel each other out.

Classic example: (2R,3S)-tartaric acid. It has two chiral centers, but the top half of the molecule is the mirror image of the bottom half. Therefore it is superimposable on its mirror image and is **optically inactive**.

**How to identify a meso compound:**
1. The molecule has 2 or more chiral centers.
2. There exists a plane of symmetry that divides the molecule into two mirror-image halves.
3. Alternatively: if inverting all stereocenters gives you the same molecule (superimposable), it is meso.

**MCAT Tip:** The question "how many stereoisomers does this molecule have?" requires checking for meso compounds. The maximum number of stereoisomers is 2^n (where n = number of chiral centers), but meso compounds reduce this number.

### Fischer Projections

Fischer projections are a 2D way to represent 3D stereochemistry, most commonly used for sugars and amino acids.

**Convention:**
- The carbon chain runs vertically, with the most oxidized carbon (e.g., aldehyde or carboxylic acid) at the top.
- **Horizontal bonds point toward you** (out of the page = wedge).
- **Vertical bonds point away from you** (into the page = dash).
- Each intersection represents a carbon atom.

**Manipulation rules:**
- **Rotating 90 degrees** changes the configuration (R becomes S). Do not do this.
- **Rotating 180 degrees** preserves the configuration. This is safe.
- **Swapping any two groups** once inverts the configuration. Swapping twice restores it.
- To determine R/S from a Fischer projection: assign priorities as normal. If the #4 priority group is on a vertical bond (pointing away from you), you can read R/S directly. If #4 is on a horizontal bond (pointing toward you), read the apparent rotation and reverse it.

**MCAT Tip:** For amino acids, the L-configuration (biologically relevant) has the amino group on the LEFT in a Fischer projection. For sugars, D-sugars (biologically relevant) have the OH on the bottom-most chiral center pointing to the RIGHT.

### Optical Activity

A **chiral, non-racemic** sample rotates the plane of plane-polarized light. This is measured with a polarimeter.

- **(+) or d (dextrorotatory):** Rotates light clockwise.
- **(-) or l (levorotatory):** Rotates light counterclockwise.

**There is NO correlation between R/S and +/-.** R does not mean + and S does not mean -. The sign of rotation must be determined experimentally.

**Specific rotation** [alpha] is a physical constant for a given compound:

$$[\alpha] = \frac{\alpha_{\text{observed}}}{c \times l}$$

where c = concentration (g/mL), l = path length (dm), and alpha_observed is the measured rotation in degrees.

**Racemic mixture:** A 50:50 mixture of enantiomers. The rotations cancel, so the mixture is **optically inactive** (observed rotation = 0). It is denoted as (+/-) or (d,l) or (rac).

**Enantiomeric excess (ee):**

$$\text{ee} = \frac{|\text{% major enantiomer} - \text{% minor enantiomer}|}{100} \times 100\%$$

Or equivalently:

$$\text{ee} = \frac{[\alpha]_{\text{observed}}}{[\alpha]_{\text{pure}}} \times 100\%$$

A racemic mixture has ee = 0%. A pure enantiomer has ee = 100%.

**MCAT Tip:** Specific rotation questions are essentially unit conversion / plug-and-chug. Make sure you know the formula and watch your units (concentration in g/mL, path length in dm, NOT cm).

### E/Z Nomenclature

E/Z is used for alkene stereoisomers when CIP priority rules are needed (as opposed to cis/trans, which only works when there are two identical substituents).

**Assign CIP priorities to the two substituents on each carbon of the double bond.** Then:
- **Z (zusammen, "together"):** The higher priority groups on each carbon are on the **same side** of the double bond.
- **E (entgegen, "opposite"):** The higher priority groups on each carbon are on **opposite sides** of the double bond.

**Mnemonic:** Z = "Zee same side." E = "opposite."

**Why does geometric isomerism exist?** Because the pi bond in a double bond **prevents rotation**. The two sides of the double bond are distinct, and groups cannot swap sides without breaking the pi bond (which requires ~260 kJ/mol of energy).

### Stereochemistry Decision Tree for MCAT Questions

When a stereochemistry question appears, run through this systematically:

```
1. Does the molecule have a chiral center?
   - Count carbons with 4 different substituents
   - If NO --> achiral, no optical activity, done
   - If YES --> continue

2. How many chiral centers?
   - If 1 --> two stereoisomers (one R, one S), they are enantiomers
   - If 2+ --> continue to step 3

3. Is there an internal plane of symmetry?
   - If YES --> meso compound (achiral, optically inactive)
   - If NO --> the molecule is chiral

4. Relationship between two stereoisomers:
   - Do they differ at ALL stereocenters? --> Enantiomers
   - Do they differ at SOME but not all? --> Diastereomers

5. For double bonds:
   - Can the substituents be assigned cis/trans? --> Use cis/trans
   - Need CIP priorities? --> Use E/Z
   - Cis/trans and E/Z isomers are diastereomers
```

### Stereochemistry Relationships at a Glance

| Relationship | Definition | Physical Properties | Optical Rotation | Separable? |
|---|---|---|---|---|
| **Enantiomers** | Mirror images, all centers inverted | Identical (in achiral environment) | Equal and opposite | Only by chiral methods |
| **Diastereomers** | Stereoisomers, not mirror images | Different | No simple relationship | Yes, by standard methods |
| **Meso** | Has stereocenters + internal symmetry | N/A (it is a single compound) | Optically inactive | N/A |
| **Constitutional isomers** | Same formula, different connectivity | Different | No relationship | Yes |

---

## High-Yield Summary Table

| Concept | What to Know Cold | Common MCAT Traps |
|---------|-------------------|-------------------|
| Lewis structures | Formal charge formula, resonance ranking rules | Forgetting expanded octets on S, P; misranking resonance contributors |
| VSEPR | Electron vs. molecular geometry, lone pair effects | Calling NH3 "tetrahedral" instead of "trigonal pyramidal" |
| Hybridization | sp/sp2/sp3 pattern, sigma vs. pi | Miscounting electron groups (lone pairs count!); forgetting that double bond = 1 sigma + 1 pi |
| Polarity | Vector sum of dipoles, symmetric cancellation | Assuming all molecules with polar bonds are polar (CCl4, CO2 are not) |
| IMFs | LDF < dipole-dipole < H-bonding < ion-dipole | Forgetting LDFs exist in polar molecules too; confusing H-bonding donor vs. acceptor |
| Chirality | 4 different groups = chiral center | Meso compounds (have stereocenters but are achiral) |
| R/S | CIP priority, orientation of #4 group | Double bond expansion; not going far enough along the chain for tiebreakers |
| Enantiomers vs. diastereomers | Mirror images vs. not | Assuming R = (+); forgetting diastereomers have different physical properties |
| Optical activity | Specific rotation formula, racemic = inactive | Unit errors (dm vs. cm); not recognizing a meso compound as optically inactive |
| E/Z | CIP priorities on double bond carbons | Confusing E/Z with R/S; assuming Z = cis always (it often is, but not always) |

---

*FC5B covers the bridge from atomic structure to molecular behavior. Master these topics and you will have the toolkit to tackle virtually any CP passage involving molecular properties, reactivity, or biological relevance of chemical structure.*
