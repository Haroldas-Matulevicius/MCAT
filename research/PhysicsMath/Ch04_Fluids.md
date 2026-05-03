# Physics & Math Chapter 4 — Fluids

Scope: Characteristics of fluids and solids; hydrostatics (density, pressure, Pascal's law, Archimedes' principle); fluid dynamics (continuity, Bernoulli, Poiseuille, viscosity, Reynolds number); surface phenomena; fluids in physiology (Starling forces, blood flow).

**Section:** Chemical/Physical (CP) — Physics & Math
**Book:** Kaplan Physics and Math Strategies 2024 — Chapter 4
**AAMC FC mapping:** FC4B (Fluids and solids)
**Yield:** Very high. Fluids is one of the most tested physics topics. Bernoulli, Poiseuille (r⁴ dependence), and Starling forces are near-guaranteed.

> **Note on gas content:** Ideal gas law, PV = nRT, KMT, Dalton's law, and real gases are NOT in this chapter. That content belongs in `research/GenChem/Ch08_Gas_Phase.md`. The gas law material that was in the legacy Fluids.md has been pruned here. Cross-reference Gen Chem Ch 8 for all gas-phase physics.

> **Cross-reference for pulmonary gas exchange:** Gas exchange in the lungs (Boyle's law for breathing mechanics, partial pressures, alveolar gas exchange) → `research/Biology/Ch06_Respiratory.md` + `research/GenChem/Ch08_Gas_Phase.md`.

---

## 1. Fluid Statics

### Density and Specific Gravity

**Density (ρ)** = mass per unit volume:

**ρ = m/V** (units: kg/m³)

Key densities to know:
- Water: **1000 kg/m³** = 1 g/mL = 1 g/cm³
- Blood: ~1060 kg/m³ (slightly denser than water)
- Air: ~1.2 kg/m³ at sea level

**Specific gravity (SG)** = ρ_substance / ρ_water

Since ρ_water = 1 g/cm³, SG is numerically equal to density in g/cm³ but is **dimensionless**.
- SG > 1 → sinks in water
- SG < 1 → floats

**MCAT tip:** "Specific gravity = 0.8" → density = 0.8 g/cm³ = 800 kg/m³. No calculation needed.

### Pressure Fundamentals

**P = F/A** (units: Pa = N/m²)

Key conversions:
- 1 atm = 101,325 Pa ≈ 10⁵ Pa
- 1 atm = 760 mmHg = 760 torr

**Gauge pressure vs absolute pressure:**
- Absolute = total pressure including atmospheric
- Gauge = pressure above atmospheric (what tire gauges read)
- **P_absolute = P_gauge + P_atm**

### Hydrostatic Pressure

Pressure at depth h in a static fluid:

**P = P_surface + ρgh**

**Critical concept: Pressure depends ONLY on depth, not on the shape or volume of the container.** (Hydrostatic paradox.) A narrow tube and a wide lake at the same depth have the same hydrostatic pressure.

**Worked approach:**
Diver 15 m below freshwater lake surface:
P = 10⁵ + (1000)(10)(15) = 10⁵ + 1.5×10⁵ = 2.5×10⁵ Pa = 2.5 atm

Quick rule: every ~10 m of water depth adds ~1 atm.

### Pascal's Law

> **Pressure applied to an enclosed fluid is transmitted undiminished to every point in the fluid and to the walls of the container.**

Hydraulic systems: **F₁/A₁ = F₂/A₂**

Small force on small piston → same pressure as large force on large piston. Trade force for distance. Work in = Work out (ideal).

**Example:** Small piston area 0.01 m², large piston area 0.5 m². Apply 100 N to small piston.
P = 100/0.01 = 10,000 Pa → F₂ = 10,000 × 0.5 = 5,000 N. MA = 50×.
Conservation of volume: A₁d₁ = A₂d₂ → large piston moves 1/50th the distance.

### Archimedes' Principle

> **The buoyant force equals the weight of the fluid displaced.**

**F_b = ρ_fluid · V_displaced · g**

**Float or sink:**
1. Compare ρ_object to ρ_fluid.
2. ρ_object < ρ_fluid → floats. ρ_object > ρ_fluid → sinks. Equal → neutrally buoyant.

**For floating objects:** V_submerged/V_total = ρ_object/ρ_fluid

Ice (SG ≈ 0.92) floating in water: 92% submerged, 8% above water.

**Apparent weight** = actual weight − buoyant force = mg − ρ_fluid · V_object · g

**Classic MCAT question:** Ice cube melts in a full glass of water — does it overflow?
Answer: No. Floating ice displaces exactly its own mass in water. When it melts, it produces the same volume of water it was displacing. Water level stays the same.

---

## 2. Fluid Dynamics

### Continuity Equation (Conservation of Mass)

For **incompressible** fluid flowing through a pipe:

**A₁v₁ = A₂v₂** (volume flow rate Q = Av is constant)

When a pipe narrows, velocity increases. When it widens, velocity decreases.

**Biological connection:** Blood flows slowly through capillaries because the **total cross-sectional area** of all capillaries combined is enormous (~4500 cm²) compared to the aorta (~2.5 cm²). Total A↑ → v↓. Slow flow allows time for gas and nutrient exchange.

**Common trap:** Students confuse individual vessel area with total cross-sectional area. One capillary is tiny, but billions in parallel = massive total area.

### Bernoulli's Equation

For **ideal fluid** (incompressible, non-viscous, steady, laminar flow):

**P + ½ρv² + ρgh = constant**

Energy per unit volume: P = pressure energy, ½ρv² = kinetic energy density, ρgh = gravitational PE density.

**Core trade-off: where velocity is high, pressure is low.** (And vice versa.)

**Applications you must know:**

**Venturi effect:** Pipe narrows → velocity increases → pressure drops. Basis of atomizers, sprayers, carburetors.

**Airplane wings (lift):** Air faster over curved top → lower pressure on top → net upward force.

**Aneurysm:** Blood vessel bulges (larger area) → by continuity, velocity decreases → by Bernoulli, pressure increases → further wall stretching (dangerous positive feedback).

**Atherosclerotic plaque (stenosis):** Narrowed lumen → increased velocity → decreased lateral pressure (may reduce turbulence locally, but downstream complications).

**Worked approach:**
Water in horizontal pipe. Point 1: diameter 4 cm, P = 200 kPa, v = 1 m/s. Point 2: diameter 2 cm.
- Continuity: A₁/A₂ = (r₁/r₂)² = 4 → v₂ = 4 m/s
- Bernoulli (horizontal, h terms cancel): P₁ + ½ρv₁² = P₂ + ½ρv₂²
- 200,000 + 500 = P₂ + 8,000 → P₂ = 192,500 Pa = 192.5 kPa

### Poiseuille's Law

For **viscous, laminar flow** through a cylindrical tube:

**Q = (π · r⁴ · ΔP) / (8 · η · L)**

Where Q = flow rate, r = radius, ΔP = pressure difference, η = viscosity, L = length.

**The r⁴ dependence is the single most important thing about this equation.**

| Change | Effect on Q |
|--------|-------------|
| r × 2 | Q × 16 |
| r × ½ | Q × 1/16 |
| ΔP × 2 | Q × 2 |
| η × 2 | Q × ½ |
| L × 2 | Q × ½ |

**Biological connection — vasoconstriction/vasodilation:**
A 20% decrease in vessel radius reduces blood flow by ~60% (0.8⁴ = 0.41). The body uses tiny radius changes to precisely control organ blood distribution.

**Resistance form:** R = 8ηL/(πr⁴) → Q = ΔP/R (analogous to Ohm's law: I = V/R).

**MCAT tip:** Almost never need to calculate Poiseuille's numerically. Know proportional reasoning — r⁴ is king.

**Polycythemia** (high hematocrit) → increases blood viscosity → increases resistance → heart works harder.
**Anemia** → decreases viscosity → decreases resistance.

### Viscosity

**Viscosity (η)** = internal resistance of fluid to flow ("thickness").

- Water: low viscosity
- Blood: moderate (depends on hematocrit, temperature, vessel diameter)
- Honey: high viscosity

Viscosity decreases with increasing temperature (molecules move more freely). Blood viscosity also depends on hematocrit — more RBCs = more viscous.

### Reynolds Number and Flow Types

**Re = (ρvD)/η**

Where D = diameter of tube.

- Re < 2000: **laminar flow** (smooth, orderly, parallel layers)
- Re > 4000: **turbulent flow** (chaotic, eddies, mixing)
- 2000–4000: transitional

**Turbulent flow requires more energy.** It also produces **audible sounds** — heard with a stethoscope during blood pressure measurement (Korotkoff sounds) and in heart murmurs.

Factors promoting turbulence: high velocity, large diameter, low viscosity, high density.

**MCAT tip:** Bernoulli and Poiseuille both assume laminar flow.

---

## 3. Surface Phenomena

### Surface Tension

**Surface tension** results from **cohesive forces** (attraction between like molecules) at the liquid surface. Molecules at the surface are pulled inward → creates a "skin" that minimizes surface area.

- Units: N/m or J/m²
- Water has high surface tension due to H-bonding.
- **Surfactants** (soap, pulmonary surfactant) reduce surface tension.

**Biological connection — pulmonary surfactant:**
Produced by type II alveolar cells (type II pneumocytes). Reduces surface tension in alveoli.

Without surfactant, **Laplace's law** (P = 2T/r) predicts that smaller alveoli (smaller r) would have higher inward pressure → collapse (atelectasis). Surfactant preferentially reduces tension more in smaller alveoli, equalizing pressures and preventing collapse.

**Premature infants** lack sufficient surfactant → **neonatal respiratory distress syndrome** (NRDS).

### Capillary Action

**Capillary action** = liquid rises or falls in a narrow tube due to:
- **Adhesive forces:** liquid to tube wall
- **Cohesive forces:** liquid to liquid

If adhesive > cohesive: liquid climbs, **concave meniscus** (water in glass).
If cohesive > adhesive: liquid depressed, **convex meniscus** (mercury in glass).

Height of rise increases with: stronger adhesion, smaller tube radius (inversely proportional to r), lower fluid density.

**MCAT tip:** Read meniscus at the **bottom of concave** (water) or **top of convex** (mercury).

---

## 4. Fluids in Physiology — Starling Forces

**This is a known Kaplan gap — the MCAT tests it.**

### The Four Starling Forces

Fluid movement across capillary walls is governed by four pressures:

| Force | Symbol | Direction | Definition |
|-------|--------|-----------|------------|
| **Capillary hydrostatic pressure** | P_c | Out of capillary | Blood pressure inside capillary |
| **Interstitial hydrostatic pressure** | P_i | Into capillary | Pressure of interstitial fluid (~0 or slightly negative) |
| **Capillary oncotic pressure** | π_c | Into capillary | Osmotic pressure from plasma proteins (mainly **albumin**) |
| **Interstitial oncotic pressure** | π_i | Out of capillary | Osmotic pressure from interstitial proteins (usually low) |

**Net filtration pressure (NFP):**

**NFP = (P_c − P_i) − (π_c − π_i)**

Positive NFP → fluid leaves capillary. Negative NFP → fluid returns.

### What Happens Along a Capillary

**Arterial end:**
- P_c ~ 35 mmHg (just came from arteriole)
- π_c ~ 26 mmHg (constant — protein concentration doesn't change much)
- NFP = 35 − 26 = +9 mmHg → net filtration OUT. Fluid and nutrients leave capillary.

**Venous end:**
- P_c has dropped to ~15 mmHg (due to resistance along capillary)
- π_c still ~26 mmHg
- NFP = 15 − 26 = −11 mmHg → net reabsorption IN. Fluid returns.

~85% of filtered fluid reabsorbs at venous end. Remaining ~15% collected by **lymphatic system**.

### Edema (Fluid Accumulation in Tissues)

Edema = excess interstitial fluid. Caused by any disruption increasing filtration or decreasing reabsorption:

| Cause | Mechanism | Clinical Example |
|-------|-----------|-----------------|
| Increased P_c | More fluid pushed out | Heart failure (venous congestion) |
| Decreased π_c | Less fluid pulled back | Liver disease (low albumin), nephrotic syndrome (albumin lost in urine), malnutrition (kwashiorkor) |
| Increased capillary permeability | Proteins leak out, raising π_i | Inflammation, burns, allergic reactions |
| Lymphatic blockage | Filtered fluid can't return | Lymph node removal, elephantiasis |

**MCAT key:** "Low albumin = edema." Albumin is the primary determinant of oncotic pressure.

---

## MCAT Strategy Summary

### Pattern Recognition

| Trigger | Action |
|---------|--------|
| "Pipe narrows" | Continuity: v increases. Bernoulli: pressure decreases. |
| "Aneurysm / vessel bulges" | Area increases → v decreases → pressure increases → dangerous positive feedback. |
| "Blood flow question with radius change" | Poiseuille: Q ∝ r⁴. Halve radius → flow drops 16×. |
| "Object submerged" | F_b = ρ_fluid · V_displaced · g. Check float/sink by density comparison. |
| "Patient with low albumin" | Decreased oncotic pressure → decreased reabsorption → edema. |
| "Korotkoff sounds / heart murmur" | Turbulent flow produces audible sounds. |
| "Capillaries slow despite small size" | Total cross-sectional area is enormous → continuity → slow flow. |

### Common Traps

1. **Bernoulli paradox:** Fast-moving fluid has LOW pressure, not high. Students expect the opposite.
2. **r⁴ in Poiseuille:** Halving radius drops flow to 1/16, not 1/2.
3. **Individual vs total cross-section:** One capillary is tiny, but billions in parallel create huge total area.
4. **Gauge vs absolute pressure:** Depths → usually absolute pressure. Tire gauges → gauge pressure.
5. **Oncotic pressure in Starling:** Don't focus only on hydrostatic. Albumin is why fluid comes back.

### Quick Reference

**ρ = m/V | P = F/A | P = P₀ + ρgh**
**F_b = ρ_fluid · V_disp · g | A₁v₁ = A₂v₂**
**P + ½ρv² + ρgh = const (Bernoulli)**
**Q = πr⁴ΔP/(8ηL) → Q ∝ r⁴ (Poiseuille)**
**NFP = (P_c − P_i) − (π_c − π_i) (Starling)**
