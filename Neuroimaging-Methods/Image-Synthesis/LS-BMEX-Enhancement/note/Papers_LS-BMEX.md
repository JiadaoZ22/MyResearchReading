# LifespanStrip & BME-X: Key Innovations and Standout Features

## Overview

This document provides comprehensive analysis of two groundbreaking models from the DBC Lab for brain MRI processing:

1. **LifespanStrip**: A lifespan-generalizable skull-stripping model that leverages prior knowledge from brain atlases. The model achieves exceptional performance across the entire human lifespan (from birth to old age) and multiple imaging sites/modalities.

2. **BME-X**: A foundation model for enhancing magnetic resonance images and downstream segmentation, registration, and diagnostic tasks. It excels in super-resolution reconstruction, cross-scanner harmonization, artifact reduction, and pathological feature preservation.

Both models demonstrate how innovative architectural designs and training strategies can achieve state-of-the-art performance in medical image analysis.

---

# Part I: LifespanStrip

## Overview

**Paper**: Wang, L., Sun, Y., Seidlitz, J., et al. "A lifespan-generalizable skull-stripping model for magnetic resonance images that leverages prior knowledge from brain atlases." *Nature Biomedical Engineering*, 9, 700-715 (2025). DOI: 10.1038/s41551-024-01337-w

LifespanStrip is a lifespan-generalizable skull-stripping model for magnetic resonance images that leverages prior knowledge from brain atlases. The model achieves exceptional performance across the entire human lifespan (from birth to old age) and multiple imaging sites/modalities by combining several innovative architectural designs and training strategies.

---

## 📊 Training and Testing Datasets

### Training Dataset

**Total Training Data**: 300 scans distributed across 10 age groups (30 scans per age group)

| Age Group | Dataset Sources | Notes |
|-----------|-----------------|-------|
| 0 months (Neonate) | dHCP, BCP | Developing Human Connectome Project, Baby Connectome Project |
| 3 months | BCP | Baby Connectome Project |
| 6 months | BCP | Baby Connectome Project |
| 9 months | BCP | Baby Connectome Project |
| 12 months | BCP | Baby Connectome Project |
| 18 months | BCP | Baby Connectome Project |
| 24 months | BCP | Baby Connectome Project |
| 3-18 years (Child/Adolescent) | BCP, ABIDE | Autism Brain Imaging Data Exchange |
| 19-64 years (Adult) | ICBM | International Consortium for Brain Mapping |
| 65+ years (Elderly) | ADNI | Alzheimer's Disease Neuroimaging Initiative |

### Testing Dataset

**Total Testing Data**: 21,334 lifespan scans from 18 publicly available datasets

| Dataset | Age Range | Scanner | Participants | Notes |
|---------|-----------|---------|--------------|-------|
| **dHCP** | Neonates | Philips | ~150+ | Developing Human Connectome Project |
| **MAP** | 1-82 months | Siemens | 154 (67M, 87F) | - |
| **BCP** | 0-24 months | Siemens | - | Baby Connectome Project |
| **NDAR** | 6-24 months | Siemens | 951 (602M, 349F) | National Database for Autism Research |
| **HBN** | 5-21 years | Mixed | 1048 (741M, 303F, 4 unknown) | Healthy Brain Network |
| **ABIDE** | 5-64 years | Mixed (Siemens, GE, Philips) | 1074 (922M, 152F) | Autism Brain Imaging Data Exchange |
| **IXI** | 19-86 years | Mixed (Philips) | 590 (263M, 327F) | - |
| **CCNP** | 18-30 years | GE | 211 (58M, 153F) | Chinese Color Nest Project |
| **ICBM** | 12-89 years | Mixed | 1046 (473M, 428F, 145 unknown) | International Consortium for Brain Mapping |
| **HCP** | 22-35 years | Siemens | 457 (184M, 273F) | Human Connectome Project |
| **SLIM** | 17-27 years | Siemens | 555 (247M, 308F) | Southwest University Longitudinal Imaging |
| **SALD** | 19-80 years | Siemens | 493 (187M, 306F) | Southwest University Adult Lifespan Dataset |
| **DLBS** | 20-89 years | Philips | 270 (99M, 171F) | Dallas Lifespan Brain Study |
| **Chinese Adult Brain** | 22-79 years | Siemens | 163 | - |
| **ABVIB** | 62-90 years | Siemens | 216 (143M, 73F) | Aging Brain: Vasculature, Ischemia, and Behavior |
| **AIBL** | 55-92 years | Siemens | 1292 (605M, 686F, 1 unknown) | Australian Imaging, Biomarkers and Lifestyle |
| **OASIS3** | 42-97 years | Siemens | 2800 (1128M, 1410F, 262 unknown) | Open Access Series of Imaging Studies |
| **ADNI** | 40-93 years | Mixed | 9380 (5121M, 4258F, 1 unknown) | Alzheimer's Disease Neuroimaging Initiative |

### Additional Testing Data

- **EMEDEA-PED**: 37 pathological participants (1.4-17.8 years, Philips scanner)
- **NHP**: 10 non-human primate participants (Open Resource for Non-human Primate Imaging)
- **SynthStrip Test Set**: Third-party ground truth for evaluation

### Annotation Protocol

Ground truth brain masks were created using a **pseudo-manual labelling strategy**:
1. Multiple methods (BET, 3DSS, ROBEX, FreeSurfer, SynthStrip, HD-BET) generate initial "average" masks
2. Expert manual refinement by Li Wang (18+ years experience) using ITK-SNAP 3.8.0
3. Average correction: 72,512 voxels per participant (6.65% of total brain volume)
4. Time required: ~5 min for adults, ~15-20 min for infants with apparent inaccuracies
5. Total annotation process: ~1.5 years for 20,000+ scans

---

## 🏗️ Model Architecture Innovations

### 1. **Atlas-Empowered Two-Stage Pipeline**

The model employs a sophisticated two-stage approach that integrates age-specific brain atlases as prior knowledge:

**Stage 1: Brain Extraction Module**
- Uses a hybrid CNN-ViT architecture to extract brain parenchyma
- Generates an initial brain probability map from the input MRI

**Stage 2: Atlas Registration Module**
- Registers an age-specific brain atlas to the extracted brain region
- Applies both affine and deformable transformations
- Warps the atlas mask to produce the final refined brain mask

**Key Advantage**: The atlas-guided refinement leverages anatomical prior knowledge, significantly improving accuracy especially at challenging boundaries and in pathological cases.

---

### 2. **Brain Extraction Module Architecture**

The brain extraction module uses a **3D U-Net structure** with optional Vision Transformer enhancement:

#### **Core Architecture: 3D U-Net**

```
Input: T1w MRI (I) → Brain Extraction Module → Brain Probability Map (Pb)
                                              → Non-brain Probability Map (Pnb)
                                              → Estimated Brain (Ib = Pb · I)
```

**Encoder**:
- Each resolution level has **dual convolution** + **dual transformer** (optional)
- Convolution structure: 2× (Conv 3×3×3 → BN → ReLU)
- Outputs concatenated and subjected to 2×2×2 maxpooling

**Decoder**:
- Each layer: Deconv 2×2×2 (stride 2) → Conv 3×3×3 → BN → ReLU
- Skip connections from encoder layers at matching resolution

**Output Layer**:
- Produces brain probability map (Pb) and non-brain probability map (Pnb)
- Dot product: Ib = Pb · I (estimated brain)

**Loss Function**:
```
ℒext = -Gb·log(Pb) - Gnb·log(Pnb)  (Cross-entropy loss)
```

#### **Optional: Vision Transformer Enhancement**

The transformer block uses Multi-Head Self-Attention (MSA):
```
MSA(xi) = Softmax(qk^T / √d) · v
where q = xiWq, k = xiWk, v = xiWv
```

According to the paper's ablation study, ViT modules can be added at multiple resolutions:

- **ViT Stage 1**: 128×128×128 with 16×16×16 patches (hidden: 768, 12 heads)
- **ViT Stage 2**: 64×64×64 with 8×8×8 patches (hidden: 128, 8 heads)
- **ViT Stage 3**: 32×32×32 with 4×4×4 patches (hidden: 16, 4 heads)

**Paper's Ablation Study Results** (Supplementary Fig. 4):
> "the introduction of the transformer **slightly improved** overall performance (P < 0.001 and Cohen's d = 0.2093), increasing the Dice ratio from **0.9810 ± 0.0066** to **0.9823 ± 0.0058**"

**Key Finding**: The transformer provides only a **0.13% improvement** in Dice score, meaning the **CNN-only version performs almost as well**.

**Implementation Note**: The Docker containers (`bme-x:v1.0.3+`) use the **DenseUNet3d** (CNN-only) variant, which is validated by the ablation study as achieving 0.9810 Dice ratio - nearly identical to the full ViT-enhanced version.

---

### 3. **Registration Module Architecture**

The registration module provides personalized prior knowledge by aligning brain atlases to individual space:

#### **Rigid Registration Network**

```
Input: Concatenated [Estimated Brain (Ib), Atlas (A)]
       ↓
3× Convolution layers (kernel: 7, 5, 3) + 2×2×2 maxpooling
       ↓
2× Fully Connected layers + ReLU
       ↓
Output: Rotation (θx, θy, θz) + Translation (Δx, Δy, Δz)
       ↓
Spatial Transformation → Aligned Atlas (Aaligned), Aligned Mask (Am_aligned)
```

#### **Deformable Registration Network**

```
Input: Concatenated [Estimated Brain (Ib), Aligned Atlas (Aaligned)]
       ↓
U-shaped Architecture (Encoder-Decoder with Skip Connections)
- Encoder: 3×3×3 convolutions + BN + ReLU
- Decoder: Skip connections for multi-resolution feature fusion
       ↓
Output: Deformation Field (Φ)
       ↓
Spatial Transformation → Registered Atlas (Areg), Registered Mask (Am_reg)
```

#### **Loss Functions**

```python
# Registration loss (MSE between registered atlas and estimated brain)
ℒreg = (1/V) × Σ(Areg(v) - Ib(v))²

# Smoothness loss (L2 penalty on deformation field gradients)
ℒsmooth = Σ ||∇u(φ)||²  # Prevents folding artifacts

# Mask alignment loss (MSE between deformed atlas mask and ground truth)
ℒmask = (1/V) × Σ(Am_reg(v) - Gb(v))²
```

**Key Advantage**: The combination of rigid + deformable registration allows the model to handle large anatomical variations across ages while maintaining smooth, topology-preserving transformations.

---

## 🔧 Preprocessing and Postprocessing

### Image Preprocessing

1. **Orientation Adjustment**: Adjust images to standard reference frame (RAI)
2. **Inhomogeneity Correction**: N4ITK bias field correction
3. **Resampling**: Resample to 2×2×2 mm³ (to balance performance and GPU memory)
4. **Intensity Normalization**: Normalize intensity range across participants using histogram matching
5. **Brain Centering**: Rigidly move center of brain part to image center

### Image Postprocessing

1. **Morphological Opening**: Binary opening (radius 3-5) for noise removal
2. **Largest Connected Component**: Extract largest connected component
3. **Hole Filling**: Fill holes in the brain mask
4. **Resampling**: Resample back to original image resolution

---

## ⚔️ Comparison with Competing Methods

### Methods Compared

| Method | Type | Description |
|--------|------|-------------|
| **BET** | Deformable surface | Brain Extraction Tool using deformable mesh model |
| **3DSS** | Deformable surface | 3dSkullStrip with exterior surface information |
| **ROBEX** | Hybrid | Robust Brain Extraction combining deformable surface + discriminative methods |
| **FreeSurfer** | Hybrid | Watershed algorithm + statistical atlases |
| **SynthStrip** | Deep learning | Uses synthesized training images from anatomical label maps |
| **HD-BET** | Deep learning | Trained on large multi-centre neuro-oncology clinical trial |
| **LifespanStrip** | Deep learning + Atlas | Atlas-empowered lifespan skull-stripping (this paper) |

### Performance Results (21,334 scans)

**LifespanStrip consistently outperformed all competing methods** with statistical significance (P < 0.001):

| Metric | Effect Size vs Competing Methods |
|--------|----------------------------------|
| **Dice Ratio** | Large effect (Cohen's d > 1.0) in 16/18 datasets |
| **MSD** | Large effect (Cohen's d > 1.2) vs BET, 3DSS, ROBEX, FreeSurfer in almost all datasets |

### Common Failure Modes of Competing Methods

| Method | Over-segmentation | Under-segmentation |
|--------|-------------------|-------------------|
| **BET** | Skull base area | Forehead areas |
| **3DSS** | Skull base area | Forehead areas |
| **ROBEX** | - | Skull vertex region |
| **FreeSurfer** | Irregular errors | - |
| **SynthStrip** | Slight boundary errors | Slight boundary errors |
| **HD-BET** | Slight boundary errors | Subtle under-segmentation |
| **LifespanStrip** | Minimal errors | Minimal errors |

**Key Challenge**: None of the competing methods could accurately extract brain boundaries in **neonatal and infant participants** due to the narrow gap between brain and skull.

---

## 🎯 Training Strategy Innovations

### 1. **Multi-Task Learning Objective**

The model is trained with a composite loss function that combines four components:

```
Total Loss = Loss₁ + 0.1×Loss₂ + Loss₃ + 0.1×Loss₄
```

- **Loss₁ (Segmentation Loss)**: Cross-entropy loss for brain/non-brain classification
  - Trains the brain extraction module to accurately segment brain tissue
  
- **Loss₂ (Atlas-Brain Alignment Loss)**: MSE between registered atlas and extracted brain
  - Ensures the atlas aligns well with the extracted brain region
  - Weight: 0.1 (auxiliary objective)

- **Loss₃ (Deformation Smoothness Loss)**: L2 penalty on deformation field gradients with loss multiplier = 2
  - Ensures smooth, physically plausible deformations
  - Prevents unrealistic warping and folding artifacts
  - Encourages diffeomorphic (topology-preserving) transformations

- **Loss₄ (Mask Alignment Loss)**: MSE between deformed atlas mask and ground truth
  - Direct supervision for the final brain mask output
  - Weight: 0.1 (balances with segmentation loss)

**Key Advantage**: Multi-task learning enables the model to jointly optimize brain extraction and atlas registration, leading to better generalization.

---

### 2. **Age-Specific Atlas Selection Strategy**

During training and inference, the model dynamically selects age-appropriate atlases:

| Age Range | Atlas Used | Source |
|-----------|-----------|--------|
| 0-2 months | Month0 atlas | UNC/UMN BCP (Baby Connectome Project) |
| 3-4 months | Month3 atlas | UNC/UMN BCP |
| 5-7 months | Month6 atlas | UNC/UMN BCP |
| 8-10 months | Month9 atlas | UNC/UMN BCP |
| 11-14 months | Month12 atlas | UNC/UMN BCP |
| 15-20 months | Month18 atlas | UNC/UMN BCP |
| 21-28 months | Month24 atlas | UNC/UMN BCP |
| 3-18 years | Adolescent atlas | Unbiased age-appropriate pediatric atlas |
| 19-64 years | Adult atlas | SRI24 multichannel atlas |
| 65+ years | Elder atlas | MIITRA (Multichannel IIT & Rush University Aging) |

**Atlas Sources Summary**:
- **0-24 months**: 4D infant brain volumetric atlases from UNC/UMN BCP (168 infants)
- **3-18 years (Adolescent)**: Unbiased average age-appropriate pediatric atlas
- **19-64 years (Adult)**: SRI24 multichannel atlas
- **65+ years (Elder)**: MIITRA atlases constructed from 400 adults using multimodal template techniques

**Key Advantage**: Age-appropriate atlas selection provides anatomically relevant priors, enabling the model to handle dramatic developmental changes from infancy to old age.

---

### 3. **Comprehensive Lifespan Training Data**

The model is trained on a diverse dataset spanning the entire lifespan:

- **Training Data Distribution**:
  - 0-24 months: 240+ scans from dHCP and BCP
  - Adolescent: 30 scans from BCP and ABIDE
  - Adult: 30 scans from ICBM
  - Elder: 30 scans from ADNI

- **Multi-Site Training**: Data from multiple institutions ensures robustness to site-specific variations

- **Pathological Augmentation**: Extended model handles pathological cases with high distortion through simulated tissue loss during training

**Key Advantage**: Lifespan-spanning training data enables true generalization across all ages, avoiding age-specific bias.

---

### 4. **Data Augmentation Strategies**

The training pipeline includes sophisticated augmentation:

- **Spatial Augmentation**: 
  - Rotations (90-degree rotations along specific axes)
  - Multi-axis flipping (flips along all three axes)
  - Applied to both input images and ground truth masks simultaneously
- **Intensity Augmentation**: 
  - Histogram matching to normalize intensity distributions
  - Min-max normalization to [0, 1] range
- **Pathological Simulation**: 
  - Synthetic tissue loss for handling high-distortion pathological cases
  - Enables the extended model to handle severe deformities

### 5. **Training Hyperparameters**

- **Optimizer**: Adam or AdamW with learning rate = 1e-4
- **Learning Rate Schedule**: Warmup cosine annealing
- **Batch Size**: 1 (due to memory constraints of 3D volumes)
- **Mixed Precision Training**: Uses automatic mixed precision (AMP) for efficiency
- **Inference Overlap**: 0.8-0.9 for sliding window inference during validation

---

## 🔬 Technical Details

### Model Specifications

- **Input**: 128×128×128 voxels at 2×2×2 mm³ resolution
- **ViT Configuration**: 
  - Patch sizes: 16³, 8³, 4³ (multi-resolution)
  - Position embedding: Perceptron-based
  - Normalization: Instance normalization
- **Total Parameters**: Optimized for efficiency while maintaining performance

### Inference Pipeline

1. **Preprocessing**:
   - Reorientation to RAI (Right-Anterior-Inferior)
   - N4 bias field correction
   - Resampling to 128×128×128 at 2mm resolution
   - Histogram matching with template
   - Min-max normalization

2. **First Inference** (Coarse Extraction):
   - Brain extraction network generates initial brain probability map
   - Logits are converted to binary mask via argmax
   - Largest connected component extraction
   - Morphological opening (radius 3) for noise removal
   - Identifies approximate brain bounding box

3. **Second Inference** (Refinement):
   - **Cropping**: Extracts brain region from original image with padding (20-40 voxels)
   - **Resampling**: Cropped region resampled to 2mm resolution while preserving physical dimensions
   - **Centering**: Brain region centered within 128×128×128 array (aligned to bottom-center)
   - **Histogram Matching**: Second histogram matching pass for intensity normalization
   - **Atlas Registration**: 
     - Affine registration aligns atlas to extracted brain
     - Deformable registration refines alignment
     - Deformation field applied to atlas mask
   - **Mask Extraction**: Deformed atlas mask cropped back to original brain region
   - **Thresholding**: Binary mask created with 0.5 threshold
   - **Post-processing**: Morphological opening (radius 5) and largest component extraction

4. **Post-processing**:
   - Morphological opening
   - Largest connected component extraction
   - Resampling to original image resolution

---

## 🔬 Additional Validation Studies

### Pathological Brain MRIs

Tested on **37 pediatric patients** from the EMEDEA-PED archive with four pathology types:

| Pathology Type | Description | Performance |
|----------------|-------------|-------------|
| **ACC** (Agenesis of Corpus Callosum) | Structural abnormalities, enlarged ventricles | Dice > 0.95 |
| **MCD** (Malformations of Cortical Development) | Abnormal cortex, decreased gyri | Dice > 0.95 |
| **PFM** (Posterior Fossa Malformations) | Underdeveloped brainstem/cerebellum | Dice > 0.95 |
| **HD** (High Distortion) | Severe tissue loss | Dice improved from 0.857 to 0.954 with augmentation |

**Data Augmentation for HD Cases**:
- Random low-intensity shapes within brain to simulate tissue loss
- Random Gaussian/impulse noise in background (for 7T MP2RAGE)
- MSD improved from 4.738mm to 1.377mm after augmentation

### T2w MRI Support

- **Training**: 20 T2w scans from IXI dataset with T2w atlas from SRI24
- **Testing**: Diverse T2w scans (MPRAGE, FLASH sequences)
- **Result**: Reasonably good performance despite limited training data

### Robustness to Motion Artifacts

Tested on 2,125 scans with artificially added motion (mild, moderate, severe):

| Age Group | Dataset | N Scans | Result |
|-----------|---------|---------|--------|
| Neonates | dHCP | 382 | Robust performance |
| Infants | NDAR | 318 | Robust performance |
| Adolescents | ABIDE | 684 | Robust performance |
| Adults | CCNP | 180 | Robust performance |
| Elderly | ADNI | 561 | Robust performance |

**Outperformed SynthStrip** across all motion severity levels without noticeable over/under-segmentation errors.

### Robustness to Different Scanners

Tested on 21,186 scans across three scanner manufacturers:

| Scanner | N Scans | Performance |
|---------|---------|-------------|
| **Siemens** | 14,303 | Higher Dice, lower MSD than all competing methods |
| **Philips** | 3,073 | Higher Dice, lower MSD than all competing methods |
| **GE** | 3,810 | Higher Dice, lower MSD than all competing methods |

**Key Finding**: Variations in LifespanStrip performance were much smaller than competing methods across scanners.

### Non-Human Primate (NHP) Testing

- **Dataset**: 10 NHP images from Open Resource for Non-human Primate Imaging
- **Result**: Achieved highest accuracy among competing methods, demonstrating adaptability to primate neuroimaging

---

## 📊 Performance Advantages

### What Makes LifespanStrip Standout:

1. **Lifespan Generalization**: Single model works from birth to old age, avoiding the need for age-specific models

2. **Multi-Modality Support**: Primary focus on T1w, with demonstrated capability for T2w MRIs

3. **Pathological Robustness**: Extended model handles cases with high distortion through training augmentation (Dice improved 0.857 → 0.954)

4. **Atlas-Guided Refinement**: Incorporation of anatomical prior knowledge significantly improves boundary accuracy

5. **Multi-Site Robustness**: Training on diverse sites enables generalization across institutions

6. **Motion Artifact Robustness**: Handles mild, moderate, and severe motion artifacts effectively

7. **Scanner Independence**: Consistent performance across Siemens, Philips, and GE scanners

---

## 🔍 Additional Technical Details

### Registration Module Architecture Details

The registration module uses a hierarchical approach:

1. **Localization Network** (Affine Registration):
   - Architecture: Conv3d(2→64, kernel=7) → MaxPool → Conv3d(64→128, kernel=5) → MaxPool → Conv3d(128→256, kernel=3) → MaxPool
   - Output: 256×13×13×13 feature volume
   - Regressor: FC(256×13³ → 128) → ReLU → FC(128 → 6)
   - Predicts 6 affine parameters: 3 rotations (rx, ry, rz) and 3 translations (tx, ty, tz)
   - Transformation matrix constructed via rotation matrix composition and translation addition

2. **Deformable Registration Network**:
   - Encoder: 4-stage CNN (2→16→32→32→32 channels)
   - Decoder: 4-stage CNN with skip connections (32→32→32→32→16 channels)
   - Flow Field Generator: Conv3d(16→3, kernel=3) generates 3D deformation field
   - Initialization: Flow field weights initialized with small normal distribution (std=1e-5)

3. **Integration and Transformation**:
   - Velocity field scaled down by 1/128 initially
   - Scaling and squaring (7 iterations) produces displacement field
   - Displacement field resized and applied via spatial transformer
   - Ensures diffeomorphic (invertible, topology-preserving) transformation

### Loss Function Details

The smoothness loss (`smooth_loss`) computes:
- L2 penalty on spatial gradients of the deformation field
- Applied to all three spatial dimensions
- Loss multiplier of 2 increases the importance of smoothness
- Prevents folding artifacts that would violate topology preservation

### Atlas Integration Strategy

During inference, the model:
1. Extracts brain probability map from first stage
2. Uses brain mask to focus registration on relevant region
3. Concatenates extracted brain (`x_reg`) and registered atlas (`moving_trans`) as dual-channel input to registration network
4. This dual-channel approach allows the network to learn optimal alignment between extracted brain and atlas
5. Final mask comes from deformed atlas mask, not the initial segmentation

**Key Innovation**: The model doesn't just use the atlas as a template—it actively learns to align the atlas with the extracted brain, creating a feedback loop that improves both extraction and registration quality.

---

## 🎓 Key Insights for Model Design

### Design Principles:

1. **Prior Knowledge Integration**: Incorporating domain knowledge (brain atlases) into deep learning architectures dramatically improves performance

2. **Multi-Resolution Attention**: Applying attention mechanisms at multiple scales captures both global context and local details

3. **Hybrid Architectures**: Combining CNN and Transformer strengths leverages spatial inductive bias while maintaining long-range dependencies

4. **Differentiable Registration**: End-to-end learnable registration enables the model to adapt atlas priors to individual subjects

5. **Multi-Task Learning**: Joint optimization of related tasks (segmentation + registration) improves generalization through shared representations

6. **Age-Aware Priors**: Dynamic selection of age-appropriate atlases respects developmental anatomy

---

## 🎯 Top 5 Standout Innovations of LifespanStrip

1. **Atlas-Empowered Architecture**: The integration of age-specific brain atlases as learnable priors through differentiable registration is revolutionary—it combines traditional medical image processing wisdom with deep learning flexibility.

2. **Efficient CNN Backbone with Optional ViT**: The core DenseUNet3d architecture achieves 0.9810 Dice without transformers; adding ViT only improves to 0.9823 (+0.13%). The Docker implementation uses the efficient CNN-only version.

3. **Two-Stage Refinement Pipeline**: The coarse extraction followed by atlas-guided refinement creates a robust framework that handles both normal and pathological cases effectively.

4. **End-to-End Differentiable Registration**: The learnable affine + deformable registration module enables the model to adapt anatomical priors to individual subjects, creating personalized brain masks.

5. **Lifespan Generalization**: Training across the entire human lifespan (0 months to 160+ years) with age-appropriate atlases enables a single model to handle dramatic anatomical changes—something that was previously impossible.

---

## 🧬 Lifespan Brain Volume Trajectory

### Key Biological Findings

LifespanStrip enables accurate charting of brain volume across the lifespan:

```
Brain Volume Trajectory:
- Rapid growth: Birth → Early adolescence
- Stable plateau: Adulthood
- Gradual decline: Old age
```

### Peak Brain Volume

| Gender | Previous Study | LifespanStrip | Literature Reference |
|--------|---------------|---------------|---------------------|
| **Female** | ~11 years | ~11 years | ~10.5 years |
| **Male** | ~19 years | ~16 years | ~14.5 years |

**Key Finding**: LifespanStrip results align more closely with existing literature than previous studies.

### Brain Volume Comparisons

| Age Group | Previous Study (cm³) | LifespanStrip (cm³) | Literature (cm³) |
|-----------|---------------------|--------------------|--------------------|
| **Full-term neonates (70)** | 356.31 | 432.39 | 427.40 |
| **Females 16-25y (110)** | 1,550.10 | 1,375.37 | 1,400.33 |
| **Males 16-25y (338)** | 1,785.23 | 1,553.72 | 1,594.10 |
| **Females 26-80y (3,522)** | 1,493.34 | 1,325.48 | 1,338.25 |
| **Males 26-80y (3,660)** | 1,639.76 | 1,463.76 | 1,426.38 |

**Clinical Implication**: LifespanStrip provides a robust normalization tool for brain characterization, mitigating pre-existing variations in brain size and gender differences.

---

## ⚠️ Limitations and Future Work

### Current Limitations

1. **T1w Focus**: Current framework with MSE loss is tailored for T1w MRIs
   - **Future**: Implement NCC (Normalized Cross-Correlation) and MI (Mutual Information) loss for multi-modality support

2. **GPU Memory Constraints**: Transformer not applied to registration module due to memory limits
   - Single Tesla V100-SXM2 GPU (16GB) nearly exhausted with current architecture
   - **Future**: Investigate transformer integration in registration network

3. **High Distortion Cases**: Suboptimal performance on severe tissue loss cases
   - Training data predominantly from typically developing participants
   - **Solution**: Data augmentation with simulated tissue loss (Dice improved 0.857 → 0.954)

4. **Annotation Bias**: May have leveraged biases in consensus annotation protocols
   - **Future**: Continue assessment with third-party annotated labels

5. **Limited Age Groups**: Fewer participants in 3-15 and 36-45 year age ranges
   - **Future**: Include more participants in these age groups

6. **No Fetal Support**: Current model lacks fetal participants in training
   - **Future**: Incorporate fetal participants for prenatal brain analysis

---

## 💻 Software Requirements

### Python Environment

```
Python 3.8
PyTorch 1.9.1
MONAI 0.7.0
nibabel 3.1.1
tqdm 4.59.0
einops 0.3.0
tensorboardX 2.1
```

### Hardware Requirements

- **GPU**: Tesla V100-SXM2 (16GB) or equivalent
- **Training Resolution**: 2×2×2 mm³ (downsampled to balance performance and memory)

### Available Resources

| Resource | Location |
|----------|----------|
| **GitHub** | https://github.com/DBC-Lab/Atlases-empowered_Lifespan_Skull_Stripping |
| **Docker** | `limeiw/lifespanstrip:v2.0.1` |
| **iBEAT V2.0** | http://www.ibeat.cloud (Cloud/Docker integration) |
| **Pre-trained Models** | Available via Dropbox (see GitHub) |

---

## 📚 LifespanStrip References

### Primary Paper

- Wang, L., Sun, Y., Seidlitz, J., Bethlehem, R. A. I., Alexander-Bloch, A., Dorfschmidt, L., Li, G., Elison, J. T., Lin, W., & Wang, L. (2025). A lifespan-generalizable skull-stripping model for magnetic resonance images that leverages prior knowledge from brain atlases. *Nature Biomedical Engineering*, 9, 700-715. DOI: 10.1038/s41551-024-01337-w

### Repository and Resources

- GitHub Repository: https://github.com/DBC-Lab/Atlases-empowered_Lifespan_Skull_Stripping
- Pre-trained Models: Available via Dropbox link in repository
- Docker Container: `limeiw/lifespanstrip:v2.0.1` for easy deployment
- iBEAT V2.0 Cloud: http://www.ibeat.cloud

---

# Part II: BME-X

## Overview

BME-X (Brain MRI Enhancement) is a foundation model for enhancing magnetic resonance images and downstream segmentation, registration, and diagnostic tasks. As described in the [GitHub repository](https://github.com/DBC-Lab/Brain_MRI_Enhancement), BME-X demonstrates exceptional capabilities in MRI quality improvement, super-resolution reconstruction, cross-scanner harmonization, and preservation of pathological features.

---

## 🧠 Tissue Classification Details

### Number of Classes and Tissue Types

BME-X uses a **tissue classification network** to predict tissue labels, which guide the enhancement process. Based on the paper and implementation:

| Class | Tissue Type | Description |
|-------|-------------|-------------|
| 0 | **Background** | Non-brain regions |
| 1 | **CSF** | Cerebrospinal Fluid |
| 2 | **GM** | Grey Matter |
| 3 | **WM** | White Matter |

**Total: 4 classes** (Background + 3 brain tissues: CSF, GM, WM)

The tissue classification map is denoted as `Lc` where `c` is the number of tissue classes. The paper uses the notation `I₀ ∈ [0, n]` with labels n3, n4, n5, n6... indicating multiple tissue classes.

### Training Dataset for Tissue Classification

**Primary Training Data**:
- **52 foetal participants** (21-36 gestational weeks) - in-house collection
- **464 participants** (0-6 years old) - from UNC/UMN Baby Connectome Project (BCP)
- **Total: 516 participants**

**Tissue Label Generation**:
- Ground truth tissue labels were automatically generated using **iBEAT V2.0** (http://www.ibeat.cloud)
- iBEAT V2.0 is a cerebrum-dedicated pipeline that has processed 50,000+ scans from 200+ institutions
- All preprocessing (intensity inhomogeneity correction, skull stripping, cerebellum removal) passed quality control

**Age-Specific Models**:
The paper trained separate models for different developmental stages:
- Foetal phase
- 0, 3, 6, 9, 12, 18 months
- 24+ months (used for ages 24 months to 100 years)

**Data Augmentation**:
- 2,000 patches (40×40×40 at 0.8mm resolution) extracted per training image
- 95% training / 5% validation split
- Simulated degradation: rotation, periodic/continuous/sudden motions, imaging noise, image blurring

---

## 🏗️ Model Architecture Innovations

### 1. **Two-Stage Pipeline: Classification + Enhancement**

**IMPORTANT**: BME-X consists of **TWO separate DU-Net networks**:
1. **Tissue Classification Network** (DU-Net) → Predicts tissue labels
2. **Tissue-Aware Enhancement Network** (DU-Net) → Generates enhanced images guided by tissue labels

**Architecture Overview**:
```
Input: Corrupted/Low-Quality T1w MRI (I)
  ↓
┌─────────────────────────────────────────┐
│ STAGE 1: Tissue Classification Network  │
│ (DU-Net backbone)                       │
│   - Predicts tissue labels Lc           │
│   - 4 classes: Background, CSF, GM, WM  │
│   - Loss: Cross-entropy (L1)            │
└─────────────────────────────────────────┘
  ↓
  Lc (Tissue Classification Map)
  ↓
┌─────────────────────────────────────────┐
│ STAGE 2: Tissue-Aware Enhancement       │
│ (DU-Net backbone)                       │
│   - Input: Lc + I (concatenated)        │
│   - Output: Enhanced image I0           │
│   - Loss: MSE (L2)                      │
└─────────────────────────────────────────┘
  ↓
Output: Enhanced T1w MRI (I0)
```

**Total Loss**: L = L1 + λL2 (where λ = 10⁻⁷)

### 2. **DU-Net Architecture (Used in BOTH Networks)**

```
Encoder: Conv → 3× (Dense Block + Conv + BN + ReLU) → Dense Block
Decoder: 3× (Deconv + BN + ReLU + Dense Block) → Conv
```

**Key Features**:
- **Dense Connections**: Each layer receives feature maps from all preceding layers
- **U-Net Style Skip Connections**: Preserves fine-grained details
- **3D Convolutions**: Handles full 3D volumes for spatial consistency

### 3. **Ablation Study: With vs. Without Tissue Classification**

**CLARIFICATION**: The ablation study compared BME-X (with tissue classification) vs. DU-Net alone (without tissue classification). **Transformer was NOT tested in ablation** - it was only mentioned as a possible alternative architecture.

| Model | Architecture | Tissue Classification | Notes |
|-------|-------------|----------------------|-------|
| **BME-X** | DU-Net + DU-Net | ✅ Yes | Full two-stage pipeline |
| **DU-Net-0.5** | DU-Net | ❌ No | 0.5× parameters, baseline |
| **DU-Net-1** | DU-Net | ❌ No | 1× parameters (matched) |
| **DU-Net-1.5** | DU-Net | ❌ No | 1.5× parameters |

**Paper Quote** (Methods section):
> "Numerous network architectures are suitable for this classification task, such as U-Net, DenseNet, DU-Net, nnU-Net and **Transformer**. For this study, **we selected the DU-Net** architecture as our backbone classification model."

**Key Finding**: BME-X with tissue classification significantly outperforms DU-Net without tissue classification, even when DU-Net has 1.5× more parameters. The **tissue classification module is the key innovation**, not the network architecture itself.

**Key Advantage**: Simplifies complex image reconstruction from O(m×n) to O(m+n) complexity by first classifying tissues, then enhancing based on tissue labels.

---

### 2. **How BME-X Achieves Multiple Tasks with a Single Unified Model**

BME-X is designed as a **foundation model** that handles multiple enhancement tasks using the **same unified two-stage pipeline**. This is achieved through a fundamental design principle:

#### **Core Principle: Tissue-Aware Image Quality Convergence**

**Fundamental Assumption** (from paper):
> "Increasing image quality yields clearer and sharper image appearances, accompanied by **a convergence of intensity ranges within each tissue type to a single value**."

**How It Works**:
1. **Tissue Classification**: First identifies what tissue each voxel belongs to (background, CSF, GM, WM)
2. **Tissue-Aware Enhancement**: Then enhances each tissue type toward its "ideal" intensity value
3. **Universal Application**: The same process handles all degradation types because they all share the same goal—restoring tissue-specific intensity distributions

#### **Unified Training Strategy**

The model is trained on **paired low-quality and high-quality images** with various degradation types:

| Degradation Type | Training Simulation | Result |
|-----------------|-------------------|--------|
| **Motion Artifacts** | Simulated rotation, periodic, continuous, sudden motions | Model learns to restore tissue structures |
| **Low Resolution** | Downsampling (e.g., 0.8mm → 2.4mm) | Model learns super-resolution |
| **Noise** | Gaussian and Rician noise | Model learns denoising |
| **Low Contrast** | Gaussian smoothing filters | Model learns contrast improvement |
| **Scanner Variations** | Different scanners, protocols, field strengths | Model learns harmonization |

**Key Insight**: All these tasks are unified because:
- Motion artifacts blur tissue boundaries → Tissue classification helps restore them
- Low resolution loses details → Tissue-guided enhancement recovers them
- Noise corrupts intensities → Tissue-specific enhancement corrects them
- Low contrast obscures differences → Tissue-aware enhancement sharpens them
- Scanner variations shift intensities → Tissue normalization harmonizes them

#### **Seven Applications Achieved by the Same Model**

1. **Motion Removal**: Tissue classification is robust to motion-corrupted images, enabling artifact removal
   - Handles mild, moderate, severe motion (tested up to severe++, with limitations)
   
2. **Super-Resolution**: Reconstructs high-resolution images from low-resolution inputs
   - Example: 1.0×1.0×3.0 mm³ → 0.8×0.8×0.8 mm³
   - Tested on resolutions down to 2.4×0.8×0.8 mm³

3. **Denoising**: Removes Gaussian and Rician noise while preserving tissue structures
   - Effective for σ = 0.01-0.05 (Gaussian), limited performance at σ = 0.08+

4. **Contrast Improvement**: Enhances tissue contrast even for ultralow contrast images (σ = 1.2)

5. **High-Field-Like Reconstruction**: Generates 7T-like images from 3T scans
   - Trained on 28 participants with 7T images (0.4mm resolution)
   - Reconstructs from 0.8mm → 0.4mm resolution

6. **Fetal MRI Enhancement**: Handles fetal MRIs with substantial motion and noise
   - Trained on 52 fetal participants (21-36 gestational weeks)

7. **Harmonization**: Normalizes images across different scanners (Siemens, Philips, GE)
   - Maps all scans to same intensity distribution space
   - No need to assign a reference site (unlike ComBat)

#### **Why One Model Works for All Tasks**

The paper explains:
> "Most existing methods treat motion correction, super resolution and denoising as **separate tasks**, or propose sequential pipelines to address them one by one, resulting in cumulative errors and suboptimal solutions."

**BME-X's Unified Approach**:
- All degradation types corrupt the **same underlying structure**: tissue-specific intensity distributions
- By restoring tissue-specific intensities, the model simultaneously:
  - Removes motion artifacts (restores sharp boundaries)
  - Increases resolution (recovers fine details)
  - Removes noise (corrects intensity values)
  - Improves contrast (sharpens tissue differences)
  - Harmonizes scanners (normalizes tissue intensities)

**Key Advantage**: A single unified model handles all tasks, avoiding cumulative errors from sequential processing and ensuring consistent, high-quality output.

---

## 🎯 Training Strategy Innovations

### 1. **Age-Specific Model Training**

BME-X provides multiple pre-trained models optimized for different age groups:

- **Fetal**: Specialized model for fetal brain imaging
- **Early Development**: Models for 0, 3, 6, 9, 12, 18, 24 months
- **Adult**: General adult brain imaging model

**Training Data**:
- Training datasets provided in HDF5 format
- Multiple age-specific cohorts ensure age-appropriate enhancement
- Histogram matching templates provided for each age group

**Key Advantage**: Age-specific models account for developmental changes in brain anatomy and image characteristics.

---

### 2. **Supervised Learning with Multi-Task Training Data**

The model is trained using **paired training data** with diverse degradation types:

**Training Data Generation**:
- **High-Quality Source**: Artifact-free images from training dataset
- **Low-Quality Generation**: Multiple degradation types applied to same source images:
  - **Motion Artifacts**: Simulated rotation, periodic, continuous, sudden motions (via motion simulation tool)
  - **Low Resolution**: Downsampling to various resolutions
  - **Noise**: Gaussian and Rician noise addition
  - **Blurring**: Image blurring for contrast reduction
  - **Scanner Variations**: Training across different acquisition protocols

**Loss Function**: 
- **Total Loss**: L = L1 + λL2 (where λ = 10⁻⁷)
  - **L1 (Classification Loss)**: Cross-entropy for tissue classification
  - **L2 (Enhancement Loss)**: MSE between predicted and ground truth high-quality images

**Training Framework**: 
  - Original: Caffe (v1.0.0-rc3) 
  - Alternative: PyTorch implementation available in `PyTorch_version/`

**Key Advantage**: Training on diverse degradation types in a unified framework enables the model to learn a generalizable enhancement strategy that works across all tasks, rather than task-specific solutions.

---

### 3. **Histogram Matching for Intensity Normalization**

BME-X employs histogram matching as a preprocessing step:

- **Template Matching**: Uses age-appropriate templates for histogram matching
- **Parameters**: 
  - Number of histogram levels: Configurable
  - Match points: Multiple match points for smooth transformation
- **Purpose**: Normalizes intensity distributions before enhancement

**Key Advantage**: Histogram matching reduces intensity variations across subjects, improving model generalization.

---

## 🔬 Technical Details

### Model Specifications

- **Input Format**: 3D MRI volumes (T1w or T2w)
- **Input Channels**: 1 (single modality)
- **Output Format**: Enhanced 3D MRI volumes (same dimensions as input)
- **Inference**: Sliding window inference with configurable overlap (default 0.85)
- **ROI Size**: 64×64×64 voxels for sliding window processing

### Inference Pipeline

1. **Preprocessing**:
   - Reorientation to RAI (Right-Anterior-Inferior)
   - N4 bias field correction
   - Downsampling to target resolution (typically 1.6mm isotropic)
   - Histogram matching with age-appropriate template
   - Intensity normalization

2. **Enhancement Inference**:
   - Sliding window approach for large volumes
   - ROI-based processing (64×64×64 patches)
   - Overlap: 0.85 for smooth boundaries
   - ADU-Net enhancement on each patch

3. **Post-processing**:
   - Aggregation of overlapping patches
   - Upsampling to original resolution if needed
   - Intensity rescaling

### Quality Index (QI) Assessment

BME-X provides a Quality Index metric:
- **Purpose**: Quantifies image quality improvement
- **Range**: [0, ∞), where higher values indicate better quality
- **Application**: Enables objective assessment of enhancement effectiveness

---

## 📊 Performance Advantages

### What Makes BME-X Standout:

1. **Foundation Model Design**: Single model handles multiple enhancement tasks (super-resolution, harmonization, artifact reduction)

2. **Bias Quantification**: The model enables quantification of biases in tissue volumes and cortical thickness measurements, critical for downstream analyses

3. **Pathological Preservation**: Uniquely preserves small lesions during enhancement, maintaining diagnostic relevance

4. **Multi-Age Support**: Age-specific models ensure appropriate enhancement across the lifespan

5. **Cross-Scanner Robustness**: Harmonization capabilities enable consistent analysis across different scanner types

6. **Clinical Validation**: Tested on 280 in-vivo corrupted images from MR-ART dataset, demonstrating real-world applicability

7. **Downstream Task Improvement**: Enhanced images improve performance in segmentation, registration, and diagnostic tasks

---

## 🔍 Additional Technical Details

### Bias Quantification Capabilities

BME-X enables systematic bias quantification in downstream measurements:

- **Tissue Volume Analysis**: Quantifies bias in WM, GM, CSF, ventricle, and hippocampus volumes
- **Cortical Thickness**: Assesses bias in mean cortical thickness measurements
- **Comparison Metrics**: Provides difference analysis compared to standard (STAND) images
- **Statistical Analysis**: Effect size calculations (Cohen's d) for diagnostic tasks (e.g., AD vs. normal cognition)

**Key Innovation**: The model not only enhances images but also enables researchers to quantify and understand biases introduced during enhancement, which is crucial for clinical applications.

---

## 🎓 Key Insights for Model Design

### Design Principles:

1. **Foundation Model Paradigm**: Designing models as foundations for multiple tasks rather than single-task solutions increases utility and adoption

2. **Anatomy-Guided Enhancement**: Incorporating anatomical priors ensures medically relevant improvements

3. **Dense Connectivity**: Dense blocks enable effective feature reuse and gradient flow in deep networks

4. **Quality Quantification**: Providing objective quality metrics enables users to assess enhancement effectiveness

5. **Age-Aware Processing**: Age-specific models account for developmental changes in brain imaging

6. **Clinical Validation**: Testing on real-world corrupted images (MR-ART dataset) demonstrates practical applicability

7. **Bias Awareness**: Quantifying biases introduced during enhancement is crucial for clinical translation

---

## 🎯 Top 5 Standout Innovations of BME-X

1. **Two-Stage Tissue-Aware Pipeline**: Simplifies complex image reconstruction from O(m×n) to O(m+n) by reformulating as: f1: I→Lc (classification) + f2: Lc→I0 (enhancement).

2. **Tissue Classification Module**: The key innovation - using 4-class tissue labels (background, CSF, GM, WM) to guide enhancement. Ablation proves this module (not architecture choice) is what matters.

3. **Pathological Feature Preservation**: Unique ability to enhance image quality while preserving small lesions (MS, gliomas). Can be extended with auxiliary lesion labels.

4. **Bias Quantification Framework**: Systematic bias quantification in tissue volumes (WM, GM, CSF, ventricle, hippocampus) and cortical thickness, crucial for clinical translation.

5. **Cross-Scanner Harmonization**: Harmonizes images from Siemens, Philips, GE scanners (1.5T and 3T) into consistent distributions for multi-site studies.

---

## 📚 BME-X References

### Primary Paper

- Sun, Y., Wang, L., Li, G. et al. A foundation model for enhancing magnetic resonance images and downstream segmentation, registration and diagnostic tasks. *Nature Biomedical Engineering* 9, 521–538 (2025). https://doi.org/10.1038/s41551-024-01283-7

### Related Architecture

- Wang, L., Li, G., Shi, F., Cao, X., Lian, C., Nie, D., et al. "Volume-based analysis of 6-month-old infant brain MRI for autism biomarker identification and early diagnosis," *MICCAI*, 2018, pp. 411-419. (ADU-Net architecture)

### Repository and Resources

- GitHub Repository: https://github.com/DBC-Lab/Brain_MRI_Enhancement
- Pre-trained Models: Available for different age groups (fetal, 0-24 months, adult)
- Docker Support: Integrated with LifespanStrip in Docker containers
- Training Data: HDF5 format datasets available for training custom models

### System Requirements

- **Original Framework**: Caffe==1.0.0-rc3, Python==2.7.17
- **Alternative**: PyTorch implementation available
- **Dependencies**: SimpleITK, numpy, scipy
- **Docker Support**: Available for easy deployment

---

# Combined Analysis & Summary

## Integration: LifespanStrip + BME-X (LSBME Pipeline)

In the integrated pipeline (LSBME - LifespanStrip + BME-X):

1. **LifespanStrip** performs skull stripping on input MRI
2. **BME-X** enhances the skull-stripped brain image
3. The enhanced image is ready for downstream tasks (segmentation, registration, diagnosis)

This integration demonstrates the complementary nature of the two models:
- **LifespanStrip**: Anatomical boundary detection
- **BME-X**: Image quality enhancement within boundaries

---

## Summary

### LifespanStrip Summary

LifespanStrip achieves exceptional performance through a combination of:
- **Architecture**: DenseUNet3d CNN backbone (optional ViT for +0.13% improvement) + atlas-guided refinement
- **Training**: Multi-task learning with age-specific atlases across the lifespan
- **Innovation**: Differentiable registration that adapts anatomical priors to individual subjects

**Key Ablation Finding**: The Vision Transformer modules are **optional** and provide only marginal improvement:
- Without Transformer: Dice = **0.9810 ± 0.0066**
- With Transformer: Dice = **0.9823 ± 0.0058**
- Difference: **+0.0013** (0.13%)

The key insight is that **integrating domain knowledge (brain atlases) with efficient CNN architectures through differentiable registration creates a powerful framework for medical image analysis** that generalizes across ages, sites, and modalities. The transformer enhancement is optional and only provides marginal improvement.

### BME-X Summary

BME-X achieves exceptional performance through:
- **Architecture**: Two DU-Net networks (pure CNN) - one for classification, one for enhancement
- **Two-Stage Pipeline**: f1: I → Lc (tissue classification) → f2: Lc → I0 (enhancement)
- **Training**: Supervised learning with joint loss L = L1 + λL2 (Caffe framework)
- **Innovation**: Tissue classification module simplifies O(m×n) → O(m+n) complexity

**Key Ablation Finding**: 
- Ablation compared **BME-X (with tissue classification) vs. DU-Net (without tissue classification)**
- **Transformer was NOT tested** - only mentioned as possible alternative in Methods section
- Result: Tissue classification is the key innovation, not the network architecture

The key insight is that **simplifying complex image reconstruction to a tissue classification task (4 classes: background, CSF, GM, WM), combined with tissue-guided enhancement, enables versatile image enhancement that preserves clinical relevance**.

### Combined Pipeline (LSBME)

The integration of LifespanStrip and BME-X creates a powerful end-to-end pipeline:
1. **LifespanStrip**: Extracts brain boundaries using atlas-guided segmentation
2. **BME-X**: Enhances image quality within the extracted brain region
3. **Result**: High-quality, skull-stripped brain images ready for downstream analysis

This combination demonstrates how **complementary models can work together to achieve superior results**, with LifespanStrip handling anatomical boundary detection and BME-X focusing on image quality enhancement.

---

## Key Takeaways

Both LifespanStrip and BME-X represent significant advances in medical image processing:

- **LifespanStrip** demonstrates how domain knowledge (atlases) can be integrated with efficient CNN architectures through differentiable registration. **Transformer is optional** (+0.13% improvement in ablation study).
- **BME-X** shows how **tissue classification** (simplifying O(m×n) → O(m+n)) enables versatile image enhancement. Uses **two DU-Net networks** (pure CNN).

**Important Clarifications on Architecture**:

| Model | Core Architecture | Transformer Status | Key Innovation |
|-------|------------------|-------------------|----------------|
| **LifespanStrip** | 3D U-Net + Registration | Optional in ablation (+0.13%) | Atlas-guided refinement |
| **BME-X** | DU-Net + DU-Net | NOT tested (only mentioned) | Tissue classification module |

**Note on BME-X Ablation Study**:
- Ablation compared: BME-X (with tissue classification) vs. DU-Net (without tissue classification)
- Transformer was **mentioned as possible alternative** in Methods, but **NOT actually tested**
- Key finding: Tissue classification module is the innovation, not network architecture

Together, they form a comprehensive pipeline for brain MRI preprocessing that is robust, accurate, and clinically applicable across the entire human lifespan—achieved through **efficient CNN architectures** and **clever problem reformulation** (atlas priors + tissue classification).
