# ROI & Feature List (Source Code Verified for Tian Tan Brain Chart Pipeline)
Last updated: 2026-05-09 | Verified against Charting-Chinese-repo source code v1.0

---

## Overview
This document lists **all ROIs and their corresponding features** used in the paper *"Charting brain morphology in international healthy and neurological populations"* (Zhuo et al., Nat Neurosci 2026). All entries are 100% verified against:
- GAMLSS-DK normative model files (`/Models/GAMLSS/DK/`)
- `MR_measures.xlsx` input structure for R pipeline
- R code (`Disease-application-normative-model.R`)
- Official FreeSurfer 7.3.2 Desikan-Killiany (DK) atlas label definitions

**Total measures = 228**: 8 global + 16 subcortical regional + 204 cortical regional.
**All measures are from FreeSurfer 7.3.2** (primary), FS 6.0.1 used only for cross-version comparison.

---

## 1. Global Measures (8 paper used + 1 auxiliary TCV)
Global measures are whole-brain summaries from `aseg.stats`/`aparc.stats` (not ROI-specific). No area/thickness features for global measures (only volume/summary metrics).

| Global Measure Name | Source | Definition | Included in paper's 228? |
|---------------------|--------|------------|--------------------------|
| GMV (Total cortical gray matter volume) | `aseg.stats` | Whole-brain cortical gray matter volume | ✅ Yes |
| sGMV (Subcortical gray matter volume) | `aseg.stats` | Sum of 7 bilateral subcortical structures: Thalamus, Caudate, Putamen, Pallidum, Hippocampus, Amygdala, Accumbens **(excludes VentralDC per paper Supplement Methods)** | ✅ Yes |
| WMV (Total cerebral white matter volume) | `aseg.stats` | Whole-brain cerebral white matter volume | ✅ Yes |
| CSF/Ventricles | Derived from `aseg.stats` | `BrainSegVol` − `BrainSegVolNotVent` = total ventricular volume | ✅ Yes |
| Cerebellum | Derived from `aseg.stats` | Sum of `Left.Cerebellum.White.Matter` + `Right.Cerebellum.White.Matter` + `Left.Cerebellum.Cortex` + `Right.Cerebellum.Cortex` | ✅ Yes |
| Brain.Stem | `aseg.stats` | Total brain-stem volume | ✅ Yes |
| Mean cortical thickness | Derived from `lh/rh.aparc.stats` | Vertex-weighted average: `(lhMeanThickness × lhVertex + rhMeanThickness × rhVertex) / (lhVertex + rhVertex)` | ✅ Yes |
| Total surface area | Derived from `lh/rh.aparc.stats` | Sum of `lh_totaISA2` + `rh_totaISA2` | ✅ Yes |
| TCV/Estimated Total Intracranial Volume | `aseg.stats` | Auxiliary measure used as covariate, not counted in paper's 228 | ❌ No |

---

## 2. Subcortical Regional Measures (16 total)
Subcortical measures are **volume-only** (no area/thickness features) from `aseg.stats`. All 16 are regional individual volumes, counted in paper's 228.

Important nuance: The **global sGMV scalar sum excludes VentralDC**, but VentralDC IS included as a separate regional measure.

| Structure Name | Left Hemisphere FS Label ID | Right Hemisphere FS Label ID | Feature | Included in paper's 228? |
|----------------|------------------------------|-------------------------------|---------|--------------------------|
| Thalamus | 10 | 49 | Volume | ✅ Yes |
| Caudate | 11 | 50 | Volume | ✅ Yes |
| Putamen | 12 | 51 | Volume | ✅ Yes |
| Pallidum | 13 | 52 | Volume | ✅ Yes |
| Hippocampus | 17 | 53 | Volume | ✅ Yes |
| Amygdala | 18 | 54 | Volume | ✅ Yes |
| Accumbens Area | 26 | 58 | Volume | ✅ Yes |
| Ventral DC | 28 | 60 | Volume | ✅ Yes (regional only; excluded from global sGMV sum) |

Total subcortical regional measures: 8 structures × 2 hemispheres = 16.

---

## 3. Cortical Regional Measures (204 total)
Cortical measures use the **FreeSurfer Desikan-Killiany (DK) atlas** (default `aparc` parcellation: 34 ROIs per hemisphere = 68 total ROIs). Each ROI has **3 features per hemisphere**: volume, area, cortical thickness.

Total cortical measures: 68 ROIs × 3 features = 204 (exactly matches paper count). All are included in paper's 228.

### Left Hemisphere (34 ROIs, 3 features each = 102 measures)
| ROI Name | Volume Feature Name | Area Feature Name | Thickness Feature Name |
|----------|---------------------|-------------------|------------------------|
| bankssts | lh_bankssts_volume | lh_bankssts_area | lh_bankssts_thickness |
| caudalanteriorcingulate | lh_caudalanteriorcingulate_volume | lh_caudalanteriorcingulate_area | lh_caudalanteriorcingulate_thickness |
| caudalmiddlefrontal | lh_caudalmiddlefrontal_volume | lh_caudalmiddlefrontal_area | lh_caudalmiddlefrontal_thickness |
| cuneus | lh_cuneus_volume | lh_cuneus_area | lh_cuneus_thickness |
| entorhinal | lh_entorhinal_volume | lh_entorhinal_area | lh_entorhinal_thickness |
| fusiform | lh_fusiform_volume | lh_fusiform_area | lh_fusiform_thickness |
| inferiorparietal | lh_inferiorparietal_volume | lh_inferiorparietal_area | lh_inferiorparietal_thickness |
| inferiortemporal | lh_inferiortemporal_volume | lh_inferiortemporal_area | lh_inferiortemporal_thickness |
| isthmuscingulate | lh_isthmuscingulate_volume | lh_isthmuscingulate_area | lh_isthmuscingulate_thickness |
| lateraloccipital | lh_lateraloccipital_volume | lh_lateraloccipital_area | lh_lateraloccipital_thickness |
| lateralorbitofrontal | lh_lateralorbitofrontal_volume | lh_lateralorbitofrontal_area | lh_lateralorbitofrontal_thickness |
| lingual | lh_lingual_volume | lh_lingual_area | lh_lingual_thickness |
| medialorbitofrontal | lh_medialorbitofrontal_volume | lh_medialorbitofrontal_area | lh_medialorbitofrontal_thickness |
| middletemporal | lh_middletemporal_volume | lh_middletemporal_area | lh_middletemporal_thickness |
| parahippocampal | lh_parahippocampal_volume | lh_parahippocampal_area | lh_parahippocampal_thickness |
| paracentral | lh_paracentral_volume | lh_paracentral_area | lh_paracentral_thickness |
| parsopercularis | lh_parsopercularis_volume | lh_parsopercularis_area | lh_parsopercularis_thickness |
| parsorbitalis | lh_parsorbitalis_volume | lh_parsorbitalis_area | lh_parsorbitalis_thickness |
| parstriangularis | lh_parstriangularis_volume | lh_parstriangularis_area | lh_parstriangularis_thickness |
| pericalcarine | lh_pericalcarine_volume | lh_pericalcarine_area | lh_pericalcarine_thickness |
| postcentral | lh_postcentral_volume | lh_postcentral_area | lh_postcentral_thickness |
| posteriorcingulate | lh_posteriorcingulate_volume | lh_posteriorcingulate_area | lh_posteriorcingulate_thickness |
| precentral | lh_precentral_volume | lh_precentral_area | lh_precentral_thickness |
| precuneus | lh_precuneus_volume | lh_precuneus_area | lh_precuneus_thickness |
| rostralanteriorcingulate | lh_rostralanteriorcingulate_volume | lh_rostralanteriorcingulate_area | lh_rostralanteriorcingulate_thickness |
| rostralmiddlefrontal | lh_rostralmiddlefrontal_volume | lh_rostralmiddlefrontal_area | lh_rostralmiddlefrontal_thickness |
| superiorfrontal | lh_superiorfrontal_volume | lh_superiorfrontal_area | lh_superiorfrontal_thickness |
| superiorparietal | lh_superiorparietal_volume | lh_superiorparietal_area | lh_superiorparietal_thickness |
| superiortemporal | lh_superiortemporal_volume | lh_superiortemporal_area | lh_superiortemporal_thickness |
| supramarginal | lh_supramarginal_volume | lh_supramarginal_area | lh_supramarginal_thickness |
| frontalpole | lh_frontalpole_volume | lh_frontalpole_area | lh_frontalpole_thickness |
| temporalpole | lh_temporalpole_volume | lh_temporalpole_area | lh_temporalpole_thickness |
| transversetemporal | lh_transversetemporal_volume | lh_transversetemporal_area | lh_transversetemporal_thickness |
| insula | lh_insula_volume | lh_insula_area | lh_insula_thickness |

### Right Hemisphere (34 ROIs, 3 features each = 102 measures)
Replace `lh_` prefix with `rh_` for all right hemisphere feature names. ROIs are identical to left hemisphere.

Examples:
- Right bankssts: `rh_bankssts_volume`, `rh_bankssts_area`, `rh_bankssts_thickness`
- Right insula: `rh_insula_volume`, `rh_insula_area`, `rh_insula_thickness`

---

## Verification Sources
1. **GAMLSS-DK model directory**: `/Models/GAMLSS/DK/`
   - `Global_feature/`: 9 .rds files (8 paper global + TCV)
   - `aseg.vol.table/`: 18 .rds files (16 subcortical + Brain.Stem + cerebellum_total)
   - `lh/rh.aparc.{volume,area,thickness}.table/`: 34 .rds files each (34 ROIs per hemisphere per metric)
2. **Input data**: `/Datasets/Dataset-norms/MR_measures.xlsx` and `/Datasets/Dataset-diseases/MR_measures.xlsx`
3. **R code**: `/Scripts/Disease-application-normative-model.R` line 51 (aseg column selection) and line 37 (aparc column selection)
4. **FreeSurfer documentation**: Desikan-Killiany atlas label definitions, FS 7.3.2
