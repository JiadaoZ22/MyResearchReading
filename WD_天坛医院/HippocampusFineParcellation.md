# FreeSurfer Hippocampus Fine Parcellation (Subfield Segmentation)

**Folder:** `fZ_Reference/WD_天坛医院/`

This note summarizes **whether and how FreeSurfer can further fine parcellate the hippocampus** beyond the single left/right hippocampus labels in the standard `aseg` output.

---

## 1. Short Answer

**Yes.** FreeSurfer provides **hippocampal subfield** segmentation as a **separate step** after `recon-all`. Standard `recon-all` only outputs **whole hippocampus** (left/right) in `aseg`; it does **not** subdivide the hippocampus into subfields. To get fine parcellation (e.g. CA1, CA2/3, CA4, dentate gyrus, subiculum, head/body/tail), you must run an additional module.

---

## 2. Standard recon-all vs Hippocampal Subfields

| Item | Standard `recon-all` | Hippocampal subfield module |
|------|----------------------|-----------------------------|
| **Hippocampus in aseg** | One label per hemisphere (Left 17, Right 53) | N/A (subfields are not in aseg) |
| **Fine parcellation** | **No** | **Yes** — subfields + optional head/body/tail |
| **When to run** | Always (base pipeline) | **After** recon-all, as a separate command |

So: **recon-all does not fine parcellate the hippocampus**; you add a dedicated subfield segmentation step on top of it.

### 2.1 Paper says “T1 and T2” — but recon-all is T1-only. What happens?

The Iglesias et al. 2015 paper describes a method that **can use both T1 and T2** (e.g. for better subfield boundaries). In FreeSurfer this is implemented as follows; there is **no contradiction**:

- **recon-all is T1-only.** The main FreeSurfer pipeline ([recon-all](https://surfer.nmr.mgh.harvard.edu/fswiki/ReconAll)) requires a **T1-weighted** structural scan. It does **not** run on T2. So you always need a T1 and must run recon-all on it first.
- **The hippocampal subfield module** (Iglesias et al. method) then runs **after** recon-all. It can operate in two ways:
  1. **T1 only:** Uses the T1-derived files from recon-all (`norm.mgz`, `aseg.mgz`, etc.). This is what [SubregionSegmentation](https://surfer.nmr.mgh.harvard.edu/fswiki/SubregionSegmentation) (Python, FS 7.3+) and `segmentHA_T1.sh` (Matlab) do. So “T1 and T2” in the paper does **not** mean “recon-all runs on T2”; it means the **subfield step** can optionally use an extra image.
  2. **T1 + additional T2 (or other contrast):** The [HippocampalSubfieldsAndNucleiOfAmygdala](https://surfer.nmr.mgh.harvard.edu/fswiki/HippocampalSubfieldsAndNucleiOfAmygdala) wiki documents **`segmentHA_T2.sh`** (Matlab only): you provide an **additional** volume (e.g. high-resolution T2) that is **registered to the T1**. The subfield algorithm then uses both the T1 (from recon-all) and this extra scan for segmentation. So the paper’s “T1 and T2” = **recon-all on T1 first**, then the **hippocampal module** can optionally take an **additional T2** as a second input. T2 is **not** a replacement for recon-all.
- **SubregionSegmentation** (Python, FS 7.3+) currently **does not** use that extra T2; the [SubregionSegmentation](https://surfer.nmr.mgh.harvard.edu/fswiki/SubregionSegmentation) wiki states: *“the current version cannot take advantage of images other than T1 scans. If you want to use eg higher resolution T2 scans for hippocampal subfield segmentation, please use the Matlab code.”*

**Summary:** Recon-all is T1-only. The paper’s “T1 and T2” means the **hippocampal subfield step** can optionally use an **additional T2** (via Matlab `segmentHA_T2.sh`); it does **not** mean recon-all runs on T2.

---

## 3. Available Modules (by FreeSurfer Version)

### 3.1 Deprecated: `-hippo-subfields` (FreeSurfer 5.2–5.3 only)

- **Command:** `recon-all -s <subject> -all -hippo-subfields` (or `-hippo-subfields` only after recon-all).
- **Status:** **Deprecated.** Documented on [HippocampalSubfieldSegmentation](https://surfer.nmr.mgh.harvard.edu/fswiki/HippocampalSubfieldSegmentation); replaced by the tools below.

### 3.2 Current: Hippocampus + amygdala (FreeSurfer 6 / 7, Matlab-based)

- **Wiki:** [HippocampalSubfieldsAndNucleiOfAmygdala](https://surfer.nmr.mgh.harvard.edu/fswiki/HippocampalSubfieldsAndNucleiOfAmygdala)
- **Requirements:** recon-all already run; **Matlab Runtime** (R2012b for FS6, R2014b for FS7) — no license needed.
- **Modes:**
  - **T1 only:** `segmentHA_T1.sh <subject> [SUBJECTS_DIR]`
  - **T1 + additional scan (e.g. T2):** `segmentHA_T2.sh <subject> FILE_ADDITIONAL_SCAN ANALYSIS_ID USE_T1 [SUBJECTS_DIR]` — better for subfields when a higher-resolution T2 is available.
  - **Longitudinal:** `segmentHA_T1_long.sh <baseID> [SUBJECTS_DIR]`
- **Output (examples for T1):**
  - **Volumes:** `lh.hippoSfVolumes-T1.v21.txt`, `rh.hippoSfVolumes-T1.v21.txt` (hippocampal subfields); `lh.amygNucVolumes-T1.v21.txt`, `rh.amygNucVolumes-T1.v21.txt` (amygdala nuclei).
  - **Labels:** `lh/rh.hippoAmygLabels-T1.v21.mgz` (and `.FSvoxelSpace.mgz`, plus hierarchy variants `.HBT.mgz`, `.FS60.mgz`, `.CA.mgz`).
  - **Stats:** `hipposubfields.lh.T1.v21.stats`, `hipposubfields.rh.T1.v21.stats` (and amygdala); can be tabulated with `asegstats2table`.

### 3.3 Unified Python interface (FreeSurfer 7.3+)

- **Wiki:** [SubregionSegmentation](https://surfer.nmr.mgh.harvard.edu/fswiki/SubregionSegmentation)
- **Command:** `segment_subregions hippo-amygdala --cross <subject>` (cross-sectional) or `segment_subregions hippo-amygdala --long-base <base>` (longitudinal).
- **Advantages:** No Matlab runtime; single command for hippo-amygdala (and optionally thalamus, brainstem); results very close to the Matlab-based tools.
- **Limitation:** **T1 only** — if you need a high-resolution T2 for hippocampus, use the Matlab-based `segmentHA_T2.sh`.
- **Output:** Similar to above (e.g. `lh.hippoSfVolumes.txt`, `lh.hippoAmygLabels.mgz`, stats in `stats/`). Exact filenames may use a different suffix (see wiki).

---

## 4. What Subfields Are Produced?

The hippocampus is subdivided into **subfields** and optionally **head / body / tail**. The exact list depends on the hierarchy level:

- **Full detail:** Subfields from an ex vivo atlas (~0.1 mm), including CA1, CA2, CA3, CA4, dentate gyrus (DG), subiculum, molecular layer, fimbria, etc., with head/body split where applicable.
- **Hierarchy levels** (Matlab-based module):
  - **HBT:** Head, body, tail (no head/body subdivision within subfields).
  - **FS60:** Mimics FreeSurfer 6.0 hippocampal output (no head/body subdivision).
  - **CA:** CA subfields with molecular layer / GC-ML-DG merged into nearest neighbor (CA2 is always merged into CA3 in these summaries).

**Note:** CA2 is always included in CA3 in the merged (CA / FS60) volumes. For full subfield definitions and label tables, see the [HippocampalSubfieldsAndNucleiOfAmygdala](https://surfer.nmr.mgh.harvard.edu/fswiki/HippocampalSubfieldsAndNucleiOfAmygdala) wiki.

**What are HBT and FS60 — atlases or something else?**

They are **not atlases** in the usual sense (a reference image + labels in a standard space). The **atlas** used for segmentation is the **ex vivo probabilistic atlas** (Iglesias et al., 2015, ~0.1 mm). **HBT** and **FS60** are **label hierarchies** (parcellation schemes): different ways of **grouping** the same underlying segmentation labels into output volumes. So: one segmentation run → one atlas-based result → multiple **hierarchy** outputs (full, HBT, FS60, CA). When we say “follow HBT or FS60,” we mean use the same **label set / hierarchy** as FreeSurfer’s HBT or FS60 output, not a different reference atlas.

**Your understanding: get ROIs first, then apply HBT/FS60 for standardized output**

**Yes.** HBT and FS60 are **label hierarchies** (standardized output schemes), **not** the segmentation algorithm. So: (1) Some **algorithm** produces hippocampus subfield ROIs; (2) you **map** that result to HBT or FS60 for standardized output (e.g. 天坛 norms). In FreeSurfer, the same module does both: one algorithm produces the segmentation and the software outputs it as full, HBT, FS60, CA. So conceptually: algorithm → ROIs → HBT/FS60 view.

**Which algorithm does FreeSurfer use for hippocampus fine parcellation?**

One **segmentation algorithm**; HBT/FS60 are **derived** from its output by **label merging**. The algorithm:

| Component | What FreeSurfer uses |
|-----------|----------------------|
| **Atlas** | **Ex vivo probabilistic atlas** (Iglesias et al., *Neuroimage* 115, 2015): ~0.1 mm ex vivo MRI, manual subfield labels. |
| **Method** | **Bayesian / probabilistic segmentation**: atlas **deformed** to subject (T1 ± T2 from recon-all); voxel-wise **posterior** over subfield labels → **detailed** segmentation (CA1, CA2, CA3, CA4, DG, subiculum, molecular layer, fimbria, head/body/tail, etc.). |
| **Output** | That segmentation is **merged/relabeled** into full, **HBT**, **FS60**, **CA**. So HBT/FS60 are **post-hoc label schemes** on the same result. |

**13 (paper) vs 19 (HBT L2) substructures:** The Iglesias et al. 2015 paper states that the ex vivo images were **manually segmented into 13 hippocampal substructures** to build the atlas (see e.g. [PubMed 25936807](https://pubmed.ncbi.nlm.nih.gov/25936807/)). FreeSurfer’s [HippocampalSubfieldsAndNucleiOfAmygdala](https://surfer.nmr.mgh.harvard.edu/fswiki/HippocampalSubfieldsAndNucleiOfAmygdala) and [SubregionSegmentation](https://surfer.nmr.mgh.harvard.edu/fswiki/SubregionSegmentation) wikis state that the same tool **subdivides the hippocampal substructures into head and body, where applicable**. So the **13** are the **anatomical subfield types** in the manual protocol (e.g. parasubiculum, presubiculum, subiculum, CA1, CA3, CA4, GC-ML-DG, molecular layer, HATA, fimbria, tail, fissure, etc.). The **HBT** hierarchy then **splits** many of these along the long axis into **head** and **body**, yielding **19 Level-2 (L2) labels**: 9 in HEAD, 8 in BODY, 1 in TAIL, 1 in FISSURE (e.g. subiculum → subiculum-head + subiculum-body; CA1 → CA1-head + CA1-body). So the paper’s atlas and FreeSurfer’s output are **the same protocol**; 13 is the number of manual substructure types, 19 is the number of HBT L2 labels after head/body/tail subdivision. Both the paper and FreeSurfer produce **HBT-compatible** results.

So: **recon-all** supplies T1 (± T2); the **hippocampus/amygdala module** runs this **atlas-based Bayesian segmentation** and writes HBT, FS60, etc. If recon-all is inevitable, improving "HBT" means (1) improving or replacing **that Bayesian step** (e.g. faster implementation or DL mimicking it) while still outputting HBT/FS60, or (2) using another ROI producer (e.g. DL) and **mapping** its labels to HBT/FS60.

**Can we use another atlas (e.g. DK) for hippocampus fine parcellation and relabel to HBT or FS60?**

- **DK (Desikan–Killiany):** **No.** DK is a **cortical** parcellation atlas (34 regions per hemisphere). It does **not** subdivide the hippocampus; in FreeSurfer, hippocampus is in **aseg** as whole left/right only (labels 17, 53). So there are no DK "hippocampus subfield" labels to relabel to HBT/FS60.
- **Another hippocampus subfield method** (e.g. HSF, ASHS, HippUnfold): In principle you could **map** that method's labels to HBT or FS60 **if** the structures are comparable. Caveats: (1) Different protocols use different boundaries (e.g. Berron vs Iglesias), so relabeling is often **approximate**, not a true 1:1. (2) **HBT** requires head/body/tail; many methods don't define that axis, so you'd need a rule (e.g. anterior/middle/posterior thirds) that may not match FreeSurfer's HBT. (3) **FS60** has specific subfield definitions (CA1, CA2/3, CA4, DG, subiculum, etc.); other atlases may merge or split differently, so a lookup table can only be approximate. For **strict** HBT or FS60 compatibility (e.g. 天坛 norms), native FreeSurfer output remains the reference; relabeling from other methods is possible but should be validated and documented.

**Using HBT (or FS60) when your algorithm uses a different hippocampus atlas: what to pay attention to**

Different algorithms use different **definitions and ROIs** for the same part of the brain (e.g. different CA1/CA2/CA3 boundaries, different head/body/tail rules, or different merging of DG/CA4). If you want to **map** such results to HBT for standardized output, pay attention to:

| What to check | Why it matters |
|---------------|----------------|
| **Label correspondence** | Your atlas may not have a 1:1 match to HBT. E.g. you may have "CA2" and "CA3" separate while HBT/FS60 often use "CA2/3" merged; or you may have no "head/body/tail" at all. Define an **explicit mapping table**: which of your labels → which HBT (or FS60) label. Document **missing** or **merged** structures (e.g. "our CA2+CA3 → HBT CA2/3"). |
| **Head/body/tail (HBT only)** | Many atlases do **not** define head/body/tail. To get HBT, you must introduce a rule (e.g. anterior / middle / posterior thirds by slice or along the long axis). That rule will **not** match FreeSurfer’s HBT definition exactly (FS uses atlas-based boundaries). So volumes labeled "head/body/tail" after mapping are **HBT-like** but not native HBT — document the rule and, if possible, validate against FS on a subset. |
| **Boundary and volume comparability** | Even when names match (e.g. "CA1"), **boundaries** differ between protocols (Iglesias vs Berron vs Winterburn, etc.). So after relabeling you have **HBT-compatible label names**, but **volumes may not be comparable** to native FreeSurfer HBT (e.g. for 天坛 norms). If you feed mapped volumes into norms or compare to FS-based studies, state that they are **"HBT-mapped from [your method]"** and consider validation or calibration. |
| **Validation** | On a subset of subjects, run **both** your algorithm (then map to HBT) and FreeSurfer HBT; compare volumes or Dice per region. That shows how much the mapping deviates from native HBT and helps interpret downstream results. |
| **Reporting** | In methods and tables, report **source atlas/method** and that HBT (or FS60) was obtained by **mapping**, not by FreeSurfer. E.g. "Hippocampus subfields were segmented with [X] and mapped to FreeSurfer HBT hierarchy for compatibility with 天坛 norms." |

**Summary:** Mapping a different atlas to HBT is possible and useful for standardization, but the result is **HBT-compatible labeling**, not **native HBT**. Pay attention to label correspondence, head/body/tail rules if needed, volume comparability with native FS, and clear reporting and (when feasible) validation.

### 4.1 Comparing HBT vs FS60 (performance, speed, hardware)

**HBT** and **FS60** are **not different models** — they are **two label hierarchies** produced by the **same** FreeSurfer hippocampus/amygdala run (`segmentHA_T1.sh`, `segmentHA_T2.sh`, or `segment_subregions hippo-amygdala`). The pipeline runs once and writes multiple outputs (full labels, HBT, FS60, CA). So:

| Aspect | HBT | FS60 | Note |
|--------|-----|------|------|
| **Performance (accuracy)** | Same | Same | Same algorithm and same underlying segmentation; only the way labels are merged differs. No extra accuracy cost or gain for choosing one over the other. |
| **Speed** | Same | Same | Both are generated in the same run. No additional runtime for HBT vs FS60. |
| **Hardware** | Same | Same | Same RAM, CPU, and (if used) GPU requirements. |

**Difference is output granularity and use case:**

| | HBT | FS60 |
|--|-----|------|
| **Definition** | Hippocampus subdivided into **head, body, tail** (Iglesias et al., 2015). Subfields can be reported within each (head/body/tail). | Mimics **FreeSurfer 6.0** hippocampal module: subfields **without** head/body/tail subdivision. |
| **Output** | Labels for head, body, tail (and subfields within them, depending on atlas). | Subfield-only labels (e.g. CA1, CA2/3, CA4, DG, subiculum, etc.) with no head/body/tail split. |
| **When to use** | When you need **along-axis** measures (e.g. head vs body vs tail volume or thickness). | When you want **FS 6.0–compatible** subfield volumes or comparison with older FS 6.0 studies; or when head/body/tail is not needed. |

**Which is preferred / more modern?**

- **More modern (anatomically):** **HBT** — it uses the newer scheme that subdivides the hippocampus into **head, body, tail**, giving along-axis structure. Use HBT when you want this extra axis or when starting new analyses.
- **Preferred for compatibility:** **FS60** — it mimics **FreeSurfer 6.0** output (subfields only, no head/body/tail), so it is preferred when you need to match older FS 6.0 studies, use published FS 6.0 norms, or only need subfield volumes without head/body/tail.

**Summary:** For **performance, speed, and hardware**, HBT and FS60 are identical because they come from the same run. Choose **HBT** if you need head/body/tail or want the more modern parcellation; choose **FS60** for subfield-only, FS 6.0–compatible output.

### 4.2 Latest FreeSurfer tool (more modern than the Matlab-based pipeline)

The **most modern** FreeSurfer option for hippocampal subfields is **`segment_subregions hippo-amygdala`** (FreeSurfer **7.3+**), not a different hierarchy than HBT/FS60 but a **newer implementation** that replaces the older Matlab-based scripts.

| | Older (Matlab-based) | Latest (Python, FS 7.3+) |
|--|----------------------|---------------------------|
| **Tool** | `segmentHA_T1.sh`, `segmentHA_T2.sh`, `segmentHA_T1_long.sh` | **`segment_subregions hippo-amygdala --cross <subject>`** (or `--long-base` for longitudinal) |
| **Runtime** | Matlab Runtime (R2012b/R2014b) required | **No Matlab** — pure Python |
| **Output** | Same hierarchy levels: full, HBT, FS60, CA | Same; results "very close but not identical" to Matlab (per [SubregionSegmentation](https://surfer.nmr.mgh.harvard.edu/fswiki/SubregionSegmentation) wiki) |
| **T2 / high-res** | **Yes** — `segmentHA_T2.sh` can use an additional T2 volume | **No** — T1 only; for T2 you must still use the Matlab `segmentHA_T2.sh` |
| **Availability** | FreeSurfer 6, 7.x | FreeSurfer **7.3+** |

So: **HBT and FS60** are just two of the **output label schemes**; they are produced by both the old and the new tool. The **latest, more modern FreeSurfer tool** is **`segment_subregions hippo-amygdala`** — use it for T1-only workflows to avoid Matlab and get a single Python interface for hippo-amygdala (and optionally thalamus, brainstem). For workflows that need **T2 or an extra high-resolution scan**, the Matlab-based **`segmentHA_T2.sh`** remains the only FreeSurfer option.

---

## 5. How to Run HBT: Input, Command, Output, Runtime

You do **not** run "HBT" as a separate program. You run the hippocampus/amygdala module **once**; it produces HBT (and FS60, CA, full labels) together. To get **HBT output**:

**Input requirements**

| Requirement | Detail |
|-------------|--------|
| **Prerequisite** | **`recon-all`** must have been run successfully on the subject (you need the full FreeSurfer subject directory with `mri/`, `surf/`, etc.). |
| **Input data** | The pipeline uses **T1-weighted MRI** that was used for recon-all (internally it uses `norm.mgz`, `aseg.mgz`, `nu.mgz`, and transforms from the subject's `mri/` and `mri/transforms/`). No separate "HBT input file" — the subject directory is the input. |
| **Optional (Matlab only)** | For **T2 or high-res**: if using `segmentHA_T2.sh`, you provide an **additional NIfTI or MGZ volume** (e.g. a T2 or PD) aligned to the T1; the script will register it and use it for better subfield boundaries. |
| **Disk** | Enough space for the subject (typically a few GB per subject); subregion outputs add on the order of tens to hundreds of MB. |
| **RAM** | ~8 GB for T1-only (Matlab or Python); more if using high-res or longitudinal. |

**Commands (choose one)**

**Option A — FreeSurfer 7.3+ (recommended, no Matlab):**

```bash
export SUBJECTS_DIR=/path/to/your/subjects
segment_subregions hippo-amygdala --cross <subject_id>
```

**Option B — Matlab-based (T1 only):**

```bash
export SUBJECTS_DIR=/path/to/your/subjects
segmentHA_T1.sh <subject_id> $SUBJECTS_DIR
```

**Option C — Matlab-based (T1 + T2 for better subfields):**

```bash
segmentHA_T2.sh <subject_id> /path/to/T2.nii.gz T2ADNI 1 $SUBJECTS_DIR
```

**Where is the HBT output?**

Outputs are in the subject's **`mri/`** directory:

| Source | HBT label volume (example) | Volume stats (per subfield) |
|--------|----------------------------|-----------------------------|
| **segment_subregions** | `lh.hippoAmygLabels*.HBT.mgz`, `rh.hippoAmygLabels*.HBT.mgz` | `lh.hippoSfVolumes*.txt`, `rh.hippoSfVolumes*.txt`; also `stats/hipposubfields.*.stats` |
| **segmentHA_T1** | `lh.hippoAmygLabels-T1.v21.HBT.mgz`, `rh.hippoAmygLabels-T1.v21.HBT.mgz` | `lh.hippoSfVolumes-T1.v21.txt`, `rh.hippoSfVolumes-T1.v21.txt` |

The **.HBT.mgz** files are the segmentations with the **head/body/tail** hierarchy. Use these (and the corresponding volume/stats files) for HBT-level analysis.

**Expected runtime**

| Pipeline | Typical time per subject |
|----------|---------------------------|
| **segment_subregions hippo-amygdala** | **~10–15 minutes** (after recon-all) |
| **segmentHA_T1.sh** | **~10–20 minutes** (after recon-all) |
| **segmentHA_T2.sh** | **~15–30 minutes** (depends on registration of the extra volume) |
| **recon-all** (required first) | **~8–24 hours** (single subject on a typical workstation; no GPU for recon-all) |

So: **to get HBT**, run recon-all once, then run one of the commands above; **expect ~10–20 min** for the hippo-amygdala step. Total time is dominated by recon-all.

---

## 6. Practical Recommendations

| Goal | Recommendation |
|------|----------------|
| **Only T1, standard resolution (1 mm)** | Use **`segment_subregions hippo-amygdala --cross <subject>`** (FS 7.3+) to avoid Matlab runtime. Alternatively `segmentHA_T1.sh`. |
| **High-resolution T2 available** | Use **`segmentHA_T2.sh`** (Matlab-based) for better subfield accuracy; `segment_subregions` does not use T2. |
| **Longitudinal** | Use **`segment_subregions hippo-amygdala --long-base <base>`** (FS 7.3+) or **`segmentHA_T1_long.sh`**. |
| **Aggregating volumes across subjects** | Use [ConcatenateSubregionsResults](https://surfer.nmr.mgh.harvard.edu/fswiki/ConcatenateSubregionsResults) (or the older `asegstats2table` with the relevant `hipposubfields.*.stats` files). |

**Interpretation at 1 mm T1:** Internal subfield boundaries rely heavily on the ex vivo atlas prior. Volumes of small internal subregions (e.g. GC-DG, CA4, molecular layer) should be interpreted with caution; head/body/tail and larger subfields (e.g. subiculum, fimbria) are more reliable. For validation, higher-resolution (e.g. T2) is recommended when possible.

---

## 7. Open-Source Hippocampus Subfield Segmentation (HBT or FS60)

This section lists **open-source tools** that follow **either** FreeSurfer’s **HBT** or **FS60** label hierarchy (or both) for hippocampal subfield segmentation. A tool need not support both; following either is enough for inclusion. Tools that use other protocols/label sets (e.g. HippUnfold, HSF, ASHS, HIPS, HippoDeep) are not included here.

| Publication | GitHub / link | HBT/FS60 hierarchy | Model / method | Framework | Performance (vs manual / notes) | Hardware (tested) | Running time (per subject) |
|-------------|----------------|------------|----------------|-----------|----------------------------------|-------------------|----------------------------|
| Iglesias et al., *Neuroimage* 115 (2015); FS 7.3+: [SubregionSegmentation](https://surfer.nmr.mgh.harvard.edu/fswiki/SubregionSegmentation) | FreeSurfer: [freesurfer/freesurfer](https://github.com/freesurfer/freesurfer) (source) | **Both HBT and FS60** (plus full labels and CA). User chooses which hierarchy to use; pipeline produces all in one run. | Probabilistic atlas (ex vivo ~0.1 mm); Bayesian segmentation | Matlab (segmentHA_*) or Python (segment_subregions, FS 7.3+) | Good subfield definition; at 1 mm T1 internal subfield boundaries rely on prior; T2 improves accuracy (Matlab `segmentHA_T2.sh` only) | ~8 GB RAM (T1 only); more if T2/high-res | **segment_subregions hippo-amygdala:** ~10–15 min; **segmentHA_T1:** ~10–20 min; **recon-all** (required first): ~10+ h |

**Notes:**

- **Inclusion rule:** A tool is listed if it follows **either** HBT **or** FS60 (or both). It does not have to support both.
- **Current list:** FreeSurfer is the only open-source pipeline that natively outputs **HBT** and **FS60** (as label hierarchies); both are produced in the same run. See §4 and §4.1 for when to use which.
- **Other tools** (HippUnfold, HSF, ASHS, HIPS, HippoDeep, etc.) use different protocols/label sets and do not follow HBT or FS60; they are omitted from this table.

**Why aren’t there tools that follow HBT or FS60 and improve efficiency?**

One would expect **faster alternatives** that keep the same HBT or FS60 definitions (e.g. deep learning trained on FreeSurfer subfield output, or GPU-accelerated reimplementations). In practice:

- **FastSurfer** speeds up FreeSurfer’s **whole-brain** pipeline (cortical + aseg, ~1 h total) but does **not** include hippocampal subfield segmentation (no HBT or FS60). So there is no “FastSurfer for subfields” yet.
- **HSF, HippUnfold, ASHS** are faster (seconds to ~30 min) but use **different** anatomical protocols and label sets (Berron, unfolding, multi-atlas). They do not follow HBT or FS60, so they cannot replace FreeSurfer when compatibility with HBT/FS60 norms (e.g. 天坛 hospital) is required.
- **HippoDeep** uses “knowledge transfer” from FreeSurfer for **whole hippocampus** (not subfields); **hippodeep_subfields** exists but is unvalidated and not tied to HBT or FS60 labels.

So: **for strict HBT or FS60 compatibility**, FreeSurfer is currently the only option. A future tool that **replicates HBT or FS60** (same labels, same hierarchy) with better speed (e.g. DL or GPU) would qualify for this table; until then, efficiency gains for subfields come from tools that use other atlases and are not drop-in replacements.

**Open-source works that are HBT-compatible (search summary)**

Searches for hippocampus fine segmentation/parcellation tools that are **natively HBT-compatible** (or that output/map to HBT) yield the following. As of this writing, **no** standalone open-source tool other than FreeSurfer natively outputs the FreeSurfer HBT label set; the options below are either FreeSurfer itself, pipelines that **run** FreeSurfer, or resources to **build** HBT-compatible tools.

| Type | Name | Link | HBT compatibility | Notes |
|------|------|------|--------------------|--------|
| **Native HBT** | FreeSurfer (segment_subregions / segmentHA_*) | [freesurfer/freesurfer](https://github.com/freesurfer/freesurfer) | **Yes** — produces HBT (and FS60, CA, full) in one run | See §4–§6. Requires recon-all first. |
| **Pipeline (runs FS)** | RhinelandStudy/freesurfer6_pipeline | [RhinelandStudy/freesurfer6_pipeline](https://github.com/RhinelandStudy/freesurfer6_pipeline) | **Yes** — runs FreeSurfer recon-all + hippocampal subfields; output is FS (hence HBT) | Nipype wrapper; automates recon-all + subfields, collects stats (e.g. JSON). Docker available. |
| **Pipeline (runs FS)** | freesurfer/AutomatedFreeSurfer | [freesurfer/AutomatedFreeSurfer](https://github.com/freesurfer/AutomatedFreeSurfer) | **Yes** — runs FreeSurfer; hippocampal subfields are part of the workflow | Official FS automation; includes hippo subfield step. |
| **Atlas resource** | Subfield atlases in MNI-ICBM space | [SubfieldAtlasesICBMspace](https://surfer.nmr.mgh.harvard.edu/fswiki/SubfieldAtlasesICBMspace) | **Enables HBT** — hippocampal subfields + amygdala (HippoAmyg.zip) in MNI-ICBM 2009c | Label probabilities in standard space; use with your own registration + labeling to build a **custom** HBT-compatible pipeline (e.g. register T1 → MNI, propagate labels, then merge to HBT). |
| **Not HBT-native** | HSF, HippUnfold, ASHS, hippodeep_subfields | See §7 notes | **No** — different protocols (Berron, unfolding, multi-atlas) | Can be **mapped** to HBT with caveats; see §4 “Using HBT when your algorithm uses a different atlas.” |

**More works that use or support HBT (head/body/tail)**

| Type | Name | Link | Relation to HBT |
|------|------|------|------------------|
| **Downstream / post-processing** | **hippovol** | [garikoitz/hippovol](https://github.com/garikoitz/hippovol) | Segments the hippocampus **along the longitudinal axis** into **HEAD, BODY, TAIL, POSTERIOR** from FreeSurfer input (aseg or FS6 subfields). Reads `?h.hippoSfLabels-T1.v10.mgz` (FS6) or aseg hippocampi; output labels = head/body/tail. **HBT-compatible** (uses FS, produces head/body/tail). Matlab; Lerma-Usabiaga et al., *Hum Brain Mapp* 2016. |
| **Consortium / protocol** | **ENIGMA-Hippocampal Subfields** | [ENIGMA Hippocampal Subfields](https://enigma.ini.usc.edu/ongoing/enigma-hippocampal-subfields/) | Working group using **FreeSurfer-based** hippocampal subfield segmentation (including head, body, tail) for multi-site studies. QC procedures for FreeSurfer subfield output (incl. HBT) in collaborative studies. |
| **Review / QC** | FreeSurfer-based segmentation review + ENIGMA QC | McCann et al., *Hum Brain Mapp* 2021, [PMC8805696](https://pmc.ncbi.nlm.nih.gov/articles/PMC8805696/) | Review of FreeSurfer hippocampal subfield methods and **novel QC procedure** for ENIGMA and other consortia using FS subfields (head/body/tail). |
| **Validation / comparison** | Seiger et al. | *Front Neurosci* 2021, [10.3389/fnins.2021.666000](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2021.666000/full) | Compares **reliability** of FreeSurfer hippocampal subfield segmentation with T1 vs T2 vs multispectral input; reports effects in **head and body** subfields (e.g. molecular layer head, CA1 head, CA3 head/body). Uses FS (hence HBT hierarchy). |
| **Protocol (harmonized)** | Hippocampal Subfields Group (HSG) | Harmonized protocols for **body** (e.g. *Neuroimage* 2026) and **tail** (e.g. [biorxiv 2025.11.20.689476](https://www.biorxiv.org/content/10.1101/2025.11.20.689476v1)) | Multi-site harmonized **manual** segmentation protocols for hippocampal body and tail on high-res MRI. Define head/body/tail consistently for validation or training; not a replacement for FreeSurfer but used to align definitions across sites. |
| **Method / atlas** | Iglesias et al. longitudinal | *Neuroimage* 2016, [Bayesian longitudinal segmentation](http://www.nmr.mgh.harvard.edu/~iglesias/pdf/Neuroimage_2016_longitudinal.pdf) | Longitudinal hippocampal subfield segmentation (subject-specific atlas); produces head/body/tail–aware segmentations in FreeSurfer 6/7. |

**Summary:** For **native** HBT output, use **FreeSurfer** (or a pipeline that runs it). **hippovol** uses FS input and outputs head/body/tail along the long axis. **ENIGMA-Hippocampal Subfields** and related QC/review papers use FreeSurfer (hence HBT). To build a **custom** HBT-compatible tool, FreeSurfer’s **HippoAmyg** atlases in MNI-ICBM space provide the same label definitions. Other open-source hippocampus subfield tools (HSF, HippUnfold, ASHS, etc.) are not HBT-compatible out of the box but can be relabeled to HBT with the precautions in §4.

### 7.1 Recommendation: one method for "latest + HBT-compatible + GPU + SoTA"

**Constraint:** No single published method currently satisfies all four at once: **(1) as latest as possible, (2) natively HBT-compatible, (3) GPU-accelerated, (4) SoTA parcellation performance.** Native HBT today = FreeSurfer only (CPU); GPU + SoTA = DL tools that use different label schemes (e.g. HSF, HippUnfold).

**Recommended choice: HSF (Hippocampal Segmentation Factory)**

| Criterion | HSF |
|-----------|-----|
| **Latest** | Yes — 2023 release, actively maintained ([clementpoiret/HSF](https://github.com/clementpoiret/HSF), [hsf.readthedocs.io](https://hsf.readthedocs.io/)). |
| **HBT-compatible** | **Not native.** Uses a different subfield protocol (Berron-style: DG, CA1, CA2, CA3, subiculum). You obtain **HBT-compatible output** by **mapping**: (a) define head/body/tail along the long axis (e.g. anterior / middle / posterior thirds), and (b) map HSF subfield labels to HBT/FS60 names where possible. See §4 "Using HBT when your algorithm uses a different atlas"; validate against FreeSurfer on a subset and report "HBT-mapped from HSF." |
| **GPU** | Yes — ONNX Runtime with **CUDA** (and TensorRT, DirectML options). Inference in **seconds** per subject. |
| **SoTA** | Yes — validated against ASHS, HIPS, HippUnfold; reported **closer to manual segmentation** than those tools (Dice, Hausdorff, volumetric similarity; *Frontiers in Neuroinformatics* 2023). 2024 benchmarks (e.g. medRxiv 24311530) include HSF among top automatic methods. |

**Why HSF over alternatives**

- **FreeSurfer:** Only option for **native** HBT and 天坛 compatibility; no GPU for the subfield step and ~10–20 min (+ recon-all) per subject. Choose FreeSurfer if **strict native HBT** outweighs speed/GPU.
- **HippUnfold:** GPU and unfolding-based morphometry; different output scheme (no direct HBT label set); mapping to HBT would be custom. HSF has stronger head-to-head subfield overlap benchmarks in published comparisons.
- **DSnet (2024):** Newer architecture (Transformer + dual-branch) but small gain over 3D U-Net; no standard HBT output or widespread pipeline yet; less mature than HSF for off-the-shelf use.

**Practical workflow if you pick HSF**

1. Run **HSF** on T1w (and T2w if available) → get subfield labels (DG, CA1, CA2, CA3, subiculum).
2. Define **head/body/tail** along the hippocampal long axis (e.g. slice-based or centerline-based thirds).
3. Build a **mapping table** from HSF labels (+ head/body/tail) to HBT (or FS60) label names.
4. **Validate**: run FreeSurfer on a subset, compare volumes or Dice for "HBT-mapped from HSF" vs native FS HBT; document and report the mapping in methods.

**Summary:** For **latest + GPU + SoTA** with **HBT-compatible** (mapped) output, **HSF** is the best current choice; use the mapping and validation steps above. For **native** HBT with no mapping step, use **FreeSurfer** (and accept CPU, no GPU acceleration for the subfield module).

### 7.1 Recommendation: one method for "latest + HBT-compatible + GPU + SoTA"

**Constraint:** No single published method currently satisfies all four at once: (1) as latest as possible, (2) natively HBT-compatible, (3) GPU-accelerated, (4) SoTA parcellation performance. Native HBT today = FreeSurfer only (CPU); GPU + SoTA = DL tools that use different label schemes (e.g. HSF, HippUnfold).

**Recommended choice: HSF (Hippocampal Segmentation Factory)**

| Criterion | HSF |
|-----------|-----|
| **Latest** | Yes — 2023 release, actively maintained ([clementpoiret/HSF](https://github.com/clementpoiret/HSF), [hsf.readthedocs.io](https://hsf.readthedocs.io/)). |
| **HBT-compatible** | **Not native.** Uses Berron-style subfields (DG, CA1, CA2, CA3, subiculum). Obtain HBT-compatible output by **mapping**: define head/body/tail along the long axis (e.g. anterior/middle/posterior thirds) and map HSF labels to HBT/FS60 names. See §4; validate against FreeSurfer on a subset and report "HBT-mapped from HSF." |
| **GPU** | Yes — ONNX Runtime with CUDA (and TensorRT, DirectML). Inference in seconds per subject. |
| **SoTA** | Yes — validated vs ASHS, HIPS, HippUnfold; closer to manual segmentation (Dice, Hausdorff, volumetric similarity; *Frontiers in Neuroinformatics* 2023). 2024 benchmarks (medRxiv 24311530) include HSF among top methods. |

**Why HSF over alternatives:** FreeSurfer = only native HBT but CPU and slower. HippUnfold = GPU but different scheme; HSF has stronger subfield benchmarks. DSnet (2024) = newer architecture but no standard HBT pipeline yet.

**Workflow if you pick HSF:** (1) Run HSF on T1w (± T2w) → subfield labels. (2) Define head/body/tail along long axis. (3) Build mapping table HSF → HBT/FS60. (4) Validate vs FreeSurfer on a subset and report mapping in methods.

**Summary:** For latest + GPU + SoTA with HBT-compatible (mapped) output, **HSF** is the best current choice. For native HBT only, use **FreeSurfer** (CPU, no GPU for subfields).

---

## 8. Thoughts on Improving HBT (Efficiency and Accuracy)

Below are practical directions to improve **efficiency** (speed, hardware) and **accuracy** (boundary quality, robustness) of algorithms that produce HBT (or FS60)-compatible hippocampus subfield output. They apply both to improving the current FreeSurfer pipeline and to building alternative tools (e.g. deep learning) that target the same hierarchy.

### 8.1 Efficiency

| Direction | Idea | Notes |
|-----------|------|--------|
| **Deep learning surrogate** | Train a network (e.g. 3D U-Net, nnU-Net) to predict HBT (or FS60) labels from T1 (and optionally T2) using FreeSurfer output as training targets. Inference can be **minutes or seconds** on GPU instead of ~10–20 min (subfields) + ~10+ h (recon-all if full pipeline). | Preserves HBT/FS60 label set; requires many FS-processed subjects and careful train/val split; possible domain shift on new sites/contrasts. |
| **Skip or approximate recon-all for subfields only** | If the goal is **only** hippocampus subfields (HBT/FS60), use a **standalone** subfield module that needs minimal preprocessing (e.g. rigid alignment to a template + crop), instead of full recon-all. DL methods (HSF-style) show this is feasible; the open gap is to do it while **outputting HBT/FS60** labels. | Would remove the 10+ h recon-all bottleneck for subfield-only studies. |
| **GPU / parallelization** | FreeSurfer’s subregion step is largely CPU-bound. Porting the atlas deformation or replacing it with a GPU-friendly model (e.g. DL) would reduce wall-clock time. | segment_subregions already supports `--threads`; further gains need algorithmic change (e.g. DL) or GPU-accelerated registration. |
| **Coarse-to-fine or ROI-only** | Run full pipeline only on a **cropped** hippocampal ROI (e.g. from fast whole-brain segmentation or template registration) to reduce memory and compute. | Similar to what HSF does with ROILoc; for FS, would require a “hippocampus-only” mode that doesn’t require full recon-all. |
| **Caching and reuse** | For longitudinal or multi-contrast studies, cache registration and atlas alignment so that only the segmentation step is re-run when adding T2 or a new time point. | Already partly supported in longitudinal FS; can be extended for T1+T2 workflows. |

### 8.2 Accuracy

| Direction | Idea | Notes |
|-----------|------|--------|
| **Use T2 or high-resolution when available** | Subfield boundaries (especially CA1/subiculum, DG/CA3) are better defined on **T2 or T2-FLAIR** (e.g. 0.4–0.8 mm coronal). Use **segmentHA_T2.sh** with an additional T2 volume for better accuracy than T1-only. | FreeSurfer’s segment_subregions is T1-only; for best accuracy with T2, the Matlab-based segmentHA_T2.sh is currently required. |
| **Better prior / atlas** | Refine the ex vivo–based atlas (e.g. more specimens, better alignment, or in vivo high-res templates) so that the Bayesian prior better matches in vivo 1 mm T1 or 0.5 mm T2. | Research-level; improves all hierarchy levels (HBT, FS60, full) at once. |
| **Longitudinal consistency** | Use **longitudinal** FreeSurfer (segment_subregions hippo-amygdala --long-base or segmentHA_T1_long.sh) when multiple time points exist. Subject-specific atlases reduce scan-to-scan variability and often improve effective accuracy in group or change-over-time analyses. | Well validated in FS; recommended for serial data. |
| **Quality control and failure detection** | Add simple QC (e.g. volume ranges, shape checks, or a small classifier trained on known-good vs bad segmentations) to flag outliers and avoid propagating bad HBT/FS60 volumes into norms or models. | Especially important if deploying DL surrogates or new sites. |
| **Post-hoc refinement** | Optionally refine boundaries using **learning-based refinement** (e.g. a small network trained to correct systematic errors of the main pipeline) while keeping the same HBT/FS60 label set. | Keeps compatibility; can improve boundary placement where training data exist. |
| **Multi-site / scanner robustness** | If building a new model (e.g. DL), train on **multi-site and multi-scanner** data so that HBT/FS60 output is robust across field strength, resolution, and contrast. Use augmentation (intensity, resolution, geometry) and possibly domain adaptation. | Reduces accuracy drop on unseen sites. |

### 8.3 Summary

- **Efficiency:** The largest gain is to avoid or replace the **recon-all** dependency for subfield-only workflows (e.g. DL that takes T1 and optionally T2 and outputs HBT/FS60 directly). Secondary gains: GPU inference, ROI-only processing, better parallelization.
- **Accuracy:** Best levers are **T2 or high-res input** (via segmentHA_T2 when possible), **longitudinal** processing when applicable, and **QC**. For new algorithms, training on diverse data and targeting the same HBT/FS60 definitions preserves compatibility with existing norms (e.g. 天坛).

---

## 9. Relation to Normative / Brain-Chart Pipelines

The 天坛医院 (Charting CH) pipeline and similar normative models typically use **whole hippocampus volume** (e.g. from `aseg.stats`: `Left-Hippocampus`, `Right-Hippocampus`), not subfield volumes. If you need **subfield-level** metrics (e.g. CA1, DG) for research or clinical questions, you add the hippocampal subfield step **after** recon-all; the subfield volumes are **not** part of the default DK/aseg outputs used by the normative scripts.

---

## 10. References and Links

- **Hippocampus atlas (ex vivo):** Iglesias et al., *Neuroimage* 115, 2015 — [A computational atlas of the hippocampal formation using ex vivo, ultra-high resolution MRI](http://www.nmr.mgh.harvard.edu/~iglesias/pdf/subfieldsNeuroimage2015preprint.pdf).
- **Longitudinal:** Iglesias et al., *Neuroimage* 141, 2016 — Bayesian longitudinal segmentation.
- **Amygdala nuclei (same module):** Saygin, Kliemann et al., *Neuroimage* 155, 2017.
- **FreeSurfer wikis:**
  - [HippocampalSubfieldsAndNucleiOfAmygdala](https://surfer.nmr.mgh.harvard.edu/fswiki/HippocampalSubfieldsAndNucleiOfAmygdala)
  - [SubregionSegmentation](https://surfer.nmr.mgh.harvard.edu/fswiki/SubregionSegmentation)
  - [ConcatenateSubregionsResults](https://surfer.nmr.mgh.harvard.edu/fswiki/ConcatenateSubregionsResults)

---

## 11. Summary

| Question | Answer |
|----------|--------|
| Does **recon-all** fine parcellate the hippocampus? | **No** — only whole left/right hippocampus in aseg. |
| Can FreeSurfer fine parcellate the hippocampus? | **Yes** — via a **separate** hippocampal subfield (and amygdala) module run **after** recon-all. |
| How to run it (current, T1 only)? | **FreeSurfer 7.3+:** `segment_subregions hippo-amygdala --cross <subject>`. |
| T2 or high-res for better subfields? | Use **`segmentHA_T2.sh`** (Matlab-based); `segment_subregions` is T1-only. |
| Output volumes? | `lh/h.hippoSfVolumes*.txt` and stats; label volumes in `mri/` (e.g. `lh.hippoAmygLabels*.mgz`). |
