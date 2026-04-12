# FC4D: Light and Sound (Physics)

> **Chem/Phys Section** | High-yield for MCAT | Kaplan Physics Ch. 7-9

This guide covers everything you need for wave mechanics, sound, optics, and the electromagnetic spectrum. Optics in particular is a favorite MCAT topic because the questions look harder than they are -- once you internalize the sign conventions and ray diagram logic, these become free points.

---

## 1. Wave Properties

### Fundamental Quantities

Every wave is described by five quantities. Know them cold:

| Quantity | Symbol | Unit | Definition |
|----------|--------|------|------------|
| **Wavelength** | lambda | m | Distance for one full cycle |
| **Frequency** | f | Hz (s^-1) | Cycles per second |
| **Amplitude** | A | varies | Maximum displacement from equilibrium |
| **Period** | T | s | Time for one full cycle |
| **Velocity** | v | m/s | Speed of propagation |

**Key relationships:**

- **T = 1/f** (period and frequency are inverses)
- **v = f * lambda** (the wave equation -- use this constantly)

MCAT tip: If they tell you the speed of a wave is fixed (like the speed of light or sound in a given medium), increasing frequency MUST decrease wavelength, and vice versa. This shows up in Doppler, EM spectrum, and optics questions.

### Transverse vs Longitudinal Waves

**Transverse waves**: Oscillation is **perpendicular** to the direction of travel.
- Examples: light (EM waves), waves on a string, water surface waves (approximately)
- Key feature: can be **polarized** (restrict oscillation to one plane)

**Longitudinal waves**: Oscillation is **parallel** to the direction of travel.
- Examples: sound waves, pressure waves, compression waves in a spring
- Key feature: consist of **compressions** (high pressure) and **rarefactions** (low pressure)
- Cannot be polarized

MCAT trap: Water waves are often described as transverse, but they actually have both transverse and longitudinal components. For MCAT purposes, treat them as transverse unless told otherwise.

### Superposition Principle

When two waves occupy the same space, the resulting displacement is the **algebraic sum** of the individual displacements. This is the basis for all interference phenomena.

**Constructive interference**: Waves in phase (crest meets crest). Amplitudes ADD. Result is a bigger wave.

**Destructive interference**: Waves out of phase by half a wavelength (crest meets trough). Amplitudes SUBTRACT. Result is a smaller wave (or complete cancellation if amplitudes are equal).

Path length difference determines the type:
- Constructive: path difference = m * lambda (m = 0, 1, 2, ...)
- Destructive: path difference = (m + 1/2) * lambda

### Standing Waves

When a wave reflects back on itself (like on a guitar string), the interference pattern creates a **standing wave** -- it looks like the wave is vibrating in place rather than traveling.

**Nodes**: Points of zero displacement (permanent destructive interference). These never move.

**Antinodes**: Points of maximum displacement (permanent constructive interference). These oscillate with maximum amplitude.

### Harmonics -- This Is High-Yield

There are three scenarios the MCAT tests. For each, you need to know the pattern.

#### Strings Fixed at Both Ends (and Open Pipes)

Both ends are **nodes** (for strings) or both ends are **antinodes** (for open pipes). Mathematically, same result:

**lambda_n = 2L / n** where n = 1, 2, 3, 4, ...

**f_n = n * v / (2L)**

- n=1: fundamental (first harmonic) -- one antinode
- n=2: second harmonic (first overtone) -- two antinodes
- **All harmonics are present** (n = 1, 2, 3, 4, ...)

#### Closed Pipes (One End Closed, One End Open)

The closed end is a **node** (air can't move). The open end is an **antinode** (air moves freely).

**lambda_n = 4L / n** where n = 1, 3, 5, 7, ... (ODD only)

**f_n = n * v / (4L)**

**Why only odd harmonics?** Here is the physical reasoning:

The fundamental mode fits exactly one quarter-wavelength in the pipe (node at closed end, antinode at open end). The next mode that satisfies these boundary conditions must have a node at the closed end and an antinode at the open end -- that requires three quarter-wavelengths (3/4 lambda). Then five quarter-wavelengths, and so on. You can never fit an even number of quarter-wavelengths while maintaining a node at one end and an antinode at the other. Sketch it out: draw the pipe, place a node on the left and antinode on the right, and try to fit standing wave patterns. You will see that only odd multiples of quarter-wavelengths work.

MCAT tip: Closed pipes have a **lower fundamental frequency** than open pipes of the same length (because lambda_1 = 4L for closed vs 2L for open, so the wavelength is longer, meaning lower frequency). The MCAT loves asking which pipe produces a lower pitch.

**Quick reference:**

| System | lambda_n | Harmonics present | Boundary conditions |
|--------|----------|-------------------|---------------------|
| String (both ends fixed) | 2L/n | All (n=1,2,3...) | Node-Node |
| Open pipe (both ends open) | 2L/n | All (n=1,2,3...) | Antinode-Antinode |
| Closed pipe (one end closed) | 4L/n | Odd only (n=1,3,5...) | Node-Antinode |

---

## 2. Sound

### Speed of Sound

Sound is a **longitudinal mechanical wave** -- it needs a medium to travel through.

**Speed depends on the medium:**
- Solids > Liquids > Gases (faster in stiffer/denser media)
- In air at room temp: ~340 m/s
- In water: ~1500 m/s
- In steel: ~5000 m/s

**This is the OPPOSITE of light**, which travels fastest in vacuum and slows down in denser media. The MCAT will try to trick you on this.

Why the difference? Sound travels through particle-to-particle collisions, so closer-packed particles transmit vibrations faster. Light is an electromagnetic wave that gets slowed by interactions with electrons in the medium.

Temperature effect: In gases, speed of sound increases with temperature (molecules move faster, transmit vibrations more quickly). For air: v ~ 331 + 0.6T (T in Celsius). You will not need this formula, but know the concept.

### Intensity and Decibels

**Intensity** (I) = power per unit area = P/A, measured in W/m^2.

**Decibel scale:**

**beta = 10 * log10(I / I_0)**

where I_0 = 10^-12 W/m^2 (threshold of human hearing).

#### Calculator-Free dB Tricks (MCAT Favorite)

You WILL see decibel questions. Memorize these relationships:

| Intensity change | dB change |
|-----------------|-----------|
| x2 (double) | +3 dB |
| x10 | +10 dB |
| x100 | +20 dB |
| x1000 | +30 dB |
| /2 (halve) | -3 dB |
| /10 | -10 dB |

**Worked approach:** "The intensity increases by a factor of 200. What is the change in dB?"

Break 200 into factors of 2 and 10: 200 = 2 x 10 x 10.
- x2 = +3 dB
- x10 = +10 dB
- x10 = +10 dB
- Total: +23 dB

Another example: "A sound has intensity 10^-5 W/m^2. What is the dB level?"

beta = 10 * log(10^-5 / 10^-12) = 10 * log(10^7) = 10 * 7 = **70 dB**

MCAT tip: The dB scale is **logarithmic**. A 10 dB increase means 10x more intense. A 20 dB increase means 100x. But perceived loudness roughly doubles every 10 dB -- this is a psych/soc crossover (Weber's law).

### Inverse Square Law

For a point source radiating equally in all directions:

**I = P / (4 * pi * r^2)**

Intensity drops off as **1/r^2**. Double the distance = 1/4 the intensity.

This means: double the distance from a sound source, intensity drops to 1/4, which is a change of -6 dB (two halvings: -3 + -3 = -6).

### Resonance

**Resonance** occurs when an external vibration matches a system's **natural frequency**. This transfers maximum energy to the system, causing large-amplitude oscillations.

Examples: pushing a swing at the right frequency, shattering a glass with a specific pitch, tuning forks.

MCAT relevance: Resonance explains why certain frequencies are amplified in tubes/pipes and why the human ear canal amplifies certain frequencies.

### Beats

When two waves of slightly different frequencies overlap, you hear a pulsation in volume called **beats**.

**f_beat = |f1 - f2|**

If two tuning forks produce 440 Hz and 444 Hz, the beat frequency is 4 Hz (you hear 4 pulses of loudness per second).

MCAT tip: Beat frequency questions are straightforward. Just subtract. They sometimes ask you to identify the unknown frequency: "A 512 Hz fork beats at 3 Hz with an unknown fork. What are the possible frequencies of the unknown?" Answer: 509 Hz or 515 Hz.

### Doppler Effect

The Doppler effect describes the apparent change in frequency when source and observer are in relative motion.

**Conceptual rules (this is what the MCAT actually tests):**

- Source and observer moving **toward** each other: perceived frequency **increases** (higher pitch)
- Source and observer moving **apart**: perceived frequency **decreases** (lower pitch)

**The formula** (for reference, but conceptual understanding matters more):

**f' = f * (v +/- v_observer) / (v -/+ v_source)**

The signs can be confusing. Use this mnemonic: **"toward = together = higher"**. If the observer moves toward the source, ADD v_observer in the numerator (makes f' bigger). If the source moves toward the observer, SUBTRACT v_source in the denominator (makes f' bigger).

**Key distinction the MCAT tests:** Moving the source toward the observer is NOT the same as moving the observer toward the source at the same speed. They produce slightly different perceived frequencies. However, at low speeds relative to the wave speed, they are approximately equal.

### Ultrasound

Ultrasound uses sound waves above human hearing range (>20,000 Hz) for medical imaging.

Key points:
- Higher frequency = better resolution but less penetration
- Reflection occurs at tissue boundaries (impedance mismatch)
- Uses the Doppler effect to measure blood flow velocity
- No ionizing radiation (unlike X-rays and CT scans)

---

## 3. Electromagnetic Spectrum

### The Spectrum (Low to High Energy)

**R**obert **M**akes **I**nteresting **V**ideos **U**sing **X**-tra **G**ear

| Type | Wavelength | Frequency | Energy |
|------|-----------|-----------|--------|
| **Radio** | >1 m | <10^9 Hz | Lowest |
| **Microwave** | 1 mm - 1 m | 10^9 - 10^12 | |
| **Infrared (IR)** | 700 nm - 1 mm | 10^12 - 4x10^14 | |
| **Visible** (ROYGBIV) | 400-700 nm | 4-7.5 x 10^14 | |
| **Ultraviolet (UV)** | 10-400 nm | 7.5x10^14 - 10^16 | |
| **X-ray** | 0.01-10 nm | 10^16 - 10^19 | |
| **Gamma** | <0.01 nm | >10^19 Hz | Highest |

Visible light: **Red** (longest wavelength, lowest frequency/energy, ~700 nm) to **Violet** (shortest wavelength, highest frequency/energy, ~400 nm).

### Photon Energy

**E = hf = hc / lambda**

where h = 6.63 x 10^-34 J*s (Planck's constant), c = 3 x 10^8 m/s.

Higher frequency = shorter wavelength = MORE energy. This relationship is linear -- double the frequency, double the energy.

MCAT tip: All EM waves travel at the speed of light (c = 3 x 10^8 m/s) **in vacuum**. They slow down in media. They are all transverse waves and can be polarized. They do NOT require a medium.

### Important Applications by Type

- **Radio/Microwave**: MRI uses radio waves (NOT ionizing)
- **IR**: Heat sensing, molecular vibrations (detected in IR spectroscopy)
- **UV**: Causes sunburn, fluorescence; enough energy to ionize some molecules
- **X-rays**: Medical imaging, enough energy to ionize atoms
- **Gamma**: Nuclear decay, radiation therapy; most penetrating, most ionizing

---

## 4. Geometric Optics

### Reflection

**Law of reflection: angle of incidence = angle of reflection**

Both angles are measured from the **normal** (the line perpendicular to the surface), NOT from the surface itself. This is an extremely common MCAT trap.

**Specular reflection**: smooth surface, parallel rays reflect in parallel (mirror).
**Diffuse reflection**: rough surface, rays scatter in many directions (paper, walls). You can still see the surface, but no clear image forms.

### Refraction and Snell's Law

When light passes from one medium to another, it changes speed and (usually) changes direction. This is **refraction**.

**n1 * sin(theta1) = n2 * sin(theta2)**

**Index of refraction**: n = c / v (always >= 1; higher n means light goes slower in that medium).

| Medium | n |
|--------|---|
| Vacuum | 1.00 |
| Air | ~1.00 |
| Water | 1.33 |
| Glass | ~1.50 |
| Diamond | 2.42 |

**Bending rules:**
- Light entering a **denser medium** (higher n): slows down, bends **toward** the normal (theta2 < theta1)
- Light entering a **less dense medium** (lower n): speeds up, bends **away** from the normal (theta2 > theta1)

Mnemonic: **"Fast to slow, bend toward. Slow to fast, bend away."** Think of it like a car with one wheel hitting mud first -- that side slows down, so the car turns toward the mud (toward the normal).

### Total Internal Reflection

When light tries to go from a denser to a less dense medium, if the angle of incidence exceeds the **critical angle**, the light reflects entirely back into the denser medium. No refraction occurs.

**sin(theta_c) = n2 / n1** (where n1 > n2)

Requirements:
1. Light must be going from **high n to low n** (dense to less dense)
2. Angle of incidence must **exceed** the critical angle

Applications: fiber optics, the shimmering surface when you look up from underwater, diamond sparkle (diamond has a very low critical angle due to high n, so light bounces around inside).

### Dispersion

Different wavelengths of light have slightly different indices of refraction in a medium. This means they refract at slightly different angles.

- **Shorter wavelengths** (violet/blue) have a **higher n** and bend **more**
- **Longer wavelengths** (red) have a **lower n** and bend **less**

This is why prisms separate white light into a rainbow -- each color refracts by a different amount.

MCAT tip: Dispersion is also why chromatic aberration occurs in lenses (different colors focus at slightly different points).

---

## 5. Mirrors and Lenses

This section is extremely high-yield. The MCAT loves optics problems because they test whether you have actually internalized the sign conventions and relationships. Here is the complete system.

### The Two Equations

**Thin lens/mirror equation:**

**1/f = 1/d_o + 1/d_i**

**Magnification:**

**m = -d_i / d_o = h_i / h_o**

These two equations, combined with sign conventions, solve every MCAT optics problem.

### Sign Conventions (CRITICAL)

This is where students mess up. Learn ONE consistent system and use it every time.

**For mirrors:**
- d_o is **positive** (object is in front of mirror -- always true for real objects)
- d_i is **positive** if the image is in front of the mirror (**real image**, same side as object)
- d_i is **negative** if the image is behind the mirror (**virtual image**)
- f is **positive** for **concave** (converging) mirrors
- f is **negative** for **convex** (diverging) mirrors

**For lenses:**
- d_o is **positive** (object is in front of lens -- always true for real objects)
- d_i is **positive** if the image is on the **opposite side** from the object (**real image**)
- d_i is **negative** if the image is on the **same side** as the object (**virtual image**)
- f is **positive** for **converging** (convex) lenses
- f is **negative** for **diverging** (concave) lenses

**For magnification (both):**
- |m| > 1: image is **enlarged**
- |m| < 1: image is **reduced**
- |m| = 1: same size
- m is **positive**: image is **upright** (same orientation as object)
- m is **negative**: image is **inverted**

### The Four Devices

| Device | Type | f sign | Real or virtual image? |
|--------|------|--------|----------------------|
| **Concave mirror** | Converging | + | Real (if d_o > f) or Virtual (if d_o < f) |
| **Convex mirror** | Diverging | - | Always virtual, upright, reduced |
| **Convex lens** | Converging | + | Real (if d_o > f) or Virtual (if d_o < f) |
| **Concave lens** | Diverging | - | Always virtual, upright, reduced |

MCAT power move: Diverging devices (convex mirror, concave lens) ALWAYS produce **virtual, upright, reduced** images. If you see a diverging device, you can immediately eliminate answer choices that say "real" or "inverted" or "enlarged."

### Ray Diagrams

For converging devices (concave mirror, convex lens), draw these three rays from the top of the object:

1. **Parallel ray**: Comes in parallel to the axis, leaves through the focal point
2. **Focal ray**: Comes in through the focal point, leaves parallel to the axis
3. **Central ray**: For lenses, goes straight through the center. For mirrors, goes to the center of curvature and reflects back on itself.

Where these rays converge = real image location. If they diverge, trace them back to find the virtual image.

### Concave Mirror / Convex Lens -- Image Behavior by Object Distance

This is extremely high-yield. Know what happens at each position:

| Object position | Image position | Image properties |
|----------------|---------------|-----------------|
| d_o > 2f (beyond C) | f < d_i < 2f | Real, inverted, **reduced** |
| d_o = 2f (at C) | d_i = 2f | Real, inverted, **same size** |
| f < d_o < 2f | d_i > 2f | Real, inverted, **enlarged** |
| d_o = f | d_i = infinity | No image (rays go parallel) |
| d_o < f | d_i < 0 (virtual) | Virtual, upright, **enlarged** |

The last case (object inside the focal point) is how a magnifying glass works.

### Lens Power

**P = 1/f** (f in meters, P in diopters)

Converging lens: P > 0. Diverging lens: P < 0.

For lenses in contact: P_total = P1 + P2 + ...

This is relevant to the eye: the cornea and lens combine their powers. Nearsightedness (myopia) is corrected with diverging lenses (negative power). Farsightedness (hyperopia) is corrected with converging lenses (positive power).

### Problem-Solving Strategy for Optics

Follow this systematic approach every time:

1. **Identify the device**: Mirror or lens? Converging or diverging?
2. **Assign the sign of f**: Converging = positive, diverging = negative
3. **Write down d_o**: Usually given, always positive for real objects
4. **Apply the thin lens equation**: 1/d_i = 1/f - 1/d_o
5. **Interpret the sign of d_i**: Positive = real, negative = virtual
6. **Calculate magnification**: m = -d_i/d_o
7. **Interpret m**: Positive = upright, negative = inverted; |m| gives size ratio

**Worked approach:** "An object is placed 30 cm from a converging lens with focal length 20 cm. Describe the image."

- Converging lens: f = +20 cm, d_o = +30 cm
- 1/d_i = 1/20 - 1/30 = 3/60 - 2/60 = 1/60
- d_i = +60 cm (positive, so real image, on opposite side of lens)
- m = -60/30 = -2 (negative, so inverted; magnitude 2, so image is twice the height)
- Answer: Real, inverted, enlarged (2x), located 60 cm from lens on the far side

**Worked approach:** "An object is placed 10 cm from a convex mirror with focal length magnitude 20 cm."

- Convex mirror: f = -20 cm, d_o = +10 cm
- 1/d_i = 1/(-20) - 1/10 = -1/20 - 2/20 = -3/20
- d_i = -20/3 ~ -6.7 cm (negative, so virtual, behind mirror)
- m = -(-6.7)/10 = +0.67 (positive = upright, less than 1 = reduced)
- Answer: Virtual, upright, reduced -- exactly what we expect from a diverging device

---

## 6. Wave Optics (Kaplan Gap -- Supplement This)

This topic is under-covered in some Kaplan editions but is testable. Know the concepts and key equations.

### Diffraction

When a wave encounters an obstacle or slit comparable in size to its wavelength, it **bends around** the obstacle. This is diffraction.

Key principle: Significant diffraction occurs when the slit width (or obstacle size) is on the order of the wavelength. Much larger openings produce minimal diffraction.

### Young's Double-Slit Experiment

This is the classic demonstration that light behaves as a wave.

Setup: Light passes through two narrow slits separated by distance d. An interference pattern of bright and dark fringes appears on a distant screen.

**Bright fringes (constructive interference):**

**d * sin(theta) = m * lambda** (m = 0, 1, 2, 3, ...)

**Dark fringes (destructive interference):**

**d * sin(theta) = (m + 1/2) * lambda**

The central bright fringe (m=0) is the brightest. Fringes get dimmer farther from center.

**What happens when you change variables:**
- **Increase wavelength (redder light)**: fringes spread apart (wider spacing)
- **Increase slit separation d**: fringes get closer together (narrower spacing)
- **Increase distance to screen**: fringes spread apart (but this doesn't change the angles)

MCAT tip: The MCAT is more likely to ask conceptual questions about how changing wavelength or slit separation affects the pattern than to ask you to calculate exact positions.

### Single-Slit Diffraction

For a single slit of width a, the dark fringes (minima) occur at:

**a * sin(theta) = m * lambda** (m = 1, 2, 3, ... -- note m != 0)

The central maximum is **twice as wide** as the other maxima. This is a common MCAT fact.

### Thin-Film Interference

Thin-film interference (soap bubbles, oil slicks, anti-reflective coatings) involves light reflecting off the top and bottom surfaces of a thin film. The two reflected beams can interfere constructively or destructively.

Two effects determine whether interference is constructive or destructive:

**1. Path length difference**: Light reflecting from the bottom surface travels an extra distance of **2t** (where t is the film thickness) through the film. The effective path difference is **2nt** (because the wavelength is shorter inside the film by a factor of n).

**2. Phase shifts at reflection**: A phase shift of half a wavelength (180 degrees) occurs when light reflects off a surface with a **higher** index of refraction (going from low n to high n). No phase shift occurs when reflecting off a surface with a lower n.

**How to solve thin-film problems:**

Step 1: Count the phase shifts. Check each reflecting surface:
- Top surface reflection: Is the film's n higher than the medium above? If yes, phase shift.
- Bottom surface reflection: Is the medium below the film higher n than the film? If yes, phase shift.

Step 2: Determine the net phase shift:
- If both reflections shift (or neither shifts): the phase shifts cancel. Constructive interference when 2nt = m * lambda (m = 0, 1, 2, ...).
- If only one reflection shifts: there is a net half-wavelength shift. Constructive interference when 2nt = (m + 1/2) * lambda.

**Worked approach:** "An oil film (n = 1.5) floats on water (n = 1.33). What is the minimum thickness for constructive reflection of 600 nm light?"

- Top reflection (air to oil): n_oil > n_air, so **phase shift** occurs
- Bottom reflection (oil to water): n_water < n_oil, so **no phase shift**
- One phase shift total: constructive when 2nt = (m + 1/2) * lambda
- Minimum thickness: m = 0, so 2(1.5)(t) = (0.5)(600 nm)
- 3t = 300 nm, t = **100 nm**

### Polarization

Only **transverse waves** can be polarized (this is why sound cannot be polarized).

**Unpolarized light** oscillates in all directions perpendicular to propagation. A **polarizer** transmits only the component along its transmission axis.

**Malus's Law**: After passing through a polarizer, the transmitted intensity is:

**I = I_0 * cos^2(theta)**

where theta is the angle between the light's polarization direction and the polarizer's transmission axis.

Special cases:
- theta = 0: I = I_0 (all light passes through)
- theta = 90: I = 0 (no light passes -- crossed polarizers)
- Unpolarized light through first polarizer: I = I_0 / 2 (regardless of orientation)

MCAT tip: If unpolarized light passes through polarizer 1 (intensity halves) then polarizer 2 at angle theta to the first (apply Malus's law), the total transmitted intensity is I = (I_0/2) * cos^2(theta).

**Brewster's angle**: When light reflects off a surface at Brewster's angle, the reflected light is completely polarized. tan(theta_B) = n2/n1. Low-yield but occasionally appears.

---

## 7. Photoelectric Effect

### The Setup

When light shines on a metal surface, electrons can be ejected. This is the photoelectric effect, and it provided key evidence for the particle nature of light.

### The Equation

**KE_max = hf - phi**

where:
- KE_max = maximum kinetic energy of ejected electrons
- h = Planck's constant (6.63 x 10^-34 J*s)
- f = frequency of incident light
- phi = **work function** (minimum energy needed to eject an electron, specific to the metal)

### Threshold Frequency

**f_0 = phi / h**

Below this frequency, **no electrons are ejected regardless of intensity**. This was the crucial observation that classical wave theory could not explain.

### Key Concepts the MCAT Tests

1. **Increasing intensity** (brighter light at same frequency): More photons hit the surface, so **more electrons** are ejected (higher current), but each electron has the **same KE_max**. Intensity does NOT change the energy per photon.

2. **Increasing frequency** (above threshold): Each photon has more energy, so KE_max **increases**. The number of electrons ejected stays the same if intensity is constant.

3. **Below threshold frequency**: Zero electrons ejected. Does not matter how bright the light is. A billion low-energy photons cannot combine their energy to eject one electron.

4. **Ejection is instantaneous**: No time delay, even at low intensity. This contradicts the wave model (which would predict energy accumulates gradually).

MCAT trap: Students confuse intensity and frequency effects. Intensity = number of photons per second. Frequency = energy per photon. These are independent variables.

### Wave-Particle Duality

Light behaves as a wave (interference, diffraction, polarization) AND as a particle (photoelectric effect, Compton scattering).

**de Broglie wavelength**: All matter has wave-like properties.

**lambda = h / p = h / (mv)**

This is mostly relevant for electrons and subatomic particles (macroscopic objects have negligibly small wavelengths). The MCAT may ask you to recognize that increasing a particle's momentum decreases its wavelength.

---

## MCAT Strategy Summary

### Top 5 Most Testable Topics in This Section

1. **Thin lens/mirror equation + sign conventions** -- practice until automatic
2. **Decibel calculations** -- the doubling/10x shortcuts
3. **Snell's law and total internal reflection** -- qualitative and quantitative
4. **Double-slit interference** -- what changes the fringe pattern
5. **Photoelectric effect** -- intensity vs frequency effects

### Common Traps to Avoid

- Measuring angles from the surface instead of the normal (reflection, refraction)
- Forgetting that sound is faster in denser media but light is slower
- Getting sign conventions backwards for mirrors vs lenses
- Confusing intensity (number of photons) with frequency (energy per photon) in the photoelectric effect
- Forgetting that closed pipes only have odd harmonics
- Applying total internal reflection in the wrong direction (only works going from high n to low n)

### Quick Equation Reference

| Equation | When to use |
|----------|-------------|
| v = f * lambda | Any wave problem |
| T = 1/f | Period-frequency conversion |
| beta = 10 * log(I/I_0) | Decibel calculations |
| I = P/(4*pi*r^2) | Intensity from point source |
| f_beat = \|f1 - f2\| | Beat frequency |
| n1*sin(theta1) = n2*sin(theta2) | Refraction (Snell's law) |
| sin(theta_c) = n2/n1 | Critical angle for TIR |
| 1/f = 1/d_o + 1/d_i | Mirrors and thin lenses |
| m = -d_i/d_o | Magnification |
| P = 1/f | Lens power in diopters |
| d*sin(theta) = m*lambda | Double-slit bright fringes |
| E = hf = hc/lambda | Photon energy |
| KE_max = hf - phi | Photoelectric effect |
| lambda = h/(mv) | de Broglie wavelength |
| I = I_0*cos^2(theta) | Malus's law (polarization) |
