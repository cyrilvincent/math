import pandas as pd

dataframe = pd.read_csv("data/heartdisease/data_with_nan.csv", na_values=".")
dataframe = dataframe.drop(["slope", "ca", "thal"], axis=1)
dataframe = dataframe.dropna()
# Supprimer les colonne slope,ca,thal
# Effacer les lignes NaN
# Bonus : Remplacer les null par la moyenne de la colonne
# Sauvegarder le dataframe
print(dataframe)
dataframe.to_csv("data/heartdisease/dataclean.csv")