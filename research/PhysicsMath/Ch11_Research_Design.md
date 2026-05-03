# Physics & Math Chapter 11 — Research Design

Scope: Scientific method (hypothesis, controls, variable types, IV/DV/confounding); basic science research (in vitro, in vivo, animal models); human subjects research (clinical trial phases, RCT, observational designs — cohort, case-control, cross-sectional); ethics (IRB, informed consent, Belmont Report); research in the real world (peer review, publication bias, replication crisis); validity, reliability, bias taxonomy.

**Section:** Chemical/Physical (CP) — Physics & Math
**Book:** Kaplan Physics and Math Strategies 2024 — Chapter 11
**AAMC FC mapping:** Research Methods — cross-cutting (tested in all four sections; most heavily in PS ~20%)
**Yield:** Very high and frequently under-prepared. This content is tested in BB and CP experimental passages, not just PS.

> **Note on origin:** This chapter content originated from `research/ResearchMethods/Research_Methods.md` and `Content/ResearchMethods/Research_Methods.md`. Both files are now deleted; this chapter (Ch11) and Ch12 are the canonical location for all research methods content. Statistics (Ch12) is a known Kaplan content gap — supplement with Khan Academy statistics.

---

## 1. Scientific Method

### Hypothesis Testing

A well-formed scientific hypothesis is:
- **Testable** (can be confirmed or refuted by experiment)
- **Falsifiable** (there must exist possible evidence that would disprove it)
- **Specific** (predicts a measurable outcome)

Standard format: "If [IV changes], then [DV will change in this way], because [proposed mechanism]."

### Variable Types

| Variable | Definition | Example |
|----------|-----------|---------|
| **Independent Variable (IV)** | Manipulated or selected by researcher | Drug vs placebo |
| **Dependent Variable (DV)** | Measured outcome | Pain score |
| **Confounding Variable** | Unmeasured third variable correlating with both IV and DV | Age (if older patients happen to get the drug) |
| **Control Variable** | Held constant to prevent confounding | All participants in same age range |

### Moderator vs Mediator — HIGH YIELD DISTINCTION

**Moderator:** Affects the **strength or direction** of the IV→DV relationship. Answers "For whom?" or "Under what conditions?" NOT in the causal chain — modifies from outside.
- Example: Antidepressant (IV) reduces symptoms (DV) more in patients under 40 than over 40. **Age** = moderator.
- Graphically: different slopes when data split by the moderator (or crossing lines).

**Mediator:** Explains the **mechanism** — HOW/WHY the IV affects the DV. Sits IN the causal chain: IV → Mediator → DV.
- Example: Exercise (IV) → increased serotonin (mediator) → improved mood (DV). Remove the mediator, IV-DV relationship weakens.

**Quick test:** Does it change the relationship (moderator) or explain it (mediator)?

### Operational Definitions

An operational definition specifies exactly how an abstract concept will be measured.
- "Aggression" (abstract) → "number of times a child hits another child during 30-minute play session" (operational)
- MCAT tests whether you can identify what concept was operationally defined and whether the definition is appropriate.

---

## 2. Experimental Designs

Experimental = researcher **manipulates** an IV and measures effect on DV.

### Randomized Controlled Trial (RCT)

- **Gold standard** for establishing **causation**
- Key features: **random assignment** to groups, **control group**, **manipulation** of IV
- Random assignment distributes known AND unknown confounds equally across groups → any DV difference attributable to the IV
- Example: 200 patients randomly assigned to Drug X or placebo.

**MCAT trap:** A study can have a control group but NOT be an RCT if it lacks random assignment → quasi-experimental.

### Quasi-Experimental

- Has IV manipulation but **no random assignment**
- Common when randomization is unethical (can't assign people to "smoker" vs "non-smoker")
- Higher threat to **internal validity** — pre-existing group differences may explain results

### Factorial Designs

- Two or more IVs (factors); detect **interaction effects** (when effect of one IV depends on level of another)
- A 2×2 factorial design: 2 IVs, each with 2 levels = 4 conditions
- **Main effect:** Overall effect of one IV averaged across levels of the other
- **Interaction effect:** Effect of one IV changes depending on level of the other IV
- MCAT loves graphs: crossing lines = interaction; parallel lines = no interaction

---

## 3. Observational Designs

Observational = researcher does NOT manipulate anything.

**Critical rule: observational studies CANNOT establish causation. Association only.**

### Cross-Sectional Study

- **Snapshot** at a single time point
- Measures **prevalence** (how common something is right now)
- Cannot determine temporal sequence
- Example: Surveying 1000 adults today about exercise habits and depression levels
- Cheap, fast, hypothesis-generating
- **Cannot establish causation, cannot calculate incidence**

### Prospective Cohort Study

- Follows a group **forward in time**
- Starts with exposure status, follows to see who develops outcome
- Measures **incidence** (new cases over time) and **relative risk (RR)**
- Example: Following 5000 nurses for 20 years, tracking diet and cancer
- Can establish temporal sequence; expensive, subject to attrition (dropout)

### Retrospective / Case-Control Study

- Starts with **outcome**, looks **backward** at exposures
- Select cases (have disease) and controls (don't), compare past exposures
- Calculates **odds ratio (OR)** — not RR
- Example: 100 lung cancer patients vs 100 healthy controls — compare smoking history
- Good for **rare diseases**, cheaper, faster
- Weaknesses: **recall bias** (disease cases remember exposures differently), cannot calculate incidence

### Retrospective Cohort

- Uses historical records to define a cohort and follow through existing data
- Can calculate RR (unlike case-control)

### Other Designs

**Naturalistic Observation:** Behavior in natural setting without interference. High ecological validity, no control.

**Case Study:** In-depth investigation of single individual. Rich detail, cannot generalize.

**Survey Research:** Questionnaires/interviews. Vulnerable to: social desirability bias, acquiescence bias, wording effects (leading questions).

**Meta-Analysis:** Statistically combines results from multiple studies. Increases power, can resolve conflicting findings. Concern: **publication bias** (significant results more likely published, biasing the pool).

**Twin and Adoption Studies:** Estimate heritability. Concordance rate = % of twin pairs where both share a trait. MZ (identical) concordance >> DZ (fraternal) = strong genetic component. Heritability is a population statistic — does NOT tell you % of an individual's trait that is genetic.

### Study Design Decision Tree

```
Can researcher manipulate the IV?
├── YES → Is there random assignment?
│         ├── YES → RCT (can establish causation)
│         └── NO → Quasi-experimental (weaker causal claims)
└── NO → Observational
          ├── One time point → Cross-sectional (prevalence)
          ├── Follow forward → Prospective cohort (incidence, RR)
          ├── Start with outcome, look back → Case-control (OR)
          └── Combine multiple studies → Meta-analysis
```

---

## 4. Controls and Blinding

### Control Groups

| Type | Purpose | Example |
|------|---------|---------|
| **Positive control** | Known to produce expected effect (proves assay works) | Known antibiotic on bacteria |
| **Negative control** | Known to produce NO effect (establishes baseline) | Bacteria with sterile water |
| **Placebo group** | Inert treatment (controls for placebo effect) | Sugar pill identical to drug |

**Why positive controls matter:** If positive control doesn't work, the experimental setup is broken — even negative results are untrustworthy.

### Blinding

| Level | Who is blinded | What it controls |
|-------|---------------|-----------------|
| **Single blind** | Participant | Placebo effect, demand characteristics |
| **Double blind** | Participant + researcher | Also: experimenter expectancy, observer bias |
| **Triple blind** | Participant + researcher + analyst | Also: analysis/interpretation bias |

### Counterbalancing

Used in **within-subjects designs** (same participants in all conditions). Addresses **order effects** (practice, fatigue, carryover). Half get Condition A→B; half get B→A.

---

## 5. Validity and Reliability

### Study Validity

#### Internal Validity
Confidence that IV **actually caused** the change in DV.

**Threats to internal validity:**

| Threat | Definition |
|--------|-----------|
| **Confounding variables** | Unmeasured variable explains IV-DV link |
| **Selection bias** | Pre-existing group differences |
| **History** | External event during study affects DV |
| **Maturation** | Participants naturally change over time |
| **Testing effects** | Taking a test changes performance on retest |
| **Attrition / Mortality** | Differential dropout between groups |
| **Regression to the mean** | Extreme scores naturally move toward average on retest |

#### External Validity
Degree findings **generalize** to other populations, settings, and times. Threatened by: homogeneous samples, artificial lab settings.

#### Ecological Validity
Subtype of external validity — do findings apply to **real-world settings**?

### Measurement Validity

| Type | Question | Example |
|------|----------|---------|
| **Face validity** | Does it LOOK like it measures what it should? | Depression questionnaire asks about sadness |
| **Content validity** | Does it cover ALL aspects of the construct? | Math test that only covers algebra lacks content validity |
| **Construct validity** | Does it measure the theoretical concept it claims? | Convergent (correlates with related measures) + discriminant (doesn't correlate with unrelated) |
| **Criterion validity** | Does it predict/correlate with relevant outcomes? | Predictive (future), concurrent (present) |

### Reliability

| Type | What it measures |
|------|-----------------|
| **Test-retest** | Stability over time |
| **Inter-rater** | Agreement between observers |
| **Internal consistency** | Items measure same construct (Cronbach's α > 0.7) |
| **Parallel/alternate forms** | Equivalent test versions give same results |

### The Reliability-Validity Relationship

> **A measure can be reliable without being valid, but it CANNOT be valid without being reliable.**

- Reliable but invalid: broken scale that always reads 5 lbs too heavy (consistent, but inaccurate).
- Neither reliable nor valid: scale giving random readings.
- Think of a target: reliability = shots clustered together; validity = shots near the bullseye.

---

## 6. Sampling Methods

### Probability Sampling (supports generalization)

| Method | How it works |
|--------|-------------|
| **Simple random** | Every individual equally likely |
| **Stratified random** | Divide into subgroups (strata), randomly sample from each |
| **Cluster** | Randomly select entire groups; sample everyone in selected groups |
| **Systematic** | Select every nth person from a list |

**Stratified vs cluster:** Stratified samples FROM each subgroup. Cluster samples ENTIRE subgroups.

### Non-Probability Sampling (does NOT support generalization)

| Method | Limitation |
|--------|-----------|
| **Convenience** | Massive selection bias (most common in psychology research) |
| **Snowball** | Selection bias; used for hard-to-reach populations |
| **Purposive** | Researcher handpicks; subjective |
| **Quota** | Fills quotas using convenience; non-random |

---

## 7. Ethics in Research

### Core Protections

- **Informed consent:** Participants must understand the study, risks, benefits, and their right to withdraw. Must be voluntary, without coercion.
- **Right to withdraw:** Participants can leave at any time without penalty.
- **Confidentiality:** Participant data must be protected.
- **Minimal risk:** Risk should not exceed everyday risk (for most studies).
- **Debriefing:** Explain true purpose after participation, especially when deception was used.

### Oversight Bodies

| Body | Oversees | Key function |
|------|---------|-------------|
| **IRB** (Institutional Review Board) | Human subjects research | Reviews protocols for ethical compliance BEFORE study begins |
| **IACUC** | Animal research | Ensures humane treatment, minimizes pain/distress, justifies animal use |

### Deception in Research

- Sometimes necessary (e.g., Milgram's obedience study).
- Rules: must be **justified** (no alternative method), must not cause undue distress, participants must be **debriefed** afterward.

### The Belmont Report (1979) — HIGH YIELD

Three core ethical principles for human subjects research:

| Principle | Meaning | Application |
|-----------|---------|-------------|
| **Respect for Persons** | Treat individuals as autonomous agents; protect those with diminished autonomy | Informed consent |
| **Beneficence** | Maximize benefits, minimize harm | Risk-benefit analysis |
| **Justice** | Fair distribution of research burdens and benefits | Don't exploit vulnerable populations |

**Tuskegee syphilis study** context: Black men denied treatment for syphilis without informed consent — violated all three Belmont principles. Directly led to modern IRB requirements.

**Vulnerable populations requiring special protection:** Children (parental consent + child's assent), prisoners (coercion concerns), pregnant women, cognitively impaired individuals, economically disadvantaged.

---

## 8. Bias Taxonomy

### Research/Design Biases

| Bias | Definition | Solution |
|------|-----------|----------|
| **Selection bias** | Groups differ systematically before study | Random assignment |
| **Sampling bias** | Sample not representative of target population | Probability sampling |
| **Attrition bias** | Differential dropout between groups | Intent-to-treat analysis |
| **Lead-time bias** | Early detection appears to increase survival time without changing disease course | Measure mortality rate, not survival from diagnosis |
| **Publication bias** | Positive/significant results more likely published | Pre-registration, funnel plots |

### Participant Biases

| Bias | Definition |
|------|-----------|
| **Hawthorne effect** | Behavior changes because participants know they're being observed |
| **Placebo effect** | Improvement due to belief in treatment |
| **Nocebo effect** | Worsening due to negative expectations |
| **Social desirability bias** | Reporting what seems socially acceptable |
| **Demand characteristics** | Participants guess hypothesis and try to confirm/deny it |
| **Recall bias** | Differential memory accuracy between groups (cases recall exposures better than controls) |
| **Acquiescence bias** | Tendency to agree with statements regardless of content |

### Researcher Biases

| Bias | Definition |
|------|-----------|
| **Experimenter expectancy (Rosenthal effect)** | Researcher unconsciously influences results in expected direction |
| **Observer bias** | Researcher's expectations influence recording/interpretation |
| **Confirmation bias** | Seeking data that confirms existing beliefs |

---

## Research in the Real World

**Peer review:** Independent experts evaluate study before publication. Catches errors, but doesn't guarantee truth — only that the methodology meets professional standards.

**Replication crisis:** Many published findings (especially in psychology) fail to replicate when independent labs try to reproduce them. Causes: publication bias, small samples, p-hacking (trying multiple analyses until p < 0.05), outcome switching.

**Publication bias:** Positive results are published; null results often aren't. Meta-analyses based on published literature therefore overestimate effect sizes.

---

## MCAT Quick-Reference Decision Trees

**"Which study design?"**
1. Manipulation of IV? No → Observational.
2. Random assignment? Yes → RCT. No → Quasi-experimental.
3. If observational: one time point (cross-sectional), forward in time (cohort), disease first (case-control), combines studies (meta-analysis).

**"Can this establish causation?"**
- Only an RCT with random assignment → YES. Everything else → association only.

**High-yield takeaways:**
1. Only RCTs with random assignment establish causation.
2. Correlation ≠ causation (third variable problem + directionality problem).
3. Moderator = changes strength/direction of relationship. Mediator = explains mechanism (in causal chain).
4. Reliable but not valid is possible. Valid but not reliable is impossible.
5. Randomization controls confounds. Blinding controls placebo and experimenter effects.
6. Belmont Report: Respect for persons, beneficence, justice.
