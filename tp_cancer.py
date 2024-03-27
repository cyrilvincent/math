import pandas as pd

dataframe = pd.read_csv("data/breast-cancer/data.csv", index_col="id")
print(dataframe)