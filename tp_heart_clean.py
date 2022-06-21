import pandas as pd

dataframe = pd.read_csv("data/heartdisease/data_with_nan.csv", na_values=".")
nbnan dataframe.isnull().sum()
# Effacer les lignes NaN
# Bonus : Remplacer les null par la moyenne de la colonne
# Sauvegarder le dataframe
print(dataframe)