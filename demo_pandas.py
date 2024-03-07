import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataframe = pd.read_csv("data/house/house.csv")
# dataframe = pd.read_excel("data/house/house.xlsx") # pip install openpyxl
loyer = dataframe["loyer"]
surface = dataframe.surface
dataframe["loyer_per_m2"] = loyer / surface
print(dataframe.describe())
dataframe.to_json("data/house/house.json",indent=2)

dataframe = dataframe.drop("loyer_per_m2", axis=1)
print(dataframe)

dataframe = dataframe[dataframe.surface < 200]


plt.scatter(dataframe.surface, dataframe.loyer)
plt.show()



