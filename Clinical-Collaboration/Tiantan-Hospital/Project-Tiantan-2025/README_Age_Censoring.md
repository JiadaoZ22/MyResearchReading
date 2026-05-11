# What Is “Age Censoring” in This Paper?

**Paper:** *Charting brain morphology in international healthy and neurological populations*  
**Folder:** `fZ_Reference/天坛医院/`

---

## Short answer

**Age censoring** here means **restricting the normative (healthy control) sample to a specific age range** when fitting the normative references, instead of using the full lifespan sample.

In this paper the main normative models use **ages about 4–85 years**. The **age-censoring** analysis uses only **18–70 years** (n = 21,205). So “age censoring” = **limiting the sample to 18–70 years** for a separate set of normative models and sensitivity analyses.

---

## Why the paper uses it

1. **Narrower confidence intervals (CIs)**  
   For the 18–70 subsample, the authors say *"the samples of these cases were relatively sufficient and had narrow fitting CIs"*. So the normative curves in that range are estimated with **tighter CIs** and are **more stable** than in the full age range (where young and very old ages have fewer subjects).

2. **Sensitivity / robustness check**  
   The paper compares:
   - Main findings: normative references fitted on the **full age range** (4–85 years), and  
   - Age-censored findings: normative references fitted only on **18–70 years**.  
   They report that *"the findings by the age censoring samples were consistent with the main findings"* on normative references, disease deviations, and clinical tasks (Supplementary Results 4, Extended Data Fig. 4).

3. **Better suited to many adult studies**  
   The GitHub README states that the **age-censoring normative models (18–70 years)** based on the Desikan–Killiany atlas *"have narrow fitting confidence intervals, and would be more robust for a majority of studies and clinical applications for adults"*. So if your application is mainly **adult (18–70)**, using these models can give more precise centile/deviation scores in that range.

---

## Where it appears

- **Main text:** Comparison of main findings with age censoring of 18–70 years; additional analyses on normative references using “age censoring samples (18–70 years)”.
- **Extended Data Fig. 4:** “Normative references by age censoring samples (aged 18–70 years)” — fitted curves, peak ages, and downstream clinical tasks using the age-censoring normative references (n = 21,205).
- **Zenodo / GitHub:** Age-censoring normative models (18–70 years) for the Desikan–Killiany atlas are provided alongside the full-age models.

---

## One-sentence summary

**In this paper, “age censoring” means fitting normative references using only healthy controls aged 18–70 years (instead of 4–85), giving narrower CIs and more robust norms for adult-focused studies and sensitivity analyses.**
