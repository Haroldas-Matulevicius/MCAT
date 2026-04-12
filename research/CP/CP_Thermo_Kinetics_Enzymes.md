# FC5E: Thermodynamics, Kinetics, and Enzymes

> **Sections:** Gen Chem + Biochem | **Tested on:** Chem/Phys (primary) + Bio/Biochem (enzymes)
> **Yield:** VERY HIGH -- thermodynamics and enzyme kinetics are among the most tested topics on the entire exam.

---

## 1. Thermodynamics

### 1.1 State Functions vs Path Functions

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

**Memory hook:** State functions have exact differentials. You don't need to know the calculus -- just remember that delta-H, delta-S, delta-G, and delta-U are path-independent. Heat and work are not.

---

### 1.2 Laws of Thermodynamics

**Zeroth Law:** If system A is in thermal equilibrium with system C, and system B is in thermal equilibrium with system C, then A and B are in thermal equilibrium with each other. This is the basis for thermometers -- it sounds trivial but it formally establishes that temperature is a measurable, transitive property.

**First Law (Conservation of Energy):**

> **deltaU = q - w**

- **deltaU** = change in internal energy of the system
- **q** = heat added TO the system (positive when system absorbs heat)
- **w** = work done BY the system (positive when system does work on surroundings)

**Sign convention matters on the MCAT.** Some textbooks use deltaU = q + w (where w is work done ON the system). The AAMC uses the convention above (q - w), but read the question carefully. Either way:
- System absorbs heat: q is positive
- System releases heat: q is negative
- System expands against surroundings (does work): w is positive (using q - w convention)
- System is compressed (work done on it): w is negative (using q - w convention)

For an **isolated system** (no heat or work exchange): deltaU = 0.
For an **adiabatic process** (no heat exchange): q = 0, so deltaU = -w.
For a **constant volume process:** w = 0 (no PdV work), so deltaU = q_v.

**Second Law:** The total entropy of the universe always increases for any spontaneous process.

> **deltaS_universe = deltaS_system + deltaS_surroundings >= 0**

The entropy of a SYSTEM can decrease (like when water freezes), but only if the surroundings gain MORE entropy to compensate. The universe as a whole always trends toward greater disorder.

**Third Law:** The entropy of a perfect crystal at absolute zero (0 K) is zero. This gives us an absolute reference point for entropy values. Low-yield on the MCAT but occasionally referenced.

---

### 1.3 Enthalpy (H)

**Enthalpy = the heat exchanged at constant pressure.** Since most biological and bench-top reactions occur at constant atmospheric pressure, enthalpy is the practical measure of heat flow.

> **deltaH = q_p** (at constant pressure)

**Exothermic reactions:** deltaH < 0. The system RELEASES heat to surroundings. Products are more stable (lower energy) than reactants. Example: combustion, neutralization reactions.

**Endothermic reactions:** deltaH > 0. The system ABSORBS heat from surroundings. Products are less stable (higher energy) than reactants. Example: dissolving ammonium nitrate, photosynthesis.

#### Hess's Law

Since H is a state function, the total enthalpy change for a reaction is the same regardless of the pathway. This means you can:

1. **Reverse a reaction** -- flip the sign of deltaH
2. **Multiply a reaction** -- multiply deltaH by the same factor
3. **Add reactions** -- add the deltaH values

This is tested directly. You'll get 2-3 reactions with known deltaH values and need to combine them to find deltaH for a target reaction.

#### Bond Dissociation Energy (BDE) Approach

> **deltaH_rxn = sum(bonds broken) - sum(bonds formed)**

- Breaking bonds COSTS energy (endothermic, positive)
- Forming bonds RELEASES energy (exothermic, negative)
- If you form stronger bonds than you break, the reaction is exothermic

**MCAT tip:** This formula uses "broken minus formed." Some students reverse it. Think of it this way: you have to PUT IN energy to break bonds (positive), and you GET BACK energy when bonds form (negative). The net is broken minus formed.

#### Standard Enthalpy of Formation

> **deltaH_rxn = sum[deltaH_f(products)] - sum[deltaH_f(reactants)]**

The standard enthalpy of formation of any element in its standard state is zero by definition.

---

### 1.4 Entropy (S)

**Entropy measures the number of microstates** -- the number of ways energy can be distributed in a system. More microstates = more entropy = more disorder.

#### Predicting the Sign of deltaS

Ask: does the system become more disordered?

| Change | deltaS |
|--------|--------|
| Solid -> Liquid -> Gas | **Positive** (more freedom of motion) |
| Fewer gas moles -> More gas moles | **Positive** |
| Dissolving a solid in solvent | **Usually positive** (more dispersed) |
| Increasing temperature | **Positive** (more kinetic energy, more microstates) |
| Gas -> Liquid -> Solid | **Negative** (less freedom) |
| More gas moles -> Fewer gas moles | **Negative** |
| 2 molecules combining into 1 | **Negative** |

**MCAT trick:** When a gas dissolves in a liquid, entropy can actually DECREASE because gas molecules become more ordered in solution. Don't autopilot -- think about the physical change.

**Phase transitions:** At the exact phase transition temperature (e.g., 0 degrees C for ice/water at 1 atm), deltaG = 0 and deltaS = deltaH / T.

---

### 1.5 Gibbs Free Energy (G)

This is the master equation of thermodynamics for the MCAT.

> **deltaG = deltaH - T*deltaS**

| deltaG | Meaning |
|--------|---------|
| deltaG < 0 | **Spontaneous** (exergonic) -- reaction proceeds forward |
| deltaG > 0 | **Non-spontaneous** (endergonic) -- reaction does NOT proceed without energy input |
| deltaG = 0 | **Equilibrium** -- no net change |

**Critical point:** Spontaneous does NOT mean fast. A reaction can be thermodynamically spontaneous but kinetically slow (diamond -> graphite is spontaneous but takes geological time). Thermodynamics tells you IF a reaction can happen; kinetics tells you HOW FAST.

#### The Four deltaH / deltaS Combinations

| deltaH | deltaS | deltaG | Spontaneity |
|--------|--------|--------|-------------|
| Negative (exo) | Positive (more disorder) | **Always negative** | **Spontaneous at ALL temperatures** |
| Negative (exo) | Negative (less disorder) | Depends on T | Spontaneous at **LOW T** (enthalpy-driven) |
| Positive (endo) | Positive (more disorder) | Depends on T | Spontaneous at **HIGH T** (entropy-driven) |
| Positive (endo) | Negative (less disorder) | **Always positive** | **NEVER spontaneous** |

**Memory hook for the "depends on T" cases:**
- When deltaH and deltaS have the SAME sign, temperature determines spontaneity
- The crossover temperature where deltaG = 0 is: **T = deltaH / deltaS**

**MCAT favorite:** "At what temperature does this reaction become spontaneous?" Set deltaG = 0 and solve for T = deltaH / deltaS. Make sure units match (J vs kJ, and deltaS is usually in J/mol*K).

---

### 1.6 Key Relationships: Connecting Thermo to Equilibrium

> **deltaG-standard = -RT * ln(Keq)**

This connects the standard free energy change to the equilibrium constant.

| deltaG-standard | Keq | Meaning |
|----------------|-----|---------|
| Negative | > 1 | Products favored at equilibrium |
| Zero | = 1 | Neither favored |
| Positive | < 1 | Reactants favored at equilibrium |

> **deltaG = deltaG-standard + RT * ln(Q)**

This gives the ACTUAL free energy change under non-standard conditions, where Q is the reaction quotient.

- At equilibrium: Q = Keq, so deltaG = 0 (confirms deltaG-standard = -RT*ln(Keq))
- When Q < Keq: ln(Q) < ln(Keq), so deltaG < deltaG-standard, reaction proceeds forward
- When Q > Keq: ln(Q) > ln(Keq), reaction proceeds in reverse

**MCAT tip:** R = 8.314 J/(mol*K) and T is in Kelvin. Watch units -- if deltaG is in kJ, convert R or deltaG to match.

---

### 1.7 Calorimetry

> **q = mc * deltaT**

- **q** = heat (J or cal)
- **m** = mass (g)
- **c** = specific heat capacity (J/g*K or cal/g*K)
- **deltaT** = T_final - T_initial

For water: c = 4.184 J/(g*K) = 1 cal/(g*K). You should have this memorized.

**Coffee cup calorimeter (constant pressure):**
- Open to atmosphere, so pressure is constant
- q_p = deltaH
- Used for reactions in solution (acid-base, dissolution)
- Assumes all heat goes to the water: q_rxn = -q_water = -mc*deltaT

**Bomb calorimeter (constant volume):**
- Sealed, rigid container -- no PdV work possible
- q_v = deltaU (not deltaH)
- Used for combustion reactions
- q_rxn = -C_cal * deltaT (where C_cal is the heat capacity of the calorimeter in J/K)

**MCAT distinction:** If a question says "constant pressure," think enthalpy. If it says "constant volume" or "bomb calorimeter," think internal energy. The difference between deltaH and deltaU is usually small for reactions not involving gases: deltaH = deltaU + P*deltaV. For reactions with gas changes, deltaH = deltaU + delta(n_gas)*RT.

---

### 1.8 Phase Diagrams

Phase diagrams plot pressure (y-axis) vs temperature (x-axis) and show which phase is stable at any given P and T.

**Key features:**
- **Triple point:** The unique P and T where solid, liquid, and gas coexist in equilibrium. All three phase boundary lines meet here.
- **Critical point:** Beyond this T and P, the distinction between liquid and gas disappears (supercritical fluid). No phase boundary above this point.
- **Phase boundary lines:** Crossing a line = phase transition. Moving along a line = two phases coexist.
- **Normal boiling point:** Temperature where liquid-gas boundary crosses P = 1 atm.
- **Normal melting point:** Temperature where solid-liquid boundary crosses P = 1 atm.

**Water's anomaly:** For most substances, the solid-liquid boundary slopes to the RIGHT (increasing P raises melting point). For water, it slopes to the LEFT -- increasing pressure LOWERS the melting point. This is because ice is less dense than liquid water (ice floats). The MCAT loves this distinction.

**Heating curves:** These plot temperature vs heat added. Flat regions = phase changes (heat goes into breaking intermolecular forces, not raising T). The length of the flat region depends on the enthalpy of the phase transition (deltaH_fus for melting, deltaH_vap for boiling). deltaH_vap > deltaH_fus because you're fully separating molecules.

**Clausius-Clapeyron equation:** Relates vapor pressure to temperature. As T increases, vapor pressure increases exponentially. The MCAT won't ask you to derive it, but you should know: ln(P2/P1) = -deltaH_vap/R * (1/T2 - 1/T1). Higher deltaH_vap = lower vapor pressure at a given T (stronger IMFs = harder to vaporize).

---

## 2. Chemical Kinetics

### 2.1 Rate Laws

The rate of a reaction tells you how fast reactants are consumed or products are formed.

> **Rate = k[A]^n[B]^m**

- **k** = rate constant (units depend on overall order)
- **n** = order with respect to A
- **m** = order with respect to B
- **n + m** = overall reaction order

**Reaction order is determined EXPERIMENTALLY, not from stoichiometry.** This is a common MCAT misconception. The balanced equation tells you nothing about the rate law unless it's an elementary step.

#### Method of Initial Rates

This is the standard MCAT approach for determining order. You're given a table of experiments with different initial concentrations and initial rates.

**Procedure:**
1. Find two experiments where only ONE reactant's concentration changes
2. See how the rate changes
3. Determine the order:

| Concentration Change | Rate Change | Order |
|---------------------|-------------|-------|
| Doubled (x2) | No change (x1) | **Zero order** (2^0 = 1) |
| Doubled (x2) | Doubled (x2) | **First order** (2^1 = 2) |
| Doubled (x2) | Quadrupled (x4) | **Second order** (2^2 = 4) |
| Tripled (x3) | Tripled (x3) | **First order** (3^1 = 3) |
| Tripled (x3) | Ninefolded (x9) | **Second order** (3^2 = 9) |

**General pattern:** If concentration changes by factor x and rate changes by factor y, then order n = log(y)/log(x). On the MCAT you can usually identify this by inspection.

#### Units of k by Reaction Order

| Overall Order | Units of k |
|--------------|------------|
| 0 | M/s (or mol L^-1 s^-1) |
| 1 | s^-1 (or 1/s) |
| 2 | M^-1 s^-1 (or L mol^-1 s^-1) |

**MCAT shortcut:** If they give you units of k, you can determine the overall order without any other information.

---

### 2.2 Integrated Rate Laws

These relate concentration to time and are used to determine order from a single experiment's data.

#### Zero Order

> **[A] = [A]_0 - kt**

- Plot **[A] vs t** -- gives a **straight line** (slope = -k)
- Half-life: t_1/2 = [A]_0 / (2k) -- depends on initial concentration
- Rate is constant regardless of concentration

#### First Order

> **ln[A] = ln[A]_0 - kt**

- Plot **ln[A] vs t** -- gives a **straight line** (slope = -k)
- Half-life: **t_1/2 = 0.693 / k** -- INDEPENDENT of concentration
- This is the only order with a constant half-life
- Radioactive decay follows first-order kinetics

#### Second Order

> **1/[A] = 1/[A]_0 + kt**

- Plot **1/[A] vs t** -- gives a **straight line** (slope = +k)
- Half-life: t_1/2 = 1 / (k[A]_0) -- depends on initial concentration

**MCAT strategy for "which order" questions:** They'll give you data and ask you to identify the order. Check which plot gives a straight line:
- [A] vs t linear = zero order
- ln[A] vs t linear = first order
- 1/[A] vs t linear = second order

---

### 2.3 Half-Life

**Half-life (t_1/2)** = time for the concentration to decrease to half its current value.

| Order | Half-Life Formula | Concentration Dependence |
|-------|------------------|------------------------|
| Zero | [A]_0 / 2k | Decreases with time (shorter half-lives as [A] drops) |
| First | **0.693 / k** | **Independent of concentration** |
| Second | 1 / (k[A]_0) | Increases with time (longer half-lives as [A] drops) |

**The MCAT loves first-order half-life problems.** After n half-lives, the fraction remaining = (1/2)^n.

| Half-Lives | Fraction Remaining | Percent Remaining |
|------------|-------------------|-------------------|
| 1 | 1/2 | 50% |
| 2 | 1/4 | 25% |
| 3 | 1/8 | 12.5% |
| 4 | 1/16 | 6.25% |
| 5 | 1/32 | 3.125% |

**Example:** A drug has a half-life of 4 hours. After 12 hours, what fraction remains? 12/4 = 3 half-lives. (1/2)^3 = 1/8 remaining.

---

### 2.4 Rate-Determining Step

In a multi-step mechanism, the **slowest step** determines the overall rate. The rate law of the overall reaction matches the rate law of the rate-determining step.

**Key rules:**
- The overall rate law is derived from the slow step
- If the slow step involves an intermediate, you must use a prior equilibrium step to substitute it out in terms of reactants
- Catalysts appear in one step and are regenerated in another
- Intermediates are produced in one step and consumed in another -- they never appear in the overall equation

**MCAT application:** They may give you a proposed mechanism and ask if it's consistent with the experimentally observed rate law. Write the rate law from the slow step and check if it matches.

---

### 2.5 Energy Diagrams (Reaction Coordinate Diagrams)

These plot **free energy (y-axis) vs reaction progress (x-axis)** and are extremely high-yield.

**Key features to identify:**
- **Reactants:** Energy level at the start (left)
- **Products:** Energy level at the end (right)
- **Activation energy (Ea):** Height from reactants to the highest transition state. This is the energy barrier.
- **Transition state (activated complex):** The PEAK(s) on the diagram. This is the highest energy, most unstable species. It cannot be isolated.
- **Intermediate:** A VALLEY between two peaks. It's a real (though often unstable) species that exists briefly. It CAN theoretically be isolated, unlike a transition state.
- **deltaG of reaction:** Difference between products and reactants energy levels.

**Exothermic/exergonic profile:** Products lower than reactants (energy released).
**Endothermic/endergonic profile:** Products higher than reactants (energy absorbed).

**Multi-step reactions** have multiple peaks (one for each elementary step). The highest peak corresponds to the rate-determining step (biggest Ea).

**With a catalyst:** The Ea is LOWERED (peaks are shorter), but the energy of reactants and products stays the same. **A catalyst changes the kinetics, not the thermodynamics.** deltaG is unchanged. Keq is unchanged. The reaction just reaches equilibrium faster.

---

### 2.6 Arrhenius Equation

> **k = A * e^(-Ea / RT)**

- **k** = rate constant
- **A** = frequency factor (related to collision orientation)
- **Ea** = activation energy
- **R** = gas constant (8.314 J/mol*K)
- **T** = temperature in Kelvin

**What this tells you:**
- Higher temperature (T up) -- exponent becomes less negative -- k increases -- reaction is **faster**
- Lower activation energy (Ea down) -- exponent becomes less negative -- k increases -- reaction is **faster**
- A catalyst lowers Ea, which increases k

**Two-point form (may be given on the MCAT):**

> ln(k2/k1) = -Ea/R * (1/T2 - 1/T1)

You probably won't need to calculate this, but understand the relationship qualitatively.

**MCAT tip:** The Arrhenius equation explains WHY catalysts speed up reactions (lower Ea) and WHY increasing temperature speeds up reactions (more molecules have enough energy to overcome the barrier). Both effects increase k.

---

### 2.7 Catalysts

**A catalyst speeds up a reaction by lowering the activation energy.** It is not consumed in the overall reaction -- it participates in one step and is regenerated in another.

**What catalysts DO:**
- Lower Ea (provide an alternative reaction pathway)
- Increase the rate constant k
- Speed up BOTH forward and reverse reactions equally
- Help the system reach equilibrium faster

**What catalysts DO NOT do:**
- Change deltaG, deltaH, or deltaS
- Change Keq
- Shift the equilibrium position
- Get consumed in the reaction

**Types:**
- **Homogeneous catalyst:** Same phase as reactants (e.g., H+ in solution catalyzing an aqueous reaction)
- **Heterogeneous catalyst:** Different phase from reactants (e.g., solid metal surface catalyzing a gas-phase reaction -- like a catalytic converter in a car)
- **Enzymes:** Biological catalysts -- proteins that catalyze biochemical reactions (covered in depth in Section 4)

---

## 3. Chemical Equilibrium

### 3.1 The Equilibrium Constant (Keq)

For the reaction: aA + bB <-> cC + dD

> **Keq = [C]^c [D]^d / [A]^a [B]^b**

**Rules:**
- Only include aqueous and gaseous species
- **Pure solids and pure liquids are EXCLUDED** (their concentrations are constant and incorporated into Keq)
- Keq is unitless by convention on the MCAT
- Keq depends ONLY on temperature

| Keq Value | Meaning |
|-----------|---------|
| Keq >> 1 | Products strongly favored (reaction goes nearly to completion) |
| Keq = 1 | Neither favored |
| Keq << 1 | Reactants favored (reaction barely proceeds) |

**Kp vs Kc:** For gas-phase reactions, Kp uses partial pressures instead of concentrations. Kp = Kc(RT)^(delta-n), where delta-n = moles of gaseous products minus moles of gaseous reactants.

---

### 3.2 Reaction Quotient (Q) vs Equilibrium Constant (K)

**Q has the exact same formula as K, but uses CURRENT concentrations instead of equilibrium concentrations.**

| Comparison | Direction of Shift |
|-----------|-------------------|
| **Q < K** | Forward (need more products to reach equilibrium) |
| **Q = K** | At equilibrium (no net change) |
| **Q > K** | Reverse (need more reactants to reach equilibrium) |

**MCAT strategy:** If they give you current concentrations and Keq, calculate Q and compare to K to determine which direction the reaction shifts.

---

### 3.3 Le Chatelier's Principle

When a system at equilibrium is disturbed, it shifts to partially counteract the disturbance.

**Adding reactant:** Shift RIGHT (toward products) -- system consumes the added reactant.
**Removing reactant:** Shift LEFT (toward reactants) -- system replenishes the removed reactant.
**Adding product:** Shift LEFT.
**Removing product:** Shift RIGHT.

**Pressure/Volume changes (gas-phase reactions only):**
- Increase pressure (decrease volume): Shift toward the side with FEWER moles of gas
- Decrease pressure (increase volume): Shift toward the side with MORE moles of gas
- If moles of gas are equal on both sides: NO shift

**Temperature changes:**
- Treat heat as a reactant (endothermic) or product (exothermic)
- Exothermic: A + B -> C + heat. Increasing T shifts LEFT (toward reactants), DECREASES Keq
- Endothermic: A + B + heat -> C. Increasing T shifts RIGHT (toward products), INCREASES Keq
- **Temperature is the ONLY factor that changes the VALUE of Keq**

**Adding a catalyst:** NO shift. Equilibrium is reached faster, but the position doesn't change. Keq is unchanged.

**Adding an inert gas at constant volume:** NO shift (partial pressures don't change). At constant pressure (container expands), it's equivalent to decreasing pressure, so shift toward more moles of gas.

---

### 3.4 Connecting deltaG-standard and Keq

> **deltaG-standard = -RT * ln(Keq)**

This is the bridge between thermodynamics and equilibrium. It's one of the most important equations on the MCAT.

- If Keq > 1: ln(Keq) > 0, so deltaG-standard < 0 (spontaneous under standard conditions)
- If Keq < 1: ln(Keq) < 0, so deltaG-standard > 0 (non-spontaneous under standard conditions)
- If Keq = 1: ln(1) = 0, so deltaG-standard = 0

**Remember:** deltaG-standard tells you about standard conditions. deltaG (without the degree symbol) tells you about actual conditions via deltaG = deltaG-standard + RT*ln(Q).

---

## 4. Enzyme Kinetics

> **This is one of the highest-yield topics on the MCAT. It appears on BOTH Chem/Phys and Bio/Biochem.** You need to know Michaelis-Menten, Lineweaver-Burk, and inhibition types cold.

### 4.1 Enzyme Basics

**Enzymes are biological catalysts** -- they speed up reactions by lowering the activation energy. They are almost always proteins (exception: ribozymes are catalytic RNA).

**Key properties:**
- Lower Ea without changing deltaG
- Not consumed in the reaction
- Highly specific (each enzyme catalyzes a specific reaction or class of reactions)
- Function optimally at specific pH and temperature
- Can be regulated (turned up or down as needed)

#### Lock-and-Key vs Induced Fit Models

- **Lock-and-key:** The substrate fits perfectly into the enzyme's active site, like a key in a lock. The enzyme's shape doesn't change. This is the older, simpler model.
- **Induced fit (current model):** The enzyme's active site changes shape slightly upon substrate binding to achieve optimal fit. The enzyme "molds" around the substrate. This is more accurate and is what the MCAT expects you to know.

#### Cofactors and Coenzymes

Some enzymes need non-protein helpers to function:

- **Cofactors:** Inorganic. Usually metal ions (Zn2+, Mg2+, Fe2+, Cu2+). Tightly bound.
- **Coenzymes:** Organic molecules, often derived from vitamins. Examples: NAD+ (from niacin/B3), FAD (from riboflavin/B2), coenzyme A (from pantothenic acid/B5), TPP (from thiamine/B1).
- **Prosthetic group:** A cofactor or coenzyme that is PERMANENTLY bound to the enzyme (e.g., heme in hemoglobin).
- **Holoenzyme:** Enzyme + cofactor/coenzyme (active form).
- **Apoenzyme:** Enzyme without its cofactor (inactive form).

---

### 4.2 Michaelis-Menten Kinetics

The Michaelis-Menten equation describes the relationship between reaction velocity and substrate concentration for a single-substrate enzyme:

> **V_0 = V_max * [S] / (K_m + [S])**

- **V_0** = initial reaction velocity
- **V_max** = maximum velocity (when ALL enzyme molecules are saturated with substrate)
- **[S]** = substrate concentration
- **K_m** = Michaelis constant = substrate concentration at which V_0 = 1/2 * V_max

**The curve is a rectangular hyperbola:**
- At low [S]: V_0 increases approximately linearly with [S] (first-order kinetics with respect to substrate)
- At high [S]: V_0 plateaus and approaches V_max (zero-order kinetics with respect to substrate -- enzyme is saturated)
- At [S] = K_m: V_0 = V_max / 2

#### Understanding K_m

**K_m is a measure of the enzyme's affinity for its substrate.**

- **Low K_m** = HIGH affinity (the enzyme reaches half-max velocity at a low substrate concentration -- it binds substrate tightly and efficiently)
- **High K_m** = LOW affinity (needs lots of substrate to reach half-max velocity -- weaker binding)

**MCAT memory trick:** K_m and affinity are INVERSELY related. Low K_m = loves the substrate (high affinity). High K_m = doesn't grab it well (low affinity).

**K_m is an intrinsic property** of the enzyme-substrate pair. It doesn't change with enzyme concentration.

#### Understanding V_max

**V_max depends on enzyme concentration:**

> **V_max = k_cat * [E]_total**

- **k_cat** (turnover number) = number of substrate molecules converted to product per enzyme molecule per unit time when fully saturated
- Doubling the enzyme concentration doubles V_max
- V_max is NOT changed by substrate concentration (it's the ceiling)

**Catalytic efficiency** = k_cat / K_m. This ratio measures how efficiently an enzyme converts substrate to product. A "perfect" enzyme (diffusion-limited) has k_cat/K_m around 10^8 to 10^9 M^-1 s^-1.

---

### 4.3 Lineweaver-Burk (Double Reciprocal) Plot

The Michaelis-Menten curve is a hyperbola, which is hard to extract precise values from. The Lineweaver-Burk plot linearizes it by taking the reciprocal of both sides:

> **1/V_0 = (K_m / V_max) * (1/[S]) + 1/V_max**

This is in the form y = mx + b:
- **Y-axis:** 1/V_0
- **X-axis:** 1/[S]
- **Slope:** K_m / V_max
- **Y-intercept:** 1/V_max (so V_max = 1 / y-intercept)
- **X-intercept:** -1/K_m (so K_m = -1 / x-intercept)

#### Lineweaver-Burk Interpretation Guide

```
    1/V_0
     ^
     |          /
     |         / <-- slope = Km/Vmax
     |        /
     |       /
     |      /
     |     /
     |----*-----------> 1/[S]
     |   /
     |  /
     * /
  (y-int = 1/Vmax)
     |
     |
  (-1/Km, 0) = x-intercept
```

**How to read changes from the plot:**
- Y-intercept MOVES UP = V_max DECREASED (since y-int = 1/V_max, bigger y-int means smaller V_max)
- Y-intercept stays same = V_max UNCHANGED
- X-intercept MOVES RIGHT (closer to zero / less negative) = K_m DECREASED
- X-intercept MOVES LEFT (further from zero / more negative) = K_m INCREASED (remember, the x-intercept is at -1/K_m, so a larger K_m means a more negative x-intercept, which is further LEFT)

Wait -- let's be precise about this because it trips people up:
- X-intercept = -1/K_m
- If K_m INCREASES, -1/K_m becomes less negative (closer to zero), so the x-intercept moves RIGHT
- If K_m DECREASES, -1/K_m becomes more negative (further from zero), so the x-intercept moves LEFT

**Correction and clarification for absolute clarity:**
- K_m = 2: x-intercept = -1/2 = -0.5
- K_m = 4: x-intercept = -1/4 = -0.25 (this is to the RIGHT of -0.5)
- So increased K_m = x-intercept moves RIGHT (toward zero)
- Decreased K_m = x-intercept moves LEFT (away from zero)

---

### 4.4 Enzyme Inhibition Types

This is the single most tested enzyme topic. You MUST know all four types and their Lineweaver-Burk signatures.

#### Competitive Inhibition

**Mechanism:** Inhibitor binds to the **active site** (same site as substrate). Competes directly with substrate for binding.

**Effects:**
- **K_m: INCREASES** (apparent K_m goes up -- enzyme appears to have lower affinity because it's harder for substrate to find an open active site)
- **V_max: UNCHANGED** -- if you add enough substrate, you can outcompete the inhibitor and still reach the same V_max
- **Can be overcome by excess substrate: YES**

**Lineweaver-Burk:** Lines intersect at the **Y-INTERCEPT** (same V_max). The inhibited line has a steeper slope and a different x-intercept (x-intercept moves right, since K_m increases and -1/K_m gets closer to zero).

```
    1/V_0
     ^
     |        / Competitive (steeper slope)
     |       /   / No inhibitor
     |      /   /
     |     /   /
     |    /   /
     |   /   /
     |--*---*---------> 1/[S]
     |  |  /
     | / /
     *  <- same y-intercept (same Vmax)
```

**Classic example:** Statins competitively inhibit HMG-CoA reductase. Methotrexate competitively inhibits dihydrofolate reductase.

#### Noncompetitive Inhibition

**Mechanism:** Inhibitor binds to an **allosteric site** (NOT the active site) on BOTH the free enzyme (E) AND the enzyme-substrate complex (ES) with **equal affinity**.

**Effects:**
- **K_m: UNCHANGED** (substrate can still bind with the same affinity -- the inhibitor doesn't interfere with substrate binding)
- **V_max: DECREASED** (some enzyme molecules are rendered inactive -- even saturating substrate can't restore full activity)
- **Can be overcome by excess substrate: NO**

**Lineweaver-Burk:** Lines intersect at the **X-INTERCEPT** (same K_m). The inhibited line has a higher y-intercept (lower V_max).

```
    1/V_0
     ^
     |      / Noncompetitive (higher y-int)
     |     /
     |    /   / No inhibitor
     |   /   /
     |  /   /
     | /   /
     |/   /
     *---*-----------> 1/[S]
     ^
  same x-intercept (same Km)
```

**Classic example:** Heavy metal poisoning (Pb, Hg) -- metals bind to sulfhydryl groups away from the active site, distorting enzyme shape.

#### Uncompetitive Inhibition

**Mechanism:** Inhibitor binds ONLY to the **enzyme-substrate complex (ES)** -- NOT to the free enzyme. It essentially locks the substrate onto the enzyme unproductively.

**Effects:**
- **K_m: DECREASED** (this seems counterintuitive -- the enzyme appears to have HIGHER affinity because the inhibitor pulls the equilibrium toward ES by binding it)
- **V_max: DECREASED** (ES-I complex can't form product)
- **Both K_m and V_max decrease by the same factor**
- **Can be overcome by excess substrate: NO** (more substrate = more ES complex = more inhibitor binding)

**Lineweaver-Burk:** **Parallel lines** (same slope, since K_m/V_max ratio is unchanged). The inhibited line is shifted UP and to the LEFT.

```
    1/V_0
     ^
     |     / Uncompetitive (shifted up)
     |    /
     |   /   / No inhibitor
     |  /   /
     | /   /
     |/   /
     |   /
     |  /
     |-/-----------> 1/[S]
     |/
     (parallel lines -- same slope)
```

**MCAT tip:** Uncompetitive inhibition is relatively rare in single-substrate reactions but more common in multi-substrate reactions.

#### Mixed Inhibition

**Mechanism:** Inhibitor binds to an allosteric site on BOTH the free enzyme (E) AND the enzyme-substrate complex (ES), but with **different affinities**. This is the general case -- noncompetitive is a special case of mixed where the affinities are equal.

**Effects:**
- **K_m: CHANGES** (can increase OR decrease depending on relative affinities)
- **V_max: DECREASED** (always decreases)
- **Can be overcome by excess substrate: NO**

If the inhibitor binds E more tightly than ES: K_m INCREASES (acts more like competitive)
If the inhibitor binds ES more tightly than E: K_m DECREASES (acts more like uncompetitive)

**Lineweaver-Burk:** Lines intersect in the **second quadrant** (left of y-axis, neither on x-axis nor y-axis). This distinguishes it from competitive (intersect on y-axis) and noncompetitive (intersect on x-axis).

#### Master Inhibition Summary Table

| Property | Competitive | Noncompetitive | Uncompetitive | Mixed |
|----------|------------|----------------|---------------|-------|
| **Binds to** | Active site | Allosteric (E and ES equally) | ES complex only | Allosteric (E and ES differently) |
| **K_m** | INCREASED | Unchanged | DECREASED | Changed (up or down) |
| **V_max** | Unchanged | DECREASED | DECREASED | DECREASED |
| **Overcome by [S]?** | YES | No | No | No |
| **LB intersection** | Y-axis | X-axis | Parallel lines | Quadrant II |
| **LB slope** | Increased | Increased | Same | Changed |

**Memory trick for Lineweaver-Burk intersections:**
- **C**ompetitive = **C**onstant V_max = intersect at **y-axis** (y-int gives V_max)
- **N**oncompetitive = **N**o change in K_m = intersect at **x-axis** (x-int gives K_m)
- **U**ncompetitive = lines go **U**p in parallel

---

### 4.5 Allosteric Regulation

Allosteric enzymes do NOT follow simple Michaelis-Menten kinetics. Instead of a hyperbolic curve, they show a **sigmoidal (S-shaped)** curve of V_0 vs [S].

**Positive allosteric effectors (activators):**
- Bind to a regulatory site and INCREASE enzyme activity
- Shift the curve to the LEFT (lower apparent K_m -- enzyme needs less substrate)
- Stabilize the R (relaxed, active) state

**Negative allosteric effectors (inhibitors):**
- Bind to a regulatory site and DECREASE enzyme activity
- Shift the curve to the RIGHT (higher apparent K_m -- enzyme needs more substrate)
- Stabilize the T (tense, inactive) state

#### Cooperativity

**Cooperativity** occurs when binding of substrate to one subunit affects binding at other subunits. Hemoglobin is the classic example (though it's a carrier, not an enzyme).

- **Positive cooperativity:** Binding of one substrate molecule makes subsequent binding easier. This creates the sigmoidal curve. Each binding event shifts remaining subunits toward the R state.
- **Negative cooperativity:** Binding of one substrate makes subsequent binding harder. This is rarer.

**Hill coefficient (n):**
- n = 1: No cooperativity (hyperbolic, normal Michaelis-Menten)
- n > 1: Positive cooperativity (sigmoidal)
- n < 1: Negative cooperativity

---

### 4.6 Covalent Modification

Enzymes can be activated or inactivated by covalent attachment of chemical groups.

**Phosphorylation** (most common and most tested):
- **Kinases** ADD phosphate groups (from ATP) -- usually to serine, threonine, or tyrosine residues
- **Phosphatases** REMOVE phosphate groups (hydrolysis)
- Phosphorylation can either activate OR inactivate an enzyme depending on the specific enzyme
- Phosphate groups are large, negatively charged -- they cause conformational changes

**Other modifications:**
- **Acetylation** (e.g., histone modification)
- **Methylation**
- **Ubiquitination** (tags protein for proteasomal degradation)
- **Glycosylation** (adding sugar -- important for secreted proteins)

**MCAT example:** Glycogen phosphorylase is ACTIVATED by phosphorylation (adds phosphate = breaks down glycogen). Glycogen synthase is INACTIVATED by phosphorylation (adds phosphate = stops building glycogen). This makes metabolic sense -- epinephrine triggers kinase cascades that simultaneously activate glycogen breakdown and inhibit glycogen synthesis.

---

### 4.7 Zymogens (Proenzymes)

**Zymogens** are inactive enzyme precursors that are activated by proteolytic cleavage (cutting off a portion of the polypeptide). This is IRREVERSIBLE activation.

**Why use zymogens?** Safety. Digestive enzymes and clotting factors would damage their own tissues if activated prematurely.

| Zymogen | Active Enzyme | Location/Function |
|---------|--------------|-------------------|
| Pepsinogen | **Pepsin** | Stomach; activated by HCl (low pH) |
| Trypsinogen | **Trypsin** | Small intestine; activated by enterokinase |
| Chymotrypsinogen | **Chymotrypsin** | Small intestine; activated by trypsin |
| Proelastase | **Elastase** | Small intestine; activated by trypsin |
| Procarboxypeptidase | **Carboxypeptidase** | Small intestine; activated by trypsin |

**Key fact:** Trypsin activates most other pancreatic zymogens AND can activate trypsinogen (autocatalysis). Enterokinase (enteropeptidase) is the initial trigger that activates the first trypsinogen molecule.

**Blood clotting cascade** also uses zymogens (clotting factors are activated sequentially). This amplification mechanism allows a small signal to produce a large response.

---

### 4.8 Feedback Inhibition

In metabolic pathways, the **end product** often inhibits an enzyme early in the pathway (usually the first committed step). This is **negative feedback** -- prevents overproduction.

**Example:** In cholesterol synthesis, cholesterol inhibits HMG-CoA reductase (the rate-limiting enzyme). This is the same enzyme that statins target competitively.

**Feedforward activation:** A metabolite early in a pathway activates an enzyme later in the pathway. Example: fructose-1,6-bisphosphate activates pyruvate kinase (PFK-1 product activates a downstream glycolysis enzyme).

---

## 5. Bioenergetics

### 5.1 ATP: The Energy Currency

**ATP (adenosine triphosphate)** stores and transfers energy in biological systems.

**Structure:** Adenine (base) + ribose (sugar) + three phosphate groups linked by phosphoanhydride bonds.

**ATP hydrolysis:**

> ATP + H_2O -> ADP + P_i    deltaG = approximately -30.5 kJ/mol (-7.3 kcal/mol)

**Why is ATP hydrolysis so exergonic?**
1. **Charge repulsion relief:** Three negatively charged phosphate groups are crowded together. Removing one relieves electrostatic repulsion.
2. **Resonance stabilization:** The products (ADP and P_i) have MORE resonance structures than ATP, making them more stable.
3. **Hydration stabilization:** The products are better hydrated (stabilized by water) than ATP.
4. **Entropy increase:** One molecule becomes two, increasing disorder.

**MCAT note:** ATP is NOT "high-energy" in absolute terms. It has an intermediate energy of hydrolysis, which makes it useful as an energy SHUTTLE. It can accept energy from higher-energy compounds (like phosphoenolpyruvate, 1,3-BPG) and donate energy to drive lower-energy reactions.

**Phosphoryl group transfer potential:** PEP > 1,3-BPG > ATP > glucose-6-phosphate. Compounds with HIGHER transfer potential can drive phosphorylation of compounds with LOWER transfer potential.

---

### 5.2 Coupled Reactions

An energetically unfavorable reaction (deltaG > 0) can be driven forward by coupling it to an energetically favorable reaction (like ATP hydrolysis) so that the NET deltaG is negative.

**How to calculate:** Just ADD the deltaG values.

**Example:**
- Glutamate + NH_3 -> Glutamine     deltaG = +14.2 kJ/mol (unfavorable alone)
- ATP -> ADP + P_i                    deltaG = -30.5 kJ/mol
- **Coupled:** Glutamate + NH_3 + ATP -> Glutamine + ADP + P_i    deltaG = -16.3 kJ/mol (favorable!)

**MCAT principle:** Most biosynthetic (anabolic) reactions are endergonic and are driven by coupling to ATP hydrolysis. This is how cells build complex molecules -- they pay the energy cost with ATP.

---

### 5.3 Electron Carriers: NAD+ and FAD

These are coenzymes that carry high-energy electrons between metabolic reactions.

#### NAD+ / NADH

- **NAD+** is the oxidized form (accepts electrons)
- **NADH** is the reduced form (carries electrons)
- NAD+ + 2H -> NADH + H+ (accepts 2 electrons and 1 proton; the hydride ion :H-)
- Derived from niacin (vitamin B3)
- Operates in: glycolysis, pyruvate dehydrogenase, TCA cycle, beta-oxidation, ETC
- Each NADH yields approximately **2.5 ATP** via oxidative phosphorylation (ETC)

#### FAD / FADH2

- **FAD** is the oxidized form
- **FADH2** is the reduced form
- FAD + 2H -> FADH2 (accepts 2 electrons and 2 protons)
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

---

### 5.4 Chemiosmotic Theory (Mitchell Hypothesis)

**Peter Mitchell's chemiosmotic theory** explains how the energy from electron transport is used to make ATP.

**The key idea:** The electron transport chain pumps protons (H+) from the mitochondrial matrix to the intermembrane space, creating a **proton-motive force** (electrochemical gradient). This gradient has two components:
1. **Chemical gradient** (concentration difference -- more H+ in intermembrane space)
2. **Electrical gradient** (charge difference -- intermembrane space is more positive)

**ATP synthase** (Complex V) is a molecular turbine. Protons flow back DOWN their gradient through ATP synthase, and this flow drives the mechanical rotation that catalyzes:

> ADP + P_i -> ATP

**Key points for the MCAT:**
- The inner mitochondrial membrane must be INTACT for oxidative phosphorylation (the gradient must be maintained)
- **Uncouplers** (e.g., 2,4-DNP, thermogenin/UCP1 in brown fat) dissipate the proton gradient by allowing H+ to cross the membrane without going through ATP synthase. ETC runs but ATP is NOT made. Energy is released as HEAT.
- **Oligomycin** directly blocks ATP synthase. Proton gradient builds up, which also slows ETC (no place for protons to go).
- **Cyanide and CO** block Complex IV. ETC stops entirely. No gradient, no ATP.

**Stoichiometry (approximate):**
- 1 NADH -> ~10 H+ pumped -> ~2.5 ATP
- 1 FADH2 -> ~6 H+ pumped -> ~1.5 ATP
- ~4 H+ needed per ATP synthesized (3 through ATP synthase + 1 for phosphate transport)
- Total from 1 glucose (aerobic): ~30-32 ATP

---

## High-Yield Summary: What the MCAT Loves to Test

1. **deltaG = deltaH - TdeltaS** -- predicting spontaneity from signs of H and S, temperature dependence
2. **deltaG-standard = -RT*ln(Keq)** -- connecting thermodynamics to equilibrium
3. **Hess's law calculations** -- combining reactions to find deltaH
4. **First-order half-life** -- t_1/2 = 0.693/k, fraction remaining after n half-lives
5. **Rate law determination** from method of initial rates
6. **Energy diagram interpretation** -- Ea, transition state vs intermediate, catalyst effects
7. **Le Chatelier's principle** -- especially temperature effects on Keq
8. **Michaelis-Menten** -- what K_m and V_max mean, how they change with inhibitors
9. **Lineweaver-Burk plots** -- identifying inhibition type from the plot
10. **Competitive vs noncompetitive vs uncompetitive inhibition** -- this gets tested repeatedly
11. **ATP coupling** -- adding deltaG values to determine if coupled reaction is spontaneous
12. **Zymogens** -- know the pancreatic enzyme activation cascade

---

## Quick-Reference Equation Sheet

| Equation | Use |
|----------|-----|
| deltaG = deltaH - TdeltaS | Spontaneity from enthalpy and entropy |
| deltaG-standard = -RT ln(Keq) | Free energy from equilibrium constant |
| deltaG = deltaG-standard + RT ln(Q) | Free energy under non-standard conditions |
| q = mc deltaT | Calorimetry |
| deltaH = bonds broken - bonds formed | Enthalpy from bond energies |
| Rate = k[A]^n[B]^m | Rate law |
| ln[A] = ln[A]_0 - kt | First-order integrated rate law |
| t_1/2 = 0.693 / k | First-order half-life |
| k = Ae^(-Ea/RT) | Arrhenius equation |
| V_0 = V_max[S] / (K_m + [S]) | Michaelis-Menten |
| 1/V_0 = (K_m/V_max)(1/[S]) + 1/V_max | Lineweaver-Burk |
| V_max = k_cat [E]_total | Max velocity from turnover number |
