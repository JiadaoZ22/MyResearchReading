# Common and Excluding ROIs: FreeSurfer vs SynthSeg (ParcEva)

**References:**  
- `fZ_Reference/BrainParcellation/SynthSeg/Atlas_SynthSeg.md`  
- `fZ_Reference/天坛医院/Atlas.md`

**Data source:** ParcEva comparison under  
`/media/zoujd4/Lenovo-8T/Zoujd_IMI/f2_Output/Brain/SynthSeg_v1.4.1/WD-MR_proj-AD/Test_20260210/ParcEva`  
(FS: `aparc+aseg.mgz`; SS: `*_synthseg.nii.gz` with `--parc`; subject: sub-2025073060_sess-1_run-2).

---

## Atlas agreement (same scheme)

Both **FreeSurfer** and **SynthSeg** use the **same label scheme**:

- **Cortical parcellation:** Desikan–Killiany (DK) atlas as in FreeSurfer `aparc` (68 regions, 34 per hemisphere).
- **Segmentation (non-cortical):** FreeSurfer **aseg** label IDs and anatomical definitions.

So there is **no second, different atlas**: same label IDs and same anatomical definitions. Any “common” ROI is from this single scheme; “excluding” ROIs are due to **pipeline coverage** (which structures each method outputs), not different atlas definitions.

---

## 1. Common ROIs from the same atlas

**98 labels** appear in **both** FS `aparc+aseg.mgz` and SS parcellation NIfTI. They are **common ROIs from the same atlas** (FreeSurfer DK + aseg): same IDs, same definitions.

| Subset | Count | Label IDs | Description |
|--------|-------|-----------|-------------|
| **Cortical (DK)** | 68 | 1001–1035 (L), 2001–2035 (R) | Desikan–Killiany; same as FreeSurfer `aparc` |
| **Subcortical (aseg)** | 16 | 10, 11, 12, 13, 17, 18, 26, 28 (L); 49, 50, 51, 52, 53, 54, 58, 60 (R) | Thalamus, caudate, putamen, pallidum, hippocampus, amygdala, accumbens, ventral DC (8×2) |
| **Other aseg** | 14 | 2, 4, 5, 7, 8, 14, 15, 16, 24, 41, 43, 44, 46, 47 | WM (2, 41), ventricles (4, 5, 14, 15), cerebellum (7, 8, 46, 47), brainstem (16), CSF (24) |
| **Total** | **98** | — | All compared in ParcEva Results_WholeBrain |

These 98 are the only labels used for Dice and volume comparison in ParcEva (whole-brain run). Per-label metrics are in `Results_WholeBrain/per_label_summary.csv` and `all_metrics.csv`.

---

## 2. Common ROIs with same definition but from different atlases

**None.**  
Both pipelines use the **same atlas** (FreeSurfer DK + aseg). There are no ROIs that are “same definition, different atlas” in this comparison.

---

## 3. Excluding ROIs (different definition or pipeline coverage)

### 3.1 In FreeSurfer only (6 labels)

SynthSeg does **not** output these; they are **excluded from the ParcEva comparison** (not in the 98 common).

| Label | Structure |
|-------|-----------|
| 77 | WM-hypointensities |
| 251 | CC_Posterior (corpus callosum) |
| 252 | CC_Mid_Posterior |
| 253 | CC_Central |
| 254 | CC_Mid_Anterior |
| 255 | CC_Anterior |

**Reason:** Different pipeline coverage — these aseg-derived structures are produced by FreeSurfer but are not part of SynthSeg’s segmentation/parcellation output.

### 3.2 In SynthSeg volume table only, not in parcellation NIfTI (2 labels)

These use the **same** FreeSurfer aseg definitions (whole-hemisphere cortex) but do **not** appear in the **parcellation NIfTI** when using `--parc`, because cortical voxels are labeled with the 68 DK regions (1001–2035), not as 3 or 42.

| Label | Structure |
|-------|-----------|
| 3 | Left cerebral cortex |
| 42 | Right cerebral cortex |

They can appear in SynthSeg’s **volume table** (e.g. with `--vol`) from the segmentation branch, but they are **excluded from the NIfTI-based ParcEva comparison** because they are not present in the saved parcellation volume.

---

## Summary table

| Category | Count | Description |
|----------|-------|-------------|
| **1. Common, same atlas** | 98 | In both FS and SS volumes; same FreeSurfer DK + aseg definitions; used for Dice/volume comparison |
| **2. Same definition, different atlases** | 0 | Not applicable (single atlas used by both) |
| **3a. Excluding — FS only** | 6 | 77, 251–255; FS outputs them, SS does not |
| **3b. Excluding — SS table only** | 2 | 3, 42; in SS volume table but not in parcellation NIfTI (cortex represented as DK only) |

---

## File references

- **ParcEva Results_WholeBrain:** `Results_WholeBrain/README.md`, `per_label_summary.csv`, `all_metrics.csv`
- **Atlas docs:** `fZ_Reference/BrainParcellation/SynthSeg/Atlas_SynthSeg.md`, `fZ_Reference/天坛医院/Atlas.md`
