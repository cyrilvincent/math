import pandas as pd

# Charger le fichier csv dans pandas avec la colonne id comme index_col="id"
# describe
# y = dataframe.diagnosis
# x = dataframe dropper la colone diagnosis
# Créer 2 dataframes : benin => diagnosis = 0, malin => diagnosis = 1
# x.radius_mean.describe(), concave, texture

dataframe = pd.read_csv("data/breast-cancer/data.csv",index_col="id")
print(dataframe)