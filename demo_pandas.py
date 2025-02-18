import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("data/house/house.csv")
print(dataframe.describe())
loyers = dataframe["loyer"]
surfaces = dataframe.surface
plt.scatter(surfaces, loyers)
plt.show()
dataframe["loyers_m2"] = loyers / surfaces
dataframe.to_excel("data/house/house.xlsx")

