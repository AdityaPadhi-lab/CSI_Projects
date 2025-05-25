import pandas as pd

df = pd.read_csv("Telco-Customer-Churn.csv")
df.dropna(inplace=True)
df.drop("customerID", axis=1, inplace=True)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(subset=['TotalCharges'], inplace=True)
