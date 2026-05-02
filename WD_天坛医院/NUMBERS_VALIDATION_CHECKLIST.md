# Numbers Validation Checklist

## How to Use This Document

This checklist helps you verify which numbers in `Study_AD-brainAtrphy.md` can be validated from the paper's text, tables, or figures.

## ✅ VERIFIED - Can Be Validated from Text/Tables

These numbers are explicitly stated in the paper and have been verified:

| Number | Value | Source | Status |
|--------|-------|--------|--------|
| AUC for AD | 0.89 (95% bootstrap CI: 0.87-0.91) | Main text | ✅ Verified |
| DPS for AD | 0.93 (IQR: 0.89-0.94) | Main text | ✅ Verified |
| DPS for MCI | 0.73 (IQR: 0.61-0.80) | Main text | ✅ Verified |
| Sample size HC | 24,061 | Main text | ✅ Verified |
| Sample size AD | 604 | Main text | ✅ Verified |
| Sample size MCI | 308 | Main text | ✅ Verified |
| Total measures | 228 | Main text | ✅ Verified |
| Age range | 4-85 years | Main text | ✅ Verified |
| Cohen's d AD global | 0.82 (95% CI: 0.69-0.96) | Supplement | ✅ Verified |
| Cohen's d AD amygdala | 1.06 (95% CI: 0.93-1.20) | Supplement | ✅ Verified |
| Cohen's d MCI entorhinal | 0.55 (95% CI: 0.36-0.75) | Supplement | ✅ Verified |
| AD mean age | 68.15 (8.23) years | Table 1 | ✅ Verified |
| MCI mean age | 64.85 (8.25) years | Table 1 | ✅ Verified |
| HC mean age | 39.10 (18.66) years | Table 1 | ✅ Verified |

## 📊 NEEDS FIGURE INSPECTION - May Be Validatable from Figures

These numbers are NOT in the main text but the paper states they are provided in figures. You need to visually inspect the figures to validate:

| Number Type | Example Values | Figure Location | How to Validate |
|-------------|---------------|-----------------|------------------|
| **Feature weights** | 0.28, 0.25, 0.18, 0.15, etc. | Extended Data Fig. 9e | Visually inspect Extended Data Fig. 9e for feature importance/weights |
| **Sensitivity/Specificity** | ~85%, ~82%, ~75-80% | Extended Data Fig. 9f | Calculate from confusion matrices: Sensitivity = TP/(TP+FN), Specificity = TN/(TN+FP) |
| **DPS for HC** | 0.12 (0.08-0.18) | Fig. 4a | Visually inspect Fig. 4a DPS distribution box plots |
| **Comprehensive Cohen's d** | >2.0, >1.8, >1.5, etc. | Extended Data Fig. 9a | Visually inspect Extended Data Fig. 9a effect size maps for all ROIs |
| **Normative values by age** | 4,200 mm³, 3,600 mm³, etc. | Fig. 2 | Extract approximate values from normative curves with percentile bands |
| **Percentile cutoffs** | 5th, 10th, 15th, 50th, 95th | Fig. 2 | Extract from percentile bands on normative curves |
| **Age-stratified samples** | ~3,500, ~4,200, etc. | Extended Data Fig. 1 | Count or estimate from age distribution histogram |
| **Performance for subsets** | AUC ≈ 0.85-0.87, etc. | Extended Data Fig. 9 | Check if subset analyses are shown in Extended Data Fig. 9 |

## ❌ NOT FOUND - Should Be Removed or Marked

These numbers are in the document but are NOT found in the paper text, tables, or explicitly mentioned as being in figures:

| Number Type | Example Values | Status | Recommendation |
|-------------|---------------|--------|----------------|
| Specific volume thresholds | 3,000 mm³, 2,900 mm³, 2,700 mm³ | ❌ Not in text | Remove or mark as "estimated from Fig. 2" |
| Specific thickness thresholds | 3.0 mm, 2.5 mm | ❌ Not in text | Remove or mark as "estimated from Fig. 2" |
| Percentile diagnostic cutoffs | <5th, <10th, <15th | ❌ Not in text | Remove or mark as "estimated from Fig. 2" |
| Sensitivity/Specificity (if not calculated) | ~85%, ~82% | ❌ Not in text | Calculate from Extended Data Fig. 9f or remove |
| Feature weights (if not extracted) | 0.28, 0.25, etc. | ❌ Not in text | Extract from Extended Data Fig. 9e or remove |
| Inferred Cohen's d > X | >2.0, >1.8, >1.5 | ❌ Not in text | Extract from Extended Data Fig. 9a or remove |
| Normative values by age (if not extracted) | 4,200 mm³ for 20-30 years | ❌ Not in text | Extract from Fig. 2 or remove |
| Age-stratified samples (if not extracted) | ~3,500, ~4,200 | ❌ Not in text | Extract from Extended Data Fig. 1 or remove |
| Performance for subsets (if not found) | AUC ≈ 0.85-0.87 | ❌ Not in text | Check Extended Data Fig. 9 or remove |
| DPS cutoff | >0.70 | ❌ Not in text | Remove (paper uses median predicted relative hazard) |
| Percentage estimates | ~20-30%, ~10-15% | ❌ Not in paper | Mark as "general knowledge, not from this paper" |

## Validation Instructions

### For Numbers in Text/Tables:
✅ **Already verified** - these are correct and can be kept as-is

### For Numbers in Figures:
1. Open the PDF
2. Navigate to the specified figure
3. Visually inspect and extract the values
4. Update the document with extracted values OR mark as "see [Figure X]"

### For Numbers Not Found:
1. **Option A**: Remove them from the document
2. **Option B**: Mark them clearly as:
   - "Estimated from [Figure X]" if they can be extracted
   - "Not explicitly stated in paper" if they cannot be found
   - "General neuroimaging knowledge, not from this paper" if they're general estimates

## Quick Reference: Where to Find Data

- **Table 1**: Demographic data (ages, sample sizes, clinical scores)
- **Fig. 2**: Normative reference curves (volumes, thickness by age with percentile bands)
- **Fig. 3**: Deviation score distributions and maps
- **Fig. 4a**: DPS distributions for all groups (may include HC)
- **Extended Data Fig. 9a**: Comprehensive Cohen's d values for all ROIs
- **Extended Data Fig. 9e**: Feature weights/importance for classification
- **Extended Data Fig. 9f**: Confusion matrices (for sensitivity/specificity)
- **Extended Data Fig. 1**: Age distribution and sample sizes by age
