# Charger data/breast-cancer/data.csv
#la colonne index = id
#ok_df, ko_df en fonction de diagnosis 1=malade
#radius_worst, area_worst => describe
# calculer np.mean, std, media, quartile
import pandas as pd
import numpy as np

dataframe = pd.read_csv("data/breast-cancer/data.csv",index_col="id",na_values=".")
print(dataframe)

benin = dataframe[dataframe.diagnosis == 0]
malin = dataframe[dataframe.diagnosis != 0]

print(np.mean(benin.radius_worst), np.median(benin.radius_worst), np.std(benin.radius_worst), np.quantile(benin.radius_worst, [0.25, 0.75]))
print(np.mean(malin.radius_worst), np.median(malin.radius_worst), np.std(malin.radius_worst), np.quantile(malin.radius_worst, [0.25, 0.75]))