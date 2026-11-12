import time

# ==========================================================
# PROBLEM STATEMENT:
# Implement Simple Linear Regression from scratch using the 
# Ordinary Least Squares (OLS) method to predict student exam 
# scores based on daily study hours.
# ==========================================================

def train_linear_regression(x_values, y_values):
    """Calculates slope (m) and intercept (c) for y = m*x + c."""
    start_time = time.time()
    n = len(x_values)
    mean_x = sum(x_values) / n
    mean_y = sum(y_values) / n

    numerator = sum((x_values[i] - mean_x) * (y_values[i] - mean_y) for i in range(n))
    denominator = sum((x_values[i] - mean_x) ** 2 for i in range(n))

    m = numerator / denominator
    c = mean_y - (m * mean_x)
    exec_time = (time.time() - start_time) * 1000
    return m, c, exec_time


if __name__ == "__main__":
    # Training Data: Study Hours (X) vs Exam Score (Y)
    study_hours = [1, 2, 3, 4, 5, 6, 7]
    exam_scores = [35, 45, 50, 62, 70, 78, 88]

    slope, intercept, elapsed = train_linear_regression(study_hours, exam_scores)

    test_hours = 8.0
    predicted_score = (slope * test_hours) + intercept

    print("=== Supervised ML: Linear Regression ===")
    print(f"Learned Equation : Score = {slope:.2f} * Hours + {intercept:.2f}")
    print(f"Test Input       : {test_hours} Study Hours")
    print(f"Predicted Score  : {predicted_score:.2f} / 100")
    print(f"Execution Time   : {elapsed:.4f} ms")
