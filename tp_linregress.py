import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import scipy.optimize as opt

dico = np.load("data/house/house.npz")
loyers = dico["np_loyers"]
surfaces = dico["np_surfaces"]
df = pd.DataFrame()
df["loyers"] = loyers
df["surfaces"] = surfaces
print(df)
mean_loyers = np.mean(df["loyers"])
std_loyers = np.std(df["loyers"])

df = df[df["surfaces"] < 200]
df = df[df["loyers"] < mean_loyers + 3 * std_loyers]

def poly2(x, a, b, c):
    return a * x ** 2 + b * x + c

weight2, conv2 = opt.curve_fit(poly2, df["surfaces"], df["loyers"])
print(weight2)
print(conv2)



slope, intercept, rvalue, pvalue, stderr = stats.linregress(surfaces, loyers)
print(slope, intercept, rvalue)

x = np.arange(200)

plt.scatter(df["surfaces"], df["loyers"])
plt.plot(df["surfaces"], slope * df["surfaces"] + intercept, color="red")
plt.plot(x, poly2(x, weight2[0], weight2[1], weight2[2]), color="black")
plt.show()