# Physics & Math Chapter 9 — Atomic & Nuclear Physics

Scope: Photoelectric effect; emission and absorption spectra; Bohr model energy levels; nuclear binding energy and mass defect (E = mc²); radioactive decay types (alpha, beta, gamma, electron capture); half-life; nuclear reactions (fission, fusion); medical applications (PET scan, radiation therapy); de Broglie wavelength.

**Section:** Chemical/Physical (CP) — Physics & Math
**Book:** Kaplan Physics and Math Strategies 2024 — Chapter 9
**AAMC FC mapping:** FC4E (Atoms, nuclear reactions, electronic structure, atomic/nuclear phenomena)
**Yield:** High. Half-life calculations, nuclear decay (A and Z changes), photoelectric effect, and spectral series are all tested.

> **Note on atomic structure content:** Subatomic particles, electron configuration (Aufbau, Pauli, Hund's rule), quantum numbers (n, l, m_l, m_s), orbital shapes, and periodic trends are NOT in this chapter. That content belongs in `research/GenChem/Ch01_Atomic_Structure.md` and `Ch02_Periodic_Table.md`. Cross-reference Gen Chem Ch 1–2 for all electron configuration and periodic trend content.

---

## 1. Photoelectric Effect

### The Setup

When light shines on a metal surface, electrons can be ejected. This phenomenon provided key evidence for the particle nature of light and led to the quantum theory.

### The Equation

**KE_max = hf − φ**

Where:
- KE_max = maximum kinetic energy of ejected electrons
- h = Planck's constant (6.63 × 10⁻³⁴ J·s)
- f = frequency of incident light
- φ = **work function** (minimum energy needed to eject one electron, specific to the metal)

### Threshold Frequency

**f₀ = φ/h**

Below this frequency, **no electrons are ejected regardless of intensity.** This observation destroyed classical wave theory.

### Key Concepts the MCAT Tests

1. **Increasing intensity** (brighter light at same frequency): More photons → **more electrons ejected** (higher current), but **each electron has the same KE_max**. Intensity does NOT change energy per photon.

2. **Increasing frequency** (above threshold): Each photon has more energy → **KE_max increases**. Number of electrons stays the same (if intensity is constant).

3. **Below threshold frequency:** Zero electrons ejected, regardless of brightness. A billion low-energy photons cannot combine energy to eject one electron.

4. **Ejection is instantaneous:** No time delay, even at very low intensity. This contradicts the wave model (which predicts gradual energy accumulation).

**MCAT trap:** Confusing intensity and frequency effects.
- Intensity = **number of photons** per second
- Frequency = **energy per photon**
These are independent variables.

### Wave-Particle Duality

Light behaves as a **wave** (interference, diffraction, polarization) AND as a **particle** (photoelectric effect, Compton scattering).

**de Broglie wavelength:** All matter has wave-like properties.

**λ = h/p = h/(mv)**

Relevant for electrons and subatomic particles (macroscopic objects have negligibly small wavelengths). Increasing a particle's momentum → **decreasing wavelength**.

---

## 2. Atomic Emission and Absorption Spectra

### The Bohr Model (Hydrogen Atom)

Bohr's model works perfectly for **hydrogen and hydrogen-like ions** (one electron: H, He⁺, Li²⁺). Breaks down for multi-electron atoms.

**Key ideas:**
- Electrons orbit in fixed circular paths called **energy levels** (n = 1, 2, 3...).
- Lower n = closer to nucleus = more negative energy = more stable.
- **Ground state:** Electron in lowest available energy level.
- **Excited state:** Electron has absorbed energy and jumped to a higher level.

**Hydrogen atom energy equation:**

**E_n = −13.6 eV/n²**

- n = 1: E = −13.6 eV (ground state)
- n = 2: E = −3.4 eV
- n = 3: E = −1.51 eV
- n = ∞: E = 0 eV (electron free = ionized)

Energy becomes less negative (closer to zero) as n increases → electron is less tightly bound.

**Energy of a transition:**

ΔE = E_final − E_initial = −13.6(1/n_f² − 1/n_i²) eV

- Electron drops to lower level → energy **emitted** (ΔE negative, photon released)
- Electron jumps to higher level → energy **absorbed** (ΔE positive, photon absorbed)
- Energy of photon = |ΔE| → E = hf = hc/λ

### Spectral Series

| Series | Transition to n = | Region |
|--------|-------------------|--------|
| Lyman | 1 | Ultraviolet |
| Balmer | 2 | Visible |
| Paschen | 3 | Infrared |

**MCAT strategy:** Lyman → UV → largest energy gaps (transitions to n = 1). The bigger the jump, the higher the energy (shorter wavelength). n=3→n=1 releases more energy than n=3→n=2.

### Emission vs Absorption Spectra

**Emission spectrum:** Bright colored lines on dark background. Excited atoms release photons at specific wavelengths as electrons fall to lower levels.

**Absorption spectrum:** Dark lines on continuous colored background. Atoms absorb specific wavelengths from white light, exciting electrons upward.

Both spectra show the **same line positions** for a given element — they are complementary. Absorption lines exactly match emission lines.

---

## 3. Nuclear Chemistry

### Radioactive Decay Types

Know the particle emitted, the change in A (mass number) and Z (atomic number), and relative penetrating power.

| Decay type | Particle emitted | Change in A | Change in Z | Symbol |
|------------|-----------------|-------------|-------------|--------|
| Alpha | ⁴₂He (helium nucleus) | −4 | −2 | α |
| Beta-minus | ⁰₋₁e (electron) | 0 | +1 | β⁻ |
| Beta-plus (positron) | ⁰₊₁e (positron) | 0 | −1 | β⁺ |
| Gamma | Photon (EM radiation) | 0 | 0 | γ |
| Electron capture | Inner electron captured | 0 | −1 | EC |

#### Alpha Decay
- Ejects ⁴He nucleus (2 protons + 2 neutrons).
- A decreases by 4, Z decreases by 2. Element changes (moves 2 left on periodic table).
- **Penetration:** Very low (stopped by sheet of paper or skin).
- **Ionization:** Very high (large, slow, charged particle interacts constantly).
- Heavy, unstable nuclei (A > 200) tend to undergo alpha decay.

#### Beta-Minus Decay
- Neutron → proton + electron + antineutrino.
- A stays same, Z increases by 1. Occurs in **neutron-rich** nuclei.
- **Penetration:** Moderate (stopped by aluminum foil or thick clothing).

#### Beta-Plus (Positron Emission)
- Proton → neutron + positron + neutrino.
- A stays same, Z decreases by 1. Occurs in **proton-rich** nuclei.
- Positron quickly annihilates with an electron → **two 511 keV gamma rays at 180°** (basis of PET scans).

#### Electron Capture
- Nucleus captures an inner-shell (K-shell) electron.
- Proton + electron → neutron.
- Same result as positron emission: A stays same, Z decreases by 1.
- Competes with β⁺ in proton-rich nuclei, especially heavier atoms.
- Produces characteristic X-rays as outer electrons fill vacated inner shell.

#### Gamma Decay
- Nucleus drops from excited to lower energy state, emitting a high-energy photon.
- No change in A or Z. Often accompanies other decay types.
- **Penetration:** Very high (requires lead or thick concrete to stop).
- **Ionization:** Low (no charge, no mass — passes through without interacting much).

**Mnemonic for penetration:** Alpha < Beta < Gamma. For ionization, the reverse: Alpha > Beta > Gamma. More interaction with matter (ionizes more) → stops sooner (less penetration).

### Half-Life

**Definition:** Time for half of a radioactive sample to decay.

**Key equation:**

**N = N₀ × (½)^(t/t₁/₂)**

**Estimation strategies (no calculator needed):**

**Method 1 — Count half-lives (most common on MCAT):**
Elapsed time is a whole number of half-lives → halve repeatedly.

Example: 80 g sample, half-life = 5 years, 20 years elapsed.
20/5 = 4 half-lives → 80 → 40 → 20 → 10 → **5 g**

**Method 2 — Recognize common fractions:**
- 50% remaining = 1 half-life
- 25% = 2 half-lives
- 12.5% = 3 half-lives
- 6.25% = 4 half-lives
- 3.125% = 5 half-lives

**Activity (decay rate):** A = λN, where λ = ln(2)/t₁/₂ = 0.693/t₁/₂.
Activity also decreases by half with each half-life — same equation applies.

---

## 4. Mass Defect and Nuclear Binding Energy

**Mass defect (Δm):** The mass of a nucleus is LESS than the sum of the masses of its individual protons and neutrons.

**Δm = (Z · m_p + N · m_n) − m_nucleus**

This "missing mass" was converted to energy when the nucleus formed = **nuclear binding energy:**

**E = Δmc²** (Einstein's mass-energy equivalence)

This is the energy needed to completely disassemble the nucleus into individual nucleons.

### Binding Energy per Nucleon

Plot binding energy per nucleon vs mass number → famous curve:
- **Iron-56** (and nickel-62) sit at the peak — most stable nuclei.
- Lighter elements can gain stability by **fusion** (combining small nuclei → higher binding energy per nucleon).
- Heavier elements can gain stability by **fission** (splitting large nuclei → higher binding energy per nucleon).
- Both fusion and fission release energy because **products have higher binding energy per nucleon** than reactants.

**MCAT connection:**
- Fusion releases more energy per nucleon than fission. The sun runs on fusion (H → He).
- Nuclear reactors use fission (uranium-235).

---

## 5. Nuclear Reactions — Fission and Fusion

### Fission

**Heavy nucleus (A > 200) splits into two lighter nuclei + neutrons + energy.**

Example: ²³⁵U + neutron → ²³⁸Kr + ⁹⁰Ba + 3 neutrons + energy (chain reaction)

Each fission releases ~200 MeV. Products have higher binding energy/nucleon → energy released.

### Fusion

**Two light nuclei combine into a heavier nucleus + energy.**

Example: ²H + ³H → ⁴He + neutron + energy

Fusion releases more energy per unit mass than fission but requires extreme temperature/pressure to overcome electrostatic repulsion between nuclei (only achievable in stars and thermonuclear weapons).

### Q-value

**Q = (mass_reactants − mass_products) × c²**

- Q > 0: energy released (exothermic; binding energy increased)
- Q < 0: energy absorbed (endothermic)

---

## 6. Medical Applications

**PET scan (Positron Emission Tomography):**
- Patient injected with positron-emitting isotope (most common: ¹⁸F-FDG, a glucose analog)
- Positrons annihilate with electrons → two 511 keV gamma rays at 180°
- Detectors pick up coincident signals to localize source
- Used for metabolically active tissue (cancer, brain activity)

**Radiation therapy:**
- High-energy radiation (gamma rays, X-rays, proton beams) damages DNA in cancer cells
- Alpha emitters can be targeted directly to tumors (internal targeted therapy)

**Radioactive tracers:**
- Use chemical properties of the radioisotope to track metabolic pathways
- Example: ¹³¹I for thyroid (iodine concentrates in thyroid)

---

## MCAT Strategy Summary

### Pattern Recognition

| Trigger | Action |
|---------|--------|
| "How much remains after N half-lives?" | Multiply by (½)^N |
| "12.5% of sample remains" | (½)³ = 0.125 → 3 half-lives elapsed |
| "Nucleus loses alpha particle" | A −4, Z −2 |
| "Beta-minus decay" | A same, Z +1 (neutron → proton) |
| "Positron emission or electron capture" | A same, Z −1 |
| "Gamma only" | A same, Z same (nucleus drops from excited state) |
| "Intensity increases, more electrons but same KE" | Photoelectric: intensity = more photons, not more energy/photon |
| "Frequency increases above threshold" | Photoelectric: KE_max = hf − φ increases |
| "Why do fission/fusion release energy?" | Products have higher binding energy per nucleon than reactants |

### Common Traps

1. **Alpha = ⁴He.** Students confuse it with a proton or neutron. Alpha decay: A−4, Z−2.
2. **Beta-minus vs Beta-plus:** β⁻ increases Z (neutron → proton). β⁺ decreases Z (proton → neutron).
3. **Photoelectric effect — intensity vs frequency:** Intensity changes count (current), frequency changes KE per electron. NEVER mix these up.
4. **Half-life is constant.** It does not depend on temperature, pressure, or chemical form of the element.
5. **Binding energy is released when nucleus forms**, not when it breaks apart. More binding energy per nucleon = more stable = products of fission/fusion.

### Quick Reference

**Photoelectric:** KE_max = hf − φ | threshold: f₀ = φ/h
**Bohr model:** E_n = −13.6/n² eV
**Spectral series:** Lyman (UV, n→1) | Balmer (visible, n→2) | Paschen (IR, n→3)
**Decay changes:**
- α: A−4, Z−2
- β⁻: A same, Z+1
- β⁺/EC: A same, Z−1
- γ: A same, Z same
**Half-life:** N = N₀(½)^(t/t₁/₂)
**Mass defect:** Δm → E = Δmc² (binding energy)
**PET scan:** β⁺ emitter → positron annihilation → two 511 keV γ at 180°
**de Broglie:** λ = h/p = h/(mv)
