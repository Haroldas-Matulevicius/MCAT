# CP Orgo Chapter 2 — Isomers

Scope: Constitutional vs stereoisomers; chirality; R/S (CIP); enantiomers; diastereomers; meso; Fischer; optical activity; E/Z.

AAMC FC mapping: FC5B (stereochem)

Kaplan: Organic Chemistry Ch 2

---

ISOMER CLASSIFICATION:
- Same MF? → isomers
  - Same connectivity? NO → constitutional/structural (butane vs isobutane, EtOH vs DME)
  - Same connectivity? YES → stereoisomers
    - Mirror images? YES → enantiomers
    - Mirror images? NO → diastereomers (incl cis/trans, E/Z, partial-stereocenter mismatch)

CHIRAL CENTER:
- C with 4 DIFFERENT substituents
- Achiral if double bond or two identical groups
- Molecule chiral overall if non-superimposable on mirror image
- Meso: has stereocenters but internal symmetry → achiral overall

R/S (CIP RULES):
1. Priority by atomic number; tiebreak along chain
2. Double bond = 2 single bonds to same atom; triple = 3
3. Orient #4 (lowest) AWAY (into page)
4. Trace 1→2→3:
   - Clockwise = R
   - Counterclockwise = S
- If #4 toward you: read apparent rotation, REVERSE
- D > H (same Z, mass tiebreaker)

ENANTIOMERS (mirror images, all centers flipped):
- Same: BP, MP, density, solubility (achiral solvent), Rf
- Same: rxn w/ achiral reagents
- Opposite: optical rotation
- Different: rxn w/ chiral reagents (enzymes), biological activity
- Separable only by chiral resolution

DIASTEREOMERS (stereoisomers, not mirror images):
- Different physical AND chemical properties
- Separable by standard methods (distillation, chrom, crystallization)
- Includes cis/trans, E/Z, partial-mismatch chirality
- Epimers (subset): differ at 1 chiral center (glu vs gal = C4 epimers)
- Anomers (subset): sugars differ at anomeric C (α axial vs β equatorial)

MESO COMPOUNDS:
- ≥2 chiral centers + internal plane of symmetry
- Optically inactive (rotations cancel internally)
- (2R,3S)-tartaric acid classic example
- Reduces max stereoisomer count below 2^n

FISCHER PROJECTIONS:
- Vertical = dashes (away); horizontal = wedges (toward you)
- Most-oxidized C at top
- 180° rotation: SAFE (preserves config)
- 90° rotation: changes R↔S (don't do)
- Single swap: inverts; double swap: preserves
- AAs: L = NH2 on LEFT
- Sugars: D = -OH on RIGHT at lowest chiral C

OPTICAL ACTIVITY:
- (+) dextrorotatory; (-) levorotatory
- R/S has NO relation to +/- (must measure experimentally)
- [α] = α_observed / (c · l); c = g/mL, l = dm
- Racemic = 50:50 enantiomers, optically inactive
- ee = |%major - %minor|/100 × 100% = [α]_obs/[α]_pure × 100%

E/Z (alkene stereoisomers):
- CIP priorities on each C of C=C
- Z (zusammen = together): higher priorities SAME side
- E (entgegen = opposite): higher priorities OPPOSITE sides
- Pi bond prevents rotation (~260 kJ/mol)

DECISION TREE:
1. Chiral center? Count C w/ 4 diff substituents. None → achiral.
2. # chiral centers: 1 → enantiomers; 2+ → continue
3. Internal symmetry? YES → meso. NO → chiral.
4. Compare two stereoisomers:
   - All centers differ → enantiomers
   - Some differ → diastereomers
5. Double bonds: 2 identical groups → cis/trans; CIP needed → E/Z

RELATIONSHIPS TABLE:
| Type | Phys props | Optical | Separable? |
|---|---|---|---|
| Enantiomers | Same (achiral env) | Equal/opposite | Chiral methods |
| Diastereomers | Different | Variable | Standard |
| Meso | -- | Inactive | -- |
| Constitutional | Different | -- | Standard |

→ Pi bond rotation barrier → Ch03
→ Sugar anomers/epimers → BB_Ch04
→ AA L-configuration → BB_Ch01
