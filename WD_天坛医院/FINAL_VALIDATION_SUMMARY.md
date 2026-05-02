# Final Validation Summary for Study_AD-brainAtrphy.md

## ✅ Numbers VERIFIED from Paper Text/Tables:

### From Main Text:
1. **AUC for AD**: 0.89 (95% bootstrap CI: 0.87-0.91) ✓
2. **DPS for AD**: 0.93 (IQR: 0.89-0.94) ✓
3. **DPS for MCI**: 0.73 (IQR: 0.61-0.80) ✓
4. **Sample size HC**: 24,061 ✓
5. **Sample size AD**: 604 ✓
6. **Sample size MCI**: 308 ✓
7. **Total measures**: 228 ✓
8. **Age range**: 4-85 years ✓

### From Supplement Text:
9. **Cohen's d AD global**: 0.82 (95% CI: 0.69-0.96) ✓
10. **Cohen's d AD left amygdala**: 1.06 (95% CI: 0.93-1.20) ✓
11. **Cohen's d MCI left entorhinal**: 0.55 (95% CI: 0.36-0.75) ✓

### From Table 1 (Extracted):
12. **AD age**: 68.15 (8.23) years ✓
13. **MCI age**: 64.85 (8.25) years ✓
14. **HC age**: 39.10 (18.66) years ✓
15. **HC females**: 12,614 (52.43%) ✓

## 📊 Numbers That MAY Be in Figures (Need Visual Inspection):

These numbers are referenced in the document but are NOT in the main text. They may be extractable from figures:

1. **Feature weights** (0.28, 0.25, 0.18, etc.)
   - **Location**: Extended Data Fig. 9e
   - **Status**: Paper says "contributing scores" are provided, but weights not in text
   - **Action**: Extract from Extended Data Fig. 9e or remove

2. **Sensitivity/Specificity values** (~85%, ~82%, etc.)
   - **Location**: Extended Data Fig. 9f (confusion matrices)
   - **Status**: Can be calculated from confusion matrices
   - **Action**: Calculate from Extended Data Fig. 9f or remove

3. **DPS for Healthy Controls** (0.12, 0.08-0.18)
   - **Location**: Fig. 4a (DPS distributions)
   - **Status**: Not in main text
   - **Action**: Extract from Fig. 4a or mark as "not stated"

4. **Comprehensive Cohen's d for all ROIs** (>2.0, >1.8, etc.)
   - **Location**: Extended Data Fig. 9a
   - **Status**: Only largest effect sizes in text
   - **Action**: Extract from Extended Data Fig. 9a or remove inferred values

5. **Normative volume/thickness values by age** (4,200 mm³, 3,600 mm³, etc.)
   - **Location**: Fig. 2 (normative curves)
   - **Status**: Curves shown, but values not tabulated
   - **Action**: Extract from Fig. 2 or mark as "approximate from figures"

6. **Percentile cutoffs** (5th, 10th, 15th, 50th, 95th)
   - **Location**: Fig. 2 (percentile bands on curves)
   - **Status**: Bands shown, but specific values not tabulated
   - **Action**: Extract from Fig. 2 or mark as "approximate from figures"

7. **Age-stratified sample sizes** (~3,500, ~4,200, etc.)
   - **Location**: Extended Data Fig. 1 or Fig. 2
   - **Status**: Distribution shown, but sizes not tabulated
   - **Action**: Extract from figures or remove

8. **Performance metrics for feature subsets** (AUC ≈ 0.85-0.87, etc.)
   - **Location**: Extended Data Fig. 9 (various panels)
   - **Status**: Not reported in main text
   - **Action**: Check Extended Data Fig. 9 or remove

## ❌ Numbers NOT Found (Should Be Removed or Clearly Marked):

These numbers are in the document but are NOT found in the paper text, tables, or explicitly mentioned as being in figures:

1. **All specific volume thresholds** (3,000 mm³, 2,900 mm³, 2,700 mm³, etc.)
   - **Status**: Not in text
   - **Action**: Remove or mark as "estimated from Fig. 2"

2. **All specific thickness thresholds** (3.0 mm, 2.5 mm, etc.)
   - **Status**: Not in text
   - **Action**: Remove or mark as "estimated from Fig. 2"

3. **All specific percentile diagnostic cutoffs** (<5th, <10th, <15th percentile)
   - **Status**: Not in text
   - **Action**: Remove or mark as "estimated from Fig. 2"

4. **All sensitivity/specificity percentages** (~85%, ~82%, ~75-80%, etc.)
   - **Status**: Not in text (can calculate from confusion matrices)
   - **Action**: Calculate from Extended Data Fig. 9f or remove

5. **All feature weights** (0.28, 0.25, 0.18, 0.15, 0.14, 0.12, 0.11, 0.09, 0.08, 0.07)
   - **Status**: Not in text
   - **Action**: Extract from Extended Data Fig. 9e or remove

6. **All inferred Cohen's d > X values** (>2.0, >1.8, >1.5, >1.4, >1.2, >1.1, >1.0, >0.9, >0.8)
   - **Status**: Not in text (only specific values like 1.06, 0.82, 0.55 are stated)
   - **Action**: Extract from Extended Data Fig. 9a or remove

7. **All normative values by age group** (4,200 mm³ for 20-30 years, etc.)
   - **Status**: Not tabulated in text
   - **Action**: Extract from Fig. 2 or remove

8. **All age-stratified sample sizes** (~3,500, ~4,200, ~2,800, ~800)
   - **Status**: Not in text
   - **Action**: Extract from Extended Data Fig. 1 or remove

9. **All performance metrics for subsets** (AUC ≈ 0.85-0.87, 0.75-0.80, 0.70-0.75)
   - **Status**: Not in text
   - **Action**: Check Extended Data Fig. 9 or remove

10. **DPS cutoff** (>0.70)
    - **Status**: Not in text (paper uses median predicted relative hazard)
    - **Action**: Remove or clarify

11. **Percentage estimates** (~20-30%, ~10-15%, ~5-7%, ~5-8%)
    - **Status**: Not in paper (these appear to be general knowledge estimates)
    - **Action**: Mark as "general neuroimaging knowledge, not from this paper"

## Recommendations:

1. **Keep all ✓ verified numbers** - these are correct
2. **For numbers in figures**: Add clear notes like "See Extended Data Fig. 9e for exact values"
3. **For numbers not found**: Either remove them or mark as "estimated/inferred from figures" with figure reference
4. **For general knowledge estimates**: Mark as "not from this paper" or remove

## Next Steps:

To complete validation, you would need to:
1. Visually inspect Extended Data Fig. 9e for feature weights
2. Visually inspect Extended Data Fig. 9f for confusion matrices (calculate sensitivity/specificity)
3. Visually inspect Extended Data Fig. 9a for comprehensive Cohen's d values
4. Visually inspect Fig. 2 for normative values by age
5. Visually inspect Extended Data Fig. 1 for age-stratified sample sizes
6. Visually inspect Fig. 4a for HC DPS values
