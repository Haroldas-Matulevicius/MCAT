# FC4E: Atoms, Nuclear Decay, Electronic Structure

**Section:** Chem/Phys (CP)
**Subjects:** Physics, General Chemistry
**Yield:** HIGH -- This content underpins half of gen chem and connects to spectroscopy, bonding, and thermodynamics.

---

## 1. Atomic Structure

### The Basics

Every atom has three subatomic particles:

| Particle | Charge | Mass (amu) | Location |
|----------|--------|------------|----------|
| Proton | +1 | ~1 | Nucleus |
| Neutron | 0 | ~1 | Nucleus |
| Electron | -1 | ~1/1836 | Orbitals around nucleus |

- **Atomic number (Z):** Number of protons. This defines the element. Change Z, you change the element.
- **Mass number (A):** Protons + neutrons. Written as a superscript left of the element symbol.
- **Isotopes:** Same Z, different number of neutrons (different A). Carbon-12 and Carbon-14 are isotopes -- same element, same chemistry, different mass. Isotopes matter for nuclear decay and mass spec.
- **Ions:** Atoms that gained or lost electrons. Cations are positive (lost electrons), anions are negative (gained electrons). The nucleus does not change when forming ions.

**MCAT trap:** The mass of an atom is almost entirely in the nucleus. Electrons contribute essentially nothing to mass. When a problem gives you atomic mass, you are counting protons + neutrons.

### The Bohr Model

Bohr's model works perfectly for **hydrogen** (one-electron systems: H, He+, Li2+). It breaks down for multi-electron atoms, but the MCAT still tests the concepts heavily.

**Key ideas:**
- Electrons orbit the nucleus in fixed circular paths called **energy levels** (n = 1, 2, 3...).
- Each level has a defined energy. Electrons do NOT exist between levels.
- Lower n = closer to nucleus = more negative energy = more stable.
- **Ground state:** Electron in the lowest available energy level.
- **Excited state:** Electron has absorbed energy and jumped to a higher level.

**The hydrogen atom energy equation:**

$$E_n = -13.6 \text{ eV} / n^2$$

This is the single most important equation for atomic structure on the MCAT. What it tells you:

- n = 1 (ground state): E = -13.6 eV
- n = 2: E = -3.4 eV
- n = 3: E = -1.51 eV
- n = infinity: E = 0 eV (ionization -- electron free)

The energy becomes less negative (closer to zero) as n increases. The electron is less tightly bound.

**Energy of a transition:**

$$\Delta E = E_{final} - E_{initial} = -13.6 \left(\frac{1}{n_f^2} - \frac{1}{n_i^2}\right) \text{ eV}$$

- If the electron drops to a lower level: energy is **emitted** (delta E is negative, photon released).
- If the electron jumps to a higher level: energy is **absorbed** (delta E is positive, photon absorbed).
- The energy of the photon equals |delta E|, and E = hf = hc/lambda.

**Spectral series you should know:**

| Series | Transition to n = | Region |
|--------|-------------------|--------|
| Lyman | 1 | Ultraviolet |
| Balmer | 2 | Visible |
| Paschen | 3 | Infrared |

**MCAT strategy:** "Lyman = UV = Largest energy gaps (transitions to n=1)." The bigger the jump, the higher the energy (shorter wavelength). A transition from n=3 to n=1 releases more energy than n=3 to n=2.

### Emission vs. Absorption Spectra

- **Emission spectrum:** Bright colored lines on a dark background. Excited atoms release photons at specific wavelengths as electrons fall to lower levels.
- **Absorption spectrum:** Dark lines on a continuous colored background. Atoms absorb specific wavelengths from white light, exciting electrons upward.

Both spectra show the SAME line positions for a given element -- they are complementary. The absorption lines match the emission lines exactly.

### Quantum Mechanical Model

Bohr's model says electrons travel in neat orbits. The quantum mechanical model says: no. Electrons exist in **probability distributions** called orbitals. You cannot know the exact position and momentum simultaneously (**Heisenberg uncertainty principle**).

- An orbital is a region of space where there is a high probability (~90%) of finding an electron.
- The shape and energy of an orbital are described by quantum numbers (next section).
- This model is more accurate than Bohr but the MCAT often uses Bohr-level reasoning for hydrogen atom problems.

---

## 2. Quantum Numbers

Every electron in an atom is described by exactly four quantum numbers. No two electrons can share all four (Pauli exclusion principle).

### Principal Quantum Number (n)

- **Values:** 1, 2, 3, 4...
- **Meaning:** Energy level (shell). Higher n = higher energy = farther from nucleus.
- **Max electrons in shell n:** 2n^2 (so n=1 holds 2, n=2 holds 8, n=3 holds 18).

### Angular Momentum Quantum Number (l)

- **Values:** 0 to (n - 1)
- **Meaning:** Subshell shape. Determines orbital shape.

| l value | Subshell letter | Shape | Max electrons |
|---------|----------------|-------|---------------|
| 0 | s | Spherical | 2 |
| 1 | p | Dumbbell (two lobes) | 6 |
| 2 | d | Cloverleaf (four lobes, mostly) | 10 |
| 3 | f | Complex (seven orbitals) | 14 |

**MCAT connection:** When n = 1, l can only be 0, so the first shell only has an s subshell. When n = 2, l = 0 or 1, so you get 2s and 2p. When n = 3, l = 0, 1, or 2, giving 3s, 3p, 3d.

### Magnetic Quantum Number (m_l)

- **Values:** -l to +l (including 0)
- **Meaning:** Orientation of the orbital in space.
- For l = 0 (s): m_l = 0 only -- one orientation (1 orbital).
- For l = 1 (p): m_l = -1, 0, +1 -- three orientations (3 orbitals: px, py, pz).
- For l = 2 (d): m_l = -2, -1, 0, +1, +2 -- five orientations (5 orbitals).

### Spin Quantum Number (m_s)

- **Values:** +1/2 or -1/2
- **Meaning:** Intrinsic spin of the electron. Each orbital holds at most 2 electrons with opposite spins.

**Quick way to count:** Number of orbitals in a subshell = 2l + 1. Number of electrons = 2(2l + 1).

**MCAT-style question pattern:** "Which set of quantum numbers is NOT possible?" Check: is l < n? Is m_l between -l and +l? These are the typical traps. Example: (n=2, l=2, m_l=0, m_s=+1/2) is impossible because l must be less than n.

---

## 3. Electron Configuration

### The Three Rules

**1. Aufbau Principle:** Fill orbitals from lowest energy to highest. The filling order is:

1s, 2s, 2p, 3s, 3p, **4s, 3d**, 4p, 5s, 4d, 5p, 6s, 4f, 5d, 6p...

Notice that 4s fills before 3d. Use the diagonal rule (draw the orbitals in rows and follow diagonal arrows from top-right to bottom-left) if you need to reconstruct the order.

**2. Hund's Rule:** Within a subshell, electrons fill each orbital singly (with parallel spins) before any orbital gets a second electron. Think of it like people on a bus -- everyone takes their own seat before doubling up.

Why? Electrons with parallel spins in separate orbitals minimize electron-electron repulsion. This is a lower energy arrangement.

**3. Pauli Exclusion Principle:** No two electrons in the same atom can have the same four quantum numbers. Practically, this means each orbital can hold at most 2 electrons, and they must have opposite spins.

### Writing Configurations

**Full configuration example -- Iron (Fe, Z = 26):**

1s^2 2s^2 2p^6 3s^2 3p^6 4s^2 3d^6

**Noble gas shorthand:** Find the nearest noble gas with fewer electrons and use its symbol in brackets.

[Ar] 4s^2 3d^6

**Orbital diagram for Fe:**
- 4s: [up-down]
- 3d: [up-down] [up] [up] [up] [up]

Wait -- Hund's rule says fill singly first. With 6 electrons in 5 d-orbitals, one orbital gets paired and four remain unpaired. Iron has **4 unpaired electrons**. This is why iron is paramagnetic.

### The Exceptions You Must Know

**Chromium (Cr, Z = 24):** Expected: [Ar] 4s^2 3d^4. Actual: **[Ar] 4s^1 3d^5**.

**Copper (Cu, Z = 29):** Expected: [Ar] 4s^2 3d^9. Actual: **[Ar] 4s^1 3d^10**.

Why? A half-filled d subshell (d^5) and a fully filled d subshell (d^10) have extra stability due to symmetric electron distribution and exchange energy. The atom "steals" one electron from 4s to achieve this.

**MCAT tip:** You will almost certainly not need to know other exceptions. Cr and Cu are the classic two. The reasoning (half-filled and fully filled stability) is more important than memorizing a list.

### Electron Configuration of Ions

This is where students get tricked. When transition metals lose electrons to form cations, **electrons are removed from the highest n first (4s before 3d), NOT in the reverse order of filling.**

- Fe: [Ar] 4s^2 3d^6
- Fe^2+: [Ar] 3d^6 (lost the two 4s electrons)
- Fe^3+: [Ar] 3d^5 (lost both 4s electrons, then one 3d)

Why? In the neutral atom, 4s fills first because it has slightly lower energy. But once the d orbitals are occupied, electron-electron repulsion shifts the energy ordering, and 4s becomes higher in energy than 3d. So 4s electrons leave first.

### Valence Electrons

- **Main group elements:** Valence electrons are in the highest n shell. Sodium (Na): [Ne] 3s^1 has 1 valence electron. Oxygen: [He] 2s^2 2p^4 has 6 valence electrons.
- **Transition metals:** Both ns and (n-1)d electrons can participate in bonding. The number of valence electrons is less fixed, which is why transition metals show multiple oxidation states.
- Valence electrons determine chemical reactivity, bonding behavior, and position on the periodic table.

---

## 4. Periodic Trends

Every major periodic trend can be explained by two competing factors: **effective nuclear charge (Z_eff)** and **distance from the nucleus / shielding**.

### Effective Nuclear Charge (Z_eff)

$$Z_{eff} = Z - S$$

Where Z is the actual nuclear charge (number of protons) and S is the shielding constant (approximated as the number of inner-shell electrons).

- **Across a period (left to right):** Z increases by 1 with each element, but the new electron goes into the SAME shell (same shielding). So Z_eff increases. Outer electrons are pulled in tighter.
- **Down a group:** A new shell is added. The inner electrons shield the outer electron from the nucleus. Z_eff felt by the outer electron does not increase as dramatically, and the electron is much farther from the nucleus.

This is the master concept. Every trend below follows from it.

### Atomic Radius

**Trend:** Decreases left to right across a period. Increases top to bottom down a group.

**Why across:** Higher Z_eff pulls electrons closer. More protons in the nucleus, same shielding, so the electron cloud contracts.

**Why down:** New principal energy level = new shell = electrons are farther from the nucleus. Shielding from inner shells also increases.

**Ionic radius:**
- **Cations are smaller** than their parent atoms (lost electrons, less repulsion, same nuclear charge pulls remaining electrons tighter).
- **Anions are larger** than their parent atoms (added electrons, more repulsion, same nuclear charge can't hold the cloud as tightly).
- **Isoelectronic series:** Ions with the same number of electrons. The one with MORE protons is smaller because higher Z_eff compresses the electron cloud. Example: O^2-, F^-, Na+, Mg^2+ all have 10 electrons. Order from largest to smallest: O^2- > F^- > Na+ > Mg^2+.

### Ionization Energy (IE)

**Definition:** Energy required to remove the outermost electron from a gaseous atom.

**Trend:** Increases left to right, increases bottom to top. (Same direction as electronegativity.)

**Why:** Higher Z_eff = electrons held tighter = harder to remove. Also, closer to the nucleus = stronger attraction = harder to remove. Noble gases have the highest IE in each period.

**Successive ionization energies:** Each successive electron is harder to remove (IE1 < IE2 < IE3...). There is a HUGE jump when you break into a new (inner) shell. For Na, IE1 is modest, but IE2 is enormous because you are pulling from the stable [Ne] core. This jump tells you the number of valence electrons.

**Exceptions within a period (high-yield):**
- **Group 2 to Group 13 dip:** Be (2s^2) has higher IE than B (2s^2 2p^1). Removing a p electron is easier than removing an s electron from a filled subshell.
- **Group 15 to Group 16 dip:** N (2p^3, half-filled) has higher IE than O (2p^4). Oxygen's fourth p electron is paired, creating repulsion that makes it easier to remove.

### Electron Affinity (EA)

**Definition:** Energy change when a gaseous atom gains an electron. More negative EA = more energy released = atom "wants" that electron more.

**Trend:** Generally becomes more negative (more favorable) going left to right and bottom to top, but it is less smooth than IE. Halogens have the most negative EA (they desperately want one more electron to complete their octet).

**Watch out:** Noble gases have near-zero or positive EA because their shells are already full. Group 2 and Group 15 elements also have less favorable EA due to filled/half-filled subshell stability.

### Electronegativity (EN)

**Definition:** Tendency of an atom to attract electrons in a chemical bond (Pauling scale).

**Trend:** Increases left to right, increases bottom to top. Fluorine is the most electronegative element (4.0). Francium is the least.

**Why:** Same Z_eff argument. Atoms with high Z_eff and small radius attract bonding electrons more strongly.

**MCAT application:** Electronegativity differences determine bond polarity. Large difference = ionic. Small difference = polar covalent. Zero difference = nonpolar covalent.

### Metallic Character

**Trend:** Opposite of electronegativity. Increases down and to the left.

Metals lose electrons easily (low IE, low EN). Nonmetals gain electrons (high IE, high EN, high EA).

### Summary Table

| Trend | Across period (L to R) | Down group | Unifying reason |
|-------|----------------------|------------|-----------------|
| Atomic radius | Decreases | Increases | Z_eff vs. shell number |
| Ionization energy | Increases | Decreases | Z_eff / proximity |
| Electron affinity | More negative | Less negative | Z_eff / proximity |
| Electronegativity | Increases | Decreases | Z_eff / proximity |
| Metallic character | Decreases | Increases | Opposite of EN |

---

## 5. Nuclear Chemistry

### Radioactive Decay Types

This is a pattern-recognition topic. Know the particle emitted, the change in A and Z, and the relative penetrating power.

| Decay type | Particle emitted | Change in A | Change in Z | Symbol |
|------------|-----------------|-------------|-------------|--------|
| Alpha | ^4_2 He (helium nucleus) | -4 | -2 | alpha |
| Beta-minus | ^0_{-1} e (electron) | 0 | +1 | beta^- |
| Beta-plus (positron) | ^0_{+1} e (positron) | 0 | -1 | beta^+ |
| Gamma | Photon (EM radiation) | 0 | 0 | gamma |
| Electron capture | Inner electron captured by nucleus | 0 | -1 | EC |

#### Alpha Decay
- The nucleus ejects a helium-4 nucleus (2 protons + 2 neutrons).
- A decreases by 4, Z decreases by 2. The element changes (moves 2 left on the periodic table).
- **Penetration:** Very low. Stopped by a sheet of paper or skin.
- **Ionization:** Very high (large, slow, charged particle interacts with everything it hits).
- Heavy, unstable nuclei (A > 200) tend to undergo alpha decay.

#### Beta-Minus Decay
- A neutron converts into a proton, releasing an electron (beta particle) and an antineutrino.
- A stays the same (a nucleon is still a nucleon), Z increases by 1.
- Occurs in nuclei with too many neutrons (neutron-rich).
- **Penetration:** Moderate. Stopped by aluminum foil or thick clothing.
- **Ionization:** Moderate.

#### Beta-Plus (Positron Emission)
- A proton converts into a neutron, releasing a positron (anti-electron) and a neutrino.
- A stays the same, Z decreases by 1.
- Occurs in nuclei with too many protons (proton-rich).
- The positron quickly encounters an electron and they **annihilate**, producing two gamma rays traveling in opposite directions (180 degrees apart). This is the basis of **PET scans**.

#### Electron Capture
- The nucleus captures an inner-shell (usually K-shell) electron.
- A proton combines with the electron to become a neutron.
- Same result as positron emission: A stays the same, Z decreases by 1.
- Competes with positron emission in proton-rich nuclei, especially in heavier atoms.
- Produces characteristic X-rays as outer electrons fill the vacated inner shell.

#### Gamma Decay
- Nucleus drops from an excited state to a lower energy state, releasing a high-energy photon.
- No change in A or Z. Often accompanies other decay types.
- **Penetration:** Very high. Requires lead or thick concrete to stop.
- **Ionization:** Low (no charge, no mass -- passes through without interacting as much).

**MCAT mnemonic for penetration:** Alpha < Beta < Gamma. For ionization, the reverse: Alpha > Beta > Gamma. Think of it as a tradeoff -- the more a particle interacts with matter (ionizes), the sooner it stops (less penetration).

### Half-Life

**Definition:** The time it takes for half of a radioactive sample to decay.

**Key equation:**

$$N = N_0 \left(\frac{1}{2}\right)^{t/t_{1/2}}$$

Where:
- N = amount remaining
- N_0 = initial amount
- t = elapsed time
- t_{1/2} = half-life

**Estimation strategies (no calculator):**

The MCAT gives you numbers that work out cleanly. Here is how to handle them:

**Method 1 -- Count half-lives:**
If the elapsed time is a whole number of half-lives, just halve repeatedly.

Example: 80 g sample, half-life = 5 years, how much remains after 20 years?
- 20 / 5 = 4 half-lives
- 80 -> 40 -> 20 -> 10 -> 5 g

**Method 2 -- For non-integer half-lives, use the fraction:**

After 1.5 half-lives, the fraction remaining = (1/2)^1.5 = (1/2)(1/2)^0.5 = (1/2)(1/sqrt(2)) = about (0.5)(0.707) = 0.354. So roughly 35% remains.

Key values to memorize:
- (1/2)^0.5 = about 0.71 (or 1/sqrt(2))
- (1/2)^1 = 0.50
- (1/2)^2 = 0.25
- (1/2)^3 = 0.125
- (1/2)^4 = 0.0625

**Method 3 -- Work from the fraction remaining:**

If a problem says "12.5% of the sample remains," recognize that 0.125 = (1/2)^3, so 3 half-lives have passed.

**Activity (decay rate):** A = lambda * N, where lambda = ln(2)/t_{1/2} = 0.693/t_{1/2}. Activity also decreases by half with each half-life. If they give you initial activity, you can use the same halving approach.

### Mass Defect and Binding Energy

The mass of a nucleus is LESS than the sum of the masses of its individual protons and neutrons. The "missing" mass is called the **mass defect** (delta m).

$$\Delta m = (Z \cdot m_p + N \cdot m_n) - m_{nucleus}$$

This mass was converted to energy when the nucleus formed, and it equals the **nuclear binding energy:**

$$E = \Delta m \cdot c^2$$

This is the energy you would need to input to completely disassemble the nucleus into individual protons and neutrons.

**Binding energy per nucleon** is the key metric for nuclear stability. Plot it against mass number and you get the famous curve:

- Iron-56 (and nickel-62) sit at the peak -- most stable nuclei, highest binding energy per nucleon.
- Lighter elements can increase stability by **fusing** (fusion -- combining small nuclei).
- Heavier elements can increase stability by **splitting** (fission -- breaking apart large nuclei).
- Both fusion and fission release energy because the products have higher binding energy per nucleon than the reactants.

**MCAT connection:** Fusion releases more energy per nucleon than fission. The sun runs on fusion (hydrogen -> helium). Nuclear reactors use fission (uranium-235).

### Medical Applications

- **PET scan (Positron Emission Tomography):** Patient is injected with a positron-emitting isotope (commonly F-18 FDG, a glucose analog). Positrons annihilate with electrons, producing two 511 keV gamma rays at 180 degrees. Detectors pick up both rays simultaneously to localize the source. Used for metabolically active tissue (cancer, brain).
- **Radiation therapy:** Uses high-energy radiation (gamma rays, X-rays, proton beams) to damage DNA in cancer cells. Alpha emitters can also be targeted to tumors.
- **Radioactive tracers:** Use the chemical properties of the radioisotope to track metabolic pathways (e.g., iodine-131 for thyroid).

---

## 6. Stoichiometry (Kaplan Gen Chem Ch 4)

**Chapter pairing:** Stoichiometry and reaction types are both taught in Kaplan Gen Chem Ch 4. Always teach them together — the MCAT routinely gives you a reaction, asks you to classify it, balance it, and then run a stoichiometry calculation on it in the same item set.

### Molecular Weight and Mole Concept

- **Molecular weight (MW):** Sum of atomic masses of all atoms in a molecule. Units: g/mol (or amu per molecule).
- **Mole:** 6.022 x 10^23 particles (Avogadro's number). One mole of any element has a mass equal to its atomic mass in grams.
- **Molar mass** of C = 12 g/mol means 12 grams of carbon contains 6.022 x 10^23 carbon atoms.

**Conversions you should do instantly:**
- grams to moles: divide by molar mass
- moles to particles: multiply by 6.022 x 10^23
- moles to volume of gas at STP (0 degrees C, 1 atm): multiply by 22.4 L/mol

### Empirical vs. Molecular Formulas

- **Empirical formula:** Simplest whole-number ratio of atoms. CH2O.
- **Molecular formula:** Actual number of atoms in one molecule. C6H12O6 (glucose).
- Molecular formula is always a whole-number multiple of the empirical formula.
- To find empirical formula from percent composition: assume 100 g sample, convert to moles, divide by the smallest mole value, round to nearest whole numbers.
- To get molecular formula: divide actual molar mass by empirical formula mass. Multiply subscripts by that integer.

### Balancing Equations

Systematic approach:
1. Balance metals/unique elements first.
2. Balance nonmetals other than H and O.
3. Balance H.
4. Balance O last.
5. For combustion: balance C first, then H, then O.

Coefficients must be whole numbers. Check that atoms and charge balance on both sides.

### Limiting Reagent

This is the reagent that runs out first and determines how much product forms.

**Systematic approach:**
1. Convert all given masses to moles (divide by molar mass).
2. Divide each reactant's moles by its stoichiometric coefficient.
3. The smallest value identifies the **limiting reagent**.
4. Use the limiting reagent's moles to calculate moles of product (stoichiometric ratios).
5. Convert product moles to grams if needed.

**MCAT shortcut:** If the problem gives you equal moles of two reactants and the equation requires a 1:2 ratio, the one with the higher coefficient requirement is limiting. Always think in moles, never grams.

### Yield Calculations

- **Theoretical yield:** Maximum product possible (from the limiting reagent calculation, assuming 100% conversion).
- **Actual yield:** What you actually get in the lab (given in the problem).
- **Percent yield:**

$$\% \text{ yield} = \frac{\text{actual yield}}{\text{theoretical yield}} \times 100\%$$

Percent yield is always less than or equal to 100% in practice.

### Percent Composition

$$\% \text{ of element} = \frac{(\text{number of atoms of element}) \times (\text{atomic mass of element})}{\text{molar mass of compound}} \times 100\%$$

Useful for going from a compound to its empirical formula or vice versa.

### Oxidation Numbers

Rules for assigning oxidation states (in priority order):

1. **Free elements** have oxidation number 0 (e.g., O2, Fe metal).
2. **Monoatomic ions** have oxidation number equal to their charge (Na+ = +1, Cl^- = -1).
3. **Hydrogen** is +1 in most compounds. Exception: metal hydrides (NaH), where H is -1.
4. **Oxygen** is -2 in most compounds. Exceptions: peroxides (H2O2) where O is -1, and OF2 where O is +2.
5. **Fluorine** is always -1 (most electronegative element, period).
6. The sum of oxidation numbers in a neutral compound = 0. In a polyatomic ion, the sum = the ion's charge.

**How to find an unknown oxidation state:** Assign all known values, then solve for the unknown using the sum rule.

Example: What is the oxidation state of Mn in KMnO4?
- K = +1, O = -2 (four oxygens = -8), total = 0
- +1 + Mn + (-8) = 0, so Mn = +7

**MCAT relevance:** Oxidation numbers are essential for identifying redox reactions (oxidation = increase in oxidation number, reduction = decrease). You need them for balancing redox equations, electrochemistry, and understanding metabolism (NAD+ being reduced to NADH involves a change in oxidation state of carbon atoms in substrates).

### Equivalents and Normality

Equivalents generalize moles to account for reactive capacity. An **equivalent** is the amount of a species that provides one mole of the reactive unit, where the reactive unit depends on the reaction type:

| Reaction type | Reactive unit (what n counts) |
|---------------|-------------------------------|
| Acid-base | Moles of H⁺ donated or accepted |
| Redox | Moles of electrons transferred |
| Ionic / precipitation | Moles of charge per ion |

**n** = number of reactive units per molecule.

**Gram equivalent weight (GEW):**

$$GEW = \frac{\text{molar mass}}{n}$$

This is the mass (in grams) of the compound that provides exactly one equivalent.

**Equivalents from mass:**

$$\text{equivalents} = \frac{\text{mass (g)}}{GEW} = \text{moles} \times n$$

**Normality:**

$$N = M \times n$$

Equivalently, M = N / n. Normality is "equivalents per liter" — it bakes n into the concentration so you can compare reactive capacity directly across species with different stoichiometries.

**Equivalence-point relationship (titrations):**

$$N_{acid} \cdot V_{acid} = N_{base} \cdot V_{base}$$

Much cleaner than molarity-based math for polyprotic acids (H₂SO₄, H₃PO₄) or multi-electron redox reactions — you avoid stopping to multiply by n mid-calculation.

**Worked examples:**

- **HCl vs H₂SO₄ acid capacity:** HCl has n = 1, molar mass 36.5 g/mol → GEW = 36.5 g/eq. H₂SO₄ has n = 2, molar mass 98 g/mol → GEW = 49 g/eq. So 36.5 g HCl and 49 g H₂SO₄ both deliver 1 mole of H⁺ — equivalent reactive capacity despite different masses.
- **Redox (Al → Al³⁺):** n = 3, molar mass = 27 g/mol → GEW = 9 g/eq. Just 9 g of Al provides 1 mole of electrons.
- **Ionic (CaCl₂):** Ca²⁺ charge = 2 → n = 2, molar mass 111 g/mol → GEW = 55.5 g/eq.

**When to reach for normality instead of molarity:**
- Polyprotic acid/base titrations
- Redox titrations with multi-electron transfers
- Comparing ionic capacity across salts with different charges

For monoprotic / single-electron / single-charge cases, n = 1 and normality collapses back to molarity — no advantage.

---

## 7. Reaction Classification (Kaplan Gen Chem Ch 4)

Chapter 4 covers reaction classification alongside stoichiometry — the MCAT expects you to classify a given equation, decide whether it's a redox reaction, and then run stoichiometric calculations on it. Pattern recognition is the skill being tested.

### 7.1 Combination (Synthesis)

**Pattern:** A + B → AB

Two or more reactants fuse into a single product.

- 2 H₂ + O₂ → 2 H₂O
- N₂ + 3 H₂ → 2 NH₃ (Haber process)
- CaO + CO₂ → CaCO₃

Usually exothermic (new bonds form, releasing energy). May or may not be redox — check oxidation state changes case by case. The two hydrogen and oxygen examples above are redox; CaO + CO₂ is not.

### 7.2 Decomposition

**Pattern:** AB → A + B

A single reactant splits into two or more products. Requires energy input — heat (Δ), light (hν), or electricity.

- 2 H₂O → 2 H₂ + O₂ (electrolysis)
- CaCO₃ → CaO + CO₂ (thermal decomposition; limestone → quicklime, industrially important)
- 2 KClO₃ → 2 KCl + 3 O₂ (Δ, MnO₂ catalyst)
- 2 H₂O₂ → 2 H₂O + O₂ (catalyzed by catalase enzyme — biochem connection)

Decomposition is the formal reverse of combination. May or may not be redox.

### 7.3 Single Displacement (Single Replacement)

**Pattern:** A + BC → AC + B

A free element displaces another element from a compound.

- Zn + CuSO₄ → ZnSO₄ + Cu (Zn more reactive than Cu)
- 2 Na + 2 H₂O → 2 NaOH + H₂
- Cl₂ + 2 NaBr → 2 NaCl + Br₂ (halogen displacement)

**Always a redox reaction** — an element goes from oxidation state 0 to a non-zero state (or vice versa), so oxidation states MUST change.

**Activity series** determines whether the reaction will actually proceed. A more reactive metal displaces a less reactive one. High-yield order (memorize at least the top half):

K > Na > Ca > Mg > Al > Zn > Fe > Pb > **H** > Cu > Ag > Au

Metals **above H** react with acids to release H₂ gas. Metals **below H** (Cu, Ag, Au) do NOT react with typical acids — this is why gold is "noble."

For halogens, reactivity decreases down the group: F₂ > Cl₂ > Br₂ > I₂. A more reactive halogen displaces a less reactive one from its salt.

### 7.4 Double Displacement (Metathesis)

**Pattern:** AB + CD → AD + CB

Ions swap partners. No oxidation states change — **usually NOT redox**. Two major subtypes:

**Precipitation reactions** — form an insoluble product that drops out of solution:
- AgNO₃ + NaCl → AgCl↓ + NaNO₃
- Pb(NO₃)₂ + 2 KI → PbI₂↓ + 2 KNO₃
- Use solubility rules to predict which pairing is insoluble. AgCl, PbI₂, BaSO₄, CaCO₃ are common MCAT precipitates.

**Neutralization reactions** — acid + base → salt + water:
- HCl + NaOH → NaCl + H₂O
- H₂SO₄ + 2 KOH → K₂SO₄ + 2 H₂O
- Net ionic equation: H⁺ + OH⁻ → H₂O (for strong acid + strong base).

**Driving force** is key: double displacement proceeds only when something removes products from equilibrium — formation of a precipitate, a gas, water, or a weak electrolyte.

### 7.5 Combustion

**Pattern:** Hydrocarbon (or organic fuel) + O₂ → CO₂ + H₂O + heat

- CH₄ + 2 O₂ → CO₂ + 2 H₂O (methane)
- C₃H₈ + 5 O₂ → 3 CO₂ + 4 H₂O (propane)
- C₆H₁₂O₆ + 6 O₂ → 6 CO₂ + 6 H₂O (glucose — also the overall equation for cellular respiration)

**Always exothermic, always redox** — carbon and hydrogen are oxidized; oxygen is reduced.

**Incomplete combustion** (insufficient O₂) yields CO (toxic carbon monoxide) or soot (elemental C). Common MCAT trap — don't assume every combustion produces clean CO₂.

### 7.6 Cross-Cutting Classifications

Some reactions fit multiple categories. The MCAT cares more about the chemistry than the label:

- **Redox reactions:** Any reaction with oxidation state changes. Overlaps with combination, decomposition, single displacement, and combustion.
- **Acid-base reactions:** Proton transfer. Overlaps with neutralization (a subtype of double displacement).
- **Precipitation:** Subtype of double displacement.
- **Disproportionation:** A single element is both oxidized AND reduced in the same reaction. Example: 2 H₂O₂ → 2 H₂O + O₂ (oxygen goes from −1 to −2 AND from −1 to 0). Also: 3 ClO⁻ → 2 Cl⁻ + ClO₃⁻.

### 7.7 Recognition Table — MCAT Workflow

| Observed pattern | Classification | Redox? |
|------------------|---------------|--------|
| Multiple reactants → one product | Combination | Sometimes |
| One reactant → multiple products | Decomposition | Sometimes |
| Free element + compound → new free element + new compound | Single displacement | **Always** |
| Two compounds swap ions | Double displacement | Rarely |
| Fuel + O₂ → CO₂ + H₂O | Combustion | **Always** |
| Acid + base → salt + water | Neutralization (subtype of DD) | No |

**Workflow for any unfamiliar reaction:**
1. Count reactants and products on each side.
2. Note whether any free element (oxidation state 0) appears.
3. Assign oxidation numbers to confirm redox vs non-redox.
4. For double displacement, identify the driving force (precipitate, gas, water, weak electrolyte).

---

## High-Yield Takeaways

1. **Bohr model + E = -13.6/n^2** will appear in passage-based questions. Be ready to calculate transition energies and connect them to photon wavelength/frequency.
2. **Quantum numbers:** Know the rules cold. The most common question is "which set is invalid?"
3. **Electron configuration of ions:** Remove from 4s before 3d. This is tested repeatedly.
4. **Periodic trends:** Do not memorize trends in isolation. Understand Z_eff and shielding and you can derive any trend on the spot.
5. **Half-life:** Practice halving problems until they are automatic. Recognize common fractions (12.5% = 3 half-lives, 6.25% = 4 half-lives).
6. **Nuclear decay:** Know what each type does to A and Z. Know penetration vs. ionization tradeoff.
7. **Limiting reagent:** Convert to moles first. Always. Then divide by coefficient to find the limiting reagent.
8. **Oxidation numbers:** Assign them quickly. Recognizing oxidation state changes lets you identify redox reactions instantly.
9. **Reaction classification (Ch 4):** Pattern-recognize combination, decomposition, single/double displacement, and combustion. Single displacement and combustion are ALWAYS redox; double displacement is almost never.
10. **Equivalents and normality:** Use N = M × n and N_a·V_a = N_b·V_b for polyprotic titrations and multi-electron redox. GEW = molar mass / n gives the grams-per-equivalent for mass ↔ equivalents conversions.
