import pandas as pd
import numpy as np

df = pd.read_csv("data/heartdisease/data_with_nan.csv", na_values=".")

print(df.thal.isnull().sum())
df = df.drop("thal", axis=1)
df = df.drop("slope", axis=1)
df = df.drop("ca", axis=1)
print(df)
print(df.isnull().sum())

mean_chol = np.mean(df.chol)
std_chol = np.std(df.chol)
print(mean_chol, std_chol)

df.fillna({"chol": mean_chol + (np.random.rand() - 0.5) * 2 * std_chol}, inplace=True)
df = df.dropna()

print(df.isnull().sum())

df.to_csv("data/heartdisease/dataclean.csv")


# Compter les NaN pour chaque colonne : df.chol.isnull().sum()
# Si beaucoup => dropper la colonne
# 2 stratégies :
# Stratégie 1 : drop la ligne (dropna())
# Stratégie 2 : remplacer la valeur manquante par mean + noise : df.chol.fillna(mean + (np.random.rand() - 0.5) * std, inplace=True)
