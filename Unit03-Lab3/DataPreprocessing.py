import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# ==========================================
# 1. CREATE / LOAD SAMPLE PLACEMENT DATASET
# ==========================================
start_time = time.time()

data = {
    'Student_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'CGPA': [8.5, 7.2, np.nan, 9.1, 6.8, 7.9, 8.8, np.nan, 6.5, 8.2],
    'IQ': [115, 102, 108, 125, 98, 110, 120, 105, 95, 114],
    'Internships': [2, 1, 1, 3, 0, 1, 2, 1, 0, 2],
    'Branch': ['MCA', 'CS', 'IT', 'MCA', 'CS', 'IT', 'MCA', 'CS', 'IT', 'MCA'],
    'Placed': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes']
}

df = pd.DataFrame(data)
print("=== 1. Original Dataset ===")
print(df, "\n")

# ==========================================
# 2. EXPLORATORY DATA ANALYSIS (EDA)
# ==========================================
print("=== 2. Dataset Summary & Missing Values ===")
print(df.describe())
print("\nMissing Values per Column:\n", df.isnull().sum(), "\n")

# ==========================================
# 3. DATA CLEANING (Handling Missing Values)
# ==========================================
# Fill missing CGPA values with the mean CGPA
df['CGPA'] = df['CGPA'].fillna(df['CGPA'].mean())
print("=== 3. Dataset After Filling Missing CGPA ===")
print(df[['Student_ID', 'CGPA']], "\n")

# ==========================================
# 4. DATA ENCODING (Label Encoding)
# ==========================================
le_branch = LabelEncoder()
le_placed = LabelEncoder()

df['Branch_Encoded'] = le_branch.fit_transform(df['Branch'])
df['Placed_Encoded'] = le_placed.fit_transform(df['Placed'])

print("=== 4. Encoded Categorical Columns ===")
print(df[['Branch', 'Branch_Encoded', 'Placed', 'Placed_Encoded']], "\n")

# ==========================================
# 5. FEATURE SELECTION & SCALING
# ==========================================
X = df[['CGPA', 'IQ', 'Internships', 'Branch_Encoded']]
y = df['Placed_Encoded']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ==========================================
# 6. TRAIN-TEST SPLIT (80% Train, 20% Test)
# ==========================================
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

exec_time = (time.time() - start_time) * 1000
print(f"=== 5. Train-Test Split Completed ===")
print(f"Training Samples: {X_train.shape[0]} | Testing Samples: {X_test.shape[0]}")
print(f"Total Preprocessing Time: {exec_time:.2f} ms\n")

# ==========================================
# 7. DATA VISUALIZATION (Matplotlib)
# ==========================================
plt.figure(figsize=(8, 5))
colors = ['green' if p == 'Yes' else 'red' for p in df['Placed']]
plt.scatter(df['CGPA'], df['IQ'], c=colors, s=100, alpha=0.8)
plt.title('Student Placement Analysis: CGPA vs IQ')
plt.xlabel('CGPA')
plt.ylabel('IQ Score')
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig('placement_eda_plot.png')
print("Visualization saved as 'placement_eda_plot.png'")
