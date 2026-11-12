import time
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# ==========================================
# 1. TENSOR OPERATIONS & AUTOGRAD BASICS
# ==========================================
print("=== 1. PyTorch Tensor & Autograd Basics ===")
x_tensor = torch.tensor([2.0, 4.0, 6.0], requires_grad=True)
y_tensor = (x_tensor ** 2).sum()
y_tensor.backward()  # Compute dy/dx = 2x
print("Input Tensor :", x_tensor.data)
print("Gradients    :", x_tensor.grad, "\n")

# ==========================================
# 2. DATASET: STUDENT STUDY HOURS vs EXAM SCORE
# ==========================================
torch.manual_seed(42)
X = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0], [6.0], [7.0], [8.0]])
y = torch.tensor([[35.0], [45.0], [52.0], [63.0], [71.0], [80.0], [88.0], [96.0]])

# ==========================================
# 3. DEFINE LINEAR REGRESSION MODEL
# ==========================================
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)  # 1 input feature -> 1 output score

    def forward(self, x):
        return self.linear(x)

model = LinearRegressionModel()
criterion = nn.MSELoss()  # Mean Squared Error Loss
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)  # Stochastic Gradient Descent

# ==========================================
# 4. TRAINING LOOP
# ==========================================
start_time = time.time()
epochs = 300
losses = []

for epoch in range(epochs):
    # Forward pass
    predictions = model(X)
    loss = criterion(predictions, y)
    losses.append(loss.item())

    # Backward pass & optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

exec_time = (time.time() - start_time) * 1000

# ==========================================
# 5. MODEL EVALUATION & PREDICTION
# ==========================================
with torch.no_grad():
    test_hours = torch.tensor([[9.0]])
    predicted_score = model(test_hours).item()

w = model.linear.weight.item()
b = model.linear.bias.item()

print("=== 2. Linear Regression Training Results ===")
print(f"Learned Equation : Score = {w:.2f} * Hours + {b:.2f}")
print(f"Final MSE Loss   : {losses[-1]:.4f}")
print(f"Predicted Score for 9 Hours Study: {predicted_score:.2f}")
print(f"Training Time    : {exec_time:.2f} ms\n")

# ==========================================
# 6. LOSS CONVERGENCE VISUALIZATION
# ==========================================
plt.figure(figsize=(8, 4))
plt.plot(range(epochs), losses, color='blue', linewidth=2)
plt.title("PyTorch Linear Regression - Training Loss Convergence")
plt.xlabel("Epochs")
plt.ylabel("MSE Loss")
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig("pytorch_loss_curve.png")
print("Loss curve saved as 'pytorch_loss_curve.png'")
