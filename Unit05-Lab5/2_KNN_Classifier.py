import time
import math
from collections import Counter

# ==========================================================
# PROBLEM STATEMENT:
# Implement the K-Nearest Neighbors (KNN) Classification 
# algorithm using Euclidean distance to classify whether a 
# fruit is an 'Apple' or an 'Orange' based on weight & texture.
# ==========================================================

def euclidean_distance(point1, point2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))


def knn_predict(training_data, new_point, k=3):
    """Classifies new_point based on majority vote of K nearest neighbors."""
    start_time = time.time()
    distances = []

    for features, label in training_data:
        dist = euclidean_distance(features, new_point)
        distances.append((dist, label))

    # Sort by closest distance and take top K neighbors
    distances.sort(key=lambda item: item[0])
    k_nearest_labels = [label for _, label in distances[:k]]

    # Majority vote
    most_common = Counter(k_nearest_labels).most_common(1)[0][0]
    exec_time = (time.time() - start_time) * 1000
    return most_common, exec_time


if __name__ == "__main__":
    # Dataset: ([Weight_in_grams, Smoothness_Score], Label)
    dataset = [
        ([140, 9], "Apple"),
        ([130, 8], "Apple"),
        ([150, 9], "Apple"),
        ([170, 3], "Orange"),
        ([180, 2], "Orange"),
        ([165, 4], "Orange")
    ]

    sample_fruit = [145, 8]
    prediction, elapsed = knn_predict(dataset, sample_fruit, k=3)

    print("=== K-Nearest Neighbors (KNN) Classifier ===")
    print(f"Test Sample Features (Weight, Smoothness) : {sample_fruit}")
    print(f"Predicted Class (K=3)                     : {prediction}")
    print(f"Execution Time                            : {elapsed:.4f} ms")
