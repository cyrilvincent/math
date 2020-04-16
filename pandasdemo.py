import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sqlite3

#dataframe = pd.read_csv("data/house/house.csv")
with sqlite3.connect("data/house/house.db3") as conn:
    dataframe = pd.read_sql('select loyer,surface from house', conn)

dataframe = dataframe[np.abs((41 * dataframe.surface - 283) - dataframe.loyer) < 3 * np.std(dataframe.loyer)]

plt.scatter(dataframe.surface, dataframe.loyer)
plt.show()
