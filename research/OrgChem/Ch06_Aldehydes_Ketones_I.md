# CP Orgo Chapter 6 — Aldehydes & Ketones I (Properties, Nucleophilic Addition, Redox)

Scope: Aldehyde and ketone properties; reactivity differences (steric & electronic); nucleophilic addition reactions (hemiacetal/acetal, imine/enamine, cyanohydrin, Grignard, NaBH₄/LiAlH₄); oxidation–reduction interconversions.

**Section:** Chemical/Physical (CP)
**Book:** Kaplan Organic Chemistry — Chapter 6
**AAMC FC mapping:** FC5D (carbonyl chemistry)
**Yield:** HIGH — nucleophilic addition is the gateway reaction class for orgo-biochem connections (sugar cyclization, transamination, Grignard synthesis).

> Note: Enolate chemistry, alpha-H acidity, and aldol reactions live in `CP_OC_Ch07_Aldehydes_Ketones_II_Enolates.md`.

---

## 1. Aldehyde and Ketone Properties

**Aldehyde:** R-CHO (carbonyl C with at least one H; terminal)
**Ketone:** R-CO-R' (carbonyl C with two R groups; internal)

The C=O is the most important functional group in organic chemistry. The carbon is **electrophilic** (δ+) due to the electronegativity of oxygen. Nucleophiles attack the carbonyl carbon.

**Properties:**
- Polar (C=O dipole) → moderate BP, partially water-soluble.
- No H-bond donor (no -OH or -NH), but strong H-bond acceptor (lone pairs on O).
- IR: sharp, strong C=O stretch at 1700-1750 cm⁻¹ (single most diagnostic peak).

### Why Aldehydes Are More Reactive Than Ketones

1. **Steric:** Ketones have two R groups flanking the carbonyl; aldehydes have only one R group and one H. Less steric hindrance = easier nucleophilic attack.
2. **Electronic:** Alkyl groups are electron-donating (inductive effect), partially stabilizing the partial positive charge on the carbonyl carbon. Ketones have two donating groups, making the carbon less electrophilic.

So: **aldehyde > ketone** in reactivity toward nucleophilic addition.

---

## 2. Nucleophilic Addition Mechanism

The general pattern:
1. Nucleophile attacks the carbonyl carbon.
2. The π bond breaks; electrons move onto oxygen.
3. Tetrahedral alkoxide intermediate forms.
4. Oxygen picks up a proton (or remains as alkoxide if anhydrous).

This differs from nucleophilic acyl substitution (in carboxylic acid derivatives) because aldehydes/ketones don't have a leaving group attached to the carbonyl C — so the tetrahedral intermediate stays put after protonation, instead of collapsing back to a carbonyl.

### Acid- vs Base-Catalyzed

- **Acid catalysis:** Protonates the carbonyl O first → makes C even more electrophilic → activates toward weak nucleophiles (water, alcohols).
- **Base catalysis:** Deprotonates the nucleophile first → makes nucleophile stronger.

---

## 3. Key Nucleophilic Addition Reactions

| Nucleophile | Product | Conditions |
|-------------|---------|------------|
| ROH (1 equiv) | **Hemiacetal/hemiketal** | Acid catalyst |
| ROH (2 equiv) | **Acetal/ketal** | Acid catalyst, remove water |
| RNH₂ (primary amine) | **Imine (Schiff base)** | Mild acid, remove water |
| R₂NH (secondary amine) | **Enamine** | Mild acid, remove water |
| HCN | **Cyanohydrin** | Base catalyst (CN⁻ is nucleophile) |
| RMgBr (Grignard) | **Alcohol** (after protonation) | Anhydrous conditions, then H₃O⁺ |
| NaBH₄ or LiAlH₄ | **Alcohol** (reduction) | NaBH₄ for mild, LiAlH₄ for strong |
| H₂O | **Hydrate (gem-diol)** | Equilibrium; usually unfavored except for formaldehyde, chloral |

### Acetal/Hemiacetal Formation (Big MCAT)

**Aldehyde + ROH (1 equiv, acid) → Hemiacetal** (R-CH(OH)(OR'))
**Hemiacetal + ROH (2nd equiv, acid, -H₂O) → Acetal** (R-CH(OR')₂)

Same for ketones: **hemiketal** then **ketal**.

**MCAT-critical:** Hemiacetal/hemiketal formation is exactly what happens during **sugar cyclization**. Glucose (aldehyde) forms an intramolecular hemiacetal — the C1 aldehyde attacks the C5 -OH of the same molecule. This generates the ring form (pyranose) and a new chiral center at C1 (the **anomeric carbon**, giving α/β anomers).

**Acetals as protecting groups:** Acetals are stable under basic and neutral conditions but cleave under acidic aqueous conditions. Chemists use acetals to protect carbonyls during reactions performed in base.

### Imine and Enamine Formation

- **Imine (Schiff base):** Primary amine attacks carbonyl, water leaves. Product has C=N. Reversible under aqueous acid conditions.
- **Enamine:** Secondary amine attacks carbonyl, water leaves. Product has C=C adjacent to nitrogen. Also reversible.

**MCAT connection:** Transamination reactions in amino acid metabolism use Schiff base (imine) intermediates with PLP (pyridoxal phosphate) as the coenzyme. This is where orgo meets metabolism (see BB_Ch11).

### Cyanohydrin

R-CHO + HCN (or CN⁻ + acidic workup) → R-CH(OH)(CN)

Useful synthetic intermediate — the nitrile can be hydrolyzed to a carboxylic acid (adds 1 carbon to the chain).

### Grignard Reagent Addition

R-MgX (made from alkyl halide + Mg in dry ether) is a strongly nucleophilic, basic carbanion equivalent.

R-MgX + R'-CHO → (after H₃O⁺) → secondary alcohol
R-MgX + R'-CO-R'' → (after H₃O⁺) → tertiary alcohol
R-MgX + HCHO (formaldehyde) → primary alcohol

**Key requirement:** anhydrous conditions! Water destroys Grignard (R-MgX + H₂O → R-H + MgX-OH).

Grignard also reacts with esters (twice, giving a tertiary alcohol with two identical R groups added) and with CO₂ (to give carboxylic acids after workup).

---

## 4. Oxidation–Reduction of Aldehydes and Ketones

### Reduction (Carbonyl → Alcohol)

(See `CP_OC_Ch05_Alcohols.md` for fuller redox treatment.)

- **NaBH₄:** Reduces aldehydes → 1° alcohols; ketones → 2° alcohols. Doesn't reduce esters, carboxylic acids.
- **LiAlH₄:** Reduces aldehydes, ketones (also esters, carboxylic acids, amides). Anhydrous.
- **H₂ / metal catalyst:** Hydrogenation. Reduces aldehydes/ketones (slower than alkenes).

### Oxidation

Aldehydes oxidize easily to carboxylic acids:
- **Tollens' reagent** (Ag(NH₃)₂⁺): mild; aldehyde → carboxylic acid. Positive test produces a **silver mirror** on the inside of the test tube — diagnostic of aldehydes (and reducing sugars, which have aldehyde forms in equilibrium).
- **KMnO₄, CrO₃, Jones reagent, K₂Cr₂O₇:** stronger; aldehyde → carboxylic acid.
- **Benedict's / Fehling's reagent** (Cu²⁺ complexes): mild; gives brick-red Cu₂O precipitate with aldehydes (and reducing sugars). Used to test for glucose in urine historically.

**Ketones do NOT oxidize easily.** No H on the carbonyl C, so further oxidation requires breaking C-C bonds (only happens with very harsh oxidizers, breaking into smaller carboxylic acids).

---

## 5. Carbonyl as the "Hub" of Orgo

The C=O group sits at the center of organic chemistry because:
1. **Polar bond** → predictable electrophilic site for nucleophiles.
2. **Reduction → alcohol; oxidation → carboxylic acid** (from aldehyde) — bridges oxidation states.
3. **Intramolecular reactions** create cyclic structures (sugars, lactones, lactams).
4. **Resonance/conjugation** (especially when α,β-unsaturated) extends the electrophilic system.
5. **Alpha hydrogens** are acidic (Ch07).

If you understand the C=O, you understand most of orgo.

---

## High-Yield Takeaways

1. **Aldehyde > ketone** in reactivity (steric + electronic).
2. **Carbonyl C is electrophilic** (δ+); nucleophile attacks here.
3. **Hemiacetal → acetal** with 2 equiv ROH + acid; this IS sugar cyclization.
4. **Acetals = protecting groups** (stable in base, cleave in acid).
5. **Imine** = primary amine + carbonyl (Schiff base; transamination/PLP).
6. **Grignard:** anhydrous; primary alcohol from formaldehyde, secondary from aldehyde, tertiary from ketone.
7. **Tollens' silver mirror, Benedict's red Cu₂O** = aldehyde tests (also positive for reducing sugars).
8. **Aldehydes oxidize easily; ketones don't.**

---

→ Enolate chemistry, alpha-H, aldol: `CP_OC_Ch07_Aldehydes_Ketones_II_Enolates.md`
→ Carboxylic acids: `CP_OC_Ch08_Carboxylic_Acids.md`
→ Sugar cyclization (hemiacetal → pyranose/furanose): `BB_Ch04_Carbohydrates.md`
→ Transamination/PLP: `BB_Ch11_Lipid_AA_Metab.md`
→ Spectroscopy (IR carbonyl): `CP_OC_Ch11_Spectroscopy.md`
