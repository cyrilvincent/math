# Charger data/heartdisease/dataclean.csv
# Moy, Std sur chol, thalach et age
# ko = dataframe[num == 1], ok = dataframe[num == 0]
# Recalculer moy, std sur les 3 features
# Reessayer la même chose en normalisant les data

import pandas as pd
import numpy as np

dataframe = pd.read_csv("data/heartdisease/dataclean.csv")
print(dataframe.describe().T)

ok = dataframe[dataframe.num == 0]
ko = dataframe[dataframe["num"] == 1]

print(ok.describe().T)
print(ko.describe().T)

chol_normalized = (dataframe.chol - np.mean(dataframe.chol)) / np.std(dataframe.chol)
print(chol_normalized.describe())