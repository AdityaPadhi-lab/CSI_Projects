import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Telco-Customer-Churn.csv')  # Make sure the file exists in the same directory

sns.countplot(data=df, x='Churn')
plt.title("Churn Distribution")
plt.show()

# ✅ Encode categorical variables into dummy/indicator variables
df = pd.get_dummies(df, drop_first=True)
