# BB Chapter 2 — Enzymes

Scope: Enzymes as biological catalysts, mechanisms of enzyme activity, enzyme kinetics, effects of local conditions, regulation.

**Section:** Bio/Biochem (BB)
**AAMC FC mapping:** FC1A (Protein Structure and Function) — enzyme portion; also FC5E (CP)
**Kaplan Reference:** Biochemistry Chapter 2

---

## Note on Primary Coverage

Enzyme kinetics is dual-listed AAMC content: it lives primarily in **CP FC5E** in this project (tested in both CP and BB sections). Load `Content/CP/` and `research/CP/` enzyme kinetics materials for the full deep-dive.

This chapter file exists to preserve the Kaplan Ch 2 slot in the BB chapter order and surface the high-level topics.

## 1. Enzymes as Biological Catalysts

- Lower activation energy (Ea) of a reaction; do NOT change ΔG, Keq, or the equilibrium position
- Provide an alternative reaction pathway through a lower-energy transition state
- Not consumed in the reaction; regenerate after each turnover
- Highly specific for substrate (lock-and-key / induced-fit models)

## 2. Mechanisms of Enzyme Activity

- **Proximity and orientation** — bring substrates together in correct alignment
- **Acid-base catalysis** — donate/accept protons (His at pH ~7 is the classic example)
- **Covalent catalysis** — form transient covalent bond with substrate (e.g., Ser in serine proteases attacking the carbonyl)
- **Electrostatic catalysis / metal ions** — stabilize negatively charged transition state (e.g., Zn²⁺ in carbonic anhydrase, Mg²⁺ in kinases)
- **Strain / transition-state stabilization** — enzyme binds TS more tightly than substrate

## 3. Enzyme Kinetics (detail in CP FC5E)

- **Michaelis-Menten:** v = Vmax[S] / (Km + [S])
- **Km** = [S] at which v = ½Vmax; measure of substrate affinity (lower Km = higher affinity)
- **Vmax** = maximum rate at saturating [S]
- **kcat** = turnover number; kcat/Km = catalytic efficiency
- **Lineweaver-Burk** double-reciprocal plot: 1/v vs 1/[S]; y-int = 1/Vmax, x-int = -1/Km

### Inhibition patterns

| Type | Km | Vmax | LB plot |
|------|----|------|---------|
| Competitive | ↑ | unchanged | lines cross at y-axis |
| Noncompetitive (pure) | unchanged | ↓ | lines cross at x-axis |
| Uncompetitive | ↓ | ↓ | parallel lines |
| Mixed | ↑ or ↓ | ↓ | cross in upper-left quadrant |

## 4. Effects of Local Conditions

- **Temperature:** rate increases with T up to the optimum (typically ~37°C for human enzymes); beyond that, denaturation drops activity rapidly
- **pH:** bell-shaped curve centered on the enzyme's optimum (pepsin ~2, trypsin ~8, most enzymes near 7)
- **Salt / ionic strength:** can disrupt electrostatic interactions

## 5. Regulation

- **Allosteric regulation** — effectors bind at site distinct from active site; cooperativity → sigmoidal kinetics (not Michaelis-Menten)
- **Feedback inhibition** — end product of pathway inhibits early committed enzyme (e.g., ATP inhibits PFK-1)
- **Covalent modification** — phosphorylation (most common; by kinases, reversed by phosphatases), glycosylation, ubiquitination
- **Proteolytic cleavage** — zymogens/proenzymes (trypsinogen → trypsin) — irreversible activation
- **Isozymes** — different enzymes catalyzing same reaction with different kinetics/tissue distribution (e.g., hexokinase vs glucokinase, LDH isoforms)

## GAPS
Full enzyme mechanism deep-dive (catalytic residues, induced fit vs lock-and-key, allosteric models — MWC vs KNF) currently distributed across Ch 1 protein structure material. Consolidation here on next pass.
