import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import numpy as np

# Installer openpyxl
dataframe = pd.read_csv("data/house/house.csv")
dataframe = pd.read_excel("data/house/house.xlsx")
with sqlite3.connect("data/house/house.db3") as db:
    dataframe = pd.read_sql("select * from house", db)
print(dataframe.loyer, dataframe["surface"])

loyer_per_m2 = dataframe.loyer / dataframe.surface
dataframe["loyer_per_m2"] = loyer_per_m2

dataframe.to_html("data/house/house.html", index=False)

bidule = np.sqrt(dataframe.loyer ** 2 + dataframe.surface)

f = lambda x : np.sqrt(x.loyer ** 2 + x.surface)
bidule = f(dataframe)
print(bidule)

# import mymodule
# f2 = lambda x: mymodule.is_prime(x)
# print(dataframe[f2(dataframe.loyer.values.astype(int))].loyer)


print(dataframe.describe())

print(np.median(dataframe.loyer), np.mean(dataframe.loyer))
print(np.quantile(dataframe.loyer, 0.25), np.quantile(dataframe.loyer, 0.75), np.mean(dataframe.loyer))

plt.scatter(dataframe.surface[dataframe.surface < 150], dataframe.loyer[dataframe.surface < 150])
plt.show()



