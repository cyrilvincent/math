# Charger data/heartdisease/data_with_nan.csv, mettre na_values="."
# Faire un describe()
# Sur l'ensemble du dataframe compter le nombre de na ;: dataframe.isnull().sum()
# Dropper les colonnes avec > 50% de na
# Dans la colonne chol le nb de na est significatif (~= 10%) -> remplacer les valeurs manquantes par mean + rnd * std
# df["chol"] = df["chol"].fillna(mean_chol + (np.random.rand() - 0.5) * std_chol)
# Pour les autres colonnes le nb de na est très faible => faire un dropna
# Sauvegarder le df dans dataclean.csv
# Créer ok_df = le df pour les num == 0
# Créer ko_df = le df pour les num == 1
# Faire un describe pour chacun des ok_df et ko_df
# Qu'en déduire sur l'age, le chol, le genre, la talach et autres ...
# Tester df.corr() et essayer de comprendre le résultat

import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

df = pd.read_csv("data/heartdisease/data_with_nan.csv", na_values=".")
print(df.describe())
print(df.isnull().sum())

df = df.drop(["slope", "ca", "thal"], axis=1)
mean_chol = df["chol"].mean()
std_chol = df["chol"].std()
df["chol"] = df["chol"].fillna(mean_chol + (np.random.rand() - 0.5) * 2 * std_chol)
df = df.dropna()

df.to_csv("data/heartdisease/dataclean.csv", index=False)

ok_df = df[df["num"] == 0]
ko_df = df[df["num"] == 1]

print(ok_df.describe())
print(ko_df.describe())

print(df.corr()["num"])