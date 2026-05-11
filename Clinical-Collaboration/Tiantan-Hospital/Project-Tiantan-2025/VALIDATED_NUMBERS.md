# Validated Numbers from Paper (Text + Tables)

## ✅ Numbers Verified from Main Text:

1. **AUC for AD classification**: 0.89 (95% bootstrap CI: 0.87-0.91) ✓
   - Location: Main text, explicitly stated
   - Quote: "disease-specific classification models achieved AUC values of 0.89 (95% bootstrap CI 0.87–0.91) for AD"

2. **DPS for AD**: 0.93 (IQR: 0.89-0.94) ✓
   - Location: Main text, explicitly stated
   - Quote: "0.93 (IQR 0.89–0.94) for AD"

3. **DPS for MCI**: 0.73 (IQR: 0.61-0.80) ✓
   - Location: Main text, explicitly stated
   - Quote: "0.73 (interquartile range (IQR) 0.61–0.80) for MCI"

4. **Sample sizes**:
   - HC: 24,061 ✓ (main text)
   - AD: 604 ✓ (main text)
   - MCI: 308 ✓ (main text)
   - PD: 1,226 ✓ (main text)
   - CSVD: 864 ✓ (main text)
   - MS: 519 ✓ (main text)
   - NMOSD: 411 ✓ (main text)
   - Total disease: 3,932 ✓ (main text)

5. **Age ranges**: 4-85 years ✓ (main text)

6. **Cohen's d values** (from supplement):
   - AD global: 0.82 (95% CI: 0.69-0.96) ✓
   - AD left amygdala: 1.06 (95% CI: 0.93-1.20) ✓
   - MCI left entorhinal: 0.55 (95% CI: 0.36-0.75) ✓

7. **Total measures**: 228 ✓ (main text)

8. **Peak ages** (from main text):
   - GMV peak: 7.1 years (95% bootstrap CI: 6.7-7.6) for Chinese
   - GMV peak: 5.9 years (95% bootstrap CI: 5.8-6.1) for ENA
   - Difference: 1.2 years later for Chinese ✓

## 📊 Numbers from Table 1 (Extracted):

From Table 1 (Demographic and clinical information):

**Age (mean (s.d.)), years**:
- HC: 39.10 (18.66) ✓
- MCI: 64.85 (8.25) ✓
- AD: 68.15 (8.23) ✓
- PD: 61.26 (9.45) ✓
- CSVD: 60.57 (10.08) ✓
- MS: 36.28 (12.07) ✓
- NMOSD: 43.42 (13.86) ✓

**Sex distribution**:
- HC: 12,614 females (52.43%) ✓
- Disease groups: 2,187 females (55.62%) ✓

**MMSE scores** (mean (s.d.)):
- HC: 27.91 (2.88) ✓
- MCI: 25.55 (3.24) ✓
- AD: 17.24 (7.13) ✓

**MoCA scores** (mean (s.d.)):
- HC: 25.32 (3.40) ✓
- MCI: 20.79 (4.01) ✓
- AD: 12.65 (6.59) ✓

## 🔍 Numbers That Need Figure Inspection:

These numbers are NOT in the main text but may be extractable from figures:

1. **DPS for Healthy Controls**
   - Check: Fig. 4a (DPS distributions)

2. **Sensitivity/Specificity**
   - Check: Extended Data Fig. 9f (confusion matrices)
   - Can calculate: TP, FP, TN, FN from confusion matrices

3. **Feature weights** (0.28, 0.25, 0.18, etc.)
   - Check: Extended Data Fig. 9e (contributing features)

4. **Comprehensive Cohen's d for all ROIs**
   - Check: Extended Data Fig. 9a (effect size maps)

5. **Normative values by age** (volumes, thickness)
   - Check: Fig. 2 (normative curves with percentile bands)

6. **Age-stratified sample sizes**
   - Check: Extended Data Fig. 1 (age distribution)

7. **Percentile cutoffs** (5th, 10th, 50th, 95th)
   - Check: Fig. 2 (normative curves with percentile bands)

## ❌ Numbers NOT Found (Should Be Removed or Marked):

Based on comprehensive text search, these are NOT in the paper:

1. All specific volume thresholds (3,000 mm³, 2,900 mm³, etc.)
2. All specific thickness thresholds (3.0 mm, 2.5 mm, etc.)
3. All specific percentile diagnostic cutoffs (<5th, <10th, etc.)
4. All sensitivity/specificity percentages (~85%, ~82%, etc.) - need to calculate from confusion matrices
5. All feature weights (0.28, 0.25, etc.) - need to extract from Extended Data Fig. 9e
6. All inferred Cohen's d > X values (>2.0, >1.8, etc.) - need to extract from Extended Data Fig. 9a
7. All normative values by age group (4,200 mm³, etc.) - need to extract from Fig. 2
8. All age-stratified sample sizes (~3,500, etc.) - need to extract from Extended Data Fig. 1

## Recommendation:

The document should:
1. ✅ Keep all verified numbers (marked with ✓)
2. 📊 Reference specific figures for numbers that may be there
3. ❌ Remove or clearly mark as "estimated/inferred from figures" any numbers that cannot be verified from text/tables
