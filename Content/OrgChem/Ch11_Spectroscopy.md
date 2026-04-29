# CP Orgo Chapter 11 — Spectroscopy

Scope: IR; 1H NMR; 13C NMR; mass spectrometry; UV-Vis; integrated structure determination.

AAMC FC mapping: FC5C (analytical) + FC5D (structure determination)

Kaplan: Organic Chemistry Ch 11

---

IR SPECTROSCOPY:
- x-axis: wavenumber (cm-1); y-axis: % transmittance
- Functional group region: 4000-1500 (diagnostic)
- Fingerprint: 1500-400 (rarely used on MCAT)
- Bond must change dipole moment to absorb (CO2 symmetric stretch IR-inactive)

KEY IR ABSORPTIONS:
- O-H alcohol: 3200-3550, broad rounded
- O-H carb acid: 2500-3300, VERY broad (swallows C-H)
- N-H: 3300-3500; 2 peaks = primary amine, 1 peak = secondary
- C-H sp3: 2850-3000
- C-H sp2: 3000-3100 (just above 3000 = unsaturation)
- C-H sp (alkyne): ~3300, sharp
- C=O: 1700-1750, sharp/strong (THE most diagnostic peak)
- C=C alkene: 1600-1680, often weak
- C-O: 1000-1250, strong
- C≡C: 2100-2260
- C≡N: 2200-2260, sharp

C=O FINE-TUNING (donating to C=O lowers freq):
- Anhydride: 1800-1830 (2 peaks)
- Ester: 1735-1750
- Aldehyde: 1720-1740 (also 2720, 2850 C-H)
- Ketone: 1705-1720
- Carb acid: 1700-1725 + broad O-H
- Amide: 1630-1690 (N donates strongly)

IR DECISION TREE:
- Broad 2500-3300 swallowing C-H + C=O 1710 → carb acid
- Broad 3200-3550, no C=O → alcohol
- Sharp 1700-1750 + aldehyde C-H 2720 → aldehyde
- Sharp 1700-1750 + C-O → ester
- Sharp 1700-1750 + N-H → amide
- Sharp 1700-1750 alone → ketone

1H NMR (most-tested):
- TMS = 0 ppm reference
- 4 pieces: # signals, chemical shift, integration, splitting

NUMBER OF SIGNALS:
- Each unique H environment = 1 signal
- Symmetry reduces # signals (DME = 1 signal for 6 H's)

CHEMICAL SHIFTS (memorize):
- 0-1: alkyl far from FG
- 1-2: alkyl R-CH2-R
- 2-2.5: α to C=O
- 2-3: allylic
- 3-4: adjacent O/N/halogen
- 3.5-4: ester OCH
- 4.5-6.5: vinyl
- 6.5-8: aromatic
- 9-10: aldehyde C-H
- 10-12: carb acid O-H
- 1-5 variable: alcohol O-H
- Mnemonic: Deshielded = Downfield = higher Delta

INTEGRATION:
- Area ∝ # protons in environment

SPLITTING (n+1 rule):
- n adjacent non-equivalent H's → n+1 peaks
- 0 = singlet, 1 = doublet, 2 = triplet, 3 = quartet, 4 = quintet, 5 = sextet
- Equivalent H's don't split each other
- O-H, N-H usually broad singlets (rapid exchange)
- Ethyl pattern: -CH2CH3 → quartet + triplet, 2:3

D2O SHAKE:
- O-H, N-H exchange with D → peaks DISAPPEAR
- Diagnostic for exchangeable H's

13C NMR:
- # peaks = # unique C environments
- NO splitting (broadband decoupled)
- Integration NOT reliable (different relaxation)
- Range: 0-220 ppm
- 0-50: alkyl sp3
- 50-90: C-O, C-N
- 100-150: aromatic, vinyl
- 170-185: carb acid, ester, amide C=O
- 190-220: aldehyde, ketone C=O
- # peaks vs total C → symmetry analysis

MASS SPECTROMETRY:
- Measures m/z; not actual spectroscopy
- M+ (molecular ion): MW; not always tallest, may be absent if fragmenting
- Base peak: tallest = 100%
- Fragmentation peaks at lower m/z

COMMON FRAGMENT LOSSES:
- 15 CH3
- 17 OH
- 18 H2O
- 28 CO or CH2=CH2
- 29 CHO or C2H5
- 31 OCH3
- 44 CO2
- 45 OEt

ISOTOPE PATTERNS:
- M+1: ~1.1% per C (13C)
- Cl: M:M+2 = 3:1 (35Cl 75%, 37Cl 25%)
- Br: M:M+2 = 1:1 (79Br/81Br ~equal)
- 2 Cl: M:M+2:M+4 = 9:6:1

NITROGEN RULE:
- Odd MW → odd # nitrogens
- Aniline C6H7N MW 93 (odd, 1 N); urea CH4N2O MW 60 (even, 2 N); glycine MW 75 (odd, 1 N)

UV-VIS:
- Electronic transitions (π→π*, n→π*)
- λ_max = wavelength of max absorbance
- Beer-Lambert: A = εlc
  - A unitless; ε in L/(mol·cm); l in cm; c in mol/L
  - A = -log(T)
  - Linear at low [c]; deviates at high
- Conjugation → longer λ_max (red/bathochromic shift)
  - Ethylene: 170 nm; butadiene: 217 nm; β-carotene: 450 nm
- HOMO-LUMO gap narrows with more conjugation

BIOLOGICAL UV-VIS:
- Protein at 280 nm: Trp (strongest) > Tyr > Phe (weak)
- DNA/RNA at 260 nm
- Pure DNA: A260/A280 ~1.8; pure RNA ~2.0; protein contamination lowers ratio
- NADH at 340 nm (NAD+ doesn't absorb): track dehydrogenase

DEGREES OF UNSATURATION:
- DoU = (2n + 2 - m + p - r)/2 [n=C, m=H, p=N, r=halogen]
- 0: saturated, no ring
- 1: 1 double bond OR 1 ring
- 2: 2 doubles, 2 rings, 1 triple
- 4: benzene (3 C=C + 1 ring)

INTEGRATED WORKFLOW:
1. MS → MW + halogens + N rule → molecular formula
2. DoU = (2n+2-m+p-r)/2
3. IR → functional groups
4. NMR → connectivity
5. Propose structure, verify all data

→ Conjugation/MO theory → CP_OC_Ch03
→ Functional group naming → CP_OC_Ch01
→ DNA absorbance → BB_Ch06
→ Enzyme kinetics absorbance → BB_Ch02
