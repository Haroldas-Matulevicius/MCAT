# CP — Physics Ch 12: Statistics

Kaplan Physics Ch 12 | Cross-cutting (all 4 sections) | Known Kaplan gap

> Supplement with Khan Academy statistics and AAMC Official Guide.
> Originated from research/ResearchMethods/Research_Methods.md (now deleted). Research design → Ch11.

---

DESCRIPTIVE STATISTICS:
- Central tendency:
  - Mean: sensitive to outliers | Median: resistant (use for skewed data) | Mode: most common
- Spread:
  - Range = max − min | IQR = Q3 − Q1 (resistant to outliers)
  - Variance = average squared deviation | SD = √variance (same units as data)
  - SEM = SD/√n (precision of sample mean; decreases with larger n)

DISTRIBUTIONS:
- Normal (bell-shaped): symmetric; 68-95-99.7 rule (±1, 2, 3 SD)
  - Mean = median = mode
- Positive skew: tail extends RIGHT; mean > median > mode (income distribution)
- Negative skew: tail extends LEFT; mean < median < mode (easy exam)
- Mean chases the tail; identify from mean vs median comparison
- Trap: tail direction names the skew, NOT the peak direction
- Bimodal: two peaks → two subpopulations

HYPOTHESIS TESTING:
- H₀ (null): no effect | H₁ (alternative): there is an effect
- p-value: probability of results at least this extreme IF H₀ is true
  - p < 0.05 → reject H₀ (statistically significant)
  - p ≥ 0.05 → fail to reject H₀ (never "accept H₀")
  - Small p ≠ large effect | p < 0.05 does NOT mean 95% probability hypothesis is true
- Alpha (α): significance threshold (usually 0.05); Type I error rate

TYPE I AND TYPE II ERRORS:
- Type I (α, false positive): reject H₀ when it's true (fire alarm with no fire)
- Type II (β, false negative): fail to reject H₀ when it's false (alarm doesn't go off)
- α and β inversely related (unless sample size changes)

STATISTICAL POWER:
- Power = 1 − β = probability of correctly detecting a real effect
- Increases with: larger n (most common way), larger effect size, higher α, less variability, one-tailed test
- Target ≥ 0.80 (80%)
- Large n can give p < 0.05 with clinically meaningless tiny effect

CONFIDENCE INTERVALS:
- 95% CI: if repeated 100 times, ~95 intervals contain true parameter
- NOT "95% probability true value is in this specific interval"
- 95% CI for mean difference not including 0 → p < 0.05 (significant)
- 95% CI for RR or OR not including 1 → significant association
- Wider CI = less precision (smaller n or more variability)

EFFECT SIZE:
- Cohen's d = (mean₁ − mean₂)/pooled SD (small ≈0.2, medium ≈0.5, large ≈0.8)
- Statistical significance ≠ practical significance; need effect size too

STATISTICAL TESTS (Kaplan gap — know when to use, not how to calculate):
- t-test: compare means of 2 groups (1 categorical IV, 1 continuous DV)
  - Independent: different groups | Paired: same group at 2 time points
- ANOVA: compare means of 3+ groups (avoids inflated Type I error from multiple t-tests)
  - Significant ANOVA → need post-hoc tests (Tukey) to find which groups differ
  - Factorial ANOVA: tests main effects + interactions
- Chi-square: test association between categorical variables (observed vs expected frequencies)
- Pearson's r (correlation): strength/direction of linear relationship (−1 to +1)
  - r² = % of variance in Y explained by X
  - CORRELATION ≠ CAUSATION (third variable problem + directionality)
- Regression: predict DV from IV(s); Y = a + bX; slope b = change in Y per unit X
- Decision: 2 group means → t-test | 3+ group means → ANOVA | both categorical → chi-square | 2 continuous → correlation | predicting → regression

EPIDEMIOLOGICAL MEASURES (Kaplan gap):
- Incidence: NEW cases in time period / population at risk (cohort studies)
- Prevalence: ALL cases at one time point / total population (cross-sectional)
- Prevalence ≈ incidence × duration
- Relative Risk (RR): risk in exposed / risk in unexposed (cohort studies; RR > 1 = increased risk)
- Odds Ratio (OR) = (a×d)/(b×c) from 2×2 table (case-control; for rare diseases OR ≈ RR)
- ARR = risk_control − risk_treatment | NNT = 1/ARR
- Sensitivity = TP/(TP+FN) = true positive rate (SnNout: sensitive test negative → rules OUT)
- Specificity = TN/(TN+FP) = true negative rate (SpPin: specific test positive → rules IN)
- Sensitivity/specificity INTRINSIC to test; don't change with prevalence
- PPV = TP/(TP+FP) | NPV = TN/(TN+FN) — DEPEND ON PREVALENCE
  - Prevalence↑: PPV↑, NPV↓ | Prevalence↓: PPV↓, NPV↑
  - Low prevalence → positive test mostly false positives (why we don't screen for rare diseases)

KEY RULES:
1. p < 0.05 means unlikely IF H₀ true (not proof of hypothesis)
2. Statistical significance ≠ practical significance (need effect size)
3. Correlation ≠ causation
4. Sensitivity/specificity are test-intrinsic; PPV/NPV change with prevalence
5. Prevalence = incidence × duration; cross-sectional = prevalence; cohort = incidence
6. RR for cohort; OR for case-control; for rare diseases OR ≈ RR

CHARTS/GRAPHS:
- Bar graph: discrete categories | Histogram: continuous distribution (look for shape)
- Box plot: median, IQR, range, outliers | Scatter plot: correlation direction and strength
- Kaplan-Meier: survival curves (proportion event-free over time)
- Reading tables: identify rows vs columns; cell values (frequencies, means, %); contingency table → chi-square; mean ± SD → t-test/ANOVA

Kaplan: Physics Ch 12
→ Deep dive: research/PhysicsMath/Ch12_Statistics.md
