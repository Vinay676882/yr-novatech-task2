import pandas as pd
import numpy as np

# 1. Load Dataset
df = pd.read_csv('customer_churn_dataset-training-master(2).csv')
print("Original Shape:", df.shape)

# 2. Remove Duplicates
df.drop_duplicates(inplace=True)

# 3. Handle Missing Values
num_cols = df.select_dtypes(include=[np.number]).columns
for col in num_cols:
    df[col].fillna(df[col].median(), inplace=True)

cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# 4. Save Cleaned Dataset
df.to_csv('cleaned_customer_churn_dataset.csv', index=False)
print("Data Cleaned and Saved Successfully!")