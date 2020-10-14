# Charger data.csv avec id comme index
# Filtrer diagnosis == 1 => malade et == 0
# Tester la moyenne pour radius_mean
# et concavity_worst

import pandas
import numpy as np

dataframe = pandas.read_csv("data/breast-cancer/data.csv", index_col="id")

dataframe_ko = dataframe[dataframe.diagnosis == 1]
dataframe_ok = dataframe[dataframe.diagnosis == 0]

print(np.mean(dataframe_ok.radius_mean), np.mean(dataframe_ko.radius_mean))
print(np.mean(dataframe_ok.concavity_worst), np.mean(dataframe_ko.concavity_worst))
