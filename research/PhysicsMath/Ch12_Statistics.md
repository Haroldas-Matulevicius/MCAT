# Physics & Math Chapter 12 — Statistics

Scope: Measures of central tendency (mean, median, mode); distributions (normal, skewed, bimodal); measures of spread (range, IQR, SD, variance, SEM); probability; hypothesis testing (null, alternative, p-value, α); Type I and II errors; statistical power; confidence intervals; effect size; statistical tests (t-test, ANOVA, chi-square, correlation, regression); charts/graphs/tables; epidemiological measures (incidence, prevalence, RR, OR, NNT, sensitivity, specificity, PPV, NPV); applying data to research conclusions.

**Section:** Chemical/Physical (CP) — Physics & Math
**Book:** Kaplan Physics and Math Strategies 2024 — Chapter 12
**AAMC FC mapping:** Research Methods — cross-cutting (all four sections)
**Yield:** Very high. Statistical interpretation is tested in experimental passages across BB, CP, and PS.

> **Note:** This is a known Kaplan content gap. The statistical tests section especially needs supplementation with Khan Academy statistics or the AAMC Official Guide. The full content here is drawn from the expanded Research_Methods.md file.

> **Note on origin:** Ch11 covers research design; Ch12 covers statistics and epidemiology. Both chapters originated from the merged `research/ResearchMethods/Research_Methods.md` file, now deleted. This file is the canonical statistics reference.

---

## 1. Descriptive Statistics

### Measures of Central Tendency

| Measure | Sensitive to outliers? | Best used when |
|---------|----------------------|----------------|
| **Mean** | YES — pulled toward outliers | Symmetric distributions, interval/ratio data |
| **Median** | NO — resistant to outliers | Skewed distributions, ordinal data |
| **Mode** | NO | Nominal data, most common category |

**MCAT key:** If a passage mentions "the distribution was skewed" or "there were extreme outliers," the **median** is the more appropriate measure of central tendency.

### Measures of Spread

- **Range** = max − min (crude, affected by outliers)
- **Interquartile range (IQR)** = Q3 − Q1 (middle 50%; resistant to outliers)
- **Variance** = average of squared deviations from the mean
- **Standard deviation (SD)** = √variance (same units as the data)
- **Standard error of the mean (SEM)** = SD/√n (variability of the sample mean; decreases as n increases)

**SD vs SEM:** SD describes spread of individual data points. SEM describes uncertainty of the sample mean estimate. Larger sample → smaller SEM → more precise estimate of the true mean.

---

## 2. Distributions

### Normal Distribution

Bell-shaped, symmetric around the mean.

**The 68-95-99.7 Rule:**
- **68%** of data within **1 SD** of the mean
- **95%** of data within **2 SD** of the mean
- **99.7%** of data within **3 SD** of the mean

**Example:** Mean = 100, SD = 15 (IQ scale).
- 68% score between 85–115
- 95% score between 70–130
- A score of 130 is 2 SD above mean → only ~2.5% scored higher

### Skewness

| Skew | Tail direction | Order | Example |
|------|---------------|-------|---------|
| **Positive** | Tail extends RIGHT | Mean > Median > Mode | Income distribution (few high earners pull mean right) |
| **Negative** | Tail extends LEFT | Mean < Median < Mode | Easy exam (few low scores pull mean left) |

**Memory trick:** The mean chases the tail. Positive skew → tail right → mean pulled right (higher than median).

**MCAT trap:** The **tail** names the skew, NOT the peak. A distribution with peak on the left and tail stretching right is **positively** skewed.

**Identifying from data:** If mean > median → positive skew. If mean < median → negative skew. If mean ≈ median → approximately symmetric.

### Other Distributions

**Bimodal:** Two peaks. Suggests the sample contains two distinct subpopulations.

**Uniform:** All values equally likely.

---

## 3. Probability

**Basic probability:** P(event) = favorable outcomes / total outcomes

**P ranges from 0 to 1.** P = 0 means impossible; P = 1 means certain.

**Mutually exclusive events:** P(A or B) = P(A) + P(B)

**Independent events:** P(A and B) = P(A) × P(B)

**Conditional probability:** P(A|B) = P(A and B) / P(B)

**MCAT application:** Probability appears in genetics (Hardy-Weinberg, Mendelian ratios), pharmacology (drug interactions), and epidemiology (disease risk).

---

## 4. Hypothesis Testing Framework

### Steps

1. State **null hypothesis (H₀):** No effect / no difference (e.g., drug has no effect on blood pressure).
2. State **alternative hypothesis (H₁):** There IS an effect / difference.
3. Collect data and calculate a test statistic.
4. Determine the **p-value**.
5. Compare p-value to significance level α (usually 0.05).
6. If p < α: **reject H₀** ("statistically significant").
7. If p ≥ α: **fail to reject H₀** (NOT "accept H₀" — you never prove H₀).

### P-value

**The probability of obtaining results at least as extreme as the observed, assuming the null hypothesis is true.**

- p = 0.03 means: "If there were truly no effect, there would be only a 3% chance of seeing results this extreme."
- p < 0.05 → reject H₀ (significant)
- p ≥ 0.05 → fail to reject H₀ (not significant)

**MCAT trap #1:** A small p-value does NOT tell you the effect is large or clinically meaningful — only that it's unlikely due to chance.

**MCAT trap #2:** "p < 0.05" does NOT mean there's a 95% probability the hypothesis is true. It means the DATA would be unlikely if H₀ were true.

---

## 5. Type I and Type II Errors

| | H₀ is actually TRUE | H₀ is actually FALSE |
|---|---|---|
| **Reject H₀** | **Type I error** (false positive) α | Correct ✓ (true positive, power) |
| **Fail to reject H₀** | Correct ✓ (true negative) | **Type II error** (false negative) β |

- **Type I error (α):** Concluding there IS an effect when there ISN'T one. False positive. Fire alarm when there's no fire.
- **Type II error (β):** Concluding there is NO effect when there IS one. False negative. Fire alarm NOT going off during a fire.

**α and β are inversely related** — reducing one increases the other (unless sample size is increased).

---

## 6. Statistical Power

**Power = 1 − β** = probability of correctly detecting a real effect (correctly rejecting a false H₀).

Factors that **increase** power:
- **Larger sample size** (most common way)
- **Larger effect size** (bigger real difference)
- **Higher α** (0.05 > 0.01, but increases Type I risk)
- **Less variability** in the data
- **One-tailed test** (more powerful but tests only one direction)

Desired power is typically ≥ 0.80 (80%).

**MCAT tip:** A study with very large n can achieve statistical significance (p < 0.05) even with a tiny, clinically meaningless effect. Power and effect size are both needed to evaluate a result.

---

## 7. Confidence Intervals

A **95% confidence interval (CI)** means: if we repeated this study 100 times and calculated a CI each time, ~95 of those intervals would contain the true population parameter.

**It does NOT mean there's a 95% probability the true value is in this specific interval** (common wrong answer on MCAT).

**Key rules:**
- If a 95% CI for a **mean difference** does NOT include 0 → result is statistically significant at p < 0.05.
- If a 95% CI for a **relative risk or odds ratio** does NOT include 1 → significant association.
- **Wider CI** = less precision (smaller sample or more variability).
- **Narrower CI** = more precision (larger sample or less variability).

---

## 8. Effect Size

**Effect size** quantifies the **magnitude** of the difference, independent of sample size.

- **Cohen's d** = (mean₁ − mean₂) / pooled SD
  - Small: ~0.2 | Medium: ~0.5 | Large: ~0.8
- A study can have a statistically significant p-value but a tiny, clinically meaningless effect (common with very large samples).
- **Statistical significance ≠ practical significance.** Always consider effect size.

---

## 9. Statistical Tests — Known Kaplan Gap

You don't need to calculate these on the MCAT, but you MUST know when each is used and how to interpret results.

### Overview Table

| Test | Purpose | Data types |
|------|---------|-----------|
| **t-test** | Compare means of 2 groups | 1 categorical IV (2 levels), 1 continuous DV |
| **ANOVA** | Compare means of 3+ groups | 1 categorical IV (3+ levels), 1 continuous DV |
| **Chi-square** | Test association between categorical variables | 2+ categorical variables |
| **Correlation (Pearson's r)** | Measure strength/direction of linear relationship | 2 continuous variables |
| **Regression** | Predict DV from IV(s) | 1+ IVs predicting 1 continuous DV |

### t-test

- **Independent samples:** Compares means of two DIFFERENT groups (drug vs placebo).
- **Paired/dependent:** Compares means from SAME group at two time points (before vs after treatment).
- Output: t-statistic and p-value. If p < 0.05 → means are significantly different.

### ANOVA (Analysis of Variance)

- Compares means across **3+ groups**.
- Why not multiple t-tests? Each test has its own Type I error rate → multiple tests inflate overall error rate (**familywise error rate**).
- ANOVA tests: "Are ANY of these group means significantly different?"
- If ANOVA is significant → need **post-hoc tests** (e.g., Tukey's HSD) to determine WHICH groups differ.
- **Factorial ANOVA:** Tests main effects of each IV and interaction effects between IVs.

### Chi-Square Test

- Tests whether two **categorical variables** are associated.
- Compares **observed** frequencies to **expected** frequencies.
- Large chi-square → observed frequencies differ substantially from expected → significant association.
- **Chi-square test of independence:** Are two categorical variables related?

### Correlation

- **Pearson's r:** ranges from **−1 to +1**
  - r = +1: perfect positive linear relationship
  - r = −1: perfect negative linear relationship
  - r = 0: no linear relationship (may still have non-linear relationship!)
  - |r| < 0.3: weak | 0.3–0.7: moderate | > 0.7: strong
- **r-squared (coefficient of determination):** proportion of variance in Y explained by X. r = 0.6 → r² = 0.36 → 36% of variance in Y explained by X.
- **CORRELATION DOES NOT EQUAL CAUSATION:**
  - Third variable problem: unmeasured confound causes both.
  - Directionality problem: does X cause Y, or Y cause X?

### Regression

- **Simple linear regression:** Y = a + bX. Slope b = for every 1-unit increase in X, Y changes by b units.
- **Multiple regression:** Predict DV from multiple IVs simultaneously. "Controlling for" other variables in the model.
- MCAT: interpret slope, identify significant predictors, understand what "controlling for" means.

### Decision Tree: Which Statistical Test?

```
What are you comparing/testing?
├── Means of groups?
│   ├── 2 groups → t-test
│   └── 3+ groups → ANOVA
├── Relationship between variables?
│   ├── Both continuous → Correlation / Regression
│   └── Both categorical → Chi-square
└── Predicting an outcome from predictors → Regression
```

---

## 10. Epidemiological Measures — Known Kaplan Gap

### Incidence vs Prevalence

| Measure | Definition | Study type |
|---------|-----------|-----------|
| **Incidence** | Number of NEW cases in a time period / population at risk | Cohort studies |
| **Prevalence** | Number of EXISTING cases at a point in time / total population | Cross-sectional |

**Key relationship:** Prevalence ≈ Incidence × Duration of disease

- High incidence, short duration (common cold) → low prevalence
- Low incidence, long duration (HIV on treatment) → high prevalence

### Relative Risk (RR) — Cohort Studies

**RR = Risk in exposed group / Risk in unexposed group**

- RR = 1.0: no association
- RR > 1.0: exposure increases risk
- RR < 1.0: exposure decreases risk (protective)
- **Used when you can directly measure incidence** (cohort/RCT)

### Odds Ratio (OR) — Case-Control Studies

**2×2 table:**

| | Disease + | Disease − |
|--|-----------|-----------|
| **Exposed** | a | b |
| **Not exposed** | c | d |

**OR = (a × d) / (b × c)**

- Interpretation similar to RR: OR > 1 = exposure associated with higher odds.
- For **rare diseases**, OR approximates RR.
- **Must use OR** (not RR) in case-control studies because you can't calculate true incidence rates.

### Absolute Risk Reduction (ARR) and NNT

- **ARR** = Risk in control group − Risk in treatment group
- **NNT = 1/ARR** = number of patients to treat to prevent one bad outcome
- Example: Control = 20% event rate, treatment = 15%. ARR = 5% = 0.05. NNT = 1/0.05 = 20.

### Sensitivity and Specificity

|  | Disease + | Disease − |
|--|-----------|-----------|
| **Test +** | True Positive (a) | False Positive (b) |
| **Test −** | False Negative (c) | True Negative (d) |

**Sensitivity = a/(a+c)** = True Positive Rate = proportion of sick people correctly identified.
- "**Sn**N**out**": A **S**ensitive test, when **N**egative, rules **OUT** the disease (few false negatives).
- High sensitivity → good **screening** test.

**Specificity = d/(b+d)** = True Negative Rate = proportion of healthy people correctly identified.
- "**Sp**P**in**": A **Sp**ecific test, when **P**ositive, rules **IN** the disease (few false positives).
- High specificity → good **confirmatory** test.

**Sensitivity and specificity are INTRINSIC to the test — do NOT change with prevalence.**

### Positive and Negative Predictive Value

**PPV = a/(a+b)** = If test is positive, probability patient actually has disease.
**NPV = d/(c+d)** = If test is negative, probability patient is actually healthy.

**PPV and NPV DEPEND ON PREVALENCE:**
- Prevalence ↑ → PPV ↑, NPV ↓
- Prevalence ↓ → PPV ↓, NPV ↑

**The MCAT loves this concept:** If disease prevalence is 1% and test has 99% sensitivity and 99% specificity, the PPV is only ~50%. Most positive results are false positives in a low-prevalence population. This is why we don't screen everyone for rare diseases.

---

## 11. Charts, Graphs, and Tables

### Reading Graphs Strategically

**Bar graph:** Comparing discrete categories. Read bar heights accurately.

**Histogram:** Distribution of continuous data. X-axis = value ranges, Y-axis = frequency. Look for shape (normal, skewed, bimodal).

**Box plot:** Shows median (middle line), IQR (box), range (whiskers), outliers (dots beyond whiskers). Quickly compare distributions across groups.

**Scatter plot:** Shows relationship between two continuous variables. Upward trend = positive correlation. Assess linearity, strength, and whether there are outliers.

**Line graph:** Shows change over time or continuous variables. Slope = rate of change.

**Kaplan-Meier curve:** Survival analysis. Shows proportion of subjects surviving (or event-free) over time. Steps down as events occur. Curves that don't cross are more interpretable.

### Tables

In a 2×2 table, always identify: what goes in rows vs columns, what the cell values represent (frequencies, percentages, or means).

**Contingency tables** for categorical data → chi-square test.
**Mean ± SD tables** for continuous data → t-test or ANOVA.

---

## MCAT Quick-Reference

### Statistics Decision Trees

**"Which statistical test?"**
1. Comparing means of 2 groups → t-test
2. Comparing means of 3+ groups → ANOVA
3. Testing association between categorical variables → Chi-square
4. Measuring linear relationship between continuous variables → Correlation
5. Predicting outcomes → Regression

**"What does the CI tell us?"**
- If 95% CI for mean difference doesn't include 0 → statistically significant (p < 0.05)
- If 95% CI for RR or OR doesn't include 1 → statistically significant association

**"Is this test sensitive or specific?"**
- Sensitive (SnNout): negative result rules OUT disease. Good screening.
- Specific (SpPin): positive result rules IN disease. Good confirmation.

### High-Yield Takeaways

1. **p < 0.05** = results unlikely if H₀ true. Does NOT mean hypothesis is correct.
2. **Statistical significance ≠ practical significance.** Need effect size too.
3. **Correlation ≠ causation.** Third variable problem + directionality.
4. **Sensitivity/specificity are test-intrinsic; PPV/NPV depend on prevalence.**
5. **Prevalence = incidence × duration.** Cross-sectional measures prevalence; cohort measures incidence.
6. **RR for cohort; OR for case-control.** For rare diseases, OR ≈ RR.
7. **Type I error (α) = false positive. Type II error (β) = false negative. Power = 1 − β.**
8. **CIs not including 0 (or 1 for RR/OR) = significant at p < 0.05.**

### Quick Formulas

**Sensitivity** = TP/(TP+FN) | **Specificity** = TN/(TN+FP)
**PPV** = TP/(TP+FP) | **NPV** = TN/(TN+FN)
**RR** = (a/(a+b)) / (c/(c+d)) | **OR** = (a×d)/(b×c)
**NNT** = 1/ARR | **ARR** = Risk_control − Risk_treatment
**Cohen's d** = (mean₁ − mean₂)/pooled SD
