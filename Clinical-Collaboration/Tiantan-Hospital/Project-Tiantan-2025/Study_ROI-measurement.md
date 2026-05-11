# Analysis of Brain ROI Count in "Charting brain morphology in international healthy and neurological populations"

## Key Finding

**The authors analyzed 228 total brain structural measures, but NOT all are from the Desikan-Killiany atlas.**

## Quick Summary Table

| Category | Count | Source | FreeSurfer Pipeline |
|----------|-------|--------|-------------------|
| **Cortical measures** | 204 | Desikan-Killiany atlas | `aparc.stats` |
| **Global measures** | 8 | Whole-brain summaries | `aseg.stats` |
| **Subcortical measures** | 16 | Subcortical structures | `aseg.stats` |
| **TOTAL** | **228** | **All from FreeSurfer** | Mixed pipelines |

**Answer to "What are the remaining 24 measures (228 - 204 = 24)?"**
- 8 global measures (whole-brain summaries, including sGMV)
- 16 subcortical volume measures (individual subcortical structures)
- **All 24 are from FreeSurfer's aseg pipeline, NOT from Desikan-Killiany atlas**

**Note**: The paper does NOT explicitly list which specific subcortical structures are included. The subcortical list is based on standard FreeSurfer aseg segmentation labels.

## Exact Breakdown of 228 Measures

### 1. **Cortical Measures from Desikan-Killiany Atlas: 204 measures**
   - **34 cortical regions per hemisphere** = 68 total cortical regions
   - **3 measures per region**: volume, cortical thickness, surface area
   - **Calculation**: 68 regions × 3 measures = **204 measures**
   - **Source**: FreeSurfer `aparc.stats` files (Desikan-Killiany parcellation)

### 2. **Global Measures (from FreeSurfer aseg.stats): 8 measures**
   These are whole-brain measures calculated by FreeSurfer `recon all`, NOT from Desikan-Killiany atlas:
   1. Total cortical gray matter volume (GMV)
   2. Total cerebral white matter volume (WMV)
   3. Subcortical gray matter volume (sGMV)
   4. Ventricular volume (CSF) - calculated as difference between BrainSegVol and BrainSegVolNotVent
   5. Total cerebellar gray and white matter volume (Cerebellum)
   6. Total brain-stem volume (braistem)
   7. Mean cortical thickness (whole brain)
   8. Total surface area (whole brain)
   - **Source**: FreeSurfer `aseg.stats` files

### 3. **Subcortical Volume Measures (from FreeSurfer aseg): 16 measures**
   These are individual subcortical structure volumes, NOT from Desikan-Killiany atlas.

   **Confirmed by source code analysis** (Charting-Chinese-repo GAMLSS-DK model files and R script `Disease-application-normative-model.R` line 51): the paper's pipeline fits **exactly 16 bilateral subcortical regional volumes** (8 structures × 2 hemispheres). The R script selects `aseg.vol.table` column indices `c(6:9, 12:14, 16:17, 24:31, 69:71)` which includes indices 17 (Left.VentralDC) and 31 (Right.VentralDC). The `Models/GAMLSS/DK/aseg.vol.table/` directory contains exactly 18 .rds files: the 16 bilateral subcortical + Brain.Stem + cerebellum_total (the latter two are shared with the Global_feature directory).

   **Standard FreeSurfer aseg subcortical structures** (8 structures per hemisphere = 16 total):
      1. Thalamus (labels 10/49)
      2. Caudate (labels 11/50)
      3. Putamen (labels 12/51)
      4. Pallidum (labels 13/52)
      5. Hippocampus (labels 17/53)
      6. Amygdala (labels 18/54)
      7. Accumbens area (labels 26/58)
      8. VentralDC (labels 28/60) — **included as a regional measure** (verified by `Left.VentralDC_normative_model.rds` and `Right.VentralDC_normative_model.rds` in the published GAMLSS-DK models)

   **Note on Basal Forebrain**: Earlier speculation that Basal Forebrain (labels 865/866) might be included (yielding 18 measures) is **not supported** by the source code — no Basal Forebrain models exist in the published GAMLSS-DK normative models.

    - **Source**: FreeSurfer `aseg.stats` files (automatic subcortical segmentation)
    - **Reference**: GAMLSS-DK model directory (`aseg.vol.table/`) and R script column-index selection

## Verification: 204 + 8 + 16 = 228 ✓

**Confirmed by source code**: The exact breakdown is 204 cortical + 8 global + 16 subcortical = 228. Verified against the GAMLSS-DK model directory structure (9 .rds in `Global_feature/` [8 paper globals + TCV auxiliary], 18 .rds in `aseg.vol.table/` [16 bilateral subcortical + Brain.Stem + cerebellum_total], and 34 .rds × 6 in `lh/rh.aparc.{volume,area,thickness}.table/`).

## Answer to Your Questions

### Q1: How many brain ROIs did the authors analyze and use?
**Answer: 228 total structural measures** (not all are "ROIs" in the traditional sense - some are global measures)

### Q2: Are all 228 ROIs from Desikan-Killiany atlas studied?
**Answer: NO**

- **Desikan-Killiany atlas provides**: 68 cortical ROIs (34 per hemisphere)
- **From Desikan-Killiany**: 204 measures (68 ROIs × 3 measures each: volume, thickness, area)
- **NOT from Desikan-Killiany**:
   - **8 global measures** (whole-brain measures from FreeSurfer aseg.stats + aparc.stats)
   - **16 subcortical volume measures** (from FreeSurfer aseg segmentation, separate from Desikan-Killiany)

### Q3: What are the remaining 24 measures (228 - 204 = 24)?
**Answer: The remaining 24 measures consist of:**

1. **8 Global Measures** (from FreeSurfer `aseg.stats`):
   - These are whole-brain summary measures, not region-specific
   - All extracted from FreeSurfer's automatic segmentation pipeline

2. **16 Subcortical Volume Measures** (from FreeSurfer `aseg`):
    - Individual volumes of subcortical structures
    - **Confirmed by source code**: exactly 8 structures per hemisphere (16 total), including VentralDC — verified by GAMLSS-DK model files and R script column-index selection
    - All extracted from FreeSurfer's automatic subcortical segmentation

**All 24 remaining measures are from FreeSurfer**, but they come from the `aseg` (automatic subcortical segmentation) pipeline, NOT from the Desikan-Killiany cortical parcellation.

## Important Notes

1. **Desikan-Killiany atlas is cortical only**: It parcellates the cerebral cortex into 34 regions per hemisphere (68 total). It does NOT include subcortical structures or global measures.

2. **All measures come from FreeSurfer, but from different pipelines**:
   - **Cortical measures (204)**: From Desikan-Killiany parcellation via `aparc.stats` files
   - **Global measures (8)**: From `aseg.stats` files (whole-brain summaries)
   - **Subcortical measures (16)**: From `aseg.stats` files (automatic subcortical segmentation)

3. **The 228 includes measures, not just ROIs**: The count includes:
    - ROI-based measures (cortical regions: 204 measures, subcortical structures: 16 measures)
    - Global whole-brain measures (8 measures, not region-specific)

4. **What subcortical structures are included?**: The paper does NOT explicitly list the individual subcortical structures used as regional measures in the main text. The supplement only mentions 7 structures in the context of sGMV (aggregate global measure), not individual measures. However, **source code analysis confirms exactly 8 bilateral structures = 16 regional subcortical volumes** (including VentralDC):
    - Verified by `Models/GAMLSS/DK/aseg.vol.table/` containing `Left.VentralDC_normative_model.rds` and `Right.VentralDC_normative_model.rds`
    - Verified by R script `Disease-application-normative-model.R` line 51 selecting MR_measures.xlsx column indices `c(6:9, 12:14, 16:17, 24:31, 69:71)` — indices 17 and 31 = Left/Right.VentralDC
    - **Important nuance**: The global sGMV scalar (one of the 8 global measures) sums only 7 bilateral structures (excludes VentralDC), but VentralDC IS included as a separate regional subcortical measure
    - **Reference**: GAMLSS-DK model directory and R script (source-code-verified, not just inferred from FreeSurfer documentation)

## Source Information

From the paper:
- Main paper: "Briefly, a total of 228 brain structural measures were extracted at both the global and regional levels."
- Supplement: "Regional volume, cortical thickness and surface area were estimated for each of 34 cortical regions defined by the Desikan–Killiany parcellation atlas"
- Supplement: Subcortical gray matter volume (sGMV) includes: "thalamus, caudate nucleus, putamen, pallidum, hippocampus, amygdala, and nucleus accumbens area"

## Conclusion

The study uses **68 cortical ROIs from Desikan-Killiany atlas** (analyzed with 3 measures each = 204 measures), plus **8 global measures** and **16 subcortical volume measures**, totaling **228 structural measures**. 

**Key Points:**
- **204 measures** come from Desikan-Killiany cortical parcellation (68 ROIs × 3 measures)
- **24 remaining measures** (228 - 204 = 24) come from FreeSurfer's aseg pipeline:
  - 8 global whole-brain measures
  - 16 subcortical structure volumes
- **All 228 measures are from FreeSurfer**, but only the 204 cortical measures use the Desikan-Killiany atlas
- The Desikan-Killiany atlas itself provides 68 ROIs, not 228 measures
