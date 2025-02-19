import pandas as pd
import numpy as np

dataframe = pd.read_csv("data/heartdisease/data_with_nan.csv", na_values=".")
print(np.nanmean(dataframe.chol.values))
# Exercice 1
# Etudier le ratio par colonne nb_nan / nb_total : dataframe.chol.isnull().sum(), dataframe.chol.size
# Si le ratio > 50% virer la colonne
# Si le ratio < 5% virer la ligne
# Sinon remplacer le nan par la moyenne (bonus + rnd * std)
# Sauvegarder le dataframe filtrer dans dataclean.csv
#
# Exercice 2
# Sur dataclean
# Créer le dataframe ok pour num==0
# Créer le dataframe ko pour num==1
# Faire des stats sur les colonnes age, chol, thalach
# Que pouvez vous en déduire ?

print(dataframe.chol.size, dataframe.isnull().sum())
ratio_slope = dataframe.fbs.isnull().sum() / dataframe.fbs.size
print(ratio_slope)
dataframe = dataframe.drop(["slope", "ca", "thal"], axis=1)
mean_chol = np.nanmean(dataframe.chol.values)
std_chol = dataframe.chol.std()
print(mean_chol, std_chol)
dataframe.chol = dataframe.chol.fillna(mean_chol + (np.random.rand() - 0.5) * std_chol * 2)
dataframe = dataframe.dropna()
dataframe.to_csv("data/heartdisease/dataclean.csv")

# def increment(x):
#     return x + 1
#
# dataframe.chol.apply(increment)
# increment(dataframe.values)

ok = dataframe[dataframe.num == 0]
ko = dataframe[dataframe.num == 1]

print(ok.chol.describe())
print(ko.chol.describe())

print(ok.age.describe())
print(ko.age.describe())

print(ok.thalach.describe())
print(ko.thalach.describe())



