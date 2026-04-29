# CP Orgo Chapter 7 — Aldehydes & Ketones II (Enolates and Aldol)

Scope: Alpha-hydrogen acidity; keto-enol tautomerism; enolate formation and reactivity; aldol condensation; retro-aldol; alpha-alkylation; biological aldol/retro-aldol (glycolysis).

**Section:** Chemical/Physical (CP)
**Book:** Kaplan Organic Chemistry — Chapter 7
**AAMC FC mapping:** FC5D (enolate chemistry)
**Yield:** HIGH — aldol condensation appears as a passage mechanism, and retro-aldol is the mechanism of fructose-1,6-bisphosphate cleavage in glycolysis (huge biochem connection).

---

## 1. Alpha Hydrogens and Their Acidity

The **alpha (α) carbon** is the carbon directly adjacent to a carbonyl. **Alpha hydrogens** are the H's on that alpha carbon.

**Alpha H's are unusually acidic** for C-H bonds:
- Ketone α-H: pKa ~20
- Aldehyde α-H: pKa ~17 (slightly more acidic than ketones)
- Ester α-H: pKa ~25
- 1,3-dicarbonyl (between two carbonyls): pKa ~5-13 (e.g., malonic ester ~13, acetylacetone ~9)

For comparison: a normal C-H on alkane ~50; alcohol O-H ~16; water 15.7. So ketone α-H is ~30 orders of magnitude more acidic than alkane C-H, but still less acidic than alcohols.

### Why Are Alpha H's Acidic?

The conjugate base — the **enolate** — is **resonance-stabilized**: the negative charge can be drawn either on the alpha carbon (carbanion) or delocalized onto the carbonyl oxygen (alkoxide form). The oxygen-based resonance structure is the major contributor (more stable — negative charge on more electronegative atom).

```
O                O⁻              O⁻
||               |               |
C─CH₂   ⇌   C=CH    or    C─CH²⁻
  α            α               α
(keto enolate)   (carbanion form)   (oxygen-localized)
```

**1,3-dicarbonyls** are far more acidic because the enolate is doubly resonance-stabilized — negative charge can delocalize onto **two** oxygens, not just one.

---

## 2. Keto-Enol Tautomerism

The **enol** is the tautomer where the proton has shifted from alpha-C to carbonyl-O, and a C=C double bond forms.

```
    O              OH
    ||             |
R—C—CH₂—R'  ⇌  R—C=CH—R'
    keto          enol
```

**Tautomers** are constitutional isomers that interconvert by proton migration. They are NOT resonance structures (atoms moved).

**Key facts:**
- Keto form is almost always more stable and predominant at equilibrium (~99.99% keto for typical ketones).
- **Exception:** 1,3-dicarbonyls and phenols, where the enol form is stabilized (intramolecular H-bonding, conjugation, aromaticity).
- Tautomerization is catalyzed by both acid and base.

**Why phenol exists as the enol:** The "keto" form of phenol would be cyclohexa-2,4-dienone, which loses aromaticity. Phenol is essentially 100% enol because of aromaticity.

---

## 3. Enolate Formation

To deprotonate an alpha H, you need a base whose conjugate acid pKa > pKa of the alpha H.

| Base | Conjugate acid pKa | Use |
|---|---|---|
| NaOH | 15.7 | Limited — only partial deprotonation of α-H (pKa 20) |
| NaOR (alkoxide) | 16-18 | Same — partial enolate |
| LDA (lithium diisopropylamide) | 36 | Quantitative deprotonation; forms enolate completely |
| NaH | 36 | Strong, irreversible base |

**LDA** is the workhorse for forming enolates cleanly. It's a bulky, very strong base — it grabs the α-H without doing nucleophilic addition itself.

**Kinetic vs Thermodynamic Enolates** (high-yield concept):
- **Kinetic enolate:** Forms faster. Less substituted C=C. Use LDA at low temperature (-78°C). Less stable but more accessible.
- **Thermodynamic enolate:** More substituted C=C, more stable. Use weaker base, higher T, equilibrium conditions.

This matters when a ketone has α-H's on both sides — different conditions select different enolates.

---

## 4. Aldol Condensation

The flagship reaction of enolate chemistry.

### Mechanism (Base-Catalyzed)

1. Base removes α-H from one carbonyl molecule → enolate.
2. The enolate (nucleophilic α-C) attacks the carbonyl C of another aldehyde/ketone molecule.
3. Tetrahedral alkoxide intermediate.
4. Protonation gives the **aldol product**: a **β-hydroxy carbonyl** (an alcohol on the β-carbon, three away from the original carbonyl C).
5. **If heated, dehydration occurs:** loss of water gives an **α,β-unsaturated carbonyl** (an enone — the **aldol condensation product**).

```
2 CH₃-CHO  --base-->   CH₃-CH(OH)-CH₂-CHO   --heat-->   CH₃-CH=CH-CHO
acetaldehyde            β-hydroxy aldehyde            α,β-unsaturated aldehyde
                        (aldol product)              (aldol condensation product)
```

**Naming convention:** "Aldol" = aldol product (β-hydroxy carbonyl). "Aldol condensation" = condensation product (α,β-unsaturated carbonyl, after H₂O loss).

### Acid-Catalyzed Aldol (Less Common)

Acid converts one molecule to its enol form (nucleophilic α-C), and protonates another carbonyl (more electrophilic). Same overall result.

### Crossed (Mixed) Aldol

When two different carbonyls are mixed, you can get up to **4 products** (each carbonyl can be the enolate or the electrophile). Usually messy unless:
1. One carbonyl has no α-H (e.g., formaldehyde, benzaldehyde) → must be the electrophile.
2. Use a directed strategy (form enolate of one with LDA at low T, then add the other).

---

## 5. Retro-Aldol

The reverse reaction: a β-hydroxy carbonyl breaks into two smaller carbonyl compounds.

This is important in **glycolysis**:
- Fructose-1,6-bisphosphate (a β-hydroxy carbonyl in disguise) is split by **aldolase** into **dihydroxyacetone phosphate (DHAP)** and **glyceraldehyde-3-phosphate (G3P)** via a **retro-aldol mechanism**.

This connection is high-yield: the MCAT often gives a passage on glycolysis and asks about the mechanism of aldolase.

**Mechanism (in glycolysis): aldolase forms a Schiff base** (imine) between an active-site lysine and the C2 carbonyl of fructose-1,6-bisphosphate, which activates the molecule for retro-aldol cleavage. Both Schiff base AND aldol/retro-aldol are CP topics — they appear together in biochem.

---

## 6. Alpha-Alkylation

Once you have an enolate, you can alkylate the alpha carbon:

Enolate + R-X (alkyl halide) → α-alkylated carbonyl

The alpha carbon (nucleophilic in enolate form) attacks the alkyl halide carbon (electrophilic) via SN2. Net result: a new C-C bond at the alpha position.

**Limitations:** Works best with primary alkyl halides (SN2-friendly). Tertiary halides give E2 instead.

**Variations:**
- **Acetoacetic ester synthesis** (using ethyl acetoacetate, a 1,3-dicarbonyl with α-H pKa ~11): produces methyl ketones.
- **Malonic ester synthesis** (using diethyl malonate, α-H pKa ~13): produces carboxylic acids.

These are classic synthetic strategies but lower-yield on the MCAT.

---

## 7. α,β-Unsaturated Carbonyls (Conjugate Addition)

When you dehydrate an aldol, you get an α,β-unsaturated carbonyl (enone). These have **two electrophilic sites**: the carbonyl C (1,2-addition) and the β-carbon (1,4-addition or "conjugate" / Michael addition).

- **1,2-addition:** typical nucleophiles (RMgX, NaBH₄ at low T, LiAlH₄) attack the carbonyl C directly.
- **1,4-addition (Michael):** soft nucleophiles (cuprates R₂CuLi, enolates, amines, thiols) attack the β-carbon. The carbonyl O ends up with a charge that's quenched on workup.

**MCAT relevance:** Michael additions are key in biosynthesis — many enzymatic reactions involve nucleophilic attack on α,β-unsaturated carbonyl systems.

---

## High-Yield Takeaways

1. **α-H pKa: ketone ~20, aldehyde ~17, ester ~25, 1,3-dicarbonyl ~5-13.**
2. **Enolate is resonance-stabilized;** O-localized form is the major contributor.
3. **Keto > enol** at equilibrium (except 1,3-dicarbonyl, phenol).
4. **LDA** is the standard base for clean enolate formation (pKa of conjugate acid ~36).
5. **Aldol product = β-hydroxy carbonyl;** after heat → α,β-unsaturated carbonyl (aldol condensation).
6. **Retro-aldol cleaves fructose-1,6-bisP → DHAP + G3P** in glycolysis (aldolase enzyme).
7. **α-Alkylation** with primary alkyl halides via SN2.
8. **Michael addition (1,4)** of soft nucleophiles to α,β-unsaturated carbonyls.

---

→ Carbonyl properties & nucleophilic addition: `CP_OC_Ch06_Aldehydes_Ketones_I.md`
→ Imine formation (Schiff base in aldolase mechanism): `CP_OC_Ch06_Aldehydes_Ketones_I.md`
→ Glycolysis aldolase step: `BB_Ch09_CarbMetab1.md`
→ Acid-base / pKa fundamentals: `CP_GC_Ch10_Acids_Bases.md`
