# Neural-Network Model Research

## 1. Objective

The objective of the machine-learning component is to assist seismic interpretation by automatically identifying geological facies in seismic sections.

The machine-learning task is formulated as a semantic segmentation problem.

For each pixel of an input seismic section, the neural network predicts the corresponding geological facies class.

---

# 2. Problem formulation

## Input

The model receives a two-dimensional seismic section extracted from a three-dimensional seismic volume.

Conceptually:

Input:

Seismic amplitude image

Output:

Pixel-level geological facies map

Therefore:

X = seismic section

Y = facies segmentation mask

The model learns a function:

f(X) → Y

where each output pixel represents a predicted geological facies class.

---

# 3. Why semantic segmentation was selected

Several possible machine-learning formulations were considered.

## Classification

Classification would assign a single label to an entire seismic image or patch.

This would not provide sufficient spatial information for geological interpretation.

## Object detection

Object detection could identify particular geological structures using bounding boxes.

However, geological facies are spatial regions rather than isolated objects, therefore bounding boxes are not an appropriate representation.

## Semantic segmentation

Semantic segmentation assigns a class to every pixel.

This makes it possible to identify geological boundaries and visualize the spatial distribution of seismic facies.

Therefore semantic segmentation is selected as the primary machine-learning task.

---

# 4. Evaluation metrics

The performance of the model will not be evaluated using a single metric.

The following metrics are selected.

---

## 4.1 Intersection over Union

For a particular class, Intersection over Union is defined as:

IoU = TP / (TP + FP + FN)

where:

- TP = true positive pixels;
- FP = false positive pixels;
- FN = false negative pixels.

IoU measures the overlap between the predicted region and the ground-truth region.

---

## 4.2 Mean Intersection over Union

Mean Intersection over Union averages IoU across all classes.

mIoU = mean(IoU_1, IoU_2, ..., IoU_n)

mIoU is selected as the primary evaluation metric.

Reason:

Pixel Accuracy can be misleading when classes are imbalanced. mIoU evaluates the quality of segmentation for individual classes and therefore provides a more informative measure of model performance.

---

## 4.3 Dice coefficient / F1 score

The Dice coefficient is defined as:

Dice = 2TP / (2TP + FP + FN)

It measures the similarity between the predicted segmentation mask and the ground-truth mask.

Dice is useful when evaluating region overlap.

---

## 4.4 Pixel Accuracy

Pixel Accuracy measures the proportion of correctly classified pixels.

Pixel Accuracy = correctly classified pixels / total pixels

It is intuitive and will be reported as an additional metric.

However, it will not be used as the only metric because seismic facies classes may be imbalanced.

---

## 4.5 Mean Class Accuracy

Mean Class Accuracy calculates accuracy independently for each class and averages the values.

This metric provides additional information about whether the model performs consistently across geological facies.

---

# 5. Selected metrics

The experimental evaluation will use:

Primary metric:

- Mean Intersection over Union (mIoU)

Secondary metrics:

- Dice / F1 score;
- Pixel Accuracy;
- Mean Class Accuracy.

The combination of several metrics provides a more reliable evaluation than Pixel Accuracy alone.

---

# 6. Baseline

A baseline is required to determine whether the neural-network approach provides meaningful results.

The initial neural-network baseline will be a standard U-Net semantic segmentation model.

The baseline experiment will use:

Dataset:

Netherlands F3

Task:

Seismic facies semantic segmentation

Model:

U-Net

Loss:

Cross-Entropy Loss

Primary metric:

mIoU

Additional metrics:

Dice/F1, Pixel Accuracy and Mean Class Accuracy.

---

# 7. Neural-network architecture comparison

Three encoder-decoder architectures are considered for the initial implementation:

1. U-Net
2. SegNet
3. DeepLabV3+

---

## 7.1 U-Net

U-Net is an encoder-decoder neural-network architecture originally developed for image segmentation.

The encoder progressively extracts higher-level features while reducing spatial resolution.

The decoder reconstructs the segmentation map.

Skip connections transfer features from encoder layers to corresponding decoder layers.

### Advantages

- well established for semantic segmentation;
- relatively simple architecture;
- skip connections preserve spatial information;
- suitable for small and medium-sized research datasets;
- numerous PyTorch implementations are available;
- suitable as a reproducible baseline.

### Limitations

- computational requirements increase with larger encoders;
- basic U-Net may have difficulty modelling large-scale context;
- performance depends on encoder and training strategy.

---

## 7.2 SegNet

SegNet is an encoder-decoder semantic segmentation architecture.

During decoding, it reuses pooling indices generated by the encoder.

### Advantages

- specifically designed for semantic segmentation;
- relatively memory-efficient decoder;
- simple conceptual architecture;
- previously used in seismic segmentation benchmarks.

### Limitations

- may preserve fine spatial detail less effectively than architectures with extensive skip connections;
- may provide lower segmentation accuracy depending on the dataset.

---

## 7.3 DeepLabV3+

DeepLabV3+ combines an encoder-decoder structure with atrous convolutions and Atrous Spatial Pyramid Pooling.

It is designed to capture information at multiple spatial scales.

### Advantages

- strong semantic segmentation architecture;
- captures multi-scale contextual information;
- effective for objects and structures of different sizes.

### Limitations

- more complex than baseline U-Net;
- higher computational cost;
- more hyperparameters and implementation complexity;
- unnecessary complexity may make the first prototype harder to reproduce.

---

# 8. Architecture comparison

| Criterion | U-Net | SegNet | DeepLabV3+ |
|---|---|---|---|
| Semantic segmentation support | High | High | High |
| Architecture complexity | Low–Medium | Medium | High |
| Fine-detail preservation | High | Medium | High |
| Multi-scale context | Medium | Medium | High |
| Computational cost | Medium | Medium | High |
| Ease of implementation | High | High | Medium |
| Suitability for baseline | Very High | High | Medium |
| Suitability for diploma prototype | Very High | High | High |

---

# 9. Selected architecture

U-Net is selected as the initial neural-network architecture.

The decision is based on the following factors:

1. U-Net is designed for semantic segmentation.
2. Its encoder-decoder architecture corresponds directly to the seismic facies segmentation task.
3. Skip connections help preserve spatial details and geological boundaries.
4. It is less complex to implement and reproduce than DeepLabV3+.
5. It provides a strong and understandable baseline.
6. U-Net-style architectures have already been investigated for seismic segmentation, which makes benchmark comparison possible.

The first prototype will therefore use U-Net.

More advanced architectures can be evaluated after establishing the U-Net baseline.

---

# 10. Proposed training configuration

Initial configuration:

Dataset:
Netherlands F3

Task:
Semantic segmentation

Model:
U-Net

Input:
2D seismic section or seismic patch

Output:
pixel-level facies segmentation mask

Loss:
Cross-Entropy Loss

Optimizer:
Adam or AdamW

Primary metric:
mIoU

Secondary metrics:
Dice/F1, Pixel Accuracy, Mean Class Accuracy

---

# 11. Experimental strategy

The experimental process will contain the following stages:

1. prepare the F3 dataset;
2. inspect seismic amplitudes and labels;
3. normalize input data;
4. prepare spatially separated training, validation and test data;
5. implement U-Net baseline;
6. train the model;
7. monitor validation metrics;
8. evaluate the final model on the test set;
9. calculate mIoU, Dice/F1, Pixel Accuracy and Mean Class Accuracy;
10. visualize predicted segmentation masks;
11. compare predictions with ground truth;
12. document limitations and potential improvements.

---

# 12. Future architecture experiments

After establishing the U-Net baseline, additional experiments may include:

- SegNet;
- DeepLabV3+;
- ResNet-based U-Net;
- attention-based segmentation models;
- Transformer-based architectures.

These experiments are considered extensions and are not required for the first prototype.

---

# 13. Expected outcome

The expected outcome is a reproducible baseline neural-network pipeline capable of producing pixel-level geological facies predictions from seismic sections.

The effectiveness of the approach will primarily be evaluated using Mean Intersection over Union and supported by Dice/F1, Pixel Accuracy and Mean Class Accuracy.