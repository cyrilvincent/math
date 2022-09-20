import pandas as pd
import numpy as np

# Import le fichier data/heart/data_with_nan.csv
# Afficher le describe

dataframe = pd.read_csv("data/heartdisease/data_with_nan.csv", na_values=".")
print(dataframe.describe())

# dataframe_ok = num == 0
# dataframe_ko = num == 1
# Refaire les describes sur les colonnes sex, age, chol, thalach

dataframe_ok = dataframe[dataframe.num == 0]
dataframe_ko = dataframe[dataframe.num == 1]

print(dataframe_ok.thalach.describe())
print(dataframe_ko.thalach.describe())

# Nettoyer le fichier en partant de dataframe
# Virer les colonnes slope,ca,thal : dataframe.drop(["slope", "ca"], axis=1)
# Virer les lignes avec des na
# Vérifier le nombre de ligne supprimées (faire un describe avant et après suppression)
# Sauvegarder dataframe dans data/heartdisease/dataclean.csv

dataframe_clean = dataframe.drop(["slope", "ca", "thal"], axis=1)
dataframe_clean = dataframe_clean.dropna()
print(dataframe_clean.describe())
dataframe_clean.to_csv("data/heartdisease/dataclean.csv", index=False)

chol = dataframe_clean.chol
print(np.mean(chol), np.std(chol), np.var(chol), np.median(chol))
print(np.quantile(chol, [0.1, 0.2, 0.3]))