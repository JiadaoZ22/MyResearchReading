# Verification Report for Study_AD-brainAtrphy.md

## Numbers Verified from Paper

### ✅ VERIFIED (Explicitly stated in paper):

1. **AUC for AD classification**: 0.89 (95% bootstrap CI 0.87-0.91) ✓
   - Source: Main paper, Fig. 4a

2. **DPS (Disease Propensity Score) for AD**: 0.93 (IQR 0.89-0.94) ✓
   - Source: Main paper, Fig. 4a

3. **DPS for MCI**: 0.73 (IQR 0.61-0.80) ✓
   - Note: Document says 0.75 (0.65-0.85) - NEEDS CORRECTION

4. **DPS for HC**: Not explicitly stated as 0.12 (0.08-0.18) in main text
   - Status: NEEDS VERIFICATION

5. **Cohen's d values (explicitly stated)**:
   - AD global deviation scores: 0.82 (95% CI 0.69-0.96) ✓
   - AD left amygdala volume: 1.06 (95% CI 0.93-1.20) ✓
   - MCI left entorhinal volume: 0.55 (95% CI 0.36-0.75) ✓
   - CSVD right thalamus volume: 0.58 (95% CI 0.45-0.71) ✓

6. **Sample size**: 24,061 healthy Chinese individuals ✓

7. **Age range**: 4-85 years ✓

### ❌ NOT FOUND in paper (likely inferred/estimated):

1. **Sensitivity/Specificity values**:
   - ~85% sensitivity - NOT FOUND
   - ~82% specificity - NOT FOUND
   - ~75-80% sensitivity for hippocampus - NOT FOUND
   - ~70-75% specificity for hippocampus - NOT FOUND
   - All other sensitivity/specificity values - NOT FOUND

2. **Feature weights** (0.28, 0.25, 0.18, etc.):
   - NOT FOUND in main text
   - Paper mentions "contributing global and regional deviation scores" in Extended Data Fig. 9e, but specific weights not stated

3. **Specific volume thresholds**:
   - <3,000 mm³ for hippocampus - NOT FOUND
   - <2,900 mm³ for age 65-70 - NOT FOUND
   - All specific mm³ values - NOT FOUND

4. **Specific percentile cutoffs**:
   - <5th percentile for hippocampus - NOT FOUND
   - <10th percentile for entorhinal - NOT FOUND
   - <15th percentile for precuneus - NOT FOUND
   - All percentile thresholds - NOT FOUND

5. **Cohen's d values (inferred, not stated)**:
   - Hippocampus: Cohen's d > 2.0 - NOT FOUND (no specific value given)
   - Entorhinal: Cohen's d > 1.8 - NOT FOUND
   - Amygdala: Cohen's d > 1.5 - NOT FOUND (actual value is 1.06)
   - All other Cohen's d > X values - NOT FOUND

6. **Normative volume values by age**:
   - 4,200 mm³ for 20-30 years - NOT FOUND (paper provides models, not tabulated values)
   - All specific volume values by age - NOT FOUND

7. **Sample sizes by age group**:
   - ~3,500 for 50-60 years - NOT FOUND
   - ~4,200 for 60-70 years - NOT FOUND
   - All age-stratified sample sizes - NOT FOUND

8. **Performance metrics for different feature sets**:
   - AUC ≈ 0.85-0.87 for top 10 ROIs - NOT FOUND
   - AUC ≈ 0.75-0.80 for single ROI - NOT FOUND
   - AUC ≈ 0.70-0.75 for raw volumes - NOT FOUND

9. **DPS cutoff**: >0.70 - NOT FOUND (paper uses median predicted relative hazard as cutoff)

10. **Absolute thickness values**:
    - <3.0 mm for entorhinal - NOT FOUND
    - All specific mm thickness values - NOT FOUND

## Recommendations

All numbers that are NOT explicitly stated in the paper should be:
1. Marked as "estimated/inferred" or "not explicitly stated in paper"
2. Removed if they cannot be verified
3. Qualified with notes about their source (e.g., "estimated from figures", "inferred from general AD literature")
