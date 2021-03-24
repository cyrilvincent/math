import pandas
import numpy as np

# Charger data_with_nan.csv avec na_values="."
# Virer les colonnes slope ca et thal
# Virer les lignes avec na (vérifier également répartis)
# Sauvegarder la dataframe dans dataclean.csv
# Trouver une corrélation sur l'age, trestbps, chol, sex en fonction num = 0 ou 1 en calculant la moyenne et std

dataframe = pandas.read_csv("data/heartdisease/data_with_nan.csv", na_values=".")
dataframeclean = dataframe.drop("ca", axis=1).drop("thal", axis=1).drop("slope", 1)
dataframeclean = dataframeclean.dropna()
dataframeclean.to_csv("data/heartdisease/dataclean.csv", index=False)

dataframe_ok = dataframeclean[dataframeclean.num == 0]
dataframe_ko = dataframeclean[dataframeclean.num == 1]

print(np.mean(dataframe_ok.age), np.std(dataframe_ok.age), np.mean(dataframe_ko.age), np.std(dataframe_ko.age))
print(np.mean(dataframe_ok.trestbps), np.std(dataframe_ok.trestbps), np.mean(dataframe_ko.trestbps), np.std(dataframe_ko.trestbps))
print(np.mean(dataframe_ok.chol), np.std(dataframe_ok.chol), np.mean(dataframe_ko.chol), np.std(dataframe_ko.chol))
print(np.mean(dataframe_ok.sex), np.std(dataframe_ok.sex), np.mean(dataframe_ko.sex), np.std(dataframe_ko.sex))

