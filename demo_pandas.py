import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataframe = pd.read_csv("data/house/house.csv")
print(dataframe.describe())
loyers = dataframe["loyer"]
surfaces = dataframe.surface
plt.scatter(surfaces, loyers)
plt.show()
dataframe["loyers_m2"] = loyers / surfaces
dataframe.to_excel("data/house/house.xlsx")

a1 = np.array([1,np.nan,3,4])
print(np.nansum(a1))
