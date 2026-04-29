# CP Orgo Chapter 9 — Carboxylic Acid Derivatives

Scope: Amides; esters; anhydrides; acyl halides; reactivity ranking; nucleophilic acyl substitution mechanism; common reactions (transesterification, hydrolysis, saponification, Fischer esterification, amide hydrolysis).

**Section:** Chemical/Physical (CP)
**Book:** Kaplan Organic Chemistry — Chapter 9
**AAMC FC mapping:** FC5D (acyl substitution chemistry)
**Yield:** HIGH — the reactivity ranking + saponification + Fischer esterification are recurring MCAT items.

---

## 1. Carboxylic Acid Derivatives — Overview

These are all compounds with a carbonyl bonded to a heteroatom-containing leaving group. They undergo **nucleophilic acyl substitution** (not just nucleophilic addition like aldehydes/ketones).

| Derivative | General Structure | Naming |
|---|---|---|
| Acyl halide | R-CO-X (X = Cl, Br) | -oyl halide (acetyl chloride) |
| Anhydride | R-CO-O-CO-R | -oic anhydride (acetic anhydride) |
| Ester | R-CO-O-R' | alkyl alkanoate (methyl acetate) |
| Amide | R-CO-NHR' or R-CO-NR'₂ | -amide (acetamide) |

Nitriles (R-C≡N) and carboxylic acids (R-COOH) are sometimes grouped here too.

---

## 2. Reactivity Ranking

**Acyl halide > Anhydride > Ester > Amide**

(Most reactive ──────────────────────────→ Least reactive)

**Why this order?** It comes down to **leaving group ability** and **resonance donation** by the heteroatom into the carbonyl.

- **Acyl halide (RCOX):** Halide (Cl⁻, Br⁻) is an excellent leaving group — very stable anion, weak base. Also, the halogen is electronegative and withdraws electron density from the carbonyl, making it more electrophilic. Halogen is a poor π-donor (lone pairs don't delocalize well into C=O).

- **Anhydride (RCO-O-COR):** Leaving group is a carboxylate (RCOO⁻), which is resonance-stabilized — good leaving group.

- **Ester (RCOOR'):** Leaving group is an alkoxide (RO⁻), a moderately strong base. Decent but not great LG. The alkoxy O donates lone pair into C=O somewhat (resonance), reducing electrophilicity.

- **Amide (RCONHR'):** Leaving group would be an amide ion (RNH⁻ or NH₂⁻), a strong base and terrible leaving group. Nitrogen also donates its lone pair STRONGLY into the carbonyl (better π-donor than O), giving the amide significant double-bond character at C-N (peptide bond planarity!) and making the carbonyl C least electrophilic.

**MCAT principle:** The better the leaving group AND the less resonance stabilization of the carbonyl by the heteroatom, the more reactive the derivative.

---

## 3. Nucleophilic Acyl Substitution Mechanism

1. **Nucleophile attacks** the carbonyl carbon (sp² → sp³, tetrahedral intermediate forms).
2. **Leaving group departs**, regenerating the C=O (sp³ → sp² again).
3. (Sometimes) deprotonation/protonation of the new substituent.

This differs from nucleophilic addition (aldehydes/ketones) because aldehydes/ketones have -H or -R as substituents, which are NOT leaving groups. Carboxylic acid derivatives have leaving groups that can depart, so the tetrahedral intermediate collapses back to a carbonyl.

### Going Down the Reactivity Ladder

**You can always go DOWN the reactivity ladder, but not up** (without special activation):
- Acyl halide → anhydride, ester, or amide ✓
- Anhydride → ester or amide ✓
- Ester → amide ✓
- Amide → harder (stable). Requires very harsh conditions (acid/base hydrolysis) to cleave.

This is because the leaving group of the higher-reactivity derivative is too good to be displaced by a weaker nucleophile.

### MCAT Application: Peptide Bond Formation

Peptide bond formation is technically making an amide from an amine and a carboxylic acid (or activated derivative). In ribosomal protein synthesis, the high energy of **aminoacyl-tRNA** (essentially an activated ester) drives amide bond formation efficiently. This is a biological example of "going from ester (high reactivity) → amide (low reactivity)."

---

## 4. Key Reactions of Carboxylic Acid Derivatives

### 4.1 Fischer Esterification

Carboxylic acid + Alcohol (H+ catalyst, heat) → **Ester** + Water

R-COOH + R'-OH ⇌ R-COOR' + H₂O

**Equilibrium reaction.** To drive forward, remove water (Le Chatelier) or use excess alcohol.

Mechanism (acid-catalyzed):
1. Protonate carbonyl O (activates C).
2. Alcohol O attacks C.
3. Proton transfers; -OH protonated.
4. Water leaves.
5. Deprotonate to give neutral ester.

Reverse process (acid-catalyzed hydrolysis): just run with excess water.

### 4.2 Saponification (Base Hydrolysis of Ester)

Ester + OH⁻ (NaOH or KOH) → Carboxylate + Alcohol

R-COOR' + NaOH → R-COO⁻Na⁺ + R'-OH

**Irreversible** because the carboxylate is resonance-stabilized and does NOT react with the alcohol under basic conditions (alkoxide and carboxylate are both bases; no driving force).

**Practical:** This is how **soap is made** from triglyceride (fat) + NaOH: yields glycerol + sodium fatty acid salts (the soap).

### 4.3 Acid-Catalyzed Hydrolysis of Ester

Ester + H₂O (H+) → Carboxylic acid + Alcohol (equilibrium — same as reverse of Fischer esterification).

### 4.4 Transesterification

One ester → another by reaction with a different alcohol (acid or base catalyst).

R-COOR' + R''-OH → R-COOR'' + R'-OH

Useful in biology: phosphatidic acid → phosphatidylcholine via transesterification.

### 4.5 Amide Hydrolysis

Amides require **harsh conditions** (strong acid or base, heat, often hours to days):

- **Acidic:** R-CONHR' + H₃O⁺ + heat → R-COOH + R'NH₃⁺
- **Basic:** R-CONHR' + OH⁻ + heat → R-COO⁻ + R'NH₂

Amide is the most stable derivative — peptide bonds in proteins persist under physiological conditions even though hydrolysis is thermodynamically favorable. **Kinetically stable** is the key concept. (Without proteases, peptide bond half-life ~hundreds of years at neutral pH.)

### 4.6 Reduction of Derivatives

| Derivative | LiAlH₄ Product | NaBH₄ Product |
|---|---|---|
| Acyl halide | 1° alcohol | (not standard — reactive) |
| Anhydride | 1° alcohols (×2) | (slowly) |
| Ester | 1° alcohol + alcohol from -OR | No reaction |
| Amide | **Amine** (special!) | No reaction |
| Carboxylic acid | 1° alcohol | No reaction |
| Nitrile | 1° amine | No reaction |

**Key special case:** LAH reduces amide to **amine** (not alcohol) — the C=O becomes CH₂ and the N stays attached. R-CO-NR'₂ → R-CH₂-NR'₂.

### 4.7 Reaction of Acyl Halides with Amines or Alcohols

Acyl chloride + amine → amide + HCl (need base to absorb HCl, often pyridine or excess amine)
Acyl chloride + alcohol → ester + HCl (similarly need base)

These are fast, irreversible, and the standard way to make esters/amides cleanly.

---

## 5. Special Behaviors

### Anhydrides as Acetylating Agents

Acetic anhydride (Ac₂O) is a workhorse acetylating reagent. Reacts with alcohols → acetate ester; with amines → acetamide. Drug example: aspirin synthesis (salicylic acid + Ac₂O → acetylsalicylic acid).

### Amides Are Not Basic

Despite having a nitrogen lone pair, **amides are NOT basic** — the lone pair is delocalized into the C=O, so it's not available to grab a proton. Amide N pKa (of conjugate acid) ~ -1 (very weak base).

This contrasts with simple amines (pKa of conjugate acid ~10), which ARE basic.

### Lactams = Cyclic Amides

5-membered (γ-lactam) and 6-membered (δ-lactam) rings are stable. **β-lactam** (4-membered) is strained — this is the reactive core of **penicillin antibiotics**, which bind transpeptidase irreversibly via β-lactam ring opening.

### Lactones = Cyclic Esters

Same idea but with ester. 5- and 6-membered lactones are very stable; β-lactones are strained.

---

## High-Yield Takeaways

1. **Reactivity ranking: acyl halide > anhydride > ester > amide.**
2. **Nucleophilic acyl substitution:** nuc attacks C, tetrahedral intermediate collapses, LG leaves.
3. **You can go DOWN the reactivity ladder, not up.**
4. **Fischer esterification:** reversible; remove water to drive forward.
5. **Saponification:** ester + OH⁻ → carboxylate + alcohol; **irreversible**; how soap is made.
6. **Amide hydrolysis** requires harsh conditions (peptide bonds are kinetically stable).
7. **LAH reduces amide to amine** (special); reduces other derivatives to alcohol.
8. **Amides are NOT basic** (lone pair conjugated into C=O).
9. **β-lactam** = strained 4-membered amide → penicillin reactivity.

---

→ Carboxylic acid chemistry: `CP_OC_Ch08_Carboxylic_Acids.md`
→ Mechanism framework (nucleophiles, leaving groups): `CP_OC_Ch04_Analyzing_Reactions.md`
→ Triglyceride saponification: `BB_Ch05_Lipids.md`
→ Peptide bonds: `BB_Ch01_AminoAcids_Proteins.md`
→ Reduction reagents (NaBH₄ vs LAH): `CP_OC_Ch05_Alcohols.md`
