# CP Orgo Chapter 2 — Isomers

Scope: Constitutional (structural) isomers; stereoisomers; chirality and chiral centers; R/S configuration (CIP rules); enantiomers; diastereomers; meso compounds; Fischer projections; optical activity; E/Z (cis/trans) nomenclature.

**Section:** Chemical/Physical (CP)
**Book:** Kaplan Organic Chemistry — Chapter 2
**AAMC FC mapping:** FC5B (stereochemistry portion)
**Yield:** HIGH — stereochemistry is one of the most heavily tested orgo topics. Requires systematic thinking, not memorization.

---

## 1. Isomer Classification

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

---

## 2. Constitutional (Structural) Isomers

Same molecular formula, **different connectivity**. The atoms are bonded to different partners.
- Butane vs. isobutane (same formula C4H10, different carbon skeleton)
- 1-propanol vs. 2-propanol (OH on different carbons)
- Ethanol vs. dimethyl ether (C2H6O — completely different functional groups)

These can have **very different** physical and chemical properties.

---

## 3. Chirality and Chiral Centers

A molecule is **chiral** if it is non-superimposable on its mirror image. The most common source of chirality is a **chiral center** (stereocenter): a carbon bonded to **four different substituents**.

How to identify chiral centers:
1. Look at each carbon in the molecule.
2. Check if it has 4 different groups attached. If yes, it is a chiral center.
3. A carbon with a double bond, or bonded to two identical groups, is NOT a chiral center.

**Important:** Chirality is a property of the whole molecule, not just the atom. A molecule can have chiral centers but still be achiral if it has an internal plane of symmetry (meso compound).

---

## 4. R/S Configuration (Cahn-Ingold-Prelog Rules)

This is the system for assigning absolute configuration to each chiral center. It is heavily tested.

**Step 1: Assign priorities (1-4) to the four substituents.**
- Higher atomic number = higher priority.
- If two substituents start with the same atom, move outward along the chain until you find a point of difference. Compare at the first point of difference.
- Double bonds count as two single bonds to the same atom (a C=O is treated as if C is bonded to O twice, and O is bonded to C twice). Triple bonds count as three.

**Step 2: Orient the molecule so priority 4 (lowest) points away from you** (into the page/back).

**Step 3: Trace a path from priority 1 to 2 to 3.**
- **Clockwise = R** (rectus, Latin for "right")
- **Counterclockwise = S** (sinister, Latin for "left")

**Shortcut when #4 is not pointing away:** If #4 is pointing toward you (coming out of the page as a wedge), determine the apparent rotation 1→2→3 and then **reverse** your answer. If it looks clockwise, it is actually S; if it looks counterclockwise, it is actually R.

**MCAT Tip:** CIP priority mistakes are the #1 source of errors on stereochemistry questions. Common traps:
- Forgetting that deuterium (D) has higher priority than hydrogen (H) (same atomic # = mass tiebreaker).
- Forgetting the double bond expansion rule.
- Rushing the comparison and not going far enough along the chain.

---

## 5. Enantiomers

**Enantiomers** are non-superimposable mirror images. They have the **opposite configuration at every chiral center** (all R become S, all S become R).

Properties of enantiomers:
- **Same** melting point, boiling point, density, solubility (in achiral solvents), Rf value.
- **Same** chemical reactivity with achiral reagents.
- **Opposite** optical rotation (if one is +30°, the other is -30°).
- **Different** reactivity with chiral reagents (e.g., enzymes, which are chiral).
- **Different** biological activity (one enantiomer of a drug may be active, the other inactive or toxic).

---

## 6. Diastereomers

**Diastereomers** are stereoisomers that are NOT mirror images. They arise when:
- A molecule has **2 or more chiral centers** and the configurations differ at **some but not all** centers.
- **Cis-trans (E/Z) isomers** around a double bond or ring.

Properties of diastereomers:
- **Different** physical properties (different melting points, boiling points, solubilities).
- **Different** chemical reactivities.
- This makes them **separable** by standard techniques (distillation, chromatography, crystallization), unlike enantiomers which require chiral resolution methods.

**Epimers** (subset of diastereomers): differ at exactly one chiral center. Glucose vs. galactose are C4 epimers; glucose vs. mannose are C2 epimers.

**Anomers:** Sugar diastereomers that differ at the anomeric carbon (the new stereocenter formed during cyclization). α (axial -OH) vs β (equatorial -OH).

---

## 7. Meso Compounds

A **meso compound** has chiral centers but possesses an **internal plane of symmetry**, making the molecule achiral overall. The chiral centers effectively cancel each other out.

Classic example: (2R,3S)-tartaric acid. It has two chiral centers, but the top half of the molecule is the mirror image of the bottom half. Therefore it is superimposable on its mirror image and is **optically inactive**.

**How to identify a meso compound:**
1. The molecule has 2 or more chiral centers.
2. There exists a plane of symmetry that divides the molecule into two mirror-image halves.
3. Alternatively: if inverting all stereocenters gives you the same molecule (superimposable), it is meso.

**MCAT Tip:** "How many stereoisomers does this molecule have?" requires checking for meso compounds. The maximum number of stereoisomers is 2^n (where n = number of chiral centers), but meso compounds reduce this number.

---

## 8. Fischer Projections

Fischer projections are a 2D way to represent 3D stereochemistry, most commonly used for sugars and amino acids.

**Convention:**
- The carbon chain runs vertically, with the most oxidized carbon (e.g., aldehyde or carboxylic acid) at the top.
- **Horizontal bonds point toward you** (out of the page = wedge).
- **Vertical bonds point away from you** (into the page = dash).
- Each intersection represents a carbon atom.

**Manipulation rules:**
- **Rotating 90°** changes the configuration (R becomes S). Do not do this.
- **Rotating 180°** preserves the configuration. This is safe.
- **Swapping any two groups** once inverts the configuration. Swapping twice restores it.
- To determine R/S from a Fischer projection: assign priorities as normal. If #4 is on a vertical bond (pointing away), read R/S directly. If #4 is on a horizontal bond (pointing toward you), read the apparent rotation and reverse it.

**MCAT Tip:** For amino acids, the L-configuration (biologically relevant) has the amino group on the LEFT in a Fischer projection. For sugars, D-sugars (biologically relevant) have the OH on the bottom-most chiral center pointing to the RIGHT.

---

## 9. Optical Activity

A **chiral, non-racemic** sample rotates the plane of plane-polarized light. This is measured with a polarimeter.

- **(+) or d (dextrorotatory):** Rotates light clockwise.
- **(-) or l (levorotatory):** Rotates light counterclockwise.

**There is NO correlation between R/S and +/-.** R does not mean + and S does not mean -. The sign of rotation must be determined experimentally.

**Specific rotation** [α] is a physical constant for a given compound:

$$[\alpha] = \frac{\alpha_{\text{observed}}}{c \times l}$$

where c = concentration (g/mL), l = path length (dm), and α_observed is the measured rotation in degrees.

**Racemic mixture:** A 50:50 mixture of enantiomers. The rotations cancel, so the mixture is **optically inactive** (observed rotation = 0). Denoted (±) or (d,l) or (rac).

**Enantiomeric excess (ee):**

ee = |%major - %minor| / 100 × 100%

Or equivalently:

ee = [α]_observed / [α]_pure × 100%

A racemic mixture has ee = 0%. A pure enantiomer has ee = 100%.

**MCAT Tip:** Specific rotation problems are unit-conversion. Watch units (concentration in g/mL, path length in dm — NOT cm).

---

## 10. E/Z Nomenclature (Alkene Stereoisomerism)

E/Z is used for alkene stereoisomers when CIP priority rules are needed (vs cis/trans, which only works when there are two identical substituents).

**Assign CIP priorities to the two substituents on each carbon of the double bond.** Then:
- **Z (zusammen, "together"):** The higher priority groups on each carbon are on the **same side** of the double bond.
- **E (entgegen, "opposite"):** The higher priority groups are on **opposite sides**.

**Mnemonic:** Z = "Zee same side." E = "opposite."

**Why does geometric isomerism exist?** Because the pi bond in a double bond **prevents rotation**. The two sides of the double bond are distinct, and groups cannot swap sides without breaking the pi bond (~260 kJ/mol).

---

## 11. Stereochemistry Decision Tree

When a stereochemistry question appears:

```
1. Does the molecule have a chiral center?
   - Count carbons with 4 different substituents
   - If NO → achiral, no optical activity, done
   - If YES → continue

2. How many chiral centers?
   - If 1 → two stereoisomers (one R, one S), they are enantiomers
   - If 2+ → continue to step 3

3. Is there an internal plane of symmetry?
   - If YES → meso compound (achiral, optically inactive)
   - If NO → the molecule is chiral

4. Relationship between two stereoisomers:
   - Differ at ALL stereocenters → Enantiomers
   - Differ at SOME but not all → Diastereomers

5. For double bonds:
   - Two identical substituents on a C → use cis/trans
   - Need CIP → use E/Z
   - Cis/trans and E/Z isomers are diastereomers
```

---

## 12. Stereochemistry Relationships at a Glance

| Relationship | Definition | Physical Properties | Optical Rotation | Separable? |
|---|---|---|---|---|
| **Enantiomers** | Mirror images, all centers inverted | Identical (in achiral environment) | Equal and opposite | Only by chiral methods |
| **Diastereomers** | Stereoisomers, not mirror images | Different | No simple relationship | Yes, by standard methods |
| **Meso** | Has stereocenters + internal symmetry | N/A (single compound) | Optically inactive | N/A |
| **Constitutional isomers** | Same formula, different connectivity | Different | No relationship | Yes |

---

## High-Yield Takeaways

1. **Chiral center = 4 different groups on a carbon.**
2. **CIP priority = atomic number → tie-break along chain → double bonds count twice.**
3. **R = clockwise (with #4 back); S = counterclockwise.** Reverse if #4 is pointing toward you.
4. **Enantiomers = identical physical props (achiral env), opposite optical rotation, different bio activity.**
5. **Diastereomers = different physical props, separable.**
6. **Meso = chiral centers + internal symmetry → optically inactive.**
7. **Max stereoisomers = 2^n** (n = chiral centers), reduced by meso.
8. **R/S has no relation to +/-** — sign of rotation must be experimentally determined.
9. **Z = same side, E = opposite side** for high-priority groups on alkene carbons.
10. **Fischer projection:** horizontal = wedge, vertical = dash. 180° rotation safe; 90° flips config.

---

→ Bonding & sigma/pi (why pi bond prevents rotation): `CP_OC_Ch03_Bonding.md`
→ Sugar anomers/epimers: `BB_Ch04_Carbohydrates.md`
→ Amino acid L-configuration & D-sugars: `BB_Ch01_AminoAcids_Proteins.md`
→ Carbonyl chirality (asymmetric synthesis): `CP_OC_Ch06_Aldehydes_Ketones_I.md`
