import pandas as pd
import matplotlib.pyplot as plt
# pip install openpyxl

dataframe = pd.read_csv("data/house/house.csv")
dataframe = dataframe[dataframe.surface < 200]
dataframe["loyer_per_m2"] = dataframe.loyer / dataframe.surface
#dataframe = pd.read_excel("data/house/house.xlsx")
print(dataframe)

dataframe.to_html("data/house/house.html")
dataframe.to_json("data/house.house.json")

print(dataframe.describe().T)

plt.scatter(dataframe["surface"], dataframe.loyer)
plt.show()

