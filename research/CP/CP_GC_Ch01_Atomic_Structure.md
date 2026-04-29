# CP Gen Chem Chapter 1 — Atomic Structure

Scope: Subatomic particles; atomic mass vs weight; isotopes/ions; Rutherford → Bohr models; quantum mechanical model; quantum numbers; electron configuration; valence electrons.

**Section:** Chemical/Physical (CP)
**Book:** Kaplan General Chemistry — Chapter 1
**AAMC FC mapping:** FC4E (atomic structure portion); FC5B (orbitals overlap)
**Yield:** HIGH — underpins half of gen chem and connects to spectroscopy, bonding, and thermodynamics.

> Note: Periodic-trend material (atomic radius, IE, EA, EN, metallic character) lives in `CP_GC_Ch02_Periodic_Table.md`. Nuclear chemistry (decay types, half-life, mass defect/binding energy, medical applications) is preserved in physics legacy file `CP_Phy_Nuclear.md`.

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

### Atomic Mass vs. Atomic Weight

- **Atomic mass:** Mass of a single atom (typically of one specific isotope), measured in amu.
- **Atomic weight:** Weighted average of all naturally occurring isotopes of an element, accounting for their relative abundances. This is the value on the periodic table.

For chlorine: ~75% Cl-35 and ~25% Cl-37, giving an atomic weight of ~35.5 amu — note that no individual chlorine atom has this mass.

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

### Paramagnetism vs. Diamagnetism

- **Paramagnetic:** Has unpaired electrons; weakly attracted to magnetic fields. Most transition metal ions.
- **Diamagnetic:** All electrons paired; weakly repelled by magnetic fields. Noble gases, most main-group cations with full shells.

To predict: write the electron configuration, draw orbital diagram, count unpaired electrons.

---

## High-Yield Takeaways

1. **Bohr model + E = -13.6/n^2** will appear in passage-based questions. Be ready to calculate transition energies and connect them to photon wavelength/frequency.
2. **Quantum numbers:** Know the rules cold. The most common question is "which set is invalid?"
3. **Electron configuration of ions:** Remove from 4s before 3d. This is tested repeatedly.
4. **Cr and Cu exceptions** — half-filled and fully filled d-subshell stability.
5. **Paramagnetic vs diamagnetic** = unpaired vs all paired electrons.

---

→ Periodic trends: see `CP_GC_Ch02_Periodic_Table.md`
→ Nuclear chemistry (decay, half-life, fission/fusion): see `CP_Phy_Nuclear.md`
→ Orbital hybridization & MOs: see `CP_OC_Ch03_Bonding.md`
