import pandas as pd
import numpy as np

df = pd.read_csv("data/heartdisease/data_with_nan.csv", na_values=["", "."])
# Je vire les colonnes avec trop de na
ratio_slope = df["slope"].isnull().sum() / len(df)
ratios = {}
for col in df.columns:
    ratios[col] = df[col].isnull().sum() / len(df)
print(ratios)


print(ratio_slope)
df = df.drop(["slope", "ca", "thal"], axis=1)
mean_chol = np.mean(df["chol"])
std_chol = np.std(df["chol"])


df = df.fillna({"chol": mean_chol + (np.random.rand() - 0.5) * std_chol})
print(df.isnull().sum())
df = df.dropna()
print(df)
df.to_csv("data/heartdisease/dataclean.csv")



# 1 Compter les nan => isnull().sum()
# 2 Les colonnes avec > 50% de nan: dropper les colonnes
# 3 les colonnes avec >2% de nan: remplacer la valeur par mean + bruit : 11.11
# 4 les colonnes avec < 2% de nan: dropper les lignes avec des nan : dropna()
# Save