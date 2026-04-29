# CP Orgo Chapter 4 — Analyzing Organic Reactions

Scope: Acids and bases in orgo (pKa-based reasoning); nucleophiles, electrophiles, leaving groups; oxidation–reduction in orgo; chemoselectivity; the six problem-solving steps for orgo reactions.

**Section:** Chemical/Physical (CP)
**Book:** Kaplan Organic Chemistry — Chapter 4
**AAMC FC mapping:** FC5D (mechanism reasoning)
**Yield:** HIGH — this is the **lens** through which all subsequent orgo chapters are read. Mastery here turns memorization-heavy chapters into predictable patterns.

> Note: Specific SN1/SN2/E1/E2 decision trees are taught alongside alcohols and alkyl halides — see `CP_OC_Ch05_Alcohols.md` for substitution/elimination at sp³ carbons in alcohol contexts. The framework below sets up the reasoning.

---

## 1. Acids and Bases in Orgo

Orgo uses BOTH Bronsted-Lowry AND Lewis definitions extensively. (See `CP_GC_Ch10_Acids_Bases.md` for foundational acid-base chemistry.)

**Key pKa values to know cold:**

| Compound class | Approximate pKa | Notes |
|---|---|---|
| HCl, HBr, HI, H₂SO₄ | -7 to -10 | Strong acids (full dissociation) |
| Carboxylic acid (R-COOH) | ~4-5 | Acetic acid 4.76 |
| Phenol (Ar-OH) | ~10 | More acidic than alcohol due to resonance |
| Ammonium (R-NH₃+) | ~10 | Conjugate acid of amine |
| Water | 15.7 | (= -log Kw / 55.5 M for water as acid) |
| Alcohol (R-OH) | ~16-18 | Methanol 15.5, ethanol 16, t-butanol 18 |
| Alpha-H to carbonyl | ~20 (ketone), ~25 (ester) | Stabilized by enolate resonance |
| Terminal alkyne (R-C≡C-H) | ~25 | sp C is more acidic than sp²/sp³ |
| Amine N-H (R₂N-H) | ~36-38 | Very weak acid |
| Alkane C-H | ~50 | Essentially non-acidic |

**Why these pKas matter:**
- A reaction "works" if the equilibrium favors deprotonation by ≥ 10⁴ — i.e., the base is at least 4 pKa units more basic than the acid's conjugate base.
- Carboxylic acid (pKa 4) + bicarbonate (pKa of H₂CO₃ ~6.4) → reaction proceeds (carboxylate forms).
- Alcohol (pKa 16) + NaH (conjugate H₂, pKa 36) → strongly favored (alkoxide forms).

**Acidity trend rationale (high-yield):**
- **Resonance:** Carboxylate spreads negative charge over 2 O's → more acidic than alcohol (alkoxide localized on 1 O).
- **Electronegativity:** O-H > N-H > C-H acidity, because more electronegative atoms stabilize the negative charge better.
- **Hybridization:** sp C-H > sp² C-H > sp³ C-H acidity. More s-character holds electrons closer → easier to ionize.
- **Inductive effect:** Electron-withdrawing groups (Cl, F, NO₂) near an acidic H lower pKa (more acidic). Trichloroacetic acid (pKa 0.7) >> acetic acid (4.76).

---

## 2. Nucleophiles, Electrophiles, Leaving Groups

Most organic reactions can be reduced to: **nucleophile attacks electrophile; leaving group leaves.**

### Nucleophiles

A **nucleophile** is electron-rich and donates an electron pair to form a new bond. It IS a Lewis base.

**Strength factors:**
- **Charge:** Negative > neutral (RO⁻ > ROH).
- **Electronegativity:** Less EN = better nucleophile (down a group). I⁻ > Br⁻ > Cl⁻ > F⁻ in protic solvents (polarizability matters more than basicity); reverses in polar aprotic solvents (basicity dominates).
- **Steric bulk:** Bulky nucleophiles (t-BuO⁻, LDA) are poor nucleophiles but good bases — they can't reach the electrophile but can grab a peripheral H.
- **Resonance stabilization:** A delocalized nucleophile is weaker than a localized one.

**Common nucleophiles:** OH⁻, RO⁻, RS⁻, CN⁻, NH₃, RNH₂, H₂O, ROH, halide ions, alkoxides, enolates, organometallics (RMgX, RLi).

### Electrophiles

An **electrophile** is electron-poor and accepts an electron pair. It IS a Lewis acid.

**Common electrophiles:**
- Carbonyl C (δ+ from O electronegativity): C=O of aldehydes, ketones, carboxylic acid derivatives.
- Carbocations (R₃C+).
- Alkyl halides (C bonded to leaving group; partial δ+ on C).
- Halogens (Cl₂, Br₂) in electrophilic addition to alkenes.
- H+ (proton itself).

### Leaving Groups

A **leaving group (LG)** departs with the electron pair from the bond it leaves.

**Good LG = stable as an anion (or neutral molecule) after leaving.**

| Leaving group | Quality | Reason |
|---|---|---|
| I⁻, Br⁻, Cl⁻ | Excellent → Good | Halides; weak conjugate bases of strong acids |
| H₂O (from ROH₂+) | Good | Neutral after leaving; that's why you protonate alcohols before SN1/SN2 |
| Tosylate (-OTs), mesylate (-OMs) | Excellent | Designed leaving groups (sulfonate esters) |
| F⁻ | Poor | Strong conjugate base (HF is weak acid) |
| ⁻OH | Poor | Strong base; you do NOT push out OH⁻ in SN1/SN2 of alcohols |
| ⁻NH₂, ⁻OR | Poor | Strong bases |

**General rule:** A leaving group's quality correlates inversely with its conjugate acid's pKa. The lower the pKa, the better the leaving group. (HCl pKa -7 → Cl⁻ is great; NH₃ pKa ~36 → ⁻NH₂ is terrible.)

---

## 3. Oxidation–Reduction in Orgo

In organic chemistry, oxidation and reduction are usually tracked by counting C-H vs C-X (X = O, N, halogen) bonds.

**Oxidation:** ↑ bonds to heteroatom (O, N, halogen) OR ↓ bonds to H. Often involves loss of H₂ (dehydrogenation) or addition of O.

**Reduction:** ↓ bonds to heteroatom OR ↑ bonds to H. Addition of H₂ (hydrogenation), or loss of O.

### Common Orgo Oxidation Levels of Carbon

| Bonds to O (or N, X) | Examples | Oxidation level |
|---|---|---|
| 0 | Alkane (C-C, C-H only) | 0 |
| 1 | Alcohol (C-O), amine (C-N), alkyl halide (C-X), alkene (C=C counts as one) | 1 |
| 2 | Aldehyde (C=O + C-H), ketone (C=O), gem-diol, hemiacetal | 2 |
| 3 | Carboxylic acid (C=O + C-O), ester, amide, anhydride, acyl halide, nitrile | 3 |
| 4 | CO₂ | 4 |

### Common Oxidation/Reduction Reagents

**Oxidizing agents:**
- KMnO₄ — strong; oxidizes alcohols all the way to carboxylic acids; cleaves alkenes (cold dilute → diol; hot/concentrated → cleavage)
- CrO₃ / H₂SO₄ (Jones reagent), Na₂Cr₂O₇ — strong; primary alcohol → carboxylic acid
- PCC (pyridinium chlorochromate) — mild; primary alcohol → aldehyde (stops there); secondary → ketone
- Tollens (Ag(NH₃)₂+) — mild; aldehyde → carboxylic acid (positive: silver mirror)
- Ozone (O₃) followed by reductive workup (Zn, dimethyl sulfide) — cleaves alkenes to two carbonyls

**Reducing agents:**
- LiAlH₄ (LAH) — very strong; reduces aldehydes, ketones, esters, carboxylic acids, amides → alcohols (or amines for amides). Anhydrous conditions.
- NaBH₄ — milder; reduces aldehydes, ketones to alcohols. Does NOT reduce esters or carboxylic acids.
- H₂ / metal catalyst (Pd, Pt, Ni) — hydrogenation; reduces alkenes, alkynes, sometimes carbonyls.

### Why Tertiary Alcohols Resist Oxidation

Oxidation of an alcohol requires removing a hydrogen from the carbon bearing the -OH. Tertiary carbons have no such hydrogen — so they cannot be oxidized to carbonyls without breaking C-C bonds (which standard reagents won't do).

---

## 4. Chemoselectivity, Regioselectivity, Stereoselectivity

- **Chemoselectivity:** Which functional group reacts (when multiple are present)? Example: NaBH₄ reduces a ketone but leaves an ester alone.
- **Regioselectivity:** Where on the molecule does the reaction occur? Example: Markovnikov addition to alkenes places H on the C with more H's; H+ on the more substituted side.
- **Stereoselectivity:** Which stereoisomer forms preferentially? Example: SN2 gives inversion of configuration; E2 gives anti-periplanar elimination.
- **Stereospecificity:** Different stereoisomers of the starting material give different stereoisomers of the product (mechanistically required, not just preferred).

---

## 5. Six Problem-Solving Steps for Orgo Reactions

When facing an unfamiliar orgo problem, run through these steps:

1. **Identify the functional groups** present in starting material(s) and reagent(s).
2. **Classify the reagents:** nucleophile, electrophile, oxidizer, reducer, acid, base?
3. **Identify the most reactive site** on the substrate (electrophilic carbonyl C, leaving-group-bearing C, alpha-H, etc.).
4. **Predict the mechanism type** (substitution, elimination, addition, oxidation/reduction, condensation, etc.).
5. **Apply pKa or stability reasoning** to predict the product (most stable ion / lowest-energy intermediate).
6. **Check stereochem and regiochem** — does the mechanism dictate inversion/retention, or Markovnikov/anti-Markovnikov?

---

## 6. Quick-Fire Pattern Recognition

| Reagent type | First instinct |
|---|---|
| Strong base + acidic H | Deprotonation; check pKa |
| Strong nucleophile + alkyl halide | SN2 (or E2 if bulky/hindered) |
| Carbonyl + nucleophile | Nucleophilic addition (aldehyde/ketone) or acyl substitution (derivative) |
| Carbonyl + alpha-H + base | Enolate chemistry, possibly aldol |
| Alkene + electrophile (HX, X₂, H₂O w/ acid) | Electrophilic addition; Markovnikov |
| Alcohol + oxidizing agent | Oxidation level changes per alcohol type and reagent strength |
| Carbonyl + LiAlH₄ or NaBH₄ | Reduction to alcohol |
| Acid + alcohol + heat | Fischer esterification |
| Ester + base + water | Saponification (irreversible) |
| Amide + harsh acid/base + heat | Hydrolysis to carboxylic acid + amine |

---

## High-Yield Takeaways

1. **Memorize key pKa landmarks** (carboxylic acid ~4, phenol ~10, ammonium ~10, water 15.7, alcohol ~16-18, alpha-H ~20, terminal alkyne ~25, amine N-H ~36-38).
2. **Acid-base equilibrium favors weaker acid + weaker base** (the side with higher pKa).
3. **Nucleophile = Lewis base; electrophile = Lewis acid; leaving group leaves with the bond electrons.**
4. **Good LG = stable anion = low conjugate acid pKa.**
5. **Track oxidation level by counting C bonds to heteroatoms.** Going up = oxidation; going down = reduction.
6. **PCC stops at aldehyde; KMnO₄/CrO₃ goes all the way to carboxylic acid.**
7. **NaBH₄ ≠ LiAlH₄ in scope.** NaBH₄ is mild (carbonyls only); LAH is strong (everything down to alcohol/amine).
8. **Tertiary alcohols can't oxidize** (no H on the C-OH carbon).
9. **Six-step protocol** (above) is the unifying problem-solving algorithm.

---

→ Acid-base fundamentals: `CP_GC_Ch10_Acids_Bases.md`
→ Alcohol substitution & oxidation reactions: `CP_OC_Ch05_Alcohols.md`
→ Carbonyl nucleophilic addition: `CP_OC_Ch06_Aldehydes_Ketones_I.md`
→ Enolate / aldol chemistry: `CP_OC_Ch07_Aldehydes_Ketones_II_Enolates.md`
→ Carboxylic acid derivative reactivity ranking: `CP_OC_Ch09_Carboxylic_Acid_Derivatives.md`
