# WD Agent Launch

## Question

Can the paper *Charting brain morphology in international healthy and neurological populations* support the message:

> "让智能体用‘中国尺子’，读懂中国人的脑，把 AD 早筛的窗口，提前 x 年？"

Short answer: **it supports the "中国尺子" part strongly, but it does not directly prove a precise `x` years of earlier AD detection**.

## Bottom Line

- **What the paper clearly supports**
  - Use a **Chinese normative reference** to read Chinese brains, instead of borrowing ENA norms.
  - This improves the validity of deviation scoring for Chinese individuals because Chinese and ENA lifespan trajectories differ.
  - AD-related structural abnormality is already visible at the **MCI stage**, not only at diagnosed AD stage.

- **What the paper does not directly support**
  - It does **not** report a validated number like "AD can be found 5 years earlier" or "8 years earlier" in Chinese people.
  - It does **not** provide a prospective lead-time analysis from normal cognition to future AD conversion.

- **Most defensible proxy for `x`**
  - If you must give a cautious, evidence-based proxy, the best one in these materials is:
  - **`x ≈ 3.3 years`**
  - Reason: the paper's Table 1 gives mean age:
    - **MCI:** `64.85` years
    - **AD:** `68.15` years
    - Difference: **`68.15 - 64.85 = 3.30 years`**
  - This means the framework is able to detect an **AD-like structural deviation pattern already in the MCI group**, whose average age is about **3.3 years younger** than the AD group.

### Why compare MCI and AD only for this “x years” proxy?

The paper includes **six disease groups**: AD, MCI, PD, CSVD, MS, NMOSD. Only **MCI and AD** lie on the **same disease continuum** (MCI often precedes AD). The other four are **different diseases** with different age-at-diagnosis and different structural signatures. So:

- **MCI vs AD:** Same condition at different stages → the mean age gap (3.3 years) is a plausible proxy for “how much earlier” the window moves when you detect an AD-like pattern at the MCI stage.
- **PD, CSVD, MS, NMOSD:** Their mean ages (e.g. PD 61.3, CSVD 60.6, MS 36.3, NMOSD 43.4 years from Table 1) are not “earlier AD”; they are different diseases. The benefit there is **differential diagnosis** and **faster triage** (see below), not “x years earlier AD.”

So the “3.3 years” proxy is intentionally restricted to the **AD–MCI continuum**; other benefits are framed as time saved in **accuracy**, **differential diagnosis**, and **method choice**, not as another “x years earlier” number.

## Important Caveat

This **3.3-year number is only a rough observational proxy**, not a proven screening lead time.

Why:

- MCI and AD here are **different groups**, not the same people followed over time.
- The paper is **cross-sectional**, not a longitudinal conversion study.
- So it is **not scientifically safe** to say:
  - "this method finds AD exactly 3.3 years earlier."
- It is safer to say:
  - "this work suggests the AD screening window may move forward to the MCI-stage structural deviation window, which is about 3.3 years earlier than the mean age of the AD cohort in this Chinese dataset."

## Strongest Evidence Chain

### 1. "中国尺子" is justified

The materials consistently show that **Chinese normative references differ from ENA references**:

- Chinese peak ages are **later by about 1.2 to 8.9 years** depending on the measure.
- Therefore, using ENA norms for Chinese individuals can give the wrong expected value at a given age, and thus the wrong centile/deviation score.

This supports the message:

> 要用“中国尺子”读懂中国人的脑。

Relevant local notes:

- `fZ_Reference/WD_天坛医院/README_BlackBox_Normative_Pipeline.md`
- `fZ_Reference/WD_天坛医院/Peak-Ages.md`
- `fZ_Reference/WD_天坛医院/README_Age_Censoring.md`

### 2. The framework detects AD-related change before full AD stage

The paper shows that the MCI group already has measurable AD-like structural deviation:

- **MCI DPS:** `0.73` (IQR `0.61-0.80`)
- **AD DPS:** `0.93` (IQR `0.89-0.94`)
- **Largest MCI regional effect explicitly stated:** left entorhinal volume, Cohen's `d = 0.55` (95% CI `0.36-0.75`)

This supports:

- the method is not only recognizing established AD,
- it is already capturing disease-related morphology in an earlier clinical stage.

Relevant local notes:

- `fZ_Reference/WD_天坛医院/VALIDATED_NUMBERS.md`
- `fZ_Reference/WD_天坛医院/FINAL_VALIDATION_SUMMARY.md`
- `fZ_Reference/WD_天坛医院/Study_AD-brainAtrphy.md`

### 3. AD is strongly separable using multivariate deviation scores

Verified metrics in the materials:

- **AUC for AD classification:** `0.89` (95% bootstrap CI `0.87-0.91`)
- **AD DPS:** `0.93` (IQR `0.89-0.94`)
- **MCI DPS:** `0.73` (IQR `0.61-0.80`)
- **AD global deviation:** Cohen's `d = 0.82`
- **AD left amygdala:** Cohen's `d = 1.06`

This supports that the Chinese normative framework is clinically meaningful for AD-related pattern detection.

## Further benefits in saving time of disease detection (from the materials)

The paper and project notes describe several ways the framework **reduces time to correct detection or diagnosis**, beyond the MCI vs AD age proxy. All points below are grounded in the materials.

### 1. Avoiding misclassification: use Chinese norms, not ENA

- **Evidence:** Chinese normative trajectories differ from ENA (e.g. peak ages **1.2–8.9 years later** depending on measure; different hippocampal decline after age 60). The paper states that population-specific norms are **necessary** and that using ENA norms for Chinese patients **may misclassify**.
- **Time benefit:** If a centre used ENA norms for Chinese individuals, some would be misclassified (e.g. normal labelled at-risk, or vice versa). Correcting this later costs extra visits and re-assessments. Using the **“中国尺子” (Chinese ruler)** from the start **avoids that delay** and gets the right result earlier in the care path.

### 2. Deviation scores vs raw volumes / z-scores

- **Evidence:** The paper states that **deviation scores (centile scores) outperformed raw structural measures and z-scores** in clinical classification tasks (Extended Data Fig. 6: centile best, z-scores good, raw poorest). Multivariate deviation scores achieved **AUC 0.89** for AD classification.
- **Time benefit:** With the **same** MRI, using deviation scores gives **better sensitivity/specificity** than raw volumes or simple z-scores. So the **same scan** leads to **earlier and more reliable** detection of disease-related deviation, reducing the need for repeat scans or delayed diagnosis due to borderline/ambiguous raw measures.

### 3. Multi-ROI vs single-ROI

- **Evidence:** The paper states that **multivariate models combining multiple regional deviation scores achieved superior classification performance compared to single-ROI approaches** (e.g. hippocampus alone). Multi-ROI reduces false positives/negatives from other causes of single-ROI change.
- **Time benefit:** Fewer **missed cases** (false negatives) and fewer **wrong alarms** (false positives) means less time lost to wrong treatment paths or unnecessary follow-up. **Faster path to the correct diagnosis** with one assessment.

### 4. One framework for six diseases: differential diagnosis in one go

- **Evidence:** The paper provides **DPS and regional deviation patterns** for **AD, MCI, PD, CSVD, MS, NMOSD** in the same Chinese normative framework (e.g. DPS per disease, Cohen’s *d* per ROI per disease in Supplementary Data 2).
- **Time benefit:** A **single** structural assessment can yield **disease propensity scores and deviation maps** for all six conditions. That supports **differential diagnosis** (e.g. AD vs PD vs CSVD) **without waiting** for multiple disease-specific workups. So **time to differential triage** is shortened compared to sequential, disease-by-disease evaluations.

### 5. Early sensitivity: entorhinal and thickness

- **Evidence:** The paper reports that **MCI** shows the largest effect in **left entorhinal volume** (Cohen’s *d* = 0.55) and describes entorhinal as **earliest cortical involvement** and gateway to hippocampus. It also recommends **including cortical thickness** in addition to volume, as thickness is **highly sensitive to AD pathology** and gives complementary information.
- **Time benefit:** The method is **sensitive to early, pre-dementia change** (entorhinal, thickness), so abnormality can be **flagged earlier** in the disease course than with measures that change only later. That supports moving the **detection window earlier** (consistent with the MCI-stage / 3.3-year proxy) and can reduce time from first concern to first actionable finding.

### 6. Summary table (benefits and how they “save time”)

| Benefit | What the materials say | How it saves time |
|--------|-------------------------|--------------------|
| Chinese norms | ENA norms may misclassify Chinese; population-specific norms necessary | Avoids wrong classification and later re-assessment with correct norms |
| Deviation scores | Outperform raw volumes and z-scores in classification | Same scan → more reliable detection, fewer repeat scans or delayed decisions |
| Multi-ROI | Outperform single-ROI (e.g. hippocampus only) | Fewer false negatives/positives → less time on wrong diagnostic path |
| Six diseases in one framework | DPS and deviations for AD, MCI, PD, CSVD, MS, NMOSD | One assessment → differential triage, shorter time to differential diagnosis |
| Early markers (entorhinal, thickness) | MCI largest effect in entorhinal; thickness sensitive to AD | Flags deviation earlier in disease course → earlier detection window |

## Best Claim Wording

### Recommended, scientifically safer version

> 让智能体用“中国尺子”，读懂中国人的脑，把 AD 风险识别窗口前移到 MCI 阶段；在这篇中国人群研究里，这个窗口相对 AD 队列的平均年龄，大约可前移 **3.3 年**。

### Even safer wording

> 现有证据不支持直接宣称“提前 x 年确诊 AD”，但支持这样一句话：用“中国尺子”可以更准确地识别中国人脑的 AD 相关偏离，而且这种偏离在 MCI 阶段已经可见。若以本研究中 MCI 与 AD 队列的平均年龄差作为粗略参照，窗口约可前移 **3.3 年**。

### Not recommended

Avoid writing:

- "可以把 AD 早筛提前 5 年/8 年"
- "已经证明能提前 x 年发现 AD"

because that would require a **longitudinal** study tracking cognitively normal Chinese individuals into MCI/AD conversion.

## Suggested One-Line Launch Copy

If you need one launch sentence now, use:

> 用“中国尺子”读懂中国人的脑：这项工作不只是在 AD 期识别异常，还能把识别窗口前移到 MCI 阶段；按该研究中 MCI 与 AD 队列的平均年龄差粗略估计，窗口约可前移 **3.3 年**。

## Evidence Sources Used Here

- `fZ_Reference/WD_天坛医院/VALIDATED_NUMBERS.md`
- `fZ_Reference/WD_天坛医院/FINAL_VALIDATION_SUMMARY.md`
- `fZ_Reference/WD_天坛医院/Study_AD-brainAtrphy.md`
- `fZ_Reference/WD_天坛医院/CHN_ADvsHC-5diseases.md`
- `fZ_Reference/WD_天坛医院/README_BlackBox_Normative_Pipeline.md`
- `fZ_Reference/WD_天坛医院/Peak-Ages.md`
- `fZ_Reference/WD_天坛医院/README_Age_Censoring.md`

## Final Answer

**My recommendation is to use `x ≈ 3.3 years` only as a cautious communication proxy, not as a strict scientific conclusion.**

The strongest evidence-based statement is:

- **Yes**: this work supports using a Chinese normative ruler to detect AD-related brain deviation earlier, already at the **MCI stage**.
- **No**: the paper does **not** directly prove an exact early-detection lead time.
- **Practical launch wording**: if you need a number, the most defensible one from the existing materials is **about 3.3 years**, derived from the mean age gap between the **MCI** and **AD** cohorts.

**Why MCI and AD only for “x years”?** MCI is the only earlier stage on the same AD continuum in this study; the other disease groups (PD, CSVD, MS, NMOSD) are different conditions, so their age gaps are not “earlier AD” — the benefit there is differential diagnosis and triage.

**Further time-saving benefits** (all from the materials): **(1)** Chinese norms avoid misclassification and re-assessment when ENA norms are used for Chinese patients; **(2)** deviation scores outperform raw volumes and z-scores → more reliable detection with the same scan; **(3)** multi-ROI outperforms single-ROI → fewer false positives/negatives and less time on the wrong diagnostic path; **(4)** one framework for six diseases (AD, MCI, PD, CSVD, MS, NMOSD) → differential diagnosis in one assessment; **(5)** early sensitivity (entorhinal, thickness) → flags deviation earlier in the disease course. See the section **“Further benefits in saving time of disease detection”** above for evidence and wording.
