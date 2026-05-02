# Can I Use the Normative Pipeline as a Ready-to-Use Black Box? (CH vs ENA)

**Paper:** *Charting brain morphology in international healthy and neurological populations*  
**Folder:** `fZ_Reference/天坛医院/`

This note answers: **Are normative data/statistics available for both CH and ENA so you can do the same normalization and percentile-deviation score computation as the paper, and can you treat the pipeline as a black box (fit in new data → get output)?**

---

## 1. Short Answer

| Population | Normative data/models available? | Black-box ready from this paper’s repo? |
|------------|----------------------------------|----------------------------------------|
| **CH (Chinese)** | **Yes** — Fitted models (GAMLSS, HBR) on Zenodo + scripts on GitHub | **Yes** — Use repo + Zenodo models; input new data → get centile/deviation scores. |
| **ENA (European/North American)** | **Yes** — From **Bethlehem et al. (ref. 10)** / **brainchart.io** | **No** — ENA is **not** in this paper’s GitHub/Zenodo. Use **brainchart.io** (or Bethlehem et al. pipeline) for ENA. |

So: **CH pipeline from this paper can be used as a black box**; **ENA** uses a **different**, publicly available resource (brainchart.io), not this repo.

---

## 2. Chinese (CH) Population — Black Box Ready

**What the paper’s repo provides:**

- **Normative models (no raw 24,061 subject data):** Fitted GAMLSS (and HBR) models for global and regional structural measures (Desikan–Killiany, HCP-MMP, DU15NET, Brainnetome, age-censoring). Hosted on **Zenodo** (see `f0_Environment/Charting-Chinese-brain-health-and-neurological-disorders-across-lifespan/README_ZENODO_DOWNLOADS.md`).
- **Scripts:** R scripts to **apply** these models to new data and compute deviation (centile) scores, e.g.:
  - **Disease-application-normative-model.R** — batch: `Clinical_vars.csv` + `MR_measures.xlsx` → deviation scores.
  - **Individual-application-normative-model.R** — single subject → deviation scores.
  - **Individualized-brain-health-report.Rmd** — report including deviation scores.

**What you need:**

1. **Get the repo** (Scripts, Source-codes, Datasets layout) and **download Zenodo models** into `Models/` (see README_ZENODO_DOWNLOADS and `download_zenodo_models.sh`).
2. **Input format:** Same as “Dataset-norms” / “Dataset-diseases” / “Dataset-individual”:
   - **Clinical_vars.csv** — at least **age**, **sex**, and **site** (if your data have site; required by the model).
   - **MR_measures.xlsx** — FreeSurfer-derived structural measures (global and regional volumes, thickness, area as in the paper). Variable names must match what the fitted models expect (Desikan–Killiany or other atlases you use).
3. **Point scripts to your paths:** Set `savepath1` (or `feature_path0`) to the folder where you extracted the **DK** (or other) models, e.g. `**/Models/GAMLSS-DK`, and set `clinical_datapath`, `MR_datapath`, `savepath` to your input/output paths.

**Output:** Deviation (centile) scores per measure per subject — same normalization and percentile-deviation computation as in the paper. You do **not** need the original 24,061 HC data; the **fitted models** contain the normative statistics.

**Caveats (so it’s “black box” only if inputs match):**

- **FreeSurfer pipeline and atlas:** Measures must come from the same pipeline/parcellation as the paper (FreeSurfer, Desikan–Killiany or the same extended atlases). Different software or atlases → different variables → not directly compatible.
- **Site and sex:** The CH models include **site** (random effect) and **sex**; your CSV must have compatible site/sex coding (see Individual-application note about “case1 and case2” for factor levels).
- **Age range:** CH models are fitted for about 4–85 years (or 18–70 for age-censoring). Extrapolation outside that range is not validated.

---

## 3. ENA (European/North American) Population — Different Resource

**What the paper uses for ENA:**

- The paper compares CH to **“ENA normative references”** from **ref. 10**: **Bethlehem, R. A. I. et al. Brain charts for the human lifespan. Nature 604, 525–533 (2022)** (101,457 healthy individuals, ENA-focused).
- ENA references are **not** part of the 天坛医院 GitHub or Zenodo. They are **publicly available** via:
  - **brainchart.io** — [https://www.brainchart.io/](https://www.brainchart.io/) — interactive resource and normative standards for centile/deviation-type scoring.
  - Bethlehem et al. pipeline / tools (e.g. normative modeling, centile calculators) as in their paper and associated code.

**So for ENA:**

- **Normative data/statistics:** **Yes** — available (Bethlehem et al. / brainchart.io).
- **Same type of normalization and percentile-deviation:** **Yes** — brainchart.io (and Bethlehem et al.) provide centile scores and normative modeling.
- **Black box from *this* paper’s repo:** **No** — this repo only provides **CH** models and scripts. For ENA you use **brainchart.io** or the Bethlehem et al. pipeline, not the 天坛医院 repo.

---

## 4. Summary: “Ready-to-Use Black Box” by Population

| Question | CH (Chinese) | ENA |
|----------|--------------|-----|
| Are normative data/statistics available? | Yes (fitted models on Zenodo) | Yes (Bethlehem et al. / brainchart.io) |
| Can I do the same normalization & percentile-deviation as the paper? | Yes, using this repo + Zenodo | Yes, using brainchart.io / Bethlehem et al. |
| Can I treat *this* repo as black box: new data in → scores out? | **Yes** (with matching FreeSurfer + format) | **No** — use brainchart.io / Bethlehem et al. |
| Where to get models / tools? | GitHub + Zenodo (see README_ZENODO_DOWNLOADS) | brainchart.io; Bethlehem et al. Nature 2022 |

**Bottom line:** For **CH**, the pipeline (repo + Zenodo models) is ready to use as a black box: you provide new data in the expected format (Clinical_vars + MR_measures from FreeSurfer) and run the application scripts to get the same normalization and percentile-deviation scores as in the paper. For **ENA**, the same *type* of analysis is available, but from **Bethlehem et al. / brainchart.io**, not from this paper’s repository.
