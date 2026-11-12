# Lab 6: Deep Learning Fundamentals using PyTorch

## 1. Aim / Problem Statement
To explore PyTorch fundamentals (Tensor operations and Automatic Differentiation) and implement a **Linear Regression Neural Network** for **Student Score Prediction** based on study hours[span_5](start_span)[span_5](end_span)[span_6](start_span)[span_6](end_span)[span_7](start_span)[span_7](end_span).

## 2. Algorithm
1. **Tensor & Autograd Setup:** Create PyTorch tensors with `requires_grad=True` and compute exact analytical gradients using `.backward()`[span_8](start_span)[span_8](end_span)[span_9](start_span)[span_9](end_span).
2. **Model Architecture:** Define a single-layer neural network (`nn.Linear(1, 1)`) representing $\hat{y} = w \cdot x + b$[span_10](start_span)[span_10](end_span).
3. **Loss & Optimizer:** Use Mean Squared Error (`nn.MSELoss`) as the objective function and Stochastic Gradient Descent (`torch.optim.SGD`, `lr=0.01`) for weight updates[span_11](start_span)[span_11](end_span).
4. **Training Loop:** Run 300 epochs of forward propagation, loss calculation, backpropagation (`loss.backward()`), and parameter updates (`optimizer.step()`)[span_12](start_span)[span_12](end_span).

## 3. Results / Output
* **Autograd Check:** For $y = \sum x^2$ at $x = [2, 4, 6]$, computed gradients $\frac{dy}{dx} = [4, 8, 12]$.
* **Learned Linear Model:** $\text{Score} \approx 8.85 \times \text{Hours} + 25.40$
* **Prediction:** For `9.0` study hours, predicted exam score is **`~105.0` (capped at 100)**.
* **Visualization:** Saved training loss convergence plot as `pytorch_loss_curve.png`.

## 4. Performance Analysis
| Metric / Parameter | Value | Observation |
| :--- | :--- | :--- |
| **Optimizer** | SGD (`lr=0.01`) | Smooth convergence without oscillation[span_13](start_span)[span_13](end_span) |
| **Loss Function** | MSE Loss | Rapidly decreased within the first 50 epochs[span_14](start_span)[span_14](end_span) |
| **Epochs** | 300 | Reached stable minimum loss |
| **Training Time** | ~45.00 ms | Fast CPU tensor computation |

## 5. Learning Outcomes
* Understood PyTorch **Tensors** and **Automatic Differentiation (Autograd)** for gradient-based optimization[span_15](start_span)[span_15](end_span)[span_16](start_span)[span_16](end_span).
* Built a complete PyTorch training loop (`forward -> loss -> backward -> step`) and analyzed gradient descent convergence[span_17](start_span)[span_17](end_span).
*
