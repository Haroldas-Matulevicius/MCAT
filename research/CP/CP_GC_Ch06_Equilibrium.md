# CP Gen Chem Chapter 6 — Equilibrium

Scope: Equilibrium constant Keq; reaction quotient Q; Le Chatelier's principle; kinetic vs thermodynamic control; ΔG° – Keq relationship.

**Section:** Chemical/Physical (CP)
**Book:** Kaplan General Chemistry — Chapter 6
**AAMC FC mapping:** FC5E (equilibrium portion)
**Yield:** HIGH — Le Chatelier reasoning and Q vs K comparisons appear constantly.

---

## 1. The Equilibrium Constant (Keq)

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

## 2. Reaction Quotient (Q) vs Equilibrium Constant (K)

**Q has the exact same formula as K, but uses CURRENT concentrations instead of equilibrium concentrations.**

| Comparison | Direction of Shift |
|-----------|-------------------|
| **Q < K** | Forward (need more products to reach equilibrium) |
| **Q = K** | At equilibrium (no net change) |
| **Q > K** | Reverse (need more reactants to reach equilibrium) |

**MCAT strategy:** If they give you current concentrations and Keq, calculate Q and compare to K to determine which direction the reaction shifts.

---

## 3. Le Chatelier's Principle

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

## 4. Connecting ΔG° and Keq

> **ΔG° = -RT * ln(Keq)**

This is the bridge between thermodynamics and equilibrium. It's one of the most important equations on the MCAT.

- If Keq > 1: ln(Keq) > 0, so ΔG° < 0 (spontaneous under standard conditions)
- If Keq < 1: ln(Keq) < 0, so ΔG° > 0 (non-spontaneous under standard conditions)
- If Keq = 1: ln(1) = 0, so ΔG° = 0

**Remember:** ΔG° tells you about standard conditions. ΔG (without the degree symbol) tells you about actual conditions via:

> **ΔG = ΔG° + RT * ln(Q)**

- At equilibrium: Q = Keq, so ΔG = 0 (confirms ΔG° = -RT·ln(Keq))
- When Q < Keq: ln(Q) < ln(Keq), so ΔG < ΔG°, reaction proceeds forward
- When Q > Keq: ln(Q) > ln(Keq), reaction proceeds in reverse

---

## 5. Kinetic vs. Thermodynamic Control

A reaction may have multiple possible products. Which one forms depends on conditions:

- **Kinetic control (low T, short time):** Product formed via the lower activation energy path predominates. Often the less stable product. Reactions are essentially irreversible at this T.
- **Thermodynamic control (high T, long time, reversible):** The more stable product (lower ΔG) predominates. The system has time to reach equilibrium, where the more stable product is favored.

**Classic example:** 1,2- vs 1,4-addition to a conjugated diene. At low T (kinetic), 1,2-product dominates (faster). At high T (thermodynamic), 1,4-product dominates (more stable).

**MCAT relevance:** If a passage describes a reaction at low temperature with a particular product, think kinetic control. If high temperature gives a different product, that's thermodynamic control.

---

## High-Yield Takeaways

1. **Pure solids/liquids excluded** from K expression.
2. **Q vs K:** Q < K → forward; Q > K → reverse; Q = K → equilibrium.
3. **Le Chatelier:** add reactant → right; add product → left; pressure ↑ → fewer moles of gas; T changes Keq itself.
4. **Catalyst doesn't shift equilibrium**, only speeds it up.
5. **ΔG° = -RT·ln(Keq)** — the master bridge between thermo and equilibrium.
6. **Kinetic control** = fastest path; **thermodynamic control** = most stable product.

---

→ Kinetics: `CP_GC_Ch05_Kinetics.md`
→ Thermochemistry & ΔG: `CP_GC_Ch07_Thermochemistry.md`
→ Acid-base equilibria: `CP_GC_Ch10_Acids_Bases.md`
→ Solubility (Ksp): `CP_GC_Ch09_Solutions.md`
