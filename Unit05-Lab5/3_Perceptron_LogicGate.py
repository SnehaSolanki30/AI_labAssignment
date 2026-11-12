import time

# ==========================================================
# PROBLEM STATEMENT:
# Implement a Single-Layer Perceptron Neural Network from 
# scratch and train it using the Perceptron Learning Rule 
# to simulate a binary AND Logic Gate.
# ==========================================================

def step_activation(weighted_sum):
    return 1 if weighted_sum >= 0 else 0


def train_perceptron(inputs, targets, lr=0.1, epochs=15):
    """Trains weights and bias for a Single-Layer Perceptron."""
    start_time = time.time()
    weights = [0.0, 0.0]
    bias = 0.0

    for _ in range(epochs):
        for x, target in zip(inputs, targets):
            linear_output = (x[0] * weights[0]) + (x[1] * weights[1]) + bias
            prediction = step_activation(linear_output)
            error = target - prediction

            # Update weights and bias
            weights[0] += lr * error * x[0]
            weights[1] += lr * error * x[1]
            bias += lr * error

    exec_time = (time.time() - start_time) * 1000
    return weights, bias, exec_time


if __name__ == "__main__":
    # AND Gate Truth Table
    X_train = [(0, 0), (0, 1), (1, 0), (1, 1)]
    y_train = [0, 0, 0, 1]

    w, b, elapsed = train_perceptron(X_train, y_train)

    print("=== Single-Layer Perceptron Neural Network (AND Gate) ===")
    print(f"Trained Weights: w1={w[0]:.2f}, w2={w[1]:.2f} | Bias: {b:.2f}\n")

    for x in X_train:
        output = step_activation((x[0] * w[0]) + (x[1] * w[1]) + b)
        print(f"Input: {x} -> Predicted Output: {output}")

    print(f"\nTraining Time: {elapsed:.4f} ms")
