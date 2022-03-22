import pandas as pd
import sqlite3

#dataframe = pd.read_csv("data/house/house.csv")
#dataframe = pd.read_excel("data/house/house.xlsx", index_col="id")
with sqlite3.connect("data/house/house.db3") as conn:
    dataframe = pd.read_sql("select * from house", conn)
print(dataframe)
loyers_serie = dataframe.loyer
print(loyers_serie)

print(dataframe.describe().T)