import matplotlib.pyplot as plt
import pandas as pd

import joblib
best_model = joblib.load('path_to_saved_model.pkl')

importances = best_model.feature_importances_

X = pd.read_csv('your_data.csv')

feat_importance = pd.Series(importances, index=X.columns).sort_values(ascending=False)

feat_importance[:10].plot(kind='barh')
plt.title("Top 10 Features Influencing Churn")
plt.show()