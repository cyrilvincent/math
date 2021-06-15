import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Installer openpyxl
dataframe = pd.read_csv("data/house/house.csv")
dataframe = pd.read_excel("data/house/house.xlsx")
with sqlite3.connect("data/house/house.db3") as db:
    dataframe = pd.read_sql("select * from house", db)
print(dataframe.loyer, dataframe["surface"])

loyer_per_m2 = dataframe.loyer / dataframe.surface
dataframe["loyer_per_m2"] = loyer_per_m2

dataframe.to_html("data/house/house.html", index=False)



print(dataframe.describe())



plt.scatter(dataframe.surface[dataframe.surface < 150], dataframe.loyer[dataframe.surface < 150])
plt.show()



