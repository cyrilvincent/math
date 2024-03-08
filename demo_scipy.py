# pip install scipy
import scipy
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
print(scipy.__version__)

dataframe = pd.read_csv("data/house/house.csv")
std = np.std(dataframe.loyer)
avg = np.mean(dataframe.loyer)
dataframe = dataframe[dataframe.surface < 200]
dataframe = dataframe[dataframe.loyer < avg + 3 * std]
plt.scatter(dataframe.surface, dataframe.loyer)
slope, intercept, rvalue, pvalue, stderr = stats.linregress(dataframe.surface, dataframe.loyer)
print(slope, intercept, rvalue, pvalue, stderr)
x = np.arange(11,200)
y = slope * x + intercept # model = 30.4*surface + 274.6
plt.plot(x, y, color="red")
plt.show()

