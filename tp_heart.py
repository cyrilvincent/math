# Lire heartdisease/data_with_nan.csv à l'aide de pandas en mettant na_values="."
# Supprimer les lignes avec des na (dropna) que se passe t'il ?
# Supprimer les colonnes à problèmes (à droite) : slope, ca, thal
# Puis supprimer avec dropna les lignes avec des na_values
# Sauvegarder le fichier nettoyé to_csv() avec le paramètre index=False
# dataframe_ok = au dataframe avec num == 0
# dataframe_ko = au dataframe avec num == 1
# Faire un describe sur les 2 dataframes regarder chol, thalach et age et en déduire une idée générale
# Facultatif faire des stats sur chol (mean, std, median, quantile, ...)

import numpy as np
import pandas as pd

dataframe = pd.read_csv("data/heartdisease/data_with_nan.csv", na_values=".")
dataframe = dataframe.drop(["slope", "ca", "thal"], axis=1)
dataframe = dataframe.dropna()
dataframe.to_csv("data/heartdisease/dataclean.csv")
dataframe_ok = dataframe[dataframe.num == 0]
dataframe_ko = dataframe[dataframe.num == 1]
print(dataframe_ok.describe().T)
print(dataframe_ko.describe().T)

chol_ok = dataframe_ok.chol.to_numpy()
chol_ko = dataframe_ko.chol.to_numpy()
print(np.mean(chol_ok), np.quantile(chol_ok, [0.25,0.5,0.75]))
print(np.mean(chol_ko), np.quantile(chol_ko, [0.25,0.5,0.75]))