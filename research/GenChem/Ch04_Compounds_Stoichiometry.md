# CP Gen Chem Chapter 4 — Compounds & Stoichiometry

Scope: Molecular weight & moles; empirical vs molecular formulas; balancing equations; reaction classification (combination, decomposition, single/double displacement, combustion); limiting reagent; percent yield; oxidation numbers; equivalents & normality.

**Section:** Chemical/Physical (CP)
**Book:** Kaplan General Chemistry — Chapter 4
**AAMC FC mapping:** FC4E (stoichiometry portion)
**Yield:** HIGH — pattern recognition (reaction type) + moles-based stoichiometry is on every exam.

---

## 1. Molecular Weight and Mole Concept

- **Molecular weight (MW):** Sum of atomic masses of all atoms in a molecule. Units: g/mol (or amu per molecule).
- **Mole:** 6.022 x 10^23 particles (Avogadro's number). One mole of any element has a mass equal to its atomic mass in grams.
- **Molar mass** of C = 12 g/mol means 12 grams of carbon contains 6.022 x 10^23 carbon atoms.

**Conversions you should do instantly:**
- grams to moles: divide by molar mass
- moles to particles: multiply by 6.022 x 10^23
- moles to volume of gas at STP (0 degrees C, 1 atm): multiply by 22.4 L/mol

---

## 2. Empirical vs. Molecular Formulas

- **Empirical formula:** Simplest whole-number ratio of atoms. CH2O.
- **Molecular formula:** Actual number of atoms in one molecule. C6H12O6 (glucose).
- Molecular formula is always a whole-number multiple of the empirical formula.
- To find empirical formula from percent composition: assume 100 g sample, convert to moles, divide by the smallest mole value, round to nearest whole numbers.
- To get molecular formula: divide actual molar mass by empirical formula mass. Multiply subscripts by that integer.

---

## 3. Balancing Equations

Systematic approach:
1. Balance metals/unique elements first.
2. Balance nonmetals other than H and O.
3. Balance H.
4. Balance O last.
5. For combustion: balance C first, then H, then O.

Coefficients must be whole numbers. Check that atoms and charge balance on both sides.

---

## 4. Reaction Classification

The MCAT expects you to classify a given equation, decide whether it's a redox reaction, and then run stoichiometric calculations on it. Pattern recognition is the skill being tested.

### 4.1 Combination (Synthesis)

**Pattern:** A + B → AB

Two or more reactants fuse into a single product.

- 2 H₂ + O₂ → 2 H₂O
- N₂ + 3 H₂ → 2 NH₃ (Haber process)
- CaO + CO₂ → CaCO₃

Usually exothermic (new bonds form, releasing energy). May or may not be redox — check oxidation state changes case by case.

### 4.2 Decomposition

**Pattern:** AB → A + B

A single reactant splits into two or more products. Requires energy input — heat (Δ), light (hν), or electricity.

- 2 H₂O → 2 H₂ + O₂ (electrolysis)
- CaCO₃ → CaO + CO₂ (thermal decomposition; limestone → quicklime)
- 2 KClO₃ → 2 KCl + 3 O₂ (Δ, MnO₂ catalyst)
- 2 H₂O₂ → 2 H₂O + O₂ (catalyzed by catalase enzyme — biochem connection)

Decomposition is the formal reverse of combination. May or may not be redox.

### 4.3 Single Displacement (Single Replacement)

**Pattern:** A + BC → AC + B

A free element displaces another element from a compound.

- Zn + CuSO₄ → ZnSO₄ + Cu (Zn more reactive than Cu)
- 2 Na + 2 H₂O → 2 NaOH + H₂
- Cl₂ + 2 NaBr → 2 NaCl + Br₂ (halogen displacement)

**Always a redox reaction** — an element goes from oxidation state 0 to a non-zero state (or vice versa), so oxidation states MUST change.

**Activity series** determines whether the reaction will actually proceed. A more reactive metal displaces a less reactive one. High-yield order:

K > Na > Ca > Mg > Al > Zn > Fe > Pb > **H** > Cu > Ag > Au

Metals **above H** react with acids to release H₂ gas. Metals **below H** (Cu, Ag, Au) do NOT react with typical acids — this is why gold is "noble."

For halogens, reactivity decreases down the group: F₂ > Cl₂ > Br₂ > I₂.

### 4.4 Double Displacement (Metathesis)

**Pattern:** AB + CD → AD + CB

Ions swap partners. No oxidation states change — **usually NOT redox**. Two major subtypes:

**Precipitation reactions** — form an insoluble product:
- AgNO₃ + NaCl → AgCl↓ + NaNO₃
- Pb(NO₃)₂ + 2 KI → PbI₂↓ + 2 KNO₃

Common MCAT precipitates: AgCl, PbI₂, BaSO₄, CaCO₃.

**Neutralization reactions** — acid + base → salt + water:
- HCl + NaOH → NaCl + H₂O
- Net ionic: H⁺ + OH⁻ → H₂O (strong acid + strong base)

**Driving force:** double displacement proceeds only when something removes products from equilibrium — precipitate, gas, water, or weak electrolyte.

### 4.5 Combustion

**Pattern:** Hydrocarbon + O₂ → CO₂ + H₂O + heat

- CH₄ + 2 O₂ → CO₂ + 2 H₂O
- C₃H₈ + 5 O₂ → 3 CO₂ + 4 H₂O (propane)
- C₆H₁₂O₆ + 6 O₂ → 6 CO₂ + 6 H₂O (glucose — overall cellular respiration)

**Always exothermic, always redox.** Incomplete combustion gives CO or soot.

### 4.6 Cross-Cutting Categories

- **Redox:** any reaction with oxidation-state changes (overlaps combination, decomposition, single displacement, combustion)
- **Disproportionation:** one element both oxidized AND reduced. Example: 2 H₂O₂ → 2 H₂O + O₂.

### 4.7 Recognition Table

| Pattern | Type | Redox? |
|---|---|---|
| Multiple → one | Combination | Sometimes |
| One → multiple | Decomposition | Sometimes |
| Free element + compound → new free element + new compound | Single displacement | **Always** |
| Two compounds swap ions | Double displacement | Rarely |
| Fuel + O₂ → CO₂ + H₂O | Combustion | **Always** |
| Acid + base → salt + water | Neutralization (DD subtype) | No |

---

## 5. Limiting Reagent

This is the reagent that runs out first and determines how much product forms.

**Systematic approach:**
1. Convert all given masses to moles (divide by molar mass).
2. Divide each reactant's moles by its stoichiometric coefficient.
3. The smallest value identifies the **limiting reagent**.
4. Use the limiting reagent's moles to calculate moles of product (stoichiometric ratios).
5. Convert product moles to grams if needed.

**MCAT shortcut:** Always think in moles, never grams.

---

## 6. Yield Calculations

- **Theoretical yield:** Maximum product possible (from the limiting reagent calculation).
- **Actual yield:** What you actually get (given in the problem).
- **Percent yield:** (actual / theoretical) × 100%

Percent yield is always ≤ 100%.

---

## 7. Percent Composition

% of element = (n_atoms × atomic mass) / molar mass × 100%

Useful for going from a compound to its empirical formula.

---

## 8. Oxidation Numbers

Rules for assigning oxidation states (in priority order):

1. **Free elements** = 0 (O₂, Fe metal).
2. **Monoatomic ions** = charge (Na+ = +1, Cl⁻ = -1).
3. **Hydrogen** = +1 (except metal hydrides like NaH where H = -1).
4. **Oxygen** = -2 (except peroxides H₂O₂ where O = -1, and OF₂ where O = +2).
5. **Fluorine** = always -1.
6. Sum = 0 in neutral compound; sum = charge in polyatomic ion.

**Solving for unknown:** Assign all known values, solve.

Example: Mn in KMnO₄ → +1 + Mn + 4(-2) = 0 → Mn = +7.

**MCAT relevance:** Oxidation numbers identify redox reactions (oxidation = ↑ ON, reduction = ↓ ON).

---

## 9. Equivalents and Normality

Equivalents generalize moles to account for reactive capacity. An **equivalent** is the amount of a species that provides one mole of the reactive unit.

| Reaction type | Reactive unit |
|---|---|
| Acid-base | Moles of H⁺ donated/accepted |
| Redox | Moles of e⁻ transferred |
| Ionic / precipitation | Moles of charge per ion |

**n** = number of reactive units per molecule.

**Gram equivalent weight (GEW):**

GEW = molar mass / n

**Equivalents from mass:**

equivalents = mass(g) / GEW = moles × n

**Normality:**

N = M × n

(Equivalently M = N/n. Normality bakes n into the concentration so reactive capacity is comparable across species.)

**Equivalence-point relationship:**

N_acid · V_acid = N_base · V_base

Cleaner than molarity-based math for polyprotic acids (H₂SO₄, H₃PO₄) or multi-electron redox.

**Worked examples:**
- HCl (n=1, MW 36.5) → GEW = 36.5 g/eq. H₂SO₄ (n=2, MW 98) → GEW = 49 g/eq. So 36.5 g HCl ≡ 49 g H₂SO₄ in H⁺ delivery.
- Al → Al³⁺: n = 3, MW = 27 → GEW = 9 g/eq.
- CaCl₂: Ca²⁺ charge = 2, MW 111 → GEW = 55.5 g/eq.

**When normality wins:**
- Polyprotic acid/base titrations
- Redox titrations with multi-electron transfers
- Ionic capacity comparisons across salts of different charges

For monoprotic / single-electron / single-charge cases, N = M (no advantage).

---

## High-Yield Takeaways

1. **Always think in moles** — convert grams to moles before stoichiometry.
2. **Reaction classification:** single displacement and combustion are **always redox**; double displacement almost never.
3. **Limiting reagent:** divide moles by coefficient, take the smallest.
4. **Oxidation numbers:** assign quickly to recognize redox.
5. **Normality (N = M × n)** for polyprotic acids and multi-electron redox titrations.

---

→ Acids/bases & titrations → `CP_GC_Ch10_Acids_Bases.md`
→ Redox half-reactions & balancing → `CP_GC_Ch11_Redox.md`
→ Solutions & molarity → `CP_GC_Ch09_Solutions.md`
