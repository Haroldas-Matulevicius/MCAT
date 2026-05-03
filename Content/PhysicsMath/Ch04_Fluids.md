# CP — Physics Ch 4: Fluids

Kaplan Physics Ch 4 | FC4B

> Gas content (ideal gas law, KMT, Dalton's law, real gases) → research/GenChem/Ch08_Gas_Phase.md
> Gas exchange (Boyle's law in lungs, partial pressures) → research/Biology/Ch06_Respiratory.md

---

FLUID STATICS:
- Density: ρ = m/V (water = 1000 kg/m³ = 1 g/mL)
- Specific gravity: SG = ρ_substance/ρ_water (dimensionless; SG > 1 → sinks)
- Pressure: P = F/A (Pa = N/m²)
  - 1 atm = 101,325 Pa = 760 mmHg
  - Absolute = gauge + atmospheric
- Hydrostatic pressure: P = P₀ + ρgh (depends only on depth, not container shape)
  - Every ~10 m water depth ≈ +1 atm
- Pascal's law: pressure transmitted equally to all points in enclosed fluid
  - Hydraulics: F₁/A₁ = F₂/A₂ | volume conserved: A₁d₁ = A₂d₂
- Archimedes' principle: F_b = ρ_fluid · V_displaced · g
  - Float if ρ_object < ρ_fluid; V_submerged/V_total = ρ_object/ρ_fluid
  - Apparent weight = mg − F_b
  - Ice melting in full glass: water level stays same (floating ice displaces its own mass in water)

FLUID DYNAMICS:
- Continuity equation: A₁v₁ = A₂v₂ (Q = Av = constant for incompressible fluid)
  - Capillaries slow despite tiny size: total cross-sectional area of all capillaries >> aorta
- Bernoulli: P + ½ρv² + ρgh = constant
  - Fast flow = LOW pressure (counterintuitive; most common conceptual error)
  - Aneurysm: area↑ → v↓ → P↑ → further dilation (dangerous positive feedback)
  - Venturi: narrowing → v↑ → P↓ (atomizers, sprayers)
  - Airplane wings: faster over top → lower pressure on top → lift
- Poiseuille's law: Q = πr⁴ΔP/(8ηL) → flow ∝ r⁴
  - r × 2 → Q × 16 | r × ½ → Q × 1/16
  - Small vasoconstriction → huge flow change (body's pressure control mechanism)
  - Resistance: R = 8ηL/(πr⁴) → Q = ΔP/R (analogous to Ohm's law)
- Viscosity: internal friction; decreases with temperature
  - Polycythemia (↑hematocrit) → ↑viscosity → ↑resistance → heart works harder
- Reynolds number: Re = ρvD/η
  - Re < 2000: laminar | Re > 4000: turbulent
  - Turbulence → audible sounds (Korotkoff sounds, heart murmurs)

SURFACE PHENOMENA:
- Surface tension: cohesive forces at liquid surface; N/m; water = high (H-bonds)
- Surfactants reduce surface tension (pulmonary surfactant prevents alveolar collapse)
- Pulmonary surfactant: type II pneumocytes; Laplace law P = 2T/r; surfactant prevents small alveoli from collapsing; absence → NRDS in premature infants
- Capillary action: adhesive > cohesive → concave meniscus (water); cohesive > adhesive → convex (mercury)

STARLING FORCES (Kaplan gap):
- Capillary hydrostatic (P_c): pushes fluid OUT (arterial end ~35 mmHg → drops to ~15 mmHg venous)
- Capillary oncotic (π_c): pulls fluid IN (~26 mmHg, albumin-driven, constant along capillary)
- NFP = (P_c − P_i) − (π_c − π_i)
  - Arterial end: +9 mmHg → filtration out (nutrients to tissue)
  - Venous end: −11 mmHg → reabsorption in
  - ~85% reabsorbed; ~15% via lymphatics
- Edema causes:
  - ↑P_c: heart failure, venous congestion
  - ↓π_c: low albumin (liver disease, nephrotic syndrome, kwashiorkor)
  - ↑capillary permeability: inflammation, burns
  - Lymphatic blockage: surgery, elephantiasis

KEY TRAPS:
- Fast flow = LOW pressure (Bernoulli) — most common error
- r⁴ in Poiseuille: halving radius drops flow 16×, not 2×
- Individual capillary area tiny, but TOTAL area of all capillaries is enormous → slow flow
- Oncotic pressure (albumin) is why fluid returns — don't focus only on hydrostatic

Kaplan: Physics Ch 4
→ Deep dive: research/PhysicsMath/Ch04_Fluids.md
