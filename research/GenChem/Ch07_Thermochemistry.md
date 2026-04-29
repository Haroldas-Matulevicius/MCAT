# CP Gen Chem Chapter 7 — Thermochemistry

Scope: Systems & processes; state functions vs path functions; laws of thermodynamics; enthalpy (Hess's law, BDE, formation); entropy; Gibbs free energy; calorimetry; phase diagrams; bioenergetics (ATP, NADH/FADH₂, chemiosmotic theory).

**Section:** Chemical/Physical (CP)
**Book:** Kaplan General Chemistry — Chapter 7
**AAMC FC mapping:** FC5E (thermo); FC1D crossover (bioenergetics)
**Yield:** VERY HIGH — ΔG = ΔH - TΔS reasoning is among the most tested concepts on the entire exam.

---

## 1. State Functions vs Path Functions

This distinction matters conceptually and shows up in discrete questions.

**State functions** depend only on the initial and final states of a system -- not on how you got there. Think of them like elevation: it doesn't matter which trail you hiked, the altitude at the summit is the same.

| State Functions | What They Measure |
|----------------|-------------------|
| **H** (enthalpy) | Heat content at constant pressure |
| **S** (entropy) | Disorder/microstates |
| **G** (Gibbs free energy) | Spontaneity |
| **U** (internal energy) | Total energy of system |
| **T** (temperature) | Average kinetic energy |
| **P** (pressure) | Force per unit area |
| **V** (volume) | Space occupied |

**Path functions** depend on the specific process taken between states:

| Path Functions | What They Measure |
|---------------|-------------------|
| **q** (heat) | Energy transferred due to temperature difference |
| **w** (work) | Energy transferred by force through displacement |

**MCAT trap:** A question might describe two different paths between the same two states and ask which thermodynamic quantity changes. If it's a state function, the answer is "same for both paths." If it asks about q or w individually, those CAN differ between paths.

---

## 2. Laws of Thermodynamics

**Zeroth Law:** If system A is in thermal equilibrium with C, and B is in thermal equilibrium with C, then A and B are in thermal equilibrium with each other. This formally establishes temperature as a measurable, transitive property.

**First Law (Conservation of Energy):**

> **ΔU = q - w**

- **ΔU** = change in internal energy of the system
- **q** = heat added TO the system (positive when system absorbs heat)
- **w** = work done BY the system (positive when system does work on surroundings)

**Sign convention matters on the MCAT.** Some textbooks use ΔU = q + w (where w is work done ON the system). The AAMC uses the convention above (q - w), but read the question carefully. Either way:
- System absorbs heat: q is positive
- System releases heat: q is negative
- System expands against surroundings (does work): w is positive (using q - w convention)
- System is compressed (work done on it): w is negative (using q - w convention)

For an **isolated system** (no heat or work exchange): ΔU = 0.
For an **adiabatic process** (no heat exchange): q = 0, so ΔU = -w.
For a **constant volume process:** w = 0 (no PdV work), so ΔU = q_v.

**Second Law:** The total entropy of the universe always increases for any spontaneous process.

> **ΔS_universe = ΔS_system + ΔS_surroundings >= 0**

The entropy of a SYSTEM can decrease (like when water freezes), but only if the surroundings gain MORE entropy to compensate. The universe as a whole always trends toward greater disorder.

**Third Law:** The entropy of a perfect crystal at absolute zero (0 K) is zero. Provides an absolute reference for entropy values.

---

## 3. Enthalpy (H)

**Enthalpy = the heat exchanged at constant pressure.** Since most biological and bench-top reactions occur at constant atmospheric pressure, enthalpy is the practical measure of heat flow.

> **ΔH = q_p** (at constant pressure)

**Exothermic reactions:** ΔH < 0. The system RELEASES heat to surroundings. Products are more stable (lower energy) than reactants. Example: combustion, neutralization reactions.

**Endothermic reactions:** ΔH > 0. The system ABSORBS heat from surroundings. Products are less stable (higher energy) than reactants. Example: dissolving ammonium nitrate, photosynthesis.

### Hess's Law

Since H is a state function, the total enthalpy change for a reaction is the same regardless of the pathway. This means you can:

1. **Reverse a reaction** -- flip the sign of ΔH
2. **Multiply a reaction** -- multiply ΔH by the same factor
3. **Add reactions** -- add the ΔH values

This is tested directly. You'll get 2-3 reactions with known ΔH values and need to combine them to find ΔH for a target reaction.

### Bond Dissociation Energy (BDE) Approach

> **ΔH_rxn = sum(bonds broken) - sum(bonds formed)**

- Breaking bonds COSTS energy (endothermic, positive)
- Forming bonds RELEASES energy (exothermic, negative)
- If you form stronger bonds than you break, the reaction is exothermic

**MCAT tip:** This formula uses "broken minus formed." Think: you have to PUT IN energy to break bonds (positive), and you GET BACK energy when bonds form (negative). The net is broken minus formed.

### Standard Enthalpy of Formation

> **ΔH_rxn = sum[ΔH_f(products)] - sum[ΔH_f(reactants)]**

The standard enthalpy of formation of any element in its standard state is zero by definition.

---

## 4. Entropy (S)

**Entropy measures the number of microstates** -- the number of ways energy can be distributed in a system. More microstates = more entropy = more disorder.

### Predicting the Sign of ΔS

Ask: does the system become more disordered?

| Change | ΔS |
|--------|--------|
| Solid -> Liquid -> Gas | **Positive** (more freedom of motion) |
| Fewer gas moles -> More gas moles | **Positive** |
| Dissolving a solid in solvent | **Usually positive** (more dispersed) |
| Increasing temperature | **Positive** (more kinetic energy, more microstates) |
| Gas -> Liquid -> Solid | **Negative** (less freedom) |
| More gas moles -> Fewer gas moles | **Negative** |
| 2 molecules combining into 1 | **Negative** |

**MCAT trick:** When a gas dissolves in a liquid, entropy can actually DECREASE because gas molecules become more ordered in solution. Don't autopilot -- think about the physical change.

**Phase transitions:** At the exact phase transition temperature (e.g., 0°C for ice/water at 1 atm), ΔG = 0 and ΔS = ΔH / T.

---

## 5. Gibbs Free Energy (G)

This is the master equation of thermodynamics for the MCAT.

> **ΔG = ΔH - T·ΔS**

| ΔG | Meaning |
|--------|---------|
| ΔG < 0 | **Spontaneous** (exergonic) -- reaction proceeds forward |
| ΔG > 0 | **Non-spontaneous** (endergonic) -- reaction does NOT proceed without energy input |
| ΔG = 0 | **Equilibrium** -- no net change |

**Critical point:** Spontaneous does NOT mean fast. A reaction can be thermodynamically spontaneous but kinetically slow (diamond -> graphite is spontaneous but takes geological time). Thermodynamics tells you IF a reaction can happen; kinetics tells you HOW FAST.

### The Four ΔH / ΔS Combinations

| ΔH | ΔS | ΔG | Spontaneity |
|--------|--------|--------|-------------|
| Negative (exo) | Positive (more disorder) | **Always negative** | **Spontaneous at ALL temperatures** |
| Negative (exo) | Negative (less disorder) | Depends on T | Spontaneous at **LOW T** (enthalpy-driven) |
| Positive (endo) | Positive (more disorder) | Depends on T | Spontaneous at **HIGH T** (entropy-driven) |
| Positive (endo) | Negative (less disorder) | **Always positive** | **NEVER spontaneous** |

**Memory hook for the "depends on T" cases:**
- When ΔH and ΔS have the SAME sign, temperature determines spontaneity
- The crossover temperature where ΔG = 0 is: **T = ΔH / ΔS**

**MCAT favorite:** "At what temperature does this reaction become spontaneous?" Set ΔG = 0 and solve for T = ΔH / ΔS.

### Connecting to Equilibrium

> **ΔG° = -RT * ln(Keq)**
> **ΔG = ΔG° + RT * ln(Q)**

(See Ch06 Equilibrium for full discussion.)

---

## 6. Calorimetry

> **q = mc * ΔT**

- **q** = heat (J or cal)
- **m** = mass (g)
- **c** = specific heat capacity (J/g·K or cal/g·K)
- **ΔT** = T_final - T_initial

For water: c = 4.184 J/(g·K) = 1 cal/(g·K). Memorize this.

**Coffee cup calorimeter (constant pressure):**
- Open to atmosphere, so pressure is constant
- q_p = ΔH
- Used for reactions in solution (acid-base, dissolution)
- Assumes all heat goes to the water: q_rxn = -q_water = -mc·ΔT

**Bomb calorimeter (constant volume):**
- Sealed, rigid container -- no PdV work possible
- q_v = ΔU (not ΔH)
- Used for combustion reactions
- q_rxn = -C_cal · ΔT (where C_cal is the heat capacity of the calorimeter in J/K)

**MCAT distinction:** "Constant pressure" → enthalpy. "Constant volume" or "bomb calorimeter" → internal energy. The difference between ΔH and ΔU is usually small for reactions not involving gases: ΔH = ΔU + P·ΔV. For reactions with gas changes, ΔH = ΔU + Δ(n_gas)·RT.

---

## 7. Phase Diagrams

Phase diagrams plot pressure (y-axis) vs temperature (x-axis) and show which phase is stable at any given P and T.

**Key features:**
- **Triple point:** The unique P and T where solid, liquid, and gas coexist in equilibrium. All three phase boundary lines meet here.
- **Critical point:** Beyond this T and P, the distinction between liquid and gas disappears (supercritical fluid). No phase boundary above this point.
- **Phase boundary lines:** Crossing a line = phase transition. Moving along a line = two phases coexist.
- **Normal boiling point:** Temperature where liquid-gas boundary crosses P = 1 atm.
- **Normal melting point:** Temperature where solid-liquid boundary crosses P = 1 atm.

**Water's anomaly:** For most substances, the solid-liquid boundary slopes to the RIGHT (increasing P raises melting point). For water, it slopes to the LEFT -- increasing pressure LOWERS the melting point. This is because ice is less dense than liquid water (ice floats). The MCAT loves this distinction.

**Heating curves:** These plot temperature vs heat added. Flat regions = phase changes (heat goes into breaking intermolecular forces, not raising T). The length of the flat region depends on the enthalpy of the phase transition (ΔH_fus for melting, ΔH_vap for boiling). ΔH_vap > ΔH_fus because you're fully separating molecules.

**Clausius-Clapeyron equation:** Relates vapor pressure to temperature. As T increases, vapor pressure increases exponentially. The MCAT won't ask you to derive it, but you should know: ln(P2/P1) = -ΔH_vap/R · (1/T2 - 1/T1). Higher ΔH_vap = lower vapor pressure at a given T (stronger IMFs = harder to vaporize).

---

## 8. Bioenergetics

### 8.1 ATP: The Energy Currency

**ATP (adenosine triphosphate)** stores and transfers energy in biological systems.

**Structure:** Adenine (base) + ribose (sugar) + three phosphate groups linked by phosphoanhydride bonds.

**ATP hydrolysis:**

> ATP + H_2O → ADP + P_i    ΔG ≈ -30.5 kJ/mol (-7.3 kcal/mol)

**Why is ATP hydrolysis so exergonic?**
1. **Charge repulsion relief:** Three negatively charged phosphate groups are crowded together. Removing one relieves electrostatic repulsion.
2. **Resonance stabilization:** The products (ADP and P_i) have MORE resonance structures than ATP, making them more stable.
3. **Hydration stabilization:** The products are better hydrated by water than ATP.
4. **Entropy increase:** One molecule becomes two.

**MCAT note:** ATP is NOT "high-energy" in absolute terms. It has an intermediate energy of hydrolysis, which makes it useful as an energy SHUTTLE. It can accept energy from higher-energy compounds (like phosphoenolpyruvate, 1,3-BPG) and donate energy to drive lower-energy reactions.

**Phosphoryl group transfer potential:** PEP > 1,3-BPG > ATP > glucose-6-phosphate. Compounds with HIGHER transfer potential can drive phosphorylation of compounds with LOWER transfer potential.

### 8.2 Coupled Reactions

An energetically unfavorable reaction (ΔG > 0) can be driven forward by coupling it to an energetically favorable reaction (like ATP hydrolysis) so that the NET ΔG is negative.

**How to calculate:** Just ADD the ΔG values.

**Example:**
- Glutamate + NH_3 → Glutamine     ΔG = +14.2 kJ/mol (unfavorable alone)
- ATP → ADP + P_i                    ΔG = -30.5 kJ/mol
- **Coupled:** Glutamate + NH_3 + ATP → Glutamine + ADP + P_i    ΔG = -16.3 kJ/mol (favorable!)

**MCAT principle:** Most biosynthetic (anabolic) reactions are endergonic and are driven by coupling to ATP hydrolysis.

### 8.3 Electron Carriers: NAD+ and FAD

These are coenzymes that carry high-energy electrons between metabolic reactions.

#### NAD+ / NADH

- **NAD+** is the oxidized form (accepts electrons)
- **NADH** is the reduced form (carries electrons)
- NAD+ + 2H → NADH + H+ (accepts 2 electrons and 1 proton; the hydride ion :H-)
- Derived from niacin (vitamin B3)
- Operates in: glycolysis, pyruvate dehydrogenase, TCA cycle, beta-oxidation, ETC
- Each NADH yields approximately **2.5 ATP** via oxidative phosphorylation (ETC)

#### FAD / FADH2

- **FAD** is the oxidized form
- **FADH2** is the reduced form
- FAD + 2H → FADH2 (accepts 2 electrons and 2 protons)
- Derived from riboflavin (vitamin B2)
- Often covalently bound to enzyme (prosthetic group), as in succinate dehydrogenase
- Operates in: TCA cycle (succinate dehydrogenase), beta-oxidation, ETC
- Each FADH2 yields approximately **1.5 ATP** via oxidative phosphorylation

**Why the difference?** FADH2 enters the ETC at Complex II, bypassing the proton pumping at Complex I. So it drives fewer protons across the membrane and generates less ATP.

#### NADPH

- Similar to NADH but with an extra phosphate group
- **Used for ANABOLIC (biosynthetic) reactions** -- fatty acid synthesis, cholesterol synthesis, nucleotide synthesis
- Generated primarily by the **pentose phosphate pathway**
- NADH is for catabolism (making ATP); NADPH is for anabolism (building molecules)

### 8.4 Chemiosmotic Theory (Mitchell Hypothesis)

**Peter Mitchell's chemiosmotic theory** explains how the energy from electron transport is used to make ATP.

**The key idea:** The electron transport chain pumps protons (H+) from the mitochondrial matrix to the intermembrane space, creating a **proton-motive force** (electrochemical gradient). This gradient has two components:
1. **Chemical gradient** (concentration difference -- more H+ in intermembrane space)
2. **Electrical gradient** (charge difference -- intermembrane space is more positive)

**ATP synthase** (Complex V) is a molecular turbine. Protons flow back DOWN their gradient through ATP synthase, and this flow drives the mechanical rotation that catalyzes:

> ADP + P_i → ATP

**Key points for the MCAT:**
- The inner mitochondrial membrane must be INTACT for oxidative phosphorylation (the gradient must be maintained)
- **Uncouplers** (e.g., 2,4-DNP, thermogenin/UCP1 in brown fat) dissipate the proton gradient by allowing H+ to cross the membrane without going through ATP synthase. ETC runs but ATP is NOT made. Energy is released as HEAT.
- **Oligomycin** directly blocks ATP synthase. Proton gradient builds up, which also slows ETC (no place for protons to go).
- **Cyanide and CO** block Complex IV. ETC stops entirely. No gradient, no ATP.

**Stoichiometry (approximate):**
- 1 NADH → ~10 H+ pumped → ~2.5 ATP
- 1 FADH2 → ~6 H+ pumped → ~1.5 ATP
- ~4 H+ needed per ATP synthesized (3 through ATP synthase + 1 for phosphate transport)
- Total from 1 glucose (aerobic): ~30-32 ATP

---

## High-Yield Takeaways

1. **State vs path functions:** H, S, G, U, T, P, V are state. q, w are path.
2. **First law:** ΔU = q - w. **Second law:** universe entropy always increases.
3. **Hess's law:** combine reactions to find ΔH for target.
4. **BDE:** ΔH = bonds broken − bonds formed.
5. **Sign of ΔS:** more gas, more dispersed, higher T → +ΔS.
6. **ΔG = ΔH - TΔS.** Four sign combos predict spontaneity.
7. **Crossover T:** T = ΔH/ΔS gives the temperature where reaction switches.
8. **Calorimetry:** coffee cup (const P → ΔH) vs bomb (const V → ΔU).
9. **Water phase diagram:** solid-liquid line slopes LEFT (anomaly).
10. **ATP hydrolysis ≈ -30.5 kJ/mol;** drives coupled reactions; ~30-32 ATP per glucose aerobically.

---

→ Equilibrium / ΔG° → Keq: `CP_GC_Ch06_Equilibrium.md`
→ Kinetics & Arrhenius: `CP_GC_Ch05_Kinetics.md`
→ Electrochemistry & ΔG = -nFE: `CP_GC_Ch12_Electrochemistry.md`
→ Carb metabolism / ETC details: `BB_Ch10_CarbMetab2.md`, `BB_Ch12_Bioenergetics.md`
