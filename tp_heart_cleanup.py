import pandas as pd
import numpy as np

df = pd.read_csv("data/heartdisease/data_with_nan.csv", na_values=["", "."])
print(df)

# 1 Compter les nan => isnull().sum()
# 2 Les colonnes avec > 50% de nan: dropper les colonnes
# 3 les colonnes avec >2% de nan: remplacer la valeur par mean + bruit : 11.11
# 4 les colonnes avec < 2% de nan: dropper les lignes avec des nan : dropna()
# Save