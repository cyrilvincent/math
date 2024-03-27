import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

dataframe = pd.read_csv("data/house/house.csv")
dataframe = dataframe[dataframe.surface < 200]

mean = np.mean(dataframe.loyer)
std = np.std(dataframe.loyer)
dataframe = dataframe[dataframe.loyer < mean + 3 * std]
print(mean, std)

slope, intercept, rvalue, pvalue, stderr = stats.linregress(dataframe.surface, dataframe.loyer)
print(slope, intercept, rvalue, pvalue, stderr )

f = lambda x: slope * x + intercept
x = np.arange(200)

plt.scatter(dataframe.surface, dataframe.loyer)
plt.plot(x, f(x), color="red")
plt.show()



