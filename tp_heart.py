# Charger data_with_nan dans pandas avec l'option na_values='.'
# Virer les colonnes slope,ca,thal
# Virer les lignes avec des NaN
# Sauvegarder le jeu de données nettoyé
# Filtrer par num = 0 (sain) et num = 1 (malade)
# Describe sur chol & thalach

import pandas as pd
import numpy as np

dataframe = pd.read_csv("data/heartdisease/data_with_nan.csv",na_values="." )
dataframe = dataframe.drop("slope", axis=1).drop("ca", axis=1).drop("thal", axis=1)
#dataframe = dataframe[dataframe.isna()]
dataframe = dataframe.dropna()

print(dataframe)
dataframe.to_csv("data/heartdisease/dataclean.csv", index=False)

ok = dataframe[dataframe.num == 0]
ko = dataframe[dataframe.num == 1]
print(ok.chol.describe())
print(ko.chol.describe())
print(ok.talach.describe())
print(ko.talach.describe())