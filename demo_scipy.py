import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt

df = pd.read_csv("data/house/house.csv")

slope, intercept, rvalue, pvalue, stderr = stats.linregress(df["surface"], df["loyer"])
print(slope, intercept, rvalue, pvalue, stderr)

def poly2(x, a, b, c):
    return a * x ** 2 + b * x + c

weights, conv = opt.curve_fit(poly2, df["surface"], df["loyer"])


x = np.arange(400)
y = x * slope + intercept
y2 = poly2(x, weights[0], weights[1], weights[2])

plt.scatter(df["surface"], df["loyer"])
plt.plot(x, y, color="red")
plt.plot(x, y2, color="black")
plt.show()