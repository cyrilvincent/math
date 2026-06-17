import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
df = pd.read_csv("data/heartdisease/data_with_nan.csv", na_values=".", decimal=",")
print(df.isnull().sum())

df = df.drop(["slope", "ca", "thal"], axis=1)

print(np.mean(df["chol"].values))

def get_value(v):
    if np.isnan(v):
        return np.round(df["chol"].mean() + (np.random.rand() - 0.5) * 2 * df["chol"].std())
    else:
        return v

df["chol"] = df["chol"].apply(lambda chol: get_value(chol))
print(df.isnull().sum())
df = df.dropna()

df.to_csv("data/heartdisease/dataclean.csv")
# Les colonnes slope, ca et thal = drop
# calculer la moyenne et std de chol np.mean, np.nanmean, df["chol"].mean()
# df["chol"]= mean + rnd * std, rnd =(np.random.rand() - 0.5) * 2
# Pour les autres dropna
# Save