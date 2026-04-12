# CP Deep Dive: Math and Data Skills (No Calculator)

There is **no calculator on the MCAT**. Every quantitative question must be solved by hand or by estimation. This is not a weakness -- it is a design feature. The test rewards students who can think proportionally, estimate confidently, and eliminate wrong answers without grinding through arithmetic. Master these skills and the CP section becomes significantly less stressful.

---

## 1. Scientific Notation

Scientific notation is the language of MCAT math. You will use it in every single quantitative problem. If you are slow with it, you are slow on the entire section.

### Multiplying

Multiply the coefficients, add the exponents.

> **(3.0 x 10^4) x (2.0 x 10^5)**
> Coefficients: 3.0 x 2.0 = 6.0
> Exponents: 4 + 5 = 9
> Answer: **6.0 x 10^9**

When the coefficient product exceeds 10, shift:

> **(4.0 x 10^3) x (5.0 x 10^6)**
> Coefficients: 4.0 x 5.0 = 20
> Exponents: 3 + 6 = 9
> 20 x 10^9 = **2.0 x 10^10**

### Dividing

Divide the coefficients, subtract the exponents (numerator minus denominator).

> **(8.0 x 10^6) / (2.0 x 10^2)**
> Coefficients: 8.0 / 2.0 = 4.0
> Exponents: 6 - 2 = 4
> Answer: **4.0 x 10^4**

When the coefficient division gives something less than 1:

> **(2.0 x 10^5) / (8.0 x 10^3)**
> Coefficients: 2.0 / 8.0 = 0.25
> Exponents: 5 - 3 = 2
> 0.25 x 10^2 = **2.5 x 10^1 = 25**

### Adding and Subtracting

You **must** match the exponents first.

> **(3.0 x 10^4) + (5.0 x 10^3)**
> Rewrite: 3.0 x 10^4 + 0.5 x 10^4 = **3.5 x 10^4**

Rule of thumb on the MCAT: if two numbers differ by 2+ orders of magnitude and you are adding, the smaller one is negligible. This saves time.

### Quick Conversion Trick

To convert between standard form and scientific notation, count decimal jumps. Moving the decimal left increases the exponent; moving right decreases it.

> 0.00045 = 4.5 x 10^-4 (decimal moved 4 places right)
> 67,000 = 6.7 x 10^4 (decimal moved 4 places left)

---

## 2. Logarithms

Logarithms are **heavily tested**. They appear in pH, pKa, Henderson-Hasselbalch, decibel calculations, rate law analysis, and Nernst equation problems. You cannot afford to be slow here.

### Key Values to Memorize

| Value | log (base 10) |
|-------|--------------|
| log(1) | 0 |
| log(2) | 0.30 |
| log(3) | 0.48 (round to 0.5) |
| log(4) | 0.60 |
| log(5) | 0.70 |
| log(6) | 0.78 |
| log(7) | 0.85 |
| log(8) | 0.90 |
| log(9) | 0.95 |
| log(10) | 1.00 |

You do not need to memorize all of these from day one. **At minimum, know log(2) = 0.3, log(3) = 0.5, log(5) = 0.7.** The rest can be derived from log rules.

### The Three Rules

These are non-negotiable. You must know them cold.

1. **Product rule:** log(A x B) = log(A) + log(B)
2. **Quotient rule:** log(A / B) = log(A) - log(B)
3. **Power rule:** log(A^n) = n x log(A)

Derivation example: log(4) = log(2^2) = 2 x log(2) = 2 x 0.3 = 0.6. You just derived log(4) from knowing log(2).

Similarly: log(6) = log(2 x 3) = log(2) + log(3) = 0.3 + 0.48 = 0.78.

### pH Calculations Without a Calculator

This is the most common log application on the MCAT. The method:

**pH = -log[H+]**

**Step 1:** Write [H+] in the form a x 10^-n.
**Step 2:** Apply: pH = -log(a x 10^-n) = -[log(a) + log(10^-n)] = -log(a) - (-n) = **n - log(a)**

This formula is your best friend: **pH = n - log(a)**, where [H+] = a x 10^-n.

#### Worked Example 1

> [H+] = 3.5 x 10^-4
> pH = 4 - log(3.5)
> log(3.5) is between log(3) = 0.48 and log(4) = 0.60, roughly 0.54
> pH = 4 - 0.54 = **3.46**
> Quick check: coefficient > 1 pushes pH below the exponent. Makes sense.

#### Worked Example 2

> [H+] = 5.0 x 10^-8
> pH = 8 - log(5) = 8 - 0.7 = **7.3**

#### Worked Example 3

> [H+] = 1.0 x 10^-2
> pH = 2 - log(1) = 2 - 0 = **2.0** (this is the easy case)

**Shortcut for multiple-choice:** If [H+] = a x 10^-n, then pH is between (n-1) and n. The larger the coefficient a, the lower the pH within that range. This alone can eliminate 2-3 answer choices instantly.

### Going Backwards: [H+] from pH

If pH = 4.7, then [H+] = 10^-4.7 = 10^-5 x 10^0.3 = 2.0 x 10^-5.

Method: split the pH into integer and decimal parts. The integer gives the 10^-n, and the decimal gives the coefficient via the antilog table (10^0.3 = 2, 10^0.7 = 5, etc.).

### Decibel Calculations

**dB = 10 log(I / I_0)**

The key relationships:
- Every **10x increase** in intensity = **+10 dB**
- Every **2x increase** in intensity = **+3 dB**
- Every **100x increase** = **+20 dB**

> A sound is 1000x more intense than the reference. How many dB?
> 10 log(1000) = 10 x 3 = **30 dB**

> A sound increases from 50 dB to 80 dB. By what factor did the intensity increase?
> Change = 30 dB = 10 x 3, so log(I_2/I_1) = 3, meaning intensity increased by **10^3 = 1000x**.

### Natural Logarithm (ln)

- **ln(e) = 1**, **ln(1) = 0**
- **ln = 2.303 x log** (use this to convert between the two)
- ln appears in first-order kinetics (ln[A] vs. t), radioactive decay, and the Nernst equation.
- For the MCAT, you rarely need to calculate ln values directly. Know the relationship and when each type of log is used.

---

## 3. Trigonometry

Trig on the MCAT is not calculus-level. You need a handful of values and the ability to decompose vectors on inclined planes and in optics problems.

### Values You Must Know

| Angle | sin | cos | tan |
|-------|-----|-----|-----|
| 0 deg | 0 | 1 | 0 |
| 30 deg | 0.50 | 0.87 | 0.58 |
| 45 deg | 0.71 | 0.71 | 1.00 |
| 60 deg | 0.87 | 0.50 | 1.73 |
| 90 deg | 1 | 0 | undefined |

Mnemonics: sin goes 0, 1/2, root2/2, root3/2, 1 as you go from 0 to 90. Cosine is the same sequence in reverse.

### SOH-CAH-TOA

- **sin(theta) = opposite / hypotenuse**
- **cos(theta) = adjacent / hypotenuse**
- **tan(theta) = opposite / adjacent**

### Where Trig Shows Up on the MCAT

**Inclined planes** (most common): For an object on a ramp at angle theta to the horizontal:
- Component of gravity along the plane (causing sliding): **mg sin(theta)**
- Component of gravity into the plane (normal force): **mg cos(theta)**

Memory trick: a steeper angle means more force pulling the object down the ramp. At theta = 90 degrees (vertical), the full mg acts along the "plane." sin(90) = 1. This confirms the sin component is along the plane.

**Snell's Law:** n_1 sin(theta_1) = n_2 sin(theta_2). You need to be comfortable solving for angles when given index values and a known angle.

**Projectile motion:** Horizontal component of velocity = v cos(theta). Vertical component = v sin(theta).

**Vector decomposition generally:** Any vector at angle theta from the x-axis has x-component = magnitude x cos(theta) and y-component = magnitude x sin(theta).

### Inverse Trig (Rare)

You almost never need to compute arcsin, arccos, or arctan on the MCAT. If a question asks for an angle, the answer choices will correspond to the standard angles (30, 45, 60) or you will recognize the ratio.

---

## 4. Unit Conversions and Metric Prefixes

### Metric Prefixes

| Prefix | Symbol | Power of 10 |
|--------|--------|-------------|
| pico | p | 10^-12 |
| nano | n | 10^-9 |
| micro | mu | 10^-6 |
| milli | m | 10^-3 |
| centi | c | 10^-2 |
| deci | d | 10^-1 |
| (base) | -- | 10^0 |
| kilo | k | 10^3 |
| mega | M | 10^6 |
| giga | G | 10^9 |

The ones you will use most: **nano, micro, milli, centi, kilo**. Know the jump between any two without hesitation.

Quick drill: how many nanometers in a micrometer? Nano is 10^-9, micro is 10^-6. Difference = 3 orders of magnitude. So 1 micrometer = 10^3 nm = **1000 nm**.

### Common Conversions to Memorize

- **1 atm = 760 mmHg = 101.3 kPa = 101,300 Pa**
- **1 cal = 4.184 J** (round to 4.2 J for estimation)
- **1 eV = 1.6 x 10^-19 J**
- **0 degrees C = 273 K** (so T(K) = T(C) + 273)
- **1 L = 10^-3 m^3 = 1000 mL = 1000 cm^3**
- **1 nm = 10^-9 m**
- **1 angstrom = 10^-10 m**
- **1 amu = 1.66 x 10^-27 kg**
- **Speed of light: c = 3.0 x 10^8 m/s**
- **R = 8.314 J/(mol*K) = 0.0821 L*atm/(mol*K)**

### Dimensional Analysis

This is the systematic approach: multiply by conversion factors that equal 1 so that unwanted units cancel.

> Convert 5.0 km/hr to m/s:
> 5.0 km/hr x (1000 m / 1 km) x (1 hr / 3600 s)
> = 5000 / 3600 m/s
> = **1.39 m/s**

Shortcut for km/hr to m/s: **divide by 3.6**. For m/s to km/hr: multiply by 3.6.

On the MCAT, always check that your final answer has the right units. If the units are wrong, your calculation is wrong -- no exceptions. This is a free error-checking tool.

---

## 5. Graphical Analysis

The MCAT loves graph-based questions. You need to extract quantitative information from figures quickly.

### Slope and Intercept

**Slope = rise / run = (y_2 - y_1) / (x_2 - x_1)**

Pick two points that fall on grid intersections for easy math. Do not try to use points that require you to estimate coordinates.

**Y-intercept** = the value of y when x = 0. Read it directly off the graph if the axis is shown.

### What Slope and Intercept Mean in Context

| Plot Type | y-axis | x-axis | Slope | y-intercept |
|-----------|--------|--------|-------|-------------|
| **Lineweaver-Burk** | 1/V | 1/[S] | K_m / V_max | 1/V_max |
| **Zero-order kinetics** | [A] | time | -k | [A]_0 |
| **First-order kinetics** | ln[A] | time | -k | ln[A]_0 |
| **Second-order kinetics** | 1/[A] | time | k | 1/[A]_0 |
| **Arrhenius plot** | ln(k) | 1/T | -E_a/R | ln(A) |
| **Beer-Lambert** | Absorbance | concentration | molar absorptivity x path length (epsilon x l) | 0 (ideally) |

Know these cold. The MCAT will show you a graph and ask what the slope represents, or how a change in conditions shifts the line.

### Area Under the Curve

The area under a curve matters when the axes multiply to give a meaningful quantity:
- **Force vs. displacement** graph: area = **work**
- **Force vs. time** graph: area = **impulse**
- **Velocity vs. time** graph: area = **displacement**
- **Power vs. time** graph: area = **energy**

For rectangular or triangular shapes, calculate the area geometrically. For curves, estimate by counting grid squares or approximating with rectangles.

### Linearization Strategies

Many real-world relationships are not linear, but the MCAT may present them as linearized plots:

- **Semi-log plot** (log y vs. x): linearizes **exponential** relationships (y = A * e^(bx)). If data forms a straight line on a semi-log plot, the underlying relationship is exponential.
- **Log-log plot** (log y vs. log x): linearizes **power law** relationships (y = A * x^n). The slope of the line on a log-log plot gives the exponent n.

Example: Radioactive decay (N = N_0 * e^(-lambda*t)) becomes linear when you plot ln(N) vs. t. The slope is -lambda.

---

## 6. Proportional Reasoning

This is arguably the **single most valuable math skill** on the MCAT. Many questions can be answered in under 30 seconds using proportional reasoning instead of full calculations.

### The Four Key Relationships

**Direct proportion: y = kx**
If x doubles, y doubles. If x triples, y triples.
> Example: F = ma. If mass doubles (acceleration constant), force doubles.

**Inverse proportion: y = k/x**
If x doubles, y halves. If x triples, y becomes 1/3.
> Example: PV = nRT at constant T and n. If volume doubles, pressure halves.

**Square proportion: y = kx^2**
If x doubles, y quadruples (2^2 = 4). If x triples, y increases 9x (3^2 = 9).
> Example: KE = 1/2 mv^2. If velocity doubles, kinetic energy quadruples.

**Inverse square: y = k/x^2**
If x doubles, y becomes 1/4. If x triples, y becomes 1/9.
> Examples: Coulomb's law (F = kq_1q_2/r^2), gravitational force, sound intensity with distance.

### The MCAT Proportional Reasoning Method

When you see a question like "What happens to X when Y changes?":

1. **Identify the equation** connecting X and Y.
2. **Identify which variables are held constant** (everything not mentioned is constant).
3. **Determine the relationship type** (direct, inverse, square, inverse square).
4. **Apply the factor.**

#### Worked Example 1

> The radius of a blood vessel doubles. What happens to flow rate? (Poiseuille's law: Q = pi*r^4*deltaP / 8*eta*L)

Flow rate is proportional to r^4. If r doubles:
Q_new = k(2r)^4 = k * 16 * r^4 = 16 * Q_old.
Flow rate increases by a factor of **16**.

#### Worked Example 2

> The distance between two charges is tripled. What happens to the electrostatic force?

F = kq_1q_2/r^2. Force is proportional to 1/r^2. If r triples:
F_new = k/(3r)^2 = k/(9r^2) = F_old / 9.
Force decreases to **1/9** of its original value.

#### Worked Example 3

> A pendulum's length is quadrupled. What happens to its period?

T = 2*pi*sqrt(L/g). Period is proportional to sqrt(L). If L quadruples:
T_new = k*sqrt(4L) = k * 2 * sqrt(L) = 2 * T_old.
Period **doubles**.

### Common Equations and Their Proportionalities

| Equation | Variable Changed | Effect on Result |
|----------|-----------------|-----------------|
| F = ma | m doubles | F doubles |
| KE = 1/2 mv^2 | v doubles | KE quadruples |
| F = kq_1q_2/r^2 | r doubles | F becomes 1/4 |
| PV = nRT | V doubles (const T,n) | P halves |
| Q = pi*r^4*dP/(8*eta*L) | r doubles | Q x 16 |
| T = 2*pi*sqrt(L/g) | L x 4 | T doubles |
| E = hf | f doubles | E doubles |
| I = P/(4*pi*r^2) | r doubles | I becomes 1/4 |

---

## 7. Common Approximations

Memorize these. They eliminate calculation steps and let you estimate faster.

| Value | Approximation | Exact |
|-------|--------------|-------|
| sqrt(2) | **1.4** | 1.414 |
| sqrt(3) | **1.7** | 1.732 |
| pi | **3** (or 3.1 for closer work) | 3.14159 |
| e | **2.7** | 2.718 |
| 1/3 | **0.33** | 0.3333... |
| 2/3 | **0.67** | 0.6667... |
| 1/7 | **0.14** | 0.1428... |
| 1/9 | **0.11** | 0.1111... |
| sqrt(10) | **3.2** | 3.162 |
| ln(2) | **0.7** | 0.693 |
| ln(10) | **2.3** | 2.303 |

### Useful Derived Approximations

- **pi^2 = ~10** (actual 9.87). This is extremely useful in spring/pendulum problems where g/pi^2 appears.
- **sqrt(2)/2 = 0.71** (sin 45 = cos 45)
- **sqrt(3)/2 = 0.87** (sin 60 = cos 30)

---

## 8. Estimation Strategies

The MCAT answer choices are typically spread far enough apart that estimation gets you to the right answer without exact calculation. Here is how to exploit that.

### Strategy 1: Round Aggressively, Then Adjust

Round numbers to single digits or easy fractions before calculating. Then note whether your rounding made the answer slightly too high or too low.

> Calculate: (6.02 x 10^23) x (3.7 x 10^-5)
> Round: 6 x 4 = 24, exponent = 23 + (-5) = 18
> Estimate: ~24 x 10^18 = **2.4 x 10^19**
> Adjustment: we rounded 3.7 up to 4 (overestimate), so actual is slightly less.
> Actual: 2.23 x 10^19. Close enough.

### Strategy 2: Order-of-Magnitude Reasoning

Sometimes you do not need the coefficient at all. Just get the power of 10 right.

> If a question asks for the energy of a visible light photon and the answer choices are:
> A) 3 x 10^-21 J, B) 3 x 10^-19 J, C) 3 x 10^-17 J, D) 3 x 10^-15 J
>
> You know E = hf. Visible light is ~5 x 10^14 Hz. h = 6.6 x 10^-34.
> Exponents: -34 + 14 = -20. Coefficient: ~6 x 5 = 30 = 3 x 10^1.
> Total: 3 x 10^(-20+1) = 3 x 10^-19.
> Answer: **B**.
>
> You never needed the exact frequency or Planck's constant. The orders of magnitude did the work.

### Strategy 3: Eliminate by Extremes

Before calculating, ask: can I rule out any answers immediately?

- If a pH answer is 11 but the solution is clearly acidic, cross it out.
- If an energy answer is positive but the process is exothermic, cross it out.
- If a velocity answer exceeds the speed of light, cross it out.
- If a percentage answer exceeds 100%, cross it out.

This sounds obvious, but under time pressure, students pick trap answers that fail basic sanity checks. Always do a 3-second gut check.

### Strategy 4: Use the Answer Choices

Glance at the answer spread before calculating. If the choices are 0.5, 5, 50, and 500, you only need to get the order of magnitude right. If the choices are 4.2, 4.8, 5.3, and 5.9, you need more precision. Let the answers dictate how carefully you calculate.

### Strategy 5: Break Complex Calculations into Steps

Never try to do a 4-variable calculation in your head at once. Write intermediate results in the margin.

> Calculate the gravitational force between two 70 kg people standing 1 m apart.
> F = G*m_1*m_2/r^2
> G = 6.67 x 10^-11
>
> Step 1: m_1 * m_2 = 70 x 70 = 4900, round to 5 x 10^3
> Step 2: G * 5 x 10^3 = 6.67 x 10^-11 x 5 x 10^3 = ~33 x 10^-8 = 3.3 x 10^-7
> Step 3: Divide by r^2 = 1^2 = 1
> Answer: **~3.3 x 10^-7 N**
>
> This is a tiny force, which makes physical sense for gravity between two people. Sanity check passed.

---

## Putting It All Together: A Full Practice Problem

> A solution has [OH-] = 4.0 x 10^-5 M. What is the pH?

**Step 1:** Find pOH.
pOH = -log(4.0 x 10^-5) = 5 - log(4)
log(4) = log(2^2) = 2 x 0.3 = 0.6
pOH = 5 - 0.6 = **4.4**

**Step 2:** Find pH.
pH + pOH = 14
pH = 14 - 4.4 = **9.6**

**Step 3:** Sanity check. OH- concentration of 10^-5 is basic (pOH < 7, so pH > 7). pH = 9.6 is basic. Confirmed.

Total time: ~20 seconds. No calculator needed.

---

## Practice Recommendations

1. **Do 5-10 mental math drills per day** during content review. Pick random scientific notation multiplications/divisions and pH problems. Time yourself.
2. **Flash cards for log values.** Drill log(2), log(3), log(5), log(7) until they are instant recall.
3. **Proportional reasoning practice.** For every equation you learn, ask yourself: "What happens to Y if I double X?" Run through the common equations above.
4. **Practice reading graphs.** When you encounter graphs in Kaplan or practice passages, always identify the slope, intercept, and what they represent before reading the questions.
5. **Estimation habit.** Before you calculate anything, estimate the order of magnitude. Then calculate. If they disagree, find your mistake.

These skills compound. Investing 15 minutes a day in math fluency during content review will pay massive dividends in timed practice later.