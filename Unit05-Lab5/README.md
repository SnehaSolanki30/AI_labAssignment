# Lab 5: Machine Learning for Intelligent Decision Making (Decision Tree)

## 1. Aim / Problem Statement
To implement a **Decision Tree Classifier** for **Student Placement Prediction** and evaluate its performance using standard classification metrics and tree visualization[span_7](start_span)[span_7](end_span)[span_8](start_span)[span_8](end_span).

## 2. Algorithm
1. **Feature Matrix Creation:** Extract predictor variables (`CGPA`, `IQ`, `Internships`) and target label (`Placed`)[span_9](start_span)[span_9](end_span).
2. **Train-Test Split:** Partition the dataset into 75% training and 25% testing sets.
3. **Model Training:** Fit a `DecisionTreeClassifier` using Gini Impurity (`criterion='gini'`, `max_depth=3`) to learn hierarchical decision rules[span_10](start_span)[span_10](end_span).
4. **Evaluation & Visualization:** Generate predictions on test samples, compute the Confusion Matrix and Classification Report, and plot the trained decision tree structure[span_11](start_span)[span_11](end_span).

## 3. Results / Output
* **Sample Test Predictions:** Accurately classified placed and non-placed students based on `CGPA` and `Internships` thresholds.
* **Confusion Matrix:**
  ```text
  [[2 0]
   [0 2]]
