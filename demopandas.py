import pandas
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

#dataframe = pandas.read_csv("data/house/house.csv")
dataframe = pandas.read_excel("data/house/house.xlsx",0)
dataframe.to_json("data/house/house.json")

plt.scatter(dataframe.surface[dataframe.surface < 150], dataframe.loyer[dataframe.surface < 150])
plt.show()