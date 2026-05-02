# What Are “Peak Ages” in This Paper?

**Paper:** *Charting brain morphology in international healthy and neurological populations*  
**Folder:** `fZ_Reference/天坛医院/`

---

## 1. Short Answer

**Peak age** in this paper is **not** the age at which people are most likely to get Alzheimer’s disease (AD) or any other disease.

**Peak age** is the **age at which a brain structural measure (e.g. volume, thickness, surface area) reaches its maximum value** over the lifespan in the **healthy (normative) population**. It is a **developmental/maturational** concept: the age when that measure is at its peak in healthy individuals, after which it typically plateaus or declines.

---

## 2. Definition in the Paper

- The paper builds **normative references** (lifespan curves) for global and regional brain structural measures (gray matter volume, white matter volume, cortical thickness, surface area, CSF, etc.) using **healthy controls (HCs)**.
- For each measure, the **normative curve** describes how the **median** (and spread) of that measure changes with **age**.
- **Peak age** (also called **milestone** in the figures) is the **age at which this normative curve reaches its maximum value**:
  - *"The curves are presented with medians and 95% CIs … with **peak age corresponding to the maximum value**."*
  - So: **peak age = age at which the structural measure is highest** in the reference (healthy) population.

---

## 3. Examples from the Paper

| Measure | Meaning of “peak age” | Example (Chinese normative reference) |
|--------|------------------------|----------------------------------------|
| **Gray matter volume (GMV)** | Age when GMV is highest in HCs | ~5.9 years (95% bootstrap CI 5.8–6.1) |
| **Subcortical gray matter volume (sGMV)** | Age when sGMV is highest | ~14.4 years |
| **White matter volume (WMV)** | Age when WMV is highest | ~28.7 years |
| **Total surface area** | Age when total surface area is highest | ~11.0 years (ENA reference) |
| **Mean cortical thickness** | Age when mean thickness is highest | ~1.7 years (very early; then near-linear decrease) |
| **Cerebellum / brainstem volume** | Age when volume is highest | ~12.7 years |

- Many **volumes and surface area** peak in **childhood or young adulthood**, then decline or plateau.
- **Cortical thickness** peaks **very early** (around 1.7 years) and then decreases almost linearly from childhood onward in the normative curve.
- **Peak ages** are also compared between **Chinese (CH)** and **European/North American (ENA)** references (e.g. CH GMV peak 1.2 years later than ENA).

So “peak age” always refers to **the age of maximum value of a brain measure in healthy people**, not to disease onset.

---

## 4. Why It’s Not About AD or Disease Risk

- **Peak age** is defined on **normative (healthy) trajectories** only. It answers: “At what age is this measure at its maximum in the healthy population?”
- It is **not**:
  - The age at which people are most likely to get AD.
  - The age at which disease risk is highest.
  - An age of “disease peak” or “diagnosis peak.”
- **AD and other diseases** are studied in the paper by **deviation scores** (e.g. centile) from these normative references—i.e. how far an individual’s measure is from the healthy distribution at their age. Disease risk or likelihood of getting AD is a different question and is not what “peak age” refers to.

---

## 5. How Peak Ages Are Used in the Paper

- **Milestones / lifespan development:** Summarize at what age each brain measure reaches its maximum in the Chinese (and ENA) normative samples.
- **Population comparison:** Compare CH vs ENA peak ages (e.g. “later peak ages” in the Chinese sample for some measures).
- **Sensitivity and reliability:** Sensitivity analyses of “estimated peak ages” with varying sample sizes (e.g. Supplementary Results 4, Extended Data Fig. 4) assess how stable these developmental milestones are.
- **Figures:** “Milestones of CH normative references on global brain structural measures with peak age presented” (e.g. Fig. 2, Extended Data Figs. 2–4) show the age at maximum (peak age) for each measure.

---

## 6. How Are Peak Ages Used in Centile and Deviation Score Computation?

**Short answer: they are not used directly in the formula.** Centile and deviation scores are computed from the **fitted normative curve** (the full GAMLSS model). Peak age is a **derived summary** of that same curve, not an input to the scoring step.

**What is used in the computation:**

1. **Normative reference (GAMLSS):** The paper fits a **GAMLSS** model for each measure using healthy controls. The model gives, at **every age** (and sex), a **distribution**: location (e.g. median), scale (spread), and shape. So you have a full **lifespan curve** — median and spread as functions of age.
2. **Centile (deviation) score for an individual:** For a person with **age A** and **measure value Y**, the centile is the **percentile rank of Y** in the **distribution at age A** implied by the fitted model. In other words: use the model to get the expected distribution at the individual’s age (median_A, scale_A, shape_A), then compute the proportion of that distribution that is ≤ Y. That proportion is the centile (e.g. 0.25 = 25th percentile). No “peak age” value is plugged in here — only the **evaluation of the fitted curve at the individual’s age**.
3. **Where peak age comes in:** **Peak age** is the **age at which the fitted median curve reaches its maximum**. It is computed *from* the same GAMLSS fit (e.g. by finding the age that maximizes the fitted median). So the **curve** that is used for centile computation is the **same curve** that has a maximum at “peak age.” But the **number** “peak age” (e.g. 5.9 years for GMV) is **not** used in the centile formula — only the curve evaluated at the **subject’s** age is used.

**Summary:** Centile and deviation scores are computed by evaluating the **normative model at the individual’s age** and then ranking the individual’s value in that distribution. Peak age is the age at which that normative curve is highest; it describes the curve and is used for reporting and population comparison (e.g. CH vs ENA), but it is **not** a direct input to the centile/deviation calculation.

---

## 7. Why Do Peak Ages Matter?

Peak ages matter for several reasons:

1. **They define the normative trajectory.** The full lifespan curve (median and spread at each age) is what you use to compute **centile/deviation scores** for a new individual. The peak age is the age at which that curve reaches its maximum. So the curve—and thus the peak age—is a core part of the normative reference.

2. **They differ between populations.** The paper reports that **Chinese (CH) normative references show later peak ages than ENA references** (by about **1.2 to 8.9 years** depending on the measure). That means the **timing** of brain development/maturation is not the same in CH and ENA populations. If you used ENA norms for a Chinese individual (or the reverse), the **expected value at a given age** could be wrong, and so would the **centile score**. Peak age is a simple summary of that timing difference.

3. **They justify population-specific norms.** The paper concludes that there is a “critical need for constructing **population-specific** normative references.” The fact that peak ages (and the full curves) differ between CH and ENA is direct evidence that one set of norms cannot be safely applied to the other. So peak ages matter for **which** reference you use (CH vs ENA), not for comparing “who has bigger ROIs.”

4. **They summarize developmental milestones.** In research and clinical communication, reporting “GMV peaks at ~6 years in CH vs ~5 years in ENA” is a clear way to describe how lifespan trajectories differ between populations.

---

## 8. Are Peak Ages Used to Compare ROIs’ Sizing Difference Across Races?

**Not in the sense of “which race has larger or smaller ROIs.”**

- **Peak age** is the **age at which** a measure (e.g. GMV or an ROI volume) is **highest** in the healthy population. So the comparison (CH vs ENA) is about **when** that maximum is reached (timing of development), not about **how big** the measure is at that peak or at a fixed age.
- The paper does **not** use peak ages to say “Chinese have larger/smaller hippocampi than ENA” or to compare absolute ROI sizes across races. It uses them to say “the **age** at which GMV (or thickness, etc.) peaks is **later** in the Chinese sample than in the ENA sample.”
- **Actual “sizing” (absolute values)** at a given age is given by the **full normative curve** (median and spread at each age), not by the peak age alone. So:
  - **Peak ages** → compare **developmental timing** across populations (CH vs ENA).
  - **Full curves / medians at each age** → describe **expected size** at each age and support correct centile/deviation scoring.
- **Bottom line:** Peak ages are used to compare **populations (races)** in terms of **when** brain measures reach their maximum (developmental timing). They support the need for population-specific norms and correct use of CH vs ENA references. They are **not** the tool used to compare “ROI sizing difference across races” in the sense of absolute size; that would come from the full normative curves or from direct group comparisons of volumes at a given age.

---

## 9. One-Sentence Summary

**In this paper, “peak age” is the age at which a brain structural measure (volume, thickness, area, etc.) reaches its maximum value in the healthy normative population over the lifespan; it is a developmental milestone, not the age at which people are most likely to get AD or any other disease.**
