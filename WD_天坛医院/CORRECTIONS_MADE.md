# Corrections Made to Study_AD-brainAtrphy.md

## Summary of Verification and Corrections

### ✅ Numbers Verified and Corrected:

1. **DPS for MCI**: Changed from 0.75 (0.65-0.85) to **0.73 (IQR 0.61-0.80)** ✓
   - Source: Main paper, explicitly stated

2. **DPS for HC**: Changed to "Not explicitly stated" 
   - The paper does not provide DPS values for healthy controls

3. **AUC**: Confirmed **0.89 (95% bootstrap CI: 0.87-0.91)** ✓
   - Corrected to specify "bootstrap CI" instead of just "CI"

### ❌ Numbers Removed or Qualified (Not Found in Paper):

1. **All Sensitivity/Specificity values** (~85%, ~82%, ~75-80%, etc.)
   - Status: Removed - not found in paper
   - Added note: "Sensitivity and specificity values are not explicitly reported"

2. **All Feature Weights** (0.28, 0.25, 0.18, etc.)
   - Status: Removed - not found in main text
   - Added note: "Specific feature weights are not explicitly stated in the main text"

3. **All Specific Volume Thresholds** (3,000 mm³, 2,900 mm³, etc.)
   - Status: Removed - not found in paper
   - Added note: "Specific percentile cutoffs and absolute volumes are not explicitly reported"

4. **All Percentile Cutoffs** (<5th, <10th, <15th percentile)
   - Status: Removed - not found in paper
   - Added note: "Specific percentile thresholds are not explicitly reported"

5. **All Cohen's d > X values** (>2.0, >1.8, >1.5, etc.)
   - Status: Removed inferred values
   - Kept only explicitly stated values:
     - AD global: 0.82 (95% CI 0.69-0.96)
     - AD left amygdala: 1.06 (95% CI 0.93-1.20)
     - MCI left entorhinal: 0.55 (95% CI 0.36-0.75)

6. **All Normative Volume Values by Age** (4,200 mm³, 3,600 mm³, etc.)
   - Status: Removed - paper provides models, not tabulated values
   - Added note: "Normative references are provided as statistical models (GAMLSS)"

7. **All Age-Stratified Sample Sizes** (~3,500, ~4,200, etc.)
   - Status: Removed - not found in paper
   - Added note: "Age distribution is shown in Figure 2, but specific sample sizes by age group are not tabulated"

8. **Performance Metrics for Feature Subsets** (AUC ≈ 0.85-0.87, etc.)
   - Status: Removed - not found in paper
   - Added note: "The paper does not explicitly report performance for different feature subsets"

9. **DPS Cutoff** (>0.70)
   - Status: Removed - paper uses median predicted relative hazard as cutoff

10. **All Absolute Thickness Values** (<3.0 mm, etc.)
    - Status: Removed - not found in paper
    - Added note: "Specific absolute thickness values are not explicitly reported"

### ✅ Information Added from Paper:

1. **Explicitly stated Cohen's d values** with confidence intervals
2. **Correct DPS values** for AD and MCI
3. **Clarifications** that normative references are provided as statistical models, not tabulated values
4. **Notes** explaining what information is available vs. what needs to be calculated from models

## Key Principle Applied:

**Only include numbers that are explicitly stated in the main text. All inferred, estimated, or extracted-from-figures values have been removed or clearly marked with notes. However, many specific values ARE available in figures and Extended Data figures, and the document now includes references to where readers can find this information (e.g., Extended Data Fig. 9e for feature weights, Extended Data Fig. 9f for confusion matrices, Fig. 2 for normative curves).**

## Important Update:

After user feedback, the document has been updated to acknowledge that:
- **Extended Data Fig. 9e** contains feature weights/importance scores
- **Extended Data Fig. 9f** contains confusion matrices (from which sensitivity/specificity can be calculated)
- **Extended Data Fig. 9a** contains comprehensive Cohen's d values for all ROIs
- **Fig. 2** contains normative reference curves from which values can be extracted
- **Fig. 3** contains deviation score distributions

See `FIGURES_TABLES_REFERENCE.md` for a complete guide to where specific data can be found in figures and tables.
