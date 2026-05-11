# Open-source agent foundations for multi-modality medical imaging platforms

**Document version**: 4.1  
**Date**: April 10, 2026  
**Purpose**: Compare recent open-source **agent orchestration** and **medical imaging agent** stacks for a platform spanning DR/CT/MR/PET (and future ultrasound), from hospital workflows through analysis, reporting, and longitudinal follow-up. This note is for **architecture and R&D planning**; clinical deployment requires separate regulatory, security, and clinical governance review.

**Important disclaimers**

- No framework delivers a **regulated, end-to-end clinical product** out of the box. “Treatment suggestion” and patient-facing advice must be framed as **decision support** with **mandatory clinician oversight**, audit trails, and indication-specific validation.
- **Verify every third-party claim** (stars, “hospital deployments,” feature lists) at the source repository or paper before procurement or public statements. Earlier versions of this file mixed **verified** references with **illustrative** examples; v4.0 prioritizes **checkable** links and explicit uncertainty where evidence is thin.

---

## Executive summary

For a **professional, upgradable foundation**:

1. **Separate concerns**: use a **clinical imaging / model layer** (e.g. MONAI ecosystem, PACS/DICOM services, modality-specific models) and an **agent orchestration layer** (workflow state, tools, policies, observability). Connect them with **stable interfaces** (MCP tool servers, FHIR/DICOM gateways, internal APIs)—so new modalities (e.g. ultrasound) are mostly **new tools + graphs**, not a rewrite of the core runtime.
2. **Orchestration choice**:
   - **LangGraph + LangChain ecosystem** (plus **LangSmith** where you need traces/evals): strong fit for **explicit graphs**, **human-in-the-loop** steps, enterprise patterns, and **documented MCP integration** ([LangChain MCP docs](https://docs.langchain.com/oss/python/langchain/mcp), [Agent Server MCP](https://docs.langchain.com/langgraph-platform/server-mcp), [langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters)).
   - **OpenClaw**: strong fit for **local-first**, multi-channel personal/ops-style agents, large skill ecosystem, and rapid glue code; **not** radiology-specific—medical coverage comes from **your tools + policies**. Operators in some jurisdictions have raised **security and data-handling** concerns for certain deployments—treat as a **deployment risk** to assess against your hospital IT and national guidance.
3. **Imaging-specific agent research**: **MedOpenClaw** ([arXiv:2603.24649](https://arxiv.org/abs/2603.24649)) targets **auditable VLM agents** operating in real viewers (e.g. 3D Slicer) on **full studies**—excellent reference for **imaging agent design and benchmarking**, not a substitute for a full hospital information stack.
4. **“Hermes” naming collision**: **Nous Research Hermes-Agent** is a **general autonomous agent** ([GitHub: NousResearch/Hermes-Agent](https://github.com/NousResearch/Hermes-Agent), [site](https://hermes-agent.nousresearch.com/)). A **different** **HERMES** in recent literature is a **physiological sensing / edge AI** stack for closed-loop healthcare scenarios ([ADS record](https://ui.adsabs.harvard.edu/abs/2026arXiv260112610Y/abstract))—relevant if you later blend **wearables + imaging + interventions**, not the same as LLM agent orchestration.

**Practical starting point**: **LangGraph (or similar explicit orchestration) + MCP-wrapped imaging/clinical tools + MONAI (and/or your existing pipelines)**; optionally prototype personal-assistant-style UX with **OpenClaw** if it passes your security review. Add **MedOpenClaw / MedFlow-Bench** as a **methodology** for evaluating imaging agents on full volumes.

---

## Design principle: agent focuses on tools and resources, not on owning PACS/DB

Your system can **read** from PACS, VNA, FHIR servers, RIS, or internal databases, but the **agent runtime** should treat that as **calling well-defined tools** (or MCP servers), not as embedding connectivity or business rules inside the model.

| Concern | Where it lives | What the agent does |
|--------|----------------|---------------------|
| DICOMweb/QIDO-RS/WADO, C-FIND/C-MOVE, de-ID, caching, bandwidth | **Tool / service layer** (hospital-approved components) | Chooses *which* tool and *with which* study/patient identifiers (within policy). |
| SQL, document stores, object storage | **Same**: dedicated connectors with RBAC | Issues structured requests via tool schemas; never raw ad hoc DB access from the LLM. |
| Segmentation, registration, quantification, report templates | **Tools** wrapping MONAI, FreeSurfer, viewers, etc. | Chains tool outputs into reasoning and user-facing explanations. |
| Consent, retention, audit, break-glass | **Gateway + policy engine** around tools | Agent only sees **allowed** tool surfaces. |

**Why this split helps**

- **Security and compliance**: credentials, PHI boundaries, and logging sit in **one** integration layer you can review and pen-test.
- **Upgradability**: swap PACS vendor or add ultrasound by adding or changing **tools**, not by retraining or rewriting the orchestration core.
- **Testability**: mock tools for CI; replay recorded tool responses for regression.
- **Honest scope**: the agent’s job is **which resource to use, in what order, and how to combine results**—not to be the database or the DICOM stack.

The orchestration framework (LangGraph, OpenClaw, etc.) is then evaluated mainly on **tool calling, state, memory, HITL, and observability**—aligned with “accessing tools and resources only” at the agent boundary.

---

## Evaluation criteria (aligned with your scope)

| Criterion | Why it matters for you |
|-----------|-------------------------|
| **Lifecycle coverage** | Registration, scheduling, protocol guidance, acquisition QA, post-processing, structured reporting, follow-up, and research workflows are **different subgraphs**—the runtime should compose them without one monolith. |
| **Multi-modality & upgrade path** | DR/CT/MR/PET/US imply **different DICOM objects, priors, and models**—prefer **tool-per-modality** (MCP servers) and shared orchestration. |
| **Interoperability** | DICOMweb/PACS, RIS/HIS/FHIR, lab systems, and staff identity (RBAC) should sit behind **tools**, not inside the LLM. |
| **Safety & governance** | Immutable audit logs, approval gates for high-risk actions, sandboxed tool execution, content security (prompt injection), and **clear “advisory only”** UX for patients. |
| **Observability & evaluation** | Trace every tool call; regression-test on **your** cases; separate **offline eval** (e.g. imaging benchmarks) from **online** clinical pilots. |
| **Open-source viability** | License, maintenance, community, and whether the project is **research code** vs **production-oriented**. |

---

## Part A — General-purpose agent runtimes (orchestration layer)

| Framework | What it is | Pros | Cons / risks | Fit for your platform |
|-----------|------------|------|--------------|------------------------|
| **OpenClaw** | Personal/ops-oriented open agent stack; multi-channel; skills ecosystem; local execution emphasis ([repo](https://github.com/openclaw/openclaw)). | Very active project; **skill/plugin** mindset matches incremental modality tools; good for **fast integration prototypes** if security posture is acceptable. | **Not** medically specialized; compliance/audit features are **your responsibility**; **policy and security scrutiny** in some regions; hype can outpace clinical validation—treat skills as **untrusted code**. | **Prototype / auxiliary** channel (e.g. technologist copilot) if approved; pair with strict tool allowlists. |
| **LangGraph + LangChain** | Graph-based state machines and agent patterns; broad enterprise adoption; MCP adapters and server endpoints documented. | **Explicit workflows** (registration → imaging → follow-up) map naturally to graphs; **HITL** checkpoints; mature patterns for RAG over guidelines; MCP: [adapters](https://github.com/langchain-ai/langchain-mcp-adapters), [docs](https://docs.langchain.com/oss/python/langchain/mcp). | Heavier engineering than a single “assistant”; you still build **all clinical connectors**; cost/complexity of hosted vs self-hosted ops. | **Primary recommendation** for a **hospital-grade orchestration core** you control end-to-end. |
| **Hermes-Agent (Nous)** | General self-hosted agent emphasizing memory, skills, and automation ([repo](https://github.com/NousResearch/Hermes-Agent)). | Interesting reference for **memory + skill** ergonomics; may inspire internal patterns. | **No** clinical modules; overlapping goals with OpenClaw/LangGraph—**pick one orchestration spine** to avoid fragmentation. | **Optional** research or **secondary** experiment; not required for a imaging-first hospital platform. |
| **Others (short list)** | **Microsoft AutoGen / Semantic Kernel**, **Google ADK**, **CrewAI**, **Temporal + LLM**, etc. | Useful if you already standardize on a cloud or .NET/Java stack. | Each needs the same **clinical wrapper** work; compare on **team skills** and **existing infra**. | Choose based on **org stack**, not blog rankings. |

---

## Part B — Medical imaging–oriented agents & tooling (imaging layer)

| Framework / asset | What it is | Pros | Cons | Fit |
|-------------------|------------|------|------|-----|
| **MONAI + MONAI Deploy** | PyTorch medical imaging library and deployment packaging ([MONAI](https://github.com/Project-MONAI/MONAI), [Deploy](https://project-monai.github.io/deploy.html)). | **Strong** for training/inference pipelines, standardized components, and clinical-style packaging; broad modality coverage in **research and productized paths** depending on your models. | **Not** a full agent orchestrator; agent logic lives **above** MONAI. | **Core imaging foundation** for many teams. |
| **VLM-Radiology-Agent-Framework (MONAI)** | Radiology-oriented VLM / agent framework direction from MONAI org ([repo](https://github.com/Project-MONAI/VLM-Radiology-Agent-Framework)). | Grounded in **radiology VLMs** and agentic patterns relevant to reporting and interaction. | Research/evolving; check repo status and model licenses for your use. | **Reference implementation** adjacent to MONAI. |
| **MedOpenClaw** | Research runtime + **MedFlow-Bench** for **full-study** imaging agent evaluation in tools like 3D Slicer ([arXiv:2603.24649](https://arxiv.org/abs/2603.24649)). | Directly addresses **3D navigation, tool use, and auditability**—key for CT/MR/PET workflows; paper discusses **failure modes** when VLMs get “too many” tools. | Academic **evaluation stack**, not a turnkey hospital platform; integration effort required. | **Methodology + benchmark** for building/evaluating **imaging agents**. |
| **OpenClaw-Medical-Skills** | Community skill collection positioned for medical/bio workflows ([repo](https://github.com/MedClaw-Org/OpenClaw-Medical-Skills)). | Large curated surface for **ideas and glue**; can accelerate prototyping. | **Quality and compliance vary**; must be **reviewed** like any third-party code; not a substitute for validated clinical software. | **Idea mine / prototype accelerator** only with governance. |
| **MMedAgent** | Multimodal medical tool-using agent (research; [paper arXiv:2407.02483](https://arxiv.org/abs/2407.02483), [code](https://github.com/Wangyixinxin/MMedAgent)). | Good reference for **tool routing** across imaging tasks. | Research scope; update paths depend on maintainers. | **Research baseline** for tool orchestration patterns. |

---

## Part C — “Hermes” disambiguation (do not merge)

| Name | Domain | Relevance to you |
|------|--------|------------------|
| **Hermes-Agent (Nous Research)** | LLM agents, memory, general automation | Optional orchestration UX; see Part A. |
| **HERMES (physiological / edge healthcare)** | Wearables, streaming inference, closed-loop interventions ([literature record](https://ui.adsabs.harvard.edu/abs/2026arXiv260112610Y/abstract)) | Relevant if the roadmap adds **continuous monitoring + device** loops alongside imaging; **orthogonal** to PACS-centric agents unless you **fuse** streams later. |

---

## Full lifecycle coverage — how to implement it (realistically)

No single open-source repo spans **HIS registration → scanner → PACS → reporting → therapy planning → longitudinal care** with production guarantees. A **defensible** pattern:

1. **Graph/steps per stage**: small state machines (e.g. LangGraph) for **scheduling**, **protocol assistant**, **QC**, **segmentation/quant**, **report draft**, **peer review queue**, **follow-up tracker**.
2. **Shared “patient context” object**: IDs, encounter IDs, study UIDs, consents, and **retrieved artifacts** (summaries, priors)—never raw prompts alone.
3. **Tool boundaries**: DICOM retrieve, segmentation service, dose report, EHR FHIR read, guideline RAG—each **MCP or microservice** with **schema/versioning**.
4. **Risk-tiered autonomy**: read-only tools widely allowed; **order entry**, **protocol changes**, or **patient messaging** behind **roles + confirmations**.
5. **Evaluation**: imaging agents on **MedFlow-Bench-style** tasks where applicable; language agents on **your** de-identified charts with clinician scoring.

---

## Verified or representative open-source samples (check before reuse)

| Resource | URL | Notes |
|----------|-----|--------|
| LangChain MCP adapters | https://github.com/langchain-ai/langchain-mcp-adapters | Official bridge from MCP servers to LangChain tools. |
| LangGraph / LangChain MCP docs | https://docs.langchain.com/oss/python/langchain/mcp | Integration patterns and caveats. |
| LangGraph Agent Server MCP endpoint | https://docs.langchain.com/langgraph-platform/server-mcp | Exposing graphs as MCP (platform-oriented). |
| Clinic-oriented LangGraph example (small) | https://github.com/co-dev0909/medical-ai-assistant | Illustrative **demo-scale** assistant; not clinical-grade. |
| MONAI VLM radiology agent direction | https://github.com/Project-MONAI/VLM-Radiology-Agent-Framework | Radiology VLM / agent research codebase. |
| MedOpenClaw paper + (if released) code from authors | https://arxiv.org/abs/2603.24649 | Follow paper “Code, Data and Media” for **authoritative** artifacts. |
| OpenClaw Medical Skills (community) | https://github.com/MedClaw-Org/OpenClaw-Medical-Skills | **Review** each skill; governance required. |
| MMedAgent | https://github.com/Wangyixinxin/MMedAgent | Research reference for multimodal medical tool use. |
| Multi-agent medical assistant (example) | https://github.com/souvikmajumder26/Multi-Agent-Medical-Assistant | Another **educational** multi-agent chatbot pattern. |
| HEARTS (time series health reasoning benchmark) | https://github.com/yang-ai-lab/HEARTS | **Benchmark** for health time-series reasoning—not a deployed monitoring agent. |

**Removed / not verified**: example entries such as `medaiihf/openclaw-hospital` returned **404** at revision time; **do not cite** unverified “hospital deployment” lists without primary sources.

---

## Recommended foundation (concise)

| Layer | Suggested direction |
|-------|---------------------|
| **Orchestration** | **LangGraph** (or org-standard equivalent) + **MCP** for tools; **LangSmith** (or your trace store) for audits/evals. |
| **Imaging AI** | **MONAI** (+ your existing pipelines such as FreeSurfer/FSL where relevant) wrapped as **services/MCP**. |
| **Imaging agent R&D** | Study **MedOpenClaw** + **MedFlow-Bench** for **full-volume** agent design; use **VLM-Radiology-Agent-Framework** as adjacent MONAI work. |
| **Optional UX / ops agent** | **OpenClaw** only after **security review** and with **strict** tool policies. |
| **Ultrasound later** | Add **US-specific DICOM tools** + models (MONAI model zoo and custom weights) as **new MCP servers**; orchestration graph unchanged in principle. |

---

## Implementation roadmap (high level)

1. **0–6 weeks**: One **modality** (e.g. CT) vertical slice—PACS retrieve → segmentation/quant service → structured draft → radiologist review UI; full **trace + audit**; no autonomous orders.
2. **2–4 months**: Second modality; shared patient context; guideline RAG with **citation** to internal protocol PDFs; expand **HITL** rules.
3. **6–12 months**: Longitudinal subgraph (prior comparison, trend language **as decision support**); formal **security, privacy, and regulatory** path for your jurisdiction; ultrasound MCP servers if models ready.

---

## Change log (this file)

- **v4.1 (2026-04-10)**: Added **design principle**: agent scope = **tool/resource access and orchestration**; PACS/DB/clinical systems remain **behind governed adapters** (MCP/services), not inside the LLM.
- **v4.0 (2026-04-10)**: Merged duplicate sections; removed **unverified** deployment claims and **dead** sample links; added **Hermes** disambiguation; aligned **MedOpenClaw** and **OpenClaw-Medical-Skills** with **checkable** references; reframed scores as **qualitative** guidance; emphasized **MCP + graphs + clinical governance** as the upgrade path for multi-modality lifecycle platforms.

---

*Filename note: `Comparsion` retains the original spelling; rename to `Comparison` locally if you want consistent naming.*
