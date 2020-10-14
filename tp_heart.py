# Charger data_with_nan.csv
# Effacer les colonnes -2 -3 -4
# Essayer 2 stratégies
#   fillna(0)
#   Calculer la moyenne et ecart type de chol
#   dropna
#   Calculer la moyenne et ecart type de chol
# Sauvegarder les données minées
# Etudier 4 colonnes : age, sex, trestbps, chol pur num = 0 et num = 1
# Calculer pour ces 4 colonnes moyennes et std

import pandas
import numpy as np
dataframe = pandas.read_csv("data/heartdisease/data_with_nan.csv", na_values=".")
dataframe = dataframe.drop("slope",1).drop("ca",1).drop("thal",1)

dataframe_1 = dataframe.fillna(0)
print(np.mean(dataframe_1.chol), np.std(dataframe_1.chol))

dataframe_2 = dataframe.dropna()
print(np.mean(dataframe_2.chol), np.std(dataframe_2.chol))

print(dataframe.shape, dataframe_2.shape)

print(np.mean(dataframe_2[dataframe_2.num == 0].age))
print(np.std(dataframe_2[dataframe_2.num == 0].age))
print(np.mean(dataframe_2[dataframe_2.num == 1].age))
print(np.std(dataframe_2[dataframe_2.num == 1].age))

print(np.mean(dataframe_2[dataframe_2.num == 0].sex))
print(np.std(dataframe_2[dataframe_2.num == 0].sex))
print(np.mean(dataframe_2[dataframe_2.num == 1].sex))
print(np.std(dataframe_2[dataframe_2.num == 1].sex))

print(np.mean(dataframe_2[dataframe_2.num == 0].trestbps))
print(np.std(dataframe_2[dataframe_2.num == 0].trestbps))
print(np.mean(dataframe_2[dataframe_2.num == 1].trestbps))
print(np.std(dataframe_2[dataframe_2.num == 1].trestbps))

print(np.mean(dataframe_2[dataframe_2.num == 0].chol))
print(np.std(dataframe_2[dataframe_2.num == 0].chol))
print(np.mean(dataframe_2[dataframe_2.num == 1].chol))
print(np.std(dataframe_2[dataframe_2.num == 1].chol))

dataframe_2.to_csv("data/heartdisease/dataclean.csv", index=False)