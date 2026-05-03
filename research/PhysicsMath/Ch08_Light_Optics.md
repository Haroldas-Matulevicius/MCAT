# Physics & Math Chapter 8 — Light & Optics

Scope: Electromagnetic spectrum; photon energy; reflection (law of reflection, specular vs diffuse); refraction (Snell's law, index of refraction, dispersion); total internal reflection; mirrors (concave/convex, sign conventions, thin lens/mirror equation); lenses (converging/diverging, same equations); lens power (diopters); diffraction (single-slit, double-slit, Young's experiment); thin-film interference; polarization (Malus's law, Brewster's angle).

**Section:** Chemical/Physical (CP) — Physics & Math
**Book:** Kaplan Physics and Math Strategies 2024 — Chapter 8
**AAMC FC mapping:** FC4D (Sound, light, and EM radiation)
**Yield:** Very high. Optics (mirrors and lenses) is a major MCAT topic — sign conventions and the thin lens equation must be mastered. EM spectrum, Snell's law, and polarization are also frequently tested.

---

## 1. Electromagnetic Spectrum

### The Spectrum (Low Energy → High Energy)

Mnemonic: **R**obert **M**akes **I**nteresting **V**ideos **U**sing **X**-tra **G**ear

| Type | Wavelength | Frequency | Energy |
|------|-----------|-----------|--------|
| **Radio** | >1 m | <10⁹ Hz | Lowest |
| **Microwave** | 1 mm – 1 m | 10⁹ – 10¹² Hz | |
| **Infrared (IR)** | 700 nm – 1 mm | 10¹² – 4×10¹⁴ Hz | |
| **Visible** (ROYGBIV) | 400 – 700 nm | 4 – 7.5×10¹⁴ Hz | |
| **Ultraviolet (UV)** | 10 – 400 nm | 7.5×10¹⁴ – 10¹⁶ Hz | |
| **X-ray** | 0.01 – 10 nm | 10¹⁶ – 10¹⁹ Hz | |
| **Gamma** | <0.01 nm | >10¹⁹ Hz | Highest |

Visible: **Red** (longest λ, lowest f/E, ~700 nm) → **Violet** (shortest λ, highest f/E, ~400 nm).

### Photon Energy

**E = hf = hc/λ**

Where h = 6.63 × 10⁻³⁴ J·s (Planck's constant), c = 3 × 10⁸ m/s.

Higher frequency = shorter wavelength = MORE energy. Linear relationship: double frequency → double energy.

**Applications by type:**
- **Radio/Microwave:** MRI uses radio waves (NOT ionizing; no DNA damage)
- **IR:** Heat sensing, molecular vibrations, IR spectroscopy
- **UV:** Causes sunburn; enough energy to ionize some molecules; fluorescence
- **X-rays:** Medical imaging; ionizing (damages DNA)
- **Gamma:** Nuclear decay, radiation therapy; most penetrating, most ionizing

**All EM waves:** travel at c = 3×10⁸ m/s in vacuum, are transverse waves, can be polarized, do NOT require a medium.

---

## 2. Reflection

### Law of Reflection

**Angle of incidence = Angle of reflection**

Both angles measured from the **normal** (perpendicular to surface), NOT from the surface. This is an extremely common MCAT trap.

**Specular reflection:** Smooth surface, parallel rays reflect in parallel (mirror).
**Diffuse reflection:** Rough surface, rays scatter in many directions (paper, walls). You can see the surface but no clear image.

---

## 3. Refraction and Snell's Law

When light passes from one medium to another, it changes speed and (usually) direction.

**Index of refraction: n = c/v** (always ≥ 1; higher n = light travels slower)

| Medium | n |
|--------|---|
| Vacuum | 1.00 |
| Air | ~1.00 |
| Water | 1.33 |
| Glass | ~1.50 |
| Diamond | 2.42 |

**Snell's Law:** n₁ sin θ₁ = n₂ sin θ₂

**Bending rules:**
- Into **denser medium** (higher n): slows down, bends **toward** normal (θ₂ < θ₁)
- Into **less dense medium** (lower n): speeds up, bends **away** from normal (θ₂ > θ₁)

Mnemonic: **"Fast to slow, bend toward. Slow to fast, bend away."** Think of a car where one wheel hits mud first — that side slows, car turns toward the mud (toward normal).

### Dispersion

Different wavelengths have different indices of refraction in a medium → refract at slightly different angles.
- Shorter wavelengths (violet/blue): higher n → bend **more**
- Longer wavelengths (red): lower n → bend **less**

Prisms separate white light into rainbows. Chromatic aberration in lenses: different colors focus at slightly different points.

### Total Internal Reflection (TIR)

When light goes from denser to less dense medium, if the angle of incidence exceeds the **critical angle**, all light reflects back into the denser medium.

**sin θ_c = n₂/n₁** (where n₁ > n₂)

Requirements:
1. Light going from **high n to low n** (denser to less dense medium)
2. Angle of incidence > critical angle

**Applications:** Fiber optics, diamonds (high n → low critical angle → light bounces around inside → sparkle), shimmering surface when viewed from underwater.

---

## 4. Mirrors and Lenses — HIGH YIELD

This section is extremely high-yield. The MCAT loves optics problems. Once you internalize the sign conventions and relationships, these become free points.

### The Two Core Equations

**Thin lens/mirror equation:**

**1/f = 1/d_o + 1/d_i**

**Magnification:**

**m = −d_i/d_o = h_i/h_o**

### Sign Conventions — CRITICAL

**For mirrors:**
- d_o is **positive** (object in front of mirror — always true for real objects)
- d_i is **positive** → real image (same side as object, in front of mirror)
- d_i is **negative** → virtual image (behind mirror)
- f is **positive** for **concave** (converging) mirrors
- f is **negative** for **convex** (diverging) mirrors

**For lenses:**
- d_o is **positive** (object in front of lens — always true for real objects)
- d_i is **positive** → real image (opposite side from object)
- d_i is **negative** → virtual image (same side as object)
- f is **positive** for **converging** (convex) lenses
- f is **negative** for **diverging** (concave) lenses

**Magnification interpretation:**
- |m| > 1: enlarged | |m| < 1: reduced | |m| = 1: same size
- m positive: upright | m negative: inverted

### The Four Optical Devices

| Device | Type | f sign | Image always |
|--------|------|--------|--------------|
| Concave mirror | Converging | + | Real (if d_o > f), Virtual (if d_o < f) |
| Convex mirror | Diverging | − | Virtual, upright, reduced |
| Convex lens | Converging | + | Real (if d_o > f), Virtual (if d_o < f) |
| Concave lens | Diverging | − | Virtual, upright, reduced |

**MCAT power move:** Diverging devices (convex mirror, concave lens) ALWAYS produce **virtual, upright, reduced** images. Immediately eliminate answer choices that say "real" or "inverted" or "enlarged" for these devices.

### Concave Mirror / Convex Lens — Image Behavior by Object Distance

| Object position | Image position | Image properties |
|----------------|---------------|-----------------|
| d_o > 2f (beyond C) | f < d_i < 2f | Real, inverted, **reduced** |
| d_o = 2f (at C) | d_i = 2f | Real, inverted, **same size** |
| f < d_o < 2f | d_i > 2f | Real, inverted, **enlarged** |
| d_o = f | d_i = ∞ | No image (parallel rays) |
| d_o < f | d_i < 0 (virtual) | Virtual, upright, **enlarged** |

Last row = magnifying glass. Object inside focal point → virtual, upright, enlarged image.

### Lens Power

**P = 1/f** (f in meters, P in diopters)

- Converging lens: P > 0
- Diverging lens: P < 0
- Lenses in contact: P_total = P₁ + P₂

**Clinical application:** Cornea + lens combine powers. Nearsightedness (myopia): image forms in front of retina → correct with **diverging lens** (negative power). Farsightedness (hyperopia): image would form behind retina → correct with **converging lens** (positive power).

### Problem-Solving Strategy for Optics

Follow this every time:
1. Identify device: mirror or lens? Converging or diverging?
2. Assign sign of f: converging = +, diverging = −.
3. Write d_o (positive for real objects).
4. Apply: 1/d_i = 1/f − 1/d_o.
5. Interpret sign of d_i: positive = real, negative = virtual.
6. Calculate m = −d_i/d_o.
7. Interpret m: positive = upright, negative = inverted; |m| gives size ratio.

**Worked example 1:** Object 30 cm from converging lens (f = 20 cm).
- f = +20, d_o = +30
- 1/d_i = 1/20 − 1/30 = 3/60 − 2/60 = 1/60 → d_i = +60 cm (real, on far side)
- m = −60/30 = −2 (inverted, 2× enlarged)
- Answer: Real, inverted, enlarged, 60 cm from lens.

**Worked example 2:** Object 10 cm from convex mirror (|f| = 20 cm).
- f = −20, d_o = +10
- 1/d_i = −1/20 − 1/10 = −3/20 → d_i = −6.7 cm (virtual, behind mirror)
- m = +6.7/10 = +0.67 (upright, reduced)
- Answer: Virtual, upright, reduced — exactly expected from diverging device.

---

## 5. Wave Optics

### Diffraction

When a wave encounters an obstacle or slit comparable in size to its wavelength, it **bends around** the obstacle.

Significant diffraction occurs when slit width ≈ wavelength. Much larger openings → minimal diffraction.

### Young's Double-Slit Experiment

Classic demonstration that light is a wave. Two slits separated by distance d. Interference pattern of bright and dark fringes on a distant screen.

**Bright fringes (constructive):** d sin θ = mλ (m = 0, 1, 2, ...)

**Dark fringes (destructive):** d sin θ = (m + ½)λ

**What changes the fringe pattern:**
- **Increase wavelength (redder light):** fringes spread apart (wider spacing)
- **Increase slit separation d:** fringes get closer together
- **Increase distance to screen:** fringes spread apart (angles unchanged)

### Single-Slit Diffraction

For a single slit of width a, dark fringes (minima) at:

**a sin θ = mλ** (m = 1, 2, 3, ... — note m ≠ 0)

Central maximum is **twice as wide** as other maxima.

### Thin-Film Interference

Occurs with soap bubbles, oil slicks, anti-reflective coatings. Light reflects off top and bottom surfaces of a thin film — the two reflected beams can interfere constructively or destructively.

Two effects determine the outcome:

**1. Path length difference:** Light reflecting from the bottom surface travels extra distance **2nt** (n = film refractive index, t = film thickness — effective path difference accounts for shorter wavelength inside film).

**2. Phase shifts at reflection:** A phase shift of λ/2 (180°) occurs when light reflects off a surface with a **higher** n (going from low n to high n). No phase shift when reflecting off lower n surface.

**Solving thin-film problems:**

Step 1: Count phase shifts (check each reflecting surface separately).
Step 2: Determine net phase shift:
- Even number of shifts (or zero): shifts cancel → constructive when 2nt = mλ
- Odd number of shifts (one): net λ/2 shift → constructive when 2nt = (m + ½)λ

**Worked example:** Oil film (n = 1.5) on water (n = 1.33). Minimum thickness for constructive reflection of 600 nm light.
- Top (air→oil): n_oil > n_air → phase shift ✓
- Bottom (oil→water): n_water < n_oil → no phase shift
- One phase shift total → constructive when 2nt = (m + ½)λ
- Minimum: m = 0 → 2(1.5)(t) = (0.5)(600 nm) → t = **100 nm**

---

## 6. Polarization

Only **transverse waves** can be polarized (why sound cannot be polarized).

**Unpolarized light** oscillates in all directions perpendicular to propagation. A **polarizer** transmits only the component along its transmission axis.

**Malus's Law:**

**I = I₀ cos²θ**

Where θ = angle between light's polarization direction and polarizer's transmission axis.

Special cases:
- θ = 0°: I = I₀ (all passes through)
- θ = 90°: I = 0 (crossed polarizers — no light)
- Unpolarized light through first polarizer: I = I₀/2 (regardless of orientation)

**MCAT tip:** Unpolarized through polarizer 1 (I halves) → then polarizer 2 at angle θ: I_total = (I₀/2) × cos²θ.

**Brewster's angle:** When light reflects at Brewster's angle, reflected light is completely polarized.
tan θ_B = n₂/n₁. Lower yield but occasionally appears.

---

## MCAT Strategy Summary

### Top 5 Most Testable Topics

1. **Thin lens/mirror equation + sign conventions** — practice until automatic
2. **Snell's law + total internal reflection** — qualitative and quantitative
3. **EM spectrum order and energy relationships** — R, M, IR, Vis, UV, X, Gamma
4. **Double-slit interference** — what changes the fringe pattern
5. **Polarization (Malus's law)** — standard calculations

### Common Traps

1. **Angles measured from normal, not from surface** (reflection, refraction). Biggest optics trap.
2. **Diverging devices ALWAYS give virtual, upright, reduced images.** Always.
3. **Sign conventions for mirrors vs lenses** — d_i > 0 means opposite things (front of mirror = real; far side of lens = real).
4. **Speed of light vs speed of sound** in media — light slows down in denser media, sound speeds up.
5. **Thin-film interference** — count phase shifts carefully. Don't assume constructive if path length = whole number of wavelengths without accounting for phase shifts.

### Quick Reference

**E = hf = hc/λ | c = 3×10⁸ m/s | n = c/v**
**Snell's law:** n₁ sin θ₁ = n₂ sin θ₂
**TIR:** sin θ_c = n₂/n₁ (n₁ > n₂, going high→low n)
**Thin lens/mirror:** 1/f = 1/d_o + 1/d_i | m = −d_i/d_o
**Lens power:** P = 1/f (diopters)
**Double-slit bright:** d sin θ = mλ
**Malus's law:** I = I₀ cos²θ
**Thin-film:** constructive when 2nt = mλ (even phase shifts) or 2nt = (m+½)λ (odd phase shifts)
