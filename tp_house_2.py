import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

dataframe = pd.read_csv("data/house/house.csv")
dataframe = dataframe[dataframe.surface < 200]
slope, intercept, r_value, p_value, mse = stats.linregress(dataframe.surface, dataframe.loyer)
print(slope, intercept, r_value, p_value, mse)

f = lambda x: slope * x + intercept

plt.scatter(dataframe.surface, dataframe.loyer)
plt.plot(np.arange(200), f(np.arange(200)), color="red")
plt.show()