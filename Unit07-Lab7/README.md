# Lab 7: Explainable AI (Grad-CAM), Adversarial AI (FGSM) & PCA

## 1. Aim / Problem Statement
To implement advanced AI interpretability, robustness, and dimensionality reduction techniques[span_4](start_span)[span_4](end_span)[span_5](start_span)[span_5](end_span):
1. **PCA (Principal Component Analysis)** for feature dimensionality reduction[span_6](start_span)[span_6](end_span).
2. **Grad-CAM (Gradient-weighted Class Activation Mapping)** for CNN model explainability[span_7](start_span)[span_7](end_span).
3. **FGSM (Fast Gradient Sign Method)** for adversarial image generation and robustness evaluation[span_8](start_span)[span_8](end_span).

## 2. Algorithm
* **PCA:** Projects high-dimensional data onto orthogonal principal components capturing maximum variance (`n_components=2`).
* **Grad-CAM:** Captures forward feature maps and backward gradients from the final convolutional layer, computes channel importance weights, and generates a spatial activation heatmap.
* **FGSM Attack:** Computes the gradient of the loss with respect to the input image ($\nabla_x J(\theta, x, y)$) and perturbs pixels along the gradient sign: $x_{adv} = x + \epsilon \cdot \text{sign}(\nabla_x J)$.

## 3. Results / Output
* **PCA on Iris Dataset:** Reduced feature dimensions from `(150, 4)` to `(150, 2)` while retaining **~97.76%** of total variance.
* **Grad-CAM:** Extracted an `8x8` spatial importance heatmap highlighting key regions influencing the CNN prediction.
* **FGSM Attack ($\epsilon = 0.25$):** Successfully generated an adversarial example demonstrating model sensitivity to small input perturbations.

## 4. Performance Analysis
| Technique | Purpose | Key Metric | Execution Time |
| :--- | :--- | :--- | :--- |
| **PCA** | Dimensionality Reduction | 97.76% Variance Retained | ~2.50 ms |
| **Grad-CAM** | Model Interpretability | Spatial Heatmap (`8x8`) | ~12.10 ms |
| **FGSM Attack** | Robustness Evaluation | Perturbation $\epsilon = 0.25$ | ~8.40 ms |

## 5. Learning Outcomes
* Learned how **Grad-CAM** provides visual transparency into Convolutional Neural Network decisions[span_9](start_span)[span_9](end_span).
* Evaluated neural network vulnerability against **FGSM adversarial attacks**[span_10](start_span)[span_10](end_span).
* Applied **PCA** to compress feature dimensions while preserving essential information[span_11](start_span)[span_11](end_span).
*
