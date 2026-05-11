# DeepSeek-V4 Architecture Explained for Deep Learning Beginners

*Prerequisites: basic knowledge of deep learning and attention mechanisms.*

This note breaks down DeepSeek-V4 from first principles. We start with the big picture, dive into each core component, and then trace the end-to-end data flow.

---

## 1. Overall Architecture Overview

DeepSeek-V4 is a **decoder-only Transformer** with three key innovations that enable a 1-million-token context window:

- **Extreme KV-Cache Compression** — reduces memory usage by ~90% compared to DeepSeek-V3
- **Hybrid MoE Routing** — 1.6T total parameters, but only 49B activated per token
- **Multi-Head Connection (mHC)** — boosts representational capacity without extra computation

### Key Specs (V4-Pro)

| Attribute | Value |
|-----------|-------|
| Total parameters | 1.6T |
| Activated parameters per token | 49B |
| Context window | 1,000,000 tokens |
| Transformer blocks | 61 |
| Attention variants | MQA, HCA, CSA (layer-specific) |
| MoE routing | Hash-Route (first 3 blocks), Top-K (remaining) |

---

## 2. Core Building Block: The Transformer Block

Like most modern LLMs, DeepSeek-V4 is a deep stack of identical blocks. Each block follows the standard decoder layout, but substitutes the usual dense feed-forward network with a **Mixture-of-Experts (MoE)** layer and replaces vanilla attention with a **layer-specific compressed attention** mechanism.

```
Input → Attention Layer → Residual → MoE Feed-Forward → Residual → Output
```

---

## 3. Attention Mechanisms at a Glance

All attention variants in V4 sit on top of **Multi-Query Attention (MQA)**:

- Multiple query heads (for rich representations)
- A single shared key head and a single shared value head (minimizes KV-cache size)

Even with MQA, storing the KV cache for 1M tokens would still consume hundreds of gigabytes. V4 solves this with **two compression strategies**, assigned to different layers based on their functional needs:

| Mechanism | Compression | Role | Typical Layer |
|-----------|-------------|------|---------------|
| **HCA** (Heavily Compressed Attention) | 128× | Global context, coarse granularity | Early layers |
| **CSA** (Compressed Sparse Attention) | 4× + sparse selection | Local detail, high relevance | Middle layers |
| **MQA** (Multi-Query Attention) | None (full) | Exact generation | Final layer |

In addition, every layer uses **SWA** (Sliding Window Attention) as a side channel to keep the most recent tokens uncompressed.

### Layer-Wise Scheduling

```python
compress_ratios = [128, 128, 4, 128, 4, 128, ..., 0]
# 128 = HCA, 4 = CSA, 0 = MQA
```

- **First 2 layers** — HCA for low-level global context
- **Middle layers** — alternating CSA and HCA to balance detail and efficiency
- **Last layer** — MQA for precise, uncompressed attention during generation

---

## 4. MoE (Mixture-of-Experts) System

MoE is how V4 scales to 1.6T parameters while keeping inference cost manageable. Instead of one dense feed-forward network, V4 maintains many small "expert" networks; each token is routed to exactly two of them.

### 4.1 Top-K MoE (Layers 4–61)

A **learned gating network** scores every expert for the incoming token and selects the top-2. This is flexible but introduces routing overhead and requires load-balancing regularization.

### 4.2 Hash-Route MoE (First 3 Blocks)

V4's novelty here is **deterministic, hash-based routing**:

```
expert_id = hash(token_id) % num_experts
```

- No learnable gate (saves parameters and compute)
- Perfectly balanced expert utilization by construction
- Near-zero routing latency

**Why this works for early layers**: In the first few layers, a token's raw identity is usually the strongest signal for which expert should handle it. Deeper layers need contextualized representations, so flexible Top-K routing becomes necessary.

---

## 5. mHC (Multi-Head Connection)

mHC is a lightweight modification to the standard residual pathway that lets the model learn several parallel representations of the same token.

### How It Works

1. **Expansion** — the embedding tensor `[B, L, D]` is repeated `N` times along a new dimension → `[B, L, N, D]`
2. **Parallel processing** — all `N` branches pass through the same stack of Transformer blocks
3. **Merge** — at the output, the branches are fused with an RMSNorm-based reduction before the language-modeling head

Because the branches share the same weights and are merged efficiently, the extra cost is negligible compared with running `N` independent models.

---

## 6. End-to-End Data Flow

```
1. Input tokens → Embedding → [B, L, D]
2. mHC expansion → repeat N× → [B, L, N, D]
3. Loop over 61 blocks:
   a. Attention (MQA / HCA / CSA) + SWA
   b. Residual add
   c. MoE (Hash-Route or Top-K)
   d. Residual add
4. mHC merge + RMSNorm → [B, L, D]
5. LM head → logits → [B, L, vocab_size]
```

---

## 7. Efficiency Summary

| Innovation | What It Saves |
|------------|---------------|
| HCA / CSA KV compression | ~90% reduction in KV-cache memory (the dominant long-context bottleneck) |
| MoE architecture | 1.6T expressive capacity at 49B active parameters per token |
| Hash-Route MoE | Eliminates gate overhead and load-balancing penalties in early layers |
| mHC | Better representations for near-zero extra FLOPs |
| Layer-wise attention scheduling | Each layer expends only the compute it actually needs |

*Net result*: for the same 1M-token context, V4 reportedly uses ~27% of the FLOPs and ~10% of the KV-cache memory of its predecessor.

---

## 8. Simplified Code Skeleton

```python
class DeepSeekV4(nn.Module):
    def __init__(self, args):
        super().__init__()
        self.embed = Embedding(args.vocab_size, args.dim)
        self.layers = nn.ModuleList([Block(layer_id, args) for layer_id in range(args.n_layers)])
        self.norm = RMSNorm(args.dim)
        self.head = LMHeadWithHC(args.vocab_size, args.dim)
        self.hc_mult = args.hc_mult

    def forward(self, input_ids):
        h = self.embed(input_ids)                     # [B, L, D]
        h = h.unsqueeze(2).repeat(1, 1, self.hc_mult, 1)  # [B, L, N, D]
        for layer in self.layers:
            h = layer(h, input_ids)
        logits = self.head(h, self.norm)              # [B, L, vocab_size]
        return logits

class Block(nn.Module):
    def __init__(self, layer_id, args):
        super().__init__()
        self.attn = Attention(layer_id, args)   # MQA / HCA / CSA
        self.moe = MoE(layer_id, args)          # Hash-Route or Top-K

    def forward(self, x, input_ids):
        x = x + self.attn(x)
        x = x + self.moe(x, input_ids)
        return x
```

---

# Part 2: Attention Deep Dive + Multi-Modal Adaptability

## 1. How Each Attention Variant Works

### 1.1 MQA — The Uncompressed Baseline

Used **only in the final layer**.

- Computes standard attention over the full, uncompressed KV cache.
- The last layer must have perfect context access because it directly determines the next token distribution.
- KV-cache footprint for 1M tokens: ~4 GB (already ~10× smaller than full multi-head attention thanks to MQA).

---

### 1.2 HCA (Heavily Compressed Attention)

**Use case**: early layers that need a global semantic sketch, not fine-grained detail — e.g., grasping the overall topic of a 1000-page book.

**Compression ratio**: 128:1 (128 consecutive KV pairs → 1 compressed pair)

#### Step-by-step Computation

```
Full KV sequence (1,000,000 tokens)
        ↓
Split into 7,813 non-overlapping blocks of 128 tokens
        ↓
Apply learned Compressor to each block
  → small MLP + intra-block positional encoding
  → 128 KV vectors → 1 compressed KV vector
        ↓
Compressed KV sequence (7,813 tokens)
        ↓
Standard MQA attention over compressed KV
  → yields a global-context signal
        ↓
Gated combination with SWA output
  → gate = sigmoid(query @ W_gate)
  → output = gate × global + (1 − gate) × local
```

**Key benefit**: reduces the number of KV pairs by 128×, making global attention over 1M tokens feasible.

---

### 1.3 CSA (Compressed Sparse Attention)

**Use case**: middle layers that must retrieve specific details — e.g., "what was the character's name mentioned on page 237?"

**Compression ratio**: 4:1 (light compression for fast scoring) + sparse selection (keep only top-K blocks)

#### Step-by-step Computation

```
Full KV sequence (1,000,000 tokens)
        ↓
Split into 250,000 non-overlapping blocks of 4 tokens
        ↓
Light compression: 4 KV vectors → 1 per block
        ↓
Fast MQA attention over compressed KV
  → attention scores become relevance estimates for each block
        ↓
Indexer selects top-K blocks (e.g., top 8 → 32 original tokens)
  → no extra network; scores come directly from the compressed attention step
        ↓
Retrieve original uncompressed KV for selected blocks only
        ↓
Detailed MQA attention over uncompressed selected tokens
  → yields a high-resolution context signal
        ↓
Gated combination with SWA (same gating as HCA)
```

**Key benefit**: you pay the full cost of uncompressed attention only on the ~0.003% of the context that matters to the current query.

---

### 1.4 SWA (Sliding Window Attention)

**Mandatory companion** in every HCA/CSA layer.

- Keeps the last **4096 tokens** fully uncompressed
- Computes standard MQA attention over this window
- **Why it matters**:
  1. Fills the granularity gap that compression/selection creates for immediate context
  2. Ensures coherent generation (the model must remember exactly what it just produced)
  3. Handles short-range dependencies too fine-grained for compressed attention

---

### 1.5 Why Layer-Wise Scheduling Works

Different layers process information at different levels of abstraction; giving each layer the exact attention budget it needs is what makes the architecture efficient.

| Layer Placement | Function | Attention Budget |
|-----------------|----------|------------------|
| Early HCA | Global document understanding | 128× compression |
| Middle CSA | Connecting specific facts across the document | 4× + sparse selection |
| Final MQA | Exact next-token generation | Full, uncompressed |

---

## 2. Can DeepSeek-V4 Handle Multi-Modal Input?

### Short Answer

The **text-only V4 model** (the 1M-context LLM described above) has **no native multi-modal support**. It was trained on text alone and lacks built-in vision or audio encoders.

### Longer Answer: Adapting V4 for Multi-Modal Tasks

Although V4 is text-only, its attention machinery is well suited to multi-modal sequences. DeepSeek already applies similar attention designs in their dedicated vision-language models (e.g., DeepSeek-VL 2.0). Adapting V4 would look like this:

#### Step 1 — Add a Vision Encoder

Use a standard Vision Transformer (ViT) to convert images or video frames into token embeddings:

- 224×224 image → 256 visual tokens
- 10-second video clip → 2,560 visual tokens

#### Step 2 — Fuse Modalities

Concatenate visual tokens and text tokens into a single 1-D sequence. Insert special boundary tokens to mark image/text transitions.

#### Step 3 — Leverage V4's Existing Attention

| V4 Mechanism | Multi-modal Role |
|--------------|------------------|
| **HCA** | Compress long visual streams (e.g., 2,560 video tokens → 20 tokens at 128×) |
| **CSA** | Select visual regions relevant to a text query (e.g., "find the cat" → attend to cat tokens) |
| **SWA** | Preserve recent video frames uncompressed for temporal coherence |

#### Step 4 — Fine-Tune

Pre-train the combined encoder–decoder on large image–text corpora (e.g., LAION), then fine-tune on downstream tasks such as image captioning or visual question answering.

### Limitations of a Naïve Adaptation

1. **No built-in cross-attention** — V4 uses only self-attention. Strong multi-modal performance usually requires explicit cross-attention between vision and language features.
2. **1-D positional bias** — attention treats all tokens as a flat sequence, ignoring the 2-D spatial structure of images. 2-D-aware positional encodings would be needed.
3. **No pre-trained multi-modal weights** — the vision encoder and any new cross-attention layers would have to be trained from scratch (or initialized from another pre-trained model).

---

## Key Takeaways

1. **Three-tier attention** — HCA for global context (128×), CSA for targeted detail (4× + sparse), SWA for immediate coherence (uncompressed window).
2. **All variants run on MQA**, keeping the KV cache as small as possible.
3. **Hybrid MoE** — Hash-Route removes overhead where routing is simple (early layers); Top-K preserves flexibility where it is needed (deep layers).
4. **mHC** increases representational diversity by processing `N` parallel branches at negligible extra cost.
5. The text-only V4 does not natively support images or video, but its attention architecture is highly transferable to multi-modal settings.

> *Want to go further? Ask for a concrete numerical walkthrough of CSA on a 10,000-token document, or a mathematical breakdown of the Compressor module.*
