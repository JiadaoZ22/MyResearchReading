# What Does “Euler Number” Mean in This Paper?

**Paper:** *Charting brain morphology in international healthy and neurological populations*  
**Folder:** `fZ_Reference/天坛医院/`

---

## 1. Definition in the Paper

In this study, **Euler number** is used as **an index of image segmentation quality** when processing 3D T1-weighted MRI with **FreeSurfer (FS)**.

- **Quote (Methods):**  
  *"Brain segmentations were visually inspected and edited (if necessary) by Z. Zhuo and then assessed by the **Euler number** (an index to represent **image segmentation quality using FS**; outliers were defined as two standardized deviations less than the median Euler number in all samples across sites)."*

- **Quality control:**  
  Scans that passed both **visual** and **automatic** quality checks were included. The automatic check uses the **Euler number** with a **cutoff value of −177.5** (see Extended Data Fig. 1).

So in this paper, **Euler number = a FreeSurfer-derived QC metric for segmentation quality**.

---

## 2. What It Represents (Technical Background)

- In **topology**, the **Euler characteristic** (often denoted χ) of a surface is a topological invariant. For a triangular mesh it can be computed as **χ = V − E + F** (vertices − edges + faces). For a **sphere** (no holes, no handles), χ = 2.

- In **FreeSurfer**, the cortical surface is represented as a mesh. The **Euler number** reported by FS is related to this characteristic and to **topological defects** in the surface (e.g. holes, handles, or other errors introduced during segmentation).

- **More negative Euler numbers** (e.g. much lower than 0, or below the cutoff −177.5) generally indicate **worse topology** — i.e. more segmentation/topology errors (handles, holes, or inconsistent mesh). **Values closer to the expected range** (e.g. near 2 for a sphere-like cortex, or above the study’s cutoff) indicate **better segmentation quality**.

So in this paper: **Euler number is a proxy for “how topologically correct and reliable the FreeSurfer segmentation is.”**

---

## 3. How the Paper Uses It

| Use | Description |
|-----|-------------|
| **Inclusion QC** | Only scans passing automatic QC using Euler number (cutoff **−177.5**) were included (Extended Data Fig. 1). |
| **Outlier definition** | Outliers were defined as scans with Euler number **two standardized deviations below the median** Euler number (across all samples/sites). |
| **Visualization** | Extended Data Fig. 1c shows the distribution of Euler number across **age**, **sex**, and **diagnostic group** (HC and diseases; n = 27,993), with the **cutoff −177.5** drawn as a horizontal line. |

So: **low (very negative) Euler number → likely poor segmentation → excluded or flagged as outlier.**

---

## 4. Summary in One Sentence

**In this paper, “Euler number” is a FreeSurfer-based metric of cortical segmentation quality (topology); the study uses a cutoff of −177.5 for automatic QC and defines outliers as two SD below the median Euler number, so that only scans with acceptable segmentation quality are included in the normative and disease analyses.**

---

## 5. Reference in the Paper

The use of Euler number for QC follows the approach of **reference 10** (ENA references / prior normative work) cited in the same Methods paragraph.
