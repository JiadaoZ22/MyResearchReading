# Automatically Parcellating the Human Cerebral Cortex (自动划分人类大脑皮层) — Summary

**Source:** Fischl B, van der Kouwe A, Destrieux C, et al. *Cerebral Cortex* (大脑皮层) January 2004;14:11–22. DOI: 10.1093/cercor/bhg087.

---

## 1. Citation & Authors

- **Title:** Automatically Parcellating the Human Cerebral Cortex (自动划分人类大脑皮层)  
- **Authors:** Bruce Fischl, André van der Kouwe, Christophe Destrieux, Eric Halgren, Florent Ségonne, David H. Salat, Evelina Busa, Larry J. Seidman, Jill Goldstein, David Kennedy, Verne Caviness, Nikos Makris, Bruce Rosen, Anders M. Dale  
- **Affiliations:** MGH/MIT/Harvard Medical School Athinoula A. Martinos Center for Biomedical Imaging (生物医学成像中心); MIT AI Lab; Laboratoire d’Anatomie/CHRU Tours; Harvard Psychiatry (精神病学); Center for Morphometric Analysis (形态测量分析中心), MGH.

---

## 2. Abstract (Key Message)

The paper presents an **automated method** to assign a **neuroanatomical label (神经解剖学标签) to every point** on a **cortical surface (皮层表面)**. It uses:

- **Probabilistic information** from a manually labeled training set  
- **Geometric information** from the cortical surface (皮层表面) model  
- **Neuroanatomical convention (神经解剖学惯例)** encoded in the training set  

The result is a **full labeling of cortical sulci and gyri (脑沟与脑回)**. The method is shown to be **comparable in accuracy to manual labeling** and is flexible enough to work with different **parcellation (脑区划分)** schemes (e.g., CMA vs. surface-based).

---

## 3. Motivation & Background

- **Cortical parcellation (皮层脑区划分)** (labeling every point on the **cortex (皮层)**) is useful for **functional and structural neuroimaging (功能与结构神经影像)** but is **rarely used** because manual parcellation (脑区划分) of high-resolution **MRI (磁共振成像)** is **very time-consuming** (on the order of a week per subject).
- Prior work (**atlas (图谱)** warping, graph-based **sulcal (脑沟)** labeling, watershed on surfaces) either does not provide **complete** cortex (皮层) labeling or does not incorporate **prior information** and **cortical geometry (皮层几何)** in a unified way.
- **Prior information is critical:** useful divisions can depend on structure–function relationships, **cytoarchitecture (细胞构筑)**, or naming conventions (e.g., **sulci (脑沟)** changing names at **lobar boundaries (脑叶边界)**), not just geometry.

---

## 4. Methods (Overview)

### 4.1 Core Idea

- Use **manually parcellated subjects** as a training set.  
- Build an **atlas (图谱)** in a **surface-based (spherical) coordinate system (基于表面的球面坐标系)** that stores, at each atlas (图谱) location:
  - **Prior probability** of each parcellation (脑区划分) label  
  - **Class-conditional statistics** (e.g., **Gaussian (高斯)** mean and covariance) of **surface geometry (表面几何)** (e.g., **convexity (凸度)**, **mean curvature (平均曲率)**) for each label  
  - **Pairwise neighborhood probabilities** (probability that a neighbor has label *c*₂ given the central vertex has label *c*₁), separately for different neighbor directions  

- **Parcellation (脑区划分)** = **maximum a posteriori (MAP) (最大后验估计)** estimate of the label at each vertex given:
  - Observed surface geometry (表面几何)  
  - Nonlinear spherical mapping to the atlas (图谱)  
  - Prior over labels and **spatial relationships** between labels  

### 4.2 Technical Components

1. **Atlas (图谱) construction**
   - Surface-based registration aligns **folding patterns (脑回折叠模式)** across subjects (Fischl et al.).
   - For each atlas (图谱) location: estimate *p*(label) from label frequency; for each label, estimate mean and covariance of a **geometry vector** (e.g., convexity (凸度), mean curvature (平均曲率)) from the training set.
   - Store **anisotropic, non-stationary (各向异性、非平稳)** neighbor statistics: probability of neighbor label *c*₂ given central label *c*₁ and neighbor position *rᵢ*, separately for the **two principal curvature directions (两个主曲率方向)** (high vs. low curvature (曲率)), so that borders (e.g., **precentral gyrus (中央前回)** vs. **central sulcus (中央沟)**) are modeled in a direction-dependent way.

2. **Prior model**
   - Parcellation (脑区划分) is modeled as a **first-order anisotropic non-stationary Markov random field (MRF) (一阶各向异性非平稳马尔可夫随机场)**.
   - Prior: product over vertices of *p*(P(r)) and ∏ *p*(P(rᵢ) | P(r), rᵢ) over neighbors *rᵢ* in *N*(r).
   - This encodes both **global** location (via *p*(P(r))) and **local** label–neighbor relationships (e.g., “**precentral gyrus (中央前回)** often borders **central sulcus (中央沟)** in the high-curvature direction”).

3. **Likelihood**
   - At each vertex, geometry likelihood *p*(G(f(r)) | P(r)=c) is **Gaussian (高斯)** with mean µ_c(r) and covariance Σ_c(r) estimated from the training set.

4. **Optimization**
   - Global MAP with the MRF prior is intractable; the authors use **iterated conditional modes (ICM) (迭代条件众数)**:
     - Initialize with MAP ignoring neighbor dependencies.
     - Iteratively update each vertex to maximize the conditional posterior given current neighbors.
     - Convergence is fast (~3 min on a 1.5 GHz Pentium III); a small post-processing step relabels small isolated patches to the most likely neighboring label.

### 4.3 Implementation Details

- **Atlas (图谱):** spherical, supersampled icosahedra; priors at ~1 mm (163,842 vertices); class-conditional densities at ~4 mm (2562 vertices).
- **Geometry (几何):** e.g., average convexity (平均凸度) and mean curvature (平均曲率); additional features (**T1/T2 (T1/T2加权)**, **Gaussian curvature (高斯曲率)**, **thickness (皮层厚度)**) can be added.

---

## 5. Parcellation (脑区划分) Schemes Used

1. **CMA (Center for Morphometric Analysis) (形态测量分析中心)**  
   - **Volumetric parcellation (体积分区)** (Rademacher et al.; Caviness et al.) sampled onto the **cortical surface (皮层表面)**.  
   - **~58 labels** (see Appendix for full list: e.g., AG, F1, F2, PRG, INS, TP, T1a, T1p, etc.).

2. **Surface-based (SB) (基于表面)**  
   - Intrinsically surface-based scheme (Destrieux et al.), following Duvernoy (1991).  
   - **85 labels** (e.g., G_precentral (中央前回), S_central_insula (中央岛叶沟), S_calcarine (距状沟), G_cingulate-Main_part (扣带回主体), etc.).

---

## 6. Data & Validation

- **CMA:** 36 subjects (2 **MP-RAGE (磁化制备快速梯度回波)** each, motion-corrected and averaged); manual parcellation (脑区划分) by trained technicians; **cortical surfaces (皮层表面)** reconstructed and manual labels sampled to the **cortical ribbon (皮层带)**.
- **SB:** 12 subjects; 24 **hemispheres (半球)** manually parcellated with FreeSurfer surface-based tools.
- **Validation:** **Leave-one-out (jackknife) (留一法):** for each subject, build atlas (图谱) from the rest, parcellate the left-out subject, then compute **point-by-point % agreement** with manual labels.

---

## 7. Results

- **Accuracy:**  
  - **CMA:** median ~81% (left), ~83% (right).  
  - **SB:** median ~80% (left), ~79% (right). Slightly lower for SB is attributed to more (and smaller) labels.
- Most of the **cortical surface (皮层表面)** had **>75%** agreement; **~40%** of the surface was **100%** correct in both schemes.
- Errors are **concentrated at label boundaries**, where manual definitions are somewhat arbitrary.
- **Surface area (表面积)** of regions (manual vs. automated): means and standard errors were **statistically indistinguishable**; automated parcellation (脑区划分) often had **smaller error bars**, suggesting potential for **better sensitivity** to group differences.
- **Outliers:** e.g., subjects with rare **folding (脑回折叠)** (e.g., split **central sulcus (中央沟)**) had lower accuracy (~70%); the training set for that subject contained no such variant.

---

## 8. Conclusions & Significance

- The method provides **automated, full cortical parcellation (全皮层脑区划分)** that is **comparable in accuracy to validated manual parcellation (脑区划分)**.
- It combines **global** (atlas (图谱) location) and **local** (MRF neighbor relationships) information and can encode **neuroanatomical convention (神经解剖学惯例)** from the training set.
- It is **flexible** across parcellation (脑区划分) schemes (CMA vs. SB) and can be extended with more features (e.g., thickness (皮层厚度), **tissue contrast (组织对比)**).
- **Applications:** **ROI (感兴趣区)** definition for **fMRI (功能磁共振成像)** (e.g., average time courses by region), **morphometry (形态测量)** in large samples, and ultimately more sensitive **anatomical signatures (解剖学特征)** for disorders. Manual **whole-cortex (全皮层)** parcellation (脑区划分) is impractical at scale; this automation makes large-scale **morphometric (形态测量)** studies feasible.

---

## 9. Appendix (Label Lists)

- **CMA:** ~58 labels (e.g., AG (角回), F1 (额上回), F2 (额中回), F3o, F3t, PRG (中央前回), INS (岛叶), FP (额极), T1a (颞上回前部), T1p (颞上回后部), PT (颞平面), Pha (海马旁回前部), PHp (海马旁回后部), PCN (楔前叶), SPL (顶上小叶), etc.).
- **SB:** 85 labels (e.g., G_precentral (中央前回), S_central_insula (中央岛叶沟), S_calcarine (距状沟), G_cingulate-Main_part (扣带回主体), Lat_Fissure-ant_sgt-ramus_horizontal (外侧裂水平支), etc.).  

Full lists are in the paper Appendix.

---

## 10. References (Selected)

- Rademacher et al., Caviness et al. (CMA parcellation (脑区划分)); Destrieux et al. (SB parcellation); Duvernoy (**neuroanatomy (神经解剖学)**).
- Dale et al., Fischl et al. (surface reconstruction (表面重建), inflation (膨胀), spherical atlas (球面图谱), thickness (皮层厚度)).
- Geman & Geman (MRF); Besag (spatial statistics, ICM); Fischl et al. (**subcortical (皮层下)** MRF).
- Validation and applications: Goldstein et al. (**schizophrenia (精神分裂症)**, **sexual dimorphism (性别二态性)**); Seidman et al.; Boling et al. (**hand motor (手运动区)** and folding (脑回折叠)).

---

## 11. One-Sentence Summary

**Automated cortical parcellation (自动皮层脑区划分) is achieved by combining a surface-based probabilistic atlas (基于表面的概率图谱) (prior + geometry likelihood per label) with an anisotropic, non-stationary Markov random field (各向异性非平稳马尔可夫随机场) over labels, trained on manual parcellations (脑区划分); the method matches manual labeling accuracy and can be used with different neuroanatomical (神经解剖学) schemes (e.g., CMA or Destrieux-style surface-based).**
