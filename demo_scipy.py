import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data/jena/jena_filtered.csv")
temp = df["T (degC)"]
x = np.arange(len(temp[12::24]))

slope, intercept, rvalue, pvalue, stderr = stats.linregress(x, temp[12::24])
print(slope, intercept, rvalue, pvalue)

def f(x, slope, intercept):
    return slope * x + intercept

plt.plot(x, temp[12::24])
plt.plot(x, f(x, slope, intercept), color="red")
plt.show()

# Faire une regression lineaire sur house


