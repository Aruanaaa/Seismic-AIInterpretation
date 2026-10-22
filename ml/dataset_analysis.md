# Seismic Dataset Analysis

## 1. Purpose

The purpose of this analysis is to identify an appropriate seismic dataset for developing and evaluating a neural-network module for automated seismic interpretation.

The planned machine-learning task is semantic segmentation of seismic sections. The model should receive a seismic image or section as input and assign a geological facies class to each pixel.

The dataset must therefore satisfy the following requirements:

- contain seismic data suitable for machine-learning experiments;
- provide labels or interpreted geological classes;
- be publicly accessible for academic use;
- support reproducible experiments;
- have sufficient documentation;
- be computationally feasible for a diploma project.

---

## 2. Candidate datasets

### 2.1 Netherlands F3

The Netherlands F3 dataset is a three-dimensional seismic dataset from the Dutch sector of the North Sea.

The dataset has been used in several machine-learning studies as a benchmark for seismic facies segmentation.

It contains seismic sections together with geological facies annotations, which makes it suitable for supervised semantic segmentation.

### Advantages

- publicly available;
- provides annotated seismic data;
- widely used in seismic machine-learning research;
- suitable for semantic segmentation;
- benchmark results from previous studies are available;
- relatively manageable size compared with many industrial seismic datasets;
- existing preprocessing and training pipelines are publicly available.

### Limitations

- the dataset represents one geological region;
- class distribution may be imbalanced;
- models trained only on F3 may not generalize to other seismic surveys;
- adjacent seismic sections are spatially correlated and therefore data splitting must be performed carefully.

### Proposed use

Netherlands F3 will be used as the primary dataset for development and baseline experiments.

---

## 2.2 Parihaka

The Parihaka seismic dataset originates from the Taranaki Basin, New Zealand.

It is another public seismic dataset used for geological interpretation and machine-learning research.

Processed versions with facies annotations are available and can be used for semantic segmentation experiments.

### Advantages

- real seismic survey;
- different geological setting from F3;
- useful for testing model generalization;
- processed machine-learning versions are publicly available.

### Limitations

- preprocessing requirements may differ from F3;
- geological characteristics differ from the main training dataset;
- adding a second dataset increases experimental complexity.

### Proposed use

Parihaka may be used during later stages of the project as an external dataset to evaluate model generalization.

---

## 2.3 Penobscot

The Penobscot dataset is a seismic dataset from offshore Nova Scotia, Canada.

Public processed versions with geological interpretations are available for machine-learning research.

### Advantages

- public research dataset;
- used in seismic interpretation benchmarks;
- provides another geological environment;
- can be used for cross-dataset experiments.

### Limitations

- preprocessing and annotations may differ from F3;
- combining datasets requires class harmonization;
- not necessary for the first implementation stage.

### Proposed use

Penobscot may be used for additional evaluation after the baseline model has been implemented using F3.

---

## 2.4 SEAM Open Data

SEAM provides several synthetic and interpreted seismic datasets designed for geophysical research and education.

### Advantages

- open access;
- high-quality synthetic seismic models;
- useful for controlled experiments;
- different seismic properties and geological structures are available.

### Limitations

- many SEAM datasets are significantly larger than the F3 benchmark;
- some datasets are synthetic rather than field observations;
- preparing SEAM data for a specific segmentation task may require additional annotation or preprocessing.

### Proposed use

SEAM is considered an additional source of seismic data but is not selected for the first prototype.

---

## 3. Dataset comparison

| Criterion | Netherlands F3 | Parihaka | Penobscot | SEAM |
|---|---|---|---|---|
| Public availability | Yes | Yes | Yes | Yes |
| Seismic data | Yes | Yes | Yes | Yes |
| Labels suitable for ML | Yes | Yes / processed versions | Yes / processed versions | Depends on subset |
| Semantic segmentation suitability | High | High | High | Medium |
| Existing ML benchmarks | Extensive | Available | Available | Task-dependent |
| Processing complexity | Medium | Medium | Medium | Medium–High |
| Suitable for initial prototype | Very high | High | High | Medium |
| Potential generalization dataset | Yes | Yes | Yes | Yes |

---

## 4. Selected dataset

The Netherlands F3 dataset is selected as the primary dataset for the first implementation of the neural-network module.

The main reasons are:

1. It contains annotated seismic data suitable for semantic segmentation.
2. It has been used in previous seismic machine-learning research.
3. Existing benchmark results allow the performance of the proposed model to be compared with previous approaches.
4. The dataset is computationally manageable for an academic prototype.
5. Public preprocessing and implementation examples are available.

---

## 5. Planned dataset usage

The planned workflow is:

Raw F3 seismic data  
loading and inspection  
normalization  
extraction of seismic sections or patches  
train/validation/test separation  
neural-network training  
semantic segmentation prediction  
metric calculation  
visualization of predicted geological facies.

During later stages, Parihaka or Penobscot may be used to evaluate whether the trained approach generalizes to another seismic survey.

---

## 6. Risks

The following dataset-related risks have been identified:

### Class imbalance

Some geological facies may occupy significantly fewer pixels than other facies.

Mitigation:

- analyze class distribution;
- use class-aware metrics;
- consider weighted loss functions if necessary.

### Spatial leakage

Neighboring seismic sections are highly correlated. Randomly mixing neighboring slices between training and test sets could result in overly optimistic evaluation.

Mitigation:

- use spatially separated training, validation, and test regions;
- preserve the official benchmark split when possible.

### Dataset-specific overfitting

A model trained only on F3 may learn characteristics specific to this survey.

Mitigation:

- evaluate on spatially independent test sections;
- later evaluate on another dataset such as Parihaka or Penobscot.

---

## 7. Expected outcome

The outcome of this task is a justified selection of the Netherlands F3 dataset as the primary dataset for development and initial evaluation of the seismic interpretation neural-network module.