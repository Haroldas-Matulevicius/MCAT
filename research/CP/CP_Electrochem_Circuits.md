# FC4C: Electrochemistry and Electrical Circuits

**Section:** Chem/Phys (CP)
**Foundational Concept 4C:** Electrostatics, Circuits, Magnetism, Electrochemistry
**Source:** Kaplan Physics Ch. 5-7, Kaplan Gen Chem Ch. 12
**Yield:** HIGH -- circuits and electrochemistry appear on nearly every MCAT

---

## 1. Electrostatics

### Charge: The Basics

**Charge is quantized** -- it comes in discrete packets. The smallest unit of charge is the elementary charge, **e = 1.6 x 10^-19 C**. Every charge you will ever encounter on the MCAT is a whole-number multiple of e. Protons carry +e, electrons carry -e. You cannot have half a charge.

**Charge is conserved** -- charge is never created or destroyed; it is only transferred from one object to another. When you rub a balloon on your hair, electrons move from your hair to the balloon. Your hair becomes positive, the balloon becomes negative, but the total charge of the system stays the same. This conservation principle shows up in circuit analysis (Kirchhoff's junction rule) and in electrochemistry (balancing half-reactions).

### Conductors vs. Insulators

- **Conductors** (metals, electrolyte solutions): electrons move freely. In a conductor at electrostatic equilibrium, all excess charge sits on the outer surface and the electric field inside is zero.
- **Insulators** (rubber, glass, plastic): electrons are locked in place. Charge stays wherever you put it.

MCAT cares about this distinction mostly for circuits and for understanding why metals form the electrodes in electrochemical cells.

### Coulomb's Law

$$F = k \frac{q_1 q_2}{r^2}$$

where **k = 8.99 x 10^9 N m^2 / C^2** (round to 9 x 10^9 for calculations).

This gives the **force** between two point charges. Key features:

- **Inverse square law** -- double the distance, force drops to 1/4. Triple the distance, force drops to 1/9. This is the same relationship as gravitational force (F = Gm1m2/r^2).
- **Like charges repel, opposite charges attract.** If you plug in signs, a negative force means attraction; positive means repulsion. On the MCAT, just reason through it conceptually.
- **Comparison to gravity:** Both are inverse square. But gravity is always attractive (masses are always positive), while electrostatic force can attract or repel. Electrostatic force is enormously stronger than gravity at the atomic scale.

**MCAT tip:** You will rarely compute Coulomb's law numerically. The test loves proportional reasoning. "If the distance between two charges triples, what happens to the force?" Answer: it decreases by a factor of 9. Practice this pattern.

### Electric Field

$$E = k \frac{Q}{r^2}$$

The **electric field** is the force per unit positive test charge at a point in space. Units: N/C or V/m (these are equivalent).

**Direction convention:** Electric field lines point **away from positive charges** and **toward negative charges**. Think of it as the direction a positive test charge would move if placed at that point.

Between two parallel plates (the setup the MCAT loves most), the field is **uniform** -- same magnitude and direction everywhere between the plates. The field points from the positive plate toward the negative plate.

$$E = \frac{V}{d} \quad \text{(between parallel plates)}$$

where V is the voltage across the plates and d is the separation. This equation is a favorite on the exam.

### Electric Potential (Voltage)

$$V = k \frac{Q}{r}$$

**Potential is a scalar, not a vector.** This is critical. When computing the potential at a point due to multiple charges, you just add the values algebraically (with signs). No vector components, no trigonometry. This makes potential calculations far easier than force or field calculations.

- Positive charges create positive potential in the surrounding space.
- Negative charges create negative potential.
- Potential decreases as you move away from a positive charge.

**Potential vs. potential energy:** Potential (V) is the property of a point in space. Potential energy (U) is the property of a charge placed at that point.

$$U = qV = k \frac{q_1 q_2}{r}$$

A positive charge naturally moves from high potential to low potential (like a ball rolling downhill). A negative charge moves from low potential to high potential. Both are moving to lower potential energy.

### Equipotential Lines

**Equipotential lines (or surfaces) are always perpendicular to electric field lines.** No work is done when moving a charge along an equipotential surface, because the force (along the field line) is perpendicular to the displacement (along the equipotential).

Around a point charge, equipotentials are concentric spheres. Between parallel plates, they are flat planes parallel to the plates. Draw this picture for yourself -- it comes up in passage figures.

### Capacitors

A **capacitor** stores charge and energy in an electric field between two conductors. The MCAT overwhelmingly focuses on the **parallel plate capacitor**.

**Capacitance:**

$$C = \varepsilon_0 \frac{A}{d}$$

where A is the plate area, d is the plate separation, and epsilon_0 = 8.85 x 10^-12 F/m is the permittivity of free space. Units of capacitance: **Farads (F)**.

Bigger plates or closer spacing = more capacitance. This is intuitive -- bigger plates hold more charge, closer plates have a stronger field pulling charge onto them.

**Charge-voltage relationship:**

$$Q = CV$$

This is the defining equation for capacitance. A capacitor with higher C stores more charge for the same voltage.

**Energy stored:**

$$U = \frac{1}{2}CV^2 = \frac{Q^2}{2C} = \frac{1}{2}QV$$

All three forms are equivalent. Which one you use depends on what's held constant in the problem (this matters a lot when the MCAT changes something -- see below).

**Dielectrics:**

A **dielectric** is an insulating material inserted between the plates. It increases capacitance by a factor of **kappa** (the dielectric constant, always >= 1):

$$C' = \kappa C$$

What happens when you insert a dielectric depends on whether the capacitor is **connected to a battery or isolated**:

| Scenario | V | Q | C | E (field) | U (energy) |
|----------|---|---|---|-----------|------------|
| **Battery connected** (V fixed) | Same | Increases (Q=CV, C up) | Increases | Same (E=V/d) | Increases (U=1/2CV^2) |
| **Isolated** (Q fixed) | Decreases (V=Q/C, C up) | Same | Increases | Decreases | Decreases (U=Q^2/2C) |

**MCAT trap:** Students constantly mix these two scenarios up. Always ask: "Is V fixed (battery connected) or is Q fixed (isolated)?" Then use the defining equations to figure out what changes.

---

## 2. Magnetism

### Force on a Moving Charge

$$F = qvB\sin\theta$$

A magnetic field exerts a force on a **moving** charge. If the charge is stationary (v = 0), there is no magnetic force. If the charge moves parallel to the field (theta = 0 or 180 degrees), sin(theta) = 0 and there is no force.

Maximum force occurs when the charge moves **perpendicular** to the field (theta = 90 degrees, sin = 1).

### The Right-Hand Rule -- Step by Step

This is worth memorizing with your hand, not just reading about.

1. **Point your fingers** in the direction of the velocity (v) of a positive charge.
2. **Curl your fingers** toward the direction of the magnetic field (B).
3. **Your thumb** points in the direction of the force (F) on the positive charge.

For a **negative charge** (like an electron), the force is in the **opposite direction** of what the right-hand rule gives you. Do the right-hand rule, then flip the answer.

**Alternative approach:** Some students prefer the flat-hand method: fingers point along v, palm faces toward B, thumb points along F. Use whichever is more natural for you, but practice until it is automatic.

### Magnetic Force Does No Work

This is one of the most testable conceptual points about magnetism on the MCAT.

**The magnetic force is always perpendicular to the velocity of the charge.** Since work = F dot d = Fd cos(theta), and the angle between F and v is always 90 degrees, the magnetic force does **zero work**. It can change the direction of motion but never the speed. A charged particle in a uniform magnetic field moves in a **circle** (constant speed, changing direction).

**MCAT consequence:** If a passage says a charged particle speeds up in a magnetic field, there must be an electric field (or some other force) doing the work. The magnetic field alone cannot change kinetic energy.

### Force on a Current-Carrying Wire

$$F = BIL\sin\theta$$

where I is the current, L is the length of wire in the field, and theta is the angle between the wire and the field. Use the right-hand rule with the direction of current replacing the velocity direction.

### Magnetic Field from a Long Straight Wire

$$B = \frac{\mu_0 I}{2\pi r}$$

The field wraps around the wire in concentric circles. To find the direction, use the right-hand rule for wires: point your thumb in the direction of current flow, and your fingers curl in the direction of the magnetic field.

This is lower yield on the MCAT, but you should know the basic relationship: field strength is proportional to current and inversely proportional to distance from the wire.

---

## 3. Circuits

### Current

$$I = \frac{Q}{t}$$

**Current** is the rate of charge flow. Units: **Amperes (A)** = Coulombs per second. By convention, current flows from high potential (+) to low potential (-), which is the direction positive charges would move. Electrons actually flow the opposite way, but the MCAT uses conventional current unless explicitly stated otherwise.

### Resistance

$$R = \frac{\rho L}{A}$$

where rho is the **resistivity** of the material (an intrinsic property), L is the length, and A is the cross-sectional area of the conductor. 

- Longer wire = more resistance (more material for electrons to push through).
- Thicker wire = less resistance (wider path for electrons).
- Higher resistivity = more resistance (the material itself resists current more).

Units: **Ohms** (omega symbol).

### Ohm's Law

$$V = IR$$

The voltage drop across a resistor equals the current through it times its resistance. This equation is the single most used equation in circuit problems. Know it cold.

### Power

$$P = IV = I^2R = \frac{V^2}{R}$$

All three forms come from combining P = IV with V = IR. Which form you use depends on what information you have and what is held constant.

**Key insight:** In a series circuit (same current through all resistors), power dissipated is proportional to R (use P = I^2 R). In a parallel circuit (same voltage across all resistors), power dissipated is inversely proportional to R (use P = V^2/R). The largest resistor in series dissipates the most power; the smallest resistor in parallel dissipates the most power.

### Series Circuits

Components connected end-to-end, forming a single path for current.

**Rules:**
- **Current is the same** through every component: I_total = I_1 = I_2 = I_3
- **Resistances add:** R_total = R_1 + R_2 + R_3
- **Voltage divides** among components proportionally to resistance: V_1 = IR_1, V_2 = IR_2, etc.
- V_total = V_1 + V_2 + V_3

**Worked approach -- voltage divider:** If a 12V battery is connected to a 3-ohm and a 6-ohm resistor in series:
- R_total = 3 + 6 = 9 ohm
- I = V/R = 12/9 = 4/3 A
- V across 3-ohm: (4/3)(3) = 4V
- V across 6-ohm: (4/3)(6) = 8V
- Check: 4 + 8 = 12V. Checks out.

### Parallel Circuits

Components connected across the same two nodes, providing multiple paths for current.

**Rules:**
- **Voltage is the same** across every branch: V_total = V_1 = V_2 = V_3
- **Reciprocal resistances add:** 1/R_total = 1/R_1 + 1/R_2 + 1/R_3
- **Current divides** among branches inversely proportional to resistance: I_1 = V/R_1, I_2 = V/R_2
- I_total = I_1 + I_2 + I_3

**Key fact:** Adding a resistor in parallel always **decreases** total resistance. The total resistance of a parallel combination is always less than the smallest individual resistor. Adding more paths for current to flow means less total resistance.

**Quick formula for two resistors in parallel:**

$$R_{total} = \frac{R_1 \times R_2}{R_1 + R_2}$$

This "product over sum" shortcut is faster than the reciprocal method for two resistors and comes up constantly.

### Kirchhoff's Rules

**Junction Rule (KCL -- Conservation of Charge):** The total current entering a junction equals the total current leaving. Charge does not pile up at a node.

$$\sum I_{in} = \sum I_{out}$$

**Loop Rule (KVL -- Conservation of Energy):** The sum of all voltage gains and drops around any closed loop equals zero. What you gain from batteries, you lose across resistors.

$$\sum V = 0 \text{ (around any closed loop)}$$

**How to apply the loop rule:**
1. Pick a direction to traverse the loop (clockwise or counterclockwise -- doesn't matter).
2. When you cross a battery from - to +, that is a voltage **gain** (+EMF).
3. When you cross a resistor in the direction of current, that is a voltage **drop** (-IR).
4. Set the sum equal to zero and solve.

These rules are how you solve any multi-loop circuit the MCAT throws at you.

### Internal Resistance and EMF

A real battery has **internal resistance** (r). The **EMF** (electromotive force, epsilon) is the ideal voltage the battery would produce with no internal resistance. The actual **terminal voltage** you measure is:

$$V_{terminal} = \varepsilon - Ir$$

where I is the current drawn from the battery. As current increases, more voltage is "wasted" inside the battery, and the terminal voltage drops.

For the full circuit with an external resistance R:

$$I = \frac{\varepsilon}{R + r}$$

**MCAT tip:** If a problem says "ideal battery," internal resistance is zero and V_terminal = EMF. If it says "real battery" or gives you an internal resistance, use the equations above.

### RC Circuits

A resistor-capacitor circuit has a **time constant:**

$$\tau = RC$$

Units: seconds (verify: ohm x farad = (V/A)(C/V) = C/A = seconds).

**Charging** (capacitor connected to a battery through a resistor):
- Charge builds up exponentially: Q(t) = Q_max(1 - e^(-t/RC))
- Current starts at maximum (I_0 = V/R) and decays: I(t) = I_0 e^(-t/RC)
- After one time constant (t = RC), the capacitor has ~63% of its final charge.
- After 5 time constants, the capacitor is ~99% charged (treat as fully charged).

**Discharging** (capacitor releases stored charge through a resistor):
- Charge decays exponentially: Q(t) = Q_0 e^(-t/RC)
- Current decays: I(t) = I_0 e^(-t/RC)
- After one time constant, ~37% of the original charge remains.

**MCAT relevance:** You probably will not need to do detailed exponential calculations. Know the shape of the curves (exponential growth toward max for charging, exponential decay toward zero for discharging) and the meaning of the time constant. Larger R or larger C means the circuit charges/discharges more slowly.

### Ammeters and Voltmeters

**Ammeter** -- measures current:
- Connected in **series** with the component.
- Must have very **low internal resistance** so it does not significantly change the current it is trying to measure.

**Voltmeter** -- measures voltage:
- Connected in **parallel** with the component.
- Must have very **high internal resistance** so it draws negligible current from the circuit.

**MCAT trap:** If these are connected incorrectly (ammeter in parallel = short circuit/damage; voltmeter in series = blocks current), the reading will be wrong or the meter may be damaged.

---

## 4. Electrochemistry

### Galvanic (Voltaic) Cells

A **galvanic cell** converts chemical energy into electrical energy through a **spontaneous** redox reaction. This is the "regular battery" you use in everyday life.

**Key identifiers of a galvanic cell:**
- **Spontaneous** (reaction proceeds without external energy input)
- **delta-G < 0** (negative free energy change = spontaneous)
- **E_cell > 0** (positive cell potential)
- **Anode is negative**, cathode is positive (this is the one that flips for electrolytic cells)

**Cell anatomy:**
- **Anode:** Oxidation occurs here. Electrons leave the anode. The anode loses mass as metal atoms are oxidized into solution.
- **Cathode:** Reduction occurs here. Electrons arrive at the cathode. The cathode gains mass as metal ions in solution are reduced and deposited.
- **Salt bridge:** Allows ions to flow between half-cells to maintain electrical neutrality. Cations migrate toward the cathode compartment (which is becoming more negative as positive ions deposit); anions migrate toward the anode compartment.
- **External wire:** Electrons flow from anode to cathode through the wire. Current (conventional) flows from cathode to anode through the wire.

**Memory aid:** **An Ox** (anode = oxidation), **Red Cat** (reduction = cathode). Also: alphabetically, A comes before C, and O comes before R.

### Electrolytic Cells

An **electrolytic cell** uses electrical energy to drive a **non-spontaneous** reaction. Think electrolysis of water, electroplating, purifying metals.

**Key identifiers of an electrolytic cell:**
- **Non-spontaneous** (requires external voltage source)
- **delta-G > 0** (positive free energy change)
- **E_cell < 0** (negative cell potential -- it would not happen on its own)
- **Anode is positive**, cathode is negative (the external battery forces the signs)

The processes at the electrodes are the same: oxidation still happens at the anode, reduction still happens at the cathode. The "An Ox, Red Cat" mnemonic works for both cell types. What changes is the sign convention on the electrodes.

### Standard Reduction Potentials

The **standard reduction potential** (E^0) is measured for each half-reaction written as a reduction. The table is always given on the MCAT. A more positive E^0 means the species has a greater tendency to be reduced.

**How to use the table:**
1. Identify which species gets **reduced** (higher E^0 = better oxidizing agent, wants electrons).
2. Identify which species gets **oxidized** (lower E^0 = better reducing agent, gives up electrons).
3. The species with the more positive reduction potential is the cathode (reduction).
4. The species with the more negative reduction potential is the anode (oxidation).

**Critical rule:** When you reverse a half-reaction (to write it as oxidation), you flip the sign of E^0 for conceptual purposes, but when calculating cell potential, use the formula below -- do NOT flip and add.

### Cell Potential Calculation

$$E^0_{cell} = E^0_{cathode} - E^0_{anode}$$

Always cathode minus anode, using the reduction potentials as given in the table. Do not reverse signs manually and add -- just subtract.

**Worked example:** Given:
- Cu^2+ + 2e^- -> Cu, E^0 = +0.34 V
- Zn^2+ + 2e^- -> Zn, E^0 = -0.76 V

Cu has the higher reduction potential, so Cu^2+ is reduced (cathode). Zn is oxidized (anode).

E^0_cell = (+0.34) - (-0.76) = +1.10 V

Positive cell potential confirms this is spontaneous as a galvanic cell.

**MCAT tip:** If your calculated E^0_cell comes out negative, either you have the cathode and anode backwards, or the reaction is non-spontaneous as written (electrolytic conditions).

### The Nernst Equation

$$E = E^0 - \frac{RT}{nF}\ln Q$$

At 25 degrees C, this simplifies to:

$$E = E^0 - \frac{0.0592}{n}\log Q$$

where:
- n = number of moles of electrons transferred
- F = Faraday's constant = 96,485 C/mol (approximately 10^5 C/mol for estimation)
- Q = reaction quotient (products over reactants, same as for equilibrium expressions)

**What this tells you:** The cell potential changes as concentrations deviate from standard conditions. If Q < 1 (more reactants), E > E^0 (cell potential increases). If Q > 1 (more products), E < E^0 (cell potential decreases). At equilibrium, Q = K and E = 0 (the battery is dead).

**MCAT approach:** You rarely need to compute a Nernst equation numerically. Understand the direction of change:
- Increasing reactant concentration increases E (drives reaction forward).
- Increasing product concentration decreases E (less driving force).
- At equilibrium, E = 0 and Q = K.

### Concentration Cells

A **concentration cell** is a galvanic cell where both half-cells have the same electrode material but different ion concentrations. E^0_cell = 0 (same half-reactions), but E_cell is not zero because Q is not 1.

The cell generates voltage purely from the concentration difference. The more concentrated side is the cathode (reduction occurs there, depositing metal to reduce ion concentration). The more dilute side is the anode (oxidation occurs there, dissolving metal to increase ion concentration).

The cell runs until concentrations equalize, at which point Q = 1, ln(Q) = 0, and E = 0.

### Free Energy and Cell Potential

$$\Delta G^0 = -nFE^0$$

This connects thermodynamics to electrochemistry. Key relationships:

| Condition | delta-G | E_cell | Reaction |
|-----------|---------|--------|----------|
| Spontaneous (galvanic) | Negative | Positive | Proceeds forward |
| Equilibrium | Zero | Zero | No net reaction |
| Non-spontaneous (electrolytic) | Positive | Negative | Requires external energy |

**Notice the signs are always opposite.** Positive E means negative delta-G, and vice versa. The factor -nF just converts between energy units and voltage.

You can also connect to equilibrium:

$$\Delta G^0 = -RT\ln K$$

So: **-nFE^0 = -RT ln K**, which gives **E^0 = (RT/nF) ln K**. A large positive E^0 means a large K (products strongly favored at equilibrium).

### Faraday's Law of Electrolysis

This is about calculating how much substance is deposited or consumed during electrolysis.

$$\text{moles of electrons} = \frac{It}{F}$$

where I is current (in Amperes), t is time (in seconds), and F is Faraday's constant.

**Step-by-step approach:**
1. Calculate total charge: Q = It (coulombs)
2. Convert to moles of electrons: mol e^- = Q / F
3. Use stoichiometry of the half-reaction to convert to moles of substance. Example: Cu^2+ + 2e^- -> Cu means 2 moles of electrons per mole of Cu deposited.
4. Convert moles of substance to grams using molar mass.

**Worked example:** How many grams of Cu are deposited when 5 A flows for 3860 seconds?
- Q = It = 5 x 3860 = 19,300 C
- mol e^- = 19,300 / 96,500 = 0.2 mol e^-
- Cu^2+ + 2e^- -> Cu, so mol Cu = 0.2/2 = 0.1 mol
- Mass = 0.1 x 63.5 g/mol = 6.35 g

This is a straightforward stoichiometry problem once you know the entry point (Q = It, convert with Faraday's constant).

---

## 5. MCAT Traps and High-Yield Pitfalls

### Trap 1: Galvanic vs. Electrolytic Anode/Cathode Signs

| | Galvanic Cell | Electrolytic Cell |
|---|---|---|
| Anode | Negative (-) | Positive (+) |
| Cathode | Positive (+) | Negative (-) |
| Oxidation at anode? | Yes | Yes |
| Reduction at cathode? | Yes | Yes |

The processes do not change. "An Ox, Red Cat" always applies. What changes is the **charge sign** on the electrodes. In galvanic cells, the anode is negative because it is the source of electrons. In electrolytic cells, the external battery forces the anode to be positive.

**How to avoid the trap:** Do not memorize electrode signs. Instead, reason from first principles -- identify which species is oxidized and which is reduced, then assign anode/cathode accordingly.

### Trap 2: Magnetic Force Does No Work

If a question says "a charged particle enters a magnetic field and gains kinetic energy," something else is providing the energy. The magnetic force cannot do work because it is always perpendicular to displacement. A magnetic field can deflect particles, cause circular motion, and sort ions by mass (mass spectrometry), but it cannot accelerate or decelerate them in terms of speed.

### Trap 3: Resistors vs. Capacitors in Series and Parallel -- Opposite Rules

| | Resistors | Capacitors |
|---|---|---|
| **Series** | Add directly: R_total = R_1 + R_2 | Add reciprocals: 1/C_total = 1/C_1 + 1/C_2 |
| **Parallel** | Add reciprocals: 1/R_total = 1/R_1 + 1/R_2 | Add directly: C_total = C_1 + C_2 |

The rules are **exactly reversed**. For resistors, series adds directly. For capacitors, parallel adds directly.

**Intuition for capacitors:** Capacitors in parallel effectively create a bigger plate area (A goes up, C goes up, so capacitances add). Capacitors in series effectively increase the distance between the outer plates (d goes up, C goes down, so reciprocals add).

### Trap 4: E_cell Calculation Sign Error

Students often try to "reverse the sign" of the anode's reduction potential and then add. This works if done correctly but causes frequent sign errors. The safer approach:

**Always use E^0_cell = E^0_cathode - E^0_anode with both values taken directly from the reduction potential table. Do not flip anything. Just subtract.**

### Trap 5: Dielectric with Battery Connected vs. Isolated

As detailed in the capacitor section above, inserting a dielectric has opposite effects on voltage and energy depending on the constraint. If the MCAT does not specify, look for clues: "battery remains connected" means V is constant; "capacitor is disconnected/isolated" means Q is constant.

### Trap 6: Standard Reduction Potentials Are Intensive Properties

Doubling the coefficients in a half-reaction does **not** change E^0. If Cu^2+ + 2e^- -> Cu has E^0 = +0.34 V, then 2Cu^2+ + 4e^- -> 2Cu also has E^0 = +0.34 V. Potential is intensive (like temperature or density). This matters when balancing half-reactions to find cell potential -- do not multiply E^0 by the stoichiometric coefficient.

### Trap 7: Current Direction vs. Electron Flow

Conventional current flows from + to - (high to low potential) through the external circuit. Electrons actually flow from - to + (anode to cathode in a galvanic cell). The MCAT may describe either. Read carefully to know which one is being asked about.

---

## Quick Reference: Key Equations

| Concept | Equation | Notes |
|---------|----------|-------|
| Coulomb's law | F = kq_1q_2/r^2 | Inverse square; k = 9 x 10^9 |
| Electric field | E = kQ/r^2 | Vector; points away from + |
| Electric field (plates) | E = V/d | Uniform between parallel plates |
| Electric potential | V = kQ/r | Scalar (no direction) |
| Potential energy | U = kq_1q_2/r | Sign matters |
| Capacitance | C = epsilon_0 A/d | Parallel plate |
| Charge on capacitor | Q = CV | Defining relationship |
| Energy in capacitor | U = 1/2 CV^2 | Also Q^2/2C, also 1/2 QV |
| Dielectric | C' = kappa C | kappa >= 1 |
| Magnetic force (charge) | F = qvBsin(theta) | Always perpendicular to v |
| Magnetic force (wire) | F = BILsin(theta) | |
| Current | I = Q/t | Charge per time |
| Resistance | R = rho L/A | Resistivity x length / area |
| Ohm's law | V = IR | Most-used circuit equation |
| Power | P = IV = I^2R = V^2/R | Three equivalent forms |
| Series R | R_total = R_1 + R_2 + ... | Same I, V divides |
| Parallel R | 1/R_total = 1/R_1 + 1/R_2 + ... | Same V, I divides |
| Series C | 1/C_total = 1/C_1 + 1/C_2 + ... | Opposite of resistors |
| Parallel C | C_total = C_1 + C_2 + ... | Opposite of resistors |
| Time constant (RC) | tau = RC | 63% charged at t = tau |
| EMF and internal R | V = EMF - Ir | Terminal voltage |
| Cell potential | E^0_cell = E^0_cathode - E^0_anode | Always subtract |
| Nernst equation | E = E^0 - (RT/nF)lnQ | Or E^0 - (0.0592/n)logQ at 25C |
| Free energy | delta-G^0 = -nFE^0 | Signs always opposite |
| Faraday's law | mol e^- = It/F | F ~ 96,500 C/mol |

---

## How to Attack MCAT Questions on These Topics

1. **Electrostatics/field questions:** Default to proportional reasoning. The test rarely asks for exact numbers. Know how changing distance, charge, or plate separation affects force, field, potential, and capacitance.

2. **Circuit questions:** Start by identifying series vs. parallel. Find total resistance, then total current, then work outward to individual components. Use Kirchhoff's rules for multi-loop circuits.

3. **Magnetism questions:** Check if the particle is moving. Check the angle. Apply the right-hand rule. Remember that magnetic force does no work.

4. **Electrochemistry questions:** First identify galvanic vs. electrolytic. Then identify the anode and cathode from reduction potentials. Calculate E^0_cell. If concentrations are non-standard, apply Nernst equation reasoning (qualitative is usually sufficient).

5. **Electrolysis calculations:** Follow the four-step process: Q = It, convert to moles of electrons, use stoichiometry, convert to grams.

6. **When in doubt on sign conventions:** Go back to first principles. Spontaneous reactions have positive E and negative delta-G. Oxidation happens at the anode. Reduction happens at the cathode. These facts do not change regardless of cell type.
