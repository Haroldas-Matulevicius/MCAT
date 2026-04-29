# CP Gen Chem Chapter 12 — Electrochemistry

Scope: Galvanic vs electrolytic cells; standard reduction potentials; E°_cell; Nernst; concentration cells; ΔG° = -nFE°; Faraday's law.

AAMC FC mapping: FC4C (electrochem)

Kaplan: General Chemistry Ch 12

Note: Electrostatics, magnetism, circuits → CP_Phy_Circuits.md

---

GALVANIC (VOLTAIC) CELLS:
- Convert chem energy → electrical energy
- SPONTANEOUS: ΔG < 0, E_cell > 0
- Anode (-): oxidation (loses mass)
- Cathode (+): reduction (gains mass)
- Salt bridge: cations to cathode, anions to anode
- e- flow: anode → cathode (external wire)
- Mnemonic: An Ox, Red Cat

ELECTROLYTIC CELLS:
- Use electrical energy → drive non-spontaneous reaction
- ΔG > 0, E_cell < 0
- Anode (+), cathode (-) — opposite charges from galvanic
- Same processes (Ox at A, Red at C); only sign convention flips
- Used in: electrolysis of water, electroplating, metal purification

STANDARD REDUCTION POTENTIALS:
- E° given as reduction
- More positive E° = better oxidizing agent (wants e-)
- More negative E° = better reducing agent (gives e-)
- Cathode = higher E° species; anode = lower E° species
- E° is INTENSIVE: doesn't scale with coefficients

CELL POTENTIAL:
- E°_cell = E°_cathode - E°_anode (ALWAYS subtract; don't flip+add)
- Worked: Cu (+0.34) vs Zn (-0.76): E° = 0.34 - (-0.76) = +1.10 V
- Negative E° → not spontaneous as written (electrolytic)

NERNST EQUATION:
- E = E° - (RT/nF)·ln Q
- @ 25°C: E = E° - (0.0592/n)·log Q
- F = 96,485 C/mol (~10^5 estimation)
- Q < 1: E > E° (more reactant)
- Q > 1: E < E° (more product)
- At equilibrium: Q = K, E = 0 (battery dead)

CONCENTRATION CELLS:
- Same electrodes, different [ion]
- E°_cell = 0; E_cell driven by [ion] difference
- Concentrated side = cathode (deposit metal, reduce [ion])
- Dilute side = anode (dissolve metal, increase [ion])
- Runs until concentrations equalize

FREE ENERGY AND CELL POTENTIAL:
- ΔG° = -nFE° (signs always OPPOSITE)
- ΔG° = -RT·ln K
- → -nFE° = -RT·ln K, E° = (RT/nF)·ln K
- Spontaneous: ΔG < 0, E > 0; equilibrium: both = 0; non-spont: ΔG > 0, E < 0

FARADAY'S LAW (electrolysis):
- mol e- = It/F (Q = It in coulombs)
- Steps:
  1. Q = It
  2. mol e- = Q/F
  3. Use half-reaction stoichiometry
  4. Mass = mol × MW
- Worked: 5 A × 3860 s = 19,300 C / 96,500 = 0.2 mol e-; Cu^2+ + 2e- → Cu: 0.1 mol Cu × 63.5 = 6.35 g

MCAT TRAPS:
- Don't memorize anode/cathode SIGNS — reason from first principles
- Don't flip E° and add; subtract directly
- Doubling coefficients doesn't change E° (intensive)
- Conventional current (+→-) ≠ electron flow (-→+)

→ Redox balancing → Ch11
→ Thermodynamics → Ch07
→ Equilibrium → Ch06
→ Circuits/electrostatics → CP_Phy_Circuits.md
