# CP Gen Chem Chapter 3 — Bonding & Intermolecular Forces

Scope: Ionic bonds; covalent bonds; Lewis structures; formal charge; resonance; octet exceptions; VSEPR; bond polarity & dipole moments; intermolecular forces (LDF, dipole-dipole, H-bonding, ion-dipole).

**Section:** Chemical/Physical (CP)
**Book:** Kaplan General Chemistry — Chapter 3
**AAMC FC mapping:** FC5B (Lewis, VSEPR, polarity, IMFs)
**Yield:** HIGH — underlies virtually every CP passage involving molecules.

> Note: Orbital hybridization, sigma/pi bonds, and molecular orbital theory live in the orgo-side bonding chapter `CP_OC_Ch03_Bonding.md`. Cross-load both for full bonding coverage.

---

## 1. Ionic vs. Covalent Bonds

**Ionic bond:** Complete electron transfer from a metal to a nonmetal. Forms cations and anions held by electrostatic attraction in a crystal lattice. ΔEN > ~1.7.
- Properties: high melting/boiling points, brittle, conduct electricity when molten or dissolved, often soluble in water.

**Covalent bond:** Sharing of electrons between nonmetals. ΔEN < ~1.7.
- **Nonpolar covalent (ΔEN ~0–0.4):** equal sharing (C–H, C–C).
- **Polar covalent (ΔEN ~0.5–1.7):** unequal sharing (O–H, C=O).

**Coordinate (dative) covalent bond:** Both shared electrons come from one atom (e.g., NH3 → BF3 forming H3N–BF3). Once formed, indistinguishable from a normal covalent bond.

**Metallic bonding:** Delocalized "sea of electrons" shared across a lattice of metal cations. Explains conductivity, malleability, ductility, luster.

---

## 2. Lewis Structures

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

## 3. VSEPR Theory

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

## High-Yield Takeaways

1. **Lewis structures + formal charge** — best structure minimizes FCs and puts negative FC on more electronegative atoms.
2. **Resonance** stabilizes ions and explains acidity differences.
3. **VSEPR**: count electron groups, account for lone pairs.
4. **Polar bonds ≠ polar molecule** — geometry matters for dipole cancellation (CO2, CCl4, SF6 nonpolar despite polar bonds).
5. **IMF ranking:** ion-dipole > H-bonding > dipole-dipole > LDF.
6. **H-bonding requires H bonded to N, O, or F.**

---

→ Hybridization, sigma/pi, molecular orbitals: `CP_OC_Ch03_Bonding.md`
→ Stereochemistry & isomers: `CP_OC_Ch02_Isomers.md`
→ Phase changes & boiling points: `CP_GC_Ch07_Thermochemistry.md`
