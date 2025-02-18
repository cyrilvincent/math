import pandas as pd
import numpy as np

dataframe = pd.read_csv("data/heartdisease/data_with_nan.csv", na_values=".")
print(np.nanmean(dataframe.chol.values))
# Exercice 1
# Etudier le ration par colone nb_nan / nb_total : dataframe.chol.isnull().sum(), dataframe.chol.size
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
# Que pouvez vous en déduire
