# WMH (White Matter Hyperintensities) Analysis

**Folder:** `fZ_Reference/WD_天坛医院/`  
**Cooperator WMH codebase:** `f0_Environment/Charting-Chinese-repo/WMH`

This note (1) answers whether FreeSurfer outputs WMH quantification and summarizes FreeSurfer-based options, and (2) provides a **detailed analysis of the cooperator’s WMH algorithms** in Charting-Chinese-repo, which are useful for **随访 (follow-up)** quantification.

---

## 1. What is WMH?

**WMH (White Matter Hyperintensities)** — also referred to as **white matter high signal** — are areas of increased signal intensity in the cerebral white matter on T2-weighted or FLAIR MRI. They are commonly associated with small-vessel disease, aging, hypertension, and cognitive decline. On **T1-weighted** MRI, the same pathology often appears as **hypointensities** (darker regions) rather than hyperintensities.

Quantifying WMH over time is important for **随访**: tracking progression/regression of small-vessel disease and treatment or risk-factor control.


### 1. How to evaulate the WMH clinically?
# 临床实践中脑白质高信号（WMH）判定标准的应用规范
本内容严格遵循**STRIVE（脑小血管病神经影像报告标准）国际共识**、《中国脑小血管病诊治指南2021》，贴合国内临床诊疗场景，核心原则是**以定性判定为基础、视觉分级为核心、鉴别诊断为前提、诊疗决策为目标**，兼顾可操作性、准确性与临床实用性，避免过度诊断与漏诊。

---

#### 一、临床应用前的必备前提：规范MRI扫描序列
WMH的准确判定完全依赖规范的影像序列，无合格序列的判读均无临床意义，临床常规扫描需满足以下要求：
1.  **核心必备序列（缺一不可）**
    - 首选**3D各向同性FLAIR序列**（3T场强最佳，1.5T可兼容），次选轴位2D FLAIR（层厚≤5mm，无层间距），是WMH判定的金标准，可清晰区分脑脊液与白质信号，避免部分容积效应。
    - 轴位T1WI、DWI序列：用于核心鉴别诊断，排除腔隙性梗死、急性缺血灶等WMH mimic病变。
2.  **补充可选序列**
    - T2WI、SWI（磁敏感加权成像）：辅助鉴别扩大的血管周围间隙（VR间隙）、脑微出血，全面评估脑小血管病（CSVD）总负荷。
3.  **禁忌**：仅用T1WI/T2WI、无FLAIR序列的头颅MRI，不可用于WMH的正式判定与报告。

#### 二、临床WMH判定的标准化操作流程
临床医生需严格遵循「**质量评估→排除mimic病变→定性判定→分级评估→综合解读**」的流程，不可直接跳过鉴别直接诊断WMH。

##### 步骤1：影像质量初筛
先排除无法判读的不合格影像：严重运动伪影、磁场不均匀伪影、层厚过厚/层间距过大、核心序列缺失的影像，需建议重新规范扫描。

##### 步骤2：严格排除WMH mimic病变（核心前提）
临床最常见的误诊是将其他白质信号异常判定为WMH，需通过多序列对比逐一排除以下病变，仅当无明确其他病因时，才可判定为CSVD相关WMH：
| 易混淆病变 | 与WMH的核心鉴别要点（多序列对比） |
|------------|--------------------------------------|
| 扩大的VR间隙 | 圆形/线性、沿血管走行分布，FLAIR/T2WI中心呈脑脊液样低信号，仅周边可有薄层高信号环；直径多＜2mm，无融合趋势 |
| 慢性腔隙性脑梗死 | T1WI呈脑脊液样明显低信号（WMH仅为等/轻度低信号，绝不会与脑脊液等信号），FLAIR呈「中心低信号+周边高信号环」，DWI急性期呈高信号 |
| 多发性硬化脱髓鞘斑块 | 多见于年轻患者，病灶垂直于侧脑室壁（Dawson手指征），可累及胼胝体、视神经、脊髓，符合「时间+空间多发」特点，与血管危险因素无明确关联 |
| 其他特异性白质病变 | 中毒/代谢性脑病、中枢神经系统血管炎、感染性脑病、单基因遗传性脑小血管病（如CADASIL）等，均有对应的病史、实验室检查或特征性影像表现，需结合临床排除 |

##### 步骤3：WMH的定性判定（符合STRIVE共识金标准）
同时满足以下所有条件，即可临床确诊WMH：
1.  FLAIR序列上呈脑白质区域的局灶/斑片状均匀高信号；
2.  T1WI序列上呈等信号或轻度低信号，信号强度显著高于脑脊液；
3.  已排除上述所有mimic病变及其他特异性病因；
4.  病灶直径＞2mm（＜2mm多为VR间隙，不纳入WMH判定）。

##### 步骤4：临床标准化分级评估（核心落地工具）
临床实践**不推荐常规使用科研级定量阈值（如信号强度3SD、自动化体积分割）**，首选操作简单、重复性好、与临床结局强相关的视觉分级法，其中**Fazekas分级为全球通用的一线方案**。
1.  **Fazekas分级（常规临床首选）**
    需分别对「脑室周围WMH」和「深部WMH」独立分级，报告需明确标注两个部位的分级，不可仅笼统描述「脑白质高信号」。
    | 分级 | 脑室周围WMH判定标准 | 深部WMH判定标准 | 临床意义 |
    |------|----------------------|------------------|----------|
    | 0级 | 无任何信号异常 | 无任何信号异常 | 正常白质 |
    | 1级（轻度） | 脑室角帽状高信号，或侧脑室旁铅笔样薄层高信号 | 散在点状高信号灶 | 老年人群（＞60岁）多见，多为生理性老化相关轻度改变，无症状者以危险因素管控为主 |
    | 2级（中度） | 侧脑室旁光滑的晕环状高信号，延伸至深部白质 | 点状病灶开始融合成斑片状 | 明确的CSVD相关病理改变，需全面筛查血管危险因素，启动干预 |
    | 3级（重度） | 不规则高信号，广泛融合延伸至深部白质 | 大片融合的高信号灶 | 严重CSVD损伤，与卒中、痴呆、步态障碍等不良结局强相关，需强化干预与密切随访 |

2.  **补充分级方案（特殊场景使用）**
    - ARWMC分级：需对脑内10个区域分别评分，适用于需要精准评估病灶分布的复杂病例（如认知障碍、步态异常患者）；
    - Scheltens分级：最细致的区域分级，仅用于科研或疑难病例的多学科会诊，不用于常规临床。

##### 步骤5：综合临床解读
不可孤立解读WMH分级，需结合患者年龄、症状、血管危险因素、其他CSVD影像标志物（腔梗、微出血、脑萎缩），完成最终的临床意义判定。

#### 三、不同临床场景下WMH判定标准的具体应用
WMH的判读与解读需贴合诊疗场景，核心是「分级结果指导临床决策」，而非单纯影像诊断。

##### 场景1：健康体检/无症状人群（全科、体检中心）
- 判读重点：严格区分正常与轻度WMH，避免过度诊断与恐慌，同时不漏诊中重度/早发性WMH。
- 临床应用：
  1.  年龄＞60岁，Fazekas 1级：无需特殊药物治疗，报告标注「符合年龄相关轻度脑白质改变」，健康宣教，嘱戒烟限酒、规律运动、管控血压/血糖/血脂等基础危险因素，无需常规复查MRI。
  2.  年龄＜50岁，Fazekas≥1级；或任何年龄Fazekas≥2级：报告标注「脑白质高信号，符合脑小血管病改变」，建议完善血管危险因素筛查（动态血压、糖化血红蛋白、血脂、同型半胱氨酸等），排查继发性病因，启动针对性干预，2-3年复查MRI评估进展。

##### 场景2：缺血性卒中/TIA患者（神经内科卒中单元/门诊）
- 判读重点：精准分级，结合其他CSVD标志物评估出血与复发风险，指导卒中二级预防。
- 临床应用：
  1.  溶栓/取栓患者：重度WMH（Fazekas 3级）是症状性颅内出血转化的独立高危因素，需术前充分告知风险，个体化评估溶栓获益与风险。
  2.  二级预防：中重度WMH患者，需强化血压管控（目标＜130/80mmHg，循证证实可延缓WMH进展）；重度WMH患者慎用长期双抗治疗，避免增加出血风险；WMH分级可作为卒中复发、功能预后不良的风险分层标志物。

##### 场景3：认知障碍/痴呆患者（认知门诊、老年科）
- 判读重点：评估WMH负荷与分布，区分血管性认知障碍、阿尔茨海默病与混合性痴呆。
- 临床应用：
  1.  Fazekas≥2级是血管性认知障碍（VCI）的核心影像诊断标准之一，WMH负荷与执行功能、处理速度下降程度显著相关。
  2.  中重度WMH合并认知障碍患者，需以血管危险因素强化管控为核心，联合认知训练，避免疾病快速进展；同时可作为痴呆风险分层的核心标志物，用于 preclinical 阶段的早期预警。

##### 场景4：老年步态异常/反复跌倒/慢性头晕患者（老年科、康复科）
- 判读重点：关注深部白质、幕下WMH的分级与分布，排除其他病因。
- 临床应用：
  1.  中重度WMH是老年人平衡障碍、步态不稳、反复跌倒、慢性非旋转性头晕的重要病因，可通过WMH分级明确病因，避免过度检查与误诊。
  2.  治疗以危险因素管控为基础，联合平衡康复训练，降低跌倒风险。

##### 场景5：老年患者围手术期评估（麻醉科、外科、老年科）
- 判读重点：术前快速分级，评估围手术期不良事件风险。
- 临床应用：
  1.  中重度WMH是老年患者术后谵妄、术后认知功能下降、围手术期心脑血管事件的独立高危因素。
  2.  术前检出中重度WMH，需优化围手术期管理：严格管控血压、避免术中低血压、减少镇静药物使用，制定个体化麻醉与术后监护方案。

##### 场景6：晚发性抑郁/精神行为异常患者（精神科、神经内科）
- 判读重点：排除其他病因，评估WMH负荷与症状的相关性。
- 临床应用：
  1.  中重度WMH是50岁以后晚发性抑郁（血管性抑郁）的重要病因，与抗抑郁药物疗效不佳、复发率高相关。
  2.  治疗需在抗抑郁治疗的基础上，联合血管危险因素管控，改善患者预后。

#### 四、临床应用的常见误区与规避策略
1.  **误区1：将所有白质高信号均诊断为WMH**
    规避：严格执行「先排除mimic病变，再诊断WMH」的流程，尤其注意区分扩大的VR间隙与点状WMH，无FLAIR序列不可出具WMH诊断报告。
2.  **误区2：过度解读轻度WMH，引发患者恐慌**
    规避：60岁以上人群Fazekas 1级WMH患病率超60%，属于年龄相关的轻度改变，不可描述为「脑梗前期」「脑供血不足」，报告需明确标注分级与临床意义，避免过度医疗。
3.  **误区3：忽视早发性/中重度WMH的干预价值**
    规避：50岁以下出现的WMH、任何年龄的Fazekas≥2级WMH，均需全面筛查病因与危险因素，不可笼统归为「老化」，错失早期干预窗口。
4.  **误区4：孤立解读WMH影像，脱离临床背景**
    规避：WMH诊断必须结合患者年龄、症状、病史与实验室检查，年轻患者无明确危险因素的重度WMH，需排查CADASIL等单基因病、血管炎、脱髓鞘疾病等继发性病因。
5.  **误区5：用科研定量阈值替代临床视觉分级**
    规避：常规临床不推荐使用信号强度阈值、自动化体积分割等科研工具，仅用于临床试验、精准进展评估等特殊场景，不可作为临床诊断依据。

#### 五、临床报告规范与随访原则
##### 1. MRI报告规范
临床报告需包含以下核心要素，避免模糊描述：
- 明确WMH的解剖分布（脑室周围、深部白质、幕下）；
- 明确标注Fazekas分级（脑室周围+深部白质分别标注）；
- 结合其他CSVD标志物，给出综合影像诊断（如「符合脑小血管病改变」）；
- 给出针对性的临床建议（如危险因素筛查、专科就诊、随访复查）。

##### 2. 随访原则
- 无症状轻度WMH：无需常规MRI复查，以危险因素年度监测为主；
- 中重度WMH、早发性WMH：每1-2年复查头颅MRI，评估病灶进展；
- 合并进展性症状（认知快速下降、步态恶化、反复卒中）：6-12个月复查，同时排查继发性病因。

---

## 2. Does Standard FreeSurfer `recon-all` Output WMH Quantification?

**No.** The standard FreeSurfer **`recon-all`** pipeline does **not** produce dedicated WMH quantification as part of its default workflow.

- **`recon-all`** is built for T1-weighted structural MRI and outputs:
  - Cortical surfaces, thickness, area
  - Subcortical segmentation (`aseg`)
  - Volumes and statistics in `stats/` (e.g. `aseg.stats`, `aparc.stats`)
- It does **not** include a WMH label or WMH volume in its standard outputs. WMH (or T1 hypointensities) are not explicitly segmented or reported.

**Caveat:** The presence of WMH can cause **systematic errors in FreeSurfer gray matter segmentations**. In cohorts with substantial WMH burden (e.g. cerebrovascular disease, aging), interpret cortical/subcortical metrics with caution or consider WMH-aware processing.

---

## 3. FreeSurfer-Based WMH Quantification: WMH-SynthSeg

FreeSurfer offers a separate tool for WMH (and T1 hypointensities) with **quantitative** outputs:

| Item | Detail |
|------|--------|
| **Tool** | **WMH-SynthSeg** (SynthSeg variant that segments anatomy + WMH) |
| **Availability** | **Development version** of FreeSurfer only (not in stable release) |
| **Input** | Any contrast and resolution (including T1); works on low-field / low-resolution data |
| **WMH label** | FreeSurfer label **77** |
| **Quantitative output** | Optional **`--csv_vols <file>`** → CSV with volumes for all segmented regions (including WMH) |
| **Output resolution** | 1 mm isotropic (regardless of input resolution) |
| **Typical runtime** | ~3 s on GPU, ~1 min on CPU per scan |

**Example command:**

```bash
mri_WMHsynthseg --i <input> --o <output> [--csv_vols <CSV file>] [--device cuda] [--threads -1]
```

- Use **`--csv_vols`** to get numeric volumes (including WMH) in a CSV file.
- Volumes are computed from **soft segmentations**, so voxel-count × voxel-volume may not match the CSV values exactly (same idea as `aseg.stats` vs counting voxels in `aseg.mgz`).

**Citation (if you use WMH-SynthSeg):**  
*Quantifying white matter hyperintensity and brain volumes in heterogeneous clinical and low-field portable MRI.* Laso P et al. Proceedings of ISBI 2024 (in press). [arXiv:2312.05119](http://arxiv.org/abs/2312.05119)

**Documentation:** [FreeSurfer Wiki – WMH-SynthSeg](https://surfer.nmr.mgh.harvard.edu/fswiki/WMH-SynthSeg)

---

## 4. Summary: FreeSurfer and WMH

| Question | Answer |
|----------|--------|
| Does **standard** `recon-all` output WMH quantification from T1? | **No** |
| Can I get WMH volumes in the FreeSurfer ecosystem? | **Yes**, via **WMH-SynthSeg** (FreeSurfer dev version), with `--csv_vols` for quantitative volumes |
| Best contrast for WMH in clinical practice? | T2 / FLAIR (hyperintensities); T1 shows them as hypointensities; WMH-SynthSeg supports T1-like inputs |

For normative / brain-chart pipelines (e.g. 天坛医院 CH models) that rely on **standard FreeSurfer** outputs: WMH is not a standard FreeSurfer measure; add WMH-SynthSeg separately if you need WMH quantification alongside DK/regional volumes.

---

## 5. Cooperator WMH Algorithms: Charting-Chinese-repo/WMH

The cooperator’s materials are under **`f0_Environment/Charting-Chinese-repo/WMH`**. That folder contains **two distinct pipelines**; only one is WMH-specific.

### 5.1 Overview of What Lives in `WMH/`

| Component | Purpose | WMH-specific? |
|-----------|---------|----------------|
| **WMH_codes/** | FLAIR-based WMH segmentation (nnU-Net + post-processing) | **Yes** |
| **end2end/** | Brain age & sex prediction (SFCN) | No (brain health charting) |
| **predictor/**, **hdbet/**, **loader/**, **bin/** | Used by end2end (age/sex pipeline) | No |
| **img_processing.py**, **predict_tumor.py** | Older multi-contrast tumor/lesion pipeline (T1C+T2+FLAIR, UNet, ResNet, radiomics) | No (tumor/IDH) |

The **WMH-specific** workflow is implemented in **`WMH_codes/`** (and the **freeseg** package inside it), plus the **nnUNet** subtree and the **WMH nnU-Net model** under `WMH_codes/model/`.

---

### 5.2 WMH Segmentation Pipeline (WMH_codes)

**Entry script:** `WMH_codes/predict.py` (or equivalent via the **freeseg** package; CLI can be exposed as e.g. `freeseg_WMH_predict` after installing the model).

#### 5.2.1 What the Algorithm Can Do

- **Input:** **FLAIR** images only (T2-FLAIR hyperintensities). One NIfTI (or path) per case; case names must be provided and unique.
- **Output:**
  - Binary WMH segmentation per case (NIfTI), in the same space as the preprocessed FLAIR.
  - Optional **GIF previews** (axial, side-by-side with FLAIR) for quick review.
- **Pipeline steps (in order):**
  1. **Preprocessing (optional):** N4 bias field correction (ANTs `N4BiasFieldCorrection`, 3D, shrink factor 2, convergence `[50×50×50,0.0]`, 2 levels). If skipped, inputs are only copied/renamed to the expected naming (`<case>_0000.nii.gz`).
  2. **Segmentation:** nnU-Net 3D full-resolution prediction:
     - **Trainer:** `nnUNetTrainerV2`
     - **Plans:** `nnUNetPlansv2.1`
     - **Task:** `Task002_FinalModel` (auto-detected if single task in model folder, or set via `--custom-task-name`)
     - **Fold:** `all` (single ensemble model)
     - **Checkpoint:** `model_best`
     - **Post-processing in nnU-Net:** disabled (`--disable_post_processing`); custom post-processing is applied instead.
  3. **Post-processing (in order):**
     - **3 mm spark removal:** Connected-component filtering that removes components with volume &lt; 3 mm³ (or &lt; 3 voxels for very thick-slice data). Implemented in `freeseg.analysis.image_ops.remove_3mm_sparks` (uses voxel spacing to convert 3 mm³ to a minimum voxel count).
     - **ROBEX masking:** Brain extraction is run on the **FLAIR** with **ROBEX** (`runROBEX.sh`); the resulting brain mask is used to mask the WMH segmentation so that only brain FOV is kept (removes neck and non-brain regions).
  4. **Preview:** Optional generation of axial GIFs (FLAIR + lesion overlay, side-by-side) for the final segmentations.

So in short: the algorithm **segments WMH on FLAIR**, **cleans small islands**, and **restricts the result to the brain mask** from ROBEX. It does **not** output volumes or tables by default; those would need to be computed from the output NIfTIs (e.g. voxel count × voxel size, or integration with a reporting pipeline).

#### 5.2.2 Model and Training

- **Model:** nnU-Net 3D full resolution, stored under  
  `WMH_codes/model/nnUNet/3d_fullres/Task002_FinalModel/nnUNetTrainerV2__nnUNetPlansv2.1/all/`  
  (training logs indicate multiple runs; the deployed checkpoint is `model_best`).
- **Installation:** A pre-trained model can be installed from a `.tar.gz` package via `WMH_codes/freeseg/main/install_model.py`. It expects a specific directory layout (nnUNet task folder, `plans.pkl`, `dataset_properties.pkl`, and the 3D/2D plans files). The installer rewrites paths in `model_best.model.pkl` so that the installed model points to the install location.
- **Environment:** `RESULTS_FOLDER` must point to the root of the installed model (the folder that contains the `nnUNet` subfolder).

#### 5.2.3 Dependencies and System Checks

- **nnU-Net:** Must be installed and on `PATH` (`nnUNet_train`, `nnUNet_predict`). The integrity check references `https://github.com/lchdl/nnUNet` (a fork).
- **ROBEX:** Required. Environment variable **`ROBEX_DIR`** must be set to the ROBEX installation directory; `runROBEX.sh` and the `ROBEX` binary must exist and be executable. Used only for brain masking in post-processing.
- **PyTorch:** Required (used by nnU-Net); GPU is optional but recommended (warning is printed if CUDA is not available).
- **ANTs:** `N4BiasFieldCorrection` is used for preprocessing; the integrity check does not enforce it in the current code (commented out), but the preprocessing step in `predict.py` calls it.
- **Python package:** The **freeseg** package (inside `WMH_codes`) is the “T2-FLAIR Hyperintensities Segmentation Toolbox” (version 0.7.3, author Chenghao Liu). It provides data I/O, parallelization, N4 shell call, ROBEX masking, 3 mm spark removal, and GIF preview utilities.

#### 5.2.4 Usage (Conceptual)

- **Input:** List of FLAIR NIfTI paths and corresponding case names.
- **Arguments:**  
  `-i` / `--input-images`, `-n` / `--case-names`, `-m` / `--trained-model` (root of installed model), `-o` / `--output-folder`, `-g` / `--gpu`.  
  Optional: `--skip-preprocessing`, `--custom-task-name`.
- **Output directories under `-o`:**
  - `001_Preprocessed_Images`: N4-corrected (or copied) FLAIR, named `<case>_0000.nii.gz`.
  - `002_Segmentations/001_raw`: Raw nnU-Net predictions.
  - `002_Segmentations/002_postproc_3mm`: After 3 mm spark removal.
  - `002_Segmentations/003_postproc_fov`: After ROBEX masking (final WMH segmentation).
  - `003_Previews`: GIFs (if generated).

Final segmentations are in **`002_Segmentations/003_postproc_fov`**.

#### 5.2.5 Relevance for 随访

- The pipeline produces **consistent, binary WMH segmentations** from FLAIR at each time point.
- For **follow-up (随访):** run the same pipeline on baseline and follow-up FLAIR; then compare or subtract segmentations (or compute volumes/location summaries) externally. The algorithm itself does not perform longitudinal registration or change detection; it only gives per-scan WMH masks. So 随访 use cases (e.g. change in WMH volume, new lesions) require an additional step (e.g. same-space resampling, or a dedicated longitudinal module) on top of these segmentations.

---

### 5.3 Other Components in the Same WMH Folder (Not WMH-Specific)

- **end2end:** Loads NIfTI/DICOM → preprocesses (loader) → **HD-BET** brain extraction → **ANTs** registration to MNI → **SFCN** brain age and sex prediction. Output is JSON (brain age, sex, etc.). No WMH segmentation.
- **img_processing.py:** Contains N4, FLIRT, BET, resampling, UNet-style normalization and cropping (128³), and radiomics/atlas-query helpers. Used by the older tumor pipeline (`predict_tumor.py`), not by the WMH_codes FLAIR→nnU-Net pipeline.
- **predict_tumor.py:** Uses HD-BET, a different nnU-Net checkpoint, and `img_processing` for tumor segmentation and IDH-related prediction; it is **not** the WMH pipeline.

---

## 6. Summary: Cooperator WMH Algorithms

| Aspect | Detail |
|--------|--------|
| **What it does** | Segments WMH from **FLAIR** using nnU-Net 3D full-res, then removes small components (&lt; 3 mm³) and masks to ROBEX brain FOV. |
| **Input** | FLAIR NIfTI per case. |
| **Output** | Binary WMH segmentation NIfTI per case (+ optional GIFs). No built-in volume table or longitudinal analysis. |
| **Model** | nnU-Net, Task002_FinalModel, nnUNetTrainerV2, nnUNetPlansv2.1, fold `all`, `model_best`. |
| **Key dependencies** | nnU-Net (lchdl fork), ROBEX, PyTorch; N4 for preprocessing. |
| **随访** | Suitable as the **segmentation backbone** for 随访; longitudinal comparison or volume reporting must be implemented separately (e.g. same-space resampling + volume/count metrics). |

For **FreeSurfer-centric** workflows (e.g. CH brain charts), adding **WMH-SynthSeg** gives T1-based WMH volumes (label 77, `--csv_vols`). For **FLAIR-based** WMH and integration with the cooperator’s Charting materials, the **WMH_codes** pipeline in `f0_Environment/Charting-Chinese-repo/WMH` is the relevant algorithm set; the end2end and tumor scripts in the same folder serve different (brain age/sex and tumor) purposes.
