# CP Gen Chem Chapter 5 — Chemical Kinetics

Scope: Rate laws; reaction order; method of initial rates; integrated rate laws (zero/first/second order); half-life; rate-determining step; energy diagrams; Arrhenius equation; catalysts.

**Section:** Chemical/Physical (CP)
**Book:** Kaplan General Chemistry — Chapter 5
**AAMC FC mapping:** FC5E (kinetics portion)
**Yield:** HIGH — first-order half-life and rate-law determination from initial-rates tables appear on nearly every exam.

> Note: Enzyme kinetics (Michaelis-Menten, Lineweaver-Burk, inhibition types) lives in `research/Biochemistry/Ch02_Enzymes.md` — cross-load when the topic involves biological catalysts.

---

## 1. Rate Laws

The rate of a reaction tells you how fast reactants are consumed or products are formed.

> **Rate = k[A]^n[B]^m**

- **k** = rate constant (units depend on overall order)
- **n** = order with respect to A
- **m** = order with respect to B
- **n + m** = overall reaction order

**Reaction order is determined EXPERIMENTALLY, not from stoichiometry.** This is a common MCAT misconception. The balanced equation tells you nothing about the rate law unless it's an elementary step.

### Method of Initial Rates

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

### Units of k by Reaction Order

| Overall Order | Units of k |
|--------------|------------|
| 0 | M/s (or mol L^-1 s^-1) |
| 1 | s^-1 (or 1/s) |
| 2 | M^-1 s^-1 (or L mol^-1 s^-1) |

**MCAT shortcut:** If they give you units of k, you can determine the overall order without any other information.

---

## 2. Integrated Rate Laws

These relate concentration to time and are used to determine order from a single experiment's data.

### Zero Order

> **[A] = [A]_0 - kt**

- Plot **[A] vs t** -- gives a **straight line** (slope = -k)
- Half-life: t_1/2 = [A]_0 / (2k) -- depends on initial concentration
- Rate is constant regardless of concentration

### First Order

> **ln[A] = ln[A]_0 - kt**

- Plot **ln[A] vs t** -- gives a **straight line** (slope = -k)
- Half-life: **t_1/2 = 0.693 / k** -- INDEPENDENT of concentration
- This is the only order with a constant half-life
- Radioactive decay follows first-order kinetics

### Second Order

> **1/[A] = 1/[A]_0 + kt**

- Plot **1/[A] vs t** -- gives a **straight line** (slope = +k)
- Half-life: t_1/2 = 1 / (k[A]_0) -- depends on initial concentration

**MCAT strategy for "which order" questions:** They'll give you data and ask you to identify the order. Check which plot gives a straight line:
- [A] vs t linear = zero order
- ln[A] vs t linear = first order
- 1/[A] vs t linear = second order

---

## 3. Half-Life

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

## 4. Rate-Determining Step

In a multi-step mechanism, the **slowest step** determines the overall rate. The rate law of the overall reaction matches the rate law of the rate-determining step.

**Key rules:**
- The overall rate law is derived from the slow step
- If the slow step involves an intermediate, you must use a prior equilibrium step to substitute it out in terms of reactants
- Catalysts appear in one step and are regenerated in another
- Intermediates are produced in one step and consumed in another -- they never appear in the overall equation

**MCAT application:** They may give you a proposed mechanism and ask if it's consistent with the experimentally observed rate law. Write the rate law from the slow step and check if it matches.

---

## 5. Energy Diagrams (Reaction Coordinate Diagrams)

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

## 6. Arrhenius Equation

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

## 7. Catalysts

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
- **Enzymes:** Biological catalysts -- proteins that catalyze biochemical reactions (see `BB_Ch02_Enzymes.md`).

---

## High-Yield Takeaways

1. **Rate law must come from data**, not stoichiometry (unless elementary step).
2. **Initial rates method:** double a concentration, see what rate does — that's your order.
3. **First-order half-life is constant** (t_1/2 = 0.693/k); zero and second order half-lives depend on [A].
4. **Catalyst lowers Ea but not ΔG, ΔH, or Keq.** Equal effect on forward and reverse.
5. **Energy diagrams:** transition state = peak (cannot isolate); intermediate = valley (can isolate).
6. **Arrhenius:** higher T or lower Ea → bigger k.

---

→ Equilibrium: `CP_GC_Ch06_Equilibrium.md`
→ Thermochemistry & ΔG: `CP_GC_Ch07_Thermochemistry.md`
→ Enzyme kinetics (Michaelis-Menten, Lineweaver-Burk): `BB_Ch02_Enzymes.md`
