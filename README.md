# Automated Interpretation of Seismic Exploration Data Using Neural Networks

Diploma project, Astana IT University  
Educational Program: Software Engineering

## About the Project

Seismic interpretation is an important part of geological and geophysical analysis, but working with large volumes of seismic data manually can take a significant amount of time.

The goal of this project is to develop a system that uses neural networks to assist with the interpretation of seismic exploration data. The first machine-learning task selected for the project is semantic segmentation of seismic facies from 2D seismic sections.

The planned workflow is:

```text
Seismic data
    ↓
Preprocessing
    ↓
Neural network
    ↓
Semantic segmentation
    ↓
Seismic facies map
```

The project is being developed step by step. At the current stage, the main focus is on requirements, system architecture, ML methodology, data preparation, backend design, and evaluation planning. A fully trained model is not part of the first checkpoint.

---

## Team

| Team member | Main responsibility |
|---|---|
| Zhaksylyk Aruana (SE-2425) | System architecture, backend, integration, testing and project documentation |
| Rafikova Shugyla (SE-2427) | Neural-network module, seismic data preparation, ML methodology and experimental evaluation |

**Supervisor:** Turarova Marzhan Kabdikalievna

Both team members work in the same GitLab repository and use their own accounts so that individual contributions can be traced through commits and merge requests.

---

## Problem

Seismic datasets contain large amounts of information about subsurface geological structures. Manual interpretation requires specialist knowledge and can become time-consuming when many seismic sections have to be reviewed.

This project investigates whether a neural-network-based workflow can support this process by automatically assigning geological facies labels to seismic data.

For the first version of the ML component, the problem is defined as:

**Input:** a 2D seismic section or seismic patch.

**Output:** a pixel-level segmentation mask representing seismic facies.

The system is intended as an interpretation support tool rather than a replacement for professional geological judgement.

---

## Project Goal

The main goal is to design and develop an intelligent system for automated interpretation of seismic exploration data using neural networks.

The project includes:

- preparation and preprocessing of seismic data;
- semantic segmentation using a neural network;
- evaluation of segmentation quality;
- a backend API for future model integration;
- presentation of the interpretation results;
- testing and documentation of the complete workflow.

---

## Current ML Approach

### Dataset

The **Netherlands F3** dataset was selected as the primary dataset for the initial experiments.

Several public seismic datasets were considered before this decision, including Netherlands F3, Parihaka, Penobscot and SEAM.

The current data preparation plan includes:

- data loading and validation;
- seismic amplitude analysis;
- normalization;
- extraction of 2D sections and patches;
- preparation of segmentation labels;
- spatial train/validation/test separation;
- data augmentation;
- conversion to tensors for neural-network input.

Special attention is given to spatial data leakage because neighbouring seismic sections can contain strongly correlated information.

### Model

The initial baseline architecture is **U-Net**.

U-Net was selected after comparing it with SegNet and DeepLabV3+. Its encoder-decoder structure and skip connections make it a suitable starting point for pixel-level segmentation while keeping the first implementation relatively simple and reproducible.

More advanced architectures may be investigated after the baseline has been implemented and evaluated.

### Evaluation

The primary evaluation metric is:

- **mIoU — Mean Intersection over Union**

Supporting metrics are:

- Dice / F1 score;
- Pixel Accuracy;
- Mean Class Accuracy.

Actual metric values will only be reported after the corresponding model experiments have been performed.

---

## System Architecture

The planned system is divided into several components:

```text
Seismic Dataset
       ↓
Data Preprocessing
       ↓
Neural-Network Model
       ↓
Semantic Segmentation
       ↓
Backend API
       ↓
Result / Facies Map
```

The ML component is responsible for preparing seismic data and generating segmentation predictions.

The backend provides the interface between the ML component and the rest of the system. This separation allows the model to be developed and evaluated independently before full system integration.

---

## Technologies

The current technology stack includes:

| Area | Technology |
|---|---|
| Machine Learning | Python, PyTorch |
| Baseline model | U-Net |
| ML task | Semantic segmentation |
| Backend | FastAPI |
| API format | REST / JSON |
| Version control | GitLab |
| Project management | YouTrack |
| Dataset | Netherlands F3 |

The stack may be adjusted during later development if experiments or integration requirements show that changes are necessary.

---

## Repository Structure

The repository is organised by project component.

```text
.
├── backend/
├── ml/
│   ├── dataset_analysis.md
│   ├── model_research.md
│   └── preprocessing.md
├── docs/
├── tests/
└── README.md
```

The structure will grow as implementation begins. ML source code, experiment configurations and evaluation results will be added during the next development stages.

---

## Current Status

The first stage of the project focuses on establishing a clear technical foundation before full implementation.

### ML work completed so far

- **SAI-4 — Seismic Dataset Research**  
  Public seismic datasets were compared and Netherlands F3 was selected for the initial experiments.

- **SAI-5 — ML Task and Evaluation Metrics**  
  The task was defined as semantic segmentation. Model input/output and evaluation metrics were specified.

- **SAI-6 — Preprocessing Pipeline Design**  
  The planned data loading, normalization, section/patch preparation, dataset splitting and augmentation workflow was documented.

- **SAI-7 — Neural-Network Architecture Selection**  
  U-Net, SegNet and DeepLabV3+ were compared and U-Net was selected as the initial baseline.

At this point, these items describe the planned ML methodology. They should not be interpreted as completed model training or experimental results.

---

## Next Steps

After the first checkpoint, development will move from design and planning to implementation and evaluation.

The next stages are expected to include:

1. implementation of seismic data loading and preprocessing;
2. implementation of the baseline U-Net model;
3. connection of the ML component with the backend;
4. training and validation on the selected seismic dataset;
5. calculation of mIoU, Dice/F1, Pixel Accuracy and Mean Class Accuracy;
6. analysis of segmentation predictions and model errors;
7. integration of the components into an end-to-end prototype;
8. final testing and documentation.

The exact implementation and experiment schedule will be refined after the current project plan is reviewed.

---

## Project Management

Project work is tracked in **YouTrack** and linked to GitLab development where applicable.

For meaningful tasks:

- a YouTrack issue is created;
- the responsible team member is assigned;
- expected outcomes and acceptance criteria are defined;
- development is carried out in a task-specific branch;
- commits use descriptive messages and reference the corresponding task;
- relevant commits or merge requests are linked back to YouTrack.

This workflow is used to keep individual contributions and project progress traceable.

**YouTrack:** `[add project link]`

---

## Documentation

Current project documentation includes:

- project proposal and scope;
- requirements and acceptance criteria;
- system architecture and diagrams;
- seismic dataset analysis;
- ML task and evaluation metrics;
- preprocessing pipeline design;
- neural-network architecture comparison;
- verification and evaluation planning;
- project work plan.

Documentation is updated together with the implementation so that the repository reflects the actual state of the project.

---

## Current Limitations

The project is still in an early development stage.

At the current checkpoint:

- the baseline U-Net has not yet been fully trained and evaluated;
- final experimental metrics are not available;
- the ML component has not yet been integrated into the complete application;
- Netherlands F3 is the primary planned dataset, so generalisation to other seismic datasets has not yet been evaluated;
- model performance and computational requirements will only be known after experiments are completed.

These limitations are expected at the current stage and will be addressed during later development.

---

## Expected Outcome

The final project is expected to provide a reproducible workflow that accepts seismic data, prepares it for neural-network processing, performs semantic segmentation and returns a geological facies map.

The final evaluation will report measured model performance, examples of segmentation results, identified limitations and possible directions for further improvement.
