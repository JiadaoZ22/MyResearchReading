# An Automated Labeling System for Subdividing the Human Cerebral Cortex (人类大脑皮层) on MRI (磁共振成像) Scans into Gyral-Based (基于脑回的) Regions of Interest (感兴趣区) — Summary

**Source:** Desikan RS, Ségonne F, Fischl B, et al. *NeuroImage* 31 (2006) 968–980. DOI: 10.1016/j.neuroimage.2006.01.021.

---

## 1. Citation & Authors

- **Title:** An automated labeling system for subdividing the human cerebral cortex (人类大脑皮层) on MRI (磁共振成像) scans into gyral-based (基于脑回的) regions of interest (感兴趣区)
- **Authors:** Rahul S. Desikan, Florent Ségonne, Bruce Fischl, Brian T. Quinn, Bradford C. Dickerson, Deborah Blacker, Randy L. Buckner, Anders M. Dale, R. Paul Maguire, Bradley T. Hyman, Marilyn S. Albert, Ronald J. Killiany
- **Affiliations:** Boston University School of Medicine (Anatomy and Neurobiology); MGH Athinoula A. Martinos Center for Biomedical Imaging (生物医学成像中心); MIT CSAIL; MGH Psychiatry (精神病学); Harvard Psychology; UCSD Neuroscience/Radiology; MGH Neurology (神经内科); Johns Hopkins Neurology; Pfizer.

---

## 2. Abstract (Key Message)

The paper evaluates **validity and reliability** of an **automated labeling system** that subdivides the **human cerebral cortex (人类大脑皮层)** on **MRI (磁共振成像)** into **gyral-based (基于脑回的) regions of interest (ROI, 感兴趣区)**. Using 40 **MRI (磁共振成像)** scans, 34 **cortical (皮层的) ROIs (感兴趣区)** were manually identified in each **hemisphere (半球)** and encoded in an **atlas (图谱)** used for automatic labeling. **Validity (效度)** and **intra-/inter-rater reliability (评分者内/间信度)** were assessed with **intraclass correlation coefficients (ICC, 组内相关系数)** and a new **mean distance maps (平均距离图)** method. Automated ROIs were highly accurate versus manual (average **ICC (组内相关系数)** 0.835; mean distance error <1 mm). Intra- and inter-rater comparisons showed little to no difference. The method is **anatomically valid (解剖学上有效) and reliable (可靠)** and may be useful for **morphometric (形态测量)** and **functional (功能)** studies and **clinical (临床)** investigations (e.g., tracking **disease (疾病)** progression, **clinical trials (临床试验)**).

---

## 3. Introduction & Background

- **Structural MRI (结构磁共振成像)** is important for characterizing **cortical (皮层)** changes in **aging (衰老)** and **dementia (痴呆)** (e.g., **Alzheimer’s disease (AD, 阿尔茨海默病)**) and for **clinical trials (临床试验)** (e.g., **multiple sclerosis (MS, 多发性硬化)**).
- Quantifying **cortical ROIs (皮层感兴趣区)** has been limited; **inter-individual variability (个体间变异)** of **cortical (皮层)** topography makes automated **cortical (皮层)** parcellation challenging.
- Prior work: manual/semi-automated ROI definition (e.g., **hippocampus (海马)**, **cingulate gyrus (扣带回)**); template warping; watershed/graph-based **sulcal (脑沟)** methods. Fischl et al. (2004) introduced a **probabilistic labeling (概率标注)** algorithm applicable to different **neuroanatomical (神经解剖学)** templates.
- This study: (1) defines ROIs on **inflated (膨胀)** surfaces using **curvature (曲率)** (sulcal) information to improve manual definitions; (2) uses a training set of 40 scans (young, middle-aged, elderly, and **AD (阿尔茨海默病)** patients) to build a **generalized atlas (通用图谱)**; (3) assesses validity/reliability with **ICC (组内相关系数)** and **mean distance maps (平均距离图)**; (4) uses **jackknife/leave-one-out (留一法)** to test applicability to novel data.

---

## 4. Methods (Overview)

### 4.1 Subjects

- 40 subjects from Washington University **ADRC (阿尔茨海默病研究中心)**. Screened for **neurological (神经学)** impairment, **depression (抑郁)**, **psychoactive medications (精神药物)**; excluded major **vascular (血管)** risk factors and relevant **MRI (磁共振成像)** abnormalities (e.g., **tumors (肿瘤)**, **infarcts (梗死)**). **White matter hyperintensities (白质高信号)** allowed. **Dementia (痴呆)** screening via **Clinical Dementia Rating (CDR, 临床痴呆评定量表)**.
- Four groups: young (n=10, mean 21.5 y); middle-aged (n=10, 49.8 y); elderly (n=10, 74.3 y); **AD (阿尔茨海默病)** (n=10, 78.2 y).

### 4.2 MRI (磁共振成像) Acquisition

- **1.5T** scanner; **T1-weighted MP-RAGE (T1加权磁化制备快速梯度回波)**; 1×1×1.25 mm; two sagittal acquisitions averaged.

### 4.3 Cortical (皮层) Surface Generation

- **FreeSurfer** pipeline: motion correction, intensity normalization, resampling to 1 mm isotropic; **skull stripping (去颅骨)**; **gray/white matter (灰质/白质)** boundary segmentation; **white matter (白质)** surface; topology correction; **pial (软脑膜/皮层)** surface. Manual quality review by trained operators.

### 4.4 Manual Delineation of Cortical (皮层) ROIs (感兴趣区)

- 34 **cortical (皮层)** regions per **hemisphere (半球)** defined by one operator (blind to age, gender, group). **Sulcal approach (脑沟法)**: tracing from sulcus depth to sulcus, including the **gyrus (脑回)**. Definitions based on atlases (Duvernoy, Ono et al.), prior literature, and expert consultation. **Volumetric (体积)** ROIs drawn on T1, then transferred to **inflated (膨胀)** surface; final labels refined using **curvature (曲率)** (sulci) on **inflated (膨胀)** surface so that **sulci (脑沟)** and **gyri (脑回)** are fully visible.

### 4.5 ROI (感兴趣区) Definitions (Summary)

- **Temporal:** superior/middle/inferior **temporal gyrus (颞上/中/下回)**, **transverse temporal cortex (颞横回)**, banks of **superior temporal sulcus (颞上沟)**; **entorhinal cortex (内嗅皮层)**, **parahippocampal gyrus (海马旁回)**, **temporal pole (颞极)**, **fusiform gyrus (梭状回)**.
- **Frontal:** **superior frontal gyrus (额上回)**, **middle frontal gyrus (额中回)** (rostral/caudal), **inferior frontal gyrus (额下回)** — **pars opercularis (岛盖部)**, **pars triangularis (三角部)**, **pars orbitalis (眶部)**; **orbitofrontal cortex (眶额皮层)** (lateral/medial); **frontal pole (额极)**; **precentral gyrus (中央前回)**.
- **Parietal:** **postcentral gyrus (中央后回)**, **paracentral lobule (中央旁小叶)**, **supramarginal gyrus (缘上回)**, **superior parietal cortex (顶上皮层)**, **inferior parietal cortex (顶下皮层)**, **precuneus (楔前叶)**.
- **Occipital:** **lingual gyrus (舌回)**, **pericalcarine cortex (距状沟周围皮层)**, **cuneus (楔叶)**, **lateral occipital cortex (外侧枕叶皮层)**.
- **Cingulate:** **rostral anterior (喙侧前部)**, **caudal anterior (尾侧前部)**, **posterior (后部)**, **isthmus (峡部)** divisions; **corpus callosum (胼胝体)** (used to bound other regions, not as a measured ROI).

### 4.6 Construction of Cortical (皮层) Atlas (图谱)

- After manual ROIs for all 40 brains (both **hemispheres (半球)**), a **cortical atlas (皮层图谱)** was built: **surface-based registration (基于表面的配准)** aligning **cortical folding patterns (皮层折叠模式)** (Fischl et al.); **probabilistic (概率)** assignment of **neuroanatomical (神经解剖学)** region to every point on the **cortical surface (皮层表面)** (Fischl et al., 2004). Algorithm: spherical representation → multi-subject registration → **spherical surface-based coordinate system (球面表面坐标系)** → **first-order anisotropic non-stationary Markov random field (MRF) (一阶各向异性非平稳马尔可夫随机场)** on **curvature (曲率)** to label **sulcal (脑沟)** and **gyral (脑回)** geometry with spatial priors from the training set.

### 4.7 Data Analysis

- **ICC (组内相关系数):** Manual vs. automated (validity): two-way **ANOVA (方差分析)** fixed effects. Intra-rater and inter-rater (reliability): two-way **ANOVA (方差分析)** random effects.
- **Mean distance maps (平均距离图):** For each subject, two distance maps (one per labeling system) give **geodesic distance (测地距离)** from each **vertex (顶点)** to the label border on the **inflated surface (膨胀表面)**. Average of the two = individual mean distance map; average across subjects = group mean distance map. Provides **point-by-point mismatch (逐点失配)** and visualization of **sulcal (脑沟)** boundary errors (e.g., 0.5 mm red, 1 mm yellow).
- **Jackknife/leave-one-out (留一法):** For each subject, atlas built from 39 others; applied to left-out subject; mismatch vs. manual quantified. Repeated for all 40; average mismatch compared to original manual vs. automated to test applicability to novel data.

---

## 5. Results

- **Validity (manual vs. automated):** 32 of 34 labels per **hemisphere (半球)** analyzed (**corpus callosum (胼胝体)** excluded; **frontal pole (额极)** excluded due to low **ICC (组内相关系数)** ~0.26). Average **ICC (组内相关系数)** = **0.835** (range 0.623–0.977). Sixty of 64 labels had **ICC (组内相关系数)** >0.70. Smaller **ROIs (感兴趣区)** (e.g., **temporal pole (颞极)**, banks of **superior temporal sulcus (颞上沟)**) had lower **ICC (组内相关系数)**; expected given **labeling error (标注误差)** scales with region size (~mm-level accuracy). **Mean distance maps (平均距离图):** mismatch concentrated at **region boundaries (区域边界)**; errors <1 mm.
- **Intra-rater and inter-rater reliability:** Minimal difference between operators/occasions; automated system highly reproducible.
- **Jackknife:** Average mismatch from **leave-one-out (留一法)** similar to original manual vs. automated comparison; atlas generalizes to novel subjects.

---

## 6. Conclusions & Significance

- The **automated labeling system (自动标注系统)** for **gyral-based (基于脑回的)** **cortical (皮层)** **ROIs (感兴趣区)** is **anatomically valid and reliable**, with high **ICC (组内相关系数)** and sub-millimeter **mean distance error (平均距离误差)**. **Mean distance maps (平均距离图)** allow visualization of **anatomical (解剖)** consistency and show that discrepancies are largely at **sulcal (脑沟)** boundaries where sub-mm precision may be unrealistic.
- The **generalized atlas (通用图谱)** approach (wide age and **atrophy (萎缩)** range) trades slight loss of accuracy in a narrow group for applicability across **aging (衰老)**, **AD (阿尔茨海默病)**, and **morphometric (形态测量)** studies.
- **Applications:** **Morphometric (形态测量)** and **functional (功能)** studies of the **cerebral cortex (大脑皮层)**; **clinical trials (临床试验)** using **MRI (磁共振成像)** to track **disease (疾病)** progression or treatment response; **co-registration (配准)** with **fMRI (功能磁共振成像)**, **PET (正电子发射断层成像)**, **SPECT (单光子发射计算机断层成像)**.
- **Limitation:** Small **ROIs (感兴趣区)** (e.g., **temporal pole (颞极)**) less reliable; future work may integrate **subcortical (皮层下)** or other cues to improve small-region accuracy.

---

## 7. Key ROIs (34 per Hemisphere (半球)) — With Chinese

| ROI | 中文 |
|-----|------|
| Banks superior temporal sulcus | 颞上沟岸 |
| Caudal anterior cingulate cortex | 扣带回尾侧前部 |
| Caudal middle frontal gyrus | 额中回尾侧部 |
| Cuneus cortex | 楔叶皮层 |
| Entorhinal cortex | 内嗅皮层 |
| Fusiform gyrus | 梭状回 |
| Inferior parietal cortex | 顶下皮层 |
| Inferior temporal gyrus | 颞下回 |
| Isthmus cingulate cortex | 扣带回峡部 |
| Lateral occipital cortex | 外侧枕叶皮层 |
| Lateral orbital frontal cortex | 眶额皮层外侧部 |
| Lingual gyrus | 舌回 |
| Medial orbital frontal cortex | 眶额皮层内侧部 |
| Middle temporal gyrus | 颞中回 |
| Parahippocampal gyrus | 海马旁回 |
| Paracentral lobule | 中央旁小叶 |
| Pars opercularis | 岛盖部 |
| Pars orbitalis | 眶部 |
| Pars triangularis | 三角部 |
| Pericalcarine cortex | 距状沟周围皮层 |
| Postcentral gyrus | 中央后回 |
| Posterior cingulate cortex | 扣带回后部 |
| Precentral gyrus | 中央前回 |
| Precuneus cortex | 楔前叶皮层 |
| Rostral anterior cingulate cortex | 扣带回喙侧前部 |
| Rostral middle frontal gyrus | 额中回喙侧部 |
| Superior frontal gyrus | 额上回 |
| Superior parietal cortex | 顶上皮层 |
| Superior temporal gyrus | 颞上回 |
| Supramarginal gyrus | 缘上回 |
| Temporal pole | 颞极 |
| Transverse temporal cortex | 颞横回 |
| (+ Frontal pole, Corpus callosum — excluded from ICC) | 额极、胼胝体 |

---

## 8. One-Sentence Summary

**Desikan et al. present and validate an automated gyral-based (基于脑回的) cortical (皮层的) ROI (感兴趣区) labeling system built from 40 manually labeled MRI (磁共振成像) scans using FreeSurfer surface reconstruction (表面重建) and the Fischl et al. (2004) probabilistic (概率) atlas (图谱); validity and reliability are high (ICC ~0.835, mean distance <1 mm), with mean distance maps (平均距离图) and jackknife (留一法) supporting anatomical accuracy and generalizability to novel data.**
