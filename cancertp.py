# Charger le dataframe breast-cancer/data.csv
# Virer la colonne id
# Filtrer par diagnosis
# Etudier ces 2 colonnes : radius_mean, concavity_worst (moyenne, ecart type)

import pandas as pd
import numpy as np

dataframe = pd.read_csv("data/breast-cancer/data.csv")

dataframe = dataframe.drop("id",1)

dataframeko = dataframe[dataframe.diagnosis == 1]
print(dataframeko.head())

dataframeok = dataframe[dataframe.diagnosis == 0]
print(dataframeok.head())

print(np.mean(dataframeko.radius_mean), np.std(dataframeko.radius_mean))
print(np.mean(dataframeok.radius_mean), np.std(dataframeok.radius_mean))

print(np.mean(dataframeko.concavity_worst), np.std(dataframeko.concavity_worst))
print(np.mean(dataframeok.concavity_worst), np.std(dataframeok.concavity_worst))