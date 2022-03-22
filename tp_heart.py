# Traiter le fichier data/heartdisease/data_with_nan.csv
# read_csv(file, na_values=".")
# Supprimer les 3 colonnes slope,ca,thal
# Supprimer les lignes avec des nan
# Créer 2 dataframe : ok_df, ko_df en fonction du num
# Faites un describe sur les 2 dataframes => conclusion

import pandas as pd

dataframe = pd.read_csv("data/heartdisease/data_with_nan.csv", na_values=".")
dataframe = dataframe.drop(["slope", "ca"], axis=1).drop("thal", axis=1)
dataframe = dataframe.dropna()
print(dataframe)

dataframe.to_csv("data/heartdisease/dataclean.csv", index=False )
dataframe.to_html("data/heartdisease/dataclean.html", index=False)

ok_df = dataframe[dataframe.num == 0]
ko_df = dataframe[dataframe.num == 1]



print(ok_df.describe().T)
print(ko_df.describe().T)