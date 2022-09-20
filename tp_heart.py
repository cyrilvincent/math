import pandas as pd

# Import le fichier data/heart/data_with_nan.csv
# Afficher le describe

dataframe = pd.read_csv("data/heartdisease/data_with_nan.csv", na_values=".")
print(dataframe.describe())

# dataframe_ok = num == 0
# dataframe_ko = num == 1
# Refaire les describes sur les colonnes sex, age, chol, thalach