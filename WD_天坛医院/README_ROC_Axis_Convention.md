# ROC Curve X-Axis Convention in This Paper

**Paper:** *Charting brain morphology in international healthy and neurological populations*  
**Folder:** `fZ_Reference/天坛医院/`

---

## Recevier Operating Curve
- Y axis => TPR
- x axis => FPR

## What the figure does

In **Task 1** (disease-specific classification model performances and DPS estimations), the ROC curves are drawn with:

- **Y-axis:** Sensitivity/Recall/TPR (0 to 1, bottom to top) — same as usual.
- **X-axis:** **Specificity**/TNR, with ticks from **1.00 (left) to 0.00 (right)**.

So the x-axis runs from 1 to 0 (left to right), not 0 to 1.

---

## Is that wrong?

**No.** It is a valid alternative convention.

- **Common convention:** X-axis = **1 − Specificity** (False Positive Rate), from 0 (left) to 1 (right).
- **This paper:** X-axis = **Specificity**, from 1 (left) to 0 (right).

Because **Specificity 1→0** (left to right) is the same scale as **(1 − Specificity) 0→1** (left to right), the **curve shape and AUC are unchanged**. Only the axis label and direction differ.

---

## Why use Specificity 1→0?

- Keeps the axis labeled as “Specificity” so “high specificity” is on the left.
- “Good” performance (high sensitivity and high specificity) can sit toward the top-left.
- Some fields and journals use this layout.

---

## One-sentence summary

**The ROC plots in this paper use an x-axis of Specificity from 1 to 0 (left to right) instead of 1 − Specificity from 0 to 1; the curve and AUC are the same, so the figure is not drawn wrongly.**
