# CP Gen Chem Chapter 8 — Gas Phase

Scope: Ideal gas law and individual gas laws (Boyle, Charles, Gay-Lussac, Avogadro); STP molar volume; Dalton's law of partial pressures; kinetic molecular theory (KMT); rms velocity & Graham's law; real gas behavior (van der Waals); Henry's law.

**Section:** Chemical/Physical (CP)
**Book:** Kaplan General Chemistry — Chapter 8
**AAMC FC mapping:** FC4B (gas phase portion)
**Yield:** HIGH — gas laws + Dalton's law + KMT show up on every exam, especially through respiratory/gas exchange physiology.

> Note: Fluid statics/dynamics (Pascal, Archimedes, Bernoulli, Poiseuille, Starling) lives in physics legacy `CP_Phy_Fluids.md`.

---

## 1. The Ideal Gas Law

> **PV = nRT**

Where:
- P = pressure (atm or Pa)
- V = volume (L or m^3)
- n = moles of gas
- R = gas constant (0.0821 L·atm/mol·K or 8.314 J/mol·K)
- T = **absolute temperature** (Kelvin, always!)

**MCAT tip:** Every gas law problem requires temperature in Kelvin. If they give Celsius, convert first: K = C + 273. Using Celsius will wreck your answer.

---

## 2. Individual Gas Laws (Special Cases of PV = nRT)

All of these are just the ideal gas law with certain variables held constant:

| Law | Relationship | Held Constant | Equation |
|-----|-------------|---------------|----------|
| **Boyle's** | P and V are inversely proportional | n, T | P1V1 = P2V2 |
| **Charles's** | V and T are directly proportional | n, P | V1/T1 = V2/T2 |
| **Gay-Lussac's** | P and T are directly proportional | n, V | P1/T1 = P2/T2 |
| **Avogadro's** | V and n are directly proportional | P, T | V1/n1 = V2/n2 |

**At STP** (0°C = 273 K, 1 atm): 1 mole of ideal gas occupies **22.4 L**.

**Combined gas law** (when n is constant): P1V1/T1 = P2V2/T2.

**Worked approach -- Boyle's Law in the lungs:**
> During inhalation, the diaphragm contracts and the thoracic cavity volume increases from 6.0 L to 6.5 L. If the initial intrapulmonary pressure is 760 mmHg, what is the new pressure?

- P1V1 = P2V2
- (760)(6.0) = P2(6.5)
- P2 = 4560/6.5 = **701.5 mmHg**

Pressure dropped below atmospheric (760 mmHg), so air flows IN. This is exactly how breathing works -- Boyle's law in action.

---

## 3. Dalton's Law of Partial Pressures

> **P_total = P_A + P_B + P_C + ...**

Each gas in a mixture exerts pressure independently as if the other gases were not there. The **partial pressure** of a gas depends on its **mole fraction**:

> **P_A = X_A · P_total** where X_A = n_A / n_total

**Biological application -- Alveolar gas exchange:**

Atmospheric air at sea level (760 mmHg) is approximately:
- N2: 78% --> P_N2 = 0.78 x 760 = ~593 mmHg
- O2: 21% --> P_O2 = 0.21 x 760 = ~160 mmHg
- CO2: 0.04% --> P_CO2 = ~0.3 mmHg

In the alveoli, partial pressures are different because air is humidified and CO2 is added:
- P_O2 ~ 100 mmHg (alveolar), vs ~40 mmHg in deoxygenated blood --> O2 diffuses IN to blood
- P_CO2 ~ 40 mmHg (alveolar), vs ~46 mmHg in deoxygenated blood --> CO2 diffuses OUT of blood

**Gas exchange is driven entirely by partial pressure gradients.** No active transport -- just diffusion down concentration (partial pressure) gradients across the thin alveolar membrane.

---

## 4. Kinetic Molecular Theory (KMT)

Assumptions of an **ideal gas**:
1. Gas particles have **negligible volume** compared to the container
2. No intermolecular forces (no attraction or repulsion between particles)
3. Collisions are perfectly **elastic** (no energy lost)
4. Particles move in **random, straight-line** motion
5. **Average kinetic energy** is proportional to absolute temperature

The key quantitative relationship:

> **KE_avg = 3/2 · k_B · T**

Where k_B is Boltzmann's constant (1.38 x 10^-23 J/K) and T is in Kelvin.

This means: **at a given temperature, ALL gases have the same average kinetic energy**, regardless of their molecular mass. A helium atom and a xenon atom at the same temperature have the same average KE.

But since KE = 1/2 · m · v^2, lighter gases must move **faster** to have the same KE:

> **v_rms = sqrt(3RT/M)**

Where M is molar mass (in kg/mol if R = 8.314 J/mol·K).

**MCAT tip:** Lighter gases diffuse faster (Graham's law), effuse faster, and have higher average speeds. At the same temperature:
- rate1/rate2 = sqrt(M2/M1)
- H2 moves 4x faster than O2 (since sqrt(32/2) = 4)

**Maxwell-Boltzmann distribution:** Speeds of gas molecules at a given T form a distribution; mean speed scales with sqrt(T/M). At higher T, the distribution flattens and shifts right (more high-speed molecules).

---

## 5. Real Gases and the van der Waals Equation

Real gases deviate from ideal behavior. The **van der Waals equation** corrects for this:

> **(P + a·n^2/V^2)(V - nb) = nRT**

The two corrections:
- **a·n^2/V^2** corrects for **intermolecular attractions** (real molecules attract each other, so actual pressure is lower than ideal; we add a term to compensate)
- **nb** corrects for **molecular volume** (real molecules take up space, so actual free volume is less than container volume; we subtract the volume occupied by molecules)

**When do gases deviate most from ideal behavior?**
- **High pressure** (molecules forced close together --> volume matters, intermolecular forces matter)
- **Low temperature** (molecules move slowly --> intermolecular attractions have more effect, can condense)

**When are gases most ideal?**
- **Low pressure, high temperature** (molecules far apart, moving fast, attractions negligible)

**MCAT tip:** Large, polar molecules (like NH3, H2O vapor) deviate more from ideal behavior than small, nonpolar ones (like He, Ne). Larger "a" values indicate stronger intermolecular forces; larger "b" values indicate larger molecular volumes.

**Worked approach -- Real vs Ideal:**
> Which gas behaves most ideally at room temperature and 1 atm: He, CO2, NH3, or H2O?

He -- it is a noble gas (smallest, nonpolar, weakest intermolecular forces). It has the smallest a and b values. CO2, NH3, and H2O all have stronger intermolecular forces and larger molecular volumes.

---

## 6. Henry's Law (Gas Solubility)

The amount of gas dissolved in a liquid is proportional to the partial pressure of that gas above the liquid:

> **[gas]_dissolved = k_H · P_gas**

This explains:
- Why CO2 dissolves out of soda when you open the can (P_CO2 drops)
- Decompression sickness ("the bends") -- at depth, high P_N2 causes more N2 to dissolve in blood; rapid ascent drops P_N2 suddenly, and N2 comes out of solution as bubbles
- Why oxygen delivery to tissues depends on P_O2

---

## High-Yield Takeaways

1. **Always use Kelvin** in PV=nRT.
2. **STP:** 22.4 L/mol at 0°C, 1 atm.
3. **Boyle's law** explains breathing (Volume↑ → Pressure↓ → air in).
4. **Dalton's law** drives alveolar gas exchange — partial pressure gradients only.
5. **KMT:** at same T, all gases have same KE_avg; lighter ones move faster (v_rms ∝ 1/√M).
6. **Graham's law:** rate1/rate2 = √(M2/M1).
7. **Real gas deviation:** worst at high P, low T. He behaves most ideally; polar/large molecules deviate most.
8. **Henry's law:** gas dissolved ∝ partial pressure (the bends).

---

→ Solutions & concentration: `CP_GC_Ch09_Solutions.md`
→ Bonding & IMFs (why real gases deviate): `CP_GC_Ch03_Bonding.md`
→ Fluid statics/dynamics (Bernoulli, Poiseuille, Starling): `CP_Phy_Fluids.md`
→ Respiratory physiology: `BB_Bio_Ch06_Respiratory.md`
