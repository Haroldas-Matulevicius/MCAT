# Research Methods & Biostatistics -- MCAT Deep Dive

> **Cross-cutting content tested in ALL four sections.** Heaviest in PS (~20% of questions), but experimental passages in BB and CP routinely test study design, variable identification, and statistical interpretation. This is one of the most commonly underprepared areas -- students lose easy points here because they never sat down and systematically learned it.

---

## 1. Study Design

The single most important skill: **look at a passage and immediately classify the study design, then know what conclusions it can and cannot support.**

### 1.1 Experimental Designs

Experimental = the researcher **manipulates** an independent variable and measures the effect on a dependent variable.

#### Randomized Controlled Trial (RCT)

- **Gold standard** for establishing **causation**
- Key features: **random assignment** to groups, **control group**, **manipulation** of IV
- Random assignment distributes confounding variables equally across groups (on average), so any difference in the DV can be attributed to the IV
- Example: 200 patients randomly assigned to Drug X or placebo. After 8 weeks, depression scores are compared.
- Why it works: because random assignment means the groups should be equivalent on everything *except* the treatment, any difference in outcome is caused by the treatment

**MCAT trap:** A study can have a control group and still not be a true experiment if it lacks random assignment. That makes it quasi-experimental.

#### Quasi-Experimental Design

- Has manipulation of an IV but **no random assignment**
- Common when randomization is unethical or impractical (e.g., you can't randomly assign people to "smoker" vs "non-smoker")
- Threats to **internal validity** are higher because pre-existing group differences may explain results
- Example: Comparing test scores of students in a school that adopted a new curriculum vs a school that didn't (the researcher chose which school gets the curriculum, not random assignment of individual students)

#### Factorial Designs

- Involve **two or more independent variables** (called factors)
- A 2x2 factorial design has 2 IVs, each with 2 levels = 4 conditions
- The power of factorial designs: they can detect **interaction effects** (when the effect of one IV depends on the level of another IV)
- Example: Testing both drug type (A vs B) and dosage (low vs high). A 2x2 design. If Drug A works better at high dose but Drug B works better at low dose, that's an interaction.
- **Main effect** = overall effect of one IV averaged across levels of the other IV
- **Interaction effect** = the effect of one IV changes depending on the level of the other IV
- MCAT loves showing you graphs with crossing lines (interaction) vs parallel lines (no interaction)

### 1.2 Observational Designs

Observational = the researcher **does not manipulate** anything. They observe, measure, and record.

**Critical rule: observational studies CANNOT establish causation.** They can only show associations/correlations.

#### Cross-Sectional Study

- **Snapshot** at a single point in time
- Measures **prevalence** (how common something is right now)
- Cannot determine temporal sequence -- did A come before B or vice versa?
- Example: Surveying 1000 adults today about their exercise habits and depression levels
- Cheap, fast, good for generating hypotheses
- **Cannot establish causation, cannot calculate incidence**

#### Longitudinal / Prospective Cohort Study

- Follows a group of people **forward in time**
- Starts with exposure status, follows to see who develops the outcome
- Measures **incidence** (new cases over time) and **relative risk**
- Example: Following 5000 nurses for 20 years, tracking diet and cancer development
- Strengths: can establish temporal sequence (exposure before outcome), calculates RR directly
- Weaknesses: expensive, time-consuming, subject to **attrition** (people drop out)

#### Retrospective / Case-Control Study

- Starts with the **outcome** and looks **backward** at exposures
- Select cases (have the disease) and controls (don't have it), then compare past exposures
- Calculates **odds ratio** (not relative risk)
- Example: 100 lung cancer patients and 100 healthy controls -- compare their smoking history
- Strengths: good for **rare diseases**, cheaper, faster than cohort
- Weaknesses: **recall bias** (people with disease may remember exposures differently), cannot calculate incidence or true RR

#### Retrospective Cohort

- Uses historical records (medical charts, databases) to define a cohort and follow them forward through existing records
- Like a prospective cohort but done after the fact using pre-existing data
- Can calculate relative risk (unlike case-control)

### 1.3 Other Designs

#### Naturalistic Observation
- Observe behavior in its natural setting without any interference or manipulation
- High ecological validity, but no control, no causation, observer may influence behavior (if noticed)

#### Case Study
- In-depth investigation of a **single individual** (or very small group)
- Rich detail, useful for rare conditions (e.g., Phineas Gage)
- Cannot generalize to broader populations

#### Survey Research
- Questionnaires or interviews administered to a sample
- Can use **Likert scales** (1-5 or 1-7 agreement scales), open-ended questions, or closed-ended questions
- Vulnerable to: **social desirability bias**, **acquiescence bias** (tendency to agree), **response bias**, low response rates
- Wording effects: leading questions, double-barreled questions (asking two things at once)

#### Meta-Analysis
- Statistically combines results from **multiple studies** on the same question
- Increases **statistical power** by pooling data
- Can resolve conflicting findings across studies
- Concern: **publication bias** (studies with significant results are more likely to be published, so the pool of available studies is skewed)
- A meta-analysis is only as good as the studies it includes

#### Twin and Adoption Studies
- Used to estimate **heritability** -- the proportion of phenotypic variation attributable to genetic variation
- **Concordance rate**: percentage of twin pairs where both twins share a trait
- If MZ (identical) concordance >> DZ (fraternal) concordance, the trait has a strong genetic component
- Adoption studies: compare adopted children to biological vs adoptive parents to separate genetic from environmental influence
- Heritability is a population statistic -- it does NOT tell you what % of an individual's trait is genetic

### 1.4 Decision Tree: Which Study Design?

```
Can the researcher manipulate the IV?
|
+-- YES --> Is there random assignment?
|           |
|           +-- YES --> RCT (can establish causation)
|           +-- NO  --> Quasi-experimental (weaker causal claims)
|
+-- NO --> Observational
           |
           +-- One time point? --> Cross-sectional (prevalence)
           +-- Follow forward? --> Prospective cohort (incidence, RR)
           +-- Start with outcome, look back? --> Case-control (OR)
           +-- Combine multiple studies? --> Meta-analysis
```

**The causation question on MCAT:** "Which study design can establish a causal relationship?" Answer: **only a true experiment with random assignment.** Everything else shows association only.

---

## 2. Variables

### Core Variable Types

| Variable | Definition | Example |
|----------|-----------|---------|
| **Independent Variable (IV)** | Manipulated or selected by the researcher | Drug vs placebo |
| **Dependent Variable (DV)** | The measured outcome | Pain score |
| **Confounding Variable** | An unmeasured third variable that correlates with both IV and DV, providing an alternative explanation | Age, if older patients happened to get the drug |
| **Control Variable** | Held constant to prevent it from becoming a confound | All participants same age range |

### Moderator vs Mediator -- A Common MCAT Distinction

These two get tested frequently. Learn the difference cold.

**Moderating Variable**: Affects the **strength or direction** of the IV-DV relationship. It answers "For whom?" or "Under what conditions?"

- The moderator is NOT in the causal chain -- it modifies the relationship from outside
- Example: A new teaching method (IV) improves test scores (DV), but MORE so for visual learners than auditory learners. **Learning style** is the moderator.
- Example: An antidepressant (IV) reduces symptoms (DV) more effectively in patients under 40 than over 40. **Age** is the moderator.
- Graphically: if you split data by the moderator and the slopes differ (or lines cross), there's moderation

**Mediating Variable**: Explains the **mechanism** -- HOW or WHY the IV affects the DV. It sits in the causal chain between IV and DV.

- IV --> Mediator --> DV
- Example: Exercise (IV) --> increased serotonin (mediator) --> improved mood (DV). Serotonin explains *why* exercise improves mood.
- Example: Socioeconomic status (IV) --> access to healthcare (mediator) --> health outcomes (DV)
- If you remove the mediator, the IV-DV relationship should weaken or disappear

**Quick test:** Does it change the relationship (moderator) or explain it (mediator)?

### Operational Definitions

An **operational definition** specifies exactly how an abstract concept will be measured in a study.

- "Aggression" is abstract. "Number of times a child hits another child during a 30-minute play session" is an operational definition.
- "Intelligence" is abstract. "Score on the WAIS-IV" is an operational definition.
- MCAT tests whether you can identify what concept a researcher operationally defined and whether the definition is appropriate

---

## 3. Controls and Blinding

### Control Groups

| Type | Purpose | Example |
|------|---------|---------|
| **Positive control** | Known to produce the expected effect; proves the experiment CAN detect the effect if it's there | Using a known antibiotic on bacteria to confirm the assay works |
| **Negative control** | Known to produce NO effect; establishes baseline | Bacteria plate with no antibiotic (or with sterile water) |
| **Placebo group** | Receives inert treatment; controls for placebo effect | Sugar pill that looks identical to the drug |

**Why positive controls matter:** If your positive control doesn't work, your experimental setup is broken and you can't trust any results -- even negative ones.

### Randomization

- Distributes known AND unknown confounds equally across groups
- Without randomization, any group difference might be due to a pre-existing difference, not the IV
- This is THE reason RCTs are the gold standard

### Blinding

| Level | Who is blinded | What it controls |
|-------|---------------|-----------------|
| **Single blind** | Participant doesn't know their group | Placebo effect, demand characteristics |
| **Double blind** | Participant AND researcher don't know | Also controls experimenter expectancy / observer bias |
| **Triple blind** | Participant, researcher, AND data analyst | Also controls analysis bias |

### Counterbalancing

- Used in **within-subjects designs** (same participants in all conditions)
- Addresses **order effects** (practice, fatigue, carryover)
- Example: Half the participants get Condition A first then B; the other half get B first then A
- Latin square designs for more than 2 conditions

---

## 4. Validity and Reliability

### Study Validity (about the study itself)

#### Internal Validity
The confidence that the IV **actually caused** the change in the DV.

**Threats to internal validity** (memorize these -- they appear on the MCAT):

| Threat | Definition | Example |
|--------|-----------|---------|
| **Confounding variables** | Unmeasured variable explains the IV-DV link | Sicker patients given the new drug |
| **Selection bias** | Pre-existing group differences | Volunteers vs non-volunteers differ systematically |
| **History** | External event during the study affects DV | War breaks out during a stress study |
| **Maturation** | Participants naturally change over time | Children improve at reading simply by aging |
| **Testing effects** | Taking a test changes performance on retest | Practice effect on cognitive assessments |
| **Instrumentation** | Measurement tool changes over time | Observers get tired and rate differently |
| **Attrition / Mortality** | Differential dropout between groups | Sicker patients drop out of treatment group |
| **Regression to the mean** | Extreme scores naturally move toward the average on retest | Selecting worst-performing students; they improve even without intervention |

#### External Validity
The degree to which findings **generalize** to other populations, settings, and times.

- Threatened by: homogeneous samples (e.g., all college students), artificial lab settings, cultural specificity
- Trade-off: tightly controlled lab studies have high internal but often low external validity

#### Ecological Validity
A subtype of external validity -- do findings apply to **real-world settings**?

- Lab studies of memory using random word lists have low ecological validity
- Studying memory for grocery lists in a supermarket has higher ecological validity

### Measurement Validity (about the instrument/measure)

| Type | Question it answers | Example |
|------|-------------------|---------|
| **Face validity** | Does it LOOK like it measures what it should? | A depression questionnaire asks about sadness -- seems valid on its face |
| **Content validity** | Does it cover ALL aspects of the construct? | A math test that only tests algebra lacks content validity for "math ability" |
| **Construct validity** | Does it measure the theoretical concept it claims to? | Does an "intelligence" test actually measure intelligence? Includes convergent (correlates with related measures) and discriminant (doesn't correlate with unrelated ones) |
| **Criterion validity** | Does it predict or correlate with a relevant outcome? | **Predictive**: SAT predicts college GPA. **Concurrent**: new depression scale correlates with established one |

### Reliability (consistency of measurement)

| Type | What it measures | Method |
|------|-----------------|--------|
| **Test-retest** | Stability over **time** | Give same test twice, correlate scores |
| **Inter-rater** | Agreement between **observers** | Two raters score the same behavior, compare |
| **Internal consistency** | Items measure the **same construct** | Cronbach's alpha (>0.7 is acceptable) |
| **Parallel/alternate forms** | Equivalent versions give same results | Two versions of a test, correlate scores |

### The Reliability-Validity Relationship

> **A measure can be reliable without being valid, but it CANNOT be valid without being reliable.**

- A broken scale that always reads 5 lbs too heavy is reliable (consistent) but not valid (inaccurate)
- A scale that gives random readings is neither reliable nor valid
- A properly calibrated scale is both reliable and valid

Think of it as a target: reliability = shots clustered together; validity = shots near the bullseye. You can cluster far from the bullseye (reliable, not valid) but you can't randomly scatter shots and happen to average at the bullseye in any meaningful way.

---

## 5. Sampling Methods

### Probability Sampling (every member of population has a known, non-zero chance of selection)

These support **generalization** to the broader population.

| Method | How it works | When to use |
|--------|-------------|-------------|
| **Simple random** | Every individual equally likely (lottery, random number generator) | Default best method, need a complete list of population |
| **Stratified random** | Divide population into subgroups (strata), then randomly sample from each stratum | When you want to ensure representation of key subgroups (e.g., equal gender sampling) |
| **Cluster** | Randomly select entire groups (clusters), then sample everyone in selected clusters | When a complete list of individuals isn't available but groups are (e.g., randomly select 10 schools, test all students in those schools) |
| **Systematic** | Select every nth person from a list | Simple to implement, risk of bias if list has a periodic pattern |

**Stratified vs cluster:** Stratified samples FROM each subgroup. Cluster samples ENTIRE subgroups. Stratified is generally more precise.

### Non-Probability Sampling (no guarantee every member has a chance)

These do **NOT support generalization** -- results apply only to the sample.

| Method | How it works | Limitation |
|--------|-------------|-----------|
| **Convenience** | Whoever is available (college students in a psych class) | Massive selection bias, most common in psychology research |
| **Snowball** | Participants recruit others | Used for hard-to-reach populations (e.g., undocumented immigrants), selection bias |
| **Purposive** | Researcher handpicks based on specific criteria | Expert judgment determines sample, subjective |
| **Quota** | Like stratified but non-random; fill quotas for each subgroup using convenience | Looks representative but isn't truly random |

### Why Sampling Matters

Sampling method directly affects **external validity**. If your sample is not representative of the target population, your findings may not generalize. MCAT passages frequently describe a study's sample and ask you to evaluate whether conclusions can be generalized.

---

## 6. Descriptive Statistics

### Measures of Central Tendency

| Measure | Sensitive to outliers? | When to use |
|---------|----------------------|-------------|
| **Mean** | YES -- pulled toward outliers | Symmetric distributions, interval/ratio data |
| **Median** | NO -- resistant to outliers | Skewed distributions, ordinal data |
| **Mode** | NO | Nominal data, describing most common category |

**MCAT key:** If a passage mentions "the distribution was skewed" or "there were several extreme outliers," the median is more appropriate than the mean.

### Measures of Spread

- **Range** = max - min (crude, affected by outliers)
- **Interquartile range (IQR)** = Q3 - Q1 (middle 50%, resistant to outliers)
- **Variance** = average of squared deviations from the mean
- **Standard deviation (SD)** = square root of variance, in the same units as the data

### Normal Distribution and the 68-95-99.7 Rule

For a normal (bell-shaped, symmetric) distribution:

- **68%** of data falls within **1 SD** of the mean
- **95%** of data falls within **2 SD** of the mean
- **99.7%** of data falls within **3 SD** of the mean

**MCAT application:** If mean = 100 and SD = 15:
- 68% of scores between 85-115
- 95% of scores between 70-130
- 99.7% of scores between 55-145
- A score of 130 is 2 SDs above the mean, meaning only ~2.5% scored higher

### Skewness

| Skew | Tail direction | Relationship | Example |
|------|---------------|-------------|---------|
| **Positive skew** | Tail extends RIGHT | Mean > Median > Mode | Income distribution (few very high earners pull mean right) |
| **Negative skew** | Tail extends LEFT | Mean < Median < Mode | Easy exam (most score high, few bomb it and pull mean left) |

**Memory trick:** The mean chases the tail. Positive skew = tail right = mean pulled right (higher). Negative skew = tail left = mean pulled left (lower).

**MCAT trap:** The tail names the skew, NOT the peak. A distribution with a peak on the left and tail stretching right is POSITIVELY skewed.

How to identify from data: compare mean and median. If mean > median, positive skew. If mean < median, negative skew. If mean = median, approximately symmetric.

---

## 7. Inferential Statistics

### Hypothesis Testing Framework

1. State **null hypothesis (H0)**: There is NO effect / NO difference (e.g., the drug has no effect on blood pressure)
2. State **alternative hypothesis (H1)**: There IS an effect / difference (e.g., the drug lowers blood pressure)
3. Collect data and calculate a test statistic
4. Determine the **p-value**
5. Compare p-value to significance level (alpha, usually 0.05)
6. If p < alpha, **reject** the null hypothesis ("statistically significant")
7. If p >= alpha, **fail to reject** the null hypothesis (NOT "accept the null" -- you never prove H0)

### P-value

The **probability of obtaining results at least as extreme as the observed results, assuming the null hypothesis is true.**

- p = 0.03 means: "If there were truly no effect, there would be only a 3% chance of seeing results this extreme."
- p < 0.05: reject H0 (significant)
- p >= 0.05: fail to reject H0 (not significant)
- A small p-value does NOT tell you the effect is large or clinically meaningful -- only that it's unlikely due to chance

**MCAT trap:** "p < 0.05" does not mean there's a 95% chance the hypothesis is true. It means the DATA would be unlikely if H0 were true.

### Type I and Type II Errors

| | H0 is actually TRUE | H0 is actually FALSE |
|---|---|---|
| **Reject H0** | **Type I error** (false positive) | Correct decision (true positive) |
| **Fail to reject H0** | Correct decision (true negative) | **Type II error** (false negative) |

- **Type I error (alpha)**: Concluding there IS an effect when there ISN'T one. Like a fire alarm going off when there's no fire.
- **Type II error (beta)**: Concluding there is NO effect when there IS one. Like a fire alarm NOT going off during a fire.
- Alpha and beta are inversely related -- reducing one increases the other (unless you increase sample size)

### Statistical Power

**Power = 1 - beta** = probability of correctly detecting a real effect (correctly rejecting a false H0)

Factors that **increase** power:
- **Larger sample size** (most common way)
- **Larger effect size** (bigger real difference)
- **Higher alpha** (0.05 > 0.01, but increases Type I risk)
- **Less variability** in the data
- **One-tailed test** (more powerful but tests only one direction)

Desired power is typically 0.80 (80%).

### Confidence Intervals

A **95% confidence interval** means: if we repeated this study 100 times and calculated a CI each time, approximately 95 of those intervals would contain the true population parameter.

- It does NOT mean there's a 95% probability the true value is in this specific interval (common MCAT wrong answer)
- If a 95% CI for a mean difference does NOT include 0, the result is statistically significant at p < 0.05
- Wider CI = less precision (smaller sample or more variability)
- Narrower CI = more precision

### Effect Size

**Effect size** quantifies the **magnitude** of the difference, independent of sample size.

- **Cohen's d** = (mean1 - mean2) / pooled SD. Small: 0.2, Medium: 0.5, Large: 0.8
- A study can have a statistically significant p-value but a tiny, clinically meaningless effect size (common with very large samples)
- MCAT takeaway: statistical significance != practical significance. Always consider effect size.

---

## 8. Statistical Tests

This is a known Kaplan gap. You don't need to calculate these on the MCAT, but you MUST know when each test is used and how to interpret results.

### Overview Table

| Test | Purpose | Data types |
|------|---------|-----------|
| **t-test** | Compare means of **2 groups** | 1 categorical IV (2 levels), 1 continuous DV |
| **ANOVA** | Compare means of **3+ groups** | 1 categorical IV (3+ levels), 1 continuous DV |
| **Chi-square** | Test association between **categorical variables** | 2+ categorical variables |
| **Correlation (Pearson's r)** | Measure strength/direction of **linear** relationship | 2 continuous variables |
| **Regression** | Predict DV from IV(s) | 1+ IVs predicting 1 continuous DV |

### t-test

- **Independent samples t-test**: Compares means of two DIFFERENT groups (e.g., drug vs placebo group)
- **Paired/dependent samples t-test**: Compares means from the SAME group at two time points (e.g., before and after treatment)
- Output: t-statistic and p-value. If p < 0.05, the means are significantly different.

### ANOVA (Analysis of Variance)

- Compares means across **3 or more groups**
- Why not just do multiple t-tests? Because each t-test has a Type I error rate -- doing many tests inflates the overall error rate (called the **familywise error rate**)
- ANOVA tests the overall question: "Are ANY of these group means significantly different?"
- If ANOVA is significant, you need **post-hoc tests** (e.g., Tukey's HSD) to determine WHICH groups differ
- **Factorial ANOVA**: tests main effects of each IV and interaction effects between IVs

### Chi-Square Test

- Tests whether two **categorical variables** are associated
- Compares **observed** frequencies to **expected** frequencies (what you'd expect by chance)
- Example: Is political party affiliation associated with vaccine acceptance? (Both variables are categories)
- Large chi-square value = observed frequencies differ substantially from expected = significant association
- **Chi-square test of independence**: are two categorical variables related?
- **Chi-square goodness of fit**: does observed distribution match expected distribution?

### Correlation

- **Pearson's r**: ranges from **-1 to +1**
  - r = +1: perfect positive linear relationship
  - r = -1: perfect negative linear relationship
  - r = 0: no linear relationship (but could still have a non-linear relationship!)
  - |r| < 0.3: weak; 0.3-0.7: moderate; > 0.7: strong (rough guidelines)
- **r-squared (coefficient of determination)**: the proportion of variance in Y explained by X
  - If r = 0.6, then r-squared = 0.36, meaning 36% of the variance in Y is explained by X
- **CORRELATION DOES NOT EQUAL CAUSATION.** Two reasons:
  - **Third variable problem**: an unmeasured confound causes both
  - **Directionality problem**: does X cause Y, or does Y cause X?

### Regression

- **Simple linear regression**: predict DV from a single IV. Y = a + bX
  - **b (slope)**: for every 1-unit increase in X, Y changes by b units
  - **a (intercept)**: predicted value of Y when X = 0
- **Multiple regression**: predict DV from multiple IVs simultaneously. Controls for other variables in the model.
- MCAT application: interpret slope, identify significant predictors, understand what "controlling for" means

### Decision Tree: Which Statistical Test?

```
What are you comparing/testing?
|
+-- Means of groups?
|   |
|   +-- How many groups?
|       +-- 2 groups --> t-test
|       +-- 3+ groups --> ANOVA
|
+-- Relationship between variables?
|   |
|   +-- Both continuous? --> Correlation / Regression
|   +-- Both categorical? --> Chi-square
|
+-- Predicting an outcome from predictors?
    --> Regression
```

---

## 9. Epidemiological Measures

Another known Kaplan gap. These show up in BB and PS passages with clinical/public health data.

### Incidence vs Prevalence

| Measure | Definition | Analogy |
|---------|-----------|---------|
| **Incidence** | Number of **NEW cases** in a time period / population at risk | Water flowing INTO a bathtub |
| **Prevalence** | Number of **EXISTING cases** at a point in time / total population | Total water IN the bathtub |

**Key relationship: Prevalence is approximately equal to Incidence x Duration of disease**

- A disease with high incidence but short duration (common cold) may have low prevalence
- A disease with low incidence but long duration (HIV with treatment) may have high prevalence
- Cross-sectional studies measure prevalence. Cohort studies measure incidence.

### Relative Risk (RR) -- Used in Cohort Studies

**RR = Risk in exposed group / Risk in unexposed group**

- RR = 1.0: no association
- RR > 1.0: exposure increases risk (risk factor)
- RR < 1.0: exposure decreases risk (protective factor)
- Example: Smokers have lung cancer incidence of 15/1000. Non-smokers: 1/1000. RR = 15/1 = 15. Smokers have 15x the risk.

### Odds Ratio (OR) -- Used in Case-Control Studies

Calculated from a **2x2 table**:

|  | Disease + | Disease - |
|--|-----------|-----------|
| **Exposed** | a | b |
| **Not exposed** | c | d |

**OR = (a x d) / (b x c)**

- Interpretation similar to RR: OR > 1 means exposure associated with higher odds of disease
- For rare diseases, OR approximates RR
- You MUST use OR (not RR) in case-control studies because you can't calculate true incidence rates

### Absolute Risk Reduction (ARR) and Number Needed to Treat (NNT)

- **ARR** = Risk in control group - Risk in treatment group
- **NNT = 1 / ARR** = how many patients you need to treat to prevent one bad outcome
- Example: Control event rate = 20%, treatment event rate = 15%. ARR = 5% = 0.05. NNT = 1/0.05 = 20. You need to treat 20 patients to prevent one event.

### Sensitivity and Specificity

|  | Disease + | Disease - |
|--|-----------|-----------|
| **Test +** | True Positive (a) | False Positive (b) |
| **Test -** | False Negative (c) | True Negative (d) |

- **Sensitivity = a / (a + c)** = True Positive Rate = proportion of sick people correctly identified
  - "SnNout": A Sensitive test, when Negative, rules OUT the disease (few false negatives)
  - High sensitivity = good screening test
- **Specificity = d / (b + d)** = True Negative Rate = proportion of healthy people correctly identified
  - "SpPin": A Specific test, when Positive, rules IN the disease (few false positives)
  - High specificity = good confirmatory test

**Sensitivity and specificity are INTRINSIC to the test -- they do NOT change with prevalence.**

### Positive and Negative Predictive Value

- **PPV = a / (a + b)** = If the test is positive, what's the probability the patient actually has the disease?
- **NPV = d / (c + d)** = If the test is negative, what's the probability the patient is actually healthy?

**PPV and NPV DEPEND ON PREVALENCE:**
- As prevalence INCREASES: PPV increases, NPV decreases
- As prevalence DECREASES: PPV decreases, NPV increases
- A positive result in a low-prevalence population is likely a false positive (low PPV) -- this is why we don't screen everyone for rare diseases

**MCAT loves this concept.** If a passage says disease prevalence is 1% and the test has 99% sensitivity and 99% specificity, the PPV is only about 50%. Most positive results are false positives.

---

## 10. Bias Taxonomy

Bias = **systematic error** that distorts results in one direction (unlike random error, which goes both ways).

### Research/Design Biases

| Bias | Definition | Solution |
|------|-----------|----------|
| **Selection bias** | Groups differ systematically before the study begins | Random assignment |
| **Sampling bias** | Sample is not representative of the target population | Probability sampling |
| **Attrition bias** | Participants drop out differentially between groups | Intent-to-treat analysis, track dropouts |
| **Lead-time bias** | Early detection appears to increase survival time even when it doesn't (just diagnosed earlier) | Measure mortality rate, not survival from diagnosis |
| **Publication bias** | Positive/significant results more likely to be published | Pre-registration, funnel plots in meta-analyses |
| **Funding bias** | Research funded by interested parties tends to favor the funder | Disclose conflicts of interest |

### Participant Biases

| Bias | Definition | Solution |
|------|-----------|----------|
| **Hawthorne effect** | Participants change behavior because they know they're being observed (not because of the IV) | Covert observation, acclimation period |
| **Placebo effect** | Improvement due to belief in treatment, not treatment itself | Placebo control group, blinding |
| **Nocebo effect** | Worsening due to negative expectations | Blinding |
| **Social desirability bias** | Reporting what seems socially acceptable rather than truth | Anonymous surveys, indirect questioning |
| **Demand characteristics** | Participants guess the hypothesis and try to confirm (or deny) it | Deception, double blinding |
| **Recall bias** | Differential accuracy of memory between groups (cases remember exposures better than controls) | Use records instead of self-report, prospective design |
| **Acquiescence bias** | Tendency to agree with statements regardless of content | Mix positively and negatively worded items |
| **Response bias** | Systematic pattern of inaccurate responses | Careful survey design, attention checks |

### Researcher Biases

| Bias | Definition | Solution |
|------|-----------|----------|
| **Experimenter expectancy (Rosenthal effect)** | Researcher unconsciously influences results in the expected direction | Double blinding |
| **Observer bias** | Researcher's expectations influence how they record or interpret data | Standardized protocols, inter-rater reliability checks, blinding |
| **Confirmation bias** | Seeking or interpreting data in ways that confirm existing beliefs | Pre-registration, blinded analysis |

### How Blinding and Randomization Address Biases

- **Randomization** addresses: selection bias, confounding
- **Single blinding (participant)** addresses: placebo/nocebo, demand characteristics, Hawthorne effect
- **Double blinding (participant + researcher)** also addresses: experimenter expectancy, observer bias
- **Triple blinding (+ analyst)** also addresses: analysis/interpretation bias

---

## 11. Ethics in Research

### Core Protections

- **Informed consent**: Participants must understand what the study involves, risks, benefits, and their right to withdraw. Must be voluntary, without coercion.
- **Right to withdraw**: Participants can leave at any time without penalty
- **Confidentiality**: Participant data must be protected
- **Minimal risk**: Risk should not exceed what participants encounter in daily life (for most studies)
- **Debriefing**: Explain the true purpose after participation, especially important if deception was used

### Oversight Bodies

| Body | Oversees | Key function |
|------|---------|-------------|
| **IRB (Institutional Review Board)** | Human subjects research | Reviews protocols for ethical compliance BEFORE the study begins |
| **IACUC (Institutional Animal Care and Use Committee)** | Animal research | Ensures humane treatment, minimizes pain/distress, justifies animal use |

### Deception in Research

- Sometimes necessary (e.g., Milgram's obedience study -- wouldn't work if participants knew the true purpose)
- Rules: Must be **justified** (no alternative method), must not cause undue distress, participants must be **debriefed** afterward
- Participants can withdraw their data after debriefing

### The Belmont Report (1979)

Three core ethical principles for research involving human subjects:

| Principle | Meaning | Application |
|-----------|---------|-------------|
| **Respect for Persons** | Treat individuals as autonomous agents; protect those with diminished autonomy | Informed consent |
| **Beneficence** | Maximize benefits, minimize harm ("do no harm" + actively do good) | Risk-benefit analysis |
| **Justice** | Fair distribution of research burdens and benefits | Don't exploit vulnerable populations; ensure equitable participant selection |

**MCAT relevance:** The Belmont Report is explicitly testable. Know these three principles and their applications.

### Vulnerable Populations

Special protections required for:
- Children (need parental consent + child's assent)
- Prisoners (coercion concerns)
- Pregnant women
- Cognitively impaired individuals
- Economically disadvantaged populations

The **justice** principle is particularly relevant: historically, vulnerable populations bore disproportionate research burdens (e.g., Tuskegee syphilis study, in which Black men were denied treatment for syphilis without informed consent).

---

## Quick-Reference Decision Trees

### "Which study design was used?"

1. Was there manipulation of a variable? If NO --> Observational
2. Was there random assignment? If YES --> RCT. If NO --> Quasi-experimental
3. If observational: at one time point? (Cross-sectional) Forward in time? (Cohort) Starting from disease looking back? (Case-control) Combining studies? (Meta-analysis)

### "Can this study establish causation?"

- RCT with random assignment --> YES
- Everything else --> NO (association only)

### "Which statistical test should they use?"

1. Comparing means of 2 groups? --> t-test
2. Comparing means of 3+ groups? --> ANOVA
3. Testing association between categorical variables? --> Chi-square
4. Measuring linear relationship between continuous variables? --> Correlation
5. Predicting outcomes? --> Regression

### "Is this measure valid?"

- Does it look right? --> Face validity
- Does it cover the full concept? --> Content validity
- Does it measure the right theoretical construct? --> Construct validity
- Does it predict/correlate with relevant outcomes? --> Criterion validity

### "What type of bias is this?"

- Participant knows they're being watched and changes behavior --> Hawthorne
- Participant improves because they believe in the treatment --> Placebo
- Participant reports socially acceptable answers --> Social desirability
- Researcher unconsciously influences participant behavior --> Experimenter expectancy
- Cases remember exposures better than controls --> Recall bias
- Sample doesn't represent the population --> Sampling bias
- Participants drop out unevenly --> Attrition bias

---

## High-Yield Takeaways for Test Day

1. **Only RCTs with random assignment can establish causation.** If a passage describes any other design and asks about causation, the answer is NO.
2. **Correlation does not equal causation.** Third variable problem and directionality problem.
3. **p < 0.05 means results are unlikely if null is true.** It does NOT mean there's a 95% probability the hypothesis is correct.
4. **Statistical significance is not practical significance.** Large samples can produce tiny, meaningless but "significant" effects.
5. **Sensitivity rules out (SnNout), specificity rules in (SpPin).** PPV depends on prevalence.
6. **Prevalence = incidence x duration.** Cross-sectional measures prevalence, cohort measures incidence.
7. **Moderator = changes the strength/direction.** Mediator = explains the mechanism (in the causal chain).
8. **Reliable but not valid is possible. Valid but not reliable is impossible.**
9. **Randomization controls confounds. Blinding controls placebo and experimenter effects.**
10. **Belmont Report: Respect for persons, beneficence, justice.** Know these cold.
