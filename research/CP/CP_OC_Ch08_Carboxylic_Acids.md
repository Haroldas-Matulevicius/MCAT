# CP Orgo Chapter 8 — Carboxylic Acids

Scope: Carboxylic acid description and properties; acidity (pKa, resonance, inductive effects); reactions of carboxylic acids — formation of acid derivatives, decarboxylation, reduction.

**Section:** Chemical/Physical (CP)
**Book:** Kaplan Organic Chemistry — Chapter 8
**AAMC FC mapping:** FC5D (carboxylic acid chemistry)
**Yield:** HIGH — carboxylic acid acidity reasoning, derivative formation, and decarboxylation are recurring MCAT themes.

---

## 1. Description and Properties

R-COOH:
- Composed of a carbonyl (C=O) AND a hydroxyl (-OH) on the same carbon (the carboxyl group).
- IUPAC suffix: **-oic acid** (e.g., methanoic acid = formic acid; ethanoic acid = acetic acid).
- Common biology: lactic acid, pyruvic acid, citric acid, fatty acids (long-chain RCOOH).

**Physical properties:**
- **High BP** (compared to alcohols of similar MW) due to dimer formation: two -COOH groups H-bond to each other in pairs.
- **Water-soluble** for short chains; solubility decreases as alkyl chain grows.
- **IR:** Very broad O-H absorption (2500-3300 cm⁻¹, swallowing C-H peaks) + sharp C=O at 1700-1725 cm⁻¹ — the broad O-H is diagnostic.

---

## 2. Acidity

Carboxylic acids are **moderately acidic**: pKa ~4-5 (acetic 4.76, formic 3.75, benzoic 4.20).

### Why So Acidic? (Compared to Alcohols)

- **Resonance stabilization of the conjugate base (carboxylate, RCOO⁻):**
  The negative charge is delocalized over **two equivalent oxygens** (two equivalent resonance structures).
- Alcohol's conjugate base (alkoxide, RO⁻) has the negative charge localized on one oxygen — much less stable.

This ~12 pKa unit difference (carboxylic ~4 vs alcohol ~16) is one of the most important comparisons in orgo, and it's purely a resonance argument.

### Substituent Effects (Inductive)

Electron-withdrawing groups (EWGs) **stabilize** the conjugate base (pull electron density away) → lower pKa = more acidic:

| Compound | pKa | Reason |
|---|---|---|
| Acetic acid (CH₃-COOH) | 4.76 | Baseline |
| Chloroacetic acid (ClCH₂-COOH) | 2.86 | Cl pulls e- inductively |
| Dichloroacetic acid (Cl₂CH-COOH) | 1.29 | 2 Cl |
| Trichloroacetic acid (Cl₃C-COOH) | 0.65 | 3 Cl |
| Trifluoroacetic acid (TFA, CF₃-COOH) | 0.23 | F more EN than Cl |
| Formic acid (HCOOH) | 3.75 | No alkyl donating group |

EDGs (alkyl) destabilize the carboxylate → higher pKa = less acidic.

**Distance matters:** EWGs on the α-carbon have a much bigger effect than on β or further. Inductive effects fall off rapidly with distance.

### MCAT Application: Strong Base Selection

To deprotonate a carboxylic acid (pKa ~4), even a mild base works:
- NaHCO₃ (conjugate of H₂CO₃, pKa 6.4): deprotonates carboxylic acid (forms CO₂ + H₂O bubbles!)
- NaOH (conjugate of H₂O, pKa 15.7): also deprotonates fully.

**Useful experimental test:** Carboxylic acids dissolve in 5% NaHCO₃ (with bubbling); phenols (pKa 10) do NOT dissolve in bicarb (need stronger base, like NaOH). This is the basis of acid-base extraction differentiation between carboxylic acids and phenols.

---

## 3. Reactions of Carboxylic Acids

### 3.1 Conversion to Acid Derivatives

You can convert a carboxylic acid into more reactive derivatives, which then can react with nucleophiles. (Detailed in `CP_OC_Ch09_Carboxylic_Acid_Derivatives.md`.)

**Acyl chlorides (R-COCl):**
- R-COOH + SOCl₂ → R-COCl + SO₂ + HCl
- R-COOH + PCl₃ or PCl₅ → R-COCl
- Acyl chlorides are highly reactive; standard intermediate for further synthesis.

**Esters (R-COOR'):**
- **Fischer esterification:** R-COOH + R'-OH (acid catalyst, heat, remove water) → R-COOR' + H₂O. Equilibrium reaction — drive forward by removing water (Le Chatelier).
- Better: convert acid to acyl chloride first, then react with alcohol (irreversible, fast).

**Amides (R-CONHR'):**
- Direct amide formation requires harsh conditions; usually go through acyl chloride or activated ester.
- Coupling reagents (DCC, EDC) are common in lab synthesis.

**Anhydrides (R-CO-O-CO-R):**
- 2 R-COOH → R-CO-O-CO-R + H₂O (need dehydration; usually thermal or chemical).

### 3.2 Decarboxylation

**β-keto acids and 1,3-dicarboxylic acids decarboxylate readily on heating:**

```
    O   O                          O
    ||  ||                         ||
R—C—CH₂—COOH    --heat-->   R—C—CH₃   +   CO₂
β-keto acid                    methyl ketone
```

The mechanism uses a cyclic transition state where the β-carbonyl oxygen accepts a proton from the carboxylic acid as CO₂ leaves. The intermediate is an enol that tautomerizes to the keto form.

**MCAT relevance:**
- **Acetoacetic acid (β-keto acid)** decarboxylates spontaneously near body temperature — it's a ketone body. Heat-sensitive.
- In **fatty acid synthesis**, malonyl-CoA decarboxylates to drive C-C bond formation (acetoacetic acid mechanism).
- In the **TCA cycle**, isocitrate dehydrogenase and α-ketoglutarate dehydrogenase both involve decarboxylation steps.

Simple monocarboxylic acids (R-COOH where R is just alkyl) are stable to decarboxylation.

### 3.3 Reduction

- **LiAlH₄ (LAH):** Reduces R-COOH all the way to R-CH₂OH (primary alcohol). Goes through aldehyde transient, but you can't stop there.
- **NaBH₄:** Does NOT reduce carboxylic acids (too weak).
- To stop at aldehyde, use **DIBAL-H (diisobutylaluminum hydride)** at low temperature on the ester or acyl chloride form (not standard MCAT).

### 3.4 Alpha-Substitution (Hell-Volhard-Zelinsky)

α-Halogenation: R-CH₂-COOH + Br₂ + PBr₃ → R-CHBr-COOH + HBr.

The α-H of a carboxylic acid is mildly acidic (~pKa 25 — the carboxylate isn't as activating as a ketone for enolization). This reaction goes through enol form.

Lower-yield on the MCAT but appears occasionally.

---

## 4. Special Cases

### Dicarboxylic Acids

Common ones (memorize for biology connections):
- Oxalic acid (HOOC-COOH): pKa1 = 1.27 (very acidic).
- Malonic acid (HOOC-CH₂-COOH): pKa1 = 2.83. Decarboxylates on heating.
- Succinic acid (HOOC-(CH₂)₂-COOH): TCA cycle intermediate.
- Glutaric acid (HOOC-(CH₂)₃-COOH): metabolic relevance.
- Adipic acid (HOOC-(CH₂)₄-COOH): nylon precursor.

The first ionization is much more acidic than the second (after one COO⁻ forms, the molecule is negative, making it harder to lose another proton).

### Beta- and Gamma-Hydroxy Acids

β-hydroxy and γ-hydroxy acids spontaneously cyclize to **lactones** (cyclic esters) on warming.
- 4-membered lactone (β-lactone): strained, less stable.
- 5-membered γ-butyrolactone: very stable.
- 6-membered δ-valerolactone: very stable.

**Biology:** β-lactam antibiotics (penicillin, cephalosporin) have a 4-membered cyclic amide (lactam) — strained, reactive, the source of their mechanism (acylating bacterial transpeptidase).

---

## High-Yield Takeaways

1. **Carboxylic acid pKa ~4-5;** much more acidic than alcohol (~16-18) due to **resonance stabilization** of carboxylate.
2. **Inductive EWGs** (Cl, F) lower pKa dramatically (TFA pKa 0.2).
3. **NaHCO₃ test:** carboxylic acids dissolve (with bubbling); phenols don't.
4. **Fischer esterification** is reversible; remove water to drive forward. Acyl chlorides give cleaner ester synthesis.
5. **β-keto acids decarboxylate** on heating — relevant for ketone bodies, TCA cycle, fatty acid synthesis.
6. **LAH reduces R-COOH → R-CH₂OH;** NaBH₄ does NOT.
7. **Acyl chloride** (via SOCl₂) is the standard way to "activate" carboxylic acid for derivative synthesis.

---

→ Acid-base extraction (separating carboxylic acids from phenols/amines): `CP_OC_Ch12_Separations_Purifications.md`
→ Carboxylic acid derivatives in detail: `CP_OC_Ch09_Carboxylic_Acid_Derivatives.md`
→ pKa fundamentals: `CP_GC_Ch10_Acids_Bases.md`
→ Fatty acid metabolism (decarboxylation in synthesis): `BB_Ch11_Lipid_AA_Metab.md`
→ TCA cycle decarboxylation steps: `BB_Ch10_CarbMetab2.md`
