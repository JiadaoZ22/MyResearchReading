# MAMBA

## AI Answer
### 1. The Core Identity: What is Mamba?
Mamba is a **Selective State Space Model (SSM)**. It is a sequence modeling architecture that achieves **linear scaling** \[O(N)] with sequence length, unlike the quadratic scaling \[O(N^2)] of Transformers, while maintaining comparable performance on language modeling tasks.

It effectively bridges the gap between:
*   **RNNs:** Fast inference (constant state size), linear training (if unrolled), but suffer from vanishing gradients and lack parallelizability during training.
*   **Transformers:** Highly parallelizable training, but slow inference (KV cache grows linearly) and quadratic training complexity.

### 2. The Mathematical Origins: From HiPPO to S4 (2020–2023)
To understand Mamba, you must understand its predecessor, **S4 (Structured State Space Sequence Models)**, developed by Albert Gu (CMU/Stanford).

#### The Continuous Time Prior
SSMs map a 1D input signal \(x(t)\) to a 1D output \(y(t)\) via a latent state \(h(t)\) (dimension \(N\)):
\[ h'(t) = \mathbf{A}h(t) + \mathbf{B}x(t) \]
\[ y(t) = \mathbf{C}h(t) \]

#### Discretization (The RNN View)
To implement this on discrete data (tokens), we discretize the system using a step size \(\Delta\) (usually learned). Using Zero-Order Hold (ZOH), the continuous parameters \((\mathbf{A}, \mathbf{B})\) transform into discrete parameters \((\mathbf{\bar{A}}, \mathbf{\bar{B}})\):
\[ h_t = \mathbf{\bar{A}}h_{t-1} + \mathbf{\bar{B}}x_t \]
\[ y_t = \mathbf{C}h_t \]
This looks exactly like a linear RNN.

#### The Convolutional View (The S4 Breakthrough)
If the system is **Linear Time Invariant (LTI)**—meaning \(\mathbf{A}, \mathbf{B}, \mathbf{C}, \Delta\) are constant for all time steps—the recurrence can be unrolled into a global convolution:
\[ y = x * \bar{K} \]
where \(\bar{K}\) is the SSM kernel. This allowed S4 to train in parallel using FFTs, solving the RNN training bottleneck.

**The HiPPO Matrix:** The matrix \(\mathbf{A}\) is initialized using the HiPPO (High-order Polynomial Projection Operator) theory, which mathematically forces the state \(h(t)\) to compress the history of \(x(t)\) via orthogonal polynomial projection. This solved the "Long Range Dependency" (LRD) problem.

### 3. Mamba-1: The "Selection" Mechanism (Dec 2023)
**Paper:** *Mamba: Linear-Time Sequence Modeling with Selective State Spaces* (Gu & Dao).

S4 had a fatal flaw for Language Modeling: it was **LTI**. The dynamics were static. It could not perform "Content-Based Reasoning" (e.g., "if token A appears, pay attention to token B, otherwise ignore"). It treated every token with the same dynamics.

#### The Innovation: Selection
Mamba makes the parameters functions of the input \(x_t\).
\[ \mathbf{B} \rightarrow \mathbf{B}_t(x_t), \quad \mathbf{C} \rightarrow \mathbf{C}_t(x_t), \quad \Delta \rightarrow \Delta_t(x_t) \]

This breaks the LTI property. **Convolution (FFT) is no longer possible.** We are back to a recurrence.

#### The Hardware Solution: Parallel Associative Scan
To train this efficiently without convolution, Gu and Dao (the creator of FlashAttention) implemented a **hardware-aware Parallel Associative Scan** (prefix sum).
*   Instead of iterating \(t=1 \dots L\) sequentially (slow on GPU), they use the parallel scan algorithm to compute the recurrence in \(O(\log L)\) time on the GPU.
*   **Memory IO:** They fuse the discretization and scan operations into a single kernel, avoiding HBM (High Bandwidth Memory) I/O, keeping the large state \(h\) in SRAM.

### 4. Mamba-2: State Space Duality (May 2024)
**Paper:** *Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality* (Dao & Gu).

By mid-2024, the "Mamba-2" architecture (SSD) refined the theoretical framework.

#### The Insight: SSD
They proved a duality between **SSMs** and **Linear Attention**.
*   Standard Attention: \( \text{Softmax}(QK^T)V \)
*   Linear Attention: \( Q(K^TV) \) (dropping Softmax)
*   Mamba-2 showed that a specific structured SSM (using semi-separable matrices) is mathematically equivalent to a variant of Linear Attention with a masked causal structure.

#### Improvements
1.  **Tensor Core Usage:** Mamba-1 relied heavily on the scan (memory-bound). Mamba-2 reformulated the computation to use block-decomposition, allowing it to exploit Matrix Multiply Units (Tensor Cores) for the bulk of computation.
2.  **Larger State Size:** Because of the efficiency gains, the state dimension \(N\) (the "head dimension" equivalent) could be much larger (e.g., 64 to 128+), improving model capacity.

### 5. The Landscape: Late 2024 to Dec 2025
As of late 2025, Mamba has not "killed" the Transformer, but it has forced a bifurcation in foundation model design.

#### A. The Hybrid Era (Jamba, Zamba, Griffin)
The industry consensus (AI21 Labs, Zyphra, Google DeepMind) settled on **Hybrid Architectures**.
*   **The Problem:** Pure Mamba struggles slightly with "In-Context Retrieval" (e.g., "copy the exact phone number from the first sentence") compared to Attention, which can look up exact history.
*   **The Solution:** Interleave layers. E.g., 1 Attention layer for every 7 Mamba layers.
    *   **Jamba (AI21):** MoE + Mamba + Attention.
    *   **RecurrentGemma (Google):** Griffin architecture (closely related to Mamba).
*   **Benefit:** You get the massive context window (due to Mamba's compressed state) with the "sharp" recall of Attention, at a fraction of the KV-cache memory cost.

#### B. Vision Mamba (Vim / VMamba)
In Computer Vision, Mamba challenged the ViT (Vision Transformer).
*   **Mechanism:** Since images are non-causal 2D, Vision Mamba scans the image in 4 directions (TL-BR, BR-TL, etc.) to build a receptive field.
*   **Status 2025:** It is highly popular in **Medical Imaging** (3D MRI/CT segmentation) and **Video Generation**. Since video is temporal, Mamba's linear scaling allows for generating much longer, temporally coherent clips than pure Diffusion-Transformers (DiT) without exploding VRAM.

#### C. Edge and Robotics
Mamba is currently the SOTA for on-device LLMs (SLMs).
*   Because Mamba inference is a fixed-state RNN, the memory required to generate token #1000 is the same as token #1.
*   This constant-memory inference is critical for robotics and mobile devices where KV-cache management is a bottleneck.

### Summary for a Researcher
**Mamba (Dec 2025)** is no longer just "an RNN." It is a highly optimized **linear-attention-dual architecture** that utilizes:
1.  **Input-dependent gating** (Selection) to solve the forgetting problem.
2.  **Parallel Associative Scans** to solve the training speed problem.
3.  **Block-wise Matrix Multiplications** (in Mamba-2) to maximize GPU utilization.

It is the standard choice for **long-context** tasks (>100k tokens) and **efficient inference**, while Transformers remain the "Precision" layer used sparsely within these hybrid systems.

---

# What is a Mamba model?

**Source:** [IBM Think](https://www.ibm.com/think/topics/mamba-model)
**Author:** Dave Bergmann, Senior Staff Writer, AI Models

**Mamba** is a neural network architecture, derived from **state space models (SSMs)**, used for language modeling and other sequence modeling tasks.

The Mamba architecture’s fast inference speed and computational efficiency, particularly for long sequences, make it the first competitive alternative to the **transformer architecture** for autoregressive **large language models (LLMs)**.

Mamba models are perhaps the first deep learning architecture to rival the efficacy of transformer models on the task for which transformers originally won their fame: **language modeling**. Most notably, the Mamba architecture has demonstrated the capacity to match equivalently sized transformers on prominent LLM benchmark evaluations while often being significantly more efficient in terms of latency and memory requirements.

The Mamba architecture was first introduced by Tri Dao and Albert Gu in the 2023 paper, *“Mamba: Linear-Time Sequence Modeling with Selective State Spaces.”* A year later, they followed up the original Mamba paper with another paper that both explored the connections between SSMs and transformers and presented a refined, significantly faster version of the Mamba architecture, which they dubbed **Mamba-2**.

Though transformers have remained the dominant mode of LLM in the 2 years following the release of the original Mamba paper, the architecture has been incorporated into a growing number of open source models. Some, such as Mistral AI’s **Codestral Mamba**, are pure Mamba models. Many more, including AI21’s **Jamba series** and **IBM Granite 4.0**, are hybrid models incorporating both attention (transformer) layers and SSM (Mamba) layers.

In addition to their performance-based benefits, the proliferation of Mamba-based models promises to democratize AI access by virtue of running smoothly on comparatively inexpensive hardware.

---

## What are state space models?

SSMs were originally designed to predict the next state of a continuous sequence, like an electrical signal, a weather pattern, or the trajectory of a moving object, based on some input.

Conceptually and mathematically, they’re related to the **recurrent neural networks (RNNs)** that dominated natural language processing (NLP) prior to the introduction of transformers in 2017, as well as to other machine learning algorithms including **convolutional neural networks (CNNs)** and **hidden Markov models (HMMs)**.

As their name suggests, SSMs make predictions about the next state in a dynamic system by modeling the **state space**: a mathematical representation of all the state variables that describe the state of a system and the range of possibilities for each of those variables in tandem with one another.

An SSM takes an input sequence \( x(t) \) and maps it to a latent state representation \( h(t) \)—analogous to the hidden state of an RNN—in order to predict an output sequence \( y(t) \).

At the core of any SSM are 2 equations:

1.  **The state equation:**
    \[ h'(t) = A \times h(t) + B \times x(t) \]
2.  **The output equation:**
    \[ y(t) = C \times h(t) + D \times x(t) \]

The key parameters of the model are \( A \), \( B \), \( C \), and \( D \), which typically take the form of a matrix of weights.

In the fields where SSMs are conventionally used, such as **control theory**, these matrices are often assumed to be fixed: they represent the dynamics of an established system, and the SSM is used to find the inputs \( x \) that lead to desirable outputs \( y \).

In more modern conceptions of SSMs, those matrices are themselves parameters to be optimized through machine learning. In deep learning models, those parameters are learned via gradient descent.

### The Problem with Traditional SSMs (S4)
While effective for continuous data, earlier Structured State Space Models (like S4) relied on **Linear Time Invariance (LTI)**. This meant the matrices \( A, B, C \) were constant for every time step. While this allowed for efficient training via convolution, it prevented the model from performing content-based reasoning (e.g., focusing on specific words while ignoring others), a key capability of Transformers.

---

## The Mamba Innovation

The Mamba architecture introduces two key innovations that allow it to outperform traditional SSMs and rival Transformers:

### 1. The Selection Mechanism
Mamba breaks the Linear Time Invariance constraint. Instead of having static matrices \( B \) and \( C \), Mamba makes these parameters **input-dependent**.

In a Mamba layer, the matrices \( B \), \( C \), and the step size \( \Delta \) are generated from the input \( x(t) \) itself. This allows the model to selectively "remember" or "ignore" information at each time step.
*   **Relevance:** This mimics the "gating" mechanisms of LSTMs or the Attention mechanism of Transformers, allowing the model to filter information based on context.

### 2. Hardware-Aware Parallel Scan
Making the matrices dynamic breaks the ability to use efficient convolutions (FFTs) for training. To solve this, Mamba utilizes a **hardware-aware parallel algorithm** (specifically, a parallel associative scan).

This algorithm optimizes how the GPU handles computations:
*   It avoids costly memory I/O between the GPU's high-bandwidth memory (HBM) and the faster SRAM.
*   It computes the recurrent state updates in parallel (logarithmic time) rather than sequentially (linear time).

This results in a model that trains as fast as a Transformer but performs inference significantly faster.

---

## Mamba vs. Transformers

| Feature | Transformers | Mamba (SSM) |
| :--- | :--- | :--- |
| **Core Mechanism** | Attention (comparing every token to every other token) | Selective State Space (compressing history into a state) |
| **Training Speed** | Fast (Parallelizable) | Fast (Parallelizable via Scan) |
| **Inference Speed** | Slow (Quadratic scaling \( O(N^2) \)) | Fast (Linear scaling \( O(N) \)) |
| **Memory Usage** | High (KV Cache grows with sequence length) | Low (Constant state size) |
| **Long Context** | Expensive | Efficient |

While Transformers excel at "copying" and exact retrieval from history, Mamba excels at reasoning over massive sequences with limited memory. This has led to the rise of **Hybrid Models** (like Jamba and Granite), which combine Mamba layers for efficiency with occasional Attention layers for precision.



- The selective SSM and RAM allocation on a GPU. Taken from the original paper, "Mamba: Linear Time-Sequence Modeling with Selective State Spaces"
    <img src="image.png" alt="image" style="width:100%; height:auto; display: block; margin: 0 auto;">
- The Mamba block. The "x" following the selective SSM refers to element-wise multiplication, rather than standard dot product.
    <img src="image-1.png" alt="image" style="width:100%; height:auto; display: block; margin: 0 auto;">
- The Mamba-2 block.
    <img src="image-2.png" alt="image" style="width:100%; height:auto; display: block; margin: 0 auto;">
