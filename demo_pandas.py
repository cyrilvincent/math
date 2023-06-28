import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

dataframe = pd.read_csv("data/house/house.csv")
# dataframe = pd.read_excel("data/house/house.xlsx", sheet_name=1)
print(dataframe)
dataframe = dataframe[dataframe.surface < 200]
loyers = dataframe.loyer
surfaces = dataframe["surface"]
print(dataframe.describe().T)
dataframe["loyers_m2"] = loyers / surfaces
dataframe.to_excel("data/house/house.xlsx")
dataframe.to_html("data/house/house.html", index=False)
plt.scatter(surfaces, loyers)
plt.show()