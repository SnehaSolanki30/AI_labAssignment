import time
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)

# ==========================================
# 1. SAMPLE STUDENT PLACEMENT DATASET
# ==========================================
start_time = time.time()

data = {
    'CGPA': [8.5, 7.2, 6.4, 9.1, 6.8, 7.9, 8.8, 6.1, 6.5, 8.2, 7.5, 8.9, 5.9, 7.8, 8.4],
    'IQ': [115, 102, 95, 125, 98, 110, 120, 92, 96, 114, 106, 122, 90, 109, 118],
    'Internships': [2, 1, 0, 3, 0, 1, 2, 0, 1, 2, 1, 3, 0, 2, 2],
    'Placed': [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1]  # 1 = Placed, 0 = Not Placed
}

df = pd.DataFrame(data)
X = df[['CGPA', 'IQ', 'Internships']]
y = df['Placed']

# ==========================================
# 2. TRAIN-TEST SPLIT & MODEL TRAINING
# ==========================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

clf = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)
clf.fit(X_train, y_train)

# ==========================================
# 3. PREDICTION & EVALUATION METRICS
# ==========================================
y_pred = clf.predict(X_test)
exec_time = (time.time() - start_time) * 1000

print("=== 1. Confusion Matrix ===")
print(confusion_matrix(y_test, y_pred), "\n")

print("=== 2. Classification Report ===")
print(classification_report(y_test, y_pred, target_names=['Not Placed', 'Placed']))

print(f"Accuracy : {accuracy_score(y_test, y_pred) * 100:.2f}%")
print(f"Precision: {precision_score(y_test, y_pred, zero_division=0) * 100:.2f}%")
print(f"Recall   : {recall_score(y_test, y_pred, zero_division=0) * 100:.2f}%")
print(f"F1-Score : {f1_score(y_test, y_pred, zero_division=0) * 100:.2f}%")
print(f"Execution Time: {exec_time:.2f} ms\n")

# ==========================================
# 4. DECISION TREE VISUALIZATION
# ==========================================
plt.figure(figsize=(10, 6))
plot_tree(
    clf,
    feature_names=['CGPA', 'IQ', 'Internships'],
    class_names=['Not Placed', 'Placed'],
    filled=True,
    rounded=True
)
plt.title("Decision Tree Classifier - Student Placement Prediction")
plt.savefig("decision_tree_plot.png")
print("Decision Tree visualization saved as 'decision_tree_plot.png'")
