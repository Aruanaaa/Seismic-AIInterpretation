# Seismic Data Preprocessing Pipeline

## 1. Purpose

The purpose of the preprocessing pipeline is to transform raw seismic data into a consistent format suitable for neural-network training and evaluation.

The preprocessing pipeline must:

- load seismic amplitudes and labels;
- validate data dimensions;
- normalize seismic amplitudes;
- create model inputs and target masks;
- separate training, validation and test data;
- prevent information leakage;
- optionally apply data augmentation;
- convert data into tensors suitable for neural-network training.

---

# 2. Pipeline overview

The proposed preprocessing workflow is:

Raw seismic volume  
→ data loading  
→ integrity validation  
→ amplitude analysis  
→ normalization  
→ section extraction  
→ optional patch extraction  
→ label preparation  
→ spatial train/validation/test split  
→ training augmentation  
→ tensor conversion  
→ neural-network input.

---

# 3. Data loading

The primary dataset is the Netherlands F3 seismic dataset.

The preprocessing module will load:

- seismic amplitude volume;
- facies label volume;
- dataset split information where available.

Processed benchmark versions may provide seismic data and labels as NumPy arrays.

The initial implementation will therefore support NumPy-based data loading.

Future versions may additionally support SEG-Y data.

---

# 4. Data integrity validation

Before preprocessing, the following checks will be performed:

- seismic data can be loaded successfully;
- label data can be loaded successfully;
- seismic and label dimensions are compatible;
- no unexpected NaN or infinite values are present;
- labels contain only expected class identifiers;
- image and mask pairs are spatially aligned.

If an invalid sample is detected, preprocessing should report the problem rather than silently using corrupted data.

---

# 5. Amplitude analysis

Seismic amplitudes may have a different numerical range from ordinary image pixels.

Before normalization, the amplitude distribution will therefore be inspected.

The following statistics will be calculated:

- minimum;
- maximum;
- mean;
- standard deviation;
- selected percentiles.

This allows abnormal values and outliers to be detected.

---

# 6. Normalization

Neural networks generally train more reliably when input values are represented on a consistent scale.

The initial normalization strategy will use standardization:

x_normalized = (x - mean) / standard_deviation

where the statistics should be derived from training data.

An alternative robust normalization strategy may use percentile clipping before normalization if extreme seismic amplitudes negatively affect training.

The validation and test data must use normalization parameters derived from the training data to avoid data leakage.

---

# 7. Section extraction

The original seismic survey is a three-dimensional volume.

The initial neural-network model operates on two-dimensional inputs.

Therefore 2D sections will be extracted from the 3D volume.

Possible section orientations include:

- inline sections;
- crossline sections.

Using 2D sections simplifies the first implementation and significantly reduces computational requirements compared with a full 3D convolutional neural network.

---

# 8. Patch extraction

If complete sections are too large to train efficiently, sections may be divided into smaller patches.

Example:

256 × 256 pixels

or

128 × 128 pixels.

Patch extraction can:

- reduce GPU memory requirements;
- increase the number of training samples;
- support randomized training.

However, patches must be extracted only after the spatial dataset split has been defined.

Otherwise patches from the same geological region could accidentally appear in both training and test sets.

---

# 9. Label preparation

Each input seismic section must have a corresponding facies segmentation mask.

The segmentation mask contains an integer class identifier for every pixel.

Example:

0 → facies class 0  
1 → facies class 1  
2 → facies class 2  
...  
N → facies class N.

The exact number and names of classes will follow the selected F3 dataset release.

Labels must not be normalized as continuous values.

They must remain discrete integer classes.

---

# 10. Train, validation and test split

The seismic dataset contains strong spatial correlation.

Neighboring seismic sections may contain nearly identical geological structures.

Therefore a completely random image-level split may cause information leakage.

The preferred strategy is to use:

- the official benchmark split, if available;
or
- spatially separated regions.

The dataset will be separated into:

Training set

Used for parameter optimization.

Validation set

Used for model selection and hyperparameter decisions.

Test set

Used only for final model evaluation.

The test set must not be used to tune model parameters.

---

# 11. Data leakage prevention

Several precautions will be used.

## 11.1 Spatial separation

Neighboring sections should not be randomly distributed between training and test sets.

## 11.2 Normalization statistics

Mean and standard deviation must be calculated only using training data.

## 11.3 Data augmentation

Augmentation must only be applied to training data.

## 11.4 Final test set

The test set must remain isolated until final evaluation.

---

# 12. Data augmentation

Data augmentation may be applied to improve model robustness.

Possible transformations include:

- horizontal flipping where geologically appropriate;
- cropping;
- small amplitude perturbations;
- controlled noise injection.

Augmentation must preserve the spatial correspondence between seismic input and segmentation mask.

Therefore geometric transformations applied to an image must also be applied to its label mask.

Aggressive transformations that could create geologically unrealistic structures should be avoided.

---

# 13. Tensor conversion

The processed data will be converted into tensors.

Conceptual shapes:

Input:

[B, C, H, W]

where:

B = batch size  
C = number of input channels  
H = image height  
W = image width.

For a single-channel seismic image:

C = 1.

Target segmentation mask:

[B, H, W]

Each target pixel contains its integer facies class.

---

# 14. Proposed implementation modules

The preprocessing code will later be separated into several components.

## dataset.py

Responsibilities:

- load seismic data;
- load segmentation labels;
- return image/mask pairs.

## preprocessing.py

Responsibilities:

- normalization;
- optional clipping;
- section preparation;
- patch extraction.

## transforms.py

Responsibilities:

- training augmentation;
- tensor conversion.

This separation improves maintainability and testing.

---

# 15. Planned pseudocode

```python
load seismic volume
load label volume

validate shapes
validate values

create spatial train/validation/test regions

calculate normalization statistics from training data

for each training section:
    normalize seismic amplitudes
    extract section
    optionally extract patches
    apply training augmentation
    convert image to tensor
    convert mask to class tensor

for validation/test sections:
    normalize using training statistics
    extract section
    optionally extract patches
    convert to tensor
```

---

# 16. Preprocessing acceptance checks

The preprocessing implementation will later be considered valid when:

1. seismic data and labels load without errors;
2. image and mask dimensions match;
3. normalized data contains finite numerical values;
4. class identifiers remain unchanged;
5. training, validation and test regions do not overlap;
6. one processed sample can be passed to the neural network;
7. the same preprocessing configuration can be reproduced.

---

# 17. Expected outcome

The result of preprocessing will be a reproducible collection of normalized seismic inputs and corresponding geological facies masks suitable for neural-network training, validation and testing.