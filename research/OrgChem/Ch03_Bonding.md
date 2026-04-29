# CP Orgo Chapter 3 — Bonding (Atomic & Molecular Orbitals, Hybridization)

Scope: Atomic orbitals & quantum number recap; molecular orbital theory (bonding/antibonding, σ vs π); hybridization (sp, sp², sp³); sigma vs pi bonds; hybridization in common functional groups.

**Section:** Chemical/Physical (CP)
**Book:** Kaplan Organic Chemistry — Chapter 3
**AAMC FC mapping:** FC5B (orbital/hybridization portion)
**Yield:** HIGH — sigma vs pi counts and hybridization questions appear constantly. Sets up reactivity reasoning.

> Note: Lewis structures, VSEPR, IMFs, bond polarity live in `CP_GC_Ch03_Bonding.md` (gen-chem-side bonding chapter). Cross-load both for full bonding coverage. Atomic-structure quantum numbers live in `CP_GC_Ch01_Atomic_Structure.md`.

---

## 1. Atomic Orbital Recap (Brief)

(See `CP_GC_Ch01_Atomic_Structure.md` for full quantum-number treatment.)

**Atomic orbitals** are probability distributions for electrons. Defined by:
- n (principal): energy level / shell
- l (angular momentum): subshell shape (s, p, d, f)
- m_l (magnetic): orientation
- m_s (spin): ±½

**Shapes:**
- **s** orbitals: spherical (1 per shell)
- **p** orbitals: dumbbell, three orientations (px, py, pz) per shell starting at n=2
- **d** orbitals: cloverleaf, five per shell starting at n=3
- **f** orbitals: complex, seven per shell starting at n=4

For organic chemistry, the s and p orbitals of C, N, O, halogens are what matter. Bonding occurs through orbital overlap.

---

## 2. Molecular Orbital (MO) Theory

When two atomic orbitals combine, they produce two molecular orbitals:

- **Bonding MO:** Lower energy than the parent atomic orbitals. Electron density concentrated BETWEEN the two nuclei. Stabilizes the bond.
- **Antibonding MO (denoted *):** Higher energy than the parent atomic orbitals. Has a node between the nuclei (zero electron density there). Destabilizes the bond if occupied.

**Bond order = (bonding e⁻ - antibonding e⁻) / 2.**
- Bond order > 0 → stable bond exists.
- Bond order = 0 → no net bond (e.g., He₂ doesn't exist).

**Example:** O₂ has both σ and π bonds, plus 2 unpaired electrons in degenerate π* antibonding orbitals → diradical, paramagnetic. Hund's rule still applies in MOs.

**Why MO theory matters for MCAT:**
- Explains paramagnetism of O₂ (Lewis structures don't).
- Explains delocalization in conjugated systems (alternating double bonds → continuous π system above and below the plane).
- Underlies UV-Vis spectroscopy (electronic transitions are between MOs).

---

## 3. Hybridization

Hybridization explains bonding geometry by mixing atomic orbitals into hybrid orbitals of equal energy. For the MCAT, this is essentially a shortcut: **count the electron groups, and you know the hybridization.**

### The Core Pattern

| Electron Groups | Hybridization | Geometry | Bond Angle | Bond Types |
|:-:|---|---|:-:|---|
| 2 | **sp** | Linear | 180° | 2 σ bonds (+ up to 2 π bonds) |
| 3 | **sp²** | Trigonal planar | 120° | 3 σ bonds (+ up to 1 π bond) |
| 4 | **sp³** | Tetrahedral | 109.5° | 4 σ bonds (no π bonds) |

**The number of electron groups = the number of hybrid orbitals = the number in the superscript plus 1.**
- sp = 2 hybrid orbitals (1 s + 1 p)
- sp² = 3 hybrid orbitals (1 s + 2 p)
- sp³ = 4 hybrid orbitals (1 s + 3 p)

Leftover unhybridized p orbitals form **π bonds**:
- sp³: 0 unhybridized p orbitals, so no π bonds.
- sp²: 1 unhybridized p orbital, so up to 1 π bond (one double bond).
- sp: 2 unhybridized p orbitals, so up to 2 π bonds (one triple bond, or two double bonds).

---

## 4. Sigma vs. Pi Bonds

| Property | Sigma (σ) | Pi (π) |
|----------|------|------|
| **Overlap** | Head-on (along bond axis) | Lateral/sideways (above and below bond axis) |
| **Rotation** | Free rotation around bond | Restricted rotation -- breaking pi bond costs energy |
| **Strength** | Stronger individually | Weaker individually |
| **Per bond** | Every bond has exactly 1 σ | Double = 1 σ + 1 π; Triple = 1 σ + 2 π |
| **Formed by** | Hybrid orbitals | Unhybridized p orbitals |

**Quick bond-counting method:**
- Single bond = 1 σ, 0 π
- Double bond = 1 σ, 1 π
- Triple bond = 1 σ, 2 π
- Total σ bonds in a molecule = total number of bonds drawn as lines (every connection is at least 1 σ)

**MCAT Tip:** A question that asks "how many sigma and pi bonds are in this molecule?" is really just asking you to count single, double, and triple bonds. Do not overthink it.

**Why double bonds prevent rotation:** The π bond requires sideways overlap of p orbitals. To rotate, you'd have to break this overlap (the p orbitals would no longer be aligned). This costs ~260 kJ/mol — essentially insurmountable at room temperature. This is why E/Z (cis/trans) isomers exist for alkenes.

**Bond strength:** A C-C single bond ~347 kJ/mol; C=C double bond ~614 kJ/mol (1 σ ~347 + 1 π ~267). Note π is weaker than σ.

---

## 5. Hybridization in Common Functional Groups

| Functional Group | Carbon Hybridization | Notes |
|-----------------|---------------------|-------|
| Alkane C-C | sp³ | All single bonds |
| Alkene C=C | sp² | One π bond, planar around the double bond |
| Alkyne C≡C | sp | Two π bonds, linear |
| Carbonyl C=O | sp² | Aldehydes, ketones, carboxylic acids, esters, amides |
| Aromatic ring C | sp² | Delocalized π system (continuous around ring) |
| Nitrile C≡N | sp | Linear |
| Carbocation (R₃C+) | sp² | Empty p orbital perpendicular to plane |
| Carbanion (R₃C:⁻) | sp³ generally; sp² if stabilized by adjacent π | Lone pair counts as electron group |

**MCAT Tip:** Nitrogen and oxygen hybridization follow the same electron-group counting rules.
- N in an amine (R-NH₂): sp³ (3 bonds + 1 lone pair = 4 groups)
- N in an amide: sp² (lone pair delocalized into the C=O π system; gives the amide its planarity and partial double-bond character)
- O in water: sp³ (2 bonds + 2 lone pairs = 4 groups)
- O in carbonyl C=O: sp²

---

## 6. Aromaticity (Quick Reference)

A planar cyclic system is aromatic if:
1. **Continuous ring of p orbitals** (every atom in the ring is sp² with a p orbital perpendicular to the plane)
2. **Hückel's rule:** contains (4n + 2) π electrons (n = 0, 1, 2, ...)
3. Planar.

Benzene: 6 π electrons (n = 1) → aromatic. Highly stable. The delocalization energy is ~150 kJ/mol below predicted from isolated double bonds.

**Antiaromatic (less stable):** 4n π electrons in a planar cyclic system (e.g., cyclobutadiene). Unstable.

**Non-aromatic:** Doesn't satisfy planarity or continuous-p requirement. Cyclohexane is non-aromatic (sp³ carbons).

**MCAT relevance:** Recognizing aromaticity explains stability and reactivity (electrophilic aromatic substitution rather than addition).

---

## High-Yield Takeaways

1. **Count electron groups → hybridization** (2 = sp, 3 = sp², 4 = sp³).
2. **Sigma per bond = number of lines drawn.** Pi: double = 1, triple = 2.
3. **Sigma rotates freely; pi locks rotation** → E/Z isomerism.
4. **Carbonyl C is sp²** (3 groups: 2 σ + 1 π in C=O).
5. **Amide N is sp²** (lone pair conjugates into C=O), explaining peptide bond planarity.
6. **MO theory:** bond order = (bonding − antibonding)/2; explains O₂'s paramagnetism.
7. **Aromaticity:** planar, continuous p, 4n+2 π electrons (Hückel).

---

→ Lewis, VSEPR, IMFs, polarity: `CP_GC_Ch03_Bonding.md`
→ Atomic orbitals & quantum numbers: `CP_GC_Ch01_Atomic_Structure.md`
→ Stereochemistry (why pi bonds give E/Z): `CP_OC_Ch02_Isomers.md`
→ Conjugation/UV-Vis: `CP_OC_Ch11_Spectroscopy.md`
