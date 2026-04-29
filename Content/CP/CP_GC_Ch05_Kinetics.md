# CP Gen Chem Chapter 5 — Kinetics

Scope: Rate laws; reaction order; integrated rate laws; half-life; rate-determining step; energy diagrams; Arrhenius; catalysts.

AAMC FC mapping: FC5E (kinetics)

Kaplan: General Chemistry Ch 5

Note: Enzyme kinetics (Michaelis-Menten, Lineweaver-Burk, inhibition) → `BB_Ch02_Enzymes.md`

---

RATE LAWS:
- Rate = k[A]^n[B]^m
- Order determined EXPERIMENTALLY, not from stoichiometry
- Method of initial rates: double [reactant], see rate change → identify order
  - x2 [A], rate same → 0 order
  - x2 [A], rate x2 → 1st order
  - x2 [A], rate x4 → 2nd order
- Units of k: 0th = M/s; 1st = 1/s; 2nd = M^-1 s^-1

INTEGRATED RATE LAWS (linearization tool):
- 0 order: [A] = [A]0 - kt; [A] vs t linear; t_1/2 = [A]0/(2k)
- 1st order: ln[A] = ln[A]0 - kt; ln[A] vs t linear; t_1/2 = 0.693/k (CONSTANT)
- 2nd order: 1/[A] = 1/[A]0 + kt; 1/[A] vs t linear; t_1/2 = 1/(k[A]0)

HALF-LIFE:
- Only 1st order is independent of [A]0
- Fraction remaining after n half-lives = (1/2)^n
- Examples: 50% → 1 t1/2; 25% → 2; 12.5% → 3; 6.25% → 4
- Radioactive decay = 1st order

RATE-DETERMINING STEP:
- Slowest step controls overall rate
- Overall rate law = rate law of slow step
- Intermediates: produced + consumed (don't appear in overall eqn)
- Catalysts: appear in one step, regenerated in another

ENERGY DIAGRAMS:
- y = free energy, x = reaction progress
- Ea = height from reactant to highest TS
- Transition state = peak (cannot isolate)
- Intermediate = valley (can isolate, briefly stable)
- ΔG = product energy - reactant energy
- Multi-step: highest peak = rate-determining step
- Catalyst: lowers Ea, doesn't change ΔG/Keq

ARRHENIUS EQUATION:
- k = A·e^(-Ea/RT)
- ↑T → ↑k (faster); ↓Ea → ↑k (faster)
- Two-point: ln(k2/k1) = -Ea/R·(1/T2 - 1/T1)

CATALYSTS:
- Lower Ea, ↑k, alternative pathway
- DOES: speed both forward+reverse, reach equilibrium faster
- DOES NOT: change ΔG, ΔH, ΔS, Keq, equilibrium position
- Homogeneous (same phase) vs heterogeneous (different phase)
- Enzymes = biological catalysts → BB_Ch02

→ Equilibrium → Ch06
→ Thermochemistry → Ch07
→ Enzymes → BB_Ch02_Enzymes.md
