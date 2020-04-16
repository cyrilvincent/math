# Charger le fichier data/heartdisease/data_with_nan.csv
# Afficher l'entête du dataframe et noter les valeurs de l'avant dernière colonne
# Effacer les colonnes slope,ca,thal
# Nettoyer le fichier en remplacant les nan par 0
# Calculer la moyenne et l'écart type de chol
# Refaire en effacant les nan
# ReCalculer la moyenne et l'écart type de chol

import pandas as pd
import numpy as np

dataframe = pd.read_csv("data/heartdisease/data_with_nan.csv",na_values=".")

dataframe = dataframe.drop("slope",1)
dataframe = dataframe.drop("ca",1)
dataframe = dataframe.drop("thal",1)

dataframe2 = dataframe.fillna(0)

print(dataframe2)
print(np.mean(dataframe2.chol), np.std(dataframe2.chol))

dataframe3 = dataframe.dropna()
print(dataframe3)
print(np.mean(dataframe3.chol), np.std(dataframe3.chol))

