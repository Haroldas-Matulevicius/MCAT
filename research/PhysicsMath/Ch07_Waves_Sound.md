# Physics & Math Chapter 7 — Waves & Sound

Scope: General wave properties (wavelength, frequency, amplitude, period, speed); transverse vs longitudinal waves; superposition, interference (constructive/destructive); standing waves, nodes, antinodes, harmonics; resonance; beats; sound waves, speed of sound, intensity, decibels, inverse square law; Doppler effect; ultrasound.

**Section:** Chemical/Physical (CP) — Physics & Math
**Book:** Kaplan Physics and Math Strategies 2024 — Chapter 7
**AAMC FC mapping:** FC4B (partially) / FC4D (Sound, light, and EM radiation)
**Yield:** High. Harmonics in pipes/strings, Doppler, and decibel calculations are highly testable. Standing waves and resonance appear frequently.

---

## 1. Wave Properties

### Fundamental Quantities

Every wave is described by five quantities:

| Quantity | Symbol | Unit | Definition |
|----------|--------|------|------------|
| **Wavelength** | λ | m | Distance for one full cycle |
| **Frequency** | f | Hz (s⁻¹) | Cycles per second |
| **Amplitude** | A | varies | Maximum displacement from equilibrium |
| **Period** | T | s | Time for one full cycle |
| **Velocity (speed)** | v | m/s | Speed of propagation |

**Key relationships:**
- **T = 1/f** (period and frequency are inverses)
- **v = fλ** (the wave equation — use this constantly)

**MCAT tip:** If wave speed is fixed (like speed of sound or light in a given medium), increasing frequency MUST decrease wavelength, and vice versa.

### Transverse vs Longitudinal Waves

**Transverse waves:** Oscillation is **perpendicular** to the direction of travel.
- Examples: light (EM waves), waves on a string, water surface waves (approximately)
- Key feature: can be **polarized** (restrict oscillation to one plane)

**Longitudinal waves:** Oscillation is **parallel** to the direction of travel.
- Examples: sound waves, pressure waves, compression waves in a spring
- Key feature: consist of **compressions** (high pressure) and **rarefactions** (low pressure)
- Cannot be polarized

**MCAT trap:** Water waves are often described as transverse, but they have both transverse and longitudinal components. For MCAT purposes, treat as transverse unless told otherwise.

---

## 2. Superposition and Interference

### Superposition Principle

When two waves occupy the same space, the resulting displacement is the **algebraic sum** of individual displacements.

**Constructive interference:** Waves in phase (crest meets crest). Amplitudes ADD → bigger wave.

**Destructive interference:** Waves out of phase by half a wavelength (crest meets trough). Amplitudes SUBTRACT → smaller wave or complete cancellation.

**Path length difference determines type:**
- Constructive: path difference = mλ (m = 0, 1, 2, ...)
- Destructive: path difference = (m + ½)λ

---

## 3. Standing Waves — HIGH YIELD

When a wave reflects back on itself, the interference pattern creates a **standing wave** — it appears to vibrate in place rather than travel.

**Nodes:** Points of zero displacement (permanent destructive interference). Never move.

**Antinodes:** Points of maximum displacement (permanent constructive interference). Oscillate with maximum amplitude.

### Case 1: String Fixed at Both Ends AND Open Pipe (Both Ends Open)

String: both ends are **nodes**. Open pipe: both ends are **antinodes**. Mathematically, same result:

**λ_n = 2L/n** where n = 1, 2, 3, 4, ... (all integers)

**f_n = nv/(2L)**

- n=1: fundamental (1st harmonic) — one antinode
- n=2: second harmonic (1st overtone) — two antinodes
- **ALL harmonics present** (n = 1, 2, 3, 4, ...)

### Case 2: Closed Pipe (One End Closed, One End Open)

Closed end → **node** (air can't move). Open end → **antinode** (air moves freely).

**λ_n = 4L/n** where n = 1, 3, 5, 7, ... (**ODD only**)

**f_n = nv/(4L)**

**Why only odd harmonics?** The fundamental fits exactly one quarter-wavelength (node at closed end, antinode at open end). The next mode satisfying these boundary conditions must fit three quarter-wavelengths (3/4 λ). Then five, etc. Even multiples of quarter-wavelengths cannot satisfy a node at one end AND antinode at the other. Sketch it out to verify.

**MCAT tip:** Closed pipes have **lower fundamental frequency** than open pipes of the same length (λ₁ = 4L for closed vs 2L for open → longer wavelength → lower frequency). Closed pipe produces a deeper pitch.

### Summary Table

| System | λ_n | Harmonics present | Boundary conditions |
|--------|-----|-------------------|---------------------|
| String (both ends fixed) | 2L/n | All (n = 1, 2, 3...) | Node-Node |
| Open pipe (both ends open) | 2L/n | All (n = 1, 2, 3...) | Antinode-Antinode |
| Closed pipe (one end closed) | 4L/n | Odd only (n = 1, 3, 5...) | Node-Antinode |

---

## 4. Resonance

**Resonance** occurs when an external vibration matches a system's **natural frequency**. Maximum energy transfer → large-amplitude oscillations.

Examples: pushing a swing at the right frequency, shattering a glass with a specific pitch, tuning forks, resonant cavities.

**MCAT relevance:** Resonance explains why certain frequencies are amplified in tubes/pipes and why the human ear canal amplifies certain frequencies (~3-4 kHz). MRI uses resonance of proton spins.

---

## 5. Sound

### Speed of Sound

Sound is a **longitudinal mechanical wave** — requires a medium.

**Speed depends on medium:**
- Solids > Liquids > Gases (faster in stiffer, denser-particle media)
- In air at room temperature: ~340 m/s
- In water: ~1500 m/s
- In steel: ~5000 m/s

**This is the OPPOSITE of light**, which travels fastest in vacuum and slows in denser media. A classic MCAT trick.

Why the difference? Sound travels through particle-to-particle collisions — closer-packed particles transmit vibrations faster. Light is an electromagnetic wave slowed by interactions with electrons in the medium.

**Temperature effect:** In gases, speed of sound increases with temperature (faster molecules = faster vibration transmission).

### Intensity and Decibels

**Intensity (I)** = power per unit area = P/A, measured in W/m².

**Decibel scale:**

**β = 10 × log₁₀(I/I₀)**

Where I₀ = 10⁻¹² W/m² (threshold of human hearing).

#### Calculator-Free dB Tricks — MCAT Favorite

| Intensity change | dB change |
|-----------------|-----------|
| × 2 (double) | +3 dB |
| × 10 | +10 dB |
| × 100 | +20 dB |
| × 1000 | +30 dB |
| ÷ 2 (halve) | −3 dB |
| ÷ 10 | −10 dB |

**Worked approach:** Intensity increases by factor of 200. What is ΔdB?
Break 200 into factors of 2 and 10: 200 = 2 × 10 × 10.
+3 + 10 + 10 = **+23 dB**

**Direct calculation:** I = 10⁻⁵ W/m². What is β?
β = 10 × log(10⁻⁵/10⁻¹²) = 10 × log(10⁷) = 10 × 7 = **70 dB**

**MCAT tip:** The dB scale is logarithmic. A 10 dB increase means 10× more intense. A 20 dB increase means 100×. Perceived loudness roughly doubles every 10 dB (Weber's law crossover — PS/Soc).

### Inverse Square Law

For a point source radiating equally in all directions:

**I = P/(4πr²)**

Intensity drops as 1/r². Double the distance → 1/4 the intensity.

Double the distance from a sound source: intensity drops to 1/4 → change of −6 dB (two halvings: −3 + −3 = −6).

### Beats

When two waves of slightly different frequencies overlap, you hear pulsations in volume called **beats**.

**f_beat = |f₁ − f₂|**

**Example:** Tuning forks at 440 Hz and 444 Hz → beat frequency = 4 Hz (4 pulses of loudness per second).

**MCAT tip:** Beat frequency questions are straightforward — just subtract. Unknown frequency: "512 Hz fork beats at 3 Hz with unknown fork. What are possible frequencies?" Answer: 509 Hz or 515 Hz.

---

## 6. Doppler Effect

The Doppler effect describes the apparent change in frequency when source and observer are in relative motion.

**Conceptual rules (what the MCAT actually tests):**
- Source and observer moving **toward** each other → perceived frequency **increases** (higher pitch)
- Source and observer moving **apart** → perceived frequency **decreases** (lower pitch)

**The formula:**

**f' = f × (v ± v_observer) / (v ∓ v_source)**

Sign convention mnemonic: **"toward = together = higher."**
- Observer moves toward source: add v_observer in numerator (f' bigger)
- Source moves toward observer: subtract v_source in denominator (f' bigger)
- Reverse for moving apart.

**Key MCAT distinction:** Moving the source toward the observer at speed u is NOT the same as moving the observer toward the source at the same speed u. They produce slightly different perceived frequencies. However, at low speeds relative to wave speed, they're approximately equal.

### Doppler in Medical Imaging

Ultrasound uses the Doppler effect to measure blood flow velocity. Reflected ultrasound from moving red blood cells is frequency-shifted; the shift magnitude is proportional to flow velocity.

---

## 7. Ultrasound

Ultrasound = sound waves above human hearing range (>20,000 Hz).

Key points:
- Higher frequency = better resolution but less penetration depth.
- Reflection occurs at tissue boundaries (impedance mismatch between tissues).
- Uses Doppler effect to measure blood flow velocity.
- No ionizing radiation (unlike X-rays and CT scans) — safe for fetuses.

---

## MCAT Strategy Summary

### Pattern Recognition

| Trigger | Action |
|---------|--------|
| "Pipe closed at one end" | Odd harmonics only. Fundamental = v/4L. |
| "Pipe open at both ends" or "string fixed at both ends" | All harmonics. Fundamental = v/2L. |
| "Intensity doubles" | +3 dB |
| "Intensity increases 10×" | +10 dB |
| "Sound source approaches" | Perceived frequency increases (higher pitch) |
| "Sound source recedes" | Perceived frequency decreases (lower pitch) |
| "Two slightly different tuning forks" | Beat frequency = |f₁ − f₂| |
| "Sound vs light — which travels faster in water?" | Sound (longitudinal, particle collisions). Light slows in water. |

### Common Traps

1. **Closed pipe only has odd harmonics.** Students forget the constraint and allow even harmonics.
2. **Closed pipe has lower fundamental than open pipe** of same length. Many students assume the opposite.
3. **dB is logarithmic.** Doubling intensity is only +3 dB, not +100%. A "10 dB louder" sound is 10× the intensity.
4. **Speed of sound: solid > liquid > gas.** Opposite of what students expect (they confuse with density effects on light).
5. **Doppler effect only changes perceived frequency**, not actual frequency emitted by the source.

### Quick Reference

**Wave equation:** v = fλ | T = 1/f
**Standing waves (string/open pipe):** λ_n = 2L/n (all n) → f₁ = v/2L
**Standing waves (closed pipe):** λ_n = 4L/n (odd n only) → f₁ = v/4L
**Decibels:** β = 10 log(I/I₀) | ×10 intensity = +10 dB | ×2 intensity = +3 dB
**Inverse square:** I = P/(4πr²) | double distance = 1/4 intensity = −6 dB
**Beats:** f_beat = |f₁ − f₂|
**Doppler (toward → higher f):** f' = f(v ± v_obs)/(v ∓ v_src)
