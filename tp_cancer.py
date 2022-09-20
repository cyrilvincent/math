import numpy as np
import pandas as pd

# Charger data/breast-cancer/data.csv
# Virer la colonne id
# dataframe_ok = diagnosis == 0
# dataframe_ko = diagnosis == 1
# Sur la colonne perimeter_worst calculer mean, std, mediane et quartile pour les 2 dataframes

print(f"{np.pi:.2f}")
dataframe = pd.read_csv("data/breast-cancer/data.csv", index_col="id")
dataframe_ok = dataframe[dataframe.diagnosis == 0]
dataframe_ko = dataframe[dataframe.diagnosis == 1]
print(np.mean(dataframe_ok.perimeter_worst), np.std(dataframe_ok.perimeter_worst), np.median(dataframe_ok.perimeter_worst))
print(np.mean(dataframe_ko.perimeter_worst), np.std(dataframe_ko.perimeter_worst), np.median(dataframe_ko.perimeter_worst))

print(np.quantile(dataframe_ok.perimeter_worst, [0.25,0.75]), np.quantile(dataframe_ko.perimeter_worst, [0.25,0.75]))
