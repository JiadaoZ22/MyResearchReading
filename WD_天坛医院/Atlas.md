# Brain parcellation atlas(es) of FreeSurfer used in the paper

**Paper:** *Charting brain morphology in international healthy and neurological populations*  
**Folder:** `fZ_Reference/天坛医院/`

---

## Summary

The paper uses **two FreeSurfer-derived parcellation/segmentation schemes** to obtain **228 brain structural measures**:

| Component | Atlas / segmentation | FreeSurfer pipeline | Measures |
|-----------|----------------------|---------------------|----------|
| **Cortical** | Desikan–Killiany atlas | `aparc` (cortical parcellation) | 204 (68 ROIs × 3: volume, thickness, area) |
| **Subcortical + global** | FreeSurfer automatic subcortical segmentation | `aseg` | 24 (8 global + 16 subcortical volumes) |
| **Total** | — | — | **228** |

---

## 1. Desikan–Killiany atlas (cortical)

- **What it is:** A **cortical parcellation atlas** that divides the cerebral cortex into **34 regions per hemisphere (68 total)** based on gyral/sulcal anatomy.
- **In the paper:**  
  - *"Regional measures included cortical and subcortical volume, cortical thickness and surface area of regions determined according to the **Desikan–Killiany atlas**."*  
  - Supplement: *"Regional volume, cortical thickness and surface area were estimated for each of **34 cortical regions** defined by the **Desikan–Killiany parcellation atlas**."*
- **FreeSurfer implementation:**  
  - Cortical parcellation is produced by the `recon-all` pipeline and written to **`aparc`** (e.g. `aparc.stats`, `aparc+aseg.mgz` for the combined volume).
  - The Desikan–Killiany scheme is the **default cortical atlas** in FreeSurfer (`aparc` = DK parcellation).
- **Measures used:** For each of the 68 cortical regions, the paper uses **volume, cortical thickness, and surface area** → **204 cortical measures** (68 × 3).
- **Output files:** `lh.aparc.stats`, `rh.aparc.stats` (and related `aparc`/`aparc+aseg` volumes).

**Reference:** Desikan et al., *An automated labeling system for subdividing the human cerebral cortex on MRI scans into gyral based regions of interest.* (2006).

---

## 2. FreeSurfer aseg (subcortical and global)

- **What it is:** FreeSurfer’s **automatic subcortical segmentation** (often referred to as **aseg**). It is not a separate named “atlas” like Desikan–Killiany; it is the standard subcortical segmentation built into `recon-all`.
- **In the paper:**  
  - The **24 non‑cortical measures** (228 − 204) come from FreeSurfer’s pipeline: **8 global** (whole‑brain) and **16 subcortical** volume measures, all derived from the same FreeSurfer processing (reported as from **`aseg.stats`** in your project notes).
- **FreeSurfer implementation:**  
  - Subcortical structures and whole‑brain summaries are produced during `recon-all` and reported in **`aseg.stats`** (and the volume `aseg.mgz` / `aparc+aseg.mgz`).
- **Typical subcortical structures (aseg):**  
  - 8 per hemisphere (16 total): Thalamus, Caudate, Putamen, Pallidum, Hippocampus, Amygdala, Accumbens area, Ventral DC.  
  - Some FreeSurfer versions also include Basal Forebrain (e.g. 18 structures total). The paper does not list the exact set; the count (16–18) is inferred from standard aseg.
- **Global measures (from aseg / recon-all):**  
  - e.g. total cortical gray matter volume, total cerebral white matter volume, subcortical gray matter volume (sGMV), ventricular volume, cerebellar volume, brainstem volume, mean cortical thickness, total surface area (see `Study_ROI-measurement.md` for the list used in your 228-measure breakdown).

**So:** The paper does **not** use a second named “atlas” for subcortical ROIs; it uses **FreeSurfer’s default aseg (automatic subcortical segmentation)** plus the global measures produced by the same FreeSurfer pipeline.

---

## 3. Pipeline context

- The paper states that the **`recon-all` pipeline** is used, including motion correction, intensity normalization, skull stripping, tissue segmentation, surface reconstruction, and **parcellation**.
- **Cortical parcellation** → Desikan–Killiany atlas (`aparc`).
- **Subcortical and whole‑brain measures** → FreeSurfer aseg and related global stats (`aseg.stats`).

---

## 4. Quick reference

| FreeSurfer “atlas” / segmentation | Type | ROIs / structures | Paper measures |
|-----------------------------------|------|-------------------|-----------------|
| **Desikan–Killiany** (aparc)      | Cortical parcellation | 68 (34 per hemisphere) | 204 (volume, thickness, area per ROI) |
| **FreeSurfer aseg**               | Subcortical + whole‑brain | 8 global + 16 subcortical volumes | 24 |
| **Total**                         | —    | —                  | **228** |

For exact lists of the 8 global and 16 (or 18) subcortical structures, see **`Study_ROI-measurement.md`** in this folder.

---

## 5. Overlap between the two: answers to two common questions

### 5.1 Do the 8 global measures equal the sum of the 68 DK (cortical) ROIs?

**No.** The 8 global measures are **computed independently** by FreeSurfer, not by summing the 68 Desikan–Killiany regional values.

- **How they are produced:**  
  Global measures (e.g. total cortical gray matter volume, total surface area, mean cortical thickness) come from FreeSurfer’s **whole-brain / surface pipeline** and **`aseg.stats`**: they are derived from the same `recon-all` run but from **different steps** (e.g. surface-based integration, aseg masks) than the **parcellation** step that fills `aparc.stats` (DK).
- **Conceptual overlap:**  
  They describe the **same anatomical compartment** (e.g. “all cortical gray matter”). So total cortical GMV from the global stats and the **sum of the 68 DK cortical volumes** are **highly correlated and usually very close**, but they are **not** the same number in the pipeline: the global value is not defined as “sum of DK ROIs.”
- **Takeaway:**  
  **No overlap in definition**: the 8 global measures are **not** “made up of the sum of subROIs in the DK atlas”; they are computed **independently**. There is **conceptual overlap** (same tissue), so the two can be used together without double-counting only if you interpret globals as whole-brain/cortex summaries and DK as regional breakdown.

#### Empirical difference (FreeSurfer only: global vs sum of 68 DK)

For the **same** FreeSurfer subject, the **total cortical gray matter** can be read in two ways:

| Source | Measure | Description |
|--------|---------|-------------|
| **Global (aseg)** | `CortexVol` in `stats/aseg.stats` | Total cortical gray matter volume from the whole-brain/surface pipeline (surface-based integration). |
| **Sum of DK (aparc)** | Sum of `GrayVol` over 68 regions in `stats/lh.aparc.stats` + `stats/rh.aparc.stats` | Sum of Desikan–Killiany regional volumes (same units: mm³). |

On one subject (sub-2025073060_sess-1_run-2, FreeSurfer recon-all output under ParcEva):

| Quantity | Value (mm³) |
|----------|-------------|
| Global **CortexVol** (aseg.stats) | 396,517.75 |
| **Sum of 68 DK** GrayVol (aparc)  | 396,483.00 |
| **Difference** (sum_DK − global)   | **−34.75** (−0.009%) |
| **Ratio** (sum_DK / global)       | 0.999912 |

So in this run they are **extremely close** but **not identical**: the small gap (~35 mm³) is consistent with the two being computed by **different steps** (global from surface-based brain volume stats, DK from summing parcellation outputs), not by “global = sum of DK.” You can reproduce the comparison for any subject with:

```bash
python3 fZ_Reference/天坛医院/compare_global_vs_sum_DK.py <subject_dir>
```

(Subject dir must contain `stats/aseg.stats`, `stats/lh.aparc.stats`, `stats/rh.aparc.stats`.)

### 5.2 Are the 16 subcortical ROIs of aseg already in the Desikan–Killiany atlas?

**No.** The Desikan–Killiany atlas is **cortical only**. It does **not** include any of the 16 subcortical structures.

- **Desikan–Killiany (2006):**  
  It subdivides the **cerebral cortex** into 34 regions per hemisphere (68 total) based on gyral/sulcal anatomy. It explicitly does **not** parcellate subcortical nuclei (thalamus, caudate, putamen, pallidum, hippocampus, amygdala, accumbens, ventral DC, etc.).
- **The 16 subcortical ROIs:**  
  They come **only** from FreeSurfer’s **aseg** (automatic subcortical segmentation). They are **not** part of the DK atlas and are **not** defined by DK.
- **Takeaway:**  
  **No overlap**: the 16 subcortical ROIs from aseg and the 68 DK cortical ROIs are **disjoint**. DK = cortex; aseg subcortical = deep gray (and other non-cortical structures). So the 228 measures in the paper are **68 cortical (DK) + 8 global + 16 subcortical (aseg)**, with no double-counting between DK and subcortical ROIs.

---

## 6. Empirical gap between two atlases on the same ROIs (SynthSeg vs FreeSurfer)

To illustrate how **the same nominal ROIs** can differ when defined by **different pipelines** (same atlas, different segmentation), the following summary uses the **ParcEva** comparison of **SynthSeg+** vs **FreeSurfer** (aparc+aseg) on one subject.  
**Source:** `f2_Output/Brain/SynthSeg_v1.4.1/WD-MR_proj-AD/Test_20260210/ParcEva/Results` (single subject: sub-2025073060_sess-1_run-2).  
**Full report (double-checked):** `ParcEva/Results/Atlases_Comparison_Report.md`.

### 6.1 What ParcEva compares

- **Same ROIs:** **30** AD-related labels evaluated (8 subcortical + 22 cortical). The AD list has 32 labels; labels **865** and **866** (Basal Forebrain) are not output by SynthSeg, so only 30 are common to both pipelines.
- **Two pipelines, same atlas:** SynthSeg+ and FreeSurfer both use the **FreeSurfer label scheme** (DK cortex + aseg). Comparison is on the **same T1** (FS conformed `orig.mgz` → SynthSeg run on it; FS from recon-all).
- **Metrics:** Per-ROI Dice (spatial overlap), volume (voxel counts, 1 mm³), and ICV (total intracranial voxels).

### 6.2 Whole-brain (ICV) gap — analogous to “global vs sum of ROIs”

- **ICV SynthSeg:** 1,396,899 voxels  
- **ICV FreeSurfer:** 1,356,284 voxels  
- **Relative difference:** SynthSeg ≈ +3% vs FreeSurfer.

So even at the **whole-brain** level, the two pipelines give **different totals** (different segmentation boundaries and possibly inclusion of CSF/other classes). That is consistent with **Q1**: global measures from one pipeline are **not** simply the sum of another pipeline’s ROIs; each pipeline computes its own totals.

### 6.3 Spatial overlap (Dice) by region type

From ParcEva `per_label_summary.csv` (1 subject, 30 ROIs):

| Region type   | ROIs (examples)                    | Dice range (this subject) | Comment |
|---------------|------------------------------------|---------------------------|---------|
| **Subcortical** | 17,18,26,28,53,54,58,60 (Hipp, Amyg, Accumbens, VentralDC) | **0.83–0.89** | Good agreement on boundaries. |
| **Cortical**    | 1006, 1007, … 2033 (entorhinal, temporal, parietal, etc.) | **0.51–0.77** | Lower overlap; boundary definitions differ. |

Overall mean Dice (30 ROIs): **0.73**. So for the **same anatomical ROIs**, the two pipelines agree more on **subcortical** than on **cortical** borders.

### 6.4 Volume differences (same ROIs, two atlases)

- **Subcortical:** Mixed. Some ROIs larger in SynthSeg (e.g. Amygdala L: 1784 vs 1407), others larger in FreeSurfer (e.g. Hippocampus R: 4294 vs 4918). No single direction.
- **Cortical:** SynthSeg volumes are **systematically larger** than FreeSurfer for most cortical ROIs in this subject, e.g.:
  - Entorhinal L (1006): 2807 vs 1422 (SS ≈ 2× FS)
  - Fusiform L (1007): 11994 vs 7124 (SS ≈ 1.7× FS)
  - Superior temporal L (1030): 11521 vs 9246 (SS ≈ 1.2× FS)

So the **gap** between the two atlases for the same ROIs is not only in **total brain (ICV)** but in **per-ROI volumes**: different boundary definitions and possibly different handling of cortex/CSF yield different regional volumes even when the ROI names match.

### 6.5 Takeaway for Q1 (8 global vs sum of DK)

- ParcEva does **not** contain the “8 global” or “sum of 68 DK” from FreeSurfer alone; it compares **SynthSeg vs FreeSurfer** per ROI and at whole-brain (ICV).
- It **does** show that:
  1. **Two pipelines (two “atlases”) on the same scan** give different **whole-brain** totals (ICV gap ~3%).
  2. **Same nominal ROIs** can have **different volumes** and **different spatial overlap** depending on the pipeline.

So the **general principle** behind Q1 holds: **global measures are not defined as “sum of parcellation ROIs”**; they are computed by their own pipeline steps. ParcEva illustrates that even with the **same** atlas (DK + aseg), two pipelines (SS vs FS) yield different volumes and overlap because each method draws boundaries differently. **Detailed, double-checked numbers:** see `ParcEva/Results/Atlases_Comparison_Report.md` in the same output tree.
