# Physics & Math Chapter 10 — Mathematics

Scope: Arithmetic and significant figures; scientific notation; exponents and logarithms (pH, pKa, decibels, Nernst); trigonometry (standard angles, SOH-CAH-TOA); unit conversions and metric prefixes; proportional reasoning; graphical analysis; estimation strategies; problem-solving approach.

**Section:** Chemical/Physical (CP) — Physics & Math
**Book:** Kaplan Physics and Math Strategies 2024 — Chapter 10
**AAMC FC mapping:** Cross-cutting — used in every quantitative CP question
**Yield:** Critical. There is NO calculator on the MCAT. These skills make or break timing on the CP section.

---

## 1. Scientific Notation

Scientific notation is the language of MCAT math. Every quantitative problem uses it.

### Multiplying

Multiply the coefficients, ADD the exponents.

> (3.0 × 10⁴) × (2.0 × 10⁵)
> = 6.0 × 10⁹

If coefficient product ≥ 10, shift:

> (4.0 × 10³) × (5.0 × 10⁶) = 20 × 10⁹ = **2.0 × 10¹⁰**

### Dividing

Divide the coefficients, SUBTRACT the exponents (numerator minus denominator).

> (8.0 × 10⁶) / (2.0 × 10²) = 4.0 × 10⁴

If coefficient result < 1:

> (2.0 × 10⁵) / (8.0 × 10³) = 0.25 × 10² = **2.5 × 10¹**

### Adding and Subtracting

Must match exponents first:

> (3.0 × 10⁴) + (5.0 × 10³) = 3.0 × 10⁴ + 0.5 × 10⁴ = **3.5 × 10⁴**

Rule of thumb: if two numbers differ by 2+ orders of magnitude when adding, the smaller one is negligible.

---

## 2. Logarithms

Logarithms are **heavily tested** on the MCAT. They appear in pH, pKa, Henderson-Hasselbalch, decibel calculations, rate law analysis, and Nernst equation.

### Key Values to Memorize

| Value | log₁₀ |
|-------|--------|
| log(1) | 0 |
| log(2) | 0.30 |
| log(3) | 0.48 (~0.5) |
| log(4) | 0.60 |
| log(5) | 0.70 |
| log(6) | 0.78 |
| log(7) | 0.85 |
| log(8) | 0.90 |
| log(9) | 0.95 |
| log(10) | 1.00 |

**Minimum to memorize:** log(2) = 0.3, log(3) = 0.5, log(5) = 0.7. Derive the rest using the rules below.

### The Three Rules (Non-Negotiable)

1. **Product rule:** log(A × B) = log(A) + log(B)
2. **Quotient rule:** log(A/B) = log(A) − log(B)
3. **Power rule:** log(Aⁿ) = n × log(A)

**Derivation examples:**
- log(4) = log(2²) = 2 × log(2) = 2 × 0.3 = **0.6**
- log(6) = log(2 × 3) = log(2) + log(3) = 0.3 + 0.48 = **0.78**
- log(8) = log(2³) = 3 × 0.3 = **0.9**

### pH Calculations Without a Calculator

**pH = −log[H⁺]**

**Method:** Write [H⁺] = a × 10⁻ⁿ → **pH = n − log(a)**

This formula is your best friend. Applies every time:

| [H⁺] | pH calculation | pH |
|------|---------------|-----|
| 3.5 × 10⁻⁴ | 4 − log(3.5) ≈ 4 − 0.54 | **3.46** |
| 5.0 × 10⁻⁸ | 8 − log(5) = 8 − 0.7 | **7.3** |
| 1.0 × 10⁻² | 2 − log(1) = 2 − 0 | **2.0** |

**Shortcut for multiple-choice:** If [H⁺] = a × 10⁻ⁿ, then pH is between (n−1) and n. Larger coefficient a → lower pH within that range. This alone eliminates 2–3 answer choices instantly.

**Going backwards — [H⁺] from pH:**
pH = 4.7 → [H⁺] = 10⁻⁴·⁷ = 10⁻⁵ × 10⁰·³ = 2.0 × 10⁻⁵

Method: split pH into integer and decimal parts. Integer → power of 10. Decimal → antilog (10⁰·³ = 2, 10⁰·⁷ = 5, 10⁰·⁶ = 4, etc.).

### Decibel Calculations

**β = 10 log(I/I₀)** (I₀ = 10⁻¹² W/m²)

Essential shortcuts (memorize these):
- ×10 intensity = **+10 dB**
- ×2 intensity = **+3 dB**
- ×100 = +20 dB | ×1000 = +30 dB

**Worked example:** Intensity increases by factor of 200. ΔdB?
200 = 2 × 10 × 10 → +3 + 10 + 10 = **+23 dB**

**Worked example:** Intensity = 10⁻⁵ W/m². β = 10 × log(10⁻⁵/10⁻¹²) = 10 × log(10⁷) = 10 × 7 = **70 dB**

### Natural Logarithm (ln)

- ln(e) = 1, ln(1) = 0
- **ln = 2.303 × log** (conversion between them)
- ln appears in first-order kinetics, radioactive decay, Nernst equation.
- For MCAT: rarely need to calculate ln values directly. Know when each type of log is used.

---

## 3. Trigonometry

Trig on the MCAT is limited. You need a handful of values and the ability to decompose vectors.

### Standard Angle Values

| Angle | sin | cos | tan |
|-------|-----|-----|-----|
| 0° | 0 | 1 | 0 |
| 30° | 0.50 | 0.87 | 0.58 |
| 45° | 0.71 | 0.71 | 1.00 |
| 60° | 0.87 | 0.50 | 1.73 |
| 90° | 1 | 0 | undefined |

**Memory pattern:** sin goes 0, ½, √2/2, √3/2, 1 from 0° to 90°. Cosine is the same sequence in reverse.

### SOH-CAH-TOA

- **sin θ = opposite/hypotenuse**
- **cos θ = adjacent/hypotenuse**
- **tan θ = opposite/adjacent**

### MCAT Applications

**Inclined planes (most common):** Object on ramp at angle θ:
- Component of gravity along the plane (causing sliding): **mg sin θ**
- Component of gravity into the plane (normal force): **mg cos θ**
Memory trick: at θ = 90° (vertical), full mg acts along the plane. sin(90°) = 1 → parallel component = mg sin θ. ✓

**Projectile motion:** v₀ₓ = v₀ cos θ, v₀ᵧ = v₀ sin θ

**Snell's law:** n₁ sin θ₁ = n₂ sin θ₂

**Vector decomposition:** Any vector at angle θ from x-axis: x-component = magnitude × cos θ, y-component = magnitude × sin θ

---

## 4. Unit Conversions and Metric Prefixes

### Metric Prefixes

| Prefix | Symbol | Power of 10 |
|--------|--------|-------------|
| pico | p | 10⁻¹² |
| nano | n | 10⁻⁹ |
| micro | μ | 10⁻⁶ |
| milli | m | 10⁻³ |
| centi | c | 10⁻² |
| deci | d | 10⁻¹ |
| (base) | — | 10⁰ |
| kilo | k | 10³ |
| mega | M | 10⁶ |
| giga | G | 10⁹ |

Most used: **nano, micro, milli, centi, kilo**. Know the jump between any two without hesitation.

Drill example: How many nanometers in a micrometer? nano = 10⁻⁹, micro = 10⁻⁶ → difference = 3 orders → 1 μm = **1000 nm**.

### Essential Conversions to Memorize

- **1 atm = 760 mmHg = 101,325 Pa ≈ 10⁵ Pa**
- **1 cal = 4.184 J** (round to 4.2 J)
- **1 eV = 1.6 × 10⁻¹⁹ J**
- **0°C = 273 K** (T(K) = T(C) + 273)
- **1 L = 10⁻³ m³ = 1000 mL**
- **1 nm = 10⁻⁹ m | 1 Å = 10⁻¹⁰ m**
- **1 amu = 1.66 × 10⁻²⁷ kg**
- **c = 3.0 × 10⁸ m/s | R = 8.314 J/mol·K = 0.0821 L·atm/mol·K**

### Dimensional Analysis

Multiply by conversion factors (= 1) to cancel unwanted units.

> 5.0 km/hr to m/s:
> 5.0 × (1000 m/1 km) × (1 hr/3600 s) = 5000/3600 = **1.39 m/s**

Shortcut: km/hr to m/s → divide by 3.6.

**Always check final units.** If units are wrong, the calculation is wrong — no exceptions. Free error-checking.

---

## 5. Proportional Reasoning

**The single most valuable math skill on the MCAT.** Many questions solvable in under 30 seconds.

### The Four Key Relationships

**Direct (y = kx):** x doubles → y doubles.
> F = ma. Mass doubles (a constant) → F doubles.

**Inverse (y = k/x):** x doubles → y halves.
> PV = nRT at constant T,n. V doubles → P halves.

**Square (y = kx²):** x doubles → y quadruples (2² = 4).
> KE = ½mv². v doubles → KE quadruples.

**Inverse square (y = k/x²):** x doubles → y becomes ¼.
> Coulomb: F = kq₁q₂/r². r doubles → F becomes ¼.

### MCAT Method

1. Identify the equation connecting the variables.
2. Identify constants (everything not mentioned is constant).
3. Determine relationship type.
4. Apply the factor.

**Common equations and their proportionalities:**

| Equation | Variable changed | Effect |
|----------|-----------------|--------|
| F = ma | m × 2 | F × 2 |
| KE = ½mv² | v × 2 | KE × 4 |
| F = kq₁q₂/r² | r × 2 | F × ¼ |
| Q = πr⁴ΔP/(8ηL) | r × 2 | Q × 16 |
| T = 2π√(L/g) | L × 4 | T × 2 |
| E = hf | f × 2 | E × 2 |
| I = P/(4πr²) | r × 2 | I × ¼ |
| β = 10 log(I/I₀) | I × 10 | β + 10 dB |

---

## 6. Graphical Analysis

### Slope and Intercept

**Slope = rise/run = (y₂ − y₁)/(x₂ − x₁)**

Pick two points on grid intersections for easy math.

**Y-intercept** = value of y when x = 0.

### What Slope and Intercept Mean in Context

| Plot type | y-axis | x-axis | Slope | y-intercept |
|-----------|--------|--------|-------|-------------|
| Lineweaver-Burk | 1/V | 1/[S] | K_m/V_max | 1/V_max |
| Zero-order kinetics | [A] | time | −k | [A]₀ |
| First-order kinetics | ln[A] | time | −k | ln[A]₀ |
| Second-order kinetics | 1/[A] | time | k | 1/[A]₀ |
| Arrhenius plot | ln(k) | 1/T | −E_a/R | ln(A) |
| Beer-Lambert | Absorbance | [concentration] | ε × l | 0 (ideally) |

### Area Under the Curve

The area under a curve = meaningful quantity when axes multiply appropriately:
- **Force vs displacement** → **work**
- **Force vs time** → **impulse**
- **Velocity vs time** → **displacement**
- **Power vs time** → **energy**

### Linearization

**Semi-log plot** (log y vs x): linearizes exponential relationships (y = A · eᵇˣ).

**Log-log plot** (log y vs log x): linearizes power law relationships (y = A · xⁿ). Slope of line = exponent n.

Example: Radioactive decay (N = N₀ · e^(−λt)) → linear on ln(N) vs t plot. Slope = −λ.

---

## 7. Estimation Strategies

### Common Approximations to Memorize

| Value | Approximation |
|-------|--------------|
| √2 | **1.4** |
| √3 | **1.7** |
| π | **3** (or 3.1 for closer work) |
| e | **2.7** |
| 1/3 | **0.33** |
| 2/3 | **0.67** |
| √10 | **3.2** |
| ln(2) | **0.7** |
| ln(10) | **2.3** |

**Bonus:** π² ≈ 10 (actual 9.87) — extremely useful in spring/pendulum problems where g/π² appears.

### Strategy 1: Round Aggressively, Then Adjust

Round to single digits before calculating. Note whether rounding made the answer too high or too low.

> (6.02 × 10²³) × (3.7 × 10⁻⁵) ≈ 6 × 4 × 10¹⁸ = 24 × 10¹⁸ = **2.4 × 10¹⁹**
> (Rounded 3.7 up → actual is slightly less → actual: 2.23 × 10¹⁹. Close enough.)

### Strategy 2: Order-of-Magnitude Reasoning

For multiple-choice: often just need to get the power of 10 right. The answer choices will be spread by factors of 10.

### Strategy 3: Eliminate by Extremes

Before calculating, rule out obviously wrong answers:
- pH = 11 for an acidic solution → eliminate.
- Energy positive for exothermic process → eliminate.
- Velocity exceeds speed of light → eliminate.

### Strategy 4: Use the Answer Choices

Glance at the spread before calculating. If choices are 0.5, 5, 50, 500 → only need order of magnitude. If choices are 4.2, 4.8, 5.3, 5.9 → need more precision. Let answers dictate calculation effort.

### Strategy 5: Break Complex Calculations into Steps

Never compute a 4-variable problem in your head at once. Write intermediate results.

---

## MCAT Strategy Summary

### Practice Priorities

1. **Daily mental math drills:** 5–10 scientific notation problems and pH calculations per day.
2. **Log values flashcards:** log(2), log(3), log(5) → instant recall.
3. **Proportional reasoning:** For every equation you learn, ask "What happens to Y if I double X?"
4. **Graph reading:** For every graph encountered, identify slope/intercept and what they represent before reading questions.
5. **Estimation habit:** Before any calculation, estimate the order of magnitude. If calculation and estimate disagree, find the mistake.

### Quick Reference

**pH = n − log(a)** where [H⁺] = a × 10⁻ⁿ

**Decibels:** ×10 intensity = +10 dB | ×2 = +3 dB

**Log rules:** log(AB) = log A + log B | log(A/B) = log A − log B | log(Aⁿ) = n·log A

**Trig angles:** sin/cos at 0°, 30°, 45°, 60°, 90°

**Key conversions:** 1 atm = 760 mmHg | 0°C = 273 K | 1 eV = 1.6×10⁻¹⁹ J

**Approximations:** √2 = 1.4 | √3 = 1.7 | π = 3 | π² = 10
