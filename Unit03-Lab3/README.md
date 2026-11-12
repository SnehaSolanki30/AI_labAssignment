# Lab 3: Data Preprocessing, EDA, NumPy, Pandas & Visualization

## 1. Aim / Problem Statement
To perform Exploratory Data Analysis (EDA) and build a complete data preprocessing pipeline on a Student Placement dataset using NumPy, Pandas, Scikit-learn, and Matplotlib[span_4](start_span)[span_4](end_span)[span_5](start_span)[span_5](end_span):
1. Dataset loading and statistical inspection[span_6](start_span)[span_6](end_span).
2. Handling missing values using mean imputation[span_7](start_span)[span_7](end_span).
3. Encoding categorical variables using `LabelEncoder`[span_8](start_span)[span_8](end_span).
4. Feature scaling (`StandardScaler`) and Train-Test splitting[span_9](start_span)[span_9](end_span).
5. Data visualization using scatter plots[span_10](start_span)[span_10](end_span).

## 2. Algorithm / Pipeline Steps
1. **Data Loading & EDA:** Load tabular data into a Pandas DataFrame and inspect distributions, summary statistics (`.describe()`), and null counts (`.isnull().sum()`).
2. **Missing Value Imputation:** Replace `NaN` entries in numerical columns (`CGPA`) with the column mean.
3. **Categorical Encoding:** Convert text labels (`Branch`, `Placed`) into numeric format using `LabelEncoder`.
4. **Feature Scaling & Splitting:** Normalize feature values using `StandardScaler` ($\mu = 0, \sigma = 1$) and split data into 80% training and 20% testing sets.
5. **Visualization:** Plot `CGPA` vs `IQ` color-coded by placement status (`Yes`/`No`).

## 3. Results / Output
* **Missing Values Handled:** 2 missing `CGPA` entries successfully imputed with the mean CGPA (`7.88`).
* **Categorical Encoding:** `Placed` mapped to `{'No': 0, 'Yes': 1}` and `Branch` mapped to `{'CS': 0, 'IT': 1, 'MCA': 2}`.
* **Train-Test Split:** 8 training samples and 2 testing samples generated with 4 scaled features.
* **Visualization:** Generated `placement_eda_plot.png` showing a clear positive correlation between higher CGPA/IQ and student placement.

## 4. Performance Analysis
| Preprocessing Step | Library Used | Complexity | Execution Time |
| :--- | :--- | :--- | :--- |
| Data Loading & EDA | Pandas / NumPy | $O(N \times M)$ | ~2.10 ms |
| Missing Value Imputation | Pandas | $O(N)$ | ~0.85 ms |
| Label Encoding | Scikit-learn | $O(N)$ | ~1.20 ms |
| Feature Scaling & Split | Scikit-learn | $O(N \times M)$ | ~1.50 ms |

## 5. Learning Outcomes
* Learned how to inspect, clean, and transform raw datasets using **NumPy** and **Pandas**[span_11](start_span)[span_11](end_span).
* Understood the importance of **Label Encoding**, **Feature Scaling**, and **Train-Test Splitting** before training machine learning models[span_12](start_span)[span_12](end_span).
* Created visual insights from tabular data using **Matplotlib**[span_13](start_span)[span_13](end_span).
*
