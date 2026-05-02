# Number Validation Checklist for Study_AD-brainAtrphy.md

## Numbers That Can Be Validated from Paper Text/Tables

### ✅ VERIFIED from Main Text:

1. **AUC for AD**: 0.89 (95% bootstrap CI: 0.87-0.91) ✓
   - Source: Main text, explicitly stated
   - Validation: Found in paper text

2. **DPS for AD**: 0.93 (IQR: 0.89-0.94) ✓
   - Source: Main text, explicitly stated
   - Validation: Found in paper text

3. **DPS for MCI**: 0.73 (IQR: 0.61-0.80) ✓
   - Source: Main text, explicitly stated
   - Validation: Found in paper text

4. **Sample size (HC)**: 24,061 individuals ✓
   - Source: Main text, explicitly stated
   - Validation: Found in paper text

5. **Sample size (ENA reference)**: 101,457 individuals ✓
   - Source: Main text, explicitly stated
   - Validation: Found in paper text

6. **Age range**: 4-85 years ✓
   - Source: Main text, explicitly stated
   - Validation: Found in paper text

7. **Cohen's d - AD global**: 0.82 (95% CI: 0.69-0.96) ✓
   - Source: Supplement, explicitly stated
   - Validation: Found in supplement text

8. **Cohen's d - AD left amygdala**: 1.06 (95% CI: 0.93-1.20) ✓
   - Source: Supplement, explicitly stated
   - Validation: Found in supplement text

9. **Cohen's d - MCI left entorhinal**: 0.55 (95% CI: 0.36-0.75) ✓
   - Source: Supplement, explicitly stated
   - Validation: Found in supplement text

10. **Total measures**: 228 ✓
    - Source: Main text, explicitly stated
    - Validation: Found in paper text

### 📊 Numbers That May Be in Figures/Tables (Need Visual Inspection):

1. **DPS for Healthy Controls**: 
   - Status: Not found in main text
   - Possible location: Fig. 4a (DPS distributions)
   - Action: Check Fig. 4a for HC DPS values

2. **Sensitivity/Specificity values**:
   - Status: Not found in main text
   - Possible location: Extended Data Fig. 9f (confusion matrices)
   - Action: Calculate from confusion matrices in Extended Data Fig. 9f

3. **Feature weights** (0.28, 0.25, 0.18, etc.):
   - Status: Not found in main text
   - Possible location: Extended Data Fig. 9e (contributing features)
   - Action: Extract from Extended Data Fig. 9e

4. **Comprehensive Cohen's d values for all ROIs**:
   - Status: Only largest effect sizes in main text
   - Possible location: Extended Data Fig. 9a (effect size maps)
   - Action: Extract from Extended Data Fig. 9a

5. **Normative volume/thickness values by age**:
   - Status: Not tabulated in main text
   - Possible location: Fig. 2 (normative curves)
   - Action: Extract approximate values from Fig. 2 curves

6. **Percentile cutoffs** (5th, 10th, 15th, etc.):
   - Status: Not explicitly stated
   - Possible location: Fig. 2 (normative curves with percentile bands)
   - Action: Extract from Fig. 2 percentile bands

7. **Age-stratified sample sizes**:
   - Status: Not tabulated in main text
   - Possible location: Extended Data Fig. 1 or Fig. 2 (age distribution)
   - Action: Extract from Extended Data Fig. 1 or Fig. 2

8. **Performance metrics for feature subsets**:
   - Status: Not reported in main text
   - Possible location: Extended Data Fig. 9 (various panels)
   - Action: Check Extended Data Fig. 9 for subset analyses

### ❌ Numbers That Are NOT in Paper (Should Be Removed or Marked as Inferred):

Based on text extraction, the following numbers appear to be inferred/estimated and are NOT explicitly stated:

1. **All specific volume thresholds** (e.g., 3,000 mm³, 2,900 mm³)
   - Status: Not found in text
   - Action: Mark as "estimated from figures" or remove

2. **All specific thickness thresholds** (e.g., 3.0 mm, 2.5 mm)
   - Status: Not found in text
   - Action: Mark as "estimated from figures" or remove

3. **All specific percentile cutoffs** (e.g., <5th, <10th percentile)
   - Status: Not found in text
   - Action: Mark as "estimated from figures" or remove

4. **All sensitivity/specificity percentages** (e.g., ~85%, ~82%)
   - Status: Not found in text
   - Action: Calculate from Extended Data Fig. 9f or remove

5. **All feature weights** (e.g., 0.28, 0.25, 0.18)
   - Status: Not found in text
   - Action: Extract from Extended Data Fig. 9e or remove

6. **All inferred Cohen's d > X values** (e.g., >2.0, >1.8)
   - Status: Not found in text (only specific values like 1.06, 0.82, 0.55 are stated)
   - Action: Extract from Extended Data Fig. 9a or remove

7. **All normative values by age group** (e.g., 4,200 mm³ for 20-30 years)
   - Status: Not tabulated in text
   - Action: Extract from Fig. 2 or remove

8. **All age-stratified sample sizes** (e.g., ~3,500 for 50-60 years)
   - Status: Not found in text
   - Action: Extract from Extended Data Fig. 1 or remove

## Validation Strategy

### For Numbers in Text:
✅ Already verified - these are correct

### For Numbers in Figures/Tables:
1. **Extended Data Fig. 9e**: Check for feature weights
2. **Extended Data Fig. 9f**: Check confusion matrices for sensitivity/specificity
3. **Extended Data Fig. 9a**: Check for comprehensive Cohen's d values
4. **Fig. 2**: Check normative curves for volume/thickness values by age
5. **Fig. 3**: Check deviation score distributions
6. **Fig. 4a**: Check DPS distributions (may include HC values)
7. **Extended Data Fig. 1**: Check age distribution for sample sizes

### Recommendation:
Since I cannot directly view PDF images, the document should:
1. Keep all verified numbers from text ✓
2. Reference specific figures/tables for numbers that may be there
3. Remove or clearly mark as "estimated/inferred" any numbers that cannot be verified
