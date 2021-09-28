import pandas as pd

dataframe = pd.read_csv("data/house/house.csv",index_col="id")
#dataframe = pd.read_excel("data/house/house.xlsx")
print(dataframe)
print(dataframe[dataframe.surface < 100])

print(dataframe.describe())

dataframe_filtre = dataframe[dataframe.surface < 200]
dataframe_filtre.to_excel("data/house/house2.xlsx")

