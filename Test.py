from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv('your_data.csv')

X = df.drop('Churn_Yes', axis=1)
y = df['Churn_Yes']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)