import time
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

# ==========================================
# 1. PCA FOR DIMENSIONALITY REDUCTION
# ==========================================
print("=== 1. PCA Dimensionality Reduction (Iris Dataset) ===")
start_time = time.time()
iris = load_iris()
X_iris = iris.data  # 4 features

pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X_iris)
print(f"Original Shape: {X_iris.shape} -> Reduced Shape: {X_reduced.shape}")
print(f"Explained Variance Ratio: {pca.explained_variance_ratio_.round(4)}\n")


# ==========================================
# 2. SIMPLE CNN FOR GRAD-CAM & FGSM DEMO
# ==========================================
class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 8, kernel_size=3, padding=1)
        self.fc = nn.Linear(8 * 8 * 8, 2)  # Binary image classification (8x8 input)
        self.gradients = None
        self.activations = None

    def activations_hook(self, grad):
        self.gradients = grad

    def forward(self, x):
        x = F.relu(self.conv1(x))
        self.activations = x
        if x.requires_grad:
            x.register_hook(self.activations_hook)
        x = x.view(x.size(0), -1)
        return self.fc(x)


torch.manual_seed(42)
model = SimpleCNN()
criterion = nn.CrossEntropyLoss()

# Sample synthetic 8x8 grayscale image & target label
sample_image = torch.rand((1, 1, 8, 8), requires_grad=True)
target_label = torch.tensor([1])

# ==========================================
# 3. EXPLAINABLE AI: GRAD-CAM HEATMAP
# ==========================================
print("=== 2. Explainable AI (Grad-CAM Visualization) ===")
output = model(sample_image)
pred_class = output.argmax(dim=1).item()

model.zero_grad()
output[0, pred_class].backward(retain_graph=True)

# Compute channel-wise weights and Grad-CAM heatmap
weights = model.gradients.mean(dim=(2, 3), keepdim=True)
grad_cam = F.relu((weights * model.activations).sum(dim=1)).squeeze().detach().numpy()
print(f"Predicted Class: {pred_class}")
print(f"Grad-CAM Importance Heatmap Shape: {grad_cam.shape} (Max Activation: {grad_cam.max():.4f})\n")


# ==========================================
# 4. ADVERSARIAL AI: FGSM ATTACK
# ==========================================
print("=== 3. Adversarial Attack using FGSM ===")
def fgsm_attack(image, epsilon, data_grad):
    """Generates adversarial example using Fast Gradient Sign Method."""
    sign_data_grad = data_grad.sign()
    perturbed_image = image + epsilon * sign_data_grad
    return torch.clamp(perturbed_image, 0, 1)

epsilon = 0.25
loss = criterion(output, target_label)
model.zero_grad()
loss.backward()

adversarial_image = fgsm_attack(sample_image, epsilon, sample_image.grad.data)
adv_output = model(adversarial_image)
adv_pred = adv_output.argmax(dim=1).item()

exec_time = (time.time() - start_time) * 1000
print(f"Original Prediction   : Class {pred_class}")
print(f"Adversarial Prediction (epsilon={epsilon}): Class {adv_pred}")
print(f"Total Execution Time  : {exec_time:.2f} ms")
