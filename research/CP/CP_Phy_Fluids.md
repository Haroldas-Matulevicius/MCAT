# FC4B: Fluids, Gas Movement, and Gas Exchange

**Section:** Chem/Phys (CP)
**Yield:** HIGH -- Fluids is one of the most tested physics topics on the MCAT
**Crossover:** Biology (circulatory system, gas exchange), Gen Chem (gas laws)

---

## 1. Fluid Statics

### Density and Specific Gravity

**Density** (rho) is mass per unit volume:

> **rho = m / V** (units: kg/m^3)

Key densities to know cold:
- Water: **1000 kg/m^3** = 1 g/mL = 1 g/cm^3
- Blood: ~1060 kg/m^3 (slightly denser than water due to dissolved solutes and cells)
- Air: ~1.2 kg/m^3 at sea level

**Specific gravity** (SG) is the ratio of a substance's density to the density of water:

> **SG = rho_substance / rho_water**

Since rho_water = 1 g/cm^3, specific gravity is numerically equal to density in g/cm^3 but is **dimensionless**. An SG > 1 means the substance sinks in water. An SG < 1 means it floats.

**MCAT tip:** When a problem says "specific gravity = 0.8," you can immediately read that as density = 0.8 g/cm^3 = 800 kg/m^3. No calculation needed -- just a unit conversion shortcut.

### Pressure Fundamentals

**Pressure** is force per unit area:

> **P = F / A** (units: Pa = N/m^2)

Key pressure conversions:
- 1 atm = 101,325 Pa ~ 10^5 Pa
- 1 atm = 760 mmHg = 760 torr

**Gauge pressure** vs **absolute pressure:**
- **Absolute pressure** = total pressure at a point, including atmospheric
- **Gauge pressure** = pressure above atmospheric (what a tire gauge reads)
- **P_absolute = P_gauge + P_atm**

A tire at "32 psi" has gauge pressure = 32 psi; absolute pressure = 32 + 14.7 = 46.7 psi.

### Hydrostatic Pressure

The pressure at depth h in a static fluid:

> **P = P_surface + rho * g * h**

Where rho is the fluid density, g = 9.8 m/s^2 (use 10 on the MCAT), and h is the depth below the surface.

**Critical concept: Pressure depends ONLY on depth, not on the shape or volume of the container.** A narrow tube and a wide lake at the same depth have the same hydrostatic pressure. This is sometimes called the "hydrostatic paradox." The reason: pressure in a fluid is transmitted in all directions. The column of fluid directly above the point determines the pressure, regardless of what the container looks like laterally.

**Worked approach -- Hydrostatic pressure:**
> A diver is 15 m below the surface of a freshwater lake. What is the absolute pressure?

- P_surface = 1 atm = 10^5 Pa
- rho_water = 1000 kg/m^3
- P = 10^5 + (1000)(10)(15) = 10^5 + 1.5 x 10^5 = **2.5 x 10^5 Pa = 2.5 atm**

Quick rule: every ~10 m of water depth adds ~1 atm. So 15 m depth = 1 atm (surface) + 1.5 atm (water) = 2.5 atm.

### Pascal's Law

> **Pressure applied to an enclosed fluid is transmitted undiminished to every point in the fluid and to the walls of the container.**

This is the principle behind **hydraulic systems**:

> F1/A1 = F2/A2

A small force on a small piston creates the same pressure as a large force on a large piston. You trade force for distance -- the small piston moves a large distance, the large piston moves a small distance. Work in = Work out (in the ideal case, ignoring friction).

**Worked approach -- Hydraulics:**
> A hydraulic lift has a small piston of area 0.01 m^2 and a large piston of area 0.5 m^2. If you push with 100 N on the small piston, what force is exerted by the large piston?

- P = F1/A1 = 100/0.01 = 10,000 Pa
- F2 = P x A2 = 10,000 x 0.5 = **5,000 N**
- Mechanical advantage = A2/A1 = 50x

**MCAT tip:** If they ask about displacement, remember conservation of volume: A1 * d1 = A2 * d2. The large piston moves 1/50th the distance.

### Archimedes' Principle

> **The buoyant force on a submerged (or partially submerged) object equals the weight of the fluid displaced by that object.**

> **F_buoyant = rho_fluid * V_displaced * g**

**Float or sink decision tree:**
1. Compare **rho_object** to **rho_fluid**
2. If rho_object < rho_fluid: object **floats** (partially submerged)
3. If rho_object > rho_fluid: object **sinks**
4. If rho_object = rho_fluid: object is **neutrally buoyant**

**For floating objects**, the fraction submerged equals the ratio of densities:

> **V_submerged / V_total = rho_object / rho_fluid**

Ice (SG ~ 0.92) floating in water: 92% submerged, 8% above water.

**Apparent weight** = actual weight - buoyant force = mg - rho_fluid * V_object * g

**MCAT tip:** When an object is fully submerged, V_displaced = V_object. When it floats, V_displaced < V_object. The MCAT loves asking about what happens to the water level when an ice cube melts in a glass (answer: it stays the same, because floating ice displaces exactly its own mass in water).

---

## 2. Fluid Dynamics

### Continuity Equation (Conservation of Mass)

For an **incompressible** fluid flowing through a pipe:

> **A1 * v1 = A2 * v2**

Where A is cross-sectional area and v is flow velocity. This says the **volume flow rate** (Q = Av) is constant throughout the pipe.

**When a pipe narrows, velocity increases.** When it widens, velocity decreases.

**Biological connection:** Blood flows slowly through capillaries despite being small vessels because the **total cross-sectional area** of all capillaries combined is enormous -- much larger than the aorta. Total A goes way up, so v goes way down. This is critical: slow flow in capillaries allows time for gas and nutrient exchange.

**Common trap:** Students confuse individual vessel area with total cross-sectional area. One capillary is tiny, but there are billions. Apply continuity to the system as a whole.

### Bernoulli's Equation

For an **ideal fluid** (incompressible, non-viscous, steady, laminar flow):

> **P + 1/2 * rho * v^2 + rho * g * h = constant**

This is really just conservation of energy per unit volume:
- **P** = pressure energy (flow work)
- **1/2 * rho * v^2** = kinetic energy per unit volume
- **rho * g * h** = gravitational potential energy per unit volume

**The core trade-off: where velocity is high, pressure is low (and vice versa).**

This is counterintuitive. Students expect fast-moving fluid to have higher pressure, but it is the opposite. Think of it as an energy budget -- if more energy goes into kinetic (speed), less is available as pressure.

**Applications you need to know:**

**Airplane wings (lift):** Air moves faster over the curved top surface than the flat bottom. Faster flow = lower pressure on top. Net upward pressure difference = lift.

**Venturi effect:** A pipe narrows, velocity increases, pressure drops. This is how a Venturi meter measures flow rate, and how an atomizer/sprayer works.

**Aneurysms:** A blood vessel bulges outward (larger cross-sectional area). By continuity, velocity decreases in the aneurysm. By Bernoulli, pressure increases. Higher pressure further stretches the weakened wall -- a dangerous positive feedback loop.

**Worked approach -- Bernoulli:**
> Water flows through a horizontal pipe. At point 1, the pipe diameter is 4 cm and the pressure is 200 kPa. At point 2, the diameter is 2 cm. What is the pressure at point 2? (rho_water = 1000 kg/m^3, flow speed at point 1 = 1 m/s)

Step 1: Find v2 using continuity.
- A1 * v1 = A2 * v2
- A is proportional to r^2, so A1/A2 = (r1/r2)^2 = (2/1)^2 = 4
- v2 = v1 * (A1/A2) = 1 * 4 = 4 m/s

Step 2: Apply Bernoulli (horizontal pipe, so h terms cancel).
- P1 + 1/2 * rho * v1^2 = P2 + 1/2 * rho * v2^2
- 200,000 + 1/2(1000)(1)^2 = P2 + 1/2(1000)(16)
- 200,000 + 500 = P2 + 8,000
- P2 = 192,500 Pa = **192.5 kPa**

Velocity went up 4x, pressure dropped. Exactly what Bernoulli predicts.

### Poiseuille's Law

For **viscous, laminar flow** through a cylindrical tube:

> **Q = (pi * r^4 * deltaP) / (8 * eta * L)**

Where:
- Q = volume flow rate (m^3/s)
- r = radius of the tube
- deltaP = pressure difference between the two ends
- eta = viscosity of the fluid
- L = length of the tube

**The r^4 dependence is the single most important thing about this equation.** If you halve the radius, flow drops by a factor of 2^4 = 16. If you double the radius, flow increases 16-fold.

**Biological connection -- this is why vasoconstriction and vasodilation are so powerful.** A 20% decrease in vessel radius reduces blood flow by about 60% (0.8^4 = 0.41). The body uses this to precisely control blood distribution to different organs.

**Resistance form:** Vascular resistance R = (8 * eta * L) / (pi * r^4), so Q = deltaP / R (analogous to Ohm's law: I = V/R).

**MCAT tip:** You almost never need to calculate with Poiseuille's law directly. Instead, know proportional reasoning:
- Q is proportional to r^4 (radius has the biggest effect)
- Q is proportional to deltaP (more pressure difference = more flow)
- Q is inversely proportional to eta (more viscous = less flow)
- Q is inversely proportional to L (longer tube = more resistance = less flow)

**Polycythemia** (high hematocrit) increases blood viscosity, increasing vascular resistance and requiring the heart to work harder. **Anemia** decreases viscosity, decreasing resistance.

### Viscosity

**Viscosity** (eta) is a measure of a fluid's internal resistance to flow -- its "thickness."

- Water: low viscosity
- Blood: moderate viscosity (depends on hematocrit, temperature, vessel diameter)
- Honey: high viscosity

Viscosity decreases with increasing temperature (molecules move more freely). Blood viscosity also depends on hematocrit -- more red blood cells = more viscous.

### Reynolds Number and Flow Types

The **Reynolds number** (Re) predicts whether flow is laminar or turbulent:

> **Re = (rho * v * D) / eta**

Where D is the tube diameter.

- **Re < 2000:** laminar flow (smooth, orderly, parallel layers)
- **Re > 4000:** turbulent flow (chaotic, eddies, mixing)
- **2000-4000:** transitional

**Turbulent flow requires more energy** (higher pressure) to maintain the same flow rate. It also produces **audible sounds** -- this is what you hear with a stethoscope during blood pressure measurement (Korotkoff sounds) and in heart murmurs.

**Factors that promote turbulence:**
- High velocity (exercise, aorta)
- Large diameter (aorta, not capillaries)
- Low viscosity (anemia)
- High density

**MCAT tip:** Bernoulli and Poiseuille both assume **laminar flow**. If a question describes turbulent conditions, these equations technically do not apply (though the MCAT rarely pushes on this distinction).

---

## 3. Surface Phenomena

### Surface Tension

**Surface tension** is the result of **cohesive forces** (attraction between like molecules) at the surface of a liquid. Molecules at the surface have no neighboring molecules above them, so they are pulled inward, creating a "skin" that minimizes surface area.

- Surface tension has units of N/m or J/m^2 (force per length or energy per area)
- Water has high surface tension due to hydrogen bonding
- **Surfactants** (like soap or pulmonary surfactant) reduce surface tension by disrupting cohesive forces

**Biological connection:** **Pulmonary surfactant** (produced by type II alveolar cells, also called type II pneumocytes) reduces surface tension in the alveoli. Without it, the alveoli would collapse (atelectasis) because small alveoli would have very high inward pressure (Laplace's law: P = 2T/r -- smaller radius means higher collapsing pressure for the same surface tension). Surfactant preferentially reduces tension more in smaller alveoli, equalizing pressures and preventing collapse. **Premature infants** lack sufficient surfactant -- this causes **neonatal respiratory distress syndrome**.

### Capillary Action

**Capillary action** occurs when a liquid rises (or falls) in a narrow tube due to the interplay of:
- **Adhesive forces:** attraction between the liquid and the tube wall
- **Cohesive forces:** attraction between liquid molecules

If adhesive > cohesive: liquid climbs the wall, forming a **concave meniscus** (e.g., water in glass)
If cohesive > adhesive: liquid is depressed, forming a **convex meniscus** (e.g., mercury in glass)

The height of capillary rise increases with:
- Stronger adhesion
- Smaller tube radius (inversely proportional to r)
- Lower fluid density

**MCAT tip:** When reading a meniscus, always read the volume at the **bottom of the concave meniscus** for water, or the **top of the convex meniscus** for mercury.

---

## 4. Gas Laws

### The Ideal Gas Law

> **PV = nRT**

Where:
- P = pressure (atm or Pa)
- V = volume (L or m^3)
- n = moles of gas
- R = gas constant (0.0821 L*atm/mol*K or 8.314 J/mol*K)
- T = **absolute temperature** (Kelvin, always!)

**MCAT tip:** Every gas law problem requires temperature in Kelvin. If they give Celsius, convert first: K = C + 273. Using Celsius will wreck your answer.

### Individual Gas Laws (Special Cases of PV = nRT)

All of these are just the ideal gas law with certain variables held constant:

| Law | Relationship | Held Constant | Equation |
|-----|-------------|---------------|----------|
| **Boyle's** | P and V are inversely proportional | n, T | P1V1 = P2V2 |
| **Charles's** | V and T are directly proportional | n, P | V1/T1 = V2/T2 |
| **Gay-Lussac's** | P and T are directly proportional | n, V | P1/T1 = P2/T2 |
| **Avogadro's** | V and n are directly proportional | P, T | V1/n1 = V2/n2 |

**At STP** (0 degrees C = 273 K, 1 atm): 1 mole of ideal gas occupies **22.4 L**.

**Worked approach -- Boyle's Law in the lungs:**
> During inhalation, the diaphragm contracts and the thoracic cavity volume increases from 6.0 L to 6.5 L. If the initial intrapulmonary pressure is 760 mmHg, what is the new pressure?

- P1V1 = P2V2
- (760)(6.0) = P2(6.5)
- P2 = 4560/6.5 = **701.5 mmHg**

Pressure dropped below atmospheric (760 mmHg), so air flows IN. This is exactly how breathing works -- Boyle's law in action.

### Dalton's Law of Partial Pressures

> **P_total = P_A + P_B + P_C + ...**

Each gas in a mixture exerts pressure independently as if the other gases were not there. The **partial pressure** of a gas depends on its **mole fraction**:

> **P_A = X_A * P_total** where X_A = n_A / n_total

**Biological application -- Alveolar gas exchange:**

Atmospheric air at sea level (760 mmHg) is approximately:
- N2: 78% --> P_N2 = 0.78 x 760 = ~593 mmHg
- O2: 21% --> P_O2 = 0.21 x 760 = ~160 mmHg
- CO2: 0.04% --> P_CO2 = ~0.3 mmHg

In the alveoli, partial pressures are different because air is humidified and CO2 is added:
- P_O2 ~ 100 mmHg (alveolar), vs ~40 mmHg in deoxygenated blood --> O2 diffuses IN to blood
- P_CO2 ~ 40 mmHg (alveolar), vs ~46 mmHg in deoxygenated blood --> CO2 diffuses OUT of blood

**Gas exchange is driven entirely by partial pressure gradients.** No active transport -- just diffusion down concentration (partial pressure) gradients across the thin alveolar membrane.

### Kinetic Molecular Theory (KMT)

Assumptions of an **ideal gas**:
1. Gas particles have **negligible volume** compared to the container
2. No intermolecular forces (no attraction or repulsion between particles)
3. Collisions are perfectly **elastic** (no energy lost)
4. Particles move in **random, straight-line** motion
5. **Average kinetic energy** is proportional to absolute temperature

The key quantitative relationship:

> **KE_avg = 3/2 * k_B * T**

Where k_B is Boltzmann's constant (1.38 x 10^-23 J/K) and T is in Kelvin.

This means: **at a given temperature, ALL gases have the same average kinetic energy**, regardless of their molecular mass. A helium atom and a xenon atom at the same temperature have the same average KE.

But since KE = 1/2 * m * v^2, lighter gases must move **faster** to have the same KE:

> **v_rms = sqrt(3RT/M)**

Where M is molar mass (in kg/mol if R = 8.314 J/mol*K).

**MCAT tip:** Lighter gases diffuse faster (Graham's law), effuse faster, and have higher average speeds. At the same temperature:
- rate1/rate2 = sqrt(M2/M1)
- H2 moves 4x faster than O2 (since sqrt(32/2) = 4)

### Real Gases and the van der Waals Equation

Real gases deviate from ideal behavior. The **van der Waals equation** corrects for this:

> **(P + a*n^2/V^2)(V - nb) = nRT**

The two corrections:
- **a*n^2/V^2** corrects for **intermolecular attractions** (real molecules attract each other, so actual pressure is lower than ideal; we add a term to compensate)
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

## 5. Starling Forces (Capillary Fluid Exchange)

This is a **known Kaplan gap** -- Kaplan covers it lightly, but the MCAT tests it. Master this.

### The Four Starling Forces

Fluid movement across capillary walls is governed by the balance of four pressures:

| Force | Symbol | Direction | Definition |
|-------|--------|-----------|------------|
| **Capillary hydrostatic pressure** | P_c | Pushes fluid OUT of capillary | Blood pressure inside the capillary |
| **Interstitial hydrostatic pressure** | P_i | Pushes fluid INTO capillary | Pressure of fluid in the tissue space (usually ~0 or slightly negative) |
| **Capillary oncotic (colloid osmotic) pressure** | pi_c | Pulls fluid INTO capillary | Osmotic pressure due to plasma proteins (mainly **albumin**) |
| **Interstitial oncotic pressure** | pi_i | Pulls fluid OUT of capillary | Osmotic pressure due to proteins in interstitial fluid (usually low) |

**Net filtration pressure (NFP):**

> **NFP = (P_c - P_i) - (pi_c - pi_i)**

Or more intuitively:
> NFP = (forces pushing fluid OUT) - (forces pulling fluid IN)

### What Happens Along a Capillary

**Arterial end:**
- P_c is high (~35 mmHg) because blood just came from the arteriole
- pi_c ~ 26 mmHg (constant along the capillary -- protein concentration does not change much)
- NFP = 35 - 0 - 26 + 0 = **+9 mmHg** (net filtration OUT)
- Fluid and nutrients leave the capillary into the tissue

**Venous end:**
- P_c has dropped (~15 mmHg) due to resistance along the capillary
- pi_c still ~ 26 mmHg
- NFP = 15 - 0 - 26 + 0 = **-11 mmHg** (net reabsorption IN)
- Fluid returns into the capillary

Approximately **85%** of filtered fluid is reabsorbed at the venous end. The remaining **15%** is collected by the **lymphatic system** and returned to the blood.

### Edema (Fluid Accumulation in Tissues)

**Edema** occurs when there is excess fluid in the interstitial space. It results from any disruption that increases filtration or decreases reabsorption:

| Cause | Mechanism | Example |
|-------|-----------|---------|
| Increased P_c | More fluid pushed out | Heart failure (venous congestion), standing for long periods |
| Decreased pi_c | Less fluid pulled back in | Liver disease (reduced albumin synthesis), nephrotic syndrome (albumin loss in urine), malnutrition (kwashiorkor) |
| Increased capillary permeability | Proteins leak into interstitium, raising pi_i | Inflammation, burns, allergic reactions |
| Lymphatic blockage | Filtered fluid cannot be returned | Lymph node removal (surgery), parasitic infection (elephantiasis) |

**MCAT tip:** "Low albumin = edema" is a high-yield connection. Albumin is the most abundant plasma protein and the primary determinant of oncotic pressure. If albumin drops (liver failure, kidney loss, malnutrition), oncotic pressure drops, reabsorption decreases, and fluid accumulates in tissues.

---

## 6. Biological Connections

### Blood Flow and the Circulatory System

The circulatory system is the MCAT's favorite playground for fluid dynamics questions. Here is how the physics maps onto biology:

**Poiseuille's Law and Blood Flow:**
- Arterioles are the primary site of **vascular resistance regulation** because smooth muscle can change their radius. Even small radius changes cause huge flow changes (r^4).
- Sympathetic activation --> vasoconstriction --> decreased radius --> dramatically decreased flow to non-essential organs during fight-or-flight.
- Local metabolites (CO2, H+, adenosine) cause **vasodilation** in active tissues --> increased radius --> increased blood flow to where it is needed.

**Continuity Equation and Blood Velocity:**
- Blood is fastest in the **aorta** (smallest total cross-section, ~2.5 cm^2)
- Blood is slowest in the **capillaries** (largest total cross-section, ~4500 cm^2)
- This slow capillary flow maximizes exchange time

**Bernoulli and Blood Pressure:**
- In an atherosclerotic plaque (stenosis): narrowed lumen --> increased velocity --> decreased lateral pressure on the wall --> but downstream, turbulence and energy loss cause complications
- In an aneurysm: widened lumen --> decreased velocity --> increased pressure --> further dilation (dangerous positive feedback)

**Blood Pressure Measurement:**
- Systolic = peak pressure during ventricular contraction
- Diastolic = minimum pressure during ventricular relaxation
- Measured in mmHg (gauge pressure, relative to atmospheric)
- Korotkoff sounds heard by stethoscope are caused by **turbulent flow** through a partially compressed brachial artery

### Gas Exchange in the Lungs and Tissues

**Ventilation mechanics (Boyle's law):**
- **Inhalation:** diaphragm contracts (flattens) + external intercostals contract --> thoracic volume increases --> intrapulmonary pressure drops below atmospheric --> air flows in
- **Exhalation (quiet):** diaphragm relaxes, elastic recoil of lungs --> thoracic volume decreases --> intrapulmonary pressure rises above atmospheric --> air flows out
- **Forced exhalation:** internal intercostals + abdominal muscles contract

**Alveolar gas exchange (Dalton's law + Fick's law of diffusion):**
- O2 diffuses from alveolar air (P_O2 ~ 100 mmHg) into blood (P_O2 ~ 40 mmHg)
- CO2 diffuses from blood (P_CO2 ~ 46 mmHg) into alveolar air (P_CO2 ~ 40 mmHg)
- The partial pressure gradient is steeper for O2 than for CO2, but CO2 diffuses ~20x faster because it is much more soluble in the aqueous alveolar membrane
- At high altitude, atmospheric P_O2 is lower --> alveolar P_O2 drops --> smaller gradient --> less O2 delivery --> body compensates by increasing ventilation rate and eventually increasing red blood cell production (EPO)

**Henry's Law** (bonus connection): The amount of gas dissolved in a liquid is proportional to the partial pressure of that gas above the liquid:

> **[gas]_dissolved = k_H * P_gas**

This explains:
- Why CO2 dissolves out of soda when you open the can (P_CO2 drops)
- Decompression sickness ("the bends") -- at depth, high P_N2 causes more N2 to dissolve in blood; rapid ascent drops P_N2 suddenly, and N2 comes out of solution as bubbles
- Why oxygen delivery to tissues depends on P_O2

---

## High-Yield Summary Table

| Concept | Key Equation | What to Remember |
|---------|-------------|-----------------|
| Hydrostatic pressure | P = rho * g * h | Depends only on depth, not container shape |
| Pascal's law | F1/A1 = F2/A2 | Pressure transmitted undiminished; hydraulic advantage |
| Archimedes | F_b = rho_fluid * V_disp * g | Float if rho_object < rho_fluid |
| Continuity | A1v1 = A2v2 | Narrow pipe = fast flow; capillaries slow due to huge total A |
| Bernoulli | P + 1/2*rho*v^2 + rho*g*h = const | Fast flow = low pressure (aneurysm, airplane wing) |
| Poiseuille | Q proportional to r^4 | r^4 is king; small vasoconstriction = huge flow drop |
| Ideal gas | PV = nRT | T must be in Kelvin; 22.4 L/mol at STP |
| Dalton | P_total = sum of P_partial | Gas exchange driven by partial pressure gradients |
| KMT | KE_avg = 3/2 * k_B * T | Same T = same KE for all gases; lighter = faster |
| van der Waals | corrections a and b | Deviate from ideal at high P, low T |
| Starling forces | NFP = (P_c - P_i) - (pi_c - pi_i) | Filtration at arterial end, reabsorption at venous end |

---

## Common MCAT Traps and Tips

1. **Forgetting to convert to Kelvin.** Every single gas law calculation requires absolute temperature. 0 degrees C is NOT zero -- it is 273 K.

2. **Confusing individual vs total cross-sectional area.** One capillary is tiny, but the sum of all capillaries is enormous. Continuity applies to the total area at each level.

3. **Thinking higher velocity = higher pressure.** Bernoulli says the opposite. Fast-moving fluid has LOW lateral pressure. This is the single most common conceptual error in fluids.

4. **Forgetting r^4 in Poiseuille.** The MCAT will ask "what happens to flow if the radius is halved?" The answer is flow drops to 1/16th, not 1/2. Always think r to the fourth.

5. **Mixing up gauge and absolute pressure.** If a problem says "the pressure is 2 atm," ask yourself: gauge or absolute? If it is depth-related, it is usually absolute.

6. **Ignoring oncotic pressure in Starling problems.** Students focus only on hydrostatic pressure, but oncotic pressure (albumin) is the reason fluid comes BACK into capillaries. Low albumin = edema.

7. **Assuming ideal gas behavior for all problems.** If a question mentions high pressure, low temperature, or asks which gas deviates most, you need to think real gas behavior.

8. **Confusing diffusion rate with average KE.** At the same temperature, all gases have the same average KE, but lighter gases move FASTER. Graham's law governs diffusion/effusion rates.
