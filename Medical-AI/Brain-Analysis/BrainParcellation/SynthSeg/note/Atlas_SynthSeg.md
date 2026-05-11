# What atlas does SynthSeg (+) use?

**Reference paper:** *Robust machine learning segmentation for large-scale analysis of heterogeneous clinical brain MRI datasets* (Billot et al., PNAS 2023)  
**Folder:** `fZ_Reference/BrainParcellation/SynthSeg/`

---

## Short answer

SynthSeg and SynthSeg+ use **the same label scheme as FreeSurfer**. They are **not** based on a different atlas; the **cortical parcellation** is the **Desikan–Killiany (DK) atlas** as implemented in FreeSurfer (`aparc`), and the **segmentation labels** (whole-brain + subcortical) follow FreeSurfer’s **aseg** classification.

So: **yes, the parcellation is derived from / identical to the FreeSurfer scheme**, which for cortex is the **Desikan–Killiany** atlas (68 cortical regions, 34 per hemisphere).

---

## Evidence

1. **FreeSurfer wiki (SynthSeg page)**  
   *"Please note that the **label values follow the FreeSurfer classification**."*  
   [https://surfer.nmr.mgh.harvard.edu/fswiki/SynthSeg](https://surfer.nmr.mgh.harvard.edu/fswiki/SynthSeg) (Section 7, list of segmented structures.)

2. **SynthSeg data in your repo**  
   In `f1_Code/Brain/SynthSeg_v1.4.1/data/labels table.txt`:  
   *"Please note that the **label values follow the FreeSurfer classification**."*  
   The listed labels (0, 2, 3, 4, … 60 for WM, cortex, ventricles, thalamus, caudate, etc.) match FreeSurfer’s aseg IDs.

3. **Cortical parcellation (--parc)**  
   SynthSeg 2.0 adds **cortical parcellation** (68 regions). In FreeSurfer, the default cortical parcellation is **Desikan–Killiany** (`aparc`). The SynthSeg parcellation model outputs the same label set as FreeSurfer’s `aparc+aseg` (aseg for subcortical/global structures, aparc = DK for cortex). Your project’s `ATLAS_MAPPING_SUMMARY.md` states: *"atlas mismatch between **SynthSeg's FreeSurfer aparc+aseg scheme** and Mindboggle101's DKT31 protocol"* — i.e. SynthSeg is explicitly treated as using the **FreeSurfer aparc+aseg** scheme.

4. **Paper (Billot et al., PNAS 2023)**  
   The paper reports comparison with **FreeSurfer** for volumes and ICV, and “cortical parcellation” without defining a new atlas; integration is “with FreeSurfer”. So the intended output is **compatible with FreeSurfer**, i.e. the same atlas (DK for cortex, aseg for the rest).

---

## Summary table

| Component              | Atlas / scheme                    | Same as                          |
|------------------------|-----------------------------------|----------------------------------|
| **Whole-brain segmentation** | FreeSurfer aseg-style labels      | FreeSurfer aseg                  |
| **Subcortical**        | Same label IDs as aseg            | FreeSurfer aseg                  |
| **Cortical parcellation** (with `--parc`) | 68 regions, same IDs as aparc     | **Desikan–Killiany** (FreeSurfer `aparc`) |

**Conclusion:** SynthSeg (+) does **not** use a different atlas. Its parcellation is **the FreeSurfer scheme**: **Desikan–Killiany** for the 68 cortical ROIs and **aseg** for subcortical and other structures. The network is trained to predict these same labels so that outputs can be used directly with FreeSurfer-based workflows and comparisons.

---

## Why does SynthSeg report 100 ROIs while FreeSurfer has 84?

When you run SynthSeg with **`--robust --parc --qc --vol`**, the **volume table** (CSV) has **100 ROIs in total**. Both use the **same atlas** (DK cortex + aseg subcortical). The difference is **which structures are counted as “ROIs”** in the volume output.

### FreeSurfer “84” ROIs

- **68** = Desikan–Killiany cortical (34 × 2 hemispheres), from **aparc**.
- **16** = subcortical from **aseg** (8 × 2): thalamus, caudate, putamen, pallidum, hippocampus, amygdala, accumbens, ventral DC.  
- **Total: 68 + 16 = 84** regional ROIs (what the 天坛医院 paper uses for “regional” measures, plus 8 global separately).

### SynthSeg **100** ROIs (with `--robust --parc --qc --vol`)

SynthSeg’s **volume table** (produced with `--vol`) is built as: **all segmentation labels** (whole-brain segmentation) **+ 68 cortical parcellation** (DK). It reports **100 ROIs in total** (every labeled structure that gets a volume row).

- **68** = same Desikan–Killiany cortical parcellation (same as FreeSurfer aparc).
- **32** = from the **segmentation** branch (FreeSurfer aseg-style labels), including:
  - **16** = the same 8 subcortical × 2 (thalamus, caudate, putamen, pallidum, hippocampus, amygdala, accumbens, ventral DC).
  - **16** = additional structures that FreeSurfer does **not** count as “regional ROIs” in the 84:
    - Ventricles: 6 (left/right lateral, left/right inferior lateral, 3rd, 4th)
    - Brainstem: 1  
    - CSF: 1  
    - Cerebellum: 4 (left/right cortex, left/right white matter)  
    - Cerebral white matter and cortex (whole hemisphere): 4 (left/right WM, left/right cortex)  
- **Total: 68 + 32 = 100 ROIs** in the volume table.

### Side-by-side

| Source        | Cortical (DK) | Subcortical (8×2) | Extra (ventricles, brainstem, CSF, cerebellum, cerebral WM/cortex) | **Total ROIs** |
|---------------|---------------|-------------------|-------------------------------------------------------------------|----------------|
| **FreeSurfer** (regional) | 68            | 16                | 0 (these are global/other in aseg.stats, not “84” ROIs)          | **84**         |
| **SynthSeg** (volume table: `--robust --parc --qc --vol`) | 68            | 16                | 16                                                                | **100**        |

So the **difference is not the atlas**: both use DK + aseg. The difference is that **SynthSeg outputs volumes for every segmentation label** (including ventricles, brainstem, CSF, cerebellum, and whole-hemisphere cerebral WM/cortex), while the **“84” FreeSurfer ROIs** are only the 68 cortical + 16 subcortical regional structures. The **16 “extra” ROIs in SynthSeg** are the same aseg labels that FreeSurfer uses for global/whole-brain or other stats (e.g. ventricles, brainstem, cerebellum) but that are not part of the 84 regional ROIs in the paper.
