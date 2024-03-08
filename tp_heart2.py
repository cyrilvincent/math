# Tester demo_house
# Charger data_cleaned_up.csv
# Faire un describe
# créer le dataset ok = [num == 0]
# Créer le dataset ko = [num == 1]
# Calculer les mean, std sur chol, age, sex
# Correction 15h55

import pandas as pd
import numpy as np

dataframe = pd.read_csv("data/heartdisease/data_with_nan.csv", na_values=".")
# Dropper les colonnes ca, thal et num
# Dropper les lignes na
# Sauvegarder dans dataclean.csv
print(dataframe)
print(dataframe.describe().T)
ok = dataframe[dataframe.num == 0]
ko = dataframe[dataframe.num == 1]
print(ok.describe().T)
print(ko.describe().T)
print(ok.chol.isnull().sum())
print(ko.chol.isnull().sum())


dataframe_clean = dataframe.drop(["ca", "thal", "slope"])

# Eventuellement
mean = dataframe.chol.mean()
std = dataframe.chol.std()
ok.chol.fillna(mean + (np.random.rand() - 0.5) * 2 * std, inplace=True)
ko.chol.fillna(mean + (np.random.rand() - 0.5) * 2 * std, inplace=True)

dataframe = dataframe.dropna()
dataframe.to_csv("dataclean.csv")



