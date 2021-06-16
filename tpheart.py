import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

dataframe = pd.read_csv("data/heartdisease/data_cleaned_up.csv")
y = dataframe.num
x = dataframe.drop("num", 1)

benin_filter = y == 0
malin_filter = y == 1

print(x[benin_filter].chol.describe())
print(x[malin_filter].chol.describe())

print(x[benin_filter].sex.describe())
print(x[malin_filter].sex.describe())

slope, intercept, r_value, p_value, std_err = stats.linregress(x.age, x.chol)
print(slope, intercept, r_value)
f = lambda x: slope * x + intercept

plt.scatter(x.age, x.chol)
plt.plot(np.arange(28,66), f(np.arange(28,66)))
plt.show()
