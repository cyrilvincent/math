import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data/house/house.csv")

slope, intercept, rvalue, pvalue, stderr = stats.linregress(df["surface"], df["loyer"])
print(slope, intercept, rvalue, pvalue, stderr)

x = np.arange(400)
y = x * slope + intercept

plt.scatter(df["surface"], df["loyer"])
plt.plot(x, y, color="red")
plt.show()