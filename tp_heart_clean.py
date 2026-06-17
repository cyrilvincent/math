import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
df = pd.read_csv("data/heartdisease/data_with_nan.csv", na_values=".", decimal=",")
print(df.isnull().sum())

# Les colonnes slope, cat et thal = drop
# calculer la moyenne et std de chol np.mean, np.nanmean, df["chol"].mean()
# df["chol"]= mean + rnd * std, rnd =(np.random.rand() - 0.5) * 2
# Pour les autres dropna
# Save