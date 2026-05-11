# MyResearchReading — Organization Guide

This repository stores papers, notes, code snippets, datasets, and auxiliary materials for research reading. To keep hundreds of items navigable, everything follows a single, strict folder taxonomy.

---

## 1. Taxonomy (4-Level Folder Hierarchy)

The original idea was a 6-level chain:

```
[Area] → [Topic] → [Tech Stack] → [Development History] → [Work] → [Materials]
```

In practice, a rigid 6-level tree creates too many empty folders and long paths. We therefore **collapse** the middle two dimensions into **naming conventions** and **material subfolders**, keeping the hierarchy flat but semantically rich:

```
Area / Topic / Work / Materials
```

| Level | Meaning | How to Name | Example |
|-------|---------|-------------|---------|
| **1. Area** | Broad domain or strategic scope | PascalCase, noun phrase | `Medical-AI`, `Foundation-Models`, `Neuroimaging-Methods` |
| **2. Topic** | Research question or sub-domain | PascalCase, specific | `Alzheimer-Detection`, `Brain-Parcellation`, `Vision-Language` |
| **3. Work** | A concrete unit of study (paper, model series, experiment, or project) | `TechStack_WorkName_Version` or `WorkName` | `MoE_DeepSeek-V4`, `VolumeAnalysis_20250912`, `Qwen-Series` |
| **4. Materials** | Actual files grouped by **role**, not by format only | Fixed subfolder names (see below) | `paper/`, `note/`, `code/`, `data/`, `asset/`, `meta/` |

### Encoding the Missing Two Dimensions

- **Tech Stack** → prefix or suffix in the **Work** name (e.g., `CNN_`, `Transformer_`, `SAM-`, `MoE-`). If a Work spans many stacks, omit the prefix and add a `meta/tech-stack.md` tag file instead.
- **Development History** → version suffix in the **Work** name (e.g., `_20250912`, `_v2`) or a `meta/dev-history.md` note. Backups and obsolete iterations go into `Work/_archive/`.

---

## 2. Material Subfolders (Inside Every Work)

Every Work folder **must** contain at least one of the following subfolders. If a Work has only a single PDF, still place it under `paper/`.

| Subfolder | Content |
|-----------|---------|
| `paper/` | Main PDF, supplementary PDFs, preprints, patents |
| `note/` | Markdown reading notes, study summaries, annotated slides |
| `code/` | Scripts, notebooks, mini-implementations, config files |
| `data/` | CSVs, extracted tables, small datasets, analysis outputs |
| `asset/` | Images, diagrams, screenshots, figures referenced by notes |
| `meta/` | Bibliographic info, dev-history, prompts, comparison tables, TODOs |

**Rules for Materials**
1. No file lives directly inside `Work/` — it must be in one of the six subfolders above.
2. If a Work has only one item, create the matching single subfolder (e.g., just `paper/`).
3. Images that belong to a specific note go into `asset/`; do not scatter them at the Topic or Area level.
4. Large binary assets (>100 MB) should stay in external storage; keep only a `meta/download-link.md` here.

---

## 3. Special Folders

| Folder | Purpose |
|--------|---------|
| `Area/_Uncategorized/` | Temporary landing zone for items you have not classified yet. Review and move them out monthly. |
| `Work/_archive/` | Obsolete iterations, backups, and deprecated experiments. Keeps active Work folders clean. |
| `_Inbox/` | (Optional) at repository root for quick drag-and-drop before sorting. |

---

## 4. Naming Conventions

- **Folders**: `Pascal-Case-With-Hyphens` (e.g., `Brain-Parcellation`, `LLM-Finetuning`).
- **Files**: Keep the original paper title if it is descriptive; otherwise use `YYYY-MM-DD_Short-Description.ext`.
- **Markdown notes**: `StudyNote_<Author><Year>_<Keyword>.md` or `Note_<Keyword>.md`.
- **Avoid** spaces in folder names; use hyphens. (Existing files may keep spaces, but new ones should not.)

---

## 5. Example Layout

```
Foundation-Models/
  Vision-Language/
    Qwen-Series/
      paper/
        Qwen-VL.pdf
        Qwen2-VL.pdf
        Qwen2.5-VL-Technical-Report.pdf
        Qwen3-VL-Technical-Report.pdf
      note/
        SeriesNote.md
      meta/
        QwVL_developmentHistory.md
        comparison-table.md
      asset/
        arch-diagram.png

Medical-AI/
  Alzheimer-Detection/
    VolumeAnalysis_20250912/
      code/
        extract_brain_roi_data.py
      data/
        BrainROIsRelVol_GPT5.csv
        BrainROIsRelVol_GPT5_note.txt
      note/
        methodology.md
      meta/
        dev-history.md
    Expert-Consensus_NIA-AA/
      paper/
        NIA-AA-Diagnostic-Guidelines.pdf
    NCA-EVA-Ensemble/
      paper/
        NCA-EVA.pdf
      note/
        NCA-EVA_Extracted.txt

Neuroimaging-Methods/
  Brain-Atlas/
    FreeSurfer/
      paper/
        Desikan-2006.pdf
        Fischl-2004.pdf
      note/
        Automatically_Parcellating_the_Human_Cerebral_Cortex_Summary.md
      asset/
        brain_lateral_view.jpg
        Gyri-and-Sulci.png
```

---

## 6. Maintenance Checklist

- [ ] When adding a new paper, decide Area → Topic → Work in ≤ 30 seconds. If stuck, use `_Uncategorized/`.
- [ ] When a Work spawns a new experiment or revision, create a new Work folder with a version suffix and link back in `meta/dev-history.md`.
- [ ] Once a month, review `_Uncategorized/` and `_archive/` folders.
- [ ] Keep `README.md` updated if the taxonomy itself evolves.

---

*Last updated: 2026-05-11*
