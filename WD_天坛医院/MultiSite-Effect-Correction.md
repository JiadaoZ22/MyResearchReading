# Multi-Site Effect Correction and Unifying Data from Various Sites

**Paper:** *Charting brain morphology in international healthy and neurological populations*  
**Folder:** `fZ_Reference/天坛医院/`

This README summarizes how the paper and its supplement handle **multi-site data** and compares the **GAMLSS** and **HBR** methods used for normative reference construction and site-effect mitigation.

---

## 1. Context: Multi-Site Data in This Study

- **24,061 healthy controls (HCs)** and **3,932 individuals with neurological diseases** from **34 provinces**, **105 sites**.
- Data were **retrospectively collected**; **data heterogeneity across sites** is a major challenge for building normative references.
- **Goal:** Build **Chinese (CH) normative references** of global and regional brain structural measures (from FreeSurfer on 3D T1-weighted MRI) and compute **deviation scores (centile scores)** for individuals, while **mitigating site effects** so that references are comparable across sites.

---

## 2. Overview of Approaches to Unify Multi-Site Data

The paper uses and compares several approaches:

| Approach | Role | Purpose |
|----------|------|---------|
| **GAMLSS** (primary) | Fit CH normative references | Model age/sex and **site as random effect** to absorb site variability. |
| **Site-calibrated ENA references** | Comparison | Calibrate existing ENA references using CH HC data (FS 6) **for site effects** (as in ref. 10). |
| **HBR** (hierarchical Bayesian regression) | Comparison (Supplementary Results 3, Extended Data Fig. 3) | Alternative fitting method that **mitigates multisite variability**; implemented via **PCNtoolkit**. |

Below we describe each and then the **overall process** of unifying data from various sites.

---

## 3. GAMLSS (Generalized Additive Models for Location, Scale and Shape)

### 3.1 What It Is

- **GAMLSS** is the **main method** used to build CH normative references (R package **GAMLSS**).
- It models not only the **mean** (location) of a structural measure as a function of covariates, but also **scale** and **shape** (e.g. variance, skewness), allowing flexible, potentially non-Gaussian normative curves over the lifespan.

### 3.2 How Site Effects Are Handled in GAMLSS

- **Fixed effects:** **Age** and **sex** (as in the paper: *"Age and sex were regarded as fixed effects"*).
- **Random effects:** **Site-specific protocols** (i.e. **site**) are included as **random effects** (*"site-specific protocols were regarded as random effects in the GAMLSS package"*).
- Including **site as a random effect** allows the model to **estimate and subtract site-specific shifts**, so that the normative curves represent a **population-level** relationship (age, sex) after accounting for between-site variability. This is the paper’s primary way of **unifying data from various sites** in the CH normative reference.

### 3.3 Other Design Choices That Support Multi-Site Validity

- **Stratified bootstrap:** *"Stratified bootstrap resampling (1,000 resampling with stratifying by sites) was conducted to calculate the CIs of normative references and associated peak ages."* Stratification by site keeps the multi-site structure in resampling and avoids over-representing single sites in the CIs.
- **Tenfold cross-validation:** Used to compute deviation scores for HCs so that each individual’s deviation score is computed from a normative reference **trained without that individual** (and the individual is not in the reference training set).

### 3.4 Role in Unifying Data

- Raw structural measures (volume, thickness, area, etc.) come from **many sites** with different scanners and protocols.
- GAMLSS **fits one normative model** over all HCs, with **site as random effect**, so that:
  - The **normative curves** (median, CIs, peak ages) are **site-adjusted** and can be used as a **single, unified reference** across sites.
  - **Deviation scores** for new individuals (from any site) are then computed against this unified reference.

---

## 4. Site-Calibrated ENA References

### 4.1 What They Are

- **ENA normative references** are previously established references based on data from **European and North American** populations (ref. 10).
- **Site-calibrated ENA references** are ENA references **calibrated for site effects** using **Chinese HC data** and **FreeSurfer 6** brain structural measures, as described in ref. 10 (*"calibrate the ENA references using brain structural measures derived from FS 6 for site effects as described previously"*).

### 4.2 Role in Unifying Data

- Calibration **adjusts the ENA reference for site (and population) differences** when applying it to the Chinese multi-site cohort, so that comparisons (e.g. CCC between CH and ENA references) are more meaningful.
- The paper reports that even **after calibration**, CH and ENA references still differ substantially for many measures (e.g. only a few measures like CSF and accumbens area showed relatively high CCCs), indicating **population-specific** differences beyond site effects.

---

## 5. HBR (Hierarchical Bayesian Regression)

### 5.1 What It Is

- **HBR** = **Hierarchical Bayesian Regression** framework, implemented in **PCNtoolkit** (refs. 14, 29).
- It is an alternative to GAMLSS for fitting **normative models** and is designed to handle **multi-site / multi-cohort** data in a hierarchical Bayesian way.

### 5.2 How the Paper Uses HBR

- The paper **compares** normative references fitted by **GAMLSS** vs **HBR** (Supplementary Results 3, **Extended Data Fig. 3**).
- **Extended Data Fig. 3**:
  - **Panel a:** Normative curves from GAMLSS vs HBR (similar units: volume ×10⁴ mm³, area ×10⁴ mm², thickness mm).
  - **Panel b:** **Z-scores across sites** (n = 105 sites) for GAMLSS and HBR. *"The closer the median value to zero, the better the site effects mitigated."*
  - **Panel c:** **Classification AUC maps** between pairs of sites; *"The closer the AUCs to zero, the better the site effects mitigated."*

### 5.3 Findings: GAMLSS vs HBR

- **HBR** *"could well fit the data and could sufficiently mitigate multisite variability across multiple sites."*
- **GAMLSS** *"had a comparative ability to mitigate multisite variability when site was considered a random effect."*
- **GAMLSS** *"demonstrated robust performance in local data fitting."*

So: **both** methods can mitigate multi-site variability when used appropriately (GAMLSS via site as random effect); **HBR** is reported as sufficiently mitigating site effects, and the paper suggests **HBR** as a more sophisticated alternative for future work to further reduce site-related bias (see Limitations).

---

## 6. Comparison: GAMLSS vs HBR

| Aspect | GAMLSS | HBR |
|--------|--------|-----|
| **Implementation** | R package GAMLSS | PCNtoolkit (refs. 14, 29) |
| **Site handling** | Site as **random effect** in the model | Hierarchical Bayesian model (multi-site structure in the hierarchy) |
| **Multisite variability** | Comparative ability to mitigate when site is random effect | Sufficiently mitigates multisite variability |
| **Local/data fit** | Robust performance in local data fitting | Fits data well |
| **Use in this paper** | **Primary** method for CH normative references and deviation scores | **Comparison** only (Supplementary Results 3, Extended Data Fig. 3) |
| **Validation** | Stratified bootstrap by site; tenfold CV for deviation scores | Evaluated via site-wise Z-scores and cross-site classification AUC |

---

## 7. Process of Unifying Data from Various Sites (Step-by-Step)

A concise flow of how multi-site data are unified into a single reference and then used for deviation scores:

1. **Data collection**  
   - 3D T1-weighted MRI from **105 sites**; visual and automatic (Euler number) QC; FreeSurfer cortical and subcortical parcellation (Desikan–Killiany and extended atlases).

2. **Normative reference construction (GAMLSS)**  
   - Fit one model per structural measure using **24,061 HCs**:
     - **Fixed effects:** age, sex.
     - **Random effects:** **site** (site-specific protocols).
   - This produces **site-adjusted** normative curves (median, CIs) and peak ages.
   - **Stratified bootstrap** (by site, 1,000 resamples) for CIs and peak-age uncertainty.

3. **ENA comparison and calibration**  
   - Compare CH references to **ENA** and **site-calibrated ENA** references (ref. 10; calibration for site effects using CH HC data and FS 6).
   - Consistency assessed via CCC; Extended Data Fig. 2.

4. **Algorithm comparison (GAMLSS vs HBR)**  
   - Fit normative references with **HBR** (PCNtoolkit) on the same data.
   - Compare site-effect mitigation via **Z-scores by site** and **cross-site classification AUC** (Extended Data Fig. 3).

5. **Deviation scores (centile scores)**  
   - For each individual (HC or patient), compute **deviation score** from the **CH normative reference** (GAMLSS).
   - **Tenfold cross-validation** for HCs so that no individual contributes to the reference used for their own score.
   - Downstream analyses use **age-, sex-, and site-matched (if available) HCs** for comparisons.

6. **Limitation**  
   - Data are retrospective and multi-site; **site as random effect in GAMLSS** may not remove all site-related bias. The paper states that **leveraging more sophisticated models (e.g. HBR)** to mitigate site variability would be an alternative for fitting normative references and warrants further validation and comparison (ref. 14).

---

## 8. Summary Table: Methods for Multi-Site Unification

| Method / step | Purpose in unifying multi-site data |
|---------------|--------------------------------------|
| **GAMLSS with site as random effect** | Primary: single site-adjusted normative reference; site variability absorbed by random effect. |
| **Stratified bootstrap by site** | CIs and peak ages respect site structure; avoid one site dominating. |
| **Tenfold CV for deviation scores** | Unbiased deviation scores; reference not contaminated by same subject. |
| **Site-calibrated ENA references** | Compare CH vs ENA after adjusting ENA for site (and population) using CH FS6 data. |
| **HBR (PCNtoolkit)** | Alternative normative model that sufficiently mitigates multisite variability; compared to GAMLSS in supplement. |
| **Age-, sex-, site-matched HCs** | Downstream case–control comparisons control for site when possible. |

---

## 9. References Cited in the Paper (Relevant to GAMLSS and HBR)

- **Ref. 10:** ENA normative references and site calibration (previous study).
- **Ref. 14:** Rutherford et al., normative modeling framework (PCNtoolkit / HBR context).
- **Ref. 29:** de Boer et al., non-Gaussian normative modelling (e.g. PCNtoolkit, hierarchical Bayesian regression).

For exact citations, see the reference list of *Charting brain morphology in international healthy and neurological populations*.
